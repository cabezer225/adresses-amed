# Projets Cabezer — fichiers, exemples et résultats

Détails propres à des montages passés, déplacés du SKILL.md en v3 pour garder les règles générales lisibles. Les chemins sont ceux du Mac de Cabezer : vérifier qu'ils existent avant de s'en servir (SKILL.md, en tête).

## Racines

- Dégustations : `/Users/cabezer225/Documents/ChatGPT/Tiktok degustation/`
- Story « Comment les fast-foods ont changé notre génération » : `Fast-food-generation-2026-09-21/`
- Films/séries : `/Users/cabezer225/Documents/ChatGPT/Film/`

## Dégustation — Milan street food (02/10/2026)

- **Notes successives :** v03 10/6, v04 10/8, v05 10/9, puis sa reprise v06 (premier cas de la notation hook/rétention, SKILL §5.2).
- **Blancs :** Milan v02 4,2 / min ; ses reels 13 à 18 / min (méthode étalonnée §5.2).
- **Scripts (exemples à adapter, ils pilotent AE et génèrent le XML, ils ne fabriquent pas d'image)** dans `Tiktok degustation/Milan-StreetFood/Controle/` :
  - `plan_milan_v05.py` — plan de montage ;
  - `creer_habillage_milan_v05.py` — création des compositions d'habillage dans AE ;
  - `creer_sous_titres_milan_v05.py` — paquets de sous-titres ;
  - `mix_milan_v05.py` — mixage ;
  - `generer_montage_milan_v05.py` — FCP XML d'assemblage ;
  - `injecter_couleur_mouvements_milan_v05.py` — couleur et mouvements.
- **Séquence :** 2160 × 3840 à 29,97 i/s ; export 1080 × 1920.
- **Hook teaser :** « 19h30 · Luini ferme à 20h ⏰ ».
- **Langue des sous-titres :** anglais.

## Dégustation — autres repères

- Maritozzo (Naples, 28/09) : « Bref, c'est partiiii » ; sous-titres anglais ; retour v09 sur les légendes Premiere génériques.
- Pizza-Naples (27/09) : appel au commentaire de fin toujours conservé ; étiquette « Pizza fritta · Naples » retirée par Cabezer (pas de texte ajouté pour relancer l'image).
- Fiches d'identité : `Tiktok degustation/Identite-Degustation/DA-Degustation-v2.md`, `Tiktok degustation/Identite-Voyage/DA-Voyage-v1.md` ; emojis : `Identite-Degustation/Emojis/` ; script de notation : `Identite-Degustation/noter_hook_retention.py` ; banque SFX : `SFX-Pixabay/` et `LICENCES-SFX.md` ; reels de référence : `References-Cabezer/`.

## Story — « Comment les fast-foods ont changé notre génération » (`Fast-food-generation-2026-09-21/`)

- **Étude B-roll / animations / son** de 9 passages de Micode, Amistory et Liv : `Coordination/ANALYSE-BROLL-ANIMATIONS-SON-MICODE-AMISTORY-LIV.md` (base de la méthode « une image par idée », validée le 29/09 sur la démo partie 3).
- **Identité v15 rose :** fiche `Coordination/v15/IDENTITE-ROSE-v15.md` ; bibliothèque ExtendScript `Habillage-Story-v01/Scripts/v15/lib_rose_v15.jsx`.
- **Générique « Amed Story 🧢 » v01 :**
  - rendu : `Habillage-Story-v01/Rendus/Generique/GENERIQUE_Amed_Story_v01_4K.mov` (4K avec son) et une variante sans impact initial ;
  - projet AE : `AE/Generique-Amed-Story-v01.aep`, une précomposition par lettre ;
  - musique : `Audio/Generique/` ;
  - modèle d'origine : son générique « HISTOIRE DE FOOD / BY AHMED » (vidéo des scandales de restaurants, 0:49,6–0:57,6).
- **Musique v10 (première application de la composition en 2–3 thèmes, 30/09) :** `Audio/MUSIQUE_v10_THEMES_0-19m03.wav` ; scripts `Habillage-Story-v01/Scripts/v15/musique/compose_v10_themes.py` et `exs_sampler.py` ; feuille de cue `Coordination/v15/MUSIQUE-v10-partition.md`.

## Films/séries

- PRISME v1 validé sur Dune ; zoom fluide IN-OUT rejeté sur Dune (14/09).
- Musiques : `/Users/cabezer225/Downloads/MUSIQUES` et `/Users/cabezer225/Documents/ChatGPT/Film/musique`.
