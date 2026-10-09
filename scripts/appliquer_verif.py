"""Apply the subagents' verification results (data/verif/) to data/lieux.json.

Run `python3 scripts/construire_guide.py site` first so the latest spreadsheet edits are in lieux.json,
then this script, then `construire_guide.py tableau` and `construire_guide.py site data/tableau-notes.xlsx`.

Rules, chosen so the public guide never shows a wrong address:
- names, types, specialities and cities are taken from every result that is not low confidence;
- an address is kept when confidence is high, or medium with no sign of doubt in the note;
- unnamed places are only renamed or merged at high or medium confidence;
- Amed's own corrections (corrections-amed.json) win over everything.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERIF = ROOT / "data" / "verif"
LIEUX = ROOT / "data" / "lieux.json"

DOUTE = ("homonyme", "suppos", "hypoth", "pas pu", "deviné", "douteu", "à confirmer", "non confirm", "pas confirm", "rien ne prouve", "aucune preuve", "non prouvé")
PREUVE_AMED = ("légende d'amed", "légende d’amed", "géotag", "tag de lieu", "tagué par amed", "lieu tagué", "description de la vidéo", "description youtube", "bio")
OK = ("haute", "moyenne")

# Decisions taken from the agents' evidence when two results disagreed.
DECISIONS = [
    {"id": "le-four", "nom": "Le Four 2.0"},  # same TikTok account @lefour92600 and same address in Asnières
]


def adresse_sure(r):
    if not r.get("adresse") or r.get("confiance") not in OK:
        return False
    if r["confiance"] == "haute":
        return True
    txt = (r.get("remarque") or "").lower() + " " + (r.get("source") or "").lower()
    return not any(k in txt for k in DOUTE) or any(k in txt for k in PREUVE_AMED)


def ids_cites(rem, lieux):
    """Place ids quoted in a note: hyphenated ids anywhere, single-word ids only inside a parenthesis or after « catalogue »."""
    zones = re.findall(r"\(([^)]*)\)", rem) + re.findall(r"catalogue\s*:?([^.)]*)", rem)
    found = set(re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)+", rem))
    for z in zones:
        found |= set(re.findall(r"[a-z0-9]{3,}", z))
    return sorted(i for i in found if i in lieux)


def fusionner_visites(cible, visites, avec_plats=True):
    for v in visites:
        v = json.loads(json.dumps(v))
        if not avec_plats:
            v["plats"] = []
        same = next((x for x in cible["visites"] if x.get("date") == v.get("date") and x.get("titre") == v.get("titre")), None)
        if same:
            urls = {x["url"] for x in same["videos"]}
            same["videos"] += [x for x in v["videos"] if x["url"] not in urls]
            noms = {p["nom"] for p in same["plats"]}
            same["plats"] += [p for p in v["plats"] if p["nom"] not in noms]
        else:
            cible["visites"].append(v)


def appliquer_champs(l, r):
    if r.get("confiance") not in OK:
        return
    if r.get("nom"):
        l["nom"] = r["nom"]
    if r.get("type") in ("chaine", "independant"):
        l["type"] = r["type"]
    if r.get("specialite"):
        l["specialite"] = r["specialite"]
    if r.get("ville") or l.get("type") == "chaine":
        l["ville"] = r.get("ville") or l.get("ville")
    if l.get("type") == "chaine":
        l["adresse"] = None
    elif adresse_sure(r):
        l["adresse"] = r["adresse"]
        l.pop("coords", None)
    if r.get("statut") == "ferme-definitivement" and r.get("confiance") in OK:
        l["statut"] = "ferme-definitivement"


def main():
    lieux = {l["id"]: l for l in json.loads(LIEUX.read_text(encoding="utf-8"))}
    resultats = [r for f in sorted(VERIF.glob("resultat-*.json")) for r in json.loads(f.read_text(encoding="utf-8"))]
    absorbe_par = {}  # merged place id -> id of the place that absorbed it (to keep its logo)
    stats = {"maj": 0, "adresses": 0, "renommes": 0, "fusions": 0, "rattachements": 0, "ignores": 0}

    for r in resultats:
        l = lieux.get(r["id"])
        if not l:
            continue
        action = r.get("action")
        if action in ("garder", "renommer"):
            avant = l.get("adresse")
            appliquer_champs(l, r)
            stats["maj"] += 1
            stats["adresses"] += bool(l.get("adresse") and l.get("adresse") != avant)
            if action == "renommer" and r.get("confiance") in OK:
                l["masquer"] = False
                stats["renommes"] += 1
        elif action == "fusionner":
            cible = lieux.get(r.get("fusionner_avec") or "")
            if not cible or r.get("confiance") not in OK or cible is l:
                stats["ignores"] += 1
                continue
            fusionner_visites(cible, l["visites"])
            if not cible.get("adresse") and cible.get("type") != "chaine" and adresse_sure(r):
                cible["adresse"] = r["adresse"]
            if not cible.get("ville") and r.get("ville") and cible.get("type") != "chaine":
                cible["ville"] = r["ville"]
            # Comparison videos: also attach the visit (without dishes) to the other catalogue places the note cites.
            if r.get("confiance") == "haute":
                for autre in ids_cites(r.get("remarque") or "", lieux):
                    if lieux[autre] is not cible and lieux[autre] is not l and not lieux[autre].get("masquer"):
                        fusionner_visites(lieux[autre], l["visites"], avec_plats=False)
                        stats["rattachements"] += 1
            absorbe_par[l["id"]] = cible["id"]
            del lieux[l["id"]]
            stats["fusions"] += 1

    questions = VERIF / "reponses-questions.json"
    if questions.exists():
        for q in json.loads(questions.read_text(encoding="utf-8")):
            for f in q.get("fusions") or []:
                cible = lieux.get(f.get("garder"))
                for src in f.get("absorber") or []:
                    if cible and src in lieux and lieux[src] is not cible:
                        fusionner_visites(cible, lieux[src]["visites"])
                        absorbe_par[src] = cible["id"]
                        del lieux[src]
                        stats["fusions"] += 1
            for rid in q.get("retirer") or []:
                if rid in lieux:
                    lieux[rid]["masquer"] = True

    for d in DECISIONS:
        if d["id"] in lieux:
            lieux[d["id"]].update({k: v for k, v in d.items() if k != "id"})

    # Logos found by the logo agents (only when the file exists and confidence is not low).
    logos = 0
    for f in sorted(VERIF.glob("logos-resultat-*.json")):
        for r in json.loads(f.read_text(encoding="utf-8")):
            rid = r.get("id")
            l = lieux.get(rid) or lieux.get(absorbe_par.get(rid, ""))
            if not l or not r.get("logo") or r.get("confiance") not in OK or not (ROOT / r["logo"]).exists():
                continue
            if rid in lieux or not l.get("logo"):  # a merged place's logo only fills a gap
                l["logo"] = r["logo"]
                logos += 1

    corrections = VERIF / "corrections-amed.json"
    if corrections.exists():
        for c in json.loads(corrections.read_text(encoding="utf-8")):
            l = lieux.get(c["id"])
            if l:
                l.update({k: v for k, v in c.items() if k not in ("id", "remarque")})
                if "adresse" in c:
                    l.pop("coords", None)

    out = sorted(lieux.values(), key=lambda x: (x.get("categorie", ""), x["nom"].lower()))
    LIEUX.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    visibles = [l for l in out if not l.get("masquer")]
    print(f"{len(out)} lieux ({len(visibles)} visibles) · {stats} · logos {logos}")
    print(f"adresses : {sum(1 for l in visibles if l.get('adresse'))} · chaînes : {sum(1 for l in visibles if l.get('type') == 'chaine')} · fermés : {sum(1 for l in visibles if l.get('statut') == 'ferme-definitivement')}")


if __name__ == "__main__":
    main()
