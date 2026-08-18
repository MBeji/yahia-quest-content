# 🛡️ أنشطة حول الرباعيات — ورشة البرهان

> 💡 «في الهندسة لا يكفي أن ترى الشكل لتقول ما هو: عليك أن **تُثبت** أنّه هو. وكلّ إثبات ينطلق من خاصيّة، لا من رسم.»

ورشة لا فصل قواعد جديدة: نستعمل مكتسباتنا عن الرباعيات لنبرهن على **طبيعة رباعي** داخل وضعيات مركّبة.

## 🗝️ عدّة البداية: الرباعيات المألوفة (من مكتسبات السنوات السابقة)

| الرباعي            | تعريفه                                     | أضلاعه              | قطراه                                      |
| ------------------ | ------------------------------------------ | ------------------- | ------------------------------------------ |
| **متوازي الأضلاع** | أضلاعه المتقابلة متوازية مثنى مثنى         | المتقابلان متقايسان | يتقاطعان في منتصفيهما                      |
| **المستطيل**       | متوازي أضلاع له زاوية قائمة                | المتقابلان متقايسان | متقايسان، ويتقاطعان في منتصفيهما           |
| **المعيّن**        | متوازي أضلاع له ضلعان متتاليان متقايسان    | الأربعة متقايسة     | متعامدان، ويتقاطعان في منتصفيهما           |
| **المربّع**        | مستطيل ومعيّن في آن واحد                   | الأربعة متقايسة     | متقايسان ومتعامدان، ويتقاطعان في منتصفيهما |
| **شبه المنحرف**    | رباعي له ضلعان متقابلان متوازيان (قاعدتاه) | لا خاصيّة عامّة     | لا خاصيّة عامّة                            |

> 🗡️ الاحتواء ليس ترتيب السطور: **كلّ مربّع هو مستطيل ومعيّن معا**، وكلّ مستطيل وكلّ معيّن هو
> متوازي أضلاع، وكلّ متوازي أضلاع هو شبه منحرف. أمّا المستطيل والمعيّن فلا يرث أحدهما الآخر:
> التقايس خاصيّة قطري المستطيل، والتعامد خاصيّة قطري المعيّن.

::: figure في متوازي الأضلاع القطران يتقاطعان في نقطة واحدة O هي منتصف كلّ منهما — العلامات المتماثلة تدلّ على التقايس
<svg viewBox="0 0 340 240">
<path d="M60 60 L240 60 L280 180 L100 180 Z" fill="#0f6e56" opacity="0.12"/>
<path d="M60 60 L240 60 L280 180 L100 180 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M60 60 L280 180 M240 60 L100 180" fill="none" stroke="#0f6e56" stroke-width="2"/>
<g stroke="#0f172a" stroke-width="2" stroke-linecap="round" fill="none">
<path d="M111 96 L119 84"/>
<path d="M221 156 L229 144"/>
<path d="M200 86 L206 94"/><path d="M204 84 L210 92"/>
<path d="M130 146 L136 154"/><path d="M134 144 L140 152"/>
</g>
<g fill="#0f172a"><circle cx="60" cy="60" r="4"/><circle cx="240" cy="60" r="4"/><circle cx="280" cy="180" r="4"/><circle cx="100" cy="180" r="4"/></g>
<circle cx="170" cy="120" r="4.5" fill="#0f6e56"/>
<g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="48" y="52" text-anchor="middle" fill="#0f172a">A</text>
<text x="252" y="52" text-anchor="middle" fill="#0f172a">B</text>
<text x="294" y="196" text-anchor="middle" fill="#0f172a">C</text>
<text x="88" y="196" text-anchor="middle" fill="#0f172a">D</text>
<text x="180" y="110" text-anchor="middle" fill="#0f6e56">O</text>
</g>
</svg>
:::

## ⚔️ كيف نُثبت أنّ رباعيا متوازي أضلاع؟ أربع طرق

> 🛡️ **القاعدة**: يكفي أن تتحقّق **إحدى** الطرق التالية ليكون ABCD متوازي أضلاع: (1) أضلاعه
> المتقابلة **متوازية** مثنى مثنى — وهو التعريف؛ (2) **قطراه [AC] و[BD] لهما نفس المنتصف**؛
> (3) له **ضلعان متقابلان متوازيان ومتقايسان**؛ (4) أضلاعه المتقابلة **متقايسة** مثنى مثنى.

الطريقة 2 هي **سلاح هذا الفصل**: كلّما رأيت «منتصف» أو «نظير نقطة بالنسبة إلى نقطة» فكّر فيها فورا،
لأنّ «D نظير B بالنسبة إلى O» تعني بالضبط «O منتصف [BD]». _مثال_ — ABC مثلث وO منتصف [AC] وD نظير
B بالنسبة إلى O: فـ O منتصف [BD] و[AC] معا، إذن **ABCD متوازي أضلاع**.

> ⚠️ **فخّ الترتيب**: اكتب الاسم بحيث يكون القطران **حرفين متقابلين** فيه. إذا كان لـ [AC] و[BD] نفس
> المنتصف فالمتوازي هو **ABCD** لا ABDC، وإلاّ حصلت على رباعي متقاطع الأضلاع لا معنى له.

## 🔷 من متوازي الأضلاع إلى المستطيل والمعيّن والمربّع

> 🛡️ **القاعدة**: ليكن ABCD **متوازي أضلاع**: فإن كانت له **زاوية قائمة** أو كان **قطراه متقايسين**
> (AC = BD) فهو **مستطيل**؛ وإن كان له **ضلعان متتاليان متقايسان** أو كان **قطراه متعامدين** فهو
> **معيّن**؛ وإن اجتمع الشرطان (قطران متقايسان **و** متعامدان) فهو **مربّع**.

_مثال_ — ABC قائم الزاوية في B، وI منتصف [AC]، وD حيث I منتصف [BD]: للقطرين [AC] و[BD] نفس المنتصف
فـ ABCD متوازي أضلاع، و BI = AC/2 (الموسط المتعلّق بالوتر) أي BD = 2 BI = AC، فالقطران متقايسان
و**ABCD مستطيل**.

> ⚠️ **الفخّ الأكبر**: «متقايسان» و«متعامدان» و«يتقاطعان في منتصفيهما» لا تُغني إحداها عن الأخرى.
> **رباعي قطراه متقايسان ومتعامدان ليس بالضرورة مربّعا**: إن لم يتقاطعا في منتصفيهما فهو ليس حتّى
> متوازي أضلاع. وتذكّر أنّ قطري المستطيل **ليسا** متعامدين.

::: figure مثال مضادّ: القطران متقايسان (علامة واحدة على كلّ منهما) ومتعامدان، ومع ذلك ليس مربّعا لأنّهما لا يتقاطعان في منتصفيهما
<svg viewBox="0 0 320 235">
<path d="M160 40 L240 90 L160 200 L80 90 Z" fill="#0f6e56" opacity="0.10"/>
<path d="M160 40 L240 90 L160 200 L80 90 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M160 40 L160 200 M80 90 L240 90" fill="none" stroke="#0f6e56" stroke-width="2"/>
<path d="M160 90 L172 90 L172 102" fill="none" stroke="#0f172a" stroke-width="2"/>
<g stroke="#0f172a" stroke-width="2" stroke-linecap="round" fill="none">
<path d="M154 160 L166 160"/><path d="M110 84 L110 96"/>
</g>
<g fill="#0f172a"><circle cx="160" cy="40" r="4"/><circle cx="240" cy="90" r="4"/><circle cx="160" cy="200" r="4"/><circle cx="80" cy="90" r="4"/></g>
<g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="160" y="28" text-anchor="middle" fill="#0f172a">A</text>
<text x="256" y="94" text-anchor="middle" fill="#0f172a">B</text>
<text x="160" y="222" text-anchor="middle" fill="#0f172a">C</text>
<text x="64" y="94" text-anchor="middle" fill="#0f172a">D</text>
</g>
</svg>
:::

## 📐 شبه المنحرف

**شبه المنحرف** رباعي له ضلعان متقابلان متوازيان على الأقلّ (**قاعدتاه**)، والآخران ساقاه، والمسافة
بين القاعدتين **ارتفاعه**. وهو **قائم الزاوية** إذا كانت إحدى ساقيه عمودية على القاعدتين،
و**متقايس الضلعين** إذا تقايست ساقاه دون أن تتوازيا.

_مثال_ — ABCD قائم الزاوية في A وD حيث AB = 5 و AD = 4 و DC = 8، وE من [AB] حيث AE = 3. المثلث ADE
قائم في A إذن DE² = 3² + 4² = 25 أي **DE = 5**. ولحساب BC نُسقط B عموديا على (DC) في H فنتحصّل على
مستطيل ABHD: إذن DH = AB = 5 و BH = AD = 4 و HC = 8 − 5 = 3، ومنه BC² = 3² + 4² = 25 أي **BC = 5**.
وفي EBCD: (EB) ∥ (DC) لكن EB = 2 ≠ DC = 8 فليس متوازي أضلاع، وساقاه ED = BC = 5 متقايستان:
إذن **EBCD شبه منحرف متقايس الضلعين**.

::: figure شبه منحرف قائم الزاوية في A وD: القاعدتان [AB] و[DC] متوازيتان، والساق [AD] عمودية عليهما فهي الارتفاع
<svg viewBox="0 0 320 205">
<path d="M60 60 L185 60 L260 160 L60 160 Z" fill="#0f6e56" opacity="0.12"/>
<path d="M60 60 L185 60 L260 160 L60 160 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M60 78 L78 78 L78 60" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M60 142 L78 142 L78 160" fill="none" stroke="#0f172a" stroke-width="2"/>
<g stroke="#94a3b8" stroke-width="1.5" fill="none">
<path d="M60 44 L185 44 M60 40 L60 48 M185 40 L185 48"/>
<path d="M60 76 L135 76 M60 72 L60 80 M135 72 L135 80"/>
<path d="M44 60 L44 160 M40 60 L48 60 M40 160 L48 160"/>
<path d="M60 176 L260 176 M60 172 L60 180 M260 172 L260 180"/>
</g>
<g fill="#0f172a"><circle cx="60" cy="60" r="4"/><circle cx="185" cy="60" r="4"/><circle cx="260" cy="160" r="4"/><circle cx="60" cy="160" r="4"/></g>
<circle cx="135" cy="60" r="4.5" fill="#0f6e56"/>
<g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="48" y="52" text-anchor="middle" fill="#0f172a">A</text>
<text x="196" y="52" text-anchor="middle" fill="#0f172a">B</text>
<text x="274" y="176" text-anchor="middle" fill="#0f172a">C</text>
<text x="48" y="178" text-anchor="middle" fill="#0f172a">D</text>
<text x="135" y="48" text-anchor="middle" fill="#0f6e56">E</text>
</g>
<g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" fill="#0f172a">
<text x="122" y="34" text-anchor="middle">5</text>
<text x="97" y="94" text-anchor="middle">3</text>
<text x="32" y="114" text-anchor="middle">4</text>
<text x="160" y="192" text-anchor="middle">8</text>
</g>
</svg>
:::

**المسقطان في شبه المنحرف متقايس الضلعين** — إذا أسقطنا رأسي القاعدة الصغيرة [AB] عموديا على القاعدة
الكبيرة [DC] في H وK، تحصّلنا على مستطيل ABKH فيكون HK = AB، **ويبقى الطرفان [DH] و[KC] متقايسين لأنّ
الساقين متقايستان**: أي أنّ الفرق DC − AB يتوزّع **مناصفة**، فـ DH = KC = (DC − AB)/2، ومنه نحسب
الارتفاع بفيثاغورس. _مثال_ — قاعدتاه 4 و 12 وساقاه 5: يبقى 12 − 4 = 8 فيتوزّع مناصفة أي DH = KC = 4،
ومنه الارتفاع h يحقّق h² = 5² − 4² = 9 أي **h = 3**.

::: figure شبه منحرف متقايس الضلعين: مسقطا A وB على (DC) يحصران HK = AB، ويبقى الطرفان DH = KC متقايسين
<svg viewBox="0 0 340 215">
<path d="M115 65 L225 65 L280 175 L60 175 Z" fill="#0f6e56" opacity="0.12"/>
<path d="M115 65 L225 65 L280 175 L60 175 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M115 65 L115 175 M225 65 L225 175" fill="none" stroke="#0f6e56" stroke-width="2" stroke-dasharray="5 4"/>
<path d="M115 163 L127 163 L127 175" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M225 163 L213 163 L213 175" fill="none" stroke="#0f172a" stroke-width="2"/>
<g stroke="#0f172a" stroke-width="2" stroke-linecap="round" fill="none">
<path d="M87 169 L87 181"/><path d="M253 169 L253 181"/>
<path d="M80 114 L91 119"/><path d="M84 121 L95 126"/>
<path d="M256 114 L245 119"/><path d="M260 121 L249 126"/>
</g>
<g fill="#0f172a"><circle cx="115" cy="65" r="4"/><circle cx="225" cy="65" r="4"/><circle cx="280" cy="175" r="4"/><circle cx="60" cy="175" r="4"/></g>
<g fill="#0f6e56"><circle cx="115" cy="175" r="4.5"/><circle cx="225" cy="175" r="4.5"/></g>
<g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="105" y="55" text-anchor="middle" fill="#0f172a">A</text>
<text x="235" y="55" text-anchor="middle" fill="#0f172a">B</text>
<text x="292" y="193" text-anchor="middle" fill="#0f172a">C</text>
<text x="48" y="193" text-anchor="middle" fill="#0f172a">D</text>
<text x="106" y="197" text-anchor="middle" fill="#0f6e56">H</text>
<text x="234" y="197" text-anchor="middle" fill="#0f6e56">K</text>
</g>
</svg>
:::

## 🧰 أدوات البرهان الثلاث

**1️⃣ المستقيم الرابط بين منتصفي ضلعي مثلث**

> 🛡️ **القاعدة**: في كلّ مثلث، المستقيم المارّ من **منتصفي ضلعين** يوازي حامل الضلع الثالث، وطول
> القطعة الرابطة بينهما يساوي **نصف** طول الضلع الثالث. **والعكس**: المستقيم المارّ من منتصف ضلع
> والموازي لحامل ضلع آخر يمرّ من **منتصف الضلع الثالث**.

_مثال_ — مثلث ABC حيث BC = 18، وI منتصف [AB] وJ منتصف [AC]: فـ IJ = 18/2 = **9** و(IJ) ∥ (BC).

**2️⃣ الموسط المتعلّق بالوتر في مثلث قائم الزاوية**

> 🛡️ **القاعدة**: ABC قائم الزاوية في A وI منتصف وتره [BC] ⟹ **IA = IB = IC = BC/2**. **والعكس**:
> I منتصف [BC] و IA = BC/2 ⟹ المثلث قائم الزاوية في A.

**ونستنتج**: A تنتمي إلى الدائرة التي **قطرها [BC]**، ومركز الدائرة المحيطة بمثلث قائم الزاوية هو
**منتصف وتره**. _مثال_ — AB = 8 و AC = 6 ⟹ BC = 10 ومنه IA = **5**.

::: figure I منتصف الوتر [BC]: الأطوال IA وIB وIC متقايسة، فالنقاط الثلاث على دائرة قطرها [BC]
<svg viewBox="0 0 300 245">
<circle cx="150" cy="125" r="100" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/>
<path d="M150 25 L70 185 L230 65 Z" fill="#0f6e56" opacity="0.10"/>
<path d="M150 25 L70 185 L230 65 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M150 25 L150 125" fill="none" stroke="#0f6e56" stroke-width="2.5"/>
<path d="M143.7 37.5 L156.2 43.8 L162.5 31.3" fill="none" stroke="#0f172a" stroke-width="2"/>
<g stroke="#0f172a" stroke-width="2" stroke-linecap="round" fill="none">
<path d="M144 75 L156 75"/><path d="M106 150 L114 160"/><path d="M186 90 L194 100"/>
</g>
<g fill="#0f172a"><circle cx="150" cy="25" r="4"/><circle cx="70" cy="185" r="4"/><circle cx="230" cy="65" r="4"/></g>
<circle cx="150" cy="125" r="4.5" fill="#0f6e56"/>
<g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="150" y="14" text-anchor="middle" fill="#0f172a">A</text>
<text x="56" y="201" text-anchor="middle" fill="#0f172a">B</text>
<text x="244" y="58" text-anchor="middle" fill="#0f172a">C</text>
<text x="136" y="140" text-anchor="middle" fill="#0f6e56">I</text>
</g>
</svg>
:::

**3️⃣ الموسط العمودي لقطعة**

> 🛡️ **القاعدة**: الموسط العمودي لقطعة [AB] هو المستقيم العمودي عليها في منتصفها. كلّ نقطة من
> الموسط العمودي متساوية البعد عن A وعن B، **والعكس صحيح**.

ومن العكس تأتي فائدته العمليّة: كلّ نقطة تبعد نفس البعد عن A وعن B تقع على هذا الموسط. _مثال_ —
[AB] طولها 10 وI منتصفها، وM من موسطها العمودي حيث MI = 12: فالمثلث MIA قائم في I ومنه
MA = MB = √(5² + 12²) = √169 = **13**.

::: figure الموسط العمودي للقطعة [AB] يمرّ من منتصفها I ويعامدها — وكلّ نقطة M منه تحقّق MA = MB
<svg viewBox="0 0 320 215">
<path d="M160 45 L160 195" fill="none" stroke="#0f6e56" stroke-width="2" stroke-dasharray="5 4"/>
<path d="M70 160 L250 160" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M160 70 L70 160 M160 70 L250 160" fill="none" stroke="#0f6e56" stroke-width="2"/>
<path d="M160 148 L172 148 L172 160" fill="none" stroke="#0f172a" stroke-width="2"/>
<g stroke="#0f172a" stroke-width="2" stroke-linecap="round" fill="none">
<path d="M115 154 L115 166"/><path d="M205 154 L205 166"/>
<path d="M110 110 L120 120"/><path d="M210 110 L200 120"/>
</g>
<g fill="#0f172a"><circle cx="70" cy="160" r="4"/><circle cx="250" cy="160" r="4"/></g>
<g fill="#0f6e56"><circle cx="160" cy="70" r="4.5"/><circle cx="160" cy="160" r="4.5"/></g>
<g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="58" y="176" text-anchor="middle" fill="#0f172a">A</text>
<text x="262" y="176" text-anchor="middle" fill="#0f172a">B</text>
<text x="160" y="58" text-anchor="middle" fill="#0f6e56">M</text>
<text x="147" y="184" text-anchor="middle" fill="#0f6e56">I</text>
</g>
</svg>
:::

## 🌟 رباعي المنتصفات

ليكن ABCD رباعيا محدّبا، وI وJ وK وL منتصفات [AB] و[BC] و[CD] و[DA] بالتتالي. في المثلث ABC:
(IJ) ∥ (AC) و IJ = AC/2؛ وفي المثلث ACD: (LK) ∥ (AC) و LK = AC/2. فللرباعي IJKL ضلعان متقابلان
متوازيان ومتقايسان، إذن **هو متوازي أضلاع مهما كان شكل ABCD**؛ وبنفس الطريقة IL = BD/2 و(IL) ∥ (BD).

> 🛡️ **المناقشة**: أضلاع IJKL هي أنصاف قطري ABCD واتّجاهاهما اتّجاها القطرين، ومنه: IJKL **معيّن**
> ⟺ AC = BD؛ و IJKL **مستطيل** ⟺ (AC) ⊥ (BD)؛ و IJKL **مربّع** ⟺ الشرطان معا. ومن هذا نستنتج أنّ
> منتصفات **مستطيل** تعطي **معيّنا**، ومنتصفات هذا المعيّن تعطي **مستطيلا**، وهكذا يتبادلان الدور.

::: figure رباعي المنتصفات IJKL (بالأخضر) متوازي أضلاع دائما: ضلعاه [IJ] و[LK] يوازيان القطر [AC] وطول كلّ منهما نصفه
<svg viewBox="0 0 320 250">
<path d="M80 40 L270 90 L230 215 L50 175 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M80 40 L230 215 M270 90 L50 175" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/>
<path d="M175 65 L250 152.5 L140 195 L65 107.5 Z" fill="#0f6e56" opacity="0.12"/>
<path d="M175 65 L250 152.5 L140 195 L65 107.5 Z" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round"/>
<g fill="#0f172a"><circle cx="80" cy="40" r="4"/><circle cx="270" cy="90" r="4"/><circle cx="230" cy="215" r="4"/><circle cx="50" cy="175" r="4"/></g>
<g fill="#0f6e56"><circle cx="175" cy="65" r="4.5"/><circle cx="250" cy="152.5" r="4.5"/><circle cx="140" cy="195" r="4.5"/><circle cx="65" cy="107.5" r="4.5"/></g>
<g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="70" y="30" text-anchor="middle" fill="#0f172a">A</text>
<text x="284" y="84" text-anchor="middle" fill="#0f172a">B</text>
<text x="242" y="234" text-anchor="middle" fill="#0f172a">C</text>
<text x="38" y="188" text-anchor="middle" fill="#0f172a">D</text>
<text x="180" y="54" text-anchor="middle" fill="#0f6e56">I</text>
<text x="266" y="152" text-anchor="middle" fill="#0f6e56">J</text>
<text x="140" y="214" text-anchor="middle" fill="#0f6e56">K</text>
<text x="50" y="102" text-anchor="middle" fill="#0f6e56">L</text>
</g>
</svg>
:::

## 📏 المساحات والمحيطات

| الشكل          | المساحة                               | المحيط                     |
| -------------- | ------------------------------------- | -------------------------- |
| المستطيل       | الطول × العرض                         | 2 × (الطول + العرض)        |
| المربّع        | الضلع × الضلع                         | 4 × الضلع                  |
| متوازي الأضلاع | القاعدة × الارتفاع المتعلّق بها       | 2 × (مجموع ضلعين متتاليين) |
| المعيّن        | القاعدة × الارتفاع = (جذاء القطرين)/2 | 4 × الضلع                  |
| شبه المنحرف    | (مجموع القاعدتين) × الارتفاع/2        | مجموع أضلاعه الأربعة       |

> 🛡️ **المحيط هو دائما مجموع أطوال الأضلاع**، والصيغ المختصرة أعلاه ليست إلاّ اختصارا له حين تتقايس
> الأضلاع. وفي المعيّن، إذا لم يُعطَ الضلع فاستخرجه بفيثاغورس من **نصفي** القطرين ثمّ اضربه في 4.
> _مثال_ — معيّن قطراه 6 و 8: مساحته (6 × 8)/2 = **24**، ونصفا قطريه 3 و 4 فضلعه √(3² + 4²) = 5
> ومحيطه 4 × 5 = **20**.

> ⚠️ **فخّان في المساحة**: في معيّن مركزه O تساوي المساحة AC × OB لأنّ OB = BD/2، أمّا OA × OB فهي
> **نصف** المساحة لأنّها تساوي (AC × BD)/4. ولمتوازي الأضلاع **ارتفاعان** حسب القاعدة المختارة
> والمساحة واحدة: إن كان H وL مسقطي A على (BC) و(CD) فإنّ AH × BC = AL × CD، ومنه **AH/AL = CD/BC**
> (الارتفاعان يتناسبان عكسيا مع قاعدتيهما).

## 🧭 في المعلّم المتعامد: نُثبت الطبيعة بالإحداثيات

في معلّم متعامد (O, I, J) يصبح البرهان **حسابا**: **منتصف** [AB] هو ((xA + xB)/2 ; (yA + yB)/2)؛
و**المسافة** AB = √((xB − xA)² + (yB − yA)²)؛ و**نظير A بالنسبة إلى نقطة K** هو (2xK − xA ; 2yK − yA)؛
و**مناظر A بالنسبة إلى محور الفواصل** هو (xA ; −yA) وبالنسبة إلى محور الترتيبات هو (−xA ; yA).
وتُقرأ الأوضاع مباشرة: لنقطتين **نفس الترتيبة** ⟹ المستقيم الرابط بينهما يوازي محور الفواصل ويعامد
محور الترتيبات (والعكس بتبديل الدورين).

> 🛡️ **القاعدة الذهبية في المعلّم**: ABCD متوازي أضلاع ⟺ [AC] و[BD] لهما **نفس المنتصف**؛ ثمّ نحسب
> الأطوال: قطران متقايسان ⟹ مستطيل، وضلعان متتاليان متقايسان ⟹ معيّن. _مثال_ — A(−1 ; 2) و B(3 ; 3)
> و C(4 ; 0): منتصف [AC] هو (1,5 ; 1)، فـ xD = 2 × 1,5 − 3 = 0 و yD = 2 × 1 − 3 = −1 أي **D(0 ; −1)**.

## ✍️ مساحات بدلالة x

في الوضعيات التي تتحرّك فيها نقطة، نعبّر عن كلّ مساحة **بدلالة x** ثمّ نحلّ معادلة أو عدم مساواة.
_مثال_ — ABCD مستطيل حيث AD = 4 و AB = 6، وP من [AD] وM من [AB] حيث AP = AM = x: الرباعي AMIP
**مربّع** ضلعه x فمساحته S = x²، والرباعي CQIN **مستطيل** بعداه 6 − x و 4 − x فمساحته
S' = (6 − x)(4 − x) = 24 − 10x + x². فتعطي **المعادلة** S = S' العلاقة 10x = 24 أي **x = 2,4**؛
وتعطي **عدم المساواة** S' > S الشرط 24 − 10x > 0 أي x < 2,4، ومع 0 < x ≤ 4 تكون مجموعة الحلول هي
المجال **]0 ; 2,4[**.

::: figure المربّع AMIP (بالأخضر أعلى اليسار) والمستطيل CQIN (بالأخضر أسفل اليمين): ضلع المربّع x، وبعدا المستطيل 6 − x و 4 − x
<svg viewBox="0 0 340 240">
<path d="M60 50 L120 50 L120 110 L60 110 Z" fill="#0f6e56" opacity="0.22"/>
<path d="M120 110 L300 110 L300 210 L120 210 Z" fill="#0f6e56" opacity="0.22"/>
<path d="M120 50 L300 50 L300 110 L120 110 Z" fill="#94a3b8" opacity="0.15"/>
<path d="M60 110 L120 110 L120 210 L60 210 Z" fill="#94a3b8" opacity="0.15"/>
<path d="M60 50 L300 50 L300 210 L60 210 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M60 110 L300 110 M120 50 L120 210" fill="none" stroke="#0f172a" stroke-width="1.8"/>
<path d="M42 50 L42 110 M38 50 L46 50 M38 110 L46 110" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
<g fill="#0f172a"><circle cx="60" cy="50" r="4"/><circle cx="300" cy="50" r="4"/><circle cx="300" cy="210" r="4"/><circle cx="60" cy="210" r="4"/></g>
<g fill="#0f6e56"><circle cx="120" cy="50" r="4.5"/><circle cx="60" cy="110" r="4.5"/><circle cx="120" cy="110" r="4.5"/><circle cx="300" cy="110" r="4.5"/><circle cx="120" cy="210" r="4.5"/></g>
<g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="60" y="40" text-anchor="middle" fill="#0f172a">A</text>
<text x="310" y="40" text-anchor="middle" fill="#0f172a">B</text>
<text x="312" y="228" text-anchor="middle" fill="#0f172a">C</text>
<text x="50" y="228" text-anchor="middle" fill="#0f172a">D</text>
<text x="120" y="40" text-anchor="middle" fill="#0f6e56">M</text>
<text x="46" y="114" text-anchor="middle" fill="#0f6e56">P</text>
<text x="133" y="103" text-anchor="middle" fill="#0f6e56">I</text>
<text x="313" y="114" text-anchor="middle" fill="#0f6e56">N</text>
<text x="120" y="228" text-anchor="middle" fill="#0f6e56">Q</text>
<text x="30" y="86" text-anchor="middle" fill="#0f172a">x</text>
</g>
</svg>
:::

> 🏆 مفتاح الفصل: **لا تصف الشكل، برهن عليه** — ابحث دائما عن منتصف، أو عن قطرين، أو عن مثلث قائم الزاوية مخفيّ.
