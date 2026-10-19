# Rapport — lot B4 (chapitres 16, 17, 18, 19 — mise à niveau)

Notes détaillées (table des écarts, puis ce qui a été fait) : `auteurs-notes/B4/NOTES.md`. Fiche : `content/programmes-officiels/programme/6eme-base/maths.md`. Pas de git de ma part.

## Constat commun
Les quatre cours étaient déjà au patron et couvraient presque toute la fiche ; les **quiz et les cinq exercices de chaque chapitre** datent de la première génération (reconnaissance répétée, une figure à lire, distracteurs absurdes) et n'exerçaient presque rien de ce que le cours enseigne (médiatrice, bissectrice, compas, grade, périmètre inverse, condition d'existence, diagonales). Aucun exercice ne déclarait de reprise.

## Par chapitre
| ch. | cours / résumé | questions remplacées → ajoutées | reprises déclarées (`manuel`) |
| --- | --- | --- | --- |
| 16 | + section « العمودي والموازي بالمسطرة والفرجار فقط » ; + carte de résumé ; figure du résumé réparée | 15 → +6 | L4 ex. 1, 2, 5 (102609) · rév. 6 ex. 1, 3ج (502603) |
| 17 | inchangés (déjà complets) | 9 → +7 | L7 ex. 1, 2, 6, 7, 8 · L4 ex. 4 |
| 18 | + section « المثلّث القائم المتساوي الساقين — نصف مربّع » ; périmètre « + une jambe » ; + 2 cartes | 17 → +7 | L8 ex. 4–9, 11 (102609) · rév. 7 ex. 2, 5, T3 sit. 3 (502603) |
| 19 | + sections « رسم شبه منحرف » et « كيف نُثبت أنّ رباعيًّا متوازي أضلاع » ; `**gras**` recollé ; + 2 cartes ; 2 `coursePitfalls` | 18 → +6 | L9 ex. 3, L15 ex. 2, 3, 9, L17 ex. 1, 6, 7, 8, 9, 11, L56 pb 1 · T1 sit. 3, T3 sit. 3, test d'orientation sit. 4 (502603) |

Défauts de fond corrigés : 16 `02-boss` q3 (énoncé « perpendiculaires », clé « parallèles ») ; 18 quiz q5 (« لونه », « محيط الدائرة ») ; 17 `05` q4 (« الفرجار فقط » discutable) ; 18 distracteur « مستقيم » ; 18 `02`/`04` « au plus un angle droit / obtus » justifiés par les perpendiculaires (cours) et non par une somme ; doublons de fait (une même figure « ⊥ ou ∥ ? » 6 fois ; « قائم » sur figure 5 fois ; « متوازي أضلاع / شبه منحرف » sur figure 4 fois) ; 4 explications qui désignaient « (د) » comme une option (lu comme l’option d) ; `renderSummary` ne rend pas `::: figure` (16).

**M3** : jamais la somme des angles d'un triangle. L7 ex. 11 (ص 23) **non reprise** ; l'angle de 45° d'un demi-carré est justifié par la diagonale qui coupe l'angle droit en deux ; l'« angle de 60° d'un équilatéral » est donné (« ce bâti donne 60°, on le vérifie au rapporteur »), jamais déduit. Condition d'existence : « le plus grand côté doit être plus petit que la somme des deux autres », sans le nom. Grade ✅ (L7 ex. 6 ; erratum p.200 L15 ex. 1 : 50 غراد = 45°, non repris). Errata appliqués : n° 14–17 (L17 ex. 6, 9, 11), n° 2 (L4 ex. 1 : « أ ن ب »). Non repris : L17 ex. 5 (SQ = diagonale, côté irrationnel), L15 ex. 9 (second polygone indécidable), L8 ex. 10 (bissectrices de l'équilatéral, ⛔), L9 ex. 8–9 (somme-différence, ◐ Q-5), T2 sit. 3 (lettres `[?]`).

## Étiquettes
Aucune étiquette inventée ; `misconceptions.json` non touché. **Ids proposés** (erreurs récurrentes ≥ 3 fois, laissées muettes) :
- `math.geo.mediatrice-un-seul-critere` — « une médiatrice passe par le milieu ET est perpendiculaire » (16 : 01 q5 b/a, 02 q3 d, 05 q2 b).
- `math.geo.arcs-ouvertures-permutees` — « l'ouverture du compas est la longueur du côté qu'on cherche à reporter de CE sommet » (18 : 03 q7 c ; 19 : 05 q3 c ; 16 : 02 q8, pitfall du cours).
- `math.geo.compas-ouverture-trop-petite` — arcs qui ne se rencontrent pas (16 : 01 q8 ; 18 : 03 q2, 04 q7 : somme égale ou inférieure).
- `math.geo.rapporteur-mauvaise-graduation` — lecture sur la mauvaise échelle (17 : 01 q8 b ; pitfall du cours).
- `math.geo.grade-et-degre-confondus` — « la droite vaut 100° » (17 : 01 q7 ; pitfall du cours) — aujourd'hui sous `valeur-angle-de-reference-confondue`.

## Doutes pour l'auditeur
- **D-1 (19)** : la section « critères de parallélogramme » énonce comme **conditions suffisantes** (sans les démontrer) : côtés opposés parallèles ; deux côtés opposés parallèles **et** égaux ; côtés opposés égaux ; diagonales de même milieu. La fiche borne « démonstrations formelles » ⛔ ; ces critères sont pourtant ce que demandent L56 pb 1 (« أثبت بأكثر من طريقة »), L17 ex. 1 (4 côtés égaux → losange) et les corrigés T3 (« parallélogramme = deux triangles égaux ») ; le cours de 19 les utilisait déjà (construction aux arcs, losange aux diagonales). À confirmer ; sinon retirer la section, 04 q7 et q8, et le `coursePitfalls` `condition-suffisante-supposee`.
- **D-2 (longueur)** : les cours dépassent largement 240 lignes (16 : ~490, 17 : ~590, 18 : ~700, 19 : ~630, figures comprises) ; la règle « au-delà de 240 lignes le chapitre se scinde » est une décision humaine — non tranchée ici.
- **D-3** : 04-defi du 19 déclare L56 sans `pages` (la leçon 56, ص 162, hors de la plage 27-30, 42-45, 47-49 du chapitre) ; idem L4 ex. 4 au 17.
- **D-4** : 02 q7 (19) et 05 q3 (18) utilisent « axes de symétrie du rectangle » et « diagonale = axe du carré » comme acquis de 5ᵉ (◐), non comme notion.
- **D-5** : « الفرجار » (corpus) / « البركار » (manuel) : usage du corpus gardé, le manuel cité une fois.
- Figures de cours : 360 de large (les anciennes : 340 à 450) ; tous les rendus ont été regardés.

## Contrôles
`content:check` ✓ · `content:qa` 0 erreur · `content:figures:check` ✓ · `content:tranche` (16–19, `--fresh --strict-longest --strict-lessons`) : clé la plus longue 0/57, paires proches 0, patron 0 en recul · `prettier --check` ✓ · rendu `renderLesson`/`renderSummary` propre (vitest jetable supprimé).
