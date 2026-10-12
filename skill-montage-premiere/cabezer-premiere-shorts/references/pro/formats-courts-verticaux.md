# Formats courts verticaux (TikTok, Reels, Shorts) — fiche de référence 2025–2026

Fiche rédigée le 12/10/2026, harmonisée avec `../decisions-harmonisation.md` de la passe 2. Elle sert à piloter Premiere et After Effects (AE) sur le Mac de Cabezer et complète le skill `cabezer-premiere-shorts` sans le modifier. Pour Premiere (proxys, multicam, export, XML), lire `premiere-pro-avance.md` ; pour le récit et le rythme, `fondamentaux-montage-narratif.md` ; pour l'environnement et les raccourcis, `pilotage-environnement-reprise.md`.

## Quand lire cette fiche

Lire cette fiche avant tout montage ou toute déclinaison **vertical 9:16 de moins de 3 minutes** : dégustation TikTok/Reels/Shorts, Short tiré d'une vidéo longue (food long, Story, tech, films/séries), hook, sous-titres animés, recadrage 16:9 → 9:16, zones sûres, export vertical, contrôle du MP4. Ne pas la lire pour une vidéo longue horizontale (voir `retention-youtube-long.md`).

**Hiérarchie (skill §1) : brief de Cabezer → règles du skill → fiches → tutoriels.** Cette fiche est au troisième niveau ; `../decisions-harmonisation.md` priment sur elle. Un chiffre de tutoriel est une **valeur de départ**, jamais une règle. Chaque technique dit quand l'utiliser, quand l'éviter et pour quelles familles : **D** dégustation · **F** food long · **S** Cabezer Story · **P** films/séries (PRISME) · **T** tech · **H** hors familles.

## Statut de vérification (à lire avant d'appliquer un chiffre)

- Les procédures Premiere/AE viennent de **8 transcriptions lues en entier** et de **tests locaux** ffmpeg. L'aide officielle d'Adobe n'a pas pu être lue (helpx.adobe.com refusé par le proxy).
- La syntaxe des expressions et scripts AE a été relue dans la documentation communautaire docsforadobe (GitHub), sans exécution dans AE.
- Tout chiffre de **zone sûre, durée de plateforme, impact statistique, prix de plugin** est « à vérifier » et ne sert jamais de règle.
- Lire la version de Premiere et d'AE avant toute procédure. Un libellé non lu à l'écran est marqué « libellé à confirmer ». Aucun raccourci n'est utilisé tant qu'il n'a pas été lu dans Raccourcis clavier ; à défaut, passer par le menu (`pilotage-environnement-reprise.md`). Aucune version ni date de sortie n'est affirmée comme certaine.
- **Niveaux de preuve :** [Skill] règle de Cabezer · [Tuto] transcription lue · [Doc lue] documentation communautaire lue · [Test] commande exécutée en local (ffmpeg 6.1 ; mêmes options sous macOS) · [Calcul] arithmétique · [Extrait] résumé de recherche ou presse, page non ouverte · [À vérifier].

## Sommaire

1. Hook (0–3 s) · 2. Structure, boucle et fin · 3. Rythme, punch-ins, J/L-cut, jump cut · 4. Sous-titres animés · 5. Son · 6. Format vertical : zones sûres, recadrage · 7. Export et contrôle du MP4 · 8. Plateformes · 9. Dégustation · 10. Mesurer · 11. Outils : IA, plugins · 12. Erreurs de débutant → réflexes de pro · 13. Liste de contrôle · 14. Décisions à demander à Cabezer · 15. Sources étudiées

---

## 1. Hook (0–3 s)

### 1.1 Ce que le hook doit faire

Le hook est le premier plan qui annonce un enjeu, une question ou une promesse, **compris sans le son** : beaucoup de spectateurs défilent son coupé (Adobe Video, 0:00) et la décision de rester se prend en un à trois secondes [Tuto]. Le skill pose déjà : produit ou bouchée dans la première seconde, texte d'accroche lisible dès 0,2 s, son dès la première image, deux changements de plan ou de cadre dans les 3 premières secondes (skill §5.2).

**Trois tests avant de valider un hook (toute famille) :**

1. **Son coupé.** Regarder les 3 premières secondes sans le son. Critère : une phrase décrit ce qu'on a compris (sujet et enjeu).
2. **Titre-miniature** (Jenny Hoyos) : l'image seule avec son texte pourrait-elle être la miniature d'une vidéo longue qui donne envie de cliquer ? Pour **F, S, T, P**. En **D** : « on voit le produit et on veut le goûter ».
3. **Lisibilité orale** : la phrase d'accroche se comprend à la première écoute, courte, un seul concept.

### 1.2 Hook d'une dégustation : le sien d'abord, noté ensuite

Le skill demande son hook à Cabezer à chaque dégustation (§5). Séquence qui prime sur toute grammaire de genre :

1. Noter **son hook choisi** avec le barème du skill §5.2 et donner la note.
2. Note **sous 8** : retravailler jusqu'à 8 (consigne de Cabezer). Si son hook l'empêche, **son choix prime** : livrer avec la note réelle et proposer **au plus deux variantes**, son hook restant une option. Limite de deux itérations : question ouverte (défaut : pas de limite).
3. Les idées d'autres grammaires (un seul axe, boucle ouverte, écart de curiosité) ne s'appliquent qu'après validation par le barème.
4. Mode autonome (skill §1) : hook = son hook habituel, noté ; validation consignée « en attente ».

### 1.3 Boucle ouverte

Poser une question et ne pas la fermer trop vite (heyDominik, 1:00–1:31 ; Hoyos, 8:39–9:09 [Tuto]). Le texte d'accroche **apporte** une question ou une tension ; il ne répète pas la voix.

- **Quand** : F, S, T, P, déclinaisons en Short ; hook agressif de D fait d'extraits de rushs.
- **Éviter** : masquer ou flouter le produit ou la bouchée en D (skill : produit ou bouchée dès la 1re seconde, pas de bouchée tronquée). Un texte vague (« Qui se reconnaît ? ») ou qui double la parole (skill §6, Story).

### 1.4 Contexte dès la première image

Une phrase qui démarre sans contexte laisse le spectateur sans repère (heyDominik, 2:01–2:32 [Tuto]). Ajouter le contexte **en une ligne** : lieu, enjeu, produit. En D, c'est l'étiquette « lieu » du hook, par exemple « 19h30 · Luini ferme à 20h » [Skill §5]. Son usage d'écriture prime ; rester cohérent dans une vidéo (§4.3).

### 1.5 Recette AE d'un hook texte + image (sans IA, sans gabarit générique)

**Quand** : hook de F, S, T, P ou H qui met un texte en avant sur un plan existant. **Éviter** en D si le texte cache la bouchée ou le produit : utiliser l'étiquette du skill (§5.1). Procédure déduite des gestes de Joseph (8:08–9:10), **[À vérifier] dans AE** :

1. Composition 1080 × 1920, cadence de la séquence Premiere (la lire).
2. Importer le vrai plan ou la vraie capture : aucune image générée, aucun détourage en ligne.
3. Pour isoler le texte sans cacher le sujet : calque de réglage sous le texte, Luminosité/Contraste (baisser) et Flou gaussien (départ : 20 à 30), masque ellipse inversé à plume large. **Jamais de flou sur le visage ni le produit.**
4. Entrée du texte : glissement court + opacité 0 → 100 en 4 à 6 images, courbes de facilité Bézier (skill §7). Ombre courte et nette (skill §5.1).
5. Rendre en ProRes 4444 alpha ; caler dans Premiere.

**Critère** : la première image affichée contient déjà le texte lisible et le sujet ; le texte reste hors de la boîte du §6.2 ; test du son coupé réussi.

### 1.6 Mesurer le hook

Compter les changements de plan ou de cadre dans les 3 premières secondes **sur la timeline** avec `lister-clips.jsx` (lecture seule, décrit une fois dans `organisation-livraison-qc.md`, section scripts ; non testé dans Premiere tant que le test n'est pas consigné). Une coupe compte seulement si elle change de rush ou de cadre. Contre-vérification sur le MP4 : détection de scène de ffmpeg (`organisation-livraison-qc.md §6`), qui rate un punch-in 100 → 115 % [Test] : contrôle, pas note. Lisibilité de la première image : planche du §7.2.

### 1.7 Photosensibilité du hook

Un hook agressif enchaîne extraits rapides, flashs blancs et whips. Avant de le valider, appliquer `conformite-droits-accessibilite.md §6` (seuil, décompte, contrôle, procédure) ; cette fiche ne répète pas le seuil. Geste propre au hook : compter dans la même seconde les flashs de l'étiquette « intérieur » ou de la note et les coupes très contrastées ; espacer ou retirer le flash plutôt que baisser son opacité sans retester.

### 1.8 Ce qu'il ne faut pas reprendre

- Le « premier plan réaliste » généré par IA (heyDominik) : interdit par défaut (skill §16).
- Le remplissage génératif pour effacer un sous-titre : seulement sur demande explicite de Cabezer ; par défaut, corriger la taille ou la position du texte.

---

## 2. Structure, boucle et fin

### 2.1 Schéma court (F, S, T, P et leurs Shorts)

D'après Jenny Hoyos (20:25–25:33) [Tuto] : hook (≤ 3 s) → amorce de ce que la vidéo tient (≤ 3 s) → relance sans « on commence » → développement par changements de situation (« mais » / « donc ») → chute ou verdict, puis fermeture de la boucle.

**Quand** : récit court, Short tiré d'une Story ou d'un food long. **Éviter en D** : la dégustation a sa structure validée (arrivée, commande, produit, bouchée, verdict, appel au commentaire, skill §5) ; ne pas imposer d'amorce.

### 2.2 Écrire la fin en premier

Hoyos écrit la dernière phrase avant de tourner (24:31–25:33), ce qui rejoint « ouvrir une boucle au début, la refermer à la fin » (skill §4). **Au montage** : repérer d'abord la phrase de chute dans les rushs, puis construire le hook pour qu'il y renvoie. Réordonner des prises est permis ; retirer un faux départ pour garder ce que Cabezer voulait dire aussi ; jamais de collage qui crée une affirmation qu'il n'a pas faite ni change le sens.

### 2.3 Fin de la vidéo

Retirer la dernière seconde d'un Short est passé de 83 % à 88 % de rétention chez Hoyos (7:08–7:38) : anecdote isolée de 2023, non généralisable [Tuto]. À retenir : une seconde morte coûte cher en format court.

- **D** : skill §4, coupe juste après le dernier mot entièrement audible. Garder l'appel au commentaire entier, avec le mot prononcé, et couper après l'extinction réelle de la voix. Aucun fondu au noir ni carton sans demande.
- **S** : « la fin est trop fin cutter » (skill §6) : regard silencieux, fondu au noir avant qu'il bouge, accord qui s'éteint. Un Short tiré d'une Story **boucle ou renvoie à la vidéo longue** (skill §12) ; la fin Story ne s'applique que si le Short est un extrait complet qui se termine comme la vidéo.
- **F, T, P, H** : suivre le brief ; défaut : coupe après le dernier mot utile.

---

## 3. Rythme : variété, punch-ins, J-cut/L-cut, masquer un jump cut

### 3.1 Qui fait quoi : Premiere ou After Effects

Définition du skill §1 et §16 (décision B.1) :

- **Animation graphique** (tout élément créé : étiquette, prix, pop-up emoji, note, sous-titre animé, flash blanc, glitch, transition graphique, shake d'une étiquette ou du prix) : **After Effects**, calques natifs modifiables.
- **Traitement d'un plan filmé** (punch-in sec, zoom façon Micode, whip ou shake du cadre, speed ramp, recadrage, Auto Reframe, stabilisation, fondu, mouvement sur une photo ou un document qui désigne un détail) : **Premiere**.

Un script peut piloter AE ; il ne fabrique jamais d'image hors d'AE. Les emojis Apple rendus par macOS sont autorisés. Exemple : dans l'« intérieur » de la DA v2, le flash blanc et le scintillement sont des compositions AE, le shake du cadre se fait dans Premiere, le shake du prix dans la composition AE du prix.

### 3.2 Variété visuelle sans « bouillie »

Learn By Leo (2:36–5:42) [Tuto] : alterner face caméra, B-roll et motion graphics ; un plan de 10 s intéressant vaut mieux qu'une coupe systématique. Pour Cabezer, le rythme vient du discours et des valeurs de plan, pas d'effets à chaque mot (skill §4) ; en D, pas plus de 6 s sans élément visuel nouveau (§5.2) ; en S, une image par idée, jamais par mot (skill §6).

### 3.3 Mouvement sur un plan filmé ou fixe

- **F, S, T, P** : zoom lent façon Micode **seulement si le moment le demande** (skill §7) : Bézier, maintien, retour au cadre de base avant la coupe. Éviter un zoom à chaque plan.
- **Photo, document, capture** : le mouvement désigne un détail ou présente un visage, avec un temps avant et après et une courbe douce ; jamais de dérive décorative, jamais sur un plan qui porte un texte à lire (skill §6).
- **D** : punch-ins secs en alternance 100 / 115 %, 120 % sur les bouchées ; shake + flash seulement sur les gros moments (prix, intérieur, verdict) ; ailleurs coupes franches (skill §5.1, valeurs de Cabezer).
- **Whip entre deux lieux (D, T, F)** : 4 à 6 images, 130 %, glissement de 12 %, flou de mouvement, swoosh (skill §5.1). Mécanique : calque de réglage, effet Transformation (Transform), échelle + position avec facilités, angle d'obturateur élevé, sujet déplacé pendant le zoom (Premiere Gal, 7:40–8:44 [Tuto]). Transition marquée, donc sonorisée (§5).
- Éviter les « wiggle keyframes » en Premiere.

**Interpolation (décision D.1).** « Jamais linéaire » vise les mouvements progressifs (Bézier). Un punch-in sec est un changement instantané (clé maintenue ou deux clips), hors de cette règle. La vitesse constante est permise pour une rotation continue, un défilement, un compteur ou une boucle.

**Punch-in sec dans Premiere** (libellés à confirmer) :

1. Couper le clip au point de bascule (outil Rasoir / Razor ; raccourci à confirmer, sinon menu).
2. Sur le clip suivant : Contrôles d'effets (Effect Controls) > Mouvement (Motion) > Échelle (Scale) : 115 (120 sur la bouchée), sans image clé.
3. Vérifier que le point d'ancrage reste sur le visage et les yeux dans le tiers central.

Un punch-in de 115–120 % reste net sur un 4K et se voit sur un 1080p [Calcul/Tuto : Premiere Gal, 1:00] : en D, privilégier les rushs 4K de la Pocket 3 dans une séquence 1080 × 1920.

### 3.4 Coupe en J et coupe en L

J-cut : l'audio du plan suivant commence **avant** l'image ; L-cut : l'audio du précédent déborde (Joseph, 5:05 [Tuto]). **Quand** : S, F, T, P, discours enchaînant plusieurs plans, lien entre propos et B-roll.

- **D** : coupes franches par défaut. J/L permis sur un enchaînement parlé s'il ne mord pas l'attaque d'un mot ; **jamais sur la bouchée ni la réaction** (décision D.4).
- **Procédure** : sélectionner **uniquement l'audio** du clip lié (dissocier par le menu Clip, libellé à confirmer, ou touche lue dans Raccourcis clavier), déplacer le bord de coupe, vérifier que la vidéo n'a pas bougé, relier. **[À vérifier]** : Joseph décrit « Alt + glisser » ; sur Mac, Option + glisser **duplique** un clip.
- **Critère** : on entend le mot suivant avant de voir le plan, sans clic ni doublon d'audio.

### 3.5 Masquer un jump cut (par ordre de préférence)

Source : Premiere Gal, 0:00–11:50 [Tuto]. En D, un jump cut visible est acceptable (sa base est la coupe franche) : ne masquer que ce qui gêne (décision D.3).

1. **Coupe franche assumée ou punch-in sec** (~110–115 %, position décalée). Technique de base de D ; **toutes familles**.
2. **Plan de coupe qui apporte quelque chose**, posé **avant** la coupe, pas pendant (Premiere Gal, 3:33).
3. **Second angle synchronisé** ; trois angles ou plus : multicam (skill §12).
4. **Animation, seulement si elle était déjà prévue** : un titre déjà décidé peut couvrir la coupe (flou animé 0 → 50 → 0 sous le titre, fondu aux bords, Premiere Gal 4:34–5:36). Titre et habillage sont faits dans AE (§3.1). Jamais d'animation ajoutée pour cacher une coupe (skill §5.1).

**Morph Cut** : seulement sur demande explicite (§11.1). **Piège** : plusieurs coupes sur un même plan se voient plus qu'une seule.

### 3.6 Le son qui cache la coupe

- Couper dans le silence de la forme d'onde, jamais dans un mot (skill §4). Le montage par le texte repère et pré-découpe ; chaque coupe est ensuite recalée à la forme d'onde et à l'énergie du son (décision D.5).
- **Fondu audio de raccord :** seulement là où un clic est audible, 1 à 2 images dans le silence, ou deux clés de volume. **Jamais en masse** sur les coupes serrées de D, **jamais** sur l'attaque d'un mot ni la fin de « Bref, c'est partiiii » (`audio-dialogue-sound-design-mixage.md §3.2`). Le fondu par défaut de 2 images sur toutes les coupes (Premiere Gal) n'est pas retenu.
- Égaliser les écarts de volume entre phrases par images clés, pas par compression globale (skill §11).

---

## 4. Sous-titres animés

### 4.1 Voie unique

Les **sous-titres finaux sont une composition AE** : un calque de texte éditable, un mot ou un paquet par clé de Texte source (Source Text), à l'identité de la famille, entrée animée, rendue en **ProRes 4444 alpha**, plus un **SRT livré**. Les légendes natives de Premiere servent seulement de **piste de travail** (transcription, relecture, calage, source du SRT) et ne partent jamais à l'export final. La commande « Mettre à niveau la légende » n'est plus utilisée. Un repli sans AE s'appellerait « repli non animé » et serait consigné dans `Suivi/decisions.md` (question §14).

### 4.2 Limites par famille et langue

Le skill prime (§9) ; les tutoriels apportent des méthodes, pas des seuils.

- **D, France et Belgique** : français, **un mot à la fois**.
- **D, tourné à l'étranger** : langue locale ou anglais, **à demander à chaque vidéo** (mode autonome : anglais). Traduction : paquets de **1 à 3 mots, ≤ 18 caractères**, petits mots collés au mot qui suit.
- **Autres familles et étranger** : **2 lignes maximum**, ≤ 24 caractères par ligne en 9:16, coupures de ligne explicites, pas de mot isolé ; anglais si tourné à l'étranger. En 16:9 : viser ≤ 42 caractères par ligne.
- Traduire le sens oral (ton naturel), garder les noms propres et le mot exact de l'appel au commentaire. Une traduction automatique n'est utilisée que relue (§11.1).

**Valeurs de tutoriel, non retenues par défaut :** Adobe Video (0:31) 20 caractères, 1,2 s minimum, une ligne ; Anthony Mediaz (0:00) 17 caractères ; Joseph (5:35) 15 caractères, 2 s ; Learn By Leo (7:13) 3 mots maximum, compatible avec la traduction D. Le skill autorise 2 lignes (question §14).

**Temps de lecture.** La formule `max(1,5 s ; 1 s + caractères/15)` du skill s'applique aux textes d'habillage, cartons, traductions de passages étrangers et blocs de sous-titres des familles longues. Elle ne s'applique **ni** aux sous-titres mot à mot de D **ni** aux coupes rapides nommées (0,4–0,8 s). Un paquet de traduction D suit le rythme de la parole (3,6 à 4,2 mots par seconde dans ses reels, skill §5) ; le plancher de 0,25 s du script est une valeur de départ à valider sur téléphone.

### 4.3 Typographie française et découpage

**Typographie à l'écran** (espaces insécables, ponctuation, guillemets, nombres, majuscules accentuées, ligature œ, heures) : `conformite-droits-accessibilite.md §7`, non répétée ici. Son usage propre prime (« 19h30 »). Vérifier que la police d'identité contient les glyphes des espaces insécables. En D mot à mot, seules la casse, les accents et l'orthographe s'appliquent. Relever noms propres et marques sur le menu ou le ticket.

**Découpage par groupes de sens (familles à 2 lignes).** Ne jamais séparer l'article et le nom, l'adjectif et le nom, le prénom et le nom, la préposition et son complément, l'auxiliaire et le participe, le pronom et le verbe (négation incluse), le nombre et son unité. Couper de préférence après une ponctuation forte ou avant une conjonction ; aucun mot isolé ; deux lignes de longueur proches. Ces principes reprennent les règles de coupe de ligne du guide Netflix [Extrait : page non lue]. Corriger par des sous-titres successifs, jamais en réduisant la police ponctuellement.

**Contrôle** : `lint-srt.py` (`organisation-livraison-qc.md §6.4`) applique ces seuils par famille et signale aussi l'espace simple avant `; : ! ?` et l'apostrophe droite.

### 4.4 Piste de travail dans Premiere (transcription et SRT)

D'après Adobe Video (0:00–1:01) et Anthony Mediaz [Tuto] ; libellés à confirmer :

1. Fenêtre > Texte (Window > Text) ; onglet Transcription ; Transcrire (Transcribe).
2. Relire mots, noms propres, chiffres, ponctuation (marques et mots étrangers souvent mal transcrits ; les temps de mot sont étirés, skill §5).
3. Créer les légendes à partir de la transcription avec les limites de la famille (§4.2) : hors D, deux lignes et 24 caractères par ligne.
4. Contrôler chaque bloc : aucune 3e ligne (Premiere peut en ajouter une, skill §9), aucun mot coupé.
5. Exporter le SRT depuis le panneau Légendes.

Le style de légende Premiere par défaut est refusé par Cabezer (Maritozzo v09).

### 4.5 Animation d'entrée : valeurs de départ

Tutoriels : Adobe Video (1:31) échelle 95 → 105 → 100 % sur 5 images avec facilités ; Joseph (7:06) 80 → 100 % sur 1 s, trop lent pour des paquets d'un mot ; Anthony Mediaz (2:05–3:38) flou 35 → 0 + opacité + léger glissement. **Skill :** D, pop en 4 images, sortie sèche au paquet suivant ; autres familles, pop léger, mots révélés un à un, sortie courte.

**Pop de D en AE** : un seul calque de texte, une clé de Texte source par mot (méthode et script de pose des clés : `after-effects-motion-design.md §7.2` et `§15.2`). Expression d'échelle qui redémarre à chaque clé ; syntaxe relue dans docsforadobe (`ease`, `framesToTime`, `nearestKey`) [Doc lue], **non exécutée dans AE** :

```
// Pop 85 -> 108 -> 100 sur 4 images depuis la dernière clé de Texte source
tx = text.sourceText; s = 100;
if (tx.numKeys > 0) {
  k = tx.nearestKey(time);
  n = (k.time > time) ? k.index - 1 : k.index;      // dernière clé déjà passée
  if (n >= 1) {
    t = time - tx.key(n).time; d = framesToTime(4);
    s = (t < d*0.6) ? ease(t, 0, d*0.6, 85, 108) : ease(t, d*0.6, d, 108, 100);
  }
}
[s, s]
```

Opacité : `ease(t, 0, framesToTime(2), 0, 100)` avec le même `t`. Centrer le point d'ancrage sur le texte (commande de centrage du point d'ancrage, libellé à confirmer), sinon le pop part d'un coin. **Mot clé** (produit, prix, note, lieu) en couleur d'accent (rouge tomate `#E63946` en France, skill §5.1) : couleur de la clé en D à un mot ; animateur « Couleur de remplissage » à sélecteur de plage en paquets. **Critère** : chaque paquet est lisible entier avant le suivant ; le mot en couleur est exact.

### 4.6 Préparer les paquets avec un script (traduction D, ou Shorts hors D)

Entrée : mots horodatés (TSV `début<TAB>fin<TAB>mot`). Le script `paquets.py` (à ranger dans le dossier de scripts de `organisation-livraison-qc.md`) forme des paquets de 1 à 3 mots et 18 caractères au plus et **décale ou retire** un paquet qui tombe sous une animation (skill §9). [Test] sur données de test ; à étalonner sur un vrai rush.

```
python3 -I paquets.py mots.tsv fenetres_animations.tsv > paquets.tsv
```

```python
import sys
PETITS = {"le","la","les","un","une","des","de","du","d'","l'","à","a","au","et","en","y","ce","se","sa","son",
          "ses","je","tu","il","on","ne","the","an","of","to","in","at","and","or","my","is","it"}
MAXC, MAXW = 18, 3
def paquets(mots):
    out, cur = [], []
    def vide():
        nonlocal cur
        if cur: out.append((cur[0][0], cur[-1][1], " ".join(m[2] for m in cur))); cur = []
    for d, f, m in mots:
        if cur and (len(" ".join(x[2] for x in cur + [(d, f, m)])) > MAXC or len(cur) >= MAXW): vide()
        cur.append((d, f, m))
        fin = m.rstrip().endswith((".", "!", "?", "…"))
        petit = m.lower().strip(",.;:!?") in PETITS
        if fin or (len(cur) >= 2 and not petit and len(" ".join(x[2] for x in cur)) >= 9): vide()
    vide(); return out
def lire(p): return [tuple(l.rstrip("\n").split("\t")) for l in open(p) if l.strip()]
mots = [(float(a), float(b), c) for a, b, c in lire(sys.argv[1])]
wins = [(float(a), float(b)) for a, b, *_ in lire(sys.argv[2])] if len(sys.argv) > 2 else []
for d, f, t in paquets(mots):
    for wd, wf in wins:
        if d < wf and f > wd:                      # chevauche une animation
            if d < wd: f = min(f, wd)              # garder la partie avant
            else: d = wf                           # attendre la fin
    if f - d >= 0.25: print(f"{d:.3f}\t{f:.3f}\t{t}")   # sinon retiré (valeur de départ)
```

- Fin de phrase : ferme le paquet. Un paquet ne se ferme pas sur un petit mot sauf si la limite de 18 caractères ou de 3 mots l'impose : relire ces cas.
- **Après la coupe de Cabezer** : les temps viennent du son conservé, pas de la transcription du rush brut ; la traduction est réécrite sans les phrases coupées (skill §9).
- Les paquets alimentent les clés de Texte source (`after-effects-motion-design.md §15.2`). Aucun gabarit générique : police, couleurs et position viennent de la fiche d'identité de la famille.

### 4.7 Position et pièges

Position des sous-titres de D (72–75 % de la hauteur) et statut par rapport à la boîte : §6.2. Les autres familles restent dans la zone autorisée de la boîte (skill §9 : éviter l'interface mobile et le visage).

- Sous-titre resté sous une animation (prix, pop-up, note, appel au commentaire) : le masquer.
- Rendu d'un seul tenant qui ne suit plus les coupes après une retouche de Cabezer : recouper aux mêmes images, vérifier la synchro dans l'export.
- Ne pas annoncer les sous-titres contrôlés tant qu'un bloc sur trois lignes existe (skill §9).

---

## 5. Son : SFX, silences, musique

Learn By Leo (10:18–13:54) [Tuto] : whoosh sur un mouvement, riser avant une information, hit après le moment, drone pour un climat sombre, pause brutale de la musique ; « ne pas en abuser ».

**Application par famille :**

- **D** : banque Pixabay dédiée et **liste de référence** du skill (swoosh, pop, ding, boing, scratch, caisse, photo, scintillement), chacun lié à un élément, aucune musique. Pas de mème vocal ni de boom (retiré le 02/10). Riser et drone sont hors liste (question §14).
- **F, S, T, P** : bibliothèque ouverte, licence dans `Suivi/licences.csv`, audible sous la voix. Whoosh sur mouvement rapide ou transition marquée ; riser seulement si un vrai enjeu suit. **S** : nappe basse continue (environ 24 dB sous la voix, `audio-dialogue-sound-design-mixage.md §5.5`), silence de 1 à 2 s avant une bascule, pas de hit ni de bruitage d'objet gratuit. **P** : musique de la bibliothèque personnelle, pas de musique tendance.
- **D, par défaut** : aucune ambiance continue, aucun bruitage d'aliment sur une bouchée ou une réaction ; ambiance sous insert muet et foley sont des questions ouvertes portées par `audio-dialogue-sound-design-mixage.md` (défaut : non).

**Calage.** À l'attaque du son (swoosh sur son pic) ; un essai A/B de ±1 image n'est adopté que s'il gagne à l'écoute de Cabezer. Chaque SFX appartient à un élément : élément retiré, SFX retiré (skill §5).

**Contrôle.** Chaque SFX est audible sous une voix intelligible sans écraser une bouchée ni une réaction (skill §11). Claude n'entend pas : il contrôle par mesures, transcription et forme d'onde ; l'écoute (volume normal, petit haut-parleur, mono) revient à Cabezer. Ne jamais écrire « écouté » pour une mesure.

---

## 6. Format vertical : zones sûres, recadrage, résolution

### 6.1 Ce que l'on sait des zones sûres

**Aucune valeur officielle n'a été lue** (TikTok, Meta, YouTube). Les guides tiers se contredisent, **à vérifier** : Shorts 180 px en haut, 380 en bas, 120 à droite (un guide) ou 15 % / 35 % (un autre) ; TikTok publicités 90–254 px en haut, 330–707 en bas, 44–242 sur les côtés ; Reels 14 % en haut, 35 % en bas, 6 % de chaque côté. Ces valeurs concernent souvent des **publicités**, qui ajoutent des boutons, et les interfaces changent. Un seul fait est stable : **le côté droit et le bas** sont occupés (boutons, légende, nom du compte). Les marges de sécurité de Premiere sont faites pour la télévision : ne pas les utiliser pour un réseau social [À vérifier à l'écran].

### 6.2 La boîte de test provisoire (source unique)

**Cette section est la seule définition des zones sûres 9:16.** `organisation-livraison-qc.md §9`, `adaptation-genres-analyse-de-style.md` et le skill y renvoient ; aucune autre fiche ne définit une autre boîte.

**Valeurs (1080 × 1920)** : zone **interdite** au texte clé = **270 px en haut** (14 %), **670 px en bas** (y ≥ 1250, 35 %), **132 px à droite** (x ≥ 948, 12 %). Enveloppe prudente des valeurs rapportées pour Reels et Shorts, plus étroite que les valeurs publicitaires les plus larges de TikTok. Boîte de test, non officielle.

**Portée** : le **texte clé** — étiquettes, prix, pop-ups, note, texte d'accroche, pastille de l'appel au commentaire. Visage et produit en gros plan restent au centre. Les sous-titres des autres familles s'y conforment (§4.7).

**Statut pour les sous-titres de dégustation.** Ils restent à **72–75 % de la hauteur** (y ≈ 1382 à 1440), base validée de Cabezer ; cette bande tombe dans la zone interdite basse. Défaut en attendant sa réponse (question §14) :

- les sous-titres de D sont **exemptés** de la boîte : le contrôle automatique ne les signale pas, mais signale tout autre texte ;
- le test sur téléphone (§6.3) vérifie qu'ils ne sont **pas masqués** par la légende, les boutons ou la barre de progression ; s'ils le sont, le dire à Cabezer sans les déplacer seul ;
- la pastille de l'appel au commentaire se place au-dessus de y = 1250.

**Remplacement.** Dès réception des captures d'écran (§6.3), remplacer la boîte par les mesures réelles, les consigner dans la fiche d'identité de la famille et dans `Suivi/verifications.md` ; le script de `organisation-livraison-qc.md §9.1` lit ces valeurs.

**Repères.** AE : calque Solide ou Forme « REPÈRES », opacité 35 %, en **calque repère** (Guide Layer ; libellé à confirmer ; propriété `guideLayer` présente dans l'API de script [Doc lue]), normalement non rendu : le vérifier au premier rendu. Premiere : PNG de repères sur la piste la plus haute, **désactivé avant l'export**. Création du PNG [Test] :

```
ffmpeg -f lavfi -i "color=c=black@0.0:s=1080x1920,format=rgba" -frames:v 1 \
 -vf "drawbox=x=0:y=0:w=1080:h=270:color=red@0.35:t=fill,drawbox=x=0:y=1250:w=1080:h=670:color=red@0.35:t=fill,drawbox=x=948:y=0:w=132:h=1920:color=red@0.35:t=fill" repères.png
```

### 6.3 Test sur le téléphone de Cabezer (sans publier)

Le skill interdit toute publication sans accord. Méthode :

1. Demander **une capture d'écran de chaque application** (TikTok, Reels, Shorts) pendant la lecture, interface visible (légende, boutons, barre de progression).
2. L'importer comme calque repère dans AE, à 50 %, et mesurer les zones couvertes.
3. Noter si l'application **recadre les côtés** ou laisse des bandes (non vérifié).
4. Remplacer la boîte par ces mesures (§6.2).

### 6.4 Recadrage 16:9 → 9:16 (Auto Reframe)

Sources : Adobe Learn et fil communautaire (extraits, non lus) ; **[À vérifier] dans l'application**. Auto Reframe est un **point de départ**, résultat vérifié (§11.1).

1. Dupliquer la séquence montée.
2. Séquence > Recadrage automatique de la séquence (Auto Reframe Sequence ; libellé à confirmer) ; 9:16 ; vitesse de suivi (plus lent, défaut, plus rapide).
3. Corriger les images clés de Position, Échelle, Rotation dans les Contrôles d'effets pour garder visage, produit ou document lisibles ; avec deux personnes ou un produit, corriger à la main.
4. Refaire textes et sous-titres à l'échelle verticale selon l'identité de la famille.
5. Lisser les mouvements progressifs (§3.3).

**Résolution** [Calcul] : un 1920 × 1080 recadré en 9:16 garde 608 px de large et exige un agrandissement de **178 %** (image molle) ; un 3840 × 2160 garde 1215 px et se réduit à **89 %** (net). **Règle** : recadrer un Short tiré d'une vidéo longue depuis les **rushs 4K** ou un master 4K, jamais d'un export 1080p (contrôler avec ffprobe) ; si seul un 1080p existe, le signaler à Cabezer.

**Éviter Auto Reframe** : D tourné en vertical ; documents Story (déplacements libres, caméra 3D) ; schémas persistants : recomposer à la main.

---

## 7. Export et contrôle du MP4

### 7.1 Réglages du skill (§13)

1080 × 1920, H.264, VBR 1 passage, environ 20 Mbit/s, AAC 48 kHz 320 kbit/s, cadence de la source. Nom `<Sujet>_<plateforme>_v<NN>.mp4`. Enregistrer `.prproj` et `.aep` avant l'export. Ce débit est **le débit de Cabezer, non issu d'une source officielle**.

D'après Shawn Dolinski (3:02–6:07 [Tuto]) :

- Les préréglages « haute qualité 1080p » ou « YouTube 1080p » repassent en **1920 × 1080** avec bandes noires (3:33–4:33) ; « Correspondre à la source – haut débit adaptatif » conserve 1080 × 1920. Contrôler la taille de sortie après **tout** changement de préréglage.
- Cocher « Utiliser la qualité de rendu maximale » (Use Maximum Render Quality) et « Rendu à la profondeur maximale » (Render at Maximum Depth) — **libellés à confirmer à l'écran** ; le skill écrivait « résolution maximale », libellé non retrouvé.
- Un réglage modifié bascule le préréglage en « Personnalisé » : normal ; enregistrer le préréglage utilisateur.
- Ouvrir l'export par le menu (Fichier > Exporter > Médias, libellé à confirmer), pas par un raccourci non lu.

**Loudness** (`audio-dialogue-sound-design-mixage.md §9`) : −14 LUFS intégrés = **repère de contrôle (±1)**, pas une cible ; crête vraie du MP4 ≤ −1 dBTP. Si elle dépasse, baisser d'abord la source fautive (SFX, musique) ; pas de limiteur de bus maître sans accord. Le mix se valide à l'écoute de Cabezer.

### 7.2 Contrôles du MP4 exporté

Ils **signalent** des cas à revoir, sans remplacer visionnage ni écoute (skill §14). Les commandes (ffprobe, blancs, son manquant, noirs, figements, niveaux, `ebur128`, scènes) sont dans la bibliothèque unique de `organisation-livraison-qc.md §6` et le script `controle-mp4.sh` : ne pas les copier. Ce que cette fiche ajoute au vertical :

- **Taille et codec** : `organisation-livraison-qc.md §6.2` ; 1080 × 1920 exact, pas de bandes noires.
- **Zones** : `organisation-livraison-qc.md §9.1` lit les valeurs du §6.2 ; aucun texte clé dans les zones rouges, aucun repère rouge dans l'export.
- **Niveaux** : repère −14 LUFS ±1 consigné, crête ≤ −1 dBTP.
- **Flashs** : `conformite-droits-accessibilite.md §6`.
- **Hook** : planche des premières images, ci-dessous.

```
# Images 0, 6, 30, 90 (≈ 0, 0,2 s, 1 s, 3 s) [Test]
ffmpeg -i f.mp4 -vf "select='eq(n,0)+eq(n,6)+eq(n,30)+eq(n,90)',scale=270:480,tile=4x1" -frames:v 1 planche.png
```

**Critère** : planche relue par Claude (lecture des images) ; accroche lisible dès la première image ; sous-titres sur deux lignes au plus, lisibles à 270 × 480.

---

## 8. Plateformes : durées et formats

- **YouTube Shorts** : jusqu'à 3 minutes pour les vidéos carrées ou verticales importées à partir du 15 octobre 2024 (aide YouTube, Engadget, Tubefilter) [Extrait].
- **TikTok** : au moins 10 minutes selon la presse (2022) ; limite actuelle non confirmée [Extrait]. La limite **éditoriale** de D est ~3:00 (skill).
- **Reels** : 3 minutes annoncées en janvier 2025 d'après la presse (Storyboard18, Social Samosa) [Extrait].

La durée optimale est un choix éditorial : les 34 s de Hoyos (2023) ne s'appliquent pas à la dégustation de Cabezer (jusqu'à 3:00). Pas de master 4K sans demande (skill §13). Relire la fenêtre d'envoi avant une série de vidéos et consigner valeur et date dans `Suivi/verifications.md`.

---

## 9. Dégustation : ce que les références confirment

Les tutoriels n'étudient pas la dégustation. Le format de Keith Lee, décrit par la presse (non vu), recoupe le skill (lieu nommé, note sur 10, pas de musique, plan serré sur la bouchée) : confirmation faible, aucune règle nouvelle.

**Applicable à D :** test du son coupé ; boucle ouverte par l'enjeu (« Luini ferme à 20h ») plutôt que par un texte qui répète la voix ; punch-in sec pour le jump cut (§3.5) ; hook noté selon le §1.2 ; fin après l'extinction de l'appel au commentaire (§2.3) ; contrôles du §7.2.

**Non applicable :** structure « amorce » de Hoyos, musique tendance, riser/drone sans accord, flou du produit, texte qui double la parole.

Aucun critique français de vidéos courtes sur des restaurants n'est documenté ici : avant l'habillage, étudier des références récentes (skill §8), consigner liens, dates, passages, métriques visibles, sans copier un montage ni récupérer les sons.

---

## 10. Mesurer : rétention et boucle d'amélioration

Hoyos (8:09–9:09) [Tuto, anecdotique] : le **taux de défilement** est la part des spectateurs qui ne swipent pas (moyenne annoncée 70 %) ; la **rétention** est la part du temps regardé. Ses repères (90 %, 34 s, 83 → 88 %) sont des observations personnelles de 2023 : ne pas les utiliser comme objectif. Les chiffres d'impact des trois premières secondes (TikTok, Vidmob, CreatorIQ) portent sur des publicités de 2023 : écartés.

Boucle du skill (§15) : repérer la chute sur la courbe (YouTube Studio, statistiques TikTok/Reels) → la relier au moment de la timeline (hook, produit, bouchée, relance, fin) → modifier **une seule variable** → garder l'hypothèse comme telle tant qu'elle n'est pas confirmée sur plusieurs vidéos de la même famille.

---

## 11. Outils : IA, plugins payants, gratuits

### 11.1 Statuts des outils IA (décision B.2, skill §16)

- **Autorisés comme aides, résultat vérifié** : transcription (Speech to Text) ; montage par le texte pour repérer et pré-découper ; détection des scènes ; Auto Reframe comme point de départ ; Roto Brush et suivi sur un vrai plan ; traduction automatique de légendes **relue**.
- **Seulement sur demande explicite de Cabezer** : Morph Cut ; Remplissage d'après le contenu (Content-Aware Fill) ; Generative Extend ; tout outil Firefly ou de génération/reconstruction de pixels (dont le remplissage génératif pour effacer un texte).
- **Interdits par défaut (règle de Cabezer)** : « Améliorer la parole » (Enhance Speech) ; Correspondance automatique et « Dynamique » d'Essential Sound ; images ou animations générées par IA (voix ou musique produites par un modèle génératif : seulement sur demande explicite, skill §16).

Hors tableau : la **suppression d'arrière-plan par un service en ligne** n'est pas utilisée (rushs hors de la machine, offre souvent payante, détourage proche des stickers refusés en DA v2) ; détourer ou suivre sur le vrai plan dans AE ou Premiere. **Object Mask** de Premiere n'est pas nommé dans les décisions : défaut, masques manuels (question §14).

### 11.2 Plugins payants à signaler (aucun installé)

Captioneer (« payant, parfois cher », Adobe Video), SubMachine, Spotlight FX Captions & Subtitles, Subtitle Pro, KaraokeSubs, Premiere Gal Toolkit, Epidemic Sound (stems), stock par abonnement. **Prix : à vérifier, non retenus.** Gratuits uniquement par défaut (skill §17) ; tout outil payant est signalé (nom, prix connu ou « à vérifier ») et attend l'accord de Cabezer. Cette fiche se passe de ces outils : le mot par mot passe par le script du §4.6.

### 11.3 Gratuit

Pixabay (SFX de D, licences dans `LICENCES-SFX.md`), Freesound (lire chaque licence), bibliothèque audio YouTube (idem), outils natifs de Premiere et d'AE. Les emojis Apple sont rendus par macOS (skill §5.1) ; aucun emoji pris sur Internet. Toute licence d'image, vidéo, son ou police est consignée dans `Suivi/licences.csv`.

---

## 12. Erreurs de débutant → réflexes de pro

| Erreur | Réflexe de pro |
|---|---|
| Hook compris seulement avec le son | Test du son coupé ; texte lisible dès 0,2 s |
| Texte qui répète la voix | Texte qui pose une question ou donne le contexte |
| Hook qui cache le produit (D) | Produit ou bouchée dans la 1re seconde |
| Hook de Cabezer écarté car sous 8 | Le noter, proposer au plus deux variantes, son choix prime |
| Sous-titres posés sans tester l'interface | Boîte du §6.2, puis captures des applications |
| Sous-titres de D déplacés seul | Garder 72–75 %, tester sur téléphone, demander |
| Export « YouTube 1080p » qui repasse en horizontal | Contrôler la taille de sortie après tout changement de préréglage |
| Recadrage d'un 1080p à 9:16 | Recadrer depuis les rushs 4K |
| Animation ajoutée pour cacher une coupe | Punch-in sec ou plan de coupe ; animation seulement si un titre était prévu |
| Whoosh sur chaque coupe | Whoosh sur un mouvement ou une transition marquée |
| Fondu audio de 2 images partout | Seulement où un clic s'entend ; jamais sur un mot protégé |
| Sous-titres sous un prix ou un pop-up | Masquer ; le paquet attend la fin de l'animation |
| Légende Premiere « mise à niveau » pour animer | Composition AE ProRes 4444 alpha + SRT |
| Flashs enchaînés dans un hook agressif | Décompte de `conformite-droits-accessibilite.md §6` |
| Valeur de tutoriel appliquée à toutes les familles | Famille, puis skill, puis tutoriel |

---

## 13. Liste de contrôle

**Avant l'habillage**
- [ ] Famille identifiée ; identité retrouvée ; hook demandé (D).
- [ ] Versions Premiere/AE lues ; libellés et raccourcis consignés dans `Suivi/environnement-verifie.md`.
- [ ] Rushs 4K si recadrage depuis une vidéo longue, sinon limite signalée.
- [ ] Animations graphiques dans AE, plans filmés traités dans Premiere (§3.1).

**Hook**
- [ ] Test du son coupé réussi ; D : hook de Cabezer noté, deux notes données si variante.
- [ ] Produit ou bouchée dans la 1re seconde (D) ; texte lisible dès 0,2 s ; 2 changements de plan ou de cadre comptés sur la timeline.
- [ ] Aucun flou ni texte sur le visage ou le produit ; flashs du hook comptés.

**Sous-titres**
- [ ] Composition AE (ProRes 4444 alpha) + SRT ; légendes Premiere non exportées.
- [ ] D : un mot à la fois, ou 1 à 3 mots ≤ 18 caractères en traduction ; langue demandée à l'étranger (autonome : anglais).
- [ ] Autres familles : 2 lignes, ≤ 24 caractères par ligne, groupes de sens, aucun mot isolé.
- [ ] Masqués pendant prix, pop-up, note, appel au commentaire ; noms, chiffres, typographie relus ; linter passé.

**Zones sûres**
- [ ] Texte clé hors zone interdite (§6.2) ; repères désactivés dans l'export.
- [ ] Sous-titres de D vérifiés sur téléphone, ou « non fait » ; boîte provisoire signalée tant que les captures manquent.

**Export**
- [ ] 1080 × 1920 ; cadence source ; VBR 1 passage ~20 Mbit/s ; AAC 48 kHz 320 kbit/s.
- [ ] Contrôles du §7.2 faits ; niveaux et crête consignés ; écoute finale demandée à Cabezer.
- [ ] `.prproj` et `.aep` enregistrés ; nom `<Sujet>_<plateforme>_v<NN>.mp4`.

**États (skill §1)** : dire ce qui est appliqué, contrôlé, validé par Cabezer ; une mesure n'est pas une écoute.

---

## 14. Décisions à demander à Cabezer

Chaque question donne le **défaut appliqué en attendant** ; l'alternative n'est jamais présentée comme une règle.

1. **Sous-titres de D et boîte de zones sûres.** Garder 72–75 % de la hauteur (sa base), bien que cette bande tombe dans la zone interdite basse ? *Défaut :* oui, exemptés de la boîte, test sur son téléphone pour vérifier qu'ils ne sont pas masqués.
2. **Captures d'écran des applications** (TikTok, Reels, Shorts, interface visible). *Défaut :* boîte provisoire du §6.2.
3. **Object Mask de Premiere** (masque assisté) accepté ? *Défaut :* non, masques manuels et suivi ; Roto Brush et suivi restent autorisés, résultat vérifié.
4. **Riser et drone en dégustation**, hors de la liste de référence : les essayer sur un Short ? *Défaut :* non.
5. **Sous-titres hors D** : une ligne de 20 à 24 caractères ou deux lignes ? *Défaut :* deux lignes, ≤ 24 caractères par ligne en 9:16 (skill).
6. **Fin de dégustation** : couper juste après l'appel au commentaire ou garder une courte image finale ? *Défaut :* coupe après l'extinction réelle de la voix (skill §4).
7. **Repli non animé des sous-titres** (légendes Premiere au style de la famille) si AE est indisponible ? *Défaut :* non ; décrire le blocage et attendre.
8. **Paquets de traduction en dégustation** : durée minimale. *Défaut :* rythme de la parole, plancher de 0,25 s du script, à valider sur téléphone.

---

## 15. Sources étudiées

**Transcriptions lues en entier (automatiques, anglais) — [Tuto]**

| Auteur | Titre | URL | Couverture réelle |
|---|---|---|---|
| Jay Clouse (Creator Science) avec Jenny Hoyos | Shorts Genius Shares Everything She Knows | https://www.youtube.com/watch?v=As7abwNhG7Y | 38 min lues ; interview du 9 oct. 2023 ; intuitions personnelles |
| Adobe Video (avec @filmriot) | Learn How to Animate Captions in Three Minutes | https://www.youtube.com/watch?v=ZCP2W_NTpLE | 3 min lues ; légendes, animation 95-105-100 ; chaîne officielle, pas la documentation |
| Anthony Mediaz | How to Create Smooth Animated Captions in Premiere Pro | https://www.youtube.com/watch?v=21B04KjqZc8 | 7 min lues ; légendes, flou, opacité ; police douteuse |
| Joseph \| Video Editing | How to Edit Viral Alex Hormozi Reels in Premiere Pro! | https://www.youtube.com/watch?v=pelJlYOkn7s | 24 min lues ; promotion de formation en fin |
| Learn By Leo | How to edit SO good your viewers get addicted to your videos | https://www.youtube.com/watch?v=sLgHqZSe2o0 | 14 min lues ; sponsors ; variété, son, musique |
| heyDominik | I Studied 1,000 Hooks, Here's How to ACTUALLY Go Viral | https://www.youtube.com/watch?v=Xqy9L-88wcw | 20 min lues ; vend un coaching ; méthode avec image IA écartée |
| Shawn Dolinski | How To EXPORT VERTICAL VIDEO in Premiere Pro CC | https://www.youtube.com/watch?v=PQizR1m1DWk | 7 min lues ; version de Premiere non indiquée |
| Premiere Gal | Hide Jump Cuts Like a PRO | https://www.youtube.com/watch?v=wVmi89tBORc | 12 min lues ; sponsor de stock |

**Documentation communautaire lue (ajoutée à la passe 2) — [Doc lue]**

| Auteur | Titre | URL | Couverture réelle |
|---|---|---|---|
| docsforadobe | After Effects Expression Reference (`ease`, `framesToTime`, `nearestKey`, `numKeys`) | https://github.com/docsforadobe/After-Effects-Expression-Reference | `interpolation.md`, `time-conversion.md`, `property.md` lus (révision du 23/01/2026) ; aucune exécution dans AE |
| docsforadobe | After Effects Scripting Guide (`addText`, `inPoint`/`outPoint`, `guideLayer`) | https://github.com/docsforadobe/After-Effects-Scripting-Guide | `layercollection.md`, `layer.md`, `avlayer.md` lus (révision du 10/09/2026) ; aucune exécution dans AE |

**Résumés de recherche (pages non ouvertes) — [Extrait]**

| Auteur | Titre | URL | Couverture réelle |
|---|---|---|---|
| YouTube (aide) ; Engadget ; Tubefilter | Understand three-minute YouTube Shorts ; YouTube Shorts can now run up to three minutes | https://support.google.com/youtube/answer/15424877 ; https://www.tubefilter.com/?p=182474 | Résumé seulement : carré ou vertical, 3 min, dès le 15/10/2024 |
| Storyboard18 ; Social Samosa | Instagram extends Reels to three minutes | https://www.storyboard18.com/digital/instagram-extends-reels-to-three-minutes-and-updates-profile-layout-54043.htm | Résumé : annonce de janvier 2025, 90 s auparavant |
| Gizmodo ; NBC News | TikTok boosts maximum video length up to 10 minutes | https://gizmodo.com/tiktok-boosts-maximum-video-length-up-to-10-minutes-1848603135 | Résumé (2022) ; limite actuelle non confirmée |
| Netflix | Timed Text Style Guide: General Requirements | https://backlothelp.netflix.com/hc/en-us/articles/215758617 | Résumé : 2 lignes, coupes après ponctuation ou avant conjonction, pas de séparation article/nom, prénom/nom, pronom/verbe ; page refusée par le proxy |

**Non lues ou par extraits** : aide Adobe sur Auto Reframe, fil communautaire Adobe, Creative Codes de TikTok, guides tiers de zones sûres, articles sur Keith Lee. **Neuf tutoriels** bloqués par YouTube (Think Media, ryancollinsvideo, Shaun Notcutt, Chriss Boustedt, Tim Runia, Jonny Duncan, Premiere Basics, Premiere Gal sur le mot par mot). **Notes de recherche** : `notes/formats-courts.md`. **Tests** : commandes ffmpeg et script de paquets exécutés en local sur un clip synthétique 1080 × 1920.
