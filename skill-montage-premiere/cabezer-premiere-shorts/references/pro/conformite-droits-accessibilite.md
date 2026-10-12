# Conformité, droits et accessibilité à l'écran

> **Réponses de Cabezer du 12/10/2026 — elles priment sur cette fiche**, en particulier sur sa section « Décisions à demander ». **Format d'abord, famille ensuite (SKILL §2)** : long (L-Food, L-Story, L-Tech, L-Films, L-Life) ou court (C-Food, C-Story, C-Tech, C-Films, C-Life) ; codes de cette fiche : D = C-Food, F = L-Food, S = L-Story, P = L-Films, T = L-Tech ; nouvelle famille Lifestyle (vlogs, face caméra : aucune musique, SFX comme la dégustation). **Tous les courts** : hook demandé, sous-titres mot à mot, aucune musique, SFX comme la dégustation, punch-ins secs, appel au commentaire, notation sur 10, identité propre au court. **Longs** : SRT seul en France ; composition musicale en Story, food et tech ; respirations d'émotion gardées en films/séries et au verdict du food long ; 4K si rushs 4K. Aussi : identité Story v15 et générique « Amed Story 🧢 » supprimés ; jamais de foley d'aliment ; ambiance en dégustation proposée au premier usage ; un rendu de sous-titres par passage ; intervenants identifiés à la première apparition (hors courts food) ; au plus deux passes de retravail sous 8 ; Tesseract, Higgsfield et SCANDALE FOOD retirés. **Réponses techniques (série 3)** : interface de Premiere et d'AE en anglais ; scripts AE et Terminal autorisés ; stock libre de droits sans redemander ; tout SFX de la banque Pixabay permis ; arrêt sur image permis partout ; pas de test de photosensibilité ; audio YouTube 384 kbit/s ; proxys toujours en long ; Frame.io pour les relectures ; WhisperX à installer ; « 19h30 » et « 12,50 € » ; Liquid Glass à recréer. **Pour cette fiche** : Claude signale au dérush les personnes filmées, Cabezer décide du floutage ; la mention commerciale (formule et durée) est choisie par Cabezer à chaque vidéo ; le test de photosensibilité n'est fait que sur sa demande. Liste complète : `../decisions-en-attente.md`.

Fiche de référence pour tout ce qui, à l'écran, expose Cabezer à un retrait de vidéo, à une revendication, à une plainte ou à un malaise du spectateur : personnes filmées, données visibles, mentions commerciales, extraits tiers, musiques, flashs, typographie française, identification des intervenants, contraste et sous-titres accessibles. Dernière vérification : 12/10/2026. Ce sont des **repères pratiques, pas un conseil juridique** : tout cas limite passe par Cabezer, puis par un juriste. Versions, libellés lus à l'écran et test de fumée des scripts : `pilotage-environnement-reprise.md` et `Suivi/environnement-verifie.md`.

## Quand lire cette fiche

- **Au brief (skill §3, étape 0)** : poser les questions de contenu commercial, de personnes filmées et d'extraits (§2.1, §3.1, §4.1).
- **Au dérush** : repérer personnes, enfants, plaques, écrans et tickets (§2) ; signaler les rushs qui scintillent (§6.7).
- **Avant l'habillage** : placer la mention commerciale, les cartouches d'intervenants et les crédits d'extraits (§3, §4, §8).
- **Avant tout export de contrôle** : typographie (§7), contraste (§8.2) ; décompte des flashs (§6.4) seulement si Cabezer demande un test de photosensibilité.
- **Au contrôle final et à la livraison** : liste de contrôle (§12) ; `organisation-livraison-qc.md §10.2` y renvoie.

À ne pas lire pour : la technique de montage, la publication (skills `cabezer-shorts-publication`, `youtube-publication-package`), l'identité visuelle (skill §5.1, §6). **Aucune règle ne contredit le skill** (§1) ; les décisions de Cabezer sont reportées dans « Décisions à demander » (§13). Familles : D dégustation, F food long, S Cabezer Story, P films/séries PRISME, T tech, H hors familles (le Lifestyle est une famille à part entière et suit ici les mêmes règles que H). **L'interface de Premiere et d'After Effects est en anglais** : le libellé anglais fait foi, le français entre parenthèses n'est qu'un repère ; tout libellé non lu à l'écran est marqué « libellé à confirmer » ; aucun raccourci clavier n'est utilisé (décision B.4).

## Sommaire

1. Principes et vue d'ensemble · 2. Droit à l'image et floutage · 3. Contenu commercial · 4. Extraits tiers · 5. Musique et licences · 6. Photosensibilité (limites chiffrées DA v2) · 7. Typographie française · 8. Intervenants et contraste · 9. Sous-titres accessibles · 10. Techniques · 11. Erreurs de débutant → réflexes de pro · 12. Liste de contrôle · 13. Décisions à demander · 14. Sources étudiées

---

## 1. Principes, niveaux de preuve et vue d'ensemble

**Pourquoi** : ces points se jouent après la publication (retrait, amende, revendication, plainte) et ne se rattrapent pas par un nouvel export. Ils relèvent du montage : flou, mention, crédit, rythme des flashs et typographie se posent dans Premiere et After Effects (AE).

**Niveaux de preuve** (même grille que `organisation-livraison-qc.md §1`) :
- **[Lu]** texte primaire, code ou donnée lus (WCAG, CLDR, LanguageTool, page YouTube).
- **[Mesuré]** essai exécuté le 12/10/2026 (ffmpeg 6.1.1, Python 3, numpy, conteneur Linux à 4 cœurs, **pas le Mac de Cabezer**).
- **[Extrait]** résultat de recherche ou synthèse secondaire, texte officiel non lu : à reprendre à la source avant d'en faire une règle ferme.
- **[Pratique]** usage de métier ou déduction non sourcée : valeur de départ à tester.
- **[À vérifier]** sources contradictoires ou non lues.

**Limite d'accès.** Légifrance, economie.gouv.fr, ARPP, CNIL, Imprimerie nationale, Netflix, Pixabay (conditions) et Adobe Help sont refusés par le proxy ; la récupération de pages de presse juridique a aussi échoué. Tout le droit ci-dessous est donc **[Extrait]**. Les seuils de flash, le contraste, les espaces insécables et le Content ID sont **[Lu]** ou **[Mesuré]**.

**Vue d'ensemble : ce qui bloque la livraison.**

| # | Sujet | Règle de départ | Statut |
|---|---|---|---|
| 1 | Personne reconnaissable (client, passant, employé) | Claude signale au dérush ; Cabezer décide du floutage | [Pratique] + [Extrait] |
| 2 | Enfant identifiable | Signalé en priorité ; Cabezer décide (repère : accord des parents pour publier) | [Pratique] + [Extrait] |
| 3 | Plaque, ticket, écran, document | Signalés ; flou seulement de ce que Cabezer désigne | [Extrait] (CNIL) + [Pratique] |
| 4 | Repas offert, invitation, partenariat | Signalé au brief ; mention (formule et durée) choisie par Cabezer à chaque vidéo | [Extrait] |
| 5 | Extrait de film, série, vidéo | Durée utile, commenté, source affichée au moins 3 s ; un crédit n'est pas une autorisation ; Content ID signalé | [Extrait] |
| 6 | Musique, son | Une ligne par piste dans `licences.csv`, preuve de licence | [Extrait] |
| 7 | Flashs | Pas de test sans demande de Cabezer ; repère facultatif : au plus 3 flashs généraux par seconde (WCAG 2.3.1) | [Lu] + [Mesuré] |
| 8 | Typographie française | Espaces insécables, virgule décimale, œ, accents sur capitales | [Lu] (CLDR, LanguageTool) |
| 9 | Intervenant nommé | Nom et fonction à la première apparition (hors courts food), durée selon la formule du skill | [Lu] (WCAG) + [Pratique] |
| 10 | Contraste du texte | 4,5:1 (normal), 3:1 (grand texte), sans arrondi | [Lu] (WCAG 1.4.3) |

Distinguer appliqué / contrôlé / validé par Cabezer (skill §1) : un test de flash, s'il est demandé, n'est pas un avis médical, une mention posée n'est pas validée juridiquement.

---

## 2. Droit à l'image : personnes, mineurs, plaques, écrans, floutage

### 2.1 Cadre (France) et questions à poser

**Pourquoi** : Cabezer filme en restaurant et dans la rue ; des clients, des employés, des enfants, des plaques et des tickets entrent dans le cadre.

*Repères légaux ci-dessous : information facultative pour Cabezer, qui décide ; ils ne déclenchent aucun flou automatique.*

- **Droit civil.** Le droit à l'image procède du respect de la vie privée (article 9 du Code civil) : une personne identifiable peut s'opposer à la publication de son image, même prise en lieu public, sauf intérêt légitime d'information [Extrait ; article non lu].
- **Droit pénal.** L'article 226-1 du Code pénal punit la captation de l'image d'une personne en lieu privé sans consentement (un an, 45 000 € selon les synthèses) [Extrait]. Un restaurant ouvert au public est un cas intermédiaire : lieu ouvert, mais propriété privée dont le gérant peut interdire de filmer [Pratique, à faire trancher].
- **Jurisprudence : ne rien citer.** Le numéro 95-10.185 donné pour la première chambre civile du 20 février 2001 est contredit : une recherche de contrôle donne le pourvoi **n° 98-23.471** (Bull. 2001 I, n° 42), sur des images de personnes impliquées dans un événement et la dignité de la personne, non sur un cliché pris en lieu public [Extrait]. L'arrêt du 20 mai 2025 (chambre criminelle) n'est pas vérifié. **Ne citer aucune décision à Cabezer** ; dire « cadre général, à faire valider ».
- **Usage commercial.** Aucune source trouvée sur une personne reconnaissable dans une vidéo sponsorisée : repère de prudence à rappeler à Cabezer : accord écrit quand la vidéo est commerciale [Pratique, lacune].
- **RGPD.** Une image identifiable est une donnée personnelle. Pour les photos, la FAQ de la CNIL indique qu'un particulier ne publie pas la photo d'un véhicule sans flouter la plaque (identification indirecte du propriétaire), avec des exceptions [Extrait : texte non ouvert ; aucune position trouvée pour la vidéo]. L'exception journalistique (article 85 du RGPD) n'a pas été étudiée : **ne pas s'en prévaloir**.
- **Critique nommée d'un restaurant.** Dénigrement et diffamation n'ont pas été recherchés : aucun jugement factuel non vérifié (skill §8) ; en cas de doute, signaler.

**Quand** : au brief, poser la question « personnes filmées ? accord obtenu ? » ; au dérush, lister ; avant l'export, vérifier que la décision de Cabezer est appliquée.
**Signaler à Cabezer** : toute personne reconnaissable (accord connu ou non), tout enfant en priorité, tout ticket ou écran lisible, avec le moment (timecode) ; Claude peut proposer un flou, un recadrage ou une coupe, **Cabezer décide**.

### 2.2 Qui apparaît, et que faire (Claude signale, Cabezer décide)

| Cas | Au dérush | Statut |
|---|---|---|
| Client isolé, reconnaissable (visage net, tatouage, vêtement distinctif) | Signaler ; proposer flou du visage, recadrage ou plan de dos ; pas de flou sans la décision de Cabezer | [Pratique] |
| Groupe sans visage reconnaissable, ou personne dont Cabezer a noté l'accord (§2.5) | Rien à signaler de plus ; pas de flou | [Pratique] |
| Serveur, cuisinier, gérant, chef | Signaler ; repère : l'accord du gérant ne suffit pas pour un salarié ; flou du visage et du badge seulement si Cabezer le décide | [Pratique] (blogs) |
| Enfant identifiable | Signaler en priorité, avec tout prénom prononcé ou sous-titré ; Cabezer décide (flou, exclusion, accord des parents) | [Pratique] + [Extrait] |
| Plaque d'immatriculation | Signaler ; si Cabezer la désigne, flou fort (bloc opaque ou mosaïque) | [Extrait] |
| Ticket de caisse, écran de caisse, réservation, note | Signaler ; proposition : garder le total et les lignes de prix, masquer numéro de carte, nom, numéro de client, adresse, si Cabezer le décide | [Pratique] |
| Capture d'écran (T, S) | Signaler onglets, e-mails, notifications, jetons ; masquage selon la décision de Cabezer | [Pratique] (`styles-food-et-tech.md`) |
| Reflet (miroir, vitre, écran) | Signaler comme une personne | [Pratique] |
| Enseigne, logo, menu affiché | Pas de flou par défaut ; le plan de stock de D exclut logo et lieu (décision D.13) | [Pratique] |
| Voix ou nom prononcé d'un tiers identifiable | Signaler ; Cabezer décide de la coupe (le flou ne suffit pas si le nom est dit ou sous-titré) | [Pratique] |

### 2.3 Mineurs

- **Article 372-1 du Code civil** (loi n° 2024-120 du 19 février 2024) : les parents protègent en commun le droit à l'image de leur enfant mineur, en l'associant selon son âge et sa maturité ; acte non usuel, donc accord des deux parents [Extrait : commentaires ; texte consolidé non lu].
- **Loi n° 2020-1266 du 19 octobre 2020** : exploitation commerciale de l'image d'enfants de moins de 16 ans ; vise surtout les comptes qui monétisent leurs propres enfants [Extrait].
- **Application à Cabezer.** Un enfant client ou passant n'est pas un enfant de la famille de Cabezer : le mineur est signalé en priorité au dérush et Cabezer décide ; repère légal : accord écrit des titulaires de l'autorité parentale pour toute publication identifiante.

### 2.4 Exécuter le floutage dans Premiere et AE (gratuit, sans IA générative)

**Principe** (pour ce que Cabezer a désigné). Un masque suivi qui porte une mosaïque ou un flou fort, vérifié image par image à 100 %, puis sur le MP4 exporté. **Jamais** de service de floutage en ligne (les rushs sortent de la machine) ni de remplissage génératif (décision B.2). Roto Brush ne sert qu'en dernier recours si le suivi décroche, résultat vérifié ; **Object Matte et Object Mask sont exclus** (réponse de Cabezer) : masques manuels et suivi.

**Quand** : **après la validation du dérush** (coupes fixées), **avant la colorimétrie et l'habillage** ; revérifier après toute retouche de Cabezer et après les punch-ins.

**Procédure Premiere (sur le plan à flouter)** : libellés anglais, français entre parenthèses ; non confirmés sur la machine de Cabezer.
1. Au dérush, poser un marqueur nommé « FLOU » (Marker) sur chaque plan concerné.
2. Ouvrir Effect Controls (Contrôles d'effets) et appliquer Mosaic (Mosaïque) ou Gaussian Blur (Flou gaussien) (libellés à confirmer ; catégories Stylize et Blur & Sharpen selon des tutoriels [Extrait]).
3. Créer un masque ellipse (Create ellipse mask, libellé à confirmer) autour du visage, marge de 20 à 30 % [valeur non sourcée], contour progressif (Mask Feather) de 10 à 30 px [valeur non sourcée] ; plus petit pour une plaque.
4. Track selected mask forward (Suivre le masque sélectionné vers l'avant, libellé à confirmer) ; attendre la fin de l'analyse avant tout autre geste (`pilotage-environnement-reprise.md`).
5. **Mosaïque de préférence** à un flou léger : le visage tient en 4 à 6 blocs de large [valeur de départ à tester].
6. Parcourir le plan image par image, surtout quand la tête tourne ou se cache : images clés manuelles au besoin.
7. Exporter 10 secondes et relire avant de traiter tout le montage. Vérifier qu'un punch-in (Motion, Mouvement) ou un second clip garde le flou : l'ordre d'application des effets est à confirmer sur la version installée.

**Alternative dans AE** : calque de forme ou masque, suivi de masque (Mask Tracking, libellé à confirmer), Mosaic ou Gaussian Blur, le tout **précomposé** pour rester modifiable et nommé « FLOU_<plan> » (skill §16, calques natifs). Le plan flouté est ensuite rendu ou lié par Dynamic Link (`after-effects-motion-design.md`).

**Critère de réussite (Claude peut le contrôler).** Extraire l'image du pire moment à 100 % et à 270 × 480 (taille d'un téléphone réduit) : yeux, nez, bouche, tatouage, coiffure et plaque ne sont plus distinguables. Si un doute subsiste, durcir.

**Pièges.** Flou léger : silhouette reconnaissable ; masque qui décroche : visage nu quelques images ; badge nominatif, nom sous-titré et reflets non floutés ; effet désactivé à l'export : vérifier **sur le MP4**.

### 2.5 Où consigner les accords et les masquages

Les décisions de Cabezer sur les personnes, les accords écrits éventuels (nom, date, supports, durée, territoire) et la liste des masquages vont dans la section « Personnes et données » de `Suivi/decisions.md` (réponse de Cabezer ; aucun fichier dédié). Un accord précise les supports, la durée et le territoire ; pour une diffusion en ligne, viser le monde entier [Extrait]. Au rapport de contrôle : « masqué : ... ; reste à valider : ... ».

---

## 3. Contenu commercial : mention, invitations, contrat

### 3.1 Cadre et question au brief

**Pourquoi** : une vidéo où un plat est offert, où Cabezer est invité ou rémunéré est une promotion à signaler. L'absence de mention est une pratique commerciale trompeuse ; la DGCCRF a contrôlé plus de 300 influenceurs en 2022-2023 (près de la moitié en anomalie) et un créateur food a payé 3 500 € par transaction pénale en juin 2024 pour des publications sur des restaurants sans mention [Extrait : presse].

- **Loi n° 2023-451 du 9 juin 2023, article 5.** La promotion doit être indiquée par la mention « Publicité » ou « Collaboration commerciale » [Extrait ; texte non lu].
- **Ordonnance n° 2024-978 du 6 novembre 2024.** Elle admet une mention équivalente, claire et adaptée au format, et aurait supprimé l'exigence « pendant toute la promotion » au profit d'une mention compréhensible [Extrait : deux sources secondaires, texte non lu ; à vérifier].
- **ARPP** : identification instantanée, explicite et lisible ; une mention en fin de vidéo, noyée dans les dièses ou la description, ou ajoutée après coup est insuffisante ; taille, contraste et durée d'affichage suffisants (aucune durée chiffrée pour les formats courts) [Extrait : PDF non lus].
- **DGCCRF** : mention dès le début et en français [Extrait].
- **Contrat écrit** : décret n° 2025-1137 du 28 novembre 2025 (le 25 selon une source, sans doute erronée ; JORF non lu), en vigueur le 1er janvier 2026 : contrat écrit à partir de **1 000 € HT** de rémunérations et avantages en nature d'un même annonceur pour un même objectif promotionnel (une source ajoute « par année civile ») ; produits offerts, invitations et cartes cadeaux y compteraient [Extrait ; **à vérifier**]. Hors montage : Claude signale, Cabezer décide.

**Question au brief (skill §3 étape 0, champ « contraintes légales »)** : « Plat offert, invitation, partenariat, affiliation, produit reçu ? Annonceur ? » Réponse dans `Suivi/brief.md`. **Sans réponse en mode autonome**, ne pas supposer l'absence : consigner « en attente » et le dire à la livraison (décision D.16).

### 3.2 Qui choisit la mention, et quels repères donner

**Réponse de Cabezer (12/10/2026)** : repas offert, invitation, produit reçu ou partenariat sont **signalés au brief** ; la **formule et la durée** de la mention sont **choisies par Cabezer à chaque vidéo**. Claude ne l'impose pas et n'ajoute rien sans sa validation.

- **Ce que Claude fait.** Signaler la contrepartie au brief (annonceur, produit offert, invitation, rémunération, affiliation), puis demander à Cabezer la formule et la durée en lui donnant les repères ci-dessous. En cas de doute sur l'existence d'une contrepartie, poser la question : la DA v2 interdit un texte non demandé pour relancer l'image, mais **une mention légale n'est pas une relance**.
- **Repères de formule (information).** La loi cite « Collaboration commerciale » ou « Publicité » ; l'ordonnance de 2024 admet une mention équivalente, claire, en français. Usage courant : « Collaboration commerciale » pour un repas ou un produit offert, « Publicité » si une marque a payé la diffusion. Ce sont des suggestions, pas une règle du skill.
- **Repères de durée (information).** ARPP et DGCCRF visent une mention dès le début, lisible, jamais seulement en fin de vidéo ou dans la description ; la durée légale exacte n'est pas lue. Cabezer choisit (début seulement, ou toute la vidéo), et son choix est consigné dans `Suivi/decisions.md`.
- **Familles.** D (étiquette discrète persistante), F, S, T, P, H : même démarche. Pour un segment sponsorisé dans une vidéo longue, Claude propose de l'afficher dès le début du segment ; la durée reste celle que choisit Cabezer. Le segment est monté comme le reste, sans atténuer ni inventer l'avis de Cabezer.

### 3.3 Réalisation dans AE et Premiere

Une fois la formule et la durée choisies par Cabezer :

1. **Composition AE « MENTION-COMMERCIALE »**, texte éditable en calque natif, à l'identité de la famille (D : pastille blanche à coins arrondis, texte noir Avenir Next Bold, casse normale, comme l'étiquette de la DA v2 ; autres familles : style d'identité validé). Entrée animée de 4 à 8 images, sortie sèche, rendue en ProRes 4444 alpha (skill §5.1 : une composition éditable par élément). Aucune image générée.
2. **Placement 9:16** : dans la boîte de `formats-courts-verticaux.md §6.2` (hors des 270 px du haut, 670 px du bas, 132 px de droite), par exemple en haut à gauche sous la zone interdite. **Une mention masquée par l'interface de la plateforme n'est pas une mention** : tester sur le téléphone de Cabezer (même fiche, §6.3). En cas de conflit avec l'étiquette « lieu » du hook, la mention reste, l'autre élément se déplace (le dire à Cabezer).
3. **Taille et contraste.** Texte lisible sur l'image réduite à 270 × 480 (corps de départ 44 px sur 1080, valeur non sourcée) ; contraste ≥ 4,5:1 (§8.2). Pastille blanche + texte noir : 21:1.
4. **Sous-titres.** Pendant l'entrée animée de la mention, la règle du skill §9 s'applique (pas de sous-titre sous un texte animé). Ensuite la mention est statique et ne recouvre jamais un sous-titre : les deux n'occupent pas la même zone.
5. **Calage dans Premiere** sur une piste de titres dédiée, pour la durée choisie par Cabezer ; piste active à l'export.
6. **À la publication** (hors périmètre du montage) : Cabezer coche la case « promotion payante » ou « contenu de marque » de la plateforme, qui complète sans remplacer la mention à l'image [Extrait ARPP]. Le dire dans le message de livraison.

**Signaler à Cabezer** : un annonceur, un produit offert ou un montant cité dans le brief ; l'absence de réponse à la question du brief ; le seuil de 1 000 € HT s'il le dépasse ; la mention qui entre en conflit avec un autre élément ; la formule et la durée à choisir.

---

## 4. Extraits de films, séries et vidéos tierces

**Pourquoi** : P et S citent des extraits officiels ; le droit français n'a pas de « fair use ».

- **Courte citation (article L122-5, 3° a), Code de la propriété intellectuelle).** Analyses et courtes citations permises si elles sont justifiées par le caractère critique, polémique, pédagogique, scientifique ou d'information, avec **nom de l'auteur et source indiqués** [Extrait : résumé du Syndicat national de l'édition ; texte non lu].
- **Interprétation stricte.** Il n'existe pas de droit général à réutiliser quelques secondes ; la charge de la preuve pèse sur celui qui cite. Le tribunal judiciaire de Paris (4 mars 2022, n° 22/00034) a écarté l'exception pour des extraits servant d'illustration, même avec liens vers les chaînes d'origine [Extrait : note de jurisprudence]. Une source isolée dit que la jurisprudence limiterait la courte citation aux œuvres écrites [À vérifier] : dans le doute, **ne pas s'appuyer sur la citation pour un extrait audiovisuel** sans décision de Cabezer.
- **Content ID (YouTube)** : l'ayant droit choisit de bloquer la vidéo, de la monétiser ou de suivre ses statistiques ; en 2024, plus de 2 milliards de revendications, moins de 1 % contestées, plus de 70 % des contestations abouties parce que l'ayant droit a retiré la revendication ou n'a pas répondu en 30 jours [Lu : page YouTube « How YouTube's Copyright Protection Tools work »]. Une revendication est fréquente et surtout une question de monétisation ; elle ne prouve pas l'illégalité.

### 4.1 Procédure de départ (règle D.14 des `../decisions-harmonisation.md`)

1. **Besoin** : l'extrait est-il nécessaire à l'analyse ? Si Cabezer peut dire la phrase, ne pas citer l'extrait.
2. **Durée minimale nécessaire**, encadrée de commentaire avant et après. Aucune durée chiffrée n'est sourcée ; réponse de Cabezer : la durée utile à ce qu'il analyse.
3. **Source affichée** dans une composition AE « SOURCE » (titre, année, éditeur ou plateforme) ; durée d'au moins 3 s, soit max(3 s ; max(1,5 s ; 1 s + caractères/15)) ; jamais en fin de vidéo seulement.
4. **Pas d'altération du sens** : ni ralenti, ni montage qui change le propos. L'exploration par caméra 3D ou la fenêtre de l'identité PRISME est un cadrage de présentation, permis sans déformation tant que le plan reste identifiable (réponse de Cabezer).
5. **Registre** `Suivi/licences.csv` : `type = extrait`, statut `citation (à valider)`, minute dans la source, durée utilisée, crédit à l'écran (`organisation-livraison-qc.md §2.2`).
6. **Un crédit n'est pas une autorisation.** Un extrait crédité peut quand même être bloqué ou revendiqué.
7. **Risque Content ID signalé à Cabezer avant publication**, avec la liste des extraits et leur durée ; Claude n'agit jamais dans YouTube Studio et ne contacte aucun ayant droit.
8. **Extraits fournis par un studio** (bandes-annonces, presse) : conditions non trouvées ; ne pas supposer l'autorisation.

**Quand l'utiliser** : P et S, parfois H ; **quand l'éviter** : D, F et T sauf extrait de produit officiel fourni par la marque ; jamais un extrait pour « habiller » un passage.

---

## 5. Musique, sons et registre des licences

- **Registre unique** : une ligne par piste, son, image, police dans `Suivi/licences.csv` (fichier, source, licence lue, URL, date, preuve, périmètre) ; « libre » seulement si la licence a été lue (`organisation-livraison-qc.md §2.2`). La banque Pixabay de la dégustation garde `LICENCES-SFX.md`.
- **Plans vidéo stock libres de droits** (Pexels, Pixabay) : accord général de Cabezer (réponse du 12/10/2026) ; téléchargés sans redemander, licence lue et consignée dans `licences.csv`, signalés (nom, source, taille). Cet accord ne vaut que pour les plans vidéo ; toute autre vidéo, image ou piste téléchargée attend son accord.
- **Musique** : aucune dans les courts ni en Lifestyle ; composition originale en Story, food long et tech (SKILL §11). **SFX** : tout son de la banque Pixabay est permis dans les courts (SKILL §5).
- **Pixabay** : usage commercial permis sans attribution, revente des fichiers bruts interdite ; une revendication Content ID reste possible, des contributeurs enregistrant leurs pistes [Extrait ; conditions officielles lues en partie]. Relire la page de licence à la date du téléchargement et en garder une capture.
- **YouTube Audio Library** : conditions propres à chaque piste [Extrait, non lu]. **Pistes achetées (Halal Beats)** : consigner la licence piste par piste. **Apple Loops** : jamais une boucle seule publiée (skill §11) ; consigner les boucles. **Musique originale** : réduit le risque de revendication sans l'annuler. **SACEM** : non étudiée [lacune] ; ne rien affirmer.
- **En cas de revendication** : ne rien supprimer, conserver les preuves de licence, laisser Cabezer contester.
- **Signaler** : toute piste sans preuve de licence, toute musique d'un tutoriel ou d'une vidéo (interdit), tout téléchargement qui attend l'accord de Cabezer.

---

## 6. Photosensibilité : flashs, secousses et coupes

> **Réponse de Cabezer (12/10/2026) : pas de test de photosensibilité.** Claude ne fait ni décompte de flashs ni `flash-check.py` de lui-même. Cette section est une **information facultative** (WCAG et mesures) : elle ne s'applique que si Cabezer demande un test, ou pour répondre à sa question. Rien ci-dessous ne bloque une livraison.

### 6.1 Le critère de référence (WCAG 2.3.1, lu)

**Pourquoi** : la DA v2 impose flash blanc, shake, scintillement et whips ; le hook agressif enchaîne des extraits rapides. Des alternances rapides de luminosité peuvent déclencher des crises chez des personnes photosensibles. Référence facultative : WCAG 2.3.1 (niveau A) « Three Flashes or Below Threshold », issu de la radiodiffusion [Lu : Understanding].

- **Flash général** : paire de changements opposés de luminance relative d'au moins **0,10** (sur 1,0) quand l'état le plus sombre est **sous 0,80**. « Opposés » : une montée suivie d'une descente, ou l'inverse [Lu : glossaire].
- **Seuil de passage** : au plus **3 flashs généraux et au plus 3 flashs rouges dans toute période d'une seconde**, **ou** surface cumulée des flashs simultanés d'au plus 0,006 stéradian, soit 25 % d'un champ de 10 degrés [Lu].
- **Exception** : motif fin et équilibré (bruit blanc, damier aux carrés de moins de 0,1 degré) [Lu].
- **Flash rouge saturé** : transition vers ou depuis un état dont R/(R+G+B) ≥ 0,8, avec un écart de chromaticité > 0,2 dans le diagramme CIE 1976 UCS [Lu].
- **Niveau AAA (2.3.2, « Three Flashes »)** : aucun flash de plus de 3 par seconde, **quelle que soit la taille ou la luminosité** [Lu : Understanding]. Les repères maison de §6.3 (aire non exemptée, au plus 2 par seconde) respectent aussi ce critère.
- **Portée.** WCAG vise le web ; les plateformes ne l'appliquent pas telle quelle. C'est un **repère de sécurité facultatif**, pas une obligation légale établie ni une règle du skill [Pratique].
- **Export SDR Rec.709** : la définition en luminance relative suffit. La formulation de l'UIT-R BT.1702 (20 cd/m² d'écart quand le côté sombre est sous 160 cd/m²) est citée par WCAG et n'a pas été lue directement [Lu par citation].

**Ce qui n'est pas un flash** : un fondu lent (une seule transition) ; un zoom, un whip, un shake ou une coupe entre plans de luminosité proche. Ces gestes en deviennent dès que des zones très claires et très sombres alternent (§6.3).

### 6.2 Surface : ne pas compter sur l'exception sur téléphone

Le champ de 10 degrés vaut 341 × 256 px CSS (87 296 px) ; un quart, **21 824 px CSS**, se mesure en pixels CSS même sur un petit écran [Lu : Understanding]. Sur un écran de 390 × 844 px CSS (hypothèse : téléphone courant) cela fait **environ 7 % de l'écran** (21 824 / 329 160 = 6,6 % ; calcul maison). L'exception ne vaut que pour une petite pastille ou de petites étincelles, **jamais pour un flash plein cadre**. Repère : tout flash couvrant plus de 7 % du cadre compte entièrement.

### 6.3 Repères chiffrés compatibles avec la DA v2 (à 29,97 images par seconde, facultatifs)

DA v2 (skill §5.1) : flash blanc 70 % → 0 en 4 images (0,133 s), shake de 6 images (0,2 s), whip de 4 à 6 images, scintillement. Le pop (0 → 118 → 96 → 100 %) et la glisse ne changent pas la luminance globale. **La DA ne fixe aucune fréquence** : le placement décide. Essais **[Mesuré]** sur clips synthétiques 180 × 320, 29,97 i/s, H.264 CRF 8, grille 18 × 32, flash mélangé en sRGB non linéaire : si le projet AE est en lumière linéaire (libellé à confirmer), la luminance d'un flash à 70 % diffère ; mesurer l'export.

| Élément | Comptage | Résultat mesuré | Respecte WCAG 2.3.1 ? | Repère maison facultatif (valeur de départ) |
|---|---|---|---|---|
| Flash blanc 70 → 0 en 4 images, seul | 1 flash par occurrence (montée puis descente) sur fond de luminance < 0,80 | 1 par seconde → 1 ; 2 par seconde → 2 ; 3 par seconde → 3 (limite) ; un toutes les 8 images (3,7 par seconde) → 4, **échec** ; pic 100 % au lieu de 70 % : même décompte | **Oui jusqu'à 3 par seconde ; non à 4** | Au plus **2 flashs par seconde** (marge d'une unité), soit **au moins 15 images (0,5 s)** entre deux flashs |
| Flash blanc sur fond déjà clair (luminance ≥ 0,80, soit environ 231/255 en sRGB) | Ne compte pas : l'état sombre dépasse 0,80 | Fond à 235 → 0 flash | Oui | Ne pas s'en servir comme excuse : un fond à 200 compte (luminance 0,58) |
| Shake de 6 images, seul | Ne change pas la luminance moyenne ; alterne localement aux arêtes contrastées | Pire cas sur 25 tirages, amplitude de 1 à 10 % de la largeur, arête blanc/noir franche : **2 à 3 flashs locaux** par secousse ; scène douce : 0 à 3 | **Oui, un shake seul** (au plus 3 locaux) ; ne laisse aucune marge pour un autre flash | Amplitude de départ 20 à 30 px sur 1080 (fiche AE), **plafond 43 px (4 % de la largeur)** ; **un shake par seconde au plus** |
| Gros moment = flash + shake simultanés (prix, intérieur, verdict) | Compter **3** (pire cas local) | Un par seconde → 3 (limite) ; deux par seconde → 5, **échec** | **Oui à un par seconde ; non à deux** | **Un gros moment par seconde au plus, et au moins 30 images (1 s) entre un gros moment et tout autre flash ou coupe très contrastée** |
| Coupes alternant plan sombre et plan clair (écart de luminance ≥ 0,10) | 2 coupes = 1 flash | Plans de 4 images → 4 par seconde (**échec**) ; 6 images → 3 (limite) ; 8 images → 2 ; 10 → 2 ; 15 → 1 | Oui à partir de 6 images | **Aucun plan de moins de 8 images (0,27 s)** entre deux plans d'écart de luminance ≥ 0,10 ; les coupes rapides du skill (0,4 à 0,8 s) sont compatibles |
| Whip entre deux lieux ; glitch graphique | Une transition ; 1 flash par aller-retour clair/sombre ≥ 0,10 | Non testés seuls | À mesurer sur le montage | Compter 1 flash par whip dont les deux plans diffèrent de ≥ 0,10 ; glitch : une alternance claire/sombre compte pour 1 |
| Scintillement (étincelles) | Chaque étincelle qui s'allume puis s'éteint = 1 flash local | Non mesuré (étincelles non fournies) | Oui par la voie de la surface si ≤ ~7 % du cadre au total | **Au plus 3 pulsations par seconde par étincelle, aire cumulée des étincelles simultanées sous 7 % du cadre** ; au-delà, compter comme un flash plein cadre |
| Rouge de l'identité (#E63946, #CE2B37, #B8323A) | R/(R+G+B) vaut 0,64 en valeurs sRGB brutes, mais 0,87 à 0,91 en valeurs linéarisées : la définition WCAG est ambiguë | Flash rouge non calculé | **À vérifier** | **Pas de clignotement du cadre entier en rouge ou en vert/rouge** ; mêmes limites de fréquence |

**Information pour Cabezer, si elle est demandée** : la DA v2 telle que spécifiée (flash 70 % → 0 en 4 images, shake de 6 images) **respecte WCAG 2.3.1 prise isolément**, à condition que les occurrences soient espacées, ce que la DA ne fixe pas. Le risque est dans les enchaînements : hook agressif (coupes courtes entre plans contrastés, whip, flash), note et intérieur rapprochés, shake répété. Les repères maison gardent une unité de marge sous 3 et sont compatibles avec 2.3.2.

**Pourquoi 2 et non 3.** Le seuil de 3 est une limite de passage, non une cible : le ré-encodage de la plateforme peut décaler les valeurs, l'outil ne calcule ni la surface ni le rouge.

### 6.4 Décompte pendant le montage (seulement si Cabezer demande un test)

1. Lister sur la timeline, **seconde par seconde** (fenêtre glissante), les événements lumineux : flash AE (1), flash de la note ou du prix (1), gros moment (3), paire de coupes très contrastées (1), whip entre plans contrastés (1), scintillement dense (1), glitch (1 par alternance), scintillement d'un rush.
2. Si une fenêtre d'une seconde cumule **plus de 2** (un gros moment isolé, compté 3, est admis seul dans sa seconde) : le signaler à Cabezer et proposer de retirer un flash, de décaler un effet de quelques images ou de rallonger un plan. Ne pas se contenter de baisser l'opacité d'un flash sans retester (70 % ou 100 %, le décompte est le même sur fond sombre : mesuré).
3. Hook agressif (`formats-courts-verticaux.md §1.7`) : compter dans les 3 premières secondes ; c'est là que l'accumulation est la plus probable.

### 6.5 Contrôle outillé sur l'export : `flash-check.py` (seulement sur demande)

Script lecture seule, **lancé uniquement si Cabezer demande un test de photosensibilité** (SKILL §3) ; fichier `references/pro/scripts/flash-check.py`. Il réduit la vidéo en grille, calcule la luminance relative WCAG de chaque zone image par image, et compte les paires de transitions (écart ≥ 0,10, côté sombre < 0,80) dans toute fenêtre d'une seconde. Appel :

```
python3 -I flash-check.py Exports/Brouillons/video.mp4 --grid 18x32 --max 3     # vertical 9:16
python3 -I flash-check.py Exports/Brouillons/video.mp4 --grid 32x18 --max 3     # horizontal 16:9
```

Sortie : une ligne JSON (`max_flashs_par_seconde`, zone, temps des flashs fautifs, verdict) ; code de sortie 1 en cas d'échec. Avec `--max 2`, un échec est un signal du repère maison ; l'échec WCAG est celui de `--max 3`.

**Validation [Mesuré].** 7 clips de la recherche (flash seul, flash local, variations sous 0,10, côté sombre au-dessus de 0,80) : résultats attendus pour les 7. 24 clips de cette passe : chiffres du tableau §6.3.

**Temps de calcul [Mesuré].** 8 s pour 60 s de vidéo 1080 × 1920 à 29,97 i/s sur 4 cœurs Linux ; extrapolation d'environ 2 min 40 s pour 20 minutes (estimation, temps sur le Mac non mesuré). Lancer sur l'export de contrôle, pas sur le master.

**Limites (à dire dans le rapport).**
- Le test compte **chaque zone séparément** (une zone = 1/576 du cadre) : il est conservateur sur les flashs locaux et peut signaler des détails sans danger ; une alerte est un cas à **examiner**, pas un verdict. Sur un motif chargé (mire `testsrc2` de 60 s), il a donné exactement 3 par seconde sans que le motif soit un flash.
- La surface (7 %) et le **flash rouge saturé** ne sont **pas calculés**.
- Aucun rush réel testé ; clips synthétiques ; cadence supposée constante.
- Tester **l'export encodé** : étalonnage et compression décalent les valeurs.
- Pas d'outil de référence essayé (la page WCAG cite PEAT et Harding FPA).

### 6.6 Procédure si Cabezer demande un test

1. Exporter la version de contrôle (même réglage que le final, `organisation-livraison-qc.md §8.5`).
2. Lancer `flash-check.py` (`--max 3`, puis `--max 2`).
3. En cas d'alerte, lire les temps fautifs, ouvrir la timeline à ces secondes et traiter selon §6.4 (retirer, décaler, rallonger).
4. Consigner dans `Controles/` : verdict, version, date, limites. En cas d'échec à 3, le dire à Cabezer avec les temps fautifs ; il décide, le test ne bloque pas la livraison.
5. Dire à Cabezer : « mesuré, pas vu » ; la validation sur son écran reste la sienne.

### 6.7 Rushs à surveiller au dérush

Plans sous néon ou LED (scintillement, bandes) : signaler à Cabezer après repérage sur une planche d'images consécutives ou par la luminance moyenne image par image (`organisation-livraison-qc.md §6.3`, signalstats) ; aucun correctif natif fiable n'est établi : proposer un autre plan.

---

## 7. Typographie française à l'écran

**Pourquoi** : sous-titres, cartons, prix et étiquettes sont en français et souvent en capitales Avenir Next Heavy. Une espace mal placée ou une apostrophe droite se voit.

**Principe de hiérarchie** : l'**usage propre de Cabezer prime** (étiquette de Milan « 19h30 · Luini ferme à 20h »), à condition de rester **cohérent dans une même vidéo**. Les règles ci-dessous valent quand son usage n'est pas connu. **Réponse de Cabezer : « 19h30 » et « 12,50 € »** pour les heures et les prix.

### 7.1 Règles et statut

| Règle | Détail | Statut |
|---|---|---|
| Avant `?` `!` `;` | Espace fine insécable U+202F (U+00A0 tolérée) | [Lu] LanguageTool, règle FRENCH_WHITESPACE |
| Avant `:` | Espace insécable U+00A0, sauf heure (23:20) et adresse web | [Lu] LanguageTool |
| Guillemets | « » (U+00AB, U+00BB), espace insécable U+00A0 à l'intérieur | [Lu] CLDR (guillemets) + LanguageTool (espaces) |
| Avant `€` et `%` | Espace insécable U+00A0 : « 12,50 € », « 50 % » | [Lu] CLDR fr (motifs `#,##0.00 ¤` et `#,##0 %`) |
| Décimale | Virgule : « 12,50 € » | [Lu] CLDR fr |
| Milliers | Espace fine insécable U+202F : « 1 200 » ; CLDR groupe dès 4 chiffres (minimumGroupingDigits hérité = 1) ; une année ne se sépare pas (« 2026 ») | [Lu] CLDR ; année : usage |
| Heures | Le format système français est `HH:mm` ; « 19h30 » et « 19 h 30 » sont des conventions de typographie, **non vérifiées** ; **réponse de Cabezer : « 19h30 »** | [Lu] CLDR (format) ; convention [À vérifier] |
| Points de suspension | Caractère unique « … » (CLDR : motifs d'ellipse avec le caractère, espace après) | [Lu] CLDR (motifs) ; usage |
| Apostrophe | Courbe ’ plutôt que droite ' | [Pratique] |
| Ligature œ | « œuf, bœuf, cœur, sœur, nœud, vœu, œil, œuvre, chœur, mœurs » ; la transcription écrit souvent « oe » ; ne pas toucher « moelleux » | Orthographe usuelle [À vérifier : source primaire non lue] |
| Capitales accentuées | « ÉCLAIR », « À EMPORTER », « DÉGUSTATION » : l'accent reste sur la capitale | Usage [À vérifier : source primaire non lue] |

**Imprimerie nationale** : non lue ; des guides secondaires sont cohérents avec LanguageTool [Extrait]. « 19 h 30 », les majuscules accentuées et la ligature œ restent **à vérifier**. La recherche présentait « 19 h 30 » comme convention de la maison ; ni `../decisions-harmonisation.md` ni le skill (« 19h30 ») ne le disent : **la réponse de Cabezer s'applique, « 19h30 » et « 12,50 € »**.

### 7.2 Mettre en œuvre dans AE et Premiere

- **Police.** Les caractères U+202F et U+00A0 doivent exister dans la police d'identité (Avenir Next Heavy et Bold, Hoefler Text, Futura, PT Mono). Test : écrire dans un calque de texte « Quoi[U+202F]? Oui[U+00A0]: 12[U+202F]000[U+00A0]€ » à 400 %, chercher un carré, un trou ou une espace trop large (police de remplacement), consigner dans `Suivi/environnement-verifie.md`. Glyphes présents non vérifiés sur la machine de Cabezer.
- **Code.** Dans un script AE (ExtendScript) : `String.fromCharCode(0x202F)` et `String.fromCharCode(0x00A0)` [Pratique, non exécuté dans AE]. Le compteur de `styles-food-et-tech.md` suit déjà cette règle pour `€`.
- **Capitales.** Attribut All Caps (Toutes les capitales, libellé à confirmer) ou `toUpperCase()` d'un script : vérifier « é », « à », « œ » dans AE.
- **SRT.** UTF-8 **sans BOM**, espaces insécables intactes ; relire avec le lint.
- **Courts, mot à mot.** Seules la casse, les accents, la ligature œ et l'orthographe s'appliquent.

### 7.3 Contrôle outillé : `lint-fr.py`

Script lecture seule (`references/pro/scripts/lint-fr.py`) ; il **complète** `lint-srt.py` (qui détecte déjà l'espace simple avant `; : ! ? € %` et l'apostrophe droite) : absence d'espace, U+00A0 contre U+202F, guillemets, décimale à point, milliers, trois points, liste fermée de mots en « oe », liste fermée de capitales sans accent. À fusionner dans `lint-srt.py` si Cabezer valide les règles.

```
python3 -I lint-fr.py "Prix: 12.50€" "un oeuf"
python3 -I lint-fr.py -f sous_titres.srt
```

**Essai [Mesuré]** : 20 chaînes (fautives et correctes) ; les cas fautifs sont signalés (espace normale avant `?`, deux-points collé, « 12.50€ », guillemets sans insécable, « 1200 », « oeuf », apostrophe droite, « … » en trois points, « ECLAIR A EMPORTER ») ; les cas corrects passent, y compris « 23:20 », une adresse web, une année et « moelleux ». **Limites** : pas de contrôle des heures, de la présence des glyphes, des noms propres, ni des majuscules accentuées hors liste ; les lignes de numérotation et d'horodatage du SRT sont à exclure (utiliser le texte seul si le lint les signale).

**Quand l'utiliser** : sur le SRT et sur le texte source de chaque composition AE de texte, avant l'export. **Quand l'éviter** : sur une langue étrangère (D à l'étranger en anglais, passages cités). **Familles** : D, F, S, P, T, H pour le texte français affiché ; en court mot à mot, uniquement casse, accents, œ.

### 7.4 Découpage et vitesse de lecture

Limites du skill (§9) : tous les courts en mot à mot, un mot en français, paquets de 1 à 3 mots et 18 caractères au plus en traduction, au rythme de la parole (plancher 0,25 s) ; format long incrusté (étranger, passages traduits) 2 lignes, 24 caractères par ligne en 9:16, 42 en 16:9. Elles sont **plus strictes** que le repère Netflix (42 caractères par ligne, 17 ou 20 caractères par seconde selon des sources secondaires contradictoires, guide non lu) [Extrait]. La formule du skill max(1,5 s ; 1 s + caractères/15) vaut environ 15 caractères par seconde : **la garder** ; elle ne s'applique ni au mot à mot des courts ni aux coupes rapides (décisions, section C).

---

## 8. Intervenants, cartouches et contraste

### 8.1 Identifier une personne qui parle

**Pourquoi** : en S, T, F et P, interviews, témoignages et experts apparaissent ; la voix ne dit ni le nom ni la fonction. WCAG 1.2.2 (sous-titres préenregistrés) demande que les sous-titres **identifient qui parle** et rendent les sons significatifs [Lu : Understanding Captions].

- **Règle de départ.** Un cartouche « Prénom Nom » sur la première ligne, « fonction ou rôle » sur la seconde (exemple « cheffe pâtissière »), à la **première apparition seulement**, jamais répété à chaque retour de la personne. Pour un particulier ou un employé, signaler à Cabezer l'absence d'accord connu de la personne (§2.2), qui décide ; l'orthographe est vérifiée sur la source primaire (skill §8).
- **Exception au skill, validée.** Le skill (§6, point 7) réserve titres et cartons aux concepts, dates et chapitres et refuse le texte qui double chaque nom. Cabezer a répondu le 12/10/2026 : identifier un intervenant (nom et fonction) à sa première apparition, une seule fois, **jamais dans les courts food** ; ce n'est pas un « doublon », la voix ne donne pas cette information.
- **Réalisation.** Composition AE « INTERVENANT » en calques natifs à l'identité de la famille (jamais un gabarit Premiere), entrée et sortie de 8 à 15 images (skill §6, point 9).
- **Durée.** Formule du skill : max(1,5 s ; 1 s + caractères/15). « Marie Dupont, cheffe pâtissière » (32 caractères) : 1 + 32/15 ≈ **3,1 s**.
- **Position.** Dans la boîte sûre 9:16 (§3.3), jamais sur le visage ni l'interface ; en 16:9, marges de la fiche d'identité.
- **Source qui parle en extrait ou archive** : crédit court pendant l'extrait (`documentaire-essai-video-archives.md §11`).
- **Voix off** : « Voix off » dans le SRT quand le locuteur ne se voit pas.

**Quand l'utiliser** : S, T, F, P avec intervenants (longs et courts hors food) ; **quand l'éviter** : courts food (D), Cabezer seul, plan sans intervenant, plan déjà identifié.

### 8.2 Contraste du texte (WCAG 1.4.3, lu)

- **Seuils** : **4,5:1** pour le texte normal, **3:1** pour le grand texte (18 points ou 14 points gras) ; valeurs limites **sans arrondi** (4,499:1 ne passe pas) [Lu].
- **Formule** : (L_clair + 0,05) / (L_sombre + 0,05), L étant la luminance relative [Lu].
- **Application à la vidéo** : transposition de référence, non obligation. Le texte d'habillage est du texte voulu (WCAG exclut le texte incidental d'une photographie).
- **Couleurs de l'identité, calculées avec cette formule [Mesuré]** :

| Texte sur fond | Rapport | Verdict |
|---|---|---|
| Noir sur blanc (étiquette, mention) | 21,0:1 | OK |
| Blanc sur rouge tomate #E63946 | 4,17:1 | OK grand texte seulement |
| Blanc sur rouge #CE2B37 (Italie) | 5,22:1 | OK |
| Blanc sur vert #009246 (Italie) | 4,04:1 | OK grand texte seulement |
| Rouge tomate #E63946 sur noir | 5,04:1 | OK |
| Encre #2B1B18 sur rose #F2C6C2 (Story) | 10,71:1 | OK |
| Rouge tampon #B8323A sur crème #FFF6EC (Story) | 5,53:1 | OK |

- **Texte gras en capitales (D).** Les sous-titres Avenir Next Heavy à environ 70 px sur 1080 de large font environ 25 px CSS sur un écran de 390 px de large, soit environ 19 points : on peut les traiter en **grand texte (3:1)** [lecture maison, à valider]. Les mots clés en rouge d'accent sur une vidéo claire passent mal : tester sur le fond le plus clair.
- **Fond variable** : mesurer sur le pire fond ; sinon fond de bloc d'opacité 70 à 85 % [valeur de départ non sourcée] ou ombre courte et nette de la DA v2, puis revérifier (le calcul WCAG porte sur le fond).

### 8.3 Contrôle outillé : `contraste-zone.py`

Mesure le contraste entre la couleur du texte et le pire fond d'une zone (percentile 95 de la luminance pour un texte clair, 5 pour un texte sombre) sur une image d'un MP4 **sans la piste de texte** :

```
python3 -I contraste-zone.py export_sans_texte.mp4 12.4 80 1382 920 120 FFFFFF
```

Arguments : temps en secondes, x, y, largeur, hauteur de la zone, couleur du texte en hexadécimal. Sortie JSON (`contraste`, `verdict`) ; code de sortie 1 sous 3:1. **Essai [Mesuré]** sur des fonds synthétiques : gris 100 avec texte blanc → 5,92:1 (calcul manuel identique) ; fond à 235 avec texte blanc → 1,19:1, échec ; avec texte sombre #2B1B18 → 13,84:1. **Limite** : il faut une image sans texte ; une seule image ne couvre pas un plan qui bouge (en prendre plusieurs).

**Quand l'utiliser** : mots clés en couleur d'accent, cartouches, mention commerciale, pop-ups sur fond clair. **Quand l'éviter** : sous-titres blancs sur fond sombre contrôlé.

---

## 9. Sous-titres accessibles et SRT

- **Contenu identique** : en France, les vidéos longues n'ont **qu'un SRT, rien d'incrusté** (réponse de Cabezer) ; dans les courts (mot à mot) et à l'étranger, les sous-titres incrustés (composition AE, ProRes 4444 alpha) et le SRT livré portent le même texte et la même ponctuation, de sorte qu'une personne sourde ou malentendante reçoive la même information que l'écran (skill §9, voie unique).
- **Sons significatifs** : un bruitage qui remplace un nom ou un prix ne doit pas être la seule information ; l'écrit est toujours présent (prix, note, mot de l'appel au commentaire) [Pratique].
- **Audiodescription** : critère 1.2.5 (niveau AA) non étudié ; à signaler pour les formats longs, sans engagement.
- **Temps de lecture** : formule du skill (§7.4) pour le format long ; dans les courts en mot à mot, rythme de la parole.
- **Traduction automatique** : relue (décision B.2).
- **Vérification** : sur le MP4, jamais sur le SRT seul (`organisation-livraison-qc.md §6.4`).

---

## 10. Techniques : quand, quand éviter, quelles familles

| Technique | Quand l'utiliser | Quand l'éviter | Familles |
|---|---|---|---|
| Question « conformité » au brief | Toujours, avant le dérush | Jamais d'omission en mode autonome : consigner « en attente » | D, F, S, P, T, H |
| Mosaïque ou flou fort sur masque suivi (Premiere) | Un visage ou une plaque que Cabezer a désigné, sur plusieurs images | Plan de moins de 1 s où une coupe ou un recadrage suffit | D, F, S, P, T, H |
| Recadrage ou coupe plutôt que flou | Cabezer a désigné la personne, elle n'est pas le sujet et le cadre le permet | Plan à protéger (yeux, mains, produit) | D, F |
| Composition AE « MENTION-COMMERCIALE » | Partenariat, repas offert, invitation, rémunération, une fois la formule et la durée choisies par Cabezer | Aucune contrepartie ni invitation liée à la vidéo | D, F, S, P, T, H |
| Composition AE « SOURCE » (crédit d'extrait) | Tout extrait tiers cité | Image personnelle de Cabezer | P, S, H |
| Décompte de flashs (§6.4) | Seulement si Cabezer demande un test de photosensibilité | Par défaut : pas de test | D surtout ; F, S, T, P, H |
| `flash-check.py` | Seulement si Cabezer demande un test de photosensibilité, sur la version de contrôle | Par défaut ; jamais sur le master 4K | D, F, S, P, T, H |
| `lint-fr.py` | Tout texte français affiché | Texte étranger | D, F, S, P, T, H |
| `contraste-zone.py` | Texte coloré, texte sur fond clair | Texte blanc sur fond sombre contrôlé | D, F, S, P, T |
| Cartouche INTERVENANT | Intervenant nommé à la première apparition | Courts food, Cabezer seul, intervenant déjà identifié | S, T, F, P |

---

## 11. Erreurs de débutant → réflexes de pro

| Erreur de débutant | Réflexe de pro |
|---|---|
| Flouter au hasard, « à la fin » ou sans décision | Lister et signaler au dérush ; flouter ce que Cabezer désigne après validation du dérush, vérifier le MP4 à 100 % |
| Flou gaussien léger sur un visage | Mosaïque ou flou fort, test à 270 × 480 |
| Ajouter la mention en fin de vidéo ou dans la description, ou choisir à la place de Cabezer | Mention à l'image dont Cabezer a choisi la formule et la durée, lisible sur téléphone, dans la boîte sûre |
| « Libre de droits » sans licence lue | Une ligne par piste dans `licences.csv`, preuve capturée |
| Baisser l'opacité d'un flash pour le « rendre sûr » (si un test est demandé) | Espacer ou retirer, puis retester l'export |
| Se fier à l'exception de surface sur téléphone (si un test est demandé) | Environ 7 % du cadre : tout flash plus grand compte entièrement |
| Espace normale avant `?` ou `€` | U+202F avant `? ! ;`, U+00A0 avant `: € %` et dans les guillemets |
| « 12.50€ », « oeuf », « ECLAIR », apostrophe droite | « 12,50 € », « œuf », « ÉCLAIR », ’ |
| Déclarer « conforme » parce que le script passe | « Contrôlé automatiquement, limites dites ; validation de Cabezer en attente » |

---

## 12. Liste de contrôle « conformité » (à intégrer au contrôle avant livraison, skill §14 et `organisation-livraison-qc.md §10.2`)

**Brief et dérush**
- [ ] Question du brief posée et consignée : plat offert, invitation, partenariat, affiliation, annonceur ; ou « en attente ».
- [ ] Personnes, enfants, plaques, tickets, écrans, reflets et voix de tiers listés au dérush et signalés à Cabezer ; ses décisions notées dans `decisions.md`.

**Personnes et données (§2)**
- [ ] Chaque personne reconnaissable, plaque, ticket ou écran signalé a reçu une décision de Cabezer (flou, recadrage, coupe ou rien), notée dans `decisions.md` ; les mineurs ont été signalés en priorité.
- [ ] Les floutages décidés par Cabezer sont vérifiés image par image à 100 % puis sur le MP4, y compris après les punch-ins et les retouches ; masquages notés au rapport.

**Contenu commercial (§3)**
- [ ] Si contrepartie : signalée au brief ; mention dont Cabezer a choisi la formule et la durée, posée à l'image, lisible à 270 × 480, dans la boîte sûre, jamais masquée par un sous-titre ; case plateforme rappelée à Cabezer.
- [ ] Seuil de 1 000 € HT signalé si Cabezer cite un montant ou un avantage.

**Extraits et licences (§4, §5)**
- [ ] Extraits : durée utile, commentés, source affichée au moins 3 s, ligne dans `licences.csv` (`citation (à valider)`), risque Content ID signalé.
- [ ] Chaque piste, son, image, police : ligne dans `licences.csv` avec preuve ; aucun fichier téléchargé sans accord, sauf les plans vidéo stock libres de droits (accord général, signalés).

**Photosensibilité (§6) : seulement si Cabezer demande un test**
- [ ] Par défaut, rien à cocher. Sur demande : décompte par seconde fait, `flash-check.py` lancé sur l'export de contrôle (grille adaptée au ratio), verdict et limites au rapport ; un échec à 3 est signalé à Cabezer, qui décide.

**Typographie, intervenants, contraste (§7, §8)**
- [ ] `lint-fr.py` et `lint-srt.py` sans ligne à corriger ; glyphes des espaces insécables présents ; heures et prix écrits « 19h30 » et « 12,50 € », de façon cohérente.
- [ ] Cartouches d'intervenants (hors courts food) : première apparition seulement, orthographe vérifiée à la source, durée selon la formule, hors visage et interface.
- [ ] Contraste ≥ 4,5:1 (3:1 grand texte) pour le texte coloré et les cartouches, mesuré sur le fond le plus clair.

**Rapport**
- [ ] « Contrôlé automatiquement / examiné à l'image / validé par Cabezer » distingués ; contrôles non faits écrits ; aucun conseil juridique présenté comme définitif.

---

## 13. Décisions à demander

> **Toutes ces questions ont reçu une réponse de Cabezer le 12/10/2026** : voir `../decisions-en-attente.md`, qui prime sur le reste de cette fiche.

Les réponses sont consignées dans `Suivi/decisions.md` et ne se redemandent pas, sauf la mention commerciale, que Cabezer choisit à chaque vidéo.

| N° | Question | Réponse de Cabezer |
|---|---|---|
| Q1 | Personnes reconnaissables : accord écrit systématique ou flou par défaut ? | Claude signale au dérush, Cabezer décide du floutage |
| Q2 | Employés de l'établissement : accord écrit ou flou ? | Même règle : Claude signale, Cabezer décide |
| Q3 | Mineurs identifiables | Même règle, mineurs signalés en priorité |
| Q4 | Mention commerciale : formule et durée | Formule et durée choisies par Cabezer à chaque vidéo |
| Q5 | Repas offerts, invitations, produits reçus : traités comme collaboration commerciale ? | Signalés au brief ; mention choisie par Cabezer à chaque fois, rien ajouté sans sa validation |
| Q6 | Suivi du seuil de contrat (1 000 € HT) | Pas de réponse particulière : Claude signale quand un montant ou un avantage est cité et ne tient aucun registre |
| Q7 | Test de flash avant export | Non : pas de test de photosensibilité ; `flash-check.py` seulement à sa demande |
| Q8 | Durée d'un extrait tiers et source affichée | Durée utile ; source au moins 3 s ; Content ID signalé |
| Q9 | Critique nommée d'un établissement | Pas de réponse particulière : aucun jugement factuel non vérifié (SKILL §8) |
| Q10 | Écriture des heures et des prix | « 19h30 » et « 12,50 € » |
| Q11 | Limites maison de photosensibilité | Sans objet sans test : simples repères facultatifs (§6.3) |
| Q12 | Exception d'identification d'un intervenant au point 7 du skill §6 | Oui : nom et fonction à la première apparition, hors courts food |
| Q13 | Nom d'un particulier ou d'un employé à l'écran | Couvert par Q12 : Claude signale l'absence d'accord connu, Cabezer décide |
| Q14 | Où consigner accords et masquages | Section « Personnes et données » de `Suivi/decisions.md` |
| Q15 | Exploration en caméra 3D d'un extrait officiel | Permise, sans déformation ni changement de sens |
| Q16 | Déclaration SACEM / licence de diffusion des musiques | Pas de réponse particulière : aucune action ; signaler que la SACEM n'a pas été étudiée |

---

## 14. Sources étudiées

Aucune vidéo YouTube téléchargée. Les « résultats de recherche » n'ont pas été ouverts (récupération impossible) : seul l'extrait renvoyé a servi.

**Textes lus**
1. **W3C**, WCAG 2 (dépôt officiel) : glossaire « flash », « general flash and red flash thresholds », « blinking », « relative luminance », « large scale » — https://github.com/w3c/wcag (`guidelines/terms/20/`) — lus en entier.
2. **W3C**, « Understanding Three Flashes or Below Threshold » (2.3.1) — `understanding/20/three-flashes-or-below-threshold.html` — lu en entier : seuils, 341 × 256 px, BT.1702 (cité), formules de chromaticité.
3. **W3C**, « Understanding Three Flashes » (2.3.2, AAA) — `understanding/20/three-flashes.html` — lu : aucun flash de plus de 3 par seconde, toute taille.
4. **W3C**, « Understanding Contrast (Minimum) » et « Understanding Captions (Prerecorded) » — `understanding/20/` — lus sur les seuils, l'absence d'arrondi, le texte incidental, l'identification des locuteurs. `guidelines/index.html` : lu partiellement (textes des critères 2.3.x absents du clone).
5. **Unicode**, CLDR `fr.xml` et `root.xml` — https://github.com/unicode-org/cldr — lus : décimale, groupe U+202F, motifs monnaie et pourcentage avec U+00A0, guillemets, ellipse, heure `HH:mm`, minimumGroupingDigits.
6. **LanguageTool**, `QuestionWhitespaceRule.java` (module fr) — https://github.com/languagetool-org/languagetool — lu : U+202F avant `? ! ;`, U+00A0 avant `:` et dans les guillemets.
7. **YouTube**, « How YouTube's Copyright Protection Tools work » — https://www.youtube.com/howyoutubeworks/copyright/ — lue : Content ID (bloquer, monétiser, suivre), chiffres 2024, délai de 30 jours.

**Essais exécutés le 12/10/2026** (ffmpeg 6.1.1, Python 3, numpy, conteneur Linux)
8. `flash-check.py` : 7 clips de la recherche, 24 clips synthétiques, un fichier de 60 s en 1080 × 1920, simulation de shake (25 tirages × 7 amplitudes × 2 types × 2 scènes). `lint-fr.py` : 20 chaînes. `contraste-zone.py` : 3 cas. Calculs de contraste et de luminance des couleurs d'identité.

**Résultats de recherche (texte officiel non lu)**
9. Loi n° 2023-451 (art. 5) et ordonnance n° 2024-978 — Lettre des réseaux https://www.lettredesreseaux.com/influence-commerciale-assouplissement-des-obligations-dinformation-reposant-sur-linfluenceur.html ; Dalloz Actualité https://www.dalloz-actualite.fr/document/ord-n-2024-978-6-nov-2024-jo-7-nov — mention équivalente, exigence « pendant toute la promotion » supprimée.
10. Décret n° 2025-1137 — Blog du Modérateur https://www.blogdumoderateur.com/partenariats-marques-influenceurs-nouvelles-regles-2026/ ; Le Petit Digital https://www.leptidigital.fr/entreprises/createurs-ugc-decret-janvier-oblige-annonceurs-recalculer-91532/ — seuil 1 000 € HT, 1er janvier 2026, date du 28 novembre (une source dit le 25).
11. DGCCRF — bilan 2022-2023 https://www.economie.gouv.fr/node/3227628 ; sanction d'un créateur food, Journal du Geek https://www.journaldugeek.com/2024/06/21/pour-la-premiere-fois-un-influenceur-food-sanctionne-par-la-dgccrf-pourquoi-cest-important/. ARPP (fiche influenceurs 2024, « Mentions et renvois ») : arpp.org inaccessible, extraits de la recherche précédente.
12. Cass. 1re civ., 20 février 2001, pourvoi n° 98-23.471 — https://www.revuegeneraledudroit.eu/blog/decisions/cass-civ-1re-20-fevrier-2001-n-98-23-471 ; loi n° 2024-120, art. 372-1 — https://www.actu-juridique.fr/civil/personnes-famille/le-respect-du-droit-a-limage-des-enfants-et-les-5-apports-de-la-loi-du-19-fevrier-2024/ ; CNIL, plaques — https://www.cnil.fr/fr/cnil-direct/question/1816 (photos, non vidéo).
13. CPI L122-5 3° a) (résumé SNE, https://www.sne.fr/droit-dauteur/les-exceptions-au-droit-dauteur-1-2/) ; TJ Paris, 4 mars 2022, n° 22/00034 (iredic.fr) — extraits de la recherche précédente. Netflix (guide français), Imprimerie nationale, Pixabay, YouTube Audio Library, Code civil art. 9, Code pénal art. 226-1, loi n° 2020-1266 : synthèses secondaires seulement.
14. Références internes lues : `SKILL.md` (§5.1, §6, §7, §9, §11), `../decisions-harmonisation.md`, `organisation-livraison-qc.md`, `formats-courts-verticaux.md`, `after-effects-motion-design.md`.

**Non couvert** : textes de loi et de décret, jurisprudence sur l'usage commercial d'une image prise en public, position de la CNIL pour la vidéo, durée d'affichage de la mention, traitement officiel des invitations, SACEM, guide Netflix, Imprimerie nationale, BT.1702 lue directement, flash rouge calculé, rush réel, libellés et glyphes sur la machine de Cabezer.
