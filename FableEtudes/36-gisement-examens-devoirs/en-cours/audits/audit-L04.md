# Audit indépendant — lot L04, maths 9ᵉ, chapitre 04 (missions 17 à 22, sujets 2001 à 2007, exercice 1)

J'ai suivi `gisement-auditeur.md` après avoir invoqué le skill `content-audit` (quality-bar, math-and-notation, audit-correction, rewards-and-modes, schéma multi/numeric). Chaque clé a été re-résolue à l'aveugle avant d'ouvrir la clé du fichier, puis tout a été recalculé par sympy : valeurs, encadrements, développements, factorisations, racines, intervalles, et les ensembles exacts des `multi` et des `numeric`.

- **Sources lues** : les transcriptions 2001, 2002, 2003, 2005, 2006 et 2007 ; les cours 03, 04 et 17 et les missions 01 à 16 du chapitre 04 sur `origin/main` ; les missions d'examen 03/15 à 20 et 17/09 à 16 ; le manifeste et la fiche programme de 9ᵉ.
- **Registre** : relu sur `origin/main` au commit 1bdffbf9 (#601 inclus, copie identique vérifiée). Aucune des douze étiquettes de #601 ne convient à une option muette de la tranche.
- **Rendu** : les 323 chaînes de la tranche sont passées dans `isolateLtrRuns` du moteur puis dans un algorithme bidi Unicode (bidi-js).
- **Gates** : `content:qa` ne signale rien sur les six fichiers. `content:tranche` sur le chapitre 04 donne 0 clé strictement la plus longue parmi les 32 QCM de la tranche et aucune paire proche qui touche la tranche.
- **Rien ouvert d'interdit** : ni `/tmp/claude-0/`, ni `sources-externes/`, ni le `cours.md` 04 modifié dans l'arbre de travail.
- **Aucun fichier modifié.**

## Tableaux par fichier

**17 — 2001** : d3, boss 120/30, displayOrder 17, titre au bon format

| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 (multi) | {a, c} | {a, c} | réserve m10 | A(1) = −1, A(1/2) = −3/2 ; b et d exécutent 2 − x |
| 2 | a | a | **ERREUR C1** | b « −3 ≤ A ≤ 5 » est aussi un encadrement vrai, car A ∈ [−3 ; 1] |
| 3 | b | b | réserve M2, m3 | vote majoritaire ; c devrait être étiquetée |
| 4 (numeric) | 1 | 1 | OK | valeur exacte, sans tolérance |
| 5 | d | d | réserve m7 | l'explication de a passe par une factorisation de trinôme non enseignée |
| 6 | c | c | OK | plan 2×2 équilibré |

**18 — 2002**

| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | a | a | réserve M4 | (−5 ; 1) ; l'étiquette de b renvoie à f(x) |
| 2 (numeric) | 2,5 | 2.5 | OK | valeur exacte |
| 3 | d | d | réserve m2 | l'étiquette de a est inexacte |
| 4 | c | c | réserve M2, m2 | 8x² − 20x ; vote ; arbitrage de l'étiquette de d |
| 5 | b | b | réserve M2 | 4x(2x − 5) ; vote ; étiquettes manquantes |
| 6 | a | a | OK | {0 ; 5/2} ; lien avec Q2 inhérent au sujet |

**19 — 2003**

| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | b | b | réserve M4 | (8 ; 1/2) ; c n'exécute « 3x lu 3 + x » qu'en x = 2 |
| 2 | a | a | réserve m13 | [−2/3 ; +∞[ |
| 3 | d | d | réserve **M3** | quasi-doublon du quiz publié Q5 |
| 4 (multi) | {a, d} | {a, d} | réserve m9, m10 | pluriel pour deux produits ; nombre de bonnes réponses déductible |
| 5 | b | b | réserve M2, m2 | 3x² + 2x |
| 6 | b | b | réserve M2 | x(3x + 2) |
| 7 (multi) | {a, b} | {a, b} | réserve m11 | 3/2 n'est pas justifié dans l'explication |

**20 — 2005**

| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | b | b | réserve M4 | (5 ; 1) |
| 2 | a | a | réserve m8 | −3/2 ; une phrase de l'explication est fausse |
| 3 | c | c | réserve M2 | 10x² + 7x − 12 |
| 4 | a | a | réserve m4 | 12 − 7x ; b et c sans étiquette |
| 5 | d | d | réserve m13 | [2 ; +∞[ |
| 6 | b | b | OK (m15 optionnel) | figure juste : cercle plein en 2, flèche à gauche |

**21 — 2006**

| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | b | b | réserve M4 | (1 ; −1/2) |
| 2 | a | a | OK | x ≥ 2/3 |
| 3 | d | d | réserve M2 | a s'élimine à vue, car l'énoncé donne B |
| 4 | c | c | **réserve M1**, m14 | l'option d se rend brouillée ; b s'élimine à vue |
| 5 | b | b | réserve M2, m18 | 2(3x − 2)(x − 2) |
| 6 | d | d | OK | 2×2 équilibré |

**22 — 2007**

| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | b | b | réserve m2 | 2x − 4 ; arbitrage de l'étiquette de d |
| 2 | a | a | OK | (−4 ; −6) |
| 3 | c | c | OK | ]−∞ ; 2] |
| 4 | d | d | réserve m12 | vocabulaire ; même cas que le « vérifie » du cours |
| 5 | d | d | OK | (2x − 4)(3x + 2) |
| 6 (multi) | {a, d, e} | {a, d, e} | OK | 6x² − 8x − 8 vérifié |
| 7 | d | d | OK | l'étage d3 est surévalué, voir la section étages |

## Défauts classés

### CRITIQUE

**C1 — 17 Q2 : deux options sont vraies.** En retirant « مداه 4 » de l'énoncé, l'option b « −3 ≤ A ≤ 5 » devient un encadrement vrai : l'intervalle [−3 ; 1] est inclus dans [−3 ; 5]. C'est la définition même du cours 17 (« a ≤ X ≤ b »). L'explication le reconnaît (« وهذا حصر مداه 8 »). La question « ما الحصر الصحيح » a donc deux réponses défendables.

Correctif :
- Garder l'énoncé tel quel.
- Option b → `−1 ≤ A ≤ 1`, laissée muette (2 retranché de la borne haute seule ; faux, car x = −1 donne A = −3).
- Dans l'explication, remplacer la dernière phrase « أمّا طرح 2 من الحدّ الأدنى وجمعه إلى الأعلى فيعطي −3 ≤ A ≤ 5 وهذا حصر مداه 8 فيوسّع الحصر الأصلي بلا مبرّر. » par :
  « أمّا طرح 2 من الحدّ الأعلى وحده فيعطي −1 ≤ A ≤ 1 ، وهو حصر خاطئ لأنّ x = −1 يعطي A = −3 وهي قيمة خارجه. »

Vérifications faites : une seule option vraie. Le vote reconstruit b, pas la clé. Longueurs 11/11/11/10, donc la clé n'est pas la plus longue. Rendu vérifié. Rétablir « مداه 4 » ne suffirait pas : aucune erreur naturelle ne donne un encadrement faux d'amplitude 4.

### MAJEUR

**M1 — 21 Q4 : rendu brouillé.** Dans l'option d et dans la fin de l'explication, « −x + 1 » s'affiche « x + 1− » et « −x − 1 » s'affiche « x − 1− ». Un signe collé à une lettre n'est pas isolé, ce que confirme la simulation bidi.
- Option d → `في السطر الأخير خطأ لأنّ (2x − 3) − (3x − 2) = −x + 1` (rendu vérifié ; 50 caractères, contre 61 pour la clé).
- Explication : remplacer « و (2x − 3) − (3x − 2) تساوي فعلًا −x − 1 وهذا لا خطأ فيه. » par « والسطر الأخير سليم لأنّ (2x − 3) − (3x − 2) = −x − 1 فعلًا ، ولا خطأ فيه. »

**M2 — vote majoritaire (8 questions).** Dans chacune de ces questions, chaque distracteur ne change qu'un seul terme de la clé. Le vote terme à terme reconstruit donc la clé sans aucun calcul. Correctif commun : un plan 2×2, en remplaçant un distracteur par une option à deux erreurs, laissée muette. J'ai vérifié par sympy que chaque option nouvelle est fausse et distincte des autres ; aucune ne devient la plus longue.

| Q | Option → nouveau texte | Étiquettes | Explication : remplacer … par … |
|---|---|---|---|
| 17 Q3 | d `(2 − x)(2 + x)` → `(x − 4)²` | c ← existante `math.alg.difference-carres-second-terme-non-eleve-au-carre` | « ، أو قلب الحدّين فيُكتب (2 − x)(2 + x) وهو ينشر إلى 4 − x² فيخالف B في الإشارة. » → « ، وقد يجتمع الخطآن فيُكتب (x − 4)² وهو ينشر إلى x² − 8x + 16 فلا يساوي العبارة B أصلًا. » |
| 18 Q4 | b `8x² + 5x − 25` → `8x⁴ − 20x + 50` | d → `signe-ignore-dans-somme` | supprimer « ، أو جمع −20x مع 25 بمعاملَيهما فيخرج 5x وهما حدّان غير متشابهين » ; remplacer le point final par « ، وقد يجتمع الخطآن فتخرج الكتابة 8x⁴ − 20x + 50 الخاطئة مرّتين. » |
| 18 Q5 | d `4x(2x + 5)` → `4(2x − 20)` | a ← T6g, c ← T2 (voir tableau des nouvelles étiquettes) | « ، أو فقدان إشارة الطرح فيخرج 4x(2x + 5) … الحدّ الثاني. » → « ، وقد يجتمع الخطآن فيخرج 4(2x − 20) وهذا ينشر إلى 8x − 80 فلا يساوي العبارة B أصلًا. » |
| 19 Q5 | c `3x² + 2x + 2` → `3x⁴ + 6x` | a ← T1 | « ، أو جمع الحدّين الثابتين 1 و 1 … حدّ ثابت زائد. » → « ، وقد يجتمع الخطآن فتخرج الكتابة 3x⁴ + 6x الخاطئة مرّتين. » |
| 19 Q6 | c `x(3x + 2x)` → `x(3x² − 2)` | a ← T3, d ← T2 | tout le passage « أمّا الخطأ الشائع … الحدّ الثاني. » → « أمّا الخطأ الشائع فهو ترك الحدّ 3x² دون قسمته على x فيخرج x(3x² + 2) وهو ينشر إلى 3x³ + 2x ، أو فقدان إشارة الجمع فيخرج x(3x − 2) وهو ينشر إلى 3x² − 2x ، وقد يجتمع الخطآن فتخرج الكتابة x(3x² − 2) الخاطئة مرّتين. » |
| 20 Q3 | b `10x² − 7x − 12` → `10x² + 12` | d ← règle des signes (m5) | « ، أو خطأ في إشارة أحد الجداءات … حدّ واحد. » → « ، أو جعل الجداء 3 × (−4) موجبًا فيخرج +12 بدل −12 ، وقد يجتمع الخطآن فتخرج الكتابة 10x² + 12 الخاطئة مرّتين. » |
| 21 Q3 | a `6x² − 9x` → `6x² − 9x + 4x − 6` | c ← règle des signes (m5) | « أمّا الخطأ الشائع فهو توزيع 3x وحدها … وهو سالب. » → « أمّا الخطأ الشائع فهو جعل الجداء (−2) × (−3) سالبًا فيخرج −6 بدل 6 ، أو خطأ في إشارة الجداء (−2) × 2x فيظهر الحدّ 4x موجبًا وهو سالب ، وقد يجتمع الخطآن إذا عومل −2 كأنّه 2 فيخرج 6x² − 9x + 4x − 6 ، وهو نشر الجداء (3x + 2)(2x − 3) لا الجداء المطلوب. » |
| 21 Q5 | c `2(3x − 2)(x − 4)` → `(3x − 2)(x + 2)` | a ← T6g, d ← T3 | « ، أو قسمة الحدّ الأوّل وحده على 2 فيخرج (x − 4) ، أو فقدان إشارة الطرح داخل القوس فيتغيّر الحدّ الثاني من القوس الأخير. » → « ، أو فقدان إشارة الطرح داخل القوس فيخرج (x + 2) بدل (x − 2) ، وقد يجتمع الخطآن فتخرج الكتابة (3x − 2)(x + 2) الخاطئة مرّتين. » |

**M3 — 19 Q3 est un quasi-doublon du quiz publié Q5.** Le quiz demande le même cas (x ≥ −3) avec les mêmes quatre gabarits d'options (cercle ouvert ou plein × flèche à gauche ou à droite), la même clé (plein, à droite) et la même explication. 22 Q4 reprend en plus le même squelette.

Correctif : transformer 19 Q3 en QCM visuel.
- Énoncé : `مجموعة حلول المتراجحة التالية هي المجال المكتوب تحتها:\n3x + 2 ≥ 0\n[−2/3 ; +∞[\nأيّ رسم يمثّل هذه المجموعة على المستقيم المدرّج ؟`, sans figure dans l'énoncé.
- Quatre options SVG. Clé d = cercle plein et flèche à droite. Code exact de d :

`<svg viewBox="0 0 360 92"><title>تمثيل على مستقيم مدرّج</title><line x1="14" y1="50.0" x2="336" y2="50.0" stroke="#1f2937" stroke-width="2"/>`+ les cinq graduations et libellés actuels (−2, −1, 0, 1, 2 en x = 30.0 / 101.5 / 173.0 / 244.5 / 316.0, copiés tels quels) +`<line x1="125.3" y1="50.0" x2="334" y2="50.0" stroke="#b91c1c" stroke-width="5" stroke-linecap="round"/><polygon points="346,50.0 334,44.0 334,56.0" fill="#b91c1c"/><circle cx="125.3" cy="50.0" r="6.5" fill="#b91c1c" stroke="#b91c1c" stroke-width="2.6"/>`+ le libellé actuel `−2/3` en (125.3 ; 32.0) +`</svg>`

- Le SVG de d supprime la pointe noire de l'axe (elle se confondait avec la flèche de solution) et la barre rouge à −2/3.
- Les trois autres options, par différence avec d :
  - b = d avec `fill="#ffffff"` sur le cercle (cercle ouvert, flèche à droite).
  - c = d avec la demi-droite à gauche : `<line x1="26" y1="50.0" x2="125.3" …/>` et `<polygon points="14,50.0 26,44.0 26,56.0" …/>`.
  - a = c avec `fill="#ffffff"` sur le cercle.
- Longueurs 2156, 2160, 2156, 2160 : la clé est à égalité, pas la plus longue.
- Étiquettes : b garde `intervalle-borne-mal-incluse` ; c reçoit T4 si elle est créée ; a reste muette. L'explication actuelle convient telle quelle.

**M4 — `math.fn.image-calculee-par-somme` sur 18 Q1 b, 19 Q1 c, 20 Q1 d, 21 Q1 c.** Son libellé montre « f(x) = 3x ». Or la notation fonctionnelle est absente du programme de 9ᵉ (fiche maths : « aucune notation f(x) »). En outre sa compétence `math.fn.fonction-lineaire` relève du chapitre 06, marqué hors programme. Correctif : remplacer par `math.num.operation-inverse-appliquee`, dont le libellé dit exactement « une somme au lieu d'un produit ». Autre possibilité, à la main de l'orchestrateur : réécrire le libellé sans f(x).

### MINEUR

- **m1 — Étages** : voir la section suivante. Il faut changer les en-têtes de 17, 18, 19, 21 et 22.
- **m2 — Étiquettes, arbitrages demandés :**
  - 18 Q3 a (4x² − 25) → `math.alg.difference-carres-confondue`. C'est le carré de différence écrit a² − b² ; `carre-somme-sans-double-produit` n'explique pas le −25 et reste exacte pour b.
  - 18 Q4 d, 19 Q5 c et 22 Q1 d → `math.int.signe-ignore-dans-somme`. Le signe moins d'un terme est perdu dans une somme algébrique ; c'est cohérent avec 19 Q5 d, et c'est ce que nomme l'explication de 22 Q1.
  - 21 Q3 a : `distribution-partielle` est exacte (le facteur 2x − 3 n'est multiplié que par 3x). Mais l'option s'élimine à vue puisque B est donné, et M2 la remplace.
- **m3 — 17 Q3 c** : option muette qui mérite l'étiquette existante `math.alg.difference-carres-second-terme-non-eleve-au-carre`. La nouvelle étiquette 13 est inutile.
- **m4 — 20 Q4 b et c** : élargir le libellé de `moins-devant-parenthese` à « Tu n'appliques le signe moins qu'à une partie des termes de la parenthèse : il change le signe de TOUS les termes ». Le libellé reste exact pour les usages existants ; étiqueter ensuite b, c et d.
- **m5 — Règle des signes** : élargir le libellé de `math.int.produit-signes-negatifs` à « produit ou quotient : même signe → positif ; signes contraires → négatif ». Cela couvre 21 Q3 b et c, 20 Q3 d, 20 Q5 c et 20 Q6 d, à la place des nouvelles étiquettes 5 et 17.
- **m6 — `transposition-sans-changer-signe`** : le libellé dit « égalité », mais trois de ses quatre usages portent sur une inéquation (19 Q2 c, 21 Q2 c, 22 Q3 a). Élargir à « égalité ou inégalité ».
- **m7 — 17 Q5, explication de a** : remplacer « ومن نشر ثمّ عكس إشارتي العاملين كتب (x − 3)(x + 2) … الحدّ الأوسط. » par « أمّا (x − 3)(x + 2) فتبادل فيه العددان 2 و 3 موضعيهما، وهو ينشر إلى x² − x − 6 فتختلف إشارة الحدّ الأوسط. »
- **m8 — 20 Q2** : « قسمة 2 على 3 » donne 2/3, pas −2/3. Remplacer « أو قسمة 2 على 3 بدل قسمة −3 على 2 فيخرج الكسر مقلوبًا. » par « أو قسمة المعامل 2 على −3 بدل قسمة −3 على 2 فيخرج الكسر مقلوبًا. »
- **m9 — 19 Q4 et Q5, pluriel pour deux objets** : « نعتبر الجداءات التالية » → « نعتبر الجداءين التاليين » ; « كلًّا منها » → « كلًّا منهما » ; en Q5, « بعد نشر الجداءات » → « بعد نشر الجداءين ».
- **m10 — Multi 17 Q1 et 19 Q4** : une seule écriture juste par valeur de x ou par produit, donc le nombre de bonnes réponses se déduit. Ajouter une écriture juste équivalente :
  - 17 Q1 e `x = 1/2 ⟹ A = −1,5`, bonnes réponses {a, c, e} ;
  - 19 Q4 f `(x − 1)² = 1 − 2x + x²`, bonnes réponses {a, d, f} ;
  - compléter les deux explications.
- **m11 — 19 Q7** : ajouter avant « ؛ أمّا الخطأ الشائع » : « ، و 3/2 يعطي 3x + 2 = 13/2 وهو غير معدوم كذلك ».
- **m12 — 22 Q4** : le cours réserve « التظليل » aux intervalles bornés ; pour une demi-droite il parle de flèche. Dans les options, « والتظليل نحو الأعداد الأكبر/الأصغر من 2 » → « وسهم نحو الأعداد الأكبر/الأصغر من 2 ». Dans l'explication, « فنظلّل الجهة التي تقع على يسار هذه النقطة » → « فنرسم السهم نحو الأعداد الأصغر من 2 أي إلى يسار هذه النقطة », et « أو تظليل الجهة المعاكسة » → « أو رسم السهم في الجهة المعاكسة ». Pour mémoire, ce cas est mot pour mot le « vérifie » du cours 04.
- **m13 — 19 Q2 et 20 Q5** : l'énoncé demande un ensemble ou un intervalle, les options disent « x ∈ … ». Écrire l'intervalle seul, comme en 22 Q3.
- **m14 — 21 Q4 b, facultatif** : b s'élimine à vue. Proposition : `بعد إخراج (3x − 2) لا يبقى من الحدّ الأخير شيء فيُحذف من المعقوفين` (reste oublié, étiquette T7/16 ; rendu vérifié ; plus courte que la clé).
- **m15 — 20 Q6, facultatif** : trois options disent « خاطئ » ; la seule « صحيح » (c) s'écarte par vote.
- **m18 — 21 Q5** : « التفكيك الأتمّ » → « التفكيك الأتمّ (التعميل التامّ) », pour reprendre le terme du cours 03.

### Hors périmètre, mais qui touche la tranche

- **H1 — Convention de représentation.** Le manuel CNP (ch. 7, p. 98 et 101) représente un intervalle sur la droite graduée par des crochets. Le cours 04 publié enseigne cercle plein ou vide et flèche. 19 Q3, 20 Q6 et 22 Q4 suivent le cours, donc ils sont enseignés dans l'app, mais pas la convention qu'attend l'examen. À traiter dans le cours 04. Je n'ai pas ouvert sa version en cours de modification ; si elle passe aux crochets, ces trois items et le quiz Q5 devront suivre.
- **H2 — Cours 03.** Le cours ne montre pas le cas « un terme égal au facteur commun laisse 1 », que testent 17 Q4 et Q5 et 21 Q4. Le cas se déduit du cours et 17 Q4 l'amène en échafaudage.

## Étages (avis)

La position d3 est mal calibrée pour cinq missions. L'exercice 1 d'examen (4 points) enchaîne des techniques élémentaires ; les missions d'examen « exercice 1 » déjà publiées (03/15 et 03/16) sont d2 practice ; et 17, 19 et 21 ne contiennent aucune question d3.

| Mission | Étage recommandé | Rampe par question |
|---|---|---|
| 17 | d2 practice 75/15 ⭐⭐ | [1, 1, 1, 1, 2, 2] |
| 18 | d2 | [1, 1, 1, 2, 2, 3] |
| 19 | d2 | [1, 2, 2, 2, 2, 2, 2] |
| 20 | d3 boss défendable, la seule | [1, 1, 2, 2, 3, 3] |
| 21 | d2 | [1, 2, 2, 2, 2, 2] |
| 22 | d2 | [2, 2, 2, 2, 2, 2, 2] (Q7 passe de d3 à d2) |

Pour 20, les deux étapes d3 sont réelles : Q5 divise par −7 avec retournement du sens, et Q6 juge une représentation qui en dépend. Un passage en d2 reste possible avec la même rampe.

Contraintes à respecter pour ne pas créer de fuite : une question dont l'énoncé redonne la clé de la précédente ne doit jamais descendre sous elle. Cela vaut pour :
- 17 : Q4 ≥ Q3, Q6 ≥ Q5 ;
- 18 : Q4 ≥ Q3, Q5 ≥ Q4, Q6 ≥ Q5 ;
- 19 : Q3 ≥ Q2, et de Q4 à Q7 chacune ≥ la précédente ;
- 20 : Q4 ≥ Q3, Q6 ≥ Q5 ;
- 21 : Q5 ≥ Q4, Q6 ≥ Q5 ;
- 22 : Q2 ≥ Q1, Q4 ≥ Q3, Q6 ≥ Q5, Q7 ≥ Q6.

Piège concret : 22 Q2 est honnêtement d1, mais la passer sous Q1 ferait fuir A = 2x − 4. Les rampes proposées respectent toutes ces contraintes.

## Fidélité, liens et fuites

- **Fidélité** : toutes les données sont conformes aux transcriptions et aucune sous-question n'est perdue.
  - L'écart (a) de l'auteur (« مداه 4 » retiré) déforme le sujet : c'est C1.
  - Les découpages (b) sont fidèles ; chaque morceau redonne le résultat précédent.
- **Liens inhérents (c)** : ce sont des dévoilements partiels voulus par le sujet, pas des fuites en avant.
  - 2002 Q2 → Q6 : 5/2 élimine b et d ; il reste le piège du 0. Amélioration facultative : Q6 b → `{ −4 ; 5/2 }`.
  - 2003 Q2 → Q7 (−2/3) : le multi teste encore la racine 0.
  - 2006 Q2 → Q6 (2/3) et 2007 Q3 → Q7 (2) : chacun ramène la question à un seul axe, sans livrer la clé.
- **Fuites** : aucune explication ne résout une question suivante, aucune décimale de vérification ne livre un verdict, aucun énoncé n'annonce le nombre de valeurs.

## Étiquettes

**Étiquettes existantes employées** (19 identifiants, 49 occurrences) : elles sont exactes, sauf :
- M4 (4 options) ;
- 18 Q3 a, 18 Q4 d, 19 Q5 c et 22 Q1 d (voir m2) ;
- les nuances de libellé de m6 ;
- `intervalle-borne-mal-incluse` posée sur un cercle ou sur « x > 2/3 » : acceptable (le cours fait correspondre crochet et cercle), élargissement facultatif du libellé.

**Options muettes à étiqueter avec l'existant** : 17 Q3 c ; 20 Q4 b et c (après m4) ; 20 Q3 d, 21 Q3 c, 20 Q5 c et 20 Q6 d (après m5).

**Options à deux erreurs laissées muettes** : je confirme les huit citées (18 Q6 d, 19 Q1 d, 19 Q2 d, 20 Q1 a, 20 Q2 c, 21 Q2 d, 22 Q2 d, 22 Q3 d). Il faut y ajouter 19 Q3 a et 22 Q4 a, sur lesquelles l'auteur proposait l'étiquette 4.

**Les 18 étiquettes proposées par l'auteur** — occurrences réelles dans les fichiers actuels, puis avis :

| # | Étiquette | Occurrences réelles | Avis |
|---|---|---|---|
| 1 | termes-semblables-exposants-additionnes | 2 (18 Q4 a, 19 Q5 a) | exacte → créer (T1) |
| 2 | facteur-commun-terme-non-divise | **5** (+ 17 Q5 b, oubliée) | exacte → créer (T2) ; 3 après M2 |
| 3 | facteur-commun-signe-change | 3 | exacte → créer (T3) ; 2 après M2 |
| 4 | inequation-demi-droite-sens-inverse | 2 réelles (19 Q3 c, 22 Q4 c ; les options a ont deux erreurs) | → créer (T4) |
| 5 | quotient-signes-negatifs | 2 | plutôt élargir `produit-signes-negatifs` (m5) |
| 6 | facteur-commun-lettre-oubliee | 1 | généraliser en « facteur divisé mais pas écrit » avec 21 Q5 a → 2 → créer (T6g) |
| 7 | facteur-commun-reste-un-oublie | 1 | fusionner avec 16 → 2 (17 Q5 c, 22 Q5 b) → créer |
| 8 | developpement-produits-croises-oublies | 1 | non |
| 9 | signe-de-x-ignore-dans-produit | 1, chemin ambigu | non |
| 10 | soustraction-ordre-inverse | 1 en QCM (17 Q1 b et d sont dans un multi, sans étiquette possible) | non |
| 11 | encadrement-operation-oubliee | 1 | non |
| 12 | encadrement-operations-opposees-aux-bornes | 1, et l'option est vraie (C1) | non |
| 13 | difference-carres-racine-non-prise | 1 | non, l'existante suffit (m3) |
| 14 | difference-carres-ordre-inverse | 1 | non |
| 15 | factorisation-somme-devenue-produit | 1 | non |
| 16 | facteur-commun-terme-oublie | 1 | fusion avec 7 |
| 17 | produit-positif-negatif | 2 (+ 21 Q3 c, oubliée) | plutôt m5 |
| 18 | trinome-signes-inverses | 1 | non : nommerait une technique non enseignée |

Nota : le schéma demande au moins 3 questions distinctes pour étendre le registre. T1, T4, T6g et la fusion 7+16 n'en ont que 2 ; c'est à l'orchestrateur de trancher.

## Doublons, rendu, figures, en-têtes, chapter.json

- **Doublons** :
  - avec le chapitre 04 publié : M3 et m12 ; les questions de produit nul reprennent le gabarit de 04/01, 02, 03, 05 et 15 sur d'autres données, ce qui est acceptable ;
  - à l'intérieur de la tranche : les Q1 « valeur en deux points », 19 Q2 et 21 Q2, 17 Q6 et 21 Q6 partagent des gabarits d'annales voisines sur des données différentes, ce qui est acceptable ;
  - avec les missions d'examen 03/15 à 20 et 17/09 à 16 : aucun recouvrement.
- **Rendu** : le seul défaut est M1. Aucun chiffre arabo-indien, trait d'union, LaTeX, virgule arabe entre crochets, nombre coupé, parenthèse d'unité ou point final collé à une formule.
- **Figures** (19 Q3, 20 Q6, 22 Q4) : exactes (−2/3 en x = 125.3, 2 en x = 173 ou 208.8), aucune ne donne la clé, arabe seulement dans `<title>`, uniquement des éléments et attributs admis.
- **En-têtes** : titres au format « 🏛️ مناظرة <année> · التمرين 1 ⭐… », sujets sans résultat, displayOrder 17 à 22 contigus ; seuls les étages changent (m1).
- **chapter.json** : par rapport à `main`, seule la ligne `sources[]` est ajoutée, identique à celle des chapitres 03, 07, 09 et 17.

## Chiffre final

- **Questions auditées** : 38 (32 QCM, 4 multi, 2 numeric), toutes re-résolues à l'aveugle.
- **Clés fausses** : 0.
- **Défauts** : 1 critique (C1), 4 majeurs (M1 à M4, sur 14 questions), 16 mineurs (m1 à m15 et m18).
- **Questions à reprendre pour critique ou majeur** : 15.
  - 11 en contenu : 17 Q2, 17 Q3, 18 Q4, 18 Q5, 19 Q3, 19 Q5, 19 Q6, 20 Q3, 21 Q3, 21 Q4, 21 Q5.
  - 4 en étiquette seule : 18 Q1, 19 Q1, 20 Q1, 21 Q1.
  - S'y ajoutent les mineurs : explications et langue de 17 Q5, 20 Q2, 19 Q7, 19 Q4 et Q5 ; multi 17 Q1 et 19 Q4 ; 22 Q4 ; 19 Q2 et 20 Q5 ; étiquettes 18 Q3 a, 18 Q4 d, 19 Q5 c, 22 Q1 d, 17 Q3 c, 20 Q4 b et c ; en-têtes de cinq missions.
- **Verdict** : la tranche ne part pas en l'état à cause de C1. Je re-vérifierai les correctifs de l'auteur.