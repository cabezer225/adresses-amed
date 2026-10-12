# Documentaire, essai vidéo et montage d'archives (familles Story et films/séries)

> **Réponses de Cabezer du 12/10/2026 — elles priment sur cette fiche**, en particulier sur sa section « Décisions à demander ». **Format d'abord, famille ensuite (SKILL §2)** : long (L-Food, L-Story, L-Tech, L-Films, L-Life) ou court (C-Food, C-Story, C-Tech, C-Films, C-Life) ; codes de cette fiche : D = C-Food, F = L-Food, S = L-Story, P = L-Films, T = L-Tech ; nouvelle famille Lifestyle (vlogs, face caméra : aucune musique, SFX comme la dégustation). **Tous les courts** : hook demandé, sous-titres mot à mot, aucune musique, SFX comme la dégustation, punch-ins secs, appel au commentaire, notation sur 10, identité propre au court. **Longs** : SRT seul en France ; composition musicale en Story, food et tech ; respirations d'émotion gardées en films/séries et au verdict du food long ; 4K si rushs 4K. Aussi : identité Story v15 et générique « Amed Story 🧢 » supprimés ; jamais de foley d'aliment ; ambiance en dégustation proposée au premier usage ; un rendu de sous-titres par passage ; intervenants identifiés à la première apparition (hors courts food) ; au plus deux passes de retravail sous 8 ; Tesseract, Higgsfield et SCANDALE FOOD retirés. **Réponses techniques (série 3)** : interface de Premiere et d'AE en anglais ; scripts AE et Terminal autorisés ; stock libre de droits sans redemander ; tout SFX de la banque Pixabay permis ; arrêt sur image permis partout ; pas de test de photosensibilité ; audio YouTube 384 kbit/s ; proxys toujours en long ; Frame.io pour les relectures ; WhisperX à installer ; « 19h30 » et « 12,50 € » ; Liquid Glass à recréer. Liste complète : `../decisions-en-attente.md`.

Fiche de référence du skill `cabezer-premiere-shorts`, publiée dans `references/pro/`. Elle apprend à monter un récit documentaire ou un essai : partition, preuve, photo, archive, carte, voix, extrait de film, crédits. Dernière révision : 12/10/2026, harmonisée avec `../decisions-harmonisation.md` de la passe 2. Versions visées : Premiere et After Effects 25.x–26.x, à confirmer sur la machine de Cabezer (`pilotage-environnement-reprise.md`).

**Légende des preuves :** **[T]** transcription lue en entier (sous-titres automatiques de YouTube, non relus ; minutes de la transcription) · **[Lu]** fichier ouvert et lu le 12/10/2026 (dépôts GitHub publics) · **[Testé ici]** commande exécutée sur fichiers synthétiques (ffmpeg 6.1.1) · **[K]** connaissance générale, à vérifier sur sa version · **[X]** extrait de résultat de recherche, page non ouverte · **[Choix]** décision de cette fiche, sans valeur de règle.

**Limite.** Légifrance, l'aide Adobe, ffmpeg.org, docsforadobe.dev, Wikimedia Commons et la presse juridique sont refusés par le proxy. Ce qui touche à Adobe (hors API de script) et au droit reste **[K]** ou **[X]**.

## Quand lire cette fiche

Lire cette fiche avant de structurer une vidéo Story (documentaire de société) ou un essai sur un film ou une série (PRISME) ; de poser une photo, un document, une archive, une carte, une capture ; de monter une interview ; de citer un extrait ; d'identifier une personne qui parle ou de créditer une source.

Ne pas la lire pour : l'identité visuelle (skill §6), le dérush technique (`premiere-pro-avance.md`), les courbes et expressions AE (`after-effects-motion-design.md`), le rythme général (`fondamentaux-montage-narratif.md`), l'ouverture et la rétention (`retention-youtube-long.md`), la couleur (`etalonnage-gestion-couleur.md`), le droit à l'image, les mentions commerciales et la typographie à l'écran (`conformite-droits-accessibilite.md`), le contrôle du MP4 (`organisation-livraison-qc.md` §6).

**Hiérarchie (skill §1) :** brief de Cabezer → règles du skill → `../decisions-harmonisation.md` → fiches → tutoriels. Chaque technique dit quand l'utiliser, quand l'éviter et pour quelles familles : dégustation (D), food long (F), Story (S), films/séries PRISME (P), tech (T), hors familles (H). La dégustation est presque toujours « non » (coupes franches, pas d'archives).

**Définition (skill §1, §16).** Une *animation graphique* (tracé, surlignage, carte, étiquette, collage, parallaxe, carton) se fait dans After Effects, en calques natifs modifiables. Un *traitement de plan* (recadrage, punch-in sec, mouvement sur une photo qui désigne un détail, fondu, vitesse) se fait dans Premiere. Aucune image ni animation n'est générée par IA.

## Sommaire

1. Principes · 2. Du sujet à la partition · 3. Ouverture et promesse · 4. Interviews et sources qui parlent · 5. Montrer la preuve (5.3 temps de lecture) · 6. Photos, archives, objets · 7. Cartes animées · 8. Le son · 9. Rythme et honnêteté du raccord · 10. Essai sur films et séries · 11. Cartons, chapitres, intervenants, crédits · 12. Sources, licences, extraits tiers · 13. Familles en bref · 14. Erreurs de débutant → réflexes de pro · 15. Liste de contrôle · 16. Décisions à demander · 17. Sources étudiées

---

## 1. Principes à retenir

1. **La clarté passe avant l'ingéniosité.** Bolanos : la confusion est la première raison de partir [T, 35i_DKPW6sc 7:09] (non mesuré). Perell : « qui fait quoi à qui » [T, zq4b96m1AvM 22:10]. Retirer toute image qui n'aide pas à comprendre.
2. **Les faits s'enchaînent par « donc » ou « mais », pas par « et puis »** (Bolanos [T, 10:43]). Une scène qui n'accepte ni l'un ni l'autre est candidate à la coupe [T, 11:13].
3. **Le spectateur a besoin de temps pour ressentir.** Zhou : l'échec de Luke dure environ 30 s, celui de Scott 30 images, et on ne croit pas au second [T, 3Q3eITC01Fg 3:38–4:41].
4. **Le son place le spectateur et porte la tension** (Nerdwriter sur *Munich* [T, 3:42–5:17]).
5. **Chaque affirmation est vérifiée et sourcée** (Perell, « source dock » [T, 30:25–31:25]) : `Suivi/verifications.md` et `Suivi/licences.csv` (skill §8).
6. **La preuve est désignée par la voix et par l'image au même instant** : « circle, shine, zoom » chez Vox (Perell [T, 61:12]).

**Désaccords à garder tels quels :** Perell rappelle la promesse dans la première minute [T, 12:54], Bolanos juge inutile de « payer » le titre tout de suite [T, 4:36] (compatibles, §3). Voix d'abord pour un documentaire parlé (Perell), image d'abord pour une animation (Kurzgesagt) : pour Story, voix d'abord.

**Limite de Claude.** Claude n'entend pas : il mesure, extrait des images, lit la forme d'onde et écrit « mesuré, non écouté » (skill §1). L'écoute finale revient à Cabezer.

---

## 2. Du sujet à la partition

**Quand :** S, P, F long, H. **Éviter :** témoignage pur où la question naît des faits ; Perell est revenu d'une préparation qui « faisait entrer l'histoire de force dans un plan » [T, 8:48]. Claude monte à partir du script de Cabezer (skill `cabezer-video-scripts`), sans le réécrire.

**Procédure.**
1. **Écrire la question en une phrase orale, avec une lentille.** Exemple de Bolanos : « Comment les pyramides ont-elles *vraiment* été construites ? » [T, 2:04]. Lire d'abord `Suivi/brief.md` (skill §3, étape 0). Si ni le brief ni le script ne la contiennent, la demander ; en mode autonome, écrire la phrase la plus proche du brief et la consigner « en attente de validation ».
2. **Contrôler la promesse :** titre et miniature annoncent ce que la vidéo tient (Perell [T, 50:55]) ; test de `retention-youtube-long.md` §2.1.
3. **Colonne vertébrale.** Histoire chronologique : la chronologie est la structure (Perell [T, 18:04]) ; sinon, ordre par « donc » et « mais ».
4. **Faire la partition sur deux colonnes** (Perell [T, 17:31]). **Adaptation au skill :** une ligne par *idée*, pas par phrase (« une image par idée, jamais par mot », skill §6, Story). Support choisi parmi les quatre du skill : preuve réelle, univers suivi, schéma qui se construit, visage.

| Phrase(s) dites | Ce que le spectateur doit comprendre | Support | Source et droit | Durée minimale |
|---|---|---|---|---|
| « En 1974, la loi change… » | Qu'une règle précise a changé à cette date | Preuve réelle : page du texte, ligne surlignée | Journal officiel, URL, date (`Suivi/licences.csv`) | Preuve : 3 s au moins ; texte ajouté : §5.3 |

5. **Après chaque interview ou source, écrire trois phrases :** ce qu'elle confirme, contredit, ce qui manque (Perell [T, 6:43]).
6. **Passes** (skill §3) : assemblage sur la voix seule (le « shame cut » de Perell [T, 2:35]) → **validation du dérush par Cabezer** → structure et habillage → mouvements → couleur → musique et mixage → sous-titres → contrôle.
7. **Séquence `CHUTES_<nom>`** pour tout passage aimé mais retiré. Pearlman : « si tu retires quelque chose, tu le regrettes presque jamais » [T, RqI4kD8RQng 37:02].

**Critère de réussite :** chaque ligne répond à « qu'est-ce que le spectateur comprend ici que la voix seule ne lui donne pas ? ». Sans réponse, la ligne devient « visage ».

---

## 3. Ouverture et promesse

**Quand :** S, P, F long, H. **Éviter :** D (hook : skill §5, barème du §5.2). Détail : `retention-youtube-long.md` §2.

**Deux obligations distinctes.**
1. **Confirmer le sujet et la promesse avant la 30e seconde**, montrés ou dits. En Story, cette confirmation tombe dans l'intro face caméra (le générique « Amed Story » a été supprimé le 12/10/2026 ; un futur générique validé se placerait après cette intro) (`retention-youtube-long.md` §2.1).
2. **Rappeler l'enjeu ensuite, sous forme de question, dans la première minute, sans y répondre ; répondre à la fin.** C'est la position de Perell [T, 12:54] ; Bolanos ne paie pas non plus le titre tout de suite [T, 4:36]. Elle ne retarde pas l'obligation 1.

**Quatre entrées observées** (Perell [T, 18:36–19:38]) : par l'action, par l'objet à regarder, par le ton, par la question.

**Procédure.** (1) Choisir une image ou une phrase d'ouverture qui ne dit pas encore la thèse. (2) Faire le test de promesse (« Le spectateur a cliqué pour voir ___ »). (3) Poser la question de rappel dans la première minute, sans y répondre. (4) Finaliser l'ouverture en dernier (skill §3) ; ouvrir une boucle au début, la refermer à la fin (skill §4). (5) Vérifier par transcription que le sujet et la promesse sont prononcés avant la 30e seconde (en Story, avant le générique).

---

## 4. Interviews, voix et sources qui parlent

### 4.1 Fidélité au sens

Jamais de « frankenbite » (réarranger des mots pour leur faire dire autre chose ; skill §4 et §8). Permis : retirer un faux départ pour garder ce que la personne voulait dire (« deux mozzarelles… trois, trois » devient « trois mozzarelles »). Jamais : un collage qui crée une affirmation que la personne n'a pas faite ou change le sens. Avant de valider une coupe : relire la phrase recollée et demander « la personne reconnaîtrait-elle ce qu'elle a dit ? ». Une pause change aussi le sens (`fondamentaux-montage-narratif.md` §8.1).

### 4.2 Dérusher par la transcription (Premiere)

Procédure : `premiere-pro-avance.md` §5.1. Compléments :
1. Transcrire, lire, puis poser des marqueurs colorés par fonction dans le panneau Texte (Text) : *preuve, contrepoint, concession, émotion*.
2. Organiser en bacs : un bac par personne, séquences de sélection `SEL_<thème>` [X, Ron Delsener Presents].
3. Filtrer par locuteur pour écarter l'intervieweur [X] ; les points d'entrée et de sortie automatiques doivent être actifs pour que les modifications de texte arrivent sur la timeline [X, fil Adobe]. À vérifier sur sa version.
4. **Le montage par le texte repère et pré-découpe, rien de plus.** Chaque coupe est ensuite recalée à la forme d'onde et à l'énergie du son, jamais aux temps de la transcription (skill §4). Aucune suppression en masse. **S : ne pas supprimer les pauses en masse** ; garder les respirations qui portent un regard ou une émotion (skill §6, Story).

### 4.3 Raccord sonore et écoute

Combler un saut de fond sonore avec le silence de la pièce du même rush (skill §4 ; `audio-dialogue-sound-design-mixage.md` §7.1) ; pour une archive, prélever le silence de la même bande. Fondus de raccord et J/L-cuts : seulement là où un clic s'entend ou pour relier deux plans, sans mordre l'attaque d'un mot (même fiche, §3.2 et §3.3). Information à retenir : la personne dit la phrase à l'écran ; doute ou émotion : rester sur celui qui écoute (`fondamentaux-montage-narratif.md` §8.2).

**Identification :** une personne qui parle longuement est nommée une fois (§11.3).

**Réussite :** on entend la personne sans savoir où sont les coupes ; chaque coupe reste « cohérente avec le sens ».

---

## 5. Montrer la preuve : désigner, documenter, laisser lire

### 5.1 Désigner l'élément au moment où la voix le nomme

**Pourquoi :** la voix invite et l'image bouge au même instant (Perell sur Vox [T, 61:12–61:43]), à condition de rester sélectif. **Quand :** S (documents, posts, pages officielles), P (affiches, plans), F, T, H. **Éviter :** D ; plus d'une désignation à la fois ; texte pas encore lu (§5.3).

**Procédure After Effects** (la désignation est une animation graphique).
1. Cercle, soulignement ou flèche : calque de forme avec **Tracés rognés (Trim Paths)** ; animer **Fin (End)** de 0 à 100 % sur 8 à 15 images avec une courbe d'accélération (`after-effects-motion-design.md` §8.1). Les propriétés s'appellent `ADBE Vector Trim Start`, `ADBE Vector Trim End` et `ADBE Vector Trim Offset` dans l'API de script [Lu : guide de script AE, noms de correspondance]. La fourchette de 8 à 15 images vient des entrées et sorties du skill (§6, Story, point 9) [Choix].
2. Surlignage de preuve : rectangle en mode Multiplier, échelle X de 0 à 100 %, point d'ancrage à gauche (même fiche, §8.1).
3. Caler le début du tracé sur le début du mot qui désigne l'élément.
4. Laisser l'élément visible tant que l'idée continue (skill §6, Story, point 9).
5. Passage en langue étrangère : afficher, pendant le coup de feutre, la traduction française fidèle et courte ; ne pas traduire les dates ; ne pas écrire « traduit de… » (skill §6).

**Réussite :** à l'arrêt sur l'image où le tracé est terminé, l'élément visé est lisible et un seul tracé est présent.

### 5.2 Document ou capture réels, explorés

Suivre `after-effects-motion-design.md` §10.1 : image à deux fois la composition au moins, calque 3D, caméra pilotée par un nul, pause de lecture complète sur chaque détail, déplacement de 8 à 15 images, aucune dérive décorative (skill §6, Story, point 11). **Un document à lire ne reçoit jamais le mouvement Premiere du §6.4.** Avant d'importer une capture ou un document, masquer les données qui ne doivent pas être visibles (onglets, e-mails, notifications, jetons) : `conformite-droits-accessibilite.md`.

### 5.3 Temps de lecture : cette section fait foi

**Règle du skill (§6, Story, point 9).** Toute information écrite reste *entièrement lisible* au moins **max(1,5 s ; 1 s + caractères/15)**. Aucune source lue ne propose un autre chiffre : n'en introduire aucun.

| Élément | Règle |
|---|---|
| Texte d'habillage, carton, traduction de passage étranger, date, tampon, ligne de liste, légende, crédit ou identification | Formule ci-dessus |
| Blocs de sous-titres des familles longues (S, F, P, T, H) | Formule ; lignes : skill §9 |
| Preuve réelle | 3 s au moins ; 3 à 11 s en pratique |
| Image sans texte | 2 s au moins |
| Univers visuel suivi | Plans de 2 à 3 s |
| Coupes rapides nommées (accumulation sans texte à lire) | 0,4 à 0,8 s, seulement quand la vitesse est le sens |
| Sous-titres mot à mot de dégustation | Hors formule : rythme de la parole (`formats-courts-verticaux.md` §4.2) |

Les repères de densité des tutoriels ne valent que pour des plans sans texte.

**Procédure.**
1. Compter les caractères affichés, espaces compris : `python3 -I -c "import sys; [print(len(s), round(max(1.5, 1+len(s)/15), 2), s) for s in sys.argv[1:]]" "1923" "Plan de Londres, 1666"` [Testé ici : 4 caractères → 1,5 s ; 21 → 2,4 s ; 45 → 4,0 s].
2. Compter la lecture *entre la fin de l'entrée et le début de la sortie* (8 à 15 images chacune, en plus). À 30 i/s, 2,4 s font 72 images ; convertir à la cadence de la séquence (`organisation-livraison-qc.md` §3.3).
3. Débit trop rapide : prolonger, cadre persistant, texte raccourci ou regroupé (skill §6, Story, point 9). Pour un bloc de sous-titres que la parole ne laisse pas durer, regrouper ou condenser avant de raccourcir la lecture.

**Réussite :** sur le MP4 exporté, lire chaque texte avec le son coupé, sur un téléphone, sans revenir en arrière.

---

## 6. Photos, archives et objets

### 6.1 Obtenir, mesurer, documenter

Procédure (Raymond [T, wTr6df0H5Po 0:38–3:39], complétée par le skill §8).
1. Demander la **plus haute résolution** à l'ayant droit : une image reçue d'un téléphone ou d'un réseau social est compressée.
2. Wikimedia Commons : ouvrir la fiche, récupérer le lien « fichier original », relever auteur (le créateur, pas forcément le téléverseur), licence, source pour `Suivi/licences.csv` (§12).
3. **Mesurer avant d'importer :** `ffprobe -v error -show_entries stream=width,height -of csv=p=0 image.jpg` [Testé ici]. **Largeur nécessaire = largeur de la séquence × zoom maximal prévu** : séquence 3840 px, zoom 130 % → 4992 px au moins [Choix]. Raymond juge problématique toute image sous 1920×1080 en séquence HD [T, 2:08].
4. Fichier incompatible : capture d'écran à la résolution maximale (Raymond [T, 2:38]), consignée.
5. Personnes identifiables sur la photo : appliquer `conformite-droits-accessibilite.md` avant de la poser.

### 6.2 Importer sans déformer

**Piège central** (Raymond [T, wTr6df0H5Po 4:09–5:12]) : ne jamais glisser une photo sur « Nouvelle séquence » ; la séquence prend la forme de la photo. Utiliser la séquence du projet (skill §3).

**Mise à l'échelle des médias** (Préférences > Média > « Mise à l'échelle par défaut des médias », libellés à confirmer). Sources concordantes [X : employé Adobe sur community.adobe.com, Mixing Light, Larry Jordan] :
- **« Définir à la taille du cadre » (Set to Frame Size)** garde les pixels d'origine et ajuste Échelle (Scale) : un zoom ensuite reste net jusqu'à la résolution native ;
- **« Mettre à l'échelle à la taille du cadre » (Scale to Frame Size)** rééchantillonne à la taille de la séquence et affiche Échelle à 100 % : un zoom ensuite rend l'image granuleuse ;
- le défaut est « Mettre à l'échelle » et ne change que les futurs clips ; pour un clip déjà posé, clic droit et choisir l'autre option (libellé à confirmer).

**Toute photo qui recevra un mouvement (§6.4) passe en « Définir à la taille du cadre »** ; lire Échelle dans les Contrôles d'effets (Effect Controls) : plus de 100 % est normal.

### 6.3 Remplir le cadre sans barres noires

Traitements de plan (Premiere), d'après Raymond [T, 5:12–7:15] : **fond flou** (copie du clip sur la piste du dessus, copie du bas à l'échelle de remplissage avec **Flou gaussien**, Effets vidéo > Flou et netteté ; libellés et geste à confirmer), **fond texture** (bois, pierre) ou **recadrage**. Fond flou : H, F, T, photo isolée ; éviter pour un portrait ou un document à lire. **Story :** fond flou en attendant la nouvelle identité (la grammaire v15, papier rose et tirages 3D, a été supprimée le 12/10/2026). **P :** identité validée ; fond flou avec l'accord de Cabezer.

### 6.4 Mouvement sur une image fixe (« Ken Burns », photomation)

**Règle commune (décisions d’harmonisation D2, skill §6 point 11 et §7).** Un mouvement sur une image fixe **désigne un détail ou présente un visage**. Il laisse un temps fixe avant et après, suit une courbe douce, et ne s'exécute **jamais sur un plan qui porte un texte à lire**. La dérive purement décorative est exclue dans toutes les familles. Raymond l'applique à toute photo contre l'effet diaporama [T, 0:08] : pratique non reprise.

**Statut.** Le mouvement sur une photo qui désigne un détail est un traitement de plan : **Premiere** (Mouvement). Le cercle ou le surlignage qui désigne est une animation graphique : AE (§5.1). Un document à lire s'explore dans AE (§5.2).

**Quand :** présenter un personnage en partant du bas de la photo vers le visage [T, 7:45] ; passer d'un détail à l'autre au fil de la voix. **Éviter :** photo de fond sans désignation, même mouvement sur plusieurs photos de suite, plan déjà animé, document à lire, insert de bouchée. **Familles :** S et P (désignation, visage) ; F, T, H : désignation seulement, cas rare ; D : non.

**Photo longue sans rien à désigner :** ne pas la faire dériver. Dans l'ordre : revenir au visage de Cabezer, la remplacer par un plan de preuve, la raccourcir à la durée de l'idée, ou poser la désignation prévue. Une image fixe tenue 2 à 3 s est correcte (§5.3).

**Procédure Premiere** (vérifiée en transcription [T, 8:46–14:24] ; libellés à confirmer) :
1. Contrôles d'effets > Mouvement (Motion) : Position, Échelle, Rotation. Photo importée en « Définir à la taille du cadre » (§6.2).
2. Tête de lecture un peu après le début (**pause initiale**), chronomètres de Position et d'Échelle activés.
3. Avancer sur le mot qui désigne le détail, changer la valeur : l'image clé se crée.
4. **Pause entre deux mouvements :** image clé *dupliquée* avec le bouton d'ajout, jamais en recliquant le chronomètre (il efface les clés).
5. Lisser : clic droit sur les clés > Interpolation temporelle > Bézier automatique ou continu, ou Ease In / Ease Out. Jamais linéaire pour un mouvement progressif (skill §7).

**Valeurs de départ [Choix] :** pause initiale et pause finale d'au moins 0,5 s ; déplacement de 8 à 15 images ; échelle finale dans la résolution disponible ; aucun mouvement pendant une désignation par la voix. **Réussite :** le détail désigné est net et lisible quand la voix le nomme.

### 6.5 Collage, passé/présent, parallaxe

**Collage et objets posés (S, P, F, H ; T rare ; D non).** Raymond le monte avec l'effet 3D de base de Premiere [T, 16:30–19:35] ; c'est une animation graphique : AE. Photos à leur résolution native dans une composition à la taille de la séquence, calques 3D, caméra parentée à un nul `CAM_PILOTE` (`after-effects-motion-design.md` §10.1), photos désalignées (rotation de quelques degrés, chevauchements, petits écarts de Z), style de calque **Ombre portée** [Choix, à l'œil : opacité 40–50 %, distance 8–15 px, flou 20–40 px], échelle augmentée si des bords noirs apparaissent (Raymond [T, 19:05]). **Quand :** relation entre plusieurs documents d'une période. **Éviter :** sources sans lien (skill : un univers suivi).

**Passé et présent (S, F, H ; pas P, T, D).** Raymond superpose une photo ancienne à une vidéo actuelle du même lieu [T, 20:06–21:09]. Dans Premiere : figer un plan actuel, poser la photo à 50 % d'opacité pour **caler** Échelle et Position, remettre à 100 %, puis fondu. Un masque animé est une animation graphique : AE. **Condition :** lieu réel et reconnaissable, correspondance non fabriquée. **Réussite :** une arête de bâtiment reste immobile pendant le fondu.

**Parallaxe 2.5D (S, P).** AE seulement (`after-effects-motion-design.md` §10.2 ; Raymond renvoie à une vidéo non lue [T, 21:41]). Séparer une photo en calques suppose de reconstituer des parties cachées : jamais par remplissage génératif ni IA ; limiter l'amplitude aux plans réellement disponibles.

### 6.6 Archives vidéo : contrôler avant de monter

```
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,sample_aspect_ratio,display_aspect_ratio,r_frame_rate,field_order,pix_fmt -of default=nw=1 archive.mov
ffmpeg -hide_banner -i archive.mov -vf idet -frames:v 200 -an -f null - 2>&1 | grep "Multi frame" | tail -1
```
[Testé ici sur un fichier synthétique entrelacé TFF : la seconde commande renvoie le décompte TFF/BFF/Progressive ; garder la **dernière** ligne, ffmpeg 6.1.1 en a affiché deux.]
- **TFF ou BFF élevé, Progressive proche de 0 :** entrelacé. Régler l'ordre des trames par Clip > Modifier > Interpréter le métrage (Interpret Footage) [K, libellés à confirmer] avant tout traitement.
- **4:3 dans une séquence 16:9 :** bandes sur le fond de l'identité (papier en Story), jamais d'étirement (§16).
- **Cadence différente :** la noter ; conformer selon `premiere-pro-avance.md` §3.4. Ni mélange d'images ni flux optique par défaut : ce sont des images calculées (§16).
- **Aucune restauration générative par défaut :** colorisation, montée en résolution IA, interpolation IA, Generative Extend et remplissage d'après le contenu reconstruisent des pixels : seulement sur demande explicite de Cabezer (skill §16), consignée dans `Suivi/decisions.md`, avec mention à l'écran ou en description.
- **Couleur :** archives traitées à part (skill §10), correction primaire minimale, mêmes réglages par lot, ni LUT de caméra ni grain ajouté. **Droit :** une archive de télévision ou d'agence est un extrait tiers (§10.4, §12).

**Réussite :** aucune bande étirée ; pas d'artefacts en peigne sur un mouvement horizontal à 100 % d'aperçu.

---

## 7. Cartes animées

**Quand :** S, P (géographie, trajet, frontière), F, T, H. **Éviter :** D ; carte décorative sans fait à montrer ; plus de deux ou trois lieux nommés par plan. Une carte est une animation graphique : AE.

**Source :** Johnny Harris, « How I Make My Maps » [T, GsojLuJpe_0], sponsorisé par Intel (performances annoncées non retenues). Deux méthodes ; seule la première respecte « gratuit uniquement ». Harris ne s'en sert plus, car moins efficace [T, 1:10].

### 7.1 Méthode sans plugin (After Effects)

1. **Fond de carte vectoriel, pays séparés.** Le fichier de Harris est réservé à ses abonnés Patreon [T, 5:46]. **Natural Earth** est « dans le domaine public », utilisable à des fins commerciales sans permission ; le crédit est facultatif (« Made with Natural Earth ») [Lu : LICENSE du dépôt nvkelso/natural-earth-vector]. Conversion en SVG avec **mapshaper** (gratuit, licence MPL 2.0, export SVG, flux avec Illustrator cité dans son journal de versions) [Lu : README, LICENSE, CHANGELOG de mbloch/mapshaper] ; la procédure exacte reste à tester. Consigner source et licence dans `Suivi/licences.csv`.
2. Importer dans AE : **Métrage (Footage)** si une pièce suffit, **Composition** si chaque pays a sa couleur [T, 6:17]. Harris passe par Illustrator (.ai) ; l'import direct d'un .svg et la présence d'Illustrator sont à vérifier. Composition à la taille de la séquence ; solide pour l'eau [T, 6:47–7:17].
3. Calque > Nouveau > **Objet nul (Null Object)** `CTRL_CARTE`. Parenter la carte, **puis tous les calques ajoutés**, à ce nul [T, 7:48] : un seul objet à animer, une seule courbe, aucun décalage entre carte, surlignages et étiquettes.
4. Activer la **rastérisation continue** (Continuously Rasterize, icône en soleil, libellé FR à confirmer) : le vecteur reste net au zoom [T, 8:18]. Dans l'API de script, c'est l'attribut `collapseTransformation` du calque [Lu : AVLayer, guide de script AE].
5. **Zoom vers un pays :** point d'ancrage du nul sur ce pays (outil Déplacer le point d'ancrage, raccourci Y à confirmer [T, 8:18]), Échelle et Position sur deux images clés, courbes lissées, pause de lecture avant et après (§5.3).
6. **Colorer un pays :** solide coloré ; copier le tracé depuis Illustrator et le coller sur le solide dans AE : il devient un masque [T, 9:18–10:19] (alternative [K] : Calque > Créer > Créer des formes à partir d'un calque vectoriel). Parenter au nul. Apparition : Opacité ; frontière ou trajet : Tracés rognés.
7. **Étiquette qui garde sa taille au zoom.** Expression de cette fiche, non exécutée dans AE (tester sur une copie). Un calque parenté multiplie sa propre Échelle par celle de son parent ; la propriété Échelle renvoie un pourcentage sous forme de tableau [Lu : référence d'expressions, `Layer.scale`]. Sur l'Échelle d'une étiquette 2D parentée au nul :
```
s = Math.max(thisComp.layer("CTRL_CARTE").scale[0], 1);
[10000/s, 10000/s]
```
Échelle de l'étiquette × échelle du parent reste égale à 100 %. Trait d'épaisseur constante : `10 * 100 / Math.max(thisComp.layer("CTRL_CARTE").scale[0], 1)` sur la largeur du contour (10 = pixels voulus).
8. **Rendre un brouillon**, l'importer dans Premiere, vérifier le timing, corriger, puis rendre le final [T, 26:17–26:48].

**Réussite :** aucun bord pixellisé au zoom maximal ; étiquettes lisibles ; carte, surlignages et étiquettes bougent comme un seul bloc.

### 7.2 Méthode avec plugin : payante, à signaler

Harris emploie GeoLayers (styles Mapbox [T, 18:33]) et parle de « 200 » sans devise, en 2021 : **prix actuel à vérifier. Plugin payant : ne pas l'installer ni le proposer sans accord de Cabezer.** Mapbox Studio est « gratuit pour un usage non commercial » selon Harris [T, 13:54] : conditions actuelles non vérifiées. **Frontières contestées :** choisir une convention, la consigner dans `Suivi/verifications.md`, la tenir sur toute la vidéo [T, 14:57] ; sujet sensible : demander à Cabezer.

---

## 8. Le son du documentaire

### 8.1 Perspective, ambiance, soustraction

Nerdwriter sur *Munich* [T, kavxsXhzD48] : une ambiance continue fait le lit, quelques bruits-clés racontent, la tension monte par soustraction. **Familles :** S, P, F, T, H ; D : aucune ambiance continue ni musique par défaut.

**Pour une archive ou une scène de Story :**
1. **Garder l'ambiance d'origine** quand elle existe ; la couper complètement sonne faux.
2. Isoler un ou deux bruits-clés (une porte, un moteur) par un léger gain, sans ajout.
3. **Musique plus basse ou absente sous une source qui parle** (skill §11) ; elle ne doit jamais faire dire « quelle belle musique » (Bolanos [T, 16:17]). Niveau de la nappe de Story : environ 24 dB sous la voix, mesuré comme en `audio-dialogue-sound-design-mixage.md` §5.5, réglage final à l'écoute de Cabezer.
4. **Silence vrai de 1 à 2 s** avant une bascule (skill §11) : couper la musique, garder le fond de la pièce de la voix (même fiche, §5.5).
5. **Aucun faux son présenté comme venant de la scène** : pas de bruitage « d'époque » sur une archive muette sans l'accord de Cabezer (`retention-youtube-long.md` §7.4).

### 8.2 Voix off ou voix enregistrée en studio

Source unique : Thomas Flight [T, dLoAw_mveFs] ; **valeurs de départ, à régler à l'écoute**. La chaîne de traitement de la voix est décrite une fois dans `audio-dialogue-sound-design-mixage.md` §4.
- **Distance au micro :** 8 à 10 pouces (20 à 25 cm) ; tester trois distances et choisir à l'oreille [T, 3:08–4:10], si Cabezer enregistre une voix off.
- **Souffles :** baisser le niveau plutôt que couper [T, 9:19–10:54] : S, quand la respiration porte le regard (skill §6) ; D : couper (skill §5).
- **Réduction de bruit :** la limiter ; si on l'entend, mieux vaut laisser le bruit [T, 11:25–12:56] ; comparer avant/après, sans dépasser le traitement uniforme du skill (§11).
- **Creux d'EQ de la musique :** large (Q faible) entre 1200 et 1400 Hz, de l'ordre de −6 à −8 dB [T, 15:00–16:01]. **C'est la profondeur d'un creux d'égalisation, pas le niveau de la musique sous la voix** ; Flight dit qu'il n'existe pas de niveau fixe [T, 13:58–14:30].

### 8.3 Contrôler le son du MP4 exporté

Mesures : `audio-dialogue-sound-design-mixage.md` §10 et la bibliothèque unique de `organisation-livraison-qc.md` §6 ; repères de contrôle : audio §9. Les valeurs informent ; l'écoute de Cabezer décide ; Claude n'écrit jamais « écouté » pour une mesure.

**Réussite :** chaque phrase se comprend au haut-parleur d'un téléphone, d'après Cabezer ; une archive se distingue de sa voix sans saut brutal de niveau (mesuré, non écouté).

---

## 9. Rythme, coupe et honnêteté du raccord

Principes de rythme : `fondamentaux-montage-narratif.md` §9. Compléments propres au documentaire :
- **Laisser le temps de ressentir.** Après une révélation, tenir le visage ou l'objet plus longtemps qu'en dégustation (valeur de départ : retomber en deux fois le temps de montée, S et P). Respirations conservées : exception de Story (skill §6) ; l'étendre à P est une question ouverte (§16).
- **Coupe invisible, visible, dérangeante.** Invisible pour l'émotion [T, EFAP 6:15] ; visible, avec mouvement qui désigne, pour diriger le regard ; dérangeante seulement pour une émotion agitée [T, EFAP 7:16].
- **Couper sur l'impulsion du mouvement.** Pearlman : couper quand l'impulsion du mouvement suivant commence ; l'œil tarde à voir la coupe [T, RqI4kD8RQng 22:42–23:45]. Vérifier image par image. Source : montage de danse ; en documentaire, pour les plans de preuve et d'ambiance, pas pour les paroles.
- **Interdit sur des faits réels : le faux raccord de mouvement.** Pearlman enchaîne les gestes de deux personnes pour simuler un seul mouvement et ne le garde pas [T, 24:17–24:49]. **Règle [Choix] :** aucun raccord qui fait croire à la continuité d'un geste, d'un lieu ou d'un moment entre deux sources, sauf si la voix annonce le rapprochement (cas P : comparer deux plans de films).
- **Masquer un saut dans une interview :** coupe franche assumée → plan de coupe qui apporte quelque chose → second angle synchronisé → animation seulement si elle était prévue ; pas de Morph Cut par défaut (`premiere-pro-avance.md` §5.4).

**Réussite :** chaque plan de plus de 8 s a une raison notée : émotion, preuve à lire, regard.

---

## 10. Essai vidéo sur films et séries (P)

Sources lues : Nerdwriter, *Succession* [T, REhlyvtiIhQ] et *Munich* [T, kavxsXhzD48] ; Tony Zhou [T, 3Q3eITC01Fg]. Valarezo, Puschak et Flight (*1917*) n'ont pas pu être lus. **Familles :** P, T, H.

### 10.1 Thèse en question, preuves, contrepoint

Structure de *Succession* : ouverture à froid (0:00), question (0:33–1:03), preuves par extraits (1:03–3:37), complication (3:37–6:16), conclusion qui élargit la portée (6:46) [T, 7:46], choix d'un auteur et non règle. **Procédure Premiere :** dupliquer la séquence avant tout essai (skill §1) ; poser avant chaque extrait un marqueur de fonction (*preuve, contrepoint, concession, conclusion*) ; chaque extrait répond à une phrase de la thèse, sinon le retirer. La promesse suit §3.

### 10.2 Analyse plan par plan avec mesures

Zhou compare les durées de plans pour montrer la montée et la chute d'un récit [T, 3:38–4:09]. Mesurer avec `mesure-plans.py` (`organisation-livraison-qc.md` §6), fondé sur `select='gt(scene,0.3)',showinfo` [Testé ici : coupe franche retrouvée à 2 s]. Seuil 0,3 : valeur de départ ; les fondus enchaînés échappent à la détection. Regrouper par blocs de 10 plans ; la vérification à l'image décide.

### 10.3 Version alternative, élément par élément

Nerdwriter refait une scène avec sa propre bande-son pour montrer ce que l'original change [T, kavxsXhzD48 1:40–2:11]. Dupliquer la séquence ; **ne modifier qu'un élément à la fois** (son, durée d'un plan, ordre) ; montrer les deux versions à la suite ou côte à côte ; annoncer à la voix ce qui change. **Réussite :** on perçoit la différence avant que la voix la nomme.

### 10.4 Citer un extrait de film ou d'émission (extraits tiers, P et S)

Règle d’harmonisation : **durée minimale nécessaire, extrait commenté, source affichée ; un crédit n'est pas une autorisation ; risque Content ID signalé avant publication** (cadre juridique : §12 et `conformite-droits-accessibilite.md`).
1. **Fonction :** l'extrait est une preuve, pas un remplissage. Écrire la phrase de thèse qu'il prouve ; sans commentaire proche, le retirer.
2. **Quantité :** aucun seuil de secondes dans le texte de loi [X]. Règle de travail [Choix] : le plan nécessaire à la démonstration ; couper dès que la preuve est faite ; pas de scène entière sans la voix de Cabezer par-dessus.
3. **Source à l'écran :** titre, auteur ou réalisateur, source, pendant l'extrait (§11.4 ; skill §8).
4. **Registre :** une ligne par extrait dans `Suivi/licences.csv`, statut « citation (à valider) », minute dans la source et durée utilisée.
5. **Content ID :** avant publication, dire à Cabezer quels extraits peuvent déclencher une revendication automatique, sans promettre l'absence de revendication (skill §11) ; un système automatique ne reconnaît pas les exceptions au droit d'auteur [X : page d'aide YouTube sur le fair use, version italienne].
6. **INA :** service payant, devis ; rien sans l'accord de Cabezer (§12). **PRISME :** affiches et extraits officiels explorés en caméra 3D dans AE, aucun visuel généré (skill §6).
7. **Valeur ajoutée :** l'apport d'un essai est le commentaire (Bolanos [T, 17:49]). **Extrait sonore étranger :** sous-titres français relus (§16).

**Familles :** P et S ; F, T, H selon le brief ; D : aucun extrait tiers.

---

## 11. Cartons, chapitres, intervenants, génériques et crédits

### 11.1 Chapitres, direction artistique, générique

**Chapitres de Story : skill §6, Story, point 12** (silence, carton seul d'environ 3 s, signature musicale, déchirure à la reprise de la voix) ; construction : `retention-youtube-long.md` §8.1. Le moment « soul » sans preuve de Perell avant les titres de chapitre [T, 44:46–45:17] n'est pas appliqué : il ajoute un plan que la règle ne prévoit pas (§16). Générique : aucune source lue ; « Amed Story » a été supprimé le 12/10/2026, un nouveau générique sera à créer et faire valider.

**Direction artistique par vidéo.** Perell tient une page « ingrédients artistiques » par vidéo et refait la direction artistique à chaque fois [T, 37:38–42:12]. **Le skill l'interdit pour l'identité** (§6). Reprise compatible [Choix] : une fiche de vidéo qui liste les *objets et matières* du sujet (documents, symboles, textures de papier) dans l'identité validée, sans toucher à la palette, aux polices ni à la grammaire.

### 11.3 Identifier une personne qui parle (usage narratif)

L'identification (nom, fonction) est une information que la voix ne donne pas : ce n'est pas un « texte qui double chaque nom » (skill §6, Story, point 7). Règle à valider avec Cabezer sur un extrait (§16), appliquée en attendant :
1. **À la première apparition seulement**, pendant que la personne parle ; jamais répétée à chaque retour.
2. **Une ligne courte** : « Nom, fonction » (« Prénom Nom » si la personne est connue du public) ; au besoin deux lignes, nom en haut, fonction en bas.
3. **Construite dans AE**, identité de la famille, entrée animée, texte éditable (jamais un gabarit Premiere).
4. **Durée :** formule du §5.3, entre l'entrée et la sortie.
5. **Placement :** jamais sur le visage ni dans la zone d'interface (`formats-courts-verticaux.md` §6) ; du côté opposé au visage ; déplacé s'il cache une main, un produit ou un document.
6. **Orthographe** vérifiée sur la source primaire (skill §8). **Accord** de la personne : jamais supposé ; droit à l'image et typographie : `conformite-droits-accessibilite.md`.
7. **Cas particuliers :** premier plan de moins de 2 s : attendre un plan plus long ; premiers plans tous très serrés : titre flottant. Repères d'un guide de style vidéo de l'université de Californie à Davis (tiers inférieur à la première prise de parole, nom puis fonction) [X : pratique d'usage, pas une norme de diffusion].
8. **Source en archive ou en extrait :** pas d'identification de personne, mais un crédit court (§11.4).

**Familles :** S, P (invité, expert), F, T, H avec interview ; D : non.

### 11.4 Crédits

Raymond crédite dans le générique de fin [T, 3:09], Perell publie un « source dock » [T, 31:25]. **Le skill exclut un générique de fin pour Story** (fin sur le regard, fondu au noir, accord qui s'éteint). Donc :
1. crédit à l'écran pendant l'extrait ou le document, une ligne courte (« Source : auteur, titre, année »), durée selon §5.3 ; si l'extrait est plus court que la lecture, prolonger le crédit sur le plan suivant ;
2. liste complète dans la description YouTube (auteur, titre, URL, licence) ;
3. registre `Suivi/licences.csv` (§12) ;
4. pas de générique de fin sans demande.

---

## 12. Sources, licences, extraits tiers (repères, pas conseil juridique)

**Avertissement.** Rien de ce qui suit n'a été relu sur Légifrance ni sur une décision : à faire valider par un juriste avant d'en faire une règle. Droit à l'image, mentions commerciales, photosensibilité et typographie à l'écran : `conformite-droits-accessibilite.md`.

### 12.1 Registre unique

Tout élément externe (image, vidéo, son, musique, police, extrait) va dans **`Suivi/licences.csv`** (colonne `type`), structure fixée par `organisation-livraison-qc.md` ; les faits vérifiés dans `Suivi/verifications.md` (skill §8) ; `LICENCES-SFX.md` reste celui de la banque de dégustation. Pour une archive ou un extrait, renseigner au minimum : auteur, titre, année, URL, licence ou statut, date de consultation, fichier local, résolution, minute dans la vidéo, crédit à l'écran, statut de droit, validé par. Statuts : `libre (licence lue)`, `licence obtenue`, `citation (à valider)`, `à demander`. Jamais « libre » sans licence lue ; un fichier sur le disque n'est pas une licence.

### 12.2 Repères français, à faire valider

- **Courte citation** (CPI, art. L122-5, 3° a) **[X]** : en indiquant clairement le nom de l'auteur et la source, les « analyses et courtes citations » sont permises quand le caractère critique, polémique, pédagogique, scientifique ou d'information de l'œuvre qui les incorpore les justifie [X : Guichet du Savoir, citant Légifrance]. Aucune durée dans le texte ; le caractère « court » s'apprécie par rapport à l'œuvre citée comme à l'œuvre citante [X : Livres Hebdo]. L'arrêt de la Cour de cassation du 8 février 2023 (n° 21-23.976) [X : Dalloz Actualité] n'a pas été relu : **ne pas le citer comme autorité**.
- **Durée de protection [K] :** en règle générale la vie de l'auteur plus soixante-dix ans ; droit moral perpétuel ; règle exacte à vérifier pour photographies et œuvres anonymes. **Ne pas transposer la règle américaine de Raymond** (1923 et avant [T, 1:38]).
- **INA :** service de licence commerciale pour professionnels (Inamédiapro), distinct du site public [X : étude Ithaka de 2009, ancienne] ; aucun tarif actuel trouvé. **Signaler à Cabezer un service payant** avant toute commande ; la citation ne suffit pas pour un extrait long.
- **Wikimedia Commons :** créditer le créateur du champ auteur, lier la licence, indiquer les modifications ; certaines images portent des restrictions de droit à l'image [X : page « Reusing content outside Wikimedia »].
- **Plateformes :** revendication ou démonétisation possibles ; jamais promettre l'absence de revendication (skill §11). YouTube admet un litige fondé sur une exception au droit d'auteur mais recommande de ne contester qu'avec des droits certains [X].

---

## 13. Familles en bref

Recommandations de départ ; le brief de Cabezer prime. Chaque technique donne ses familles dans sa section.
- **S (Story) :** partition à une ligne par idée (§2), promesse dans l'intro face caméra (§3), transcription pour repérer seulement (§4.2), désignation et collage en AE (§5.1, §6.5), mouvement sur photo pour désigner ou présenter (§6.4), nappe basse et silences (§8.1), chapitres du skill (§11.1) ; ni fond flou ni générique de fin.
- **P (films/séries) :** extraits commentés et A/B de version (§10), mouvement sur photo pour désigner (§6.4), fond flou avec accord, pas de passé/présent.
- **F, T, H :** question et promesse (§2, §3), désignation (§5.1), carte (§7.1), fond flou (§6.3) ; mouvement sur photo rare.
- **D :** aucune technique de cette fiche (coupes franches, pas d'archives ni d'extrait tiers).
- **Jamais sans accord de Cabezer :** plugin de carte payant (§7.2), INA ou tout service payant (§12.2). **Jamais :** faux raccord de mouvement (§9).

---

## 14. Erreurs de débutant → réflexes de pro

| Erreur | Réflexe de pro |
|---|---|
| Une image par mot pour « faire vivre » | Un support par idée (skill §6) |
| Photo glissée sur « Nouvelle séquence » | Séquence du projet, mise à l'échelle ensuite (§6.2) |
| Photo importée en « Mettre à l'échelle » puis zoomée : image granuleuse | « Définir à la taille du cadre » pour toute photo qui bougera (§6.2) |
| Ken Burns sur toutes les photos, ou mouvement sur un document à lire | Mouvement seulement pour désigner ou présenter, avec pauses ; document à lire exploré dans AE (§6.4, §5.2) |
| Texte qui passe trop vite, ou formule appliquée au mot à mot de dégustation | Formule du §5.3 dans son périmètre, vérifiée sur le MP4 son coupé |
| Promesse repoussée après 30 s, ou répondue tout de suite | Confirmer avant 30 s, rappeler en question, répondre à la fin (§3) |
| Archive colorisée ou « améliorée » par IA, ou musique sur une archive qui parle | Aucun traitement génératif sans demande explicite (§6.6) ; musique basse ou absente (§8.1) |
| −6 à −8 dB d'un tutoriel pris pour le niveau de la musique | C'est un creux d'EQ ; niveau de nappe : audio §5.5 (§8.2) |
| Coupe sur un geste de deux sources | Raccord honnête, ou rapprochement annoncé à la voix (§9) |
| Extrait long sans commentaire ; crédit pris pour une autorisation | Durée minimale, commentaire, source affichée, Content ID signalé (§10.4) |
| Interviewé sans nom, ou nom répété à chaque retour | Identification unique à la première apparition (§11.3) |
| « Libre de droits » non vérifié | Lire la licence, la consigner (§12.1) |

---

## 15. Liste de contrôle

À relire point par point (skill §14).
- [ ] Question centrale écrite ; sujet et promesse prononcés avant la 30e seconde (dans l'intro face caméra en Story) ; enjeu rappelé en question dans la première minute ; scènes reliées par « donc » ou « mais ».
- [ ] Une ligne de partition par idée, un support par idée, aucun B-roll qui répète une animation ; désignations, collages et cartes faits dans AE, une seule désignation à la fois.
- [ ] Textes à l'écran conformes au §5.3 ; preuve 3 s au moins ; image sans texte 2 s au moins.
- [ ] Photos en « Définir à la taille du cadre » si elles bougent ; mouvement sur image fixe : désigne ou présente, temps fixe avant et après, courbe douce, aucun texte à lire dessous ; rien de pixellisé à 100 % d'aperçu.
- [ ] Archives lues (`ffprobe`, `idet`), sans étirement ni peigne ; aucune image générée ni restaurée par IA sans demande explicite consignée.
- [ ] Données visibles et personnes identifiables traitées selon `conformite-droits-accessibilite.md`.
- [ ] Ambiance d'origine sous les archives ; musique basse ou absente sous une source qui parle ; voix mesurée ; écoute faite par Cabezer ou signalée comme non faite.
- [ ] Chaque extrait : commentaire proche, mention (titre, auteur, source), ligne `citation (à valider)`, risque Content ID signalé.
- [ ] Chaque personne qui parle longuement est identifiée une fois (ou la décision contraire est consignée), orthographe vérifiée.
- [ ] `Suivi/licences.csv` à jour, aucun « libre » sans licence lue ; services payants signalés avant achat.
- [ ] Crédits à l'écran et en description ; pas de générique de fin non demandé ; fin Story : regard, fondu au noir, accord qui s'éteint.

---

## 16. Décisions à demander à Cabezer et points à vérifier sur sa version

> **Toutes ces questions ont reçu une réponse de Cabezer le 12/10/2026** : voir `../decisions-en-attente.md`, qui prime sur les défauts ci-dessous.

**Décisions** (poser la question la première fois, noter la réponse dans `Suivi/decisions.md` ; en attendant, appliquer le défaut).

| # | Question | Défaut en attendant |
|---|---|---|
| 1 | Photo ou archive isolée en Story : fond noir, fond flou ou traitement de la future identité ? (v15 supprimée le 12/10/2026) | Fond flou du même plan, en attendant la nouvelle identité Story |
| 2 | Archive en 4:3 : bandes, fond ou recadrage ? | Bandes sur le fond de l'identité ; jamais d'étirement |
| 3 | Extrait sonore étranger dans une vidéo française : sous-titres en français ? (le skill règle les vidéos tournées à l'étranger par Cabezer, pas les archives insérées) | Sous-titres français relus, 2 lignes, 24 caractères par ligne en 9:16, 42 en 16:9 |
| 4 | Flux optique, changement de cadence calculé ou interpolation sur archive | Non utilisés (question commune avec `premiere-pro-avance.md`) |
| 5 | INA ou tout service de licences payant | Aucun achat ; signaler nom et prix avant commande |
| 6 | Moment visuel sans preuve avant un chapitre (« soul moment » de Perell) | Non appliqué ; règle du skill |
| 7 | Identification d'une personne à sa première apparition (§11.3) | Appliquée quand la voix ne donne pas nom et fonction ; à valider sur un extrait |
| 8 | Respirations conservées aux moments d'émotion de P | Règle du skill inchangée (question commune avec `fondamentaux-montage-narratif.md`) |

**À vérifier sur sa version** (à consigner dans `Suivi/environnement-verifie.md`) : filtre par locuteur et points d'entrée automatiques (`premiere-pro-avance.md` §5) ; « Mise à l'échelle par défaut des médias », « Interpréter le métrage », « Interpolation temporelle », « Flou gaussien » ; AE : « Rastérisation continue », « Créer des formes à partir d'un calque vectoriel », « Tracés rognés », import d'un .svg ; Illustrator installé ; raccourcis (Y, S, P, T) ; expressions du §7.1 sur une copie.

---

## 17. Sources étudiées

**Transcriptions lues en entier** [T] (sous-titres automatiques de YouTube, non relus) :
- David Perell, « Johnny Harris Reveals How He Writes YouTube Videos » (2025), https://www.youtube.com/watch?v=zq4b96m1AvM : partition, promesse, direction artistique, source dock.
- Johnny Harris, « How I Make My Maps » (sponsorisé Intel), https://www.youtube.com/watch?v=GsojLuJpe_0 : cartes sans plugin et avec GeoLayers ; prix et licences Mapbox non vérifiés.
- Kurzgesagt, « How to Make a Kurzgesagt Video in 1200 Hours » (2020), https://www.youtube.com/watch?v=uFk0mgljtns : production d'équipe, ordre de grandeur.
- Vaun Raymond, « How to Use Still Images in Documentary & Non Fiction Films », https://www.youtube.com/watch?v=wTr6df0H5Po : images fixes, Premiere seulement.
- Thomas Flight, « Video Essay Voiceover Guide - My Workflow », https://www.youtube.com/watch?v=dLoAw_mveFs : voix off, EQ de la musique ; choix d'un auteur.
- Nerdwriter1, « Succession: Say What You Mean » (2019), https://www.youtube.com/watch?v=REhlyvtiIhQ : structure d'un essai.
- Nerdwriter1, « See With Your Ears: Spielberg And Sound Design » (2018), https://www.youtube.com/watch?v=kavxsXhzD48 : tension par le son, version alternative.
- Tony Zhou, Every Frame a Painting, « How Does an Editor Think and Feel? », https://www.youtube.com/watch?v=3Q3eITC01Fg : durée et émotion ; Murch, Kahn, Schoonmaker de seconde main.
- Karen Pearlman et Richard James Allen, « Cutting Rhythms » (NBFF 2021), https://www.youtube.com/watch?v=RqI4kD8RQng : film de danse ; transfert partiel.
- Federico Bolanos, « I Studied 100 YouTube Documentary Channels », https://www.youtube.com/watch?v=35i_DKPW6sc : lentille, structure, clarté, son ; chiffres non vérifiés.

**Fichiers ouverts le 12/10/2026 [Lu]** :
- Natural Earth, LICENSE.md, https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/LICENSE.md : domaine public, usage commercial, crédit facultatif ; conditions complètes du site non ouvertes.
- Matthew Bloch, mapshaper, README, CHANGELOG, LICENSE, https://raw.githubusercontent.com/mbloch/mapshaper/master/README.md : licence MPL 2.0, export SVG, flux Illustrator ; procédure de conversion à tester.
- docsforadobe, After Effects Scripting Guide, https://raw.githubusercontent.com/docsforadobe/After-Effects-Scripting-Guide/master/docs/layer/avlayer.md et `/docs/matchnames/layer/shapelayer.md` : noms d'API (`collapseTransformation`, Trim Paths), sans interface.
- docsforadobe, After Effects Expression Reference, https://raw.githubusercontent.com/docsforadobe/After-Effects-Expression-Reference/master/docs/layer/properties.md : type de retour de `Layer.scale` ; rien sur la multiplication par l'échelle du parent.

**Extraits de résultats de recherche seulement [X]** (pages non ouvertes) :
- Mise à l'échelle des médias : employé Adobe sur community.adobe.com ; Larry Jordan (larryjordan.com) ; Mixing Light, « Why You Need to Master the Frame Size Options in Premiere Pro CC ».
- L122-5 3° a du CPI : Guichet du Savoir (https://www.guichetdusavoir.org/question/voir/140595), Livres Hebdo ; Cass. 1re civ., 8 février 2023, n° 21-23.976 : Dalloz Actualité (https://www.dalloz-actualite.fr/document/civ-1re-8-fevr-2023-fs-b-n-21-23976).
- YouTube, « Dispute a Content ID claim » (https://support.google.com/youtube/answer/2797454) et page sur le fair use ; Wikimedia Commons, « Reusing content outside Wikimedia » (https://commons.wikimedia.org/wiki/Commons:Reusing_content_outside_Wikimedia).
- UC Davis Health, « Video Style Standards » (https://health.ucdavis.edu/graphicstandards/video/index.html) ; Ithaka S+R, « L'Institut national de l'audiovisuel 2009 » (https://sr.ithaka.org/publications/linstitut-national-de-laudiovisuel-2009/).
- Pages d'aide Adobe (édition par le texte), Ron Delsener Presents ; un résumé tiers sur LEMMiNO (usage d'IA) n'est pas retenu.

**Non obtenues :** Joe Walker, Joss Fong, Walter Murch, Max Valarezo, Evan Puschak, Thomas Flight (*1917*), documentation Adobe, Légifrance, références Micode et Amistory. Aucun monteur de documentaire primé n'a été lu : les règles reposent sur des créateurs de vidéo, une monteuse de film de danse et des essayistes.

**Vérifications du 12/10/2026 :** `ffprobe` (largeur et hauteur), `ffmpeg` (`idet`, détection de plans) et calcul de durée de lecture exécutés sur fichiers synthétiques ; expressions After Effects non exécutées.
