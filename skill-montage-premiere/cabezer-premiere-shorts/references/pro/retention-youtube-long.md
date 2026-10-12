# Rétention et rythme des vidéos YouTube longues

> **Réponses de Cabezer du 12/10/2026 — elles priment sur cette fiche**, en particulier sur sa section « Décisions à demander ». **Format d'abord, famille ensuite (SKILL §2)** : long (L-Food, L-Story, L-Tech, L-Films, L-Life) ou court (C-Food, C-Story, C-Tech, C-Films, C-Life) ; codes de cette fiche : D = C-Food, F = L-Food, S = L-Story, P = L-Films, T = L-Tech ; nouvelle famille Lifestyle (vlogs, face caméra : aucune musique, SFX comme la dégustation). **Tous les courts** : hook demandé, sous-titres mot à mot, aucune musique, SFX comme la dégustation, punch-ins secs, appel au commentaire, notation sur 10, identité propre au court. **Longs** : SRT seul en France ; composition musicale en Story, food et tech ; respirations d'émotion gardées en films/séries et au verdict du food long ; 4K si rushs 4K. Aussi : identité Story v15 et générique « Amed Story 🧢 » supprimés ; jamais de foley d'aliment ; ambiance en dégustation proposée au premier usage ; un rendu de sous-titres par passage ; intervenants identifiés à la première apparition (hors courts food) ; au plus deux passes de retravail sous 8 ; Tesseract, Higgsfield et SCANDALE FOOD retirés. **Réponses techniques (série 3)** : interface de Premiere et d'AE en anglais ; scripts AE et Terminal autorisés ; stock libre de droits sans redemander ; tout SFX de la banque Pixabay permis ; arrêt sur image permis partout ; pas de test de photosensibilité ; audio YouTube 384 kbit/s ; proxys toujours en long ; Frame.io pour les relectures ; WhisperX à installer ; « 19h30 » et « 12,50 € » ; Liquid Glass à recréer. Liste complète : `../decisions-en-attente.md`.

Fiche de référence du skill `cabezer-premiere-shorts`. Elle apprend à tenir la promesse d'une vidéo longue du premier plan jusqu'à la fin : ouverture, boucles, rythme, B-roll, son, chapitres, fin, lecture de la courbe. Elle ne remplace aucune règle du skill. Elle renvoie aux autres fiches de `references/pro/` par nom de fichier et numéro de section, et au skill par « skill §N » (numérotation v3).

## Quand lire cette fiche

- Avant de structurer ou de remonter une vidéo YouTube longue : food long (F), Story (S), films/séries PRISME (P), tech (T), hors familles (H).
- Pour écrire ou refaire les 30 premières secondes.
- Quand une vidéo paraît lente, agitée, confuse ou fatigante sans qu'on sache pourquoi.
- Pour poser chapitres et fin de vidéo, ou lire une courbe de rétention (skill §15).

Ne pas la lire pour un format court TikTok/Shorts/Reels (dégustation D et autres courts) : le hook et la rétention y sont notés sur 10 par le barème du skill §5.2 (adapté à la famille), qui ne vaut pas pour les vidéos longues. Ne pas la lire non plus pour l'identité visuelle (skill §6), les sous-titres (`formats-courts-verticaux.md` §4, skill §9), la couleur ou l'export.

**Hiérarchie (skill §1) :** brief de Cabezer, puis règles du skill, puis cette fiche, puis tutoriels. Chaque technique dit quand l'employer, quand l'éviter et pour quelles familles. Aucun chiffre de tutoriel n'est une règle.

**Limite de Claude.** Claude ne ressent pas l'ennui d'un spectateur et n'entend pas. Il remplace l'ennui par des mesures (durée des plans, coupes par minute, part de face caméra), des planches d'images, la transcription et la forme d'onde. Écrire « mesuré », « lu en transcription » ou « vu sur planche », jamais « écouté » pour une mesure, jamais « le rythme est bon » sans dire comment on le sait. L'écoute finale et la validation reviennent à Cabezer (skill §1, §3).

**Conventions.**
- Interface de Premiere et d'After Effects en anglais : le libellé anglais fait foi, le repère français suit entre parenthèses. Tout libellé non lu à l'écran est marqué « libellé à confirmer ».
- Aucun raccourci clavier tant qu'il n'a pas été lu dans Keyboard Shortcuts (Raccourcis clavier) ; sinon passer par le menu. Libellés et raccourcis lus : `Suivi/environnement-verifie.md` (`pilotage-environnement-reprise.md`), qui fait aussi foi pour les versions.
- Gratuits uniquement par défaut ; tout outil payant est signalé et attend l'accord de Cabezer.

**Statuts de preuve :**
- **[vérifié]** : lu dans une source primaire accessible (texte complet) ou recoupé par deux sources.
- **[extrait]** : seul le résumé d'une recherche a été lu (pages d'aide YouTube, presse) ; à traiter avec prudence.
- **[une source]** : un seul professionnel ou une seule page ; préférence, pas norme.
- **[testé ici]** : essayé en session sur un fichier synthétique, jamais sur un vrai projet de Cabezer.
- **[à vérifier]** : menu, raccourci ou fonction qui change selon la version.

## Sommaire

1. Le modèle de base · 2. Les 30 premières secondes · 3. Boucles ouvertes, payoff, re-hooks · 4. Squelette, rythme et montage long · 5. B-roll, mouvement, raccords · 6. Face caméra, texte · 7. Le son comme outil de rythme · 8. Chapitres et cartons · 9. Fin de vidéo et écran de fin · 10. Sur-montage, sujets graves, revue sans yeux · 11. Courbe de rétention · 12. Tableau par famille · 13. Affirmations écartées ou à vérifier · 14. Erreurs de débutant → réflexes de pro · 15. Liste de contrôle · 16. Décisions à demander · 17. Sources étudiées

---

## 1. Le modèle de base : promesse, clarté, élan

Un spectateur de YouTube part d'un clic. Il reste tant que trois choses tiennent : la vidéo fait ce que le titre et la miniature ont promis, il comprend ce qui se passe, il sent qu'il y a une suite. Tout le reste de cette fiche sert l'une des trois.

**Ce que YouTube mesure** (aide YouTube « moments clés de rétention » [extrait]) :
- Le rapport n'existe qu'au niveau d'une vidéo ; les données mettent 1 à 2 jours à apparaître. Les moments clés ne s'affichent que si la vidéo dure au moins 60 s et compte au moins 100 vues, et seulement s'ils sont détectés [extrait ; à vérifier].
- L'indicateur d'introduction donne la part des spectateurs encore présents après 30 s.
- Un pic signale un passage revu ou partagé (parfois par confusion). Un creux signale un passage quitté ou sauté. Les « moments forts » sont des passages où presque personne ne part. Une baisse progressive est normale.
- Le rapport ne dit jamais pourquoi. La cause est une hypothèse à poser sur la timeline.

**Principes partagés par au moins deux professionnels indépendants :**

1. **Confirmer le clic.** Montrer dans les 30 premières secondes ce que titre et miniature promettent (Hillier-Smith, qui reprend le principe du créateur qu'il critique ; Paddy Galloway). Voir §2.
2. **Efficace n'est pas rapide.** Hillier-Smith : l'efficacité se mesure à « combien tu me demandes de rester » contre « combien tu me supplies de rester ». Paddy Galloway rejette aussi la vitesse comme remède. Un montage trop nerveux empêche de comprendre, et le spectateur part.
3. **Chaque coupe a une raison :** émotion, information ou changement de point de vue (Hillier-Smith ; monteurs de *The Bear*).
4. **Raccorder le mouvement** d'un plan à l'autre (Hillier-Smith ; *The Bear*). Voir §5.2.
5. **Le son d'abord.** Hillier-Smith : on s'en sort avec de mauvaises images, pas avec un mauvais son. Paddy : beaucoup de spectateurs écoutent sans casque ou dans le bruit. Voir §7.
6. **Ne jamais juger un passage par la courbe seule.** Paddy : une section qui coûte 2 % peut en faire gagner plus loin ; il faut mieux la raconter, pas la supprimer.
7. **Se tester comme spectateur.** Paddy note l'ennui et fait un « test de distraction » (téléphone, bruit). Hillier-Smith : un lien incompris après cinq visionnages est un défaut de montage.

**Contre-exemple : MrBeast.** Le 3 mars 2024, il écrit sur X avoir ralenti ses vidéos et constaté une hausse des vues. Tubefilter compte 38 coupes sur une minute d'une vidéo de 2023 contre 23 sur une vidéo récente, sans prouver la cause [extrait ; deux vidéos comptées]. Retenir : le montage le plus nerveux n'est pas la seule voie. Ne pas retenir : « ralentir fait monter les vues ».

**Désaccord entre sources.** Film Booth donne en modèle 10 changements de plan en 20 s ; Hillier-Smith écrit « way too short, slow down » sur une ouverture rapide. Les deux marchent si chaque plan sert une seule idée et ne porte aucun texte à lire (temps de lecture, §6.3). Le repère de Film Booth est un constat sur un exemple, pas une règle.

---

## 2. Les 30 premières secondes

**Pourquoi :** le spectateur y décide si la vidéo tient sa promesse ; un début haché annonce une vidéo agressive (Hillier-Smith).

### 2.1 Aligner la promesse : deux obligations distinctes

Ne pas confondre confirmer et payer.

1. **Confirmer le sujet et la promesse avant la 30e seconde.** Le spectateur doit savoir de quoi parle la vidéo et ce qu'il va obtenir, montré ou dit, pas seulement suggéré. En Story, cette confirmation tombe dans l'intro face caméra (skill §6, Story).
2. **Rappeler l'enjeu ensuite, répondre à la fin.** L'enjeu peut revenir sous forme de question dans la première minute, sans y répondre ; la réponse arrive à la fin (S, P, F long : `documentaire-essai-video-archives.md` §3). Cela ne retarde pas la confirmation de l'obligation 1.

**Test de promesse** (à faire avant de monter l'ouverture) :
1. Relire titre et miniature validés, ou le brief (skill §3, étape 0). Écrire : « Le spectateur a cliqué pour voir ___. » Si ni titre ni miniature ni brief ne donnent la promesse, la demander à Cabezer ; en mode autonome, écrire la phrase la plus proche du brief, consignée « en attente de validation ».
2. Lister les 30 premières secondes plan par plan, avec ce que chacun apporte à cette phrase.
3. Couper ou remplacer tout plan qui n'y apporte rien.
4. Vérifier qu'à 30 s le sujet et la promesse ont été montrés ou dits.

**Réussite :** transcrire les 30 premières secondes (par fenêtres de 10 s qui se chevauchent, skill §5.2 pour la méthode de transcription) ; quelqu'un qui n'a vu que la miniature et ce texte retrouve la phrase écrite à l'étape 1. En Story, la transcription couvre l'intro face caméra.

**Quand l'abréger :** retouche ponctuelle d'une vidéo déjà validée. **Familles :** F, S, P, T, H ; pas D.

### 2.2 Remonter un passage fort en ouverture (Paddy Galloway)

Paddy remplace une intro faible par un passage plus fort pris plus loin et le relie à l'intro. Technique de tutoriel : la proposer à Cabezer, avec le passage candidat, et ne l'appliquer qu'avec son accord (réponse du 12/10/2026), seulement si ce passage correspond à ce qu'annonce la miniature.

1. Enregistrer sous une nouvelle version (skill §1). Dupliquer la séquence montée (clic droit dans le panneau Project, repère français : Projet ; libellé à confirmer) et travailler sur la copie.
2. Dans la transcription, repérer le passage ; poser un marqueur `HOOK:candidat` (menu Marker, repère français : Marqueur ; libellé à confirmer) et marquer entrée et sortie. Vérifier qu'il se comprend sans ce qui précède.
3. Le copier en tête de séquence par la commande d'insertion ou d'écrasement du menu Sequence (repère français : Séquence ; libellés à confirmer).
4. Écrire la liaison avec des phrases déjà tournées ; ne jamais recomposer une phrase ni créer par collage une affirmation que Cabezer n'a pas faite (skill §4 et §8).
5. Rejouer le passage à sa place d'origine ou justifier son absence (§3).
6. Sur chaque nouveau raccord, appliquer les règles de coupe : aucun mot coupé, sortie à l'extinction réelle du son, room tone si un trou apparaît (`audio-dialogue-sound-design-mixage.md` §3.1 et §7.1).

**À éviter :** un teaser qui spoile la chute ou ne se retrouve jamais dans la vidéo.
**Familles :** F (verdict ou réaction forte, si le dérush le contient) ; S seulement si Cabezer le valide (le récit chronologique est sa signature) ; T, P, H selon brief ; jamais D.

### 2.3 Repère de structure, 0-60 s (synthèse, non normative)

- **0-3 s :** image forte, promesse, son dès la première image.
- **3-30 s :** contexte, personne, enjeu ; pas de logo ni de présentation de chaîne qui retarde la promesse (Film Booth).
- **30-60 s :** preuve, première relance, première boucle ouverte.

**Contraintes de Cabezer prioritaires :**
- Story : la promesse est dite dans l'intro face caméra (skill §6, Story). Le générique « Amed Story » a été supprimé le 12/10/2026 (à refaire en entier) : aucun générique n'est posé tant que Cabezer n'en a pas validé un nouveau.
- Hook finalisé en dernier, une fois la structure stable (skill §3, étape Structure et habillage).
- Ne jamais écrire « Cabezer Story » dans un titre ou une carte (skill §6, Story). (Le générique « Amed Story » a été supprimé le 12/10/2026.)
- Demander le hook à Cabezer quand le brief ne le donne pas. En mode autonome : écrire le hook du test de promesse et le consigner « en attente ».

### 2.4 Pièges

- **Hook qui ne tient pas la promesse :** Paddy cite un début sur le golf, lent et peu clair, qui faisait chuter la courbe.
- **Hook trop nerveux pour le sujet** (§10.3), ou qui sert le monteur plutôt que le spectateur (« insecure editing », Hillier-Smith).
- **Confondre confirmer et répondre :** répondre dans les 30 secondes tue la boucle ; ne rien montrer de la promesse tue le clic.

---

## 3. Boucles ouvertes, payoff, re-hooks

**Principe :** annoncer un enjeu, le faire sentir, le fermer plus loin. Paddy déteste le « j'y reviendrai plus tard » dit trop vite : le spectateur n'a pas ressenti la difficulté. À la fin d'un sujet, il faut donner le suivant (un autre fil, une touche d'humour, du contexte). Les monteurs de *The Bear* posent dès les premiers plans des images qui reviennent (« tent poles »), comme le motif récurrent du skill (§4).

**Quand :** F, S, P, T, H. **Éviter :** D.

### 3.1 Procédure : marqueurs et audit

1. Nommer chaque marqueur de séquence `TYPE:clé`, types `PROMESSE`, `BOUCLE`, `PAYOFF`, `REHOOK`. Exemple : `BOUCLE:golf` à l'ouverture, `PAYOFF:golf` à la fermeture. Poser par le menu Marker (repère français : Marqueur ; libellé à confirmer), double-clic pour nommer.
2. Par script, au choix. Ne pas lancer un script sur le projet maître : l'essayer sur une copie (chaîne d'exécution et test de fumée : `pilotage-environnement-reprise.md`).
   - **UXP** (préféré pour un nouvel outil dans Premiere). Signatures vérifiées sur les définitions de types `@adobe/premierepro` 26.5.0 ; code non exécuté dans Premiere ; version minimale de l'API à vérifier par le test de fumée :
```javascript
const ppro = require("premierepro");
const projet = await ppro.Project.getActiveProject();
const sequence = await projet.getActiveSequence();
const marqueurs = await ppro.Markers.getMarkers(sequence);
projet.executeTransaction((action) => {
  action.addAction(marqueurs.createAddMarkerAction(
    "BOUCLE:golf", "Comment", ppro.TickTime.createWithSeconds(75)));
}, "Poser le marqueur BOUCLE:golf");
```
   Types acceptés d'après les définitions : `Comment`, `Chapter`, `Segmentation`, `WebLink`. Le temps est un `TickTime`, pas un nombre de secondes.
   - **ExtendScript**, tant que le test de fumée le confirme sur la machine : `var m = app.project.activeSequence.markers.createMarker(75.0); m.name = "BOUCLE:golf";` (secondes) [une source, guide de scripts Premiere non rouvert ; à tester sur une copie].
3. Auditer les boucles par la voie de secours XML : exporter la séquence en FCP XML (menu File > Export, repère français : Fichier > Exporter ; libellé à lire) puis lancer `xml-coupes.py` (jeu de scripts de `organisation-livraison-qc.md` §6 ; ne pas réécrire un script ici). Résultat attendu : pour chaque clé, un `BOUCLE` avant son `PAYOFF` avec l'écart en secondes ; `OUVERTE` pour une boucle sans payoff ; `ORPHELIN` pour un payoff sans boucle. Structure lue `<marker><name><in>` sous `<sequence>` [testé sur un XML synthétique, à confirmer sur un vrai export]. Si le script n'offre pas cet audit, l'ajouter à ce jeu, pas à cette fiche. Lire tout XML avec `python3 -I`.
4. Relire chaque ouverture : l'enjeu est-il senti (un plan qui laisse peser, une phrase) avant la promesse de retour ?
5. Écrire en une ligne ce qui donne envie du sujet suivant, à chaque fin de sujet.

**Réussite :** ni `OUVERTE` ni `ORPHELIN` ; chaque re-hook donne une raison concrète de rester.

### 3.2 Hypothèse à tester, pas une règle

Le mémo divulgué de MrBeast (authenticité non confirmée par son équipe) décrirait la première minute comme la plus importante et placerait des relances vers 3 et 6 minutes [une source, mémo non lu]. À comparer avec la courbe de Cabezer (§11), sans l'imposer.

### 3.3 Pièges

Boucle oubliée (première frustration citée par Paddy) ; re-hook factice (question sans réponse ni relance) ; aller-retour dans le temps non balisé : annoncer chaque bascule par un élément visuel (tenue, angle, date) ou sonore.

---

## 4. Squelette, rythme et montage long

### 4.1 Le squelette (Paddy Galloway)

Paddy liste les huit ou dix progressions de la vidéo, puis demande pourquoi chaque scène est là et si elle doit venir plus tôt ou plus tard. Avant de monter, remplir dans `Suivi/decisions.md` :

| Scène | Début | Durée | Ce que le spectateur doit comprendre | Émotion | Mouvement dominant | Son | Boucle |
|---|---|---|---|---|---|---|---|

La colonne 4 reprend la règle Story du skill (§6, « une image par idée » : écrire en une ligne ce que le spectateur doit comprendre). **Réussite :** aucune scène sans raison écrite ; deux scènes consécutives de même émotion sont justifiées ou réordonnées. **Familles :** F, S, P, T, H.

### 4.2 Le rythme suit l'état émotionnel

- *The Bear* : le calme vient après le chaos, le style revient au chaos quand l'histoire y revient ; fondus enchaînés pour le calme, coups d'énergie brefs (zoom rapide) avant les montages. Transposer l'idée, pas la recette : le skill réserve les transitions **visibles** aux changements d'argument ou de séquence (skill §7), donc le calme se construit par des plans tenus. En long, la coupe franche reste le défaut et les fondus sont rares (fin de Story ou sur demande) : un fondu enchaîné de calme, une coupe au noir ou un noir dans un gag ne se posent que sur demande de Cabezer, avec deux versions sur un extrait (réponse du 12/10/2026). Micro-fondus audio de 1 à 2 images et J/L-cuts sont permis s'ils ne mordent pas l'attaque d'un mot (`audio-dialogue-sound-design-mixage.md` §3.2 et §3.3) ; jamais sur la bouchée ou la réaction en dégustation.
- Flash et zoom de choc : repère WCAG facultatif dans `conformite-droits-accessibilite.md` ; aucun test de photosensibilité n'est imposé (réponse du 12/10/2026).
- Hillier-Smith aime les contrastes (« ping-pong, whiplash ») : seulement sur un changement de ton voulu.
- **Respirer.** Hillier-Smith conseille de rester sur le visage quelques secondes, puis d'élargir. En **Story**, le skill garde les respirations qui portent un regard, une émotion ou une attente construite et cette exception prime sur la coupe au dernier mot (skill §6). Elle est étendue aux **moments d'émotion de films/séries (P)**, au **verdict du food long (F)** et au Lifestyle posé (réponse du 12/10/2026, skill §4). **Ailleurs, la coupe du skill s'applique** (skill §4) : un blanc ne reste que s'il est occupé par un élément prévu (illustration, réaction d'une autre personne, ambiance du lieu), jamais vide. Aucune exception en dégustation ni en tech.
- **Montage par le texte.** Il sert à repérer et à pré-découper un assemblage ; chaque coupe est ensuite recalée à la forme d'onde et à l'énergie du son, jamais aux temps de transcription (skill §4, `premiere-pro-avance.md` §5.1). En Story, ne pas supprimer les pauses en masse.

### 4.3 Mesures : ce qu'elles disent et ce qu'elles cachent

- **ASL** (durée moyenne des plans) : durée totale divisée par le nombre de plans [extrait Cinemetrics]. Une moyenne masque l'alternance entre plans courts et longs.
- Cutting et collègues (160 films, 1935-2010) : les films se rapprochent d'un motif de variation des plans proche de celui de l'attention humaine, et ce motif est indépendant de la moyenne [extrait d'un article en accès libre]. Conséquence : ne pas viser une ASL ; surveiller la variété (médiane, plus long plan, coupes par minute par fenêtre).

**Scripts.** Les mesures passent par le jeu de scripts nommés de `organisation-livraison-qc.md` §6, jamais recopiés ici. Ils restent « testés sur fichiers générés » tant qu'ils n'ont pas tourné sur un vrai export de Cabezer (skill §20).
- **Sur le MP4 exporté** (ce que voit le spectateur) : `mesure-plans.py`, paramètres seuil de scène et fenêtre, sortie CSV. Demander ASL, médiane, plus long plan, coupes par minute par fenêtre de 60 s. Seuil de départ 0,3 : la doc ffmpeg du filtre `select` juge 0,3 à 0,5 « généralement raisonnable » [vérifié, `filters.texi`]. Il rate les fondus et peut prendre un flash pour une coupe : le calibrer sur une minute connue.
- **Sur la timeline Premiere** (avant export) : `xml-coupes.py` sur un export FCP XML (voie de secours, `premiere-pro-avance.md` §13). Pour la part de face caméra, nommer les clips concernés d'un motif commun (par exemple `facecam`) avant l'export et le passer au script. Règles de calcul à exiger : à chaque instant, le clip de la piste la plus haute compte ; deux clips contigus du même fichier sans trou dans la source ne forment qu'un plan. Limites [testé sur un XML synthétique] : transitions, clips imbriqués et multicam non gérés ; un `start` ou `end` à -1 signale un clip voisin d'une transition, à ignorer. Si l'option manque, l'ajouter au jeu de scripts.
- Seuils ffmpeg de blancs, noirs et figements : tableau « usage, commande, seuil » de `organisation-livraison-qc.md` §6. Ne pas les confondre avec la méthode étalonnée des blancs du skill §5.2, réservée à la note des dégustations.

### 4.4 Lire les mesures

1. Mesurer d'abord les deux ou trois meilleures vidéos de la famille (bonne courbe) : c'est la référence. Ne pas comparer des familles différentes.
2. Sur la vidéo à contrôler, repérer les fenêtres qui s'écartent de la référence, le plus long plan et les cinq plus longs passages face caméra.
3. Pour chacun, écrire pourquoi il est justifié (émotion, preuve à lire, explication) ou proposer une relance. Une mesure signale un cas ; elle ne le juge pas.

**Réussite :** chaque fenêtre atypique a une raison écrite dans `Suivi/`, et la vidéo alterne phases denses et phases tenues.

### 4.5 Montage long (20 à 40 minutes)

L'architecture d'un montage long (séquence maîtresse, séquences par chapitre, sessions, verrouillage par passes, proxys, rendus intermédiaires AE) est décrite dans `pilotage-environnement-reprise.md`. Ce que la rétention y ajoute :
1. Poser un marqueur de type `Chapter` au début de chaque chapitre, nommé du titre court (§8), et garder les marqueurs `BOUCLE`/`PAYOFF` dans la séquence maîtresse pour l'audit du §3.1.
2. À la fin de chaque chapitre terminé, produire l'aperçu léger avec timecode (`organisation-livraison-qc.md` §5.1) et prendre les mesures du §4.3 sur cet aperçu.
3. Avant la validation finale, refaire les mesures par fenêtres de 60 s sur le MP4 complet et comparer à la référence de la famille (§4.4).

**Familles :** F, S, P, T, H dès qu'une vidéo dépasse une vingtaine de minutes.

---

## 5. B-roll, mouvement, raccords

### 5.1 Un B-roll, une idée

Hillier-Smith : un B-roll a besoin d'une intention de récit ; il préfère un plan de drone à quatre plans rapides. C'est la méthode « une image par idée, jamais par mot » du skill (§6, Story). Sur le stock, les interlocuteurs ne s'accordent pas ; le skill tranche : rushs de Cabezer d'abord, compléments précis ensuite. Les plans stock libres de droits ont un accord général : téléchargés sans redemander, licence consignée dans `Suivi/licences.csv`, signalés à Cabezer ; toute autre vidéo à télécharger demande son accord (skill §6, §8, `conformite-droits-accessibilite.md`).

### 5.2 Raccorder le mouvement

**Règle :** garder la même direction de mouvement sur trois plans consécutifs d'un même lieu, ou la casser à dessein. Hillier-Smith : de gauche à droite puis de droite à gauche fait sursauter ; des mouvements cohérents adoucissent la coupe (*The Bear* fait de même). **Familles :** F, S, P, T, H.

**Contrôle (Claude) :**
1. Extraire une planche autour de la coupe (`fondamentaux-montage-narratif.md` §18.3).
2. Noter pour chaque plan la direction du mouvement et l'échelle.
3. Si deux directions opposées se suivent sans motif, réordonner ou choisir une autre prise. Ne pas retourner l'image d'un lieu réel.

**Réussite :** aucune inversion non voulue sur trois plans de suite.

### 5.3 Mouvement sur une image fixe : désigner ou présenter, jamais décorer

**Statut (skill §1, §16).** Un mouvement sur une photo ou une capture sans texte à lire est un traitement de plan : il se fait **dans Premiere**. Tout élément créé (surlignage, entourage, flèche, étiquette, schéma) est une animation graphique : **dans After Effects**, en calques natifs. Un document ou une page à lire s'explore dans AE (caméra 3D, surlignage) : `documentaire-essai-video-archives.md` §5.2, `after-effects-motion-design.md` §10.

**Règle commune :** le mouvement désigne un détail au moment où la voix le nomme, ou présente un visage (partir du bas d'une photo vers le visage). Il laisse un temps fixe avant et après, suit une courbe douce, et ne s'exécute jamais sur un plan qui porte un texte à lire. La dérive purement décorative (poussée lente sur chaque photo) est exclue dans toutes les familles. L'échelle de 115-120 % de Film Booth n'est plus un défaut [une source].

**Quand :** photo, capture ou archive qui doit durer plus de 2 ou 3 s et dont un détail compte pour ce que dit la voix. **Éviter :** photo de fond sans désignation, même mouvement sur plusieurs photos de suite, plan déjà animé, plan portant un texte, insert de bouchée.

**Familles :**
- S et P : désignation d'un détail, présentation d'un visage (`documentaire-essai-video-archives.md` §6.4).
- F, T, H : désignation seulement, cas rare.
- D : non (le hook de dégustation n'emploie pas de photo, skill §5).

**Procédure Premiere** (interface en anglais ; libellés à confirmer à l'écran) :
1. Effect Controls (Contrôles d'effets) > Motion (Mouvement) : Position et Scale (Échelle).
2. Placer la tête de lecture un peu après le début du plan (pause initiale d'au moins 0,5 s, valeur de départ de `documentaire-essai-video-archives.md` §6.4) et activer les chronomètres de Position et d'Échelle.
3. Avancer sur le mot qui désigne le détail et changer la valeur : Premiere crée l'image clé. Garder l'échelle finale dans la définition de la source ; vérifier qu'aucun bord de l'image n'apparaît (une source 4K dans une séquence 1080p laisse environ 200 % de marge selon Film Booth [une source ; à mesurer]).
4. Pour la pause après le mouvement, dupliquer l'image clé avec le bouton d'ajout, jamais en recliquant le chronomètre (il efface les clés).
5. Lisser : clic droit sur les clés > Temporal Interpolation > Auto Bezier ou Continuous Bezier (repère français : Interpolation temporelle > Bézier automatique ou continu ; libellés à confirmer). Jamais linéaire pour un mouvement progressif (skill §7).
6. Lire à vitesse réelle : un mouvement qui paraît rapide paraît mauvais (Film Booth).

**Réussite :** le détail désigné est net et lisible quand la voix le nomme ; le mouvement se sent sans se voir ; l'arrivée est douce.

### 5.4 Pièges

Zoom ou dérive sur chaque plan (le zoom façon Micode n'est permis que si le moment le demande, skill §7) ; mouvement ajouté à un plan qui bouge déjà ; tous les plans dans la même direction pendant 30 s ; animation graphique faite dans Premiere au lieu d'AE.

---

## 6. Face caméra, texte

### 6.1 Éviter les tunnels

Film Booth cible peu de face caméra à l'ouverture (18 s sur 60 dans son exemple) : règle personnelle, pas norme. En Story, le skill valorise le visage (5 à 27 s, skill §6). Appliquer partout :

1. Lister les cinq plus longs passages face caméra continus (§4.3).
2. Pour chacun : le spectateur a-t-il autre chose à regarder que ce qu'il entend ? Un visage qui porte une émotion, un aveu ou une nuance est une raison de tenir.
3. Sinon, relancer sans surcharger : changement de valeur de plan, insert qui explique, document ou capture réels, ambiance. Une relance qui n'explique rien est du bruit.

Ne jamais couvrir de B-roll un moment que Cabezer porte par son regard (skill §4). **Familles :** F, S, P, T, H.

### 6.2 Cadrage et gestes

Film Booth : un cadrage trop serré coupe les mains. Le skill protège déjà yeux, mains et gestes au recadrage (skill §3).

### 6.3 Texte à l'écran

- **Mots-clés incrustés** (Film Booth) : quelques mots qui renforcent ce qui est dit. **Quand :** F et T, si la charte de la famille le permet (skill §6) ; H selon brief. **Éviter :** S et P, car le skill réserve titres et cartons à un concept, une date ou un chapitre. D : voir skill §5.1 (étiquettes, pop-ups), hors de cette fiche.
- **Texte réel :** filmer un panneau, une page, un menu et le laisser lisible (compatible avec la preuve réelle de la Story).
- **Temps de lecture** la formule `max(1,5 s ; 1 s + caractères/15)` du skill s'applique aux mots-clés incrustés, cartons, traductions et blocs de sous-titres des familles longues ; une preuve reste au moins 3 s, une image sans texte au moins 2 s, un univers visuel suivi 2 à 3 s. Elle ne vaut ni pour les sous-titres mot à mot des courts ni pour les coupes rapides nommées (0,4 à 0,8 s) de la Story. Détail : `documentaire-essai-video-archives.md` §5.3.
- **Ton du graphisme :** une carte très léchée sur un sujet grave fait perdre confiance ; il suit l'identité de la famille.
- Toute animation de texte se fait dans After Effects en calques natifs (skill §16). Typographie française à l'écran (espaces avant « : », « ? », « ! », guillemets) : `conformite-droits-accessibilite.md`.

**Montrer plutôt que dire :** Film Booth et Hillier-Smith convergent ; le skill règle l'application en Story (preuve, univers suivi, schéma, visage) et interdit d'illustrer littéralement une métaphore (skill §6, Story).

---

## 7. Le son comme outil de rythme

Complète la passe de mixage (skill §11) sans la remplacer. Les valeurs de loudness (−14 LUFS intégrés = repère de contrôle à ±1, crête vraie ≤ −1 dBTP) et le ducking sont dans `audio-dialogue-sound-design-mixage.md` §9 et §5.4, jamais ici.

### 7.1 Intelligibilité d'abord

1. **Mesurer** le MP4 exporté avec les commandes de `audio-dialogue-sound-design-mixage.md` §10 (niveau intégré, crête vraie, compatibilité mono) et lister les trous de son à examiner avec le tableau de `organisation-livraison-qc.md` §6. Consigner niveau intégré et crête vraie comme repères, non comme cibles (skill §13).
2. **Demander à Cabezer l'écoute finale** au casque, au haut-parleur du téléphone, puis sur téléviseur si possible. Claude n'entend pas : il ne déclare jamais le mix « écouté » ni « validé » (skill §11).
3. Pourquoi le téléviseur : YouTube représentait 11,6 % du temps passé devant la télévision aux États-Unis en février 2025 selon Nielsen [extrait ; chiffre américain].

**Réussite :** chaque phrase se comprend sans effort au haut-parleur du téléphone, d'après le retour de Cabezer.

### 7.2 Ambiance par lieu

Hillier-Smith : si un lieu est présenté comme vivant, chaque plan de ce lieu doit porter son son ; une image muette dans un lieu sonore se remarque. Poser l'ambiance **avant** le premier plan du lieu, avec fondu d'entrée, et la tenir sur toute la scène (skill §11, `audio-dialogue-sound-design-mixage.md` §7.2). La prendre dans les rushs du lieu, sinon dans une banque dont la licence est consignée.
**Familles :** F, S, P, T, H. **D :** aucune ambiance continue ni musique ; une ambiance discrète du lieu sous un insert muet est à proposer au premier usage et n'est posée qu'avec l'accord de Cabezer (réponse du 12/10/2026).

### 7.3 Son provisoire pour couper plus tôt

*The Bear* : un petit bruitage sous l'image permet de quitter le plan plus vite, car le spectateur relie l'action. **Quand :** gestes et objets en F et T, avec la bibliothèque ouverte (skill §11). **Éviter :**
- Story : pas de bruitage d'objet gratuit (skill §11).
- Foley d'aliment : jamais (réponse du 12/10/2026), ni sur une bouchée ni sur une réaction.
- Tout SFX doit rester audible sous la voix.
- Caler le SFX sur l'attaque de l'événement, un swoosh sur son pic, sans essai A/B (réponse du 12/10/2026).

### 7.4 Contraste sonore, faux sons, musique

- Hillier-Smith emploie un son décalé pour renforcer une image. Film Booth avertit que de faux bruitages dans un contenu personnel font perdre la confiance : en S, P et documentaire, aucun faux son présenté comme venant de la scène.
- Hillier-Smith cherche d'abord la sensation de la scène, puis la musique. Sa recommandation d'une bibliothèque musicale est un partenariat : ne pas la suivre. Les règles musicales du skill priment (skill §11) ; un morceau fini garde sa vitesse d'origine.

---

## 8. Chapitres et cartons

**Sources :** Hillier-Smith répond « no title » à la question d'un carton de titre sur une vidéo d'environ 10 minutes (quelques secondes perdues). Paddy termine un chapitre en amorçant le suivant.

**Règle de Cabezer.** Le skill montre le carton de chapitre seul environ 3 s, sans voix, avec la signature musicale, et le déchire quand la voix reprend (skill §6, Story). C'est une signature validée par Cabezer pour la **Story** : la garder. Hors Story, aucun carton de chapitre à l'écran : les chapitres vont dans la description YouTube (`youtube-publication-package`) et en marqueurs de séquence (réponse du 12/10/2026). Le titre que Cabezer prononce n'est pas un chapitre.

### 8.1 Procédure (carton de chapitre, Story)

1. Couper dans le silence après la phrase de conclusion.
2. Carton seul d'environ 3 s avec la signature musicale, déchiré quand la voix reprend. Le carton est une animation graphique : composition After Effects en calques natifs (skill §16).
3. Jamais pendant une phrase clé.
4. Poser un marqueur de séquence au début de chaque chapitre, nommé du titre court (type `Chapter` si posé par UXP, §3.1).

### 8.2 Chapitres de la description YouTube

Selon des guides tiers (page d'aide non lue) : premier horodatage à 0:00, au moins trois horodatages, au moins 10 s par chapitre, ordre chronologique ; les guides divergent sur la couverture à 100 % [extrait ; à vérifier]. La rédaction relève de `youtube-publication-package`.

### 8.3 Mesurer l'effet d'un carton

Une vidéo ne tranche pas : relever la rétention avant et après chaque carton sur plusieurs vidéos de la famille, avec et sans carton (skill §15).

---

## 9. Fin de vidéo et écran de fin

- **Laisser respirer.** Une fin coupée sèchement ne donne pas de conclusion (échange dans la critique de Hillier-Smith). En Story, le skill est précis : regard silencieux à la caméra, accord réel qui s'éteint, fondu au noir avant que Cabezer bouge, aucun bruitage, pas de carton d'abonnement (skill §6, Story).
- **Écran de fin** [extrait de l'aide YouTube ; à vérifier sur la page en cours] : 5 à 20 dernières secondes, vidéo d'au moins 25 s, jusqu'à quatre éléments en 16:9 (les autres ratios peuvent en limiter le nombre) ; il masque les teasers de cartes et le filigrane ; indisponible pour les vidéos conçues pour les enfants. Gabarits et tailles : lire la page d'aide.
- **Au montage :** aucune information utile, texte ou animation essentielle dans les 20 dernières secondes. Garder un fond calme sur ces 5 à 20 s réservées ; les éléments à poser sont indiqués par `youtube-publication-package` (réponse du 12/10/2026). Cet écran n'est pas un carton d'abonnement dans l'image : il ne contredit pas la fin silencieuse de la Story.

**Réussite :** si l'on masque mentalement les 20 dernières secondes, aucune chute ni aucun appel au commentaire n'est perdu ; l'appel au commentaire protégé par le skill (§4) reste entier et audible.
**Familles :** F, S, T, H ; P selon brief ; jamais en court, où l'appel au commentaire tombe dans les 5 dernières secondes et la coupe se fait à l'extinction de la voix (skill §4).

---

## 10. Sur-montage, sujets graves, revue sans yeux

### 10.1 Signaux

Hillier-Smith et Paddy décrivent le même travers : tout jeter au spectateur par peur de l'ennui. Signaux : retours en arrière pour comprendre ; plans qu'on n'a pas le temps de regarder ; lien entre deux scènes qui échappe ; zoom, texte ou whoosh à chaque phrase. Aucun seuil dans les sources : comparer à la référence (§4.4).

### 10.2 Revue sans yeux (Claude)

1. Transcrire par fenêtres de 10 s qui se chevauchent (skill §5.2), regrouper par fenêtres de 60 s, et écrire une ligne par fenêtre : « le spectateur comprend ___ ». Une fenêtre impossible à résumer est un problème de clarté.
2. Produire une planche de contact (une image toutes les 2 s) avec la commande de `organisation-livraison-qc.md` §6.3, en changeant l'intervalle. Chercher les séries d'images quasi identiques (tunnel) et les changements de cadre trop fréquents.
3. Mesures (§4.3) et revue des cinq plus longs tunnels (§6.1).
4. Test de distraction de Paddy, adapté : chaque phrase doit rester compréhensible sans l'image qui l'accompagne.
5. Dire ce qui a été vu, lu en transcription, mesuré. L'écoute et la validation appartiennent à Cabezer (skill §3, revue du MP4).

### 10.3 Sujets graves

Hillier-Smith juge inappropriées les tactiques de rétention sur un reportage de guerre ; le créateur critiqué voulait éviter un ton manipulateur et reconnaît l'équilibre difficile. **Pour Cabezer :** sur un sujet grave (santé, drame, décès, injustice), retirer les effets de pure attention (zoom de choc, whoosh, texte qui claque), tenir les plans qui portent l'émotion, garder la musique en retrait. Appliquer la règle des respirations (skill §4, §6) : en Story, aux moments d'émotion de films/séries et au verdict du food long. Ne pas utiliser la détresse d'une personne comme hook ; droit à l'image et intervenants : `conformite-droits-accessibilite.md`.

---

## 11. Courbe de rétention et boucle post-publication

Détaille le skill §15. Une courbe est un signal, jamais une cause.

1. **Obtenir la courbe** : Cabezer l'envoie depuis YouTube Studio (Content > la vidéo > Analytics, onglet Engagement ; libellés à vérifier), 1 à 2 jours au moins après publication. Pas de vidIQ (réponse du 12/10/2026).
2. **Comparer** à ses propres vidéos de la même famille et de durée proche. Le graphique relatif de YouTube compare à des vidéos de durée similaire [extrait, deux sources] sans dire si le niveau est bon pour sa niche. Un pourcentage seul n'a pas de valeur absolue.
3. **Marquer** les cinq plus grosses baisses et les pics, retrouver le timecode dans le montage publié (projet versionné) et extraire une planche autour de chaque point (commande de planche de `organisation-livraison-qc.md` §6.3, avec `-ss` au timecode et `-t 20`).
4. **Noter** pour chaque point ce qui se passe à l'image et au son, et une seule hypothèse (confusion, passage long, son, carton, relance absente, sujet, sponsor), marquée « hypothèse ». Calculer coupes par minute et plus long plan autour du point (§4.3).
5. **Proposer une règle** à Cabezer seulement quand la même observation revient sur plusieurs vidéos de la même famille (skill §15, statut des méthodes au skill §20).

| Forme | Lecture prudente | À vérifier dans le montage |
|---|---|---|
| Chute dans les 30 premières secondes | Promesse non confirmée ou ouverture lente | Test de promesse (§2.1), son, première image |
| Baisse régulière | Normale sur YouTube | N'agir que si plus raide que la référence |
| Pic | Passage revu ou partagé, parfois par confusion | La phrase est-elle claire ? |
| Moment fort | Passage où presque personne ne part | Qu'a-t-il de commun avec les autres vidéos de la famille ? |
| Creux net | Passage quitté ou sauté | Plan long, carton, sponsor, son, explication longue |
| Chute dans les dernières secondes | Fin perçue comme finie | Appel au commentaire, écran de fin (§9) |

Pièges : un pic n'est pas toujours un succès ; la rétention dépend aussi du sujet, de la miniature et de la diffusion (Paddy).

---

## 12. Tableau par famille

| Technique | Dégustation courte (D) | Food long (F) | Story (S) | Films/séries PRISME (P) | Tech (T) | Hors familles (H) |
|---|---|---|---|---|---|---|
| Confirmer sujet et promesse avant 30 s (§2.1) | Non (skill §5.2) | Oui | Oui, dans l'intro | Oui | Oui | Oui |
| Rappel de l'enjeu en question, réponse à la fin (§2.1) | Non | Oui | Oui | Oui | Selon brief | Selon brief |
| Remonter un passage fort (§2.2) | Non | Oui, avec accord | Si Cabezer le valide | Selon brief | Selon brief | Selon brief |
| Boucles, re-hooks, squelette (§3, §4.1) | Non | Oui | Oui | Oui | Oui | Oui |
| Mesures de rythme (§4.3) | Voir skill §5.2 | Oui | Oui, avec prudence | Oui | Oui | Oui |
| Mouvement sur image fixe qui désigne (§5.3) ; dérive décorative : jamais | Non | Rare | Oui | Oui | Rare | Rare |
| Mots-clés incrustés (§6.3) | Voir skill §5.1 | Si la charte le permet | Non | Non | Si la charte le permet | Selon brief |
| Ambiance par lieu (§7.2) | Proposée au premier usage ; sans accord, non | Oui | Oui | Oui | Oui | Oui |
| Carton de chapitre de 3 s (§8) | Non | Non, chapitres dans la description | Oui (signature) | Non, chapitres dans la description | Non, chapitres dans la description | Non, chapitres dans la description |
| Respiration au-delà de la coupe du skill (§4) | Non | Oui, au verdict | Oui (skill §6) | Oui, moments d'émotion | Non | Selon brief ; Lifestyle posé : oui |
| Libérer les 20 dernières secondes (§9) | Non | Oui | Oui | Selon brief | Oui | Oui |

---

## 13. Affirmations écartées ou à vérifier

Ne pas reprendre sans nouvelle vérification :
- **Paddy Galloway :** 88 % de rétention à 30 s, perte moyenne de 30 à 40 %, 3 000 à 5 000 courbes, 2 ou 10 milliards de vues (deux entretiens se contredisent), CTR des premières heures prédictif, 5 à 10 % de vidéos tendance. La technique (§2.2) est retenue, pas les chiffres.
- **Film Booth :** 85 % de rétention pour MrBeast ; « un tiers de face caméra » et « aucun plan au-delà de 3 s » (constats sur un exemple) ; l'expérience des bras attachés ; la règle 7-38-55 appliquée à toute communication ; une citation attribuée à Casey Neistat dont l'auteur doute ; l'échelle de 115-120 % comme défaut sur plan fixe (§5.3).
- **Hillier-Smith et son interlocuteur :** 65 % de vues sur téléviseur, 40 000 $ de bibliothèque d'effets, règle de 15 s de conversation sans image. **Murch :** pondérations 51/23/10/7/5/4 % (synthèses ; livre non lu), « 70 % rythme » (non retrouvé).
- **Presse sur Cutting :** moyenne de 12 s en 1930 à 2,5 s aujourd'hui (seule la tendance est retenue). **MrBeast :** causalité ralentissement-vues ; contenu exact du mémo. **Outils payants** des sources (LIT, One of 10, Riverside) : aucun n'est requis.
- **Premiere :** touches par défaut de Lift et d'Extract (sources contradictoires ; ne lire que les raccourcis de l'application). Détection automatique des pauses du panneau Texte : instable, un rapport de bug de la communauté Adobe signale une régression entre les versions 26.0.2 et 26.3 [extrait ; à vérifier sur sa version] ; couper à la forme d'onde (skill §4). Extension générative (Generative Extend) : seulement sur demande explicite ; « Améliorer la parole » (Enhance Speech) : interdit par défaut (skill §16).
- **YouTube :** tailles des gabarits d'écran de fin, élément vidéo obligatoire, couverture des chapitres à 100 %.

---

## 14. Erreurs de débutant → réflexes de pro

| Erreur de débutant | Réflexe de pro |
|---|---|
| Couper de plus en plus vite pour « retenir » | Écrire ce que chaque coupe apporte ; mesurer la variété, pas la vitesse (§1, §4.3) |
| Annoncer la promesse sans la confirmer, ou répondre dès les 30 premières secondes | Confirmer sujet et promesse avant 30 s, garder la réponse pour la fin (§2.1) |
| Faire un teaser qui spoile ou disparaît | Remonter un passage réel avec l'accord de Cabezer, le relier, le rejouer à sa place (§2.2) |
| Dire « on y reviendra » trop vite | Faire sentir l'enjeu, marquer la boucle, vérifier le payoff (§3) |
| Supprimer la scène qui fait baisser la courbe | Mieux la raconter ; juger son effet plus loin (§1, §11) |
| Viser une ASL ou un nombre de coupes | Comparer à ses meilleures vidéos ; regarder la variété (§4.4) |
| Couvrir un tunnel par n'importe quel B-roll | Relancer avec un plan qui explique ou prouve (§6.1) |
| Pousser ou faire dériver chaque photo | Un mouvement seulement pour désigner un détail ou présenter un visage, avec pause avant et après (§5.3) |
| Faire un surlignage ou une flèche dans Premiere | Animation graphique dans After Effects, en calques natifs (§5.3) |
| Supprimer toutes les pauses avec le montage par le texte | Pré-découper, puis recaler chaque coupe à la forme d'onde (§4.2) |
| Dire que le mix est « écouté » après une mesure | Mesurer, puis demander l'écoute de Cabezer (§7.1) |
| Tirer une règle d'une seule courbe | Poser une hypothèse ; attendre la répétition sur la famille (§11) |

---

## 15. Liste de contrôle

**Avant le montage**
- [ ] Phrase de promesse écrite, comparée au titre et à la miniature (ou au brief) ; sinon « en attente ».
- [ ] Squelette rempli ; famille identifiée ; règles du skill relues pour elle.

**Ouverture et structure**
- [ ] Sujet et promesse confirmés avant la 30e seconde (dans l'intro face caméra en Story) ; son dès la première image ; hook finalisé en dernier.
- [ ] Marqueurs `BOUCLE`/`PAYOFF` audités (§3.1) : aucune boucle ouverte, aucun payoff orphelin ; chaque fin de sujet donne une raison d'attendre la suite.
- [ ] Chapitres posés selon la famille (carton de 3 s à l'écran en Story seulement ; ailleurs, chapitres dans la description), marqueurs nommés.

**Rythme et son**
- [ ] Mesures prises sur l'export ; fenêtres atypiques justifiées dans `Suivi/` ; cinq plus longs passages face caméra justifiés ou relancés.
- [ ] Mouvements raccordés et doux ; mouvement sur image fixe seulement pour désigner ou présenter, jamais sur un texte ; temps de lecture respecté (§6.3).
- [ ] Niveau intégré et crête vraie consignés comme repères ; écoute finale demandée à Cabezer ; ambiance par lieu ; SFX audibles sous la voix.

**Fin**
- [ ] Rien d'essentiel dans les 20 dernières secondes ; appel au commentaire entier ; fin non coupée sèchement.

**Après publication**
- [ ] Courbe comparée à la famille ; cinq baisses reliées à la timeline ; hypothèses marquées.
- [ ] Aucune règle nouvelle sans répétition sur plusieurs vidéos.

---

## 16. Décisions à demander

> **Toutes ces questions ont reçu une réponse de Cabezer le 12/10/2026** : voir `../decisions-en-attente.md`, qui prime sur tout autre passage.

| Question tranchée | Réponse de Cabezer |
|---|---|
| Étendre l'exception des respirations de la Story aux moments d'émotion des films/séries et au verdict d'un food long ? | Oui : respirations gardées dans les deux cas (et au Lifestyle posé). |
| En dégustation, autoriser une ambiance discrète du lieu sous un insert muet ? | À proposer au premier usage ; sans accord, aucune ambiance continue ni musique. |
| Autoriser un foley d'aliment en vidéo longue ? | Jamais. |
| Teaser « passage fort remonté en ouverture » (§2.2) en food long et en Story ? | Proposé avec le passage candidat, appliqué seulement avec l'accord de Cabezer. |
| Ajouter un carton de chapitre hors Story ? | Non : chapitres dans la description. |
| Qui pose l'écran de fin (éléments cliquables) ? | 5 à 20 s réservées au montage ; éléments indiqués par `youtube-publication-package`. |
| Utiliser vidIQ pour récupérer la courbe ? | Non : Cabezer envoie la courbe depuis YouTube Studio. |

## 17. Sources étudiées

**Réseau de la session.** Les pages d'aide YouTube et Adobe, developer.adobe.com, docsforadobe.dev, Wikipedia, Passionfruit, Cinemetrics et la presse n'ont pas pu être ouvertes (refus du proxy ou échec DNS) : elles sont citées en « extrait » (résumé d'une recherche). Les textes du registre npm et de GitHub brut ont été lus en entier.

### Transcriptions lues en entier (sous-titres automatiques ; citations approximatives)

| Auteur | Titre | URL | Couverture |
|---|---|---|---|
| Paddy Galloway (The Editing Podcast) | Paddy Galloway Reveals The #1 YouTube Editing Error To Avoid | https://www.youtube.com/watch?v=Q0zRBsYQnA0 | transcription lue ; chiffres non vérifiés |
| Hayden Hillier-Smith | When Editing Ruins Your Video | https://www.youtube.com/watch?v=IROKEjmIIlM | transcription lue ; sponsor |
| Hayden Hillier-Smith (The Editing Podcast) | Optimize Your Editing for YouTube With HillierSmith | https://www.youtube.com/watch?v=eboQ7R34Ums | transcription lue (7 déc. 2022) |
| Joanna Nagel, Adam Epstein (The Editing Podcast) | Asking The Bear Editors How They Cut With INTENSITY | https://www.youtube.com/watch?v=fox4gyOYVpE | transcription lue ; fiction, transposition partielle |
| Film Booth | The Silent Hack YouTubers Use To Hook You | https://www.youtube.com/watch?v=IaWRqyOtUUQ | transcription lue (2022) |
| Film Booth | Can't Hit 57% YouTube Video Retention? TRY THIS | https://www.youtube.com/watch?v=YwbPVcGQT5s | transcription relue (2021) |
| Film Booth | Editing Hacks YouTubers Use To Hook You | https://www.youtube.com/watch?v=sZ4t7fJXnT0 | transcription lue |
| Jay Clouse (avec Paddy Galloway) | Meet the Man Who Solved YouTube | https://www.youtube.com/watch?v=HEiAiPGatwc | transcription lue |

Non obtenues : Hillier-Smith « 10x deeper » (mPhhBgTIG2Y), Jon Youshaei (h-8C3bntQRo), Aprilynne Alter (TOHQXdCAo5k). Aucun entretien de monteur francophone trouvé.

### Textes techniques lus en entier

| Auteur | Sujet | URL | Couverture réelle |
|---|---|---|---|
| Adobe | Définitions de types UXP, paquet `@adobe/premierepro` 26.5.0 (Apache-2.0) | https://registry.npmjs.org/@adobe/premierepro/-/premierepro-26.5.0.tgz | `src/premierepro.d.ts` lu aux sections Markers, Marker, executeTransaction, TickTime (signatures du §3.1). Aucun code exécuté dans Premiere. |
| FFmpeg | Documentation des filtres, `doc/filters.texi` (master) | https://raw.githubusercontent.com/FFmpeg/FFmpeg/master/doc/filters.texi | Section `select` : seuil de scène entre 0 et 1, 0,3 à 0,5 « sane » (§4.3). |

### Pages (extraits de recherche)

| Auteur | Sujet | URL | Retenu |
|---|---|---|---|
| YouTube Help | Moments clés de rétention | https://support.google.com/youtube/answer/9314415 | Indicateur à 30 s, pics, creux, moments forts, délai, niveau vidéo, seuils 60 s et 100 vues (à vérifier) |
| YouTube Help | Écrans de fin | https://support.google.com/youtube/answer/6388789 | 5-20 s, 25 s minimum, 4 éléments en 16:9 |
| YouTube Help | Chapitres | https://support.google.com/youtube/answer/9884579 | Règles relayées par des guides tiers (Storyblocks, Dickinson College, entre autres) ; page non lue |
| Tubefilter | MrBeast et son style de montage | https://tubefilter.com/2024/03/04/mrbeast-editing-style-number-of-cuts-per-video/ | Message du 3 mars 2024, coupes |
| Passionfruit | Mémo divulgué de MrBeast | https://passionfru.it/mrbeast-leaked-document-81151/ | Première minute, relances ; mémo non lu |
| Adobe Community | Régression des pauses en 26.3 | https://community.adobe.com/bug-reports-728/text-based-editing-pause-detection-has-regressed-between-premiere-pro-26-0-2-build-2-and-26-3-1628855 | Instabilité (à vérifier) |
| Cutting et al. ; Cinemetrics | Longueur des plans ; ASL | https://pmc.ncbi.nlm.nih.gov/articles/PMC3485803/ ; https://cinemetrics.uchicago.edu/article/616e7ecc-7915-4768-b84d-7dec79aa77c2 | Variation des plans ; définition de l'ASL |
| Cord Cutters News (Nielsen) | YouTube à 11,6 % du temps TV | https://cordcuttersnews.com/youtube-dominated-tv-viewership-with-a-record-11-6-share-of-tv-viewing-bigger-than-disney-netflix-more/ | Chiffre américain, février 2025 |

**Scripts.** Ceux de la version précédente (plans, boucles, face caméra) ont migré vers le jeu de `organisation-livraison-qc.md` §6 ; ils restent « testés sur fichiers générés » (skill §20).
