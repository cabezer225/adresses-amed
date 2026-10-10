"""Apply the scores, prices and reviews heard in Amed's videos (data/verif/notes-*-resultat-*.json) to data/lieux.json.

A score is kept only when the quoted words actually contain it (or its /20 equivalent); a price only when its
quote contains a number. Scores Amed typed himself in the spreadsheet always win. New places heard in a video
are listed for review, not created.
"""
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERIF = ROOT / "data" / "verif"
LIEUX = ROOT / "data" / "lieux.json"


def norm(s):
    s = unicodedata.normalize("NFD", str(s or "").lower())
    return re.sub(r"[^a-z0-9]+", " ", "".join(c for c in s if unicodedata.category(c) != "Mn")).strip()


def nombres(txt):
    return {float(x.replace(",", ".")) for x in re.findall(r"\d+(?:[.,]\d+)?", txt or "")}


def note_valide(note, citation):
    if not isinstance(note, (int, float)) or not 0 <= note <= 10:
        return False
    vus = nombres(citation)
    demi = "demi" in (citation or "").lower() and float(int(note)) in vus and note - int(note) == 0.5
    return any(abs(n - note) < 1e-6 or abs(n - note * 2) < 1e-6 for n in vus) or demi


def prix_valide(prix, citation):
    return isinstance(prix, (int, float)) and 0 < prix < 500 and bool(nombres(citation))


def plateforme(url):
    return "youtube" if "youtu" in url else "tiktok" if "tiktok" in url else "instagram"


def main():
    lieux = {l["id"]: l for l in json.loads(LIEUX.read_text(encoding="utf-8"))}
    raw = {}
    for f in ("youtube", "tiktok", "tiktok-anciennes", "instagram"):
        p = ROOT / "data" / "raw" / f"{f}.json"
        if p.exists():
            for x in json.loads(p.read_text(encoding="utf-8")):
                raw[x["url"]] = x
    stats = {"videos": 0, "tests": 0, "notes": 0, "notes_rejetees": 0, "prix": 0, "avis": 0, "visites_creees": 0, "adresses": 0}
    nouveaux = []

    fichiers = sorted(VERIF.glob("notes-long-resultat-*.json")) + sorted(VERIF.glob("notes-tt-resultat-*.json"))
    for f in fichiers:
        try:
            entrees = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"  fichier illisible, ignoré : {f.name}")
            continue
        for e in entrees:
            url = e.get("video")
            if not url:
                continue
            stats["videos"] += 1
            for t in e.get("tests") or []:
                l = lieux.get(t.get("lieu_id") or "")
                if not l:
                    if t.get("lieu_nom"):
                        nouveaux.append({"lieu": t["lieu_nom"], "video": url, "plats": [p.get("nom") for p in t.get("plats") or []]})
                    continue
                stats["tests"] += 1
                v = next((x for x in l["visites"] if any(y["url"] == url for y in x["videos"])), None)
                if v is None:
                    r = raw.get(url, {})
                    v = {"date": r.get("date") or e.get("date") or "", "titre": (e.get("titre") or r.get("texte") or "Visite")[:80],
                         "partenariat": None, "plats": [], "videos": [{"platform": plateforme(url), "url": url}]}
                    l["visites"].append(v)
                    stats["visites_creees"] += 1

                plats = []
                for p in t.get("plats") or []:
                    if not p.get("nom"):
                        continue
                    note = p.get("note")
                    if note is not None and not note_valide(note, p.get("citation_note")):
                        stats["notes_rejetees"] += 1
                        note = None
                    prix = p.get("prix") if prix_valide(p.get("prix"), p.get("citation_prix")) else None
                    plats.append({"nom": p["nom"].strip(), "prix": prix, "note": note, "source": "video"})
                    stats["notes"] += note is not None
                    stats["prix"] += prix is not None

                # Keep what Amed typed in the spreadsheet; otherwise the video's precise list replaces caption guesses.
                saisis = {norm(p["nom"]): p for p in v["plats"] if p.get("note") is not None and p.get("source") != "video"}
                if plats:
                    fusion = []
                    for p in plats:
                        s = saisis.pop(norm(p["nom"]), None)
                        fusion.append(s or p)
                    v["plats"] = fusion + list(saisis.values())

                ng = t.get("note_globale")
                if ng is not None and note_valide(ng, t.get("citation_note_globale")):
                    v["note_globale"] = ng
                if t.get("avis") and not v.get("avis"):
                    v["avis"] = t["avis"].strip()
                    stats["avis"] += 1
                for champ in ("points_forts", "points_faibles"):
                    if t.get(champ):
                        actuels = l.get(champ) or []
                        for x in t[champ]:
                            if len(actuels) < 4 and norm(x) not in {norm(a) for a in actuels}:
                                actuels.append(x.strip())
                        l[champ] = actuels
                cite = t.get("adresse_ou_ville_citee")
                if isinstance(cite, dict):
                    cite = ", ".join(x for x in (cite.get("adresse"), cite.get("ville")) if x)
                if cite and l.get("type") == "independant" and not l.get("adresse") and re.search(r"\d", cite):
                    l["adresse"] = cite.strip()
                    l.pop("coords", None)
                    stats["adresses"] += 1

    # A place's review is the one from its most recent visit that has one, unless Amed wrote his own.
    for l in lieux.values():
        if not l.get("avis"):
            avec = sorted((v for v in l["visites"] if v.get("avis")), key=lambda v: v.get("date") or "", reverse=True)
            if avec:
                l["avis"] = avec[0]["avis"]

    LIEUX.write_text(json.dumps(list(lieux.values()), ensure_ascii=False, indent=1), encoding="utf-8")
    (VERIF / "nouveaux-lieux-entendus.json").write_text(json.dumps(nouveaux, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{stats} · nouveaux lieux entendus : {len(nouveaux)}")


if __name__ == "__main__":
    main()
