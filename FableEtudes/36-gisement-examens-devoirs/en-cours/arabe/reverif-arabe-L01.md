# Re-vérification ciblée — gisement arabe 9ᵉ, lot L01 (après correction)

> Auditeur indépendant, 2026-10-14. Objet : commit `3c5d3ae1` (« L01 corrigé après audit ; cours 09 et 10
> complétés ») sur `wip/gisement-arabe-9eme`, comparé à mon audit `audit-arabe-L01.md`. Périmètre :
> `content/arabic/10-fahm-wa-intaj/exercices/07…12-*`, `10-fahm-wa-intaj/chapter.json`, `cours.md` du 10,
> `09-al-intaj-al-kitabi/cours.md` et `resume.md` (les fichiers L03 du ch. 09 présents dans le même commit
> sont hors périmètre et n'ont pas été lus). Aucun fichier modifié, aucune écriture git.

## 1. Mes textes, repris mot pour mot ?

Vérifié ligne à ligne sur les fichiers actuels (les identifiants d'options ont été remélangés : sans effet,
le moteur mélange à l'affichage).

| correctif | état |
| --- | --- |
| C-1 « قد (مع الماضي) » : ch. 10 l. 268 + phrase de la حالة حدّيّة ; ch. 09 l. 443, 484, 551 ; `09/resume.md` l. 10 | ✓ conformes |
| M-1 ordinaux en lettres (07 Q4, 08 Q4 énoncés, options, explications) | ✓ |
| M-2 07 Q3 (b, c, d, explication) | ✓ |
| M-3 07 Q1 explication ; 08 Q4 explication | ✓ |
| M-4 07 Q5 option تاريخيّة + explication ; cas limite سلطة au cours (l. 236) | ✓ |
| M-5 08 Q8 | **écart déclaré** → § 2 |
| M-5 12 Q5 a + explication | ✓ |
| M-6 retrait des chevilles (07 Q7 c, d ; 08 Q7 ; 10 Q6 ; 10 Q7) | ✓ |
| M-7 08 Q1 « أخلاقيّة », 08 Q2 « يستحقّ » + explications + étiquettes | ✓ |
| M-8 09 Q1 (énoncé, options, explication) | ✓ |
| M-9 09 Q3 a, b + explication ; 12 Q7 | ✓ |
| M-10 09 Q7 | ✓ |
| M-11 11 Q5 a, d + explication | ✓ |
| M-12 11 Q1 en QCM sur les quatre candidats officiels | ✓ (+ QCM « يُزاحِمُ », § 2) |
| C-2 العنوان المضمونيّ (ch. 10 l. 58) ; C-3 bloc « تطوّرُ الموقفِ » (l. 511-513) ; C-5 ألفاظ الشمول (l. 447) | ✓ textes conformes ; rendu → § 4 |
| m-1 étiquette 07 Q6 ; m-2 pont 08 Q3 ; m-3 08 Q3 b ; m-4 08 Q5 ; m-9 09 Q6 ; m-10 10 Q1 ; m-11 10 Q2 ; m-15 10 Q6 ; m-16 11 Q4 (désormais Q5) ; m-17 11 Q7 (désormais Q8) ; m-19 12 Q4 ; m-20 `chapter.json` | ✓ (m-2 : collage maladroit, § 3) |

## 2. Écarts déclarés — jugement

- **08 Q8 c → option « حظّ » remplacée.** L'objection de l'auteur est **fondée** : mon option « لا يكفي
  وحدَه؛ فالعاملُ يحتاجُ أيضًا إلى الحظِّ… » n'est contredite par rien dans le texte, et la clé ajoute elle
  aussi un élément extérieur (« أجرًا عادلًا ») : deux réponses défendables. Mais le texte retenu est
  **incohérent** : `لا يكفي وحدَه؛ فالعاملُ يحتاجُ أيضًا إلى الحظِّ، وأمّا المعارفُ فلا تلزمُه في عالمٍ تقودُه الآلاتُ`
  — « لا يكفي وحدَه » pose que les معارف sont nécessaires, la seconde moitié le nie ; il recopie en outre le
  motif de l'option « لا يكفي؛ لأنّ المعارفَ لا قيمةَ لها… الآلاتُ » (deux distracteurs sur la même erreur) et
  devient l'option la plus longue (86). → **MAJEUR R-1**, correctif plus bas.
- **09 Q3 et 09 Q6 d, longueurs réajustées** : accepté. 09 Q6 c « …بالحربِ والتهجيرِ » et la clé
  « …بعد أنْ بدا مختلفًا » (54 / 67) : clé non la plus longue ; explication mise à jour ✓. 09 Q3 : clé
  toujours strictement la plus courte (40 contre 48/48/56), toléré (voir § 3, indice inverse au niveau du lot).
- **11 Q1 en QCM + QCM « يُزاحِمُ » (mission à 8 q.)** : accepté. Plan du QCM sans vote ✓ (chaque candidat une
  fois par case). « يُزاحِمُ » re-résolu : يُنافِسُ ✓ ; « يَدْفَعُ » piège de sens courant (étiquette exacte),
  « يُعاوِنُ » contraire, « يُقاتِلُ » excès. Rampe 1-1-1-1-2-2-2-3 ✓, 8 questions ≤ 12 ✓, toujours d2 practice
  75/15 ✓. Pas de doublon avec 06/07 Q9 (اسم مفعول de تحصيل) ni avec 11 Q8 (même phrase, autre notion).
- **Étiquette `arabe.fahm.jawab-min-kharij-al-nass` en 08 Q8** : son libellé (« تجيبُ من رأيِك أو من الحياةِ لا من
  قرائنِ النّصِّ ») ne décrit pas une option qui **contredit** le texte ; à retirer avec R-1 (option muette).

## 3. Re-résolution à l'aveugle des questions retouchées et de leurs voisines

Re-résolues : 07 Q1–Q7, 08 Q1–Q8, 09 Q1–Q7, 10 Q1–Q2, Q6–Q7, 11 Q1–Q8, 12 Q3–Q5, Q7 (40 questions).
**Toutes les clés sont justes.** Points nouveaux :

- **R-1 (MAJEUR) 08 Q8 option d** (voir § 2). Remplacer par
  `لا يكفي وحدَه؛ فلا بدَّ أيضًا أن يلزمَ العاملُ تخصّصًا دقيقًا في عمليّةٍ واحدةٍ لا يغادرُها`
  (nuancée, cohérente, contredite par le texte : « تحطيمَ الإطارِ الجامدِ للتخصّصِ الضيّقِ »،
  « لا تكتفي بعمليّةٍ واحدةٍ ») ; **sans étiquette**. Longueurs : clé 66 / 59 / 67 / 78 ✓. Dans l'explication,
  remplacer « وأمّا الجوابُ الذي يضيفُ الحظَّ وينفي حاجةَ العاملِ إلى المعارفِ فجوابٌ من الحياةِ لا من النصِّ
  ينقضُه قولُه إنّ الآلاتِ تتطلّبُ معرفةً؛ » par
  « وأمّا الجوابُ الذي يشترطُ تخصّصًا دقيقًا في عمليّةٍ واحدةٍ فينقضُه النصُّ الذي يدعو إلى تحطيمِ الإطارِ
  الجامدِ للتخصّصِ الضيّقِ؛ ». Ne donne pas la clé de 08 Q7 (qui porte sur la **raison** de ce « تحطيم »,
  l'obsolescence des savoirs).
- **R-2 (MAJEUR, préexistant, manqué à mon premier passage) 08 Q8 explication : renvoi ordinal.**
  « فالجوابُ الأخيرُ يعترفُ… » désigne une option par sa place ; les options sont mélangées (la clé est
  d'ailleurs aujourd'hui `a`). Remplacer par « فالجوابُ الذي يعترفُ بأنّ المعارفَ شرطٌ لازمٌ ثمّ يضيفُ ما
  تتوقّفُ عليه المنزلةُ موقفٌ معلَّلٌ يحكمُ «إلى حدٍّ ما». » (balayage du lot : aucun autre renvoi par
  lettre ou par rang).
- **R-3 (mineur) 08 Q3 explication** : le pont m-2 a été collé devant l'ancienne phrase, d'où deux « : » et
  « فمعناها التوكيدُ » deux fois. Texte propre :
  `«لا شكَّ أنّ» من صيغِ الوثوقِ التي يقوّي بها الكاتبُ خبرَه، فمعناها في الحجاجِ التوكيدُ. والحكمُ بمعنى المؤشِّرِ لا بصورتِه: وجودُ «لا» لا يجعلُه نفيًا، فهي تنفي الشكَّ لا الحدثَ، والعبارةُ مع «أنّ» تشدّدُ على ما بعدَها وتثبّتُه. وليست استدراكًا إذ لا كلامَ قبلَها تعارضُه، ولا تفسيرًا إذ لا ما سبقَها ليُشرَحَ، ولا نفيًا لأنّ الكاتبَ يُثبتُ أثرَ الثورةِ العلميّةِ.`
- **R-4 (mineur, préexistant) 12 Q3 `multi`** : l'option clé « …فيتبادلونَ الترحّمَ على الفقيدِ » est la plus
  longue des cinq (61) et déforme « فيترحّمون على من فُقِد » (pas d'échange). Remplacer par
  `مكانٌ يسمعُ فيه الناسُ أخبارَ الوفياتِ فيترحّمونَ` (≈ 42 ; les autres options restent 28–51).

**Fuites** (le donjon tire les questions seules, la mission les trie par difficulté) : 07 Q1 ↔ Q3 ↔ Q4,
08 Q4 → Q5, 09 Q1 → Q2 sont **refermées**. Restes acceptés : 07 Q3 c paraphrase la phrase 1 (« فلا يتّخذ من
حوادثها قصصه »), déjà citée dans 07 Q1 — c'est le texte lui-même ; 08 Q7 explication nomme thèse et
conclusion (fuite **arrière** vers 08 Q4, mineure). Aucune nouvelle fuite créée par les correctifs.

**Indices de forme** : clé strictement la plus longue **0/30** ; clé strictement la plus courte
**9/30 = 30 %** (avant : 48 %) — au niveau du hasard (≈ 25 %), plus de défaut de lot. `multi` : 07 Q3, 08 Q6,
09 Q1 sans clé la plus longue ; 12 Q3 → R-4. Plans 2×2 (08 Q4, 10 Q4, 11 Q1, 11 Q5) : aucun vote, options à
deux erreurs muettes ✓.

## 4. Rendu

- **Items, `dir=rtl`, refait** (`isolateLtrRuns` + Chromium `/opt/pw-browsers/chromium-1194`) : sur les six
  fichiers, `isolateLtrRuns` n'insère **plus aucun isolat** ; les seules chaînes à chiffres sont les en-têtes
  « (مناظرة 2026، عامّ) », rendus dans le bon ordre. Les « (1) « » brouillés ont disparu.
- **Ajouts de cours, `renderLesson`** (moteur `eng-argis`, rendu Chromium) :
  - « قد (مع الماضي) », phrase قد + المضارع, cas limite سلطة, ألفاظ الشمول dans le tableau : rendus propres,
    dans leur bloc.
  - **R-5 (mineur)** : le paragraphe « **والعنوانُ المضمونيُّ** … » est rendu **collé** à la « حالةٌ حدّيّةٌ » qui le
    précède (même paragraphe à l'écran : le bloc `methode` ne crée pas de saut après sa liste). Le sortir en
    bloc propre, juste après la fermeture `:::` du `methode` :
    ```
    ::: propriete
    **العنوانُ المضمونيُّ** الذي قد يطلبُه الامتحانُ لكلِّ ركنٍ أو للنصِّ كلِّه عبارةٌ اسميّةٌ قصيرةٌ تلخّصُ ما يقولُه الجزءُ المحدَّدُ **كلُّه**، لا ما تقولُه فقرةٌ أخرى ولا تفصيلةٌ منه: لأطروحةِ نصِّ الحِرَفِ «جدارةُ الحِرَفِ اليدويّةِ بأن يتعلّمَها الشبابُ»، ولاستنتاجِه «إدخالُ الحِرَفِ في برامجِ المدارسِ».
    :::
    ```
  - « تطوّرُ الموقفِ » : bloc `propriete` rendu proprement (« خاصّية »).
- **Exactitude des ajouts selon les manuels** : « قد » توكيد avec le passé = 101909 p. 13 (liste de la famille
  التوكيد) lue avec 101908 (درس 14 : قد + ماضٍ = تحقيق) ; « قد » + présent = احتمال = 101908 p. 82 ✓. Le cas
  limite سلطة étend la définition « مرجع أدبي… أقوال وشواهد » de 101909 sans la contredire ✓. Titre, évolution
  d'un موقف et ألفاظ الشمول sont des savoir-faire d'épreuve, sans contradiction avec les manuels ✓.
- **Patron (mineur, R-6)** : « العنوان المضمونيّ » et « تطوّر الموقف » sont deux notions nouvelles enseignées en un
  seul énoncé, sans exemple résolu ni `::: verifie` (le patron demande les deux). Acceptable pour ce lot ; à
  compléter au prochain passage `content-cours`. Le tableau du ch. 10 l. 447 a une cellule rallongée : laisser
  `content:gates` (Prettier) réaligner.

## 5. Résumé

- **Clés fausses : 0** (40 questions re-résolues, 44 au total dans le lot, 11 désormais à 8 q.).
- **Majeurs restants : 2**, tous deux en **08 Q8** — R-1 (option d incohérente, étiquette inexacte) et R-2
  (« الجوابُ الأخيرُ », renvoi ordinal) ; textes ci-dessus.
- **Mineurs restants : 4** — R-3 (08 Q3 explication), R-4 (12 Q3 e), R-5 (rendu du paragraphe « العنوان
  المضمونيّ »), R-6 (patron des deux notions nouvelles).
- **Verdict : publiable après R-1 et R-2** (deux remplacements de texte dans un seul fichier, `08-…json`) ;
  R-3 à R-5 recommandés dans la même passe, R-6 au prochain passage du cours.

## Suite donnée par le pilote (2026-10-14)

R-1 à R-5 appliqués mot pour mot (texte de R-1 contrôlé contre la transcription 2025 générale, l. 32 :
« تَحطِيمَ الإِطَارِ الجَامِدِ لِلتَّخَصُّصِ الضَّيِّقِ » ; d = 78 car. > clé 66). R-6 (exemple résolu et `verifie`
pour « العنوان المضمونيّ » et « تطوّر الموقف ») reporté au prochain passage du cours. **L01 prêt à livrer.**
