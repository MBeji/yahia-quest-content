# Audit indépendant — correction « clé la plus longue », SVT 9ᵉ, chapitres 12 · 13 · 14

> Mandat : `.claude/skills/content-engine/references/audit-correction.md`, appliqué à la lettre.
> Corpus relu : `/home/user/wt-svtkey` (branche `wip/svt-9eme-cle-longue`), diff
> `git diff origin/main -- content/sciences-vie-terre/<CHAPITRE>` après `fetch origin main`.
> Référence : `cours.md` de chaque chapitre + manuel 105905 (cache). Hors périmètre :
> `12-…/exercices/07…10-examen-*`. L'auditeur n'a modifié aucun fichier du corpus.
> Indices de questions : 1-based. Longueurs en caractères (Python `len`) ; toutes les
> corrections proposées ont été vérifiées : la clé n'y redevient pas strictement la plus longue.

## Chapitre 12 — `12-takawwun-al-janin`

Résolution à l'aveugle : **aucune clé fausse, aucune clé ambiguë** sur les 36 questions modifiées.
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

