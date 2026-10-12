#!/usr/bin/env python3
# reprise-candidats.py : inventaire en lecture seule des candidats de reprise
# d'un dossier de projet (.prproj, .aep, sauvegardes, enregistrements automatiques).
# Usage : python3 -I reprise-candidats.py <dossier_sujet> [--copie-vers <dossier>] [--rang N]
# Ne modifie jamais les fichiers source. --copie-vers copie (sans écraser) le candidat
# choisi par --rang (0 = le plus récent) dans le dossier indiqué, avec empreinte SHA-256.
import argparse, datetime, gzip, hashlib, os, re, shutil, sys

EXT = {".prproj", ".aep", ".bak", ".aep.bak", ".prproj.bak"}
STAMP = re.compile(r"-\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}")  # forme Premiere (à confirmer par test)
AUTOSAVE_DIR = re.compile(r"auto[- ]?save", re.IGNORECASE)


def est_candidat(chemin, dossier_auto):
    nom = os.path.basename(chemin).lower()
    if any(nom.endswith(e) for e in EXT):
        return True
    return dossier_auto and (nom.endswith(".prproj") or nom.endswith(".aep"))


def entete(chemin):
    """Retourne une étiquette de format sans supposer le contenu : gzip ou non, XML ou non."""
    try:
        with open(chemin, "rb") as f:
            debut = f.read(4096)
    except OSError as e:
        return f"illisible ({e.__class__.__name__})"
    if not debut:
        return "VIDE"
    if debut[:2] == b"\x1f\x8b":
        try:
            with gzip.open(chemin, "rb") as g:
                interne = g.read(64)
            return "gzip, " + ("XML" if interne.lstrip().startswith(b"<?xml") or interne.lstrip().startswith(b"<") else "contenu non XML")
        except (OSError, EOFError):
            return "gzip ABIME"
    return "XML" if debut.lstrip().startswith(b"<") else "binaire (format AE ou autre)"


def collecte(racine, profondeur_max=6):
    trouves = []
    racine = os.path.abspath(racine)
    base_n = racine.count(os.sep)
    for dp, dn, fn in os.walk(racine):
        if dp.count(os.sep) - base_n > profondeur_max:
            dn[:] = []
            continue
        dossier_auto = bool(AUTOSAVE_DIR.search(os.path.basename(dp)))
        for f in fn:
            p = os.path.join(dp, f)
            if est_candidat(p, dossier_auto):
                st = os.stat(p)
                trouves.append({
                    "chemin": p, "mtime": st.st_mtime, "taille": st.st_size,
                    "auto": dossier_auto or bool(STAMP.search(f)),
                })
    trouves.sort(key=lambda d: d["mtime"], reverse=True)
    return trouves


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("racine")
    ap.add_argument("--copie-vers")
    ap.add_argument("--rang", type=int, default=0)
    a = ap.parse_args()
    if not os.path.isdir(a.racine):
        sys.exit("dossier introuvable : " + a.racine)
    c = collecte(a.racine)
    if not c:
        print("Aucun candidat (.prproj, .aep, .bak, dossier Auto-Save).")
        return
    print(f"{'rang':>4}  {'date (locale)':19}  {'octets':>10}  {'format':34}  fichier")
    for i, d in enumerate(c):
        date = datetime.datetime.fromtimestamp(d["mtime"]).strftime("%Y-%m-%d %H:%M:%S")
        flag = "  [auto]" if d["auto"] else ""
        print(f"{i:>4}  {date:19}  {d['taille']:>10}  {entete(d['chemin']):34}  {os.path.relpath(d['chemin'], a.racine)}{flag}")
    if a.copie_vers:
        if not (0 <= a.rang < len(c)):
            sys.exit("rang hors liste")
        src = c[a.rang]["chemin"]
        os.makedirs(a.copie_vers, exist_ok=True)
        dst = os.path.join(a.copie_vers, os.path.basename(src))
        if os.path.exists(dst):
            sys.exit("refus : la destination existe déjà (aucun écrasement) : " + dst)
        h = hashlib.sha256()
        with open(src, "rb") as f:
            for bloc in iter(lambda: f.read(1 << 20), b""):
                h.update(bloc)
        shutil.copy2(src, dst)
        print(f"copie : {dst}\nsha256 : {h.hexdigest()}")


if __name__ == "__main__":
    main()
