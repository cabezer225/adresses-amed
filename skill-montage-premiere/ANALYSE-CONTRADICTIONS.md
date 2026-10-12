# Analyse du skill de montage « cabezer-premiere-shorts »

Ce que je te conseille de **garder**, **retirer** ou **reformuler**, et les questions qui ne relèvent que de toi.

## Comment l'analyse a été faite

- Deux audits indépendants du SKILL.md v2 (58 Ko, 532 lignes), ligne à ligne : le mien et celui d'un agent Sonnet 5.5. Chaque point a été vérifié sur le texte exact du skill.
- 13 agents rédacteurs (11 fiches de la passe 1, puis 2 nouvelles fiches) ont comparé ton skill aux pratiques des monteurs professionnels et signalé chaque règle qui s'y oppose. Ils ne l'ont jamais réécrite d'eux-mêmes.
- Un agent critique a cherché les conflits entre les fiches et ton skill, puis tout a été harmonisé sur une liste de décisions communes.
- Un relecteur indépendant a comparé la v2 et la v3 ligne à ligne : aucune valeur chiffrée ni aucun chemin perdu ; ses 19 remarques (pertes de nuance, renvois faux, règle « minimum 8 » affaiblie) sont corrigées.

**Résultat :** 23 contradictions réelles, 11 éléments périmés ou mal rangés, 3 règles perdues dans l'historique, une vingtaine d'ambiguïtés (tranchées par tes réponses, section 4) et un problème de structure grave : les fichiers cités sont absents. Tout ce qui pouvait se trancher avec ta propre règle (« la consigne la plus récente l'emporte ») est appliqué dans la v3. Le reste t'a été posé : tes 19 réponses du 12/10/2026 sont appliquées (section 4).

---

## 1. Le problème le plus grave : ton skill renvoie à des fichiers qui n'existent pas

La version de ton skill installée sur claude.ai ne contient **que SKILL.md**. Ces 23 fichiers sont cités mais absents :

- **18 fiches `references/`** :
  - générales : `techniques-et-controles.md`, `tutoriels-2026-09-12.md`, `methode.md`, `aprilynne-recit-regard-rythme.md`, `tutoriels-2026-09-14.md`, `dji-osmo-pocket-3-luts.md`, `montage-higgsfield.md`, `musiques-originales-cabezer.md`, `plugins-installes.md`, `premiere-tesseract.md`, `story-montage-micode-amistory.md`, `story-references-2026-09-20.md`, `zooms-broll-et-respirations.md` ;
  - `identites-visuelles/` : `food-degustation-v1.md`, `films-series-prisme-v1.md` ;
  - `after-effects/` : `premiere-after-effects.md`, `tech-liquid-glass.md`, `tutoriels-2026-09-16.md`.
- **5 fichiers `assets/sfx-cabezer/`** : les 4 SFX de base et `manifest.json`.

Depuis tes réponses, `premiere-tesseract.md` et `montage-higgsfield.md` ne servent plus (outils retirés) : il en reste 16 à rapatrier, plus les 5 SFX.

**Conséquence :** quand Claude lit ton skill depuis claude.ai, il ne peut ouvrir ni PRISME, ni Liquid Glass, ni la chaîne couleur Pocket 3, ni la méthode Micode/Amistory. Il devine ou il saute.

**À faire (toi) :** ces fichiers existent sans doute dans ton dossier de skill sur le Mac. Au moment d'installer la v3, fusionne les dossiers (section 7) pour que tout parte ensemble. En attendant, la v3 dit à Claude de signaler un fichier manquant et de ne jamais en deviner le contenu.

---

## 2. À garder absolument (les forces de ton skill)

Ces règles sont meilleures que ce que proposent la plupart des formations. Les monteurs pros les appliquent, souvent sans les écrire :

- **L'ordre de priorité et « appliqué / contrôlé / validé ».** Les fiches pros insistent sur la même chose : un export lancé n'est pas un export validé.
- **Les protections de ta voix :**
  - « Bref, c'est partiiii » gardé en entier ;
  - fin des exclamations étirées ;
  - moments humains et famille ;
  - appel au commentaire jamais inventé.

  C'est la règle n° 1 de Walter Murch : l'émotion avant tout.
- **Le dérush de dégustation issu de tes propres reprises** : hésitations, bonne correction seulement, restes autour des coupes, test sur le son source. Les monteurs de Shorts appellent ça « tuer le gras ».
- **La DA Dégustation v2 bâtie sur ta propre base** plutôt que sur un créateur copié. Un pro emprunte une grammaire, jamais une identité.
- **La notation hook/rétention.** Peu de créateurs mesurent ; c'est exactement la méthode « mesurer pour décrire » des fiches.
- **« Une image par idée, jamais par mot »** et le **temps de lecture minimal**. C'est la méthode des documentaristes étudiés (Johnny Harris, Vox, Nerdwriter), en plus précise.
- **La chaîne couleur par caméra** (« une seule conversion »), conforme à la gestion des couleurs pro.
- **Les pièges FCP XML vérifiés sur Milan.** C'est du savoir terrain qu'aucun tuto ne donne.
- **La prudence sur la rétention** (une vidéo isolée ne fait pas une règle).
- **« Gratuits uniquement »** et **« méthodes réellement étudiées, pas des liens »**.

---

## 3. Contradictions : ce que la v3 a tranché

Gravité : 🔴 fausse un montage · 🟠 fait hésiter Claude · 🟡 mineure.

| # | Où (v2) | Ce qui se contredit | Décision dans la v3 |
|---|---|---|---|
| 1 🔴 | §11 / Historique 30/09 bis | Nappe Story à **15 dB** sous la voix dans la règle, **24 dB** dans l'historique (plus récent) | **24 dB** (le plus récent), mesuré en LUFS court terme ; 15 dB retiré |
| 2 🔴 | §9 / §1 / §16 | « Pour animer des sous-titres : Graphiques et titres > Mettre à niveau la légende » (animation dans Premiere) contre « animations uniquement dans AE » et « pas de légendes Premiere au style générique » | Sous-titres incrustés = composition AE pour toutes les familles ; la piste Premiere sert de transcription et de SRT. **« Mettre à niveau la légende » retiré** |
| 3 🔴 | §1 / §5.1 / §7 / §16 | Le mot « animation » n'est jamais défini : punch-ins, whips, shakes, zooms Micode et speed ramps se font dans Premiere alors que « les animations se font uniquement dans AE » | Définition en §1 : **animation graphique** (texte, emoji, prix, schéma, sous-titre animé…) = AE ; **traitement d'un plan filmé** (punch-in, zoom, whip, shake, rampe, recadrage) = Premiere |
| 4 🟠 | §6 point 2 / point 9 | Plans d'univers suivi de **1,5 à 3 s** contre « une image sans texte reste au moins **2 s** » (plus récent) | **2 à 3 s** ; les coupes rapides de 0,4 à 0,8 s restent l'exception nommée |
| 5 🟠 | §11 Story | Composition originale = solution de repli (« si aucune musique libre ne convient ») contre « compose réellement 2 ou 3 musiques » (plus récent) ; méthode Apple Loops décrite en entier alors qu'elle est déclassée | Composition en 2–3 thèmes = **défaut en Story** ; Apple Loops = matériau possible, jamais en collage ; méthode en 4 étapes **déplacée dans l'historique**. Étendue au food long et à la tech par ta réponse |
| 6 🟡 | §11 | « Conserver la vitesse d'origine du morceau » contre « ramener au tempo commun avec atempo » | Vitesse d'origine pour tout morceau fini ; le tempo ne se change que dans une composition faite de boucles |
| 7 🟠 | §5.1 / §16 | Scripts Python Milan « creer_habillage », « creer_sous_titres » contre « pas de graphisme fabriqué hors d'AE (Python) » | Précisé : ces scripts **pilotent AE** et génèrent le XML, ils ne fabriquent aucune image ; ce sont des exemples, pas des gabarits ; liste déplacée dans `projets-cabezer.md` |
| 8 🟠 | §5 / §5.2 | « Demander le hook » (dont **ton hook habituel**) contre le barème qui donne 3 points au « produit dans la 1re seconde » : ton hook peut être recalé, et la boucle « retravailler jusqu'à 8 » n'a pas de fin | **Minimum 8 gardé** (ta consigne). Seule exception : si 8 est impossible sans contredire ton choix, ton choix prime et la note réelle est livrée avec l'explication et au plus 2 variantes. Limite à 2 itérations : question 17 |
| 9 🟡 | §6 générique | « Décaler tout ce qui suit de **240 images** » = 8 s seulement à 30 i/s (9,6 s à 25 i/s) | Sans objet : le générique a été supprimé (ta réponse) ; un futur générique s'insérera avec l'outil Insérer, durée convertie à la cadence de la séquence |
| 10 🟠 | §7 / §2 / §5.1 | §7 « zoom jamais imposé, pas de zoom à chaque plan » sans exception, alors que la dégustation impose un punch-in à chaque coupe face caméra | §7 précise : zoom Micode pour F, S, P, T ; **exception dégustation** = punch-ins secs |
| 11 🟠 | §4 / §5 / §5.2 | Trois seuils pour les blancs : aucun blanc (§4), couper > 0,25 s (§5), jusqu'à 6 blancs ≥ 0,25 s/min tolérés (§5.2) | Ligne « Blancs » ajoutée au tableau §2 par famille ; le « 6 par minute » est un **contrôle du résultat**, pas une cible de coupe |
| 12 🟠 | §2 / §5 / §11 | Dégustation : banque Pixabay ; §11 : « bibliothèque ouverte » et autres sources, sans dire laquelle prime | Dégustation = banque Pixabay et ta **liste de référence** (autre son de la banque sur ton accord) ; bibliothèque ouverte pour les autres familles |
| 13 🔴 | §6 point 9 | Le temps de lecture vise « toute information écrite (… légende) » : appliqué aux sous-titres mot à mot de dégustation (≈ 0,25 s/mot), il est impossible | Portée précisée : familles longues ; **ne s'applique pas** aux sous-titres mot à mot de dégustation |
| 14 🟠 | §5 / §5.1 | Le prix apparaît de trois façons, et « pas de cartouche descriptif » contredit la pastille « produit · prix » | Deux cas : petite étiquette « produit · prix » à la révélation ; **montant seul en grand** animé seulement à une vraie annonce |
| 15 🟠 | §5 / §8 | Un plan stock de préparation « appétissant » contre « une image ne doit pas suggérer une expérience que Cabezer n'a pas vécue » | Stock gardé (avec ton accord) mais du même type de produit, sans logo ni lieu identifiable, **jamais présenté comme le plat servi** |
| 16 🟠 | §5 / §8 / §12 | Tes exemples de corrections (« deux mozzarelles… trois » → « trois mozzarelles ») recollent des morceaux de prises, alors que §8 et §12 interdisent de « recomposer les paroles » | Règle précise : retirer un faux départ pour garder **ce que tu voulais dire** est permis ; un collage qui crée une affirmation jamais faite est interdit |
| 17 🟡 | §4 / §5.2 / §14 | Appel au commentaire « présent » obligatoire (§14) et noté (§5.2), mais interdit de l'inventer s'il n'a pas été tourné | S'il n'a pas été tourné : le signaler, accepter le point en moins, ne pas bloquer la livraison |
| 18 🔴 | §3 / §11 / §14 | « Visionnage et écoute intégraux », « mixage écouté » : **Claude n'entend pas** | Partout : « mesuré (LUFS, crêtes, mono, transcription) », et ton écoute est demandée, notée « faite » ou « en attente » |
| 19 🟠 | Intro / §1 | Deux règles d'arbitrage concurrentes : l'ordre de priorité, et « la version la plus récente l'emporte » | Une seule : brief → exception de famille → règle générale → fiches → tutoriels ; **à niveau égal**, la plus récente l'emporte |
| 20 🟡 | §3 / §11 | « Ne jamais fusionner couleur et mixage » contre « une demande de terminer… autorise ces passes ensemble » | L'autorisation supprime seulement les validations intermédiaires ; les passes restent distinctes |
| 21 🟡 | §7 | « Transitions réservées aux changements d'argument » contre J/L-cuts et micro-fondus audio | La règle vise les transitions **visibles** ; J/L-cuts permis, jamais sur la bouchée ou la réaction en dégustation |
| 22 🟡 | §7 / §5.1 | « Jamais linéaire » contre punch-in sec (pas d'interpolation) | Un punch-in sec est un changement instantané, pas un mouvement ; vitesse constante permise pour une rotation, un défilement ou un compteur |
| 23 🟠 | §1 / §16 | « Animations uniquement dans AE » contre Tesseract (animations) et Higgsfield (« textes animés ») | **Tesseract et Higgsfield retirés du skill** (ta réponse) |

---

## 4. Tes réponses du 12/10/2026 (appliquées dans la v3)

| Question | Ta réponse | Ce qui change dans le skill |
|---|---|---|
| Sous-titres des vidéos longues tournées en France | SRT seulement | Rien d'incrusté ; SRT livré (§2, §9) |
| Story v15 rose et générique « Amed Story 🧢 » | Supprimés, à refaire en entier | Blocs v15 et générique retirés ; Story sans identité validée : nouvelle direction à proposer sur un extrait (§6) ; fichiers gardés en archive dans `projets-cabezer.md` |
| Short/Reel monté seul en dégustation | Coupe courte partout | Exception du 17/09 retirée (§5) |
| Personnes filmées | Je signale, tu décides | Liste au dérush, floutage seulement sur ta désignation (§8) |
| Ambiance du lieu sous un insert muet (D) | À me proposer d'abord | Méthode proposée au premier usage (§5, §20) |
| Foley d'aliment | Jamais | Aucun son ajouté, dans aucune famille (§5) |
| Composition musicale originale | Story + food long + tech | Méthode par défaut en S, F, T ; films/séries : ta bibliothèque (§2, §11) |
| Respirations d'émotion | Étendre | Gardées aussi en films/séries et au verdict du food long (§2, §4) |
| Écran de fin YouTube en Story | Oui | 5 à 20 s réservées (§6) |
| Sous-titres de dégustation | Un rendu par séquence ; gardés à 72–75 % | Un rendu AE par passage validé ; exemptés de la boîte de zones sûres, contrôle sur capture (§9) |
| SCANDALE FOOD | N'existe plus | Mention retirée (§12) |
| Intervenants | Oui, à la 1re apparition | Nom et fonction une fois, hors dégustation (§6 point 7) |
| Tesseract et Higgsfield/Higgsedit | Retirer les deux | Retirés de la description, de §1 et §16 |
| YouTube long | 4K si rushs 4K | 3840×2160 par défaut quand les rushs sont en 4K (§13) |
| Réduction de bruit | Adapter si prise très bruyante | Chaîne identique, un peu plus de réduction seulement sur une prise très bruyante, signalée (§11) |
| Notation sous 8 | 2 essais max puis livrer | Au plus deux passes de retravail (§5.2) |
| Identité food long | Créer une charte sur extrait | 30 s habillées à valider, puis la fiche devient la règle (§6) |
| Scripts de contrôle | Sans redemander | Les scripts qui ne font que lire se lancent seuls ; ceux qui modifient attendent ton accord (§3) |
| Repas offert, invitation, produit reçu | Me demander à chaque fois | Signalé au brief, tu choisis la mention (§8) |

Il reste environ 70 questions techniques (libellés, seuils, outils) dans `references/decisions-en-attente.md`. Elles ont toutes un défaut prudent et ne seront posées qu'au moment où elles bloquent un montage.

---

## 4 bis. Formats long et court, famille Lifestyle (tes réponses du 12/10/2026, série 2)

Le skill sépare maintenant **le format d'abord, la famille ensuite** (SKILL §2) : dix cas, chacun avec sa colonne.

| | Food | Story | Tech | Films/séries | Lifestyle |
|---|---|---|---|---|---|
| **Long** | L-Food | L-Story | L-Tech | L-Films | L-Life |
| **Court** | C-Food (dégustation, duel, recette, vlog street food) | C-Story | C-Tech | C-Films | C-Life |

| Ta réponse | Règle dans le skill |
|---|---|
| Courts Story, Tech, Films : extraits du long et tournés exprès | Selon le brief, défaut : extrait (§2.3, §12) |
| Courts food : dégustation, duel/classement, recette, vlog street food | Tous en DA v2, sans musique ; note à l'écran en dégustation et duel/classement seulement (§2.4) |
| Nouvelle famille Lifestyle, long et court | Aucune musique ; SFX comme la dégustation ; vlog : cartes de lieu et de date, speed ramps et transitions, textes et emojis de réaction ; face caméra serré ou posé selon le sujet ; identité à créer (§2.5) |
| Identité propre au court | Chaque famille a une identité de court distincte du long ; à créer sur extrait pour Story, Tech, Films et Lifestyle (§6) |
| Notation sur 10 pour tous les courts | Barème adapté par famille (§5.2) |
| Sous-titres mot à mot, aucune musique, punch-ins secs pour les courts Story, Tech, Films | §2.1, §2.3, §9, §11 |
| Durée jusqu'à 3 min selon le sujet | Tous les courts (§2.1) |
| Hook demandé, SFX comme la dégustation, appel au commentaire, langue à l'étranger à demander | Tous les courts (§2.1, §9) |

À créer avec toi, sur des extraits à valider : les identités de court Story, Tech, Films et Lifestyle, l'identité Lifestyle longue, la charte food long et la nouvelle identité Story.

---

## 5. À retirer ou déplacer (fait dans la v3)

| Élément de la v2 | Pourquoi | Où c'est maintenant |
|---|---|---|
| Nappe « environ 15 dB » | Remplacée le 30/09 bis | Historique |
| Méthode Apple Loops en 4 étapes (CAF, atempo, zone par zone) | Abandonnée le 30/09 (« sonnait comme une seule boucle partout ») | Historique |
| « Graphiques et titres > Mettre à niveau la légende » | Contredit « animations uniquement dans AE » | Supprimé |
| « Si aucune musique libre ne convient, composer… » et « décider musique ou silence selon le contexte » (Story) | Remplacés par la nappe continue validée « comme les références » et par la composition en 2–3 thèmes | Historique |
| « Rendu à la résolution maximale » | Cette option n'existe pas sous ce nom : c'est « Rendu à la profondeur maximale » ou « Utiliser la qualité de rendu maximale » | Corrigé dans §13 (libellé à confirmer sur ton écran) |
| « Améliorer le dialogue » | Le nom français est sans doute « Améliorer la parole » (Enhance Speech) | Corrigé, à confirmer |
| Entrées de l'historique « Johan Papz » présentées comme actives | Remplacées le 02/10 par la DA v2 ; le renvoi « (§5.1) » disait l'inverse | Annotées « remplacée » |
| Historique dans le désordre (… 30/09, 30/09 bis, 29/09 ter, 29/09 bis, 29/09, 28/09 ter) | Impossible d'appliquer « la plus récente l'emporte » | Trié dans `references/historique.md` |
| Scripts Milan, notes v03 à v06, chemins de la musique v10, fichiers du générique et de v15 | Détails de projets passés mêlés aux règles générales | `references/projets-cabezer.md` |
| « Pas de bruitage d'objet gratuit » | Ambigu (« gratuit » : sans raison ou sans payer ?) | « Aucun bruitage sans élément visuel correspondant » |
| « Musique : Absente par défaut » (tableau dégustation) | « Par défaut » laissait croire qu'on pouvait en mettre | « Absente (ton choix, sauf demande) » |

**Règles qui n'existaient que dans l'historique**, remontées dans le corps :
- montrer ta chaîne YouTube, pas ton profil TikTok, quand tu parles de ta chaîne principale ;
- bruitages Story : tampon, ticket, feutre, vraie déchirure CC0 ;
- nappe à 24 dB.

---

## 6. Ce que les pros font et qui manquait (ajouté dans la v3)

- **Étape 0 « brief »** avant tout montage : promesse en une phrase, partenariat, personnes à protéger, niveau d'autonomie.
- **Règle pour les montages hors familles** (vlog, pub, interview, clip) : extrait de 15 à 30 s à faire valider, fiche « adaptation et genres ».
- **Mode autonome avec défauts** : hook habituel, anglais à l'étranger, rien de téléchargé sans accord.
- **Outils IA classés** en trois statuts : autorisé comme aide, sur demande, interdit.
- **Crête vraie ≤ −1 dBTP**, absente de la v2. L'encodage AAC fait monter les crêtes : sans cette marge, risque de saturation après publication.
- **iPhone HLG / Apple Log**, absent de la chaîne couleur, alors que l'iPhone est cité en multicam.
- **Extraits tiers** : un crédit n'est pas une autorisation (Content ID).
- **Statut des méthodes** « à valider » depuis le 28/09 : elles sont désormais proposées au premier usage au lieu d'être appliquées d'office.
- **Principes de monteur pro** et **index des 13 fiches** (§19).

Ce que j'ai **refusé** parmi les suggestions des agents :
- **Un fondu audio de 2 à 4 images sur chaque coupe.** Ça adoucirait tes coupes sèches de dégustation ; il est gardé seulement là où un clic s'entend.
- **Faire de la piste de légendes Premiere la source des sous-titres incrustés.** Tu as refusé ce rendu sur Maritozzo ; c'est devenu la question n° 9.

---

## 7. Installer la v3

1. Sur ton Mac, ouvre le dossier actuel du skill `cabezer-premiere-shorts` : celui qui contient tes `references/` et `assets/`.
2. Fais-en une copie de sauvegarde.
3. Remplace `SKILL.md` par celui de ce dépôt.
4. Copie dedans le dossier `references/pro/` (13 fiches et 10 scripts) et les fichiers `references/historique.md`, `projets-cabezer.md`, `decisions-en-attente.md` et `decisions-harmonisation.md`.
5. Vérifie que les 18 fiches et les 5 SFX de la section 1 sont bien présents, puis compresse le dossier et téléverse-le là où tu gères ce skill sur claude.ai (le dossier entier, pas seulement SKILL.md).

L'archive `cabezer-premiere-shorts-v3.zip` de ce dépôt contient déjà tout ce que j'ai produit. Il ne lui manque que tes 23 fichiers d'origine.
