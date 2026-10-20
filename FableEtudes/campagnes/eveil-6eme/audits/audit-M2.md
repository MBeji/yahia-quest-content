# Audit M2 — missions du gisement, éveil 6ᵉ (`02` 06–07, `03` 06–11, `10` 06–07)

> Auditeur indépendant (opus), 2026-10-20. Fichiers lus dans `/home/user/wt-ev6/content/` (pas de git : état du disque à cette date, ré-auditer si les fichiers bougent).
> Méthode suivie : chaque question a été re-résolue à l'aveugle (énoncé et options d'abord, clés ensuite) ; confrontation aux transcriptions `examens-nationaux/6eme-base/eveil/` et aux PDF (2016 à 150, 400 et 800 dpi, 2025 à 110 dpi) ; cours et exercices `01`–`05` + quiz des trois chapitres relus pour le croisement « ne pas redemander » ; rendu Chromium à 360 px, `dir=rtl`, des 14 questions à figure ; gates.
> Le rapport de l'auteur (`rapports/rapport-M2.md`) n'a été lu qu'**après** la re-résolution.

## Bilan

| mission | fichier | q. | ma réponse = clé | critique | majeur | mineur |
| --- | --- | --: | --: | --: | --: | --: |
| m013 | `02/06-exam-2016-…` | 7 | 7/7 | 0 | 3 | 2 |
| m014 | `02/07-exams-2010-2026-…` | 8 | 8/8 | 0 | 3 | 2 |
| m015 | `03/06-exam-2025-…` | 7 | 7/7 | 2 | 1 | 1 |
| m016 | `03/07-exams-2015-2024-…` | 8 | 8/8 | 0 | 2 | 2 |
| m017 | `03/08-exams-2019-2026-…` | 7 | 7/7 | 0 | 2 | 2 |
| m018 | `03/09-exams-2019-2026-…` | 6 | 6/6 | 0 | 1 | 1 |
| m019 | `03/10-exams-2008-2025-…` | 6 | 6/6 | 1 | 0 | 2 |
| m020 | `03/11-devoir-…` | 8 | 8/8 | 0 | 4 | 0 |
| m021 | `10/06-exams-2013-2018-…` | 5 | 5/5 | 0 | 1 | 2 |
| m022 | `10/07-devoir-…` | 7 | 7/7 | 0 | 2 | 1 |
| **total** | | **69** | **69/69** | **3** | **19** | **15** |

**Il n'y a aucune clé fausse** : mes 69 réponses à l'aveugle sont égales aux clés.

Les défauts sont d'un autre ordre :
- 3 critiques :
  - une explication qui donne pour erreur l'association juste ;
  - une inversion de données face au sujet 2025 ;
  - un distracteur que l'élève ne peut pas réfuter (m019 Q4).
- Des questions qui redemandent le patron ou le cours.
- Des fuites d'une question vers une autre.
- Des notions du `03` ou du `04` exigées avant d'avoir été enseignées.
- La répétition de la grille 2×2 « couleur × gaz ».

**Verdict : à corriger.** Une fois les correctifs ci-dessous appliqués, le lot est prêt. Les tailles qui en résultent sont données au § Tailles.

### Gates (depuis `/home/user/eng-deliver`, lien `content` → `/home/user/wt-ev6/content` inchangé)

- `content:check` ✓ : 121 sujets, 31 689 questions.
- `content:qa -- --subject eveil-scientifique-6eme` ✓ : aucune clé suspecte.
- `content:figures:check` ✓.
- `content:tranche … --chapters 02-respiration,03-sang-circulation,10-microbes-defense --fresh --strict-longest --strict-lessons` ✓ (code de sortie 0) :
  - clé strictement la plus longue : 0/104 ;
  - positions de clé : 20 / 26 / 28 / 27 % ;
  - 0 cours en recul ;
  - 3 paires proches : m021 Q2↔Q3, m014 Q1↔Q8, m015 Q1↔Q5 (traitées plus bas) ;
  - 0 candidat gabarit automatique. La répétition est entre missions : elle est jugée au § Gabarit.
- `content:gisement:controle` (m020, m022) ✓ : 0 plage ≥ 8 mots, 0 plage ≥ 6 mots, 0 exercice dont on reprenne 3 données. Je n'ai pas lu les snapshots.
- `chapter.json` : `sources[]` porte la ligne « Sujets officiels du concours… » aux trois chapitres et la ligne « Calibré sur des devoirs publics… » au `03` et au `10` ✓.
- Rendu : aucun débordement (`scrollWidth` = 360). Les 14 figures ont été regardées une par une ; elles sont justes et aucune ne marque la clé. Une seule légende est rognée (m016 Q3, m-5).
- En-têtes ✓ : d3 `boss` 120/30 (m013, m015), d2 `practice` 75/15 (les autres). Titres en « 🏛️ … » / « 📝 … » sans clé. Toutes les missions ont ≤ 12 questions.
- Étiquettes : aucune sur un `multi`, un `ordering` ou un `matching`. Ids existants. Une seule est mal placée (m020 Q4, M-17).

### Tableaux par fichier (ma réponse à l'aveugle · clé · verdict)

**m013** :
- Q1 a·a OK.
- Q2 c·c OK (étiquette manquante, m-1).
- Q3 d·d **réserve** (donnée non imprimée, redemande ; M-2).
- Q4 s1–s5·idem **réserve** (fuite vers Q6, notion du `03` ; M-1, M-3).
- Q5 b·b OK.
- Q6 c·c **réserve** (notion du `03`).
- Q7 b·b **réserve** (notion du `03`).

**m014** :
- Q1 a·a OK.
- Q2 s1–s4·idem **réserve** (écrit « ماء الجير », qui est la clé de Q3 ; M-4).
- Q3 ماء الجير·idem **ERREUR de forme** (fuite et redemande ; M-4).
- Q4 c·c OK.
- Q5 l1-r1, l2-r2, l3-r3·idem **réserve** (fuite depuis Q4, quiz#3, sang « dans » l'alvéole ; M-5).
- Q6 {b,d}·idem **réserve** (items c et d relèvent du `03` ; M-6).
- Q7 b·b OK (m-3).
- Q8 d·d OK.

**m015** :
- Q1 d·d : clé juste mais **explication FAUSSE** (C-1) et **numéros d'organes inversés** (C-2).
- Q2 b·b OK.
- Q3 {a,c}·idem **réserve** (même savoir que Q4 ; M-7).
- Q4 c·c OK.
- Q5 a·a OK (C-2, gabarit).
- Q6 b·b OK : les quatre dessins ont été vérifiés au rendu, un seul est juste.
- Q7 l1-r1…l4-r4·idem OK.

**m016** :
- Q1 b·b OK (le dessin rend la clé unique).
- Q2 a·a **réserve** (son explication et Q1 donnent la clé ; verifie du cours ; M-8).
- Q3 b·b OK (figure rognée, m-5).
- Q4 d·d **ERREUR « ne pas redemander »** (= 03/02-boss#4 ; M-9).
- Q5 l1-r1…l4-r4·idem OK (gabarit).
- Q6 c·c OK.
- Q7 c·c OK.
- Q8 {a,b}·idem OK.

**m017** :
- Q1 d·d OK.
- Q2 c·c OK.
- Q3 {a,b,c}·idem OK.
- Q4 d·d **retouche** (M-10).
- Q5 b·b OK (m-4).
- Q6 s1–s4·idem **à remplacer** : الأذينة et البطين ne sont pas enseignés (M-10).
- Q7 c·c OK (m-4).

**m018** :
- Q1 b·b OK.
- Q2 l1-r1…·idem OK.
- Q3 l1-r1…·idem OK.
- Q4 l1-r1…l4-r4·idem **réserve** (= exemple résolu du cours ; M-11).
- Q5 idem **réserve** (M-11).
- Q6 d·d OK.

**m019** :
- Q1 {c,e,f}·idem OK, mais doublon de m020 Q8.
- Q2 {c,d}·idem OK (m-7).
- Q3 l1-r1…·idem **réserve** (item officiel remplacé sans le dire ; m-6).
- Q4 d·d **ERREUR** : l'option b est défendable (C-3).
- Q5 s1–s4·idem OK.
- Q6 {d,e}·idem OK.

**m020** :
- Q1 d·d OK.
- Q2 b·b OK (gabarit).
- Q3 b·b OK.
- Q4 a·a **ERREUR d'étiquette** + redemande (M-17).
- Q5 d·d **ERREUR « ne pas redemander »** (M-14).
- Q6 b·b **ERREUR « ne pas redemander »** (M-14).
- Q7 idem·idem **ERREUR de portée** (`04` ; M-15).
- Q8 {a,c,e}·idem **doublon de mission** (M-16).

**m021** :
- Q1 c·c OK (m-8).
- Q2 d·d OK.
- Q3 {a,b,c}·idem **réserve** (même énoncé que Q2 ; M-12).
- Q4 l1-r1…·idem OK (m-9).
- Q5 {a,c,f}·idem OK (m-10).

**m022** :
- Q1 b·b OK.
- Q2 c·c OK.
- Q3 s1–s4·idem **réserve** (= 10/04-defi#7, 05#7 et tableau du cours ; M-13).
- Q4 l1-r1…·idem OK.
- Q5 a·a OK.
- Q6 d·d OK.
- Q7 c·c **ERREUR « ne pas redemander »** (M-13).

---

## Défauts — critique

### C-1 · m015 `03/exercices/06-exam-2025-le-depliant-du-don-de-sang.json` Q1 : l'explication enseigne l'erreur

**Phrase fautive** : « الخطأ الشائع ربط اللّون بالغاز ربطًا مقلوبًا: القاتم مع ثاني أكسيد الكربون، والقاني مع الأكسجين ». Elle présente comme erreur l'association JUSTE (le sang sombre porte le CO₂, le sang vif porte l'O₂).

**Remplacement** de la dernière phrase de l'`explanation` :
- ancien : `الخطأ الشائع ربط اللّون بالغاز ربطًا مقلوبًا: القاتم مع ثاني أكسيد الكربون، والقاني مع الأكسجين.`
- nouveau : `الخطأ الشائع أن نجمع لونًا وغازًا لا يتلازمان: الدّم القاتم يحمل ثاني أكسيد الكربون، والقاني يحمل الأكسجين، فلا يجتمع القاني مع ثاني أكسيد الكربون ولا القاتم مع الأكسجين.`

### C-2 · m015 Q1 et Q5 : numéros d'organes inversés par rapport au sujet 2025

**Ce que montre le sujet.** Sur le PDF officiel (page 2), le vaisseau du haut à gauche part du cœur droit (côté légendé « الأذينة اليمنى ») vers **العضو 2**, et le retour de العضو 2 entre au cœur gauche. Le cadre « يتمّ التّبادل الغازيّ في مستوى: خلايا الجسم / الرّئتين » pointe **العضو 1**. Donc, dans le sujet : العضو 2 = les poumons, العضو 1 = un organe du corps.

**Ce que dit la mission.** Elle écrit l'inverse : « الرّئتين (العضو 1) وعضلة (العضو 2) ». C'est une donnée infidèle à la session citée.

**Remplacements** :
- Q1 `prompt` : remplacer `الرّئتين (العضو 1) وعضلة (العضو 2)` par `عضلة (العضو 1) والرّئتين (العضو 2)`.
- Q5 `prompt` : remplacer `من القلب إلى العضلة (العضو 2)` par `من القلب إلى العضلة (العضو 1)`.

Aucune clé ne change, et les figures de Q6 ne portent pas de numéro.

Mineur à corriger en même temps : la consigne officielle 1-أ « اُشطب العبارة الخاطئة في كلّ خانة لتحصل على الإفادة الصّحيحة » est paraphrasée (« نختار في كلّ خانة العبارة الصّحيحة »). Remplacer cette paraphrase par la phrase imprimée.

### C-3 · m019 `03/exercices/10-exams-2008-2025-globules-coagulation-et-anemie.json` Q4 : l'élève ne peut pas réfuter l'option b

**Option actuelle** : `b` « أصيب بمرض تصلّب الشّرايين فنقص عدد كريّاته الحمراء ».

**Le défaut.** L'artériosclérose n'est jamais enseignée (E-8). L'élève ne peut donc pas savoir qu'elle ne fait pas baisser les globules rouges. Or l'option b contient le BON mécanisme (moins de globules rouges), et elle explique les symptômes aussi bien que la clé d. Pour un élève de 6ᵉ, il y a deux réponses défendables.

**Remplacement** :
- `b` devient `أصيب بمرض تصلّب الشّرايين فكثرت كريّاته البيضاء` (47 car. ; clé `d` 48, `a` 48, `c` 55 : la clé n'est pas la plus longue). Le distracteur se réfute avec ce qui est enseigné : plus de globules blancs n'explique ni la fatigue ni la pâleur.
- Dernière phrase de l'`explanation` :
  - ancien : `وكلمة «تصلّب الشّرايين» اسم مرض لم نتعلّمه ولا يجعل الكريّات الحمراء تنقص في هذه الوضعيّة.`
  - nouveau : `و«تصلّب الشّرايين» اسم مرض لم نتعلّمه، وكثرة الكريّات البيضاء لا تفسّر الإرهاق واصفرار الوجه، فعملها الدّفاع عن الجسم.`

---

## Défauts — majeur

### M-1 · m013 (`02/06-exam-2016-…`) Q4–Q7 : notions du chapitre `03` exigées au `02`

**Le constat.** Le cours du `02` s'arrête au poumon. Sa clôture le dit : « التالي: كيف ينقل الدّم هذا الأكسجين إلى كلّ أعضاء الجسم ». Il ne nomme ni le cœur comme pompe, ni les artères.

**Les questions touchées** (elles en ont besoin, alors que ces notions ne sont enseignées qu'au `03`, § « ❤️ القلب يضخّ الدّم ») :
- Q4 (étape « يضخّ القلب الدّم في الشّرايين ») ;
- Q6 (les dessins avec le cœur) ;
- Q7 (sa clé dit « من الرّئتين إلى القلب ثمّ إلى العضلة »).

La note de la carte (« acquis de 5ᵉ ») ne suffit pas : la règle est « enseigné par le chapitre ou par un chapitre antérieur ».

**Correctif recommandé : déplacer m013 au `03`.**
- Fichier : `03-sang-circulation/exercices/12-exam-2016-de-lair-aux-cellules-le-trajet-de-loxygene.json`, `displayOrder` 12.
- Tout y devient enseigné : la respiration (`02`) précède le `03`.
- Mettre à jour le champ `fichier` de m013 dans `gisement.json`. Les `sources[]` du `03` portent déjà la ligne d'examen ; celle du `02` reste pour m014.

**Repli, si le pilote tient au placement au `02`.** Supprimer Q4, Q6 et Q7, et garder Q1, Q2, Q3 et Q5 (4 q). Le cours du `02` enseigne déjà « les organes prennent l'oxygène et rendent le CO₂ » (verifie du § التبادل الغازي). On perd alors la consigne 1 du support 2.

### M-2 · m013 Q3 : donnée non imprimée attribuée au sujet, et redemande

**Les deux défauts.**
- Le sujet 2016 n'imprime pas que l'eau de chaux se trouble : la transcription et le PDF montrent seulement la coupelle légendée. Pourtant Q3 écrit « (مناظرة 2016 — السّند 1) … بعد 20 دقيقة تعكّر ماء الجير ».
- Elle redemande aussi 02/02-boss#3, 03-revision#8 et 05-entrainement#1 (l'eau de chaux qui se trouble prouve le CO₂).

**Remplacement** (`difficulty` 2) : il garde le rôle de l'eau de chaux, que la carte demande, sans inventer d'observation.
- `prompt` : `(مناظرة 2016 — السّند 1) في الوعاء المغلق، بجانب الفأر، كأس فيها ماء الجير الصّافي. لو بقي الفأر في الوعاء مدّة أطول، ماذا نتوقّع أن نلاحظ في الكأس، ولماذا؟`
- options :
  - `a` `يتعكّر ماء الجير، لأنّ الفأر يطرح ثاني أكسيد الكربون في تنفّسه` [62] (clé)
  - `b` `يتعكّر ماء الجير، لأنّ الفأر يطرح بخار الماء في الوعاء` [54], étiquette `eveil.gaz.test-mal-associe`
  - `c` `يبقى ماء الجير صافيًا، لأنّ الفأر لا يطرح في الوعاء أيّ غاز` [59], muette
  - `d` `يبقى ماء الجير صافيًا، لأنّ ماء الجير لا يتعكّر إلّا بالأكسجين` [62], étiquette `eveil.gaz.test-mal-associe`
- `explanation` : `يتعكّر ماء الجير بثاني أكسيد الكربون، والفأر يطرح هذا الغاز في هواء الوعاء كلّما تنفّس، فنتوقّع أن يتعكّر ماء الجير. أمّا بخار الماء فنكشفه بقطرات على جدار بارد لا بماء الجير، والأكسجين لا يعكّره، والفأر الحيّ لا يتوقّف عن طرح الغازات في تنفّسه.`

Vérifications faites :
- La clé n'est pas strictement la plus longue (elle est à égalité avec d).
- Vote « يتعكّر/يبقى » : 2 contre 2.
- Aucune option ne nomme le gaz dont la part baisse : pas de fuite vers Q1.
- Aucune prémisse niée : le sujet ne dit rien de l'eau de chaux.

### M-3 · m013 Q4 → Q6 : l'explication de Q4 résout Q6

**Le constat.** L'explication de Q4 déroule « هواء ← رئتان ← دم ← قلب ← شرايين ← عضلة » : c'est exactement la clé du QCM visuel Q6. Q7 corrige ensuite le même trajet, ce qui fait trois questions sur un seul geste.

**Correctif** : supprimer Q4, l'`ordering`. Garder Q6, qui est la forme la plus fidèle à « أحدّد بسهم … على الرّسم (ب) ». L'ordering du trajet existe déjà au `02` (03-revision#7) et au `03` (02-boss#8).

### M-4 · m014 (`02/07-exams-2010-2026-…`) Q2 → Q3 : fuite, et Q3 redemande le patron

**Le constat.**
- Les étapes s1 et s2 de Q2 écrivent « ماء الجير » : c'est la réponse `short_answer` de Q3.
- Q3 est aussi mot pour mot 02/05-entrainement#1 (« ماذا نستعمل؟ — ماء الجير »).

**Correctif** : supprimer Q3. L'expérience 2026 (2-2) reste portée par l'ordering Q2.

### M-5 · m014 Q4 → Q5 : fuite, item du quiz, et science inexacte

**Les défauts.**
- La figure officielle de 2020 (Q4) et sa phrase « يصل الدّم إليها غنيًّا بثاني أكسيد الكربون ويغادرها غنيًّا بالأكسجين » donnent les lignes l1 et l2 de Q5.
- La ligne l3 (air expiré : CO₂ et vapeur d'eau) est 02/quiz#3.
- « الدّم الّذي يدخل الحويصلة » est faux : le sang ne pénètre pas dans l'alvéole, il passe dans la شعيرة qui l'entoure. L'explication répète « يدخل الحويصلة ».

**Correctif** : supprimer Q5. La session 2015 reste reprise par m016 et m021.

### M-6 · m014 Q6 : deux des quatre items 2010 relèvent du `03`

**Les items touchés.**
- L'item d (« الكريّات الحمراء … نقل الغذاء ») exige le rôle du plasma.
- L'item c (« يمرّ الدّم من الرّئتين إلى القلب ») exige le cœur.

Ces deux notions ne sont enseignées qu'au `03`. Au `02`, le cours dit que le sang « يعود إلى أعضاء الجسم أحمر قانيًا » : un élève du `02` peut donc juger c faux.

**Remplacement** (`type` mcq, `difficulty` 2, clé `b`) :
- `prompt` : `(مناظرة 2010 — السّند 6) نهض أحمد في الصّباح وخرج من الخيمة قائلا: «هلمّوا يا أصدقائي نمارس أنشطة رياضيّة في الهواء الطّلق». أضع العلامة (×) أمام الإفادة الخاطئة. أيّ إفادة خاطئة؟`
- options :
  - `a` `يتمّ التّبادل الغازي بين الجسم وهواء المحيط في مستوى الحويصلات الرّئويّة` [72] (item 1 officiel)
  - `b` `أتنفّس بأنفي لأنّ أغشيته تُنقّي الهواء من ثاني أكسيد الكربون` [60] (item 2 officiel, clé). Le sujet écrit « ثنائي » : on peut garder « ثنائي » pour la lettre.
  - `c` `يعود الدّم من الرّئتين إلى أعضاء الجسم محمّلًا بالأكسجين` [56] (item 3 ramené au cours du `02`)
  - `d` `يخرج ثاني أكسيد الكربون من الجسم مع هواء الزّفير` [48]
  - Toutes muettes.
- `explanation` : `أغشية الأنف تُدفئ الهواء وتنقّيه من الغبار، ولا تنقّيه من ثاني أكسيد الكربون: هذا الغاز يخرج من الجسم مع هواء الزّفير. والإفادات الأخرى صحيحة: التّبادل الغازي في الحويصلات الرّئويّة، والدّم يغادر الرّئتين محمّلًا بالأكسجين نحو أعضاء الجسم. (في المناظرة إفادة رابعة عن الكريّات الحمراء ونقل الغذاء، وهي من درس الدّم، فلم نُدرجها هنا.)`

Vérifications faites :
- La clé n'est pas la plus longue.
- Une seule option est fausse.
- Il n'y a pas de paire vrai/faux sur la même phrase.

### M-7 · m015 Q3 ↔ Q4 : même savoir, et chacune donne l'autre

**Le constat.** Le `multi` des erreurs (Q3 : forme et moelle) et la phrase corrigée (Q4) se résolvent l'une par l'autre. Les deux reprennent aussi le verifie du cours (l.104 : « مستديرة، مقعّرة الوجهين … وأين تكوّنت؟ ») et 03/02-boss#1–#2.

**Correctif** : supprimer Q3 et garder Q4, qui est la forme officielle « أصلح ».

### M-8 · m016 (`03/07-exams-2015-2024-…`) Q1 → Q2 : fuite, et verifie du cours

**Le constat.**
- L'explication de Q1 décrit les deux tubes : c'est la clé de Q2.
- Le dessin de Q1 montre déjà les deux aspects.
- Q2 est aussi le verifie du cours, l.165 (« كتلة حمراء داكنة يحيط بها سائل مصفرّ: دم مترسّب أم متخثّر؟ »).

**Correctif** : supprimer Q2. Q1 garde la consigne 2022 (2-ب).

### M-9 · m016 Q4 = 03/02-boss#4

**Le constat.** 02-boss#4 dit : « يدخل الدّم … داكنًا ويخرج … قانيًا. ماذا حدث له؟ — ترك CO₂ وأخذ O₂ ». Q4 pose la même question et a la même clé.

**Correctif** : supprimer Q4. L'auteur le proposait lui-même.

### M-10 · m017 (`03/08-exams-2019-2026-…`) : remplacement de Q6 et retouche de Q4 (décision du pilote)

**Q6 : remplacement.** L'`ordering` actuel exige الأذينة اليسرى, البطين الأيسر et الشّريان الأبهر. Il est remplacé par un QCM (`difficulty` 3, clé `a`) :

- `prompt` : `(مناظرة 2020 — الوضعيّة عدد 1، التّعليمة 2) أصلح مسار الدّم القادم من الرّئتين إلى القلب. جاء في الوثيقة: الأوردة الرّئويّة ← البطين الأيسر ← الأذينة اليمنى ← الشّريان الأبهر. دون الدّخول في أجزاء القلب، أيّ مسار صحيح للدّم الغنيّ بالأكسجين من الرّئتين إلى أعضاء الجسم؟`
- options :
  - `a` `الرّئتان ← الأوردة الرّئويّة ← القلب ← الشّرايين ← أعضاء الجسم` [62] (clé)
  - `b` `الرّئتان ← الشّرايين الرّئويّة ← القلب ← الشّرايين ← أعضاء الجسم` [64]
  - `c` `الرّئتان ← الأوردة الرّئويّة ← القلب ← الأوردة ← أعضاء الجسم` [60]
  - `d` `الرّئتان ← الشّرايين الرّئويّة ← القلب ← الأوردة ← أعضاء الجسم` [62] (deux erreurs, muette)
  - Toutes muettes : le registre n'a pas d'id artère/veine (voir M-18).
- `explanation` : `الدّم الّذي يغادر الرّئتين يعود أوّلًا إلى القلب في الأوردة الرّئويّة، لأنّ الوعاء الّذي يعيد الدّم إلى القلب وريد. ثمّ يضخّه القلب في الشّرايين نحو أعضاء الجسم، لأنّ الوعاء الّذي يحمل الدّم من القلب شريان. نسمّي الوعاء بحسب اتّجاه الدّم لا بحسب لونه: من سمّى الوعاء العائد من الرّئتين شريانًا، أو الوعاء الذّاهب إلى الأعضاء وريدًا، خالف هذه القاعدة. أمّا حجرات القلب المذكورة في الوثيقة فلا يُسأل عنها هنا.`

Vérifications faites sur Q6 :
- Plan 2×2 (vaisseau du retour × vaisseau de l'aller) : vote 2 contre 2 sur chaque position.
- La clé n'est pas la plus longue.
- Aucune question n'exige une cavité du cœur.
- Rendu Chromium `dir=rtl` à 360 px : les chaînes « ← » se lisent dans l'ordre et passent à la ligne proprement.
- Pas de doublon avec 03/02-boss#8, qui suit le trajet inverse (sang sombre depuis les organes).

**Q4 : retouche.** Dans le `prompt`, remplacer `(الأذينان حجرتان من حجرات القلب)` par `(الأذين الأيمن والأذين الأيسر جزآن من القلب، ولا يُسأل عنهما هنا)`.

Le mot « حجرات » est absent du cours, et la question ne porte que sur veines / veines pulmonaires. La citation officielle reste intacte, et l'explication ne cite aucune cavité.

### M-11 · m018 (`03/09-exams-2019-2026-…`) : la table composant ↔ fonction posée trois fois

**Le constat.**
- Q4 (2026 1-ب) est l'exemple résolu du cours « نرتّب الأعمال في الجدول » : mêmes quatre fonctions, mêmes quatre composants. C'est aussi 03/05-entrainement#4.
- Q5 (fonction de chaque flèche) et Q6 (table 2019) reposent la même table.

**Correctif** : supprimer Q4 et Q5, garder Q6 (seule question de la session 2019 dans cette mission).

Si le pilote préfère garder la session la plus récente : garder Q4, supprimer Q5 et Q6, et inscrire au rapport de correction la réserve « Q4 reprend l'exemple du cours ».

### M-12 · m021 (`10/06-exams-2013-2018-…`) Q2 ↔ Q3 : même énoncé 2018

**Le constat.** La tranche signale la paire (0,54). Le QCM de la phrase corrigée (Q2) et le `multi` des trois erreurs (Q3) se résolvent l'un par l'autre. Q2 porte aussi l'id `vaccin-pris-pour-medicament`, déjà vu en 03-revision#6 (« مناعة مكتسبة »).

**Correctif** : supprimer Q3.

### M-13 · m022 (`10/07-devoir-…`) : Q3 et Q7 redemandent le patron et le cours

**Q3 (ordering des phases).**
- Ses étapes s1 et s2 reprennent 10/05-entrainement#7 et le tableau du cours (étapes 2–4).
- La suite (globules blancs, puis pus / septicémie) reprend 10/04-defi#7.

**Q7 (« plaie lavée à l'eau seulement »).** Elle reprend l'exemple de ريم du cours, 10/02-boss#4 et 10/04-defi#4.

**Correctif** : supprimer Q3 et Q7. Il reste 5 questions. E-1 range déjà m022 parmi les missions à couper en premier : si le pilote préfère couper toute la mission, le lot n'y perd aucun geste d'examen.

### M-14 · m020 (`03/11-devoir-…`) Q5 et Q6 : redemandes mot pour mot

**Le constat.**
- Q5 (le constituant qui aide la croûte à se former : les plaquettes) = 03/01-pratique#7 et quiz#6. C'est aussi le verifie l.232.
- Q6 (« où les aliments passent dans le sang : الأمعاء الدّقيقة ») = 03/03-revision#5.

**Correctif** : supprimer Q5 et Q6.

### M-15 · m020 Q7 : trois éléments relèvent du chapitre `04`

**Le constat.** النّشويّات (énergie), الماء (deux tiers du corps) et الفيتامينات (protection) ne sont enseignés qu'au `04` (nutrition), qui vient après le `03`.

**Remplacement** (`matching`, `difficulty` 2) :
- `prompt` : `اربط كلّ عنصر بما يناسبه من عمل أو دور:`
- paires :
  - `l1` `الكريّات الحمراء` → `r1` `تنقل الأكسجين وثاني أكسيد الكربون`
  - `l2` `الكريّات البيضاء` → `r2` `تدافع عن الجسم`
  - `l3` `مادّة الحديد` → `r3` `نقصها في الغذاء يسبّب فقر الدّم`
  - `l4` `القلب` → `r4` `يضخّ الدّم في الأوعية الدّمويّة`
- `explanation` : `الكريّات الحمراء تنقل الغازين، والكريّات البيضاء تدافع عن الجسم، ونقص مادّة الحديد في الغذاء من أسباب فقر الدّم لأنّ الكريّات الحمراء غنيّة بها، والقلب عضلة تضخّ الدّم في الأوعية الدّمويّة. الخطأ الشائع أن نخلط بين عمل الكريّات الحمراء وعمل الكريّات البيضاء.`

Vérifications faites : les quatre notions sont enseignées au `03`. L'association fer ↔ anémie et le cœur sont absents de 05#4.

### M-16 · m020 Q8 = m019 Q1 (doublon entre missions)

**Le constat.** Les deux questions cochent les mêmes propriétés (مقعّرة الوجهين، بها نواة، غنيّة بمادّة الحديد) entre globules rouges et blancs.

**Correctif** : supprimer m020 Q8 et garder m019 Q1, qui est la reprise officielle de 2012.

### M-17 · m020 Q4 : étiquette sur l'option à deux erreurs, et redemande

**L'étiquette mal placée.** `b` (« الكتلة: الكريّات، والسّائل: البلازما ») a deux erreurs mais porte `eveil.sang.plasma-et-serum-confondus`. L'erreur simple est `c` (« العلقة » + « البلازما »).

**La redemande.** Q4 reprend aussi 03/03-revision#3 et le verifie l.165.

**Correctif** : supprimer Q4. Si elle est gardée, déplacer l'étiquette de `b` vers `c` et laisser `b` muette.

### M-18 · ids d'étiquette manquants (m015, m016, m017, m020)

**Le constat.** Aucun id du registre ne dit « artère et veine nommées par la couleur » ni « sang coagulé et sang décanté confondus ». Les pièges de la carte C04#1, C08#2, C05#3, D04#1 et D04#2 restent donc muets. m017 n'a aucune étiquette.

**Ce que je propose.** J'appuie la proposition de l'auteur, rédigée au registre :
- `eveil.sang.nom-du-vaisseau-par-la-couleur` : « Tu nommes le vaisseau d'après la couleur de son sang : on dit artère ou veine selon le sens, du cœur ou vers le cœur ». Occurrences : m015 Q2 a/d, m017 Q2 b, m020 Q1 a.
- `eveil.sang.coagule-et-decante-confondus` : m016 Q1 a, m020 Q3.

Je ne propose **pas** `couleur-selon-le-sens-inversee` : `eveil.resp.sens-echanges-gazeux-inverse` couvre déjà ce cas.

### Gabarit · les 2×2 « couleur × gaz » de m014–m017 et m020 (demande du pilote)

**Inventaire.** Une douzaine de questions posent le même cadre : un vaisseau ou un sang au voisinage des poumons, croisé avec couleur, gaz ou nom.
- m014 Q8
- m015 Q1, Q2, Q5
- m016 Q3, Q4, Q5, Q7, Q8a
- m017 Q4, Q5, Q7
- m020 Q1, Q2

Cinq d'entre elles sont dans la seule m016. C'est un **gabarit** : ces questions ne diffèrent que par le vaisseau choisi.

**Allègement proposé.** Il garde chaque session officielle au moins une fois et un seul 2×2 de ce cadre par mission, deux au plus en m015 et m017, dont c'est le sujet.
- m016 : supprimer Q4 (M-9) et **Q5**. 2024 reste reprise par m019 Q3, et Q7 (2015) dit la même chose sous la forme « أصلح ».
- m015 : garder Q1 et Q5 (cadres officiels), plus Q2 (le nom par le sens).
- m020 : supprimer **Q2**. Le vaisseau ب (« وريد غنيّ بالأكسجين ») est déjà m015 Q2 et m017 Q5 ; Q1 garde le geste neuf du devoir, le schéma du cœur.
- m014 Q8 et m017 Q5/Q7 sont gardés : ce sont des formes « أصلح » différentes et des sessions distinctes.

**Résultat** : on passe de 14 à 10 questions de ce cadre, et aucune mission n'en a plus de 3.

---

## Défauts — mineur

- **m-1** · m013 Q2 : `a` (« يمتصّه ماء الجير ») exécute le piège C11#1b, mais ne porte aucune étiquette. Poser `eveil.gaz.test-mal-associe`.
  - Q1 `b` (gaz produit pris pour le gaz consommé) : pas d'id dans le registre. Laisser muette.
- **m-2** · m013 Q5 : sur le PDF 2016 (dessin أ), le sens des flèches est illisible au scan. La flèche liée à « غاز 2 » paraît entrer dans la cellule.
  - Cela n'est pas bloquant : la mission fixe les sens par écrit et reste juste.
  - Mais elle ne doit pas prétendre reproduire la numérotation imprimée. Ajouter à l'énoncé « (أعدنا رسم السّند) ».
- **m-3** · m014 Q7 : `d` (« غطّى الدّخان جلدها … مسامّها ») est un distracteur faible, mais l'idée « on respire par la peau » existe chez l'enfant. Je le garde.
  - Ne pas le remplacer par « l'air a perdu de l'oxygène dans le feu » : cette option serait vraie et créerait une seconde réponse.
  - Par ailleurs, m014 Q6 normalise « ثنائي أكسيد الكربون » (2010) en « ثاني ». Rétablir la graphie imprimée dans l'item cité.
- **m-4** · m017 Q5 `d` et Q7 `d`, m014 Q8 `c` : « …، ولا خطأ فيه » nie la prémisse « أصلح كلّ خطأ » et s'élimine à vue.
  - Ce n'est pas grave, car la grille 2×2 reste entière.
  - Remplacer par l'énoncé fautif sans la mention « ولا خطأ », comme le fait déjà m015 Q4.
- **m-5** · m016 Q3, figure : les deux `<text … x="14" … text-anchor="start">دم</text>` sont rognés au bord gauche en page RTL (vu au rendu). Le `start` y devient le bord droit. Remplacer par `x="22" … text-anchor="middle"` (rendu vérifié).
  - Le rapport de l'auteur affirme à tort « ancrage `middle` uniquement ».
- **m-6** · m019 Q3 : l'item 3 officiel (« سائل ينقل الفضلات … إلى الكليتين ») est remplacé par « كتلة داكنة … » (العلقة), sans que l'énoncé ni l'explication le disent. Ajouter à l'explication : `(في المناظرة سطر ثالث عن سائل ينقل الفضلات، وهو البلازما أيضًا، فعوّضناه بالعلقة.)`
  - Par ailleurs, Q3 l1 (sérum) donne la clé de Q6a.
- **m-7** · m019 Q2 c (« الدّم المتخثّر يتكوّن من علقة ومصل ») = 03/quiz#5. Il est toléré, comme item officiel d'un `multi` de quatre.
- **m-8** · m021 Q1 : les deux premiers blancs (« الغذاء والدّفء ») = 10/01-pratique#4. L'item est officiel. Le 2×2 est sain, avec `a` muette.
- **m-9** · m021 Q4 : même tâche et même colonne de droite que 10/05-entrainement#4 (les trois types de défense), avec d'autres éléments. C'est une reprise officielle. Je la garde, en réserve.
- **m-10** · m021 Q5 (`multi`) : les six options sont trois paires « énoncé / correction ». Le nombre de bonnes réponses (une par paire) se déduit donc.
  - Correctif : retirer `b` et `e`, déjà cités dans l'énoncé, et ajouter :
    - `g` `يكفي زيدان أن يغسل جرحه بالماء ثمّ يتركه مكشوفًا` (faux) ;
    - `h` `يحتاج زيدان إلى تطهير جرحه قبل أن يضع عليه ضمادة` (vrai).
  - Clé : `a`, `c`, `f`, `h`.
  - Ajouter à l'explication : `والماء وحده لا يطهّر الجرح، فلا بدّ من مطهّر ثمّ ضمادة.`
- **m-11** · m022 Q3 (si elle est gardée malgré M-13) : le cours dit aussi « الانتفاخ دليل على توجّه الكريّات البيضاء » ; l'ordre s2 → s3 suit le tableau du cours. C'est une réserve, pas une erreur.
- **m-12** · Effectifs : 69 questions au lieu des 90 de la carte. m021 n'a que 5 questions, alors que la carte en prévoyait 9 : les trois QCM de 2013 sont devenus un seul `multi`. Rien à corriger, à acter par le pilote.
- **m-13** · Le rapport de l'auteur dit que les transcriptions n'existaient pas. Je les ai confrontées : les phrases officielles reprises sont conformes, sauf C-2, M-2, m-6 et la normalisation « ثنائي » → « ثاني ».

## Tailles après correction (si tout est appliqué, allègement compris)

- m013 : 6 q (au `03` si M-1 est retenu).
- m014 : 6 q.
- m015 : 6 q.
- m016 : 5 q.
- m017 : 7 q.
- m018 : 4 q.
- m019 : 6 q.
- m020 : 3 q (Q1, Q3 et Q7 remplacé).
- m021 : 4 q.
- m022 : 5 q.

**Total : 52 questions.**

m020 ne garderait que ses deux gestes neufs (schéma du cœur, tubes) et l'appariement. Le pilote peut aussi la fusionner avec m019, ou la couper (E-1) : le lot ne perdrait aucun geste d'examen.

## Verdict

**À corriger.** Les 3 critiques (C-1, C-2, C-3) et les majeurs M-1 à M-17 doivent être appliqués avant l'armement. Les textes de remplacement ci-dessus ont été vérifiés :
- par script : longueurs, clé jamais strictement la plus longue, votes 2×2 ;
- dans Chromium `dir=rtl` à 360 px : les chaînes « ← » de M-10 et la légende de m-5.

Aucun fichier de `content/` n'a été modifié, et aucune commande git n'a été lancée.
