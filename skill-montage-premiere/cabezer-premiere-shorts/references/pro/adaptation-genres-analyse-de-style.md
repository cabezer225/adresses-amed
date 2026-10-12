# S'adapter à tout montage : analyse de style et grammaires de genres

Fiche de référence du skill `cabezer-premiere-shorts` (publiée dans `references/pro/`), rédigée le 12/10/2026, harmonisée (passe 2) avec le skill v3 et `../decisions-harmonisation.md`. Elle apprend à fixer un brief pour un montage hors familles, à analyser une référence, à en tirer une grammaire (rythme, ordre des plans, accroche, son) et à l'appliquer sans copier ni changer l'identité de Cabezer. Elle ne remplace aucune règle du skill.

Codes de famille : **D** dégustation, **F** food long, **S** Story, **P** films/séries (PRISME), **T** tech, **H** hors familles.

## Quand lire cette fiche

- Cabezer demande un montage « dans le style de » : bande-annonce, publicité, clip, vlog de voyage, aftermovie, interview, gag, court métrage.
- Il donne une vidéo de référence à imiter ou à comprendre.
- Le montage ne rentre dans aucune des familles D, F, S, P, T (famille **H**) : lire d'abord la section 3.
- Avant l'étude de références récentes demandée par le skill (§8, « Inspiration actuelle »).
- Une coupe ou un rythme « ne marche pas » et il faut comparer à une référence avec des chiffres.

Ne pas la lire pour l'identité visuelle (skill §5.1, §6), les sous-titres (§9), l'audio technique (§11) ou l'export (§13). Fiches liées : `fondamentaux-montage-narratif.md` (logique de coupe, brief narratif), `premiere-pro-avance.md`, `after-effects-motion-design.md`, `formats-courts-verticaux.md` (zones sûres, hook), `organisation-livraison-qc.md` (scripts, commandes, arborescence, registres), `audio-dialogue-sound-design-mixage.md`, `pilotage-environnement-reprise.md` (raccourcis lus, versions), `conformite-droits-accessibilite.md` (droits, mentions commerciales, photosensibilité), `documentaire-essai-video-archives.md` (cartes, temps de lecture, extraits).

**Hiérarchie (skill §1) :** brief de Cabezer → règles du skill → fiches → tutoriels. Une technique citée ici vient d'un tutoriel ou d'une analyse : jamais une règle universelle. Chaque technique dit quand l'utiliser, quand l'éviter et pour quelles familles.

## Sommaire

1. Statut de vérification et conventions
2. Grammaire et identité : ce qu'on reprend, ce qu'on ne reprend pas
3. Brief de démarrage d'un montage hors familles (H)
4. Analyser une référence : protocole
5. Choisir la grammaire selon l'intention
6. Grammaires par genre (6.1 à 6.9)
7. Tableau genre × famille Cabezer
8. Contrôler que l'adaptation est réussie
9. Versions, outils IA, plugins et coûts
10. Erreurs de débutant → réflexes de pro
11. Liste de contrôle
12. Décisions à demander à Cabezer
13. Sources étudiées

---

## 1. Statut de vérification et conventions

Les notes de recherche de départ étaient des données non fiables ; chaque point a été recoupé, et ce qui ne se vérifie pas est retiré ou marqué.

| Marque | Sens |
|---|---|
| **[Testé]** | Exécuté : ffmpeg 6.1.1, PySceneDetect 0.7.1, Python 3, vidéo synthétique, Linux. En passe 2, seules les échelles de `select` et `scdet` ont été rejouées. À refaire sur le Mac de Cabezer. |
| **[Lu]** | Transcription intégrale lue (section 13). |
| **[Code source]** | Lu dans le code de PySceneDetect 0.7.1 (passe 1). |
| **[Extrait]** | Vu dans un extrait de résultat de recherche, page non ouverte : indice, pas preuve. |
| **[Un praticien]** | Une seule source : technique à essayer, pas un principe. |
| **À vérifier / libellé à confirmer** | Menu, raccourci ou fonction de Premiere/After Effects (AE) non lu à l'écran ni dans une documentation officielle. |
| **Heuristique** | Convention de métier, non mesurée. |

**Conventions d'interface (`../decisions-harmonisation.md` B) :**
- Nom français puis anglais entre parenthèses ; libellé non lu = « libellé à confirmer ».
- **Aucun raccourci n'est utilisé tant qu'il n'a pas été lu** dans Premiere/AE > Raccourcis clavier (Keyboard Shortcuts) sur la machine de Cabezer ; sinon passer par le menu. Les raccourcis cités ici sont des défauts courants **à confirmer** ; une fois lus, ils vont dans `Suivi/environnement-verifie.md` (`pilotage-environnement-reprise.md`).
- Aucune version, date de sortie ou statut de fonction n'est affirmé sans source officielle lue : « selon <source>, à vérifier sur sa version ».
- Claude n'entend pas : il contrôle par mesures, transcription et forme d'onde ; l'écoute revient à Cabezer. Ne jamais écrire « écouté » pour une mesure.

**Limites :** documentations Adobe, ffmpeg.org, scenedetect.com et TikTok inaccessibles ; valeurs d'outils tirées d'exécutions locales et du code. Les vidéos non lues (section 13) ne fondent aucune règle.

---

## 2. Grammaire et identité : ce qu'on reprend, ce qu'on ne reprend pas

**Règle de fond :** la grammaire vient de la référence, l'identité vient de Cabezer. Le skill l'impose : « ne pas recréer une direction à chaque vidéo ni transposer celle d'une autre famille » (§6) et « ne pas copier un montage ni récupérer ses sons » (§8).

| On reprend (grammaire) | On ne reprend pas (identité et propriété) |
|---|---|
| Durées de plans, courbe d'accélération, ordre des plans | Plans, musiques, voix, sons de la référence |
| Forme de l'accroche (question, boucle ouverte, contexte) | Logos, marques, typographies sous licence |
| Densité de texte et moments où il apparaît | Presets, templates identiques, signature de l'auteur |
| Logique émotionnelle (quand on tient, quand on coupe) | Couleurs, polices et habillage de l'auteur |
| Place du son dans la coupe (SFX sur l'image, silences) | Toute image ou animation générée par IA |

**Pourquoi :** une grammaire est un savoir-faire réutilisable ; une identité rend la chaîne reconnaissable. Les mélanger fait un pastiche.

**Application aux familles :**
- D, F, S, P, T : l'identité validée de la famille reste inchangée ; seule la grammaire est empruntée, si elle ne contredit aucune règle de la famille (pas de musique de fond en dégustation).
- **Le barème du skill §5.2 prime sur toute grammaire de genre** (hook et rétention des dégustations). Une grammaire n'apporte que des idées de hook (un seul axe, boucle ouverte, écart de curiosité), retenues si le barème les valide (`formats-courts-verticaux.md` §1.2).
- H : le skill dit « proposer un court extrait représentatif et le faire valider avant de décliner ». Ne pas attribuer arbitrairement couleurs ou polices définitives.

**Animations :** tout élément graphique créé (texte, forme, carte, sous-titre animé, transition graphique, flash ou glitch graphique) est construit dans After Effects en calques natifs modifiables (skill §1, §16). Une référence faite avec des packs ou de l'IA se reconstruit avec des effets natifs d'AE, ou on y renonce. Punch-in sec, speed ramp et recadrage d'un plan filmé sont des traitements de plan, faits dans Premiere.

---

## 3. Brief de démarrage d'un montage hors familles (H)

**Quand l'utiliser :** tout montage H et tout montage « dans le style de ». **Quand l'éviter :** retouche ponctuelle d'un montage déjà briefé ; pour D, F, S, P, T le brief est cadré par `fondamentaux-montage-narratif.md` §3.1. **Familles :** H ; les autres réutilisent les champs 9 et 13 à 16 quand une référence de style est en jeu.

Aucun montage ne commence sans brief écrit dans `Suivi/brief.md`. Les douze champs et la méthode (Claude remplit à partir du dossier, ne pose de question que sur les champs bloquants) sont définis dans **skill §3, étape 0** ; en cas de différence de libellé, le skill prime. Le brief fait foi pour le contrôle final (`organisation-livraison-qc.md` §6.5).

**Modèle à copier dans `Suivi/brief.md` :**

```
BRIEF H — <Sujet> — <date> — état : brouillon | validé par Cabezer le ___
 1. FAMILLE : hors famille (H). Genre visé (section 6) : ___
    Intention en une ligne : le spectateur doit ressentir / comprendre ___
 2. PLATEFORMES ET RATIOS : ___ (9:16, 16:9, 1:1)
    Texte clé : boîte de test de formats-courts-verticaux.md §6.2
 3. DURÉE CIBLE : ___ s
 4. PROMESSE : « le spectateur a cliqué pour voir ___ »
    Sujet et promesse confirmés avant la 30e seconde.
 5. HOOK : ___ (écrit en dernier, une fois la structure stable)
 6. LANGUE DES SOUS-TITRES : ___ (tourné à l'étranger : à demander ; défaut anglais)
 7. MUSIQUE ET AMBIANCES : ___ (source, licence ; vitesse d'origine du morceau)
 8. MATÉRIEL ET PROFIL COULEUR DES RUSHS : ___ (lus avec ffprobe, pas supposés)
 9. RÉFÉRENCES DE STYLE : 3 liens ___
    Accord de téléchargement : oui | non (nom, source, taille demandés)
10. CONTRAINTES LÉGALES : partenariat | personnes filmées | musique |
    extraits tiers (conformite-droits-accessibilite.md)
11. AUTONOMIE : valider le dérush avant l'habillage ? oui | non
    (jamais de publication sans accord explicite)
12. LIVRABLES ET ÉCHÉANCE : MP4 ___, SRT, séquences, .aep ; date ___
Compléments propres à H
13. IDENTITÉ : proposition provisoire (couleurs, police gratuite), à valider
    sur l'extrait de 15 à 30 s (hook, passage calme, passage rapide).
14. À NE PAS REPRENDRE de la référence : ___
15. ANIMATIONS GRAPHIQUES PRÉVUES (toutes dans After Effects) : ___
16. CRITÈRE DE RÉUSSITE MESURABLE : ___ (ex. coupes/min du hook proche
    de la référence, écart expliqué)
```

**Procédure :**
1. Lire le dossier (rushs, notes, messages) et remplir tout ce qui s'y trouve ; marquer le reste « à demander ».
2. **Champs bloquants pour H :** genre ou intention, promesse, plateformes et durée, contraintes légales si partenariat ou personnes filmées. Les poser **en une seule fois**, avec un défaut proposé pour chacun.
3. Pour les autres champs, appliquer le mode autonome (décisions D16) : langue à l'étranger = anglais ; téléchargement = jamais sans accord (s'en passer) ; validations consignées « en attente » dans `Suivi/decisions.md`.
4. Faire valider le brief et dater la validation. Tout changement de promesse ou de plateforme est noté dans `Suivi/decisions.md`.

**Critère de réussite :** Claude, après une reprise de session, refait les mêmes choix de genre, de durée et de livrables en lisant uniquement le brief.

---

## 4. Analyser une référence : protocole

**Quand l'utiliser :** H ou demande « dans le style de » ; F, P, T pour un passage monté sur musique ou un teaser ; mesure d'une nouvelle référence de S. **Quand l'éviter :** D (le barème du skill §5.2 et la DA v2 suffisent) ; retouche sans comparaison à faire. **Familles :** H, F, P, T ; S pour mesurer seulement (6.9).

### 4.1 Cadre, accord et rangement

1. **Demander l'accord avant de télécharger** une vidéo de référence, avec nom, source et taille : le skill l'impose pour toute vidéo à télécharger (§6 « Ses propres images », §8), références d'analyse comprises. Sans accord : visionner, relever à la main, ou travailler sur les captures que Cabezer fournit.
2. Ranger le fichier **hors du projet**, jamais dans une séquence de Cabezer. Mesures et fiche de style vont dans `Controles/Analyses/` ; accord, taille et suppression sont consignés dans `Suivi/journal.md`. Suppression du fichier : question 1 de la section 12.
3. Noter titre, chaîne, date de publication, URL, durée exacte, date de consultation.
4. Mesurer **au moins 60 secondes**, idéalement 2 minutes. En dessous de 30 s, la durée moyenne d'un plan n'a pas de sens.
5. Analyser **trois références** du même genre avant de conclure : une seule donne un style d'auteur, pas une grammaire de genre.
6. Ne jamais affirmer qu'une tendance est « virale en ce moment » sans données (skill §8) ; consigner les métriques visibles sans en faire une cause.

### 4.2 Ce qu'on mesure

- **ASL** (average shot length, durée moyenne d'un plan) : durée totale / nombre de plans ; ajouter la **médiane**, plus robuste quand un plan très long fausse la moyenne. **Plan** = coupes détectées + 1.
- **Coupes par minute**, globales puis par tranche de 15 s : elles donnent la **courbe** (accélération, plateau, décélération).
- **À la main sur la planche :** taille des plans (% de la durée), mouvement de caméra, texte à l'écran (occurrences par minute, durée d'affichage), SFX par minute, musique (présence, tempo, coupes sur le temps), palette, typographie.

**Pièges de mesure :**
- Un effet (zoom, flash, glitch) n'est pas toujours détecté comme une coupe ; un fondu enchaîné ne l'est presque jamais [Testé]. Contrôler à l'œil les zones à effets.
- Décider une fois pour toutes si un plan long avec transition interne compte pour un ou plusieurs plans, et appliquer la même règle à toutes les références.
- **Ne pas confondre avec les « relances » du skill (§5.2)** : le barème de rétention compte une coupe seulement si elle change de rush ou de cadre ; l'analyse compte toutes les coupes détectées. Ne jamais mettre une note de rétention en face d'un ASL.
- **Durée d'affichage d'un texte :** comparer au temps de lecture de `documentaire-essai-video-archives.md` §5.3. Cette formule vise cartons, textes d'habillage et traductions ; elle ne vise ni les sous-titres mot à mot de D ni les coupes rapides nommées (0,4 à 0,8 s).

### 4.3 Détecter les coupes

**Commandes et scripts : pas de copie ici.** La bibliothèque unique (tableau « usage, commande, seuil ») et le jeu de scripts nommés sont dans `organisation-livraison-qc.md` §6. Pour cette fiche :
- cadence et taille : ligne « conformité technique » (§6.2) ;
- `mesure-plans.py` (paramètres : seuil de scène, fenêtre, sortie CSV) : demander ASL, médiane, plans le plus court et le plus long, coupes par minute **par fenêtre de 15 s**, et garder `plans.csv` dans `Controles/Analyses/` ;
- planche contact : commande de §6.3, une image toutes les 0,5 s pour une référence rapide ;
- attaques sonores et palette : si le jeu ne les contient pas, **les y ajouter** (`attaques-sons.py`, extraction de palette), pas ici.
- lire tout fichier externe (vidéo, XML, SRT, transcription) avec `python3 -I` ; tout script reste « testé sur fichiers générés » tant qu'il n'a pas tourné sur un vrai export de Cabezer (skill §20).

**Valeurs et pièges des détecteurs (seuil de départ `select` : 0,3) :**

| Outil | Quand l'utiliser | Quand l'éviter | Valeurs vérifiées |
|---|---|---|---|
| ffmpeg `select` + variable `scene` | Liste brute reproductible, toutes familles | Fondus (score maximal 0,05 dans le test) | Échelle 0 à 1 [Testé]. Plans très différents : 0,62 à 1,00. Couleurs voisines : **0,36** (seuil 0,4 : ratée ; 0,2 et 0,3 : trouvée). |
| ffmpeg `scdet` | Second avis | Y reprendre un seuil de `select` | Échelle **0 à 100**, défaut 10 [Testé, rejoué]. Même coupe : 0,36 en `select` ≈ 13,96 en `scdet`. |
| PySceneDetect `detect-content` (facultatif) | Recoupement | Montage rapide sans `-m 2` | Seuil par défaut **27.0**, moyenne de variation d'intensité en HSV [Code source]. `-s stats.csv` écrit `content_val`. |
| PySceneDetect `detect-adaptive` | Mouvements de caméra rapides | Plans quasi statiques | `adaptive_threshold` 3.0, `window_width` 2, `min_content_val` 15.0 [Code source]. |

- **Piège majeur :** en ligne de commande, `-m/--min-scene-len` vaut **0,6 s par défaut** [Code source, `--help`]. Une référence plus rapide (clip, aftermovie, TikTok) perd des coupes sans prévenir : passer `-m 2` (2 images), et ne jamais comparer deux montages mesurés avec des réglages différents.
- Les seuils des guides tiers (0,25 à 0,30 pour un montage rapide, 0,35 en général, 0,45 à 0,50 pour des coupes dures) sont des points de départ : lire les scores avant de choisir. Sur la vidéo de test, PySceneDetect a trouvé les 5 coupes vraies **et** une fausse coupe dans un plan très animé : un détecteur seul se trompe dans les deux sens.
- **Méthode :** ffmpeg pour la liste brute, PySceneDetect (installé avec l'accord de Cabezer) pour recouper, puis contrôle de **10 % des coupes au minimum** et de toutes les zones à effets.
- **Dans Premiere :** clic droit sur un clip, puis la détection des changements de plan (Scene Edit Detection ; libellé à confirmer ; `premiere-pro-avance.md` §5.2). Un extrait de formation signale qu'elle peut rater des coupes ou produire des images éclair et de mauvais fondus [Extrait, section 13]. À utiliser pour feuilleter une référence dans une séquence d'analyse, pas pour mesurer. **Dans AE :** même fonction sur un calque (libellé à confirmer). Détection des scènes = aide autorisée, résultat vérifié (skill §16).

### 4.4 Coupes et attaques sonores

**Quand l'utiliser :** montage sur musique ou sur SFX (F, S, P, T, H). **Quand l'éviter :** coupe de voix ; D hors SFX. Question posée à la référence : « coupe-t-elle sur le temps, une image avant, ou pas du tout ? ». Utiliser `attaques-sons.py` (4.3) avec les temps de coupe ; la précision annoncée en passe 1 est d'environ une demi-image sur un son net (clics toutes les 0,5 s) [Testé]. Sur une musique dense, contrôler la forme d'onde de Premiere et demander à Cabezer.

### 4.5 Supports d'analyse

Planches contact, palettes, CSV et fiches de style sont des **supports d'analyse** : jamais importés dans le montage de Cabezer. L'interdiction du skill (§16) vise les images et graphismes de montage fabriqués hors d'AE ; ces fichiers n'en sont pas. Pour une couleur de texte, utiliser la pipette de Premiere sur une image fixe (la compression déforme les couleurs d'une vidéo).

### 4.6 Fiche de style à remplir (une par référence)

```
RÉFÉRENCE : titre, chaîne, date, URL, durée, date de consultation
FAMILLE CIBLE / INTENTION
RYTHME : plans | ASL | médiane | coupes/min | par tranche de 15 s | courbe
PLANS : large/moyen/serré % | mouvement % | coupes franches / fondus
SON : musique (présence %, coupes sur le temps) | voix | SFX par minute
TEXTE : occurrences par minute | durée d'affichage | zone de sécurité
IMAGE : palette | contraste, saturation, dominante
GRAMMAIRE OBSERVÉE : 3 à 6 règles courtes
NE PAS REPRENDRE : plans, sons, voix, logos, polices, signature
ADAPTATION CABEZER : équivalent | contraintes du skill | à faire valider
ÉTAT : mesuré | vu | écouté par Cabezer | validé par Cabezer
```
**Réussite :** la fiche tient en une page et chaque chiffre dit de quel outil et de quel seuil il vient. Ranger dans `Controles/Analyses/`.

---

## 5. Choisir la grammaire selon l'intention

Écrire d'abord **en une ligne** ce que le spectateur doit ressentir ou comprendre (champ 1 du brief). Sans cette ligne, ne pas choisir de grammaire.

| Intention | Grammaire la plus proche | Section |
|---|---|---|
| Donner envie de voir sans tout dévoiler | Bande-annonce « setup » ou « ambiance » | 6.1 |
| Vendre ou promouvoir en 15 à 30 s | Publicité / UGC | 6.2 |
| Accompagner une musique | Clip, montage sur temps | 6.3 |
| Montrer un lieu et un trajet | Vlog voyage | 6.4 |
| Faire témoigner, faire parler | Interview, extrait de podcast | 6.5 |
| Faire rire par le cadre ou le timing | Comédie visuelle | 6.6 |
| Célébrer un événement | Aftermovie, hype | 6.7 |
| Raconter une histoire courte | Court métrage | 6.8 |
| Expliquer un fait de société | Documentaire (famille Story) | 6.9 |

Règle d'arbitrage commune : l'émotion voulue passe avant le rythme, le rythme avant le raccord parfait (Murch, règle des six : émotion, histoire, rythme, regard, axe, espace ; listée dans deux transcriptions lues, citée par une troisième). Les pondérations en pourcentage souvent citées ne sont pas reprises. Détail : `fondamentaux-montage-narratif.md` §2.

---

## 6. Grammaires par genre

### 6.1 Bande-annonce et teaser

**Couverture : une vidéo lue en entier (Derek Lieu, modèle A24). Le reste est de l'expérience de métier non sourcée.**

**Principes [Lu] :**
- Derek Lieu classe les bandes-annonces selon ce que le spectateur sait en sortant : **chronologie**, **prémisse (setup)**, **personnages**, **ambiance et ton** (sa typologie personnelle, « probablement insuffisante et réductrice »). Sur 50 bandes-annonces A24 : 5 proches d'une chronologie, 24 setup, 11 personnages, environ 10 ambiance.
- Plus la chronologie est visible, plus la bande-annonce « spoile » ; un film à l'accroche forte a besoin d'expliquer moins.
- Techniques A24 : dialogue gardé dans sa scène d'origine (pas de réplique fabriquée avec des bribes de scènes différentes) ; voix off minimale ; peu de transitions qui « ferment » une séquence ; **un ou deux** moments musicaux forts ; cartons de titre comme respirations et pour sauter dans le temps ; un seul axe.

**Retiré :** le terme « button » et les durées d'acte (vidéos non lues) ne sont pas sourcés.

**Procédure (Premiere + AE) :**
1. Transcrire le matériau. Marquer chaque réplique et chaque plan avec un marqueur de séquence (raccourci courant M, à confirmer ; sinon menu, libellé à confirmer) nommé par catégorie : prémisse, personnage, ambiance, chronologie.
2. Compter par catégorie ; la dominante est l'axe. Si la chronologie domine, retirer des plans jusqu'à ce que la prémisse domine.
3. Monter en trois blocs : prémisse (peu de mots), montée d'ambiance, final. Voix off limitée à la prémisse.
4. Construire les cartons dans AE (calques natifs), puis les poser dans Premiere comme respirations.
5. Au plus un ou deux moments musicaux forts ; ne pas couper la musique au milieu d'une phrase.

**Extraits tiers (P, S, H) :** extraits officiels et affiches seulement ; durée minimale nécessaire, commentés, source affichée ; un crédit n'est pas une autorisation ; signaler le risque Content ID avant publication (`documentaire-essai-video-archives.md` §10.4, `conformite-droits-accessibilite.md`).

**Quand l'utiliser :** teaser d'un épisode Story, annonce d'une série ou d'un film (P), annonce de saison en F ou T, H. **Quand l'éviter :** dégustation, où le barème (§5.2) exige produit ou bouchée dès la première seconde et un enjeu compris en 3 s : « montrer moins » ne s'y applique pas ; D n'emprunte que l'idée d'un seul axe et de cartons-respirations, après validation par le barème.

**Réussite :** on peut dire en une phrase ce que le spectateur saura en sortant et c'est ce qui était visé.

### 6.2 Publicité et UGC

**Couverture : moyenne pour l'accroche (une vidéo lue, heyDominik) ; faible pour la structure chiffrée (guides de vendeurs, non testés).**

**Principes de l'accroche [Lu, auteur marketing] :**
- Le spectateur défile en pilote automatique jusqu'à ce qu'une image déclenche un « tiens, c'est intéressant ». L'auteur ne chiffre pas ce délai : ne pas inventer de durée.
- Ouvrir une boucle (question), la tenir ; quand elle se ferme, en ouvrir une autre.
- Donner du **contexte** dès la première image : une affirmation sans contexte laisse le spectateur sans raison de rester.
- Cacher ou flouter un élément pour garder une question ouverte (**hors D** : en D, produit ou bouchée visibles dès la première seconde, sans bouchée tronquée).
- **Exclu :** l'auteur génère une première image par IA ; Cabezer interdit les images générées (skill §16).

**Squelette en quatre temps (heuristique) :** accroche, problème, solution (montrer le produit qui résout), appel à l'action. Les durées des guides (0–3 s, 3–10 s, 10–20 s, appel de 3 à 5 s) sont des conventions : ne pas les appliquer sans les comparer à trois références avec la fiche de 4.6.

**Sound design publicitaire :** vidéos de Daniel Schiffer non lues, rien retenu ; observer la synchronisation son/image des références (4.4).

**Zones sûres : une seule boîte.** Le **texte clé** (étiquettes, prix, pop-ups, note, appel au commentaire) respecte la « boîte de test provisoire » de `formats-courts-verticaux.md` §6.2 ; aucune autre valeur n'est définie ici. Les sous-titres de dégustation restent à 72–75 % de la hauteur, avec contrôle sur téléphone qu'ils ne sont pas masqués (question 5, section 12). Contrôle sans publier : captures d'écran des applications fournies par Cabezer (`formats-courts-verticaux.md` §6.3) ; jamais de publication de test sans son accord (skill §1).

**Mentions commerciales :** publicité et partenariat exigent des mentions (`conformite-droits-accessibilite.md`).

**Quand l'utiliser :** H (publicité, partenariat, présentation de produit) ; accroche d'une vidéo F ou T quand Cabezer demande de « travailler le hook ». **Quand l'éviter :** S et P (le ton « vendeur » casse l'identité) ; D, qui a son barème.

**Pièges :** accroche qui résume la suite ; plusieurs appels à l'action ; logo avant la première image utile ; texte sous les boutons de la plateforme.

### 6.3 Clip musical et montage sur musique

**Couverture : forte (deux vidéos lues), mais chacune défend un seul praticien.**

**Technique 1 : la coupe une image avant le temps fort [Lu, Filmmaker IQ — un praticien].**
- L'auteur place la coupe **une image avant** l'attaque lue dans la forme d'onde : l'oreille réagit plus vite que l'œil, et une image d'avance laisse à l'œil le temps de lire le plan quand le son arrive. Il précise que cela vaut aussi pour les coupes sur action et les réactions : « ajoute quelques images de chaque côté et regarde ce qui marche ».
- Une image dure 41,7 ms à 24 i/s, 40 ms à 25 i/s, 33,4 ms à 29,97 i/s, 16,7 ms à 59,94 i/s.
- **Statut :** le défaut du skill est la coupe ou l'accent **sur l'attaque** (swoosh sur son pic). La technique est un **essai A/B** à procédure unique, décrite dans `audio-dialogue-sound-design-mixage.md` §6.2 (−1, 0, +1 image sur un extrait), adopté seulement avec la validation de Cabezer sur plusieurs vidéos (skill §15, §20). Ne pas la présenter comme règle.

**Procédure de l'essai (Premiere) :** zoomer jusqu'à l'image sur l'attaque ; poser la coupe sur l'attaque ; préparer les variantes −1 et +1 avec l'outil d'édition par roulement (Rolling Edit Tool ; raccourci courant N, à confirmer ; ou menu) ; remettre les trois versions à Cabezer, qui juge à l'écoute à volume normal. Une coupe parfaitement sur le temps qui casse le ton est une mauvaise coupe.

**Technique 2 : plans courts, répartis uniformément [Lu, Jay Sia — un praticien].** Plans de 2 à 3 s au maximum, chaque prise utilisée au maximum, plans répartis régulièrement sur le morceau, 3 à 4 prises (jusqu'à 10 ou 15) pour avoir de la matière, pauses remplies par des transitions de mouvement rapide.

**Flux de Jay Sia et flux de Cabezer :** Jay Sia séquence dans Premiere, exporte, puis termine dans AE. **Ce n'est pas le flux de Cabezer** : Premiere reste la timeline maîtresse. Effets et habillage se font dans AE et s'intègrent par « Remplacer par une composition After Effects » (clic droit ; libellé à confirmer ; `premiere-pro-avance.md` §9) : la lecture ralentit, éviter sur des dizaines de clips.

**Effets cités, classés :**
- **Natifs AE (ou très probablement) :** Roto Brush, CC Light Sweep, Posterize Time (8 à 15 i/s dans son exemple), Displacement Map, Optics Compensation, Luma Key (libellés à lire à l'écran), pré-composition, Easy Ease. Raccourcis courants (Cmd+Maj+C, F9) **à confirmer**.
- **Payants (accord de Cabezer avant tout usage) :** Sapphire (Boris FX), Element 3D (Video Copilot), packs de l'auteur (Fast Movement Effects : tarif à vérifier). **Statut non vérifié :** Deep Glow, CRT Emulator, MXM : ne pas installer avant d'avoir signalé le prix (skill §17).
- Reconstruire un effet de style (papier, CRT) avec des effets natifs d'AE, en calques éditables.

**Musique :** un morceau fini garde sa vitesse d'origine ; un ajustement de tempo ne concerne qu'une composition faite de boucles (décision D15). Licence consignée dans `Suivi/licences.csv` (skill §11). **Flashs et glitchs :** vérifier la photosensibilité (`conformite-droits-accessibilite.md`).

**Quand l'utiliser :** passages montés sur musique en F, S, T (générique, transition, bilan), P, H (clip, aftermovie). **Quand l'éviter :** D (pas de musique de fond ; la technique ne vise que les SFX, calés sur l'attaque) ; toute coupe de voix, qui suit le dernier mot entièrement audible (skill §4) ; S quand une respiration porte une émotion (skill §6).

**Pièges :** une coupe sur chaque temps fait un défilé sans intention (varier : sur le temps, après une respiration, plan tenu sur une note longue) ; un effet « papier » ou « CRT » partout perd son effet ; Posterize Time : rendre à la cadence de la séquence et vérifier le scintillement ; repasser en pleine résolution avant tout jugement de netteté, de flou ou de grain (Jay Sia prévisualise en quart de résolution).

### 6.4 Vlog voyage

**Couverture : faible. Aucune vidéo de référence lue ; techniques à tester.** Sam Kolder dit travailler surtout les transitions, le son et le rythme (site officiel, extrait) ; rien d'autre n'est vérifié.

**Techniques à essayer (à valider sur un extrait) :**
- **Mouvement raccordé :** deux plans qui vont dans le même sens, coupés là où le mouvement est le plus fort (cohérent avec la coupe sur l'action [Lu, StudioBinder]) ; transition marquée, sonorisée (skill §7).
- **Masque par objet de premier plan :** un bras, un dos ou un tronc traverse le cadre et sert de cache entre deux plans. Se prépare au tournage ; se construit par masque ou pré-composition dans AE.
- **Interprétation de cadence pour un ralenti propre :** rapport de vitesse = cadence de la séquence / cadence de la source (séquence à 29,97 i/s : source 59,94 i/s → 50 % ; 119,88 i/s → 25 %). Dans Premiere : Clip > Modifier > Interpréter le métrage (Interpret Footage ; libellé à confirmer). Vérifier la cadence réelle du rush avant de promettre un ralenti (skill §7 ; `premiere-pro-avance.md` §3.4 et §7.1).
- **Ralenti sur les inserts seulement**, jamais sur la parole ni sur la bouchée retenue ; un ralenti partout supprime le repère de vitesse. Un speed ramp sans son perd son impact : SFX synchronisé sur la transition marquée.

**Cartes et trajets.** La méthode de carte animée (fond vectoriel, objet nul, zoom, étiquettes) est dans `documentaire-essai-video-archives.md` §7 ; ne pas la dupliquer. Pour un trajet :
1. **Fond de carte :** préférer Natural Earth (domaine public selon le dépôt, même fiche §7.1). Pour des données OpenStreetMap, le crédit demandé est « © OpenStreetMap contributors », avec la licence ODbL rendue claire et un lien vers openstreetmap.org/copyright [Extrait : guide d'attribution de l'OSMF]. Consigner source, licence et capture dans `Suivi/licences.csv`.
2. **Tracé :** outil Plume sur un calque de forme, puis Trim Paths animé sur **Fin (End)** de 0 à 100 % avec une courbe douce. Libellé français à confirmer : « Réduire les tracés » dans un fil de la communauté Adobe [Extrait], « Tracés rognés » dans `after-effects-motion-design.md` §8.1.
3. **Repère qui suit le trajet :** copier le tracé, le coller sur la Position du repère, activer l'orientation automatique du calque (libellé à confirmer). Vitesse constante permise pour un défilement continu, sinon courbe douce (décision D1).
4. Placer la carte entre deux lieux, pas à chaque déplacement ; respecter le temps de lecture (`documentaire-essai-video-archives.md` §5.3).

**Quand l'utiliser :** F tourné à l'étranger, H (vlog). **D tourné à l'étranger :** couleurs du pays et sous-titres en langue locale ou anglais (à demander) ; changements de lieu par whip de 4 à 6 images (skill §5.1), sans carte animée sauf demande. **Quand l'éviter :** S (images réelles et documents explorés d'abord) ; P ; carte qui ne sert pas à comprendre.

**Pièges :** même transition à chaque plan ; trop de ralentis ; carte décorative.

### 6.5 Interview et extraits de podcast

**Couverture : moyenne pour les techniques de coupe (StudioBinder lu), faible pour les interviews documentaires et le choix des moments d'un podcast.**

**Techniques de coupe [Lu, StudioBinder] :**
- **Raccord de regard (eyeline match) :** couper vers l'objet que regarde la personne.
- **Champ-contrechamp (shot-reverse-shot) :** alterner deux personnes sous des angles proches.
- **Insert :** gros plan d'un détail.
- **Coupes en J et en L :** le son du plan suivant démarre avant son image (J) ; celui du plan précédent continue sur l'image suivante (L) (`fondamentaux-montage-narratif.md` §6). Permises si elles ne mordent pas une attaque de mot ; **jamais sur la bouchée ou la réaction en dégustation** (D4).
- **Coupe sur l'action et sur l'impact :** couper au milieu du mouvement.

**Dérush :** le montage par le texte repère et pré-découpe (aide autorisée, relecture obligatoire) ; chaque coupe est recalée à la forme d'onde et à l'énergie du son, jamais aux temps de transcription (`premiere-pro-avance.md` §5.1). Retirer un faux départ pour garder ce que la personne voulait dire est permis ; jamais un collage qui crée une affirmation qu'elle n'a pas faite (D7).

**Masquer un jump cut** (`premiere-pro-avance.md` §5.4) : coupe franche assumée ou punch-in sec (D) → plan de coupe qui apporte quelque chose → second angle synchronisé → animation seulement si prévue. Pas de Morph Cut par défaut.

**Guides tiers (non vérifiés) :** cacher une hésitation par un plan de coupe ; voix de l'interviewé sur du B-roll. La durée de 10 s par plan de B-roll d'un guide n'est pas sourcée : durées du skill (§6).

**Multicam :** séquence source multicaméra (Create Multi-Camera Source Sequence ; libellé à confirmer), synchronisation par forme d'onde, un seul micro pour la voix (skill §12 ; `premiere-pro-avance.md` §6.1).

**Moments d'un podcast : aucune source lue.** Retenir les passages qui portent une émotion ou une information (critères 1 et 2 de Murch), compréhensibles sans le reste, avec chute ou verdict : c'est la règle du skill pour les Shorts tirés d'une vidéo longue (§12, « passages autonomes »), à valider avec Cabezer.

**Quand l'utiliser :** S (témoignages, avis d'experts), P (analyse), T (explication), F, H. **Quand l'éviter :** D, où la voix reste collée aux coupes franches (seul décalage utile : le B-roll sous la voix, skill §5). Identification des intervenants à l'écran : `conformite-droits-accessibilite.md`.

**Pièges :** changement d'angle au milieu d'un mot ; jump cut sans plan de coupe ni punch-in ; sous-titres sur le visage ; décalage J/L qui fait entendre un bout de phrase supprimée.

### 6.6 Comédie

**Couverture : forte pour la mise en cadre (Every Frame a Painting, deux vidéos lues) ; la coupe au noir n'a aucune source.**

**Neuf techniques de cadre et de son [Lu, Edgar Wright par Tony Zhou] :** entrées et sorties du cadre drôles ; aller-retour ; raccords de transition correspondants ; effet sonore parfaitement calé ; action synchronisée sur la musique ; éclairages dramatiques ; « fence gags » (terme non défini) ; fusillades imaginaires. Principe : « le cadre est un terrain de jeu ». Une coupe brusque, musique baissée et effets montés, rend un changement de lieu drôle.

**Timing [Lu] :**
- Thelma Schoonmaker : tenir un plan « un tout petit peu trop longtemps » puis couper, si c'est justifié ; la gêne produit le rire.
- Hitchcock sur le suspense (Film Riot) : le même dialogue devient tendu si le spectateur sait qu'une bombe est sous la table ; le montage choisit le moment où l'on donne l'information. Cela sert aussi la comédie (retarder la révélation du gag).
- La durée d'un plan porte l'émotion (Every Frame a Painting) ; les chiffres annoncés (30 images contre 30 secondes) ne sont pas repris. Gags d'action (Jackie Chan) : `fondamentaux-montage-narratif.md` §12.

**Procédure Premiere :**
1. Poser le SFX du gag **sur son attaque** (défaut du skill). Pour tester un décalage, utiliser l'essai A/B unique de `audio-dialogue-sound-design-mixage.md` §6.2 ; Cabezer juge à l'écoute.
2. Gag de cadre : caler l'entrée dans le cadre sur le plan de réaction, pas sur le suivant.
3. Gag de fin de plan : couper une image après la dernière action et préparer la variante à deux images ; Cabezer choisit.

**Coupe au noir : aucune source.** Pas de règle. Si Cabezer la demande, monter deux versions (avec et sans noir de 3 à 6 images) sur un extrait et les lui faire comparer.

**Quand l'utiliser :** D (la « touche mème » du skill passe par des SFX de la liste fermée bien placés et un punch-in sec, sans mèmes vocaux ni boom) ; F (moments drôles) ; H sur brief. **Quand l'éviter :** S et P sérieux, sauf demande : une coupe pour le gag qui casse le ton viole le critère 1 de Murch.

**Pièges :** trop de gags (le rythme devient un tic) ; SFX mal calé ; SFX synthétisé ou générique (skill §11).

### 6.7 Aftermovie, hype et sport

**Couverture : très faible. Aucune vidéo du genre n'a été lue.**

**Ce que les sources lues permettent de reprendre :**
- **Eye trace :** garder le point d'intérêt de l'action au même endroit du cadre d'un plan à l'autre pour que des plans de moins d'une seconde restent lisibles (chef opérateur de *Mad Max: Fury Road* dans la vidéo de StudioBinder ; Film Riot cite le même exemple) [Lu].
- **Coupe sur l'impact** pour donner de la force à un coup ou un choc [Lu, StudioBinder]. Les plans courts de Jay Sia (6.3) sont ceux d'un clip, pas d'un aftermovie.

**Structure d'un aftermovie : non sourcée.** Ne pas inventer de durées. Analyser trois aftermovies validés par Cabezer (section 4), puis proposer un plan de montage et un extrait à faire valider. Flashs rapides : photosensibilité ; personnes filmées lors d'un événement : droit à l'image (`conformite-droits-accessibilite.md`).

**Quand l'utiliser :** événement filmé en H ; compilation de moments forts. **Quand l'éviter :** D (barème de rétention) ; S. F et P : rare, sur brief.

### 6.8 Court métrage narratif

**Couverture : moyenne (Film Riot lu deux fois). La structure en actes n'a aucune source lue.**

**Principes [Lu] :**
- **Histoire et intrigue :** l'histoire est le sujet général (« un garçon grandit »), l'intrigue la suite des détails. Une séquence coûteuse qui n'avance pas l'histoire se supprime (critère 2 de Murch, Epstein).
- **Le montage est la réécriture finale du film.** Un bon montage a une intention ; un mauvais est un montage dont l'intention échappe à son auteur (Film Riot).
- **Pas de bon rythme en soi** : le rythme sert le ton (rapide pour un passage nerveux, long pour une scène de deuil, et l'inverse si le ton l'exige) (Epstein).
- **Impressionnisme (Hitchcock) :** le cerveau complète ce qui n'est pas montré (douche de *Psychose* : environ 78 morceaux en 45 secondes selon Hitchcock cité dans la vidéo, non vérifié).
- **Eye trace :** un plan d'horreur où la créature était du mauvais côté du regard a réduit la surprise (Film Riot).

**Procédure :** monter l'histoire en une phrase par séquence, supprimer toute séquence qui ne la sert pas, puis régler le rythme séquence par séquence (arbitrage de la section 5). **Respirations :** l'exception du skill (garder les pauses qui portent un regard ou une émotion) vise Story ; l'étendre aux moments d'émotion de films/séries est une question ouverte (section 12), défaut : règle du skill inchangée.

**Quand l'utiliser :** P (extraits officiels), fiction en H. **Quand l'éviter :** D, T, et F sauf annonce.

### 6.9 Documentaire de société (famille Story)

**Couverture : aucune source de cette étude. Les règles actuelles de Cabezer priment.**

Le skill contient déjà une méthode validée (§6 : « une image par idée, jamais par mot », nappe musicale, respirations, chapitres en carton seul, temps de lecture) et une analyse de passages de Micode, Amistory et Liv. **Ne pas la remplacer par une grammaire de cette fiche** (méthode complète : `documentaire-essai-video-archives.md`). Utiliser cette fiche seulement pour mesurer une nouvelle référence de Story avec la section 4, **après accord de Cabezer pour le téléchargement**, ou comparer le rythme d'un extrait monté à une référence déjà analysée (plans de visage de 5 à 27 s selon le skill).

**Quand l'utiliser :** S, mesure seulement. **Quand l'éviter :** tout remplacement de la méthode du skill ; D, F, T. **Piège :** transposer le rythme d'un clip ou d'une publicité à un récit de société (coupes de 0,4 à 0,8 s seulement quand la vitesse est le sens).

---

## 7. Tableau genre × famille Cabezer

« Non » : le skill ou le style de la famille l'écarte. « Hook seulement » : emprunter l'idée dans le hook, validée par le barème. « Brief » : demander à Cabezer (section 3).

| Grammaire | D | F | S | P | T | H |
|---|---|---|---|---|---|---|
| Bande-annonce (6.1) | Hook seulement | Annonces | Teaser | Oui | Annonces | Oui |
| Publicité / UGC (6.2) | Hook : barème d'abord | Hook | Non | Non | Accroche | Oui, extrait à valider |
| Montage sur musique (6.3) | SFX seulement | Passages montés | Montées, générique | Oui | Passages montés | Oui |
| Vlog voyage (6.4) | Whip entre lieux (skill) | Oui | Selon récit | Non | Non | Oui |
| Interview / podcast (6.5) | Non | Oui | Oui | Oui | Oui | Oui |
| Comédie (6.6) | SFX liste fermée, punch-in | Moments drôles | Rare | Non | Rare | Brief |
| Aftermovie / hype (6.7) | Non | Rare, brief | Non | Rare, brief | Non | Brief, extrait à valider |
| Court métrage (6.8) | Non | Non | Non | Oui | Non | Oui |
| Documentaire de société (6.9) | Non | Non | Méthode du skill | Non | Non | Non |

---

## 8. Contrôler que l'adaptation est réussie

Un montage « dans le style de » est réussi quand il **ressemble par la grammaire, pas par l'identité**, et que les règles de Cabezer sont intactes.

1. **Comparer les chiffres :** relancer `mesure-plans.py` (4.3) sur l'export avec les réglages de la référence ; comparer ASL, coupes par minute, courbe. Un écart voulu s'explique en une phrase. Jamais de comparaison avec une note de rétention.
2. **Vérifier ce qui n'a pas été repris :** aucun plan, son, voix, logo, police ou couleur de la référence.
3. **Vérifier les règles de la famille** avec le skill §14 et le rapport de `organisation-livraison-qc.md` §6.5 (sous-titres, musique, notes de hook et de rétention en D, appel au commentaire, animations dans AE, zones sûres de `formats-courts-verticaux.md` §6.2).
4. **Essai court d'abord :** pour toute grammaire nouvelle, livrer un extrait de 15 à 30 s représentatif (hook, passage calme, passage rapide) et attendre la validation avant de décliner (skill §6, « Famille sans identité validée »).
5. **Comparer au brief** (promesse, durée, plateformes, livrables) et **distinguer** mesuré, vu, écouté par Cabezer, validé par Cabezer (skill §1).

**Réussite globale :** Cabezer reconnaît sa chaîne, le spectateur reconnaît le genre, et un second visionnage à froid ne révèle ni plan inutile ni coupe qui casse le ton.

---

## 9. Versions, outils IA, plugins et coûts

- **Versions et libellés :** les commandes citées existent depuis plusieurs versions de Premiere et d'AE, mais leurs libellés français et raccourcis n'ont pas pu être vérifiés dans la documentation Adobe : les lire dans l'interface. Table des versions et test de fumée (ExtendScript, UXP, XML) : `pilotage-environnement-reprise.md`.
- **Outils IA, trois statuts (skill §16 ; `premiere-pro-avance.md` §2) :**
  - aides autorisées, résultat vérifié : transcription, montage par le texte, détection des scènes, Auto Reframe comme point de départ, Media Intelligence, Roto Brush et suivi sur un vrai plan ;
  - seulement sur demande explicite : Morph Cut, Remplissage d'après le contenu, **Generative Extend** (crée des images absentes des rushs), tout outil Firefly ou de génération de pixels ;
  - interdits par défaut : « Améliorer la parole », Correspondance automatique, « Dynamique » d'Essential Sound, voix ou musique générées, images ou animations générées.
- **Plugins :** gratuits uniquement par défaut ; tout outil payant est signalé (nom, prix connu ou « à vérifier ») et attend l'accord de Cabezer (6.3).
- **Analyse :** `ffmpeg`/`ffprobe` suffisent ; aucune installation (PySceneDetect facultatif) sur le Mac de Cabezer sans son accord.

---

## 10. Erreurs de débutant → réflexes de pro

| Erreur de débutant | Réflexe de pro |
|---|---|
| Lancer un montage H sans brief | Remplir `Suivi/brief.md`, poser les seules questions bloquantes, faire valider |
| Copier le montage d'une référence (plans, sons, polices) | Extraire la grammaire, garder l'identité de la famille, remplir « Ne pas reprendre » |
| Conclure à partir d'une seule référence | En analyser trois du même genre |
| Télécharger une référence sans demander | Demander l'accord (nom, source, taille) ; ranger hors projet |
| Se fier à un seuil de détection copié d'un guide | Lire les scores, calibrer, contrôler 10 % des coupes à l'œil |
| Laisser PySceneDetect à 0,6 s sur un montage rapide, ou reprendre un seuil de `select` pour `scdet` | `-m 2` ; deux échelles (0 à 1 contre 0 à 100) ; mêmes réglages pour comparer |
| Croire que ASL bas = bon rythme, ou le comparer à une note de rétention | L'ASL décrit, il ne juge pas ; « relances » du skill et coupes détectées ne se comptent pas pareil |
| Couper tout sur les temps d'un morceau | Varier : sur le temps, après une respiration, plan tenu sur une note longue |
| Adopter « une image avant » comme règle, ou l'appliquer à une voix | Défaut : sur l'attaque ; essai A/B jugé par Cabezer ; la voix suit le dernier mot audible |
| Appliquer le rythme d'une publicité à une Story | Une image par idée ; coupes rapides seulement quand la vitesse est le sens |
| Cacher le produit en D pour garder un écart de curiosité | Le barème prime : produit ou bouchée dans la première seconde |
| Reproduire un effet avec un pack payant | Effets natifs d'AE, calques éditables ; signaler tout payant |
| Écrire une règle de genre sans source, ou « écouté » pour une mesure | Marquer « non sourcé », tester sur un extrait ; mesuré par Claude, écouté par Cabezer |

---

## 11. Liste de contrôle

**Avant le montage**
- [ ] Brief H écrit, champs bloquants posés en une fois, validation datée.
- [ ] Une ligne écrite : ce que le spectateur doit ressentir ou comprendre.

**Avant et pendant l'analyse**
- [ ] Accord de Cabezer pour tout téléchargement ; fichier hors projet ; source, date, durée notées.
- [ ] Trois références du genre, au moins 60 s mesurées chacune ; cadence relevée.
- [ ] Coupes détectées par deux outils, seuils notés, `-m 2` si montage rapide ; 10 % des coupes et zones à effets contrôlées à l'œil.
- [ ] Fiche de style dans `Controles/Analyses/`, « Ne pas reprendre » compris.

**Pendant le montage**
- [ ] Règles du skill relues ; extrait de 15 à 30 s validé avant de décliner.
- [ ] Aucun élément de la référence dans la timeline ; aucun plugin payant sans signalement ; aucune image générée par IA.

**Avant livraison**
- [ ] Mesures relancées sur l'export, écarts expliqués ; contrôles du skill §14 faits.
- [ ] Texte clé hors de la boîte de `formats-courts-verticaux.md` §6.2 ; sous-titres D vérifiés sur téléphone.
- [ ] Mentions commerciales, droits et photosensibilité vérifiés (`conformite-droits-accessibilite.md`).
- [ ] Mesuré / vu / écouté par Cabezer / validé distingués dans le rapport.

---

## 12. Décisions à demander à Cabezer

Chaque question donne le **défaut appliqué en attendant** ; l'alternative n'est jamais une règle.

1. **Fichier de référence téléchargé : le supprimer après l'analyse ?** *Défaut :* oui, à la fin de la session d'analyse ; mesures, fiche de style et URL restent dans `Controles/Analyses/`.
2. **Respirations hors Story :** garder les pauses qui portent une émotion aussi en films/séries et au verdict d'un food long ? *Défaut :* règle du skill inchangée (exception de Story seulement).
3. **Coupe sur la musique ou SFX : essayer −1 / 0 / +1 image ?** *Défaut :* sur l'attaque ; essai A/B sur un extrait seulement à sa demande, adopté après validation sur plusieurs vidéos.
4. **Coupe au noir dans un gag.** *Défaut :* aucune ; sur demande, deux versions sur un extrait.
5. **Sous-titres de dégustation à 72–75 % de la hauteur** (bande qui tombe dans la zone basse de la boîte de test). *Défaut :* exemptés de la boîte, contrôle sur son téléphone qu'ils ne sont pas masqués (question reprise de `formats-courts-verticaux.md` §14).
6. **Captures d'écran de ses applications** pour remplacer la boîte de test par des mesures réelles. *Défaut :* boîte provisoire de `formats-courts-verticaux.md` §6.2.
7. **Montage H sans référence ni accord de téléchargement.** *Défaut :* grammaire choisie en section 6, extrait de 15 à 30 s à valider, aucune référence téléchargée.

---

## 13. Sources étudiées

**Transcriptions lues en entier (9)**

| Auteur | Titre | URL | Couverture réelle |
|---|---|---|---|
| Derek Lieu (The Art of Making Trailers) | « How to Edit a Pro Movie Trailer like A24 », 31:43 | https://www.youtube.com/watch?v=IYC5l5iTiDo | Transcription lue. Typologie personnelle, comptage sur 50 bandes-annonces A24, dialogue, cartons, musique. Images non examinées. |
| Tony Zhou (Every Frame a Painting) | « Edgar Wright - How to Do Visual Comedy », 8:00 | https://www.youtube.com/watch?v=3FOzD4Sfgag | Transcription lue. Neuf techniques de mise en cadre. Extraits de films non visionnés. |
| Tony Zhou (Every Frame a Painting) | « How Does an Editor Think and Feel? », 9:24 | https://www.youtube.com/watch?v=3Q3eITC01Fg | Transcription lue. Citations de Murch et Schoonmaker telles que citées. Le « 70 % de rythme » attribué à Murch n'est pas repris. |
| John Hess (Filmmaker IQ) | « Editing to the Beat - the One Frame Trick », 7:15 | https://www.youtube.com/watch?v=7E_mi_xNYOk | Transcription lue. Un seul praticien. Démonstration sur 24 i/s, à écouter pour juger. |
| Adam Epstein, talk MZ, relayé par Film Riot | « 6 Rules for Cinematic Editing » | https://www.youtube.com/watch?v=9_KOfYrxcF4 | Transcription lue. Hitchcock, règle des six sans pourcentages, histoire/intrigue. |
| Film Riot | « The Theory of Editing », 10:59 | https://www.youtube.com/watch?v=XA87UorMO-U | Transcription lue. Effet Kuleshov, suspense, règle des six, eye trace. |
| StudioBinder | « 6 Ways to Edit Any Scene », 18:48 | https://www.youtube.com/watch?v=FVR8zz8ci2k | Transcription lue. Raccord de regard, champ-contrechamp, coupe croisée, J/L, coupe sur l'action. |
| Jay Sia | « Editing a Music Video From START TO FINISH (Full Masterclass) - Premier Pro and After Effects », 23:20 | https://www.youtube.com/watch?v=SAlJ32_g5r8 | Transcription lue. Workflow orienté vers ses packs, outils payants ou de statut inconnu, aucune version de Premiere/AE précisée. |
| heyDominik | « I Studied 1,000 Hooks, Here's How to ACTUALLY Go Viral », 20:07 | https://www.youtube.com/watch?v=Xqy9L-88wcw | Transcription lue. Principes d'accroche d'un auteur marketing ; partie IA exclue ; aucun délai chiffré fiable. |

**Ajoutées en passe 2 (extraits de résultats de recherche ; pages non ouvertes, résolution DNS refusée)**

| Auteur | Titre | URL | Couverture réelle |
|---|---|---|---|
| OpenStreetMap Foundation | « Attribution Guidelines » | https://osmfoundation.org/wiki/Attribution | Extrait seulement : l'attribution nomme OpenStreetMap et rend la licence ODbL claire, par exemple par un lien vers openstreetmap.org/copyright. Texte complet non lu. |
| OpenStreetMap | « Copyright and License » | https://www.openstreetmap.org/copyright | Extrait : afficher la notice de copyright et indiquer l'ODbL ; la formule « © OpenStreetMap contributors » vient de versions archivées. Texte actuel non lu. |
| Adobe Community (fil francophone) | « Réduire les tracés » | https://community.adobe.com/t5/after-effects-discussions/r%C3%A9duire-les-trac%C3%A9/m-p/13476110 | Titre et extrait : « Réduire les tracés » désigne Trim Paths. Fil non ouvert ; libellé à confirmer à l'écran. |
| LinkedIn Learning (ex-Lynda) | « Scene edit detection » (Premiere Pro 2021 New Features) | https://www.lynda.com/Premiere-Pro-tutorials/Scene-edit-detection-clips/2871172/2415177-4.html | Extrait : la fonction découpe les clips contenant des changements de plan et peut rater des coupes. Cours non visionné ; menu français non confirmé. |

**Vérifications locales :** passe 1, ffmpeg 6.1.1 (`select`, `scdet`, `tile`, `palettegen`) et PySceneDetect 0.7.1 (code, `--help`) sur une vidéo de test à coupes connues. Passe 2 : échelles `select` (0 à 1) et `scdet` (0 à 100, défaut 10) rejouées sur une autre vidéo synthétique (0,56 et 0,48 contre 21,75 et 18,60 sur les mêmes coupes). Ces essais prouvent le comportement des outils, pas leur qualité sur les rushs de Cabezer.

**Consultées par extrait seulement ou non ouvertes (rien de chiffré n'en est retenu comme règle) :** Walter Murch, *In the Blink of an Eye* (livre non lu ; table de pourcentages vue dans une thèse en extrait) ; documentations Adobe, PySceneDetect en ligne, ffmpeg.org, TikTok (inaccessibles) ; vidéos non lues faute d'accès : Derek Lieu (trois actes, « pro editor »), Murch (Web of Stories), Daniel Schiffer, Chase Chappell, Sam Kolder, Learn Online Video, Mark Bone, Javier Mercedes (multicam, hype reel), Every Frame a Painting (Buster Keaton), Konradnoises (Edgar Wright) ; guides tiers (structure publicitaire, spécifications TikTok, Lensvid, Nearstream, Larry Jordan, Mark Bone via Musicbed), jamais source unique d'une règle.
