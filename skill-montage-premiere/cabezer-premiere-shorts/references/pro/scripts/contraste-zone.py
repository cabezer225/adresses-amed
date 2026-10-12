#!/usr/bin/env python3
"""contraste-zone.py - rapport de contraste WCAG entre une couleur de texte et le fond d'une zone d'une image d'un MP4.
Usage : python3 -I contraste-zone.py video.mp4 t_secondes x y w h couleur_texte_hex [--percentile 95]
  - À utiliser sur un export SANS la piste de texte, ou sur une image prise juste avant l'entrée du texte,
    pour que la zone ne contienne que le fond.
  - Texte clair : le pire fond est le plus clair (percentile haut) ; texte sombre : le plus sombre (percentile bas).
  - Seuils WCAG 1.4.3 : 4,5:1 texte normal ; 3:1 grand texte (18 pt ou 14 pt gras) ; sans arrondi.
Sortie : une ligne JSON. Code de sortie 1 si < 3:1.
"""
import json
import subprocess
import sys

import numpy as np


def lin(c):
    c = c / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def lum(rgb):
    r, g, b = lin(rgb[..., 0]), lin(rgb[..., 1]), lin(rgb[..., 2])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def main(a):
    video, t, x, y, w, h, col = a[1], float(a[2]), int(a[3]), int(a[4]), int(a[5]), int(a[6]), a[7].lstrip("#")
    pct = float(a[a.index("--percentile") + 1]) if "--percentile" in a else 95.0
    txt = np.array([int(col[i:i + 2], 16) for i in (0, 2, 4)], dtype=np.float64)
    lt = float(lum(txt))
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", video, "-frames:v", "1",
                          "-vf", f"crop={w}:{h}:{x}:{y}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         stdout=subprocess.PIPE, check=True).stdout
    img = np.frombuffer(raw, np.uint8)[: w * h * 3].reshape(h, w, 3).astype(np.float64)
    lb = lum(img)
    light_text = lt >= 0.18
    lbg = float(np.percentile(lb, pct if light_text else 100 - pct))
    hi, lo = max(lt, lbg), min(lt, lbg)
    ratio = (hi + 0.05) / (lo + 0.05)
    res = {"t_s": t, "zone": [x, y, w, h], "texte": "#" + col.upper(), "L_texte": round(lt, 4),
           "L_fond_pire_cas": round(lbg, 4), "percentile": pct if light_text else 100 - pct,
           "contraste": round(ratio, 2),
           "verdict": "OK texte normal (>= 4,5:1)" if ratio >= 4.5 else
                      "OK grand texte seulement (>= 3:1)" if ratio >= 3 else "ECHEC (< 3:1)"}
    print(json.dumps(res, ensure_ascii=False))
    return 0 if ratio >= 3 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
