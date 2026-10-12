# Analyse du skill de montage « cabezer-premiere-shorts »

Ce que je te conseille de **garder**, **retirer** ou **reformuler**, et les questions qui ne relèvent que de toi.

## Comment l'analyse a été faite

- Deux audits indépendants du SKILL.md v2 (58 Ko, 532 lignes), ligne à ligne : le mien et celui d'un agent Sonnet 5.5. Chaque point a été vérifié sur le texte exact du skill.
- 13 agents rédacteurs (11 fiches de la passe 1, puis 2 nouvelles fiches) ont comparé ton skill aux pratiques des monteurs professionnels et signalé chaque règle qui s'y oppose. Ils ne l'ont jamais réécrite d'eux-mêmes.
- Un agent critique a cherché les conflits entre les fiches et ton skill, puis tout a été harmonisé sur une liste de décisions communes.

**Résultat :** 23 contradictions réelles, 11 éléments périmés ou mal rangés, 3 règles perdues dans l'historique, une vingtaine d'ambiguïtés (dont 16 questions pour toi) et un problème de structure grave : les fichiers cités sont absents. Tout ce qui pouvait se trancher avec ta propre règle (« la consigne la plus récente l'emporte ») est appliqué dans la v3. Le reste est marqué **[Q]** : la v3 applique un défaut prudent en attendant ta réponse (section 4).

---

## 1. Le problème le plus grave : ton skill renvoie à des fichiers qui n'existent pas

La version de ton skill installée sur claude.ai ne contient **que SKILL.md**. Ces 23 fichiers sont cités mais absents :

- **18 fiches `references/`** :
  - générales : `techniques-et-controles.md`, `tutoriels-2026-09-12.md`, `methode.md`, `aprilynne-recit-regard-rythme.md`, `tutoriels-2026-09-14.md`, `dji-osmo-pocket-3-luts.md`, `montage-higgsfield.md`, `musiques-originales-cabezer.md`, `plugins-installes.md`, `premiere-tesseract.md`, `story-montage-micode-amistory.md`, `story-references-2026-09-20.md`, `zooms-broll-et-respirations.md` ;
  - `identites-visuelles/` : `food-degustation-v1.md`, `films-series-prisme-v1.md` ;
  - `after-effects/` : `premiere-after-effects.md`, `tech-liquid-glass.md`, `tutoriels-2026-09-16.md`.
- **5 fichiers `assets/sfx-cabezer/`** : les 4 SFX de base et `manifest.json`.

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
| 5 🟠 | §11 Story | Composition originale = solution de repli (« si aucune musique libre ne convient ») contre « compose réellement 2 ou 3 musiques » (plus récent) ; méthode Apple Loops décrite en entier alors qu'elle est déclassée | Composition en 2–3 thèmes = **défaut en Story** ; Apple Loops = matériau possible, jamais en collage ; méthode en 4 étapes **déplacée dans l'historique**. Hors Story : **[Q]** |
| 6 🟡 | §11 | « Conserver la vitesse d'origine du morceau » contre « ramener au tempo commun avec atempo » | Vitesse d'origine pour tout morceau fini ; le tempo ne se change que dans une composition faite de boucles |
| 7 🟠 | §5.1 / §16 | Scripts Python Milan « creer_habillage », « creer_sous_titres » contre « pas de graphisme fabriqué hors d'AE (Python) » | Précisé : ces scripts **pilotent AE** et génèrent le XML, ils ne fabriquent aucune image ; ce sont des exemples, pas des gabarits ; liste déplacée dans `projets-cabezer.md` |
| 8 🟠 | §5 / §5.2 | « Demander le hook » (dont **ton hook habituel**) contre le barème qui donne 3 points au « produit dans la 1re seconde » : ton hook peut être recalé, et la boucle « retravailler jusqu'à 8 » n'a pas de fin | Ton choix prime ; on note ton hook, on propose au plus 2 variantes, **2 itérations maximum** ; si 8 est impossible sans contredire ton choix, livraison avec la note réelle et l'explication |
| 9 🟡 | §6 générique | « Décaler tout ce qui suit de **240 images** » = 8 s seulement à 30 i/s (9,6 s à 25 i/s) | Insertion avec l'outil Insérer, durée réelle du fichier convertie à la cadence de la séquence |
| 10 🟠 | §7 / §2 / §5.1 | §7 « zoom jamais imposé, pas de zoom à chaque plan » sans exception, alors que la dégustation impose un punch-in à chaque coupe face caméra | §7 précise : zoom Micode pour F, S, P, T ; **exception dégustation** = punch-ins secs |
| 11 🟠 | §4 / §5 / §5.2 | Trois seuils pour les blancs : aucun blanc (§4), couper > 0,25 s (§5), jusqu'à 6 blancs ≥ 0,25 s/min tolérés (§5.2) | Ligne « Blancs » ajoutée au tableau §2 par famille ; le « 6 par minute » est un **contrôle du résultat**, pas une cible de coupe |
| 12 🟠 | §2 / §5 / §11 | Dégustation : banque Pixabay ; §11 : « bibliothèque ouverte » et autres sources, sans dire laquelle prime | Dégustation = banque Pixabay et **liste fermée** ; bibliothèque ouverte pour les autres familles |
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
| 23 🟠 | §1 / §16 | « Animations uniquement dans AE » contre Tesseract (animations) et Higgsfield (« textes animés ») | Ils restent des exceptions **sur demande nominative** ; leur statut gratuit ou payant est à vérifier **[Q]** |

---

## 4. Questions pour toi (la v3 applique le défaut en attendant)

| # | Question | Défaut appliqué | Mon avis |
|---|---|---|---|
| 1 | Food long, Story, films, tech **tournés en France** : sous-titres français incrustés, ou seulement un SRT ? | SRT livré, pas d'incrustation | Pour YouTube long, le SRT suffit souvent ; à incruster si ton public regarde sans le son |
| 2 | **Identité food long** : il n'existe aucune charte (« Charte food » n'est définie nulle part). On en crée une ? | Faire valider un extrait | Oui : 30 s de test suffisent |
| 3 | **Story v15 rose** et **générique Amed Story** : validés depuis le 30/09 ? | En attente | Si oui, dis-le : je retire « à valider » |
| 4 | « Un Short/Reel **monté seul** garde la dégustation complète » : cette exception tient encore ? (le reste de la DA v2 dit « bouchée courte » partout) | Oui | Probablement à retirer : c'est un reste du 17/09 |
| 5 | Dégustation : **ambiance du lieu** sous un insert muet ? **foley** (bruit de croustillant) sur un insert de préparation ? | Non et non | Les créateurs food utilisent le vrai son ; le faux foley est risqué pour une dégustation, qui est un avis honnête |
| 6 | **Composition musicale** en food long et tech, ou seulement en Story ? | Story seulement | D'accord : la composition coûte cher en temps |
| 7 | **Respirations** gardées aussi pour l'émotion en films/séries et le verdict en food long ? | Non (règle §4) | Je conseille oui : c'est ce que font tous les monteurs étudiés |
| 8 | Fin de Story : réserver **5 à 20 s** pour l'écran de fin YouTube ? | Oui (noir et musique qui s'éteint) | Oui, sinon les éléments de fin recouvrent ton regard final |
| 9 | Sous-titres dégustation : un **rendu d'un seul tenant**, à recouper après tes retouches, ou une piste par séquence ? | Rendu AE, recoupé | Une piste par séquence validée t'éviterait les désynchronisations |
| 10 | Sous-titres à 72–75 % de la hauteur : exemptés de la « boîte de zones sûres » ? | Oui, contrôle sur téléphone | À vérifier sur une capture de chaque application |
| 11 | **SCANDALE FOOD** : famille à part ou série Story ? | Règles Story | — |
| 12 | Afficher le **nom et la fonction** d'un intervenant à sa première apparition ? | Seulement sur demande | Pratique standard en documentaire |
| 13 | **Flouter** les inconnus identifiables (clients, employés, enfants, plaques) ? | Signaler au dérush, flouter sur ta décision | Voir la fiche conformité : le droit à l'image français est strict |
| 14 | **Tesseract et Higgsfield** : toujours utilisés ? gratuits ? | Seulement sur demande nominative | S'ils ne servent plus, retire-les de la description |
| 15 | Réduction de bruit **identique sur toutes les prises** (ta règle) ou adaptée prise par prise (pratique pro) ? | Ta règle | Garde ta règle pour le timbre ; adapter seulement le niveau de réduction sur une prise très bruyante |
| 16 | **YouTube long en 4K** ? Ta v2 disait « 1920×1080 ou 3840×2160 » sans trancher | 1080p ; 4K sur demande depuis des rushs 4K | YouTube encode mieux un fichier envoyé en 4K, même pour les spectateurs en 1080p : à envisager pour tes vidéos phares |

Les questions plus techniques issues des fiches (libellés, seuils, outils) sont dans `references/decisions-en-attente.md`.

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
