# Audit L10 — gisement maths 9ᵉ · chapitre `08-thales` · missions d'examen 13 à 20

> Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md` + skill
> `content-audit`). Rapport écrit au fil de l'eau — **état : TERMINÉ** (chiffre final en fin de document).
>
> - Contenu audité : arbre de travail de `/home/user/yahia-quest-content` (fichiers 13 à 20 de
>   `content/math/08-thales/exercices/` + ligne `sources[]` du `chapter.json`).
> - Références : `origin/main` du dépôt de contenu à `fa035eef` (registre des étiquettes, compétences,
>   cours, missions publiées) ; moteur `origin/main` à `aaec43f` (arena#1139) pour `bidi.ts`.
> - Méthode : chaque question re-résolue **à l'aveugle** (script qui n'affiche que l'énoncé et les
>   options, sans `correctOption`, sans explication, sans étiquette), calculs refaits en `Fraction` /
>   sympy, **clé lue seulement après**. Figures rendues en Chromium (Playwright) et coordonnées
>   recalculées. Rendu arabe simulé avec `splitMathRuns` / `isDisplayEquation` du moteur, en
>   Chromium `dir=rtl`, position de chaque caractère mesurée.
> - **Légende des fuites** (énoncé qui redonne la clé d'une autre question de la mission — le donjon les
>   tire au hasard) : **É** = évitable, le résultat redonné n'est pas énoncé par le sujet officiel (étape
>   de l'auteur, ou résultat que le sujet fait TROUVER), ou il est inutile à la question → **majeur** ;
>   **S** = structurelle, le sujet l'énonce lui-même (« بيّن أنّ … », « استنتج أنّ … ») et l'étape suivante
>   en a besoin → tolérée par « le minimum de la situation », **mineure** ; elle ne disparaît que si la
>   question amont passe de « quelle valeur » à « quelle étape / quelle justification ».

---

## Fichier 13 — `13-examen-2010-technique-ex1-qcm-puissance-racines-remise-milieux.json`

Transcription : `2010-technique.md`, exercice 1 (QCM officiel à trois choix). En-tête : d2 · practice
· 75/15 · `displayOrder` 13 ✓. Titre « 🏛️ مناظرة 2010 (تقني) · التمرين 1 ⭐⭐: اختيار من متعدّد — قوّة كسر وجمع
جذرين وتخفيض بنسبة مائوية ومنتصفا ضلعين » ✓ (nomme des notions, aucun résultat).

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 1/343 | a (1/343) | OK | 3/21 = 1/7 ; (1/7)³ = 1/343 |
| 2 | 7 | c (7) | OK · réserve étiquettes | √16 + √9 = 4 + 3 = 7 |
| 3 | 40 | b (40) | OK · réserve fidélité | 50 × 0,8 = 40 |
| 4 | IJ = AC/2 | d | OK | droite des milieux : (IJ) ∥ (AC) et IJ = AC/2 |

Contrôles :
- **Fidélité** : énoncés et valeurs identiques à la transcription (Q1 `(3/21)³`, Q2 `√16 + √9`,
  Q3 50 dinars / 20 %, Q4 triangle « غير متقايس الضلعين », I milieu de [AB], J milieu de [BC]).
  Les options officielles sont toutes gardées en Q1, Q2, Q4 (plus une quatrième) ; **en Q3, le
  distracteur officiel 47,5 a disparu** (remplacé par 60 et 62,5) — voir défaut 13-c.
- **Figure Q4** (seule figure) : A(70;50), B(40;205), C(285;185) ; I = (55;127,5) et J = (162,5;195)
  sont bien les milieux ; codage simple sur [AB], double sur [BC] ; IJ = ½ AC vectoriellement
  (107,5;67,5) = ½ (215;135) ✓. Ne donne pas la clé. `<title>` seul en arabe, rien hors `viewBox`.
  Remarque sans gravité : CA ≈ 254 et CB ≈ 246 unités (triangle presque isocèle en C, écart 3 %),
  alors que l'item repose sur « غير متقايس الضلعين ».
- **Programme** : puissance d'un quotient (16), racines (01/02), remise en % (acquis antérieurs,
  primaire/7ᵉ), droite des milieux (cours 08, section centre de gravité, étape 1 de l'exemple, nommée
  « المستقيم الرابط بين منتصفي ضلعي مثلث » ; manuel ch. 10 §I.2) ✓.
- **Indices de forme** : clé jamais strictement la plus longue (Q1 à égalité avec 27/21) ; en Q4 le
  vote par composante (facteur « /2 » majoritaire, côté « BC » majoritaire) reconstruit BC/2, un
  distracteur, pas la clé ✓. Aucune option somme/différence de deux autres.
- **Explications** : toutes les égalités recalculées justes (27/9261 = 1/343 ; 9/63 = 1/7 ;
  21/3 = 7 ; 50 × 20/100 = 10 ; 50/0,8 = 62,5). La « seconde méthode » de Q3 (80 %) ne livre aucune
  autre clé.
- **Rendu arabe** : aucun défaut (les seuls écarts mesurés sont l'arithmétique chiffres-seuls,
  lue de droite à gauche par conception, et la parenthèse de « (تقني) », traitée par arena#1138).
- **Doublons** : aucun (le quiz de `02` cite √9 + √16 = 7 comme contre-exemple d'une propriété,
  pas comme calcul demandé).

Défauts de 13 :
- **13-a [mineur · étiquette manquante]** Q2 option `b` « 5 » (√16 + √9 → √25) est muette ; le
  libellé élargi sur `origin/main` de `math.num.racine-distribuee-sur-somme` (« … (ou tu fusionnes
  deux racines ainsi) ») nomme exactement cette erreur → poser `"misconceptionTag":
  "math.num.racine-distribuee-sur-somme"` sur `b`.
- **13-b [mineur · étiquette inexacte + distracteur faible]** Q2 option `a` « 1 » (4 − 3) porte
  `math.num.operation-inverse-appliquee`, dont le libellé donne l'erreur dans l'autre sens (« جمعًا
  بدل الطرح » : additionner au lieu de soustraire) ; et soustraire devant un « + » écrit est peu
  plausible. Correctif : remplacer l'option `a` par `"12,5"` avec
  `"misconceptionTag": "math.num.racine-confondue-avec-moitie"` (√16 pris pour 8, √9 pour 4,5), et
  dans l'explication remplacer « أو طرح الجذرين بدل جمعهما فنجد 4 − 3 = 1. » par « أو أخذ نصف كلّ عدد
  بدل جذره التربيعي فنجد 8 + 4,5 = 12,5. ». Vérifié : options 5 / 7 / 12,5 / 25, clé non la plus
  longue, aucune option somme ou différence de deux autres (5 + 7 = 12), pas de paire proche créée.
- **13-c [mineur · fidélité + étiquette]** Q3 : le distracteur officiel **47,5** (20 % calculé comme
  50 ÷ 20 = 2,5) est retiré ; l'option `d` « 62,5 » (50 ÷ 0,8) porte `operation-inverse-appliquee`
  alors que son erreur est de prendre 50 pour le prix APRÈS remise (base du pourcentage confondue),
  ce que le libellé ne dit pas. Correctif : option `d` → `"47,5"`, **muette** ; dans l'explication
  remplacer « أو قسمة 50 على 0,8 بدل ضربه في 0,8 ، أي إجراء العمليّة المعاكسة ، فنجد 62,5. » par « أو حساب
  20 % من 50 بقسمة 50 على 20 فنجد 2,5 ثمّ 50 − 2,5 = 47,5. ». Vérifié : options 30 / 40 / 47,5 / 60,
  clé non la plus longue, 60 − 30 = 30 n'est pas une autre option, aucune fuite.
- Étiquettes vérifiées exactes : Q1 `b` (a³ → a × 3 sur chaque terme : 3 × 3 = 9, 21 × 3 = 63),
  Q1 `c` (numérateur seul), Q1 `d` `numerateur-denominateur-inverses` (21/3 = 7 puis 7³ = 343 :
  c'est bien l'échange des deux termes — étiquette **acceptée**), Q3 `a` (le « 20 » recopié comme
  montant), Q3 `c` (addition au lieu de soustraction : exact).

Étage : d2 practice juste (quatre items à une étape, rampe plate d2 non décroissante) ✓.

---

## Fichier 14 — `14-examen-2011-technique-ex3-thales-plan-de-quartier-echelle.json`

Transcription : `2011-technique.md`, exercice 3 (plan au 1/1000, (DE) ∥ (AC), BC = 6 cm, DE = 2 cm,
BE = 1,5 cm ; 1) expliquer BE/BC = DE/AC ; 2a) montrer AC = 8 cm ; 2b) distance réelle en mètres).
En-tête d2 · practice · 75/15 · `displayOrder` 14 ✓. Titre conforme, sans résultat ✓.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | c (points sur les côtés + parallèle ⇒ Thalès direct dans BAC) | c | OK · réserve forme | seule option qui cite les deux hypothèses (défaut 14-b) |
| 2 | 1,5/6 = 2/AC | d | OK | substitution directe |
| 3 | 8 | a | OK | 1,5 × AC = 12 ⇒ AC = 8 |
| 4 | 8000 | d | OK · réserve fuite | 8 × 1000 = 8000 cm |
| 5 | 80 | b | OK · réserve fuite | 8000 ÷ 100 = 80 m |

Contrôles :
- **Fidélité** : données identiques (1/1000, BC = 6, DE = 2, BE = 1,5, alignements, parallèle) ; la
  sous-question 2b (« بالمتر ») est scindée en « en cm » (Q4) puis « en m » (Q5).
- **Figure** (même SVG en Q1–Q3) : A(182;38), B(50;214), C(182;214), D(83;170) à t = 0,25 de [BA],
  E(83;214) ; (DE) et (AC) verticales ⇒ parallèles ✓ ; BE/BC = 33/132 = 0,25 = 1,5/6 et
  DE/AC = 44/176 = 0,25 = 2/8 : figure **à l'échelle des données** ✓ ; bande « نهر » entre D et A comme
  dans le sujet ; aucune longueur portée, aucune clé ✓.
- **Glose de l'échelle** (Q4) : « السلّم 1/1000 يعني أنّ كلّ 1 cm في التصميم يمثّل 1000 cm في الواقع » —
  **juste et suffisante**, ne donne pas la valeur (il reste 8 × 1000) ; elle réduit l'item à une
  multiplication (niveau réel d1).
- **Étiquettes** : Q1 `a` `thales-sans-verifier-parallelisme` exact ; Q1 `b` `thales-reciproque-role`
  exact (réciproque employée pour tirer les rapports du parallélisme) ; Q2 `a` `thales-rapport-inverse`
  exact, `b` `thales-formes-melangees` exact (BE/EC = DE/AC), `c` muette (double erreur, plan 2×2 réel) ;
  Q3 `b` 6,5 `thales-longueurs-au-lieu-de-rapports` exact (6 − 1,5 = AC − 2), `c` 6 `formes-melangees`
  exact (2 × 4,5 ÷ 1,5), `d` 4,5 `rapport-inverse` exact (6 × 1,5 ÷ 2) ; Q4 `b` 8
  `reponse-a-l-autre-inconnue` acceptable, `c` 800 `puissance-de-dix-rangs-mal-comptes` exact ; Q5 `a`
  8 et `c` 800 `puissance-de-dix-rangs-mal-comptes` exacts ; Q5 `d` 8000 muette (acceptable).
- **Explications** : toutes les égalités justes (1,5 × AC = 12 ; 12 ÷ 1,5 = 8 ; 0,25 = 0,25 ;
  8 × 1000 = 8000 ; 8000 ÷ 100 = 80).
- **Rendu arabe** : aucun défaut. La ligne de données « BC = 6 ، DE = 2 ، BE = 1,5 » (virgule arabe =
  classe CS, pas de lettre arabe) s'affiche d'un seul tenant de gauche à droite, chaque égalité
  intacte ; « 1 cm », « 8000 cm » : nombre + unité, rendu habituel du corpus.
- **Doublons** : aucune mission publiée ne traite l'échelle ; aucune paire proche avec 01–12.

Défauts de 14 :
- **14-a [majeur · fuite (donjon) + paire proche + étage de complaisance]** L'énoncé de **Q5** donne
  « 8000 cm », **clé de Q4** (fuite **É** : résultat que le sujet ne donne pas, né du découpage de 2b) ;
  l'énoncé de **Q4** donne « AC = 8 cm », **clé de Q3** (fuite **S** : le sujet l'énonce, « بيّن أنّ AC = 8 cm »).
  Tirées au hasard dans le donjon, Q4 avant Q3 ou Q5 avant Q4 livrent la réponse. De plus Q4 et Q5 partagent trois
  options sur quatre (8, 800, 8000) et sont chacune une opération unique (d1 réel) étiquetée d2 pour
  garder l'ordre — ce que `quality-bar.md` interdit. Correctif : **fusionner Q4 et Q5** en une seule
  question, la 2b officielle (en mètres), posée depuis les données brutes, d3 :
  - énoncé : « على تصميم الحيّ السكني ، (DE) ∥ (AC) و D من [BA] و E من [BC] ، والأطوال بالصنتمتر هي :\nBC = 6 ، DE = 2 ، BE = 1,5\nوالسلّم 1/1000 يعني أنّ كلّ 1 cm في التصميم يمثّل 1000 cm في الواقع. ما البعد الحقيقي بين المنزلين A و C بالمتر ؟ » + la figure ;
  - options : `a` « 45 » (`math.geo.thales-rapport-inverse`), `b` « 80 » (clé), `c` « 450 » (muette,
    deux erreurs), `d` « 800 » (`math.num.puissance-de-dix-rangs-mal-comptes`) ;
  - explication : « من BE/BC = DE/AC نجد 1,5/6 = 2/AC ، ومنه AC = 2 × 6 ÷ 1,5 = 8 cm على التصميم. وبالسلّم يمثّل كلّ 1 cm في التصميم 1000 cm في الواقع : 8 × 1000 = 8000 cm ، أي 8000 ÷ 100 = 80 m ✓. الخطأ الشائع: قلب إحدى النسبتين (AC/BC = BE/DE) فنجد AC = 4,5 cm أي 45 m ؛ أو القسمة على 10 بدل 100 عند التحويل إلى المتر فنجد 800 m ؛ أو الخطأين معًا فنجد 450 m. »
  Vérifié : 4,5 cm → 45 m ; 8000 ÷ 10 = 800 ; plan 2×2 (vote « 45/8 » et « ×10 » à égalité), clé non
  la plus longue, aucune option somme/différence de deux autres, aucun énoncé ne donne plus la clé
  d'une autre question (l'explication rappelle AC = 8 cm, clé d'une question PRÉCÉDENTE dans l'ordre
  d'émission : pas de fuite en avant). Mission : 4 questions d1 · d2 · d2 · d3.
- **14-b [majeur · indice de forme, question d'argumentation]** Q1 : la clé `c` est la **seule** à
  réunir les deux hypothèses (« D من [BA] و E من [BC] » que portent `a` et `d`, « (DE) ∥ (AC) » que porte
  `b`) : l'élève qui choisit « l'option la plus complète » la trouve sans la notion. Le plan 2×2
  annoncé est incomplet (`b` perd les points). Correctif : `b` → « D من [BA] و E من [BC] و (DE) ∥ (AC) ،
  فنطبّق النظرية العكسية لطاليس في المثلّث BAC » (étiquette `math.geo.thales-reciproque-role` gardée).
  Longueurs : a 78 · b 82 · c 71 · d 68 → la clé n'est pas la plus longue ; `b` ne nie aucune
  prémisse ; `d` (sans parallèle + réciproque) reste la double erreur muette.
- **14-c [mineur · étiquette inexacte]** Q4 `a` « 0,008 » (8 ÷ 1000 au lieu de × 1000) porte
  `math.num.operation-inverse-appliquee` (libellé : addition/soustraction, somme/produit) ; l'étiquette
  EXISTANTE exacte est `math.num.puissance-de-dix-sens-inverse`. (Sans objet si 14-a est appliqué.)
- **14-d [mineur · figure]** le mot arabe « نهر » est un `<text>` DANS le dessin (la consigne veut l'arabe
  seulement dans `<title>`). Correctif : supprimer `<text x="252" y="114" … direction="rtl">نهر</text>`
  des trois copies de la figure ; l'énoncé dit déjà « يقطعه نهر » et le `<title>` nomme le fleuve.

Étage : d2 practice juste (Thalès en une étape + échelle). Rampe d1 · d2 · d2 · d2 · d2 non
décroissante, mais Q4 et Q5 sont des d1 relevés (14-a).

---

## Fichier 15 — `15-examen-2017-technique-ex1-qcm-radicaux-milieu-segment-hausse.json`

Transcription : `2017-technique.md`, exercice 1 (QCM officiel à trois choix). En-tête d2 · practice ·
75/15 · `displayOrder` 15 ✓. Titre conforme ✓.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | √3 | d | OK · réserve étiquette | √12 = 2√3 ; 2√3 − √3 = √3 |
| 2 | C milieu de [AB] | c | OK | ((2 − 4)/2 ; (−3 + 5)/2) = (−1 ; 1) = C |
| 3 | 3 | a | OK | IJ = BC/2 = 3 cm |
| 4 | 200 | b | OK | 216 ÷ 1,08 = 200 ; contrôle 200 + 16 = 216 |

Contrôles :
- **Fidélité** : toutes les données et **toutes les options officielles** sont gardées (Q1 3 / √3 / −√3,
  Q2 A, B, C milieux, Q3 3,5 / 2,5 / 3, Q4 208 / 200 / 233,28), chacune complétée d'une quatrième ✓.
- **Figure Q3** : A(78;28,84), B(40;215), C(268;215) ; AB : AC : BC = 190 : 266 : 228 = 5 : 7 : 6
  (38 unités/cm) — **à l'échelle** ; I, J milieux exacts, [IJ] horizontal ∥ [BC], IJ = 114 = BC/2 ;
  codage simple sur [AB], double sur [AC] ✓. Aucune clé marquée ; rien hors `viewBox`.
- **Programme** : radicaux (02), milieu par coordonnées (12, sans vecteur), droite des milieux
  (cours 08 + manuel ch. 10 §I.2), hausse en % : acquis du primaire (6ᵉ, « الزيادة والتخفيض ») ; le
  retour au prix initial se fait par mise en équation (04 : « ترجمة المسائل إلى معادلات »), et le
  manuel lui-même pose ce problème inverse en rappel du ch. 7 (« باع تاجر بضاعة بربح يقدر بـ 15 % …
  أوجد ثمن شرائها ») : **pas de technique hors programme**.
- **Indices de forme** : clé jamais la plus longue (Q2 : l'option longue est le distracteur `d`,
  réelle, non méta) ; aucune option somme/différence de deux autres ; Q1 : « √3 » dans trois options
  sur quatre, mais le signe et le coefficient ne se votent pas (clé non reconstructible).
- **Explications** : toutes recalculées justes (milieux (−2,5 ; 3) et (0,5 ; −1) ; sommes (−2 ; 2),
  (−5 ; 6), (1 ; −2) ; 216 × 1,08 = 233,28 ; 216 × 0,92 = 198,72).
- **Étiquettes** : Q1 `b` 3√3 `facteur-racine-sans-carre` exact (√12 = 4√3 : c'est l'exemple même du
  libellé, √8 = 4√2) ; Q2 `d` `vec.milieu-sans-moitie` exact (sans la moitié, aucune somme ne tombe
  sur un point, d'où « aucun milieu ») ; Q3 `c` 12 `droite-des-milieux-facteur-deux` exact ; Q4 `c` 208
  `pourcentage-recopie-comme-resultat` exact (le « 8 » recopié comme 8 dinars).
- **Rendu arabe** : aucun défaut (ligne de données « AB = 5 ، AC = 7 ، BC = 6 » d'un seul tenant ;
  points A(2 ; −3)… isolés par leurs parenthèses).
- **Doublons** : le gabarit de Q2 (« A/B/C milieu de … » + une quatrième) existe en `12/04-defi` Q3,
  mais données, clé et quatrième option diffèrent : pas de doublon. Q3 et **13 Q4** portent la même
  propriété avec les mêmes pièges, mais sous deux angles distincts (relation symbolique en 13, valeur
  en 15) et les deux items sont officiels : acceptable.

Défauts de 15 :
- **15-a [mineur · étiquette manquante]** Q1 `a` « 3 » (√12 − √3 → √(12 − 3) = √9) est muette ; le
  libellé élargi de `math.num.racine-distribuee-sur-somme` (« … une somme ou une différence (ou tu
  fusionnes deux racines ainsi) ») la nomme exactement → poser ce tag sur `a`.
- Options muettes Q3 `b`/`d` et Q4 `a`/`d` : voir le bilan des étiquettes proposées (§ Étiquettes).

Étage : d2 practice juste ; rampe plate d2 ✓.

---

## Fichier 16 — `16-examen-2003-ex3-repere-milieu-thales-coordonnees.json`

Transcription : `2003.md`, exercice 3 (repère orthonormé ; A(3,0), B(−2,3), C(2,−3) ; 1a placer, 1b O milieu
de [BC] ; 2) parallèle à (OI) par B, coupe (OJ) en K et (CA) en M : 2a K, 2b BM = 6, 2c M). En-tête d3 ·
boss · 120/30 · `displayOrder` 16 ✓. Titre « 🏛️ مناظرة 2003 · التمرين 3 ⭐⭐⭐: … » (session unique, sans
filière) ✓.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | B seule (dessinée en (3 ; −2)) | b | OK · réserve énoncé | A(3;0) et C(2;−3) justes sur la figure |
| 2 | (0 ; 0) | c | OK · réserve distracteur | ((−2 + 2)/2 ; (3 − 3)/2) |
| 3 | (0 ; 3) | d | OK | y = 3 coupe x = 0 |
| 4 | CO/CB | a | OK · réserve fuite | Thalès dans CBM, (OA) ∥ (BM) |
| 5 | 6 | b | OK · réserve fuite + explication | OA/BM = 1/2, OA = 3 |
| 6 | (4 ; 3) | c | OK · réserve fuite | y = 3 sur (CA) : y = 3x − 9 ⇒ x = 4 ; A milieu de [CM] ✓ |

Contrôles :
- **Figure Q1** (volontairement fausse) : unité 30 px, origine (112;138) ; A dessinée en (3;0) ✓,
  C en (2;−3) ✓, **B en (3;−2)** (au lieu de (−2;3)) ✓ comme annoncé ; axes gradués de −3 à 4 et de
  −4 à 4, I et J aux unités ; `<title>` neutre (« كما رسمها التلميذ »). « فحصل على الشكل التالي » renvoie
  bien à la figure présente (pas un faux renvoi).
- **Figure Q4** : unité 28 px ; B(62;58), C(174;226), A(202;142), M(230;58) = exactement (−2;3),
  (2;−3), (3;0), (4;3) ✓ ; (BM) horizontale ∥ (OI) ✓ ; O sur [BC] ✓ ; A milieu de [CM] ✓. Figure à
  l'échelle (BM = 6 × OI) : vraie, n'affiche aucune valeur ; mais son `<title>` dit « O منتصف [CB] »
  (voir 16-b).
- **Fidélité / adaptations** : « أُرسم النقاط » → « quel point est mal placé » garde la compétence
  (situer un couple) ; « أثبت أنّ O منتصف [BC] » → calcul du milieu : la preuve est ce calcul, rien
  n'est perdu ; 2b est scindée en rapport (Q4) puis valeur (Q5) ✓. Données identiques.
- **Étiquettes** : Q1 `d` `vec.coordonnees-point-inversees` exact (lire (y ; x) rend B « juste » et A,
  C « fausses ») ; Q2 `d` `int.signe-ignore-dans-somme` exact ((2 + 2)/2 ; (3 + 3)/2) ; Q3 `a`
  `perpendiculaire-et-parallele-confondus` exact, `b`/`c` `coordonnees-point-inversees` acceptables ;
  Q4 `b` `formes-melangees`, `c` `rapport-inverse` exacts, `d` double erreur muette (plan 2×2 réel) ;
  Q5 `c` 3 `longueurs-au-lieu-de-rapports` exact (BM = OA « parce que parallèles »), `d` 1,5
  `rapport-inverse` exact ; Q6 `b` exact.
- **Explications** : toutes les égalités recalculées justes (milieux, (−4 ; 6), (2 ; 3), 3/BM = 1/2,
  milieu de [CM] = (3 ; 0) = A).
- **Rendu arabe** : aucun défaut. **Doublons** : `09/19-examen-2011-generale-ex4` (publié) partage le
  genre « repère + Thalès + coordonnées » mais ni les données, ni la configuration, ni les options :
  pas de doublon ; rien de proche dans `12`.

Défauts de 16 :
- **16-a [majeur · énoncé au pluriel qui annonce un nombre]** Q1 : « فأيّ الإجابات تحدّد النقاط التي وُضعت
  في غير موضعها ؟ » annonce PLUSIEURS points mal placés alors qu'un seul l'est ; le pluriel pousse vers
  `d` (la seule option à deux points). Correctif : « … فأيّ الإجابات تحدّد النقطة أو النقاط التي وُضعت في
  غير موضعها ؟ ».
- **16-b [majeur · fuites (donjon)]** Les énoncés redonnent des clés d'autres questions : Q4 pose
  « والنقطة O منتصف [BC] » (= clé de Q2, O étant (0 ; 0) ; **É**, inutile à Q4), le `<title>` de la figure Q4
  aussi ; Q5 pose « CO/CB = OA/BM » (= **clé de Q4**, **É** : étape de l'auteur) et « O منتصف [CB] » (**S**) ;
  Q6 pose « BM = 6 » (= **clé de Q5**, **S** : « بيّن أنّ BM = 6 »). Q5 devient en outre un calcul à une étape
  (3/BM = 1/2), d1–d2 réel sous une étiquette d2 dans un boss. Les correctifs suppriment aussi les fuites S.
  Correctifs :
  - Q4 : « والنقطة O منتصف [BC] ، » → « والنقطة O من [BC] ، » ; `<title>` de la figure : « و O منتصف
    [CB] » → « و O من [CB] ». (Thalès n'a besoin que de O ∈ [CB].)
  - Q5 (d3) : énoncé « (O, I, J) معيّن متعامد ومتجانس ووحدة الطول OI ، والنقاط A(3 ; 0) و B(−2 ; 3) و C(2 ; −3) ، والمستقيم المارّ من B والموازي لـ (OI) يقطع (CA) في النقطة M. ما طول BM بوحدة الطول ؟ » ;
    options `a` « 5 » (muette), `b` « 6 » (clé), `c` « 3 » (tag inchangé), `d` « 1,5 » (tag inchangé) ;
    explication « منتصف [BC] هو ((−2 + 2)/2 ; (3 + (−3))/2) = (0 ; 0) ، أي O ، فـ CO/CB = 1/2. و A على (OI) و (BM) ∥ (OI) ، فـ (OA) ∥ (BM) ، وبنظرية طاليس في المثلّث CBM : OA/BM = CO/CB = 1/2. و OA = 3 ، فـ 3/BM = 1/2 ، ومنه BM = 6 وحدات ✓. الخطأ الشائع: قلب النسبة فنكتب BM/OA = 1/2 فنجد BM = 1,5 ؛ أو مساواة الطولين BM = OA لأنّ المستقيمين متوازيان فنجد 3 ؛ أو اعتبار M فوق A مباشرة فنجد BM = 3 − (−2) = 5 ، مع أنّ M على (CA) لا على العمودي المارّ من A. »
    (le 12 disparaît : voir 16-c). Vérifié : 1,5 / 3 / 5 / 6, clé non la plus longue, aucune option
    somme ou différence de deux autres (la suite 1,5 → 3 → 6 → 12, où la clé était un terme, est
    rompue) ; l'explication ne rappelle que des clés de questions ANTÉRIEURES (Q2, Q4, d2).
  - Q6 : supprimer « وBM = 6 وحدات طول ، » de l'énoncé ; explication : remplacer « وبما أنّ BM = 6 » par
    « وبنظرية طاليس في المثلّث CBM : OA/BM = CO/CB = 1/2 مع OA = 3 ، فـ BM = 6 ، إذن ». Les options
    restent (−8 ; 3), (3 ; 4), (4 ; 3), (6 ; 3).
- **16-c [majeur · notion non enseignée dans une explication]** Q5 `a` « 12 » : « تربيع النسبة كما في
  المساحات » invoque la règle k² des aires, **absente du programme de 9ᵉ** (manuel ch. 10, bornes :
  « agrandissement / réduction … totalement absents ») et enseignée seulement dans `13-geometrie-espace`,
  hors manifeste. L'erreur n'est pas plausible pour un élève de 9ᵉ. Correctif : l'option `a` devient
  « 5 » (ci-dessus). (Voir aussi l'étiquette proposée n° 3.)
- **16-d [majeur · distracteur éliminé à vue]** Q2 `b` « (−2 ; 3) » est **l'extrémité B elle-même**,
  donnée dans l'énoncé : le milieu de [BC] ne peut pas être B. Correctif : `b` → « (0,5 ; −0,5) »
  (muette : l'abscisse et l'ordonnée d'un MÊME point additionnées au lieu des deux abscisses :
  ((−2 + 3)/2 ; (2 + (−3))/2)) ;
  dans l'explication remplacer « أخذ نصف الفرق بدل نصف المجموع فنجد ((−2 − 2)/2 ; (3 − (−3))/2) = (−2 ; 3) ، أو
  الفرق كاملًا فنجد (−4 ; 6) » par « أخذ الفرق بدل المجموع فنجد (−2 − 2 ; 3 − (−3)) = (−4 ; 6) ؛ أو جمع
  فاصلة النقطة وترتيبتها بدل جمع فاصلتي النقطتين فنجد ((−2 + 3)/2 ; (2 + (−3))/2) = (0,5 ; −0,5) ». Vérifié :
  la clé « (0 ; 0) » n'est pas la plus longue, aucune option n'est une extrémité ni une somme d'options.

Étage : **d3 boss justifié seulement avec 16-b** (Q5 et Q6 deviennent des chaînes de 3 étapes). En
l'état, Q1 d1 et Q2–Q5 sont des items à une étape (les résultats intermédiaires étant donnés) : la
mission se joue comme un d2. Rampe d1 · d2 · d2 · d2 · d2 · d3 non décroissante ✓ (d1 · d2 · d2 · d2 ·
d3 · d3 après correctif).

---

## Fichier 17 — `17-examen-2010-generale-ex3-factorisation-produit-nul-thales-aire.json`

Transcription : `2010-generale.md`, exercice 3 (A = x² + 2x − 8 ; 1) A pour x = 2 ; 2a montrer
A = (x + 1)² − 9 ; 2b factoriser ; 2c A = 0 ; 3a papillon (BE) ⊥ (BC), (BE) ⊥ (EF), AE = 4, BC = 2, AB = x,
EF = x + 2 : montrer x/4 = 2/(x + 2) et en déduire x² + 2x − 8 = 0 ; 3b aire de AEF). En-tête d3 · boss ·
120/30 · `displayOrder` 17 ✓. Titre conforme (2010 générale, sans marque de filière, comme les missions
publiées) ✓.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 0 | a | OK | 4 + 4 − 8 |
| 2 | (x + 1)² − 9 | d | OK · réserve fuite | se développe en x² + 2x − 8 |
| 3 | (x − 2)(x + 4) | c | OK · réserve fuite | a² − b², a = x + 1, b = 3 |
| 4 | {−4 ; 2} | b | OK · réserve fuite | produit nul |
| 5 | x/4 = 2/(x + 2) | a | OK · réserve fuite | papillon de sommet A : AB/AE = BC/EF |
| 6 | x² + 2x − 8 = 0 | d | OK · réserve fuite | x(x + 2) = 8 |
| 7 | x = 2 | b | OK · réserve fuite + étage | longueur > 0 |
| 8 | 8 | c | OK · réserve fuite + étage | (4 × 4)/2 |

Contrôles :
- **Fidélité / adaptations** : données identiques. « Montrer que A = (x + 1)² − 9 » → « quelle écriture
  est égale à A » (Q2) : l'élève vérifie en développant chaque option, rien n'est perdu ; « montrer
  x/4 = 2/(x + 2) » → « quelle égalité » (Q5) ; « en déduire x² + 2x − 8 = 0 » → « quelle équation après
  produit en croix » (Q6) : fidèles. La 3b est scindée en x (Q7) puis aire (Q8).
- **Figure** (Q5, Q8) : B(170;34), C(226;34), A(170;90), E(170;202), F(58;202) : (BC) et (EF)
  horizontales ⊥ (BE) ✓, angles droits codés en B et E (donnés par l'énoncé, pas à démontrer) ✓, C, A, F
  alignés ✓, longueurs portées sur des segments entiers ✓ ; à 28 px/cm la figure est **à l'échelle de
  x = 2** (AB = BC = 56 px, AE = EF = 112 px) — toute figure cohérente avec les quatre étiquettes l'est
  forcément ; sans conséquence tant que x est donné ou déductible des options ; triangle AEF grisé en Q8
  (désigne l'objet, pas la réponse) ✓. Après 17-a, x n'est plus donné dans la question finale : AB y est
  dessiné égal à BC (étiqueté 2), indice visuel de x = 2 — tolérable (l'aire reste à calculer), ou bien
  ajouter « والرسم غير مرسوم بمقياس الرسم » et redessiner avec AB ≠ BC en gardant C, A, F alignés (p. ex.
  AB = 40 px et EF = 156,8 px, AE et BC inchangés).
- **Programme** : identités et factorisation par a² − b² (03), produit nul et « solutions de l'équation /
  solutions du problème » (04), papillon (08), aire du triangle rectangle (acquis) ✓. L'indice
  (x + 1)² − 9 est officiel et donné : aucune forme canonique à trouver.
- **Étiquettes** : Q1 `c` 16 `int.signe-ignore-dans-somme` exact, `d` 18 `chiffres-juxtaposes-au-lieu-du-produit`
  exact (2x lu 22) ; Q3 `d` `difference-carres-confondue` exact ; Q4 `a` `produit-nul-racine-signe-non-oppose`
  exact, `d` ∅ `produit-nul-et-au-lieu-de-ou` exact ; Q5 `b`/`c` exacts, `d` double muette ; Q6 `a`
  (4 + 2 au lieu de 4 × 2) `operation-inverse-appliquee` exact (« une somme au lieu d'un produit »), `c`
  `transposition-sans-changer-signe` exact, `b` double muette ; Q7 `a` et `d`
  `solution-hors-contrainte-gardee` acceptables ; Q8 `a` `aire-triangle-sans-moitie` exact, `b`/`d`
  `reponse-a-l-autre-inconnue` (aires de BEF et ABC) acceptables.
- **Explications** : toutes les égalités recalculées justes (développements des quatre écritures de Q2,
  (x − 2)(x + 4) = x² + 2x − 8, 4² + 2 × 4 − 8 = 16, aires 16 / 12 / 8 / 2).
- **Rendu arabe** : aucun défaut (lignes de données d'un seul tenant, formules isolées).
- **Doublons** : même **gabarit** que la mission publiée `08/12-devoir-radicaux-trinome-thales` (indice
  canonique → factorisation → produit nul → égalité de Thalès en x → racine positive), avec les mêmes
  familles de pièges ; données, figure et options différentes : pas un doublon au sens de la consigne,
  à signaler au lecteur de la série.

Défauts de 17 :
- **17-a [majeur · fuites en chaîne (donjon)]** six énoncés sur huit redonnent la clé d'une autre
  question : Q3 « A = (x + 1)² − 9 » = clé de Q2 (**S**) ; Q4 « A = (x − 2)(x + 4) » = clé de Q3 (**É** : la
  2b officielle est à TROUVER) ; Q6 « x/4 = 2/(x + 2) » = clé de Q5 (**S**) ; Q7 « x² + 2x − 8 = 0 » = clé de
  Q6 (**S**) **et** « وأنّ حلّي هذه المعادلة هما −4 و 2 » = clé de Q4 (**É**) ; Q8 « x = 2 » = clé de Q7 (**É**).
  (Le motif existe dans des missions publiées, p. ex. `04/18-examen-2002` Q4–Q5, mais la consigne en
  vigueur l'interdit.) Correctif — reprise en 7 questions, aucune clé dans un autre énoncé (les fuites S
  disparaissent aussi) :
  1. **Q2** (clé déplacée vers l'étape de calcul) : énoncé « نضع :\nA = x² + 2x − 8\nولنبيّن أنّ A = (x + 1)² − 9 ننشر العبارة (x + 1)² − 9. ما النشر الصحيح قبل الاختزال ؟ » ; options `a` « x² − 2x + 1 − 9 »
     (`math.alg.carre-somme-signe-double-produit`), `b` « x² + 1 − 9 » (`math.alg.carre-somme-sans-double-produit`),
     `c` « x² + x + 1 − 9 » (`math.alg.double-produit-sans-facteur-2`), `d` « x² + 2x + 1 − 9 » (clé) ;
     explication « بمتطابقة مربّع المجموع (a + b)² = a² + 2ab + b² مع a = x و b = 1 : (x + 1)² = x² + 2x + 1 ، فيكون (x + 1)² − 9 = x² + 2x + 1 − 9 = x² + 2x − 8 = A ✓. الخطأ الشائع: إعطاء الجداء المضاعف الإشارة − فنكتب x² − 2x + 1 − 9 ؛ أو نسيان الجداء المضاعف فنكتب x² + 1 − 9 ؛ أو كتابته دون العامل 2 فنكتب x² + x + 1 − 9. » (d2 ; clé à égalité de longueur avec `a` ; seule `d` vaut A — vérifié.)
  2. **Q3** inchangée.
  3. **Q5** inchangée, **placée avant Q4** (rampe).
  4. **Q4** (d3) : énoncé « نعلم أنّ :\nA = (x + 1)² − 9\nما مجموعة الأعداد الحقيقيّة x التي تحقّق A = 0 ؟ » ;
     options inchangées, `c` {2} reçoit `math.num.racine-carree-negative-oubliee` ((x + 1)² = 9 ⇒ x + 1 = 3
     seulement) ; explication précédée de « نفكّك A كفرق مربّعين (9 = 3²) : A = (x + 1 − 3)(x + 1 + 3) = (x − 2)(x + 4) ، ثمّ » et suivie du contrôle « (2 + 1)² − 9 = 0 و (−4 + 1)² − 9 = 0 ✓ ».
  5. **Q6** (d3) : énoncé « في الشكل التالي المستقيم (BE) عمودي على (BC) وعلى (EF) ، والنقطة A من [BE] ، والنقاط C و A و F على استقامة واحدة ، والأطوال بالصنتمتر :\nAE = 4 ، BC = 2 ، AB = x ، EF = x + 2\nنكتب المساواة التي تعطيها نظرية طاليس ثمّ نجري الضرب التقاطعي وننشر. ما المساواة التي نحصل عليها ؟ » + figure de Q5 ;
     options `a` « x² + 2x = 6 » (`math.num.operation-inverse-appliquee`), `b` « x² + 2 = 8 »
     (`math.alg.distribution-partielle`), `c` « x² + 2 = 6 » (muette, deux erreurs), `d` « x² + 2x = 8 » (clé) ;
     explication « (BC) و (EF) عموديان على (BE) فهما متوازيان ، والوضعية وضعية الفراشة ورأسها A : AB/AE = BC/EF ، أي x/4 = 2/(x + 2). بالضرب التقاطعي : x × (x + 2) = 4 × 2 ، أي x² + 2x = 8 ✓ ، وهي المعادلة x² + 2x − 8 = 0 بعد نقل 8. الخطأ الشائع: جمع 4 و 2 بدل ضربهما فنجد x² + 2x = 6 ؛ أو ضرب x في الحدّ الأوّل من القوس وحده فنجد x² + 2 = 8 ؛ أو جمع الخطأين فنجد x² + 2 = 6. »
     (plan 2×2 ; la clé n'est plus l'écriture de A que montrent Q1 et Q2, ce qui supprime aussi le
     raccourci « l'option qui ressemble à A ».)
  6. **Q7 + Q8 → une seule question** (la 3b officielle, d3) : énoncé « في الشكل التالي المستقيم (BE) عمودي على (BC) وعلى (EF) ، والنقطة A من [BE] ، والنقاط C و A و F على استقامة واحدة ، والأطوال بالصنتمتر :\nAE = 4 ، BC = 2 ، AB = x ، EF = x + 2\nوالطول x يحقّق المعادلة التالية :\n(x + 1)² − 9 = 0\nما مساحة المثلّث AEF بالصنتمتر المربّع ؟ » + figure de Q8 ;
     options 16 / 12 / 8 / 2 inchangées (tags inchangés) ; explication « (x + 1)² − 9 = 0 تُفكَّك إلى (x − 2)(x + 4) = 0 ، فـ x = 2 أو x = −4 ؛ و x طول القطعة [AB] فهو موجب قطعًا ، إذن x = 2 ، ومنه EF = x + 2 = 4. والمثلّث AEF قائم في E ، فمساحته (AE × EF)/2 = (4 × 4)/2 = 8 cm² ✓. الخطأ الشائع: نسيان القسمة على 2 فنجد 16 ؛ أو حساب مساحة مثلّث آخر من الشكل : BEF (BE = 6 و EF = 4) فنجد 12 ، أو ABC (AB = 2 و BC = 2) فنجد 2. »
  Ordre final : Q1 d1 · Q2 d2 · Q3 d2 · Q5 d2 · Q4 d3 · Q6 d3 · Q7/8 d3 (rampe non décroissante, chaque
  explication ne rappelle que des clés de questions émises avant elle). Vérifié par calcul (sympy).
- **17-b [mineur · difficulté de complaisance]** en l'état, Q7 (choisir le positif entre deux solutions
  données) et Q8 (aire avec x donné) sont des items à une étape étiquetés d3 : c'est le correctif 17-a
  qui rend l'étage d3 honnête.
- **17-c [mineur · étiquettes existantes non posées]** Q2 `a` « (x − 1)² − 9 » (double produit affecté du
  mauvais signe) mérite `math.alg.carre-difference-signes` ; Q3 `a` « (x − 8)(x + 10) » (9 pris pour b au
  lieu de 3) mérite `math.alg.difference-carres-second-terme-non-eleve-au-carre` (précédent publié :
  `04/17-examen-2001` Q3, « (x − 4)(x + 4) »). (Sans objet pour Q2 si 17-a est appliqué.)

Étage : d3 boss **justifié après 17-a** (trois questions finales à 2–4 étapes) ; en l'état la mission se
joue en d2 (chaque énoncé fournit le résultat précédent).

---

## Fichier 18 — `18-examen-2016-generale-ex2-thales-parametre-equation-produit.json`

Transcription : `2016-generale.md`, exercice 2 (repère, OI = OJ = 1, A(a, 0), B(0, a), a > 1 ; 1) parallèle
à (BI) par A → E : montrer OA/OI = OE/OB, en déduire OE = a² ; 2) M sur [OJ), EM = 1, M ∉ [OE] : OM ;
3) parallèle à (AM) par J → K : montrer OK = a/(a² + 1) ; 4a) montrer (x − 2)(x − 1/2) = x² − (5/2)x + 1 ;
4b) si OK = 2/5 alors I milieu de [OA]). En-tête d3 · boss · 120/30 · `displayOrder` 18 ✓. Titre ✓.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | OA/OI = OE/OB | a | OK · réserve fuite | Thalès de sommet O, rapports inversés ensemble |
| 2 | a² | c | OK | a/1 = OE/a |
| 3 | a² + 1 | d | OK | M au-delà de E |
| 4 | OK/OA = OJ/OM | a | OK · réserve fuite | (JK) ∥ (AM) |
| 5 | a/(a² + 1) | b | OK · réserve fuite | OK = a × 1/(a² + 1) |
| 6 | x² − (5/2)x + 1 | c | OK | −x/2 − 2x = −5x/2 ; (−2)(−1/2) = 1 |
| 7 | 2a² − 5a + 2 = 0 | d | OK | 5a = 2a² + 2 |
| 8 | {1/2 ; 2} | c | OK · réserve fuite | (a − 2)(a − 1/2) = 0 |
| 9 | a = 2 | b | OK · réserve fuite + étage | a > 1 |
| 10 | I milieu, I ∈ [OA] et OI = OA/2 | a | OK · réserve fuite + étage | a = 2 |

Contrôles :
- **Figures** (Q1, Q3, Q4) : unité 46 px ; A et B à 69 px (a = 1,5), E à 103,5 px (= a² = 2,25), M à
  149,5 px (= a² + 1 = 3,25), K à 21,23 px (= a/(a² + 1) = 0,4615) ; (BI) ∥ (EA) (vecteurs (46;69) et
  (69;103,5)) ✓, (JK) ∥ (AM) (rapport 0,4615 des deux côtés) ✓ ; angle droit en O (repère orthogonal
  donné) ✓ ; flèches de parallélisme sur des parallèles données ✓. Figure tracée pour a = 1,5 : elle ne
  livre ni a = 2 ni aucune clé ✓. Rien hors `viewBox`, arabe seulement dans `<title>`.
- **Fidélité** : données identiques ; toutes les sous-questions sont présentes (1 → Q1–Q2, 2 → Q3,
  3 → Q4–Q5, 4a → Q6, 4b → Q7–Q10).
- **Programme** : Thalès (08), identités et produit nul (03, 04), milieu (12) ✓.
- **Étiquettes** : Q1 `b` `rapport-inverse` et `d` `formes-melangees` exacts, `c` double muette (plan 2×2
  réel, vote à égalité sur chaque rapport) ; Q2 `d` 2a − 1 `longueurs-au-lieu-de-rapports` exact ; Q4 `b`/`c`
  exacts ; Q5 `a` `reponse-a-l-autre-inconnue` (le rapport au lieu de OK) acceptable, `d`
  `rapport-inverse` exact ; Q6 `b` `int.produit-signes-negatifs` exact ; Q7 `a` `transposition-sans-changer-signe`,
  `b` `distribution-partielle` (2(a² + 1) = 2a² + 1) exacts ; Q8 `a` `produit-nul-racine-signe-non-oppose`,
  `d` `produit-nul-et-au-lieu-de-ou` exacts ; Q9 `a`/`c` `solution-hors-contrainte-gardee` exacts ; Q10 `b`
  `geo.condition-suffisante-supposee` (« entre O et A » pris pour une preuve) acceptable, `d`
  `vec.milieu-sans-moitie` exact.
- **Explications** : toutes justes (a² − (2a − 1) = (a − 1)² ; 1/4 − 5/4 + 1 = 0 ; 4 − 5 + 1 = 0 ;
  IA = 2 − 1 = 1).
- **Q10 (argumentation)** : `c` et `d` sont fausses sans ambiguïté (conclusion fausse) ; `b` a une
  conclusion vraie et une raison insuffisante — piège classique, recevable ; la clé n'est pas la plus
  longue (45 contre 62) et ne reprend pas seule les mots de l'énoncé.
- **Rendu arabe** : aucun défaut. **Doublons** : aucun avec les publiées ; même famille de pièges que 17
  (produit en croix + transposition, produit nul, contrainte) mais géométrie, paramètre et conclusion
  différents : pas un doublon de gabarit.

Défauts de 18 (fuites classées : **S** = donnée que le sujet officiel énonce lui-même — « بيّن أنّ … /
استنتج أنّ … » — et dont l'étape suivante a besoin ; **É** = résultat non donné par le sujet ou inutile à
la question, donc évitable) :
- **18-a [majeur · fuites évitables (É)]** Q4 donne « M(0 ; a² + 1) » (clé de Q3), inutile pour choisir
  des rapports ; Q5 donne « OK/OA = OJ/OM » (clé de Q4) et « OM = a² + 1 » (clé de Q3) ; Q8 donne
  « 2a² − 5a + 2 = 0 » (clé de Q7) ; Q9 donne les solutions « 1/2 و 2 » (clé de Q8) et l'équation (clé de
  Q7) ; Q10 donne « a = 2 » (clé de Q9). (Fuites S tolérées par la règle « le minimum de la situation » :
  Q2 ← Q1, Q3 ← Q2, Q7 ← Q5, Q8 ← Q6.) Correctif :
  1. **Q4** : énoncé « (O, I, J) معيّن متعامد حيث OI = OJ = 1 ، والنقطة A(a ; 0) حيث a > 1 ، والنقطة M من نصف المستقيم [OJ) حيث OM > 1 ، والمستقيم المارّ من J والموازي لـ (AM) يقطع (OI) في النقطة K ، فأيّ مساواة بين النسب تعطيها نظرية طاليس ؟ » (options et explication inchangées).
  2. **Q5** (reste d2 : OM se lit, puis un Thalès) : énoncé « (O, I, J) معيّن متعامد حيث OI = OJ = 1 ، والنقطتان A(a ; 0) و E(0 ; a²) حيث a > 1 ، والنقطة M من نصف المستقيم [OJ) حيث EM = 1 و M لا تنتمي إلى القطعة [OE] ، والمستقيم المارّ من J والموازي لـ (AM) يقطع (OI) في النقطة K. ما البعد OK بدلالة a ؟ » + figure de Q4 ; explication « M خارج [OE] ، فـ OM = OE + EM = a² + 1. و (JK) ∥ (AM) مع J من [OM] و K من [OA] ، فبنظرية طاليس OK/OA = OJ/OM ، أي OK/a = 1/(a² + 1) ، ومنه OK = a/(a² + 1) ✓. الخطأ الشائع: الاكتفاء بالنسبة OJ/OM = 1/(a² + 1) دون ضربها في OA ؛ أو قسمتها على OA بدل ضربها فنجد OK = 1/(a(a² + 1)) ؛ أو قلبها فنجد OK = a × (a² + 1). » (options inchangées ; Q5 garde sa place avant Q7, dont l'énoncé rappelle OK = a/(a² + 1) : pas de fuite dans l'ordre de la quête. d2 défendable — OM se lit, puis un seul Thalès ; la classer d3 l'enverrait après Q7, dont l'énoncé montre OK = a/(a² + 1) : garder d2.)
  3. **Q8 + Q9 + Q10 → une seule question**, la 4b officielle (d3) : énoncé « (O, I, J) معيّن متعامد حيث OI = OJ = 1 ، والنقطة A(a ; 0) حيث a > 1 ، والنقطة K من [OA] حيث OK = a/(a² + 1). نفترض أنّ OK = 2/5 ، ونعلم أنّه لكلّ عدد حقيقي x :\n(x − 2)(x − 1/2) = x² − (5/2)x + 1\nأيّ الجمل التالية صحيحة ؟ » ;
     options `a` « a = 2 ، إذن OA = 2 × OI ، فالنقطة I منتصف [OA] » (clé), `b` « a = 1/2 أو a = 2 ، والنقطة I منتصف [OA] في الحالتين » (`math.alg.solution-hors-contrainte-gardee`), `c` « a = 1/2 ، إذن OA < OI ، فالنقطة I ليست منتصف [OA] » (`math.alg.solution-hors-contrainte-gardee`), `d` « a = 2 ، لكنّ OI ≠ OA ، فالنقطة I ليست منتصف [OA] » (muette : OI comparé à OA au lieu de IA) ;
     explication « بالضرب التقاطعي في a/(a² + 1) = 2/5 : 5a = 2a² + 2 ، أي 2a² − 5a + 2 = 0 ، وبقسمة الطرفين على 2 : a² − (5/2)a + 1 = 0 ، وحسب المتطابقة (a − 2)(a − 1/2) = 0 ، فـ a = 2 أو a = 1/2. والشرط a > 1 يُقصي 1/2 ، إذن a = 2 و A(2 ; 0). والنقطة I(1 ; 0) من [OA] و OI = 1 = OA/2 ، فهي منتصف [OA] ✓. الخطأ الشائع: الاحتفاظ بالحلّ 1/2 رغم الشرط a > 1 ، أو بالحلّين معًا ؛ أو مقارنة OI بـ OA بدل مقارنتها بـ IA = 2 − 1 = 1. »
     Vérifié (sympy : solutions 1/2 et 2) ; longueurs 46 / 51 / 49 / 48 (clé la plus courte) ; plan 2×2
     (valeur de a × jugement), vote à égalité sur « a = 2 » et sur « منتصف ».
  Mission : 8 questions, d1 · d2 × 6 · d3 ; aucune clé dans un autre énoncé hors fuites S.
- **18-b [mineur · étage de complaisance]** en l'état Q9 (choisir la solution > 1 parmi deux données) et
  Q10 (I milieu avec O, I, A donnés) sont des d1 étiquetés d3 ; l'option `d` de Q9 (« لا توجد قيمة … »)
  tombe à vue puisque l'énoncé donne 2 > 1, et l'énoncé de Q9 ne dit pas que a est solution de
  l'équation. Tout disparaît avec 18-a.3.
- **18-c [mineur · étiquettes]** Q6 `a` « x² − (3/2)x + 1 » (x × (−1/2) pris positif) est muette alors que
  c'est l'erreur de `math.int.produit-signes-negatifs`, portée par `b` (plan 2×2 : `a` et `b` une erreur
  chacune, `d` les deux) → poser ce tag sur `a`. Q2 `a` « 1 » (a ÷ a au lieu de a × a) et Q5 `c` (÷ OA au
  lieu de × OA) portent `math.num.operation-inverse-appliquee`, dont le libellé ne cite que « جمعًا بدل
  الطرح ، أو جمعًا بدل الضرب » : l'élève qui a divisé lit qu'il a additionné — **élargir le libellé du
  registre** (« … ou une division au lieu d'une multiplication, ou l'inverse ») ou laisser muet.

Étage : d3 boss justifié par la longueur de la chaîne et, après 18-a, par la question finale ; en l'état
la mission se joue en d2 (neuf items à une étape).

---

## Fichier 19 — `19-examen-2013-technique-ex2-terrain-thales-echelle-aire-prix.json`

Transcription : `2013-technique.md`, exercice 2 (plan au 1/1000 ; rectangle ABCD, AD = 4 cm, DC = 6 cm ;
BEF rectangle en B, EB = 2 cm, D, E, F alignés ; 1) AE ; 2a) expliquer EB/EA = FB/AD ; 2b) FB = 2 cm ;
3) aire réelle de BEF = 200 m² ; 4) prix minimum du m² pour 18 000 dinars). En-tête d3 · boss · 120/30 ·
`displayOrder` 19 ✓. Titre ✓.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 4 | c | OK | AE = DC − EB = 6 − 2 |
| 2 | a (⊥ commune à (AB) ⇒ ∥, Thalès papillon de sommet E) | a | **réserve majeure** | `c` défendable (défaut 19-b) |
| 3 | 2/4 = FB/4 | d | OK · réserve fuite | substitution |
| 4 | 2 | b | OK · réserve fuite | 4 × FB = 8 |
| 5 | 20 | c | OK | 2 × 1000 = 2000 cm = 20 m |
| 6 | 200 | b | OK · réserve fuite | 20 m × 20 m ÷ 2 |
| 7 | 200 × p ≥ 18000 | a | OK · réserve étage | « au moins » ⇒ ≥, recette = produit |
| 8 | 90 | d | OK · réserve fuite + forme | 18000 ÷ 200 |

Contrôles :
- **Figure** (Q1, Q2, Q6 ; même dessin) : 30 px/cm ; A(58;92), B(238;92), C(238;212), D(58;212),
  E(178;92), F(238;32) : AD = 4 cm, DC = 6 cm, EB = 2 cm exacts ; D, E, F alignés (pentes −1 et −1) ✓ ; F sur la
  perpendiculaire à (AB) en B ✓ ; angles droits codés en A, D (rectangle) et B (donné) ✓ ; [EB] en pointillé
  et longueurs portées sur des segments entiers ✓ ; triangle BEF grisé (désigne l'objet) ✓. Toute figure
  cohérente avec ces étiquettes a FB = EB : la figure montre donc [BF] égal à [EB], ce que personne ne peut
  éviter sans la rendre fausse — sans gravité.
- **Gloses de l'échelle** : Q5 « السلّم 1/1000 ، أي أنّ كلّ 1 cm في التصميم يمثّل 1000 cm في الواقع » : juste,
  suffisante, ne donne pas la clé (reste × 1000 puis ÷ 100). Q6 « كلّ 1 cm في التصميم يمثّل 10 m في الواقع » :
  juste, mais c'est la **clé de Q5** toute faite (défaut 19-a). (L'échelle est d'ailleurs un acquis de 6ᵉ :
  leçon « أوظّف التّناسب في السّلّم » du programme de 6ᵉ ; la glose reste bienvenue.)
- **Rapport des aires (Q6)** : la question se résout par les longueurs réelles (20 m et 20 m) puis l'aire
  du triangle — aucune règle k² requise ; l'explication dérive 1 cm² ↔ 100 m² de 1 cm ↔ 10 m, en contrôle :
  recevable.
- **Adaptation « prix minimum » → condition (Q7) puis valeur (Q8)** : ne déforme rien (la traduction
  « au moins » ⇒ ≥ est au programme des inéquations de 04) ✓.
- **Étiquettes** : Q1 `d` 8 `operation-inverse-appliquee` exact (addition au lieu de soustraction) ; Q2
  `b` `thales-reciproque-role` exact ; Q3 `a`/`b` exacts, `c` double muette ; Q4 `a` 4/3 `formes-melangees`,
  `c` 4 `longueurs-au-lieu-de-rapports`, `d` 8 `rapport-inverse` exacts ; Q5 `b` 200
  `puissance-de-dix-rangs-mal-comptes` exact ; Q6 `a` `aire-triangle-sans-moitie` exact, `d` 2
  `reponse-a-l-autre-inconnue` acceptable ; Q7 `c` somme au lieu de produit : exact ; Q8 `a`/`c`
  `rangs-mal-comptes` exacts, `b` 1/90 `numerateur-denominateur-inverses` exact (200/18000).
- **Explications** : égalités toutes justes (4 × FB = 8 ; 2000 ÷ 100 = 20 ; (20 × 20)/2 = 200 ; 200 × 90 =
  18000).
- **Rendu arabe** : un seul écart hors conception — voir 19-e. **Doublons** : aucun (seules 14 et 19 portent
  l'échelle ; 14 est une distance, 19 une aire et un prix).

Défauts de 19 :
- **19-a [majeur · fuites évitables]** Q3 et Q4 donnent « EA = 4 » (**clé de Q1**, résultat que le sujet fait
  CALCULER) ; la glose de Q6 « 1 cm … يمثّل 10 m » livre la conversion qui fait toute Q5 (**clé de Q5** : 2 × 10 =
  20 m) ; Q8 donne « 200 × p ≥ 18000 » (**clé de Q7**, étape de l'auteur). (Fuites S tolérées : Q6 ← FB = 2,
  Q7 ← 200 m², énoncés officiels « استنتج / أثبت ».) Correctifs :
  - Q3 et Q4 : remplacer la ligne « EB = 2 ، EA = 4 ، AD = 4 » par « في تصميم قطعة الأرض ABCD مستطيل والنقطة E من [AB] ، والأطوال بالصنتمتر :\nAD = 4 ، DC = 6 ، EB = 2 » (l'élève retrouve EA = 6 − 2 ; le distracteur 2/6 de Q3 y gagne en
    vraisemblance) ; dans les deux explications, ajouter en tête « في المستطيل AB = DC = 6 ، فـ EA = 6 − 2 = 4. ».
  - Q6 : glose « كلّ 1 cm في التصميم يمثّل 1000 cm في الواقع » au lieu de « … 10 m … » ; Q6 passe d3
    (échelle + conversion + aire) ; explication : « في الواقع EB = FB = 2 × 1000 = 2000 cm = 20 m … » (le reste
    inchangé).
  - Q8 : énoncé « المساحة الحقيقية للجزء BEF هي 200 m² ، ويريد صاحب الأرض شراء سيّارة ثمنها 18000 دينار ببيع هذا الجزء. ما السعر الأدنى لبيع المتر المربّع الواحد بالدينار الذي يمكّنه من شراء السيّارة ؟ » (l'inéquation n'apparaît plus que dans l'explication, après Q7).
- **19-b [majeur · option d'argumentation défendable]** Q2 `c` « (FB) ∥ (AD) لأنّ ABCD مستطيل ، ثمّ نطبّق نظرية
  طاليس … » n'est **pas fausse sans ambiguïté** : F est sur la perpendiculaire à (AB) en B, donc sur (BC), et
  la figure la montre dans le prolongement de [CB] ; « (FB) ∥ (AD) car ABCD est un rectangle » est un
  raccourci que beaucoup accepteront. L'explication affirme en outre à tort que le rectangle « لا يقول شيئًا عن
  (FB) » alors que (FB) = (BC). Correctif : `c` → « (FB) ∥ (AD) لأنّ D و E و F على استقامة واحدة ، ثمّ نطبّق
  نظرية طاليس في وضعية الفراشة ذات الرأس E » ; `d` → « (FB) ∥ (AD) لأنّ D و E و F على استقامة واحدة ، ثمّ نطبّق
  النظرية العكسية لطاليس في وضعية الفراشة ذات الرأس E » ; dans l'explication remplacer « الاستناد إلى المستطيل
  لتبرير توازٍ لا يخصّه ، فالمستطيل يعطي (AD) ∥ (BC) ولا يقول شيئًا عن (FB) » par « تبرير التوازي باستقامة
  النقاط D و E و F ، وهي لا تقول شيئًا عن اتّجاهَي (FB) و (AD) ». Longueurs : a 94 · b 105 · c 97 · d 108 → clé
  non la plus longue ; `c` reprend elle aussi des mots de l'énoncé ; aucune prémisse niée.
- **19-c [mineur · étage de complaisance]** Q7 (une traduction en inéquation) et Q8 (une division) sont des d2
  réels étiquetés d3 ; Q6 (d2) devient d3 avec 19-a. Étage de la mission : d3 défendable (7 points officiels,
  quatre notions) une fois 19-a appliqué.
- **19-d [mineur · forme]** Q8 : 9, 90, 900 encadrent la clé d'un zéro de moins et d'un zéro de plus — la
  valeur du milieu se choisit sans calcul. Correctif : `c` « 9 » → « 45 » (muette : aire 400 m² prise sans la
  moitié, 18000 ÷ 400) ; explication : remplacer « فنجد 9 أو 900 » par « فنجد 900 ؛ أو القسمة على 400 ، أي
  مساحة المثلّث دون القسمة على 2 ، فنجد 45 ». Q6 : chaque distracteur (400, 20, 2) ne change qu'un facteur de la
  clé et aucun n'en cumule deux ; plan 2×2 suggéré : `d` « 2 » → « 40 » (muette : sans la moitié ET × 10 au lieu
  de × 100) et l'explication en conséquence.
- **19-e [mineur · rendu]** explication de Q5 : « فنجد 2 cm = 0,02 m » s'affiche « cm = 0,02 m 2 » (le « 2 »
  détaché à droite du bloc : nombre + unité ouvrant une égalité, forme que le moteur n'isole pas).
  Correctif : « فنجد 0,02 m بدل 20 m ».
- Étiquettes : Q5 `a` « 2000 » (résultat intermédiaire en cm) pourrait porter
  `math.alg.reponse-a-l-autre-inconnue` ; Q6 `c` « 20 » : voir l'étiquette proposée n° 3.

---

## Fichier 20 — `20-examen-2025-technique-ex3-phare-mur-thales.json`

Transcription : `2025-technique.md`, exercice 3 (voiture face à un mur ; (AB) et (PH) ⊥ (MH) ; AH = 300,
PH = 60 ; I) MH = 3000 : 1) montrer MA = 2700 ; 2a) position de (AB) et (PH) ; 2b) expliquer MA/MH = AB/PH ;
2c) en déduire AB = 54 ; II) MH = 4500 : montrer AB = 56). En-tête d3 · boss · 120/30 · `displayOrder` 20 ✓.
Titre ✓.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 2700 | b | OK | 3000 − 300 |
| 2 | parallèles, car toutes deux ⊥ (MH) | a | OK · réserve fuite | |
| 3 | MA/MH = AB/PH | a | OK | Thalès de sommet M |
| 4 | 9/10 | b | OK · réserve fuite | 2700/3000 |
| 5 | 54 | d | OK · réserve fuite | 60 × 9/10 |
| 6 | 56 | c | OK | MA = 4200 ; 60 × 4200/4500 = 60 × 14/15 |

Contrôles :
- **Figure** (Q1–Q3, identique) : H(60;186), P(60;148), A(130;186), B(130;159,08), M(300;186) ; P, B, M
  alignés (pentes 0,1583 et 0,1584) ✓ ; (PH) et (AB) verticales ⊥ sol, angles droits codés en H et A
  (donnés) ✓ ; coupure « // » sur le sol et `<title>` « رسم غير مقيس » : figure hors échelle assumée,
  cohérente avec l'ajout « وهو غير مرسوم بمقياس الرسم » ; AB/PH = MA/MH = 0,708 dans le dessin (Thalès
  respecté) ; aucune longueur portée, aucune clé ✓ ; `<rect>` admis, arabe seulement dans `<title>`.
- **Fidélité** : données identiques ; l'adaptation « expliquer pourquoi MA/MH = AB/PH » → « quelle égalité
  donne Thalès » (Q3) perd la citation explicite des conditions, que Q2 (parallélisme avec sa raison)
  reprend : perte légère, acceptable.
- **Programme** : soustraction de longueurs, perpendiculaires à une même droite (acquis), Thalès (08),
  fraction d'un nombre (acquis) ✓.
- **Étiquettes** : Q1 `a` 300 `reponse-a-l-autre-inconnue` acceptable, `d` 3300 `operation-inverse-appliquee`
  exact ; Q2 `b` `regle-perpendiculaire-parallele-inversee` exact ; Q3 `b` `formes-melangees`, `c`
  `rapport-inverse` exacts, `d` double muette ; Q4 `c` 11/10 (MA = 3000 + 300) `operation-inverse-appliquee`
  exact, `d` 10/9 `rapport-inverse` exact ; Q5 `a` 600 `fraction-d-un-nombre-multipliee-au-lieu-de-divisee`,
  `b` 6 et `c` 540 `fraction-d-un-nombre-etape-oubliee` exacts ; Q6 `d` 64 (MA = 4800) exact.
- **Explications** : toutes justes (2700/3000 = 9/10 ; 60 × 9/10 = 54 ; 4200/4500 = 14/15 ; 60 × 14/15 = 56 ;
  60 × 300/4500 = 4 ; 60 × 4800/4500 = 64).
- **Rendu arabe** : aucun défaut. **Doublons** : aucun (situation inédite dans le corpus).

Défauts de 20 :
- **20-a [majeur · fuites évitables]** Q3 pose « (AB) ∥ (PH) » : c'est la **clé de Q2** (le sujet DEMANDE cette
  position, il ne la donne pas) ; Q5 pose « MA/MH = 9/10 » : **clé de Q4** (étape de l'auteur). (Fuites S
  tolérées : Q4 ← MA = 2700, Q5 et Q6 ← MA/MH = AB/PH, énoncés officiels.) Correctifs :
  - Q3 : « (AB) ∥ (PH) ، » → « المستقيمان (AB) و (PH) عموديان على (MH) ، » ; explication précédée de
    « (AB) و (PH) عموديان على (MH) فهما متوازيان ؛ ».
  - Q5 : « ونعلم أنّ MA/MH = 9/10 وأنّ PH = 60 » → « ونعلم أنّ MA = 2700 و MH = 3000 و PH = 60 » ;
    explication : remplacer « من AB/PH = 9/10 » par « MA/MH = 2700/3000 = 9/10 ، فـ AB/PH = 9/10 ، ومنه ». Q5
    reste d2 (deux petites étapes), avant Q6.
- **20-b [mineur · étiquettes existantes non posées]** Q4 `a` « 1/10 » (AH/MH : le rapport de l'autre
  segment) mérite `math.alg.reponse-a-l-autre-inconnue`, comme le publié `08/11` Q4 `d` (OB donné pour ON) ;
  Q6 `b` « 54 » (valeur du cas I rendue pour le cas II) aussi.
- **20-c [mineur · étage]** la plus facile des cinq d3 : Q1–Q2 d1, Q3–Q5 d2 à une étape, seule Q6 en
  enchaîne trois. **Avis : d2 practice (75/15) serait plus juste** ; d3 ne se défend que par le poids
  officiel (7 points) et par Q6.

---

## Étiquettes — bilan de la tranche

Mesuré : 51 questions, 153 distracteurs, **90 étiquetés / 63 muets, 31 identifiants**, tous présents dans le
registre d'`origin/main` ; toutes les compétences existent. Aucune clé n'est étiquetée.

**Retraits / ajouts de l'auteur.** Avec le libellé ÉLARGI de `math.num.racine-distribuee-sur-somme` (« … ou tu
fusionnes deux racines ainsi »), **13 Q2 `b`** (√16 + √9 → √25) et **15 Q1 `a`** (√12 − √3 → √9) le méritent de
nouveau (défauts 13-a, 15-a). `numerateur-denominateur-inverses` sur 13 Q1 `d` (21/3 = 7 puis 7³) : exact.
`thales-longueurs-au-lieu-de-rapports` sur 16 Q5 `c` (BM = OA « parce que parallèles ») : exact.

**Étiquettes existantes à poser** (options muettes ou mal étiquetées) : 13 Q2 `b` et 15 Q1 `a`
→ `racine-distribuee-sur-somme` ; 14 Q4 `a` → `puissance-de-dix-sens-inverse` (au lieu de
`operation-inverse-appliquee`) ; 17 Q2 `a` → `carre-difference-signes` ; 17 Q3 `a` →
`difference-carres-second-terme-non-eleve-au-carre` ; 18 Q6 `a` → `int.produit-signes-negatifs` ; **19 Q6 `c`
« 20 » → `math.mes.conversion-aire-facteur-errone`** (« une aire se convertit par 100, pas par 10 » : c'est
exactement 2 cm² × 10 au lieu de × 100) ; 19 Q5 `a`, 20 Q4 `a`, 20 Q6 `b` →
`math.alg.reponse-a-l-autre-inconnue`. Libellé à élargir au registre : `math.num.operation-inverse-appliquee`
ne cite que « addition au lieu de soustraction, somme au lieu de produit » alors qu'elle sert ici pour une
soustraction au lieu d'une addition (13 Q2 `a`) et pour ÷ au lieu de × (13 Q3 `d`, 18 Q2 `a`, 18 Q5 `c`).

**Les neuf étiquettes proposées** (seuil : ≥ 3 questions distinctes + une phrase d'élève) — décompte par
recherche des mécanismes dans les options ET explications de toutes les missions et quiz de maths publiés :

| n° | identifiant proposé | tranche (questions) | publié `origin/main` (questions, toutes muettes sauf mention) | libellé exact ? étiquette existante ? | verdict |
| --- | --- | --- | --- | --- | --- |
| 1 | `racines-regroupees-sous-un-radical` | 13 Q2, 15 Q1 → 2 | 26 questions portent déjà `racine-distribuee-sur-somme`, dont la fusion (03/07 Q1, 03/09 Q1, 03/26 Q3, 04/14 Q1…) | couvert par le libellé élargi de `racine-distribuee-sur-somme` | **refusée** — poser l'existante |
| 2 | `pourcentage-applique-au-prix-final` | 15 Q4 → 1 (2 avec 13 Q3 `d` si « base confondue ») | 0 | libellé juste pour 15 Q4 `a` et `d` ; rien d'existant (`percent.of-confused-with-off` est autre chose) | **refusée** (< 3) — options muettes |
| 3 | `rapport-longueurs-aires-confondus` | 19 Q6 (l'option est **`c`** « 20 », pas `b` qui est la clé 200), 16 Q5 → 2 | 08/06 Q2 `a` (60 cm²), 08/04 Q6 `d` (28) | le libellé citerait la règle k² des aires, **hors programme de 9ᵉ** (manuel ch. 10 : agrandissement/réduction absents ; enseignée seulement dans `13-geometrie-espace`, hors manifeste) ; 19 Q6 `c` est couverte par `mes.conversion-aire-facteur-errone` | **refusée** — existante pour 19 Q6 `c` ; 16 Q5 `a` à remplacer (16-c) |
| 4 | `droite-des-milieux-mauvais-cote` | 13 Q4, 15 Q3 → 2 | 18/07-devoir Q5 `a` (2,5 = AB/2), 18/12-devoir Q2 `d`/`e` (IK = AB/2, IL = AD/2), 18/19-devoir Q3 (AB/2 = 6 relevé comme erreur) → 3 | aucune existante (`droite-des-milieux-facteur-deux` = le facteur) ; libellé proposé : « Tu prends la moitié d'un côté qui porte l'un des milieux : le segment des milieux vaut la moitié du TROISIÈME côté, celui qui ne passe par aucun des deux » / « تأخذ نصف ضلع يمرّ منه أحد المنتصفين: القطعة الواصلة بين المنتصفين تساوي نصف الضلع الثالث الذي لا يمرّ منه أيّ منهما » ; compétence `math.geo.triangles-base` | **acceptée** (5 questions) — 13 Q4 `a`,`b` ; 15 Q3 `b`,`d` ; 13 Q4 `c` reste muette (double) |
| 5 | `thales-segment-complementaire` | 20 Q4, 20 Q6 → 2 (une seule mission) | 08/11-devoir Q4 `d` (OB donné pour ON) — étiqueté `reponse-a-l-autre-inconnue` | 20 Q4 `a` (AH/MH donné pour MA/MH) est exactement `reponse-a-l-autre-inconnue` ; seule 20 Q6 `a` (AH employé DANS le rapport) resterait | **refusée** — existante pour 20 Q4 `a`, 20 Q6 `a` muette |
| 6 | `milieu-difference-au-lieu-de-somme` | 16 Q2 → 1 | 09/09-devoir Q8 `d`, 12/07-devoir Q5 `b`, 18/07-devoir Q2 `c`, 18/08-devoir Q1 `c`, 18/11-devoir Q1 `a` (+ `c`), 18/17-devoir Q2 `c` → 6 | aucune existante ; libellé : « Tu prends la moitié de la DIFFÉRENCE des coordonnées (ou la différence entière) : le milieu a pour coordonnées la moitié de leur SOMME » / « تأخذ نصف الفرق بين الإحداثيّات (أو الفرق كاملًا): إحداثيّتا المنتصف هما نصف مجموع إحداثيّتي الطرفين ». **Préfixe** : garder `math.vec.` — c'est celui de la sœur `math.vec.milieu-sans-moitie` et de la compétence `math.vec.repere-calculs` (« Calculs dans un repère : milieu, distance, symétrique »), qui porte déjà tous les calculs de repère du chapitre 12 ; renommer la famille re-clé les missions publiées. À corriger au registre en revanche : `math.vec.repere-calculs` a pour prérequis `math.vec.somme` (vecteurs, hors programme 9ᵉ) | **acceptée** (7 questions), compétence `math.vec.repere-calculs` |
| 7 | `position-relative-ignoree` | 18 Q3, 16 Q6 → 2 | 08/11-devoir Q4 `c` (9 cm : O mis hors de [BN]), 09/09-devoir Q6 `c` (5 : H mis hors de [BO]) → 2 | aucune existante ; libellé à écrire pour couvrir « ajouter ou retrancher » ET « de quel côté » : « Tu ignores la position relative des points : selon que le point est ENTRE les deux autres ou À L'EXTÉRIEUR (et de quel côté), les longueurs se retranchent ou s'additionnent » / « تُهمل الوضعيّة النسبيّة للنقاط: حسب وقوع النقطة بين النقطتين الأخريين أو خارجهما (وفي أيّ جهة) تُطرح الأطوال أو تُجمع » ; compétence la plus proche `math.geo.thales-direct` (3 des 4 cas) | **acceptée** (4 questions) |
| 8 | `produit-nul-un-seul-facteur` | 17 Q4, 18 Q8 → 2 | 09/14-devoir Q4 `b` (« موضع واحد » : une seule des deux racines) → 1 | aucune existante ne dit « un seul facteur annulé » (`division-par-inconnue-perd-solution` et `racine-carree-negative-oubliee` sont des cas particuliers) ; **recoupement** : l'autre lot propose `produit-nul-une-seule-solution` (absente d'`origin/main`) — même erreur : **un seul identifiant**. Libellé : « Tu n'annules qu'un des facteurs : un produit est nul dès que l'UN OU l'AUTRE l'est, et chaque facteur nul donne une solution » / « تُعدِم أحد العاملين فقط: الجداء ينعدم بانعدام أحدهما، وكلّ عامل معدوم يعطي حلًّا » ; compétence `math.alg.equations-produit` | **acceptée** (3 questions, seuil juste atteint), fusionnée avec la proposition de l'autre lot |
| 9 | `solution-negative-rendue-positive` | 17 Q7 → 1 | 08/12-devoir Q7 `b` (√3 − 1 : la racine 1 − √3 rendue positive) → 1 | libellé juste ; rien d'existant | **refusée** (2 < 3) — muette ; l'occurrence de 17 disparaît avec 17-a |

---

## Récapitulatif des points d'attention

- **Aveugle** : 51/51 clés retrouvées avant lecture ; **aucune divergence**. Toutes les explications recalculées
  justes (aucune égalité fausse, aucun mécanisme d'erreur qui ne produise pas sa valeur).
- **Adaptations signalées par l'auteur** : 2003 « placer » → « quel point est mal placé » : garde la
  compétence ; « prouver O milieu » → calcul du milieu : fidèle ; 2010 générale (écriture, égalité, équation) :
  fidèles ; 2013 technique « prix minimum » → condition puis valeur : fidèle ; 2025 technique 2b → « quelle
  égalité » : perte légère de la justification, compensée par Q2. **Non signalée** : 2010 technique Q3, le
  distracteur officiel 47,5 retiré (13-c). Aucun item écarté ni « admis », aucun marqueur hors programme.
- **Gloses** : 14 Q4 et 19 Q5 justes, suffisantes, sans clé ; **19 Q6 « 1 cm = 10 m » juste mais c'est la clé
  de Q5** (19-a). L'échelle est au programme de 6ᵉ (« أوظّف التّناسب في السّلّم »).
- **Programme** : droite des milieux enseignée (cours 08, étape 1 de l'exemple du centre de gravité, nommée ;
  manuel ch. 10 §I.2) — mais seulement au détour d'un exemple, remarque pour le cours ; hausse en % et
  ÷ 1,08 : acquis de 6ᵉ + mise en équation (04), le manuel pose ce problème inverse au rappel du ch. 7 ;
  aires : 19 Q6 se résout par les longueurs réelles, **16 Q5 invoque k²** (16-c) ; factorisation de 17 : indice
  officiel donné ; ni vecteur ni translation (les identifiants `math.vec.*` ne sont que des noms historiques
  des calculs de repère).
- **Étages** : 13–15 d2 justes ; 16–19 d3 justifiés **après** leurs correctifs de fuites (qui transforment
  des items à une étape en chaînes) ; **20 : d2 plus juste** (20-c). Rampes internes toutes non décroissantes ;
  étiquettes de complaisance : 14 Q4–Q5, 17 Q7–Q8, 18 Q9–Q10, 19 Q7–Q8.
- **Indices de forme** : aucune clé strictement la plus longue (`content:tranche` : 0 dans la tranche), aucune
  option somme ou différence de deux autres (contrôle par script), plans 2×2 annoncés **vérifiés** (14 Q2, 16 Q4,
  17 Q5–Q6, 18 Q1, Q3, Q4, Q6, Q7, 19 Q7, 20 Q3 — plus 19 Q3 ; en 18 Q6, `a` est à étiqueter) sauf **14 Q1**
  (union, 14-b) et **19 Q2** (`c` défendable, 19-b) ; valeur du milieu d'une triade 9/90/900 en 19 Q8 (19-d). Questions
  d'argumentation : 14 Q1 ✗ (14-b), 18 Q10 ✓, 19 Q2 ✗ (19-b).
- **Titres** : format « 🏛️ مناظرة … · التمرين N ⭐…: » respecté, « (تقني) » partout où il faut, aucun
  résultat dans un sujet ; étages et `displayOrder` 13 → 20 ✓. **`chapter.json`** : seule la ligne `sources[]`
  diffère d'`origin/main`, mot pour mot celle des chapitres publiés ✓.
- **Doublons** : aucun avec 01–12, ni avec 12, 09, 03, 04, 17 publiés (`content:tranche` : aucune paire
  proche impliquant 13–20) ; gabarits voisins signalés sans défaut : 13 Q4 / 15 Q3 (deux angles), 17 / 18 /
  `08/12` (même famille de pièges), 15 Q2 / `12/04` Q3.
- **Fuites** : c'est le défaut systémique de la tranche — **27 énoncés sur 51** redonnent au moins une clé
  d'une autre question de leur mission, **34 cas** (14 : 2 ; 16 : 4 ; 17 : 6 ; 18 : 11 ; 19 : 6 ; 20 : 5), dont
  **19 évitables (É)** et 15 structurels (S). Aucune fuite « en avant » par une explication (contrôle par
  script de l'ordre d'émission).
- **Rendu arabe** (`splitMathRuns` / `isDisplayEquation` en Chromium `dir=rtl`, 314 chaînes) : un seul écart
  hors conception, « 2 cm = 0,02 m » dans l'explication de 19 Q5 (19-e). Les lignes de données « AB = 5 ،
  AC = 7 ، … » s'affichent d'un seul tenant de gauche à droite (virgule arabe de classe CS).
- **Piège de passe** : « على الشكل التالي » n'apparaît qu'en 16 Q1 (« فحصل على الشكل التالي »), où c'est bien un
  renvoi à la figure, présente ✓ ; aucun renvoi sans SVG.
- **Figures** : **18 SVG** (11 dessins distincts, tous en énoncé, aucun en option — et non 22) ; toutes vraies
  (coordonnées recalculées), aucune clé, aucun élément ni attribut interdit, rien hors `viewBox` ; la seule
  entorse est « نهر » dans le dessin de 14 (14-d). La figure de 16 Q1 est fausse à dessein (B en (3 ; −2)) ✓.
- **Gates** (moteur `origin/main`, copie isolée du corpus) : `content:check` vert ; `content:qa --subject math` :
  0 erreur, aucun avertissement sur 08 ; `content:tranche --chapters 08` : clé la plus longue 3 % (aucune de la
  tranche), aucune paire proche ni candidat gabarit pour 13–20.

---

## Défauts classés (liste consolidée ; correctifs exacts dans les sections par fichier)

**Critiques (clé fausse, double réponse, figure fausse) : aucun.** (19-b frôle la double réponse.)

**Majeurs (11)**
1. **14-a** — fuites Q5 ← Q4 (É) et Q4 ← Q3 (S), Q4/Q5 paire proche, deux d1 étiquetés d2 → fusion de Q4 et
   Q5 en une 2b « en mètres » depuis les données brutes (d3).
2. **14-b** — Q1 : la clé est la seule à réunir les deux hypothèses (union) → `b` reprend les mêmes
   hypothèses avec la réciproque.
3. **16-a** — Q1 : « النقاط التي وُضعت في غير موضعها » annonce plusieurs points → « النقطة أو النقاط ».
4. **16-b** — fuites Q4 (É), Q5 (É + S), Q6 (S) → Q4 « O من [BC] », Q5 et Q6 depuis les données brutes.
5. **16-c** — Q5 `a` « 12 » expliqué par la règle k² des aires, hors programme → `a` « 5 ».
6. **16-d** — Q2 `b` « (−2 ; 3) » = l'extrémité B, éliminée à vue → « (0,5 ; −0,5) ».
7. **17-a** — six fuites (É : Q4, Q7, Q8 ; S : Q3, Q6, Q7) → reprise en 7 questions (Q2 étape de
   développement ; Q4 depuis (x + 1)² − 9 ; Q6 depuis la figure ; Q7 + Q8 fusionnées en la 3b).
8. **18-a** — fuites É (Q4, Q5 ×2, Q8, Q9 ×2, Q10) → Q4 sans M(0 ; a² + 1) ; Q5 depuis E(0 ; a²) ; Q8 + Q9 + Q10
   fusionnées en la 4b.
9. **19-a** — fuites É (Q3, Q4 ← EA = 4 ; Q6 ← glose « 10 m » ; Q8 ← l'inéquation) → DC = 6 au lieu de EA = 4,
   glose « 1000 cm » en Q6, Q8 depuis les données.
10. **19-b** — Q2 `c`/`d` (« لأنّ ABCD مستطيل ») pas fausses sans ambiguïté, explication inexacte → raison
    « D و E و F على استقامة واحدة ».
11. **20-a** — fuites É (Q3 ← Q2, Q5 ← Q4) → Q3 « عموديان على (MH) », Q5 avec MA = 2700 et MH = 3000.

**Mineurs (15)** — 13-a, 13-b, 13-c (fidélité : 47,5 officiel retiré), 14-c, 14-d (« نهر » dans le dessin),
15-a, 17-b, 17-c, 18-b, 18-c, 19-c, 19-d, 19-e (rendu « 2 cm = 0,02 m »), 20-b, 20-c ; plus, sans reprise
exigée : les fuites S tolérées de 18 (Q2, Q3, Q7, Q8), 19 (Q6, Q7) et 20 (Q4, Q5, Q6), l'élargissement du
libellé de `operation-inverse-appliquee` et le prérequis `math.vec.somme` de `math.vec.repere-calculs`
(registre, hors du lot de l'auteur).

**Étiquettes nouvelles** : acceptées n° 4 (`droite-des-milieux-mauvais-cote`), n° 6
(`math.vec.milieu-difference-au-lieu-de-somme`), n° 7 (`position-relative-ignoree`), n° 8
(`produit-nul-un-seul-facteur`, **fusionnée** avec `produit-nul-une-seule-solution` de l'autre lot) ; refusées
n° 1, 3, 5 (une existante couvre), n° 2 et 9 (< 3 questions). L'ajout au registre reste à l'orchestrateur
(l'auteur n'édite pas `misconceptions.json`).

---

## Chiffre final

- **Questions auditées : 51** (8 missions, 18 SVG) + la ligne `sources[]` du `chapter.json` (conforme).
- **Clés fausses : 0** (51/51 retrouvées à l'aveugle ; explications toutes justes).
- **Questions à reprendre : 37**, dont **25 touchées par un défaut majeur** (14 : Q1, Q4, Q5 · 16 : Q1, Q2, Q4, Q5,
  Q6 · 17 : Q2, Q4, Q6, Q7, Q8 · 18 : Q4, Q5, Q8, Q9, Q10 · 19 : Q2, Q3, Q4, Q6, Q8 · 20 : Q3, Q5) et 12
  seulement par un mineur (13 : Q2, Q3 · 14 : Q2, Q3 (figure) · 15 : Q1 · 17 : Q3 · 18 : Q2, Q6 · 19 : Q5, Q7 · 20 :
  Q4, Q6). Défauts : **0 critique · 11 majeurs · 15 mineurs**.
- Verdict : **à reprendre avant publication** — rien de faux, mais la tranche n'est pas prête pour le donjon :
  27 énoncés sur 51 y redonnent une clé, dont 19 fuites évitables.
