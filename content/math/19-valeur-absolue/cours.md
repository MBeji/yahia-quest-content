# ⚔️ القيمة المطلقة لعدد حقيقي — سلاح البُعد

> 💡 «كلّ عدد حقيقي يجلس في مكانٍ ما على المستقيم المدرّج. القيمة المطلقة لا تسأل: في أيّ جهة؟ بل تسأل: على أيّ بُعد؟»

## 🏰 التعريف: القيمة المطلقة بُعدٌ

نعتبر مستقيمًا مدرّجًا (OI) : النقطة O هي المبدأ، والبعد OI هو وحدة الطول.

::: figure نقطتان على مستقيم مدرّج: بُعد كلّ نقطة عن المبدأ هو القيمة المطلقة لفاصلتها
<svg viewBox="0 0 360 165"><title>مستقيم مدرّج تُقاس عليه أبعاد النقاط عن المبدأ</title><line x1="30" y1="100" x2="330" y2="100" stroke="#334155" stroke-width="2"/><polygon points="338,100 328,95 328,105" fill="#334155"/><line x1="40" y1="95" x2="40" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="75" y1="95" x2="75" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="110" y1="95" x2="110" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="145" y1="95" x2="145" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="180" y1="95" x2="180" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="215" y1="95" x2="215" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="250" y1="95" x2="250" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="285" y1="95" x2="285" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="320" y1="95" x2="320" y2="105" stroke="#94a3b8" stroke-width="1.5"/><text x="40" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−4</text><text x="75" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−3</text><text x="110" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−2</text><text x="145" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−1</text><text x="180" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">0</text><text x="215" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">1</text><text x="250" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">2</text><text x="285" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">3</text><text x="320" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">4</text><text x="180" y="139" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate">O</text><text x="215" y="139" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate">I</text><circle cx="75" cy="100" r="5" fill="#dc2626"/><circle cx="250" cy="100" r="5" fill="#2563eb"/><text x="75" y="86" text-anchor="middle" font-size="13" font-weight="700" fill="#dc2626" direction="ltr" unicode-bidi="isolate">M</text><text x="250" y="86" text-anchor="middle" font-size="13" font-weight="700" fill="#2563eb" direction="ltr" unicode-bidi="isolate">N</text><line x1="75" y1="64" x2="180" y2="64" stroke="#dc2626" stroke-width="2"/><line x1="180" y1="64" x2="250" y2="64" stroke="#2563eb" stroke-width="2"/><line x1="75" y1="59" x2="75" y2="69" stroke="#dc2626" stroke-width="2"/><line x1="180" y1="59" x2="180" y2="69" stroke="#334155" stroke-width="2"/><line x1="250" y1="59" x2="250" y2="69" stroke="#2563eb" stroke-width="2"/><text x="127" y="52" text-anchor="middle" font-size="12" font-weight="700" fill="#dc2626" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">OM = 3</text><text x="215" y="52" text-anchor="middle" font-size="12" font-weight="700" fill="#2563eb" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ON = 2</text><text x="180" y="158" text-anchor="middle" font-size="11" fill="#64748b">القيمة المطلقة هي البعد عن المبدأ</text></svg>
:::

**تعريف** — لتكن M نقطة من مستقيم مدرّج (OI) فاصلتها عدد حقيقي x . القيمة المطلقة لـ x هي البعد OM ، ونكتب:

$$ |x| = OM $$

في الرسم أعلاه، فاصلة M هي −3 وبعدها عن المبدأ هو 3 ، إذن |−3| = 3 . وفاصلة N هي 2 وبعدها 2 ، إذن |2| = 2 .

> 🗡️ بما أنّ القيمة المطلقة بُعدٌ، فهي **لا تكون سالبة أبدًا**: مهما كان العدد الحقيقي x فإنّ القيمة المطلقة |x| موجبة أو معدومة.

## 🗡️ حساب القيمة المطلقة حسب إشارة العدد

النقطتان اللتان فاصلتاهما x و −x تقعان على البعد نفسه من المبدأ، لكن في جهتين مختلفتين. ومنه:

| حالة العدد x    | القيمة المطلقة |
| --------------- | -------------- |
| x موجب أو معدوم | \|x\| = x      |
| x سالب          | \|x\| = −x     |

_أمثلة محسوبة_:

- العدد 6 موجب، إذن |6| = 6 .
- العدد −13 سالب، إذن |−13| = −(−13) = 13 .
- |0| = 0 ، و |−4/7| = 4/7 ، و |−√5| = √5 ، و |π| = π .

⚠️ الكتابة −x **ليست** بالضرورة عددًا سالبًا: إذا كان x سالبًا فإنّ −x موجب. مثلًا مع x = −13 نجد −x = 13 .

### الحالة التي تحتاج تفكيرًا: عبارة إشارتها غير ظاهرة

قبل حذف الأقواس، **ابحث عن إشارة العبارة** داخل القيمة المطلقة.

::: methode القيمة التقريبية العشرية: الطريقة الوحيدة المعتمدة هنا لتحديد الإشارة

عوّض كلّ عدد أصمّ بقيمته التقريبية العشرية، ثمّ أنجز الطرح واقرأ إشارة النتيجة. القيم التقريبية المرجعية:

- √2 ≈ 1,41
- √3 ≈ 1,73
- √5 ≈ 2,24
- π ≈ 3,14

ولأيّ عدد أصمّ آخر، اطلب قيمته التقريبية من الآلة الحاسبة (مثلًا √6 ≈ 2,45 و √7 ≈ 2,65).

:::

_مثال 1_: العبارة √6 − 3 . بما أنّ √6 ≈ 2,45 فهي أصغر من 3 ، ومنه √6 − 3 عدد سالب:

$$ |√6 − 3| = −(√6 − 3) = 3 − √6 $$

_مثال 2_: العبارة π − 2 . بما أنّ π ≈ 3,14 فهي عبارة موجبة، ومنه:

$$ |π − 2| = π − 2 $$

> ⚠️ الفخّ الأشهر: قلب الطرحين آليًّا. الكتابة |a − b| = b − a **ليست قاعدة**؛ هي صحيحة فقط لمّا يكون a − b سالبًا.

## 🔮 المساواة بقيمة مطلقة

- المساواة |x| = 0 تعني أنّ x = 0 : النقطة الوحيدة التي بعدها عن المبدأ معدوم هي المبدأ نفسه.
- إذا كان a عددًا موجبًا فإنّ المساواة |x| = a تعني أنّ x = a أو x = −a : هناك نقطتان على البعد a من المبدأ، واحدة في كلّ جهة.
- إذا كان a سالبًا فإنّ المساواة |x| = a **لا تقبل أيّ حلّ**، لأنّ البعد لا يكون سالبًا.

_أمثلة محسوبة_:

- المساواة |x| = 10 لها حلّان: x = 10 أو x = −10 .
- المساواة |x| = −2 لا تقبل أيّ حلّ في ℝ .
- المساواة |−x| = 7 تكافئ |x| = 7 (لأنّ x و −x لهما البعد نفسه)، فحلّاها x = 7 أو x = −7 .

## 📐 البعد بين نقطتين على مستقيم مدرّج

القيمة المطلقة تقيس أيضًا البعد بين نقطتين أيًّا كان ترتيبهما. إذا كانت A و B نقطتين من (OI) فاصلتاهما a و b على التوالي، فإنّ:

$$ AB = |b − a| $$

_مثال محسوب_: فاصلة A هي −6 وفاصلة B هي −1 . إذن AB = |−1 − (−6)| = |5| = 5 .

::: figure النقطتان A و B على مستقيم مدرّج: البعد AB هو القيمة المطلقة للفرق بين فاصلتيهما
<svg viewBox="0 0 360 165"><title>البعد بين نقطتين فاصلتاهما سالبتان على مستقيم مدرّج</title><line x1="20" y1="100" x2="330" y2="100" stroke="#334155" stroke-width="2"/><polygon points="338,100 328,95 328,105" fill="#334155"/><line x1="30" y1="95" x2="30" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="60" y1="95" x2="60" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="90" y1="95" x2="90" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="120" y1="95" x2="120" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="150" y1="95" x2="150" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="180" y1="95" x2="180" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="210" y1="95" x2="210" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="240" y1="95" x2="240" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="270" y1="95" x2="270" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="300" y1="95" x2="300" y2="105" stroke="#94a3b8" stroke-width="1.5"/><text x="30" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−7</text><text x="60" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−6</text><text x="90" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−5</text><text x="120" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−4</text><text x="150" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−3</text><text x="180" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−2</text><text x="210" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−1</text><text x="240" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">0</text><text x="270" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">1</text><text x="300" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">2</text><text x="240" y="139" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate">O</text><text x="270" y="139" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate">I</text><circle cx="60" cy="100" r="5" fill="#dc2626"/><circle cx="210" cy="100" r="5" fill="#2563eb"/><text x="60" y="86" text-anchor="middle" font-size="13" font-weight="700" fill="#dc2626" direction="ltr" unicode-bidi="isolate">A</text><text x="210" y="86" text-anchor="middle" font-size="13" font-weight="700" fill="#2563eb" direction="ltr" unicode-bidi="isolate">B</text><line x1="60" y1="64" x2="210" y2="64" stroke="#0f172a" stroke-width="2"/><line x1="60" y1="59" x2="60" y2="69" stroke="#dc2626" stroke-width="2"/><line x1="210" y1="59" x2="210" y2="69" stroke="#2563eb" stroke-width="2"/><text x="135" y="52" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">AB = 5</text><text x="180" y="158" text-anchor="middle" font-size="11" fill="#64748b">البعد لا يتعلّق بترتيب النقطتين</text></svg>
:::

> 🗡️ الترتيب لا يهمّ: لو حسبنا |−6 − (−1)| = |−5| = 5 لوجدنا النتيجة نفسها. وهذا طبيعي، فالبعد AB هو البعد BA .

نظير النقطة N بالنسبة إلى النقطة I هي النقطة P التي تجعل I منتصف [NP] ، أي IN = IP .

## 🛡️ خاصيّتا الجذاء وخارج القسمة

مهما يكن العددان الحقيقيان a و b :

$$ |a × b| = |a| × |b| $$

ومهما يكن العدد الحقيقي a والعدد الحقيقي b المخالف للصفر:

$$ |a/b| = |a|/|b| $$

$$ |1/b| = 1/|b| $$

_أمثلة محسوبة_:

- |(−7) × 2| = |−7| × |2| = 7 × 2 = 14 . ونتحقّق مباشرة: (−7) × 2 = −14 ومنه |−14| = 14 .
- |−20/(−4)| = |−20|/|−4| = 20/4 = 5 .
- |1/(−3)| = 1/|−3| = 1/3 .

_مثال محسوب مركّب_: أوجد القيمة المطلقة للجذاء (3 − √2)(1 − √6) .

نبحث عن إشارة كلّ عامل: بما أنّ √2 ≈ 1,41 فإنّ 3 − √2 عدد موجب ومنه |3 − √2| = 3 − √2 ؛ وبما أنّ √6 ≈ 2,45 فإنّ 1 − √6 عدد سالب ومنه |1 − √6| = √6 − 1 . وبتطبيق خاصيّة الجذاء:

$$ |(3 − √2)(1 − √6)| = (3 − √2)(√6 − 1) $$

> ⚠️ **الخاصيّة موجودة للجذاء والخارج، لا للمجموع.** الكتابة |a + b| = |a| + |b| خاطئة عمومًا: مع a = 7 و b = −7 نجد |a + b| = |0| = 0 بينما |a| + |b| = 14 .

> 🏆 أتقنت هذه البوّابة! القيمة المطلقة أداة بُعد ستلازمك في التأطير، وفي الجذور، وفي قراءة المستقيم المدرّج.
