#!/usr/bin/env python3
# paquets.py : paquets de sous-titres traduits des courts (1 a 3 mots, 18 caracteres max), retires ou decales sous les animations.
# Usage : python3 -I paquets.py mots.tsv [fenetres_animations.tsv] > paquets.tsv
#   mots.tsv : debut<TAB>fin<TAB>mot (temps du derush valide) ; fenetres : debut<TAB>fin des pop-ups, prix, note, appel.
# Plancher d'affichage : 0,25 s (reponse de Cabezer du 12/10/2026 : au rythme de la parole, verifie sur telephone).
import sys
PETITS = {"le","la","les","un","une","des","de","du","d'","l'","à","a","au","et","en","y","ce","se","sa","son",
          "ses","je","tu","il","on","ne","the","an","of","to","in","at","and","or","my","is","it"}
MAXC, MAXW = 18, 3
def paquets(mots):
    out, cur = [], []
    def vide():
        nonlocal cur
        if cur: out.append((cur[0][0], cur[-1][1], " ".join(m[2] for m in cur))); cur = []
    for d, f, m in mots:
        if cur and (len(" ".join(x[2] for x in cur + [(d, f, m)])) > MAXC or len(cur) >= MAXW): vide()
        cur.append((d, f, m))
        fin = m.rstrip().endswith((".", "!", "?", "…"))
        petit = m.lower().strip(",.;:!?") in PETITS
        if fin or (len(cur) >= 2 and not petit and len(" ".join(x[2] for x in cur)) >= 9): vide()
    vide(); return out
def lire(p): return [tuple(l.rstrip("\n").split("\t")) for l in open(p) if l.strip()]
mots = [(float(a), float(b), c) for a, b, c in lire(sys.argv[1])]
wins = [(float(a), float(b)) for a, b, *_ in lire(sys.argv[2])] if len(sys.argv) > 2 else []
for d, f, t in paquets(mots):
    for wd, wf in wins:
        if d < wf and f > wd:                      # chevauche une animation
            if d < wd: f = min(f, wd)              # garder la partie avant
            else: d = wf                           # attendre la fin
    if f - d >= 0.25: print(f"{d:.3f}\t{f:.3f}\t{t}")   # sinon retiré (valeur de départ)
