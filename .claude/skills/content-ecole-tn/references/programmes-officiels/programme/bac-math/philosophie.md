# الفلسفة / Philosophie — Baccalauréat (الشّعب العلميّة) · programme officiel CNP

> **Sources** (une seule — voir §5) :
>
> - **Guide enseignant** (programme) : **non disponible au corpus CNP**. Aucun guide n'existe pour
>   ce couple ⇒ **le manuel élève fait référence** (profil `ecole-secondaire`).
> - **Manuel élève** (contenu/exemples/exercices) : `210402P00.pdf`
>   (`cnp-officiel/manuels/secondaire/c4/eleve/`) — « كتاب الفلسفة — لتلاميذ السّنة الرّابعة من
>   التّعليم الثانوي — الشّعب العلميّة ». **408 pages** (page PDF = page imprimée, **offset 0**).
>   **Pages lues** : p.1–6 (page de titre, copyright, التقديم, خارطة الكتاب, ouverture du محور 1),
>   p.404–408 (فهرس الكتاب intégral).
>   **Transcrit le** : 2026-08-04. **Statut** : ⚠️ **first-pass — ossature seule** (voir §6).
>   **Langue d'enseignement** : `ar`. **gradeSlug porteur** : `bac-math`.
>   **subject ids** attendus : `philosophie-bac-math`, `philosophie-bac-sciences-exp`,
>   `philosophie-bac-eco-gestion`, `philosophie-bac-techniques`, `philosophie-bac-info`
>   (un seul dossier source `content/philosophie-bac/`, mutualisé par `compileTo`).

## 0. Quelles sections ce manuel dessert-il ? (le constat, pas la déduction)

Question ouverte par le plan de campagne : « الشّعب العلميّة » ne détaille pas ses sections — le
rattachement d'**éco-gestion** était **déduit par élimination**. Ce qui a été **constaté**, avec ses
pages :

1. **Page de titre (p.1)** : le manuel s'adresse à « **لتلاميذ السّنة الرّابعة من التّعليم الثانوي
   — الشّعب العلميّة** ». Il nomme le **groupe** de sections ; **il n'en énumère aucune**.
2. **التقديم (p.3)** et **خارطة الكتاب (p.4–5)** : aucune liste de sections non plus. Le verso de la
   page de titre (p.2) ne porte que le copyright du CNP.
3. **Catalogue CNP (`cnp-officiel/catalogue.csv`, 346 manuels — recherche exhaustive sur
   « فلسفة »)** : pour la 4ème année (`classe = 4`), il n'existe que **deux** manuels de
   philosophie — `210402` « فلسفة_الشعب العلمية » et `210422` + `210423` « فلسفة ج1/ج2_شعبة
   الآداب » (deux tomes). **Aucun manuel propre** à éco-gestion, aux sections techniques ou à
   l'informatique.

**Conclusion** : le manuel lui-même **ne tranche pas** (constat 1–2) ; c'est l'**exhaustivité du
catalogue officiel** (constat 3) qui tranche. La partition des manuels de philosophie du bac est
binaire — آداب d'un côté, tout le reste de l'autre — donc les cinq sections non-Lettres
(`bac-math`, `bac-sciences-exp`, `bac-eco-gestion`, `bac-techniques`, `bac-info`) sont desservies
par `210402`. Le rattachement d'éco-gestion n'est donc **plus une déduction par élimination interne
au manuel**, mais un constat sur le corpus officiel complet.

⛔ **`bac-lettres` n'est pas une cible de cette fiche** : sa philosophie est un autre programme,
nettement plus large, porté par `210422` + `210423` (deux tomes). Ces deux codes restent **non
rattachés** au registre et demandent leur propre LOT A.

## 1. Cadre & compétences (الكفايات / les objectifs généraux)

Transcrit du **التقديم (p.3)** et de la **خارطة الكتاب (p.4–5)** — le manuel n'ayant pas de guide,
c'est là que le cadrage est imprimé.

**L'intention déclarée (التقديم, p.3)** — la philosophie y est posée en **atelier**, pas en corpus
à mémoriser. Le manuel s'ouvre sur une formule attribuée à كانغيلام : la philosophie n'est pas un
temple mais **un atelier** (« ليست الفلسفة معبدا، إنّها ورشة »). La lecture qu'en tire la commission
d'auteurs, telle qu'imprimée :

- l'ambition **n'est pas** de développer le seul stock de connaissances de l'élève
  (« لا تطمح لجنة التأليف … إلى تنمية مخزونك المعرفي فقط ») ;
- elle est de lui donner **l'occasion de reprendre sa pensée et d'examiner ce qui s'y est
  déposé**, face aux problèmes philosophiques pris comme problèmes de l'humain lui-même ;
- le manuel se veut un **espace partagé** — un moment où les idées s'attirent et se repoussent,
  où le plaisir de se rapprocher rivalise avec celui de diverger ;
- la thèse adressée à l'élève : penser à la manière des philosophes **est possible**, reconsidérer
  ses propres convictions **est possible**, l'indépendance du jugement **est possible**.

**Les compétences visées, telles que l'en-tête de la خارطة الكتاب (p.4) les énonce** — verbatim :

> « أتمرّس بالحريّة بفضل ممارسة التفكير — أتمكّن من فهم أفضل وتأويل أعمق لما أعرف سلفا — أتحرّر من
> قوالب الآراء المتداولة ومن سيطرة الأحكام المتسرّعة »

Soit quatre capacités : **s'exercer à la liberté** par la pratique de la pensée · **mieux
comprendre et interpréter plus profondément** ce qu'on sait déjà · **se libérer des moules** des
opinions courantes · et **de l'emprise des jugements hâtifs**.

Le bandeau latéral de la même page ajoute la série d'opérations attendues (lisible verticalement,
p.4) : **مفاهيم — بنية — تقنيات — تمشّيات — سياقات — تأليف — مقالات — منهجيّة** [?] (bandeau en
rotation, voir §6).

**La démarche en six fenêtres (نوافذ)** — c'est l'ossature de chaque مبحث, et elle est explicitée
p.4–5 :

| #   | نافذة                                | ce qu'elle fait faire à l'élève (p.4–5)                                                                                                             |
| --- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **مدخل إلى التفكير في المسألة**      | « أبدأ في التفكير في المسألة » : convoquer ses représentations, les éprouver, penser avec puis **contre** elles, les mettre en crise, en percevoir les points faibles, se préparer à les réviser — puis convertir ses réflexions en **questions** ordonnées logiquement, distinguer les niveaux, les ramasser en problèmes philosophiques, en percevoir l'enjeu |
| 2   | **سندات التفكير في المسألة**         | « أواصل التفكير في المسألة » : appareil de lecture d'un texte de philosophe — **عنوان** (oriente vers l'objet du texte), **تمهيد** (situe le niveau de traitement, la spécificité problématique de l'espace, la place du support dans la question générale), **نصّ لأحد الفلاسفة** (le philosophe y expose son point de vue propre sur le problème général), **تعريف بالكاتب** (situer l'approche dans un moment de l'histoire de la philosophie et le contexte intellectuel), **هوامش** (élucider les expressions obscures, identifier les noms et lieux cités), **مهامّ** |
| 3   | **دعائم للتفكير في المسألة**         | تحديدات وتمييزات مفهوميّة (définitions et distinctions conceptuelles) + سياقات فكريّة (les courants dans lesquels les thèses se situent)                                                                                                                                                                                             |
| 4   | **كيفيّات التفكير**                  | les procédés de la pensée et de l'écriture philosophiques                                                                                                                                                                                                                                                                             |
| 5   | **نصّ مطوّل**                        | un texte long d'un philosophe, suivi dans son intégralité                                                                                                                                                                                                                                                                            |
| 6   | **مختصرات**                          | le récapitulatif de fin de مبحث                                                                                                                                                                                                                                                                                                       |

Les **مهامّ** de la fenêtre 2 sont elles-mêmes typées (p.4), et cette typologie est la clé de tout
exercice honnête sur ce programme :

- **أفكّر مع الفيلسوف** : dégager sa thèse (كشفا لأطروحته), **suivre le parcours de son
  argumentation** (وتعقّبا لمسار حجاجه), **raisonner sur les implicites et les prémisses**
  (وتعقّلا للضمنيات والمسلّمات) ;
- **أفكّر ضدّ الفيلسوف** : critique des positions et dépassement des limites de l'idée ;
- **أفكّر مع نفسي** : revoir ses propres représentations, convoquer son vécu.

## 2. Plan annuel (البرنامج — 3 محاور, 5 مباحث)

⚠️ **Ce §2 est établi à partir du فهرس الكتاب (p.404–408), lu intégralement, et des pages
d'ouverture p.6.** Il donne le **scope exact et les plages de pages** de chaque مبحث, mais **pas**
le contenu enseigné (thèses, définitions, encadrés) : celui-ci demande la lecture des pages
elles-mêmes et **n'est pas transcrit** dans ce palier. Voir §6.

### محور 1 : الإنساني بين الكثرة والوحدة — p.6

Ouverture p.6 : illustration (masques de théâtre), encadré d'un texte d'**إمنوال كانط** sous le
titre « ما التوجّه في التفكير؟ », et la liste des concepts du محور imprimée en marge :
**التّاريخ · الجسد · الذات · اللاّوعي · الوعي**.

#### مبحث 1.1 : الآنيّة والغيريّة — p.6–114

- **Structure (فهرس, p.404–405)** :
  - `1.1.1` نافذة مدخل إلى التفكير في المسألة — p.7
    - وضعيّة استكشافيّة أولى : نص **غرامشي** — p.8
    - وضعيّة استكشافيّة ثانية : نص **إبيكتاتس** — p.10
    - وضعيّة استكشافيّة ثالثة : نص **باسكال** — p.12
    - الأبعاد الإشكاليّة للمسألة — p.14
  - `1.1.2` نافذة سندات التفكير في المسألة — p.15–74 — **29 سندات**
  - `1.1.3` نافذة دعائم للتفكير في المسألة — p.75
    - `1.1.3.1` تحديدات وتمييزات مفهوميّة — p.76 : **التأويل** p.76 · **الزّمان** p.79 · **الجوهر** p.81
    - `1.1.3.2` سياقات فكريّة — p.83 : **التحليل النفسي** p.83 · **الفينومينولوجيا** p.87 · **الوجوديّة** p.91 · **فلسفة التاريخ** p.94
    - `1.1.3.3` بحث وتحقيق : **فلاسفة الظنّة** — p.98
  - `1.1.4` نافذة كيفيّات التفكير — p.100
  - `1.1.5` نافذة نصّ مطوّل — **ديكارت** : *التأمّلات الميتافيزيقيّة*, التأمّل الثاني — p.104
  - `1.1.6` مختصرات — p.113
- **Inventaire des 29 سندات** (n° — auteur — titre — page ; du فهرس p.404–405) :

  | #   | المؤلّف       | عنوان السّند           | ص.  |
  | --- | ------------- | ---------------------- | --- |
  | 1   | فورباخ        | الوعي ميزة إنسانيّة    | 16  |
  | 2   | ابن طفيل      | الذات النفس            | 18  |
  | 3   | ابن سينا      | في إثبات الآنية        | 20  |
  | 4   | ديكارت        | في يقين الكوجيتو       | 22  |
  | 5   | هيغل          | تحقّق الوعي            | 24  |
  | 6   | روسّو         | التوق إلى الاكتمال     | 26  |
  | 7   | شوبنهاور      | التاريخ ذاكرة الوعي    | 28  |
  | 8   | برغسون        | الوعي والديمومة        | 30  |
  | 9   | أفلاطون       | الجسد الوضيع           | 32  |
  | 10  | مالبرونش      | الجسم امتداد           | 34  |
  | 11  | سبينوزا       | في وحدة النفس والجسد   | 36  |
  | 12  | هيغل          | الجسد تجسيد للحريّة    | 38  |
  | 13  | موران         | مركزيّة الذات          | 40  |
  | 14  | مرلوبونتي     | تجربة الجسد            | 42  |
  | 15  | ليفيناس       | الجسد إحساس بالهويّة   | 44  |
  | 16  | سارتر         | تجربة الخجل            | 46  |
  | 17  | هيوم          | هل الأنا وهم؟          | 48  |
  | 18  | ماركس وانغلز  | هل الوعي كيان مستقل؟   | 50  |
  | 19  | نيتشه         | الوعي نتاج التواصل     | 53  |
  | 20  | ألتوسير       | الاعتراف الإيديولوجي   | 55  |
  | 21  | فوكو          | الجسد في لعبة السلطة   | 57  |
  | 22  | بودريار       | استثمار الجسد          | 59  |
  | 23  | فوكو          | مساءلة الكوجيتو        | 61  |
  | 24  | فرويد         | بنية الجهاز النفسي     | 63  |
  | 25  | فرويد         | سيادة الأنا؟           | 65  |
  | 26  | دولوز         | الآخر بما هو بنية      | 67  |
  | 27  | لاكون         | في اللاّوعي            | 69  |
  | 28  | مرلوبونتي     | منزلة اللاّوعي         | 72  |
  | 29  | سارتر         | الإنسان مشروع          | 73  |

- **Bornes de scope** :
  - ✅ INCLUS : الوعي · اللاّوعي · الذات · الجسد · التّاريخ ; التأويل, الزّمان, الجوهر ; psychanalyse, phénoménologie, existentialisme, philosophie de l'histoire ; les « philosophes du soupçon » (فلاسفة الظنّة).
  - ⛔ EXCLU : tout ce que le manuel de **شعبة الآداب** (`210422`/`210423`) ajoute et que celui-ci ne porte pas — ce manuel-ci est le programme **des sections non-Lettres**, et il est le seul scope de cette fiche.

#### مبحث 1.2 : الخصوصيّة والكونيّة — p.115–214

- **Structure (فهرس, p.405–406)** :
  - `1.2.1` نافذة مدخل إلى التفكير في المسألة — p.116
    - وضعيّة استكشافيّة أولى : نص **محمد ه** [?] — p.117 (nom tronqué au فهرس, voir §6)
    - وضعيّة استكشافيّة ثانية : مقطع من شريط « **مغامرات الحاخام يعقوب** » — p.119
    - وضعيّة استكشافيّة ثالثة : نص **مونتانيو** — p.121
    - الأبعاد الإشكاليّة للمسألة — p.122
  - `1.2.2` نافذة سندات التفكير في المسألة — p.123–176 — **28 سندات**
  - `1.2.3` نافذة دعائم للتفكير في المسألة — p.177
    - `1.2.3.1` تحديدات وتمييزات مفهوميّة — p.178 : **الثقافة – الحضارة** p.178 · **العولمة** · **التمثّلات**
    - `1.2.3.2` سياقات فكريّة — p.189 : **الأنثروبولوجيا** p.189 · **الاستشراق** p.195
  - `1.2.4` نافذة كيفيّات التفكير — p.197
  - `1.2.5` نافذة نصّ مطوّل — **بول ريكور** : *التاريخ والحقيقة*, الفصل الثاني — الجزء الثالث — p.201
  - `1.2.6` مختصرات — p.214
- **Inventaire des 28 سندات** (فهرس p.405–406) :

  | #   | المؤلّف   | عنوان السّند              | ص.  |
  | --- | --------- | ------------------------- | --- |
  | 1   | تايلور    | مساءلة الهويّة            | 124 |
  | 2   | موران     | الهويّة المركّبة          | 126 |
  | 3   | مالبرونش  | العقل الكوني              | 127 |
  | 4   | كانط      | الأرض وطن للجميع          | 128 |
  | 5   | موران     | في الاندماج               | 130 |
  | 6   | أ. كونت   | العيش من أجل الآخرين      | 131 |
  | 7   | شتراوس    | تقريظ الاختلاف            | 134 |
  | 8   | تودوروف   | التسامح                   | 136 |
  | 9   | مونتانيو  | الهمجيّة                  | 138 |
  | 10  | التوحيدي  | في المفاضلة بين الأمم     | 140 |
  | 11  | غوستورف   | الثقافة ماهيّة الحضارة    | 142 |
  | 12  | دو براي   | وظيفة الصّورة             | 144 |
  | 13  | الطهطاوي  | صورة الإفرنج              | 146 |
  | 14  | دو بوفوار | صورة المرأة               | 148 |
  | 15  | هيغل      | بين الشرق والغرب          | 150 |
  | 16  | ابن خلدون | الاقتداء بالغالب          | 152 |
  | 17  | غادامار   | اللغة ومطلب التّفاهم      | 154 |
  | 18  | غاندي     | الحوار إقصاء للعنف        | 156 |
  | 19  | نيتشه     | حدود التّواصل             | 158 |
  | 20  | دوركايم   | المقدّس الدّيني           | 159 |
  | 21  | ريكور     | صورة المقدّس              | 161 |
  | 22  | فرويد     | ما وراء المثل الأعلى      | 163 |
  | 23  | جيمس      | تعدّد الملل والنّحل       | 165 |
  | 24  | فولتير    | داء التعصّب               | 167 |
  | 25  | هنتنجتون  | الحضارة العالميّة         | 169 |
  | 26  | هنتنجتون  | السّياسي والثّقافي        | 171 |
  | 27  | أدونيس    | أزمة هويّة                | 173 |
  | 28  | بودريار   | العالمي والكوني           | 175 |

- **Bornes de scope** :
  - ✅ INCLUS : الهويّة · الاختلاف · التسامح · الثقافة/الحضارة · العولمة · التمثّلات · الصّورة · المقدّس · التعصّب ; anthropologie, orientalisme.
  - ⛔ EXCLU : idem 1.1 — le programme de شعبة الآداب.

### محور 2 : العلم بين الحقيقة والنمذجة — p.215–270

Ce محور ne comporte **qu'un seul مبحث**, qui porte son nom.

#### مبحث 2 : العلم بين الحقيقة والنمذجة — p.215–270

- **Structure (فهرس, p.406–407)** :
  - `2.1` نافذة مدخل للتفكير في المسألة — p.216
    - وضعيّة استكشافيّة — p.217
    - الأبعاد الإشكاليّة للمسألة — p.219
  - `2.2` نافذة سندات للتفكير في المسألة — p.220–250 — **16 سندات**
  - `2.3` نافذة دعائم للتفكير في المسألة — p.251
    - `2.3.1` تحديدات وتمييزات مفهوميّة — p.252 : **الواقع** p.252 · **البراديغم** p.254
    - `2.3.2` سياقات فكريّة — p.256 : **السيبارنيتيقا** p.256 · **الإبستيمولوجيا البنائيّة** p.257
  - `2.4` نافذة كيفيّات التفكير — p.260
  - `2.5` نافذة نصّ مطوّل — **كارل بوبير** : *أسطورة الإطار*, الفصل الثامن — p.264
  - `2.6` مختصرات — p.270
- **Inventaire des 16 سندات** (فهرس p.406) :

  | #   | المؤلّف     | عنوان السّند                                          | ص.  |
  | --- | ----------- | ----------------------------------------------------- | --- |
  | 1   | مولود       | في أصل النّماذج                                       | 221 |
  | 2   | تنّودجي     | النّموذج واستكشاف الظّواهر                            | 223 |
  | 3   | كارناب      | في الفرق بين النّموذج الرّياضي والنّموذج الفيزيائي    | 225 |
  | 4   | سيمون       | النمذجة والأنساق الرمزيّة                             | 227 |
  | 5   | بياجيه      | النّموذج والبنية                                      | 229 |
  | 6   | لودفيغ باسكال | النّموذج بناء خيالي                                 | 231 |
  | 7   | لوموانيو    | قيمة النمذجة                                          | 233 |
  | 8   | نوفال       | النّموذج تبسيط                                        | 235 |
  | 9   | فرويندتال   | كيف ينشأ النّموذج؟                                    | 237 |
  | 10  | لوموانيو    | النمذجة للفهم                                         | 238 |
  | 11  | توم         | شروط صلاحيّة النّموذج                                 | 240 |
  | 12  | لادريار     | النّشاط العلمي والنّشاط التقني                        | 242 |
  | 13  | فرودنتال    | النمذجة إجراء منهجي                                   | 244 |
  | 14  | لوموانيو    | النمذجة وسؤال المعنى                                  | 245 |
  | 15  | دوهام       | حدود النموذج الميكانيكي                               | 247 |
  | 16  | بلانشي      | قيمة النّماذج                                         | 249 |

- **Bornes de scope** :
  - ✅ INCLUS : الحقيقة · النمذجة · النّموذج · الواقع · البراديغم · البنية ; cybernétique, épistémologie constructiviste ; le rapport activité scientifique / activité technique.
  - ⛔ EXCLU : idem — le programme de شعبة الآداب.

### محور 3 : القيم بين النسبي والمطلق — p.271–402

#### مبحث 3.1 : الدولة — السيادة والمواطنة — p.271–346

- **Structure (فهرس, p.407–408)** :
  - `3.1.1` نافذة مدخل إلى التفكير في المسألة — p.272
    - وضعيّة استكشافيّة أولى : نص **ابن المقفّع** — p.273
    - وضعيّة استكشافيّة ثانية : **الإعلان العالمي لحقوق الإنسان** — p.275
    - الأبعاد الإشكاليّة للمسألة — p.277
  - `3.1.2` نافذة سندات التفكير في المسألة — p.278–318 — **22 سندات**
  - `3.1.3` نافذة دعائم للتفكير في المسألة — p.319
    - `3.1.3.1` تحديدات وتمييزات مفهوميّة — p.320 : **السّياسة** p.320 · **اللائكيّة** p.322 · **الكليانيّة** p.324
    - `3.1.3.2` سياقات فكريّة — p.327 : **الليبراليّة** p.327 · **الفوضويّة** p.330
    - **فلسفة العقد الاجتماعي** — p.332
  - `3.1.4` نافذة كيفيّات التفكير — p.335
  - `3.1.5` نافذة نصّ مطوّل — **سبينوزا** : *كتاب السّياسة*, الفصل الثّالث — p.339
  - `3.1.6` مختصرات — p.346
- **Inventaire des 22 سندات** (فهرس p.407) :

  | #   | المؤلّف     | عنوان السّند                  | ص.  |
  | --- | ----------- | ----------------------------- | --- |
  | 1   | شميت        | في السياسي                    | 279 |
  | 2   | فوكو        | حدّ السلطة                    | 281 |
  | 3   | ريكور       | التّفكير في السّلطة           | 282 |
  | 4   | ابن خلدون   | العصبيّة والملك               | 284 |
  | 5   | هيوم        | الحاجة إلى الدّولة            | 285 |
  | 6   | باكونين     | في الدّولة                    | 287 |
  | 7   | نيتشه       | حدّث زرادشت عن الدّولة قال…   | 289 |
  | 8   | الفارابي    | مراتب الرئاسة                 | 291 |
  | 9   | الكواكبي    | الرّاعي والرعيّة              | 293 |
  | 10  | كونستون     | في الدّيمقراطيّة              | 295 |
  | 11  | تودوروف     | الدّولة والشرعيّة             | 297 |
  | 12  | سبينوزا     | الحقّ والقانون                | 299 |
  | 13  | ستيوارت ميل | حريّة الرّأي                  | 301 |
  | 14  | ميشو        | الحق والعنف                   | 303 |
  | 15  | ماركس       | في نقد الحقّ                  | 305 |
  | 16  | أرسطو       | العدالة والإنصاف              | 307 |
  | 17  | أفلاطون     | العدالة والقانون              | 309 |
  | 18  | باسكال      | العدل والقوّة                 | 311 |
  | 19  | راولس       | العدل أساس الطاعة             | 312 |
  | 20  | إيبكتاتس    | المواطن العالمي               | 314 |
  | 21  | تاسّان      | مواطن العالم المشترك          | 315 |
  | 22  | كاستلاس     | المواطن العالمي الجديد        | 317 |

- **Bornes de scope** :
  - ✅ INCLUS : الدّولة · السّيادة · المواطنة · السّلطة · الحقّ · القانون · العدالة · الشرعيّة · الدّيمقراطيّة ; السّياسة, اللائكيّة, الكليانيّة ; libéralisme, anarchisme, philosophie du contrat social.
  - ⛔ EXCLU : idem — le programme de شعبة الآداب.

#### مبحث 3.2 : الأخلاق — الخير والسّعادة — p.347–402

- **Structure (فهرس, p.408)** :
  - `3.2.1` نافذة مدخل إلى التفكير في المسألة — p.348
    - وضعيّة استكشافيّة أولى : نص **ابن حزم** — p.349
    - وضعيّة استكشافيّة ثانية : نص **مسراهي** — p.350
    - الأبعاد الإشكاليّة للمسألة — p.351
  - `3.2.2` نافذة سندات التفكير في المسألة — p.352–381 — **18 سندات**
  - `3.2.3` نافذة دعائم للتفكير في المسألة — p.382
    - `3.2.3.1` تحديدات وتمييزات مفهوميّة — p.383 : **الآداب** p.383 · **الإيتيقا** p.385
    - `3.2.3.2` سياقات فكريّة — p.389 : **العدميّة** p.389 · **النفعيّة** p.391
    - `3.2.3.3` نافذة كيفيّات التفكير — p.393
  - `3.2.4` نافذة نصّ مطوّل — **نيتشه** : *أفول الأصنام*, « الأخلاق فضيلة مضادّة » — p.397
  - `3.2.5` مختصرات — p.402
- **Inventaire des 18 سندات** (فهرس p.408) :

  | #   | المؤلّف     | عنوان السّند                | ص.  |
  | --- | ----------- | --------------------------- | --- |
  | 1   | أرسطو       | حدّ الفضيلة                 | 353 |
  | 2   | ابن مسكويه  | ما الخير؟                   | 354 |
  | 3   | سبينوزا     | الفاضل                      | 356 |
  | 4   | ستيوارت ميل | المنفعة أساس الأخلاق        | 358 |
  | 5   | كانط        | الإنسان غاية                | 360 |
  | 6   | كيركغارد    | ما الواجب ؟                 | 362 |
  | 7   | كانط        | الأمر الأخلاقي              | 364 |
  | 8   | دوركايم     | في نقد الواجب               | 366 |
  | 9   | نيتشه       | أخلاق القوّة                | 367 |
  | 10  | ماركس       | الأخلاق والمجتمع            | 369 |
  | 11  | برغسون      | الحريّة الأخلاقيّة          | 370 |
  | 12  | أبيقور      | اللذة والسّعادة             | 371 |
  | 13  | أرسطو       | الخير الأسمى                | 372 |
  | 14  | روسّو       | سبيل السّعادة               | 373 |
  | 15  | دو أولباخ   | في مدح التقدّم والرّفاه     | 374 |
  | 16  | فرويد       | حدود السّعادة               | 376 |
  | 17  | بودريار     | في السّعادة الجديدة         | 378 |
  | 18  | مسراهي      | الحريّة السّعيدة            | 380 |

- **Bornes de scope** :
  - ✅ INCLUS : الأخلاق · الخير · السّعادة · الفضيلة · الواجب · المنفعة · اللذة · الحريّة الأخلاقيّة ; الآداب vs الإيتيقا ; nihilisme, utilitarisme.
  - ⛔ EXCLU : idem — le programme de شعبة الآداب.

## 3. Notes pédagogiques / méthode

**Ce que le manuel impose à toute génération de contenu**, tel qu'imprimé p.4–5 :

- La démarche est **problématisante**, pas doctrinale : chaque مبحث part de représentations
  spontanées, les met en crise, les convertit en **questions ordonnées**, puis en **problème
  philosophique**. Le manuel dit explicitement viser à libérer l'élève « des moules des opinions
  courantes et de l'emprise des jugements hâtifs » (p.4).
- Les **مهامّ** typent trois postures distinctes — *avec* le philosophe (thèse, parcours
  argumentatif, implicites et prémisses), *contre* le philosophe (critique, limites), *avec
  soi-même* (révision de ses représentations). Ce sont **trois opérations vérifiables**, et elles
  sont la matière légitime d'un exercice.
- L'appareil de chaque سند (**عنوان · تمهيد · نصّ · تعريف بالكاتب · هوامش · مهامّ**) désigne
  précisément ce qui est **restituable** : l'objet du texte, le niveau de traitement, la thèse du
  philosophe, son moment dans l'histoire de la philosophie, les termes élucidés.

> ⚠️ **Conséquence directe pour le LOT B — à lire avant d'écrire la moindre question.** Une
> dissertation ne se met pas en QCM, et un QCM qui note une **opinion** est un défaut de fond
> qu'aucun gate ne voit. Sur ce programme, ce qui se teste honnêtement est **exactement** ce que le
> manuel objective : la **restitution d'une thèse et de son auteur** (les 113 سندات sont faits pour
> ça), la **structure d'un argument** (prémisse / conclusion / implicite — c'est « أفكّر مع
> الفيلسوف » verbatim), la **distinction conceptuelle** que le manuel définit lui-même en نافذة
> دعائم (الثقافة/الحضارة, الآداب/الإيتيقا, الواقع/النموذج, السّياسة/اللائكيّة/الكليانيّة…), et le
> **repérage d'un sophisme ou d'un implicite**. Ce qui ne se teste **jamais** : « la bonne position
> sur X ». Le format `vrai/faux motivé` et les missions interactives (appariement thèse↔auteur,
> remise en ordre d'un argument) sont les mieux adaptés. Un chapitre qui se réduirait à un atelier
> de dissertation se marque `optional: true` au manifeste plutôt que d'être forcé.

## 4. Chapitrage retenu (→ alimente `manifest/bac-*.json`)

Cinq chapitres = les cinq **مباحث** du programme. Les plages de pages sont dérivées du فهرس
(p.404–408) et bornées par le مبحث suivant.

| #   | slug                            | notion (المبحث)                                 | manuel élève (code · pages) |
| --- | ------------------------------- | ----------------------------------------------- | --------------------------- |
| 1   | `01-aniyya-ghayriyya`           | المحور 1 — الآنيّة والغيريّة                    | `210402` · p.6–114          |
| 2   | `02-khususiyya-kawniyya`        | المحور 1 — الخصوصيّة والكونيّة                  | `210402` · p.115–214        |
| 3   | `03-ilm-haqiqa-namdhaja`        | المحور 2 — العلم بين الحقيقة والنمذجة           | `210402` · p.215–270        |
| 4   | `04-dawla-siyada-muwatana`      | المحور 3 — الدّولة : السّيادة والمواطنة         | `210402` · p.271–346        |
| 5   | `05-akhlaq-khayr-saada`         | المحور 3 — الأخلاق : الخير والسّعادة            | `210402` · p.347–402        |

> Le manifeste est **répliqué à l'identique dans les cinq `manifest/bac-*.json`** (un par section
> desservie) : c'est le même manuel, le même programme, les mêmes 5 chapitres. Le contenu est
> mutualisé par `compileTo` depuis l'unique dossier `content/philosophie-bac/` (étude 16 D-4), sans
> retranscription ni duplication.

## 5. Sources croisées

- **Guide enseignant** : **aucun** au corpus CNP pour ce couple. Le manuel élève **fait donc
  référence** (profil `ecole-secondaire`) — signalé ici comme la méthode l'exige.
- **Manuel élève** : `210402` — « كتاب الفلسفة … الشّعب العلميّة », 408 p. (source de scope **et**
  de contenu ; pages par chapitre en §4).
- **Codes sœurs non rattachés** : `210422` + `210423` — « فلسفة ج1/ج2_شعبة الآداب ». **Hors scope
  de cette fiche** (voir §0) ; ils demandent leur propre LOT A sur `bac-lettres`.
- **Taybah** : aucune entrée pour la philosophie du bac.
- **Divergences signalées** : aucune à ce palier (une seule source, pas de guide à confronter).

## 6. Incertitudes / à revérifier

- ⚠️ **PROFONDEUR RÉELLE DE CE PALIER — first-pass, ossature seule.** Ce qui est transcrit ici a
  été **lu sur les pages** : la page de titre et son verso (p.1–2), le التقديم (p.3), la خارطة
  الكتاب (p.4–5), l'ouverture du محور 1 (p.6) et le **فهرس intégral** (p.404–408). Le §2 et le §4
  en dérivent : ils donnent le **scope, la structure et les plages de pages** exacts, ainsi que
  l'inventaire nominatif des **113 سندات** (auteur + titre + page).
  **Ce qui n'est PAS transcrit** : le contenu enseigné des p.7–402 — les thèses des سندات, les
  encadrés de تحديدات وتمييزات مفهوميّة, les سياقات فكريّة, les كيفيّات التفكير, les نصوص مطوّلة,
  les مختصرات et les وضعيّات استكشافيّة. **Aucun chapitre n'atteint la profondeur de génération
  (R-5)** ⇒ `chapitresGeneration: []` au registre, et **le LOT B est interdit** sur les cinq
  chapitres tant que ces pages ne sont pas lues.
- **Motif de l'arrêt** : limite d'usage de session atteinte (2026-08-04), qui a tué les deux
  sous-agents de transcription avant leur première écriture. Arrêt propre au dernier palier
  poussable (méthode, T-9/T-10) plutôt que fiche bâclée.
- **Reprise** : les 408 pages sont déjà **rendues en PNG 150 dpi** (offset 0, `p-NNN.png` = page
  imprimée NNN) — la reprise n'a pas à re-rendre. Ordre de reprise conseillé : le مبحث 2 (p.215–270,
  56 p., le plus court et le plus autonome), puis 3.2 (p.347–402, 56 p.), puis 3.1 (p.271–346),
  puis 1.2 (p.115–214), puis 1.1 (p.6–114). **Ne pas relire** p.1–6 ni p.404–408 (T-2/R-4).
- `[?]` p.117 : le فهرس annonce « وضعيّة استكشافيّة أولى : نص **محمد ه** » — nom visiblement
  **tronqué dans le sommaire lui-même**. À lire sur la page 117 pour rétablir l'auteur.
- `[?]` p.4 : le bandeau latéral de la خارطة الكتاب est imprimé **en rotation** ; la série de termes
  relevée (مفاهيم — بنية — تقنيات — تمشّيات — سياقات — تأليف — مقالات — منهجيّة) est lisible mais à
  reconfirmer à 300 dpi.
- Le فهرس ne donne **pas** de page pour deux entrées de 1.2.3.1 (**العولمة**, **التمثّلات**) : leurs
  pages sont à relever sur p.178–188.
- **Translittération des noms** : les auteurs sont transcrits **tels qu'imprimés en arabe** dans les
  inventaires §2. L'équivalent latin (Feuerbach, Ibn Tufayl, Malebranche, Le Moigne, Lévinas…) n'est
  **pas** donné par le فهرس ; ne pas l'inventer dans le contenu sans l'avoir lu dans un تعريف
  بالكاتب du manuel.
- **R-7 non faite** (la fiche n'atteint pas la profondeur de génération) ⇒ `r7: null` au registre.
