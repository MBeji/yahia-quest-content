# ⚔️ القيمة المطلقة لعدد حقيقي — سلاح البُعد

> 💡 «كلّ عدد حقيقي يجلس في مكانٍ ما على المستقيم المدرّج. القيمة المطلقة لا تسأل: في أيّ جهة؟ بل تسأل: على أيّ بُعد؟»

## 🏰 التعريف: القيمة المطلقة بُعدٌ

بيتك يبعد 3 km شرق المدرسة، وبيت صديقك يبعد 3 km غربها. مَن منكما أبعد عن المدرسة؟ لا أحد:
المسافة نفسها، والجهة وحدها تختلف. فكيف نكتب رياضيًّا «المسافة دون الجهة»؟

::: figure نقطتان على مستقيم مدرّج: بُعد كلّ نقطة عن المبدأ هو القيمة المطلقة لفاصلتها
<svg viewBox="0 0 360 165"><title>مستقيم مدرّج تُقاس عليه أبعاد النقاط عن المبدأ</title><line x1="30" y1="100" x2="330" y2="100" stroke="#334155" stroke-width="2"/><polygon points="338,100 328,95 328,105" fill="#334155"/><line x1="40" y1="95" x2="40" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="75" y1="95" x2="75" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="110" y1="95" x2="110" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="145" y1="95" x2="145" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="180" y1="95" x2="180" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="215" y1="95" x2="215" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="250" y1="95" x2="250" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="285" y1="95" x2="285" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="320" y1="95" x2="320" y2="105" stroke="#94a3b8" stroke-width="1.5"/><text x="40" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−4</text><text x="75" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−3</text><text x="110" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−2</text><text x="145" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−1</text><text x="180" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">0</text><text x="215" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">1</text><text x="250" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">2</text><text x="285" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">3</text><text x="320" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">4</text><text x="180" y="139" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate">O</text><text x="215" y="139" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate">I</text><circle cx="75" cy="100" r="5" fill="#dc2626"/><circle cx="250" cy="100" r="5" fill="#2563eb"/><text x="75" y="86" text-anchor="middle" font-size="13" font-weight="700" fill="#dc2626" direction="ltr" unicode-bidi="isolate">M</text><text x="250" y="86" text-anchor="middle" font-size="13" font-weight="700" fill="#2563eb" direction="ltr" unicode-bidi="isolate">N</text><line x1="75" y1="64" x2="180" y2="64" stroke="#dc2626" stroke-width="2"/><line x1="180" y1="64" x2="250" y2="64" stroke="#2563eb" stroke-width="2"/><line x1="75" y1="59" x2="75" y2="69" stroke="#dc2626" stroke-width="2"/><line x1="180" y1="59" x2="180" y2="69" stroke="#334155" stroke-width="2"/><line x1="250" y1="59" x2="250" y2="69" stroke="#2563eb" stroke-width="2"/><text x="127" y="52" text-anchor="middle" font-size="12" font-weight="700" fill="#dc2626" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">OM = 3</text><text x="215" y="52" text-anchor="middle" font-size="12" font-weight="700" fill="#2563eb" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ON = 2</text><text x="180" y="158" text-anchor="middle" font-size="11" fill="#64748b">القيمة المطلقة هي البعد عن المبدأ</text></svg>
:::

في الشكل، فاصلة M هي −3 وفاصلة N هي 2 — الإشارة تقول الجهة، والبعد يقول المسافة.

::: definition
نعتبر مستقيمًا مدرّجًا (OI): النقطة O هي المبدأ، والبعد OI هو وحدة الطول. لتكن M نقطة فاصلتها
عدد حقيقي x. **القيمة المطلقة** (valeur absolue) لـ x هي البعد OM، ونكتب:
$$ |x| = OM $$
:::

::: exemple قراءة الشكل

1. فاصلة M هي −3، وبعدها عن المبدأ 3 وحدات — إذن |−3| = **3**.
2. فاصلة N هي 2، وبعدها عن المبدأ وحدتان — إذن |2| = **2**.
3. لاحظ أنّ الإشارة اختفت في الحالتين: البعد لا يحمل جهة.

:::

> ⚠️ **الخطأ الشائع**: الظنّ أنّ قيمة مطلقة قد تكون سالبة. هي **بُعدٌ**، والبعد لا يكون سالبًا
> أبدًا: مهما كان العدد الحقيقي x فإنّ |x| موجبة أو معدومة.

::: verifie
احسب |−9| و |0| و |√3|.

---

|−9| = **9**، لأنّ النقطة ذات الفاصلة −9 تبعد 9 وحدات عن المبدأ.
|0| = **0**، لأنّ المبدأ يبعد عن نفسه بعدًا معدومًا.
|√3| = **√3**، لأنّ √3 عدد موجب فبعده عن المبدأ هو هو.
:::

::: retenir
|x| هو بُعد العدد x عن الصفر — ولا يكون سالبًا أبدًا.
:::

## 🗡️ حساب القيمة المطلقة حسب إشارة العدد

|6| = 6 ، فهل نكتب دائمًا |x| = x ؟ جرّب مع −13 : لو كتبنا |−13| = −13 لكان البعد سالبًا. إذن
القاعدة تتفرّع — ومتى بالضبط؟

::: propriete
النقطتان اللتان فاصلتاهما x و −x تقعان على البعد نفسه من المبدأ، لكن في جهتين مختلفتين. ومنه:

| حالة العدد x    | القيمة المطلقة |
| --------------- | -------------- |
| x موجب أو معدوم | \|x\| = x      |
| x سالب          | \|x\| = −x     |

:::

::: exemple أربع قيم، وحالتان فقط

1. العدد 6 موجب، إذن |6| = **6** — الحالة الأولى، القيمة هي العدد نفسه.
2. العدد −13 سالب، إذن |−13| = −(−13) = **13** — الحالة الثانية، القيمة هي المقابل (opposé).
3. |−4/7| = **4/7** و |−√5| = **√5** — الحالة الثانية أيضًا.
4. |0| = **0** و |π| = **π** — الحالة الأولى.

:::

> ⚠️ **الخطأ الشائع**: أخذ المقابل في كلّ الحالات. القيمة المطلقة لا تغيّر الإشارة إلّا إذا كان
> العدد **سالبًا**. والخطأ التوأم: قراءة الكتابة −x كعدد سالب دائمًا — إذا كان x سالبًا فإنّ −x
> **موجب**: مع x = −13 نجد −x = 13.

::: methode العبارة التي لا تظهر إشارتها — القيمة التقريبية العشرية
قبل حذف الأقواس، **ابحث عن إشارة العبارة** داخل القيمة المطلقة: عوّض كلّ عدد أصمّ بقيمته
التقريبية، ثمّ أنجز الطرح واقرأ إشارة النتيجة. القيم المرجعية: √2 ≈ 1,41 و √3 ≈ 1,73 و
√5 ≈ 2,24 و π ≈ 3,14 ؛ ولأيّ عدد آخر، اطلب القيمة من الآلة (√6 ≈ 2,45 و √7 ≈ 2,65).
:::

::: exemple عبارتان، إشارتان مختلفتان

1. العبارة √6 − 3 : بما أنّ √6 ≈ 2,45 فهي أصغر من 3، إذن العبارة **سالبة**.
2. فنأخذ المقابل: |√6 − 3| = −(√6 − 3) = **3 − √6**.
3. العبارة π − 2 : بما أنّ π ≈ 3,14 فهي **موجبة**.
4. فنُبقيها كما هي: |π − 2| = **π − 2** — القوسان يسقطان دون تغيير.

:::

> ⚠️ **الفخّ الأشهر**: قلب الطرحين آليًّا. الكتابة |a − b| = b − a **ليست قاعدة**؛ هي صحيحة
> فقط لمّا يكون a − b سالبًا. اختبر الإشارة أوّلًا، دائمًا.

::: verifie
احسب |√2 − 2| ثمّ |5 − √3|.

---

√2 ≈ 1,41 < 2، فالعبارة **سالبة** ونأخذ المقابل: |√2 − 2| = **2 − √2**.
√3 ≈ 1,73 < 5، فالعبارة 5 − √3 **موجبة** وتبقى كما هي: |5 − √3| = **5 − √3**.
:::

::: retenir
اختبر إشارة ما داخل الأقواس **قبل** حذفها: الموجب يبقى، والسالب يصير مقابله.
:::

## 🔮 المساواة بقيمة مطلقة

ابحث عن كلّ نقطة تبعد 10 وحدات عن المبدأ. واحدة على اليمين، وواحدة على اليسار: نقطتان. والآن
ابحث عن نقطة تبعد −2 وحدة. كم نقطة تجد؟

::: propriete

- المساواة |x| = 0 تعني أنّ x = 0: النقطة الوحيدة التي بعدها عن المبدأ معدوم هي المبدأ نفسه.
- إذا كان a عددًا موجبًا: المساواة |x| = a تعني أنّ x = a **أو** x = −a — نقطتان، واحدة في كلّ جهة.
- إذا كان a سالبًا: المساواة |x| = a **لا تقبل أيّ حلّ**، لأنّ البعد لا يكون سالبًا.

:::

::: exemple ثلاث مساواة، ثلاث حالات

1. |x| = 10 لها **حلّان**: x = 10 أو x = −10 — لأنّ النقطتين تبعدان 10 وحدات عن المبدأ.
2. |x| = −2 **لا تقبل أيّ حلّ** في ℝ — لأنّ البعد لا يكون سالبًا.
3. |−x| = 7 تكافئ |x| = 7، لأنّ x و −x لهما البعد نفسه — فحلّاها x = 7 أو x = −7.

:::

> ⚠️ **الخطأ الشائع**: الاكتفاء بحلّ واحد. المساواة |x| = a لها **حلّان متقابلان** كلّما كان a
> موجبًا قطعًا — ونسيان الحلّ السالب يُفقد نصف الجواب.

::: verifie
حلّ المساواة |x| = 4، ثمّ المساواة |x| = 0، ثمّ المساواة |x| = −3.

---

|x| = 4 : حلّان، **x = 4 أو x = −4** — نقطتان على البعد 4 من المبدأ.
|x| = 0 : حلّ وحيد، **x = 0** — المبدأ وحده بعده معدوم.
|x| = −3 : **لا حلّ**، لأنّ البعد لا يكون سالبًا.
:::

::: retenir
|x| = a (مع a > 0) لها **حلّان** متقابلان ؛ و |x| = 0 حلّ وحيد ؛ و a سالب: لا حلّ.
:::

## 📐 البعد بين نقطتين على مستقيم مدرّج

مدينتان على طريق مستقيم: الأولى عند الكيلومتر −6 والثانية عند الكيلومتر −1. كم بينهما؟ لا تطرح
عشوائيًّا: الفرق قد يخرج سالبًا، والمسافة لا تكون سالبة.

::: propriete
إذا كانت A و B نقطتين من (OI) فاصلتاهما a و b على التوالي، فإنّ:
$$ AB = |b − a| $$
:::

::: figure النقطتان A و B على مستقيم مدرّج: البعد AB هو القيمة المطلقة للفرق بين فاصلتيهما
<svg viewBox="0 0 360 165"><title>البعد بين نقطتين فاصلتاهما سالبتان على مستقيم مدرّج</title><line x1="20" y1="100" x2="330" y2="100" stroke="#334155" stroke-width="2"/><polygon points="338,100 328,95 328,105" fill="#334155"/><line x1="30" y1="95" x2="30" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="60" y1="95" x2="60" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="90" y1="95" x2="90" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="120" y1="95" x2="120" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="150" y1="95" x2="150" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="180" y1="95" x2="180" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="210" y1="95" x2="210" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="240" y1="95" x2="240" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="270" y1="95" x2="270" y2="105" stroke="#94a3b8" stroke-width="1.5"/><line x1="300" y1="95" x2="300" y2="105" stroke="#94a3b8" stroke-width="1.5"/><text x="30" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−7</text><text x="60" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−6</text><text x="90" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−5</text><text x="120" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−4</text><text x="150" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−3</text><text x="180" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−2</text><text x="210" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">−1</text><text x="240" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">0</text><text x="270" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">1</text><text x="300" y="120" text-anchor="middle" font-size="11" fill="#475569" direction="ltr" unicode-bidi="isolate">2</text><text x="240" y="139" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate">O</text><text x="270" y="139" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate">I</text><circle cx="60" cy="100" r="5" fill="#dc2626"/><circle cx="210" cy="100" r="5" fill="#2563eb"/><text x="60" y="86" text-anchor="middle" font-size="13" font-weight="700" fill="#dc2626" direction="ltr" unicode-bidi="isolate">A</text><text x="210" y="86" text-anchor="middle" font-size="13" font-weight="700" fill="#2563eb" direction="ltr" unicode-bidi="isolate">B</text><line x1="60" y1="64" x2="210" y2="64" stroke="#0f172a" stroke-width="2"/><line x1="60" y1="59" x2="60" y2="69" stroke="#dc2626" stroke-width="2"/><line x1="210" y1="59" x2="210" y2="69" stroke="#2563eb" stroke-width="2"/><text x="135" y="52" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">AB = 5</text><text x="180" y="158" text-anchor="middle" font-size="11" fill="#64748b">البعد لا يتعلّق بترتيب النقطتين</text></svg>
:::

في الشكل، البعد هو طول القطعة بين النقطتين — والقيمة المطلقة هي ما يضمن أنّه موجب.

::: exemple البعد بين A(−6) و B(−1)

1. نطبّق القاعدة: AB = |−1 − (−6)| — ونحذر إشارتَي الطرح المتتاليتين.
2. −1 − (−6) = −1 + 6 = 5، إذن AB = |5| = **5** وحدات.
3. ولو عكسنا الترتيب: |−6 − (−1)| = |−5| = 5 — النتيجة نفسها، وهذا طبيعيّ لأنّ AB هو BA.

:::

> 🗡️ الترتيب لا يهمّ، والقيمة المطلقة هي التي تجعله لا يهمّ: هي تمحو إشارة الفرق.

ونظير النقطة N بالنسبة إلى النقطة I هي النقطة P التي تجعل I منتصف [NP]، أي IN = IP.

::: verifie
احسب البعد بين A(−2) و B(7)، ثمّ بين C(3,5) و D(−1,5).

---

AB = |7 − (−2)| = |9| = **9** وحدات.
CD = |−1,5 − 3,5| = |−5| = **5** وحدات — والقيمة المطلقة محت إشارة الفرق.
:::

::: retenir
AB = |b − a| : الفرق ثمّ القيمة المطلقة، والترتيب لا يهمّ.
:::

## 🛡️ خاصيّتا الجذاء وخارج القسمة

|−7| × |2| = 14، و |(−7) × 2| = |−14| = 14. النتيجة نفسها. جرّب الآن مع الجمع: |7| + |−7| = 14،
بينما |7 + (−7)| = |0| = 0. فأيّ العمليات تحترم القيمة المطلقة وأيّها لا؟

::: propriete
مهما يكن العددان الحقيقيان a و b:
$$ |a × b| = |a| × |b| $$
ومهما يكن العدد الحقيقي a والعدد الحقيقي b المخالف للصفر:
$$ |a/b| = |a|/|b| $$
$$ |1/b| = 1/|b| $$
:::

::: exemple ثلاث تطبيقات مباشرة

1. |(−7) × 2| = |−7| × |2| = 7 × 2 = **14** — والتحقّق المباشر: (−7) × 2 = −14 ومنه |−14| = 14 ✓.
2. |−20/(−4)| = |−20|/|−4| = 20/4 = **5**.
3. |1/(−3)| = 1/|−3| = **1/3** — فالمقلوب يحتفظ بالقيمة المطلقة مقلوبةً.

:::

::: exemple حالة مركّبة: |(3 − √2)(1 − √6)|

1. نبحث عن إشارة كلّ عامل على حدة — لأنّ الخاصيّة تفصل الجداء إلى عاملين.
2. √2 ≈ 1,41 < 3، إذن 3 − √2 **موجب**، ومنه |3 − √2| = 3 − √2.
3. √6 ≈ 2,45 > 1، إذن 1 − √6 **سالب**، ومنه |1 − √6| = √6 − 1.
4. بتطبيق خاصيّة الجذاء:
   $$ |(3 − √2)(1 − √6)| = (3 − √2)(√6 − 1) $$

:::

> ⚠️ **الخطأ الشائع**: توزيع القيمة المطلقة على **المجموع**. الكتابة |a + b| = |a| + |b| خاطئة
> عمومًا: مع a = 7 و b = −7 نجد |a + b| = |0| = 0 بينما |a| + |b| = 14. الخاصيّة موجودة للجذاء
> والخارج، **لا للمجموع**.

::: verifie
احسب |(−3) × 5| ثمّ |(2 − √5)(1 + √2)|.

---

|(−3) × 5| = |−3| × |5| = 3 × 5 = **15** — والتحقّق: (−3) × 5 = −15 ومنه |−15| = 15 ✓.
√5 ≈ 2,24 > 2، إذن 2 − √5 **سالب** و |2 − √5| = √5 − 2 ؛ والعامل 1 + √2 موجب فيبقى كما هو.
إذن الناتج = **(√5 − 2)(1 + √2)**.
:::

::: retenir
القيمة المطلقة تتوزّع على **الجذاء والقسمة**، لا على الجمع.
:::

> 🏆 أتقنت هذه البوّابة! القيمة المطلقة أداة بُعد ستلازمك في التأطير، وفي الجذور، وفي قراءة
> المستقيم المدرّج.
