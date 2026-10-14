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

Relu : `quiz` et les exercices `01`…`06`, soit 40 questions touchées, avec leurs options non
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
