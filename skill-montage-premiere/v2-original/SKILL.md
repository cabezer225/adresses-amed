---
name: "cabezer-premiere-shorts"
description: "Monter les vidéos de Cabezer (YouTube long, Shorts, TikTok, Reels) avec Premiere Pro et After Effects (animations uniquement dans After Effects ; Tesseract et Higgsfield/Higgsedit seulement sur demande explicite). Appliquer ses règles de dérush, identité par famille, audio, couleur, sous-titres, déclinaisons, export et contrôle. Pas pour la génération vidéo, les miniatures ou la publication seules."
---

# Montage Cabezer — Premiere Pro, After Effects et méthodes complémentaires

Ce fichier contient les **règles actuelles**. Les consignes datées qui se remplaçaient entre elles ont été fusionnées ; leur chronologie est résumée à la fin (« Historique des consignes »). En cas de doute, la version la plus récente l'emporte.

## 1. Priorités et portée

**Ordre de priorité :** brief actuel de Cabezer → règles de ce skill (dont les exceptions par famille) → fiches de référence → méthodes complémentaires des plugins → valeurs des tutoriels.

- S'applique à tous les montages Cabezer, dans tous les dossiers et formats. Le nom historique « shorts » ne limite pas la portée. Ne pas imposer le vertical à une vidéo longue.
- **Premiere Pro = timeline maîtresse.** Tesseract uniquement pour une animation ou transition demandée. Higgsedit comme moteur de montage seulement sur demande explicite, avec les mêmes règles éditoriales.
- **Animations : uniquement dans After Effects, pour tous les projets et toutes les familles (consigne du 30/09/2026 : « les animations se font uniquement par AE et non par génération comme avant »).** Allers-retours avec Premiere sans redemander la permission. Détail en §16.
- Identifier d'abord la **famille éditoriale** : dégustation, food long, Cabezer Story (société/documentaire), films/séries (PRISME), tech. Chaque famille a son identité et ses exceptions (tableau §2).
- Avant de modifier un montage existant : **Enregistrer sous** une nouvelle version du projet. Tester d'abord sur une copie et un aperçu court quand Cabezer demande un essai sur un projet ouvert.
- **Validations :** faire valider le dérush avant l'habillage, sauf autorisation explicite d'enchaîner (« fais ça de manière autonome », « export final direct »). Une autorisation d'enchaîner n'autorise jamais la publication.
- Distinguer toujours **appliqué / contrôlé / validé par Cabezer**. Un import n'est pas un montage ; un export lancé n'est pas un export validé ; une mesure n'est pas une écoute ; une méthode écrite n'est pas un preset créé.

## 2. Règles actuelles par famille — vue rapide

| Règle | Dégustation (TikTok/Shorts/Reels) | Food long | Story | Films/séries | Tech |
|---|---|---|---|---|---|
| Sous-titres | **Français** mot à mot en France et Belgique ; à l'étranger **langue locale ou anglais, à lui demander à chaque fois** (masqués pendant les textes animés) | Selon brief, 2 lignes max ; anglais si étranger | 2 lignes max ; anglais si étranger | 2 lignes max ; anglais si étranger | 2 lignes max, vocabulaire accessible ; anglais si étranger |
| Musique de fond | **Absente par défaut** | Selon émotion | Selon émotion | Bibliothèque perso | Selon émotion |
| SFX | Banque Pixabay tendance TikTok + touche mème, sans mèmes vocaux ni boom, audibles | Bibliothèque ouverte, audibles | Idem, pas de bruitage d'objet gratuit | Idem | Idem |
| Zoom facecam | Punch-ins secs 100/115 %, 120 % sur les bouchées ; shake + flash sur les gros moments ; whip entre deux lieux | Zoom avant/arrière façon Micode, seulement si pertinent | Idem ; déplacements libres sur documents | Idem | Idem |
| Identité | DA Dégustation v2 : sa base de reels améliorée, minimal propre, vrais emojis Apple, couleurs du pays en voyage (§5.1) | Charte food | Méthode Micode/Amistory | PRISME v1 | Liquid Glass |
| Durée | ~3:00 max en TikTok | Selon récit | Selon récit | Selon brief | Selon brief |
| Coupe bouchée | Courte : arrivée en bouche → morsure → réaction (TikTok) ; hook et rétention notés /10, minimum 8 (§5.2) | Dégustation complète | — | — | — |

## 3. Flux de travail

Créer au début une liste de suivi avec ces étapes **distinctes** ; ne jamais fusionner couleur et mixage dans une passe « finitions ».

1. **Préparation.** Copier les rushs d'une carte amovible, conserver les originaux. Projet avec `Media/`, `Projet/`, `Exports/`, `Suivi/`. Examiner durée, cadence, orientation, profil couleur, audio (Cabezer enregistre en 32 bits flottant). Garder une séquence source et une séquence montée.
2. **Transcription et dérush** (§4). Transcrire le rush réel ; ne jamais prendre le script comme preuve de ce qui a été dit. Vérifier les faits (§8). → **Validation du dérush.**
3. **Format.** Ratio/résolution selon la destination ; cadence cohérente avec la source. Recadrer en protégeant yeux, mains, gestes et produit.
4. **Structure et habillage.** Cartographier mise en place → progression → réponse. Appliquer l'identité validée de la famille (§6) ; si elle manque, faire valider un extrait avant de généraliser. Illustrations et animations AE en une passe. Hook finalisé en dernier, une fois la structure stable.
5. **Zooms et mouvements** (§7).
6. **Colorimétrie** (§10).
7. **Musique, SFX, ambiances, mixage** (§11).
8. **Sous-titres** (§9) ; en dégustation, toujours : français en France et Belgique, langue locale ou anglais à l'étranger (à demander).
9. **Contrôles avant export** (§14) puis export (§13).
10. **Revue du MP4 exporté** : visionnage et écoute intégraux, mesures après encodage, aperçu à Cabezer avec les limites réelles du contrôle.
11. **Après publication** : boucle rétention (§15) quand les données existent.

Pour les dégustations, ranger le projet dans `/Users/cabezer225/Documents/ChatGPT/Tiktok degustation/<Sujet>/` (médias, versions, exports, contrôles, suivi ; `Publication/` si couverture et textes sont demandés). Pour le package de publication, utiliser `cabezer-shorts-publication` ou `youtube-publication-package`.

**Travail multi-agents :** quand Cabezer demande plusieurs agents, leur confier des missions séparées (ex. dérush, habillage AE, recherches/illustrations) ; un seul coordinateur intègre dans le projet maître.

**Pilotage de l'ordinateur :** identifier la version et les panneaux réellement présents ; les raccourcis dépendent de la langue. Ne jamais remplacer silencieusement Premiere par un autre éditeur. Si un panneau bloque, décrire le blocage et conserver les étapes vérifiées.

## 4. Dérush et intention du créateur

- Garder sa voix orale, ses connecteurs et ses réactions. Retenir la meilleure prise complète ; couper essais abandonnés et phrases reprises sans changer le sens.
- **Coupe par défaut :** juste après le dernier mot entièrement audible, sans blanc résiduel ; ne jamais couper le début du mot suivant (syllabe ou consonne). Un blanc reste seulement s'il est occupé par une illustration, une transition ou un effet prévu. Placer les coupes à l'écoute et à la forme d'onde, jamais aux seuls timecodes de transcription ni avec une marge fixe.
- **Room tone :** si une coupe laisse un saut de fond sonore audible, combler avec le silence de la pièce du même rush plutôt que de laisser un trou numérique.
- **À protéger toujours :**
  - son **« Bref, c'est partiiii »** : le garder à chaque fois qu'il le dit, dans toutes les vidéos, entier jusqu'à la fin de la dernière syllabe étirée ; placer la sortie après l'extinction réelle du son (consigne du 28/09/2026, Maritozzo) ;
  - la fin des exclamations étirées (« enfin ! », « waouh ») : attendre la fin réelle de la voix avant de couper ;
  - les passages où Cabezer parle de donner ou faire plaisir à sa famille et ses proches, et les moments humains qui montrent son intention ;
  - l'**appel au commentaire de fin** (« commentez le mot… ») avec le mot réellement prononcé : ne jamais le retirer, le vérifier dans la séquence puis dans l'export. Ne jamais l'inventer s'il n'a pas été tourné.
- Le rythme vient du discours et des changements de valeur de plan, pas d'effets à chaque mot.
- **Motif récurrent :** quand le récit s'y prête, installer un repère (phrase, plan, carte, son) lié à un point à retenir, le reprendre aux articulations puis le varier. Ouvrir une boucle au début et la refermer à la fin.
- Après validation du dérush et des retouches manuelles de Cabezer, préserver ses coupes et la voix traitée pendant l'habillage.
- Scripts prompteur : phrases complètes, pas de retour à la ligne forcé en milieu de phrase.

Références : [techniques retenues](references/techniques-et-controles.md), [notes par vidéo](references/tutoriels-2026-09-12.md), [méthode antérieure](references/methode.md), [récit, regard et rythme — Aprilynne Alter](references/aprilynne-recit-regard-rythme.md), [audio, automatismes, motifs](references/tutoriels-2026-09-14.md).

## 5. Vidéos courtes de dégustation

**Direction actuelle : DA Dégustation v2 (02/10/2026)**, fiche complète `/Users/cabezer225/Documents/ChatGPT/Tiktok degustation/Identite-Degustation/DA-Degustation-v2.md`, à lire avant chaque dégustation.
- **Origine :** ses réponses au questionnaire du 02/10, après le rejet du Milan v01 (« SFX pas ouf, pops nuls, dérush pas dynamique, effets pas clean »), et l'analyse de 6 de ses reels (`Tiktok degustation/References-Cabezer/`).
- **Principe :** reprendre **sa propre base** et l'améliorer.
- **Ce qu'elle remplace :** la direction Johan Papz et les stickers détourés.

**Sa base, à garder :**
- sous-titres incrustés tout du long ;
- étiquette produit + prix près du produit ;
- gros plan « regardez-moi l'intérieur » ;
- note sur 10 ;
- bouchée en plan serré ;
- appel au commentaire avec un mot-clé ;
- surtout des coupes franches ;
- 3,6 à 4,2 mots par seconde.

**Au démarrage, demander à chaque vidéo :**
- **Le hook.** Par exemple :
  - son hook habituel ;
  - un hook agressif fait de plusieurs extraits rapides des rushs ;
  - un teaser produit de 0 à 1,3 s sous sa voix, avec une étiquette d'enjeu (Milan : « 19h30 · Luini ferme à 20h ⏰ »).
  - Pas de photos, pas de bouchée tronquée.
- **La langue des sous-titres, à l'étranger** (§9).

**Dérush — dynamique naturel et clarté (consignes du 02/10/2026, issues de ses propres reprises) :**
- **Blancs :** couper respirations et blancs de plus de 0,25 s dans les monologues ; garder les réactions et les échanges. Placer les bords à l'énergie du son, pas aux temps de Whisper (qui étire les mots), en protégeant les mots dits doucement.
- **Hésitations :** les couper, même un seul mot étiré (« Et on… », « une… » avant un nom).
- **Corrections :** ne garder que la bonne version. Par exemple :
  - « Voici les panzerottis / Non, panzerotti / OK » devient « Les gars, voici les panzerotti en personne » ;
  - « un peu plus gras… enfin plus généreux » devient « plus généreux » ;
  - « deux mozzarelles… trois, trois » devient « trois mozzarelles ».
- **Redites et passages où il tourne en rond :** les couper, pour que les explications soient claires.
- **Restes autour d'une coupe :** retirer la phrase entière, y compris les petits morceaux juste avant ou après (deux « c'est bon » restés avant une redite). Retirer aussi un plan sans parole qui traîne après une phrase. Relire chaque segment de moins de 1,5 s voisin d'une coupe.
- **Avant d'appliquer une coupe :** la tester sur le son source (retranscription du passage recollé).
- **Contenu gardé :** arrivée et lieu, commande, potes, moments hors sujet, en version courte. Durée jusqu'à 3:00.
- **Ses coupes priment :** ne pas retirer un passage qu'il a gardé dans son propre dérush sans le lui demander.

**Préparation :** quand il annonce le produit (« on va tester les… »), poser un plan de préparation sous sa voix.
- D'abord le chercher dans les rushs.
- À défaut, prendre une vidéo stock appétissante sous licence (Pexels, Pixabay) :
  - téléchargée seulement après son accord, en lui donnant nom, source et taille ;
  - licence consignée ;
  - conformée à la cadence et au cadre de la séquence (§14).

**Coupe de la bouchée (TikTok et déclinaisons) — courte :**
1. Commencer à l'arrivée du produit en bouche ; retirer préparatifs, attente, approche.
2. Garder la morsure entière à vitesse réelle, en plan serré.
3. Reprendre directement à la réaction vocale utile, en protégeant le début du mot.
4. Retirer chaque « bismillah » sans toucher la bouchée suivante.
5. Repérer ces points à l'image et à l'écoute.

Pour un Short/Reel monté seul ou un autre format, conserver la dégustation complète sauf demande.

**Prix :**
- Seulement aux vraies annonces : montant payé, prix par produit.
- Montant seul en grand, avec un petit shake et une caisse clairement audible.
- Pas de cartouche descriptif ; sous-titres masqués pendant l'animation.

**Images :**
- **Plan produit filmé sans parole :** c'est du B-roll, à placer sous la voix quand il parle du produit.
- **Inserts muets :** toujours sans leur son source.
- **Sources :** vidéos originales, pas de photos ; produits et bouchées toujours visibles sous les textes.

**Son :**
- Pas de musique (noter « musique : absente par choix »).
- SFX tendance TikTok + touche mème, banque Pixabay `Tiktok degustation/SFX-Pixabay/` (licences dans `LICENCES-SFX.md`) :
  - swoosh, pop, ding, boing, scratch, caisse, photo, scintillement ;
  - **pas de mèmes vocaux**, **plus de boom** (retiré le 02/10 : « tu l'utilises mal ») ;
  - clairement audibles, sans en mettre partout ;
  - recadrés sur leur attaque ; le swoosh est calé sur son pic.
- **Chaque SFX appartient à un élément :** si l'élément est retiré, retirer son SFX.

### 5.1 Habillage dégustation — DA v2 (minimal propre)

**Ce que « pas clean » veut dire pour lui :**
- contours épais, ombres baveuses ;
- sticker détouré, pictos dessinés ;
- tampon de ville, liseré tricolore ;
- animations molles.

**Charte :**
- **Police :** moderne grasse, Avenir Next Heavy et Bold.
- **France :** blanc + rouge tomate `#E63946`.
- **Voyage :** couleurs du pays seulement (Italie : rouge `#CE2B37`, vert `#009246`), sans tampon ni liseré. Fiche : `Tiktok degustation/Identite-Voyage/DA-Voyage-v1.md`.
- **Ombres :** courte et nette uniquement.

**Éléments (9:16, base 1080 × 1920) :**
- **Étiquette :**
  - pastille blanche à coins arrondis, texte noir Avenir Next Bold, casse normale ;
  - glisse de 8 px en 4 images ;
  - une étiquette « lieu » dans le hook, une étiquette « produit · prix » à la révélation du produit.
- **Prix :** montant seul, Avenir Next Heavy blanc très grand, pop + petit shake + caisse.
- **Pop-up :**
  - **vrai emoji Apple** (rendu par macOS, `Tiktok degustation/Identite-Degustation/Emojis/`, importé et animé dans AE) + un mot court en capitales si utile ;
  - pop 0 → 118 → 96 → 100 % en 7 images ;
  - 2 à 4 par vidéo, seulement sur de vraies réactions.
- **Note :** « 7-8/10 » en grand + emoji, avec flash et ding.
- **Intérieur :** flash blanc (70 % → 0 en 4 images) + shake de 6 images + emoji 👀 + scintillement.
- **Appel au commentaire :** pastille « commente » + mot-clé en couleur d'accent + 👇.
- **Mouvements :**
  - punch-ins secs en alternance 100 / 115 % aux coupes face caméra, 120 % sur les bouchées ;
  - shake + flash seulement sur les gros moments (prix, intérieur, verdict) ;
  - whip/swish entre deux lieux : 4 à 6 images, agrandi à 130 %, glissement de 12 %, flou de mouvement, swoosh.
  - Ailleurs, coupes franches.
- **Pas d'ajout pour la note :** il a retiré l'étiquette « Pizza fritta · Naples » ajoutée pour relancer l'image. Relancer par punch-in, coupe ou insert, jamais par un texte qu'il n'a pas demandé.

**Réalisation — uniquement dans After Effects (§16) :**
- Une composition éditable par élément, rendue en ProRes 4444 alpha.
- Calage dans Premiere ; punch-ins, whips et shakes dans Premiere (Mouvement / Transformation avec flou de mouvement).
- Gabarits de scripts éprouvés sur Milan : `Tiktok degustation/Milan-StreetFood/Controle/` (`plan_milan_v05.py`, `creer_habillage_milan_v05.py`, `creer_sous_titres_milan_v05.py`, `mix_milan_v05.py`, `generer_montage_milan_v05.py`, `injecter_couleur_mouvements_milan_v05.py`).

### 5.2 Notation obligatoire : hook et rétention sur 10 (consigne du 02/10/2026)

Chaque dégustation est notée avant livraison. **Si une note est sous 8, retravailler puis renoter jusqu'à 8 minimum, et donner les deux notes à Cabezer.** Barème complet : DA v2 §5.

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
- **Blancs :** méthode étalonnée seulement, sur la voix seule. Une trame est un blanc si elle est 18 dB sous le 80e centile sur 4 s. Repères : ses reels 13 à 18 / min, Milan v02 4,2 / min. Ne pas changer de méthode en cours de route.
- **Relances :** une coupe compte seulement si elle change de rush ou de cadre.
- **Clarté :** retranscrire l'export par fenêtres de 10 s qui se chevauchent (Whisper saute des passages sur un long fichier), puis refaire chaque zone douteuse à part.
- **Premier cas, Milan :** v03 10/6, v04 10/8, v05 10/9 ; puis sa reprise v06.

## 6. Identité visuelle par famille

Chaque famille garde une identité reconnaissable, déclinée en 9:16 et 16:9 (taille des textes, composition et zones sûres ajustées, identité inchangée). Avant l'habillage, retrouver la charte et les montages validés de la famille ; ne pas recréer une direction à chaque vidéo ni transposer celle d'une autre famille. Le style par défaut d'un plugin ne définit pas l'identité.

- **Dégustation :** DA Dégustation v2 (§5.1), fiche `Tiktok degustation/Identite-Degustation/DA-Degustation-v2.md`. Ni Johan Papz, ni Food dégustation v1 (Slak v27), ni les stickers et tampons du Milan v01 ne servent plus de modèle.
- **Food long :** [Food dégustation v1](references/identites-visuelles/food-degustation-v1.md) reste un repère de lisibilité. Animations faites dans AE comme la dégustation (§5.1, réalisation) : titres de restaurant, cartes de lieu, prix, notes et comparatifs construits en calques AE, avec ses vraies images (façades, menus, tickets) explorées en caméra 3D plutôt que des cartes génériques.
- **Films/séries :** [PRISME v1](references/identites-visuelles/films-series-prisme-v1.md), validé sur Dune. Réservé à cette famille. Construit dans AE : titres, fiches de personnages et frises en calques natifs, extraits et affiches officiels explorés en caméra 3D. Pas d'affiche ni de visuel généré.
- **Tech :** [méthode Liquid Glass](references/after-effects/tech-liquid-glass.md) ; rendre le propos accessible à un public food. Le verre, les interfaces et les schémas techniques sont faits dans AE (formes, flous, réfraction par effets natifs), avec les vraies captures d'écran et pages officielles. Pas de maquette d'interface générée ailleurs.
- **Cabezer Story :** voir ci-dessous.

**Cabezer Story.** Lire [Raconter avec les images — Micode / Amistory](references/story-montage-micode-amistory.md) avant le découpage visuel ; [registre des références](references/story-references-2026-09-20.md) pour les passages sources.
- Choisir d'abord la scène, l'objet ou la preuve qui apporte quelque chose à la parole, puis concevoir entrée, évolution, maintien, raccord.
- Alterner images réelles, documents explorés, schémas persistants et retours au visage. Titres réservés aux concepts et articulations.
- **Respirations :** garder les pauses qui portent un regard, une émotion, une attente construite ; couper celles où Cabezer cherche ses mots. Cette règle prime sur la coupe au dernier mot.
- Déplacements explicatifs libres sur documents, cartes, objets ; zooms facecam = zooms avant/arrière façon Micode (§7), seulement quand ils servent le propos.
- Ne jamais écrire le nom de chaîne (« Cabezer Story ») dans les animations, titres ou cartes (consigne du 29/09/2026). Seule exception : le générique « Amed Story 🧢 » ci-dessous, nom choisi par Cabezer le 30/09/2026.
- **Refusés :** habillage v08 à grands bandeaux ; Dossiers v0.2 n'est plus la direction par défaut (inventaire d'assets seulement).
- Toute nouvelle direction se valide sur un extrait concret (vraies images, preuve ou mécanisme, visage, raccords), pas sur une série titre/carte.

**Une image par idée, jamais par mot — méthode validée par Cabezer le 29/09/2026** (démo partie 3 de « Comment les fast-foods ont changé notre génération » ; étude image + transcription + son de 9 passages de Micode, Amistory et Liv : `Fast-food-generation-2026-09-21/Coordination/ANALYSE-BROLL-ANIMATIONS-SON-MICODE-AMISTORY-LIV.md`). Consigne : « tu devrais utiliser un b-roll pour faire comprendre ce que je veux dire », pas « un b-roll pour chaque mot » ; une succession d'images inutiles « fait perdre la tête aux viewers ».

1. **Avant de choisir une image**, écrire en une ligne ce que le spectateur doit comprendre dans le passage.
2. **Un seul support par idée**, tenu sur toutes les phrases de l'idée :
   - **Une preuve réelle** (post, profil, article, étude, page officielle), laissée lisible 3 à 11 s, puis explorée (surlignage, zoom sur la ligne désignée).
   - **Un univers visuel suivi** : les mêmes personnes au même endroit sur plusieurs plans de 1,5 à 3 s. Une série de clips d'un même auteur ou tournage, jamais un décor et des personnes différents à chaque phrase.
   - **Un schéma qui se construit** au fil de la parole et revient quand l'idée revient (Micode : 50 s de la même brigade d'icônes). Par exemple, des barres qui changent sur le mot.
   - **Le visage** (5 à 27 s) pour les questions, les avis, la nuance, l'adresse au spectateur et les commentaires sur sa propre démarche.
3. **Énumérations :**
   - si la liste est l'information, un élément par mot dans un même cadre persistant ;
   - si ce sont des exemples d'une situation, montrer la situation en train de se produire ;
   - si Cabezer dit que la liste n'est pas le sujet, rester sur son visage.
4. **Ne pas illustrer littéralement une comparaison ou une métaphore :** « comme un distributeur de tickets » ne devient pas une machine à tickets. Montrer ce que la comparaison veut dire, ou rester sur le visage.
5. **Rappels :** faire revenir un visuel déjà vu quand l'idée revient. Exemples : le souvenir de famille de la partie 2 sur « on n'est plus avec ses parents » ; la cuisine rapide de la partie 1 sur « servir vite ».
6. **Comparaisons :** deux fenêtres dans un même cadre, avec un repère stable.
7. **Titres et cartons :** seulement pour un concept, une date ou un chapitre. Pas de texte qui double chaque nom.
8. **Coupes rapides** (0,4 à 0,8 s) seulement quand la vitesse est le sens : accumulation, « on est envahi de… ».
9. **Temps de lecture (30/09/2026)** — « certaines informations viennent et partent trop vite ». Toute information écrite (texte, traduction, date, tampon, ligne de liste, légende) reste entièrement lisible au moins **max(1,5 s ; 1 s + caractères/15)**. Une image sans texte reste au moins 2 s, une preuve au moins 3 s.
   - Entrées et sorties en 8 à 15 images.
   - L'information reste tant que l'idée continue.
   - Si le débit est trop rapide : prolonger, cadre persistant, texte raccourci ou regroupé.
10. **Pas de B-roll qui répète une animation (30/09/2026).** Après un schéma, une liste ou une page qui a fait comprendre l'idée, tenir l'animation ou revenir au visage ; un B-roll ne suit que s'il apporte du nouveau.
11. **Zooms sur B-roll : sobriété (30/09/2026).** Seulement sur le mot qui désigne un détail ; aucune poussée ni dérive décorative.
12. **Chapitres (30/09/2026).** Couper dans le silence après sa phrase, puis montrer le carton **seul ~3 s**, sans voix, avec la signature musicale. Il se déchire quand sa voix reprend. Le titre qu'il prononce (intro, rappel en conclusion) n'est pas un chapitre.

**Famille sans identité validée :** proposer un court extrait représentatif et le faire valider avant de décliner. Ne pas attribuer arbitrairement couleurs ou polices définitives.

**Story v15 — identité rose pâle `#F2C6C2` (30/09/2026, en attente de validation sur l'aperçu complet).**
- Encre `#2B1B18`, crème `#FFF6EC`, accent rouge tampon `#B8323A`.
- Polices : Hoefler Text Black pour les titres, Futura Bold pour les rubriques, PT Mono pour le ticket.
- Grammaire : papier rose fait dans AE, bords déchirés, tampons, étiquettes de prix, traits à la main, vraies photos en tirages 3D.
- Fiche : `Fast-food-generation-2026-09-21/Coordination/v15/IDENTITE-ROSE-v15.md` ; bibliothèque `Habillage-Story-v01/Scripts/v15/lib_rose_v15.jsx`.

**Passages en langue étrangère (30/09/2026, toutes familles) :** chaque surlignage, entourage ou soulignement sur un texte non français affiche, pendant le coup de feutre, la traduction française fidèle et courte du passage marqué, sans le cacher. **On ne traduit pas les dates** (le surlignage reste) et on n'écrit jamais « traduit de l'anglais » ni de mention de langue.

**Ses propres images (30/09/2026) :** puiser dans toute sa chaîne et ses rushs, pas dans 2 vidéos. Aucun plan en double ; aucune source qui domine. Toute vidéo à télécharger demande son accord, avec la taille.

**Générique réutilisable « Amed Story 🧢 » (30/09/2026, à valider sur l'aperçu) :**
- **Placement :** juste après son intro face caméra, avant le premier sujet, dans le silence après sa dernière phrase d'intro.
  - Dans la timeline maîtresse, garder le temps d'origine : dupliquer la séquence, couper toutes les pistes au point d'insertion et décaler tout ce qui suit de 240 images.
  - La montée musicale d'avant débouche sur l'impact du générique ; le premier carton de partie arrive juste après.
- **Principe :** repris de son générique « HISTOIRE DE FOOD / BY AHMED » (vidéo des scandales de restaurants, 0:49,6–0:57,6) et refait dans l'identité rose. En 8 s :
  1. coupe franche sur papier rose déchiré ;
  2. lettres découpées (ticket, étiquette, tampon, papiers) qui tombent sur les notes ;
  3. glitch dans les couleurs de l'identité ;
  4. replacement sur le motif musical ;
  5. casquette de son logo en autocollant ;
  6. fondu au noir.
- **Fichiers prêts à poser :** `Fast-food-generation-2026-09-21/Habillage-Story-v01/Rendus/Generique/GENERIQUE_Amed_Story_v01_4K.mov` (4K avec son), plus une variante sans impact initial.
- **Pour modifier :** projet AE `AE/Generique-Amed-Story-v01.aep`, une précomposition par lettre ; musique `Audio/Generique/`.

**Fin d'une vidéo Story (30/09/2026, « la fin est trop fin cutter ») :** ne jamais couper juste après le dernier mot.
- Garder son regard silencieux à la caméra quelques secondes, en le vérifiant à l'image dans le rush : fondre au noir **avant** qu'il bouge ou se lève.
- Laisser la musique conclure sur un vrai accord qui s'éteint sur le noir.
- Aucun bruitage sur le fondu, pas de carton d'abonnement.

**Après validation :** une fiche par famille dans `references/identites-visuelles/` : couleurs exactes, polices et graisses, hiérarchie, marges et zones sûres, styles de texte, règles d'animation, MOGRT/presets réellement disponibles, projet modèle, aperçu approuvé, version et preuve de validation. Une refonte devient une nouvelle version.

## 7. Zooms, mouvements et transitions

**Zoom facecam — façon Micode, jamais imposé (consigne du 29/09/2026) :** la règle du zoom iPhone Duo est retirée ; ne plus poser le preset `CABEZER - Zoom iPhone Duo - 10 images` par défaut. Quand un zoom sert le moment (tension, révélation, changement d'idée, chute), faire un zoom avant ou arrière à la manière de Micode : mouvement numérique fluide et progressif (images clés lissées), centré sur le visage, amplitude modérée, puis maintien ; le zoom arrière ramène au cadre de base avant une coupe ou une nouvelle idée. Pas de zoom à chaque plan ni d'aller-retour continu étiré sur toute la prise. Si un calque fixe (retouche de décor, cache) est aligné sur la facecam, lui appliquer exactement le même zoom.

**Whoosh :** plus obligatoire sur chaque zoom ; un zoom lent façon Micode reste silencieux ou porté par la musique. Un whoosh accompagne un mouvement rapide ou une transition marquée, calé sur le déplacement visuel et dosé sous la voix ; éviter les doublons.

**Transitions :** réservées aux changements d'argument ou de séquence. Sonoriser les transitions marquées (fanions, drapeaux) avec un effet synchronisé.

**Speed ramps et raccords dans le mouvement** *(méthode ajoutée le 28/09/2026, à valider sur un premier montage)* :
- Rampes de vitesse sur les gestes de préparation, arrivée du plat, versement, coupe, uniquement sur les **inserts**, jamais sur la parole ni sur la bouchée retenue (qui reste à vitesse réelle).
- Rampe avec Remappage temporel et images clés lissées ; nécessite un rush à cadence élevée (50/60p ou plus) pour un ralenti propre. Vérifier la cadence avant de promettre un ralenti.
- Raccords de mouvement (whip pan, match cut sur un objet ou une forme) pour relier deux lieux ou deux produits dans un hook agressif. Un raccord de ce type = une transition marquée, sonorisée.

**Lissage des images clés :** tout mouvement animé (échelle, position) en Bézier/Progressif, jamais linéaire.

## 8. Recherches, illustrations et références

- **Vérification factuelle :** partir de ce qui est prononcé. Vérifier chiffres, prix, dates, caractéristiques incertains ou susceptibles d'avoir changé ; privilégier la source primaire, contrôler date, territoire, version, unité. Consigner affirmation, passage, lien, date de consultation, résultat (confirmé / nuancé / non confirmé). En cas d'erreur, proposer une correction visible ou une reprise, jamais une recomposition des paroles. Une recherche ne valide pas une dégustation ou un avis.
- **Illustrations :** d'abord les rushs et médias personnels, puis les compléments qui montrent précisément ce qui est évoqué. Conserver auteur, URL, crédits, conditions d'usage, fichier. Une image illustre, elle ne prouve pas et ne doit pas suggérer une expérience que Cabezer n'a pas vécue. Ne pas couvrir chaque phrase de B-roll. En Story, une image par idée, jamais par mot (§6). Préférer visuels officiels de marque et sources tierces aux habillages génériques. Extraits YouTube crédités à l'écran selon [la méthode du 13/09](references/zooms-broll-et-respirations.md).
- **Inspiration actuelle :** avant l'habillage d'une vidéo courte, étudier des références récentes de la même famille (hook, rythme, cadrages, hiérarchie des textes, relances). Consigner liens, dates, passages, métriques visibles. Ne pas affirmer une tendance « virale en ce moment » sans données ; ne pas copier un montage ni récupérer ses sons.

## 9. Sous-titres

**Vidéos tournées à l'étranger — familles hors dégustation (consigne du 28/09/2026, Maritozzo à Naples ; dégustation : voir plus bas) : toujours des sous-titres en anglais.** Deux lignes maximum réellement affichées par bloc. **Ne jamais les afficher pendant qu'un mot ou une phrase est animé à l'écran** (titre, tampon, prix, note, repère, pop-up, CTA…) : couper ou raccourcir le bloc pour laisser l'animation seule, puis reprendre. Traduire le sens oral de Cabezer (ton naturel, pas mot à mot), y compris les échanges avec les vendeurs ; garder les noms propres et le mot exact de l'appel au commentaire. Livrer la piste éditable et le SRT avec le montage. **Style (retour Cabezer sur Maritozzo v09, 28/09/2026) :** pas de légendes Premiere au style générique ; créer les sous-titres dans After Effects avec l'identité de la famille et **animer au moins leur entrée** (pop léger + mots révélés un à un, sortie courte). Coupures de ligne explicites, jamais de retour automatique (Premiere ajoutait une 3ᵉ ligne) : ≤ 24 caractères par ligne en 9:16 à ~70 px sur 1080, blocs trop longs découpés en sous-titres successifs équilibrés, sans mot isolé. Vérifier ensuite sur le MP4 exporté.

**Dégustation — consigne du 02/10/2026 (remplace « aucun sous-titre en France » et le style crème/contour du Maritozzo) :**
- **Toujours des sous-titres incrustés**, comme dans ses reels.
- **Langue :**
  - en France et en Belgique, en français, mot à mot ;
  - à l'étranger, dans la langue locale ou en anglais selon la pertinence. **Le lui demander à chaque vidéo tournée à l'étranger** (Milan : anglais).
- **Style DA v2 :**
  - Avenir Next Heavy en capitales, blanc, ombre courte et nette, sans contour épais ;
  - vers 72–75 % de la hauteur ;
  - mots clés (produit, prix, note, lieu) dans la couleur d'accent.
- **Découpage :**
  - en français, un mot à la fois ;
  - en traduction, paquets de 1 à 3 mots, 18 caractères au plus, les petits mots collés au mot qui suit.
- **Entrée :** pop en 4 images ; sortie sèche au paquet suivant.
- **Calage :**
  - les paquets sont répartis seulement sur le temps conservé au dérush ;
  - un paquet qui tombe sous un pop-up, un prix, la note ou l'appel au commentaire attend la fin de l'animation, sinon il est retiré ;
  - la traduction est réécrite sans les phrases coupées.
- **Réalisation :** composition AE rendue en ProRes 4444 alpha, plus le SRT.
- **Si Cabezer retouche ensuite la timeline :** ce rendu d'un seul tenant ne suit pas ses coupes. Le recouper aux mêmes images, puis vérifier la synchro dans l'export.

**Autres familles : deux lignes maximum réellement affichées, pour chaque bloc.** Un SRT correct ou une mesure hors Premiere ne suffit pas : vérifier dans Premiere puis dans le MP4 exporté après tout import, changement de style ou déclinaison. Créer des sous-titres éditables depuis le montage final ; corriger noms, chiffres et ponctuation. Corriger par la segmentation aux groupes de sens (sous-titres successifs), pas en réduisant la police ponctuellement. Respecter taille, marges et zones sûres de l'identité ; éviter l'interface mobile et le visage. Pour animer des sous-titres : Graphiques et titres > Mettre à niveau la légende. Ne pas annoncer les sous-titres contrôlés tant qu'un bloc sur trois lignes existe.

## 10. Colorimétrie

Passe distincte et obligatoire. Consigner version, réglages, contrôle, limites.

**Chaîne technique selon la caméra** — confirmer le profil réel du rush :
- **DJI Osmo Pocket 3, D-Log M :** exposition/blancs → conversion DJI D-Log M → Rec.709 **une seule fois** → **Exterior Cinema** ou **Exterior Doux**, dosé sur les plans réels. Fichiers : [chaîne Pocket 3 et LUT Cabezer](references/dji-osmo-pocket-3-luts.md), `assets/luts/dji-osmo-pocket-3/`.
- **Panasonic V-Log/V-Gamut :** conversion Panasonic → Rec.709, **jamais la LUT DJI**.
- **Source déjà Rec.709 :** pas de conversion technique. Jamais de LUT D-Log M sur du HLG/HDR ; jamais conversion automatique + LUT technique cumulées.

**Correction primaire :** exposition, balance des blancs, contraste, carnation ; comparer avant/après sur plusieurs prises et harmoniser. Traiter à part captures d'écran, graphiques et extraits de films (pas de look facecam dessus).

**Correction secondaire food** *(méthode ajoutée le 28/09/2026, à valider)* :
- Après la primaire, isoler par TSL (Lumetri > Courbes teinte/saturation ou TSL secondaire) les couleurs clés du produit — rouge de sauce, jaune de fromage, vert d'herbes, brun de croûte — et les renforcer légèrement sans toucher la carnation.
- Contrôler la carnation sur la ligne de chair du vectorscope, et les aliments sur un moniteur de référence visuel : le produit doit donner envie sans paraître artificiel.
- Lumières mixtes de restaurant (néon + fenêtre) : corriger la dominante principale en primaire, puis masquer/suivre la zone gênante si elle touche le produit.
- Harmoniser les inserts B-roll avec la facecam de la même scène.

## 11. Audio : SFX, musique, ambiances, mixage

**Organisation des pistes :** A1–A2 voix, A3–A4 SFX, A5 musique ; ajouter une piste ambiances si utilisée.

**SFX — bibliothèque ouverte.** Choisir selon le sujet et l'animation. Clics, caisses, whooshes et accents doivent être **clairement audibles** dans le mix final sous une voix intelligible, sans être envahissants ; un son inaudible ne remplit pas sa fonction. Ne pas multiplier les accents ni recouvrir bouchées et réactions. Refuser les SFX synthétisés ou génériques peu pertinents : sources = fichiers de Cabezer, ses bibliothèques **Cabezer-Sons-Vol1** et **Cabezer-Ajouts-Food-Lifestyle** (WAV 24 bits/48 kHz), Adobe Stock via son compte, ou toute source dont la licence couvre l'usage. Ne jamais prélever les sons d'une vidéo TikTok ou d'un tutoriel. Consigner provenance, licence, crédits, fichier ; ne pas inventer une licence.

| SFX de base | Fichier |
|---|---|
| Caisse | [modestas123123-cash-register-kaching-sound-effect-125042.mp3](assets/sfx-cabezer/modestas123123-cash-register-kaching-sound-effect-125042.mp3) |
| Riser | [u_1pruylktlg-riser-7-130957.mp3](assets/sfx-cabezer/u_1pruylktlg-riser-7-130957.mp3) |
| Whoosh | [soundreality-whoosh-end-384629.mp3](assets/sfx-cabezer/soundreality-whoosh-end-384629.mp3) |
| Clic de souris | [matthewvakaliuk73627-mouse-click-290204.mp3](assets/sfx-cabezer/matthewvakaliuk73627-mouse-click-290204.mp3) |

Provenance et empreintes : [manifeste](assets/sfx-cabezer/manifest.json) (pas une preuve de licence). Copier les sons utilisés dans les médias du projet.

**Ambiances et sound design de fond** *(méthode ajoutée le 28/09/2026, à valider)* :
- Sous les inserts muets et aux changements de lieu, une ambiance discrète (salle de restaurant, rue, cuisine) peut lier les plans, prise de préférence dans les rushs du lieu, sinon d'une banque licenciée.
- Toujours sous la voix, jamais au détriment des bouchées ; ce n'est pas une musique de fond et ne contredit pas la règle dégustation.
- Fondus d'entrée/sortie aux changements de séquence ; ne pas laisser une ambiance couper net sur une coupe.

**Musique (hors dégustation) :** choisir, maintenir, changer ou retirer selon l'émotion réelle (question, découverte, doute, verdict, moment drôle), pas à chaque changement de produit. Changements aux articulations naturelles, avec fondus ou silences maîtrisés ; fondu exponentiel en fin de morceau. Ne pas déplacer une réaction pour suivre la musique. Conserver la vitesse d'origine du morceau.
- Films/séries : `/Users/cabezer225/Downloads/MUSIQUES` et `/Users/cabezer225/Documents/ChatGPT/Film/musique`, après écoute réelle des extraits.
- Compositions originales : [bibliothèque originale Cabezer](references/musiques-originales-cabezer.md) (Cédric Grolet notamment) ; ne pas confondre avec les achats Halal Beats. Ne pas garantir l'absence de revendications.
- Distinguer sélection proposée, employée, approuvée. Présence locale ≠ licence.
- **Story (consigne du 29/09/2026) :** décider musique ou silence selon le contexte de chaque séquence, sans se limiter aux nasheeds ni aux bibliothèques locales ; d'autres musiques et bruitages libres de droits peuvent être utilisés (téléchargement après accord de Cabezer, licence consignée). Si aucune musique libre ne convient, composer une musique originale calée sur le montage (temps forts sur les coupes, impacts sur titres et chapitres). S'inspirer de Micode (nappes et pulsations électroniques, tension) et d'Amistory (rythmes légers et documentaires).
- **Story, mesures sur Micode, Amistory et Liv, règle validée le 29/09/2026 (« comme les références ») :**
  - **Nappe basse presque continue** sous toute la narration, visage compris, environ 15 dB sous la voix. Elle change de texture selon la partie : groove léger pour une scène de vie, motif analytique pour les chiffres.
  - **Plus basse ou absente** sous une interview ou une source qui parle.
  - **Vrai silence de 1 à 2 s** juste avant une bascule (nouvelle partie, rebondissement, idée reçue cassée), ou sous la chute.
  - **Montée ou impact** juste avant un concept clé ou une preuve.
  - Cette règle remplace l'ancienne consigne « silence pendant les explications face caméra ».
- **Vrais instruments, consigne du 29/09/2026 (« utilise de vrais instruments pour la musique, comme GarageBand ») :**
  - Ne plus synthétiser la musique note à note (numpy).
  - Composer avec de vrais enregistrements : les Apple Loops de GarageBand (sons principaux installés sur son Mac, `/Library/Audio/Apple Loops/Apple`), libres d'usage dans une composition. Ne jamais publier une boucle seule en l'état.
  - Méthode :
    1. Indexer les boucles (tempo, tonalité, instrument), à partir des métadonnées CAF.
    2. Choisir des familles pensées pour aller ensemble, dans une même tonalité (ex. « Longing » en do mineur et « Rise Up » en do majeur, 82 BPM).
    3. Ramener au tempo commun avec `atempo`.
    4. Assembler zone par zone : nappe, groove, pulsation, preuves, comparaisons, chapitres, montées, silences.
  - Consigner les boucles utilisées.
  - La bibliothèque complète de GarageBand (25 Go) n'est pas installée ; la télécharger seulement avec son accord.
- **De vraies compositions, consigne du 30/09/2026** (« les musiques sont souvent les mêmes, compose réellement 2 ou 3 musiques avec une ambiance pour la vidéo en général et 2-3 ambiances max par émotion adaptées aux passages ») :
  - Le collage de boucles zone par zone ci-dessus sonnait comme une seule boucle partout ; il ne sert plus de méthode par défaut.
  - Composer **2 ou 3 thèmes par vidéo**, chacun avec mélodie, harmonie, basse, rythme et forme (intro, thème, développement, reprise, fin). Par exemple : un thème principal chaleureux qui revient en conclusion, un thème « explication », un thème « tension/écran ».
  - Au plus **2 à 3 ambiances par émotion**, déclinées de ces thèmes (orchestration, densité). Les changements se font aux articulations (chapitres, silences, montées).
  - Jouer les notes avec les **instruments échantillonnés d'Apple** installés : pianos, guitares et Drum Kit Designer de `/Library/Application Support/Logic/EXS Factory Samples/` ; cordes, cuivres, bois, contrebasse de `/Library/Application Support/GarageBand/Instrument Library/Sampler/Sampler Files/`. Humaniser et ajouter de la réverbération.
  - Fournir les thèmes seuls pour l'écoute, et des stems par thème.
  - La musique **conclut vraiment** à la fin de la vidéo (cadence, résonance) : jamais de fin coupée sèche.
  - Première application : `Fast-food-generation-2026-09-21`, `Audio/MUSIQUE_v10_THEMES_0-19m03.wav`, scripts `Habillage-Story-v01/Scripts/v15/musique/compose_v10_themes.py` + `exs_sampler.py`, feuille de cue `Coordination/v15/MUSIQUE-v10-partition.md`.

**Mixage — passe distincte et obligatoire :**
- **Traitement voix uniforme** sur toute la séquence : mêmes réglages fixes sur tous les clips (réduction de bruit, EQ de présence, compression douce) + un limiteur unique sur la piste. Pas de « Correspondance automatique », pas de « Dynamique » d'Essential Sound, pas d'« Améliorer le dialogue » (change le timbre).
- Régulariser la voix entre prises, puis doser SFX, ambiances et musique dessous ; soigner fondus et crêtes ; jamais d'écrêtage.
- Écouter les raccords en contexte ; réécouter le MP4 à volume normal, sur petit haut-parleur et en mono si possible. Les valeurs de tutoriels et les mesures complètent l'écoute sans la remplacer.
- Si l'écoute est impossible, livrer l'aperçu en le disant et demander la validation auditive ; ne pas déclarer le mix validé.

Une demande de terminer musique, SFX, mixage et couleur autorise ces passes ensemble, sans validations intermédiaires redondantes.

## 12. Déclinaisons et tournages multi-caméras

**Du format long aux Shorts** *(méthode ajoutée le 28/09/2026, à valider)* — pour SCANDALE FOOD, Story, food long :
1. Repérer les passages **autonomes** : une idée complète, compréhensible sans le reste, avec une chute ou un verdict.
2. Écrire un nouveau hook à partir des paroles existantes (réordonner des prises, jamais recomposer une phrase pour changer son sens).
3. Recadrer 16:9 → 9:16 : Auto Reframe comme point de départ, puis correction manuelle des images clés pour garder visage, produit ou document lisibles. Refaire les textes à l'échelle verticale selon l'identité de la famille.
4. Appliquer les règles du format court de la famille (dégustation : sous-titres français en France et Belgique, langue locale ou anglais à l'étranger, etc.).
5. Fin qui renvoie à la vidéo longue ou qui boucle sur le début.
6. Une séquence par Short dans le même projet, nommée d'après le passage.

**Déclinaison du même montage court** (TikTok → Shorts/Reels) : conserver coupes et durée validées ; adapter seulement les zones sûres si besoin.

**Multicam** *(méthode ajoutée le 28/09/2026, à valider)* :
- Synchroniser par forme d'onde audio (Créer une séquence source multicaméra > Audio), contrôler la synchro sur un clap ou un son net.
- Harmoniser les boîtiers (Pocket 3, iPhone, Panasonic) en couleur avant le montage multicam : chaîne technique propre à chaque caméra (§10), puis correspondance sur la caméra principale.
- Choisir le meilleur son comme piste principale ; ne pas mélanger les micros des deux caméras sur la voix.

## 13. Export et cibles de plateforme

Exporter en MP4 H.264 (ou H.265 si demandé) au ratio, à la résolution et à la cadence du projet. Nommer `<Sujet>_<plateforme>_v<NN>.mp4`.

| Destination | Format de base | Repères à vérifier |
|---|---|---|
| TikTok / Reels / Shorts | **FHD 1080×1920 exporté directement de Premiere** (consigne du 02/10/2026) : taille d'image personnalisée 1080 × 1920, « Rendu à la résolution maximale » et « Qualité de rendu maximale » cochés, H.264 VBR 1 passage environ 20 Mbit/s, AAC 320 ; cadence source ; master 4K seulement sur demande | Zones sûres : textes hors du bas (légende, boutons) et du bord droit ; texte clé dans le tiers central |
| YouTube long | 1920×1080 ou 3840×2160, cadence source | Chapitres et fin compatibles avec l'écran de fin |

**Loudness :** les plateformes normalisent le volume ; YouTube est généralement cité autour de −14 LUFS intégrés. Ce sont des **repères de contrôle, pas des cibles imposées** : le mix se valide à l'écoute, puis se mesure sur le MP4 exporté (niveau intégré et crêtes vraies, sans écrêtage). Consigner les mesures réelles.

Enregistrer le `.prproj` (et le `.aep` si AE a servi) avant chaque export.

## 14. Contrôles avant livraison

**Liste de contrôle — relire chaque état séparément :**
- Dérush/raccords : aucun mot coupé, aucun blanc résiduel non voulu, appel au commentaire présent et entier.
- Cadrage, zones sûres, illustrations (sources et crédits consignés).
- Habillage ; sous-titres (dégustation : français en France et Belgique, langue choisie à l'étranger ; masqués pendant les textes animés ; autres familles : 2 lignes max).
- **Dégustation :** notes hook et rétention ≥ 8 (§5.2) ; aucun reste de phrase coupée ni plan muet qui traîne ; pas de SFX orphelin d'un élément retiré.
- Musique / SFX / ambiances : audibles, dosés, whooshes synchronisés.
- **Colorimétrie** faite et comparée.
- **Mixage** fait et écouté.
- Début/fin, durée (≤ 3:00 en TikTok dégustation), pas de noirs involontaires, pas de médias hors ligne, pas d'audio d'insert résiduel en dégustation.
- AE : compositions liées/rendues, alpha correct, pas d'audio guide en doublon, `.aep` et sources conservés.

**Pièges vérifiés (Milan, 02/10/2026) :**
- **Ordre des clips :** dans un FCP XML, écrire les clips de chaque piste dans l'ordre chronologique. Un clip écrit après un clip plus tardif s'importe, mais manque à l'export.
- **Média sans son :** un média déclaré avec son mais qui n'en a pas (stock passé en `-an`) s'importe hors ligne. Lui ajouter une piste muette.
- **Stock :** conformer à la cadence et au cadre de la séquence (29,97 i/s, 2160 × 3840) avant import.
- **Import :** ouvrir le XML sans projet ouvert, sinon il s'importe dans le projet ouvert.
- **Retouches de Cabezer :** enregistrer ses retouches sous une nouvelle version avant d'exporter, puis vérifier que les pistes d'un seul tenant (sous-titres) suivent ses coupes.

**Contrôles automatisables** *(méthode ajoutée le 28/09/2026, outils à tester avant usage)* : avec un script ExtendScript/UXP ou une analyse du MP4 exporté (ffmpeg/ffprobe), repérer médias hors ligne, trous et noirs dans la timeline, clips audio non muets sur les pistes d'inserts, durée, niveaux et crêtes. Ces contrôles signalent des cas à revoir ; ils ne remplacent pas le visionnage et l'écoute.

## 15. Boucle rétention → montage

*(Méthode ajoutée le 28/09/2026, à valider.)* Après publication, quand les données existent (YouTube Studio, vidIQ, statistiques TikTok) :
1. Récupérer la courbe de rétention et les moments de décrochage marqués.
2. Les relier à la timeline du montage publié : hook, entrée du produit, bouchée, relances, transitions, fin.
3. Consigner dans le suivi du projet : moment, ce qui se passe à l'écran, hypothèse.
4. Quand une même observation revient sur **plusieurs vidéos de la même famille**, la proposer à Cabezer comme nouvelle règle de ce skill. Une vidéo isolée ne suffit pas.
Ne jamais présenter une hypothèse comme une cause prouvée ; la rétention dépend aussi du sujet, de la miniature et de la diffusion.

## 16. After Effects, Tesseract et Higgsfield

- **Toutes les animations se font dans After Effects (30/09/2026), quelle que soit la famille.** Elles sont construites en calques AE natifs et modifiables :
  - animateurs de texte, effets et préréglages d'AE, Trim Paths, caches par approche, caméra 3D et profondeur de champ ;
  - courbes d'accélération travaillées, jamais linéaires ;
  - une composition par scène, nommée, que Cabezer peut ouvrir et retoucher.

  **Plus de « génération » comme avant :**
  - pas de gabarit générique assemblé par script (cartes arrondies sur voile flouté, flèches, nœuds, même pop partout), jugé « comme tous les utilisateurs de Claude » ;
  - pas d'image ni de graphisme fabriqué hors d'AE (Python, HTML, IA) ;
  - pas d'animation générée par IA.

  Seules les vraies sources sont importées : rushs, photos, captures de pages. Un script peut piloter AE, mais le résultat doit être un vrai projet AE travaillé.
- **Premiere ↔ AE :** lire [le flux et les techniques](references/after-effects/premiere-after-effects.md) avant l'habillage : Dynamic Link ou rendu intermédiaire, alpha, contrôleurs, versions, conservation des projets modifiables. Titres, cartes, prix, tracés, masques, suivis, détourages, interfaces dans AE ; calage final dans Premiere. [Registre des sept tutoriels AE](references/after-effects/tutoriels-2026-09-16.md).
- **Tesseract :** animations ou transitions demandées seulement ; jamais dérush ni montage final. Rendre, importer, vérifier dans Premiere ; conserver le `.tsrct` et son rendu à part. [Échange Premiere ↔ Tesseract](references/premiere-tesseract.md).
- **Higgsfield/Higgsedit :** [méthode intégrée](references/montage-higgsfield.md) (entrée/maintien/sortie, textes animés, synchronisation, coupes ciblées, contrôle du rendu). Pas de génération IA, d'abonnement ou de transfert de rushs imposés.
- Techniques Premiere utiles : imbriquer un élément réinitialise recadrage et point d'ancrage avant un effet ; modes de fusion (écran, incrustation) pour les textures.

## 17. Plugins

Consulter [l'inventaire et l'état vérifié](references/plugins-installes.md). Utiliser un plugin quand il apporte un gain réel, sans multiplier les effets. Consigne d'installation : **gratuits uniquement pour le moment**. Téléchargé, installé, en essai et fonctionnel dans Premiere sont des états distincts ; tester sur une copie avant usage réel. Un preset ou plugin n'autorise pas automatiquement l'usage de son audio intégré.

## 18. Apprendre de nouvelles références

Cabezer veut des méthodes réellement étudiées, pas des liens. Lire le contenu ou la transcription d'un tutoriel avant d'en tirer des règles ; indiquer la couverture réelle (transcription lue, images examinées, visionnage non attesté) et les dépendances de version ou de plugin. Les valeurs et promesses d'un tutoriel ne deviennent pas des règles universelles. Consigner dans une fiche `references/` et ajouter ici seulement la règle retenue.

## Historique des consignes

Résumé des changements qui expliquent les règles actuelles (détails dans les fiches liées).

- **02/10 — dégustation refondue (Milan street food).**
  - Milan v01 rejeté, puis questionnaire complet : **DA Dégustation v2** (§5, §5.1), à partir de ses propres reels. Elle remplace Johan Papz, les stickers détourés, les tampons et liserés.
  - Vrais emojis Apple ; Avenir Next ; rouge tomate en France, couleurs du pays en voyage.
  - Punch-ins secs, shake + flash, whips entre deux lieux.
  - SFX Pixabay sans mèmes vocaux ; **boom retiré**.
  - **Sous-titres :** désormais toujours en dégustation, en français en France et Belgique, langue locale ou anglais à l'étranger, à lui demander (§9). Le hook se demande à chaque vidéo.
  - Après sa reprise du dérush : clarté (hésitations, bonne correction seulement, redites, restes autour des coupes), plan de préparation à l'annonce du produit, **notation hook et rétention /10 avec minimum 8** (§5.2).
  - Après sa reprise de la v05 : pas d'étiquette ajoutée pour la note ; retirer le SFX d'un élément retiré.
  - Exports TikTok en FHD 1080×1920 directement depuis Premiere (§13).

- **13/09** : méthode zooms/B-roll/respirations ; extraits YouTube crédités.
- **14/09** : zoom iPhone Duo exclusif (fluide IN-OUT rejeté sur Dune) ; whoosh sur chaque zoom ; sous-titres 2 lignes max ; musique, SFX, mixage, couleur obligatoires.
- **16/09** : AE intégré ; chaîne Pocket 3 ; direction dégustation et durée ~3:00 ; inserts muets ; plus de sous-titres en dégustation ; pas de musique en dégustation ; nouvelles animations food sans PRISME ; musique selon les émotions. *(Restriction à cinq SFX et interdiction des whooshes en dégustation — levées le 23/09 ; « plus de sous-titres en dégustation » levé le 02/10.)*
- **17/09** : TikTok dégustation « arrivée en bouche → morsure → parole » ; côté humain protégé ; recherches/illustrations ; fusion Higgsfield.
- **18/09** : méthode Aprilynne Alter (récit, regard, rythme).
- **20/09** : méthode Story Micode/Amistory ; v08 refusé, Dossiers v0.2 abandonné comme défaut.
- **23/09** : bibliothèque SFX ouverte, whooshes permis partout, SFX clairement audibles ; choix du hook et annonces de prix en TikTok dégustation.
- **26/09** : références Johan Papz.
- **27/09** : dérush Pizza-Naples ; appel au commentaire de fin toujours conservé.
- **28/09** : réécriture du skill en règles actuelles ; ajout des méthodes speed ramps, secondaire food, ambiances, long → Shorts, multicam, cibles d'export, contrôles automatisables et boucle rétention (à valider sur de vrais montages).
- **28/09 (bis)** : animations des dégustations désormais inspirées des reels de Johan Papz (§5.1) ; les vidéos précédentes de Cabezer ne servent plus de base pour ces animations.
- **30/09** : animations uniquement dans After Effects, pour tous les projets, règle déclinée par famille : dégustation §5.1, food long, films/séries, tech §6 (plus de génération ni de gabarit générique). Story v15 : identité rose pâle `#F2C6C2` ; traduction française des passages étrangers surlignés ; images variées de toute sa chaîne. Musique Story : 2–3 vrais thèmes composés et au plus 2–3 ambiances par émotion (§11). Pas de fin coupée sèche. Générique réutilisable « Amed Story 🧢 » entre l'intro face caméra et le premier sujet (§6). Sa chaîne YouTube enregistrée à l'écran, et non son profil TikTok, quand il parle de sa chaîne principale.
- **30/09 (bis)** : Story — chapitres en carton seul ~3 s sans sa voix ; musique encore plus basse (nappe environ 24 dB sous la voix) ; dates non traduites, aucune mention de langue ; temps de lecture minimal pour chaque information ; pas de B-roll qui répète une animation ; zooms de B-roll seulement sur désignation ; bruitages choisis : tampon, impression de ticket, coche au feutre, et vraie déchirure de papier (CC0).
- **29/09 (ter)** : musique Story en vrais instruments (Apple Loops de GarageBand), plus de synthèse note à note.
- **29/09 (bis)** : Story — une image par idée et non par mot (univers suivi, preuve réelle, schéma qui se construit, visage ; règle des énumérations ; rappels), nappe musicale continue sous la narration avec silences de bascule ; validé sur la démo partie 3 de « Comment les fast-foods ont changé notre génération ».
- **29/09** : zoom iPhone Duo retiré ; zooms avant/arrière façon Micode, seulement si pertinents ; musique Story selon le contexte (pas forcément nasheed), autres sources libres permises, composition originale si besoin ; plus jamais « Cabezer Story » écrit dans les animations.
- **28/09 (ter, Maritozzo)** : « Bref, c'est partiiii » toujours gardé entier ; fin des exclamations étirées protégée ; vidéos tournées à l'étranger : sous-titres anglais toujours, 2 lignes max, masqués pendant les mots ou phrases animés.