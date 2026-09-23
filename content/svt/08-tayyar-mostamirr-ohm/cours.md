# ⚔️ التيّار الكهربائي المتغيّر والتيّار المتناوب الجيبي — سرّ العلامة ~

> 💡 «وراء كلّ منشب في بيتك توتّر يغيّر علامته مئة مرّة في الثانية. تعلَّم قراءته، وستفهم ما تعنيه العلامة 220 V ~ 50 Hz على أجهزتك.»

## 🏰 التيّار المتغيّر — حين يسري التيّار في الاتّجاهين

تعرف منذ السنة الثامنة أنّ العمود الجافّ يدفع التيّار في اتّجاه واحد: من قطبه الموجب نحو قطبه السالب خارج المولّد.
لكنّ بعض أجهزة التغذية في المخبر تحمل العلامة ~ بدل العلامة =. فهل يمكن لمولّد أن يدفع التيّار في الاتّجاهين؟

::: definition
**التيّار الكهربائي المتغيّر** (courant variable) هو تيّار لا يبقى ثابتًا مع الزمن في اتّجاهه، أو في شدّته، أو فيهما معًا.
**التيّار المستمرّ** (courant continu) هو تيّار اتّجاهه وحيد وشدّته ثابتة مع الزمن، مثل تيّار العمود الجافّ أو البطاريّة. وكلّ تيّار غير مستمرّ هو تيّار متغيّر.
:::

نركّب مولّدًا وقاطعًا ومعدّلة (لحماية الصمّامين) مع صمّامين مشعّين موصولين على التوازي بين النقطتين A و B، كلّ واحد في اتّجاه معاكس للآخر.

::: figure صمّامان مشعّان متعاكسان بين A و B: D1 لا يمرّر التيّار إلّا من A إلى B، و D2 إلّا من B إلى A
<svg viewBox="0 0 340 240">
<path d="M60 90 L60 40 L125 40" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M155 40 L175 40" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M215 40 L270 40" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M60 150 L60 200 L270 200" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="60" cy="120" r="30" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<text x="60" y="128" text-anchor="middle" fill="#0f172a" font-size="26" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">~</text>
<circle cx="125" cy="40" r="3" fill="#0f172a"/><circle cx="155" cy="40" r="3" fill="#0f172a"/>
<line x1="125" y1="40" x2="152" y2="26" stroke="#0f172a" stroke-width="2"/>
<text x="140" y="20" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">K</text>
<rect x="175" y="31" width="40" height="18" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<path d="M270 40 L240 40 L240 102" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M240 138 L240 200" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M270 40 L300 40 L300 102" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M300 138 L300 200" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M270 200 L300 200" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M240 200 L270 200" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="240" y1="102" x2="240" y2="110" stroke="#0f172a" stroke-width="2"/>
<line x1="240" y1="130" x2="240" y2="138" stroke="#0f172a" stroke-width="2"/>
<polygon points="228,110 252,110 240,130" fill="#dc2626" fill-opacity="0.35" stroke="#dc2626" stroke-width="2"/>
<line x1="228" y1="130" x2="252" y2="130" stroke="#dc2626" stroke-width="2.5"/>
<line x1="255" y1="114" x2="265" y2="106" stroke="#dc2626" stroke-width="1.6"/>
<polygon points="265,106 262.7,111.1 259.5,107.2" fill="#dc2626"/>
<line x1="255" y1="123" x2="265" y2="115" stroke="#dc2626" stroke-width="1.6"/>
<polygon points="265,115 262.7,120.1 259.5,116.2" fill="#dc2626"/>
<line x1="300" y1="102" x2="300" y2="110" stroke="#0f172a" stroke-width="2"/>
<line x1="300" y1="130" x2="300" y2="138" stroke="#0f172a" stroke-width="2"/>
<polygon points="288,130 312,130 300,110" fill="#16a34a" fill-opacity="0.35" stroke="#16a34a" stroke-width="2"/>
<line x1="288" y1="110" x2="312" y2="110" stroke="#16a34a" stroke-width="2.5"/>
<line x1="315" y1="114" x2="325" y2="106" stroke="#16a34a" stroke-width="1.6"/>
<polygon points="325,106 322.7,111.1 319.5,107.2" fill="#16a34a"/>
<line x1="315" y1="123" x2="325" y2="115" stroke="#16a34a" stroke-width="1.6"/>
<polygon points="325,115 322.7,120.1 319.5,116.2" fill="#16a34a"/>
<circle cx="270" cy="40" r="4" fill="#0f172a"/><circle cx="270" cy="200" r="4" fill="#0f172a"/>
<text x="270" y="28" text-anchor="middle" fill="#0f172a" font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">A</text>
<text x="270" y="222" text-anchor="middle" fill="#0f172a" font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">B</text>
<text x="212" y="125" text-anchor="middle" fill="#dc2626" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">D1</text>
<text x="326" y="160" text-anchor="middle" fill="#16a34a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">D2</text>
</svg>
:::

الصمّام D1 في الشكل هو الذي يضيء حين يسري التيّار من A نحو B، والصمّام D2 هو الذي يضيء حين يسري من B نحو A.

::: exemple عمود جافّ ثمّ جهاز تغذية يحمل العلامة ~

1. مع العمود الجافّ يضيء صمّام واحد فقط — لأنّ الصمّام المشعّ لا يمرّر التيّار إلّا في اتّجاه واحد، والعمود يدفع التيّار في اتّجاه واحد.
2. نعوّض العمود بجهاز التغذية ~ ونغلق القاطع: يضيء الصمّامان معًا — لأنّ كلّ صمّام يجد في لحظات ما تيّارًا يسري في اتّجاهه.
3. إذن التيّار يسري في هذه الدارة تارةً من A إلى B وتارةً من B إلى A — لأنّ D1 و D2 لا يضيئان في الاتّجاه نفسه.

:::

> ⚠️ **الخطأ الشائع**: الظنّ أنّ التيّار لا يكون متغيّرًا إلّا إذا غيّر اتّجاهه.
> مصباح يقوى توهّجه ثمّ يضعف بلا توقّف، وصمّام مشعّ موصول معه على التسلسل يبقى مضيئًا: الاتّجاه لم يتغيّر، لكنّ الشدّة تغيّرت.
> هذا التيّار متغيّر: يكفي أن يتغيّر **الاتّجاه أو الشدّة**، ولا يشترط تغيّرهما معًا.

::: propriete
للحكم على تيّار نطرح سؤالين: هل اتّجاهه ثابت؟ هل شدّته ثابتة؟ إذا كان الجواب «نعم» مرّتين فالتيّار مستمرّ، وإلّا فهو متغيّر.
حالة حدّية: في تجربة مولّد TBF يرفّ صمّام مشعّ موصول مع المصباح، ولا يضيء إلّا مرّة من كلّ مرّتين يتوهّج فيهما المصباح: هنا تتغيّر الشدّة **والاتّجاه** معًا.
:::

::: verifie
صمّام مشعّ موصول على التسلسل مع مصباح يبقى مضيئًا طوال التجربة، ويبقى توهّج المصباح هو نفسه دون أيّ تغيّر. هل التيّار مستمرّ أم متغيّر؟

---

التيّار مستمرّ. الصمّام المضيء دائمًا يدلّ على أنّ الاتّجاه وحيد، والتوهّج الذي لا يتغيّر يدلّ على أنّ الشدّة ثابتة: الشرطان متحقّقان معًا.
:::

::: retenir
تيّار متغيّر = اتّجاهه أو شدّته (أو كلاهما) غير ثابت مع الزمن؛ تيّار مستمرّ = اتّجاه وحيد وشدّة ثابتة.
:::

## ⚡ التوتّر المتغيّر u — البقعة الضوئيّة التي لا تهدأ

التيّار لا يسري في دارة إلّا إذا حفظ المولّد توتّرًا بين قطبيه. فإذا كان التيّار متغيّرًا، ماذا يحدث للتوتّر؟
التوتّر يتغيّر بسرعة لا تتابعها العين على فولتمتر، لذلك نستعمل **مشواف الذبذبات** (oscilloscope) بعد إيقاف **المسح** (balayage)، أي الحركة الأفقيّة للبقعة الضوئيّة على الشاشة.

::: definition
**التوتّر المتغيّر** (tension variable) هو توتّر لا تبقى قيمته الجبريّة، أي قيمته المطلقة وعلامته، ثابتة مع الزمن. والتوتّر الثابت يُسمّى **توتّرًا مستمرًّا**.
نرمز إلى المقدار المتغيّر بحرف لاتينيّ صغير: التوتّر المتغيّر u والشدّة المتغيّرة i، عوضًا عن U و I.
:::

::: figure المسح موقَف: (1) بقعة انزاحت ثمّ استقرّت؛ (2) بقعة تصعد وتنزل بلا انقطاع حول المركز فترسم قطعة عموديّة
<svg viewBox="0 0 340 200">
<rect x="20" y="30" width="120" height="120" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<line x1="40" y1="30" x2="40" y2="150" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="60" y1="30" x2="60" y2="150" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="80" y1="30" x2="80" y2="150" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="100" y1="30" x2="100" y2="150" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="120" y1="30" x2="120" y2="150" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="20" y1="50" x2="140" y2="50" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="20" y1="70" x2="140" y2="70" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="20" y1="90" x2="140" y2="90" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="20" y1="110" x2="140" y2="110" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="20" y1="130" x2="140" y2="130" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="20" y1="90" x2="140" y2="90" stroke="#94a3b8" stroke-width="1.6"/>
<line x1="80" y1="30" x2="80" y2="150" stroke="#94a3b8" stroke-width="1.6"/>
<circle cx="80" cy="50" r="6" fill="#0f6e56"/>
<circle cx="80" cy="90" r="4" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-dasharray="3 2"/>
<line x1="80" y1="84" x2="80" y2="60" stroke="#0f172a" stroke-width="1.4" stroke-dasharray="4 3"/>
<polygon points="80,58 83,64 77,64" fill="#0f172a"/>
<rect x="200" y="30" width="120" height="120" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<line x1="220" y1="30" x2="220" y2="150" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="240" y1="30" x2="240" y2="150" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="260" y1="30" x2="260" y2="150" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="280" y1="30" x2="280" y2="150" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="300" y1="30" x2="300" y2="150" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="200" y1="50" x2="320" y2="50" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="200" y1="70" x2="320" y2="70" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="200" y1="90" x2="320" y2="90" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="200" y1="110" x2="320" y2="110" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="200" y1="130" x2="320" y2="130" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="200" y1="90" x2="320" y2="90" stroke="#94a3b8" stroke-width="1.6"/>
<line x1="260" y1="30" x2="260" y2="150" stroke="#94a3b8" stroke-width="1.6"/>
<line x1="260" y1="50" x2="260" y2="130" stroke="#0f6e56" stroke-width="6" stroke-linecap="round"/>
<line x1="284" y1="80" x2="284" y2="52" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="284,50 287,56 281,56" fill="#0f172a"/>
<line x1="284" y1="100" x2="284" y2="128" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="284,130 281,124 287,124" fill="#0f172a"/>
<text x="80" y="178" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">(1)</text>
<text x="260" y="178" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">(2)</text>
</svg>
:::

في الشاشة (1) تغيّرت قيمة التوتّر مرّة واحدة ثمّ بقيت ثابتة، وفي الشاشة (2) تتغيّر قيمته وعلامته في كلّ لحظة.

::: exemple قراءة الشاشتين

1. الشاشة (1): البقعة صعدت تدريجتين ثمّ ثبتت — لأنّ التوتّر المطبَّق موجب وقيمته لا تتغيّر، فهو توتّر مستمرّ (عمود أو بطاريّة).
2. الشاشة (2): البقعة تتحرّك عموديًّا في الاتّجاهين حول المركز — لأنّ قيمة التوتّر تتغيّر وعلامته تنقلب مع الزمن.
3. إذن المولّد الموصول بالشاشة (2) مولّد توتّر متغيّر — لأنّ البقعة لا تستقرّ أبدًا، سواء كانت الدارة مفتوحة أو مغلقة.

:::

> ⚠️ **الخطأ الشائع**: «البقعة ابتعدت عن المركز، إذن التوتّر متغيّر».
> هذا خطأ: في الشاشة (1) ابتعدت البقعة ثمّ ثبتت، والتوتّر مستمرّ. ما يكشف التوتّر المتغيّر هو **حركة لا تتوقّف**، لا الابتعاد عن المركز.

::: propriete
لا يغذّي مولّد دارة مغلقة بتيّار متغيّر إلّا إذا حفظ بين قطبيه توتّرًا متغيّرًا: كلّ تيّار متغيّر ناتج عن توتّر متغيّر.
حالة حدّية: البقعة تتحرّك في الشاشة (2) حتّى والدارة مفتوحة، لأنّ التوتّر موجود بين قطبي المولّد ولو لم يسرِ أيّ تيّار.
:::

::: verifie
بأيّ رمز تكتب التوتّر بين قطبي مولّد TBF؟ وبين قطبي بطاريّة؟

---

بين قطبي مولّد TBF نكتب u بحرف صغير، لأنّ توتّره متغيّر. وبين قطبي البطاريّة نكتب U بحرف كبير، لأنّ توتّرها مستمرّ.
:::

::: retenir
توتّر متغيّر u = قيمة جبريّة غير ثابتة؛ الحرف الصغير (u و i) يدلّ على مقدار متغيّر.
:::

## 🔄 التوتّر المتناوب والتيّار المتناوب — القطبان يتبادلان الأدوار

على الأمبيرمترات والفولتمترات في المخبر زرّ ينتقل بين الوضعين = و ~، ولم نستعمل الوضع ~ من قبل.
نصل فولتمترًا رقميًّا بقطبي مولّد TBF: يعرض بالتناوب قيمًا موجبة ثمّ قيمًا سالبة. وفي دارة الصمّامين يضيء D1 ثمّ D2 بالتناوب. ماذا يحدث داخل المولّد؟

::: definition
**التوتّر المتناوب** (tension alternative) هو توتّر متغيّر تأخذ قيمته الجبريّة بالتناوب، وبلا انقطاع، قيمًا موجبة ثمّ قيمًا سالبة.
**التيّار المتناوب** (courant alternatif) هو التيّار الذي يولّده توتّر متناوب في دارة مغلقة: يسري في اتّجاه، ثمّ في الاتّجاه المعاكس، وهكذا دواليك.
:::

::: figure (1) مستمرّ: ثابت دائمًا؛ (2) متغيّر لكنّه لا يصير سالبًا أبدًا؛ (3) متناوب: موجب ثمّ سالب بالتناوب
<svg viewBox="0 0 340 300">
<line x1="40" y1="60" x2="320" y2="60" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="326,60 319,63.5 319,56.5" fill="#0f172a"/>
<line x1="40" y1="98" x2="40" y2="18" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="40,14 43.5,21 36.5,21" fill="#0f172a"/>
<text x="318" y="76" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">t</text>
<text x="28" y="26" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">u</text>
<text x="18" y="65" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">(1)</text>
<path d="M40 35 L310 35" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="40" y1="160" x2="320" y2="160" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="326,160 319,163.5 319,156.5" fill="#0f172a"/>
<line x1="40" y1="198" x2="40" y2="118" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="40,114 43.5,121 36.5,121" fill="#0f172a"/>
<text x="318" y="176" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">t</text>
<text x="28" y="126" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">u</text>
<text x="18" y="165" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">(2)</text>
<path d="M40 160 L40 135 L75 135 L75 160 L107.5 160 L107.5 135 L142.5 135 L142.5 160 L175 160 L175 135 L210 135 L210 160 L242.5 160 L242.5 135 L277.5 135 L277.5 160 L310 160" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="40" y1="255" x2="320" y2="255" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="326,255 319,258.5 319,251.5" fill="#0f172a"/>
<line x1="40" y1="293" x2="40" y2="213" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="40,209 43.5,216 36.5,216" fill="#0f172a"/>
<text x="318" y="271" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">t</text>
<text x="28" y="221" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">u</text>
<text x="18" y="260" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">(3)</text>
<path d="M40 255 L62.5 230 L85 255 L107.5 280 L130 255 L152.5 230 L175 255 L197.5 280 L220 255 L242.5 230 L265 255 L287.5 280 L310 255" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
</svg>
:::

المنحنى (3) وحده يعبر المحور الأفقي نحو الأسفل: هو وحده يأخذ قيمًا سالبة، ولذلك هو وحده متناوب.

::: exemple قراءة الفولتمتر والصمّامين معًا

1. حين يعرض الفولتمتر قيمة موجبة يضيء D1 — لأنّ A يلعب دور القطب الموجب، فيسري التيّار خارج المولّد من A إلى B.
2. حين يعرض قيمة سالبة يضيء D2 — لأنّ B صار القطب الموجب، فيسري التيّار من B إلى A.
3. إذن انقلاب اتّجاه التيّار ناتج عن تبادل القطبين A و B للأدوار — لأنّ علامة التوتّر هي التي تحدّد أيّ القطبين موجب.

:::

> ⚠️ **الخطأ الشائع**: «كلّ توتّر متغيّر هو توتّر متناوب».
> المنحنى (2) يتغيّر فعلًا، لكنّه لا ينزل تحت الصفر أبدًا: التيّار الذي يولّده لا ينقلب اتّجاهه. هو متغيّر **غير متناوب**.

::: propriete

| نوع التوتّر       | قيمته الجبريّة           | اتّجاه التيّار |
| ----------------- | ------------------------ | -------------- |
| مستمرّ            | ثابتة                    | وحيد           |
| متغيّر غير متناوب | تتغيّر وتحفظ علامتها     | وحيد           |
| متناوب            | موجبة ثمّ سالبة بالتناوب | ينقلب بالتناوب |

كلّ توتّر متناوب متغيّر، والعكس غير صحيح. حالة حدّية: في اللحظة التي يمرّ فيها التوتّر بالصفر لا يضيء أيّ صمّام.
:::

::: verifie
مولّد يحفظ بين قطبيه توتّرًا ثابتًا قيمته −6 V. هل توتّره متناوب؟

---

لا، هو توتّر مستمرّ. علامته سالبة، لكنّها لا تتغيّر أبدًا وقيمته ثابتة؛ والتوتّر المتناوب هو الذي تتناوب علامته بين موجبة وسالبة.
:::

::: retenir
متناوب = موجب ثمّ سالب بالتناوب، فينقلب اتّجاه التيّار؛ كلّ متناوب متغيّر، وليس كلّ متغيّر متناوبًا.
:::

## 〰️ التوتّر المتناوب الجيبي — منحنى من جيوب متطابقة

نضبط مولّد TBF على تغيّر بطيء جدًّا، ونقرأ الفولتمتر الرقمي كلّ 10 s بواسطة ميقت.
ما شكل المنحنى الذي نحصل عليه إذا مثّلنا القيم المقيسة بدلالة الزمن؟

| t (s) | 0   | 10  | 20  | 30  | 40  | 50  | 60   | 70  | 80  |
| ----- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
| u (V) | 0   | 6   | 8,5 | 6   | 0   | −6  | −8,5 | −6  | 0   |

::: definition
**التوتّر المتناوب الجيبي** (tension alternative sinusoïdale) هو توتّر متناوب يتطوّر مع الزمن في شكل منحنى جيبي، أي جيوب متتالية ومتطابقة. والتيّار الذي يولّده في دارة مغلقة **تيّار متناوب جيبي**.
:::

::: figure نقاط الجدول تقع على منحنى مكوّن من جيوب متتالية ومتطابقة
<svg viewBox="0 0 340 230">
<line x1="50" y1="115" x2="335" y2="115" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="341,115 334,118.5 334,111.5" fill="#0f172a"/>
<line x1="50" y1="205" x2="50" y2="22" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="50,16 53.5,23 46.5,23" fill="#0f172a"/>
<line x1="46" y1="30.1" x2="54" y2="30.1" stroke="#0f172a" stroke-width="1.5"/>
<line x1="54" y1="30.1" x2="306" y2="30.1" stroke="#94a3b8" stroke-width="0.8" stroke-dasharray="3 3"/>
<text x="42" y="34.1" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">8,5</text>
<line x1="46" y1="55" x2="54" y2="55" stroke="#0f172a" stroke-width="1.5"/>
<line x1="54" y1="55" x2="306" y2="55" stroke="#94a3b8" stroke-width="0.8" stroke-dasharray="3 3"/>
<text x="42" y="59" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">6</text>
<line x1="46" y1="175" x2="54" y2="175" stroke="#0f172a" stroke-width="1.5"/>
<line x1="54" y1="175" x2="306" y2="175" stroke="#94a3b8" stroke-width="0.8" stroke-dasharray="3 3"/>
<text x="42" y="179" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">−6</text>
<line x1="46" y1="199.9" x2="54" y2="199.9" stroke="#0f172a" stroke-width="1.5"/>
<line x1="54" y1="199.9" x2="306" y2="199.9" stroke="#94a3b8" stroke-width="0.8" stroke-dasharray="3 3"/>
<text x="42" y="203.9" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">−8,5</text>
<line x1="114" y1="111" x2="114" y2="119" stroke="#0f172a" stroke-width="1.5"/>
<text x="126" y="135" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">40</text>
<line x1="178" y1="111" x2="178" y2="119" stroke="#0f172a" stroke-width="1.5"/>
<text x="190" y="135" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">80</text>
<line x1="242" y1="111" x2="242" y2="119" stroke="#0f172a" stroke-width="1.5"/>
<text x="254" y="135" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">120</text>
<line x1="306" y1="111" x2="306" y2="119" stroke="#0f172a" stroke-width="1.5"/>
<text x="318" y="135" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">160</text>
<path d="M50 115 L51.3 109.7 L52.6 104.4 L53.8 99.1 L55.1 93.9 L56.4 88.8 L57.7 83.8 L59 78.9 L60.2 74.1 L61.5 69.5 L62.8 65.1 L64.1 60.9 L65.4 56.9 L66.6 53.1 L67.9 49.6 L69.2 46.4 L70.5 43.4 L71.8 40.6 L73 38.2 L74.3 36.1 L75.6 34.3 L76.9 32.8 L78.2 31.7 L79.4 30.8 L80.7 30.3 L82 30.1 L83.3 30.3 L84.6 30.8 L85.8 31.7 L87.1 32.8 L88.4 34.3 L89.7 36.1 L91 38.2 L92.2 40.6 L93.5 43.4 L94.8 46.4 L96.1 49.6 L97.4 53.1 L98.6 56.9 L99.9 60.9 L101.2 65.1 L102.5 69.5 L103.8 74.1 L105 78.9 L106.3 83.8 L107.6 88.8 L108.9 93.9 L110.2 99.1 L111.4 104.4 L112.7 109.7 L114 115 L115.3 120.3 L116.6 125.6 L117.8 130.9 L119.1 136.1 L120.4 141.2 L121.7 146.2 L123 151.1 L124.2 155.9 L125.5 160.5 L126.8 164.9 L128.1 169.1 L129.4 173.1 L130.6 176.9 L131.9 180.4 L133.2 183.6 L134.5 186.6 L135.8 189.4 L137 191.8 L138.3 193.9 L139.6 195.7 L140.9 197.2 L142.2 198.3 L143.4 199.2 L144.7 199.7 L146 199.9 L147.3 199.7 L148.6 199.2 L149.8 198.3 L151.1 197.2 L152.4 195.7 L153.7 193.9 L155 191.8 L156.2 189.4 L157.5 186.6 L158.8 183.6 L160.1 180.4 L161.4 176.9 L162.6 173.1 L163.9 169.1 L165.2 164.9 L166.5 160.5 L167.8 155.9 L169 151.1 L170.3 146.2 L171.6 141.2 L172.9 136.1 L174.2 130.9 L175.4 125.6 L176.7 120.3 L178 115 L179.3 109.7 L180.6 104.4 L181.8 99.1 L183.1 93.9 L184.4 88.8 L185.7 83.8 L187 78.9 L188.2 74.1 L189.5 69.5 L190.8 65.1 L192.1 60.9 L193.4 56.9 L194.6 53.1 L195.9 49.6 L197.2 46.4 L198.5 43.4 L199.8 40.6 L201 38.2 L202.3 36.1 L203.6 34.3 L204.9 32.8 L206.2 31.7 L207.4 30.8 L208.7 30.3 L210 30.1 L211.3 30.3 L212.6 30.8 L213.8 31.7 L215.1 32.8 L216.4 34.3 L217.7 36.1 L219 38.2 L220.2 40.6 L221.5 43.4 L222.8 46.4 L224.1 49.6 L225.4 53.1 L226.6 56.9 L227.9 60.9 L229.2 65.1 L230.5 69.5 L231.8 74.1 L233 78.9 L234.3 83.8 L235.6 88.8 L236.9 93.9 L238.2 99.1 L239.4 104.4 L240.7 109.7 L242 115 L243.3 120.3 L244.6 125.6 L245.8 130.9 L247.1 136.1 L248.4 141.2 L249.7 146.2 L251 151.1 L252.2 155.9 L253.5 160.5 L254.8 164.9 L256.1 169.1 L257.4 173.1 L258.6 176.9 L259.9 180.4 L261.2 183.6 L262.5 186.6 L263.8 189.4 L265 191.8 L266.3 193.9 L267.6 195.7 L268.9 197.2 L270.2 198.3 L271.4 199.2 L272.7 199.7 L274 199.9 L275.3 199.7 L276.6 199.2 L277.8 198.3 L279.1 197.2 L280.4 195.7 L281.7 193.9 L283 191.8 L284.2 189.4 L285.5 186.6 L286.8 183.6 L288.1 180.4 L289.4 176.9 L290.6 173.1 L291.9 169.1 L293.2 164.9 L294.5 160.5 L295.8 155.9 L297 151.1 L298.3 146.2 L299.6 141.2 L300.9 136.1 L302.2 130.9 L303.4 125.6 L304.7 120.3 L306 115" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="50" cy="115" r="3.5" fill="#0f172a"/>
<circle cx="66" cy="55" r="3.5" fill="#0f172a"/>
<circle cx="82" cy="30.1" r="3.5" fill="#0f172a"/>
<circle cx="98" cy="55" r="3.5" fill="#0f172a"/>
<circle cx="114" cy="115" r="3.5" fill="#0f172a"/>
<circle cx="130" cy="175" r="3.5" fill="#0f172a"/>
<circle cx="146" cy="199.9" r="3.5" fill="#0f172a"/>
<circle cx="162" cy="175" r="3.5" fill="#0f172a"/>
<circle cx="178" cy="115" r="3.5" fill="#0f172a"/>
<circle cx="194" cy="55" r="3.5" fill="#0f172a"/>
<circle cx="210" cy="30.1" r="3.5" fill="#0f172a"/>
<circle cx="226" cy="55" r="3.5" fill="#0f172a"/>
<circle cx="242" cy="115" r="3.5" fill="#0f172a"/>
<circle cx="258" cy="175" r="3.5" fill="#0f172a"/>
<circle cx="274" cy="199.9" r="3.5" fill="#0f172a"/>
<circle cx="290" cy="175" r="3.5" fill="#0f172a"/>
<circle cx="306" cy="115" r="3.5" fill="#0f172a"/>
<text x="318" y="105" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">t (s)</text>
<text x="72" y="20" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">u (V)</text>
</svg>
:::

كلّ نقطة سوداء في الشكل هي خانة من الجدول، والمنحنى الأخضر هو التوتّر u بين قياسين متتاليين.

::: exemple من الجدول إلى المنحنى

1. نرسم محورًا أفقيًّا للزمن t ومحورًا عموديًّا للتوتّر u — لأنّنا نمثّل u بدلالة t.
2. نضع نقاط الجدول، ثمّ نواصل: القيم نفسها تعود بالترتيب نفسه بعد t = 80 s — لأنّ المولّد يعيد التطوّر نفسه.
3. نصل النقاط بخطّ منحنٍ أملس، لا بقطع مستقيمة — لأنّ التوتّر يتغيّر تدريجيًّا بين قياسين.
4. نلاحظ أقواسًا متطابقة، واحدة فوق المحور ثمّ واحدة تحته — لأنّ القيم الموجبة والسالبة متناظرة.

:::

> ⚠️ **الخطأ الشائع**: «كلّ توتّر متناوب هو توتّر جيبي».
> توتّر دينامو الدرّاجة متناوب، لكنّ قممه مدبّبة وغير متناظرة، والمنحنى (3) في الفقرة السابقة مثلّثات: كلاهما متناوب **غير جيبي**. لا نقول «جيبي» إلّا إذا كان شكل المنحنى جيوبًا.

::: propriete
جيبي ⟸ متناوب ⟸ متغيّر: كلّ توتّر جيبي متناوب، وكلّ متناوب متغيّر، والعكس في الحالتين غير صحيح.
حالة مهمّة: التوتّر الكهربائي المنزلي مثال للتوتّر المتناوب الجيبي.
:::

::: verifie
رسم تذبذبي يتناوب فيه التوتّر بين +4 V و −4 V، لكنّه يقفز من قيمة إلى أخرى ويبقى ثابتًا بينهما (شكل مربّعات). كيف تصفه؟

---

متغيّر ومتناوب لأنّ علامته تتناوب بين موجبة وسالبة، لكنّه غير جيبي لأنّ منحناه مربّعات لا جيوب.
:::

::: retenir
جيبي = متناوب منحناه جيوب متتالية ومتطابقة؛ والتوتّر المنزلي جيبي.
:::

## ⏱️ الدورة T والتردّد N — كم مرّة يتكرّر الشكل؟

في جدول الفقرة السابقة تعود القيم 0 ثمّ 6 ثمّ 8,5… بالترتيب نفسه كلّ 80 s.
التوتّر إذن يعيد نفسه بانتظام: ما مدّة الجزء الذي يتكرّر؟ وكم مرّة يتكرّر في الثانية الواحدة؟

::: definition
**الدورة** (période) T هي أصغر مدّة يستعيد بعدها التوتّر القيمة نفسها مع التطوّر في الاتّجاه نفسه؛ وحدتها الثانية (s).
**التردّد** (fréquence) N هو عدد الدورات المتطابقة المتتالية في الثانية الواحدة؛ وحدته الهرتز (Hz).
$$ N = 1/T $$
:::

::: figure الدورة T هي نفسها مهما كانت نقطة البداية: من صفر صاعد إلى الصفر الصاعد الموالي، أو من قمّة إلى القمّة الموالية
<svg viewBox="0 0 340 220">
<line x1="30" y1="105" x2="325" y2="105" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="331,105 324,108.5 324,101.5" fill="#0f172a"/>
<line x1="30" y1="180" x2="30" y2="30" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="30,24 33.5,31 26.5,31" fill="#0f172a"/>
<path d="M30 105 L31.4 100.5 L32.9 96 L34.3 91.5 L35.8 87.2 L37.2 82.9 L38.6 78.8 L40.1 74.8 L41.5 71 L43 67.3 L44.4 63.9 L45.8 60.7 L47.3 57.8 L48.7 55.2 L50.2 52.8 L51.6 50.7 L53 48.9 L54.5 47.5 L55.9 46.4 L57.4 45.6 L58.8 45.1 L60.2 45 L61.7 45.2 L63.1 45.8 L64.6 46.7 L66 47.9 L67.4 49.5 L68.9 51.4 L70.3 53.5 L71.8 56 L73.2 58.8 L74.6 61.8 L76.1 65 L77.5 68.5 L79 72.2 L80.4 76.1 L81.8 80.1 L83.3 84.3 L84.7 88.6 L86.2 93 L87.6 97.5 L89 102 L90.5 106.5 L91.9 111 L93.4 115.5 L94.8 119.9 L96.2 124.3 L97.7 128.5 L99.1 132.6 L100.6 136.5 L102 140.3 L103.4 143.8 L104.9 147.2 L106.3 150.3 L107.8 153.1 L109.2 155.7 L110.6 157.9 L112.1 159.9 L113.5 161.6 L115 162.9 L116.4 163.9 L117.8 164.6 L119.3 165 L120.7 165 L122.2 164.6 L123.6 163.9 L125 162.9 L126.5 161.6 L127.9 159.9 L129.4 157.9 L130.8 155.7 L132.2 153.1 L133.7 150.3 L135.1 147.2 L136.6 143.8 L138 140.3 L139.4 136.5 L140.9 132.6 L142.3 128.5 L143.8 124.3 L145.2 119.9 L146.6 115.5 L148.1 111 L149.5 106.5 L151 102 L152.4 97.5 L153.8 93 L155.3 88.6 L156.7 84.3 L158.2 80.1 L159.6 76.1 L161 72.2 L162.5 68.5 L163.9 65 L165.4 61.8 L166.8 58.8 L168.2 56 L169.7 53.5 L171.1 51.4 L172.6 49.5 L174 47.9 L175.4 46.7 L176.9 45.8 L178.3 45.2 L179.8 45 L181.2 45.1 L182.6 45.6 L184.1 46.4 L185.5 47.5 L187 48.9 L188.4 50.7 L189.8 52.8 L191.3 55.2 L192.7 57.8 L194.2 60.7 L195.6 63.9 L197 67.3 L198.5 71 L199.9 74.8 L201.4 78.8 L202.8 82.9 L204.2 87.2 L205.7 91.5 L207.1 96 L208.6 100.5 L210 105 L211.4 109.5 L212.9 114 L214.3 118.5 L215.8 122.8 L217.2 127.1 L218.6 131.2 L220.1 135.2 L221.5 139 L223 142.7 L224.4 146.1 L225.8 149.3 L227.3 152.2 L228.7 154.8 L230.2 157.2 L231.6 159.3 L233 161.1 L234.5 162.5 L235.9 163.6 L237.4 164.4 L238.8 164.9 L240.2 165 L241.7 164.8 L243.1 164.2 L244.6 163.3 L246 162.1 L247.4 160.5 L248.9 158.6 L250.3 156.5 L251.8 154 L253.2 151.2 L254.6 148.2 L256.1 145 L257.5 141.5 L259 137.8 L260.4 133.9 L261.8 129.9 L263.3 125.7 L264.7 121.4 L266.2 117 L267.6 112.5 L269 108 L270.5 103.5 L271.9 99 L273.4 94.5 L274.8 90.1 L276.2 85.7 L277.7 81.5 L279.1 77.4 L280.6 73.5 L282 69.7 L283.4 66.2 L284.9 62.8 L286.3 59.7 L287.8 56.9 L289.2 54.3 L290.6 52.1 L292.1 50.1 L293.5 48.4 L295 47.1 L296.4 46.1 L297.8 45.4 L299.3 45 L300.7 45 L302.2 45.4 L303.6 46.1 L305 47.1 L306.5 48.4 L307.9 50.1 L309.4 52.1 L310.8 54.3 L312.2 56.9 L313.7 59.7 L315.1 62.8 L316.6 66.2 L318 69.7" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="30" y1="105" x2="30" y2="196" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="150" y1="105" x2="150" y2="196" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="32" y1="192" x2="148" y2="192" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="30,192 36,189 36,195" fill="#0f172a"/>
<polygon points="150,192 144,195 144,189" fill="#0f172a"/>
<text x="90" y="186" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">T</text>
<line x1="60" y1="45" x2="60" y2="25" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="180" y1="45" x2="180" y2="25" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="62" y1="29" x2="178" y2="29" stroke="#0f6e56" stroke-width="1.6"/>
<polygon points="60,29 66,26 66,32" fill="#0f6e56"/>
<polygon points="180,29 174,32 174,26" fill="#0f6e56"/>
<text x="120" y="23" text-anchor="middle" fill="#0f6e56" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">T</text>
<circle cx="30" cy="105" r="4" fill="#0f172a"/>
<circle cx="150" cy="105" r="4" fill="#0f172a"/>
<circle cx="60" cy="45" r="4" fill="#0f6e56"/>
<circle cx="180" cy="45" r="4" fill="#0f6e56"/>
<text x="323" y="123" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">t</text>
<text x="18" y="32" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">u</text>
</svg>
:::

كلّ سهم في الشكل يحيط بجزء واحد من المنحنى يتكرّر كما هو: طوله هو T، وعدد هذه الأجزاء في ثانية واحدة هو N.

::: exemple من الدورة إلى التردّد

1. نضبط مولّد TBF على دورة T = 0,5 s: في ثانية واحدة نعدّ شكلين كاملين — لأنّ 1 s تحتوي مرّتين 0,5 s.
2. إذن N = 2 Hz، والحساب يؤكّد ذلك: N = 1/0,5 = 2 Hz — لأنّ التردّد عدد الدورات في الثانية.
3. التوتّر المنزلي: T = 0,02 s، إذن N = 1/0,02 = 50 Hz — لأنّ 0,02 s تتكرّر 50 مرّة في الثانية.
4. توتّر الجدول: T = 80 s، إذن N = 1/80 = 0,0125 Hz — تردّد صغير جدًّا، لذلك استطعنا تتبّعه بالعين.

:::

> ⚠️ **الخطأ الشائع**: أخذ المدّة بين صفرين متتاليين دورةً.
> في الجدول يمرّ u بالصفر عند t = 0 s ثمّ عند t = 40 s، لكنّه عند 0 s كان يصعد وعند 40 s ينزل: لم يستعد التطوّر نفسه. الدورة هي T = 80 s، والمدّة بين صفرين متتاليين نصف دورة فقط.

::: propriete
التردّد N والدورة T مقداران متعاكسان: N = 1/T و T = 1/N، بشرط أن تكون T بالثانية ليكون N بالهرتز.
للتيّار الجيبي الدورة نفسها والتردّد نفسه اللذان للتوتّر الذي يولّده. وفي كلّ دورة يكون التوتّر موجبًا مرّة ثمّ سالبًا مرّة: فالتيّار ينقلب اتّجاهه مرّتين في كلّ دورة، وكلّ صمّام من صمّامين متعاكسين يضيء مرّة واحدة في كلّ دورة.
مضاعفات الهرتز: الكيلوهرتز (kHz) والميغاهرتز (MHz) والجيغاهرتز (GHz).
$$ 1 kHz = 10³ Hz ; 1 MHz = 10⁶ Hz ; 1 GHz = 10⁹ Hz $$
حالة حدّية: T = 20 ms يجب تحويلها أوّلًا إلى 0,02 s، فنجد N = 50 Hz، لا 1/20 = 0,05 Hz.
:::

::: verifie
دورة توتّر جيبي T = 4 ms. ما تردّده بالهرتز ثمّ بالكيلوهرتز؟

---

نحوّل أوّلًا: T = 4 ms = 0,004 s، لأنّ N بالهرتز يتطلّب T بالثانية. ثمّ N = 1/0,004 = 250 Hz، أي 0,25 كيلوهرتز، لأنّ الكيلوهرتز الواحد يساوي 1000 Hz.
:::

::: retenir
الدورة T (s) مدّة الجزء الذي يتكرّر، والتردّد N (Hz) عدد الدورات في الثانية: N = 1/T.
:::

## 📺 مشواف الذبذبات — قراءة Um و T بالتدريجات

تردّد التوتّر المنزلي 50 Hz: خمسون دورة في الثانية، وهذا أسرع بكثير من أن نتابعه بفولتمتر وميقت.
مشواف الذبذبات يرسم لنا u بدلالة t على شاشة مقسّمة إلى تدريجات. فكيف نحوّل التدريجات إلى فولطات وإلى ثوانٍ؟

::: definition
**الحساسيّة العموديّة** (sensibilité verticale) هي عدد الفولطات الذي تمثّله تدريجة عموديّة واحدة، مثل 2 V لكلّ تدريجة.
**المسح** هو المدّة التي تمثّلها تدريجة أفقيّة واحدة، مثل 5 ms لكلّ تدريجة.
**القيمة القصوى** (valeur maximale) Um هي أكبر قيمة يبلغها التوتّر الجيبي، فيبقى محصورًا بينها وبين مقابلتها:
$$ −Um ≤ u ≤ +Um $$
:::

للمعاينة: نضع زرّ الانتقاء على الوضع ≃، ونصل القطب الأحمر للمولّد بالمدخل A والقطب الأسود بالهيكل، ثمّ نعدّل المسح والحساسيّة حتّى يثبت المنحنى ويملأ الشاشة.

::: figure Um يُعدّ بالتدريجات من الخطّ الأفقي المركزي إلى القمّة، و T بالتدريجات على طول شكل واحد يتكرّر
<svg viewBox="0 0 340 250">
<rect x="50" y="16" width="240" height="192" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<line x1="74" y1="16" x2="74" y2="208" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="98" y1="16" x2="98" y2="208" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="122" y1="16" x2="122" y2="208" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="146" y1="16" x2="146" y2="208" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="170" y1="16" x2="170" y2="208" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="194" y1="16" x2="194" y2="208" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="218" y1="16" x2="218" y2="208" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="242" y1="16" x2="242" y2="208" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="266" y1="16" x2="266" y2="208" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="50" y1="40" x2="290" y2="40" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="50" y1="64" x2="290" y2="64" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="50" y1="88" x2="290" y2="88" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="50" y1="112" x2="290" y2="112" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="50" y1="136" x2="290" y2="136" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="50" y1="160" x2="290" y2="160" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="50" y1="184" x2="290" y2="184" stroke="#94a3b8" stroke-width="0.8"/>
<line x1="50" y1="112" x2="290" y2="112" stroke="#94a3b8" stroke-width="1.6"/>
<line x1="170" y1="16" x2="170" y2="208" stroke="#94a3b8" stroke-width="1.6"/>
<path d="M50 112 L51.2 106.4 L52.4 100.7 L53.6 95.2 L54.8 89.8 L56 84.4 L57.2 79.3 L58.4 74.4 L59.6 69.7 L60.8 65.2 L62 61.1 L63.2 57.3 L64.4 53.8 L65.6 50.6 L66.8 47.8 L68 45.5 L69.2 43.5 L70.4 42 L71.6 40.9 L72.8 40.2 L74 40 L75.2 40.2 L76.4 40.9 L77.6 42 L78.8 43.5 L80 45.5 L81.2 47.8 L82.4 50.6 L83.6 53.8 L84.8 57.3 L86 61.1 L87.2 65.2 L88.4 69.7 L89.6 74.4 L90.8 79.3 L92 84.4 L93.2 89.8 L94.4 95.2 L95.6 100.7 L96.8 106.4 L98 112 L99.2 117.6 L100.4 123.3 L101.6 128.8 L102.8 134.2 L104 139.6 L105.2 144.7 L106.4 149.6 L107.6 154.3 L108.8 158.8 L110 162.9 L111.2 166.7 L112.4 170.2 L113.6 173.4 L114.8 176.2 L116 178.5 L117.2 180.5 L118.4 182 L119.6 183.1 L120.8 183.8 L122 184 L123.2 183.8 L124.4 183.1 L125.6 182 L126.8 180.5 L128 178.5 L129.2 176.2 L130.4 173.4 L131.6 170.2 L132.8 166.7 L134 162.9 L135.2 158.8 L136.4 154.3 L137.6 149.6 L138.8 144.7 L140 139.6 L141.2 134.2 L142.4 128.8 L143.6 123.3 L144.8 117.6 L146 112 L147.2 106.4 L148.4 100.7 L149.6 95.2 L150.8 89.8 L152 84.4 L153.2 79.3 L154.4 74.4 L155.6 69.7 L156.8 65.2 L158 61.1 L159.2 57.3 L160.4 53.8 L161.6 50.6 L162.8 47.8 L164 45.5 L165.2 43.5 L166.4 42 L167.6 40.9 L168.8 40.2 L170 40 L171.2 40.2 L172.4 40.9 L173.6 42 L174.8 43.5 L176 45.5 L177.2 47.8 L178.4 50.6 L179.6 53.8 L180.8 57.3 L182 61.1 L183.2 65.2 L184.4 69.7 L185.6 74.4 L186.8 79.3 L188 84.4 L189.2 89.8 L190.4 95.2 L191.6 100.7 L192.8 106.4 L194 112 L195.2 117.6 L196.4 123.3 L197.6 128.8 L198.8 134.2 L200 139.6 L201.2 144.7 L202.4 149.6 L203.6 154.3 L204.8 158.8 L206 162.9 L207.2 166.7 L208.4 170.2 L209.6 173.4 L210.8 176.2 L212 178.5 L213.2 180.5 L214.4 182 L215.6 183.1 L216.8 183.8 L218 184 L219.2 183.8 L220.4 183.1 L221.6 182 L222.8 180.5 L224 178.5 L225.2 176.2 L226.4 173.4 L227.6 170.2 L228.8 166.7 L230 162.9 L231.2 158.8 L232.4 154.3 L233.6 149.6 L234.8 144.7 L236 139.6 L237.2 134.2 L238.4 128.8 L239.6 123.3 L240.8 117.6 L242 112 L243.2 106.4 L244.4 100.7 L245.6 95.2 L246.8 89.8 L248 84.4 L249.2 79.3 L250.4 74.4 L251.6 69.7 L252.8 65.2 L254 61.1 L255.2 57.3 L256.4 53.8 L257.6 50.6 L258.8 47.8 L260 45.5 L261.2 43.5 L262.4 42 L263.6 40.9 L264.8 40.2 L266 40 L267.2 40.2 L268.4 40.9 L269.6 42 L270.8 43.5 L272 45.5 L273.2 47.8 L274.4 50.6 L275.6 53.8 L276.8 57.3 L278 61.1 L279.2 65.2 L280.4 69.7 L281.6 74.4 L282.8 79.3 L284 84.4 L285.2 89.8 L286.4 95.2 L287.6 100.7 L288.8 106.4 L290 112" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="74" y1="112" x2="74" y2="48" stroke="#dc2626" stroke-width="2"/>
<polygon points="74,40 77.5,47 70.5,47" fill="#dc2626"/>
<text x="46" y="80" text-anchor="end" fill="#dc2626" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">Um</text>
<line x1="122" y1="184" x2="122" y2="202" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="218" y1="184" x2="218" y2="202" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="124" y1="198" x2="216" y2="198" stroke="#dc2626" stroke-width="2"/>
<polygon points="122,198 128,195 128,201" fill="#dc2626"/>
<polygon points="218,198 212,201 212,195" fill="#dc2626"/>
<text x="170" y="192" text-anchor="middle" fill="#dc2626" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">T</text>
<text x="110" y="230" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">2 V/div</text>
<text x="230" y="230" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">5 ms/div</text>
</svg>
:::

السهم Um في الشكل يغطّي 3 تدريجات عموديّة، والسهم T يغطّي 4 تدريجات أفقيّة؛ الضبطان مكتوبان تحت الشاشة.

::: exemple قراءة الرسم التذبذبي

1. من الخطّ المركزي إلى القمّة 3 تدريجات، والحساسيّة 2 V لكلّ تدريجة، فنجد Um = 3 × 2 = 6 V — لأنّ كلّ تدريجة عموديّة تمثّل 2 V.
2. الشكل الذي يتكرّر يمتدّ على 4 تدريجات، والمسح 5 ms لكلّ تدريجة، فنجد T = 4 × 5 = 20 ms — لأنّ كلّ تدريجة أفقيّة تمثّل 5 ms.
3. نحوّل: T = 20 ms = 0,02 s، ثمّ N = 1/0,02 = 50 Hz — لأنّ العلاقة N = 1/T تتطلّب الثانية.

:::

> ⚠️ **الخطأ الشائع**: عدّ التدريجات من القعر إلى القمّة لحساب Um.
> من القعر إلى القمّة 6 تدريجات، أي 12 V: هذا ضعف القيمة القصوى (2Um). القيمة القصوى تُعدّ من **الخطّ المركزي** إلى القمّة: Um = 6 V.

::: methode
**القيمة القصوى = عدد التدريجات من الخطّ المركزي إلى القمّة × الحساسيّة العموديّة.**
**الدورة = عدد تدريجات الشكل الذي يتكرّر × المسح**، ثمّ N = 1/T بعد تحويل T إلى الثانية.
حالة حدّية: إذا أوقفنا المسح ترسم البقعة قطعة عموديّة طولها 2Um. مثال: قطعة من 3,4 تدريجة و 5 V لكلّ تدريجة تعطي 3,4 × 5 = 17 V = 2Um، إذن Um = 8,5 V.
:::

::: verifie
حساسيّة عموديّة 0,5 V لكلّ تدريجة، والقمّة على بعد 4 تدريجات من المركز؛ المسح 1 ms لكلّ تدريجة، والدورة تمتدّ على 5 تدريجات. أوجد Um و T و N.

---

Um = 4 × 0,5 = 2 V، لأنّنا نعدّ من المركز إلى القمّة. T = 5 × 1 = 5 ms = 0,005 s، لأنّ كلّ تدريجة أفقيّة 1 ms. ثمّ N = 1/0,005 = 200 Hz.
:::

::: retenir
على المشواف: Um = تدريجات (مركز ← قمّة) × الحساسيّة، و T = تدريجات دورة × المسح.
:::

## 💡 القيمة الفعّالة U و I — ما يقيسه الفولتمتر والأمبيرمتر

مولّد جيبي مضبوط على العلامة 12 V، ومشواف الذبذبات يعطي لتوتّره Um ≈ 17 V. ومع ذلك يشتغل مصباح 12 V بصفة عاديّة، ويشير الفولتمتر إلى 12 V.
فما الذي تعنيه 12 V هنا، إذا كان التوتّر يبلغ 17 V؟

نغذّي المصباح نفسه مرّة بالمولّد الجيبي (12 V) ومرّة بمولّد مستمرّ 12 V: يضيء بالشدّة نفسها، ويشير الفولتمتر إلى 12 V في الحالتين. ومع الضبط 6 V يحمرّ سلك المصباح فقط، مع المولّد الجيبي ومع مولّد مستمرّ 6 V على حدّ سواء.

::: definition
**القيمة الفعّالة** (valeur efficace) U لتوتّر جيبي هي قيمة التوتّر المستمرّ الذي يجعل المصباح نفسه يضيء بالشدّة نفسها. تُقاس بالفولتمتر.
وبالطريقة نفسها، **الشدّة الفعّالة** I لتيّار جيبي هي شدّة التيّار المستمرّ الذي يعطي المصباح الإضاءة نفسها. تُقاس بالأمبيرمتر.
:::

::: figure التوتّر الجيبي يصعد حتّى Um ≈ 17 V، لكنّ مفعوله في المصباح يساوي مفعول توتّر مستمرّ 12 V (الخطّ المتقطّع): تلك قيمته الفعّالة U
<svg viewBox="0 0 340 230">
<line x1="60" y1="115" x2="325" y2="115" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="331,115 324,118.5 324,111.5" fill="#0f172a"/>
<line x1="60" y1="210" x2="60" y2="16" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="60,10 63.5,17 56.5,17" fill="#0f172a"/>
<path d="M60 115 L61.2 109.4 L62.5 103.9 L63.8 98.4 L65 93 L66.2 87.7 L67.5 82.5 L68.8 77.4 L70 72.4 L71.2 67.6 L72.5 63 L73.8 58.7 L75 54.5 L76.2 50.6 L77.5 46.9 L78.8 43.5 L80 40.4 L81.2 37.5 L82.5 35 L83.8 32.8 L85 30.9 L86.2 29.4 L87.5 28.2 L88.8 27.3 L90 26.8 L91.2 26.6 L92.5 26.8 L93.8 27.3 L95 28.2 L96.2 29.4 L97.5 30.9 L98.8 32.8 L100 35 L101.2 37.5 L102.5 40.4 L103.8 43.5 L105 46.9 L106.2 50.6 L107.5 54.5 L108.8 58.7 L110 63 L111.2 67.6 L112.5 72.4 L113.8 77.4 L115 82.5 L116.2 87.7 L117.5 93 L118.8 98.4 L120 103.9 L121.2 109.4 L122.5 115 L123.8 120.6 L125 126.1 L126.2 131.6 L127.5 137 L128.8 142.3 L130 147.5 L131.2 152.6 L132.5 157.6 L133.8 162.4 L135 167 L136.2 171.3 L137.5 175.5 L138.8 179.4 L140 183.1 L141.2 186.5 L142.5 189.6 L143.8 192.5 L145 195 L146.2 197.2 L147.5 199.1 L148.8 200.6 L150 201.8 L151.2 202.7 L152.5 203.2 L153.8 203.4 L155 203.2 L156.2 202.7 L157.5 201.8 L158.8 200.6 L160 199.1 L161.2 197.2 L162.5 195 L163.8 192.5 L165 189.6 L166.2 186.5 L167.5 183.1 L168.8 179.4 L170 175.5 L171.2 171.3 L172.5 167 L173.8 162.4 L175 157.6 L176.2 152.6 L177.5 147.5 L178.8 142.3 L180 137 L181.2 131.6 L182.5 126.1 L183.8 120.6 L185 115 L186.2 109.4 L187.5 103.9 L188.8 98.4 L190 93 L191.2 87.7 L192.5 82.5 L193.8 77.4 L195 72.4 L196.2 67.6 L197.5 63 L198.8 58.7 L200 54.5 L201.2 50.6 L202.5 46.9 L203.8 43.5 L205 40.4 L206.2 37.5 L207.5 35 L208.8 32.8 L210 30.9 L211.2 29.4 L212.5 28.2 L213.8 27.3 L215 26.8 L216.2 26.6 L217.5 26.8 L218.8 27.3 L220 28.2 L221.2 29.4 L222.5 30.9 L223.8 32.8 L225 35 L226.2 37.5 L227.5 40.4 L228.8 43.5 L230 46.9 L231.2 50.6 L232.5 54.5 L233.8 58.7 L235 63 L236.2 67.6 L237.5 72.4 L238.8 77.4 L240 82.5 L241.2 87.7 L242.5 93 L243.8 98.4 L245 103.9 L246.2 109.4 L247.5 115 L248.8 120.6 L250 126.1 L251.2 131.6 L252.5 137 L253.8 142.3 L255 147.5 L256.2 152.6 L257.5 157.6 L258.8 162.4 L260 167 L261.2 171.3 L262.5 175.5 L263.8 179.4 L265 183.1 L266.2 186.5 L267.5 189.6 L268.8 192.5 L270 195 L271.2 197.2 L272.5 199.1 L273.8 200.6 L275 201.8 L276.2 202.7 L277.5 203.2 L278.8 203.4 L280 203.2 L281.2 202.7 L282.5 201.8 L283.8 200.6 L285 199.1 L286.2 197.2 L287.5 195 L288.8 192.5 L290 189.6 L291.2 186.5 L292.5 183.1 L293.8 179.4 L295 175.5 L296.2 171.3 L297.5 167 L298.8 162.4 L300 157.6 L301.2 152.6 L302.5 147.5 L303.8 142.3 L305 137 L306.2 131.6 L307.5 126.1 L308.8 120.6 L310 115" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="60" y1="52.6" x2="315" y2="52.6" stroke="#dc2626" stroke-width="2.2" stroke-dasharray="7 4"/>
<line x1="56" y1="26.6" x2="315" y2="26.6" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="56" y1="203.4" x2="315" y2="203.4" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<text x="52" y="30.6" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">17</text>
<text x="52" y="56.6" text-anchor="end" fill="#dc2626" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">12</text>
<text x="52" y="207.4" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">−17</text>
<text x="82" y="14" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">u (V)</text>
<text x="322" y="133" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">t</text>
</svg>
:::

الخطّ الأحمر المتقطّع هو U = 12 V، والقمم هي Um = 17 V: الخطّ الفعّال يقع دائمًا تحت القمم.

::: exemple البحث عن العلاقة بين Um و U

1. مع الضبط 12 V: Um/U = 17/12 ≈ 1,42 — لأنّ المشواف أعطى Um ≈ 17 V والفولتمتر أعطى U = 12 V.
2. مع الضبط 6 V: المشواف أعطى Um ≈ 8,5 V، فنجد Um/U = 8,5/6 ≈ 1,42 — النسبة نفسها.
3. نقارن بالعدد √2 ≈ 1,41: النسبتان تساويانه تقريبًا — لأنّ القيم المقيسة مدوّرة (12 × √2 ≈ 16,97 V).
4. إذن Um = U × √2 — ونجد من خلالها القيمة القصوى إذا عرفنا ما يشير إليه الفولتمتر.

:::

> ⚠️ **الخطأ الشائع**: «فولتمتر موصول بمنشب منزليّ يشير إلى 220 V، إذن التوتّر لا يتجاوز 220 V».
> الفولتمتر لا يقيس في التيّار الجيبي إلّا القيمة الفعّالة. التوتّر نفسه يبلغ Um = 220 × √2 ≈ 311 V. والخطأ المعاكس، ضرب القيمة القصوى في √2 للحصول على U، يعطي قيمة أكبر من Um، وهذا مستحيل.

::: propriete
$$ Um = U × √2 ; Im = I × √2 $$
ومنه U = Um ÷ √2 و I = Im ÷ √2: القيمة الفعّالة أصغر دائمًا من القيمة القصوى.
في التيّار الجيبي لا يقيس الفولتمتر إلّا U، ولا يقيس الأمبيرمتر إلّا I، أمّا المشواف فيعطي Um.
حالة مهمّة: التوتّر المنزلي في تونس جيبي، قيمته الفعّالة U = 220 V وتردّده N = 50 Hz، فدورته T = 0,02 s وقيمته القصوى Um ≈ 311 V.
:::

::: verifie
مصباح يحتاج في اشتغاله العادي إلى تيّار شدّته 0,5 A. نغذّيه بتيّار متناوب جيبي: ماذا يجب أن يشير إليه الأمبيرمتر؟ وما القيمة القصوى Im؟

---

يجب أن يشير الأمبيرمتر إلى I = 0,5 A، لأنّ الشدّة الفعّالة هي التي تعطي المصباح إضاءة التيّار المستمرّ نفسها. ثمّ Im = 0,5 × √2 ≈ 0,71 A.
:::

::: retenir
القيمة الفعّالة (U و I) هي ما يقيسه الفولتمتر والأمبيرمتر: Um = U × √2 و Im = I × √2؛ المنزل: 220 V و 50 Hz.
:::

> 🏆 فككتَ سرّ العلامة ~: تميّز المستمرّ من المتغيّر والمتناوب والجيبي، وتقرأ T و N و Um على المشواف، وتعرف أنّ 220 V قيمة فعّالة. الكهرباء المنزليّة في انتظارك!
