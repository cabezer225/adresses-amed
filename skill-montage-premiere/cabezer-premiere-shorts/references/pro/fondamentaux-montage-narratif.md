# Fondamentaux du montage narratif — penser comme un monteur de cinéma

> **Réponses de Cabezer du 12/10/2026 — elles priment sur cette fiche**, en particulier sur sa section « Décisions à demander ». **Format d'abord, famille ensuite (SKILL §2)** : long (L-Food, L-Story, L-Tech, L-Films, L-Life) ou court (C-Food, C-Story, C-Tech, C-Films, C-Life) ; codes de cette fiche : D = C-Food, F = L-Food, S = L-Story, P = L-Films, T = L-Tech ; nouvelle famille Lifestyle (vlogs, face caméra : aucune musique, SFX comme la dégustation). **Tous les courts** : hook demandé, sous-titres mot à mot, aucune musique, SFX comme la dégustation, punch-ins secs, appel au commentaire, notation sur 10, identité propre au court. **Longs** : SRT seul en France ; composition musicale en Story, food et tech ; respirations d'émotion gardées en films/séries et au verdict du food long ; 4K si rushs 4K. Aussi : identité Story v15 et générique « Amed Story 🧢 » supprimés ; jamais de foley d'aliment ; ambiance en dégustation proposée au premier usage ; un rendu de sous-titres par passage ; intervenants identifiés à la première apparition (hors courts food) ; au plus deux passes de retravail sous 8 ; Tesseract, Higgsfield et SCANDALE FOOD retirés. **Réponses techniques (série 3)** : interface de Premiere et d'AE en anglais ; scripts AE et Terminal autorisés ; stock libre de droits sans redemander ; tout SFX de la banque Pixabay permis ; arrêt sur image permis partout ; pas de test de photosensibilité ; audio YouTube 384 kbit/s ; proxys toujours en long ; Frame.io pour les relectures ; WhisperX à installer ; « 19h30 » et « 12,50 € » ; Liquid Glass à recréer. Liste complète : `../decisions-en-attente.md`.

Fiche de référence du skill `cabezer-premiere-shorts` (publiée dans `references/pro/`). Elle apprend à décider où couper, quoi garder, quoi montrer, quelle transition poser et dans quel ordre travailler. Elle ne remplace aucune règle du skill.

## Quand lire cette fiche

- Au démarrage d'un montage : brief, découverte de la matière (§3).
- Quand une coupe « ne marche pas » sans qu'on sache pourquoi (§2, §4).
- Pour une interview, un dialogue, une séquence émotionnelle, un gag, une compression de temps (§8 à §12).
- Pour choisir une transition (coupe franche, fondu enchaîné, fondu au noir, fondu final, J-cut, L-cut) : §5.4 et §6.
- Pour une famille sans identité validée, ou un montage hors familles : la fiche donne la logique de base.

Ne pas la lire pour l'identité visuelle (skill §5.1, §6), les sous-titres (§9), l'audio technique (§11, `audio-dialogue-sound-design-mixage.md`) ou l'export (§13).

**Hiérarchie (skill §1) :** brief de Cabezer → règles du skill (dont les exceptions par famille) → fiches, dont celle-ci → méthodes de plugins → valeurs des tutoriels. Chaque technique dit quand l'employer, quand l'éviter et pour quelles familles (D dégustation, F food long, S Story, P films/séries, T tech, H hors familles). Une technique de cinéma n'est jamais une règle universelle : un long métrage n'est pas un TikTok de 3 minutes.

**Limite de Claude.** Claude ne « sent » pas le rythme et n'entend pas. Il le remplace par des mesures (durées de plans, blancs, niveaux), des images extraites autour des coupes, la transcription et la forme d'onde. L'écoute finale revient à Cabezer. Écrire « mesuré, non écouté » ou « écouté par Cabezer », jamais « écouté » pour une mesure (distinction appliqué / contrôlé / validé, skill §1).

## Sommaire

1. Principes · 2. Règle des six · 3. Brief et découverte · 4. Où couper · 5. Raccords, jump cut, transitions · 6. J-cut et L-cut · 7. Plans de coupe · 8. Entretien et documentaire · 9. Rythme · 10. Montage parallèle · 11. Ellipse · 12. Comédie · 13. Le son · 14. Quand ne pas couper · 15. Passes · 16. Premiere Pro · 17. After Effects · 18. Contrôles par script · 19. Tableau par famille · 20. Erreurs → réflexes · 21. Liste de contrôle · 22. Décisions à demander · 23. Sources

---

## 1. Principes communs aux monteurs

Retrouvés chez au moins trois monteurs lus en transcription intégrale :

1. **Regarder la matière deux fois avant de couper** : une vue pour ressentir, une avec marqueurs.
2. **Retrouver n'importe quel plan en deux clics.**
3. **Premier jet imparfait, puis raffinage.**
4. **Le son porte la scène.** Un son moyen est pire que pas de son (Hamilton).
5. **Tester avec un regard neuf.**
6. **Partir de l'émotion et du regard.** Zhou : « le montage, c'est les yeux ».
7. **Trouver le rythme en essayant et en mesurant**, pas en théorie.
8. **Ne pas s'attacher à sa première idée.**
9. **Le réalisateur est un partenaire.** Ici, Cabezer décide : proposer des options, ne jamais imposer.

**Préférences d'un seul monteur (ne pas généraliser) :** Murch monte debout, se méfie du match on action et travaille sur une seule timeline. Schoonmaker et Scorsese gardent des coupes rugueuses. Baxter pratique le « vertical sound editing » de Fincher. Hamilton ne coupe jamais une scène sans que le réalisateur l'ait vue, ce qui rejoint la validation du dérush du skill (§1).

---

## 2. Règle des six (Murch) : arbitrer une coupe

**Source :** conférence de Murch (Adobe, 2015, transcription lue) et résumé StudioBinder. Le livre *In the Blink of an Eye* n'a pas été lu.

**Six critères, par priorité décroissante :** 1) émotion ; 2) histoire ; 3) rythme ; 4) trajectoire du regard ; 5) plan 2D (axe des 180°) ; 6) continuité 3D de l'espace. On ne les satisfait pas tous la plupart du temps.

**Dépannage :** renoncer dans l'ordre à la continuité 3D, puis à l'axe, puis au regard, puis au rythme. Si un plan porte la bonne émotion mais reste « momentanément confus », le garder. Ne jamais sacrifier l'émotion pour sauver un raccord : c'est l'erreur type du débutant. Le spectateur pardonne une entorse du bas de la liste si l'émotion et l'histoire sont justes.

**Par famille :**
- **D :** émotion = envie et plaisir. Les seuils du skill (§5.2) sont des contraintes ; la règle arbitre entre deux coupes qui les respectent déjà.
- **F :** émotion (appétit, surprise), puis histoire (verdict).
- **S, T :** histoire en tête ; émotion aux moments humains.
- **P et H :** les six critères, dans l'ordre.

**Chiffres écartés** (aucune source primaire) : les pondérations 51/23/10/7/5/4 % et la phrase « le montage, c'est 70 % de rythme » attribuée à Murch par Zhou. Ne pas les citer.

**Critère de réussite :** pour toute coupe contestée, Claude dit en une phrase quel critère il garde et lequel il sacrifie.

---

## 3. Brief de démarrage et découverte de la matière

### 3.1 Brief de démarrage

Aucun montage ne commence sans brief écrit. Lire `Suivi/brief.md`, ou le créer : les douze champs et la méthode (remplissage à partir du dossier, questions seulement sur les champs bloquants) sont définis dans **skill §3, étape 0**. Six champs pèsent sur le montage narratif :

1. **Famille** (ou « hors famille ») : elle donne les exceptions du skill et la colonne du §19. Famille sans identité validée : prévoir l'extrait de 15 à 30 s à faire valider (skill §6).
2. **Promesse en une phrase** : « le spectateur a cliqué pour voir ___ ». Elle sert de critère « histoire » (§2). Sujet et promesse sont confirmés avant la 30e seconde (dans l'intro face caméra en Story) ; l'enjeu peut être rappelé ensuite (`retention-youtube-long.md` §2).
3. **Durée cible et plateformes.**
4. **Hook (tous les courts)** : le demander à chaque vidéo. Noter le hook choisi avec le barème du skill §5.2 (adapté à la famille) et donner la note ; sous 8, au plus deux passes de retravail, puis livrer avec la note réelle (réponse du 12/10/2026) ; son hook reste une option si Cabezer le préfère.
5. **Niveau d'autonomie** : valider le dérush avant l'habillage, sauf autorisation d'enchaîner ; elle n'autorise jamais la publication (skill §1).
6. **Contraintes** : langue des sous-titres à l'étranger, références de style et accord de téléchargement, contraintes légales (`conformite-droits-accessibilite.md`).

**Mode autonome :** hook = son hook habituel, noté ; langue à l'étranger = anglais (en court, la langue locale ou l'anglais est à demander ; défaut anglais consigné) ; plans stock libres de droits permis sans redemander (licence consignée, signalés) ; tout autre téléchargement (vidéo de sa chaîne ou d'un tiers, référence) demande son accord, donc s'en passer ; validations consignées « en attente » dans `Suivi/decisions.md`. Champ bloquant manquant (famille, promesse) : poser la question. Le brief fait foi pour le contrôle final.

### 3.2 Découvrir la matière avant de couper

**Quand :** chaque nouveau projet, même un dérush de dégustation. **Abréger :** une retouche ponctuelle sur un montage validé. **Familles :** toutes.

1. **Premier passage sans noter :** lire la transcription du rush réel (jamais le script comme preuve de ce qui a été dit, skill §3) et parcourir les rushs (planches d'images, forme d'onde) pour saisir l'intention.
2. **Second passage avec marqueurs :** meilleure prise, émotions, réactions, erreurs de fait, phrases protégées du skill (« Bref, c'est partiiii », appel au commentaire, passages sur la famille, skill §4).
3. **Classer les prises** d'un même moment : meilleure, deuxième, troisième (Schoonmaker). Garder deux options sur les moments à forte charge (Hamilton).
4. **Découper en unités de sens** : une réplique, un geste.
5. **Assembler un premier jet**, même mauvais, dans l'ordre.

**Choisir la prise utile, pas la plus parfaite** : chercher les instants où l'on voit la personne penser, décider, écouter. **Organisation :** `organisation-livraison-qc.md` §2, marqueurs colorés avec commentaire court. **Ampleur :** version courte en D ; version complète en S, P, F et pour les explications tech.

---

## 4. Où couper : fin de pensée, mouvement, regard, clignement

### 4.1 Fin de pensée
Murch coupe quand la pensée est finie, avant le début de l'action suivante. Le skill fixe la coupe de voix (§4 : juste après le dernier mot entièrement audible, bords placés à la forme d'onde et à l'énergie du son). Critère d'image ajouté : sur un visage, couper quand l'expression de fin de phrase retombe, pas en plein mouvement de bouche ou de tête. **Familles :** toutes.

**Respirations.** L'exception du skill (§4, §6) vise Story : garder les pauses qui portent un regard, une émotion, une attente construite, jamais un blanc vide. Elle est étendue aux moments d'émotion de films/séries (P), au verdict du food long (F) et au Lifestyle posé (réponse du 12/10/2026, skill §4). Interdite en D (courts) et en T.

### 4.2 Clignement
Murch : un clignement marque la fin d'une pensée ; couper **une image avant** lui paraît naturel. Contrepoint de Baxter : il retire les clignements hors du rythme des mots en gros plan, mais en a gardé dans *The Killer*. **Pour Cabezer :** le clignement est un **indice**, jamais une règle. Si fin de phrase et clignement coïncident, couper juste avant. Ne pas retoucher un clignement sans demande. En jump cut de D, le rythme des mots prime. **Familles :** indice partout ; critère plein en P.

### 4.3 Mouvement
Murch : un pas, couper **après** le pas ; une marche, à l'apex entre deux pas ; un impact, sur le temps fort. **Pourquoi :** couper en plein mouvement le montre deux fois et l'œil saute. **Éviter :** en D, ne pas couper au milieu du geste main → bouche (skill §5). **Familles :** toutes.

### 4.4 Critère de réussite
Extraire des images autour de la coupe (§18.3) : le mouvement n'est pas montré deux fois ; aucun œil mi-clos ni bouche en plein mot sur la première image entrante.

---

## 5. Raccords, jump cut et catalogue des transitions

### 5.0 Raccords

| Raccord | Définition retenue | Quand l'utiliser | Quand l'éviter | Familles |
|---|---|---|---|---|
| Sur le mouvement | Le geste commence dans un plan et finit dans le suivant | Gestes, entrées dans le cadre, bouchée | Plan fixe d'interview | Toutes |
| De regard (eyeline match) | On coupe d'un regard vers ce qu'il regarde | Montrer produit, document, lieu | Objet illisible dans le plan suivant | S, P, F, T |
| Match cut | Deux plans liés par une forme, un cadrage, un mouvement ou un son | Passage entre deux lieux ou idées ; hook | Lien illisible en moins d'une seconde | Hook D, P, S |
| Jump cut | Saut dans le temps sur un même plan | Retirer un blanc ; effet voulu | Quand une coupe invisible est attendue | D (style), T |
| Franchissement de l'axe | Plans qui traversent la ligne d'action | Avec point d'intérêt commun | Dialogues sans repère | P, S |

**État des sources.** Aucune source lue ne définit « eyeline match » (définition du métier) ; pour match cut et match on action, les sources divergent : retenir le tableau. La règle empirique de 30° est une aide de tournage, pas une loi.

### 5.1 Raccord de regard
1. Repérer le point d'intérêt du plan sortant. 2. Choisir le plan entrant dont le point d'intérêt tombe **au même endroit de l'écran**. 3. Laisser le regard se tenir un instant avant la coupe. 4. Vérifier le sens (regard à gauche → objet attendu du bon côté). **Réussite :** le spectateur suit sans chercher où regarder.

### 5.2 Match cut graphique dans Premiere
1. Repérer le point commun (forme, position). 2. Caler les deux plans pour que ce point tombe au même endroit ; vérifier en superposant le plan entrant à 50 % d'opacité, puis rétablir 100 %. 3. Caler le début du mouvement entrant sur la fin du mouvement sortant.

**Son :** le match cut est une transition marquée. Un whoosh ne le sonorise que dans un hook agressif de dégustation (skill §7), calé sur le déplacement visuel. Ailleurs (S, P, F, T), le son continu (ambiance, voix, musique) le porte ; un whoosh le rend visible. Les enchaînements de Satoshi Kon (selon Zhou) inspirent les hooks, ils ne sont pas une règle.

### 5.3 Jump cut : le garder ou le masquer
**Le garder** (Schoonmaker, Scorsese ; Ficarra : trois jump cuts sur un visage marquent un changement d'enjeu). **Condition :** un motif précis, sinon cela ressemble à une erreur. D : style de base (skill §5). S, P : changements d'enjeu.

**Le masquer** (jump cut involontaire), par ordre de préférence :
1. coupe franche assumée ou punch-in sec (D) ;
2. plan de coupe qui apporte une information (§7) ;
3. second angle synchronisé ;
4. animation, seulement si elle était déjà prévue.

Morph Cut seulement sur demande (§16.3), pas de texte ajouté seulement pour relancer l'image (skill §5.1). Détail : `formats-courts-verticaux.md` §3.4, `premiere-pro-avance.md` §5.4.

### 5.4 Catalogue des transitions : durées de départ et emploi par famille

**Règle du skill (§7) :** transitions réservées aux changements d'argument ou de séquence. Elle vise les transitions **visibles**. En long : **coupe franche par défaut, fondus rares (fin de Story ou sur demande)** ; fondu de calme, coupe au noir et noir dans un gag seulement sur demande, avec deux versions sur un extrait (réponse du 12/10/2026). Les micro-fondus audio de 1 à 2 images et les J/L-cuts sont permis s'ils ne mordent pas l'attaque d'un mot (skill §4) ; jamais de J/L-cut sur la bouchée ni la réaction en D.

**Statut des valeurs.** Repères de la littérature : un fondu enchaîné classique dure 24 à 48 images (environ 1 à 2 s) ; un fondu de 6 à 12 images (« soft-cut ») adoucit un jump cut (Pixel Valley Studio, MasterClass, Boris FX : extraits de recherche). Les durées du tableau sont des **valeurs de départ de métier, non sourcées, à valider sur un extrait avec Cabezer**, en images à 29,97 i/s ; reconvertir à la cadence de la séquence (12 images = 0,40 s à 29,97, 0,48 s à 25). La durée par défaut d'une transition dans Premiere serait de 1 s selon l'aide Adobe (extrait ; à vérifier dans Preferences > Timeline, libellé anglais à confirmer) : souvent trop long ici, donc **fixer la durée à la pose**.

| Transition | Durée de départ | Employer quand | Éviter quand | Familles |
|---|---|---|---|---|
| **Coupe franche** | 0 | Défaut partout : même idée, même lieu, changement de valeur de plan | Temps ou lieu qui changent sans repère (§11) | Toutes ; seule transition des courts, hors whip et flash de C-Food |
| **Fondu enchaîné** (Cross Dissolve) | 12 à 24 images ; 24 à 48 pour une ellipse longue ou un fondu de calme | Rare : changement de temps, de lieu ou de ton ; passé/présent ; ellipse, seulement sur demande de Cabezer (fondu de calme : deux versions sur un extrait) | Par défaut ; entre deux prises du même visage (fantôme) ; pour masquer un jump cut ; sur une preuve à lire | Longs, sur demande (en S, rare, surtout en fin de vidéo) ; **jamais dans les courts** |
| **Fondu au noir** (Dip to Black, libellé à confirmer), milieu de vidéo | 12 à 24 images à la descente, autant à la remontée | Seulement sur demande : fin d'une grande partie, rupture nette de ton ou de jour | Par défaut ; entre deux idées voisines ; courts | Longs, sur demande (en S, le chapitre a son carton, skill §6) |
| **Fondu depuis le noir** (ouverture) | 12 à 24 images | Seulement sur demande : ouverture posée d'un film ou d'une série | Par défaut ; quand l'image 1 porte le hook ou le produit | Longs, sur demande ; **jamais en court** (produit ou bouchée dans la 1re seconde, skill §5.2) |
| **Fondu final** | S : 30 à 60 images (1 à 2 s) proposées ; autres : 12 à 24 | Refermer une vidéo | Courts : aucun ajouté | **S :** après le regard silencieux, avant que Cabezer bouge, accord musical qui s'éteint sur le noir, aucun bruitage, pas de carton d'abonnement (skill §6) ; 5 à 20 s réservées à l'écran de fin. **F, T, P, L-Life :** sur demande seulement, compatible avec l'écran de fin (skill §13). **Tous les courts :** appel au commentaire dans les 5 dernières secondes, puis coupe à l'extinction réelle de la voix (skill §4) |
| **Cut au noir** (coupe sèche vers le noir), y compris le noir dans un gag | 0 ; noir tenu à décider avec Cabezer (départ 0,5 s) | Choc ou chute au milieu d'une vidéo, seulement sur demande, deux versions sur un extrait | Par défaut ; fin de Story (pas de fin coupée sèche, skill §6) ; tout noir non écrit (skill §14 traque les noirs involontaires) | Sur demande seulement ; sinon non utilisé |
| **J-cut / L-cut** | Décalage de départ 6 à 15 images | Voir §6 | Voir §6 | Voir §6 |
| **Fondu audio de raccord** | 1 à 2 images dans le silence, ou deux clés de volume | Seulement où un clic ou un saut de fond est audible (§13.3) | En masse ; coupes serrées de D ; attaque d'un mot | Toutes, avec ces limites |

**Spécifiés ailleurs :** flash blanc, shake et whip de 4 à 6 images (D, skill §5.1) ; carton de chapitre (S, skill §6 point 12 ; générique « Amed Story » supprimé le 12/10/2026) ; match cut (§5.2).

**Transitions graphiques.** Iris, glissement, zoom, volet, flash, glitch, déchirure : ce sont des animations graphiques, donc construites dans After Effects en calques natifs (skill §1, §16). Aucune transition intégrée générique de Premiere de ce type. Les fondus sont un traitement du plan : ils se posent dans Premiere.

**Poser un fondu dans Premiere.**
1. Vérifier que les deux clips ont des images au-delà de la coupe (poignées) ; sinon poser la transition au bord du clip.
2. Panneau Effects > Video Transitions > Dissolve (interface de Premiere en anglais ; libellés à confirmer, repères français d'après des tutoriels : Effets > Transitions vidéo > Fondu enchaîné, Fondu au noir, Fondu au blanc). Glisser la transition sur le point de montage, fixer la durée en images.
3. Le fondu vidéo ne traite pas l'audio : poser le fondu audio à part (§13.3).
4. Fondu au noir : selon l'aide Adobe (extrait), il peut affecter une vidéo posée sur une piste inférieure ; vérifier l'aperçu avec toutes les pistes (à vérifier). Rendre la plage avant de juger.

**Contrôle.** Relire la liste des transitions de la séquence (`xml-coupes.py`, §18.5) et écrire une raison par transition dans `Suivi/decisions.md`. Un détecteur de coupes ne voit presque jamais un fondu enchaîné : les contrôler à l'œil.

---

## 6. J-cut et L-cut

**Définitions :** J-cut = le son du plan suivant démarre avant son image ; L-cut = l'image change mais le son du plan précédent continue. **Pourquoi :** décaler les coupes audio et image lie deux plans (Baxter coupe sur l'écoute : le personnage suivant apparaît avant de parler).

**Quand :** interview ou scène à deux (passer à l'écoute, montrer une réaction) ; voix de Cabezer qui continue sur un document ou un lieu ; ambiance du lieu suivant qui arrive avant l'image. **Familles :** S, F, P, T, H.
**Quand l'éviter :** D, où la voix reste collée aux coupes franches : jamais sur la bouchée ni la réaction ; seul décalage utile, le B-roll sous la voix (skill §5). Éviter aussi tout décalage qui ferait entendre un bout de phrase supprimée ou mordrait l'attaque d'un mot.

**Procédure Premiere :**
1. Vérifier que la Sélection liée (Linked Selection) est active (libellé à confirmer).
2. **J-cut :** maintenir Option (Mac) et tirer le bord gauche de la vidéo du plan B vers la droite, l'audio restant en place (geste à confirmer sur sa version).
3. **L-cut :** même geste sur le bord droit de l'audio du plan A vers la droite, ou raccourcir la vidéo du plan A en laissant l'audio.
4. Variante lente : clic droit > Dissocier (Unlink, libellé à confirmer), trimmer vidéo et audio séparément, puis re-lier.
5. Poser un fondu audio court si un clic est audible (§13.3).

La sélection liée peut se désactiver après une coupe : la revérifier avant chaque trim. **Réussite :** forme d'onde nette autour de la coupe, aucun mot rogné, aucun bout de phrase supprimée sous l'image suivante ; Cabezer valide à l'écoute.

---

## 7. Plans de coupe, inserts et B-roll

**Définitions** (consensus de glossaires) :
- **Plan de coupe (cutaway)** : bref plan d'autre chose que le sujet (réaction, objet, lieu) inséré pendant que le son principal continue ; il masque une coupe ou couvre un saut de temps.
- **Insert** : gros plan d'un objet, d'un texte ou d'un geste. **B-roll** : la matière filmée ; le plan de coupe en est l'usage éditorial.

**Quand :** masquer une coupe d'interview (S, F) ; montrer une réaction ; apporter une preuve. **Familles :** S, F, P, T, H. **Quand l'éviter :** en D, ne pas masquer une coupe : le style de Cabezer est la coupe franche. Pour relancer l'image : punch-in, coupe ou insert, jamais un texte non demandé (skill §5.1).

**Règles :**
1. Choisir le plan d'après ce que le spectateur doit comprendre, pas d'après le mot prononcé (skill §6, étape 1).
2. Il apporte une information nouvelle ou masque une coupe voulue ; sinon rester sur le visage.
3. **Temps de lecture :** appliquer `documentaire-essai-video-archives.md` §5.3 (formule du skill) aux textes d'habillage, cartons, traductions et blocs de sous-titres des familles longues. Elle ne vise ni les sous-titres mot à mot de D ni les coupes rapides nommées de 0,4 à 0,8 s (accumulation sans texte à lire). Image sans texte : 2 s au moins ; univers visuel suivi : 2 à 3 s.
4. Plan muet : sans son source (skill §5).
5. **Mouvement sur une image fixe ou un document :** seulement pour désigner un détail ou présenter un visage, avec un temps avant et après et une courbe douce ; jamais de dérive décorative, jamais sur un plan qui porte un texte à lire (skill §6 point 11 et §7, « Mouvement sur image fixe »).
6. **Plan stock de préparation (D) :** accord général de Cabezer pour les plans stock libres de droits : téléchargés sans redemander, licence consignée dans `Suivi/licences.csv`, signalés à Cabezer ; une préparation du même type de produit, jamais présentée comme le plat servi, sans logo ni lieu identifiable (skill §5).
7. **Extrait tiers (P, S) :** durée minimale nécessaire, commenté, source affichée ; un crédit n'est pas une autorisation ; signaler le risque Content ID avant publication (`conformite-droits-accessibilite.md`).

**Exemple de Hamilton :** un briefing de *Top Gun: Maverick* alterné avec des plans de pilotes sous une musique ; le briefing donne l'information, les plans le sentiment. **Réussite :** sans le plan de coupe, quelque chose manque ; sinon le supprimer.

---

## 8. Entretien, dialogue et documentaire (Cabezer Story)

**Couverture réelle :** une seule source de monteur traite l'interview (Baxter, en fiction), plus Hullfish, Schoonmaker et des ressources d'éthique documentaire lues par résumé. Aucun documentariste lu : valider sur un extrait avec Cabezer. Compléments : `documentaire-essai-video-archives.md`.

### 8.1 Fidélité au sens
Le skill l'impose (§8, §12). Les ressources d'éthique décrivent le « frankenbite » (réarranger des mots pour faire dire autre chose) : à proscrire. Un cas PBS montre qu'un silence conservé peut rendre un interviewé évasif : garder ou couper une pause change aussi le sens.

**Permis au dérush :** retirer un faux départ pour garder ce que Cabezer voulait dire (ses exemples : « deux mozzarelles… trois, trois » devient « trois mozzarelles »). **Jamais :** un collage qui crée une affirmation qu'il n'a pas faite ou qui change le sens. **Procédure :** relire la phrase recollée et se demander si la personne reconnaîtrait ce qu'elle a dit.

### 8.2 Écoute ou parole à l'écran
Baxter cherche les « meilleurs moments d'écoute » et coupe sur celui qui écoute avant qu'il réponde. Hamilton et Lee Smith (cités par Hullfish) : pour une information à retenir, la personne dit la réplique à l'écran. Information → la personne parle ; doute ou émotion → rester sur celui qui écoute. En S : visage pour la nuance, document quand la preuve doit être lue (skill §6).

### 8.3 Taille de plan
Baxter reste large pendant les déplacements et réserve le gros plan au point important ; en facecam, zoom façon Micode seulement quand il sert le moment (skill §7).

### 8.4 Montage par le texte dans Premiere
Procédure détaillée : `premiere-pro-avance.md` §5.1. Le panneau Text (Texte) transcrit les clips ; supprimer un mot supprime le passage avec ripple. Selon des guides, une fonction repère les mots de remplissage et supprime les pauses au-delà d'une durée réglable (défaut cité 0,75 s).

**Règles pour Cabezer :**
- **Repérer et pré-découper** un assemblage, rien de plus. Aucune suppression en masse.
- **Recaler chaque coupe** à la forme d'onde et à l'énergie du son, jamais aux temps de la transcription (qui étire les mots) ; vérifier qu'aucun début de mot n'est mordu (skill §4). Pour recaler en série, utiliser l'outil d'affinage des bords de `audio-dialogue-sound-design-mixage.md` §3.1 : il propose des candidats en CSV, jamais appliqués sans l'écoute de Cabezer, et se règle d'abord sur un montage validé.
- **D et tous les courts :** abaisser le seuil de pause à 0,25 s si le panneau le permet, sinon couper à la main ; garder réactions et échanges.
- **S :** pas de « supprimer toutes les pauses » : cela efface les respirations que le skill garde (§6).
- Une fonction « Paper Edit » est annoncée par une source non officielle : à vérifier sur sa version avant d'en parler.

---

## 9. Rythme

### 9.1 La durée porte l'émotion
Zhou : dans une séquence de Star Wars, les plans raccourcissent vers le sommet en environ 15 secondes, puis la descente dure deux fois plus. Un échec traité en 30 images contre 30 secondes ailleurs ne convainc pas. **Valeur de départ (à tester, non universelle) :** après un sommet, laisser retomber au moins le double du temps de montée. **Familles :** S, P, F ; en D, rythme contraint par le skill.

### 9.2 Tension et relâchement
Baxter : quand le personnage maîtrise, on étire ; quand il perd le contrôle, on passe aux jump cuts ; une bagarre se monte « étirer, étirer, exploser, pause », calée sur la musique. **Par famille :** S, alterner posé et accéléré (coupes de 0,4 à 0,8 s seulement par accumulation sans texte à lire, skill §6) ; P, « étirer / exploser / pause » ; D, rythme du skill (3,6 à 4,2 mots par seconde, blancs de plus de 0,25 s coupés), sans autre apport que laisser la réaction après la bouchée.

### 9.3 Tenir un plan plus longtemps que confortable
Baxter tient certains plans un peu trop longtemps ; Scorsese : « un peu trop longtemps, puis couper si c'est justifié » (via Zhou). Deux cas :
- **Plan sans parole** (extrait, document, lieu, carton) : durée fixée par le temps de lecture (§7 règle 3) et l'émotion. Permis en S, F, P.
- **Visage de Cabezer après son dernier mot** (respiration) : exception du skill (§4) en S, aux moments d'émotion de P, au verdict de F et dans le Lifestyle posé. Ailleurs (C-Food, T, tous les courts), couper selon le skill §4.

**Éviter :** D, explications tech, tout moment où Cabezer cherche ses mots.

### 9.4 Trouver le point de coupe par essais
Murch place la coupe, ajoute ou retire des images, relit (la fenêtre de trim affiche le décalage).
1. Placer la coupe selon transcription, forme d'onde et énergie du son.
2. Tester trois positions : −3 images, point retenu, +3 images, hors des mots (§4).
3. Comparer images, forme d'onde et transcription ; choisir la version qui garde l'intention (critère 1).
4. Écrire le choix. Si l'écart change le sens ou le rythme, fournir à Cabezer un aperçu court A/B : son écoute tranche.

### 9.5 Mesurer le rythme
`mesure-plans.py` (§18.2) donne durée moyenne et médiane des plans. Ces valeurs ne définissent pas un bon rythme : elles repèrent une zone anormalement longue ou monotone et comparent deux versions. **Réussite :** chaque zone longue est justifiée par une émotion ou une preuve à lire. **Familles :** toutes.

---

## 10. Montage parallèle et intercut

**Couverture réelle :** aucun monteur lu ne traite le montage parallèle en tant que tel (articles généralistes ; cas Hamilton). Points de départ à valider.

**Définition :** alterner des actions simultanées ou qui se répondent, en des lieux ou époques différents (cross-cutting). Dans *Le Parrain*, le baptême est alterné avec les meurtres commandés par Michael.

**Quand :** deux histoires qui se rejoignent ; un propos confronté à une image ; une attente avec un enjeu qui approche. **Familles :** S, P ; F et T rare. **Éviter :** D, sauf hook fait d'extraits rapides (skill §5) ; lignes de longueurs très inégales.

**Procédure :** écrire en une ligne l'effet recherché (contraste, urgence, écho), sinon ne pas alterner ; garder des durées comparables entre les deux lignes ; chercher un lien à chaque bascule (son, geste, forme, mot) ; accélérer en approchant de la jonction ; tenir l'ensemble par une musique ou une voix continue. **Piège :** alterner par dynamisme fait « perdre la tête aux viewers » (skill §6).

---

## 11. Ellipse et compression

**Ellipse :** passer sur un moment en gardant le sens (Kon saute l'action attendue et montre le résultat). **Procédure (Hamilton) :** 1) rapporter chaque scène à sa fonction ; 2) pour chaque plan, demander s'il peut être une image plus court ou supprimé ; 3) compresser une suite de scènes avec musique et une ou deux répliques clés. « L'information est la mort de l'émotion » : Hamilton serre jusqu'à casser, puis rend de l'air.

**Application :** D, déjà très comprimée, ne pas retirer les réactions ; S, P (moments d'émotion) et verdict de F, garder les respirations qui portent une émotion (skill §4, §6) ; déclinaisons, comprimer avec les paroles existantes sans recomposer le sens (skill §12). **Piège :** une ellipse sans repère de temps désoriente ; ajouter un signal : fondu enchaîné (§5.4), lumière, mot, musique.

---

## 12. Comédie et gags

**Source :** Zhou sur Jackie Chan (transcription lue). Edgar Wright et Roger Nygard non lus. Action et réaction dans le même plan quand c'est possible ; ne pas couper sur chaque coup ; montrer le coup deux fois, en reprenant le geste trois images en arrière (un seul coup, plus fort) ; faire payer le gag par le visage.

**Quand :** un moment comique de Cabezer en F, S ou P. **Éviter :** généraliser les trois images, propres à l'action ; en D, la chute passe par la coupe franche et le SFX du skill. **Chute dite à voix haute :** laisser finir la dernière syllabe, puis couper. Tenir le visage 0,5 à 1 s relève de la respiration (§4.1) : permis en S, en P et au verdict de F quand il porte l'émotion ; pas en D ni en T.

---

## 13. Le son mène l'image

### 13.1 Idées retenues
Le son est la moitié de l'histoire (Hamilton). **Contrôler le rythme visuel sans le son** une fois : un bon son cache un rythme faible (Claude lit planche d'images et durées, §18 ; Cabezer regarde l'aperçu muet).

### 13.2 Compatibilité avec le skill
Tous les courts : aucune musique, SFX de la banque Pixabay audibles comme en dégustation (skill §5, §11) ; le « silence composé » ne s'y applique pas. D : aucune ambiance continue par défaut ; une ambiance discrète du lieu sous un insert muet est à proposer au premier usage et n'est posée qu'avec l'accord de Cabezer ; foley d'aliment : jamais (`audio-dialogue-sound-design-mixage.md` §15). S : nappe continue et vrai silence de 1 à 2 s avant une bascule (skill §11 ; valeurs dans `audio-dialogue-sound-design-mixage.md` §5.5), qui recouvre les silences de Baxter.

### 13.3 Éviter les clics aux raccords audio
Nedomansky pose un fondu enchaîné de 2 images aux bords des clips de dialogue (il dit « 2 images » puis « une image » : valeur à confirmer). **La version ciblée de `audio-dialogue-sound-design-mixage.md` §3.2 fait foi :**
1. Chercher le clic sur la forme d'onde (saut d'amplitude à la coupe) ; l'écoute de Cabezer confirme. Poser un fondu **seulement là où un clic ou un saut de fond est audible**.
2. Le placer **dans le silence**, sur 1 à 2 images, ou le remplacer par deux clés de volume si la coupe est serrée. Jamais sur l'attaque d'un mot ni sur un mot protégé.
3. Jamais en masse ; jamais sur les coupes serrées de D.
4. Pour un saut de fond, combler avec le silence de la pièce du même rush (skill §4).

Types de fondu croisé audio : même fiche, §3.2. Raccourci et durée par défaut : à lire dans l'interface (§16). **Réussite :** aucune coupe audible chez Cabezer, aucun début de mot atténué.

---

## 14. Quand ne pas couper

Rester large quand les gens bougent (Baxter) ; laisser une image plus longtemps que confortable si c'est justifié (§9.3) ; laisser musique ou regard porter la scène (plage de *Top Gun: Maverick*, répliques retirées) ; ne pas couper sur le début d'une action (Murch) ni sur chaque coup d'un gag ; ne pas trop raccourcir : l'information tue l'émotion.

**Test :** « que perd le spectateur si je ne coupe pas ici ? » Si rien, ne pas couper.

---

## 15. Passes et regard neuf

**Passes** (ordre du skill §3) : brief (§3.1), découverte (§3.2), assemblage de la scène entière, montage fin à l'image près (« une image de moins ? », Hamilton), son quand la structure est stable, verrouillage et contrôles (skill §13, §14). Accepter de reprendre une scène.

**Regard neuf :** demander « pourquoi », pas seulement « est-ce que ça marche » ; laisser une scène vivre dans le montage complet avant de la juger ; regarder le tout, pas seulement le plan (Nedomansky).

### 15.1 Copie de référence (transposition de la « peau » de Murch)
Murch exporte le film, place cette copie au-dessus de la timeline et la découpe là où il modifie ; la lecture suivante montre les zones changées. **Aucune source ne décrit cette méthode dans Premiere : transposition à tester sur copie.** « Enregistrer sous » une nouvelle version ; exporter la séquence en vidéo seule, codec léger ; l'importer sur la piste vidéo la plus haute ; découper la copie aux endroits modifiés ; avant l'export final, la retirer et vérifier qu'aucune piste ne reste masquée.

**Quand :** S, F, P. **Éviter :** Shorts et TikToks de 3 minutes (séquence source et séquence montée suffisent, skill §3).

---

## 16. Procédures Premiere Pro

**Raccourcis (skill §3).** N'utiliser aucun raccourci tant qu'il n'a pas été lu dans Premiere > Keyboard Shortcuts (Raccourcis clavier) sur la machine de Cabezer (interface en anglais) ; sinon passer par la commande de menu. Consigner raccourcis et libellés lus dans `Suivi/environnement-verifie.md` (`pilotage-environnement-reprise.md`). Les raccourcis d'édition courants, marqués « à confirmer », sont dans `premiere-pro-avance.md` §4.

**Versions.** Ne pas affirmer une version, une date ou un statut de fonction : la version lue dans l'application fait foi (`pilotage-environnement-reprise.md`). Libellé non lu = « libellé à confirmer ».

### 16.1 Retailler une coupe avec feedback chiffré (Murch)
1. Repère sur le point d'édition ; mode trim par double-clic (geste à confirmer). 2. Ajouter ou retirer des images ; lire le décalage affiché (+1, −4) : affichage vu dans CC 2015, à vérifier. 3. Comparer trois valeurs (§9.4) et noter la retenue.

### 16.2 Ralenti
Réservé aux inserts (skill §7), jamais sur la parole ni la bouchée retenue. Vitesse constante : clic droit > Speed/Duration (Vitesse/Durée, libellé à confirmer). Rampe : Time Remapping (Remappage temporel) avec images clés lissées. Vérifier la cadence du rush (50/60p) avant de promettre un ralenti. Schoonmaker ralentit un instant pour souligner un regard, puis revient à la vitesse normale. **Interpolation :** ralentis sur rushs 50/60p, sinon mélange de trames ; le flux optique est interdit (réponse du 12/10/2026).

### 16.3 Fonctions IA : trois statuts (skill §16)
Le skill §16 fait foi ; ne sont rappelées que les fonctions qui touchent le montage narratif.
- **Aides autorisées, résultat vérifié :** transcription (Speech to Text), montage par le texte pour repérer et pré-découper (§8.4), détection des changements de plan, recherche Media Intelligence, Auto Reframe comme point de départ, détection de mots de remplissage (repérage, jamais suppression automatique).
- **Seulement sur demande explicite de Cabezer :** Extension générative (Generative Extend), Morph Cut, Remplissage d'après le contenu, tout outil Firefly. Si un plan manque d'une demi-seconde : un autre plan réel, un ralenti d'insert, un fondu, un plan de coupe, dans cet ordre.
- **Interdits par défaut (règle de Cabezer) :** Enhance Speech (Améliorer la parole), Auto Match (Correspondance automatique) et « Dynamics » (Dynamique) d'Essential Sound, images ou animations générées par IA (voix ou musique produites par un modèle génératif : seulement sur demande explicite, skill §16). Si une fonction manque dans sa version, le dire.

---

## 17. Procédures After Effects

Toutes les animations graphiques se font dans After Effects en calques natifs (skill §1, §16). Pour le montage narratif, AE sert à caler une animation sur une coupe ou à lier deux plans par un élément graphique. Courbes, expressions et éléments de la DA v2 : `after-effects-motion-design.md` §5, §6, §9.

### 17.1 Caler une animation sur une coupe
1. Dans Premiere, noter le temps de la coupe qui déclenche l'animation. 2. Dans AE, poser un marqueur de composition au même temps. 3. Animer à partir du marqueur. Exemple générique sur l'Échelle (à tester dans sa version ; exige un marqueur dans la composition) :
```
t = time - thisComp.marker.key(1).time;   // temps écoulé depuis le marqueur 1
s = ease(t, 0, framesToTime(4), 0, 100);  // 0 → 100 % en 4 images, accélération douce
[s, s]
```
`ease`, `framesToTime` et `thisComp.marker.key()` font partie du langage d'expressions d'AE. Ce n'est pas un élément de la DA v2 (pop 0 → 118 → 96 → 100 % en 7 images, skill §5.1).

### 17.2 Courbes
Tout mouvement progressif (échelle, position) est lissé en Bézier / Progressif, jamais linéaire (skill §7) : sélectionner les images clés, appliquer Easy Ease (Animation > Keyframe Assistant, repère français : Assistant de clés ; libellé à confirmer ; raccourci à lire dans AE), affiner dans l'éditeur de graphiques (Graph Editor). Deux exceptions qui ne sont pas des défauts : un **punch-in sec** est un changement instantané (clé maintenue ou deux clips) ; la **vitesse constante** est permise pour une rotation continue, un défilement, un compteur ou une boucle.

### 17.3 Remappage temporel
Pour un plan filmé seul, le ralenti se fait dans Premiere (§16.2). Dans AE, seulement pour une composition qui contient déjà un plan dans un habillage : Layer > Time > Enable Time Remapping (repère français : Calque > Temps > Activer le remappage temporel ; libellé à confirmer). AE crée une image clé au début et à la fin du calque (aide Adobe, résumé) ; option grisée sur un calque d'animation : précomposer d'abord (fil Adobe, à vérifier). **Rampe :** deux images clés intermédiaires, Easy Ease. La bouchée retenue n'est jamais ralentie.

---

## 18. Contrôles par script

Les commandes ffmpeg/ffprobe (tableau « usage, commande, seuil ») et les scripts nommés vivent dans **`organisation-livraison-qc.md` §6** : `mesure-plans.py`, `xml-coupes.py`, `lister-clips.jsx`, `lint-srt.py`, `controle-mp4.sh`. Ne pas les recopier ici ; cette section dit quoi en demander pour le montage narratif. Ils signalent des cas à revoir, sans remplacer visionnage et écoute (skill §14). Tout script reste marqué « testé sur fichiers générés » tant qu'il n'a pas tourné sur un vrai export de Cabezer (statut au skill §20). Lire tout fichier externe (XML, SRT, transcription) avec `python3 -I`.

### 18.1 Cadence et taille
`controle-mp4.sh` (§6.2 de la fiche d'organisation). Vérifier la cadence avant de convertir des durées en images (§5.4).

### 18.2 Coupes et durée des plans
`mesure-plans.py` (paramètres : seuil, fenêtre, sortie CSV). Seuil de départ 0,3 : il manque les fondus enchaînés et les coupes entre plans proches. Lire le résultat avec §9.5.

### 18.3 Images autour d'une coupe
Commande propre à ce domaine (essayée sur un fichier de test, ffmpeg 6.1 ; adapter fenêtre et `tile` à la cadence). Quatre images dans 0,16 s autour d'une coupe à 2,00 s :
```
ffmpeg -y -i montage.mp4 -vf "select='between(t,1.92,2.08)',scale=160:-1,tile=4x1" -frames:v 1 -an coupe.png
```
Regarder : mouvement non montré deux fois, ni œil mi-clos ni bouche en plein mot sur la première image entrante (§4.4). Planches de contact : fiche d'organisation §6.3.

### 18.4 Silences, noirs, images figées, niveau
Utiliser le tableau de la fiche d'organisation §6 (blancs à vérifier, son manquant, fin d'un mot protégé, noirs, figements, ebur128). Pour la note de rétention des courts (skill §5.2), n'employer que la méthode étalonnée du skill (18 dB sous le 80e centile sur 4 s, voix seule). `freezedetect` signale aussi les plans fixes volontaires : interpréter avant de corriger. Le loudness est un repère, pas une cible (`audio-dialogue-sound-design-mixage.md` §9).

### 18.5 Coupes et transitions de la timeline
`xml-coupes.py` lit un export FCP XML (voie de secours, `premiere-pro-avance.md` §13) et liste coupes, trous et transitions (un `<start>` de −1 indiquerait une transition : à confirmer sur un export réel). `lister-clips.jsx` lit la piste V1 sans rien modifier ; ExtendScript sert tant que le test de fumée de `pilotage-environnement-reprise.md` le confirme, UXP est préféré pour un nouvel outil.

---

## 19. Tableau par famille

Raccords : §5.0 ; transitions : §5.4 ; plans de coupe : §7.

| Technique | D | F | S | P | T | H |
|---|---|---|---|---|---|---|
| Règle des six | Après les seuils du skill | Oui | Oui (histoire d'abord) | Oui | Oui (histoire d'abord) | Oui |
| J-cut / L-cut | Jamais sur bouchée ni réaction ; B-roll sous voix | Oui | Oui | Oui | Oui | Oui |
| Respiration après le dernier mot | Non | Oui, au verdict | Oui | Oui, moments d'émotion | Non | Selon brief ; Lifestyle posé : oui |
| Tenir un plan sans parole | Non | Oui | Oui | Oui | Non | Selon émotion |
| Montage parallèle | Hook seulement | Rare | Oui | Oui | Rare | Cas par cas |
| Montage par le texte | Aide, recaler, seuil 0,25 s | Aide | Aide, garder respirations | Aide | Aide | Aide |
| Copie de référence | Non | Oui | Oui | Oui | Possible | Selon durée |

« Non » : le skill ou le style de la famille l'écarte. « Cas par cas » ou « selon brief » : consulter le brief (§3.1).

---

## 20. Erreurs de débutant → réflexes de pro

| Erreur de débutant | Réflexe de pro |
|---|---|
| Couper sans brief ni lecture de toute la transcription | Brief écrit, puis deux passages : sentir, puis marquer (§3) |
| Sauver un raccord au prix de l'émotion | Règle des six : sacrifier le bas de la liste (§2) |
| Couper pendant le mouvement | Couper après le pas, sur le temps fort (§4) |
| Un B-roll par mot | Une image par idée, avec une ligne de justification (skill §6) |
| Cacher un jump cut de dégustation par un plan non demandé | Punch-in ou coupe franche (§5.3) |
| Se fier aux temps de la transcription | Recaler à la forme d'onde et à l'énergie du son (skill §4) |
| « Supprimer toutes les pauses » | Garder celles qui portent un regard ou une émotion (S) |
| Fondu audio en masse ou qui mord un début de mot | Fondu dans le silence, 1 à 2 images, seulement où un clic est audible |
| Laisser la transition à 1 s par défaut | Fixer la durée en images à la pose (§5.4) |
| Transition intégrée générique de Premiere (iris, glissement) | Coupe franche, fondu, ou transition construite dans AE |
| Juger un rythme avec le son parfait | Contrôler le rythme visuel sans le son, mesurer les plans |
| Couper une pause sans mesurer le sens | Relire la phrase recollée (§8.1) |
| Écrire « écouté » pour une mesure | « Mesuré, non écouté » ou « écouté par Cabezer » |
| Modifier sans version | « Enregistrer sous » avant toute modification (skill §1) |

---

## 21. Liste de contrôle

- [ ] `Suivi/brief.md` lu ; famille, promesse (confirmée avant la 30e seconde) et niveau d'autonomie connus ; exceptions de la famille (skill §2) prioritaires sur cette fiche.
- [ ] Chaque coupe contestée est arbitrée par la règle des six, avec le critère sacrifié nommé.
- [ ] Aucune coupe ne montre deux fois le même mouvement (§18.3) ; coupes de voix recalées à la forme d'onde, aucun début de mot mordu.
- [ ] Aucune phrase recollée ne change le sens de ce que la personne a dit.
- [ ] J-cut / L-cut : aucun bout de phrase supprimée ; aucun sur bouchée ou réaction en D.
- [ ] Chaque plan de coupe apporte une information ou masque une coupe voulue.
- [ ] Transitions relues : une raison écrite et une durée en images chacune ; aucune dans les courts hors whip et flash de C-Food ; coupe franche par défaut en long, fondus seulement en fin de Story ou sur demande.
- [ ] Respirations gardées (S, moments d'émotion de P, verdict de F, Lifestyle posé) ou coupées selon le skill §4 ailleurs.
- [ ] Zones longues et courtes listées (§18.2) et justifiées ; rythme visuel contrôlé sans le son ; écoute finale demandée à Cabezer.
- [ ] Aucune fonction IA hors des aides autorisées ; raccourcis et menus lus sur l'interface réelle.
- [ ] Suivi : appliqué / contrôlé (mesuré, extrait) / validé par Cabezer.

---

## 22. Décisions à demander

> **Toutes ces questions ont reçu une réponse de Cabezer le 12/10/2026** : voir `../decisions-en-attente.md`, qui prime sur tout autre passage.

| Question tranchée | Réponse de Cabezer |
|---|---|
| Étendre l'exception « Respirations » aux moments d'émotion de films/séries et au verdict d'un food long ? | Oui : respirations gardées en films/séries (moments d'émotion) et au verdict du food long, en plus de la Story et du Lifestyle posé. |
| Durées de départ des transitions (§5.4) | Coupe franche par défaut en long ; fondus rares (fin de Story ou sur demande). Durée fixée en images à la pose, vérifiée sur l'extrait. |
| Fondu enchaîné de calme, cut au noir, noir dans un gag | Seulement sur demande, avec deux versions sur un extrait. |
| Interpolation par flux optique pour les ralentis d'inserts | Non : ralentis sur rushs 50/60p, sinon mélange de trames. |
| Morph Cut sur un face caméra stable | Seulement sur demande. |

## 23. Sources étudiées

Couverture : **transcription lue en intégralité** (sous-titres automatiques YouTube non relus, noms propres parfois déformés) ; **extrait de recherche** (résumé de résultats web, page non ouverte : le réseau de la session refuse helpx.adobe.com, adobe.com, Wikipedia, StudioBinder et d'autres hôtes) ; **non lu**.

**Vidéos et conférences (transcriptions lues)**
1. Walter Murch, « Making the Right Editing Choices & Switching to Adobe Premiere Pro CC », Adobe Creative Cloud, 2015. https://www.youtube.com/watch?v=zprzAROe9i4. Règle des six, mouvement, clignement, trim en images, « peau ». Version CC 2015.
2. StudioBinder, « The Book Every Editor Has to Read — Walter Murch… », 2024. https://www.youtube.com/watch?v=PKYeClvvlTw. Résumé secondaire : règle des six, règle des 30°.
3. Vashi Nedomansky, « The 7 Laws of Film Editing », This Guy Edits, 2019. https://www.youtube.com/watch?v=i9mGSDluh9g. Double visionnage, organisation, fondus audio.
4. Steve Hullfish, interview This Guy Edits. https://www.youtube.com/watch?v=Ehvh5adVqMo. Réaction contre réplique à l'écran.
5. Thelma Schoonmaker, « Rare 17-minute interview… », Making the Cut (mise en ligne 2020, date de 1993 non vérifiée). https://www.youtube.com/watch?v=21jVGsqMYgs. Prises classées, coupes rugueuses, ralenti.
6. Eddie Hamilton, StudioBinder Academy, 2024. https://www.youtube.com/watch?v=sTukWT1s3ms. Passes, compression, son, intercut du briefing.
7. Tony Zhou, « How Does an Editor Think and Feel? ». https://www.youtube.com/watch?v=3Q3eITC01Fg. Yeux, durée de l'émotion ; contient la citation « 70 % » non utilisée.
8. Tony Zhou, « Satoshi Kon — Editing Space & Time », 2014. https://www.youtube.com/watch?v=oz49vQwSoTE. Match cuts, ellipse.
9. Tony Zhou, « Jackie Chan — How to Do Action Comedy ». https://www.youtube.com/watch?v=Z1PCtIaM_GQ. Action et réaction, décalage de trois images.
10. Tony Zhou, « Joel & Ethan Coen — Shot | Reverse Shot », 2016. https://www.youtube.com/watch?v=5UE3jz_O_EM. Champ-contrechamp, rythme non verbal.
11. Kirk Baxter, The Editing Podcast, 2023. https://www.youtube.com/watch?v=J4cdr_HFnuI. Étirer / exploser, clignements, écoute.

**Pages web (extraits de recherche, pages non ouvertes)**
- Pixel Valley Studio, « The Cross Dissolve: Its history… ». https://pixelvalleystudio.com/pmf-articles//the-cross-dissolve-its-history-process-in-film-and-lots-of-interesting-facts. Fondus de 24 à 48 images, dissolves de 6 à 12 images contre les jump cuts (§5.4).
- MasterClass, « What Is a Dissolve in Filmmaking? ». https://www.masterclass.com/articles/what-is-a-dissolve-in-filmmaking-how-to-know-when-to-use-a-dissolve-transition. Même fourchette de 24 à 48 images.
- Boris FX, « Dissolve Transition Tutorial 2024 ». https://borisfx.com/blog/dissolve-transition-tutorial-2024-what-are-dissolves/. Même fourchette.
- Adobe, « Video dissolve transitions in Premiere » (page sous /premiere/desktop/ : produit exact à confirmer). https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/list-of-video-dissolve-transitions.html. Types de fondu, avertissement sur Dip to Black et les pistes inférieures.
- Adobe, « Change transition duration in Premiere » (même réserve). https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/change-transition-duration-using-the-effect-controls-panel.html. Durée par défaut de 1 s.
- Elephorm, « Maîtriser les Transitions dans Premiere Pro ». https://www.elephorm.com/formation/maitriser-les-transitions-dans-premiere-pro. Noms français indicatifs des fondus.
- Adobe, « Time-stretching and time-remapping » (After Effects). https://helpx.adobe.com/ca/after-effects/desktop/animate-in-after-effects/time-stretching-and-time-remapping/time-stretching-time-remapping.html. Image clé au début et à la fin du calque.
- RedShark News, montage par le texte. https://www.redsharknews.com/how-to-delete-pauses-and-filler-words-with-text-based-editing. Suppression des pauses et mots de remplissage.
- No Film School, J-cuts en une étape. https://nofilmschool.com/one-step-j-cuts-premiere-pro. Geste de J-cut.
- PlayPlay (https://playplay.com/glossary/cutaway-shots), MasterClass (https://www.masterclass.com/articles/cross-cutting-explained) : définitions du plan de coupe et du montage alterné.
- PBS Standards, montage éthique d'un entretien. https://www.pbs.org/standards/blogs/standards-case-studies/ethically-editing-an-interview. Cas du silence conservé.
- Filmdaft, règle des six (pourcentages écartés). https://filmdaft.com/walter-murchs-rule-of-six-the-editors-formula-for-choosing-the-right-cut/.

**Non lus ou inaccessibles :** les livres de Murch, Pearlman et Hullfish ; plusieurs vidéos YouTube bloquées (Murch « six criteria », Joe Walker sur *Dune*, Baxter sur *Gone Girl*, Edgar Wright, Pearlman) ; pages du réseau refusé. Aucun monteur documentariste lu. Les durées de transition du §5.4, hors fourchettes citées, sont des valeurs de métier non sourcées.
