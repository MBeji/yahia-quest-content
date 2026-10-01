# Audit à l'aveugle — tranche L13 (math 9ᵉ, ch.09, NN 30–35, sujets officiels)

> **v2 — rapport complet** (la v1 était la sauvegarde de reprise). Arbre de travail tel quel le 2026-10-01 ; les six fichiers n'ont pas bougé pendant l'audit (md5 identiques à la lecture et à la fin). Moteur lu sur `origin/main` arena a7f041f8 (bidi #1137→#1145 inclus). Aucun fichier du dépôt modifié : les correctifs ont été appliqués à des COPIES hors dépôt pour être vérifiés.

## Méthode
- Chaque question re-résolue À L'AVEUGLE (énoncé + options seuls : clé, explication et étiquettes masquées), réponse notée AVANT lecture de la clé ; recalcul par script (`Fraction`, sympy : repère de 35 reconstruit — A(0;0) B(3;0) C(0;4) E(−2;0) F(8;0) K(4;2) H(0;−6) G(2;−2), identique à celui de l'auteur ; H = orthocentre de BCF et G = centre de gravité de HEF vérifiés).
- Transcriptions officielles lues : 2010-tech ex.3, 2012-tech ex.3, 2015-tech ex.3, 2024-tech ex.3, 2026-tech ex.3, 2002 ex.4.
- Figures : coordonnées extraites et contrôlées (alignements, parallèles, angles droits, proportions, étiquettes), rendues en Chromium ; `check-figures` ✓ ; `check-overflow` (calibré) ✓ 31 figures, 0 texte hors viewBox.
- Rendu arabe : `splitMathRuns` / `isDisplayEquation` d'`origin/main` + contrôle PROGRAMMATIQUE de l'ordre visuel de chaque formule (1 193 segments) en Chromium `dir=rtl`, à 760 px et 340 px.
- Gates lus : `content:check` ✓ ; `content:qa` 0 erreur, aucun avertissement sur 30–35 ; `content:tranche` (ch.09) : clé strictement la plus longue 0/48, aucune paire proche ≥ 0,45 impliquant 30–35 ; balayage notation (chiffres indo-arabes, espace simple entre groupes, LaTeX, `$`, radicande arabe, virgule arabe entre crochets, tiret ASCII) : 0.
- Registres lus sur `origin/main` (`misconceptions.json`, `competences/math.json`) ; cours lus : ch.08, ch.09, ch.12 (9ᵉ) et math-6eme/7eme/8eme pour l'échelle, la médiane, la hauteur, la symétrie centrale, la propriété des perpendiculaires.

## Chiffre final
**48 questions auditées · 0 clé fausse (48/48 = ma réponse aveugle) · 0 défaut critique · 13 majeurs · 17 mineurs · 32 questions touchées par les correctifs : 19 à réécrire (énoncé, option, explication ou figure : 30 Q1 ; 31 Q4, Q7, Q8 ; 32 Q3, Q7, Q8 ; 33 Q3, Q4, Q5, Q6 ; 34 Q1, Q2, Q3, Q7 ; 35 Q3, Q5, Q8, Q9), 9 pour des étiquettes seules (30 Q7 ; 31 Q5 ; 34 Q4, Q5 ; 35 Q1, Q2, Q4, Q10, Q12), 4 pour l'étage seul (30 Q6 ; 34 Q6 ; 35 Q6, Q7) ; + en-têtes de 4 missions (30, 33, 34 → d2 practice 75/15 ; 35 → d3 boss 120/30) et 2 titres (30, 35).** Tous les correctifs ont été appliqués sur copie hors dépôt et revérifiés (§ Vérification des correctifs).

---

## Tableaux (ma réponse aveugle · clé · verdict)

### 30 — 2010 (tech.) ex.3, d3 boss 120/30 — fidèle (AB = 9, AC = 4,8, BH = 3 ; 1a→Q1, 1b→Q2-Q3, 2a→Q4-Q5, 2b→Q6, 2c→Q7 ; l'échelle 1/50 n'est pas employée par le sujet non plus)
| Q | moi | clé | verdict | motif |
|---|---|---|---|---|
| 1 | b | b | à reprendre (mineur) | d « متقايس الضلعين » nie la figure (angle droit marqué, AB ≠ AC à vue) |
| 2 | c | c | OK | 81 + 23,04 = 104,04 ; d (190,44) muette, voir familles |
| 3 | d | d | OK | √104,04 = 10,2 |
| 4 | a | a | OK / réserve | titre « إثبات التوازي » livre la moitié de la clé (M-1) ; gabarit répété (m-14) |
| 5 | b | b | OK | plan 2×2 sain |
| 6 | a | a | réserve | d3 surcoté (M-9) |
| 7 | d | d | réserve | d3 surcoté (M-9) ; b muette → `segment-mal-choisi` |

### 31 — 2012 (tech.) ex.3, d3 boss 120/30 — fidèle (AB = 4, AD = 3, BM = 3 ; 1→Q1, 2a→Q2-Q3, 2b→Q4-Q6, 3→Q7-Q8)
| Q | moi | clé | verdict | motif |
|---|---|---|---|---|
| 1 | b | b | réserve | 3-4-5 déjà publié (09/19 Q3, options 5/7/25) — mineur |
| 2 | a | a | OK | proche de 09/29 Q1 publiée (même fait, autres pièges) — mineur |
| 3 | d | d | OK | — |
| 4 | c | c | à reprendre | rapport NOMMÉ dans l'énoncé (M-11) |
| 5 | b | b | OK | a muette → `segment-mal-choisi` |
| 6 | a | a | OK | — |
| 7 | c | c | mineur | « المنزل » non introduit |
| 8 | b | b | à reprendre | glose de l'échelle absente ; « على الرسم » sans figure ; étiquettes (M-5, m-3) |

### 32 — 2015 (tech.) ex.3, d3 boss 120/30 — fidèle (AB = 10, BE = 4, BF = 5, EF = 3, 189 000 D, 3150 m² ; 8 questions pour 7 sous-questions, 4a scindée — adaptation sans perte)
| Q | moi | clé | verdict | motif |
|---|---|---|---|---|
| 1 | b | b | OK | — |
| 2 | a | a | OK | — |
| 3 | c | c | mineur | l'énoncé annonce le but « لإثبات أنّ … متوازيان » |
| 4 | d | d | OK | — |
| 5 | c | c | OK | — |
| 6 | a | a | OK | — |
| 7 | b | b | à reprendre | **technique non enseignée** (facteur des aires) et glose absente (M-3) |
| 8 | c | c | à reprendre | d3 pour une division, énoncé qui imprime la clé de Q7, explication inexécutable (M-4) |

### 33 — 2024 (tech.) ex.3, d3 boss 120/30 — fidèle (AC = 5, BC = 4, AM = 3,75, 1/40)
| Q | moi | clé | verdict | motif |
|---|---|---|---|---|
| 1 | d | d | OK | plan 2×2 sain ; a, c muettes (famille « réciproque », voir étiquettes) |
| 2 | b | b | OK | — |
| 3 | a | a | à reprendre | distracteur c DÉFENDABLE (M-6) |
| 4 | c | c | à reprendre | rapport nommé (M-11) |
| 5 | b | b | réserve | d3 surcoté (M-9) ; étiquette « 4 cm » ambiguë (m-9) |
| 6 | c | c | réserve | glose absente ; étiquettes (m-3) |

### 34 — 2026 (tech.) ex.3, d3 boss 120/30 — fidèle (AB = 3, AC = 4, CE = 8, 1/10000 ; 1a reformulée en « quelle égalité », sans perte)
| Q | moi | clé | verdict | motif |
|---|---|---|---|---|
| 1 | a | a | à reprendre | vote terme à terme reconstruit la clé (M-7) |
| 2 | c | c | à reprendre | doublon de fait de 31 Q1 / 09/19 Q3 (M-10) |
| 3 | d | d | à reprendre | vote terme à terme + explication fausse (M-8) |
| 4 | c | c | OK | d muette → `segment-mal-choisi` |
| 5 | b | b | OK | d muette → `segment-mal-choisi` |
| 6 | d | d | réserve | d3 surcoté : somme de 4 longueurs DONNÉES le long d'un tracé SURLIGNÉ (M-9) |
| 7 | b | b | à reprendre | « يمثّل الرسم » sans figure (M-2) ; glose absente |

### 35 — 2002 ex.4 (problème), d4 challenge 300/60 — fidèle (1a « أُرسم » non transformable, absorbée par Q1 ; 5 « G centre de gravité » → Q12 « HG/HB », conclusion seulement dans l'explication : acceptable)
| Q | moi | clé | verdict | motif |
|---|---|---|---|---|
| 1 | b | b | OK | a muette → `segment-mal-choisi` |
| 2 | c | c | OK | a, d muettes → `position-relative-ignoree` |
| 3 | a | a | mineur | explication écrit « √80 = 16√5 » |
| 4 | d | d | OK | b muette → `segment-mal-choisi` |
| 5 | b | b | mineur | explication écrit « (2√5)² = 2 × 5 = 10 » |
| 6 | a | a | réserve | d3 surcoté (M-12) |
| 7 | d | d | OK | b, c fausses sans ambiguïté (« دائمًا ») ; clé non la plus longue (57 c. contre 58) |
| 8 | c | c | à reprendre | clé désignée par l'énoncé ET la couleur ; figure inexacte (M-13) |
| 9 | a | a | mineur | « المستقيم الكامل [EB] » ([EB] est une قطعة, pas un مستقيم) |
| 10 | d | d | OK | a muette → `segment-mal-choisi` |
| 11 | b | b | OK | — |
| 12 | c | c | à reprendre | titre « ومركز الثقل » livre 2/3 (M-1) |

---

## Défauts classés

### Critiques
Aucun : 48/48 clés justes, aucune double réponse avérée (33 Q3 c est défendable, classé majeur M-6).

### Majeurs
- **M-1 — Titres qui livrent une clé.** 30 : « فيثاغورس ثمّ إثبات التوازي وطاليس » annonce le RÉSULTAT de Q4 (متوازيان) et réduit Q4 à deux options. 35 : « … وطاليس ومركز الثقل » annonce que le point nouveau de Q12 (G) est le centre de gravité ⇒ HG/HB = 2/3 sans calcul (même piège que « عددان مقلوبان »). Correctifs : titres ci-dessous (§ Correctifs exacts).
- **M-2 — 34 Q7 renvoie à un dessin absent** : « يمثّل الرسم تصميمًا لمضمار سباق … » sans `<svg>` (la regex `FIGURE_REFERENCE` ne connaît que « الرسم التالي/المجاور », d'où le vert des gates). L'élève est envoyé vers un dessin qui n'existe pas. Correctif : énoncé réécrit (sans « الرسم », glose ajoutée).
- **M-3 — 32 Q7 : technique non enseignée.** L'aire réelle à partir d'une aire de plan exige le facteur k² (×1000², puis ÷10 000) : aucun cours antérieur à 09 ne l'enseigne (math-6eme/14, 7eme/07, 8eme/05 n'enseignent l'échelle que pour les LONGUEURS ; k² n'est qu'en math/13, hors de l'ordre du manifeste). Constat factuel : **la glose de l'échelle annoncée par l'auteur n'est dans AUCUN énoncé** (31 Q8, 32 Q7, 33 Q6, 34 Q7 : seulement « وفق السلّم 1/1000 » / « سلّمه 1/40 ») — elle n'est que dans les explications. Pour les longueurs ce n'est pas un défaut (échelle enseignée en 6ᵉ-8ᵉ, glose mot pour mot dans math-6eme/14 : « السلّم 1/1000 يعني أنّ 1 cm على التصميم يمثّل 1000 cm في الحقيقة ») ; pour l'aire, si. Correctif retenu : la glose du 6ᵉ dans l'énoncé (« أي أنّ كلّ 1 cm على التصميم يمثّل 1000 cm في الواقع »), qui rend le pas « carré de 10 m de côté = 100 m² » dérivable d'acquis (aire du carré) sans donner la clé : les trois pièges (315, 31 500, 315 000) restent exécutables. Si l'orchestrateur exige la règle k² elle-même dans l'énoncé, la question devient d1 : je ne le recommande pas ; mieux vaudrait l'enseigner dans le cours 08 ou 09 (hors tranche).
- **M-4 — 32 Q8.** (i) d3 pour une seule division 189 000 ÷ 3150 (la même tâche est d2 en 08/19 Q8 publiée) ; (ii) l'étage n'est relevé que pour garder Q8 derrière Q7, car son énoncé IMPRIME 3150 = clé de Q7 (interdit : « Jamais relever la difficulté d'une étape réellement facile pour la forcer à sa place ») ; (iii) l'explication décrit des mécanismes inexécutables (« القسمة على مساحة حُسبت خطأ … 315 … 31,5 … 31 500 ») alors que l'énoncé DONNE 3150. Correctif : l'énoncé donne l'aire du plan + l'échelle glosée (Q8 devient un vrai d3 : aire réelle puis division ; 3150 n'est plus imprimé ; les trois distracteurs redeviennent exécutables et l'explication est réécrite).
- **M-5 — 31 Q8, 33 Q6, 34 Q7 (et 32 Q7) : distracteurs muets qui ont une étiquette EXISTANTE exacte** (précédent publié 08/19 Q5, 08/14 Q4) : résultat laissé en cm (7500, 200, 240 000) et aire/périmètre du plan (7,5) → `math.alg.reponse-a-l-autre-inconnue` ; ÷10 au lieu de ÷100 ou ÷1000 (750, 20, 24 000, 240) → `math.num.puissance-de-dix-rangs-mal-comptes` ; division par l'échelle 5 ÷ 40 = 0,125 → `math.num.operation-inverse-appliquee` (« قسمةً بدل الضرب ») ; 32 Q7 : 315 (facteur 10 au lieu de 100) et 315 000 (« 1 m² = 10 000 cm² » ignoré) → `math.mes.conversion-aire-facteur-errone` — son libellé est ici exact à la lettre (« par 100, pas par 10 » ; « 1 m² = … 10 000 cm² ») et c'est l'étiquette posée sur la même erreur en 08/19 Q6. 31 500 reste muette (double erreur).
- **M-6 — 33 Q3 c défendable.** « متوازيان ، لأنّ المثلّثين ABC و AMN قائمان » : avec l'énoncé (droits en B et en M, B ∈ [AM]) c'est la forme INCOMPLÈTE de la clé, pas une erreur ; un élève peut la défendre. Correctif : c/d « … لأنّ B من [AM] و C من [AN] » (fausse sans ambiguïté : la position des points ne donne pas le parallélisme), c étiquetée `math.geo.thales-sans-verifier-parallelisme`, d muette (double erreur) ; le plan 2×2 est conservé, et le gabarit s'écarte de 30 Q4 (dont c/d sont « يقطع (AB) »).
- **M-7 — 34 Q1 : vote terme à terme.** Chaque distracteur ne change qu'une composante de la clé (membre de gauche BC/AC/AB ; carrés ou non) : majorité « BC » (a, d) × majorité « carrés » (a, b, c) = a, la clé. Correctif : c → « AC = AB + BC » (double erreur, muette) ; plan 2×2 parfait (BC/AC × carrés/sans).
- **M-8 — 34 Q3 : vote terme à terme + explication fausse.** Seconde nouvelle « CE/CA » majoritaire (b, d), numérateur « CD » majoritaire (a, c, d) ⇒ d, la clé. L'explication dit « استعمال المستقيم الكامل [DB] بدل الجزء [CD] » : [DB] est une قطعة, et elle remplace [CB], pas [CD] (le mécanisme écrit ne produit pas l'option). Correctif : b → « CB/CD = CA/CE = DE/AB » (`thales-rapport-inverse` : deux nouvelles inversées, la troisième non — fausse : 1/2, 1/2, 2) ; a et c → `segment-mal-choisi` ; explication réécrite.
- **M-9 — Étage des missions 30, 33, 34 (en-tête malhonnête) et rampes surcotées.** La même tâche — une longueur par Thalès en une étape — est d2 en 31 Q5/Q6, 32 Q5, 34 Q4/Q5 et d3 en 30 Q6/Q7, 33 Q5. Honnêtement étiquetées, 30 et 33 n'ont AUCUNE question d3 (Q6/Q7 de 30 et Q5/Q6 de 33 sont d2) ; 34 Q6 est une somme de quatre longueurs données le long d'un tracé surligné (d1-d2) et seule 34 Q7 (somme + échelle + conversion) est d3. Un en-tête d3 dont toutes les questions sont plus faciles que lui est malhonnête. Précédent publié : les exercices « technique » de même facture (08/14 2011-tech ex.3, 08/19 2013-tech ex.2, 08/20 2025-tech ex.3) sont **d2 practice 75/15**. Correctif : 30, 33, 34 → d2 practice 75/15, ⭐⭐ ; rampes 30 : 1,2,2,2,2,2,2 ; 33 : 1,1,2,2,2,2 ; 34 : 1,2,2,2,2,2,3 (Q2 réécrite d2). L'ordre d'émission reste celui du fichier (vérifié). 31 (Q7 : deux soustractions + somme ; Q8 : somme + échelle + conversion) et 32 (Q6, Q7, Q8 corrigée) gardent un d3 défendable.
- **M-10 — 34 Q2 doublon de fait.** √(3² + 4²) = 5 avec options {5, 7, 25, …}, mêmes pièges (somme, racine oubliée), même explication que 31 Q1 (tranche) et que 09/19 Q3 publiée (même chapitre) ; 35 Q1 fait le même calcul mais sous l'angle « rayon = BC » (acceptable). Correctif : 34 Q2 change d'angle — longueur du parcours A→B→C sur le plan (BC calculé à l'intérieur : la sous-question 1b reste exigée) : options 7 (AC au lieu de BC, `segment-mal-choisi`), **8**, 10 (BC = 3 + 4, `pythagore-sans-carres`), 28 (BC² = 25 non racine, `pythagore-racine-oubliee`) ; d2. Alternative si l'orchestrateur préfère la lettre du sujet : garder Q2 et la justifier en PR comme exercice parallèle.
- **M-11 — 31 Q4 et 33 Q4 : le rapport est NOMMÉ dans l'énoncé** (« ما قيمة النسبة BM/BA ؟ » avec AB = 4, BM = 3 ; « AM/AB » avec 3 et 3,75) : la question est une division d1 étiquetée d2, et les distracteurs 3, 1/4, 5, 0,25 ne sont accessibles que par une mauvaise lecture ; l'étiquette `thales-formes-melangees` de « 3 » (31) et de « 5 » (33) est inexacte (aucune égalité n'est écrite). Correctif : demander le rapport que Thalès fait CHOISIR — « ما قيمة النسبة MN/AD ؟ » (31 ; clé 3/4) et « ما قيمة النسبة MN/BC ؟ » (33 ; clé 1,25) : les étiquettes deviennent exactes (MN/AD = BM/MA → mélange des formes ; BA/BM → rapport inversé ; MA/BA → `segment-mal-choisi`).
- **M-12 — Étage de 35 : le d4 n'est pas honnête.** Honnêtement, Q6 (droite des milieux, application directe), Q7 (choix d'une propriété), Q8 (lecture des deux perpendiculaires données), Q9-Q10 (Thalès papillon : la même tâche est d2 en 34 Q3-Q5) sont d2, Q5 (réciproque avec radicaux) d2 ; seules Q11 (substitution) et Q12 (symétrie + rapport) sont d3. Chaque étape étant redonnée avec ses données, l'enchaînement du « problème » (8 points) n'est plus exigé : c'est un **d3 boss 120/30** (comme 09/22-09/25 publiées, de même ampleur) ; la parité avec les d4 de 20/19-21 ne tient que par l'ampleur. Correctif : d3 boss 120/30, ⭐⭐⭐, rampe 2×10 puis 3,3 (Q5-Q10 → 2). NB : garder Q5 à 3 en descendant Q6-Q10 ferait passer Q7 (« EFC القائم في C ») avant Q5 dont c'est la clé — d'où Q5 → 2.
- **M-13 — 35 Q8 : clé désignée, figure inexacte.** L'énoncé donne exactement « (BK) ⊥ (CF) في K » et « (CA) ⊥ (BF) في A », et la figure trace en VERT ces deux seules droites (couleur qui désigne la clé), avec les deux marques d'angle droit : aucune lecture n'est à faire (d1-d2, étiqueté d3). De plus la figure est fausse à l'échelle de son propre dessin : AC = 88 px pour AB = 72 px (3,67 au lieu de 4), d'où (BK) ∧ (CF) ≈ 86° là où l'angle droit est marqué, BC ≠ BF. Correctif : toutes les droites à l'encre du triangle, C(88;22), K(184;70), H(88;262), marque en K recalculée (SVG exact ci-dessous, vérifié : BK·CF = 0, BC = BF = BE, H ∈ (BK), AH = 6) ; d2 (cf. M-12). L'item reste une vérification de la définition de la hauteur ; c'est honnête en d2.

### Mineurs
- **m-1 — 30 Q1 d** « متقايس الضلعين ، عكس نظرية فيثاغورس » s'élimine à vue (droit marqué en A, AB ≠ AC sur la figure). → « قائم ، عكس نظرية طاليس » (2×2 : direct/réciproque × Pythagore/Thalès), explication complétée.
- **m-2 — 31 Q7** « ويُبنى المنزل » : référent non introduit (l'énoncé se lit seul) → « ويُبنى منزل ».
- **m-3 — « على الرسم » dans des énoncés sans figure** (31 Q8, 32 Q7) → « على التصميم » (comme 33 Q6) ; glose de l'échelle ajoutée aussi en 31 Q8, 33 Q6, 34 Q7 (non requise — échelle enseignée en 6ᵉ-8ᵉ — mais c'est l'adaptation déclarée et le précédent 08/14, 08/19).
- **m-4 — 32 Q3** « لإثبات أنّ المستقيمين (EF) و (AC) متوازيان » annonce le but que la 3ᵉ étape contredit → « لتحديد الوضعيّة النسبيّة للمستقيمين (EF) و (AC) ».
- **m-5 — 35 Q3 et Q5 : égalités fausses écrites** dans l'explication pour décrire l'erreur (« √80 = 16√5 », « (2√5)² = 2 × 5 = 10 ») → reformulées « 16√5 بدل 4√5 », « حساب 2 × 5 = 10 بدل 4 × 5 = 20 ».
- **m-6 — 35 Q9** « المستقيم الكامل [EB] » (c'est une قطعة) et « نسب جزء إلى كلّ لا تصلح في وضعية الفراشة » (inexact : AB/EB = AH/CH est vraie ; elle n'égale simplement pas BH/EC) → reformulé.
- **m-7 — 35 Q12 b** étiquetée `centre-gravite-milieu-mediane` : l'énoncé ne parle pas de centre de gravité ; la voie numérique naturelle vers 1/2 est HG/HK (G est le milieu de [HK]). L'étiquette reste défendable par le titre du sujet ; à défaut, mentionner HG/HK dans l'explication. d (4/3, G du côté de K) → `position-relative-ignoree` (exact).
- **m-8 — Figures à l'échelle de la solution** : 30 Q6/Q7 (H au tiers de [BA] : HK ≈ AC/3 lisible contre 2,4 = AC/2 et 3,2 = 2AC/3), 31 Q5 (MN ≈ 3/4 de AD). Distordre légèrement (p. ex. BH ≈ 0,42 BA) si l'on veut fermer la lecture à l'œil.
- **m-9 — 33 Q5** : « 4 cm » posé ENTRE [BC] et [MN] (y = 194, BC à 174, MN à 210) → (x = 120, y = 166), au-dessus de [BC], hors du chevron (vérifié en rendu).
- **m-10 — 34 Q1** porte AB = 3 et AC = 4, inutiles à la question (charge).
- **m-11 — 34 Q6** : tracé A-B-C-D-E surligné en vert épais ; il désamorce les pièges AC + CE = 12, 18, 21 (le plan officiel n'a que trait plein / pointillés). Ramené à d2 (M-9), acceptable ; sinon tracer à l'encre normale.
- **m-12 — Vocabulaire** : « عكس نظرية طاليس » (31 Q3 b) quand le cours 08 dit « النظرية العكسية » — compréhensible, à aligner si l'on retouche.
- **m-13 — Restitutions de clés antérieures (donjon)** : 30 Q3 (104,04), 30 Q6 (10,2), 31 Q6-Q8 (5, 2,25, 3,75 ; 31 Q8 donne les 4 côtés ⇒ clé de Q7 par somme), 32 Q2 (25), 32 Q3 (EBF droit en E), 32 Q6 (7,5), 32 Q7 (31,5), 33 Q4-Q5 (AB = 3), 33 Q6 (MN = 5), 34 Q4-Q6 (5, 10, 6), 34 Q7 (les 4 segments ⇒ clé de Q6), 35 Q2 (BE = 5), 35 Q4 (AE = 2, AF = 8), 35 Q5 (CF = 4√5), 35 Q7 (« القائم في C »), 35 Q11, Q12. **Route quête : aucune fuite en avant** (ordre d'émission = ordre du fichier dans les six missions, vérifié, y compris après correctifs). Donjon : fuite possible si l'ordre s'inverse ; c'est le schéma accepté dans les missions publiées (08/19 Q7-Q8 redonnent 200 m², 08/20 Q4-Q5, 09/19-22) ; les cas où la donnée redonnée tue une question d3 sont traités (M-4 : 32 Q8 ; M-2/M-9 : 34 Q7 reste d3 mais 34 Q6 est d2 et la précède). 30 Q6 pourrait aussi recevoir AB, AC, BH au lieu de BC (Pythagore + Thalès, vrai d3 sans fuite) si l'on garde 30 en d3.
- **m-14 — Gabarits répétés** : 30 Q4 ≈ 08/20 Q2 publiée (a/b identiques aux lettres près, même étiquette) — 33 Q3 corrigé s'en écarte ; 31 Q2 ≈ 09/29 Q1 publiée (même fait, autres pièges) ; neuf calculs « Thalès en une étape » à trois mêmes pièges (inverse / formes / additif) ; trois conversions « échelle → m » (31 Q8, 33 Q6, 34 Q7 ; cf. 08/19 Q5). Exercices parallèles voulus par le sujet (données officielles différentes) : acceptables, à signaler en PR.
- **m-15 — Distracteurs 3-4-5 éliminables par l'inégalité triangulaire** (31 Q1, 35 Q1 : seules 5 est entre 4 et 7) — pièges classiques, toléré.
- **m-16 — Rendu (moteur, pas contenu)** : « 1 m = 100 cm », « 1 m² = 10 000 cm² », « 1000 cm = 10 m » dans les explications (31 Q8, 32 Q7, 33 Q6, 34 Q7) se posent « m = 100 cm 1 » à l'œil ; l'ordre de LECTURE (droite à gauche) reste exact, et `DIGIT_FIRST_FORMULA` ne les vise pas (pas d'opérateur entre « 1 » et « m »). Contournement de contenu fourni pour 32 Q7/Q8 (« 1000 cm ، أي 10 m »).
- **m-17 — 31 Q4 / 33 Q4** : avant correctif, d2 pour une division nommée (cf. M-11).

---

## Réponses aux points d'attention

- **Aveugle** : 48/48 conformes. Figures : vraies (alignements, parallèles, angles droits, proportions de 30, 31, 32, 33, 34 exactes au pixel près) sauf 35 Q8 (M-13) ; aucune longueur écrite sur un tronçon coupé ; aucun angle droit marqué là où il est à démontrer (32 Q3 marque E : c'est une prémisse de l'énoncé) ; arabe seulement dans `<title>` ; aucun élément ni attribut interdit ; rien hors viewBox.
- **Fidélité** : toutes les données = transcription ; aucune sous-question perdue. Adaptations déclarées : « montrer que » → choix : OK ; 32 à 8 questions : OK ; 35 Q8 rappel de « المركز القائم » (non enseigné : vérifié, aucun cours ; même procédé que 09/11 Q2 et 09/15 publiées) : OK ; 35 Q12 définit la symétrie (« B منتصف [KG] ») : OK (symétrie centrale enseignée en 8ᵉ de toute façon) ; 35 Q6/Q7 « B milieu de [EF] parce que diamètre » : OK ; 35 Q2 BE = 5 : nécessaire (rayon), livre la clé de Q1 au seul donjon (m-13) ; BC = 10,2 (30 Q6), AC = 7,5 (32 Q6), BH = (3/2) × EC (35 Q11) : livrent la clé de Q3, Q5, Q10 respectivement au seul donjon (m-13).
- **Échelle** : la glose déclarée n'existe que dans les explications (M-3). Pour les longueurs, inutile (enseignée en 6ᵉ-8ᵉ) ; ajoutée par cohérence (m-3). Pour l'aire (32 Q7/Q8), nécessaire et suffisante pour rendre le pas dérivable ; elle ne donne pas la clé (le carré reste à faire) ; le facteur k² n'est pas donné.
- **Programme (R-3)** : Pythagore + réciproque (09, 8ᵉ), Thalès + papillon + droite des milieux + centre de gravité (08), médiane/hauteur (7ᵉ), perpendiculaires/parallèles (6ᵉ, y compris « عمودي على أحد مستقيمين متوازيين »), symétrie centrale (8ᵉ), aire du triangle, conversions (6ᵉ), échelle des longueurs (6ᵉ-8ᵉ) : enseignés. Non enseignés : orthocentre (donné par rappel, OK) ; facteur des aires (M-3). Aucun vecteur, aucune translation.
- **Étiquettes** : les 69 étiquettes posées sont exactes, sauf « 3 » (31 Q4) et « 5 » (33 Q4) → corrigées par M-11 ; 35 Q12 b discutable (m-7). Options muettes qui ont une étiquette existante : 30 Q7 b, 31 Q5 a, 31 Q4 d*, 33 Q4 a*, 34 Q2 a*, 34 Q3 a, 34 Q3 c, 34 Q4 d, 34 Q5 d, 35 Q1 a, 35 Q4 b, 35 Q9 c, 35 Q10 a → `math.geo.segment-mal-choisi` (origin/main seulement : à rebaser ; sans compétence au registre) ; 35 Q2 a, d et 35 Q12 d → `math.geo.position-relative-ignoree` (origin/main) ; échelle : M-5 ; 30 Q4 c « يقطع (AB) » → `math.geo.intersection-prise-pour-perpendicularite` envisageable (précédent 09/29 Q1 d), laissée muette dans mes copies car le libellé parle de perpendicularité, pas de parallélisme (au choix de l'orchestrateur). (* après correctif.)
- **Familles muettes — nouvelle étiquette ?** (comptage tranche + `origin/main`, grep) :
  - Réciproque/direct de Pythagore confondus : 30 Q1 a, 33 Q1 c (+ a, double), **09/25 Q2 publiée** (« نظرية فيثاغورس المباشرة » pour prouver un angle droit, muette) ⇒ **3 questions : mérite une étiquette**. Proposition : `math.geo.pythagore-reciproque-role`, compétence `math.geo.pythagore` (« مبرهنة فيثاغورس: المباشرة والعكسية ») ; fr « Tu confonds Pythagore et sa réciproque : le théorème part d'un triangle rectangle pour donner l'égalité des carrés ; la réciproque part de l'égalité pour prouver l'angle droit » ; en « You mix up Pythagoras' theorem and its converse: the theorem starts from a right triangle and gives the equality of squares; the converse starts from that equality and proves the right angle » ; ar « تخلط بين مبرهنة فيثاغورس وعكسها: المباشرة تنطلق من مثلّث قائم لتعطي تساوي المربّعات، والعكسية تنطلق من تساوي المربّعات لتُثبت الزاوية القائمة » ; phrase d'élève fr « L'angle droit est marqué, donc j'applique la réciproque pour écrire BC² = AB² + AC² » / ar « الزاوية القائمة معلّمة ، فأطبّق عكس فيثاغورس لأكتب BC² = AB² + AC² » / en « The right angle is marked, so I use the converse to write BC² = AB² + AC² ». À poser sur 30 Q1 a et 33 Q1 c (33 Q1 a reste muette : double erreur ; 33 Q1 b « مثلّث AMN » → `segment-mal-choisi` possible).
  - (a + b)² pris pour a² + b² : 30 Q2 d, 32 Q1 a ; aucune occurrence publiée trouvée ⇒ 2 : muette.
  - Facteur linéaire appliqué à l'aire : 32 Q7 a, 32 Q8 b (après correctif), 08/19 Q6 c publiée ⇒ 3, mais l'étiquette existante `conversion-aire-facteur-errone` est exacte ici (facteur 10 contre 100) et déjà employée pour ce cas : pas d'étiquette nouvelle nécessaire. (Une étiquette générique « تطبّق على المساحة نسبة الأطوال » enseignerait k², non enseigné : déconseillé tant que le cours ne le porte pas.)
  - Droite/segment entier au lieu du tronçon (papillon) : couvert par `segment-mal-choisi` existant.
  - E/F permutés (35 Q2 b) : 1 question, double erreur, muette.
  - Périmètre du mauvais polygone (31 Q7 a, b) : 1 question ; `reponse-a-l-autre-inconnue` conviendrait (« une autre grandeur que celle demandée ») — facultatif.
  - « Couper une sécante commune » : 30 Q4 c, 31 Q2 b ⇒ 2 (33 Q3 c/d relevait d'une autre raison) : muette.
  - Mauvais sommet/triangle de Thalès : 31 Q3 a, 32 Q4 a-c ⇒ 2 questions : muette.
  - Orthocentre (35 Q8) : 1 : muette.
- **Distracteurs / forme** : 0 clé strictement la plus longue (brut et sans diacritiques) ; aucune option somme ou différence de deux autres ; votes terme à terme : 34 Q1 et 34 Q3 (M-7, M-8), tous les autres plans 2×2 sains (30 Q4/Q5, 31 Q3, 32 Q2, 33 Q1/Q3, 35 Q2/Q4/Q6/Q8) ; options niant une prémisse : 30 Q1 d (m-1) ; énoncé annonçant le résultat : 32 Q3 (m-4) ; aucune paire « −2 ، 3 » (35 Q2 étiquette les valeurs « AE = 2 ; AF = 8 ») ; coches ✓ toujours après la clé.
- **Titres** : format exact, displayOrder 30-35, récompenses canoniques ; fuites : M-1.
- **Doublons** : (a) 31 Q1 ≈ 09/19 Q3 (mineur), 31 Q2 ≈ 09/29 Q1 (mineur) ; (b) 34 Q2 ≈ 31 Q1 (M-10), 30 Q4 ≈ 33 Q3 (réduit par M-6), répétitions de gabarit (m-14) ; (c) 30 Q4 ≈ 08/20 Q2 ; 32 Q7/Q8 ≠ 08/19 Q6/Q8 (autres données, Q8 publiée est une inéquation) ; 33 Q6 ≈ 08/19 Q5 (même famille de pièges, autres données) ; rien de quasi identique ailleurs (12, 18, 20, 03, 04, 07, 17).
- **Rendu arabe** : 0 chaîne brouillée (contrôle d'ordre visuel en Chromium, deux largeurs ; lignes de données toutes acceptées par `isDisplayEquation` ; options mixtes de 35 Q6/Q8 lues dans l'ordre source) ; m-16 pour le comportement du moteur.
- **Piège de passe** : aucune « على الشكل التالي » ; le vrai trou est l'inverse (M-2 : « يمثّل الرسم » sans figure, non vu par la regex).

---

## Correctifs exacts (texte de remplacement, appliqué sur copie et revérifié)

#### 30 — `30-examen-2010-technique-ex3-escalier-pythagore-thales.json`
- `title` : `🏛️ مناظرة 2010 (تقني) · التمرين 3 ⭐⭐⭐: تصميم مدارج — فيثاغورس ثمّ إثبات التوازي وطاليس` → `🏛️ مناظرة 2010 (تقني) · التمرين 3 ⭐⭐: تصميم مدارج — فيثاغورس والوضعية النسبية لمستقيمين وطاليس`
- `difficulty` : `3` → `2`
- `mode` : `boss` → `practice`
- `xpReward` : `120` → `75`
- `rewardCoins` : `30` → `15`
- Q1 option d : «متقايس الضلعين ، عكس نظرية فيثاغورس» → «قائم ، عكس نظرية طاليس»
- Q1 `explanation` → «رمز الزاوية القائمة في الرسم عند A ، فالمثلّث ABC قائم في A ووتره [BC] هو الضلع المقابل لها. وفي مثلّث قائم نطبّق نظرية فيثاغورس المباشرة: مربّع الوتر يساوي مجموع مربّعي الضلعين القائمين ، أي BC² = AB² + AC² ✓. الخطأ الشائع: استعمال عكس نظرية فيثاغورس ، وهي لا تُستعمل إلّا لإثبات أنّ مثلّثًا قائم انطلاقًا من أطواله ، أمّا هنا فالزاوية القائمة معطاة في الرسم ؛ أو الخلط مع نظرية طاليس أو عكسها ، وهما تتعلّقان بنسب أطوال ومستقيمات متوازية ولا تعطيان مجموع مربّعات.»
- Q6 `difficulty` : 3 → 2
- Q7 `difficulty` : 3 → 2
- Q7 option b `misconceptionTag` : (muette) → math.geo.segment-mal-choisi

#### 31 — `31-examen-2012-technique-ex3-terrain-rectangle-diagonale-thales.json`
- Q4 `prompt` (texte ; figure éventuelle inchangée, notée <svg…/>) → «ABCD مستطيل يمثّل تصميمًا لقطعة أرض ، والنقطة M من القطعة [AB] ، والنقطة N من القطعة [BD] ، والمستقيمان (MN) و (AD) متوازيان ، ونعلم أنّ الأطوال بالصنتمتر هي:
AB = 4
BM = 3
ما قيمة النسبة MN/AD ؟
<svg…/>»
- Q4 option d `misconceptionTag` : (muette) → math.geo.segment-mal-choisi
- Q4 `explanation` → «(MN) ∥ (AD) و M من [BA] و N من [BD] ، فبنظرية طاليس في المثلّث BAD تساوي النسبة MN/AD النسبة BM/BA ، أي MN/AD = 3/4 ✓ ، وهو المعامل الذي يصغّر المثلّث BAD إلى BMN. الخطأ الشائع: قلب النسبة فنجد BA/BM = 4/3 ؛ أو مقابلة MN/AD بنسبة الجزء على الجزء المتبقّي BM/MA ، حيث MA = 4 − 3 = 1 ، فنجد 3 ؛ أو أخذ القطعة المتبقّية MA بدل BM فنجد MA/BA = 1/4.»
- Q5 option a `misconceptionTag` : (muette) → math.geo.segment-mal-choisi
- Q7 `prompt` (texte ; figure éventuelle inchangée, notée <svg…/>) → «ABCD مستطيل يمثّل تصميمًا لقطعة أرض ، والنقطة M من القطعة [AB] ، والنقطة N من القطعة [BD] ، ويُبنى منزل على الرباعي AMND المظلَّل في الرسم.
نعلم أنّ طول كلّ قطعة من القطع التالية على الرسم بالصنتمتر هو:
AB = 4
AD = 3
BD = 5
BM = 3
BN = 3,75
MN = 2,25
ما محيط الرباعي AMND على الرسم بالصنتمتر ؟
<svg…/>»
- Q8 `prompt` (texte ; figure éventuelle inchangée, notée <svg…/>) → «يمثّل الرباعي AMND تصميمًا لجزء من قطعة أرض وفق السلّم 1/1000 ، أي أنّ كلّ 1 cm على التصميم يمثّل 1000 cm في الواقع ، وأطوال أضلاعه على التصميم بالصنتمتر هي:
AM = 1
MN = 2,25
ND = 1,25
DA = 3
ما المحيط الحقيقي لهذا الجزء بالمتر ؟»
- Q8 option a `misconceptionTag` : (muette) → math.alg.reponse-a-l-autre-inconnue
- Q8 option c `misconceptionTag` : (muette) → math.num.puissance-de-dix-rangs-mal-comptes
- Q8 option d `misconceptionTag` : (muette) → math.alg.reponse-a-l-autre-inconnue
- Q8 `explanation` → «السلّم 1/1000 يعني أنّ 1 cm على التصميم يمثّل 1000 cm في الواقع. محيط الرباعي على التصميم هو 1 + 2,25 + 1,25 + 3 = 7,5 cm ، فمحيطه الحقيقي 7,5 × 1000 = 7500 cm. ونحوّل إلى المتر بالقسمة على 100 لأنّ 1 m = 100 cm ، فنجد 7500 ÷ 100 = 75 m ✓. الخطأ الشائع: ترك النتيجة بالصنتمتر وقراءتها بالمتر فنجد 7500 ؛ أو القسمة على 10 بدل 100 عند التحويل فنجد 750 ؛ أو إهمال السلّم فنجد 7,5.»

#### 32 — `32-examen-2015-technique-ex3-terrain-reciproque-thales-aire-prix.json`
- Q3 `prompt` (texte ; figure éventuelle inchangée, notée <svg…/>) → «في تصميم قطعة الأرض ، المثلّث ABC قائم في A ، والنقطة E من القطعة [AB] ، والنقطة F من القطعة [CB] ، والمثلّث EBF قائم في E.
لتحديد الوضعيّة النسبيّة للمستقيمين (EF) و (AC) كتب تلميذ ما يلي:
الخطوة 1 : المثلّث EBF قائم في E ، فالمستقيم (EF) عمودي على المستقيم (EB).
الخطوة 2 : المستقيم (EB) هو المستقيم (AB) ، والمثلّث ABC قائم في A ، فالمستقيم (AC) عمودي على (AB).
الخطوة 3 : المستقيمان (EF) و (AC) عموديان على مستقيم واحد ، إذن (EF) و (AC) متعامدان.
في أيّ خطوة يوجد الخطأ ؟
<svg…/>»
- Q7 `prompt` (texte ; figure éventuelle inchangée, notée <svg…/>) → «يمثّل الرباعي AEFC تصميمًا لجزء من قطعة أرض وفق السلّم 1/1000 ، أي أنّ كلّ 1 cm على التصميم يمثّل 1000 cm في الواقع ، ومساحته على التصميم بالصنتمتر المربّع هي 31,5.
ما مساحته الحقيقية بالمتر المربّع ؟»
- Q7 option a `misconceptionTag` : (muette) → math.mes.conversion-aire-facteur-errone
- Q7 option d `misconceptionTag` : (muette) → math.mes.conversion-aire-facteur-errone
- Q7 `explanation` → «السلّم 1/1000 يعني أنّ 1 cm على التصميم يمثّل 1000 cm ، أي 10 m ، في الواقع. والمساحة تُنسب إلى بُعدين ، فيُضرب عامل الأطوال في نفسه: 1 cm² على التصميم يمثّل 10 × 10 = 100 m². فالمساحة الحقيقية 31,5 × 100 = 3150 m² ✓. الخطأ الشائع: تطبيق عامل الأطوال 10 على المساحة فنجد 31,5 × 10 = 315 ؛ أو ضرب المساحة في 1000 وقراءتها بالمتر المربّع فنجد 31 500 ؛ أو ضربها في 1000 × 1000 ثمّ التحويل بالقسمة على 100 فنجد 315 000 ، مع أنّ 1 m² = 10 000 cm².»
- Q8 `prompt` (texte ; figure éventuelle inchangée, notée <svg…/>) → «بيع الجزء AEFC من قطعة أرض بثمن جملي قدره 189 000 دينار ، ومساحته على تصميم سلّمه 1/1000 هي 31,5 cm² ، أي أنّ كلّ 1 cm على التصميم يمثّل 1000 cm في الواقع.
ما ثمن بيع المتر المربّع الواحد بالدينار ؟»
- Q8 option a `misconceptionTag` : (muette) → math.alg.reponse-a-l-autre-inconnue
- Q8 option b `misconceptionTag` : (muette) → math.mes.conversion-aire-facteur-errone
- Q8 `explanation` → «نحسب أوّلًا المساحة الحقيقية: كلّ 1 cm على التصميم يمثّل 1000 cm ، أي 10 m ، فكلّ 1 cm² يمثّل 10 × 10 = 100 m² ، والمساحة الحقيقية 31,5 × 100 = 3150 m². ثمن المتر المربّع الواحد هو الثمن الجملي مقسومًا على هذه المساحة: 189 000 ÷ 3150 = 60 دينارًا ✓ ، لأنّ 3150 × 60 = 189 000. الخطأ الشائع: تطبيق عامل الأطوال 10 على المساحة فنجد 315 m² ثمّ 189 000 ÷ 315 = 600 ؛ أو القسمة على مساحة التصميم 31,5 فنجد 6000 ؛ أو ضرب مساحة التصميم في 1000 فنجد 31 500 ثمّ 6.»

#### 33 — `33-examen-2024-technique-ex3-panneau-solaire-pythagore-thales-echelle.json`
- `title` : `🏛️ مناظرة 2024 (تقني) · التمرين 3 ⭐⭐⭐: هيكل حديدي للوحة شمسية — فيثاغورس وطاليس والسلّم` → `🏛️ مناظرة 2024 (تقني) · التمرين 3 ⭐⭐: هيكل حديدي للوحة شمسية — فيثاغورس وطاليس والسلّم`
- `difficulty` : `3` → `2`
- `mode` : `boss` → `practice`
- `xpReward` : `120` → `75`
- `rewardCoins` : `30` → `15`
- Q3 option c : «متوازيان ، لأنّ المثلّثين ABC و AMN قائمان» → «متوازيان ، لأنّ B من [AM] و C من [AN]»
- Q3 option c `misconceptionTag` : (muette) → math.geo.thales-sans-verifier-parallelisme
- Q3 option d : «متعامدان ، لأنّ المثلّثين ABC و AMN قائمان» → «متعامدان ، لأنّ B من [AM] و C من [AN]»
- Q3 `explanation` → «المثلّث ABC قائم في B والنقطة B من [AM] ، فالمستقيم (BC) عمودي على (AM). والمثلّث AMN قائم في M ، فالمستقيم (MN) عمودي على (AM). وكلّ مستقيمين عموديين على مستقيم واحد متوازيان ، إذن (BC) ∥ (MN) ✓ ، وهذا التوازي شرط تطبيق نظرية طاليس. الخطأ الشائع: الاستنتاج أنّ المستقيمين متعامدان ، والصواب أنّ العموديّين على مستقيم واحد متوازيان ؛ أو الاكتفاء بأنّ B من [AM] و C من [AN] ، وهذا وحده لا يعطي التوازي: لو أخذنا نقطة أخرى من [AN] مكان C لما وازى (BC) المستقيم (MN).»
- Q4 `prompt` (texte ; figure éventuelle inchangée, notée <svg…/>) → «في الهيكل الحديدي للوحة شمسية ، المثلّث ABC قائم في B والمثلّث AMN قائم في M ، والنقطة B من القطعة [AM] ، والنقطة C من القطعة [AN] ، والمستقيمان (BC) و (MN) متوازيان ، ونعلم أنّ الأطوال بالصنتمتر هي:
AB = 3
AM = 3,75
ما قيمة النسبة MN/BC ؟
<svg…/>»
- Q4 option a `misconceptionTag` : (muette) → math.geo.segment-mal-choisi
- Q4 `explanation` → «(BC) ∥ (MN) والنقطتان B و C من [AM] و [AN] ، فبنظرية طاليس في المثلّث AMN تساوي النسبة MN/BC النسبة AM/AB ، أي MN/BC = 3,75/3 = 1,25 ✓ ، وهو معامل التكبير من المثلّث ABC إلى المثلّث AMN. الخطأ الشائع: قلب النسبة فنجد AB/AM = 3/3,75 = 0,8 ؛ أو مقابلة MN/BC بنسبة الجزء على الجزء المتبقّي AM/BM ، حيث BM = 3,75 − 3 = 0,75 ، فنجد 5 ؛ أو أخذ القطعة BM بدل AM فنجد BM/AB = 0,75/3 = 0,25.»
- Q5 `prompt` : seule la figure SVG change (voir § Figures)
- Q5 `difficulty` : 3 → 2
- Q6 `prompt` (texte ; figure éventuelle inchangée, notée <svg…/>) → «تمثّل القطعة [MN] قاعدة هيكل حديدي في تصميم سلّمه 1/40 ، أي أنّ كلّ 1 cm على التصميم يمثّل 40 cm في الواقع ، وطولها على التصميم بالصنتمتر هو 5.
ما طولها الحقيقي بالمتر ؟»
- Q6 `difficulty` : 3 → 2
- Q6 option a `misconceptionTag` : (muette) → math.alg.reponse-a-l-autre-inconnue
- Q6 option b `misconceptionTag` : (muette) → math.num.puissance-de-dix-rangs-mal-comptes
- Q6 option d `misconceptionTag` : (muette) → math.num.operation-inverse-appliquee

#### 34 — `34-examen-2026-technique-ex3-trace-course-pythagore-thales-papillon.json`
- `title` : `🏛️ مناظرة 2026 (تقني) · التمرين 3 ⭐⭐⭐: مضمار سباق بالسلّم — فيثاغورس وطاليس في وضعية الفراشة` → `🏛️ مناظرة 2026 (تقني) · التمرين 3 ⭐⭐: مضمار سباق بالسلّم — فيثاغورس وطاليس في وضعية الفراشة`
- `difficulty` : `3` → `2`
- `mode` : `boss` → `practice`
- `xpReward` : `120` → `75`
- `rewardCoins` : `30` → `15`
- Q1 option c : «AB² = AC² + BC²» → «AC = AB + BC»
- Q1 option c `misconceptionTag` : math.geo.hypotenuse-mal-choisie → (muette)
- Q1 `explanation` → «المستقيمان (AB) و (AC) متعامدان ، فالمثلّث ABC قائم في A ووتره [BC] الذي يقابل الزاوية القائمة. ونظرية فيثاغورس تضع مربّع الوتر في طرف ومجموع مربّعي الضلعين القائمين في الطرف الآخر: BC² = AB² + AC² ✓. الخطأ الشائع: وضع ضلع قائم مكان الوتر فنكتب AC² = AB² + BC² ، مع أنّ الوتر هو الضلع المقابل للزاوية القائمة عند A ؛ أو جمع الأطوال دون تربيعها فنكتب BC = AB + AC ؛ أو الخطأين معًا فنكتب AC = AB + BC.»
- Q2 `prompt` (texte ; figure éventuelle inchangée, notée <svg…/>) → «في تصميم مضمار سباق ، المستقيمان (AB) و (AC) متعامدان ، ونعلم أنّ الأطوال بالصنتمتر هي:
AB = 3
AC = 4
يمرّ المضمار من A إلى B ثمّ من B إلى C. ما طول هذا الجزء من المضمار على الرسم بالصنتمتر ؟
<svg…/>»
- Q2 `difficulty` : 1 → 2
- Q2 `correctOption` : c → b
- Q2 option a : «25» → «7»
- Q2 option a `misconceptionTag` : math.geo.pythagore-racine-oubliee → math.geo.segment-mal-choisi
- Q2 option b : «7» → «8»
- Q2 option b `misconceptionTag` : math.geo.pythagore-sans-carres → (muette)
- Q2 option c : «5» → «10»
- Q2 option c `misconceptionTag` : (muette) → math.geo.pythagore-sans-carres
- Q2 option d : «1» → «28»
- Q2 option d `misconceptionTag` : math.geo.pythagore-sans-carres → math.geo.pythagore-racine-oubliee
- Q2 `explanation` → «المثلّث ABC قائم في A ووتره [BC] ، فبنظرية فيثاغورس BC² = AB² + AC² = 3² + 4² = 9 + 16 = 25 ، ومنه BC = 5 cm. وطول الجزء من A إلى B ثمّ إلى C هو AB + BC = 3 + 5 = 8 cm ✓. الخطأ الشائع: المرور بالضلع [AC] بدل [BC] فنجد 3 + 4 = 7 ؛ أو حساب BC بجمع الطولين دون تربيع ، أي BC = 7 ، فنجد 3 + 7 = 10 ؛ أو نسيان الجذر والتوقّف عند BC² = 25 فنجد 3 + 25 = 28.»
- Q3 option a `misconceptionTag` : (muette) → math.geo.segment-mal-choisi
- Q3 option b : «CB/CD = CE/CA = DE/AB» → «CB/CD = CA/CE = DE/AB»
- Q3 option c `misconceptionTag` : (muette) → math.geo.segment-mal-choisi
- Q3 `explanation` → «المستقيمان (AE) و (BD) يتقاطعان في C بين A و E وبين B و D ، و (AB) ∥ (DE) ، فنحن في وضعية الفراشة برأس C: المثلّثان CAB و CED متقابلان بالرأس C ، و D يقابل B و E يقابل A. وتقارن نسب طاليس كلّ طول من المثلّث CED بنظيره من المثلّث CAB: CD/CB = CE/CA = DE/AB ✓. الخطأ الشائع: قلب النسبتين الأوليين فنكتب CB/CD = CA/CE ، فلا تبقى في الاتّجاه نفسه مع DE/AB ؛ أو مقابلة D بـ A و E بـ B فنكتب CD/CA = CE/CB ؛ أو أخذ القطعتين الكاملتين [DB] و [EA] بدل [CB] و [CA] فنكتب CD/DB = CE/EA.»
- Q4 option d `misconceptionTag` : (muette) → math.geo.segment-mal-choisi
- Q5 option d `misconceptionTag` : (muette) → math.geo.segment-mal-choisi
- Q6 `difficulty` : 3 → 2
- Q7 `prompt` (texte ; figure éventuelle inchangée, notée <svg…/>) → «مضمار سباق مرسوم على تصميم وفق السلّم 1/10000 ، أي أنّ كلّ 1 cm على التصميم يمثّل 10 000 cm في الواقع ، وأطوال قطعه الأربع على التصميم بالصنتمتر هي:
AB = 3
BC = 5
CD = 10
DE = 6
ما الطول الحقيقي للمضمار بالمتر ؟»
- Q7 option a `misconceptionTag` : (muette) → math.num.puissance-de-dix-rangs-mal-comptes
- Q7 option c `misconceptionTag` : (muette) → math.num.puissance-de-dix-rangs-mal-comptes
- Q7 option d `misconceptionTag` : (muette) → math.alg.reponse-a-l-autre-inconnue
- Q7 `explanation` → «طول المضمار على التصميم 3 + 5 + 10 + 6 = 24 cm. والسلّم 1/10000 يعني أنّ 1 cm على التصميم يمثّل 10 000 cm في الواقع ، فالطول الحقيقي 24 × 10 000 = 240 000 cm. ونحوّل إلى المتر بالقسمة على 100 لأنّ 1 m = 100 cm ، فنجد 240 000 ÷ 100 = 2400 m ✓. الخطأ الشائع: ترك النتيجة بالصنتمتر وقراءتها بالمتر فنجد 240 000 ؛ أو القسمة على 10 بدل 100 عند التحويل فنجد 24 000 ؛ أو القسمة على 1000 فنجد 240.»

#### 35 — `35-examen-2002-ex4-cercle-pythagore-milieux-orthocentre-thales-gravite.json`
- `title` : `🏛️ مناظرة 2002 · التمرين 4 ⭐⭐⭐⭐: مسألة دائرة مركزها B — فيثاغورس وعكسه والمستقيم الرابط بين منتصفين والمركز القائم وطاليس ومركز الثقل` → `🏛️ مناظرة 2002 · التمرين 4 ⭐⭐⭐: مسألة دائرة مركزها B — فيثاغورس وعكسه والمستقيم الرابط بين منتصفين والمركز القائم وطاليس والتناظر المركزي`
- `difficulty` : `4` → `3`
- `mode` : `challenge` → `boss`
- `xpReward` : `300` → `120`
- `rewardCoins` : `60` → `30`
- Q1 option a `misconceptionTag` : (muette) → math.geo.segment-mal-choisi
- Q2 option a `misconceptionTag` : (muette) → math.geo.position-relative-ignoree
- Q2 option d `misconceptionTag` : (muette) → math.geo.position-relative-ignoree
- Q3 `explanation` → «المثلّث ACF قائم في A لأنّ F من المستقيم (AB) العمودي على (AC) ، ووتره [CF] ، فبنظرية فيثاغورس CF² = AC² + AF² = 16 + 64 = 80. ومنه CF = √80 = √(16 × 5) = 4√5 cm ✓ بإخراج العامل 16 من تحت الجذر بجذره 4. الخطأ الشائع: جمع الطولين فنجد 4 + 8 = 12 ؛ أو التوقّف عند CF² = 80 ؛ أو إخراج 16 من تحت الجذر دون أخذ جذره فنجد 16√5 بدل 4√5.»
- Q4 option b `misconceptionTag` : (muette) → math.geo.segment-mal-choisi
- Q5 `difficulty` : 3 → 2
- Q5 `explanation` → «نربّع الأطوال الثلاثة: EC² = (2√5)² = 4 × 5 = 20 و CF² = (4√5)² = 16 × 5 = 80 و EF² = 10² = 100. مربّع الضلع الأطول [EF] وحده في طرف ، و EC² + CF² = 20 + 80 = 100 = EF² ، فبعكس نظرية فيثاغورس المثلّث EFC قائم ووتره [EF] ، أي قائم في C ✓. الخطأ الشائع: تربيع الجذر وحده وترك العامل ، أي حساب 2 × 5 = 10 بدل 4 × 5 = 20 ، و 4 × 5 = 20 بدل 16 × 5 = 80 ، ثمّ 10 + 20 = 30 ≠ 100 ، فيُظنّ المثلّث غير قائم ؛ أو اختيار وتر غير [EF] فيُنسب التعامد إلى الرأس E أو F.»
- Q6 `difficulty` : 3 → 2
- Q7 `difficulty` : 3 → 2
- Q8 `prompt` : seule la figure SVG change (voir § Figures)
- Q8 `difficulty` : 3 → 2
- Q9 `difficulty` : 3 → 2
- Q9 option c `misconceptionTag` : (muette) → math.geo.segment-mal-choisi
- Q9 `explanation` → «(EB) و (CH) يتقاطعان في A بين E و B وبين C و H ، و (BH) ∥ (EC) ، فنحن في وضعية الفراشة برأس A: المثلّثان AEC و ABH متقابلان بالرأس A ، و B يقابل E و H يقابل C. فنسب طاليس AB/AE = AH/AC = BH/EC ✓ ، أي BH/EC = AB/AE. الخطأ الشائع: قلب النسبة فنكتب AE/AB ؛ أو أخذ القطعة الكاملة [EB] بدل الجزء [AE] ، فنكتب AB/EB أو AE/EB ، وهي نسب لا تساوي BH/EC.»
- Q10 `difficulty` : 3 → 2
- Q10 option a `misconceptionTag` : (muette) → math.geo.segment-mal-choisi
- Q12 option d `misconceptionTag` : (muette) → math.geo.position-relative-ignoree

### Figures
- **35 Q8** — remplacer tout le `<svg>…</svg>` du `prompt` par :

```
<svg viewBox="0 0 320 276"><title>المثلّث BCF والمستقيمان (BK) و (CA) المتقاطعان في H</title><polygon points="160,118 88,22 280,118" fill="#0f6e56" fill-opacity="0.08"/><path d="M40 118 L160 118" fill="none" stroke="#64748b" stroke-width="2" stroke-linecap="round"/><polygon points="160,118 88,22 280,118" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linejoin="round"/><path d="M184 70 L88 262" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/><path d="M88 22 L88 262" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/><path d="M179.53 78.94 L188.47 83.42 L192.94 74.47" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M99 118 L99 107 L88 107" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="88" cy="118" r="3.8"/><circle cx="160" cy="118" r="3.8"/><circle cx="88" cy="22" r="3.8"/><circle cx="40" cy="118" r="3.8"/><circle cx="280" cy="118" r="3.8"/><circle cx="184" cy="70" r="3.8"/><circle cx="88" cy="262" r="3.8"/></g><g font-size="15" font-weight="700" direction="ltr" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="75" y="111" text-anchor="middle" fill="#0f172a">A</text><text x="164" y="107" text-anchor="middle" fill="#0f172a">B</text><text x="74" y="22" text-anchor="middle" fill="#0f172a">C</text><text x="37" y="138" text-anchor="middle" fill="#0f172a">E</text><text x="293" y="123" text-anchor="middle" fill="#0f172a">F</text><text x="197" y="64" text-anchor="middle" fill="#0f172a">K</text><text x="102" y="267" text-anchor="middle" fill="#0f172a">H</text></g></svg>
```
- **33 Q5** — dans le `<svg>` du `prompt`, remplacer `<text x="166" y="194" text-anchor="middle" fill="#64748b">4 cm</text>` par `<text x="120" y="166" text-anchor="middle" fill="#64748b">4 cm</text>`.
- **Nouvelle étiquette (registre, hors fichiers de l'auteur)** : `math.geo.pythagore-reciproque-role` (textes ci-dessus), puis 30 Q1 a et 33 Q1 c → cette étiquette.
- **Rebasage** : `math.geo.segment-mal-choisi` et `math.geo.position-relative-ignoree` n'existent que sur `origin/main` (pas dans l'arbre de travail).

## Vérification des correctifs (copies hors dépôt)
Sur les six fichiers corrigés : clés inchangées et re-résolues (31 Q4 = 3/4 = MN/AD ; 33 Q4 = 1,25 = MN/BC ; 34 Q2 = 3 + 5 = 8 ; 32 Q8 = 189 000 ÷ (31,5 × 100) = 60) ; tous les distracteurs faux en valeur (34 Q3 b : 1/2, 1/2, 2 ; 34 Q1 c faux) ; clé strictement la plus longue 0/48 (fonction `longestKey` du moteur et mesure sans diacritiques) ; aucune option somme/différence ; plans 2×2 de 30 Q1, 33 Q3, 34 Q1 parfaits, vote de 34 Q3 sans majorité ; `nearPairs` du moteur sur tout `math` (2 107 items) : 0 paire impliquant la tranche ; aucune fuite en avant (ordre d'émission = ordre du fichier) ; 32 Q8 n'imprime plus 3150 ; aucune référence à un dessin dans un énoncé sans figure ; balayage notation 0 ; rendu Chromium `dir=rtl` 760/340 px : 0 chaîne brouillée ; figures : `check-figures` ✓, `check-overflow` ✓ (31), 35 Q8 exacte (BK·CF = 0, BC = BF = BE = 5 u, H ∈ (BK), AH = 6 u). Étiquettes employées : toutes présentes sur `origin/main`.
