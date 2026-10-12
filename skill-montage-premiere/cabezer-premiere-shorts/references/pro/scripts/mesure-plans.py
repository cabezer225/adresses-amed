# mesure-plans.py : durees de plans d'un MP4 exporte. python3 -I mesure-plans.py f.mp4 [seuil=0.3] [fenetre_s=60] > plans.csv
import re, statistics as S, subprocess, sys
f, th, win = sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else 0.3, float(sys.argv[3]) if len(sys.argv) > 3 else 60
o = subprocess.run(['ffmpeg', '-hide_banner', '-i', f, '-an', '-vf', f"select='gt(scene,{th})',showinfo", '-f', 'null', '-'], capture_output=True, text=True).stderr
d = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))
cuts = [0.0] + [float(x) for x in re.findall(r'pts_time:([\d.]+)', o)] + [d]
pl = [b - a for a, b in zip(cuts, cuts[1:]) if b > a]
print('debut_s;duree_s')
for a, b in zip(cuts, cuts[1:]): print(f'{a:.2f};{b - a:.2f}')
print(f'# plans={len(pl)} moyenne={S.mean(pl):.2f}s mediane={S.median(pl):.2f}s max={max(pl):.2f}s', file=sys.stderr)
for w in range(int(-(-d // win))): print(f'# fenetre {w * win:.0f}-{(w + 1) * win:.0f}s : {sum(1 for c in cuts[1:-1] if w * win <= c < (w + 1) * win)} coupes', file=sys.stderr)
