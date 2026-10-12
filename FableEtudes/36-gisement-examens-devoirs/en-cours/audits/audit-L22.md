# Audit indépendant — tranche L22 (maths 9ᵉ, examens 2019 et 2022 technique : 18/42, 07/25, 12/22)

Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skill `content-audit`).
Périmètre : `/home/user/wt-m22` (arbre tel quel), 3 fichiers, 21 questions. Rien n'est modifié. Rapport écrit au fil de l'eau.

## Réponses à l'aveugle (posées AVANT toute lecture de clé, d'explication ou d'étiquette)

Chaîne officielle refaite par script (Fraction) depuis les transcriptions :
- 2019 ex.2 : OB = 30 ; OA = √(2500 − 900) = 40 ; AE/AB = 3/10 ; EF = 18 ; AK = 12 ; KO = 28 ;
  aire EFCB = (18 + 60)/2 × 28 = 1092 cm² = (60 × 40)/2 − (18 × 12)/2 = 1200 − 108 ✓ ; 0,1092 m² × 100 = 10,92 D.
- 2019 ex.3 : N = 200 ; centres 800 et 1000 ; cumuls 150 et 190 ; moyenne 138 000/200 = 690 ; médiane
  (interpolation) 500 + 200 × 50/70 = 642,86 ; 120/200 = 60 % sous 700 ; étendue 1300 − 300 = 1000 ; mode [500;700[.
- 2022 ex.1 : 0 solution de (x + 2)/2 = 1 + x ; AB = √(4 + 16) = 2√5 ; 6 − 4√2 = (2 − √2)² ; A(−3 ; 4), B(3 ; 4) symétriques par rapport à (OJ).

18/42 (énoncés et options lus sans clé) : Q1 30 · Q2 « [AB] hypoténuse, Pythagore » · Q3 40 · Q4 « (EF) // (BC), Thalès » ·
Q5 18 · Q6 12 · Q7 1092 · Q8 28 · Q9 10,92.

07/25 (sans clé) : Q1 200 · Q2 1000 · Q3 1000 · Q4 [500 ; 700[ · Q5 190 · Q6 60 % · Q7 690 (à confirmer sur le tableau SVG) ·
Q8 640 (642,86 lu sur le graphique ; la plus proche des options).
12/22 (sans clé) : Q1 (x + 2)/2 = 1 + x · Q2 2√5 · Q3 (2 − √2)² · Q4 la droite (OJ).

Toutes les clés des fichiers concordent ensuite avec ces réponses : **21/21, aucune clé fausse.**

## Méthode

- Transcriptions officielles lues d'abord (`examens-nationaux/9eme-base/math/2019-technique.md`, `2022-technique.md`), chaînes
  refaites par script (Fraction, sympy), énoncés et options extraits SANS clé ni explication ni étiquette, réponses notées
  ci-dessus, puis seulement comparaison aux `correctOption`.
- Registre des étiquettes, compétences, missions publiées : `origin/main` 5a762ac2 du corpus. Cours : arbre `wt-m22`
  (ch. 07, 12, 18 identiques à `origin/main`).
- Rendu : `splitMathRuns` / `isDisplayEquation` de `/home/user/eng-m22/src/shared/lib/bidi.ts` (identique à
  `origin/main` d'arena eeeea0e), banc `bench-rtl` (Chromium 1194, `dir=rtl`, 360/400/600 px) sur les trois fichiers ET sur
  chaque texte de remplacement ; figures rendues dans Chromium ; mesure des libellés SVG par `getBBox`.
- Gates (moteur `eng-m22`, contenu `wt-m22`) : `content:check` vert (120 matières) ; `content:qa:strict` 0 erreur, aucun
  avertissement sur les trois fichiers ; `content:tranche --chapters 18|07|12` : clé strictement la plus longue 0 sur la
  tranche ; une seule paire proche touche la tranche (12/22 Q2 ↔ 12/15 Q4, Jaccard 0,45 : autres points, autres options —
  pas un doublon).
- Doublons : scan des 21 questions contre tout le publié de maths (`origin/main`, quiz + missions) et entre elles.

---

## Fichier 18/42 — `42-examen-2019-technique-ex2-marbre-isocele-pythagore-thales-hauteur-aire-trapeze-prix.json`

En-tête : d3 · boss · 120/30 · displayOrder 42 · rampe 1,1,2,2,2,2,2,3,3 (non décroissante, ordre d'émission = ordre du
fichier). Titre « 🏛️ مناظرة 2019 (تقني) · التمرين 2 ⭐⭐⭐: … — فيثاغورس وطاليس والارتفاع والمساحة والثمن » conforme (notions,
aucun résultat). Fidélité : BC = 60, AB = AC = 50, O milieu, AE = 15, (EF) // (BC), K = (AO) ∩ (EF), 100 D/m² — toutes les
données sont celles du sujet ; les sous-questions 1a–1c, 2a–2b, 3a–3b, 4 sont toutes présentes (1b et 2a en justification
2×2, 4 découpée en aire / hauteur / prix).

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 (d1) | 30 | b (30) | OK | 60 ÷ 2 ; 25, 50, 60 exécutés et expliqués |
| 2 (d1) | [AB] hypoténuse + Pythagore | c | OK | plan 2×2 réel (côté × théorème, chaque case deux fois) ; prémisses : « [OA] وتر » faux, c'est le distracteur ; `hypotenuse-mal-choisie` exacte sur a, b et d muettes |
| 3 (d2) | 40 | c (40) | OK | √3400 `hypotenuse-mal-choisie`, 20 `pythagore-sans-carres`, 1600 `pythagore-racine-oubliee` : exactes |
| 4 (d2) | (EF) // (BC) + Thalès | d | OK | plan 2×2 réel (isocèle / parallèles × Thalès / Pythagore) ; prémisse « ABC isocèle » vraie mais non pertinente ; `thales-sans-verifier-parallelisme` exacte sur a ; c double muette |
| 5 (d2) | 18 | c (18) | OK · réserve | 200 `thales-rapport-inverse`, 25 `thales-longueurs-au-lieu-de-rapports` exactes ; 200 > BC tombe au raisonnement (précédent publié accepté) |
| 6 (d2) | 12 | a (12) | OK · **mineur** | F jamais défini dans l'énoncé (m-1) ; 5 et 400/3 étiquettes exactes |
| 7 (d2) | 1092 | c (1092) | OK · **majeur** | l'énoncé DONNE 28, clé de Q8 (fuite en avant) ; gabarit de 18/26 Q5 (M-1) |
| 8 (d3) | 28 | d (28) | OK · **mineur** | 50 > AO = 40 s'écarte au raisonnement ; 12 (AK, résultat intermédiaire) mérite l'étiquette existante (m-2) |
| 9 (d3) | 10,92 | c (10,92) | OK | 4,68 (hauteur AK), 21,84 `aire-trapeze-sans-demi-somme` exacte, 109,2 (÷ 1000) muette — chaîne complète, d3 honnête |

Figures : refaites (4,2 px/cm) — B(24 ; 200), C(276 ; 200), A(150 ; 32) : BC = 252 = 60 × 4,2, AO = 168 = 40 × 4,2,
AB = 210 = 50 × 4,2 ; E = A + 0,3(B − A) = (112,2 ; 82,4), F symétrique, K(150 ; 82,4) : exactes. Angle droit marqué en O
seulement quand l'énoncé le pose (Q2, Q3, Q8, Q9) ; [EF] en vert = l'objet, pas la clé ; arabe seulement dans `<title>` ;
rien ne déborde du `viewBox` (libellé O à y = 222 < 232, B à x = 12). Réserve : la figure est à l'échelle de la solution
(KO ≈ 0,7 AO se voit) ; le correctif de Q8 (35 au lieu de 50) rend cette lecture inopérante.

Fuites : Q2 redonne OB = 30 (clé Q1), Q6/Q8/Q9 redonnent AO = 40 (clé Q3), Q7 redonne EF = 18 (clé Q5) : toutes EN
ARRIÈRE, convention des étapes. **Q7 donne la hauteur 28 = clé de Q8, question SUIVANTE (quête) et tirable seule (donjon)
après Q7 : fuite en avant.** L'explication de Q9 recalcule 18, 28, 1092 (clés de Q5, Q8, Q7, toutes antérieures) : admis,
c'est la question finale. Aucune autre explication ne résout une question suivante.

Étage : d3 boss honnête — Q8 (Thalès puis différence) et surtout Q9 (Thalès, hauteur, aire, conversion cm² → m², prix,
depuis les seules données) sont des d3 réels ; Q1–Q2 d1 et Q3–Q7 d2 bien calibrées.

Programme : Pythagore (ch. 09) et Thalès (ch. 08) avant 18 dans le manifeste ; aire du trapèze au cours 18 (tableau
l. 488-495) ; aire du triangle et 1 m² = 10 000 cm² enseignés en `math-6eme/20-aires-polygones` (l. 142) : tout est
enseigné.

Doublons : aucun quasi-doublon publié (scan : max Jaccard d'énoncé 0,27). Les questions « لماذا / ما التبرير » ont des
sœurs en 18/25-28 (même type officiel, options et axes différents : direct/réciproque) : pas un doublon. **Q7 actuelle =
gabarit de 18/26 Q5** (« trapèze, bases et hauteur données, ما مساحته ؟ ») : renforce M-1.

### Défauts 18/42

- **[MAJEUR] M-1 — Q7 livre la clé de Q8 (et reprend le gabarit de 18/26 Q5).** « وارتفاعه 28 cm » est la clé de Q8.
  Correctif : Q7 calcule l'aire par différence (aire ABC − aire AEF, la seconde méthode), sans jamais écrire 28 ; elle reste
  d2, ne redonne que des clés ANTÉRIEURES (AO = 40 de Q3, EF = 18 de Q5, AK = 12 de Q6), réutilise la figure de Q8, et n'est
  plus le gabarit de 18/26 Q5. Texte exact plus bas (« Correctifs exacts »). Vérifié : 1200 − 108 = 1092 ; 1200 (aire de
  ABC seule) `math.alg.reponse-a-l-autre-inconnue` (« un résultat intermédiaire ») exacte ; 984 = 1200 − 216
  `math.mes.aire-triangle-sans-moitie` exacte ; 840 = 1200 − 360 (AO pris pour hauteur de AEF) muette ; aucune option somme
  ou différence de deux autres ; clé non strictement la plus longue (1200, 1092, 984, 840) ; aucune option n'est la clé
  d'une autre question ; explication sans 28 ni 10,92 ; banc Chromium : 0 formule à lettres brouillée (la première
  rédaction « مساحة EFCB = مساحة ABC − … » se brouillait : réécrite en « بطرح … من … »).
  Variante si l'auteur préfère garder la formule du trapèze : échanger Q7 et Q8 (hauteur en 7ᵉ position, d2 ; aire avec 28
  donnée en 8ᵉ, d2) — rampe 1,1,2,2,2,2,2,2,3, mais il ne resterait qu'un d3 et le gabarit 18/26 Q5 demeure : moins bon.
- **[MINEUR] m-1 — Q6 : F n'est pas défini** (« والنقطة E من [AB] حيث المستقيم (EF) يوازي (BC) »). Énoncé exact plus bas.
- **[MINEUR] m-2 — Q8 : 50 (= AB) dépasse AO = 40 donné** (la hauteur du trapèze ne peut excéder celle du triangle) et
  ne correspond à aucune erreur ; 12 (= AK) est un résultat intermédiaire que l'étiquette existante
  `math.alg.reponse-a-l-autre-inconnue` nomme exactement. Correctif : 50 → 35 (la jambe oblique [EB] = 50 − 15 prise pour
  hauteur, erreur que l'explication actuelle évoque déjà), 12 étiquetée. Vérifié : {12, 15, 35, 28} — aucune somme ou
  différence de deux options ne vaut 28 ; 35 < 40 (aucune prémisse niée) ; longueurs égales. La famille proposée
  « hauteur partielle (AK) » ne compte alors que 18 Q9 [4,68] : < 3 questions, **ne pas la créer**, 4,68 reste muette.
- Réserves sans correctif exigé : Q5 200 > BC et Q6 400/3 > AO (rapport inversé « absurde », pratique admise au publié) ;
  Q9 109,2 (÷ 1000) reste muette — `math.mes.conversion-aire-facteur-errone` dit « par 100, pas par 10 », pas ÷ 1000 ; ne
  pas la remplacer par 1092 (ce serait la clé de Q7 affichée en option de Q9).
- Rendu : « 468 cm² » (explication Q9) s'affiche unité à gauche ; l'ordre de lecture droite-gauche reste exact (cas moteur
  déjà classé en L13 m-16) : aucun correctif de contenu.

Verdict 18/42 : 9/9 clés justes ; 1 majeur, 2 mineurs ; à reprendre : Q6, Q7, Q8.

---

## Fichier 07/25 — `25-examen-2019-technique-ex3-usine-salaires-mediane-polygone-moyenne-classes.json`

En-tête : d3 · boss · 120/30 · displayOrder 25 · rampe 1,1,2,2,2,2,3,3. Titre « 🏛️ مناظرة 2019 (تقني) · التمرين 3 ⭐⭐⭐:
مرتّبات عمّال مصنع — المدى والمنوال والتراكم والنسبة والمعدّل والموسّط بالمضلّع » conforme. Fidélité : classes, effectifs
50/70/30/40/10, centres, cumuls, seuil 700, polygone (300 ; 0) … (1300 ; 200) : exacts ; sous-questions 1a (Q1), 1b (Q3
étendue, Q4 mode), 2a (Q2 centre, Q5 cumul), 2b (Q7), 3 (Q8), 4 (Q6) toutes présentes.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 (d1) | 200 | b (200) | OK | 5 (nombre de classes), 170, 160 (une classe oubliée) expliqués |
| 2 (d1) | 1000 | c (1000) | OK | 900/1100 `borne-de-classe-au-lieu-du-centre` exactes ; 800 muette expliquée |
| 3 (d2) | 1000 | a (1000) | OK · **mineur** | règle donnée puis application directe : d1 (m-3) ; 1600 `operation-inverse-appliquee` exacte |
| 4 (d2) | [500 ; 700[ | d | OK · **majeur** | « الفئة المنوالية » ni enseignée ni donnée (M-4) ; « الجدول التالي » sans tableau |
| 5 (d2) | 190 | b (190) | OK · **majeur** | 110 et 130 sans mécanisme, 130 inobtenable (M-3) ; terme « التراكمي الصاعد » absent du cours |
| 6 (d2) | 60 % | c (60 %) | OK · **mineur** | « بين 700 و900 » : bornes floues pour le piège du seuil (m-4) ; 40 % = complément, étiquette existante |
| 7 (d3) | 690 | a (690) | OK · **majeur** | tableau SVG illisible : libellés de classes plus larges que leurs cellules (M-5) ; étiquettes exactes |
| 8 (d3) | 640 | d (640) | OK · **majeur** | seule option non multiple de 100 : la clé se choisit par la forme (M-2) |

Calculs : moyenne 138 000 ÷ 200 = 690 ; 590 (bornes inférieures, 118 000 ÷ 200) `borne-de-classe-au-lieu-du-centre`
exacte ; 800 (centres non pondérés) `moyenne-sans-ponderation` exacte ; 27 600 (÷ 5) `moyenne-divisee-par-le-nombre-de-valeurs`
exacte. Médiane : 500 + 200 × 50/70 = 642,86. **La lecture graphique justifie 640** : sur la figure, l'ordonnée 100
(y = 115 px, ligne de grille présente) coupe le segment (114,5 ; 152,5)–(161,5 ; 100) en x = 148,1 px, 10 px à droite de la
verticale 600 sur un pas de 23,5 px : « un peu moins de la moitié entre 600 et 700 », soit ≈ 640 ; 600/700 sont lisiblement
faux. Les distracteurs à 40 d'écart sont défendables au graphique ; ce qui ne l'est pas, c'est la forme (M-2).

Figures : polygone exact (x : 23,5 px pour 100 D, 300 ↦ 67,5 ; y : 0,75 px par ouvrier, 50 ↦ 152,5, 120 ↦ 100, 150 ↦ 77,5,
190 ↦ 47,5, 200 ↦ 40) ; grille 100 D × 20 ouvriers comme l'officiel ; arabe seulement dans `<title>` ; rien hors du
`viewBox`. Réserve : l'axe des abscisses commence à 200 (coin à x = 44) sans signe de coupure ; le « 0 » du coin est celui de
l'axe vertical — sans incidence sur la lecture (300 est gradué). Tableau de Q7 : voir M-5.

Fuites : Q6 et Q8 redonnent 200 (clé de Q1), Q8 redonne (1100 ; 190) (clé de Q5) et (700 ; 120) — toutes en arrière.
L'explication de Q7 cite les centres dont 1000 (clé de Q2, antérieure). Aucune explication ne résout une question suivante ;
aucun ✓ après un distracteur.

Étage : d3 boss **à la limite mais défendable** : Q7 (moyenne pondérée de 5 classes, centres à calculer, effectif total à
recalculer) et Q8 (lecture graphique interpolée) sont de vrais d3 ; après correctifs, la rampe devient 1,1,1,1,2,2,3,3
(quatre d1). Même profil que 07/24 (2018 technique, d3 boss, 2 d1 · 5 d2 · 2 d3). Si l'orchestrateur veut plus de
marge : d2 · practice · 75/15, comme 07/20 (2024 technique) — non exigé.

Programme (cours 07 lu) : enseignés — effectif, effectif cumulé « التكرار المجمّع » (pour des valeurs, l. 56), centre de
classe et moyenne en classes (l. 171-172), mode d'une série de VALEURS (l. 205), médiane par rangs. NON enseignés :
étendue (Q3 : donnée dans l'énoncé ✓), classe modale (Q4 : **non donnée** → M-4), terme « التكرار التراكمي الصاعد » (Q5,
Q8 : à gloser, M-3), lecture graphique de la médiane (Q8 : règle donnée ✓), polygone des effectifs cumulés (Q8 : points
listés dans l'énoncé ✓). Pourcentage : cycle primaire.

Doublons : aucun quasi-doublon. 07/20 (2024 technique) pose les mêmes sous-questions officielles (total, étendue avec règle,
classe modale) sur d'autres données et d'autres options ; 07/24 Q5 (cumul) a d'autres pièges (décalé, décroissant) que le
correctif M-3 évite à dessein de recopier ; 07/24 Q8-Q9 (médiane interpolée) demandent une expression et un calcul au
centième, pas une lecture graphique. Recyclage d'annales, pas un défaut.

### Défauts 07/25

- **[MAJEUR] M-2 — Q8 : la clé est la seule option qui n'est pas un multiple de 100** (500, 600, 700 contre 640) —
  « marqueur de forme ». Correctif : 500 → 560, interpolation menée depuis la borne supérieure (700 − 200 × 50/70 ≈ 557),
  étiquette existante `math.stat.interpolation-mal-posee` (« point de départ, rapport ou largeur de classe ») exacte. Vérifié :
  {600, 560, 700, 640}, écarts ≥ 40 ; au graphique, l'abscisse 560 correspond à 71 ouvriers (faux à la lecture), 640 à 99 ;
  aucune somme/différence ; l'étiquette de 500 disparaît, 600 et 700 gardent `mediane-egale-centre-ou-borne-de-la-classe`.
  Explication mise à jour (texte exact plus bas).
- **[MAJEUR] M-3 — Q5 : 110 et 130 n'exécutent aucune erreur nommée, et 130 est inobtenable** avec les quatre effectifs de
  l'énoncé (l'explication ne dit que 40). Correctif : options {70, 190, 40, 140} — 70 = 30 + 40 (la classe précédente seule),
  140 = 70 + 30 + 40 (première classe oubliée), toutes deux `math.stat.classes-concernees-incompletes` (« toutes les classes
  situées du bon côté du seuil comptent ») ; 40 garde `effectif-cumule-non-cumule`. Vérifié : aucune somme/différence de deux
  options ne vaut 190 ; pas le jeu de pièges de 07/24 Q5 (décalé/décroissant), donc pas de gabarit recopié. Et le terme
  officiel, absent du cours, est glosé par le terme du cours : « التكرار التراكمي الصاعد (التكرار المجمّع) ».
- **[MAJEUR] M-4 — Q4 : « الفئة المنوالية » n'est enseignée par aucun cours** (le cours 07 n'a que le mode d'une série de
  valeurs) et l'énoncé ne la définit pas (07/20 Q3, même sous-question, la définit). Correctif : poser la définition en tête,
  passer Q4 en **d1** (règle donnée puis application directe), et remplacer « يوزّع الجدول التالي » (aucun tableau n'est
  dessiné) par « يتوزّع … كما يلي : ». La définition ne désigne pas la clé (elle vaut pour les quatre options, il reste à
  lire le plus grand effectif) ; `mode-et-valeur-maximale-confondus` sur [1100 ; 1300[ reste exacte.
- **[MAJEUR] M-5 — Q7 : tableau SVG illisible.** Cellules de 62 unités, libellés « [900 ; 1100[ » et « [1100 ; 1300[ »
  plus larges (mesurés 80 à 91 unités en DejaVu Sans, `getBBox`) : ils débordent sur la cellule voisine et se chevauchent au
  rendu Chromium. Correctif : tableau vertical (une ligne par classe, classe à droite, effectif à gauche), `viewBox`
  240 × 170, police 13-14 — rendu vérifié net à 340 px ; l'énoncé dit l'ordre des colonnes. Texte et SVG exacts plus bas.
  (Une version horizontale à cellules de 88 tient mais s'affiche en ≈ 8 px sur téléphone : écartée.)
- **[MINEUR] m-3 — Q3 en d2** : la règle est donnée, il reste 1300 − 300 ; la même sous-question est d1 en 07/20 Q2.
  Correctif : `difficulty: 1` (rampe 1,1,1,1,2,2,3,3 avec M-4, non décroissante).
- **[MINEUR] m-4 — Q6 : « بين 300 و500 … بين 700 و900 … أعلى من 900 »** ne dit pas à quelle classe appartient 700 pile,
  or le distracteur 75 % (`classe-commencant-au-seuil-comptee`) repose sur « [700 ; 900[ commence à 700 » ; « أعلى من 900 »
  exclut aussi 900, qui est dans [900 ; 1100[. Correctif : énoncé en classes (texte exact plus bas). Et 40 % (= 80/200, la part
  des non-aidés) prend l'étiquette existante `math.alg.reponse-a-l-autre-inconnue` (« l'autre inconnue »), comme 07/24 Q6
  pour le même piège.

Verdict 07/25 : 8/8 clés justes ; 4 majeurs, 2 mineurs ; à reprendre : Q3, Q4, Q5, Q6, Q7, Q8.

---

## Fichier 12/22 — `22-examen-2022-technique-ex1-qcm-solution-distance-carre-symetrie.json`

En-tête : d2 · practice · 75/15 · displayOrder 22 · rampe 1,2,2,2. Titre « 🏛️ مناظرة 2022 (تقني) · التمرين 1 ⭐⭐: أسئلة
اختيار من متعدّد — حلّ معادلة والبعد بين نقطتين ومربّع عدد وتناظر نقطتين » conforme. Fidélité : équations, A(1 ; −1),
B(−1 ; 3), 6 − 4√2, A(−3 ; 4), B(3 ; 4) exacts ; coordonnées réécrites avec « ; » (bidi-sûr) ; Q1 garde les 3 options
officielles ; Q2 ajoute 2√2, Q3 ajoute une 4ᵉ option (non déclarée, sans incidence), Q4 remplace (OI) par (AB) et ajoute J.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 (d1) | (x + 2)/2 = 1 + x | c | OK · **majeur** | l'explication désigne les options par leur rang (« في الأولى/الثانية/الثالثة ») alors qu'elles sont mélangées (M-6) |
| 2 (d2) | 2√5 | b (2√5) | OK · réserve | 20 `distance-sans-racine` exacte ; 2√2 (3 − (−1) écrit 2) et 2 expliqués ; 20 = (2√5)² est inhérent à l'étiquette et aux options officielles |
| 3 (d2) | (2 − √2)² | c | OK · **majeur** | vote terme à terme : 2 (×2), − (×3), √2 (×4) reconstruit la clé (M-7) |
| 4 (d2) | (OJ) | d | OK · **majeur** | symétrie dans un repère enseignée par aucun cours, règle non donnée (M-8) ; « (AB) » est sans ambiguïté faux |

Fuites : aucune (quatre items indépendants). Pas de figure attendue (QCM de calcul ; Q2/Q4 se résolvent aux coordonnées).

Étage : d2 practice honnête ; Q1 d1 (substitution), Q2-Q4 d2. Q1 à 3 options : celles du sujet, acceptable (une 4ᵉ option
ne s'impose pas ; aucune des trois ne s'écarte à vue).

Programme : équations (ch. 04), radicaux et identités (ch. 02, 03), distance (cours 12, l. 316-337) avant 12 : enseignés.
**Symétrie par rapport à un axe ou à O dans un repère : absente des cours 12, 7ᵉ et 8ᵉ** (le cours 8ᵉ/07 n'a que la
construction de la symétrie centrale ; les missions publiées 12/18 Q2 et 12/21 Q2 donnent la règle dans l'énoncé).

Q4 et la fidélité : le remplacement de (OI) par (AB) et l'ajout de J évitent bien le jeu {(OI), (OJ), I, O} de 20/22 Q3,
mais perdent le piège officiel « l'autre axe ». Défendable ; avec le correctif M-8 (définitions générales), (AB) et J
deviennent de vrais pièges (milieu, médiatrice). L'énoncé « متناظرتان بالنسبة إلى المستقيم (AB) » est sans ambiguïté : A et B
sont sur (AB), chacune est son propre symétrique.

Doublons : Q4 a la même configuration et la même clé que 12/21 Q2 (2002 : M(3/2 ; 2), N(−3/2 ; 2) → (OJ), rappel des règles
en coordonnées) — options et pièges différents, et le correctif M-8 rappelle les définitions (milieu, médiatrice) au lieu des
règles de coordonnées : recyclage d'annales, pas un quasi-doublon. Q1 reprend le cadre « quelle équation vérifie ce
nombre ? » de 12/18 Q3 et 09/17 Q3 (équations différentes) : idem. Q2 ↔ 12/15 Q4 et 12/16 Q2 : autres points, autres options.

### Défauts 12/22

- **[MAJEUR] M-6 — Q1 : rangs d'options dans l'explication.** « في الأولى … في الثانية … في الثالثة » nomme des positions que
  l'élève ne voit pas (options mélangées). Correctif : nommer chaque équation par son écriture (texte exact plus bas ; banc :
  les trois équations à lettres sont isolées et lues dans l'ordre).
- **[MAJEUR] M-7 — Q3 : la clé se reconstruit par vote.** Options (2 + √2)², (3 − √2)², (2 − √2)², (1 − 2√2)² : premier
  terme 2 deux fois, signe − trois fois, √2 partout → (2 − √2)². Correctif : (1 − 2√2)² → **(3 + √2)²** = 11 + 6√2 : plan
  2×2 {2 ; 3} × {+ ; −}, chaque case deux fois, aucun vote ; les quatre options ont la même longueur ; sympy : seule
  (2 − √2)² vaut 6 − 4√2. Explication mise à jour.
- **[MAJEUR] M-8 — Q4 : technique non enseignée et non donnée.** Correctif : rappeler dans l'énoncé les DÉFINITIONS (centre
  = milieu, axe = médiatrice), qui valent pour les quatre options — un rappel des règles en coordonnées n'aurait couvert que
  O et (OJ) (« rappel qui reprend la formule de deux options seulement ») ; il faut alors calculer le milieu (0 ; 4) (ni O ni
  J) et voir que (OJ) passe par lui perpendiculairement à (AB) horizontale : la question reste d2. Explication réécrite sans
  rang d'option (texte exact plus bas ; banc : 0 formule brouillée). `symetrie-regle-confondue` sur O reste exacte.

Verdict 12/22 : 4/4 clés justes ; 3 majeurs ; à reprendre : Q1 (explication), Q3, Q4.

---

## Correctifs exacts (textes de remplacement vérifiés)

Chaque texte ci-dessous a été appliqué à une COPIE des fichiers (bloc-notes de l'audit, rien dans le dépôt), puis :
re-résolu (clé inchangée, chaque distracteur faux et produit par l'erreur nommée) ; contrôlé par script (rampe non
décroissante 1,1,2,2,2,2,2,3,3 / 1,1,1,1,2,2,3,3 / 1,2,2,2 ; clé jamais strictement la plus longue ; aucune option somme ou
différence de deux autres ; aucune valeur répétée ; aucune option égale à la clé d'une autre question) ; étiquettes présentes
dans `content/misconceptions.json` de `origin/main` ET de l'arbre `wt-m22` ; rendu au banc Chromium `dir=rtl` à 360 et 600 px :
aucune formule à lettres brouillée. `<SVG>` = la figure actuelle de la question (18 Q7 : reprendre celle de Q8). Les champs
non cités restent inchangés.

#### 18/42 Q6
prompt :
```text
ABC مثلّث متقايس الضلعين قمّته A، وO منتصف [BC]، والنقطة E من [AB] والنقطة F من [AC] حيث (EF) // (BC)، ونسمّي K نقطة تقاطع (AO) و(EF). الأطوال بالصنتمتر :
AB = 50
AO = 40
AE = 15
ما طول [AK] بالصنتمتر ؟
<SVG>
```

#### 18/42 Q7
prompt :
```text
ABC مثلّث متقايس الضلعين قمّته A، وO منتصف [BC] و(AO) عمودي على (BC)، والنقطة E من [AB] والنقطة F من [AC] حيث (EF) // (BC)، ونسمّي K نقطة تقاطع (AO) و(EF). الأطوال بالصنتمتر :
BC = 60
AO = 40
EF = 18
AK = 12
نحصل على شبه المنحرف EFCB بقصّ المثلّث AEF من المثلّث ABC.
ما مساحة شبه المنحرف EFCB بالصنتمتر المربّع ؟
<SVG>
```
options :
  - `a` « 1200 » · `math.alg.reponse-a-l-autre-inconnue`
  - `b` « 984 » · `math.mes.aire-triangle-sans-moitie`
  - `c` « 1092 » · muette · **clé**
  - `d` « 840 » · muette
explanation :
```text
نحصل على مساحة شبه المنحرف EFCB بطرح مساحة المثلّث AEF من مساحة المثلّث ABC. ارتفاع ABC هو AO لأنّ (AO) عمودي على (BC)، وارتفاع AEF هو AK لأنّ (EF) // (BC) فالمستقيم (AK) عمودي على (EF). مساحة ABC = 60 × 40 ÷ 2 = 1200 ومساحة AEF = 18 × 12 ÷ 2 = 108، إذن مساحة EFCB = 1200 − 108 = 1092 cm² ✓.
الخطأ الشائع: الاكتفاء بمساحة المثلّث ABC أي 1200 دون طرح AEF؛ أو نسيان القسمة على 2 في مساحة AEF فنجد 1200 − 216 = 984؛ أو أخذ AO ارتفاعًا للمثلّث AEF فنجد 1200 − 360 = 840.
```

#### 18/42 Q8
options :
  - `a` « 12 » · `math.alg.reponse-a-l-autre-inconnue`
  - `b` « 15 » · muette
  - `c` « 35 » · muette
  - `d` « 28 » · muette · **clé**
explanation :
```text
المستقيم (AO) عمودي على القاعدتين المتوازيتين، فالمسافة بينهما هي KO. بطاليس: AK/AO = AE/AB = 3/10، إذن KO = AO − AK = 40 × (1 − 3/10) = 40 × 7/10 = 28 cm ✓.
الخطأ الشائع: اعتماد القطعة [AK] وطولها 12، وهي الجزء الأعلى من [AO] لا المسافة بين القاعدتين؛ أو أخذ AE = 15 أو الساق المائلة [EB] = 50 − 15 = 35 ارتفاعًا، والارتفاع عمودي على القاعدتين.
```

#### 07/25 Q3
difficulty : 1

#### 07/25 Q4
prompt :
```text
الفئة المنوالية هي الفئة التي لها أكبر تكرار.
يتوزّع عمّال أحد المصانع حسب مرتّباتهم الشهرية كما يلي :
المرتّب الشهري بالدينار :
[300 ; 500[ ، [500 ; 700[ ، [700 ; 900[ ، [900 ; 1100[ ، [1100 ; 1300[
عدد العمّال :
50 ، 70 ، 30 ، 40 ، 10
ما الفئة المنوالية لهذه السلسلة ؟
```
difficulty : 1

#### 07/25 Q5
prompt :
```text
في سلسلة مرتّبات عمّال مصنع، تكرارات الفئات الأربع الأولى [300 ; 500[ و[500 ; 700[ و[700 ; 900[ و[900 ; 1100[ هي على الترتيب 50 و70 و30 و40.
ما التكرار التراكمي الصاعد (التكرار المجمّع) للفئة [900 ; 1100[ ؟
```
options :
  - `a` « 70 » · `math.stat.classes-concernees-incompletes`
  - `b` « 190 » · muette · **clé**
  - `c` « 40 » · `math.stat.effectif-cumule-non-cumule`
  - `d` « 140 » · `math.stat.classes-concernees-incompletes`
explanation :
```text
التكرار التراكمي الصاعد للفئة [900 ; 1100[ يجمع تكرارها وتكرارات كلّ الفئات التي تسبقها: 50 + 70 + 30 + 40 = 190 ✓.
الخطأ الشائع: الاكتفاء بتكرار الفئة نفسها 40 دون تراكم؛ أو نسيان بعض الفئات السابقة: 30 + 40 = 70 بالفئة السابقة وحدها، أو 70 + 30 + 40 = 140 دون الفئة الأولى.
```

#### 07/25 Q6
prompt :
```text
يعمل في مصنع 200 عامل، وتتوزّع مرتّباتهم الشهرية بالدينار كما يلي : 50 عاملًا في الفئة [300 ; 500[ و70 في [500 ; 700[ و30 في [700 ; 900[ والبقيّة في الفئتين [900 ; 1100[ و[1100 ; 1300[.
قرّرت الإدارة منح مساعدة لكلّ عامل يقلّ مرتّبه الشهري عن 700 دينار.
ما النسبة المئوية للعمّال الذين تشملهم هذه المساعدة ؟
```
options :
  - `a` « 25 % » · `math.stat.classes-concernees-incompletes`
  - `b` « 40 % » · `math.alg.reponse-a-l-autre-inconnue`
  - `c` « 60 % » · muette · **clé**
  - `d` « 75 % » · `math.stat.classe-commencant-au-seuil-comptee`

#### 07/25 Q7
prompt :
```text
يبيّن الجدول توزيع عمّال أحد المصانع حسب مرتّباتهم الشهرية بالدينار : في كلّ سطر الفئة ثمّ عدد عمّالها.
ما معدّل المرتّبات الشهرية لعمّال هذا المصنع بالدينار ؟
<SVG>
```

#### 07/25 Q8
options :
  - `a` « 600 » · `math.stat.mediane-egale-centre-ou-borne-de-la-classe`
  - `b` « 560 » · `math.stat.interpolation-mal-posee`
  - `c` « 700 » · `math.stat.mediane-egale-centre-ou-borne-de-la-classe`
  - `d` « 640 » · muette · **clé**
explanation :
```text
نصف التكرار الكلّي هو 200 ÷ 2 = 100. بين النقطتين (500 ; 50) و(700 ; 120) يرتفع المضلّع بانتظام، والمستوى 100 يقع بعد 50 من أصل 70 على هذه القطعة، أي عند 500 + 200 × 50/70 ≈ 643، فالقيمة التقريبية للموسّط حوالي 640 دينارًا ✓.
الخطأ الشائع: أخذ مركز الفئة التي تضمّ الموسّط (600) أو حدّها الأعلى (700) بدل البحث عن الفاصلة التي يبلغ عندها التكرار التراكمي 100؛ أو حساب الإزاحة انطلاقًا من الحدّ الأعلى 700 − 200 × 50/70 ≈ 557 فنجد حوالي 560.
```

#### 12/22 Q1
explanation :
```text
نعوّض x بالعدد 0 في كلّ معادلة.
في (x − 2)/2 = 1 − x نجد (0 − 2)/2 = −1 بينما 1 − 0 = 1، فالطرفان مختلفان.
في (x + 2)/2 = x − 1 نجد (0 + 2)/2 = 1 بينما 0 − 1 = −1، فالطرفان مختلفان.
في (x + 2)/2 = 1 + x نجد (0 + 2)/2 = 1 و1 + 0 = 1، فالطرفان متساويان ✓.
الخطأ الشائع: مقارنة طرف واحد فقط أو إهمال علامة − عند التعويض.
```

#### 12/22 Q3
options :
  - `a` « (2 + √2)² » · muette
  - `b` « (3 − √2)² » · muette
  - `c` « (2 − √2)² » · muette · **clé**
  - `d` « (3 + √2)² » · muette
explanation :
```text
نطوّر بالمتطابقة (a − b)² = a² − 2ab + b²: (2 − √2)² = 4 − 4√2 + 2 = 6 − 4√2 ✓.
والبقيّة تخالفه: (2 + √2)² = 6 + 4√2 ، (3 − √2)² = 11 − 6√2 ، (3 + √2)² = 11 + 6√2.
```

#### 12/22 Q4
prompt :
```text
(O, I, J) معلم متعامد في المستوي حيث OI = OJ = 1 ، والنقطتان A(−3 ; 4) و B(3 ; 4).
نذكّر أنّ نقطتين تكونان متناظرتين بالنسبة إلى نقطة إذا كانت هذه النقطة منتصف القطعة الواصلة بينهما، وبالنسبة إلى مستقيم إذا كان هذا المستقيم الموسّط العمودي لهذه القطعة.
النقطتان A و B متناظرتان بالنسبة إلى :
```
explanation :
```text
منتصف القطعة [AB] هو (0 ; 4) لأنّ الفاصلتين −3 و3 متقابلتان والترتيبتين متساويتان، فهو ليس O ولا J. والمستقيم (AB) أفقي لأنّ للنقطتين نفس الترتيبة 4، والمستقيم (OJ) هو محور التراتيب : يمرّ من المنتصف (0 ; 4) ويعامد (AB)، فهو الموسّط العمودي للقطعة [AB] ✓.
أمّا المستقيم (AB) فيحمل القطعة نفسها، فنظير كلّ من A وB بالنسبة إليه هو النقطة نفسها لا الأخرى؛ وبالنسبة إلى O يتغيّر الإحداثيّان معًا فنظير A هو (3 ; −4)؛ وبالنسبة إلى J(0 ; 1) نظير A هو (3 ; −2).
```

SVG exact de 07/25 Q7 (remplace l'actuel) :
```text
<svg viewBox="0 0 240 170"><title>جدول توزيع عمّال المصنع حسب فئات المرتّب الشهري</title><rect x="100" y="10" width="130" height="30" fill="#e6f4ef" stroke="#0f172a" stroke-width="1.2"/><rect x="10" y="10" width="90" height="30" fill="none" stroke="#0f172a" stroke-width="1.2"/><rect x="100" y="40" width="130" height="30" fill="#e6f4ef" stroke="#0f172a" stroke-width="1.2"/><rect x="10" y="40" width="90" height="30" fill="none" stroke="#0f172a" stroke-width="1.2"/><rect x="100" y="70" width="130" height="30" fill="#e6f4ef" stroke="#0f172a" stroke-width="1.2"/><rect x="10" y="70" width="90" height="30" fill="none" stroke="#0f172a" stroke-width="1.2"/><rect x="100" y="100" width="130" height="30" fill="#e6f4ef" stroke="#0f172a" stroke-width="1.2"/><rect x="10" y="100" width="90" height="30" fill="none" stroke="#0f172a" stroke-width="1.2"/><rect x="100" y="130" width="130" height="30" fill="#e6f4ef" stroke="#0f172a" stroke-width="1.2"/><rect x="10" y="130" width="90" height="30" fill="none" stroke="#0f172a" stroke-width="1.2"/><g direction="ltr" unicode-bidi="isolate" font-weight="700"><text x="165" y="30" text-anchor="middle" font-size="13" fill="#0f172a">[300 ; 500[</text><text x="55" y="30" text-anchor="middle" font-size="14" fill="#0f172a">50</text><text x="165" y="60" text-anchor="middle" font-size="13" fill="#0f172a">[500 ; 700[</text><text x="55" y="60" text-anchor="middle" font-size="14" fill="#0f172a">70</text><text x="165" y="90" text-anchor="middle" font-size="13" fill="#0f172a">[700 ; 900[</text><text x="55" y="90" text-anchor="middle" font-size="14" fill="#0f172a">30</text><text x="165" y="120" text-anchor="middle" font-size="13" fill="#0f172a">[900 ; 1100[</text><text x="55" y="120" text-anchor="middle" font-size="14" fill="#0f172a">40</text><text x="165" y="150" text-anchor="middle" font-size="13" fill="#0f172a">[1100 ; 1300[</text><text x="55" y="150" text-anchor="middle" font-size="14" fill="#0f172a">10</text></g></svg>
```

---

## Synthèse transversale

### Étiquettes (libellés relus sur `origin/main` 5a762ac2)

Toutes les étiquettes posées sont exactes : `hypotenuse-mal-choisie` (18 Q2 a, Q3 a), `pythagore-sans-carres`,
`pythagore-racine-oubliee`, `thales-sans-verifier-parallelisme` (18 Q4 a), `thales-rapport-inverse` (Q5 200, Q6 400/3),
`thales-longueurs-au-lieu-de-rapports` (Q5 25 = 60 − 35, Q6 5 = 40 − 35), `aire-trapeze-sans-demi-somme` (Q7 1680 « une seule
base », 2184 et Q9 21,84 « la somme entière »), `operation-inverse-appliquee` (07 Q3 1600), `borne-de-classe-au-lieu-du-centre`,
`mode-et-valeur-maximale-confondus`, `effectif-cumule-non-cumule`, `classes-concernees-incompletes`,
`classe-commencant-au-seuil-comptee`, `moyenne-sans-ponderation`, `moyenne-divisee-par-le-nombre-de-valeurs`,
`mediane-egale-centre-ou-borne-de-la-classe`, `distance-sans-racine`, `symetrie-regle-confondue`. Aucune option à deux
erreurs n'est étiquetée (18 Q2 d, Q4 c muettes).

Ajouts proposés (étiquettes EXISTANTES, libellé exact à la lettre) : 18 Q7 1200 et 18 Q8 12 →
`math.alg.reponse-a-l-autre-inconnue` (« un résultat intermédiaire ») ; 18 Q7 984 → `math.mes.aire-triangle-sans-moitie` ;
07 Q5 70 et 140 → `math.stat.classes-concernees-incompletes` ; 07 Q6 40 % → `math.alg.reponse-a-l-autre-inconnue` (précédent
07/24 Q6) ; 07 Q8 560 → `math.stat.interpolation-mal-posee`.
Famille neuve « hauteur partielle (AK) prise pour la hauteur du trapèze » : 18 Q8 [12] et 18 Q9 [4,68], rien au publié →
2 questions < 3, **non créée** ; avec le correctif 18 Q8 [12] prend l'étiquette existante, 4,68 reste muette. Conversions
m²/cm² de 18 Q9 (109,2) : muette (le libellé `conversion-aire-facteur-errone` ne dit pas ÷ 1000).

### Doublons

(a) Publié : aucun quasi-doublon (scan des 21 questions contre tout le publié de maths, quiz compris). Gabarit relevé :
18 Q7 actuelle ≈ 18/26 Q5 (aire d'un trapèze, bases et hauteur données) → levé par M-1. Recyclages d'annales admis (autres
données, autres options) : 07 Q1/Q3/Q4 ↔ 07/20 Q1-Q3 ; 12 Q4 ↔ 12/21 Q2 ; 12 Q1 ↔ 12/18 Q3, 09/17 Q3 ; 18 Q2/Q4 ↔ 18/25-28
« ما التبرير ». L'auteur évite bien 20/22 Q3 (12 Q4) ; 09/17 Q3 est un autre cadre d'équation (−2, premier degré simple).
(b) Entre les trois missions : aucun (thèmes disjoints ; aucune paire d'énoncés à Jaccard ≥ 0,4, aucune paire d'options
partagées).

### Rendu arabe

Banc Chromium sur les 21 questions (énoncés, options, explications) : aucune formule à lettres brouillée ; aucun chiffre
arabe-indien, LaTeX, virgule arabe dans un groupe de notation, espace entre groupes de chiffres ; aucune occurrence de
« على الشكل التالي » ; les renvois « الرسم » (07 Q8) ont leur SVG ; « المقابل » (18 Q2) et « المجاورة » (07 Q2) sont de la
prose. Observation moteur (pas un défaut de contenu, déjà classée en L13 m-16) : une formule de chiffres seuls dans une phrase
arabe (« 1 − 0 = 1 », « 1200 − 216 = 984 ») et « 468 cm² » s'affichent dans l'ordre droite-gauche ; l'ordre de LECTURE reste
exact.

### Rapport « fuites »

Une seule fuite en avant : 18 Q7 → Q8 (M-1). Toutes les autres reprises sont en arrière (ordre d'émission = ordre du fichier
dans les trois missions, avant et après correctifs).

---

## Chiffre final

| Fichier | questions | clés fausses | critiques | majeurs | mineurs | à reprendre |
| --- | --- | --- | --- | --- | --- | --- |
| 18/42 | 9 | 0 | 0 | 1 (M-1) | 2 (m-1, m-2) | Q6, Q7, Q8 |
| 07/25 | 8 | 0 | 0 | 4 (M-2 à M-5) | 2 (m-3, m-4) | Q3, Q4, Q5, Q6, Q7, Q8 |
| 12/22 | 4 | 0 | 0 | 3 (M-6 à M-8) | 0 | Q1, Q3, Q4 |
| **Total** | **21** | **0** | **0** | **8** | **4** | **12 questions** |

Verdict : **corriger d'abord** (aucune clé fausse, mais huit majeurs) ; les textes de remplacement ci-dessus sont prêts et
vérifiés. Étages : 18/42 d3 honnête ; 07/25 d3 à la limite mais défendable ; 12/22 d2 honnête.
