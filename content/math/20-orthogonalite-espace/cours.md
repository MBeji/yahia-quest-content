# ⚔️ التعامد في الفضاء — سلاح العمودي على مستوٍ

> 💡 «في المستوي يكفي مستقيم واحد ليفرض التعامد. أمّا في الفضاء فلا يكفي أبدًا: من أراد أن يكون عموديًا على مستوٍ بأكمله، عليه أن يواجه **مستقيمين متقاطعين** منه في نفس النقطة.»

## 🏰 أستحضـر: لغة الوضعيات في الفضاء

قبل أن نتكلّم عن التعامد، نستحضر أربعة رموز وثلاث حالات.

- **الانتماء**: نقطة تنتمي إلى مستقيم أو إلى مستوٍ، فنكتب A ∈ (BC) و A ∈ (BCD) ؛ وإن لم تنتمِ نكتب A ∉ (BCD) .
- **الاحتواء**: مستقيم محتوى في مستوٍ، فنكتب (AB) ⊂ (ABC) ؛ وإن لم يكن محتوى فيه نكتب (AB) ⊄ (CDE) .
- **وضعيّة مستقيمين**: في الفضاء لمستقيمين ثلاث حالات لا رابع لها — متوازيان، أو متقاطعان، أو **ليسا في نفس المستوي**.

> 🗡️ **قاعدة أساسية**: مستقيمان في نفس المستوي يكونان **إمّا متوازيين وإمّا متقاطعين**. فإذا لم يكن مستقيمان لا متوازيين ولا متقاطعين، فهما حتمًا ليسا في نفس المستوي.

::: figure الحرفان (AB) و(CG) في المكعّب لا يتقاطعان ولا يتوازيان: إنّهما ليسا في نفس المستوي — وهي الحالة التي لا وجود لها في المستوي
<svg viewBox="0 0 235 205"><path d="M40 175 L150 175 L150 65 L40 65 Z" fill="#0f6e56" opacity="0.08"/><path d="M40 175 L150 175 L195 140 M40 175 L40 65 M150 175 L150 65 M195 140 L195 30 M40 65 L150 65 L195 30 L85 30 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M40 175 L85 140 L195 140 M85 140 L85 30" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M40 175 L150 175 M195 140 L195 30" fill="none" stroke="#0f6e56" stroke-width="3.5" stroke-linecap="round"/><g fill="#0f172a"><circle cx="40" cy="175" r="3.5"/><circle cx="150" cy="175" r="3.5"/><circle cx="195" cy="140" r="3.5"/><circle cx="85" cy="140" r="3.5"/><circle cx="40" cy="65" r="3.5"/><circle cx="150" cy="65" r="3.5"/><circle cx="195" cy="30" r="3.5"/><circle cx="85" cy="30" r="3.5"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="30" y="192" text-anchor="middle" fill="#0f172a">A</text><text x="158" y="192" text-anchor="middle" fill="#0f172a">B</text><text x="207" y="137" text-anchor="middle" fill="#0f172a">C</text><text x="74" y="154" text-anchor="middle" fill="#0f172a">D</text><text x="29" y="60" text-anchor="middle" fill="#0f172a">E</text><text x="159" y="60" text-anchor="middle" fill="#0f172a">F</text><text x="207" y="26" text-anchor="middle" fill="#0f172a">G</text><text x="74" y="24" text-anchor="middle" fill="#0f172a">H</text></g></svg>
:::

> 📐 **ذخيرة من السنوات السابقة، لا يستقيم هذا الفصل بدونها**:
>
> - في مثلث متقايس الأضلاع طول ضلعه a : الارتفاع يساوي (a√3)/2 ، ومركز الدائرة المحيطة به هو نقطة تقاطع متوسّطاته، يبعد عن كلّ رأس بـ **ثلثي** المتوسّط، وعن منتصف كلّ ضلع بـ **ثلثه**. إذن شعاع دائرته المحيطة يساوي (a√3)/3 .
> - في مربّع طول ضلعه a : القطر يساوي a√2 ، ومركزه يبعد عن كلّ رأس بـ (a√2)/2 .
> - **نظرية بيتاغور**: في مثلث قائم، مربّع الوتر يساوي مجموع مربّعي الضلعين الآخرين. و**عكسها**: إذا كان مربّع أطول ضلع يساوي مجموع مربّعي الضلعين الآخرين فالمثلث قائم.
> - **نسبة طاليس**: في مثلث، إذا كان (MN) موازيًا لـ(AB) مع M من [SA] و N من [SB] فإنّ SM/SA = SN/SB = MN/AB . ونستعملها في وجه جانبي من الهرم كلّما رسمنا فيه مستقيمًا موازيًا لضلع القاعدة.
> - **نظرية المنتصفين**: القطعة الواصلة بين منتصفَي ضلعين في مثلث موازية للضلع الثالث وتساوي نصفه.
> - **مساحة مثلث**: (1/2) × القاعدة × الارتفاع المتعلّق بها. وفي المثلث القائم يكفي نصف جداء الضلعين القائمين.

## ⚡ متى يكون مستقيم عموديًا على مستوٍ؟

::: figure المستقيم (SA) يقطع المستوي P في A ويعامد فيه مستقيمين متقاطعين (AB) و(AC): عندئذٍ فقط نقول إنّه عمودي على P
<svg viewBox="0 0 320 230"><path d="M35 185 L225 185 L280 135 L90 135 Z" fill="#0f6e56" opacity="0.12"/><path d="M35 185 L225 185 L280 135 L90 135 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M65 160 L245 160" fill="none" stroke="#0f6e56" stroke-width="2"/><path d="M130 182.5 L180 137.5" fill="none" stroke="#0f6e56" stroke-width="2"/><path d="M155 55 L155 160" fill="none" stroke="#0f172a" stroke-width="2.5"/><path d="M155 160 L155 200" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M155 150 L141 150 L141 160" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M155 146 L165 137 L165 151" fill="none" stroke="#0f172a" stroke-width="1.6"/><g fill="#0f172a"><circle cx="155" cy="160" r="4"/><circle cx="155" cy="55" r="4"/></g><g fill="#0f6e56"><circle cx="245" cy="160" r="4"/><circle cx="177" cy="140" r="4"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="142" y="177" text-anchor="middle" fill="#0f172a">A</text><text x="155" y="46" text-anchor="middle" fill="#0f172a">S</text><text x="257" y="158" text-anchor="middle" fill="#0f6e56">B</text><text x="187" y="132" text-anchor="middle" fill="#0f6e56">C</text><text x="58" y="177" text-anchor="middle" fill="#0f172a">P</text></g></svg>
:::

**تعريف** — مستقيم عمودي على مستوٍ هو مستقيم عمودي على **مستقيمين متقاطعين** من هذا المستوي **في نفس النقطة**.

⚠️ الشرطان معًا، ولا غنى عن أيّ منهما:

- **مستقيمان لا مستقيم واحد**: التعامد مع مستقيم واحد من المستوي لا يكفي؛ فحول أيّ مستقيم يوجد عدد لا نهائي من المستقيمات العمودية عليه، وأغلبها ليس عموديًا على المستوي.
- **متقاطعان لا متوازيان**: مستقيمان متوازيان من المستوي يعطيان نفس الاتّجاه، فمعاملتهما لا تضيف أيّ معلومة جديدة.

**نتيجة (نستعملها في كلّ تمرين تقريبًا)** — إذا كان مستقيم عموديًا على مستوٍ في نقطة، فهو عمودي على **كلّ** مستقيمات هذا المستوي المارّة من تلك النقطة.

> 🗡️ الاتّجاهان يعملان معًا: نُثبت العمودية على المستوي بمستقيمين اثنين، ثمّ نحصد منها عمودية على عدد لا نهائي من المستقيمات. هذا هو الربح الكامل للفصل.

## 🗡️ أوّل تطبيق: الموشور القائم

::: figure في الموشور القائم ABCDEF الحرف [BE] يعامد الضلعين (BA) و(BC) المتقاطعين في B: إذن (BE) عمودي على مستوي القاعدة (ABC)
<svg viewBox="0 0 250 220"><path d="M60 185 L190 185 L115 143 Z" fill="#0f6e56" opacity="0.12"/><path d="M60 90 L190 90 L115 48 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M60 185 L190 185" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M60 185 L60 90 M190 185 L190 90" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M60 185 L115 143 L190 185 M115 143 L115 48" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M60 174 L71 174 L71 185" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M60 166 L75 154.5 L75 173.5" fill="none" stroke="#0f172a" stroke-width="1.6"/><g fill="#0f172a"><circle cx="60" cy="185" r="3.5"/><circle cx="190" cy="185" r="3.5"/><circle cx="115" cy="143" r="3.5"/><circle cx="60" cy="90" r="3.5"/><circle cx="190" cy="90" r="3.5"/><circle cx="115" cy="48" r="3.5"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="199" y="200" text-anchor="middle" fill="#0f172a">A</text><text x="48" y="200" text-anchor="middle" fill="#0f172a">B</text><text x="105" y="159" text-anchor="middle" fill="#0f172a">C</text><text x="203" y="86" text-anchor="middle" fill="#0f172a">D</text><text x="48" y="86" text-anchor="middle" fill="#0f172a">E</text><text x="115" y="40" text-anchor="middle" fill="#0f172a">F</text></g></svg>
:::

في الموشور القائم ABCDEF (قاعدتاه ABC و DEF ، وأحرفه الجانبية [AD] و[BE] و[CF]) كلّ حرف جانبي عمودي على الوجهين القاعدتين. مثلًا (BE) عمودي على (BA) وعلى (BC) ، وهما مستقيمان متقاطعان في B من المستوي (ABC) ، إذن:

$$ (BE) ⊥ (ABC) $$

ومن النتيجة السابقة نستنتج مباشرة أنّ (BE) عمودي كذلك على المستقيم (BM) مهما كانت M نقطة من المستوي (ABC) مخالفة لـ B . ولهذا يكون المثلث BEM **قائم الزاوية في B** ، وهو المثلث الذي سنطبّق فيه بيتاغور.

> 🛡️ نفس الشيء في المكعّب وفي متوازي المستطيلات: كلّ حرف رأسي عمودي على مستوي القاعدة، لأنّه يعامد فيه ضلعين متقاطعين من القاعدة.

## 🏛️ الهرم المنتظم

::: figure الهرم المنتظم SABCD: رأسه S فوق مركز O للدائرة المحيطة بالقاعدة، والارتفاع [SO] عمودي على مستوي القاعدة
<svg viewBox="0 0 300 225"><path d="M70 185 C93.5 196 151.7 196 200 185 C248.3 174 268.5 156 245 145 C221.5 134 163.3 134 115 145 C66.7 156 46.5 174 70 185 Z" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M157.5 50 L70 185 L200 185 Z" fill="#0f6e56" opacity="0.10"/><path d="M157.5 50 L70 185 M157.5 50 L200 185 M157.5 50 L245 145 M70 185 L200 185 M200 185 L245 145" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M70 185 L115 145 L245 145 M157.5 50 L115 145 M70 185 L245 145 M200 185 L115 145 M157.5 50 L157.5 165" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M157.5 151 L171 148 L171 162" fill="none" stroke="#0f172a" stroke-width="1.6"/><g fill="#0f172a"><circle cx="157.5" cy="50" r="4"/><circle cx="70" cy="185" r="3.5"/><circle cx="200" cy="185" r="3.5"/><circle cx="245" cy="145" r="3.5"/><circle cx="115" cy="145" r="3.5"/><circle cx="157.5" cy="165" r="3.5"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="157.5" y="41" text-anchor="middle" fill="#0f172a">S</text><text x="57" y="201" text-anchor="middle" fill="#0f172a">A</text><text x="209" y="201" text-anchor="middle" fill="#0f172a">B</text><text x="258" y="141" text-anchor="middle" fill="#0f172a">C</text><text x="103" y="138" text-anchor="middle" fill="#0f172a">D</text><text x="169" y="179" text-anchor="middle" fill="#0f172a">O</text></g></svg>
:::

**تعريف** — الهرم المنتظم هو هرم قاعدته **مضلّع منتظم**، وينتمي رأسه إلى **المستقيم العمودي على مستوي القاعدة في مركز الدائرة المحيطة بهذا المضلّع**.

**خاصيّة** — في الهرم المنتظم، الأوجه الجانبية **مثلثات متقايسة**، وكلّ منها **متقايس الضلعين** قمّته الرئيسية رأس الهرم.

هكذا يكون التعامد هو **معرّف** الهرم المنتظم: لو تحرّك الرأس عن العمودي في المركز، لاختلّت الأوجه الجانبية وفقدت تقايسها.

_مثال_: في هرم منتظم SABCD قاعدته المربّع ABCD مركزه O ، المثلثات SAB و SBC و SCD و SDA متقايسة، وكلّ منها متقايس الضلعين قمّته S ، لأنّ SA = SB = SC = SD .

## 🛡️ التعامد يولّد التوازي

::: figure المستقيمان (D1) و(D2) عموديان على نفس المستوي P: هذا وحده يكفي ليكونا متوازيين
<svg viewBox="0 0 300 215"><path d="M30 180 L220 180 L275 130 L85 130 Z" fill="#0f6e56" opacity="0.12"/><path d="M30 180 L220 180 L275 130 L85 130 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M110 60 L110 158 M200 55 L200 158" fill="none" stroke="#0f6e56" stroke-width="2.5"/><path d="M110 158 L110 192 M200 158 L200 192" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M110 148 L122 148 L122 158" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M200 148 L212 148 L212 158" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M104 100 L110 107 L116 100 M194 100 L200 107 L206 100" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="110" cy="158" r="4"/><circle cx="200" cy="158" r="4"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="97" y="175" text-anchor="middle" fill="#0f172a">A</text><text x="214" y="175" text-anchor="middle" fill="#0f172a">B</text><text x="110" y="48" text-anchor="middle" fill="#0f6e56">D1</text><text x="200" y="43" text-anchor="middle" fill="#0f6e56">D2</text><text x="52" y="172" text-anchor="middle" fill="#0f172a">P</text></g></svg>
:::

قاعدتان متقابلتان تمامًا، وهما من أكثر ما يُستعمل في الامتحان:

- **مستقيمان عموديان على نفس المستوي هما مستقيمان متوازيان.**
- **مستويان عموديان على نفس المستقيم هما مستويان متوازيان.**

_مثال_: في متوازي المستطيلات ABCDEFGH ، الحرفان (AE) و(CG) عموديان كلاهما على مستوي القاعدة (ABC) ، إذن (AE) و(CG) متوازيان. وبنفس المنطق، المستويان (ABC) و(EFG) عموديان كلاهما على المستقيم (AE) ، إذن هما متوازيان.

## 🔮 الوجود والوحدانية

قاعدتان تُجيبان عن سؤال «كم واحدًا؟»:

- **من نقطة معلومة من الفضاء يمرّ مستوٍ واحد فقط عمودي على مستقيم معلوم.**
- **من نقطة معلومة من الفضاء يمرّ مستقيم واحد فقط عمودي على مستوٍ معلوم.**

::: figure من النقطة A الخارجة عن المستوي P يمرّ مستقيم واحد لا غير عمودي على P ، هو Δ ، ويقطعه في المسقط العمودي H
<svg viewBox="0 0 300 205"><path d="M30 180 L220 180 L275 130 L85 130 Z" fill="#0f6e56" opacity="0.12"/><path d="M30 180 L220 180 L275 130 L85 130 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M150 50 L150 155" fill="none" stroke="#0f6e56" stroke-width="2.5"/><path d="M150 155 L150 192" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M150 145 L163 145 L163 155" fill="none" stroke="#0f172a" stroke-width="1.6"/><g fill="#0f172a"><circle cx="150" cy="50" r="4"/><circle cx="150" cy="155" r="4"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="150" y="41" text-anchor="middle" fill="#0f172a">A</text><text x="136" y="172" text-anchor="middle" fill="#0f172a">H</text><text x="166" y="75" text-anchor="middle" fill="#0f6e56">Δ</text><text x="52" y="172" text-anchor="middle" fill="#0f172a">P</text></g></svg>
:::

> 🗡️ «واحد فقط» تعني شيئين في آن: **يوجد** (يمكن دائمًا رسمه) و**لا يوجد غيره**. وسواء كانت النقطة داخل المستوي أو خارجه، الجواب هو نفسه.

هذا المستقيم الوحيد العمودي على المستوي P والمارّ من نقطة A يقطع P في نقطة تُسمّى **المسقط العمودي** للنقطة A على المستوي P .

## 📐 قطر متوازي المستطيلات

::: figure في متوازي المستطيلات ABCDEFGH: المثلث EHC قائم في H، ومنه يُستخرج القطر EC من الأبعاد الثلاثة
<svg viewBox="0 0 300 225"><path d="M60 190 L190 190 L190 95 L60 95 Z" fill="#0f6e56" opacity="0.08"/><path d="M60 190 L190 190 L245 148 M60 190 L60 95 M190 190 L190 95 M245 148 L245 53 M60 95 L190 95 L245 53 L115 53 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M60 190 L115 148 L245 148 M115 148 L115 53" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M60 95 L245 148 M115 53 L245 148" fill="none" stroke="#0f6e56" stroke-width="2.2" stroke-dasharray="6 4"/><path d="M105 61 L115 69 L125 61" fill="none" stroke="#0f172a" stroke-width="1.6"/><g fill="#0f172a"><circle cx="60" cy="190" r="3.5"/><circle cx="190" cy="190" r="3.5"/><circle cx="245" cy="148" r="3.5"/><circle cx="115" cy="148" r="3.5"/><circle cx="60" cy="95" r="3.5"/><circle cx="190" cy="95" r="3.5"/><circle cx="245" cy="53" r="3.5"/><circle cx="115" cy="53" r="3.5"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="48" y="206" text-anchor="middle" fill="#0f172a">A</text><text x="198" y="206" text-anchor="middle" fill="#0f172a">B</text><text x="258" y="145" text-anchor="middle" fill="#0f172a">C</text><text x="103" y="162" text-anchor="middle" fill="#0f172a">D</text><text x="48" y="90" text-anchor="middle" fill="#0f172a">E</text><text x="201" y="90" text-anchor="middle" fill="#0f172a">F</text><text x="258" y="50" text-anchor="middle" fill="#0f172a">G</text><text x="103" y="46" text-anchor="middle" fill="#0f172a">H</text></g></svg>
:::

نضع AB = a و AE = b و AD = c . المسار في خطوتين:

1. المستقيم (HD) عمودي على مستوي القاعدة (ABC) ، فالمثلث HDC قائم في D ومنه HC² = DC² + DH² = a² + b² .
2. المستقيم (EH) عمودي على (HD) وعلى (HG) ، وهما مستقيمان متقاطعان في H من مستوي الوجه (DCG) ، إذن (EH) عمودي على هذا المستوي، فهو عمودي على كلّ مستقيماته المارّة من H ومنها (HC) . ومنه المثلث EHC قائم في H و EC² = EH² + HC² = c² + a² + b² .

**قاعدة** — في متوازي المستطيلات ABCDEFGH ، الأقطار [EC] و[HB] و[AG] و[DF] **متقايسة**، وقيس طول كلّ منها:

$$ √(AB² + AE² + AD²) $$

_مثال محسوب_: متوازي مستطيلات أبعاده 9 و 12 و 20 (بالصنتمتر). قطره يساوي √(81 + 144 + 400) = √625 = 25 cm .

_حالة المكعّب_: إذا كان حرف المكعّب a فإنّ أبعاده الثلاثة متساوية، ومنه القطر = √(a² + a² + a²) = √(3a²) = **a√3** .

> ⚠️ **الفخّ الأشهر**: جمع الأبعاد بدل جمع مربّعاتها. مع 9 و 12 و 20 يعطي الجمع 41 ، والقطر الحقيقي 25 . القطر أصغر دائمًا من مجموع الأبعاد.

## ⚔️ الحرف الجانبي للهرم المنتظم

::: figure المثلث SOA القائم في O: ساقاه الارتفاع h وشعاع الدائرة المحيطة R، ووتره الحرف الجانبي SA
<svg viewBox="0 0 300 210"><path d="M60 40 L60 170 L240 170 Z" fill="#0f6e56" opacity="0.10"/><path d="M60 40 L60 170 L240 170 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M60 152 L78 152 L78 170" fill="none" stroke="#0f172a" stroke-width="2"/><g fill="#0f172a"><circle cx="60" cy="40" r="4"/><circle cx="60" cy="170" r="4"/><circle cx="240" cy="170" r="4"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="49" y="34" text-anchor="middle" fill="#0f172a">S</text><text x="49" y="187" text-anchor="middle" fill="#0f172a">O</text><text x="251" y="187" text-anchor="middle" fill="#0f172a">A</text><text x="44" y="108" text-anchor="middle" fill="#0f6e56">h</text><text x="150" y="190" text-anchor="middle" fill="#0f6e56">R</text></g></svg>
:::

في الهرم المنتظم، سمّينا S الرأس و O مركز الدائرة المحيطة بالقاعدة و h = SO الارتفاع و R شعاع تلك الدائرة. المستقيم (SO) عمودي على مستوي القاعدة، إذن هو عمودي على (OA) مهما كان A رأسًا من القاعدة: المثلث SOA **قائم الزاوية في O** ، وبيتاغور يعطي SA² = h² + R² .

**قاعدة** — في الهرم المنتظم، قيس طول كلّ حرف من الأحرف الجانبية يساوي الجذر التربيعي لمجموع مربّعي الارتفاع وشعاع الدائرة المحيطة بالقاعدة:

$$ SA = √(h² + R²) $$

وبما أنّ R لا يتغيّر من رأس إلى آخر، فكلّ الأحرف الجانبية **متقايسة** — وهذا هو سبب تقايس الأوجه الجانبية.

> 🧭 **مفردة من المنهج**: إذا كانت H منتصف ضلع من القاعدة، فإنّ القطعة [SH] الواصلة من الرأس إلى منتصف ذلك الضلع تُسمّى **عمد الهرم**. وهي في الوقت نفسه ارتفاع الوجه الجانبي المتعلّق بذلك الضلع (لأنّ هذا الوجه متقايس الضلعين قمّته S)، ونحسبها بنفس المسار: المستقيم (SO) عمودي على مستوي القاعدة فهو عمودي على (OH) ، والمثلث SOH قائم في O ومنه SH² = SO² + OH² .

_مثال محسوب_: هرم منتظم قاعدته مربّع طول ضلعه 8 وارتفاعه 3 (بالصنتمتر). شعاع الدائرة المحيطة بالمربّع هو R = (8√2)/2 = 4√2 ومنه R² = 32 . إذن الحرف الجانبي يساوي √(9 + 32) = √41 cm .

## 🧭 مسألة محلولة: بيتاغور وعكسه في الفضاء

::: figure الموشور القائم ABCDEF بقاعدة قائمة في A: ثلاث مرّات بيتاغور ثمّ مرّة واحدة عكسه
<svg viewBox="0 0 260 225"><path d="M60 185 L190 185 L115 143 Z" fill="#0f6e56" opacity="0.10"/><path d="M60 90 L190 90 L115 48 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M60 185 L190 185 M60 185 L60 90 M190 185 L190 90" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M60 185 L115 143 L190 185 M115 143 L115 48" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M190 185 L60 90" fill="none" stroke="#0f6e56" stroke-width="2.2"/><path d="M60 90 L115 143" fill="none" stroke="#0f6e56" stroke-width="2.2" stroke-dasharray="6 4"/><path d="M178 185 L167.5 179 L179.5 179" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M60 174 L71 174 L71 185" fill="none" stroke="#0f172a" stroke-width="1.6"/><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="125" y="202" text-anchor="middle" fill="#0f6e56">3</text><text x="170" y="155" text-anchor="middle" fill="#0f6e56">2</text><text x="45" y="140" text-anchor="middle" fill="#0f6e56">5</text></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="201" y="200" text-anchor="middle" fill="#0f172a">A</text><text x="48" y="200" text-anchor="middle" fill="#0f172a">B</text><text x="105" y="159" text-anchor="middle" fill="#0f172a">C</text><text x="205" y="86" text-anchor="middle" fill="#0f172a">D</text><text x="48" y="86" text-anchor="middle" fill="#0f172a">E</text><text x="115" y="40" text-anchor="middle" fill="#0f172a">F</text></g></svg>
:::

**المعطيات** _(وحدة قيس الطول هي الصنتمتر)_ — ABCDEF موشور قائم قاعدته المثلث ABC القائم في A ، مع AB = 3 و AC = 2 و BE = 5 . المطلوب: احسب BC ثمّ AE ثمّ EC ، وبيّن أنّ المثلث AEC قائم.

**الحـلّ**

1. المثلث ABC قائم في A ، ومنه BC² = AB² + AC² = 9 + 4 = 13 ، إذن BC = √13 .
2. الحرف [BE] عمودي على مستوي القاعدة، فهو عمودي على (BA) : المثلث ABE قائم في B ومنه AE² = BE² + BA² = 25 + 9 = 34 ، إذن AE = √34 .
3. وهو عمودي كذلك على (BC) : المثلث EBC قائم في B ومنه EC² = BC² + BE² = 13 + 25 = 38 ، إذن EC = √38 .
4. في المثلث AEC نحسب AE² + AC² = 34 + 4 = 38 = EC² ، وحسب **عكس نظرية بيتاغور** يكون المثلث AEC **قائم الزاوية في A** .

> 🗡️ لاحظ المنهج: لم نستعمل إلّا العمودية على المستوي، وهي التي وفّرت لنا الزاويتين القائمتين في B . هذا هو المسار المطلوب في كلّ مسائل الفصل.

## 📋 أحوصــل — القواعد الستّ

1. مستقيم عمودي على مستوٍ في نقطة هو مستقيم عمودي على **كلّ** مستقيمات هذا المستوي المارّة من هذه النقطة.
2. مستقيم عمودي في نقطة على مستقيمين متقاطعين في نفس النقطة من مستوٍ هو عمودي على هذا المستوي.
3. مستقيمان عموديان على نفس المستوي هما متوازيان.
4. مستويان عموديان على نفس المستقيم هما متوازيان.
5. من نقطة معلومة من الفضاء يمرّ مستوٍ واحد عمودي على مستقيم معلوم.
6. من نقطة معلومة من الفضاء يمرّ مستقيم واحد عمودي على مستوٍ معلوم.

وتُضاف إليها نتيجتان في القيس: قطر متوازي المستطيلات √(AB² + AE² + AD²) ، والحرف الجانبي للهرم المنتظم √(h² + R²) .

> 🏆 أتقنت هذا الباب! صار بيدك مفتاحان: مفتاح يفتح التعامد (مستقيمان متقاطعان) ومفتاح يحسب الأطوال (بيتاغور). بهما تُحلّ كلّ مسائل الفضاء في التاسعة.
