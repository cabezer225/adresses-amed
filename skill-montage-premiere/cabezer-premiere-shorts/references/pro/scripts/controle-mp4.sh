#!/bin/bash
# controle-mp4.sh : lecture seule. Usage : bash controle-mp4.sh export.mp4 [largeur hauteur]  (defaut 1080 1920)
f=$1; W=${2:-1080}; H=${3:-1920}; [ -f "$f" ] || { echo "fichier absent"; exit 1; }
python3 -I - "$f" "$W" "$H" <<'PY'
import json, subprocess, sys
f, W, H = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
j = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',f]))
v = next(s for s in j['streams'] if s['codec_type'] == 'video')
a = next((s for s in j['streams'] if s['codec_type'] == 'audio'), None)
n, d = map(int, v['avg_frame_rate'].split('/')); fps = n / d; br = int(j['format']['bit_rate']) / 1e6
bt = [v.get(k) for k in ('color_primaries', 'color_transfer', 'color_space')]
rows = [('taille', f"{v['width']}x{v['height']}", (v['width'], v['height']) == (W, H)),
 ('codec', f"{v['codec_name']} {v.get('profile')} niv.{v.get('level')} {v['pix_fmt']}", v['codec_name'] == 'h264' and v['pix_fmt'] == 'yuv420p'),
 ('cadence', f"{fps:.3f}" + ('' if v['r_frame_rate'] == v['avg_frame_rate'] else ' VARIABLE'), v['r_frame_rate'] == v['avg_frame_rate']),
 ('couleur', '/'.join(map(str, bt)), bt == ['bt709'] * 3),
 ('debit', f"{br:.1f} Mbit/s", True), ('duree', f"{float(j['format']['duration']):.2f} s", True)]
if a:
    gap = abs(float(a['duration']) - float(v['duration']))
    rows += [('audio', f"{a['codec_name']} {a['sample_rate']} Hz {a['channels']} ch", (a['codec_name'], a['sample_rate'], a['channels']) == ('aac', '48000', 2)),
             ('ecart A/V', f"{gap:.3f} s", gap < .1)]
else:
    rows.append(('audio', 'ABSENT', False))
for k, val, ok in rows: print(('OK    ' if ok else 'ECART ') + f'{k:10} {val}')
PY
echo "--- integrite"; ffmpeg -v error -i "$f" -f null - && echo "decodage OK"
echo "--- noirs (d=0.04)";   ffmpeg -hide_banner -i "$f" -an -vf blackdetect=d=0.04:pix_th=0.10 -f null - 2>&1 | grep -o 'black_start.*'
echo "--- figes (-60 dB, 1 s)"; ffmpeg -hide_banner -i "$f" -map 0:v -vf freezedetect=n=-60dB:d=1 -f null - 2>&1 | grep -o 'freeze_.*'
echo "--- son manquant (-50 dB, 0,5 s)"; ffmpeg -hide_banner -i "$f" -vn -af silencedetect=n=-50dB:d=0.5 -f null - 2>&1 | grep -o 'silence_.*'
echo "--- niveaux video (legal 16-235)"; ffmpeg -hide_banner -i "$f" -vf "signalstats,metadata=mode=print:file=-" -an -f null - 2>/dev/null | grep -E "YMIN|YMAX" | sed 's/.*=//' | sort -n | sed -n '1p;$p' | paste -sd' ' -
echo "--- loudness (repere, pas cible)"; ffmpeg -hide_banner -nostats -i "$f" -vn -af ebur128=peak=true -f null - 2>&1 | sed -n '/Summary/,$p' | awk '/^ *I:/{i=$2} /^ *LRA:/{l=$2} /^ *Peak:/{p=$2} END{print "I="i" LUFS  LRA="l" LU  crete vraie="p" dBFS"}'
