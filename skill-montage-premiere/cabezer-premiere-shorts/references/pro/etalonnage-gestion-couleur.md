# Étalonnage et gestion des couleurs pro (Lumetri et théorie)

> **Réponses de Cabezer du 12/10/2026 — elles priment sur cette fiche**, en particulier sur sa section « Décisions à demander ». **Format d'abord, famille ensuite (SKILL §2)** : long (L-Food, L-Story, L-Tech, L-Films, L-Life) ou court (C-Food, C-Story, C-Tech, C-Films, C-Life) ; codes de cette fiche : D = C-Food, F = L-Food, S = L-Story, P = L-Films, T = L-Tech ; nouvelle famille Lifestyle (vlogs, face caméra : aucune musique, SFX comme la dégustation). **Tous les courts** : hook demandé, sous-titres mot à mot, aucune musique, SFX comme la dégustation, punch-ins secs, appel au commentaire, notation sur 10, identité propre au court. **Longs** : SRT seul en France ; composition musicale en Story, food et tech ; respirations d'émotion gardées en films/séries et au verdict du food long ; 4K si rushs 4K. Aussi : identité Story v15 et générique « Amed Story 🧢 » supprimés ; jamais de foley d'aliment ; ambiance en dégustation proposée au premier usage ; un rendu de sous-titres par passage ; intervenants identifiés à la première apparition (hors courts food) ; au plus deux passes de retravail sous 8 ; Tesseract, Higgsfield et SCANDALE FOOD retirés. **Réponses techniques (série 3)** : interface de Premiere et d'AE en anglais ; scripts AE et Terminal autorisés ; stock libre de droits sans redemander ; tout SFX de la banque Pixabay permis ; arrêt sur image permis partout ; pas de test de photosensibilité ; audio YouTube 384 kbit/s ; proxys toujours en long ; Frame.io pour les relectures ; WhisperX à installer ; « 19h30 » et « 12,50 € » ; Liquid Glass à recréer. Liste complète : `../decisions-en-attente.md`.

Fiche de référence pour étalonner comme un coloriste dans Premiere Pro, sous les règles de Cabezer. Rédigée le 12/10/2026, harmonisée en passe 2 le même jour. Le skill (§10) fixe les règles de la passe couleur ; cette fiche en donne la théorie, les procédures et les contrôles. Famille de fiches : `references/pro/`. Renvois entre fiches : nom de fichier + section.

## Quand lire cette fiche

Lire cette fiche avant toute passe colorimétrique (skill §3 : la couleur est une passe distincte), avant d'ouvrir le panneau Couleur Lumetri, avant de choisir un LUT, quand deux caméras se côtoient dans une séquence, quand un clip d'iPhone (HLG ou Apple Log) entre dans le projet, quand une image paraît délavée, trop claire ou différente après l'export, et quand un graphisme After Effects doit s'accorder avec des plans étalonnés. Elle ne remplace ni le brief ni le skill (§1).

Familles : dégustation (D), food long (F), Story (S), films/séries PRISME (P), tech (T), hors familles (H).

## Sommaire

1. Principes
2. Avant de toucher à une image
3. Gestion des couleurs dans Premiere (dont la chaîne par caméra)
4. Gamma d'affichage et écran de contrôle
5. Ordre des opérations
6. Lecture des scopes
7. Exposition, contraste, balance, saturation
8. Look et LUT créatives
9. Correspondance de plans et multicaméra
10. Peau
11. Food
12. iPhone, HLG, Apple Log et HDR
13. After Effects et couleur
14. Export, balises et contrôle du fichier
15. Contrôle sur téléphone
16. Erreurs de débutant → réflexes de pro
17. Liste de contrôle
18. Décisions à demander à Cabezer
19. Sources étudiées

**Niveaux de preuve utilisés dans la fiche**
- **[Tuto]** : transcription lue en entier ; valeur d'auteur, pas une règle. **[Tuto Adobe]** : tutoriel de Jason Druss, qui se présente comme membre de l'équipe Premiere ; ce n'est pas la documentation officielle.
- **[Doc lue]** : documentation ou code source lu en entier. **[Mesuré]** : commande exécutée sur un fichier de test synthétique (ffmpeg et ffprobe 6.1.1), jamais sur un rush de Cabezer.
- **[Métier]** : pratique standard, non recoupée en ligne. **[S]** : extrait de recherche, page non lue ; ne fonde jamais une règle seul. **[I]** : déduit par le rédacteur. **[À vérifier]** : à tester sur la version installée.

**Limites.** Aucune documentation Adobe n'a pu être lue : helpx.adobe.com, community.adobe.com, gamut.io, support.apple.com, colour-science.org, docsforadobe.dev et les sites de tutoriels sont refusés par le proxy. Tout chemin de menu est donc « à confirmer à l'écran ». Premiere et After Effects sont utilisés **en anglais** (réponse du 12/10/2026) : le libellé anglais affiché à l'écran fait foi, et les libellés français de cette fiche, suivis d'un astérisque (*) quand ils sont seulement probables, ne sont qu'un repère ; rien de ce qui dépend d'une bêta n'est écrit comme procédure.

---

## 1. Principes

**Pourquoi** : l'étalonnage a trois buts. Rendre tous les plans cohérents, rendre l'image lisible, donner une intention (appétence, ambiance). Les deux premiers se mesurent. Le troisième se juge.

1. **Une chaîne en trois temps : entrée, travail, sortie.** Caméra vers espace de travail, correction, espace de travail vers affichage. Quatre sources concordent [Tuto : Cullen Kelly 1:31 ; Mario So 2:31 ; Darren Mostyn « 5 PRO Fundamentals » 1:33 ; Tuto Adobe : Druss 16:25].
2. **Le technique avant le créatif.** Conversion, exposition, contraste et balance d'abord. Le look ensuite [Tuto : Cullen Kelly 8:08 ; Mostyn 8:10].
3. **Une seule conversion par clip.** Conversion automatique de Premiere, ou conversion du fabricant en LUT. Jamais les deux (skill §10) [Tuto : Mario So 6:38 ; Tuto Adobe : Druss 9:17].
4. **Les scopes mesurent, l'œil tranche.** Un scope ne remplit pas un cahier des charges créatif [Tuto : Mostyn scopes 13:41].
5. **Le contraste se voit plus que la balance** entre deux plans [Tuto : Mostyn 8:40]. **Caler la peau, ne jamais la keyer** [Tuto : Mostyn 13:13].
6. **Une technique de tutoriel n'est pas une règle.** Presque tous les coloristes lus travaillent sur DaVinci Resolve : leurs principes passent dans Premiere, leurs outils non. Chaque technique dit quand l'utiliser, quand l'éviter, pour quelles familles.
7. **Étalonner = passe distincte (skill §3, §10).** Consigner dans `Suivi/journal.md` la version de Premiere, le preset de couleur de la séquence, les LUT utilisés, les contrôles faits et les limites. Distinguer toujours **appliqué / contrôlé / validé par Cabezer** (skill §1) : une mesure n'est pas un jugement de Cabezer, un export lancé n'est pas un export validé.
8. **Gratuit par défaut.** Tout LUT du marché, plugin de pellicule ou outil de texture payant est signalé (nom, prix connu ou « à vérifier ») et attend l'accord de Cabezer (skill §17).

---

## 2. Avant de toucher à une image

1. **Lire la version de Premiere** dans l'application (menu de l'application > À propos) et la consigner dans `Suivi/environnement-verifie.md`. La version lue à l'écran fait foi. La table des versions connues, avec sa source, et le test de fumée des scripts vivent dans `pilotage-environnement-reprise.md` : ne pas citer ici de numéro de version comme certain. Les noms de menus bougent d'une version à l'autre.
2. **Repérer le panneau.** Ouvrir l'espace de travail Couleur (Color) : panneau Couleur Lumetri (Lumetri Color) et Scopes Lumetri* (Lumetri Scopes) [Tuto : Levine 3:33].
3. **Si l'écran montre un « mode Color » à la place de Lumetri : s'arrêter et demander.** Selon des extraits de recherche non lus [S], une bêta récente de Premiere ajouterait un mode Color qui remplace le panneau Lumetri ; ni l'aide ni la vidéo d'Adobe correspondantes n'ont été lues [À vérifier sur sa version]. Si ce mode est présent, ne pas appliquer les chemins de cette fiche : décrire à Cabezer ce qui est affiché et garder les étapes vérifiées (skill §3).
4. **Travailler sur une copie** (Enregistrer sous) quand on change un réglage de séquence ou de projet (skill §1). Juger dans le Moniteur Programme [`premiere-pro-avance.md`].
5. **Saisir les valeurs au clavier** (double-clic sur le nombre d'un curseur) et noter la valeur initiale avant un essai [Métier].
6. **Raccourcis.** Aucun n'est utilisé tant qu'il n'a pas été lu dans Premiere > Raccourcis clavier ; sinon passer par le menu. Ceux cités ci-dessous sont courants et marqués « à confirmer ».

---

## 3. Gestion des couleurs dans Premiere

### 3.1 Architecture

Selon Druss, le pipeline couleur de Premiere a été réécrit dans la série 25.2 [Tuto Adobe : 13:52] ; vérifier sur sa version. Trois étages :
- **Entrée** : l'espace du média. Premiere le lit dans les métadonnées du fichier (log, RAW, HLG) ou on le force.
- **Espace de travail** : défini par le « Color Setup » de la séquence.
- **Sortie** : Rec.709 par défaut.

**Les presets de séquence** [Tuto Adobe : Druss 12:51 à 14:23] : Direct Rec.709, Direct HLG, Direct PQ, Gamut large (trois variantes de mappage de tons), ou gestion des couleurs désactivée.
- **Direct Rec.709 (SDR)** est le défaut et se comporte comme l'ancien système. Les projets existants ne changent pas.
- **Gamut large (Wide gamut)** place le log dans un conteneur plus vaste, ACEScct, puis fait le mappage de tons vers Rec.709 à la sortie. Druss précise que c'est un conteneur intermédiaire, pas un pipeline ACES complet.
- Lumetri et plusieurs effets Adobe deviennent « conscients de l'espace couleur » : ils agissent sur les données log d'origine.

**Pourquoi le gamut large aide** (pour information : Cabezer travaille en Direct Rec.709, le gamut large n'est ni utilisé ni à tester) : Druss descend l'exposition de 3 valeurs : en Direct Rec.709 l'image devient pâteuse, en gamut large le dégradé de la lampe reste intact [Tuto Adobe : 20:32 à 22:39] ; Mario So obtient la même chose sur un clip S-Log3 à ±2 EV [Tuto : 9:10 à 10:44]. Raison : en Rec.709, le log est compressé à l'import avant tout réglage.

### 3.2 Réglages à vérifier, dans l'ordre

1. **Préférences > Général** : cocher « gestion des couleurs d'affichage » (Display Color Management)*. Sans elle, l'écran ne reflète pas l'export [Tuto : Mario So 4:05 ; Druss 6:45]. « Extended dynamic range monitoring » : à cocher si l'écran du Mac le permet ; sans effet sur un export SDR.
2. **Réglages du projet** : cocher la détection automatique des médias log et RAW (« Color manage autodetected log and raw media ») et les effets conscients de l'espace couleur (« Enable color space aware effects »)*. Une fois cochés, ils restent actifs pour les projets suivants [Tuto Adobe : Druss 7:16].
3. **Interpolation LUT 3D : tétraédrique** [Tuto : Mario So 5:06 ; Mostyn D-Log M 6:06 pour Resolve].
4. **Réglages de séquence > onglet Gestion des couleurs***, ou onglet Réglages du panneau Lumetri : choisir le Color Setup.
5. **Gamma de visionnage** : voir §4.
6. **HDR Graphics White** : laisser la valeur par défaut (Mario So garde 203 nits). Ne pas toucher en SDR.
7. **Sortie** : Rec.709 ; laisser les mappages de tons de sortie par défaut. Mario So recommande le mappage de tons et la compression de gamma **en sortie** (appliqués après les effets, une fois pour toute la séquence) plutôt qu'en entrée, pour préserver les hautes lumières, et conclut que les défauts donnent de bons résultats dans la plupart des cas [Tuto : 11:16 à 12:48]. Garder les défauts, puis tester sur le plan le plus difficile.

**Critère de réussite** : le panneau Lumetri > Réglages ou la fiche « clip de séquence » indique pour un clip log : « converti de [espace d'origine] vers l'espace de travail, puis vers Rec.709 » [Tuto : Mario So 12:48 à 13:19].

### 3.3 Choisir le preset de séquence

**Preset retenu : Direct Rec.709** (réponse du 12/10/2026, skill §10), avec la conversion unique par clip décrite en 3.4 et 3.5. Il n'y a **pas de gamut large à tester** et aucune bascule à proposer : le gamut large (3.1) n'est décrit que pour comprendre les sources.

| Cas | Choix | Pourquoi |
|---|---|---|
| Rushs déjà Rec.709 (iPhone SDR, captures d'écran, stock) | Direct Rec.709 | Rien à convertir [Tuto Adobe, Tuto : Mario So 7:38] |
| Rushs log (Pocket 3 D-Log M, Panasonic V-Log) | Direct Rec.709 | Conversion unique par clip (3.4, 3.5) ; la marge à l'exposition se règle dans Lumetri après la conversion (§5) |
| Séquence mixte log et SDR ou HLG | Direct Rec.709 | Chaque clip passe par sa conversion unique avant comparaison [Tuto Adobe : Druss 14:53 ; Mario So 2:31] |
| Tout HLG uniquement | Direct Rec.709, conversion par clip (§12) | La livraison est toujours en SDR Rec.709 ; jamais de séquence Direct HLG |

**Règle** : ne jamais changer le preset d'une séquence déjà étalonnée sans refaire le contrôle de tous les plans. Les effets et LUT réagissent différemment selon l'espace de travail [fiche `premiere-pro-avance.md` ; une seule source].

### 3.4 Réglage par clip

Clic droit sur le clip > Modifier (Modify) > Couleur (Color)* [Tuto Adobe : Druss 9:17 à 10:48 ; Mario So 6:38 à 7:38]. Options :
- **LUT d'entrée (Color input LUTs)** : aucun, ou un LUT.
- **Utiliser l'espace colorimétrique du média** : la lecture du tag du fichier.
- **Remplacer l'espace colorimétrique du média** (Override) : forcer le format réel (F-Log, C-Log2, S-Log3…).
- **Préserver le RVB** (Preserve RGB) : coupe la conversion automatique, quand on convertit soi-même.

**Quand la conversion automatique ne se fait pas** (proxy, fichier transcodé, stock, log acheté en ligne) : la transcodification efface la balise de log, donc Premiere affiche « Rec.709 » à tort [Tuto Adobe : Druss 9:48 à 10:18]. Sélectionner les clips d'un dossier, Modifier > Couleur > Remplacer l'espace, choisir le format réel. Ne pas empiler un LUT.

### 3.5 La chaîne par caméra

Le skill (§10) donne la chaîne. La fiche précise le mécanisme, sans le contredire.

| Source | Procédure | Preuve |
|---|---|---|
| **DJI Pocket 3, D-Log M** (tournage en D-Log M) | Skill §10 : diagnostic, conversion DJI D-Log M → Rec.709 **une seule fois**, exposition et blancs dans Lumetri, puis Exterior Cinema ou Doux dosé. Tester si Premiere reconnaît le clip (Modifier > Couleur > espace du média) : si oui, pas de conversion DJI en plus ; sinon, la conversion DJI **une fois** (LUT d'entrée). Ordre exposition/conversion : §5 | Druss cite DJI parmi les fabricants gérés, sans nommer le D-Log M [Tuto Adobe 11:18] ; Mostyn préconise le LUT officiel DJI [Tuto] ; **détection à vérifier** |
| **Pocket 3, HLG** (cas exceptionnel : Cabezer tourne en D-Log M) | Clip HLG (§12). **Jamais de LUT D-Log M sur du HLG** (skill §10) | Druss préfère le HLG, avis qu'il qualifie de « hot take » [Tuto Adobe 14:23 à 14:53] |
| **Panasonic V-Log/V-Gamut** | Skill §10 : conversion Panasonic → Rec.709, **jamais le LUT DJI**. Par défaut, conversion native de Premiere (Remplacer l'espace → Panasonic V-Log / V-Gamut) ; LUT Panasonic officiel seulement si elle est absente ; jamais les deux | Panasonic figure dans la liste de Druss [Tuto Adobe 11:18] ; un forum juge la conversion native meilleure qu'un LUT en gamut large [S] ; **à vérifier** |
| **iPhone HLG, Apple Log** | Voir §12 | Druss 11:18 à 11:49 ; Apple (Doc lue) |
| **Stock, captures d'écran, graphiques** | Direct Rec.709 sans look ni conversion. Voir §8 et §13 | skill §10 |

### 3.6 LUT de conversion et LUT créative : deux rôles

Un LUT de conversion remplace la conversion automatique : il vient du fabricant. Un LUT créatif applique un look [Tuto Adobe : Druss 4:16 à 5:12]. En gamut large, le LUT créatif demande l'espace de couleur du clip : sans lui l'image paraît fausse (Druss déclare « Canon C-Log2 » dans son exemple, puis baisse l'intensité [24:43 à 25:47]).

---

## 4. Gamma d'affichage et écran de contrôle

**Ce que disent les sources** : Premiere propose un gamma de visionnage dans les réglages du projet (Mario So) ou dans Lumetri > Réglages (Druss) : 2.4 pour la diffusion, 2.2 pour le web, 1.96 pour QuickTime [Tuto : Mario So 4:35 à 5:36 ; Tuto Adobe : Druss 7:46 à 8:16]. Le menu de ce réglage n'est pas au même endroit dans les deux vidéos : le trouver à l'écran.

**À quoi sert le réglage** : il change ce que l'étalonneur voit, pas le fichier exporté [I d'après Druss]. Un export peut sembler plus clair dans QuickTime que dans Premiere : 1.96 reproduit ce rendu [Tuto Adobe 7:46 à 8:16].

**Procédure** (toutes familles)
1. Étalonner en **2.4** dans une pièce contrôlée (Mostyn grade en 2.4 et admet 2.2 [Tuto : 896vcqJijtQ 2:02]).
2. Pour contrôler un MP4 lu dans QuickTime, passer ponctuellement à **1.96**, comparer, revenir à 2.4.
3. Ne jamais étalonner un livrable en 1.96 : il paraîtrait plus sombre sur YouTube et sur un téléphone [Tuto : Mario So 5:06 ; I].
4. Certains font suivre le gamma à la pièce (2.4 sombre, 2.2 claire) [S : Mixing Light] : pratique non retenue.

**Tranché (réponse du 12/10/2026)** : les sources divergent (2.4 partout chez Mostyn, selon la destination chez Druss et Mario So, selon la pièce chez Mixing Light), mais Cabezer a choisi **2.4 de travail**, avec validation sur téléphone (§15), et aucune correction globale qui compense un affichage. Le plan test sur téléphone est proposé, jamais bloquant.

**Écran de destination.** Un UHD, un 1080p et une tablette n'affichent pas la même image [Tuto : Levine 37:32]. Cabezer publie surtout sur téléphone : voir §15.

---

## 5. Ordre des opérations

Fixer un arbre d'opérations évite de se perdre. Mostyn le défend avec un arbre à nœuds fixes qu'il suit comme une carte [Tuto : 1:02]. Premiere n'a pas de nœuds ; la correspondance ci-dessous est une inférence [I].

| Étape | Quoi | Où dans Premiere | Contrôle |
|---|---|---|---|
| A. Normaliser | Conversion d'entrée (auto ou LUT du fabricant) | Modifier > Couleur ; Réglages Lumetri | Un seul mécanisme actif |
| B. Exposition | Régler l'exposition sur le sujet (peau en général) | Lumetri > Basique (Basic)* > Exposition | Waveform |
| C. Contraste | Contraste, noirs, blancs | Basique ; Courbes | Waveform et parade |
| D. Balance | Température, teinte, balance des blancs | Basique > Balance des blancs ; Roues* | Parade, vectorscope, peau |
| E. Harmoniser | Faire coller les plans entre eux | §9 | Comparaison côte à côte |
| F. Look | LUT créatif dosé, courbes, vignette | Créatif (Creative)* | Image, puis scopes |
| G. Secondaires | Couleurs ciblées, masques | Courbes teinte/saturation ; TSL secondaire | Image |

**Ordre du skill pour le Pocket 3 (skill §10, réponse du 12/10/2026).** Les sources lues placent la conversion d'entrée avant les curseurs de Lumetri (normaliser, puis exposer), car Lumetri agit après la conversion d'entrée en Direct Rec.709. Ordre appliqué :
1. **Diagnostiquer** l'exposition du rush au waveform, sans rien régler.
2. **Convertir une seule fois** (étape A).
3. **Ajuster** exposition et blancs dans Lumetri Basique (étapes B et C), avant le LUT Exterior.
4. **Poser Exterior** en Créatif, dosé sur les plans réels (étape F).
Il n'y a pas d'ordre alternatif : régler l'exposition « avant la conversion » ne vaudrait qu'en gamut large, qui n'est pas utilisé [Tuto Adobe : Druss 20:32].

**Option de rangement** : une instance de Lumetri par étape (« 1 Normalisation », « 2 Balance », « 3 Look ») pour désactiver un étage et juger. Quand : plan difficile. Éviter : séquence longue (plus de rendu). Procédure Adobe non lue [À vérifier].

**Auto Color.** Adobe le place en tête [S] ; les coloristes lus règlent d'abord à la main [Tuto : Cullen Kelly, Mostyn]. Ne pas s'en servir comme étalonnage de référence ; l'essayer sur un brouillon, résultat vérifié aux scopes.

**Familles** : l'ordre vaut pour toutes. D et F pèsent sur B à D et G ; S sur E (sources variées) ; P et T limitent F à ce que l'identité demande.

---

## 6. Lecture des scopes

Les scopes se lisent à pleine résolution : en lecture à la moitié ou au huitième de résolution, la valeur change quand on s'arrête [Tuto : Levine 11:15 à 11:46]. Arrêter la lecture avant de mesurer.

### 6.1 Waveform (luminance)

- **Sert à** : exposition, contraste, noirs, blancs [Tuto : Mostyn scopes 0:30 à 2:00].
- **Ne sert pas à** : la saturation. Monter la saturation à l'extrême ne change presque rien à la forme [Tuto : Mostyn 2:31].
- **Échelle** : IRE. 0 = noir, 100 = blanc, ~103 = limite haute [Tuto : Levine 6:36 à 7:40].
- **Règle de Mostyn** : ne pas coller les hautes lumières au plafond. Seul le blanc de référence monte en haut [Tuto : 2:00].
- **Dépassements** : décocher « Limiter le signal » (Clamp signal)* pour voir ce qui sort de la plage [Tuto : Levine 9:12].

### 6.2 Parade RVB

- **Sert à** : comparer les trois canaux. Un canal plus haut aux blancs signale une dominante (bleu plus haut : baisser le bleu du gain [Tuto : Mostyn 4:01]). Contraste à zéro, la parade devient une ligne plate : elle mesure aussi le contraste [Tuto : 3:31].

### 6.3 Histogramme

Facultatif : repère les pixels écrasés au noir [Tuto : Mostyn 5:03].

### 6.4 Vectorscope

- **Sert à** : teinte (angle) et saturation (distance au centre). Un plan gris reste au centre [Tuto : Levine 15:55 ; Mostyn 6:36].
- **Ne sert pas à** : l'exposition ni le contraste. La trace bouge quand on monte le contraste parce que la saturation monte aussi [Tuto : Mostyn 7:06].
- **Ligne de chair** : repère de la teinte de peau (skill §10 : contrôler la carnation sur cette ligne). Mostyn : « cette ligne n'est pas la loi » ; être sur, au-dessus ou sous la ligne compte moins que la **constance** dans la scène [Tuto : 6:38 à 8:06 et « 5 PRO Fundamentals » 6:38]. Usage : voir §10.
- **Limite de saturation** : Levine désigne un anneau intérieur d'environ 75 % comme maximum broadcast [Tuto : 17:28, ancienne version]. Sur les réseaux sociaux, c'est un signal d'alerte (rouges d'abord), pas une obligation. Une trace décentrée est acceptable si elle est voulue [Tuto : Mostyn 13:11].

### 6.5 Règle de lecture

Lire le scope pour trouver ce que l'œil rate, puis revenir à l'image. Une scène de nuit reste dans le tiers bas du waveform : ne pas la remplir par principe [Tuto : Mostyn 12:09].

**Comment Claude lit un scope** : capture d'écran, scope en pleine taille, plan à l'arrêt. Noter par plan : plancher, plafond, position de la peau, dominante éventuelle en parade. Claude juge une capture, pas un écran qu'il ne voit pas (§15).

---

## 7. Exposition, contraste, balance, saturation

Les valeurs ci-dessous sont des **points de départ à régler à l'œil**, jamais des cibles.

### 7.1 Exposition

- Régler d'abord le sujet principal, en général la peau. Il n'existe pas de valeur unique : cela dépend de la pièce et de l'expérience [Tuto : Mostyn « 5 PRO Fundamentals » 4:34 à 6:07].
- Procédure Lumetri : Basique > Exposition, en lisant le waveform. Ensuite Hautes lumières, Ombres, Blancs, Noirs.
- **Repère de départ [I]** : si l'exposition de la peau est bonne et que les hautes lumières dépassent, baisser **Hautes lumières** et **Blancs** avant de toucher l'exposition. Garder un peu de marge sous le plafond.
- **Éviter** : « récupérer » un plan très sous-exposé en Direct Rec.709 (l'image devient pâteuse [Tuto Adobe : Druss 20:32]) ; le signaler à Cabezer et corriger l'exposition modérément, sans basculer en gamut large.

### 7.2 Contraste

- **Technique A (Resolve)** : gain et offset plutôt que le curseur « contraste », dont le pivot est à vérifier ; noir au-dessus de 0, hautes lumières sous le plafond [Tuto : Mostyn 8:10 à 9:10].
- **Technique B** : monter le gain, descendre le gamma, pousser le contraste, revenir un peu en arrière si l'image sort des limites ; rendu « commercial » de Waqas Qazi [Tuto : 5:47 à 6:17].
- **Dans Lumetri [I]** : courbe en S légère (Courbes RVB) plutôt que le curseur Contraste seul ; Hautes lumières et Ombres jouent le rôle du gain et du gamma. Vérifier au waveform à chaque mouvement.

| Technique | Quand | Éviter | Familles |
|---|---|---|---|
| Plafond avec marge, noir ≥ 0 | Plans lumineux, peau, produit | Style volontairement écrasé | D, F, T, H |
| Contraste poussé « commercial » | Pub, rendu punchy | Plans de peau délicats, dérush Story documentaire | D (avec prudence), P |

### 7.3 Noirs et blancs : trois positions

- Mostyn : noirs sous 0 acceptables si c'est voulu [Tuto : 5:34]. Levine : garder le détail, même pour YouTube [Tuto : 15:23, contexte broadcast]. Qazi : un pro pousse noirs et hautes lumières pour un rendu commercial [Tuto : 2:12 à 3:43, 11:54].

**Lecture** : les positions portent sur des objectifs différents (données et diffusion contre style). **Règle (réponse du 12/10/2026, skill §10) : détail gardé partout** ; pas d'écrasement des noirs de la peau ni du produit ni du décor ; un noir plus profond sur un décor est seulement proposé à Cabezer plan par plan, jamais appliqué d'office. Pour D et F, le produit garde son détail (croûte, sauce, fromage).

### 7.4 Balance des blancs et teinte

- Pipette de balance des blancs de Lumetri sur une zone **réellement neutre**, puis contrôle au parade [Tuto : Levine 8:42 à 9:12]. Mostyn règle la balance sur la **peau**, pas sur les murs [Tuto : « MATCH Shots » 8:42].
- Cullen Kelly règle la température en kelvins, une seule fois [Tuto : 4:04 à 5:34] ; les curseurs Température et Teinte de Lumetri ne sont pas des kelvins réels [I].
- **Pipette** : utile avec une référence neutre sûre (D, F, T) ; à éviter sur nappe colorée, éclairage mixte, plan sans neutre (D, F, S) : caler alors sur la peau, puis juger le plat.

### 7.5 Saturation

- **Problème** : la saturation « primaire » fait monter la luminance et donne un rendu « numérique » [Tuto : Mostyn 9:10] ; observation faite dans Resolve : dans Lumetri, **mesurer au waveform avant et après**.
- **Alternatives** : saturation sélective par teinte (Courbes teinte/saturation), vibrance, densité plutôt que saturation pour les rouges (plan avec un pic rouge : le rendre plus foncé) [Tuto : Mostyn 10:07 à 10:37 ; Levine 40:38].
- En espace étroit (Direct Rec.709), la saturation casse bords et ciels (Resolve) [Tuto : 896vcqJijtQ 10:09 à 11:10] : l'augmenter par petites touches et mesurer au vectorscope dans Lumetri.

| Technique | Quand | Éviter | Familles |
|---|---|---|---|
| Vibrance | Hausse légère, peau sensible | Remonter une couleur terne sans mesurer | D, F, H |
| Teinte/saturation ciblée | Couleur clé d'un produit | Points de contrôle trop étroits (bascules brutales) [Tuto : Mostyn « MATCH » 12:19 à 12:49] | D, F |
| Saturation globale forte | Rendu « pub » demandé par Cabezer | Peau, vectorscope hors zone | à valider |

---

## 8. Look et LUT créatives

- **Placer le look en bout de chaîne**, après les corrections de base, avec l'espace couleur du clip déclaré [Tuto Adobe : Druss 24:43 à 26:18]. Un look de pellicule émulée se place avant la sortie et reste constant sur toute la vidéo [Tuto : Mostyn 896vcqJijtQ 12:44]. Dehancer, outil de cet exemple, est payant (prix non relevé) : ne pas l'installer.
- **Doser** : regarder à 100 %, puis baisser l'intensité (« wet/dry » [Tuto : Levine 34:00]). Un LUT de film est souvent trop contrasté : baisser l'intensité, relever les ombres [Tuto : Levine 35:31 ; Druss 25:47].
- **Skill §10 : LUT Exterior Cinema ou Doux, dosés sur les plans réels, réservée au Pocket 3.** iPhone et Panasonic ne reçoivent pas ce LUT : ils sont harmonisés à la main (exposition, balance sur la peau, §9). Un look ne remplace pas une bonne exposition.
- **LUT du marché** : beaucoup sont payants. Signaler chaque fois ; ne rien installer sans l'accord de Cabezer (skill §17).

| Famille | Look conseillé | À éviter |
|---|---|---|
| D | Cohérence produit et peau d'un plan à l'autre ; look léger (Exterior dosé sur le Pocket 3 seulement) | Dominante qui change le produit ; look hors de l'identité DA v2 |
| F | Chaleur du plat, fond propre | Plat gris ou orange |
| S | Sobre, documentaire ; cohérence entre sources variées | Look fort sur documents, captures, archives |
| P | Look propre au film ou à la série ; extraits officiels à part (skill §10) | Look facecam sur un extrait de film |
| T | Neutre, blancs nets, interfaces lisibles | Teinte qui fausse une interface |
| H | Selon le brief | Imposer le look d'une famille |

---

## 9. Correspondance de plans et multicaméra

**Pourquoi** : la cohérence entre plans fait un montage « fini » (principe 5, §1).

### 9.1 Méthode de Mostyn (Resolve), transposable en principe [Tuto : « MATCH Shots »]

Caler un plan de référence sur la peau ; copier le réglage sur le plan voisin (un décalage d'exposition subsiste souvent) ; corriger sur la peau, **pas sur les murs** (de face puis de profil, les murs ne sont pas comparables) ; comparer par fondu ou côte à côte ; grouper les plans d'une scène. La « taille de référence » du scope est propre à Resolve : pas d'équivalent à chercher dans Premiere.

### 9.2 Procédure Premiere [I, à tester sur sa version]

1. Étalonner le plan de référence complètement.
2. Sélectionner l'effet Lumetri dans Contrôles d'effets, copier (Cmd+C, à confirmer), sélectionner les plans voisins, **Coller les attributs** (Paste Attributes, Cmd+Option+V*, à confirmer), ne cocher que Couleur Lumetri [Métier].
3. Ajuster chaque plan dans une **instance séparée** : exposition d'abord, puis balance sur la peau, ensuite saturation.
4. Comparer deux plans en Moniteur Programme, en alternant, et au waveform et au vectorscope.
5. **Correspondance de couleur (Color Match)** : Lumetri propose une fonction « Roues chromatiques et correspondance »* avec comparaison de vue. Les sources lues n'en documentent pas l'usage. Quand : premier jet sur deux plans de la même scène. Éviter : résultat final, plans à éclairage mixte [À vérifier]. Toujours corriger à la main ensuite.

### 9.3 Multicaméra (skill §12)

1. **Chaque caméra dans son espace propre**, via sa conversion unique (§3.5, §12), **avant** de comparer [Tuto : Mario So 2:31 ; skill §12].
2. Choisir la caméra principale. Caler les autres dessus : exposition, puis balance sur la peau.
3. **Piège** : une caméra qui voit des couleurs différentes sous un même éclairage ne se corrige pas avec le même réglage. Corriger plan par plan.
4. **Ciel** : doit rester cohérent d'un plan à l'autre [Tuto : Mostyn 896vcqJijtQ 16:16].
5. Contrôle : planche de plans côte à côte, peau dans la même zone du vectorscope [Tuto : Mostyn « 5 PRO Fundamentals » 13:43, Resolve ; équivalent à tester].

**Familles.** D : caler une fois par lieu. F et S : une scène à la fois. P : respecter le look de référence. T : ne pas matcher captures d'écran et facecam. Pocket 3 + iPhone : chacun passe par sa conversion avant le calage sur la peau.

---

## 10. Peau

- **Caler la peau avant tout** : c'est la référence [Tuto : Mostyn « 5 PRO Fundamentals » 13:13].
- **Constance avant fidélité.** Même zone du vectorscope sur toute la scène [Tuto : Mostyn 6:38].
- **Ligne de chair = repère de contrôle (skill §10), pas une cible.** Regarder où tombe la trace de la peau par rapport à la ligne ; si elle s'en écarte mais que l'image paraît naturelle et reste cohérente d'un plan à l'autre, ne pas la déplacer sur la seule foi du scope. Une peau très éloignée de la ligne sur un seul plan signale une balance ou une dominante à revoir.
- **Ne pas keyer la peau.** Si la peau paraît fausse, revenir à la balance de base [Tuto : Mostyn 13:13].
- **Peau visiblement fausse** : courbe teinte/teinte, petit décalage vers la ligne sans exagérer [Tuto : Qazi 8:19 à 8:50].
- **Diversité des teints** : aucune source dédiée n'a été lue. Ne pas imposer une valeur de luminance unique ni caler tous les visages sur la même position. Juger plan par plan, laisser la cohérence interne de la scène primer [I].

**Lissage de peau.** Mostyn utilise l'outil Beauty de Resolve, limité par un masque suivi et mélangé à l'original [Tuto : g4K1NPIA4vY]. Aucun équivalent natif de Premiere n'est documenté. Règle : **ne pas lisser les visages sans demande de Cabezer** ; tester d'abord les outils natifs ; tout outil de génération ou de reconstruction de pixels (Firefly et assimilés) n'est utilisé que sur demande explicite ; signaler tout plugin payant.

**Masques suivis dans Premiere** : non documentés par les sources lues. En principe, les masques d'effets de Lumetri (ellipse, polygone) existent avec suivi [Métier ; à vérifier]. Le suivi sur un vrai plan est un outil autorisé comme aide, résultat vérifié.

---

## 11. Food

**Aucune source food n'a été lue.** Cette section est dérivée et marquée [I]. Elle sert de protocole d'essai, pas de règle sourcée. Le skill (§10) demande déjà une méthode « à valider ».

**Principes dérivés**
1. **Le produit donne envie, sans paraître artificiel** (skill §10). Critère : un spectateur reconnaît la couleur réelle du plat.
2. **Dominante du lieu en primaire**, pas en secondaire : néon + fenêtre = lumière mixte. D'abord la dominante principale, puis, si une zone gêne, un masque (skill §10).
3. **Rouges** (tomate, sauce, viande, fraise) : régler la **densité** avant la saturation [Tuto : Mostyn 10:07 à 10:37 ; transposition I]. Un rouge qui dépasse nettement l'anneau interne du vectorscope attire l'œil.
4. **Séparer produit et peau** : teinte/saturation ciblée, points de contrôle larges, sans déplacer la peau [Tuto : Qazi 8:50 ; Mostyn « MATCH » 12:19].
5. **Chaleur** : légère chaleur sur le plat, fond plus neutre. Le « teal-orange » s'appuie sur l'opposition avec la peau [Tuto : Mostyn scopes 8:37] ; idée à essayer sur plan réel, pas une règle [I].
6. **Textures** : ne pas écraser les ombres du plat ; pas de netteté haute fréquence sans accord (l'outil cité, Texture Pop, est payant).

**Protocole d'essai sur plans réels** (D, F)
1. Choisir trois plans : bouchée en plan serré, gros plan « intérieur », plat sur table.
2. Faire l'étalonnage primaire (§5) et poser une capture de référence.
3. Appliquer une correction ciblée (Courbes teinte/saturation) d'une couleur clé à la fois.
4. Comparer avant/après en alternant ; regarder le vectorscope et la peau. Le produit doit gagner en présence, sans perdre ses détails.
5. Consigner et faire valider avant de généraliser.

**Quand l'éviter** : T (interfaces), S (documents). **Familles** : D (plans courts, bouchée en gros plan, cohérence d'un lieu à l'autre), F (scènes plus longues, ambiance du lieu).

---

## 12. iPhone, HLG, Apple Log et HDR

**Pourquoi** : Cabezer mélange Pocket 3, iPhone et Panasonic (skill §12). Un iPhone livre du SDR, du HDR en HLG ou du log (Apple Log) ; chaque cas se traite différemment et l'erreur ne se voit souvent qu'à l'export (image trop claire, fichier étiqueté HDR). Livraison : **toujours SDR Rec.709**, y compris pour les rushs HDR de l'iPhone (réponse du 12/10/2026, skill §10) [Tuto : Mario So 10:44].

### 12.1 Ce que disent les sources

- **Druss** : Apple figure parmi les fabricants gérés nativement ; Rec.709, Rec.2020 et HLG aussi, HLG étant « ce qui sort de l'iPhone en HDR » [Tuto Adobe : 11:18 à 11:49]. Séquence 100 % HLG : Direct HLG. Séquence mixte : gamut large, conversion par clip [14:23 à 14:53]. Ces deux préconisations ne sont pas retenues : la séquence de Cabezer est en Direct Rec.709 et la livraison en SDR.
- **Apple, documentation pour les développeurs (AVCaptureColorSpace)** [Doc lue] : « HLG_BT2020 » = primaires BT.2020, blanc D65, transfert HLG ; « appleLog » = primaires BT.2020 + courbe Apple Log ; « appleLog2 » = primaires « Apple Gamut » + courbe Apple Log. **Conséquence [I]** : un réglage, un LUT ou une conversion conçu pour Apple Log en Rec.2020 ne convient pas à Apple Log 2 (gamut différent). Savoir lequel des deux l'iPhone de Cabezer produit avant de choisir quoi que ce soit.
- **Courbe Apple Log** [Doc lue : colour-science `apple_log_profile.py`, qui cite le livre blanc Apple 2023, et la transformation ACES AMPAS `IDT.Apple.AppleLog_BT2020`] : un gris 18 % linéaire donne environ 0,488 codé (recalculé [Mesuré]). Contrôle de cohérence d'un outil, pas un réglage. Le livre blanc Apple n'a pas été atteint.
- **Adobe, annonce de la bêta « automatic iPhone ProRes Log support »** [S : extrait de recherche, page non lue ; février 2024] : l'option « Auto Detect Log Video Color Space » classe un clip ProRes Log d'iPhone en « Apple Log / Rec 2020 » dans Lumetri, avec mappage de tons automatique vers Rec.709 ou HLG/PQ, **sans LUT** ; le texte concerne le ProRes Log, pas le HEVC Log ; pour utiliser son propre LUT, désactiver la détection ou forcer le clip en Rec.709. **À vérifier sur sa version** (version d'arrivée du réglage non fiable).
- **Forum Adobe, réponses de Neil Haugen, 2022 à 2024** [S : extraits de recherche, pages non lues] : sur une séquence Rec.709, un clip HLG d'iPhone sort trop clair parce que Premiere lit le tag HDR ; remèdes cités : Modifier > « Interpréter le métrage » (Interpret Footage)*, Gestion des couleurs, « Override to » Rec.709 ; séquence Rec.709 ; mappage de tons automatique et gestion des couleurs d'affichage cochés ; ne pas exporter avec un préréglage dont le nom contient HLG ou PQ ; tourner en SDR si le HDR est inutile. Menus de 2022 : à retrouver dans la version actuelle. **À vérifier**.
- **Signalements de forum** [S] : lecture verdâtre d'un Apple Log HEVC sur Mac Apple Silicon (bêtas 25.5 et 26.0) ; surexposition sur un iPhone 16 Pro avec détection log et mappage de tons activés. Le résultat dépend de la version : comparer à l'image de référence (12.3).

### 12.2 Procédure par clip d'iPhone

Quand : à chaque nouveau lot d'iPhone. Éviter : « Remplacer l'espace » avant d'avoir lu le tag. Familles : D, F, S, T.

1. **Lire les balises du rush** (original, jamais la copie transcodée) :
```
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,profile,pix_fmt,color_range,color_space,color_transfer,color_primaries:stream_side_data=side_data_type -of default=nw=1 rush.mov
```
Syntaxe vérifiée sur un fichier de test [Mesuré]. Noms ffmpeg des valeurs : `arib-std-b67` = HLG, `smpte2084` = PQ, `bt2020` = primaires Rec.2020, `bt2020nc` = matrice Rec.2020 [Doc lue : FFmpeg `pixdesc.c`].
2. **Classer le clip**.

| Ce que lit ffprobe | Nature | Traitement |
|---|---|---|
| `bt709/bt709/bt709`, 8 bits | SDR | Aucune conversion, pas de LUT technique (skill §10) |
| `bt2020` + `arib-std-b67`, 10 bits | HLG | Étape 3 |
| `smpte2084` | PQ | S'arrêter et demander à Cabezer |
| `prores`, transfert non explicite | Probablement Apple Log [I] | Étape 4 ; ce qu'affiche ffprobe pour un Apple Log n'a pas été constaté : le noter dans `Suivi/verifications.md` |
| Rien d'explicite (`unknown`) | Balise absente | Ne pas deviner : lire l'espace détecté par Premiere (Modifier > Couleur) |

3. **HLG vers séquence SDR Rec.709.** Vérifier dans Modifier > Couleur que Premiere lit le clip comme HLG et que le mappage de tons automatique est actif (libellé à confirmer). Au waveform, la peau ne doit pas être collée au plafond ni le clip « brûlé ». Si le clip est nettement trop clair, essayer le remède du forum (remplacer l'espace par Rec.709, au clip) et **comparer** à la référence ffmpeg (12.3) et à un clip voisin du Pocket 3. Garder l'option qui conserve le plus de détail dans les hautes lumières et la noter dans `Suivi/journal.md`.
4. **Apple Log.** Détection automatique des médias log active (§3.2) ; vérifier l'espace affiché (Rec.2020 pour Apple Log, Apple Gamut pour Apple Log 2). **Aucun LUT** : une seule conversion (skill §10). Si le clip n'est pas détecté (proxy, copie transcodée, HEVC), Remplacer l'espace colorimétrique du média > Apple Log. Si Apple Log 2 n'est pas proposé, ne pas prendre un espace voisin : décrire le blocage à Cabezer.
5. **Look.** Aucune LUT D-Log M sur un clip HLG ou Apple Log (skill §10). Le LUT Exterior est réservé au Pocket 3 (réponse du 12/10/2026) : ne pas l'appliquer à l'iPhone ; harmoniser avec le Pocket 3 à la main, par l'exposition et la balance sur la peau (§9).
6. **Contrôler l'export** : balises `bt709` sur les trois champs (voir §14 et `organisation-livraison-qc.md §6`). Un fichier qui sort en `arib-std-b67` est un export HDR par erreur : recommencer avec un préréglage sans HLG ni PQ dans son nom [S].

**Rendu moins lumineux attendu.** Un clip d'iPhone HDR lu dans l'application Photos paraît plus lumineux que sa version SDR : perte de dynamique attendue, pas une erreur. Cabezer a accepté cette perte : la livraison est toujours en SDR Rec.709 ; le rappeler quand il compare.

### 12.3 Image de référence HLG vers SDR avec ffmpeg (approximative)

Quand : un clip HLG paraît douteux dans Premiere. Éviter : s'en servir comme étalonnage ou cible. Familles : toutes.

```
ffmpeg -i hlg.mov -vf "zscale=t=linear:npl=1000,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p" -frames:v 1 ref_sdr.png
```
La chaîne s'exécute sur un fichier de test synthétique [Mesuré] ; elle n'a été comparée ni à un vrai clip d'iPhone ni à Premiere. Le mappage de tons de ffmpeg n'est pas celui d'Adobe : elle donne un ordre de grandeur de clarté [I]. Vérifier la présence de `zscale` et `tonemap` sur le ffmpeg du Mac (`ffmpeg -filters`).

### 12.4 HDR : cas de la livraison

- **SDR Rec.709** sauf brief contraire (skill §13) ; une séquence SDR n'exporte pas en HDR [S].
- **Séquence 100 % HLG** : Direct HLG fonctionne [Tuto Adobe : Druss 14:23], seulement si Cabezer demande une livraison HDR.
- **Séquence mixte** : conversion par clip (Direct Rec.709 par défaut ; gamut large à tester, §3.3).
- **Contrôle** : après export, vérifier les balises (§14) ; un fichier HLG a un transfert différent de Rec.709.

---

## 13. After Effects et couleur

Les animations sont faites dans After Effects (skill §16) ; leur couleur doit rester juste.

1. **Ne pas étalonner les graphismes.** Le look et les corrections se posent sur les plans vidéo (V1, V2), pas sur un calque d'ajustement qui recouvre les pistes d'habillage. Raison : les couleurs d'identité (rouge tomate #E63946, couleurs de pays, skill §5.1) doivent sortir exactes. Si un calque d'ajustement global est indispensable, l'appliquer **sous** les graphismes. Le skill ne fixe pas la place de l'étalonnage par rapport aux graphismes : ceci est le défaut de cette fiche (question 10, §18).
2. **Profondeur de la composition AE** : voir `after-effects-motion-design.md §3.1` (8 bpc pour aplats et texte ; 16 bpc pour ombres douces, dégradés, verre). Si un dégradé de fond montre des bandes, passer cette composition à 16 bpc, puis à 32 bpc seulement si les bandes restent [Tuto : Levine 50:26 à 50:57, ancien ; principe toujours valable, **à vérifier sur AE installé**].
3. **Espace de travail AE** : désaccord non tranché. Levine (ancien) : AE ne tient pas compte d'un espace de travail avec Premiere ; Frame.io : Rec.709 gamma 2.4 dans Fichier > Paramètres du projet > Couleur [S]. **Ne pas choisir sur la foi d'une source** : le test ci-dessous tranche.
4. **Rendu ProRes 4444 alpha** (skill §5.1) : importer dans Premiere et vérifier qu'un aplat de couleur connu (#E63946) ressort identique avant/après passage par Premiere.
5. **Dynamic Link** : les effets Lumetri suivent le clip ; éviter de doubler une correction des deux côtés [Tuto : Levine 48:51 à 50:57].

**Test de couleur pour un modèle AE** (une fois par machine ; D, F, S, P, T)
1. Dans AE, créer une composition 1080 × 1920 avec un aplat #E63946, un dégradé noir-blanc horizontal et un gris 50 %.
2. Rendre en ProRes 4444 avec alpha. Lire d'abord la valeur du pixel du rendu seul avec la commande de `after-effects-motion-design.md §14` (point 5, couleur de marque, attendu `(230, 57, 70)` à ±2).
3. Importer le rendu dans une séquence Premiere (Direct Rec.709), l'exporter en MP4, puis lire le même pixel sur une image du MP4 (grand aplat, pour éviter l'erreur du sous-échantillonnage de la chrominance [I]). Un écart sensible entre les deux lectures indique un réglage d'espace à corriger côté AE ou côté séquence.
4. Consigner la procédure exacte dans la fiche d'identité de la famille.

---

## 14. Export, balises et contrôle du fichier

**Lacune** : aucune source lue ne décrit les balises couleur écrites par Premiere à l'export. Ne pas affirmer : contrôler le fichier exporté avec la bibliothèque de `organisation-livraison-qc.md §6`. Établi : sortie Rec.709 par défaut ; mappage de tons et compression de gamma de sortie appliqués après les effets [Tuto : Mario So 10:44, 11:47].

### 14.1 Ce qui est déjà dans organisation-livraison-qc.md §6 (ne pas dupliquer)

- **Balises du MP4** et attendu `bt709/bt709/bt709` : niveau 1, §6.2 (script `controle-mp4.sh`, ligne « couleur »). Lire aussi `color_range` : `tv` attendu en SDR. `unknown` n'est pas grave, mais certains lecteurs devinent alors la matrice ; noter ce que Premiere écrit sur la machine de Cabezer.
- **Niveaux et saturation** (`signalstats` : `YMIN`, `YMAX`, `SATMAX`) : niveau 3, §6.3. En 8 bits « tv », noir 16 et blanc 235 ; un `YMAX` nettement au-dessus de 235 signale des hautes lumières hors plage. Ces mesures signalent un cas à revoir, elles ne remplacent pas le visionnage (skill §14).

### 14.2 Commandes propres à la couleur (à ajouter à la bibliothèque §6 après validation)

| Usage | Commande | Seuil ou lecture |
|---|---|---|
| Image fixe de contrôle avec matrice forcée | `ffmpeg -ss 5 -i export.mp4 -frames:v 1 -vf "scale=in_color_matrix=bt709:in_range=tv:out_range=pc" frame.png` | Évite qu'ffmpeg suppose une autre matrice sur un fichier sans balise |
| Waveform du fichier, indépendant de Premiere | `ffmpeg -ss 5 -i export.mp4 -frames:v 1 -vf "waveform=scale=ire:graticule=green" wave.png` | Comparer au waveform de Premiere : mêmes plafonds |
| Vectorscope du fichier | `ffmpeg -ss 5 -i export.mp4 -frames:v 1 -vf "vectorscope=mode=color3:graticule=green" vec.png` | Peau dans la même zone d'un plan à l'autre |
| Corriger seulement les balises, sans toucher aux pixels (H.264) | `ffmpeg -i in.mp4 -c copy -bsf:v h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=1:video_full_range_flag=0 out.mp4` | Seulement si les pixels sont réellement Rec.709 ; pour du H.265, même commande avec `hevc_metadata` |

Commandes exécutées sur un fichier de test [Mesuré], jamais sur un export de Premiere : tester d'abord sur une copie. Réétiqueter un fichier dont les pixels ne sont pas en Rec.709 masque l'erreur sans la corriger. L'écart « plus clair dans QuickTime » vient du gamma de lecture (§4), pas du fichier. Statuts : balises lues = contrôlé ; couleur validée à l'œil par Cabezer = validé (skill §1).

---

## 15. Contrôle sur téléphone

**Pas de source sur cette procédure.** Procédure proposée [I], à faire valider.

1. Exporter un **plan test** de 10 s (sombre, clair, peau), au format de livraison, et l'envoyer sur le téléphone de Cabezer (luminosité automatique, puis moyenne).
2. Comparer à l'écran de montage : une image plus claire ou moins contrastée est normale dans une pièce lumineuse.
3. Questions à poser à Cabezer : le produit donne-t-il envie ? la peau est-elle naturelle ? des détails dans les ombres ont-ils disparu ? Pour D, ajouter : les sous-titres de dégustation (72 à 75 % de la hauteur, skill §9) restent-ils lisibles sur le fond ?
4. **Corriger sur l'écran de montage**, jamais un plan entier d'après le téléphone : il sert à valider ou à déceler un plan trop sombre.

Claude ne peut pas voir le téléphone. Noter dans `Suivi/retours.md` : « contrôle sur téléphone non fait » tant que Cabezer n'a pas répondu (skill §1 : distinguer contrôlé et validé).

---

## 16. Erreurs de débutant → réflexes de pro

| Erreur | Réflexe |
|---|---|
| Ajouter un LUT sur un clip converti automatiquement | Un seul mécanisme par clip ; vérifier le tag (Modifier > Couleur) |
| Faire confiance à « Rec.709 » pour un proxy ou un stock | Remplacer l'espace du média par le format réel |
| Appliquer un LUT D-Log M à un clip d'iPhone HLG ou Apple Log | Aucun LUT D-Log M hors Pocket 3 en D-Log M (skill §10) ; lire le tag et traiter selon §12 |
| Exporter un clip d'iPhone HDR sans regarder les balises | Lire `color_transfer` du MP4 : `bt709` attendu, jamais `arib-std-b67` (§12.2) |
| S'étonner qu'un iPhone HDR paraisse moins lumineux en SDR | Perte de dynamique attendue ; comparer au waveform, pas à l'application Photos |
| Étalonner en 1.96 | Rester en 2.4 ; 1.96 simule QuickTime |
| Tout garder au milieu du waveform | Contraste voulu ; marge en haut, noir au-dessus de 0 pour peau et produit |
| Remonter la saturation à fond | Densité des rouges, vibrance, saturation ciblée ; mesurer au vectorscope |
| Corriger la peau par une incrustation | Revenir à la balance de base |
| Déplacer une peau vers la ligne de chair par principe | La ligne est un repère ; la constance et l'aspect naturel priment (§10) |
| Appliquer un look à 100 % sans le baisser | Regarder à 100 %, puis doser |
| Poser un calque d'ajustement global sur tout, habillage compris | Étalonner les plans vidéo ; graphismes AE hors étalonnage (§13) |
| Changer de preset de séquence après l'étalonnage | Fixer le preset d'abord, ou tout contrôler à nouveau |

---

## 17. Liste de contrôle

- [ ] Version de Premiere relevée et consignée dans `Suivi/environnement-verifie.md`. Pas de mode Color mélangé avec Lumetri (sinon s'arrêter et demander).
- [ ] Gestion des couleurs d'affichage activée ; gamma de travail noté.
- [ ] Projet : détection auto log/RAW et effets conscients de l'espace couleur cochés.
- [ ] Séquence : preset de couleur noté (Direct Rec.709 par défaut) ; Rec.709 en sortie.
- [ ] Chaque clip : un seul mécanisme de conversion (Modifier > Couleur vérifié).
- [ ] Clips d'iPhone : balises lues, nature classée (SDR, HLG, Apple Log), aucun LUT D-Log M (§12).
- [ ] Exposition, puis contraste, puis balance : dans cet ordre, scopes à pleine résolution.
- [ ] Peau cohérente entre plans, pas de keying de peau, pas de lissage non demandé.
- [ ] Hautes lumières avec marge ; noirs de la peau et du produit non écrasés.
- [ ] Saturation mesurée ; rouges contrôlés au vectorscope.
- [ ] Look dosé ; plans comparés côte à côte ; ciel et peau cohérents.
- [ ] Food : produit attirant et naturel, validé à l'œil.
- [ ] Graphismes AE hors étalonnage ; couleurs d'identité exactes (test §13).
- [ ] MP4 exporté : balises `bt709` lues, niveaux mesurés (`organisation-livraison-qc.md §6`).
- [ ] Contrôle sur téléphone proposé ; statut noté (appliqué / contrôlé / validé par Cabezer).
- [ ] Consignation : version, réglages, LUT, mesures, limites.

---

## 18. Décisions à demander à Cabezer

> **Toutes ces questions ont reçu une réponse de Cabezer le 12/10/2026** : voir `../decisions-en-attente.md`, qui prime sur les défauts ci-dessous.

Défaut en attendant : appliquer la valeur indiquée, ne jamais présenter l'alternative comme une règle.

1. **Gamma de travail** : 2.4 partout, ou 2.2 pour ce qui part sur téléphone ? Défaut : 2.4, validation sur téléphone.
2. **Preset de séquence (Pocket 3, séquences mixtes)** : Direct Rec.709 + conversion unique + LUT Exterior, ou gamut large (test à trois plans, §3.3) ? Défaut : Direct Rec.709 ; gamut large = essai sur copie.
3. **Pocket 3 : D-Log M ou HLG au tournage** ? Les sources divergent. Défaut : D-Log M (skill §10) ; essai HLG seulement à sa demande.
4. **Ordre exposition / conversion du skill §10** : l'intention est-elle de régler l'exposition avant la conversion (littéral) ? Défaut : diagnostic de l'exposition, conversion unique, puis exposition et blancs dans Lumetri avant le LUT Exterior (§5).
5. **Noirs** : écrasement de décor autorisé en style, ou détail conservé partout ? Défaut : détail conservé partout.
6. **Lissage de peau** : jamais, ou seulement à sa demande ? Défaut : seulement à sa demande, outils natifs d'abord, aucune génération de pixels.
7. **iPhone au tournage** : SDR, HDR (HLG) ou Apple Log ? Apple Log ou Apple Log 2 ? Défaut : aucune consigne imposée ; chaque clip est traité selon son tag (§12).
8. **LUT Exterior sur iPhone et Panasonic** ? Défaut : non, sans accord.
9. **Perte du HDR de l'iPhone à l'export SDR** : acceptée ? Défaut : oui (skill §13).
10. **Étalonnage et graphismes AE** : seulement les plans vidéo, jamais un calque d'ajustement global sur l'habillage ? Défaut : oui (§13).
11. **Ligne de chair** : repère avec validation visuelle ? Défaut : oui, sans déplacer une peau naturelle et cohérente (§10).
12. **Contrôle sur téléphone** (§15) : procédure acceptable ? Défaut : proposée à chaque projet, jamais bloquante.

---

## 19. Sources étudiées

Neuf transcriptions relues en entier ; celle de Levine (57 min) relue par recherche de passages. En passe 2, seuls developer.apple.com et raw.githubusercontent.com étaient atteignables ; les pages Adobe, gamut.io, colour-science.org, support.apple.com, Wikipédia et le site FFmpeg ont été refusés.

| Auteur | Titre | URL | Couverture réelle |
|---|---|---|---|
| Darren Mostyn | How I ACTUALLY Read My Scopes | https://www.youtube.com/watch?v=6m3AR-hNsSw | Transcription lue (Resolve) |
| Darren Mostyn | How To IMPROVE Your D-Log M Grades | https://www.youtube.com/watch?v=896vcqJijtQ | Transcription lue (Resolve ; Pocket 3) |
| Darren Mostyn | Has Colour Grading Got Too Complicated? 5 PRO Fundamentals (25/05/2026) | https://www.youtube.com/watch?v=z7PFk8vYSxs | Transcription lue (Resolve) |
| Darren Mostyn | How To Grade Skin Smooth | https://www.youtube.com/watch?v=g4K1NPIA4vY | Transcription lue (Resolve, outil Beauty) |
| Darren Mostyn | Learn to PRO Color MATCH Shots in 15 mins! | https://www.youtube.com/watch?v=l3rOObH74TE | Transcription lue (Resolve) |
| Cullen Kelly | Objective Grading, Part 2 (2021) | https://www.youtube.com/watch?v=0JvfdRX32Eg | Transcription lue (Resolve) |
| Waqas Qazi | Common Mistake Beginners make when Grading LOG Footage | https://www.youtube.com/watch?v=P1VKvN9VycU | Transcription lue (Resolve ; style commercial) |
| Jason Druss (se présente comme membre de l'équipe Premiere) | No More Confusion – Premiere 25 Made Color Simple | https://www.youtube.com/watch?v=TiW9W1fWxcA | Transcription lue (Premiere 25.2 à 25.4) ; relue en passe 2 pour la liste des caméras et le HLG de l'iPhone (11:18 à 11:49, 14:23 à 14:53) |
| Mario So | THIS Will Forever Change How You Colour Grade in Premiere Pro! (08/02/2025) | https://www.youtube.com/watch?v=s1ytvMGb9pE | Transcription lue (se dit non professionnel ; numéro de version de la bêta douteux, non retenu) |
| Jason Levine (Adobe) | How to Make Great Videos with COLOR – Part 3 | https://www.youtube.com/watch?v=SARTaz3FuQI | Transcription lue ; interface ancienne, avant la gestion de couleur 2025 |
| Apple | Documentation développeur : AVCaptureColorSpace (HLG_BT2020, appleLog, appleLog2) | https://developer.apple.com/documentation/avfoundation/avcapturecolorspace | Lue en entier (données de la page) le 12/10/2026 ; primaires et transfert de chaque espace, pas le comportement de Premiere |
| Colour Developers (colour-science) | `apple_log_profile.py` | https://raw.githubusercontent.com/colour-science/colour/develop/colour/models/rgb/transfer_functions/apple_log_profile.py | Code lu en entier ; constantes de la courbe Apple Log (cite le livre blanc Apple 2023, non atteint) |
| AMPAS | `IDT.Apple.AppleLog_BT2020.ctl` (ACES) | https://raw.githubusercontent.com/ampas/aces-dev/528c78fe2c0f4e7eb322581e98aba05de79466cb/transforms/ctl/idt/vendorSupplied/apple/IDT.Apple.AppleLog_BT2020.ctl | Lu en entier ; confirme constantes et primaires BT.2020 |
| FFmpeg | `libavutil/pixfmt.h`, `libavutil/pixdesc.c` | https://raw.githubusercontent.com/FFmpeg/FFmpeg/master/libavutil/pixfmt.h | Extraits lus : noms `arib-std-b67`, `smpte2084`, `bt2020`, `bt2020nc` |
| Rédaction | Essais ffmpeg et ffprobe 6.1.1 | — | Commandes de §12 et §14 exécutées sur fichiers synthétiques ; aucun rush de Cabezer, aucun export de Premiere |
| Adobe Community (annonce « now in beta automatic iphone prores log video support » ; fils de Neil Haugen sur l'iPhone HLG) | pages citées par la recherche web | https://community.adobe.com/announcements-732/now-in-beta-automatic-iphone-prores-log-video-support-313720 | **Non lues** (extraits de recherche) ; aucune règle ne repose sur elles seules |
| Adobe, Frame.io, Mixing Light, DJI, gamut.io | pages citées par la recherche préalable | — | **Non lues** (extraits de recherche) |
| — | Vidéos non lues : Adobe « Color Management in Color Mode » (sa6MpFSph5k), Juan Melara (8qJ7i9b28Lo), Cullen Kelly (VxCcs3ZWYtg), Waqas Qazi « Seven Levels » (cw9a1p6DScY) | — | Échec de téléchargement (bot-check) ; à reprendre |
