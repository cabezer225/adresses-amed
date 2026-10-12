#!/usr/bin/env python3
"""flash_check.py - contrôle de la règle « trois flashs par seconde » (WCAG 2.3.1, flash général).

Méthode (WCAG 2.x, glossaire « general flash and red flash thresholds ») :
  - un flash général = une paire de changements opposés de luminance relative
    d'au moins 0,10 (sur un maximum de 1,0), le côté le plus sombre étant < 0,80 ;
  - le contenu passe si, dans toute période d'une seconde, il y a au plus 3 flashs.
Implémentation : la vidéo est réduite en grille (par défaut 32x18, moyenne par zone de l'image),
ffmpeg fournit des images RGB ; chaque zone a une série de luminance relative ; un flash
local (une seule zone) est donc compté. Le test est donc conservateur sur les flashs locaux.

NON calculé ici (à faire à part si nécessaire) :
  - l'exception de surface (flashs contigus sur moins d'un quart d'un champ de 10 degrés) ;
  - le flash rouge saturé (R/(R+G+B) >= 0,8 et écart de chromaticité > 0,2) ;
  - les vidéos à fréquence variable (la fréquence d'image de ffprobe est supposée constante).

Usage : python3 flash_check.py video.mp4 [--grid 32x18] [--max 3]
Sortie : une ligne JSON (max_flashs_par_seconde, zone, temps des flashs fautifs, verdict).
"""
import argparse
import json
import subprocess
import sys

import numpy as np


def probe(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=r_frame_rate,width,height", "-of", "json", path])
    st = json.loads(out)["streams"][0]
    num, den = st["r_frame_rate"].split("/")
    return float(num) / float(den), int(st["width"]), int(st["height"])


def read_grid(path, gw, gh):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-an",
           "-vf", f"scale={gw}:{gh}:flags=area",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    raw = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout
    n = len(raw) // (gw * gh * 3)
    arr = np.frombuffer(raw, dtype=np.uint8)[: n * gw * gh * 3]
    return arr.reshape(n, gh, gw, 3)


def rel_lum(arr):
    """Luminance relative WCAG (0..1) de chaque zone, arr shape (n, h, w, 3)."""
    c = arr.astype(np.float64) / 255.0
    lin = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * lin[..., 0] + 0.7152 * lin[..., 1] + 0.0722 * lin[..., 2]


def zigzag(series, thr):
    """Pivots alternés (indice, valeur) ; chaque segment entre pivots fait >= thr."""
    n = len(series)
    if n < 2:
        return []
    pivots = []
    d = 0  # 0 = indéterminé, +1 = on suit un maximum, -1 = on suit un minimum
    base_v = series[0]
    ei, ev = 0, series[0]
    for i in range(1, n):
        v = series[i]
        if d == 0:
            if v - base_v >= thr:
                d, ei, ev = 1, i, v
            elif base_v - v >= thr:
                d, ei, ev = -1, i, v
            continue
        if d == 1:
            if v > ev:
                ei, ev = i, v
            elif ev - v >= thr:
                pivots.append((ei, ev, +1))
                d, ei, ev = -1, i, v
        else:
            if v < ev:
                ei, ev = i, v
            elif v - ev >= thr:
                pivots.append((ei, ev, -1))
                d, ei, ev = 1, i, v
    if d != 0:
        pivots.append((ei, ev, d))
    return pivots


def flash_times(series, fps, thr=0.10, dark_max=0.80):
    """Temps (s) de fin de chaque flash : paires consécutives de transitions opposées
    qualifiantes (écart >= thr, côté sombre < dark_max)."""
    piv = zigzag(series, thr)
    times = []
    run = []  # indices des transitions qualifiantes consécutives
    prev_end = None
    for k in range(len(piv) - 1):
        a, b = piv[k], piv[k + 1]
        qualifies = min(a[1], b[1]) < dark_max
        if qualifies:
            if run and run[-1] != k - 1:
                # coupure : on vide le groupe courant
                times.extend(_pairs(run, piv, fps))
                run = []
            run.append(k)
        else:
            times.extend(_pairs(run, piv, fps))
            run = []
    times.extend(_pairs(run, piv, fps))
    return sorted(times)


def _pairs(run, piv, fps):
    out = []
    for j in range(0, len(run) - 1, 2):
        end_pivot = piv[run[j + 1] + 1]
        out.append(end_pivot[0] / fps)
    return out


def max_in_one_second(times):
    """Nombre maximal de flashs dans une fenêtre d'une seconde [t, t+1)."""
    best, best_t, j = 0, None, 0
    for i, t in enumerate(times):
        while times[j] <= t - 1.0 and j < i:
            j += 1
        count = i - j + 1
        if count > best:
            best, best_t = count, t
    return best, best_t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--grid", default="32x18")
    ap.add_argument("--max", type=int, default=3)
    args = ap.parse_args()
    gw, gh = (int(x) for x in args.grid.split("x"))
    fps, w, h = probe(args.video)
    grid = rel_lum(read_grid(args.video, gw, gh))  # (n, gh, gw)
    n = grid.shape[0]
    worst = {"count": 0, "cell": None, "at": None, "times": []}
    for y in range(gh):
        for x in range(gw):
            series = grid[:, y, x]
            times = flash_times(series, fps)
            if not times:
                continue
            c, t = max_in_one_second(times)
            if c > worst["count"]:
                worst = {"count": c, "cell": [x, y], "at": t, "times": times}
    fails = worst["count"] > args.max
    offending = []
    if fails and worst["at"] is not None:
        offending = [round(t, 2) for t in worst["times"]
                     if worst["at"] - 1.0 < t <= worst["at"] + 1.0][:12]
    result = {
        "fichier": args.video,
        "fps": round(fps, 3),
        "images_analysees": n,
        "grille": f"{gw}x{gh}",
        "max_flashs_par_seconde": worst["count"],
        "zone_la_plus_chargee_xy": worst["cell"],
        "fenetre_debut_s": round(worst["at"], 2) if worst["at"] is not None else None,
        "temps_flashs_fautifs_s": offending,
        "verdict": "ECHEC (plus de %d flashs par seconde)" % args.max if fails
        else "OK (au plus %d flashs par seconde, test de surface et flash rouge non calcules)" % args.max,
    }
    print(json.dumps(result, ensure_ascii=False))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
