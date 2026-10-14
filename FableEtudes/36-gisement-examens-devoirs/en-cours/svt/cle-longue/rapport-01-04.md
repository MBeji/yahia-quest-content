# Rapport correcteur — fuite « clé la plus longue », SVT 9ᵉ, chapitres 01 · 02 · 03 · 04

> Mandat : `.claude/skills/content-engine/references/correction-cle-longue.md`, appliqué à la lettre ; audits
> `audit-12-14.md` et `audit-09-11.md` lus avant de commencer. Corpus : `/home/user/wt-svtkey`
> (`wip/svt-9eme-cle-longue`), moteur `/home/user/eng-svtkey`. Fichiers édités : seulement
> `quiz.json` et `exercices/0[1-6]-*.json` des huit dossiers `0[1-4]-*` ; aucune mission `*-examen-*`,
> aucun git. Sauvegardes avant/après : `/tmp/claude-0/cle-longue/svt0104/` (`bak/`, `patches/`).
> Note de périmètre : chaque numéro `NN` recouvre DEUX dossiers (01-takathur-insan + 01-wadhifat-al-ittisal,
> 02-al-af3al-al-in3ikasiya + 02-manaa, 03-al-ibsar + 03-wiratha, 04-al-hajiyat-al-ghithaiya + 04-zalazil) ;
> les huit ont été traités. Les taux de `content:tranche` incluent les missions d'examen (non touchées).

## Taux « clé strictement la plus longue » (`content:tranche`)

| NN | Dossiers | avant | après |
| -- | -------- | ----- | ----- |
| 01 | takathur-insan · wadhifat-al-ittisal | 57/90 = 63 % | 0/90 = 0 % |
| 02 | al-af3al-al-in3ikasiya · manaa | 66/99 = 67 % | 0/99 = 0 % |
| 03 | al-ibsar · wiratha | 49/105 = 47 % | 0/105 = 0 % |
| 04 | al-hajiyat-al-ghithaiya · zalazil | 62/90 = 69 % | 0/90 = 0 % |

Fuite inverse (clé strictement la plus COURTE, quiz + exercices 01-06) : 4 %, 12 %, 11 %, 11 % — sous le hasard (25 %).
Total : 243 questions touchées (29 + 29 + 33 + 33 + 34 + 21 + 31 + 33).

## Méthode, en bref

- Parade 1 (clé raccourcie, justification laissée à l'`explanation`) partout où la clé restait vraie à la lettre
  et répondait à tout l'énoncé ; parade 2 (distracteurs étoffés de même forme, faux sans ambiguïté) sinon ; les deux
  ensemble dans la majorité des cas (pour que la clé ne devienne pas la plus COURTE d'une marge nette).
- Aucune justification retirée n'a été recollée en queue d'explication : les 19 explications retouchées l'ont été
  en phrases complètes (ajout d'un distracteur à réfuter, connecteurs « ثمّ » à la place des flèches, etc.).
- Chaque question touchée a été relue à l'aveugle après édition ; contrôle automatique « clé non strictement la plus longue »
  à chaque patch (`apply.py`), format Prettier (largeur 100, objets d'option inline/éclatés préservés) vert.

## Points d'attention traités (liste des audits 09-14)

- Clé raccourcie qui ne répond plus à l'énoncé : conservé « فيروس », « الكيف/الكمّ », « القرنيّة أوّل وسط… », etc. ; ex. 04-hajiyat
  `03-boss` Q2 (clé garde la part « qualitative »), 03-wiratha `06` Q5 (« أحد الأبوين مصاب »).
- Piège « الخطأ في أنّ… » (02-al-af3al `03-boss` Q3) : clé reformulée « الخطأ في نسيان أنّ المنفّذ يأتي آخر الحلقة », et « نسيان »
  porté aussi par deux distracteurs (pas d'indice de forme).
- Indices de forme supprimés : polarité « خاطئ/صحيح » rééquilibrée 2/2 (01-takathur `04-defi` Q4) ; clé seule sans « لأنّ »
  ou seule « بفضل » (02-manaa `02-tamrin` Q5, `05-tadrib` Q5, 02-al-af3al quiz Q9) ; clé seule sans le mot « الميكروب » (02-manaa
  `02-tamrin` Q2, ramené à quatre noms nus) ; clé seule non introduite par « أن » (04-hajiyat `05-tadrib` Q5, quatre groupes nominaux) ;
  sens ← / « ; » cohérents entre options (04-zalazil `06` Q1, 03-wiratha `06` Q3) ; fraction « 1/16 » seule de 4 caractères (03-wiratha `06` Q4,
  d « 1/8 » remplacé par le piège naturel « 3/16 » = 1/4 × 3/4, expliqué).
- Distracteurs préexistants contredits par l'énoncé ou défendables, remplacés : 02-al-af3al `02-tamrin` Q2 (« لم ينجح التخدير » alors que le
  patient est inconscient d'après l'énoncé), `03-boss` Q2/Q4, 04-defi Q5 manaa, 03-al-ibsar `02-tamrin` Q2 (d « ليس مقلوبا » contredit la
  prémisse), 04-hajiyat `06` Q6 (distracteur « الأوّل : 270 مقابل 320 » qui se contredisait lui-même → « 270 مقابل 80 »), etc.
- Explications désignant une option par sa lettre ou un renvoi positionnel (avertissements QA) : corrigées (02-manaa quiz Q7, `05-tadrib` Q3,
  `04-defi` Q2/Q3, `06` Q5 ; 04-zalazil `06` Q5) → 0 avertissement de ce type.

## Doublons de fait réécrits (énoncé de l'exercice, ids/clé/étiquettes conservés)

| Paire (avant) | Jaccard | Réécriture de l'exercice |
| ------------- | ------- | ------------------------ |
| 03-al-ibsar quiz Q2 ↔ `01-tamrin` Q1 (ordre des membranes) | 0,80 | Q1 : « quelle membrane tapisse l'intérieur et porte les récepteurs ? » → la rétine (la cornée reste le distracteur étiqueté) |
| 03-al-ibsar quiz Q3 ↔ `01-tamrin` Q4 (ordre des milieux) | 0,71 | Q4 : « milieu qui suit l'humeur aqueuse » → corps cristallin |
| 03-al-ibsar quiz Q4 ↔ `02-tamrin` Q1 (image inversée) | 0,69 | Q1 : « type de lentille que miment les milieux » → lentille convergente |
| 03-al-ibsar quiz Q1 ↔ `01-tamrin` Q2 (rôle de l'iris) | 0,52 | Q2 : « qui convertit la lumière en influx » → rétine (iris = distracteur étiqueté) |
| 03-al-ibsar quiz Q9 ↔ `03-boss` Q6 (centres visuels) | 0,47 | Q6 : situation de choc occipital → perte de la vue yeux sains |
| 03-wiratha quiz Q1 ↔ `05-tadrib` Q1 (où sont les chromosomes) | 0,71 | Q1 : « rôle des chromosomes » |
| 03-wiratha `03-boss` Q6 ↔ 07-annales `01-sujet` Q2 (inter-chapitres, caryotype 44+XY) | 0,53 | Q6 : caryotype 44+XX (a/b permutés), la clé reste `b` ; 07 n'est pas de mon périmètre |
| 04-hajiyat `02-tamrin` Q1 ↔ `05-tadrib` Q2 et quiz Q4 (kcal d'un gramme) | 0,77 / 0,45 | Q1 : « quel groupe donne le plus d'énergie par gramme » |
| 04-zalazil `01-tamrin` Q2 ↔ `05-tadrib` Q1 (définition du foyer) | 0,46 | Q1 de `05` : définition inversée (nom d'un point à 10 km de profondeur) |
| 01-takathur quiz Q3 ↔ `02-tamrin` Q3 (lieu de la fécondation) | 0,47 | Q3 : situation (« l'ovule monte vers l'utérus, les spermatozoïdes depuis le vagin… ») ; options inchangées |
| 01-wadhifat quiz Q5 ↔ `01-tamrin` Q3 (31 paires de nerfs rachidiens) | 0,60 | Q3 : « d'où émergent les nerfs crâniens ? » → cerveau |

## Paires proches LAISSÉES (exercice parallèle voulu, à trancher)

- 01-takathur `04-defi` Q1 ↔ `06` Q2 (0,58) : même savoir-faire (jour d'ovulation = longueur − 14), données différentes (30 vs 32 jours), deux paliers de difficulté 3.
- 03-al-ibsar quiz Q7 ↔ `03-boss` Q1 (0,50) : presbytie (hypermétropie) vs myopie — faits miroirs, pas le même fait.
- 03-wiratha `03-boss` Q6 ↔ 07-annales `01-sujet` Q2 (0,47, inter-chapitres) : le contenu de 07 appartient à l'autre correcteur ; à recouper au niveau du tronc.
- 04-hajiyat `01-tamrin` Q1 ↔ `05-tadrib` Q1 (0,53) : réactifs différents (amidon / chlorures) ; `03-boss` Q5 ↔ `05-tadrib` Q6 (0,53) : besoins en fer vs calcium.

## Défauts préexistants repérés, NON corrigés (hors mandat)

- **Position de la clé** (interdit d'y toucher) : b 47-53 %, d 2-7 %, dans les quatre numéros — fuite de position massive, à traiter par une autre tranche (permutation des ids).
- 01-wadhifat quiz Q5 : option `d` « 31 عصبا لا 31 زوجا » incohérente (non touchée).
- 01-takathur `04-defi` Q2 : `b`/`d` (« بطانة رقيقة », « مهبل قصير ») contredisent l'énoncé (« أجهزتها سليمة ») ; conservés, étoffés seulement.
- 03-wiratha quiz Q4 et `02-tamrin` Q1 : la clé est la seule option qui contient « ADN » (indice de forme préexistant).
- 04-hajiyat `04-defi` Q2 : l'option `b` (« اختلاف الجنس ») est écartée par l'énoncé (deux femmes) — voulue par l'explication, mais éliminable à vue.
- 02-manaa `description` : chapitre « خارج البرنامج الرسمي » (supplémentaire) ; idem 03-wiratha, 04-zalazil.
- `qa:strict` : 1 avertissement hors périmètre (« 07-annales-subur sans domaine »).

## Sorties des trois commandes (état final)

```
npm run -s content:check            → Validated 120 subject(s): 1058 chapters, 4747 exercises, 28834 questions. (0 erreur)
npm run -s content:qa:strict -- --subject sciences-vie-terre | tail -3
                                    → Content QA: 0 error(s), 1 warning(s) to review. (avertissement : 07-annales-subur sans domaine)
npm run -s content:tranche -- --subject sciences-vie-terre --chapters 01|02|03|04
                                    → clé strictement la plus longue : 0/90 · 0/99 · 0/105 · 0/90 (0 %)
                                      paires proches : 2 (01) · 0 (02) · 2 (03) · 2 (04), toutes justifiées ci-dessus
npx prettier --check content/sciences-vie-terre/0[1-4]-*  → All matched files use Prettier code style!
```

## Détail par question (réf, parade, ancien → nouveau pour la clé)

Notation : `quiz` ou `exercices/<fichier>`, `Q<n>` 1-based. « clé raccourcie » = parade 1 ; « distracteurs étoffés/remplacés » = parade 2
(lettres des options étoffées) ; options et explications intégrales : voir `git diff` du dossier et `bak/` ci-dessus.

### 01-takathur-insan

- `quiz` Q1 — clé raccourcie — clé c : « بدء الغدد التناسلية في إنتاج الأمشاج » (36) → « بدء إنتاج الأمشاج » (17)
- `quiz` Q3 — clé raccourcie — clé d : « في البوق (قناة فالوب) » (21) → « في البوق » (8)
- `quiz` Q4 — clé raccourcie — clé b : « في منتصف الدورة (نحو اليوم 14) » (30) → « نحو اليوم 14 من الدورة » (22)
- `quiz` Q5 — clé raccourcie — clé c : « على عدم حدوث إلقاح فتساقطت بطانة الرحم » (38) → « على عدم حدوث إلقاح في الدورة » (28)
- `quiz` Q7 — distracteurs étoffés/remplacés a,c,d — clé b : « البيضة المخصّبة (اللاقحة) » (25) → « البيضة المخصّبة (اللاقحة) » (25)
- `quiz` Q8 — clé raccourcie — clé d : « مصافحة شخص مصاب أو مشاركته الطعام » (33) → « مصافحة شخص مصاب أو مجالسته » (26)
- `02-tamrin` Q1 — clé retouchée ; distracteurs étoffés/remplacés a,c,d — clé b : « من اليوم الأوّل للطمث » (21) → « من أوّل يوم لنزول الطمث » (23)
- `02-tamrin` Q2 — clé raccourcie — clé b : « تتفكّك وتنزل مع الدم (الطمث) » (28) → « تتفكّك وتنزل مع الدم » (20)
- `02-tamrin` Q3 — énoncé réécrit (doublon) ; clé raccourcie — clé c : « في البوق (قناة فالوب) » (21) → « في البوق » (8)
- `02-tamrin` Q4 — distracteurs étoffés/remplacés a,c,d — clé b : « بيضة مخصّبة (لاقحة) » (19) → « بيضة مخصّبة (لاقحة) » (19)
- `02-tamrin` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « لأنّ البيضة المخصّبة انغرست فبقيت بطانة الرحم لاحتضان الجنين » (60) → « لأنّ البيضة المخصّبة انغرست فبقيت البطانة » (41)
- `02-tamrin` Q6 — clé raccourcie — clé b : « عن طريق المشيمة والحبل السرّي » (29) → « عن طريق المشيمة » (15)
- `03-boss` Q1 — clé raccourcie ; distracteurs étoffés/remplacés b — clé a : « إفراز الغدد التناسلية للهرمونات الجنسية » (39) → « إفراز الهرمونات الجنسية » (23)
- `03-boss` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « كي يكتمل العدد عند اندماجهما فيرث الكائن الجديد من الأبوين معًا » (63) → « كي يكتمل عدد الصبغيّات عند اندماجهما » (36)
- `03-boss` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « انقسام البيضة المخصّبة وتنقّلها ← تعشيش في بطانة الرحم ← بداية الحمل » (68) → « انقسام البيضة ← تعشيش في الرحم ← بداية الحمل » (44)
- `03-boss` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « تغذية النطاف وحملها لتنتقل وتبقى حيّة » (37) → « تغذية النطاف وحملها نحو البويضة » (31)
- `03-boss` Q6 — clé raccourcie — clé a : « على حدوث حمل محتمل (انغراس بيضة مخصّبة) » (39) → « على احتمال انغراس بيضة مخصّبة » (29)
- `04-defi` Q2 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « غياب المشيج الذكري يمنع اندماجه مع البويضة » (42) → « غياب المشيج الذكري عن المنيّ » (28)
- `04-defi` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,d — clé b : « لضمان اندماج نطفة واحدة فقط فيكتمل العدد الصبغي بشكل سليم » (57) → « لضمان اندماج نطفة واحدة فقط » (27)
- `04-defi` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « خاطئ؛ لا ينتقل الفيروس بالمصافحة أو المشاركة العادية، بل بالجنس غير المحمي والدم الملوّث ومن الأمّ إلى جنينها » (109) → « خاطئ، فالفيروس لا ينتقل بالمصافحة ولا بالمقعد » (45)
- `04-defi` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « لأنّه يقي من الأمراض المنقولة جنسيًّا ويمنع الحمل غير المرغوب فيه معًا » (70) → « لأنّه يقي من العدوى ومن الحمل غير المرغوب » (41)
- `04-defi` Q6 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « المتابعة الطبّية أثناء الحمل والولادة والحذر في الرضاعة وفق إرشاد الطبيب » (72) → « المتابعة الطبّية في الحمل والولادة والرضاعة » (43)
- `05-tadrib` Q3 — clé raccourcie — clé b : « تحرير المبيض لبويضة ناضجة حول منتصف الدورة » (42) → « تحرير المبيض لبويضة ناضجة » (25)
- `05-tadrib` Q4 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « الإلقاح اندماج النطفة بالبويضة، والتعشيش انغراس البيضة المخصّبة في بطانة الرحم » (78) → « الإلقاح اندماج المشيجين والتعشيش انغراس اللاقحة » (47)
- `05-tadrib` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « لأنّ بطانة الرحم تبقى محفوظةً لاحتضان الجنين فلا تتساقط » (55) → « لأنّ بطانة الرحم تبقى محفوظة لاحتضان الجنين » (43)
- `05-tadrib` Q6 — clé raccourcie ; distracteurs étoffés/remplacés a,d — clé b : « لأنّ النطفة والبويضة يحمل كلّ منهما نصف المعلومة الوراثية فتجتمعان في البيضة المخصّبة » (85) → « لأنّ المشيجين يحمل كلّ منهما نصف المعلومة الوراثية » (50)
- `06-defi-concours` Q1 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « تثخين بطانة الرحم وتهيئتها لتعشيش بويضة مخصّبة محتملة » (53) → « تثخين بطانة الرحم للتعشيش » (25)
- `06-defi-concours` Q3 — clé raccourcie — clé a : « عدم حدوث الإباضة، فلا تُطلَق بويضة للإخصاب » (42) → « غياب الإباضة في هذه الدورة » (26)
- `06-defi-concours` Q6 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « الحيض يحدث عند غياب الإخصاب: تتساقط بطانة الرحم؛ أمّا التعشيش فيوقف الحيض » (73) → « الحيض يحدث عند غياب الإخصاب لا عند التعشيش » (42)

_29 questions touchées._

### 01-wadhifat-al-ittisal

- `quiz` Q3 — clé raccourcie — clé c : « من ألياف عصبيّة محاطة بأغمدة دهنيّة » (35) → « من ألياف عصبيّة بأغمدة دهنيّة » (29)
- `quiz` Q4 — clé raccourcie ; distracteurs étoffés/remplacés b,c — clé d : « في خارج المخ (القشرة) وفي داخل النّخاع » (38) → « في خارج المخ وفي داخل النّخاع » (29)
- `quiz` Q7 — clé raccourcie — clé c : « لأنّ المحور العصبيّ جزء من الخليّة نفسها، فيضمحلّ بموت جسمها الخلويّ » (68) → « لأنّ المحور جزء من الخليّة فيضمحلّ بموت جسمها الخلويّ » (53)
- `quiz` Q9 — clé raccourcie — clé b : « ضغط نفسيّ ظرفيّ، وهو ردّ فعل عاديّ يزول بزوال سببه » (50) → « ضغط نفسيّ ظرفيّ يزول بزوال سببه » (31)
- `01-tamrin` Q3 — énoncé réécrit (doublon) ; clé retouchée ; distracteurs étoffés/remplacés a,b,d ; explication retouchée — clé c : « 31 زوجا » (7) → « من الدّماغ مباشرةً » (18)
- `01-tamrin` Q4 — clé raccourcie ; distracteurs étoffés/remplacés d ; explication retouchée — clé b : « معالجة السّيالة العصبيّة، لأنّها تتكوّن من أجسام خلويّة » (55) → « معالجة السّيالة بأجسامها الخلويّة » (33)
- `01-tamrin` Q5 — distracteurs étoffés/remplacés a,b,d — clé c : « الخليّة العصبيّة » (16) → « الخليّة العصبيّة » (16)
- `01-tamrin` Q6 — clé raccourcie ; distracteurs étoffés/remplacés b — clé a : « في اتّجاه واحد: من التّغصّنات إلى التّفرّع النّهائيّ » (52) → « اتّجاه واحد من التّغصّنات إلى التّفرّع » (38)
- `02-tamrin` Q2 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « الفطريّ موجود عند كلّ سليم منذ الولادة، والشّرطيّ مكتسب بالتدرّب » (64) → « الفطريّ منذ الولادة، والشّرطيّ يُكتسب » (37)
- `02-tamrin` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,b — clé c : « في خارج المخّ (القشرة) وفي داخل النّخاع » (39) → « في خارج المخّ وفي داخل النّخاع » (30)
- `02-tamrin` Q6 — clé raccourcie — clé a : « العاديّ ظرفيّ وردّ فعل طبيعيّ، والمرضيّ مزمن ومستمرّ » (52) → « العاديّ ظرفيّ، والمرضيّ مزمن ومستمرّ » (36)
- `03-boss` Q1 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « أنّ كلّ نصف كرة يتحكّم في الجانب المخالف: المسار يتقاطع » (55) → « أنّ كلّ نصف كرة يتحكّم في الجانب المخالف له » (43)
- `03-boss` Q2 — clé raccourcie ; distracteurs étoffés/remplacés a,d — clé c : « شلل المنطقة التي يعصّبها هذا العصب وحدها » (40) → « شلل منطقة هذا العصب وحدها » (25)
- `03-boss` Q4 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « لأنّ البيضاء ألياف بأغمدة دهنيّة مخصّصة للنّقل، والسّنجابيّة أجسام خلويّة مخصّصة للمعالجة » (89) → « لأنّ البيضاء ألياف للنّقل، والسّنجابيّة أجسام للمعالجة » (54)
- `03-boss` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,d — clé c : « انعكاسيّ فطريّ، لأنّه بلا تفكير وموجود منذ الولادة » (50) → « انعكاسيّ فطريّ، لأنّه موجود منذ الولادة » (39)
- `04-defi` Q1 — clé raccourcie ; distracteurs étoffés/remplacés c — clé b : « إصابة تمسّ المسار الحركيّ دون المسار الحسّيّ » (44) → « إصابة تمسّ المسار الحركيّ دون الحسّيّ » (37)
- `04-defi` Q2 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « الأوّل يُشلّ جانبه الأيسر، والثّاني تُشلّ منطقة عصب النّسا الأيمن وحدها » (71) → « الأوّل يُشلّ جانبه الأيسر والثّاني منطقة العصب الأيمن وحدها » (59)
- `04-defi` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « لأنّ الجهاز المركزي هو الدّماغ والنّخاع فقط، والأعصاب مهما اتّصلت بهما تبقى محيطيّة » (83) → « لأنّ المركزي هو الدّماغ والنّخاع الشّوكيّ فقط » (45)
- `04-defi` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « تمييز المسار الحسّيّ من المسار الحركيّ، إذ يصير كلّ عصب مزدوجا بالضّرورة » (72) → « تمييز المسار الحسّيّ من المسار الحركيّ » (38)
- `04-defi` Q5 — clé raccourcie — clé b : « خاطئ: المعيار هو وجود القرار لا السّرعة — والضّغط على الفرامل سريع وهو شرطيّ » (76) → « خاطئ: المعيار هو وجود القرار لا السّرعة » (39)
- `04-defi` Q6 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « لأنّه يحدّ من الضّغط النّفسيّ، وهو أحد عوامل الخطر مع الضّجيج والمخدّرات » (72) → « لأنّه يحدّ من الضّغط النّفسيّ وهو من عوامل الخطر » (48)
- `05-tadrib` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a — clé c : « الجسم الخلويّ الموجود في النّخاع » (32) → « الجسم الخلويّ في النّخاع » (24)
- `05-tadrib` Q5 — clé raccourcie — clé b : « يُفقد الإحساس في راحة اليد دون شلل حركيّ » (40) → « يُفقد الإحساس في راحة اليد وحده » (31)
- `05-tadrib` Q6 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « الضّجيج، التّوتّر النّفسيّ المزمن، المخدّرات » (44) → « الضّجيج، التّوتّر المزمن، المخدّرات » (35)
- `06-defi-concours` Q2 — clé raccourcie ; distracteurs étoffés/remplacés a,b,d — clé c : « لأنّه مرتبط بطعام تعرّف عليه الشّخص سابقا: فهو مكتسب، إذن شرطيّ » (63) → « لأنّه مكتسب بتجربة سابقة مع الطّعام » (35)
- `06-defi-concours` Q3 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « نطلب منه تحريك يده إراديّا: إن تحرّكت فالمسار الحركيّ سليم والخلل حسّيّ » (71) → « نطلب تحريك يده إراديّا: إن تحرّكت فالحركيّ سليم » (47)
- `06-defi-concours` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a — clé b : « التّقاطع هو ما يجعل كلّ نصف كرة مسؤولا عن الجانب المخالف من الجسم » (65) → « التّقاطع يجعل كلّ نصف كرة مسؤولا عن الجانب المخالف » (50)
- `06-defi-concours` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « الأوّل ردّ فعل ظرفيّ عاديّ، والثّاني ضغط مزمن وهو عامل خطر على الجهاز العصبي » (76) → « الأوّل ظرفيّ عاديّ، والثّاني ضغط مزمن عامل خطر » (46)
- `06-defi-concours` Q6 — clé raccourcie ; distracteurs étoffés/remplacés b,c — clé a : « لأنّ الأجسام الخلويّة تعالج والألياف تنقل: فحيثما وُجدت معالجة وُجدت سنجابيّة، وحيثما وُجد نقل وُجدت بيضاء » (106) → « لأنّ الأجسام الخلويّة تعالج والألياف تنقل » (41)

_29 questions touchées._

### 02-al-af3al-al-in3ikasiya

- `quiz` Q1 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « منبّهات خارجيّة ومنبّهات داخليّة » (32) → « منبّهات خارجيّة وداخليّة معا » (28)
- `quiz` Q3 — clé raccourcie ; distracteurs étoffés/remplacés b,d — clé a : « المستقبل الحسّي ضروريّ لحدوث الفعل الانعكاسيّ » (45) → « المستقبل الحسّي ضروريّ لحدوث الفعل » (34)
- `quiz` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « خمسة: مستقبل حسّي، ناقل حسّي، مركز عصبيّ، ناقل حركيّ، عضو منفّذ » (63) → « خمسة: مستقبل، ناقل حسّي، مركز، ناقل حركيّ، منفّذ » (48)
- `quiz` Q7 — clé raccourcie — clé a : « لأنّ المخ ليس من عناصر القوس الانعكاسي النّخاعيّ » (48) → « لأنّ المخ ليس من عناصر القوس النّخاعيّ الخمسة » (45)
- `quiz` Q9 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « لربح الوقت: الحلقة أقصر فتحدث الحركة قبل الشّعور بالألم » (55) → « لأنّ الحلقة أقصر فتحدث الحركة قبل أن نتألّم » (43)
- `quiz` Q10 — clé raccourcie ; distracteurs étoffés/remplacés d — clé c : « لأنّ النّتيجة لن تسمّي أيّ العنصرين كان السّبب » (46) → « لأنّ النّتيجة لن تحدّد أيّ العنصرين هو السّبب » (45)
- `01-tamrin` Q1 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d,e — clé b : « أنّه موجود منذ الولادة ويحدث بنفس الطّريقة عند كلّ الأفراد العاديّين من نفس النّوع » (82) → « أنّه موجود منذ الولادة وثابت عند كلّ الأفراد » (44)
- `01-tamrin` Q6 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « وقاية الجسم من الأخطار والحفاظ على توازنه وتنظيم وظائف أعضائه الدّاخليّة » (72) → « وقاية الجسم من الأخطار وحفظ توازنه » (34)
- `02-tamrin` Q1 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé b : « استطالة العضلة الباسطة التي شدّها الوتر » (39) → « استطالة العضلة الباسطة » (22)
- `02-tamrin` Q2 — clé raccourcie ; distracteurs étoffés/remplacés a — clé b : « لأنّ الوعي ليس من عناصر القوس الانعكاسيّ الخمسة » (47) → « لأنّ الوعي ليس من عناصر القوس الخمسة » (36)
- `02-tamrin` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,d — clé c : « أنّ المستقبل الحسّيّ ضروريّ لحدوث الفعل » (39) → « أنّ المستقبل الحسّيّ ضروريّ للفعل » (33)
- `02-tamrin` Q6 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « لأنّ دماغها خُرّب ولم يبق لها من المراكز إلّا النّخاع الشّوكيّ » (62) → « لأنّ دماغها خُرّب وبقي لها النّخاع الشّوكيّ » (43)
- `03-boss` Q1 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « لأنّ «لا حركة» نتيجة مشتركة بين الثّلاث: ما يسمّي العنصر هو المقارنة بين تجربتين لا تختلفان إلّا فيه » (100) → « لأنّ «لا حركة» نتيجة مشتركة بين الثّلاث فلا تسمّي العنصر » (56)
- `03-boss` Q2 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « أنّ المركز والعضلات ما زالت سليمة، وأنّ العطب في النّاقل الأيمن وحده » (68) → « أنّ المركز سليم وأنّ العطب في النّاقل الأيمن وحده » (49)
- `03-boss` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « الخطأ في أنّ العضو المنفّذ آخر الحلقة دائمًا، والقرب المكانيّ لا يغيّر ترتيب المرور » (83) → « الخطأ في نسيان أنّ المنفّذ يأتي آخر الحلقة دائمًا » (49)
- `03-boss` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « أنّ إصابة بلغت النّخاع الشّوكيّ، وهو المركز المشترك للرّجلين » (60) → « أنّ إصابة بلغت النّخاع الشّوكيّ المشترك للرّجلين » (48)
- `03-boss` Q5 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « مستقبل في القرنيّة ← عصب حسّيّ ← مركز عصبيّ ← عصب حركيّ ← الغدّة الدّمعيّة » (74) → « مستقبل ← عصب حسّيّ ← مركز ← عصب حركيّ ← الغدّة الدّمعيّة » (56)
- `03-boss` Q6 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé b : « لأنّ مساره أقصر: يتوقّف عند النّخاع ولا يصعد إلى المخّ » (54) → « لأنّ مساره أقصر: يتوقّف عند النّخاع » (35)
- `04-defi` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « أنّ المركز العصبيّ ضروريّ للفعل، وأنّ العضلة ليست هي المعطوبة » (61) → « أنّ المركز العصبيّ ضروريّ للفعل وأنّ العضلة سليمة » (49)
- `04-defi` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a — clé b : « أنّ التّخدير ألغى مستقبلات اللّثة وحدها، ومستقبلات الشّمّ خارج منطقته » (69) → « أنّ التّخدير ألغى مستقبلات اللّثة وحدها » (39)
- `04-defi` Q5 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « لأنّ الإصابة فوق مركز هذا الفعل: القوس القطنيّ سليم وكامل رغم انقطاع الصّلة بالمخّ » (82) → « لأنّ الإصابة فوق مركزه: القوس القطنيّ سليم » (42)
- `04-defi` Q6 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « لأنّ الضّفدعة السّليمة تتحرّك إراديًّا أيضًا، فلا يمكن تمييز الحركة الانعكاسيّة من الإراديّة » (92) → « لأنّ السّليمة تتحرّك إراديًّا فتختلط الحركتان » (45)
- `05-tadrib` Q2 — clé raccourcie — clé b : « من المركز إلى العضو المنفّذ » (27) → « من المركز إلى المنفّذ » (21)
- `05-tadrib` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,d — clé c : « يحدث منذ الولادة وبنفس الطّريقة عند الأفراد العاديّين من نفس النّوع » (67) → « يحدث منذ الولادة وبنفس الطّريقة عند الجميع » (42)
- `05-tadrib` Q4 — clé raccourcie — clé b : « الغدّة اللّعابيّة أو الدّمعيّة » (30) → « الغدّة الدّمعيّة » (16)
- `05-tadrib` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « تغيير عنصر واحد في كلّ مرّة ومقارنة النّتيجة بالشّاهد » (53) → « تغيير عنصر واحد في كلّ مرّة ومقارنته بالشّاهد » (45)
- `05-tadrib` Q6 — clé raccourcie ; distracteurs étoffés/remplacés a,b,d — clé c : « سلامة النّخاع الشّوكيّ والقوس الذي يمرّ به » (42) → « سلامة النّخاع الشّوكيّ » (22)
- `06-defi-concours` Q1 — clé raccourcie — clé b : « يثبت أنّ كلّ ما بعد المستقبل سليم، فيصير غياب الحركة منسوبًا إلى المستقبل وحده » (78) → « يثبت أنّ كلّ ما بعد المستقبل سليم » (33)
- `06-defi-concours` Q2 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « كونه موجودًا منذ الولادة ويحدث بنفس الطّريقة عند كلّ المواليد العاديّين » (71) → « كونه موجودًا منذ الولادة وثابتًا عند المواليد » (45)
- `06-defi-concours` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « الأوّل يغلق في النّخاع بخمسة عناصر، والثّاني ينطلق من المخّ وينزل إلى العضلة » (76) → « الأوّل يغلق في النّخاع والثّاني ينطلق من المخّ » (46)
- `06-defi-concours` Q4 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « أنّ القوس النّخاعيّ يخضع لتأثير المخّ الذي قد يكبح الفعل، وشغل الانتباه يرفع هذا الكبح » (86) → « أنّ المخّ قد يكبح القوس، وشغل الانتباه يرفع الكبح » (49)
- `06-defi-concours` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « أنّ كلّ عنصر من عناصر القوس ضروريّ، وأنّ إلغاء أيّ واحد منها يكفي لإلغاء الفعل » (78) → « أنّ كلّ عنصر ضروريّ، وإلغاء أيّ منها يلغي الفعل » (47)
- `06-defi-concours` Q6 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « الحرق أتلف المستقبلات الحسّيّة في المنطقة المحروقة وحدها، وبقيت مستقبلات ظهر اليد سليمة » (87) → « الحرق أتلف مستقبلات المنطقة المحروقة وحدها » (42)

_33 questions touchées._

### 02-manaa

- `quiz` Q1 — clé raccourcie ; distracteurs étoffés/remplacés a,d — clé b : « جزيء غريب عن الجسم يستثير ردّ فعل دفاعيًّا » (42) → « جزيء غريب يستثير ردّ فعل دفاعيًّا » (33)
- `quiz` Q6 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé b : « أنّه يرتبط بمستضدّ واحد موافق له فقط كالمفتاح وقفله » (51) → « أنّه يرتبط بمستضدّ واحد موافق له فقط » (36)
- `quiz` Q7 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d ; explication retouchée — clé b : « التلقيح يحقن ميكروبًا مُضعَّفًا فيصنع الجسمُ مناعته (وقاية)، والمصل يحقن أجسامًا مضادّة جاهزة (علاج سريع) » (105) → « التلقيح يحقن ميكروبًا مُضعَّفًا، والمصل يحقن أجسامًا مضادّة جاهزة » (65)
- `quiz` Q8 — clé raccourcie ; distracteurs étoffés/remplacés d — clé b : « أنّ فيروس VIH يدمّر اللمفاويات T فينهار جهاز المناعة وتظهر أمراض انتهازية » (73) → « أنّ فيروس VIH يدمّر اللمفاويات T فينهار جهاز المناعة » (52)
- `01-tamrin` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « دخول متعضّية ممرضة إلى الجسم وتكاثرها فيه » (41) → « دخول ميكروب ممرض إلى الجسم وتكاثره فيه » (38)
- `01-tamrin` Q4 — distracteurs étoffés/remplacés a,b,c — clé d : « الأجسام المضادّة » (16) → « الأجسام المضادّة » (16)
- `01-tamrin` Q5 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé b : « لأنّ الأنفلونزا يسبّبها فيروس، والمضادّ الحيوي فعّال ضدّ البكتيريا فقط » (70) → « لأنّ الأنفلونزا يسبّبها فيروس لا بكتيريا » (40)
- `01-tamrin` Q6 — clé raccourcie ; distracteurs étoffés/remplacés c — clé b : « يُخترَق خطّ الدفاع الأوّل فتتمكّن الجراثيم من الدخول وقد تسبّب عدوى » (67) → « يُخترَق خطّ الدفاع الأوّل فتدخل الجراثيم » (40)
- `02-tamrin` Q1 — clé raccourcie — clé b : « الكريات البيضاء البلعمية » (24) → « الكريات البيضاء » (15)
- `02-tamrin` Q2 — clé raccourcie — clé c : « إطراح بقايا الميكروب المهضوم » (28) → « الإطراح » (7)
- `02-tamrin` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « الالتهاب الذي يرافق نشاط الكريات البيضاء » (40) → « الالتهاب وتوافد الكريات البيضاء » (31)
- `02-tamrin` Q5 — clé raccourcie ; distracteurs étoffés/remplacés c — clé b : « بفضل الذاكرة المناعية التي تجعل الردّ الثاني أسرع وأقوى » (55) → « لأنّ الذاكرة المناعية تجعل الردّ أسرع » (37)
- `03-boss` Q1 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « ينتجها جسم الملقَّح نفسه استجابةً للميكروب المُضعَّف » (52) → « ينتجها جسم الملقَّح نفسه استجابةً للّقاح » (40)
- `03-boss` Q2 — clé raccourcie ; distracteurs étoffés/remplacés a — clé b : « حقن مصل مضادّ للكزاز لأنّه يوفّر أجسامًا مضادّة جاهزة فوريّة » (60) → « حقن مصل مضادّ للكزاز لتوفير أجسام مضادّة جاهزة » (46)
- `03-boss` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « التلقيح يمنح حماية طويلة الأمد (بذاكرة مناعية)، والمصل حماية قصيرة (بلا ذاكرة) » (78) → « التلقيح يمنح حماية طويلة بذاكرة، والمصل قصيرة بلا ذاكرة » (55)
- `03-boss` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « أنّه حالة نقص في مناعة الجسم مكتسبة بسبب فيروس VIH » (50) → « أنّه نقص في المناعة مكتسب بفيروس VIH » (36)
- `03-boss` Q6 — clé raccourcie — clé b : « لأنّ تدمير اللمفاويات T يُضعف المناعة النوعية فيعجز الجسم عن مقاومة العدوى » (74) → « لأنّ تدمير اللمفاويات T يُضعف المناعة النوعية » (45)
- `04-defi` Q1 — clé raccourcie ; distracteurs étoffés/remplacés c — clé b : « الردّ الثاني أقوى وأسرع بفضل الذاكرة المناعية المتكوّنة بعد الحقنة الأولى » (73) → « الردّ الثاني أقوى وأسرع بفضل الذاكرة المناعية » (45)
- `04-defi` Q2 — clé raccourcie ; distracteurs étoffés/remplacés d ; explication retouchée — clé b : « الحقن الأوّل بالميكروب المُضعَّف أكسب الفأر (أ) مناعة (تلقيح) فقاوم الميكروب الممرض » (83) → « الحقن الأوّل بالميكروب المُضعَّف أكسب الفأر (أ) مناعة » (53)
- `04-defi` Q3 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d ; explication retouchée — clé a : « المصل يمنح حماية فورية بأجسام مضادّة جاهزة، واللقاح يبني حماية طويلة الأمد لاحقًا » (81) → « لأنّ المصل يمنح حماية فورية واللقاح حماية طويلة » (47)
- `04-defi` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « تدمير VIH للمفاويات T يُضعف المناعة، فتنتهز الميكروبات هذا الضعف وتسبّب العدوى » (78) → « تدمير VIH للمفاويات T يُضعف المناعة فتنتهز الميكروبات ذلك » (57)
- `04-defi` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a — clé b : « المضادّ الحيوي لا يؤثّر في الفيروسات، وسوء استعماله قد يسبّب مقاومة البكتيريا للمضادّات » (87) → « المضادّ الحيوي لا يؤثّر في الفيروسات بل في البكتيريا » (52)
- `05-tadrib` Q1 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « جسم غريب يدخل الجسم فيستثير ردّ فعل مناعيًّا » (44) → « جسم غريب يستثير ردّ فعل مناعيًّا » (32)
- `05-tadrib` Q2 — clé raccourcie ; distracteurs étoffés/remplacés b — clé a : « الجلد والأغشية المخاطية السليمة » (31) → « الجلد والأغشية المخاطية » (23)
- `05-tadrib` Q3 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d ; explication retouchée — clé a : « النوعية موجّهة ضدّ ميكروب محدّد وتترك ذاكرة، أمّا غير النوعية فعامّة وسريعة » (75) → « النوعية موجّهة ضدّ ميكروب محدّد وتترك ذاكرة » (43)
- `05-tadrib` Q4 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « التلقيح لأنّه يكسب الجسم ذاكرة مناعية تدوم طويلًا » (49) → « التلقيح لأنّه يكسب الجسم ذاكرة مناعية » (37)
- `05-tadrib` Q5 — clé raccourcie ; distracteurs étoffés/remplacés c — clé b : « بفضل خلايا الذاكرة المتكوّنة من التعرّض الأوّل » (46) → « لأنّ الذاكرة تكوّنت من التعرّض الأوّل » (37)
- `05-tadrib` Q6 — clé raccourcie ; distracteurs étoffés/remplacés d — clé b : « المصافحة والاحتكاك اليومي العادي لا ينقلان الفيروس فلا مبرّر للإقصاء » (68) → « المصافحة والاحتكاك العادي لا ينقلان الفيروس » (43)
- `06-defi-concours` Q1 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « المستضدّ (الأنتيجان) الذي حرّض إنتاجه فقط » (41) → « المستضدّ الذي حرّض إنتاجه فقط » (29)
- `06-defi-concours` Q2 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « الذاكرة المناعية: خلايا ذاكرة تكوّنت في التماسّ الأوّل » (54) → « الذاكرة المناعية من التماسّ الأوّل » (34)
- `06-defi-concours` Q4 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « اللقاح مستضدّ مُضعَّف يمنح مناعة ذاتية بطيئة ودائمة (وقائيّ) ; المصل أجسام مضادّة جاهزة تمنح مناعة منقولة فورية وقصيرة (علاجيّ) » (127) → « اللقاح مستضدّ مُضعَّف يمنح مناعة ذاتية دائمة، والمصل أجسام جاهزة تمنح مناعة قصيرة » (81)
- `06-defi-concours` Q5 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d ; explication retouchée — clé a : « كلاهما محميّ: (أ) بمناعة ذاتية و(ب) بمناعة منقولة عبر المصل » (59) → « كلاهما محميّ: (أ) بمناعة ذاتية و(ب) بمصل جاهز » (45)
- `06-defi-concours` Q6 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « المستضدّ جسمٌ غريب يدخل الجسم، والأجسام المضادّة يُنتجها الجسم ردًّا عليه لتُبطله » (81) → « المستضدّ غريب والأجسام المضادّة يُنتجها الجسم ردًّا عليه » (56)

_33 questions touchées._

### 03-al-ibsar

- `quiz` Q1 — clé raccourcie — clé b : « تعديل كمّيّة الضّوء الدّاخل عبر الحدقة » (38) → « تعديل كمّيّة الضّوء الدّاخل إلى العين » (37)
- `quiz` Q5 — clé raccourcie — clé b : « لأنّ الإبصار يحدث في المخ، وهو الذي يدمج الصّورتين في الاتّجاه الصّحيح » (70) → « لأنّ المخ هو الذي يصحّح الاتّجاه عند الإبصار » (44)
- `quiz` Q8 — clé raccourcie — clé d : « في نقل السّيالة من الشّبكيّة إلى المخ » (37) → « في نقل السّيالة إلى مراكز الإبصار » (33)
- `quiz` Q9 — distracteurs étoffés/remplacés b — clé a : « في الجهة الخلفيّة من المخ » (25) → « في الجهة الخلفيّة من المخ » (25)
- `quiz` Q10 — clé raccourcie — clé c : « لأنّ أنبوبة القطرة تلامس العين المصابة فتحمل إفرازاتها النّاقلة للعدوى » (70) → « لأنّ أنبوبة القطرة تحمل إفرازات عين مصابة » (41)
- `01-tamrin` Q1 — énoncé réécrit (doublon) ; clé raccourcie ; distracteurs étoffés/remplacés a,c,d ; explication retouchée — clé b : « الصّلبة ← المشيميّة ← الشّبكيّة » (31) → « الشّبكيّة » (9)
- `01-tamrin` Q2 — énoncé réécrit (doublon) ; clé raccourcie ; distracteurs étoffés/remplacés b,c,d ; explication retouchée — clé a : « تعديل كمّيّة الضّوء الدّاخل إلى العين » (37) → « الشّبكيّة » (9)
- `01-tamrin` Q4 — énoncé réécrit (doublon) ; clé raccourcie ; distracteurs étoffés/remplacés a,c,d ; explication retouchée — clé b : « القرنيّة ← الخلط المائيّ ← الجسم البلّوريّ ← الخلط الزّجاجيّ » (60) → « الجسم البلّوريّ » (15)
- `01-tamrin` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « منع العرق من النّزول إلى العين » (30) → « منع العرق من دخول العين » (23)
- `02-tamrin` Q1 — énoncé réécrit (doublon) ; clé raccourcie ; distracteurs étoffés/remplacés a,c,d ; explication retouchée — clé b : « مقلوبًا وأصغر » (13) → « عدسة لامّة » (10)
- `02-tamrin` Q2 — clé raccourcie ; distracteurs étoffés/remplacés a,b,d — clé c : « لأنّ الإبصار يحدث في المخّ، وهو الذي يفسّر الصّورتين في الاتّجاه الصّحيح » (72) → « لأنّ الإبصار يحدث في المخّ الذي يفسّر الصّورتين » (47)
- `02-tamrin` Q4 — clé raccourcie ; distracteurs étoffés/remplacés b,c — clé a : « اتّسعت الحدقة بحركة انعكاسيّة فدخل ضوء أكثر » (43) → « اتّسعت الحدقة بحركة انعكاسيّة لا إراديّة » (40)
- `02-tamrin` Q5 — clé retouchée ; distracteurs étoffés/remplacés a,c — clé b : « موضع ارتباط الشّبكيّة بالعصب البصريّ » (36) → « موضع اتّصال الشّبكيّة بالعصب البصريّ » (36)
- `03-boss` Q2 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « عدسات مفرّقة، لأنّها تبعّد نقطة التّجمّع فتردّها إلى الشّبكيّة » (62) → « عدسات مفرّقة، لأنّها تبعّد نقطة التّجمّع » (40)
- `03-boss` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,d — clé b : « التّسمية تصف المسافة التي يراها جيّدًا: قصير البصر يرى القريب جيّدًا ويصعب عليه البعيد » (86) → « قصير البصر يرى القريب جيّدًا ويصعب عليه البعيد » (46)
- `03-boss` Q5 — clé raccourcie ; distracteurs étoffés/remplacés c — clé a : « عبور الضّوء وتشكّل الخيال ← نشأة السّيالة بالشّبكيّة ← نقلها بالعصب البصريّ ← تحليلها بمراكز الإبصار » (100) → « عبور الضّوء ← نشأة السّيالة ← نقلها بالعصب ← تحليلها بالمخّ » (59)
- `03-boss` Q6 — énoncé réécrit (doublon) ; clé retouchée ; distracteurs étoffés/remplacés a,c,d ; explication retouchée — clé b : « في الجهة الخلفيّة » (17) → « فقدان الإبصار رغم سلامة العينين » (31)
- `04-defi` Q1 — distracteurs étoffés/remplacés a,b,d — clé c : « في مراكز الإبصار بالمخّ » (23) → « في مراكز الإبصار بالمخّ » (23)
- `04-defi` Q2 — distracteurs étoffés/remplacés b,c,d — clé a : « الأولى: عبور الضّوء وتشكّل الخيال » (33) → « الأولى: عبور الضّوء وتشكّل الخيال » (33)
- `04-defi` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « أنّه انقطاع في إحدى مراحل الإبصار الأربع، وموضع الانقطاع هو الذي يحدّد العلاج » (77) → « أنّه انقطاع في إحدى مراحل الإبصار الأربع » (40)
- `04-defi` Q4 — clé raccourcie — clé b : « قصر بصر، ويؤكّده قياس حدّة البصر على البعيد عند طبيب العيون » (59) → « قصر بصر، ويؤكّده قياس حدّة البصر للبعيد » (39)
- `04-defi` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « نقل العدوى بالإفرازات إلى إخوته، مع احتمال تعقّد المرض عنده بإصابة القرنيّة فيضرّ إبصاره » (88) → « عدوى إخوته بالإفرازات، وبلوغ المرض قرنيّته » (42)
- `04-defi` Q6 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « لأنّ العلاج يستوجب مضادّات حيويّة يصفها الطّبيب بعد عيادة، والقطرات المشتركة نفسها طريق للعدوى » (94) → « لأنّ العلاج يحتاج مضادّات حيويّة يصفها الطّبيب » (46)
- `05-tadrib` Q1 — clé raccourcie — clé b : « استمرار الصّلبة الشّفّاف في مقدّمة العين » (40) → « الصّلبة الشّفّافة في مقدّمة العين » (33)
- `05-tadrib` Q2 — clé raccourcie — clé a : « الفتحة التي تتوسّط القزحيّة » (27) → « الفتحة في وسط القزحيّة » (22)
- `05-tadrib` Q3 — distracteurs étoffés/remplacés a,d — clé b : « عدسة مرنة محدّبة الوجهين » (24) → « عدسة مرنة محدّبة الوجهين » (24)
- `05-tadrib` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « حركة انعكاسيّة تقي العين من الغبار والضّوء » (42) → « حركة انعكاسيّة تقي العين من الغبار » (34)
- `05-tadrib` Q6 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « يبطّن الجفنين ويغطّي الجزء الأبيض الأماميّ من العين » (51) → « يبطّن الجفنين ويغطّي مقدّمة العين » (33)
- `06-defi-concours` Q1 — clé retouchée ; distracteurs étoffés/remplacés a,c,d — clé b : « قصر بصر، تصحّحه عدسات مفرّقة » (28) → « قصر بصر، تصحّحه عدسات مفرّقة مقعّرة » (35)
- `06-defi-concours` Q2 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé a : « طول بصر: خيال القريب يتشكّل خلف الشّبكيّة، والبعيد يقع عليها » (60) → « طول بصر: خيال القريب يتشكّل خلف الشّبكيّة » (41)
- `06-defi-concours` Q3 — clé raccourcie ; distracteurs étoffés/remplacés c — clé a : « لأنّ القرنيّة أوّل وسط شفّاف يعبره الضّوء، فتعكّرها يمسّ تشكّل الخيال نفسه » (74) → « لأنّ القرنيّة أوّل وسط شفّاف يعبره الضّوء » (41)
- `06-defi-concours` Q4 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé b : « أنّ المسار انعكاسيّ ويمرّ بمركز عصبيّ يوجّه الأمر إلى القزحيّتين معًا » (69) → « أنّ المسار انعكاسيّ ويمرّ بمركز عصبيّ مشترك » (43)
- `06-defi-concours` Q5 — clé raccourcie ; distracteurs étoffés/remplacés b,c — clé a : « اليمنى: لا استجابة رغم سلامة الشّبكيّة؛ اليسرى: استجابة عاديّة » (62) → « اليمنى: لا استجابة؛ اليسرى: استجابة عاديّة » (42)
- `06-defi-concours` Q6 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « أنّ الآلة تحفظ الصّورة بينما العين لا تكتفي بالتّصوير: الإبصار يتمّ في المخّ الذي يفسّر الصّورتين ويصحّح اتّجاههما » (114) → « أنّ الإبصار يتمّ في المخّ لا في العين وحدها » (43)

_34 questions touchées._

### 03-wiratha

- `quiz` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé d : « المورّثة مقطع من الـ ADN محمول على الصبغيّ ومسؤول عن صفة » (56) → « المورّثة مقطع من الـ ADN محمول على الصبغيّ » (42)
- `quiz` Q4 — clé raccourcie ; distracteurs étoffés/remplacés b,c — clé a : « من جزيء الـ ADN الحامل للمورّثات » (32) → « من جزيء الـ ADN الطويل » (22)
- `quiz` Q6 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé b : « الأب، لأنّ النطفة تحمل إمّا X وإمّا Y بينما البويضة تحمل X دائمًا » (65) → « الأب، لأنّ النطفة X أو Y والبويضة X دائمًا » (42)
- `quiz` Q8 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « وجود ثلاث نسخ من الصبغيّ رقم 21 فيصبح العدد 47 » (46) → « وجود ثلاث نسخ من الصبغيّ رقم 21 » (31)
- `01-tamrin` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « النمط النووي (caryotype) » (24) → « النمط النووي للخليّة » (20)
- `01-tamrin` Q4 — clé raccourcie — clé c : « صبغيّ من الأب وصبغيّ من الأمّ » (29) → « صبغيّ من الأب وآخر من الأمّ » (27)
- `01-tamrin` Q6 — clé raccourcie ; distracteurs étoffés/remplacés c — clé b : « متلازمة داون (التثلّث الصبغي 21) » (32) → « متلازمة داون الصبغيّة » (21)
- `02-tamrin` Q1 — clé retouchée ; distracteurs étoffés/remplacés a,c,d — clé b : « الـ ADN » (7) → « جزيء الـ ADN » (12)
- `02-tamrin` Q2 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « مقطع من الـ ADN مسؤول عن صفة وراثية » (35) → « مقطع من الـ ADN مسؤول عن صفة » (28)
- `03-boss` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « كلّ منهما حامل للحليل المتنحّي (مهجّن) دون أن يكون مريضًا » (57) → « كلّ منهما حامل للحليل المتنحّي دون أن يمرض » (42)
- `03-boss` Q5 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « لأنّه يحمل المورّثات التي تحدّد الصفات وتُنسخ عند تكوين الخلايا » (63) → « لأنّه يحمل المورّثات التي تحدّد الصفات » (38)
- `03-boss` Q6 — énoncé réécrit (doublon) ; clé retouchée ; distracteurs étoffés/remplacés a ; explication retouchée — clé b : « ذكر عدد صبغيّاته 46 » (19) → « أنثى عدد صبغيّاتها 46 » (21)
- `04-defi` Q5 — clé raccourcie — clé a : « لأنّ الأمّ XX ولا تملك صبغيّ Y أصلًا » (36) → « لأنّ الأمّ XX ولا تملك Y أصلًا » (30)
- `05-tadrib` Q1 — énoncé réécrit (doublon) ; clé retouchée ; distracteurs étoffés/remplacés b,c,d ; explication retouchée — clé a : « في النواة » (9) → « حمل المورّثات المحدّدة للصفات » (29)
- `05-tadrib` Q3 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « نوع الصبغي الجنسي الذي تحمله النطفة (X أو Y) » (44) → « نوع الصبغي الجنسي الذي تحمله النطفة » (35)
- `05-tadrib` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,d — clé b : « أنّ كلًّا منهما هجين B//b يحمل الأليل المتنحّي » (46) → « أنّ كلًّا منهما هجين B//b يحمل b » (32)
- `05-tadrib` Q6 — clé raccourcie ; distracteurs étoffés/remplacés b,d — clé a : « لأنّه يخزّن المعلومات التي تحدّد الصفات وتنتقل عبر المورّثات إلى الأبناء » (72) → « لأنّه يخزّن المعلومات التي تحدّد الصفات » (39)
- `06-defi-concours` Q3 — clé raccourcie ; distracteurs étoffés/remplacés d — clé a : « 1/2 ; يحدّده الأب (نطفة تحمل X أو نطفة تحمل Y) » (46) → « 1/2 ; يحدّده الأب (نطفة X أو نطفة Y) » (36)
- `06-defi-concours` Q4 — distracteurs étoffés/remplacés d ; explication retouchée — clé a : « 1/16 » (4) → « 1/16 » (4)
- `06-defi-concours` Q5 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé a : « سائد (يظهر بوجود حليل واحد، فيلزم أن يكون أحد الأبوين مصابًا) » (61) → « سائد (يكفي حليل واحد فأحد الأبوين مصاب) » (39)
- `06-defi-concours` Q6 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « في المرض المتنحّي قد يكون الأبوان حاملَين سليمَين (A//a) فيُنجبان طفلًا مصابًا (a//a) باحتمال 1/4 » (97) → « قد يكون الأبوان حاملَين سليمَين فيُنجبان طفلًا مصابًا » (53)

_21 questions touchées._

### 04-al-hajiyat-al-ghithaiya

- `quiz` Q7 — clé raccourcie ; distracteurs étoffés/remplacés b,c — clé a : « لأنّ التّصنيف يقوم على الوظيفة: فهي تبني الأنسجة وتوفّر طاقة أيضا » (65) → « لأنّ التّصنيف وظيفيّ: تبني الأنسجة وتوفّر طاقة » (46)
- `quiz` Q8 — clé raccourcie ; distracteurs étoffés/remplacés a — clé b : « وجبته كافية كمّا لكنّها فقيرة كيفا في الحديد والبروتيدات والفيتامين B12 » (71) → « وجبته كافية كمّا لكنّها فقيرة كيفا في الحديد » (44)
- `quiz` Q9 — clé raccourcie ; distracteurs étoffés/remplacés a,b,d — clé c : « السنّ والجنس ودرجة النّشاط البدنيّ والحالة الفيزيولوجيّة » (56) → « السنّ والجنس والنّشاط والحالة الفيزيولوجيّة » (43)
- `quiz` Q10 — clé raccourcie ; distracteurs étoffés/remplacés b — clé c : « لا، لأنّ الشّرط الكمّي غير محقّق مهما كان تركيبها جيّدا » (55) → « لا، لأنّ الكمّ يفوق الحاجة رغم جودة التّركيب » (44)
- `01-tamrin` Q2 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « نسي التّسخين، وكاشف فهلنق لا يعطي راسبه الأحمر الآجريّ إلّا بالتّسخين » (69) → « نسي التّسخين، وفهلنق لا يعمل بدونه » (34)
- `01-tamrin` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « لأنّ التّصنيف بالوظيفة، والبروتيدات تبني الأنسجة وتعطي طاقة أيضًا » (65) → « لأنّ التّصنيف بالوظيفة، وهي تبني وتعطي طاقة » (43)
- `01-tamrin` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « ببقعة شافّة على الورق لا تختفي بالتّسخين » (40) → « ببقعة شافّة على الورق » (21)
- `02-tamrin` Q1 — énoncé réécrit (doublon) ; clé retouchée ; distracteurs étoffés/remplacés a,c,d ; explication retouchée — clé b : « 9 » (1) → « الدّهنيّات » (10)
- `02-tamrin` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « الطّاقة التي ترفع حرارة كغ من الماء بدرجة واحدة » (47) → « الطّاقة اللّازمة لرفع حرارة كغ ماء بدرجة واحدة » (46)
- `02-tamrin` Q5 — distracteurs étoffés/remplacés a — clé b : « لأنّها غير قابلة للاحتراق في الجسم » (34) → « لأنّها غير قابلة للاحتراق في الجسم » (34)
- `02-tamrin` Q6 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « السنّ، الجنس، النّشاط البدنيّ، الحالة الفيزيولوجيّة » (51) → « السنّ، الجنس، النّشاط، الحالة الفيزيولوجيّة » (43)
- `03-boss` Q1 — clé retouchée ; distracteurs étoffés/remplacés a,c,d — clé b : « الكُساح: نقص كلسيوم وفسفور وفيتامين D » (37) → « الكُساح: نقص الكلسيوم والفسفور وفيتامين D » (41)
- `03-boss` Q2 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « لأنّ الطّرفين يمرضان: الإفراط يعطي السّمنة، والافتقار يعطي الهزال؛ وقد يمرض من يأكل كثيرًا إن غابت مجموعة كاملة » (111) → « لأنّ من يأكل كثيرًا قد يمرض إن غابت عنه مجموعة غذائيّة » (54)
- `03-boss` Q3 — distracteurs étoffés/remplacés a,c,d — clé b : « البروتيدات والحديد وفيتامين B12 » (31) → « البروتيدات والحديد وفيتامين B12 » (31)
- `03-boss` Q4 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « أنّ في الغذاء مكوّنات ضروريّة بكمّيّات ضئيلة لا يصنعها الجسم، سمّاها فونك سنة 1911 فيتامينات » (92) → « أنّ الجسم يحتاج مكوّنات ضئيلة الكمّ لا يصنعها » (45)
- `03-boss` Q6 — clé raccourcie ; distracteurs étoffés/remplacés d — clé a : « توازن مائيّ؛ واختلاله يعني تجفّفًا إن نقص الدّخول أو احتباسًا إن نقص الخروج » (75) → « توازن مائيّ؛ واختلاله تجفّف أو احتباس » (37)
- `04-defi` Q1 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « لا: حاجته من 4000 إلى 5000 كيلو حريرة بسبب نشاطه البدنيّ الشّديد » (64) → « لا: حاجته من 4000 إلى 5000 كيلو حريرة » (37)
- `04-defi` Q2 — clé retouchée ; distracteurs étoffés/remplacés a,b,d — clé c : « الحالة الفيزيولوجيّة » (20) → « اختلاف الحالة الفيزيولوجيّة بينهما » (34)
- `04-defi` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « غير متوازنة: كلّها من المجموعة الطّاقيّة، ولا شيء فيها من البنّاءة ولا من الواقية » (81) → « غير متوازنة: كلّها من المجموعة الطّاقيّة وحدها » (46)
- `04-defi` Q4 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « يستنتج وجود جليكوز وغياب النّشا؛ ولا يستطيع أن يستنتج شيئًا عن البروتيدات والدّهنيّات والأملاح » (94) → « يستنتج وجود جليكوز وغياب النّشا، ولا شيء عن غيرهما » (50)
- `04-defi` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « السّمنة: لأنّ الطّاقة الدّاخلة تفوق المستهلكة فتُخزَّن » (54) → « السّمنة: لأنّ الطّاقة الدّاخلة تفوق المستهلكة » (45)
- `04-defi` Q6 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « نعم: السّكّريات نحو النّصف، والدّهنيّات نحو الثّلث، والبروتيدات نحو الخمس تقريبًا » (81) → « نعم: السّكّريات نصف والدّهنيّات ثلث والبروتيدات خمس » (51)
- `05-tadrib` Q1 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « نترات الفضّة، وتعطي راسبًا أبيض يسودّ في الضّوء » (47) → « نترات الفضّة، وتعطي راسبًا أبيض يسودّ بالضّوء » (45)
- `05-tadrib` Q3 — distracteurs étoffés/remplacés c,d — clé b : « البروتيدات وبعض الأملاح » (23) → « البروتيدات وبعض الأملاح » (23)
- `05-tadrib` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « الكيف (شيء من المجموعات الثّلاث) والكمّ (يوافق حاجة هذا الفرد) » (62) → « الكيف الجيّد والكمّ الموافق للحاجة » (34)
- `06-defi-concours` Q1 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé a : « بقي 600، ويُركَّب العشاء من المجموعات الثّلاث لا من الحلويات وحدها » (66) → « بقي 600، ويُركَّب العشاء من المجموعات الثّلاث » (45)
- `06-defi-concours` Q2 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « الكمّ الطّاقيّ مضمون فحُفظ الوزن، والكيف ناقص فتأخّر النّموّ وظهر الشّحوب: نقص في البنّاءة والواقية » (99) → « الكمّ مضمون فحُفظ الوزن، والكيف ناقص فتأخّر النّموّ » (51)
- `06-defi-concours` Q3 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « لأنّ النّتيجة السّالبة تنفي مكوّنها وحده، وقد يكون الغذاء غنيًّا بمكوّنات لم تُختبر » (83) → « لأنّ النّتيجة السّالبة تنفي مكوّنها وحده » (40)
- `06-defi-concours` Q4 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « أنّ السنّ والجنس لا يكفيان لتقدير الحاجة، وأنّ النّشاط البدنيّ عامل حاسم بمفرده » (79) → « أنّ السنّ والجنس لا يكفيان والنّشاط عامل حاسم » (45)
- `06-defi-concours` Q5 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « لأنّ الكلسيوم يبني عظام الجنين والحديد يدخل في الهيموغلوبين، وحاجة الأمّ ترتفع لأنّها تغذّي جسمين » (97) → « لأنّ الكلسيوم يبني عظام الجنين والحديد من الهيموغلوبين » (54)
- `06-defi-concours` Q6 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « الثّاني: 320 مقابل 270 كيلو حريرة، والدّرس أنّ الكتلة قد تغلب كثافة الغرام » (74) → « الثّاني: 320 مقابل 270 كيلو حريرة » (33)

_31 questions touchées._

### 04-zalazil

- `quiz` Q1 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « هزّة أرضية مفاجئة ناتجة عن تحرّر مفاجئ لطاقة في أعماق الأرض » (59) → « هزّة أرضية مفاجئة ناتجة عن تحرّر طاقة في الأعماق » (48)
- `quiz` Q2 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « البؤرة نقطة المنشأ في العمق، والمركز السطحي النقطة على السطح فوقها مباشرة » (73) → « البؤرة نقطة المنشأ في العمق، والمركز السطحي فوقها على السطح » (59)
- `quiz` Q6 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « الشدّة تقيس آثار الزلزال على السطح وتختلف من مكان لآخر، والمقدار يقيس الطاقة المحرَّرة وقيمته واحدة » (99) → « الشدّة تقيس الآثار وتتغيّر مكانيًّا، والمقدار يقيس الطاقة بقيمة واحدة » (69)
- `quiz` Q7 — clé raccourcie ; distracteurs étoffés/remplacés a,b,d — clé c : « حركة الصفائح التكتونية وانكسار الصخور على الفوالق عند حدودها » (60) → « حركة الصفائح التكتونية وانكسار الصخور عند حدودها » (48)
- `01-tamrin` Q1 — clé raccourcie ; distracteurs étoffés/remplacés b,d — clé a : « تحرّر مفاجئ لطاقة مخزّنة في صخور الأعماق » (40) → « تحرّر طاقة مخزّنة في صخور الأعماق » (33)
- `01-tamrin` Q2 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé b : « النقطة داخل الأرض التي تنطلق منها الموجات الزلزالية » (51) → « النقطة داخل الأرض التي تنطلق منها الموجات » (41)
- `01-tamrin` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,b,d — clé c : « النقطة على سطح الأرض الواقعة عموديًّا فوق البؤرة مباشرة » (55) → « النقطة على السطح فوق البؤرة مباشرة » (34)
- `01-tamrin` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,d — clé b : « لأنّها الأقرب إلى البؤرة فتصلها الموجات أقوى » (44) → « لأنّها الأقرب إلى البؤرة فتصلها الموجات » (39)
- `01-tamrin` Q6 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « الزلزال يحرّر طاقة تنتقل على شكل موجات زلزالية تُحدث الاهتزاز » (61) → « الزلزال يحرّر طاقة تنتقل على شكل موجات زلزالية » (46)
- `02-tamrin` Q2 — clé raccourcie ; distracteurs étoffés/remplacés c — clé a : « المخطّط الزلزالي (sismogramme) » (30) → « المخطّط الزلزالي » (16)
- `02-tamrin` Q3 — clé raccourcie — clé b : « من فرق زمن وصول الموجات P و S المسجَّل في المراصد » (49) → « من فرق زمن وصول الموجات P و S » (29)
- `02-tamrin` Q4 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé b : « تقيس آثار الزلزال على السطح وتختلف من مكان إلى آخر » (50) → « تقيس آثار الزلزال على السطح وتختلف مكانيًّا » (43)
- `02-tamrin` Q5 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « يقيس الطاقة المحرَّرة عند البؤرة وله قيمة واحدة للزلزال الواحد » (62) → « يقيس الطاقة المحرَّرة عند البؤرة وله قيمة واحدة » (47)
- `02-tamrin` Q6 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé b : « المقدار، لأنّه يقيس الطاقة المحرَّرة عند البؤرة » (47) → « المقدار، لأنّه يقيس الطاقة عند البؤرة » (37)
- `03-boss` Q1 — clé raccourcie ; distracteurs étoffés/remplacés d — clé b : « تنكسر الصخور فجأة على مستوى فالق فتتحرّر الطاقة المخزّنة دفعةً واحدة » (68) → « تنكسر الصخور فجأة على مستوى فالق » (32)
- `03-boss` Q3 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d — clé b : « كسر في الصخور يحدث على طوله انزلاق مفاجئ يحرّر الطاقة » (53) → « كسر في الصخور يحدث على طوله انزلاق مفاجئ » (40)
- `03-boss` Q4 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé b : « لأنّها قريبة من منطقة التقاء الصفائح في حوض البحر الأبيض المتوسّط » (65) → « لأنّها قريبة من منطقة التقاء الصفائح » (36)
- `03-boss` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a,c,d ; explication retouchée — clé b : « حركة الصفائح ← تراكم الضغوط ← انكسار الصخور على فالق ← تحرّر الطاقة وموجات زلزالية » (82) → « حركة الصفائح ← تراكم الضغوط ← انكسار الصخور ← تحرّر الطاقة » (58)
- `03-boss` Q6 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé b : « اختلاف الشدّة بسبب عمق البؤرة وقرب العمران ونوع التربة وجودة البناء » (67) → « اختلاف الشدّة بحسب العمق والعمران والتربة والبناء » (49)
- `04-defi` Q2 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « تسونامي (موجات بحرية عملاقة) » (28) → « تسونامي: موجات بحرية كبيرة » (26)
- `04-defi` Q3 — clé raccourcie ; distracteurs étoffés/remplacés b,c — clé a : « تشييد مبانٍ مقاومة للزلازل وفق معايير مضادّة للهزّات » (52) → « بناء مبانٍ مقاومة للزلازل وفق معايير خاصّة » (42)
- `04-defi` Q4 — distracteurs étoffés/remplacés a,c,d — clé b : « الاحتماء تحت طاولة متينة والابتعاد عن النوافذ » (45) → « الاحتماء تحت طاولة متينة والابتعاد عن النوافذ » (45)
- `04-defi` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a — clé b : « المقدار قيمة واحدة (الطاقة عند البؤرة)، بينما تختلف الشدّة من مدينة لأخرى حسب الآثار » (84) → « المقدار قيمة واحدة، وتختلف الشدّة من مدينة لأخرى » (48)
- `04-defi` Q6 — clé raccourcie ; distracteurs étoffés/remplacés a,c — clé b : « لأنّها تحدّد مواقع الزلازل وتراقب النشاط الزلزالي فتدعم الإنذار المبكّر وخرائط المخاطر » (86) → « لأنّها تحدّد مواقع الزلازل فتدعم الإنذار المبكّر » (48)
- `05-tadrib` Q1 — énoncé réécrit (doublon) ; clé raccourcie ; distracteurs étoffés/remplacés b,c,d ; explication retouchée — clé a : « النقطة في باطن الأرض التي ينطلق منها الزلزال » (44) → « البؤرة الزلزالية » (16)
- `05-tadrib` Q2 — clé raccourcie ; distracteurs étoffés/remplacés c,d — clé a : « المرصاد الزلزالي (le sismographe) » (33) → « المرصاد الزلزالي » (16)
- `05-tadrib` Q3 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « المقدار يعبّر عن الطاقة المحرَّرة عند البؤرة، والشدّة تعبّر عن آثار الزلزال على المكان » (86) → « المقدار يقيس الطاقة المحرَّرة، والشدّة تقيس الآثار » (50)
- `05-tadrib` Q4 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « تحرّك الصفائح التكتونية وتراكم الإجهادات في الصخور ثمّ تكسّرها فجأةً » (68) → « تحرّك الصفائح التكتونية وتكسّر الصخور فجأةً » (43)
- `05-tadrib` Q5 — clé raccourcie ; distracteurs étoffés/remplacés a — clé b : « اختلاف عمق البؤرة وقرب المركز السطحي من العمران ونوع المباني والتربة » (68) → « اختلاف عمق البؤرة وقرب العمران ونوع التربة » (42)
- `05-tadrib` Q6 — clé raccourcie ; distracteurs étoffés/remplacés d — clé a : « الاحتماء تحت طاولة متينة بعيدًا عن النوافذ والابتعاد عن الأشياء التي قد تسقط » (76) → « الاحتماء تحت طاولة متينة بعيدًا عن النوافذ » (42)
- `06-defi-concours` Q1 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « البؤرة نقطة انطلاق الزلزال في العمق ; المركز السطحيّ إسقاطها عموديًّا على سطح الأرض » (83) → « البؤرة في العمق ; المركز السطحيّ إسقاطها على السطح » (50)
- `06-defi-concours` Q5 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d ; explication retouchée — clé a : « (أ)، لأنّ الزلازل تتركّز أساسًا عند حدود الصفائح حيث تحتكّ وتتحرّك » (66) → « (أ)، لأنّ الزلازل تتركّز عند حدود الصفائح » (41)
- `06-defi-concours` Q6 — clé raccourcie ; distracteurs étoffés/remplacés b,c,d — clé a : « عدد الضحايا يتعلّق بالشدّة المحلّية وكثافة السكّان ومتانة البناء وساعة الوقوع، لا بالمقدار وحده » (95) → « الضحايا يتعلّقون بالشدّة وكثافة السكّان ومتانة البناء » (53)

_33 questions touchées._

## Suites appliquées (audit-01-04.md)

Tous les MAJOR et MINOR de l'audit sont appliqués (patch `patches/p_audit.py`, `p_fix9.py`), dossiers 01-04 uniquement,
`cours.md` intact. Chaque texte de l'auditeur a été revérifié contre le `cours.md` et le dossier entier (faits enseignés :
cycle sismique, ondes S, alerte précoce, kyste/pus, soi/non-soi, allèles, autosomes, cervelet « خلف المخ », tache aveugle, etc.).

- **Clés inexactes / incomplètes / tautologiques** : 01-takathur `03-boss` Q5, `04-defi` Q3, 04-hajiyat quiz Q10 et `06` Q6 (énoncé raccourci),
  04-zalazil `01-tamrin` Q5, 02-af3al `03-boss` Q1 (plus de guillemets) — appliqués.
- **Doublons réécrits (clé au même id, étiquettes ajustées)** : 01-takathur `02-tamrin` Q3 (nombre d'ovules par cycle), Q4 (durée de la grossesse),
  `05-tadrib` Q5 (date des règles suivantes) ; 01-wadhifat `02-tamrin` Q3, `06` Q6 ; 02-af3al `02-tamrin` Q1, Q2, Q5 ; 02-manaa `05-tadrib` Q1, Q5,
  `06` Q2, Q4, `03-boss` Q6 ; 03-al-ibsar `01-tamrin` Q1, Q2 (difficulté 2), `02-tamrin` Q2, `03-boss` Q6 ; 03-wiratha `05-tadrib` Q1, Q3, Q5, Q6, `02-tamrin` Q1 ;
  04-hajiyat `01-tamrin` Q4, `02-tamrin` Q6 ; 04-zalazil `06` Q1, `05-tadrib` Q3, Q4, Q5, Q6, `04-defi` Q3. Plus, mes propres ajouts hors liste :
  01-wadhifat `01-tamrin` Q6 (cervelet), 04-hajiyat `02-tamrin` Q1 (« مكوّن غذائيّ ») et Q3 (120 g / 40 g, quiz Q5 ↔ Q3).
- **Indices de forme** : 01-takathur quiz Q7 (noms nus, plus de parenthèse ni glose), 01-wadhifat `01-tamrin` Q3 (tanwīn), 04-hajiyat `05-tadrib` Q5
  (tous à deux termes), 03-wiratha quiz Q4 (clé sans « ADN » : le « ADN » n'apparaît plus que dans l'explication).
- **Notion absente du cours** : 02-af3al `06` Q4 (freinage du réflexe) récrite sur le réflexe du dormeur chatouillé (verifie du cours), sans toucher au cours.
- **Divergences avec l'auditeur (texte corrigé avant écriture)** :
  - 01-takathur `04-defi` Q3 : « كي لا يختلّ… » donnait une clé à l'amorce unique (« كي ») ; remplacée par « لأنّ دخول نطفتين يُفسد عدد الصبغيّات » (même sens, amorce « لأنّ »).
  - 03-wiratha quiz Q4 : sa suggestion « من البروتينات وحدها بلا ADN » emploie une notion absente du cours (protéines) ; j'ai plutôt retiré « ADN » de la clé.
  - 03-al-ibsar `03-boss` Q6 : sa version recréait une paire (0,54) avec quiz Q8 (mêmes quatre étapes) ; options changées en éléments (« مستقبلات الشّبكيّة », « العصب البصريّ »…).
  - 02-af3al `06` Q4 : options du dormeur chatouillé écrites par moi (les distracteurs b/d plus longs que la clé) ; explication en phrases complètes.
  - 02-af3al quiz Q1 et 01-takathur `06-defi-concours` Q6 : expl. refaite en phrase complète (« وبلا منبّه لا يحدث أيّ فعل انعكاسيّ »).
- **Défauts préexistants signalés** : 01-wadhifat quiz Q5 d, 01-takathur `04-defi` Q2 (b/d), 04-hajiyat `04-defi` Q2 b, ADN 03-wiratha — corrigés. Position de la clé : toujours hors mandat.
- **Laissés (acceptés par l'auditeur)** : 01-takathur `04-defi` Q1 ↔ `06` Q2 ; 03-al-ibsar quiz Q7 ↔ `03-boss` Q1 (0,50) ; 04-hajiyat `01-tamrin` Q1 ↔ `05-tadrib` Q1 et `03-boss` Q5 ↔ `05-tadrib` Q6 ; 03-wiratha `03-boss` Q6 ↔ 07-annales.
  Notions hors cours (LH / corps jaune, 01-takathur `06` Q1/Q3) : signalées, non traitées (cohérence d'ordre de chapitres).

Vérifications finales : `content:check` 0 erreur ; `qa:strict` 0 erreur (1 avertissement hors périmètre, 07-annales sans domaine) ;
`tranche` 01-04 : 0/90, 0/99, 0/105, 0/90 en « clé la plus longue » ; paires restantes : 1, 0, 1, 2 (toutes justifiées) ; Prettier `--check` vert.
