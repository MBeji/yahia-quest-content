# ⚔️ المعادلات والمتراجحات — ساحة المجهول

> 💡 «المعادلة هي سؤال رياضي: ما العدد المجهول الذي يجعل الطرفين متساويين؟ المتراجحة تسأل: في أيّ منطقة يعيش هذا المجهول؟»

## 🏰 تعريف المعادلة من الدرجة الأولى

قال لك زميلك: «اخترتُ عددًا، أنقصتُ منه 5/2، ضربتُ النتيجة في 6، ثمّ أضفتُ 75، فوجدتُ 216.» أنت
لا تعرف عدده، لكنّك تعرف ما فعله به. فسمِّ العدد المجهول x واكتب ما قاله: 6(x − 5/2) + 75 = 216.
هذه الكتابة هي **معادلة** — سؤال مكتوب بلغة الرياضيات.

::: definition
كلّ عبارة تؤول كتابتها إلى الشكل ax = b، حيث a عدد حقيقي معلوم **مخالف للصفر** و b عدد حقيقي
معلوم و x عدد مجهول، تسمّى **معادلة من الدرجة الأولى ذات مجهول واحد** في ℝ، وحلّها:
$$ x = b/a $$
:::

::: exemple ثلاث معادلات من الدرجة الأولى

1. 2x − 5 = 0 — تؤول إلى 2x = 5، إذن هي من الدرجة الأولى وحلّها x = 5/2.
2. 3x + 7 = 4x − 1 — الطرفان يحملان x، لكنّها تؤول إلى الشكل ax = b بعد النقل.
3. 2(x + 3) = 10 — الأقواس لا تغيّر الدرجة: بعد النشر تصير 2x = 4.

:::

> 🗡️ المعادلة من الدرجة الثانية تحتوي x²، لذا لا تشتبه بين الدرجتين: x² − 1 = 0 ليست من الدرجة الأولى.

> ⚠️ **الشرط a ≠ 0 ليس زينة**: لو كان a معدومًا لصارت المعادلة 0 × x = b، وهي إمّا مستحيلة
> (إن كان b ≠ 0) وإمّا محقّقة بكلّ عدد (إن كان b = 0) — وفي الحالتين لم تعد معادلة من الدرجة الأولى.

::: verifie
أيّ العبارات التالية معادلة من الدرجة الأولى ذات مجهول واحد؟ 5x + 1 = 0 ، x² + x = 3 ، 7 = 2x.

---

5x + 1 = 0 : **نعم** — تؤول إلى 5x = −1.
x² + x = 3 : **لا** — تحتوي x²، فهي من الدرجة الثانية.
7 = 2x : **نعم** — تؤول إلى 2x = 7، والترتيب بين الطرفين لا يغيّر شيئًا.
:::

::: retenir
معادلة من الدرجة الأولى = ما يؤول إلى ax = b مع a ≠ 0، وحلّها x = b/a.
:::

## ⚡ حلّ المعادلة من الدرجة الأولى

المعادلة ميزان: الطرفان متساويان. إن أضفتَ الكتلة نفسها إلى الكفّتين بقي الميزان متوازنًا، وإن
ضاعفتَ الكفّتين كذلك. هذه هي الحيلة الوحيدة: نغيّر شكل المعادلة دون أن نمسّ توازنها، حتّى يبقى
المجهول وحده في كفّة.

::: methode أربع خطوات

1. نوسّع الأقواس (إن وجدت).
2. ننقل حدود x إلى طرف وحدود الأعداد إلى الطرف الآخر — **والنقل يقلب الإشارة**.
3. نجمع الحدود المتشابهة حتّى نصل إلى ax = b.
4. نقسم الطرفين على معامل x.

:::

::: exemple 3x + 7 = x + 15، خطوة بخطوة

1. لا أقواس، فنبدأ بالنقل: نطرح x من الطرفين ليبقى x في طرف واحد → 3x − x + 7 = 15.
2. نجمع المتشابه: 2x + 7 = 15.
3. ننقل 7 إلى اليمين — وينقلب إلى −7 لأنّ طرحه من الطرفين هو ما فعلناه فعلًا → 2x = 8.
4. نقسم الطرفين على 2، وهو معامل x → x = **4**.
5. **التحقّق** في المعادلة الأصلية: 3(4) + 7 = 19، و 4 + 15 = 19 ✓.

:::

::: exemple معادلة تستلزم النشر أوّلًا: 2(x + 3) − 4 = 3(x − 1)

1. ننشر الطرفين: 2x + 6 − 4 = 3x − 3.
2. نبسّط الطرف الأيسر: 2x + 2 = 3x − 3.
3. ننقل: 2 + 3 = 3x − 2x، أي 5 = x.
4. **التحقّق**: 2(5 + 3) − 4 = 16 − 4 = 12، و 3(5 − 1) = 12 ✓.

:::

> ⚠️ **الخطأ الشائع**: النقل دون قلب الإشارة. من 2x + 7 = 15 نحصل على 2x = 15 **−** 7، لا
> 2x = 15 + 7. النقل ليس انتقالًا، بل طرحٌ من الطرفين.

> ⚠️ **الخطأ التوأم**: التوقّف عند 2x = 8 وإعلان الحلّ 8. المطلوب هو x لا 2x: **اقسم على المعامل**.

> 🗡️ تحقّق دائمًا بتعويض الحلّ في المعادلة **الأصلية**، لا في سطر وسيط قد يحمل خطأك.

::: verifie
حلّ المعادلة 5x − 3 = 2x + 9، ثمّ تحقّق.

---

ننقل: 5x − 2x = 9 + 3 → 3x = 12 → x = **4**.
التحقّق: 5(4) − 3 = 17، و 2(4) + 9 = 17 ✓.
:::

::: retenir
العملية نفسها على الطرفين ؛ النقل يقلب الإشارة ؛ والقسمة على المعامل هي الخطوة الأخيرة.
:::

## 🧭 ترجمة المسائل إلى معادلات

عُد إلى لغز زميلك في بداية الدرس. صرتَ الآن تملك أداة الحلّ — ولم يبقَ إلّا أن تترجم الكلام إلى
كتابة رياضية. هذه الترجمة هي أصعب ما في المسائل، وأكثر ما يُطلب في الامتحان.

::: methode من الكلام إلى المعادلة
سمِّ المجهول x → اكتب معادلة تترجم كلّ شرط في المسألة → حلّ → **فسّر** النتيجة في سياق المسألة.
:::

::: exemple لغز الزميل

1. نسمّي العدد المختار x.
2. «أنقصتُ منه 5/2» تُكتب x − 5/2 ؛ «ضربتُ في 6» تُكتب 6(x − 5/2) ؛ «أضفتُ 75» تُكتب + 75.
3. المعادلة: 6(x − 5/2) + 75 = 216.
4. ننشر: 6x − 15 + 75 = 216، أي 6x + 60 = 216.
5. ننقل ونقسم: 6x = 156، ومنه x = **26**.
6. **التحقّق بالقصّة**: 26 − 2,5 = 23,5 ؛ 23,5 × 6 = 141 ؛ 141 + 75 = 216 ✓.

:::

::: exemple مسألة أعمار

1. عمر الأب ضعف عمر الابن، ومجموع عمريهما 36 سنة.
2. نسمّي عمر **الابن** x، فيكون عمر الأب 2x.
3. المجموع: x + 2x = 36 → 3x = 36 → x = 12.
4. **التفسير**: عمر الابن 12 سنة وعمر الأب 24 سنة. والتحقّق: 24 = 2 × 12 ✓ و 12 + 24 = 36 ✓.

:::

> ⚠️ **الخطأ الشائع**: تقديم x كجواب نهائي دون قراءة السؤال. هنا لو سُئلتَ عن عمر **الأب**
> فالجواب 24 وليس 12. المجهول الذي سمّيتَه ليس بالضرورة المطلوب.

::: verifie
مجموع عددين متتاليين 47. ما هما؟

---

نسمّي الأصغر x، فالذي يليه x + 1. المعادلة: x + (x + 1) = 47 → 2x + 1 = 47 → 2x = 46 → x = **23**.
العددان هما **23 و 24**، والتحقّق: 23 + 24 = 47 ✓.
:::

::: retenir
سمِّ المجهول، ترجم كلّ شرط، حلّ، ثمّ **أجب عن السؤال المطروح** لا عن x وحده.
:::

## 🛡️ مبدأ الجداء المعدوم

جداء عددين يساوي 12: احتمالاته لا تُحصى (3 × 4 ; 2 × 6 ; 24 × 0,5…). لكن جداء عددين يساوي **صفرًا**:
جرّب أن تجد عاملين غير معدومين جداؤهما صفر — لن تجد. هذه الحالة الاستثنائية هي أقوى أداة لحلّ
المعادلات المكتوبة على شكل جداء.

::: propriete
مهما يكن العددان a و b:
$$ a × b = 0 ⟺ a = 0 أو b = 0 $$
:::

::: exemple (x − 3)(x + 5) = 0

1. الطرف الأيسر جداء عاملين، والطرف الأيمن صفر — إذن المبدأ ينطبق.
2. إمّا x − 3 = 0، وهي معادلة من الدرجة الأولى حلّها x = **3**.
3. أو x + 5 = 0، وحلّها x = **−5** — لاحظ أنّ الإشارة **تنقلب** عند النقل.
4. الحلول: x = 3 أو x = −5. والتحقّق بـ x = −5: (−5 − 3)(−5 + 5) = (−8)(0) = 0 ✓.

:::

::: exemple 2x(3x − 6) = 0

1. العاملان هما 2x و (3x − 6).
2. إمّا 2x = 0 → x = **0**.
3. أو 3x − 6 = 0 → 3x = 6 → x = **2**.

:::

> ⚠️ **الخطأ الأشهر**: قراءة العامل (x + 5) كحلّ x = 5. العامل يساوي صفرًا لمّا يكون
> x = **−5**: الجذر هو **مقابل** العدد الظاهر في القوس. اقلب الإشارة دائمًا.

> 💡 الجداء المعدوم لا يعمل للجمع: a + b = 0 **لا** يعني a = 0 أو b = 0 — مثال: 7 + (−7) = 0.

::: verifie
حلّ (2x − 1)(x + 4) = 0.

---

إمّا 2x − 1 = 0 → 2x = 1 → x = **1/2** ؛ أو x + 4 = 0 → x = **−4**.
الحلّان: 1/2 و −4 — ولاحظ قلب الإشارة في العامل الثاني.
:::

::: retenir
جداء معدوم ⟹ أحد عامليه معدوم ؛ وجذر العامل هو **مقابل** ما تراه في القوس.
:::

## 🔮 تعريف المتراجحة من الدرجة الأولى

المعادلة تسأل: أيّ عدد **بالضبط**؟ لكن كثيرًا من المسائل لا تطلب عددًا واحدًا: «ما هي الكمّيات
التي يكفي ثمنها 20 دينارًا؟» الجواب ليس عددًا بل **منطقة كاملة** من الأعداد. والأداة التي
تصف منطقة هي المتراجحة.

::: definition
كلّ **لا مساواة** تؤول كتابتها إلى ax + b ≤ 0 أو ax + b < 0 أو ax + b ≥ 0 أو ax + b > 0، حيث a
عدد حقيقي معلوم **مخالف للصفر** و b عدد حقيقي معلوم و x عدد مجهول، تسمّى **متراجحة من الدرجة
الأولى ذات مجهول واحد** في ℝ.
:::

الحلّ ليس عددًا واحدًا بل **مجموعة من الأعداد** تُكتب على شكل مجال.

::: exemple ثلاث لا مساواة

1. 3x − 6 < 9 — متراجحة، ومجموعة حلولها مجال مفتوح.
2. −2x + 1 ≥ 7 — متراجحة أيضًا، والإشارة ≥ تعني أنّ الطرف مشمول.
3. x² > 4 — **ليست** من الدرجة الأولى: المجهول مربّع.

:::

::: verifie
أيّ ما يلي متراجحة من الدرجة الأولى؟ 4x + 1 ≤ 0 ، 5 > x² ، −x ≥ 2.

---

4x + 1 ≤ 0 : **نعم**. 5 > x² : **لا** (درجة ثانية). −x ≥ 2 : **نعم** — معاملها −1، وهو مخالف للصفر.
:::

::: retenir
المتراجحة تصف **منطقة** من الأعداد، لا عددًا واحدًا.
:::

## 🧪 حلّ المتراجحة من الدرجة الأولى

خذ اللا مساواة الصحيحة 2 < 5 واضرب الطرفين في −1: تصير −2 و −5. لكن −2 **أكبر** من −5! فالضرب
في عدد سالب قلب الترتيب. هذه الملاحظة الصغيرة هي الفرق الوحيد بين حلّ متراجحة وحلّ معادلة.

::: figure حلُّ المتراجحة نصفُ مستقيم: دائرةٌ مفتوحة عند < وممتلئة عند ≤، والسهمُ نحو الحلول
<svg viewBox="0 0 360 175"><path d="M20 56 H318" stroke="#1f2937" stroke-width="1.8"/><path d="M318 56 l-8 -4 v8 z" fill="#1f2937"/><path d="M34 52 V60" stroke="#1f2937" stroke-width="1.2"/><text x="34.0" y="73.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">-4</text><path d="M61 52 V60" stroke="#1f2937" stroke-width="1.2"/><text x="61.0" y="73.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">-3</text><path d="M88 52 V60" stroke="#1f2937" stroke-width="1.2"/><text x="88.0" y="73.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">-2</text><path d="M115 52 V60" stroke="#1f2937" stroke-width="1.2"/><text x="115.0" y="73.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">-1</text><path d="M142 52 V60" stroke="#1f2937" stroke-width="1.2"/><text x="142.0" y="73.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><path d="M169 52 V60" stroke="#1f2937" stroke-width="1.2"/><text x="169.0" y="73.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><path d="M196 52 V60" stroke="#1f2937" stroke-width="1.2"/><text x="196.0" y="73.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><path d="M223 52 V60" stroke="#1f2937" stroke-width="1.2"/><text x="223.0" y="73.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><path d="M250 52 V60" stroke="#1f2937" stroke-width="1.2"/><text x="250.0" y="73.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><path d="M277 52 V60" stroke="#1f2937" stroke-width="1.2"/><text x="277.0" y="73.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><path d="M304 52 V60" stroke="#1f2937" stroke-width="1.2"/><text x="304.0" y="73.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><path d="M24 49 H277" stroke="#b91c1c" stroke-width="4"/><circle cx="277" cy="49" r="5" fill="#ffffff" stroke="#b91c1c" stroke-width="2"/><text x="277.0" y="36.0" text-anchor="middle" font-size="12" font-weight="700" fill="#b91c1c" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x < 5</text><text x="150.5" y="36.0" text-anchor="middle" font-size="11" font-weight="700" fill="#b91c1c" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">]−∞ ; 5[</text><path d="M20 132 H318" stroke="#1f2937" stroke-width="1.8"/><path d="M318 132 l-8 -4 v8 z" fill="#1f2937"/><path d="M34 128 V136" stroke="#1f2937" stroke-width="1.2"/><text x="34.0" y="149.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">-4</text><path d="M61 128 V136" stroke="#1f2937" stroke-width="1.2"/><text x="61.0" y="149.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">-3</text><path d="M88 128 V136" stroke="#1f2937" stroke-width="1.2"/><text x="88.0" y="149.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">-2</text><path d="M115 128 V136" stroke="#1f2937" stroke-width="1.2"/><text x="115.0" y="149.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">-1</text><path d="M142 128 V136" stroke="#1f2937" stroke-width="1.2"/><text x="142.0" y="149.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><path d="M169 128 V136" stroke="#1f2937" stroke-width="1.2"/><text x="169.0" y="149.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><path d="M196 128 V136" stroke="#1f2937" stroke-width="1.2"/><text x="196.0" y="149.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><path d="M223 128 V136" stroke="#1f2937" stroke-width="1.2"/><text x="223.0" y="149.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><path d="M250 128 V136" stroke="#1f2937" stroke-width="1.2"/><text x="250.0" y="149.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><path d="M277 128 V136" stroke="#1f2937" stroke-width="1.2"/><text x="277.0" y="149.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><path d="M304 128 V136" stroke="#1f2937" stroke-width="1.2"/><text x="304.0" y="149.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1f2937" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><path d="M61 125 H314" stroke="#15803d" stroke-width="4"/><circle cx="61" cy="125" r="5" fill="#15803d" stroke="#15803d" stroke-width="2"/><text x="61.0" y="112.0" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x ≥ −3</text><text x="187.5" y="112.0" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">[−3 ; +∞[</text></svg>
:::

::: propriete
الخطوات **مطابقة لحلّ المعادلة**، مع قاعدة إضافية واحدة حاسمة:

| العملية                        | أثرها على إشارة التراجح |
| ------------------------------ | ----------------------- |
| الجمع أو الطرح بعدد من الطرفين | **لا تغيير** في الإشارة |
| الضرب أو القسمة بعدد **موجب**  | **لا تغيير** في الإشارة |
| الضرب أو القسمة بعدد **سالب**  | **قلب الإشارة**         |

:::

::: exemple 3x − 6 < 9 — لا قلب

1. نضيف 6 للطرفين: 3x < 15 — الجمع لا يمسّ الإشارة.
2. نقسم على 3، وهو **موجب**، فالإشارة تبقى: x < 5.
3. الحلّ: x ∈ ]−∞ ; 5[ — القوس مفتوح لأنّ 5 غير مشمول.

:::

::: exemple −2x + 1 ≤ 7 — مع القلب

1. نطرح 1 من الطرفين: −2x ≤ 6 — الطرح لا يمسّ الإشارة.
2. نقسم على −2، وهو **سالب**، فالإشارة **تنقلب**: x ≥ −3.
3. الحلّ: x ∈ [−3 ; +∞[ — القوس مغلق لأنّ −3 مشمول.
4. **التحقّق بعدد**: نأخذ x = 0 (وهو ≥ −3): −2(0) + 1 = 1، و 1 ≤ 7 ✓.

:::

> ⚠️ **الفخّ الأشهر**: نسيان قلب إشارة التراجح عند الضرب أو القسمة على عدد **سالب**. هذا الخطأ
> يقلب الحلّ تمامًا: تكتب x ≤ −3 بدل x ≥ −3، فتُجيب بالمنطقة المعاكسة كلّها.

> ⚠️ **خطأ القوس**: الخلط بين الطرف المشمول وغير المشمول. الإشارة < تعطي قوسًا **مفتوحًا** ودائرة
> فارغة ؛ والإشارة ≤ تعطي قوسًا **مغلقًا** ودائرة ممتلئة.

::: verifie
حلّ المتراجحة −3x + 2 < 11 ثمّ اكتب مجموعة الحلول بمجال.

---

نطرح 2: −3x < 9. نقسم على −3، وهو سالب، **فتنقلب** الإشارة: x > −3.
مجموعة الحلول: **]−3 ; +∞[** — قوس مفتوح لأنّ الإشارة > لا تشمل الطرف.
:::

::: retenir
سالبٌ في الضرب أو القسمة ⟹ **اقلب** إشارة التراجح. وإلّا فلا شيء يتغيّر.
:::

## ⚖️ المتراجحة المزدوجة

أحيانًا يكون المجهول محصورًا بين طرفَين في آن واحد، كأن يقال: «درجة الحرارة بين 18 و 25». كيف
نحلّ كتابةً تحمل ثلاثة أطراف بدل طرفين؟

::: propriete
نُجري العملية نفسها على **الأطراف الثلاثة** معًا — وقاعدة قلب الإشارة عند السالب تبقى سارية،
وتنطبق على التراجحين معًا.
:::

::: exemple −3 ≤ 2x − 5 < 7

1. نضيف 5 للأطراف الثلاثة: −3 + 5 ≤ 2x < 7 + 5، أي 2 ≤ 2x < 12.
2. نقسم الأطراف الثلاثة على 2، وهو **موجب**، فلا قلب: 1 ≤ x < 6.
3. الحلّ: x ∈ [1 ; 6[ — مغلق يسارًا لأنّ ≤، ومفتوح يمينًا لأنّ <.

:::

> 🗡️ إذا أُعطيت شرطَين منفصلَين (مثل x > 1 و x < 6) فالحلّ هو **تقاطع الشرطين**: 1 < x < 6؛ والحلول الصحيحة (الأعداد الطبيعية الممكنة) هنا هي 2 و3 و4 و5.

::: verifie
حلّ 1 < 3x + 4 ≤ 13.

---

نطرح 4 من الأطراف الثلاثة: −3 < 3x ≤ 9. نقسم على 3 وهو موجب فلا قلب: −1 < x ≤ 3.
مجموعة الحلول: **]−1 ; 3]**.
:::

::: retenir
ثلاثة أطراف، والعملية نفسها عليها جميعًا.
:::

## 📐 تمثيل حلول المتراجحة على المستقيم

مجموعة الحلول ]−∞ ; 5[ كتابةٌ مختصرة. لكن العين تفهم الرسم أسرع: نصف مستقيم يبدأ من نقطة
ويمتدّ في اتّجاه. والسؤال الوحيد الذي يبقى: هل النقطة نفسها من الحلول أم لا؟

::: methode أربع حالات

- **x > a**: سهم إلى اليمين من a مع دائرة **مفتوحة** عند a (غير مشمول).
- **x ≥ a**: سهم إلى اليمين من a مع دائرة **مملوءة** عند a (مشمول).
- **x < a**: سهم إلى اليسار من a مع دائرة مفتوحة.
- **a ≤ x ≤ b**: نظلّل القطعة بين a و b مع دوائر ملائمة على الطرفين.

:::

::: exemple x ≥ −3

1. الإشارة ≥ تشمل الطرف، إذن الدائرة عند −3 **مملوءة**.
2. الحلول أكبر من −3، إذن السهم يتّجه إلى **اليمين**.
3. والكتابة بمجال: [−3 ; +∞[ — القوس المغلق يقابل الدائرة الممتلئة، تمامًا.

:::

> ⚠️ **الخطأ الشائع**: دائرة ممتلئة مع إشارة صارمة (< أو >). الصرامة تعني أنّ الطرف **ليس**
> حلًّا: دائرة فارغة وقوس مفتوح.

::: verifie
مثّل مجموعة الحلول ]−∞ ; 2] ثمّ ]0 ; 4[.

---

]−∞ ; 2] : دائرة **ممتلئة** عند 2 وسهم إلى اليسار — لأنّ 2 مشمول.
]0 ; 4[ : دائرتان **فارغتان** عند 0 و 4 مع تظليل ما بينهما — الطرفان غير مشمولَين.
:::

::: retenir
الدائرة الممتلئة = قوس مغلق = طرف مشمول ؛ والفارغة = قوس مفتوح = طرف مستبعد.
:::

> 🏆 أتقنتَ أدوات المعادلات والمتراجحات! ستجدها في كلّ باب رياضي: الهندسة، الدوالّ، والمسائل التطبيقية. قاعدة قلب الإشارة هي الحارس الأمين لحلولك.
