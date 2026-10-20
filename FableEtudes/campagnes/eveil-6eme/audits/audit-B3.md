# Audit B3 — `04-nutrition` · `06-reproduction-florale` · `05-milieu-chaines-alimentaires`

Auditeur indépendant (opus), 2026-10-20, branche `wip/eveil-6eme-un-passage` (commit `33a161ec`).
Lus en entier avant l'audit : `content-audit`, `course-quality.md`, `course-explanation.md`,
`quality-bar.md`, `prof-eveil-primaire`, fiche `6eme-base/eveil.md` (§1.7, §2 unités 3–4, §4 bis,
§6.0–6.1, §7.23–7.25, §7.31–7.42), PLAN § 3 (V1–V5). Manuel `103604` relu **à l'image** p.84–95,
101–107, 110–117 ; guide `503604` p.128–129. Re-résolution à l'aveugle faite AVANT la lecture des
notes et du rapport de l'auteur.

**Questions re-résolues : 133** (04 : 46 · 05 : 42 · 06 : 45). **Aucune clé fausse, aucune
double réponse, aucune science fausse** dans les items. Les 24 sections de cours sont au patron
(ancrage → définition → tableau/figure + phrase-pont → exemple → piège → règle + cas limite →
`verifie` → `retenir`) ; chaque exemple, piège et `verifie` a été recalculé : tous justes
(36 kg → 24 kg, 45 kg → 30 kg, 5 graines → 5 ovules / 5 grains de pollen, rangs des
consommateurs).

## Gates

| gate | résultat |
| --- | --- |
| `content:check` | ✓ 121 sujets valides |
| `content:qa -- --subject eveil-scientifique-6eme` | ✓ aucun signalement |
| `content:figures:check` | ✓ |
| `content:tranche … --chapters 04,05,06 --fresh --strict-longest --strict-lessons` | ✓ 0/20 clé la plus longue · 0 paire proche · 0 recul de patron. Mesure complète (133 q., hors `--fresh`) : **0** clé strictement la plus longue |
| chiffres arabo-indiens / `\d \d{3}` hors SVG | 0 |
| rendu `renderLesson`/`renderSummary` + Chromium 360 px | 6 pages, `scrollWidth` = 360 (aucun défilement horizontal), 21 tableaux ≤ 344 px, 5 figures de cours + 3 figures d'items lisibles et justes (fleur, cycle, chaîne, station, groupes ; items 06/01 Q7, 06/02 Q7, 05/03 Q6). Fichiers jetables supprimés. |

## Points d'arbitrage vérifiés

- **V1** : le seul chiffre exigé est « الماء = ثلثا كتلة الجسم » (manuel p.86 5-ب, autorisé §4 bis). ✓
- **V4** : le cours enseigne « إزالة الشوائب ثمّ قتل الجراثيم » et montre la station en schéma ; seule
  question sur la station : `05/03-revision Q6`, **lecture pure** du schéma fourni (rendu vérifié :
  les six cases et les flèches portent la réponse). Conforme au texte du PLAN. ✓
- **Erreurs du manuel/guide non reprises** : sens de la flèche « يتغذّى على » (vers la nourriture —
  vérifié p.110–111 à 250 dpi), « الهزال الرزّي » jamais clé, six groupes jamais clé, vitamine D
  « يكسب مناعة » absente. ✓
- **`coursePitfalls`** : 7 + 8 + 6 tags, chacun montré dans un `::: piege` ET porté par au moins un
  distracteur. ✓
- **Reprises (`manuel`) confrontées au PDF** : 05/01 p.112 1-ب ✓ (mêmes 4 organismes) · 05/04 p.117 7-أ ✓
  · 05/05 p.117 7-ب ✓ (« ومحطّات توليد الكهرباء » coupé) · 04/05 p.95 6-أ ✓ (« وقصر القامة » coupé) ·
  06/02 p.103 أقيّم 7 ✓ · **04/02 p.128 1-أ ✗** et **06/03 p.106 6-أ ✗** (voir M-14, M-15).
- **Faits du manuel vérifiés** (pas d'erreur) : signe du diabète « عدم التئام الجروح بسرعة », vit. A →
  ضعف البصر, fer → فقر الدم (p.94–95) ; ثمرة كاذبة (p.107 معجمي) ; مدّخرات الجنين (p.106 6-ب) ; Javel
  dans l'eau du robinet (p.114 7-ب) ; diagnostic par analyse des selles (p.117 6-3) ; symptômes des
  trois maladies (p.116).

---

## Défauts

Aucun **critique**. Les remplacements ci-dessous sont vérifiés : une seule réponse, clé jamais
strictement la plus longue (longueurs mesurées), aucune fuite, étiquette = erreur exécutée.

### MAJEURS

#### M-1 à M-12 — questions qui redonnent un exemple ou un `verifie` résolu du cours

La consigne l'interdit : l'élève qui a lu le cours lit la réponse au lieu de raisonner. Chaque
remplacement garde le rang, la difficulté et l'id de clé.

**M-1 · `04-nutrition/exercices/02-boss.json` Q4** (= exemple « ماذا نقص وجبة سامي؟ », même
bouchée œuf + eau).
- prompt : `عدّاءة تناولت قبل السباق قطعة جبن وتفّاحة فقط، فتعبت قبل خطّ الوصول بكثير. ما التفسير الأقرب؟`
- options : a `خلت وجبتها من أغذية الطاقة` (clé) · b `خلت وجبتها من أغذية البناء` · c `خلت وجبتها من أغذية الوقاية` · d `تناولت وجبة متوازنة تمامًا` (26/26/27/26)
- explanation : `الجبن من أغذية البناء، والتفّاحة من أغذية الوقاية، لكنّ أغذية الطاقة غابت، وهي الّتي يتحرّك بها الجسم، فتعبت العدّاءة. ولا يصحّ القول إنّ وجبتها خلت من البناء أو من الوقاية، ووجبة تغيب عنها مجموعة ليست متوازنة.`

**M-2 · `04-nutrition/exercices/03-revision.json` Q4** (= `verifie` « لحم مشويّ وجزر مسلوق وتفّاحة », mot pour mot).
- prompt : `وجبة: أرز بالخضر وخبز وبرتقالة. ماذا ينقصها لتكون متوازنة؟`
- options : a `أغذية الطاقة كالبطاطا` · b `أغذية البناء كالبيض` (clé) · c `أغذية الوقاية كالتفّاح` · d `لا ينقصها أيّ غذاء` (21/19/22/18)
- explanation : `الأرز والخبز من أغذية الطاقة، والخضر والبرتقالة من أغذية الوقاية، لكن لا يوجد فيها غذاء للبناء. فنضيف بيضًا أو لحمًا أو عدسًا لتجتمع المجموعات الثلاث.`

**M-3 · `04-nutrition/exercices/04-defi.json` Q1** (= `verifie` du rachitisme, mot pour mot).
- prompt : `طفل لا يشرب الحليب ولا يأكل مشتقّاته، فصارت عظامه ليّنة وساقاه مقوّستين. ما المرض المحتمل؟`
- options inchangées (clé c `الكساح`).
- explanation : `ليونة العظام وتقوّس الساقين من علامات الكساح، وسببه نقص الفيتامين «د» أو أملاح الكالسيوم والفسفور الموجودة في الحليب ومشتقّاته. أمّا الإسقربوط فعلامته انتفاخ اللثّة ونزفها، وفقر الدم سببه نقص الحديد.`

**M-4 · `04-nutrition/exercices/04-defi.json` Q4** (= `verifie` « طفلان: الأوّل يأكل الحلويات… »).
- prompt : `أختان: سلمى تأكل الخبز والمقرونة بكثرة وتقضي يومها جالسة، ومريم لا تأكل إلّا لقيمات قليلة فنحفت كثيرًا. أيّ عبارة صحيحة؟`
- options : a `كلتاهما في حالة سوء تغذية` (clé) · b `سلمى وحدها في حالة سوء تغذية` · c `مريم وحدها في حالة سوء تغذية` (tag `eveil.nutri.malnutrition-seulement-par-manque`) · d `ولا واحدة منهما في حالة سوء تغذية` (25/28/28/33)
- explanation : `سوء التغذية يكون بالنقص أو بالإفراط: سلمى أفرطت في أغذية الطاقة مع قلّة النشاط فتهدّدها السمنة، ومريم نقصها الغذاء فيهدّدها الهزال. الخطأ الشائع أن نظنّ سوء التغذية قلّة أكل فقط.`

**M-5 · `04-nutrition/exercices/03-revision.json` Q8** (≈ exemple « بائع الأكلة الخفيفة » : pain, œuf, légume, à découvert).
- prompt : `في حفلة مدرسيّة، بقيت صحون كسكسي باللحم والخضر مكشوفة تحت الشمس من الصباح إلى المساء، والذباب يحوم حولها. أيّ عبارة صحيحة؟`
- options inchangées (clé b `الوجبة متوازنة لكنّها غير سليمة`).
- explanation : `في الكسكسي باللحم والخضر غذاء من كلّ مجموعة: اللحم للبناء، والكسكسي للطاقة، والخضر للوقاية، فهو متوازن. لكنّه بقي مكشوفًا ساعات طويلة، والذباب ينقل الجراثيم والحرارة تساعدها على التكاثر، فهو غير سليم. التغذية السليمة توازن ونظافة معًا.`

**M-6 · `05-milieu…/quiz.json` Q3** (= ligne du tableau « الإنسان ← الخروف ← العشب الأخضر »).
- prompt : `في السلسلة: الإنسان ← الدجاجة ← حبوب القمح، الإنسان مستهلك من الدرجة:`
- options inchangées (clé b `الثانية`, c taguée inchangée).
- explanation : `نعدّ من النبات: حبوب القمح منتج، والدجاجة تتغذّى عليها فهي من الدرجة الأولى، والإنسان يتغذّى على الدجاجة فهو من الدرجة الثانية. لا نعدّ الإنسان من الدرجة الثالثة لمجرّد أنّه في رأس السلسلة.`

**M-7 · `05-milieu…/quiz.json` Q6** (= exemple « مبيد يقتل العوالق الحيوانيّة », même chaîne, même question).
- prompt : `في السلسلة: البطّة ← السمكة الصغيرة ← العوالق الحيوانيّة ← العوالق النباتيّة، ماتت الأسماك الصغيرة كلّها. من يفقد غذاءه مباشرةً؟`
- options : a `العوالق النباتيّة الّتي تصنع غذاءها` · b `البطّة الّتي تتغذّى على السمكة الصغيرة` (clé) · c `العوالق الحيوانيّة الّتي تتغذّى على النباتيّة` · d `لا أحد، فالسمكة الصغيرة لا يأكلها أحد` (35/38/45/37)
- explanation : `البطّة تتغذّى على السمكة الصغيرة، فهي الّتي تفقد غذاءها مباشرةً. أمّا العوالق الحيوانيّة فلم تعد تأكلها الأسماك الصغيرة فقد تكثر، والعوالق النباتيّة منتجة تصنع غذاءها. وغياب حلقة يؤثّر في السلسلة كلّها.`

**M-8 · `05-milieu…/exercices/02-boss.json` Q1, Q2, Q4, Q6, Q7** — cinq items du boss qui redonnent le cours
(Q1 = `verifie` أفعى/فأر/ذرة ; Q2 = `verifie` عقاب/حمامة/بذور ; Q4 = `verifie` fève au placard, mot pour mot ;
Q6 = ancrage et exemple « سامي : خبز القمح ثمّ لحم الخروف » ; Q7 = ancrage et tableau جراد/أرنب/ثعلب).
- **Q1** prompt : `في السلسلة: القنفذ ← الحلزون ← الخسّ، على ماذا يتغذّى الحلزون؟` · options a `على القنفذ` (tag fleche inchangé) · b `على الخسّ` (clé) · c `على القنفذ والخسّ` · d `لا يتغذّى على شيء` · explanation : `السهم يُقرأ «يتغذّى على»: السهم الخارج من الحلزون يتّجه نحو الخسّ، فالحلزون يتغذّى على الخسّ ✓. الخطأ الشائع أن نقرأ السهم بالعكس فنظنّ أنّ الحلزون يأكل القنفذ، والحقيقة أنّ القنفذ هو الّذي يتغذّى على الحلزون.`
- **Q2** options : a `القمح ← الفأر ← البومة` (tag fleche) · b `الفأر ← البومة ← القمح` · c `البومة ← القمح ← الفأر` · d `البومة ← الفأر ← القمح` (clé) · explanation : `البومة تتغذّى على الفأر، والفأر يتغذّى على حبوب القمح، والسهم يتّجه دائمًا نحو الغذاء: البومة ← الفأر ← القمح ✓، وتنتهي الأسهم عند النبات. الخطأ الشائع هو القمح ← الفأر ← البومة: رتّب الكائنات جيّدًا لكنّه قلب اتّجاه الأسهم.`
- **Q4** prompt : `نبتتا فاصوليا متشابهتان في أصيصين بالتربة نفسها، وسُقيتا بالماء نفسه: وُضعت الأولى قرب النافذة، والثانية في قبو مظلم. بعد أسبوعين ذبلت الثانية وحدها. لماذا؟` · options a `لأنّها تحتاج الضوء لتصنع غذاءها` (clé) · b `لأنّ السقي يكفيها، فذبولها من مرض أصابها` (tag `eveil.eco.plante-sans-lumiere` — exécute « l'eau suffit ») · c `لأنّ الفطر يأكلها حين يغيب الضوء` · d `لأنّ الظلام يمنع الجذور من امتصاص الماء` (31/40/32/39) · explanation : `النبات الأخضر منتج يصنع المادّة العضويّة بمساعدة ضوء الشمس، والنبتتان سُقيتا بالماء نفسه في التربة نفسها، فالفرق الوحيد بينهما هو الضوء ✓. في القبو لا ضوء، فتوقّفت الثانية عن صنع غذائها وذبلت. الخطأ الشائع أن نظنّ أنّ الماء يكفي النبات، وهو لا يعوّض الضوء.` *(corrige aussi l'ancien d « الماء ينقصها », contredit par l'énoncé et mal étiqueté.)*
- **Q6** prompt : `تأكل ليلى في الغداء سلطة طماطم، وفي العشاء سمكة صغيرة تغذّت على الطحالب. ما درجتها مستهلكةً في السلسلتين؟` · options inchangées (clé a `الأولى ثمّ الثانية`) · explanation : `في الغداء: ليلى ← الطماطم، والطماطم نبات، فليلى من الدرجة الأولى. في العشاء: ليلى ← السمكة ← الطحالب، والسمكة تتغذّى على النبات فهي من الدرجة الأولى، فليلى من الدرجة الثانية ✓. الخطأ الشائع أن نجعل الإنسان من الدرجة الثالثة دائمًا لأنّه في رأس السلسلة، والدرجة تُحسب من غذائه في كلّ سلسلة.`
- **Q7** prompt : `في السلسلة: العصفور ← الجرادة ← العشب الأخضر، أصاب الجفاف الحقل فيبس العشب كلّه. ماذا يحدث للجرادة وللعصفور؟` · options a `العصفور وحده يتأثّر، لأنّه في رأس السلسلة` · b `لا يتأثّران، لأنّ العصفور لا يأكل العشب مباشرةً` · c `الجرادة تفقد غذاءها، ثمّ يفقد العصفور غذاءه` (clé) · d `الجرادة لا تتأثّر، لأنّها تتغذّى على العصفور` (tag `eveil.eco.fleche-lue-a-l-envers`) (41/47/43/44) · explanation : `الجرادة تتغذّى على العشب، فإذا يبس العشب فقدت غذاءها، والعصفور يتغذّى على الجرادة فيفقد غذاءه بدوره ولو لم يأكل العشب. فغياب حلقة واحدة يؤثّر في السلسلة كلّها، والسهم يُقرأ «يتغذّى على»: الجرادة لا تأكل العصفور.`

**M-9 · `05-milieu…/exercices/03-revision.json` Q5** (= exemple « ماء البئر القريبة من مصبّ الفضلات »).
- prompt : `في رحلة، وجد التلاميذ عينًا ماؤها صافٍ جدًّا، لكنّ قطيع ماعز يشرب ويرعى حولها. هل ماؤها صالح للشرب؟`
- options : a `نعم، لأنّ ماءها صافٍ تمامًا` (tag eau-limpide inchangé) · b `نعم، لأنّ ماء العيون لا يتلوّث أبدًا` · c `ليس حتمًا، ففيه جراثيم قد لا تُرى` (clé) · d `لا، لأنّ ماء العيون لا يُشرب أبدًا` (27/36/33/34)
- explanation : `الجراثيم لا تُرى بالعين، وفضلات القطيع قد تحملها إلى ماء العين، فقد يكون الماء صافيًا وملوّثًا معًا. لذلك نغليه أو نعقّمه قبل شربه. الصفاء وحده لا يدلّ على أنّ الماء صالح للشرب.`

**M-10 · `05-milieu…/exercices/04-defi.json` Q2 et Q7** (Q2 = exemple « خضر سُقيت بمياه مستعملة » ; Q7 = `verifie` des inondations).
- **Q2** prompt : `أكل طفل حلوى مكشوفة كان الذباب يحطّ عليها قرب مكبّ للفضلات، ثمّ أحسّ بحمّى وصداع وآلام في الأمعاء. ما مرضه وكيف انتقلت العدوى؟` · options a `الكوليرا، عبر الذباب الناقل للجراثيم` · b `الحمّى التيفيّة، عبر الذباب الناقل للجراثيم` (clé) · c `البوصفّير، عبر الذباب الناقل للجراثيم` · d `الحمّى التيفيّة، ولا عدوى لأنّه لم يشرب ماءً ملوّثًا` (tag eau-polluee inchangé) (36/43/37/52) · explanation : `الحمّى والصداع وآلام الأمعاء أعراض الحمّى التيفيّة، والذباب ينقل جرثومتها من الفضلات إلى الطعام المكشوف ✓. الخطأ الشائع أن نظنّ أنّ الماء الملوّث لا يُمرض إلّا من يشربه، والذباب والخضر الملوّثة تنقل الجرثومة أيضًا.` (manuel p.116 : le الذباب transmet la typhoïde.)
- **Q7** prompt : `بعد أمطار غزيرة صار ماء الماجل عكرًا، فتركه الجدّ ساكنًا حتّى صفا. لماذا ينصح الطبيب بعدم شربه قبل تعقيمه؟` · options a `لأنّ التعقيم يزيل الأتربة الّتي بقيت في الماء الصافي` · b `لأنّ الترسيب يكفي، والطبيب يبالغ في الحذر` (tag `eveil.eco.eau-limpide-donc-potable` — exécute « limpide donc potable ») · c `لأنّ السيول جرفت فضلات وجراثيم إلى الماجل والجراثيم لا تُرى` (clé) · d `لأنّ الماء الّذي وصلته الأمطار لا يصلح للشرب أبدًا مهما كان` (52/41/59/59) · explanation : `السيول تجرف الفضلات والأوساخ إلى المواجل، وترك الماء ساكنًا يزيل الشوائب فيصفو، لكنّه لا يقتل الجراثيم الّتي لا تُرى. لذلك نعقّمه قبل شربه. والتعقيم يقتل الجراثيم ولا يزيل الأتربة، ومياه الأمطار نفسها نظيفة.` *(corrige aussi l'ancien b « الماء الصافي فيه جراثيم أكثر… », qui exécutait l'erreur INVERSE de son étiquette.)*

**M-11 · `05-milieu…/exercices/05-entrainement.json` Q6** (= `verifie` du choléra, mêmes trois symptômes).
- prompt : `انتشر في قرية مرض بعد أن اختلطت مياه المجاري بماء البئر، ومن أعراضه تقيّؤ وإسهال متكرّر مع آلام في الأطراف. ما المرض وما سببه؟`
- options inchangées (clé d `الكوليرا، وسببها جرثومة`).
- explanation : `التقيّؤ والإسهال مع آلام الأطراف أعراض الكوليرا، وسببها جرثومة تعيش في الجهاز الهضميّ للمريض وتخرج مع برازه، فلوّثت مياه المجاري البئر ✓. الخطأ الشائع أن نجعل سببها فيروسًا، والفيروس سبب البوصفّير وحده.`

**M-12 · `06-reproduction-florale/exercices/02-boss.json` Q4, Q6, Q8 et `04-defi.json` Q3**
(Q4 = exemple du sachet, ET doublon de Q7 — la reprise p.103 — dans le même exercice ; Q6 = `verifie` citronnier/insecte ; Q8 = 4ᵉ pas de l'exemple « النخيل » mot pour mot ; défi Q3 = cas limite « طلع تفّاح على ميسم برتقال » de la `methode`).
- **boss Q4** prompt : `في تجربة، قطع باحث مياسم كلّ أزهار غصن من شجرة مشمش قبل تفتّحها، وترك باقي أجزائها. ماذا يحدث لمبايض هذه الأزهار؟` · options a `تتحوّل إلى ثمار كالعادة` (tag fruit-sans-pollinisation) · b `تتحوّل إلى حبّات طلع` · c `لا تتحوّل إلى ثمار` (clé) · d `تتحوّل كلّ منها إلى بذرة واحدة` (23/20/18/30) · explanation : `حبّات الطّلع تحطّ على الميسم، فإذا قُطع الميسم لم يجد الطّلع مكانًا يحطّ عليه: لا تأبير، فلا إخصاب، فلا تتحوّل المبايض إلى ثمار. والبويضات هي الّتي تصير بذورًا بعد الإخصاب، لا المبيض.`
- **boss Q6** prompt : `حملت الرّياح حبّات طلع من سنبلة قمح إلى ميسم زهرة في سنبلة قمح أخرى. ما صنف هذا التّأبير؟` · options inchangées (clé d `تأبير خلطيّ` ; le tag de a `type-pollinisation-par-l-agent` devient juste : « sans insecte donc ذاتيّ ») · explanation : `الطّلع انتقل إلى ميسم زهرة أخرى من نفس النّوع، فهو تأبير خلطيّ ولو لم تنقله حشرة: الصّنف تقرّره الزّهرتان لا الوسيلة. الخطأ الشائع أن نظنّ التّأبير ذاتيًّا لأنّه حدث دون حشرة.`
- **boss Q8** prompt : `في حقل تجارب، نقل باحث بفرشاة صغيرة حبّات طلع من زهرة طماطم إلى ميسم زهرة طماطم في نبتة أخرى. ما صنف هذا التّأبير؟ وما وسيلته؟` · options a `تأبير خلطيّ، ووسيلته الإنسان الّذي نقل الطّلع بين نبتتين` (clé) · b `تأبير ذاتيّ، ووسيلته الإنسان الّذي نقل الطّلع بين زهرتين` · c `تأبير ذاتيّ، لأنّ الطّلع لم تنقله حشرة ولا رياح` (tag `eveil.flor.type-pollinisation-par-l-agent`) · d `ليس تأبيرًا، لأنّ التّأبير لا يحدث إلّا بالحشرات أو الرّياح` (56/56/47/59) · explanation : `الطّلع انتقل إلى ميسم زهرة في نبتة أخرى من نفس النّوع، فالتّأبير خلطيّ، والّذي نقله هو الباحث فوسيلته الإنسان، كما يفعل الفلاّح مع النّخيل. ولا يكون التّأبير ذاتيًّا إلّا إذا وصل الطّلع إلى ميسم الزّهرة نفسها، أيًّا كانت الوسيلة.` *(supprime aussi l'ancien c « ووسيلته الرّياح », contredit par l'énoncé.)*
- **défi Q3** prompt : `نقلت فراشة حبّات طلع من زهرة خوخ إلى ميسم زهرة رمّان. هل هذا تأبير؟` · options a `نعم، تأبير خلطيّ لأنّهما زهرتان مختلفتان` · b `نعم، تأبير ذاتيّ لأنّ فراشة واحدة نقلته` (tag inchangé) · c `لا، لأنّ الزّهرتين ليستا من نفس النّوع` (clé) · d `لا، لأنّ الفراشات لا تنقل حبّات الطّلع` (40/39/38/38) · explanation : `التّأبير هو انتقال الطّلع إلى ميسم زهرة من نفس النّوع، والخوخ والرّمّان نوعان مختلفان، فهذا ليس تأبيرًا. ولا يكفي أن تكون الزّهرتان مختلفتين ليكون التّأبير خلطيًّا: يجب أن تكونا من نفس النّوع.`

#### M-13 — `06` : « التّلقيح = الحقنة » (science, contredit le ch. 10)
Le ch. `10-microbes-defense` enseigne trois voies de vaccination (الكشط / التجرّع / الحقن, manuel
p.77) ; dire que التلقيح « هو الحقنة » est faux pour le vaccin oral. Quatre endroits :
- `06/cours.md` l.88–89 : `> ⚠️ لا نقول «التّلقيح» للنّبات: التّلقيح في الإيقاظ العلميّ هو إعطاء اللّقاح الّذي يقي الإنسان من بعض الأمراض الجرثوميّة،` / `> أمّا نقل حبّات الطّلع فاسمه **التّأبير**.`
- `06/resume.md` puce 2, fin : `ولا نقول «التّلقيح» للنّبات، فهو إعطاء اللّقاح الّذي يقي الإنسان من المرض.`
- `06/quiz.json` Q6 explanation, 2ᵉ phrase : `والتّلقيح في الإيقاظ العلميّ هو إعطاء اللّقاح الّذي يقي الإنسان من المرض،`
- `06/exercices/03-revision.json` Q8 explanation, 1ʳᵉ phrase : `نقل الطّلع إلى الميسم اسمه التّأبير، والتّلقيح في الإيقاظ العلميّ إعطاء لقاح يقي من المرض.`

#### M-14 — `04/exercices/02-boss.json` : reprise déclarée `تقييم 2 · 1-أ` qui n'en est pas une
Guide p.128–129 : 1-أ = classer les **huit** aliments du petit-déjeuner (زبدة، بيض، جبن، تفّاح، حليب،
خبز، عسل، برتقالة) dans les **trois** colonnes. Q7 demande seulement les aliments de la **طاقة** parmi
**six** (جبن et برتقالة retirés) : tâche et données différentes = variante. 1-ب (Q8, le propos
d'Ahmed) est fidèle. Correction : `"items": ["تقييم 2 · 1-ب"]`.

#### M-15 — `06/exercices/03-revision.json` : reprise déclarée `أطبّق 6-أ` (p.106) qui n'en est pas une
Le manuel fait ordonner **des dessins** de germination et de croissance ; Q7 ordonne **cinq étapes
écrites** (dont التأبير ثمّ الإخصاب). Variante → retirer le champ `manuel` du fichier (aucun autre
item n'est une reprise de p.106).

#### M-16 — `04/exercices/04-defi.json` Q8 : énoncé « أيّ خطرين » et clé à trois risques ; c contredit l'énoncé
- prompt : `طفل لا يأكل إلّا الحلويات والمشروبات الغازيّة الّتي يشتريها مكشوفة أمام المدرسة. أيّ الأخطار تهدّده أكثر؟`
- c : `الكساح وفقر الدم، لأنّ الحلويات خالية من الكالسيوم والحديد` (tag `eveil.nutri.malnutrition-seulement-par-manque` gardé) — remplace « لأنّه لا يأكل شيئًا », démenti par l'énoncé.
- d : `السمنة وحدها، لأنّ الأكل المكشوف لا يحمل أيّ جراثيم` (sans tag) — remplace l'absurde « لا تضرّ الأسنان أبدًا ».
- longueurs a/b/c/d = 55/54/58/51 ; clé b inchangée.
- explanation : `الإفراط في الحلويات والمشروبات الغازيّة يسبّب السمنة وتسوّس الأسنان، والأكل المكشوف قد يحمل جراثيم فتنتقل العدوى. أمّا أمراض النقص كالإسقربوط والكساح وفقر الدم فليست ما يهدّده أوّلًا، فهو يأكل كثيرًا من نوع واحد، والجراثيم لا تُرى فلا يكفي أن يبدو الأكل نظيفًا.`

#### M-17 — `05/exercices/05-entrainement.json` Q7 (libre) : bonne réponse refusée
L'énoncé décrit l'hépatite (« سببه فيروس يلتهب منه الكبد ») : « التهاب الكبد » est juste et serait
refusé (le tier automatique ne gère que l'article et les graphies). Et l'explication contient
« التهاب الكبد ».
- prompt : `ما اسم المرض المنقول بالمياه الملوّثة، الّذي سببه فيروس، ومن أعراضه اصفرار بياض العينين؟`
- `"acceptedAnswers": ["التهاب الكبد", "التهاب الكبد الفيروسي", "مرض البوصفير"]` (aucune n'égale « الكوليرا » ni « الحمى التيفية »)
- explanation : `اصفرار البشرة وبياض العينين علامة مرض يصيب الكبد، وسببه فيروس لا جرثومة. أمّا المرضان الآخران من أمراض المياه الملوّثة فسببهما جرثومة، وعلامتاهما التقيّؤ والإسهال، أو الحمّى وآلام الأمعاء.`

#### M-18 — étiquettes qui ne nomment pas l'erreur exécutée
- `04/exercices/02-boss.json` Q8 option a (« صحيح، لأنّ الجسم ينمو بالطاقة… ») : elle exécute « l'énergie fait grandir », et accepte en plus tout le propos (deux erreurs) → **retirer** `misconceptionTag`.
- `06/exercices/04-defi.json` Q6 option b (« بحبّات الطّلع المخزّنة في البذرة ») : rien ne « naît du pollen » ici → **retirer** le tag `eveil.flor.plante-nait-du-pollen`.
- (`05/02-boss Q4 d`, `05/04-defi Q7 b`, `06/02-boss Q6 a` : réglés par M-8, M-10, M-12.)

#### M-19 — `05/cours.md` § « حلقة تغيب » : le `verifie` teste une autre notion
Le `verifie` (pesticide → plus d'abeilles → moins de fruits) teste la **pollinisation** (ch. 06), pas
la chaîne alimentaire (les abeilles ne mangent pas les fruits), et double `06/04-defi Q7`. Remplacer
le bloc l.259–267 par :

```
::: verifie
في السلسلة: الصقر ← الأفعى ← الضفدع ← الجرادة ← العشب، صاد الناس الأفاعي كلّها. ماذا يحدث للصقر؟ وللضفادع؟

---

يفقد الصقر غذاءه، لأنّه يتغذّى على الأفعى. أمّا الضفادع فقد تكثر، لأنّ الأفعى الّتي كانت تتغذّى
عليها اختفت. فغياب حلقة أثّر في الحلقة الّتي فوقها وفي الّتي تحتها، لأنّ الكائنات مرتبطة بالغذاء.
:::
```
et dans `05/resume.md`, puce « حلقة تغيب » : `(جراد يأكل العشب، مبيد يقتل العوالق الحيوانيّة)` au lieu de `(جراد يأكل العشب، مبيد يقتل الحشرات)`.

### MINEURS

- **m-1** `04/quiz.json` Q2 option d « المصدر الحيوانيّ » : deux erreurs (origine fausse ET origine au lieu du groupe) → retirer le tag.
- **m-2** `04/exercices/05-entrainement.json` Q7 : ajouter `"acceptedAnswers": ["مرض الإسقربوط", "داء الإسقربوط"]` (le tier automatique couvre « إسقربوط », « الاسقربوط »).
- **m-3** `06/exercices/01-pratique.json` Q9 : ajouter `"acceptedAnswers": ["عملية الإخصاب", "الإلقاح"]` (« إلقاح » est le terme du guide p.142 ; « التأبير » reste l'erreur attendue).
- **m-4** `06/exercices/02-boss.json` Q2 option d « الجذور والسّاق والأوراق الخضراء » : remplissage → `الرّحيق والعسل والألوان` (hypothèses du manuel p.101 ; longueurs 13/25/30/23, clé non la plus longue).
- **m-5** `06/exercices/02-boss.json` Q5 (6 graines → 6 ovules) : jumeau très proche du `verifie` (5 graines) — acceptable, mais varier le support (`ثمرة طماطم فيها 40 بذرة`) le rendrait moins mécanique.
- **m-6** `06/exercices/04-defi.json` Q2 : redit le cas limite de la règle (« زهرة قُطعت أسديتها… ») et la situation du manuel p.99 ; garder (c'est la reprise de l'idée du manuel) ou changer de plante.
- **m-7** `06/exercices/05-entrainement.json` Q2 (جلبّان, ذاتيّ) et Q6 (le grand-père garde les graines) reprennent l'exemple 1 et l'ancrage — faciles, mais sans calcul redonné.
- **m-8** Pièges sans étiquette du registre (aucun libellé n'existe) : 04 § الوجبة المتوازنة (« repas = groupes »), 04 § سلامة الغذاء, 05 § حلقة تغيب, 06 § الثمرة الكاذبة. Les ids proposés par l'auteur (`eveil.eco.maillon-retire-sans-effet`, `eveil.nutri.equilibre-sans-salubrite`, `eveil.nutri.groupes-confondus-avec-repas`) sont pertinents ; à créer dans `misconceptions.json` puis à poser sur les distracteurs muets.
- **m-9** `04/cours.md` l.77 : lien causal douteux (« الأدوار الثلاثة تحتاج كمّيّة كبيرة من الماء، ولذلك يمثّل الماء ثلثي كتلة الجسم ») → `الماء حاضر في كلّ أنحاء الجسم ليقوم بهذه الأدوار الثلاثة، وهو يكوّن ثلثي كتلته.`
- **m-10** `04/cours.md` l.253 : la raison « لأنّه لا يمدّ الجسم بالطاقة » vaut aussi pour les vitamines (rangées dans un groupe) → `2. الماء ضروريّ للجسم لكنّه ليس من المجموعات الثلاث — لأنّه لا يبني الجسم ولا يمدّه بالطاقة، بل يحتاجه الجسم مع كلّ المجموعات.`
- **m-11** `05/cours.md` tableau des maladies : le manuel p.116 donne aussi « الرّغبة في التقيّؤ » pour البوصفّير ; la ligne la tait, et « التقيّؤ مع الإسهال للكوليرا » reste juste (le إسهال ne figure que pour le choléra). Ajouter `، رغبة في التقيّؤ` à la ligne البوصفّير pour suivre le manuel.
- **m-12** Nombre de notions : 04 et 05 ont 9 sections (seuil ~8) ; 05 porte trois دروس (27–29). Question de programme pour l'humain (pas de coupe silencieuse) — l'auteur le signale aussi.
- **m-13** `06/cours.md` figure de la fleur : l'étiquette « البتلة » (rose foncé) est posée sur la pétale rose ; lisible grâce au halo blanc, mais à 360 px elle est la moins contrastée.
- **m-14** `04/exercices/03-revision.json` Q6 option d « لأنّ الفواكه من أغذية البناء وحدها » : formulation bancale → `لأنّ الفواكه من أغذية الطاقة وحدها`.

---

## Après lecture des notes et du rapport de l'auteur

- L'auteur affirme en « Doutes 10 » que « l'article et la vocalisation sont repliés par le moteur » :
  **vérifié exact** (`free-answer.ts`, tier morphologique arabe) — d'où m-2/m-3 en mineur et non en
  majeur ; M-17 reste majeur (paraphrase juste, pas une variante d'article).
- Ses doutes 2, 5, 6, 7, 8 sont levés par le PDF (flèche du lac p.112 ; sachet p.103 ; ثمرة كاذبة p.107).
  Doute 1 = m-12. Ses ids d'étiquettes = m-8.
- Il n'a pas vu : les redites du cours dans les exercices (M-1 à M-12), le `verifie` hors notion (M-19),
  « التلقيح = الحقنة » (M-13), les deux reprises déclarées qui sont des variantes (M-14, M-15),
  « خطرين » (M-16), les étiquettes inversées (M-18).

## Bilan

| chapitre | questions | critiques | majeurs | mineurs |
| --- | --- | --- | --- | --- |
| 04-nutrition | 46 | 0 | 8 (M-1 à M-5, M-14, M-16, M-18a) | 6 (m-1, m-2, m-9, m-10, m-14, m-8) |
| 05-milieu-chaines-alimentaires | 42 | 0 | 8 (M-6 à M-11, M-17, M-19) | 3 (m-8, m-11, m-12) |
| 06-reproduction-florale | 45 | 0 | 4 (M-12, M-13, M-15, M-18b) | 6 (m-3 à m-7, m-13) |

Cours : patron complet et juste dans les 24 sections ; aucune erreur du manuel reprise ; V1 et V4
respectés. Verdict : **à corriger** — aucune clé fausse, mais ~22 items redonnent le cours mot pour
mot ou presque, plus deux champs `manuel` à corriger et une définition de التلقيح à rectifier.
Tous les remplacements sont prêts à coller.
