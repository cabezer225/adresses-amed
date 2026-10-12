# lint-srt.py : lecture seule. python3 -I lint-srt.py f.srt D-fr|D-trad|autre [9:16|16:9] [--mids]
import re, sys
srt, fam = sys.argv[1], sys.argv[2]; ratio = sys.argv[3] if len(sys.argv) > 3 and ':' in sys.argv[3] else '9:16'
CPL = 24 if ratio == '9:16' else 42
T = lambda s: sum(float(x) * k for x, k in zip(s.replace(',', '.').split(':'), (3600, 60, 1)))
prev, bad, mids = 0.0, 0, []
for b in re.split(r'\n\s*\n', open(srt, encoding='utf-8-sig').read().strip()):
    L = b.strip().split('\n'); m = re.match(r'(\S+) --> (\S+)', L[1]); a, z, txt = T(m[1]), T(m[2]), L[2:]
    words, n, pb = ' '.join(txt).split(), len(' '.join(txt)), []; mids.append(round((a + z) / 2, 2))
    if fam == 'D-fr' and len(words) != 1: pb.append('plus d un mot')
    elif fam == 'D-trad' and (len(words) > 3 or n > 18): pb.append('plus de 3 mots ou 18 car')
    elif fam == 'autre':
        if len(txt) > 2: pb.append(f'{len(txt)} lignes')
        if max(map(len, txt)) > CPL: pb.append(f'ligne > {CPL} car')
        if len(txt) > 1 and any(len(x.split()) == 1 for x in txt): pb.append('mot isole')
        if z - a < max(1.5, 1 + n / 15): pb.append(f'lecture courte {z - a:.2f}s (formule du skill)')
    if a < prev - .001: pb.append('chevauche')
    if re.search(r"\S [;:!?€%]", ' '.join(txt)): pb.append('espace simple avant ; : ! ? % €')
    if "'" in ' '.join(txt): pb.append('apostrophe droite')
    if pb: bad += 1; print(f'#{L[0]} {m[1]} ' + ', '.join(pb) + ' | ' + ' / '.join(txt))
    prev = z
print(len(mids), 'blocs,', bad, 'a revoir'); print(*mids) if '--mids' in sys.argv else None
