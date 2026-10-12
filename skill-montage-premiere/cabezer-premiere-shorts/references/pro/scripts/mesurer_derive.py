#!/usr/bin/env python3
# mesurer_derive.py : decalage camera/enregistreur au debut, au milieu et a la fin d'une prise. python3 -I mesurer_derive.py cam.mov rec.wav
import subprocess, sys
import numpy as np
SR, FEN, MARGE=16000, 20, 5  # 16 kHz ; fenetres de 20 s ; recherche +-5 s
def lire(p):
    b=subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(b, dtype="<f4").astype(np.float64)
cam, rec=lire(sys.argv[1]), lire(sys.argv[2])
duree=min(len(cam), len(rec))/SR
for nom, t in (("debut", MARGE), ("milieu", duree/2-FEN/2), ("fin", duree-FEN-MARGE)):
    a=cam[int(t*SR):int((t+FEN)*SR)]
    b=rec[int((t-MARGE)*SR):int((t+FEN+MARGE)*SR)]
    n=1 << int(np.ceil(np.log2(len(a)+len(b))))
    c=np.fft.irfft(np.fft.rfft(b-b.mean(), n)*np.conj(np.fft.rfft(a-a.mean(), n)), n)[:len(b)-len(a)+1]
    print(f"{nom:6} t={t:7.1f} s  decalage enregistreur - camera = {(np.argmax(c) / SR - MARGE) * 1000:+8.1f} ms")
