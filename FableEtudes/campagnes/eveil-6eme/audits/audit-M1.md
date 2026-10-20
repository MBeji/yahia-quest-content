# Audit M1 — missions du gisement, éveil 6ᵉ (`09`, `12`, `01`)

Auditeur indépendant (opus), 2026-10-20. Rapport écrit au fil de l'eau.
Périmètre : `09-oeil-vision/06`, `07` ; `12-dhaw/06`, `07` ; `01-air/06`–`13` ; `chapter.json` (sources) des trois chapitres.

## Journal (en cours)

- Lecture des grilles faite (gisement-auditeur, consigne auteurs, PLAN-gisement, assign-M1).

## Chapitre `09-oeil-vision`

Rendu Chromium 360 px `dir="rtl"` fait pour toutes les figures des deux missions : tracés vrais, libellés « الرسم 1/2 », « الصورة 1/2 », chiffres « 1 », « 2 » lisibles et à leur place. Fidélité vérifiée sur les PDF 2008, 2012, 2013, 2015, 2018 (vision 150 dpi, zoom 400 dpi sur les pupilles de 2015 : الصورة 1 = grande pupille, conforme).

### `exercices/06-exams-2008-2013-schemas-de-loeil-defaut-lentille-legendes.json` (9 q)

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | الجسم البلّوري | c | OK | |
| 2 | ترتسم عليه الصورة مقلوبة | b | OK | |
| 3 | قرنيّة→نافذة, قزحيّة→حدقة, شبكيّة→صورة | idem | réserve | paire « القزحيّة ↔ تتكيّف مع كمّيّة النّور » = 02-boss#7 (mineur) |
| 4 | قصر النّظر | b | ERREUR (doublon + fidélité) | = 05-entrainement#6 (même lecture de schéma) ; numérotation inversée |
| 5 | طول النّظر، يُبعد | c | réserve | numérotation inversée |
| 6 | تقرّب… على الشبكيّة | b | ERREUR (fidélité + redemande) | « الحالة (2) » = image derrière : faux au sujet ; redonne le `verifie` du cours (عليّ… عدسة محدّبة لأنّ…) |
| 7 | يقرؤها قريبة | a | réserve | explication livre la clé de Q9 (« وهي المحدّبة ») |
| 8 | مقعّرة، تُبعد | a | ERREUR (fidélité + redemande) | « الحالة (1) » = image devant : faux au sujet ; = quiz#6 et exemple « نظّارة صفوان » |
| 9 | rendu a | a | ERREUR (forme) | seul dessin à point sur la rétine (clé à vue) ; explication désigne une option par sa place (« الرسم الأخير ») |

**C-1 (critique, infidélité de donnée) — Q4, Q5, Q6, Q8.** Au PDF 2013 (support 2), le schéma ① porte l'image d'une fleur **derrière** la rétine (hors du globe) = طول النّظر, le ② **devant** = قصر النّظر. La mission inverse : « الرسم 1 » = devant, « الحالة (2) » = derrière. Correctif (avec M-1 ci-dessous qui supprime Q4 et Q8) : Q5, dans le SVG, `>الرسم 2</text>` → `>الرسم 1</text>` ; Q6 réécrite (M-1).

**M-1 (majeur, ne pas redemander) — Q4, Q6, Q8.** Q4 = 05-entrainement#6 (même schéma, image devant → قصر النّظر) ; Q8 = quiz#6 (« أيّ عدسة تُصلح قصر النّظر، ولماذا؟ المقعّرة، لأنّها تُبعد ») et l'exemple « نظّارة صفوان » ; Q6 = le `verifie` de la section des lentilles (« عليّ مصاب بطول النّظر. أيّ عدسة… ولماذا؟ — محدّبة… تقرّب الأشعّة فتتقدّم الصورة »). Correctif : **supprimer Q4 et Q8** ; **remplacer Q6** par la consigne 2 de 2013 prise d'un bloc (les deux cas à la fois, forme absente du chapitre) :

- prompt : `مناظرة 2013 — «أكمل وأفسّر: يتمّ تعديل الرؤية في الحالة (1) بعدسة ........ لأنّ ........ / يتمّ تعديل الرؤية في الحالة (2) بعدسة ........ لأنّ ........». في الحالة (1) ترتسم الصورة خلف الشبكيّة، وفي الحالة (2) ترتسم أمامها. أيّ إتمام صحيح للجملتين؟`
- a (clé) : `(1) بعدسة محدّبة لأنّها تقرّب الأشعّة، و(2) بعدسة مقعّرة لأنّها تُبعد الأشعّة`
- b `misconceptionTag: eveil.vision.lentilles-inversees` : `(1) بعدسة مقعّرة لأنّها تُبعد الأشعّة، و(2) بعدسة محدّبة لأنّها تقرّب الأشعّة`
- c (muette) : `(1) بعدسة محدّبة لأنّها تُبعد الأشعّة، و(2) بعدسة مقعّرة لأنّها تقرّب الأشعّة`
- d (muette) : `(1) و(2) بعدسة محدّبة لأنّها تكبّر صورة الجسم فتصير أوضح`
- explication : `في الحالة (1) الصورة خلف الشبكيّة، فنحتاج إلى عدسة تقرّب الأشعّة لتتقدّم الصورة إلى الشبكيّة: عدسة محدّبة. وفي الحالة (2) الصورة أمام الشبكيّة، فنحتاج إلى عدسة تُبعد الأشعّة لتتراجع الصورة: عدسة مقعّرة. تبادل العدستين خطأ شائع، والعدسة لا تُصلح العيب بتكبير الصورة بل بتغيير مكان التقاء الأشعّة.`
- `difficulty: 2`. Longueurs : a 77, b 77, c 77, d 55 caractères (clé non strictement la plus longue). La mission passe à 7 questions.

**M-2 (majeur, clé à vue) — Q9.** Seule l'option a montre le point sur la rétine : la clé se lit sans savoir quelle lentille corrige. Correctif (plan 2×2 lentille × lieu) : remplacer l'option c (sans lentille) par une lentille **concave** avec point **sur** la rétine (deux erreurs : muette) :

```
<svg viewBox="0 0 300 160"><circle cx="175" cy="80" r="60" fill="#e0f2fe" stroke="#0f172a" stroke-width="2.5"/><path d="M232.4 63 A60 60 0 0 1 232.4 97" fill="none" stroke="#dc2626" stroke-width="5"/><ellipse cx="150" cy="80" rx="7" ry="24" fill="#bae6fd" stroke="#0f172a" stroke-width="2"/><path d="M122 62 L122 48 M122 98 L122 112" stroke="#b45309" stroke-width="6" fill="none"/><path d="M70 38 L90 38 Q82 80 90 122 L70 122 Q78 80 70 38 Z" fill="#bae6fd" stroke="#0f172a" stroke-width="2"/><polyline points="10,62 80,62 150,54 231,80" fill="none" stroke="#d97706" stroke-width="2.2" stroke-linejoin="round"/><polyline points="10,98 80,98 150,106 231,80" fill="none" stroke="#d97706" stroke-width="2.2" stroke-linejoin="round"/><circle cx="231" cy="80" r="4" fill="#d97706"/></svg>
```

et l'explication (aucune place d'option) : `عين الممرّض طويلة النّظر: الصورة فيها خلف الشبكيّة، فتُصلَح بعدسة محدّبة تقرّب الأشعّة، وبعد التعديل تلتقي الأشعّة على القوس الأحمر. العدسة المقعّرة تُبعد الأشعّة فتدفع نقطة الالتقاء إلى الخلف أكثر، فلا يصحّ رسمٌ يجمع عدسة مقعّرة ونقطةً على الشبكيّة؛ وفي رسم العدسة المحدّبة الّذي تقع فيه النقطة أمام الشبكيّة تقدّمت الصورة أكثر من اللازم.` (rendu vérifié en Chromium, voir plus bas).

**M-3 (majeur, fuite) — Q7.** L'explication nomme la lentille de Q9. Remplacer `العدسة المناسبة، وهي المحدّبة، تقرّب الأشعّة فتقع الصورة على الشبكيّة` par `العدسة المناسبة تُرجع مكان التقاء الأشعّة إلى الشبكيّة`.

**m-1 (mineur) — Q3** : la paire de l'iris recoupe 02-boss#7 ; acceptable : c'est la consigne officielle de 2008 et les deux autres paires (قرنيّة, شبكيّة) sont neuves ; aucun correctif exigé. **m-2 (mineur) — Q7/Q9** : la carte est lue de près mais les rayons dessinés arrivent parallèles (objet lointain) ; tolérable à ce niveau.

### `exercices/07-exams-2015-2018-hypermetropie-lentille-pupille.json` (10 q)

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | طول النّظر | b | réserve | proche de 03-revision#8 / 04-defi#5 (voit loin, lit mal de près) ; garder (phrase officielle) |
| 2 | جسم بلّوري… خلف الشبكيّة | c | réserve | énoncé non autonome (« عين الجدّ » sans dire ce qu'il voit) |
| 3 | a b c d e | idem | ERREUR (fuite) | ses étiquettes visibles donnent mot pour mot la clé de Q2 et celle de Q10 ; rejoue l'exemple « كيف أرى الكرة » |
| 4 | b (sur la rétine) | b | OK | |
| 5 | محدّبة، تقرّب | a | ERREUR (redemande + autonomie) | = `verifie` de la section des lentilles ; « عيب الجدّ » non décrit |
| 6 | a (convergente) | a | réserve | « عيب الجدّ » non décrit (autonomie) |
| 7 | قصر النّظر | b | OK | E-5 appliqué et dit dans l'explication (proche de 03-revision#5, accepté : consigne officielle reformulée) |
| 8 | a | a | réserve | l'explication livre la clé de Q9 |
| 9 | ضوء أكثر | a | ERREUR (critique) | renvoie à « الصورة 1 » sans figure (la figure est dans Q8) |
| 10 | d (derrière) | d | OK | |

**C-2 (critique, figure absente) — Q9.** « فصارت تبدو كما في الصورة 1 » : Q9 n'a pas de SVG ; le donjon la tire seule. Correctif du prompt : `مناظرة 2015 — «أفسّر الاختلاف بين الصورتين». اتّسعت حدقة نور. ما أثر هذا الاتّساع على ما يدخل عينها؟` (sans « ضوء خافت », qui livrerait Q8).

**M-4 (majeur, fuite) — Q8 → Q9.** Remplacer l'explication de Q8 par : `القزحيّة هي الّتي تضبط اتّساع الحدقة حسب كمّيّة الضوء: الحدقة الواسعة في الصورة 1 تناسب الضوء الخافت، والحدقة الضيّقة في الصورة 2 تناسب الضوء القويّ. أمّا بُعد الجسم أو قربه فلا علاقة له باتّساع الحدقة.`

**M-5 (majeur, fuite + redemande) — Q3.** Les items visibles « يجمّع الجسم البلّوري الأشعّة تجميعًا لا يكفي » et « تلتقي الأشعّة في نقطة تقع خلف الشبكيّة » sont la clé de Q2 et celle de Q10 ; la chaîne est l'exemple du cours. Correctif : **supprimer Q3**.

**M-6 (majeur, redemande) — Q5.** Même demande que le `verifie` « عليّ مصاب بطول النّظر. أيّ عدسة يحتاج إليها، ولماذا؟ » et que 02-boss#6. Correctif : **supprimer Q5** et reporter sa note E-5 dans l'explication de Q6 (voir M-7). La mission passe à 8 questions.

**M-7 (majeur, autonomie) — Q2, Q6.** Q2 : remplacer `الأشعّة الآتية من شاشة الهاتف تخترق الأوساط الشفّافة في عين الجدّ. أيّ تفسير صحيح؟` par `الجدّ يرى الثعلب البعيد بوضوح، لكنّه لا يقرأ ما على شاشة الهاتف القريبة. الأشعّة الآتية من الشاشة تخترق الأوساط الشفّافة في عينه. أيّ تفسير صحيح؟`. Q6 : remplacer `أيّ هذه الرسوم يمثّل العدسة الملائمة لعيب الجدّ مع الأشعّة المتوازية الداخلة إليها؟` par `الجدّ يرى الثعلب البعيد بوضوح، ويتعذّر عليه أن يقرأ على شاشة الهاتف القريبة. أيّ هذه الرسوم يمثّل العدسة الملائمة لعيبه مع الأشعّة المتوازية الداخلة إليها؟` ; et l'explication de Q6 : `عيب الجدّ طول النّظر، فعدسته محدّبة: أسمك في وسطها، تقرّب الأشعّة المتوازية وتجمّعها بعد خروجها منها. العدسة المقعّرة تُبعد الأشعّة وتفرّقها فتناسب قصر النّظر، وصفيحة الزجاج ذات الوجهين المتوازيين لا تغيّر اتّجاه الأشعّة فلا تصلح أيّ عيب. تنبيه: في مناظرة 2018 تبعت هذا السؤالَ إجابةٌ تذكر العدسة المقعّرة، وهو خطأ مصدره كتاب مدرسيّ؛ والصواب العلميّ، المعلّل بمكان الصورة خلف الشبكيّة، هو العدسة المحدّبة.`

**m-3 (mineur) — Q2** : « تجميعًا غير كافٍ » n'est pas dit par le cours (qui donne, en للاستزادة, un globe trop court) ; la clé reste la seule défendable (a, b, d sont fausses à vue du cours) — accepté. **m-4 (mineur) — Q8** : le piège C12#6b (pupille et distance) n'a pas d'id au registre ; proposer `eveil.vision.pupille-selon-la-distance` (« Tu crois que la pupille change de taille selon la distance de l'objet : c'est la quantité de lumière qui la fait varier ») pour les options c et d. **m-5 (mineur) — Q4** : la phrase officielle « جسّد هذه الظاهرة » vise le défaut (objet proche), Q4 l'applique à l'objet lointain ; acceptable comme étape préparatoire.

## Chapitre `12-dhaw`

### Point à trancher n° 1 — « se rapproche de la normale en entrant dans l'eau, s'en écarte en sortant »

Relu à l'image : manuel élève 103604P00, p.25–28 (درس « انكسار الضّوء »). Le manuel **ne formule pas** la règle en mots et n'emploie pas « النّاظم » dans ces pages ; mais il l'**enseigne qualitativement et l'exige** :

- p.26 (أجرّب وأتثبّت, photo 1) : le faisceau du مكشاف entre obliquement dans le حويض et se redresse vers la verticale dans l'eau ; conclusion à compléter « … يغيّر اتّجاه انتشاره عند [السطح] من الهواء إلى الماء » ;
- p.27 (6 أطبّق وأوظّف, أ) : « أرسم الشّعاع المنكسر أو الوارد في كلّ وضعيّة » — trois situations (هواء/ماء ; هواء/كحول, rayon donné dans le liquide ; هواء/ماء زهر/هواء) qui sont **exactement** celles du sujet 2017 (m003 Q7–Q9) ; (ب) la pièce de monnaie qui paraît plus proche de la surface ;
- guide p.41–42 : objectif 6 « إدراك ظاهرة انكسار الضّوء » ; la loi d'ابن الهيثم et la table د/ر restent ◐ (savoir du maître), E-9 du plan autorise des options qui ne diffèrent que par « le rapprochement ou l'éloignement de la normale ».

Un élève ne peut pas tracer le rayon de la p.27 sans le sens de la déviation : **c'est donc enseigné qualitativement, et le cours doit le dire** (règle d'or : tout ce qui est testé est enseigné ; aujourd'hui m003 Q5 et m004 Q6 l'exigent sans le rappeler — voir M-9). Le donner dans l'énoncé est la mauvaise solution : le rappel de Q7–Q9 de m003 livre la clé de Q5 (fuite), et il manque à Q5 et à m004 Q6. Texte à ajouter (cours et résumé du `12`, session du chapitre) :

1. `cours.md`, section « 🥄 انكسارُ الضّوء », bloc `::: propriete` — remplacer
   `أو من الماء إلى الهواء). **حالةٌ حدّيّة**: إذا وصل الشّعاعُ **عموديًّا** على سطح الماء، عبره دون أن`
   par
   `أو من الماء إلى الهواء)، والشّعاعُ المنكسرُ يواصلُ سيرَه في الجهة المقابلة للشّعاع الوارد من **النّاظم** (الخطّ العموديّ على السّطح الفاصل عند نقطة الورود): عند **دخوله** الماءَ من الهواء **يقتربُ** من النّاظم، وعند **خروجه** من الماء إلى الهواء **يبتعدُ** عنه. **حالةٌ حدّيّة**: إذا وصل الشّعاعُ **عموديًّا** على سطح الماء، عبره دون أن`
   (la figure de la section montre déjà le rayon « ك » qui se rapproche de la verticale : vérifié au rendu ; y ajouter la normale en pointillés est souhaitable, pas exigé).
2. `cours.md`, même section, un second `::: verifie` après le premier :
   ```
   ::: verifie
   نوجّهُ ضوءَ المكشاف مائلًا نحو ماء الحويض. في أيّ جهةٍ من النّاظم يسيرُ الشّعاعُ داخل الماء، وهل يقتربُ منه أم يبتعدُ عنه؟

   ---

   يسيرُ في الجهة المقابلة للشّعاع الوارد من النّاظم، ويقتربُ منه، لأنّه يدخلُ من الهواء إلى الماء.
   :::
   ```
   (sens air → eau, à dessein : le sens eau → air reste la question de m003 Q5, qui ne redemande donc pas le `verifie`.)
3. `resume.md`, puce « انكسارُ الضّوء » — remplacer `الشّعاعُ العموديُّ على السّطح لا يغيّرُ اتّجاهه.` par `يقتربُ الشّعاعُ من النّاظم عند دخوله الماء، ويبتعدُ عنه عند خروجه إلى الهواء؛ والشّعاعُ العموديُّ على السّطح لا يغيّرُ اتّجاهه.`

Une fois le cours complété : dans m003 Q7, Q8 et Q9, **supprimer** la phrase de rappel `نذكّر بأنّ الشعاع الّذي يدخل الماء مائلًا يقترب من الناظم، وأنّ الشعاع الّذي يخرج من الماء إلى الهواء يبتعد عن الناظم، وأنّ الشعاع المنكسر يقع في الجهة المقابلة للشعاع الوارد من الناظم (الخطّ المنقّط).` et la remplacer par `الخطّ المنقّط هو الناظم.` ; dans m004 Q9, remplacer `نذكّر بأنّ الشعاع الّذي يدخل الماء مائلًا يقترب من الناظم (الخطّ المنقّط)، ويقع في الجهة المقابلة للشعاع الوارد.` par `الخطّ المنقّط هو الناظم.` (si Q9 est gardée, voir M-12). **Tant que le cours n'est pas complété, les missions m003 et m004 ne partent pas** (carte, E-11).

### `exercices/06-exams-2016-2017-refraction-definition-et-rayons.json` (9 q)

Fidélité : PDF 2016 et 2017 relus ; les trois situations, le poisson, les mots soulignés « انعكاس / انتشار / الكتلة » et le défaut « من الهواء إلى الماء » (E-5) sont fidèles.

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | تغيّر | b | ERREUR (majeur) | la clé est écrite dans l'énoncé (« تغيّر اتّجاهها ») |
| 2 | انكسار | d | ERREUR (majeur) | l'option b reprend le mot que l'énoncé déclare faux : s'élimine à vue |
| 3 | الشفّافيّة | a | ERREUR (majeur) | l'option c contient « الكتلة », le mot déclaré faux |
| 4 | c | c | OK | figures vraies (rendu) ; proche de la figure de la pièce du cours (consigne officielle : gardée) |
| 5 | d | d | réserve | exige la règle du point 1, non enseignée et absente de l'énoncé ; donnée par le rappel de Q7–Q9 (fuite) |
| 6 | أعمق | b | ERREUR (majeur) | énoncé recopié de 02-boss#4 (« ينظر صيّاد من زورقه… فيراها أقرب إلى السطح ممّا هي عليه ») ; c'est l'ancrage du cours (« مددتَ يدَك… فوجدتَها أعمق ») ; aucune phrase officielle de 2016 |
| 7 | a | a | OK | figures vraies |
| 8 | c | c | OK | figures vraies |
| 9 | b | b | ERREUR (critique) | b et c respectent toutes deux la règle donnée (côté opposé, s'écarte de la normale) ; seule la quantité (« parallèle ») les sépare : deux réponses défendables, contraire à E-9 |

**C-3 (critique, deux réponses) — Q9.** Remplacer l'option c (sortie plus inclinée que l'entrée) par une sortie qui se **rapproche** de la normale (erreur de sens, qualitative) :

```
<svg viewBox="0 0 210 140"><rect x="0" y="50" width="210" height="50" fill="#bfdbfe"/><line x1="0" y1="50" x2="210" y2="50" stroke="#0f172a" stroke-width="2"/><line x1="0" y1="100" x2="210" y2="100" stroke="#0f172a" stroke-width="2"/><line x1="100" y1="10" x2="100" y2="130" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5 4"/><line x1="131.2" y1="70" x2="131.2" y2="135" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5 4"/><polyline points="54,11.4 100,50" fill="none" stroke="#d97706" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><polyline points="74.1,24.3 77.0,30.7 70.2,29.0" fill="none" stroke="#d97706" stroke-width="2.2" stroke-linejoin="round"/><polyline points="100,50 131.2,100" fill="none" stroke="#d97706" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><polyline points="114.8,68.0 115.6,75.0 109.7,71.3" fill="none" stroke="#d97706" stroke-width="2.2" stroke-linejoin="round"/><polyline points="131.2,100 137.5,125" fill="none" stroke="#d97706" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><polyline points="129.3,106.5 134.4,112.5 135.9,104.9" fill="none" stroke="#d97706" stroke-width="2.2" stroke-linejoin="round"/></svg>
```

et l'explication : `عند الدخول إلى الماء يقترب الشعاع من الناظم، وعند الخروج منه إلى الهواء السفليّ يبتعد عنه، فيقع الشعاع الخارج في الجهة المقابلة من الناظم وأبعد عنه من الشعاع داخل الماء، فيخرج في الواقع موازيًا للشعاع الوارد. في الرسم الّذي يواصل فيه ميله داخل الماء لم ينكسر الشعاع عند الخروج، وفي الرسم الّذي يقترب فيه من الناظم عند الخروج اتّجاه الانحراف معكوس، وفي الرسم الّذي يعود فيه إلى جهة الورود خطأ في الجهة.` (rendu vérifié, voir § Rendus.)

**M-8 (majeur, indices de forme) — Q1, Q2, Q3.**
- Q1 : supprimer de l'énoncé la phrase `والأشعّة في هذه الظاهرة تغيّر اتّجاهها عند السطح الفاصل بين الوسطين.` et remplacer `«[انتشار] في مسار الأشعّة الضّوئيّة».` par `«[انتشار] في مسار الأشعّة الضّوئيّة المارّة من وسط شفّاف إلى وسط شفّاف آخر».`
- Q2 : supprimer l'option b (`انعكاس`, déjà le mot à corriger) ; l'étiquette reste sur c. Trois options.
- Q3 : remplacer l'option c `الكتلة والثقل` par `درجة الحرارة`, et dans l'explication `كتلة الوسط ولونه وشكله` par `حرارة الوسط ولونه وشكله`.

**M-9 (majeur, notion non enseignée) — Q5** (et m004 Q6) : sans le cours complété (point 1), la clé repose sur une règle que ni le cours ni l'énoncé ne donnent. Correctif : le point 1.

**M-10 (majeur, redemande) — Q6** : **supprimer Q6** (la mission passe à 8 questions).

### `exercices/07-exams-2008-2012-reflexion-miroir-rayons-et-definitions.json` (9 q)

Fidélité : PDF 2008, 2009, 2012 relus ; cas a/b/c de 2012, deux schémas de 2009 (miroir ; eau), deux situations de 2008 : fidèles.

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | b | b | ERREUR (majeur) | l'énoncé ne cite pas le texte souligné : reste « quelle est la définition de la réflexion ? » = quiz#2 et la définition du cours ; l'explication parle du « premier / second » texte imprimé que l'élève ne voit pas |
| 2 | a | a | ERREUR (majeur) | option c « لا خطأ في العبارة » nie la prémisse (« هذه العبارة المسطّرة خاطئة ») |
| 3 | b | b | ERREUR (majeur) | = 04-defi#8 (même figure : quel rayon est le réfléchi ?) |
| 4 | c | c | ERREUR (majeur) | = 04-defi#2 et la « حالة حدّيّة » du cours (rayon perpendiculaire qui revient sur lui-même) |
| 5 | a | a | OK | |
| 6 | a | a | réserve | exige la règle du point 1 (aucun rappel) |
| 7 | l1-r3, l2-r1, l3-r2 | idem | OK | |
| 8 | c | c | OK | geste inverse, neuf |
| 9 | b | b | ERREUR (majeur) | même tâche, mêmes quatre dessins que m003 Q7 (air → eau, rayon réfracté) et que Q6 de cette mission |

**M-11 (majeur) — Q2** : remplacer l'option c `لا خطأ في العبارة، فكلّ جسم عاتم يكسر الضوء الّذي يصل إليه فيغيّر مساره` par `ينتج الانكسار عن مرور الضوء عبر جسم عاتم، فيخرج من جهته الأخرى بميل مختلف`.

**M-12 (majeur, ne pas redemander) — Q1, Q3, Q4, Q9** : **supprimer** les quatre. Q1 n'a pas d'autre forme non redondante (la forme « mot souligné à corriger » est déjà m003 Q2, sujet 2017 identique). La mission tombe à 5 questions (Q2, Q5, Q6, Q7, Q8) : soit elle part ainsi (boss court), soit le pilote la fusionne avec m003 (10 questions au total après les suppressions de m003). Recommandation : fusion, sous le nom de m003, en gardant les sessions citées.

Rendus des deux SVG de remplacement (m001 Q9 option c ; m003 Q9 option c) : vérifiés en Chromium 360 px `dir="rtl"` — lentille concave et point sur la rétine ; rayon de sortie qui se rapproche de la normale, flèche dans le sens de la marche.

## Chapitre `01-air`

Rendu Chromium 360 px `dir="rtl"` de toutes les figures (06 à 13) : libellés « إناء 1/2 », « أنبوب 1/2 », « ماء ملوّن » lisibles ; une légende mal placée (m005, ci-dessous).

### `exercices/06-exam-2025-deux-bocaux-bougie-et-glace.json` (8 q)

Fidélité : PDF et transcription 2025 relus (deux bocaux de 100 صل, tubes 1 et 2, phrases des consignes 1, 2-أ, 2-ب, 3) : fidèles.

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | هباب الفحم | b | ERREUR (majeur) | option d « لا خطأ في الإفادة » nie la consigne « أصلح الخطأ » ; l'explication livre la clé de Q2 (« بخار الماء وثاني أكسيد الكربون ») |
| 2 | بخار الماء وثاني أكسيد الكربون | a | OK | |
| 3 | O₂ أصغر, N₂ تساوي, CO₂ أكبر | idem | ERREUR (critique, science) | « نسبة » : après la combustion l'eau monte dans le bocal 1, le gaz restant a un volume plus petit pour la même quantité d'azote : la **proportion** d'azote y est plus grande, pas égale. Juste seulement pour la **quantité** |
| 4 | b | b | réserve | proche de 04-defi#3 et du `verifie` (air refroidi qui se contracte) ; gardée (situation entière de 2025, piège propre : l'oxygène consommé) ; explication qui livre Q5 |
| 5 | d | d | ERREUR (majeur) | non autonome (le bocal 2 n'est ni décrit ni dessiné) ; clé donnée par l'énoncé et l'explication de Q4 ; même piège que le distracteur c de Q4 |
| 6 | 100 ÷ 5 | a | OK | E-4 respecté (« حوالي », la bougie s'éteint avant) ; option b (×5 → 500 صل > 100) faible |
| 7 | c | c | ERREUR (majeur) | même défaut « نسبة » que Q3 ; l'étiquette `azote-entretient-combustion` est sur b (l'azote « augmente ») alors que c'est a qui exécute l'erreur (« النتروجين يساعد على الاحتراق ») |
| 8 | 20 | 20 | ERREUR (majeur) | la réponse est dans la phrase officielle citée par l'énoncé (« تقدّر بحوالي 20 صل ») |

**C-4 (critique, science) — Q3 et Q7 : « نسبة » → « كمّيّة ».** Le sujet compare des « نسب » ; la mission compare des quantités, et l'explication le dit (E-5). Remplacements exacts :
- Q3, options : `نسبة الأكسجين في الإناء 1 مقارنةً بالإناء 2` → `كمّيّة الأكسجين في الإناء 1 مقارنةً بالإناء 2` ; idem pour `نسبة النتروجين` → `كمّيّة النتروجين` et `نسبة ثاني أكسيد الكربون` → `كمّيّة ثاني أكسيد الكربون`. Ajouter à la fin du prompt (avant le SVG) : ` (نقارن الكمّيّات: نسب الغازات في الورقة الأصليّة تتغيّر كلّها في الإناء 1، لأنّ الماء صعد إليه فصغر حجم الغاز.)`. Explication : remplacer `فنسبة الأكسجين أصغر من نسبته في الإناء 2، ونسبة ثاني أكسيد الكربون أكبر. أمّا النتروجين فلا يتدخّل في الاحتراق، فنسبته في الإناءين متساوية.` par `فكمّيّة الأكسجين أصغر من كمّيّته في الإناء 2، وكمّيّة ثاني أكسيد الكربون أكبر. أمّا النتروجين فلا يتدخّل في الاحتراق، فكمّيّته في الإناءين متساوية.`
- Q7 : prompt `لماذا لا تتغيّر نسبة النتروجين في الإناء 1؟` → `لماذا لا تتغيّر كمّيّة النتروجين في الإناء 1؟` ; option b `لأنّ نسبة النتروجين تزيد بقدر ما تنقص نسبة الأكسجين دائمًا` → `لأنّ كمّيّة النتروجين تزيد بقدر ما تنقص كمّيّة الأكسجين` **sans étiquette** ; poser `misconceptionTag: eveil.air.azote-entretient-combustion` sur l'option a ; explication `فكمّيّته ثابتة ونسبته ثابتة` → `فكمّيّته ثابتة`.

**M-13 (majeur) — Q1** : supprimer l'option d ; remplacer l'explication par `هباب الفحم جسيمات سوداء لا تظهر إلّا حين يكون الاحتراق غير تامّ، أمّا بخار الماء فمن نواتج احتراق الشمعة دائمًا. فالخطأ هو ذكر هباب الفحم.`

**M-14 (majeur) — Q5 et Q8** : **supprimer Q5 et Q8** (la mission passe à 6 questions). Dans l'explication de Q4, supprimer `الخطأ الشائع تفسير الصعود باستهلاك الأكسجين، مع أنّه لا شيء يحترق في الإناء 2.` et mettre `ولا يصحّ تفسيره باستهلاك الأكسجين: لا شيء يحترق في الإناء 2.`

**m-6 (mineur, figure) — Q3/Q4** : la légende « ماء وثلج » est écrite dans le bocal 2 (qui contient de l'air). Dans le SVG (deux occurrences, Q3 et Q4), remplacer `<text x="269" y="184" font-size="14"` par `<text x="269" y="104" font-size="14"` (« إناء 2 » dans le bocal) et `<text x="269" y="92" font-size="12"` par `<text x="269" y="184" font-size="12"` (« ماء وثلج » sous le récipient) — rendu vérifié.

### `exercices/07-exams-2019-2021-refroidir-chauffer-peser-lair.json` (9 q)

Fidélité : PDF 2019, 2020, 2021 relus (356,6 / 354 / 2 ل ; 615,3 / 613,5 / 1 ل ; دورق chauffé) : données fidèles. Au PDF 2021 la balance ne porte que la balle, la bouteille de 2 ل est à côté : l'énoncé est juste.

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | b | b | ERREUR (majeur) | = 04-defi#3 (flacon refroidi, l'eau monte dans le tube) et doublon de m005 Q4 (même cause, mêmes options a/b) |
| 2 | a | a | réserve | option d « قوله صحيح » s'élimine à vue (mineur) ; non autonome si Q1 disparaît (voir correctif) |
| 3 | c | c | OK | prévision (2021 2-ب) |
| 4 | a b c d e | idem | ERREUR (critique) | deux ordres défendables : retourner la bouteille pleine sur le bassin (b) peut se faire avant la première pesée (a) |
| 5 | 2,6 | 2,6 | OK | |
| 6 | 1,8 | 1,8 | OK | |
| 7 | c | c | ERREUR (majeur) | = 01-pratique#5 (flacon chauffé → bulles → dilatation) et même geste que Q3 |
| 8 | 1,3 | 1,3 | OK | |
| 9 | d | d | OK | |

**C-5 (critique) — Q4** : fusionner b et c. Item b → `تقلب قارورة سعتها 2 ل مملوءة بالماء الملوّن فوق حوض فيه ماء ملوّن، ثمّ توصلها بالكرة بأنبوب فيطرد الهواء ماءها كلّه` ; supprimer l'item c ; `answerKey.order` → `["a", "b", "d", "e"]`.

**M-15 (majeur, redemande) — Q1, Q7** : supprimer Q1 et Q7 (7 questions restent). Q2 devient autonome : prompt → `مناظرة 2021 — «أتأمّل التّجربة وأفسّر سبب صعود الماء الملوّن في الأنبوب بعد إضافة الماء والثّلج إلى الإناء البلّوري.» قارورة فيها هواء مسدودة بسدّادة يعبرها أنبوب ينغمس طرفه في ماء ملوّن، وُضعت في إناء بلّوريّ أضيف إليه الماء والثلج، فصعد الماء الملوّن في الأنبوب. قال تلميذ: «الهواء البارد يمصّ الماء الملوّن إلى الأعلى». أيّ تفسير يصحّح قوله؟` suivi du SVG actuel de Q1 (déplacé tel quel) ; option d `قوله صحيح، فكلّ غاز بارد يمصّ السوائل القريبة منه` → `الماء الملوّن يتمدّد بالبرودة فيرتفع وحده في الأنبوب`. Le piège C08#10 (compression) de Q7 disparaît avec elle ; il reste porté par 01/01-pratique (انضغاط).

**m-7 (mineur)** — l'item e de Q4 (« تقسم الفرق على سعة القارورة ») et l'explication de Q4 donnent la méthode de Q8 ; tolérable (la valeur n'est pas donnée).

**M-15 bis (majeur, paire proche) — Q5** (2,6 g) est l'étape intermédiaire de Q8, même données (tranche : Jaccard 0,63) : **supprimer Q5** ; Q8 garde le calcul complet dans son explication. m006 finit à 6 questions (Q2, Q3, Q4, Q6, Q8, Q9).

### `exercices/08-exams-2020-2024-bougie-sous-le-tube-un-cinquieme-doxygene.json` (10 q)

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | تدريجة 1 | a | réserve (figure) | légende « ماء ملوّن » coupée au bord gauche en page RTL (ancre `start`) |
| 2 | a, c | a, c | OK | E-5 (« ربع حجم الهواء ») dit dans l'explication |
| 3 | a b c d | idem | OK | |
| 4 | a | a | OK | |
| 5 | b, c | b, c | réserve | l'item c (خُمس) est la 4ᵉ occurrence du cinquième dans la mission |
| 6 | d | d | ERREUR (majeur) | = quiz#5 (« نكّسنا قارورة على شمعة… تنطفئ لأنّ الأكسجين يقلّ ») |
| 7 | c | c | OK | E-4 respecté |
| 8 | c | c | OK | plan 2×2 propre (d à deux erreurs, muette) ; « la masse ne change pas au chauffage » n'est pas écrit au cours (mineur, voir m-9) |
| 9 | b | b | ERREUR (majeur) | l'énoncé (« يستقرّ الماء عند تدريجة واحدة ») donne la clé de Q1 ; Q9 redemande Q1 (cinquième) |
| 10 | d | d | ERREUR (majeur) | option a « أربعة أخماس » = 80 %, la valeur que l'énoncé déclare fausse (s'élimine à vue) ; le cinquième est déjà Q1, Q2, Q5 |

**M-16 (majeur) — Q6, Q9, Q10 : supprimer** (7 questions restent). Q5 : remplacer l'item c `يمثّل الأكسجين حوالي خُمس حجم الهواء` par `يتكوّن ثاني أكسيد الكربون أثناء احتراق الشمعة` (clé inchangée : b, c) et, dans l'explication, `والأكسجين حوالي خُمس حجم الهواء، وهو الّذي يساعد على الاحتراق لا النتروجين.` par `وثاني أكسيد الكربون من نواتج الاحتراق، والأكسجين هو الّذي يساعد على الاحتراق لا النتروجين.`

**M-17 (majeur, rendu) — Q1** : dans le SVG, remplacer `<text x="40" y="172" font-size="12" font-weight="700" fill="#0f172a" text-anchor="start"` par `<text x="56" y="172" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle"` (rendu vérifié : la légende tient dans le bassin, à gauche du tube).

**m-9 (mineur, cours)** — Q8 : la conservation de la masse de l'air chauffé n'est pas écrite au cours ; à ajouter à la `propriete` de la section « 🌡️ » : `حالة للانتباه: حين يسخن الهواء يزداد حجمه، لكنّ كتلته لا تتغيّر، لأنّ كمّيّته هي نفسها.` (session du chapitre).

### `exercices/09-exams-2019-2026-bruleur-flamme-complete-ou-incomplete.json` (9 q)

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | a, b, e | idem | OK | E-5 (suie en flamme bleue) dit ; paires a/c et d/e contradictoires (mineur) |
| 2 | a | a | ERREUR (majeur) | = 04-defi#6 (flamme jaune → suie, combustion incomplète) ; donnée par Q1 (b, d, e et son explication) |
| 3 | d | d | OK | |
| 4 | a, c | a, c | OK | monoxyde enseigné (section ☠️) |
| 5 | d | d | ERREUR (majeur) | même savoir que Q7 (clé presque identique : « الهواء غير كافٍ فصار الاحتراق غير تامّ ») |
| 6 | a | a | ERREUR (majeur) | même savoir (assez / pas assez d'oxygène) que Q2, Q5, Q7, Q9 |
| 7 | b | b | OK | |
| 8 | c | c | réserve | « فعلًا » désigne l'option a (la phrase citée) comme fausse avant lecture |
| 9 | b | b | ERREUR (majeur) | quatrième « l'oxygène suffit / ne suffit pas » de la mission |

**M-18 (majeur, redondance interne) — supprimer Q2, Q5, Q6, Q9** (5 questions restent : Q1, Q3, Q4, Q7, Q8 ; les sessions 2019 et 2022 3-2-ب tombent, la 2022 reste par Q4). Q8 : remplacer `ماذا وفّر تعديل ضابط الهواء فعلًا؟` par `ماذا يوفّر تعديل ضابط الهواء؟`.

### `exercices/10-exams-2008-2024-elements-produits-et-preuves-de-la-combustion.json` (12 q)

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | a, b, c | idem | ERREUR (majeur) | = 01-pratique#6 (trois éléments) et même contenu que Q4 |
| 2 | a, b | a, b | OK | |
| 3 | d | d | ERREUR (majeur) | même contenu que Q2 (l'oxygène n'est pas un produit) ; paire proche Q3↔Q4 (tranche) |
| 4 | d | d | OK | |
| 5 | a | a | OK | E-5 (chaleur) dit |
| 6 | c | c | réserve | miroir de quiz#4 ; gardée (formulation officielle 2008, quatre tests) ; son explication livre la clé de Q9 corrigée |
| 7 | d | d | OK | |
| 8 | b | b | ERREUR (majeur) | cause « pas assez d'oxygène » déjà posée par m008 (Q7) et 05-entrainement#4 |
| 9 | a | a | ERREUR (majeur) | même clé que m010 Q4 (« بخار الماء… يتكثّف عند ملامسة سطح بارد ») ; le geste de 2020 est la PREUVE d'un produit |
| 10 | a b c d | idem | réserve | c (éloigner l'assiette) et d (constater le noir) permutables |
| 11 | a | a | ERREUR (majeur) | = 04-defi#6 (assiette blanche noircie au-dessus de la flamme jaune → هباب الفحم) |
| 12 | appariement | idem | ERREUR (majeur) | = 04-defi#7 (mêmes quatre paires observation ↔ gaz) |

**M-19 (majeur) — supprimer Q1, Q3, Q8, Q11, Q12** (7 questions restent).
**M-20 (majeur) — Q9 réécrite** (la preuve, pas la condensation) :
- prompt : `مناظرة 2020 — «أعمّر فراغات الجدول التّالي حسب ما تتطلّبه كلّ وضعيّة من الوضعيّتين التّاليتين.» في الوضعيّة 1 ننكّس أنبوبًا باردًا على لهب شمعة فتظهر قطرات ماء على جداره الداخليّ. ما الناتج الّذي تثبته هذه الملاحظة؟`
- a (clé) `بخار الماء من نواتج احتراق الشمعة` ; b `ثاني أكسيد الكربون من نواتج احتراق الشمعة` (`eveil.gaz.test-mal-associe`) ; c `هباب الفحم من نواتج احتراق الشمعة` (muette) ; d `الأكسجين من نواتج احتراق الشمعة` (`eveil.air.reactifs-et-produits-inverses`).
- explication : `الاحتراق ينتج بخار الماء، فإذا لامس جدار الأنبوب البارد تكثّف قطرات ماء: فالقطرات تثبت أنّ بخار الماء من نواتج الاحتراق. ثاني أكسيد الكربون يُكشف بتعكّر ماء الجير، وهباب الفحم بسواد صحن أبيض، والأكسجين يُستهلك في الاحتراق ولا ينتج عنه.`
- longueurs : a 33, b 41, c 34, d 33 (clé non la plus longue).
- Q6, explication (pour ne plus livrer Q9) : remplacer `اسوداد الصحن يدلّ على هباب الفحم، وقطرات الماء على جدار بارد تدلّ على بخار الماء، والفرقعة ليست كشفًا لثاني أكسيد الكربون.` par `اسوداد الصحن يدلّ على هباب الفحم، والفرقعة وقطرات الماء لا تكشفان ثاني أكسيد الكربون.`
**m-10 (mineur) — Q10** : fusionner c et d → c `نبعد الصحن عن اللهب بعد لحظات فنلاحظ أنّه اسودّ`, supprimer d, `order` `["a","b","c"]`.

### `exercices/11-exams-2013-2023-proprietes-et-composants-de-lair.json` (10 q)

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | بخار الماء | b | ERREUR (majeur) | = 01-pratique#4 (gouttelettes sur une paroi froide → vapeur d'eau de l'air) |
| 2 | a | a | OK | |
| 3 | c | c | OK | |
| 4 | b | b | OK | |
| 5 | a, b, c | idem | ERREUR (majeur) | = `verifie` de la section « 🎈 » (طوق gonflé : compressible + se répand) ; option e « لون أزرق » de remplissage |
| 6 | a, c, e | idem | réserve | a (cinquième) redit m005/m007 ; b et c contradictoires (une seule juste, déductible) |
| 7 | l1-r2, l2-r3, l3-r1 | idem | réserve | l3 (montgolfière) se défend aussi par r3 (dilatation) ; tenable car r1 est la seule qui explique la montée et l2 n'est expliqué que par r3 |
| 8 | a | a | ERREUR (majeur) | = 01-pratique#5 et tableau du cours (air chauffé → bulles) ; doublon de m006 Q3 |
| 9 | a | a | ERREUR (majeur) | = 04-defi#3 (glace → l'eau monte) ; doublon de m005 Q4 |
| 10 | b | b | ERREUR (majeur) | même question et même clé que m007 Q7 (« نقص/اختفى جزء من الغاز… مكان شاغر ») |

**M-21 (majeur) — supprimer Q1, Q5, Q8, Q9, Q10** (5 questions restent : Q2, Q3, Q4, Q6, Q7). Q6 : remplacer l'item a `الأكسجين يمثّل حوالي خُمس حجم الهواء` par `الهواء خليط من عدّة غازات` (clé inchangée a, c, e) et, dans l'explication, `الأكسجين حوالي خُمس حجم الهواء، والهواء` par `الهواء خليط من غازات، وهو`. Si 5 questions paraissent trop peu pour un boss, fusionner m010 dans m012 ou m006 (décision du pilote).

### `exercices/12-devoir-un-feu-conditions-etat-tirage.json` (9 q, salle blanche)

`content:gisement:controle` : 0 plage ≥ 8 mots, 0 à ≥ 6 mots, 0 exercice source à ≥ 3 données (19 textes des deux devoirs). Snapshots non lus.

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | c | c | OK | |
| 2 | a | a | réserve | même fait que m009 Q4 (CO₂ n'est pas un intervenant) — accepté (geste du devoir : corriger une définition) |
| 3 | l1-r3, l2-r1, l3-r2 | idem | réserve | « le bois chauffé dégage des gaz qui brûlent » n'est pas écrit au cours (bougie seulement) ; soluble par élimination |
| 4 | d | d | OK | |
| 5 | b | b | OK | |
| 6 | c | c | ERREUR (majeur) | = 03-revision#3 (ouverture basse du poêle → air neuf) et l'exemple du cours ; la carte l'interdisait |
| 7 | d | d | OK | |
| 8 | a b c d e | idem | OK | cinq temps (le patron en a trois) |
| 9 | a | a | réserve | même scène que 05-entrainement#4 (charbon, pièce fermée) ; clé différente (CO) : gardée |

**M-22 (majeur) — supprimer Q6** (8 questions).

### `exercices/13-devoir-experiences-sur-lair.json` (10 q, salle blanche)

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | c | c | OK | |
| 2 | a | a | ERREUR (majeur) | = 01-pratique#2 (compresser → résistance) et même savoir que Q1 |
| 3 | d | d | OK | |
| 4 | b | b | OK | |
| 5 | c | c | ERREUR (majeur) | = `verifie` de la section « 🌡️ » (« سخّنّا قارورة… ثمّ برّدناها ونكّسناها في حوض ماء، فدخل الماء ») |
| 6 | d | d | ERREUR (majeur) | trois distracteurs de remplissage (« نكتب أنّنا قمنا بتجربة طويلة ») ; compression déjà Q1 |
| 7 | a | a | OK | |
| 8 | appariement | idem | réserve | deux paires sur trois = 04-defi#7 ; la paire de l'azote est neuve |
| 9 | b | b | ERREUR (majeur) | même question et même clé que m007 Q7 (et m010 Q10) |
| 10 | c | c | OK | piège « air consommé » propre |

**M-23 (majeur) — supprimer Q2, Q5, Q6, Q9** (6 questions).

## Point à trancher n° 3 — les recouvrements « assumés » (m010, m006)

Le rapport de l'auteur les justifie par « le sujet les impose ». La règle R6 / E-12 du plan et la consigne des auteurs ne prévoient **aucune** exception de ce type : « aucune question ne redonne un exemple, un piège ou un `verifie` du cours, ni une question des exercices 01–05 ». Une phrase officielle reprise ne rend pas neuve une question dont la tâche et la clé sont celles d'un exercice publié : l'élève qui a fait 01/01-pratique#5 refait m010 Q8 et m006 Q7 sans rien apprendre. Verdict : **non recevables**. Les sessions concernées restent citées par les autres questions des mêmes missions (2013 par m010 n'a plus de question : la session 2013 reste servie en `09` et `12`, la règle « 17 sessions sur 17 » tient). Correctifs : M-14, M-15, M-21 (et, par la même règle, M-1, M-6, M-10, M-12, M-16, M-18, M-19, M-22, M-23).

Note sur le doute de l'auteur : « الصورة 1 », « الرسم 1 », « أنبوب 2 », « إناء 1 » s'affichent dans le bon ordre en Chromium `dir="rtl"` (ancre `middle`) ; une seule légende fautive (M-17, ancre `start`).
