# xml-coupes.py : liste coupes, trous, desordres, transitions d'un FCP XML (xmeml). python3 -I xml-coupes.py seq.xml [motif_nom_face_camera]
import sys, xml.etree.ElementTree as ET
r = ET.parse(sys.argv[1]).getroot(); motif = sys.argv[2].lower() if len(sys.argv) > 2 else None
s = r.find('.//sequence'); rate = s.find('rate'); tb = int(rate.findtext('timebase')); fps = tb * (1000 / 1001 if rate.findtext('ntsc') == 'TRUE' else 1)
sec = lambda fr: int(fr) / fps
for kind in ('video', 'audio'):
    for i, tr in enumerate(s.findall(f'./media/{kind}/track'), 1):
        prev_end, last_start, face = 0, -1, 0.0
        for el in tr:
            if el.tag == 'transitionitem': print(f'{kind[0].upper()}{i} TRANSITION {sec(el.findtext("start")):.2f}-{sec(el.findtext("end")):.2f}s'); continue
            if el.tag != 'clipitem': continue
            st, en, nm = int(el.findtext('start')), int(el.findtext('end')), el.findtext('name') or '?'
            if st < 0 or en < 0: print(f'{kind[0].upper()}{i} {nm} : debut/fin -1 (lie a une transition, a lire a la main)'); continue
            if st < last_start: print(f'{kind[0].upper()}{i} DESORDRE {nm} @{sec(st):.2f}s : ecrit apres un clip plus tardif (manque a l\'export, skill 14)')
            if st > prev_end and kind == 'video': print(f'{kind[0].upper()}{i} TROU {sec(prev_end):.2f}-{sec(st):.2f}s')
            if st < prev_end: print(f'{kind[0].upper()}{i} CHEVAUCHE {nm} @{sec(st):.2f}s')
            if el.findtext('enabled') == 'FALSE': print(f'{kind[0].upper()}{i} DESACTIVE {nm} @{sec(st):.2f}s')
            if motif and motif in nm.lower(): face += sec(en - st)
            print(f'{kind[0].upper()}{i} COUPE {sec(st):.2f}s  {nm}  ({sec(en - st):.2f}s)')
            prev_end, last_start = max(prev_end, en), st
        if motif and kind == 'video': print(f'V{i} face camera ({motif}) : {face:.1f}s')
