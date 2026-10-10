# Re-vérification ciblée — tranche L16 (maths 9ᵉ, ch. 18, missions 29 à 35) après le tour de corrections

Auditeur indépendant (même consigne que `audit-L16.md`). Fichiers relus dans l'arbre de travail tels quels
(md5 : 29 `64c602ba` · 30 `ada301e8` · 31 `da4aebad` · 32 `d3676d34` · 33 `96794708` · 34 `3a8d4d43` · 35 `b843484b`) ;
version auditée = ma copie du 2026-10-02 (md5 identiques à ceux de `audit-L16.md`). Questions touchées re-résolues à
l'aveugle AVANT lecture de la clé ; rien n'est modifié dans le dépôt. Priorité : les défauts INTRODUITS par les
correctifs (les miens comme ceux de l'auteur).

_Re-vérification complète : fichiers 29 à 35, étiquettes (dont le dossier en attente), gates, chiffre final._

## Méthode

- Diff structurel aveugle (énoncés, options, type, difficulté, figures par empreinte — sans clé, explication ni
  étiquette), questions appariées une à une par similarité d'énoncé (les déplacements de 31, 33, 34, 35 sont suivis).
  Numérotation ci-dessous = celle de l'arbre ACTUEL ; « ex-Qn » = numéro dans la version auditée.
- Rendu : moteur `origin/main` bffcca85 (avec #1160 : `DIGIT_FIRST_FORMULA` accepte « ° » et les lettres grecques ;
  `SvgFigure` posée `dir="ltr"`). Page qui reproduit `RichField`/`OptionContent` (lignes, équations posées, runs
  insécables, figure dans un cadre `w-64`), Chromium headless, `dir=rtl`, à 800 et 400 px ; détecteur : tout noyau
  de formule à lettre latine + opérateur dont l'ordre visuel n'est pas gauche-à-droite. Contrôle positif : avec
  l'ancien `bidi.ts`, « ظا 30° = OI/OB » est signalé (« OI/OB = °30 »), avec le nouveau il ne l'est plus ;
  « 3 + 3 = 6 cm » reste signalé dans les deux (le détecteur est vivant).
- Registre des étiquettes relu sur `origin/main` 18c8a7ac : aucun libellé existant n'a changé depuis l'audit
  (d8af0b75) ; deux entrées ajoutées hors lot (`math.alg.carre-difference-ecrit-difference-carres`,
  `bio.dig.eau-sans-enzyme`) ; `math.geo.fonction-trigo-mal-choisie` n'y est pas (en attente, `pending-tags/L16.json`).
- Gates en lecture seule sur une copie de travail : corpus `origin/main` 18c8a7ac + les sept fichiers, moteur bffcca85.

## Fichier 29 (11 questions, challenge d4 300/60, rampe 1,1,2,2,2,2,3,3,3,3,3 — inchangés)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (options a, b, c réécrites) | d | d | OK |
| Q3 (explication du « 2 ») | 2√3 | b | OK |
| Q4 (d étiquetée) | a | a | OK |
| Q8 (c rendue muette) | a | a | OK |
| Q10 (d « 2√6 », options, explication) | 4√3 | b | OK |
| « شعاعها » → « نصف قطرها » (Q1, Q2, Q4, Q5, Q7, Q8, Q9, Q10) | 60 · c · c · 60 (Q2, Q5, Q7, Q9) | idem | OK |

- **Q1.** Mes trois textes, mot pour mot. Prémisses toutes vraies ; règles générales toutes fausses sauf celle de d.
  Vote par élément : perpendicularité (a, d), milieu (b, d), cercle (a, c) — a et d sont à égalité, le vote ne
  reconstruit pas la clé. Longueurs a 110 · b 115 · c 94 · d 97 : clé non la plus longue. Étiquettes : a et b
  `condition-suffisante-supposee` (chacune garde UNE des deux conditions de la médiatrice) — exactes ; c muette (fausse
  propriété du cercle, non répertoriée). L'explication, inchangée, couvre toujours les trois gestes.
- **Q3.** Phrase de l'audit appliquée : « طرح الطولين 4 − 2 = 2 بدل طرح مربّعيهما، أو الخلط بين [AH] و [HB] » — juste
  (AB − HB = 2, HB = 2) ; « 2 » reste muet (deux gestes).
- **Q4.** d porte `condition-suffisante-supposee` : propriété du cours privée de « un côté est un diamètre », que
  l'explication nomme déjà. Exact.
- **Q8.** c (✗✗ : prémisse fausse OB ≠ AD et propriété du rectangle) muette. Exact.
- **Q10.** CH = 6, DH = 2√3, CD = √48 = 4√3 ; « 2√6 » = √(36 − 12) ([CH] pris pour hypoténuse) →
  `hypotenuse-mal-choisie` exacte ; « 6 + 2√3 » = CH + DH → `pythagore-sans-carres` exacte (étiquette suivie avec le
  texte, ids permutés) ; « 4 » = √(2² + 12) avec CH = 4 − 2 → `position-relative-ignoree` exacte. Recouvrement avec
  Q5 réduit à {4√3, 4}. Longueurs 7/3/1/3 ; aucune option somme ou différence de deux autres ; phrase d'explication
  ajoutée juste. Cosmétique : options non rangées dans le fichier (6 + 2√3, 4√3, 4, 2√6) — l'affichage les mélange.
- Plus aucun « شعاع » dans les sept fichiers ; figures de 29 inchangées (empreintes identiques).
- Rendu Chromium `dir=rtl` 800/400 px : aucune unité mal ordonnée dans 29.
- En-tête : 5 vraies d3 (Q7 à Q11), inchangées : d4 honnête (constat de l'audit inchangé).

**Verdict 29 : OK.**

## Fichier 30 (12 questions, challenge d4 300/60, rampe 2×7 puis 3×5 — inchangés)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q2 (énoncé « 6 cm », d, étiquettes b c d, explication) | a | a | OK · réserve mineure (résidu de MON correctif) |
| Q3 (énoncé « 6 cm », options a et c) | d | d | OK |
| Q4 (a rendue muette) | 3√3/2 (champs aveugles inchangés) | b | OK |
| Q6 (clé et piège reformulés par l'auteur, explication) | d | d | OK · réserve faible |
| Q8 (options b et c) | a | a | OK |
| Q11 (figure) | 6 | c | OK |

- **Q2.** d = mon texte ; dérivation ajoutée par l'auteur juste de bout en bout : OBE a OB = OE (rayons) et un angle de
  60° en B, il est équilatéral, EB = 3 ; EC² = 36 − 9 = 27, EC = 3√3 ; côtés 3, 3√3, 6 tous différents, donc « ليس
  متقايس الضلعين » est exact. Étiquettes : b, c `hypotenuse-mal-choisie` (angle droit au mauvais sommet = un autre côté
  que le diamètre pris pour hypoténuse, ce que l'explication dit maintenant) et d `description-la-plus-precise-manquee`
  (« …ou tu en ajoutes une que rien ne prouve ») : exactes.
  **Réserve (introduite par mon correctif) :** le sommet E figure dans a et d (2 options sur 4), et b « قائم الزاوية في
  B » contredit la prémisse (angle de 60° de l'équilatéral, déjà signalé à l'audit et que je n'avais pas traité) : b
  écartée, le vote garde {a, d} ; d se réfute de plus à l'œil (EB ≈ 3 contre EC ≈ 5,2 sur la figure). Une question
  « nature » sur figure exacte reste lisible (inhérent, constat de l'audit). Correctif facultatif, vérifié (plan 2×2
  sommet E/C × simple/isocèle : vote E 2 – C 2, isocèle 2 – 2 ; longueurs 17/33/17/33 ; rendu Chromium `dir=rtl`
  800/400 px propre) :
  - b « قائم الزاوية في B » → « قائم الزاوية في C ومتقايس الضلعين » (✗✗ : muette, retirer `hypotenuse-mal-choisie`) ;
  - explication : « الخطأ الشائع: وضع الزاوية القائمة في B أو في C، أي » → « الخطأ الشائع: وضع الزاوية القائمة في C، أي ».
- **Q3.** Mes deux textes mot pour mot, ouverture « طول ضلعه 6 cm » posée. Prémisses vraies (CAB = 60°, E sur (AB)) ;
  vote sans majorité (hauteur a/d, CA = CB c/d, E sur (AB) b/c) ; longueurs 119/91/110/107 ; a et c
  `condition-suffisante-supposee` exactes.
- **Q4.** « 3/2 » muette (3 − 1,5 sans les carrés, ou [BF] pris pour [FE]) : retrait conforme à la règle d'ambiguïté.
- **Q6 (écart de l'auteur).** Clé d par le cercle (ma suggestion) : AB = AC = AD = 6, donc B, C, D sur le cercle de
  centre A, [CD] diamètre — juste. Nouveau a « diamètre seul » : prémisses vraies (diamètre ; CAB = 60°), règle privée de
  « le troisième sommet est sur le cercle » → `condition-suffisante-supposee` exacte ; erreur plausible et classique.
  Plus de gabarit commun avec 29-Q4 (là : clé = réciproque de la médiane, d = « sommets sur un cercle »). Explication
  juste (elle redonne aussi la voie de la médiane). Indice faible résiduel : a et d énoncent le même théorème, d avec
  la condition de plus — même structure qu'avant correction (ancien a/d : médiane seule / médiane + AB = CD/2), non
  aggravée ; la plus longue est a (143 contre 128). À garder.
- **Q8.** Mes deux textes mot pour mot ; vote sans reconstruction (« E منتصف » a b d ; parallèle a c ; perpendiculaire
  a b ; F ∈ [BO] b c : a et b à égalité) ; b et c `condition-suffisante-supposee` exactes.
- **Q11.** Figure refaite comme demandé : [AI] tracé jusqu'à I seulement, K posé sur (CE), rien en vert. Vérifiée par
  coordonnées : ABC équilatéral (133,95), D = 2A − C, I milieu de [BD], E milieu de [AB], K = (CE) ∩ (AI) à
  x = 49,54 (A, I, K alignés). Reste K à l'échelle (AK = BC, tous deux horizontaux) : accepté à l'audit.
- Rendu Chromium `dir=rtl` 800/400 px : aucune unité mal ordonnée dans 30. Aucune explication ne livre la clé d'une
  question émise plus tard (EB = 3 et EC = 3√3 de Q2 ne sont les clés d'aucune question suivante).
- En-tête : 5 vraies d3 (Q8 à Q12), inchangées : d4 honnête.

**Verdict 30 : réserve mineure** (Q2, correctif facultatif ci-dessus ; rien de bloquant).

## Fichier 31 (11 questions, challenge d4 300/60, rampe 1, 2×6, 3×4 — ex-Q8 déplacée en Q11)

Appariement : Q1–Q7 = ex-Q1–Q7 ; Q8 = ex-Q9 (nature de EFC) ; Q9 = ex-Q10 (CM) ; Q10 = ex-Q11 (`multi` sur K) ;
Q11 = ex-Q8 (centre de gravité, passée de d2 à d3, énoncé refait).

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q3 (c étiquetée) | a (champs aveugles inchangés) | a | OK |
| Q4 (a et b réécrites) | d | d | OK |
| Q6 (`multi`, énoncés entremêlés) | {b, c, e, f} | {b, c, e, f} | OK |
| Q8 = ex-Q9 (c « حادّ الزوايا ومختلف الأضلاع », explication) | d | d | OK |
| Q10 = ex-Q11 (`multi` 3 vrais sur 6, figure sans K, explication) | {a, d, f} | {a, d, f} | OK |
| Q11 = ex-Q8 (centre de gravité, d3, déplacée, énoncé, figure, explication) | R (AR = 6) | c | OK |

- **Fuite levée.** Plus aucune prémisse « B منتصف [CK] » avant Q10 ; Q11 reconstruit K par Thalès dans KEC
  (KB/(KB + 3) = 1/2, KB = 3 = BC) puis le centre de gravité aux deux tiers de la médiane [AB] : AG = 6 (recalculé :
  G = ((0 + 9 + 9)/3 ; (0 + 3 − 3)/3) = (6 ; 0) = F). Ordre d'émission = ordre du fichier (rampe non décroissante) ;
  aucune explication émise avant Q11 ne donne sa clé (Q10 donne B milieu de [CK], maillon et non clé).
- **Q11, écart de l'auteur (options anonymes P/Q/R/B au lieu de « النقطة F » en clé).** Le motif de l'auteur se tient
  et l'écart est meilleur que mon texte : avec mes options, la clé « النقطة F » et le distracteur « النقطة B »
  formaient un groupe « points nommés » face à P et Q définis par une distance (une chance sur deux à la forme) ; ici
  trois options homogènes « النقطة X حيث AX = … » et B, l'intruse, est fausse. Longueurs 22/24/22/8 (clé non la plus
  longue). Étiquettes : a (AP = 3, tiers pris depuis le sommet) `centre-gravite-tiers-inverse` et b (AQ = 4,5, milieu
  de la médiane) `centre-gravite-milieu-mediane` exactes ; d muette. Seule perte : l'officiel demande de montrer que
  **F** est le centre de gravité, et l'explication ne le dit pas. Ajout facultatif, vérifié (Chromium `dir=rtl`
  800/400 px propre) : remplacer « 6 cm ✓، أي النقطة R. » par « 6 cm ✓، أي النقطة R، وهي النقطة F نفسها لأنّ AF = 6 cm. ».
- **Figure de Q11** (A, B, C, D, E, F, K, triangle ACK) vérifiée par coordonnées : 26,67 unités/cm, CE = 6, BF = 3,
  BK = 3 (K = (270 ; 195)), E, F, K alignés (pente 1) ; aucun codage du milieu B de [CK]. K y est à l'échelle (BK = BC
  se lit), mais Q11 vient après Q10 en quête ; au donjon seulement, mineur (même régime que l'audit).
- **Q10, écart de l'auteur (K retiré de la figure au lieu d'être « placé plus bas »).** L'auteur a raison et **mon
  correctif était faux** : K est l'intersection de (EF) et (BC) ; E et F étant à leur place, K placé plus bas ne serait
  plus aligné avec eux (figure fausse). Retirer K est la seule option juste ; l'élève prolonge (EF) lui-même. Figure
  vérifiée (27,11 unités/cm ; E à CE = 6, F à BF = 3 ; codages AF = CE et BF = BC aux milieux des segments). Énoncés :
  (FB) ∥ (EC) ✓, K milieu de [BC] ✗, KC = 4,5 ✗ (KC = 6), B milieu de [CK] ✓, KB = 1,5 ✗, KB = 3 ✓ — 3 vrais sur 6,
  gabarit désormais distinct de Q6 (4 sur 6). Explication juste ; « KC = KB + BC = 3 + 3 = 6 cm » s'ouvre sur des
  lettres et se lit gauche-à-droite (l'ancien « 3 + 3 = 6 cm » inversé a disparu).
- **Q4.** Mes deux textes mot pour mot (AF = 6 = 2 × BF vrai ; E ∈ [CD] vrai). Plan 2×2 (égaux × parallèles) avec c
  hors plan ; chaque option à deux prémisses : le compte de conditions ne désigne plus la clé. Étiquettes inchangées,
  exactes.
- **Q6.** Énoncés jugés un à un (H = (6 ; 3), E = (3 ; 3), C = (9 ; 3)) : H milieu de [CD] ✗ (4,5), HC = 3 ✓, EC = 6 ✓,
  HC = 6 ✗, H milieu de [EC] ✓, EH = 3 ✓. L'explication décrit les énoncés par leur contenu, pas par leur lettre :
  elle reste juste après le réordonnancement.
- **Q8.** Plan 2×2 complet (droit/aigu × isocèle/scalène) : chaque terme dans deux options ; c ✗✗ muette. Phrase
  ajoutée juste (FE = FC = 3√2, EC = 6).
- **Q3.** c `condition-suffisante-supposee` : règle du triangle rectangle isocèle privée de « isocèle » — exacte.
- Rendu Chromium `dir=rtl` 800/400 px : aucune unité mal ordonnée dans 31.
- **En-tête (point c).** 4 vraies d3 : Q8 (médiatrice puis réciproque de la médiane), Q9 (Pythagore puis rapport),
  Q10 (Thalès + équation, six énoncés), Q11 (Thalès + équation puis deux tiers de la médiane) ; d1/d2 directs. Seuil
  de 4 retenu aux lots précédents et profil des d4 publiés (04/28 : 4 d3 sur 11) : **challenge d4 honnête**.

**Verdict 31 : OK** (un ajout facultatif à l'explication de Q11).

## Fichier 32 (11 questions, challenge d4 300/60, rampe 2×5 puis 3×6 — inchangés)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (a étiquetée) | 6√2 (champs aveugles inchangés) | b | OK |
| Q3 (`multi`, énoncés entremêlés) | {a, c, d, f} | {a, c, d, f} | OK |
| Q4 (d étiquetée) | a | a | OK |
| Q6 (a, b, c réécrites, étiquettes, explication) | d | d | **défaut (de MON correctif) : vote par case** |
| Q7 (d étiquetée) | 2√5 | c | OK |
| Q8, Q9 (figures sans H ; 12 et 18 muets en Q9) | d · 9 | d · b | OK (résidu accepté) |
| Q10 (rappel, b de l'auteur, c d les miennes, explication) | a | a | **défaut : vote par case + c, d fausses à l'œil** |
| Q11 (rappel entre parenthèses) | c | c | OK · remarque |

Valeurs recalculées (Fraction, A(0 ; 0), B(6 ; 0), C(6 ; 6), D(0 ; 6)) : K = (9/2 ; 3/2) sur le cercle de diamètre [BI] et
sur (BD) ; IK·BD = 0, AC·BD = 0, DC·BI = 0, IK·DI = −9/2, DC·DB = 36 ; H = (9 ; 6) sur (DC) et (IK) ; J = (4 ; 4).

- **Q6 — défaut que j'ai moi-même introduit (même mécanisme que celui que j'ai relevé en 34-Q2 à l'audit).** Mes trois
  textes sont appliqués mot pour mot ; chacun a des prémisses vraies et une inférence fausse. Mais l'argument a deux
  cases (ce qui est dit de (IK), ce qui est dit de (AC)) : la justification juste de chaque case figure deux fois
  (a + d, b + d) et chaque fausse une seule (« (AC) يقطع (BD) في المركز O » en a, « (IK) يقطع (BD) في K » en b ; c
  hors patron) — le vote par case reconstruit d, exactement le constat « plan 2×2 incomplet » de 34-Q2. Correctif
  (vérifié : chaque valeur de case deux fois ; prémisses vraies ; longueurs a 131 · b 118 · c 146 · d 103, clé non la
  plus longue ; Chromium `dir=rtl` 800/400 px propre) — c devient la case ✗✗ du même patron, muette :
  - c → « (IK) يقطع (BD) في K لأنّ K من الدائرة ومن المستقيم (BD) معًا، و (AC) يقطع (BD) في المركز O لأنّ قطرَي المربّع يتقاطعان في منتصفيهما، فهما متوازيان » (retirer `condition-suffisante-supposee`) ;
  - explication : remplacer « ؛ أو تطبيق خاصيّة المنتصفين بمنتصف واحد: K في هذه الحجّة نقطة من [BO] فقط، والخاصيّة تشترط منتصفَي ضلعين. » par « ؛ أو الاكتفاء بأنّ كلًّا من المستقيمين يقطع (BD)، وهذا لا يثبت توازيهما. ».
  Perte assumée : le piège « خاصيّة المنتصفين بمنتصف واحد » quitte Q6 ; la tranche le garde en 30-Q8 d (propriété
  directe avec un seul milieu) et, sous sa forme réciproque, en 32-Q5 b.
- **Q6, point (b) — `condition-suffisante-supposee` sur a, b, c (contre la consigne initiale de laisser a et b
  muettes).** La consigne visait les ANCIENS textes (règle vraie dans la figure, raisonnement valide non justifié) ;
  sur les nouveaux, le libellé `origin/main` (« Tu prends une seule propriété pour une preuve : il faut toutes les
  conditions ») nomme exactement l'erreur de chacune : a et b établissent UNE des deux perpendicularités à (BD) et
  mettent un fait vrai mais hors sujet à la place de l'autre ; c applique la propriété des milieux avec un seul milieu.
  Les trois sont donc exactes — **aucune à retirer** ; avec le correctif ci-dessus, a et b gardent l'étiquette, la
  nouvelle c (aucune des deux conditions) est muette.
- **Q10 — écart de l'auteur (point a) et faiblesse résiduelle (point d).** Mon jeu b/c/d mettait « (IK) ⊥ (BD) » dans
  trois options sur quatre : **défaut de mon correctif**, bien vu. Le b de l'auteur (« يمرّ من الرأس », prémisses
  vraies, `condition-suffisante-supposee` exacte) ramène ce compte à deux, mais le plan reste incomplet : par case,
  la valeur juste figure deux fois (« (DC) عمودي على (BI) » a, c ; « (IK) عمودي على (BD) » a, d) et chaque fausse une
  seule (b, c, d ont trois fausses différentes) → le vote par case reconstruit a. S'y ajoute (d) : c « (IK) ⊥ (DI) »
  (angle ≈ 108° sur la figure) et d « (DC) ⊥ (DB) » (45°) se réfutent à l'œil. **Pas acceptable en l'état.** Correctif
  (vérifié : chaque valeur de case deux fois ; toutes les prémisses vraies, donc plus rien de faux à l'œil ; longueurs
  103/105/104/104 ; Chromium `dir=rtl` 800/400 px propre) — plan 2×2 complet sur la valeur fausse que l'auteur a
  choisie pour b :
  - c → « (DC) عمودي على (BI) فهو ارتفاع صادر من D، و (IK) يمرّ من الرأس I فهو ارتفاع صادر من I، و H نقطة تقاطعهما » (`condition-suffisante-supposee`, au lieu de `segment-mal-choisi`) ;
  - d → « (DC) يمرّ من الرأس D فهو ارتفاع صادر من D، و (IK) عمودي على (BD) فهو ارتفاع صادر من I، و H نقطة تقاطعهما » (`condition-suffisante-supposee`, au lieu de `segment-mal-choisi`) ;
  - b inchangée (même erreur répétée : l'étiquette reste exacte, comme 29-Q11 a/d) ;
  - explication : remplacer tout le passage à partir de « الخطأ الشائع: » par « الخطأ الشائع: الاكتفاء بأنّ المستقيم يمرّ من رأس لاعتباره ارتفاعًا صادرًا منه، ولو لأحد المستقيمين فقط: فالارتفاع يمرّ من الرأس ويكون عموديًّا على حامل الضلع المقابل له، ويلزم إثبات ذلك لكلٍّ من (DC) و (IK). ».
  Le rappel « نذكّر بأنّ ارتفاعات أيّ مثلّث تلتقي في نقطة واحدة… » est juste et ne livre plus la clé (toutes les
  options parlent de deux hauteurs).
- **Q8, Q9 (figures, écart de l'auteur).** H n'est plus dessiné : DH = 1,5 × DC (clé 9 de Q9) ne se lit plus. Le petit
  segment vert part de I (215,17 ; 115) vers (254,83 ; 75,33), direction (1 ; −1) parallèle à (AC) — vérifié — et sort
  du carré à droite de C : l'axe « position » de Q8 (H au-delà de C) se devine en le prolongeant, résidu déjà accepté
  à l'audit (et la position se déduit sans figure). Figures vraies (J aux 2/3 de [DI] et sur (AC)). Q10 et Q11, émises
  après, montrent H à l'échelle : donjon seulement, mineur.
- **Q11.** Rappel « (نقطة تلاقي ارتفاعاته الثلاثة) » posé. Effet de bord de MON correctif, mineur : b (« الموسّطات الثلاثة
  تتلاقى في H ») contredit maintenant l'énoncé et s'écarte à la lecture ; le rappel reste nécessaire (orthocentre non
  enseigné), à accepter.
- **Étiquettes posées.** Q1 a « 3√2 » = OA → `segment-mal-choisi` exacte (l'explication le nomme) ; Q4 d (angle droit en
  B) → `hypotenuse-mal-choisie`, même lecture que 30-Q2 ; Q7 d « 3√5 » = la médiane DI entière →
  `alg.reponse-a-l-autre-inconnue` (« …ou un résultat intermédiaire ») exacte ; Q9 c, d (12 et 18, deux gestes chacun)
  muettes : retrait conforme.
- **Q3.** Énoncés jugés un à un : [DI] médiane ✓, J milieu de [DI] ✗ (milieu (3 ; 4,5)), [CO] médiane ✓, J intersection
  des deux ✓, J centre du carré ✗, J centre de gravité ✓ ; l'explication parle des énoncés par leur contenu.
- **Correction de mon audit (préexistant, non introduit).** J'avais rangé 32-Q5 parmi les modèles : à tort. Le
  triangle « BOC » figure dans a, b, c et « BCD » dans d seule (d s'écarte au vote), puis a est la réunion de b
  (milieu) et c (parallèle). Mineur, hors du périmètre des correctifs ; à reprendre avec le prochain passage sur la
  mission si le déposant le souhaite.
- Rendu Chromium `dir=rtl` 800/400 px : aucune unité mal ordonnée dans 32.
- En-tête : 6 vraies d3 (Q6 à Q11), inchangées : d4 honnête.

**Verdict 32 : défaut à corriger** (Q6 et Q10, textes ci-dessus).

## Fichier 33 (8 questions, PASSÉ en boss d3 120/30, titre ⭐⭐⭐, rampe 1, 2×4, 3×3 — aire déplacée en Q8)

Appariement : Q1–Q5 = ex-Q1–Q5 ; Q6 = ex-Q7 (OI par la tangente de 30°) ; Q7 = ex-Q8 (losange) ; Q8 = ex-Q6 (aire,
passée de d2 à d3, énoncé refait). Valeurs recalculées (O(0 ; 0), B(−3 ; 0), C(3 ; 0)) : A(−3/2 ; 3√3/2),
E(−3 ; 3√3), D(3/2 ; −3√3/2), I(0 ; −√3), J(0 ; √3) ; EB = 3√3, OI = √3, IJ = 2√3, aire = 6√3.

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (b, c : seconde prémisse vraie) | a | a | OK |
| Q2 (rappel « عمودي على (OB) », angle droit codé) | 30 | 30 | OK |
| Q4 (a, b : seconde prémisse vraie) | c | c | OK |
| Q5 (rappel, angle droit codé ; « 3 » muet) | 3√3 | c | OK |
| Q6 = ex-Q7 (explication sans « ظا 30° = OI/OB ») | √3 | b | OK |
| Q7 = ex-Q8 (b, c réécrites, étiquettes, explication) | d | d | OK · réserve mineure |
| Q8 = ex-Q6 (aire en d3, OI à calculer, déplacée) | 6√3 | b | OK |
| en-tête boss d3 120/30, ⭐⭐⭐ | — | — | OK |

- **Fuite levée.** « OI = √3 » n'est plus donné : Q8 enchaîne angle OBD = 30°, tangente, IJ = 2 × OI, aire — vraie d3,
  après Q6 et Q7 ; sa prémisse « CIBJ معيّن مركزه O » est la clé de Q7, émise avant (convention des prémisses). Aucune
  explication émise avant une question ne donne sa clé (EB = 3√3 de Q5 n'est que la valeur d'un distracteur en Q6/Q8 ;
  IJ = 2√3 dans l'explication de Q7 suit Q6, qui donne déjà OI).
- **Q1, Q4.** Mes textes mot pour mot ; prémisses vraies. Pas de point de convergence : en Q1, b et c partagent la règle
  fausse « فللمثلّث OAB ضلعان متقايسان على الأقلّ، إذن هو متقايس الأضلاع », a partage un fait avec chacune ; en Q4, a et
  b partagent « فالنقطة A تبعد عن … مسافة 3 cm، إذن A منتصف [OE] ». Longueurs : Q1 110/137/126/97, Q4 137/124/130/151
  (clés non les plus longues). Étiquettes `condition-suffisante-supposee` exactes (une des deux égalités manque).
- **Q2, Q5.** Rappel « وهو عمودي على (OB) » posé ; angle droit codé en B sur les deux figures (vérifié : (BE) verticale,
  (BO) horizontale) ; il ne livre que l'angle de 90°, pas les clés 30 et 3√3. Q5 « 3 » muet (6 − 3 sans carrés, ou
  OB, ou AB) : retrait conforme ; « 3√2 » `segment-mal-choisi` et « 3√5 » `hypotenuse-mal-choisie` exactes.
- **Q6.** Mon texte appliqué (l'auteur aurait pu garder l'ancien depuis #1160, le mien reste juste). Rendu : « OI = OB ×
  √3/3 = 3 × √3/3 = √3 cm » gauche-à-droite. Note moteur, préexistante et voulue : dans la même phrase d'erreurs,
  « ظا 60° = √3 » et « جتا 30° = √3/2 » sont isolées (radical) mais « جا 30° = 1/2 », sans lettre ni radical, reste en
  arithmétique droite-à-gauche (« 1/2 = °30 » à l'écran, lu juste de droite à gauche). Pas un défaut de contenu.
  Options a « 3/2 » et c « 3√3/2 » muettes en attendant `math.geo.fonction-trigo-mal-choisie` (voir Étiquettes) ;
  d « 3√3 » `valeurs-remarquables-confondues` exacte (tan 60° pris pour tan 30°).
- **Q7 (losange), réserve mineure sur MON correctif.** b (milieu commun seul, `condition-suffisante-supposee`) et c
  (« مربّع », `description-la-plus-precise-manquee`) sont mes textes, exacts et plus d'option à prémisse fausse. Mais c et d
  reprennent mot pour mot les deux justifications (chacune présente dans 3 options sur 4) : le vote ramène à {c, d},
  puis « مربّع » se réfute sur la figure (IJ = 2√3 ≈ 3,5 contre BC = 6). C'est le régime ordinaire du piège « carré »
  sur figure exacte (même cas que 30-Q12 d), et c'est mieux qu'avant (deux options à prémisse fausse visible) ; à
  garder. Une refonte sans indice demanderait le modèle de 30-Q9 (mêmes affirmations partout, seules les raisons
  changent) : non exigée.
- **Q8.** Explication de l'auteur juste ; « 8√3 » (périmètre) `aire-et-perimetre-confondus` et « 12√3 » (sans moitié)
  `aire-losange-sans-moitie` exactes ; « 3√3 » (demi-diagonales) muette comme avant. Figure inchangée et vraie
  (IJ/BC = 110,22/190,9 = 1/√3).
- **Q3 facultative écartée (point a).** AEB = 30° aurait eu la clé de Q2 et une paire à 0,95 : bonne décision ; BAE = 120°
  reste (Q3 n'a pas besoin du rappel de la tangente).
- **En-tête (point c).** 3 vraies d3 sur 8 (Q6 tangente après deux déductions d'angles, Q7 symétrie centrale + critère,
  Q8 chaîne complète) ; rampe 1, 2, 2, 2, 2, 3, 3, 3 non décroissante ; boss d3 120/30 et ⭐⭐⭐ : honnête.
- Rendu Chromium `dir=rtl` 800/400 px : seul signal du détecteur, « CI² = 3² + (√3)² = 12) » (explication de Q8) —
  parenthèse fermante d'une incise ouverte plus tôt, à sa place à l'écran (faux positif déjà jugé à l'audit).

**Verdict 33 : OK** (réserve mineure sur Q7, sans correctif exigé).

## Fichier 34 (9 questions, PASSÉ en boss d3 120/30, titre ⭐⭐⭐, rampe 2×6, 3×3 — périmètre déplacé en Q9)

Appariement : Q1–Q6 = ex-Q1–Q6 ; Q7 = ex-Q8 (orthocentre) ; Q8 = ex-Q9 (x = AI, figure ajoutée) ; Q9 = ex-Q7
(périmètre, passé de d2 à d3, « AI = 3 cm » retiré). Valeurs recalculées (A(0 ; 0), B(8 ; 0), D(0 ; 4)) : I(3 ; 0),
J(5 ; 4), K(0 ; −6) ; DI = IB = BJ = JD = 5 ; périmètre 20 ; I = (BA) ∩ (KI) orthocentre de KBD.

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (a : « ومن الضلع [AB] ») | c | c | OK · note préexistante |
| Q2 (c = case ✗✗ du même patron, explication) | d | d | OK |
| Q7 = ex-Q8 (rappel de l'orthocentre) | b | b | OK |
| Q8 = ex-Q9 (figure ajoutée, I en position générique) | 3 | 3 | OK |
| Q9 = ex-Q7 (périmètre en d3, déplacé, explication) | 20 | 20 | OK |
| en-tête boss d3 120/30, ⭐⭐⭐ | — | — | OK |

- **Fuite levée.** Plus aucune longueur donnée avant Q8 ; Q9 refait l'étape officielle 3b complète (équation puis
  4 × IB), émise après Q8 ; sa prémisse « DIBJ معيّن » est la clé de Q3, émise avant. Aucune explication antérieure ne
  livre 3 ou 20.
- **Q2.** Mon texte de case ✗✗ appliqué : chaque justification (juste ou fausse) figure exactement deux fois — vote
  neutralisé ; longueurs 146/171/161/157 ; c muette ; phrase d'explication « أو الجمع بين التعليلين الناقصين » posée.
- **Q1.** Mon ajout appliqué (prémisse vraie). Note préexistante (non introduite, mineure) : la formule de conclusion
  « فهي تبعد عن D وعن B المسافة نفسها، إذن ID = IB » est commune à a, b, d et absente de la clé (qui conclut par « فالمستقيم
  (OI) هو الموسّط العمودي للقطعة [BD] والنقطة I منه ») : la clé est l'intruse de forme. Pas de point de convergence par ailleurs ; à garder.
- **Q7.** Rappel posé ; il ne contredit aucune option (c et d s'appuient sur une seule hauteur). Plan : (BA) ⊥ (KD) en
  b, d ; (KI) ⊥ (BD) en b, c ; c et d partagent leur conclusion fausse — pas de point de convergence. Étiquettes
  inchangées et exactes.
- **Q8.** Figure = celle de Q4 (même empreinte) : rectangle et I sur [AB] à AI = 2,5, sans tracer DIB — schéma d'une
  inconnue, il ne contredit rien de dessiné et ne livre pas 3. Correction de mon audit : les figures de Q4–Q5 plaçaient
  déjà I à 2,5 (et non à 3 comme je l'avais écrit) ; seules celles de Q1–Q3, Q7 et Q9 le placent à 3.
- **Q9, faiblesse résiduelle (point d).** La figure trace le losange vrai (I à 3, IB = 145 sur AB = 232 unités) :
  IB/AB ≈ 0,62 s'estime à l'œil, d'où 5 puis 20. **Acceptable** : un I générique ferait un losange faux (DI ≠ IB) ;
  l'estimation à l'œil d'une valeur `numeric` exacte n'est pas fiable sans graduation ; en quête, Q8 vient de donner
  x = 3. Pas de correctif.
- **En-tête (point c).** 3 vraies d3 sur 9 (Q7 hauteurs, Q8 mise en équation, Q9 chaîne équation + périmètre) ; rampe
  non décroissante ; boss d3 120/30 et ⭐⭐⭐ : honnête.
- Rendu Chromium `dir=rtl` 800/400 px : aucune unité mal ordonnée dans 34.

**Verdict 34 : OK.**

## Fichier 35 (11 questions, challenge d4 300/60, rampe 1, 2×5, 3×5 — HE déplacée en Q9)

Appariement : Q1–Q6 = ex-Q1–Q6 ; Q7 = ex-Q8 (papillon) ; Q8 = ex-Q9 (HJ) ; Q9 = ex-Q7 (HE, passée de d2 à d3,
« HJ = 0,7 » retiré) ; Q10, Q11 inchangées de place. Valeurs recalculées (A(0 ; 0), B(4 ; 0), C(0 ; 3)) : AH = 12/5,
H(1,44 ; 1,92), BH = 3,2, CH = 1,8, I(2 ; 0), J(2 ; 1,5), HJ = 0,7, E(0 ; 48/7), HE = 36/7, K(2 ; −1,5).

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q3 (options 0,6 / 1,8 / 3,2 / 3,24, explication sans relation non enseignée) | 1,8 | a | OK |
| Q4 (« 1,8 » muet ; « 1,5 » retiré de l'explication) | 2 | d | OK |
| Q5 (« BC/2 = 2,5 » retiré de l'explication) | 1,5 | d | OK |
| Q8 = ex-Q9 (BH par Pythagore dans AHB) | 0,7 | c | OK |
| Q9 = ex-Q7 (HE en d3, HJ à calculer, déplacée) | 36/7 | b | OK |
| Q10 (`multi` : « AKBJ معيّن » vrai, 5 vrais sur 6, énoncés entremêlés) | {a, b, c, e, f} | {a, b, c, e, f} | OK |

- **Fuite levée.** Q9 ne donne plus HJ : BH = 5 − 1,8, BJ = 2,5, J entre B et H, HJ = 0,7, puis HE = 2 × 1,8/0,7 = 36/7
  (vérifié aussi par coordonnées) ; émise après Q8. Balayage des fuites en avant (clé d'une question émise plus tard
  retrouvée comme jeton dans un énoncé ou une explication plus tôt) : celles de l'audit ont disparu (33 « √3 », 34 « 3 »,
  35 « 0,7 », et les deux nettoyages de l'auteur en 35, « 1,5 » en Q4 et « 2,5 » en Q5, sont justes) ; il ne reste
  que des coïncidences inhérentes déjà connues (60°, 4√3, côté 6, 3, 9) ; la seule nouveauté est « 6 cm » dans les
  énoncés de 30-Q2/Q3 (le côté, que j'ai fait ajouter ; égal par construction à la clé AK = 6 de 30-Q11) — sans effet.
- **Q3.** Mon jeu appliqué : 0,6 = 3 − 2,4 `pythagore-sans-carres`, 3,2 = BH `segment-mal-choisi`, 3,24 = CH²
  `pythagore-racine-oubliee` — exactes ; aucune option somme ou différence de deux autres ; longueurs 3/3/3/4.
  Explication juste (9 − 5,76 = 3,24) ; AH × BC = AB × AC est la relation des aires déjà employée en Q2 (émise avant).
- **Q8 = ex-Q9.** 16 − 5,76 = 10,24, BH = 3,2 ; étiquettes inchangées et exactes (5,7 position, 1,8 et 3,2 segments).
- **Q9 = ex-Q7.** 7/9 (rapport inversé), 18/7 (arrêt à HC/HJ, `alg.reponse-a-l-autre-inconnue`), 31/10 (différences)
  restent exactes avec HJ calculé ; longueurs 3/4/4/5.
- **Q10.** Énoncés jugés un à un : I milieu de [KJ] ✓, (KJ) ⊥ (AB) ✓, AK = BJ = 2,5 ✓, KJ = AB ✗ (3 contre 4),
  JA = JB ✓, AKBJ losange ✓ (quatre côtés 2,5). Explication réécrite juste ; gabarit désormais distinct (5 vrais sur 6).
  La prémisse « AKBJ معيّن » de Q11 suit Q10.
- Rendu Chromium `dir=rtl` 800/400 px : aucune unité mal ordonnée dans 35 (« AH = 2,4 cm (AH × BC = AB × AC) » se lit
  dans l'ordre).
- **En-tête (point c).** 5 vraies d3 (Q7 papillon, Q8 position + Pythagore, Q9 chaîne HJ puis rapport, Q10 six
  énoncés, Q11 aire avec diagonale à construire) : d4 honnête.

**Verdict 35 : OK.**

## Étiquettes (points b et e)

- **Décompte relu** (sept fichiers tels quels) : 60 `mcq`, 9 `numeric`, 4 `multi` = 73 ; 180 distracteurs, 139 étiquetés,
  41 muets ; 27 étiquettes distinctes, toutes au registre `origin/main` ; aucune clé étiquetée ; aucune étiquette sur
  une `multi`. Avec mes correctifs : 32-Q6 c muette (−1), 32-Q10 c, d passent de `segment-mal-choisi` à
  `condition-suffisante-supposee`, 30-Q2 b muette si le facultatif est pris (−1), 33-Q6 a, c étiquetées (+2) à la
  livraison de l'étiquette neuve.
- **Retraits vérifiés, tous à bon droit** : 29-Q8 c (✗✗), 30-Q4 a (deux gestes), 33-Q5 a (trois gestes), 32-Q9 c et d
  (deux gestes chacune), 35-Q4 b (valeur de remplissage).
- **Poses vérifiées, toutes exactes** : 29-Q4 d, 31-Q3 c `condition-suffisante-supposee` ; 30-Q2 b, c et 32-Q4 d
  `hypotenuse-mal-choisie` (angle droit au mauvais sommet) ; 32-Q7 d `alg.reponse-a-l-autre-inconnue` (résultat
  intermédiaire) ; 32-Q1 a `segment-mal-choisi` — le « un peu large » de l'auteur tient au libellé, générique par
  construction (« Tu prends dans la figure un autre segment que celui que demande la propriété ») ; « 3√2 » est
  exactement le segment [OA] de la figure rendu à la place de [AC] : exacte. Poses nouvelles relues dans les sections
  par fichier (30-Q6 a, 31-Q11 a b, 32-Q6 a b c, 33-Q7 b c, 35-Q3 b c d) : exactes.
- **Étiquette neuve `math.geo.fonction-trigo-mal-choisie`** (`pending-tags/L16.json`). Libellés fr/en/ar relus :
  l'ajout « trigonométrique / trigonometric / المثلّثية » aligne sur `trigo-rapport-inverse` (« النسبة المثلّثية ») ;
  « الجيب وجيب التمام » et « الظلّ » sont les termes du registre et de la compétence `math.geo.trigonometrie` (présente
  dans `content/competences/math.json` de `origin/main`). Le libellé nomme l'erreur dans les deux sens (deux côtés de
  l'angle droit → tangente ; sinus et cosinus → hypoténuse) : exact. Placements relus sur `origin/main` :
  - **33-Q6 a « 3/2 »** = OB × sin 30° et **c « 3√3/2 »** = OB × cos 30°, là où OI (opposé) et OB (adjacent) appellent la
    tangente : exacts.
  - **09/03-Q6 a « 1/2 »** (on demande ظا(A), AB adjacent, BC opposé) : AB/AC = cos A, que l'explication publiée nomme
    (« الخلط مع جتا(A) … = 1/2 ») : exact.
  - **09/06-Q1 — à corriger dans le dossier en attente (et l'erreur vient de MON audit).** On demande جتا(∠ABC), angle
    droit en A, AB = 5, AC = 12, BC = 13. « 12/5 » (d) = AC/AB = **tan B exactement** : c'est d qui exécute l'erreur de
    l'étiquette neuve (tangente au lieu du cosinus). « 5/12 » (c) = AB/AC **n'est pas** tan B ; le seul geste simple qui
    y mène est de prendre [AC], le plus long des deux côtés donnés, pour hypoténuse dans « adjacent/hypoténuse » →
    `math.geo.hypotenuse-mal-choisie` exacte. `trigo-rapport-inverse` est inexacte sur les deux (ni 5/12 ni 12/5 n'est
    l'inverse de 5/13). Donc : **c → `math.geo.hypotenuse-mal-choisie`, d → `math.geo.fonction-trigo-mal-choisie`** (et non
    « c → étiquette neuve »). L'explication publiée est fausse au même endroit (« ظا = AB/AC ») ; remplacement vérifié
    (valeurs par Fraction ; Chromium `dir=rtl` 800/400 px : la partie modifiée se lit dans l'ordre — j'ai écrit les
    fonctions en toutes lettres pour ne pas coller « ظا(B) » à une formule latine) : remplacer
    « أو حساب ظا = AB/AC = 5/12؛ أو قلب النسبة (12/5). » par
    « أو اعتبار [AC] وترًا لأنّه أطول الضلعين المعطيين فنجد AB/AC = 5/12؛ أو حساب ظلّ الزاوية B بدل جيب تمامها، أي AC/AB = 12/5. ».
    (Hors correctif : le début publié « جتا(B) = المجاور/الوتر = AB/BC = 5/13. ✓ (5-12-13 …) » mêle mots arabes et formule
    latine ; il se lit dans l'ordre mais mal coupé à l'écran — préexistant, à signaler seulement.)
  - **09/06-Q6 b « نعم، جتا = المقابل/المجاور »** : c'est la définition de la tangente donnée pour le cosinus → étiquette
    neuve exacte ; `cosinus-sinus-confondus` y était inexacte ; d (« لا خطأ ») la garde à bon droit.
  - **Seuil** : 4 questions distinctes (33-Q6, 09/03-Q6, 09/06-Q1, 09/06-Q6) ≥ 3 — franchi, quel que soit le choix c/d.
  - Livraison : l'entrée au registre DANS LE MÊME commit que les placements. Vérifié sur la copie de travail (registre
    + les cinq placements corrigés + tous mes correctifs) : `content:check` vert (856 étiquettes), `content:qa --strict`
    0 erreur, `content:tranche --changed --fresh` inchangé (0/60, 0 paire).

## Gates (point f, lecture seule)

Copie de travail : corpus `origin/main` 18c8a7ac (dépôt git local, base) + les sept fichiers non suivis ; moteur
`origin/main` bffcca85 (node_modules de l'arène). Rien d'écrit dans le dépôt partagé.

- `content:check` : vert — 120 matières, 4 684 exercices, 28 423 questions ; math 20 chapitres, 310 exercices, 2 126
  questions ; 855 étiquettes.
- `content:qa --strict --subject math` : 0 erreur ; 18 avertissements, aucun sur 29–35 (lettres d'options citées dans
  des explications publiées ailleurs, et la longueur d'une section du cours ch.18, préexistante).
- `content:tranche --changed --fresh --base` (base = `origin/main`) : 73 questions neuves ; clé strictement la plus longue
  **0/60** ; positions de clé a 14 · b 15 · c 18 · d 13 ; paires proches **0** ; candidats gabarit 0. Sans `--fresh`
  (ch.18 entier) : 8/220 clés les plus longues, toutes dans des missions publiées (01–06, quiz) ; 2 paires proches
  préexistantes (01↔03, 03↔05), aucune ne touche 29–35.
- Jaccard de surface (ma mesure, figures ignorées) : maximum 0,57 contre le publié (35-Q2 ~ 27-Q1 : même cadre « ABC
  قائم في A », autres données, autre tâche) ; en interne, jusqu'à 0,85 entre questions d'un même problème (33-Q2 ~ Q3 :
  mêmes données, angles différents), attendu pour un sujet d'examen découpé ; la gate écarte à raison les paires à
  figures différentes.
- `check-figures` : OK sur ch.18 ; `check-overflow` (Chromium, calibration passée) : aucun texte hors `viewBox` sur 241
  figures.
- Rouge attendu à la livraison : `content:catalogue` (CATALOGUE.md à committer).

## Chiffre final

73 questions relues ; 48 re-résolues à l'aveugle avant lecture de la clé (toutes les questions touchées) ; **0 clé
fausse** ; 0 figure fausse (8 figures retouchées ou ajoutées — 30-Q11, 31-Q10, 31-Q11, 32-Q8, 32-Q9, 33-Q2, 33-Q5,
34-Q8 — vérifiées par coordonnées) ; rendu Chromium `dir=rtl`
propre sur les sept fichiers ; les quatre fuites en avant de l'audit sont levées, aucune nouvelle.

- **À corriger (2 questions, défauts introduits par les correctifs)** : 32-Q6 (mon correctif : vote par case, plan
  2×2 incomplet) et 32-Q10 (mon c/d + le b de l'auteur : vote par case, et c, d fausses à l'œil) — textes vérifiés en
  section 32.
- **Dossier d'étiquettes en attente à amender** : 09/06-Q1 — c → `hypotenuse-mal-choisie`, d → étiquette neuve, et
  l'explication publiée (texte vérifié ci-dessus).
- **Réserves mineures, sans blocage** : 30-Q2 (correctif facultatif vérifié), 30-Q6 (paire « même théorème », à garder),
  31-Q11 (ajout facultatif à l'explication), 32-Q11 (b contredit par le rappel, à garder), 33-Q7 (vote ramené à {c, d},
  à garder), 34-Q1 (formule de conclusion intruse, préexistante), 34-Q9 (losange à l'échelle, acceptable) ; cosmétique :
  ordre des options de 29-Q10.
- **Écarts de l'auteur jugés** : tous fondés — 31-Q11 options anonymes (meilleures que les miennes), 31-Q10 et 32-Q8/Q9
  points retirés (mon « K plus bas » donnait une figure fausse), 30-Q2 dérivation juste, 30-Q6 « diamètre seul » exact,
  33-Q3 facultative écartée à raison, 32-Q6 étiquettes exactes ; seul 32-Q10 b ne suffit pas (le plan reste incomplet).
- **Mes erreurs d'audit reconnues** : 32-Q10 (« (IK) ⊥ (BD) » trois fois), 32-Q6 (plan incomplet que j'avais pourtant
  relevé en 34-Q2), 31-Q10 (« K plus bas »), 09/06-Q1 (« 5/12 = tan » : c'est 12/5), 32-Q5 rangée à tort parmi les
  modèles, figures de 34-Q4/Q5 mal décrites.

**Verdicts** : 29 OK · 30 réserve mineure · 31 OK · 32 **défaut à corriger** · 33 OK (réserve mineure) · 34 OK · 35 OK.
Livrable après les deux correctifs de 32 et l'amendement du dossier d'étiquettes (09/06-Q1).
