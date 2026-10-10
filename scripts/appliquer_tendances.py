"""Flag the « Tendances 🔥 » places in data/lieux.json from data/verif/tendances-resultat-*.json (high/medium confidence)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIEUX = ROOT / "data" / "lieux.json"

lieux = json.loads(LIEUX.read_text(encoding="utf-8"))
res = {r["id"]: r for f in sorted((ROOT / "data" / "verif").glob("tendances-resultat-*.json")) for r in json.loads(f.read_text(encoding="utf-8"))}
n = 0
for l in lieux:
    r = res.get(l["id"])
    if r and r.get("tendance") and r.get("confiance") in ("haute", "moyenne") and r.get("raison"):
        l["tendance"] = r["raison"].strip()
        n += 1
    elif r is not None:
        l.pop("tendance", None)
LIEUX.write_text(json.dumps(lieux, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{n} lieux tendances")
