#!/usr/bin/env python3
"""lint-fr.py - typographie française à l'écran (sous-titres, cartons, étiquettes). Lecture seule.
Usage : python3 -I lint-fr.py "texte" ...   ou   python3 -I lint-fr.py -f fichier.srt|.txt
Règles (sources lues : CLDR fr, LanguageTool FRENCH_WHITESPACE ; reste = usage courant, à vérifier) :
  ; ! ?   espace fine insécable U+202F attendue (U+00A0 tolérée)         [LanguageTool]
  :       espace insécable U+00A0 attendue, sauf heure 23:20 et adresse   [LanguageTool]
  « »     U+00A0 à l'intérieur                                            [LanguageTool]
  € %     U+00A0 avant le symbole                                         [CLDR]
  milliers  nombre de 4 chiffres ou plus : séparateur U+202F              [CLDR]
  décimale  virgule, pas de point                                         [CLDR]
  apostrophe droite ' (courbe ’ attendue) ; trois points ... (… attendu)  [usage, à vérifier]
  œ       mots de la liste fermée écrits « oe »                           [orthographe usuelle]
  accents capitales : liste fermée de mots en capitales sans accent       [usage, à vérifier]
Ne vérifie PAS : « 19h30 » / « 19 h 30 » (usage de Cabezer prime), présence des glyphes dans la police.
Code de sortie 1 s'il y a au moins une ligne à corriger.
"""
import re
import sys

NNBSP, NBSP = " ", " "
SP = "[   ]?"
OE = re.compile(r"\b(oeufs?|boeufs?|coeurs?|soeurs?|noeuds?|voeux?|oeil|oeuvres?|manoeuvres?|choeurs?|moeurs?)\b", re.I)
CAPS = re.compile(r"\b(A EMPORTER|ECLAIRS?|DEGUSTATIONS?|PATISSERIES?|DELICIEUX|DELICIEUSE|CREME|BRULEE|DEJEUNER|PREPARATION)\b")

def check(text):
    out = []
    for m in re.finditer(r"(\S)(" + SP + r")([;!?])", text):
        sep, ch = m.group(2), m.group(3)
        if ch == "?" and m.group(1) in "?!":
            continue
        if m.group(1) == "!" and ch == "!":
            continue
        if sep in (NNBSP, NBSP):
            continue
        out.append(f"avant '{ch}' : espace fine insécable U+202F attendue (trouvé {sep!r})")
    for m in re.finditer(r"(\S)(" + SP + r"):", text):
        if m.group(1).isdigit() and re.match(r"\d", text[m.end():m.end() + 1] or ""):
            continue
        ctx = text[max(0, m.start() - 8):m.end() + 3]
        if "//" in ctx or "http" in ctx:
            continue
        if m.group(2) != NBSP:
            out.append(f"avant ':' : espace insécable U+00A0 attendue (trouvé {m.group(2)!r})")
    for m in re.finditer(r"«([^»]*)»", text):
        if not m.group(1).startswith(NBSP):
            out.append("« : U+00A0 attendue juste après «")
        if not m.group(1).endswith(NBSP):
            out.append("» : U+00A0 attendue juste avant »")
    for m in re.finditer(r"(\d)(" + SP + r")(€|%)", text):
        if m.group(2) != NBSP:
            out.append(f"avant '{m.group(3)}' : espace insécable U+00A0 attendue (trouvé {m.group(2)!r})")
    for m in re.finditer(r"(?<![\d.,])(\d{1,3}(?:[   .]\d{3})+|\d{4,})(?![\d])(?!,\d)(?=[^\d]|$)", text):
        n = m.group(0)
        if re.fullmatch(r"\d{4}", n) and 1900 <= int(n) <= 2100:
            continue  # année probable
        if re.fullmatch(r"\d{1,3}( \d{3})+", n):
            continue
        out.append(f"nombre {n!r} : séparateur de milliers U+202F attendu (ex. 1 200) ; une année ne prend pas de séparateur")
    for m in re.finditer(r"\d+\.\d{1,2}(?!\d)", text):
        out.append(f"décimale avec point ({m.group(0)}) : virgule attendue")
    if "'" in text:
        out.append("apostrophe droite : apostrophe courbe ’ attendue")
    if "..." in text:
        out.append("trois points : le caractère … est attendu")
    for m in OE.finditer(text):
        out.append(f"ligature : « {m.group(0)} » s'écrit avec œ")
    for m in CAPS.finditer(text):
        out.append(f"capitale sans accent probable : {m.group(0)}")
    return out

def main(argv):
    if len(argv) >= 3 and argv[1] == "-f":
        lines = [l for l in open(argv[2], encoding="utf-8-sig").read().splitlines() if l.strip()]
    else:
        lines = argv[1:]
    bad = 0
    for ln in lines:
        probs = check(ln)
        if probs:
            bad += 1
            print(repr(ln))
            for p in probs:
                print("   -", p)
    print(f"{bad} ligne(s) à corriger sur {len(lines)}")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
