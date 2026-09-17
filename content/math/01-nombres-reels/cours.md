# ⚔️ الأعداد الحقيقية — ساحة المعركة الأولى

> 💡 «قبل أن تخوض أيّ معركة حسابية، عليك أن تعرف عالم الأعداد الذي تقاتل فيه.»

## 🏰 عوالم الأعداد — لماذا لم يكفِ عالم واحد؟

عُدَّ تلاميذ قسمك: 28. عدد صحيح طبيعي، ولا حاجة إلى غيره. لكن سجّل درجة الحرارة في ليلة شتاء
بالقصرين: −3 °C، فقد خرجتَ من ℕ. زِن كيلوغرامًا ونصفًا من اللحم: 1,5 kg، فقد خرجتَ من ℤ. اقسم
رغيفًا على ثلاثة: 1/3، وقد خرجتَ من العشريّات. فهل ينتهي الأمر هنا، أم يوجد عدد لا يُكتب حتى
على شكل كسر؟

::: figure عوالم الأعداد متداخلة: ℕ داخل ℤ داخل 𝔻 داخل ℚ داخل ℝ، ولا يبقى خارج ℚ إلّا الأعداد الصمّاء
<svg viewBox="0 0 360 200"><rect x="12" y="10" width="336" height="180" rx="10" fill="#0f6e56" fill-opacity="0.12" stroke="#0f6e56" stroke-width="2"/><rect x="34" y="32" width="292" height="136" rx="10" fill="#ffffff" stroke="#0f6e56" stroke-width="2"/><rect x="56" y="54" width="248" height="92" rx="10" fill="#0f6e56" fill-opacity="0.12" stroke="#0f6e56" stroke-width="2"/><rect x="78" y="76" width="204" height="52" rx="10" fill="#ffffff" stroke="#0f6e56" stroke-width="2"/><rect x="100" y="96" width="160" height="24" rx="8" fill="#0f6e56" fill-opacity="0.12" stroke="#0f6e56" stroke-width="2"/><text x="30" y="27" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">ℝ</text><text x="52" y="49" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">ℚ</text><text x="74" y="71" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">𝔻</text><text x="96" y="92" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">ℤ</text><text x="118" y="113" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">ℕ</text><text x="252" y="27" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">√2</text><text x="300" y="27" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">π</text><text x="246" y="49" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−5/3</text><text x="296" y="49" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2/3</text><text x="238" y="71" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,25</text><text x="288" y="71" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−3,4</text><text x="222" y="92" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−5</text><text x="262" y="92" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−12</text><text x="180" y="113" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0</text><text x="214" y="113" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">7</text></svg>
:::

في الشكل، كلّ إطار يحتوي الذي قبله تمامًا كما احتاج كلّ مثال أعلاه إلى عالم أوسع من سابقه.

::: definition
نرتّب عوالم الأعداد من الأصغر إلى الأكبر، وكلّ عالم يحتوي ما قبله:

- **ℕ** الأعداد الصحيحة الطبيعية: 0، 1، 2، 3، …
- **ℤ** الأعداد الصحيحة النسبية: …، −2، −1، 0، 1، 2، …
- **𝔻** الأعداد العشرية: لها كتابة عشرية تتوقّف، مثل 4,7 أو −0,006.
- **ℚ** الأعداد الكسرية النسبية: تُكتب على شكل كسر a/b حيث a وb صحيحان نسبيان وb ≠ 0.
- **ℝ** الأعداد الحقيقية: كلّ عدد يمثّل فاصلة نقطة من المستقيم العددي.

$$ ℕ ⊂ ℤ ⊂ 𝔻 ⊂ ℚ ⊂ ℝ $$
:::

::: exemple قراءة الرمزين ∈ و ⊂

1. نستعمل ∈ بين **عدد ومجموعة**: 6 ∈ ℕ، ونقرأ «العدد 6 ينتمي إلى ℕ» — لأنّ 6 عدد صحيح طبيعي.
2. و −8 ∉ ℕ لأنّ ℕ لا تحتوي الأعداد السالبة، لكنّ −8 ∈ ℤ — فالسالب يحتاج عالمًا أوسع.
3. ونستعمل ⊂ بين **مجموعتين**: ℤ ⊂ ℚ، ونقرأ «ℤ محتواة في ℚ» — لأنّ كلّ عدد صحيح نسبي n يُكتب
   كسرًا n/1.
4. أمّا ℝ ⊄ ℚ فلأنّ في ℝ أعدادًا ليست كسرية، وسنلقاها بعد قليل.

:::

> ⚠️ **الخطأ الشائع**: قلب سلسلة الاحتواء، فيُكتب ℝ ⊂ ℚ. السلسلة تسير من **الأصغر إلى الأكبر**:
> ℕ ⊂ ℤ ⊂ 𝔻 ⊂ ℚ ⊂ ℝ. وخطأ قريب منه: الخلط بين ما تحتويه كلّ مجموعة — ℤ فيها السوالب، و𝔻 فيها
> العشريّات المتناهية فقط، فالعدد 1/3 ∉ 𝔻 رغم أنّه كسري.

::: propriete
كلّ عدد صحيح طبيعي هو عدد صحيح نسبي، وكلّ عدد صحيح نسبي هو عدد كسري — **والعكس غير صحيح**.
ونرمز بـ ℝ+ لمجموعة الأعداد الحقيقية الموجبة، وبـ ℝ− للسالبة، ولنا ℝ = ℝ+ ∪ ℝ−.
حالة حدّية تستحقّ الانتباه: العدد 0 موجب وسالب في آنٍ، فهو ينتمي إلى ℝ+ وإلى ℝ− معًا.
:::

::: verifie
أعطِ عددًا ينتمي إلى ℚ ولا ينتمي إلى 𝔻، ثمّ عددًا ينتمي إلى 𝔻 ولا ينتمي إلى ℤ، ثمّ أتمم
بالرمز المناسب: 2/3 … ℤ و −5 … ℚ.

---

1/3 ∈ ℚ ولا ينتمي إلى 𝔻، لأنّ كتابته العشرية 0,333… لا تتوقّف.
−0,4 ∈ 𝔻 ولا ينتمي إلى ℤ، لأنّ كتابته العشرية تتوقّف لكنّه ليس عددًا صحيحًا.
2/3 ∉ ℤ لأنّ 2 لا يقبل القسمة على 3 ؛ و −5 ∈ ℚ لأنّ كلّ صحيح نسبي كسريّ.
:::

::: retenir
ℕ ⊂ ℤ ⊂ 𝔻 ⊂ ℚ ⊂ ℝ : الرمز ∈ بين عدد ومجموعة، والرمز ⊂ بين مجموعتين.
:::

## 🔢 الكتابات العشرية لعدد كسري

خذ آلتك الحاسبة واقسم: 12,5 ÷ 7 ثمّ 17 ÷ 9 ثمّ 4 ÷ 3 ثمّ 3 ÷ 22. ماذا تلاحظ؟ لا واحدة من هذه
القسمات تتوقّف، لكنّ شيئًا فيها **يتكرّر**. فهل تنتهي قسمة عدد كسري دائمًا إلى هذا التكرار؟

::: propriete
عندما نُنجز قسمة عدد كسري نحصل دائمًا على إحدى الحالتين، ولا ثالثة لهما:

- **كتابة عشرية متناهية** (écriture décimale finie) (تتوقّف): 3/8 = 0,375 و 9/4 = 2,25.
- **كتابة عشرية دوريّة غير متناهية** (écriture décimale illimitée périodique): مجموعة من الأرقام تتكرّر بلا توقّف.

لكلّ عدد كسري نسبي كتابة عشرية دوريّة، وكلّ كتابة عشرية دوريّة تمثّل عددًا كسريًّا وحيدًا.
والكتابة المتناهية ليست إلّا حالة خاصّة: دورها الرقم 0، فـ 5,6 = 5,6(0).
:::

::: exemple القسمة 3 ÷ 22 والدور

1. ننجز القسمة فنجد 3/22 = 0,13636363… — والأرقام لا تتوقّف.
2. نلاحظ أنّ المجموعة 36 تتكرّر بصفة دوريّة؛ نسمّيها **الدور** — لأنّها تعود بالترتيب نفسه بلا نهاية.
3. نكتبها بين قوسين لاختصار الكتابة:
   $$ 3/22 = 0,1(36) $$

:::

::: methode البحث عن رقم في رتبة معيّنة
بما أنّ الدور يتكرّر بانتظام، يكفي أن نقسم رتبة الرقم على طول الدور وننظر إلى **الباقي**.
_تطبيق_: 1/7 = 0,(142857) وطول دورها 6. ما الرقم الذي رتبته 20 بعد الفاصل؟ نحسب
20 = 6 × 3 + 2، والباقي 2 يدلّ على الرقم الثاني من الدور 142857، وهو **4**.
:::

::: verifie
العدد 1/11 = 0,(09). ما طول دوره؟ وما الرقم الذي رتبته 15 بعد الفاصل؟

---

طول الدور 2، لأنّ المجموعة 09 هي التي تتكرّر.
نحسب 15 = 2 × 7 + 1، والباقي 1 يدلّ على الرقم الأوّل من الدور 09، وهو **0**.
:::

::: retenir
كلّ عدد كسري كتابته العشرية دوريّة، والدور هو ما يتكرّر بلا توقّف.
:::

## ⚡ الأعداد الصمّاء — حين لا يوجد أيّ دور

رأيتَ أنّ كلّ كسر ينتهي إلى دور. اكتب الآن العدد 2,101001000100001… حيث يزيد عدد الأصفار في كلّ
مرّة. كتابته لا تتوقّف — وهذا معتاد — لكن **لا شيء فيها يتكرّر بانتظام**. فهل هو كسر؟

::: definition
العدد الذي كتابته العشرية **غير متناهية وغير دوريّة** معًا يسمّى **عددًا أصمّ** (irrationnel)، ولا يمكن كتابة
أيّ منه على شكل كسر. أمثلة: √2 = 1,414213562… و π = 3,141592653… والعدد أعلاه.
:::

::: propriete
مجموعة الأعداد الحقيقية ℝ هي اتّحاد مجموعة الأعداد الكسرية ℚ ومجموعة الأعداد الصمّاء، ونرمز
لهذه الأخيرة بالرمز **I**، فنكتب: ℝ = ℚ ∪ I.
:::

::: exemple كيف نحكم على طبيعة عدد

1. العدد 0,272727… **ناطق** — لأنّ المجموعة 27 تتكرّر بانتظام، فله دور، وكلّ ذي دور كسريّ.
2. العدد 0,272277222777… **أصمّ** — لأنّ عدد الأرقام يتغيّر في كلّ مجموعة، فلا دور له.
3. العدد √16 **ناطق** — لأنّنا نحسب أوّلًا: √16 = 4، وهو عدد صحيح.
4. العدد 1 + √3 **أصمّ** — لأنّ إضافة عدد ناطق إلى عدد أصمّ لا تُنهي كتابته ولا تُدوّرها.

:::

> 🛡️ **لماذا √2 ليس عددًا كسريًّا؟** نستعمل **الاستدلال بالخلف**. نفترض أنّ √2 = a/b حيث a وb
> عددان صحيحان طبيعيان أوليان فيما بينهما. بالتربيع: a² = 2b²، إذن a² زوجي ومنه a زوجي،
> فنكتب a = 2p. بالتعويض: 4p² = 2b² أي b² = 2p²، إذن b² زوجي ومنه b زوجي. فالعددان a وb
> زوجيان معًا، وهذا يناقض كونهما أوليين فيما بينهما. الافتراض مرفوض إذن: العدد √2 ليس كسريًّا.

> ⚠️ **الفخّ الأشهر**: الظنّ أنّ وجود رمز الجذر يجعل العدد أصمّ. الصحيح أنّ √49 = 7 عدد ناطق؛
> العدد يكون أصمّ فقط إذا لم يكن ما تحت الجذر مربّعًا. والفخّ المعاكس موجود أيضًا: الحكم بأنّ
> عددًا أصمّ لأنّ كتابته تبدو معقّدة، بينما √(4/9) = 2/3 كسريّ تمامًا.

وطبيعة الناتج لا تُقرأ من شكل الكتابة: العبارة √2 + (−√2) تساوي 0 وهو عدد صحيح، بينما √2 + 1
يبقى عددًا أصمّ. **احسب أوّلًا، ثمّ احكم.**

::: verifie
صنّف: √36 و √7 و 0,25 و π/π. أيّها ناطق وأيّها أصمّ؟

---

√36 = 6 **ناطق**، لأنّ 36 مربّع كامل.
√7 **أصمّ**، لأنّ 7 ليس مربّعًا كاملًا.
0,25 = 1/4 **ناطق**، لأنّ كتابته العشرية متناهية.
π/π = 1 **ناطق**: الرمز π يظهر في الكتابة، لكنّ الحساب يعطي 1 — احسب أوّلًا ثمّ احكم.
:::

::: retenir
عدد أصمّ = كتابة عشرية لا تتوقّف ولا تتكرّر، ولا يُكتب كسرًا ؛ و ℝ = ℚ ∪ I.
:::

## 📐 الجذر التربيعي — أيّ عدد موجب مربّعه 16؟

سؤال المنهج بحرفه: ما العدد الكسري الموجب الذي يساوي مربّعه 16؟ الجواب 4، لأنّ 4² = 16. وما
العدد الذي مربّعه 81؟ وما العدد الذي مربّعه 2؟ السؤالان الأوّلان سهلان، والثالث هو الذي فتح
باب هذا الفصل كلّه.

::: definition
الجذر التربيعي لعدد حقيقي (réel) موجب a هو العدد الحقيقي **الموجب** b الذي مربّعه يساوي a:
$$ √a = b ⟺ a = b² $$
:::

::: exemple ثلاثة جذور بالبحث عن المربّع

1. √49 = 7 — لأنّ 7² = 49، ولأنّ 7 موجب.
2. √0,04 = 0,2 — لأنّ (0,2)² = 0,04.
3. √(4/9) = 2/3 — لأنّ (2/3)² = 4/9، والجذر يوزَّع على البسط والمقام.

:::

> ⚠️ **الخطأ الشائع**: الخلط بين المعادلة والرمز. المعادلة x² = a (حيث a > 0) لها **حلّان**:
> العدد √a والعدد −√a، لأنّ العددين المتقابلين لهما المربّع نفسه. أمّا الرمز √a فيدلّ على الحلّ
> الموجب وحده. _مثال_: المعادلة x² = 81 حلّاها 9 و −9، ومجموعة حلولها {−9 ; 9}، لكنّ √81 = 9 فقط.

**من أين يأتي العدد √2 ؟** من الهندسة. نأخذ مربّعًا ABCD طول ضلعه 2 cm، ونصل منتصفات أضلاعه
I وJ وK وL. المثلثات الأربعة الناتجة متقايسة، والرباعي IJKL مربّع مساحته نصف مساحة ABCD.
وبما أنّ مساحة المربّع تساوي مربّع طول ضلعه، فإنّ طول ضلع IJKL هو العدد a الذي يحقّق a² = 2،
ونكتب a = √2.

::: figure المربّع الداخلي IJKL مساحته نصف مساحة ABCD، أي 2 cm²، فطول ضلعه هو العدد الذي مربّعه 2
<svg viewBox="0 0 300 220"><rect x="70" y="30" width="140" height="140" fill="none" stroke="#0f172a" stroke-width="2"/><polygon points="140,30 210,100 140,170 70,100" fill="#0f6e56" fill-opacity="0.12" stroke="#0f6e56" stroke-width="2"/><circle cx="140" cy="30" r="3" fill="#0f172a"/><circle cx="210" cy="100" r="3" fill="#0f172a"/><circle cx="140" cy="170" r="3" fill="#0f172a"/><circle cx="70" cy="100" r="3" fill="#0f172a"/><text x="60" y="24" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A</text><text x="220" y="24" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">B</text><text x="220" y="184" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">C</text><text x="60" y="184" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D</text><text x="140" y="20" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">I</text><text x="228" y="105" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">J</text><text x="140" y="190" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">K</text><text x="54" y="105" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">L</text><text x="140" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">a² = 2</text><text x="140" y="116" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">a = √2</text><text x="140" y="210" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">AB = 2 cm</text></svg>
:::

::: methode الحصر والقيم التقريبية
كتابة √2 العشرية لا تتوقّف، فنحيطه بعددين نعرفهما، ونقارن **بالمربّعات**:

1. نحسب 1² = 1 و 2² = 4، وبما أنّ 1 < 2 < 4 نستنتج الحصر 1 < √2 < 2.
2. نُدقّق بأعداد عشرية: (1,4)² = 1,96 و (1,5)² = 2,25، ومنه 1,4 < √2 < 1,5.
3. العدد 1,4 هو **قيمة تقريبية بالنقصان** (valeur approchée par défaut) (الحدّ الأصغر)، والعدد 1,5 **بالزيادة** (الحدّ الأكبر).
4. وبرقمين بعد الفاصل: (1,41)² = 1,9881 و (1,42)² = 2,0164، وبما أنّ 1,9881 < 2 < 2,0164 فإنّ
   1,41 < √2 < 1,42.

:::

وبالطريقة نفسها نحصر π: لدينا 3,14 < π < 3,15، فالعدد 3,14 قيمة تقريبية بالنقصان للعدد π،
والعدد 3,15 قيمة تقريبية بالزيادة له.

> ⚠️ **الخطأ الشائع**: قلب النقصان والزيادة. القيمة **بالنقصان** تبقى **تحت** العدد، والقيمة
> **بالزيادة** تبقى **فوقه**. في الحصر 1,4 < √2 < 1,5 الحدّ الأيسر هو النقصان دائمًا.

::: verifie
احصر العدد √5 بين عددين صحيحين متتاليين، ثمّ أعطِ قيمة تقريبية بالنقصان له برقم واحد بعد الفاصل.

---

2² = 4 و 3² = 9، وبما أنّ 4 < 5 < 9 فإنّ 2 < √5 < 3.
ثمّ (2,2)² = 4,84 و (2,3)² = 5,29، وبما أنّ 4,84 < 5 < 5,29 فإنّ 2,2 < √5 < 2,3.
القيمة التقريبية **بالنقصان** برقم واحد بعد الفاصل هي **2,2**، لأنّها الحدّ الأصغر في الحصر.
:::

::: retenir
√a هو العدد الموجب الذي مربّعه a ؛ ونحصره بمقارنة المربّعات، لا بالتخمين.
:::

## 📏 تدريج مستقيم بواسطة الأعداد الحقيقية

ارسم مستقيمًا مدرّجًا وضع عليه النقطة A التي فاصلتها 2. سهل. والآن ضع النقطة C التي فاصلتها
12/5، والنقطة D التي فاصلتها 19/4. أين تقع كلّ منهما بالضبط؟ وهل لكلّ نقطة من المستقيم فاصلةٌ
ما، حتى لو كانت عددًا أصمّ؟

::: definition
نختار على المستقيم نقطة O تسمّى **أصل التدريج**، ونقطة I تسمّى **النقطة الواحدية**؛ والمسافة OI
هي **وحدة التدريج** (unité de graduation). يصير المستقيم (OI) عندئذ **المستقيم العددي** (droite graduée)، وإذا كانت x فاصلة النقطة M
نكتب M(x).
:::

::: exemple وضع 12/5 و 19/4 وقياس بُعدهما

1. 12/5 = 2,4 — فالنقطة C تقع بين 2 و3، وأقرب إلى 2.
2. 19/4 = 4,75 — فالنقطة D تقع بين 4 و5، وأقرب إلى 5.
3. البعد CD هو عدد وحدات التدريج بينهما: CD = 4,75 − 2,4 = **2,35** — لأنّ البعد يُحسب بطرح
   الفاصلة الصغرى من الكبرى.

:::

::: propriete

- نصف المستقيم [OI) يمثّل الأعداد الحقيقية الموجبة، ونصف المستقيم المقابل يمثّل السالبة.
- **مناظر** نقطة بالنسبة إلى الأصل O تنقلب إشارة فاصلته: مناظر M(x) هو M′(−x).
- البعد بين نقطتين هو عدد وحدات التدريج التي تفصل بينهما: إذا كانت A(−1,5) وB(2) فإنّ AB = 3,5.

:::

ونكتب 2√2 للدلالة على 2 × √2، وبما أنّ √2 ≈ 1,414 فإنّ 2√2 ≈ 2,83.

::: figure حتّى الأعداد الصمّاء لها مواضع دقيقة على المستقيم العددي: √2 بين 1 و2، وπ بين 3 و4
<svg viewBox="0 0 440 112"><line x1="20" y1="74" x2="414" y2="74" stroke="#0f172a" stroke-width="2"/><polygon points="414,68 430,74 414,80" fill="#0f172a"/><line x1="40" y1="68" x2="40" y2="80" stroke="#0f172a" stroke-width="2"/><line x1="110" y1="68" x2="110" y2="80" stroke="#0f172a" stroke-width="2"/><line x1="180" y1="68" x2="180" y2="80" stroke="#0f172a" stroke-width="2"/><line x1="250" y1="68" x2="250" y2="80" stroke="#0f172a" stroke-width="2"/><line x1="320" y1="68" x2="320" y2="80" stroke="#0f172a" stroke-width="2"/><line x1="390" y1="68" x2="390" y2="80" stroke="#0f172a" stroke-width="2"/><circle cx="209" cy="74" r="4.5" fill="#0f6e56"/><circle cx="330" cy="74" r="4.5" fill="#0f6e56"/><text x="40" y="96" text-anchor="middle" font-size="12" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−1</text><text x="110" y="96" text-anchor="middle" font-size="12" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0</text><text x="180" y="96" text-anchor="middle" font-size="12" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text><text x="250" y="96" text-anchor="middle" font-size="12" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text><text x="320" y="96" text-anchor="middle" font-size="12" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text><text x="390" y="96" text-anchor="middle" font-size="12" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4</text><text x="110" y="62" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text><text x="180" y="62" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">I</text><text x="209" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M(√2)</text><text x="332" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">N(π)</text></svg>
:::

في الشكل، √2 ليس تقريبًا موضوعًا على عجل: موضعه محدّد تمامًا، لأنّه فاصلة نقطة وحيدة.

> 🗡️ **القاعدة الكبرى للفصل**: كلّ عدد حقيقي يمثّل فاصلة نقطة وحيدة من المستقيم العددي، وكلّ
> نقطة من المستقيم تمثّل عددًا حقيقيًّا وحيدًا. لا توجد «ثقوب» في المستقيم العددي.

::: verifie
النقطة C فاصلتها 12/5. ما فاصلة مناظرتها C′ بالنسبة إلى O؟ وما البعد C′A إذا كانت A(2)؟

---

فاصلة C′ هي **−2,4**، لأنّ المناظرة بالنسبة إلى الأصل تقلب إشارة الفاصلة.
C′A = 2 − (−2,4) = **4,4** وحدة، لأنّ البعد هو الفرق بين الفاصلتين، من الصغرى إلى الكبرى.
:::

::: retenir
لكلّ عدد حقيقي نقطةٌ وحيدة على المستقيم، ولكلّ نقطةٍ عددٌ وحيد: لا ثقوب.
:::

> 🏆 أتقنت البوّابة الأولى! الأعداد الحقيقية هي أرضيّة كلّ ما سيأتي: العمليّات على الجذور،
> الترتيب، الحساب الحرفي، والمعادلات.
