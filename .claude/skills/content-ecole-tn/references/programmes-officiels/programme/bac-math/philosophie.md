# الفلسفة / Philosophie — Baccalauréat (الشّعب العلميّة) · programme officiel CNP

> **Sources** (une seule — voir §5) :
>
> - **Guide enseignant** (programme) : **non disponible au corpus CNP**. Aucun guide n'existe pour
>   ce couple ⇒ **le manuel élève fait référence** (profil `ecole-secondaire`).
> - **Manuel élève** (contenu/exemples/exercices) : `210402P00.pdf`
>   (`cnp-officiel/manuels/secondaire/c4/eleve/`) — « كتاب الفلسفة — لتلاميذ السّنة الرّابعة من
>   التّعليم الثانوي — الشّعب العلميّة ». **408 pages** (page PDF = page imprimée, **offset 0**).
>   **Pages lues** : p.1–6 (page de titre, copyright, التقديم, خارطة الكتاب, ouverture du محور 1),
>   **p.215–226** (ouverture du مبحث 2 + نافذة مدخل complète + سندات 1–3 — **en profondeur**),
>   p.404–408 (فهرس الكتاب intégral).
>   **Transcrit le** : 2026-08-04. **Statut** : ⚠️ **first-pass — ossature + une amorce de
>   profondeur sur le seul مبحث 2 (p.215–226)** (voir §6).
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

#### مبحث 2 — transcription en PROFONDEUR (partielle : p.215–226 seulement)

> ⚠️ **Portée réelle de ce bloc : p.215–226**, soit la page d'ouverture, la نافذة مدخل complète
> et les **3 premiers سندات sur 16**. Les p.227–270 (سندات 4–16, la نافذة دعائم et ses
> تحديدات/سياقات, la نافذة كيفيّات التفكير, le نصّ مطوّل de بوبير et les مختصرات) ne sont
> **PAS** transcrites. Ce chapitre n'atteint donc **pas** la profondeur de génération : il reste
> hors de `chapitresGeneration` (R-5). **Source** : manuel élève `210402`
> (كتاب الفلسفة — السّنة الرّابعة من التّعليم الثانوي — الشّعب العلميّة, CNP).
> Ce مبحث constitue à lui seul le **محور 2** du manuel : il est autonome.

---

##### Page d'ouverture du مبحث — p.215

Titre imprimé en bandeau : **العلم بين الحقيقة والنمذجة**.

Mention manuscrite (en rose, bas de page) : « تمّ إنجاز هذه المسألة بالتعاون مع لجنة تأليف كتاب
الرابعة آداب ».

**Encadré de citation** (verbatim) :

> « إنّ جعل التمثّل هندسيّا أي رسم الظواهر والترتيب المتسلسل للأحداث الحاسمة في تجربة ما، هما
> المهمّة الأولى في توكيد العقل العلمي ».
> — **باشلار، تكوين العقل العلمي**

**Le plan du مبحث, tel qu'il est imprimé sous forme de deux organigrammes** (c'est la carte
conceptuelle officielle de la question — verbatim) :

**1 — أبعاد النمذجة**

| البعد | مكوّناته تِباعا كما هي مطبوعة |
| --- | --- |
| **البعد التركيبي** | الأكسمة — البنية — التريّض — الصورنة |
| **البعد الدلالي** | الافتراضي — الملائم — الواقعي — القانون — النظريّة |
| **البعد التداولي** | التفسير — التحقّق — الفهم — النجاعة |

**2 — النمذجة ومطلب الحقيقة**

| الحدود | مكوّناتها كما هي مطبوعة |
| --- | --- |
| **الحدود الابستيمولوجيّة** | الاختزاليّة — التاريخيّة — الأنظمة التقنيّة |
| **الحدود الفلسفيّة** | الحقيقة — المسؤولية — المعنى |

Illustration : composition en couleurs — polyèdres géométriques (icosaèdre, cube filaire,
tétraèdres) suspendus sur des orbites elliptiques autour d'un soleil, sur fond rouge et noir.

---

##### 2.1 نافذة مدخل إلى التفكير في المسألة — p.216–219

###### Page de titre de la نافذة — p.216

Deux illustrations : (a) une silhouette de tête d'homme sur fond bleu portant un grand **point
d'interrogation** ; (b) une image colorée d'un tableau noir portant la formule
`α = (√5 − 1) / 2`.

**Encadré de citation** (verbatim) :

> " إذا قام مؤرّخ العلوم بتفحّص وثائق ماضي البحث من وجهة النظر التأريخيّة المعاصرة، فإنّه
> سيُغْرى لربّما بكتابة أنّه عندما تتغيّر البراديغمات فإنّ العالم نفسه سيتغيّر معها ".
> — ▲ **توماس س. كوهن، بنية الثورات العلميّة**

###### 1 — وضعية استكشاف — p.217

C'est une **fiche de travail à remplir par l'élève** (cases vides, pointillés). Support :
la **comparaison de deux théories astronomiques**, celle de **بطلميوس** (Ptolémée) et celle de
**نيوتن** (Newton). Consignes imprimées :

- **1.1 — أبحث ... وأحدّد** : deux cadres à remplir — « أهمّ خصائص نظريّة بطلميوس الفلكيّة » /
  « أهمّ خصائص نظريّة نيوتن الفلكيّة ».
- **2.1 — أرسم..** : deux cadres de dessin — « صورة الكون وموقع الأرض في نظريّة بطلميوس. » /
  « صورة الكون وموقع الأرض في نظريّة نيوتن ».
- **3.1 — أستخلص ما يجمع بين النظريّتين وما يميّز بينهما** : un cadre « ما يجمع بينهما : » et un
  cadre « ما يميّز بينهما: » à double colonne (بطلميوس / نيوتن).
- **4.1 — ماذا أستنتج في خصوص طبيعة الاختلاف بين النظريّتين؟**

###### 1.2 — أتابع التفكير : أقرأ النص قراءة متأنّية وأفكّر في مضمونه … — p.218

**Texte support** — **فيرنر هيزنبرغ**, *الجزء والكل: محاورات في مضمار الفيزياء الذرّيّة*,
ترجمة وتحقيق محمد أسعد عبد الرؤوف، الهيئة المصريّة العامة للكتاب، 1986، ص 51—52.

Forme : un fragment de dialogue, la parole étant donnée à **أوتو**. **Thèse** : la différence
entre l'astronomie ptoléméenne et l'astronomie newtonienne n'est pas jugée « essentielle » par
le locuteur ; l'astronomie de Ptolémée fut une bonne science (quinze siècles d'enseignement),
et Newton n'a pas apporté quelque chose de plus fondamental — il a seulement donné
« un autre **تمثيلا رياضيّا** » du mouvement des planètes, représentation que les siècles ont
prouvée la plus **réussie** (نجاحا).

**الكاتب — فيرنر هيزنبرغ** `Werner Karl HEISENBERG` (notice biographique imprimée, verbatim
resserré) : وُلد في 5 ديسمبر 1901 بفورتسبورغ بألمانيا. درس الفيزياء في مونيخ وغوتنغين. حصل في
1924—1925 على منحة روكفلر وعمل لدى نيلز بوهر في كوبنهاغن. أصبح أستاذا بجامعة لايبزيك سنة 1927.
حصل على جائزة نوبل للفيزياء سنة 1932. تولّى رئاسة معهد القيصر فيلهلم للفيزياء سنة 1941. قام سنة
1936 بإنشاء معهد ماكس بلانك للفيزياء في غوتنغين ثمّ انتقل به إلى مونيخ سنة 1957 حيث توفي في
1 فيفري 1976.

**الهوامش** (verbatim resserré) :

1. **أوتو** : فيزيائي وصديق هيزنبرغ. شاركه في أكثر من حوار في كتاب "الجزء والكل".
2. **بطلميوس** `Ptolémée` (90—168)، عالم فلك يوناني من المدرسة الإسكندرانيّة، من أشهر مؤلّفاته
   "الماجسطي" الذي وضع فيه مبادئ علم الفلك القديم القائم على فكرة **مركزيّة الأرض**
   `géocentrisme`، وهي الفكرة التي سيقوّضها بعد ذلك **كوبرنيك** `Copernic` (1473—1543) صاحب كتاب
   "في دوران الأجرام السماويّة" الذي أحدث ثورة تسمّى بعد ذلك **بالثورة الكوبرنيكيّة**.
3. **نيوتن** `Newton` (1642—1727)، عالم إنجليزي في الرياضيات والفيزياء وواضع **قانون الجاذبيّة**.
   من أهم مؤلّفاته "المبادئ الرياضيّة للفلسفة الطبيعيّة" (1687).

**2.2 — أنجز المهام التالية** (les 7 consignes imprimées, verbatim) :

- ما طبيعة الاختلاف بين نظريّة بطلميوس ونظريّة نيوتن حسب الكاتب؟ هل يتّفق مع استخلاصي السابق؟
- لِمَ اعتبر الكاتب علم بطلميوس علما جيّدا جدّا ؟
- بِمَ تميّزت نظريّة نيوتن في رأي الكاتب ؟
- ما دلالة ((التمثيل الرّياضي)) وما قيمته العلميّة ؟
- أبحث في دلالة ((النمذجة)) وأتساءل عن علاقتها بـ((التمثيل الرياضي)).
- ما دلالة ((النجاح)) الذي يتحدّث عنه الكاتب ؟
- أفكّر في العلاقات الممكنة بين (( النجاح )) و(( الحقيقة )) وأستخلص الاحراجات النظريّة التي يمكن
  أن تترتّب عليها.

Illustration : portrait peint de **نيوتن**.

###### 2 — الأبعاد الإشكاليّة للمسألة — p.219

⚠️ Cette page **n'imprime pas** une liste de dimensions problématiques rédigées : c'est une
**page de méthode + espace de travail vierge**. Ce qui est imprimé, verbatim :

> **أستحضر مكاسبي…**
> وأحوّل الاحراجات النظريّة التي انتهيت إليها إلى أسئلة تساعدني على التقدّم في معالجة المسألة.
> وأحدّد الرهانات النظريّة والعمليّة التي تدعو إلى التفكير في المسألة.

**التمشيات** (organigramme, deux étapes, verbatim) :

1. أطرح الأسئلة كــمــا تــرد في ذهني
2. أعيد النظر في الأسئلة: أنظّمها وأقوم بصياغتها في مشكلات فلسفية

Le grand cadre à gauche de l'organigramme est **vide** (à remplir par l'élève).

---

##### 2.2 نافذة سندات للتفكير في المسألة — p.220–250

###### Page de titre de la نافذة — p.220

Deux illustrations : (a) une table d'alchimiste/savant ancien (livre ouvert, bougie, alambic,
manuscrit) ; (b) un champignon atomique.

Deux **encadrés de citation** (verbatim) :

> " إنّ كلّ قيمة تقسّم الذات المقيّمة. فهي تعطي الذات، على الأقل، تاريخ تقييمها، ويكون إذاك
> للذات ماض من اللاقيمة تقتضي معارضته مع حاضر من القيمة ".
> — ▲ **غاستون باشلار، العقلانيّة المطبّقة**

> " إذا كنت تـفـرّق هكـذا بين الاكتـشـاف والاختراع، فأين تضع إذن هذه النتيجة المفزعة للتقدّم
> التكنلوجي [sic]، أعني القنبلة الذريّة؟ ".
> — **هيزنبرغ**

###### Tableau récapitulatif des 16 سندات

> **Convention de la نافذة** : chaque سند occupe une double page — une page de **texte** précédée
> d'un **تمهيد** (chapeau problématisant, imprimé en rose), puis une page (ou une demi-page) de
> **الهوامش** / **الكاتب** / **المهام**.

| # | المؤلّف (كما هو مطبوع) | عنوان السّند | ص. | الأطروحة (مُعاد صياغتها) | المفاهيم |
| --- | --- | --- | --- | --- | --- |
| 1 | **نوال مولود** `Noël MOULOUD` — *الموسوعة العالميّة* (`Encyclopédia Universalis`, pp 529-530) | **في أصل النماذج** | 221–222 | L'origine du mot « نموذج » est **technologique** : c'est d'abord un « تصميم », un objet **réduit** et maniable qui reproduit sous forme simplifiée les propriétés d'une chose de grandes dimensions. Ce sens n'est pas le « المثال » platonicien : le modèle renverse la situation du modèle platonicien puisqu'il est **réalisé** au lieu d'être une idée à réaliser. Dans les sciences, le modèle est un **pont entre la conception et l'expérimentation**, matériel ou abstrait, et l'économie, la sociologie et la biologie se donnent à elles-mêmes des « نماذج نظريّة » des faits qu'elles décrivent. | النموذج — التصميم — المثال (الأفلاطوني) — التحقّق — الإبستيمولوجيا — التصور والتجريب — النماذج النظريّة |
| 2 | **جيل كوهن تنّودجي** `G. Cohen TANNODJI` — *معنى النموذج في الفيزياء النظرية* (`La notion de modèle en physique théorique`, p 31, in *enquête sur le concept de modèle*, sous la direction de `Pascal Nouvel`) | **النموذج واستكشاف الظواهر** | 223–224 | Les modèles jouent, dans le développement de toute théorie physique, des **rôles distincts selon l'état d'avancement** de la théorie. Dans la phase **exploratoire**, ils sont dits « فينومينولوجية » ou « استكشافيّة » et fonctionnent comme des **وسائط استكشافيّة** transitoires — le dessin d'une théorie qui n'existe pas encore. Ils sont abandonnés puis remplacés par de plus performants à mesure que la théorie se consolide ; même stabilisée, une théorie doit être complétée par des données extérieures et des « ثوابت حرّة », ce qui montre qu'elle **garde toujours une part de modélisation**. | النموذج — الاستكشاف — النماذج الفينومينولوجيّة — الوسائط الاستكشافيّة — ثوابت حرّة — الصورنة — الإطار النظري — التوقّعات النظريّة والمعطيات التجريبيّة |
| 3 | **ر. كارناب** — *مدخل إلى فلسفة العلوم — الأسس الفلسفية للفيزياء*, ترجمة السيد نفادي، ص 183-184 | **في الفرق بين النموذج الرياضي والنموذج الفيزيائي** | 225–226 | Il ne faut pas confondre le modèle au sens de **construction visuelle spatiale** et le modèle au sens **mathématique moderne** : chez les mathématiciens, logiciens et savants, le modèle est une construction **abstraite** (une équation ou un ensemble d'équations), non un objet qu'on manipule avec des boules et des fils. C'est une **description simplifiée** — donc appauvrie — d'une structure physique, économique ou sociologique. Le modèle visuel bien construit **n'est pas une garantie** de la validité d'une théorie, et l'absence de modèle visuel n'est pas une raison de la réfuter. | النموذج الرياضي — النموذج الفيزيائي — البناءات المكانيّة البصريّة — الثابتات `paramètres` — الحدس — الوصف المبسّط — حدود النموذج |

*(les سندات 4 à 16 sont détaillés plus bas dans ce même tableau — voir la suite)*

###### Détail des سندات lus

##### سند 1 — في أصل النماذج — p.221–222

**التمهيد** (verbatim) :

> ساد اعتقاد بأنّ العمل العلمي هو مجرّد وصف للوقائع يكون بتوفّر شرط موضوعيّة النقل عبر قراءة
> للأحداث قوامها حياد الذّات. ومع ذلك، لنا أن نرتاب في اعتقاد كهذا، تهزّه تصوّرات جديدة لعمل
> العقل العلمي حين يُدرك فاعليّة لا تكتفي بالمعرفة بل تذهب إلى توفير شروط المعرفة.

**الهوامش** (verbatim resserré) :

1. **نموذج** `Paradigme` : المقصود هنا النموذج **الإرشادي** للعلم بالمعنى الذي يقدمه **توماس
   كوهن** في *بنية الثورات العلمية*. (انظر تحديدات وتمييزات مفهوميّة)
2. **نموذج بوهر** : هو النموذج أو الرّسم الذي قدّمه بوهر للذرّة والذي استعاره من نموذج المجموعة
   الشمسية حيث توجد النواة في الوسط وتدور الكهارب حولها، غير أنّه تمّ الآن التخلي عن هذا
   النموذج بعد معرفة طبيعة حركة الكهارب التي لا تدور بشكل منتظم بل تقوم بقفزات مختلفة وترسل
   موجات.

**الكاتب — نوال مولود (1921—1997)** : أستاذ بجامعة الآداب والعلوم الإنسانية بليل بفرنسا، له
عدّة مقالات بالموسوعة العالمية : الحدس، الحدسية، الحكم، النموذج. وله كتابات أخرى :
"اللغة والبنى : محاولة منطقية وسميولوجية" (1969)، "بنى البحث والمعرفة"، و"علم النفس والبنى".

**المهام** (verbatim) :

- كيف يحدّد الكاتب دلالة ((النموذج)) ؟
- ما الفرق بين النموذج والمثال ؟
- أرصد معنيي النموذج كما عرضهما الكاتب.
- كيف يعمل النّموذج في الحقل العلمي ؟
- ماذا يقصد الكاتب بتعقّد أنواع النموذج وتنوّع استعمالاته ؟
- أفكّر في نموذج ((بوهر)) وأكشف عن الطابع **الإجرائي** للنموذج.
- أستحضر مثالا من العلوم الفيزيائيّة التي أدرسها لأتبيّن قيمة ((النموذج)).
- ماذا تحمل النمذجة للعلم اليوم : معرفة أم منهجا ؟

**Encadré-citation (p.222, courte, attribuée)** : « فالنموذج هو بادئ ذي بدء "التصميم" … » —
**مولود**.

##### سند 2 — النموذج واستكشاف الظواهر — p.223–224

**التمهيد** (verbatim) :

> يجري استعمال النماذج، في الحقل العلمي، على أنحاء مختلفة. ولعلّ في استحضارها ما يستجيب لأغراض
> متنوّعة تبدو خارجة عن النماذج ذاتها، وكأنّ فضلها كامن لا فيما تنغلق عليه من حقيقة بل فيما
> تنفتح عليه من إمكان.

**الكاتب — جيل كوهن تنودجي (1938)** : فيزيائي فرنسي وُلد بالجزائر، من قدماء معهد البوليتكنيك وهو
شقيق الفيزيائي **كلود كوهن تنودجي** الحائز على جائزة نوبل للفيزياء (1997). يُعدّ أب مفهوم
"الأفق" ونال سنة 1971 جائزة **تيبو** `Thibaud`. درّس بجامعة باريس `XI`. من أهمّ ما كتب نذكر
"الثّوابت الكونيّة" (1991). كما كتب بالاشتراك مع ميشال ستيرو `STIRO` [sic — lire `SPIRO`]
"المادة فضاء — زمن" (1986).

**المهام** (verbatim) :

- كيف يحدّد الكاتب دور النموذج ؟
- لِمَ يتحدّث الكاتب عن (( نماذج )) لا عن (( نموذج)) ؟
- أتتبّع النص وأستخرج أنواع النماذج التي يشير إليها الكاتب.
- أستند إلى النصّ وأعمّر الجدول التالي : *(tableau à 3 colonnes vides —* **أنواع النماذج** /
  **مراحل تطوّر النظريّة** / **أدوار النماذج***)*
- أستعيد مكتسباتي من النصّ وأتبيّن الفارق بين الواقع الذي تقدّمه النظريّة العلميّة والواقع كما
  أدركه في تجربتي المباشرة.
- أستخلص دلالة النمذجة.

**Encadré-citation (p.223)** : « تشبه النماذج ما يسميه المهندسون "نموذجا مصغّرا" أو "تصميما" » —
**تنّودجي**.

##### سند 3 — في الفرق بين النموذج الرياضي والنموذج الفيزيائي — p.225–226

**التمهيد** (verbatim) :

> إن رهان العقل العلمي المعاصر على (( الحدس )) في تعقل الواقع قد يبرّر إلى حد ما إنشاءه لنماذج
> متعددة بتعدد مجالات اشتغاله. وهذا أمر يطرح الحاجة إلى التفريق بين هذه النماذج المتنوعة :
> بين نموذج رياضي وآخر فيزيائي.

Points saillants du texte (reformulés) : le modèle mathématique **exclut de nombreux facteurs**
et c'est précisément ce qui lui permet de simplifier le complexe (modèle de l'économie de
marché vs de l'économie planifiée ; modèle mathématique de l'apprentissage ; chaînes de
`Markov` en psychologie) — il diffère donc totalement des modèles de la physique du XIX<sup>e</sup>
siècle, où le but était de **rendre visible**. Le modèle mathématique est **hypothétique** : il
contient des `paramètres` ajustés pour coller aux données ; des observations plus fines
n'imposent pas seulement un réglage plus fin mais parfois la **révision des équations
fondamentales** — l'ancien modèle nous a menés jusqu'ici, il faut un nouveau modèle. Le modèle
physique du XIX<sup>e</sup>, lui, était **spatial et visuel** (maquette de navire, d'avion). La
conclusion : les modèles visuels aident (l'esprit travaille par intuition), mais un modèle
visuel réussi n'est **pas** une garantie de vérité de la théorie, et son absence n'est pas un
motif de réfutation.

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

- ⚠️ **PROFONDEUR RÉELLE DE CE PALIER — first-pass (ossature) + 12 pages en profondeur.** Ce qui
  est transcrit ici a été **lu sur les pages** :
  - **l'ossature** — la page de titre et son verso (p.1–2), le التقديم (p.3), la خارطة الكتاب
    (p.4–5), l'ouverture du محور 1 (p.6) et le **فهرس intégral** (p.404–408). Le §2 et le §4 en
    dérivent : ils donnent le **scope, la structure et les plages de pages** exacts, ainsi que
    l'inventaire nominatif des **113 سندات** (auteur + titre + page).
  - **une amorce de profondeur sur le seul مبحث 2** — **p.215–226** : la page d'ouverture (avec
    les deux organigrammes officiels أبعاد النمذجة / النمذجة ومطلب الحقيقة), la **نافذة مدخل
    complète** (وضعية استكشاف بطلميوس/نيوتن, le texte de هيزنبرغ avec sa notice, ses هوامش et ses
    7 مهامّ, la page de méthode الأبعاد الإشكاليّة) et les **3 premiers سندات sur 16** (مولود,
    تنّودجي, كارناب) avec تمهيد verbatim, thèse, هوامش, notice d'auteur et مهامّ.

  **Ce qui n'est PAS transcrit** : tout le reste — p.7–214, **p.227–270** (سندات 4–16 du مبحث 2, sa
  نافذة دعائم et ses تحديدات/سياقات, sa نافذة كيفيّات التفكير, le نصّ مطوّل de بوبير, ses
  مختصرات) et p.271–402. **Aucun chapitre n'atteint la profondeur de génération (R-5)** — pas même
  le مبحث 2, couvert à 12 pages sur 56 ⇒ `chapitresGeneration: []` au registre, et **le LOT B est
  interdit** sur les cinq chapitres tant que ces pages ne sont pas lues.
- **Motif de l'arrêt** : limite d'usage de session atteinte (2026-08-04), qui a tué les deux
  sous-agents de transcription avant leur première écriture. Arrêt propre au dernier palier
  poussable (méthode, T-9/T-10) plutôt que fiche bâclée.
- **Reprise — rendu des pages.** Le rendu PNG de la session 2026-08-04 vivait dans un scratchpad
  **éphémère** : ne pas compter dessus. Le re-rendu est **déterministe et gratuit** (T-1 — aucun
  LLM), ~12 min pour les 408 pages ; `p-NNN.png` = page imprimée NNN (**offset 0**) :

  ```bash
  pdftoppm -png -r 150 -f 227 -l 270 \
    cnp-officiel/manuels/secondaire/c4/eleve/210402P00.pdf <dir>/p
  ```

  (poppler local : `_tools/poppler/poppler-26.02.0/Library/bin/pdftoppm.exe`. 150 dpi suffit ; 300
  seulement pour un encadré douteux.) ⚠️ La couche-texte du PDF est un encodage QuarkXPress hérité,
  **illisible telle quelle** (glyphes en ordre visuel) : `pdftotext` ne sert à rien, la vision est
  obligatoire.
  Ordre de reprise conseillé : **finir le مبحث 2
  en reprenant à la p.227** (سند 4 « سيمون », il reste 44 p. — c'est le chapitre le plus proche de
  la barre R-5, donc le premier à devenir générable), puis 3.2 (p.347–402, 56 p.), puis 3.1
  (p.271–346), puis 1.2 (p.115–214), puis 1.1 (p.6–114). **Ne pas relire** p.1–6, p.215–226 ni
  p.404–408 (T-2/R-4).
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
