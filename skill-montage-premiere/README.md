# Skill de montage Cabezer — version 3 (niveau pro)

Nouvelle version du skill `cabezer-premiere-shorts` (Premiere Pro + After Effects), construite le 12/10/2026 à partir de ta v2 et des méthodes des meilleurs monteurs.

## Contenu

| Élément | Rôle |
|---|---|
| [`ANALYSE-CONTRADICTIONS.md`](ANALYSE-CONTRADICTIONS.md) | **À lire en premier.** Ce qu'il faut garder, ce qui a été retiré ou reformulé, les 23 contradictions tranchées et les 16 questions qui t'appartiennent |
| [`cabezer-premiere-shorts/SKILL.md`](cabezer-premiere-shorts/SKILL.md) | Le skill v3 : toutes tes règles, sans contradiction, avec la définition de l'animation, le mode autonome, les outils IA classés, le statut des méthodes et l'index des fiches pro |
| [`cabezer-premiere-shorts/references/pro/`](cabezer-premiere-shorts/references/pro/) | 13 fiches de monteur professionnel (environ 7 000 à 9 000 mots chacune), harmonisées avec tes règles |
| [`cabezer-premiere-shorts/references/pro/scripts/`](cabezer-premiere-shorts/references/pro/scripts/) | 10 scripts de contrôle en lecture seule : MP4, coupes du XML, sous-titres, typographie, photosensibilité, contraste, environnement du Mac, reprise après plantage |
| `cabezer-premiere-shorts/references/historique.md` | Historique des consignes, trié dans l'ordre et annoté (« remplacée le… ») |
| `cabezer-premiere-shorts/references/projets-cabezer.md` | Détails des projets passés (Milan, Story fast-food, générique, musique v10) sortis des règles générales |
| `cabezer-premiere-shorts/references/decisions-en-attente.md` | Registre unique des questions ouvertes, avec le défaut appliqué en attendant |
| `cabezer-premiere-shorts/references/decisions-harmonisation.md` | Les arbitrages communs auxquels les fiches renvoient |
| `v2-original/SKILL.md` | Ta version précédente, pour comparer |

## Les 13 fiches pro

1. **Fondamentaux du montage narratif** — Walter Murch, This Guy Edits, Every Frame a Painting, Eddie Hamilton, Kirk Baxter, Thelma Schoonmaker
2. **Rétention YouTube long** — document de production MrBeast, Paddy Galloway, Film Booth, Aprilynne Alter
3. **Formats courts verticaux** — hooks, sous-titres animés, zones sûres, recadrage 9:16, export social
4. **Premiere Pro avancé** — Jason Levine, Premiere Gal, Larry Jordan, doc UXP Adobe : trims, montage par le texte, multicam, double système, cadences, plans défaillants, XML, scripting
5. **After Effects et motion design** — School of Motion, Ben Marriott, ECAbrams, Jake In Motion, SonduckFilm : courbes, animateurs de texte, expressions, caméra 3D, parallaxe, rendu, pilotage par script
6. **Audio pro** — Curtis Judd, Jason Levine, EBU R128 : dialogue, chaîne voix, ducking, nappe Story, SFX, loudness
7. **Étalonnage et gestion des couleurs** — Cullen Kelly, Darren Mostyn, Jason Druss : chaîne par caméra, scopes, peau, food, HDR/HLG
8. **Documentaire, essai vidéo, archives** — Johnny Harris, Vox, Nerdwriter, Every Frame a Painting, Kurzgesagt, David Perell
9. **Styles food et tech** — Best Ever Food Review Show, Mythical Kitchen, Epicurious, MKBHD, Mrwhosetheboss
10. **Adaptation et genres** — analyser n'importe quelle référence (ffmpeg, PySceneDetect) ; pub, clip, vlog, interview, comédie, bande-annonce
11. **Organisation, livraison et QC** — arborescence, sauvegardes, retours, bibliothèque ffmpeg, spécifications d'export
12. **Pilotage, environnement et reprise** — piloter Premiere et AE sur ton Mac, exécuter des scripts, test de démarrage, reprise après plantage
13. **Conformité, droits et accessibilité** — droit à l'image, mentions commerciales, extraits tiers, photosensibilité, typographie française

## Comment c'est fait

- **Deux workflows, 40 agents.**
  - Recherche : Haiku 5.5 en effort xhigh.
  - Rédaction, vérification, audit et harmonisation : Sonnet 5.5 en effort high.
  - Synthèse finale, arbitrages et skill v3 : Claude, dans cette session.
- **Environ 110 transcriptions de tutoriels, conférences et formations lues en entier**, plus environ 320 autres sources (documentation, articles, guides, ouvrages).
- Chaque fiche indique la couverture réelle de chaque source (transcription lue, page lue, extrait seulement) et marque « à vérifier » ce qui n'a pas pu être confirmé.

**Limites :**
- YouTube a bloqué une partie des téléchargements de transcriptions (vérification anti-robot), surtout pour After Effects : rattrapage partiel en passe 2 (10 tutos).
- Les sites `helpx.adobe.com`, `schoolofmotion.com` et la doc ffmpeg étaient inaccessibles depuis cet environnement.
- Les libellés de menus, les raccourcis et les versions sont donc à confirmer sur ton Mac. La fiche « pilotage » prévoit un test de démarrage qui les relève une fois pour toutes.

## Installer la v3

1. Sur ton Mac, ouvre ton dossier actuel du skill `cabezer-premiere-shorts`, celui qui contient tes `references/` et `assets/`, et fais-en une copie de sauvegarde.
2. Remplace `SKILL.md` par celui d'ici.
3. Ajoute `references/pro/` (fiches et scripts) et les 4 fichiers `references/historique.md`, `projets-cabezer.md`, `decisions-en-attente.md` et `decisions-harmonisation.md`.
4. Vérifie que tes 18 fiches d'origine et tes 5 SFX y sont bien. **Ils manquent dans la version installée sur claude.ai** : voir la section 1 de l'analyse.
5. Compresse le dossier entier et téléverse-le là où tu gères ce skill sur claude.ai.
