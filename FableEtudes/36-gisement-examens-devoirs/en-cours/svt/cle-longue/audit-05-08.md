# Audit indépendant — correction « clé la plus longue », SVT 9ᵉ, chapitres 05 · 06 · 07 · 08

> Mandat : `.claude/skills/content-engine/references/audit-correction.md`, appliqué à la lettre.
> Corpus relu : `/home/user/wt-svtkey` (branche `wip/svt-9eme-cle-longue`, tête `4f90aab6`), diff
> `git diff origin/main -- content/sciences-vie-terre/<CHAPITRE>` après `fetch origin main`.
> Référence : le `cours.md` de chaque chapitre, et le manuel 105905 quand un point le demande.
> Hors périmètre : `exercices/*-examen-*`. L'auditeur n'a modifié aucun fichier du corpus.
> Les indices de questions sont 1-based. Les longueurs sont en caractères (Python `len`). Chaque
> correction proposée a été vérifiée : la clé n'y redevient pas strictement la plus longue.
> Rapport rédigé au fil de l'eau, un dossier après l'autre.

## Mesures de forme sur la tranche (avant de lire)

- `content:tranche --chapters 05,06,07,08` (moteur `/home/user/eng-svtkey`, lien `content` → ce
  corpus) : la clé est strictement la plus longue dans **0/342** questions. Trois paires proches
  restent (elles sont tranchées plus bas, aux dossiers 07-annales et 08).
- **Fuite inverse (la clé est désormais la plus courte)**, mesurée sur les 298 QCM à 3 options ou
  plus, hors examens. Sur `origin/main`, la clé était strictement la plus courte dans 11 cas (4 %).
  Sur la branche, c'est **34/298 (11 %)**. Le hasard donnerait 25 % : il n'y a donc **pas de fuite
  inverse globale**. Sept cas restent marqués, où la clé fait moins de 80 % du distracteur le plus
  court : `06-safaih/05-tadrib` Q1 (0,46) · `08/05-tadrib` Q6 (0,57) · `07-ad-dawaran/quiz` Q4
  (0,67, options de 2–3 caractères) · `07-annales/03-defi` Q1 (0,70) · `07-annales/02-sujet` Q1
  (0,76) · `05-al-hadm/quiz` Q9 (0,79) · `08/04-defi` Q3 (0,79). Chacun est traité dans son dossier.
- Positions de clé : a 34 % · b 48 % · c 12 % · d 6 %. Ce déséquilibre est **sans effet** pour
  l'élève, puisque l'affichage mélange les options. Il est noté ici pour mémoire.

---

## Dossier 1 — `05-al-hadm`

Relu : `quiz` et les exercices `01`…`06`, soit 36 questions touchées, avec leurs options non
retouchées, et le `cours.md`.
Résolution à l'aveugle : **aucune clé fausse ni ambiguë.**

### MAJOR

**M05h-1 — `exercices/03-boss.json` Q2 — l'énoncé élimine les trois distracteurs** (défaut présent
avant la correction, sur une question touchée). La question demande ce que l'expérience a prouvé
« contre l'avis de Borelli » (« ضدّ رأي بوريلّي »). Or `a` (« la viande protégée est restée
intacte »), `c` (« le broyage seul suffit ») et `d` (« l'estomac ne sécrète rien ») vont tous **dans
le sens** de Borelli. La prémisse les écarte d'un coup, et la clé se trouve sans rien savoir. On
remet trois erreurs qui contredisent aussi Borelli, mais qui vont plus loin que ce que l'expérience
de Réaumur établit.
- `a` ancien : `أنّ اللّحم المحميّ بقي كما هو لغياب الطّحن` → nouveau : `أنّ الهضم كيميائيّ صرف لا دور فيه للطّحن` (40)
- `c` ancien : `أنّ الطّحن وحده يكفي لتفكيك اللّحم في المعدة` → nouveau : `أنّ المعدة تمتصّ اللّحم المحميّ دون أن تفكّكه` (45)
- `d` ancien : `أنّ المعدة لا تفرز شيئًا يؤثّر في اللّحم` → nouveau : `أنّ حرارة جسم الطّائر وحدها تفكّك اللّحم` (40)
- La clé `b` reste inchangée (42) : `c` (45) est plus longue.
- Explication, ajouter à la fin : ` لكنّها لا تثبت أنّ الطّحن بلا دور (فهو يسرّع الهضم)، ولا تفصل الحرارة عن العصارة: ذلك ما أضافه سبالانزاني بأنبوب الماء.`

**M05h-2 — `exercices/05-tadrib.json` Q1 — la clé réunit la moitié de chaque distracteur.** La
correction a donné `a` = « الأحماض الأمينيّة **والغليسيرول** » et `d` = « **الأحماض الدّهنيّة**
وسكّر الشّعير ». La clé `b` (« الغليسيرول والأحماض الدّهنيّة ») est exactement la paire des deux
termes qui reviennent : c'est le piège de forme que nomme le mandat. On équilibre les options pour
que chaque terme apparaisse deux fois.
- `c` ancien : `الجليكوز` → nouveau : `الأحماض الأمينيّة والجليكوز` (27)
- `d` ancien : `الأحماض الدّهنيّة وسكّر الشّعير` → nouveau : `الأحماض الدّهنيّة والجليكوز` (27)
- Après correction, chaque terme apparaît deux fois : glycérol (b, a), acides gras (b, d), acides
  aminés (a, c), glucose (c, d). La clé `b` (29) est à égalité avec `a` (29). L'explication actuelle
  couvre déjà les trois classes d'aliments.

### MINOR

**m05h-1 — `quiz.json` Q9 — fuite inverse** : la clé `c` « الأوعية اللّمفاويّة » (19) est nettement
plus courte que les autres (24 / 33 / 45 ; rapport 0,79).
- `c` → `الأوعية اللّمفاويّة داخل الخملات` (32). C'est vrai : le cours et sa figure placent le
  capillaire lymphatique dans la villosité. `a` (45) reste la plus longue.

**m05h-2 — `exercices/03-boss.json` Q3, `c` neuf — distracteur que l'énoncé élimine.** « الهضم
يحتاج إلى حركة المعدة مع عصارتها » est contredit par « خارج الجسم ». Ce nouveau distracteur reprend
aussi le `d` de `quiz` Q1 (même expérience de Spallanzani, avec un énoncé presque identique).
- `c` ancien : `أنّ الهضم يحتاج إلى حركة المعدة مع عصارتها` → nouveau : `أنّ العصارة المعديّة تهضم كلّ أصناف الأغذية` (43).
  C'est une généralisation que l'expérience ne prouve pas, et la spécificité, enseignée dans ce même
  chapitre, la contredit. La clé `b` (33) n'est pas la plus longue.
- Explication, ajouter : ` ولا تقول التّجربة شيئًا عن غير اللّحم: لكلّ أنزيم مادّته.`

**m05h-3 — `exercices/06-defi-concours.json` Q5 — distracteur `a` défendable et énoncé bancal.**
« الدّهنيّات تُهضم آخر الأمر » a du vrai : selon le cours, la digestion des lipides commence dans
l'intestin grêle, après celle de l'amidon et des protides. L'énoncé met aussi en scène deux personnes
(« شخصان … في دم الأوّل ») alors que la seconde ne sert à rien.
- prompt ancien : `شخصان أكلا نفس الوجبة الدّسمة. ظهرت الدّهنيّات في دم الأوّل متأخّرة عن ظهور الجليكوز والأحماض الأمينيّة. كيف يُفسَّر هذا التّأخّر؟`
- prompt nouveau : `أكل شخص وجبة دسمة، فظهرت الدّهنيّات في دمه متأخّرة عن ظهور الجليكوز والأحماض الأمينيّة. كيف يُفسَّر هذا التّأخّر؟`
- `a` ancien : `لأنّ الدّهنيّات تُهضم آخر الأمر بعد بقيّة الأغذية` → nouveau : `لأنّ الكبد يحتجز الدّهنيّات قبل أن تبلغ الدّم` (45 ; clé `b` = 43)

**m05h-4 — `exercices/02-tamrin.json` Q5 — l'énoncé ne dit pas que la viande baigne dans une
enzyme**, alors que la clé et `d` parlent de « العصارة ». Un élève peut donc tenir `a` (« التّقطيع
وحده يهضم دون عصارة ») pour compatible avec l'énoncé. Le défaut existait avant la correction.
- prompt ancien : `لماذا يختفي 20 غ من اللّحم المقطّع في 24 ساعة بينما تبقى نفس الكتلة في قطعة واحدة ظاهرة؟`
- prompt nouveau : `في عصارة معديّة في 37 درجة، لماذا يختفي 20 غ من اللّحم المقطّع في 24 ساعة بينما تبقى نفس الكتلة في قطعة واحدة ظاهرة؟`

**m05h-5 — explications où la justification est recollée en fin de texte** sans lien logique avec la
phrase qui précède :
- `quiz.json` Q1 : « فالهضم ليس ظاهرة ميكانيكيّة صرفة… » vient après la phrase sur l'eau, et le
  « ف » ne s'y rattache à rien. Explication nouvelle : `لا أسنان ولا معدة في التّجربة، والمتغيّر الوحيد بين الأنبوبين هو العصارة. فالانحلال يُنسب إليها: في العصارة ما يفكّك اللّحم، والهضم ليس ظاهرة ميكانيكيّة صرفة كما ظنّ بوريلّي. أمّا الماء فهو على العكس طرف في التّفاعل: الأنزيم ييسّر مفعوله.`
- `exercices/03-boss.json` Q6, dernière phrase : accord du verbe. `يليه فتحة الشّرج` → `تليه فتحة الشّرج`.

**m05h-6 — fuite inverse légère** : `exercices/04-defi.json` Q5, clé `b` (32) contre 36 / 36 / 56.
- `b` → `يصبّ اللّمف في الدّم عبر الأوردة الكبرى` (39 ; `a` = 56). Le cours dit : « الأوعية
  اللّمفاويّة الكبرى مرتبطة بالأوردة ».

**m05h-7 — paires proches entre fichiers** (fichiers distincts, donc pas des doublons au sens du
mandat ; à surveiller) :
- `quiz` Q6 ↔ `01-tamrin` Q4 : même fait (l'unité des protides), même clé (« الأحماض الأمينيّة »).
- `quiz` Q3 ↔ `02-tamrin` Q3 : chaque question porte sur un témoin différent, et leurs options se
  croisent (la clé de l'une est un distracteur de l'autre). Le correcteur l'a voulu ainsi, et le
  défaut n'est pas à corriger : chaque question est juste pour son énoncé.
- `quiz` Q10 ↔ `05-tadrib` Q4 : même fait (la fréquence de l'acidité), mais pas le même angle
  (« durée entre deux nettoyages » / « répétition des crises »).

### Questions relues sans constat (05-al-hadm)

`quiz` Q2, Q3, Q5, Q6, Q8, Q10 · `01-tamrin` Q1, Q3, Q5, Q6 · `02-tamrin` Q1, Q2, Q3, Q6 ·
`03-boss` Q1, Q4, Q5 · `04-defi` Q1, Q3, Q6 · `05-tadrib` Q3, Q4, Q6 · `06-defi-concours` Q2, Q3,
Q4, Q6.

**Verdict 05-al-hadm : à corriger avant publication** (2 MAJOR). Aucune clé fausse, aucune faute de
langue bloquante.

---
## Dossier 2 — `05-barakin`

Relu : `quiz` et `01`…`06`, soit 33 questions touchées (avec leurs options non retouchées) ; le
`cours.md` ; l'ordre des chapitres (04-zalazil = 18, 05-barakin = 19, 06-safaih = 20 : la
structure du globe, avec « الوشاح » et « الليثوسفير », n'est enseignée qu'au chapitre **suivant**).
Résolution à l'aveugle : **aucune clé fausse ni ambiguë.**

### MAJOR

**M05b-1 — `quiz.json` Q6 — indice de forme : la clé est la seule option sans « + ».** La
correction a remplacé `موادّ سائلة (لابة) + موادّ غازية + …` par « موادّ سائلة وغازية وصلبة ». Or
les trois distracteurs gardent la forme « X + Y + Z ». La clé est aussi la seule option qui nomme
des catégories, ce que l'énoncé demande ; mais c'est le savoir testé, et ce point peut rester.
- `a` (clé) ancien : `موادّ سائلة وغازية وصلبة` → nouveau : `موادّ سائلة + غازية + صلبة` (26 ; `c` = 37)

**M05b-2 — `quiz.json` Q5 — l'énoncé souffle la réponse et élimine les trois distracteurs.**
L'énoncé dit « (الهادئ) » et la clé dit « بهدوء ». `a` (« انفجار عنيف ») contredit « الهادئ » ;
`c` (« عدم خروج أيّ مادّة ») et `d` (« خروج الماء فقط ») ne sont pas des éruptions. Les options non
retouchées sont en cause.
- prompt ancien : `ما الذي يميّز الثوران البركاني الانسيابي (الهادئ)؟` → nouveau : `ما الذي يميّز الثوران البركاني الانسيابي؟`
- `c` ancien : `عدم خروج أيّ مادّة من الفوّهة` → nouveau : `قذف رماد كثيف يغطّي المنحدرات` (29)
- `d` ancien : `خروج الماء فقط دون لابة` → nouveau : `خروج غازات محبوسة تنطلق فجأة` (28)
- La clé `b` reste inchangée (26) ; `a` (46) est la plus longue. Retirer d'éventuels
  `misconceptionTag` sur `c` et `d` s'ils ne conviennent plus. Explication, ajouter : ` والرماد الكثيف والغازات المحبوسة التي تنطلق فجأة علامات الثوران الانفجاري.`

**M05b-3 — `exercices/05-tadrib.json` Q2 — des notions pas encore enseignées dans les distracteurs.**
« الوشاح », « النواة », « الليثوسفير » et « الأسثينوسفير » ne sont enseignés qu'en 06-safaih. La
correction a même ajouté « القشرة الأرضية » à `d` en gardant « الوشاح ». Ces distracteurs sont faits
de mots que l'élève n'a jamais vus. On les remplace par des confusions du chapitre lui-même : les
projections et les matières, qui ne sont pas des parties de la structure.
- `c` ancien : `الليثوسفير والأسثينوسفير فقط` → nouveau : `اللابة والرماد والقنابل البركانية` (33)
- `d` ancien : `الوشاح والنواة والقشرة الأرضية` → nouveau : `الصهارة واللابة والغازات البركانية` (34)
- Clé `a` (33) inchangée ; `b` (40) et `d` (34) sont plus longues.
- explication nouvelle : `يتكوّن البركان من خزّان صهاري في العمق تصعد منه الصهارة عبر مدخنة لتخرج من فوّهة في القمّة. البؤرة والمركز السطحي والموجات الزلزالية مصطلحات خاصّة بالزلازل، واللابة والرماد والقنابل مقذوفات، والصهارة والغازات موادّ: لا شيء منها جزء من بنية البركان.`

**M05b-4 — `exercices/03-boss.json` Q1 — l'explication réfute une option qui n'existe plus.**
« ولا يوجدان في الجوّ » répond à l'ancien `d` (« كلاهما يوجد في الجوّ فقط »). Le nouveau `d`
(« كلاهما في الباطن، وما يخرج إلى السطح غاز فقط ») n'est pas réfuté.
- dans l'explication, ancien : `ولا يوجدان في الجوّ.` → nouveau : `ولا يقتصر ما يخرج إلى السطح على الغاز: الصهارة نفسها تخرج وتسيل لابةً.`

**M05b-5 — doublons de fait entre `03-boss` et `05-tadrib`** (même énoncé à un mot près, même
clé, distracteurs de même nature). Ils existaient avant la correction, mais celle-ci a rapproché les
clés. On propose de réécrire complètement la question de `05-tadrib` en gardant l'identifiant de
clé :
- **`05-tadrib` Q6 ↔ `03-boss` Q6** (« وُجد في إقليم تربة بركانية خصبة وينابيع… ما العلاقة
  الصحيحة؟ »). Réécriture de `05-tadrib` Q6 :
  - prompt : `أيّ ممّا يلي ليس من فوائد البراكين؟`
  - `a` (clé) : `تلوّث الهواء بالغازات` (21) · `b` : `خصوبة التربة البركانية` (22) · `c` : `الطاقة الحرارية الأرضية` (23) · `d` : `الثروات المعدنية` (16). La clé n'est pas la plus longue.
  - explication : `تلوّث الهواء من مخاطر البراكين لا من فوائدها. أمّا خصوبة التربة البركانية والطاقة الحراريّة الأرضيّة (الجيوحراريّة) والثروات المعدنيّة فمن فوائدها، ومعها ينابيع المياه السّاخنة.`
  - Retirer les `misconceptionTag` des anciennes options.
- **`05-tadrib` Q5 ↔ `03-boss` Q3** (« لماذا تتراصف (معظم) البراكين والزلازل في الأحزمة نفسها؟ »,
  même clé). Le même fait figure aussi dans `04-defi` Q2. Réécriture de `05-tadrib` Q5 :
  - prompt : `أين يقع «حزام النار» الذي تتركّز فيه أغلب البراكين النشطة؟`
  - `a` (clé) : `حول المحيط الهادئ` (17) · `b` : `حول المحيط الأطلسي` (18) · `c` : `على طول خطّ الاستواء` (20) · `d` : `حول البحر الأبيض المتوسّط` (25)
  - explication : `حزام النار يحيط بالمحيط الهادئ، وفيه أكبر تجمّع للبراكين والزلازل لأنّه يتبع حدود صفائح تكتونية. وفي البحر الأبيض المتوسّط براكين أيضًا، لكنّه ليس حزام النار، ولا علاقة لتوزّع البراكين بخطّ الاستواء.`
- **`05-tadrib` Q1 ↔ `quiz` Q3** (« ما الفرق … بين الصهارة واللابة؟ ») : les clés sont presque
  identiques (« الصهارة في الباطن، واللابة هي … ») et les deux questions ont le même distracteur
  miroir. Réécriture de `05-tadrib` Q1 sur le critère du lieu :
  - prompt : `حمم متوهّجة تسيل على منحدر بركان. ما اسم هذه المادّة الآن، وأين كانت تُسمّى صهارة؟`
  - `a` (clé) : `لابة، وكانت صهارة في الخزّان والمدخنة` (37) · `b` : `صهارة، وستصير لابة حين تبرد وتتصلّب` (35) · `c` : `لابة، وكانت صهارة في المخروط البركاني` (37) · `d` : `صهارة، لأنّها ما زالت منصهرة ومتوهّجة` (37). La clé est à égalité avec `c` et `d`.
  - explication : `الاسم يتغيّر بالموقع لا بالحالة: هي صهارة ما دامت في الباطن (الخزّان والمدخنة)، ولابة بمجرّد خروجها إلى السطح ولو بقيت منصهرة متوهّجة. والمخروط جبل خارجيّ تتراكم فيه المقذوفات، لا مكانًا للصهارة.`

**M05b-6 — `exercices/04-defi.json` Q4 — l'énoncé élimine les trois distracteurs et souffle la
clé.** L'énoncé demande ce qui « يجمع بين الضرر والفائدة », et la clé est la seule option à dire
« مخاطر … وفوائد ». `a` (« مفيدة فقط ») et `b` (« ضارّة فقط ») sont écartés par l'énoncé lui-même.
Réécriture sur le mécanisme de la fertilité, en gardant la clé `c` :
- prompt nouveau : `بعد سنوات من ثوران انفجاري، أصبحت أراضي المنطقة من أخصب الأراضي الزراعية رغم الدمار الذي خلّفه الثوران. ما سبب هذه الخصوبة؟`
- `a` : `لأنّ حرارة الحمم تعقّم التربة من الآفات لسنوات` (46) · `b` : `لأنّ الرماد يحبس ماء المطر فلا تجفّ التربة أبدًا` (48) · `c` (clé) : `لأنّ موادّ البركان المتحلّلة تغني التربة بالمعادن` (49) · `d` : `لأنّ الثوران يقتل الحشرات فتنمو المحاصيل بلا عائق` (49)
- explication : `للبركان مخاطر آنية (دمار وحرائق ورماد) وفوائد لاحقة: موادّه، كالرماد واللابة المتحلّلة، تغني التربة بالمعادن فتصير خصبة مع الزمن. أمّا حرارة الحمم فتنقضي بانتهاء الثوران، والرماد لا يمنع جفاف التربة، وموت الحشرات لا يفسّر خصوبة تدوم سنوات.`

### MINOR

**m05b-1 — distracteurs triviaux ou que l'énoncé élimine** (présents avant la correction, sur des
questions touchées) :
- `quiz` Q8 : les trois distracteurs (« تدمير », « خنق », « تلوّث ») sont des dommages, que le sens
  commun écarte quand on demande « فائدة ». `b` → `تكوّن النفط في الصخور البركانية` (31) ; `c` →
  `تنقية الهواء بالغازات البركانية` (31). La clé `a` (22) n'est pas la plus longue. Explication,
  ajouter : ` والنفط يتكوّن في الصخور الرسوبيّة لا البركانيّة، والغازات البركانيّة تلوّث الهواء ولا تنقّيه.`
- `quiz` Q2 `d` (« في الرماد البركاني » n'est pas un lieu) → `في المدخنة البركانية` (20 ; clé = 18).
  C'est un piège sérieux : on confond le lieu où le magma passe et celui où il s'accumule.
- `02-tamrin` Q6 : `c` « المخروط البركاني » et `d` « الخزّان الصهاري » ne sont pas des projections,
  alors que l'énoncé dit « مقذوف ». `c` → `القنابل البركانية` (17) ; `d` → `الكُتل الصخرية` (14).
  La clé `b` (15) n'est pas la plus longue. Ces deux projections retombent près du volcan, ce qui en
  fait de vrais pièges.
- `02-tamrin` Q2 `a` « لون اللابة ودرجة حرارتها » : la température est réellement liée à la
  viscosité, donc l'option se défend. → `لون اللابة وشكل الفوّهة` (23).
- `04-defi` Q5 `d` « الخزّان الصهاري لا يحتوي أيّ غازات » est contredit par l'énoncé (« الصهارة التي
  كانت في الخزّان » est plus riche en gaz). La fin de l'explication, « وهي السبب في ذلك الفرق »,
  n'a pas de référent clair : la supprimer.
- `06-defi-concours` Q5 `b` et `d` sont contredits par « تُعدّ … خطرًا واسع النطاق ». À reprendre
  plus tard.

**m05b-2 — explications où un ajout recollé fait doublon** :
- `02-tamrin` Q4 : la dernière phrase, « وأشهر هذه الأحزمة حزام النار حول المحيط الهادئ. », répète
  la première. La supprimer.
- `03-boss` Q5 : « ويضاف إلى ذلك تلوّث الهواء. » répète « ويلوّث الهواء ». La supprimer.

**m05b-3 — langue et terminologie** (explications non retouchées de questions touchées) :
- `06-defi-concours` Q2 : `فتتراكم وتزداد الضغط داخل المدخنة` → `فتتراكم ويزداد الضغط داخل المدخنة` (ازداد est intransitif).
- `06-defi-concours` Q1, Q2 et Q6 parlent de « اللابة اللزجة » qui « تحبس الغازات … داخل
  المدخنة ». Le cours pose en règle que c'est la **صهارة** tant qu'elle est dedans. À harmoniser
  avec le cours lors d'un passage de qualité (« الصهارة اللزجة »).

**m05b-4 — paires proches dans le chapitre** (le même fait est testé deux fois, mais les options
diffèrent) : `03-boss` Q2 ↔ `05-tadrib` Q3 (même énoncé : « بركان صهارته لزجة جدًّا وغنيّة
بالغازات ») ; `quiz` Q6 ↔ `05-tadrib` Q4 (les trois sortes de projections).

### Questions relues sans constat (05-barakin)

`quiz` Q1, Q3, Q7 · `01-tamrin` Q5 · `02-tamrin` Q3 · `03-boss` Q2, Q4 · `04-defi` Q2, Q3, Q6 ·
`05-tadrib` Q3, Q4 · `06-defi-concours` Q1, Q6.

**Verdict 05-barakin : à corriger avant publication** (6 MAJOR, dont 3 doublons de fait). Aucune clé
fausse.

---
## Dossier 3 — `06-dirasat-ad-dam`

Relu : `quiz` et `01`…`06`, soit 32 questions touchées (avec leurs options non retouchées), et le
`cours.md`.
Résolution à l'aveugle : **aucune clé fausse ni ambiguë.**

### MAJOR

**M06d-1 — la clé réunit la moitié de chaque distracteur** (le piège nommé par le mandat). Trois
questions sont touchées, et la correction a créé ou aggravé le défaut dans les trois :
- **`05-tadrib` Q1** (la forme de l'hématie). `c` « قرصيّة مقعّرة الوجهين ذات نواة » donne la
  forme, `d` « مغزليّة بلا نواة » donne « بلا نواة », et la clé `b` est leur somme. On fait un 2×2
  propre :
  - `d` ancien : `مغزليّة بلا نواة` → nouveau : `كرويّة بلا نواة` (15). Formes {قرصيّة: b, c ;
    كرويّة: a, d} × noyau {بلا: b, d ; ذات: a, c}. La clé `b` (30) est à égalité avec `c`.
- **`03-boss` Q5** (les constituants du plasma). `d` (« الماء بنحو 900 ‰، ثمّ الدّهنيّات ») donne
  le premier terme et `b` (« البروتيدات … ») le second. La clé est la seule option qui porte les
  deux termes majoritaires. On équilibre :
  - `c` ancien : `الأملاح المعدنيّة بنحو 900 ‰، ثمّ الماء` → nouveau : `الماء بنحو 900 ‰، ثمّ الدّهنيّات` (32)
  - `d` ancien : `الماء بنحو 900 ‰، ثمّ الدّهنيّات` → nouveau : `البروتيدات بنحو 900 ‰، ثمّ الأملاح` (34)
  - Premier terme : eau (a, c), protides (b, d). Second terme : chacun une fois. La clé `a` (32)
    n'est pas la plus longue. Explication, ajouter : ` والأملاح المعدنيّة بضعة أجزاء في الألف فقط (الصّوديوم 3,3 ‰).`
- **`04-defi` Q5** (714). `b` donne « 714 », `d` donne « أقلّ عددًا لا أهمّيّة », et la clé est la
  seule option qui porte les deux. On complète le 2×2 :
  - `c` ancien : `نحو 7000، والبيضاء أكثر عددًا وأكبر أهمّيّة` → nouveau : `نحو 71، والبيضاء أقلّ أهمّيّة لقلّتها` (37)
  - Avec ce seul changement, la clé `a` (39) deviendrait **strictement la plus longue** (b 38, c 37,
    d 38). Il faut donc raccourcir la clé et son jumeau `d` :
    - `a` (clé) ancien : `نحو 714، والبيضاء أقلّ عددًا لا أهمّيّة` → nouveau : `نحو 714، والبيضاء أقلّ عددًا لا دورًا` (37)
    - `d` ancien : `نحو 71، والبيضاء أقلّ عددًا لا أهمّيّة` → nouveau : `نحو 71، والبيضاء أقلّ عددًا لا دورًا` (36)
  - Résultat : a 37 · b 38 · c 37 · d 36. La clé n'est pas la plus longue, et le 2×2 est exact
    ({714, 71} × {أقلّ عددًا لا دورًا, أقلّ أهمّيّة لقلّتها}).
  - Explication, remplacer `والجواب 71 خطأ بعشرة أضعاف في القسمة.` par `والجواب 71 خطأ بعشرة أضعاف في القسمة، وقلّة العدد لا تعني قلّة الدّور.`

**M06d-2 — `exercices/03-boss.json` Q6 — indice de forme : la clé est la seule option sans
« كلّها ».** La correction a écrit « نقل الغازات كلّها » dans les trois distracteurs, contre « جزء
من الغازات » pour la clé. La clé reprend aussi « الأغذية · الفضلات » de `c` et « الأجسام المضادّة »
de `d`.
- `c` ancien : `نقل الأغذية · نقل الفضلات · هضم الدّهنيّات · نقل الغازات كلّها` → nouveau : `نقل الأغذية · نقل الفضلات · هضم الدّهنيّات · جزء من الغازات` (59).
  « جزء » apparaît alors deux fois, et `c` ne se distingue de la clé que par « هضم الدّهنيّات »,
  un vrai piège. La clé `a` (68) reste à égalité avec `d`.

**M06d-3 — doublons de fait entre le quiz et les exercices** (même énoncé, même clé, mêmes
distracteurs). La correction les a rapprochés en recopiant les distracteurs de l'un dans l'autre :
- **`04-defi` Q6 ↔ `quiz` Q2** (« لماذا يُضاف/نضيف أكسلات الأمونيوم … »). Le nouveau `d` de
  `04-defi` (« لحفظ الدّم من الجراثيم مدّة التّجربة ») recopie le `d` du quiz. Réécriture complète
  de `04-defi` Q6, clé `b` :
  - prompt : `نسي تلميذ إضافة أكسلات الأمونيوم إلى الدّم قبل تركه يومين في الثّلاجة. ماذا سيلاحظ؟`
  - `a` : `ثلاث طبقات عاديّة، لكنّها تظهر أبطأ` (35) · `b` (clé) : `كتلة واحدة متخثّرة لا تنفصل طبقاتها` (35) · `c` : `طبقة بلازما واحدة بعد تحلّل الكريات` (35) · `d` : `دمًا سائلًا متجانسًا لا يترسّب` (30)
  - explication : `أكسلات الأمونيوم تمنع التّخثّر. فبدونها يتخثّر الدّم ويصير كتلة واحدة تحبس الخلايا في شبكة، فلا تنفصل البلازما عن الخلايا ولا تُقاس النّسب. فالتّخثّر لا يبطئ التّرسّب بل يمنعه، ولا يحلّ الكريات، ولا يُبقي الدّم سائلًا.`
- **`03-boss` Q2 ↔ `quiz` Q7** (40 000 plaquettes, même clé « نزف يطول », et les distracteurs
  « العدوى المتكرّرة » / « فقر الدّم مع الإرهاق » recopiés du quiz). Réécriture de `03-boss` Q2,
  clé `b`, dans l'esprit du boss (« اقرأ تحليل دم ») :
  - prompt : `ثلاثة مرضى عدد صفيحاتهم في المم³: الأوّل 40 000، الثّاني 200 000، الثّالث 500 000. من المعرّض لنزف يطول بعد الجرح؟`
  - `a` : `الثّالث، لأنّ عدده تجاوز الحدّ الأعلى` (37) · `b` (clé) : `الأوّل، لأنّ عدده دون الحدّ الأدنى` (34) · `c` : `الأوّل والثّالث، لأنّهما خارج المجال العاديّ` (44) · `d` : `الثّاني، لأنّه الأقرب إلى الحدّ الأدنى` (38)
  - explication : `المجال العاديّ من 150 000 إلى 450 000. الأوّل دونه بكثير، والصّفيحات هي التي توقف النّزف بالتّخثّر، فنقصها يطيل النّزف. والثّاني داخل المجال. والثّالث فوقه، لكنّ كثرة الصّفيحات لا تطيل النّزف: ما يطيله هو نقصها.`

**M06d-4 — `exercices/04-defi.json` Q4 — la phrase ajoutée à l'explication dit le faux.** Elle a
été recollée après la phrase sur le glucose : « … ومسارها معاكس: من المعي إلى الخلايا. **فهي
تُحمل إلى الكلية والغدد العرقيّة.** » Le pronom « هي » renvoie au glucose et aux acides aminés, et
l'explication affirme donc que les nutriments vont aux organes d'excrétion.
- explication nouvelle : `البولة والحمض البوليّ فضلتان ناتجتان عن نشاط الخلايا، تحملهما البلازما إلى أعضاء الإخراج: الكلية والغدد العرقيّة. أمّا الجليكوز والأحماض الأمينيّة فمغذّيات لا فضلات، ومسارها معاكس: من المعي إلى الخلايا.`

**M06d-5 — `exercices/06-defi-concours.json` Q2 — l'observation de l'énoncé élimine les trois
distracteurs.** L'énoncé dit « فارتفع عدد كرياته الحمراء ». Or le nouveau `b` parle des globules
**blancs**, `c` des plaquettes, et `d` (« لا علاقة للارتفاع بالدّم ») nie l'observation. On les
remplace par de fausses explications de **la hausse des hématies**.
- `b` ancien : `الجسم يعوّض قلّة الأكسجين بزيادة الكريات البيضاء` → nouveau : `البرد يزيد إنتاج الكريات الحمراء لتدفئة الجسم` (45)
- `c` ancien : `البرد يزيد عدد الصّفيحات الدّمويّة` → nouveau : `قلّة الأكسجين تجعل الكريات الحمراء تنقسم أسرع` (45).
  Le cours le contredit : l'hématie, sans noyau, ne se divise pas.
- `d` ancien : `لا علاقة للارتفاع بالدّم` → nouveau : `الجسم يزيد الكريات ليحمل ثنائي أكسيد الكربون الزّائد` (52)
- La clé `a` (39) n'est pas la plus longue.
- dans l'explication, ancien : `والنّاقلات هي الكريات الحمراء بهيموغلوبينها، لا البيضاء.` → nouveau : `والنّاقلات هي الكريات الحمراء بهيموغلوبينها. وهي لا تنقسم لأنّها بلا نواة، ولا تزيد لتدفئة الجسم، والغاز الذي ينقص في المرتفعات هو الأكسجين لا ثنائي أكسيد الكربون.`

### MINOR

**m06d-1 — `exercices/03-boss.json` Q4 — phrase recollée sans lien.** « … ومع ذلك تُعدّ كلّ منها
بالمجهر لا في الأنبوب » : « ومع ذلك » n'a pas de sens après la phrase précédente, et l'accord est
fautif.
- dernière phrase, ancien : `وعدد الكريات الحمراء يفوق عدد البيضاء بمئات المرّات، ومع ذلك تُعدّ كلّ منها بالمجهر لا في الأنبوب.` → nouveau : `أمّا العدد فيُقاس بالمجهر لا في الأنبوب: الكريات الحمراء تفوق البيضاء بمئات المرّات.`

**m06d-2 — `exercices/06-defi-concours.json` Q6 — exactitude et énoncé** (antérieur à la
correction) : après **deux jours** de jeûne, la réserve de glycogène du foie est épuisée (≈ 24 h).
La clé « من الغليكوجين المخزون في الكبد » est donc discutable pour un lecteur informé. De plus,
l'énoncé commence par « جدول: » alors qu'il n'y a aucun tableau.
- prompt ancien : `جدول: مريض صام يومين فبقي جليكوز دمه قرب 1 غ في اللتر. من أين جاء هذا الجليكوز؟` → nouveau : `شخص صام من الفجر إلى المغرب فبقي جليكوز دمه قرب 1 غ في اللتر. من أين جاء هذا الجليكوز؟`
- explication : remplacer `في هذين اليومين` par `في هذه السّاعات`.

**m06d-3 — distracteurs que l'énoncé élimine** (présents avant la correction) : `04-defi` Q3 `a`
(« الدّم لا يتحرّك » alors que l'énoncé dit « في حركة دائمة ») ; `06-defi-concours` Q3 `d`
(« الكلية تصنع الهرمون » alors que le texte dit qu'il a été injecté) ; `06-defi-concours` Q5 `b`
(« قياس الحجم غير ممكن » alors que l'énoncé suppose la mesure) ; `06-defi-concours` Q6 `a` (« من
الأكل » alors que la personne jeûne). À reprendre lors d'un passage de qualité.

### Questions relues sans constat (06-dirasat-ad-dam)

`quiz` Q2, Q3, Q4, Q5, Q7, Q10 · `01-tamrin` Q1, Q4, Q5 · `02-tamrin` Q2, Q4, Q5, Q6 · `03-boss`
Q1 · `04-defi` Q1 · `05-tadrib` Q2, Q3 · `06-defi-concours` Q1, Q3, Q4, Q5.

**Verdict 06-dirasat-ad-dam : à corriger avant publication** (5 MAJOR). Aucune clé fausse. Une
explication dit le faux (M06d-4).

---
## Dossier 4 — `06-safaih-taktuniya`

Relu : `quiz` et `01`…`06`, soit 32 questions touchées (avec leurs options non retouchées), et le
`cours.md`. On a aussi vérifié les points que signale le correcteur : `quiz` Q2 refait en 2×2, et
les termes « الوشاح » et « المتحجّرات ». Le cours enseigne bien « الوشاح » et « المتحجّرات » (« الأدلّة
الأحفورية (المتحجّرات) »). L'harmonisation de `06-defi-concours` Q6 (« الأحافير » → « المتحجّرات »,
« الرداء » → « الوشاح ») et la correction de « عند التقاربهما » → « عند تقاربهما » (`06-defi-concours`
Q4) sont **justes**.
Résolution à l'aveugle : **aucune clé fausse ni ambiguë.**

`quiz` Q2 (2×2) est **conforme** : épaisseur {أسمك : b, c ; أرقّ : a, d} × densité {أكثر : a, b ;
أقلّ : c, d}, quatre options de 44 caractères, une seule juste (`c`).

### MAJOR

**M06s-1 — `exercices/05-tadrib.json` Q5 — la réécriture a créé un doublon de fait avec `02-tamrin`
Q5.** Les deux questions ont le même énoncé (« أيّ ممّا يلي ليس / لم يكن من أدلّة فاجنر على انجراف
القارّات؟ ») et les **mêmes trois distracteurs** (côtes, fossiles, roches et chaînes) ; seule la clé
change. Le fait « le moteur n'est pas une preuve de Wegener » est en outre déjà testé dans `03-boss`
Q6 et `06-defi-concours` Q6. Réécriture complète de `05-tadrib` Q5, clé `a`, sur un exemple du cours
(l'Islande) :
- prompt : `في إيسلندا وادٍ صخريّ يتّسع كلّ سنة بنحو سنتيمترين، على أحد جانبيه صفيحة أمريكا الشمالية وعلى الآخر الصفيحة الأوراسية. على أيّ نوع من الحدود تقع إيسلندا؟`
- `a` (clé) : `حدود متباعدة عند ظهرة محيطية` (28) · `b` : `حدود متقاربة عند منطقة طمر` (26) · `c` : `وسط صفيحة بعيدًا عن أيّ حدود` (28) · `d` : `حدود متقاربة بين صفيحتين قارّيتين` (33)
- explication : `الوادي يتّسع لأنّ الصفيحتين تتباعدان: إيسلندا جزء ظاهر من الظهرة الأطلسية، حيث تتكوّن قشرة جديدة. أمّا الطمر وتصادم صفيحتين قارّيتين فحدود متقاربة تقصر عندها المسافة ولا تطول، ووجود صفيحتين على جانبي الوادي ينفي أن يكون في وسط صفيحة.`
- Retirer les `misconceptionTag` des anciennes options.

**M06s-2 — `exercices/04-defi.json` Q2 — la clé raccourcie repose sur une notion non enseignée.**
La clé « تغوص الصفيحة الأقدم تحت الأحدث » se déduisait de sa justification, que la correction a
retirée (« (الأبرد والأكثر كثافة) »). Or le cours ne dit nulle part que la croûte océanique se
densifie en vieillissant. La clé devient un fait à savoir par cœur, et ce fait n'est pas enseigné.
On met la prémisse dans l'énoncé (la clé reste courte et juste, et `a` reste un piège plausible) :
- prompt ancien : `تتقارب صفيحتان محيطيتان متساويتا الكثافة تقريبًا. أيّ نتيجة أكثر اتّساقًا مع آليّة الطمر؟`
- prompt nouveau : `تتقارب صفيحتان محيطيتان متساويتا الكثافة تقريبًا، علمًا أنّ القشرة المحيطية تبرد فتزداد كثافتها كلّما تقادمت. أيّ نتيجة أكثر اتّساقًا مع آليّة الطمر؟`

**M06s-3 — `exercices/03-boss.json` Q3, `d` non retouché — distracteur défendable que l'explication
ne réfute pas.** « البذور حملتها الرياح عبر المحيط الأطلسي » est une hypothèse de dispersion
réelle, qu'un élève peut soutenir. L'explication ne réfute que la nage (`a`).
- `d` ancien : `البذور حملتها الرياح عبر المحيط الأطلسي` → nouveau : `مياه المحيط حملت المتحجّرات من قارّة إلى أخرى` (45 ; clé `b` = 36)
- Explication, ajouter : ` والمتحجّرات توجد في صخور القارّتين نفسها، فلم تنقلها مياه المحيط.`

**M06s-4 — `exercices/06-defi-concours.json` Q4, `b` — l'énoncé le contredit.** L'énoncé dit
« صفيحة قارّية (أقلّ كثافة) », et `b` dit « الصفيحة القارّية، لأنّها أكثف ». On le remplace par
l'erreur que nomme le cours (« لأنّها أسمك »).
- `b` ancien : `الصفيحة القارّية، لأنّها أكثف` → nouveau : `الصفيحة القارّية، لأنّها أسمك` (29 ; clé `a` = 29, à égalité)
- Explication, ajouter : ` والسُّمك لا يقرّر الغوص: القارّية أسمك لكنّها أخفّ.`

**M06s-5 — `exercices/04-defi.json` Q5 — l'énoncé élimine les trois distracteurs.** `b` (« السواحل لا
تتطابق أصلًا ») nie la prémisse ; `c` (« التطابق وحده يكفي تمامًا ») contredit « لا يكفي » ; `d`
(« المتحجّرات تنفي الانجراف ») contredit « احتاج إلى أدلّة أخرى ». La clé se trouve sans rien
savoir.
- `b` → `لأنّ تطابق السواحل يفسّره ارتفاع مستوى البحار` (45)
- `c` → `لأنّ فاجنر لم يكن يملك خرائط دقيقة للسواحل` (42)
- `d` → `لأنّ السواحل يغيّر شكلَها المدّ والجزر كلّ يوم` (46)
- La clé `a` (32) n'est pas la plus longue.
- Explication, ajouter : ` والمدّ والجزر ومستوى البحار لا يصنعان تطابقًا بين قارّتين، والخرائط لم تكن هي المشكل: الشكل وحده لا يميّز الصدفة من الالتصاق.`

**M06s-6 — `exercices/05-tadrib.json` Q1 (réécrit) — fuite inverse forte.** La clé « الوشاح » (6)
est le seul mot unique face à 13 / 15 / 15 caractères (rapport 0,46). L'élève qui hésite prend le
terme nu.
- `a` (clé) ancien : `الوشاح` → nouveau : `الوشاح الصخري` (13 ; `b` et `c` = 15). Le cours dit « الوشاح:
  الطبقة الوسطى … صخري ».

### MINOR

**m06s-1 — `quiz.json` Q4 — distracteurs qui ne sont pas des noms de continent.** La question
demande « القارّة العملاقة », et `a` « الأسثينوسفير », `b` « الظهرة », `d` « الليثوسفير » s'éliminent
à vue. Le défaut est antérieur à la correction. Proposition : `a` → `أوراسيا` (7) · `b` → `إفريقيا`
(7) · `d` → `لوراسيا` (7). La clé `c` « بانجيا » (6) est la plus courte, à un caractère près.
Explication : remplacer la dernière phrase par `أمّا أوراسيا وإفريقيا فقارّتان حاليّتان كانتا من أجزائها.`
Si l'on veut éviter « لوراسيا » (terme non enseigné), garder `d` = `الليثوسفير`.

**m06s-2 — explications où une phrase recollée répète ce qui précède** :
- `02-tamrin` Q1 : « وتقع هذه السلسلة في وسط المحيط. » (déjà dit par « وسط المحيط ») → supprimer.
- `02-tamrin` Q6 : « والخنادق المصاحبة للطمر خنادق محيطية عميقة، والزلازل فيها قويّة. » → supprimer.
- `04-defi` Q1 : « وهذا توسّع محيطي متماثل. » répète « أي توسّع محيطي متماثل » → supprimer.
- `05-tadrib` Q3 : « فهي تتكوّن من الصهارة الصاعدة عند الظهرة. » vient après « والصفائح هناك
  تتباعد », si bien que « هي » renvoie aux plaques → `فالقشرة الجديدة تتكوّن من الصهارة الصاعدة عند الظهرة.`

**m06s-3 — un même fait testé plusieurs fois dans le chapitre.** Pour chaque paire, on propose de
réécrire la question de `05-tadrib`, qui est la révision :
- « Quelle plaque plonge ? » apparaît quatre fois : `quiz` Q7, `03-boss` Q1, `05-tadrib` Q4
  (réécrit en « صحّح كلام التلميذ ») et `06-defi-concours` Q4. Les formes restent distinctes, donc
  on garde.
- `05-tadrib` Q3 ↔ `quiz` Q6 (« ماذا يحدث عند الظهرة/الظهرات المحيطية؟ », même clé, deux
  distracteurs communs). Réécriture proposée pour `05-tadrib` Q3, clé `a` :
  prompt `ما الذي يصعد عند الظهرة فيكوّن القشرة المحيطية الجديدة؟` · `a` `صهارة من الوشاح تبرد فتتصلّب` (28) · `b` `أملاح من ماء البحر تترسّب وتتصلّب` (33) · `c` `قطع من القشرة القارّية تنزلق إليها` (34) · `d` `صهارة من النواة الخارجية السائلة` (32) ; explication `عند الظهرة يصعد الصهير من الوشاح ويبرد فيكوّن قشرة محيطية جديدة. فهو لا يأتي من النواة، ولا تتكوّن القشرة من أملاح البحر ولا من قطع قارّية.`
- `05-tadrib` Q6 ↔ `quiz` Q8 (les séismes et volcans aux frontières des plaques).
- `04-defi` Q4 ↔ `quiz` Q3 : la correction a donné **le même texte** aux deux clés (« القشرة وأعلى
  الوشاح الصلب »). Les énoncés sont distincts (plaque / lithosphère).

**m06s-4 — distracteurs que l'énoncé élimine** (défauts antérieurs à la correction) : `04-defi` Q6
`b` (« تتّسع » alors que l'énoncé pose un taux de subduction supérieur) et `c` (« ثابتة مهما كانت
المعدّلات »).

### Questions relues sans constat (06-safaih-taktuniya)

`quiz` Q2, Q3, Q5, Q6 · `01-tamrin` Q1, Q2, Q3, Q4, Q6 · `03-boss` Q1, Q2, Q5, Q6 · `04-defi` Q3,
Q4 · `05-tadrib` Q2, Q4 · `06-defi-concours` Q5, Q6.

**Verdict 06-safaih-taktuniya : à corriger avant publication** (6 MAJOR, dont un doublon que la
correction a elle-même créé). Aucune clé fausse.

---
## Dossier 5 — `07-ad-dawaran`

Relu : `quiz` et `01`…`06`, soit 36 questions touchées (avec leurs options non retouchées), et le
`cours.md`. Les calculs refaits sont justes : 80 × 0,6 = 48 ; 48 × 0,3 = 14,4 ; 48 × 0,7 = 33,6 ;
80 × 0,3 = 24 ; 9 % et 21 % de 42 donnent 3,78 et 8,82.
Résolution à l'aveugle : **aucune clé fausse**. Deux clés sont **inexactes à la lettre** (M07d-1,
M07d-2).

### MAJOR

**M07d-1 — `exercices/04-defi.json` Q4 — clé inexacte à la lettre.** La correction a écrit « أنّ
أكبر خزّان **ماء** يحيط بالخلايا مباشرة ». Or le plus grand réservoir d'eau est l'eau
**intracellulaire** (70 %, soit 29,4 kg), et la question 3 du même exercice vient de la calculer.
Ce qui est vrai, c'est que le liquide interstitiel dépasse le volume des vaisseaux.
- `b` (clé) ancien : `أنّ أكبر خزّان ماء يحيط بالخلايا مباشرة` → nouveau : `أنّ ما يحيط بالخلايا أكبر ممّا في الأوعية` (41 ; `c` = 45)

**M07d-2 — `quiz.json` Q9 — clé trop générale.** « لأنّ **الخلايا** أكبر من أن تعبر جدار الشّعيرة »
est faux pour les globules blancs : la lymphe en contient, et le cours ne lui retire que « الكريات
الحمراء والصّفيحات ». L'explication dit aussi « ويحبس الخلايا ».
- `b` (clé) ancien : `لأنّ الخلايا أكبر من أن تعبر جدار الشّعيرة` → nouveau : `لأنّ الكريات الحمراء أكبر من أن تعبر جدار الشّعيرة` (50 ; `c` = 51)
- dans l'explication, ancien : `ويحبس الخلايا.` → nouveau : `ويحبس الكريات الحمراء والصّفيحات.`

**M07d-3 — doublons de fait entre le quiz et les exercices.** La correction a rendu les distracteurs
encore plus proches :
- **`03-boss` Q2 ↔ `quiz` Q2** (« الشّريان الرّئويّ يحمل دمًا… » ; même clé ; distracteurs
  « مؤكسج لأنّه شريان » et « مختلط » dans les deux). Le même fait est aussi testé en
  `06-defi-concours` Q4. Réécriture de `03-boss` Q2 en 2×2, clé `b` :
  - prompt : `قارن تلميذ دم الشّريان الرّئويّ بدم الشّريان الأبهر. أيّ مقارنة صحيحة؟`
  - `a` : `كلاهما مؤكسج، لأنّهما شريانان يخرجان من القلب` (45) · `b` (clé) : `الأوّل محمّل بثنائي أكسيد الكربون، والثّاني مؤكسج` (49) · `c` : `الأوّل مؤكسج، والثّاني محمّل بثنائي أكسيد الكربون` (49) · `d` : `كلاهما محمّل بثنائي أكسيد الكربون` (33)
  - explication : `الشّريان الرّئويّ يخرج من البطين الأيمن بدم آتٍ من الأعضاء، محمّل بثنائي أكسيد الكربون، والأبهر يخرج من البطين الأيسر بدم عائد من الرّئتين، مؤكسج. فكلاهما شريان لأنّه يخرج من القلب، ومحتواهما مختلف: التّسمية بالاتّجاه لا بالمحتوى.`
- **`03-boss` Q4 ↔ `quiz` Q7** : l'énoncé est presque mot pour mot le même (« ما الصّفات/الخاصّيّات
  التي تجعل الشّعيرات الدّمويّة موضع/ملائمة للتّبادل؟ »), la clé aussi, et `a` est le même
  distracteur miroir. Réécriture de `03-boss` Q4, clé `b`, à partir de la question « vérifie » du
  cours :
  - prompt : `لماذا يكون الضّغط مرتفعًا في الشّريان وضعيفًا في الوريد، والدّم هو نفسه؟`
  - `a` : `لأنّ الوريد يحمل دمًا أقلّ من الشّريان` (38) · `b` (clé) : `لأنّ الدّم يعبر الشّعيرات قبل الوريد فيفقد دفعه` (47) · `c` : `لأنّ صمّامات الوريد تمتصّ ضغط الدّم` (35) · `d` : `لأنّ جدار الوريد الرّقيق يرشّح الدّم إلى الخارج` (47)
  - explication : `الشّريان يستقبل الدّم مباشرة من ضخّ البطين، والوريد يستقبله بعد أن عبر الشّعيرات، وهي بكثرتها ورقّتها تبدّد الضّغط. أمّا صمّامات الوريد فتمنع الرّجوع ولا تمتصّ الضّغط، ورقّة جداره نتيجة الضّغط الضّعيف لا سببه، والدّم الذي يعود في الأوردة هو نفسه الذي خرج في الشّرايين.`
- **`01-tamrin` Q4 ↔ `quiz` Q3** (« لماذا جدار البطين الأيسر أسمك/أكثر سمكًا…؟ », même clé,
  distracteurs « يستقبل دمًا أكثر » et « صمّامات » dans les deux). Réécriture de `01-tamrin` Q4 en
  2×2 d'identification, clé `b` :
  - prompt : `في مقطع عرضيّ لقلب، وُجد أحد البطينين أسمك جدارًا بكثير. أيّهما هو، وإلى أين يضخّ؟`
  - `a` : `الأيمن، ويضخّ إلى كافّة أعضاء الجسم` (35) · `b` (clé) : `الأيسر، ويضخّ إلى كافّة أعضاء الجسم` (35) · `c` : `الأيسر، ويضخّ إلى الرّئتين وحدهما` (33) · `d` : `الأيمن، ويضخّ إلى الرّئتين وحدهما` (33)
  - explication : `البطين الأيسر أسمك لأنّه يضخّ الدّم إلى كافّة أعضاء الجسم: المسافة أطول والمقاومة أكبر، فيلزم ضغط أعلى وعضلة أقوى. أمّا البطين الأيمن فيضخّ إلى الرّئتين وحدهما، وهما قريبتان.`

**M07d-4 — `exercices/03-boss.json` Q1 — la clé est l'option majoritaire à chaque étape.** La
correction a porté `c` et `d` à 80 caractères avec les mêmes maillons que la clé. Chaque position
du trajet est alors tranchée par le vote majoritaire : la clé reprend le début de `d` et le milieu de
`c`. On équilibre :
- `c` ancien : `الأذينة اليمنى ← الشّريان الرّئويّ ← الأسناخ ← الأوردة الرّئويّة ← البطين الأيسر` → nouveau : `البطين الأيمن ← الشّريان الرّئويّ ← الأسناخ ← الأوردة الرّئويّة ← الأذينة اليمنى` (80)
- `d` ancien : `البطين الأيمن ← الأوردة الرّئويّة ← الأسناخ ← الشّريان الرّئويّ ← الأذينة اليسرى` → nouveau : `البطين الأيسر ← الشّريان الرّئويّ ← الأسناخ ← الأوردة الرّئويّة ← الأذينة اليسرى` (80)
- Après correction : départ {الأيمن : b, c ; الأيسر : a, d} ; arrivée {اليسرى : b, d ; اليمنى : a,
  c}. La clé `b` (80) est à égalité avec `c` et `d`.
- explication nouvelle : `الدّورة الصّغرى تبدأ من البطين الأيمن وتنتهي في الأذينة اليسرى، مرورًا بالأسناخ حيث يُطرح ثنائي أكسيد الكربون ويُؤخذ الأكسيجين. فالشّريان الرّئويّ يخرج من البطين الأيمن لا الأيسر، والأوردة الرّئويّة تصبّ في الأذينة اليسرى لا اليمنى، والمسار من البطين الأيسر إلى الأبهر هو الدّورة الكبرى.`

### MINOR

**m07d-1 — explications où l'ajout recollé répète ce qui précède** (sans faute de sens) : `quiz` Q1
(« ويقع انغلاق … في بداية الانقباض البطينيّ »), `quiz` Q5, `01-tamrin` Q6, `02-tamrin` Q5, `03-boss`
Q5 (« وهذا الجدار لا يسمح بأيّ انتقال »), `04-defi` Q5, `05-tadrib` Q4. On peut les garder ;
supprimer de préférence celle de `03-boss` Q5, qui est purement redondante.

**m07d-2 — `exercices/05-tadrib.json` Q5 — distracteurs qui s'éliminent à vue** (antérieurs à la
correction). L'énoncé demande « من قواعد الوقاية », et `a` (« الإكثار من الملح ») comme `d`
(« الإكثار من الدّهنيّات الحيوانيّة ») sont des comportements à risque. Proposition : `a` →
`شرب الماء بكثرة بعد الأكل` (25), ce qui laisse `d` (32) au-dessus de la clé `b` (28). Ne pas
remplacer `d` par « الحدّ من الدّهنيّات الحيوانيّة » : dans le monde réel, ce conseil aide aussi
contre l'hypertension, et l'option deviendrait défendable.

**m07d-3 — `exercices/05-tadrib.json` Q6 — énoncé mal construit** (antérieur) : « التهاب الشّغاف
يستوجب التّعقيم الصّارم عند: » → `الوقاية من التهاب الشّغاف تستوجب التّعقيم الصّارم عند:`

**m07d-4 — `exercices/06-defi-concours.json` Q6 — `b` en partie défendable.** Dans le monde réel, le
tabac favorise aussi l'artériosclérose et la sédentarité élève la tension. La clé reste la seule
conforme au cours, mais un lecteur informé peut discuter `b`. À surveiller.

### Questions relues sans constat (07-ad-dawaran)

`quiz` Q2, Q5, Q7, Q10 · `01-tamrin` Q1, Q2 · `02-tamrin` Q1, Q2, Q6 · `03-boss` Q6 · `04-defi`
Q1, Q2, Q3, Q6 · `05-tadrib` Q1, Q2 · `06-defi-concours` Q1, Q2, Q3, Q4, Q5.

**Verdict 07-ad-dawaran : à corriger avant publication** (4 MAJOR, dont deux clés inexactes à la
lettre et trois doublons de fait). Aucune clé fausse.

---
## Dossier 6 — `07-annales-subur`

Relu : `quiz`, `01-sujet`, `02-sujet` et `03-defi`, soit 19 questions touchées (avec leurs options
non retouchées), et le `cours.md`. Ce chapitre de révision réutilise les savoirs des chapitres 01 à
06 de la série (qui le précèdent tous). Aucune notion n'y est donc « non encore enseignée ».
Résolution à l'aveugle : **aucune clé fausse ni ambiguë.**

### Les deux paires inter-chapitres signalées par `content:tranche` — tranchées

**P1 — `03-wiratha/03-boss` Q6 ↔ `07-annales-subur/01-sujet` Q2 (Jaccard 0,53) : doublon de fait,
à réécrire.** Même énoncé (« 44 صبغيًّا جسميًّا + XY »), même clé (« ذكر عدد صبغيّاته 46 »), et
`a` identique. Ce n'est pas un exercice parallèle : ce sont les mêmes données et la même lecture.
L'élève qui a fait le boss reconnaît la question, il ne la résout pas. On réécrit la question des
annales (`01-sujet` Q2, clé `b`) avec un autre document à lire :
- prompt : `وثيقة 2 (نمط نووي): صورة نمط نووي لخليّة تُظهر 22 صبغيًّا جسميًّا + صبغيًّا جنسيًّا واحدًا X. ما الاستنتاج؟`
- `a` : `خليّة جسمية لأنثى لأنّها تحمل X` (31) · `b` (clé) : `مشيج (بويضة أو نطفة) عدد صبغيّاته 23` (36) · `c` : `خليّة جسمية عدد صبغيّاتها 23` (28) · `d` : `نطفة حتمًا لأنّها تحمل صبغيًّا جنسيًّا واحدًا` (45)
- explication : `22 صبغيًّا جسميًّا + صبغيّ جنسيّ واحد = 23، وهو نصف عدد الخليّة الجسمية: فهي مشيج. والصبغيّ X يوجد في كلّ بويضة وفي نصف النطف، فلا نستطيع الجزم بأنّها نطفة. ولو كانت خليّة جسمية لكان فيها 46 صبغيًّا وزوج جنسيّ كامل (XX أو XY).`

**P2 — `03-wiratha/03-boss` Q4 ↔ `07-annales-subur/quiz` Q4 (Jaccard 0,47) : doublon de fait,
à réécrire.** L'énoncé est le même (« أبوان سليمان (ظاهريًّا) أنجبا طفلًا مصابًا بمرض وراثي
متنحٍّ »), la clé est la même, et deux distracteurs sont identiques (« un seul parent porteur » et
« acquis du milieu »). Le même fait figure **une troisième fois** dans le chapitre lui-même :
`02-sujet` Q3 (pédigrée, génotypes A//a). On garde `02-sujet` Q3, qui est bien une lecture de
document en notation, et on réécrit `quiz` Q4 (clé `b`) sur un autre croisement. Il se déduit du
cours, qui dit qu'un parent transmet son allèle à ses gamètes et que A domine a. Le calcul
25 % n'est **pas** enseigné, donc on ne l'invoque pas.
- prompt : `رجل مصاب بمرض وراثي متنحٍّ (a//a) تزوّج امرأة سليمة نقيّة (A//A). ما حال أطفالهما؟`
- `a` : `كلّهم مصابون مثل أبيهم a//a` (27) · `b` (clé) : `كلّهم سليمون وحاملون A//a` (25) · `c` : `نصفهم مصاب a//a ونصفهم سليم A//a` (32) · `d` : `كلّهم سليمون ونقيّون A//A` (25)
- explication : `الأب a//a لا يعطي أمشاجه إلّا a، والأمّ A//A لا تعطي إلّا A، فكلّ طفل A//a: سليم لأنّ A سائد، لكنّه حامل ينقل a إلى نصف أمشاجه. ولا يكون أحدهم a//a لأنّ الأمّ لا تحمل a، ولا A//A لأنّ الأب لا يحمل A.`
- Retirer les `misconceptionTag` des anciennes options.

(La troisième paire signalée, `08` quiz Q4 ↔ `02-tamrin` Q5, est tranchée au dossier 7.)

### MAJOR

**M07a-1 — `quiz.json` Q8 ↔ `02-sujet` Q5 : doublon de fait dans le chapitre, aggravé par la
correction.** Les deux énoncés comparent un volcan explosif et un volcan effusif. Les clés sont
devenues presque identiques (« لزوجة الصهارة وغناها بالغازات » / « … وكمّية غازاتها »), et les
distracteurs sont de même nature (couleur, hauteur, âge ou heure). L'énoncé du quiz dit en plus
« صهارة لزجة جدًّا », ce qui donne la clé. Réécriture de `quiz` Q8 (clé `a`) sur le **mécanisme** :
- prompt : `لماذا تنفجر الصهارة اللزجة بعنف بينما تنساب الصهارة السائلة بهدوء؟`
- `a` (clé) : `اللزجة تحبس غازاتها فيتراكم ضغطها` (33) · `b` : `اللزجة أسخن فتغلي غازاتها فجأة` (30) · `c` : `السائلة لا تحتوي على أيّ غازات` (30) · `d` : `اللزجة أثقل فتضغط على جدران المدخنة` (35)
- explication : `الصهارة اللزجة تحبس الغازات فيتراكم ضغطها حتّى ينفجر البركان، أمّا السائلة فتُفلت غازاتها بسهولة وهي تصعد. فالسائلة فيها غازات لكنّها تفلت، والانفجار لا يأتي من الحرارة ولا من ثقل الصهارة بل من الغاز المحبوس.`

**M07a-2 — la clé réunit la moitié de chaque distracteur** (la correction l'a créé) :
- **`quiz.json` Q3** : `c` devient « **أنثى** مصابة بالتثلّث الصبغي 21 » et `a` « ذكر **عدد صبغيّاته
  طبيعي** ». La clé « أنثى عدد صبغيّاتها طبيعي » est leur somme. De plus, `d` (« مشيج ») est
  contredit par « لخليّة جسمية ». On complète le 2×2 :
  - `d` ancien : `مشيج (خليّة تناسلية)` → nouveau : `ذكر مصاب بالتثلّث الصبغي 21` (27). Sexe {ذكر : a,
    d ; أنثى : b, c} × nombre {طبيعي : a, b ; تثلّث : c, d}. La clé `b` (24) n'est pas la plus longue.
  - explication, remplacer `والمشيج يحمل 23 صبغيًّا فقط لا 46.` par `والتثلّث يصيب الذكر والأنثى معًا، فالجنس وحده لا يكفي: لا بدّ من عدّ الصبغيّات.`
- **`03-defi.json` Q6** : `d` « **أنثى مصابة بالتثلّث 21**، سببه طفرة » + `a` « ذكر …، **خلل في عدد
  الصبغيّات** » donnent la clé `b`. On complète le 2×2 :
  - `c` ancien : `أنثى سليمة عدد صبغيّاتها طبيعي` → nouveau : `ذكر مصاب بالتثلّث 21، سببه طفرة في حليل واحد` (44). La clé `b` (44) est à égalité avec `c`, et `d` = 46.
  - explication, remplacer `والعدد 47 ليس طبيعيًّا، ` par rien. La phrase réfutait l'ancien `c`, qui
    disparaît. Le reste couvre déjà le sexe et la cause.

### MINOR

**m07a-1 — fuite inverse légère** :
- `02-sujet` Q1 : clé `a` (29) contre 38 / 42 / 43. `a` → `أنّ التلقيح يمنح الفأر ذاكرة مناعية تحميه` (41 ; `d` = 42, `b` = 43).
- `01-sujet` Q1 : clé `a` (18) contre 22 / 30 / 30. `a` → `تتثخّن بطانة الرحم تدريجيًّا` (28 ; `b` et `d` = 30).
- `03-defi` Q1 : clé « الإباضة » (7) contre 10 / 21 / 21. C'est un terme, et c'est acceptable en l'état.

**m07a-2 — distracteurs que l'énoncé élimine** : `02-sujet` Q6 `c` (« تُستهلَك عند الظهرة » alors
que l'énoncé dit que la croûte s'y forme) ; `quiz` Q4 `d` (« كلا الأبوين مصاب » alors que l'énoncé
les dit « سليمان ») disparaît avec la réécriture P2.

**m07a-3 — `03-defi.json` Q4 — ajout recollé en double** : « وهذه الصهارة هي التي تغذّي البراكين »
répète la première phrase. Garder seulement ` والزلزال لا يولّد البركان: الظاهرتان مظهران لسبب واحد.`

**m07a-4 — `quiz.json` Q2** : dans l'explication, « فبـ مقارنته » contient une espace fautive (défaut
antérieur) → `فبمقارنته`.

### Questions relues sans constat (07-annales-subur)

`quiz` Q2, Q6, Q7 · `01-sujet` Q3, Q6 · `02-sujet` Q2, Q5 (garde sa forme : c'est le quiz qui est
réécrit) · `03-defi` Q2, Q3, Q5.

**Verdict 07-annales-subur : à corriger avant publication** (2 doublons inter-chapitres à réécrire,
2 MAJOR). Aucune clé fausse.

---
## Dossier 7 — `08-at-tanaffus`

Relu : `quiz` et `01`…`06`, soit 37 questions touchées (avec leurs options non retouchées), et le
`cours.md`. Les calculs refaits sont justes : 196 m² = 196 000 000 mm², divisés par 700 000 000,
donnent 0,28 mm² ; les conversions 0,5 µm = 0,0005 mm, 0,05 µm = 0,00005 mm et 0,05 mm = 50 µm sont
exactes ; 21 − 16,4 = 4,6 ; 0,04 + 4,6 = 4,64 ; 18 ÷ 5 = 3,6.
Résolution à l'aveugle : **aucune clé fausse ni ambiguë.**

### La troisième paire signalée par `content:tranche` — tranchée

**P3 — `quiz` Q4 ↔ `02-tamrin` Q5 (Jaccard 0,48) : exercice parallèle voulu, à garder.** Le
correcteur a retourné `02-tamrin` Q5 : il donne maintenant la surface totale et demande celle d'un
alvéole. L'inconnue change, l'opération aussi (division avec conversion, au lieu d'une
multiplication), et les distracteurs aussi (oubli de conversion, erreurs d'un facteur dix). Le
savoir-faire est le même, avec d'autres données : c'est la définition d'un exercice parallèle. On
peut le justifier au rapport sans réécrire.

### MAJOR

**M08-1 — `exercices/05-tadrib.json` Q6 ↔ `quiz.json` Q10 : doublon de fait.** Même énoncé (« ما
الضّرر / ما الذي يفعله النّيكوتين … »), même clé (« يشلّ الأهداب »), et les trois mêmes
distracteurs (tumeurs, O₂ transporté, inflammation chronique). `quiz` Q10 a été retouché. De plus,
`05-tadrib` Q6 présente une fuite inverse forte : la clé fait 12 caractères contre 21 à 23 (rapport
0,57). Réécriture de `05-tadrib` Q6, clé `b`, sur un autre composant du tableau du cours :
- prompt : `أيّ مكوّن من دخان السّيجارة يتسبّب في التهاب مزمن للمسالك التنفّسيّة؟`
- `a` : `النّيكوتين` (10) · `b` (clé) : `أكسيد النّيتروجين` (17) · `c` : `القطران` (7) · `d` : `أحادي أكسيد الكربون` (19)
- explication : `أكسيد النّيتروجين يسبّب الالتهاب المزمن للمسالك التنفّسيّة. أمّا النّيكوتين فيشلّ الأهداب، والقطران يسبّب الأورام السّرطانيّة، وأحادي أكسيد الكربون يقلّص الأكسيجين المنقول إلى الخلايا.`

**M08-2 — `exercices/06-defi-concours.json` Q1 — distracteurs neufs que l'énoncé contredit, et clé
qui fait écho à l'énoncé.** L'énoncé dit « رئتاه سليمتان ». Or `d` (« جدار الأسناخ المتلف ») et
`b` (« الشّعيبات المنسدّة ») placent la panne dans le poumon. Trois options sur quatre disent
« أحادي أكسيد الكربون », et seule la clé reprend « لا في الرّئة ». On fait un 2×2 gaz × lieu de la
panne :
- `b` ancien : `ثنائي أكسيد الكربون؛ والعطب في الشّعيبات المنسدّة` → nouveau : `ثنائي أكسيد الكربون؛ والعطب في النّاقل لا في الرّئة` (51)
- `d` ancien : `أحادي أكسيد الكربون؛ والعطب في جدار الأسناخ المتلف` → nouveau : `ثنائي أكسيد الكربون؛ والعطب في الحجاب الحاجز المشلول` (52)
- `c` reste `أحادي أكسيد الكربون؛ والعطب في الحجاب الحاجز المشلول` (52). La clé `a` (51) est à
  égalité avec `b`.
- dans l'explication, ancien : `والرّئة والحجاب والشّعيبات سليمة.` → nouveau : `وثنائي أكسيد الكربون لا يحتلّ الهيموغلوبين على هذا النّحو، والحجاب الحاجز المشلول يوقف الحركات التنفّسيّة نفسها، وهي هنا قائمة.`

**M08-3 — `exercices/06-defi-concours.json` Q3 — trois distracteurs absurdes.** « رئته تصنع
الأكسيجين », « دمه لا يحتاج إلى أكسيجين » et « حجابه الحاجز لا يتحرّك فيوفّر الطّاقة » se
rejettent sans rien savoir. La correction les a allongés sans les rendre plausibles. On remplace les
deux premiers par des erreurs que le cours réfute :
- `b` ancien : `لأنّ رئته تصنع الأكسيجين الذي تحتاجه عضلاته` → nouveau : `لأنّ دمه يحمل أكسيجينًا ذائبًا في البلازما أكثر` (47).
  Le cours dit : « أقلّ من 1 % إلى 1,5 % ».
- `c` ancien : `لأنّ دمه لا يحتاج إلى أكسيجين أثناء المجهود` → nouveau : `لأنّ إيقاعه التنفّسيّ في الرّاحة أسرع من غيره` (45)
- La clé `a` (38) n'est pas la plus longue.
- Explication, ajouter : ` أمّا الأكسيجين الذّائب في البلازما فضئيل عند الجميع، وإسراع الإيقاع لا يصنع سعة.`

### MINOR

**m08-1 — langue** : `03-boss` Q4, ajout à l'explication. `والقيمتان 20 و60 و50 قيم نهائيّة أو أوّليّة` (un duel suivi de trois valeurs) → `والقيم 20 و60 و50 قيم نهائيّة أو أوّليّة`.

**m08-2 — ajouts recollés redondants** : `04-defi` Q1 (« ويسمّى هذا المركّب الأكسي هيموغلوبين »,
déjà dit dans la première phrase) → supprimer ; `quiz` Q2 et `05-tadrib` Q5 : la dernière phrase
répète la précédente, mais elle reste utile.

**m08-3 — distracteurs que l'énoncé élimine** (défauts antérieurs) : `05-tadrib` Q5 (les trois
distracteurs sont des comportements nocifs, alors qu'on demande des « قواعد حفظ الصّحّة ») ;
`06-defi-concours` Q4 `b` (« تُجمع أضرارها », alors que l'énoncé dit « لا مجرّد مجموع ») ;
`06-defi-concours` Q5 `d` (« كلاهما في القفص الصّدريّ »).

**m08-4 — paires proches dans le chapitre, à surveiller** : `quiz` Q2 ↔ `02-tamrin` Q2 (les
anneaux de la trachée ; la version `02-tamrin` est en deux parties, plus riche) ; `quiz` Q6 ↔
`04-defi` Q1 (le transport de l'O₂) ; `quiz` Q5 ↔ `03-boss` Q1 (l'azote à 79 %, même énoncé mais
autre question : le sens / l'usage comme témoin). La correction a recopié en `03-boss` `c` le
distracteur `b` du quiz (« يُستهلك ويُعوَّض »).

**m08-5 — fuite inverse légère** : `04-defi` Q3 (clé « الجليكوز والأكسيجين », 19, contre 24 / 26 /
30). Si on l'allonge, elle devient la plus longue : on la laisse.

### Questions relues sans constat (08-at-tanaffus)

`quiz` Q2, Q3, Q5, Q6, Q7, Q8, Q9 · `01-tamrin` Q2, Q3, Q5, Q6 · `02-tamrin` Q2, Q4, Q5, Q6 ·
`03-boss` Q1, Q2, Q3, Q5, Q6 · `04-defi` Q1, Q2, Q3, Q4, Q5, Q6 · `05-tadrib` Q1, Q2, Q3 ·
`06-defi-concours` Q2, Q4, Q5, Q6.

**Verdict 08-at-tanaffus : à corriger avant publication** (3 MAJOR). Aucune clé fausse.

---

## Synthèse

- **Clés fausses : aucune** sur les 225 questions touchées des sept dossiers. **Clés inexactes à la
  lettre : 2**, toutes deux en `07-ad-dawaran` : `04-defi` Q4 (« أكبر خزّان ماء ») et `quiz` Q9
  (« الخلايا » au lieu de « الكريات الحمراء »). Une **explication dit le faux** : `06-dirasat-ad-dam`
  `04-defi` Q4 (le « فهي » recollé envoie les nutriments au rein).
- **Fuite longue** : 0/342. **Fuite inverse** : 34/298 (11 %, sous le hasard). Sept cas marqués,
  traités dans les dossiers.
- **Défaut dominant de cette tranche** : la **clé qui réunit la moitié de chaque distracteur**,
  souvent créée par la correction elle-même quand elle allonge un distracteur avec un morceau de la
  clé. On l'a relevé dans `05-al-hadm` `05-tadrib` Q1, `06-dirasat` `05-tadrib` Q1, `03-boss` Q5 et
  Q6 et `04-defi` Q5, `07-ad-dawaran` `03-boss` Q1, et `07-annales` `quiz` Q3 et `03-defi` Q6.
  Le remède est le **2×2 exact**, chaque élément apparaissant deux fois.
- **Second défaut** : les **doublons de fait** entre le `quiz` et les exercices (`03-boss`,
  `05-tadrib`). La correction en a aggravé plusieurs en recopiant un distracteur de l'un dans
  l'autre, et en a créé un (`06-safaih` `05-tadrib` Q5). Pour chacun, une réécriture complète est
  fournie, avec la clé au même identifiant.
- **Paires `content:tranche`** : P1 (`03-wiratha` boss Q6 ↔ annales `01-sujet` Q2) et P2 (`03-wiratha`
  boss Q4 ↔ annales `quiz` Q4) sont des **doublons à réécrire** (réécritures fournies). P3 (`08`
  `quiz` Q4 ↔ `02-tamrin` Q5) est un **exercice parallèle voulu, à garder**.
- **Termes** : « الوشاح » et « المتحجّرات » sont conformes au cours de `06-safaih`. Mais
  « الوشاح », « النواة » et « الليثوسفير » apparaissent en `05-barakin` `05-tadrib` Q2, **un chapitre
  avant** leur enseignement (M05b-3).

| Dossier | BLOCKER | MAJOR | Verdict |
| --- | --- | --- | --- |
| 05-al-hadm | 0 | 2 | à corriger |
| 05-barakin | 0 | 6 | à corriger |
| 06-dirasat-ad-dam | 0 | 5 | à corriger |
| 06-safaih-taktuniya | 0 | 6 | à corriger |
| 07-ad-dawaran | 0 | 4 (dont 2 clés inexactes) | à corriger |
| 07-annales-subur | 0 | 2 + 2 paires à réécrire | à corriger |
| 08-at-tanaffus | 0 | 3 | à corriger |
