# Audit indépendant — tranche T23-I (maths 9ᵉ, devoirs T2′ salle blanche, ch. 09-triangle-rectangle-trigo, missions 42 → 46)

Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md` lue en entier, skill `content-audit` invoqué).
Périmètre : `/home/user/wt-m22`, `content/math/09-triangle-rectangle-trigo/exercices/42…46-devoir-*.json` (5 missions, 34 questions).
Cartes lues : `plan/assign-T23-I.md` (aucun texte source). Aucune source de devoir, aucune note d'auteur, rien de
`sources-externes/` ouvert. Rien n'est modifié dans les fichiers audités ; aucune écriture git. Rapport écrit au fil de l'eau.
Référence publiée : `origin/main` du corpus au commit `5a762ac2` (missions d'examen 47–51 du chapitre comprises).
Moteur de rendu : `/home/user/eng-m22` (`618147d`).

## 1. Réponses à l'aveugle (posées AVANT lecture des clés, explications et étiquettes)

Énoncés et options extraits par script sans `correctOption`, `explanation` ni `misconceptionTag` ; chaque calcul refait
(sympy pour les radicaux et les encadrements, coordonnées des figures recalculées par script).

- 42 : Q1 (37 − 33)(37 + 33) · Q2 28 (D = 280 = 2³ × 5 × 7) · Q3 (−9 ; −12) · Q4 18 (C(9 ; 12)) · Q5 7√2 · Q6 7√3 (√147) · Q7 √3/3.
- 43 : Q1 3 (AH² = 16 − 7) · Q2 6,5 < BH < 7 · Q3 9/7 < CH < 18/13 (CH ≈ 1,354 dedans) · Q4 32 + 8√7 · Q5 2 + 2√7
  (ab = 4, a² + 7b² = 32) · Q6 2√7 − 2 (|2 − 2√7|) · Q7 24 (= AH × BC = 3 × 8) · Q8 8 + 4√7.
- 44 : Q1 « AB² + AC² = 900 = BC², قائم في A » · Q2 14,4 · Q3 216 · Q4 15 · Q5 10 · Q6 4,8 (Thalès dans KAH, KG/KA = 1/3) · Q7 72 (= 216/3).
- 45 : Q1 18 · Q2 24 (EF = 25) · Q3 75 · Q4 9 (756/84) · Q5 5√5 · Q6 « AB² + BC² = AC², قائم في B ».
- 46 : Q1 6√3 · Q2 11 · Q3 x² > 4 · Q4 0 ≤ x² < 9 · Q5 AB² + BC² + CG² · Q6 9.

**Comparaison aux clés : 34/34 identiques. Aucune clé fausse.**

## 2. Tableaux par fichier

Verdict : OK, ERREUR (clé fausse, aucune), **réserve** (défaut classé au § 3).

### 42 — ⭐⭐ d2 practice 75/15 (rampe 1,2,2,2,2,2,2)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | (37 − 33)(37 + 33) | c | OK | b étiquetée `difference-carres-confondue`, exacte |
| 2 | 28 | a | réserve | M5 : l'énoncé « D = 4 × 70 » livre la clé de Q1 |
| 3 | (−9 ; −12) | d | OK | b `symetrie-regle-confondue`, c `coordonnees-point-inversees`, exactes |
| 4 | 18 | b | réserve | M5 : l'énoncé donne B(−9 ; −12), clé de Q3 |
| 5 | 7√2 | c | OK | triangle rectangle donné dans l'énoncé ; trois étiquettes exactes |
| 6 | 7√3 | a | réserve (mineure) | m4 : AC = 7√2 = clé de Q5 (fuite structurelle) |
| 7 | √3/3 | d | réserve | M4 : « في المكعّب نفسه » ; m4 : AG = 7√3 = clé de Q6 |

### 43 — 👑 d4 challenge 300/60 (rampe 2,2,3,3,3,3,3,3)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | 3 | a | réserve | M1 (triangle publié ×2) |
| 2 | 6,5 < BH < 7 | c | réserve | M1 ; m1 (mécanisme de b faux) |
| 3 | 9/7 < CH < 18/13 | d | réserve | M1 ; M5 (énoncé = clé de Q2) ; m5 (paire miroir) |
| 4 | 32 + 8√7 | b | réserve | M1 ; plan 2×2 exact |
| 5 | 2 + 2√7 | d | réserve | M1 |
| 6 | 2√7 − 2 | a | réserve | M1 ; M4 « بالطريقة نفسها » ; d (= AB) et b (= CH) impossibles à obtenir sans les autres questions |
| 7 | 24 | c | réserve | M1 |
| 8 | 8 + 4√7 | b | réserve | M1 ; m6 (une étape, d3 pour l'ordre) |

### 44 — ⚔️ d3 boss 120/30 (rampe 1,2,2,2,3,3,3)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | AB² + AC² = BC², قائم في A | b | réserve | M2 (triangle de 09/07) ; m7 (titre) |
| 2 | 14,4 | d | réserve | **M2 : doublon exact de 09/07 Q2** ; m2 |
| 3 | 216 | a | réserve | M2 |
| 4 | 15 | c | réserve | M2 |
| 5 | 10 | b | réserve | **M2 : doublon de facto de 08/07 Q2** ; **M6** (figure) |
| 6 | 4,8 | d | réserve | M5 (AK = 15 inutile, clé de Q4) ; **M7** (figure « G′ ») |
| 7 | 72 | a | réserve | **M8** (75/150 impossibles à obtenir ; d étiquetée à deux erreurs) |

### 45 — ⚔️ d3 boss 120/30 (rampe 1,2,2,3,3,3)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | 18 | c | OK | d `mediane-hypotenuse-demi` acceptable |
| 2 | 24 | a | OK | c `hypotenuse-mal-choisie`, d `pythagore-sans-carres`, exactes |
| 3 | 75 | d | OK | — |
| 4 | 9 | b | OK (mineure m4) | sans k² : aires calculées ; « 3 » = rapport des longueurs ET des périmètres, `echelle-aire-rapport-non-carre` acceptée ; DF = 24 = clé de Q2 (structurelle) |
| 5 | 5√5 | a | réserve | M5 : Q6 affiche AC² = 125 (énoncé ET options) |
| 6 | قائم في B | c | réserve | M4 « في المعلّم نفسه » ; M5 ; **M10** (titre livre « زاوية قائمة ») |

### 46 — ⭐⭐ d2 practice 75/15 (rampe 1,1,2,2,2,2)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | 6√3 | d | OK (m3) | explication muette sur 8√3 et 24 |
| 2 | 11 | a | OK | étiquettes exactes ; gabarit voisin de 02/05 Q5 (m8) |
| 3 | x² > 4 | c | OK | — |
| 4 | 0 ≤ x² < 9 | b | réserve | **M9** : technique non enseignée ; a « 0 ≤ x² < 5 » sans mécanisme réel |
| 5 | AB² + BC² + CG² | d | OK | triangles rectangles donnés ; étiquettes exactes |
| 6 | 9 | a | réserve | **M3** (pavé publié 20/02 Q4) ; **M4** (« في العلبة نفسها » : insoluble seul) |

## 3. Défauts classés

### Critiques
Aucun : 34/34 clés justes, aucune explication contradictoire, aucune figure fausse en géométrie (coordonnées recalculées :
43 rectangle en A à 10⁻¹² près, BH/CH = (4 + √7)/(4 − √7), AH = 3 à l'échelle ; 44 AB = 162 px = 18 × 9, AC = 216 px,
G = A + (2/3)(K − A) exact, L entre H et K ; 45 repère O(80 ; 100), unité 20 px, A, B, C exacts, AB ⊥ BC ; cubes en
perspective cavalière cohérents).

### Majeurs

- **M1 — 43 est le triangle publié de 09/13 multiplié par 2.** 09/13 (même chapitre, même étage d4, publié) : AB = √7 + 1,
  AC = √7 − 1, BC = 4, AH = 3/2, BH = (4 + √7)/2. 43 : AB = 2√7 + 2, AC = 2√7 − 2, BC = 8, AH = 3, BH = 4 + √7. Mêmes pièges
  (|2 − 2√7| contre |1 − √7| en 13 Q4 ; BH × CH en 13 Q8 ; AB × AC en 13 Q6). Correctif : **même chaîne, autre triangle**,
  q = 14 : BH = 9 ± 2√14, AH = 5, BC = 18, AB = 3√14 + 6, AC = 3√14 − 6, AB × AC = 90, périmètre 18 + 6√14 ; encadrement
  3 < √14 < 4 (deux étapes ×2 puis +9, digne du d4). Les huit questions sont réécrites au § 7 (avec la figure SVG43) ;
  elles corrigent aussi M4 (Q6), M5 (Q3) et m1 (Q2 b). Vérifié : 43 contrôles sympy (chaque clé unique, chaque
  distracteur faux et produit par son mécanisme), clé jamais strictement la plus longue (Q4 : 11 = 11 signes ; Q5, Q6 :
  quatre options de 8 signes), aucune option somme de deux autres, plan 2×2 en Q4 (162 / 112 + 36√14 / 112 muette),
  aucun vote terme à terme vers la clé (Q5 : premiers termes 9, 18, 2, 6 ; seconds 2√14, √14, 9√14, 3√14), √14 absent
  des missions publiées du chapitre sous cette forme.
- **M2 — 44 reprend le triangle 18-24-30 de 09/07.** 44 Q2 = 09/07 Q2 (mêmes données, même question, même clé 14,4) ;
  44 Q5 = 08/07 Q2 de facto (mêmes quatre options 22,5 / 10 / 7,5 / 5, même clé 10). Correctif : triangle **27-36-45**
  (même forme 3-4-5, les figures restent vraies) : AH = 21,6, aire 486, AK = 22,5, AG = 15, GK = 7,5, GL = 7,2,
  aire GBC = 162 (= 486/3). Textes au § 7. Vérifié : aucun 27-36-45 ni AH = 21,6 publié en maths ; dupscan après correctif :
  plus aucune paire à options communes.
- **M3 — 46 Q6 reprend le pavé de 20/02-boss Q4** (AB = AD = 4, diagonale 9, arête 7, distracteur √65 commun). Correctif :
  pavé 6 × 6 × 7, AG = 11 (options 11 / 19 / 121 / √85), figure SVG46 refaite à l'échelle (§ 7).
- **M4 — Autonomie** : 42 Q7 « في المكعّب نفسه », 43 Q6 « بالطريقة نفسها » (et ses options b = CH, d = AB, absents de
  l'énoncé), 45 Q6 « في المعلّم نفسه », 46 Q6 « في العلبة نفسها » (les triangles rectangles ABC et ACG ne sont posés qu'en Q5 :
  Q6 ne se résout pas seule). Correctifs au § 7 (énoncés qui redonnent cube, repère, ou prémisses).
- **M5 — Fuites évitables (donjon)** : 42 Q2 « D = 4 × 70 » → clé de Q1 ; 42 Q4 « B(−9 ; −12) » → clé de Q3 ;
  43 Q3 « 6,5 < BH < 7 » → clé de Q2 ; 44 Q6 « AK = 15 », donnée inutile à la clé → clé de Q4 ; 45 Q6 « AB² = 25 … AC² = 125 »
  dans l'énoncé ET les options → clé de Q5 (5√5 = √125). Correctifs : 42 Q2 pose D = 37² − 33² (explication par
  1369 − 1089, sans l'écriture factorisée) ; 42 Q4 prend C symétrique de A par (OJ) (24 et 30 deviennent les règles de
  (OI) et de O, toutes deux `symetrie-regle-confondue`) ; 43 Q3 redonne BH = 9 + 2√14 et l'encadrement de √14 ;
  44 Q6 donne BC = 45 à la place de AK ; 45 Q6 sans valeurs (calcul des trois carrés demandé, options « ≠ / = » sans nombre).
- **M6 — 44 Q5 : la figure place G aux deux tiers, à l'échelle** : 7,5 (milieu) et 5 (tiers depuis A) se réfutent à l'œil,
  22,5 > AK. Correctif : retirer le point G et son étiquette (le cours 08 montre déjà la position ; ici l'élève la calcule).
- **M7 — 44 Q6 : la figure nomme « G′ » le pied que l'énoncé appelle L.** Correctif : étiquette « L », décalée à x = 138
  pour ne plus toucher « K » (le point ne bouge pas).
- **M8 — 44 Q7 : 75 et 150 utilisent GK = 5, absent de l'énoncé** (distracteurs impossibles à obtenir), et 150 (deux
  erreurs) porte `aire-triangle-sans-moitie`. Correctif : l'énoncé pose K et G (GK devient calculable), d muette.
- **M9 — 46 Q4 : le carré d'un encadrement qui contient 0 n'est enseigné nulle part** (cours 17 : bornes positives, bornes
  négatives, |x| ≤ |y| ⟺ x² ≤ y² ; 17/06-defi Q1 publié : intervalle négatif seulement). Correctif : l'énoncé donne le
  découpage en deux cas (technique donnée, clé non désignée : c reste le piège « tout carrer ») ; a « 0 ≤ x² < 5 » (« طرح 4
  من 9 », aucun mécanisme réel) devient « 0 ≤ x² < 13 » (somme des deux encadrements, opération du cours mal appliquée).
- **M10 — 45 : le titre « … وزاوية قائمة في المعلّم » donne le verdict de Q6** (a et b s'éliminent). Correctif :
  `⚔️ زعيم الفرض ⭐⭐⭐: موسّط الوتر، مقارنة مساحتين، ومربّعات المسافات في المعلّم`.

### Mineurs

- **m1** — 43 Q2 b « 5 < BH < 5,5 » : « إضافة 4 إلى حصر أضيق » ne le produit pas (il faudrait 1 < √7 < 1,5, faux). Réglé
  par M1 (b = « 11 < BH < 12 », √81 + √56 fusionnés en √137, `racine-distribuee-sur-somme`, libellé exact « tu fusionnes
  deux racines ainsi »).
- **m2** — 44 Q2 a (28,8) : « مضاعفة النتيجة » ne nomme aucune erreur. Réglé par M2 (43,2 = oubli du « ÷ 2 » d'un seul côté).
- **m3** — 46 Q1 : l'explication ne dit rien de 8√3 ni de 24. Phrase ajoutée (§ 7).
- **m4 — fuites structurelles (donjon seulement, la quête est saine)** : l'énoncé redonne la valeur dont l'étape a besoin —
  42 Q6 (AC = 7√2), 42 Q7 (AG = 7√3), 43 Q4 (AH), Q5 (AB²), Q7-Q8 (AB, AC), 44 Q6 (AH), Q7 (GL), 45 Q4 (DF = 24) ; et 44 Q4 b
  affiche AH (piège « hauteur pour médiane »). Inhérent au découpage T2′ (« chaque question s'appuie sur la précédente ») ; à
  garder, aucune ne descend sous la question qu'elle dévoile.
- **m5** — 43 Q3 a (`inverse-conserve-l-ordre`) : l'étiquette est exacte, mais l'option est un intervalle vide, miroir de
  la clé ; on peut choisir « celui des deux qui est rangé ». Toute exécution de cette erreur donne un intervalle vide :
  acceptée, sans correctif.
- **m6 — étages** : 43 d4 sans question d4 — conforme aux 14 missions « devoir » d4 publiées (toutes plafonnent à d3).
  43 Q8 et 44 Q7 sont des calculs d'une étape, laissés en d3 pour rester après la question dont leur énoncé reprend la clé.
- **m7** — 44 : le titre « عكس فيثاغورس » oriente Q1 vers « قائم ». Facultatif : `⚔️ زعيم الفرض ⭐⭐⭐: مربّعات الأضلاع ثمّ مركز ثقل ومساحة`.
- **m8 — gabarits voisins (imposés par les cartes, acceptés)** : 42 Q5-Q6 et 46 Q5-Q6 (diagonale d'un solide) ; 44 Q4 et
  45 Q1 (médiane = moitié de l'hypoténuse) ; 43 Q7 et 46 Q2 (produit de conjugués, mêmes deux étiquettes) ; 44 et 09/12
  (réciproque → médiane → AG) ; 46 Q2 et 02/05 Q5 ; 42 Q5-Q6 et 20/01 Q3, 20/17 Q2 (cube 6 et 5). Données et options
  différentes.
- **m9 — programme** : « médiane = moitié de l'hypoténuse » n'est enseignée que par une puce « حالة خاصّة » de la méthode du
  cours 08 (§ « ⚖️ مركز ثقل المثلّث ») ; le cours 09 ne l'énonce pas. Suffisant ici (08 précède 09) ; à signaler à la session
  « cours ».
- **m10** — 42 Q2 b, c `divisibilite-un-seul-critere` : le libellé parle de « deux critères (6 = 2 × 3) », l'erreur exécutée
  est un contrôle partiel des facteurs de 30 = 2 × 3 × 5 et 42 = 2 × 3 × 7 ; proche, acceptée.
- **m11 — figures (cosmétique)** : AC et AG tracés pleins alors qu'ils traversent ou longent des faces cachées (convention
  de surlignage, admise) ; 46 Q5, étiquette F barrée par l'arête FG (corrigée dans SVG46 : F à (143 ; 64)).
- **m12** — 44 Q7 sans figure ; facultatif : reprendre la figure de Q6.

## 4. Étiquettes et familles proposées

Toutes les étiquettes posées ont été relues contre les libellés d'`origin/main` (`content/misconceptions.json`) : exactes
(liste : `difference-carres-confondue`, `divisibilite-un-seul-critere` (m10), `symetrie-regle-confondue`,
`coordonnees-point-inversees`, `pythagore-racine-oubliee`, `pythagore-sans-carres`, `facteur-racine-sans-carre` (49√2),
`hypotenuse-mal-choisie` (42 Q6, 43 Q4, 44 Q1, 45 Q2-Q3-Q6, 46 Q5), `rationalisation-denominateur-oublie` (√3 = multiplier
sans diviser par 3), `difference-carres-somme-au-lieu-de-difference`, `relation-hauteur-racine-oubliee`,
`relation-hauteur-somme-au-lieu-de-produit`, `inverse-conserve-l-ordre`, `carre-somme-sans-double-produit`,
`racine-carre-sans-valeur-absolue`, `difference-carres-second-terme-non-eleve-au-carre`, `angle-droit-mauvais-sommet`,
`relation-aire-mauvais-cote`, `aire-triangle-sans-moitie`, `hauteur-confondue-avec-mediane`, `mediane-hypotenuse-demi`,
`centre-gravite-milieu-mediane`, `centre-gravite-tiers-inverse`, `echelle-aire-rapport-non-carre` (sa première phrase est
l'erreur exacte ; l'échelle n'y est qu'un exemple), `distance-sans-racine`, `racine-distribuee-sur-somme`,
`carre-conserve-l-ordre`, `diagonale-du-pave-en-deux-dimensions` (compétence du ch. 20, notion déjà connue, triangles donnés)).
Seule fausse pose : 44 Q7 d (deux erreurs) → muette (M8). Options à deux erreurs muettes ailleurs : 43 Q4 c, 44 Q7 d corrigée.

| famille proposée | questions | publiées équivalentes | verdict |
|---|---|---|---|
| `math.num.carre-encadrement-contenant-zero` | 1 (46 Q4 c) | 0 (17/06 Q1 : intervalle négatif seulement) | **REJET** — < 3 questions ; l'erreur exécutée (carrer les bornes en gardant l'ordre) est celle de `carre-conserve-l-ordre`, déjà posée : la garder |
| `math.num.denominateur-radical-conserve` | 1 (42 Q7 c) | 0 (02/02 Q1 « 2/√2 » et 02/04 Q4 « 1/(√5 − 2) » sont d'autres erreurs) | **REJET** — < 3 questions ; 42 Q7 c reste muette |

## 5. Points de l'orchestrateur

- **44 et le centre de gravité : CONFIRMÉ.** Le cours `08-thales` (§ « ⚖️ مركز ثقل المثلّث », sur `origin/main`) enseigne la
  propriété AG = (2/3) × AK, GK = (1/3) × AK, sa preuve, les deux pièges étiquetés, et, dans la méthode, le cas du triangle
  rectangle (« الموسّط … نصفُ الوتر، إذن AG = (2/3) × (BC/2) = BC/3 »). 08 précède 09 dans le manifeste : Q5-Q7 restent
  (avec M6, M7, M8). Thalès (Q6) relève aussi de 08.
- **Cube (42) et pavé (46)** : triangles rectangles bien donnés dans 42 Q5, Q6 et 46 Q5 ; manquants en 46 Q6 (M4, corrigé).
- **45 sans k²** : conforme ; aires calculées, « 3 » exécute bien « rapport des longueurs/périmètres pris pour celui des aires ».
- **43 Q3 `inverse-conserve-l-ordre` sur intervalle vide** : étiquette exacte, acceptée (m5).
- **43 Q1 ↔ Q4** : paire proche acceptée (AH² = BH × CH contre Pythagore dans AHB, données et options différentes).
- **44 Q1 QCM d'énoncés complets** : sain (b et c de même longueur, plan calcul × sommet) ; seul le titre oriente (m7).
- **Familles neuves** : les deux rejetées, options muettes (§ 4).

## 6. Rendu, doublons, contrôles

- Rendu `dir=rtl` (Chromium, `splitMathRuns`/`isDisplayEquation` de `/home/user/eng-m22`) : 0 formule brouillée sur les 34
  questions d'origine ET sur les 22 questions corrigées (dont « BH = 9 + 2√14 » en phrase, « AB² + AC² ≠ BC²، … » en option).
  `lot-lint` : 0 point sur l'origine comme sur la version corrigée (après déplacement du ✓ de 43 Q8 : « = 6√14 + 18 ✓ »).
- Doublons : `dupscan.py` adapté au ch. 09 (missions 42-46 contre tout le publié de maths d'`origin/main`, quiz compris),
  plus recherches ciblées (triplets, valeurs-clés, solides) : M1, M2, M3 trouvés ; après correctifs, plus aucune paire à
  options communes (restent des parallèles de formulation, m8).
- Étages/en-têtes : 42 et 46 d2 practice 75/15, 43 d4 challenge 300/60, 44 et 45 d3 boss 120/30 ; `displayOrder` = préfixe ;
  rampes non décroissantes ; titres au format, aucun n'énonce un résultat sauf 45 (M10).
- Notation : chiffres latins, aucun LaTeX, `;` dans les couples, aucune virgule arabe dans une notation.

## 7. Textes de remplacement (vérifiés)

Chaque bloc donne les champs à substituer, tels quels, dans la question nommée (ordre et `id` des options inchangés ;
`correctOption` inchangé partout). Vérification : copies corrigées construites hors du dépôt, puis sympy (43 contrôles),
`lot-lint`, banc Chromium `dir=rtl`, `dupscan`, et rendu des trois figures neuves ou retouchées. Hors blocs : titre de 45
(M10, texte au § 3).

**42 Q2** — champs remplacés : prompt, explanation
```json
{
 "prompt": "العدد D معرَّف كما يلي:\nD = 37² − 33²\nأيّ عدد من الأعداد التالية يقسم D ؟",
 "explanation": "نحسب D = 37² − 33² = 1369 − 1089 = 280، ثمّ نفكّكه إلى عوامل أوّلية: 280 = 2³ × 5 × 7. العدد 28 يساوي 2² × 7 وعاملاه موجودان في التفكيك، فهو قاسم لـ D ✓. أمّا 30 = 2 × 3 × 5 و 42 = 2 × 3 × 7 فكلّ منهما يحتاج العامل 3 وهو غائب، و 16 = 2⁴ يحتاج أربعة عوامل 2 بينما في D ثلاثة فقط. الخطأ الشائع: التحقّق من بعض العوامل فقط، كأن نرى 2 و 5 في 30 أو 2 و 7 في 42 ونحكم بالقسمة دون السؤال عن العامل 3."
}
```

**42 Q4** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "وحدة الطول في معلّم متعامد ومتجانس هي السنتيمتر، ونعلم أنّ:\nA(−9 ; 12)\nالنقطة C مناظرة A بالنسبة إلى محور التراتيب (OJ). ما طول القطعة [AC] بالسنتيمتر ؟",
 "options": [
  {
   "id": "a",
   "text": "15"
  },
  {
   "id": "b",
   "text": "18"
  },
  {
   "id": "c",
   "text": "24",
   "misconceptionTag": "math.vec.symetrie-regle-confondue"
  },
  {
   "id": "d",
   "text": "30",
   "misconceptionTag": "math.vec.symetrie-regle-confondue"
  }
 ],
 "explanation": "المناظرة بالنسبة إلى محور التراتيب (OJ) تُبقي الترتيبة وتغيّر إشارة الفاصلة فقط، فـ C(9 ; 12). للنقطتين A و C الترتيبة نفسها 12، فالقطعة [AC] أفقيّة وطولها فرق الفاصلتين: AC = 9 − (−9) = 18 ✓. الخطأ الشائع: الخلط بين المحورين فيخرج 24؛ أو تغيير الإشارتين معًا كأنّها مناظرة بالنسبة إلى المبدإ O فيخرج 30؛ أو أخذ المسافة OA بدل AC، وهي 15."
}
```

**42 Q7** — champs remplacés : prompt
```json
{
 "prompt": "في المكعّب ABCDEFGH نعلم أنّ:\nAG = 7√3\nCG = 7\nما قيمة النسبة التالية مكتوبةً دون جذر في المقام ؟\nCG / AG"
}
```

**43 Q1** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "ABC مثلّث قائم في A، و H المسقط العمودي للنقطة A على القطعة [BC]. نعلم بالسنتيمتر أنّ:\nBH = 9 + 2√14\nCH = 9 − 2√14\nما طول الارتفاع [AH] بالسنتيمتر ؟\n[SVG43 — ci-dessous]",
 "options": [
  {
   "id": "a",
   "text": "5"
  },
  {
   "id": "b",
   "text": "√137",
   "misconceptionTag": "math.alg.difference-carres-somme-au-lieu-de-difference"
  },
  {
   "id": "c",
   "text": "25",
   "misconceptionTag": "math.geo.relation-hauteur-racine-oubliee"
  },
  {
   "id": "d",
   "text": "3√2",
   "misconceptionTag": "math.geo.relation-hauteur-somme-au-lieu-de-produit"
  }
 ],
 "explanation": "علاقة الارتفاع في المثلّث القائم: AH² = BH × CH. إذن AH² = (9 + 2√14)(9 − 2√14) = 81 − 56 = 25، لأنّ (2√14)² = 4 × 14 = 56، ومنه AH = √25 = 5 ✓. الخطأ الشائع: جمع القطعتين بدل ضربهما، AH² = 18 فيخرج √18 = 3√2؛ أو جمع المربّعين في جداء المرافقين، 81 + 56 = 137 فيخرج √137؛ أو التوقّف عند AH² = 25 دون أخذ الجذر."
}
```

**43 Q2** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "نعلم أنّ العدد √14 محصور كما يلي:\n3 < √14 < 4\nأيّ حصر للعدد BH = 9 + 2√14 صحيح ؟",
 "options": [
  {
   "id": "a",
   "text": "27 < BH < 41"
  },
  {
   "id": "b",
   "text": "11 < BH < 12",
   "misconceptionTag": "math.num.racine-distribuee-sur-somme"
  },
  {
   "id": "c",
   "text": "15 < BH < 17"
  },
  {
   "id": "d",
   "text": "12 < BH < 13"
  }
 ],
 "explanation": "نضرب أطراف الحصر في 2 الموجب فلا يتغيّر الترتيب: 6 < 2√14 < 8. ثمّ نضيف 9 إلى الأطراف الثلاثة، والإضافة لا تغيّر الترتيب: 9 + 6 < 9 + 2√14 < 9 + 8، أي 15 < BH < 17 ✓. الخطأ الشائع: نسيان المعامل 2 فيُضاف 9 إلى حصر √14 وحده، فيخرج 12 < BH < 13؛ أو تربيع الحدّين، 9 + 2 × 9 و 9 + 2 × 16، فيخرج 27 < BH < 41؛ أو إدخال 9 و 2√14 تحت جذر واحد، √81 + √56 كأنّه √137، والجذر لا يُجمع هكذا، فيُحصر √137 بين 11 و 12."
}
```

**43 Q3** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "نعلم أنّ:\nBH = 9 + 2√14\n3 < √14 < 4\nBH × CH = 25\nأيّ حصر للطول CH صحيح ؟",
 "options": [
  {
   "id": "a",
   "text": "5/3 < CH < 25/17",
   "misconceptionTag": "math.num.inverse-conserve-l-ordre"
  },
  {
   "id": "b",
   "text": "375 < CH < 425"
  },
  {
   "id": "c",
   "text": "8 < CH < 10"
  },
  {
   "id": "d",
   "text": "25/17 < CH < 5/3"
  }
 ],
 "explanation": "نحصر BH أوّلًا: من 3 < √14 < 4 نجد 6 < 2√14 < 8 ثمّ 15 < BH < 17. ومن BH × CH = 25 نكتب CH = 25 / BH. المرور إلى المقلوب يقلب الترتيب بين عددين موجبين: 1/17 < 1/BH < 1/15. نضرب الأطراف في 25 الموجب فلا يتغيّر الترتيب: 25/17 < CH < 25/15، أي 25/17 < CH < 5/3 ✓. الخطأ الشائع: الحفاظ على الترتيب نفسه عند المقلوب، فيُكتب 5/3 < CH < 25/17 وهو مجال فارغ لأنّ 5/3 أكبر من 25/17؛ أو ضرب الحدّين في 25 دون قسمة فيخرج 375 < CH < 425؛ أو طرح BH من 25 فيخرج 8 < CH < 10."
}
```

**43 Q4** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "في المثلّث ABC القائم في A، والنقطة H المسقط العمودي للنقطة A على [BC]، نعلم بالسنتيمتر أنّ:\nAH = 5\nBH = 9 + 2√14\nما قيمة AB² ؟\n[SVG43 — ci-dessous]",
 "options": [
  {
   "id": "a",
   "text": "162",
   "misconceptionTag": "math.alg.carre-somme-sans-double-produit"
  },
  {
   "id": "b",
   "text": "162 + 36√14"
  },
  {
   "id": "c",
   "text": "112"
  },
  {
   "id": "d",
   "text": "112 + 36√14",
   "misconceptionTag": "math.geo.hypotenuse-mal-choisie"
  }
 ],
 "explanation": "المثلّث AHB قائم في H ووتره [AB]. بنظرية فيثاغورس: AB² = AH² + BH² = 25 + (9 + 2√14)² = 25 + 81 + 36√14 + 56 = 162 + 36√14 ✓. الخطأ الشائع: اعتبار [BH] هو الوتر فتُطرح المربّعات، 137 + 36√14 − 25، فيخرج 112 + 36√14؛ أو نسيان الجداء المضاعف عند نشر مربّع المجموع فيخرج 162؛ أو الخطآن معًا فيخرج 112."
}
```

**43 Q5** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "نعلم أنّ:\nAB² = 162 + 36√14\nأيّ العبارات التالية تساوي AB دون جذر متداخل ؟",
 "options": [
  {
   "id": "a",
   "text": "9 + 2√14"
  },
  {
   "id": "b",
   "text": "18 + √14"
  },
  {
   "id": "c",
   "text": "2 + 9√14"
  },
  {
   "id": "d",
   "text": "6 + 3√14"
  }
 ],
 "explanation": "نبحث عن عبارة a + b√14 مربّعها a² + 14b² + 2ab√14، فيلزم 2ab = 36 و a² + 14b² = 162. نتحقّق بالتربيع: (6 + 3√14)² = 36 + 36√14 + 126 = 162 + 36√14 ✓، والعدد 6 + 3√14 موجب فهو AB. أمّا العبارات الأخرى فتحقّق 2ab = 36 دون الشرط الثاني: (9 + 2√14)² = 137 + 36√14، و (18 + √14)² = 338 + 36√14، و (2 + 9√14)² = 1138 + 36√14. الخطأ الشائع: الاكتفاء بالجداء المضاعف 36√14 دون التحقّق من الحدّ الناطق 162؛ ومنه اعتبار AB = BH مع أنّ الوتر [AB] أطول من الضلع [BH] في المثلّث AHB."
}
```

**43 Q6** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "في المثلّث ABC القائم في A نعلم أنّ:\nAC² = 162 − 36√14\nما طول AC بالسنتيمتر ؟",
 "options": [
  {
   "id": "a",
   "text": "3√14 − 6"
  },
  {
   "id": "b",
   "text": "9 − 2√14"
  },
  {
   "id": "c",
   "text": "6 − 3√14",
   "misconceptionTag": "math.num.racine-carre-sans-valeur-absolue"
  },
  {
   "id": "d",
   "text": "9√14 − 2"
  }
 ],
 "explanation": "نلاحظ أنّ (3√14 − 6)² = 126 − 36√14 + 36 = 162 − 36√14 ✓، وكذلك (6 − 3√14)² يعطي العدد نفسه. الجذر التربيعي لمربّع عدد هو قيمته المطلقة: AC = |6 − 3√14|. وبما أنّ (3√14)² = 126 أكبر من 6² = 36 فإنّ 3√14 > 6، والعدد 6 − 3√14 سالب، إذن AC = 3√14 − 6 ✓. الخطأ الشائع: كتابة √(a²) = a دون اختبار الإشارة فيخرج عدد سالب لا يصلح طولًا؛ أو الاكتفاء بالجداء المضاعف 36√14 دون التحقّق من الحدّ الناطق، فـ (9 − 2√14)² = 137 − 36√14 و (9√14 − 2)² = 1138 − 36√14."
}
```

**43 Q7** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "نعلم بالسنتيمتر أنّ:\nAB = 3√14 + 6\nAC = 3√14 − 6\nما قيمة الجداء AB × AC ؟",
 "options": [
  {
   "id": "a",
   "text": "162",
   "misconceptionTag": "math.alg.difference-carres-somme-au-lieu-de-difference"
  },
  {
   "id": "b",
   "text": "6"
  },
  {
   "id": "c",
   "text": "90"
  },
  {
   "id": "d",
   "text": "120",
   "misconceptionTag": "math.alg.difference-carres-second-terme-non-eleve-au-carre"
  }
 ],
 "explanation": "هذا جداء مرافقين: (a + b)(a − b) = a² − b² مع a = 3√14 و b = 6. إذن AB × AC = (3√14)² − 6² = 126 − 36 = 90 ✓. الخطأ الشائع: جمع المربّعين بدل طرحهما فيخرج 162؛ أو عدم تربيع الحدّ الثاني فيخرج 126 − 6 = 120؛ أو تربيع الجذر وحده كأنّه 3 × 14 فيخرج 42 − 36 = 6."
}
```

**43 Q8** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "في المثلّث ABC القائم في A، والنقطة H المسقط العمودي للنقطة A على القطعة [BC]، نعلم بالسنتيمتر أنّ:\nAB = 3√14 + 6\nAC = 3√14 − 6\nBH = 9 + 2√14\nCH = 9 − 2√14\nما محيط المثلّث ABC بالسنتيمتر ؟",
 "options": [
  {
   "id": "a",
   "text": "6√14"
  },
  {
   "id": "b",
   "text": "18 + 6√14"
  },
  {
   "id": "c",
   "text": "30 + 6√14"
  },
  {
   "id": "d",
   "text": "24√14"
  }
 ],
 "explanation": "H تقع على القطعة [BC] فـ BC = BH + CH = (9 + 2√14) + (9 − 2√14) = 18. المحيط هو AB + AC + BC = (3√14 + 6) + (3√14 − 6) + 18 = 6√14 + 18 ✓، فالحدّان 6 و −6 يتلاشيان. الخطأ الشائع: نسيان الضلع BC فيخرج 6√14؛ أو أخذ الضلع AC مساويًا AB فيخرج 30 + 6√14؛ أو جمع 18 و 6√14 كأنّهما حدّان متشابهان فيخرج 24√14."
}
```

**44 Q1** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "أطوال أضلاع المثلّث ABC بالسنتيمتر:\nAB = 27\nAC = 36\nBC = 45\nأيّ الاستدلالات التالية صحيح ؟",
 "options": [
  {
   "id": "a",
   "text": "AB + AC = 27 + 36 = 63، وهو يخالف BC، إذن المثلّث ليس قائمًا",
   "misconceptionTag": "math.geo.pythagore-sans-carres"
  },
  {
   "id": "b",
   "text": "AB² + AC² = 729 + 1296 = 2025 = BC²، إذن المثلّث قائم في A"
  },
  {
   "id": "c",
   "text": "AB² + AC² = 729 + 1296 = 2025 = BC²، إذن المثلّث قائم في B",
   "misconceptionTag": "math.geo.angle-droit-mauvais-sommet"
  },
  {
   "id": "d",
   "text": "AB² + BC² = 729 + 2025 = 2754، وهو يخالف AC²، إذن المثلّث ليس قائمًا",
   "misconceptionTag": "math.geo.hypotenuse-mal-choisie"
  }
 ],
 "explanation": "في عكس نظرية فيثاغورس نقارن مربّع أطول ضلع بمجموع مربّعي الضلعين الآخرين. أطول ضلع هو [BC]: AB² + AC² = 729 + 1296 = 2025 و BC² = 2025، فالمساواة محقّقة والمثلّث قائم ✓. والزاوية القائمة تقابل الوتر [BC]، فهي إذن في الرأس A المقابل له. الخطأ الشائع: وضع الزاوية القائمة في أحد طرفي الوتر؛ أو مقارنة مربّع ضلع قصير مع مجموع مربّعين يدخل فيهما الوتر؛ أو جمع الأطوال دون تربيعها."
}
```

**44 Q2** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "ABC مثلّث قائم في A، والنقطة H المسقط العمودي للنقطة A على (BC)، ونعلم بالسنتيمتر أنّ:\nAB = 27\nAC = 36\nBC = 45\nما طول الارتفاع [AH] بالسنتيمتر ؟\n[SVG d'origine de 44 Q2, inchangé]",
 "options": [
  {
   "id": "a",
   "text": "43,2"
  },
  {
   "id": "b",
   "text": "60",
   "misconceptionTag": "math.geo.relation-aire-mauvais-cote"
  },
  {
   "id": "c",
   "text": "972"
  },
  {
   "id": "d",
   "text": "21,6"
  }
 ],
 "explanation": "نحسب مساحة المثلّث ABC بطريقتين: (AH × BC)/2 و (AB × AC)/2. إذن AH × BC = AB × AC، أي AH × 45 = 27 × 36 = 972، ومنه AH = 972 ÷ 45 = 21,6 ✓. الخطأ الشائع: ضرب الارتفاع في ضلع قائم بدل الوتر، AH × AB = AC × BC، فيخرج 60؛ أو التوقّف عند الجداء 972 دون القسمة؛ أو نسيان القسمة على 2 في أحد الطرفين، (AH × BC)/2 = AB × AC، فيخرج 43,2."
}
```

**44 Q3** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "ABC مثلّث قائم في A، و AB = 27 و AC = 36 بالسنتيمتر. ما مساحة المثلّث ABC بالسنتيمتر المربّع ؟",
 "options": [
  {
   "id": "a",
   "text": "486"
  },
  {
   "id": "b",
   "text": "607,5"
  },
  {
   "id": "c",
   "text": "810"
  },
  {
   "id": "d",
   "text": "972",
   "misconceptionTag": "math.mes.aire-triangle-sans-moitie"
  }
 ],
 "explanation": "في المثلّث القائم يمكن أخذ أحد الضلعين القائمين قاعدةً والآخر ارتفاعًا: S = (AB × AC)/2 = (27 × 36)/2 = 486 ✓. الخطأ الشائع: نسيان القسمة على 2 فيخرج 972؛ أو أخذ الوتر قاعدةً مع ضلع قائم ارتفاعًا، وهما غير متعامدين، فيخرج 810 أو 607,5."
}
```

**44 Q4** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "ABC مثلّث قائم في A، و K منتصف وتره [BC]، ونعلم بالسنتيمتر أنّ:\nAB = 27\nAC = 36\nBC = 45\nما طول الموسّط [AK] بالسنتيمتر ؟\n[SVG d'origine de 44 Q4, inchangé]",
 "options": [
  {
   "id": "a",
   "text": "11,25"
  },
  {
   "id": "b",
   "text": "21,6",
   "misconceptionTag": "math.geo.hauteur-confondue-avec-mediane"
  },
  {
   "id": "c",
   "text": "22,5"
  },
  {
   "id": "d",
   "text": "45",
   "misconceptionTag": "math.geo.mediane-hypotenuse-demi"
  }
 ],
 "explanation": "في المثلّث القائم الموسّط الصادر من رأس الزاوية القائمة يساوي نصف الوتر: AK = BC / 2 = 45 / 2 = 22,5 ✓. الخطأ الشائع: خلط الموسّط بالارتفاع الصادر من الرأس نفسه، وهما قطعتان مختلفتان لأنّ الارتفاع لا يصل إلى المنتصف؛ أو نسيان القسمة على 2؛ أو القسمة على 2 مرّتين فيخرج 11,25."
}
```

**44 Q5** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "ABC مثلّث قائم في A، و BC = 45 cm، و K منتصف [BC]، و G مركز ثقل المثلّث ABC. ما طول القطعة [AG] بالسنتيمتر ؟\n[SVG d'origine de 44 Q5 SANS le point G : retirer <circle cx=\"142.4\" cy=\"156.8\" r=\"4.5\" fill=\"#d97706\"/> et <text x=\"154.4\" y=\"152.8\" text-anchor=\"middle\" fill=\"#d97706\" font-size=\"15\">G</text>]",
 "options": [
  {
   "id": "a",
   "text": "11,25",
   "misconceptionTag": "math.geo.centre-gravite-milieu-mediane"
  },
  {
   "id": "b",
   "text": "15"
  },
  {
   "id": "c",
   "text": "33,75"
  },
  {
   "id": "d",
   "text": "7,5",
   "misconceptionTag": "math.geo.centre-gravite-tiers-inverse"
  }
 ],
 "explanation": "الموسّط [AK] الصادر من رأس الزاوية القائمة يساوي نصف الوتر: AK = 22,5. ومركز الثقل G يقع على [AK] عند ثلثيه انطلاقًا من الرأس A: AG = (2/3) × 22,5 = 15 ✓، وبقية الموسّط GK = 7,5. الخطأ الشائع: وضع G في منتصف الموسّط فيخرج 11,25؛ أو عدّ الثلث من الرأس A بدل منتصف الضلع فيخرج 7,5؛ أو استعمال النسبة 3/2 بدل 2/3 فيخرج 33,75."
}
```

**44 Q6** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "ABC مثلّث قائم في A، و AH ارتفاعه، و K منتصف [BC]، و G مركز ثقله، و L المسقط العمودي للنقطة G على (BC)، والمستقيمان (GL) و (AH) متوازيان. نعلم بالسنتيمتر أنّ:\nAH = 21,6\nBC = 45\nما طول GL بالسنتيمتر ؟\n[SVG d'origine de 44 Q6 où <text x=\"146.4\" y=\"219\" text-anchor=\"middle\" fill=\"#2563eb\" font-size=\"14\">G′</text> devient <text x=\"138\" y=\"219\" text-anchor=\"middle\" fill=\"#2563eb\" font-size=\"14\">L</text>]",
 "options": [
  {
   "id": "a",
   "text": "7,5"
  },
  {
   "id": "b",
   "text": "10,8",
   "misconceptionTag": "math.geo.centre-gravite-milieu-mediane"
  },
  {
   "id": "c",
   "text": "14,4",
   "misconceptionTag": "math.geo.centre-gravite-tiers-inverse"
  },
  {
   "id": "d",
   "text": "7,2"
  }
 ],
 "explanation": "النقاط K و G و A على استقامة واحدة، والنقاط K و L و H على (BC)، و (GL) ∥ (AH). بنظرية طاليس في المثلّث KAH: GL/AH = KG/KA. ومركز الثقل يجعل KG ثلث الموسّط KA، فـ GL = AH/3 = 21,6 ÷ 3 = 7,2 ✓. الخطأ الشائع: استعمال النسبة 2/3 المأخوذة من الرأس A بدل 1/3 المأخوذة من منتصف الضلع فيخرج 14,4؛ أو وضع G في منتصف الموسّط فيخرج 10,8؛ أو أخذ GL مساويًا القطعة المائلة GK، وهي ثلث الموسّط 22,5، فيخرج 7,5."
}
```

**44 Q7** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "ABC مثلّث قائم في A و BC = 45 cm، و K منتصف [BC]، و G مركز ثقله، و L المسقط العمودي للنقطة G على (BC)، ونعلم أنّ GL = 7,2 cm. ما مساحة المثلّث GBC بالسنتيمتر المربّع ؟",
 "options": [
  {
   "id": "a",
   "text": "162"
  },
  {
   "id": "b",
   "text": "168,75"
  },
  {
   "id": "c",
   "text": "324",
   "misconceptionTag": "math.mes.aire-triangle-sans-moitie"
  },
  {
   "id": "d",
   "text": "337,5"
  }
 ],
 "explanation": "مساحة مثلّث هي نصف جداء قاعدته في ارتفاعه، والارتفاع الموافق للقاعدة [BC] هو GL العمودي عليها: S = (BC × GL)/2 = (45 × 7,2)/2 = 162 ✓. الخطأ الشائع: نسيان القسمة على 2 فيخرج 324؛ أو أخذ القطعة المائلة GK، وهي ثلث الموسّط 22,5 أي 7,5، مكان الارتفاع GL فيخرج 168,75، ومع نسيان القسمة على 2 أيضًا 337,5."
}
```

**45 Q6** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "في معلّم متعامد ومتجانس (O, I, J) وحدة الطول فيه السنتيمتر، نعلم أنّ:\nA(−2 ; −2)\nB(1 ; 2)\nC(9 ; −4)\nأيّ الاستدلالات التالية صحيح ؟\n[SVG d'origine de 45 Q6, inchangé]",
 "options": [
  {
   "id": "a",
   "text": "AB² + AC² ≠ BC²، إذن المثلّث ABC ليس قائمًا",
   "misconceptionTag": "math.geo.hypotenuse-mal-choisie"
  },
  {
   "id": "b",
   "text": "AB + BC ≠ AC، إذن المثلّث ABC ليس قائمًا",
   "misconceptionTag": "math.geo.pythagore-sans-carres"
  },
  {
   "id": "c",
   "text": "AB² + BC² = AC²، إذن المثلّث ABC قائم في B"
  },
  {
   "id": "d",
   "text": "AB² + BC² = AC²، إذن المثلّث ABC قائم في A",
   "misconceptionTag": "math.geo.angle-droit-mauvais-sommet"
  }
 ],
 "explanation": "نحسب مربّعات الأضلاع بقاعدة المسافة: AB² = (1 + 2)² + (2 + 2)² = 9 + 16 = 25، و BC² = (9 − 1)² + (−4 − 2)² = 64 + 36 = 100، و AC² = (9 + 2)² + (−4 + 2)² = 121 + 4 = 125. أطول ضلع هو [AC] لأنّ مربّعه 125 هو الأكبر، و AB² + BC² = 25 + 100 = 125 = AC². المساواة محقّقة، فبعكس نظرية فيثاغورس المثلّث قائم، وزاويته القائمة مقابلة للوتر [AC]، أي في الرأس B ✓. الخطأ الشائع: وضع الزاوية القائمة في الرأس A؛ أو مقارنة مجموع مربّعين يدخل فيهما الوتر مع مربّع ضلع قصير، AB² + AC² = 150 وهو يخالف BC²؛ أو جمع الأطوال دون تربيعها، 5 + 10 = 15 وهو يخالف AC."
}
```

**46 Q1** — champs remplacés : explanation
```json
{
 "explanation": "نخرج أكبر مربّع كامل من كلّ جذر: √48 = √(16 × 3) = 4√3، و √12 = √(4 × 3) = 2√3. الجذران متشابهان فنجمع المعاملين: 4√3 + 2√3 = 6√3 ✓. الخطأ الشائع: جمع ما تحت الجذرين، √48 + √12 = √60، وهذه القاعدة لا تصحّ إلّا مع الجداء. وضرب المعاملين 4 × 2 = 8 مع الإبقاء على √3 يعطي 8√3، وهو خلط بين الجمع والضرب؛ وضرب الجذرين √48 × √12 = √576 = 24 يحسب الجداء لا المجموع."
}
```

**46 Q4** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "x عدد حقيقي يحقّق:\n−2 < x < 3\nنميّز حالتين:\n−2 < x < 0\n0 ≤ x < 3\nأيّ حصر للعدد x² صحيح ؟",
 "options": [
  {
   "id": "a",
   "text": "0 ≤ x² < 13"
  },
  {
   "id": "b",
   "text": "0 ≤ x² < 9"
  },
  {
   "id": "c",
   "text": "4 < x² < 9",
   "misconceptionTag": "math.num.carre-conserve-l-ordre"
  },
  {
   "id": "d",
   "text": "0 ≤ x² < 4"
  }
 ],
 "explanation": "في الحالة الأولى −2 < x < 0 العددان سالبان، والتربيع يقلب ترتيب السالبين: 0 < x² < 4. وفي الحالة الثانية 0 ≤ x < 3 العددان موجبان، والتربيع يحفظ ترتيب الموجبين: 0 ≤ x² < 9. العدد x² يقع في إحدى الحالتين، وكلتاهما داخل الحصر 0 ≤ x² < 9، إذن 0 ≤ x² < 9 ✓، والقيمة 0 تُبلَغ عند x = 0. الخطأ الشائع: تربيع حدّي الحصر مباشرة فيخرج 4 < x² < 9 مع أنّ x = 0 مسموح به؛ أو الاكتفاء بالحالة الأولى فيخرج 0 ≤ x² < 4 مع أنّ x = 2,5 يعطي 6,25؛ أو جمع حصري الحالتين طرفًا بطرف كأنّهما حصرا عددين مختلفين فيخرج 0 ≤ x² < 13."
}
```

**46 Q6** — champs remplacés : prompt, options, explanation
```json
{
 "prompt": "ABCDEFGH علبة على شكل متوازي مستطيلات قاعدتها ABCD مربّعة، والمثلّث ABC قائم في B والمثلّث ACG قائم في C. نعلم بالسنتيمتر أنّ:\nAB = 6\nBC = 6\nCG = 7\nما طول القطر [AG] بالسنتيمتر ؟\n[SVG46 — ci-dessous]",
 "options": [
  {
   "id": "a",
   "text": "11"
  },
  {
   "id": "b",
   "text": "19",
   "misconceptionTag": "math.geo.pythagore-sans-carres"
  },
  {
   "id": "c",
   "text": "121",
   "misconceptionTag": "math.geo.pythagore-racine-oubliee"
  },
  {
   "id": "d",
   "text": "√85",
   "misconceptionTag": "math.esp.diagonale-du-pave-en-deux-dimensions"
  }
 ],
 "explanation": "AC² = AB² + BC² = 36 + 36 = 72، ثمّ AG² = AC² + CG² = 72 + 49 = 121، إذن AG = √121 = 11 ✓. الخطأ الشائع: استعمال بعدين فقط، 36 + 49 = 85 فيخرج √85؛ أو جمع الأبعاد الثلاثة دون تربيعها فيخرج 19؛ أو التوقّف عند AG² = 121."
}
```

**SVG43** (43 Q1 et Q4 ; triangle BC = 18, BH = 9 + 2√14, AH = 5 à l'échelle 280/18 px par cm ; produit scalaire en A ≈ 0) :
```
<svg viewBox="0 0 330 175"><title>مثلّث ABC القائم في A وارتفاعه AH</title><polygon points="276.4,72.2 20,150 300,150" fill="#0f6e56" fill-opacity="0.09" stroke="#0f172a" stroke-width="2.2" stroke-linejoin="round"/><line x1="276.4" y1="72.2" x2="276.4" y2="150" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round" stroke-dasharray="6 4"/><path d="M 267.8 74.8 L 270.4 83.4 L 279 80.8" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M 268.4 150 L 268.4 142 L 276.4 142" fill="none" stroke="#0f6e56" stroke-width="1.6"/><circle cx="276.4" cy="72.2" r="3.5" fill="#0f172a"/><circle cx="20" cy="150" r="3.5" fill="#0f172a"/><circle cx="300" cy="150" r="3.5" fill="#0f172a"/><circle cx="276.4" cy="150" r="3.5" fill="#0f172a"/><g font-weight="700" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="272.4" y="61" text-anchor="middle" fill="#0f172a" font-size="15">A</text><text x="14" y="169" text-anchor="middle" fill="#0f172a" font-size="15">B</text><text x="314" y="169" text-anchor="middle" fill="#0f172a" font-size="15">C</text><text x="272.4" y="169" text-anchor="middle" fill="#0f6e56" font-size="15">H</text></g></svg>
```

**SVG46** (46 Q6 ; pavé 6 × 6 × 7 en perspective cavalière, 20 px par unité, fuyante (10 ; −7) par unité, comme l'original) :
```
<svg viewBox="0 0 254 246"><title>علبة ABCDEFGH قاعدتها مربّعة</title><polygon points="34,212 154,212 154,72 34,72" fill="#0f6e56" fill-opacity="0.08" stroke="none"/><line x1="34" y1="212" x2="94" y2="170" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="5 4"/><line x1="94" y1="170" x2="214" y2="170" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="5 4"/><line x1="94" y1="170" x2="94" y2="30" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="5 4"/><line x1="34" y1="212" x2="154" y2="212" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><line x1="154" y1="212" x2="214" y2="170" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><line x1="214" y1="170" x2="214" y2="30" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><line x1="34" y1="212" x2="34" y2="72" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><line x1="154" y1="212" x2="154" y2="72" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><line x1="34" y1="72" x2="154" y2="72" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><line x1="154" y1="72" x2="214" y2="30" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><line x1="214" y1="30" x2="94" y2="30" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><line x1="34" y1="72" x2="94" y2="30" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><line x1="34" y1="212" x2="214" y2="170" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><line x1="214" y1="170" x2="214" y2="30" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><line x1="34" y1="212" x2="214" y2="30" stroke="#d97706" stroke-width="2.6" stroke-linecap="round"/><circle cx="34" cy="212" r="3.5" fill="#0f172a"/><circle cx="154" cy="212" r="3.5" fill="#0f172a"/><circle cx="214" cy="170" r="3.5" fill="#0f172a"/><circle cx="94" cy="170" r="3.5" fill="#0f172a"/><circle cx="34" cy="72" r="3.5" fill="#0f172a"/><circle cx="154" cy="72" r="3.5" fill="#0f172a"/><circle cx="214" cy="30" r="3.5" fill="#0f172a"/><circle cx="94" cy="30" r="3.5" fill="#0f172a"/><g font-weight="700" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="23" y="228" text-anchor="middle" fill="#0f172a" font-size="15">A</text><text x="166" y="228" text-anchor="middle" fill="#0f172a" font-size="15">B</text><text x="227" y="175" text-anchor="middle" fill="#0f172a" font-size="15">C</text><text x="106" y="161" text-anchor="middle" fill="#0f172a" font-size="15">D</text><text x="23" y="67" text-anchor="middle" fill="#0f172a" font-size="15">E</text><text x="143" y="64" text-anchor="middle" fill="#0f172a" font-size="15">F</text><text x="227" y="24" text-anchor="middle" fill="#0f172a" font-size="15">G</text><text x="91" y="20" text-anchor="middle" fill="#0f172a" font-size="15">H</text></g></svg>
```

## 8. Bilan

- Questions auditées : **34** (5 missions). Clés fausses : **0**. Critiques : **0**.
- Majeurs : **10** (M1 43 = triangle publié 09/13 ×2 ; M2 44 = triangle de 09/07, doublon exact Q2 et de facto Q5 ;
  M3 46 Q6 = pavé de 20/02 Q4 ; M4 autonomie ×4 ; M5 fuites évitables ×5 ; M6 figure 44 Q5 livre G ; M7 figure 44 Q6
  « G′ » au lieu de L ; M8 44 Q7 distracteurs impossibles + étiquette à deux erreurs ; M9 46 Q4 technique non enseignée ;
  M10 titre de 45).
- Mineurs : 12 (dont 3 réglés par les correctifs majeurs).
- Questions à reprendre : **22** — 43 entière (8, renumérotée q = 14), 44 entière (7, renumérotée 27-36-45, figures Q5/Q6
  retouchées), 42 Q2, Q4, Q7, 45 Q6 (+ titre), 46 Q1 (explication), Q4, Q6. Textes exacts au § 7.
- Étiquettes : toutes exactes sauf 44 Q7 d (→ muette) ; les deux familles neuves **rejetées** (une question chacune), options
  muettes.
- Doublons : 3 trouvés contre le publié (M1, M2, M3), aucun après correctifs.
- **Verdict : à corriger avant livraison** (fix-first) ; après application du § 7, la tranche est livrable (re-vérification
  de l'orchestrateur : gates `--tranche` + relecture des 22 questions reprises).
