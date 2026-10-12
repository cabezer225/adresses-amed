# Premiere Pro niveau expert : gestes avancés, rushs hétérogènes, plans défaillants

> **Réponses de Cabezer du 12/10/2026 — elles priment sur cette fiche**, en particulier sur sa section « Décisions à demander ». **Format d'abord, famille ensuite (SKILL §2)** : long (L-Food, L-Story, L-Tech, L-Films, L-Life) ou court (C-Food, C-Story, C-Tech, C-Films, C-Life) ; codes de cette fiche : D = C-Food, F = L-Food, S = L-Story, P = L-Films, T = L-Tech ; nouvelle famille Lifestyle (vlogs, face caméra : aucune musique, SFX comme la dégustation). **Tous les courts** : hook demandé, sous-titres mot à mot, aucune musique, SFX comme la dégustation, punch-ins secs, appel au commentaire, notation sur 10, identité propre au court. **Longs** : SRT seul en France ; composition musicale en Story, food et tech ; respirations d'émotion gardées en films/séries et au verdict du food long ; 4K si rushs 4K. Aussi : identité Story v15 et générique « Amed Story 🧢 » supprimés ; jamais de foley d'aliment ; ambiance en dégustation proposée au premier usage ; un rendu de sous-titres par passage ; intervenants identifiés à la première apparition (hors courts food) ; au plus deux passes de retravail sous 8 ; Tesseract, Higgsfield et SCANDALE FOOD retirés. **Réponses techniques (série 3)** : interface de Premiere et d'AE en anglais ; scripts AE et Terminal autorisés ; stock libre de droits sans redemander ; tout SFX de la banque Pixabay permis ; arrêt sur image permis partout ; pas de test de photosensibilité ; audio YouTube 384 kbit/s ; proxys ProRes Proxy toujours en format long (en court seulement si la lecture saccade) ; Production Premiere au-delà de 20 min ; cadence de séquence = caméra principale ; son externe qui dérive resynchronisé par morceaux (étirement en dernier recours) ; Morph Cut seulement sur demande ; flux optique, Object Mask / Object Matte, « Synthesize Edges » et MOGRT interdits ; pas de repli de sous-titres sans AE ; Frame.io pour les relectures ; WhisperX à installer ; « 19h30 » et « 12,50 € » ; Liquid Glass à recréer. Liste complète : `../decisions-en-attente.md`.

Fiche de référence pour piloter Premiere comme un monteur professionnel, dans le cadre des règles de Cabezer. Dernière vérification : 12/10/2026. Les numéros de version, la table des versions et le test de fumée des scripts vivent dans `pilotage-environnement-reprise.md` ; cette fiche ne les répète pas.

**Niveaux de preuve** (utilisés partout) :
- **[Adobe]** : extrait de page d'aide ou de notes de version Adobe vu dans un résultat de recherche. Les pages Adobe n'ont pas pu être ouvertes en entier (proxy).
- **[Presse]** : plusieurs articles concordants, ou un seul article cité comme tel.
- **[Tuto]** : transcription ou extrait de tutoriel ; valeur d'auteur, pas une règle.
- **[Mesure]** : testé ici avec ffmpeg 6.1.1 et Python sur des fichiers générés, pas sur un export réel de Cabezer.
- **[À vérifier]** : non confirmé ; à tester sur sa version avant usage.

## Quand lire cette fiche

Lire cette fiche avant tout geste avancé dans Premiere : dérush assisté, projet long, proxys, cadence et rushs hétérogènes, enregistreur externe, multicam, arrêt sur image, accéléré, ralenti, plan défaillant, incrustation, recadrage vertical, échange avec After Effects (AE), export, scripts ou XML. Rythme, récit et transitions : `fondamentaux-montage-narratif.md`. Identité visuelle et animations : skill §6 et `after-effects-motion-design.md`.

Cette fiche ne remplace ni le brief ni le skill (ordre : brief, skill, fiches, tutoriels). Chaque technique dit **quand l'utiliser, quand l'éviter, pour quelles familles** : dégustation (D), food long (F), Cabezer Story (S), films/séries PRISME (P), tech (T), hors familles (H).

## Sommaire

1. Principes de pilotage et de vérification
2. Outils IA : trois statuts
3. Projet, montage long, proxys, préférences, cadence et rushs hétérogènes
4. Édition de précision
5. Dérush assisté : texte, scènes, recherche, masquer un jump cut
6. Multicam et synchronisation en double système
7. Vitesse, ralenti, accéléré, arrêt sur image
7 bis. Corriger un plan défaillant sans IA
8. Recadrage vertical, mouvements, sous-titres, incrustation
9. After Effects : Dynamic Link et rendu
10. Couleur sous gestion des couleurs
11. Audio : ce que Premiere automatise
12. Export
13. Échanges, XML, scripts
14. Erreurs de débutant → réflexes de pro
15. Liste de contrôle
16. Décisions à demander
17. Sources étudiées

---

## 1. Principes de pilotage et de vérification

**Pourquoi** : les menus changent à chaque version majeure. L'interface de Premiere et d'After Effects est en **anglais** (réponse du 12/10/2026) : les libellés anglais font foi, les noms français ne sont qu'un repère.

1. **Lire la version et le nom affiché** : Premiere > About. Selon la presse (PetaPixel, DigitalProduction, janvier 2026), le logiciel s'appelle « Adobe Premiere » depuis la 26.0 : le menu peut afficher ce nom. « Premiere » désigne ici l'application quelle que soit la version. Consigner dans `Suivi/environnement-verifie.md`.
2. **Aucun raccourci tant qu'il n'est pas lu** dans Premiere > Keyboard Shortcuts (Raccourcis clavier) de la machine ; sinon passer par le menu. Les raccourcis cités sont des défauts courants, **à confirmer** ; l'AZERTY change plusieurs touches.
3. **Libellés** : nom anglais d'abord, repère français entre parenthèses ; chercher à l'écran le libellé anglais ; un libellé non lu à l'écran est « à confirmer ». Séparer appliqué, contrôlé, validé par Cabezer (skill §1).
4. **Tout essai risqué se fait sur une copie** (Enregistrer sous une nouvelle version). Régler l'enregistrement automatique à 5 minutes et 20 versions, dans Premiere et dans After Effects (réponse du 12/10/2026), et noter les valeurs dans `environnement-verifie.md` plutôt que se fier aux défauts [Adobe : valeurs par défaut].
5. **Une technique de tutoriel est un point de départ** : régler les valeurs à l'œil sur le plan réel. Claude n'entend pas : il contrôle par mesures, transcription et forme d'onde ; l'écoute finale revient à Cabezer.

---

## 2. Outils IA : trois statuts

Table de référence : **skill §16**. Application dans Premiere :

- **Aides autorisées, résultat toujours vérifié** : transcription et montage par le texte (§5.1), détection des changements de plan (§5.2), recherche Media Intelligence (§5.3), Auto Reframe comme point de départ (§8.1), suivi et Roto Brush sur un vrai plan (§8.4), Warp Stabilizer (Stabilisation de la déformation, §7 bis, traitement d'un plan filmé), traduction de légendes **relue**. Paper Edit (construit une séquence depuis des lignes du panneau Texte [Adobe : notes de version, extrait]) relève du montage par le texte.
- **Seulement sur demande explicite de Cabezer** : Morph Cut, Content-Aware Fill (Remplissage d'après le contenu), Generative Extend, Generative Media Tool, tout outil Firefly ou de génération ou reconstruction de pixels. Generative Extend génère jusqu'à 2 s d'images ou 10 s d'audio au bord d'un clip, consomme des crédits [Adobe : FAQ, extrait] et envoie un extrait hors de la machine : le consigner si Cabezer l'autorise.
- **Interdits par défaut (règle de Cabezer)** : Enhance Speech (« Améliorer la parole », change le timbre), Auto Match (Correspondance automatique), curseur Dynamics d'Essential Sound (Clarity en est l'équivalent, §11), images ou animations générées par IA (voix ou musique produites par un modèle génératif : seulement sur demande explicite, skill §16).
- **Interdits (réponse du 12/10/2026)** : Optical Flow (flux optique : il interpole des images à partir d'images existantes), masques assistés Object Mask (masque suivi cliqué, calculé sur l'appareil [Presse]) et Object Matte, « Synthesize Edges » de la stabilisation (§7 bis), modèles MOGRT (§8.3). À la place : masques manuels, suivi (tracking) et Roto Brush vérifié (§8.4) ; ralentis sur rushs 50/60p, sinon Frame Blending (mélange de trames) (§7.1).

**Si un plan manque d'une demi-seconde**, utiliser dans cet ordre : un autre plan réel, un arrêt sur image sur une image réelle (§7.3), un ralenti d'insert en mélange de trames, un fondu. Une image absente des rushs ferait passer du faux pour du réel (skill §8).

---

## 3. Projet, montage long, proxys, préférences, cadence

### 3.1 Structure du projet et montage long

Arborescence unique : `organisation-livraison-qc.md §2.1`. Ne pas la redéfinir.

**Montage de plus de 20 minutes (toutes familles)** : utiliser une **Production** Premiere (réponse du 12/10/2026) [Tuto : Levine et Soulet, Adobe, 2020 ; interface datée]. Le dossier de production vit dans `Projet/` et ne contient que des projets ; les médias restent dans `Media/`, référencés. Un projet léger par tâche (rushs, B-roll, sélections), la bibliothèque de sons à part. Ajouter un projet par clic droit dans le panneau Production (libellé à confirmer), jamais en le déplaçant dans le Finder. Dossiers numérotés avec écarts (01, 02, 05, 10). **En dessous de 20 minutes** (dégustation courte comprise) : un projet unique suffit.

**Architecture d'un montage long (20 à 40 minutes)** :
1. Une séquence maîtresse à plat pour la voix ; une séquence par chapitre seulement pour les passages à habillage lourd, imbriquée dans la maîtresse au dernier moment, nommée du titre court et de la version.
2. Marqueurs de chapitre ; export FCP XML pour auditer (`retention-youtube-long.md §3`).
3. Fin de session : Enregistrer sous, une ligne dans `Suivi/journal.md`, la liste de ce qui reste, un aperçu MP4 léger avec timecode par chapitre terminé.
4. Verrouiller par passes (dérush, structure, habillage, couleur, son, sous-titres) ; après verrouillage, aucune retouche sans Enregistrer sous.
5. Rendre les éléments AE par chapitre.

### 3.2 Proxys

**Quand** : **format long, toujours** (réponse du 12/10/2026), quelle que soit la famille. **Format court** : seulement si la lecture saccade (multicam, plans 4K à plusieurs couches, Mac qui ne lit pas en temps réel). Décision de fond : `organisation-livraison-qc.md §3.2`.

1. File > Project Settings > **Ingest Settings** (Réglages d'ingestion) > Create Proxies [Tuto : Premiere Gal 2025].
2. **ProRes Proxy, un quart de la taille, dossier séparé des rushs** (réponse du 12/10/2026 : toujours ce format en format long), sans repli en H.264. Confirmer par un essai sur un rush de Cabezer. Un rapport de 2025 signale, sur Mac Apple Silicon, un gel de lecture avec des proxys ProRes 422 issus de HEVC 10 bits DJI 5K, évité en H.264 [Adobe Community, un seul fil] : si ce gel se produit sur un rush de Cabezer, le signaler et le noter dans `Suivi/decisions.md` avant tout changement de format.
3. Bouton Toggle Proxies (« Basculer les proxys ») du Program Monitor (Moniteur Programme, libellé à confirmer).
4. **Avant tout export** : proxys désactivés, puis `ffprobe` sur le MP4 pour vérifier la résolution, sans se fier aux affirmations contradictoires sur le comportement de l'export.

### 3.3 Préférences

D'après Larry Jordan (Premiere 25) [Tuto, un auteur ; libellés à vérifier] : gestion des couleurs d'affichage activée ; fichiers en croissance non actualisés ; cache média vidé chaque mois ; 6 à 12 Go laissés aux autres applications ; indicateurs de désynchronisation activés. Déplacer le cache avant d'ouvrir le projet. Versions natives Apple Silicon de Premiere et d'AE.

### 3.4 Cadence, séquence et rushs hétérogènes : arbre de décision

**Pourquoi** : Cabezer mélange Pocket 3, iPhone, Panasonic, stock, enregistrements d'écran ; chaque rush doit entrer proprement dans la cadence de sortie.

**Étape 0 : inventorier.** Pour chaque rush : `ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,profile,pix_fmt,width,height,r_frame_rate,avg_frame_rate:stream_side_data=rotation -of default=nw=1 rush.mov` [Mesure]. Consigner le tableau (fichier, taille, cadence, codec, rotation) dans `Suivi/brief.md`, section Médias.

**Étape 1 : créer la séquence avec les paramètres du brief** (taille, cadence, pixels carrés), par File > New > Sequence. **Ne pas glisser un média sur « New Sequence »** : elle prendrait ses réglages. Si Premiere propose de changer la séquence, répondre « Keep Existing Settings » (Conserver les paramètres existants, libellé à confirmer) [Tuto : Larry Jordan].

**Étape 2 : choisir la cadence de la séquence** = celle de la **caméra principale** (réponse du 12/10/2026 ; visage, Pocket 3), lue par `ffprobe` et notée dans `Suivi/brief.md` ; les autres plans sont conformés à cette cadence.

| Rush | Décision | Réserve |
|---|---|---|
| Même cadence que la séquence | Rien à faire | — |
| 50 ou 59,94 i/s dans une séquence 25 ou 29,97 | Lecture à vitesse réelle (une image sur deux) ; **ralenti propre jusqu'à 50 %** (§7.1) | Ne pas « interpréter » en 29,97 pour conformer : le clip passe à 50 % de vitesse [Adobe Community, un fil] |
| 25 i/s dans une séquence 29,97 (ou l'inverse) | Accepter l'écart, ou conformer une copie ; tester 10 s de panoramique | Flux optique interdit (§2) ; micro-saccades possibles [À vérifier] |
| **Cadence variable** (iPhone, enregistrement d'écran, visioconférence) | Conformer une **copie** en cadence constante avant import : `ffmpeg -i rush.mov -fps_mode cfr -r 30000/1001 -c:v prores_ks -profile:v 3 -c:a pcm_s24le copie_cfr.mov` ; l'original reste intact | Détection : `r_frame_rate` ≠ `avg_frame_rate` (`organisation-livraison-qc.md §3.3`). Téléphones et outils de capture produisent souvent du VFR, avec dérive audio dans Premiere [Presse : Streaming Learning Center]. Si le résultat reste variable, essayer la cadence exacte de la séquence |
| **Enregistrement d'écran du Mac** (T) | Même traitement ; vérifier par `ffprobe` (VFR non confirmé pour macOS) | Texte lisible : ni rampe de vitesse ni zoom flou |
| **Vertical (iPhone, 9:16) dans une séquence 16:9** | Lire la rotation ; **fond = flou du même plan, plan net au centre** (réponse du 12/10/2026) : dupliquer le clip sur la piste du dessous, le mettre à l'échelle pour couvrir tout le cadre et lui appliquer un Gaussian Blur (flou gaussien) ; sur le clip net au-dessus, clic droit > Set to Frame Size (Définir à la taille de l'image) ; **jamais étirer** | Méthode classique [Tuto : Larry Jordan] ; ce flou de fond ne vaut que pour le plan vertical, pas pour un flou simulé sur un rush |
| **Archive 4:3 dans une séquence 16:9** | Plan net au centre, **bandes sur le fond de l'identité** de la famille (réponse du 12/10/2026) ; **jamais étirée**, pas de fond flou | — |
| **HEVC ou H.264 10 bits, 4:2:2, long-GOP** | Lire codec, profil, `pix_fmt` ; si la lecture saccade en format court, proxys ; en format long ils sont déjà générés (§3.2) | Décodage matériel 4:2:2 sur Mac ARM annoncé en 2021 [Adobe Community] : statut actuel à vérifier |
| Stock | Conformer à la cadence et au cadre avant import (skill §14) | Licence dans `Suivi/licences.csv` |

**Étape 3 : mode d'échelle.** Set to Frame Size (« Définir à la taille de l'image ») affiche l'échelle réelle (4K en 1080 : 50 %), Scale to Frame Size (« Mettre à l'échelle ») affiche 100 % ; lire le mode actif avant d'écrire « zoom 115 % » ou un XML. Interpret Footage (« Interpréter le métrage ») change la cadence d'un clip sans trace visible : le noter dans `Suivi/decisions.md`.

**Critère** : tableau des médias rempli, aucune dérive audio, aucune image dupliquée visible sur un panoramique, MP4 à la cadence du brief.

---

## 4. Édition de précision

Raccourcis cités = défauts courants, **à confirmer** (§1) ; sinon passer par le menu.

- I / O : entrée / sortie. Cmd+K : point de montage sur les pistes ciblées. Q / W : supprimer jusqu'au point de montage précédent ou suivant et fermer le trou [Tuto]. Activer ou désactiver un clip : trois tutoriels, trois raccourcis ; utiliser le menu Clip.
- **Ciblage des pistes** : le bouton V1/A1 détermine où agissent « Ajouter un point de montage », « Supprimer et fermer » et le ripple. Cibler avant tout ripple. Sync Lock (verrou de synchronisation) activé pour garder musique et voix alignées, désactivé pour une piste d'habillage figée.
- **Trois points** : deux marques d'un côté, une de l'autre ; Premiere calcule le quatrième. **Roll** déplace un point de coupe sans changer la durée ; **slip** change le contenu d'un clip sans le déplacer ; **slide** le déplace entre ses voisins.
- **Nest** (imbriquer) : regroupe des clips pour régler un effet d'ensemble ; réinitialise recadrage et point d'ancrage (skill §16). Le nommer ; éviter pour ce qu'on retouche souvent.
- **Adjustment Layer** (calque d'effet) : applique un effet à tous les plans dessous (grain commun).
- **Transitions** : `fondamentaux-montage-narratif.md §5.4` ; les transitions animées sont construites dans AE (skill §1).

**Critère** : aucun trou involontaire, aucune piste décalée par rapport à la voix.

---

## 5. Dérush assisté

### 5.1 Montage par le texte (Window > Text)

**Procédure** [Tuto : Jason Levine, Adobe, 2023] : transcrire, identifier les intervenants, **relire** (noms propres et mots rares souvent faux), régler la longueur de pause (défaut cité : 0,75 s), sélectionner une ellipse pour créer entrée/sortie puis supprimer en ripple. Couper-coller des blocs réordonne la timeline.

**Règle** : le montage par le texte **repère et pré-découpe** ; chaque coupe est ensuite **recalée à la forme d'onde et à l'énergie du son, jamais aux temps de transcription** (skill §4). Ne rien supprimer en masse.
- **D** : le seuil du skill est 0,25 s ; le défaut de 0,75 s est trop large. Descendre le seuil si le panneau le permet [À vérifier], sinon couper à la main. Garder réactions et échanges ; relire chaque suppression de mots parasites.
- **S** : « supprimer toutes les pauses » est interdit ; garder les respirations qui portent un regard ou une émotion (skill §6). En P (moments d'émotion), au verdict de F et en L-Life posé, garder aussi les respirations (réponse du 12/10/2026).
- **F, T, P** : usage libre pour entretiens et voix off, avec relecture. Détection de pauses : régression signalée en 26.3 [source secondaire, à vérifier].
- **Corrections** : retirer un faux départ pour garder ce que Cabezer voulait dire (« trois mozzarelles ») est permis ; jamais un collage qui crée une affirmation qu'il n'a pas faite ni ne change le sens.

**Critère** : aucun mot coupé, aucune syllabe du mot suivant mangée ; chaque raccord testé.

### 5.2 Détection des changements de plan

Clic droit sur un clip > détection des changements de plan (libellé à confirmer) : coupe à chaque point, sous-clips ou marqueurs [Tuto]. **Quand** : réutiliser un montage existant, trier un reportage de référence. **Éviter** : rushs de dégustation (peu de ruptures franches).

### 5.3 Recherche de médias (Media Intelligence)

Préférences > Analyse des médias et transcription ; panneau de recherche, filtres Visuels / Texte / Métadonnées [Adobe : article de lancement]. Analyse locale. **Recherche visuelle en anglais seulement** [Adobe, à vérifier] : traduire les requêtes (« bite of pizza »). Pas d'OCR. **Quand** : S, P, grosses archives. **Éviter** pendant un montage actif (l'analyse ralentit la machine).

### 5.4 Masquer un jump cut : hiérarchie

1. **Coupe franche assumée** ou **punch-in sec** à la coupe (D) : changement instantané, 100 → 115 % par clé maintenue ou deux clips (§8.2).
2. **Plan de coupe** qui apporte quelque chose, posé avant la coupe (skill §6 point 10 : jamais un B-roll qui répète).
3. **Second angle synchronisé** (§6).
4. **Animation** seulement si un titre était déjà prévu (skill §5.1 : aucun élément ajouté pour relancer l'image).

**Morph Cut** (Video Transitions > Dissolve > Morph Cut) : **seulement sur demande de Cabezer** (réponse du 12/10/2026), jamais proposé comme solution par défaut ; déconseillé en D (bouche, gestes). Conditions Adobe : un seul sujet, caméra fixe, fond statique et uniforme, tête grande dans le cadre, mains hors cadre [Adobe : page d'aide, extrait]. Contrôler image par image que la bouche ne se déforme pas.

**Critère** : aucune saute visible à vitesse réelle, aucune déformation en pause sur trois images.

---

## 6. Multicam et synchronisation en double système

### 6.1 Multicam

**Quand** : S, F (même scène, plusieurs caméras), tournages Pocket 3 + iPhone + Panasonic (skill §12). **Éviter** : plans qui ne se recouvrent pas.

1. Appliquer la chaîne couleur propre à chaque caméra (`etalonnage-gestion-couleur.md §9`), puis correspondance sur la caméra principale.
2. Sélectionner les clips > clic droit > **Create Multi-Camera Source Sequence** (Créer une séquence source multicaméra) ; synchroniser par **audio**, contrôler sur un clap ou un son net [Tuto : Premiere Gal 2025 ; Javier Mercedes].
3. **Audio** : le meilleur son comme piste principale, sans mélanger les micros (skill §12). Choisir le réglage de séquence « Caméra 1 », ou ouvrir la séquence source et ne laisser actif que le meilleur micro. **Ne pas choisir « Switch Audio » (Changer l'audio) ni « All Cameras » (Toutes les caméras)** : l'audio suivrait l'angle et mélangerait les micros.
4. Clic droit sur la séquence source > Nouvelle séquence avec clip ; vue multicam du Moniteur Programme ; changer d'angle en direct. Pour couper un angle, couper un micro ou étalonner : ouvrir la séquence source.

**Pièges** : mono et stéréo mélangés (double mono avant) ; caméra qui coupe toutes les 30 minutes (monter ses fichiers dans une séquence, imbriquer, puis multicam).

**Critère** : voix continue sans saut de micro, lèvres synchrones en trois points (début, milieu, fin).

### 6.2 Double système : enregistreur ou micro externe (32 bits flottant)

**Quand** : toute prise où la voix vient d'un fichier séparé de la caméra. Toutes familles ; indispensable en S et F. **Éviter** de mélanger l'audio caméra et le fichier externe (phase, écho).

1. **Identifier les fichiers.** `ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,sample_rate,channels,bits_per_sample -of default=nw=1 f.wav` ; un WAV 32 bits flottant affiche `pcm_f32le` [Mesure]. Même fréquence (48 kHz) sur l'enregistreur et la caméra. Si l'enregistreur livre une **piste normale et une piste de sécurité** (gain plus bas), monter avec la normale ; ne jamais empiler les deux (phase).
2. **Synchroniser.** Sélectionner la vidéo et le WAV > clic droit > **Merge Clips** (Fusionner les clips, libellé à confirmer) > point de synchronisation **Audio** ; cocher **« Remove Audio from AV Clip »** (Supprimer l'audio du clip AV) [Tuto : plusieurs guides concordants]. L'audio caméra sert de guide ; les originaux restent dans `Media/`. La commande Synchroniser opère sur la timeline sans créer de clip. Plusieurs caméras : monter le fichier externe dans le multicam (§6.1) ou fusionner chaque caméra avec lui.
3. **Contrôler en trois points** (début, milieu, fin de prise) à l'image près, sur un clap ou une consonne nette ; tolérance : ± 1 image. L'œil juge la fermeture des lèvres ; la forme d'onde juge l'attaque.
4. **Dérive.** La commande Synchroniser ne corrige pas une dérive interne à un fichier ; il faut retimer [Presse : ProVideoCoalition, extrait]. La dérive peut ne pas être linéaire [Tuto : forum Audacity]. Ordre de travail :
   - Éliminer les causes : fréquences différentes, rush à cadence variable (§3.4).
   - Mesurer l'écart au début, au milieu et à la fin avec `references/pro/scripts/mesurer_derive.py` (ci-dessous). Ordre de grandeur (calcul, non sourcé) : à 50 ppm d'écart d'horloges, une image à 29,97 i/s (33 ms) apparaît en ~11 minutes.
   - Écart de moins d'une image sur la prise : accepter.
   - Sinon (réponse du 12/10/2026), **resynchroniser par morceaux : couper la prise en segments à des pauses et resynchroniser chacun**. **L'étirement est le dernier recours**, seulement si aucune coupe n'est possible dans la prise (parole continue) : modifier légèrement la vitesse du clip audio (Speed/Duration, facteur calculé depuis la dérive mesurée, par exemple 99,97 % ; « Maintain Audio Pitch » coché, libellé à confirmer), ou `ffmpeg -af atempo=<facteur>` sur une copie ; refaire les trois points et noter l'étirement dans `Suivi/decisions.md`.
   - Noter la méthode dans `Suivi/decisions.md` : tous les clips suivent la même.
5. **Niveau 32 bits flottant** : une crête positive est normale ; **baisser** le gain du clip au lieu de remonter une prise basse (`audio-dialogue-sound-design-mixage.md §2.3`).

**Script de mesure de dérive** : `python3 -I references/pro/scripts/mesurer_derive.py camera.mov externe.wav`. Le script lit lui-même l'audio de chaque fichier par ffmpeg (mono, 16 kHz), mesure le décalage enregistreur − caméra sur des fenêtres de 20 s au début, au milieu et à la fin (recherche à ± 5 s) et l'affiche pour chaque point ; la dérive est la différence entre le dernier et le premier. Il ne fait que lire : il se lance sans redemander.

[Un essai antérieur sur signal synthétique retrouvait un décalage de 500 ms et une dérive de 0,03 % à ± 15 ms près ; précision insuffisante pour juger seul : contrôler à l'image.]

**Critère de réussite** : voix synchrone aux trois points, une seule source de voix dans la séquence, méthode consignée.

---

## 7. Vitesse, ralenti, accéléré, arrêt sur image

### 7.1 Ralenti, rampe, interpolation

Le skill autorise les rampes **uniquement sur les inserts**, jamais sur la parole ni la bouchée retenue (§7).

- **Speed/Duration** (Vitesse/durée) : valeur fixe. Temporal Interpolation (« Interpolation temporelle ») : **Frame Sampling** (échantillonnage de trames : défaut, rapide, saccadé), **Frame Blending** (mélange de trames : doux, fantômes) ; **Optical Flow** (flux optique : images estimées, déformations) est **interdit** (réponse du 12/10/2026) [Presse, Adobe Learn extraits].
- **Time Remapping** (remappage temporel) : afficher les images clés de vitesse, ajouter des points, tirer la courbe ; poignées de Bézier pour adoucir (skill §7 : jamais linéaire pour un mouvement progressif).
- **Cadence** : vérifier la cadence réelle avant de promettre un ralenti. 25 ou 30 i/s ralentis à 50 % donnent un ralenti saccadé ; 50 ou 60 i/s ralentis à 50 % donnent un ralenti propre (§3.4).
- Ralenti de 100 à 70–90 % : mélange de trames. **Pas de flux optique** (réponse du 12/10/2026) : un ralenti marqué se fait sur un rush 50/60p, sinon en mélange de trames, ou la vitesse réelle est gardée. Rendre la plage avant de juger.
- Des interpolations ignorées sur des rampes sont signalées [Adobe Community, un fil, 2025] : vérifier l'export, pas l'aperçu. Remappage temporel inaccessible par script en 26.3 [source secondaire, à vérifier] : les rampes se font à la main.

**Quand** : D (préparation, arrivée du plat, versement), F, T (démo d'écran, jamais sur une capture à texte lisible). **Éviter** : S sur la parole. **Critère** : pas d'image dupliquée visible à vitesse réelle, pas de déformation sur mains ni produit.

### 7.2 Accéléré

**Quand** : geste long d'un insert (cuisson, installation, trajet), accumulation (F, T, S, H). **Éviter** : parole ; bouchée ou réaction (D) ; texte à lire.
1. Clip > Vitesse/durée : valeur supérieure à 100 %. Cocher « Ripple Edit, Shifting Trailing Clips » (Montage par ondulation, déplacer les clips suivants) pour ne laisser aucun trou [Tuto : guides, libellés à confirmer].
2. Interpolation : échantillonnage de trames ; le mélange crée des fantômes [À vérifier à l'œil]. À très haute vitesse, le geste devient saccadé : préférer deux coupes sèches sur les moments clés.
3. Audio : couper le son de l'insert en D (skill §5) ; ailleurs, « Conserver la hauteur audio » (Maintain Audio Pitch) ou son remplacé. Un accéléré marqué est un mouvement rapide : whoosh calé sur le mouvement, sous la voix (skill §7).
**Critère** : le geste reste lisible, la durée gagnée correspond au brief.

### 7.3 Arrêt sur image

**Quand** : **permis dans tous les formats** (réponse du 12/10/2026), dégustation comprise, pour désigner un détail (ticket, prix, document) pendant qu'une annotation AE le désigne ; prolonger de moins d'une demi-seconde la fin d'un plan (image réelle, donc hors IA) ; poser une capture d'image réelle. **Éviter** : plan portant la parole (lèvres figées) ; arrêt sur image qui ne désigne rien (il se lit comme un plan gelé, `organisation-livraison-qc.md §6.3`).
1. **Add Frame Hold** (ajouter un arrêt sur image) fige de la tête de lecture à la fin du clip ; **Frame Hold Options** (options d'arrêt sur image) choisit l'image (entrée, sortie, tête de lecture) ; **Insert Frame Hold Segment** (insérer un segment d'arrêt sur image) fige au milieu d'un clip sans l'arrêter [Tuto : guides, libellés à confirmer].
2. Changer la durée d'un segment figé par Vitesse/durée peut changer l'image tenue : rogner les bords ou utiliser l'outil Ripple [Adobe Community, un fil].
3. Image fixe vers AE : bouton Export Frame (« Exporter l'image », libellé à confirmer). `freezedetect` signalera le figement : faux positif attendu (`organisation-livraison-qc.md §6.3`).
**Critère** : image tenue nette, sans bouche mi-ouverte ; durée voulue.

---

## 7 bis. Corriger un plan défaillant sans IA

**Principe** : diagnostiquer, corriger avec les outils gratuits sur une **copie**, comparer avant/après, et **savoir refuser un plan**. Aucun Content-Aware Fill ni outil génératif sans demande explicite (§2). Tout outil **payant** est signalé et attend l'accord de Cabezer.

**1. Scintillement et bandes (néon, LED).** Diagnostic : planche d'images consécutives, et luminance moyenne par image : `ffmpeg -i f -vf signalstats,metadata=mode=print:file=- -an -f null - | grep YAVG`. En France, le secteur est à 50 Hz et l'éclairage vacille à 100 Hz ; les bandes naissent quand l'intensité change pendant l'exposition. Au tournage, un obturateur multiple de 1/50 s (1/50, 1/100) limite le défaut ; les LED à modulation PWM ne suivent pas le secteur [Presse : blog Kasson, extrait, photo] : transmettre ce réglage à Cabezer, à confirmer sur ses caméras.
- **Pulsation globale** (YAVG oscille) : le filtre gratuit `deflicker` d'ffmpeg lisse la luminance moyenne. [Mesure sur flicker synthétique : écart-type de YAVG de 12,9 à 1,6 avec `deflicker=size=11:mode=am` ; la médiane sur 25 images n'a rien corrigé.] Sur copie : `ffmpeg -i f.mov -vf deflicker=size=11 -c:v prores_ks -profile:v 3 copie.mov` ; vérifier carnations et produit. Il ne corrige pas la couleur.
- **Bandes qui défilent dans l'image** : le même filtre est sans effet [Mesure : PSNR de 42 dB entre l'original et le résultat]. Aucun correctif natif fiable n'est établi : ne rien promettre ; autre prise ou autre cadrage.
- **Payant, non installé** : Flicker Free (Digital Anarchy) existe ; prix et efficacité à vérifier.

**2. Moiré.** Il vient de la grille de pixels du capteur contre celle de l'écran, pas de l'obturateur [Presse : guides d'extrait]. En T, **préférer la capture d'écran native à un plan filmé**. Sinon, au tournage : changer distance et angle, défocaliser légèrement, changer la résolution de l'écran. En post, un flou masqué réduit le moiré mais abîme le texte.

**3. Instabilité.** Effet **Warp Stabilizer** (Stabilisation de la déformation, libellé à confirmer) ; traitement de plan, permis. Appliquer, **attendre la fin de l'analyse**. Cadrage par défaut « Stabilize, Crop, Auto-scale » (Stabiliser, rogner, adapter) ; méthode Subspace Warp (sous-espace par déformation) puissante mais risque d'effet gélatine, Position, échelle, rotation plus prudente ; réduction de l'ondulation de l'obturateur automatique par défaut [Adobe : page Warp Stabilizer, extrait]. Tester **Smooth Motion** (Mouvement lisse ; lissage 50 % par défaut) puis **No Motion** (Sans mouvement ; effet trépied, seulement si le plan doit sembler fixe) ; surveiller le recadrage automatique, qui agrandit l'image. « Synthesize Edges » (Synthétiser les bords) remplit les bords avec des images voisines : c'est une reconstruction de pixels, **interdite** (réponse du 12/10/2026). Stabiliser et rogner ; si le recadrage nécessaire est trop fort ou si des bords vides apparaissent, **refuser le plan** (point 7). Imbriquer avant une rampe ; éviter sur une bouchée nette. **Critère** : pas de gélatine, bords stables.

**4. Horizon.** Mouvement > Rotation, puis échelle minimale pour couvrir les coins : `cos θ + sin θ × max(L/H, H/L)` [Mesure : calcul]. En 16:9 comme en 9:16 : 1° demande 103,1 %, 2° 106,1 %, 3° 109,2 %. Au-delà, refaire la prise. Protéger yeux, mains, produit.

**5. Bruit.** Premiere n'a pas de réducteur de bruit natif fiable : les sources divergent sur l'effet Médian ou « VR De-Noise » [Presse : guides d'extrait]. Gratuit : `hqdn3d` d'ffmpeg sur copie, `ffmpeg -i f.mov -vf hqdn3d=4:3:6:4.5 -c:v prores_ks -profile:v 3 copie.mov`. [Mesure sur bruit synthétique : PSNR de 28,5 dB à 29,9 dB avec ces valeurs, 31,4 dB avec `8:6:12:9`, mais plus de flou.] Valeurs de départ ; comparer en écran partagé, ne pas lisser la texture du plat. **Payant, non installé** : Neat Video, Red Giant Denoiser (prix à vérifier).

**6. Tache sur l'objectif.** Dans AE, calque dupliqué décalé, masqué et suivi à la main (pixels réels), à tester ; jamais de Content-Aware Fill sans demande explicite.

**7. Plan inutilisable.** Le lister avec raison et minutage, le proposer à Cabezer pour reprise ; ne jamais le « sauver » par un effet qui dégrade le produit.

---

## 8. Recadrage vertical, mouvements, sous-titres, incrustation

### 8.1 Auto Reframe (16:9 → 9:16)

Clic droit sur la séquence > Auto Reframe Sequence (recadrage automatique de la séquence, libellé à confirmer) > 9:16. Premiere crée des images clés de position. Ensuite : corriger Position, Scale, Rotation dans Effect Controls (Contrôles d'effets) là où le suivi dérape.

**Règle** : point de départ, jamais résultat final (skill §12) ; protéger yeux, mains, produit. **Quand** : Shorts tirés d'un long (F, S, T). **Éviter** : deux sujets à garder ensemble ; refaire les textes à l'échelle verticale. Zones sûres : `formats-courts-verticaux.md §6`. **Critère** : visage et produit dans le tiers central.

### 8.2 Mouvements sur plan filmé (traitement de plan, dans Premiere)

Définition unique : skill §1, §16. Éléments **graphiques** (étiquette, prix, pop-up, flash, glitch) : AE (`after-effects-motion-design.md §6, §9`).
- **Punch-in sec** (D) : effet Transform (Transformation) ou Scale de Motion (Mouvement), 100 → 115 % (120 % sur les bouchées), clés « maintenir » ou deux clips voisins d'échelle différente : un changement instantané, pas un mouvement progressif.
- **Zoom façon Micode** (F, S, P, T, en format long seulement) : progressif, Bézier, centré sur le visage, seulement si le moment le sert (skill §7). En court, punch-ins secs uniquement, pas de zoom progressif.
- **Whip entre deux lieux** (C-Food et vlogs C-Life) : 4 à 6 images, échelle jusqu'à 130 %, glissement de 12 %, flou de mouvement, swoosh (skill §5.1). Dans Transformation : décocher « Utiliser le rapport de forme composite » si l'échelle étire l'image.
- **Shake du cadre** d'un plan filmé : dans Premiere, en C-Food seulement (en C-Story, C-Tech et C-Films : punch-ins secs, sans shake ni flash). Le shake d'une étiquette ou d'un prix : dans AE.
- **Mouvement sur une photo ou un document fixe** : seulement pour désigner un détail ou présenter un visage, avec un temps avant et après, courbe douce ; jamais de dérive décorative ; jamais sur un plan qui porte un texte à lire (skill §6 point 11 et §7, « Mouvement sur image fixe »).
- La vitesse constante reste permise pour rotation continue, défilement, compteur, boucle.

### 8.3 Sous-titres et légendes

**Règle par format** (skill §9) :
- **Courts, toutes familles** : sous-titres mot à mot incrustés = **composition AE** à l'identité du court de la famille (entrée animée, texte éditable, rendu ProRes 4444 alpha à la taille de la séquence) + **SRT livré** (`formats-courts-verticaux.md §4`). En dégustation, un rendu par passage validé.
- **Long tourné en France** : **SRT seul, rien d'incrusté** (réponse du 12/10/2026).
- **Long tourné à l'étranger, passages et extraits sonores non français** : sous-titres incrustés en composition AE, 2 lignes maximum (anglais à l'étranger ; français pour un extrait étranger dans une vidéo française).
- La piste de légendes native de Premiere sert de **transcription et de calage** (relire noms et chiffres, tracer le SRT) ; elle n'est jamais le rendu final. « Mettre à niveau la légende » n'est plus utilisé. Limites par famille et langue : `formats-courts-verticaux.md §4.2`.
- **Si After Effects est indisponible** : pas de repli de sous-titres dans Premiere (réponse du 12/10/2026). Décrire le blocage à Cabezer et attendre.
- **Incrustation à l'export** (Burn Captions Into Video, libellé à confirmer) : utile seulement avec une piste de légendes natives. Les sous-titres AE sont des clips vidéo : rien à cocher. Des préréglages basculent parfois l'incrustation en silence [Adobe Community, un fil de 2025] : vérifier le MP4 (ni doublons ni manque). En long tourné en France, la case reste décochée (SRT seul).
- **MOGRT** : non utilisés, dans aucune famille (réponse du 12/10/2026). Tout élément graphique est un rendu AE ProRes 4444 alpha à la taille de la séquence (l'identité DA v2 est faite sur mesure dans AE).

### 8.4 Incrustation sur fond uni et caches de luminance

**Quand** : T, S, F, pour placer Cabezer devant un vrai document ou une capture ; H au brief. **Éviter** : D (la DA v2 rejette les stickers détourés) ; fond froissé ou inégal ; suppression de fond en ligne (sort les rushs de la machine, souvent payante).

**Ultra Key** (Video Effects > Keying ; libellés des réglages à lire à l'écran en anglais), sur copie :
1. Pipette sur le fond (moyenne 5 × 5 pixels conseillée [Adobe, extrait]). **Sortie** sur « Canal alpha » (Alpha Channel) pour voir le cache [Tuto : wiki Evergreen] ; le préréglage **Agressif** élargit la plage retirée [Adobe].
2. **Génération du cache** : Transparence (défaut 45, de 0 à 100), Lumière (Highlight, 10), Ombre (Shadow, 50), Tolérance (50), Socle (Pedestal, 10, filtre le bruit de l'alpha) [Adobe : valeurs par défaut]. Ajuster d'abord Transparence et Tolérance.
3. **Nettoyage du cache** : Contraction (Choke, 0 ; 100 = noyau 9 × 9 [Adobe]) puis Adoucissement (Soften) très léger.
4. **Suppression des reflets** (Spill Suppression) : Désaturer (Desaturate) et Plage (Range) corrigent la couleur du fond sur les bords clairs (cheveux) ; trop forte, elle vire au magenta [Tuto : cours Lynda, extrait].
5. Vérifier sur fond **clair puis foncé** ; bords légèrement adoucis ; ombre portée courte et nette (cohérente avec la DA v2).

**Clé de luminance** (Luma Key) : pour un élément très contrasté (silhouette noire sur blanc). Réglages Seuil (Threshold) et Atténuation (Cutoff) [Tuto : 4kshooters] ; le sens du seuil est incertain dans les sources : **tester sur le plan**.

**Track Matte Key** (cache de piste, libellé à confirmer) : l'effet se pose sur le clip à révéler (V2), le cache sur la piste au-dessus (V3) ; menu Cache = Vidéo 3 ; « Composite avec » = Cache luminance (Matte Luma) pour un cache opaque noir et blanc (le clair révèle), Cache alpha (Matte Alpha) s'il a de la transparence [Adobe : page d'aide, extrait]. Case Inverser non confirmée. Un cache **animé** est une animation graphique : AE, cache de luminance natif (`after-effects-motion-design.md §8.2`).

**Masque d'effet avec suivi** : pour isoler une zone, masque dans l'effet ou dans Lumetri, suivi avant et arrière, contrôle image par image.

**Statuts** : Roto Brush (AE) et suivi (tracking) = aides autorisées, résultat vérifié ; Object Mask et Object Matte = interdits (réponse du 12/10/2026), masques manuels à la place ; aucune restauration générative des bords.
**Critère de réussite** : aucun halo, aucun scintillement du bord sur 3 images consécutives, couleur de peau cohérente avec la scène.

---

## 9. After Effects : Dynamic Link et rendu

Les animations graphiques se font dans AE (skill §1, §16). Module de sortie ProRes 4444 alpha, alpha, `aerender` : `after-effects-motion-design.md §13`. Côté Premiere, trois chemins :

| Chemin | Quand | À éviter |
|---|---|---|
| **Rendu intermédiaire** (ProRes 4444 alpha, à la taille de la séquence) | Éléments finis : étiquette, prix, pop-up, sous-titres | Cabezer retouche souvent le texte |
| **Replace with After Effects Composition** | Un plan à retoucher dans AE avec ses rushs | Des dizaines de clips (lenteur, plantages) |
| **Séquence entière vers AE** | Rare | Montage vivant : un clip déplacé après coup laisse un trou noir [Tuto : Cinecom] |

- La composition hérite des dimensions, du rapport de pixel, de la cadence et de la fréquence audio de la séquence [Adobe]. Une composition par scène, nommée ; `.aep` numérotés (`_v01`).
- **Render and Replace** (rendre et remplacer) : source « clips individuels », codec intermédiaire léger (ProRes 422 usuel, à tester). Le plan est ensuite figé : « Restaurer l'original » pour le retoucher.
- Premiere, AE et Media Encoder à la même version majeure (`pilotage-environnement-reprise.md`).
- **Couleur** : aligner l'espace de la composition sur celui de la séquence (`etalonnage-gestion-couleur.md §13`) ; valider par un test avec et sans passage par AE.

**Critère** : ni trou noir ni média hors ligne ; rendu du MP4 final identique à l'aperçu ; `.aep` à côté des sources.

---

## 10. Couleur sous gestion des couleurs

Principes et chaîne par caméra : `etalonnage-gestion-couleur.md §3`. Ici, les gestes propres à Premiere.

1. **Une seule voie** : soit la conversion automatique de Premiere (détection du log), soit la LUT technique D-Log M → Rec.709 de Cabezer, jamais les deux (skill §10). Pocket 3 : séquence en Rec.709 direct, puis exposition et blancs dans Lumetri, puis LUT Exterior ; iPhone et Panasonic harmonisés à la main, sans Exterior.
2. **Tester sur un plan Pocket 3** : lire l'espace du média (Projet > Propriétés > Couleur, ou Lumetri > Réglages > Clip source). Si Premiere reconnaît le D-Log M et mappe, pas de LUT ; sinon désactiver la détection pour ce projet et appliquer la LUT une fois [À vérifier].
3. **Juger dans le Moniteur Programme**, jamais dans le Moniteur Source : des utilisateurs de 25.x constatent une surexposition dans la source avec détection de log [Adobe Community].
4. Surcharge d'espace d'un média : Lumetri > Réglages > Clip source ; revérifier après réouverture (non conservée signalée en 25.1).
5. Fixer l'espace de travail **avant** d'étalonner. Auto Color et correspondance de couleur : points de départ [Tuto : Levine]. Presets Lumetri conçus pour le Rec.709.

**Critère** : carnation sur la ligne de chair du vectorscope, noirs ni bouchés ni lavés sur le MP4 comparé au plan source.

---

## 11. Audio : ce que Premiere automatise

Chaîne de voix, ducking, fondus de raccord, nappe de Story : `audio-dialogue-sound-design-mixage.md §3.2, §4, §5.4, §5.5`. Conséquences pour Essential Sound (Son essentiel) :
- **Clarity** (compresseur de dialogue) = le curseur Dynamics du skill : interdit. **Enhance Speech** : interdit. **Auto Match** (Correspondance automatique) : interdit, la musique se cale à la main (réponse du 12/10/2026).
- **Remix** : F, S, P, T longs avec musique de bibliothèque ; jamais en format court (aucune musique), ni sur une musique composée sur mesure. Un morceau fini garde sa vitesse d'origine : n'accepter le remix que si la vitesse ne change pas, sinon couper à la main sur les temps forts.
- **Ducking automatique** : étiqueter Dialogue et Musique, cocher Ducking, « Générer les images clés ». Valeurs de départ de `audio §5.4` (la démo de Levine de 2023 donne des durées plus longues : régler à l'écoute). Régénérer **écrase** les retouches manuelles. Exclu pour la nappe de Story (courbe tracée à la main).
- **Fondus de raccord** : seulement là où un clic est audible, dans le silence, 1 à 2 images ou deux clés de volume ; jamais en masse, jamais sur l'attaque d'un mot (`audio §3.2`).
- **Room tone** : combler un trou de fond par le silence de la pièce du même rush (skill §4).

---

## 12. Export

Tableau d'export et cibles : skill §13 ; contrôle du MP4 (ffprobe, blackdetect, freezedetect, silencedetect, ebur128) : bibliothèque unique de `organisation-livraison-qc.md §6`. Ne pas la dupliquer.

- **Libellés** : « Utiliser la qualité de rendu maximale » (Use Maximum Render Quality) et « Rendre à la profondeur de bits maximale » (Render at Maximum Depth) ; libellés à confirmer à l'écran et consignés. Le skill écrivait « Rendu à la résolution maximale », libellé non retrouvé.
- **Débit** : environ 20 Mbit/s VBR 1 passe en vertical est le **débit de Cabezer, non issu d'une source officielle** ; ne pas le changer. Les guides tiers divergent (de 4–8 à 20–30 Mbit/s).
- Après tout changement de préréglage : vérifier la taille de sortie (1080 × 1920) et que les proxys sont désactivés.
- **Loudness** : −14 LUFS intégrés = repère de contrôle (±1), pas une cible ; crête vraie du MP4 **au plus −1 dBTP** ; si elle dépasse, baisser d'abord la source fautive (`audio §9`). AAC 48 kHz 320 kbit/s en format court ; 384 kbit/s pour YouTube long.
- Sous-titres : voir §8.3. **YouTube long** : 3840×2160 si les rushs sont en 4K, sinon 1920×1080, H.264 VBR 2 passages, 1080p 16 Mbit/s (24 en 50/60 i/s), 4K 50 Mbit/s (75), testés sur 60 s avant le premier export, AAC 48 kHz 384 kbit/s (skill §13). **Carré (1:1) et 4:5 : jamais** (réponse du 12/10/2026). Encodage **logiciel** pour le livrable, matériel pour les aperçus ; détails : `organisation-livraison-qc.md §8`.

**Critère** : résolution, cadence, durée conformes au brief ; sous-titres présents une seule fois ; mesures consignées.

---

## 13. Échanges, XML, scripts

### 13.1 FCP XML (voie de secours éprouvée)

- Règles du skill §14 : clips dans l'ordre chronologique par piste ; média sans son déclaré avec son = hors ligne ; ouvrir le XML sans projet ouvert.
- **Ne passent pas toujours** : vitesses variables, imbrications, effets d'extension, étalonnages Lumetri [Presse : Digital Production]. Un fil signale des entrées/sorties décalées vers Resolve pour des clips de cadence différente [Adobe Community]. **Tester un petit échantillon avant l'export complet** (arrêts sur image et changements de cadence compris).
- Audit sans API : exporter en FCP XML puis `python3 -I xml-coupes.py fichier.xml` (jeu de scripts de `organisation-livraison-qc.md` ; `-I` car le XML est non fiable). Résultat = cas à examiner.

### 13.2 OTIO

Import/export OpenTimelineIO présents depuis la bêta d'octobre 2024 [Adobe, notes de version] ; stabilité non confirmée. **Pas sans test** ; préférer FCP XML.

### 13.3 Scripts : alignement ExtendScript, UXP, XML

- **ExtendScript** : utilisé tant que le test de fumée le confirme sur la machine de Cabezer. Selon le guide de scripts de Premiere, Adobe oriente l'extensibilité tierce vers UXP depuis novembre 2025, sans évolution prévue de l'API ExtendScript, dont la prise en charge était annoncée jusqu'en septembre 2026 [Adobe, extrait] ; cette date est passée, aucune annonce de retrait n'a été lue.
- **UXP** : préféré pour un **nouvel** outil dans Premiere ; mode développeur dans Préférences > Plugins ; version minimale non tranchée selon les sources (un responsable de la communauté cite la 25.6) : la **contrôler par le test de fumée**, pas par un numéro. Limite de janvier 2025 : pas d'ajout d'un élément du panneau Projet à une séquence par l'API [Tuto : NT Productions], non revérifiée.
- **XML** : voie de secours pour un premier assemblage et l'audit (13.1).
- **Chaîne d'exécution** (arbre à tester une fois, résultat dans `environnement-verifie.md` ; détail dans `pilotage-environnement-reprise.md`) : ffmpeg et Python dans le Terminal avec `python3 -I` pour tout fichier non fiable, sorties dans `Controles/` ; AE par File > Scripts > Run Script File (Fichier > Scripts > Exécuter un fichier de script ; voie sûre), `aerender -help` d'abord ; Premiere sans menu dédié : panneau UXP chargé par Cabezer, sinon voie XML. Test de fumée : un script qui écrit sa version dans un fichier texte.
- Les scripts de lecture seule (relevés, contrôles) se lancent sans redemander ; tout autre script qui modifie ou copie un fichier s'exécute sur une copie et attend l'accord de Cabezer (skill §3). Exception : les scripts After Effects sont autorisés à écrire des fichiers et à accéder au réseau, et le Terminal à piloter Premiere et AE (Automatisation, Accessibilité, Enregistrement d'écran) (réponse du 12/10/2026). Le compte rendu distingue vérifié et non vérifié.

---

## 14. Erreurs de débutant → réflexes de pro

| Erreur | Réflexe |
|---|---|
| Couper aux temps de la transcription | Pré-découper au texte, régler chaque raccord à la forme d'onde (skill §4) |
| Supprimer toutes les pauses en un clic | Garder les respirations utiles (S), seuil 0,25 s en D |
| Glisser un rush sur « Nouvelle séquence », ou importer un rush à cadence variable | Séquence aux paramètres du brief ; copie conformée en cadence constante |
| « Interpréter » un 59,94 en 29,97 pour conformer | Lire à vitesse réelle ; interpréter seulement pour un ralenti voulu, et le noter |
| Mélanger audio caméra et fichier externe, ou piste normale et de sécurité | Fusionner par l'audio, supprimer l'audio caméra, une seule voix ; mesurer la dérive |
| Exporter sans désactiver les proxys | Livrer des originaux, vérifier la résolution par `ffprobe` |
| Laisser Premiere convertir le log **et** ajouter la LUT, juger dans le Moniteur Source | Une seule conversion ; juger dans le Moniteur Programme |
| Prolonger un plan avec Generative Extend | Autre plan réel, arrêt sur image réel, ralenti d'insert, fondu |
| Morph Cut sur un geste ou un fond mobile | Plan de coupe, punch-in, autre prise ; sur demande explicite seulement |
| Rampe de vitesse sur la parole, ralenti sur un rush 25 i/s | Inserts seulement (skill §7) ; vérifier la cadence |
| Activer Optical Flow pour un ralenti | Ralenti sur rush 50/60p, sinon mélange de trames |
| Stabiliser une bouchée nette, ou laisser « Synthesize Edges » actif | Éviter la bouchée nette ; Synthesize Edges jamais : stabiliser et rogner, sinon refuser le plan |
| Croire que `deflicker` règle les bandes de néon | Il lisse la luminance globale ; changer de prise pour les bandes |
| Déplacer un clip lié à AE après verrouillage | Rendre et remplacer, ou restaurer l'original avant |
| Faire confiance à un raccourci de tuto | Lire la commande dans la fenêtre, ou passer par le menu |
| Laisser un préréglage décider des sous-titres | Contrôler le MP4 : sous-titres une seule fois |

---

## 15. Liste de contrôle

**Avant le montage**
- [ ] Version, nom affiché et `environnement-verifie.md` lus ; projet sur copie ; arborescence de `organisation-livraison-qc.md §2.1`.
- [ ] Tableau des médias rempli ; séquence créée aux paramètres du brief ; cadences variables conformées sur copie ; proxys ProRes Proxy générés (format long ; en court seulement si la lecture saccade).
- [ ] Voix externe synchronisée, trois points contrôlés, méthode de dérive notée.

**Pendant**
- [ ] Pistes ciblées avant chaque ripple ; coupes réglées à la forme d'onde ; aucun mot coupé.
- [ ] Aucun outil génératif ; Morph Cut seulement sur demande de Cabezer ; flux optique, Object Mask / Object Matte et Synthesize Edges interdits.
- [ ] Multicam : un seul micro actif. Rampes, accélérés, arrêts sur image : inserts, cadence vérifiée.
- [ ] Plans défaillants : diagnostic noté, copie comparée, plan refusé listé.
- [ ] Une seule conversion couleur ; animations AE nommées, Dynamic Link sans trou noir.

**Avant l'export**
- [ ] `.prproj` et `.aep` enregistrés sous une nouvelle version ; proxys désactivés ; sous-titres : courts = composition AE + SRT ; long tourné en France = SRT seul, rien d'incrusté ; incrustation native décochée si inutile.

**Après l'export (MP4 réel)**
- [ ] Contrôles de `organisation-livraison-qc.md §6` faits ; crête vraie au plus −1 dBTP ; niveau intégré noté.
- [ ] Visionnage et écoute intégraux par Cabezer ; appel au commentaire présent (skill §4) ; compte rendu : appliqué / contrôlé / validé.

---

## 16. Décisions à demander à Cabezer, et points à vérifier

> **Toutes ces questions ont reçu une réponse de Cabezer le 12/10/2026** : voir `../decisions-en-attente.md`, qui prime sur les défauts ci-dessous.

**Réponses de Cabezer (12/10/2026) et règles appliquées dans cette fiche :**
1. **Flux optique et Object Mask / Object Matte** : non. Masques manuels, suivi et Roto Brush vérifié ; ralentis sur rushs 50/60p, sinon mélange de trames.
2. **Structure Production** : Production Premiere au-delà de 20 min ; projet unique en dessous.
3. **Fond d'un vertical inséré dans un horizontal** : flou du même plan en fond, plan net au centre. Archive 4:3 : bandes sur le fond de l'identité, jamais étirée.
4. **Resynchronisation d'une dérive** : par morceaux ; étirement du son en dernier recours.
5. **Plugins payants** (anti-scintillement, réducteur de bruit) : aucun par défaut (règle du skill, §1) ; signaler nom et prix puis attendre l'accord de Cabezer.
6. **Stabilisation avec « Synthesize Edges »** : non ; stabiliser et rogner, sinon refuser le plan.
7. **Cadence de la séquence** : celle de la caméra principale, lue par `ffprobe`.
8. **Autres réponses appliquées ici** : Morph Cut seulement sur demande ; MOGRT non (rendus AE ProRes 4444 alpha) ; pas de repli de sous-titres sans AE ; proxys ProRes Proxy toujours en format long ; arrêt sur image permis dans tous les formats ; interface de Premiere et d'AE en anglais.

**À vérifier dans l'application, puis consigner dans `environnement-verifie.md`** : raccourcis, libellés « à confirmer » (Merge Clips, Warp Stabilizer, Ultra Key, Track Matte Key, Frame Hold), seuil de pause du panneau Texte, détection du log Pocket 3, UXP et ExtendScript.

**Vidéos non lues** (YouTube bloqué) : Premiere Gal « Fall 2026 Update », Jason Druss (couleur de Premiere 25).

---

## 17. Sources étudiées

Couverture : **T** = transcription lue par le chercheur précédent ; **E** = extrait de résultat de recherche seulement (page non ouverte) ; **L** = testé en local. helpx.adobe.com, community.adobe.com, larryjordan.com, petapixel.com, provideocoalition.com et docsforadobe.dev sont refusés par le proxy ou injoignables : aucune page Adobe n'a été lue en entier.

**Transcriptions (T)**
- Jason Levine, Adobe Live. « Video Masterclass | All the A.I. in Premiere Pro Today » (19/05/2023). https://www.youtube.com/watch?v=PoiOFoa2U0U. Montage par le texte, remix, ducking, Clarity.
- Matt Christensen et Marjorie Sachs, Adobe. « Premiere Pro Best Practices Guide ». https://www.youtube.com/watch?v=o11jX3E3D-0. Échanges, Dynamic Link.
- Jason Levine et Carl Soulet, Adobe. « How to use Premiere Pro Productions as an Individual Editor » (2020). https://www.youtube.com/watch?v=9uRaWEbfERc.
- Premiere Gal. « FASTER Editing with PROXY Files in Premiere Pro 2025 » (https://www.youtube.com/watch?v=JjeZrdBjSWE) ; « Hide Jump Cuts Like a PRO » (https://www.youtube.com/watch?v=wVmi89tBORc) ; « Mastering Multi-Camera Editing » (https://www.youtube.com/watch?v=KnlPOB34Fng).
- Javier Mercedes. « 10 Shortcuts I Use Every Time I Open Premiere Pro » (https://www.youtube.com/watch?v=UfTqLJHfdHQ) ; « 3 Powerful Ways to Use Multicam Sequences » (https://www.youtube.com/watch?v=42oHeDEc0FQ).
- Larry Jordan. « Optimize Preferences in Adobe Premiere Pro v25 » (2025). https://www.youtube.com/watch?v=hXkKUQDAOkc.
- Adobe Live. « Find Any Clip in Seconds! Media Intelligence » (2025). https://www.youtube.com/watch?v=36Hj0wdFftQ. Adobe x filmriot, « Edit Faster With These Hotkeys » (2025). https://www.youtube.com/watch?v=uhw50nxeDQY.
- NT Productions. « Learn UXP For Premiere Pro » (2025). https://www.youtube.com/watch?v=EbtndtElBUg. Cinecom.net, « Premiere Pro and After Effects workflow: Dynamic Link ». https://www.youtube.com/watch?v=8SKZUuZkE08.

**Extraits (E), consultés le 12/10/2026**
- Adobe Help : Generative Extend FAQ (https://helpx.adobe.com/lv/premiere/desktop/edit-projects/edit-with-generative-ai/generative-extend-faq.html), notes de version (https://helpx.adobe.com/id_en/premiere/desktop/whats-new/release-notes.html), Morph Cut (https://helpx.adobe.com/ph_en/premiere-pro/kb/morph-cut.html), Media Intelligence, Auto Save.
- Adobe Help, « Warp Stabilizer settings » (cadrage, Synthesize Edges, méthodes) : https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/warp-stabilizer-settings.html. « Ultra Key effect parameters » (valeurs par défaut ; Contraste et Point milieu non lus) : https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/ultra-key-effect-parameters.html. « Add Track Matte Key » (case Inverser non lue) : https://helpx.adobe.com/si/premiere-pro/how-to/add-track-matte-key.html.
- Premiere Pro Scripting Guide (UXP, ExtendScript, septembre 2026) : https://ppro-scripting.docsforadobe.dev/ ; fil https://community.adobe.com/questions-729/extendscript-to-uxp-for-premiere-pro-1553924.
- ProVideoCoalition, « Using Synchronize in Premiere Pro » : https://www.provideocoalition.com/using-synchronize-premiere-pro/. Guides Merge Clips : https://evercast.us/blog/syncing-audio-in-premiere ; https://www.online-tech-tips.com/how-to-sync-audio-and-video-in-adobe-premiere-pro/.
- Dérive : forum Audacity (https://forum.audacityteam.org/t/correcting-audio-drift-with-sync-video-clips/46276).
- Jan Ozer, Streaming Learning Center, « Restoring A/V Sync in Premiere Pro » (cadence variable) : https://streaminglearningcenter.com/blogs/editing-technique-restoring-av-sync-in-premiere-pro.html.
- Larry Jordan, « Add Vertical Video to a Horizontal Timeline » : https://larryjordan.com/articles/add-vertical-video-to-a-horizontal-timeline-without-losing-image-quality/. « Premiere Pro: 4 Ways to Change Clip Speed » : https://larryjordan.com/articles/premiere-pro-4-ways-to-change-clip-speed/. Adobe Learn, « Work with clips, channels, speed » : https://www.adobe.com/learn/premiere-pro/web/work-with-clips-channels-speed.
- Adobe Community : proxys ProRes 422 et HEVC DJI 5K sur Mac (https://community.adobe.com/t5/premiere-pro-bugs/prores-422-proxies-cause-playback-freeze-with-dji-5k-hevc-footage-on-macos-works-fine-on-windows/idi-p/15266368) ; décodage 4:2:2 sur Mac ARM, bêta 2021 (https://community.adobe.com/t5/premiere-pro-beta/discuss-hardware-acceleration-decode-for-4-2-2-10-bit-h264-hevc-now-available-on-mac-arm-beta/m-p/12323477).
- Jonathan Kasson, bandes d'éclairage et obturateur (photo) : https://blog.kasson.com/gfx-50s/mitigating-lighting-banding-in-gfx-es-images. Moiré (photo d'écrans) : https://divoom.com/blogs/setup-ideas/reduce-moire-filming-pixel-led-screen. Bruit : https://blog.neatvideo.com/post/reduce-noise-pr.
- Wiki Evergreen « Ultra Key - Premiere Pro » ; 4kshooters « 5 Super Simple Luma Key Effects » (https://4kshooters.net/2021/04/16/5-super-simple-luma-key-effects-in-premiere-pro-cc) ; PetaPixel (20/01/2026), DigitalProduction (22/01/2026).

**Tests locaux (L)** : ffmpeg 6.1.1 (`deflicker`, `hqdn3d`, `atempo`, `signalstats`, `astats`, `-fps_mode cfr`, `-display_rotation`) et Python 3 / numpy sur fichiers générés (flou, bandes, bruit, dérive). Aucun test sur un rush réel de Cabezer.
