# Audit indépendant — correction « clé la plus longue », SVT 9ᵉ, dossiers 01 · 02 · 03 · 04

> Mandat : `.claude/skills/content-engine/references/audit-correction.md`, appliqué à la lettre.
> Corpus relu : `/home/user/wt-svtkey` (branche `wip/svt-9eme-cle-longue`, tête `f894f272`), diff
> `git diff origin/main -- content/sciences-vie-terre/<CHAPITRE>` après `fetch origin main`.
> Référence : `cours.md` de chaque dossier + manuel 105905 (cache). Hors périmètre : les missions
> `exercices/*-examen-*`. L'auditeur n'a modifié aucun fichier du corpus.
> Indices de questions : 1-based. Longueurs en caractères (Python `len`) ; chaque correction proposée a
> été mesurée : la clé n'y redevient jamais strictement la plus longue.
> Rapport rédigé au fil de l'eau, un dossier après l'autre.

## Mesures (quiz + exercices 01-06, missions d'examen exclues)

| Dossier | n | clé strict. la plus longue avant → après | clé strict. la plus COURTE avant → après |
| ------- | - | ---------------------------------------- | ---------------------------------------- |
| 01-takathur-insan | 44 | 29 (65 %) → 0 | 1 (2 %) → 3 (6 %) |
| 01-wadhifat-al-ittisal | 46 | 28 (60 %) → 0 | 1 (2 %) → 1 (2 %) |
| 02-al-af3al-al-in3ikasiya | 46 | 33 (71 %) → 0 | 2 (4 %) → 6 (13 %) |
| 02-manaa | 44 | 33 (75 %) → 0 | 1 (2 %) → 5 (11 %) |
| 03-al-ibsar | 46 | 30 (65 %) → 0 | 1 (2 %) → 5 (10 %) |
| 03-wiratha | 44 | 19 (43 %) → 0 | 5 (11 %) → 5 (11 %) |
| 04-al-hajiyat-al-ghithaiya | 46 | 30 (65 %) → 0 | 2 (4 %) → 7 (15 %) |
| 04-zalazil | 44 | 32 (72 %) → 0 | 1 (2 %) → 3 (6 %) |

**Fuite inverse** : de 2 à 15 % selon le dossier, toujours sous le hasard (25 %). Elle n'est pas
exploitable. Les mesures du correcteur sont confirmées. La position de la clé n'a pas bougé
(b ≈ 50 %, d ≈ 2–5 %). Cette fuite préexistait et sort du mandat ; elle reste à traiter.

---

## Dossier 1 — `01-takathur-insan`

Relu : 29 questions touchées, leurs options non retouchées, le `cours.md`, et le reste du dossier
pour chercher les doublons. Résolution à l'aveugle : **aucune clé fausse**. Défauts : une clé
devenue inexacte, une clé tautologique, deux doublons de fait que la correction n'a pas défaits
(dont un qu'elle a aggravé), des distracteurs qui s'éliminent à vue.

### MAJOR

**M01t-1 — `exercices/03-boss.json` Q5, clé `b` : le raccourci rend la clé inexacte.**
« تغذية النطاف وحملها نحو البويضة » dit que le liquide séminal porte les spermatozoïdes jusqu'à
l'ovule. C'est faux : ils remontent les voies femelles par leur propre flagelle. Le cours dit seulement
« يغذّي النطاف وينقلها ».
- `b` ancien : `تغذية النطاف وحملها نحو البويضة` (31) → nouveau : `تغذية النطاف ونقلها عند القذف` (29 ; `d` = 34)

**M01t-2 — `exercices/04-defi.json` Q3, clé `b` : la clé est tautologique.**
L'énoncé demande *pourquoi* l'ovule se ferme après l'entrée d'un spermatozoïde. « لضمان اندماج نطفة
واحدة فقط » redit ce qui se passe sans donner la raison. La raison (le nombre de chromosomes) n'est plus
que dans l'explication. La clé recoupe aussi `quiz` Q6 (« نطفة واحدة فقط »).
- `b` ancien : `لضمان اندماج نطفة واحدة فقط` (27) → nouveau : `كي لا يختلّ عدد الصبغيّات في البيضة` (35 ; `c` = 40)

**M01t-3 — `exercices/02-tamrin.json` Q3 ↔ `quiz.json` Q3 : le doublon de fait reste entier.**
Le correcteur a réécrit l'énoncé, mais les deux questions ont les mêmes quatre options (في الرحم / في
المهبل / في البوق / في المبيض), le même fait (le lieu de la fécondation) et la même clé. C'est exactement
le cas du mandat : « mêmes options, même clé, deux énoncés ». Le fait est même testé une troisième fois
(`06-defi-concours` Q5). Le nouvel énoncé souffle en plus la réponse : la rencontre se fait entre
l'ovaire, que l'ovule a quitté, et le vagin, d'où partent les spermatozoïdes. Il faut donc réécrire
entièrement `02-tamrin` Q3 sur un fait du cours qui n'est testé nulle part : une seule ovule par cycle.
Clé gardée en `c`.
- énoncé : `كم بويضة ناضجة يطلقها المبيضان عادةً في كلّ دورة جنسية؟`
- `a` : `ملايين البويضات كالنطاف` (23) — retirer l'étiquette `bio.repro.fecondation-dans-l-uterus`, qui ne s'applique plus
- `b` : `بويضتان، واحدة من كلّ مبيض` (26)
- `c` (clé) : `بويضة واحدة من أحد المبيضين` (27)
- `d` : `عشر بويضات أو أكثر في كلّ أسبوع` (31)
- explication : `تُطلق المرأة عادةً بويضة واحدة ناضجة في كلّ دورة، من أحد المبيضين، عند الإباضة نحو منتصف الدورة. الملايين تخصّ النطاف عند الرجل لا البويضات، والمبيضان لا يطلقان بويضة معًا في كلّ دورة، والإباضة حدث شهريّ لا أسبوعيّ؛ وعدد البويضات محدود منذ الولادة.`

**M01t-4 — `exercices/02-tamrin.json` Q4 ↔ `quiz.json` Q7 : doublon de fait aggravé par la correction.**
Les deux questions portent sur le même fait, avec la même clé : le produit de la fusion est la cellule-œuf
(اللاقحة). Pour étoffer, le correcteur a ajouté « جنين (الـ)مكتمل النموّ » dans les deux, ce qui les
rapproche encore. On réécrit entièrement `02-tamrin` Q4 sur la durée de la grossesse, qui est dans le
cours et n'est testée nulle part. Clé gardée en `b`.
- énoncé : `كم يدوم الحمل عند المرأة تقريبًا؟`
- `a` : `نحو 3 أشهر` · `b` (clé) : `نحو 9 أشهر` · `c` : `نحو 12 شهرًا` · `d` : `نحو 6 أشهر` (10 à 12 caractères chacune)
- explication : `يدوم الحمل نحو 9 أشهر (38 إلى 40 أسبوعًا): تتطوّر البيضة المخصّبة إلى مضغة ثمّ إلى جنين يتغذّى عبر المشيمة، ثمّ تحدث الولادة. في 3 أو 6 أشهر لا يكون الجنين قد اكتمل نموّه، و12 شهرًا مدّة أطول من الحمل عند الإنسان.`

**M01t-5 — `quiz.json` Q7 : les trois distracteurs étoffés s'éliminent à vue.**
Les gloses ajoutées disent elles-mêmes ce que sont ces options :
- « الجنين المكتمل النموّ » : un fœtus achevé n'est pas une cellule ;
- « المشيمة الرابطة بين الأمّ والجنين » : un organe, postérieur à la grossesse ;
- « الجُريب الحاوي للبويضة » : un contenant, antérieur à la fécondation.

La clé est en outre la seule option avec une parenthèse. On revient à des noms nus, de même forme :
- `a` → `المضغة الأولى` (13)
- `b` (clé) `البيضة المخصّبة (اللاقحة)` → `البيضة المخصّبة` (15)
- `c` → `البويضة الناضجة` (15 ; confusion ovule / œuf)
- `d` → `الجُريب الناضج` (14)
- explication : `اندماج النطفة بالبويضة ينتج البيضة المخصّبة (اللاقحة)، وهي أوّل خليّة للكائن الجديد. المضغة مرحلة لاحقة تنشأ بعد انقسامات البيضة، والبويضة الناضجة هي المشيج الأنثويّ قبل الإلقاح لا بعده، والجُريب هو ما يحتوي البويضة داخل المبيض قبل الإباضة.`

**M01t-6 — `exercices/02-tamrin.json` Q5 ↔ `exercices/05-tadrib.json` Q5 : doublon de fait.**
Les deux questions demandent pourquoi les règles s'arrêtent pendant la grossesse. Les clés sont
équivalentes et les distracteurs `a` aussi (« المبيضان يتوقّفان / تعطّلا نهائيًّا »). Dans `05-tadrib`
Q5, `a` est de plus contredit par l'énoncé, puisque les règles reviennent. On réécrit entièrement
`05-tadrib` Q5 sur la date des règles suivantes. Le calcul est enseigné (exemple de سلمى) et n'est testé
nulle part. Clé gardée en `b`.
- énoncé : `امرأة دورتها منتظمة طولها 28 يومًا، وكان أوّل يوم لطمثها الأخير 1 مارس. في أيّ يوم يُنتظر طمثها التالي إن لم يحدث حمل؟`
- `a` : `نحو 14 مارس` · `b` (clé) : `نحو 29 مارس` · `c` : `نحو 1 أفريل` · `d` : `نحو 28 مارس` (11 caractères chacune)
- explication : `1 مارس هو اليوم الأوّل للدورة، والدورة 28 يومًا، فاليوم الأوّل للدورة الموالية هو 1 + 28 = 29 مارس (كما في مثال سلمى: 3 جانفي ثمّ 31 جانفي). 14 مارس قرب موعد الإباضة لا الطمث، و28 مارس آخر يوم من الدورة الحاليّة، و1 أفريل يفترض خطأً أنّ الدورة شهر كامل.`

**M01t-7 — `exercices/03-boss.json` Q3, distracteur `c` : l'ajout le fait contredire l'énoncé.**
L'énoncé pose que chaque gamète « يحمل نصف المعلومة الوراثية ». L'ajout « لا تحمل شيئًا » contredit
cette prémisse, et l'option tombe d'elle-même.
- `c` ancien : `لأنّ المشيج خليّة ميتة لا تحمل شيئًا` → nouveau : `لأنّ المشيج خليّة لم يكتمل نضجها بعد` (36 ; clé `b` = 36, `d` = 36)
- dans l'explication, remplacer `والمشيج خليّة حيّة` par `والمشيج خليّة ناضجة حيّة`.

**M01t-8 — `exercices/04-defi.json` Q2 : défaut préexistant signalé par le correcteur, ici corrigé.**
« وأجهزتها سليمة » élimine d'avance `b` (rareté de la muqueuse) et `d` (vagin court). La clé ne fait en
outre que reprendre l'énoncé (« خالٍ تمامًا من النطاف »). On retire la prémisse qui élimine `b` et l'on
remplace `d` par un distracteur qui empêcherait vraiment la fécondation mais qu'aucune donnée ne soutient.
- énoncé : `…خالٍ تمامًا من النطاف بينما تبويض المرأة وأجهزتها سليمة…` → `…خالٍ تمامًا من النطاف بينما تبويض المرأة منتظم…`
- `d` ancien : `قِصَر المهبل عن المعتاد عند المرأة` → nouveau : `انسداد البوقين عند المرأة` (25 ; clé `a` = 28)
- explication : remplacer `رغم سلامة جهة المرأة` par `مهما كانت حال المرأة`, et `وطول المهبل لا يمنع صعود النطاف لو وُجدت.` par `وانسداد البوقين لا تدلّ عليه أيّ معطيات، أمّا غياب النطاف فثابت بالتحليل.`

### MINOR

- **m01t-1 — `exercices/05-tadrib.json` Q4, `d`** : « …يسبق الإلقاح دائمًا بأيّام قليلة جدًّا قبل ذلك » est redondant (« يسبق » et « قبل ذلك » disent la même chose). → `التعشيش يسبق الإلقاح دائمًا ببضعة أيّام في المبيض` (49 ; clé `a` = 47).
- **m01t-2 — `exercices/06-defi-concours.json` Q6, `c`** : « لا يحدث إلّا … وحدها » répète la restriction deux fois. → `الحيض لا يحدث إلّا أثناء فترة الحمل نفسها` (41 = longueur inchangée ; clé 42, `b` 45).
- **m01t-3 — `exercices/02-tamrin.json` Q5, `c`** : l'ajout « فلا ينزل الطمث » se contredit (« plus de sang, donc pas de règles »). → `لأنّ الرحم يفرز دمًا أكثر من المعتاد` (36 ; clé 41, `a` 50).
- **m01t-4 — `exercices/04-defi.json` Q6, énoncé (préexistant)** : l'enfant est déjà né, alors que la clé parle du suivi pendant la grossesse et l'accouchement. → `امرأة حامل مصابة بفيروس السيدا. أيّ تدبير يقلّل خطر انتقال الفيروس إلى مولودها؟`
- **m01t-5 — `quiz.json` Q5** : la clé raccourcie est devenue la négation mot pour mot de `a` (« على حدوث إلقاح في الدورة » / « على عدم حدوث إلقاح في الدورة »). Un tel couple d'options contraires signale la paire où chercher. → `a` : `على حدوث إلقاح وبداية تعشيش` (27).
- **m01t-6 — notions absentes du cours (préexistant, non touché)** : `06-defi-concours` Q1 et Q3 invoquent LH et le corps jaune. LH n'est dans aucun `cours.md` de la matière. Le dossier, préfixé 01, est une « مراجعة جامعة » des chapitres 10 à 14. À traiter lors d'un passage de cohérence de l'ordre des chapitres.

### Paire laissée par le correcteur — tranchée

- **`04-defi` Q1 ↔ `06-defi-concours` Q2 (jour d'ovulation = longueur − 14 ; 30 et 32 jours) : acceptée.**
  Les données, les options et les clés diffèrent (16 / 18) : ce n'est pas un doublon de fait. On peut la
  garder comme exercice parallèle, à deux paliers.

### Défaut préexistant signalé par le correcteur

- `04-defi` Q2 `b`/`d` : corrigé ci-dessus (M01t-8).

### Questions relues sans constat

`quiz` Q1, Q3, Q4, Q8 · `02-tamrin` Q1, Q2, Q6 · `03-boss` Q1, Q4, Q6 · `04-defi` Q4, Q5 ·
`05-tadrib` Q3, Q6 · `06-defi-concours` Q1, Q3.

**Verdict 01-takathur-insan : à corriger avant publication.** 0 BLOCKER, 8 MAJOR (dont 3 doublons de fait),
6 MINOR. Aucune clé fausse.

---

## Dossier 2 — `01-wadhifat-al-ittisal`

Relu : 29 questions touchées, leurs options non retouchées, le `cours.md`, et le reste du dossier
pour chercher les doublons. Résolution à l'aveugle : **aucune clé fausse, aucune clé ambiguë**. La
correction a pourtant créé deux doublons de fait : en harmonisant des options, elle a rendu deux paires
de questions presque identiques.

### MAJOR

**M01w-1 — `exercices/02-tamrin.json` Q3 ↔ `quiz.json` Q4 : doublon de fait créé par la correction.**
Les énoncés étaient déjà presque identiques (« أين توجد المادّة السّنجابيّة في المخ(ّ) وأين توجد في
النّخاع الشّوكيّ؟ »), avec la même clé. En étoffant les distracteurs, le correcteur leur a donné le même
texte dans les deux fichiers (« في الخارج في المخ(ّ) وفي النّخاع معا » / « في الدّاخل … معا »). On a
désormais les mêmes options, la même clé et deux énoncés quasi identiques. On réécrit entièrement
`02-tamrin` Q3 : on demande à l'élève de déduire la couleur du cordon médullaire à partir de l'inversion
grise / blanche (cours : « حبل أبيض اللّون »). Clé gardée en `c`, et l'étiquette de `a` reste juste.
- énoncé : `يبدو النّخاع الشّوكيّ من الخارج بلون معيّن. ما هذا اللّون، ولماذا؟`
- `a` : `سنجابيّ، لأنّ السّنجابيّة في خارجه` (34) — étiquette `bio.nerv.substance-grise-toujours-dehors` conservée
- `b` : `سنجابيّ، لأنّ الأجسام الخلويّة تغلّفه` (37)
- `c` (clé) : `أبيض، لأنّ المادّة البيضاء في خارجه` (35)
- `d` : `أبيض، لأنّ السّحايا بيضاء اللّون` (32)
- explication : `في النّخاع الشّوكيّ تكون المادّة السّنجابيّة في الدّاخل وتحيط بها المادّة البيضاء، فيبدو النّخاع حبلًا أبيض اللّون. والموضع ينقلب في المخّ حيث السّنجابيّة في الخارج (القشرة)؛ ولون النّخاع يأتي من الأغمدة الدّهنيّة لألياف المادّة البيضاء لا من السّحايا.`

**M01w-2 — `exercices/06-defi-concours.json` Q6 ↔ `exercices/03-boss.json` Q4 : doublon de fait créé par la correction.**
La clé raccourcie de 06 Q6 (« لأنّ الأجسام الخلويّة تعالج والألياف تنقل ») est désormais la clé de
03-boss Q4 (« لأنّ البيضاء ألياف للنّقل، والسّنجابيّة أجسام للمعالجة »), reformulée. Les deux questions
portent sur le même fait, et le distracteur sur la couleur figure dans les deux (« لون المادّة… يحدّد »).
La partie supprimée (« فحيثما وُجدت معالجة وُجدت سنجابيّة… ») était justement ce qui distinguait 06 Q6.
On réécrit entièrement 06 Q6 en question d'application. Clé gardée en `a`.
- énoncé : `كشف المجهر في منطقة من النّخاع الشّوكيّ أليافًا عصبيّة كثيرة محاطة بأغمدة دهنيّة، ولا أجسام خلويّة فيها. ما هذه المادّة، وما دورها؟`
- `a` (clé) : `مادّة بيضاء تنقل السّيالة` (25)
- `b` : `مادّة سنجابيّة تعالج السّيالة` (29) — étiquette `bio.nerv.substances-grise-blanche-confondues`
- `c` : `مادّة بيضاء تعالج السّيالة` (26) — remplacer l'étiquette `bio.nerv.substance-grise-toujours-dehors` par `bio.nerv.substances-grise-blanche-confondues`
- `d` : `مادّة سنجابيّة تنقل السّيالة` (28)
- explication : `الألياف ذات الأغمدة الدّهنيّة هي ما يكوّن المادّة البيضاء ويعطيها لونها، ودورها النّقل. أمّا المعالجة فتتمّ في المادّة السّنجابيّة حيث توجد الأجسام الخلويّة، وهي غائبة هنا. فالبنية وحدها تكفي لتحديد المادّة ودورها.`
- (La clé est la plus courte d'un seul caractère, ce qui n'est pas exploitable dans une grille 2 × 2.)

**M01w-3 — `exercices/01-tamrin.json` Q3 (énoncé réécrit par le correcteur) : indice de forme et distracteurs faibles.**
Seule la clé porte le tanwīn (« مباشرةً » ; `b` a « مباشرة »). C'est « l'unique option vocalisée » que
nomme le mandat. De plus, `b` (« من الجلد ») et `d` (« من العضلات ») ne viennent pas d'une confusion
d'élève sur l'origine des nerfs crâniens.
- `c` (clé) : `من الدّماغ مباشرةً` → `من الدّماغ مباشرة` (17)
- `b` : `من الجلد مباشرة` → `من السّحايا المحيطة بالمخّ` (26)
- explication, ajouter : ` والسّحايا أغشية واقية لا تنبثق منها الأعصاب.`

### MINOR

- **m01w-1 — `quiz.json` Q5, `d` (défaut préexistant signalé)** : « 31 عصبا لا 31 زوجا » n'est pas une réponse à « كم عدد أزواج… », et sa forme le dénonce. → `d` : `43 زوجا` (7 = toutes les options) ; explication, ajouter : ` و43 هو مجموع الأزواج القحفيّة والشّوكيّة معًا لا عدد الشّوكيّة وحدها.`
- **m01w-2 — `exercices/04-defi.json` Q2, clé `a`** : en raccourcissant, on a perdu le verbe de la seconde proposition (« والثّاني منطقة العصب… » : « منطقة » reste sans prédicat ni accord). → `الأوّل يُشلّ جانبه الأيسر، والثّاني تُشلّ منطقة عصبه وحدها` (58 ; `c` = 59).
- **m01w-3 — doublon préexistant, `quiz.json` Q8 ↔ `exercices/01-tamrin.json` Q6** : le même énoncé (sens de l'influx dans le neurone), reformulé, avec la même clé ; `05-tadrib` Q1 le teste une troisième fois. On réécrit `01-tamrin` Q6 sur la place du cervelet (cours : « خلف المخ »), clé en `a` :
  énoncé `أين يوجد المخيخ؟` ; `a` `خلف المخّ، فوق البصلة الشّوكيّة` (31) ; `b` `أمام المخّ، داخل عظم الجبهة` (27) ; `c` `داخل النّخاع الشّوكيّ في الظّهر` (31) ; `d` `أسفل البصلة الشّوكيّة في العنق` (30) ; retirer les étiquettes `bio.nerv.sens-du-message-inverse` de `b` et `c` ; explication `يوجد المخيخ خلف المخّ، وتوجد تحته البصلة الشّوكيّة التي ترتبط بالنّخاع الشّوكيّ؛ والثّلاثة تكوّن الدّماغ داخل القحف. والنّخاع في العمود الفقريّ، وليس المخيخ فيه ولا في الجبهة.`
- **m01w-4 — `exercices/03-boss.json` Q1 ↔ `exercices/06-defi-concours.json` Q4** : les deux clés disent maintenant presque la même phrase (« كلّ نصف كرة يتحكّم في / مسؤولا عن الجانب المخالف »). Les questions restent distinctes (déduction à partir d'un cas / notion), donc on peut les garder. À reprendre si l'on veut réduire les recoupements.
- **m01w-5 — `exercices/04-defi.json` Q3, clé `b`** : la clé raccourcie ne traite plus le « رغم أنّه يصل إلى المخّ » de l'énoncé. L'explication le traite (« كلّ عصب خارجهما محيطيّ »), donc c'est acceptable.

### Défaut préexistant signalé par le correcteur

- `quiz` Q5 `d` : corrigé ci-dessus (m01w-1).

### Questions relues sans constat

`quiz` Q3, Q7, Q9 · `01-tamrin` Q4, Q5 · `02-tamrin` Q2, Q6 · `03-boss` Q2, Q5 · `04-defi` Q1, Q4, Q5, Q6 ·
`05-tadrib` Q4, Q5, Q6 · `06-defi-concours` Q2, Q3, Q5.

**Verdict 01-wadhifat-al-ittisal : à corriger avant publication.** 0 BLOCKER, 3 MAJOR (2 doublons créés
par la correction, 1 indice de forme), 5 MINOR. Aucune clé fausse.

---

## Dossier 3 — `02-al-af3al-al-in3ikasiya`

Relu : 33 questions touchées, leurs options non retouchées, le `cours.md`, et le reste du dossier
pour chercher les doublons. Résolution à l'aveugle : **aucune clé fausse**. Le dossier est très
redondant : le `quiz` et `02-tamrin` posent trois fois la même question. En raccourcissant les clés, la
correction les a rendues presque identiques d'un fichier à l'autre, et `content:tranche` n'a vu aucune
de ces paires (« 0 paire proche » pour 02).

### MAJOR

**M02a-1 — `exercices/02-tamrin.json` Q1 ↔ `quiz.json` Q6 : doublon de fait, aggravé.**
Les deux questions portent sur le stimulus réel du réflexe rotulien. Clés : « استطالة العضلة الباسطة » /
« استطالة العضلة الباسطة للسّاق ». Le distracteur `a` est le même (la frappe du marteau sur la peau).
On réécrit entièrement 02-tamrin Q1 sur le rôle du larmoiement, qui est dans le cours (« الدّمع يغسل
العين ويجرف الجسم الغريب ») et n'est testé nulle part. Clé gardée en `b`.
- énoncé : `يدخل غبار في العين فيسيل الدّمع. ما فائدة هذا الفعل الانعكاسيّ؟`
- `a` : `تغذية العين بالماء والأملاح` (27) — retirer l'étiquette `bio.nerv.stimulus-du-reflexe-rotulien`
- `b` (clé) : `غسل العين وجرف الجسم الغريب` (27)
- `c` : `تحسين الرّؤية في الضّوء القويّ` (30)
- `d` : `تبريد العين بعد ارتفاع حرارتها` (30)
- explication : `فائدته وقائيّة: الدّمع يغسل العين ويجرف الجسم الغريب، وهذا من أدوار الأفعال الانعكاسيّة في وقاية الجسم من الأخطار. والعضو المنفّذ هنا غدّة تفرز، والإفراز لا علاقة له بتغذية العين ولا بتحسين الرّؤية ولا بتبريدها.`

**M02a-2 — `exercices/02-tamrin.json` Q2 ↔ `quiz.json` Q7 : doublon de fait, aggravé.**
Même fait (réflexe rotulien conservé sous anesthésie générale) et même clé. Après raccourcissement, les
deux clés finissent par « …ليس من عناصر القوس (النّخاعيّ) الخمسة ». On réécrit entièrement 02-tamrin
Q2 sur la vivacité anormale du réflexe (cours : « تحدث بصفة مُبالغ فيها … في حالات مرضيّة »). Clé
gardée en `b` ; les étiquettes de `c` et `d` restent justes.
- énoncé : `يجد الطّبيب الفعل الرّضفيّ عند مريض مبالغًا فيه، أي أقوى بكثير من المعتاد. علامَ يدلّ ذلك؟`
- `a` : `أنّ عضلات المريض قويّة جدّا` (27)
- `b` (clé) : `أنّ حالته العصبيّة قد تكون مضطربة` (33)
- `c` : `أنّ المخّ صار يقود هذا الفعل مباشرة` (35) — étiquette `bio.nerv.cerveau-dans-l-arc-reflexe` conservée
- `d` : `أنّ الفعل صار مكتسبًا بالتّعوّد` (31) — étiquette `bio.nerv.inne-pris-pour-acquis` conservée
- explication : `يتّخذ الأطبّاء حدّة الأفعال الانعكاسيّة دليلًا على الحالة العصبيّة: الفعل الغائب أو البطيء أو المبالغ فيه علامة على اضطراب في المسار العصبيّ. وقوّة العضلة لا تفسّر وحدها هذه المبالغة، والمخّ ليس من عناصر القوس، والفعل الانعكاسيّ فطريّ لا يُكتسب بالتّعوّد.`

**M02a-3 — `exercices/02-tamrin.json` Q5 ↔ `quiz.json` Q3 : doublon de fait.**
Les deux questions décrivent la même expérience (anesthésie de la peau de la grenouille, aucun mouvement)
et ont la même clé (« المستقبل الحسّيّ ضروريّ ل(حدوث) الفعل »). Les distracteurs se recoupent : « العضلة
غير قادرة على التّقلّص » se retrouve dans les deux. On réécrit 02-tamrin Q5 sur une autre ligne du
tableau du cours (« قطع عصب النّسا … لا حركة … النّاقل ضروريّ »). Clé gardée en `c` ; `a`, `b` et `d`
restent inchangés, étiquettes comprises.
- énoncé : `في تجربة الضّفدعة النّخاعيّة، بعد قطع عصب النّسا الأيمن لم تحدث أيّ حركة عند وخز القدم اليمنى. ماذا نستنتج مباشرة؟`
- `c` (clé) : `أنّ المستقبل الحسّيّ ضروريّ للفعل` → `أنّ العصب النّاقل ضروريّ للفعل` (30 ; `a` = 30, `b` = 36)
- explication : `القطع ألغى النّاقل وحده، وبقي المستقبل والنّخاع والعضلة سليمة؛ فاختفاء الحركة يُنسب إلى ما أُلغي: النّاقل ضروريّ. ولا شيء في التّجربة يدلّ على عطب المركز أو العضلة، وقطع عصب رجل واحدة لا يشلّ الضّفدعة كلّها.`

**M02a-4 — `exercices/03-boss.json` Q1, clé `a` : clé tautologique, avec un indice de forme.**
L'énoncé dit que les trois expériences donnent le même résultat et demande pourquoi ce résultat ne
suffit pas. La clé raccourcie le redit (« نتيجة مشتركة بين الثّلاث فلا تسمّي العنصر »). La raison (la
comparaison de deux expériences qui ne diffèrent que d'un élément) a été retirée. La clé est en outre la
seule option entre guillemets (« «لا حركة» »).
- `a` ancien : `لأنّ «لا حركة» نتيجة مشتركة بين الثّلاث فلا تسمّي العنصر` (56) → nouveau : `لأنّ ما يسمّي العنصر هو مقارنة تجربتين لا تختلفان إلّا فيه` (58 ; `b` = 59)

**M02a-5 — `exercices/06-defi-concours.json` Q4 : notion absente du cours (préexistante, question touchée).**
La clé et l'explication reposent sur le freinage du réflexe par le cerveau (« المخّ قد يكبح القوس »).
« كبح » ne figure nulle part dans `cours.md`, qui dit au contraire « نتيجته لا تتلوّث بإرادة المريض ولا
بانتباهه ». Il y a deux corrections possibles :
- ajouter au cours, dans « 🩺 الفعل الانعكاسي الرّضفي », après la liste numérotée : `> 🔮 المخّ ليس من عناصر القوس، لكنّه قد يكبح بعض الأفعال الانعكاسيّة أو يسهّلها؛ ولهذا يطلب الطّبيب أحيانًا من المريض أن يشبك يديه ويشدّهما ليشغل انتباهه.`
- puis, dans le même cours, corriger la contradiction : `نتيجته لا تتلوّث بإرادة المريض ولا بانتباهه` → `نتيجته لا تتوقّف على إرادة المريض`.

### MINOR

- **m02a-1 — `quiz.json` Q1 (préexistant)** : la clé est la réunion de `a` (« خارجيّة فقط ») et de `c` (« داخليّة فقط »). C'est le motif « clé = moitié de chaque distracteur ». → `c` : `تقلّصات تلقائيّة للعضلة دون منبّه` (33 ; clé 28, `a` 34) ; dans l'explication, ajouter : ` ولا فعل انعكاسيًّا دون منبّه.`
- **m02a-2 — `exercices/04-defi.json` Q5, clé `a`** : « القوس القطنيّ » (le niveau lombaire) n'est pas dans le cours. → `لأنّ الإصابة فوق مركزه، والقوس تحتها سليم` (41 ; `c` = 43). Dans l'explication, remplacer `يغلق في الجزء القطنيّ من النّخاع، أي تحت الإصابة` par `يغلق في جزء من النّخاع يقع تحت الإصابة`.
- **m02a-3 — `exercices/05-tadrib.json` Q3 ↔ `exercices/01-tamrin.json` Q1 (préexistant)** : même définition, même clé (« منذ الولادة وبنفس الطّريقة / ثابت عند كلّ الأفراد ») et mêmes distracteurs étiquetés (« تدريب », « يختلف من شخص إلى آخر »). Réécriture de 05-tadrib Q3, clé en `c` : énoncé `أيّ هذه الأفعال الانعكاسيّة دوره تنظيم وظيفة داخليّة في الجسم؟` ; `a` `سحب اليد عن جسم ساخن` (20) ; `b` `الطّرفة أمام ضوء قويّ` (21) ; `c` `تنظيم إيقاع التّنفّس` (20) ; `d` `ركوب الدّرّاجة دون سقوط` (23) ; retirer les étiquettes de `a`, `b` et `d` ; explication `تؤدّي الأفعال الانعكاسيّة ثلاثة أدوار: وقاية الجسم من الأخطار، وحفظ توازنه، وتنظيم وظائف داخليّة كالتّنفّس والتّغذية. فسحب اليد والطّرفة فعلان انعكاسيّان دورهما وقائيّ، وركوب الدّرّاجة سلوك مكتسب بالتّدريب لا فعل انعكاسيّ.` Cette réécriture comble aussi le manque laissé par `01-tamrin` Q6 : sa clé a perdu le troisième rôle (« تنظيم وظائف أعضائه الدّاخليّة »).
- **m02a-4 — `exercices/05-tadrib.json` Q5, clé `b`** : dans « ومقارنته بالشّاهد », le pronom renvoie à l'élément modifié, alors que ce qu'on compare au témoin, c'est l'expérience. Un ajustement qui garde la clé ≤ 48 caractères est souhaitable ; on peut aussi l'accepter tel quel, car le sens reste compris.
- **m02a-5 — recoupements préexistants à surveiller** : `quiz` Q8 ↔ `01-tamrin` Q5 (organe effecteur de la salivation, même clé, fichiers non touchés) ; `quiz` Q9 ↔ `03-boss` Q6 (« الحلقة / مساره أقصر ») ; `quiz` Q5 ↔ `05-tadrib` Q1 ↔ `01-tamrin` Q2 (les cinq éléments de l'arc).

### Questions relues sans constat

`quiz` Q5, Q7, Q9, Q10 · `01-tamrin` Q1, Q6 · `02-tamrin` Q6 · `03-boss` Q2, Q3, Q4, Q5, Q6 ·
`04-defi` Q3, Q4, Q6 · `05-tadrib` Q2, Q4, Q6 · `06-defi-concours` Q1, Q2, Q3, Q5, Q6.

**Verdict 02-al-af3al-al-in3ikasiya : à corriger avant publication.** 0 BLOCKER, 5 MAJOR (3 doublons de
fait aggravés, 1 clé tautologique avec guillemets, 1 notion non enseignée), 5 MINOR. Aucune clé fausse.

---

## Dossier 4 — `02-manaa`

> Chapitre complémentaire, « خارج البرنامج الرسمي ». Il est relu au même niveau d'exigence.

Relu : 29 questions touchées, leurs options non retouchées, le `cours.md`, et le reste du dossier
pour chercher les doublons. Résolution à l'aveugle : **aucune clé fausse, aucune clé ambiguë**. Les
clés raccourcies restent justes à la lettre. Le dossier pose plusieurs fois la même question : une
seule notion (vaccin et sérum, mémoire immunitaire, mécanisme du SIDA) revient trois ou quatre fois. En
raccourcissant clés et distracteurs, la correction a fait converger ces paires.

### MAJOR

**M02m-1 — `exercices/05-tadrib.json` Q1 ↔ `quiz.json` Q1 : doublon de fait aggravé.**
Les deux questions portent sur la définition de l'antigène. Les clés sont désormais calquées l'une sur
l'autre (« جزيء / جسم غريب يستثير ردّ فعل دفاعيًّا / مناعيًّا »). Deux distracteurs sont communs : « جسم
مضادّ ينتجه الجسم… » et « دواء يقتل البكتيريا (مباشرةً) داخل الجسم ». On réécrit entièrement 05-tadrib
Q1 sur le critère soi / non-soi, qui est dans le cours et n'est testé nulle part. Clé gardée en `a`.
- énoncé : `يميّز جهاز المناعة بين ما يهاجمه وما يتركه. ما المعيار الذي يعتمده؟`
- `a` (clé) : `على كونه غريبًا عن الجسم لا ذاتيًّا` (35)
- `b` : `على كونه كبير الحجم مهما كان أصله` (33)
- `c` : `على كونه حيًّا يتكاثر داخل الجسم` (32)
- `d` : `على كونه من خلايا الجسم السّليمة نفسها` (38)
- explication : `يميّز جهاز المناعة «الذاتي» (من الجسم) من «غير الذاتي» (الغريب)، ويهاجم الغريب وحده: ميكروبًا كان أو سُمًّا يفرزه أو خليّة غريبة. فالحجم ليس معيارًا، والسُّمّ مستضدّ رغم أنّه لا يتكاثر، وخلايا الجسم السّليمة لا يهاجمها.`

**M02m-2 — `exercices/05-tadrib.json` Q5 ↔ `exercices/02-tamrin.json` Q5 : doublon de fait aggravé.**
Les deux questions portent sur la mémoire immunitaire au deuxième contact, et les clés sont équivalentes.
La correction a rendu le distracteur `c` identique dans les deux (« لأنّ الجلد يصبح أكثر سُمكًا بعد
المرض »), et `a` l'est presque (« الميكروب يضعف / يصبح أضعف من تلقاء نفسه »). On réécrit entièrement
05-tadrib Q5 sur le pus, qui est dans le cours (« خليط من كريات بيضاء وميكروبات ميتة ») et n'est testé
nulle part. Clé gardée en `b`.
- énoncé : `يظهر القيح (الصّديد) في جرح ملتهب. ممّ يتكوّن؟`
- `a` : `كريات حمراء تجمّعت في الجرح` (27)
- `b` (clé) : `كريات بيضاء وميكروبات ميتة` (26)
- `c` : `أجسام مضادّة تجمّدت في الجلد` (28)
- `d` : `مصل يفرزه الجلد لتعقيم الجرح` (28)
- explication : `القيح خليط من كريات بيضاء وميكروبات ميتة بعد معركة البلعمة، فهو دليل على نشاط الدفاع غير النوعيّ في مكان العدوى. الكريات الحمراء تنقل الأكسجين ولا تبتلع الميكروبات، والأجسام المضادّة ذائبة في الدم، والجسم لا يفرز «مصلًا».`

**M02m-3 — `exercices/06-defi-concours.json` Q2 ↔ `exercices/04-defi.json` Q1 : doublon de fait.**
Les deux énoncés décrivent la même courbe (une première réponse lente et faible, une seconde rapide et
forte) et ont la même clé (« الذاكرة المناعية »). Le fait est testé une quatrième fois avec 02-tamrin Q5
et l'ancienne 05-tadrib Q5. On réécrit entièrement 06 Q2 sur les barrières chimiques (cours : sueur,
salive, larmes, « العصارة المعدية الحمضية »). Clé gardée en `a`.
- énoncé : `بعض الحواجز الطبيعيّة ميكانيكيّة وبعضها كيميائيّ يقتل الجراثيم. أيّ ممّا يلي حاجز كيميائيّ؟`
- `a` (clé) : `العصارة المعدية الحمضية` (23)
- `b` : `الجلد السليم` (12)
- `c` : `الأجسام المضادّة في الدم` (24)
- `d` : `الكريات البيضاء البلعمية` (24)
- explication : `العصارة المعدية الحمضية، ومثلها العرق واللعاب والدموع، إفرازات تقتل الجراثيم: حواجز كيميائيّة. أمّا الجلد السليم فحاجز ميكانيكيّ يمنع العبور، والأجسام المضادّة والكريات البيضاء خطوط دفاع داخليّة تتدخّل بعد اختراق الحواجز، فليست حواجز طبيعيّة.`

**M02m-4 — `exercices/06-defi-concours.json` Q4 ↔ `quiz.json` Q7 : doublon de fait aggravé.**
L'énoncé est le même (« ما الفرق الأساسي بين التلقيح والمصل »), la clé aussi. Le distracteur inversé de
06 Q4 `b`, une fois étoffé, est devenu la paraphrase de `quiz` Q7 `a`. On réécrit entièrement 06 Q4 sur
le cas du paysan que le cours développe dans `::: verifie`, et que seul le cours pose. Clé gardée en `a`.
- énoncé : `فلّاح غير ملقَّح جرح يده بأداة صدئة فحُقن مصلًا مضادًّا للكزاز. بعد ستّة أشهر جُرح من جديد. هل ما زال ذلك المصل يحميه؟`
- `a` (clé) : `لا، فأجسام المصل زالت ولم تترك ذاكرة` (36)
- `b` : `نعم، فالمصل يترك ذاكرة تدوم سنوات` (33) — étiquette `bio.immun.vaccin-serum-inverses` conservée
- `c` : `نعم، لأنّ جسمه صنع أجسامًا من المصل` (35)
- `d` : `لا، لأنّ المصل لا يؤثّر في الكزاز أصلًا` (39) — retirer l'étiquette `bio.immun.vaccin-serum-inverses`
- explication : `أجسام المصل المضادّة جاهزة لم يصنعها جسم الفلّاح، فتزول بعد مدّة قصيرة ولا تترك ذاكرة؛ فهو غير محميّ بعد ستّة أشهر، وكان يلزمه اللقاح أيضًا ليصنع أجسامه وخلايا ذاكرته. والمصل فعّال فعلًا ضدّ الكزاز، لكنّ مفعوله قصير.`

**M02m-5 — `exercices/03-boss.json` Q6 ↔ `quiz.json` Q8 : doublon de fait aggravé.**
La correction a retiré de la clé du `quiz` Q8 ce qui la distinguait (« وتظهر أمراض انتهازية »). Les deux
clés disent maintenant « تدمير اللمفاويات T يُضعف/فينهار جهاز المناعة ». Les distracteurs `a` (« يقوّي
اللمفاويات ») et `d` (« فائض / إنتاج مفرط للأجسام المضادّة ») sont parallèles, et `04-defi` Q4 teste le
même mécanisme une troisième fois. On réécrit entièrement 03-boss Q6 sur la prévention, qui est dans le
cours et n'est testée nulle part. Clé gardée en `b`.
- énoncé : `أيّ إجراء يقي فعلًا من انتقال فيروس السيدا (VIH)؟`
- `a` : `تجنّب مصافحة المصابين ومجالستهم في القسم` (40) — étiquette conseillée `bio.sante.transmission-vih-par-contact`
- `b` (clé) : `استعمال أدوات حقن معقّمة وعدم تبادلها` (37)
- `c` : `أخذ مضادّ حيويّ بعد كلّ جرح` (27) — étiquette conseillée `bio.sante.agent-pathogene-confondu`
- `d` : `تلقّي مصل مضادّ للسيدا مرّة في كلّ سنة` (38)
- explication : `ينتقل VIH بالدم الملوّث، فأدوات الحقن المعقّمة غير المتبادلة تقطع هذا الطريق، ومعها تحاليل الدم المنقول والوسائل الواقية. أمّا المصافحة والمجالسة فلا تنقلانه أصلًا، والمضادّ الحيويّ لا يؤثّر في الفيروسات، ولا يوجد مصل يقي من السيدا.`

### MINOR

- **m02m-1 — `exercices/04-defi.json` Q2, `c` et `d`** : le correcteur a remplacé `d` par une deuxième version de `c` (« أقوى بنية » / « أضعف بنية »). Les deux options tombent ensemble. → `d` : `الفأر (أ) صار مقاوِمًا لكلّ الميكروبات لا لهذا وحده` (51 ; clé 53, `a` 62) ; explication : remplacer la dernière phrase par `ولا شيء في التجربة يدلّ على فرق في البنية بين الفأرين، والمناعة المكتسبة نوعيّة: تحمي من هذا الميكروب وحده لا من كلّ الميكروبات.`
- **m02m-2 — `quiz.json` Q7, `c`** : la cheville « عند الأفراد » n'ajoute rien. → `كلاهما يحقن أجسامًا مضادّة جاهزة وتأثيرهما يدوم سنوات` (le sens est inchangé et la longueur reste ≤ 83).
- **m02m-3 — `exercices/05-tadrib.json` Q4, `c`** : « يقي من كلّ المرض » est mal construit. → `المضادّ الحيوي لأنّه يقي من كلّ الأمراض` (39 ; clé 37, `b` 42).
- **m02m-4 — recoupements préexistants** (fichiers distincts, à surveiller) : `quiz` Q2 ↔ `05-tadrib` Q2 ↔ `01-tamrin` Q4 (première ligne de défense) ; `quiz` Q6 ↔ `06-defi-concours` Q1 (spécificité de l'anticorps) ; `01-tamrin` Q5 ↔ `04-defi` Q5 (antibiotique et virus).
- **m02m-5** : dans les explications de `04-defi` Q2 et `06-defi-concours` Q5, le correcteur a remplacé « (أ) / (ب) » par des périphrases. Ces lettres désignaient les souris de l'énoncé, pas des options : le remplacement n'était pas nécessaire, mais il ne nuit pas.

### Questions relues sans constat

`quiz` Q1, Q6, Q8 · `01-tamrin` Q3, Q4, Q5, Q6 · `02-tamrin` Q1, Q2, Q3 · `03-boss` Q1, Q2, Q3, Q4 ·
`04-defi` Q1, Q3, Q4, Q5 · `05-tadrib` Q2, Q3, Q6 · `06-defi-concours` Q1, Q5, Q6.

**Verdict 02-manaa : à corriger avant publication.** 0 BLOCKER, 5 MAJOR (tous des doublons de fait, quatre
aggravés par la correction), 5 MINOR. Aucune clé fausse.

---

## Dossier 5 — `03-al-ibsar`

Relu : 34 questions touchées, dont 5 dont le correcteur a réécrit l'énoncé (des doublons), leurs options
non retouchées, le `cours.md`, et le reste du dossier pour chercher les doublons. Résolution à
l'aveugle : **aucune clé fausse**. Mais trois des cinq réécritures de « doublon » ont créé un nouveau
doublon. Deux d'entre eux sont dans le même exercice que la question réécrite.

### MAJOR

**M03i-1 — `exercices/01-tamrin.json` Q1, Q2 et Q3 : trois questions du même exercice ont la même clé et le même fait.**
- Q1 (réécrite) : « أيّ غشاء يبطّن جدار العين من الداخل ويحمل المستقبلات البصريّة؟ », clé « الشّبكيّة ».
- Q2 (réécrite) : « أيّ جزء من العين يحوّل الضّوء إلى سيالة عصبيّة؟ », clé « الشّبكيّة ».
- Q3 (non touchée) : « أين توجد المستقبلات البصريّة؟ », clé « في الشّبكيّة ».

Les trois clés désignent la rétine et l'option « القرنيّة » revient dans les trois. L'explication de Q2
répond même à Q3 (« المستقبلات البصريّة توجد في الشّبكيّة وحدها »). On réécrit Q1 et Q2 sur des faits
du cours que rien ne teste.

*Q1 → la sclérotique, clé gardée en `b`* (les options sont des noms seuls, de 7 à 9 caractères) :
- énoncé : `أيّ غشاء من أغشية جدار العين أبيض صلب وسميك، ووجهه الأماميّ هو بياض العين؟`
- `a` : `الشّبكيّة` · `b` (clé) : `الصّلبة` · `c` : `القرنيّة` (étiquette `bio.vis.cornee-quatrieme-membrane` conservée) · `d` : `المشيميّة`
- explication : `الصّلبة غشاء أبيض صلب وسميك يقي العين، ووجهها الأماميّ هو بياض العين، وتتواصل في الأمام بالقرنيّة الشّفّافة. والمشيميّة غشاء رقيق غنيّ بالشّعيرات، والشّبكيّة غشاء رقيق يحمل المستقبلات، والقرنيّة ليست غشاءً رابعًا بل استمرار الصّلبة الشّفّاف.`

*Q2 → l'œil sec (le `verifie` du cours), clé gardée en `a`* :
- énoncé : `لماذا يضرّ جفاف العين بالإبصار، ولو لم تُصَب العين بأيّ مرض؟`
- `a` (clé) : `لأنّ القرنيّة تفقد صفاءها فيتشوّش الضّوء` (40)
- `b` : `لأنّ الشّبكيّة تفقد مستقبلاتها البصريّة` (39) — retirer l'étiquette `bio.vis.recepteurs-hors-retine`
- `c` : `لأنّ الحدقة تنغلق تمامًا عند جفاف العين` (39)
- `d` : `لأنّ العصب البصريّ يتوقّف عن نقل السّيالة` (41)
- explication : `الدّمع يحافظ على رطوبة الوجه الأماميّ للعين وينظّفه؛ وبجفافه تفقد القرنيّة الشّفّافة صفاءها، فيتشوّش الضّوء قبل أن يبلغ الشّبكيّة. والجفاف لا يمسّ مستقبلات الشّبكيّة ولا العصب البصريّ في العمق، ولا يغلق الحدقة.`
- `difficulty` : passer de 1 à 2 (il faut raisonner).

**M03i-2 — `exercices/03-boss.json` Q6 (énoncé réécrit) ↔ `exercices/04-defi.json` Q1 : doublon créé par la réécriture.**
La nouvelle Q6 (un choc à l'arrière de la tête détruit les centres visuels, les yeux sont sains → cécité)
reprend le cas de 04-defi Q1 (des yeux sains, une lésion à l'arrière de la tête → la coupure est dans les
centres visuels). L'explication de `quiz` Q9 dit la même chose (« إتلاف منطقة في قفا الرّأس … رغم سلامة
العينين »). On réécrit Q6 sur le seul stade du mécanisme qu'aucune question ne teste : le stade 2,
illustré dans le cours par le diabétique au décollement de rétine. Clé gardée en `b`.
- énoncé : `مريض بالسّكّري حدث عنده نزف في أوعية الشّبكيّة ثمّ انفصال شبكيّ، ففقد الإبصار بتلك العين. في أيّ مرحلة من آليّة الإبصار يقع العطب؟`
- `a` : `في عبور الضّوء للأوساط الشّفّافة` (32)
- `b` (clé) : `في نشأة السّيالة بالشّبكيّة` (27)
- `c` : `في نقل السّيالة بالعصب البصريّ` (30)
- `d` : `في تحليلها بمراكز المخّ` (23)
- explication : `الأوساط الشّفّافة سليمة والضّوء يعبر، لكنّ المستقبلات الحسّيّة في الشّبكيّة تضرّرت، فلا تنشأ السّيالة العصبيّة أصلًا: العطب في المرحلة الثّانية. والعصب البصريّ ومراكز الإبصار سليمة، لكن لا شيء يصلها.`

**M03i-3 — `exercices/02-tamrin.json` Q2 ↔ `quiz.json` Q5 : doublon de fait que la correction n'a pas vu, et qu'elle a aggravé.**
L'énoncé est le même mot pour mot (« إذا كان الخيال (المتشكّل) على الشّبكيّة مقلوبًا، فلماذا لا نرى
الأشياء مقلوبة؟ »), la clé aussi (le cerveau). En étoffant, le correcteur a calqué les distracteurs d'une
question sur ceux de l'autre : « الشّبكيّة تعيد قلب / تصلح اتّجاه الخيال قبل إرساله » et « الجسم
البلّوريّ يعيد قلب / يصحّح الاتّجاه ». On réécrit entièrement 02-tamrin Q2 sur la tache aveugle qui
passe inaperçue (cours : « المخ يملأ الفراغ بما تراه العين الأخرى »). Clé gardée en `c`.
- énoncé : `في كلّ شبكيّة نقطة عمياء لا مستقبلات فيها، ومع ذلك لا نلاحظ ثقبًا في ما نراه. لماذا؟`
- `a` : `لأنّ الجسم البلّوريّ يحرّك الخيال بعيدًا عنها` (45) — étiquette `bio.vis.image-redressee-par-l-oeil` conservée (motif « l'œil corrige lui-même »)
- `b` : `لأنّ الشّبكيّة تجدّد مستقبلاتها فيها باستمرار` (45) — même étiquette, conservée
- `c` (clé) : `لأنّ المخّ يملأ الفراغ بما تراه العين الأخرى` (44)
- `d` : `لأنّ العصب البصريّ نفسه يلتقط الضّوء هناك` (41)
- explication : `في النّقطة العمياء يخرج العصب البصريّ فلا توجد مستقبلات، والنّقص حقيقيّ في الشّبكيّة. لكنّ المخّ يملأ الفراغ بما تراه العين الأخرى وبما يجاوره، فلا نلاحظه. والجسم البلّوريّ لا يحرّك الخيال، والمستقبلات لا تنشأ في هذا الموضع، والعصب ينقل السّيالة ولا يلتقط الضّوء.`

### MINOR

- **m03i-1 — `exercices/05-tadrib.json` Q6, clé `a`** : le raccourci « ويغطّي مقدّمة العين » inclut la cornée, que la conjonctive ne recouvre pas. Le cours dit « للجزء الأبيض الأمامي ». → `يبطّن الجفنين ويغطّي بياض العين الأماميّ` (40 ; `b` = 40).
- **m03i-2 — `exercices/01-tamrin.json` Q4, `d`** : la lumière passe bien par la pupille entre l'humeur aqueuse et le cristallin. Seul le mot « الوسط » de l'énoncé exclut `d`. Le piège est subtil mais tenable, car l'explication le dit (« الحدقة فتحة لا وسط شفّاف »). On peut le garder.
- **m03i-3 — `quiz.json` Q6 ↔ `exercices/04-defi.json` Q4 (préexistant)** : le même cas (l'élève qui ne lit pas le tableau mais lit son livre) et la même première moitié de clé (« قصر (ال)بصر »). Seconde moitié différente (lentille / examen). À surveiller.

### Paire laissée par le correcteur — tranchée

- **`quiz` Q7 ↔ `03-boss` Q1 : acceptée.** Les faits sont distincts (hypermétrope, image d'un objet
  proche, derrière la rétine / myope, image d'un objet lointain, devant), mais les listes d'options sont
  presque les mêmes et les clés inversées. Comme les deux questions sont dans des fichiers différents, ce
  n'est pas un « miroir du même exercice ». `06-defi-concours` Q2 réunit d'ailleurs les deux faits dans
  ses options `a` et `b`, ce qui est voulu. La paire peut rester.

### Questions relues sans constat

`quiz` Q1, Q5, Q8, Q9, Q10 · `01-tamrin` Q4, Q5 · `02-tamrin` Q1, Q4, Q5 · `03-boss` Q2, Q3, Q5 ·
`04-defi` Q1, Q2, Q3, Q4, Q5, Q6 · `05-tadrib` Q1, Q2, Q3, Q4 · `06-defi-concours` Q1 à Q6.
(La réécriture de `02-tamrin` Q1, l'œil comparé à une lentille convergente, est saine. La lentille
convergente est au cours : « كعدسة لامّة تمامًا ».)

**Verdict 03-al-ibsar : à corriger avant publication.** 0 BLOCKER, 3 MAJOR (4 questions à réécrire, dont 3
doublons créés par les réécritures du correcteur), 3 MINOR. Aucune clé fausse.

---

## Dossier 6 — `03-wiratha`

> Chapitre complémentaire, « خارج البرنامج الرسمي ».

Relu : 21 questions touchées, leurs options non retouchées, le `cours.md`, et le reste du dossier
pour chercher les doublons. Résolution à l'aveugle : **aucune clé fausse**. Les calculs ont été refaits
(1/16, 3/16, 50 %, 1/2) et sont justes. Défauts : un doublon créé par une réécriture du correcteur, et
trois doublons de fait que la correction n'a pas vus (dont un énoncé identique mot pour mot).

### MAJOR

**M03w-1 — `exercices/05-tadrib.json` Q6 ↔ `exercices/03-boss.json` Q5 : énoncé identique, doublon de fait que la correction n'a pas vu.**
Les deux demandent « لماذا يُعدّ الـ ADN «حاملًا للبرنامج الوراثي»؟ », avec la même clé (« يحمل / يخزّن
… التي تحدّد الصفات ») et des distracteurs parallèles (« صفة مكتسبة من المحيط / يكتسب الصفات من البيئة »).
On réécrit entièrement 05-tadrib Q6 sur la définition des allèles, qui est au cours et n'est jamais
demandée directement. Clé gardée en `a`.
- énoncé : `ما المقصود بالحليلات (allèles)؟`
- `a` (clé) : `أشكال مختلفة للمورّثة نفسها` (27)
- `b` : `صبغيّات جنسيّة تحدّد الجنس` (26)
- `c` : `أزواج الصبغيّات الجسميّة كلّها` (30)
- `d` : `خلايا تناسليّة تحمل 23 صبغيًّا` (30)
- explication : `لكلّ مورّثة أشكال مختلفة تُسمّى الحليلات (مثل B وb لمورّثة لون العينين)، ويملك الفرد حليلين لكلّ مورّثة: واحدًا من الأب وواحدًا من الأمّ. فالحليل ليس صبغيًّا كاملًا ولا زوجًا من الصبغيّات، وليس خليّة تناسليّة.`

**M03w-2 — `exercices/05-tadrib.json` Q1 (énoncé réécrit) : la réécriture crée un doublon.**
La nouvelle Q1 (« ما دور الصبغيّات؟ » → « حمل المورّثات المحدّدة للصفات ») reprend le fait de 03-boss Q5
(« الـ ADN يحمل المورّثات التي تحدّد الصفات ») et, avant M03w-1, celui de Q6 du même fichier, avec le même
distracteur sur l'énergie. On réécrit Q1 sur les autosomes (cours : « 22 زوجًا … متطابقة عند الذكر
والأنثى »). Clé gardée en `a`.
- énoncé : `ما الذي يميّز الصبغيّات الجسميّة (22 زوجًا) عند الإنسان؟`
- `a` (clé) : `أنّها متطابقة عند الذكر والأنثى` (31)
- `b` : `أنّها تحدّد جنس المولود وحدها` (29)
- `c` : `أنّها لا توجد إلّا في الأمشاج` (29)
- `d` : `أنّها تأتي كلّها من الأمّ وحدها` (31)
- explication : `في خلايا الإنسان 22 زوجًا من الصبغيّات الجسميّة متطابقة عند الذكر والأنثى، وزوج واحد جنسيّ (XX أو XY) هو الذي يحدّد الجنس. والصبغيّات الجسميّة توجد في كلّ الخلايا، وفي كلّ زوج صبغيّ من الأب وآخر من الأمّ.`

**M03w-3 — `exercices/02-tamrin.json` Q1 ↔ `quiz.json` Q4 : doublon de fait aggravé, avec l'indice « ADN » signalé par le correcteur.**
quiz Q4 demande de quoi est fait le chromosome, 02-tamrin Q1 comment s'appelle la longue molécule dont
il est fait : même fait, même clé. La clé raccourcie du quiz (« من جزيء الـ ADN الطويل ») reprend même les
mots de l'énoncé de 02-tamrin. Dans les deux, la clé est la seule option qui contient « ADN ». On
réécrit entièrement 02-tamrin Q1 sur la non-transmission des caractères acquis. Le cours la souligne
(« الصفات المكتسبة لا تنتقل ») et aucune question ne la pose ainsi. Clé gardée en `b`.
- énoncé : `رجل بنى عضلات قويّة بالتمرين طوال سنوات. هل تنتقل هذه العضلات القويّة إلى أبنائه بالوراثة؟`
- `a` : `نعم، لأنّ كلّ صفات الأب تنتقل إلى أبنائه` (40)
- `b` (clé) : `لا، فهي صفة مكتسبة لا تمرّ عبر الأمشاج` (38)
- `c` : `نعم، إذا كانت الأمّ رياضيّة هي أيضًا` (36)
- `d` : `لا، لأنّ الأب لا ينقل إلّا الصبغيّ Y` (36)
- explication : `العضلات المبنيّة بالتمرين صفة مكتسبة من المحيط أثناء الحياة، والوراثة لا تمرّ إلّا عبر الأمشاج، فلا تنتقل إلى الأبناء مهما كانت حال الأمّ. والأب ينقل 23 صبغيًّا في نطفته، لا الصبغيّ Y وحده.`
- pour l'indice « ADN » qui reste dans `quiz` Q4 : `b` `من الماء والأملاح فقط` → `من البروتينات وحدها بلا ADN` (27 ; clé 22). Explication du quiz, ajouter : ` ولا يتكوّن الصبغيّ من البروتينات وحدها، بل أساسه جزيء الـ ADN.`

**M03w-4 — `exercices/05-tadrib.json` Q3 ↔ `quiz.json` Q6 : doublon de fait aggravé.**
Les deux demandent qui détermine le sexe, avec la même clé (le spermatozoïde X ou Y). Les distracteurs
ont convergé : l'ajout « بحسب الغذاء » en `quiz` Q6 `d` répond à « تغذية الأمّ » de 05-tadrib `c`. Le
fait est testé une troisième fois en 06 Q3. On réécrit 05-tadrib Q3 sur la méiose réductionnelle
(« انقسام خاصّ »), qui est au cours et n'est testée nulle part. Clé gardée en `a`.
- énoncé : `كيف يحمل المشيج 23 صبغيًّا فقط بدل 46؟`
- `a` (clé) : `بانقسام خاصّ يُنصّف عدد الصبغيّات` (33)
- `b` : `لأنّه يفقد نصف صبغيّاته عند الإلقاح` (35)
- `c` : `لأنّه يحمل الصبغيّات الجنسيّة وحدها` (35)
- `d` : `لأنّه يتكوّن من نصف خليّة جسميّة` (32)
- explication : `يُنتج كلّ والد أمشاجه بانقسام خاصّ يُنصّف عدد الصبغيّات، فيحمل المشيج 23 صبغيًّا (واحدًا من كلّ زوج). وعند الإلقاح يتّحد مشيجان فيعود العدد 46 في البيضة المخصّبة. فالتّنصيف يسبق الإلقاح ولا يحدث أثناءه، والمشيج يحمل صبغيّات جسميّة وجنسيّة معًا.`

**M03w-5 — `exercices/05-tadrib.json` Q5 ↔ `exercices/04-defi.json` Q2 : même énoncé, doublon de fait.**
Dans les deux, des parents aux yeux bruns ont un enfant aux yeux bleus et l'on demande le génotype des
parents. La clé est la même (B//b pour chacun), les distracteurs aussi (« كلاهما B//B », « أحدهما فقط »).
`03-boss` Q4 pose la même chose en termes de maladie. On réécrit 05-tadrib Q5 sur le `verifie` du cours
(le frère d'أمينة). Clé gardée en `b` ; l'étiquette de `a` reste juste.
- énoncé : `أمينة زرقاء العينين (b//b) وأبواها بنّيّا العينين. أخوها بنّيّ العينين؛ ما تركيبه الوراثيّ الممكن؟`
- `a` : `B//B فقط، لأنّه بنّيّ العينين` (29) — étiquette `bio.gen.dominant-toujours-pur` conservée
- `b` (clé) : `B//B أو B//b، فكلاهما ممكن` (26)
- `c` : `B//b فقط، لأنّ أخته زرقاء العينين` (33)
- `d` : `b//b مثل أخته تمامًا` (20)
- explication : `الأبوان بنّيّا العينين وأنجبا أمينة b//b، فكلّ منهما B//b. ومن أبوين B//b يمكن أن يرث الأخ B من كلّ منهما (B//B) أو B من أحدهما وb من الآخر (B//b)، وكلاهما يعطي عينين بنّيّتين. ولا يمكن أن يكون b//b لأنّه سيكون أزرق العينين.`

### MINOR

- **m03w-1 — `quiz.json` Q3 ↔ `exercices/02-tamrin.json` Q2 (préexistant)** : les deux clés donnent la définition du gène (« مقطع من الـ ADN… »). quiz Q3 pose la question sous l'angle de la différence chromosome / gène, ce qui la rend acceptable. À surveiller.
- **m03w-2 — `exercices/03-boss.json` Q6, `a`** : « بالضبط » ne sert qu'à allonger. C'est inoffensif : l'option n'est pas la clé et la mention n'oriente pas vers elle. On peut la garder.

### Paire laissée par le correcteur — tranchée

- **`03-boss` Q6 (44 + XX) ↔ `07-annales-subur/01-sujet` Q2 (44 + XY) : acceptée.** Les conclusions
  diffèrent (fille / garçon) et le fait a été inversé proprement : la clé reste `b`, l'explication est
  cohérente et aucune option ne parle encore de XY comme d'une clé. Il n'y a pas de doublon de fait.

### Défauts préexistants signalés par le correcteur

- `quiz` Q4 et `02-tamrin` Q1 (la clé est seule à contenir « ADN ») : corrigés par M03w-3.

### Questions relues sans constat

`quiz` Q3, Q6, Q8 · `01-tamrin` Q3, Q4, Q6 · `02-tamrin` Q2 · `03-boss` Q4, Q5, Q6 · `04-defi` Q5 ·
`06-defi-concours` Q3, Q4, Q5, Q6.

**Verdict 03-wiratha : à corriger avant publication.** 0 BLOCKER, 5 MAJOR (doublons de fait, dont 1 créé par
une réécriture du correcteur et 2 aggravés), 2 MINOR. Aucune clé fausse.

---

## Dossier 7 — `04-al-hajiyat-al-ghithaiya`

Relu : 31 questions touchées, leurs options non retouchées, le `cours.md`, et le reste du dossier
pour chercher les doublons. Résolution à l'aveugle : **aucune clé fausse**, mais une clé dit désormais
une chose que l'énoncé ne donne pas. Tous les calculs ont été refaits (370, 600, 270/320, 32 % / 18 %) et
sont justes. Défauts : deux clés raccourcies qui ne répondent plus à tout l'énoncé, un indice de forme créé
par l'étoffement, deux doublons de fait que la correction a rendus identiques.

### MAJOR

**M04h-1 — `quiz.json` Q10, clé `c` : la clé affirme un fait absent de l'énoncé.**
« لا، لأنّ الكمّ يفوق الحاجة رغم جودة التّركيب » pose que la composition est bonne, alors que l'énoncé
n'en dit rien (on ne connaît que les 3000 kcal). L'ancienne clé disait « مهما كان تركيبها ».
- `c` ancien : `لا، لأنّ الكمّ يفوق الحاجة رغم جودة التّركيب` → nouveau : `لا، لأنّ الكمّ يفوق الحاجة مهما كان التّركيب` (44 ; `d` = 44)

**M04h-2 — `exercices/06-defi-concours.json` Q6, clé `b` : la clé ne répond plus à la seconde moitié de l'énoncé.**
L'énoncé demande « أيّهما أعلى قيمة طاقيّة، **وما الدّرس المستفاد؟** », et la leçon a été retirée de la
clé. C'est le cas « الكامل / النوع والعلّة » du mandat. Comme la leçon est dans l'explication, le plus
simple est de raccourcir l'énoncé.
- énoncé : `… أيّهما أعلى قيمة طاقيّة، وما الدّرس المستفاد؟` → `… أيّهما أعلى قيمة طاقيّة؟`

**M04h-3 — `exercices/05-tadrib.json` Q5 : indice de forme créé par l'étoffement.**
L'énoncé annonce « الشّرطان ». Une fois étoffés, `a` (« السخونة والطزاجة … ولذّة الطعم ») et `c` (« الكثرة
والرخص وسهولة الإعداد ») énumèrent trois choses, et la clé est la seule à n'en donner que deux. De plus,
`a` et `c` sont les seules options non vocalisées (« السخونة », « الطزاجة », « الرخص »).
- `a` → `السّخونة والطّزاجة عند التّقديم` (31)
- `c` → `الكثرة والرّخص في السّوق` (24)
- `d` → `اللّحم والخبز معًا في كلّ وجبة يوميّة` (37 ; clé `b` = 34)

**M04h-4 — `exercices/02-tamrin.json` Q6 ↔ `quiz.json` Q9 : doublon de fait que la correction a rendu littéral.**
Les deux questions portent sur les quatre facteurs du besoin énergétique. En retirant « البدنيّ », le
correcteur a rendu les deux clés identiques (« السنّ(،) (و)الجنس(،) (و)النّشاط(،) (و)الحالة الفيزيولوجيّة
»). En étoffant, il a donné au distracteur étiqueté le même texte dans les deux (« السنّ وحده دون غيره من
العوامل »). On réécrit entièrement 02-tamrin Q6 sur le déficit chronique, qui mène à l'amaigrissement
(cours : « والافتقار يؤدّي إلى الهزال ») et qu'aucune question ne pose. Clé gardée en `a`.
- énoncé : `شخص يتناول طوال أشهر أقلّ من حاجته اليوميّة من الطّاقة. ماذا يحدث له؟`
- `a` (clé) : `يُصاب بالهزال لأنّ ما يدخله أقلّ من حاجته` (41)
- `b` : `يُصاب بالسّمنة لأنّ جسمه يخزّن كلّ ما يأكله` (43)
- `c` : `يُصاب بالكُساح لأنّ عظامه تفقد طاقتها` (37)
- `d` : `لا يتأثّر ما دام يشرب ماءً كافيًا كلّ يوم` (41) — retirer l'étiquette `bio.alim.age-seul`
- explication : `الافتقار المستمرّ عن الحاجة يجعل الجسم يستهلك احتياطيّه ثمّ أنسجته، وذلك طريق الهزال. والسّمنة نتيجة الفائض لا النّقص، والكُساح نقص في الكلسيوم والفسفور والفيتامين D لا في الطّاقة، والماء لا قيمة طاقيّة له.`

**M04h-5 — `exercices/01-tamrin.json` Q4 ↔ `quiz.json` Q7 : doublon de fait aggravé.**
Même énoncé (pourquoi les protides figurent dans deux groupes) et même clé (« التّصنيف وظيفيّ / بالوظيفة:
تبني … وتوفّر / وتعطي طاقة »), raccourcie de la même manière dans les deux. Le distracteur étiqueté
`classement-par-origine` est le même (« توجد في الأغذية الحيوانيّة والنباتيّة / في اللّحم والنّبات معًا »).
On réécrit entièrement 01-tamrin Q4 sur les rôles du calcium (tableau du cours : « تكوين العظام والأسنان،
… تخثّر الدّم »), qu'aucune question ne pose. Clé gardée en `b`.
- énoncé : `ما الدّور الذي يؤدّيه الكلسيوم في الجسم؟`
- `a` : `نقل الأكسجين في الكريات الحمراء` (31) — étiquette conseillée `bio.alim.carences-confondues`
- `b` (clé) : `بناء العظام والأسنان وتخثّر الدّم` (33)
- `c` : `إمداد الجسم بطاقة عند الاحتراق` (30) — remplacer l'étiquette `bio.alim.classement-par-origine` par `bio.alim.vitamines-energetiques`
- `d` : `هضم الدّهنيّات في الأمعاء الدّقيقة` (34)
- explication : `الكلسيوم مادّة بناء تدخل في تكوين العظام والأسنان، ويتدخّل أيضًا في نقل السّيالة وفي تخثّر الدّم. أمّا نقل الأكسجين فدور الحديد في الهيموغلوبين، والأملاح المعدنيّة لا تحترق فقيمتها الطّاقيّة صفر، والهضم عمل العصارات الهاضمة.`

### MINOR

- **m04h-1 — `exercices/04-defi.json` Q2, `b` (défaut préexistant signalé)** : « اختلاف الجنس » est éliminé d'avance, puisque les deux personnes sont des femmes. On le remplace par un facteur plausible mais qui n'est pas l'un des quatre du cours. → `b` : `اختلاف كتلة الجسم بين المرأتين` (30 ; clé 34) ; dans l'explication, remplacer `المرأتان من نفس الجنس وقد تكونان` par `كتلة الجسم ليست من العوامل الأربعة، والمرأتان قد تكونان`.
- **m04h-2 — `exercices/04-defi.json` Q6, clé `a`** : sans « نحو », la clé dit « ثلث » et « خمس » pour 32 % et 18 %. Le cours insiste sur « نسب توجيهيّة تقريبيّة ». → `نعم: نحو النّصف والثّلث والخمس على التّوالي` (43 ; `b` 45, `d` 61).
- **m04h-3 — `exercices/06-defi-concours.json` Q5, clé `a`** : « والحديد من الهيموغلوبين » se lit à l'envers (« le fer vient de l'hémoglobine »). → `لأنّ الكلسيوم يبني عظام الجنين والحديد يصنع دمه` (47 ; `b` 56, `c` 47).
- **m04h-4 — `exercices/02-tamrin.json` Q1 (énoncé réécrit)** : « أيّ **مجموعة** من الأغذية » emploie « مجموعة », que le cours réserve aux trois groupes fonctionnels (طاقيّة / بنّاءة / واقية), pour désigner des nutriments. → `أيّ مكوّن غذائيّ يعطي أكبر طاقة لكلّ غرام؟`
- **m04h-5 — `exercices/01-tamrin.json` Q5, clé `b`** : « ببقعة شافّة على الورق » a perdu « لا تختفي بالتّسخين », qui la distingue d'une tache d'eau. L'explication porte ce critère et la clé reste la réponse attendue en 9ᵉ, donc c'est acceptable. Le `a` étoffé (« بماء اليود على الورق ») n'a guère de sens, mais il est inoffensif.
- **m04h-6 — doublon préexistant, fichiers non touchés** : `quiz` Q5 ↔ `02-tamrin` Q3. Mêmes données (100 g de glucides / 20 g de lipides), même question, même clé. À réécrire lors d'un passage de qualité, par exemple en mettant d'autres masses dans 02-tamrin Q3.

### Paires laissées par le correcteur — tranchées

- **`01-tamrin` Q1 (amidon) ↔ `05-tadrib` Q1 (chlorures) : acceptée.** Les faits sont distincts, tirés
  de la même palette de réactifs. Ce sont deux fichiers différents, donc ce n'est pas un miroir au sens
  du mandat. **Attention** : ne pas réécrire `01-tamrin` Q4 sur un autre réactif. La réécriture
  M04h-5 l'évite pour cette raison, puisque Q1 et Q4 deviendraient des miroirs dans le même exercice.
- **`03-boss` Q5 (fer, 10 mg) ↔ `05-tadrib` Q6 (calcium, 0,9 g) : acceptée.** Les ensembles d'options
  sont presque identiques et les clés croisées, mais les faits sont distincts et le cours les oppose
  explicitement (« لماذا تُقاس حاجة الحديد بالمليغرام وحاجة الكلسيوم بالغرام »). La paire est donc voulue.

### Défaut préexistant signalé par le correcteur

- `04-defi` Q2 `b` : corrigé ci-dessus (m04h-1).

### Questions relues sans constat

`quiz` Q7, Q8, Q9 · `01-tamrin` Q2 · `02-tamrin` Q4, Q5 · `03-boss` Q1, Q2, Q3, Q4, Q6 · `04-defi` Q1, Q3, Q4, Q5 ·
`05-tadrib` Q1, Q3 · `06-defi-concours` Q1, Q2, Q3, Q4.

**Verdict 04-al-hajiyat-al-ghithaiya : à corriger avant publication.** 0 BLOCKER, 5 MAJOR (1 clé qui pose
un fait non donné, 1 clé incomplète, 1 indice de forme, 2 doublons aggravés), 6 MINOR. Aucune clé fausse.

---

## Dossier 8 — `04-zalazil`

> Chapitre complémentaire, « خارج البرنامج الرسمي ».

Relu : 33 questions touchées, leurs options non retouchées, le `cours.md`, et le reste du dossier
pour chercher les doublons. Résolution à l'aveugle : **aucune clé fausse**. C'est le dossier le plus
redondant :
- foyer / épicentre : 6 questions ;
- intensité / magnitude : 9 questions ;
- cause des séismes : 4 questions ;
- conduite à tenir : 2 questions.

L'étoffement des distracteurs, fait question par question avec les mêmes formules, a rendu plusieurs
paires presque identiques **entre fichiers**. Une clé raccourcie a aussi perdu sa raison.

### MAJOR

**M04z-1 — `exercices/01-tamrin.json` Q5, clé `b` : le raccourci a supprimé la raison.**
« لأنّها الأقرب إلى البؤرة فتصلها الموجات » : les ondes atteignent aussi toutes les autres régions.
C'est « أقوى » qui expliquait les dégâts, et il a été retiré. On remet le mot et l'on allonge `c` pour
que la clé ne soit pas la plus longue.
- `b` ancien : `لأنّها الأقرب إلى البؤرة فتصلها الموجات` (39) → nouveau : `لأنّها الأقرب إلى البؤرة فتصلها الموجات أقوى` (44)
- `c` ancien : `لأنّ المرصاد الزلزالي موجود فيها دائمًا` → nouveau : `لأنّ المرصاد الزلزالي يوضع فيها دائمًا قرب المباني` (50 ; `a` = 43)

**M04z-2 — `exercices/06-defi-concours.json` Q1 ↔ `quiz.json` Q2 : doublon de fait, l'inverse est devenu identique.**
L'énoncé est le même (« ما الفرق بين (بؤرة الزلزال) والمركز السطحي ») et la clé aussi. Après
étoffement, le distracteur inversé est le même texte dans les deux : « البؤرة على سطح الأرض(،/;)
المركز السطحيّ في العمق تحتها ». On réécrit entièrement 06 Q1 sur le cycle sismique, qui est au cours et
n'est testé nulle part. Clé gardée en `a`.
- énoncé : `بعد زلزال قويّ على فالق نشط، يتوقّع الجيولوجيّون زلزالًا آخر على الفالق نفسه بعد سنوات أو عقود. لماذا؟`
- `a` (clé) : `لأنّ الصفيحتين تتحرّكان فتتراكم الإجهادات من جديد` (49)
- `b` : `لأنّ الزلزال الأوّل صنع طاقة جديدة في صخور الفالق` (49)
- `c` : `لأنّ مياه الأمطار تملأ الفالق كلّ شتاء فينزلق` (45)
- `d` : `لأنّ دوران الأرض حول الشمس يعيد الزلزال كلّ سنة` (47)
- retirer les étiquettes `bio.geo.foyer-epicentre` de `b` et `c`
- explication : `الصفيحتان لا تتوقّفان عن الحركة بعد الزلزال، فتعود الإجهادات إلى التراكم على الفالق نفسه الذي صار أضعف من محيطه، حتّى تتجاوز مقاومة الصخور من جديد: هذه هي الدورة الزلزالية. والزلزال لا يصنع الطاقة بل يحرّرها، والأمطار ودوران الأرض لا يسبّبان الزلازل التكتونية.`

**M04z-3 — `exercices/05-tadrib.json` Q3 ↔ `quiz.json` Q6 : doublon de fait aggravé.**
L'énoncé est le même (« ما الفرق بين شدّة الزلزال ومقداره »), la clé aussi, et après étoffement les deux
distracteurs inversés disent la même chose (« الشدّة تقاس بسلّم ريشتر … والمقدار بـميركالّي »). On
réécrit entièrement 05-tadrib Q3 sur la propagation des ondes S, que le cours énonce et qu'aucune
question ne teste. Clé gardée en `a`.
- énoncé : `أيّ الموجات الزلزاليّة لا تنتشر إلّا في الأوساط الصّلبة؟`
- `a` (clé) : `الموجات الثانوية (S)` (20) · `b` : `الموجات الأوّلية (P)` (20) · `c` : `الموجات السطحية` (15) · `d` : `كلّ الموجات الزلزالية دون استثناء` (33)
- retirer les étiquettes `bio.geo.intensite-magnitude` de `b`, `c` et `d`
- explication : `الموجات الثانوية (S) أبطأ من الأوّلية ولا تنتشر إلّا في الأوساط الصّلبة، أمّا الموجات الأوّلية (P) فهي الأسرع وتنتشر في أوساط أخرى أيضًا. والموجات السطحية تنتشر قرب السطح وهي الأكثر تدميرًا.`

**M04z-4 — `exercices/05-tadrib.json` Q5 ↔ `exercices/03-boss.json` Q6 : même énoncé, doublon de fait que la correction n'a pas vu.**
Dans les deux, deux séismes de même magnitude causent des dégâts inégaux, et l'on demande « ما التفسير
الأرجح؟ ». La clé est la même (profondeur, urbanisation, sol, construction). On réécrit 05-tadrib Q5 sur
l'alerte précoce : le cours précise que « النظام لا يتنبّأ بالزلزال: هو يسابق موجاته ». Clé gardée en `b`.
- énoncé : `كيف يعمل نظام الإنذار المبكّر بالزلازل؟`
- `a` : `يتنبّأ بالزلزال قبل وقوعه بأيّام` (32) — retirer l'étiquette `bio.geo.intensite-magnitude`
- `b` (clé) : `يلتقط الموجة P فيسبق الموجات المدمّرة` (37)
- `c` : `يمنع الموجات السطحية من بلوغ المدن` (34)
- `d` : `يقيس شدّة الزلزال بعد انتهاء كلّ الأضرار` (40)
- explication : `تلتقط المراصد القريبة الموجة P، وهي الأسرع والأقلّ تدميرًا، وترسل الإشارة بسرعة الضوء، فتصل قبل الموجات المدمّرة بثوانٍ تكفي لإيقاف القطارات وقطع الغاز. فالنظام لا يتنبّأ بالزلزال بل يسابق موجاته بعد وقوعه، ولا يمنع انتشارها.`

**M04z-5 — `exercices/05-tadrib.json` Q4 ↔ `quiz.json` Q7 : doublon de fait aggravé.**
La question est la même (la cause principale des séismes), la clé aussi, et les distracteurs, après
étoffement, sont des paraphrases l'un de l'autre (pluies / « دوران الأرض حول الشمس … كلّ عام / طوال
السنة كلّها » / chaleur). On réécrit 05-tadrib Q4 sur la profondeur du foyer (cours : « المسافة بينهما
هي عمق البؤرة، ويُقاس عموديًّا لا مائلًا »). Clé gardée en `a`.
- énoncé : `ماذا يُسمّى «عمق البؤرة»؟`
- `a` (clé) : `المسافة العموديّة بين البؤرة والمركز السطحيّ` (44)
- `b` : `المسافة بين المركز السطحيّ وأقرب مرصاد` (38)
- `c` : `طول الفالق الذي انكسرت عليه الصخور` (34)
- `d` : `المسافة المائلة بين البؤرة وأقرب مدينة مأهولة` (45)
- explication : `عمق البؤرة هو المسافة بين البؤرة والمركز السطحيّ، ويُقاس عموديًّا لا مائلًا لأنّ المركز السطحيّ على الشاقول فوق البؤرة تمامًا. أمّا المسافة إلى المرصاد فتُحسب من فرق وصول الموجات P وS، والفالق سطح الكسر لا مسافة.`

**M04z-6 — `exercices/05-tadrib.json` Q6 ↔ `exercices/04-defi.json` Q4 : doublon de fait aggravé.**
Les deux portent sur la conduite à tenir en classe ou dans un bâtiment. Les clés sont devenues presque
identiques (« الاحتماء تحت طاولة متينة بعيدًا عن / والابتعاد عن النوافذ »), et les distracteurs aussi
(fenêtres, ascenseur, course). On réécrit 05-tadrib Q6 sur l'origine de l'énergie libérée (cours : « الطاقة
لم تُصنع وقت الزلزال: كانت موجودة »). Clé gardée en `a`.
- énoncé : `متى تكوّنت الطاقة التي يحرّرها الزلزال؟`
- `a` (clé) : `تراكمت في الصخور سنوات طويلة قبله` (33)
- `b` : `صُنعت لحظة وقوع الزلزال نفسه` (28)
- `c` : `جاءت من حرارة الشمس في ذلك اليوم` (32)
- `d` : `نتجت عن الموجات الزلزالية بعد انتشارها` (38)
- explication : `الصخور في العمق تتعرّض لضغوط تتراكم عليها سنوات طويلة فتخزّن الطاقة كنابض مضغوط، ثمّ تنكسر فجأة فتتحرّر هذه الطاقة دفعةً واحدة. فالطاقة لم تُصنع وقت الزلزال، والموجات نتيجة لتحرّرها لا مصدر لها، وحرارة الشمس لا علاقة لها بذلك.`

**M04z-7 — `exercices/04-defi.json` Q3 ↔ `quiz.json` Q8 : doublon de fait aggravé.**
Les deux portent sur la mesure de construction qui réduit les dégâts : « بناء مقاوم للزلازل واحترام معايير
البناء » / « بناء مبانٍ مقاومة للزلازل وفق معايير خاصّة ». En remplaçant « تشييد » par « بناء », le
correcteur a calqué la clé sur celle du quiz. Le distracteur « البناء … عند / فوق الفوالق النشطة » est
présent dans les deux. On réécrit 04-defi Q3 sur les cartes de risque sismique (cours). Clé gardée en `a`.
- énoncé : `لماذا تُرسم خرائط للمخاطر الزلزاليّة؟`
- `a` (clé) : `لتجنّب البناء عند الفوالق النشطة` (32)
- `b` : `لمنع الزلازل من الوقوع في المدن` (31)
- `c` : `لرفع مقدار الزلازل المسجّلة فيها` (32)
- `d` : `لتحديد ساعة وقوع الزلزال القادم` (31)
- explication : `خرائط المخاطر تبيّن المناطق المعرّضة للزلازل والفوالق النشطة، فتسمح بتجنّب البناء عندها وبتخطيط العمران. لكنّها لا تمنع الزلازل ولا تغيّر مقدارها، ولا تحدّد موعد الزلزال القادم: لا أحد يستطيع التنبّؤ بساعة وقوعه.`

### MINOR

- **m04z-1 — `exercices/05-tadrib.json` Q1 (énoncé inversé par le correcteur) ↔ `exercices/01-tamrin.json` Q2** : passer de « terme → définition » à « définition → terme » garde le même fait (la définition du foyer). Le procédé est légitime, mais ce fait est déjà testé six fois. La paire peut rester si M04z-2 est appliqué, puisque celui-ci supprime un des six.
- **m04z-2 — recoupements préexistants à surveiller** : `02-tamrin` Q6 ↔ `04-defi` Q5 (magnitude unique, intensités multiples) ; `03-boss` Q2 ↔ `06-defi-concours` Q5 (séismes aux frontières des plaques) ; `quiz` Q1 ↔ `01-tamrin` Q1 (énergie libérée).
- **m04z-3 — `exercices/01-tamrin.json` Q1, `c`** : la cheville « دائمًا » (« سقوط النيازك على سطح الأرض دائمًا ») est vide de sens. → `سقوط النيازك الكبيرة على سطح الأرض` (34 ; clé 33, `b` 35).

### Questions relues sans constat

`quiz` Q1, Q6, Q7 · `01-tamrin` Q1, Q2, Q3, Q6 · `02-tamrin` Q2, Q3, Q4, Q5, Q6 · `03-boss` Q1, Q3, Q4, Q5, Q6 ·
`04-defi` Q2, Q4, Q5, Q6 · `05-tadrib` Q1, Q2 · `06-defi-concours` Q5, Q6.

**Verdict 04-zalazil : à corriger avant publication.** 0 BLOCKER, 7 MAJOR (1 clé amputée de sa raison,
6 doublons de fait, dont 5 aggravés par l'étoffement), 3 MINOR. Aucune clé fausse.

---

## Synthèse

| Dossier | BLOCKER | MAJOR | MINOR | Clés fausses | Verdict |
| ------- | ------- | ----- | ----- | ------------ | ------- |
| 01-takathur-insan | 0 | 8 | 6 | 0 | à corriger |
| 01-wadhifat-al-ittisal | 0 | 3 | 5 | 0 | à corriger |
| 02-al-af3al-al-in3ikasiya | 0 | 5 | 5 | 0 | à corriger |
| 02-manaa | 0 | 5 | 5 | 0 | à corriger |
| 03-al-ibsar | 0 | 3 (4 questions) | 3 | 0 | à corriger |
| 03-wiratha | 0 | 5 | 2 | 0 | à corriger |
| 04-al-hajiyat-al-ghithaiya | 0 | 5 | 6 | 0 | à corriger |
| 04-zalazil | 0 | 7 | 3 | 0 | à corriger |

**Aucune clé fausse ni ambiguë** sur les 243 questions touchées, et la fuite inverse n'est pas
exploitable (2–15 %). Le défaut dominant est le **doublon de fait** : 32 réécritures complètes sont
proposées, toujours sur un fait du `cours.md` que rien ne testait, avec la clé au même identifiant. Il a
trois causes, qui valent pour la méthode :

1. **L'étoffement en série fait converger les paires d'un fichier à l'autre.** Le `quiz` et les
   exercices posent souvent la même question. En étoffant chaque distracteur avec les mêmes formules
   (« … وحده دون غيره من العوامل », « … بعد المرض », « … على سطح الأرض … تحتها »), le correcteur a rendu
   identiques des options qui ne l'étaient pas. `content:tranche` n'a vu aucune de ces paires.
2. **Les réécritures de doublon ont créé d'autres doublons** : 03-al-ibsar `01-tamrin` Q1/Q2 (trois
   questions qui ont la rétine pour clé dans le même exercice), 03-al-ibsar `03-boss` Q6, 03-wiratha
   `05-tadrib` Q1. Changer l'énoncé sans changer les options ni le fait laisse le doublon entier :
   01-takathur `02-tamrin` Q3, 04-zalazil `05-tadrib` Q1. **Une réécriture doit viser un fait du cours
   qu'aucune question du dossier ne teste**, et il faut le vérifier en listant tout le dossier.
3. **Des doublons préexistants n'ont pas été vus**, dont des énoncés identiques mot pour mot :
   03-wiratha `03-boss` Q5 / `05-tadrib` Q6, 03-al-ibsar `quiz` Q5 / `02-tamrin` Q2, 04-zalazil
   `03-boss` Q6 / `05-tadrib` Q5.

**Autres défauts relevés, par gravité (tous MAJOR, aucun BLOCKER)** :
- **Clé raccourcie devenue inexacte ou incomplète** : 01-takathur `03-boss` Q5 (« حملها نحو البويضة ») ;
  04-hajiyat `quiz` Q10 (« رغم جودة التّركيب », un fait non donné) ; 04-hajiyat `06` Q6 (la « leçon »
  demandée a disparu) ; 04-zalazil `01-tamrin` Q5 (« أقوى » retiré).
- **Clé tautologique** : 01-takathur `04-defi` Q3 ; 02-af3al `03-boss` Q1, qui est de plus la seule option
  entre guillemets.
- **Indices de forme** : 04-hajiyat `05-tadrib` Q5 (seule option à deux termes pour « الشّرطان ») ;
  01-wadhifat `01-tamrin` Q3 (seule option avec tanwīn) ; 01-takathur `quiz` Q7 (des gloses qui éliminent
  les distracteurs).
- **Notion absente du cours** : 02-af3al `06` Q4 (le cerveau qui freine le réflexe ; ajout au cours
  proposé).

**Défauts préexistants signalés par le correcteur** : la correction de chacun est donnée (01-wadhifat
`quiz` Q5 d ; 01-takathur `04-defi` Q2 ; 03-wiratha `quiz` Q4 et `02-tamrin` Q1 ; 04-hajiyat `04-defi`
Q2). **Paires laissées par le correcteur** : toutes **acceptées** (01-takathur `04-defi` Q1 ↔ `06` Q2 ;
03-al-ibsar `quiz` Q7 ↔ `03-boss` Q1 ; 04-hajiyat `01-tamrin` Q1 ↔ `05-tadrib` Q1 et `03-boss` Q5 ↔
`05-tadrib` Q6 ; 03-wiratha `03-boss` Q6 passé en 44 + XX).

Point ouvert, hors mandat : la position de la clé (b ≈ 50 %, d ≈ 2–5 %) reste à traiter.
