#!/usr/bin/env python3
# affiner_bords.py : recale les bornes de mots Whisper sur l'energie du son.
# python3 -I affiner_bords.py rush.mov mots.json sortie.csv   (mots.json = sortie JSON de whisper --word_timestamps True)
import csv, json, subprocess, sys
import numpy as np

SR, HOP, WIN, HOLD=48000, 240, 960, 4  # 48 kHz ; pas 5 ms ; fenetre 20 ms ; silence soutenu 4 pas = 20 ms
MARGE, MARGE_DOUX, DOUX=6.0, 3.0, 15.0  # seuil = plancher + 6 dB (+ 3 dB si mot doux : pic < 15 dB au-dessus)
PAD_IN, PAD_OUT, EXT=0.020, 0.010, 1.5  # marges gardees (s) ; recherche etendue des mots proteges (s)
PROTEGES=("parti", "enfin", "waouh")

def f(t): return int(round(t*SR/HOP))  # secondes -> indice de pas

def charger(chemin):
    pcm=subprocess.run(["ffmpeg", "-v", "error", "-i", chemin, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    x=np.pad(np.frombuffer(pcm, dtype="<f4").astype(np.float64), (WIN//2, WIN//2))
    idx=np.arange((len(x)-WIN)//HOP+1)[:, None]*HOP+np.arange(WIN)[None, :]
    return 20*np.log10(np.sqrt((x[idx] ** 2).mean(axis=1))+1e-9)  # dBFS par pas

def sortie(db, t0, t1, seuil, proteger):
    p0, lo=min(len(db)-1, f(t1)), f(t0)
    hi=min(len(db)-1, f(t1+(EXT if proteger else 0.3)))
    if db[p0]<seuil:  # Whisper finit trop tard : reculer a la derniere trame energique
        k=p0
        while k>lo and db[k]<seuil: k -= 1
        return (k+1)*HOP/SR, ""
    k, bas=p0, 0  # Whisper finit en pleine energie : avancer jusqu'au silence
    while k<hi:
        bas=bas+1 if db[k]<seuil else 0
        if bas>=HOLD: return (k-HOLD+1)*HOP/SR, ""
        k += 1
    k, bas=p0, 0  # repli : dernier silence soutenu juste derriere
    while k>max(lo, p0-30):
        bas=bas+1 if db[k]<seuil else 0
        if bas>=HOLD:
            while k>lo and db[k-1]<seuil: k -= 1
            return k*HOP/SR, "SANS_SILENCE"
        k -= 1
    return t1, "SANS_SILENCE"

def entree(db, t0, t1, seuil, borne):
    p0, hi=f(t0), min(len(db)-1, f(t1))
    lo=max(f(borne), p0-f(0.3))
    if db[p0]>=seuil:  # deja en energie : reculer jusqu'au vrai silence
        k, bas=p0, 0
        while k>lo:
            bas=bas+1 if db[k]<seuil else 0
            if bas>=HOLD: return (k+HOLD)*HOP/SR, ""
            k -= 1
        return lo*HOP/SR, "COLLE"
    k=p0
    while k<hi and not (db[k:k+3]>=seuil).all(): k += 1  # attaque : 3 pas (15 ms) au-dessus du seuil
    return k*HOP/SR, ""

def main(audio, js, out):
    db=charger(audio)
    W=[dict(w, mot=w["word"].strip()) for s in json.load(open(js, encoding="utf-8"))["segments"] for w in s.get("words", []) if "start" in w and "end" in w]  # mots sans temps ignores
    lignes, prev=[["n", "mot", "debut_whisper", "fin_whisper", "debut_propose", "fin_propose", "ecart_debut_ms", "ecart_fin_ms", "plancher_db", "pic_db", "drapeaux"]], 0.0
    for i, w in enumerate(W):
        a, b=w["start"], w["end"]
        plancher=float(np.percentile(db[max(0, f(a)-200): f(b)+200], 10))  # +-1 s autour du mot
        pic=float(db[f(a):f(b)+1].max())
        doux=pic-plancher<DOUX
        seuil=plancher+(MARGE_DOUX if doux else MARGE)
        prot=any(p in w["mot"].lower() for p in PROTEGES)
        fin, e1=sortie(db, a, b, seuil, prot)
        deb, e2=entree(db, a, b, seuil, prev)
        deb, fin=max(0.0, deb-PAD_IN), fin+PAD_OUT
        if not prot and not e1 and i+1<len(W): fin=min(fin, max(W[i+1]["start"]-0.020, deb+0.05))
        d=[x for x in (e1, e2) if x]+["DOUX_A_ECOUTER"]*doux+["PROTEGE_A_ECOUTER"]*prot
        if fin<=deb: d.append("MOT_SANS_ENERGIE")
        if fin-b>0.15: d.append("WHISPER_TROP_COURT")
        if abs(fin-b)>0.25 or abs(deb-a)>0.25: d.append("GRAND_ECART")
        lignes.append([i, w["mot"], f"{a:.3f}", f"{b:.3f}", f"{deb:.3f}", f"{fin:.3f}", round((deb-a)*1000),
                       round((fin-b)*1000), f"{plancher:.1f}", f"{pic:.1f}", " ".join(d) or "ok"])
        prev=fin
    with open(out, "w", newline="", encoding="utf-8") as fh: csv.writer(fh).writerows(lignes)

main(*sys.argv[1:4])
