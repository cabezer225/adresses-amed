"""Duplicate visits and places in data/lieux.json.

  python3 scripts/doublons.py preparer N     write N batches data/verif/doublons-entree-*.json + the place catalogue
  python3 scripts/doublons.py appliquer      apply data/verif/doublons-resultat-*.json and doublons-lieux-resultat.json,
                                             minus the merges listed in data/verif/doublons-rejets.json

The same tasting is often published as a long YouTube video plus a Short, TikTok or Reel: it becomes one visit
with every video link. Only high or medium confidence merges are applied.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERIF = ROOT / "data" / "verif"
LIEUX = ROOT / "data" / "lieux.json"
OK = ("haute", "moyenne")


def norm(s):
    s = unicodedata.normalize("NFD", str(s or "").lower())
    return re.sub(r"[^a-z0-9]+", " ", "".join(c for c in s if unicodedata.category(c) != "Mn")).strip()


def durees():
    p = VERIF / "yt-durees.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def duree(url, d):
    m = re.search(r"(?:v=|shorts/|youtu\.be/)([\w-]{11})", url)
    return d.get(m.group(1)) if m else None


def preparer(n):
    lieux = [l for l in json.loads(LIEUX.read_text(encoding="utf-8")) if not l.get("masquer")]
    d = durees()
    multi = []
    for l in lieux:
        if len(l["visites"]) < 2:
            continue
        visites = sorted(l["visites"], key=lambda v: v.get("date") or "")
        multi.append({
            "lieu_id": l["id"], "lieu": l["nom"], "type": l["type"],
            "visites": [{
                "i": i, "date": v.get("date"), "titre": v.get("titre"), "avis": v.get("avis"), "note_globale": v.get("note_globale"),
                "plats": [{"nom": p["nom"], "prix": p.get("prix"), "note": p.get("note")} for p in v.get("plats", [])],
                "videos": [{"platform": x["platform"], "url": x["url"], "duree_s": duree(x["url"], d) if x["platform"] == "youtube" else None} for x in v["videos"]],
            } for i, v in enumerate(visites)],
        })
    # Balance batches by number of visits.
    multi.sort(key=lambda x: -len(x["visites"]))
    lots = [[] for _ in range(n)]
    for x in multi:
        min(lots, key=lambda b: sum(len(y["visites"]) for y in b)).append(x)
    for i, b in enumerate(lots, 1):
        (VERIF / f"doublons-entree-{i}.json").write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
    cat = [{"id": l["id"], "nom": l["nom"], "type": l["type"], "ville": l.get("ville"), "adresse": l.get("adresse"),
            "specialite": l.get("specialite"), "logo": l.get("logo"), "visites": [v.get("titre") for v in l["visites"]][:6]} for l in lieux]
    (VERIF / "catalogue-doublons-lieux.json").write_text(json.dumps(cat, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(multi)} lieux à vérifier en {n} lots : {[sum(len(y['visites']) for y in b) for b in lots]} visites ; {len(cat)} lieux au catalogue")


def fusionner(garde, autres):
    for v in autres:
        urls = {x["url"] for x in garde["videos"]}
        garde["videos"] += [x for x in v["videos"] if x["url"] not in urls]
        par_nom = {norm(p["nom"]): p for p in garde.get("plats", [])}
        for p in v.get("plats", []):
            k = norm(p["nom"])
            if k not in par_nom:
                garde.setdefault("plats", []).append(p)
                par_nom[k] = p
            else:
                q = par_nom[k]
                if q.get("note") is None and p.get("note") is not None:
                    q["note"] = p["note"]
                if q.get("prix") is None and p.get("prix") is not None:
                    q["prix"] = p["prix"]
        if not garde.get("avis") or (v.get("avis") and len(v["avis"]) > len(garde["avis"]) and not garde.get("plats")):
            garde["avis"] = v.get("avis") or garde.get("avis")
        if garde.get("note_globale") is None and v.get("note_globale") is not None:
            garde["note_globale"] = v["note_globale"]
        garde["partenariat"] = garde.get("partenariat") or v.get("partenariat")
        if v.get("date") and (not garde.get("date") or v["date"] < garde["date"]):
            garde["date"] = v["date"]
    # Drop placeholder dishes when real ones exist.
    if any(p.get("note") is not None for p in garde.get("plats", [])):
        garde["plats"] = [p for p in garde["plats"] if p.get("note") is not None or p.get("prix") is not None or not re.search(r"nouveaut|box|menu|à compléter", p["nom"], re.I)]


def appliquer():
    lieux = {l["id"]: l for l in json.loads(LIEUX.read_text(encoding="utf-8"))}
    rejets = set()
    pr = VERIF / "doublons-rejets.json"
    if pr.exists():
        rejets = {(r["lieu_id"], r["garder"], tuple(sorted(r["fusionner"]))) for r in json.loads(pr.read_text(encoding="utf-8"))}
    n_visites = n_lieux = 0
    for f in sorted(VERIF.glob("doublons-resultat-*.json")):
        for r in json.loads(f.read_text(encoding="utf-8")):
            l = lieux.get(r.get("lieu_id"))
            if not l:
                continue
            visites = sorted(l["visites"], key=lambda v: v.get("date") or "")  # same order as in preparer()
            absorbees = set()
            for g in r.get("groupes") or []:
                key = (r["lieu_id"], g.get("garder"), tuple(sorted(g.get("fusionner") or [])))
                if g.get("confiance") not in OK or key in rejets:
                    continue
                idx = [i for i in g.get("fusionner") or [] if isinstance(i, int) and 0 <= i < len(visites) and i != g["garder"]]
                if not isinstance(g.get("garder"), int) or not 0 <= g["garder"] < len(visites) or not idx:
                    continue
                garde = visites[g["garder"]]
                fusionner(garde, [visites[i] for i in idx])
                if g.get("titre"):
                    garde["titre"] = g["titre"]
                absorbees |= set(idx)
                n_visites += len(idx)
            # A long video merged into several tests stays in each of them; only the absorbed visits go away.
            l["visites"] = [v for i, v in enumerate(visites) if i not in absorbees]

    pl = VERIF / "doublons-lieux-resultat.json"
    if pl.exists():
        for r in json.loads(pl.read_text(encoding="utf-8")):
            if r.get("confiance") not in OK or r.get("garder") not in lieux:
                continue
            g = lieux[r["garder"]]
            for src in r.get("absorber") or []:
                s = lieux.pop(src, None)
                if not s or s is g:
                    continue
                g["visites"] += s["visites"]
                for k in ("adresse", "ville", "logo", "specialite", "avis"):
                    if not g.get(k) and s.get(k):
                        g[k] = s[k]
                n_lieux += 1

    LIEUX.write_text(json.dumps(list(lieux.values()), ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"visites fusionnées : {n_visites} · lieux fusionnés : {n_lieux}")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "preparer":
        preparer(int(sys.argv[2]) if len(sys.argv) >= 3 else 4)
    elif len(sys.argv) >= 2 and sys.argv[1] == "appliquer":
        appliquer()
    else:
        print(__doc__)
        sys.exit(1)
