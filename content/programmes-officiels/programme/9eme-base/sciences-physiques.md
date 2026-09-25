# العلوم الفيزيائية (Sciences physiques) — 9ème année de base (année de concours national) · programme officiel CNP

> **Sources** (règle « sources combinées » — voir [`programme/README.md`](../README.md)) :
>
> - **Guide enseignant** : **AUCUN** au corpus CNP pour cette matière à ce niveau (`suivi/corpus-cnp.json` :
>   les seuls documents de physique de classe 9 sont les manuels élève `103902` et `123901`). Une seule
>   source de programme ⇒ le manuel élève fait référence, comme pour les maths et les SVT de 9ème.
> - **Manuel élève** (source de référence) : `103902P00.pdf` — « **العلوم الفيزيائية** — لتلامذة السّنة
>   التّاسعة من التّعليم الأساسي », المركز الوطني البيداغوجي. المؤلّفون : **توفيق بكّاري**، **الهادي خالد**،
>   **عبد الحميد بعطوط** ; المقيّمان : **أحمد العرضاوي**، **الفاضل ضحى**. **223 pages**, pagination PDF =
>   pagination imprimée.
>   **Pages lues** : p. 1–223 (intégralité), à l'image — la couche texte est un mojibake (encodage de police
>   propriétaire, lettres arabes rendues en caractères latins accentués), inutilisable sauf pour localiser.
>   Lecture du 2026-09-23 par quatre lecteurs en contexte vierge (leçons 1–7, 8–14, 15–22, 23–30), zooms
>   200–400 dpi sur tout encadré ou tableau douteux ; p. 1–8 lues par l'orchestrateur.
> - **Édition « collèges pilotes »** : `123901P00.pdf` (200 p., en FRANÇAIS, mêmes auteurs) — même carte
>   du livre (courant variable, électricité domestique, électrostatique, combustibles, atome, solutions
>   ioniques, réflexion/réfraction, lumière blanche). Consultée seulement pour recouper le chapitrage et
>   l'absence des leçons 29–30 (§6). ⚠️ Le contenu du corpus est en arabe : c'est **103902** qui le fonde ;
>   `subject.json` déclarait à tort `123901`.
>
> **Langue d'enseignement** : `ar`. **gradeSlug** : `9eme-base`. **subject id** : **`svt`** — ⚠️ id trompeur
> hérité : il porte **العلوم الفيزيائية**, pas les SVT (qui sont `sciences-vie-terre`, fiche `svt.md`).

## 1. Cadre & compétences (المقدّمة, p. 3 — extraits verbatim)

« أنجز هذا العمل في العلوم الفيزيائيّة لفائدة تلاميذ أقسام السّنة التّاسعة من التعليم الأساسي بهدف المساهمة
في : - مساعدتهم على ترسيخ ما بنوْا في القسم من مفاهيم متعلّقة سواء بالتفاعل الكيميائي والذرّة، بالمحاليل
المائيّة الشارديّة و ناقليّاتها للكهرباء، بالتيّار الكهربائي المتغيّر وتوليده أو بانعكاس الضوء و بانكساره،
و ذلك نتيجة ما قاموا به مع أساتذهم من معاينات و معالجات تجريبيّة تحليليّة لظواهر طبيعيّة بسيطة ومألوفة
كاحتراق بعض المواد في الأكسيجين وانحلال العديد من المواد الأخرى في الماء وانتشار الضوء وتغيّر مساره...
-تدريبهم على الاستعمال الوجيه لما حصل عندهم من معارف ومهارات و الإدماج الموفّق لما يلزم منها في حلّ
المشاكل، -تعويدهم على توخّي التمشّي العلمي في كلّ المواقف. » (p. 3)

Méthode déclarée (p. 3) : chaque leçon part de « قوادح في كلّ مرّة من تأمّلات و تساؤلات » vers des activités
(« تجارب في المخبر وبحوث ميدانيّة ») jusqu'à « الإستنتاج الصّحيح » ; en fin de باب, des exercices, un projet
simple, « هل من مزيد؟ » et un « ركن للتسلية الهادفة ». Rubriques de leçon (p. 8–11) : أتأمّل وأتساءل، أجرّب
وألاحظ، أستنتج، الخلاصة، أستغلّ وثيقة، أجرّب بنفسي، أقيّم مكتسباتي، أتمرّن على حلّ المسائل.

## 2. Plan annuel (خريطة الكتاب, p. 4–7) — 3 محاور, 7 أبواب, 30 دروس

| # | الدّرس | ص (réelles) | المحور | الباب | chapitre `svt/` |
| - | ------ | ----------- | ------ | ----- | --------------- |
| 1 | مفهوم التيّار الكهربائي المتغيّر | 15–19 | الكهرمغناطيس | التيّار الكهربائي المتغيّر | `08` |
| 2 | التيّار المتناوب | 20–28 | الكهرمغناطيس | التيّار الكهربائي المتغيّر | `08` |
| 3 | خاصيّات التيّار المتناوب الجيبي | 29–42 | الكهرمغناطيس | التيّار الكهربائي المتغيّر | `08` |
| 4 | الكهرباء المنزليّة | 43–54 | الكهرمغناطيس | الكهرباء المنزليّة | `10` |
| 5 | التكهرب بالاحتكاك | 55–58 | الكهرمغناطيس | الكهرباء الساكنة | `11` |
| 6 | التكهرب بالتماس | 59–61 | الكهرمغناطيس | الكهرباء الساكنة | `11` |
| 7 | الشحنة الكهربائيّة | 62–69 | الكهرمغناطيس | الكهرباء الساكنة | `11` |
| 8 | المحروقات : أنواعها، مصادرها واستعمالاتها | 70–75 | المادّة في الطبيعة | الذرّة والاحتراق | `12` |
| 9 | نقل المحروقات وتخزينها والحماية من مخاطرها | 76–85 | المادّة في الطبيعة | الذرّة والاحتراق | `12` |
| 10 | التفاعل الكيميائي | 86–88 | المادّة في الطبيعة | الذرّة والاحتراق | `05` |
| 11 | الذرّة | 89–94 | المادّة في الطبيعة | الذرّة والاحتراق | `04` |
| 12 | بنية الذرّة | 95–98 | المادّة في الطبيعة | الذرّة والاحتراق | `04` |
| 13 | رمز الذرّة والصيغ الكيميائيّة | 99–102 | المادّة في الطبيعة | الرموز الكيميائيّة | `04` |
| 14 | معادلات التفاعلات الكيميائيّة | 103–109 | المادّة في الطبيعة | الرموز الكيميائيّة | `05` |
| 15 | ناقليّة المحاليل المائيّة للكهرباء | 110–115 | المادّة في الطبيعة | المحاليل الشارديّة | `07` |
| 16 | تأثير التركيز على ناقليّة المحلول الشاردي للكهرباء | 116–117 | المادّة في الطبيعة | المحاليل الشارديّة | `07` |
| 17 | الأنيونات والكاتيونات | 118–122 | المادّة في الطبيعة | المحاليل الشارديّة | `07` |
| 18 | المحلول المائي الحامضي والمحلول المائي القلوي | 124–126 | المادّة في الطبيعة | المحاليل الشارديّة | `06` |
| 19 | قيس pH | 127–130 | المادّة في الطبيعة | المحاليل الشارديّة | `06` |
| 20 | درجة حموضة محلول مائي حامضي | 131–136 | المادّة في الطبيعة | المحاليل الشارديّة | `06` |
| 21 | درجة قلويّة محلول مائي قلوي | 137–141 | المادّة في الطبيعة | المحاليل الشارديّة | `06` |
| 22 | المحلول المتعادل | 143–151 | المادّة في الطبيعة | المحاليل الشارديّة | `06` |
| 23 | انعكاس الضوء | 152–159 | الضوء | تغيّر مسار الضوء | `02` |
| 24 | المرآة المسطّحة | 160–169 | الضوء | تغيّر مسار الضوء | `02` |
| 25 | انكسار الضوء | 170–175 | الضوء | تغيّر مسار الضوء | `03` |
| 26 | الانكسار الحدّي والانعكاس الكلّي | 176–181 | الضوء | تغيّر مسار الضوء | `03` |
| 27 | تطبيقات لتغيّر مسار الضوء | 182–189 | الضوء | تغيّر مسار الضوء | `03` |
| 28 | الأضواء المرئيّة والضوء الأبيض | 190–200 | الضوء | تغيّر مسار الضوء | `13` |
| 29 | مفهوم الطاقة الضوئيّة | — (absente du livre) | الضوء | الطاقة الضوئيّة | `—` |
| 30 | الطاقة الشمسيّة | — (absente du livre) | الضوء | الطاقة الضوئيّة | `—` |

Les pages « réelles » corrigent la خريطة là où elle se trompe (leçon 12 annoncée p. 96, commence p. 95 ;
ouvertures de باب comptées dans la leçon qui suit). Objectifs de chaque leçon : au §2 bis.

## 2 bis. Les 30 leçons — lues à l'image (2026-09-23)

> Notes de lecture telles quelles : objectifs, déroulé (données re-calculées), encadrés **الخلاصة /
> أستنتج VERBATIM** (ils font foi pour les définitions, formules, unités et symboles), exercices re-calculés,
> **bornes ✅/⛔ constatées**, vocabulaire officiel, incohérences du manuel. Le contenu ne reprend jamais une
> incohérence signalée ici.

### Leçon 01 — « مفهوم التيّار الكهربائي المتغيّر » (ص 15–19)

- **محور** : الكهرمغناطيس (ouverture p. 12 : photo d'éclair ; 3 أبواب : التيّار الكهربائي المتغيّر / الكهرباء المنزليّة / الكهرباء السّاكنة).
- **باب** : التيّار الكهربائي المتغيّر (ouverture p. 14 : دروس 1- مفهوم التيّار المتغيّر، 2- التيّار المتناوب، 3- خاصّيات التيّار المتناوب الجيبي).
- Type de séance (خريطة الكتاب p. 4) : icône « expérimentation » (télescope/savant).

### Ouverture du محور (p. 9–14) — relevé
- p. 9–11 : تقديم الكتاب / « كيف أستعمل كتابي ؟ » — rubriques du manuel : المحور المقترح، المكتسبات القبليّة، الأبواب المكوّنة للمحور، الدّروس المقترحة، قوادح في قالب تساؤلات، رقم الدرس وعنوانه، محتوى الدّرس (« أنشطة متنوّعة تعتمد على التّجربة و البحوث الميدانيّة انطلاقا من وضعيّات مختارة من الواقع المعيش أو المحيط، مشفوعة بمقترحات للتّقييم الذّاتي »)، استنتاج، الخلاصة، أستغلّ وثيقة، هل من مزيد؟، أتمرّن على حلّ المسائل، ركن للتّسلية الهادفة، أستعين ببعض العناوين.
- p. 13 **مكتسباتي القبليّة** (verbatim) :
  - المعارف : « 1- أعدّد تأثيرات التيار الكهربائي. 2- أعلم أنّ للتيّار الكهربائي اتّجاه. 3- أعرف ثبوت شدّة التيّار الكهربائي في مختلف نقاط دارة كهربائيّة بالتسلسل. 4- أسرد قانون توزيع التوتّر الكهربائي في دارة كهربائيّة بالتسلسل (قانون الحلقات). 5- أسرد قانون توزيع شدّة التيّار الكهربائي في دارة كهربائيّة بالتوازي (قانون العُقَد). »
  - المهارات : « 1- أميّز بين مولّد ومتقبّل. 2- أميّز بين ناقل وعازل. 3- أنجز رسما بيانيّا لدارة كهربائية. 4- أنجز دارة كهربائية بالتسلسل. 5- أنجز دارة كهربائية بالتّوازي. 6- أحدّد اتجاه التيار الكهربائي في دارة مغلَقة. 7- أقوم بتجاربَ تبيّن تأثيراتِ التيّار الكهربائي. 8- أقيس شدّة التيار الكهربائي. 9- أقيس التوتّر الكهربائي. 10- أتحقّق من ملائمة ثنائي قطب متقبّل مع ثنائي قطب مولّد. » (sic « ملائمة »)
- p. 14 photo « محطّة لتوليد التيّار الكهربائي المتغيّر » + قوادح : « إلامَ ترمز الإشارة ~ المسجّلة على علامة العديد من الأجهزة الكهربائيّة؟ » ; « ما هو الفرق بين التيّار الكهربائي الذي تُوفّره الشّركة التونسيّة للكهرباء والغاز والتيّار الكهربائي الذي تُولّده بطاريّة ؟ » ; « لماذا لا بدّ من استعمال ذلك الجهاز الصغير والمعروف بالمحوّل عند شحن بطارية الهاتف الجوّال أو عند تشغيل أجهزة إلكترونيّة أخرى بالكهرباء المنزليّة؟ »

### Objectifs (خريطة الكتاب p. 4)
- « التعرّف إلى تيّار كهربائي متغيّر. »
- « التعرّف إلى توتّر كهربائي متغيّر. »

### Déroulé
**§ ما هو التيّار المتغيّر ؟ (p. 15–16)**
- أتأمّل وأتساءل : « ما المقصود بالتيّار الكهربائي المتغيّر؟ هل هذا يعني أنّ هناك مولّدات يمكن أن توفّر تيّارا كهربائيّا مُغايرا للتيّار الذي يوفّره عمود جاف أو بطاريّة ؟ »
- أجرّب وألاحظ : matériel — عمود جاف ؛ جهاز تغذية يحمل العلامة ~ (photo « ALIMENTATION STABILISEE EL5 », sorties 6 V/12 V, bornes = et ~ ; شكل 1.a) ؛ صمّام مشعّ أخضر وصمّام مشعّ أحمر (شكل 1.b) ؛ معدّلة (لوقاية الصمّامين) ؛ أسلاك موصّلة.
  - Montage (شكل 2) : générateur + interrupteur + معدّلة en série avec deux DEL montées en parallèle et en sens inverses entre A et B.
  - Avec la pile (شكل 3) : seule la DEL rouge s'allume.
  - Avec l'alimentation ~ (شكل 4) : « ألاحظ أنّه بمجرّد غلق الدارة يشعّ الصمّامان معًا ».
- أحلّل وأفسّر : la verte ne s'allume pas dans le 1er montage « لأنّه موصَل بطريقة لا تسمح بعبور التيّار الكهربائي فيه من النقطة A إلى النقطة B » ; son allumage dans le 2e montage « يُثبت أنّ جهاز التغذية المستعمل والحامل للرمز~ أو∿ يدفق في الدارة الكهربائيّة الخارجيّة تيّارا في كلا الاتّجاهيْن ».

**§ شدّة التيّار المتغيّر (p. 17–18)**
- أتأمّل وأتساءل : projecteurs de spectacle dont l'intensité lumineuse varie en continu — quelle propriété du courant variable ?
- أجرّب وألاحظ : « جهاز تغذية بتيّار متغيّر من نوع خاصّ (يُعرف بمولّد TBF) » + مصباح + صمّام مشعّ (أخضر) + معدّلة + قاطع + أسلاك (شكل 5 : lampe et DEL en parallèle entre A et B). Observation : le filament rougit progressivement jusqu'à briller fortement puis revient à l'état initial, cycliquement ; en même temps la DEL clignote vert, mais « كلّما توهّج المصباح ولكن مرّة بمرّة » (une incandescence sur deux).
- أحلّل وأفسّر : variation de rougeur/éclat = variation de l'intensité ; clignotement de la DEL = changement de sens.

**§ التوتّر المتغيّر (p. 18–19)**
- Même montage (شكل 6) + مشواف ذبذبات branché aux bornes du TBF. « هامّ جدّا » : utiliser « الطريقة العمليّة المقترحة بصفحة 27 » mais laisser le balayage (المسح) non activé.
- Observation : circuit ouvert ou fermé, le spot lumineux ne reste pas fixe (comme avec un générateur continu, où il se déplace vers le haut ou le bas puis reste fixe) mais « تتحرّك عموديّا وبدون انقطاع في الاتّجاهين حول مركز الشاشة ».
- أحلّل وأفسّر : spot fixe ⇒ tension constante ; mouvement vertical continu autour du centre ⇒ « توتّر متغيّر في القيمة الجبريّة (القيمة المطلقة والعلامة) ».
- Aucune donnée chiffrée dans la leçon (pas de mesure, pas de calcul).

### Encadrés (VERBATIM)
- **أستنتج (p. 16)** : « خلافا للعمود الجافّ والبطاريّة وأجهزة التغذية الأخرى التي تغذّي الدّارة بتيّار كهربائي في اتّجاه وحيد هناك أجهزة يمكن لها أن تغذّي الدّارة بتيّار يدور فيها في كلا الاتّجاهين، يُسمّى مثل هذا التيّار تيّارا متغيّرا. »
- **أستنتج (p. 18)** : « زيادة على تغيّر اتجاه دورانه في الدارة يمكن للتيّار المتغيّر أن يتميّزَ بتغيّر شدّته مع الزمن. »
- **تعريف التيّار المتغيّر (encadré rose, p. 18)** : « التيّار الكهربائيّ المتغيّر هو كلّ تيّار غير ثابت في اتجاهه أو في شدّته مع الزمن. »
- (p. 18) « كلّ جهاز قادر على تزويد دارة بتيّار متغيّر يسمّى جهاز تغذية بتيّار متغيّر. »
- **ملاحظة (p. 18)** : « كلّ تيّار كهربائي ذي اتجاه وحيد وثابتٍ في شدّته مع الزمن مثل التيّار الذي يولّده عمود جاف أو بطاريّة في دارة مُغلقة يُنعتُ بالتيّار المستمر. بالتالي، كلّ تيّار غير مستمرّ هو تيّار متغيّر. »
- **أستنتج (p. 19)** : « بالإضافة إلى تلك المولّدات (العمود الجاف والبطاريّة...) التي تحفظ بين قطبيها توترا ثابتا يُعرف بالتوتّر المستمرّ هناك مولّدات تحفظ بين قطبيها توترا غير ثابت في القيمة الجبريّة يُعرف بالتوتّر المتغيّر u. بالتالي تُنعَت المولّدات من النوع الأوّل بمولّدات توتّر مستمرّ أمّا مولّدات النوع الثاني فتنعت بمولّدات توتّر متغيّر. »  « كلّ تيّار متغيّر في دارة مغلقة ناتج عن توتّر متغيّر يوفّره المولّد المستعمَل. »
- **ملاحظة (p. 19)** : « يشار عادة إلى كلّ مقدار فيزيائي متغيّر بحرف لاتيني صغير. بالتالي يشار إلى التوتّر المتغيّر بـ u عوضا عن U وللشدّة المتغيّرة بـ i عوضا عن I. »
- Symboles : ~ / ∿ (générateur variable), = (continu), TBF (مولّد), u, i (minuscules = grandeurs variables) vs U, I.

### Exercices
- **أقيّم مكتسباتي (p. 18)** : « بعد مدّة استعمال طويلة يصبح العمود الجافّ غير قادر على تزويد مصباح جيبي مثلا بتيّار كهربائي مستمرّ. لماذا، هل لأنّ التيّار أصبح يسري في اتجاهين أم لسبب آخر عليّ تبيينه؟ » — Réponse attendue : non, le sens reste unique ; c'est l'intensité qui n'est plus constante (elle diminue au cours du temps) → le courant n'est plus « مستمرّ » au sens de la définition (intensité non constante). *Ambiguïté* : le manuel ne dit rien sur l'usure de la pile ; réponse à déduire de la définition.
- **أقيّم مكتسباتي (p. 19), شكل 7** : deux graphes créneaux u1(t) et u2(t) (sans graduation chiffrée). u1 : créneau entre un niveau positif et ≈0 (jamais négatif) ; u2 : créneau alternant entre +a et −a (amplitude plus petite que u1).
  1. « أتبيّن إن كان كلّ من u1 و u2 متغيّرا أم مستمرّا » → les deux sont variables (non constants dans le temps) ; u1 garde un seul signe, u2 change de signe.
  2. « أريد تشغيل مصباح ولكنّ المولّد الذي بحوزتي لا يمكن أن يحفظ بين قطبيه إلاّ التوتّر u1 أو التوتّر u2. ما هو التوتّر الأنسب؟ لماذا؟ » — ⚠ **Énoncé ambigu** : une lampe à incandescence fonctionne quel que soit le sens ; le manuel ne donne ni valeurs ni tension nominale ; aucun critère « الأنسب » n'est enseigné. Pas de corrigé imprimé.

### Bornes
- ✅ Distinction courant/tension continus vs variables ; variable = sens et/ou intensité non constants dans le temps ; mise en évidence par 2 DEL tête-bêche, par la lampe (variation d'éclat) et par l'oscilloscope sans balayage (spot vertical).
- ✅ Notation minuscule u, i pour les grandeurs variables.
- ⛔ Aucune mesure chiffrée, aucune formule, aucune unité introduite.
- ⛔ Le mot « متناوب » n'apparaît pas encore (réservé à la leçon 2) ; pas de période ni fréquence.
- ⛔ L'oscilloscope est utilisé sans balayage ; son mode opératoire est renvoyé à p. 27.

### Vocabulaire officiel
التيّار الكهربائي المتغيّر (i) ؛ التوتّر المتغيّر (u) ؛ التيّار المستمرّ ؛ التوتّر المستمرّ ؛ جهاز تغذية بتيّار متغيّر ؛ مولّد TBF ؛ مولّدات توتّر مستمرّ / مولّدات توتّر متغيّر ؛ صمّام مشعّ ؛ معدّلة ؛ قاطع ؛ عمود جاف ؛ بطاريّة ؛ مشواف ذبذبات ؛ البقعة الضوئيّة ؛ المسح ؛ القيمة الجبريّة (القيمة المطلقة والعلامة) ؛ الاتّجاه ؛ الشدّة. (Correspondances françaises : voir lexique, relevé dans L07.)

### Leçon 02 — « التيّار المتناوب » (ص 20–28)

- **محور** : الكهرمغناطيس — **باب** : التيّار الكهربائي المتغيّر. Séance « expérimentation » (خريطة p. 4).
- Contient aussi (p. 24–28) la rubrique « أعوّل على نفسي : أتمرّن على حلّ المسائل » (5 تمارين) et « أجرّب بنفسي : كيف أستعمل مشواف الذبذبات ؟ » (p. 27–28), fiche à laquelle renvoient L01 (p. 18 → « صفحة 27 ») et L02 (p. 22 → « الصفحة 28 »).

### Objectifs (خريطة الكتاب p. 4)
- « التعرّف إلى توتّر متناوب. »
- « التعرّف إلى توتّر متناوب جيبي »

### Déroulé
**§ مفهوم التيّار المتناوب (p. 20–21)**
- أتأمّل وأتساءل : ampèremètres/voltmètres du labo à bouton glissant entre « = » et « ~ » (شكل 1, photo d'un milliampèremètre à aiguille, calibres 10 mA…5 A) : pourquoi la position ~ qu'on n'a jamais utilisée en 7e/8e ?
- أجرّب وألاحظ : مولّد تيّار متغيّر TBF ؛ أسلاك ؛ فولتمتر رقمي ؛ صمّام مشعّ أحمر وآخر أخضر ؛ معدّلة. Montage شكل 2 (TBF + interrupteur + معدّلة, deux DEL tête-bêche entre A et B). Le voltmètre numérique branché au générateur affiche alternativement des valeurs positives et négatives ; circuit fermé, les DEL s'allument alternativement : rouge ↔ valeurs positives, verte ↔ valeurs négatives.
- أحلّل وأفسّر (p. 21) : valeurs positives + DEL rouge ⇒ courant de A vers B hors du générateur, A joue le rôle de pôle + ; inversement pour la verte ⇒ B devient pôle +. « إذَنْ تداوُلُ سريانِ التيّار في الدّارة خارجَ المولّد من قطبه A إلى قطبه B مع سريانه من B إلى A ناتج عن تداوُل القطبينِ A وB مع بعضهما في الأدوار. »

**§ التوتّر المتناوب الجيبي (p. 21–22)**
- أجرّب وألاحظ : même montage + ميقت (chronomètre) ; mesure de u au voltmètre numérique toutes les 10 s. Tableau imprimé :

| t(s) | 0 | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 | 110 | 120 | 130 | 140 | 150 | 160 | 170 | 180 | 190 | 200 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| u(V) | 0 | 6 | 8,48 | 6 | 0 | -6 | -8,48 | -6 | 0 | 6 | 8,48 | 6 | 0 | -6 | -8,48 | -6 | 0 | 6 | 8,48 | 6 | 0 |

- Courbe u = f(t) (شكل 3) : « منحنى متكوّن من جيوب متتابعة ومتطابقة » ; axe t gradué 20, 60, 100, 140, 180 ; axe u : ±6.00 ; ±8.48.
- **Recalcul** : les données correspondent exactement à u = 6√2·sin(2πt/80) : période 80 s (f = 1/80 = 0,0125 Hz), amplitude 6√2 = 8,485 V (le manuel écrit 8,48, troncature) ; aux t = 10, 30… on a 8,485·sin 45° = 6,00 V. Rien de cela (période, fréquence, √2) n'est dit dans L02 ; c'est cohérent avec la valeur efficace 6 V de la leçon 3. Données cohérentes, aucune erreur.
- ملاحظة (p. 22) : on peut visualiser u(t) à l'oscilloscope « معتمدا الطريقة العمليّة المقترحة في الصفحة28 مع ضبط مناسب للمسح وللحساسيّة العموديّة » → oscillogramme (شكل 4) semblable à la شكل 3.

### Encadrés (VERBATIM)
- **أستنتج (p. 21)** : « هناك توتّرات كهربائيّة متغيّرة تتميّز بقيمة جبريّة تتغيّر بالتناوب مع الزمن بين سالبة وموجبة تُسمّى هذه التوتّرات توتّرات متناوبة. » ; « كلّ مولّد ذي توتّر متناوب يُغذّي دارة مُغلقة بتيّار يسري في الاتّجاهيْن بالتناوب يسمّى بدوره تيّارا متناوبا. »
- (p. 22) « …فأحصل على منحنى متكوّن من جيوب متتابعة ومتطابقة (الشكل 3). لذلك ينعت مثل هذا التوتّر المتناوب بالتوتّر المتناوب الجيبي. »
- **أستنتج (p. 22)** : « هناك من التوتّرات المتناوبة ما يتميّز بتطوّر جيبي بدلالة الزمن. » ; « يسمّى كلّ توتّر متناوب يتغيّر في شكل منحنى جيبي توتّرا متناوبا جيبيّا. »
- **الخلاصة (p. 23, encadré)** :
  - « التيّار الكهربائي الثابتُ في اتجاهه وفي شدّته مع الزمن هو تيّار مستمرّ. إن كان ليس كذلك فهو تيّار متغيّر. »
  - « كلّ تيّار متغيّر هو تيّار ناتج عن توتّر متغيّر، أي غير ثابت في قيمته الجبرية مع الزمن. »
  - « لا يغذّي المولّدُ الدّارةَ الكهربائية بتيّار متغيّر إلاّ إذا حفظ بين قطبيه توترا متغيّرا. »
  - « التوتّرات الكهربائية مختلفة، منها ماهو موجب فسالب على التّوالي وبدون انقطاع مع الزمن فيُسمّى توتّرا متناوبا. »
  - « التوتّر المتناوب يولّد في الدارة المغلَقة تيّارا متناوبا يتميّز بانقلاب متواصل لاتّجاهه مع الزمن من الموجب إلى السّالب فمن السالب إلى الموجب وهكذا دواليك. »
  - « التوتّر المتناوب الجيبيّ هو التوتّر المتناوب الذي يتميّز تطوّره مع الزمن بشكل جيبيّ لمنحَناه. »
  - « التوتّر الكهربائي المنزلي مثال للتوتّر المتناوب الجيبيّ. »
- **Fiche oscilloscope (p. 27–28, VERBATIM des items)** :
  - I. أتعرّف إلى أزرار المشواف وأقطابه : « 1 تشغيل/ توقيف ؛ 2 زرّ الانتقاء (~ ، ≃، 0) ؛ 3 المدخل A ؛ 4 الهيكل ؛ 5 المدخل B (مدخل ثانٍ مستقلّ عن المدخل A) ؛ 6 ضبط المسح ؛ 7 ضبط الحساسيّة العموديّة ؛ 8 ضبط الموضع الأفقي للبقعة الضوئيّة ؛ 9 ضبط الموضع العمودي للبقعة الضوئيّة ؛ 10 الإشراقة (أو النورانيّة) ؛ 11 التركيز ». (Façade : M/A, Luminosité, Focus, Balayage ms/µs 0,1…50, Voie A/Voie B, V/mV 1…50 / 20…100.)
  - II. أقوم بتعديلات أوّليّة للمشواف : 1. أشغّل (زرّ 1) ; 2. زرّ الانتقاء 2 « على الموضع 0 » ; 3. si rien n'apparaît, tourner le bouton 9 ; 4. « أعدّل المسح: أدير الزر 6 إلى أن تصبح البقعة الضوئيّة ثابتة على الشاشة في شكل خطّ أفقي » ; 5. bouton 8 jusqu'à ce que le trait couvre toute la largeur ; 6. luminosité (10) et focus (11) ; 7. bouton 9 → trait horizontal et central. « ملاحظة: للتثبّت من حسن التعديلات الأوّليّة التي قمت بها، يجب أن أحصل على بقعة ضوئيّة نقطيّة في مركز الشاشة عندما أوقف المسح. »
  - III. أُظهِر توتّرا كهربائيّا (بين قطبَي مُولّد مثلا) على شاشة المشواف : 1. « أنقل زرّ الانتقاء 2 إلى الموضع ≃ مهما كان نوع التوتّر (مستمرًّا أو متغيّرا) » ; 2. relier la borne rouge à l'entrée A ou B, la borne noire (pôle − en continu, ou borne marquée 0 ou ⏚) à la masse 4 ; ملاحظة : fil rouge pour les bornes rouges, fil noir pour les noires ; 3. « أعدّل المسح 6 والحساسيّة العموديّة 7 لكي أحصل على رسم تذبذبي ثابت ومنتشر على مجمل مساحة شاشة المشواف يمثّل تطوّر التوتّر بدلالة الزمن: u = f(t). »
- Symboles : ~, =, ≃ (tel qu'imprimé), u = f(t), V, s.

### Exercices
- **أقيّم مكتسباتي (p. 23), شكل 5** : (1) u1(t) aux bornes d'une dynamo de vélo — courbe périodique alternant +/−, forme non sinusoïdale (pics pointus asymétriques) ; (2) u2(t) aux bornes d'une prise domestique — sinusoïde. Question : متغيّر؟ متناوب؟ جيبي؟ → u1 : variable, alternative, non sinusoïdale ; u2 : variable, alternative, sinusoïdale (cohérent avec الخلاصة « التوتّر الكهربائي المنزلي مثال للتوتّر المتناوب الجيبيّ »).
- **تمرين 1 (QCM, p. 24)** :
  1. « لا يكون التيار الكهربائي متغيّرا في دارة مغلقة إلاّ إذا » → « كان التوتّر بين قطبي المولّد الذي يغذّيه متغيّرا مع الزمن » (seule condition nécessaire, cf. الخلاصة « لا يغذّي… إلاّ إذا »). ⚠ Les options « اتجاهه يتغيّر » et « شدّته تتغيّر » sont suffisantes mais pas nécessaires ; « اتجاهه وشدّته يتغيّران » est trop restrictive.
  2. « يتميّز التوتّر الكهربائي المتغيّر بـ » → « تغيّر قيمته الجبريّة مع الزمن ».
  3. « يكون التيّار المتغيّر متناوبا عندما » → « يمرّ في دارة مغلقة تارةً في اتّجاه وتارةً في الاتّجاه المعاكس ». ⚠ L'option « يتغيّر اتجاهه مع تغيّر التوتّر الذي يولّده » est aussi défendable (formulation floue) ; « يتغيّر اتجاهه وشدّته معًا وباستمرار » aussi vraie pour un courant alternatif mais pas caractéristique. Plusieurs réponses discutables.
- **تمرين 2 (texte à trous, p. 24)** — mots : توتّر – موجبة – سالبة – متغيّر – تيّار – المتناوب – تغذية – جيبي. Réponses reconstituées :
  - « يُغذّي مولّد توتّر **متغيّر** دارة مُغلقة بـ**تيّار** متغيّر بدلالة الزمن. »
  - « التوتّر **المتناوب** هو كلّ توتّر **متغيّر** يأخذ بالتداول قِيمًا **موجبة** وأخرى سالبة. »
  - « يَنتُج عن كلّ **تغذية** دارة كهربائيّة بـ**توتّر** متناوب جيبي **تيّار** متناوبٌ **جيبي** في تلك الدارة. »
  - « يأخذ التوتّر المتناوب بالتداول قيما **سالبة** وقيما موجبة بدلالة الزمن. »
  (⚠ « متغيّر » sert deux fois ; la liste n'est pas en correspondance 1-1 avec les trous.)
- **تمرين 3 (vrai/faux, p. 25)** :
  1. « يُستعمَل العمود الجافّ لتغذية دارة مغلقة بتيّار كهربائي متغيّر » → faux.
  2. « التيّار الكهربائي المتغيّر هو كلّ تيّار ثابت في اتجاهه ومتغيّر في شدّته » → faux (définition incomplète : « أو »).
  3. « التوتّر المتغيّر هو كلّ توتّر غير ثابت في القيمة الجبريّة » → vrai.
  4. « تيّار كهربائي ذو شدّة جبريّة غير ثابتة بدلالة الزمن هو كلّ تيّار يُوفّره مولّد توتّر متغيّر » → vrai (cf. « كلّ تيّار متغيّر ناتج عن توتّر متغيّر »). ⚠ phrase maladroite (sujet/attribut inversés).
  5. « كلّ تيّار كهربائي متغيّر هو تيّار متناوب » → faux.
  6. « سواء كان التيّار الكهربائيّ متغيّرا أو مستمرّا في الدارة المغلقة فللمولّد قطب موجب وقطب سالب في كلّ لحظة » → ⚠ **ambigu** : réponse attendue probablement « faux » (en alternatif les pôles s'échangent, p. 21), mais littéralement, à chaque instant où u ≠ 0 il existe bien un pôle + et un pôle −.
  7. « كلّ تيّار متناوب جيبي هو تيّار متغيّر » → vrai.
- **تمرين 4 (p. 25)** : trois montages (1) pile + interrupteur + معدّلة + DEL ; (2) générateur ~ ; (3) TBF ~ ; même DEL orientée de B vers A (même sens que la DEL verte de L01 شكل 3, qui ne s'allumait pas avec la pile).
  1. Courant variable : montages (2) et (3).
  2. Appariement : (1) → لا يضيء (DEL en sens bloquant ; pile : grand trait à gauche) ; (2) → يضيء دائما ; (3) → يرفّ. ⚠ L'appariement (2)/« يضيء دائما » repose sur la fréquence élevée d'un générateur ~ (réseau) vs basse fréquence du TBF — notion (fréquence, persistance rétinienne) non enseignée à ce stade ; l'élève doit la deviner.
- **تمرين 5 (p. 26)** : six graphes u(t) : (a) constante positive ; (b) sinusoïde centrée ; (c) dents de scie triangulaires alternées (+/−) ; (d) demi-alternances positives (redressement simple alternance) ; (e) constante négative ; (f) sinusoïde décalée restant ≥ 0.
  1. Variables : b, c, d, f. 2. Alternatives : b, c (b seule sinusoïdale ; non demandé).

### Bornes
- ✅ Tension/courant alternatif (changement de signe / de sens, échange des rôles des pôles) ; tension alternative sinusoïdale ; tension du secteur = exemple de sinusoïdale ; lecture des positions = / ~ des appareils ; mode opératoire de l'oscilloscope (réglages, u = f(t)).
- ✅ Courbe tracée point par point à partir d'un tableau de mesures (voltmètre numérique + chronomètre).
- ⛔ Aucune notion de période, fréquence, amplitude ou valeur maximale dans cette leçon (réservée à L03) ; la valeur 8,48 V n'est pas nommée ; aucune expression u = Um·sin(…) n'est écrite.
- ⛔ Pas de mesure d'intensité en alternatif ici.

### Vocabulaire officiel
التيّار المتناوب ؛ التوتّر المتناوب ؛ التوتّر المتناوب الجيبي ؛ منحنى جيبي / جيوب متتابعة ومتطابقة ؛ فولتمتر رقمي ؛ ميقت ؛ مشواف الذبذبات (المشواف) ؛ رسم تذبذبي ؛ المسح ؛ الحساسيّة العموديّة ؛ زرّ الانتقاء ؛ المدخل A / المدخل B ؛ الهيكل ; الإشراقة (النورانيّة) ؛ التركيز ؛ البقعة الضوئيّة ؛ القطب الموجب / القطب السالب ؛ يرفّ ؛ دينامو دراجة ؛ منشب تيّار كهربائي منزلي.

### Leçon 03 — « خاصيّات التيّار المتناوب الجيبي » (ص 29–42)

- **محور** : الكهرمغناطيس — **باب** : التيّار الكهربائي المتغيّر. Séance « expérimentation » (خريطة p. 4).
- Structure : cours p. 29–36 (الخلاصة p. 36) ; « أعوّل على نفسي : أتمرّن على حلّ المسائل » p. 37–41 (تمارين 1–10) ; « أستغلّ وثيقة : التوتّرات المتناوبة والطب » p. 42. (p. 43 = ouverture du باب الكهرباء المنزليّة → L04.)

### Objectifs (خريطة الكتاب p. 4)
- « قيس التوتّر الفعّال بالنسبة إلى تيّار متناوب جيبي. »
- « قيس الشدّة الفعّالة بالنسبة إلى تيّار متناوب جيبي. »

### Déroulé
**أتأمّل وأتساءل (p. 29)** : plaque signalétique (شكل 1 : « CD RADIO CASSETTE-CORDER / AC: 220 V ~ 50Hz 20W / DC: 9V ⎓ FLASHLIGHT BATTERY R20 SIZE D x 6 OR EQUIVALENT ») : « ما المقصود بالكتابة 220V-50Hz… ؟ » ; transformateur 220 V / 110 V (شكل 2) : « لماذا لا بدّ من استعمال ما يُعرف بالمُحوّل والذي كتب عليه 220V-110V ؟ ».

**§ دورة التوتّر المتناوب الجيبي (p. 29–30)** — reprise de la courbe de L02 (شكل 3, ±8.48 V, maxima à 20, 100, 180 s). شكل 4 : trois « مقاطع صغرى متطابقة » A1B1, A2B2, A3B3 choisis à des débuts différents (0→80 s ; 60→140 s ; ~25→105 s) : « فإنّ المدّة التي تفصل نقطة النهاية Bj عن نقطة البداية Aj تبقى هي نفسها Δt1=Δt2=Δt3=80s » ⇒ u varie « دوريّا (أو بصفة دوريّة) » ; « أمّا تلك المدّة الزمنيّة Δt =80s فتُسمَّى دورة التوتّر ». ✔ Cohérent avec le tableau de L02 (période 80 s recalculée).
- أقيّم مكتسباتي (p. 31) : refaire « التركيب المرسوم في الشكل6 صفحة 96 », visualiser u, mesurer T sachant « زرّ المسح يشير إلى 0,2s/div ». ⚠ **Renvoi erroné probable** : « صفحة 96 » ne correspond pas à cette partie (le montage TBF + oscilloscope est la شكل 6 de la p. 18). Lecture de l'oscillogramme imprimé (écran 12 div × 10 div) : période ≈ 4,6 div ⇒ T ≈ 0,9 s ; la suite (« أنقص… إلى أن تبلغ 0,5s ») suggère une valeur voulue de 1 s (5 div) — dessin imprécis, pas de réponse imprimée.

**§ تردّد التيّار المتناوب الجيبي (p. 31–32)** — on diminue T au bouton du TBF jusqu'à 0,5 s. « ملاحظة: …لا أنسى أن أعدّل المسح بواسطة الزرّ 2 طبعًا للمشواف. » ⚠ **Erreur de renvoi** : sur la fiche p. 27, le bouton 2 est « زرّ الانتقاء » ; le balayage est le bouton **6**. شكل 5 : Δt = 1 s contient 2 motifs ⇒ « التوتّر ذا الدورة T=0,5s له تردّد N يساوي مقطعين في الثانية الواحدة ». Relation : « مدّة المقطع الأصغر الواحد هي T. بالتّالي فإنّ عدد المقاطع الصغرى في الثانية الواحدة هو N=1/T أي عدد المقاطع الصغرى في الثانية الواحدة هو N ، وهذا يعني أنّ مدّة المقطع الأصغر هي T=1/N ». Recalcul : 1/0,5 = 2 Hz ✔.

**§ القيمة القصوى للتوتّر المتناوب الجيبي (p. 32–33)** — مولّد توتّر متناوب جيبي « حامل للعلامة 12V » + مشواف + قاطع + أسلاك. Crêtes et creux symétriques (شكل 7.a) ⇒ « u يتراوح في تغيّره بدلالة الزمن بين القيمتين المتقابلتين u1 = 17 V و u2 = -17 V ». « توصية عمليّة » : couper le balayage → segment vertical (شكل 7.b) « يمثّل طوله 2× 17V ».

**§ القيمة الفعّالة للتوتّر المتناوب الجيبي (p. 34–35)** — matériel : مولّد جيبي « 6 V-12 V », مولّد مستمرّ 12 V, مولّد مستمرّ 6 V, مصباح (12 V), فولتمتر, قاطع (شكل 8 : lampe + voltmètre aux bornes du générateur).
- Sinusoïdal réglé sur 12 V → la lampe brille, voltmètre « U = 12 V » ; continu 12 V → même éclat, 12 V.
- Sinusoïdal réglé sur 6 V → filament seulement rouge, voltmètre « U’= 6 V » ; continu 6 V → même état, 6 V.
- Rappel Um = 17 V (12 V) et U’m = 8,5 V (6 V) : chercher Um/U et U’m/U’ et comparer à √2. **Recalcul** : 17/12 = 1,4167 ; 8,5/6 = 1,4167 ; √2 = 1,4142 (écart 0,17 % — valeurs arrondies ; 12√2 = 16,97 V, 6√2 = 8,49 V).

**§ القيمة الفعّالة لشدّة التيّار المتناوب الجيبي (p. 35)** — مولّد جيبي de valeur efficace 12 V, مولّد مستمرّ 12 V, مصباح (12 V), أمبيرمتر, قاطع (شكل 10, série). Même éclat, même indication I de l'ampèremètre ⇒ I = valeur efficace de l'intensité. « ملاحظة: باتّباع نفس الطريقة المعتمدة للتوتّر يمكن أن أبيّن أنّ Im = I.√2 » (aucune mesure chiffrée d'intensité).

### Encadrés (VERBATIM)
- **أستنتج (p. 30)** :
  - « التوتّر المتناوب الجيبي مقدار فيزيائي دوريّ لأنّه يأخذ نفس القيمة الجبريّة (مع تطوّره في نفس الاتّجاه) إثر مُدَدٍ متتالية ومتساوية تمثّل الواحدة منها دورةَ التوتّر ويشار إليها بالحرف اللاتيني T »
  - « بما أنّ كلّ توتّر متناوب جيبي يُنتج في دارة مغلقة تيّارا كهربائيّا متناوبا جيبيّا فإنّ شدّة التيّار مقدار متناوب جيبيّ. وبالتالي فإنّ التيّار المتناوب الجيبي ظاهرةٌ دوريّة وشدّته مقدار دوريّ. »
  - « دورة التيّار المتناوب الجيبي هي نفسها دورة شدّته ودورة التوتّر الذي أحدثه. »
  - « الدورة مقدار قابل للقيس ووحدتها العالميّة هي الثانيةُ وحدةُ الزمن. »
- **أستنتج (p. 32)** :
  - « بالإضافة إلى الدورة تتميّز دوريّة التيّار الكهربائي المتناوب الجيبي بالتردّد وهو عدد التطوّرات المتتالية والمتطابقة في الثانية الواحدة. يشار عادة إلى التردّد بالحرف اللاتيني N »
  - « تردّد التيّار المتناوب الجيبي هو نفسه تردّد شدّته وتردّد التوتّر الذي أحدثه. »
  - « التردّد مقدار قابل للقيس ووحدته العالميّة هي الهِرتز، ورمزها Hz. »
  - « من مضاعفات الهرتز هناك: - الكيلوهرتز، ورمزه kHz : 1kHz = 10³ Hz - الميغاهرتز، ورمزه MHz : 1MHz = 10⁶ Hz - الجيغاهرتز، ورمزه GHz : 1GHz = 10⁹ Hz »
  - « التردّد N للتيّار المتناوب الجيبي مرتبط بدورته T ، والعلاقة بينهما هي: **N = 1/T** » (encadré)
- **أستنتج (p. 33)** : « في تغيّره بدلالة الزمن يبقى التوتّر المتناوب الجيبي متراوحا بين قيمة قصوى Um وقيمة دنيا مقابلة للأولى : **-Um ≤ u ≤ +Um** » ; « يمكّن مشواف الذبذبات من قيس القيمة القصوى Um للتوتّر »
- **أستنتج (p. 35)** : « يتميّز التوتّر المتناوب الجيبي بمقدار يسمّى التوتّر الفعّال تساوي قيمته قيمة التوتّر المستمرّ الذي يعطي للمصباح إشعاعا بنفس الشدّة. » ; « تقاس القيمة الفعّالة للتوتّر المتناوب الجيبي بواسطة الفولتمتر. » ; « القيمة الفعّالة U للتوتّر المتناوب الجيبي مرتبطة بقيمتها القصوى Um والعلاقة بينهما هي: **Um = U√2** »
- **أستنتج (p. 36)** : « الشدّة الفعّالة مقدارٌ تتميّز به شدّة التيّار المتناوب الجيبي وتساوي قيمتُه قيمةَ شدّة التيّار المستمرّ الذي يعطي للمصباح إشعاعا بنفس الشدّة. » ; « تقاس القيمة الفعّالة لشدّة التيّار المتناوب الجيبي بواسطة الأمبيرمتر. » ; « القيمة الفعّالة I لشدّة التيّار المتناوب الجيبي مرتبطة بقيمتها القصوى Im حسب : **Im = I √2** »
- **الخلاصة (p. 36)** :
  - « التيّار المتناوب الجيبيّ تيّار كهربائي دوريّ في التوتّر u الذي يتولّد عنه وفي شدّته i. »
  - « دورة التيّار المتناوب الجيبيّ T هي المدّة الزمنيّة للتطوّر الجزئي الذي يتكرّر للتوتّر u المتولّد عنه أو لشدّته i كما هو وبدون انقطاع، بينما التردّد N هو عددُ تلك التطوّرات الجزئيّة المتطابقة والمتتابعة في الثانية الواحدة. **N = 1/T** »
  - « مشواف الذبذبات جهاز عمليّ لإظهار الرسوم التذبذبية للتوتّرات الكهربائيّة المتناوبة ذات التردّد الذي لا يسمح بالمتابعة المباشرة لتطوّرها مع الزمن. »
  - « بالاضافة إلى دوريّته مع الزمن يتميّز التيّار المتناوب الجيبيّ بأنّ للتوتّر المتولّد عنه قيمة قصوى Um وقيمة فعّالة U وبأنّ لشدّته قيمة قصوى Im وقيمة فعّالة I. **Um = U √2 ; Im = I √2** »
  - « التوتّر الفعّال U والشدّة الفعّالة I للتيّار المتناوب الجيبيّ هما المقداران المساويان على التوالي لقيمةَ التوتّر المستمرّ U ولقيمة شدّة التيّار المستمرّ I الذي يعطي للمصباح إشعاعا بنفس الشدّة. »
  - « بالنسبة إلى التيّار المتناوب الجيبيّ لا يقيس الفولتمتر إلاّ التوتّر الفعّال U في حين أنّ الأمبيرمتر لا يقيس إلاّ الشدّة الفعّالة I. »
  - « التوتّر الكهربائي المنزليّ في بلادنا هو توتّر متناوب جيبيّ ذو تردّد N = 50 Hz وقيمة فعّالة U = 220 V. »
- Symboles/unités : T (s), N (Hz, kHz, MHz, GHz), Um, U, Im, I, u, i, √2, div, s/div, ms/div, V/div.

### Exercices (avec recalculs)
- **أقيّم مكتسباتي p. 32 (شكل 6)** : tension domestique, axe t en 10⁻² s (graduations 0,5 … 4,5) ; passages par zéro à 1, 2, 3, 4 ×10⁻² s ⇒ T = 2×10⁻² s = 0,02 s ⇒ **N = 50 Hz**.
- **أقيّم مكتسباتي p. 33** : générateur « 6 V » ; sans balayage, segment de 3,4 div à 5 V/div ⇒ 17 V = 2U’m ⇒ **U’m = 8,5 V** ✔ (vérification demandée).
- **أقيّم مكتسباتي p. 35 (شكل 9)** : tension domestique, crêtes ±311 V, même axe (T = 0,02 s). 1) **Um = 311 V** ; 2) **U = 311/√2 = 219,9 ≈ 220 V**.
- **أقيّم مكتسباتي p. 36** : lampe nécessitant 0,5 A en fonctionnement normal : 1) oui, on peut l'alimenter en sinusoïdal ; 2) **I (efficace) = 0,5 A** (Im = 0,5√2 = 0,71 A, non demandé).
- **تمرين 1 (p. 37, trous)** — mots : مشواف الذبذبات – نصف دورة – دورة – الأمبيرمتر – الفعّالة – القيمة – التوتّر – التيّار – تطوّر – الاتّجاه. Reconstitution : « إثر كلّ **دورة** يستعيد **التيّار** المتناوب الجيبيّ نفس **القيمة** مع **تطوّر** في نفس الاتّجاه » ; « يعكس **التيّار** المتناوب الجيبيّ اتّجاه سريانه إثر كلّ **نصف دورة** وتستعيد شدّته نفس **القيمة** مع تطوّر في نفس **الاتّجاه** إثر كلّ دورة » ; « بالنسبة إلى **التوتّر** المتناوب الجيبيّ نستعمل الفولتمتر لقيس قيمته **الفعّالة** و **مشواف الذبذبات** لقيس قيمته القصوى » ; « بالنسبة إلى **التيّار** المتناوب الجيبيّ لا يُستعمَل **الأمبيرمتر** إلاّ لقيس القيمة **الفعّالة** لشدّته ». ⚠ « نصف دورة » (inversion du sens à chaque demi-période) n'est jamais énoncé dans le cours.
- **تمرين 2 (tableau)** : الدّورة → ثانية, s ; (colonne à remplir) → التردّد, هرتز, Hz (le « هرتز » est pré-imprimé) ; التوتّر الفعّال → فولت, V ; شدّة التيّار القصوى → أمبير, A.
- **تمرين 3.1 (cases)** : « لا يكون التوتّر المتناوب إلاّ موجبا أو سالبا » → ⚠ ambigu (u s'annule aussi ; attendu probablement faux) ; « تقاس القيمة القصوى… بفولتمتر و… الفعّالة بالمشواف » → faux (inversé) ; « Um أكبر من U إذ تساوي √2.U » → vrai ; « وحدة قيس التوتّر هي الفولت ووحدة قيس الدورة هي الهرتز » → faux ; « تتغيّر قيمة التوتّر المتناوب بدلالة الزمن » → vrai.
- **تمرين 3.2** : oscillogramme en créneaux, alternativement au-dessus et au-dessous de l'axe central avec des hauteurs (≈ +3,2 ; −3 ; +1 ; −1 ; +2 div) et des durées inégales → **« متناوب غير دوري »**.
- **تمرين 3.3 (p. 38)** : réglages 4 ms/div et 2 V/div ; choix : (a) Um=6,5mV ; T=15ms ; N=66,7Hz — (b) Um=13V ; T=15ms ; N=15Hz — (c) Um=6,5V ; T=15ms ; N=66,7Hz — (d) Um=6,5V ; T=7,5ms ; N=133Hz. Crête ≈ 3,25 div × 2 V/div = **6,5 V**. Réponse attendue **(c)** (1/0,015 = 66,67 Hz ✔ ; (d) est aussi cohérente en interne : 1/0,0075 = 133,3 Hz). ⚠ **Figure incohérente** : la période lue sur l'oscillogramme imprimé ≈ 2,8 div (≈ 11 ms), ni 3,75 div (15 ms) ni 1,875 div (7,5 ms).
- **تمرين 4 (p. 38)** : courbe i(t) sinusoïdale ; 1) « جيبي » ; 2) Y (du zéro à la crête) = **« القصوى »** ; 3) X (creux à creux) = **« دورة »**.
- **تمرين 5 (p. 38)** : 4 oscillogrammes (a)–(d), mêmes réglages. 1) tous sinusoïdaux alternatifs ; 2–4) à lire sur la photo : (b) et (d) plus grande amplitude apparente, (a) plus petite ; (b) plus grande période / plus petite fréquence, (a) et (c) plus petites périodes / plus grandes fréquences. ⚠ Photo trop petite pour trancher entre (a) et (c) ; pas de valeurs.
- **تمرين 6 (p. 39)** : tableau t(ms) 0…22 / u(V) : 0, −6, −10,4, −12, −10,4, −6, 0, 6, 10,4, 12, 10,4, 0. Échelle 1 cm ↔ 2 ms ; 1 cm ↔ 2 V. **Recalcul** : u = −12·sin(2πt/24 ms) (12·sin30° = 6 ; 12·sin60° = 10,39 ✔). 2) variable et alternative ; 3) **T = 24 ms**, **N = 1/0,024 = 41,7 Hz**. ⚠ Le tableau s'arrête à 22 ms (période non entièrement couverte) ; T se déduit de l'écart entre les zéros (0 et 12 ms = T/2) ou min (6 ms) / max (18 ms).
- **تمرين 7** : secteur STEG, U = 220 V, N = 50 Hz. 1) **T = 1/50 = 0,02 s = 20 ms** ; 2) tracé (1 cm ↔ 10 ms ; 1 cm ↔ 100 V ⇒ Um = 220√2 = **311,1 V** → 3,11 cm ; T → 2 cm) ; 3) **100 fois par seconde** (2 zéros par période × 50) ; 4) pas de clignotement visible car la fréquence est trop élevée pour l'œil. ⚠ Ce dernier point (persistance rétinienne) n'est pas enseigné dans la leçon.
- **تمرين 8 (p. 39–40)** : générateur ~, D1 et D2 tête-bêche chacun avec une résistance R, voltmètre aux bornes ; u(t) sinusoïdale Um = 3 V, zéros à 0, 2, 4, 6… s ⇒ **T = 4 s** (u > 0 sur ]0;2[, u < 0 sur ]2;4[). Tableau à remplir pour [0;4s], [4;8s], [8;12s] : ⚠ **Énoncé défectueux** : chaque intervalle couvre une période entière, donc chaque DEL est allumée la moitié de l'intervalle et éteinte l'autre moitié — le tableau ne peut contenir ni « منير » ni « منطفئ » seuls (intervalles de 2 s attendus). De plus la polarité du générateur (quel pôle est à u > 0) n'est pas indiquée, donc on ne peut pas attribuer D1/D2 à l'alternance positive sans convention.
- **تمرين 9 (p. 40)** : oscillogramme (écran 12 div × 10 div), boutons : balayage sur **0,2 ms/div** ; sensibilité : l'aiguille pointe entre « 500 » et « 200 » mV, plus près de **200 mV/div** (lecture incertaine). 1) bouton de sensibilité verticale ; crête ≈ 4,2 div ⇒ Um ≈ 0,84 V (≈ 2,1 V si 500 mV/div). 2) période ≈ 3,4 div ⇒ T ≈ 0,68 ms ⇒ N ≈ 1,47 kHz. 3) voltmètre : U = Um/√2 ≈ 0,59 V (hypothèse 200 mV/div). ⚠ **Lectures non entières** (4,2 div, 3,4 div) et aiguille ambiguë : exercice non exploitable tel quel sans zoom ; aucune réponse imprimée.
- **تمرين 10 (p. 41)** : face avant complète, voie A. Écran 14 div × 12 div ; sinusoïde crête ≈ 3 div, période ≈ 6,7 div. Balayage **0,2 ms/div** ; sensibilité voie A : aiguille vers la graduation imprimée « 20 » en haut à droite (entre « 50 » et « 100 ») — étiquettes tronquées (probablement 200 mV/div). Réponses (hypothèse 200 mV/div) : 1) variable (sinusoïde) ; 2) alternative sinusoïdale ; 3) 0,2 ms/div ; ~200 mV/div ; 4) Um ≈ 3 div → **0,6 V** ; T ≈ 6,7 div → **1,34 ms** ; 5) N ≈ 750 Hz ; 6) U = 0,6/√2 ≈ **0,42 V**, mesurée au **فولتمتر**. ⚠ Graduations du bouton de sensibilité illisibles/tronquées (« 50, 20, 100, 50, 20 mV ») ; période non entière.
- **أستغلّ وثيقة « التوتّرات المتناوبة والطب » (p. 42)** : ECG d'un adulte (شكل 1, échelle 0,32 mV ↑ / 0,4 s →), points A (oreillettes), BCDE (ventricules) ; شكل 2 cœur (أذينة يمنى/يسرى، بطين أيمن/أيسر). Texte : fréquence cardiaque Nc (« عدد نبضات القلب في الدقيقة ») variable avec âge, activité, état psychique, ions (كالسيوم، بوتسيوم، صوديوم), fièvre ; « فيتراوح بين 140 و160 بالنسبة إلى الجنين ويصل إلى 70 بالنسبة إلى كهل له من العمر 45 سنة » ; « بين 64 و72 بالنسبة إلى كهل وبين 72 و80 بالنسبة إلى امرأة في نفس السنّ ». Questions : 1) montrer que la tension est « متغيّر ومتناوب غير جيبي » ; 2) déterminer N puis Nc ; 3) Um ; 4) après effort, « N’c = (220 − عدد سنين عمرك) ».
  - Recalcul (lecture de la figure) : un grand carreau ≈ longueur de chaque flèche d'échelle ; intervalle C–C ≈ 4,2 carreaux (et inégal : ≈ 4,5 puis 3,9) ⇒ T ≈ 1,7 s ⇒ N ≈ 0,6 Hz ⇒ Nc ≈ 36 battements/min. ⚠ **Incohérence** avec le texte (≈ 70/min pour un adulte de 45 ans) : l'échelle 0,4 s par grand carreau est probablement fausse (0,2 s donnerait ≈ 72/min). Crête C ≈ 3 carreaux × 0,32 mV ≈ **0,96 ≈ 1 mV**. Pour 14 ans : N’c = 220 − 14 = **206 /min**. ⚠ « متناوب » discutable : l'ECG est surtout positif (seuls B, D légèrement négatifs).

### Bornes
- ✅ Période T (s), fréquence N (Hz et multiples kHz, MHz, GHz), N = 1/T ; valeur maximale Um (oscilloscope, −Um ≤ u ≤ +Um), valeurs efficaces U et I définies par l'équivalence d'éclat d'une lampe avec le continu ; Um = U√2, Im = I√2 ; voltmètre/ampèremètre en ~ mesurent les valeurs efficaces ; secteur tunisien 220 V – 50 Hz ; lecture d'oscillogrammes (div, s/div, V/div).
- ⛔ Aucune expression mathématique u(t) = Um sin(…) ; le mot « amplitude » n'est pas utilisé (seulement « القيمة القصوى ») ; pas de valeur crête-à-crête nommée (seulement « 2×17V »).
- ⛔ Im = I√2 énoncé sans mesure (« يمكن أن أبيّن ») ; aucune mesure numérique d'intensité.
- ⛔ Pas de puissance (W) malgré la plaque « 20W » ; le transformateur (المحوّل 220V-110V) est seulement évoqué en question d'ouverture, pas expliqué.
- ⛔ Pas de notion de phase, ni de pulsation ω.

### Vocabulaire officiel
الدورة (T) ؛ التردّد (N) ؛ الهرتز (Hz) ؛ الكيلوهرتز، الميغاهرتز، الجيغاهرتز ؛ مقدار فيزيائي دوريّ ؛ مقطع أصغر ؛ القيمة القصوى (Um, Im) ؛ القيمة الدنيا ؛ القيمة الفعّالة / التوتّر الفعّال (U) / الشدّة الفعّالة (I) ؛ المحوّل ؛ المسح (s/div) ؛ الحساسيّة العموديّة (V/div) ؛ تدريجة ؛ رسم تذبذبي ؛ مخطّط القلب الكهربائي ؛ أذينة، بطين ؛ تردّد النبض (Nc).

### Leçon 04 — « الكهرباء المنزليّة » (ص 44–54 ; ouverture du باب p. 43)

- **محور** : الكهرمغناطيس — **باب** : الكهرباء المنزليّة (leçon unique du باب). Type de séance (خريطة p. 4) : icône « livre/documentaire » (≠ expérimentation) — la leçon repose surtout sur la recherche documentaire (« أبحث وأتأكّد »).
- p. 43 (ouverture du باب) : « 4- الكهرباء المنزليّة » ; photo « … من الاستعمالات المتعدّدة للكهرباء المنزليّة » ; قادح : « ما هي خاصيّة التركيب المنزلي الّتي يمكن بفضلها التحكّم في تشغيل أيّ جهاز كهربائي أو إلكتروني دون التأثير على باقي الأجهزة المشتغلة ؟ »
- Structure : § طبيعة الكهرباء المنزلية وخصائصها (p. 44–45) ; § مخاطر الكهرباء المنزليّة وأساليب الوقاية منها (p. 46–48) ; الخلاصة (p. 49) ; أتمرّن على حلّ المسائل (p. 50–51, تمارين 1–4) ; أستغلّ وثيقة (p. 51–52) ; أتسلّى (p. 53, كلمات متقاطعة) ; أستعين بعناوين (p. 54, fin du باب التيّار المتغيّر + الكهرباء المنزليّة).

### Objectifs (خريطة الكتاب p. 4)
- « ذكر بعض الخصائص الكهرباء المنزليّة. » (sic)
- « ذكر بعض استعمالات الكهرباء المنزليّة. »
- « ذكر أخطار الكهرباء المنزليّة. »
- « وصف أساليب الوقاية من أخطار الكهرباء المنزليّة. »

### Déroulé
**§ طبيعة الكهرباء المنزلية وخصائصها (p. 44–45)**
- أتأمّل وأتساءل : façade du compteur (شكل 1 : « SOCIETE INDUSTRIELLE D'APPAREILLAGES ET DE MATERIELS ELECTRIQUES — GROMBALIA (TUNISIE) », KWh 71278, « PROPRIETE' STEG », « COMPTEUR MONOPHASE 2 FILS TYPE E76C C=1,666 Wh/tr I=10-40 A F=50 Hz U=127-220 V N° 43662023 Année 2005 », Ph/N SECTEUR/ABONNE). On y lit « 127V-220V، 50Hz و 10A-40A » ; sur le disjoncteur voisin seulement « 10A أو 20A مثلا ». Donc secteur alternatif 50 Hz, compteur utilisable avec 127 V ou 220 V efficaces. Questions : sens de « 10A-40A » ? pourquoi 10 A ou 20 A sur le فاصل ? (sans réponse explicite imprimée ; cf. le 3e أستنتج p. 45).
- أبحث وأتأكّد : indépendance des appareils, commande par interrupteur propre, marquage 220V ⇒ « تركيب تلك الأجهزة بالتوازي بين طرفي القطاع أي أنّ الشبكة المنزلية هي عبارة عن مضاعَفة لمنشَب القطاع 220V في مختلَف أركان المحلّ » (شكل 2 : عدّاد كهربائي منزلي → فاصل → شبكة كهربائيّة منزليّة). « أمّا العدّاد الكهربائي المنزلي فهو جهاز خاصّ بقيس الطّاقة الكهربائيّة المستهلكة. »
- أجرّب وألاحظ (p. 45) : simulation d'un réseau domestique (شكل 3 : « غرفة1 », « مطبخ », « غرفة2 ») — جهاز تغذية بتوتّر متناوب جيبيّ (6V) ؛ ثلاثة مصابيح 6V ؛ محرّك 6V (~) ؛ منشب توتّر 6V ؛ أربعة عُلب تحويل (3 أغماد حمراء + 3 زرقاء) ؛ أمبيرمتر ؛ خمسة قواطع (أو أربعة) ؛ أسلاك حمراء وزرقاء. Interrupteur général K, branches K1…K4 d'intensités I1…I4, ampèremètre sur la ligne principale (I). Observation : « كلّما ازداد عدد الأجهزة المشتغلة سجّل الأمبيرمتر شدّة فعّالة I أكبر. » (aucune valeur numérique ; loi des nœuds I = I1+I2+I3+I4 non écrite).

**§ مخاطر الكهرباء المنزليّة وأساليب الوقاية منها (p. 46–48)**
- أتأمّل وأتساءل : questions sur les risques ; fils de couleurs différentes (prise شكل 4) ; « لماذا تزوّد المناشب الخاصّة بالآلات الكهربائية كالثلاّجة أو الغسّالة بمأخَذ ثالث ذكر ؟ (الشكل5) » ; décharge au toucher de la carcasse ; rôle du « الفاصل », des « الفواصل والفاصل التفاضلي على لوحة التوزيع(الشكل6) » ; prise de salle de bain à couvercle plastique ; ne pas toucher avec des mains mouillées.
- أبحث وأتأكّد : contacter un technicien STEG, recherche documentaire (livres, revues, Internet).

### Encadrés (VERBATIM)
- **أستنتج (p. 45)** :
  - « التوتّر الكهربائي المنزلي توتّر متناوب جيبي ذو تردّد 50 Hz وذو قيمة فعّالة 220V »
  - « الشبكات الكهربائية المنزلية مصمّمة بطريقة تجعل كلّ الأجهزة المستعمَلة مركّبة بالتوازي وكلّ واحد منها مغذّى بتوتّر القطاع 220V فعّال. »
  - « ترتفع الشدّة الفعّالة للتيّار الكهربائي الرئيسي في شبكة منزليّة مع عدد الأجهزة الكهربائيّة المشتغلة في نفس الوقت إلاّ أنّ هذا العدد يبقى محدودا لأنّ قيمة الشدّة الفعّالة المسموح بها يجب أن لا تتعدّى القيمةَ المسجّلة على العدّاد. »
- **أستنتج (p. 47–48)** :
  - « يُنقَل التيّار الكهربائيّ من محطّة التوليد إلى الحضَر عبر خطوط يتكوّن الواحد منها من سلكيْن، سلك الطور وسلك موصَل بالأرض يُسمَّى السلكَ المحايدَ.(الشكل7) »
  - « يحفظ القطاع الكهربائيّ المنزليّ توتّرا فعّالا ذا قيمة تساوي 220V بين كلّ من طرف سلك الطور وطرف السلك المحايد. »
  - « للتمييز بين أسلاك الطور والأسلاك المحايدة يختار الفنّيون عند التركيب اللونَ الأزرقَ للأسلاك المحايدة واللون الأحمر لأسلاك الطور. »
  - « لتبيُّن مأخذ(أو ثقْب) المنشب الموصل بطرف سلك الطور يستعمل الفنّي مفكّ لَوالبَ مخبارًا (الشكل8) : كلّما كان المفكّ في الطور يشعّ مصباحه. »
  - « مخاطر الكهرباء المنزلي نوعان، مخاطرٌ على الأشخاص وأخرى على التجهيزات المنزليّة : »
  - « * عندما يلمس شخصٌ ما آلة كهربائيّة فيها خلل يتمثّل في عدم عزل هيكلها المعدني عن سلك الطور يتعرّض إلى هزّة كهربائيّة (الشكل9) يمكن أن تصل به إلى حدّ الصعق وذلك بسبب مرور التيّار الكهربائي عبر جسمه من سلك الطور إلى الأرض. لتفادي ذلك وجب تزويد المناشب الخاصّة بالآلات الكهربائيّة بمآخذ ثالث ذَكَر (الشكل5) يوصلُ بسلكٍ مزدوج اللون (أصفر– أخضر) يُسمّى سلكَ التأريض (الشكل10) لأنّ طرَفه الثاني موصل بقضيب نحاسي طول 1,20m (الشكل11) يُدقّ في الأرض بعيدا عن كلّ قناة منزليّة تحتيّة. » (sic « بمآخذ ثالث »)
  - « * تتمثل المخاطر على التجهيزات المنزليّة في احتمال اندلاع الحرائق نتيجةَ: – دارةٍ مقصورة تحصل إثرَ تلامس عرَضيٍّ لسلك الطور بالسلك المحايد. – بلوغ الشدّة الفعّالة للتيّار قيمةً مرتفعةً لا تحتملها الشبكةُ المنزليّة سواء في التفريعات (في حالة استعمال نفس المنشب لتشغيل عدّة أجهزة في نفس الوقت) أو في جزئها الرئيسي (من جهة العدّاد). »
  - « لحماية التجهيزات تُركَز فواصلُ في الشبكة : * فاصل رئيسي(الشكل12) يُركّز مع العدّاد الكهربائي من قبل المُزوّد (الشركة التونسيّة للكهرباء والغاز)، لازم للحماية من كلّ خطر يمكن أن ينجم عن دارة مقصورة أو إثر تشغيل عدد كبير من الأجهزة الكهربائيّة في نفس الوقت بالإضافة إلى دوره كقاطعٍ عامٍّ للتيّار الكهربائي. * فواصل أخرى خاصّة بكلّ تفريعات الشبكة تُركز على لوحة التوزيع كما في الشكل6 ص 46. »
  - « لضمان أكثر حماية للأشخاص والتجهيزات المنزليّة يُحبّذ تركيز فاصل تفاضلي في الجزء الرئيسي للشبكة (الفاصل الموجود على أقصى اليسار في الشكل6 والمرسوم في الشكل 10.b) : يلعب دورَ القاطع الآلي الذي يكشف عن التيّارات الكهربائيّة المتسرّبة والتي تفوق شدّتها 30 mA إثر مرورها عبر السلك الأرضي عوضًا عن السلك المحايد. »
  - Figures : شكل 10.a — prise : 220 V entre phase et neutre, 220 V entre phase et terre, « 0 V » entre neutre et terre ; شكل 12 — disjoncteur « SIAME C32a » (plaques 10/10).
- **الخلاصة (p. 49)** :
  - « الشبكة الكهربائية المنزليّة مصمَّمة لتركيب الأجهزة بالتوازي بين طرَفَيْ توتّر القطاع. »
  - « سلك الطور والسلك المحايد أساسيّان في كلّ تركيب كهربائيّ منزليّ ويحفظ القطاع بينهما توتّرا متناوبا جيبيّا 220V فعّال في بلادنا. أمّا سلك التأريض والفواصل وغيرها من متمّمات التركيب المنزليّ فهي لازمة لوظيفتها الوقائيّة. »
  - « للكهرباء المنزليّة منافعُ متنوّعة ومتعدّدة ولكنَّ في استغلالها مخاطرُ لابدّ من احترام قواعد السلامة الخاصّة بها لتفاديها. »
- Grandeurs/symboles : 220 V, 50 Hz, 127 V, 10A-40A, 10 A/20 A/32 A, 30 mA, 1,20 m, kWh (compteur), Wh/tr.

### Exercices
- **أقيّم مكتسباتي (p. 48)** : appareils à fiche à 3 bornes (2 mâles + 1 femelle) pour prise de sécurité à 3e broche mâle. 1) nature de la carcasse → **métallique** (conductrice) ; 2) la borne femelle doit être reliée, via le cordon, **à la carcasse métallique** (liaison à la terre : en cas de défaut, le courant de fuite passe par le fil de terre et non par la personne ; déclenchement du différentiel).
- **تمرين 1 (trous, p. 50)** — mots : أحمر – أصفر – أزرق – ضروريّ – سلك التأريض – الفاصل – موصّلة – الشبكة – عناصر الشبكة. Reconstitution : « للتعرّف إلى **عناصر الشبكة** الكهربائيّة المنزليّة يستعمل الفنّيون في التركيب أسلاكا **موصّلة** ذات غلاف **أحمر** للطور وذات غلاف **أزرق** للمحايد، أمّا بالنسبة إلى **سلك التأريض** فيلتجؤون إلى استعمال أسلاك ذات غلاف مخطَّط بالـ**أصفر** وبالأخضر. » ; « زيادةً على **الفاصل** الرئيسيّ المصاحب للعدّاد الفاصلُ التفاضليّ **ضروريّ** كذلك لأنّه يحمي **الشبكة** الكهربائية المنزلية ومستعمِليها من كلّ خطر. »
- **تمرين 2 (cases, p. 50)** :
  1. « لا يوجد توتّر بين السلك المحايد وسلك التأريض » → vrai (شكل 10.a : 0 V) ; « تُركّب الأجهزة… بالتسلسل » → faux ; « احتمال الصعق الكهربائيّ وارد في المنزل رغم تركيب فاصل تفاضليّ » → vrai (le différentiel limite, n'annule pas le risque — ⚠ non dit explicitement dans le cours).
  2. Contact carcasse métallique d'une machine à laver / phase, installation avec différentiel : « يُقطَع التيّار بسبب تكوّن دارة مقصورة » → faux ; « يصاب الشخص… بصعق » → faux (attendu) ; « لا يحمي الفاصلُ الشخصَ… إلاّ مع وجود سلك التأريض » → **vrai** (attendu) ; « يحمي الفاصلُ… من كلّ خطر » → faux. ⚠ Ambigu : un différentiel 30 mA détecte aussi une fuite passant par la personne ; la réponse attendue repose sur le cours (fuite « عبر السلك الأرضي »).
  3. Changer une ampoule sans ouvrir le disjoncteur, sur escabeau en bois, réseau sans différentiel, en touchant les deux plots de la douille (contact phase–neutre) : « لن تُصابَ بأيّ سوء لأنّ السلم يعزلك عن الأرض » → faux ; « لن تُصابَ… لأنّ في لمسك للغمد تكوّن دارة مقصورة ينتج عنها انقطاع التيّار » → faux ; « أنتَ معرّض إلى خطر الصعق لأنّ التيار الكهربائي سيمرّ عبر جسمِك » → **vrai**.
- **تمرين 3 (p. 51)** : schéma : 220 V ; interrupteur bipolaire général ; lampe avec « قاطع » ; fusibles/disjoncteurs 10A, 10A, 32A (« صهيرة » désigne le 32A) ; prise 10A avec terre ; prise 32A du réfrigérateur **sans fil de terre**.
  1. L'interrupteur de la lampe est placé sur le **fil neutre (bleu)** ; la lampe reste reliée à la phase même éteinte → il doit couper la phase.
  2. Non : la prise du réfrigérateur n'est pas reliée à la terre (carcasse métallique non mise à la terre).
  3. Four de 12 A sur la prise libre protégée par 10 A → **12 A > 10 A** : la protection (صهيرة/فاصل 10 A) coupe le circuit (fusion / déclenchement).
- **تمرين 4 (p. 51)** : réparer la lampe de chevet après avoir ouvert l'interrupteur ; léger fourmillement en touchant un fil. 1) défaut : l'interrupteur coupe le neutre et non la phase ; 2) précaution : couper le disjoncteur (ou débrancher) / vérifier au tournevis testeur ; 3) les interrupteurs modernes sont **bipolaires** (coupent phase et neutre) pour garantir la coupure de la phase quel que soit le sens de branchement de la fiche. (réponses déduites, non imprimées)
- **أستغلّ وثيقة (p. 51–52, « المؤلفون »)** : usages de l'électricité (éclairage, appareils, industrie, agriculture irriguée) ; appel à la consommation rationnelle (« الاستهلاك بترشّد ») ; danger d'électrocution — données : « جسم الإنسان ليس بالناقل الجيّد… فهو قادر إذا مسَكَ صاحبه طرفَيْ سلكَيْن يحفظان بينهما 25 V على نقل تيّار يمكن أن تبلغ شدّته 25 mA إذا كان مبلّلاً، إلاّ أنّه لا يحتمل إلاّ التيّار الذي لا تتعدّى قيمةُ شدّتِه 5 mA » ; « بين 10 mA و20 mA يشعر المتأثّر به بتنمّل في جسمه وحتّى بتشنّج في العضلات » ; « بين 25 mA و30 mA يؤدّي إلى إحداث تقبُّضاتٍ تكرّزية في عضلات التنفّس فيبدو الذي تلقّى الصّعقَ وكأنّه ميّت » ; « 50 mA … الموت الحقيقيّ للمصابِ بتوقّف القلب عن النّبض أكثرَ من أربعة دقائق » (sic « أربعة دقائق ») ; secours : 1. isoler la victime (couper le courant, ne pas la toucher) ; 2. « الاستنجادُ هاتفيّا بالحماية المدنيّة ( ☎198) » ; 3. respiration artificielle bouche-à-bouche / massage cardiaque externe par un secouriste. Questions : 1) domaines d'usage ; 2) usage pour l'irrigation (pompage) ; 3) consommation rationnelle ; 4) « لماذا يُعتمَد في المخبر تحويل توتّر القطاع من 220V فعّال إلى12V فعّال أو أقلَّ ولا أكثرَ؟ » ; 5) autres dangers. Recalcul Q4 (déductible du texte) : R ≈ 25 V / 25 mA = 1000 Ω (corps mouillé) ⇒ sous 12 V : I ≈ 12 mA (seuil de tétanisation non atteint) ; sous 220 V : I ≈ 220 mA ≫ 50 mA (mortel). ⚠ La résistance du corps (U/I) n'est pas calculée dans le manuel ; incohérence interne : 12 mA dépasse les « 5 mA » supportables cités.
- **أتسلّى (p. 53)** : mots croisés — définitions : 1 « صفة لتوتّر متغيّر » (→ متناوب) ; 2 « غير مستمرّ » (→ متغيّر) ; 3 « وحدة قيس التردّد » (→ هرتز) ; 4 « صفة لتيّار القطاع » (→ جيبي/متناوب) ; 5 « مدّة زمنيّة يتميّز بها التوتّر الجيبي » (→ دورة) ; 6 « قاطع آلي للتيّار الكهربائي » (→ فاصل) ; 7 « عكس الدورة » (→ تردّد) ; 8 « صفة لقيمة توتّر جيبي تقاس بالفولتمتر » (→ فعّال). « من هو صاحب الصورة؟ » : physicien allemand né à Hambourg en 1857, mort à Bonn en 1894 → **هرتز** (Heinrich Hertz) ; cases IV-II-I-III. (réponses non imprimées ; la longueur des cases n'a pas été vérifiée une à une)
- **أستعين بعناوين (p. 54)** : liste de sites (ac-strasbourg, physiquecollege.free.fr, www.dspt.club.fr, www.steg.com.tn, etc.) pour « التيّار الكهربائي المتغيّر، المتناوب والمتناوب الجيبي، الكهرباء المنزليّة ».

### Bornes
- ✅ Secteur 220 V efficace, 50 Hz ; montage en parallèle des appareils ; intensité principale croissant avec le nombre d'appareils, limitée par la valeur du compteur/disjoncteur ; phase (rouge), neutre (bleu, relié à la terre), terre (vert-jaune, piquet cuivre 1,20 m) ; tournevis testeur ; dangers pour personnes (électrisation, électrocution) et équipements (court-circuit, surintensité → incendie) ; disjoncteur principal, disjoncteurs divisionnaires, différentiel 30 mA ; seuils physiologiques (5, 10–20, 25–30, 50 mA) ; gestes de secours (198).
- ✅ Compteur = mesure de « الطّاقة الكهربائيّة المستهلكة » (kWh sur la photo).
- ⛔ Aucune formule de puissance ou d'énergie (P = U·I, E = P·t absentes) ; la constante C = 1,666 Wh/tr n'est pas exploitée.
- ⛔ Aucune valeur numérique dans l'expérience de simulation (6 V) ; loi des nœuds non écrite explicitement.
- ⛔ Le transformateur 220 V → 12 V est évoqué (Q4 document) sans explication de son fonctionnement.
- ⛔ Le « fusible » (صهيرة) n'apparaît que dans la figure de l'exercice 3, jamais défini dans le cours.

### Vocabulaire officiel
الكهرباء المنزليّة ؛ القطاع (توتّر القطاع) ؛ الشبكة الكهربائيّة المنزليّة ؛ العدّاد الكهربائي المنزلي ؛ الفاصل (الرئيسي) ؛ الفاصل التفاضلي ؛ لوحة التوزيع ؛ التفريعات ؛ منشب / مأخذ (ثقب) / مأخذ ثالث ذكر ؛ سلك الطور ؛ السلك المحايد ؛ سلك التأريض ؛ قضيب نحاسي ؛ مفكّ لوالب مخبار ؛ هزّة كهربائيّة ؛ الصعق ؛ دارة مقصورة ؛ التيّارات المتسرّبة ؛ القاطع الآلي ؛ صهيرة ؛ علبة تحويل ؛ الحماية المدنيّة (198) ؛ تنفّس اصطناعي ؛ تدليك خارجي للقلب.

### Leçon 05 — « التكهرب بالاحتكاك » (ص 56–58)

- **محور** : الكهرمغناطيس — **باب** : الكهرباء السّاكنة (ouverture du باب p. 55 : « 5- التكهرب بالاحتكاك / 6- التكهرب بالتماس / 7- الشحنة الكهربائيّة » ; photo « السّماء عندما يشقّها البرق… » ; قوادح : « بم تفسّر القشعريرة التي يشعر بها كلّ من يقرّب ظهر يده من شاشة جهاز التلفزة ؟ » ; « بعد توقّف السيّارة يشعر السائق أحيانا برجّة خفيفة عند لمسها من الخارج بمناسبة غلق بابها. بم يُفسّر ذلك ؟ » ; « البرق، الرعد والصاعقة … متى وأين ؟ ما هي مصادرها ؟ »).
- Type de séance (خريطة p. 4) : icône « livre/documentaire » (bien que la leçon soit expérimentale).
- Sections : ظاهرة التكهرب (p. 56–57) ; المكشاف الكهربائي (p. 57–58). Pas de الخلاصة ni d'exercices « أتمرّن » propres (seulement deux « أقيّم مكتسباتي »).

### Objectifs (خريطة الكتاب p. 4)
- « كهربة جسم بالاحتكاك. »

### Déroulé
**§ ظاهرة التكهرب (p. 56–57)**
- أتأمّل وأتساءل : « ما سبب الطقطقة الخفيفة التي تُسمع عند تسريح الشعر الجاف بمشط، عند فصل ورقتين شفّافتين عن بعضهما…؟ » ; « بمَ أفسّر الاحساس بوخز خفيف عند خلع صدرة من النيلون ؟ »
- أجرّب وألاحظ : matériel — « قضيب من الإبونيت (مطاط صلد مُعالج بالكبريت) » ; قضيب من الزجاج ; قطعة من الفراء ; قطعة من الحرير ; « نواس كهربائي: جهاز متكوّن من كويرة صغيرة من لبّ البَيْلسان عُلّقت بخيط دقيق من الحرير (الشكل1) ».
  - Ébonite non frottée approchée de la boule : rien (شكل 2a) ; frottée à la fourrure puis approchée : « الطرف المُدلّك يجذب الكويرة » (شكل 2b).
  - Même expérience avec verre frotté à la soie (شكل 3a, 3b) : attraction.
- أحلّل وأفسّر : les deux bâtons frottés acquièrent la propriété d'attirer les corps légers du côté frotté ⇒ « الطرف المدلّك قد تكهرب أي أصبح يحمل كمّية من الكهرباء » ; « وبما أنّ التكهرب حصْرٌ على الجزء المحكوك تنعت الكهرباء المتمركزة على طرف القضيب المدلّك بالكهرباء الساكنة. »
- ملاحظة : « ترجع تسميّة النواس المستعمَل في التجربة السابقة بالنواس الكهربائي إلى خاصيّة تأثّره بالكهرباء. »

**§ المكشاف الكهربائي (p. 57–58)**
- أتأمّل وأتساءل : « هل النواس الكهربائي هو الأداة الوحيدة المستعملة في المخبر للكشف عن ظاهرة التكهرب ؟ »
- أجرّب وألاحظ : « مكشاف كهربائي وهو جهاز متكوّن من قفص له وجهان من الزجاج الشفّاف ويخترق سطحه ساق معدنيّة عبر سدّاد من المطّاط ثُبّتت عليها قرص معدنيّ وشُدّ إلى نصفها الأسفل ورقة معدنيّة قابلة للحركة. (الشكل5) ». Approche du bout frotté (verre ou ébonite) du disque : « الورقة المعدنيّة تبتعد عن ساق المكشاف » (شكل 6). ملاحظة : « تعود الورقة المعدنيّة إلى وضعها الأصليّ عند إبعاد الطرف المكهرب للقضيب. »
- Aucune donnée chiffrée dans la leçon.

### Encadrés (VERBATIM)
- **أستنتج (p. 57)** :
  - « بتأثير الاحتكاك تصير الموادّ قادرة على جذب الأجسام الخفيفة : إنّها ظاهرة التكهرب. »
  - « يحمل كلّ جسم متكهرب كمّية من الكهرباء الساكنة. »
  - « النوّاس الكهربائي أداة كاشفة لظاهرة التكهرب. »
- **أستنتج (p. 58)** : « المكشاف الكهربائي جهاز يُستخدم في المخبر للكشف عن ظاهرة التكهرب. »

### Exercices
- **أقيّم مكتسباتي (p. 57)** : frotter l'ébonite avec la fourrure puis approcher **la fourrure** (côté frotté) du pendule : la boule subit le même effet qu'avec le bâton (attraction, شكل 4). « بمَ أفسّر ذلك ؟ » → la fourrure s'est elle aussi électrisée par frottement (les deux corps frottés s'électrisent). (Le fait que la fourrure porte l'électricité de signe opposé n'est pas abordé ici — cf. L07.)
- **أقيّم مكتسباتي (p. 58)** : bâton de cuivre frotté par un bout avec un tissu puis approché du disque : la feuille ne bouge pas, sauf si le bâton est tenu par un manche en verre (شكل 7).
  1. Montrer que l'absence d'effet quand on le tient à la main ne nie pas son électrisation ; expliquer : le cuivre est conducteur, l'électricité acquise s'écoule par la main/le corps (vers la terre) ; isolé par le manche en verre, il la conserve.
  2. « هل يمكن أن أثبت بهذه التجربة أنّ كلّ الأجسام الصلبة قابلة للتكهرب بالاحتكاك ؟ » → non, on ne peut pas généraliser à partir de trois matériaux (ébonite, verre, cuivre) — ⚠ question ouverte ; la réponse attendue n'est pas imprimée (on peut aussi comprendre « oui, isolants et conducteurs isolés s'électrisent »). Ambigu.
  - ⚠ Les notions « ناقل / عازل » en électrostatique ne sont pas formulées dans la leçon ; l'élève doit les mobiliser (مكتسبات p. 13 : « أميّز بين ناقل وعازل »).

### Bornes
- ✅ Électrisation par frottement (ébonite/fourrure, verre/soie) ; électricité statique localisée sur la partie frottée ; pendule électrique et électroscope (مكشاف) comme détecteurs.
- ⛔ Pas de notion de charge positive/négative, ni d'attraction/répulsion entre corps chargés, ni d'électrons dans cette leçon (renvoyés à L07) ; l'expression « كمّية من الكهرباء » est employée, pas encore « شحنة ».
- ⛔ Pas d'explication du fonctionnement de l'électroscope (pourquoi la feuille s'écarte) ; pas de grandeur ni d'unité (coulomb absent).
- ⛔ Les questions d'ouverture (TV, voiture, foudre) ne reçoivent pas de réponse dans la leçon.

### Vocabulaire officiel
ظاهرة التكهرب ؛ التكهرب بالاحتكاك ؛ متكهرب ؛ الكهرباء الساكنة ؛ كمّية من الكهرباء ؛ الإبونيت (مطاط صلد معالج بالكبريت) ؛ الزجاج ؛ الفراء ؛ الحرير ؛ القماش ؛ النواس الكهربائي ؛ كويرة من لبّ البيلسان ؛ خيط من الحرير ; المكشاف الكهربائي ؛ قرص معدنيّ ؛ ساق معدنيّة ؛ ورقة معدنيّة ؛ سدّاد من المطّاط ؛ مقبض زجاجي ؛ الطرف المدلّك.

### Leçon 06 — « التكهرب بالتماس » (ص 59–61)

- **محور** : الكهرمغناطيس — **باب** : الكهرباء السّاكنة. Type de séance (خريطة p. 4) : pas d'icône propre (ligne fusionnée avec la leçon 5, icône « livre/documentaire »). Leçon très courte : un seul أستنتج, un seul أقيّم مكتسباتي, pas de الخلاصة ni d'exercices.

### Objectifs (خريطة الكتاب p. 4)
- « كهربة جسم بالتماس. »

### Déroulé (§ ظاهرة التكهرب بالتماس)
- أتأمّل وأتساءل (p. 59) : « هل لا يحصل التكهرب إلاّ بالاحتكاك ؟ » ; « بمَ أفسّر شعوري برجّة خفيفة عند لمس شاشة التلفاز عَرَضا مباشرة إثر إيقاف تشغيله ؟ »
- **تجربة عدد1 (p. 59–60)** : matériel — قضيب من الإبونيت أو البلكسيقلاص ؛ قضيب من الزجاج ؛ قطعة من الفراء ؛ قطعة من الحرير ؛ نواسان كهربائيّان اثنان.
  - Deux pendules A et B rapprochés doucement : aucune interaction (شكل 1a).
  - On électrise l'ébonite (ou plexiglas) par frottement, on l'approche jusqu'au contact de la boule A (B à l'écart), on retire le bâton, puis on rapproche les pendules : A et B s'attirent (شكل 1b, boules accolées).
  - Même chose avec le verre (شكل 2a, 2b).
- **« تجربة عدد1 » (sic — seconde expérience, p. 60 ; ⚠ numérotation erronée : devrait être « عدد2 »)** : matériel — قضيبان من الإبونيت أو البلكسيقلاص ؛ قضيبان من الزجاج ؛ فراء ؛ حرير ؛ مكشاف كهربائي.
  - Électriser un bâton par frottement ; vérifier l'écartement de la feuille (شكل 3). Puis toucher avec le bout frotté un bout du second bâton de même matière.
  - Réapprocher le 1er bâton : la feuille s'écarte « ثانية ولكن بأقلّ حدّة » (شكل 4) ; approcher le 2e bâton (au bout touché) : la feuille s'écarte aussi.
  - Refaire avec les deux bâtons de verre.
- أحلّل وأفسّر (p. 60) : « في التجربة الأولى، جذب الكويرة A للكويرة B دليل على تكهرب الكويرة A نتيجة لمسها للطرف المدلّك للقضيب المكهرب بالاحتكاك. » ; « في التجربة الثانية، عند لمس القضيب المكهرب بالاحتكاك للقضيب الثاني يتكهرب هذا الأخير باكتسابه جزءا من كمّية الكهرباء المتمركزة على الطرف المدلّك للقضيب الأوّل وهذا ما يفسّر النقص في مدى تأثيره على الورقة المعدنيّة عند تقريبه من قرص المكشاف الكهربائي في المرّة الثانية. »
- Aucune donnée chiffrée.

### Encadrés (VERBATIM)
- **أستنتج (p. 61)** : « بالإضافة إلى التكهرب بالإحتكاك يُمكن لجسم ما أن يتكهرب بالتماس. »
- Aucun encadré-définition, aucune formule, aucun symbole ni unité.

### Exercices
- **أقيّم مكتسباتي (p. 61)** : « بعد توقف السيّارة يشعر السائق أحيانا برجّة خفيفة عند لمسها من الخارج مناسبة غلق بابها. بم يُفسّر ذلك ؟ » (sic « مناسبة » pour « بمناسبة ») → la carrosserie (et/ou le conducteur) s'est électrisée par frottement (air, sièges) pendant le trajet ; au contact, une partie de l'électricité passe par le corps du conducteur (électrisation par contact / décharge). Réponse non imprimée ; c'est la même question que l'ouverture du باب p. 55.

### Bornes
- ✅ Électrisation par contact : un corps neutre touché par un corps électrisé s'électrise en prenant une partie de sa quantité d'électricité ; le corps source perd donc de son effet (feuille de l'électroscope moins écartée).
- ⛔ Le signe de l'électricité acquise (même signe que la source) n'est pas dit ici ; pas de répulsion observée (seule l'attraction A–B est montrée), pas de charges +/−, pas d'électrons (renvoyés à L07).
- ⛔ Électrisation par influence (induction) non abordée.
- ⛔ La question d'ouverture sur l'écran de télévision ne reçoit pas de réponse.

### Vocabulaire officiel
التكهرب بالتماس ؛ التكهرب بالاحتكاك ؛ الإبونيت ؛ البلكسيقلاص ; الزجاج ؛ الفراء ؛ الحرير ؛ نواسان كهربائيّان ؛ الكويرة A / B ؛ المكشاف الكهربائي ؛ قرص المكشاف ؛ ساق المكشاف ؛ الورقة المعدنيّة ؛ الطرف المدلّك ؛ كمّية الكهرباء ؛ رجّة خفيفة.

### Leçon 07 — « الشحنة الكهربائيّة » (ص 62–69)

- **محور** : الكهرمغناطيس — **باب** : الكهرباء السّاكنة. Séance « expérimentation » (خريطة p. 4, page de début 62).
- ⚠ **Bornes réelles** : la leçon s'étend de p. 62 à p. 69 (فقرة « هل من مزيد » p. 69). Les p. 70–72 n'en font **pas** partie : p. 70 = ouverture du محور suivant « المادّة في الطبيعة » (أبواب : الذّرة والاحتراق / الرّموز الكيميائيّة / المحاليل الشارديّة) ; p. 71 = مكتسباتي القبليّة de ce محور ; p. 72 = ouverture du باب « الذّرة والاحتراق » (دروس 8 à 12). Il n'y a ni « أتسلّى » ni « أستعين بعناوين » pour le باب الكهرباء الساكنة.
- Sections : أنواع الكهرباء (p. 62–63) ; الشحنة الكهربائيّة (p. 63–65) ; الخلاصة (p. 65) ; أتمرّن على حلّ المسائل (p. 65–67, تمارين 1–6) ; أجرّب بنفسي « أصنع مكشافا كهربائيّا » (p. 68) ; هل من مزيد « الكهرباء الساكنة » (p. 69).

### Objectifs (خريطة الكتاب p. 4)
- « التعرّف إلى الشحنة الكهربائيّة السالبة والشحنة الكهربائيّة الموجبة. »
- « التعرف إلى نوع شحنة كهربائيّة من خلال تأثيرها على شحنة أخرى معروفة. »

### Déroulé
**§ أنواع الكهرباء (p. 62–63)**
- أتأمّل وأتساءل : « لماذا لا تُستعمل نفس المادّة لكهربة كلّ من قضيبَيْ الزجاج والابونيت ؟ » ; « كما هو معلوم تتكهرب كويرة نوّاس كهربائي بلمسها لقضيب مكهرب إلاّ أنّها لا تبقى ملتصقة بطرف القضيب بل تندفع مبتعدة عنه. بمَ أفسّر ذلك ؟ »
- أجرّب وألاحظ : matériel — قضيبان اثنان من الإبونيت أو البلكسيقلاص ؛ قضيبان اثنان من الزجاج ؛ قطعة من الفراء وأخرى من الحرير ؛ « حاملان يتكوّن كلّ منهما من ركاب معلّق بخيط رقيق من الحرير. (الشكل1) ».
  - Deux ébonites (ou plexiglas) frottées à la fourrure, posées chacune sur un étrier, bouts frottés en regard : « فيحدث بينهما تنافر في الحين » (شكل 2).
  - Deux verres : même observation (شكل 3, répulsion).
  - Un ébonite/plexiglas et un verre : « فلا يحدث أيّ تنافر بل يتجاذب الطرفان المتكهربان » (شكل 4).
- أحلّل وأفسّر (p. 63) : répulsion de deux bâtons identiques frottés par le même tissu ⇒ même type d'électricité ; attraction ⇒ l'électricité du verre frotté diffère de celle de l'ébonite/plexiglas. « فعلا لقد أثبتت التجارب العلميّة أنّه ينتج عن التكهرب بالاحتكاك ظهور كهرباء إمّا مماثلة للكهرباء المرتبطة بتكهرب الزجاج أو مماثلة للكهرباء المرتبطة بتكهرب الإبونيت. »

**§ الشحنة الكهربائيّة (p. 63–64)**
- أتأمّل وأتساءل : « لماذا يُنعت أحد قطبَيْ العمود الجاف بالقطب الموجب والآخر بالقطب السالب ؟ » ; « لتفادي خطر الصواعق يُثبّت على البناية العالية جهاز يُسمّى دافع الصواعق. ما هو مبدأ اشتغاله ؟ » (⚠ ces deux questions ne reçoivent pas de réponse dans la leçon).
- أجرّب وألاحظ : l'écart du pendule/de la feuille de l'électroscope varie d'un cas à l'autre et croît avec la durée de frottement du verre à la soie ⇒ « أستخلص أنّ كمّيات الكهرباء تختلف من حالة إلى أخرى. »
- أحلّل وأفسّر (p. 64) : « لتفسير الاختلاف المسجّل بين كمّيات الكهرباء أسلّم بأنّ كلّ كمّية الكهرباء التي تظهر على الزجاج بالاحتكاك متكوّنة من كمّيات صغيرة جدّا متطابقة وغير قابلة للتجزئة تسمّى الواحدة منها شحنة كهربائيّة بسيطة يرمز لها بالحرف اللاتيني « e ». بالتالي فإنّ أيّ كمّية كهرباء زجاجيّة هي شحنة كهربائيّة متكوّنة من عدد معيّن n من شحنات كهربائيّة بسيطة يُرمَز لها بالحرف اللاتيني « q » : **q = n.e** » ; « للتمييز بين نَوعَي الكهرباء تنعت الشحنة المجسّمة للكهرباء الزجاجيّة بالشحنة الموجبة (q > 0) والشحنة المجسّمة للكهرباء الراتنجيّة بالشحنة السالبة (q < 0) إذنْ تُكتَب الشحنة الموجبة : **q = + n.e** أمّا الشحنة السالبة فتكتبُ : **q = - n.e** » ; « الشحنة الكهربائيّة قابلة للقيس، وحدة قيسها الكولون ورمزها « C ». » ; « قيمة الشحنة الكهربائيّة البسيطة : **e = + 1,6.10⁻¹⁹ C** »
- ملاحظة (p. 64) : « رغم أنّ الشحنة الكهربائيّة التي نحصل عليها بالتكهرب تحتوي عددا كبيرا من الشحنات الكهربائيّة البسيطة تبقى قيمتها صغيرة وهذا ما يبرّر استعمال بعض قواسم الكولون كوحدات قيس أخرى: * المِكروكولون (µC) : **1µC = 10⁻⁶C** * المِلّيكولون (mC) : **1mC = 10⁻³C** »
- ⚠ Formulation : « أيّ كمّية كهرباء زجاجيّة هي… q = n.e » — l'hypothèse de quantification n'est énoncée que pour l'électricité « vitreuse » avant d'être étendue par signe.

### Encadrés (VERBATIM)
- **أستنتج (p. 63)** : « الكهرباء نوعان: ◄الكهرباء الزجاجيّة وهي من نوع تلك التي تظهر على مادّة الزجاج بالاحتكاك. مثال : مَرْو (بلّور الصخر) مدلّك بالقطن. ◄ الكهرباء الراتنجيّة وهي من نوع تلك التي تظهر على مادّة الراتنج بالاحتكاك. مثال : قضيب إبونيت أو بلكسيقلاص مدلّك بقطعة فراء. ◄ تتنافر كمّيتا كهرباء من نفس النوع بينما تتجاذبان كلّما كانتا من نوعين مختلفين. »
- **أستنتج (p. 64)** :
  - « الشحنة الكهربائيّة مقدار فيزيائي يُجسّم كمّية الكهرباء التي تظهر على جسم مُكهرب. »
  - « الشحنة الكهربائيّة مقدار قابل للقيس، وحدة قيسها الكولون (C) »
  - « الشحنات الكهربائيّة نوعان: الشحنات الموجبة والشحنات السالبة. »
  - « للشحنة الكهربائيّة قيمة مطلقة مضاعفة لقيمة الشحنة الكهربائيّة البسيطة : **|q| = n. e , n ∈ IN\*** »
  - « تتنافر شحنتان كهربائيتان من نفس العلامة بينما تتجاذبان كلّما كانتا من علامتين مختلفتين. »
- **الخلاصة (p. 65)** :
  - « يمكن أن تحدث ظاهرة التكهرب بالاحتكاك او بالتماس. »
  - « الإضافة إلى المكشاف الكهربائي يستخدم النوّاس الكهربائي كأداة كاشفة لظاهرة التكهرب. » (sic « الإضافة » pour « بالإضافة »)
  - « كلّ جسم متكهرب يحمل شحنة كهربائيّة ذات قيمة مطلقة مضاعفة لقيمة الشحنة الكهربائيّة البسيطة : **|q| = n.e , n ∈ IN\*** »
  - « الشحنة الكهربائيّة مقدار فيزيائي قابل للقيس وحدة قيسها الكولون (C) . »
  - « تتجاذب شحنتان كهربائيتان كلّما كانتا من علامتين مختلفتين بينما تتنافر كلّ شحنتين كهربائيتين لهما نفس العلامة. »
- Symboles/unités : q, e, n, n ∈ IN*, |q|, C, µC, mC, e = 1,6.10⁻¹⁹ C, q > 0 / q < 0.

### Exercices (avec recalculs)
- **أقيّم مكتسباتي (p. 63)** : bâton (T) en mica électrisé par frottement ; matériel disponible : ébonite, verre, fourrure, soie, deux étriers. 1) proposer une expérience : électriser le verre à la soie (ou l'ébonite à la fourrure), le poser sur l'étrier, approcher le bout frotté de T : répulsion ⇒ même type ; attraction ⇒ type opposé. 2) interaction entre T et le second bâton après frottement : l'opposé de celle observée avec le premier (si T repousse le verre, il attire l'ébonite, et inversement). (Réponse non imprimée ; le résultat réel du mica n'est pas donné.)
- **أقيّم مكتسباتي (p. 65)** : verre frotté à la soie, q = 0,032 µC. 1) **n = 0,032×10⁻⁶ / 1,6×10⁻¹⁹ = 2×10¹¹** (recalcul exact). 2) montrer que la charge de la soie est négative. ⚠ La leçon n'énonce nulle part que les deux corps frottés prennent des charges opposées ; seul le texte « هل من مزيد » p. 69 (Du Fay : électricité « راتنجيّة » produite « في الكهرمان والحرير ») permet de conclure. Question en partie hors cours.
- **تمرين 1 (vrai/faux, p. 65)** : 1 « نحصل على الكهرباء الساكنة بواسطة تكهرب الأجسام » ✔ ; 2 « لا يتكهرب جسم ماديّ إلاّ بالاحتكاك » ✘ ; 3 « التكهرب بالتماس طريقة عمليّة لظهور الكهرباء الساكنة » ✔ ; 4 « النوّاس الكهربائي أداة تدلّ على تكهرب الأجسام » ✔ ; 5 « كلّ جسم ماديّ متكهرب ناقل للكهرباء » ✘ ; 6 « كلّ جسم متكهرب بالتماس يحمل شحنة » ✔ ; 7 « لا يتنافر جسمان إلاّ إذا كانا حاملين لشحنتين كهربائيتين لهما نفس العلامة » ✔.
- **تمرين 2 (QCM, p. 66)** :
  1. un bâton de verre électrisé par frottement attire → « كلّ قضيب إبونيت متكهرب بالاحتكاك » (et aussi, attendu en creux, « كلّ قضيب زجاجي آخر تكهرب بالتماس مع قضيب إبونيت متكهرب بالاحتكاك » — ⚠ deux réponses justes).
  2. l'électrisation produit → « ظهور كمّية من الكهرباء الساكنة » ; ⚠ ambigu : « ظهور شحنة كهربائيّة سالبة أو شحنة كهربائيّة موجبة » est aussi juste pour un corps, et « …سالبة وشحنة… موجبة في نفس الوقت » est physiquement juste pour le couple frotté (non enseigné).
  3. A négative, B positive, pendules rapprochés doucement → « تتجاذب الكويرتان A و B ».
  4. A attire B et repousse C ⇒ B et C de signes opposés ⇒ « يحصل تجاذب بينهما » (⚠ l'option « تنتقل كمّية من الكهرباء… » peut suivre un contact, non demandé).
  5. ébonite frottée à la fourrure → « تظهر على قضيب الإبونيت شحنة كهربائيّة سالبة ».
- **تمرين 3 (tableau, p. 66–67)** — lignes : verre frotté (+) ; verre électrisé par contact avec une ébonite frottée (−). Colonnes : verre frotté (+) ; plexiglas frotté (−) ; ébonite électrisée par contact avec un plexiglas frotté (−).
  - Ligne verre (+) : تنافر / تجاذب / تجاذب.
  - Ligne verre (−) : تجاذب / تنافر / تنافر.
- **تمرين 4 (p. 67)** : corps électrisé A ; boule de fer B chargée **positivement**, suspendue à un fil isolant ; B est attirée jusqu'au contact puis repoussée. Explication : A est de signe opposé (négatif) ⇒ attraction ; au contact B prend une partie de la charge de A et devient du même signe que A ⇒ répulsion. ⚠ **Énoncé défectueux** : la question demande « علامة الشحنة التي كانت تحملها الكويرة في البدء » alors que ce signe (positif) est donné dans l'énoncé ; il s'agit vraisemblablement du signe de A (négatif). De plus, que B devienne négative suppose |qA| > |qB| (non discuté, pas enseigné).
- **تمرين 5 (p. 67)** : q = 4,8.10⁻¹⁴ C. 1) e = 1,6.10⁻¹⁹ C ; 2) **n = 4,8×10⁻¹⁴ / 1,6×10⁻¹⁹ = 3×10⁵** ; 3) q’ = −4,8.10⁻¹⁴ C → même nombre **3×10⁵** (même valeur absolue).
- **تمرين 6 (p. 67)** : A1 et A2 chargés positivement. Exp. 1 : A1 attire B (électrisé) ⇒ **B négatif**. Exp. 2 : A2 touche C non électrisé ⇒ **C positif** (électrisation par contact, même signe). 3) B (−) approché de C (+) ⇒ **attraction**. ⚠ « الجسم B متكهرب » est nécessaire pour exclure un B neutre attiré (phénomène d'influence non enseigné).
- **أجرّب بنفسي « أصنع مكشافا كهربائيّا » (p. 68)** : matériel : قنّينة زجاجيّة صغيرة، سلك معدني صلد، رقيقة ألومنيوم (مطبخ)، رقيقة معدنيّة (حلوى)، قلم جاف مع قطعة من الحرير، ورق كرتون، شريط لاصق، غراء، زرديّة ومقص. Étapes : disque en carton au diamètre du goulot ; fil plié à angle droit à un bout, passé par le centre du disque, collé ; bande de feuille métallique pliée sur le bout coudé (شكل 1) ; disque fixé sur le goulot (شكل 2) ; boule de papier alu au sommet (شكل 3) ; stylo frotté à la soie approché : « ألاحظ أنّ طرَفَيْ الشريط المعدني يتنافران » (شكل 4). ⚠ Le stylo frotté à la soie : signe non précisé.
- **هل من مزيد « الكهرباء الساكنة » (p. 69, « من موسوعة التطبيقات العلمية الميسّرة »)** : Thalès (~600 av. J.-C., ambre/« الكهرمان (العنبر) » frotté attire plumes, fils, laine) ; « وليام جلبرت (1544-1603) » médecin d'Élisabeth Ire : verre et soufre aussi ; nom « إلكترون » = ambre en grec (« ونحن حذونا حذوه في العربيّة باشتقاق «كهرباء» من كهرمان ») ; « شارل دوفييه (1698-1739) », 1733 : deux types — « كهرباء «زجاجيّة» تتولّد عن حكّ الزجاج والبلّور والشعر أو الصوف » et « كهرباء «راتنجيّة» تتولّد في الكهرمان والحرير » ; « وأنّ النوعين المختلفين يتجاذبان بينما المتماثلان يتنافران ».

### Bornes
- ✅ Deux sortes d'électricité (vitreuse/résineuse) ; charge électrique q, charge élémentaire e = 1,6.10⁻¹⁹ C ; q = ±n.e, |q| = n.e, n ∈ IN* ; unité coulomb C et sous-multiples µC, mC ; signe conventionnel : vitreuse > 0, résineuse < 0 ; attraction/répulsion selon les signes ; détermination du signe inconnu par comparaison à une charge connue.
- ⛔ **Le mot « électron » n'est jamais associé à e ni au transfert de charges** dans la leçon (il n'apparaît que dans l'étymologie p. 69) ; aucune explication microscopique (transfert d'électrons, atomes) ; « e » est présenté comme « شحنة كهربائيّة بسيطة » positive (e = + 1,6.10⁻¹⁹ C).
- ⛔ Pas de loi de Coulomb, ni de force chiffrée, ni de distance ; pas d'électrisation par influence ; pas de conservation de la charge énoncée.
- ⛔ Il n'est pas dit explicitement que les deux corps frottés prennent des charges opposées (pourtant requis par l'أقيّم مكتسباتي p. 65).
- ⛔ Les questions d'ouverture (pôles de la pile, paratonnerre) restent sans réponse.

### Vocabulaire officiel (Arabe ↔ lexique p. 211–216, entrée française)
- شحنة كهربائيّة بسيطة ↔ Charge Electrique élémentaire ; شحنة سالبة ↔ Charge négative ; شحنة موجبة ↔ Charge positive ; مشحون سلبا / إيجابا ↔ Chargé négativement / positivement ; كولون ↔ Coulomb ; ألكترون ↔ Electron ; تعادل كهربائي ↔ Electroneutralité.
- كهرباء راتنجيّة ↔ Electricité résineuse ; كهرباء زجاجيّة ↔ Electricité vitreuse ; تكهرب ↔ Electrisation ; كهرباء ساكنة ↔ Electrostatique ; مكشاف كهربائي ↔ Electroscope ; نواس كهربائي ↔ Pendule Electrique ; ركاب ↔ Etrier ; تجاذب ↔ Attraction ; تنافر ↔ Répulsion ; راتنج ↔ Résine ; ميكا ↔ Mica ; بليكسيقلاص ↔ Plexiglas ; إبونيت (مطاط صلب معالج بالكبريت) ↔ Ebonite ; بيلسان ↔ Sureau ; كرة أو كويرة ↔ Boule ; مرو (بلّور الصخر) ↔ « Qaurtz » (sic) ; نيلون ↔ Nylon ; احتكاك (تدليك) ↔ Frottement ; دلك ↔ Frotter ; طقطقة أو فرقعة ↔ Crépitement ; دافع الصواعق ↔ Paratonnerre ; مضاعف ↔ Multiple.
- Termes des leçons 1–4 présents au lexique : جهاز تغذية ↔ Alimentation (en électricité) ; متناوب ↔ Alternatif ; مناوب ↔ Alternateur ; تيّار مستمرّ ↔ Courant continu ; تيّار القطاع ↔ Courant secteur ; جيبيّ (تيّار متناوب) ↔ Sinusoïdal (courant alternatif) ; دورة ↔ Période ; تردّد ↔ Fréquence ; قيمة فعّالة ↔ Valeur efficace ; فعّال (توتّر) ↔ Efficace (tension) ; قيمة قصوى ↔ Valeur maximale ; مسح ↔ Balayage ; رسم تذبذبي ↔ Oscillogramme ; مشواف الذبذبات ↔ Oscilloscope ; بقعة ضوئيّة ↔ Spot lumineux ; إشراقة (أو نورانية) ↔ Luminosité ; تركيز ↔ Focalisation ; منحى ↔ Courbe / Direction ; لحظة ↔ Instant ; متناظر ↔ Symétrique ; دينامو (مولّدة) درّاجة ↔ Dynamo (ou génératrice) de bicyclette ; محور الفاصلات، الترتيبات ↔ Axes des abscisses, des ordonnées ; علامة ↔ Plaque signalétique ; محوّل ↔ Transformateur ; عدّاد ↔ Compteur ; قطاع ↔ Secteur ; توتّر القطاع ↔ Tension du secteur ; تركيب منزلي ↔ Installation domestique ; شبكة كهربائيّة ↔ Réseau électrique ; منشب تيّار ↔ Prise de courant ; نشيبة ↔ Fiche ; غمد ↔ Douille ; فاصل (تفاضلي) ↔ Disjoncteur (différentiel) ; سلك الطور ↔ Fil de phase ; سلك محايد ↔ Fil neutre ; سلك التأريض ↔ Fil de terre ; سلك مكهرب ↔ Fil sous tension ; سلك عار ↔ Fil dénudé ; هيكل جهاز كهربائي ↔ Masse d'appareil électrique ; صعق ↔ Electrocution ; مفكّ لوالب مخبار ↔ Tournevis testeur ; محاكاة ↔ Simulation.
- ⚠ Absents du lexique (constaté p. 211–216) : « Tension alternative », « Variable (courant/tension) », « Valeur crête », « Hertz », « Court-circuit » (دارة مقصورة), « Fusible » (صهيرة), « Diode électroluminescente » (صمّام مشعّ), « Rhéostat » (معدّلة).
- ⚠ Anomalies du lexique relevées au passage : « Carbonate de soduim » (sic) ; « Qaurtz » (sic) ; en-tête « E » répété au lieu de « G » p. 213 (Galet de dynamo…) et entrées « F » (Fibre optique, Fiche…, Fréquence, Frottement) rangées sous l'en-tête « G » ; dans l'entrée arabe p. 217 : « Déviation ↔ انعكاس كلّي » et « Réflexion de la lumière ↔ انكسار الضوء » (correspondances erronées).

### Leçon 08 — « المحروقات : أنواعها، مصادرها واستعمالاتها » (ص 73–75)

Manuel CNP 103902P00, 9ème. محور : **المادّة في الطبيعة** — باب : **الذرّة والاحتراق** (خريطة p. 5). Type de séance (خريطة) : icône « expérimentale » (télescope). Titre carte : « المحروقات : أنواعها، مصادرها واستعمالاتها ».

### Pages d'ouverture du محور (p. 70–72) — lues
- p. 70 : page de titre « المــادّة في الطبيعة » (image d'un modèle moléculaire éclaté-compact) ; bandeau : « الذّرة والاحتراق / الرّموز الكيميائيّة / المحاليل الشارديّة ».
- p. 71 « مكتسباتي القبليّة » :
  - **المعارف** : 1- أحدّد الحالة الفيزيائيّة الّتي يوجد عليها جسم ما. 2- أعرّف الجسم النّقيّ. 3- أذكر بعض التّحوّلات الفيزيائية للمادّة. 4- أعدّد خاصّيات الأجسام الغازيّة والأجسام السّائلة والأجسام الصّلبة. 5- أذكر أهمّية الأكسجين في عمليّة الاحتراق. 6- أعرّف الكتلة والحجم. 7- أعرّف الكتلة الحجمية للأجسام. 8- أعرّف الهباءة والجسم النّقيّ الهبائي.
  - **المهارات** : 1- أقوم بتجارب تبيّن مختلف التحوّلات الفيزيائيّة. 2- أقوم بإثبات وجود ثاني أكسيد الكربون. 3- أتعرّف إلى منتجات عمليّة الاحتراق. 4- أتعرّف إلى الاحتراق التّام وإلى الاحتراق غير التّام من خلال نتائجه. 5- أقيس كتلة جسم وحجمه. 6- أميّز بين المنحلّ والمحلّ. 7- أقوم بتجارب انحلال. 8- أتعرّف إلى المزيج المتجانس والمزيج غير المتجانس. 9- أفصل بين مكوّنات المزيج. 10- أفسّر ظاهرة الانحلال بتقطّع المادّة. 11- أشغّل موقدا غازيّا. 12- أدرك مخاطر الاحتراق غير التّام على الحياة والبيئة.
  - Remarque : « الهباءة » et « الجسم النّقيّ الهبائي » sont donnés comme **prérequis** (acquis de 8ème) — la leçon 11 réemploie « الهباءة ».
- p. 72 « الــذّرة والاحــتراق » (page de باب) : liste 8 à 12 ; questions d'amorce : « فيم تتمثّل عمليّة تكرير النفط ؟ وما الفائدة منها ؟ » ; « لماذا ينصح دائما بالاقتصاد في استهلاك المحروقات ؟ » ; « ما الذي يجعل منتجات عمليّة الاحتراق تختلف عن المُحرِق والمحروق ؟ » ; « لماذا كلّ ذلك الاهتمام بالغاز الطبيعي في مختلف أنحاء المعمورة رغم كثرة الاحتياطات الواجب اتّخاذها في كلّ أطوار استغلاله ؟ » ; « هل الاحتراق تحوّل فيزيائي أم كيميائي ؟ » ; « ما الفرق بين الهباءة والذرّة ؟ ».

### Objectifs (خريطة p. 5, communs aux leçons 8 et 9)
- ذكر بعض المحروقات المتداولة
- ذكر مصادر بعض المحروقات.
- وصف طرائق نقل المحروقات وتخزينها طبقا لقواعد السلامة.

### Déroulé
- **أتأمّل وأتساءل (p. 73)** — 4 vignettes-questions, aucune expérience ni mesure :
  - briquet : « ما هي المــادّة الموجودة داخل قارورة الغاز المنزليــّة ومـا هو مصدرها ؟ لماذا تسمّى تلك القارورة «قارورة غاز» في حين عند تحريكها يُسمع خريرُ سائل ؟ هل هو نفسه السّــائل الّذي تحتوي عليه ولاّعة الجيب ؟ »
  - pompes (GASOIL, SUPER, SANS PLOMB 95/98) : « لماذا ذلك التنوّع للمحروقات الموجودة بمحطّة تزويد السيارات بالوقود ؟ وما هي مصادرها ؟ »
  - plate-forme pétrolière : « تُستخرج من النفط محروقات عديدة. ما هي تلك المحروقات ؟ وكيف يتمّ الحصول عليها ؟ ما هي مجالات استعمالاتها ؟ »
  - braises : « لا تزال الكثير من العائلات في بلادنا تستعمل الفحم في العديد من الأغراض المنزليّة (التدفئة، التّسخين، الطّهي...) ما هو مأتاه ؟ وكيف نحافظ على جودته ؟ »
- **أبحث وأتأكّد (p. 74)** : recherche documentaire/terrain — « أقوم ببحث وثائقي في الغرض وذلك بالرّجوع إلى مصادر مختلفة من كتب ومجلاّت وشبكة الواب وببحث ميدانيّ إن أمكن (الاتّصال مثلا بالوكالة التّونسيّة للطّاقة، زيارة معمل تكرير النّفط ببنزرت، محطّة الهواريّة لضخّ الغاز الطّبيعي، زيارة حقل من حقول استخراج النّفط ببلادنا...) ». Aucune donnée chiffrée, aucun calcul.
- **Tableau المحروق / مجالات استعماله / المصدر (p. 74)** — verbatim :

| المحروق | مجالات استعماله | المصدر |
|---|---|---|
| الفحم | استعمالات منزليّة بالأساس | تفحّم الحطب في فرن (طريقة صناعيّة) أو في مفحمة (طريقة تقليديّة تعرف في بلادنا باسم المردومة.) |
| الفحم الحجري | إنتاج الكهرباء – صناعة الفولاذ – صناعة المعادن– التّسخين– التّدفئة المنزليّة– إنتاج بعض المحروقات الغازيّة (الهيدروجين – الايتان...) | مناجم صخور طبقيّة من أصل نباتي سوداء أو بنيّة اللّون. |
| البوتان والبروبان | استعمالات منزليّة بالأساس. | النفط (البترول) : سائل يتكوّن من بقايا النـباتـات والحيـوانـات الموجـودة تحت رسوبات متراكمة. (cellule commune aux 5 lignes pétrolières) |
| البنزين | السيارات | ″ |
| البارافين | الشمعة | ″ |
| الكيروزين | الطائرات | ″ |
| المازوت | الجرارات – الباخرات – آلات التّسخين. | ″ |
| الغاز الطبيعي (مزيج متكوّن أساسا من الميتان ومن كميات قليلة متفاوتة من البروبان والبوتان والإيتان ) | الطّبخ – التّسخين – التدفئة. | يتكوّن الغاز الطبيعي إثر تخمّر موادّ عضويّة (بقايا النباتات والحيوانات البحريّة الدّقيقة) ويوجد بين طبقات الصّخور العميقة في باطن الأرض. ويأتي في مصدرين : – الغاز المرافق للنّفط والّذي يفصل عنه ويُجمع من الإفرازات. – الغاز الحر (وهو أكثر وفرة من الغاز المرافق) المستخرج من آبار بريّة أو بحريّة منفصلة عن آبار النّفط. |

### Encadré أستنتج (p. 74) — VERBATIM
> **المحروقات المستعملة متعدّدة، فمنها ما هو سائل كالبنزين والفيول ومنها ما هو غاز كالبوتان والميتان ومنها ما هو صلب كالفحم والحطب.**
> **أهميّة المحروقات مرتبطة بوفرتها وبمجالات استعمالها وتعدّدها :** (suivi du tableau ci-dessus)

Aucune formule, unité ou symbole dans la leçon (pas de formule chimique : ni CH₄ ni C₄H₁₀).

### Exercices
- **أقيّم مكتسباتي (p. 75)** : « بالاعتماد على ما حصلت عليه من مكتسبات وبالاستناد إلى الوثيقة التّالية، أعدّد المحروقات المستخرجة من النّفط وأحدّد مجالات استعمالاتها. »
  Document = schéma de raffinerie :
  - « برج تقطير مجزّأ تحت الضغط الجوّي » alimenté par « نفط خام » chauffé ; niveaux de température (du haut vers le bas) **120°C, 180°C, 260°C, 340°C, 360°C, 370°C** ; soutirages : « غاز وبنزين » (tête → voiture/pompe), « نفتا » → « مواد كيميائيّة », « كيروزين » → hélicoptère, « مازوط » → tracteur / bus, « فيول منزلي » → maison, « فيول صناعي » ; en fond « مواد ثقيلة » réchauffées → « برج تقطير تحت ضغط منخفض » : « مواد للتحويل » → « مواد كيميائيّة », « زيوت » → lampe, « فيول ثقيل » → navire, fond **400°C** : « زفت صناعي » → « خرسانة اسفلتيّة ».
  - Réponse attendue : غاز (بوتان/بروبان) وبنزين (سيارات)، نفتا (مواد كيميائية)، كيروزين (طائرات)، مازوط (جرارات، حافلات)، فيول منزلي (تدفئة)، فيول صناعي، زيوت، فيول ثقيل (بواخر)، زفت (طرقات). Pas de calcul.
  - ⚠ Orthographe : le schéma écrit « مازوط », le tableau p. 74 « المازوت » ; « اسفلتيّة » sans hamza. Le mot « التقطير المجزّأ » apparaît pour la première fois ici (dans une image) ; il n'est pas défini dans la leçon (il reparaît dans l'exercice 1-3 et 2-1 p. 81).
- Les exercices « أعوّل على نفسي » p. 81–83 et les documents p. 84–85 (placés après la leçon 9) portent aussi sur la leçon 8 — voir L09.md.

### Bornes
- ✅ Classement des combustibles par état physique (صلب / سائل / غاز) avec exemples officiels (البنزين، الفيول ؛ البوتان، الميتان ؛ الفحم، الحطب).
- ✅ Origine : الفحم (تفحّم الحطب، « المردومة ») ≠ الفحم الحجري (مناجم) ; النفط (بقايا نباتات وحيوانات تحت رسوبات) ; الغاز الطبيعي (تخمّر موادّ عضويّة ; غاز مرافق / غاز حرّ — le gaz libre « أكثر وفرة »).
- ✅ Gaz naturel = « مزيج » majoritairement de méthane + propane, butane, éthane.
- ✅ Usages de chaque combustible (tableau) ; produits du raffinage (schéma).
- ⛔ Aucune formule chimique, aucune composition chiffrée, aucun pouvoir calorifique, aucune équation de combustion.
- ⛔ Le principe physique de la distillation fractionnée (températures d'ébullition) n'est pas expliqué dans le texte — seules les températures du schéma p. 75 figurent.
- ⛔ Pas d'expérience réalisée malgré l'icône « expérimentale » de la carte (séance documentaire de fait).

### Vocabulaire officiel (à croiser avec le lexique p. 211–223, hors de ma plage)
المحروقات، المحروق، الفحم، الحطب، الفحم الحجري، تفحّم، مفحمة (المردومة)، النفط (البترول)، البوتان، البروبان، الميتان، الإيتان، الهيدروجين، البنزين، البارافين، الكيروزين، المازوت (مازوط)، الفيول (منزلي/صناعي/ثقيل)، نفتا، زيوت، زفت، الغاز الطبيعي، الغاز المرافق، الغاز الحر، تكرير النفط، برج تقطير مجزّأ، نفط خام، مصدر، مجالات الاستعمال.

### Leçon 09 — « نقل المحروقات وتخزينها والحماية من مخاطرها » (ص 76–85)

محور : **المادّة في الطبيعة** — باب : **الذرّة والاحتراق**. Type de séance (خريطة) : icône documentaire (livre). Pages 76–80 = leçon ; 81–83 = « أعوّل على نفسي / أتمرّن على حلّ المسائل » (exercices 1–8, couvrant les leçons 8 et 9) ; 84–85 = « أستغلّ وثيقة » (النفط ; الغاز الطبيعي).

### Objectifs (خريطة p. 5 — case commune aux leçons 8 et 9)
- ذكر بعض المحروقات المتداولة
- ذكر مصادر بعض المحروقات.
- وصف طرائق نقل المحروقات وتخزينها طبقا لقواعد السلامة.

### Déroulé
- **أتأمّل وأتساءل (p. 76)** — 5 questions sur images, sans mesure :
  - « تُستعمل أحيانا رغوة الصّابون للتأكّد من عدم تسرّب البوتان خارج قارورة الغاز. ما الغاية من ذلك؟ وماذا يمكن أن ينجم عن تسرّب الغاز ؟ »
  - pictogramme flamme : « ماذا يعني الرّمز المجسّد في الشكل المقابل ؟ »
  - tuyau « A REMPLACER AVANT 2001 » : « في عدّة حصص إذاعيّة وتلفزيّة يُنصَحُ بتغيير الأنبوب الّذي يوصل غاز البوتان إلى جهاز استهلاكه بصفة متجدّدة. ما الغاية من ذلك ؟ وماذا يمكن أن يحدث في صورة ما إذا تمادينا في استعمال أنبوب مُتقادم ؟ »
  - « لماذا لا نترك قارورة الكحول المنزلي مفتوحة وخاصّة بجانب مصدر حرارة ؟ »
  - extincteur : « مطفأة الحرائق لازمة في كلّ مكان يرتاده العموم. لماذا ؟ »
- **أبحث وأتأكّد (p. 77)** : « أقوم ببحث وثائقي في الغرض وذلك بالرّجوع إلى مصادر مختلفة من كتب ومجلاّت وشبكة الواب وببحث ميدانيّ إن أمكن (الاتّصال مَثَلا بالوكالة الوطنيّة لحماية المحيط، بوكالة الحماية المدنيّة...) ».
- **Tableau المحروق / طريقة نقله وتخزينه (p. 77–78)** — verbatim :
  - **الغاز الطّبيعي** : « يُنقل الغاز الطبيعي عبر شبكات أنابيب ذات أقطار كبيرة وضغوط عالية كما ينـقل مسيّلا في ميتانيّة (سفينة لنقل الميتان). يـخزّن الـغاز الطـبيعي تحت الأرض وذلك بضخّه في طبقة من الرّمال أو الأحـجـار الإسفـنجـيّة. (أنظر الرّسم المقابل) كـمـا يمكن تـخزينه في المناجم النّاضبة من الملح. » Schéma : « بئر للمراقبة »، « ابار للضخ والجلب »، « محطّة للانضغاط »، « طبقة من الطين غير قابلة للاختراق »، « الغاز »، « ماء و رمل »، « توزيع ».
  - **البوتان والبروبان** : « يتمّ تخزين البوتان والبروبان متمازجين على حالة سائلة وبنسب متفاوتة في قوارير وصهاريج حديديّة تحت ضغط عال. »
  - **المحروقات النفطيّة** : « تُخزّن المحروقات النّفطيّة في خزّانات حديديّة كبيرة مركّزة عادة في معامل تكرير النّفط أو خارجها وتُنقل إلى محطّات التّوزيع للعموم في صهاريج خاصّة. »
  - **الفحم** : « يخزّن في كهوف ومستودعات ويُنقل في أكياس إلى البيع للاستهلاك. »
- **Tableau « الحماية من مخاطر المحروقات » : نوع المخاطر / المخاطر وقواعد السّلامة (p. 79–80)** — verbatim :
  - **خطر الحرائق** : « كلّ محروق غازي قابل للاشتعال حتّى في غياب محراق. لتجنّب الخطر النّاجم عن اشتعال المحروق يجب احترام العديد من قواعد السّلامة، منها ما يلي : 1 – اتّباع طريقة عمليّة سليمة عند تشغيل موقد غاز. 2 – إبعاد كلّ لهب وتفادي إحداث أيّ شرارة بالقرب من المحروقات. 3 – تخزين المحروق في مكان به هواء متجدّد. 4 – تركيز ظاهريّ للأنابيب النّحاسيّة النّاقلة للغاز الطّبيعي داخل أيّ محلّ. 5 – مراقبة سلامة الأنبوب المطّاطي الموصل قارورة البوتان بجهاز الاستعمال وتغييره في الآجال. 6 – تجهيز كلّ محلّ بمطفئة الحرائق. » (photo station-service, pictogramme « interdit de fumer »).
  - **خطر الانفجار** : « تتسبّب المحروقات الغازيّة وحتّى السّائلة منها (حيث إنّ المحروقات النفطيّة سهلة التبخّر) في حدوث انفجار إذا ما تسرّبت في فضاء مُغلق. لتفادي ذلك يجب احترام العديد من قواعد السّلامة منها ما يلي : 1 – تخزين المحروق في مكان به هواء متجدّد. 2 – مزج المحروقات الغازيّة من قبل المصنّع بشوائب ذات رائحة تمكّننا من التفطّن بالشمّ إلى أيّ تسرّب للغاز. 3 – مراقبة حفظ المحروق في خزّانه لتفادي أي تسرّب عرضي له في الفضاء المحيط به. 4– إبعاد كلّ لهب وتفادي إحداث أيّ شرارة بمكان الخزن. 5– عدم تشغيل موقد غازي قبل التثبّت من انعدام أيّ تسرّب للغاز عن طريق حاسّة الشمّ. »
  - **خطر الاختناق** : « يمكن أن يتسبّب الاحتراق غير التّام في الاختناق. وجب إذن الحرص على أن يكون الإحتراق المستغلّ تامّا. لذلك ينصح باحترام قواعد السّلامة. من أهمّ تلك القواعد نذكر ما يلي : 1 – صيانة الأجهزة المشتغلة بالغاز (أجهزة طبخ ، تدفئة، تسخين...) وذلك بتجهيز كلّ محراق بالنضاحة المناسبة وبتنظيفه. 2 – الحرص على ضبط الجهاز أو إشعار المِهني المختصّ للقيام باللاّزم كلّما لوحظ أنّ اللّهب المنبعث من محراق الجهاز غير نظيف. 3 – تهوئة كلّ فضاء نحتاج فيه إلى استغلال عمليّة احتراق. 4 – تركيز الأجهزة المشتغلة بالغاز في أمكنة بها هواء متجدّد بالإضافة إلى تزويدها بمنافذ مناسبة للتهوئة. » Deux photos de flammes : bleue (complète) et jaune-orangée (incomplète), sans légende.

### Encadré أستنتج (p. 80) — VERBATIM
> ◄ **رغم تعدّد ميادين استغلال المحروقات وأهميّتها، فالمخاطر النّاجمة عن الإستعمالات غير الواعية قد تؤدّي إلى كوارث بيئيّة وبشريّة كالحرائق والانفجارات والاختناق.**
> ◄ **الإستغلال المرشّد للمحروقات يتطلّب تخزينا مدروسا يأخذ بعين الاعتبار طبيعتها والعوامل الّتي من شأنها أن تتسبّب في احتراقها العرضي.**
> ◄ **تفاديا لكلّ خطر قد ينجم عن استغلال المحروقات يخضع كلّ تخزين لجملة من الاحتياطات الوقائيّة وتُضبط لكلّ استهلاك قواعد سلامة مناسبة.**

Aucune formule/unité/symbole ; aucun gaz toxique nommé (le CO « أحادي أكسيد الكربون » n'est pas cité ici — seulement « الاحتراق غير التّام » → « الاختناق »).

### Exercices
- **أقيّم مكتسباتي (p. 80)** : « ما هي العوامل الّتي تتسبّب في الاشتعال العرضي للمحروقات الغازيّة ؟ » → réponse : flamme/étincelle à proximité, fuite (tuyau vétuste, bouteille mal fermée), local non aéré. « لماذا يُمنع ترك محرّك السيارة يشتغل في محطّة البنزين أثناء تزويده بالوقود ؟ » → vapeurs d'essence (سهلة التبخّر) + étincelle/chaleur du moteur ⇒ incendie/explosion.
- **أعوّل على نفسي — أتمرّن على حلّ المسائل (p. 81–83)** :
  - **تمرين 1** (أجب بنعم أو لا) : 1- « الغاز الطبيعي مزيج من عدّة غازات. » → نعم (p. 74). 2- « يحتوي النفط على أجسام نقيّة مركّبة. » → نعم (mais la notion « جسم نقيّ مركّب » n'est enseignée qu'à la leçon 11 — ⚠ anticipation). 3- « عمليّة التّقطير المجزّإ للنفط هي عمليّة كيميائيّة. » → لا (séparation physique ; notion physique/chimique vue à la leçon 10 — ⚠ anticipation). 4- « توجد المحروقات في النّفط على ثلاث حالات فيزيائيّة. » → نعم (p. 84 : « الغازيّة كالبوتان والسّائلة كالبنزين والصّلبة كالزفت والقطران »).
  - **تمرين 2** (ضع علامة × أمام كلّ مقترح صحيح) : 1- « عمليّة التقطير المجزّأ للنّفط الخام تعطي » : أ- الفحم ب- البنزين ج- البارافين د- الكبريت → ب، ج. ⚠ د (الكبريت) : non traité dans le manuel ; le soufre est récupéré au raffinage (désulfuration) mais pas par distillation fractionnée → réponse attendue probablement « لا ». 2- « نوعيّة المحروقات المتأتّية من النّفط » : أ- هي نفسها مهما كان نوع النّفط. ب- مرتبطة بالحقل البترولي ج- مرتبطة بعمليّة التّكرير → ⚠ ambigu : rien dans la leçon ne permet de trancher entre ب et ج ; les deux sont défendables (réponse vraisemblable : ب و ج).
  - **تمرين 3** : « أتعرّف في القائمة التّالية إلى الأجسام الّتي تعتبر من عائلة المحروقات مبيّنا الحالة الفيزيائيّة الّتي يوجد عليها كلّ منها في الطّبيعة : الخشب، الماء، الفحم الحجري، الميتان، النّحاس، البروبان، البوتان، البنزين، الكيوروزين، المازوت، الكحول، الفحم، الهيدروجين. » → محروقات : صلبة : الخشب، الفحم الحجري، الفحم ؛ غازيّة : الميتان، البروبان، البوتان، الهيدروجين ; سائلة : البنزين، الكيروزين، المازوت، الكحول. Non combustibles : الماء، النّحاس. ⚠ Coquille : « الكيوروزين » (p. 82) au lieu de « الكيروزين ». ⚠ « في الطّبيعة » ambigu pour البوتان/البروبان (stockés liquides sous pression, p. 77) et pour الفحم/البنزين (produits transformés, pas « dans la nature »).
  - **تمرين 4** (أربط بواسطة سهم المحروق بمصدره) : البوتان → البترول ؛ الفحم → الخشب ؛ الغاز الطبيعي → « ترسّب بقايا النباتات والحيوانات البحريّة على مدى السّنين » ; الفحم الحجري → « مناجم صخور طبقيّة من أصل نباتي ». ⚠ Léger flou : le gaz naturel est aussi associé au pétrole (« الغاز المرافق »), et le butane figure aussi dans le gaz naturel (p. 74) ; la bijection reste reconstituable.
  - **تمرين 5** : correspondance 1 غاز البوتان، 2 كيروزين، 3 بنزين، 4 بارافين، 5 فيول ↔ أ دراجة ناريّة، ب شمعة، ج طائرة، د سيّارة، و سخّان. « أسند لكلّ رقم محروق الحرف المناسب لجهاز استعماله. » → 1-و، 2-ج، 3-د (et أ)، 4-ب ; 5 (فيول) → aucun appareil ne lui correspond clairement (le tableau p. 74 ne mentionne pas le fioul ; le schéma p. 75 donne « فيول منزلي » → maison) : ⚠ exercice mal bouclé — soit 5-و (chauffe-eau/chauffage au fioul) et 1 sans lettre, soit 3 prend أ et د. À signaler comme ambigu.
  - **تمرين 6** (compléter avec : تفحّم الحطب – منجم صخري من أصل نباتي – مادّة البوتان – النّفط – الكيروزين – البنزين – المازوت – الفيول) : 1- « يتأتّى الفحم من » تفحّم الحطب. 2- « تحتوي ولاّعة الجيب على » مادّة البوتان « ومصدرها » النّفط. 3- « تستعمل الطّائرات » الكيروزين « كوقود ». 4- « توجد في محطّة البنزين عدّة محروقات مثل : » البنزين – المازوت (– الفيول). « منجم صخري من أصل نباتي » = distracteur (source du charbon minéral).
  - **تمرين 7** : « أذكر مثالين من المحروقات المستعملة في المنزل ومصادرهما ؟ » → ex. البوتان (النفط)، الغاز الطبيعي (حقول الغاز)، الفحم (تفحّم الحطب).
  - **تمرين 8** (image salle de bain : chauffe-eau mural à gaz, radiateur à gaz sur bouteille, aucune fenêtre visible) : « في غرفة الاستحمام المرسومة بالصّورة المقابلة لم تحترم قواعد السّلامة الصحيّة. لماذا ؟ بيّن في فقرة موجزة، الإحتياطات الّتي يمكن اتّخاذها لتفادي الخطر. » → appareils à combustion dans un local fermé non ventilé ⇒ risque d'asphyxie (احتراق غير تامّ) ; placer les appareils dans un lieu à air renouvelé, منافذ للتهوئة, entretien.
- **أستغلّ وثيقة — النّفط (p. 84)** (« من كتاب الطّاقة والتكنولوجيا الحديثة (بتصرّف) ») : extraits clés verbatim : « النّفط (أو البترول) هو سائل معدنيّ قاتم اللّون يحتوي على أجسام كيميائيّة منها الغازيّة كالبوتان والسّائلة كالبنزين والصّلبة كالزفت والقطران. يتكوّن النّفط إثر تحلّل بمعزل عن الأكسيجين لموادّ عضويّة (بقايا نباتات وحيوانات) متجمّعة تحت رسوبات صلبة متراكمة. » ; transport : pipelines, ناقلات ضخمة, « الاسطوانيّة الّتي ينقل ويوزّع بها غاز النّفط المسيّل وهو مزيج من البوتان والبروبان » ; stockage : خزّانات حديديّة سطحيّة ; souterrain en « أربعة مواقع هي : المناجم النّاضبة من الملح، الاستخدام الجانبي للمناجم القائمة، الكهوف المتبقّية تحت الأرض من المناجم الخاصّة والتّخزين في مجمّعات المياه الجوفيّة. » Questions : 1- ما هي المحروقات الّتي يمكن استخراجها من النفط ؟ 2- ما هي وسائل النقل المستعملة لنقل تلك المحروقات ؟ 3- أين وكيف يخزّن البترول قصد استغلاله ؟ (réponses dans le texte).
- **أستغلّ وثيقة — الغاز الطّبيعي (p. 85)** (même source) : « إنّ الغاز الطّبيعي هو من أحسن أنواع الوقود الموجودة في الطبيعة لأنّه علاوة على قابليّته السّهلة للاحتراق لا يترك أيّة شوائب تؤثّر في البيئة ويتوفّر في المناطق النّفطيّة. » ; deux catégories « الغاز المرافق للنّفط والغاز الحرّ (غير المرافق) » ; « والميتان هو العنصر الرّئيسي في الغاز الطبيعي مع أنّ هناك مواد أخرى مثل الإيتان والبروبان والبوتان. وتوجد أحيانا في حقل الغاز الطبيعي سوائل البنزين الطبيعي وثاني أكسيد الكربون والأزوت والماء. » ; transport liquide en « ميتانيات ». Questions : 1- خاصيات الغاز الطبيعي... 2- أمثلة لمعامل أو مصانع تستخدم الغاز الطبيعي كمصدر للطاقة. 3- لماذا يُنقل الغاز الطبيعي أحيانا مسيّلا في الميتانيات رغم ما يحفّ بذلك من مخاطر ؟

### Bornes
- ✅ Modes de transport/stockage par combustible (gaz naturel : pipelines haute pression, méthaniers, stockage souterrain/mines de sel ; butane-propane : liquides sous haute pression en bouteilles/citernes ; produits pétroliers : réservoirs, camions-citernes ; charbon : grottes/dépôts, sacs).
- ✅ Trois risques officiels : **خطر الحرائق، خطر الانفجار، خطر الاختناق** avec leurs règles de sécurité numérotées (tests à la mousse de savon, odorisant « شوائب ذات رائحة », tuyau caoutchouc à changer, aération, extincteur).
- ✅ Lien احتراق غير تامّ → اختناق ; flamme « غير نظيف » ⇒ appareil à régler.
- ⛔ Aucune mention du monoxyde de carbone par son nom dans la leçon ; aucune donnée chiffrée (pression, volumes, limites d'explosivité).
- ⛔ Le mot « مطفأة/مطفئة » : les deux graphies apparaissent (p. 76 « مطفأة الحرائق », p. 79 « بمطفئة الحرائق »).

### Incohérences / points à signaler
- p. 79 : « كلّ محروق غازي قابل للاشتعال حتّى في غياب محراق » — formulation scientifiquement discutable (un gaz ne s'enflamme pas spontanément sans source d'ignition à température ambiante ; le texte veut probablement dire « hors d'un brûleur »). À ne pas reprendre tel quel.
- p. 85 : « لا يترك أيّة شوائب تؤثّر في البيئة » — surestimation (la combustion produit du CO₂) ; texte d'une source citée « بتصرّف ».
- p. 84 : « النّفط ... سائل معدنيّ » vs p. 74 : formé de restes végétaux et animaux (organique) — tension terminologique.
- Coquilles : « الكيوروزين » (ex. 3), « الإحتراق / الإستعمالات / الإستغلال » avec hamza fautive.

### Vocabulaire officiel
نقل، تخزين، خزّانات حديديّة، صهاريج، قوارير، ميتانيّة (ميتانيات)، مسيّل، شبكات أنابيب، محطّة للانضغاط، المناجم النّاضبة من الملح، الأحجار الإسفنجيّة، تسرّب، رغوة الصّابون، مطفأة/مطفئة الحرائق، خطر الحرائق، خطر الانفجار، خطر الاختناق، قواعد السّلامة، هواء متجدّد، تهوئة، منافذ للتهوئة، محراق، النضاحة، موقد غاز، الأنبوب المطّاطي، الأنابيب النّحاسيّة، شوائب ذات رائحة، سهلة التبخّر، الاحتراق غير التّام، الاحتراق العرضي، التقطير المجزّأ، غاز النّفط المسيّل، الزفت، القطران.

### Leçon 10 — « التّفاعل الكيميائي » (ص 86–88)

محور : **المادّة في الطبيعة** — باب : **الذرّة والاحتراق**. Séance expérimentale (icône télescope). Trois sous-titres : « احتراق الكربون » (p. 86), « الإحتراق التّام للميتان » (p. 87), « أنجز تجربة احتراق الكبريت » (p. 88, dans أقيّم مكتسباتي).

### Objectifs (خريطة p. 5)
- تعريف التفاعل الكيميائي
- التمييز بين التحوّلات الفيزيائيّة والتفاعلات الكيميائيّة
- التمييز بين المواد المتفاعلة ومنتجات التفاعل الكيميائي.

### Déroulé
1. **احتراق الكربون — أجرّب وألاحظ (p. 86)** : matériel « قطعة فحم، حامل، موقد كهربائي (أو موقد بنزن)، قنّينة حاوية لغاز الأكسجين، ماء الجير. » Protocole : « أسخّن بقعة من قطعة فحم حتّى التوهّج ثمّ أدخلها في القنّينة الحاوية لغاز الأكسيجين فألاحظ أنّ قطعة الفحم تتأجّج بشدّة لمدّة من الزّمن وفي الأثناء يتعكّر ماء الجير ويكسو قطعة الفحم طبقة رقيقة من الرّماد. » Schéma en 3 étapes : قطعة فحم sur حامل chauffée par « موقد بنزن » → dans flacon « غاز الأكسيجين » → flacon avec « ماء الجير » au fond. Aucune mesure.
   - **أفسّر ما حدث (p. 87)** — verbatim : « أثناء الاحتراق لم يتحوّل الفحم إلى حالة فيزيائيّة أخرى و لم ينحلّ جسم منهما في الآخر بل نفذ الأكسيجين وتآكل الفحم، وفي نفس الوقت ظهر ثاني أكسيد الكربون (الغاز الذي عكّر ماء الجير)، وهذا يعني تحوّل الفحم والأكسيجين إلى جسم جديد وهو ثاني أكسيد الكربون. إذن، لا يمكن أن يكون احتراق الفحم في الأكسيجين تحوّلا فيزيائيّا بل تحوّلا من نوع جديد يسمّى تفاعلا كيميائيّا. نقول إنّ الفحم والأكسيجين تفاعلا معًا فنسمّي كلاًّ منهما متفاعلا. أمّا ثاني أكسيد الكربون فهو الجسم الّذي نتج عن ذلك التّفاعل فنسمّيه منتجَ التفاعل. »
   - Bilan écrit (équation en mots, flèche rouge →) : **كربون + أكسيجين ⟵ ثاني أكسيد الكربون** — sous-titres « (المتفاعلان) » / « (منتج التّفاعل) ».
2. **الإحتراق التّام للميتان — أجرّب وألاحظ (p. 87)** : « أنجز التركيب المقابل » ; « أشغّل موقد بنزن ثمّ أسحب بلطف فوهته تحت القمع. فألاحظ أنّ الجانب الدّاخلي للقمع يغطّى شيئا فشيئا ببخار الماء، وفي الأثناء يُعكّر ماء الجير. » Schéma : « غاز الميتان » alimentant le bec, entonnoir renversé (« بخار الماء » sur la paroi), aspiration vers flacon « ماء الجير ».
   - **أفسّر ما حدث (p. 87)** — verbatim : « أعلم أنّه كلّما تحوّل جسم مادّي من حالة فيزيائيّة إلى أخرى أو انحلّ في الماء تحفظ طبيعته ولا تتغيّر تركيبته. أثناء تجربة الاحتراق التام تفاعل الميتان والأكسيجين معًا لينتج عن ذلك ظهور جسمين جديدين وهما ثاني أكسيد الكربون وبخار الماء. إذن لا يمكن اعتبار احتراق الميتان في الأكسيجين تحوّلا فيزيائيا بل هو تفاعل كيميائي كالّذي حصل بين الكربون والأكسيجين. نقول إنّ الميتان والأكسيجين لعبا دور المتفاعلين في عمليّة الاحتراق. أما ثاني أكسيد الكربون وبخار الماء فهما مُنتجَا ذلك التّفاعل. »
   - Bilan : **ميتـان + أكسيجين ⟵ ثاني أكسيد الكربون + ماء** — « (المتفاعلان) » / « (منتجا التّفاعل) ».

### Encadré أستنتج (p. 88) — VERBATIM
> ◄ **التّفاعل الكيميائي هو تحوّل تختفي أثناءه أجسام وتظهر أجسام جديدة .**
> ◄ **تسمّى الأجسام المتفاعلة متفاعلات والأجسام الجديدة مُنتَجات التفاعل.**
> ◄ **الاحتراق في الأكسيجين مثال للتّفاعل الكيميائي.**

Symboles/formules : aucun symbole chimique (C, O₂, CO₂, CH₄, H₂O absents) — bilans **en mots uniquement**, flèche « → » (dessinée ⟵ dans la mise en page RTL), signe « + ». Réactif témoin : **ماء الجير** (se trouble ⇒ CO₂). Unités : cm seulement (exercice).

### Exercices
- **أقيّم مكتسباتي — « أنجز تجربة احتراق الكبريت » (p. 88)** :
  - لوازم التجربة : « مسحوق الكبريت، سلك معدني، زرديّة، موقد بنزن (أو قدّاحة)، قنّينة ملئت أكسجينا ومحقنة. »
  - التجربة الأولى : « مستخدما الزرديّة، أقطع سلكا معدنيّا طوله 50 cm تقريبا وأثني أحد طرفيه لأشكّل حلقة صغيرة لا يزيد قطر تجويفها عن 0,5 cm . * أغمس الحلقة في مسحوق الكبريت (لعلّي إذا بللتها من قَبْل أجعل المسحوق يلتصق بسهولة). * أمسك السلك من طرفه الآخر ثمّ أشعل الكبريت. ما لون لهب الكبريت أثناء الاحتراق ؟ » → réponse attendue : flamme bleue (pâle/violacée) — non écrite dans le manuel.
  - التجربة الثّانية : « أعيد مراحل التّجربة الأولى ثمّ أدخل الكبريت المشتعل في قنّينة الأكسيجين. فألاحظ أنّ الكبريت يشتعل بتوهّج مفرزا غازا لا لون له يُسمّى ثاني أكسيد الكبريت، أتعرّف إليه بالسّعال الّذي يثيره. »
  - « هام جدّا : أسحب السلك المعدني وأغلق مباشرة القنّينة لكي لا أستنشق غاز ثاني أكسيد الكبريت. »
  - أستغلّ التجربة المنجزة : « 1 – أثْبتُ أنّه حصل تفاعل كيميائيّ. 2 – أُحدِّدُ الأجسام المتفاعلة والأجسام المنتَجة. » → 1) disparition du soufre et de l'oxygène, apparition d'un corps nouveau (ثاني أكسيد الكبريت) ; 2) **كبريت + أكسيجين → ثاني أكسيد الكبريت**.
  - ⚠ Méthode d'identification officielle du SO₂ = « بالسّعال الّذي يثيره » (toux) — procédé sensoriel, alors que la même page exige de ne pas le respirer (« لكي لا أستنشق ») : tension à signaler. « المحقنة » listée dans le matériel n'est pas utilisée dans le protocole.

### Bornes
- ✅ Définition du تفاعل كيميائي (disparition de corps / apparition de corps nouveaux) ; vocabulaire **متفاعلات / مُنتَجات التفاعل** ; opposition au تحوّل فيزيائي (changement d'état, dissolution : « تحفظ طبيعته ولا تتغيّر تركيبته »).
- ✅ Trois combustions : carbone (→ CO₂), méthane complète (→ CO₂ + eau), soufre (→ SO₂), toutes en mots.
- ✅ Tests : ماء الجير يتعكّر (CO₂) ; buée sur l'entonnoir (eau).
- ⛔ Aucun symbole ni formule, aucune équation équilibrée (réservé aux leçons 13–14).
- ⛔ Pas de conservation de la masse (loi de Lavoisier) — non mentionnée dans cette leçon.
- ⛔ La combustion incomplète du méthane n'est pas traitée ici (seul « الإحتراق التّام » ; pas de CO ni de carbone/suie).
- ⛔ Pas de notion d'énergie de réaction (exo/endothermique).

### Incohérences / remarques
- p. 86 : matériel « موقد كهربائي (أو موقد بنزن) » mais le schéma montre un « موقد بنزن ».
- Alternance d'orthographe « الأكسجين / الأكسيجين » (même page) et « الإحتراق » (hamza fautive) dans le sous-titre p. 87.
- « الفحم » (texte) et « كربون » (bilan) utilisés comme équivalents sans justification (le charbon de bois est assimilé au carbone).
- Le bilan écrit « ماء » alors que le texte dit « بخار الماء ».

### Vocabulaire officiel
التّفاعل الكيميائي، تحوّل فيزيائي، متفاعل / متفاعلات / المتفاعلان، منتج التفاعل / مُنتَجات / منتجا التفاعل، احتراق، الاحتراق التّام، الأكسيجين (الأكسجين)، الكربون، الفحم، ثاني أكسيد الكربون، الميتان، بخار الماء، ماء الجير (يتعكّر)، الرّماد، يتأجّج، التوهّج، الكبريت، مسحوق الكبريت، ثاني أكسيد الكبريت، موقد بنزن، قدّاحة، زرديّة، قمع، قنّينة، محقنة.

### Leçon 11 — « الذّرّة » (ص 89–94)

محور : **المادّة في الطبيعة** — باب : **الذرّة والاحتراق**. Séance expérimentale (icône télescope). Sous-parties : « وجود الذرّة » (p. 89), « تمثيل احتراق الكربون باستعمال النماذج الهبائيّة » (p. 90), « الأجسام النقيّة البسيطة والأجسام النقيّة المركَّبة » (p. 91) ; exercices « أعوّل على نفسي » p. 92–93 ; « أستغلّ وثيقة » + « أجرّب بنفسي » p. 94.

### Objectifs (خريطة p. 5)
- تجسيم بعض التفاعلات البسيطة باعتماد النماذج الهبائيّة
- التمييز بين الأجسام النقيّة المركّبة والأجسام النقيّة البسيطة.

### Déroulé
1. **وجود الذرّة — أتأمّل وأتساءل (p. 89)** — verbatim : « أعلم أنّ العديد من الأجسام الماديّة النقيّة مُتكوّنة من جزيئات مجهريّة متطابقة تُسمّى هباءات. إن كانت الهباءة (هذا الجسيم الأصغر الذي يمكن أن ينتُج عن تقطّع المادّة) لا تتجزّأ، فكيف وبمَ أفسّر التفاعلات الكيميائيّة بين هباءات مختلفة ؟ »
   - **أسلّم بوجود الذرّة** : « لأفسّر تفاعلا كيميائيّا أسلّم بأنّ الهباءة قابلة للتجزّء. لقد أثبتت التجارب والأبحاث فعلا أنّ كلّ هباءة مُتكوّنة من عدد معلوم من الجزيئات تسمّى كلّ جزيئة منها ذرّة. فهباءة الأكسيجين مثلا تتكوّن من ذرّتين متطابقتين (ذرّتا الأكسيجين)، أمّا هباءة ثاني أكسيد الكربون فهي تتكوّن من ذرّتَي أكسيجين وذرّة كربون. »
   - **أجسّد الذرّة والهباءة** : « لكي أجعل تركيبة الهباءة مُتاحة للعين المُجرّدة، أسند إلى الهباءة نموذجا تظهر فيه الذرّات المُكوّنة لها على شكل كويرات متماسكة. للتمييز بين ذرّة وأخرى مُختلفة عنها في الهباءة الواحدة تُعطى للكويرات النماذج أحجام وألوان مُختلفة. »
   - **Tableau des modèles d'atomes (أمثلة)** : الكربون → كويرة سوداء ; الأكسيجين → كويرة حمراء ; الهيدروجين → كويرة بيضاء ; الكبريت → كويرة صفراء ; الكلور → كويرة خضراء.
   - **Tableau des modèles de هباءات** : الأكسيجين (2 rouges accolées) ; الكربون (1 boule noire seule) ; ثاني أكسيد الكربون (rouge-noire-rouge, linéaire) ; الهيدروجين (2 blanches) ; الميتان (1 noire + 4 blanches) ; الماء (1 rouge + 2 blanches, coudée).
2. **Encadré أستنتج (p. 90)** — voir ci-dessous.
3. **تمثيل احتراق الكربون باستعمال النماذج الهبائيّة — أجرّب وألاحظ (p. 90)** : « علمًا أنّ ثاني أكسيد الكربون هو مُنتج تفاعل الكربون مع الأكسيجين بالاحتراق، أبحث كيف أحصل على نموذج لهباءة ثاني أكسيد الكربون باستعمال نموذج هباءة الأكسيجين ونموذج ذرّة الكربون. ألاحظ أنّه لا يمكن أن أحصل على نموذج هباءة ثاني أكسيد الكربون إلاّ بتفكيك نموذج هباءة الأكسيجين وتثبيت نموذجَيْ ذرّتَيْ الأكسيجين المفكوكتين إلى نموذج ذرّة الكربون. » Schéma : O ⟶ C ⟵ O puis ⟵ O-C-O.
4. **الأجسام النقيّة البسيطة والأجسام النقيّة المركَّبة — أتأمّل وألاحظ (p. 91)** : « أتأمّل النماذج الهبائية لبعض الأجسام النقيّة في الشكل المُقابل من حيث التركيبة، فألاحظ أنّ هناك هباءات متكونة من ذرّات متطابقة مثل هباءات الأكسيجين والكلور والأوزون وهناك هباءات أخرى متكوّنة من ذرّات مختلفة مثل : * هباءة الماء المتكوّنة من ذرّة أكسيجين وذرّتَي هيدروجين. * هباءة ثاني أكسيد الكربون المتكوّنة من ذرّة كربون وذرّتَي أكسيجين. * هباءة الميتان المتكوّنة من ذرّة كربون وأربع ذرّات هيدروجين. » Tableau الجسم النّقيّ / النموذج الهبائي : غاز الأكسيجين (2 O), الماء, غاز ثاني أكسيد الكربون, غاز الكلور (2 vertes), الميتان, غاز الأوزون (3 O).

### Encadrés أستنتج — VERBATIM
**p. 90 (1)**
> ◄ **تتكوّن الهباءة من جزيئات مجهريّة لا تتسنّى رؤيتها لا بالعين المُجرّدة ولا بالمجهر البصري وتسمّي الواحدة منها ذرّة.**
> ◄ **تنوّعُ الذرّات في الهباءة الواحدة مرتبط بطبيعة المادّة.**
> ◄ **لتجسيد الهباءات، تُمثل الذرّات بنماذج كرويّة الشكل.**

**p. 90 (2)**
> **احتراق الكربون في الأكسيجين تفاعل كيميائيّ يُمَثِّلُ بالنماذج الهبائيّة كما يلي :**
> [ذرّة كربون] + [هباءة أكسيجين] ⟵ [هباءة ثاني أكسيد الكربون] (modèles : ● + ●● → ●●●)

**p. 91 (3)**
> ◄ **الأجسام الهبائية النقية نوعان :**
> **أجسام نقية ذات هباءات متكوّنة من ذرّات متطابقة، وتسمّى أجسام نقية بسيطة.**
> **أمثلة : غازات الأكسيجين، الكلور، الأوزون...**
> ◄ **أجسام نقية ذات هباءاتٍ متكوّنة من ذرّات مختلفة، وتسمّى أجسام نقية مُركّبة.**
> **أمثلة : الماء، الميتان، ثاني أكسيد الكربون.**

Aucun symbole chimique (pas de C, O, H…) ni formule : tout est en noms + modèles colorés. Unités présentes : m (10⁻¹⁰ m), kg (10⁻²⁷ kg), g, cm absent. Grandeur « الذّريّة » (atomicité) définie dans l'exercice 5 seulement.

### Exercices
- **أقيّم مكتسباتي (p. 91)** : « بالاعتماد على نماذج الهباءات المرسومة على الشكل المقابل لأجسام نقية مختلفة، أصنّف تلك الأجسام إلى أجسام بسيطة وأجسام مُركّبة. » Modèles : غاز الأزوت (2 boules bleu-violet), غاز ثاني أكسيد الكبريت (O-S-O, jaune entre 2 rouges), غاز الهيدروجين (2 blanches), غاز النُشادر (1 bleue + 3 blanches). → بسيطة : الأزوت، الهيدروجين ; مركّبة : ثاني أكسيد الكبريت، النشادر. ⚠ La couleur de l'atome d'azote (bleu-violet) n'est pas dans le tableau des modèles p. 89 (5 atomes seulement : C, O, H, S, Cl) — l'élève doit l'inférer.
- **أعوّل على نفسي — أتمرّن على حلّ المسائل (p. 92–93)** :
  - **تمرين 1** (le terme scientifique) : 1- « تحوّلٌ لجسمٌ نقي من حالة فيزيائيّة إلى حالة فيزيائيّة أخرى » → تحوّل فيزيائي (تغيّر الحالة). 2- « تحوّلٌ تختفي أثناءه أجسام وتظهر أجسام جديدة » → التفاعل الكيميائي. 3- « أجسام تختفي إثر تفاعل كيميائيٌّ » → المتفاعلات. 4- « أجسام جديدة تظهر إثر تفاعل كيميائيٌّ » → منتجات التفاعل. 5- « جسمٌ نقيٌّ متكوّنٌ من هباءات ذات ذرّات متطابقة » → جسم نقيّ بسيط. (coquille : « لجسمٌ » avec tanwin).
  - **تمرين 2** (compléter le tableau التفاعل الكيميائي / الأجسام المتفاعلة / مُنتجات التفاعل) : احتراق الكربون → [الكربون والأكسيجين] → ثاني أكسيد الكربون ; الاحتراق التامّ لِـ[البوتان] → البوتان والأكسيجين → [ثاني أكسيد الكربون والماء] ; احتراق الكحول → الكحول و[الأكسيجين] → [ثاني أكسيد الكربون والماء]. ⚠ La combustion du butane et de l'alcool n'a pas été expérimentée dans la leçon 10 (transfert depuis le méthane). Numérotation « 1 – اِنسخ » sans « 2 ».
  - **تمرين 3** (× devant l'énoncé correct) : 1. « تُمثَّلُ الذرّات والهباءات بنماذج كرويّة الشكل. » → ⚠ ambigu : l'encadré dit que les **atomes** sont représentés par des sphères ; une هباءة polyatomique n'est pas sphérique → probablement faux (mais un élève peut cocher). 2. « كلّ جسم نقيّ يتكوّن من هباءات متطابقة يسمّى جسمًا نقيًّا بسيطًا. » → faux (il faut des **atomes** identiques). 3. « تتكوّن الذرّة من هباءة أو أكثر. » → faux. 4. « تتكوّن الهباءة من ذرّة أو أكثر. » → vrai (cf. هباءة الكربون = 1 atome, p. 89).
  - **تمرين 4** (× devant chaque corps composé ; modèles) : الإيتان (2 C + 6 H), الأوزون (3 O), الأسيتيلين (H-C-C-H), الهيدروجين (2 H), الكحول الأثيلي (2 C, 1 O, 6 H), الكلور (2 Cl) → مركّبة : الإيتان، الأسيتيلين، الكحول الأثيلي ; بسيطة : الأوزون، الهيدروجين، الكلور.
  - **تمرين 5** — définition verbatim : « نعني بالذّريّة عدد الذرّات المكوّنة للهباءة. مثال : تتكون هباءة الماء من ذرّة أكسيجين ومن ذرّتَيْ هيدروجين فنقول أنّ ذريّة هباءة الماء تساوي 3. إبحث إذن عن الذرية في الهباءات للأجسام التالية : الهيدروجين، الأكسيجين، غاز النّشادر، ثاني أكسيد الكربون، الإيتان، الماء. » → H₂ : 2 ; O₂ : 2 ; NH₃ : 4 ; CO₂ : 3 ; C₂H₆ : 8 ; H₂O : 3.
  - **تمرين 6** — tableau imprimé (verbatim, colonnes « ذرّة | قطرها (10⁻¹⁰ m) | كتلتها (10⁻²⁷ kg) ») :

    | ذرّة | قطرها (10⁻¹⁰ m) | كتلتها (10⁻²⁷ kg) |
    |---|---|---|
    | الكربون | 5,1 | 2 |
    | الهيدروجين | 1 | 7,1 |
    | الأكسيجين | 4,1 | 66,2 |
    | الأزوت | 5,1 | 33,2 |

    Questions : « 1. بالاعتماد على المعطيات المبيّنة بالجدول المقابل : أ– أيّ من الذرّات أقلّ حجما ؟ ب– ابحث عن كتلة هباءة الماء وكتلة هباءة الميتان. 2. لدينا قطعة من الفحم ذات كتلة قدرها m = 20 g إن اعتبرنا أنّ القطعة متكوّنة من الكربون فقط. أ– ابحث عن عدد ذرّات الكربون التي تحويها ؟ ب– ما هو الطول المتحصّل عليه، إن وضعنا ذرات الكربون جنبا إلى جنب وفي صفّ واحد. »
    - ⚠⚠ **Tableau fautif** (vérifié à 300 dpi et dans la couche texte : les chiffres imprimés sont bien 5,1 / 2 ; 1 / 7,1 ; 4,1 / 66,2 ; 5,1 / 33,2). Valeurs physiquement incohérentes : l'hydrogène (7,1) serait 3,5 fois plus lourd que le carbone (2). Les chiffres semblent **inversés** (défaut de mise en page RTL) : « 5,1 »→1,5 ; « 4,1 »→1,4 ; « 7,1 »→1,7 ; « 66,2 »→2,66 ; « 33,2 »→2,33. Valeurs réelles : d(C)≈1,5 ; d(O)≈1,4 ; d(N)≈1,5 (×10⁻¹⁰ m) ; m(H)=1,67×10⁻²⁷ kg ; m(C)=1,99×10⁻²⁶ kg ; m(O)=2,66×10⁻²⁶ kg ; m(N)=2,33×10⁻²⁶ kg — donc même « désinversée », la colonne masse mélange deux puissances (10⁻²⁷ pour H, 10⁻²⁶ pour C, O, N). La leçon 12 p. 95 donne d'ailleurs C 0,15 nm, O 0,14 nm, H 0,11 nm ; m(C)=2,0, m(O)=2,7, m(H)=0,2 (×10⁻²⁶ kg), ce qui confirme le diagnostic.
    - Réponses **avec les valeurs imprimées** (Decimal) : 1-أ : الهيدروجين (d = 1). 1-ب : m(H₂O) = 66,2 + 2×7,1 = **80,4×10⁻²⁷ kg** ; m(CH₄) = 2 + 4×7,1 = **30,4×10⁻²⁷ kg**. 2-أ : N = 0,020 / (2×10⁻²⁷) = **1×10²⁵** atomes. 2-ب : L = 10²⁵ × 5,1×10⁻¹⁰ = **5,1×10¹⁵ m**.
    - Réponses **avec les valeurs réelles** : m(H₂O) = 26,6 + 2×1,67 = 29,94 ≈ **29,9×10⁻²⁷ kg** ; m(CH₄) = 19,93 + 4×1,67 = 26,61 ≈ **26,6×10⁻²⁷ kg** ; N = 0,020/(2×10⁻²⁶) = **1×10²⁴** (1,0035×10²⁴ avec 1,993×10⁻²⁶) ; L = 10²⁴ × 1,5×10⁻¹⁰ = **1,5×10¹⁴ m**.
    - ⚠ L'exercice 6 fait calculer une masse de molécule et un nombre d'atomes **avant** la leçon 12 (qui introduit masse et taille des atomes) — anticipation.
- **أستغلّ وثيقة — الذرّة (p. 94)** — verbatim : « تهتمّ الكيمياء بالإضافة إلى دراسة الأجسام المختلفة وخواصّها وتفاعلاتها المتبادلة، بالكشف عن المكوّنات الأساسيّة للمادّة والتي يطلق عليها اسم العناصر مثل الذهب والنحاس والكربون... فإذا جزئت المادّة إلى قطع أصغر فأصغر سنحصل في النهاية على جُسيْمات صغيرة جدّا تحتفظ بخواصّ العنصر وتُسمّى الذرّات. وقد جاءت كلمة الذرّة من الأصل الإغريقي «atomos» التي تعني «الجزء الذي لا يتجزّأ» فالذرّة إذن هي أصغر جُسيم مادّي يمكن تمثيله بشكل كروي متناهي الصّغر لا يتعدّى قطره 1/10¹⁰ m. » Questions : 1- ما يدلّ على أنّ الذرّة لا تُرى بالعين المجرّدة ولا بالمجهر البصري (→ diamètre ≤ 10⁻¹⁰ m) ; 2- « هل تتكوّن كلّ الموادّ التي تحيط بنا من نوع واحد من ذرّات ؟ علّل جوابك. » (→ non : corps composés).
  - ⚠ « لا يتعدّى قطره 10⁻¹⁰ m » contredit les données du manuel (C ≈ 1,5×10⁻¹⁰ m ; p. 95 : plomb 0,3 nm = 3×10⁻¹⁰ m). Le mot « عنصر » apparaît ici sans définition (défini à la leçon 13).
- **أجرّب بنفسي — « كيف أزيل قشرة البيضة دون تكسيرها ؟ » (p. 94)** : matériel « بيضة غير مسلوقة– كأس زجاجيّة– خلّ » ; « أضع البيضة في الكأس. أصبّ الخلّ في الكأس حتّى أغمر البيضة. بعد ثلاثة أيام، أخرج البيضة بعناية من الكأس وأعرضها في الضوء. أحاول رؤية ما بداخل البيضة. » أحلّل وأفسّر : « 1- أبيّن أنّ ما حدث ناتج عن تفاعل كيميائي وأحدّد المتفاعلات ؟ 2– أتثبّت إن كان الخلّ قد تفاعل كذلك مع غشاء البيضة أم لا. » → la coquille (calcaire) disparaît, bulles de gaz (CO₂) : المتفاعلات = الخلّ وقشرة البيضة ; la membrane reste (pas de réaction). ⚠ Le manuel ne nomme ni le calcaire ni le gaz dégagé ; la réponse attendue n'est pas donnée.

### Bornes
- ✅ Atome (ذرّة) = constituant de la هباءة ; la هباءة est « قابلة للتجزّء » ; modèles moléculaires (boules colorées : C noir, O rouge, H blanc, S jaune, Cl vert) ; représentation d'une réaction par modèles (C + O₂ → CO₂) ; corps pur **simple** vs **composé** ; « الذّريّة » (atomicité, exo 5).
- ✅ Ordre de grandeur de l'atome (document : ≤ 10⁻¹⁰ m ; origine « atomos »).
- ⛔ Aucun symbole chimique ni formule (leçon 13).
- ⛔ Structure interne de l'atome (noyau, électrons) non abordée (leçon 12).
- ⛔ Le mot « عنصر » n'est pas défini (seulement cité dans le document p. 94).
- ⛔ La combustion du méthane n'est pas modélisée ici (seulement celle du carbone).

### Incohérences
- Carte p. 5 : leçon 12 « بنية الذرّة » annoncée p. 96, mais elle commence **p. 95** ; la leçon 11 occupe donc 89–94.
- Tableau de l'exercice 6 p. 93 : chiffres inversés / unités mêlées (détail ci-dessus) — **à ne pas reprendre**.
- Document p. 94 : diamètre « لا يتعدّى 10⁻¹⁰ m » incompatible avec les valeurs du manuel.
- Couleur de l'atome d'azote non définie avant l'exercice p. 91.
- Mot « جزيئات » employé pour « particules » (constituants de la هباءة), pas au sens de « molécule » — attention à la traduction.

### Vocabulaire officiel
الذرّة / الذرّات، الهباءة / الهباءات، جزيئات مجهريّة، النموذج الهبائي / النماذج الهبائيّة، كويرة (سوداء، حمراء، بيضاء، صفراء، خضراء)، العين المجرّدة، المجهر البصري، الجسم النقيّ البسيط، الجسم النقيّ المركّب، الذّريّة، الأوزون، الكلور، الأزوت، النشادر، ثاني أكسيد الكبريت، الإيتان، الأسيتيلين، الكحول الأثيلي، العناصر، atomos، تفكيك، تثبيت.

### Leçon 12 — « بنية الذّرّة » (ص 95–98)

محور : **المادّة في الطبيعة** — باب : **الذرّة والاحتراق**. Séance documentaire (icône livre). ⚠ La خريطة (p. 5) annonce la leçon **p. 96** ; elle commence en réalité **p. 95**. Sous-parties : « حجم الذرّة وكتلتها » (p. 95–96), « مكوّنات الذرّة » (p. 96–98).

### Objectifs (خريطة p. 5)
- التمييز بين مكوّنات الذرّة.

### Déroulé
1. **حجم الذرّة وكتلتها — أتأمّل وأتساءل (p. 95)** : « بما أنّ الهباءة متكوّنة من مجموعة ذرّات فإنّه من البديهيّ أن تكون الذرّة أصغر من الهباءة، ولكن كيف السبيل إلى معرفة حجمها وكتلتها ؟ »
   - **أبحث وأتأكّد (p. 95)** — verbatim : « بالقيام ببحث وثائقي في الغرض (على شبكة الواب، في المكتبات...) يظهر أنّه لكوْن الذرّة جسيْمٌ صغير جدّا لم يتأكّد الباحثون من وجوده إلاّ باستعمال مِجهَر إلكترونيّ خاصّ يتميّز بقدرته على مضاعفة الحجم الحقيقيّ بما قدره 50 مليون مرّة، كما يتّضح أنّ ذرّات العنصر الواحد (الأكسيجين مثلا) متطابقة في الحجم والكتلة ولكنّها تختلف قليلا عن ذرّات عنصر آخر (الكربون مثلا)، ولكن في كلّ الحالات لا يتجاوز قطر الذرّة الواحدة بعضَ أعشار النانومتر (nm)* ،أي بعض أعشار الجزء المليار من المتر. أمّا الكتلة فهي متناهية في الصغَر وتقَدَّر ببعض الآحاد لـ 10⁻²⁶ kg » ; « * 1 nm = 10⁻⁹ m ». Photo : « صورة لذرّات تنقستان أخذت بمجهر إلكتروني ».
   - **أمثلة (tableau p. 95)** :

     | الذرّة | الهيدروجين | الأكسيجين | الكربون | الحديد | الرّصاص |
     |---|---|---|---|---|---|
     | قطرها (nm) | 0,11 | 0,14 | 0,15 | 0,23 | 0,3 |
     | كتلتها (10⁻²⁶ kg) | 0,2 | 2,7 | 2,0 | 9,3 | 34,5 |

   - **ملاحظة** : « ذرّة الهيدروجين هي أصغر وأخفّ ذرّة وذرّة الحديد هي من الحجم المتوسّط، أمّا ذرّة الرصاص فهي من الذرّات الكبيرة والثقيلة. »
   - Vérif. (valeurs de référence) : m(H)=0,167 ; m(C)=1,99 ; m(O)=2,66 ; m(Fe)=9,27 ; m(Pb)=34,4 (×10⁻²⁶ kg) → tableau cohérent à l'arrondi (0,2 pour H). Ces données permettent de **corriger le tableau fautif de l'exercice 6 p. 93** (voir L11).
2. **مكوّنات الذرّة — أتأمّل وأتساءل (p. 96)** : « عند كهربة قضيب من الزجاج بالاحتكاك أعلم أنّ قطعة الحرير التي استعملت للتدليك تتكهرب كذلك باكتساب شحنة كهربائيّة سالبة عليها ولكن بم أفسّر علامتها المقابلة لعلامة الشحنة التي تظهر على قضيب الزجاج ؟ » (renvoi à l'électrisation — leçons 5–7).
   - **أبسط فرضيات (p. 96)** — verbatim : « بما أنّ التكهرب لم يغيّر طبيعة المادّة حيث بقيَ زجاج القضيب المدلوك زجاجا والحرير حريرا يمكن أن أجزم أنّه لم يطرأ أيّ تغيير سواء في تركيبة الزجاج أو في تركيبة الحرير. إذن يمكن أن أفترض انّ الذرّة نفسها تحوي على الأقلّ نوعين اثنين من الجسيمات: جسيمات تحمل شحنة كهربائيّة موجبة وأخرى تحمل شحنة كهربائيّة سالبة مقابلة للأولى وهذا ما يفسّر التعادل الكهربائي للمادّة. بتأثير الاحتكاك إمّا أن تكون قطعة الحرير قد انتزعت من ذرّات الزجاج بعض الشحنات السالبة وإمّا أن يكون قضيب الزجاج قد انتزع بعض الشحنات الموجبة من ذرّات قطعة الحرير، وفي كلا الحالتين النتيجة واحدة حيث يصير قضيب الزجاج حاملا لشحنة كهربائيّة موجبة وتصبح قطعة الحرير حاملة لشحنة كهربائيّة سالبة. »
   - **أبحث وأتأكّد — وثيقة « مكونات الذرة » (p. 97–98)** (« من موسوعة التطبيقات العلمية الميسَّرة بتصرّف ») : points clés verbatim/quasi-verbatim — atomes visibles seulement au « مِجهَر المسح الإلكترونيّ » ; « فالنقطة في نهاية هذه الجملة وحدَها قد تحوي أكثر من مِلياريْ ذرّة » ; Grecs « منذ أكثر من ألفَي سنة » : « الجوهر الذي لا يتجزّأ » ; **1804** : « أعلن الكيميائي الإنقليزي جون دالتون (Dalton) نظريّته القائلة إنّ جميع الذرّات في العنصر الواحد ... متطابقة تماما لكنّها تختلف عن ذرّات أي عنصر آخر » ; **1897** : ج.ج. طومسون « اكتشاف جسيْمات دقيقة ، أخفّ 1836 مرّة من أصغر ذرّة معروفة وهي ذرّة الهيدروجين، سمّيَت الواحدة منها إلكترون لأنّها تحمل شحنة كهربائية » ; modèle « حبّات الزبيب على قرص الحلوى » ; **1911** : « إرنسْت رذرفورد (Ernest Rutherford) النّيوزيلَنْدي المَوْلدِ : أنّ الذرّة تتكوّن من نواة مركزية عالية الكثافة تدور حولها الإلكترونات في شبه غمامة ضخمة نسبيا خوائية في معظَمها ... تتركّز فيها غالبيّة كتلتها » ; « بعد عاميْن فقط » : « نيلْز بور (Niels Bohr) » — électrons « تدوّم حول النواة المشحونة إيجابا في مدارات محدَّدة ... تنتظم في طبقات أو غلافات كما في الكرُمْب » ; aujourd'hui : « نواة حاملة لشحنة كهربائية موجبة ومجموعة من الإلكترونات حاملة لشحنة جمْلِية مقابلة للأولى. تحوز النواة مركز الذرّة وتتركّز فيها معظم كتلتها ... حيث يبلغ قطرها 1 على 100000 من قطر الذرّة. أمّا عن الإلكترونات فلقد اتّضح أنّه يستحيل التعرّف إلى طبيعة حركتها حول نواة الذرّة بل لا يمكن إلاّ تقدير مدى احتمال وجود الإلكترون الواحد منها بنقطة ما حول النواة في لحظة معيَّنة. »
     - Vérif. : 1836 ≈ m(H)/mₑ (1,67×10⁻²⁷ / 9,11×10⁻³¹ ≈ 1833) ✔ ; 1911 + 2 = 1913 (Bohr) ✔.
   - **أستغلّ النصّ (p. 98)** : 1. أحدّد المفاهيم التي وردت في النصّ بشأن الذرّة. 2. أبحث عن الأسباب التي حالت دون تبنّي العلماء لمفهوم واحد للذرّة عبر التاريخ. 3. أتثبّت من المكوّنات والخاصيات التي اتّفق حولها العلماء في هذا العصر بشأن الذرّة. 4. أتبيّن المفاهيم القديمة التي يتفق معها المفهوم الحالي في طبيعة مكوّنات الذرّة وأحدّد نقاط الاختلاف. 5. أتعرّف إلى الجسيمات القابلة للاقتلاع من الذرّة بالاحتكاك (→ الإلكترونات). 6. أبيّن أنّ انتزاع الشحنات السالبة هو الافتراض الصحيح لتفسير تكهرب الزجاج بالاحتكاك (→ seuls les électrons, périphériques et légers, sont arrachables ; le noyau est fixe).

### Encadrés أستنتج — VERBATIM
**p. 96**
> **لا يتجاوز قطر الذرّة بعضَ أعشار النانومتر أمّا كتلتها فتراوح حسب طبيعتها بين العُشُرَين وبعض الآحاد من القيمة 10⁻²⁶ kg**

**p. 98**
> ◄ **الذرّة متكوّنة من نواة مركزيّة موشّحة بمجموعة من الإلكترونات في حركة عشوائيّة دائمة حولها.**
> ◄ **كلّ الإلكترونات متطابقة إلاّ أنّ عددها هو الذي يختلف من مادّة إلى أخرى فهو إذن خاصيّة من خاصيّات الذرّة.**
> **للإلكترون الواحد كتلة صغيرة جدّا تساوي: mₑ = 9,11 . 10⁻³¹ kg.**
> ◄ **رغم أنّ قطر نواة الذرّة أصغر مائة ألف مرّة من قطر الذرّة نفسها فكتلة النواة هي نفسها كتلة الذرّة وذلك لأنّ كتلة ألالإلكترونات مجمّعة قابلة للإهمال أمام كتلة النواة.**
> ◄ **للنواة شحنة كهربائيّة موجبة ولكلّ إلكترون شحنة سالبة مقابلة للشحنة الكهربائيّة البسيطة : q = -e**
> ◄ **الذرّة متعادلة كهربائيّا لأنّ جملة شحنة إلكتروناتها مقابلة لشحنة نواتها.**
> ◄ **النواة بكتلتها و شحنتها الكهربائيّة خاصيّة أخرى للذرّة.**

Formules/symboles/unités : **nm** (1 nm = 10⁻⁹ m), **kg** (10⁻²⁶ kg), **mₑ = 9,11 . 10⁻³¹ kg**, **q = -e** (e = « الشحنة الكهربائيّة البسيطة » ; sa valeur **e = + 1,6.10⁻¹⁹ C** n'est pas rappelée ici — elle figure p. 64, leçon 7), **C** (coulomb, exercice). Rapport noyau/atome : 1/100000 (« أصغر مائة ألف مرّة »).
Coquille dans l'encadré : « كتلة ألالإلكترونات ».

### Exercices
- **أقيّم مكتسباتي (p. 96)** : « مع العلم أنّ الشرار المتطاير من نار الحطب عبارة عن حبّات كربون صغيرة ذات قطر يساوي 0,2 mm 1. أبحث عن عدد الذرّات المكوّنة لحبّة الكربون إذا اعتبرت أنّها متراصّة. 2. أحتسب كتلة حبّة الكربون. » (données à prendre dans le tableau p. 95 : d(C) = 0,15 nm, m(C) = 2,0×10⁻²⁶ kg)
  - ⚠ **Ambigu** : « عدد الذرّات ... متراصّة » — nombre d'atomes alignés sur un diamètre, ou dans tout le volume ? Aucune méthode (rapport de volumes, compacité) n'est enseignée.
  - Calcul (fractions) : rapport des diamètres = 0,2×10⁻³ / 0,15×10⁻⁹ = 4 000 000/3 ≈ **1,33×10⁶** (atomes alignés sur un diamètre). Par rapport des volumes (sphère/sphère, sans compacité) : (4×10⁶/3)³ ≈ **2,37×10¹⁸** atomes. Masse correspondante : 2,37×10¹⁸ × 2,0×10⁻²⁶ ≈ **4,74×10⁻⁸ kg** (≈ 0,047 mg). La question 2 n'a de sens qu'avec l'interprétation volumique.
- **أقيّم مكتسباتي (p. 98)** : « أبحث عن عدد إلكترونات ذرّة الكلور مع العلم أنّ شحنة نواتها تساوي 27.10⁻¹⁹ C . »
  - Calcul : n = 27×10⁻¹⁹ / 1,6×10⁻¹⁹ = 135/8 = **16,875** → non entier ; réponse attendue **17** (Z(Cl) = 17 ; 17 × 1,6 = 27,2). ⚠ Donnée arrondie (27 au lieu de 27,2) → quotient non entier : à signaler.
  - ⚠ La valeur de e n'est pas redonnée dans la leçon 12 (seulement « q = -e ») ; il faut la reprendre de la leçon 7 (p. 64 : e = + 1,6.10⁻¹⁹ C).

### Bornes
- ✅ Ordres de grandeur : diamètre de l'atome ~ quelques dixièmes de nm ; masse entre 0,2 et quelques unités de 10⁻²⁶ kg ; tableau H, O, C, Fe, Pb.
- ✅ Structure : noyau central (+), électrons (−) en « حركة عشوائيّة دائمة » ; électrons tous identiques ; mₑ = 9,11×10⁻³¹ kg ; charge électron q = −e ; atome électriquement neutre ; noyau 100 000 fois plus petit mais porte la quasi-totalité de la masse.
- ✅ Historique (document) : Grecs, Dalton 1804, Thomson 1897, Rutherford 1911, Bohr (1913).
- ✅ Explication de l'électrisation par frottement par transfert d'électrons (charges négatives arrachées).
- ⛔ **Protons et neutrons ne sont jamais nommés** ; pas de numéro atomique Z, pas de nombre de masse, pas d'isotopes.
- ⛔ Pas de couches électroniques exploitées (le mot « طبقات أو غلافات » n'apparaît que dans le récit historique de Bohr), pas de configuration électronique.
- ⛔ Pas d'ion (réservé aux leçons 15–17 « المحاليل الشارديّة » ; hors de ma plage).
- ⛔ La formule charge du noyau = Z·e n'est pas écrite ; elle est implicite dans l'exercice du chlore.

### Incohérences
- Carte p. 5 : page 96 annoncée pour la leçon 12 ; début réel p. 95.
- p. 95 : « ذرّات العنصر الواحد ... متطابقة في الحجم والكتلة » (ignore les isotopes — simplification assumée, présentée aussi comme théorie de Dalton « مشكوك فيها » p. 97 : tension interne non résolue).
- Encadré p. 98 : « حركة عشوائيّة دائمة » vs document (Bohr, « مدارات محدَّدة ») — l'encadré tranche pour la vision moderne.
- Exercice chlore : 27×10⁻¹⁹ C / e ≠ entier.
- « الكترون » : écrit « إلكترون / الإلكترونات » ; coquille « ألالإلكترونات ».

### Vocabulaire officiel
حجم الذرّة، كتلة الذرّة، قطر الذرّة، النانومتر (nm)، مِجهر إلكتروني، مجهر المسح الإلكتروني، مكوّنات الذرّة، النواة (مركزيّة، مشحونة إيجابا)، الإلكترون / الإلكترونات، الشحنة الكهربائيّة البسيطة (e)، شحنة موجبة / سالبة، التعادل الكهربائي، متعادلة كهربائيّا، الاحتكاك، التكهرب، قضيب الزجاج، قطعة الحرير، عنصر، نظرية دالتون، طومسون، رذرفورد، بور، مدارات، طبقات / غلافات، غمامة، ذرّات تنقستان، الحديد، الرصاص.

### Leçon 13 — « رمز الذّرّة والصيَغ الكيميائيّة » (ص 100–102)

محور : **المادّة في الطبيعة** — باب : **الرّموز الكيميائيّة** (page de باب p. 99). Séance documentaire (icône livre). p. 102 : seule la moitié haute est imprimée (ملاحظة + أقيّم مكتسباتي), bas de page blanc.

### Page de باب (p. 99) — « الــرّموز الكيميــائيّة »
- Liste : « 13- رمز الذّرة والصيغ الكيميائيّة » ; « 14- معادلات التفاعلات الكيميائيّة ».
- Image : « نموذج لهباءة الأسبيرين المتكوّنة من ذرّات كربون وهيدروجين وأكسيجين ».
- Questions d'amorce : « هل هناك كتابة عمليّة لإبراز تركيبة كلّ هباءة ؟ » ; « ما المقصود بالكتابة CO₂ على لصيقة مطفأة الحرائق ؟ » ; « من المعادلات المستعملة في العلوم هناك المعادلة الرّياضيّة والمعادلة الكيميائيّة. ما الفرق بينهما ؟ »

### Objectifs (خريطة p. 5)
- ذكر رموز بعض العناصر الطبيعيّة
- كتابة صيغ بعض الأجسام النقيّة بسيطة التركيبة.

### Déroulé
1. **أتأمّل وأتساءل (p. 100)** : « ما المقصود بالكتابة CO₂ على لصيقة مطفأة الحرائق وبالكتابة H₂SO₄ على قارورة حمض الكبريتيك وبتلك الكتابات المماثلة على لصائق معلّبات الأدوية ؟ » (photo d'extincteur).
2. **أبحث وأتأكّد (p. 100–101)** — verbatim : « أدقّق النظر في الهباءات المُجسَّمة في الشكل المُقابل. لتمثيلها كتابيّا بطريقة عامّة يفهمها كلّ قارئ، أسند لكلّ منها صيغة مبنيّة على أساس أنواع الذرّات المكوّنة لها وعددها. لذلك وجب إسناد رمز عامّ لكلّ ذرّة. بالاستناد على الاصطلاح العالمي المعمول به يرمز إلى ذرّة :
   * الهيدروجين بـ **H**، وهو الحرف الأوّل من اسمه اللاتيني Hydrogène
   * الكربون بـ **C**، وهو الحرف الأوّل من اسمه اللاتيني Carbone
   * الأكسيجين بـ **O**، وهو الحرف الأوّل من اسمه اللاتيني Oxygène
   * الألومنيوم بـ **Al**، وهو ثنائي الحرفين الأوّل والثاني من اسمه اللاتيني. Aluminium
   * الكلور بـ **Cl**، وهو ثنائي الحرفين الأوّل والثالث من اسمه اللاتيني Chlore ، وذلك لتفادي الخلط مع رمز ذرّة الكربون.
   هكذا أسند إلى هباءتي الميتان والايتان المتكوّنتين كلّ منهما من ذرّات الكربون والهيدروجين نفس الصيغة الأوّلية CH. وللتمييز بينهما أرفق كلّ رمز على يمينه وفي الأسفل بعدد الذرّات الموجودة في الهباءة وبالتالي، أتحصّل على الصيغة النهائيّة **CH₄** للميتان و **C₂H₆** للإيتان. »
   - **ملاحظة (p. 100)** : « بالنسبة إلى هباءة الميتان، أكتب الصيغة CH₄ بدلا من C₁H₄ وهذا يُعمَّم على جميع أنواع الذرّات أحاديّة العدد في هباءة ما. »
   - (p. 101) « بِتوخّي نفس التمشّي أحصل على الصيغة : * **O₃** لهباءة غاز الأوزون. * **H₂O** لهباءة الماء * **HCI** [sic] لهباءة حامض الكلورهيدريك. » Modèles illustrés en marge : O₃, H₂O, HCl (vert + blanc), CH₄, C₂H₆.

### Encadrés أستنتج — VERBATIM (p. 101–102)
> ◄ **يُرمز للذرّة بالحرف الأوّل من اسمه اللاتيني، ونلجأ أحيانا إلى إضافة الحرف الثاني لنميّز بين ذرّتين يبدأ اسماهما بنفس الحرف.**
> **أمثلة :**

| الذرّة — اسمها | هيدروجين | أكسيجين | كربون | كبريت | فليور | حديد |
|---|---|---|---|---|---|---|
| اسمها اللاّتيني | Hydrogène | Oxygène | Carbone | Soufre | Fluor | Fer |
| رمزها | H | O | C | S | F | Fe |

| الذرّة — اسمها | ألومنيوم | نحاس | كلور | كلسيوم | صوديوم | أزوت |
|---|---|---|---|---|---|---|
| اسمها اللاّتيني | Aluminium | Cuivre | Chlore | Calcium | Natrium | Nitrogène |
| رمزها | Al | Cu | Cl | Ca | Na | N |

> ◄ **تُبنَى صيغة الهباءة بكتابة رموز الذرّات المُكوّنة لها مع إرفاق كلّ رمز على اليمين وفي الأسفل بعدد الذرّات الّتي يمثّلها والموجودة في الهباءة.**
> **أمثلة :**

| الهباءة | غاز الأكسيجين | غاز الهيدروجين | الماء | الميتان | ثاني أكسيد الكربون |
|---|---|---|---|---|---|
| مكوّناتها | ذرّتان من الأكسيجين | ذرّتان من الهيدروجين | ذرّة أكسيجين وذرّتا هيدروجين | ذرّة كربون وأربع ذرّات هيدروجين | ذرّة كربون وذرّتا أكسيجين |
| صيغتها | O₂ | H₂ | H₂O | CH₄ | CO₂ |

> **ملاحظة : لا يكتب عدد الذرّات في صيغة الهباءة إلاّ إذا كان عددها يُساوي أو يفوق الاثنين.** (p. 102, en rouge = règle officielle)

Symboles introduits (12) : **H, O, C, S, F, Fe, Al, Cu, Cl, Ca, Na, N**. Formules écrites : **CO₂, H₂SO₄, CH₄, C₂H₆, O₃, H₂O, HCl (imprimé « HCI »), O₂, H₂**. Convention de l'indice : « على اليمين وفي الأسفل ».

### Exercices — أقيّم مكتسباتي (p. 102)
1. « علما أنّ هباءة غاز البوتان تتكوّن من أربع ذرّات كربون وعشر ذرّات هيدروجين. ما هي صيغتها ؟ » → **C₄H₁₀**.
2. « أكمل كتابة الصيغة C… H… O… الخاصّة بهباءة الكحول الأثيلي (الكحول الصيدلي) المتكوّنة من ستّ ذرّات هيدروجين وذرّتَي كربون وذرّة أكسيجين واحدة. » → **C₂H₆O** (le gabarit impose l'ordre C, H, O ; la formule semi-développée C₂H₅OH n'est pas attendue).
3. « بما أنّ صيغة هباءة حامض الكبريتيك هي H₂SO₄ ، أحدّد أنواع الذرّات المكوّنة لها وعدد كلّ منها. » → 2 H, 1 S, 4 O (atomicité 7).

### Bornes
- ✅ Symbole = 1ʳᵉ lettre majuscule du nom « latin », + une 2ᵉ lettre minuscule si ambiguïté ; 12 symboles officiels.
- ✅ Formule d'une هباءة = symboles + indice en bas à droite ; indice 1 non écrit.
- ✅ Distinction « الصيغة الأوّلية » (CH) / « الصيغة النهائيّة » (CH₄, C₂H₆) — terminologie propre au manuel.
- ⛔ Pas de tableau périodique, pas de numéro atomique, pas de masse molaire.
- ⛔ Pas d'ions ni de formules ioniques ; pas de règle d'ordre des symboles dans une formule (l'ordre est seulement montré).
- ⛔ Pas de coefficient (réservé à la leçon 14) ; pas de règle de valence.
- ⛔ Le mot « عنصر » (objectif « رموز بعض العناصر الطبيعيّة ») n'est pas défini dans la leçon : le texte parle de « رمز الذرّة ».

### Incohérences
- **« اسمه اللاتيني »** : les noms donnés sont **français** (Hydrogène, Oxygène, Carbone, Soufre, Fer, Cuivre, Chlore, Calcium…) sauf **Natrium** (latin) ; « **Nitrogène** » n'est ni français (azote) ni latin (nitrogenium). Fe/Cu viennent en réalité du latin *ferrum/cuprum* (la règle fonctionne ici par coïncidence avec Fer/Cuivre) ; Na ne s'explique qu'avec « Natrium ».
- Encadré « إضافة **الحرف الثاني** » vs exemple **Cl** = « الحرفين الأوّل **والثالث** » (p. 100) : contradiction interne.
- **« HCI »** : imprimé avec un **I majuscule** (confirmé dans la couche texte du PDF) au lieu de **HCl**.
- « حمض الكبريتيك » (p. 100) / « حامض الكبريتيك » (p. 102) ; « حامض الكلورهيدريك » : alternance حمض / حامض.
- Mise en page de « H₂O » dans le tableau p. 101 : indice décalé sous le H (« H₂O » lisible mais mal placé).
- « فليور » (fluor) : graphie à noter.

### Vocabulaire officiel
رمز الذرّة، الرّموز الكيميائيّة، الصيغة الكيميائيّة، صيغة الهباءة، الصيغة الأوّلية، الصيغة النهائيّة، الاصطلاح العالمي، الاسم اللاتيني، عدد الذرّات، على اليمين وفي الأسفل، أحاديّة العدد، الأوزون، حامض الكلورهيدريك، حمض/حامض الكبريتيك، الكحول الأثيلي (الكحول الصيدلي)، البوتان، الإيتان، الأسبيرين، هيدروجين، أكسيجين، كربون، كبريت، فليور، حديد، ألومنيوم، نحاس، كلور، كلسيوم، صوديوم، أزوت.

### Leçon 14 — « معادلات التفاعلات الكيميائيّة » (ص 103–109)

محور : **المادّة في الطبيعة** — باب : **الرّموز الكيميائيّة**. Séance expérimentale (icône télescope). Sous-parties : « التفاعل الكيميائيّ وحفظ المادّة » (p. 103–104), « معادلة التفاعل الكيميائي » (p. 104–105), « الخلاصة » (p. 105) ; « أعوّل على نفسي » p. 106–107 ; « هل من مزيد ؟ — نموذج الذرّة » p. 108 ; « أتسلّى » p. 108–109 ; « أستعين بعناوين » p. 109 (fin du باب).
Pages 110–112 (hors leçon, lues) : p. 110 page du باب suivant « المحاليل الشاردية » (تركيبة المحلول الشاردي / المحاليل الحامضيّة والمحاليل القلويّة / المحاليل المتعادلة) ; p. 111 « مكتسباتي القبليّة » (المعارف 1–11 : المزيج، الأجسام النقيّة البسيطة والمركّبة، الانحلال، المحل، المحلول، التركيز، الانحلاليّة، المحلول المشبّع، التفاعل الكيميائي، الهباءة والذرّة، رموز الذرّات ; المهارات 1–5 dont « 5- أكتب معادلات تفاعلات كيميائيّة بسيطة. ») ; p. 112 page « تركيبة المحلول الشاردي » (leçons 15 ناقليّة المحاليل المائيّة للكهرباء، 16 تأثير التركيز على ناقليّة المحلول الشاردي للكهرباء، 17 الأنيونات والكتيونات ; questions : ماء شروب خال من النّيترات ؟ تربة تفتقر إلى الحديد ؟ الأسمدة الأزوتيّة والفسفاطيّة ؟). Ces pages relèvent de la partie suivante.

### Objectifs (خريطة p. 5)
- تجسيم التفاعلات الكيميائيّة بمعادلات كيميائيّة
- موازنة معادلة تفاعل كيميائي.

### Déroulé
1. **أتأمّل وأتساءل (p. 103)** : « مثّلتُ الذرّةَ برمز والهباءةَ بصيغة. إذن كيف لي أن أمَثّلَ تحوّلا كيميائيّا ؟ »
2. **التفاعل الكيميائيّ وحفظ المادّة — أجرّب وألاحظ (p. 103)** : matériel « ميزان إلكتروني ( ميزان روبرفال إن تعذّر ذلك) ; كأسا اختبار ; محلول مائي لكبريتات النحاس ; محلول مائي للصودا ». Protocole : « أسكب قليلا من المحلول المائي لكبريتات النحاس في كأس اختبار وقليلا من محلول مائي للصودا في الكأس الثانية. أتثبت من أنّ المقياس الرقميّ للميزان الإلكتروني معدّل على الصفر ثمّ أضع الكأسين الحاوتين للمحلولين على كفّته وأقرأ الكتلة الجمليّة لحمولة الكفّة. أسكب بتُؤدَة محتوى كأس في الكأس الأخرى فألاحظ ظهور راسب أزرق اللون بمجرّد مزج المحلولين معًا. أقرأ من جديد القيمة العدديّة للكتلة الجمليّة وأقارنها بالقيمة العدديّة السّابقة. » Schéma : balance « 00,00g » (tarée) → **200,0g** avant → **200,0g** après (précipité bleu). Écart = 0 g.
   - **أحلّل وأفسّر** — verbatim : « * أفسّر ظهور الراسب الأزرق اللون بحدوث تفاعل كيميائي بين محلولَيْ الصودا وكبريتات النحاس. * التساوي بين القيمتين العدديّتين للكتلة الجمليّة لحمولة كفّة الميزان قبل التفاعل وبعده يدلّ على أنّ التفاعل الكيميائي الذي حدث لم يتسبّب في تغيير كتلة المادّة المتفاعلة. وبما أنّ المادّة متكوّنة من ذرّات يمكن لي أن أجزم أنّ التفاعل الكيميائي الذي حدث لم يتسبّب في تغيّر العدد الجملي للذرّات المكوّنة لكميّة المادة المتفاعلة. »
3. **معادلة التفاعل الكيميائي — أبحث وأتأكّد (p. 104–105)** : « أتزوّد بنماذج هبائيّة. بالرجوع إلى الدرس العاشر حول التفاعل الكيميائي، أجسّم احتراق الميتان باستعمال النماذج الهبائيّة. » Bilan en mots : **ميتـان + أكسيجين ⟵ ثاني أكسيد الكربون + ماء** + modèles (1 CH₄ + 1 O₂ → 1 CO₂ + 1 H₂O).
   - « باستعمال الصيغ الكيميائيّة يمكن لي إذن تمثيل هذا التفاعل بالمعادلة التالية : **CH₄ + O₂ ⟶ CO₂ + H₂O** ولكن هل هذا يعني أنّ احتراق هباءة الميتان يتطلب هباءة أكسيجين واحدة ؟ إذا كان الأمر كذلك فإنّ مبدأ حفظ المادّة لم يُحترم، فما هو إذن العدد المناسب من هباءات الأكسيجين لاحتراق هباءة واحدة من الميتان ؟ »
   - « أفكّك نموذجَيْ هباءة الميتان وهباءة الاكسيجين وأبحث كيف أحصل على نموذَجيْ هباءتيْ المنتجين (ثاني اكسيد الكربون والماء) باستعمال نماذج الذرّات المفكّكة » ; figure « نماذج الذرّات النّاتجة عن تفكّك هباءتي الميتان والأكسيجين » (1 C, 2 O, 4 H) → soit CO₂ + 4 H libres, soit C + 2 H₂O (« أو ») : impossible d'obtenir les deux produits.
   - (p. 105) « ألاحظ أنّه لا يمكن الحصول على نموذجيْ المنتجين معًا إلاّ إذا سلّمت باستعمال نموذجيْ هباءتَيْ الأكسيجين مع نموذج هباءة الميتان. » Modèles : CH₄ + 2 O₂ → CO₂ + 2 H₂O. « وهذا يعني انّ احتراق هباءة واحدة للميتان يتطلّب التفاعل مع هبائتيْ أكسيجين لذا وجبت موازنة المعادلة الممثلة لاحتراق الميتان كما يلي : **CH₄ + 2O₂ ⟶ CO₂ + 2H₂O** ألاحظ أنّه بتساوي عدد كلّ نوع من الذرات قبل التفاعل (من خلال عدد هباءات المتفاعلين) وبعده (من خلال عدد هباءات المنتجين) تحقّق توازن المعادلة. »
   - Vérif. : C 1=1 ; H 4 = 2×2 ; O 2×2 = 2+2 ✔.

### Encadrés أستنتج / الخلاصة — VERBATIM
**p. 104 — مبدأ حفظ المادّة**
> **أثناء كلّ تفاعل كيميائي تُحفَظ المادّة المتفاعلة، وبالتالي يُحفَظ العدد الجملي للذرّات المكوّنة لتلك المادّة.**

**p. 105**
> **يُمثَّل كلّ تفاعل كيميائي بمعادلة متوازنة تُعتَمد في كتابتها الصيغ الكيميائية للمتفاعلات والمُنتجات.**
> **لا تكون معادلة التفاعل الكيميائي متوازنة، إلاّ إذا احتُرِم في كتابتها مبدأ حفظ المادّة.**

**p. 105 — الخلاصة (bilan du باب, encadré rose)**
> ◈ **بهدف الاستغلال المريح لمفهوم الذرّة في دراسة التفاعلات الكيميائية :**
> **1- يُسنَد إلى كلّ نوع من الذرّات رمز خاصّ به يتمثّل عادة في الحرف الأوّل (مع إضافة الحرف الثاني أو الثالث في بعض الحالات) من اسمه اللاتيني.**
> **2 - تُمثَّلُ كلّ هباءة بصيغة يُرَاعى فيها أنواع الذرّات المكوّنة لها وعدد كلّ منها.**
> ◈ **يستجيب كلّ تفاعل كيميائي لمبدأ حفظ المادّة.**
> ◈ **معادلة التفاعل الكيميائي أداة عمل لا تكون ناجعة إلاّ إذا كانت متوازنة.**

Formules/symboles : flèche « ⟶ », « + », **coefficients** placés devant les formules (2O₂, 2H₂O) — le mot « معامل / معاملات » **n'est jamais employé** (on parle de « عدد هباءات »). Unité : g (balance, 200,0 g).
Note : la الخلاصة rectifie l'encadré de la leçon 13 (« الحرف الثاني **أو الثالث** »).

### Exercices
- **أقيّم مكتسباتي (p. 105)** : « أكتب كتابة متوازنة لمعادلتَي الاحتراق التامّ لِـ : 1- الكربون C 2 – الايتان C₂H₆ علما أنّ منتجاته هي نفس منتجات الاحتراق التامّ للميتان. »
  - 1 : **C + O₂ ⟶ CO₂** (déjà équilibrée).
  - 2 : **2C₂H₆ + 7O₂ ⟶ 4CO₂ + 6H₂O** (vérifié : C 4=4, H 12=12, O 14=8+6). ⚠ Forme à coefficients entiers ; la forme C₂H₆ + 7/2 O₂ n'est pas enseignée — l'élève doit penser à doubler (méthode non montrée dans la leçon).
- **أعوّل على نفسي — أتمرّن على حلّ المسائل (p. 106–107)** :
  - **تمرين 1** (× devant chaque proposition correcte) : 1- « يمكن لجسمين أن يحتويا على نفس نوع الذرّات » → صحيح (ex. CO et CO₂ ; O₂ et O₃). 2- « ثاني أكسيد الكربون جسم نقيّ مركّب. » → صحيح. 3- « القيمة المطلقة لشحنة إلكترون الذرّة متساوية مع قيمة شحنة نواته. » → خطأ (charge du noyau = somme des charges des électrons ; vrai seulement pour H) — ⚠ énoncé ambigu (« إلكترون » au singulier). 4- « يُسند رمز للهباءة وصيغة للذرّة. » → خطأ (inversé). 5- « He هو رمز ذرّة الهيدروجين » → خطأ (H). 6- « لكتابة تفاعل كيميائي نستعمل معادلة كيميائيّة. » → صحيح. 7- « لا تكون معادلة التفاعل الكيميائيّ متوازنة إلاّ إذا احتُرِمَ في كتابتها مبدأ حفظ المادّة. » → صحيح (verbatim de l'encadré). 8- « الذرّة أصغر من الهباءة. » → صحيح en général (⚠ pour une هباءة monoatomique comme « هباءة الكربون » p. 89, atome = هباءة).
  - **تمرين 2** (QCM) : 1- هباءة ثاني أكسيد الكربون تتكوّن من : 1) ثلاث ذرّات متطابقة 2) ذرّة أكسيجين وذرّتَيْ كربون 3) ذرّة كربون وذرّتَيْ أكسيجين → **3**. 2- « هباءة ثاني أكسيد الكربون وهباءة أحادي أكسيد الكربون لهما نفس » : 1) عدد الذرّات 2) نوع الذرّات 3) الكتلة → **2** (CO₂ : 3 atomes, CO : 2). ⚠ « أحادي أكسيد الكربون » (CO) n'a jamais été présenté dans les leçons 10–14. 3- « هباءة ثاني أكسيد الكربون وهباءة الماء لهما نفس » : 1) عدد الذرّات 2) نوع الذرّات 3) الكتلة → **1** (3 atomes chacune ; masses 44 u vs 18 u).
  - **تمرين 3** (équilibrer ; tableau p. 107, cases « .... ») — réponses vérifiées par comptage d'atomes :
    1. C₃H₈ + 5O₂ ⟶ 3CO₂ + 4H₂O
    2. 6HCl + 2Al ⟶ 3H₂ + 2AlCl₃
    3. N₂ + 2O₂ ⟶ 2NO₂
    4. H₂S + Cl₂ ⟶ 2HCl + S
    5. CH₄ + 2Cl₂ ⟶ 4HCl + C
    - ⚠ **Typographie fautive** (confirmée dans la couche texte du PDF) : « HCI », « AI », « AICI₃ », « CI₂ » imprimés avec un **I majuscule** au lieu de **l** minuscule (Cl, Al). Symboles Al et Cl pourtant enseignés p. 100–101. À ne pas reprendre.
  - **تمرين 4** (classer simple/composé avec justification) : الأكسيجين O₂ → بسيط ; البروبان C₃H₈ → مركّب ; الإيوْد I₂ → بسيط ; كلورير الألومنيوم « AICI₃ » [= AlCl₃] → مركّب ; كحول الصيدليّة C₂H₆O → مركّب. ⚠ Symbole **I** (iode) jamais introduit dans la leçon 13 ; même coquille AICI₃. ⚠ AlCl₃ est un composé ionique : parler de « هباءة » est un abus (non signalé par le manuel).
  - **تمرين 5** (tableau الجسم النقيّ / نموذجه الهبائي / صيغة الهباءة ; « الكويرة الرماديّة تمثّل في النماذج الهبائيّة ذرّة الهيدروجين والكويرة السوداء ذرّة الكربون والكويرة الحمراء ذرّة الأكسيجين ») : 1- simple ou composé ; 2- écrire la formule. → أسيتيلين **C₂H₂** (مركّب) ; ميتان **CH₄** (مركّب) ; ايتان **C₂H₆** (مركّب) ; كحول **C₂H₆O** (مركّب). ⚠ L'hydrogène est dit ici « رماديّة » alors que p. 89 il est « كويرة بيضاء » : incohérence de code couleur.
- **هل من مزيد ؟ — نموذج الذرّة (p. 108)** — encadrés historiques (verbatim résumé) :
  - « في أوائل منتصف القرن الخامس قبل الميلاد أقرّ الفيلسوفان اليونانيان لوسيب وأفلاطون بأنّ المادّة قابلة للتقطّع إلى حدّ الحصول على جزيء غير قابل للتجزء ويسمّى أطوموس (ويعني لا انقساميّة باليونانيّة) »
  - « في أواخر منتصف القرن الخامس قبل الميلاد، وقع الاستغناء عن نظرية لوسيب وأقرّ الفيلسوف اليوناني أرسطو بأنّ المادّة تتكوّن من أربع عناصر وهي الأرض والماء والنار والهواء. »
  - « في سنة 1803 وبعد دراسة علميّة، أقرّ جون دلتون بوجاهة نظريّة أفلاطون فوقع التراجع عن نظرية أرسطو ومثّلت الذرّة على شكل كويرة. »
  - « في سنة 1913 مثّل نيلس بوهر الذرّة بالجسم المتكوّن من نواة حاملة لشحنة موجبة ومن مجموعة ألكترونات في حالة دوران متواصل حول النواة على مدرات محدودة وذات أقطار محدّدة جدّا، ويُعرف هذا النموذج بنموذج بوهر. »
- **أتسلّى (p. 108–109)** : 1. كلمات متقاطعة — définitions : ◄1 « تتفاعل معًا » (donné : **متفاعلات**) ; ▼2 « تكُونُ عليها معادلة كيميائيّة » ; ◄3 « تُمثّلُ تفاعلا كيميائيّا » ; ▼4 « تحوّلٌ تختفي إثره أجسام و تَظهر أجسام جديدة. » ; ▼5 « تنتج عن تفاعل كيميائي » ; ◄6 « تتكوّن من عدد محدود من الذرّات » ; ▼7 « أصغر جسيم يكوّن المادّة ». Solution reconstituée à partir de la grille : 2 **متوازنة**, 3 **معادلة**, 4 **تفاعل**, 5 **منتجات**, 6 **هباءة**, 7 **ذرّة** (croisements cohérents). 2. « من هو صاحب الصورة ؟ هو عالم تصوّر أنّ الذرّة لا تتجزّأ » : cases I=و, II=ت, III=ن, IV=د, V=ل ; ordre imprimé (lecture RTL) IV V II I III → **دلتون** ✔.
- **أستعين بعناوين (p. 109)** : liste d'URL par thème (المحروقات، النفط ومشتقّاته، الغاز الطّبيعي، الكربون، الذرّة، تاريخ الذرّة في صور، التفاعلات الكيميائيّة) — sites anciens (probablement morts), à ne pas reprendre.

### Bornes
- ✅ **مبدأ حفظ المادّة** (conservation de la masse ⇒ conservation du nombre total d'atomes de chaque sorte), démontré par la pesée CuSO₄ + soude (200,0 g → 200,0 g).
- ✅ Équation chimique avec formules ; **équilibrage** par ajustement du nombre de هباءات ; exemple de référence CH₄ + 2O₂ → CO₂ + 2H₂O.
- ✅ Équilibrage d'équations simples (combustions d'hydrocarbures, HCl + Al, N₂ + O₂, H₂S + Cl₂, CH₄ + Cl₂).
- ⛔ Le mot « معامل » (coefficient stœchiométrique) n'apparaît pas ; pas de coefficients fractionnaires ; pas de méthode algorithmique d'équilibrage.
- ⛔ Pas d'états physiques (s), (l), (g), (aq) dans les équations.
- ⛔ Le nom de Lavoisier n'est pas cité ; le précipité bleu n'est pas nommé (hydroxyde de cuivre) et son équation n'est pas écrite.
- ⛔ Pas de notion de mole ni de calcul de masses à partir de l'équation.

### Incohérences
- Symboles « AI, HCI, CI₂, AICI₃ » (I majuscule au lieu de l) — exercices 3 et 4 p. 107.
- Symbole **I** (iode) et corps **CO** (أحادي أكسيد الكربون) utilisés sans avoir été enseignés.
- Couleur de l'hydrogène : « رماديّة » (p. 107) vs « بيضاء » (p. 89).
- Historique : Dalton **1803** (p. 108) vs **1804** (p. 97) ; « لوسيب وأفلاطون » partisans de l'atome (historiquement Leucippe et **Démocrite** ; Platon n'était pas atomiste) ; « أرسطو ... أواخر منتصف القرن الخامس قبل الميلاد » (Aristote est du IVᵉ s. av. J.-C.) ; « دلتون بوجاهة نظريّة أفلاطون » repose sur la même confusion ; « ألكترونات / مدرات » (coquilles). Contenu « هل من مزيد » non fiable pour des questions factuelles.
- « الحاوتين » (p. 103) pour « الحاويتين » ; « هبائتيْ » (p. 105) pour « هباءتيْ ».
- Titre p. 103 : icône expérimentale ✔ ; la خريطة place bien la leçon 14 p. 103.

### Vocabulaire officiel
معادلة التفاعل الكيميائي، المعادلة الكيميائيّة، معادلة متوازنة، موازنة المعادلة، توازن المعادلة، مبدأ حفظ المادّة، العدد الجملي للذرّات، الكتلة الجمليّة، ميزان إلكتروني، ميزان روبرفال، كفّة الميزان، معدّل على الصفر، كبريتات النحاس، الصودا، راسب أزرق اللون، المتفاعلات، المنتجات، النماذج الهبائيّة، تفكيك، أحادي أكسيد الكربون، الأسيتيلين، البروبان، الإيود، كلورير الألومنيوم، كحول الصيدليّة، نموذج بوهر، أطوموس.

### Leçon 15 — « ناقليّة المحاليل المائيّة للكهرباء » (ص 113–115)

- **محور** : المادّة في الطبيعة · **باب** : المحاليل الشارديّة (خريطة الكتاب p. 5).
- Type de séance (pictogramme de la carte) : séance expérimentale (télescope). Première leçon du باب.

### Objectifs (الأهداف — خريطة الكتاب p. 5, verbatim)
- تعريف المحلول الشاردي
- التعرّف إلى محلول شاردي

### Déroulé

**Partie 1 — « ناقليّة الماء النقيّ للكهرباء » (p. 113–114)**
- أتأمّل وأتساءل (verbatim) : « لماذا يُنصح عند تشغيل مصباح كهربائي منزلي بأن لا نلمس القاطع بيد مبلّلة ؟ »
- أجرّب وألاحظ — matériel : « جهاز تغذية (6V) – أميرمتر رقمي – محلال كهربائي – قاطع – مصباح كهربائي (6V) – أسلاك موصلة. » + « ماء نقيّ (ماء مقطّر) ».
  1. Circuit série générateur + قاطع + مصباح pour vérifier « ملاءمة المصباح للمولّد المستعمَل » (الشكل 1) → la lampe brille.
  2. On verse « 100 mL من الماء المُقطّر » dans l'électrolyseur (électrodes totalement immergées), inséré en série (الشكل 2).
  3. « أغلق الدارة، فألاحظ أنّ المصباح لا يضيء. هل هذا يعني أنّ الماء عازل للتيّار الكهربائي ؟ » → on insère l'ampèremètre numérique : « يشير إلى مرور تيّار كهربائي ضعيف جدًا في الدّارة » (الشكل 3).
  - Figure 3 : l'afficheur de l'ampèremètre montre « 343.0 » ; l'unité est minuscule, illisible même à 300 dpi (« nA » ou « µA » probable). Valeur illustrative, non exploitée dans le texte.
- **أستنتج** (verbatim) : « الماء النقيّ ناقل للتيّار الكهربائي ولكن بصعوبة. »

**Partie 2 — « قابليّة المحاليل المائيّة لنقل الكهرباء » (p. 114–115)**
- أتأمّل وأتساءل (verbatim) : « لصيانة البطاريّة، لماذا يوصي الصانع بإضافة السائل المعروف بالماء الحمضي وليس الماء العادي ؟ » ; « هل السوائل قادرة على نقل الكهرباء ؟ »
- أجرّب وألاحظ — même matériel ; « محاليل مائيّة لها نفس التركيز لـ : السكّر – الملح – كحول الصيدليّة – كبريتات النحاس. »
  - Solution de sel à la place de l'eau distillée (même volume) : « سليك المصباح يحمرّ قليلا وأنّ الأمبيرمتر يشير إلى شدّة تيّار أرفع بكثير من شدّة التيار الذي نقله الماء النقيّ » (الشكل 4 ; afficheur ≈ « 83.0 » ou « 93.0 », unité illisible).
  - Sucre, alcool pharmaceutique : courant « ضعيفة جدًّا (مثل ما هو الشأن بالنسبة إلى الماء النقيّ) » ; sulfate de cuivre : « كبيرة نسبيّا (مثل ما هو الشأن بالنسبة إلى محلول ملح الطعام) ».
- أحلّل وأفسّر (verbatim) : « خلافا لمحلولَيْ السكّر وكحول الصّيدلية، المحلول المائي لكبريتات النّحاس والمحلول المائي لملح الطّعام أقدر من الماء المقطّر على نقل التيّار الكهربائي. »
- Aucune donnée chiffrée à recalculer (seule tension : 6V pour générateur et lampe).

### Encadré أستنتج (p. 115, verbatim — contient la définition officielle)
> « المحاليل المائيّة ناقلة للتيّار الكهربائي ولكن بقابليّات متفاوتة، فمنها ما هو مثل الماء النقيّ تقريبا ومنها ما هو أقدر بكثير من الماء النقيّ على نقل التيار الكهربائي. »
> « يُنعت كلّ محلول مائي أقدر من الماء النقيّ على نقل التيّار الكهربائي بالمحلول الشاردي. »
> « أمثلة : » — flacons légendés « محلول كبريتات النّحاس » (bleu), « محلول ثاني كرومات البوتسيوم » (orange), « محلول كلورير البوتسيوم » (incolore).

Symboles/unités présents : V (volt, 6V), mL (100 mL). Aucun symbole de grandeur (pas de I, pas de G ni σ).

### Exercices
- **أقيّم مكتسباتي** (p. 115, verbatim) : « علمًا أنّ المحلول المائي لكلورير الألومنيوم محلول شاردي. أقارن قابليته مع قابلية محلول كحول الصّيدلية لنقل الكهرباء. »
  - Réponse : محلول شاردي ⇒ plus apte que l'eau pure à conduire ; l'alcool pharmaceutique conduit comme l'eau pure (très faiblement) ⇒ la solution de chlorure d'aluminium conduit beaucoup mieux que la solution d'alcool.
- Aucune autre série d'exercices (pas de أتمرّن / أجرب بنفسي dans p. 113–115).

### Bornes
- ✅ L'eau pure conduit le courant « بصعوبة » (courant très faible détecté seulement à l'ampèremètre, lampe éteinte).
- ✅ Les solutions aqueuses conduisent « بقابليّات متفاوتة » ; sucre et alcool ≈ eau pure ; sel et sulfate de cuivre bien plus conducteurs.
- ✅ Définition opérationnelle : محلول شاردي = محلول مائي أقدر من الماء النقيّ على نقل التيّار.
- ⛔ Le mot « شاردة / أيون » n'apparaît pas encore (pas d'explication microscopique de la conduction) — la définition est purement expérimentale.
- ⛔ Aucune grandeur de conductivité (ni symbole, ni unité, ni mesure chiffrée exploitée) ; les valeurs d'ampèremètre n'apparaissent que dans les figures.
- ⛔ Pas de notion de concentration chiffrée (seulement « نفس التركيز »).

### Vocabulaire officiel (équivalents français du lexique p. 211–216 : tableau en fin de L22.md — ex. Conductibilité = ناقليّة, Electrode = مَسْرى (أو إلكترود), Ionique = شاردي)
ناقليّة، محلول مائي، محلول شاردي، الماء النقيّ / الماء المقطّر، محلال كهربائي، إلكترود (« ألكترودَيْ »)، أمبيرمتر رقمي، جهاز تغذية، قاطع، مصباح، سليك المصباح، عازل، كبريتات النحاس، ملح الطعام، كحول الصيدليّة، ثاني كرومات البوتسيوم، كلورير البوتسيوم، كلورير الألومنيوم.

### Remarques de fidélité
- Orthographes du manuel : « أميرمتر » (p. 113, liste matériel) vs « أمبيرمتر » ailleurs ; « البوتسيوم » (sans ا). « أُلكترودَيْ ». À ne pas « corriger » silencieusement.
- Deux mentions de l'eau pure dans le montage : « ماء نقيّ (ماء مقطّر) » — le manuel assimile eau pure et eau distillée.

### Leçon 16 — « تأثير التركيز على ناقليّة المحلول الشاردي للكهرباء » (ص 116–117)

- **محور** : المادّة في الطبيعة · **باب** : المحاليل الشارديّة. Séance expérimentale.

### Objectifs (خريطة الكتاب p. 5, verbatim)
- مقارنة تركيزَيْ محلولين شارديّين حسب قابليّتهما لنقل الكهرباء.

### Déroulé
- أتأمّل وأتساءل (verbatim) : « لصيانة البطارية يُستعمَل محلول حامضيّ مخفّف، يُعرف بماء البطاريّة. لماذا لا يكون ذلك المحلول حامضا مركّزا أو ماء نقيّا ؟ » (photo « بطارية »).
- أجرّب وألاحظ — matériel : « جهاز تغذية (12V) – قاطع – كأس اختبار ذو سعة 100mL وإلكترودتان من الغرافيت (نوع صَلدٌ من الكربون) – محراك – مِسوَط – أسلاك موصّلة – أمبيرمتر. » ; « ماء نقيّ (ماء مقطّر) » ; « مساحيق ملح الطعام، كبريتات النحاس ونيترات البوتسيوم. »
  1. Circuit série : générateur, interrupteur, ampèremètre, électrolyseur (bécher + électrodes graphite) (الشكل 1 ; afficheur 000.0).
  2. Bécher rempli à moitié d'eau distillée : « الأمبيرمتر يشير إلى تيّار ذي شدّة I₀ صغيرة جدّا » (الشكل 2 ; afficheur 247.0, unité illisible).
  3. + une مِسوَط de sel, agitation → « شدّة تيار كهربائي I₁ أرفع من I₀ » (الشكل 3 ; afficheur 543.0).
  4. + une autre مِسوَط de sel, même volume → « شدّة تيار كهربائي I₂ أرفع من I₁ » (الشكل 4 ; afficheur 543.0).
  5. Répéter avec sulfate de cuivre, puis nitrate de potassium, « وأسجّل ملاحظاتي في كلّ مرحلة ».
- أحلّل وأفسّر (verbatim) : « كلّما زدنا من كميّة المنحلّ بدون تغيير حجم المحلول ارتفع تركيز المحلول. بالتالي أفسّر الارتفاع التدريجي لشدّة التيار الكهربائي في كلّ مرّة سواء مع ملح الطعام أو كبريتات النحاس أو نيترات البوتسيوم بالزيادة في قابليّة المحلول لنقل الكهرباء مع ارتفاع تركيزه. »
- Aucune valeur numérique à recalculer ; relation qualitative I₀ < I₁ < I₂.

### Encadré أستنتج (p. 117, verbatim)
> « تتأثّر ناقليّة المحلول المائي الشاردي للكهرباء بقيمة تركيز المحلول إذ ترتفع الناقليّة بارتفاع التركيز وتنقص بنقصانه. »

Symboles : I₀, I₁, I₂ (intensités, notées I avec indice) ; unités : V (12V), mL (100mL).

### Exercices
- **أقيّم مكتسباتي** (verbatim) : « في حوزتي قنينتان غير معنونتين تحوي واحدة منهما محلولا مشبّعا عديم اللّون والأخرى محلولا غير مشبّع من نفس النوع. أقترح تجربة أتعرّف بها إلى القنينة الحاوية للمحلول المشبّع. »
  - Réponse attendue : insérer successivement chaque solution (même volume, mêmes électrodes, même tension) dans le circuit avec ampèremètre ; la plus grande intensité ⇒ la plus concentrée ⇒ solution saturée. (Suppose implicitement un soluté ionique ; l'énoncé ne le dit pas — « من نفس النوع ».)

### Bornes
- ✅ Loi qualitative : conductivité croît avec la concentration (et décroît quand elle diminue).
- ✅ Concentration augmente quand on ajoute du soluté à volume constant (« بدون تغيير حجم المحلول »).
- ⛔ Aucune formule de concentration (pas de C = m/V ni unité g/L) ; concentration jamais chiffrée.
- ⛔ Aucune valeur d'intensité dans le texte (I₀, I₁, I₂ sont seulement comparées).
- ⛔ Pas de saturation/limite de la loi évoquée dans le cours (seulement dans l'exercice : « محلول مشبّع »).

### Vocabulaire officiel (équivalents français : tableau du lexique p. 211–216 en fin de L22.md)
تركيز، ناقليّة، محلول شاردي، منحلّ، محلول مشبّع / غير مشبّع، محلول حامضيّ مخفّف / مركّز، ماء البطاريّة، إلكترودتان من الغرافيت، محراك، مِسوَط، كأس اختبار، نيترات البوتسيوم، كبريتات النحاس، ملح الطعام، شدّة التيار.

### Incohérences / remarques
- Figures 3 et 4 : l'ampèremètre affiche la même valeur « 543.0 » alors que le texte affirme I₂ > I₁ (illustration non mise à jour).
- Figure 2 (eau pure) affiche « 247.0 », alors que le texte dit « صغيرة جدّا » — sans unité lisible, la figure est ambiguë ; ne pas en tirer de valeurs.
- Le manuel écrit « إلكترودتان » ici (p. 116) et « ألكترودَيْ » en L15.

### Leçon 17 — « الأنيونات والكتيونات » (ص 118–122)

- **محور** : المادّة في الطبيعة · **باب** : المحاليل الشارديّة. Pictogramme de la carte : livre (séance documentaire/cours), mais la leçon contient une manipulation (migration des ions sur papier filtre).
- Titre : bandeau de la leçon « الأنيونات والكتيونات » ; carte p. 6 : « الأنيونات والكتيونات ». Dans le corps du texte, le manuel écrit tantôt « كتيونات » (bandeau, أتأمّل, تمرين 1) tantôt « كاتيونات » (أستنتج, خلاصة, تمرين 2, تمرين 5) — les deux graphies coexistent.

### Objectifs (خريطة الكتاب p. 6, verbatim)
- التمييز بين الشاردة والذرّة.
- التمييز بين الأنيونات والكتيونات.

### Déroulé
- **أتأمّل وأتساءل** (verbatim) : « ما الذي يجعل المحاليل الشارديّة قادرة على نقل التيار الكهربائيّ بسهولة مقارنةً مع الماء ؟ » ; « ما هي تلك الأصناف المنعوتة بالأنيونات وبتلك الأصناف المنعوتة بالكاتيونات على علامة قارورة ماء معدني ؟ »
  - Document : étiquette d'eau minérale bilingue « خفيف و متوازن / Légère et équilibrée » (sans unité imprimée ; mg/L implicite) — الأنيونات : بيكربونات 146,0 ; كبريتات 28,0 ; كلوريدات 21,0 ; نيترات (0) ; نيتريت 0,0 ; فليووريدات 0,2 — كاتيونات : كلسيوم 32,0 ; مانيزيوم 14,6 ; صوديوم 11,4 ; بوتاسيوم 3,5 — مجموع الأملاح 200,0.
  - Recalcul (non demandé par le manuel) : Σ anions = 195,2 ; Σ cations = 61,5 ; somme = 256,7 ≠ 200,0 (« Sels totaux » = résidu sec sur l'étiquette réelle ; le manuel ne commente pas).
- **أجرّب وألاحظ** — matériel : « جهاز تغذية (24V) – قاطع – لوح زجاجي (10 cm x 15 cm) – صفيحتان من النحاس أو الزنك (3 cm x 15 cm) مجهّزة كلّ منهما بقطب كهربائي – لفيفة من ورق ترشيح ذات سمك 5 mm على الأقل (عشر طبقات من الورق تقريبا) – قطّارة – محراك – جوزتا شدّ – أسلاك موصّلة. » ; « محاليل مائيّة شارديّة مركّزة لـ : كلورير البوتسيوم (محلول عديم اللون) – كبريتات النحاس (محلول أزرق اللون) – ثاني كرومات البوتسيوم (محلول برتقاليّ اللون) – ثاني كرومات النحاس. »
  - Papier filtre imbibé de KCl sur la plaque de verre, deux lames métalliques fixées aux bords → « محلال كهربائي » (الشكل 1) ; branchement série générateur + interrupteur (الشكل 2).
  - Gouttes : sulfate de cuivre en A, dichromate de potassium en B, dichromate de cuivre en C (الشكل 3).
  - Observation (الشكل 4) : bleu de A vers « المهبط (قطبُ المحلال الموصَلُ بالقطب السالب لجهاز التغذية) » ; orange de B vers « المصعد (قطبُ المحلال الموصلُ بالقطب الموجب لجهاز التغذية) » ; depuis C : bleu vers المهبط et orange vers المصعد.
- **أحلّل وأفسّر** (p. 119–120, extraits verbatim) :
  - « ... باحتواء محلولَيْ كبريتات النحاس وثاني كرومات النحاس لنوع مشترك من جزيئات متأتّية من النحاس تُسمّى الواحدة منها شاردة النحاس، يجذبها المهبط فتهاجر نحوه وبالتّالي فإنّها حاملة لشحنة كهربائيّة موجبة »
  - « ... جزيئات متأتّية من الكروم تُسمّى الواحدة منها شاردة ثاني الكرومات، يجذبها المصعد فتهاجر نحوه وبالتّالي فإنّها حاملة لشحنة كهربائيّة سالبة. »
  - « إذن، يتركّب المحلول المائي الشاردي لثاني كرومات النحاس من شوارد النحاس وشوارد ثاني الكرومات. »
  - « تُدعى شاردة النحاس الحاملة لشحنة موجبة شاردة موجبة أو كتيونا، أمّا شاردة ثاني الكرومات الحاملة لشحنة سالبة فتدعى شاردة سالبة أو أنيونا. »
  - Déductions : sulfate de cuivre ⇒ anions = « شوارد الكبريتات » ; dichromate de potassium ⇒ cations = « شوارد البوتسيوم ». Migration des sulfates et du potassium « ولو أنّه لم يتسنّ للعين المجرّدة مشاهدة تلك الهجرة » (ions incolores).
  - Schéma الشكل 5 : cuve, ions « + » (bleus) et « − » (orange) migrant en sens opposés.
- Aucune donnée numérique à recalculer dans l'expérience (dimensions et tension seulement).

### Encadré أستنتج (p. 120, verbatim)
> « تتركّب المحاليل المائيّة الشارديّة من نوعين من الشوارد، شوارد موجبة وشوارد سالبة. »
> « تؤمّن ناقليّة المحاليل الشارديّة للكهرباء بفضل حركة كلّ نوع من الشوارد في اتّجاه معيّن : »
> « – الشوارد الموجبة التي لا تنتقل في المحلول إلاّ نحو المهبط وتسمّى لذلك شوارد مهبطيّة (أو كاتيونات) مثل شوارد النحاس وشوارد البوتسيوم. »
> « – الشوارد السالبة التي لا تنتقل إلاّ نحو المصعد وتسمّى لذلك شوارد مصعديّة (أو أنيونات) مثل شوارد ثاني البكرومات وشوارد الكبريتات. »

(⚠ « ثاني البكرومات » : coquille imprimée pour « ثاني الكرومات ».)

### Encadré الخلاصة (p. 120, verbatim — couvre les leçons 15–17)
> « المحاليل المائيّة الشارديّة أقدر من الماء النقيّ على نقل الكهرباء. »
> « كلّما ازداد تركيز مَحلول شارديّ ارتفعت ناقلية المحلول للكهرباء. »
> « يحوي كل محلول شارديّ نوعين اثنين من الشوارد: شوارد موجبة وشوارد سالبة. »
> « تدعى الشوارد الموجبة كاتيونات والشوارد السّالبة أنيونات. »
> « مرور التيّار الكهربائي في محلول مائيّ شارديّ ناتج عن حركة جماعيّة منظّمَة للشوارد : تنتقل الشوارد المصعديّة دائما في الاتّجاه المعاكس للشوارد المهبطيّة. »

Symboles : aucune formule chimique d'ion (pas de Cu²⁺, SO₄²⁻, K⁺, Cl⁻, Cr₂O₇²⁻), aucune charge chiffrée. Unités : V, cm, mm.

### Exercices
- **أقيّم مكتسباتي** (p. 120, verbatim) : « بالاعتماد على التجربة السابقة أبحث عن تركيبة المحلول المائي الشاردي لكلورير البوتسيوم وأحدّد نوع شوارد الكلورير (مصعديّة أم مهبطيّة). »
  - Réponse : شوارد البوتسيوم (موجبة/مهبطيّة) + شوارد الكلورير ⇒ الكلورير مصعديّة (أنيونات).

**أعوّل على نفسي — أتمرّن على حلّ المسائل (p. 121–122)**
- **تمرين 1** — « ضع علامة x أمام كلّ بيان صحيح » :
  1. « محلول ملح الطعام المركّز ناقل ضعيف للتيار الكهربائي. » → faux.
  2. « الماء المقطر ناقل جيّد للتيار الكهربائي. » → faux.
  3. « المحاليل الناقلة للتيار الكهربائي تحوي كثيرا من الكاتيونات وقليلا من الأنيونات. » → faux (contredit « نوعين » ; la neutralité électrique n'est jamais énoncée dans la leçon, donc le rejet s'appuie seulement sur la leçon de façon indirecte).
  4. « المحاليل الشاردية ناقلة للتيار الكهربائي. » → vrai.
  5. « كلّ محلول مائي شاردي يتكون من نوع واحد من الأنيونات ونوع واحد من الكتيونات. » → faux au sens strict (un mélange peut en contenir plusieurs, ex. l'eau minérale de la p. 118) ; ⚠ ambigu : la خلاصة dit « يحوي كل محلول شارديّ نوعين اثنين من الشوارد » (au sens « deux catégories »), un élève peut cocher « vrai ».
- **تمرين 2** — compléter avec « الأنيونات – الكاتيونات – الشاردي – متشتتة – نقْل – ناقليّة – ناقل – أقدر – عازل » :
  1. الماء النقيّ **ناقل** للتيار الكهربائي ولكن بصعوبة.
  2. يُنعت كلّ محلول مائي **أقدر** من الماء النقيّ على **نقل** التيار الكهربائي بالمحلول الشاردي.
  3. تتأثّر **ناقليّة** المحلول **الشاردي** للكهرباء بقيمة تركيزه.
  4. تتركّب المحاليل الشاردية من أنيونات وكاتيونات **متشتتة** في الماء.
  5. تؤمّن ناقليّة المحاليل الشارديّة للكهرباء بفضل حركة جماعيّة لـ**الأنيونات** نحو المصعد ولـ**الكاتيونات** نحو المهبط.
  (« عازل » est un distracteur non utilisé ; « متشتتة » n'apparaît nulle part dans le cours.)
- **تمرين 3** — deux tubes, l'un solution de sel, l'autre eau distillée ; décrire une expérience (avec matériel) pour les identifier. → circuit série générateur + interrupteur + ampèremètre (ou lampe) + électrolyseur ; la solution de sel donne un courant nettement plus intense.
- **تمرين 4** — « لمقارنة تركيز محلولين لنفس المادّة » ; ampèremètre : تجربة 1 → 0,01A ; تجربة 2 → 0,1A.
  1. Le plus apte à conduire : solution de l'expérience 2 (0,1 A > 0,01 A ; rapport 10).
  2. La plus concentrée : solution 2.
- **تمرين 5** — solution violette de permanganate de potassium (« شوارد البوتاسيوم وشوارد البرمنغنات ») ; expérience du « الدرس السابع عشر » avec permanganate seul ; le violet se déplace vers l'électrode de gauche.
  1. L'électrode vers laquelle migre le violet : **المصعد** (plaque reliée au + d'après le câblage du schéma).
  2. Violet = ions permanganate ⇒ **أنيونات**.
  3. « هل كان بإمكانك التعرّف إلى نوع شوارد البرمنغنات دون اللجوء إلى انجاز هذه التجربة، إذا علمت أنّ شوارد ثاني الكرومات الموجودة في محلول ثاني كرومات البوتسيوم هي من الأنيونات ؟ » → oui : dans le dichromate de potassium, le potassium est donc le cation ; la même شاردة البوتسيوم est présente dans le permanganate de potassium, et une solution contient les deux types ⇒ le permanganate est l'anion.
  - Graphie : ex. 5 écrit « البوتسيوم » et « البوتاسيوم » dans le même énoncé.

### Bornes
- ✅ Distinction شاردة موجبة / سالبة ; noms كاتيون = شاردة مهبطيّة, أنيون = شاردة مصعديّة ; المهبط = قطب المحلال الموصول بالقطب السالب ; المصعد = الموصول بالقطب الموجب.
- ✅ Conduction = « حركة جماعيّة منظّمَة للشوارد » en sens opposés.
- ✅ Une شاردة est présentée comme « جزيئات متأتّية من النحاس/الكروم » portant une charge.
- ⛔ Objectif « التمييز بين الشاردة والذرّة » : le texte ne donne aucune définition explicite comparant atome et ion (pas de gain/perte d'électrons écrit) — seule la charge électrique distingue implicitement.
- ⛔ Aucune formule d'ion, aucune charge chiffrée (pas de 2+, pas de Cl⁻), aucune équation de dissociation.
- ⛔ Pas d'énoncé de l'électroneutralité de la solution.
- ⛔ Le mot « إلكترون » n'apparaît pas dans la leçon.

### Vocabulaire officiel (équivalents français : tableau du lexique p. 211–216 en fin de L22.md)
شاردة / شوارد، شاردة موجبة، شاردة سالبة، كاتيون / كتيون (كاتيونات، كتيونات)، أنيون (أنيونات)، شوارد مهبطيّة، شوارد مصعديّة، المهبط، المصعد، هجرة الشوارد، محلال كهربائي، ورق ترشيح، قطّارة، جوزة شدّ، شاردة النحاس، شاردة ثاني الكرومات، شوارد الكبريتات، شوارد البوتسيوم، شوارد الكلورير، شوارد البرمنغنات، كلورير البوتسيوم، ثاني كرومات البوتسيوم / النحاس، برمنغنات البوتسيوم.

### Incohérences / remarques
- Coquille « ثاني البكرومات » (أستنتج p. 120).
- Graphies كتيونات/كاتيونات et البوتسيوم/البوتاسيوم alternées.
- Étiquette d'eau minérale : Σ ions (256,7) ≠ « مجموع الأملاح » 200,0 ; aucune unité (mg/L) imprimée.
- Ex. 1-5 ambigu vis-à-vis de la خلاصة (« نوعين اثنين من الشوارد »).

### Leçon 18 — « المحلول المائي الحامضي والمحلول المائي القلوي » (ص 124–126)

- **محور** : المادّة في الطبيعة · **باب** : المحاليل الشارديّة (carte p. 6).
- Page d'ouverture p. 123 « المحاليل الحامضيّة والمحاليل القلويّة » regroupe les leçons 18 à 21 (« 18- المحلول المائي الحامضي والمحلول المائي القلوي / 19- قيس pH / 20- درجة حموضة محلول مائي حامضي / 21- درجة قلويّة محلول مائي قلوي ») — la leçon 22 n'y figure pas. Photo « ثمار حامضيّة وبعض العصائر المستخلصة منها » et questions d'amorce (verbatim) : « لماذا تكنّى بعض الثّمار بالحمضيات ؟ » ; « بماذا نفسّر ذلك المذاق القارص في عصير اللّيمون أو في عصير الطماطم ؟ » ; « ما هي الأمطار الحمضيّة والعوامل المتسبّبة في ظهورها ؟ ما هي مخاطرها ؟ » ; « ما هي خاصيّة المحاليل الّتي تُستعمَل لتهدئة لسع النّحل، ولماذا ؟ »
- Pictogramme carte : livre (mais contient une manipulation au pH-mètre).

### Objectifs (carte p. 6, verbatim)
- تعريف المحلول المائي الحامضي والمحلول المائي القلوي.
- التمييز بين محلول مائي حامضي ومحلول مائي قلوي حسب قيمة pH .

### Déroulé
- **أتأمّل وأتساءل** (verbatim) : « ما هو الجهاز المستعمل لمراقبة جودة السوائل والمحاليل الغذائيّة ؟ » ; « ما المقصود بالكتابة "pH = 7" على قارورة ماء معدني معيّن والكتابة "pH = 7,5" على أخرى ؟ » ; « ما المقصود بالكتابة "pH = 5,5" على علبة مناشف إزالة مساحيق التجميل والكتابة "pH = 8" على علبة نوع خاصّ من الأسبيرين ؟ » (photos : « p.H. 5.5 » sur un déodorant, « PH8 » sur une boîte).
- **أجرّب وألاحظ** — matériel : « جهاز pH متر : جهاز رقمي أو إبري (ذو مرقَم مدرّج من 0 إلى 14) مصحوب بمسبر. (الشكل 1) – كؤوس اختبار سعة 100 mL – ورق الترشيح – لوازم تجربة ناقليّة الكهرباء. » ; « ماء نقيّ (ماء مقطّر) – عصير برتقال أو ليمون – ماء جافال – محلول مائي للصودا – محلول مائي لحامض الكلورهيدريك. »
  1. Expérience préliminaire : conductivité de l'eau de Javel et du jus (pas de résultat écrit).
  2. Mesures au pH-mètre (sonde rincée à l'eau distillée et séchée au papier filtre entre deux mesures) :
     | Solution | pH lu (texte) | Afficheur figure |
     |---|---|---|
     | ماء مقطّر | 7 | 7.07 (الشكل 2) |
     | ماء جافال | 11 | — |
     | العصير | 2,3 | — |
     | محلول الصودا | 13 | 13.04 (الشكل 3) |
     | محلول حامض الكلورهيدريك | 1 | — |
- Classement recalculé : pH < 7 → jus (2,3), HCl (1) = acides ; pH > 7 → Javel (11), soude (13) = basiques ; eau pure = 7.

### Encadré أستنتج (p. 125, verbatim ; inégalités à lire de gauche à droite comme imprimées)
> « يختصّ كلّ محلول مائيّ شارديّ بمقدار عددي يتراوح بين 0 و 14 في 25° C ويُسمّى pH المحلول. »
> « pH المحلول المائي مقدار قابل للقيس. »
> « الـ pH متر جهاز يُستعمَل لقيس الـ pH »
> « للماء النقيّ: pH = 7 في 25° C . »
> « هناك من المحاليل المائيّة الشارديّة ما يتميّز بـ pH < 7 في 25° C ، وتُعرف بالمحاليل الحَامضيّة، أمّا تلك التي تتميّز بـ pH > 7 في 25° C فهي تُعرف بالمحاليل القِلويّة. »

### Encadré تعريف (p. 126, verbatim)
> « يُسمّى محلولا حامضيّا كلّ محلول شارديّ له pH أصغر من pH الماء النقيّ في نفس درجة الحرارة. »
> « محلول حامضيّ ⟺ محلول شارديّ ذو pH < 7 في 25° C »
> « أمثلة: عصير الليمون، محلول حامض الكلورهيدريك، محلول حامض الأسكوربيك (فيتامين C)... »
> « يُسمّى محلولا قِلويّا كلّ محلول شارديّ له pH أكبر من pH الماء النقيّ في نفس درجة الحرارة. »
> « محلول قِلويّ ⟺ محلول شارديّ ذو pH > 7 في 25° C »
> « أمثلة : محلول الصودا، ماء جافال، ماء البحر، محلول النُّشادِر... »

Symboles/unités : pH (toujours en latin, sans unité), « 25° C » (écrit avec espace), ⟺ (double flèche d'équivalence), 0 à 14.

### Exercices
- **أقيّم مكتسباتي** (p. 126, verbatim) : « قُدّمَت لي ثلاثة كؤوس اختبار وقيل لي إنّ أحداها تحتوي على ماء مقطّر والثانية على محلول حامضيّ والثالثة على محلول قِلويّ وطُلِب منّي التعرّف إلى كلّ من المحلول الحامضي والمحلول القوي عن طريق التجربة. أقترح تمشيّا للغرض مستعملا فيه جهاز الـpH متر. »
  - Réponse : mesurer le pH de chacune (sonde rincée/séchée entre les mesures) : pH = 7 → eau distillée ; pH < 7 → acide ; pH > 7 → basique (à 25 °C).
  - ⚠ Coquille : « والمحلول القوي » pour « القلوي ».
- Pas de série « أعوّل على نفسي » dans cette leçon (p. 124–126).

### Bornes
- ✅ pH : nombre entre 0 et 14 à 25 °C, mesurable au pH-mètre ; eau pure pH = 7 à 25 °C.
- ✅ Définition acide/basique par comparaison au pH de l'eau pure « في نفس درجة الحرارة » + équivalence à 25 °C.
- ⛔ Aucune définition chimique du pH (pas de H₃O⁺/H⁺, pas de log, pas de concentration) — pH est présenté comme « مقدار عددي ».
- ⛔ La notion de « محلول متعادل » n'est pas nommée ici (réservée à la leçon 22).
- ⛔ Aucune dépendance quantitative du pH à la température n'est donnée (seulement la précision « في 25° C »).
- ⛔ Le résultat de l'« expérience préliminaire » de conductivité (Javel, jus) n'est pas écrit.

### Vocabulaire officiel (équivalents français : tableau du lexique p. 211–216 en fin de L22.md)
محلول مائي حامضي / حامضيّ، محلول مائي قلوي / قِلويّ، pH، pH متر (جهاز رقمي أو إبري)، مسبر، مرقَم مدرّج، ماء جافال، محلول الصودا، حامض الكلورهيدريك، حامض الأسكوربيك (فيتامين C)، محلول النُّشادِر، ماء البحر، عصير الليمون / البرتقال، الحمضيات، الأمطار الحمضيّة.

### Incohérences / remarques
- « المحلول القوي » (coquille, أقيّم مكتسباتي).
- Afficheurs des figures (7.07 ; 13.04) ≠ valeurs du texte (7 ; 13) — arrondis, sans contradiction de fond.
- « أحداها » (accord) — reproduit tel quel.

### Leçon 19 — « قيس pH » (ص 127–130)

- **محور** : المادّة في الطبيعة · **باب** : المحاليل الشارديّة. Séance expérimentale.

### Objectifs (carte p. 6, verbatim)
- قيس pH محلول مائي باستعمال pH متر أو ورق pH.

### Déroulé

**Partie 1 — « استعمال الـ pH متر » (p. 127–129)**
- أجرّب وألاحظ — matériel : « pH متر مُعايَر (الشكل 1) – كؤوس اختبار سعة 100 mL – ورق ترشيح. » ; « ماء نقيّ (ماء مقطّر) – محلول مائي لحامض الخَلّيك – محلول مائي للصودا – محلول مائي لحامض الكلورهيدريك – محلول مائي للنُّشادر. » (الشكل 1 : « أنواع مختلفة لأجهزة الـ pH متر »).
- Protocole (verbatim résumé, avec l'exemple de l'acide acétique) :
  - « أسكب في كأس اختبار كمّيّة من المحلول المائي لحامض الخَلّيك تسمح بغمر الجزء الحسّاس من مسبر الـ pH متر. »
  - « أحرك المسبر بلطف (الشكل 2) قصد غمسه في المحلول ثمّ أثبّته في مكانه عندما أتأكد من غمر المحلول للجزء الحساس كليّا مع الحرص على أن لا يلمس طرفه السفلي قاع الكأس (تفاديا لكل عطب). »
  - « أشغّل الـ pH متر ثمّ أقرأ قيمة pH المحلول عند ثبوتها على مرْقَم الجهاز (الشكل 3). » (afficheur 3.45)
  - « أوقف تشغيل الجهاز ثمّ أخرج المسبر من المحلول وأثبّته عاليا، بعيدا عن كأس الاختبار. » ; rinçage à l'eau distillée (الشكل 4) et séchage au papier filtre (الشكل 5).
- Tableau p. 128 (pH-mètre) :
  | المحلول المائي | حامض الخَلّيك | الصودا | حامض الكلورهيدريك | النُّشادر |
  |---|---|---|---|---|
  | pH | 3,45 | 12,04 | 1,98 | 10,57 |

**Encadré أستنتج 1 (p. 129, verbatim)**
> « للحصول على قيس صحيح لِـ pH المحلول يجب احترام عَددٍ من القواعد، من أهمّها : »
> « – التأكّد في البداية من أنّ الـ pH متر معايَر. »
> « – غمس الجزء الحسّاس للمسبر كليّا في المحلول. »
> « – غسل المسبر بالماء المقطر إثر كلّ عمليّة قيس. »
> « الـ pH متر جهاز قيس دقيق فهو ذو حسّاسيّة تصل إلى حدّ 1/100 من وحدةِ pH . »

**Partie 2 — « استعمال ورق pH » (p. 129–130)**
- Matériel : « علبة ورق pH في شكل شريط ملفوف على بكرة (الشكل 6) أو في شكل مجموعة شُرَيْطات (الشكل 7) – كؤوس اختبار سعة 100 mL – قطارة. » + mêmes solutions. (Figures : bobine « pH 1-14 » avec disque de teintes ; nuancier à bandes gradué 0–3 et 3,5–9 par pas de 0,5, 11–14.)
- « بواسطة القطارة، أبلّل شُرَيْطا (أو جزءا صغيرا من شريط اللفيفة) بمحلول حامض الخَلّيك ثمّ أقارن الألوان الظاهرة على الشريط مع ألوان الدليل المرسومة على علبة ورق pH المستعمل، وذلك لتحديد قيمة pH المحلول. »
- Tableau p. 130 (papier pH) :
  | المحلول المائي | حامض الخَلّيك | الصودا | حامض الكلورهيدريك | النّشادر |
  |---|---|---|---|---|
  | pH | 3,5 | 12 | 2 | 10,5 |
- « حالة بحالة، أقارن قيمة pH بالقيمة التي تحصّلت عليها في التجربة السابقة باستعمال الـ pH متر. فألاحظ أنّها متقاربة جدّا إن لم تكن متساوية. »
- Recalcul des écarts papier − pH-mètre : acétique +0,05 ; soude −0,04 ; HCl +0,02 ; ammoniac −0,07 (tous < 0,1 unité pH).

**Encadré أستنتج 2 (p. 130, verbatim)**
> « ورق pH أداة أخرى لقيس pH المحاليل الشارديّة، ولكنّها أقلّ دقّة من الـ pH متر. »
> « استعمال ورق pH طريقة عمليّة لقيس pH ولكنّها تقريبيّة. »

Symboles : pH ; « 1/100 من وحدةِ pH » (le manuel parle de « وحدة pH » tout en n'attribuant pas d'unité au pH ailleurs).

### Exercices
- Aucun exercice (ni أقيّم مكتسباتي ni أتمرّن) dans p. 127–130.

### Bornes
- ✅ Protocole de mesure au pH-mètre (étalonné, sonde immergée, rinçage), précision 1/100 d'unité pH.
- ✅ Papier pH : comparaison à un nuancier ; méthode pratique mais approchée.
- ⛔ L'étalonnage (« معايَر ») n'est pas expliqué (aucune solution tampon mentionnée).
- ⛔ Aucune précision chiffrée pour le papier pH (seulement « أقلّ دقّة », « تقريبيّة »).
- ⛔ Pas de classement acide/basique demandé dans cette leçon, bien que les valeurs le permettent (acétique, HCl acides ; soude, ammoniac basiques).

### Vocabulaire officiel (équivalents français : tableau du lexique p. 211–216 en fin de L22.md)
pH متر مُعايَر، مسبر، الجزء الحسّاس للمسبر، مرْقَم الجهاز، ورق pH (شريط ملفوف على بكرة، شُرَيْطات)، دليل الألوان، قطّارة، حامض الخَلّيك، حامض الكلورهيدريك، الصودا، النُّشادر، دقّة، حسّاسيّة، وحدة pH، تقريبيّة.

### Remarques
- Soude : pH 13 en leçon 18, 12,04 ici — solutions différentes, non contradictoire mais à ne pas confondre dans un QCM.
- Le texte écrit « أحرك المسبر بلطف » (sans hamza sur ك/ doublement non marqué) — tel quel.

### Leçon 20 — « درجة حموضة محلول مائي حامضي » (ص 131–136)

- **محور** : المادّة في الطبيعة · **باب** : المحاليل الشارديّة (sous-ensemble « المحاليل الحامضيّة والمحاليل القلويّة », p. 123). Séance expérimentale.
- Carte p. 6 : « درجة حموضة محول مائي حامضي » (coquille « محول » dans la carte ; bandeau p. 131 correct : « درجة حموضة محلول مائي حامضي »).

### Objectifs (carte p. 6, verbatim)
- التعرّف إلى درجة حمضيّة محلول مائي حمضي حسب قيمة pH.
  (⚠ la carte dit « حمضيّة / حمضي », la leçon dit « حموضة / حامضي ».)

### Déroulé
- **أتأمّل وأتساءل** (p. 131, verbatim) :
  - « كلّما زادت ثمرة البرتقال أو العنب نضجا تقلّصت قروصتها، لماذا ؟ »
  - « ما المقصود بالكتابة «ماء حامضي 5%» على قارورة ماء البطاريّة ؟ »
  - « من المعلوم أنّ حامض الكلورهيدريك «ماء الفرق» سائل خطر. لماذا تنقص خطورة محلوله المائي كلّما نقص تركيزه ؟ »
  - « لماذا توصف القوارص والخلّ وعصائر بعض الثمار كالطماطم والجزر والفراولة بالحوامض اللطيفة، في حين أنّ حامض الكلورهيدريك وحامض الكبريتيك تُنعتُ بالحوامض الخطرة ؟ »
  - « من المعلوم أنّ حامض الخَلّيك هو مادّة كيميائيّة أكّالة وحرّاقة لاذعة، بما أفسّر إذَنْ وجود قنّينة الخلّ على طاولة الأكل رغم احتواء هذا السائل لحامض الخَلّيك ؟ »
- **أتأمّل وألاحظ** : jus de citron pur imbuvable « بسبب شدّة قروصته » ; dilué « تنقص قروصته فيصير مستساغا » ; trop dilué « يفقد العصير قروصته ويصبح كأنّه محلول سكّري ». HCl concentré utilisable seulement au labo « بحذر شديد ... أكّال وحرّاق كما هو مشار إليه في علامة قارورته » ; « بتخفيفه نحصل على محلول قليل الخطورة ».
- **أحلّل** (verbatim) : « أعلم أنّ عصير الليمون محلول حامضيّ، وقروصته تدلّ على حموضته. كما أنّ صفتيْ الحرّاق والأكّال لحامض الكلورهيدريك تدلان على حموضته. بالتالي ينقص عصير الليمون ومحلول حامض الكلورهيدريك حموضة كلّما زدت في تخفيفهما. »

**Encadré أستنتج 1 (p. 131, verbatim)**
> « ليست هناك حموضة مطلقة : لكلّ محلول حامضيّ درجة حموضة معيّنة ترتفع بزيادة التركيز وتنقص بنقصانه. »
> « كلّما زادت درجة الحموضة، كان المحلول الحامضيّ قارصا (بالنسبة للموادّ الغذائيّة) وحرّاقا وأكّالا. »

- **أجرّب وألاحظ** (p. 132) — matériel : « كؤوس اختبار ذات سعة 100mL – pH متر – محراك. » ; « ماء الحنفيّة – عصير الليمون أو عصير البرتقال. »
  - **تجربة 1** : mesurer le pH du jus ; « أخفّف تدريجيّا العصير بإضافة 10mL من ماء الحنفيّة في كلّ مرّة وأقيس pH المحلول فألاحظ أنّ قيمة pH ترْتفع كلّما زاد العصير تخفيفا. »
  - **تجربة 2** : mesurer le pH de l'eau du robinet ; « أضيف تدريجيّا كميّة هامّة من عصير الليمون في الماء وأقيس في كلّ مرّة pH المحلول. فألاحظ أنّ قيمة pH تزيد كلّما زاد العصير تركيزا. »
    - ⚠ **Erreur du manuel** : quand la concentration en jus augmente, le pH doit **diminuer** (cf. تجربة 1 et l'encadré qui suit). « تزيد » contredit l'أستنتج de la même page.
  - « ملاحظة : قبل كلّ عمليّة قيس pH المحلول لا بدّ من تحريك المزيج. »
  - Aucune valeur de pH chiffrée dans ces deux expériences.

**Encadré أستنتج 2 (p. 132, verbatim)**
> « كلّما زادت درجة حموضة محلول مائي شارديّ انخفضت قيمة pH المحلول والعكس بالعكس. »
> « ⇕ »
> « كلّما انخفضت قيمة pH محلول مائي حامضي زادت درجة الحموضة والعكس بالعكس. »

**Encadré تعريف (p. 132, verbatim)**
> « مقدار pH أداة تُعَرَّفُ بها درجة حموضة المحاليل المائيّة الشارديّة. »

**Encadré الخلاصة (p. 133, verbatim)**
> « المحاليل المائيّة الحامضيّة هي محاليل شارديّة ذات pH<7 في 25°C »
> « في حموضة المحاليل الشارديّة درجات مختلفة تتأثّر بالتركيز. »
> « نتعرّف إلى درجة حموضة محلول مائي شاردي بتحديد قيمة pH المحلول. »
> « انخفاض قيمة pH محلول مائي شارديّ حمضيّ دليل على ارتفاع درجة حموضته والعكس بالعكس. »

Symboles/unités : pH, 25°C, mL, % (« ماء حامضي 5% »).

### Exercices
- **أقيّم مكتسباتي** (p. 133) : « علما أنّ قيمة pH عصير ليمون تساوي 2,3 وقيمة pH خلّ تساوي 8, 2. »
  - ⚠ Valeur du vinaigre composée « 8, 2 » (inversion bidi probable de **2,8**). Lecture retenue : 2,8 (le seul sens cohérent avec « خلّ » acide et la question 2).
  1. « أقارن درجة حموضة العصير بدرجة حموضة الخل. » → 2,3 < 2,8 ⇒ le jus de citron est plus acide que le vinaigre.
  2. « أقترح تجربة أغيّر بها قيمة pH عصير الليمون حتّى تصبح متساوية مع قيمة pH الخلّ. » → diluer progressivement le jus avec de l'eau en agitant et mesurant au pH-mètre jusqu'à lire 2,8.

**أعوّل على نفسي — أتمرّن على حلّ المسائل (p. 134–136)**
- **تمرين 1** — compléter avec « مقدار عددي – مقدار المحاليل الحامضيّة – أربعة عشر – سبعة – المحاليل القلوية – أكثر دقّة – أقلّ دقّة » (liste imprimée ambiguë : « مقدار عددي– مقدار المحاليل الحامضيّة– ... » ; lire « مقدار عددي – مقدار – المحاليل الحامضيّة – ... »).
  1. يختصّ كلّ محلول مائيّ شارديّ **بمقدار عددي** يتراوح بين صفر و**أربعة عشر** و يُسمّى pH.
  2. pH محلول مائيّ شارديّ **مقدار** قابل للقيس بجهاز الـ pH متر.
  3. تُختصّ **المحاليل الحامضيّة** بـ pH أقلّ من سبعة في 25°C.
  4. عمليّة قيس pH بالـ pH متر **أكثر دقّة** من قيسه بورق pH.
  (distracteurs : سبعة، المحاليل القلوية، أقلّ دقّة)
- **تمرين 2** — cocher × les énoncés faux puis les corriger :
  1. « لكلّ محلول حامضيّ درجة حموضة معيّنة ترتفع بانخفاض التركيز وتنقص بارتفاعه. » → **خاطئ** ; correction : ترتفع بارتفاع التركيز وتنقص بانخفاضه.
  2. « مقدار pH أداة تُعرّف بها درجة حموضة المحاليل المائيّة الشارديّة. » → صحيح.
  3. « نتعرّف إلى درجة حموضة محلول مائي شاردي بتحديد تركيز المحلول. » → **خاطئ** ; correction : بتحديد قيمة pH المحلول.
  4. « في حموضة المحاليل الشارديّة درجات مختلفة تتأثّر بالتركيز. » → صحيح.
  5. « ارتفاع قيمة pH محلول شارديّ دليل على ارتفاع درجة حموضته والعكس بالعكس. » → **خاطئ** ; correction : انخفاض قيمة pH ... دليل على ارتفاع درجة حموضته.
- **تمرين 3** — « قم ببحث يساعدك على تحديد المواد الحامضيّة من بين المواد التالية : عصير التفّاح، محلول الصودا، عصير الفراولة، ماء مقطّر، محلول حامض الكلورهيدريك، الماء الشروب، محلول البوتاس، محلول حامض النيتريك. »
  - Acides : عصير التفّاح، عصير الفراولة، حامض الكلورهيدريك، حامض النيتريك. Non acides : الصودا، البوتاس (قلويّان)، ماء مقطّر. Le « الماء الشروب » dépend de l'eau (pH ≈ 7, souvent légèrement > 7) — ⚠ réponse non tranchée par la leçon (c'est une « recherche »).
- **تمرين 4** — lait pH = 6,5 ; jus de fraise pH = 5,5 à 25°C.
  1. Les deux < 7 à 25°C ⇒ acides.
  2. 5,5 < 6,5 ⇒ le jus de fraise est plus acide que le lait.
  3. Diluer progressivement le jus de fraise (eau distillée), agiter, mesurer jusqu'à pH = 6,5.
- **تمرين 5** — ranger « ترتيبا تصاعديا حسب قيمة درجة حموضتها » :
  | السائل | ماء مقطّر | عصير طماطم | عصير برتقال | عصير ليمون | حامض النيتريك |
  |---|---|---|---|---|---|
  | pH في 25°C | 7 | 2,4 | 3,5 | 3,2 | 2 |
  - Acidité croissante (pH décroissant) : ماء مقطّر (7) < عصير برتقال (3,5) < عصير ليمون (3,2) < عصير طماطم (2,4) < حامض النيتريك (2).
  - ⚠ Remarques : (a) l'eau distillée (pH 7) n'est pas acide : « درجة حموضة » ne s'applique pas en toute rigueur ; (b) valeurs peu réalistes et incohérentes avec le reste du manuel : jus de tomate 2,4 plus acide que le citron 3,2, alors que l'أقيّم مكتسباتي p. 133 donne citron = 2,3 et la leçon 18 jus = 2,3.
- **تمرين 6** — 5 béchers numérotés 1 à 5, chacun avec 100 mL de solution acide de pH 2,9 ; eau potable ajoutée : 100 / 300 / 700 / 900 / 1900 mL. pH mesurés dans le désordre : 3,5 – 3,2 – 3,4 – 3,05 – 3,57.
  1. Plus on dilue (moins concentré), moins c'est acide ⇒ pH plus grand.
  2. Volumes totaux 200 / 400 / 800 / 1000 / 2000 mL (dilution ×2, ×4, ×8, ×10, ×20) ⇒ كأس 1 : 3,05 ; كأس 2 : 3,2 ; كأس 3 : 3,4 ; كأس 4 : 3,5 ; كأس 5 : 3,57.
  - Contrôle (hors programme, pour vérifier la cohérence) : pour un acide faible, pH ≈ 2,9 + ½·log(f) donne 3,05 / 3,20 / 3,35 / 3,40 / 3,55 → proche des valeurs du manuel ; un acide fort donnerait 3,2 / 3,5 / 3,8 / 3,9 / 4,2. L'ordre suffit au niveau 9ème.
- **أستغلّ وثيقة — « الأمطار الحامضيّة »** (p. 135–136) : pluie « تتميّز تقريبا بـ pH=7 » ; avec le CO₂ (« ثاني أكسيد الكربون ») elle devient acide, pH « إلى 5,6 تقريبا » ; avec « أكاسيد الكبريت و الأزوت », pH « إلى 4,2 ». Effets : forêts et cultures détruites (taches « كالصدأ », feuilles enroulées puis tombées, « خلال عامين تقريبا تذبل الأشجار كلّيا فتصبح الغابات جرداء »), « تتآكل المنحوتات الرخامية وكل المنشآت والتماثيل المعدنيّة » ; photos « تضرّ الأمطار الحمضيّة بالأشجار », « تآكل تمثال أبو الهول ».
  - الأسئلة : 1- « أعرّف الأمطار الحمضيّة. » → d'après le texte seul : pluies devenues acides (pH < 7 : ≈ 5,6 avec le CO₂, jusqu'à 4,2 avec les oxydes de soufre et d'azote). (La convention scientifique « pluie acide = pH < 5,6 » n'est PAS dans le manuel.) 2- effets négatifs (cf. texte). 3- solutions (réduire les émissions industrielles de gaz polluants, etc. — réponse ouverte).
  - ⚠ Le document dit que l'eau de pluie « تتميّز تقريبا بـ pH=7 » avant CO₂ ; il nomme « الأمطار الحامضيّة » (titre) et « الحمضيّة » (questions) : deux graphies.

### Bornes
- ✅ Degré d'acidité variable (« ليست هناك حموضة مطلقة »), croît avec la concentration ; dilution ⇒ pH augmente.
- ✅ Relation inverse pH ↔ degré d'acidité ; « مقدار pH أداة تُعَرَّفُ بها درجة حموضة ».
- ✅ Vocabulaire sensoriel/sécurité : قارص، حرّاق، أكّال.
- ⛔ Aucune loi quantitative pH ↔ dilution (pas de log, pas de « +1 par dilution ×10 »).
- ⛔ Aucune formule chimique (même pas H⁺) ; CO₂ est seulement nommé en toutes lettres dans le document.
- ⛔ Le pourcentage « 5% » est cité sans être expliqué.

### Vocabulaire officiel (équivalents français : tableau du lexique p. 211–216 en fin de L22.md)
درجة الحموضة، حموضة مطلقة، محلول حامضي، تخفيف / تركيز، قارص (قروصة)، حرّاق، أكّال، لاذع، الحوامض اللطيفة / الخطرة، حامض الكلورهيدريك (ماء الفرق)، حامض الكبريتيك، حامض الخَلّيك، حامض النيتريك، الخلّ، القوارص، البوتاس، الماء الشروب، ماء الحنفيّة، الأمطار الحامضيّة / الحمضيّة، أكاسيد الكبريت والأزوت، ثاني أكسيد الكربون.

### Incohérences
1. p. 132 تجربة 2 : « قيمة pH تزيد كلّما زاد العصير تركيزا » — faux, contredit l'encadré voisin.
2. p. 133 : pH du vinaigre imprimé « 8, 2 » (≈ 2,8).
3. p. 135 تمرين 5 : jus de tomate (2,4) plus acide que citron (3,2), incohérent avec citron 2,3 (p. 133) ; eau distillée incluse dans un classement d'acidité.
4. Carte p. 6 : « محول » ; objectif formulé « حمضيّة/حمضي ».

### Leçon 21 — « درجة قلويّة محلول مائي قلوي » (ص 137–141)

- **محور** : المادّة في الطبيعة · **باب** : المحاليل الشارديّة (sous-ensemble « المحاليل الحامضيّة والمحاليل القلويّة », p. 123). Séance expérimentale. Structure calquée sur la leçon 20.

### Objectifs (carte p. 6, verbatim)
- التعرّف إلى درجة قلويّة محلول مائي قلوي حسب قيمة pH.

### Déroulé
- **أتأمّل وأتساءل** (verbatim) : « ما المقصود بالكتابة «hydroxyde de sodium 29%» على قوارير المحاليل المستعملة لتسليك المواسير. » ; « لماذا نشعر أحيانا بشيء من الحرق على مستوى البشرة إثر الاغتسال بالماء والصابون؟ »
- **أجرّب وألاحظ** : « كؤوس اختبار – محراك – ملعقة صغيرة » ; « كُيَيْسُ خميرة – ماء » (photo sachet « levure boulangère instantanée / خميرة فورية »).
  - « أضع ملعقة من مسحوق الخميرة في كأس اختبار يحتوي على 100mL من الماء ثمّ أحرّك المزيج فأحصل على محلول الخميرة. فألاحظ أنّ طعمه مُرّ وأنّ ملمسه صابونيّ. »
  - « إثر تخفيف هام للمحلول ألاحظ أنّ مرارته تنقص وأنّ ملمسه الصّابونيّ يزول تقريبا. »
  - ⚠ Goûter une solution au laboratoire est une consigne de sécurité discutable (le manuel le fait sans avertissement).
- **أتأمّل وألاحظ** (verbatim) : « كما هو الشأن بالنسبة لحامض الكلورهيدريك، لا يمكن استعمال المحلول المائي للصّودا المركّز في المخبر إلاّ باحترام قواعد سلامة محدّدة وبحذر شديد وذلك بسبب خطورته الكبيرة المتمثلة في أنّه كاوٍ وأكّال كما هو مشار إليه في علامة قارورته. بتخفيفه نحصل على محلول قليل الخطورة وذي ملمس صابونيّ. »
- **أحلّل** (verbatim) : « أعلم أنّ خاصيتي المرارة والملمس الصابوني بالنسبة لمحلول الخميرة و خاصيّة الكاويّة للصّودا تدلّ على قلويتهما. بالتالي ينقص محلول الخميرة و محلول الصودا قلوية كلّما زدت في تخفيفهما. »

**Encadré أستنتج 1 (p. 138, verbatim)**
> « ليست هناك قلويّة مطلقة: لكلّ محلول قلويّ درجة قلويّة معيّنة ترتفع بارتفاع التركيز وتنقص بنقصانه. »
> « كلّما زادت درجة القلويّة، كان المحلول القلويّ مرّا (بالنسبة للموادّ الغذائيّة) وكاويا. »

- **أجرّب وألاحظ** (p. 138) — « كؤوس اختبار ذات سعة 100mL – pH متر – محراك. » ; « ماء الحنفيّة – ماء البحر أو ماء جافال. »
  - **تجربة 1** : pH de l'eau de Javel ; dilution par ajouts de « 10mL من ماء الحنفيّة » ⇒ « قيمة pH تنقص كلّما زاد ماء جافال تخفيفا. »
  - **تجربة 2** : pH de l'eau du robinet ; ajout progressif de Javel ⇒ « قيمة pH ترتفع كلّما زاد المحلول تركيزا. » (cohérent, contrairement à la leçon 20)
  - « ملاحظة: لا أنسى أن أحرّك المزيج قبل كلّ عمليّة قيس pH المحلول. »
  - Aucune valeur de pH chiffrée.

**Encadré أستنتج 2 (p. 138, verbatim)**
> « كلّما زادت درجة قلويّة محلول مائي شارديّ ارتفعت قيمة pH المحلول والعكس بالعكس. »
> « ⇕ »
> « كلّما ارتفعت قيمة pH محلول مائي قلوي زادت درجة القلوية والعكس بالعكس. »

**Encadré تعريف (p. 138, verbatim)**
> « كما هو أداة للتعرّف إلى درجة حموضة للمحاليل المائية الشارديّة مقدار pH أداة تُعرّفُ بها كذلك درجة قلوية المحاليل المائيّة الشارديّة »

**Encadré الخلاصة (p. 139, verbatim)**
> « المحاليل المائيّة القلوية هي محاليل شارديّة ذات pH>7 في 25°C . »
> « لقلوية المحاليل الشارديّة درجات مختلفة تتأثّر بالتركيز. »
> « نتعرّف إلى درجة قلوية محلول مائي شاردي بتحديد قيمة pH المحلول. »
> « ارتفاع قيمة pH محلول مائي قلويّ دليل على ارتفاع درجة قلويته والعكس صحيح. »

Symboles/unités : pH, 25°C, mL, %, « C = 10 g.L-1 » (p. 141 — première et seule apparition d'une concentration chiffrée avec unité g.L⁻¹ et symbole C dans les leçons 15–22).

### Exercices
- **أقيّم مكتسباتي** (p. 139) : « علما أنّ قيمة pH محلول الصودا تساوي 12 وقيمة pH محلول النّشادر 10,8 : »
  1. « أقارن درجة قلوية محلول الصودا بدرجة قلوية محلول النّشادر. » → 12 > 10,8 ⇒ soude plus basique.
  2. « أقترح تجربة أغيّر بها قيمة pH محلول الصودا حتّى تصبح متساوية مع قيمة pH محلول النَّشادر. » → diluer progressivement la soude (eau), agiter, mesurer au pH-mètre jusqu'à 10,8.

**أعوّل على نفسي — أتمرّن على حلّ المسائل (p. 140)**
- **تمرين 1** — flacon « pH=13 » ; 3 béchers de 1mL chacun ; eau ajoutée V₁=9mL, V₂=99mL, V₃=999mL ; pH mesurés (désordre) : 11، 10 و 12.
  1. La dilution diminue l'alcalinité ⇒ pH plus faible quand on ajoute plus d'eau.
  2. Volumes totaux 10 / 100 / 1000 mL (dilution ×10, ×100, ×1000) ⇒ الكأس الأوّل : 12 ; الثاني : 11 ; الثالث : 10.
  - Vérif. (hors programme) : base forte, pH = 13 − log₁₀(f) → 12 / 11 / 10 exactement. Le manuel ne formule jamais la règle « −1 par dilution ×10 » ; seul l'ordre est exigible.
- **تمرين 2** — « رتّب هذه المحاليل ترتيبا تصاعديّا حسب قيمة درجة قلويتها » :
  | المحلول | الصودا | البوتاس | النّشادر | ماء جافال | ماء البحر | الدم |
  |---|---|---|---|---|---|---|
  | pH في 25°C | 13 | 12 | 11,8 | 10,6 | 8,4 | 7,4 |
  - Alcalinité croissante : الدم (7,4) < ماء البحر (8,4) < ماء جافال (10,6) < النّشادر (11,8) < البوتاس (12) < الصودا (13).
- **تمرين 3** — « قيمة pH ماء البحر تساوي 8,5 وقيمة pH ماء جافال المركّز تساوي 10,6 في نفس درجة الحرارة » :
  1. Javel plus basique que l'eau de mer (10,6 > 8,5).
  2. Diluer progressivement l'eau de Javel en mesurant jusqu'à pH = 8,5.
  - ⚠ Valeurs non homogènes d'un exercice à l'autre : ماء البحر 8,4 (تمرين 2) vs 8,5 (تمرين 3) ; ماء جافال 10,6 ici vs 11 en leçon 18 ; « ماء جافال المركّز » a le même pH (10,6) que le « ماء جافال » de l'exercice 2.
- **تمرين 4** — (+) vrai / (−) faux et corriger :
  1. « لكلّ محلول قلوي درجة قلوية معيّنة ترتفع بارتفاع التركيز وتنقص بانخفاضه » → (+).
  2. « انخفاض قيمة pH المحلول المائي الشاردي دليل على ارتفاع درجة قلويته والعكس بالعكس » → (−) ; correction : ارتفاع قيمة pH ... دليل على ارتفاع درجة قلويته.
  3. « تُعرف المحاليل القلوية بـ pH أكثر من سبعة في 25°C. » → (+).
  4. « نتعرّف إلى درجة قلوية محلول مائي شاردي بتحديد تركيز المحلول. » → (−) ; correction : بتحديد قيمة pH المحلول.

**هل من مزيد ؟ (p. 141, lecture complémentaire, verbatim essentiel)**
- « محلول النشادر المخفّف (تركيز C = 10 g.L-1) ، وهو محلول قلويّ يستعمل كمنعّم للجلد ومُطهّر ومزيل لكافّة الروائح. »
- « محلول بيكربونات الصوديوم، وهو محلول قلوي يُستخدَم كعلاج للَدْغ النحل الأنثى ذي الخاصّية الحامضيّة. »
- « محاليل الخل وعصير الليمون، وتستعمل: – كعلاج للدغ دبّور النّحل لأنه يتميز بتأثير قلوي. – كمزيل لبقع الحبر. »
  - ⚠ Formulation ambiguë : « لأنه يتميز بتأثير قلوي » — le sujet de « يتميز » est la piqûre de guêpe (dont l'effet est basique, d'où le remède acide), mais la phrase peut se lire comme si le vinaigre avait un effet basique.

### Bornes
- ✅ Degré d'alcalinité variable (« ليست هناك قلويّة مطلقة »), croît avec la concentration ; dilution ⇒ pH diminue.
- ✅ Relation directe pH ↔ degré d'alcalinité ; propriétés sensorielles/sécurité : مرّ، ملمس صابونيّ، كاوٍ، أكّال.
- ⛔ Aucune loi quantitative de dilution ; aucune espèce chimique (pas de OH⁻).
- ⛔ « hydroxyde de sodium 29% » cité en français, sans explication du pourcentage ; le nom arabe « هيدروكسيد الصوديوم » n'est pas donné (la leçon dit « الصّودا »).
- ⛔ La concentration C = 10 g.L-1 (p. 141) n'est ni définie ni exploitée.

### Vocabulaire officiel (équivalents français : tableau du lexique p. 211–216 en fin de L22.md)
درجة القلويّة، قلويّة مطلقة، محلول قلوي، مرارة / مُرّ، ملمس صابونيّ، كاوٍ / الكاويّة، أكّال، الصودا، البوتاس، النّشادر، ماء جافال، ماء البحر، الدم، الخميرة، بيكربونات الصوديوم، لدغ النحل / دبّور النحل، منعّم، مطهّر، تخفيف، تركيز.

### Incohérences
1. Valeurs de pH de l'eau de mer (8,4/8,5) et de l'eau de Javel (10,6/11) différentes selon les pages.
2. تعريف p. 138 : phrase syntaxiquement bancale (« كما هو أداة للتعرّف إلى درجة حموضة للمحاليل ... »).
3. هل من مزيد 3 : attribution ambiguë de « تأثير قلوي ».

### Leçon 22 — « المحلول المائي المتعادل » (ص 143–151)

- **محور** : المادّة في الطبيعة · **باب** : المحاليل الشارديّة (carte p. 6 : « المحلول المتعادل » ; bandeau p. 143 : « المحلول المائي المتعادل »). Pictogramme carte : livre (mais manipulations au pH-mètre).
- Page d'ouverture p. 142 « المحاليل المتعادلة » : « 22- المحلول المائي المتعادل » ; photo « شجرة السمسم تفرز زيتا متعادلا » ; questions (verbatim) : « لماذا ينصح باستعمال صابون حامضي خفيف أو متعادل وبدون ملوّنات لتنظيف جسم الإنسان ؟ » ; « لإخصاب الأراضي الحمضيّة لماذا يُشترَط أن تكون الأسمدة المستعملة قلويّة ؟ »
- Pages 152–154 = ouverture de la partie suivante « الضّوء / تغيّر مسار الضوء » (leçons 23–28) et « مكتسباتي القبليّة » — hors de cette partie, non traitées ici.

### Objectifs (carte p. 6, verbatim)
- تذكّر أنّ قيمة pH المحلول المائي المتعادل يساوي قيمة pH الماء النقي في نفس درجة الحرارة.
- التعرّف إلى محلول مائي متعادل.

### Déroulé

**Partie 1 — « مدلول المحلول المتعادل » (p. 143–144)**
- أتأمّل وأتساءل (verbatim) : « ما الذي يجعل شامبو الرضيع لا يسبّب أيّ احتراق في العين؟ » ; « ما المقصود بالعبارة «pH neutre» المتداوَلة في ومضات إشهار بعض مواد التجميل؟ » (étiquette « EXTRADOUX … PH NEUTRE »).
- أجرّب وألاحظ — « جهاز pH متر – كؤوس اختبار سعة 100mL – ورق ترشيح. » ; « ماء مقطّر – محلول مائي لكلورير الصوديوم – محلول مائي لكلورير البوتسيوم. »
  - Eau distillée : « فيشير إلى العدد 7 » ; solutions de chlorure de sodium puis de potassium : « فيشير الـ pH متر إلى القيمة 7 تقريبا لكلّ محلول. » (figure : afficheur 7.05 pour « محلول كلورير الصوديوم »).
- أحلّل (verbatim) : « تَساوي pH محلول كلورير الصوديوم أو البوتسيوم مع pH الماء النقيّ رغم أنّهما محلولان شارديان يعني أنهما ليسا بالحامضين ولا بالقلويين فهما يختصّان بدرجة تتوسّط درجات الحموضة ودرجات القلويّة، فنقول إنّ كلاًّ منهما محلول متعادل. بالتالي نقول إنّ الماء النقيّ سائل متعادل. »

**Encadré أستنتج (p. 144, verbatim)**
> « هناك من المحاليل المائيّة الشارديّة التي تتميّز بـ pH يساوي قيمة pH الماء النقيّ في نفس درجة الحرارة، وتُعرف بالمحاليل المتعادلة. »

**Encadré تعريف (p. 144, verbatim)**
> « كلّ محلول شارديّ له pH يساوي قيمة pH الماء النقي في نفس درجة الحرارة يسمّى محلولاً متعادلا. »

**Suite de l'encadré (hors cadre, en rouge, verbatim)**
> « في 25°C، كلّ محلول شارديّ ذو pH=7 هو محلول متعادل »
> « الماء النقيّ وسط متعادل. »
> « أمثلة أخرى : محلول ملح الطعام، محلول كلورير البوتسيوم، محلول نيترات الصوديوم... »

- **أقيّم مكتسباتي** (p. 144) : classer (pH à 25°C) :
  | المحلول | ميتيلأمين | نيترات البوتاسيوم | خل | فلورير الهيدروجين | بوتاس | ملح الطّعام |
  |---|---|---|---|---|---|---|
  | pH | 11 | 7 | 5 | 3 | 12 | 7 |
  - Réponse : acides = خل (5)، فلورير الهيدروجين (3) ; basiques = ميتيلأمين (11)، بوتاس (12) ; neutres = نيترات البوتاسيوم (7)، ملح الطّعام (7).

**Partie 2 — « محاليل متعادلة مستعمَلة في الحياة اليوميّة » (p. 144–145)**
- أجرّب وألاحظ — « جهاز pH متر – كؤوس اختبار سعة 100 mL – ورق ترشيح. » ; « ماء مقطّر – شامبو أطفال – صابون أطفال – سكّر – كحول الصيدليّة. »
  - Eau distillée + shampoing, puis savon, sucre, alcool : « فألاحظ في كلّ الحالات أنّ pH المحلول يساوي تقريبا pH الماء المقطّر المستعمَل. »
- **أستنتج** (p. 145, verbatim) : « من المحاليل المستعملة في الحياة اليوميّة توجد المحاليل المتعادلة. »
  - ⚠ **Incohérence de définition** : le sucre et l'alcool pharmaceutique ont été montrés NON ioniques en leçon 15 (conduction ≈ eau pure) ; or la définition p. 144 réserve « متعادل » à « كلّ محلول شارديّ ». Les ranger parmi les « محاليل متعادلة » contredit la définition. (Le manuel ne commente pas.)
- **أقيّم مكتسباتي** (p. 145) :
  1. « ما المقصود بالعبارة المكتوبة بالفرنسيّة «pH NEUTRE» على العلامة المقابلة لنوع من الشامبو والتي تُترجَمُ بـ« pH متعادل» ؟ » → le shampoing est une solution neutre : son pH égale celui de l'eau pure à la même température (7 à 25°C).
  2. « هل يصحّ فعلا القول« pH متعادل»؟ لماذا؟ » → non, abus de langage : c'est la solution qui est متعادل ; le pH est une valeur (= pH de l'eau pure). (Réponse attendue, déduite de la définition ; le manuel ne la donne pas.)

### Exercices — أعوّل على نفسي / أتمرّن على حلّ المسائل (p. 146–147)
- **تمرين 1** — cocher ✗ la bonne proposition :
  1. « pH محلول متعادل في 25°C » : a أقلّ من العدد 7 / b يساوي العدد 7 / c يساوي العدد 14 → **b**.
  2. « pH محلول متعادل » : a يتأثّر بالحرارة فقط / b يتأثّر بالتركيز فقط / c يتأثّر بالحرارة والتركيز معًا → **a** (il vaut toujours le pH de l'eau pure à la même température). ⚠ Cette dépendance thermique n'est enseignée qu'implicitement (« في نفس درجة الحرارة ») et chiffrée seulement à l'exercice 3.
  3. « كلّ محلول مائي متعادل » : a يحتوي على نفس شوارد الماء النقي / b لا يحتوي على أيّ شاردة / c يحتوي على نفس العدد من الشوارد المصعديّة والشوارد المهبطيّة / d يحتوي على نوعين من الشوارد بنسب تميّزه بـpH يساوي pH الماء النقي → **d**. ⚠ La proposition c n'est jamais traitée dans le cours ; elle est fausse en général mais un élève ne peut la réfuter qu'avec un contre-exemple non enseigné.
- **تمرين 2** — 1. pH de l'eau pure à 25°C = 7.
  2. Tableau (pH à 25°C) :
  | السّائل | عصير برتقال | ماء جافال | ماء المطر | الدّم | ماء البحر | حليب البقر | اللّعاب |
  |---|---|---|---|---|---|---|---|
  | pH | 3.5 | 10.6 | 6 | 7.4 | 8.5 | 6.5 | 7 |
  - أ : trois groupes — acides (pH < 7) : عصير برتقال، ماء المطر، حليب البقر ; basiques (pH > 7) : ماء جافال، الدّم، ماء البحر ; neutre (pH = 7) : اللّعاب.
  - ب : liquide neutre : اللّعاب seul.
  - Remarque : ce tableau imprime les décimales avec un **point** (3.5, 10.6…) alors que le reste du chapitre utilise la virgule (3,5).
- **تمرين 3** — pH de l'eau pure selon la température :
  | T(°C) | 0 | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 50 | 98 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | pH الماء | 7,47 | 7,37 | 7,27 | 7,17 | 7,08 | 7 | 6,92 | 6,84 | 6,77 | 6,63 | 6,5 |
  - Solutions : (م1) pH 5 à 0°C ; (م2) pH 7 à 0°C ; (م3) pH 7,47 à 0°C ; (م4) pH 6,63 à 50°C.
  1. (م1) : 5 < 7,47 ⇒ حامضي ; (م2) : 7 < 7,47 ⇒ حامضي (piège : pH 7 n'est neutre qu'à 25°C) ; (م3) : 7,47 = pH de l'eau à 0°C ⇒ متعادل.
  2. (م4) : 6,63 = pH de l'eau à 50°C ⇒ **متعادل** (bien que < 7).
  3. (م3) à 50°C (restant neutre) : pH = **6,63**.
  - ⚠ Donnée suspecte : 98°C → 6,5. Les autres valeurs suivent les tables usuelles (pKe/2), qui donnent ≈ 6,1–6,2 vers 98–100°C ; 6,5 rompt la tendance (−0,14 pour 10°C entre 40 et 50, puis seulement −0,13 pour 48°C). Non utilisée dans les questions.
  - 📌 Seul endroit des leçons 15–22 où la variation du pH de l'eau pure avec la température est chiffrée.
- **تمرين 4** — solution + papier pH, nuancier 3.5 à 9.0 par pas de 0,5 (8 rangées de pastilles).
  1. Étapes (d'après la leçon 19) : déposer une goutte de solution (قطّارة) sur un bout de papier pH, comparer la teinte obtenue au nuancier de la boîte, lire le pH.
  2. Bandelette témoin (de haut en bas) : bleu pâle, crème, bleu pâle, **vert pâle**, magenta, bleu, bleu foncé, violet — correspond à la colonne **7.0** (seule colonne où la 4ᵉ rangée est vert pâle).
     - 1.2 : pH = 7,0.
     - 2.2 : solution **متعادل** (pH = 7) — ⚠ l'énoncé ne précise pas la température ; la conclusion suppose 25°C (cf. تمرين 3). Lecture faite à l'image 220 dpi ; couleurs imprimées proches pour 7.0/7.5 sur les rangées 5–8, mais la rangée 4 tranche.

### أستغلّ وثيقة (p. 148) — savons et shampoings
- Résumé verbatim des données : « الصّابون ... يتشكّل الصابون كيميائيّا من خلال التفاعل بين الدهون والزيوت والقلويات » ; détergents industriels (« "نظيف" و"أومو" ») : « المنظفات الشديدة القلويّة مثل الموادّ المستعملة لتنظيف البالوعات حيث تصل قيمة pH هذه المواد إلى 11 » ; shampoings contenant « السيلينيوم » ; « إنّ قيمة pH الجلد تتراوح بين 4,2 و 5,6 ... فإنّ جلد الذكور أكثر حموضة من الإناث » ; le savon pour bébés « لا يكون قلويّا بل متعادلا أو قليل الحموضة، لا يحوي ملوّنات أو عطورا، يحوي مواد مرطبة للبشرة ».
- أسئلة : 1- « حدّد مجال pH موادّ التنظيف المستعملة. » (le texte ne donne qu'une borne haute, 11 ; ⚠ réponse incomplète possible) ; 2- extraire ce qui montre que la plupart sont basiques ; 3- comparer pH peau (4,2–5,6, acide) et savons/shampoings ; 4- savon enfants légèrement acide ou neutre (peau fine, pores ouverts) ; 5- pourquoi conseiller aux filles un savon de type enfant (peau moins acide — d'après le texte).

### هل من مزيد ؟ (p. 149–150) — indicateur au chou rouge
- « يستخدم الكيميائيون كواشف لاختبار ما إذا كان المحلول حامضا أو قلويّا أو متعادلاً. » ; indicateur à partir de « الكُرنب الأحمر أو من عصير حبّ البَلَسان أو من توت العُلّيق ».
- Préparation : chou rouge coupé, eau distillée chaude, repos « نصف ساعة أو أكثر », filtration → « كاشفا ذا لون أرجوانيّ يميل إلى الحمرة القاتمة ».
- Résultats (verbatim) : « المحلول المائي الحامضي يحمرّ. – المحلول المائي القلويّ يخضرّ. – المحلول المائي المتعادل لا يؤثّر في لون الكاشف. »
  - ⚠ Photo p. 150 : le bocal légendé « محلول قلويّ » est presque noir/violet foncé, pas vert.

### أتسلّى (p. 150) — mots croisés + « من هو صاحب الصّورة ؟ »
- Définitions (verbatim) : 1 « تنتقلُ نحوه الكاتيونات » ; 2 « نوع من الشّوارد يتواجد مع الأنيون » ; 3 « محلول ذو pH=7 في 25°C » ; 4 « مزيج سائل متجانس يتكوّن من منحلّ و محل » ; 5 « خاصيّة تزداد بازدياد درجة القلويّة » ; 6 « محلول يمتاز بـ pH<7 في 25°C » ; 7 « محلول يمتاز بـ pH>7 في 25°C ».
- Réponses probables : 1 المهبط ; 2 الكاتيون ; 3 متعادل ; 4 محلول ; 5 (non résolu à coup sûr : الكاويّة / المرارة) ; 6 حامضي ; 7 قلوي. La grille n'a pas été vérifiée lettre à lettre.
- Portrait : « عالم كيميائي أثبت أنّ المحاليل الحامضيّة هي محاليل شارديّة ... اسمه الذي ينتهي بحرف السّين » (7 cases V IV I VI II III س) → Arrhenius (« أرينيوس » — graphie arabe non imprimée ; ⚠ la phrase attribue à Arrhenius la preuve que les acides sont ioniques, simplification).
- « محلّ » (4) = coquille probable pour « مُحِلّ » (solvant) — terme jamais défini dans les leçons 15–22.

### أستعين بعناوين (p. 151)
- Liste d'URL francophones (edu.cpln.ch, intellego.fr, keepschool.com, ac-versailles, ac-besancon, ac-strasbourg, lachimie.com, chimie.scola.ac-paris.fr…) sous « المحاليل الشارديّة » et « المحاليل الحامضيّة والقلويّة والمتعادلة » — sans contenu à transcrire.

### Bornes
- ✅ Définition : محلول شارديّ متعادل ⟺ pH = pH الماء النقيّ à la même température ; à 25°C : pH = 7.
- ✅ Eau pure = « سائل متعادل » / « وسط متعادل » ; exemples : NaCl, KCl, nitrate de sodium, nitrate de potassium.
- ✅ Via exercice 3 : le pH neutre dépend de la température (table chiffrée 0–98°C).
- ✅ Indicateur coloré naturel (chou rouge) en lecture complémentaire.
- ⛔ Aucune explication ionique de la neutralité (pas d'H⁺/OH⁻, pas d'égalité de concentrations).
- ⛔ Pas de réaction de neutralisation acide + base (le mot « تعادل » n'est pas pris au sens réactionnel).
- ⛔ Le terme « تعادل كهربائي » (Electroneutralité, lexique p. 213) n'apparaît pas dans les leçons.

### Vocabulaire officiel
محلول متعادل، وسط متعادل، سائل متعادل، pH neutre / pH متعادل، كلورير الصوديوم (ملح الطعام)، كلورير البوتسيوم، نيترات الصوديوم، نيترات البوتاسيوم، ميتيلأمين، فلورير الهيدروجين، بوتاس، كاشف، الكُرنب الأحمر، البَلَسان، توت العُلّيق، شامبو، صابون، منظّفات، الأسمدة، الأراضي الحمضيّة.

---

### Lexique officiel (p. 211–216, « قائمة في مصطلحات علمية مترجمة – مدخل فرنسي ») — entrées utiles aux leçons 15–22
| Français (imprimé) | Arabe (imprimé) |
|---|---|
| Acide (solution) | حامضي أو (حمضي) |
| Acide acétique | حامض الخليك |
| Acide chlorhydrique | حامض الكلورهيدريك (ماء فرق) |
| Acide sulfurique | حامض الكبريتيك |
| Acidité | حموضة |
| Alimentation (en électricité) | جهاز تغذية |
| Ammoniac | نُشادر |
| Ammoniaque (ou solution d'ammoniac) | محلول النُّشادر |
| Anion | شاردة مصعديّة (أو أنيون) |
| Atome | ذرّة |
| Bandelette | شُريط |
| Basicité | قلويّة |
| Basique (solution) | قلوي (محلول) |
| Bicarbonate de sodium | بيكربونات الصوديوم |
| Cadran | مينا (أو مرْقم) |
| Calibrage / Calibré | معايرة / معاير |
| Cation | شاردة مهبطيّة (أو كاتيون) |
| Causticité | كاويّة |
| Charge négative / positive | شحنة سالبة / شحنة موجبة |
| Chlorure | كلورير |
| Chlorure d'aluminium | كلورير الألومنيوم |
| Chlorure de sodium | كلورير الصوديوم (ملح الطعام) |
| Conductibilité | ناقليّة |
| Electrode | مَسْرى (أو إلكترود) |
| Electron | ألكترون |
| Electroneutralité | تعادل كهربائي |
| Ion / Ion négatif / Ion positif | شاردة / شاردة سالبة / شاردة موجبة |
| Ionique | شاردي |
| Neutre (solution) | متعادل (محلول) |
| Sachet | كُيَيْس |
| Sonde | مِسبَر |
| Soude caustique | صودا كاوية |
| Spatule | ملْوَق (مسْوط) |

Absents du lexique (constaté p. 211–216) : Concentration (تركيز), Solution/Soluté/Solvant, pH-mètre, papier pH, Anode/Cathode (مصعد/مهبط), Electrolyseur (محلال), Dilution. (Coquilles du lexique : « Carbonate de soduim », « Qaurtz ».)

### Leçon 23 — « انعكاس الضّوء » (ص 155–159)

محور : **الضّوء** — باب : **تغيّر مسار الضّوء** (pictogramme de séance : الملاحظة/التجربة — lunette astronomique, cf. خريطة الكتاب p. 7).

Pages d'ouverture du محور lues (p. 152–154) :
- p. 152 : page de titre « الضّوء » + sous-titre de باب « تغيّر مسار الضوء » ; photo légendée : « صورة غلاف كتاب المناظر للحسن ابن الهيثم، موسوعة فيزيائيّة من أنفس ما أنتج العرب في مجال البصريات ».
- p. 153 : « مكتسباتي القبليّة » — المعارف : 1- أعدّد مصادر الضوء. 2- أعرّف الجسم المضيء والجسم المضاء. 3- أعرّف انتشار الضوء. 4- أعرّف الوسط الشفّاف والوسط الشّاف والوسط العاتم. 5- أعرّف المصدر النقطي والمصدر الموسّع للضوء. 6- أذكر مختلف أنواع الحزم الضوئيّة. 7- أعرّف الحزمة الضوئيّة المتوازية ، الحزمة المتجمّعة والحزمة المتباعدة. 8- أذكر مبدأ الانتشار المستقيم للضوء. — المهارات : 1- أفسّر مفهوم الرؤية. 2- أميّز بين جسم مضيء وجسم مضاء. 3- أميّز بين مصدر ضوئي نقطي ومصدر موسّع. 4- أميّز بين وسط شفّاف، وسط شافّ ووسط عاتم. 5- أطبّق مبدأ الانتشار المستقيمي للضوء. 6- أميّز بين الشعاع الضوئي والحزمة الضوئيّة. 7- أميّز بين مختلف أنواع الحزم الضوئيّة. 8- أرسم مسار حزمة ضوئيّة.
- p. 154 : « تغيّر مسار الضّوء » — liste des leçons 23 à 28 ; photos « منظر لنزل بقمّرت (تونس) مع صورته المعكوسة في ماء المسبح » et « ظاهرة السراب بمنطقة الفوّار (الجنوب التونسي) » ; questions d'amorce : « لماذا تُكتَب كلمة «إسعاف» معكوسةً على سيارة الإسعاف ؟ » ; « لماذا يبدو كلّ جسم مغمور جزئيًا في بركة ماء هادئ منكسرا على مستوى سطح الماء؟ » ; « ما هي الألياف البصرية؟ وكيف تشتغل؟ » ; « ما هو السّراب ومتى وأين يظهر؟ » ; « بِمَ نفسّر ظاهرة قوس قزح؟ ».
- NB : p. 150–151 appartiennent à la fin de la partie chimie (أتسلّى : كلمات متقاطعة sur pH / محاليل ; « من هو صاحب الصّورة ؟ » — عالم كيميائي dont le nom finit par « س » ; « أستعين بعناوين » : liens web المحاليل الشارديّة / المحاليل الحامضيّة والقلويّة والمتعادلة). Hors leçons 23–30.

### Objectifs (خريطة الكتاب p. 7)
- تعريف ظاهرة انعكاس الضوء .
- ذكر قانونيْ انعكاس الضوء .
- رسم شعاع (أو حزمة ضوئيّة) منعكس.

### Déroulé

**I. ظاهرة انعكاس الضّوء**
- **أتأمّل وأتساءل** (p. 155) : « كيف لأضواء الطريق المنبعثة من سيّارة أن تتسبّب في انعدام الرؤية لسائق السيّارة التي تسير أمامها حتّى يُمنَعَ تشغيلُها حسب قانون الطرقات؟ لماذا يجب توجيه محدّد لمرآة المنوار العاكس حتّى تُضاء شاشة العرض؟ »
- **أجرّب وألاحظ** : matériel « مصدر لأشعّة ليزر ( أو فانوس مع مُكثّف يسمح بإرسال حزمة ضوئيّة متوازية) » + « جسم ذو سطح صقيل (قطعة زجاج، قطعة من ورق الألومينيوم للفّ الموادّ الغذائيّة، غطاء علبة ياغورت...) ». La حزمة ترتدّ « في منحى معاكس (الشكل1) يتغيّر بتغيير منحى السطح الصقيل أو منحى مصدر الضوء ». Pas de mesure.
- **أحلّل وأفسّر** : « على عكس الانتثار (الارتداد الذي ينتج عن ورود ضوء على سطح عادي لجسم عاتم في عدّة مناحي)، يرتدّ الضوء الوارد على سطح صقيل في منحى وحيد مرتبط بموقع السطح بالنسبة إلى المصدر. »

**II. قانونا انعكاس الضّوء** (p. 157–159)
- القانون الأوّل (قانون المستويات) — أجرّب وألاحظ : « الجهاز المخبري الخاصّ بدراسة انعكاس الضوء (الشكل2) » = مصدر حزيمة ضوئيّة S + قرص أبيض مدرّج + مرآة مسطّحة صغيرة M. La حزيمة suit un diamètre du disque (شكل3) ; miroir posé sur un diamètre non perpendiculaire : tache IR sur le disque, « أمام المرآة ومن الجهة الأخرى للعمود القائم IN على العاكس المسطّح M في نقطة الورود I (شكل4) ».
  - أحلّل وأفسّر : « ...فإنّ الشعاع المنعكس IR يوجد في نفس المستوي الحاوي للشعاع الوارد SI وللعمود NI والمعروف بمستوي الورود (SI ، NI) ».
- القانون الثاني (قانون الزوايا) — أجرّب وألاحظ (p. 158) : définition des deux angles (voir encadrés), rotation du disque, mesures (tableau imprimé) :

| i(°) | 0 | 10 | 20 | 30 | 45 | 60 | 70 | 80 | 87 |
|---|---|---|---|---|---|---|---|---|---|
| r(°) | 0 | 10 | 20 | 30 | 45 | 60 | 70 | 80 | 87 |

  Consigne : « أقارن مقدار كلّ زاوية r بمقدار الزاوية i الموافقة لها. » → r = i pour les 9 mesures (vérifié : égalité stricte colonne par colonne).

### Encadrés (VERBATIM)
- أستنتج (p. 156) : « كلما ورد الضوء على سطح صقيل يحدث له ارتداد في منحى معيّن دون غيره يسمّى انعكاسا. »
- **تعريف** : « انعكاس الضوء هو ارتداده في منحى معيّن دون غيره على مستوى سطح صقيل. »
  (schéma S → I → R, surface en I)
- **تعريفات أخرى** :
  - « *يسمّى السطح الذي يحدث على مستواه انعكاس الضوء عاكسا. »
  - « * يسمّى الضوءُ ( الحزمة الضوئيّة، الشعاع الضوئي SI ) المتّجِهُ نحو العاكس ضوءا واردا (حزمةً واردةً، شعاعا واردا) »
  - « * يسمّى الضوءُ (الحزمة الضوئيّة، الشعاع الضوئي IR المُرتدُّ على مستوى العاكس ضوءا منعكسا ( حزمةً منعكسةً، شعاعا منعكسا). » [sic : parenthèse ouvrante non refermée avant « المُرتدُّ »]
  - « * تسمّى نقطةُ التقاء الشعاع الوارد على العاكس نقطةَ الورود(I) »
- Définitions des angles (p. 158, texte courant) : « – زاوية i ناتجة عن تقاطع الشعاع الوارد (SI) مع العمود (NI) في نقطة الورود وتسمّى زاوية الورود. » ; « – زاوية r ناتجة عن تقاطع الشعاع المنعكس (IR) مع العمود (NI) في نقطة الورود وتسمّى زاوية الانعكاس (شكل5) . »
- أستنتج (p. 158) : « نص القانون الأوّل للانعكاس (قانون المستويات): ينتشر الشعاع المنعكس في مستوي الورود »
- أستنتج (p. 159) : « نص القانون الثاني للانعكاس (قانون الزوايا): قيمة زاوية الانعكاس تساوي قيمة زاوية الورود <=> r = i »
- ملاحظة (p. 159) : « يُرمز دائما إلى المرآة المسطحة كما ورد آنفا وكما هو مشار إليه في الشكل6. » (trait hachuré ; légende « وجه المرآة العاكس » côté non hachuré).
- Symboles : S (source), I (نقطة الورود), R, N / NI / IN (العمود), SI, IR, M (مرآة), i, r, angles en degrés (°). Formule unique : **r = i**.

### Exercices
- أقيّم مكتسباتي (p. 156) : « أعيد نفس التجربة مستعملا مرآة كجسم ذي سطح صقيل. أسجّل ملاحظاتي وأستنتج أنّ المرآة قادرة على القيام بدور العاكس. » (qualitatif)
- أقيّم مكتسباتي (p. 159) : « أنسخ الشكل المقابل ( الشكل7) ثمّ أرسم مسار الحزمة الضوئيّة الناتجة عن انعكاس الحزمة الضوئيّة المنبعثة من المصدر النقطي S على المرآة المسطّحة M. » — réponse : tracer en chaque point d'incidence la normale et le rayon réfléchi avec r = i ; les rayons réfléchis semblent provenir du symétrique S' de S par rapport à M (construction non enseignée dans cette leçon — elle vient en L24). Pas de données chiffrées.
- Aucune rubrique « أتمرّن » / « أتسلّى » dans cette leçon (p. 155–159).

### Bornes
✅ Distinction انعكاس / انتثار (surface صقيل vs سطح عادي لجسم عاتم) ; vocabulaire عاكس، ضوء وارد، ضوء منعكس، نقطة الورود، العمود، مستوي الورود، زاوية الورود، زاوية الانعكاس ; 2 lois (المستويات، الزوايا) ; symbolisation de la مرآة مسطّحة ; tracé d'un rayon réfléchi.
⛔ Angles mesurés par rapport à la **normale** (NI), jamais par rapport à la surface — aucun angle rasant n'est défini. Le cas i = 90° n'est pas mesuré (max 87°). Pas de miroir courbe (concave/convexe) dans la leçon. Aucune notion quantitative de « proportion de lumière réfléchie ». Le mot « انتثار » est cité mais pas défini par un encadré.

### Vocabulaire officiel
انعكاس الضوء (réflexion de la lumière — cf. lexique) ; سطح صقيل ; الانتثار (diffusion) ; عاكس (réflecteur) ; ضوء / حزمة / شعاع وارد (incident) ; ضوء / حزمة / شعاع منعكس (réfléchi) ; نقطة الورود (point d'incidence) ; العمود / العمود القائم (normale) ; مستوي الورود (plan d'incidence) ; زاوية الورود (angle d'incidence) ; زاوية الانعكاس (angle de réflexion) ; قانون المستويات ; قانون الزوايا ; مرآة مسطّحة (miroir plan) ; قرص مدرّج ; حزيمة ضوئيّة ; مصدر نقطي ; منوار (projecteur). [Correspondances FR : voir lexique p. 211–223, relevé dans L30.md.]

### Leçon 24 — « المرآة المسطّحة » (ص 160–169)

محور : **الضّوء** — باب : **تغيّر مسار الضّوء** (pictogramme de séance : livre = حصّة تطبيقيّة/وثائقيّة, cf. خريطة p. 7). La leçon inclut la **خلاصة commune L23+L24** (p. 164) et la section « أعوّل على نفسي » (p. 165–169) qui porte sur les deux leçons.

### Objectifs (خريطة الكتاب p. 7)
- رسم صورة جسم ما عبر مرآة مسطّحة.

### Déroulé
- **أتأمّل وأتساءل** (p. 160) : « لماذا تكتب عبارة "AMBULANCE" معكوسة كما يلي "ƎƆИA⅃UᗺMA" وكما هي في الشكل 1 على الواجهة الأماميّة لسيارة إسعاف؟ » ; « بِمَ أفسّر مشاهدة صورتي كلّما نظرت في مرآة كما هو الشأن لتلك الأشياء في الشكل2؟ » ; « ما هي خاصيّة المرآة العاكسة التي تمكّن سائقَ سيّارة رؤية ما خلفه كما هو في الشكل3؟ »
- **أجرّب وألاحظ** (p. 161–162) : matériel « شمعتان (ش1) و (ش2) متطابقتان شكلا وطولا » ; « صفيحة من الزجاج الرقيق » ; « مِنصَب مُسطّح أُحدِث فيه أخدود يسمح بتثبيت صفيحة الزجاج شاقوليّا » ; « كوس، مسطرة ودبّوسان اثنان ملوّنان ».
  - ش1 allumée en A, dans l'obscurité ; vue à travers la vitre : image en A' ; « أحاول مسكها فلا أجد شيئا. ما هي إذن طبيعة هذه الصورة؟ »
  - ش2 non allumée déplacée derrière la vitre jusqu'à coïncider avec l'image en A' → paraît allumée ; en éteignant ش1, « فيختفي لهب الشمعة (ش2) ».
  - Repérage de A et A' par les دبّوسان ; « فألاحظ أنّ المستقيم (A A') والأخدود متعامدان في النقطة I. (الشكل7) » ; « أقيس طول كلّ من قطعتي المستقيم [AI] و[IA'] بالمسطرة فألاحظ تساويهما. إذن فالنقطتان A و A' متناظرتان بالنسبة للأخدود. » (aucune valeur numérique donnée).
- **أحلّل وأفسّر** (p. 162–163) : « مُشاهدةُ صورة الشمعة المشتعلة (ش1) عبر صفيحة الزجاج دليلٌ على ورود ضوء على شبكة العين متأتٍّ من الشمعة (ش1) بعد انعكاسه على الصفيحة. وبالتالي لعبت صفيحة الزجاج دور المرآة المسطّحة. » Construction : rayon SI → rayon réfléchi IR via « قانونَيْ الانعكاس ثمّ امتداده خلف المرآة (الشكل9) » ; 2e rayon SI' : « ...فألاحظ أنّ امتداد الشعاع المنعكس I'R' يتقاطع مع امتداد الشعاع IR في النقطة 'S المتناظرة مع S بالنسبة لمستوي المرآة. وهذا يُعمّم على كلّ الأشعّة المنبعثة من النقطة S. » ; « وبالتالي تبدو الحزمة الضوئيّة المنعكسة على المرآة والواردة على العين كأنّها منبعثة من النقطة 'S (الشكل10). » ; « وكذا لكلّ النقاط الضوئيّة للشمعة فتكوِّن النقاطُ المتناظرةُ لها الصُّورةَ الافتراضيّة التي تشاهدها العين للشمعة (الشكل11). »

### Encadrés (VERBATIM)
- **أستنتج** (p. 163) : « تعطي المرآة المسطّحة لجسم حقيقيّ صورةً افتراضيّةً متناظرةً معه بالنسبة لها. »
- **الخلاصة** (p. 164, commune L23–L24) :
  - « على عكس الانتثار، انعكاسُ الضوء هو تغيّرٌ لمسار الضوء في منحى معيّن دون غيره. »
  - « انعكاس الضوء ظاهرةٌ فيزيائيّةٌ تخضع لقانونين اثنين : »
  - « *القانون الأوّل (قانون المستويات) : ينتشر الشعاع المنعكس في مستوي الورود »
  - « *القانون الثّاني (قانون الزوايا) : قيمة زاوية الانعكاس تساوي قيمة زاوية الورود <=> r = i »
  - « ينتج عن انعكاس الضوء المنبعث من جسم حقيقيّ على مرآة مسطّحة صورةٌ افتراضيّةٌ متناظرةٌ لذلك الجسم بالنسبة لمستوي المرآة. »
- Symboles : A, A', S, S', I, I', R, R', N, N', M, AB / A'B' ; convention (Ex 5) : « كلّ ما هو افتراضيّ رُسِمَ بخطّ مُنقَّط ».

### Exercices — « أعوّل على نفسي : أتمرّن على حلّ المسائل » (p. 165–167)
- **تمرين 1** : reproduire le schéma et compléter les étiquettes (الشعاع ...، زاوية ...، نقطة ...). Réponse : الشعاع الوارد، الشعاع المنعكس، زاوية الورود i، زاوية الانعكاس r، نقطة الورود، العمود (النّاظم) — le schéma porte i (secteur rouge) et r (secteur vert).
- **تمرين 2 (QCM)** :
  1. « شعاع وارد في منحى مائل بزاوية قدرها66° مع مرآة مسطّحة ينعكس تحت زاوية انعكاس ذات قيمة: أكبر من66° / تساوي66° / تساوي24° ». Calcul : angle avec la **surface** = 66° ⇒ i = 90 − 66 = **24°** ⇒ r = 24° → « تساوي24° ». ⚠️ Piège : la leçon ne définit que des angles par rapport à la normale ; l'exercice exige la conversion 90° − 66° jamais montrée dans le cours.
  2. « تعطي المرآة المسطّحة لكلّ جسم حقيقيّ AB: صورة حقيقيّة 'A'B متطابقة مع الجسم AB / صورة حقيقيّة 'A'B أكبر من الجسم AB / صورة افتراضيّة 'A'B متطابقة مع الجسم AB / صورة افتراضيّة 'A'B متناظرة مع الجسم AB بالنسبة للمرآة » → réponse attendue : la dernière. ⚠️ Ambiguïté : « افتراضيّة ... متطابقة مع الجسم » est aussi défendable (même taille) ; seule la formulation « متناظرة » reprend l'encadré.
- **تمرين 3** (compléter avec : الجسم، الانتثار، وارد، الحقيقيّ، صورة، سطح، منحى، متناظرا، الافتراضيّة، الضوء المنعكس، الانعكاس) — réponses :
  1. « يَحدث **الانعكاس** عوضا عن **الانتثار** لمّا يرد الضوء على **سطح** صقيل. »
  2. « يتميّز **الضوء المنعكس** على مرآة بانتشاره في منحى وحيد مرتبط بـ**منحى** الضوء الوارد عليها. »
  3. « تُعطي المرآة المسطّحة لكلّ شعاع ضوئيّ **وارد** عليها شعاعا منعكسا **متناظرا** مع الشعاع الوارد بالنسبة إلى العمود على نقطة الورود. »
  4. « تختصّ **صورة** الجسم **الحقيقيّ** المتكوّنةُ عبر مرآة مسطّحة بصفتها **الافتراضيّة** وبتناظرها مع **الجسم** بالنسبة إلى المرآة. »
- **تمرين 4** (صحيح/خطأ) : 1. « يحدث الانعكاس كلّما ورد الضوء على سطح جسم صلب. » → خطأ (سطح صقيل). 2. « يمكن أن ينعكس شعاع ضوئيّ على مرآة في نفس منحى الورود. » → صحيح (i = 0 ⇒ r = 0, retour sur lui-même ; le tableau p. 158 contient i = 0). 3. « تتصف صورة جسم حقيقيّ في مرآة مسطّحة بتناظرها بالنسبة إلى العمود المقام على المرآة. » → خطأ (symétrie par rapport au plan du miroir). 4. « تحصل في المرآة صورة لكلّ جسم حقيقيّ نتيجة مرور الضوء من خلالها. » → خطأ (réflexion, pas traversée). 5. « يظهر الضوء المنعكس على مرآة مسطّحة وكأنّه منبعث من صورة مصدره. » → صحيح.
- **تمرين 5** : choisir, pour 3 cas, le bon schéma de l'image de AB (virtuel = pointillé). Lecture à 200 dpi :
  - الحالة1 (AB vertical) : bon = schéma **central** (A'B' pointillé, même taille, A' à la même distance du miroir que A — mesuré ≈ 113 vs 117 px). Faux : A'B' collé au miroir ; A'B' deux fois plus loin (≈ 207 vs 118 px).
  - الحالة2 : bon = schéma de **gauche** (pointillé, même hauteur). Faux : A'B' en trait plein (image réelle) ; A'B' plus grand.
  - الحالة3 (AB incliné, B s'écartant du miroir) : bon = schéma de **droite** (B' incliné en s'écartant du miroir, symétrique). Faux : A'B' vertical ; A'B' simplement translaté (même inclinaison).
- **تمرين 6** : tracer, parmi les rayons issus de S, celui qui passe par A après réflexion sur M. Réponse : construire S' symétrique de S / M, tracer (S'A) qui coupe M en I, puis SI et IA.
- **تمرين 7** : « انسخ رسم الشكل المقابل ثمّ أكمِلهُ برسم مستوي سطح المرآة M في المنحى الذي يضمن مرور الشعاع الوارد (SI) بالنقطة A بعد انعكاسه في النقطة I. » Réponse : la normale en I est la bissectrice de l'angle SIA ; la surface est perpendiculaire à cette bissectrice en I.
- **تمرين 8** : deux miroirs plans M1, M2 parallèles (verticaux, face à face) ; SI arrive sur M1 avec l'angle 45° marqué entre SI et l'horizontale pointillée (= la normale) ⇒ i = 45°. 1. compléter le trajet : réflexions alternées toutes à 45°, zigzag descendant. 2. « سواء بالترفيع أو بالتنقيص من قيمة زاوية الورود SI بيّن أنّه يمكن جعل الشعاع المنبثق من بين المرآتين موازيا للشعاع الوارد SI . » Calcul : chaque réflexion inverse la composante horizontale ; après un nombre **pair** de réflexions la direction est celle de SI (parallèle), après un nombre impair elle est symétrique. ⚠️ Énoncé elliptique : la longueur des miroirs et l'écart ne sont pas donnés ; le « parallélisme » dépend de la parité du nombre de réflexions, qu'on règle en changeant i — c'est ce que l'exercice attend, mais ce n'est pas dit.
- **تمرين 9** : deux miroirs M1 ⊥ M2 (dièdre droit). Trajet : après réflexion sur M1 puis M2, le rayon ressort **parallèle et de sens opposé** à SI (i1 + i2 = 90°). Non formulé dans le manuel, conclusion calculée.
- **أستغلّ وثيقة : « المرآة المسطّحة »** (p. 167–168) : « تتكوّن المرآة العاديّة المستعمَلة في حياتنا اليوميّة من طبقة رقيقة من القصدير الممزوج بالزئبق مبسوطة على السطح الخلفي للوح من الزجاج ومحميّة بطلاء من مادّة داكنة اللون. إلاّ أنّ هذا النوع من المرآة لا يُستعمل في صناعة الأجهزة البصريّة الدقيقة مثل المجهر والتلسكوب وغيرها لعدّة أسباب منها أنّ جزءا من الضوء ينعكس على السطح الأمامي للزجاج قبل أن يصل إلى الطبقة المعدنية العاكسة. لذلك تُصنَع المرايا لمثل هذه الأجهزة بصقل السطح الزجاجي صقلا جيّدا ليصل إلى درجة عالية من النعومة ثم يتمّ طليُه بطبقة معدنيّة رقيقة جدّا من الفضّة أو الألومنيوم قادرة على عكس معظَم الأشعّة الواردة عليها. » Questions : 1. ce qui montre que l'élément réfléchissant est la couche métallique (« ...لا يُستعمل... لأنّ جزءا من الضوء ينعكس على السطح الأمامي للزجاج قبل أن يصل إلى الطبقة المعدنية العاكسة » ; « الطبقة المعدنيّة... قادرة على عكس معظم الأشعّة »). 2. cause de la réflexion sur la face avant du verre : la surface du verre est صقيلة (lisse) — réponse déduite, non écrite.
- **أجرّب بنفسي : « المُشاكل (أو منظار النماذج المتغيّرة) »** (kaléidoscope, p. 168–169) : 3 miroirs rectangulaires 250mm x 50mm ; carton 200mm x 254mm ; colle. Collage en laissant 2mm de chaque côté, écart 5mm entre miroirs ; pliage en prisme triangulaire. Vérif : 3 × 50 + 2 × 5 = 160 mm de hauteur utilisée sur 200 mm ; 250 + 2 × 2 = 254 mm ✔. Il reste 200 − 160 = 40 mm de carton : c'est « الجزء المتبقّي » collé après pliage (p. 169) — cotes cohérentes. « ملاحظة : يمكنني صنع مُشاكلِ ذي خمسة وجوه عوضا عن ثلاثة... »
- **هل من مزيد ؟ « كتاب المناظر لابن الهيثم »** (p. 169) : œuvre « في القرن الحادي عشر الميلادي » ; « الانتشار المستقيمي والانعكاس » ; réfutation de Ptolémée (« زعم بطليموس أنّ الرؤية تتمّ بواسطة أشعّة تنبعث من العين إلى الجسم المرئي ») ; « أثبت أنّ الرؤية تتمّ بواسطة الأشعّة المنبعثة من الجسم المرئي باتّجاه عين المبصر ».

### Bornes
✅ Image d'un objet réel dans un miroir plan : **virtuelle**, **symétrique** par rapport au plan du miroir (même distance, même taille implicite) ; construction par prolongement des rayons réfléchis ; construction d'un rayon passant par un point donné ; systèmes de 2 miroirs (parallèles, perpendiculaires) en exercice.
⛔ Pas de champ de vision du miroir, pas de formule de distance chiffrée (aucune distance objet/image numérique), pas d'image réelle par miroir, aucun miroir sphérique. La notion « image inversée gauche/droite » n'est évoquée que par l'exemple AMBULANCE (question d'amorce), sans énoncé. « متطابقة » n'est pas défini ; la taille de l'image n'est jamais énoncée dans un encadré (seulement via Ex 2 et Ex 5).

### Vocabulaire officiel
المرآة المسطّحة (miroir plan) ; صورة افتراضيّة (image virtuelle) ; صورة حقيقيّة (image réelle, en distracteur) ; جسم حقيقيّ (objet réel) ; متناظر / التناظر (symétrique) ; مستوي المرآة ; امتداد الشعاع ; شبكة العين (rétine) ; صفيحة الزجاج ; أخدود ; المُشاكل / منظار النماذج المتغيّرة (kaléidoscope) ; المجهر ; التلسكوب ; الطبقة المعدنيّة العاكسة ; كتاب المناظر ; ابن الهيثم ; بطليموس. [FR : cf. lexique relevé dans L30.md.]

### Leçon 25 — « انكسار الضّوء » (ص 170–175)

محور : **الضّوء** — باب : **تغيّر مسار الضّوء** (séance expérimentale, pictogramme lunette).

### Objectifs (خريطة الكتاب p. 7)
- تعريف ظاهرة انكسار الضوء.
- ذكر قانونيْ انكسار الضوء.
- رسم شعاع (أو حزمة ضوئيّة) منكسر.

### Déroulé
- **أتأمّل وأتساءل** (p. 170) : « عندما أغمس جسما صلبا مستقيما (محراك، مسطرة، قلم...) في كأس به ماء، يبدو لي ذلك الجسم وكأنّه مُنكسر .ما سبب ذلك؟ » (photo : « نفس القلم في كأس فارغة على اليمين وفي كأس بها ماء على اليسار ») ; « عندما أنظر من فوق إلى جسم في قاع حوض أو إناء به ماء أرى الجسم على عمق أقل من العمق الحقيقي. بما أفسّر ذلك؟ »
- **I. ظاهرة الانكسار — أجرّب وألاحظ** : laser (ou فانوس + مكثّف, حزمة متوازية) + « حويض به ماء ملوّن ». Observation : « عندما ترد الحزمة الضوئيّة المنبعثة من المصدر تواصل انتشارها في السائل بشيء من الانحراف. وفي نفس الوقت يرتدّ جزء منها على السطح في منحى متناظر مع منحى الحزمة الواردة بالنسبة إلى العمود على سطح الماء في نقطة الورود.(الشكل1) »
  - 2e expérience (p. 171) : même dispositif que L23 (S + قرص أبيض مدرّج) + « نصف اسطوانة من البلاستيك الشفّاف (بليكسيقلاس) (P) », centre I au centre du disque (شكل 2) ; la حزمة traverse le plexiglas « بشيء من الانحراف على مستوى نقطة الورود وينعكس جزء منها.(الشكل3) »
  - **أحلّل وأفسّر** : « تنتشر الحزمة الضوئيّة المنبعثة من المصدر المستعمَل في الهواء ولكنّ مسارها ينحرف عند اختراقها الماء أو البليكسيقلاس على مستوى السطح الفاصل بين كلّ من هذين الوسطين الشفّافين والهواء. وهذا يعني أنّ مرور الضوء من الهواء إلى الماء أو من الهواء إلى البليكسيقلاس تسبّب في تغيير مساره، وتعرف هذه الظاهرة بانكسار الضوء. زيادة على ظاهرة الانكسار حصل للضوء انعكاس في كلتا الحالتين وكان ذلك متوقّعا في التجربة الثانية لأنّ البليكسيقلاس جسم صُلبٌ ذو سطح صَقيل، أمّا في التجربة الأولى رغم أنّ الماء ليس بالجسم الصلب فقد أمكن لسطحه لعب دور العاكس. »
- **II. القانون الأوّل (قانون المستويات)** (p. 173) — même expérience, trace IR dans le plexiglas ; « ...فإنّ الشّعاع المنكسرIR يوجد في المستوي الحاوي للشّعاع الوارد SI و للعمود NI والمعروف بمستوي الورود (SI,NI) (الشّكل3). »
- **III. القانون الثّاني : قانون الزّوايا** (p. 173–174) : définitions i (SI avec NI) et r (IR avec NI) « وتسمّى زاوية الانكسار » (الشكل4). Rotation : « فألاحظ أنّ الشعاع IR ينعطف نحو العمود ويزداد هذا الانعطاف كلّما كان منحى الشعاع الوارد مقتربا أكثر من سطح البليكسيقلاس والعكس بالعكس. »
  - Tableau imprimé (air → plexiglas) :

| i(°) | 0 | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 89 |
|---|---|---|---|---|---|---|---|---|---|---|
| r(°) | 0 | 6.5 | 13 | 19 | 26 | 31 | 36 | 39 | 41 | 41.8 |

  - Texte : « ...فألاحظ أنّ قيمة زاوية الانكسار ترتفع بارتفاع قيمة زاوية الورود i إلاّ أنّها تبقى دائما هي الصغرى دون أن تتجاوز قيمة 42° ( يشار عادة إلى هذه القيمة القصوى بالحرف اللاتيني λ ). »
  - Recalcul (loi de Snell-Descartes, **non enseignée dans le manuel**, pour contrôle seulement) avec n = 1,5 : r = 0 ; 6.6 ; 13.2 ; 19.5 ; 25.4 ; 30.7 ; 35.3 ; 38.8 ; 41.0 ; 41.8. Le tableau est cohérent à ±0,7° (écarts max : 26 vs 25.4 ; 36 vs 35.3) ; arcsin(1/1,5) = 41.81° ✔ (λ ≈ 42°).
  - Eau (demi-cylindre d'eau, شكل5) : « ...انكسار الضوء صار أقلّ حدّة ... ممّا انجرّ عنه الحصول على زاوية انكسار قصوى λ' = 49° أكبر من λ = 42° . لهذه الأسباب نقول إنّ البليكسيقلاس وسط شفّاف يتميّز بانكساريّة أهمّ من انكساريّة الماء. » Contrôle : arcsin(1/1,33) = 48.75° ≈ 49° ✔.

### Encadrés (VERBATIM)
- **أستنتج** (p. 172) : « عند ورود الضوء على السطح الفاصل بين وسطين شفّافين ينعطف إلى الوسط الثاني ولا ينفذ على استقامته، وتسمّى هذه الظاهرة انكسار الضوء. »
- **تعريف** : « انكسار الضوء هو التغيّر الذي يحصل لمساره عند مروره من وسط شفّاف إلى وسط شفّاف آخر » (schéma S, N, I, N', R ; « وسط1 » / « وسط2 »)
- **تعريفات أخرى** :
  - « * يسمّى الضوءُ ( الحزمة الضوئيّة، الشعاع الضوئي SI) المتّجهُ نحو السطح الفاصل بين الوسطين الشفّافين ضوءا واردا (حزمةً واردةً، شعاعا واردا) »
  - « * يسمّى الضوءُ (الحزمة الضوئيّة، الشعاع الضوئي IR) المُنعطف في مستوى السطح الفاصل بين الوسطين الشفّافين ضوءا منكسرا (حزمةً منكسرة، شعاعا منكسرا). »
  - « * تسمّى نقطةُ التقاء الشعاع الوارد والسطح الفاصل بين الوسطين الشفّافين نقطةَ الورود (I) »
- **أستنتج** (p. 173) : « نص القانون الأوّل للانكسار (قانون المستويات): ينتشر الشعاع المنكسر في مستوي الورود »
- **أستنتج** (p. 175) : « نص القانون الثاني للانكسار (قانون الزوايا): في كلّ انكسار ينتج عن مرور الضوء من الهواء إلى وسط شفّاف آخر تنعطف الأشعّة نحو العمود المقام على السطح الفاصل بين الوسطين بحدّة مرتبطة بانكساريّة ذلك الوسط <=> r < i »
  « عند انعطاف الضوء من الهواء إلى وسط شفّاف آخر يكون الانكسارُ أكثرَ حِدّة وبالتالي تكون القيمة القصوى لزاوية الانكسار أصغرَ كلّما كان الوسط الثاني أكثر انكساريّة. »
- **أمثلة** (axe « زاوية الانكسار القصوى λ », flèche « اتجاه ارتفاع الانكساريّة » vers la gauche) : الماس 24.3° ; الزجاج (intervalle pointillé 36° ↔ 42°) ; البليكسيقلاس 42° ; الماء 49°. Contrôle (n = 1/sin λ, non enseigné) : 2.43 ; 1.70–1.49 ; 1.49 ; 1.33 ✔.
- Symboles : S, I, R, N, N', P (plexiglas), i, r, **λ, λ'** (زاوية الانكسار القصوى), relation **r < i**. Aucun indice de réfraction « n », aucune formule sin.

### Exercices
- **أقيّم مكتسباتي** (p. 175) : comparer انكساريّة الزجاج et الماء (air→eau puis air→verre, حزمة متوازية).
  1. « هل أتمكّن من المقارنة المقصودة إذا ما ورد الضوء في منحى العمود المقام على السطح الفاصل بين الوسطين الشفّافين؟ لماذا؟ » → Non : i = 0 ⇒ r = 0 dans les deux milieux (tableau : i = 0, r = 0), pas de déviation à comparer.
  2. « إذا ما كانت قيمة زاوية الورود تساوي i=30° أحصل على حزمة ضوئيّة منكسرة ذات زاوية انكسار r = 22° بالنسبة إلى الماء وr =19° بالنسبة إلى الزجاج. أحدّد إذن من بين الوسطين (الماء والزجاج) أيّهما الأكثر انكساريّة. » → le **زجاج** (r plus petit ⇒ انعطاف plus fort). Contrôle Snell : n_eau = sin30/sin22 = 1.335, n_verre = sin30/sin19 = 1.536 ✔.
- Aucune série « أتمرّن على حلّ المسائل » propre à L25 : elle est regroupée après L26 (voir L26.md).

### Incohérences / points à signaler
- ⚠️ « يشار عادة إلى هذه القيمة القصوى بالحرف **اللاتيني** λ » : λ (lambda) est une lettre **grecque**, pas latine.
- ⚠️ Loi énoncée « r < i » sans exception, alors que le tableau de la même page et l'exercice 1 donnent i = 0 ⇒ r = 0 (égalité) ; l'inégalité n'est stricte que pour i ≠ 0.
- ⚠️ La loi est restreinte au passage **air → autre milieu** ; le sens inverse (r > i) n'apparaît qu'en L26.
- Le terme « λ » désigne ici l'**angle de réfraction limite** (air → milieu) ; en L26 le même λ sert d'angle limite d'incidence (milieu → air). Même valeur, rôle inversé — cohérent physiquement (retour inverse) mais jamais explicité.

### Bornes
✅ Définition du انكسار ; coexistence انكسار + انعكاس partiel à l'interface ; 2 lois qualitatives (مستويات ; r < i avec « انعطاف نحو العمود ») ; notion qualitative de **انكساريّة** d'un milieu ; angle de réfraction maximal λ (valeurs : ماس 24.3°، زجاج 36–42°، بليكسيقلاس 42°، ماء 49°).
⛔ **Aucune loi de Snell-Descartes (n1 sin i1 = n2 sin i2), aucun indice de réfraction n, aucun sinus** : la انكساريّة n'est jamais quantifiée autrement que par λ. Pas de profondeur apparente calculée (seulement la question d'amorce). Pas de vitesse de la lumière dans les milieux. Pas de lentilles.

### Vocabulaire officiel
انكسار الضوء (réfraction) ; السطح الفاصل ; وسط شفّاف ; الانحراف ; ينعطف / الانعطاف ; ضوء / حزمة / شعاع منكسر (réfracté) ; زاوية الانكسار ; زاوية الانكسار القصوى λ ; الانكساريّة (réfringence) ; بليكسيقلاس (plexiglas) ; نصف اسطوانة ; حويض ; الماس (diamant) ; الزجاج ; مستوي الورود ; قانون المستويات ; قانون الزوايا. [FR : cf. lexique relevé dans L30.md.]

### Leçon 26 — « الانكسار الحدّي والانعكاس الكلّي » (ص 176–181)

(Titre en tête de page 176 : « الإنكسار الحدّي والإنعكاس الكلّي » — hamza sur l'alif ; خريطة p. 7 : « الانكسار الحدّي والانعكاس الكلّي ».)
محور : **الضّوء** — باب : **تغيّر مسار الضّوء** (séance expérimentale). La خلاصة p. 178 et la série « أعوّل على نفسي » p. 179–181 couvrent **L25 + L26**.

### Objectifs (خريطة الكتاب p. 7)
- تفسير ظاهرتي الانكسار الحدّي والانعكاس الكلّي.

### Déroulé
- **I. الإنكسار من وسط شفّاف ما إلى الهواء — أجرّب وألاحظ** (p. 176) : même dispositif (S, قرص أبيض مدرّج, نصف اسطوانة بليكسيقلاس (P)), mais la حزمة entre « عموديّا على الوجه الاسطواني لينفذ الضوء في البليكسيغلاس [sic, graphie « البليكسيغلاس » ici vs « بليكسيقلاس » ailleurs] على استقامته دون أيّ انحراف ويصل إلى المركز I من الوجه المستوي للبليكسيقلاس تحت زاوية ورود صغيرة ( i=20° مثلا) كما في الشكل1. » Observation : « ...تنعطف إلى الهواء في النقطة I ولكن نحو السطح الفاصل بين البليكسيقلاس والهواء ( الوجه المستوي لنصف الأسطوانة) عكس ما حصل سابقا في الانعطاف من الهواء إلى البليكسيقلاس. (الشكل2) » ; avec l'eau (وعاء نصف دائري) : mêmes observations « ولكن مع انعطاف أقلّ حدّة ممّا كان عليه مع البليكسيقلاس. »
- **II. تأثير منحى الورود على الإنكسار** (p. 177) : rotation depuis i = 0° :
  - « حياد الحزيْمة المنكسرة IR عن العمود المقام IN أكثر من حياد الحزيْمة الواردة عن نفس العمود، وهذا يعني أنّ قيمة زاوية الانكسار r ترتفع مع ارتفاع قيمة زاوية الورود i ولكن دائما مع r > i »
  - « في الوقت نفسه ومع الحزيْمَة المنكسرة ظهُورَ حزيْمة منعكسة يزداد إشراقها مع ارتفاع قيمة زاوية الورود i على حساب إشراق الحزيْمة المنكسرة. »
  - « اقترابا شديدا للحزيْمة المنكسرة من الوجه المستوي للبليكسيقلاس(r ≈ 90°) عندما تقارب قيمة زاوية الورود i القيمة الحرجة λ = 42° ثمّ اختفاءً كليًّا لها عندما تتجاوز قيمة i القيمة λ في حين أنّ الحزيْمَة المنعكسة تبقى شديدة الإشراق. »
  - Eau : « ...الاختفاء الكلّيّ للحزيْمة المنكسرة عند بلوغ قيمة زاوية الورود i القيمَةَ الحرجة λ' = 49° عوضا عن القيمة λ = 42°. »
  - Aucune table de mesures dans cette leçon.

### Encadrés (VERBATIM)
- **أستنتج** (p. 177) :
  - « ➤ كما هو الشأن للانكسار من الهواء إلى وسط شفّاف آخر يحصل للضوء انكسار كلّما مرّ من وسط شفّافٍ مَا إلى الهواء ولكن بانعطاف نحو السطح الفاصل بين الهواء والوسط الشفّاف الآخر. <=> r > i ( الشّكل3) » (schéma : « وسط شفّاف » en haut, « هواء » en bas)
  - « ➤ في كلّ انكسار ناتج عن مرور الضوء من وسط شفّاف ما إلى الهواء تنعطف الأشعّة الضوئيّة نحو السطح الفاصل بين الهواء والوسط الشفّاف بحدّة مرتبطة بانكساريّة ذلك الوسط . »
- **أستنتج** (p. 178) :
  - « ➤ كما يحصل عند المرور من الهواء إلى وسط شفّاف آخر يحصل صحبةَ الانعكاس انكسارٌ للضوء عند مروره من وسط شفّافٍ مَا إلى الهواء، إلاّ أنّ الانكسار يصبح مستحيلا عندما تبلغ قيمة زاوية الورود قيمةً حرجة مرتبطةً بانكساريّة ذلك الوسط الشفّاف وتسمّى هذه الظاهرةُ الانكسارَ الحدّي. »
  - « ➤ يترتّب عن الانكسار الحدّي انعكاسٌ كلّي للضوء في مستوى السطح الفاصل بين الوسط الشفّاف والهواء. »
- **الخلاصة** (p. 178, L25 + L26) :
  - « الانكسار هو مثال آخر لتغيّر مسار الضوء ولكن عند مروره من وسط شفّاف إلى وسط شفّاف آخر. »
  - « انكسار الضوء ظاهرةٌ فيزيائيّة تخضع لقانونين اثنين: – القانون الأوّل (قانون المستويات) ينتشر الشعاع المنكسر في مستوي الورود – القانون الثّاني (قانون الزوايا) في كلّ انكسار ينتج عن مرور الضوء من الهواء إلى وسط شفّاف آخر(الحالة الأولى) أو من ذلك الوسط الشفّاف إلى الهواء (الحالة الثانية) تنعطف الأشعّة بحدّة مرتبطة بانكساريّة ذلك الوسط: – نحو العمود المقام على السطح الفاصل بين الوسطين في الحالة الأولى <=> r < i – نحو السطح الفاصل بين الوسطيْن في الحالة الثانية <=> r > i »
  - « يتمثّل الانكسار الحدّي في استحالة الانكسار عند مرور الضوء من وسط شفّاف إلى الهواء إذا تجاوزت قيمة زاوية الورود قيمة الزاوية الحرجة ويترتّب عن ذلك انعكاس كلّي للضوء. »
- Symboles : **λ = 42°** (بليكسيقلاس), **λ' = 49°** (ماء) nommées « القيمة الحرجة / الزاوية الحرجة » ; r > i ; r ≈ 90°.

### Exercices — « أعوّل على نفسي : أتمرّن على حلّ المسائل » (p. 179–181, L25+L26)
- **تمرين 1** : 1. compléter les étiquettes d'un schéma S–I–R, normale N–N', angles notés **i1** (وسط1) et **i2** (وسط2) → الشعاع الوارد، العمود (NN')، السطح الفاصل، الشعاع المنكسر، زاوية الورود i1، زاوية الانكسار i2. 2. « حدّد من بين الوسطين 1 و2 أيّهما الهواء. » Mesure sur le schéma (200 dpi) : i1 ≈ 48°, i2 ≈ 62° ⇒ i2 > i1 (rayon qui s'écarte de la normale) ⇒ **وسط 2 = الهواء**. ⚠️ Notation i1/i2 différente de i/r du cours.
- **تمرين 2 (QCM)** : 1. air → milieu : la حزمة منكسرة se rapproche de « العمود المقام على السطح الفاصل بين الوسطين في نقطة الورود ». 2. milieu → air : se rapproche de « السطح الفاصل بين الهواء والوسط الشفّاف ». 3. air → « وسط شفّاف آخر أكثر انكساريّة » : options « زاوية الانكسار أكبر من قيمة زاوية الورود » / « أقلّ من قيمة زاوية الانعكاس » / « مساوية لقيمة زاوية الانعكاس » → **« أقلّ من قيمة زاوية الانعكاس »** (r < i et زاوية الانعكاس = i, loi de L23 — raisonnement croisé non explicité).
- **تمرين 3** (mots : تنعكس، تنكسر، الانكسار، أكبر، الورود، الهواء، وسط شفّاف، انكساريّة، زاوية الورود، أقلّ) :
  1. « عندما تعترض مرآة مسطّحة مسار حزمة ضوئيّة **تنعكس** هذه الأخيرة في حين أنّها تنعكس و**تنكسر** في الآن نفسه عندما تمرّ من **الهواء** إلى وسط شفّاف آخر. »
  2. « عندما تمرّ حزمة ضوئيّة من وسط شفّاف إلى **الهواء** تكون قيمة زاوية الانكسار **أكبر** من قيمة زاوية **الورود** ومن قيمة زاوية الانعكاس، وإذا ارتفعت قيمة زاوية الورود ارتفعت قيمة زاوية **الانكسار** وعند بلوغ قيمة **زاوية الورود** قيمة الزاوية الحرجة **تنعكس** الحزمة الضوئيّة كليّا. » (« انكساريّة », « أقلّ », « وسط شفّاف » restent en distracteurs.)
- **تمرين 4** (صحيح/خطأ) :
  1. « عندما تمرّ حزمة ضوئيّة من وسط شفّاف إلى وسط شفّاف آخر تنعطف وتنعكس في الآن نفسه مهما كانت قيمة زاوية الورود. » → خطأ (au-delà de l'angle critique, milieu→air : plus de réfraction).
  2. « عندما تمرّ حزمة ضوئيّة من الهواء إلى وسط شفّاف آخر تكون قيمة زاوية الانكسار دائما أصغر من قيمة زاوية الورود » → صحيح attendu. ⚠️ faux au sens strict pour i = 0 (r = 0 = i, cf. tableau p. 174).
  3. « ينتج الانكسار الحدّي للضوء عن انعكاسه الكلّي. » → خطأ (c'est l'inverse : الانعكاس الكلّي يترتّب عن الانكسار الحدّي).
  4. « يمكن أن يَحْصُل الانكسار الحدّي سواء مرّ الضوء من الهواء إلى وسط شفّاف آخر أو من هذا الأخير إلى الهواء. » → خطأ (seulement milieu → air).
  5. « عند مرور الضوء من الماء إلى الهواء يصبح الانعكاس كليّا عند بلوغ زاوية الورود قيمة أكبر من قيمتها التي تحصل بها نفس الظاهرة عند مرور الضوء من الزجاج إلى الهواء. » → صحيح (ماء 49° > زجاج 36–42°).
- **تمرين 5** (p. 180–181) : ح1 (oblique) et ح2 (normale) arrivent en I ; ح3 dans وسط2. 1. ح3 provient de **ح1** (ح2 à incidence normale n'est pas déviée ; ح3 est oblique). 2. Rayon manquant : réfracté de ح2, **prolongement vertical non dévié** dans وسط2. 3. Mesures (200 dpi) : ح1 ≈ 50° de la normale, ح3 ≈ 27° ⇒ r < i ⇒ **وسط1 = الهواء**.
- **تمرين 6** : « عند مرور حزمة ضوئيّة متوازية بسطح فاصل بين وسطين شفّافين أحدهما الهواء والآخر الماء... » ; ①, ② dans وسط2, ③ dans وسط1. 1. ③ ne peut **pas** être l'incidente : l'incidente et la réfléchie sont du même côté ; ① et ② seraient alors toutes deux dans l'autre milieu, impossible. 2. ① et ② symétriques / normale (≈ 28° et 30° mesurés) → l'une incidente, l'autre réfléchie ; ③ réfractée, à droite de la normale ⇒ **① incidente, ② réfléchie, ③ réfractée**. 3. ③ ≈ 49° > 28° ⇒ r > i ⇒ passage milieu → air ⇒ **وسط2 = الماء**. (Contrôle hors programme : sin49/sin28 ≈ 1.61 ≠ 1.33 — schéma purement qualitatif.)

### Incohérences / points à signaler
- ⚠️ Seuil de la réflexion totale formulé de trois façons : p. 177 « عندما **تتجاوز** قيمة i القيمة λ » ; p. 178 أستنتج « عندما **تبلغ** قيمة زاوية الورود قيمةً حرجة » ; خلاصة « إذا **تجاوزت** » ; تمرين 3 « عند **بلوغ** ». Ambiguïté i = λ vs i > λ.
- ⚠️ « r > i » (milieu → air) énoncé sans exception i = 0.
- Graphie variable : « البليكسيغلاس » (p. 176) / « البليكسيقلاس » ; « الإنكسار / الانكسار », « الإنعكاس / الانعكاس ».
- λ désigne dans L25 la « زاوية الانكسار القصوى » (air → milieu) et ici « القيمة/الزاوية الحرجة » d'incidence (milieu → air) — mêmes valeurs, jamais relié explicitement.

### Bornes
✅ Réfraction milieu → air (r > i, déviation vers la surface) ; croissance de la réflexion partielle avec i ; angle critique (الزاوية الحرجة λ : بليكسيقلاس 42°، ماء 49°) ; الانكسار الحدّي ⇒ الانعكاس الكلّي ; identification des milieux et des rayons (incident / réfléchi / réfracté) sur schéma.
⛔ Aucune formule de l'angle critique (sin λ = 1/n), aucun indice n, aucun calcul trigonométrique. Aucune mesure d'intensité (seulement « إشراق » qualitatif). Pas de cas « milieu 1 → milieu 2 » hors air (toujours air d'un côté).

### Vocabulaire officiel
الانكسار الحدّي (réfraction limite) ; الانعكاس الكلّي (réflexion totale) ; الزاوية الحرجة / القيمة الحرجة λ (angle critique / limite) ; السطح الفاصل ; الوجه المستوي / الوجه الاسطواني ; حزيمة منعكسة / منكسرة ; الإشراق (luminosité) ; الحياد عن العمود ; الانكساريّة. [FR : cf. lexique relevé dans L30.md.]

### Leçon 27 — « تطبيقات لتغيّر مسار الضّوء » (ص 182–189)

محور : **الضّوء** — باب : **تغيّر مسار الضّوء** (pictogramme livre = séance documentaire). Trois parties : النّافورة المضيئة (p. 182–183), الألياف البصريّة (p. 183–184), السّراب (p. 185–187) + أعوّل على نفسي (p. 188–189). **Pas d'encadré « الخلاصة »** dans cette leçon.

### Objectifs (خريطة الكتاب p. 7)
- تفسير مبدأ اشتغال النّافورة المضيئة و الألياف البصريّة.
- تفسير ظاهرة السّراب.

### Déroulé

**I. النّافورة المضيئة** (p. 182)
- أتأمّل وأتساءل : « بم أفسّر قدرة النافورة «المضيئة» على الإضاءة ؟ »
- **أفسّر قدرة النّافورة على الإضاءة** : « يتدفّق الماء شاقوليّا من الفوّارة في شكل عمود ليتفرّع بعد ذلك إلى باقة دائريّة جميلة من الخيوط المائيّة. وتزداد هذه الباقة جمالا في الليل بالضوء الصادر من المنوار المثبّت بجانب الفوّارة. » ; « ينتشر الضوء المنبعثُ من المنوار على استقامته في العمود المائي. عندما يسقط الشعاع الواحد منه على السطح الفاصل بين الهواء وخيط مائي في النقطة I1 بزاوية ورود i1 ذات قيمة أكبر من قيمة الزاوية الحرجة λ (λ >i1) [sic, cf. infra], لا ينعطف في الهواء بل ينعكس كلّيًا في الماء بزاوية انعكاس r1 متقايسة مع i1 حسب قانون الزوايا الخاص بالانعكاس ليرتدّ ثانية على السطح الفاصل بين الماء والهواء في النقطة I2 من الناحية المقابلة للنقطة I1 بزاوية i2 متقايسة مع i1 إذا اعتبرنا الخيط ذا شكل إسطواني، بالتالي يرتدّ الشعاع مرّة أخرى في الماء كما في الحالة الأولى ولنفس السبب.( الشكل1) » ; « وهكذا يتمكّن الضوء من اختراق الخيط المائي نتيجة انعكاسات كُلّية متتالية حتّى يصل إلى الطّرف الثاني للخيط على مستوى سطح البركة. »
- **أجرّب وأتأكّد** (p. 183) : modèle du filet d'eau par « ليفة بلاستيكية شفّافة رقيقة ( ذات قطر يناهز واحد ملّيمتر) » ; une extrémité contre « المنبّه المشعّ لأحد التجهيزات الكهربائيّة في حالة اشتغال (صمّام مشعّ...) » → « فيظهر في التوّ على الطرف الثاني وميضٌ برّاق (شكل2) لا يُفَسَّرُ إلاّ كما سبق. » (photo « تحفة » à fibres).

**II. الألياف البصريّة** (p. 183–184)
- أتأمّل وأتساءل : « كثر الحديث في السنوات الأخيرة عن اللألياف [sic] البصرية في ميادين الاتصالات والطبّ وغيرها. ما هي هذه الألياف البصريّة؟ ما هو دورها في تلك الميادين؟ وما هو مبدأ اشتغالها؟ »
- أبحث وأتأكّد : recherche documentaire + « بحث ميداني (بزيارة فرع جهوي لوكالة تونس للاتصالات مثلا) ».

**III. السّراب** (p. 185–187)
- أتأمّل وأتساءل : désert (« لمعانًا على الرمل يحسبه بِرَكًا من الماء... ») et route « بقَعٌ من الماء على الإسفلت «تهرب» منه كلّما تقدّم ».
- أبحث وأتأكّد : documentation (تعريفه، خاصيّاته، الظروف المناخيّة الملائمة لظهوره، تفسيره).
- **أجرّب وألاحظ** (p. 185–186) — simulation dans l'eau : « كأس اختبار كبير الحجم (سعة 500 mL مثلا) » ; « جهاز تسخين معتدل (موقد كحولي مثلا) » ; محراك ; laser ; ماء حنفيّة ; « مادّة ملوّنة للماء (مسحوق الفلوروسين، حليب...) ». Laser oblique vers la surface « في منحى غير شاقوليّ كما في الشكل 5 . شاقولي شاقولي كما في الشكل5. » [sic : ligne parasite dupliquée p. 186]. Après chauffage par le bas : « تغيّر مسار الضوء المنكسر في الماء يصير منحنيا مع اِنعطاف إلى الأعلى. (الشكل6) »
- **أفسّر ما حدث** : « عند التسخين، تقلّ كثافة الماء كلّما اقتربنا من مصدر الحرارة وبالتالي تقلّ انكسارية الماء من الأعلى إلى الأسفل. وعندما ينفذ الضوء في الماء من فوق فإنّه يمرّ من وسط شفّاف إلى وسط شفّاف آخر أقلّ انكساريّة فيخضع حسب قانونَيْ الانكسار إلى تغيّر في مساره نحو الأعلى. (الشكل7) » (légendes : « طبقة مائيّة باردة » en haut, « طبقة مائيّة ساخنة » en bas)

### Encadrés (VERBATIM)
- **أستنتج — الألياف البصريّة** (p. 184) :
  - « ➤ تستعمل الليفة البصريّة للنقل الموجّه والدقيق للإشارات الضوئيّة على مسافات قريبة أو بعيدة حسب الحاجة. »
  - « ➤ تتكون الليفة البصريّة من ثلاثة أجزاء اسطوانيّة متّحدة المحور: – جزء مركزي ذو قطر في سمك شعرة الرأس (0,001mm) يسمّى قلب الليفة، مصنوع من زجاج يختصّ بانكساريّة كبيرة. – جزء محيط بالقلب يسمّى الغلاف البصري، في شكل قشرة رقيقة جدّا (ذات سمك 0,05mm)، وهو مصنوع من زجاج نقيّ يختصّ بانكساريّة أصغر بقليل من انكساريّة زجاج القلب. – غلاف خارجي مصنوع من مادّة عاتمة ومتينة، يحيط بالغلاف البصري وذلك لحمايته ولتفادي أيّ تسرّب خارج الليفة. (الشكل3) » (légendes : قلب الليفة، الغلاف البصري، الغلاف الخارجي)
  - « ➤ ينفذ الضوء في الليفة البصريّة ويَرِد على السطح الفاصل بين القلب والغلاف البصري تحت زاوية ورود أكبر من الزاوية الحرجة، وبما أنّ زجاج القلب أكثر انكساريّة من الغلاف البصري فإنّ الضوء ينتشر في الليفة من طرف إلى آخر نتيجة انعكاسات كلّيّة متعاقبة (الشكل4) كما في التجربة الخاصّة بمحاكاة النافورة المضيئة. »
  - « ➤ بفضل مرونتها وقدرتها على نقل الضوء بدون امتصاص تقريبا تُستعمَل الألياف البصرية في عدّة مجالات هامّة نذكر منها: – ميدان الاتصال وذلك لبثّ المعلومات عبر مسافات طويلة (كوابل الهاتف، كوابل البثّ التلفزي...) أو مسافات قصيرة (كوابل ربط بين الحسوب الرئيسي والحواسيب الجانبية أو الطابعة في شبكة محليّة...) – ميدان الطب، وذلك لفحص أعضاء باطنيّة لجسم إنسان (القناة الهضميّة، الكبد، الأمعاء، المجاري البوليّة..) بواسطة المجواف. »
- **أستنتج — السّراب** (p. 187) :
  - « السراب هو ظاهرة طبيعيّة تتمثّل في مشاهدة بِرَكِ ماءٍ وهميّة على مسافة بعيدة في الأيّام شديدة الحرّ تضمحلّ أو تبعدكلّما ظنّ المشاهد أنّه اقترب منها وتبقى المسافة ثابتة بينه وبينها. تشاهد ظاهرة السراب عادة في الصحراء وعلى الطرق المعبّدة بالخرسانة الاسفلتيّة. »
  - « في الطقس الحارّ ترتفع درجة الحرارة كلّما اقتربنا من سطح الأرض فيكون الهواء في الجوّ على طبقات ذات كثافة متفاوتة تنقص من الأعلى إلى الأسفل فينتج عن ذلك انخفاض في الانكساريّة. بالتالي يمكن اعتبار أنّ كلّ طبقة هواء تتميّز بانكساريّة أهمّ من انكساريّة الطبقة التي تحتها وأقلّ من انكساريّة الطبقة التي تعلوها.(الشكل8) »
  - « لذلك عندما يرد ضوء الشمس من الطبقات العليا للهواء يخضع إلى انكسارات متتالية على مستوى السطح الفاصل بين طبقة وأخرى ينتج عنها ارتفاع تدريجيّ في قيمة زاوية الورود إلى أن يتعدّى قيمة الزاوية الحرجة فيترتّب عن ذلك انعكاس كلّيّ يرتدّ بسببه الضوء إلى أعلى في نقطة ورود معيّنة IM ليواصل الخضوع إلى انكسارات متتالية (الشكل9) حتّى يصل إلى عين المشاهد فيحسبه متأتّيا على استقامة من النقطة A وهكذا تتراءى له «بركة ماء» ولكنّها في الواقع هي صورة افتراضيّة لزرقة السماء(الشكل10). »
- Symboles/unités : i1, r1, i2, I1, I2, λ, IM, A ; 0,001mm ; 0,05mm ; 500 mL ; « ~1 ملّيمتر ».

### Exercices
- **أقيّم مكتسباتي** (p. 187) : « أبيّن لماذا: – تتسبّب الانكسارات المتتالية لضوء الشمس المتأتّي من الطبقات العليا للهواء في ارتفاع تدريجيّ لقيمة زاوية الورود. – لا يترتّب عن تعدّي قيمة زاوية الورود لقيمة الزاوية الحرجة الناتج عن تلك الانكسارات إلاّ انعكاس كلّي واحد. » Réponses attendues : (1) chaque passage vers une couche moins réfringente éloigne le rayon de la normale (r > i), et r d'une interface = i de la suivante (couches parallèles) ⇒ i croît ; (2) après la réflexion totale le rayon remonte vers des couches **plus** réfringentes ⇒ il se rapproche de la normale (r < i), plus de réflexion totale possible.
- **أعوّل على نفسي — أستغلّ وثيقة « مميّزات الألياف البصرية وبعض ميادين استعمالها »** (p. 188) : texte (ليفة « من الزجاج أو البلاستيك في سمك شعرة الرأس » ; capacité de nombreuses lignes/canaux par câble ; « عدم تعرّضها للتداخلات الكهرمغناطيسية » ; « بسرية تامة... لأغراض عسكرية » ; « عدم قابليتها للاشتعال » ; faible énergie ; réseaux, « التصوير الطبي »، « التنقيب في باطن الأرض »، caméras numériques, « التصوير الميكانيكي لفحص اللحام والوصلات في الأنابيب والمولدّات »، capteurs de température et pression, ailes d'avion). **أسئلة** (p. 189) : 1. « حدّد وظيفة ليفة بصريّة. » → نقل الضوء (الإشارات الضوئيّة) من مكان إلى آخر. 2. « أذكر أهمّ مميزات الألياف البصريّة. » → صغر الحجم وخفّة الوزن، قدرة حمل كبيرة، المحافظة على الإشارات وعدم تداخلها، عدم التعرّض للتداخلات الكهرمغناطيسية (سرّية)، عدم قابلية الاشتعال، طاقة ضعيفة، مرونة ودقّة. 3. « عدّد مجالات استعمالات الألياف البصريّة. » → الاتصالات وشبكات الحواسيب، التصوير الطبّي، التنقيب، الكاميرات الرقمية والمناظير، التصوير الميكانيكي، المجسّات (حرارة/ضغط)، الطائرات.
- **هل من مزيد ؟ « السراب المعكوس »** (p. 189) : bateau vu « مقلوبة ومعلّقة في الفضاء فوق الماء » quand les couches basses (proches de l'eau) sont froides et les couches hautes chaudes ; rayon qui s'éloigne de la normale en montant → « تصبح زاوية الورود في إحدى الطبقات أكبر من الزاوية الحرجة بالنسبة إلى الطبقة التي تعلوها فيحصل انعكاس كلّي للشعاع وينحني مساره إلى أسفل » ; exemples : « والشمس التي تتراءى مسطّحة في الأفق، الشخصُ الذي يختفي وهو أمام جدار أبيض وقشّةُ التبن المنحنية في كأس به ماء أمثلةٌ أخرى لظاهرة السراب المعكوس. » (schéma : « الهواء يبرد كلّما اقتربنا من سطح الماء » ; « السطح البارد » ; « المنطقة التي يظهر فيها السطح لامعا »)

### Incohérences / points à signaler
- ⚠️ p. 182 : la condition est écrite « (λ >i1) » dans l'image (lecture LTR : λ > i1), ce qui contredit le texte « i1 ذات قيمة أكبر من قيمة الزاوية الحرجة λ ». Probable inversion de signe due à la mise en page RTL ; la bonne relation est **i1 > λ**.
- ⚠️ p. 184 : « قطر في سمك شعرة الرأس (0,001mm) » : 0,001 mm = 1 µm, alors qu'un cheveu fait ~0,05–0,1 mm ; et la gaine (0,05 mm) serait 50 fois plus épaisse que le cœur. Chiffres incohérents entre eux et avec la comparaison « شعرة الرأس » (pour une fibre monomode réelle le cœur fait ~0,008–0,01 mm). À ne pas reprendre tel quel.
- ⚠️ La réflexion totale est appliquée à une interface **verre → verre** (cœur/gaine) et **air → air** (couches) alors que L26 ne l'a établie que pour « وسط شفّاف → الهواء ». Extension non justifiée dans le cours (mais énoncée ici : « بما أنّ زجاج القلب أكثر انكساريّة من الغلاف البصري »).
- Coquilles : « اللألياف » (p. 183) ; ligne dupliquée « شاقولي شاقولي كما في الشكل5. » (p. 186) ; « الحسوب الرئيسي » (p. 184) ; « تبعدكلّما » (p. 187).
- « سراب المعكوس » (p. 189) : exemple « قشّة التبن المنحنية في كأس به ماء » relève de la réfraction simple (L25), pas du mirage inversé — classement discutable.

### Bornes
✅ Explication qualitative : fontaine lumineuse, fibre optique (3 couches, réflexions totales successives, usages), mirage (couches d'air de انكساريّة décroissante vers le sol, réfractions successives + une réflexion totale, image virtuelle du ciel), mirage inversé (enrichissement).
⛔ Aucun calcul (pas d'angle, pas d'indice, pas d'atténuation, pas de débit) ; pas d'ouverture numérique ; l'angle critique cœur/gaine n'est pas chiffré ; aucune loi nouvelle (réutilisation de L23–L26).

### Vocabulaire officiel
النّافورة المضيئة (fontaine lumineuse) ; الفوّارة ; الخيط المائي ; المنوار ; الانعكاسات الكلّية المتتالية ; الليفة البصريّة / الألياف البصريّة (fibre optique) ; قلب الليفة (cœur) ; الغلاف البصري (gaine optique) ; الغلاف الخارجي ; الإشارات الضوئيّة ; المجواف (endoscope) ; التداخلات الكهرمغناطيسية ; السّراب (mirage) ; السراب المعكوس (mirage inversé / supérieur) ; طبقات الهواء ; الكثافة ; صورة افتراضيّة ; الخرسانة الاسفلتيّة ; مسحوق الفلوروسين. [FR : cf. lexique relevé dans L30.md.]

### Leçon 28 — « الأضواء المرئيّة والضّوء الأبيض » (ص 190–200)

محور : **الضّوء** — باب : **تغيّر مسار الضّوء** (خريطة p. 7 : deux pictogrammes, séance expérimentale + documentaire). Contient la **خلاصة de L27 + L28** (p. 195), la série « أعوّل على نفسي » (p. 196–198), « أتسلّى » (p. 199–200) et « أستعين بعناوين » (p. 200) qui clôt le باب.

### Objectifs (خريطة الكتاب p. 7)
- إنجاز تجربة تشتّت الضوء الأبيض.
- التعرّف إلى الضوء الأبيض.
- تفسير ظاهرة قوس قزح.

### Déroulé
- **أتأمّل وأتساءل** (p. 190) : « من بين المصابيح المنزليّة ومصابيح التنوير العمومي ما هي تلك التي تشعّ ضوءا أبيض؟ لماذا يسمّى ضوءا أبيض؟ » ; « بم أفسّر ظهور بقعة متعدّدة الألوان (من الأحمر إلى البنفسجي) على السطح الحسّاس للقرص المضغوط عندما يُوجَّهُ إلى الشمس بشيء من الإمالة ؟ » ; « بم أفسّر احتواء قوس قزح لكلّ تلك الألوان الزاهية؟ لماذا لا يظهر إلاّ بعد نزول المطر وبعيدا عن منتصف النهار؟ هل يظهر من نفس الجهة في الصباح وفي المساء؟ أيّ جهة؟ لماذا؟ »
- **I. انتشار الضّوء عبر موشور — أجرّب وألاحظ** (p. 190–191) : « موشور زجاجي » ; « مصدر لأشعّة ليزر (أشعّة حمراء) » ; « الجهاز الخاصّ بدراسة الانكسار ». Description : « قطعة من الزجاج الشفّاف ذات ثلاثة وجوه صقيلة ومستطيلة الشكل ووجهين غير صقيلين (على شكل مثلّث متساوي الساقين) ومتوازيين مع المقطع القائم للموشور (أي متعامديْن مع حروف الموشور). (الشكل1) » ; « هام جدّا: في التعامل مع الموشور لا يجب أن نلمسَ الوجوه الصقيلة حتّى لا نفقده خاصياته البصريّة... نضعه على واحد منهما ونوجّهه بحيث يرد الضوء على واحد من الوجهين الصقيلين المتناظرين على قرب من حرف التقاطع 'AA. يسمّى المثلّث الذي يوضع عليه الموشور قاعدة الموشور(الشكل 2). » ; « ملاحظة : يمكن إنجاز نفس التجربة باستعمال موشور مائيّ عوضا عن موشور زجاجي. »
- **أفسّر ما حدث** (p. 192) : en I1 « سطح يفصل بين وسطين شفّافين، الهواء والزجاج، فينفذ في الموشور خاضعا للانكسار، وبما أنّه ورد في مستوي المقطع القائم للموشور يبقى حسب القانون الأوّل للانكسار في نفس المستوي، لذلك يُرسَم الموشور دائما في شكل مثلّث يمثّل مستوي المقطع القائم (أومستوٍ متوازٍ مع الوجهين المثلّثيْن للموشور) كما في الشكل 5 . » ; en I2 « يخضع إلى الانكسار مرّة ثانية لينتشر من جديد في الهواء في المنحى I2R منحرفا أكثر عن المنحى الأصلي SI1 (الشكل5) » (angles notés i1, r1, i2, r2 sur le schéma).
- **II. تشتّت الضّوء الأبيض — أجرّب وألاحظ** (p. 192–193) : lampe du dispositif (« مصباح متوهّج ») ; sans prisme : trace « أبيض(به مسحة من الاصفرار) » ; avec prisme : « بقعة ملوّنة يزيد عرضها كلّما ابتعدنا عن الموشور وتتوزّع الألوان فيها تدريجيّا من الأحمر (الأثر الأقلّ انحرافا) إلى البنفسجي (الأثر الأكثر انحرافا) مرورا بالبرتقالي فالأصفر، الأخضر، الأزرق، النّيلي. (الشكل7) » ; écran (« حاجزا ») : « بقعة ضوئيّة مستطيلة الشكل ... محتوية لنفس الألوان وفي نفس الترتيب. (الشكل8) »
- **أفسّر ما حدث** (p. 193) : « كلّ لون من ألوان البقعة الضوئيّة المتكوّنة على الحاجز برهانٌ على انبثاق ضوء بذلك اللون من الموشور. بالتالي نفذت عبر الموشور أضواءٌ متعدّدة الألوان صادرة من الفانوس S، وكما كان الشأن بالنسبة إلى أشعّة الليزر الحمراء في التجربة السابقة، خضع كل ضوء من تلك الأضواء إلى انعطاف بقيمة مرتبطة بلونه، ممّا تسبّب في تشتّت الضوء الأبيض عبر الموشور. »
- **III. ظاهرة قوس قزح — أستغلّ وثيقة** (p. 194–195) : définition (« قوس من أضواء متعدّدة الألوان يُشاهَد في السماء قبالةَ الشمس بعد انتهاء المطر أو في الرذاذ الذي يصدر من شلالات المياه... اللون الأحمر هو اللون الخارجي في حين أنّ اللون البنفسجي يكون اللونَ الداخلي، الأقربَ إلى سطح الأرض. ») ; matin → vu à l'ouest (nuages → pluie), après-midi → vu à l'est (amélioration) ; proverbe « إذا قوس قزح ظهر في الصباح هبّط حملك وارتاح ويذا ظهر في العشيّة هز حملك وشد الثنيّة » ; histoire : ابن الهيثم (القرن الحادي عشر ميلادي / الخامس هجري, كتاب المناظر, citation) ; « وفي القرن الثالث عشر الميلادي (السابع الهجري) استطاع الشيرازي تعليل قوس قزح تعليلا دقيقا فقال: «ينشأ قوس قزح من وقوع أشعّة الشمس على قطرات الماء الصغيرة الموجودة في الجو عند سقوط الأمطار، وحينئذ تعاني الأشعّة انعكاسا داخليا، وبعد ذلك تخرج إلى الرائي». » ; « عندما يخترق ضوء الشمس قطرة مطر تنكسر فعلا كلّ إشعاعة أحاديّة اللون بزاوية خاصّة مختلفة عن زوايا انكسار الإشعاعات الأخرى الأحاديّة اللون، وعند ورود هذه الإشعاعات على السطح الداخلي للقطرة تنعكس وتنكسر مرّة أخرى عند خروجها من القطرة إلى الهواء (الشكل9) » (schéma : « إشعاعة بنفسجيّة » 40°, « إشعاعة حمراء » 42°) ; « ...يمكنه رؤية الألوان من قطرات معيّنة عندما تكون زاوية الانعكاس بين الشمس وقطرة الماء وخط رؤية من يشاهد هذه الألوان تتراوح قيمتها بين40° و42°... » ; « كلّما كبر حجم القطرة كان تشتّت الضوء أفضل وقوس قزح أوضح... مع العلم أنّه لا ينتج أبدا عن تساقط الثلوج. »
  - أسئلة (p. 195) : 1. « بيّن من خلال النص ما يدلّ على أنّ ضوء الشمس ضوءٌ أبيضُ. » → « وهو يحتوي على نفس ألوان طيف الضوء الأبيض وبنفس الترتيب ». 2. « ممّا ينتج قوس قزح؟ ما هو العنصر الذي يلعب في ظهوره دور الموشور؟ » → تشتّت ضوء الشمس (انكسار + انعكاس داخلي + انكسار) ; قطرات الماء (المطر). 3. « لماذا لا يظهر قوس قزح في يوم صحوٍ؟ » → pas de gouttes d'eau dans l'air. 4. « لماذا لا يمكن مشاهدة قوس قزح في منتصف النهار؟ » → soleil haut : l'arc (40°–42° sous la direction anti-solaire) se trouve sous l'horizon (« ...ويظهر منخفضا عندما تكون الشمس مرتفعة »).

### Encadrés (VERBATIM)
- **أستنتج** (p. 192) : « يخضع الضوء عبر موشور إلى انحراف في مساره نتيجة لانكسارين متتاليين الأوّل على وجه الدخول هواء–زجاج والثاني على وجه الخروج زجاج–هواء. »
- **أستنتج** (p. 193) :
  - « ➤ يحتوي الضوء الأبيض على مجموعة لا متناهية من الإشعاعات أحاديّة اللون تمتدّ من الأحمر إلى البنفسجي لذلك نقول إنّ الضوء الأبيض إشعاعة متعدّدة الألوان. »
  - « ➤ تشتّتُ الضوء الأبيض عبر موشور ظاهرةٌ ناتجةٌ عن خضوع كلّ إشعاعة أحاديّة اللون منها إلى انحراف في مسارها ولكن بقيمة مرتبطة بلونها ترتفع من الأحمر إلى البنفسجي مرورا بالبرتقالي فالأصفر، الأخضر، الأزرق، النّيلي. »
  - « ➤ تسمّى البقعة الضوئيّة متعدّدةُ الألوان، الناتجة عن تشتّت الضوء الأبيض طيفَ الضوء الأبيض. »
  - « ➤ طيف الضوء الأبيض طيفٌ متواصلٌ يحتوي على كلّ ألوان قوس قزح. »
  - « ➤ المصباح المتوهّج مثالٌ لمصدر ضوء أبيض. »
- **أستنتج** (p. 195) :
  - « ➤ ضوء الشمس مثال آخر للضوء الأبيض. »
  - « ➤ قوس قزح ظاهرة طبيعيّة تمثّل طيف ضوء الشمس، ناتجة عن انكسارات وانعكاسات عبر قطرات المطر في الجوّ. »
  - « ➤ لا يُشاهَد قوس قزح إلاّ تحت زاوية تتراوح قيمتها بين40° و42° فيظهر عاليا نسبيّا عندما تكون الشمس منخفضة في السماء ويظهر منخفضا عندما تكون الشمس مرتفعة. »
- **الخلاصة** (p. 195, L27 + L28) :
  - « لانكسار الضوء بصفة عامّة وللانكسار الحدّي وللانعكاس الكلّي بصفة خاصّة تطبيقات كثيرة، من أهمّها الألياف البصريّة »
  - « السراب ظاهرة طبيعيّة ناتجة عن انكسارات متتالية وانعكاس كلّي في الجوّ الحارّ. »
  - « يحتوي الضوء الأبيض على عدد لا متناه من الأضواء المرئيّة تمتدّ من الأحمر إلى البنفسجي. »
  - « طيف الضوء الأبيض طيف متواصل توافق ألوانه ألوانَ قوس قزح. »
  - « تشتّت الضوء الأبيض ناتج عن ارتباط انكساريّة الوسط الشفّاف بلون الإشعاعة التي تنفذ فيه »
  - « قوس قزح ظاهرة طبيعيّة ناتجة عن تشتّت ضوء الشمس عبر قطرات الماء في الجوّ. »
- Ordre officiel des couleurs : أحمر، برتقالي، أصفر، أخضر، أزرق، نيلي، بنفسجي (7 couleurs, rouge = moins dévié). Angles 40° (violet) – 42° (rouge).

### Exercices
- **أقيّم مكتسباتي** (p. 193) : même expérience avec « مصباح نيون (tube néon) » → spectre de la figure 8 (quelques raies séparées rouges/orange + une jaune). 1. Comparer au spectre continu (fig. 7) → **non**, pas un ضوء أبيض (spectre discontinu, raies). 2. Lumières constituantes : quelques radiations rouges/orangées et une jaune (lecture de la figure ; aucune longueur d'onde).
- **أتمرّن على حلّ المسائل** (p. 196–197) :
  - **تمرين 1** : 1. « يُستعملُ الموشور لـ: التعرّف إلى طيف الضوء / تشتيت الضوء الأبيض فقط / تحليل الأضواء / مزج الأضواء أحاديّة اللون » → « تحليل الأضواء » (et « التعرّف إلى طيف الضوء » aussi défendable ⚠️ double bonne réponse possible ; « فقط » disqualifie la 2e). 2. « الضوء الأبيض: لا ينبعث إلاّ من الشمس / متكوّن من مزيج لعدد لا متناهٍ من إشعاعات أحاديّة اللون / يُنعَت بالأبيض لأنّه متكوّن من أشعّة أحادية اللون الأبيض » → la 2e. 3. « ظاهرة قوس قزح ناتجة عن: تشتّت ضوء الشمس عبر قطرات ماء المطر / انكسارات متعدّدة عبر قطرات الماء في الجوّ / انكسارات وانعكاسات عبر قطرات الماء في الجوّ » → ⚠️ la 1re reprend mot pour mot la خلاصة (« ناتجة عن تشتّت ضوء الشمس عبر قطرات الماء ») et la 3e reprend le أستنتج p. 195 (« ناتجة عن انكسارات وانعكاسات عبر قطرات المطر ») : **deux options conformes au manuel**.
  - **تمرين 2** (mots : لا متناهية، تشتّتُ، عاليا، أحادي اللون، طيف متواصل، الليزر، منخفضا، الشمس) : 1. « تغيّرُ مسار ضوءٍ **أحادي اللون** عبر موشور مرتبط بلون الضوء. » 2. « أشعة **الليزر** إشعاعةٌ أحاديّة اللون، أمّا ضوء **الشمس** فهو إشعاعة متعدّدة الألوان. » 3. « كلّ إشعاعة متعدّدة الألوان تحتوي على مجموعة **لا متناهية** من الإشعاعات أحاديّة اللون. » 4. « طيف الضوء الأبيض **طيف متواصل** يحتوي على ألوان قوس قزح. » 5. « يظهر قوس قزح **عاليا** نسبيًا عندما تكون الشمس منخفضة في السماء ويظهر **منخفضا** عندما تكون الشمس مرتفعة. » (« تشتّتُ » en distracteur.)
  - **تمرين 3** (صحيح/خطأ) : 1. « يظهر قوس قزح دائما من ناحية الغرب. » → خطأ (le matin à l'ouest, l'après-midi à l'est). 2. « ظهور قوس قزح شرقا ينبئ بالطقس الجميل. » → صحيح (selon le texte p. 194). 3. « ضوء مصباح متأجّج مثال للضوء الأبيض. » → صحيح [« متأجّج » ici vs « متوهّج » dans le cours]. 4. « لا تخضع أشعّة الليزر عبر موشور للانحراف. » → خطأ (déviée, mais non dispersée). 5. « الموشور قادر على تغيير مسار الضوء بنسبة تزداد من الأحمر إلى البنفسجي. » → صحيح. 6. « يخضع الضوء الأبيض عبر موشور إلى انحراف في مساره نتيجة انكسارين اثنين. » → صحيح.
  - **تمرين 4** : trois حزيمات monochromatiques (برتقاليّة / حمراء / زرقاء), air → eau, même i. Mesures (200 dpi) : r3 ≈ 25.5°, r1 ≈ 34.6°, r2 ≈ 46.8° ⇒ **r3 < r1 < r2**. Rouge = moins dévié = r le plus grand ⇒ (2) **أحمر**, (1) **برتقالي**, (3) **أزرق**. (Schéma qualitatif : r2 ≈ 47° pour i ≈ 58° donnerait n ≈ 1,16, irréaliste pour l'eau.)
  - **تمرين 5** : prisme, rayon rouge (haut) et bleu (bas) ; zones ① au-dessus du rouge, ③ entre rouge et bleu, ② sous le bleu. Violet (plus dévié que le bleu) → **②** ; vert (entre rouge et bleu) → **③**.
- **أستغلّ وثيقة — détecteur de fumée** (p. 198) : « جهاز كشف الدخّان » = « مِجَسّ حسّاس للضوء وهو الصمّام الضوئي » + « جهاز الكتروني يُصدر صوتا منبّها مرتفعا » ; « خليّة كهرضوئيّة » ; « صمّام مشعّ (LED) » ; tube en T à « زاوية 90° » ; en présence de fumée les « حبّات الدخان » dévient la lumière vers la cellule → alarme. Source : « عن تفسير للدكتور حازم فلاح سكيك (بتصرّف) ». **سؤال** : « إذا سلّمنا بأنّ حبّات الدخان كرويّة الشكل وشفّافة مثل قطرات المطر، اقترحْ تفسيرا لانعطاف الضوء نحو الصمّام الضوئي... » → réfractions (+ réflexion interne) dans chaque grain comme dans une goutte d'eau (L28 §III).
- **أتسلّى** (p. 199–200) : 1. كلمات متقاطعة — définitions : 1 « إحدى تطبيقات الانعكاس الكلّي » ; 2 « تكون عليها المسافة بين السراب والمشاهد » (→ ثابتة) ; 3 « واحدة من ظواهر تغيّر مسار الضوء » ; 4 « جسم يمكّن من تشتّت الضوء الأبيض » (→ موشور) ; 5 « ظاهرة ارتداد الضوء في منحى وحيد » (→ انعكاس) ; 6 « جسم مسطّح يعكس الضوء » (→ مرآة) ; 7 « جمع ليفة » (→ ألياف) ; 8 « شيء نحصل عليه بتشتّت الضوء الأبيض » (→ طيف) ; 9 « جسم شفّاف يحيط بنا » (→ هواء) ; 10 « أشعّة حمراء اللون » (→ ليزر). Réponses proposées, non vérifiées case par case sur la grille. 2. « من هو صاحب الصورة ؟ » : « عالم عربي اهتمّ بدراسة قائمة على التمشّي العلمي لخصائص الضوء في الانتشار المستقيمي والانعكاس والانكسار » — 9 cases I→IX → **ابن الهيثم** (9 lettres ا-ب-ن-ا-ل-ه-ي-ث-م ✔). 3. croyances : proverbe tunisien, « أسطورة قديمة » (accord entre Dieu et Noé), « أسطورة إفريقيّة » (serpent), « جسر نحو الجنّة », « الألمان... في العصور الوسطى ».
- **أستعين بعناوين** (p. 200) : liens web pour « انعكاس وانكسار الضوء », « السراب والألياف البصريّة », « تشتّت الضوء الأبيض وقوس قزح ».

### Incohérences / points à signaler
- ⚠️ QCM Ex 1.1 et 1.3 : deux options conformes au texte du manuel.
- ⚠️ p. 195 : « زاوية **الانعكاس** بين الشمس وقطرة الماء وخط رؤية... بين 40° و42° » — il s'agit de l'angle entre la direction solaire et la ligne de visée (angle de déviation complémentaire), pas d'un « angle de réflexion » au sens de L23.
- ⚠️ Numérotation des figures p. 192–193 : le texte renvoie « (الشكل7) » pour la tache colorée sur le disque puis « (الشكل8) » pour la bande sur l'écran ; or la bande imprimée p. 193 est légendée « الشكل 7 » et « الشكل 8 » est le spectre du néon.
- « مصباح متأجّج » (Ex 3) vs « مصباح متوهّج » (cours).
- Le cours dit « الضوء الأبيض إشعاعة متعدّدة الألوان » (singulier « إشعاعة » pour un mélange).
- Pas de lien quantitatif couleur ↔ longueur d'onde ; nombre de couleurs « لا متناهية » mais 7 noms.

### Bornes
✅ Déviation par un prisme (2 réfractions) ; dispersion ; lumière blanche = infinité de radiations monochromatiques (rouge → violet, 7 couleurs nommées dans l'ordre) ; spectre continu ; lampe à incandescence et Soleil = lumière blanche ; spectre du néon non blanc (discontinu, sans le mot « raie ») ; arc-en-ciel (gouttes = prismes, 40°–42°, position/heure).
⛔ Aucune longueur d'onde (nm), aucune fréquence, pas de mot « طول الموجة » ; aucun calcul de déviation du prisme (angle au sommet non utilisé) ; pas de synthèse additive des couleurs (« مزج الأضواء » apparaît seulement comme distracteur) ; pas de couleur des objets / filtres (le lexique cite « Filtre de lumière مرشّح ضوء » mais la leçon non) ; pas d'infrarouge/UV.

### Vocabulaire officiel
الأضواء المرئيّة ; الضوء الأبيض ; موشور (prisme) ; موشور مائيّ ; المقطع القائم / مقطع أصلي (section principale) ; قاعدة الموشور ; حرف الموشور ; انحراف (déviation) ; تشتّت الضوء (dispersion de la lumière) ; إشعاعة أحاديّة اللون / متعدّدة الألوان (radiation) ; طيف الضوء الأبيض (spectre de la lumière blanche) ; طيف متواصل ; المصباح المتوهّج ; مصباح نيون ; قوس قزح (arc-en-ciel) ; الأحمر، البرتقالي، الأصفر، الأخضر، الأزرق، النّيلي، البنفسجي ; حاجز (écran) ; القرص المضغوط ; جهاز كشف الدخّان ; الصمّام الضوئي / الخليّة الكهرضوئيّة (photoélectrique) ; صمّام مشعّ (LED) ; الشيرازي ; ابن الهيثم ; طيفيّة (spectroscopie). [FR : cf. lexique relevé dans L30.md.]

### Leçon 29 — « مفهوم الطّاقة الضّوئيّة » (ص 200 selon خريطة الكتاب) — **ABSENTE DU PDF**

محور : **الضّوء** — باب : **الطّاقة الضّوئيّة** (خريطة p. 7 ; pictogramme lunette = séance expérimentale).

### Objectifs (خريطة الكتاب p. 7 — seul contenu officiel disponible)
- التعرّف إلى الطّاقة الضوئيّة وتحوّلاتها. (objectif commun aux leçons 29 et 30, cellule fusionnée dans la خريطة)

### Constat (vérifié page par page, 100 dpi + pdftotext)
- p. 200 du PDF = fin de L28 (« أتسلّى » §3 croyances + « أستعين بعناوين ») — pas de titre « 29 ».
- p. 201 = page de titre du lexique « قائمة في مصطلحات علمية مترجمة / مدخل فرنسي / مدخل عربي ».
- p. 202, 203, 204, 205 = **pages entièrement blanches** (PNG 4180 octets identiques ; pdftotext = 0 caractère ; aucune image).
- Aucune page d'ouverture de باب « الطّاقة الضّوئيّة » dans tout le PDF (la page d'ouverture p. 154 ne liste que les leçons 23–28).
- ⇒ Le PDF 103902P00 (223 p., QuarkXPress 2010) **ne contient pas les leçons 29 et 30**. Numérotation : la خريطة annonce L29 p. 200 et L30 p. 204, pages occupées ici par la fin de L28 et par des blancs/lexique.

### Déroulé / Encadrés / Exercices
- Néant (non imprimés dans cette édition PDF). **Aucun contenu ne doit être inventé** pour cette leçon à partir de ce manuel.

### Indices indirects (lexique uniquement, sans valeur de cours)
- Le lexique contient « Photosynthèse — تركيب ضوئي », « Photoélectrique — كهرضوئي » (aussi utilisé en L28, خليّة كهرضوئيّة), « Méthanier — ميتانيّة », « Centrale hydraulique — محطة هيدروليكيّة » ; **aucune** entrée « Énergie (lumineuse / solaire) », « Panneau solaire », « Photopile / cellule photovoltaïque », « Capteur solaire ».

### Bornes
⛔ Tout : aucune définition, aucune formule, aucune unité de la « طاقة ضوئيّة » n'est lisible dans ce PDF. Source alternative requise (autre édition du manuel ou guide du professeur).

### Vocabulaire officiel
الطّاقة الضّوئيّة (seul terme attesté, par la خريطة p. 7) ; تحوّلات (الطاقة).

### Leçon 30 — « الطّاقة الشّمسيّة » (ص 204 selon خريطة الكتاب) — **ABSENTE DU PDF** + relevé du lexique (p. 201–223)

محور : **الضّوء** — باب : **الطّاقة الضّوئيّة** (خريطة p. 7 ; pictogramme livre = séance documentaire).

### Objectifs (خريطة الكتاب p. 7)
- التعرّف إلى الطّاقة الضوئيّة وتحوّلاتها. (objectif commun L29–L30)

### Constat
- p. 204 du PDF = page **blanche** (comme 202, 203, 205). Aucune trace de L30 (ni titre, ni activité, ni خلاصة, ni exercice) sur p. 200–223. Voir L29.md pour la vérification.
- Déroulé / Encadrés / Exercices / Bornes : **néant — rien à transcrire, rien à inventer.**

---

### Relevé du lexique « قائمة في مصطلحات علمية مترجمة » (p. 201–223)

### Plage et structure (constatées)
| Pages PDF | Contenu |
|---|---|
| 201 | Page de titre : « قائمة في مصطلحات علمية مترجمة / مدخل فرنسي / مدخل عربي » |
| 202–205 | **Blanches** |
| 206–208 | Entrée française, sections **I → V** (I, J, L, M, N, O / P, Q, R / S, T, U, V) — **doublon exact** de p. 214–216 (seul l'ordre Q diffère : Q après P en p. 207, Q en fin de p. 216 écrit « Qaurtz ») |
| 209–210 | Entrée arabe, sections **أ، ب / ت، ج، ح** — **doublon exact** de p. 217–218 |
| 211–213 | Entrée française (titre « قائمة في مصطلحات علمية مترجمة / مدخل فرنسي »), sections **A, B / C, D / D (fin), E, « G » , « E »** |
| 214–216 | Entrée française, sections I → V + Q |
| 217–223 | Entrée arabe (titre « مدخل عربي »), sections أ، ب / ت، ج، ح / د، ذ، ر، ز، س، ش / (ش suite)، ص، ط، ع، غ، ف / ق، ك، ل، م / (م suite) / (م fin)، ن، هـ، و |

Tableau à 2 colonnes (FR à gauche, AR à droite), une bande colorée par lettre. Pas de section **H** ni **K** en FR ; en AR pas de section **خ، ض، ظ، ي** ; pas de section **ث**.

### Défauts du lexique (à ne pas recopier)
- Pages dupliquées (206–208 = 214–216 ; 209–210 = 217–218) et ordre des pages non alphabétique (I–V avant A–G).
- p. 213 : bandeau « **G** » au-dessus d'entrées en **F** (Fibre optique… Frotter) ; bandeau « **E** » au-dessus d'entrées en **G** (Galet de dynamo, Génératrice…, Gicleur).
- Entrée arabe, section أ (p. 209 = 217) — **appariements faux** : « Déviation — انعكاس كلّي » (doit être Réflexion totale) ; « Réflexion de la lumière — انكسار الضوء » (doit être Réfraction) ; « Diffusion de la lumière — انتشار الضوء » (انتشار = propagation ; la diffusion est « الانتثار » en L23). Même « Diffusion de la lumière — انتشار الضّوء » en entrée FR p. 212.
- Entrée arabe, section ص (p. 220) — décalage : « Radiation — صعق », « Rainure — صودا كاوية », « Période — صورة حقيقيّة », « Photoélectrique — صيغة كيميائيّة » ; section ط : « Radiation — طيف الضوء », « Rainure — طيفيّة ». (Les bons couples existent ailleurs : Electrocution—صعق, Soude caustique—صودا كاوية, Image réelle—صورة حقيقيّة, Formule chimique—صيغة كيميائيّة.)
- Section ش (p. 219) : « Ionique — شاردة مصعديّة (أنيون) » (doit être Anion) puis « Ionique — شارديّ ».
- Coquilles FR : « Carbonate de soduim », « Qaurtz », « gicleur » (minuscule), « Sacle / Socle ».
- « Calibrage — معايرة (أو مرقّم) » en AR p. 222 vs « Cadran — مينا (أو مرقم) » en FR.

### Termes d'optique présents (correspondances officielles FR ↔ AR)
Angle critique — زاوية حرجة ; Angle de réflexion — زاوية الانعكاس ; Angle de réfraction — زاوية الانكسار ; Angle d'incidence — زاوية الورود ; Arc-en-ciel — قوس قزح ; Convergent (faisceau) — متجمّعة (حزمة) ; Divergent (faisceau) — متباعدة (حزمة) ; Coaxial — متّحد المحور ; Condenseur — مكثّف ; Déviation — انحراف ; Diffusion de la lumière — انتشار الضّوء [sic] ; Dispersion de la lumière — تشتّت الضّوء ; Direction — منحى ; Ecran — حاجز (أو حائل)، شاشة ; Endoscope — مجْواف (كاشف الأجواف) ; Fibre optique — ليفة بصريّة ; Filtre de lumière — مرشّح ضوء ; Focalisation — تركيز / Focalisation de la lumière — تركيز الضوء ; Image optique — صورة بصريّة ; Image réelle — صورة حقيقيّة ; Image virtuelle — صورة افتراضيّة ; Jet d'eau — انبجاس ماء ; Lanterne — فانوس ; Luminosité — إشراقة (أو نورانية) ; Mirage — سراب ; Miroir plan — مرآة مسطّحة ; Normale — عمود ; Objet virtuel — جسم افتراضي ; Photoélectrique — كهرضوئي ; Photosynthèse — تركيب ضوئي ; Pinceau lumineux — حُزيمة ضوئيّة ; Plan d'incidence — مستوي الورود ; Plexiglas — بليكسيقلاص (graphie du lexique ; le cours écrit « بليكسيقلاس ») ; Pointillé — مُنقّط ; Prisme — موشور ; Radiation — إشعاعة ; Rayonnement — إشعاع ; Rainure — أخدود ; Rayon — شُعاع ; Rayon incident — شُعاع وارد ; Rayon réfléchi — شُعاع منعكس ; Rayon réfracté — شُعاع منكسر ; Réflecteur — عاكس ; Réflexion de la lumière — انعكاس الضّوء ; Réflexion totale — انعكاس كلّي ; Réfraction de la lumière — انكسار الضّوء ; Réfraction limite — انكسار حدّي ; Réfringence — انكساريّة ; Réfringent — كاسر ; Rétroprojecteur — منوار عاكس ; Rétroviseur — مرآة عاكسة ; Sacle [sic] — مِنْصب ; Section principale — مقطع أصلي ; Simulation — محاكاة ; Spectre de la lumière blanche — طيف الضّوء الأبيض ; Spectroscopie — طيْفيّة (دراسة الأطياف الضّوئيّة) ; Spot lumineux — بقعة ضوئيّة ; Symétrique — متناظر ; Valeur critique — قيمة حرجة ; Valeur maximale — قيمة قصوى ; Verre dépoli — زجاج (أو بلّور) أغْبش ; Verre poli — زجاج صقيل (أو ألمس) ; Virtuel — افتراضي.

Termes du cours **absents** du lexique : الانتثار (diffusion au sens L23), قلب الليفة / الغلاف البصري (cœur/gaine), نافورة مضيئة, مُشاكل (kaléidoscope), إشعاعة أحاديّة اللون (monochromatique), طيف متواصل, موشور مائيّ.

### Lentilles « العدسات » et « قانون أوم »
- **Dans les pages lues (150–223 + خريطة 4 et 7)** : **aucune** mention de « العدسات » / « عدسة » ni de « قانون أوم ». Le lexique n'a **aucune** entrée « Lentille » (section L = Laiton, Lanterne, Luminosité ; AR ع = عاكس… sans عدسة) ni « Ohm / Loi d'Ohm » (section O = Objet virtuel, Orbite, Oscillogramme, Oscilloscope ; aucune entrée « أوم »). Seuls termes voisins : « Convergent/Divergent (faisceau) » (حزمة متجمّعة/متباعدة, prérequis p. 153), « Focalisation — تركيز », « Condenseur — مكثّف » (utilisé dans « فانوس مع مكثّف »), « Coulomb — كولون » (seule unité électrique nommée dans le lexique).
- La خريطة p. 4 (L1–L7) et p. 7 (L23–L30) ne mentionnent ni lentilles ni loi d'Ohm (p. 5–6 = autres parties, non lues ici).

## 3. Notes pédagogiques / méthode

- **Physique qualitative et expérimentale** : les lois de l'optique sont QUALITATIVES (r = i ; r < i de
  l'air vers le milieu ; angle limite λ mesuré) — **aucun sinus, aucun indice n, aucune loi de Snell** ; la
  chimie ne nomme **ni protons ni neutrons**, ne définit **pas le pH chimiquement** (ni H⁺ ni log) et
  n'écrit **aucune formule d'ion** ; l'électricité ne donne **ni P = U × I ni loi d'Ohm**.
- Grandeurs variables en **minuscules** (u, i), efficaces en majuscules (U, I) ; U = Um/√2, I = Im/√2 ;
  N = 1/T ; secteur tunisien 220 V / 50 Hz ; q = ± n·e, e = 1,6·10⁻¹⁹ C.

## 4. Chapitrage retenu (→ `manifest/9eme-base.json`) — arbitré le 2026-09-23

Décision du propriétaire (2026-09-23) : **réaligner en place, sans renommer ni supprimer de slug**, et
**créer les chapitres manquants au patron**.

| chapitre | leçons | statut |
| -------- | ------ | ------ |
| `08-tayyar-mostamirr-ohm` | 1–3 | réécrit : il enseignait le courant CONTINU et la loi d'Ohm, absents du programme ; devient « التيّار الكهربائي المتغيّر والتيّار المتناوب الجيبي » (slug gardé) |
| `10-kahraba-manzilia` | 4 | neuf |
| `11-kahraba-sakina` | 5–7 | neuf |
| `12-mahroukat` | 8–9 | neuf |
| `05-tafa3ul-kimiya2i` | 10, 14 | réaligné |
| `04-dharrat-jouzayyat` | 11–13 | réaligné |
| `07-mahalil-charida` | 15–17 | réaligné |
| `06-ahmad-qawa3id-ph` | 18–22 | réaligné |
| `01-intichar-mostaqim-dho2` | — | **rappel des acquis de 8ème** (propagation rectiligne, manuel 103802), prérequis du باب الضوء ; marqué « مراجعة » |
| `02-in3ikas-dho2` | 23–24 | réaligné |
| `03-inkisar-3adasat` | 25–27 | réaligné : les **lentilles**, hors programme 9ème, retirées (slug gardé) |
| `13-dho2-abyadh` | 28 | neuf |
| `09-annales-subur` | toutes | à refaire sur le vrai programme (il reposait sur Ohm et les lentilles) |

## 5. Sources croisées

- `123901P00` (édition collèges pilotes, en français) : même carte du livre ; s'arrête elle aussi à la
  lumière blanche.
- `103802P00` (physique 8ème) : propagation rectiligne, ombres, phases de la Lune (p. 108–145) → fonde le
  rappel `01` ; intensité, tension, lois des nœuds et des mailles (p. 88–103, d'après sa خريطة p. 6) — la loi d'Ohm
  n'y figure pas non plus.

## 6. Incertitudes / à revérifier

1. **Leçons 29–30 absentes** : la خريطة (p. 7) annonce « مفهوم الطاقة الضوئيّة » (p. 200) et « الطاقة
   الشمسيّة » (p. 204), mais la p. 200 clôt la leçon 28, la p. 201 est le titre du lexique et les p. 202–205
   sont **blanches** (images identiques, aucun texte). L'édition 123901 ne les porte pas davantage. Sans
   source, elles ne sont **pas** enseignées ; seul l'objectif de la خريطة est connu : « التعرّف إلى الطّاقة
   الضوئيّة وتحوّلاتها ».
2. **Lexique** (p. 201, 206–223) : doublons (p. 206–210 = p. 214–218) et appariements faux (Déviation —
   انعكاس كلّي ; Réflexion de la lumière — انكسار الضوء ; Diffusion — انتشار) : à ne jamais reprendre.
3. Les incohérences propres à chaque leçon (valeurs imprimées fausses, énoncés ambigus, coquilles) sont
   listées dans sa note au §2 bis.
4. **Relecture R-7 non faite** : transcription de première main par quatre lecteurs indépendants.
