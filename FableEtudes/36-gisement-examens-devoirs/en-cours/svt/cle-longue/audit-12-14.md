# Audit indépendant — correction « clé la plus longue », SVT 9ᵉ, chapitres 12 · 13 · 14

> Mandat : `.claude/skills/content-engine/references/audit-correction.md`, appliqué à la lettre.
> Corpus relu : `/home/user/wt-svtkey` (branche `wip/svt-9eme-cle-longue`), diff
> `git diff origin/main -- content/sciences-vie-terre/<CHAPITRE>` après `fetch origin main`.
> Référence : `cours.md` de chaque chapitre + manuel 105905 (cache). Hors périmètre :
> `12-…/exercices/07…10-examen-*`. L'auditeur n'a modifié aucun fichier du corpus.
> Indices de questions : 1-based. Longueurs en caractères (Python `len`) ; toutes les
> corrections proposées ont été vérifiées : la clé n'y redevient pas strictement la plus longue.

## Chapitre 12 — `12-takawwun-al-janin`

Résolution à l'aveugle : **aucune clé fausse, aucune clé ambiguë** sur les 37 questions modifiées.
Défauts : clés raccourcies qui ne répondent plus à tout l'énoncé, un distracteur devenu
quasi-vrai, des distracteurs que l'énoncé élimine, deux fautes de langue.

### BLOCKER

**B12-1 — `exercices/04-defi.json` Q5 — faute de langue dans l'énoncé** (non retouché, question touchée).
« يُصاب فقر الدّم الأمّ » est agrammatical : le verbe est au passif et prend deux sujets.
- ancien : `لماذا يُصاب فقر الدّم الأمّ أكثر من مولودها في حالات تقارب الولادات؟`
- nouveau : `لماذا يُصيب فقرُ الدّم الأمَّ أكثر من مولودها في حالات تقارب الولادات؟`

### MAJOR

**M12-1 — `exercices/06-defi-concours.json` Q1, clé `b` — le raccourci rend le sens faux.**
« المنع يخصّ الأغلب لا الكلّ في زمن تكوّن الأعضاء » laisse croire que le filtre est partiel
*seulement* pendant l'organogenèse. Les deux facteurs (filtre relatif / période sensible) doivent rester
coordonnés.
- `b` ancien : `أنّ المنع يخصّ الأغلب لا الكلّ في زمن تكوّن الأعضاء`
- `b` nouveau : `أنّ المنع نسبيّ، والشّهر الثّاني زمن تكوّن الأعضاء` (50 ; `a` = 52)

**M12-2 — `exercices/06-defi-concours.json` Q3, clé `b` — la clé ne répond plus à l'énoncé.**
L'énoncé met en avant la chatte (« امرأة تربّي قطّة ») ; la clé raccourcie a gardé « طبخ اللّحم »
et perdu la seule mesure qui concerne l'animal.
- `b` ancien : `اختبار قبل الحمل وطبخ اللّحم، لأنّ الطّفيل يعبر المشيمة`
- `b` nouveau : `اختبار قبل الحمل وتجنّب القطط، لأنّ الطّفيل يعبر المشيمة` (56 ; `c` = 60)

**M12-3 — `exercices/06-defi-concours.json` Q6, distracteur `b` — il est devenu quasi juste.**
L'ajout « ولا النّساء الحوامل » rapproche l'option d'un fait réel : on ne vaccine pas pendant la
grossesse. Un élève informé peut la défendre. On remet à la place une erreur franche, contredite par le
cours (la femme en âge de procréer est vaccinée).
- `b` ancien : `لأنّ اللّقاح لا ينفع الكبار ولا النّساء الحوامل`
- `b` nouveau : `لأنّ اللّقاح لا ينفع إلّا الأطفال دون سنّ الخامسة` (49 ; clé `a` = 43)

**M12-4 — `quiz.json` Q8, clé `b` — la clé ne répond plus à « خاصّة عندما تتقارب الولادات ».**
La clé « يأخذ حديده من جسم أمّه » vaut pour toute grossesse ; seule l'explication parle de l'absence de
reconstitution du stock. Pour que la clé ne devienne pas la plus longue, on allonge aussi `a`.
- `b` ancien : `لأنّ الجنين يأخذ حديده من جسم أمّه`
- `b` nouveau : `لأنّ الجنين يأخذ من مخزون أمّ لم يُعوَّض بعد` (44)
- `a` ancien : `لأنّ الجنين يمنع امتصاص الحديد في معي أمّه`
- `a` nouveau : `لأنّ الجنين يمنع امتصاص الحديد في معي أمّه طوال الحمل` (53)

**M12-5 — `exercices/04-defi.json` Q3 — indice de forme : seule la clé donne un nombre.**
L'énoncé demande « وما الحدّ المذكور ». Seule `a` cite un seuil chiffré (« 3 مغ ») ; `b` et `d` disent
« حدّه اليوميّ ». De plus, `c` (« إفراط في الأكل ») n'est pas un *نقص* et l'énoncé l'élimine. Les deux
remplacements ci-dessous donnent des seuils chiffrés : un piège sur le nutriment (le manque de vitamine C
donne aussi de la fatigue selon le cours) et un piège sur le seuil.
- `b` ancien : `نقص فيتامين D، إذا نزل عن حدّه اليوميّ`
- `b` nouveau : `نقص فيتامين C، إذا نزل عن 3 مغ في اليوم` (39)
- `c` ancien : `إفراط في الأكل، إذا زاد عن حاجة الجسم`
- `c` nouveau : `نقص الحديد، إذا نزل عن 30 مغ في اليوم` (37)
- Explication, ajouter à la fin : ` والحدّ المذكور في الدّرس 3 مغ لا 30، وفيتامين C يسبّب نقصه الإرهاق لكن لا ضمور مخاطيّة اللّسان.`

**M12-6 — `exercices/04-defi.json` Q2, distracteur `d` — l'énoncé le contredit.**
L'énoncé précise que les deux chiffres concernent « عمر البويضة ». L'ajout « هما البويضة والحيوان
المنويّ معًا » rend `d` éliminable d'un coup d'œil.
- `d` ancien : `الرّقمان يخصّان مشيجين مختلفين، هما البويضة والحيوان المنويّ معًا`
- `d` nouveau : `الرّقم الأوّل لعمرها في المبيض، والثّاني لعمرها في القناة` (57 ; clé `b` = 64)

**M12-7 — `exercices/04-defi.json` Q4 — l'explication ne justifie plus la clé.**
La clé a perdu « في التّغذية يضرّ النّقص والإفراط معًا ». L'explication ne dit nulle part que l'excès
de vitamine D cause des malformations, et elle ne réfute pas `c` ni `d` (des signes de manque de fer).
- explication nouvelle : `الإفراط في فيتامين D يسبّب تشوّهات عند الجنين: في التّغذية يضرّ النّقص والإفراط معًا، كما في الطّاقة. أمّا الشّحوب وضمور مخاطيّة اللّسان فعلامات فقر الدّم الحديديّ، لا علاقة لها بفيتامين D.`

### MINOR

**m12-1 — `exercices/01-tamrin.json` Q2, clé `b`** : « المنويّ » est employé seul comme nom, ce qui
est fautif. En corrigeant, on allonge aussi `a` pour que la clé ne devienne pas la plus longue.
- `b` → `في الثّلث العلويّ للقناة، لأنّ البويضة بطيئة والحيوان المنويّ سريع` (66)
- `a` → `في الرّحم، لأنّه أوسع تجويف تتجمّع فيه كلّ الحيوانات المنويّة بعد القذف` (71)

**m12-2 — `exercices/06-defi-concours.json` Q6, clé `a`** : accord. « الحميراء » est un nom féminin.
- `a` ancien : `لأنّه بلا علاج وأخطر آثاره في الأشهر الأولى` → nouveau : `لأنّها بلا علاج وأخطر آثارها في الأشهر الأولى` (45 ; `b` = 47 ou 49 après M12-3)

**m12-3 — `exercices/05-tadrib.json` Q4, clé `a`** : `اعتام` → `إعتام` (nom verbal de la forme IV, avec
hamza). La même graphie apparaît dans `cours.md` (tableau de la rubéole), à corriger aussi.

**m12-4 — `exercices/01-tamrin.json` Q4 — l'explication ne réfute pas `c`** (la pénétration passe avant
l'entourage). Ajouter : ` والإحاطة تسبق الدّخول: الحيوانات المنويّة تحيط بالبويضة قبل أن يخترقها واحد.`

**m12-5 — distracteurs que l'énoncé élimine, présents avant la correction et laissés tels quels** :
- `04-defi` Q4 `a` (« لا يضرّ » alors que l'énoncé demande « لماذا يضرّ ») ;
- `05-tadrib` Q4 `c` (« لا مخاطر » alors que l'énoncé dit « من مخاطر ») ;
- `04-defi` Q6 `a`/`d` (cause bactérienne ou virale pour un mal qui porte le nom de l'alcool).

À reprendre lors d'un passage de qualité, sans urgence.

**m12-6 — paire proche entre deux fichiers** : `quiz.json` Q8 ↔ `exercices/04-defi.json` Q5. C'est le même
fait (le fer de la mère, les naissances rapprochées) et les clés sont voisines. Les fichiers sont
distincts, donc pas de doublon au sens du mandat, mais à surveiller.

### Questions relues sans constat (ch. 12)

`01-tamrin` Q1, Q5, Q6 · `02-tamrin` Q2, Q3, Q4, Q6 · `03-boss` Q1, Q2, Q3, Q5 · `04-defi` Q1 ·
`05-tadrib` Q1, Q2, Q3, Q5, Q6 · `06-defi-concours` Q2, Q4, Q5 · `quiz` Q2, Q5, Q6, Q7, Q10.

**Verdict ch. 12 : à corriger avant publication.** 1 BLOCKER de langue, 7 MAJOR. Aucune clé fausse.

## Chapitre 13 — `13-tandhim-al-wiladat`

Résolution à l'aveugle : **aucune clé fausse** sur les 37 questions modifiées. Un chiffre officiel a été
altéré dans une clé. Un distracteur est rendu défendable par sa justification. Deux distracteurs sont
contredits par l'énoncé. Une paire proche est à trancher.

### MAJOR

**M13-1 — `exercices/02-tamrin.json` Q4, clé `a` — chiffre du manuel altéré** (point signalé par le correcteur, tranché).
Le manuel 105905 et le cours disent « **أكثر من 99 %** » pour les pilules combinées et « **99 %** »
pour le stérilet. La clé « نحو 99 % » efface cette distinction, et l'explication (« أكثر من 99 % ») ne
cite plus le texte de la clé. Remettre « أكثر من » seulement dans la clé la rendrait la plus longue, et
« أكثر من 70 % » serait juste lui aussi. On réécrit donc les quatre options (le chiffre réel de chaque
autre méthode du cours sert de piège).
- `a` (clé) : `نحو 99 %` → `أكثر من 99 %` (12)
- `b` : `نحو 70 %` → `بين 85 % و98 %` (14 ; le préservatif)
- `c` : `نحو 50 %` → `نحو 70 %` (8 ; méthodes naturelles, échec jusqu'à 30 %)
- `d` : `نحو 85 %` → `أقلّ من 50 %` (12)
- explication nouvelle : `أكثر من 99 % إذا التزمت المرأة بقواعد استعمالها، فوق الآلة الرّحميّة (99 %). والمجال من 85 % إلى 98 % يخصّ الواقي الذّكريّ، والفارق فيه يأتي من الاستعمال غير السّليم أو غير المطلق ومن الانزلاق والتّقطّع. و70 % تقريبًا هو ما يبقى للطّرق الطّبيعيّة التي تصل نسبة إخفاقها إلى 30 %.`

**M13-2 — `exercices/04-defi.json` Q1, distracteur `c` — sa justification le rend défendable.**
« الامتناع الدّوريّ، لأنّه لا يستعمل أيّ هرمون » : c'est vrai, et c'est bien le critère de l'énoncé
(« لا تؤثّر على حليبها »). Un élève peut la défendre contre la clé. On lui donne une justification que
le cours dément (30 % d'échec).
- `c` ancien : `الامتناع الدّوريّ، لأنّه لا يستعمل أيّ هرمون`
- `c` nouveau : `الامتناع الدّوريّ، لأنّ نسبة إخفاقه لا تتجاوز 1 %` (49 ; clé `b` = 50)
- Explication : la dernière phrase reste valable. Ajouter : ` ونسبة إخفاقه تصل إلى 30 %.`

**M13-3 — `exercices/02-tamrin.json` Q3, distracteur `b` — l'énoncé le contredit.**
L'énoncé demande « المفعول الثّلاثيّ » ; `b` (« منع الإباضة وحدها · دون أيّ أثر… ») annonce un
effet unique et s'élimine d'un coup d'œil. On le remplace par la confusion plausible avec la pilule
combinée.
- `b` ancien : `منع الإباضة وحدها · دون أيّ أثر في عنق الرّحم · أو في بطانة الرّحم`
- `b` nouveau : `منع الإباضة كلّيًّا · رفع تركيز هرمونين · إلغاء التّغيّر الدّوريّ` (65 ; `c` = 78)
- Explication, ajouter : ` ورفعُ تركيز هرمونين لمنع الإباضة وحدها هو مفعول الأقراص المركّبة لا أحاديّة الهرمون.`

**M13-4 — paire proche `quiz.json` Q3 ↔ `exercices/03-boss.json` Q1** (signalée par le correcteur, tranchée : **à réécrire**).
Même énoncé (cycle de 26 jours, jour d'ovulation), mêmes quatre options (12/13/14/26), même clé. C'est
un doublon de fait. Le boss (difficulté 3) est réécrit en un calcul à deux étapes ; la clé reste à
l'identifiant `b`.
- `03-boss` Q1, nouvel énoncé : `امرأة معدّل طول دورتها 30 يومًا وتعتمد الامتناع الدّوريّ. ما أوّل يوم في فترة خصوبتها؟`
- `a` : `اليوم 10` (garder `misconceptionTag: bio.cycle.ovulation-au-milieu-du-cycle` : 30 ÷ 2 = 15, − 5)
- `b` (clé) : `اليوم 11`
- `c` : `اليوم 13` (16 − 3 : borne minimale de survie des spermatozoïdes au lieu de la maximale)
- `d` : `اليوم 16` (le jour d'ovulation pris pour le début de la fenêtre)
- `correctOption` : `b` (inchangé)
- explication : `الإباضة: 30 − 14 = اليوم 16. وبداية فترة الخصوبة تُحسب بالمدّة القصوى لعيش الحيوانات المنويّة داخل المسالك الأنثويّة: 16 − 5 = اليوم 11. وقسمة الطّول على اثنين تعطي 15 ثمّ 10 — خطأ بيوم ؛ وطرح 3 بدل 5 يضيّق النّافذة ويُدخل أيّامًا خطرة في «فترة الأمان» ؛ واليوم 16 هو الإباضة نفسها لا بداية الفترة.`
- Vérifié : 30 − 14 = 16 ; 16 − 5 = 11 ; une seule option juste. Pas de collision avec `06-defi-concours` Q1 (cycle de 25 à 31 jours, question qualitative).

### MINOR

**m13-1 — `exercices/01-tamrin.json` Q5, clé `b`** : « وتدوم 10 سنوات » a perdu « حتّى ». Le cours dit
« jusqu'à 10 ans » (pour le DIU au cuivre), et l'explication dit encore « حتّى 10 سنوات ».
- `b` → `يضعها الطّبيب، وتدوم حتّى 10 سنوات` (34)
- `a` → `تضعها المرأة بنفسها، وتدوم سنة واحدة` (36, pour que la clé ne devienne pas la plus longue)

**m13-2 — `exercices/04-defi.json` Q3, clé `b`** : même perte de « حتّى ».
- `b` → `الآلة الرّحميّة النّحاسيّة: صلوحيّة حتّى 10 سنوات وعودة الإنجاب` (63)
- `c` → `ربط قناتَي البيض: نجاعة عالية وعودة الإنجاب بعد فكّ الرّبط مباشرة` (65)

**m13-3 — `exercices/03-boss.json` Q6, clé `a`** : « تقتل المنويّة » emploie l'adjectif comme nom, ce qui
est fautif.
- `a` → `تمنع الانغراس وتغيّر الإفرازات وتقتل الحيوانات المنويّة؛ ولا تمسّ المبيض` (72)
- `b` → `تمنع الإباضة وتوقف الدّورة الجنسيّة؛ ولا تؤثّر في بطانة الرّحم ولا في عنقه` (74)

**m13-4 — distracteurs que l'énoncé élimine, présents avant la correction** :
- `04-defi` Q4 `d` (le préservatif « plus efficace que la pilule », alors que l'énoncé donne les chiffres) ;
- `05-tadrib` Q3 `d` (« لا ترتفع » alors que l'énoncé dit « ارتفاع الحرارة ») ;
- `06-defi-concours` Q1 `d` (« تصلح للجميع », qui n'est pas une raison de difficulté) ;
- `06-defi-concours` Q6 `b`/`c`/`d` (trois absurdités).

Sans urgence.

**m13-5 — paire proche entre deux fichiers** : `05-tadrib` Q6 ↔ `06-defi-concours` Q6 (« لا وسيلة أفضل » /
« اختيار النّوع المناسب » : même idée, clés voisines). À surveiller.

### Questions relues sans constat (ch. 13)

`01-tamrin` Q1, Q2, Q6 · `02-tamrin` Q1, Q2, Q5 · `03-boss` Q2, Q3, Q4, Q5 · `04-defi` Q2, Q5, Q6 ·
`05-tadrib` Q1, Q2, Q4, Q5 · `06-defi-concours` Q2, Q3, Q4, Q5 · `quiz` Q5, Q6, Q7, Q9, Q10.

**Verdict ch. 13 : à corriger avant publication.** 0 BLOCKER, 4 MAJOR (dont la réécriture d'un doublon).
Aucune clé fausse.

## Chapitre 14 — `14-al-amrad-al-manqula`

Résolution à l'aveugle : **aucune clé fausse** sur les 40 questions modifiées. En revanche, le
raccourcissement a créé un indice de polarité, une explication qui cite un texte disparu, une clé
devenue mot pour mot celle d'une autre question, et deux distracteurs que l'énoncé contredit.

### MAJOR

**M14-1 — `exercices/04-defi.json` Q1 — indice de forme créé par la correction** (point signalé, tranché).
L'énoncé demande « هل يطمئنّ؟ ». La clé `b` est maintenant **le seul « لا »** face à trois « نعم ».
Avant la correction, `c` commençait aussi par « لا » ; en la réécrivant, le correcteur l'a fait passer
à « نعم ». Il faut rétablir deux « لا » contre deux « نعم ». Le nouveau `c` a le bon verdict et une
raison que le cours dément.
- `c` ancien : `نعم: يصبح المصاب إيجابيّ المصل بعد أسبوع واحد فقط من الخطر`
- `c` nouveau : `لا: عليه أن ينتظر ظهور الأعراض ليتأكّد من سلامته` (48 ; clé `b` = 60, `d` = 62)
- Explication, ajouter : ` وانتظار الأعراض لا يفيد: المرحلة الأولى قد تدوم سنوات بلا عرض، والفيصل اختبار يُعاد بعد انقضاء النّافذة.`

**M14-2 — `exercices/06-defi-concours.json` Q1 — l'explication cite un texte disparu.**
« والنّسبتان تجعلانها أرجح الاحتمالات » renvoie aux deux pourcentages (3/4 et 70 %), qui ne figurent
plus nulle part. Ils ont été retirés de la clé sans être reportés dans l'explication.
- explication nouvelle : `غيابُ الأعراض هو بالذّات ما يوجّه نحو الكلاميديا لا ما يبعد عنها: فهي صامتة عند ثلاثة أرباع المصابات، وتقف وراء نحو 70 % من حالات العقم الأنبوبيّ — فهي أرجح الاحتمالات. والزّهري في طوره الثّالث يترك آثارًا أخرى في الجسم كلّه، والسّيدا يضرب المناعة لا قناتَي البيض.`

**M14-3 — `exercices/02-tamrin.json` Q2 — deux distracteurs que l'énoncé contredit, et une clé identique à celle d'une autre question.**
L'énoncé pose « رغم أنّها قابلة للعلاج ». `b` (« لا تُعالَج ولا تُشفى ») et `c` (« ولا علاج تامًّا
لها ») contredisent cette prémisse : il ne reste qu'un choix entre deux options. De plus, la clé
(« تتطوّر في صمت بلا أعراض عند أغلب المصابين ») est maintenant **mot pour mot** celle de `quiz.json` Q2,
dont l'énoncé est le même. C'est un doublon de fait, créé par la correction. On réécrit la question
entière ; la clé reste à l'identifiant `a`.
- nouvel énoncé : `في مائة امرأة مصابة بالكلاميديا، كم واحدة تقريبًا لا تظهر عليها أيّ أعراض؟`
- `a` (clé) : `نحو 75` · `b` : `نحو 50` (la proportion chez les hommes) · `c` : `نحو 25` (le complément) · `d` : `نحو 70` (confusion avec les 70 % d'infertilité tubaire)
- `correctOption` : `a` (inchangé)
- explication : `ثلاثة أرباع المصابات، أي 75 من كلّ 100، لا تظهر عليهنّ أيّ أعراض. والنّصف تقريبًا نسبةُ الرّجال المصابين بلا أعراض، و70 % نسبةُ حالات العقم الأنبوبيّ التي تتسبّب فيها الكلاميديا. وهذا الصّمت هو ما يجعلها الأخطر رغم أنّها قابلة للعلاج.`
- Vérifié : aucune autre question du chapitre ne demande ce chiffre ; le cours le donne (exemple « احسب: في مائة امرأة مصابة »). Les quatre options ont la même longueur (6).
- Si l'on préfère garder l'énoncé actuel, remplacer au minimum `b` par `لأنّ أعراضها أشدّ وأكثر تقيّحًا من أعراض السّيلان` (49) et `c` par `لأنّها تقتل المصاب في طورها الثّالث كالزّهري` (44). Le doublon avec `quiz` Q2 resterait alors.

**M14-4 — paire proche `quiz.json` Q6 ↔ `exercices/01-tamrin.json` Q4** (signalée par le correcteur, tranchée : **à réécrire**).
Même énoncé (« أيّ/ما الخلايا التي يصيبها فيروس السّيدا؟ »), mêmes distracteurs (globules rouges,
plaquettes…), même clé. On réécrit `01-tamrin` Q4 pour interroger le **rôle** des cellules T4 ; la clé
reste à l'identifiant `c`.
- nouvel énoncé : `يصيب فيروس السّيدا الخلايا اللّمفاويّة من صنف ت4. ما دور هذه الخلايا؟`
- `a` : `تنقل الأكسيجين من الرّئتين إلى الخلايا` (38) · `b` : `تساهم في تخثّر الدّم عند حدوث جرح` (33) · `c` (clé) : `ضروريّة لنجاعة المناعة المكتسبة` (31) · `d` : `تنقل الأغذية الذّائبة إلى الخلايا` (33)
- `correctOption` : `c` (inchangé)
- explication : `خلايا ت4 من الكريات البيضاء، وهي ضروريّة لنجاعة المناعة المكتسبة — ولهذا يؤدّي موتها إلى نقص حادّ في المناعة، ومنه اسم المرض. أمّا نقل الأكسيجين فدور الكريات الحمراء، والتّخثّر دور الصّفيحات الدّمويّة، ونقل الأغذية الذّائبة دور البلازما.`
- Vérifié : ces rôles sont enseignés au chapitre `06-dirasat-ad-dam` (antérieur), et la formulation de la clé reprend le cours mot pour mot. Pas de collision avec `04-defi` Q3, qui porte sur le cycle du virus.

**M14-5 — `exercices/04-defi.json` Q5 — distracteurs triviaux dans un défi** (point signalé, tranché).
`c` (« التّلقيح ممنوع قانونيًّا في كلّ البلدان ») est une absurdité, et `b` (« الفيروس ضعيف وتقضي
عليه المناعة بسهولة ») se réfute par le simple nom de la maladie. On les remplace par deux erreurs
d'élève que le cours dément.
- `b` ancien : `لأنّ الفيروس ضعيف وتقضي عليه المناعة بسهولة` → nouveau : `لأنّ المصاب لا ينتج أيّ جسم مضادّ ضدّ الفيروس` (45)
- `c` ancien : `لأنّ التّلقيح ممنوع قانونيًّا في كلّ البلدان` → nouveau : `لأنّ الفيروس يكمن في الكريات الحمراء فلا يبلغه اللّقاح` (54)
- Explication, ajouter : ` والمصاب ينتج أجسامًا مضادّة فعلًا — وعليها يقوم اختبار إيجابيّة المصل — والفيروس يصيب خلايا ت4 لا الكريات الحمراء.`
- Clé `a` = 34 : elle n'est pas la plus longue.

### MINOR

**m14-1 — `exercices/04-defi.json` Q4** (point signalé) : relu, **aucun constat**. La clé est juste, les
distracteurs sont plausibles (mort « par le virus directement », anémie, fièvre) et l'explication réfute.

**m14-2 — `exercices/05-tadrib.json` Q4, distracteur `a`** : dans « المصافحة وتبادل التّحيّة بينهما »,
le pronom « بينهما » n'a pas d'antécédent.
- `a` → `المصافحة وتبادل التّحيّة مع المصاب` (34 ; clé `b` = 25)

**m14-3 — `quiz.json` Q9 `c` et `exercices/01-tamrin.json` Q5 `a`** : les ajouts « في المستشفيات (العموميّة) »
attribuent aux hôpitaux (publics) des transfusions de sang non contrôlé. C'est une affirmation que le cours
ne fait pas, et un message malvenu.
- `quiz` Q9 `c` → `نقل الدّم الملوّث وغير المراقب من متبرّع مصاب بالفيروس` (54 ; clé `b` = 46)
- `01-tamrin` Q5 `a` → `نقل دم ملوّث وغير مراقب من متبرّع مصاب` (38 ; clé `c` = 35, `b` = 41)

**m14-4 — `exercices/05-tadrib.json` Q2, explication** : « فينغرس الجنين في غير موضعه » → `فتنغرس المضغة في غير موضعها`.
C'est le terme du chapitre 12 au stade de la nidation.

**m14-5 — `exercices/02-tamrin.json` Q2 / `quiz.json` Q2, clés** : « بلا أعراض عند أغلب المصابين » est
approximatif, puisque chez les hommes la proportion est d'environ la moitié. Si M14-3 n'est pas appliqué,
préférer `عند ثلاثة أرباع المصابات` dans `quiz` Q2 `c`.

**m14-6 — distracteurs que l'énoncé élimine, présents avant la correction** :
- `01-tamrin` Q3 `c` (« فيروس » alors que l'énoncé dit « بكتيريا الكلاميديا ») ;
- `02-tamrin` Q4 `d` et Q5 `d` (« لا فرق » / « لا تعقيدات ») ;
- `03-boss` Q4 `d` (« لا مخاطر ») et Q5 `c` (« شكل مبكّر فقط » alors que l'énoncé dit « شكلاه ») ;
- `05-tadrib` Q2 `d` et Q5 `c` ;
- `06-defi-concours` Q2 `c` (« الخطأ الوحيد » alors que l'énoncé dit « المزدوج »).

Sans urgence.

**m14-7 — paires proches entre deux fichiers, non signalées par le correcteur** :
- `quiz` Q4 ↔ `03-boss` Q2 (« يزول القرح تلقائيًّا… ماذا يعني ذلك؟ », clé identique sur le fond) ;
- `quiz` Q7 ↔ `04-defi` Q1 (test négatif précoce).

À trancher au même titre que M14-4 si le gate « paires proches » les remonte.

### Questions relues sans constat (ch. 14)

`01-tamrin` Q2, Q6 · `02-tamrin` Q3, Q6 · `03-boss` Q1, Q3, Q6 · `04-defi` Q3, Q4, Q6 · `05-tadrib` Q3,
Q5, Q6 · `06-defi-concours` Q3, Q4, Q5, Q6 · `quiz` Q1, Q8, Q10.

**Verdict ch. 14 : à corriger avant publication.** 0 BLOCKER, 5 MAJOR (dont deux réécritures complètes).
Aucune clé fausse.

## Bilan

| Chapitre | Questions modifiées relues | Clés fausses | BLOCKER | MAJOR | MINOR | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| 12 | 37 | 0 | 1 (langue) | 7 | 6 | à corriger |
| 13 | 37 | 0 | 0 | 4 | 5 | à corriger |
| 14 | 40 | 0 | 0 | 5 | 7 | à corriger |

Points signalés par le correcteur, tranchés :
- ch13 `quiz` Q3 ↔ `03-boss` Q1 : doublon, à réécrire (M13-4) ;
- ch14 `quiz` Q6 ↔ `01-tamrin` Q4 : doublon, à réécrire (M14-4) ;
- ch13 `02-tamrin` Q4 « نحو 99 % » : faux au sens du manuel, réécriture des quatre options (M13-1) ;
- ch14 `04-defi` Q1 : indice de polarité (M14-1) ;
- ch14 `04-defi` Q4 : aucun constat ;
- ch14 `04-defi` Q5 : distracteurs triviaux (M14-5).

Après application, relancer `content:gates -- --tranche` : la mesure « clé la plus longue » et les
paires proches doivent être recalculées.
