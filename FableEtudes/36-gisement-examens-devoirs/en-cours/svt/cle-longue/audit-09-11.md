# Audit indépendant — correction « clé la plus longue », SVT 9ᵉ, chapitres 09 · 10 · 11

> Mandat : `.claude/skills/content-engine/references/audit-correction.md`, appliqué à la lettre.
> Corpus relu : `/home/user/wt-svtkey` (branche `wip/svt-9eme-cle-longue`, HEAD `dab0eaf9`), diff
> `git diff origin/main -- content/sciences-vie-terre/<CHAPITRE>` après `fetch origin main`.
> Référence : `cours.md` de chaque chapitre, et le manuel 105905 en cas de doute. Hors périmètre :
> `exercices/07…09-examen-*`. L'auditeur n'a modifié aucun fichier du corpus.
> Indices de questions : 1-based. Longueurs en caractères (Python `len`). Pour chaque correction
> proposée, on a vérifié que la clé ne redevient pas strictement la plus longue.

## Mesure de la « fuite inverse » (la clé désormais strictement la plus courte)

Périmètre : quiz + `exercices/01…06`, soit 46 questions QCM par chapitre.

| Chapitre | clé strictement la plus longue (main → branche) | clé strictement la plus courte (main → branche) |
| -------- | ----------------------------------------------- | ----------------------------------------------- |
| 09       | 33 → 0                                          | 4 (9 %) → 8 (17 %)                              |
| 10       | 33 → 0                                          | 2 (4 %) → 6 (13 %)                              |
| 11       | 30 → 0                                          | 1 (2 %) → 2 (4 %)                               |

Ces taux restent **sous le hasard**, qui est de 25 % pour quatre options. Les écarts sont faibles
(1 à 3 caractères), et quatre des cas sont des clés nues préexistantes (`0`, `الكبد`, `الحويض`, des
chiffres). On ne relève donc **pas de fuite inverse** : rien à corriger à ce titre.

## Chapitre 09 — `09-al-ikhraj`

Résolution à l'aveugle des 39 questions modifiées et des options non retouchées : **aucune clé
fausse**. En revanche, **une clé est ambiguë** (06 Q2, le point d qu'avait signalé le correcteur).
On relève aussi deux clés raccourcies qui ne répondent plus à tout l'énoncé, une clé qui porte un
indice de forme et deux distracteurs que l'énoncé élimine.

Les trois énoncés modifiés ont été vérifiés :

- **01-tamrin Q2** : le nouvel énoncé correspond aux options. Les distracteurs sont bien choisis,
  en particulier le remplacement de « الجلد », qui était défendable.
- **02-tamrin Q3** : la clé `a` est exacte (6 → 6 → 10, ce qui donne une réabsorption partielle,
  conforme au cours) et l'explication est juste. La question ne fait plus doublon avec le glucose
  du quiz Q4.
- **03-boss Q3** : 60 × 60 × 24 = 86 400 mL, soit 86,4 L. La clé `c` est exacte et le distracteur
  `a` (3,6 L) correspond bien à l'oubli décrit dans l'explication.

### BLOCKER

**B09-1 — `exercices/06-defi-concours.json` Q2, `d` « لا يمكن الحكم » : le distracteur est défendable, donc la clé est ambiguë** (point signalé, tranché).
L'énoncé dit « شخص » et non « إنسان عاديّ ». Pour l'élève, avec trois heures de données, « on ne
peut pas juger » est une réponse rigoureuse. L'explication elle-même l'écrit : « فمقارنةُ نافذة من
ثلاث ساعات … لا تصلح حكمًا على التّوازن ». Elle donne ainsi raison à `d` contre la clé `b`.
On corrige l'énoncé (la personne est saine, comme le « إنسان عاديّ » du cours), le distracteur et
la phrase de l'explication.

- prompt ancien : `شخص شرب 1,5 لتر ماء، ففقد 1,6 لتر في 3 ساعات. هل اختلّ توازنه المائيّ؟`
- prompt nouveau : `شخص سليم شرب 1,5 لتر ماء، ففقد 1,6 لتر في 3 ساعات. هل اختلّ توازنه المائيّ؟`
- `d` ancien : `لا يمكن الحكم` (13)
- `d` nouveau : `نعم: كلّ فقدان يفوق الشّرب يعني جفافًا` (38 ; clé `b` = 48 = `c`)
- explication, remplacer `فمقارنةُ نافذة من ثلاث ساعات بمدخول واحد لا تصلح حكمًا على التّوازن.` par
  `فمقارنةُ نافذة من ثلاث ساعات بمدخول واحد لا تدلّ على اختلال: هذا ما يقع عند كلّ إنسان سليم.`

### MAJOR

**M09-1 — `exercices/04-defi.json` Q5, clé `b` : la clé ne répond plus à tout l'énoncé.**
L'énoncé demande pourquoi on ajoute « أملاح معدنيّة **وجليكوز** ». La clé raccourcie ne parle plus que
des sels. Le glucose n'apparaît que dans l'explication : c'est le même schéma que M12-4. On rallonge
aussi `a`, sans quoi la clé deviendrait strictement la plus longue.

- `b` ancien : `لأنّ العرق يُخرج أملاحًا لا يعوّضها الماء` (41)
- `b` nouveau : `لأنّ العرق يُخرج أملاحًا والجري يستهلك الجليكوز` (47)
- `a` ancien : `لأنّ طعم الماء المملّح أطيب عند الجري` (37)
- `a` nouveau : `لأنّ الماء المملّح والمحلّى أطيب طعمًا عند الجري` (48)
- explication, remplacer la phrase finale `والجليكوز يعوّض الطّاقة المنفقة.` par
  `والماء الصّافي لا يعوّض أملاح العرق، والجليكوز يعوّض الطّاقة التي أنفقتها العضلات.`

**M09-2 — `exercices/06-defi-concours.json` Q4, clé `b` : la clé ne répond plus à la comparaison demandée.**
L'énoncé demande de comparer la filtration glomérulaire à l'absorption dans l'intestin grêle (« قارن …
أين الفرق الجوهريّ؟ »). La clé raccourcie ne décrit plus que la filtration ; l'intestin n'apparaît que
dans l'explication. Seul `c` parle encore des deux termes de la comparaison.

- `b` ancien : `الترشيح أعمى يفرز بالحجم؛ والانتقاء يأتي بعده` (45)
- `b` nouveau : `الترشيح أعمى يفرز بالحجم، والامتصاص يمرّر نواتج الهضم` (53)
- `c` ancien : `الترشيح ينتقي النّافع، والامتصاص المعويّ أعمى` (45)
- `c` nouveau : `الترشيح ينتقي النّافع، والامتصاص المعويّ أعمى يمرّر كلّ شيء` (59)
- explication : il n'y a rien à changer. Elle dit déjà « والانتقاء يأتي بعده » (retiré de la clé) et
  « الامتصاص المعويّ فيمرّر نواتج الهضم النّافعة ».

**M09-3 — `exercices/06-defi-concours.json` Q3, clé `a` : indice de forme.**
La clé est la seule option qui contienne une parenthèse (« (قرابة المليون) »). De plus, « العدد الهائل
يعوّض » est impropre : ce ne sont pas les nombres qui compensent, mais les néphrons restants.

- `a` ancien : `لأنّ العدد الهائل (قرابة المليون) يعوّض ما تلف` (46)
- `a` nouveau : `لأنّ النّيفرونات الباقية كثيرة فتعوّض ما تلف` (44 ; `b` = 47, `c` = 48)
- explication, compléter la dernière phrase : `فالباقي من النّيفرونات — وأصلها قرابة المليون في كلّ كلية — يعوّض التّالف حتّى تتجاوز الخسارة احتياطًا كبيرًا.`

**M09-4 — `exercices/03-boss.json` Q2 : `b` et `c` réécrits restent éliminés par la prémisse.**
L'énoncé pose que le rein « تطبّق عتبة لا تتّخذ قرارًا ». Or `b` (« تغيّر ما تُعيده بحسب رغبة
الجسم ») et `c` (« تتلقّى أمرًا من المخّ ») décrivent justement une décision : l'élève les écarte
sans rien savoir. On les remplace par deux règles fixes, qui répondent donc à la question, mais qui
sont fausses d'après le tableau du cours (7 → 10, 10 → 13).

- `b` ancien : `لأنّها تغيّر ما تُعيده بحسب رغبة الجسم` (38)
- `b` nouveau : `لأنّها تُعيد امتصاص الملح كلّه في كلّ حالة` (42)
- `c` ancien : `لأنّها تتلقّى أمرًا من المخّ في كلّ حالة` (40)
- `c` nouveau : `لأنّها تطرح كلّ الملح متى تجاوز تركيزه 7 غ/ل` (44 ; clé `a` = 36)
- explication, ajouter à la fin : ` وهي لا تسترجع الملح كلّه دائمًا (7 يعطي 10 في البول)، ولا تطرح كلّه فوق العتبة: تطرح الفائض وحده.`

### MINOR

**m09-1 — `exercices/01-tamrin.json` Q1, clé `a` : graphie.** Il manque la shadda de « السّامّة »
(c'est l'adjectif سامّ). La même faute figure dans la définition de `cours.md` (« الزّائدة
و**السّامة** »).
- `a` ancien : `طرح المواد الزّائدة والسّامة` → nouveau : `طرح المواد الزّائدة والسّامّة` (29 ; `b` = 32)

**m09-2 — `exercices/01-tamrin.json` Q2, `d` : forme hétérogène.** Les trois autres options
séparent les organes par « · », alors que `d` les relie par « و ». Ce n'est pas un indice vers la
clé, mais `d` se signale à l'œil.
- `d` ancien : `الكليتان والمثانة والحالبان والإحليل` → nouveau : `الكليتان · المثانة · الحالبان · الإحليل` (39)

**m09-3 — `exercices/01-tamrin.json` Q3 : l'explication ne réfute pas `c`.** La règle « كلّ ترتيب يضع
المثانة قبل الحالب » écarte `a` et `d`, mais pas `c`, où le إحليل est placé avant le حالب. Ajouter :
` ووضع الإحليل قبل الحالب يجعل البول يخرج قبل أن يُنقل إلى المثانة.`

**m09-4 — `exercices/06-defi-concours.json` Q6, `b` et `d` (préexistants, non retouchés sur le
fond) : contredits par l'énoncé.** `b` (« الخلل في الكبيبات ») heurte « كليتاه سليمتان بالتّصوير ».
`d` (« لا خلل: القيمة عاديّة ») heurte « أقلّ من 400 مل », qui est le signe du cours. À reprendre lors
d'un passage de qualité.

**m09-5 — paires de même fait entre le quiz et les exercices** (préexistantes, non touchées).
Ce ne sont pas des doublons au sens du mandat : les fichiers diffèrent et les options aussi. Elles
sont à surveiller :
- `quiz` Q2 ↔ `02-tamrin` Q2 (protéines 80 → 0) ;
- `quiz` Q3 ↔ `02-tamrin` Q4 (ammoniac 0/0/0,5) ;
- `quiz` Q5 ↔ `02-tamrin` Q5 (urée ×67) ;
- `quiz` Q10 ↔ `04-defi` Q6 (dialyse).

### Questions relues sans constat (ch. 09)

`quiz` Q1, Q4, Q6, Q10 · `01-tamrin` Q2 (énoncé), Q4, Q5 · `02-tamrin` Q1, Q2, Q3, Q4, Q6 ·
`03-boss` Q3, Q6 · `04-defi` Q1, Q2, Q3, Q4, Q6 · `05-tadrib` Q2, Q4, Q5, Q6 · `06-defi-concours` Q1, Q5.

**Verdict ch. 09 : à corriger avant publication.** 1 BLOCKER (clé ambiguë, préexistante), 4 MAJOR.
Aucune clé fausse.

## Chapitre 10 — `10-an-nudj-al-jinsi`

Résolution à l'aveugle des 37 questions modifiées et des options non retouchées : **aucune clé
fausse, aucune clé ambiguë**. Les défauts relevés sont un indice de forme, des distracteurs que
l'élève élimine à vue (dont certains créés par l'ajout de chiffres) et des phrases d'explication
mal raccordées.

### MAJOR

**M10-1 — `exercices/03-boss.json` Q5 : indice de forme, et un distracteur que l'énoncé élimine.**
- La clé `b` (« هو بلوغ مبكّر (9-10 عند الفتيان) لا حالة شاذّة ») est la seule option qui porte une
  parenthèse et des chiffres. C'est aussi la seule qui ne commence ni par « نعم » ni par « لا ».
- `a` (« … وغير ممكن عند الفتيان أبدًا ») est démenti par l'énoncé lui-même, puisque le garçon *a*
  atteint la puberté à 9 ans.

On harmonise les quatre options sur un même gabarit, chacune avec une réponse et une plage d'âges ;
les plages des distracteurs sont fausses.
- `a` ancien : `نعم، هو خارج المألوف وغير ممكن عند الفتيان أبدًا` → nouveau : `نعم: هو بلوغ شاذّ، فالمبكّر عند الفتيان من 11 إلى 12` (52)
- `b` ancien : `هو بلوغ مبكّر (9-10 عند الفتيان) لا حالة شاذّة` → nouveau : `لا: هو بلوغ مبكّر، ومجاله عند الفتيان من 9 إلى 10` (49)
- `c` ancien : `لا، هو بلوغ متوسّط عاديّ عند الفتيان` → nouveau : `لا: هو بلوغ متوسّط، ومجاله عند الفتيان من 9 إلى 12` (50)
- `d` ancien : `نعم، هو حالة شاذّة تستدعي العلاج فورًا` → nouveau : `نعم: هو حالة شاذّة، فلا بلوغ عند الفتيان قبل 13` (47)
- explication : supprimer la phrase finale redondante `ومجال البلوغ المبكّر معروف.` et ajouter
  ` و13 سنّ البداية المعتادة لا حدّ أدنى لا يُتجاوز.`

**M10-2 — `exercices/03-boss.json` Q6 : les chiffres ajoutés font que deux distracteurs se réfutent eux-mêmes.**
`b` (« متوسّط، والمجال المعتمد من 10,5 إلى 14 ») affiche une plage qui exclut 17, l'âge donné par
l'énoncé. `a` (« بلوغ مبكّر، والحدّ المعتمد قبل 9 ») est réfuté par l'énoncé : la jeune fille n'est
« pas encore pubère », elle ne peut donc pas l'être de façon précoce. Il ne reste en réalité que `c`
et `d`. On remplace `a` et `b` par des seuils faux mais compatibles avec 17.
- `a` ancien : `بلوغ مبكّر، والحدّ المعتمد قبل 9` → nouveau : `حالة عاديّة، والحدّ المعتمد للتّأخّر بعد 19` (43)
- `b` ancien : `متوسّط، والمجال المعتمد من 10,5 إلى 14` → nouveau : `متوسّط، والمجال المعتمد من 13 إلى 18` (36 ; clé `c` = 34)
- explication : rien à changer, elle donne déjà les plages exactes (10,5-14 ; avant 9 ; après 17).

### MINOR

**m10-1 — doublon de fait `quiz` Q4 ↔ `exercices/01-tamrin` Q6 (signalé par le correcteur, tranché : vrai doublon).**
L'énoncé est le même (« أين يتمّ إلقاح البويضة » / « أين يقع الإلقاح ») et la clé aussi, mot pour mot
(`في قناة البيض`). Seuls les distracteurs diffèrent. Comme les fichiers sont distincts, le constat
reste MINOR, mais l'élève rencontre deux fois la même question. On réécrit l'énoncé de l'exercice en
situation ; les options restent inchangées et la clé reste `b`.
- prompt ancien : `أين يقع الإلقاح؟`
- prompt nouveau : `تحرّرت بويضة والتقطها قمع فالوب، ودخلت حيوانات منويّة المسالك الأنثويّة. أين يلتقيان فيقع الإلقاح؟`
- les options restent telles quelles (`a` في تجويف الرّحم · `b`* في قناة البيض · `c` في جريب المبيض · `d` في أعلى المهبل).
- explication, remplacer le début `في قناة البيض.` par `يلتقيان في قناة البيض: القمع يسلّم البويضة إلى القناة، والحيوانات المنويّة تصعد إليها.`

**m10-2 — `exercices/02-tamrin.json` Q5 : l'ajout répète l'explication.** La phrase finale
`وتنقلها تقلّصات القناة.` redit ce que la première phrase affirme déjà (« وتنقلها تقلّصات القناة نحو
الرّحم »). La supprimer.

**m10-3 — `exercices/04-defi.json` Q5 : l'explication se termine par une proposition qui n'a pas de
phrase principale.** Le segment `لأنّ الخصيتين تؤدّيان دورين: إنتاج الأمشاج وإفراز الهرمون.` commence
par « لأنّ » après un point et répète la première phrase. Le supprimer.

**m10-4 — `exercices/06-defi-concours.json` Q3 : le sujet de l'ajout est indéterminé.** Dans
`فينتظر البويضة التي تعيش 24 ساعة.`, le verbe au masculin suit « فترة الخصوبة ».
→ `فالحيوان المنويّ الموجود قبل الإباضة ينتظر البويضة التي لا تعيش إلّا 24 ساعة.`
Hors correction, une question reste ouverte : l'énoncé dit « ويومين بعدها » alors que l'ovule vit
24 heures. Ce point préexistant est à vérifier dans le manuel lors d'un passage de qualité.

**m10-5 — `exercices/06-defi-concours.json` Q2 : l'ajout est mal raccordé.** Dans `ويمكن أن تظهر دون
أن ينشط إنتاج الأمشاج.`, le sujet sous-entendu est « الصّفات », alors que le dernier nom cité est
« عضو واحد ». → `فالصّفات الثّانويّة يمكن أن تظهر دون أن ينشط إنتاج الأمشاج.`

**m10-6 — `exercices/01-tamrin.json` Q1 : l'ajout est mal raccordé.** Dans `وهو قادر على الإنجاب عند
اكتماله.`, « هو » renvoie au البلوغ, qui ne peut pas être « قادر على الإنجاب ».
→ `ويصير الجسم عند اكتماله قادرًا على الإنجاب.`

**m10-7 — `exercices/05-tadrib.json` Q2 : du remplissage a été ajouté aux distracteurs.**
« الخصيتان التّناسليّتان » est un pléonasme. « الإحليل البوليّ » est inexact chez l'homme, où le
cours le décrit comme « تناسليّة بوليّة ».
- `a` → `الخصيتان والبربخان الملتفّان` (28 ; clé `b` = 32)
- `d` → `القناتان المنويّتان والإحليل المشترك` (36)

**m10-8 — paires de même fait entre le quiz et les exercices** (préexistantes, distracteurs
différents) : `quiz` Q8 ↔ `04-defi` Q6 (nombre de gamètes) ; `quiz` Q10 ↔ `01-tamrin` Q5 ↔ `04-defi`
Q5 (double rôle de la gonade). À surveiller, sans action requise.

### Questions relues sans constat (ch. 10)

`quiz` Q2, Q5, Q7, Q8, Q9, Q10 · `01-tamrin` Q3, Q5 · `02-tamrin` Q2, Q6 · `03-boss` Q4 ·
`04-defi` Q1, Q2, Q3, Q6 · `05-tadrib` Q1, Q3, Q5, Q6 · `06-defi-concours` Q1, Q4, Q5, Q6.

**Verdict ch. 10 : publiable après les 2 MAJOR.** Aucun BLOCKER, aucune clé fausse. Les MINOR
d'explication sont à appliquer dans le même passage, car ils ne coûtent rien.

## Chapitre 11 — `11-ad-dawra-al-jinsiya`

Résolution à l'aveugle des 37 questions modifiées et des options non retouchées : **aucune clé
fausse, aucune clé ambiguë**. Restent deux vrais doublons de fait à réécrire, plus un troisième
(un énoncé identique), une explication que l'ajout rend fausse, une étiquette devenue inexacte et
des distracteurs triviaux.

### Doublons signalés par le correcteur — décisions

| Paire | Décision | Motif |
| ----- | -------- | ----- |
| `quiz` Q5 ↔ `04-defi` Q2 | **vrai doublon → réécrire le quiz** | Même expérience (ablation de l'utérus), même conclusion, mêmes distracteurs en substance (« متبادلة », « الرّحم يقود »). Le quiz Q5 tire en outre de cette seule expérience une conclusion qui exige aussi l'expérience 2 (son explication l'admet). |
| `quiz` Q6 ↔ `04-defi` Q3 | **paire proche, à garder** | Même greffe, mais la question diffère : « ماذا يثبت » (le transport par le sang) contre « لماذا هي الحاسمة » (seul lien restant). Les distracteurs n'ont rien en commun. |
| `quiz` Q7 ↔ `04-defi` Q4 | **vrai doublon → réécrire le quiz** | Même injection quotidienne, même question (« ما الاستنتاج » / « ماذا يثبت »), même clé (« الدّوريّة من الإفراز »), distracteurs équivalents (« يضرّ », « لا يعوّض / لا يعمل », « دوريّة ذاتيّة »). |
| `quiz` Q10 ↔ `02-tamrin` Q3 | **vrai doublon → réécrire le quiz** | Énoncé quasi identique (« لماذا يُقاس/تُقاس … كلّ صباح قبل النّهوض »), clé de même sens. |

On réécrit le quiz plutôt que `04-defi` (« خمس تجارب », une suite qui a besoin de chaque expérience)
et plutôt que `02-tamrin` (exercice consacré à la courbe). Chaque réécriture garde l'identifiant de
la clé et les étiquettes aux mêmes identifiants.

### MAJOR

**M11-1 — `quiz.json` Q5 : réécriture complète (doublon de `04-defi` Q2). La clé reste `b`.** On passe
de la souris à une application chez la femme, qui combine l'expérience 3 et l'origine du sang des
règles.
- prompt : `امرأة استُؤصل رحمها لسبب صحّيّ وبقي مبيضاها سليمين. ماذا يحدث لإباضتها ولحيضها؟`
- `a` : `تتوقّف الإباضة والحيض معًا كما بعد سنّ الخصوبة` (46)
- `b`* : `تتواصل الإباضة دوريًّا، ولا ينزل حيض لغياب الرّحم` (49)
- `c` : `تتوقّف الإباضة لأنّ الرّحم هو الذي ينظّم المبيضين` (49 ; étiquette `bio.cycle.uterus-autonome` conservée)
- `d` : `تتواصل الإباضة ويستمرّ الحيض لأنّ دمه من المبيض` (47)
- explication : `المبيض لا يتبع الرّحم: نزعُ الرّحم لا يؤثّر في نشاط المبيضين (التّجربة 3)، فتتواصل الإباضة. أمّا الحيض فتهدّمُ بطانة الرّحم ودمُه دمها، فلا حيض بلا رحم. ولو كان الرّحم هو الذي ينظّم المبيض لتوقّفت الإباضة.`

**M11-2 — `quiz.json` Q7 : réécriture complète (doublon de `04-defi` Q4). La clé reste `a`.** Elle
porte sur l'observation clinique du cours (l'âge après la fertilité).
- prompt : `في سنّ ما بعد الخصوبة يتوقّف النّشاط الدّوريّ للمبيض نهائيًّا، فينقطع الحيض. كيف تفسّر انقطاعه؟`
- `a`* : `لأنّ الرّحم لم يعد يتلقّى إفرازًا دوريًّا من المبيض` (51)
- `b` : `لأنّ دم الحيض كان يأتي من المبيض فتوقّف بتوقّفه` (47)
- `c` : `لأنّ بطانة الرّحم تفقد مع السنّ دوريّتها الخاصّة بها` (52 ; étiquette `bio.cycle.uterus-autonome` conservée)
- `d` : `لأنّ قناتَي البيض تنسدّان فلا تصل البويضة إلى الرّحم` (51)
- explication : `في التّجربة 2 أدّى نزع المبيضين إلى ضمور البطانة، وفي سنّ ما بعد الخصوبة يحدث الشّيء نفسه طبيعيًّا: لا إفراز دوريّ، فلا بناء للبطانة ولا تهدّم، فلا حيض. ودم الحيض دم البطانة لا دم المبيض، والرّحم لا يملك دوريّة خاصّة به (التّجربة 5).`

**M11-3 — `quiz.json` Q10 : réécriture complète (doublon de `02-tamrin` Q3). La clé reste `c`.** La
question devient une lecture de mesure. Les options sont en deux paires « صالحة / غير صالحة », pour
qu'aucune ne se distingue par sa forme.
- prompt : `قاست امرأة حرارتها بعد الفطور والمشي، فوجدتها 37,2 في الطّور الجريبي. كيف تقرأ هذه القيمة؟`
- `a` : `قيمة صالحة: الإباضة وقعت في ذلك اليوم` (37)
- `b` : `قيمة صالحة: المرأة حامل منذ بداية الدّورة` (41)
- `c`* : `قيمة غير صالحة: النّشاط والأكل رفعا الحرارة` (43)
- `d` : `قيمة غير صالحة: الحرارة لا تُقاس إلّا مساءً` (43)
- explication : `القفزة المنتظرة عند الإباضة نحو نصف درجة فقط، والنّشاط البدنيّ والأكل يرفعان الحرارة بقدر يماثلها؛ فقيمة أُخذت بعد الفطور والمشي لا تُقرأ على المنحنى. ولهذا تُقاس الحرارة كلّ صباح قبل النّهوض، لا في المساء ولا بعد النّشاط.`

**M11-4 — `exercices/02-tamrin.json` Q6 : l'ajout attribue la reconstruction à la mauvaise phase.**
La phrase ajoutée `ففيه يُعاد بناء الغشاء المخاطيّ …` suit immédiatement la phrase sur « طور ما قبل
الحيض ». Le « فيه » se lit donc comme le طور ما قبل الحيض, ce qui contredit à la fois la clé et le
cours. On réordonne l'explication :
- explication nouvelle : `إعادة بناء بعد الهدم: في هذا الطّور، الممتدّ من نهاية الحيض إلى الإباضة، يُعاد بناء الغشاء المخاطيّ ويزداد سمكه وتتطوّر الغدد الأنبوبيّة. أمّا الشّبيك الرّحمي بغدده الملتوية وأوعيته الكثيفة فيتكوّن في طور ما قبل الحيض، أي بعد الإباضة.`

### MINOR

**m11-1 — `exercices/04-defi.json` Q1, `c` : l'étiquette est devenue inexacte.** Le nouveau texte
(« أنّ المبيضين يغذّيان الرّحم بالدّم مباشرة ») ne correspond plus à l'idée fausse
`bio.cycle.uterus-autonome`, que portait l'ancien « البطانة تعمل وحدها ». Retirer l'étiquette de `c`.

**m11-2 — `exercices/02-tamrin.json` Q1 : l'ajout est un fragment sans verbe.** Dans `من 36,5-36,7 إلى
نحو 37,1 درجة.`, placé après la phrase sur le corps jaune, il manque le verbe.
→ `وترتفع الحرارة من 36,5-36,7 إلى نحو 37,1 درجة.`

**m11-3 — `exercices/03-boss.json` Q4, clé `b` : « نهايتها » n'a pas d'antécédent dans l'option.**
- `b` ancien : `… فتُحسب الإباضة من نهايتها` → nouveau : `الجريبي متغيّر واللّوتيني ثابت، فتُحسب الإباضة من نهاية الدّورة` (63 ; `a` = 63)

**m11-4 — `exercices/05-tadrib.json` Q6 : les trois distracteurs sont hors sujet** (échanges
gazeux, coagulation, digestion), et l'élève les écarte sans rien savoir du chapitre. Le défaut est
préexistant ; le correcteur les a seulement allongés. On propose des erreurs du chapitre :
- `b` → `لتكوين بويضات جديدة في المبيض كلّ شهر` (37)
- `c` → `لإحداث الإلقاح داخل قناة البيض` (30)
- `d` → `لتهديم البطانة في آخر كلّ دورة` (30 ; étiquette possible `bio.cycle.regles-par-hausse-hormonale`)
- explication, ajouter : ` ولا تصنع بويضات جديدة (المخزون موجود منذ الولادة)، والحيض يأتي من انخفاضها لا من عملها.`

**m11-5 — `quiz.json` Q9 : l'ajout est redondant.** `فتبقى بطانة الرّحم قائمة.` répète « فلا يتهدّم
الشّبيك الرّحمي ». On peut le garder ou le supprimer ; ce n'est pas une faute.

### Questions relues sans constat (ch. 11)

`quiz` Q1, Q6, Q9 · `01-tamrin` Q3, Q4, Q5 · `02-tamrin` Q2, Q3, Q5 · `03-boss` Q2, Q5, Q6 ·
`04-defi` Q2, Q3, Q4, Q6 · `05-tadrib` Q1 · `06-defi-concours` Q2, Q3, Q4, Q5, Q6.

**Verdict ch. 11 : à corriger avant publication.** 4 MAJOR (3 doublons de fait à réécrire et une
explication rendue fausse), aucun BLOCKER, aucune clé fausse.

## Bilan

| Chapitre | Clés fausses | BLOCKER | MAJOR | MINOR | Verdict |
| -------- | ------------ | ------- | ----- | ----- | ------- |
| 09       | 0            | 1 (06 Q2 : `d` « لا يمكن الحكم » défendable, l'explication l'appuie) | 4 | 5 | à corriger |
| 10       | 0            | 0       | 2     | 8     | publiable après les 2 MAJOR |
| 11       | 0            | 0       | 4     | 5     | à corriger |

Il n'y a pas de fuite inverse : la clé strictement la plus courte représente 17 %, 13 % et 4 % des
questions, sous le hasard de 25 %. Le défaut le plus fréquent de cette tranche est le même qu'en
12–14 : une **clé raccourcie qui ne répond plus à tout l'énoncé** (09 04-defi Q5, 09 06 Q4). Vient
ensuite la **phrase d'explication ajoutée en queue sans raccord** (09–11, une dizaine de cas). Le
correcteur colle la justification retirée de la clé à la fin de l'explication. Ce collage produit
des fragments (« لأنّ … », « من 36,5 … »), des sujets indéterminés et, une fois (11 02-tamrin Q6), un
contresens.
