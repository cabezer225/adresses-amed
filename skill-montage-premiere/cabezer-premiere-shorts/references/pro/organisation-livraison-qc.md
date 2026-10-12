# Workflow pro de bout en bout : organisation, retours, contrôle qualité et livraison

> **Réponses de Cabezer du 12/10/2026 — elles priment sur cette fiche**, en particulier sur sa section « Décisions à demander ». **Format d'abord, famille ensuite (SKILL §2)** : long (L-Food, L-Story, L-Tech, L-Films, L-Life) ou court (C-Food, C-Story, C-Tech, C-Films, C-Life) ; codes de cette fiche : D = C-Food, F = L-Food, S = L-Story, P = L-Films, T = L-Tech ; nouvelle famille Lifestyle (vlogs, face caméra : aucune musique, SFX comme la dégustation). **Tous les courts** : hook demandé, sous-titres mot à mot, aucune musique, SFX comme la dégustation, punch-ins secs, appel au commentaire, notation sur 10, identité propre au court. **Longs** : SRT seul en France ; composition musicale en Story, food et tech ; respirations d'émotion gardées en films/séries et au verdict du food long ; 4K si rushs 4K. Aussi : identité Story v15 et générique « Amed Story 🧢 » supprimés ; jamais de foley d'aliment ; ambiance en dégustation proposée au premier usage ; un rendu de sous-titres par passage ; intervenants identifiés à la première apparition (hors courts food) ; au plus deux passes de retravail sous 8 ; Tesseract, Higgsfield et SCANDALE FOOD retirés. **Réponses techniques (série 3)** : interface de Premiere et d'AE en anglais ; scripts AE et Terminal autorisés ; stock libre de droits sans redemander ; tout SFX de la banque Pixabay permis ; arrêt sur image permis partout ; pas de test de photosensibilité ; audio YouTube 384 kbit/s ; proxys toujours en long ; Frame.io pour les relectures ; WhisperX à installer ; « 19h30 » et « 12,50 € » ; Liquid Glass à recréer. Liste complète : `../decisions-en-attente.md`.

Fiche de référence pour mener un montage de l'ingestion à la livraison comme un monteur professionnel, dans le cadre des règles de Cabezer. Dernière vérification : 12/10/2026. Versions, test de fumée des scripts et libellés lus à l'écran : `pilotage-environnement-reprise.md` et `Suivi/environnement-verifie.md` ; cette fiche ne répète pas de numéro de version.

## Quand lire cette fiche

Au démarrage d'un projet (arborescence, ingestion, sauvegarde), quand Cabezer renvoie des retours, avant tout export (contrôle), puis à la livraison et à l'archivage. Elle est **la source unique** de quatre objets partagés : l'arborescence et le dossier `Suivi/` (§2), la bibliothèque de commandes ffmpeg/ffprobe (§6.3), le jeu de scripts nommés (§6.6) et les réglages d'export hors vertical (§8). Les autres fiches y renvoient. Couleur, mixage, sous-titres et rythme : le skill et les fiches concernées.

Hiérarchie (skill §1) : brief de Cabezer, règles du skill, fiches, tutoriels. Aucune règle ici ne contredit le skill. Familles : dégustation (D), food long (F), Story (S), films/séries PRISME (P), tech (T), hors familles (H). Chaque technique dit quand l'utiliser, quand l'éviter et pour quelles familles.

## Sommaire

1. Principes et niveaux de preuve · 2. Arborescence, dossier Suivi, nommage · 3. Ingestion, proxys, cadence · 4. Sauvegarde, archivage, reprise · 5. Boucle de retours · 6. Contrôle qualité et scripts · 7. Audio · 8. Export (vertical, YouTube long, carré et 4:5, matériel ou logiciel) · 9. Plateformes, zones sûres, sous-titres livrés · 10. Livraison, conformité, clôture · 11. Techniques : quand, quand éviter, quelles familles · 12. Erreurs de débutant → réflexes de pro · 13. Liste de contrôle · 14. Décisions à demander · 15. Sources étudiées

---

## 1. Principes et niveaux de preuve

**Pourquoi** : un export défectueux se republie difficilement, et Claude n'entend pas : il contrôle par mesures (ebur128, crêtes, spectre), transcription et forme d'onde ; l'écoute finale revient à Cabezer. Ne jamais écrire « écouté » pour une mesure (skill §14).

Séparer quatre états : **appliqué** (fait dans le projet), **contrôlé** (mesuré ou examiné, limites dites), **validé par Cabezer** (il a regardé et écouté), **publié** (jamais sans son accord explicite). Un export lancé n'est pas un export validé. En mode autonome, une validation attendue est consignée « en attente ».

Niveaux de preuve : **[Doc lue]** documentation ou code lu (ffmpeg, API UXP, guides docsforadobe) ; **[Mesuré]** essayé le 12/10/2026 avec ffmpeg 6.1.1 sur des fichiers générés ; **[Extrait]** résultat de recherche, page non ouverte ; **[Tuto]** valeur d'auteur, jamais règle ; **[À vérifier]** à tester sur sa version.

**Limite.** Les pages d'aide d'Adobe, YouTube, TikTok, Instagram, Netflix, EBU et Frame.io n'ont pas pu être ouvertes (proxy) : aucune spécification de plateforme n'est donnée comme certaine. Les chemins de menu viennent de tutoriels de 2015 à 2022.

**Interface en français.** Nom français suivi de l'anglais entre parenthèses. Noms sûrs : Fichier > Enregistrer sous (Save As), Gestionnaire de projet (Project Manager), Moniteur Programme (Program Monitor), Contrôles d'effets (Effect Controls), Imbriquer (Nest). Tout autre libellé : « libellé à confirmer », à lire à l'écran puis consigner dans `Suivi/environnement-verifie.md`. Aucun raccourci tant qu'il n'a pas été lu dans Raccourcis clavier.

---

## 2. Organiser le projet : arborescence, dossier Suivi, nommage

**Pourquoi** : une arborescence stable évite les médias hors ligne et permet de rouvrir un projet un an plus tard [Tuto : « Chris »]. Cette section fait foi pour toutes les fiches.

### 2.1 Arborescence disque (toutes familles)

```
<Sujet>/
  Media/     Rushs/<camera>/ (originaux, jamais touchés)   Assets/ (surcouches, photos, captures, stock)
             Audio/ (musique, SFX, ambiances)               Proxys/ (jamais avec les rushs)
  Projet/    .prproj et .aep versionnés, enregistrement automatique
  Exports/   Brouillons/  Final/
  Controles/ rapports, images, mesures, manifeste de copie
  Suivi/     voir §2.2
  Publication/  (facultatif : couverture et textes, si demandés)
```

- Dégustation : le dossier vit dans `/Users/cabezer225/Documents/ChatGPT/Tiktok degustation/<Sujet>/` (skill §3) ; ses dossiers existants restent valables (« versions » = `Projet/`, « contrôles » = `Controles/`).
- Projet long à plusieurs séquences (S, P, F de plus de 20 min) : un dossier de Production **dans `Projet/`, qui ne contient que des projets** ; médias référencés dans `Media/` (`premiere-pro-avance.md §3.1`).

### 2.2 Dossier Suivi (registre unique)

| Fichier | Contenu |
|---|---|
| `brief.md` | famille, plateformes, durée, promesse, hook, langue des sous-titres, matériel et profil couleur, tableau des sources (cadence, taille), contraintes légales, autonomie, livrables |
| `decisions.md` | une ligne par décision (date, changement, raison) ; libellés d'export lus ; interprétations de métrage ; couleurs d'étiquettes |
| `retours.md` | liste des retours de Cabezer (§5.1) |
| `journal.md` | une ligne par geste significatif ou export : date, application et version, fichier, opération, état, preuve |
| `environnement-verifie.md` | libellés, raccourcis, versions et réglages lus sur sa machine (`pilotage-environnement-reprise.md`) |
| `licences.csv` | **registre unique** des images, vidéos, sons, musiques, polices et extraits |
| `verifications.md` | faits vérifiés (skill §8) : affirmation, passage, lien, date, résultat |

`LICENCES-SFX.md` de la banque dégustation reste en place ; `licences.csv` y renvoie. `suivi.md` et `licences.md` ne sont plus créés.

`licences.csv` : séparateur « ; », UTF-8, une ligne par élément, colonnes `type;fichier;titre;auteur;url;licence_ou_statut;preuve;date_consultation;resolution;minute_source;duree_utilisee_s;credit_ecran;valide_par` ; `type` ∈ image, video, son, musique, police, extrait. Statuts : `libre (licence lue)`, `licence obtenue`, `citation (à valider)`, `à demander`. Jamais « libre » sans licence lue ; un fichier sur le disque n'est pas une licence.

### 2.3 Chutes (bins), pistes, étiquettes, nommage

- Chutes : `Rushs` (une sous-chute par caméra), `Assets`, `Audio`, `Séquences` (`Selects`, puis `V01`, `V02`…) ; une séquence source et une séquence montée (skill).
- Pistes (skill §11) : A1–A2 voix, A3–A4 SFX, A5 musique, ambiances si besoin ; V1 face caméra, V2 inserts et B-roll, pistes hautes pour l'habillage AE. Pas de LUT sur un calque d'effets : la conversion D-Log M vers Rec.709 se fait **une seule fois** (skill §10).
- Étiquettes couleur (Préférences > Étiquettes, à confirmer) : une par type (A-roll, B-roll, graphique AE, audio) ; reprendre celles de Cabezer et les noter dans `decisions.md`. L'API UXP expose `ProjectItemColorLabel` [Doc lue].
- Exports : `<Sujet>_<plateforme>_v<NN>.mp4` (skill §13) ; relecture : suffixe `_REVIEW`. Jamais « final2 » ni « ok ». Projets : `<Sujet>_v<NN>.prproj`. **Enregistrer sous** une nouvelle version avant de modifier un montage existant (skill §1), avec une ligne dans `decisions.md`.

---

## 3. Ingestion, proxys, interprétation des médias

### 3.1 Copie vérifiée des cartes

**Pourquoi** : une copie corrompue se découvre au montage, carte déjà formatée. **Toutes familles.**

1. Copier la carte entière vers `Media/Rushs/<camera>/` ; conserver les originaux (skill §3).
2. Vérifier octet par octet : soit la copie avec vérification **md5** des réglages d'ingestion de Premiere [Tuto : Larry Jordan], soit un manifeste de sommes de contrôle [Mesuré] :

```bash
(cd "/Volumes/CARTE" && find . -type f -print0 | sort -z | xargs -0 shasum -a 256) > Controles/carte.sha
(cd "Media/Rushs/PocketA" && shasum -a 256 -c ../../../Controles/carte.sha)   # toute ligne FAILED : recopier
```

Réussite : toutes les lignes `OK`. Ne formater la carte qu'après la sauvegarde du §4.2.

### 3.2 Proxys (décision de fond)

**Défaut : ProRes Proxy, dossier `Media/Proxys/` séparé, environ un quart de la taille source.** H.264 seulement si l'espace disque manque (petit, mais lourd à décoder) [Tuto : Larry Jordan, 2020]. À confirmer par un essai sur un rush de Cabezer (lecture fluide, durée d'encodage). **Quand** : S, P, F longs, multicam, rushs > 4K, machine qui saccade. **Éviter** : D sur un Mac qui lit en temps réel.

Dans tous les cas, sans se fier aux affirmations contradictoires sur l'export :
1. Avant tout export, **désactiver les proxys** (bouton Basculer les proxys du Moniteur Programme ; libellé à confirmer).
2. **Vérifier la résolution du MP4** avec ffprobe (§6.2). Un tutoriel ancien affirme que l'export utilise toujours les originaux : non retenu sans test [À vérifier].

### 3.3 Cadence et interprétation

- Les rushs de téléphone peuvent être à cadence **variable** : voir la ligne « cadence » de `controle-mp4.sh` (`r_frame_rate` ≠ `avg_frame_rate`). Si l'audio dérive ou qu'une coupe saute, convertir une **copie** : `ffmpeg -i rush.mov -fps_mode cfr -r 30000/1001 -c:v prores_ks -profile:v 3 -c:a pcm_s24le copie_cfr.mov` [Doc lue : `-fps_mode cfr` duplique et supprime des images]. Arbre de décision : `premiere-pro-avance.md §3.4`.
- **Interpréter le métrage** (Clip > Modifier) change la cadence d'un clip **sans trace visible** : si utilisé (ralenti d'un rush 59,94), le noter dans `decisions.md` ; mouvements et export XML en dépendent [Tuto]. **Éviter** pour masquer une cadence variable.
- **Mode d'échelle** : « Définir à la taille de l'image » (Set to Frame Size) affiche l'échelle réelle (rush 4K en séquence 1080 : 50 %), « Mettre à l'échelle » (Scale to Frame Size) affiche 100 % [Tuto]. Avant d'écrire « zoom 115 % » ou un FCP XML, **lire le mode actif**. L'affirmation « meilleure qualité » d'un mode n'est pas vérifiée : écartée.

---

## 4. Sauvegarde, versions, archivage, reprise

### 4.1 Pendant le montage

1. **Enregistrement automatique** actif, vers `Projet/` (Préférences > Enregistrement automatique, à confirmer). Départ : 5 minutes, 20 versions. Les défauts de Premiere ne sont pas établis : les régler et les noter dans `environnement-verifie.md` [À vérifier].
2. **Enregistrer sous** avant chaque étape lourde : dérush validé, habillage, retouches de Cabezer, export. L'enregistrement automatique sert à la panne, pas à revenir sur une décision.
3. Enregistrer `.prproj` et `.aep` **avant** chaque export (skill §13).

### 4.2 Règle 3-2-1 pour les rushs

Trois copies, deux supports, une hors du lieu de travail. Règle très citée, aucune source officielle lue [À vérifier]. Une sauvegarde non restaurée n'en est pas une : une fois par projet, ouvrir une copie et vérifier qu'elle se lit.

### 4.3 Reprise après incident (règles locales)

Procédure : `pilotage-environnement-reprise.md §9`. Réflexes qui touchent cette fiche :
1. **Plantage** : ne pas cliquer sur Restaurer par réflexe. Ouvrir le dernier projet de `Projet/` ou d'enregistrement automatique, faire aussitôt **Enregistrer sous** une nouvelle version, puis comparer les listes de coupes de l'ancienne et de la nouvelle version (`xml-coupes.py`, §6.6).
2. **Média hors ligne** : Lier les médias (libellé à confirmer) en cherchant **uniquement dans `Media/Rushs/`** ; vérifier durée et timecode ; ne jamais lier un proxy à la place d'un original ; noter dans `decisions.md`.
3. **Espace disque** : avant un export ou un rendu AE lourd, `df -h` et comparer à 3 fois la taille estimée (§8.2 donne le calcul).
4. **Nouvelle session de Claude** : relire dans l'ordre `brief.md`, `decisions.md`, `retours.md`, `journal.md`, le dernier rapport de `Controles/`, la liste des versions ; refaire l'état réel (ffprobe des exports, XML de la séquence) ; ne pas supposer qu'un état « appliqué » est encore vrai ; dire à Cabezer ce qui a été relu.

### 4.4 Archive de fin de projet

Après publication et validation, jamais en cours de montage. Gestionnaire de projet (Fichier > Gestionnaire de projet) [Tuto : David V. Clarke, 2016 ; confirmer chaque libellé] :
1. **Collecter les fichiers et copier vers un nouvel emplacement** : exclure les clips inutilisés et les rendus (Premiere les refait) ; « Calculer » donne la taille (exemple de l'auteur : 30 Go réduits à 700 Mo).
2. **Consolider et transcoder** (parties utilisées avec **poignées**, départ de l'auteur : 25 images) : seulement si l'espace manque, car le transcodage s'ajoute à la compression d'origine.
3. Cocher la conversion des compositions After Effects en clips si Dynamic Link est utilisé, sinon la timeline aura un trou sans AE. Le gestionnaire ignore les médias importés directement dans AE.

After Effects : Fichier > Rassembler les fichiers (Collect Files, libellé à confirmer), après Consolider tous les métrages, Supprimer les métrages inutilisés, Réduire le projet [Doc lue]. Lister les polices (`app.project.usedFonts` [Doc lue]) et consigner celles de la famille (Avenir Next, Hoefler Text, Futura, PT Mono) : une archive sans police se rouvre avec des remplacements.

**Se conserve** : `.prproj`, `.aep`, médias utilisés, assets, exports finaux et SRT, tout `Suivi/`, rapports, `carte.sha`. Un master ProRes d'archive seulement sur demande de Cabezer : très lourd, et le skill exporte en MP4.

---

## 5. Boucle de retours

**Pourquoi** : ses coupes priment (skill §5). Perdre une retouche manuelle de Cabezer à l'export est plus grave qu'une erreur de montage.

### 5.1 Protocole

1. **Aperçu court d'abord** (skill §1) : un extrait représentatif avant de généraliser.
2. **Fichier de relecture** : MP4 léger, timecode incrusté, suffixe `_REVIEW`, pour que Cabezer dise « à 1:12,15 ». En 29,97 i/s, **drop-frame** (séparateur « ; ») [Mesuré ; Doc lue : `drawtext` gère le drop-frame à 30 et 60 i/s] :

```bash
ffmpeg -i export.mp4 -vf "drawtext=timecode='00\:00\:00\;00':rate=30000/1001:fontcolor=white:fontsize=48:box=1:boxcolor=black@0.5:x=24:y=24,scale=-2:720" -c:v libx264 -crf 23 -pix_fmt yuv420p -c:a aac -b:a 128k export_REVIEW.mp4
```

   À 25 i/s : `timecode='00\:00\:00\:00':rate=25`. **Jamais** livré comme export final. **Quand** : S, P, F longs ; D si demandé.
3. **Retours = liste datée** dans `Suivi/retours.md` : `R12 | v04 | 1:12,15 | « le hook est mou » | action | état (à faire, appliqué, contrôlé, validé)`.
4. **Retour ambigu** (« plus dynamique », « pas ouf ») : ne pas deviner ; proposer deux options chiffrées (« couper les blancs > 0,2 s » ou « ajouter un punch-in ») et demander ; il a déjà rejeté un ajout non demandé (skill §5.1).
5. **Retouches manuelles de Cabezer** : enregistrer sa version sous un nouveau numéro avant tout. Pour savoir ce qu'il a changé, exporter les deux séquences en FCP XML et comparer avec `xml-coupes.py`. Les pistes d'un seul tenant (sous-titres, habillage rendu) ne suivent pas ses coupes : les recouper (skill §9, §14).
6. **Chaque version rejoue le contrôle du §6 en entier** : une retouche locale décale tout ce qui suit.

### 5.2 Outils de revue

- **Défaut** : fichier `_REVIEW` envoyé par message, plus un marqueur Premiere par retour (couleur par état) : gratuit et suffisant pour Cabezer seul.
- **Frame.io** : commentaires au timecode, versions, import comme marqueurs [Tuto : Adobe Live, vers 2022]. **Plan payant possible : signaler à Cabezer avant tout usage** (gratuits uniquement) ; plan gratuit non vérifié [À vérifier].

### 5.3 Relecture à froid

**Non sourcée : pratique de métier, à proposer, pas règle.** Avant livraison, laisser passer du temps, regarder l'export **entier** sans toucher à rien, puis en petit format vertical ; noter les gênes avant de corriger. Claude n'a pas d'œil frais : il s'appuie sur images, transcription et mesures (§6). **Éviter** en cas d'urgence.

---

## 6. Contrôle qualité : niveaux 0 à 3, bibliothèque de commandes, scripts

**Pourquoi quatre niveaux** : chacun attrape ce que les autres manquent ; une mesure repère un noir ou un pic, pas une phrase coupée. Aucun ne remplace le visionnage et l'écoute de Cabezer (skill §14). Niveau 0 avant l'export ; niveaux 1 à 3 sur le **MP4 exporté**. Chaque détection est un **cas à examiner**, jamais un verdict.

### 6.1 Niveau 0 : pré-contrôle de la séquence

Dans Premiere : aucun média hors ligne, clip désactivé oublié ni trou vidéo ; appel au commentaire présent et entier ; pistes d'inserts muettes en dégustation (skill §5) ; proxys désactivés (§3.2) ; si l'export utilise « les rendus » (Use Previews), les vérifier à jour ou décocher l'option [À vérifier] ; `.prproj` et `.aep` enregistrés.

`lister-clips.jsx` (lecture seule) signale hors ligne, clips désactivés, trous vidéo, pistes audio. API lue dans le guide docsforadobe ; testé sur objets simulés, **jamais exécuté dans Premiere** : essayer sur une copie. Voie d'exécution : `pilotage-environnement-reprise.md §4` (ExtendScript tant que le test de fumée le confirme, UXP pour un nouvel outil, FCP XML en secours). Un script de contrôle **ne modifie rien** ; tout script qui écrit s'exécute sur une copie.

### 6.2 Niveau 1 : conformité technique

`controle-mp4.sh f.mp4 [largeur hauteur]` (défaut 1080 1920) compare le fichier au brief (taille, codec, cadence constante, étiquettes couleur, débit, durée, audio AAC 48 kHz stéréo, écart A/V), puis enchaîne intégrité, noirs, figements, son manquant, niveaux vidéo et loudness (§6.3). Lecture seule [Mesuré]. Lecture des lignes :
- **couleur** : `None` = export sans étiquettes (le lecteur devine l'espace couleur). Un export SDR Rec.709 de Premiere doit donner `bt709/bt709/bt709` (`etalonnage-gestion-couleur.md`). **Source HLG ou HDR** (iPhone) : conversion vers SDR à décider avec Cabezer [À vérifier].
- **cadence** : `VARIABLE` est un défaut (§3.3).
- **débit** : affiché sans seuil ; environ 20 Mbit/s en vertical = **débit de Cabezer, non issu d'une source officielle**.
- **niveau H.264** : x264 choisit au minimum 4.1 pour 1080×1920 à 29,97 i/s, 5.1 pour 3840×2160 à 30 [Mesuré]. « Constrained Baseline » est anormal pour un export réel.
- **niveaux vidéo** : plage légale 8 bits 16 à 235 ; au-delà, cas à examiner.
- Autre format : `bash controle-mp4.sh f.mp4 1080 1350`.

### 6.3 Bibliothèque de commandes ffmpeg/ffprobe (tableau unique)

**Cette table fait foi.** Les autres fiches renvoient à la ligne voulue, jamais à un seuil recopié. Les seuils sont des **usages différents**, non des variantes d'une même mesure. Testés avec ffmpeg 6.1.1 ; options et valeurs par défaut lues dans la doc [Doc lue].

| Usage | Commande (extrait) | Seuil | Lecture |
|---|---|---|---|
| Blancs à écouter (D) | `-vn -af silencedetect=n=-35dB:d=0.25 -f null -` sur la voix seule | −35 dB, 0,25 s | Coupes à examiner ; **ne remplace pas** la méthode étalonnée du skill (§5.2 : −18 dB sous le 80e centile sur 4 s), seule à noter la rétention |
| Son manquant | `-af silencedetect=n=-50dB:d=0.5` | −50 dB, 0,5 s | Trou involontaire. Silence voulu en S (1 à 2 s avant une bascule) : positif attendu |
| Fin d'un mot protégé | `-ss <t-0.5> -t 1 -af silencedetect=n=-40dB:d=0.1` | −40 dB, 0,1 s | À calibrer par rush (environ 10 dB au-dessus du bruit d'une pause) |
| Room tone | `-af silencedetect=n=-45dB:d=1` | −45 dB, 1 s | Cherche une pause sans respiration ; à calibrer |
| Noir d'une image | `-vf blackdetect=d=0.04:pix_th=0.10` | d = 0,04 s | Repère un noir d'une image à 25 i/s (défaut de 2 s trop lâche) |
| Figement | `-vf freezedetect=n=-60dB:d=1` | −60 dB, 1 s | **Faux positifs normaux** : preuve tenue 3 à 11 s (S), titre, carton de chapitre. Figé entre deux inserts en D : suspect |
| Niveaux vidéo | `-vf "signalstats,metadata=mode=print:file=-"` | 16–235 | `YMIN`, `YMAX` |
| Loudness | `-af ebur128=peak=true` | repère −14 LUFS ±1 ; crête ≤ −1 dBTP | `controle-mp4.sh`. Autres mesures (court terme, mono, `astats`) : `audio-dialogue-sound-design-mixage.md §10` |
| Intégrité | `ffmpeg -v error -i f -f null -` | aucun message | Lisible en entier |
| Cadence constante | `ffprobe … r_frame_rate,avg_frame_rate` | égales | §3.3 |
| Première, dernière image | `-frames:v 1 -update 1 first.png` ; `-sseof -0.1 … last.png` | — | Pas de noir ni de texte coupé ; S : fondu au noir après le regard (skill §6) |
| Planche contact | `-vf "fps=1,scale=240:-1,tile=8x8" -frames:v 1 -update 1 sheet.png` | — | Noirs, textes dupliqués, cadres oubliés ; changer `fps` pour l'intervalle |
| Changements de plan | `-vf "select='gt(scene,0.3)',showinfo"` | 0,3 (départ) | `mesure-plans.py` ; manque fondus et coupes entre plans proches |
| Comparer deux exports | `-i a.mp4 -i b.mp4 -lavfi "[0:v][1:v]psnr"` ou `ssim` | `inf` = identiques | Même taille et nombre d'images [Doc lue] ; 39 dB = simple différence de compression [Mesuré]. Premiere : référence en mode Différence [Tuto] |

Chaque cas examiné est noté dans le rapport (§6.5).

### 6.4 Niveau 3 : examen par images, transcription, forme d'onde

**Claude peut** lire des images extraites, transcrire l'export par fenêtres de 10 s qui se chevauchent (skill §5.2), mesurer, comparer des listes. **Il ne peut pas** écouter ni juger un rythme : le dire dans le rapport.

**Sous-titres.** Extraire les images aux **milieux de bloc** du SRT, puis les ouvrir (réduire à 270 × 480 pour juger la lisibilité mobile) :

```bash
for t in $(python3 -I lint-srt.py sous_titres.srt autre 9:16 --mids | tail -1); do ffmpeg -v error -y -ss $t -i export.mp4 -frames:v 1 -vf scale=360:-1 -update 1 "bloc_$t.png"; done
```

Regarder : jamais trois lignes, aucun mot coupé ou collé au bord, aucun sous-titre sur un texte animé (skill §9), sur le visage ou sur l'interface. Un SRT correct ne prouve rien : le contrôle porte sur le MP4.

`lint-srt.py f.srt D-fr|D-trad|autre [9:16|16:9] [--mids]` applique les limites du skill (§9) : `D-fr` un mot par bloc ; `D-trad` 1 à 3 mots, 18 caractères au plus ; `autre` 2 lignes, 24 caractères par ligne en 9:16 (42 en 16:9), pas de mot isolé, bloc d'au moins **max(1,5 s ; 1 s + caractères/15)** (formule du skill, familles longues, **jamais** pour le mot à mot de D). Pour tous : espace simple avant `; : ! ? € %`, apostrophe droite (`conformite-droits-accessibilite.md §7`). [Mesuré]

**Coupes, mots coupés, appel au commentaire.**
1. `xml-coupes.py seq.xml [motif]` liste coupes, trous, chevauchements, clips désactivés, transitions, clips écrits dans le désordre (piège du skill §14) et, avec un motif de nom, la part de face caméra. Dans un xmeml : `start`/`end` = images d'**enregistrement** (`end` exclusif) ; `in`/`out` = images de la source ; `ntsc` TRUE signifie `timebase × 1000/1001` (30 → 29,97) ; `start` = −1 marque un clip pris dans une transition [Doc lue : notes de pipeline GitHub, §15]. Testé sur un export Premiere de tiers, pas de Cabezer.
2. Pour chaque coupe suspecte, extraire 1 s et transcrire : `ffmpeg -ss <t-0.5> -t 1 -i export.mp4 -vn fenetre.wav`. Forme d'onde : `… -vn -filter_complex "showwavespic=s=1200x300" -frames:v 1 -update 1 onde.png` [Mesuré] ; une onde qui s'arrête en plein pic, sans extinction, signale un mot coupé.
3. Transcrire l'export entier : « Bref, c'est partiiii » entier jusqu'à la dernière syllabe ; mot de l'appel au commentaire conforme à ce qui est prononcé (skill §4). Ne jamais inventer un appel non tourné.
4. Décision finale d'un mot coupé : l'écoute de Cabezer.

### 6.5 Rapport de contrôle

Dans `Controles/` : date, version, commandes, sorties brutes, **chaque cas examiné avec son issue** (« noir à 12,4 s : voulu, fondu » ; « figé 5,2–8,0 s : preuve tenue »). Distinguer « contrôlé automatiquement », « examiné à l'image », « écouté par Cabezer » ; écrire tout contrôle non fait. En D, rejouer le barème du skill §5.2 et donner les deux notes (≥ 8).

### 6.6 Jeu de scripts nommés (source unique)

Fichiers dans `references/pro/scripts/` du skill (emplacement proposé, §14). Tout fichier lu (XML, SRT, transcription) passe par `python3 -I`. **Statut** : « testé sur fichiers générés » jusqu'au passage sur un vrai export de Cabezer, consigné au skill §20.

| Script | Rôle et appel | Détail |
|---|---|---|
| `controle-mp4.sh` | conformité et détecteurs du MP4 ; `bash controle-mp4.sh f.mp4 [L H]` | §6.2 |
| `lint-srt.py` | limites de sous-titres par famille, typographie | §6.4 |
| `lister-clips.jsx` | pré-contrôle de séquence, lecture seule | §6.1 |
| `xml-coupes.py` | coupes, trous, désordres, transitions d'un FCP XML | §6.4 |
| `mesure-plans.py` | durées de plans d'un MP4 ; `python3 -I mesure-plans.py f.mp4 [seuil=0.3] [fenetre_s=60] > plans.csv` ; moyenne, médiane et coupes par fenêtre sur stderr | — |
| `paquets.py` | paquets de sous-titres, décalage sous les animations | `formats-courts-verticaux.md §4.6` |
| `affiner_bords.py` | recale les bords de mots sur l'énergie du son | `audio-dialogue-sound-design-mixage.md §3.1` |
| `mesure-derive.py` | dérive caméra/enregistreur (`mesurer_derive.py` dans audio §2.4 : même rôle, un seul fichier à garder) | `premiere-pro-avance.md §6.2` |
| `reprise-candidats.py`, `envcheck-mac.sh` | reprise, relevé d'environnement | `pilotage-environnement-reprise.md` ; `noter_hook_retention.py` (D) : skill §5.2 |

`mesure-plans.py` repère une zone anormalement longue ou monotone et compare deux versions ; ses valeurs ne définissent pas un bon rythme. Seuil de scène 0,3 : valeur de départ.

---

## 7. Audio : mesurer sans normaliser aveuglément

**Pourquoi** : le skill (§11, §13) valide le mix à l'écoute, puis le mesure sur le MP4 ; les niveaux sont des **repères**, pas des cibles imposées. Valeurs et méthode : `audio-dialogue-sound-design-mixage.md §9` (loudness) et `§10` (contrôle du MP4). Ici, seulement ce qui touche la livraison.

- **Repères** : −14 LUFS intégrés (±1) ; crête vraie du MP4 ≤ −1 dBTP ; AAC 48 kHz 320 kbit/s. Si la crête dépasse, baisser d'abord la source fautive (SFX, musique), pas de limiteur de bus maître sans accord. Aucun chiffre vérifié pour YouTube, TikTok, Instagram ni Shorts : n'en pas inventer.
- **Repère personnel** : mesurer 3 exports validés à l'écoute par Cabezer, noter I, LRA et crête dans `Suivi/verifications.md`, comparer les nouveaux exports à cette plage. Écart : revoir la chaîne voix (skill §11) et la balance SFX/voix, sans corriger au hasard.
- **Normalisation** : « Correspondance automatique » et « Dynamique » d'Essential Sound sont écartées par le skill ; pas de normaliseur sur le mix final sans accord. `loudnorm=print_format=json` sert à **mesurer** (`input_i`, `input_tp`), pas à traiter [Mesuré].
- **Repliement mono** (skill §11) : comparer l'intégré stéréo à `-af "pan=mono|c0=0.5*c0+0.5*c1,ebur128"`. Un fichier déphasé est passé de −18,9 à −70 LUFS [Mesuré]. Plus de 3 LU de chute sur une voix stéréo = signal de phase.
- **Par famille** : D voix + SFX, sans musique ; S nappe sous la voix (`audio §5.5`), silences de 1 à 2 s voulus ; F, P, T musique selon l'émotion, vitesse du morceau inchangée.

---

## 8. Export : vertical, YouTube long, carré et 4:5, encodage matériel ou logiciel

**Pourquoi** : les plateformes recompressent toujours ; un fichier trop léger est recompressé une seconde fois et se dégrade [Tuto : Larry Jordan, 2015 ; son 720p est périmé, non repris].

### 8.1 Vertical : TikTok, Reels, Shorts (D ; F, S, P, T déclinés)

Réglages du skill (§13), point de départ unique : FHD 1080×1920 exporté directement de Premiere, MP4 H.264, **VBR 1 passe environ 20 Mbit/s** (débit de Cabezer, non issu d'une source officielle), AAC 48 kHz 320 kbit/s, cadence de la source ; master 4K sur demande seulement. Cases « Utiliser la qualité de rendu maximale » (Use Maximum Render Quality) et « Rendre à la profondeur de bits maximale » (Render at Maximum Depth) : libellés à confirmer à l'écran (le skill écrivait « résolution maximale »), à consigner dans `environnement-verifie.md` puis `decisions.md`. Après tout changement de préréglage, **contrôler la taille 1080 × 1920** : les préréglages « YouTube 1080p » repassent en 1920 × 1080 avec bandes noires (`formats-courts-verticaux.md §7.1`, d'après un tutoriel de Dolinski).

H.265 : sur demande seulement (skill §13) ; tester la lecture sur téléphone et navigateur. La doc ffmpeg utilise `-tag:v hvc1` pour HEVC en MP4 ; l'exigence de QuickTime n'y est pas écrite [À vérifier].

### 8.2 YouTube long (F, S, P, T)

**Quand** : toute vidéo longue horizontale. **Éviter** : 4K sans source 4K. Rushs en 4K : export 4K par défaut (réponse du 12/10/2026, skill §13).

Base (skill §13) : 3840×2160 quand les rushs sont en 4K (réponse du 12/10/2026), sinon 1920×1080 ; cadence de la séquence, SDR Rec.709. Pour les envois SDR, YouTube recommande [Extrait de sa page d'aide, non ouverte] H.264 profil High, progressif, 4:2:0, audio AAC-LC 48 kHz ; aucune limite de débit imposée, seulement des repères :

| Résolution | 24, 25, 30 i/s : repère YouTube | départ de la fiche | 48, 50, 60 i/s : repère YouTube | départ de la fiche |
|---|---|---|---|---|
| 1080p | 8 Mbit/s | **16** | 12 Mbit/s | **24** |
| 4K (2160p) | 35–45 Mbit/s | **50** | 53–68 Mbit/s | **75** |

(1440p : 16 et 24 Mbit/s selon le même extrait.) **Les départs sont mes propositions, non sourcées** : deux fois le repère en 1080p, un peu au-dessus du haut de la fourchette en 4K, puisque YouTube ré-encode. Les tester sur 60 s de plans difficiles (feuillage, dégradés, texte fin) avant adoption ; H.264 VBR 1 passe.

Poids ≈ débit × durée / 8 : 16 Mbit/s × 1 200 s = 2 400 Mo ; 50 Mbit/s = 7 500 Mo. Vérifier l'espace libre (§4.3) et la limite de taille de la plateforme [À vérifier]. Audio : 320 kbit/s (skill) ; le même extrait liste 384 kbit/s en stéréo (§14). Contrôle : `bash controle-mp4.sh f.mp4 1920 1080`. Chapitres et fin compatibles avec l'écran de fin (skill §13).

### 8.3 Carré (1:1) et 4:5 (H ; D, F, S déclinés)

**Quand** : fil Instagram (4:5) ou demande explicite. **Éviter** par défaut : le 9:16 reste le format des Shorts, Reels et TikTok ; un carré de moins de 3 minutes compte comme Short mais s'affiche avec des bandes noires [Extrait : guides tiers ; `formats-courts-verticaux.md §8`]. Dimensions : 1:1 = 1080 × 1080 ; 4:5 = 1080 × 1350 [Extrait : guides tiers sur Instagram, page officielle non lue].

1. **Recomposer, pas rogner** : nouvelle séquence 1080×1350 ou 1080×1080 à partir du montage maître. Un 9:16 en 4:5 ne garde que 70 % de la hauteur, un 16:9 en 4:5 que 45 % de la largeur : textes compris, le reste disparaît. Auto Reframe (`premiere-pro-avance.md §8.1`, options de ratio à lire à l'écran) n'est qu'un départ ; corriger visage, produit, mains.
2. **Refaire textes et sous-titres** à cette taille, en compositions AE (skill §9) ; à largeur égale (1080), 24 caractères par ligne reste le départ.
3. **Zones sûres** : la boîte de `formats-courts-verticaux.md §6.2` vaut pour le 9:16 seulement. Aucune boîte validée en 4:5 ni 1:1 : texte clé dans le tiers central, test sur téléphone (§14).
4. **Export** comme §8.1 (VBR 1 passe, 20 Mbit/s de Cabezer, AAC 320). Nom : `<Sujet>_InstagramFeed4x5_v<NN>.mp4`. Contrôle : `bash controle-mp4.sh f.mp4 1080 1350`, puis chaque fichier à part (§8.6).

### 8.4 Encodage matériel ou logiciel sur Mac (Apple Silicon)

**Quand tester** : avant le premier export livré, puis à chaque changement de machine ou mise à jour majeure. **Éviter** : de changer d'encodeur sans essai, ou entre deux versions d'une même vidéo.

Ce que les sources établissent :
- Apple Silicon (M1 Pro et suivants) prend en charge l'encodage matériel H.264 et H.265 dans Premiere [Extrait : page d'aide Adobe].
- Le réglage « Encodage matériel / logiciel » (Performance, Hardware / Software Encoding) est dans la fenêtre d'export (libellé à confirmer). Des fils de la communauté Adobe rapportent que le matériel n'est proposé qu'avec **VBR 1 passe** (le VBR 2 passes serait réservé au logiciel) et que l'option peut être grisée (CBR, « Correspondre à la source ») [Extrait : forums, non officiel]. Le réglage du skill (VBR 1 passe) est donc compatible.
- **Aucune comparaison de qualité sur Apple Silicon n'a été lue.** Les tests de Puget Systems portent sur d'autres machines : environ ×2 en vitesse et peu de différence visible avec des cartes NVIDIA/AMD (2021) ; avec Intel Quick Sync, débit cible pas toujours atteint et qualité inférieure (2018) [Extrait]. Non transposable.
- ffmpeg expose `h264_videotoolbox` et `hevc_videotoolbox` (options `allow_sw`, `realtime`, `prio_speed`, `profile`) [Doc lue : `videotoolboxenc.c`] ; il ne sert qu'aux essais, Premiere exporte le livrable.

**Défaut avant l'essai** : logiciel pour le livrable, matériel permis pour les brouillons. **Essai, une fois** :
1. Sur 20 à 60 s de plans difficiles : exporter un **master ProRes** (référence), puis deux MP4 au même débit en VBR 1 passe, l'un matériel, l'autre logiciel.
2. Noter durée d'encodage, taille et débit réel (le matériel peut s'écarter du débit demandé).
3. Comparer chacun au master : `ffmpeg -i mp4.mp4 -i master.mov -lavfi "[0:v][1:v]ssim" -f null -` (même taille ; plus haut = meilleur ; **aucun seuil sourcé**, le score départage). Exemple [Mesuré] : MP4 à 4 Mbit/s contre master, SSIM 0,994, PSNR 42,9 dB.
4. Cabezer regarde les deux sur les plans critiques (bouchée, gros plan, dégradés). Consigner dans `decisions.md`. Matériel adopté pour les livrables seulement si le débit réel est conforme (±10 %, départ non sourcé) et si Cabezer ne voit pas de différence.

### 8.5 Procédure d'export

1. `.prproj` et `.aep` enregistrés sous une version (§4.1) ; niveau 0 du §6 passé ; espace disque contrôlé.
2. Séquence active sélectionnée ; Fichier > Exporter > Média (Export > Media, libellé à confirmer). Régler d'après §8.1 à §8.3 ; nommer selon §2.3.
3. **Exporter** (direct) ou **Envoyer à Media Encoder** (file : on continue à monter, utile pour plusieurs variantes) [À vérifier]. Dossiers de contrôle de Media Encoder : jamais sur `Media/Rushs/` (le fichier source est déplacé), `pilotage-environnement-reprise.md §6`.
4. Après l'export : le fichier existe, sa taille est plausible, **les niveaux 1 à 3 du §6 sont rejoués sur ce fichier**. Noter « exporté », puis « contrôlé ».

Par script [Doc lue] : ExtendScript `sequence.exportAsMediaDirect(outputPath, presetPath, workAreaType)` (0 entier, 1 entrée-sortie, 2 zone de travail) ; UXP `EncoderManager.exportSequence(sequence, exportType, outputFile, presetFile, exportFull)` avec `ExportType.IMMEDIATELY`, `QUEUE_TO_AME` ou `QUEUE_TO_APP`. Les deux demandent un préréglage `.epr` : le créer une fois à la main depuis un export validé et le ranger dans `Projet/`.

### 8.6 Déclinaisons et dégradés

- TikTok vers Shorts/Reels, ou long vers court (skill §12) : une séquence par variante. **Rejouer le contrôle sur chaque fichier** : une variante réencodée n'est plus « la même ».
- Dégradés lisses (verre Liquid Glass, fonds colorés) : bandes possibles en 8 bits. Examiner l'image exportée ; si bandes, tester un débit plus haut ou un léger grain dans AE [À vérifier]. **Familles** : T, S.

---

## 9. Plateformes, zones sûres, sous-titres livrés

**Principe** : durée maximale, taille, débit conseillé, zone sûre et volume des plateformes changent, et les sources lues se contredisaient. **Avant une série de vidéos, lire la page d'aide actuelle ou la fenêtre d'envoi**, noter valeur et date dans `Suivi/verifications.md` ; ne jamais citer un chiffre de mémoire. Durées et formats connus : `formats-courts-verticaux.md §8`. Règles de Cabezer, qui prévalent : dégustation TikTok environ 3:00 au plus ; texte clé hors du bas et du bord droit (skill §13).

### 9.1 Zones sûres 9:16 : une seule boîte

La seule définition est la **boîte de test provisoire** de `formats-courts-verticaux.md §6.2` (1080 × 1920 : 270 px en haut, y ≥ 1250 en bas, x ≥ 948 à droite), qui vaut pour le **texte clé** (étiquettes, prix, pop-ups, note, appel au commentaire). Les sous-titres de D restent à 72–75 % de la hauteur (règle de Cabezer) : exemptés en attendant sa réponse, avec contrôle sur téléphone qu'ils ne sont pas masqués (§14). Dès réception de ses captures d'écran, remplacer les valeurs par les mesures réelles, et les nombres de la commande avec elles. Contrôle d'un export vertical [Mesuré] :

```bash
ffmpeg -ss 5 -i export.mp4 -vf "drawbox=x=iw*948/1080:y=0:w=iw*132/1080:h=ih:color=red@0.35:t=fill,drawbox=x=0:y=0:w=iw:h=ih*270/1920:color=red@0.35:t=fill,drawbox=x=0:y=ih*1250/1920:w=iw:h=ih*670/1920:color=red@0.35:t=fill" -frames:v 1 -update 1 zones.png
```

Réussite : ni texte clé ni visage dans les zones rouges (sous-titres de D exemptés). Les marges de sécurité TV de Premiere ne conviennent pas au vertical [À vérifier].

### 9.2 Sous-titres livrés

**Voie unique** (skill §9) : sous-titres finaux incrustés = **composition After Effects** à l'identité de la famille (calque de texte éditable, un mot ou un paquet par clé de Texte source, entrée animée), rendue en ProRes 4444 alpha, **plus le SRT livré**. La piste de légendes de Premiere ne sert que de transcription, de calage et de source du SRT ; « Mettre à niveau la légende » n'est plus utilisé. Un repli sans AE, si Cabezer l'accepte, s'appelle « repli non animé » et se consigne dans `decisions.md`.
- D : langue demandée à chaque tournage à l'étranger ; autres familles tournées à l'étranger : anglais, deux lignes. Limites : §6.4.
- Générer le SRT à partir de **la même liste de coupes** que le rendu AE ; si Cabezer retouche la timeline, recouper puis rejouer le §6.4. Menu d'export SRT : à lire à l'écran.

---

## 10. Livraison, conformité, clôture

### 10.1 Paquet de livraison

Dans `Exports/Final/` : `<Sujet>_<plateforme>_v<NN>.mp4`, SRT si requis, `_REVIEW` si utile. Message à Cabezer qui distingue les états :

```
Livré : <Sujet>_TikTok_v03.mp4 (1080×1920, 29,97 i/s, 2:41, ~20 Mbit/s).
Appliqué : retours R10 à R14. Contrôlé : technique OK ; noirs et silences examinés (cas listés) ; I=-xx LUFS, crête=-x dBFS.
Non contrôlé : écoute (à faire par toi), rendu sur ton téléphone. Hook x/10, rétention x/10.
Publication : non faite. Licences : Suivi/licences.csv.
```

**Ne jamais publier** : une autorisation d'enchaîner n'autorise pas la publication (skill §1). Pour publier, passer par les skills dédiés.

### 10.2 Liste de contrôle de conformité

Seuils et procédures : `conformite-droits-accessibilite.md` (numéros de section du brouillon, à confirmer) ; à faire valider par un juriste. Cette fiche ne répète ni seuil ni texte de loi.
- **Personnes et données visibles** (§2) : visages, enfants, employés, plaques, tickets, écrans traités ou accord obtenu ; masquages notés au rapport.
- **Contenu commercial** (§3) : question posée au brief (plat offert ou invité, partenariat, affiliation ?) ; si oui, mention construite dans AE, dès le début, lisible sur téléphone, jamais masquée par un sous-titre.
- **Extraits tiers** (§4, P et S) : durée minimale, commentés, source affichée ; un crédit n'est pas une autorisation ; risque Content ID signalé avant publication.
- **Musique et sons** (§5) : chaque piste dans `licences.csv` avec preuve.
- **Photosensibilité** (§6), **typographie française** (§7, avec `lint-srt.py`), **intervenants et contraste** (§8) : vérifiés.

### 10.3 Clôture

`licences.csv` à jour ; rapport dans `Controles/` ; `.prproj`, `.aep`, sources enregistrés, archive selon §4.4 si terminé ; après publication, boucle rétention (skill §15) quand les données existent.

---

## 11. Techniques : quand, quand éviter, quelles familles

| Technique | Utiliser quand | Éviter quand | Familles |
|---|---|---|---|
| Copie vérifiée (somme de contrôle) | Toute carte copiée | Jamais | D F S P T H |
| Proxys ProRes Proxy | Multicam, rushs > 4K, machine qui saccade | Rushs légers ; export sans vérifier la bascule | S P F ; D rarement |
| Interpréter le métrage | Ralenti d'un rush à cadence élevée | Pour masquer une cadence variable | Toutes |
| Fichier `_REVIEW` + timecode | Retours par minutage | Livraison finale | S P F longs ; D si demandé |
| Frame.io | Relecteurs distants | Gratuit seulement ; Cabezer seul | S P F longs |
| `controle-mp4.sh` et détecteurs | Chaque export | Les lire comme verdict | D F S P T H |
| `xml-coupes.py`, `mesure-plans.py` | Audit de coupes, comparaison de versions | Juger un bon rythme | F S P T ; D coupes |
| ebur128 + crête vraie, repliement mono | Chaque export | Cible imposée ; normalisation sans accord ; voix mono dupliquée | Toutes |
| Planche contact, images aux blocs | Verticaux, sous-titres | Juger le rythme | D F ; verticaux |
| `lint-srt.py` | SRT ou sous-titres éditables | Mot à mot : sans durée minimale ni débit | D F S P T H |
| `lister-clips.jsx` | Avant export | Sur l'original avec écriture | Toutes |
| Zones sûres en superposition | Export 9:16 | Horizontal, 4:5, 1:1 (pas de boîte) | D ; verticaux |
| Export YouTube long (§8.2) | Vidéo horizontale longue | 4K sans source 4K | F S P T |
| Carré, 4:5 recomposés | Fil Instagram, demande | Par défaut ; simple rognage | H ; D F S déclinés |
| Encodage matériel (après essai) | Brouillons ; gain établi | Livrable sans essai ; VBR 2 passes | Toutes |
| Relecture à froid | Avant livraison | Urgence explicite | Toutes |

Hors familles (H) : commande, carré, 4:5, multilingue. Même flux ; relire la page de plateforme ; faire valider l'identité (skill §6).

---

## 12. Erreurs de débutant → réflexes de pro

| Erreur de débutant | Réflexe de pro |
|---|---|
| Formater la carte sans copie vérifiée | Somme de contrôle, sauvegarde 3-2-1, puis formatage |
| Un seul projet « final », export sans enregistrer, proxys actifs | `Enregistrer sous` versionné, `.prproj` et `.aep` enregistrés, proxys désactivés |
| « L'export est lancé, c'est fini » | Niveaux 1 à 3 sur le MP4 ; états appliqué/contrôlé/validé |
| Prendre −14 LUFS pour une obligation, normaliser pour « tomber juste » | Repère ; comparer à ses vidéos validées ; régler la chaîne voix |
| Se fier au SRT | Contrôler les blocs sur les images du MP4 |
| Lire une détection comme une faute, ou copier un seuil d'une autre fiche | Cas à examiner ; lire la ligne du tableau §6.3, chaque seuil a son usage |
| Retoucher sans sauvegarder la version de Cabezer | Sa version d'abord, puis comparer les listes de coupes |
| Citer une valeur de plateforme d'un blog ou d'un tutoriel de 2015 | Page actuelle, valeur et date notées ; libellés lus à l'écran |
| Rogner un 9:16 pour faire un 4:5 | Recomposer, refaire textes et sous-titres |
| Passer en encodage matériel « parce que c'est plus rapide » | Essai à débit égal, SSIM, regard de Cabezer |
| Archiver en MP4 recompressé, oublier polices et `.aep` | Originaux avec poignées, `usedFonts`, Rassembler les fichiers |

---

## 13. Liste de contrôle

**Avant le montage**
- [ ] Rushs copiés et vérifiés (`carte.sha`), originaux intacts ; arborescence et `Suivi/` créés ; enregistrement automatique actif ; sauvegarde 3-2-1 prévue.
- [ ] Famille identifiée, brief relu (dont la question du contenu commercial), règles de plateforme lues (valeur et date notées).

**Avant l'export**
- [ ] Niveau 0 : aucun hors ligne, désactivé oublié, trou ou noir ; appel au commentaire présent.
- [ ] Proxys désactivés ; `.prproj` et `.aep` enregistrés sous une version ; espace disque suffisant.
- [ ] Couleur et mixage faits à part ; mix écouté, ou signalé non écouté.

**Après l'export (sur le MP4)**
- [ ] `controle-mp4.sh` : lisible en entier ; taille, codec, cadence constante, étiquettes `bt709` conformes au brief.
- [ ] Noirs, images figées, silences : chaque cas examiné et noté.
- [ ] Intégré, LRA, crête vraie (≤ −1 dBTP), repliement mono, écrêtage consignés.
- [ ] Planche contact, premières et dernières images vues ; zones sûres contrôlées (9:16).
- [ ] Sous-titres : `lint-srt.py`, jamais trois lignes, masqués pendant les textes animés, vérifiés sur les images ; SRT recoupé.
- [ ] Mots coupés, « Bref, c'est partiiii », mot de l'appel au commentaire vérifiés (transcription, forme d'onde).
- [ ] Dégustation : hook et rétention ≥ 8 notés ; aucun SFX orphelin ni audio d'insert.
- [ ] Chaque variante (YouTube long, 1:1, 4:5, déclinaisons) contrôlée à part.

**Livraison**
- [ ] Conformité du §10.2 passée ; rapport dans `Controles/` ; états distingués ; ce qui n'a pas été contrôlé est écrit (écoute, téléphone).
- [ ] `licences.csv` à jour ; aucune publication sans accord ; archive ou nettoyage proposé.

---

## 14. Décisions à demander

> **Toutes ces questions ont reçu une réponse de Cabezer le 12/10/2026** : voir `../decisions-en-attente.md`, qui prime sur les défauts ci-dessous.

Défaut appliqué en attendant la réponse ; une réponse consignée dans `Suivi/decisions.md` ne se redemande pas.

| Question | Défaut en attendant |
|---|---|
| Sous-titres de D à 72–75 % de la hauteur : exemptés de la boîte de zones sûres ? | Exemptés ; test sur téléphone ; pas déplacés seul |
| Proxys : ProRes Proxy convient-il après essai sur un de tes rushs ? | ProRes Proxy ; H.264 seulement si l'espace manque |
| Encodage matériel ou logiciel pour les livrables, après l'essai du §8.4 ? | Logiciel pour le livrable ; matériel permis pour les brouillons |
| Débits de départ YouTube long du §8.2 : OK ? (4K quand les rushs sont en 4K : réponse du 12/10/2026) | Valeurs du §8.2, testées sur 60 s |
| Audio YouTube long : 320 kbit/s (skill) ou 384 ? | 320 kbit/s |
| Carré et 4:5 : quelles plateformes, quelle zone sûre ? | Seulement si demandé ; texte clé dans le tiers central |
| Dossier des scripts : `references/pro/scripts/` du skill ? | Oui, un seul jeu |
| Frame.io (plan payant possible) ? | Non ; fichier `_REVIEW` |
| Master ProRes d'archive en fin de projet ? | Non, sauf demande |
| Repli sans After Effects pour les sous-titres (« repli non animé ») accepté dans certains cas ? | Non : composition AE + SRT |

---

## 15. Sources étudiées

**Transcriptions lues** (transcriptions lues pendant la recherche, non livrées). Six autres prévues (export maître de Larry Jordan, mesure de volume, Frame.io, règle 3-2-1, limiteur) n'ont pas pu être obtenues : YouTube a bloqué la récupération.

| Auteur | Titre | URL | Couverture réelle |
|---|---|---|---|
| « Chris » (chaîne non indiquée) | Dossiers et chutes dans Premiere (titre non fourni) | https://www.youtube.com/watch?v=xcilOo3AcEg | Entière (3:36). §2 ; disposition des pistes écartée. |
| Larry Jordan | Compressing Files For YouTube (Adobe Media Encoder), 07/04/2015 | https://www.youtube.com/watch?v=7mDQ5lB0-9U | Entière (5:50). Retenu : YouTube recompresse. Écarté : 720p. |
| Larry Jordan | Premiere Pro: Automatically Transcode Media and Create Proxy Files, 13/06/2020 | https://www.youtube.com/watch?v=jJOaS3t3d3Q | Entière (5:52). Trois codecs, ProRes Proxy. |
| Larry Jordan | Flux de proxys de Premiere (titre et date non fournis) | https://www.youtube.com/watch?v=gvXwwvOwH8A | Entière. Ingestion md5, dossier séparé, bascule. Affirmation sur l'export non retenue. |
| David V. Clarke | General 1: Premiere Pro's Project manager for backup and archive, 09/03/2016 | https://www.youtube.com/watch?v=zWCn7tYv4Ww | Entière (19:04). Options du gestionnaire ; codecs d'archive datés. |
| Darren Mostyn (titre non fourni) | Premiere vers DaVinci Resolve par XML | https://www.youtube.com/watch?v=C561OeNewME | Entière (~17 min). Référence avec timecode, mode d'échelle. Resolve non utilisé par Cabezer. |
| Jason Levine, Sean McDaniel (Adobe Live, vers 2022 déduit) | Master class Frame.io (titre non fourni) | https://www.youtube.com/watch?v=hBYlngfTPLE | Jusqu'à 37 min environ. Commentaires au timecode, versions. Plans et tarifs non couverts. |
| Auteur non indiqué | Conformation par un « hub » Resolve (titre non fourni) | https://www.youtube.com/watch?v=7wewapPxgis | Début (~9 min), reste parcouru. Référence en différence. |
| Andrew, D80 Microphones | Sound 101 : le timecode | https://www.youtube.com/watch?v=msXlVokMK7w | Parcourue, non retenue. |

**Documentation et code lus**
- FFmpeg (https://github.com/FFmpeg/FFmpeg), `doc/filters.texi` et `doc/ffmpeg.texi` : `blackdetect`, `freezedetect`, `silencedetect`, `ebur128`, `drawtext` (drop-frame), `psnr`, `ssim`, `-fps_mode`, exemple `hevc_videotoolbox … -tag:v hvc1` ; `libavcodec/videotoolboxenc.c` : options des encodeurs VideoToolbox (aucune mesure de qualité). Seuls ces passages lus.
- AdobeDocs, API UXP de Premiere (https://github.com/AdobeDocs/uxp-premiere-pro) et exemples : `EncoderManager`, `ExportType`, `ProjectItemColorLabel`.
- docsforadobe, guides de scripts Premiere (https://github.com/docsforadobe/premiere-scripting-guide) et After Effects (https://github.com/docsforadobe/After-Effects-Scripting-Guide) : `exportAsMediaDirect`, `isOffline`, `Track.isMuted`, `TrackItem.disabled`, `usedFonts`, `consolidateFootage`, `reduceProject`.
- edunascimentt, `video-editor-assistant`, `premiere-notes.md` (https://github.com/edunascimentt/video-editor-assistant ; lu en partie) : sens de `start`, `end`, `in`, `out`, `ntsc`, −1 dans les xmeml ; notes d'un auteur de pipeline, non officielles.
- DELAxGithub, `davinciauto`, `premiere/projects/022/inputs/022_edit.xml` (https://github.com/DELAxGithub/davinciauto) : export xmeml de Premiere de tiers (10 clips) servant à tester `xml-coupes.py` ; pas un export de Cabezer.

**Extraits de recherche, pages non ouvertes**
- YouTube Help, « YouTube recommended upload encoding settings » (https://support.google.com/youtube/answer/1722171) : repères SDR 1080p, 1440p, 2160p ; codec, profil, audio ; pas de limite imposée.
- Adobe Help, « Hardware-accelerated encoding and decoding in Premiere » (https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/hardware-accelerated-decoding-and-encoding.html) : H.264/H.265 sur Apple Silicon.
- Adobe Community : « No VBR dual pass for H.265 hardware encoding, stay with H.264 ? » (https://community.adobe.com/t5/premiere-pro-discussions/no-vbr-dual-pass-for-h-265-hardware-encoding-stay-with-h-264/td-p/11352036), « No Hardware Encoding on M1 Pro » (https://community.adobe.com/t5/premiere-pro-discussions/no-hardware-encoding-on-m1-pro/td-p/12485400), « Premiere Pro 25.2: Hardware encoding greyed out / unavailable » (https://community.adobe.com/questions-729/premiere-pro-25-2-hardware-encoding-greyed-out-unavailable-1418072) : VBR 1 passe, option grisée.
- Puget Systems, « Premiere Pro 14.2 H.264 and H.265 Hardware Encoding Performance » (https://www.pugetsystems.com/labs/articles/premiere-pro-14-2-h-264-and-h-265-hardware-encoding-performance-1778/) et « H.264 Hardware Acceleration in Adobe Media Encoder - Good or Bad? » (https://www.pugetsystems.com/labs/articles/video-h-264-hardware-acceleration-in-adobe-media-encoder-good-or-bad-1211/) : autres machines que le Mac.
- Guides tiers, dimensions seulement : Instagram 4:5 = 1080 × 1350 (https://influencermarketinghub.com/instagram-video-size/, https://posteverywhere.ai/blog/instagram-aspect-ratios) ; Shorts carrés (https://riverside.com/blog/youtube-shorts-dimensions).

**Essais du 12/10/2026** (ffmpeg et ffprobe 6.1.1, fichiers générés) : les quatre scripts hors Premiere, `drawbox`, `ssim`, `psnr`, drop-frame, repliement mono, sommes de contrôle, niveaux H.264. `lister-clips.jsx` jamais exécuté dans Premiere.

**Hôtes refusés par le proxy, non contournés** : helpx.adobe.com, support.google.com, tech.ebu.ch, partnerhelp.netflixstudios.com, support.tiktok.com, www.cisa.gov, ffmpeg.org, larryjordan.com, ppro-scripting.docsforadobe.dev, developer.adobe.com, web.archive.org. À remonter à l'administrateur.

