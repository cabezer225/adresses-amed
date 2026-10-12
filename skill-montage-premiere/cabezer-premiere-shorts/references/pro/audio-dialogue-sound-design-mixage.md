# Audio pro : montage dialogue, sound design, musique, mixage et loudness

Fiche de référence pour piloter l'audio dans Premiere Pro et After Effects comme un monteur son, dans le cadre des règles de Cabezer. Dernière vérification : 12/10/2026. Versions de Premiere et d'After Effects : non affirmées ; elles se lisent à l'écran et se consignent avec le test de fumée de `pilotage-environnement-reprise.md`.

**Niveaux de preuve** :
- **[Skill]** : règle du skill ; elle prime sur toute la fiche.
- **[Doc lue]** : texte primaire ouvert (documentation FFmpeg, code de Whisper, README de stable-ts et WhisperX).
- **[Tuto]** : transcription lue en entier (Judd, Levine, Film Riot) ; valeur d'un auteur, jamais une règle universelle.
- **[Extrait]** : extrait de résultat de recherche (aide Adobe, EBU, forums) ; page non ouverte.
- **[Mesure ici]** : exécuté pendant la rédaction (ffmpeg 6.1.1, Python 3.13, numpy 2.5, Linux) sur des signaux synthétiques. Syntaxe et logique vérifiées ; les chiffres ne valent jamais pour la voix de Cabezer.
- **[À vérifier]** : connaissance générale ou source unique ; contrôler à l'écran, dans sa version.

**Limite** : l'aide Adobe, l'EBU, YouTube, Spotify et ffmpeg.org sont restés inaccessibles ; les chiffres EBU viennent d'extraits de recherche, aucun loudness de plateforme n'est confirmé.

## Quand lire cette fiche

Avant toute passe audio : coupes et raccords de voix, synchronisation d'un enregistreur externe, room tone, musique, ducking, SFX et calage sur les animations After Effects, ambiances, mixage, loudness, contrôle du MP4. Rythme et récit : `fondamentaux-montage-narratif.md` ; Premiere hors audio : `premiere-pro-avance.md` ; contrôles ffmpeg : `organisation-livraison-qc.md §6`.

Priorité (skill §1) : brief, skill, fiches, tutoriels. Chaque technique dit **quand l'utiliser, quand l'éviter, pour quelles familles** : dégustation (D), food long (F), Story (S), films/séries PRISME (P), tech (T), hors familles (H). En cas de doute, appliquer le skill et signaler l'écart.

## Sommaire

1. Principes, limites de Claude et outils automatiques
2. Pistes, gain, double système, ordre de travail
3. Montage du dialogue (dont l'outil d'affinage des bords)
4. Chaîne de traitement de la voix
5. Musique, ducking, nappe de Story
6. SFX et sound design
7. Ambiances et room tone
8. Mixage
9. Loudness : mesure et repères
10. Contrôle du MP4
11. Procédures Premiere et After Effects, libellés
12. Application par famille
13. Erreurs de débutant → réflexes de pro
14. Liste de contrôle
15. Décisions à demander à Cabezer
16. Sources étudiées

---

## 1. Principes, limites de Claude et outils automatiques

**Règles du skill qui encadrent l'audio** [Skill §4, §5, §11, §13] :
- Coupe juste après le dernier mot entièrement audible, sans blanc résiduel, placée à l'énergie du son et à la forme d'onde, jamais aux seuls temps de transcription ; saut de fond comblé par le silence de la pièce du même rush.
- Protéger « Bref, c'est partiiii » entier, la fin des exclamations étirées et l'appel au commentaire.
- Voix : mêmes réglages fixes sur tous les clips, un limiteur unique sur la piste. SFX clairement audibles sous une voix intelligible ; jamais d'écrêtage ; mixage = passe distincte.

Sur téléphone, une voix claire est claire partout (Levine) ; un plugin de restauration dépanne, il ne répare pas une mauvaise prise (Judd, Film Riot) [Tuto]. Donc : mesurer d'abord, corriger peu, faire écouter par Cabezer.

**Outils IA et automatismes audio** :

| Statut | Outils |
|---|---|
| Autorisés comme aides, résultat vérifié | Transcription (Speech to Text), montage par le texte pour repérer et pré-découper |
| Sur demande explicite de Cabezer seulement | Tout outil de génération ou de reconstruction de son |
| Interdits par défaut (règle de Cabezer) | « Améliorer la parole » (Enhance Speech, change le timbre), « Correspondance automatique » (Auto Match), curseur « Dynamique » d'Essential Sound, voix ou musique générées |

**Claude n'entend pas.** Il contrôle par mesures (ebur128, crêtes, spectre), transcription et forme d'onde. Ne jamais écrire « écouté » pour une mesure.

| Mesurable par Claude | À faire écouter à Cabezer |
|---|---|
| Niveau intégré, crête vraie, écrêtage | Naturel des raccords et des fondus |
| Écarts de niveau voix / musique / SFX | Timbre de la voix après traitement |
| Blancs, trous, restes de phrases (avec la transcription) | Dosage des SFX, de l'ambiance, de la musique |
| Compatibilité mono (phase) | Confort au casque et au téléphone |
| Intelligibilité (ci-dessous) | Verdict « validé par Cabezer » |

**Test d'intelligibilité** [À vérifier, non étalonné] : retranscrire l'export mixé en fenêtres de 10 s qui se chevauchent (skill §5.2) et comparer à la voix seule ; des mots perdus signalent un mix trop chargé. Elle ne prouve pas la clarté au haut-parleur : Whisper est plus robuste qu'une oreille.

**Plugins : gratuits uniquement** (skill §17). Tout plugin payant (iZotope RX, suites de restauration « un bouton », Acon Digital, Deep Breath, BeatEdit 2, Auto Edit Clip, LA-2A) est signalé avec son prix connu ou « à vérifier » et attend l'accord de Cabezer. Les effets natifs suffisent pour tout ce qui suit.

---

## 2. Pistes, gain, double système, ordre de travail

### 2.1 Pistes [Skill §11]

A1–A2 voix, A3–A4 SFX, A5 musique, une piste d'ambiance si utilisée. **Un type de son par piste** (sinon pas de chaîne voix uniforme). Nommer les pistes ; couper l'audio source des inserts muets (skill §5).

### 2.2 Gain avant effet [Tuto]

Ordre : gain du clip, EQ, dynamique, fader de piste ; recaler après chaque boost d'EQ (Levine). Crêtes de voix autour de **−12 dBFS** avant dynamique, jamais au-delà de −6 (Judd, départ). Faders de piste à **−3 dB** au départ (Levine, « pas une règle absolue »).

### 2.3 Les prises 32 bits flottants de Cabezer [Skill §3, Tuto Judd 2025]

Un fichier 32 bits flottant garde les niveaux au-dessus de 0 dBFS sans écrêtage : on les récupère en **baissant** le gain du clip. Le fader de l'enregistreur n'agit pas sur le préampli : remonter une prise trop basse remonte aussi le bruit.
1. Format réel : `ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,sample_rate,channels -of default=nw=1 rush.mov` [Mesure ici]. Un WAV flottant affiche `pcm_f32le` [À vérifier sur ses fichiers].
2. Niveau : `ffmpeg -hide_banner -nostats -i rush.mov -vn -af astats=measure_perchannel=none:measure_overall=Peak_level+RMS_level -f null - 2>&1 | grep -E "Peak|RMS"`. Une crête positive est normale en flottant ; la ramener sous −6 dBFS avec le gain du clip. `Peak_level` = crête d'échantillon en dBFS [Doc lue : FFmpeg, astats].
3. Noter fréquence (48 kHz en vidéo) et canaux ; rush mono sur séquence stéréo : §9.5.

### 2.4 Synchronisation double système (son enregistré à part de l'image)

**Quand** : toutes familles, dès que la voix vient d'un enregistreur ou d'un micro externe. **Éviter** : audio déjà dans le fichier caméra. Les gestes Premiere (fusion, multicam) sont dans `premiere-pro-avance.md §6` (« Double système ») ; voici le côté audio, à tester sur une copie.

1. **Identifier les pistes.** Fichier externe (codec, canaux, fréquence : commande du §2.3) et audio caméra, qui ne sert que de guide. Ne jamais mélanger une piste normale et sa piste de sécurité (même signal à deux gains : phase) ; n'importer que la normale.
2. **Synchroniser sur la forme d'onde.** Clic droit sur la vidéo et le WAV > Fusionner les clips (Merge Clips) > synchronisation par l'audio (Audio) ; cocher la suppression de l'audio caméra (Remove Audio from AV Clip) pour éviter l'écho [Extrait : tutoriels ProVideo Coalition, Emerson ; libellés à confirmer]. Désactiver l'audio caméra sans le supprimer avant le point 3. La fusion peut supprimer des métadonnées audio (`premiere-pro-avance.md §6`) : contrôler les canaux après. Plusieurs caméras : multicam.
3. **Contrôler en trois points** (début, milieu, fin de prise) à l'image près, sur un clap ou un son net. Sur une prise longue, mesurer avec `mesurer_derive.py` (ci-dessous).
4. **Dérive.** Chaque appareil a sa propre horloge : même réglés à 48 kHz, ils ne restent pas alignés sur une prise longue [Extrait : forums DVinfo, fabricants]. Dérive = décalage de fin − décalage de début. Une image = 33 ms à 29,97 i/s, 40 ms à 25 i/s. **Seuil : plus d'une image sur la prise** ; en dessous, laisser. Corriger dans l'ordre :
   - **Segmenter** : couper la prise en tronçons (aux silences) et resynchroniser chacun. Le plus sûr.
   - **Étirer l'audio sans changer la hauteur**, en dernier recours (Vitesse/Durée, ou `ffmpeg -af atempo=<rapport>` sur une copie). Test : sur 28,6 ms de dérive en 570 s, `atempo=0.99995` n'a ramené que 14 ms, non linéairement, et `atempo=1.00005` a aggravé l'écart [Mesure ici]. Le sens et la précision se vérifient en remesurant.
   - **Prévenir** : une claquette de tête et de fin de prise donne la dérive sans calcul [Extrait : Sound Devices].
5. **Prises 32 bits flottants** : §2.3.
6. **Consigner** dans `Suivi/decisions.md` la méthode et le décalage mesuré par prise, pour que tous les clips de la vidéo suivent la même.

`mesurer_derive.py` [Mesure ici : 300 ms de décalage et 50 ppm de dérive simulés sur 10 min, retrouvés à 1 ms près ; positif = le son arrive plus tard dans l'enregistreur]. Les deux fichiers doivent commencer à moins de 5 s l'un de l'autre, et les fenêtres tomber sur de la parole :

```python
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
```

### 2.5 Ordre de travail

Passes distinctes (skill §3). (1) Synchroniser le son séparé (§2.4). (2) Éditer la parole pendant le dérush (§3) et traiter la voix **après**, pour ne pas traiter des prises jetées (Judd) [Tuto]. (3) Poser la chaîne voix (§4) après validation du dérush, sans défaire les coupes de Cabezer. (4) Poser SFX, musique, ambiances, puis mixer (§8). (5) Exporter et mesurer le MP4 (§9, §10).

---

## 3. Montage du dialogue

### 3.1 Placer une coupe de parole et affiner ses bords

**Quand** : toutes familles. **Pourquoi** : Whisper étire les mots et tronque les mots longs, donc ses temps ne suffisent jamais (skill §4, §5). Le montage par le texte sert à **repérer et pré-découper** ; chaque coupe est ensuite recalée à la forme d'onde et à l'énergie du son. Un recollage ne crée jamais une affirmation que Cabezer n'a pas faite (skill §5).

**À la main** :
1. Cibler les pistes, zoomer jusqu'à l'image (raccourcis : lire dans Raccourcis clavier, sinon menu).
2. Ajouter un point de montage (Séquence > Ajouter un point de montage ; libellé à confirmer) là où l'énergie du mot retombe au niveau du bruit de fond, puis fermer le trou.
3. Contrôler le raccord : forme d'onde et retranscription de 1 s autour de la coupe (`ffmpeg -ss <t-0.5> -t 1 -i export.mp4 -vn fenetre.wav`). Cabezer valide à l'écoute.

**Critère** : aucun début de mot avalé, consonne finale tronquée, clic ni saut du fond de pièce.

#### Outil d'affinage : `affiner_bords.py`

**Quand** : à chaque dérush, surtout en D (coupes serrées) et près d'un mot protégé. **Éviter** : musique ou ambiance sur le plancher de bruit (passer la voix seule) ; rapport signal/bruit faible (presque tous les mots sortent « DOUX ») : couper à la main.

**Pourquoi un outil.** Dans le code de Whisper, les temps de mots viennent de l'attention croisée et d'un alignement temporel dynamique ; des « hacks » tronquent les mots longs aux frontières de phrase et de segment, à deux fois la durée médiane des mots (médiane plafonnée à 0,7 s) [Doc lue : `whisper/timing.py`]. Un « partiiii » étiré peut recevoir une fin trop courte ; `--word_timestamps` est marqué expérimental [Doc lue : `transcribe.py`]. WhisperX (alignement forcé wav2vec2) et stable-ts (suppression de silence) resserrent les temps [Doc lue : README] mais s'installent seulement avec l'accord de Cabezer.

**Étapes** :
1. **Transcrire** en local : `whisper rush.wav --language fr --model <modèle> --word_timestamps True --output_format json --output_dir mots/` [Doc lue : options de `transcribe.py`]. Noter modèle et version dans `Suivi/journal.md`. Si Whisper saute des passages, transcrire par tranches en ajoutant leur décalage.
2. **Lancer** (voix seule si possible) : `python3 -I affiner_bords.py rush.mov mots/rush.json affinage.csv`.
3. **Lire le CSV** : bord Whisper, bord proposé, écart en ms, plancher, pic, drapeaux. Les bornes sont des **candidats**, jamais appliquées sans contrôle ; Claude ne les valide pas seul.
4. **Reporter** les bornes dans la séquence à la main ou par le script de montage prévu : l'outil ne coupe rien.

**Règles de l'algorithme** (valeurs de départ, non étalonnées sur la voix de Cabezer) :
- Énergie RMS par pas de 5 ms sur 20 ms, audio mono 48 kHz. **Plancher** = 10e centile dans ±1 s autour du mot ; **seuil** = plancher + 6 dB.
- **Sortie** : si Whisper finit en pleine énergie, avancer tant qu'elle dure ; s'il finit trop tard, reculer à la dernière trame énergique. Silence exigé : 20 ms sous le seuil. Marges gardées : 10 ms après l'énergie, 20 ms avant l'attaque.
- **Mots doux** (pic à moins de 15 dB du plancher) : seuil à plancher + 3 dB, drapeau `DOUX_A_ECOUTER` ; jamais de coupe sur un mot doux sans écoute de Cabezer.
- **Mots protégés** (« parti », « enfin », « waouh ») : recherche étendue à 1,5 s au-delà de la borne Whisper, drapeau `PROTEGE_A_ECOUTER` ; vérifier que la sortie tombe après l'extinction réelle.
- Autres drapeaux : `SANS_SILENCE` (borne de repli, couper à la main), `COLLE` (touche le mot précédent), `WHISPER_TROP_COURT` (fin proposée plus de 150 ms après celle de Whisper), `GRAND_ECART` (plus de 250 ms), `MOT_SANS_ENERGIE`.

```python
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
    W=[dict(w, mot=w["word"].strip()) for s in json.load(open(js, encoding="utf-8"))["segments"] for w in s.get("words", [])]
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
```

**Test** [Mesure ici] : 7 mots synthétiques sur un plancher à −58 dBFS, dont un mot doux, deux mots collés à 50 ms et un « partiiii » de 1,6 s ; bornes Whisper décalées jusqu'à 150 ms, une fin tronquée de 1,1 s. Bornes retrouvées à 25 ms près (marges comprises), « partiiii » étendu, mot doux marqué. Aucune parole réelle testée.

**Étalonnage obligatoire avant confiance** : comparer les bornes à 10 coupes d'un montage validé par Cabezer (Milan v05), consigner l'écart moyen, ajuster seuil et marges.

**Contrôle indépendant de la fin d'un mot protégé** : `silencedetect` à −40 dB / 0,1 s (ligne « fin d'un mot protégé », `organisation-livraison-qc.md §6`), seuil environ 10 dB au-dessus du bruit d'une pause du même rush [À vérifier, à calibrer par rush]. Sans options, `silencedetect` prend −60 dB et 2 s [Doc lue : FFmpeg] : toujours passer les seuils. Une sortie avant le premier `silence_start` coupe l'exclamation.

### 3.2 Fondus de raccord et clics

Un clic naît d'une coupe en pleine amplitude. Premiere ne cale pas sur un passage par zéro [À vérifier]. Règle : **fondu seulement là où un clic ou un saut de fond est audible**, 1 à 2 images (33 à 67 ms à 29,97 i/s) **dans le silence**, ou deux images clés de volume. **Jamais en masse sur les coupes serrées de dégustation, jamais sur l'attaque d'un mot.**
- Un fondu centré sur une coupe serrée mord le mot suivant (skill §4) : le mettre sur le silence qui précède, passer à 1 image ou utiliser des images clés.
- Transition par défaut : Séquence > Appliquer la transition audio par défaut (libellé à confirmer) ; raccourci à lire dans Raccourcis clavier. Pas de traitement en masse.
- Types : Gain constant, Puissance constante, Fondu exponentiel (Constant Gain, Constant Power, Exponential Fade ; à confirmer). Puissance constante entre deux clips différents ; fondu exponentiel en fin de morceau (skill §11).
- Sans transition : deux images clés sur 1 à 2 images de la ligne de volume (Cmd + clic, geste à confirmer).

### 3.3 Coupes en J et en L

Le son précède (J) ou déborde (L) l'image pour lier deux plans. Permis s'ils ne mordent pas l'attaque d'un mot. Procédure : dissocier audio et vidéo (clic droit > Dissocier, à confirmer) ou sélectionner l'audio seul (Option + clic, à confirmer) ; décaler le bord audio, vidéo immobile ; contrôler écho et synchro labiale.

| Famille | Usage |
|---|---|
| S, F, P, T | Oui, pour relier deux plans ou laisser vivre une réponse. H : selon le brief |
| D | Rare (le skill privilégie les coupes franches) ; **jamais sur la bouchée ni la réaction**. Équivalent utile : la voix qui continue sur un plan produit sans parole (skill §5) |

**Éviter** : sur un mot protégé ; sur les inserts muets.

### 3.4 Respirations, bruits de bouche, blancs

- **D** : couper respirations et blancs de plus de 0,25 s dans les monologues, garder réactions et échanges (skill §5). Deep Breath (payant) est inutile.
- **S** : garder les pauses qui portent un regard, une émotion, une attente ; couper celles où il cherche ses mots (skill §6, prime sur la coupe au dernier mot).
- **F, P, T** : règle du skill §4 inchangée ; pauses d'émotion de P et verdict de F : question pour Cabezer (§15).
- Une respiration restante s'atténue de quelques dB par images clés, jamais jusqu'au silence numérique. Plosives : passe-haut (§4), sinon baisser le clip sur 1 à 2 images.

### 3.5 Harmoniser le niveau entre prises sans Auto Match

1. Mesurer chaque segment de la voix exportée seule (les prises à corriger sont repérées par la mesure, puis par l'écoute de Cabezer) : `for seg in "0 8" "8 6"; do set -- $seg; ffmpeg -hide_banner -nostats -ss $1 -t $2 -i voix.wav -vn -af ebur128 -f null - 2>&1 | awk '/Summary/{s=1} s&&/I:/{print $2,$3}'; done` [Mesure ici] (chaque couple « début durée » est un clip).
2. Corriger par le **gain du clip** ; viser moins d'environ 1,5 LU d'écart dans une scène [À vérifier]. Un segment de moins de 3 s est peu fiable.

---

## 4. Chaîne de traitement de la voix

Mêmes réglages fixes sur tous les clips + un limiteur unique sur la piste. Construire la chaîne une fois, l'enregistrer comme préréglage, la coller partout (Édition > Coller les attributs, Paste Attributes ; ne cocher que les effets audio).

### 4.1 Ordre et valeurs de départ

Ordre consensuel : passe-haut, EQ soustractif, expandeur ou réduction de bruit, compresseur, gain de sortie, limiteur [Tuto Judd, Levine]. Valeurs de **départ**, à faire valider à l'écoute ; Judd les donne pour un direct, sur sa voix [Tuto].

| Étage | Départ | Piège |
|---|---|---|
| Passe-haut (Égaliseur paramétrique, Parametric Equalizer) | 70 à 90 Hz | La parole descend rarement sous 80 Hz (le 46 Hz de Judd est un défaut de mélangeur) |
| EQ soustractif | Balayer une bande étroite en boost, baisser le médium agressif d'environ 5 dB, élargir | Judd : agressif vers 1 kHz sur sa voix. Levine : boue vers 150–350 Hz, acidité vers 5,5–8,5 kHz |
| Réduction de bruit | Seulement si le bruit gêne, sans excès | Trop poussée : son ondulé (Film Riot, Levine) |
| Expandeur / gate (effet Dynamique, Dynamics) | Plage d'environ −9 dB plutôt que −18 | Évite l'effet « on/off » (Judd) |
| Compresseur | Seuil environ 6 dB sous les crêtes, 2:1, attaque rapide, relâchement environ 100 ms | Réduction de 2 à 4 dB sur les phrases fortes |
| Limiteur (un seul, sur la piste) | Plafond vers −2 à −3 dB | Réduction de moins de 3 dB, sinon corriger en amont |

Levine recommande l'Égaliseur paramétrique, le plus « musical » des EQ natifs [Tuto]. Réparations : effets natifs ou Son essentiel > Réparation [libellés à confirmer]. DeHum : 50 Hz en Europe. Dé-esseur : seulement si les « s » piquent. Déréverbération : dégrade vite le timbre [Tuto Levine].

### 4.2 Piège de libellé : « Dynamique »

Le skill interdit la « Dynamique » d'**Essential Sound** (curseur Clarté > Dynamique, qui pilote compression, expansion et gate d'un coup). L'**effet** Dynamique (Dynamics, Amplitude et compression) est un autre outil, manuel, utilisé ci-dessus. Ne pas les confondre.

### 4.3 Voix à exclure

« Améliorer la parole » est **interdit par défaut** : il change le timbre ; la V2 tourne dans le cloud et consomme des crédits [Extrait : communauté Adobe] ; des sifflantes altérées sont signalées [Extrait : forum Adobe]. Voix inexploitable : proposer de reprendre la prise ; seul Cabezer peut rouvrir l'outil.

**Critère** : même timbre du premier au dernier clip, pas de pompage, aucun bruit de fond qui monte dans les pauses (solo, puis mix).

---

## 5. Musique, ducking, nappe de Story

### 5.1 Quand en mettre [Skill §2, §11]

**D** : absente par défaut ; noter « musique : absente par choix ». **F, T** : selon l'émotion réelle (question, découverte, doute, verdict, humour), pas à chaque produit. **S** : nappe presque continue sous la narration, plus basse ou absente sous une source qui parle, vrai silence de 1 à 2 s avant une bascule, montée ou impact avant un concept clé. **P** : bibliothèque perso après écoute d'extraits. Ne pas déplacer une réaction pour suivre la musique.

**Vitesse** : tout morceau fini (bibliothèque, musique de film, composition livrée) garde sa **vitesse d'origine**. Un ajustement de tempo (`atempo`) ne concerne qu'une composition faite de boucles, méthode désormais secondaire (skill §11).

### 5.2 Monter un morceau

Découper par **sections** (intro, action, retombée), pas à l'aveugle [Tuto Film Riot].
Repérer les temps forts sur la forme d'onde (les morceaux de bibliothèque sont souvent en 4/4, par phrases de 4 à 16 mesures [Extrait : Motion Array]) ; couper **sur un coup de percussion ou un temps fort**, avant l'entrée d'une section. Avec des stems, retirer les percussions juste avant un événement pour un silence tendu, puis relancer [Tuto Film Riot]. Faire finir une montée (riser) **exactement** sur l'événement.

### 5.3 Fins de morceau et de vidéo

- Fin sur un temps fort ou une résolution, jamais un accord coupé ; fondu exponentiel sur une phrase complète.
- **S** : vrai accord qui s'éteint sur le noir, après le regard silencieux de Cabezer ; aucun bruitage sur le fondu [Skill §6].
- **Remix** (Son essentiel) réarrange un morceau pour une durée donnée ; F, S, P, T avec musique seulement, pas pour une musique composée sur mesure. Selon un tutoriel il peut appliquer 1 à 2 % de variation de vitesse [Extrait : LensVid, non vérifié]. **Toléré seulement si la vitesse reste celle du morceau** : superposer une section non réarrangée à l'original, les pics de percussion doivent coïncider [À vérifier] ; sinon, couper à la main sur les temps forts.

### 5.4 Ducking

**Quand** : F, T, P avec musique sous narration. **Éviter** : nappe de Story (courbe à la main, §5.5) et D. Valeurs de départ de référence (`premiere-pro-avance.md §11` y renvoie).

**Automatique (Son essentiel)** [Tuto Levine 2019, 2023 ; menus à confirmer] :
1. Étiqueter : voix = Dialogue, musique = Musique, ambiances = Ambiance, SFX = SFX/Effets sonores.
2. Sélectionner la musique, cocher l'atténuation automatique (Ducking) contre Dialogue.
3. Régler Sensibilité, Atténuation, Durée du fondu. Départ (démo 2019) : atténuation de −12 dB ramenée vers −6 dB ; −18 dB (défaut) beaucoup trop fort ; fondu de 0,4 à 0,5 s, 0,8 s trop long ; ambiance sous voix : 3,5 à 4 dB. La démo de 2023 retient des fondus plus longs (0,5 à 1,1 s) : valeurs d'auteur, à régler à l'écoute.
4. « Générer les images clés » (libellé à confirmer), à refaire après chaque réglage. **Régénérer écrase les retouches manuelles** : retoucher après.

**Manuel** : quatre images clés de volume par passage : descente 0,3 à 0,5 s avant le premier mot, maintien, remontée 0,5 à 1 s après la dernière syllabe, en Bézier, jamais linéaire (skill §7). Une musique mixée fort demande plus de 6 dB sous la voix (Levine) [Tuto].

### 5.5 Nappe de Story : environ 24 dB sous la voix

**Règle** : nappe à **environ 24 dB sous la voix**, consigne la plus récente (30/09 bis) ; la valeur de 15 dB est périmée. **Mesure** : écart en LU entre les LUFS court terme de la voix et de la musique, **sur les passages où la voix parle**. Réglage final à l'écoute de Cabezer, qui confirme le chiffre à son prochain aperçu.

1. Exporter voix seule et musique seule en WAV 48 kHz.
2. Calculer l'écart médian des séries court terme (S), en ne gardant que les instants où la voix dépasse −45 LUFS court terme (seuil à calibrer) [Mesure ici : écart de 30,1 LU retrouvé sur des signaux de test] :

```bash
S() { ffmpeg -hide_banner -nostats -i "$1" -af ebur128 -f null - 2>&1 | grep -E "t: .* S:" | sed -E 's/.* S: *(-?[0-9.]+).*/\1/'; }
paste <(S voix.wav) <(S musique.wav) | awk '$1>-45 {print $1-$2}' | sort -n | awk '{d[NR]=$1} END{printf "n=%d ecart median = %.1f LU\n", NR, d[int((NR+1)/2)]}'
```

3. Consigner l'écart mesuré et la cible de 24 dB (un écart de faders n'est pas cet écart : le timbre compte).

Vrai silence avant une bascule : couper la **musique** (descente rapide, Bézier), garder le fond de la pièce de la voix (skill §4) ; un silence numérique pur sonne comme un trou.

---

## 6. SFX et sound design

### 6.1 Principes

- **Un SFX appartient à un élément** : si l'élément disparaît, le SFX aussi (skill §5). Le plus gros mouvement reçoit le son le plus marqué.
- **Audibles mais pas envahissants**, réglés dans le mix complet ; ni sur les bouchées et réactions ni en accents multipliés (skill §11).
- **Sources** : D = banque Pixabay dédiée (`Tiktok degustation/SFX-Pixabay/`, licences dans `LICENCES-SFX.md`) et **liste fermée** du skill (swoosh, pop, ding, boing, scratch, caisse, photo, scintillement), ni mèmes vocaux ni boom. F, S, P, T = bibliothèque ouverte (Cabezer-Sons-Vol1, Cabezer-Ajouts-Food-Lifestyle, Adobe Stock, toute source sous licence). Chaque son va dans `Suivi/licences.csv` ; jamais de son prélevé d'une vidéo TikTok ou d'un tutoriel.

### 6.2 Caler un SFX sur une image dans Premiere

**Défaut (skill) : caler sur l'attaque**, le swoosh sur son pic.
1. Importer le SFX, **rogner le silence de tête** pour que le début du clip soit l'attaque.
2. Zoomer jusqu'à l'image ; placer l'attaque (swoosh : le pic) sur l'image où le mouvement arrive.
3. Superposer au plus deux couches : un impact sec et une queue brève. Régler le niveau dans le mix complet.

**Essai A/B facultatif** (procédure unique) : sur un extrait, comparer −1, 0 et +1 image par rapport à l'attaque, à volume normal. Adopté seulement avec la validation de Cabezer sur plusieurs vidéos (§15) ; sinon le calage reste sur l'attaque.

**Whip entre deux lieux** (skill §5.1) : pic du swoosh sur l'image la plus floue. **Zoom lent façon Micode** : pas de whoosh (skill §7).

### 6.3 Synchroniser son et animation dans After Effects

L'animation est en calques AE natifs, rendue en ProRes 4444 alpha, **sans audio guide en doublon** ; le son définitif se pose dans Premiere. Procédure [À vérifier : aucune transcription AE lue] :
1. Importer l'audio de repère et afficher sa forme d'onde (calque > Audio > Formes d'onde, Waveform ; libellé à confirmer).
2. Poser un marqueur de calque à chaque temps fort (Calque > Ajouter un marqueur, Layer > Add Marker ; à confirmer).
3. Caler les images clés d'impact sur ces marqueurs et noter chaque image d'impact pour les SFX. Un script AE peut lister les temps des images clés (propriété `keyTime`, en secondes à convertir en images) [À vérifier sur copie ; statut d'ExtendScript : `premiere-pro-avance.md §13.3`].
4. Dans Premiere, placer le SFX à l'image correspondante (décalage de la composition inclus). Avant le rendu, **supprimer ou couper** l'audio guide (skill §14).

La conversion de l'audio en images clés donne un mouvement mécanique : réserver à un visualiseur [À vérifier].

### 6.4 Foley alimentaire

**Défaut : aucun foley d'aliment** : jamais sur une bouchée ni une réaction (le skill interdit de les recouvrir et de suggérer une expérience non vécue, §8), pas sur un insert muet sans accord. Sources lues : articles de prestataires seulement [non fiable]. Si Cabezer accepte (§15) : insert de préparation à action visible (versement, friture), bas niveau, SFX rattaché à un élément et consigné. En S : pas de bruitage d'objet gratuit (skill §2).

---

## 7. Ambiances et room tone

### 7.1 Room tone

Capturer **10 à 20 s de silence de la pièce** sur chaque lieu [Tuto Levine].
- Sans room tone enregistré : chercher une pause de 1 à 3 s sans respiration, avec `silencedetect` à −45 dB / 1 s (ligne « room tone », `organisation-livraison-qc.md §6`), seuil à calibrer.
- Boucler en alternant les morceaux (un segment répété s'entend), fondus aux deux bouts, environ 1,5 dB sous l'original (Levine). **Seulement dans les trous** : sous la parole, les niveaux s'additionnent et le fond monte.

**Critère** : on ne perçoit pas où le fond a changé à une coupe.

### 7.2 Ambiance d'un lieu

[Skill §11, méthode du 28/09, à valider] **F, S, P, T** : sous les inserts muets et aux changements de lieu, une ambiance discrète du lieu, prise dans les rushs, sinon d'une banque licenciée. Sous la voix, jamais au détriment des bouchées ; la poser **avant** le premier plan du lieu, fondus d'entrée et de sortie. Niveau assez bas pour qu'on remarque son absence plus que sa présence, fixé à l'écoute (aucun chiffre sourcé), écart mesuré comme au §5.5.

**D : aucune ambiance continue ni musique.** Une ambiance discrète sous un insert muet est une question pour Cabezer (§15) ; défaut : aucune.

---

## 8. Mixage

### 8.1 Hiérarchie et procédure

Hiérarchie : voix, puis SFX narratifs (sous la voix quand ils se chevauchent), musique, ambiance à peine perceptible.
1. Voix seule homogène ? 2. Ajouter SFX, musique, ambiance ; ducker (§5.4). 3. Vérifier crêtes et niveau intégré sur le MP4 (§9, §10). 4. Livrer l'aperçu en disant que Claude n'a pas écouté, et demander la validation auditive (skill §11) : volume normal, casque, petit haut-parleur, mono.

### 8.2 Automation dans Premiere [Tuto Levine, 56 min]

- **Automation de piste** (Mélangeur de pistes audio, Audio Track Mixer) : ne suit pas un clip déplacé ; pour un montage figé. **Automation de clip** (Mélangeur de clips audio, ou images clés dans Commandes d'effets) : suit le clip ; à préférer pour ducking et niveaux.
- Ne pas mélanger images clés dessinées et mode d'écriture (Toucher, Latch, Écriture) sur un même paramètre ; piloter par l'interface avec des **images clés dessinées**, plus prévisibles.
- Gate : automatiser le **seuil**, pas le contournement (bypass : il fait cliquer). Panoramique inutile, voix centrée.

---

## 9. Loudness : mesure et repères

Cette section fait foi pour le loudness ; le skill §13 et les autres fiches y renvoient.

### 9.1 Règles

- **−14 LUFS intégrés = repère de contrôle (±1), pas une cible imposée** (règle de Cabezer).
- **Crête vraie du MP4 ≤ −1 dBTP**, repère consigné. Audio livré : AAC, 48 kHz, 320 kbit/s.
- **Si la crête dépasse, baisser d'abord la source fautive** (SFX, musique). Pas de limiteur de bus maître sans accord de Cabezer (§15).
- Mesurer le **MP4 exporté**, jamais la timeline (skill §13) ; consigner les mesures réelles.
- Voix seule sans musique : si −14 exige plus de 3 dB de limitation, ne pas écraser la voix ; consigner et signaler à Cabezer (§15).

Vocabulaire : **I** = LUFS intégré, niveau perçu moyen ; **court terme** (3 s) et **momentané** (400 ms) = lectures glissantes ; **LRA** = écart entre passages forts et faibles ; **crête vraie (dBTP)** = crête réelle entre les échantillons.

### 9.2 Ce qui est connu, ce qui ne l'est pas

| Sujet | État |
|---|---|
| EBU R128 | −23 LUFS, ±0,5 LU (±1 LU en direct), crête vraie maximale −1 dBTP [Extrait : éditions 2014 et 2020]. Le filtre `ebur128` prend −23 par défaut et note que le contenu en ligne préfère parfois −16 LUFS [Doc lue : FFmpeg]. Sans objet pour le web |
| YouTube | Aucune page officielle lue. −14 LUFS cité par des tiers, repris par le skill comme repère. **Non confirmé** |
| TikTok, Reels, Shorts | Aucune source officielle ; valeurs de tiers contradictoires (−13 ; −14 à −16 ; −10 à −12). **Non vérifié** |
| Spotify, AES77 | Non lus ; AES77 (parole −18 LUFS) connu par la presse, **non retenu** (audio seul) |

### 9.3 Surcrête à l'encodage, `loudnorm`, mono

- Sur deux bruits synthétiques limités, l'AAC a relevé la crête vraie de +0,1 à +0,7 dB à 320 kbit/s, +0,2 dB à 192, +1,5 à +1,8 dB à 128 et +3,1 dB à 96 [Mesure ici, ordre de grandeur]. Les plateformes ré-encodent souvent plus bas : la marge de −1 dBTP évite l'écrêtage côté spectateur.
- Ne pas corriger le fichier avec `loudnorm` : très loin de la cible, il passe en mode dynamique (test : −13,99 LUFS mais `normalization_type: dynamic`) [Mesure ici]. Corriger dans Premiere, ré-exporter ; `loudnorm` sert à mesurer.
- Piège mono : `ebur128` traite une entrée mono en « dual mono » si `dualmono=true`, loi de panoramique −3,01 dB par défaut [Doc lue : FFmpeg] ; un même signal mono mesuré sur un canal vaut 3 dB de moins qu'une copie sur deux canaux (−32,4 contre −29,4 LUFS) [Mesure ici]. Mesurer le MP4 **tel que publié** (stéréo), jamais une piste mono isolée.

### 9.4 Test de plateforme, une fois par famille [À vérifier, à valider par Cabezer]

1. **Base maison** : mesurer ses reels de référence (`Tiktok degustation/References-Cabezer/`) et ses vidéos Story publiées (commande du §10) ; information, pas cible.
2. YouTube : vidéo test **non répertoriée** à niveau connu ; une atténuation affichée dans les statistiques du lecteur = la plateforme baisse le niveau [intitulé à vérifier]. TikTok et Reels (brouillon ou privé) : comparaison à l'oreille avec des reels de la même famille.
3. Consigner par plateforme et proposer à Cabezer pour le skill.

---

## 10. Contrôle du MP4

Commandes exécutées avec ffmpeg 6.1.1 [Mesure ici], à lancer sur le MP4 exporté. Elles signalent des cas à revoir, sans remplacer le visionnage ni l'écoute de Cabezer. **Bibliothèque unique** (blancs −35 dB / 0,25 s, son manquant −50 dB / 0,5 s, fin de mot −40 dB / 0,1 s, `ffprobe`, blackdetect, freezedetect) : `organisation-livraison-qc.md §6`. Ces détecteurs ne remplacent pas la méthode étalonnée des blancs du skill §5.2 (18 dB sous le 80e centile sur 4 s, voix seule), seule utilisée pour la note de rétention.

**1. Niveau intégré, plage, crête vraie** :
`ffmpeg -hide_banner -nostats -i montage.mp4 -vn -af ebur128=peak=true -f null - 2>&1 | awk '/Summary/{s=1} s&&/(I:|LRA:|Peak:)/'`
Critère : I proche du repère (±1), Peak ≤ −1. `peak=true` mesure la crête vraie sur signal suréchantillonné [Doc lue : FFmpeg].

**2. Écrêtage** :
`ffmpeg -hide_banner -nostats -i montage.mp4 -vn -af "astats=measure_perchannel=none:measure_overall=Flat_factor+Peak_level+Peak_count" -f null - 2>&1 | grep -E "Peak|Flat"`
`Flat_factor` mesure les échantillons consécutifs de même valeur aux crêtes [Doc lue : FFmpeg]. Test : signal sain, Flat factor 0 et 2 crêtes ; signal écrêté, 35 et plus de 100 000 crêtes identiques [Mesure ici]. Beaucoup de crêtes à la même valeur = écrêtage à corriger en amont.

**3. Compatibilité mono** :
`for m in "pan=mono|c0=0.5*c0+0.5*c1" "pan=mono|c0=c0"; do echo "$m"; ffmpeg -hide_banner -nostats -i montage.mp4 -vn -af "$m,ebur128" -f null - 2>&1 | awk '/Summary/{s=1} s&&/I:/{print $2,$3}'; done`
Opposition de phase parfaite : −70 contre −32,4 LUFS (test). Somme mono plus basse de plus de 3 à 4 dB que le canal gauche = problème de phase [repère de pratique, à vérifier].

**4. Écart entre stems** : §5.5.

---

## 11. Procédures Premiere et After Effects, libellés

Aucun libellé de cette fiche n'a été lu sur la machine de Cabezer ; l'interface est probablement en français. Confiance forte : Son essentiel (Essential Sound), Égaliseur paramétrique, Coller les attributs, effet Dynamique. Moyenne : Mélangeur de clips et de pistes audio, Appliquer la transition audio par défaut. Faible, à lire à l'écran : Loudness Meter, types de fondu, Fusionner les clips. Libellés et raccourcis lus : `Suivi/environnement-verifie.md` (`pilotage-environnement-reprise.md`).

**Mesurer dans Premiere** : panneau Loudness Meter (Fenêtre ou espace de travail Audio), qui mesure sans modifier le son [Extrait : aide Adobe]. Lire toute la séquence, puis comparer à la mesure ffmpeg de l'export, qui fait foi.

**Scripts** : ils préparent et contrôlent, ils ne remplacent pas l'écoute. Il n'est pas vérifié qu'ExtendScript ou UXP exposent les images clés de volume audio : **ne pas promettre d'automatiser ducking ou mixage par script** avant un test sur copie (`premiere-pro-avance.md §13.3`, `pilotage-environnement-reprise.md`). Un export FCP XML décrit les coupes audio pour un audit sans transporter fidèlement tous les effets (`premiere-pro-avance.md §13.1`). Pour contrôler voix, musique et SFX, exporter chaque piste seule (WAV 48 kHz, 24 bits) ; menu d'export à confirmer.

---

## 12. Application par famille

- **D** : coupes serrées via `affiner_bords.py`, blancs de plus de 0,25 s coupés, « Bref, c'est partiiii » entier ; musique absente ; SFX Pixabay de la liste fermée ; aucune ambiance ni foley ; pas de J/L sur la bouchée ni la réaction.
- **F** : règle de coupe du skill §4 ; J/L possibles ; musique selon l'émotion, ducking automatique puis retouche ; bibliothèque SFX ouverte ; ambiance par lieu possible.
- **S** : pauses qui portent gardées ; voix uniforme ; nappe à environ 24 dB sous la voix mesurée (§5.5), silences avant bascule, fin sur accord, courbe tracée à la main ; chapitre = carton seul ~3 s avec signature musicale ; pas de bruitage d'objet gratuit.
- **P** : J/L fréquents, ambiances de scène ; bibliothèque perso après écoute ; sound design pour un moment dramatique.
- **T** : voix claire avant tout ; clic de souris, riser, whoosh aux transitions marquées. **H** : demander le brief, mesurer, consigner.
- **Toutes** : repère −14 LUFS (±1), crête vraie ≤ −1 dBTP, mesures sur le MP4 ; synchronisation double système si le son est séparé (§2.4).

---

## 13. Erreurs de débutant → réflexes de pro

| Erreur | Réflexe |
|---|---|
| Couper aux temps de la transcription | Pré-découper au texte, recaler à l'énergie (`affiner_bords.py`) et à la forme d'onde |
| Croire la fin d'un mot étiré donnée par Whisper | Chercher l'extinction réelle ; drapeau `PROTEGE_A_ECOUTER` |
| Fondu de raccord sur un début de mot ou posé en masse | Fondu dans le silence, 1 à 2 images, ou images clés ; seulement où un clic s'entend |
| Fusionner caméra et enregistreur sans contrôle | Trois points de contrôle, dérive mesurée, méthode consignée |
| Remonter une prise basse avec le gain | Baisser le gain du clip ; reprendre la prise si trop de bruit |
| Auto Match, Dynamique ou Améliorer la parole sur la voix | Chaîne fixe sur tous les clips, niveau réglé à la main et mesuré |
| Musique au niveau de la voix | Ducker ; nappe de Story mesurée à 24 dB ; contrôle au petit haut-parleur |
| Mesurer la timeline | Mesurer le MP4 exporté |
| Écrire « écouté » pour une mesure | « Mesuré » ou « validé par Cabezer », jamais confondus |

---

## 14. Liste de contrôle

**Avant** : [ ] format, fréquence, canaux de chaque rush notés ; son séparé synchronisé, dérive mesurée (§2.4) ; dérush validé. [ ] Pistes nommées ; inserts muets sans audio source.

**Pendant** :
- [ ] Chaque coupe contrôlée (forme d'onde, retranscription) ; drapeaux de l'outil d'affinage traités ; aucun début de mot coupé ; fins étirées entières.
- [ ] Fondus dans le silence, seulement où un clic s'entend ; room tone seulement dans les trous.
- [ ] Chaîne voix identique partout, un limiteur unique ; musique absente en D, selon l'émotion ailleurs, ducking retouché, nappe de Story mesurée.
- [ ] SFX rattachés à un élément, calés sur l'attaque, audibles, au registre des licences ; aucun audio guide AE en doublon.

**Après export** :
- [ ] I, LRA, crête vraie mesurés et consignés ; crête ≤ −1 dBTP ; aucun écrêtage ; somme mono comparée au canal gauche.
- [ ] Blancs et trous listés ; appel au commentaire entier ; AAC, 48 kHz, 2 canaux, environ 320 kbit/s, mesuré sur ce fichier.
- [ ] Écoute demandée à Cabezer ; statut « mesuré » ou « validé par Cabezer ».

---

## 15. Décisions à demander à Cabezer

Chaque défaut s'applique en attendant sa réponse.

| Question | Défaut en attendant |
|---|---|
| Nappe de Story : confirmer environ 24 dB sous la voix à son prochain aperçu ? | 24 dB mesurés (§5.5), réglage final à son écoute |
| Limiteur de sécurité sur le bus maître, en plus de celui de la piste voix ? | Non : baisser la source fautive |
| Auto Match toléré pour égaliser des morceaux de musique entre eux ? | Non : égalisation à la main |
| Foley d'aliment sur un insert muet (versement, friture) ? | Aucun foley |
| Ambiance discrète du lieu sous un insert muet en dégustation ? | Aucune ambiance en D |
| Voix seule en D qui exige plus de 3 dB de limitation pour atteindre −14 ? | Ne pas écraser ; mesure consignée et signalée |
| Conserver pauses et respirations aux moments d'émotion de P et au verdict de F ? | Règle du skill §4 inchangée |
| Essai A/B du calage des SFX (−1, 0, +1 image) ? | Pas d'essai ; calage sur l'attaque |
| Installer un alignement forcé (WhisperX, stable-ts) ? | Non : Whisper local et `affiner_bords.py` |
| Remplacer le repère −14 par la base mesurée de ses reels ? | Non : −14 (±1), base mesurée à titre d'information |
| Moment de la validation auditive ? | Aperçu, puis export final |

---

## 16. Sources étudiées

« Transcription lue » = lue en entier (sous-titres automatiques non relus). Aucune vidéo visionnée.

**Documentation et code lus**
- FFmpeg, `doc/filters.texi` (miroir GitHub), https://raw.githubusercontent.com/FFmpeg/FFmpeg/master/doc/filters.texi : `silencedetect` lue en entier (défauts −60 dB et 2 s), `ebur128` jusqu'à l'option `gauge` (cible −23 LUFS, `peak`, `dualmono`, `panlaw`, remarque sur −16 LUFS en ligne), `astats` par ses définitions (`Peak_level`, `Flat_factor`).
- OpenAI, Whisper, `whisper/timing.py`, https://github.com/openai/whisper/blob/main/whisper/timing.py : temps de mots, troncature des mots longs (lignes 290 à 385 lues) ; `whisper/transcribe.py` (options, `--word_timestamps` expérimental) ; `whisper/utils.py` (écriture JSON).
- jianfch, stable-ts (README), https://github.com/jianfch/stable-ts : suppression de silence, VAD ; installation non testée.
- Max Bain, WhisperX (README), https://github.com/m-bain/whisperX : alignement forcé wav2vec2 et limites ; installation non testée.

**Transcriptions lues**
- Curtis Judd, « My YouTube Audio Workflow », 2021-04-11, https://www.youtube.com/watch?v=SsRexob7faM : ordre de traitement.
- Curtis Judd, « 32-bit float recorders & differences in audio quality », 2025-07-06, https://www.youtube.com/watch?v=mxWH8V5BaYk : gain, bruit.
- Curtis Judd, « ATEM Mini Sound Settings », 2020-05-03, https://www.youtube.com/watch?v=j4RLCBd3Q64 : dynamique d'un direct.
- Jason Levine, « How to use Auto-Ducking for Dialogue & Ambient Sound Design in Premiere Pro », 2019-05-23, https://www.youtube.com/watch?v=n1-MQuhSHos : ducking.
- Jason Levine, « How to Level/Match Loudness between Multiple Dialogue Clips », 2019-04-19, https://www.youtube.com/watch?v=82bcQnmdwVc : Auto Match.
- Jason Levine, « VIDEO MASTERCLASS | The Essentials: Mixing Sound », 2022-06-03, https://www.youtube.com/watch?v=POHgJLl-FZg : faders, EQ, room tone.
- Jason Levine, « Sound Mix Automation in Premiere Pro », https://www.youtube.com/watch?v=zFfkSsTOEoA (date non récupérée) : automation.
- Film Riot, « How to Edit Music to Your Film », https://www.youtube.com/watch?v=ie7PIe1Jwnk (date non récupérée) : stems, riser.
- Film Riot, « Fix Your AUDIO with One Button », https://www.youtube.com/watch?v=7K7wGfdVzNQ (date non récupérée ; partenaire d'un éditeur de plugins payants) : limites de la restauration.

**Extraits de recherche, pages non ouvertes** : EBU R 128 (éditions 2014 et 2020) ; tutoriels de synchronisation Premiere (ProVideo Coalition, Emerson, Adobe Learn) ; forums DVinfo et Sound Devices sur la dérive d'horloge ; aide Adobe (Son essentiel, Enhance Speech, Loudness Meter, Remix) ; aide YouTube ; LensVid ; Motion Array ; prestataires de foley. Fiches voisines : `premiere-pro-avance.md`, `fondamentaux-montage-narratif.md`, `formats-courts-verticaux.md`, `retention-youtube-long.md`, `organisation-livraison-qc.md`.

**Non obtenus** : quatre vidéos (Levine ne1q-Ljy1gY, Judd Z21jajLVEZ8, Film Riot xqfyVu40V_o et VJ8HEfA5tLg), refus anti-bot non contourné ; livre de John Purcell, *Dialogue Editing for Motion Pictures* (métadonnées seulement). Aucune transcription After Effects sur la synchronisation son/animation ; aucune source primaire pour le loudness des plateformes ni pour l'interface française de Premiere.
