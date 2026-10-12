---
name: "cabezer-premiere-shorts"
description: "Monter les vidéos de Cabezer à un niveau professionnel dans Premiere Pro et After Effects : dégustations courtes (TikTok, Shorts, Reels), food long, Cabezer Story, films/séries (PRISME), tech et tout autre format. Couvre dérush, structure et rythme, habillage par famille (animations graphiques uniquement dans After Effects), sous-titres, étalonnage, audio et mixage, déclinaisons, export, contrôle qualité et reprise de projet. À utiliser pour tout montage ou partie de montage d'une vidéo de Cabezer. Pas pour la génération vidéo, les miniatures ou la publication seules."
---

# Montage Cabezer — Premiere Pro et After Effects, niveau professionnel

Ce fichier contient les **règles actuelles** de Cabezer et l'index des **fiches pro** (§19). Version 3 du 12/10/2026, réponses de Cabezer intégrées le même jour : contradictions de la v2 résolues, règles restées dans l'historique remontées dans le corps, méthodes de monteurs professionnels ajoutées. Les consignes datées et leur chronologie sont dans [l'historique](references/historique.md) ; les détails propres à des projets passés sont dans [projets Cabezer](references/projets-cabezer.md).

**[Q]** marque une décision qui attend Cabezer : appliquer le défaut (écrit dans le texte ou dans le registre, §20), le noter dans `Suivi/decisions.md`, poser la question une fois, seulement quand elle bloque.

**Fichiers cités introuvables :** le dire, demander le fichier, continuer avec le résumé de ce skill marqué « non vérifié ». Ne jamais deviner le contenu d'une fiche absente.

## 1. Priorités, portée et arbitrage

**Une seule règle d'arbitrage :** 1) brief du jour de Cabezer ; 2) exception de famille de ce skill ; 3) règle générale de ce skill ; 4) fiches de référence (`references/`, dont `references/pro/`) ; 5) plugins et tutoriels. À niveau égal, la consigne datée la plus récente l'emporte. Une valeur de tutoriel n'est jamais une règle universelle.

- S'applique à tous les montages Cabezer, dans tous les dossiers et formats. Le nom historique « shorts » ne limite pas la portée. Ne pas imposer le vertical à une vidéo longue.
- **Familles :** D dégustation courte, F food long, S Cabezer Story (société/documentaire), P films/séries (PRISME), T tech. Identifier la famille d'abord (tableau §2). **Hors familles (H)** — vlog, interview, pub, clip… : le dire à Cabezer, appliquer les règles générales (§3, §4, §7 à §14), n'appliquer aucune identité avant validation d'un extrait de 15 à 30 s, lire [adaptation et genres](references/pro/adaptation-genres-analyse-de-style.md).
- **Premiere Pro = timeline maîtresse.** Ne jamais remplacer silencieusement Premiere par un autre éditeur.
- **Animation : définition (consigne du 30/09/2026, précisée en v3).**
  - *Animation graphique* = tout élément créé : texte, pastille, prix, note, emoji, forme, schéma, carte, sous-titre animé, flash ou glitch graphique, transition graphique, parallaxe 2.5D. **Uniquement dans After Effects**, en calques natifs modifiables (« les animations se font uniquement par AE et non par génération comme avant »). Allers-retours avec Premiere sans redemander la permission. Détail §16.
  - *Traitement d'un plan filmé* = punch-in sec, zoom façon Micode, whip ou shake du cadre, speed ramp, recadrage, Auto Reframe, stabilisation, fondu, mouvement sur une photo ou un document qui désigne un détail. **Autorisé dans Premiere.**
  - Un script peut piloter AE (compositions, calques, clés) ; il ne fabrique jamais d'image hors d'AE. Les vrais emojis Apple rendus par macOS sont des sources autorisées.
- Avant de modifier un montage existant : **Enregistrer sous** une nouvelle version. Tester d'abord sur une copie et un aperçu court quand Cabezer demande un essai sur un projet ouvert.
- **Validations :** faire valider le dérush avant l'habillage, sauf autorisation explicite d'enchaîner (« fais ça de manière autonome », « export final direct »). Une autorisation d'enchaîner n'autorise jamais la publication.
- **Mode autonome — défauts :** hook = son hook habituel, noté (§5.2) ; langue des sous-titres à l'étranger = anglais ; téléchargement = jamais sans accord (s'en passer) ; toute validation manquante est notée « en attente » dans `Suivi/decisions.md` et rappelée à la livraison.
- Distinguer toujours **appliqué / contrôlé / validé par Cabezer / publié**. Un import n'est pas un montage ; un export lancé n'est pas un export validé ; une méthode écrite n'est pas un preset créé. **Claude n'entend pas :** il contrôle par mesures, transcription et forme d'onde ; une mesure n'est jamais une écoute, et l'écoute finale revient à Cabezer.
- **Payant :** gratuits uniquement par défaut. Tout outil, plugin, banque ou service payant est signalé (nom, prix connu ou « à vérifier ») et attend l'accord de Cabezer.

## 2. Règles par famille — vue rapide

| Règle | D Dégustation (TikTok/Shorts/Reels) | F Food long | S Story | P Films/séries | T Tech |
|---|---|---|---|---|---|
| Sous-titres | Incrustés toujours ; **français** mot à mot en France et Belgique ; à l'étranger **langue locale ou anglais, à demander** (défaut anglais) ; masqués pendant les textes animés (§9) | France : SRT français seulement, rien d'incrusté (réponse du 12/10/2026) ; étranger : anglais incrusté, 2 lignes max | Idem F | Idem F | Idem F, vocabulaire accessible |
| Musique | **Absente** (choix de Cabezer, sauf demande) | Selon émotion ; composition originale (§11) | Nappe continue ~24 dB sous la voix, silences de bascule ; composition originale (§11) | Bibliothèque perso | Selon émotion ; composition originale (§11) |
| SFX | Banque Pixabay dédiée, liste de référence (§5), sans mèmes vocaux ni boom, audibles | Bibliothèque ouverte, audibles | Idem F ; aucun bruitage sans élément visuel correspondant | Idem F | Idem F |
| Zoom facecam | Punch-ins secs 100/115 %, 120 % sur les bouchées ; shake + flash sur les gros moments ; whip entre deux lieux | Zoom avant/arrière façon Micode, seulement si pertinent | Idem F ; déplacements libres sur documents | Zoom Micode sur son visage seulement, jamais d'aller-retour continu (rejeté sur Dune) | Idem F |
| Identité | DA Dégustation v2 (§5.1) | Charte à créer sur un extrait de 30 s à valider (§6) | Méthode Micode/Amistory ; identité visuelle à refaire entièrement (v15 supprimée le 12/10/2026) | PRISME v1 | Liquid Glass |
| Durée | ~3:00 max en TikTok | Selon récit | Selon récit | Selon brief | Selon brief |
| Blancs | Coupés au-delà de 0,25 s dans les monologues (§5) | Coupe au dernier mot ; respiration gardée au verdict (§4) | Respirations qui portent gardées (§6) | Coupe au dernier mot ; respirations d'émotion gardées (§4) | Coupe au dernier mot (§4) |
| Coupe bouchée | Courte : arrivée en bouche → morsure → réaction ; hook et rétention notés /10, minimum 8 (§5.2) | Dégustation complète | — | — | — |

## 3. Flux de travail

Créer au début une liste de suivi avec ces étapes **distinctes** ; ne jamais fusionner couleur et mixage dans une passe « finitions ».

0. **Brief** (`Suivi/brief.md`) : famille ; destinations et formats ; durée cible ; promesse en une phrase ; ce que le spectateur doit comprendre ou ressentir ; partenariat, produit offert ou invitation (mention obligatoire, §8) ; personnes ou données à protéger ; références éventuelles ; échéance ; niveau d'autonomie. En dégustation, demander aussi le hook et la langue à l'étranger (§5).
1. **Préparation.** Copier les rushs d'une carte amovible avec vérification par somme de contrôle, conserver les originaux. Arborescence : `Media/` (Rushs/<caméra>, Assets, Audio, Proxys), `Projet/` (.prproj et .aep versionnés), `Exports/` (Brouillons, Final), `Controles/`, `Suivi/`. Lire chaque rush avec ffprobe : durée, cadence (variable ?), orientation, profil couleur (D-Log M, V-Log, HLG/Apple Log, Rec.709), audio (Cabezer enregistre en 32 bits flottant). Garder une séquence source et une séquence montée. Première session sur une machine : test de fumée et `Suivi/environnement-verifie.md` ([pilotage](references/pro/pilotage-environnement-reprise.md)).
2. **Transcription et dérush** (§4). Transcrire le rush réel ; ne jamais prendre le script comme preuve de ce qui a été dit. Vérifier les faits (§8). → **Validation du dérush.**
3. **Format.** Ratio et résolution selon la destination ; cadence de séquence = celle de la majorité des rushs, les autres conformées. Recadrer en protégeant yeux, mains, gestes et produit ; recadrer depuis les rushs 4K, jamais depuis un export 1080p.
4. **Structure et habillage.** Cartographier mise en place → progression → réponse. Écrire la promesse et vérifier qu'elle est montrée avant la 30e seconde. Appliquer l'identité validée de la famille (§6) ; si elle manque, faire valider un extrait avant de généraliser. Illustrations et animations AE en une passe. Hook finalisé en dernier, une fois la structure stable.
5. **Zooms et mouvements** (§7).
6. **Colorimétrie** (§10).
7. **Musique, SFX, ambiances, mixage** (§11).
8. **Sous-titres** (§9).
9. **Contrôles avant export** (§14) puis export (§13).
10. **Revue du MP4 exporté** : visionnage intégral du MP4, image par image aux points sensibles, mesures après encodage, transcription de contrôle ; aperçu à Cabezer pour le visionnage et l'écoute, avec les limites réelles du contrôle.
11. **Après publication** : boucle rétention (§15) quand les données existent.

Pour les dégustations, ranger le projet dans `/Users/cabezer225/Documents/ChatGPT/Tiktok degustation/<Sujet>/` (médias, versions, exports, contrôles, suivi ; `Publication/` si couverture et textes sont demandés). Pour le package de publication, utiliser `cabezer-shorts-publication` ou `youtube-publication-package`.

**Dossier `Suivi/` :** `brief.md`, `decisions.md` (décisions et questions **[Q]**), `retours.md` (retours datés avec timecode), `journal.md` (état pour qu'une nouvelle session reprenne), `environnement-verifie.md` (versions, libellés et raccourcis lus), `licences.csv` (registre unique : images, vidéos, sons, musiques, polices), `verifications.md` (faits). `LICENCES-SFX.md` de la banque dégustation reste en place.

**Travail multi-agents :** quand Cabezer demande plusieurs agents, leur confier des missions séparées (ex. dérush, habillage AE, recherches/illustrations) ; un seul coordinateur intègre dans le projet maître.

**Pilotage de l'ordinateur** ([fiche](references/pro/pilotage-environnement-reprise.md)) : identifier la version et les panneaux réellement présents ; vérifier l'effet de chaque geste par une capture ; aucun raccourci tant qu'il n'a pas été lu dans Raccourcis clavier sur sa machine, sinon passer par le menu ; consigner libellés et raccourcis lus. Si un panneau bloque, décrire le blocage et conserver les étapes vérifiées.

**Scripts de contrôle :** ceux de `references/pro/scripts/` qui ne font que lire (relevé du Mac, contrôle du MP4, coupes, sous-titres, typographie, flashs, contraste) se lancent sans redemander (réponse du 12/10/2026) ; résultats dans `Controles/`. Tout script qui modifie ou copie un fichier attend l'accord de Cabezer.

**Méthode de fabrication :** interface ou UXP pour les réglages natifs ; FCP XML pour un premier assemblage (pièges §14, limites dans [Premiere avancé](references/pro/premiere-pro-avance.md)) ; ExtendScript pour piloter AE et pour les contrôles, tant qu'un test de fumée le confirme sur sa machine.

**Montage long (20 à 40 min) :** une séquence par partie, imbriquées dans une séquence maîtresse ; Production Premiere si le projet devient lourd ; un point de contrôle (version enregistrée + ligne de `journal.md`) à la fin de chaque session.

## 4. Dérush et intention du créateur

- Lire d'abord toute la transcription et marquer les moments forts ; classer les prises (meilleure, deuxième) et garder deux options sur les moments émotionnels.
- Garder sa voix orale, ses connecteurs qui portent le rythme et ses réactions. Retenir la meilleure prise complète ; couper essais abandonnés et phrases reprises sans changer le sens.
- **Coupe par défaut :** juste après le dernier mot entièrement audible, sans blanc résiduel ; ne jamais couper le début du mot suivant (syllabe ou consonne). Un blanc reste seulement s'il est occupé par une illustration, une transition ou un effet prévu. Placer les coupes à la forme d'onde et à l'énergie du son, jamais aux seuls timecodes de transcription ni avec une marge fixe. Exceptions par famille : blancs de dégustation (§5) ; **respirations** (§6) en Story, et aussi aux moments d'émotion de films/séries et au verdict du food long (réponse du 12/10/2026) : garder le regard ou le silence qui porte l'émotion, jamais un blanc où il cherche ses mots.
- **Montage par le texte** de Premiere : seulement pour repérer et pré-découper ; chaque coupe est ensuite recalée à la forme d'onde ([audio §3.1](references/pro/audio-dialogue-sound-design-mixage.md) donne un script d'affinage).
- **Corrections :** retirer un faux départ pour garder ce que Cabezer voulait dire est permis (ses exemples §5) ; jamais un collage qui crée une affirmation qu'il n'a pas faite ni ne change le sens. Relire chaque phrase recollée : la reconnaîtrait-il ?
- **Fondus audio :** seulement là où un clic est audible, 1 à 2 images dans le silence ; jamais en masse sur les coupes serrées, jamais sur l'attaque d'un mot.
- **Room tone :** si une coupe laisse un saut de fond sonore audible, combler avec le silence de la pièce du même rush plutôt que de laisser un trou numérique.
- **À protéger toujours :**
  - son **« Bref, c'est partiiii »** : le garder à chaque fois qu'il le dit, dans toutes les vidéos, entier jusqu'à la fin de la dernière syllabe étirée ; placer la sortie après l'extinction réelle du son (consigne du 28/09/2026, Maritozzo). Cette signature prime sur la coupe des mots étirés ;
  - la fin des exclamations étirées (« enfin ! », « waouh ») : attendre la fin réelle de la voix avant de couper ;
  - les passages où Cabezer parle de donner ou faire plaisir à sa famille et ses proches, et les moments humains qui montrent son intention ;
  - l'**appel au commentaire de fin** (« commentez le mot… ») avec le mot réellement prononcé : ne jamais le retirer, le vérifier dans la séquence puis dans l'export. Ne jamais l'inventer s'il n'a pas été tourné : le signaler à Cabezer.
- Le rythme vient du discours et des changements de valeur de plan, pas d'effets à chaque mot. Couper en fin de pensée ; pour arbitrer une coupe difficile : émotion, puis histoire, puis rythme, puis regard, puis géographie de l'image ([fondamentaux](references/pro/fondamentaux-montage-narratif.md)).
- **Motif récurrent :** quand le récit s'y prête, installer un repère (phrase, plan, carte, son) lié à un point à retenir, le reprendre aux articulations puis le varier. Ouvrir une boucle au début et la refermer à la fin ; marquer chaque boucle et son payoff dans les marqueurs de séquence.
- Après validation du dérush et des retouches manuelles de Cabezer, préserver ses coupes et la voix traitée pendant l'habillage.
- Scripts prompteur : phrases complètes, pas de retour à la ligne forcé en milieu de phrase.

Références : [techniques retenues](references/techniques-et-controles.md), [notes par vidéo](references/tutoriels-2026-09-12.md), [méthode antérieure](references/methode.md), [récit, regard et rythme — Aprilynne Alter](references/aprilynne-recit-regard-rythme.md), [audio, automatismes, motifs](references/tutoriels-2026-09-14.md), [fondamentaux pro](references/pro/fondamentaux-montage-narratif.md).

## 5. Vidéos courtes de dégustation

**Direction actuelle : DA Dégustation v2 (02/10/2026)**, fiche complète `/Users/cabezer225/Documents/ChatGPT/Tiktok degustation/Identite-Degustation/DA-Degustation-v2.md`, à lire avant chaque dégustation.
- **Origine :** ses réponses au questionnaire du 02/10, après le rejet du Milan v01 (« SFX pas ouf, pops nuls, dérush pas dynamique, effets pas clean »), et l'analyse de 6 de ses reels (`Tiktok degustation/References-Cabezer/`).
- **Principe :** reprendre **sa propre base** et l'améliorer. Elle remplace la direction Johan Papz et les stickers détourés.
- Lire aussi [formats courts](references/pro/formats-courts-verticaux.md) et [styles food et tech](references/pro/styles-food-et-tech.md) ; elles ne changent pas la DA.

**Sa base, à garder :** sous-titres incrustés tout du long ; étiquette produit + prix près du produit ; gros plan « regardez-moi l'intérieur » ; note sur 10 ; bouchée en plan serré ; appel au commentaire avec un mot-clé ; surtout des coupes franches ; débit de 3,6 à 4,2 mots par seconde après dérush (contrôle, jamais de voix accélérée).

**Au démarrage, demander à chaque vidéo :**
- **Le hook.** Son hook habituel ; un hook agressif fait de plusieurs extraits rapides des rushs ; ou un teaser produit de 0 à 1,3 s sous sa voix, avec une étiquette d'enjeu (Milan : « 19h30 · Luini ferme à 20h ⏰ »). Pas de photos, pas de bouchée tronquée. Noter le hook choisi avec le barème §5.2.
- **La langue des sous-titres, à l'étranger** (§9).

**Dérush — dynamique naturel et clarté (consignes du 02/10/2026, issues de ses propres reprises) :**
- **Blancs :** couper respirations et blancs de plus de 0,25 s dans les monologues ; garder les réactions et les échanges. Placer les bords à l'énergie du son, pas aux temps de Whisper (qui étire les mots), en protégeant les mots dits doucement.
- **Hésitations :** les couper, même un seul mot étiré (« Et on… », « une… » avant un nom) ; sa signature « Bref, c'est partiiii » n'est jamais une hésitation.
- **Corrections :** ne garder que la bonne version, comme dans ses reprises : « Voici les panzerottis / Non, panzerotti / OK » devient « Les gars, voici les panzerotti en personne » ; « un peu plus gras… enfin plus généreux » devient « plus généreux » ; « deux mozzarelles… trois, trois » devient « trois mozzarelles ».
- **Redites et passages où il tourne en rond :** les couper, pour que les explications soient claires.
- **Restes autour d'une coupe :** retirer la phrase entière, y compris les petits morceaux juste avant ou après (deux « c'est bon » restés avant une redite). Retirer aussi un plan sans parole qui traîne après une phrase. Relire chaque segment de moins de 1,5 s voisin d'une coupe.
- **Avant d'appliquer une coupe :** la tester sur le son source (retranscription du passage recollé).
- **Contenu gardé :** arrivée et lieu, commande, potes, moments hors sujet, en version courte. Durée jusqu'à 3:00.
- **Ses coupes priment :** ne pas retirer un passage qu'il a gardé dans son propre dérush sans le lui demander.

**Préparation :** quand il annonce le produit (« on va tester les… »), poser un plan de préparation sous sa voix.
- D'abord le chercher dans les rushs.
- À défaut, une vidéo stock appétissante sous licence (Pexels, Pixabay) : téléchargée seulement après son accord (nom, source, taille) ; licence consignée ; même type de produit, sans logo ni lieu identifiable, jamais présentée comme le plat servi ; conformée à la cadence et au cadre de la séquence (§14).

**Coupe de la bouchée — courte** (TikTok, Shorts, Reels) :
1. Commencer à l'arrivée du produit en bouche ; retirer préparatifs, attente, approche.
2. Garder la morsure entière à vitesse réelle, en plan serré.
3. Reprendre directement à la réaction vocale utile, en protégeant le début du mot.
4. Retirer chaque « bismillah » sans toucher la bouchée suivante.
5. Repérer ces points à l'image et à l'écoute.

Coupe courte sur tous les formats courts, y compris un Short ou Reel monté seul (réponse du 12/10/2026) ; une dégustation complète seulement sur demande.

**Prix :**
- **Étiquette « produit · prix »** (petite, près du produit) à la révélation du produit, quand le prix est connu.
- **Montant seul en grand** (pop, petit shake, caisse clairement audible) seulement aux vraies annonces : montant payé, prix par produit.
- Pas de cartouche descriptif ; sous-titres masqués pendant l'animation.

**Images :**
- **Plan produit filmé sans parole :** c'est du B-roll, à placer sous la voix quand il parle du produit.
- **Inserts muets :** toujours sans leur son source.
- **Sources :** vidéos originales, pas de photos ; produits et bouchées toujours visibles sous les textes.

**Son :**
- Pas de musique (noter « musique : absente par choix »). Pas d'ambiance continue ; une ambiance discrète du lieu sous un insert muet (§11, « ne contredit pas la règle dégustation ») est une méthode à proposer au premier usage : sans son accord, aucune. **Jamais de foley d'aliment** (bruit ajouté de croustillant, de friture…), ni sur un insert, ni sur une bouchée, ni sur une réaction (réponse du 12/10/2026).
- SFX tendance TikTok + touche mème, banque Pixabay `Tiktok degustation/SFX-Pixabay/` (licences dans `LICENCES-SFX.md`) ; « tendance » désigne un style de son, jamais un son prélevé :
  - liste de référence : swoosh, pop, ding, boing, scratch, caisse, photo, scintillement ; un autre son de la banque (riser, drone…) seulement avec son accord **[Q]** (défaut : non) ;
  - **pas de mèmes vocaux**, **plus de boom** (retiré le 02/10 : « tu l'utilises mal ») ;
  - clairement audibles, sans en mettre partout ;
  - recadrés sur leur attaque ; le swoosh est calé sur son pic.
- **Chaque SFX appartient à un élément :** si l'élément est retiré, retirer son SFX. Poser un marqueur à l'attaque de chaque élément sonorisé.

### 5.1 Habillage dégustation — DA v2 (minimal propre)

**Ce que « pas clean » veut dire pour lui :** contours épais, ombres baveuses ; sticker détouré, pictos dessinés ; tampon de ville, liseré tricolore ; animations molles.

**Charte :**
- **Police :** moderne grasse, Avenir Next Heavy et Bold.
- **France :** blanc + rouge tomate `#E63946`.
- **Voyage :** couleurs du pays seulement (Italie : rouge `#CE2B37`, vert `#009246`), sans tampon ni liseré. Fiche : `Tiktok degustation/Identite-Voyage/DA-Voyage-v1.md`.
- **Ombres :** courte et nette uniquement.

**Éléments (9:16, base 1080 × 1920 ; durées en images à 29,97 i/s, à convertir en secondes sur une autre cadence) :**
- **Étiquette :** pastille blanche à coins arrondis, texte noir Avenir Next Bold, casse normale ; glisse de 8 px en 4 images ; une étiquette « lieu » dans le hook, une étiquette « produit · prix » à la révélation du produit.
- **Prix :** montant seul, Avenir Next Heavy blanc très grand, pop + petit shake + caisse.
- **Pop-up :** **vrai emoji Apple** (rendu par macOS, `Tiktok degustation/Identite-Degustation/Emojis/`, importé et animé dans AE) + un mot court en capitales si utile ; pop 0 → 118 → 96 → 100 % en 7 images ; 2 à 4 par vidéo, seulement sur de vraies réactions.
- **Note :** « 7-8/10 » en grand + emoji, avec flash et ding.
- **Intérieur :** flash blanc (70 % → 0 en 4 images) + shake de 6 images + emoji 👀 + scintillement.
- **Appel au commentaire :** pastille « commente » + mot-clé en couleur d'accent + 👇.
- **Mouvements :** punch-ins secs en alternance 100 / 115 % aux coupes face caméra, 120 % sur les bouchées ; shake + flash seulement sur les gros moments (prix, intérieur, verdict) ; whip/swish entre deux lieux : 4 à 6 images, agrandi à 130 %, glissement de 12 %, flou de mouvement, swoosh. Ailleurs, coupes franches.
- **Pas d'ajout pour la note :** il a retiré l'étiquette « Pizza fritta · Naples » ajoutée pour relancer l'image. Relancer par punch-in, coupe ou insert, jamais par un texte qu'il n'a pas demandé.
- Flashs et secousses restent dans les limites de photosensibilité de [conformité](references/pro/conformite-droits-accessibilite.md).

**Réalisation :**
- Éléments graphiques **dans After Effects** : une composition éditable par élément (texte vivant, pastille liée au texte par `sourceRectAtTime`), rendue en ProRes 4444 alpha depuis la file de rendu d'AE ; recettes dans [After Effects](references/pro/after-effects-motion-design.md).
- Mouvements du cadre dans Premiere : punch-ins, whips et shakes par Mouvement / Transformation avec flou de mouvement.
- Les scripts éprouvés sur Milan pilotent AE et génèrent le XML ; ils ne fabriquent aucune image. Ce sont des exemples à adapter, pas des gabarits à relancer tels quels ([liste](references/projets-cabezer.md)).

### 5.2 Notation obligatoire : hook et rétention sur 10 (consigne du 02/10/2026)

Chaque dégustation est notée avant livraison. **Si une note est sous 8, retravailler puis renoter jusqu'à 8 minimum, et donner les deux notes à Cabezer.** Seule exception : si 8 est impossible sans contredire un choix de Cabezer (son hook, un passage qu'il a gardé, un appel non tourné), son choix prime : livrer avec la note réelle, dire ce qui bloque et proposer au plus deux variantes de hook en gardant le sien comme option. **Au plus deux passes de retravail** (réponse du 12/10/2026) : si la note reste sous 8, livrer avec la note réelle et ce qui bloque. Les notes sont une auto-évaluation de Claude, pas une validation. Barème complet : DA v2 §5.

**Hook (0–3 s) :**

| Critère | Points |
|---|---|
| Produit ou bouchée dans la 1re seconde | 3 |
| Enjeu ou promesse compris en 3 s | 3 |
| Texte d'accroche lisible dès 0,2 s | 1 |
| 2 changements de plan ou de cadre | 2 |
| Son dès la 1re image | 1 |

**Rétention :**

| Critère | Points |
|---|---|
| Au plus 6 blancs de 0,25 s ou plus par minute | 2 |
| Aucune hésitation, correction ni redite restante | 2 |
| Aucun passage de plus de 6 s sans élément visuel nouveau | 2 |
| Produit avant 3 s et 1re bouchée avant la moitié | 2 |
| Récompenses : prix, bouchée, intérieur, verdict, appel au commentaire | 1 |
| Appel au commentaire dans les 5 dernières secondes | 1 |

- **Script :** `Tiktok degustation/Identite-Degustation/noter_hook_retention.py`.
- **Blancs :** méthode étalonnée seulement, sur la voix seule. Une trame est un blanc si elle est 18 dB sous le 80e centile sur 4 s. Repères : ses reels 13 à 18 / min, Milan v02 4,2 / min. Ne pas changer de méthode en cours de route ; ne pas confondre avec `silencedetect`. Le critère « 6 blancs par minute » contrôle le résultat, ce n'est pas une cible de coupe.
- **Relances :** une coupe compte seulement si elle change de rush ou de cadre (un punch-in change le cadre).
- **Clarté :** retranscrire l'export par fenêtres de 10 s qui se chevauchent (Whisper saute des passages sur un long fichier), puis refaire chaque zone douteuse à part.
- **Test du son coupé :** sans le son, les 3 premières secondes doivent se résumer en une phrase.

## 6. Identité visuelle par famille

Chaque famille garde une identité reconnaissable. Une déclinaison 9:16 ou 16:9, quand elle est demandée, ajuste taille des textes, composition et zones sûres sans changer l'identité. Avant l'habillage, retrouver la charte et les montages validés de la famille ; ne pas recréer une direction à chaque vidéo ni transposer celle d'une autre famille. Le style par défaut d'un plugin ne définit pas l'identité.

- **Dégustation :** DA Dégustation v2 (§5.1). Ni Johan Papz, ni Food dégustation v1 (Slak v27), ni les stickers et tampons du Milan v01 ne servent plus de modèle pour la dégustation.
- **Food long :** **créer la charte** (réponse du 12/10/2026) : proposer 30 s habillées (couleurs, polices, titres de lieu, prix, notes, comparatifs) à faire valider ; la fiche validée (`references/identites-visuelles/`) devient la règle. [Food dégustation v1](references/identites-visuelles/food-degustation-v1.md) reste un repère de lisibilité, pas la charte. Animations faites dans AE comme la dégustation : titres de restaurant, cartes de lieu, prix, notes et comparatifs construits en calques AE, avec ses vraies images (façades, menus, tickets) explorées en caméra 3D plutôt que des cartes génériques. Duels et classements : 3 à 5 critères, une preuve à l'image par critère, verdict en dernier.
- **Films/séries :** [PRISME v1](references/identites-visuelles/films-series-prisme-v1.md), validé sur Dune. Réservé à cette famille. Construit dans AE : titres, fiches de personnages et frises en calques natifs, extraits et affiches officiels explorés en caméra 3D. Pas d'affiche ni de visuel généré. Extraits : voir §8 et [documentaire et essai](references/pro/documentaire-essai-video-archives.md).
- **Tech :** [méthode Liquid Glass](references/after-effects/tech-liquid-glass.md) ; rendre le propos accessible à un public food. Le verre, les interfaces et les schémas techniques sont faits dans AE (formes, flous, réfraction par effets natifs), avec les vraies captures d'écran et pages officielles. Pas de maquette d'interface générée ailleurs.
- **Cabezer Story :** voir ci-dessous.
- **Quand Cabezer parle de sa chaîne principale** (toutes familles) : montrer sa chaîne YouTube enregistrée à l'écran, et non son profil TikTok (consigne du 30/09/2026).

**Cabezer Story.** Lire [Raconter avec les images — Micode / Amistory](references/story-montage-micode-amistory.md) avant le découpage visuel ; [registre des références](references/story-references-2026-09-20.md) pour les passages sources ; [documentaire et essai](references/pro/documentaire-essai-video-archives.md) pour la partition et les preuves.
- Relier la vidéo à une question centrale en une phrase ; relier les scènes par « donc » ou « mais ».
- Choisir d'abord la scène, l'objet ou la preuve qui apporte quelque chose à la parole, puis concevoir entrée, évolution, maintien, raccord.
- Alterner images réelles, documents explorés, schémas persistants et retours au visage. Titres réservés aux concepts et articulations.
- **Respirations :** garder les pauses qui portent un regard, une émotion, une attente construite ; couper celles où Cabezer cherche ses mots. Cette règle prime sur la coupe au dernier mot.
- Déplacements explicatifs libres sur documents, cartes, objets ; zooms facecam = zooms avant/arrière façon Micode (§7), seulement quand ils servent le propos.
- Ne jamais écrire le nom de chaîne (« Cabezer Story ») dans les animations, titres ou cartes (consigne du 29/09/2026). Le générique « Amed Story 🧢 » (nom choisi le 30/09/2026) a été **supprimé le 12/10/2026, à refaire en entier** ; seul un nouveau générique validé par Cabezer pourra porter un nom.
- **Refusés :** habillage v08 à grands bandeaux ; identité rose v15 et générique v01 (supprimés le 12/10/2026, à refaire en entier) ; Dossiers v0.2 n'est plus la direction par défaut (inventaire d'assets seulement).
- **Identité Story :** aucune identité visuelle validée. Une nouvelle direction se propose sur un extrait concret (règle ci-dessous) ; ne réutiliser ni la palette rose, ni ses polices, ni le générique v01.
- Toute nouvelle direction se valide sur un extrait concret (vraies images, preuve ou mécanisme, visage, raccords), pas sur une série titre/carte.

**Une image par idée, jamais par mot — méthode validée par Cabezer le 29/09/2026** (démo partie 3 de « Comment les fast-foods ont changé notre génération » ; étude image + transcription + son de 9 passages de Micode, Amistory et Liv). Consigne : « tu devrais utiliser un b-roll pour faire comprendre ce que je veux dire », pas « un b-roll pour chaque mot » ; une succession d'images inutiles « fait perdre la tête aux viewers ».

1. **Avant de choisir une image**, écrire en une ligne ce que le spectateur doit comprendre dans le passage (partition par idée : idée, support, source, durée de lecture).
2. **Un seul support par idée**, tenu sur toutes les phrases de l'idée :
   - **Une preuve réelle** (post, profil, article, étude, page officielle), laissée lisible 3 à 11 s, puis explorée (surlignage, zoom sur la ligne désignée). Désigner au début du mot qui la nomme, une désignation à la fois.
   - **Un univers visuel suivi** : les mêmes personnes au même endroit sur plusieurs plans de 2 à 3 s (minimum 2 s, point 9). Une série de clips d'un même auteur ou tournage, jamais un décor et des personnes différents à chaque phrase.
   - **Un schéma qui se construit** au fil de la parole et revient quand l'idée revient (Micode : 50 s de la même brigade d'icônes). Par exemple, des barres qui changent sur le mot.
   - **Le visage** (5 à 27 s) pour les questions, les avis, la nuance, l'adresse au spectateur et les commentaires sur sa propre démarche.
3. **Énumérations :** si la liste est l'information, un élément par mot dans un même cadre persistant ; si ce sont des exemples d'une situation, montrer la situation en train de se produire ; si Cabezer dit que la liste n'est pas le sujet, rester sur son visage.
4. **Ne pas illustrer littéralement une comparaison ou une métaphore :** « comme un distributeur de tickets » ne devient pas une machine à tickets. Montrer ce que la comparaison veut dire, ou rester sur le visage.
5. **Rappels :** faire revenir un visuel déjà vu quand l'idée revient. Exemples : le souvenir de famille de la partie 2 sur « on n'est plus avec ses parents » ; la cuisine rapide de la partie 1 sur « servir vite ».
6. **Comparaisons :** deux fenêtres dans un même cadre, avec un repère stable.
7. **Titres et cartons :** seulement pour un concept, une date ou un chapitre. Pas de texte qui double chaque nom. Exception : **identifier un intervenant** (nom et fonction) à sa première apparition, une seule fois, ligne faite dans AE à l'identité de la famille, hors visage, durée selon le point 9 (réponse du 12/10/2026) ; jamais en dégustation.
8. **Coupes rapides** (0,4 à 0,8 s) seulement quand la vitesse est le sens : accumulation, « on est envahi de… ». Exception nommée aux durées minimales du point 9.
9. **Temps de lecture (30/09/2026)** — « certaines informations viennent et partent trop vite ». Pour les familles longues (S, F, P, T), toute information écrite (texte, traduction, date, tampon, ligne de liste, bloc de sous-titres) reste entièrement lisible au moins **max(1,5 s ; 1 s + caractères/15)**. Une image sans texte reste au moins 2 s, une preuve au moins 3 s. Ne s'applique pas aux sous-titres mot à mot de dégustation.
   - Entrées et sorties en 8 à 15 images.
   - L'information reste tant que l'idée continue.
   - Si le débit est trop rapide : prolonger, cadre persistant, texte raccourci ou regroupé.
10. **Pas de B-roll qui répète une animation (30/09/2026).** Après un schéma, une liste ou une page qui a fait comprendre l'idée, tenir l'animation ou revenir au visage ; un B-roll ne suit que s'il apporte du nouveau.
11. **Zooms sur B-roll : sobriété (30/09/2026).** Seulement sur le mot qui désigne un détail ; aucune poussée ni dérive décorative.
12. **Chapitres (30/09/2026).** Couper dans le silence après sa phrase, puis montrer le carton **seul ~3 s**, sans voix, avec la signature musicale. Il se déchire quand sa voix reprend. Le titre qu'il prononce (intro, rappel en conclusion) n'est pas un chapitre.

**Famille sans identité validée :** proposer un court extrait représentatif et le faire valider avant de décliner. Ne pas attribuer arbitrairement couleurs ou polices définitives.

**Passages en langue étrangère (30/09/2026, toutes familles) :** chaque surlignage, entourage ou soulignement sur un texte non français affiche, pendant le coup de feutre, la traduction française fidèle et courte du passage marqué, sans le cacher. **On ne traduit pas les dates** (le surlignage reste) et on n'écrit jamais « traduit de l'anglais » ni de mention de langue.

**Ses propres images (30/09/2026) :** puiser dans toute sa chaîne et ses rushs, pas dans 2 vidéos. Aucun plan en double ; aucune source qui domine. Toute vidéo à télécharger demande son accord, avec la taille.

**Fin d'une vidéo Story (30/09/2026, « la fin est trop fin cutter ») :** ne jamais couper juste après le dernier mot.
- Garder son regard silencieux à la caméra quelques secondes, en le vérifiant à l'image dans le rush : fondre au noir **avant** qu'il bouge ou se lève.
- Laisser la musique conclure sur un vrai accord qui s'éteint sur le noir.
- Aucun bruitage sur le fondu, pas de carton d'abonnement.
- Prévoir la place de l'écran de fin YouTube (5 à 20 s de noir et de musique qui s'éteint, sans information utile) (réponse du 12/10/2026).

**Après validation :** une fiche par famille dans `references/identites-visuelles/` : couleurs exactes, polices et graisses, hiérarchie, marges et zones sûres, styles de texte, règles d'animation, MOGRT/presets réellement disponibles, projet modèle, aperçu approuvé, version et preuve de validation. Une refonte devient une nouvelle version.

## 7. Zooms, mouvements et transitions

**Zoom facecam par famille :** façon Micode pour F, S, P (visage de Cabezer seulement, jamais sur les extraits), T. **Exception dégustation :** punch-ins secs alternés (§5.1), pas de zoom progressif.

**Zoom façon Micode — jamais imposé (consigne du 29/09/2026) :** la règle du zoom iPhone Duo est retirée ; ne plus poser le preset `CABEZER - Zoom iPhone Duo - 10 images` par défaut. Quand un zoom sert le moment (tension, révélation, changement d'idée, chute), faire un zoom avant ou arrière : mouvement numérique fluide et progressif (images clés lissées), centré sur le visage, amplitude modérée, puis maintien ; le zoom arrière ramène au cadre de base avant une coupe ou une nouvelle idée. Pas de zoom à chaque plan ni d'aller-retour continu étiré sur toute la prise (rejeté sur Dune). Si un calque fixe (retouche de décor, cache) est aligné sur la facecam, lui appliquer exactement le même zoom.

**Whoosh :** plus obligatoire sur chaque zoom ; un zoom lent façon Micode reste silencieux ou porté par la musique. Un whoosh accompagne un mouvement rapide ou une transition marquée, calé sur le déplacement visuel et dosé sous la voix ; éviter les doublons.

**Transitions :** les transitions **visibles** sont réservées aux changements d'argument ou de séquence ; les transitions marquées (fanions, drapeaux, raccords de mouvement) sont sonorisées par un effet synchronisé. Micro-fondus audio et J/L-cuts sont permis s'ils ne mordent pas une attaque de mot ; jamais de J/L-cut sur la bouchée ou la réaction en dégustation. Catalogue et durées : [fondamentaux](references/pro/fondamentaux-montage-narratif.md).

**Masquer un jump cut, dans l'ordre :** coupe franche assumée ou punch-in sec (D) → plan de coupe qui apporte quelque chose → second angle synchronisé → animation seulement si elle était déjà prévue. Pas de Morph Cut sans demande (§16).

**Speed ramps et raccords dans le mouvement** *(méthode du 28/09/2026, à proposer au premier usage, §20)* :
- Rampes sur les gestes de préparation, arrivée du plat, versement, coupe, uniquement sur les **inserts**, jamais sur la parole ni sur la bouchée retenue (qui reste à vitesse réelle).
- Rampe par Remappage temporel et images clés lissées (6 à 12 images d'étirement) ; ralenti propre seulement avec un rush à cadence élevée (50/60p ou plus) : lire la cadence avec ffprobe avant de promettre un ralenti.
- Raccords de mouvement (whip pan, match cut sur un objet ou une forme) pour relier deux lieux ou deux produits dans un hook agressif. Un raccord de ce type = une transition marquée, sonorisée. Un match cut n'est retenu que si le lien se lit en moins d'une seconde.
- Accéléré d'une préparation et arrêt sur image pour désigner un détail : sur des inserts seulement ([styles food et tech](references/pro/styles-food-et-tech.md)).

**Lissage des images clés :** tout mouvement progressif (échelle, position) en Bézier/Progressif, jamais linéaire. Un punch-in sec est un changement instantané (clé maintenue ou deux clips), pas un mouvement. La vitesse constante reste correcte pour une rotation continue, un défilement, un compteur.

**Mouvement sur image fixe :** il désigne un détail ou présente un visage, avec un temps avant et après, courbe douce ; jamais de dérive décorative ; jamais sur un plan qui porte un texte à lire.

## 8. Recherches, illustrations, droits et références

- **Vérification factuelle :** partir de ce qui est prononcé. Vérifier chiffres, prix, dates, caractéristiques incertains ou susceptibles d'avoir changé ; privilégier la source primaire, contrôler date, territoire, version, unité. Consigner affirmation, passage, lien, date de consultation, résultat (confirmé / nuancé / non confirmé) dans `Suivi/verifications.md`. En cas d'erreur, proposer une correction visible ou une reprise, jamais une recomposition des paroles. Une recherche ne valide pas une dégustation ou un avis.
- **Illustrations :** d'abord les rushs et médias personnels, puis les compléments qui montrent précisément ce qui est évoqué. Conserver auteur, URL, crédits, conditions d'usage, fichier (`Suivi/licences.csv`). Une image illustre, elle ne prouve pas et ne doit pas suggérer une expérience que Cabezer n'a pas vécue. Ne pas couvrir chaque phrase de B-roll. En Story, une image par idée, jamais par mot (§6). Préférer visuels officiels de marque et sources tierces aux habillages génériques. Extraits YouTube crédités à l'écran selon [la méthode du 13/09](references/zooms-broll-et-respirations.md).
- **Extraits tiers (films, séries, vidéos) :** durée minimale nécessaire, commentés ou analysés, source affichée pendant l'extrait. Un crédit n'est pas une autorisation : signaler à Cabezer le risque Content ID avant publication.
- **Personnes, données, partenariats, photosensibilité, typographie** : [conformité](references/pro/conformite-droits-accessibilite.md). **Personnes filmées** (réponse du 12/10/2026) : repérer au dérush les tiers identifiables (clients, employés), les mineurs en priorité, les plaques, écrans et documents personnels, et les lister à Cabezer ; flouter seulement ce qu'il désigne. **Repas offert, invitation, produit reçu ou partenariat** (réponse du 12/10/2026) : le signaler au brief et poser la mention que Cabezer choisit, à chaque fois ; rien n'est ajouté sans sa validation.
- **Inspiration actuelle :** avant l'habillage d'une vidéo courte, étudier des références récentes de la même famille pour le hook, le rythme, les cadrages, la hiérarchie des textes et les relances, jamais pour changer l'identité validée. Consigner liens, dates, passages, métriques visibles. Ne pas affirmer une tendance « virale en ce moment » sans données ; ne pas copier un montage ni récupérer ses sons. Méthode d'analyse : [adaptation et genres](references/pro/adaptation-genres-analyse-de-style.md).

## 9. Sous-titres

**Langue :**

| Lieu de tournage | Dégustation | Autres familles |
|---|---|---|
| France, Belgique francophone | Français mot à mot, incrustés | SRT français seulement, rien d'incrusté (réponse du 12/10/2026) |
| Étranger | Langue locale ou anglais, **à demander à chaque vidéo** (défaut : anglais ; Milan : anglais) | Anglais incrusté, toujours (consigne du 28/09/2026, Maritozzo) |
| Passages non français dans une vidéo française | Idem (§6) | Traduction française sur les passages surlignés (§6) |

**Réalisation commune :**
- La piste de légendes Premiere sert de transcription, de calage et d'export SRT. Les sous-titres incrustés finaux sont une **composition After Effects** à l'identité de la famille, entrée animée, texte resté éditable (un calque de texte, un mot ou un paquet par clé de Texte source), rendue en ProRes 4444 alpha. Livrer la composition, le rendu et le SRT. Plus de légendes Premiere au style générique (retour sur Maritozzo v09, 28/09/2026).
- **Jamais affichés pendant qu'un mot ou une phrase est animé à l'écran** (titre, tampon, prix, note, repère, pop-up, appel au commentaire) : couper ou raccourcir le bloc pour laisser l'animation seule, puis reprendre.
- Les paquets sont répartis seulement sur le temps conservé au dérush ; la traduction est réécrite sans les phrases coupées.
- **Un rendu par passage validé** (réponse du 12/10/2026) : une composition AE et un rendu ProRes 4444 par séquence (passage) validée, calés sur ses coupes. Si Cabezer retouche une coupe, refaire seulement le rendu du passage touché, puis vérifier la synchro dans l'export.
- Typographie française (espaces insécables, guillemets, nombres, prix, heures) : [conformité](references/pro/conformite-droits-accessibilite.md).

**Dégustation — consigne du 02/10/2026 :**
- **Style DA v2 :** Avenir Next Heavy en capitales, blanc, ombre courte et nette, sans contour épais ; vers 72–75 % de la hauteur, exemptés de la boîte de zones sûres (réponse du 12/10/2026) ; contrôler sur une capture de chaque application qu'ils ne sont pas masqués et signaler tout conflit ; mots clés (produit, prix, note, lieu) dans la couleur d'accent.
- **Découpage :** en français, un mot à la fois ; en traduction, paquets de 1 à 3 mots, 18 caractères au plus, les petits mots collés au mot qui suit.
- **Entrée :** pop en 4 images ; sortie sèche au paquet suivant.
- Un paquet qui tombe sous un pop-up, un prix, la note ou l'appel au commentaire attend la fin de l'animation, sinon il est retiré.

**Autres familles (y compris tournées à l'étranger) — la dégustation reste régie par le bloc ci-dessus :**
- **Deux lignes maximum réellement affichées**, pour chaque bloc. Coupures de ligne explicites, jamais de retour automatique (Premiere ajoutait une 3ᵉ ligne) : ≤ 24 caractères par ligne en 9:16 à ~70 px sur 1080 ; en 16:9, viser ≤ 42 caractères par ligne. Blocs trop longs découpés en sous-titres successifs équilibrés, par groupes de sens, sans mot isolé ; ne pas réduire la police ponctuellement.
- Traduire le sens oral de Cabezer (ton naturel, pas mot à mot), y compris les échanges avec les vendeurs ; garder les noms propres et le mot exact de l'appel au commentaire. Corriger noms, chiffres et ponctuation.
- **Style :** identité de la famille, entrée animée au moins (pop léger + mots révélés un à un, sortie courte). Respecter taille, marges et zones sûres de l'identité ; éviter l'interface mobile et le visage.
- Un SRT correct ou une mesure hors Premiere ne suffit pas : vérifier dans Premiere puis dans le MP4 exporté après tout import, changement de style ou déclinaison. Ne pas annoncer les sous-titres contrôlés tant qu'un bloc sur trois lignes existe.

## 10. Colorimétrie

Passe distincte et obligatoire. Consigner version, réglages, contrôle, limites. Lire [étalonnage](references/pro/etalonnage-gestion-couleur.md).

**Avant tout :** activer la gestion des couleurs de l'affichage et vérifier la configuration couleur de la séquence ; contrôler en gamma 2.4 (un export qui paraît plus clair dans QuickTime n'est pas un fichier défectueux).

**Chaîne technique selon la caméra** — confirmer le profil réel du rush (ffprobe et métadonnées) ; **une seule conversion par plan**, jamais conversion automatique + LUT technique cumulées :
- **DJI Osmo Pocket 3, D-Log M :** exposition/blancs → conversion DJI D-Log M → Rec.709 **une seule fois** → **Exterior Cinema** ou **Exterior Doux**, dosé sur les plans réels. Fichiers : [chaîne Pocket 3 et LUT Cabezer](references/dji-osmo-pocket-3-luts.md), `assets/luts/dji-osmo-pocket-3/`.
- **Panasonic V-Log/V-Gamut :** conversion Panasonic → Rec.709, **jamais la LUT DJI**.
- **iPhone HLG/HDR ou Apple Log :** convertir vers Rec.709 SDR (gestion des couleurs de Premiere ou LUT Apple Log officielle, pas les deux) avant les corrections ; jamais de LUT D-Log M dessus.
- **Source déjà Rec.709 :** pas de conversion technique.

**Ordre :** réglage d'exposition et de blancs d'entrée si la chaîne caméra le prévoit (Pocket 3) → conversion unique → exposition → contraste → balance → harmonisation entre plans → look → secondaires. Lecture exacte de l'ordre Pocket 3 **[Q]** (défaut : diagnostic de l'exposition, conversion unique, puis exposition et blancs dans Lumetri avant la LUT Exterior). Lire les scopes à l'arrêt : forme d'onde pour la luminance, parade pour la balance, vectorscope pour la saturation et la peau.

**Correction primaire :** exposition, balance des blancs, contraste, carnation ; comparer avant/après sur plusieurs prises et harmoniser ; viser la constance de la peau entre plans. Traiter à part captures d'écran, graphiques et extraits de films (pas de look facecam dessus). Ne jamais étalonner les graphismes AE : pas de calque de réglage global au-dessus de l'habillage.

**Correction secondaire food** *(méthode du 28/09/2026, à proposer au premier usage, §20)* :
- Après la primaire, isoler par TSL (Lumetri > Courbes teinte/saturation ou TSL secondaire) les couleurs clés du produit — rouge de sauce, jaune de fromage, vert d'herbes, brun de croûte — et les renforcer légèrement sans toucher la carnation.
- Contrôler la carnation sur la ligne de chair du vectorscope ; l'appétence finale se juge par Cabezer sur son écran : le produit doit donner envie sans paraître artificiel.
- Lumières mixtes de restaurant (néon + fenêtre) : corriger la dominante principale en primaire, puis masquer/suivre la zone gênante si elle touche le produit.
- Harmoniser les inserts B-roll avec la facecam de la même scène.

**Contrôle du MP4 :** balises bt709 et plage tv (ffprobe), YMIN/YMAX/SATMAX (signalstats) ; jugement visuel final sur téléphone par Cabezer.

## 11. Audio : SFX, musique, ambiances, mixage

Lire [audio pro](references/pro/audio-dialogue-sound-design-mixage.md).

**Organisation des pistes :** A1–A2 voix, A3–A4 SFX, A5 musique ; ajouter une piste ambiances si utilisée.

**SFX.** Dégustation : banque Pixabay et liste de référence (§5). Autres familles : **bibliothèque ouverte**, choisie selon le sujet et l'animation. Clics, caisses, whooshes et accents doivent être **clairement audibles** dans le mix final sous une voix intelligible, sans être envahissants ; un son inaudible ne remplit pas sa fonction. Ne pas multiplier les accents ni recouvrir bouchées et réactions. Aucun bruitage sans élément visuel correspondant à l'écran. Refuser les SFX synthétisés ou génériques peu pertinents : sources = fichiers de Cabezer, ses bibliothèques **Cabezer-Sons-Vol1** et **Cabezer-Ajouts-Food-Lifestyle** (WAV 24 bits/48 kHz), Adobe Stock via son compte (licence payante : à signaler), ou toute source dont la licence couvre l'usage. Ne jamais prélever les sons d'une vidéo TikTok ou d'un tutoriel. Consigner provenance, licence, crédits, fichier ; ne pas inventer une licence. Bruitages Story retenus (30/09/2026) : tampon, impression de ticket, coche au feutre, vraie déchirure de papier (CC0).

| SFX de base | Fichier |
|---|---|
| Caisse | [modestas123123-cash-register-kaching-sound-effect-125042.mp3](assets/sfx-cabezer/modestas123123-cash-register-kaching-sound-effect-125042.mp3) |
| Riser | [u_1pruylktlg-riser-7-130957.mp3](assets/sfx-cabezer/u_1pruylktlg-riser-7-130957.mp3) |
| Whoosh | [soundreality-whoosh-end-384629.mp3](assets/sfx-cabezer/soundreality-whoosh-end-384629.mp3) |
| Clic de souris | [matthewvakaliuk73627-mouse-click-290204.mp3](assets/sfx-cabezer/matthewvakaliuk73627-mouse-click-290204.mp3) |

Provenance et empreintes : [manifeste](assets/sfx-cabezer/manifest.json) (pas une preuve de licence). Copier les sons utilisés dans les médias du projet.

**Ambiances et sound design de fond** *(méthode du 28/09/2026, à proposer au premier usage, §20)* :
- Sous les inserts muets et aux changements de lieu, une ambiance discrète (salle de restaurant, rue, cuisine) peut lier les plans, prise de préférence dans les rushs du lieu, sinon d'une banque licenciée. Poser l'ambiance d'un lieu avant son premier plan.
- Toujours sous la voix, jamais au détriment des bouchées ; ce n'est pas une musique de fond. En dégustation : voir §5.
- Fondus d'entrée/sortie aux changements de séquence ; ne pas laisser une ambiance couper net sur une coupe.

**Musique (hors dégustation) :** choisir, maintenir, changer ou retirer selon l'émotion réelle (question, découverte, doute, verdict, moment drôle), pas à chaque changement de produit. Changements aux articulations naturelles, avec fondus ou silences maîtrisés ; fondu exponentiel en fin de morceau. Ne pas déplacer une réaction pour suivre la musique. Un morceau fini garde sa vitesse d'origine. Ducking : valeurs de départ de la fiche audio, retouchées à la main.
- Films/séries : `/Users/cabezer225/Downloads/MUSIQUES` et `/Users/cabezer225/Documents/ChatGPT/Film/musique`, après écoute réelle des extraits par Cabezer ou sur sa validation.
- Compositions originales : [bibliothèque originale Cabezer](references/musiques-originales-cabezer.md) (Cédric Grolet notamment) ; ne pas confondre avec les achats Halal Beats. Ne pas garantir l'absence de revendications.
- Distinguer sélection proposée, employée, approuvée. Présence locale ≠ licence.

**Musique Story (consignes du 29/09 et du 30/09/2026) :**
- **Nappe basse presque continue** sous toute la narration, visage compris, **environ 24 dB sous la voix** (consigne du 30/09 bis, qui remplace les 15 dB du 29/09), mesurée en LUFS court terme sur les passages parlés ; réglage final à l'écoute de Cabezer. Elle change de texture selon la partie : groove léger pour une scène de vie, motif analytique pour les chiffres.
- **Plus basse ou absente** sous une interview ou une source qui parle.
- **Vrai silence de 1 à 2 s** juste avant une bascule (nouvelle partie, rebondissement, idée reçue cassée), ou sous la chute ; puis carton de chapitre avec sa signature (§6 point 12).
- **Montée ou impact** juste avant un concept clé ou une preuve.
- Cette règle remplace l'ancienne consigne « silence pendant les explications face caméra ».
- **Sources :** musiques et bruitages libres de droits possibles en plus des nasheeds et bibliothèques locales (téléchargement après accord, licence consignée). Inspiration : Micode (nappes et pulsations électroniques, tension), Amistory (rythmes légers et documentaires).
- **Composition originale (30/09/2026 :** « compose réellement 2 ou 3 musiques avec une ambiance pour la vidéo en général et 2-3 ambiances max par émotion ») : méthode par défaut en **Story, food long et tech** (réponse du 12/10/2026) ; films/séries : bibliothèque perso.
  - Composer **2 ou 3 thèmes par vidéo**, chacun avec mélodie, harmonie, basse, rythme et forme (intro, thème, développement, reprise, fin) : par exemple un thème principal chaleureux qui revient en conclusion, un thème « explication », un thème « tension/écran ».
  - Au plus **2 à 3 ambiances par émotion**, déclinées de ces thèmes (orchestration, densité). Les changements se font aux articulations (chapitres, silences, montées). La musique est calée sur le montage : temps forts sur les coupes, impacts sur les titres et les chapitres.
  - Jouer les notes avec de **vrais instruments échantillonnés** d'Apple installés (pianos, guitares, Drum Kit Designer de `/Library/Application Support/Logic/EXS Factory Samples/` ; cordes, cuivres, bois, contrebasse de `/Library/Application Support/GarageBand/Instrument Library/Sampler/Sampler Files/`). Jamais de synthèse note à note (numpy). Humaniser et ajouter de la réverbération. Les Apple Loops (`/Library/Audio/Apple Loops/Apple`) peuvent servir de matériau dans une composition, jamais seules ni en collage zone par zone (méthode abandonnée le 30/09, voir historique). Usage selon la licence du logiciel Apple installé : consigner version et clause. La bibliothèque complète de GarageBand (25 Go) n'est téléchargée qu'avec son accord.
  - Fournir les thèmes seuls pour l'écoute, et des stems par thème.
  - La musique **conclut vraiment** à la fin de la vidéo (cadence, résonance) : jamais de fin coupée sèche.
  - Premier exemple : [projets Cabezer](references/projets-cabezer.md).

**Mixage — passe distincte et obligatoire :**
- **Traitement voix uniforme** sur toute la séquence : mêmes réglages fixes sur tous les clips (réduction de bruit, EQ de présence, compression douce) + un limiteur unique sur la piste. Seule exception : une prise très bruyante reçoit un peu plus de réduction de bruit, signalée dans le suivi (réponse du 12/10/2026). Valeurs de départ dans la fiche audio (passe-haut vers 70–90 Hz, compression douce, gain réglé avant les effets). Interdits : « Correspondance automatique », le curseur « Dynamique » d'Essential Sound et « Améliorer la parole » (Enhance Speech, que le skill appelait « Améliorer le dialogue » ; libellé à confirmer) qui change le timbre. L'effet manuel Dynamique (Amplitude et compression) reste permis.
- Régulariser la voix entre prises au gain de clip après mesure, puis doser SFX, ambiances et musique dessous ; soigner fondus et crêtes ; jamais d'écrêtage.
- Contrôler les raccords en contexte ; mesurer le MP4 (ebur128, crête vraie, repliement mono) ; demander à Cabezer l'écoute à volume normal, sur petit haut-parleur et en mono. Les valeurs de tutoriels et les mesures complètent l'écoute sans la remplacer : ne jamais déclarer le mix validé sans sa validation auditive.

Une demande de terminer musique, SFX, mixage et couleur supprime seulement les validations intermédiaires : les passes restent distinctes et consignées séparément.

## 12. Déclinaisons et tournages multi-caméras

**Du format long aux Shorts** *(méthode du 28/09/2026, à proposer au premier usage, §20)* — pour Story et food long :
1. Repérer les passages **autonomes** : une idée complète, compréhensible sans le reste, avec une chute ou un verdict.
2. Écrire un nouveau hook à partir des paroles existantes (réordonner des prises, jamais recomposer une phrase pour changer son sens).
3. Recadrer 16:9 → 9:16 depuis les rushs 4K : Auto Reframe comme point de départ, puis correction manuelle des images clés pour garder visage, produit ou document lisibles. Refaire les textes à l'échelle verticale selon l'identité de la famille.
4. Appliquer les règles du format court de la famille : dégustation (§5, §9) ; pour S et F, sous-titres de la famille adaptés au 9:16 (2 lignes, ≤ 24 caractères) **[Q]** (défaut : oui).
5. Fin qui renvoie à la vidéo longue ou qui boucle sur le début.
6. Une séquence par Short dans le même projet, nommée d'après le passage.

**Déclinaison du même montage court** (TikTok → Shorts/Reels) : conserver coupes et durée validées ; adapter seulement les zones sûres si besoin.

**Multicam** *(méthode du 28/09/2026, à proposer au premier usage, §20)* :
- Synchroniser par forme d'onde audio (Créer une séquence source multicaméra > Audio), contrôler la synchro sur un clap ou un son net ; passer les sources mono en double mono avant la création.
- Harmoniser les boîtiers (Pocket 3, iPhone, Panasonic) en couleur avant le montage multicam : chaîne technique propre à chaque caméra (§10), puis correspondance sur la caméra principale.
- Choisir le meilleur son comme piste principale ; ne pas mélanger les micros des deux caméras sur la voix. Son externe en double système : [Premiere avancé](references/pro/premiere-pro-avance.md).

## 13. Export et cibles de plateforme

Exporter en MP4 H.264 (ou H.265 si demandé) au ratio, à la résolution et à la cadence de la destination. Nommer `<Sujet>_<plateforme>_v<NN>.mp4` (`social` pour un export commun TikTok/Reels/Shorts). Désactiver les proxys avant l'export. Détails et commandes : [organisation, livraison et QC](references/pro/organisation-livraison-qc.md).

| Destination | Format de base | Repères à vérifier |
|---|---|---|
| TikTok / Reels / Shorts | **FHD 1080×1920 exporté directement de Premiere** (consigne du 02/10/2026) : taille d'image personnalisée 1080 × 1920, « Utiliser la qualité de rendu maximale » coché (utile pour la réduction 4K → 1080), « Rendu à la profondeur maximale » selon les effets (libellés à confirmer ; le skill écrivait « Rendu à la résolution maximale »), H.264 VBR 1 passage environ 20 Mbit/s, AAC 320 ; cadence de la séquence ; master 4K seulement sur demande | Zones sûres : textes hors du bas (légende, boutons) et du bord droit ; texte clé dans le tiers central et dans la boîte de test de [formats courts](references/pro/formats-courts-verticaux.md) ; contrôle sur capture réelle des applications |
| YouTube long | **3840×2160 quand les rushs sont en 4K** (YouTube encode mieux un fichier 4K) (réponse du 12/10/2026), sinon 1920×1080 ; cadence de la séquence ; H.264 VBR 2 passages, débit de départ dans la fiche (repères YouTube à vérifier), AAC 48 kHz 320 kbit/s | Chapitres ; 5 à 20 s de fin compatibles avec l'écran de fin |

**Loudness :** les plateformes normalisent le volume ; YouTube est généralement cité autour de −14 LUFS intégrés. C'est un **repère de contrôle (±1), pas une cible imposée** : le mix se valide à l'écoute de Cabezer, puis se mesure sur le MP4 exporté. **Crête vraie du MP4 ≤ −1 dBTP** (l'encodage AAC relève les crêtes) ; si elle dépasse, baisser d'abord la source fautive. Consigner les mesures réelles.

**Contrôle du fichier :** ffprobe (taille, codec, cadence constante, balises bt709, audio 48 kHz, durée, débit). Enregistrer le `.prproj` (et le `.aep` si AE a servi) avant chaque export.

## 14. Contrôles avant livraison

**Liste de contrôle — relire chaque état séparément :**
- Dérush/raccords : aucun mot coupé (lister les coupes, retranscrire 1 s autour des coupes suspectes), aucun blanc résiduel non voulu, « Bref, c'est partiiii » entier, appel au commentaire présent et entier.
- Cadrage, zones sûres (boîte de test), illustrations (sources et crédits dans `licences.csv`).
- Habillage ; sous-titres : langue selon §9, jamais trois lignes, masqués pendant les textes animés, typographie française.
- **Dégustation :** notes hook et rétention ≥ 8, ou note réelle expliquée si un choix de Cabezer l'empêche (§5.2) ; aucun reste de phrase coupée ni plan muet qui traîne ; pas de SFX orphelin d'un élément retiré ; pas d'audio d'insert résiduel.
- Musique / SFX / ambiances : présents, dosés, whooshes synchronisés (mesure) ; écoute demandée à Cabezer.
- **Colorimétrie** faite et comparée ; balises du MP4.
- **Mixage** fait et mesuré (ebur128, crête vraie, mono) ; validation auditive de Cabezer : faite ou « en attente ».
- **Conformité :** tiers identifiables traités selon sa décision, mention de partenariat si besoin, flashs et secousses dans les limites, extraits tiers crédités.
- Début/fin, durée (≤ 3:00 en TikTok dégustation), pas de noirs ni d'images figées involontaires, pas de médias hors ligne.
- AE : compositions liées/rendues, alpha correct (yuva444p12le, pas de frange), pas d'audio guide en doublon, `.aep` et sources conservés.

**Pièges vérifiés (Milan, 02/10/2026) :**
- **Ordre des clips :** dans un FCP XML, écrire les clips de chaque piste dans l'ordre chronologique. Un clip écrit après un clip plus tardif s'importe, mais manque à l'export.
- **Média sans son :** un média déclaré avec son mais qui n'en a pas (stock passé en `-an`) s'importe hors ligne. Lui ajouter une piste muette.
- **Stock :** conformer à la cadence et au cadre de la séquence avant import (Milan : 29,97 i/s, 2160 × 3840).
- **Import :** ouvrir le XML sans projet ouvert, sinon il s'importe dans le projet ouvert.
- **Retouches de Cabezer :** enregistrer ses retouches sous une nouvelle version avant d'exporter, comparer les listes de coupes avant d'écraser quoi que ce soit, puis vérifier que les pistes d'un seul tenant (sous-titres) suivent ses coupes.

**Contrôles automatisables** *(méthode du 28/09/2026)* : pré-contrôle de séquence (hors ligne, clips désactivés, trous, pistes d'inserts muettes) par script, puis analyse du MP4 (blackdetect, freezedetect, silencedetect, ebur128, signalstats) avec les commandes et seuils de [la bibliothèque unique](references/pro/organisation-livraison-qc.md). Ces contrôles signalent des cas à revoir ; ils ne remplacent ni le visionnage ni l'écoute.

## 15. Boucle rétention → montage

*(Méthode du 28/09/2026, à proposer au premier usage, §20.)* Après publication, quand les données existent (YouTube Studio, vidIQ, statistiques TikTok) :
1. Récupérer la courbe de rétention et les moments de décrochage marqués.
2. Les relier à la timeline du montage publié : hook, entrée du produit, bouchée, relances, transitions, fin.
3. Consigner dans le suivi du projet : moment, ce qui se passe à l'écran, hypothèse.
4. Quand une même observation revient sur **plusieurs vidéos de la même famille**, la proposer à Cabezer comme nouvelle règle de ce skill. Une vidéo isolée ne suffit pas.

Ne jamais présenter une hypothèse comme une cause prouvée ; la rétention dépend aussi du sujet, de la miniature et de la diffusion. Ne jamais supprimer un passage seulement parce que la courbe baisse : mieux le raconter. Méthode : [rétention YouTube](references/pro/retention-youtube-long.md).

## 16. After Effects et outils IA

- **Toutes les animations graphiques se font dans After Effects (30/09/2026), quelle que soit la famille** (définition §1). Elles sont construites en calques AE natifs et modifiables : animateurs de texte, effets et préréglages d'AE, Trim Paths, caches par approche, caméra 3D et profondeur de champ ; courbes d'accélération travaillées ; une composition par scène, nommée, que Cabezer peut ouvrir et retoucher ; taille et cadence de chaque composition = celles de la séquence de destination.

  **Plus de « génération » comme avant :** pas de gabarit générique assemblé par script (cartes arrondies sur voile flouté, flèches, nœuds, même pop partout), jugé « comme tous les utilisateurs de Claude » ; pas d'image ni de graphisme fabriqué hors d'AE (Python, HTML, IA) ; pas d'animation générée par IA. Seules les vraies sources sont importées : rushs, photos, captures de pages, emojis Apple rendus par macOS. Un script peut piloter AE, mais le résultat doit être un vrai projet AE travaillé. Méthode et recettes : [After Effects](references/pro/after-effects-motion-design.md).
- **Premiere ↔ AE :** lire [le flux et les techniques](references/after-effects/premiere-after-effects.md) avant l'habillage : Dynamic Link (Premiere, AE et Media Encoder à la même version) ou rendu intermédiaire, alpha, contrôleurs, versions, conservation des projets modifiables. Titres, cartes, prix, tracés, masques, suivis, détourages, interfaces dans AE ; calage final dans Premiere. [Registre des sept tutoriels AE](references/after-effects/tutoriels-2026-09-16.md).
- **Outils IA — trois statuts :**

| Statut | Outils |
|---|---|
| Autorisés comme aides, résultat vérifié | Transcription, montage par le texte (repérage et pré-découpe), détection des scènes, Auto Reframe (point de départ), recherche dans les médias, Roto Brush et suivi sur un vrai plan, traduction automatique de légendes relue |
| Seulement sur demande explicite de Cabezer | Morph Cut, flux optique sur un plan clé, Remplissage d'après le contenu, Generative Extend et tout outil de génération ou de reconstruction de pixels ; voix ou musique produites par un modèle génératif (la composition jouée avec les instruments échantillonnés d'Apple, §11, reste la méthode Story) |
| Interdits (règles de Cabezer) | « Améliorer la parole », Correspondance automatique et curseur « Dynamique » d'Essential Sound ; images ou animations générées par IA ; musique synthétisée note à note |

- **Tesseract et Higgsfield/Higgsedit :** retirés du skill (réponse du 12/10/2026) ; ne plus les proposer.
- Techniques Premiere utiles : imbriquer un élément réinitialise recadrage et point d'ancrage avant un effet ; modes de fusion (écran, incrustation) pour les textures. Plus dans [Premiere avancé](references/pro/premiere-pro-avance.md).

## 17. Plugins

Consulter [l'inventaire et l'état vérifié](references/plugins-installes.md). Utiliser un plugin quand il apporte un gain réel, sans multiplier les effets. Consigne d'installation : **gratuits uniquement pour le moment** (§1). Téléchargé, installé, en essai et fonctionnel dans Premiere sont des états distincts ; tester sur une copie avant usage réel. Un preset ou plugin n'autorise pas automatiquement l'usage de son audio intégré. Tout effet vu dans une référence se reconstruit avec des effets natifs avant d'envisager un pack.

## 18. Apprendre de nouvelles références

Cabezer veut des méthodes réellement étudiées, pas des liens. Lire le contenu ou la transcription d'un tutoriel avant d'en tirer des règles ; indiquer la couverture réelle (transcription lue, images examinées, visionnage non attesté) et les dépendances de version ou de plugin. Les valeurs et promesses d'un tutoriel ne deviennent pas des règles universelles. Consigner dans une fiche `references/` et ajouter ici seulement la règle retenue, après accord de Cabezer.

## 19. Fiches pro — méthodes des meilleurs monteurs

Étudiées en octobre 2026 (transcriptions de tutoriels, conférences et formations, documentation, ouvrages de référence) et harmonisées avec ce skill ([décisions d'harmonisation](references/decisions-harmonisation.md), auxquelles les fiches renvoient par lettre et numéro). Elles complètent les règles de Cabezer sans jamais les remplacer. Chaque fiche indique la couverture réelle de ses sources et marque « à vérifier » ce qui n'a pas pu être confirmé. Scripts de contrôle en lecture seule (à tester sur sa machine avant usage) : `references/pro/scripts/` — `controle-mp4.sh`, `mesure-plans.py`, `xml-coupes.py`, `lint-srt.py`, `lint-fr.py`, `flash-check.py`, `contraste-zone.py`, `lister-clips.jsx`, `envcheck-mac.sh`, `reprise-candidats.py`.

**Principes de monteur professionnel, toujours :**
- Chaque coupe, plan de coupe ou B-roll a une raison qu'on peut dire (émotion, information, changement de point de vue) ; sinon rester sur le visage.
- L'émotion d'abord : on sacrifie la continuité, puis le regard, puis le rythme, jamais l'émotion ni l'histoire (règle des six de Walter Murch).
- Mesurer pour décrire, jamais pour viser : durée des plans, coupes par minute, blancs se comparent aux meilleures vidéos de la même famille de Cabezer, pas à une norme de tutoriel.
- Promesse tenue tôt, boucles ouvertes marquées et toutes refermées, aucune information utile dans la zone de l'écran de fin.
- Tenir un plan plus longtemps que confortable seulement pour un regard, une attente, une émotion ; laisser retomber après un sommet.
- En AE : un seul élément principal bouge à la fois ; entrée plus rapide que le maintien, sortie plus courte que l'entrée ; jamais sur la bouchée, le produit ou le visage.
- Regard neuf : revoir le montage sans le son, puis le lendemain ou après une autre tâche, avant de le livrer.
- Emprunter à une référence sa grammaire (durées, ordre, forme de l'accroche, place du son), jamais son identité, ses plans ni ses sons.

| Fiche | La lire quand |
|---|---|
| [Fondamentaux du montage narratif](references/pro/fondamentaux-montage-narratif.md) | Dérush, choix des prises, raccords, J/L-cuts, rythme, comédie, transitions ; toute coupe difficile |
| [Rétention YouTube long](references/pro/retention-youtube-long.md) | Ouverture, promesse, boucles, relances, chapitres, fin d'une vidéo longue ; lecture d'une courbe |
| [Formats courts verticaux](references/pro/formats-courts-verticaux.md) | Hook, structure, sous-titres animés, zones sûres, recadrage 9:16, export social |
| [Premiere Pro avancé](references/pro/premiere-pro-avance.md) | Organisation, proxys, trims, montage par le texte, multicam, double système, cadences, plans défaillants, Dynamic Link, XML, scripting |
| [After Effects et motion design](references/pro/after-effects-motion-design.md) | Tout habillage : courbes, animateurs de texte, expressions, caméra 3D, parallaxe, suivi, rendu ProRes 4444, pilotage d'AE par script |
| [Audio pro](references/pro/audio-dialogue-sound-design-mixage.md) | Dialogue, room tone, chaîne voix, ducking, nappe Story, SFX, mesures de loudness |
| [Étalonnage et gestion des couleurs](references/pro/etalonnage-gestion-couleur.md) | Toute passe couleur : chaîne par caméra, scopes, peau, food, HDR/HLG, balises d'export |
| [Documentaire, essai vidéo, archives](references/pro/documentaire-essai-video-archives.md) | Story et films/séries : partition, preuves, photos, cartes, extraits, cartons |
| [Styles food et tech](references/pro/styles-food-et-tech.md) | B-roll food, rampes, duels et classements, captures d'écran et interfaces tech |
| [Adaptation et genres](references/pro/adaptation-genres-analyse-de-style.md) | Montage hors familles, analyse d'une référence, pub, clip, vlog, interview, comédie, bande-annonce |
| [Organisation, livraison et QC](references/pro/organisation-livraison-qc.md) | Arborescence, sauvegardes, retours, bibliothèque ffmpeg et scripts de contrôle, specs d'export |
| [Pilotage, environnement et reprise](references/pro/pilotage-environnement-reprise.md) | Première session sur une machine, exécution de scripts, pilotage de l'interface, plantage, reprise par une nouvelle session |
| [Conformité, droits et accessibilité](references/pro/conformite-droits-accessibilite.md) | Personnes filmées, partenariats, extraits tiers, photosensibilité, typographie française à l'écran |

## 20. Statut des méthodes et décisions en attente

Une méthode « à proposer au premier usage » est présentée à Cabezer avant d'être appliquée ; après validation, noter ici la date et le montage, et retirer la mention.

| Méthode | Depuis | Statut |
|---|---|---|
| Speed ramps et raccords de mouvement (§7) | 28/09/2026 | À proposer au premier usage |
| Correction secondaire food (§10) | 28/09/2026 | À proposer au premier usage |
| Ambiances (§11) | 28/09/2026 | À proposer au premier usage, dégustation comprise (réponse du 12/10/2026) |
| Long → Shorts (§12) | 28/09/2026 | À proposer au premier usage |
| Multicam (§12) | 28/09/2026 | À proposer au premier usage |
| Contrôles automatisables (§14) | 28/09/2026 | Appliqués comme signaux ; outils à tester sur sa machine |
| Boucle rétention (§15) | 28/09/2026 | À proposer au premier usage |
| Identité Story v15 rose et générique « Amed Story 🧢 » v01 (§6) | 30/09/2026 | **Supprimés le 12/10/2026, à refaire en entier** |
| Charte food long (§6) | 12/10/2026 | À créer sur un extrait de 30 s à valider |

**Réponses de Cabezer du 12/10/2026 :** appliquées dans ce texte (mention « réponse du 12/10/2026 ») ; elles priment sur les sections « Décisions à demander » des fiches. Tableau récapitulatif en tête du registre ci-dessous.

**Décisions en attente :** chaque **[Q]** donne son défaut dans le texte ou dans le registre. Registre complet, dédupliqué et classé par thème (les questions prioritaires marquées ★) : [décisions en attente](references/decisions-en-attente.md). Poser une question seulement quand elle bloque, une fois, avec le défaut proposé ; une réponse de Cabezer devient une règle datée de ce skill.
