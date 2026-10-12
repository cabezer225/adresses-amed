# Montage food et tech : ce que font les meilleurs créateurs

Fiche de référence pour monter des vidéos food et tech comme un professionnel, dans le cadre des règles de Cabezer. Dernière vérification : 12/10/2026. La version de Premiere ou d'After Effects lue dans l'application fait foi (table des versions et test de fumée : `pilotage-environnement-reprise.md`).

## Quand lire cette fiche

Lire cette fiche avant de monter ou d'habiller une vidéo food (dégustation, duel d'adresses, street food, recette) ou tech (test de produit, explication, capture d'écran), ou avant d'emprunter une technique à ces créateurs : rampe de vitesse, accéléré de préparation, arrêt sur image sur un détail, plan macro, compteur ou jauge, zoom sur une capture, son de cuisine, étalonnage de nourriture.

Elle ne remplace jamais le brief de Cabezer ni le skill (§1 : brief, skill, fiches, tutoriels). Pour chaque technique, elle dit quand l'utiliser, quand l'éviter et pour quelles familles : dégustation (D), food long (F), Cabezer Story (S), films/séries PRISME (P), tech (T), hors familles (H). Elle renvoie aux fiches Premiere, After Effects, audio, couleur et formats courts au lieu de les répéter.

## Sommaire

1. Ce que valent les sources, et comment s'en servir
2. Principes partagés par les meilleurs créateurs
3. Food : structure, réaction, image, son
4. Food et tech : vitesse, arrêt sur image, recadrage, texte, couleur
5. Tech : process, plans produit, captures, interfaces
6. Tech : schémas, chiffres, compteurs, jauges
7. Piloter et contrôler
8. Outils payants et dépendances de version
9. Matrice famille × technique
10. Erreurs de débutant → réflexes de pro
11. Liste de contrôle
12. Décisions à demander à Cabezer, et tests à faire
13. Sources étudiées

---

## 1. Ce que valent les sources, et comment s'en servir

**Niveaux de preuve** (utilisés partout) :
- **[Tuto]** : transcription lue en entier. Valeur d'auteur, jamais règle universelle. Transcription automatique : noms propres possiblement faux, minutes à ± 30 s, aucune image examinée.
- **[Doc dev Adobe]** : référence développeur lue (dépôts `AdobeDocs/uxp-premiere-pro` et `uxp-after-effects`). Elle prouve ce que l'API permet, pas les menus ni sa stabilité sur sa version.
- **[Mesure]** : commande exécutée sur un fichier de test synthétique (ffmpeg 6.1.1, 12/10/2026). Elle prouve le filtre, pas Premiere.
- **[Extrait]** : résumé de résultat de recherche web, page non ouverte. Indice à confirmer, jamais preuve.
- **[Métier]** : pratique courante, sans source. Valeur de départ à régler sur le plan réel.
- **[À vérifier]** : non confirmé. Tester sur sa version avant usage.

**Limite majeure.** Les pages d'aide d'Adobe sont inaccessibles ici (refus du proxy) : aucun menu ni raccourci n'est confirmé par l'aide officielle. Libellés : nom français, anglais entre parenthèses, « libellé à confirmer » tant qu'il n'est pas lu à l'écran. Un raccourci n'est utilisé qu'après lecture dans Raccourcis clavier ; ceux cités ici sont « à confirmer », le menu fait foi. Consigner les libellés lus dans `Suivi/environnement-verifie.md`.

**Pourquoi.** Ces créateurs ont des équipes et des budgets que Cabezer n'a pas : retenir le principe, pas le geste.

**Autorité** (jugement) : forte pour MKBHD, Mythical Kitchen, Epicurious et la session Adobe ; moyenne pour Mark Wiens, B&H et les tutoriels de créateurs ou de vendeurs ; faible pour le tutoriel de 2020 (interface ancienne).

**Ce qui manque** : aucun tutoriel lu sur le zoom de curseur, l'accéléré ou l'arrêt sur image (§4.2, §4.3 et §5.3 sont des propositions étayées par la doc d'ffmpeg et des extraits) ; aucune technique testée sur un rush de Cabezer.

**Règle d'emploi.** Une technique est une valeur de départ, à tester sur une copie et un extrait court (skill §1, §18).

**Animation ou traitement de plan ?** Définition unique : skill §1 et §16.
- *Animation graphique* (texte, forme, emoji, pastille, prix, note, schéma, carte, sous-titre animé, flash, glitch, transition graphique, parallaxe 2.5D) : After Effects, en calques natifs modifiables.
- *Traitement d'un plan filmé* (punch-in sec, zoom façon Micode, whip ou shake du cadre, rampe de vitesse, recadrage, Auto Reframe, stabilisation, fondu, mouvement sur une photo ou un document qui désigne un détail) : Premiere. Un calque de réglage qui porte un effet sur des plans filmés (flou directionnel d'une rampe) reste un traitement de plan ; avec une forme, un texte ou un flash, c'est une animation : After Effects.
- Un script peut piloter After Effects, jamais fabriquer d'image hors d'After Effects. Aucune image ni animation générée par IA.

---

## 2. Principes partagés par les meilleurs créateurs

**P1. La qualité se décide avant le montage.** « 80 % de l'image se fait sur le plateau, 20 % en étalonnage » (MKBHD) [Tuto, S1 10:39] ; « 90 % de la qualité sonore, c'est placer le micro » [S1 25:36]. **Pour Claude** : au dérush, repérer ce que le rush ne contient pas (plan large du lieu, préparation, gros plan produit) et le signaler à Cabezer. Ne jamais compenser un plan manquant par un effet.

**P2. Une idée par image, un chemin de lecture.** Un élément à la fois, un projecteur sur ce dont on parle, aucun décalage entre parole et mouvement [S1 19:53–21:25] ; appliquer aux cartons, comparatifs et captures (skill §6).

**P3. Le mouvement a une courbe.** L'easing est « une des marques les plus visibles entre un amateur et un pro » [S1 17:20] ; une rampe de vitesse suit la même logique [S10 2:01 ; S11 0:33]. Un mouvement progressif n'est jamais linéaire (skill §7) ; un punch-in sec est instantané ; la vitesse constante reste permise pour rotation continue, défilement, compteur, boucle.

**P4. Le silence n'est jamais du silence.** Un trou numérique paraît faux : on le comble avec le silence de la pièce du même rush ou une ambiance [S1 33:11–35:21 ; skill §4, room tone]. En D, les inserts restent muets de leur son source (skill §5.1) et aucune ambiance continue n'est posée par défaut (§3.5) : la continuité vient de la voix.

**P5. Moins de texte, plus de poids** [S2 24:33] (skill §6). **P6. Les transitions servent un changement** : la créatrice food de la session Adobe n'en met pas dans ses vidéos d'une minute [S9 55:43] ; une rampe joue ce rôle [S10 3:02] (skill §7).

**P7. L'honnêteté de l'image.** Mark Wiens décrit le plat et laisse le spectateur décider [S3 7:07] ; le food visualist de B&H cite le fromage filant à la colle, stylisme publicitaire [S6 4:12]. Cabezer filme de vrais plats achetés : ne jamais ajouter d'élément qui fait paraître le produit meilleur qu'il n'est (fromage truqué, glaçage, étalonnage qui change la couleur, plan stock présenté comme le plat servi). Corriger, ne pas embellir (§4.6).

**Préférences d'un seul auteur (ne pas généraliser)** : ouvrir sur un geste de nouilles [S9 40:31] ; calque de réglage global [S9 66:52] ; pas de musique au-delà de 20–30 s chez MKBHD [S1 8:08] ; démarrer la recette sur le premier temps de la musique [S12 5:01], exclu en D (pas de musique) ; boucler la fin sur le début [S9 82:34], à éviter quand l'appel au commentaire clôt la vidéo (skill §4).

---

## 3. Food : structure, réaction, image, son

### 3.1 Structurer un duel, un classement, un test par critères

Nick DiGiovanni construit un sandwich comme une suite de décisions (pain, œuf, fromage, viande, sauce) : chaque segment compare des options, en élimine, retient une avec une raison [S5 0:00–12:38].

**Quand** : duel entre deux adresses, classement, test de plusieurs versions d'un plat ; F, H ; T pour comparer des produits. **Éviter** : D sur un seul plat (arrivée, morsure, réaction, verdict : skill §5.1) ; ne pas la découper en décisions qui cassent la bouchée.

**Procédure** :
1. Écrire la grille avant le dérush : 3 à 5 critères (goût, texture, prix, quantité, accueil).
2. Repérer pour chaque critère le plan qui le prouve (morsure, intérieur, ticket) ; sans preuve, retirer le critère ou le signaler à Cabezer.
3. Poser un marqueur par critère (menu Marqueur ; raccourci M à confirmer) : plan de montage, pas texte à l'écran.
4. Montrer le choix de chaque critère à la fin de son segment, même cadre, même repère (skill §6, comparaisons).
5. Confirmer sujet et promesse (qui est comparé, sur quoi) avant la 30e seconde ; verdict en dernier.

**Critère de réussite** : les marqueurs seuls redonnent la logique du classement. **Piège** : le « top 5 » sans thèse, format que MKBHD a arrêté [S1 41:28] : donner une thèse.

### 3.2 Réaction de dégustation : laisser vivre l'instant

Mark Wiens refuse le jeu d'acteur : il décrit et laisse l'avis au spectateur [S3]. Pour Cabezer (skill §4, §5.1) :
1. Bouchée à vitesse réelle, en plan serré, sans rampe ni zoom pendant la morsure.
2. Réaction vocale gardée jusqu'à la fin réelle du dernier mot ; exclamations étirées protégées.
3. Coupe posée à la forme d'onde et à l'énergie du son, jamais aux seuls temps de transcription (`audio-dialogue-sound-design-mixage.md §3.1`). Claude mesure ; l'écoute finale revient à Cabezer.
4. Jamais de réaction doublée, rejouée ou recalée, jamais de J/L-cut sur la bouchée ou la réaction (`audio-dialogue-sound-design-mixage.md §3.3`).

**Critère de réussite** : la réaction se comprend sans sous-titre.

### 3.3 B-roll appétissant : plan de description, vapeur, macro, ralenti

**Plans de description (« beauties »).** Mythical Kitchen place des plans de plats au ralenti (vapeur, fromage saupoudré, liquide versé) pendant que l'hôte décrit le plat [S4 29:07–30:07] : c'est le principe du skill (§5), plan produit sans parole = B-roll sous la voix, insert muet. **Quand** : D, F, à l'annonce du produit. **Éviter** : S (une image par idée, skill §6). **Critère** : le plan montre un détail que la voix cite.

**Vapeur et fromage fondu.** Nick DiGiovanni couvre la poêle d'un peu d'eau et d'un couvercle [S5 6:04–7:05]. Geste de cuisine : s'il figure dans le rush, le garder comme plan de préparation ; ne jamais le recréer.

**Macro et haute cadence.** Le food visualist de B&H filme parfois vers 1 000 i/s [S6 2:08] : le ralenti propre se décide au tournage. Avant de promettre un ralenti, lire la cadence (`organisation-livraison-qc.md §6.2`, ou `ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate,avg_frame_rate -of default=nw=1 "rush.mov"`). 24 à 30 i/s ralentis à 50 % saccadent ; 50 ou 60 i/s donnent un ralenti propre [Métier ; `premiere-pro-avance.md §7.1`]. Pas de ralenti sur la bouchée retenue (skill §7). Stylisme : ne pas reproduire (P7).

### 3.4 Plan de préparation : les rushs d'abord, le plan stock ensuite (D, F)

Quand Cabezer annonce le produit (« on va tester les… »), un plan de préparation se pose sous sa voix (skill §5). **Quand** : D, F. **Éviter** : S, P, T (montrer le vrai produit).

1. Chercher dans les rushs : cuisson, versement, vitrine, cuisine (recherche de médias : `premiere-pro-avance.md §5.3`). Si rien ne convient, dire à Cabezer ce qui manque (P1) ; ne rien fabriquer.
2. Un plan **stock** n'est posé qu'avec l'accord de Cabezer, pour cette vidéo. Lui présenter nom du fichier, source, taille et licence ; ne rien télécharger avant. Sans accord (mode autonome) : s'en passer et noter « validation en attente ».
3. Choisir le **même type de produit** et le même geste (une friture de pâte pour une pizza frite), **sans logo, sans enseigne, sans lieu ni visage identifiable** (`conformite-droits-accessibilite.md`, section droit à l'image). Jamais présenté comme le plat servi : pas de « le plat arrive », pas de gros plan du résultat. Il dure le temps de l'annonce, sous la voix, en insert **muet**.
4. Consigner dans `Suivi/licences.csv` : source, URL, auteur, licence, date, fichier. Les licences de Pexels et de Pixabay n'ont pas pu être lues ici : relire la page à la date du téléchargement [À vérifier], notamment pour marques et personnes visibles.
5. Conformer à la cadence et au cadre de la séquence avant import, avec une piste muette (un média déclaré avec son mais sans son s'importe hors ligne : skill §14). Exemple pour 2160 × 3840 à 29,97 i/s [Mesure] :
   `ffmpeg -i stock.mp4 -f lavfi -i anullsrc=r=48000:cl=stereo -shortest -vf "fps=30000/1001,scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840" -c:v prores_ks -profile:v 3 -c:a pcm_s24le conforme.mov`
   Un stock horizontal recadré en vertical perd les deux tiers de sa largeur : préférer le vertical.
6. Harmoniser sa couleur avec la facecam sans l'embellir (§4.6).

**Critère de réussite** : nul ne peut croire que c'est son plat ; licence consignée ; plan conforme à la séquence.

### 3.5 Son : SFX, ambiance, foley, débruitage

**Sources.** Le foley reste discret, « de l'assaisonnement » [S8 0:31–3:34] ; en street food, le son du lieu fait partie du plat [S3 2:01].

**SFX par famille** (détail : `audio-dialogue-sound-design-mixage.md §6`) :
- **D** : banque Pixabay dédiée (`Tiktok degustation/SFX-Pixabay/`, licences dans `LICENCES-SFX.md`) et **liste fermée** du skill : swoosh, pop, ding, boing, scratch, caisse, photo, scintillement ; ni mème vocal ni boom. Un SFX appartient à un élément : élément retiré, SFX retiré. Calage par défaut **à l'attaque** (swoosh sur son pic) ; un essai A/B de −1, 0 et +1 image n'est adopté que s'il gagne à l'écoute de Cabezer (§12).
- **F, S, P, T** : bibliothèque ouverte, licence consignée dans `Suivi/licences.csv`. S : pas de bruitage d'objet gratuit.
- Jamais de son prélevé d'une vidéo TikTok ou d'un tutoriel.

**Ambiance.**
- **D : aucune ambiance continue ni musique.** Une ambiance discrète du lieu sous un insert muet est une question ouverte (§12), défaut : aucune.
- **F, S, P, T** : ambiance discrète du lieu, tirée des rushs, posée avant le premier plan du lieu, sous la voix, avec fondus aux changements de lieu (skill §11 ; `audio-dialogue-sound-design-mixage.md §7.2`).

**Foley d'aliment.** Défaut, pour toutes les familles : **aucun**. Jamais sur une bouchée ni une réaction ; pas non plus sur un insert muet sans accord. Un craquement rejoué fabrique un son que le plat n'a pas fait (P7). Question posée une fois (§12). En cas d'accord : insert de préparation à action visible, bas niveau, SFX rattaché à un élément et consigné (`audio-dialogue-sound-design-mixage.md §6.4`).

**Débruitage.** Un bruit constant se retire bien, un bruit variable (foule, cuisine) mal ; régler par petits pas, comparer avec et sans [S9 94:18–97:53]. Même réglage sur toutes les prises ; jamais « Améliorer la parole » (Enhance Speech) ni « Améliorer le dialogue » : interdits par défaut, ils changent le timbre (`audio-dialogue-sound-design-mixage.md §4`).

**Critère de réussite** : voix intelligible (mesure, puis écoute de Cabezer sur petit haut-parleur) ; chaque SFX a un élément ; aucune ambiance ni foley non validés.

### 3.6 Lieu, carte, prix et données visibles

- **Plan d'établissement** : façade ou rue avant l'intérieur [S9 40:31, une seule auteure]. En D, le lieu passe par l'étiquette « lieu » du hook ; aucun plan d'établissement ne retarde le produit au-delà de 3 s (skill §5.1, §5.2).
- **Carte** : photographier le menu pour l'orthographe exacte [S9 36:57] ; le prix payé (ticket) prime.
- **Prix à l'écran** : seulement aux vraies annonces. Montant seul, grand, pop + petit shake + caisse audible (skill §5.1). Pas de compteur qui monte en D (§6.2).
- **Données visibles** (visages de clients ou d'employés, enfants, plaques, numéro de carte sur un ticket, onglets et notifications d'une capture) : les repérer au dérush et les traiter selon `conformite-droits-accessibilite.md` (section droit à l'image). Aucun rush n'est envoyé à un service en ligne.

---

## 4. Food et tech : vitesse, arrêt sur image, recadrage, texte, couleur

### 4.1 Ralenti et rampes de vitesse sur les inserts

Une rampe change la vitesse progressivement : elle donne de l'énergie à un geste (verser, couper, déposer) ou relie deux plans de mouvement compatible [S10, S11]. Traitement de plan : Premiere (§1).

**Quand** : inserts de préparation, arrivée du plat, versement, coupe (skill §7) ; D (inserts), F, T (démonstration physique). **Éviter** : parole, bouchée retenue, S sur une prise de parole, capture d'écran à texte lisible.

**Procédure dans Premiere** (méthode de S10, mai 2025 ; libellés à confirmer) :
1. Vérifier la cadence (§3.3). Sous 50 i/s, limiter la rampe à l'accélération.
2. Sur le clip : clic droit sur le badge « fx » > Remappage temporel (Time Remapping) > Vitesse (Speed). Agrandir la piste pour manipuler les poignées [S10 4:05].
3. Poser deux images clés de vitesse, une avant et une après la portion visée (outil Plume ou Cmd + clic sur la ligne [S11] ; raccourcis à confirmer). Tirer le segment entre elles vers le haut (accélérer) ou le bas (ralentir) ; Maj pour des pas de 5 % [S10].
4. **Adoucir** : tirer la moitié gauche ou droite de chaque clé pour étirer la transition sur 6 à 12 images [Métier], puis régler les poignées de Bézier. Sans étirement, le changement est brutal.
5. **Interpolation** : mélange de trames (Frame Blending) pour un ralenti de 100 à 70–90 %, échantillonnage de trames (Frame Sampling) sinon (`premiere-pro-avance.md §7.1`). Le **flux optique** (Optical Flow), utilisé par S10, n'est pas employé sans l'accord de Cabezer (§12) ; accordé, l'examiner image par image sur mains, vapeur et liquides, et revenir au mélange en cas de déformation.
6. **Flou de mouvement** : S10 constate que Premiere n'en offre pas sur une rampe [mai 2025, à vérifier]. Contournement natif : calque de réglage au-dessus de la seule section rampée, effet Flou directionnel (Directional Blur), direction 90° pour un mouvement vertical, 0° pour un horizontal, intensité animée de 0 à environ 15 puis retour à 0 [S10 2:01–2:32 ; libellé du paramètre à confirmer]. Ce calque ne porte aucune forme, aucun texte, aucun flash. Il vignette les bords [S11 2:13] : agrandir de 5 à 10 % le plan dessous [Métier].
7. **Stabilisation** : Stabilisation de la déformation (Warp Stabilizer), attendre la fin de l'analyse, imbriquer avant la rampe [S10 3:02] (`premiere-pro-avance.md §7 bis`).
8. **Audio** : Premiere ne rampe pas l'audio [S10 4:37]. Les inserts de D sont muets (skill §5.1) ; ailleurs, séparer l'audio.

**Rampe-transition entre deux plans** [S10 3:02–3:34 ; S11 0:33] : deux plans de même direction de mouvement ; clé de vitesse quelques images avant la fin du premier (accélérer) et quelques images après le début du second (même vitesse élevée, jusqu'à 100 %) ; supprimer l'espace entre les clips ; calque de flou directionnel sur l'ensemble. Transition marquée, donc sonorisée (swoosh en D, pic sur l'image la plus floue : `audio-dialogue-sound-design-mixage.md §6.2`). En D, une seule, pour le changement de lieu du hook agressif.

**Alternative** : accélérer par coupes, sans courbe, est plus sobre et valable en F [S9 15:00]. Sur de la nourriture, partir de 150 à 300 % (S11 monte à 500 % sur des voitures) [Métier].

**Critère de réussite** : à vitesse réelle, ni image dupliquée visible ni saccade ; la vitesse monte et redescend sans à-coup ; mains et produit non déformés. À contrôler sur le MP4 exporté (§7.2).

### 4.2 Accéléré d'une préparation (insert)

Un accéléré comprime un geste long (pâte qui lève, cuisson, dressage, installation d'un produit, trajet) sans toucher à la parole. Traitement de plan : Premiere.

**Quand** : D (insert muet de préparation), F, T (installation, démonstration longue), S et H (insert illustratif). **Éviter** : parole, bouchée retenue, réaction, texte à lire, et tout accéléré qui laisse croire à une durée réelle fausse (cuisson, attente).

**Procédure** (libellés à confirmer ; `premiere-pro-avance.md §7.2` fait foi pour les options) :
1. Lire cadence et durée du rush (§3.3). Une source à 50 ou 60 i/s donne un accéléré plus fluide qu'une source à 25 i/s.
2. Clic droit sur le clip > Vitesse/durée (Speed/Duration) ; saisir plus de 100 %. Point de départ : **150 à 400 %** [Métier] ; monter tant que le geste reste identifiable, s'arrêter au premier doute.
3. Cocher « Montage par ondulation, déplacer les clips suivants » (Ripple Edit, Shifting Trailing Clips) pour ne laisser aucun trou [Extrait].
4. **Audio** : en D, retirer l'audio de l'insert (skill §5.1). Ailleurs, le couper ou le remplacer ; s'il est gardé, « Conserver la hauteur audio » (Maintain Audio Pitch) [Extrait].
5. Interpolation : échantillonnage de trames par défaut ; à forte vitesse, le mélange crée des fantômes [À vérifier à l'œil]. Si le geste devient saccadé, préférer deux coupes sèches sur les moments clés.
6. Un accéléré marqué est un mouvement rapide : un whoosh peut le souligner (swoosh de la liste fermée en D), calé sur le mouvement, sous la voix (skill §7).
7. **Signalement.** Si l'accéléré peut tromper sur la durée réelle, le dire à Cabezer ; rien n'est ajouté à l'écran sans son accord (aucun texte non demandé : skill §5.1).

**Time-lapse.** Une vidéo à intervalle issue de la caméra a déjà la cadence de son résultat : relever cadence et durée (`ffprobe`), sans flux optique. Pour juger un rendu, `-vf "framestep=20,setpts=N/(30*TB)" -r 30` garde une image sur vingt : 600 images deviennent 30, soit 1 s à 30 i/s [Mesure ; filtres lus dans la doc d'ffmpeg]. La vitesse finale se fait dans Premiere.

**Critère de réussite** : geste lisible, durée gagnée conforme au brief, aucune image dupliquée (§7.2), aucun son d'insert résiduel en D.

### 4.3 Arrêt sur image pour désigner un détail

L'arrêt sur image tient une image réelle pendant que la voix cite un détail : ligne du menu, prix du ticket, étiquette, composant, valeur d'une capture. Le figé est un traitement de plan (Premiere) ; l'annotation qui désigne le détail (surlignage, entourage) est une animation (After Effects).

**Quand** : F, S, T, P, H, pour tenir un détail ou une preuve. **D : éviter par défaut** : un plan figé y est suspect (`organisation-livraison-qc.md §6.3`) ; la désignation passe par le punch-in sec et le pop (§12). **Éviter partout** : bouchée, réaction, plan portant la parole (lèvres figées), plan dont le mouvement est le sujet, et **jamais pour masquer un trou ou un manque de rush**.

**Procédure** (libellés à confirmer ; `premiere-pro-avance.md §7.3` fait foi) :
1. Avancer image par image jusqu'à une image nette : sans flou de mouvement, texte lisible, geste terminé, bouche fermée si une personne est visible. Poser un marqueur.
2. Si la voix est liée au clip, dissocier l'audio avant de figer, pour que voix et ambiance continuent ; vérifier l'audio après.
3. Clic droit sur le clip, tête de lecture sur l'image : Insérer un segment d'arrêt sur image (Insert Frame Hold Segment) pour figer au milieu sans perdre la suite, ou Ajouter un arrêt sur image (Add Frame Hold) pour figer la fin du clip [Extrait ; une source indique 2 s par défaut, non confirmé].
4. Régler la durée en rognant le bord du segment ; éviter Vitesse/durée sur un segment figé, qui peut changer l'image tenue [Extrait, fil Adobe Community]. Pour un document ou un ticket, préférer la photo ou la capture d'origine.
5. **Durée** : image sans texte **2 s au moins** ; preuve **3 s au moins** (skill §6) ; texte à lire : formule de `documentaire-essai-video-archives.md §5.3`. Entrée et sortie de l'annotation en 8 à 15 images ; image immobile pendant la lecture.
6. Vers After Effects : Exporter l'image (Export Frame, libellé à confirmer).

**Contrôle.** `freezedetect` signale le figé : **faux positif attendu** [Mesure : 3 s animées puis 2 s figées, `freeze_start` à 2,98 s avec −60 dB/1 s comme avec −50 dB/0,5 s]. Compter les images dupliquées avec `mpdecimate` (§7.2) [Mesure : 300 images dont 120 dupliquées donnent 180]. Seuils : `organisation-livraison-qc.md §6.3`.

**Critère de réussite** : image nette tenue, voix et ambiance continues, durée respectée, aucun saut visible entre le dernier mouvement et le figé.

### 4.4 Recadrage vertical et recette

- **Séquence** : régler la taille avant de recadrer ; 1080 × 1920 en vertical (skill §13) ; le tutoriel de 2020 utilise 1080 × 1350 [S12 2:51].
- **Auto Reframe** : point de départ, jamais résultat final (skill §12) ; procédure : `premiere-pro-avance.md §8.1`, `formats-courts-verticaux.md §6.4`. Corriger les images clés pour garder visage, produit et mains.
- **Détection des changements de plan** : utile pour découper un export déjà monté, inutile sur un rush brut [S12 1:17] (`premiere-pro-avance.md §5.2`).
- **Tourner large** : la créatrice de la session Adobe cadre pour le vertical en 4K [S9 21:08–23:45].
- **Deux plans simultanés** sur fond flou ou uni [S9 23:15] : F ou recette seulement ; en D, la bouchée occupe le cadre. Zones sûres des textes : `formats-courts-verticaux.md §6.2`.

### 4.5 Sous-titres : ce que les pros automatisent

Limites, style, animation et rendu : `formats-courts-verticaux.md §4` (source unique). Sous-titres finaux = composition After Effects à l'identité de la famille, plus SRT ; la piste de légendes de Premiere ne sert que de transcription et de calage.

- **Flux de la créatrice food** : transcrire, créer les légendes, définir un style une fois et le propager, corriger, exporter un SRT [S9 102:27–106:34]. À retenir comme **piste de travail** seulement.
- **Scripts** : la référence UXP décrit `Transcript.transcribeClipProjectItem(clip, {language})`, `exportToJSON`, `importFromJSON`, `createImportTextSegmentsAction`, `hasTranscript`, `querySupportedLanguages()` [Doc dev Adobe ; version à vérifier sur la sienne]. Cabezer charge le panneau UXP. Les temps de mot d'un modèle externe étirent les mots : ne pas s'en servir pour placer une coupe (`audio-dialogue-sound-design-mixage.md §3.1`).
- **Connexion** : le tutoriel de 2021 exigeait Internet [S9 103:28] ; transcription locale ou cloud : [À vérifier sur sa version].
- **Sous-titres natifs de TikTok** : la créatrice retire ses incrustations pour TikTok [S9 106:03]. Contraire au skill (§9, sous-titres toujours incrustés en dégustation) : non retenu.

### 4.6 Étalonnage et lumière de la nourriture

Méthode complète : skill §10 et `etalonnage-gestion-couleur.md §11` (food), scopes `§6`. Ici, seulement ce qui vient des sources.

**Consensus.** La lumière se fait au tournage ; l'étalonnage corrige (P1). La nourriture ne doit pas être sur-étalonnée [S9 68:55].

**Divergence.** MKBHD stylise ses images avec un plugin payant (grain, halation, bloom) après des LUT par caméra [S1 11:10–14:14] : style de produit tech, pas une correction. **Règle** : D, F, S : naturel. T : look sobre, rien de stylisé sans l'accord de Cabezer, plugin payant exclu (skill §17). P : style de l'identité PRISME.

**Complément** :
1. Chaîne technique de la caméra, une seule fois (skill §10).
2. Calque de réglage global pour harmoniser luminosité et contraste des plans food d'une même scène [S9 66:52] : au-dessus des clips de même chaîne, jamais sur des captures d'écran ni des extraits de film.
3. Scope Waveform en luminance seule (YC No Chroma, libellé à vérifier) : une ligne collée à 100 indique des hautes lumières écrêtées [S9 71:27–72:28]. Les scopes aident l'œil, ils ne le remplacent pas.
4. Puis la correction secondaire food du skill : sauce, fromage, herbe, croûte, sans toucher la carnation.

**Critère de réussite** : plat reconnaissable à sa couleur réelle à côté du ticket ; peau naturelle ; aucune haute lumière écrêtée.

---

## 5. Tech : process, plans produit, captures, interfaces

### 5.1 Process d'une équipe de production (MKBHD)

Principes [S1 0:31–8:39] : bon entrant, bon sortant ; focus (ce qu'on coupe compte autant que ce qu'on garde) ; pas ennuyeux, pas insultant (le rythme n'est pas couper vite) ; montrer plutôt que raconter [S1 6:06] ; regard neuf avant verrouillage [S1 3:02] ; pas de montage tape-à-l'œil qui cache le propos [S1 7:06] ; passes séparées, comme le skill (§3).

**Pour Cabezer en T** : public food, vocabulaire accessible, un mécanisme à la fois, un chiffre que la voix ne dit pas plutôt qu'un mot qu'elle répète (skill §6). Demander à Cabezer, « regard neuf », de relire l'aperçu avant l'habillage final.

### 5.2 Plans produit propres

Un produit net, un fond simple, une source de contraste dominante [S2 39:20 ; Métier] ; lumière douce, drapeaux sombres contre les reflets [S2 10:48–14:53] : ce sont des conseils de tournage. En post, signaler un plan inutilisable (reflet, produit coupé, flou) sans chercher à le sauver (`premiere-pro-avance.md §7 bis`). Sur écran filmé, le moiré se traite au tournage : préférer la capture d'écran native. **Critère** : le produit occupe une part stable du cadre d'un plan à l'autre ; aucune zone d'interface de plateforme ne le masque (`formats-courts-verticaux.md §6.2`).

### 5.3 Captures d'écran et enregistrements : zoom guidé

**État de la preuve : proposition non validée.** Aucun tutoriel de zoom de curseur n'a pu être lu. Les outils de zoom automatique suivent le curseur puis reviennent au plan complet ; trop agressifs, ils donnent le mal de mer [Extrait d'éditeurs, non indépendants]. Les seules règles lues sont celles de MKBHD : un élément à la fois, un projecteur sur ce dont on parle, mouvement calé sur le mot [S1 19:22–21:25].

**Quand** : T (logiciel, application, page officielle). **Éviter** : texte trop petit pour être lu même agrandi ; zoom qui cache l'information citée. En S, les documents explorés suivent le skill §6 et `after-effects-motion-design.md §10`.

**Voie.** Un mouvement seul sur la capture est un traitement de plan, possible dans Premiere. Dès qu'une mise en valeur s'ajoute (assombrissement, entourage), tout se fait dans une composition After Effects.

**Procédure proposée** (à tester sur une capture réelle) :
1. Importer la capture en calque natif, à la résolution d'origine ; la parenter à un calque nul « ZOOM » animé en position et échelle (le retour au plan complet est un retour à 100 %).
2. Au mot qui désigne l'élément : clé de 120 à 150 % selon sa taille [Métier]. Contrôler à 100 % : sous la définition réelle de la capture, l'agrandissement pixelise.
3. Lisser : Facilité des images clés (Easy Ease ; F9 à confirmer), influence d'environ 70–80 % dans l'éditeur de graphiques [Métier]. Zoom de 8 à 15 images, puis capture immobile le temps de lecture (`documentaire-essai-video-archives.md §5.3`), retour au plan complet avant la coupe suivante. Flou de mouvement pour un zoom rapide (`after-effects-motion-design.md §12`).
4. Mise en valeur d'un seul élément à la fois ; garder le curseur de l'enregistrement.
5. Masquer onglets, e-mails, notifications et jetons (`conformite-droits-accessibilite.md`).

**Critère de réussite** : l'élément est visible au mot prononcé, lisible, sans tangage.

### 5.4 Animer une interface : design d'abord, easing, timing, staging

**Ce que fait l'équipe de MKBHD** [S1 15:14–22:59] : design fixe avant animation ; un calque par élément ; easing, timing, staging (une chose à la fois) ; un léger éclat (Glow) réduit jusqu'à presque disparaître [S1 21:25]. Les plugins cités (Motion Studio, Overlord) ont une gratuité non vérifiée : ne pas les installer ; l'éditeur de graphiques d'After Effects suffit (skill §17).

**Procédure** (After Effects, pour Liquid Glass et tout élément T) :
1. Poser l'état final et valider l'image fixe avec Cabezer.
2. Images clés sur le mot clé : une demi-seconde de décalage rend la lecture difficile [S1 19:53]. Courbe d'accélération sur chaque clé (skill §7).
3. Décaler l'entrée des éléments d'un groupe de 2 à 4 images (`after-effects-motion-design.md §9.4`).
4. Revoir à vitesse réelle : si l'animation se remarque, la réduire. « Un bon design est invisible » [S1 22:59].

**Aspect dessiné à la main.** MKBHD combine Turbulent Displace (libellé français à vérifier) et une expression Wiggle (toutes les 3 s, amplitude 150) [S1 21:56–22:59] ; le paramètre qui reçoit l'expression n'est pas indiqué : [À vérifier]. **Pas en D** (« pictos dessinés » n'est pas clean : skill §5.1) ni en T Liquid Glass. Possible en S si l'identité v15 le prévoit (skill §6), après validation d'un extrait.

**Critère de réussite** : en couvrant le texte, on comprend encore quel élément compte.

---

## 6. Tech : schémas, chiffres, compteurs, jauges

### 6.1 Barres, jauges, icônes qui se remplissent (After Effects)

**Principe** [S7 1:31–4:06] : un contrôleur central pilote plusieurs éléments ; on anime un seul nombre.
1. Calque nul « DATA » avec l'effet Contrôle du curseur (Slider Control), renommé « v1 ».
2. Forme : outil Plume, tracé épais à extrémité arrondie (barre) ou ellipse sans remplissage (jauge). Dupliquer : le calque du dessous est le fond, celui du dessus porte l'accent.
3. Sur celui du dessus : Rogner les tracés (Trim Paths ; libellé français à vérifier). Lier Fin (End) : Alt/Option + clic sur le chronomètre (raccourci à confirmer), expression `effect("v1")(1)`. L'index `(1)` évite le nom du paramètre, qui change avec la langue de l'interface.
4. Animer v1 de 0 à la valeur finale (0–100 = pourcentage). Une barre de plus = un contrôleur de plus.
5. **Icône qui se remplit** [S7 4:06] : dupliquer l'icône (copie d'accent), couvrir celle-ci par un trait très épais de bas en haut dont la Fin est liée à v1, et l'utiliser comme cache.

**Quand** : T (comparatif de prix, de performances), F (note sur 10 d'un duel, si Cabezer le valide). **Éviter** : D, où la note est définie par le skill (« 7-8/10 » en grand + emoji, flash, ding). **Critère** : la forme atteint exactement la valeur annoncée, puis ne bouge plus.

**Vie après l'entrée** [S7 2:01]. Un trait peut vivre légèrement ensuite, **à condition que le chiffre affiché ne bouge pas** : poser le wiggle sur la propriété Fin de la forme seule, jamais sur le contrôleur lu par un texte. Exemple [Métier, syntaxe vérifiée sous Node avec des objets simulés, jamais exécuté dans After Effects : à tester] :
```
v = effect("v1")(1);
tS = 2;   // seconde où l'entrée est terminée
v + (time < tS ? 0 : (wiggle(1.5, 1) - value) * linear(time, tS, tS + 0.5, 0, 1))
```

### 6.2 Compteur numérique

1. Texte + nul « DATA » avec un contrôleur « v1 » [S7 0:30–1:31].
2. Sur Texte source (Source Text) : même geste sur le chronomètre, puis `Math.round(effect("v1")(1))`. Sans `Math.round`, des décimales s'affichent. Préfixe ou suffixe : `"+" + Math.round(...)` ou `Math.round(...) + " %"`.
3. **Format français d'un prix** (extension de la méthode, absente de la source) [Métier ; sortie vérifiée sous Node : 12,3456 donne « 12,35 € », 9,9 donne « 9,90 € » ; jamais exécuté dans After Effects] :
   ```
   v = Math.round(effect("v1")(1) * 100) / 100;
   p = v.toFixed(2).split(".");
   p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, "\u202F");
   p.join(",") + "\u00A0€"
   ```
   `toFixed(2)` garde deux décimales ; `replace` insère une espace fine insécable entre les milliers ; `join(",")` met la virgule ; `\u00A0` est l'espace insécable avant le symbole. Vérifier que la police contient ces glyphes (`conformite-droits-accessibilite.md §7`).
4. Animer v1 de la valeur de départ à la valeur finale ; lisser les deux clés.

**Quand** : T (produits vendus, prix d'un composant, autonomie). **Éviter** : D et F pour un prix payé (pop + shake + caisse, skill §5.1). **Critère** : le dernier chiffre est celui de la voix ; le compteur s'arrête avant la fin de la phrase ; temps de lecture respecté (`documentaire-essai-video-archives.md §5.3`).

### 6.3 Cartes et comparatifs

- **Carte** : chaque région en calque séparé dans Illustrator, importé comme composition dans After Effects, animé par opacité ou tracé [S7 4:37]. Une carte n'est une preuve que si elle est exacte et sourcée (skill §8) ; comme aucun graphisme n'est fabriqué hors d'After Effects (skill §16), n'utiliser que des fichiers fournis ou validés par Cabezer. Le pack de modèles de S7 est payant : exclu.
- **Comparatif** : deux éléments, un repère stable, une couleur d'accent [S2 39:20 ; skill §6]. Le chiffre arrive sur le mot, jamais avant.

---

## 7. Piloter et contrôler

### 7.1 Ce que les API officielles permettent

[Doc dev Adobe, lue le 12/10/2026 ; disponibilité par version à vérifier sur la sienne]
- **Premiere (UXP)** : ouvrir, enregistrer et « Enregistrer sous » un projet ; importer des fichiers et des compositions AE ; lire les clips de timeline (nom, durée, vitesse en lecture seule) ; insérer un MOGRT ; créer et lire des images clés de paramètre d'effet ; exporter une image de séquence ; transcrire (§4.5). Les actions s'écrivent dans `project.lockedAccess(...)`.
- **Absent de la référence** : modifier la vitesse d'un clip, créer une rampe, régler l'interpolation, créer un arrêt sur image. Les faire à la main (§4.1 à §4.3).
- **After Effects (UXP)** : application, projet, compositions, calques, propriétés, textes, file de rendu.
- **Position commune** : ExtendScript tant que le test de fumée le confirme sur la machine de Cabezer ; UXP préféré pour un nouvel outil dans Premiere ; FCP XML en voie de secours (`premiere-pro-avance.md §13.3`). Aucun script n'est lancé sans ce test (`pilotage-environnement-reprise.md`).

### 7.2 Contrôles sur le fichier exporté

Toutes les commandes de contrôle (identité du média, cadence régulière, loudness et crête, blancs, son manquant, noirs, images figées) vivent dans **une seule bibliothèque**, avec leurs seuils : `organisation-livraison-qc.md §6` (scripts nommés, dont `controle-mp4.sh`). Loudness : −14 LUFS intégrés est un repère (±1), pas une cible ; crête vraie ≤ −1 dBTP (`audio-dialogue-sound-design-mixage.md §9`). La note de rétention en D utilise la seule méthode étalonnée du skill (§5.2). Ces contrôles signalent des cas à revoir ; ils ne remplacent ni le visionnage ni l'écoute de Cabezer (skill §14).

**Contrôles propres à cette fiche** [Mesure ; à ajouter à la bibliothèque après validation] :
- **Images dupliquées** (rampe, ralenti, arrêt sur image) : `ffmpeg -i x.mp4 -vf mpdecimate -an -f null -`, puis comparer au nombre d'images de la source (§4.3). Un ralenti à 50 % d'une source à 25 i/s : 500 images dont 250 uniques [Mesure].
- **Planche de contrôle d'une rampe** : `ffmpeg -i "x.mp4" -ss <début> -t 2 -vf "fps=15,scale=180:-1,tile=6x5" -frames:v 1 planche.png`, puis chercher des vignettes consécutives identiques ou déformées.

Consigner chaque sortie dans le suivi ; aucun résultat n'est présenté comme « validé » (skill §1).

---

## 8. Outils payants et dépendances de version

**Payants ou à gratuité non vérifiée** (skill §17 : gratuits uniquement ; rien n'est installé sans l'accord de Cabezer) : Real Smart Motion Blur (payant selon le tuto, prix à vérifier) ; Dehancer (environ 400 dollars pour deux postes selon le tuto) ; Epidemic Sound (abonnement, prix à vérifier) ; Overlord, Motion Studio, Brevity (gratuité non vérifiée) ; packs de modèles d'infographies (payants).

**Remplaçants natifs** : Remappage temporel, Vitesse/durée, Flou directionnel, Stabilisation de la déformation, Auto Reframe, Transcription, Contrôle du curseur, Trim Paths, éditeur de graphiques.

**À confirmer à l'écran** : Remappage temporel et interpolation (tuto 2025) ; absence de flou de mouvement sur rampe (mai 2025) ; libellés des arrêts sur image ; Auto Reframe et détection de plans (tutos de 2020) ; transcription locale ou cloud (tuto 2021). **Écartés** : normalisation de crête par clip (gain différent à chaque prise : même réglage sur toute la piste, `audio-dialogue-sound-design-mixage.md §4`) et « Instagram accepte la 4K » (2021).

---

## 9. Matrice famille × technique

| Technique | D | F | S | P | T | H |
|---|---|---|---|---|---|---|
| Structure par critères (§3.1) | Non | Oui | Si récit | Non | Oui | Oui |
| Plan de description au ralenti (§3.3) | Insert muet | Oui | Non | Non | Non | Oui |
| Plan stock de préparation (§3.4) | Avec accord | Avec accord | Non | Non | Non | Avec accord |
| SFX (§3.5) | Liste fermée Pixabay | Ouverte | Ouverte, sans bruitage d'objet gratuit | Ouverte | Ouverte | Ouverte |
| Ambiance du lieu (§3.5) | Non (défaut) | Oui | Oui | Oui | Oui | Oui |
| Foley d'aliment (§3.5) | Non (défaut) | Non (défaut) | Non | Non | Non | Non (défaut) |
| Rampe sur insert (§4.1) | Oui | Oui | Non | Non | Oui | Oui |
| Rampe-transition (§4.1) | 1 au hook | Rare | Non | Non | Rare | Oui |
| Accéléré d'insert (§4.2) | Oui, muet | Oui | Insert | Rare | Oui | Oui |
| Arrêt sur image (§4.3) | Non (défaut) | Oui | Oui | Oui | Oui | Oui |
| Sous-titres natifs de plateforme (§4.5) | Non | Non | Non | Non | Non | Non |
| Zoom guidé de capture (§5.3) | Non | Non | Non | Non | À valider | Oui |
| Tremblement de trait (§5.4) | Non | Non | Si v15 | Non | Non | Non |
| Jauges, barres (§6.1) | Note déjà définie | Si validé | Si schéma | Selon identité | Oui | Oui |
| Compteur (§6.2) | Non pour prix payé | Rare | Si chiffre | Rare | Oui | Oui |

« H » : montage hors familles ; suivre le brief de Cabezer, ces techniques servent de boîte à outils.

---

## 10. Erreurs de débutant → réflexes de pro

| Erreur | Pourquoi | Réflexe |
|---|---|---|
| Rampe sans étirer les images clés, ou flou sur tout le plan | Changement brutal ; plan flou en permanence | Étirer 6 à 12 images ; calque de flou limité à la rampe, 0 → 15 → 0 (§4.1) |
| Flux optique par défaut sur vapeur ou liquides | Déformation ; non accordé | Mélange de trames ; flux optique avec l'accord de Cabezer |
| Accélérer jusqu'à rendre le geste illisible | On ne comprend plus | Monter la vitesse tant que le geste reste identifiable (§4.2) |
| Figer une image pour boucher un trou, ou depuis un plan flou | Cache un manque ; détail illisible | Signaler le manque ; figer une image nette pour tenir un détail (§4.3) |
| Plan stock présenté comme le plat servi | Trompe le spectateur | Même type de produit, sans lieu ni logo, jamais « le plat arrive » (§3.4) |
| Embellir le plat en post | Le spectateur achète ce que le plat n'est pas | Corriger seulement (§4.6) |
| Compteur qui monte sur un prix en D | Remplace le pop du skill | Pop + shake + caisse (skill §5.1) |
| Wiggle sur un contrôleur qui alimente un nombre | Le chiffre ment | Wiggle sur la propriété de la forme seule (§6.1) |
| Foley d'aliment sur une bouchée ou un insert | Fabrique un son | Aucun par défaut ; demander une fois (§3.5) |
| Imiter l'animation d'une chaîne point par point | Aucune raison de regarder l'original [S1] | Garder le principe, refaire dans l'identité de la famille |

---

## 11. Liste de contrôle

Avant d'utiliser une technique :
- La famille est identifiée et la matrice (§9) l'autorise ; le brief et le skill ne la contredisent pas.
- Le libellé du menu est confirmé à l'écran ou marqué « à confirmer » ; aucun raccourci avant lecture.
- Un essai a été fait sur une copie et un extrait court.

Après le montage :
- **Rampes, accélérés, arrêts sur image** : cadence vérifiée ; images clés étirées ; flou limité à la rampe ; rien sur la voix ni la bouchée ; image figée nette, voix continue ; images dupliquées contrôlées (§7.2).
- **Plans de préparation** : stock seulement avec accord ; licence dans `Suivi/licences.csv` ; muet ; conforme à la séquence ; jamais présenté comme le plat servi.
- **Plats** : couleur naturelle comparée au ticket ; aucune haute lumière écrêtée ; aucun stylisme ajouté.
- **Sons** : chaque SFX a un élément ; D : liste fermée, calé à l'attaque, aucune ambiance ni foley non validés ; autres familles : ambiance sous la voix avec fondus ; sources consignées ; mesures faites (écoute finale par Cabezer).
- **Texte et chiffres** : temps de lecture respecté ; chiffre affiché = chiffre prononcé ; prix seulement aux vraies annonces.
- **Captures et tickets** : texte lisible, zoom sur le mot ; données personnelles masquées.
- **Plugins** : natifs ou gratuits ; tout outil payant signalé.
- **MP4 exporté** : contrôles de `organisation-livraison-qc.md §6` ; visionnage par Cabezer ; états distingués (appliqué, contrôlé, validé par Cabezer).

---

## 12. Décisions à demander à Cabezer, et tests à faire

**À demander** (le défaut s'applique en attendant ; l'alternative n'est jamais une règle) :

| Question | Défaut en attendant |
|---|---|
| Foley d'aliment sur un insert muet de préparation (versement, friture) ? | Aucun foley, jamais sur une bouchée ni une réaction |
| Ambiance discrète du lieu sous un insert muet en dégustation ? | Aucune ambiance en D |
| Essai A/B du calage des SFX (−1, 0, +1 image) en D ? | Pas d'essai ; calage sur l'attaque |
| Plan stock de préparation en D : accord général, ou à chaque vidéo ? | À chaque vidéo ; sans accord, signaler le manque et s'en passer |
| Flux optique accepté pour ses ralentis ? | Non ; mélange de trames |
| Arrêt sur image en D (ticket, prix) ? | Non ; punch-in sec et pop |
| Signaler à l'écran un accéléré qui peut tromper sur la durée ? | Rien d'ajouté ; la voix le dit |
| Compteur animé pour un prix en F ? | Pop identique à D |
| Zoom guidé de capture en T ? | À tester sur un extrait avant usage, pas généralisé |
| Version exacte de Premiere et d'After Effects, langue de l'interface ? | Les lire à l'écran (`pilotage-environnement-reprise.md`) |

**Tests à faire** (rien n'a été testé sur un rush de Cabezer) : une rampe d'insert avec et sans flou directionnel sur un rush 50/60 i/s ; un accéléré à 150, 300 et 400 % ; un arrêt sur image sur un ticket, voix conservée ; le format d'un prix ; une capture avec zoom guidé ; les libellés de vitesse, d'arrêt sur image et d'Auto Reframe.

---

## 13. Sources étudiées

**Transcriptions lues en entier** (sous-titres automatiques YouTube ; minutes à ± 30 s ; aucune image examinée). Les références S1 à S12 renvoient à cette liste.
- **S1.** The Studio (MKBHD), « The MKBHD Method™ For Editing High Quality Videos », 43:06, 12/10/2025. https://www.youtube.com/watch?v=eNgD1kg3U14. Process, easing, son.
- **S2.** The Studio (MKBHD), « How to Make High Quality Videos in 54 min, 19 sec, 20 milliseconds », 54:19. https://www.youtube.com/watch?v=3dQ6yKSttEc. Lumière, micro, texte.
- **S3.** More Best Ever Food Review Show, « Inside @MarkWiens ! Do You Fake Your Yummy Face?? », 10:01, 29/08/2020. https://www.youtube.com/watch?v=n37A3VZy0hw. Description, son du lieu.
- **S4.** Mythical Kitchen, « How We Made 100 Episodes of Last Meals », 37:37, 24/03/2026. https://www.youtube.com/watch?v=5diMuiDQ2Wo. Plans de description.
- **S5.** Epicurious, « How Nick DiGiovanni Makes His Perfect Breakfast Sandwich: Every Choice, Every Step », 12:48, 30/06/2023. https://www.youtube.com/watch?v=Hy0ZaBXIof0. Décisions, vapeur.
- **S6.** B&H Photo Video Pro Audio, « David Ma's Career Journey from Advertising to Food Videography | 21 Questions », 19:00. https://www.youtube.com/watch?v=W-31aRyK0Ug. Haute cadence, stylisme.
- **S7.** SonduckFilm, « 5 Infographic Edits You Should Know in After Effects », 5:28. https://www.youtube.com/watch?v=SKU3QdqKLOs. Compteur, jauge, barres, carte. Promotionnel.
- **S8.** Shutterstock Tutorials, « How To Make Your Own Foley + 41 FREE SOUND EFFECTS », 3:48. https://www.youtube.com/watch?v=5Hkz2TR199E. Foley de pas.
- **S9.** Adobe Creative Cloud, « Editing Food Vlogs for Social Media with FoodwithSoy – 2 of 2 », 117:16, probablement octobre 2021. https://www.youtube.com/watch?v=xm5YIr923C4. Réglage, scopes, débruitage, légendes, vertical. Interface 2021.
- **S10.** Justin Serran, « The EASIEST Way to Speed Ramp in Premiere Pro (2025 Tutorial) », 4:52, 27/05/2025. https://www.youtube.com/watch?v=U2TukFGyqew. Rampes, flou directionnel.
- **S11.** Camilo Castañeda, « My SECRET To Smooth Speed Ramp Transitions! », 2:40. https://www.youtube.com/watch?v=85bb-oveozc. Rampes, vignettage.
- **S12.** Hey Ashley Renne, « ADOBE PREMIERE PRO CC TUTORIAL: How to Edit a Food Video », 10:46, 28/11/2020. https://www.youtube.com/watch?v=HeL5glonJCI. Auto Reframe (interface 2020).

**Documentation lue**
- Adobe, UXP for Premiere Pro, référence API et journal de version. https://github.com/AdobeDocs/uxp-premiere-pro. Classes `Transcript`, `VideoClipTrackItem`, `ComponentParam`, `Exporter`, `Project` lues ; rien sur les menus.
- Adobe, UXP for After Effects, référence API. https://github.com/AdobeDocs/uxp-after-effects. Index et application lus.
- FFmpeg, `doc/filters.texi`. https://github.com/FFmpeg/FFmpeg (lu via raw.githubusercontent.com, 12/10/2026). Sections `setpts`, `tpad`, `framestep`, `freezedetect` lues ; commandes exécutées en local (ffmpeg 6.1.1, fichiers synthétiques) : `freeze_start` détecté sur un figé ; `mpdecimate` ramène 300 images à 180 ; accéléré à 300 % : 600 images deviennent 200 ; `framestep=20` : 600 deviennent 30 ; stock conformé en ProRes avec piste muette. Ne prouve rien sur Premiere.
- Les expressions de §6 ont été vérifiées sous Node (objets simulés), jamais dans After Effects.

**Extraits de recherche web (pages non ouvertes : indices, pas preuves)** : Larry Jordan, « Premiere Pro: 4 Ways to Change Clip Speed » (larryjordan.com) ; Joseph Nilo, guide des arrêts sur image (josephnilo.com) ; Filmora (filmora.wondershare.fr) et Elephorm (elephorm.com), tutoriels français ; Adobe Community, fil sur la durée d'un segment d'arrêt sur image ; Evergreen Help Wiki, « Speed and Duration » ; Noble Desktop, vitesse et Rate Stretch. Couverture réelle : noms Add Frame Hold et Insert Frame Hold Segment, options Ripple Edit et Maintain Audio Pitch, trois modes d'interpolation. Libellés exacts et durée par défaut non confirmés.

**Non lu** : aide Adobe, developer.adobe.com, docsforadobe.dev, support.google.com, ffmpeg.org, pexels.com et pixabay.com (licences) inaccessibles ici ; aucune page d'aide sur le remappage, l'arrêt sur image, l'Auto Reframe ou la transcription ; aucune page de licence de banque. Transcriptions bloquées : MKBHD (intro animée 2023), Arestov Design, Motion Nations, brainstorm.academy, Jacques Crafford, B&H (macro), Patrick Tomasso ; non téléchargées : partie 1 de la session Adobe, tutoriel « like Mrwhosetheboss ». Aucune source lue sur Joshua Weissman, Sorted Food, Keith Lee, BuzzFeed Worth It, Micode, Underscore_ ni Linus Tech Tips.
