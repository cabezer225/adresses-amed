"""Build the notes spreadsheet and the site data for « Les adresses d'Amed ».

  python3 scripts/construire_guide.py tableau            data/lieux.json -> data/tableau-notes.xlsx
  python3 scripts/construire_guide.py site NOTES.xlsx    data/lieux.json + Google Sheets export -> data/guide.json

data/lieux.json is the collected structure (places, visits, videos). The spreadsheet is where Amed adds
scores, prices, reviews and fixes; for the dishes of a visit, the spreadsheet rows win over lieux.json.
"""
import datetime as dt
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tableur import ecrire_xlsx, lire_xlsx  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
LIEUX = ROOT / "data" / "lieux.json"
GUIDE = ROOT / "data" / "guide.json"
GEOCACHE = ROOT / "data" / "geocache.json"
TABLEAU = ROOT / "data" / "tableau-notes.xlsx"

CATEGORIES = {
    "fast-food": "Fast-food & restos",
    "patisserie-glacier": "Pâtisseries & glaces",
    "street-food-etranger": "Street food à l'étranger",
}
CAT_BY_LABEL = {v.lower(): k for k, v in CATEGORIES.items()}
TYPES = {"chaine": "Chaîne", "independant": "Indépendant"}
TYPE_BY_LABEL = {"chaîne": "chaine", "chaine": "chaine", "indépendant": "independant", "independant": "independant", "indé": "independant"}
NETS = ("tiktok", "instagram", "youtube")

LIEUX_COLS = ["ID", "Lieu", "Catégorie", "Spécialité", "Type", "Ville", "Adresse", "Mon avis", "Points forts", "Points faibles", "Afficher"]
PLATS_COLS = ["ID lieu", "Lieu", "Date visite", "Visite", "Plat", "Prix (€)", "Note /10", "Vidéo"]


def charger_lieux():
    return json.loads(LIEUX.read_text(encoding="utf-8"))


def cmd_tableau():
    lieux = charger_lieux()
    aide = [
        ["Mode d'emploi"],
        ["1. Onglet « Plats » : une ligne par plat goûté. Remplis la note sur 10 (ex. 7,5) et le prix si tu l'as. Corrige le nom du plat si besoin."],
        ["2. Une visite sans plat listé a une ligne « (à compléter) » : remplace-la par tes plats. Pour ajouter un plat, copie une ligne de la même visite (même ID lieu et même date)."],
        ["3. Onglet « Lieux » : écris ton avis en 1 ou 2 phrases, tes points forts et faibles séparés par « ; », et l'adresse des indépendants si tu la connais."],
        ["4. Colonne « Afficher » : mets « non » pour retirer une adresse du guide (vidéo hors sujet, resto fermé…)."],
        ["5. La note d'un resto est la moyenne de ses plats notés. Un plat sans note n'est pas compté."],
        ["6. Ne change pas la colonne ID. Quand tu as fini (même en partie), dis-le à Claude : il met le site à jour."],
    ]
    rows_l = [LIEUX_COLS]
    rows_p = [PLATS_COLS]
    for l in sorted(lieux, key=lambda x: (x.get("categorie", ""), x["nom"].lower())):
        rows_l.append([
            l["id"], l["nom"], CATEGORIES.get(l.get("categorie"), l.get("categorie") or ""), l.get("specialite") or "",
            TYPES.get(l.get("type"), ""), l.get("ville") or "", l.get("adresse") or "", l.get("avis") or "",
            "; ".join(l.get("points_forts") or []), "; ".join(l.get("points_faibles") or []), "non" if l.get("masquer") else "oui",
        ])
        for v in sorted(l.get("visites", []), key=lambda x: x.get("date") or "", reverse=True):
            url = next((x["url"] for n in NETS for x in v.get("videos", []) if x["platform"] == n), "")
            plats = v.get("plats") or [{"nom": "(à compléter)"}]
            for p in plats:
                rows_p.append([l["id"], l["nom"], v.get("date") or "", v.get("titre") or "", p.get("nom") or "",
                               p.get("prix") if p.get("prix") is not None else "", p.get("note") if p.get("note") is not None else "", url])
    feuilles = [
        ("Plats", rows_p, [16, 22, 12, 30, 34, 10, 10, 46]),
        ("Lieux", rows_l, [16, 22, 22, 18, 13, 16, 30, 50, 34, 34, 10]),
    ]
    questions = ROOT / "data" / "a-verifier.json"
    if questions.exists():
        rows_q = [["Sujet", "Question", "Ta réponse"]] + [q + [""] for q in json.loads(questions.read_text(encoding="utf-8"))]
        feuilles.append(("À vérifier", rows_q, [44, 80, 50]))
    feuilles.append(("Mode d'emploi", aide, [120]))
    ecrire_xlsx(TABLEAU, feuilles)
    print(f"{TABLEAU.relative_to(ROOT)} : {len(rows_l) - 1} lieux, {len(rows_p) - 1} lignes de plats")


def nombre(s):
    s = str(s or "").strip().replace("€", "").replace(",", ".").replace(" ", "").replace(" ", "")
    if not s:
        return None
    try:
        return round(float(s), 2)
    except ValueError:
        return None


def date_iso(s):
    s = str(s or "").strip()
    if not s:
        return ""
    if s.replace(".", "", 1).isdigit():  # Sheets serial date
        return (dt.date(1899, 12, 30) + dt.timedelta(days=int(float(s)))).isoformat()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d/%m/%y"):
        try:
            return dt.datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            pass
    return s


def table(rows, cols):
    header = [h.strip() for h in rows[0]] if rows else []
    idx = {c: header.index(c) for c in cols if c in header}
    out = []
    for r in rows[1:]:
        if not any(str(x).strip() for x in r):
            continue
        out.append({c: (r[i].strip() if i < len(r) and isinstance(r[i], str) else (r[i] if i < len(r) else "")) for c, i in idx.items()})
    return out


def geocoder(requete, cache):
    if requete in cache:
        return cache[requete]
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode({"q": requete, "format": "json", "limit": 1})
    req = urllib.request.Request(url, headers={"User-Agent": "les-adresses-d-amed/1.0 (guide fast-food)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            res = json.load(r)
        cache[requete] = [round(float(res[0]["lat"]), 6), round(float(res[0]["lon"]), 6)] if res else None
    except Exception as e:  # network errors leave the pin out rather than failing the build
        print(f"  géocodage impossible pour « {requete} » : {e}")
        return None
    time.sleep(1.1)  # Nominatim usage policy: at most 1 request per second
    return cache[requete]


def cmd_site(xlsx):
    lieux = {l["id"]: l for l in charger_lieux()}
    feuilles = lire_xlsx(xlsx)
    lignes_l = table(feuilles.get("Lieux", []), LIEUX_COLS)
    lignes_p = table(feuilles.get("Plats", []), PLATS_COLS)

    for row in lignes_l:
        l = lieux.get(row.get("ID"))
        if not l:
            print(f"  lieu inconnu dans l'onglet Lieux : {row.get('ID')} — ignoré")
            continue
        l["nom"] = row.get("Lieu") or l["nom"]
        l["categorie"] = CAT_BY_LABEL.get((row.get("Catégorie") or "").lower(), l.get("categorie"))
        l["specialite"] = row.get("Spécialité") or None
        l["type"] = TYPE_BY_LABEL.get((row.get("Type") or "").lower(), l.get("type"))
        l["ville"] = row.get("Ville") or None
        l["adresse"] = row.get("Adresse") or None
        l["avis"] = row.get("Mon avis") or None
        l["points_forts"] = [x.strip() for x in (row.get("Points forts") or "").split(";") if x.strip()]
        l["points_faibles"] = [x.strip() for x in (row.get("Points faibles") or "").split(";") if x.strip()]
        l["masquer"] = (row.get("Afficher") or "oui").strip().lower() in ("non", "no", "n")

    # Dishes: the spreadsheet rows replace the dishes of each (place, date) visit they mention.
    par_visite = {}
    for row in lignes_p:
        key = (row.get("ID lieu"), date_iso(row.get("Date visite")))
        par_visite.setdefault(key, []).append(row)
    for (lid, date), rows in par_visite.items():
        l = lieux.get(lid)
        if not l:
            print(f"  lieu inconnu dans l'onglet Plats : {lid} — ignoré")
            continue
        v = next((x for x in l.setdefault("visites", []) if x.get("date") == date), None)
        if v is None:
            v = {"date": date, "titre": rows[0].get("Visite") or "Visite", "videos": []}
            l["visites"].append(v)
        if rows[0].get("Visite"):
            v["titre"] = rows[0]["Visite"]
        v["plats"] = [
            {"nom": r["Plat"], "prix": nombre(r.get("Prix (€)")), "note": nombre(r.get("Note /10"))}
            for r in rows if r.get("Plat") and r["Plat"] != "(à compléter)"
        ]

    cache = json.loads(GEOCACHE.read_text(encoding="utf-8")) if GEOCACHE.exists() else {}
    publies = []
    for l in lieux.values():
        if l.get("masquer"):
            continue
        if l.get("adresse") and not l.get("coords"):
            l["coords"] = geocoder(l["adresse"], cache)
        for v in l.get("visites", []):
            if v.get("adresse") and not v.get("coords"):
                v["coords"] = geocoder(v["adresse"], cache)
        publies.append({k: val for k, val in l.items() if k != "masquer"})
    GEOCACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")

    guide = {"meta": {"maj": dt.date.today().isoformat(), "categories": CATEGORIES}, "lieux": publies}
    GUIDE.write_text(json.dumps(guide, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    notes = sum(1 for l in publies for v in l.get("visites", []) for p in v.get("plats", []) if p.get("note") is not None)
    print(f"{GUIDE.relative_to(ROOT)} : {len(publies)} lieux publiés, {notes} plats notés")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "tableau":
        cmd_tableau()
    elif len(sys.argv) >= 3 and sys.argv[1] == "site":
        cmd_site(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(1)
