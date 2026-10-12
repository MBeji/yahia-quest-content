# Re-vérification ciblée — tranche L21 (maths 9ᵉ, ch. 09, missions 47 à 51)

Contre-audit de l'application de `audit-L21.md`. Arbre `/home/user/wt-m21` tel quel ; publié lu sur `origin/main`
9a3090c9 ; moteur `/home/user/eng-m21`. Aucun fichier modifié, aucune écriture git. Écarts de l'auteur lus à la fin
de `auteurs-notes/l21/NOTES.md`.

## Méthode

- Les 28 questions ré-extraites SANS clé (`blind.py`) et re-résolues. Je l'ai fait d'abord pour les questions
  retouchées et leurs voisines (47 Q2-Q4, 48 Q1-Q7, 50 en entier après renumérotation, 51 Q3-Q6), puis seulement
  comparées aux clés : **28/28 justes**.
- Textes de l'audit comparés par script, caractère pour caractère, au fichier.
- Recherche de recouvrements d'options sur les 2 291 questions de `content/math/` de `origin/main` (≥ 3 options
  communes, ou ≥ 2 avec la même clé), et à l'intérieur du lot.
- Rendu Chromium `dir=rtl` de 173 chaînes (titres, énoncés, options, explications) avec `splitMathRuns` /
  `isDisplayEquation` du moteur ; figures de 50 comparées octet par octet aux correctifs rendus dans l'audit.
- Gates : `content:check` vert ; `content:qa:strict` 0 erreur, aucun avertissement sur 47-51 ;
  `content:tranche --chapters 09` : clé strictement la plus longue 0/28 sur le lot, aucune paire proche qui touche
  47-51.

## Correctifs de l'audit — appliqués mot pour mot

| correctif | état |
| --- | --- |
| 47 Q4 énoncé (demi-disque collé, « الشكل الناتج ») | identique |
| 47 Q4 phrase « حدّ الشكل الناتج … فصارت داخله ، فمحيطه » | identique ; l'auteur a aussi récrit le piège (« وهو صار داخل الشكل وليس من حدّه ») : cohérent avec le nouvel énoncé, accepté |
| 47 Q2 explication + étiquette `int.produit-signes-negatifs` sur « −1 » | identique |
| titres 47 et 49 (« اختيار من متعدّد — ») | identiques |
| 48 Q1 « يمثّل التصميم التالي » | identique |
| 48 Q4 énoncé, options 2,4 / 2,5 / 12/7 / 0,48 + étiquettes, explication | identiques |
| 48 Q7 fin de l'explication (2160) | identique (U+00A0 de « 10 000 » gardée) |
| 50 Q4 → désormais Q5 : options, étiquettes, explication | identiques |
| 50 figure : « N » à y = 174 (six SVG), « 6 m » à (206 ; 128) | octet pour octet identiques aux SVG rendus dans l'audit |
| 50 « 10,8 » muette | fait |
| 51 en-tête practice d2 75/15 ⭐⭐, Q5-Q6 en d2 | fait ; rampe 1,1,2,2,2,2 |
| 51 Q3 énoncé, quatre options muettes, explication | identiques ; clé = « كلٌّ من (DE) و (CB) عمودي على المستقيم (AD) » |
| 51 Q5 « 5 » `operation-inverse-appliquee` + explication ; 51 Q6 « 4,5 » `segment-mal-choisi` | faits |

## Tableaux de re-résolution (questions retouchées et voisines)

| mission · Q | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| 47 Q2 | 3 | d (3) | OK |
| 47 Q3 | 10 | b (10) | OK — écart jugé plus bas |
| 47 Q4 | 14 + 5π | c | OK — les options 24 + … ne se rejettent plus à la lecture |
| 48 Q1 | Pythagore, AB² | c | OK |
| 48 Q2 | 5 | b (5) | OK — écart jugé plus bas |
| 48 Q3 | BC × AH ÷ 2 = AB × AC ÷ 2 | d | OK |
| 48 Q4 | 2,4 | a (2,4) | OK |
| 48 Q5 | 1,8 | b (1,8) | OK — écart jugé plus bas |
| 48 Q6, Q7 | 2,16 ; 216 | a ; c | OK |
| 50 Q1, Q2 | ABS théorème ; 6,5 | c ; a | OK |
| 50 Q3 (ex-Q5) | 4,2 | d (4,2) | OK |
| 50 Q4 (ex-Q3) | parallèles, ⟂ à (SB) | b | OK |
| 50 Q5 (ex-Q4) | SM/SA = SN/SB = MN/AB | a | OK — vote : rapports 1 et 2 sans majorité sur la clé, rapport 3 à égalité 2-2 |
| 50 Q6, Q7 | 1,75 ; 4,55 | b ; c | OK |
| 51 Q3 | « عمودي على المستقيم (AD) » | b | OK |
| 51 Q4, Q5, Q6 | AC/AD = AB/AE = CB/DE ; 6 ; 9 | d ; a ; c | OK |
| 47 Q1, 49 Q1-Q4, 51 Q1-Q2 | 150 ; 2, √3 − 1, −1, 30 ; c, √13 | inchangées | OK |

## Écarts de l'auteur — jugement

Contexte : sur ces trois questions, l'audit n'avait vu que les recouvrements par la même donnée (18/27 Q1). L'auteur
en a trouvé de plus forts, et je les confirme sur `origin/main`. **Ancien 47 Q3** {2√7, 10, 14, 100} avait LES QUATRE
options de `18-quadrilateres/09` Q1 et de `20-orthogonalite-espace/09` Q3, avec la même clé. **Ancien 48 Q5**
{0,6, 1,8, 3,24} en avait trois avec `18-quadrilateres/35` Q3 (clé 1,8). **Ancien 48 Q2** {√7, 5, 7, 25} avait les
mêmes quatre options que `09/31` Q1 (même palier boss) et trois avec `09/40` Q2. Les trois écarts étaient donc
nécessaires.

- **47 Q3 — accepté.** Options 2√7 (`hypotenuse-mal-choisie`, √28), 10, √14 (`pythagore-sans-carres`, √(8 + 6) :
  « additionnes les longueurs au lieu de leurs carrés », exact), 28 (muette : hypoténuse mal choisie ET racine
  oubliée, deux erreurs, nommée dans l'explication). Toutes fausses. Longueurs 3/2/3/2 : la clé n'est pas la plus
  longue. Il ne reste en commun avec le publié que {10, 2√7}, ce qui est inévitable sur le triangle 6-8-10. Le plan
  « hypoténuse × racine » est incomplet (100 est retiré), mais il ne désigne pas la clé.
- **48 Q2 — accepté, avec une réserve mineure.** Options √7 (`hypotenuse-mal-choisie`), 5, √12 (muette, « ضرب
  الطولين تحت الجذر »), 49 (muette, (3 + 4)², somme puis carré sans racine : deux erreurs). Toutes fausses, toutes
  nommées dans l'explication. Il ne reste en commun avec 09/31 Q1, 09/40 Q2 et 12/01-02 que {5, √7}, inévitable sur le
  triangle 3-4-5. Réserve : √(3 × 4) est une erreur rare (un produit de côtés pris pour le carré de l'hypoténuse).
  Elle reste plausible dans une mission où l'aire AB × AC revient en Q3-Q4, et elle n'est pas un remplissage pur.
  Je la garde. Pas de texte à reprendre.
- **48 Q5 — accepté.** 5,4 = 3 + 2,4 porte `pythagore-sans-carres` (« additionnes ou soustrais », exact), comme
  0,6. Seule {0,6, 1,8} reste commune avec 18/35 Q3, inévitable. Observation déjà faite dans l'audit : 5,4 et √14,76
  dépassent AB = 3 (l'hypoténuse de ABH), ce qui en élimine deux à vue. C'était déjà le cas avec 3,24. Pas un défaut
  nouveau.
- **50 Q5 → d1, placée 3ᵉ (Q1, Q2, SN, ⟂, chaîne, MN, SM) — accepté.** Rampe 1,1,1,2,2,3,3 non décroissante. Aucune
  fuite :
  - Q3 (SN) ne cite ni MN, ni la chaîne, ni le parallélisme.
  - Q6 (MN) ne donne pas SN : elle part de SB et BN. Son explication recalcule SN, qui est la clé de Q3 émise avant.
  - Q4 et Q5 ne contiennent aucun nombre.
  - Étiquettes de Q3 : 7,8 `operation-inverse-appliquee` exacte, 10,8 muette, 1,8 `segment-mal-choisi` exacte.
- **47 Q2 « −1 » étiquetée — accepté.** C'est l'erreur de signe du produit −2 × (−1) ; le libellé est exact. Elle
  porte la même étiquette que −3, ce qui est sans gêne : les deux chemins sont différents et chacun est nommé.

## Contrôles transverses après correction

- **Doublons.** Plus aucune question du lot n'a ≥ 3 options communes avec le publié, sauf des listes de petits
  entiers sans rapport (51 Q5 {4, 5, 6}, 51 Q6 {1, 6, 9} : autres questions, autres notions). 48 Q4 ↔ 18/25 Q3 :
  il ne reste que {2,4, 2,5}, et l'énoncé est désormais à deux étapes. 51 Q3 n'a plus le gabarit de 30 Q4 / 33 Q3.
  Dans le lot, seuls 47 Q2 et 49 Q3 partagent {−1, 1}, avec des questions sans rapport.
- **Longueurs.** Aucune clé n'est strictement la plus longue (0/28). 51 Q3 : clé de 43 caractères contre 58.
- **Fuites.** Aucune fuite en avant. Les données redonnées restent les « استنتج » de l'officiel. 48 Q4 ne redonne
  plus BC.
- **Rendu `dir=rtl`.** Aucune formule à lettre mal ordonnée. Les formules neuves « √(8 + 6) = √14 »,
  « √(3 × 4) = √12 » et « (3 + 4)² = 49 » sont isolées en `.math-run` et s'affichent dans l'ordre source. Les
  chaînes de chiffres seuls (« 3 + 2,4 = 5,4 », « 6 × 1,8 = 10,8 ») et « 10 g », « 1 cm » suivent le sens arabe, par
  conception du moteur. Aucun chiffre arabo-indien, aucun LaTeX, aucune espace simple dans un groupe de chiffres,
  aucune virgule arabe en notation, aucun « على الشكل ».
- **Figures de 50.** Le codage d'angle droit en N est visible et « 6 m » est à droite du mur (rendu vérifié dans
  l'audit, SVG identiques). Les autres figures sont inchangées.
- **Étiquettes.** Toutes figurent au registre `origin/main` (`content:check` vert). Les familles neuves restent
  écartées, et les options de 47 Q4 restent muettes.

## Chiffre final

| | questions | clés fausses | critiques | majeurs restants | mineurs restants |
| --- | --- | --- | --- | --- | --- |
| 47-51 | 28 | 0 | 0 | 0 | 0 bloquant (une réserve sur 48 Q2 « √12 », gardée ; aucun texte à reprendre) |

Les cinq majeurs de l'audit sont corrigés, ainsi que tous les mineurs retenus. Les trois écarts sont acceptés et
justifiés par des doublons réels sur `origin/main`.

**Verdict : livrable.**
