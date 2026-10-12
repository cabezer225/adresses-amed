# After Effects et motion design niveau expert

> **Réponses de Cabezer du 12/10/2026 — elles priment sur cette fiche**, en particulier sur sa section « Décisions à demander » : SRT seul pour les vidéos longues tournées en France ; identité Story v15 et générique « Amed Story 🧢 » supprimés (à refaire) ; coupe courte de la bouchée sur tous les formats courts ; jamais de foley d'aliment ; ambiance en dégustation proposée au premier usage ; composition musicale en Story, food long et tech ; respirations d'émotion gardées aussi en films/séries et au verdict du food long ; 4K pour YouTube long quand les rushs sont en 4K ; un rendu de sous-titres par passage validé ; intervenants identifiés à la première apparition (hors D) ; au plus deux passes de retravail sous 8 ; Tesseract, Higgsfield et SCANDALE FOOD retirés. Liste complète : `../decisions-en-attente.md`.

Fiche de référence pour animer dans After Effects (AE) et livrer à Premiere comme un motion designer professionnel, dans le cadre des règles de Cabezer. Révision v2 du 12/10/2026. La version d'AE lue à l'écran fait foi.

**Niveaux de preuve** : **[Skill]** règle de Cabezer ou décision d’harmonisation, elle prime. **[Doc lue]** référence d'expressions ou guide de scripting (sources docsforadobe lues sur GitHub) : prouve noms, signatures et texte de l'aide, pas le comportement dans AE. **[T1…T10]** transcription lue en entier, avec minutage (§22). **[Testé ici]** exécuté dans cette session (ffmpeg, Node, faux moteur d'API) : prouve un outil de contrôle ou une syntaxe, jamais AE. **[Extrait]** extrait de recherche, page non lue. **[À vérifier]** savoir général non recoupé. Sans étiquette : conseil de méthode.

**Limites.** Aucun code n'a été exécuté dans After Effects. Le proxy refuse les pages Adobe, School of Motion et motionscript ; YouTube a refusé 3 des 6 tentatives autorisées (anti-robot), sans contournement.

## Quand lire cette fiche

Avant toute animation, tout habillage ou tout échange Premiere ↔ AE : étiquettes, prix, pop-ups, notes, sous-titres animés, documents explorés en 3D, suivi, rendu ProRes 4444 alpha, scripts. Gestes dans Premiere : `premiere-pro-avance.md`. Identité par famille : skill §5.1, §6. Interface et exécution des scripts sur le Mac : `pilotage-environnement-reprise.md`.

Hiérarchie (skill §1) : brief → skill → fiches → tutoriels. Chaque technique dit **quand l'utiliser, quand l'éviter, pour quelles familles** : D dégustation, F food long, S Story, P films/séries (PRISME), T tech, H hors familles.

## Sommaire

1 Pilotage, version, langue · 2 Premiere ou AE · 3 Outils IA · 4 Projet et organisation · 5 Principes d'animation · 6 Éditeur de graphiques, easing, rebond · 7 Recettes D et photosensibilité · 8 Texte et sous-titres · 9 Formes, Trim Paths, caches · 10 Expressions · 11 Caméra 3D, profondeur de champ, parallaxe · 12 Suivi, roto, incrustation · 13 Flou de mouvement · 14 Passerelle Premiere, rendu, MOGRT · 15 Contrôler un rendu · 16 Piloter AE par script · 17 Matrice par famille · 18 Plugins · 19 Erreurs → réflexes · 20 Liste de contrôle · 21 Décisions à demander · 22 Sources

---

## 1. Pilotage, version, langue

1. **Lire la version** : After Effects > À propos (libellé à confirmer). Le journal du guide de scripts cite 26.0 (janvier 2026), 26.3 (juin) et 26.5 (septembre 2026) [Doc lue] ; table complète : `pilotage-environnement-reprise.md §2`. Ne pas affirmer une fonction récente tant qu'elle n'est pas à l'écran.
2. **Libellés** : nom français, anglais entre parenthèses, « libellé à confirmer » tant qu'il n'est pas lu.
3. **Raccourcis** : aucun avant lecture dans l'éditeur de raccourcis clavier ; sinon le menu (décisions d’harmonisation B4). F9, U, Maj+F3, Alt+W cités ici sont **à confirmer** ; touches de fonction = Fn sur Mac.
4. **Scripts** : préférer noms de correspondance (`ADBE Position`) et attributs (`lyr.position`) aux noms affichés, qui peuvent être traduits [À vérifier]. `app.findMenuCommandId("…")` n'est pas fiable d'une langue à l'autre : relever l'identifiant puis `app.executeCommand` ; `app.isoLanguage` donne la langue d'AE, `$.locale` celle du système [Doc lue].
5. **Interface en anglais** : à proposer, jamais à imposer (§21).
6. Séparer appliqué / contrôlé / validé ; Enregistrer sous une nouvelle version avant de modifier un projet.

---

## 2. Premiere ou After Effects

Définition du skill §1, §16 (décisions d’harmonisation B1) :
- **Animation graphique** (texte, forme, emoji, pastille, prix, note, schéma, carte, sous-titre animé, flash ou glitch graphique, transition graphique, parallaxe 2.5D) : **AE**, calques natifs modifiables.
- **Traitement d'un plan filmé** (punch-in sec, zoom façon Micode, whip ou shake du cadre, speed ramp, recadrage, Auto Reframe, stabilisation, fondu, mouvement sur photo ou document qui désigne un détail) : **Premiere** (`premiere-pro-avance.md §8.2`).

Cas limites : shake d'étiquette ou de prix = AE, shake du cadre = Premiere ; flash blanc et scintillement = AE, whip entre deux lieux = Premiere ; zoom simple sur une image plate qui désigne un détail = Premiere, tout ce qui demande plusieurs plans, caméra 3D, cache, surlignage ou parallaxe = AE. Un script pilote AE ; il ne fabrique jamais d'image hors d'AE (§16).

---

## 3. Outils IA : trois statuts

Tableau de référence : skill §16.

| Outil | Statut |
|---|---|
| Remplissage génératif, Generative Extend, tout outil Firefly ou texte-vers-image/vidéo | **Interdit** sans demande explicite |
| Remplissage d'après le contenu (reconstruit des pixels [Extrait]) | **Seulement sur demande explicite** (décisions d’harmonisation B2) |
| Roto Brush (3.0 selon T7), suivi sur un vrai plan | **Autorisé comme aide, résultat vérifié** |
| Object Matte (nature à confirmer sur la version) | **Non tranché : demander** ; défaut : ne pas utiliser |
| Suivi, Warp Stabilizer, Mocha AE | Autorisé |

**Pourquoi** : retirer ou ajouter un objet fait passer du faux pour du réel (skill §8). Alternatives : recadrer, changer de plan, masquer par un élément graphique assumé, nettoyer à la main. T7 présente Roto Brush 3.0 comme « alimenté par un nouveau modèle d'IA » ; les décisions d’harmonisation l'autorisent quand même (§12.2).

---

## 4. Projet, composition, organisation

### 4.1 Réglages à la création

1. **Taille et cadence = celles de la séquence Premiere**, relues à chaque projet (Milan : 29,97 i/s, 2160 × 3840 [Skill §14]). Par script, relire `comp.frameRate` après `addComp` [Doc lue : l'exemple de l'aide utilise 29.97].
2. **Pixels du skill = base 1080 × 1920** : `px composition = px base × largeur / 1080` (×2 pour 2160). Les pourcentages ne changent pas.
3. **Poids d'un ProRes 4444 alpha** [Testé ici, 30 images, éléments synthétiques] : pastille blanche plate 0,96 Mo en 1080 × 1920 et 3,9 Mo en 2160 × 3840 ; contenu bruité 10 Mo et 28 Mo. Compter ×4 entre les tailles ; mesurer au premier vrai rendu.
4. Durée = élément + 5 images au plus. 8 bpc pour aplats et texte, 16 bpc pour ombres douces et dégradés [À vérifier].
5. Polices Avenir Next Heavy et Bold [Skill] ; par script, nom PostScript, à lire dans le panneau Caractère. Emojis : PNG Apple (`Identite-Degustation/Emojis/`) à 2× ; ne pas taper un emoji dans un calque de texte [À vérifier].
6. Couleurs hexadécimales du skill (`#E63946`, `#CE2B37`, `#009246`), jamais à la pipette. Par script : tableau 0–1 [Doc lue].

### 4.2 Organisation

- Dossiers `00_PRECOMPS`, `01_ELEMENTS`, `02_MEDIAS`, `03_RENDUS`.
- **Deux niveaux sans contradiction** (skill §5.1, §16) : en **D**, une composition éditable **par élément**, rendue en alpha ; en **F, S, P, T**, une composition **par scène**, nommée, contenant les éléments en précompositions ouvrables.
- Ne pas dupliquer un calque de précomp pour le rendre différent : dupliquer la composition [Extrait]. Contrôleurs nommés sans accent (`CTRL_Retard`), lus par numéro `effect("CTRL_Retard")(1)` ; un seul pilote par réglage récurrent.
- **Identités absentes** : un lien cassé vers une fiche d'identité est annoncé en début de session, jamais remplacé par une invention. **Liquid Glass (T)** : ne pas prétendre l'appliquer sans sa fiche ; la construire avec Cabezer avant toute animation tech (modèle : SKILL.md §6, « Après validation »).

**Réussite** : ouvrir le projet à froid permet de changer un texte ou un prix et de refaire le rendu.

---

## 5. Principes d'animation

Les douze principes de Thomas et Johnston (*The Illusion of Life*, 1981 [Extrait]) guident sans imposer de valeurs. Retenir : **compter en images** (à 29,97 i/s, 4 images ≈ 133 ms, 7 ≈ 234 ms [Testé ici]) ; ralentir à l'entrée et à la sortie (easing) ; anticipation et dépassement avec parcimonie (D : la pop du skill suffit) ; arcs en séparant X et Y de 1 à 3 images [Extrait] ; **un seul élément principal bouge à la fois**.

Règles de direction : chaque mouvement révèle, désigne ou récompense, sinon le supprimer ; sortie plus courte que l'entrée ; mêmes courbes et durées pour une famille (c'est l'identité) ; en vertical, éléments grands, tenus max(1,5 s ; 1 s + caractères/15), soit 2,6 s pour 24 caractères [Testé ici] (pas pour le mot à mot de D ni les coupes rapides, décisions d’harmonisation C) ; ni bouchée, ni produit, ni visage recouverts.

**Réussite** : à vitesse réelle, sur téléphone, on comprend l'élément sans le chercher.

---

## 6. Éditeur de graphiques, easing, rebond

### 6.1 Procédure [T1 sauf mention]

1. Sélectionner les clés > Animation > Assistant de clés (Keyframe Assistant) > Easy Ease [2:06 ; libellé à confirmer]. Boutons Easy Ease, Ease In, Ease Out aussi dans l'éditeur [15:26].
2. Ouvrir l'**éditeur de graphiques** (Graph Editor) [3:45], « ajuster tous les graphes à la vue » [4:16].
3. **Graphique de valeur** : la courbe est la valeur, sa **pente** la vitesse. **Graphique de vitesse** : la **hauteur** est la vitesse ; Joey le réserve à des cas précis [4:48, 6:27]. Ne pas lire l'un comme l'autre.
4. **Séparer les dimensions** (clic droit sur Position ; libellé à confirmer) pour piloter X et Y [8:30] ; contrepartie : plus de poignées dans la fenêtre de composition [Extrait], et `numKeys` change [Doc lue].
5. Maj verrouille l'orientation d'une poignée [9:33] ; copier-coller une clé garde l'angle [21:18] ; Option/Alt + glisser la première ou dernière clé étire l'ensemble [23:27].
6. **Le moins de clés possible** : deux valent mieux que trois, courber les poignées plutôt que caler une étape [35:41].

### 6.2 Valeurs

- **Easy Ease = vitesse 0, influence 33,33 %** [Extrait, deux fils ; aucune source lue] ; T1 ne donne aucune influence. Par script, influence de **0,1 à 100** [Doc lue].
- Valeurs de départ à régler à l'œil, à vitesse réelle (non sourcées) : arrivée douce (étiquette, carte) arrivée 75 / départ 25 ; mouvement sec (prix, pop) départ 25, arrivée plus longue. Les plages « 16–33 % et 70–90 % » des notes sont écartées. Les poser par script (§16.4).

### 6.3 Rebond à la main [T1 13:19–24:58]

T1 est tourné **à 24 i/s** (« we're in 24 », 17:00) : ses nombres d'images sont des proportions. Chute 16 images (essai de 20 trop lent), impact **sans ease de sortie** ; rebond à **la moitié de la hauteur** (8 images de montée, quelques images de suspension), retombée = montée copiée inversée ; rebonds suivants 4, 3, 2 images, chacun une « miniature » du précédent en copiant la courbe ; effet cartoon : étirer l'arc au sommet puis Option/Alt sur l'ensemble. À 29,97 i/s, 16 images à 24 i/s valent environ 20 images (0,67 s) [calcul]. **Quand** : objet qui tombe dans un schéma (S, T, F). **Éviter** : D, P.

### 6.4 Linéaire correct (décisions d’harmonisation D1)

« Jamais linéaire » vise les mouvements progressifs. Corrects : un **punch-in sec** (changement instantané, clé maintenue ou deux clips, dans Premiere) et la **vitesse constante** pour rotation continue, défilement, compteur, boucle. La signaler dans `Suivi/journal.md`.

### 6.5 Pièges

Une propriété pilotée par expression ignore l'easing de ses clés [À vérifier] ; poignée trop tirée = dépassement qui ressemble à un bug.

**Réussite** : courbe de vitesse propre (une bosse, pas de dents).

---

## 7. Recettes D et photosensibilité

Valeurs du skill §5.1 [Skill], base 1080 × 1920. Famille D ; F et T si le brief le demande. Interdits DA v2 : contours épais, ombres baveuses, stickers détourés, pictos dessinés, tampons, liserés, animations molles.

| Élément | Mouvement | Durée à 29,97 i/s | Où |
|---|---|---|---|
| Étiquette | Glisse de 8 px en 4 images + opacité | 133 ms | AE |
| Pop-up emoji | 0 → 118 → 96 → 100 % en 7 images | 234 ms | AE |
| Flash intérieur | Blanc 70 % → 0 en 4 images | 133 ms | AE |
| Shake d'étiquette ou de prix | 6 images | 200 ms | AE |
| Whip entre deux lieux | 4 à 6 images, 130 %, glissement 12 % | 133–200 ms | Premiere |
| Punch-in sec | 100 / 115 %, 120 % sur la bouchée | instantané | Premiere |

**Pop-up** : emoji à 2× ; échelle 0 puis 118 % (image 2), 96 % (image 4), 100 % (image 6), positions indicatives à caler sur l'attaque du SFX ; Bézier ; opacité 0 → 100 % en 2 images ; ombre courte et nette (distance 4 à 6 px, opacité 30 à 40 %, non sourcé). **Étiquette** : forme arrondie + texte Avenir Next Bold noir, pastille liée au texte (§8.3) ; une étiquette lieu dans le hook, produit · prix à la révélation ; aucune étiquette ajoutée pour relancer l'image. **Prix** : montant seul, Heavy blanc, pop + petit shake (§10.1) + caisse. **Note** : « 7-8/10 » + emoji, flash, ding. **Marqueurs SFX** : un marqueur de calque sur l'image d'attaque de chaque élément, exporté en CSV (§16.5) ; élément retiré = SFX retiré.

**Photosensibilité.** Flash blanc, note avec flash et scintillement sont des variations de luminance : ils comptent dans la limite de flashs par seconde de `conformite-droits-accessibilite.md §6` (au plus 3 flashs généraux par seconde ; test de l'export en §6.5-6.6). Dans un hook agressif, compter flashs, whips à fond blanc et coupes de forte luminance ; au-delà de 3, supprimer ou espacer. Un shake ne change pas la luminance. Consigner dans `Controles/`.

**Réussite** : un élément = un son = un changement visible ; aucun élément ne couvre la bouchée.

---

## 8. Texte, sous-titres animés, boîtes responsives

### 8.1 Animateurs de texte

**Quand** : révélation mot à mot, titres (S titres de concept, F, T). **Éviter** : D (pop du skill), P (mouvements retenus), longs textes avec flou de mouvement [À vérifier]. Procédure [T5 1:30–2:00 ; libellés à confirmer] : Animer (Animate) > Opacité à 0 % ; sélecteur de plage (Range Selector), clé de **Début** 0 % puis 100 % douze images plus loin ; Avancé > **Basé sur (Based On) : Mots** (sur « Caractères », effet machine à écrire ; T5 propose Mots ou Lignes) ; Easy Ease sur la dernière clé ; Forme **Lisse** pour adoucir [10:40] ; un bloc de texte par pensée.

**Noms de correspondance lus** [Doc lue] : `ADBE Text Animators` > `ADBE Text Animator` ; sélecteur `ADBE Text Selector` (Début/Fin/Décalage `ADBE Text Percent Start/End/Offset`) ; `ADBE Text Range Advanced` avec Lissage `ADBE Text Selector Smoothness`, Ease High/Low `ADBE Text Levels Max/Min Ease` ; propriétés `ADBE Text Opacity`, `Fill Color`, `Blur`. Le nom de « Basé sur » n'y figure pas : construire l'animateur à la main.

**Variantes** : inversion par flou [Extrait, Adobe Community 2020] : Décalage de 100 à −100, forme Rampe descendante, Basé sur Mots, Ease Low 100 %. Départ à 0 % d'échelle : la boîte liée au texte saute, commencer à **1 %** [T3 7:10]. Couleur par mot : Effet > Générer > Remplissage [T5 4:32] ; ordre de lisibilité contraste, couleur, flou. Sortie : clés de plage à 0 %, le dernier bloc sort le premier [T5 10:10]. Flou de mouvement sur le calque **et** la composition [T5 5:33].

### 8.2 Sous-titres animés : voie unique (décisions d’harmonisation C)

Sous-titres finaux = **composition AE** à l'identité de la famille : un calque de texte éditable, **un mot ou un paquet par clé de Texte source**, entrée animée, rendu **ProRes 4444 alpha**, plus **SRT livré**. Les légendes natives de Premiere servent de transcription et de calage ; « Mettre à niveau la légende » n'est plus utilisé ; un repli sans AE s'appellerait « repli non animé » et serait consigné. Détail et expression de pop : `formats-courts-verticaux.md §4`.

Limites (décisions d’harmonisation C) : D français = **un mot à la fois** ; D traduction = 1 à 3 mots, 18 caractères au plus ; autres familles et étranger = 2 lignes, 24 caractères par ligne en 9:16, environ 42 en 16:9. Style D [Skill §9] : Avenir Next Heavy en capitales, blanc, ombre courte, 72–75 % de la hauteur (exemption de zone sûre : `formats-courts-verticaux.md §6.2`), mots clés en accent, **pop de 4 images, sortie sèche**, masqués pendant tout texte animé. Les mots sont posés par script (§16.3) depuis les temps du dérush validé, jamais les temps bruts de transcription (skill §4) ; retirer ceux qui tombent dans la durée d'un élément (§7) ; recouper si Cabezer retouche la timeline ; contrôler l'export (§15).

### 8.3 Pastille qui épouse son texte

Taille du tracé rectangle, puis position du calque de forme [valeurs testées avec un faux moteur ; `sourceRectAtTime(t, includeExtents)` est dans la doc] :

```
pad = 28;                                    // marge en px, valeur de départ
t = thisComp.layer("TXT_Etiquette");
r = t.sourceRectAtTime(time, false);
s = t.transform.scale;                       // la boîte ignore la transformation du calque
[r.width * s[0] / 100 + 2 * pad, r.height * s[1] / 100 + 2 * pad]
```
```
t = thisComp.layer("TXT_Etiquette");
r = t.sourceRectAtTime(time, false);
t.toComp([r.left + r.width / 2, r.top + r.height / 2])
```
`toComp(point)` convertit un point de l'espace du calque en espace composition [Doc lue]. Écrire `[w, h]` avec crochets [Extrait].

**Ancre centrée sur le texte** [T3 3:06–4:36] : sur le Point d'ancrage, `a = sourceRectAtTime(time, false); [a.left + a.width/2, a.top + a.height/2]` ; `top` va de la ligne de base au haut des lettres, sans descendantes. Rectangle aligné : `[a.width/-2 - a.left, a.height/-2 - a.top]` sur son ancre [5:38].

**Correction de la v1.** T3 fige la taille avec `sourceRectAtTime(2, true)`. La doc limite le second argument aux calques de **forme** et de **texte en paragraphe** (boîte du paragraphe) ; pour un texte ponctuel, c'est le **temps fixe** qui fige. À tester.

---

## 9. Formes, Trim Paths, caches de piste

### 9.1 Trim Paths

**Quand** : flèche, cercle de désignation, soulignement, trait de schéma (S, T, F). **Éviter** : tracé très long avec flou de mouvement. Calque de forme > Contenu > Ajouter > Tracés rognés (Trim Paths) [Extrait] ; animer **Fin** de 0 à 100 % avec easing ; Fin à 50 % puis Début à 50 % : la forme disparaît puis se redessine [T1 28:08–31:26] ; cascade de copies décalées de 2 images, rotations 90° puis 180°, échelles 150 % puis 130 % [T1 31:56]. Garder le texte séparé du tracé pour rester éditable.

**Surlignage de preuve (S)** : rectangle en Multiplier, échelle X de 0 à 100 % ancrée à gauche, 8 à 15 images ; sur un passage étranger, traduction française pendant le coup de feutre, dates non traduites [Skill §6]. Formes d'Illustrator [T2 0:36–5:57] : Créer des formes à partir des calques vectoriels (libellé à confirmer) ; trou entre formes : Simple Choker à −1 [8:33]. Posterize Time 12 i/s de T2 [14:54] est un choix de style, pas un défaut.

### 9.2 Caches de piste (track mattes)

**Quand** : révéler un texte à travers une forme, remplir un texte avec une vidéo.
- Depuis AE 23.0, **tout calque peut servir de cache à tout autre**, quelle que soit sa place [Doc lue] ; le cache est **masqué par défaut** [Extrait]. Colonne Cache de piste (TrkMat) : Alpha, Alpha inversé, Luma, Luma inversé ; bascule Interrupteurs/Modes par F4 (à confirmer) [Extrait].
- Script : `calque.setTrackMatte(autre, TrackMatteType.ALPHA)`, `removeTrackMatte()` ; `NO_TRACK_MATTE` est sans effet dans `setTrackMatte`. Pour un **calque de texte**, `trackMatteType`, `isTrackMatte`, `hasTrackMatte` sont déclarés inutilisés [Doc lue] : prendre une forme comme cache ou précomposer.
- Set Matte (libellé à confirmer) : alpha d'un autre calque ; T2 note qu'il faut rastériser le source en continu, point peu clair [13:51]. Le cache suit sa cible si on le lui parente.

**Réussite** : bords nets à 100 %, aucun contour parasite.

---

## 10. Expressions utiles

Une expression rend un élément autonome ou remplace un travail répétitif ; elle ne remplace pas les clés d'un mouvement simple. Alt/Option + clic sur le chronomètre l'ouvre.

**Confirmé dans la référence** [Doc lue] : `wiggle(freq, amp, octaves=1, amp_mult=0.5, t=time)` (freq en oscillations par seconde, amp dans l'unité de la propriété) ; `framesToTime(n)` ; `ease(t, tMin, tMax, v1, v2)` (vitesse 0 aux bornes), `linear`, `easeIn`, `easeOut` ; `nearestKey(t)` (`.index`, `.time`), `key(n)`, `numKeys` ; `valueAtTime`, `velocityAtTime` ; `loopOut("cycle" | "pingpong" | "offset" | "continue")` ; `previousKey`/`nextKey` (26.0). **`loopIn`/`loopOut` ne s'appliquent pas** à Source Text ni aux tracés. Tableaux : `add`, `sub`, `mul`, `div`, `clamp` ; les exemples officiels écrivent aussi `+` et `/` sur des tableaux.

Les codes ont passé un contrôle de syntaxe et de valeurs avec un faux moteur [Testé ici] ; **jamais exécutés dans AE** : tester sur copie, sur le plan réel.

**10.1 Secousse qui s'éteint (Position), D, gros moments seulement**
```
d = framesToTime(6);                         // 6 images (skill)
t = time - inPoint;
if (t >= 0 && t < d) {
  wiggle(20, 30 * (1 - t / d));              // amplitude de départ 30 px (base 1080), non sourcée
} else {
  value;
}
```
Forme « démarrer et arrêter un wiggle » de l'exemple officiel. Éviter un wiggle partout (skill §5.1).

**10.2 Retard (follow-through)** : `delay = effect("CTRL_Retard")(1); thisComp.layer("PILOTE").transform.position.valueAtTime(time - delay)` (forme de l'exemple officiel « traînée »). Ne pas parenter en plus : le déplacement doublerait.

**10.3 Décalage de liste stable**
```
step = thisComp.layer("CTRL_Liste").effect("CTRL_Decalage")(1);
d = (index - thisComp.layer("CTRL_Liste").index) * step;
ease(time - inPoint - d, 0, 0.25, 0, 100)    // opacité de 0 à 100 % en 0,25 s
```
Index relatif à un contrôleur, car `index` change si on réordonne. Alternative : Animation > Assistant de clés > Séquencer les calques [À vérifier], à refaire après réordonnancement.

**10.4 Oscillation amortie à volume constant** (échelle ; déclenchée après la **dernière** clé), adaptée de l'exemple officiel « échelle à chaque marqueur » [Doc lue] :
```
n = numKeys;
t = (n > 0) ? time - key(n).time : -1;
if (t < 0) {
  value;
} else {
  amp = 15; freq = 5; decay = 3.0;           // valeurs de l'exemple officiel, à régler
  f = (100 + amp * Math.sin(freq * 2 * Math.PI * t) / Math.exp(decay * t)) / 100;
  [value[0] * f, value[1] / f];              // largeur x f, hauteur / f : volume constant
}
```
Le produit largeur × hauteur reste 100 × 100 [Testé ici]. **Variante « inertie »** (Mike Murphy, T6) : trois paramètres amplitude, fréquence, décroissance ; Position, Échelle, Rotation, Opacité ; deux ou trois clés [0:30–1:32] ; contrôleurs Effet > Contrôles d'expression > Curseur (Slider Control), un par paramètre, pick-whip ; **piège : les valeurs repassent à zéro à la création des curseurs, retaper les originales** [4:07]. Son code est en description de vidéo, **non lu** ; forme reconstituée d'après `nearestKey` et `velocityAtTime` du doc [syntaxe testée] :
```
amp = 0.04; freq = 3.0; decay = 7.0;         // départ à régler
n = 0;
if (numKeys > 0) { n = nearestKey(time).index; if (key(n).time > time) n--; }
if (n > 0) {
  t = time - key(n).time;
  v = velocityAtTime(key(n).time - thisComp.frameDuration / 10);
  value + v * amp * Math.sin(freq * t * 2 * Math.PI) / Math.exp(decay * t);
} else { value; }
```
**Correction de la v1** : elle jugeait la division par `Math.exp` « débordante ». C'est inexact : diviser par `Infinity` donne 0 [Testé ici : `1/Math.exp(710)` vaut 0] et l'exemple officiel divise ; les deux écritures sont équivalentes. **Quand** : éléments ludiques validés, F et T. **Éviter** : D, P, textes longs. Par défaut : pas de rebond sans accord (§21).

**10.5 Écrasement-étirement selon la vitesse** : `sp = length(transform.position.velocity); s = clamp(sp / 2000, 0, 0.25); [100 * (1 + s), 100 / (1 + s)]` (diviseur et plafond à régler ; `velocity` est un tableau pour Position [Doc lue]). Mouvements horizontaux ; **éviter** en D et P.

**Réussite** : aucune alerte (bandeau jaune) ; comportement identique sur 3 durées d'élément.

---

## 11. Caméra 3D, profondeur de champ, parallaxe

**Quand** : S, F, P, T (skill §6 : extraits, affiches, façades, menus, tickets explorés en caméra 3D plutôt que cartes génériques). **Éviter** : D et tout mouvement décoratif (skill §6 point 11 et §7, décisions d’harmonisation D2).

**Exploration d'un document** : importer à 2× la composition au moins ; commutateur 3D du calque ; Calque > Nouveau > Caméra (libellé à confirmer) ; parenter la caméra à un nul `CAM_PILOTE` et animer le nul ; entre deux détails, pause nette (temps de lecture), déplacement de 8 à 15 images, aucune dérive ; deux vues (face, dessus) pour contrôler la profondeur [T8 2:34].

**Profondeur de champ** [T8 0:31–4:38] : calques en 3D, fond reculé (il rapetisse) ; nouvelle caméra 50 mm avec **Activer la profondeur de champ** ; Options de caméra : **Distance de mise au point**, **Ouverture**, **Niveau de flou** (réglé à part) ; ouverture plus grande = zone nette plus étroite ; animer la distance d'un calque à l'autre ; f-stop : Ctrl/Cmd+Maj+Y (à confirmer). Scripts : `cameraOption.focusDistance`, `aperture`, `blurLevel` [Doc lue]. T8 ne donne aucune valeur. Le journal de scripting ajoute en 26.3 les propriétés `FocusAreaWidth` et `NearFarBlurMultiplier`, « Advanced 3D seulement » [Doc lue] : moteur distinct de la méthode ci-dessus, non couvert par une source lue, GPU sollicité. **Plans filmés** : cette méthode vaut pour des calques créés dans AE ; flouter un plan réel modifie la prise, défaut = **non** (§21).

**Parallaxe 2.5D** [T9 1:01–3:01] : **au moins trois couches** (premier plan, plan médian, fond) en 3D, caméra créée, fond reculé et agrandi ; **déplacer d'abord la caméra de la moitié de l'amplitude de l'autre côté** pour découvrir deux fois moins de zones à recouvrir ; plan qui suit trop la caméra : le reculer. **Quand** : documents faits de plans naturels (affiche + fond + texte, ticket sur table). **Éviter** : photo de personnes ou de lieu réel dont il faut combler les trous. Le Tampon de duplication de T9 (flux 50 %, mode constant, Aligné désactivé, traits étendus à toute la durée [3:32–5:03]) sert à recouvrir des bords ; T9 s'en sert aussi pour « ajouter des pieds » à des personnages : **retouche de contenu sur photo réelle exclue sans accord, surtout en S et P**, idem Liquify ou marionnette sur une personne [8:05–11:39]. Wave Warp ou brume par Turbulent Displace [6:03, 13:41] : procéduraux, pas de l'IA, mais décoratifs : pas sans brief. La parallaxe est une animation graphique (AE) mais déplace tout le cadre alors que le skill veut un mouvement qui désigne un détail : en S et P, **pas de parallaxe sans accord** (§21).

**Réussite** : aucun bord vide ni plan « carton » ; le déplacement va du détail A au détail B sans revenir au centre.

---

## 12. Suivi, rotoscopie, incrustation

### 12.1 Suivi d'un point

Étiquette collée à un produit qui bouge (D, F, S si le brief le demande ; éviter si une coupe franche suffit) : Fenêtre > Suivi (Tracker), « Suivre le mouvement » [À vérifier] ; point à fort contraste, stable ; appliquer à un nul, parenter l'étiquette ; contrôler aux coupures. Suivi caméra 3D et Mocha AE : à confirmer dans les menus ; Mocha Pro est **payant**. Plan instable : `premiere-pro-avance.md §7 bis`.

### 12.2 Roto Brush : aide autorisée, résultat vérifié [T7]

1. Outil Roto Brush (Alt/Option+W, à confirmer). **Travailler dans la fenêtre du calque** (double-clic sur le métrage) : l'outil ne répond pas dans la composition [1:01]. Taille : Fenêtre > Pinceaux, ou Ctrl/Cmd + glisser.
2. Traits **verts (+)** sur le sujet, Alt/Option pour le **rouge (−)** ; Espace lance le calcul image par image ; une correction à pause n'affecte pas les images déjà calculées [1:32].
3. Cheveux et bords fins : **Affiner le bord**, blanc gardé, noir retiré [2:03] ; vues rayons X, bord alpha, superposition.
4. **Figer** une fois validé [2:33]. Contrôles d'effet : plume, Maj + bord pour resserrer, « Utiliser le flou de mouvement » [3:04].
5. **Vérifier** : aucun scintillement du cache sur 3 images consécutives, sur fond clair et foncé.

### 12.3 Incrustation sur fond uni, nettoyage

Placer Cabezer devant un document ou une capture (T, S, F ; pas en D) : Ultra Key et clé de luminance dans `premiere-pro-avance.md §8.4`. Côté AE : **Keylight** est fourni avec AE [Extrait], fond uni éclairé de façon homogène ; Roto Brush si le fond n'est pas uni ; bords adoucis, ombre courte. Interdits : suppression de fond en ligne, restauration générative des bords. Le papier plié de T10 (Keylight bleu puis vert) repose sur des fichiers tiers de licence non lue : **non utilisé** sans accord. Poussière sur l'objectif : masque et suivi manuels, jamais de Remplissage d'après le contenu sans accord.

---

## 13. Flou de mouvement

1. Activer le commutateur du calque **et** celui de la composition [T5 5:33].
2. Composition > Paramètres > Avancé : **angle d'obturation** (entier de 0 à 720 par script), **phase** (−360 à 360), échantillons par image (2 à 64, pour 3D classique, formes et certains effets), limite adaptative (16 à 256, mouvement 2D) [Doc lue pour les plages]. Défauts récents 180° et −90° (centre le flou) : [Extrait, **non confirmé**].
3. **Contradiction non tranchée** : un fil Adobe conseille une phase positive pour que le flou s'arrête sur la dernière clé. Garder les valeurs lues dans la composition et tester sur le premier élément (dernière image nette ou non).
4. **Quand** : D (pop, whips d'éléments), T. **Éviter** : étiquette de 8 px, longs textes à animateurs.

**Réussite** : le flou se voit à la vitesse maximale, jamais sur l'état final.

---

## 14. Passerelle Premiere, rendu, MOGRT

### 14.1 Choisir la voie

| Voie | Quand | Limites |
|---|---|---|
| **ProRes 4444 alpha** | Éléments finis (skill §5.1) : étiquette, prix, pop-up, sous-titres | Lourd ; refaire le rendu à chaque changement |
| **Dynamic Link** (Remplacer par une composition After Effects ; libellé à confirmer) | Plan à retoucher avec ses rushs | Lecture lente ; un clip déplacé casse le lien |
| **MOGRT** | Texte changé souvent dans Premiere | §14.3 ; à proposer, pas par défaut |

**Dynamic Link** [Cinecom] : clic droit > Remplacer par une composition After Effects ; rendre avec Entrée (ligne verte) ; figer par Rendre et remplacer, « clips individuels » ; **verrouiller le montage avant** ; alpha : ProRes 4444, pas le DNxHD de cette vidéo ancienne.

### 14.2 Module de sortie ProRes 4444 alpha

Ajouter à la file de rendu (Cmd+M à confirmer ou script, §16.6) ; module QuickTime, Apple ProRes 4444, canaux **RVB + alpha**, profondeur la plus haute [À vérifier] ; **le Format ne se règle pas par script** (lisible, non modifiable [Doc lue]) : créer le module une fois à la main puis l'enregistrer comme modèle `ProRes4444_alpha_Cabezer` (`saveAsTemplate` existe par script). Alpha : partir de **Straight (Unmatted)** et tester. Rendre depuis AE, pas Media Encoder (alpha mal conservé selon des fils [Extrait]) ; repli : séquence PNG alpha. Nom `<Sujet>_<Element>_v<NN>.mov`, dossier `03_RENDUS`. Dans Premiere, vérifier l'alpha sur fond clair **et** foncé ; Clip > Modifier > Interpréter le métrage change l'interprétation [À vérifier].

### 14.3 Essential Graphics et MOGRT

- Seules les propriétés exposées sont modifiables dans Premiere. **Types exposables** [Doc lue] : case à cocher, couleur, curseur numérique à valeur unique, Source Text. Position, échelle, masque (multi-valeurs) ne le sont donc pas directement : cela explique les clés « perdues » des forums [Extrait]. Contournement à tester : curseur relié par expression.
- API [Doc lue] : `propriété.canAddToMotionGraphicsTemplate(comp)`, `addToMotionGraphicsTemplate(comp)`, `addToMotionGraphicsTemplateAs(comp, nom)`, `comp.motionGraphicsTemplateName`, `comp.exportAsMotionGraphicsTemplate(écraser, dossier)` ; dossier par défaut macOS `/Users/<nom>/Library/Application Support/Adobe/Common/Motion Graphics Templates/` ; enregistrer le projet avant l'export.
- Texte : n'exposer que Source Text ; remplacement de média incompatible avec un calque rastérisé en continu [Extrait]. Tester chaque modèle ; éviter en D (`premiere-pro-avance.md §8.3`).

### 14.4 Performances

Rendu multi-image actif par défaut depuis AE 22.0 [Extrait]. **Deux réglages de sens différents** : le curseur des préférences réserve 0 à 70 % du CPU aux autres applications (10 % par défaut [Extrait]) ; `app.setMultiFrameRenderingConfig(mfr_on, max_cpu_perc)` fixe le **maximum utilisé** (1 à 100) pour le prochain rendu seulement, 100 si `mfr_on` est faux [Doc lue]. Gains annoncés (1,2 à 4×, table Adobe de 2022) : ne pas les promettre.

**Réussite** : le `.mov` s'importe à la bonne cadence, sans média hors ligne, alpha propre, et passe le §15.

---

## 15. Contrôler un rendu

Commandes exécutées sur des ProRes 4444 alpha de test [Testé ici] ; elles signalent des cas à revoir. Seuils de noir, figement, niveaux, loudness : `organisation-livraison-qc.md §6.3`.

1. **Identité** : `ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=codec_name,profile,pix_fmt,width,height,r_frame_rate,nb_read_frames -of default=nw=1 element.mov`. Attendu `prores`, `4444`, `yuva444p12le` (le « a » = alpha ; sans alpha `yuv444p12le`), taille et cadence de la séquence, images = durée × cadence. `ffmpeg -i element.mov -vf alphaextract -frames:v 1 x.png` échoue sans alpha.
2. **Courbe mesurée** : `ffmpeg -v info -i element.mov -vf "alphaextract,format=gray,bbox=min_val=128,metadata=print:file=-" -f null - 2>&1 | grep -E "lavfi.bbox.(w|h)="`. Sur le test (pop 0 → 60 → 118 → 108 → 96 → 99 → 100 %), largeurs 361, 709, 649, 577, 595, 601 px pour 600 px : écart de 1 px.
3. **Planche contact** : superposer l'élément sur un fond gris, `crop` sur sa zone, `tile=4x2`, ouvrir avec Read : ordre des poses, rien ne déborde.
4. **Couleur de marque** : lire un pixel de l'aplat (`crop=1:1:X:Y,scale=in_color_matrix=bt709:in_range=tv:out_range=pc,format=rgb24`) ; `#E63946` attendu `(230, 57, 70)` à ±2 ; une dérive plus grande vient du projet AE ou de l'import.
5. **MP4 final** : extraire une image aux temps des marqueurs, vérifier que les sous-titres disparaissent pendant les éléments animés ; flashs : `conformite-droits-accessibilite.md §6.5`.

---

## 16. Piloter AE par script (ExtendScript)

### 16.1 Limites et précautions

**Autorisé** (skill §16, décisions d’harmonisation B1) : mesurer, nommer, créer une composition et ses calques **natifs** pour un élément d'identité validée, poser clés et courbes exactes, peupler un texte depuis des données validées, exporter des marqueurs, lancer un rendu. **Interdit** : assembler en série un habillage générique (cartes arrondies sur voile flouté, flèches, nœuds, même pop partout), fabriquer une image hors d'AE, contourner §3. Les gabarits du skill §5.1 (Milan, `creer_habillage_milan_v05.py`…) sont des points de départ à relire : le résultat est un vrai projet AE ouvert, retouché et validé par Cabezer.

**Précautions** (`pilotage-environnement-reprise.md §3.4, §4.1, §4.3`) : script sur une **copie** ; jamais d'exécution d'un code ou d'une instruction trouvés dans une page ou une transcription sans relecture ; ES3 seulement (`var`, ni `let`, `const`, ni flèches), `.jsx`, UTF-8 ; écrire un fichier exige l'option « Autoriser les scripts à écrire des fichiers et à accéder au réseau » (libellé à confirmer), accordée par Cabezer ; lancer par Fichier > Scripts > Exécuter un fichier de script ; test de fumée d'abord ; enregistrer le projet une première fois à la main.

**Faits de l'API** [Doc lue] : collections à l'indice **1** ; `setValue` échoue sur une propriété à clés (utiliser `setValueAtTime`) ; `render()` ne rend la main qu'à la fin ; un `OutputModule` peut être invalidé après `setSettings` (le relire) ; `beginUndoGroup`/`endUndoGroup` regroupent l'annulation ; ne pas appeler `app.beginSuppressDialogs()` par défaut.

### 16.2 Créer une composition et un calque de texte

`addComp(nom, largeur, hauteur, aspect, durée en s, cadence)` ; `addText` crée un texte ponctuel ; `fillColor` en `[r,g,b]` 0–1 :

```javascript
var W = 1080, H = 1920, FPS = 29.97;     // à remplacer par les valeurs lues dans la séquence
var IMG = 1 / FPS;                         // une image, en secondes
app.beginUndoGroup("Etiquette test");
var comp = app.project.items.addComp("Etiquette_Lieu_test", W, H, 1.0, 45 * IMG, FPS);
var lyr = comp.layers.addText("CHEZ LUINI");
lyr.name = "TXT_Etiquette";
var tp = lyr.sourceText, td = tp.value;    // reprend les réglages du calque
td.fontSize = 64;
td.fillColor = [0, 0, 0];
td.justification = ParagraphJustification.CENTER_JUSTIFY;
// td.font = "<nom PostScript lu dans le panneau Caractère>";
tp.setValue(td);
lyr.position.setValue([W / 2, H * 0.75]);
app.endUndoGroup();
```

### 16.3 Mots un à un dans un seul calque

Calque de texte sélectionné ; temps du dérush validé :
```javascript
var tp = app.project.activeItem.selectedLayers[0].sourceText;
var mots = [["BREF", 0.00], ["C'EST", 0.35], ["PARTI", 0.60]], i, td;
app.beginUndoGroup("Mots un a un");
for (i = 0; i < mots.length; i++) {
  td = tp.value; td.text = mots[i][0];     // garde police, taille, couleur
  tp.setValueAtTime(mots[i][1], td);
}
app.endUndoGroup();
```

### 16.4 Clés Bézier avec influence exacte

Le nombre d'objets `KeyframeEase` de `setTemporalEaseAtKey` est **2 pour TwoD, 3 pour ThreeD, 1 pour tout autre type, Position (spatiale) comprise** [Doc lue : cela tranche le doute de la v1] ; influence de 0,1 à 100 ; `setInterpolationTypeAtKey(k, KeyframeInterpolationType.BEZIER)` d'abord. L'influence d'**arrivée** règle la clé qui reçoit le mouvement, celle de **départ** la clé qui le lance. Glisse de 8 px (base 1080) et opacité en 4 images :
```javascript
function nEase(p) {
  var t = p.propertyValueType;
  return t == PropertyValueType.TwoD ? 2 : (t == PropertyValueType.ThreeD ? 3 : 1);
}
function poser(p, temps, valeurs, infArrivee, infDepart) {
  var i, k, a, b;
  for (i = 0; i < temps.length; i++) p.setValueAtTime(temps[i], valeurs[i]);
  for (k = 1; k <= p.numKeys; k++) {
    p.setInterpolationTypeAtKey(k, KeyframeInterpolationType.BEZIER);
    a = []; b = [];
    for (i = 0; i < nEase(p); i++) { a.push(new KeyframeEase(0, infArrivee)); b.push(new KeyframeEase(0, infDepart)); }
    p.setTemporalEaseAtKey(k, a, b);
  }
}
var comp = app.project.activeItem;
if (comp instanceof CompItem) {
  var IMG = comp.frameDuration, lyr = comp.layer("TXT_Etiquette");
  var v = lyr.position.value, z = v[2] || 0;
  app.beginUndoGroup("Courbes etiquette");
  poser(lyr.position, [0, 4 * IMG], [[v[0], v[1] + 8, z], [v[0], v[1], z]], 75, 25);
  poser(lyr.opacity, [0, 4 * IMG], [0, 100], 75, 25);
  app.endUndoGroup();
}
```
75 et 25 sont des valeurs de départ non sourcées. Logique rejouée avec un faux moteur d'API [Testé ici] : bon nombre d'objets d'easing pour Position, Opacité, Échelle. **Pop** : même `poser` sur `calque.scale` (ThreeD) avec `[0,0,100]`, `[118,118,100]`, `[96,96,100]`, `[100,100,100]` aux images 0, 2, 4, 6 (positions indicatives) et 33,33 des deux côtés comme valeur neutre [Extrait].

### 16.5 Exporter les marqueurs de SFX

```javascript
var comp = app.project.activeItem;
if (comp instanceof CompItem && app.project.file) {
  var mk = comp.layer("SFX_MARQUES").marker, k, txt = "image;commentaire\n";
  for (k = 1; k <= mk.numKeys; k++) txt += Math.round(mk.keyTime(k) / comp.frameDuration) + ";" + mk.keyValue(k).comment + "\n";
  var f = new File(app.project.file.parent.fsName + "/marques_" + comp.name + ".csv");
  f.encoding = "UTF-8";
  if (f.open("w")) { f.write(txt); f.close(); alert(f.fsName); } else { alert("Ecriture refusee : option des scripts."); }
}
```
Poser un marqueur : `calque.marker.setValueAtTime(t, new MarkerValue("swoosh"))` [Doc lue]. Déplacer le CSV vers `Suivi/`.

### 16.6 Modèle de module de sortie et file d'attente

Ajoute la composition active à la file, applique un **modèle de module de sortie existant**, rend :
```javascript
var MODELE = "ProRes4444_alpha_Cabezer";     // à créer une fois à la main (§14.2)
var comp = app.project.activeItem;
if (comp instanceof CompItem && app.project.file) {
  var rqi = app.project.renderQueue.items.add(comp);
  var om = rqi.outputModule(1), trouve = false, i;
  for (i = 0; i < om.templates.length; i++) { if (om.templates[i] == MODELE) trouve = true; }
  if (!trouve) { rqi.remove(); alert("Modele absent. Disponibles : " + om.templates.join(" | ")); }
  else {
    om.applyTemplate(MODELE);
    om.file = new File(app.project.file.parent.fsName + "/" + comp.name + "_v01.mov");
    app.project.renderQueue.render();        // bloquant jusqu'à la fin
  }
}
```
`outputModule(1)` : premier module à l'indice 1. Réglages de rendu : lister `rqi.templates` avant `rqi.applyTemplate(nom)`, le nom dépend de la langue. `queueInAME(false)` envoie la file à Media Encoder sans la lancer ; pour le ProRes 4444 alpha, rendre depuis AE. Contrôle de projet en lecture seule : parcourir `app.project.item(i)` (indice 1), lister taille, cadence, durée des `CompItem` et les éléments avec `footageMissing`, comparer à la séquence. Un rendu n'est validé qu'après §15.

### 16.7 `aerender`

Sources : extraits Adobe et forums [Extrait], aucune page officielle ouverte.
1. Trouver l'exécutable (`find /Applications -maxdepth 4 -name aerender -type f`), ne pas le supposer.
2. **`aerender -help` d'abord**. L'exemple Adobe combine `-project`, `-comp`, `-s`, `-e` (images de début et de fin), `-RStemplate`, `-OMtemplate`, `-output` ; par défaut `aerender` démarre **sa propre instance** d'AE, `-reuse` utilise l'instance ouverte (erreur d'événement Apple -1712 signalée sur macOS récent) ; `-mem_usage` non confirmé.
3. Forme à tester : `aerender -project <fichier.aep> -comp "<nom>" -s 0 -e 6 -OMtemplate "ProRes4444_alpha_Cabezer" -output <fichier.mov>` ; un fil signale qu'un modèle personnalisé peut ne pas être chargé : tester.
4. Rendre quelques images dans `Exports/Brouillons/`, contrôler (§15), puis le rendu complet. Journaliser chaque script ou commande : chemin, empreinte `shasum -a 256`, version d'AE, résultat (`pilotage-environnement-reprise.md §4.1`).

---

## 17. Matrice par famille

| Technique | D | F | S | P | T | H |
|---|---|---|---|---|---|---|
| Pop, étiquette, prix, note, CTA (§7) | oui | oui | rare | non | avec accord | brief |
| Sous-titres animés AE (§8.2) | oui | oui | oui | oui | oui | oui |
| Révélation mot à mot (§8.1) | non | oui | titres de concept | non | oui | brief |
| Trim Paths, surlignage (§9) | rare | oui | oui | oui | oui | oui |
| Caméra 3D sur documents (§11) | non | oui | oui | oui | oui | brief |
| Profondeur de champ sur calques AE | non | rare | rare | non | oui | brief |
| Parallaxe 2.5D | non | avec accord | avec accord | avec accord | non | brief |
| Rebond, écrasement-étirement (§10.4-5) | non | avec accord | non | non | avec accord | brief |
| Suivi attaché au plan (§12) | avec accord | oui | oui | rare | oui | brief |
| Roto Brush, aide vérifiée | rare | oui | oui | oui | oui | brief |
| Flou de mouvement (§13) | oui | oui | oui | léger | oui | oui |

**Imposé par famille** : skill §6 (jamais « Cabezer Story » écrit en S ; pas d'affiche générée en P). T : Liquid Glass sans fiche = non appliqué ; verre par effets natifs, repères non validés [À vérifier] : calque de réglage + cache de forme + flou, Décalage turbulent, 16 bpc ; barres et compteurs : `styles-food-et-tech.md §6`.

---

## 18. Plugins gratuits et payants

Gratuits uniquement (skill §17, décisions d’harmonisation B3) ; téléchargé, installé, en essai, fonctionnel sont des états distincts. **Inclus dans AE** : éditeur de graphiques, expressions, animateurs, Trim Paths, caméra 3D, Suivi, Mocha AE, Keylight, rendu multi-image, flou de mouvement, Roto Brush. **Payants, sans accord non intégrés** : Essential Namer (aescripts), Mocha Pro, Video Copilot (Element 3D, Shockwave…), formations School of Motion et Skillshare. **Licence non lue, traités comme payants** : fichier ECAbrams (Gumroad), fichiers d'expressions de Mike Murphy, paquet de papier plié de T10. Un preset gratuit n'autorise pas son audio, ses polices ni ses images ; consigner dans `Suivi/licences.csv`.

---

## 19. Erreurs de débutant → réflexes de pro

1. Régler en secondes à l'œil → compter en images, sur la cadence de la séquence.
2. Composition d'une autre taille ou cadence que la séquence → les relire dans Premiere.
3. Tout en linéaire ou tout en Easy Ease par défaut → courbes travaillées (§6), linéaire seulement pour une vitesse constante voulue.
4. Pop et shake partout, plusieurs éléments qui bougent ensemble → vraies récompenses seulement (2 à 4 pops par vidéo), un élément principal.
5. Valeur de tutoriel appliquée telle quelle → valeur de départ, réglée sur le plan réel.
6. Pastille réglée à la main → liée au texte (§8.3). Index de calque pour décaler une liste → index relatif (§10.3).
7. Précomp dupliquée pour la rendre différente → dupliquer la composition source.
8. Alpha rendu via Media Encoder → rendu AE direct, alpha testé sur fond clair et foncé. Clip déplacé après Dynamic Link → verrouiller le montage avant.
9. Croire que `/ Math.exp(...)` « déborde » → les deux écritures sont valides (§10.4).
10. Roto ou remplissage par IA sans demander → §3. Retouche de contenu sur photo réelle → exclue (§11).
11. Script lancé sur le projet de travail → copie, test de fumée, journal (§16.1).
12. Mauvais nombre d'objets `KeyframeEase` → 1 pour Position et valeurs simples, 3 pour l'échelle (§16.4).
13. Confondre le curseur de CPU réservé et le paramètre de script → deux sens opposés (§14.4).
14. Flash en plein cadre sans compter → limite de `conformite-droits-accessibilite.md §6`.
15. Animation déclarée finie après le rendu → contrôles §15, puis revue du MP4 final.

---

## 20. Liste de contrôle

**Avant le rendu** : version AE lue, projet enregistré sous une nouvelle version, script lancé sur copie · taille et cadence = séquence, durée = élément + marge · polices, emojis, couleurs du skill · easing travaillé (ou vitesse constante signalée), timing en images, un seul élément principal · texte éditable, pastilles liées, contrôleurs nommés, sous-titres en voie unique · marqueurs d'attaque posés pour chaque SFX · flashs comptés et export testé (`conformite-droits-accessibilite.md §6`) · aucun outil génératif, outil « à demander » non employé · plugin ou script tiers gratuit, licence consignée.

**Après le rendu** : `ffprobe` (codec, `yuva444p12le`, taille, cadence, images) · courbe mesurée ou planche conforme · couleur de marque à ±2 · import Premiere à la bonne cadence, alpha propre sur fond clair et foncé, aucun hors ligne · sous-titres masqués pendant l'élément, SFX calé sur l'attaque · visionnage à vitesse réelle sur téléphone · `.aep` et sources conservés, état noté (appliqué / contrôlé / validé).

---

## 21. Décisions à demander à Cabezer

Défaut en attendant sa réponse entre parenthèses.

1. **Object Matte** permis comme aide vérifiée ? (Non, ne pas l'utiliser.)
2. **Taille des éléments rendus** : taille de la séquence (2160 × 3840 pour Milan, lourd) ou FHD ? (Taille de la séquence lue, durée la plus courte.)
3. **Retouche de contenu sur photo réelle** (tampon de duplication, Liquify, marionnette sur une personne) : jamais ou cas par cas ? (Exclue, surtout S et P.)
4. **Profondeur de champ ou flou simulé sur plans filmés** (S, P) ? (Non ; calques créés dans AE seulement.)
5. **Parallaxe 2.5D** sur photos et documents en S et P ? (Non sans accord.)
6. **Rebond d'inertie et écrasement-étirement** : jamais ou F et T ? (Jamais sans accord.)
7. **Interface d'AE en anglais** ? (Non, rien n'est changé.)
8. **Fiche Liquid Glass** à fournir avant toute animation tech. (Aucune animation T.)
9. **MOGRT** pour changer le texte dans Premiere ? (Non, rendus alpha.)
10. **Papier plié (T10) et fichiers d'expressions tiers (T6)** : accord et licence ? (Non utilisés.)
11. **Repli sans AE** pour les sous-titres (« repli non animé ») ? (Non.)

---

## 22. Sources étudiées

**Transcriptions lues en entier** (YouTube, minutages cités dans le texte)
- T1 School of Motion (Joey), « Intro to Animation Curves in After Effects », 27/06/2017, 37:35, https://www.youtube.com/watch?v=AG19fyRcOkA — graphe, easing, rebond à la main (24 i/s), Trim Paths.
- T2 Ben Marriott, « Impossible Geometry in After Effects », 10/07/2019, https://www.youtube.com/watch?v=8Xhiffa4wq8 — formes, précomps, boucle, Set Matte.
- T3 ECAbrams, « SourceRectAtTime() Revisited », https://www.youtube.com/watch?v=In4miXUdxko — boîte de texte, ancre ; son `true` est corrigé par la doc (§8.3).
- T4 Jake In Motion, « You NEED to understand spaces in After Effects », https://www.youtube.com/watch?v=gSq19gpWwSU — espaces et `toComp` ; principe seulement.
- T5 SonduckFilm (Josh Noel), « 3 Kinetic Typography Techniques in After Effects », 02/12/2019, https://www.youtube.com/watch?v=UnK5lGmadSs — animateurs de texte, Basé sur Mots.
- T6 Mike Murphy, « How To Use Inertial Bounce Expression in After Effects », https://www.youtube.com/watch?v=dZML8QkhYmc — méthode des curseurs ; code en description, **non lu**.
- T7 Adobe Video × Film Riot, « Learn How to Rotoscope in After Effects in Under Four Minutes », 01/08/2024, https://www.youtube.com/watch?v=eoOIrdb_0ko — Roto Brush 3.0.
- T8 Holmes Motion, « Depth of Field (DOF) in After Effects in 5 MINS », https://www.youtube.com/watch?v=uL1-x4mOrFQ — caméra, profondeur de champ.
- T9 Academy Of Edits, « 4 steps to animate your photos in after effects, 2.5D parallax », https://www.youtube.com/watch?v=CjUeDBbdG_o — parallaxe, déformations (retouche de contenu exclue).
- T10 chaîne non identifiée, « EASIEST Paper Fold-Out animation in After Effects », https://www.youtube.com/watch?v=yu1ZN0-FAaQ — transcription automatique pauvre ; matériel tiers, non retenu.
- Cinecom.net (Jordy), « Premiere Pro + After Effects Dynamic Link », https://www.youtube.com/watch?v=8SKZUuZkE08 — lue en entier, ancienne.

**Documentation lue en partie** (sources Markdown docsforadobe sur GitHub ; jamais exécutée)
- Guide de scripting After Effects : https://github.com/docsforadobe/After-Effects-Scripting-Guide (ItemCollection, CompItem, LayerCollection, AVLayer, Property, KeyframeEase, RenderQueue, RenderQueueItem, OutputModule, Application, Project, TextDocument, noms de correspondance, journal).
- Référence des expressions : https://github.com/docsforadobe/After-Effects-Expression-Reference (Interpolation, Property, Key, Layer Space Transforms, Time Conversion, Vector Math, Examples, journal).
- Guide ExtendScript, objet `File` : https://github.com/docsforadobe/Javascript-Tools-Guide. Typages : npm `types-for-adobe` 7.2.6 (signatures seulement).

**Contrôles exécutés ici** : ffmpeg 6.1.1, Node 22, Python (ProRes alpha, `bbox`, couleur, poids, `Math.exp`, syntaxe, faux moteur d'API). Aucune exécution dans AE.

**Extraits de recherche seulement** (Adobe refusé par le proxy) : Adobe, rendu automatisé https://helpx.adobe.com/en/after-effects/using/automated-rendering-network-rendering.html ; vitesse entre clés https://helpx.adobe.com/ca/after-effects/desktop/animate-in-after-effects/speed-between-keyframes/speed.html ; Roto Brush https://helpx.adobe.com/ca/after-effects/desktop/roto-brush-and-refine-matte/roto-brush/roto-brush-refine-matte.html ; rendu multi-image https://helpx.adobe.com/after-effects/desktop/render-and-export/multi-frame-rendering/multi-frame-rendering.html ; track mattes https://helpx.adobe.com/after-effects/using/track-mattes-and-traveling-mattes.html. Adobe Community et Creative COW (Easy Ease 33 %, flou de mouvement, alpha, `-reuse`, MOGRT ; Range Selector https://community.adobe.com/t5/after-effects-discussions/ae-s-text-tool-range-selector-visualizer-video-logic-table/td-p/15334792). ProVideo Coalition https://www.provideocoalition.com/cmg_hidden_gems_chapter_11_all_about_track_mattes/ ; aejuice https://aejuice.com/blog/dynamic-text-box-after-effects  ; TechCrunch (Remplissage d'après le contenu, 2019) https://techcrunch.com/2019/04/03/adobe-brings-content-aware-fill-for-videos-to-after-effects ; Wikipedia, douze principes https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation.

**Non lues** : pages directes helpx.adobe.com et community.adobe.com, School of Motion, motionscript.com, sites compilés docsforadobe (lus via GitHub). YouTube : 3 tentatives sur 6 refusées ; non transcrites : Jake In Motion (`7pOCtlrrE3Y`), School of Motion (`mEmRHw4p4_A`), Ben Marriott (`rsW4fwscwKI`). *The Animator's Survival Kit* : titre seulement.
