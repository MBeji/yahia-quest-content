# الفلسفة / Philosophie — Baccalauréat (الشّعب العلميّة) · programme officiel CNP

> **Sources** (une seule — voir §5) :
>
> - **Guide enseignant** (programme) : **non disponible au corpus CNP**. Aucun guide n'existe pour
>   ce couple ⇒ **le manuel élève fait référence** (profil `ecole-secondaire`).
> - **Manuel élève** (contenu/exemples/exercices) : `210402P00.pdf`
>   (`cnp-officiel/manuels/secondaire/c4/eleve/`) — « كتاب الفلسفة — لتلاميذ السّنة الرّابعة من
>   التّعليم الثانوي — الشّعب العلميّة ». **408 pages** (page PDF = page imprimée, **offset 0**).
>   **Pages lues** : p.1–6 (page de titre, copyright, التقديم, خارطة الكتاب, ouverture du محور 1),
>   **p.215–270 — le مبحث 2 en entier, à profondeur de génération**,
>   p.404–408 (فهرس الكتاب intégral).
>   **Transcrit le** : 2026-08-04 → 2026-08-05. **Statut** : **`partielle` / profondeur `mixte`** —
>   ossature sur tout le programme, **profondeur de génération sur le seul مبحث 2** (voir §6).
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

4. **Corroboration externe — le manuel de FRANÇAIS du même niveau** (`221402` « Au gré des textes »,
   transcrit par une autre session le 2026-08-05, fiche `programme/bac-math/francais.md`) : le
   catalogue CNP l'intitule « **فرنسية_شعب علمية** » — le même label que le nôtre — et **sa page de
   titre énumère les cinq sections une par une** : Mathématiques · Sciences techniques · **Économie
   et gestion** · Sciences expérimentales · Sciences de l'informatique.
   Ce constat ne porte pas sur *notre* manuel et **ne s'y transpose pas mécaniquement** (la fiche
   français le dit elle-même : « la question reste OUVERTE pour l'arabe et la philosophie »). Mais
   il établit un fait qui, lui, vaut pour le catalogue entier : **le label « شعب علمية » du CNP
   inclut bel et bien éco-gestion**, alors même que cette section n'est pas scientifique. Le seul
   soupçon sérieux qui pesait sur le raisonnement 1–3 — « et si "الشّعب العلميّة" excluait
   éco-gestion ? » — est donc levé sur pièce.

**Conclusion** : le manuel lui-même **ne tranche pas** (constat 1–2) ; c'est l'**exhaustivité du
catalogue officiel** (constat 3) qui tranche, et le sens attesté du label (constat 4) qui écarte la
seule objection restante. La partition des manuels de philosophie du bac est binaire — آداب d'un
côté, tout le reste de l'autre — donc les cinq sections non-Lettres (`bac-math`,
`bac-sciences-exp`, `bac-eco-gestion`, `bac-techniques`, `bac-info`) sont desservies par `210402`.
Le rattachement d'éco-gestion n'est donc **plus une déduction par élimination interne au manuel**,
mais un constat sur le corpus officiel complet.

> ⚠️ Ce qui manquerait pour un constat **direct** : une page de `210402` qui énumère les sections.
> Les p.1–6 et le فهرس (p.404–408) n'en portent pas. Si les p.7–402 en révélaient une, elle
> primerait sur tout ce qui précède — l'y consigner alors, avec sa page.

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

#### مبحث 2 — transcription en PROFONDEUR, **intégrale** (p.215–270)

> ✅ **Portée : p.215–270, la totalité du مبحث** — page d'ouverture et ses deux organigrammes,
> نافذة مدخل complète, les **16 سندات** un par un, la نافذة دعائم (تحديدات + سياقات فكريّة),
> la نافذة كيفيّات التفكير, le نصّ مطوّل de بوبير et les مختصرات.
> C'est le **seul chapitre à la profondeur de génération** : il est déclaré dans
> `chapitresGeneration` au registre, et lui seul. **R-7 non encore faite** (§6). **Source** : manuel élève `210402`
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

##### 2.2 نافذة سندات — suite : سندات 4-16 (p.227-250)

> **Pages lues** : p.227–250 (intégral). **Source** : manuel élève `210402`
> (كتاب الفلسفة — السّنة الرّابعة من التّعليم الثانوي — الشّعب العلميّة, CNP).
> Suite directe de la نافذة سندات du **مبحث 2 — العلم بين الحقيقة والنمذجة** (les سندات 1–3,
> p.220–226, sont décrits plus haut dans la fiche).
>
> **Convention constatée** : chaque سند s'ouvre par un **تمهيد** (chapeau problématisant imprimé
> sur fond rose) suivi du texte et de sa référence bibliographique, puis des encadrés
> **الهامش / الهوامش / الهامشان** (notes), **الكاتب** (notice d'auteur) et **المهام** (consignes de
> travail). ⚠️ L'extension n'est **pas** systématiquement une double page : les سندات 9, 10, 14 et
> 16 tiennent en une page ou débordent différemment — la colonne « ص. » ci-dessous donne
> l'étendue réellement imprimée.

###### Tableau récapitulatif des سندات 4–16

| # | المؤلّف (كما هو مطبوع) | عنوان السّند | ص. | الأطروحة (مُعاد صياغتها) | المفاهيم |
| --- | --- | --- | --- | --- | --- |
| 4 | **هربرت سيمون** — *علوم الأنساق وعلوم الاصطناعي* (`H. SIMON, Sciences des systèmes, sciences de l'artificiel`, Paris, Dunod, 1991, pp 22-23) | **النمذجة والأنساق الرمزية** | 227–228 | L'ordinateur n'est qu'un membre d'une **famille de systèmes de symboles** dont l'autre membre majeur est le cerveau humain : ce sont des artefacts **intentionnels** (قصديّة) de traitement de l'information. Un tel système peut **modéliser son milieu** grâce à des représentations internes, à condition d'avoir « des mains et des fenêtres sur le monde » (entrées/sorties) qui encodent et décodent l'information du dehors. Les ordinateurs ont fait passer les systèmes de symboles du « paradis platonicien des Idées » à un **monde empirique de processus réellement effectués**. | أنساق الرموز — النمذجة — التمثّلات الداخليّة — التشفير ومعادة التشفير — المصنوعات — القصديّة — الحاسوب والدّماغ — الإحكام والدقّة والبرهنة — الفردوس الأفلاطوني للمثل |
| 5 | **ج. بياجيه** — *البنيوية* (`Jean PIAGET, Le structuralisme`, éd. PUF, Que sais-je ? 1996, pp 6-7-8) | **النموذج والبنية** | 229–230 | La **بنية** est d'abord un système de transformations qui se conserve et s'enrichit par son propre jeu, sans faire appel à des éléments extérieurs : elle a trois caractères — **الكلّيّة، التحوّلات، الانتظام الذاتي**. En un second sens, elle doit aider à trouver une **صورنة** (formalisation) traduisible en équations logico-mathématiques ou passant par un **نموذج تحكّمي** (cybernétique). D'où la thèse centrale : la formalisation est l'**œuvre du théoricien**, alors que la structure, elle, en est **indépendante**. | البنية — النموذج — الصورنة — التحوّلات — الكلّيّة — الانتظام الذاتي — النموذج التحكّمي (السيبارنيطيقا) — عمل المنظّر |
| 6 | **لودويغ باسكال** — *فلسفة العلوم في القرن العشرين* (`Ludwig PASCAL, La philosophie des sciences au 20 ème Siècle`, éd. Flammarion 2000, pp 200-201) | **النموذج بناء خيالي** | 231–232 | Les modèles que bâtissent les savants peuvent parler de choses qui n'existent que dans une **idéalisation** (`idéalisation`), une **construction imaginaire** dont l'unique fin est d'organiser des données ou d'obtenir des prévisions. Mais les théories, elles, sont des discours qui affirment la **nécessité d'existence** de certaines choses : les savants distinguent la **نمذجة**, apparentée à l'imagination, et la **تنظير** qu'accompagne une foi sérieuse en la vérité des propositions. À cette condition seulement l'étude des **présupposés ontologiques** d'une théorie devient possible. | النموذج — التخيّل — التأمثل `idéalisation` — النظريّة والنمذجة والتنظير — الواقعي والافتراضي — المفترضات الأنطولوجيّة — التوقّعات |
| 7 | **جون لويس لوموانيو** — *البنائيّة* (`LE MOIGNE, Le constructivisme`, éd L'Harmattan, 2002, T. 1, p 196) | **قيمة النمذجة** | 233–234 | Le **changement de code** (« تغيير الشّفرات ») opéré par les modélisateurs rend soudain **simple, descriptible et interprétable** un phénomène qui paraissait d'une complexité extrême : ellipse, électron, fonction d'onde sont des concepts inventés pour se représenter des phénomènes complexes. Exemple imprimé : l'orbite de **Mars**, que Kepler mit 900 feuilles de calcul à établir, devient descriptible par une seule équation périodique dès qu'on abandonne les cercles-dans-des-cercles de Ptolémée et de Copernic — au prix de renoncer à « التماثل الإلهي » du cercle. | النمذجة — الشّفرة/تغيير الشّفرات — التبسيط — التعقيد — التفسير والوصف والتأويل — النموذج الرياضي — تعدّد النماذج |
| 8 | **باسكال نوفل** — *بحث في مفهوم النموذج*, مقالة: النماذج والاستعارات (`Pascal NOUVEL, Enquête sur le concept de modèle - Article : Modèles et métaphores`, PUF, 2002, pp 193-196) | **النموذج تبسيط** | 235–236 | Le modèle n'est pas un signe d'une relation nouvelle entre éléments : il exprime une **stratégie de la négligence** (إستراتيجيا الإهمال). Il vaut non pour sa vérité mais parce qu'il permet de laisser de côté un grand nombre de traits d'une situation pour n'en retenir qu'un ou quelques-uns : « ne regardez pas cela, regardez seulement ceci ». Il est ainsi l'**opération inverse de la métaphore** (qui montre en cachant peu) ; la deuxième loi de Newton, écrite `f = m.a`, est donnée comme le modèle exemplaire de cette simplification qui rend une situation compréhensible. | النموذج — التبسيط — إستراتيجيا الإهمال — الاستعارة — الفهم — الرّسم الاختزالي — تفسير المرئي المعقّد باللامرئي البسيط |
| 9 | **هانز فرودونتال** — *دلاليّة عبارة النموذج* (`Hans FREUDENTHAL, La sémantique du terme modèle`, Paris 1978, pp 159-160) | **كيف ينشأ النموذج ؟** | 237 | La **technique** est une source d'exemples de modèles aussi riche que la science : on étudie la circulation de l'air dans une mine, ou la circulation sanguine, en la **simulant** par le modèle du circuit électrique ; les calculateurs analogiques incarnent les opérations mathématiques en processus physiques ; les outils de contrôle du trafic routier ont été trouvés **par hasard** en assimilant le flux routier à un système. De même l'économie théorique fabrique des modèles macro, méso et micro : des modèles **numérisés** qu'on bâtit et manipule pour calculer l'effet d'une variation d'impôt. | النموذج — التقنيّة — المحاكاة — الحواسيب التماثليّة — النماذج الاقتصاديّة (ماكرو/ميزو/ميكرو) — التناول الرقمي — الإجرائيّة |
| 10 | **جون لويس لوموانيو** — *البنائيّة* (`LE MOIGNE, Le constructivisme`, éd L'Harmattan, 2002, T3, pp 11-13) | **النمذجة للفهم** | 238–239 | « النمذجة للفهم » : modéliser, c'est chercher à comprendre nos relations au monde en les représentant par des **systèmes symboliques artificiels** que nous produisons et pratiquons — rendant ainsi **intelligible** l'aventure de la connaissance. Nous en avons l'habitude depuis toujours (écriture musicale, rythme, écriture mathématique, informatique, chimie) ; astronome, poète, ingénieur, compositeur, sculpteur y trouvent le même bon usage. Mais le partage de ces modèles **ne va pas de soi** : chacun les interprète et les transforme, l'un invoquant « الموضوعية العلمية », l'autre la garantie symbolique de son projet — d'où la **scission entre « les deux cultures »**, littéraires et scientifiques, que l'auteur déplore. | النمذجة — الفهم — الأنساق الرمزيّة الاصطناعيّة — المعرفة والمغامرة — التأويل — الموضوعيّة العلميّة — الثقافتان (الإنسانيون ورجال العلم) — التصميم |
| 11 | **رونيه توم** — *أمثال وكوارث* (`René THOM, Paraboles et catastrophes ; éd. Flammarion, Paris, 1983, pp 521-621` — pagination telle qu'imprimée) | **شروط صلاحية النموذج** | 240–241 | Modéliser, c'est répondre à une situation **surprenante** en construisant un système — matériel **ou mental** — analogue à elle, en y transportant la question par analogie, puis en rapatriant la réponse. D'où **deux justifications** : **ماقبلي** (a priori : une théorie de l'analogie entre système naturel et modèle) et **مابعدي** (a posteriori : confrontation aux données de l'expérience). La science contemporaine, faite d'expériences très coûteuses, devrait exiger la première ; elle fait l'inverse et la néglige — d'où sa **stérilité**. Chute paradoxale : les modèles **les plus coûteux et les moins soignés** dans leur construction donnent les meilleurs résultats. | النمذجة العلميّة — صلاحيّة النموذج — المماثلة — التبرير الماقبلي/المابعدي — التجريب وكلفته — عقم العلم المعاصر — نظريّة الكوارث |
| 12 | **جون لادريار** — *رهانات العقلانية* (`Jean LADRIERE, Les enjeux de la rationalité`, Paris - Aubier 1977, p 63) | **النشاط العلمي والنشاط التقني** | 242–243 | Science et technique se comparent par le couple **معلومة / تنظيم**. La **science** convertit une information objectivement réalisée **sous forme organisée** en information réalisée **sous forme de représentations conceptuelles** — information **libre**, incorporée à aucun support, donc de valeur « **كونيّة** ». La **technique** fait le trajet **inverse** : elle projette l'information abstraite sur un support sensible, ajoutant aux systèmes naturels des **systèmes artificiels** — d'où une action plus large, plus instrumentale, aux effets plus forts et plus variés, et une **autonomie accrue** de l'homme face au milieu naturel. | النشاط العلمي — النشاط التقني — المعلومة والتنظيم — التمثّلات المفهوميّة — الكونيّة — الأنساق الاصطناعيّة — الأداتيّة — استقلاليّة الفعل |
| 13 | **هانز فرودنتال** — *مخاطر هيمنة مفرطة لعلم التركيب على علم الدلالة في العلوم الراهنة* (`Hans FREUDENTHAL, Colloque : Dangers d'une prédominance abusive du syntaxe sur la sémantique dans les sciences actuelles`, Paris 1978, p161) | **النمذجة إجراء منهجيّ** | 244 | Des modèles matériels aux modèles théoriques, le modèle est resté l'**image simplifiée et réduite** d'une réalité. Or dans la **théorie des modèles**, la relation modèle/chose paraît **inversée** : à force de décrire les faits platoniciens par des **systèmes axiomatiques**, on a fini par confondre la réalité avec sa description — c'est le **الارتداد الدّلالي**. D'où deux emplois distincts : un modèle qui sert à **contrôler théoriquement** une réalité donnée, et un modèle qui sert à **remplir de contenu réel** une structure théorique. | النموذج — النمذجة كإجراء منهجي — الأكسمة/الأنساق الأكسيوميّة — الارتداد الدّلالي — الهندسة اللاإقليديّة — النموذج الكوكبي للذرّة — صلاحيّة النموذج |
| 14 | **جون لويس لوموانيو** (avec un premier bloc attribué à **آلان فانفلي**) — *البنائيّة* (`LE MOIGNE, Le constructivisme`, éd L'Harmattan, 2002 T2, pp 311-312-313) | **النمذجة وسؤال المعنى** | 245–246 | La question **téléologique** (à quoi et à qui sert le modèle) oblige la **النمذجة النسقيّة** à inclure dans son parcours **les fins du modélisateur lui-même**, qui ne peut se tenir hors du modèle qu'il construit. La `TSG` a-t-elle de quoi affronter le **problème éthique** sans se réfugier dans la neutralité ? Et puisque toute construction produit une **forme**, la modélisation touche aussi à l'**esthétique**, donc à la **question du sens**. Contre l'ambition positiviste de tout réduire à « l'expression la plus simple », Le Moigne oppose cette capacité **à produire du sens** par le traitement intentionnel des **symboles**. | النمذجة النسقيّة — الغائيّة — الإيتيقا — الإستيتيقا — الهرمينوطيقا — إنشاء المعنى — الشكل/المضمون — الرمز — نقد الوضعيّة والاختزال |
| 15 | **بيار دوهام** — *النظريّة الفيزيائيّة: موضوعها وبنيتها* (`Pierre DUHEM, La théorie physique : son objet et sa structure`, éd. Vrin 1989, pp 143-144) | **حدود النموذج الميكانيكي** | 247–248 | Dès qu'on cesse de créditer les **modèles** de découvertes qui reviennent aux **théories abstraites**, et qu'on ne confond plus modèle et **analogie**, la part des théories « imaginatives » dans les progrès de la physique se révèle **très faible**. Kelvin doit ses découvertes aux systèmes abstraits (thermodynamique, électrodynamique) et n'use des modèles mécaniques que pour **exposer** l'acquis ; Maxwell n'a fondé la théorie électromagnétique de la lumière qu'en **abandonnant tout modèle**, par extension analogique aux courants de déplacement. | النموذج الميكانيكي — النظريّة المجرّدة — المماثلة — التخيّلي والافتراضي — حدود النموذج — الاختراع والعرض — تيارات التنقّل |
| 16 | **ر.بلانشي** `Robert BLANCHÉ` — *الأكسيومية أو منظومة الأوليات*, ترجمة محمود بن جماعة، دار محمد علي للنشر 2004، ص 101 | **قيمة النماذج** | 249–250 | Les physiciens se partagent entre **théories abstraites** et **théories représentées par des images** ; mais comprendre exige un **va-et-vient à deux niveaux** — s'élever du fait à l'idée puis redescendre de l'idée au fait —, mouvement redoublé où se résume toute connaissance et dont l'**axiomatique** est l'exemple le plus net. Celle-ci récuse le **dogmatisme de la synthèse** et le rêve d'un point de départ absolu, généralise la forme **hypothético-déductive**, et son **recul** dément le logicisme en trouvant toujours un « antérieur ». Mais coupée de ses **fondements intuitifs**, elle devient « un jeu vain, sans relation avec la science ». | النظريّات المجرّدة والممثّلة بصور — الفكرة والواقعة — الأكسيوميّة — الأوليّات — الشكل الفرضي-الاستنتاجي — وثوقيّة التركيب — المواضعيّة — الحدس — الحقيقة العلميّة |

---

###### سند 4 — النمذجة والأنساق الرمزية — p.227–228

**التمهيد** (verbatim) :

> يمثل الحاسوب أحد أهم إنجازات العقل البشري. وإذا كان هذا بالذّات شاهدا عند بعضهم على تفوّق
> العقل، فإنّه شاهد أوثق على كيفية اشتغال هذا العقل. إنّه أحد المصنوعات التي تترجم المسارات
> المعقّدة للعقل في النمذجة، في تشفير المعلومات المستمدّة من العالم الخارجي.

**Référence imprimée** : هربرت سيمون، علوم الأنساق وعلوم الاصطناعي —
`H. SIMON, Sciences des systèmes, sciences de l'artificiel, Paris, Dunod, 1991, pp 22-23`.

**Points saillants du texte** (reformulés) : l'ordinateur est un individu d'une famille
d'artefacts appelés **أنساق الرموز** ; certains pensent (`anthropomorphie` — « أنتروبومورفيا »)
que le membre le plus important en est la pensée et le cerveau humain. Ces systèmes sont
« جوهريّة » parce que leur seule raison d'être est leur capacité à **s'adapter à un milieu** ; ce
sont des systèmes **intentionnels** (قصديّة) de traitement de l'information. Un système de
symboles physiques contient des entités appelées **رموز** — figures physiques (traits de craie
sur un tableau noir) qui peuvent être des composants d'une structure de symboles (parfois
appelées « عبارات ») — et possède des processus simples qui agissent sur ces structures : ils
créent, modifient, copient et détruisent les symboles. Ce que fait un tel système, c'est
**produire des représentations internes** (des « صورا ذهنيّة ») du milieu auquel il cherche à
s'adapter, ce qui lui permet de le **modéliser** avec précision. Pour cela il lui faut « أيدي
ونوافذ على العالم » : des moyens d'acquérir l'information du dehors et de la ré-encoder en
symboles internes, et des moyens de produire des symboles qui agissent en retour sur le milieu.
On dit ces systèmes « physiques » pour rappeler qu'ils existent comme **outils du monde réel**,
faits ici de verre et de métal (les ordinateurs), là de chair et de sang (les cerveaux). Chute
du texte : les ordinateurs ont transporté les systèmes de symboles du « **الفردوس الأفلاطوني
للمثل** » vers un monde empirique de processus réalisés par des machines, par ces cerveaux, ou
par les deux ensemble.

**الهامش** (verbatim) :

1. إشارة إلى ما ورد في الفقرة الأولى من النص.

**الكاتب — هربرت سيمون (1916—2001)** (verbatim resserré) : ولد يوم 15 جوان 1916 في ميلوانكي
(فيسكونسين) وتوفي في 9 فيفري 2001 ببيتسبورغ. كان أحد الروّاد الأمريكيين للذكاء الصناعي، وهو باحث
في العديد من المجالات كالإعلامية وعلم النفس المعرفي والفلسفة. كان أيضا عالم اقتصاد، كما اهتمّ
ببنية التنظيم الاقتصادي وخصائص مسار القرار المتعلّق به. نال جائزة نوبل في الاقتصاد سنة 1978.
دارت أعماله حول جدوى الفوردية وشكّك في النظريات الكلاسيكية الجديدة. من أهمّ كتاباته : "السلوك
الإداري" (1947)، "علوم الأنساق، علوم الاصطناعي" (1969)، "نماذج التفكير" (ج1 1979/ج2 1989)،
"نماذج لحدود العقلانية والسلوكية الاقتصادية وأعمال التنظيم" (ج1 وج2 1982) و"نماذج من حياتي"
(1991).

**المهام** (verbatim) :

- أفهم قول الكاتب بانتماء الدّماغ البشري إلى عائلة ((أنساق الرّموز)) وأحدّد وجوه التماثل بينه
  وبين الحاسوب.
- أحدد معنى هذه الأنساق الرمزيّة وأفهم كيف يمكن أن تنمذج الوسط.
- هل يعبّر تعقيد هذه الأنساق على تعقيد الواقع؟
- على أيّ وجه أفهم العلاقة بين الأنساق الرمزيّة والعالم الواقعي؟
- بأيّ معنى أفهم الوجود المتجسّد في الواقع للنظم الرمزية؟
- أحدد معنى الآلة: هل هي بمنزلة الشيء أم الرمز؟
- كيف أفهم قول الكاتب بأنّ (( الحواسيب قد نقلت الأنساق العلامات [sic] من الفردوس الأفلاطوني
  للمثل إلى عالم خبري للسيرورات الواقعيّة )) ؟

**Encadré-citation (p.228)** : « تُسمّى الأنساق الرمزيّة أنساقا "فيزيائية"… هي مصنوعة هنا من
بلّور ومعدن (حواسيب)، أوهناك من لحم ودم (الأدمغة) » — **سيمون**.

**Illustrations** : p.227 portrait photo de Simon ; p.228 profil de tête stylisé traversé par un
ordinateur et des rayons de lumière.

---

###### سند 5 — النموذج والبنية — p.229–230

**التمهيد** (verbatim) :

> مثّلت البنيويّة تيّارا واسعا شمل العلم والفلسفة على حدّ السواء. وإذا كانت عند الفلاسفة نزعة
> عارضة يمكن الارتداد عنها، فإنّها في العلم المعاصر سمة مخصوصة بل، إنّها بالذّات ما يسعى العقل
> العلمي، في مساراته المختلفة، إلى تأكيدها من خلال عملية النمذجة.

**Référence imprimée** : ج. بياجيه، البنيوية —
`Jean PIAGET, Le structuralisme, éd. PUF. Que sais-je ? 1996, pp 6-7-8`.

**Points saillants du texte** (reformulés) : en une première approche, la **بنية** est un système
de transformations qui contient aussi des **lois** (par opposition aux propriétés des éléments),
qui **se conserve** et s'enrichit par le jeu même de ses transformations, sans que celles-ci
sortent de ses limites ni fassent appel à des éléments extérieurs — d'où les **trois caractères
fondamentaux : الكلّيّة، التحوّلات، الانتظام الذاتي**. En une seconde approche — qui vient après la
découverte de la structure bien qu'elle porte sur une étape antérieure —, la structure doit aider
à trouver une **صورنة**. Il faut seulement comprendre que cette formalisation est l'**œuvre du
théoricien**, tandis que la structure en est **indépendante** ; et cette formalisation peut se
traduire directement en équations logico-mathématiques ou passer par un **نموذج تحكّمي**
(cybernétique). Il existe donc **des degrés variables de formalisation possible**, tributaires des
décisions du théoricien, à qui il revient de vérifier le type d'existence de la structure qu'il
découvre dans chaque champ de recherche.

**الهامش** (verbatim) :

1. **تحكّمي (سيبارنيطيقي)** : نسبة إلى السيبارنيطيقا `Cybernétique` وهو علم حديث ظهر في بداية
   الأربعينيات من القرن الـ20 ويعتبر الرياضي نوربرت فينر من أهمّ مؤسسيه وقد عرّف فينر
   السيبارنيطيقا على أنّه علم القيادة والتحكّم `control` في الأحياء والآلات ودراسة آليات التواصل
   `communication` في كلّ منهما. **(انظر سياقات فكريّة)**

**الكاتب — جون وليام فريتز بياجيه (1896—1980)** (verbatim resserré) : عالم نفس وبيولوجي ومنطقي
وإبستيمولوجي سويسري، ولد يوم 09 أوت 1896 بنوشاتيل وتوفي يوم 16 سبتمبر 1980 بجنيف. نال شهادة
الدكتوراه في العلوم الطبيعية وعُرف بأعماله في علم النفس النمو أو التطوري وأسّس إبستيمولوجيا سماها
**"الإبستيمولوجيا التكوينية"**. كانت له إضافات هامة جدا فيما يتعلق بعلم نفس الطفل فبيّن أنّ للطفل
أنماط تفكير خاصة به وتميزه كليّا عن الشخص البالغ وقد حدّد لهذه الأنماط مراحل تطورية تُعَدُّ إلى
حدّ الآن مرجعا لعديد الأبحاث الأخرى خاصة في التربية وعلم الاجتماع وعلم النفس والإبستيمولوجيا
والاقتصاد والحقوق. من أهمّ أعماله نذكر : "تكون الواقع عند الطفل" (1937)، "مقدمة للإبستيمولوجيا
التكوينيّة" (1950)، "دراسات سوسيولوجية" (1965)، "المنطق والمعرفة العلمية" (1967)، "البيولوجيا
والمعرفة" (1967)، "البسيكولوجيا والبيداغوجيا" (1969)، "البسيكولوجيا والإبستيمولوجيا" (1970).

**المهام** (verbatim) :

- أحدد خصائص البنية من خلال النص.
- أفهم المقصود بالصورنة وأوضّح كيف يمكن للبنية أن تساعد على تحقيقها.
- ما الذي يفسر تعدد البنيات في العلم؟
- أحدد علاقة البنية بالنموذج وأفهم معنى أن تكون البنية مستقلة عن عمل المنظر.
- أستثمر ما أعرفه عن السيبارنيطيقا لأدقّق العلاقة بين البنية والصورنة والنموذج التحكمي.
  (أستأنس بما ورد في نافذة سياقات فكريّة حول السيبارنيطيقا)

**Encadré-citation (p.230)** : « إنّ هذه الصورنة هي عمل المنظّر، في حين أن البنية تكون مستقلّة
عنه » — **بياجيه**.

**Illustrations** : p.229 portrait photo de Piaget ; p.230 photo d'un homme écrivant des schémas
et des formules à la craie sur un tableau noir.

⚠️ **Renvoi interne imprimé** : le هامش et la dernière مهمّة renvoient tous deux à la نافذة
**سياقات فكريّة** du même مبحث, à l'entrée **السيبارنيطيقا**.

---

###### سند 6 — النموذج بناء خيالي — p.231–232

**التمهيد** (verbatim) :

> ساد الاعتقاد طويلا بأن العلم لا يكترث بالسؤال الأنطولوجي عن حقيقة الموجود في العالم. فذاك من
> شأن الفلسفة، عليه فحسب تفسير ما يوجد في العالم. غير أنّ طبيعة النظرية العلمية من جهة وإنشاء
> النماذج في العلم يحملان على إعادة النظر في توزيع الأدوار، يحصل هذا انطلاقا من مساءلة منظور
> العلم للواقع.

**Référence imprimée** : لودويغ باسكال، فلسفة العلوم في القرن العشرين —
`Ludwig PASCAL, La philosophie des sciences au 20 ème Siècle, éd. Flammarion 2000, pp 200-201`.

**Points saillants du texte** (reformulés) : les modèles que construisent les savants peuvent
parler de choses qui **ne peuvent exister que dans une idéalisation** (`idéalisation`), dans une
**construction imaginaire** dont l'unique but est d'organiser des données ou d'obtenir des
prévisions. Mais les théories, elles, sont des discours qui, semble-t-il, affirment la
**nécessité de l'existence** de certaines choses ; contrairement à ce qui vaut pour les
imaginations ou les modèles, on peut tenir les spécialistes pour sérieusement disposés à prouver
le contenu des théories qu'ils bâtissent, et à le faire **réellement** en maintes occasions. La
question fut disputée : **فان فراسن** défend l'idée que les théories scientifiques ne sont pas
objets de croyance pour les savants, lesquels se contentent de les accepter sans les adopter en
droit, afin de pouvoir les utiliser de façon **prévisionnelle** (توقّعي). L'auteur, lui, tient que
les savants distinguent nettement l'acte de **نمذجة** — qui relève à un titre de l'imagination —
et l'acte de **تنظير**, accompagné d'une foi sérieuse en la vérité des propositions constituant
le discours théorique. Cette condition acceptée, l'étude des **présupposés ontologiques** d'une
théorie devient possible, et donc la détermination des **types d'êtres qui existent selon elle**.

**الهامش** (verbatim) :

1. **فراسن** `Van Frassen` [sic — lire `Van Fraassen`] : معاصر (1969)

**الكاتب — لودويغ باسكال (29 — 04 — 1968)** : أستاذ الفلسفة وعلم الاجتماع بجامعة السربون بباريس
وباحث فرنسي في مؤسسة "جان نيكو". من مؤلفاته : "اللغة" (1997)، "فلسفة العلوم في القرن العشرين" —
بالاشتراك مع باربروس وكستلار — (2000)، "الفن والفكر" (2002).

**المهام** (verbatim) :

- أفهم ردّ الكاتب النموذج إلى التخيّل وأحاول فهم معنى عمليّة النمذجة.
- هل ردّ النموذج إلى التخيّلي يفيد فصله عن الواقع مطلقا؟
- أفهم صلة النموذج بالواقع، وأحدد دلالة هذا الواقع: هل هو واقع فعلي أم افتراضي؟
- أحدد دلالة الافتراضي وقيمته.
- أبرز الفرق — حسب النص — بين النظرية والنموذج مستندا على نظرية علمية مثالا.
- أتساءل عن قيمة النموذج في معرفة الواقع وأحدّد رهاناته النظرية والعملية.

**Encadré-consigne (p.232)** : « أتأوّل هذه الصورة في ضوء الفقرة الأولى من النص. »

**Illustrations** : p.231 photographie d'un parc avec une personne assise au bord de l'eau ;
p.232 image de synthèse — une tête de verre translucide entourée de pyramides et de suites de
chiffres binaires (`010`, `1011`, `0122`, `10÷0`, `01-0`, `10-7`).

---

###### سند 7 — قيمة النمذجة — p.233–234

**التمهيد** (verbatim) :

> يؤكد العقل العلمي في مختلف مجالات اشتغاله وبدرجات متفاوتة قدرته على التوصل إلى تفسير الوقائع
> ووصفها، خاصة منها الظواهر الفيزيائية، بطريقة تجعلها أبسط وأكثر وضوحا وذلك كلّما تقدّم في إبداعه
> لنماذج، ينوّعها ويطوّرها ويزيدها دقة منمذجون باتوا يملكون الكلمة المفتاح: النمذجة.

**Référence imprimée** : جون لويس لوموانيو، البنائيّة —
`LE MOIGNE, Le constructivisme, éd L'Harmattan, 2002, T. 1, p 196`.

**Points saillants du texte** (reformulés) : l'observation est chose ordinaire, mais nombre de
phénomènes d'abord perçus comme quasi intelligibles ou mal représentés deviennent soudain
**clairs** dès que les modélisateurs procèdent par « **تغيير الشّفرات** » pour les décrire, ou
décodent le code dans lequel ils se lisent — ainsi de l'**ellipse**, de l'**électron**, de la
**fonction d'onde**, concepts inventés par l'homme pour se représenter simplement des phénomènes
qui semblaient complexes, exactement comme la force, l'énergie ou l'efficacité. Grâce à un
**nouveau code (ou langage) purement conceptuel**, le phénomène d'hier, extrêmement compliqué,
nous devient intelligible et même simple. Exemple imprimé : l'orbite de la planète **Mars**, dont
la détermination coûta à **Kepler** 900 feuilles de calcul, devient d'un coup facile à décrire et
à interpréter par une équation périodique du second ordre, dès lors qu'on remplace les symboles
ptoléméens et coperniciens des sphères célestes (« des cercles qui tournent dans des cercles, qui
tournent autour de… ») par le **symbole de l'ellipse** — au prix de l'audace de renoncer à
« **التماثل الإلهي** » du cercle. La première loi de Kepler (« les orbites des planètes sont des
ellipses dont le Soleil occupe l'un des foyers ») est une expression admirable d'intelligibilité
d'un phénomène tenu, au XVII<sup>e</sup> siècle, pour le comble de la complexité — exemple : les
mouvements **rétrogrades apparents** de certaines planètes vus depuis la Terre.

**الهامش** (verbatim) :

1. **جوهانز كبلار** `Johannes Kepler` (1571—1630) فلكي ورياضي ألماني، ولد بوارتنبرغ. عُرف بنظريته
   في كروية الأرض ودورانها وبقوانينه الثلاث الخاصّة بحركات الأجرام السماويّة والّتي كانت إحدى
   عناصر التأليف النيوتوني لقانون الجاذبيّة.

**الكاتب — جون لويس لوموانيو (1930)** : مهندس وصناعي فرنسي، ولد في 22 مارس 1930 بالدار البيضاء
بالمغرب. عمل أستاذا بجامعات فرنسا وساهم في تطوير البنيوية من خلال مؤلّفه الضخم **البنائيّة** الذي
جاء في ثلاثة أجزاء. له أيضا "علوم الإنسان وعلوم الهندسة"، "علوم التنظيم"، "ابستيمولوجيا العلوم"،
"تركيبية علوم الهندسة"…

**المهام** (verbatim) :

- أبيّن كيف أن عمليّة النمذجة تبسيط لمعقّد يجعله أيسر وصفا وتأويلا. أعتمد مثالا من علم الفيزياء.
- أشتغل على المثال الذي قدّمه النص استدلالا على قيمة النمذجة.
- يتحدث الكاتب عن النموذج بوصفه تعقّلا رائعا للظواهر، أفهم دلالة هذا الحكم وأتبيّن حدوده.
- إذا كان النموذج نتاج تصور مجرّد لواقعة، فكيف يمكن أن يكون تعقّلا يبسّط تعقيدها وييسّر تفسيرها
  ووصفها؟
- هل من تناقض بين تعدّد النماذج وتغيّرها وفكرة نظام موحد للواقع؟

**Encadrés-citation (p.234)** :

- « **نظام كوبرنيك** : "… ( وهي دوائر تدور في دوائر، تدور حول… )…" » — **لوموانيو**
- « (فلنأخذ على سبيل المثال الحركات المتراجعة ظاهريا لمراقب من الأرض لبعض الكواكب). **مثال كوكب
  "مارس"**. » — **لوموانيو**

**Illustrations** : p.233 portrait photo de Le Moigne ; p.234 (a) gravure ancienne du système du
monde (roue zodiacale, visage du Soleil au centre, mention `Mary Evans Picture Library/Photo
Researchers, Inc.`) ; (b) **schéma légendé en français** de la rétrogradation apparente de Mars —
positions 1 à 7 de la `Terre` et de `Mars` autour du `Soleil`, avec les lignes de visée
projetant la boucle rétrograde sur le fond du ciel.

---

###### سند 8 — النموذج تبسيط — p.235–236

**التمهيد** (verbatim) :

> يعتبر العلم، في تاريخه، مثالا على تجربة الإنسان في فك ألغاز العالم من حوله؛ ولأنّ الواقع يزداد
> تعقيدا كلّما اقتربنا منه، ابتدع العقل العلمي لنفسه طريقة يخترق بها حجب الغموض: أن يفترض أنّ ما
> يحدث في العالم يحدث ((كما لو أنّه…)) وفي كلمة أن ينمذج الواقع.

**Référence imprimée** : باسكال نوفل، بحث في مفهوم النموذج، مقالة: النماذج والاستعارات —
`Pascal NOUVEL, Enquête sur le concept de modèle - Article : Modèles et métaphores, PUF, 2002,
pp 193-196`.

**Points saillants du texte** (reformulés) : le modèle n'est pas le signe d'une relation nouvelle
entre de nombreux éléments ; il est l'expression d'une **إستراتيجيا الإهمال** (stratégie de la
négligence). D'où : à quoi bon le modèle en matière de vérité ? Il ne sert pas à « regarder
comme… », il sert à **négliger** une grande part des traits d'une situation pour n'en retenir
qu'un ou quelques-uns. Exemple imprimé : représenter une **enzyme** par des cercles et des carrés
est un dessin réducteur, mais c'est aussi une façon de montrer ce qu'on ne voit pas en la
regardant ; la forme réelle de l'enzyme est plus complexe que ce que le modèle laisse voir, mais
si l'on veut y voir clair il faut **négliger** un grand nombre d'apparences et faire comme si
l'enzyme était simplement un cercle ou un carré. « Ne regardez pas cela, regardez seulement
ceci » : ainsi les choses deviennent claires. La stratégie de la négligence est donc liée au
**فهم**, et non à la mise en évidence : elle est l'**opération inverse de la métaphore** — la
métaphore montre en cachant peu, le modèle cache pour ne garder que peu. Si la science se
reconnaît dans son usage du modèle, c'est qu'elle tient à l'idée d'une **simplification** des
phénomènes. La deuxième loi de Newton, écrite `f = m.a` (« القوة هي حاصل ضارب الكتلة في التسارع »),
est donnée comme modèle exemplaire : elle simplifie une situation réelle en la ramenant à une
situation simple. Newton dit en effet : « ne regardez que ceci, oubliez tout le reste ». C'est un
modèle parce que cela **ne se produit jamais** dans la nature (forces de frottement) : il faut
donc pousser la simplification à l'extrême pour pouvoir dire que « cela arrive toujours ». Et
donc : **la simplification est modélisation**. Autre exemple imprimé : le **نموذج الخميرة**
(modèle allostérique), qui aide à comprendre l'évolution d'une situation elle-même de complexité
moyenne.

**الهوامش** (verbatim) :

1. **جان بيران** : (1870—1942) فيزيائي فرنسي متحصل على جائزة نوبل 1926.
2. `f = m.a`
3. **نموذج الخميرة** `allostérie` : تأثير جزيء على أنزيم بروتيدي.

**الكاتب — باسكال نوفل** : أستاذ محاضر بجامعة باريس — ديدرو وجامعة العلوم بول فاليري بمونبوليه
`III`، ومدير برنامج في المعهد العالي للفلسفة. وهو دكتور في البيولوجيا والفلسفة. له عدّة كتابات في
الفلسفة والإبستيمولوجيا وتاريخ العلوم. من كتبه : "فن حبّ العلم" (2000)، "راهنيّة غاستون باشلار
ومآله" (1992)، وأشرف على عمل بعنوان "بحث في مفهوم النموذج" (2002).

**المهام** (verbatim) :

- استخرج من النص تحديدا للنموذج وللنمذجة.
- أية علاقة لعملية النمذجة باستراتيجيا الإهمال؟
- أبيّن معنى أن يكون القانون الثاني لنيوتن مثالا على النمذجة في بعدها الدلالي.
- أبحث عن محتوى مثال ((نموذج الخميرة)) لفهم تحديد الكاتب للنمذجة.
- أفهم الفرق بين النمذجة والاستعارة.
- أستخلص أثر عملية النمذجة على جهد الإنسان في فهم الطبيعة والعالم من حوله.

**Encadré-citation (p.236)** : « يتمثل العلم في تفسير المرئي المعقّد باللامرئي البسيط » —
**جون بيران**.

**Illustrations** : p.235 portrait photo de Pascal Nouvel ; p.236 image bleutée — profil de
visage superposé à des instruments de mesure (rapporteur, règle, notation `7 x 10`).

---

###### سند 9 — كيف ينشأ النموذج ؟ — p.237

⚠️ **Sur une seule page** : تمهيد + texte + الكاتب + المهام, sans encadré الهامش.

**التمهيد** (verbatim) :

> لا ينحصر إنشاء النموذج على فعل التخيّل فحسب، بل إنّ مجال الممارسة ( التقنية مثلا ) يقدّم
> للمنظّر أمثلة لا تحصى عن نماذج عليه أن يحاكيها ويترجمها جبريّا ليجعل منها أداة لحساب دقيق يطوّر
> به ممارستنا ويجعلها أكثر نجاعة.

**Référence imprimée** : هانز فرودونتال، دلاليّة عبارة النموذج —
`Hans FREUDENTHAL, La sémantique du terme modèle, Paris 1978, pp 159-160`.

**Points saillants du texte** (reformulés) : la **technique** est une source d'exemples de modèles
non moins riche que la science. On étudie la circulation de l'air dans une mine, ou la
circulation du sang dans les vaisseaux, en la **simulant** par le modèle du **circuit
électrique** — résistance, puissances, immunité propre. Dans les **calculateurs analogiques**, on
incarne les opérations mathématiques en processus physiques : le flux du trafic routier sur les
routes ressemble à des outils que l'on s'est trouvé prendre **par hasard** pour contrôler un
vaste système de circulation. L'**économie théorique** nous donne à son tour une impression d'un
vaste système d'instructions pour fabriquer des modèles macro, méso et micro-économiques — par
exemple pour dessiner une image approchée d'une économie nationale, où entrent en jeu des
ensembles informes de consommateurs, salariés, producteurs, distributeurs, intermédiaires,
fournisseurs, exportateurs, investisseurs et détenteurs de revenus, et l'ensemble des individus
semblables et différents par leur nombre, leurs fonctions de production, de transformation, de
production de leurs biens et d'échange de la monnaie. Ce sont des **modèles que nous bâtissons et
manipulons de façon numérique** pour calculer les résultats d'une baisse ou d'une hausse
décisives de certains impôts et de certaines mesures financières ou économiques.

**الكاتب — هانز فرودونتال (1905—1990)** : رياضي ألماني. له مساهمات متميزة في علم الجبر وكتابات في
الفلسفة والأدب والتاريخ… من أهمّ كتاباته نذكر "أساسيات التربية الرياضية"…

**المهام** (verbatim) :

- أبيّن معنى أن تكون التقنية مصدرا لبناء نماذج.
- أفهم موجبات اتساع تطبيق النماذج في الحياة العملية للبشر.
- هل يسند هذا التطبيق المتّسع للنّماذج جهد المنظّرين في بناء النماذج وتنويعها؟
- أتساءل عن مخاطر ممكنة لإجرائيّة النماذج.
- أبحث حولي عن أمثلة تؤكد هذه الإجرائيّة وتبرز حدودها.

**Illustration** : p.237 portrait photo (noir et blanc) de Freudenthal.

⚠️ **Orthographe du nom** : le manuel écrit ici « **هانز فرودونتال** » ; au سند 13 (p.244) le même
auteur est nommé « **فرودنتال** » et le فهرس donne « فرويندتال ». Le nom latin imprimé est
`Hans FREUDENTHAL` dans les deux cas.

---

###### سند 10 — النمذجة للفهم — p.238–239

**التمهيد** (verbatim) :

> إذا كان من مستلزمات الإنسانية التوق إلى السمو، ومغادرة أشكال اليقين الحسي الزائف، فإنّه يصبح
> ضروريا على العقل أن لا يهدأ، فيتراءى تاريخه حمّال اكتشافات، وصانع مناهج ومبتكر رموز، كلّها
> نشاطات إذ تنأى به عن الطبيعة تمكّنه من إحكام السيطرة عليها.

**Référence imprimée** : جون لويس لوموانيو، البنائيّة —
`LE MOIGNE, Le constructivisme, éd L'Harmattan, 2002, T3, pp 11-13`.

**Points saillants du texte** (reformulés) : « **النمذجة للفهم** » — c'est ainsi qu'on peut tenir
à comprendre les expériences de nos relations au monde en les représentant par des **أنساق رمزية
اصطناعية**, des modèles que nous produisons et pratiquons, par lesquels nous démontrons et
échangeons des idées, et qui rendent **intelligible** l'aventure éblouissante de la connaissance
dans laquelle l'humanité s'est engagée depuis son origine. Cette aventure sans limites — la
transformation continue des expériences humaines en science, avec la conscience d'inventer des
expériences nouvelles — est « l'aventure hors du commun où s'est engagé le genre humain, s'y
éloignant peut-être des conditions premières de son espèce ». Pour cela l'auteur retient, avec
**بول فاليري**, « بإرادة الوضوح ونقاوة الفكر » par laquelle on perçoit les milliers de nuances
fines entre l'ombre et la lumière, sans briser, par l'impulsion de la domination aveugle, les
évidences claires et honnêtes. Nous sommes **familiers de ces exercices de modélisation** depuis
longtemps : nous ne percevons nos projets et ne comprenons nos conduites qu'à l'aide de modèles
symboliques — écriture musicale, rythme, écritures mathématiques, informatiques, chimiques.
L'astronome, le poète, l'ingénieur, le compositeur, l'ingénieur chimiste, l'architecte, le
biologiste, le sculpteur, le rythmicien et le mécanicien se réjouissent souvent de découvrir
qu'ils ont bien géré et qu'ils peuvent, dans le contexte de leur compréhension des modèles,
échanger et assimiler des phénomènes et des projets — ce qui les rend capables ensuite de faire
œuvre de raison dans leur domaine. Avec **ليونار دو فنشي** ils savent que « **النمذجة (التصميم)**
est une voie remarquable qui ne se borne pas à mettre en avant les réalisations de la nature,
mais qui en produit un nombre illimité et varié, et **dépasse la nature**, car les formes
fondamentales de celle-ci sont limitées alors que les œuvres réclamées par l'œil de la main de
l'homme sont sans limite ». Mais ce compagnonnage et ce partage cognitif des expériences **ne se
communiquent pas aisément** : dès que chacun se met à interpréter et transformer ces modèles, il
est conduit vers certaines formules fixes de compréhension du phénomène. L'un prétend détenir les
**critères universels** garantissant l'atteinte de la vérité finale supposée des régularités
intellectuelles autorisant ses interprétations — quitte à appauvrir son modèle par respect
excessif de ce critère méthodologique nommé « **الموضوعية العلمية** » ; l'autre s'intéresse à la
**garantie symbolique** de la singularité de ses projets idéologiques ou esthétiques qui
autorisent ses interprétations du modèle et prouvent qu'il est un modèle légitime. Ainsi se
confirme, à travers nos civilisations, une **scission quasi déclarée entre « les deux cultures »**,
que l'auteur regrette dans l'apparence tout en la trouvant admissible au fond, parce qu'elle
paraît justifier un partage relatif et pacifique des rôles sociaux entre **الإنسانيون ورجال
العلم**.

**الهامشان** (verbatim) :

1. **بول فاليري** `Paul Valéry` (1871—1945) : مفكّر فرنسي اهتمّ في مؤلّفاته بسيرورة المعرفة، كما
   اهتمّ بمشاكل العالم المعاصر.
2. **ليونار دو فنشي** `Léonard de Vinci` (1452—1519) : رسام ومعماري ونحّات وعالم إيطالي. اشتهر
   بلوحاته الفنيّة مثل ((الموناليزا)).

**الكاتب** (verbatim) : جون لويس لوموانيو : **انظر التعريف بالكاتب الوارد بالسند عدد 7 من المسألة
نفسها**.

**المهام** (verbatim) :

- أكشف عن التصوّر الذي يقدّمه الكاتب في بداية النص للنمذجة، وأستخلص تعريفا لها.
- بأي معنى يعتبر الكاتب النمذجة اصطناعا رمزيا انخرطت فيه الإنسانية منذ نشأتها ؟
- يمتدح الكاتب النمذجة، ويعتبرها مغامرة مُبهرة، أكشف عن مبررات ذلك.
- ما هي قيمة النمذجة وآثارها على مفهوم الحقيقة ؟
- يقيم الكاتب مقارنة بين مجال الطبيعة وما يجرى في ذهن الإنسان، أحدّد عناصر المقارنة وأستخلص قيمة
  ما يضيفه الإنسان من ابتكارات.
- يشير النص إلى "انشقاق" شبه معلن بين ((ثقافتين))، أكشف عن مبررات هذا الانشقاق وأنظر فيما إذا كان
  له من مبرر اليوم ؟
- هل النمذجة شأن خاص بالعلماء دون غيرهم من المبدعين؟ أعلّل جوابي.

**Illustration** : p.239 silhouette de tête humaine faite d'un circuit imprimé.

---

###### سند 11 — شروط صلاحية النموذج — p.240–241

⚠️ Pas d'encadré **الهامش** pour ce سند.

**التمهيد** (verbatim) :

> لئن كان اكتشاف الحقائق شغل العلوم الشاغل، فإنّ معرفة قوانين الطبيعة ترجع إلى ما يبتكره العقل،
> حتّى صار سيره على هذا الدّرب قدرا يؤثّث به حقول المعرفة العلمية بشبكات من الرموز مبهرة وعجيبة،
> لا لكونها تتناسب مع الواقع، بل لذهابها بعيدا على صعيد التجريد.

**Référence imprimée** : رونيه توم، أمثال وكوارث —
`René THOM, Paraboles et catastrophes ; éd. Flammarion, Paris, 1983, pp 521-621`
*(pagination reproduite telle qu'imprimée — vraisemblablement une coquille de la source)*.

**Points saillants du texte** (reformulés) : il est difficile d'expliquer ce que veut dire
**النموذج العلمي**. Nous nous trouvons devant une situation qui présente une propriété
**surprenante** pour l'observateur : elle évolue de façon imprévue, quelque chose s'y produit par
pur hasard, ou des facteurs y agissent de manière non objective — action à distance. On cherche
alors à maîtriser ces situations **à l'aide de la modélisation**, c'est-à-dire en construisant un
نسق — matériel **ou mental** — analogue à la situation naturelle de départ ; on formule sur le
modèle, par le biais de l'analogie, la question qui portait sur la situation naturelle, puis on
développe le modèle de manière à en obtenir une réponse. En appliquant l'analogie **en sens
inverse**, on obtient une réponse sur la situation naturelle, réponse qui affronte finalement les
données de l'expérience. La modélisation fournit donc **deux types de justification** :
**تبرير ماقبلي** (a priori) et **تبرير مابعدي** (a posteriori). La justification a priori exige une
théorie de l'analogie entre le système naturel et le modèle, alors même que la formulation d'une
telle théorie — ainsi de la **théorie des catastrophes** — n'est pas encore achevée ; dans
certains cas on peut néanmoins produire une justification de l'analogie (par la construction d'un
plan, par exemple, où l'on trouve une correspondance entre les données du plan et les données
réelles). Là où l'analogie entre situation naturelle et modèle est **scientifiquement fondée**, le
modèle est **justifié a priori**. La justification a posteriori, elle, consiste à confronter la
réponse du modèle aux données expérimentales. Or la caractéristique fondamentale de la science
contemporaine est, selon l'auteur, qu'elle **exige des expériences très coûteuses** : il faudrait
donc que les modèles proposés soient rigoureusement justifiés a priori, avant de s'aventurer dans
une expérimentation onéreuse, si la modélisation était bien construite. Mais les choses se passent
**en sens inverse** : la science contemporaine néglige pratiquement la justification a priori —
et là réside, dit l'auteur, l'une des causes de la **stérilité de la science contemporaine**,
stérilité qui s'entend comme le manquement des conceptions théoriques générales. Presque tous les
résultats obtenus étaient prévus d'avance ; d'où l'affirmation finale, qui « peut paraître
paradoxale » : **les modèles les plus coûteux et les moins soignés dans leur construction sont
ceux qui donnent les meilleurs résultats** — beaucoup de savants étant, selon lui, prêts à
convenir que la plupart des résultats importants et signifiants, jusque dans les disciplines les
plus expérimentales comme la biologie, ont été obtenus à partir d'expériences qui ne coûtaient
pratiquement rien.

**الكاتب — رونيه توم (1923 — 2002)** : فيلسوف وعالم رياضيات فرنسي، مثّل لقاؤه بعالم الرياضيات
**هنري كارتون** منعرجا حاسما في حياته، إذ كان هذا الأخير أحد مؤسسي جماعة ((بورباكي)) والتي أشرفت
على الأطروحة التي قدّمها سنة 1951. كشفت أبحاثه عن مسار جديد للرياضيات عُرف بنظرية الكوارث أو ما
يسمى ((رياضيات الكوارث)) ؛ بيّن توم ما تلعبه الكوارث في بناء العلم بمختلف تفرعاته وقطاعاته.

**المهام** (verbatim) :

- أتبين من خلال النص دلالة النمذجة العلمية.
- يقارن الكاتب بين نوعين من التبريرات تتوفر عليهما النمذجة، أحدّد خصائص كل منهما.
- ما هي شروط صلاحية نموذج ما ؟
- أي معنى أفهم من قول الكاتب (( إنّ النّماذج الأكثر كلفة والأقلّ جودة من ناحية البناء تعطي أفضل
  النتائج )) ؟ هل من مفارقة في هذا الحكم ؟
- أستخلص قيمة النمذجة العلميّة في علاقتها بمفهوم الحقيقة.

**Illustrations** : p.240 portrait peint de René Thom ; p.241 peinture d'un cabinet d'astronome
ancien (globes terrestre et céleste, lunette astronomique, cartes, sol en damier).

---

###### سند 12 — النشاط العلمي والنشاط التقني — p.242–243

⚠️ Pas d'encadré **الهامش** pour ce سند.

**التمهيد** (verbatim) :

> إذا كانت مسارات النمذجة في العلم تعبّر عن طابع كونيّ، فإنّ تحويل هذه المسارات إلى نماذج
> تطبيقيّة ينفتح بنا على مجال التنوّع والاختلاف والخصوصيّة.

**Référence imprimée** : جون لادريار، رهانات العقلانية —
`Jean LADRIERE, Les enjeux de la rationalité, Paris - Aubier 1977, p 63`.

**Points saillants du texte** (reformulés) : on peut comparer l'activité scientifique et l'activité
technique en usant du couple **معلومة — تنظيم** (information / organisation). L'**activité
scientifique** consiste à obtenir une information supplémentaire portant sur les systèmes
existants : elle convertit une information **objectivement réalisée sous forme organisée** en une
information **réalisée sous forme de représentations conceptuelles**. Il faut, dans certains cas,
convertir l'organisation en une information aux traits opératoires déterminés, entièrement soumise
à un principe quantitatif d'équivalence. L'intérêt d'une telle conversion est que l'information
conceptuelle est **libre et non incorporée** à un support sensible : n'étant fondue dans aucun
support déterminé, elle vaut pour **tout** support et peut être utilisée dans n'importe quelle
situation et pour n'importe quel type de donnée — bref, elle a une valeur « **كونية** ».
L'**activité technique**, au contraire, va **en sens inverse** : elle convertit une information
réalisée sous forme de **représentations mentales** (schémas, dessins de procédures ou règles de
procédure) en une information réalisée sous forme d'**organisation objective** — autrement dit
elle projette une information abstraite et libre sur un support sensible déterminé, qui accepte
par ce fait même une organisation supplémentaire. L'utilité de cette conversion tient à ce qu'elle
**ajoute aux systèmes naturels des systèmes artificiels** (ou donne aux systèmes naturels des
propriétés nouvelles et un caractère artificiel) : elle procure ainsi à l'action un support plus
large, plus varié, plus instrumental, la rendant capable d'effets quantitativement plus forts et
qualitativement plus variés. L'action se donne alors des fins croissantes en extension et en
distinction, et **renforce sensiblement son autonomie à l'égard du milieu naturel**.

**الكاتب — جون لادريار (1921)** : ابستمولوجي ومفكر بلجيكي، يعدّ خبيرا عالميّا في مجال إيتيقا العلم
والتكنولوجيا نظرا لثقافته الموسوعية التي تجمع بين العلم والفلسفة والتيولوجيا. عُرف بنقده لكلّ
العقلانية المطلقة والمنغلقة على نفسها، دون أن ينتهي إلى الإقرار بعجز الفكر عن إدراك الحقيقة؛ كما
اهتم بإبراز تأثير المنطق والرياضيات على الفكر المعاصر. من أهم مؤلفاته "تمفصل المعنى" (1984) — في
ثلاثة أجزاء —، "رهانات العقلانية" (1992)، "الإيتيقا في عالم العقلانية" (1997) و"العقيدة المسيحية
ومصير العقل" (2004).

**المهام** (verbatim, p.243) :

- يقارن الكاتب بين النشاط العلمي والنشاط التقني، أفهم هذه المقارنة وأحدّد مستوياتها.
- أحدد خصائص النشاط العلمي.
- مثلما أن العلم نظام من المعلومات، فإنّ التقنية نشاط تنظيمي لتلك المعلومات : كيف أفهم هذه
  العلاقة؟
- النشاط العلمي بوصفه نسقا من المعلومات يكتسي قيمة كونية، أفسّر ذلك.
- إذا كانت المعلومة العلمية ذاتها قيمة نظرية كونية، فما هي قيمة التنظيم التقني لتلك المعلومة؟

**Illustrations** : p.242 portrait photo de Ladrière ; p.243 gravure ancienne — un savant debout
dans son atelier, entre une presse et des machines à roues.

---

###### سند 13 — النمذجة إجراء منهجيّ — p.244

⚠️ **Sur une seule page** : تمهيد + texte + الكاتب (renvoi) + المهام, sans encadré des هوامش.

**التمهيد** (verbatim) :

> لا أحد ينكر اليوم الكثافة الجدالية حول الاقتصاد في مجالات متنوعة، جدال قد يكون عقيما ما لم
> يُدرج في الحسبان اقتصاد مهمّ، هو الاقتصاد في التفكير والتعبير باعتباره جذر كلّ مشروع علمي.
> إذّاك تكون النمذجة إجراء منهجيّا لازما لكلّ علم.

**Référence imprimée** : هانز فرودنتال، مخاطر هيمنة مفرطة لعلم التركيب على علم الدلالة في العلوم
الراهنة —
`Hans FREUDENTHAL, Colloque : Dangers d'une prédominance abusive du syntaxe sur la sémantique dans
les sciences actuelles ; Paris 1978, p161`.

**Points saillants du texte** (reformulés) : des **modèles matériels** — du type des mouvements
des planètes — aux **modèles théoriques** des sciences naturelles et de l'économie, le modèle est
toujours resté l'image approchée ou exacte, simplifiée et réduite, d'une réalité physique,
biologique ou sociale. Or dans la **théorie des modèles**, la relation entre le modèle et la chose
qu'il représente paraît **inversée** (علاقة عكسيّة). D'où vient ce renversement ? De ce que le
modèle est une **description précise de quelque chose** : parlons du modèle de la **géométrie
non-euclidienne** — c'est une réalité platonicienne. Nous avons pris l'habitude, un siècle durant,
de décrire ce genre de faits platoniciens par des **outils implicites** et des **systèmes
axiomatiques**, et nous avons fini par faire coïncider cette réalité avec sa description
axiomatique. Cette dernière étape, naturelle pour nous en tant que mathématiciens, est la cause de
ce que l'auteur nomme le **الارتداد الدّلالي** (renversement sémantique). Le modèle euclidien de
la géométrie non-euclidienne ne semble donc pas très différent du **modèle planétaire de
l'atome** ; sauf qu'un modèle euclidien d'un système axiomatique a une **résonance autre** : dans
le premier cas le modèle sert à **contrôler théoriquement** une réalité donnée, dans le second il
sert à **remplir une structure théorique d'un contenu plus réel**.

**الكاتب** (verbatim) : هانز فرودنتال : **انظر التعريف بالكاتب الوارد بالسند عدد 9 من المسألة
نفسها**.

**المهام** (verbatim) :

- أتبيّن دلالة النموذج من خلال النص وأقدم صورا له من سجلات مختلفة.
- أكشف عن العلاقة بين النموذج والشيء الذي يمثله. أستثمر نماذج من الهندسة.
- يتحدث الكاتب عن علاقة بين النموذج والأكسمة، أكشف عن هذه العلاقة.
- يتحدث الكاتب عن حالتين لصلاحية النموذج، أحدّدهما وأتبيّن الاختلاف بينهما.
- فيم تكمن القيمة العلمية للنموذج ؟

**Illustrations** : p.244 portrait photo (noir et blanc) de Freudenthal ; vignette d'un **atome
stylisé** (noyau + électrons sur orbites) accolée aux المهام — illustration du « نموذج كوكبي
للذرّة » évoqué dans le texte.

---

###### سند 14 — النمذجة وسؤال المعنى — p.245–246

**التمهيد** (verbatim) :

> يحرص العقل العلمي على إنشاء النّماذج حرصه على تفسير الواقع وصفا واختزالا، ضمن عمليّة تحوّل هذا
> الواقع ذاته إلى كيان من كياناته. ومع هذا، يحصل أن يذهل العلماء عن الكشف عمّا تنشدّ إليه هذه
> العمليّات من غايات، تنكّرا منهم لصامت يوجّههم في صمته أو لتقليد تفاخروا يوما بالقطع معه. قد
> نجرأ، إذن، على التظنّن على عملهم رغبة منّا في إنقاذ "نمذجة" نريدها ذات دلالة وفي استعادة واقع
> نريده ذا معنى.

**Référence imprimée** : جون لويس لوموانيو، البنائيّة —
`LE MOIGNE, Le constructivisme, éd L'Harmattan, 2002 T2, pp 311- 312 - 313`.

⚠️ **Forme du سند** : le texte est un **échange à deux voix** typographiquement marqué — un premier
bloc attribué à **آلان فانفلي** (Alain Finféli), un second introduit par **جون لويس لوموانيو**.

**Points saillants du texte** (reformulés) :

- **آلان فانفلي** : le questionnement **téléologique** porte sur la fonction des modèles — par qui
  ils sont bâtis et pour quelles fins. C'est entendu ; mais la **النمذجة النسقيّة** (modélisation
  systémique) ne devrait-elle pas s'obliger à inclure dans son parcours **les fins du modélisateur
  lui-même** ? car celui-ci, s'il a bien compris la leçon, ne peut en aucun cas se tenir pour
  extérieur au modèle qu'il est en train de construire. La **نظريّة الأنساق العامّة** (`TSG`)
  possède-t-elle les ressources suffisantes pour cerner **le problème éthique** sans recourir à la
  neutralité traditionnelle de la science ? Enfin, si la modélisation systémique ne répond que
  mal à la question éthique (« René Thom n'a réussi à la formuler que de mauvaise façon »), elle
  paraît se soutenir d'une **autre science oubliée de la philosophie : l'esthétique** — car toute
  construction débouche sur une **forme**, d'où le problème central du rapport
  **الشكل/المضمون** pour le jugement esthétique. Nous voilà ainsi ramenés à la **question du
  sens**, que **رونيه توم** a mise en lumière avec brio — mais qui ne représente ici, elle aussi,
  qu'une hypothèse de travail.
- **جون لويس لوموانيو** : ne devons-nous pas d'abord nous étonner de ce caractère nouveau et
  difficile — pour nos cultures contemporaines — des questions que soulève notre mémoire limitée
  en **إيتيقا، غائيّة، إستيتيقا، هرمينوطيقا** ? Ce sont des questions qui conduisent toutes nos
  capacités collectives vers « **إنشاء معنى** ». Et l'objection la plus importante qu'on puisse
  opposer aux tendances **positivistes** dans leur ambition folle de simplification (« pour
  expliquer, nous devons réduire à l'expression la plus simple ») — ambition qui a failli nous
  faire oublier que le projet de la science est la connaissance de la sagesse — c'est cette
  **étonnante capacité à produire du sens**, capacité qui excède la description tout en nous étant
  familière, et qui s'accomplit par le **traitement intentionnel et intelligent des symboles** ; le
  symbole, cet artefact **le plus complexe absolument** que l'homme ait conçu et construit.

**الهوامش** (verbatim, p.246) :

1. **آلان فانفلي** `Alain Finféli` : كاتب ورئيس تحرير مجلّة `Informel`
2. **النظريّة العامّة للأنساق** `TSG` : هيّ [sic] نظريّة النمذجة، وتتمثّل في بناء تصوّر أو تصوّرات
   قصد بناء معرفة تربط بين المعارف والأفعال. وهي عبارة مرادفة "للنمذجة النسقيّة"
3. **رونيه توم** `René THOM` : انظر التعريف الوارد بالسند عدد 11 من هذه المسألة.

**الكاتب** (verbatim, p.245) : لوموانيو : **انظر التعريف بالكاتب الوارد بالسند عدد 7 من المسألة
نفسها**.

**المهام** (verbatim, p.246) :

- أستثمر مكتسباتي وأحدّد ملامح النموذج وخصائص تمشياته.
- أحدد وظيفة النموذج وغايته.
- كيف أفهم ربط الكاتب بين النمذجة والفلسفة كما تتجلّى في الاستيتيقا والإيتيقا والهرمونيتيقا ؟
- هل يمكن أن نعزل غايات المنمذج عن غايات النموذج ؟
- المعنى إنشاء، والنمذجة إنشاء : بأي معنى أفهم التقارب بينهما بوصفه اعتراضا يُصاغ ضد الوضعية ؟

**Encadré-citation (p.246)** : « لكي نفسر علينا أن نختزل في أبسط عبارة » — **لوموانيو**.

**Illustrations** : p.245 portrait photo d'un homme âgé devant un micro ; p.246 photographie d'une
main traçant au stylo technique un schéma (cercle et segments) sur un plan.

---

###### سند 15 — حدود النموذج الميكانيكي — p.247–248

**التمهيد** (verbatim) :

> قد يبدو للبعض أنّ بناء النظريّة الفيزيائيّة لا يمثّل إلاّ تتويجا لعمليّة وصف الظّواهر الواقعيّة
> واختبارها، ممّا يجعل من الوقائع المصدر الأساسي للفكر الفيزيائي. غير أنّ حقيقة النظريّة بالنسبة
> إلى الفيزيائيين تنبني على أسس تخيّليّة وافتراضيّة، هي التي تسمح بإنشاء صور ونماذج للواقع تعبّر
> عن مظاهر تطوّر العلم.

**Référence imprimée** : بيار دوهام، النظريّة الفيزيائيّة: موضوعها وبنيتها —
`Pierre DUHEM, La théorie physique : son objet et sa structure, éd. Vrin 1989, pp 143 - 144`.

**Points saillants du texte** (reformulés) : si l'on évite d'attribuer aux **modèles** des
découvertes qui procèdent en réalité des **théories abstraites**, et si l'on se garde de confondre
l'usage des modèles avec l'usage de l'**analogie** (المماثلة), quelle part revient aux théories
**imaginatives** dans les progrès de la physique ? Une part qui « nous paraît bien assez faible ».
Le physicien **Lord Kelvin**, célèbre pour n'accorder d'intelligence rationnelle à une théorie que
s'il en voyait un modèle, doit ses plus belles découvertes — conduction électrique de la chaleur,
propriétés des courants variables, lois de la décharge des charges électriques oscillantes, et
bien d'autres phénomènes — aux **systèmes abstraits** de la thermodynamique et de
l'électrodynamique classiques ; chaque fois qu'il recourt aux modèles mécaniques, il se borne à
**exposer des résultats déjà obtenus**, sans être en train d'inventer. De même, le modèle des
actions électrostatiques et électromagnétiques formulé dans le mémoire « **في المسار الفيزيائي
للقوّة** » n'a pas aidé **Maxwell** à inventer la théorie électromagnétique de la lumière : il
s'est sans doute efforcé de tirer ce modèle des deux formulations fondamentales de cette théorie,
mais cette méthode même a fini par montrer que les résultats prétendument obtenus lui étaient déjà
connus par ailleurs, et le désir de les retrouver l'a conduit jusqu'à **falsifier** l'une des
formulations fondamentales. Maxwell n'a pu établir la théorie qu'il visait qu'en **renonçant à
tout modèle** et en étendant, par la voie de l'analogie, le système abstrait de l'électrodynamique
aux **courants de déplacement**. Conclusion : l'usage **intentionnel** des modèles mécaniques
figurés qu'on prête aujourd'hui à la physique n'est démontré que dans les travaux de **Lord
Kelvin**, et non dans ceux de **Maxwell**.

**الهامشان** (verbatim) :

1. **اللورد كالفن** `Lord KELVIN` (1824—1907) : فيزيائي انجليزي، له أعمال هامّة في التيرمو —
   ديناميكا. أكتشف [sic] مفهوم تكافؤ عدد الذرّات، وأكتشف [sic] أيضا نظرية التحليل الطيفي.
2. **ماكسوال** `Maxwel` [sic — lire `Maxwell`] (1831—1879) فيزيائي انجليزي مكتشف سلسلة من المعادلات
   التي تلخّص كلّ خاصيات موجات الألكترو — مغناطيسية. له أيضا إسهامات في النظرية الحركية للغاز.

**الكاتب — بيار دوهام (1861 — 1916)** : فيزيائي وإبستيمولوجي فرنسي. عُرف بمعارضته للتفسيرات
الماديّة والواقعيّة في الفيزياء وبدفاعه عن تصوّر أداتي للعلم ووظيفته التوقّع. من أهمّ مؤلّفاته :
"نظريات الحرارة" (1895)، "تطوّر الميكانيكا" (1902)، "مصادر الستاتيكا" (1903)، "النظريّة
الفيزيائيّة : موضوعها وبنيتها" (1906)، "مقالة تتعلّق بمفهوم النظريّة الفيزيائيّة من أفلاطون إلى
غاليلي" (1908)، "نسق العالم" (1913).

**المهام** (verbatim) :

- ما المقصود من السؤال الذي طرحه الكاتب في بداية النص؟
- هل من فارق بين النموذج والنظرية؟ أعلل جوابي من خلال أمثلة من الفيزياء.
- يعتبر الكاتب أن اللّجوء إلى النموذج ليس فيه اختراع، بأي معنى أفهم هذا الموقف ؟
- النموذج والنظرية: أية علاقة لهما بالحقيقة العلميّة؟
- أستخلص من النص عيوب النموذج بالاعتماد على أمثلة من الفيزياء.

**Illustrations** : p.247 portrait photo ancien (noir et blanc) de Duhem ; p.248 photographie d'une
**sphère armillaire** dorée sur pied sculpté.

---

###### سند 16 — قيمة النماذج — p.249–250

⚠️ Pas d'encadré **الهامش** pour ce سند ; les **المهام** sont imprimées sur la page suivante
(p.250), qui **clôt la نافذة سندات** de ce مبحث.

**التمهيد** (verbatim) :

> لا أحد ينكر اليوم قيمة الابتكارات الكثيرة والمتنوعة للعقل البشرى [sic]، ابتكارات يغذيها هوس
> بالحقيقة العلمية سبيلا لمزيد السيطرة والتحكّم في الطبيعة، ويبدو أن قوّة الذكاء البشري بلغت حدّا
> أصبح معه ممكنا ترجمة الرموز واقعياً، وصياغة الواقع رمزيا.

**Référence imprimée** *(traduction arabe — pas de titre latin imprimé)* : ر.بلانشي، الأكسيومية أو
منظومة الأوليات — ترجمة محمود بن جماعة، دار محمد علي للنشر 2004، ص 101.

**Points saillants du texte** (reformulés) : les physiciens se divisent, comme il a été rappelé,
sur la valeur respective des **théories abstraites** et des **théories représentées par des
images** : les esprits diffèrent en capacités, l'un excellant à **lire l'abstrait dans le
concret**, l'autre à **l'interpréter par le concret**. Mais de même qu'une différence de
température est nécessaire pour qu'une machine thermique fonctionne, de même l'esprit doit, pour
comprendre, **changer de niveau de regard** et se mouvoir entre deux plans : s'élever du fait à
l'idée, puis redescendre de l'idée au fait. Dégager la règle et l'incarner dans un exemple : tel
est le **mouvement redoublé** où se résume toute connaissance, et dont l'**axiomatique**
(الأكسيومية) nous donne une détermination — l'un des exemples où la règle se saisit le mieux.
Ainsi voit-on quelles positions philosophiques l'axiomatique **contredit** et lesquelles elle
**soutient** : elle refuse la **وثوقيّة التركيب** (dogmatisme de la synthèse) et le rêve d'un point
de départ absolu qui garantirait à la déduction une certitude définitive ; elle **généralise
aujourd'hui la forme hypothético-déductive** à la science tout entière. Et de même que la méthode
expérimentale a ruiné la confiance dans le rêve **cartésien** d'une physique démonstrative, de même
le **logicisme** — l'idée d'une science rationnelle qui ne présupposerait plus rien — se trouve
démenti par le **recul axiomatique** (التراجع الأكسيومي), qui trouve toujours devant lui un
« سابق » non résorbé, si loin qu'il remonte. Mais surtout : les **أوليّات** ne s'imposent pas en
vertu d'une évidence intérieure, et pourtant elles **ne résultent pas de décisions arbitraires** ;
seul défend le **conventionnalisme** (المواضعيّة), semble-t-il, celui qui sépare artificiellement
l'axiomatique de ses **fondements et de ses prolongements intuitifs** — sans lesquels l'axiomatique
devient « un jeu vain, sans relation avec la science ».

**الكاتب — ر.بلانشي `Robert BLANCHÉ` (1898 — 1975)** : ابستيمولوجي فرنسي، كان أستاذا شرفيا بجامعة
تولوز، عُرف خاصّة بأعماله في المنطق الرّياضي وبمؤلّفاته المُيَسِّرة حول المنطق والإبستيمولوجيا، كما
أكّد على ضرورة عدم الفصل بين دراسة العلوم الصوريّة ومشكلة المعرفة في الفلسفة. من أهم مؤلّفاته :
"العلم الفيزيائي والواقع، المواقف المثاليّة" (1949)، "الأكسيومية أو منظومة الأوليات" (1955)،
"مقدّمة إلى المنطق المعاصر" (1957)، "العلم الراهن والعقلانية" (1967)، "المنطق وتاريخه من أرسطو
إلى راسل" (1970) و"الإبستيمولوجيا" (1972)،

**المهام** (verbatim, p.250) :

- أحدّد الفرق بين النظريّات المجرّدة والنظريّات الممثّلة بصور. أستخلص قيمة كل منهما.
- أكشف عن دلالة العلاقة الجدلية بين الفكرة والواقعة وأستخلص القيمة العلمية للنظرية.
- هل في ابتكار نماذج نظرية مجرّدة ابتعاد عن الواقع أم مزيد من السيطرة عليه؟
- يتحدث الكاتب عن شكل فرضي — استنتاجي يعمّم الآن على العلم بأكمله. أكشف عن دلالة هذا الشكل
  وأتبيّن قيمته العلمية. أوظف أمثلة على ذلك.
- أيّة صورة للحقيقة العلميّة في ضوء الثورة الأكسيومية؟
- متى تصبح الأكسيومية لهوا باطلا، ومن غير علاقات بالعلم؟

**Encadré-question (p.250)** : « متى تصبح الأكسيوميّة لهوا باطلا ؟ »

**Illustration** : p.250 image de synthèse — une **main en fil de fer** (wireframe orange/magenta)
au-dessus d'une **sphère wireframe**.

---

###### Bornes de scope (tranche p.227–250)

- ✅ **INCLUS** : les 13 سندات n° **4 à 16** de la نافذة **سندات للتفكير في المسألة** du
  **مبحث 2 — العلم بين الحقيقة والنمذجة**, avec pour chacun : le **تمهيد verbatim**, la référence
  bibliographique telle qu'imprimée, la thèse reformulée, les **هوامش**, la **notice d'auteur** et
  les **مهامّ verbatim**, ainsi que les encadrés-citation et les illustrations.
- ⛔ **EXCLU** (hors de cette tranche) : la page d'ouverture du مبحث (p.215), la
  **نافذة مدخل** (p.216–219), la page de titre de la نافذة سندات et les **سندات 1 à 3**
  (p.220–226) — traités par ailleurs dans cette fiche ; et **tout ce qui suit p.250**
  (نافذة دعائم / تحديدات وتمييزات مفهوميّة, سياقات فكريّة, كيفيّات التفكير, نصّ مطوّل, مختصرات).
- ⛔ **NON PRODUIT** : aucun QCM, aucune question, aucun exercice — ce lot est une transcription.

###### Renvois internes imprimés (à conserver pour la génération)

| Depuis | Vers | Nature |
| --- | --- | --- |
| سند 5, هامش 1 + dernière مهمّة (p.229–230) | نافذة **سياقات فكريّة**, entrée **السيبارنيطيقا** | « (انظر سياقات فكريّة) » |
| سند 10, encadré الكاتب (p.239) | **سند 7** (même مسألة) | notice d'auteur non répétée (Le Moigne) |
| سند 13, encadré الكاتب (p.244) | **سند 9** (même مسألة) | notice d'auteur non répétée (Freudenthal) |
| سند 14, encadré الكاتب (p.245) | **سند 7** (même مسألة) | notice d'auteur non répétée (Le Moigne) |
| سند 14, هامش 3 (p.246) | **سند 11** (même مسألة) | notice d'auteur non répétée (René Thom) |

###### Terminologie officielle relevée dans la tranche (couple arabe / latin quand il est imprimé)

- **النمذجة** — *(modélisation)*, **النموذج** — le manuel oppose النموذج à النظريّة (سند 6),
  à البنية (سند 5), à الاستعارة (سند 8), à الأكسمة (سند 13).
- **أنساق الرموز / الأنساق الرمزيّة (الفيزيائيّة)** — systèmes de symboles (سند 4, سند 10).
- **الصورنة** (سند 5) ; **النموذج التحكّمي** = السيبارنيطيقا `Cybernétique`, `control`,
  `communication` (سند 5, هامش).
- **التأمثل** `idéalisation` (سند 6) ; **المفترضات الأنطولوجيّة** (سند 6).
- **تغيير الشّفرات** (سند 7) ; **إستراتيجيا الإهمال** (سند 8) ; **نموذج الخميرة** `allostérie`
  (سند 8, هامش 3).
- **التبرير الماقبلي / التبرير المابعدي** (سند 11) ; **صلاحيّة النموذج** (سند 11).
- **معلومة — تنظيم**, **قيمة كونيّة**, **الأنساق الاصطناعيّة** (سند 12).
- **الارتداد الدّلالي**, **الأنساق الأكسيوميّة**, **الهندسة اللاإقليديّة**, **النموذج الكوكبي
  للذرّة** (سند 13).
- **النمذجة النسقيّة** = **النظريّة العامّة للأنساق** `TSG` (سند 14, هامش 2) ; **إنشاء معنى**,
  **الإستيتيقا / الإيتيقا / الهرمينوطيقا** (سند 14).
- **المماثلة** (analogie), **تيارات التنقّل** (courants de déplacement) (سند 15).
- **الأكسيوميّة**, **الأوليّات**, **الشكل الفرضي — الاستنتاجي**, **التراجع الأكسيومي**,
  **المواضعيّة** (سند 16).

###### Incertitudes

- **p.228, dernière مهمّة** : imprimé « الحواسيب قد نقلت **الأنساق العلامات** من الفردوس
  الأفلاطوني للمثل… » — tournure fautive de la source (lire vraisemblablement « أنساق العلامات »).
  Lecture confirmée sur un rendu 300 dpi ; transcrite telle quelle avec `[sic]`.
- **p.231, هامش 1** : le nom latin est imprimé `Van Frassen` (pour `Van Fraassen`) et la date
  donnée est « معاصر (1969) » — reproduit tel quel.
- **p.241, référence** : imprimée `pp 521-621`. Pagination invraisemblable pour un ouvrage de
  Flammarion ; lecture **confirmée** sur rendu 300 dpi — c'est une coquille de la source, pas une
  erreur de transcription.
- **Nom de Freudenthal** : le manuel l'écrit « **فرودونتال** » (سند 9, p.237) et
  « **فرودنتال** » (سند 13, p.244) ; le فهرس, lui, donne « فرويندتال ». Trois graphies pour un
  seul auteur, `Hans FREUDENTHAL` en latin dans les deux سندات.
- **p.248, هامش 2** : le nom latin est imprimé `Maxwel` (un seul `l`) et les deux verbes du
  هامش 1 sont imprimés « أكتشف » (hamza de coupure) au lieu de « اكتشف » — reproduits tels quels.
- **p.249, تمهيد** : imprimé « للعقل البشرى » (yāʾ sans points en finale) au lieu de « البشري ».
- **p.245** : l'identité de la personne photographiée n'est **pas** légendée ; le texte étant à
  deux voix (فانفلي / لوموانيو), l'attribution du portrait n'est pas déterminable. `[?]`
- **p.246, هامش 2** : imprimé « **هيّ** نظريّة النمذجة » (au lieu de « هي ») — reproduit tel quel.

##### 2.3 نافذة دعائم للتفكير في المسألة — p.251-259

> **Pages lues** : p.251–259 (intégral). **Source** : manuel élève `210402`, مبحث 2 « العلم بين الحقيقة والنمذجة ».

**p.251 — page d'ouverture de la نافذة.** Image : une pile de livres reliés rouge avec une paire
de lunettes posée dessus, sur fond de feuillage. Encadré-citation (verbatim) :

> « لقد فهمنا على أي حال، أنّه ليس كافيا بالنسبة إلى الفرد الذي اتخذ التقدّم التكنولوجي أو
> العلمي واجبا له، أن يفكّر فقط في هذا الواجب. بل عليه أن يراه كجزء من تطوّر أكبر يوافق عليه.
> بمجرّد اتّخاذه لهذا الواجب. »
> — هيزنبرغ، *الجزء والكلّ*

Sommaire imprimé en bas de page (deux entrées numérotées) : **1 — تحديدات وتمييزات مفهوميّة**
· **2 — سياقات فكريّة**.

---

###### 2.3.1 تحديدات وتمييزات مفهوميّة — p.252-255

Deux concepts seulement sont définis dans cette نافذة : **الواقع** (p.252-253) et **البراديغم**
(p.254-255). Chacun suit le même gabarit en trois entrées — **لغة** / **اصطلاحا** /
**فلسفيا وإبستمولوجيا** — puis une rubrique **« قيل في … »** (florilège de citations attribuées).

**1 — الواقع · `La Réalité` — p.252-253**

**■ لغة (verbatim)** :

> « الواقع » يحيل إلى **الواقعي** بوصفه الشيء الموجود بالفعل ويقابله **الاعتباري** الذي لا وجود
> له، أو هو ما يكون شيئا أو ما يختص بالأشياء، كما يقال أيضا في مقابل **الظاهر** و**الوهمي**
> و**الخيالي**.

*Distinctions posées ici* : الواقعي ≠ الاعتباري · الواقعي ≠ الظاهر · ≠ الوهمي · ≠ الخيالي.

**■ اصطلاحا (verbatim)** :

> يقال « واقعي » في نظام التمثلات على ما يكون **راهنا أو معطى**، كما يقال بالتقابل إمّا مع
> **الممكن** بحيث يفيد الواقعي الأشياء **كما هي، لا كما يمكنها أن تكون أو كما ينبغي أن تكون**،
> ويُقال أيضا بالتعارض مع **صورة المعرفة** أي ما يشكّل **مادة المعرفة** بوصفه مضمونا وضعيا.

*Distinctions posées ici* : الواقعي ≠ الممكن (l'être ≠ le possible ≠ le devoir-être) ·
مادة المعرفة ≠ صورة المعرفة.

**■ فلسفيا وإبستمولوجيا (verbatim, resserré sur les articulations)** :

> يفيد **الواقعي** معنى يتعلّق بفكرة الشيء بوصفه غرضا فكريا، فهو **الرّاهن والمعطى** ويشمل مادة
> المعرفة كلّها، كما يتعلّق بفكرة الشيء لكن بالمعنى التام لهذه الكلمة أي ما يشكّل **موضوعا
> محدّدا، منطقيا وله استقلاليّة معيّنة**، وهذا الشيء الواقعي يمكن تصوّره باعتباره **مظهرا
> كلّيا، أي ملازما للتمثّل**. إذ تفيد عبارة **تمثّل** في المقام الأول **حضور صورة لها معنى**،
> ويقدّم مضمون الصورة وجها آخر للموضوع أو للحدث يتحقق بواسطة تجربة فعلية.

Suite de l'entrée (p.252, colonne de gauche) — la thèse épistémologique centrale du chapitre :

- إنشاء التمثّلات **لا يقتضي ضرورة استحضار الصور المعطاة أو المستوحاة من الواقع المباشر** ; ما
  يمثّله **المفهوم العلمي** هو الواقع en tant qu'il contient l'idée non seulement d'un état
  actuel (**حالة راهنة**) mais aussi d'un état **لا راهنيّة له** qui participe pourtant à la
  figuration du réel.
- « **تصوّرا علميا لا يصوّر فقط ما هو كائن وإنّما يتخيّل ما يمكن أن يكون** » ; d'où :
  **المعرفة العلميّة = القدرة على استنتاج حالة واقعية من موضوع تفكير أو تعقّل** — « وهو ما يعني
  أنّ **الواقع العلمي منشأ أو مبني وليس معطى** ».
- **باشلار** — règle citée verbatim par le manuel :
  > « في كل الأحوال ينبغي على **المعطى** أن يترك المكان **للمنشأ** »

  et son corollaire, énoncé **بالتضاد مع التصوّر التقليدي للاكتشاف العلمي** :
  **« أنّ ظاهرة ما معروفة علميا لا تُكتشف وإنّما تُنتج »**.
- Ce **التصور البنائي للعلم** ne produit pas seulement un soupçon sur la **النزعة الواقعية في
  العلم** : il conduit à dire que **« العلم لا يعترف إلاّ بما هو مبني »**.
- **Rapport à Kant** : si **الكانطية** concevait la connaissance comme **تنظيم للبعدي عن طريق
  الماقبلي**, la conception contemporaine *approfondit* Kant tout en dépassant deux points de sa
  théorie — (1) que les **المبادئ القبلية** seraient insusceptibles de critique ou de révision,
  (2) qu'elles auraient une existence indépendante de toute intervention créatrice humaine
  (« فهي بالتالي لا تنشأ وإنّما لها وجود موضوعي وتفرض على كلّ العقول »). Justification prise à
  l'histoire des sciences : **مبدأ الحتمية** ayant buté sur son inapplicabilité au domaine
  **الميكروفيزيائي**, ce que Kant tenait pour principe nécessaire de toute connaissance est
  devenu **مجرّد فرضية**.
- Conclusion de bascule (p.252→253) : le concept de réel **n'a longtemps pas fait problème pour
  la science** ; il **est devenu un problème épistémologique avec la science contemporaine** —
  et ce n'est pas à entendre en un sens négatif, la rupture avec l'ancienne conception ayant
  **libéré la pensée d'illusions anciennes**.

**Le couple qui porte tout le chapitre (p.253, verbatim)** :

> فإذا كنّا … نفهم **الوضعي** على معنى **الواقعي** في مقابل **الوهمي**، بحيث ينكشف أمام أنظارنا
> نظام الواقع ويكون معيار علمية كشوفاتنا هو **تطابق النظرية مع الواقع**، فقد مكّننا **الدرس
> الباشلاردي** من إدراك أنّ **العلم لا ينطلق من الواقع وإنّما يتجه إليه**، مثلما أدركنا مع
> **الإبستمولوجيا البنائية** أنّ **الحقائق ليست كنوزا تكتشف بل أبنية تشيد عبر النماذج**.

**Définition du نموذج donnée ici (p.253, verbatim)** — c'est la définition officielle du modèle
dans ce chapitre :

> ويحيل فيها **النموذج** **لا على معنى المثل الأعلى الذي ينبغي محاكاته** وإنما على معنى **نسق
> الرموز الخطية أو الوصفية أو الرياضية أو الصورية المبسّطة والمرنة** والتي من خلالها نصف
> **موضوعا ملاحظا أو متخيلا أو افتراضيا** (موضوعا ينتمي إلى **واقع افتراضي**) عبر نسق من
> الترقيمات الرياضية أو الموسيقية وعبر إنشاء تمثلات **لا تدّعي لنفسها الكمال ولا الشمولية**، إذ
> لا يوجد نموذج يدعي قدرة على استيعاب العالم في كليّته.

⇒ **Distinction explicite : النموذج ≠ المثل الأعلى (modèle-à-imiter)**, et **tout modèle a des
limites**. Analogie imprimée, attribuée à **كارل بوبار** : le modèle est **شبكة صيد** — un filet
qui attrape certains poissons et en laisse d'autres passer, ou n'a pas la capacité de tous les
embrasser.

**■ قيل في الواقع (p.253, verbatim, 4 citations)** :

| Auteur (tel qu'imprimé) | Citation |
| --- | --- |
| **رسّل** | « إنّنا ننطلق جميعا من **الواقعية السّاذجة**، أي من المذهب الذي يقرّر أنّ الأشياء هي على ما تبدو عليه… إنّ الواقعية السّاذجة تقود إلى الفيزياء، بينما تثبت الفيزياء، إذا كانت صحيحة، أنّ الواقعية السّاذجة **باطلة** ». |
| **كانط** | « لا يحتوي **الواقع** على شيء أكثر من **الممكن** ». |
| **بشلار** | « **الواقع لا يشار إليه، وإنّما يبرهن عليه** ». |
| **بول فاليري** | « لقد بحثنا طويلا عن **تفسيرات** في حين تعلّق الأمر **بتمثلات** نقدر فقط على محاولة خلقها ». |

**Encadré-image p.253** (photo : têtes de pierre bleutées, pièces de puzzle qui s'envolent,
une flamme) — légende verbatim : **« الواقع تركيب ذهني »**.

**2 — البراديغم · `Paradigme` — p.254-255**

**■ لغة (verbatim)** :

> يُرَدُّ لفظ **البراديغم** إلى عبارة `Paradigme` اليونانية الأصل والتي تفيد **النموذج أو
> المثال** أمّا في اللغة اللاّتينية فيفيد **البرهنة**.

**■ اصطلاحا (verbatim, hors champ scientifique)** :

> خارج المجال العلمي، يستخدم لفظ **براديغم** في معنى **إدراك العالم**، كما يفيد وصف **مجموع
> التجارب والمعتقدات والقيم** التي تؤثر على طريقة رؤية الفرد إلى الواقع، إذ يسمح له هذا النظام
> من التمثلات من **تعريف العالم** الذي يحيط به **والتواصل معه** بل حتّى **فهمه أو توقعه**…
> كما يفيد **البراديغم** في المعنى الجمعي **نسقا من التمثلات مقبولة في ميدان معين**، وهو ما
> يعني أن **البراديغمات تختلف بحسب المجموعات وتتغير في الزمن بحكم تطور المعارف**.

Le manuel ajoute que le paradigme est **مجديا بالنسبة إلى ملاحظ لمستخدم هذا البراديغم** : il
permet de montrer comment l'observateur traite les données du paradigme.

**■ فلسفيا وإبستمولوجيا (verbatim resserré)** :

> يحيل **البراديغم** على معنى **تمثل للعالم**، و**طريقة في النظر إلى الأشياء**، و**نموذجا
> متناسقا في رؤية العالم يستند على جملة مبادئ** (قواعد سلوكية أو نموذج نظريّ أو تيّار فكري).

Repères historiques et d'usage imprimés :

- Le terme est employé **في بداية القرن التاسع عشر** comme terme épistémologique pour dire
  **نموذج فكري في القطاعات العلمية**.
- L'usage **le plus répandu** est celui du philosophe et sociologue de la connaissance
  **توماس كوهن** : **مجموع التطبيقات العلمية** ; synonyme employé pour le même sens :
  **العلم النموذجي**.
- **Définition de Kuhn retenue par le manuel (verbatim)** : le paradigme est
  **« مجموع الملاحظات والأحداث المتحققة، ومجموع الأسئلة التي تتصل بالإنسان والتي ينبغي أن تطرح
  ويجب أن تجد الحلول الملائمة »**, et il comporte **توجيهات منهجية** qui fixent **كيفية طرح تلك
  الأسئلة وكيفية تأويل نتائج البحث العلمي**.
- **Dimension sociale** : l'appartenance à un paradigme est, selon Kuhn, **ظاهرة اجتماعية** —
  une **جماعة فكرية** se constitue autour d'une méthode, d'objectifs et de **وسائل مشتركة**
  (صحف، محاضرات…).

**Distinctions conceptuelles explicites (c'est le cœur testable de la page)** :

1. **البراديغم ≠ منظومة الأفكار / البنية المفهومية** — « ولئن كان البراديغم يبدو **قريبا في
   معناه** من منظومة الأفكار أو البنية المفهومية، **فإنّه يختلف عنها في بعض التفاصيل أو
   الجزئيات** » : le paradigme doit signifier **نظام القواعد المقبولة والمتفق عليها والمستبطنة
   بوصفها معايير من قبل الجماعة العلمية، في فترة زمنية معيّنة من تاريخها**, pour lui permettre
   de trier les faits **الجديرة بالبحث والمعالجة**.
2. **En sciences sociales** : le paradigme = **شبكة معايير قراءة الأحداث وتأويلها** avec des
   moyens méthodologiques propres — exemples imprimés : **براديغم ولادة الرأسمالية**,
   **براديغم الصراع الطبقي**.
3. **En linguistique (الألسنية)** : le paradigme = **مجموع الأشكال المختلفة التي يمكن أن تتخذها
   عبارة أو فعل ما** — exemple imprimé : (كنت، كان، كنّا…).
4. **Autres acceptions signalées** : le **الحقل اللامتناهي** bâti sur un système d'hypothèses
   dont nous n'avons pas conscience — soit la **البنية الفوقية** (بالمعنى الماركسي للمفهوم)
   correspondant à une étape du développement historique ; et le concept d'**الإبستيمي** chez
   **فوكو** = **نظاما من التمثلات التي تهم صورة المعرفة في حقبة تاريخية معيّنة**.

**الثورة العلمية — ce que la définition permet de comprendre (p.254-255, verbatim resserré)** :

> يسمح لنا هذا التحديد من فهم معنى **الثورة العلمية** التي يفترض قيامها **انقلابا على براديغم
> سائد والانتقال إلى براديغم جديد** يتوافق وروح الثورة ذاتها أي مع مبادئها وإحداثياتها في الحقل
> العلمي، بحيث أنّ **أي تغيّر في البراديغم يصحبه ضرورة طريقة جديدة في النظر إلى المشاكل
> القديمة**، وبذلك فإنّ **أية أزمة يشهدها العلم لا تكون مجرّد هدم إذ يقترن الهدم بالبناء**.

Exemple imprimé : **نظرية النسبية** a rouvert le **البراديغم النيوتوني** et permis de résoudre
des recherches restées inachevées faute de pouvoir l'être dans l'ancien paradigme.

**Valeur de l'analyse de Kuhn selon le manuel (deux apports, verbatim)** :
(1) **كشف سيرورة الثورة في العلم وما يعترضها من مقاومة** ; (2) **إبراز الطابع الجمعي للعلم**,
car il reflète **وعي العلماء الجمعيّ الذي يحقّق توافقا تعتبره حقبة ما حقائقها الموضوعية ومعرفتها
العلمية**.

**■ قيل في البراديغم (p.255, verbatim, 2 citations)** :

| Auteur (tel qu'imprimé) | Citation |
| --- | --- |
| **توماس كوهن** | « البراديغم هو **ما يمتلكه أعضاء جماعة علمية بشكل مشترك** ». |
| **رولان أومناس** | « البراديغم هو **حالة نجاح علمي ملحوظة، تحمل قيمة نموذجية، تدفع العلماء إلى محاكاتها** ». |

**Encadré `* لمزيد التعمّق` (p.255)** — deux listes de sites, l'une en regard de l'onglet
**البراديغم**, l'autre en regard de l'onglet **الواقع** :

- **البراديغم** : `www.forums.futura-sciences.com` · `www.mrhzoom.com` ·
  `www.fr.wikipedia.org/wiki/Epistémologie` · `www.univ-montp3.fr`
- **الواقع** : `www.ac-grenoble.fr` · `www.etudes-lacaniennes.net` ·
  `www.publimath.irem.univ-mrs.fr` · `www.onphi.org`

Illustration p.255 : gravure d'un chimiste du 18e siècle en habit, élevant un ballon de verre
dans son laboratoire (sans légende imprimée).

---

###### 2.3.2 سياقات فكريّة — p.256-259

Deux courants exposés : **السييارنيطيقا** (p.256-257) et **الإبستيمولوجيا البنائية**
(p.257-259). Gabarit imprimé : **\* التعريف** → (pour la cybernétique) **\* الجهاز المفهومي** →
**\* لمزيد التعمّق**.

**1 — السييارنيطيقا · `La Cybernétique` — p.256-257**

**\* التعريف (verbatim resserré)** :

> تفيد **السييارنيطيقا** **علم المراقبة والإعلام**، الذي يهدف إلى **معرفة النظم أو الأنساق
> وقيادتها**، إذ تعني، في الدلالة اللغوية اليونانية، **فعل التحكم والحكم**، ولذلك استخدم
> **أفلاطون** المصطلح للدلالة على **قيادة السفينة**.

Éléments d'histoire imprimés :

- Avant de devenir une théorie, ses principes furent **appliqués en ingénierie** (الآلات
  البخارية — machines à vapeur fabriquées pour la conduite des navires) ; ils ont **aussi servi
  à conduire les hommes**, « وهو ما يعني أنّها **تحيل على مجال سياسي** ».
- Le terme **reste ouvert** au sens de **علم الأنساق أو النظم**. Définition d'aujourd'hui :
  **علم التّحكم في الأنساق أو النظم، الحيّة وغير الحيّة**.
- **Fondation** : « تأسست، بما هي علم، **سنة 1948** على يد عالم الرياضيات الأمريكي **نوربارت
  فينر** » qui tient que **notre monde se compose en totalité de systèmes imbriqués et en
  interaction** — d'où l'on peut regarder comme des systèmes : **المجتمع، الاقتصاد، شبكة
  الحاسوب، الآلة، المؤسسة، الخلية، العضوية، الفرد**.
- **Les ordinateurs et toutes les machines intelligentes** ne sont que le produit des
  applications de la cybernétique ; elle a fourni des procédés efficaces pour contrôler **نسقين
  أساسيين : المجتمع والاقتصاد**.

**Définition du نسق/نظام سييارنيطيقي (verbatim)** :

> يمكن تعريف **نسق أو نظام سييارنيطيقي** بوصفه **مجموع عناصر متفاعلة**، هذا التفاعل بين العناصر
> يمكن أن يتمثل في **تبادل المواد أو الطّاقة أو المعلومة**، وهذا التبادل يمثل بدوره **تواصلا**
> بموجبه **تغيّر العناصر وضعها أو تبدّل نمط فعلها**.

**Notions centrales déclarées** : **التواصل** · **الإشارة** · **الإعلام** · **المفعول الرجعي**
(rétroaction) — « معاني مركزية في سييارنيطيقا كلّ الأنساق أو النظم ».

Autres acceptions imprimées :

- **علم الأنساق / الدراسة الديناميكية للبنى**, la **بنية** étant **مجموع العلاقات الموجودة بين
  عناصر المجموعة** ; sur cette base la cybernétique signifie **المراقبة والتحكم**.
- **نمذجة التبادل** par l'étude des informations et des principes d'interaction, issus de
  l'étude du **النظام العصبي** et incarnés dans la production de **الذكاء الاصطناعي**.
- Bilan de tout le mouvement scientifique **الممتدة على كل القطاعات والاختصاصات** ; au plan
  technique, **طريقة تدرس التطور الديناميكي للأنساق أو النظم** en s'appuyant sur les relations
  entre disciplines.
- Définition citée entre guillemets par le manuel : **« العلم المركب من مجموع النظريات التي تضم
  دراسة سيرورة القيادة والتواصل وتعديلها عند الكائن الحي، وفيما يتعلّق بالآلات، والأنساق
  الاجتماعية والاقتصادية »**.
- D'où quatre sens retenus : **علم الأنساق** · **علم المعلومة** · **مبدأ نسقي** ·
  **وسيلة مراقبة**.

**Les deux étapes du mouvement cybernétique (verbatim)** :

- **\* المرحلة الأولى** : « تمتد بين سنة **1942 و1953** وهي مرحلة **بروز طريقة جديدة في تحليل
  الظواهر** ».
- **\* المرحلة الثانية** : « المرحلة التي تم **دمج هذه الطريقة ضمن أفق البحث العلمي وتطبيقاته**،
  والتي كان من نتائجها **إحداث ضرب من القطيعة الإبستيمولوجيّة أثّرت في كل ميادين العلم** ».

Conséquence imprimée (p.257) : le champ de la cybernétique étant **جدّ ممتداً**, on n'a pu la
cantonner à une discipline ou un secteur scientifique déterminé — « ولذلك **لم تصبح
السييارنيطيقا مجالا علميا في ذاته** لذلك **انتهت إلى نظرية في الأنساق أو النظم** ».

**\* الجهاز المفهومي (p.257)** :

- **■ النسق أو النظام** — « من أهم ما يميز نظرة السييارنيطيقي إلى المشكلات **التفكير في إطار
  الأنساق أو النظم أو المنظومات** » ; c'est un **مصطلح جوهري** : rien ne fonctionne sans
  **ضبط حدود النسق أو المنظومة التي يراد درسها**, sa description et son expression **بلغة
  رياضية أو بأي لغة تسمح بقدر معيّن من الحساب وإجراء الدراسات اعتمادا على نموذج**.
- **Quatre bases de classification des systèmes (verbatim)** :
  1. **■ نظام ملموس** (الإنسان، الصاروخ) ↔ **نظام غير ملموس** (النظام المصرفي، النظام الاشتراكي).
  2. **■ المعادلات التي تصف النموذج** : **النظم الخطية** qu'on peut traiter mathématiquement
     avec aisance ↔ **نظم غير خطية** « لا يعتمد في معالجتها طريقة خاصة » `[?]` (formulation de
     la source, voir § Incertitudes).
  3. **■ نظم ترتبط فيها الخاصيّة المدروسة بالزمان** ↔ **أخرى ترتبط بالزمان والمكان**.
  4. **■ نظم تكون فيها الخاصية المدروسة متصلة** ↔ **أخرى منفصلة أو متقطعة**.

**\* لمزيد التعمّق (p.257, verbatim, translittérations de la source)** :
**أندري أمبار** : *بحث في فلسفة العلوم* · **نوربارت فينر** : *السييارنيطيقا والمجتمع* ·
**لويس كوفينيال** : *بحث حول التعريف العام للسييارنيطيقا* · **دفيد أورال** :
*السييارنيطيقا والإنساني* · **سالين لفانتان** : *امبراطورية السييارنيطيقا*.

**2 — الإبستيمولوجيا البنائية · `Epistémologie constructiviste` — p.257-259**

**\* التعريف (verbatim, une phrase)** :

> تمثّل **الإبستيمولوجيا البنائيّة** تيّارا إبستيمولوجيّا **يؤكّد الخاصيّة البنائيّة والمبنيّة
> للمعرفة، وبالتالي للواقع**.

**أصل مصطلح البنائية (p.257)** — la généalogie telle que le manuel la trace :

- **جان بياجيه** : rattachement historique du courant ; il a employé le terme **البنائية** et
  l'a présenté comme approche épistémologique **منذ سنة 1967** dans un article intitulé
  **« المنطق والمعرفة العلمية »**.
- Racines plus anciennes : **بروتاغوراس** `Protagoras` — « **أنّ الإنسان مقياس كلّ الأشياء** » ;
  puis **بيرون** `Pyrrhon` **والريبيين عموما**, pour qui **النظام الذي ندركه قد لا يكون نظام
  الطبيعة الواقعي** : nous ne pouvons connaître le réel en soi, seulement **أسماء هذا الواقع
  وتمثلاته**.
- **باشلار**, connu pour avoir forgé **مفهوم العائق الإبستيمولوجي** — ce qui empêche qu'un
  changement se produise **في بنية العقل العلمي** — et pour avoir affirmé **أسبقية المشكل العلمي
  على أي إنشاء نظري**, aboutissant à : **« لا شيء معطى، الكلّ منشأ »**. Raison donnée : les
  problèmes scientifiques ne se posent pas d'eux-mêmes ; la connaissance scientifique est, pour
  l'esprit scientifique, **إجابة عن سؤال أو مشكل** — « ففي ظل غياب الأسئلة **لا مجال لإمكان قيام
  معرفة علميّة**، وكأنّنا به يعتبر أنّ **الدرب تنتجه الخطوات** ».

**Rupture attribuée à Piaget** : il est **أب البنائية**, celui qui rompt avec les idées tenant
que **المعرفة العلمية تكتسب عن طريق الكشف والاكتشاف**. Argument d'appui : les
**« العلوم الاصطناعيّة »** (علم التحكم أو السييارنيطيقا، وعلوم التنظيم والقرار) **ne trouvent pas
leur place** dans l'épistémologie classique qui voit dans la science **نتاجا للتجربة** — ce qui
confirme la valeur de l'épistémologie constructiviste.

**Définition piagétienne de l'épistémologie + les 3 questions (verbatim, p.258)** :

> تعرّف **الإبستيمولوجيا** مع **بياجيه** بما هي **« دراسة إنشاء المعارف الصحيحة أو المشروعة »**
> وهو تعريف لا يمكن أن يفهم إلا باستحضار **أسئلة أساسية ثلاثة** :
> 1/ **ما المعرفة ؟**
> 2/ **كيف تنشأ المعرفة ؟**
> 3/ **كيف نقدّر قيمتها أو صلاحيّتها ؟**

**Réponse à la 1ʳᵉ question — les deux hypothèses de لوموانيو (verbatim resserré)** :

- **الفرضية الأولى — ذات طبيعة فينومينولوجية** : **لا يمكن أن نفصل بين الذات العارفة والظاهرة
  موضوع المعرفة**.
- **الفرضية الثانية — من طبيعة تيلولوجية** (« تدرس **التيلولوجيا** نظام الغايات أو نسق
  الأهداف ») : elle porte sur **الهدف الذي يحرّك الذات العارفة لمعرفة ظاهرة أو موضوع ما**.

**Opposition frontale posée par le manuel — constructivisme ↔ épistémologie positive-réaliste** :

Cette approche s'oppose à **الإبستيمولوجيا الوضعية ـ الواقعيـة**, c'est-à-dire :

| Épistémologie positive-réaliste | Épistémologie constructiviste |
| --- | --- |
| **الفرضيّة الأنطولوجيّة** : للواقع وجود موضوعي مستقل | لا فصل بين الذات العارفة وموضوع المعرفة (فرضية فينومينولوجية) |
| **مبدأ الحتميّة** : علاقات موضوعية ضرورية وثابتة تحكم الظواهر | مبدأ **اللاتعيّن** (فيزياء الكوانتا) vient l'appuyer |
| نظام الطبيعة **معطى نكتشفه بواسطة المنهج العلمي** | المعرفة **تُبنى** — « **لا نعرف موضوعا إلا بالفعل فيه وتحويله** » (بياجيه) |
| المعرفة **إستنتاجيّة أو استنباطية** — مبدأ التحليل (**ديكارت**) + مبدأ السبب أو العلّة الكافية (**لايبنتز**) | مبدأ **التّمذجة النّسقية المركّبة** + مبدأ **العقل الجدلي أو الحذر أو المتداول** (**لوموانيو**) |

Précision imprimée : ce que la physique quantique révèle **n'est pas une surprise pour le
sociologue**, qui a bien perçu que **حضوره بوصفه ملاحظا ودارسا للظواهر الاجتماعيّة ليس محايدا**.
D'où la question du **pourquoi tel modèle plutôt qu'un autre** — c'est-à-dire du **الهدف أو
الغاية** ; « **الإنسان الباحث لا يمكن أن يكون محايدا وإنما تحكمه ضرورة دوافع معيّنة** », les
commanditaires ou les chercheurs pouvant avoir **أهداف أو مصالح خاصة**. Appui : **بشلار** —
**تأمّل الذات للموضوع يتّخذ دوما صورة مشروع**.

**مبدأ التّمذجة النسقية المركّبة (p.258, verbatim resserré)** :

> يعدّ **النموذج** وفق هذا المبدأ **وسيلة لا ينبغي أن يتم الخلط بينها وبين الواقع**، إذ
> **« أنّ الخريطة ليست الأرض »**، وبما أنّ **كلّ نظرية تتضمّن دائما وضرورة وعلى الأقلّ مصادرة
> لا تتم البرهنة عليها في إطار تلك النظرية**، فإنّ **العالم الملاحظ لا يمكن أن يوضع في معادلات
> أو يتم وصفه بصورة كلّية**.

**ادغار موران — « من أجل إصلاح الفكر » (article nommé, citation verbatim)** :

> « **التفكير المركّب** هو تفكير **يعمل في نفس الآن على التمييز والوصل**… إنّ **الثقة في حتمية
> كونية قد انهارت**. والكون **لا يخضع إلى سيادة نظام مطلقة**، إنّه **لعبة ورهان حوار بين النظام
> والفوضى والتنظيم** ».

Glose imprimée : la pensée complexe est **بناية ذات طوابق عديدة** dont la base se compose de
**نظرية الإعلام** + **السييارنيطيقا أو نظرية التحكم** + **نظرية الأنساق**, et qui contient les
moyens nécessaires pour construire **نظرية في التنظيم**. Par contraste avec la vision classique,
Morin insiste sur **ضرورة تجاوز كلّ محاولة لتأسيس منطق واحد** : **العقلانيّة الحق هي التي تدرك
حدودها وتكون قادرة على التفكير فيها وتجاوزها** tout en reconnaissant **وجود ما لا يمكن تعقله**.

**Objection traitée : « هل تنتهي بنا الإبستمولوجيا البنائية إلى نفي كلّ قيمة عن العلم ؟ »
(p.259)** :

- **L'accusation** : à l'instar de la **فلسفة ما بعد الحداثة**, le constructivisme est accusé de
  **النسبية العدمية**.
- **La réponse des constructivistes** : à défaut de fonder **اليقين** permettant une
  **معرفة حقيقية**, il reste possible de produire une connaissance **على صورة السنفونية أو اللحن
  الموسيقي الطويل المركب** ; la connaissance n'est pas **بناء معماري تكون قاعدته صخرة ثابتة**,
  mais des **مباحث متعددة تترابط فيما بينها** produisant une connaissance de sens différent du
  sens classique — « وهو ما يعني أنّ **البنائية** بهذا الموقف إنّما **تعلن عن ولادة براديغم
  جديد** ».

**La connaissance comme « معرفة فاعلة » (p.259, verbatim)** :

> تنظر هذه المقاربة الإبستيمولوجية إلى المعرفة بما هي **« معرفة فاعلة »** على حد عبارة
> **لوموانيو**، بحيث **لا ينبغي البحث عن التفسير وإنما عن تمثُلات يمكن لنا إبداعها**، وبالتالي
> تقترح **البنائية** معرفة **بوصفها تمثلا، أو نموذجا** يسمح لنا الفهم الذي يقدّمه لنا بشأن ظاهرة
> ما **الفعل فيها** طالما **« أنّ الحقيقي هو الفعل ذاته »** أو طالما **« أنّ الحقائق ليست أشياء
> تكتشف وإنما هي أفعال نقوم بها، إنها أبنية وليست كنوزا »**.

**Position finale du constructivisme sur le réel (p.259, verbatim — la distinction la plus
testable de la section)** :

> ترى **البنائية** **الواقع الموضوعي، الواقع في ذاته** بوصفه **حدّا يستحيل بلوغه**، أمّا
> **الواقع الذي نريد تعقّله** فهو عبارة عن **تمثّل**، بحيث **تحل البينذاتية محلّ الموضوعية**،
> وبهذا المعنى تقترح البنائية **تجاوز النقائض الكلاسيكية بين المثالية والخبرية بين الذات
> والموضوع**، وهو موقف **يتجاوز أيضا النزعة الواقعية أو الوضعية دون سقوط في فخ النسبوية**،
> و بالسعي إلى إنتاج **معارف مجدية أو فاعلة أو قابلة للتجسيد** تراهن البنائية على **العلوم
> التطبيقية أو المطبقة مثل الهندسة أو الإدارة**.

**\* لمزيد التعمّق (p.259, verbatim)** : **بشلار** : *الروح العلمي الجديد* ·
**جون لوي لوموانيو** : *علم الأنساق* ; *الإبستمولوجيا البنائية* · **جون بياجيه** :
*المنطق والمعرفة العلمية* ; *الإبستمولوجيا التكوينيّة* · **إدغار موران** : *معرفة المعرفة*.

**Encadré-image p.259** (photo : un cube et une pyramide sombres posés sur une surface dorée, une
lueur derrière) — légende verbatim : **« إنّ الحقائق ليست أشياء تكتشف وإنما هي أفعال نقوم بها،
إنها أبنية وليست كنوزا »**.

##### 2.4 نافذة كيفيّات للتفكير — p.260-263

> **Pages lues** : p.260–263 (intégral).

**p.260 — page d'ouverture.** Titre imprimé : **كيفيات للتفكير**. Image : une chouette effraie
perchée dans l'encadrement d'une vieille fenêtre en bois, la nuit. Encadré-citation avec portrait
de **فوكو** (verbatim) :

> « علينا أن نضع من جديد موضع سؤال، هذه **التركيبات الجاهزة**، ونطرح ثانية للبحث تلك
> **التجميعات** الّتي درجنا على تقبّلها **دون إعمال للفكر النقدي** »
> — فوكو، *حفريّات المعرفة*

La نافذة comporte **4 تمارين**, chacun bâti sur le même gabarit : **المهارة المستهدفة** (la
compétence visée) → **توضيح** (l'encadré de méthode) → un support (**السند** / **المفهوم** /
**الموقف** / **المهمّة**) → **المهام** ou **التمشّيات** (les démarches).

###### تمرين 1 — p.261

- **المهارة المستهدفة** : **الكشف عن بنية النص المنطقيّة**.
- **توضيح (encadré de méthode, verbatim)** :
  > تتميّز **الكتابة الفلسفيّة** بـ**صرامة منطقيّة** تتعلّق بـ**الروابط القائمة بين القضايا**
  > التي يجري عرضها في النص قصيرا كان أو طويلا. **تحدّد تلك الروابط دور كلّ قضيّة في بنية
  > النص** بحيث **يكوّن الكلّ وحدة ذات معنى**.
- **السند** — texte attribué à **ج. ق. قرانجي**, *الاحتمالي والممكن والعرضي*, **ص 236**.
  *Thèse* : le réel de la science est un réel **interprété** (partiellement, provisoirement, mais
  nécessairement) ; les modèles abstraits naissent d'un **écart de la pensée** passant par les
  **الافتراضيات**, si bien que la modélisation intègre, à côté des faits actuellement réalisés,
  des **وقائع افتراضيّة** qui peuvent se réaliser comme ne pas se réaliser. Formule finale citée
  verbatim par le manuel : **« قد يصحّ القول إنّ ما لم يوجد يفسّر ما يوجد »**.
  *Concepts mobilisés* : الواقع · التفسير · النموذج · الافتراضي · التجريد · اليقين.
- **المهام (verbatim, 6 consignes)** :
  1. أرصد مختلف **القضايا** الواردة في النص.
  2. أتبيّن **الروابط المنطقيّة** القائمة بين تلك القضايا.
  3. أحدّد **دور كلّ قضيّة** في النص.
  4. أستخلص **الفكرة الناظمة** التي تربط بين مختلف القضايا.
  5. أتثبّت إن كان بالإمكان **الاستغناء عن بعض القضايا** دون إحداث خلل في بنية النص.
  6. أستخلص **الأطروحة** التي يدافع عنها الكاتب.

###### تمرين 2 — p.261-262

- **المهارة المستهدفة** : **تحديد سياقي للمفهوم**.
- **المفهوم** : **« التفسير »**.
- **توضيح (encadré de méthode, verbatim)** :
  > – **المفهوم فكرة تتميّز بالتجريد والكليّة** وله **قيمة إجرائيّة كوسيلة للفهم والتفسير**.
  > – **للمفهوم موضعه ووجوده علائقيّ، لذا لا يتحدّد معناه إلاّ سياقيّا**.
- **التمشّيات (p.262, verbatim, 4 étapes)** :
  1. أعود إلى **نصّ التمرين الأوّل** وأحدّد **موقع** مفهوم « التفسير ».
  2. أتبيّن **علاقات المفهوم بغيره من المفاهيم** الواردة في النصّ.
  3. أحدّد **دلالة التفسير** في ضوء فهمي للعلاقات التي رصدتها.
  4. أستخلص **المدلول السياقي** لمفهوم التفسير وأصوغه في **عبارة واضحة تتضمّن كلّ خصائصه**.

###### تمرين 3 — p.262

- **المهارة المستهدفة** : **الحجاج على موقف**.
- **توضيح (encadré de méthode, verbatim)** :
  > ■ **الحجاج أسلوب في القول يهدف إلى الإقناع برأي أو موقف بتوسل جملة من الحجج المدعمة
  > بأمثلة.**
  > ■ **يبنى الحجاج وفق أساليب مختلفة : دحضا أو مماثلة…**
- **الموقف (à défendre, verbatim)** :
  > « **ردّ النمذجة إلى عمليّة تخييليّة افتراضيّة يجعل منها ضربا من الترف الفكري وملهاة
  > للعقل** ».
- **المهام (verbatim, 4 consignes)** :
  1. أحدّد **دلالة هذا الموقف** وأتبيّن **سياقه**.
  2. أستحضر **مكتسباتي** حول هذا السياق.
  3. أتخيّر **أسلوب الحجاج المناسب** لتأكيد هذا الموقف.
  4. أستحضر **حججا تتلاءم مع الأسلوب** الذي تخيّرته.

###### تمرين 4 — p.262-263

- **المهارة المستهدفة** : **القدرة على التأليف**.
- **المهمّة (verbatim)** :
  > **هل تستجيب النمذجة لمطلب الكوني ؟**
  > أجيب عن هذا السؤال في **فقرة لا تتجاوز العشرين سطرا** متبعا في ذلك التمشيات المصاحبة.
- **التمشّيات (p.263) — la méthode de rédaction en 3 مراحل, verbatim** :

  **■ مرحلة بناء المشكل**
  - أبيّن **ما يبرر معالجة هذا السؤال**.
  - أشير إلى **أهميّة السؤال**.
  - أستخلص **مشكلا فلسفيّا أصوغه بوضوح**.

  **■ مرحلة بلورة الجواب**
  - أستحضر **دلالة النمذجة**.
  - أحدّد **معنى الكوني في هذا السياق**.
  - أنظر في **العلاقة الممكنة بينها وبين مطلب الكوني**.
  - أستحضر **بعض المؤيّدات** تأكيدا لهذه العلاقة.
  - **أتظنّن على هذه العلاقة** باعتماد **أمثلة دقيقة**.
  - أستفيد من **واقع تعدّد النماذج وتنوّعها**.

  **■ مرحلة الاستخلاص**
  - أستخلص **الموقف النهائي**.
  - أشير إلى **قيمته**.

Illustration p.263 : tête humaine en fil de fer quadrillé de damiers roses, blancs et bleus,
flottant au-dessus d'un damier vert sur fond étoilé (sans légende imprimée).

##### 2.5 نافذة نصّ مطوّل — كارل بوبار : *أسطورة الإطار*, الفصل الثامن — p.264-269

> **Pages lues** : p.264–269 (intégral). Extrait sous droits : **non recopié** (R-2) — restitué
> par sa structure argumentative, telle que le manuel la découpe en marge, et par de courtes
> citations attribuées.

###### Identification de l'œuvre (p.264-265, verbatim)

- **Auteur** : **كارل بوبار** — mention imprimée p.264 : **كارل بوبر (1902–1980)**, `Karl POPER`
  [sic — un seul `P`].
- **Œuvre** : **أسطورة الإطار** — sous-titre imprimé : **في دفاع عن العلم والعقلانيّة**.
- **Chapitre** : **الفصل الثامن : النّماذج والأدوات والصدق**.
- **Traduction** : **ترجمة : أ.د. يمنى طريف الخولي** — **( عالم المعرفة، أفريل/ماي 2003 )**.
- **Couverture reproduite p.264** : collection **عالم المعرفة**, n° **292**, **أبريل/مايو 2003** ;
  **تأليف : كارل. ر. بوبر** · **تحرير : مارك أ. نوترنو** `[?]` · **ترجمة : أ.د. يمنى طريف
  الخولي**.
- **Note de bas de page (1) imprimée en marge, p.265** : **« عنوان المحاضرة : منهجيّة البحث في
  العلوم الاجتماعيّة »** — l'extrait s'ouvre sur « في هذا الجزء الثاني من محاضرتي(1) ».
- **Encadré-citation p.264 (verbatim, la seule citation autonome de la page)** :
  > « على هذا النحو يتكوّن **النموذج** من **عناصر معيّنة وضعت بحيث ترتبط بعلاقات نمطية مع بعضها
  > البعض**… ويبدو أنّنا في العادة **نعمل أوّلا بنماذج**، وأنّ النماذج برفقة **آلية عمل
  > ابتدائية**، قد تقدّم حلولا لبعض مشاكل من النّوع الثاني، أي **تفسير بعض الأحداث النمطيّة** ».
- Illustrations p.264 : détail de peinture (mains feuilletant un manuscrit enluminé) ; photo
  noir et blanc de Popper âgé, la main sur le front ; reproduction de la couverture arabe.

###### Structure de l'argumentation — le découpage imprimé en marge par le manuel

Le texte est **numéroté par lignes de 5 en 5** (l.5 → l.138 environ) et chaque mouvement est
nommé dans la marge. C'est ce découpage qui fait office de guide de lecture (il n'y a **aucun
questionnaire imprimé** dans cette نافذة — voir § Bornes de scope).

| # | Repère marginal imprimé (verbatim) | Lignes | Ce que le passage établit |
| --- | --- | --- | --- |
| 1 | **الانطلاق من التمييز بين نوعين من مشاكل التفسير** | p.265, l.4-16 | Deux types de problèmes d'explication/prédiction : le **premier** porte sur **un événement singulier** (ou un petit nombre) ; le **second** sur **un type ou un mode d'événements**. |
| 2 | **إبراز الفارق بين هذين النوعين من المشاكل : التأكيد على أهمية تشييد نموذج لتفسير نوع أو نمط معيّن من الأحداث** | p.265, l.17-25 | La différence : **« النوع الأوّل يمكن حلّه بغير تشييد نموذج »** — il suffit de lois générales + conditions initiales, dans un cadre théorique (Newton). |
| 3 | **مثال عن نموذج في العلوم الطبيعية** | p.265-266, l.26-35 | Pour le second type on construit un **نموذج ميكانيكيّ فعليّ** ou un **رسم منظوري** : une lampe fixe (le soleil), un petit globe de bois tournant autour, une petite lune tournant autour de la Terre. |
| 4 | **بيان دواعي اعتبار النموذج استقرابيا** | p.266, l.36-42 | Popper appelle ce modèle **استقرابيّا** : il **ne prétend pas** représenter la situation en vérité ni la mécanique newtonienne ; il ignore les orbites elliptiques et les perturbations — « ومع هذا قد يحرز أهدافه جيّدا، مادام يحلّ مشكلة التفسير المطروحة ». |
| 5 | **بيان دور النموذج : يحلّ النموذج محلّ الشروط الأوّلية** | p.266, l.43-62 | Pour les problèmes du second type, **« تشييد نموذج يمكن أن يحلّ تماما محل الشّروط الأوّليّة »** ; les **الشّروط الأولية النمطيّة** s'y incarnent. D'où la conclusion : le premier type marche **بقوانين عموميّة وشروط أوّليّة**, le second **بالنّماذج**. Mais le modèle a besoin de lois générales — les **القوانين « الباعثة للحياة »** `Animating` — pour se mettre en mouvement (« نبث الحياة في أعطاف النموذج »). |
| 6 | **الإشارة إلى بعض حدود النموذج** | p.267, l.65-73 | Les tentatives de **réduire** les lois animatrices à des **propriétés structurelles du modèle** peuvent réussir largement, mais **« لن تستطيع أبدا اختزال كلّ القوانين الباعثة للحياة إلى نماذج وبنيات »**. |
| 7 | **التأكيد على الدّور الذي لعبته النّماذج في تقدّم معظم النّظريات** | p.267, l.74-86 | La réciproque est fausse : la plupart des questions auxquelles la théorie de Newton répond pourraient l'être **sans modèle**. Mais historiquement les modèles ont été décisifs : **بطلميوس وكوبرنيك وكبلر** furent tous **صنّاع نماذج** ; la théorie de Newton naît en partie comme tentative d'expliquer **ce qui anime le modèle de Kepler** ; au 20e siècle, le modèle de l'atome de **رذرفورد وبوهر** précède de plusieurs années la mécanique quantique, qui a fourni ce qui l'anime. |
| 8 | **تحديد مكونات النّموذج** | p.267, l.87-99 | Le modèle = **عناصر معيّنة** liées par des **علاقات نمطية**, **plus** des **قوانين عموميّة معيّنة عن التأثير المتبادل بينها** (les lois « animatrices »). Précision majeure : **« النّموذج ليس من الضّروري أن يكون نموذجا ميكانيكيا حتّى في العلوم الفيزيائية »**. |
| 9 | **بيان علاقة النموذج بالنظرية من ناحية وبالقوانين من ناحية أخرى** | p.267-268, l.100-107 | Les modèles peuvent être dits **« نظريّات »** ou **تجسيد نظريّات**, en tant que **محاولات لحلّ مشكلات التّفسير** ; mais **l'inverse est faux** : toutes les théories ne sont pas des modèles. Thèse centrale : **« إنّ النّماذج تمثّل شروطا أوّليّة نمطيّة أكثر من أن تمثّل قوانين عموميّة »** — d'où le besoin qu'elles ont d'être rejointes par des lois générales qui, elles, **ne sont pas des modèles**. |
| 10 | **تدعيم الموقف بمثال من الكيمياء العضوية** | p.268, l.108-116 | Les **نماذج الجزيئات** de la chimie organique représentent l'arrangement des atomes et peuvent figurer les **الرّوابط الكيميائية**, mais **ne représentent pas les lois** (ou la **الرّنين**) supposées animer la cohésion des molécules — là s'arrête le modèle typique et commencent les **القوانين المجرّدة البحتة**. |
| 11 | **الانتقال لمعالجة منزلة النموذج في العلوم الاجتماعية** | p.268, l.117 | Charnière imprimée en gras : **« وحسبنا هذا عن النماذج في العلوم الطبيعية »**. |
| 12 | **التأكيد على أن مغزى النموذج ودلالته يظل واحدا سواء تعلّق الأمر بالعلوم الطبيعية أو الاجتماعية** | p.268, l.118-120 | La thèse annoncée : ce qui a été dit du sens et de la portée des modèles dans les sciences de la nature **vaut aussi** pour les sciences sociales. |
| 13 | **إبراز كيف تعد النماذج في العلوم الاجتماعية أكثر أهمية** | p.268, l.120-127 | **« النّماذج قد تكون أكثر أهميّة هنا »** : la méthode newtonienne (lois générales + conditions initiales) **يصعب جدّا تطبيقه** en sciences sociales théoriques. **« وعلى وجه التقريب تعمل هذه العلوم دائما بمنهج تشييد مواقف أو شروط نمطيّة، أي بمنهج تشييد نماذج »**. Rattaché à un fait : en sciences sociales, il y a — dans les termes de **هايك** — **moins d'« تفسير تفصيلي »** et **plus d'« تفسير من حيث المبدأ »** qu'en physique. |
| 14 | **تأكيد أن النماذج في العلوم الاجتماعية هي توصيفات أو إعادة تشييد لمواقف اجتماعية نمطية** | p.268, l.128-136 | Le problème fondamental des sciences sociales théoriques et historiques est **تفسير وفهم الأحداث في حدود الأفعال الإنسانيّة والمواقف الاجتماعيّة** ; le terme-clef est **« الموقف الاجتماعي »**. La description d'une situation historique concrète y est **l'analogue des conditions initiales** en science de la nature. D'où : **« و«النماذج» في العلوم الاجتماعيّة النّظريّة هي في جوهرها توصيفات أو إعادة تشييد مواقف اجتماعيّة نمطيّة »**. |
| 15 | **ابراز أن فكرة الموقف الاجتماعي هي المقولة الأساسية في منهجية العلوم الاجتماعية** | p.268, l.136-138 | Clôture : **فكرة الموقف الاجتماعي هي المقولة الأساسيّة في منهجيّة العلوم الاجتماعيّة** — « تقريبا، كلّ مشكلة للتفسير في العلوم الاجتماعية تتطلّب تحليلا لموقف اجتماعي ». |

**Exemples imprimés dans le texte (utiles pour toute question sur la distinction des deux types
de problèmes)** :

| | Problème de **type 1** (événement singulier) | Problème de **type 2** (type d'événement) |
| --- | --- | --- |
| **العلوم الطبيعية** | « متى ستحدث المرّة التالية لخسوف القمر ؟ » | « لماذا يحدث خسوف القمر المرّة تلو الأخرى، وفقط حينما يكون القمر بدرا ؟ » |
| **العلوم الاجتماعية** | « متى سيكون الارتفاع التّالي لمعدّلات البطالة في ميدلاندز، أو في وست أونتاريو ؟ » | « لماذا ترتفع وتنخفض معدّلات البطالة في صناعة البناء بصورة موسميّة ؟ » |

**Noms propres cités dans l'extrait** : نيوتن · بطلميوس · كوبرنيك · كبلر · رذرفورد · بوهر ·
هايك. **Termes latins imprimés dans le texte arabe** : `Animating` (l.57, glosé
**« الباعثة للحياة »**).

**p.269 — la page d'illustration du نصّ مطوّل** (aucun texte suivi) :
- Photo noir et blanc d'une éclipse totale avec couronne solaire — légende : **كسوف الشمس**.
- Schéma légendé en français — titre imprimé en arabe : **نموذج استقرابي يفسر كسوف الشمس** ;
  le schéma oppose **`éclipse totale`** et **`éclipse annulaire`**, avec les mentions
  `soleil` · `ombre de la lune` · `lune` · `observateur sur la terre`.

##### 2.6 مختصرات — p.270

> **Page lue** : p.270 (intégral). **Récapitulatif officiel du مبحث — reproduit verbatim**, dans
> l'ordre des 6 encadrés imprimés. Illustration : plume d'oie noire posée sur un manuscrit ancien.

**■ Encadré 1 — le cadre (problématique + les 3 dimensions)**

> لئن كان **مطلب الكوني** متجذّرا في **أفق التواصل الإنساني**، ها هو في الجهة الأخرى مطلب ملحٌّ
> في **مجال العلم** قد يتحقق عبر عمليّة **النمذجة** بما هي **فعل تنظير**، له **أبعاد ثلاثة** هي
> **مسارات للعقل العلمي** : **بعد تركيبي وبعد دلالي وبعد تداولي**.

**■ Encadré 2 — البعد التركيبي**

> تبيّنت أنّ **البعد التركيبي** يتجلّى في حقل العلم ضمن **مسار إنشائي** يعمد فيه العقل إلى
> **بناء نظم أو أنساق رمزية أو نماذج**، هي **بنى تصوريُّة مجرّدة أو إمكانات للصورنة**، قوامها
> **تخيّل يلعب فيه الحدس دورا رئيسيًا**.

**■ Encadré 3 — البعد الدلالي**

> أدركت أنّ **النمذجة** تتحقق أيضا في **بعد دلالي** على نحو **اختزالي، تبسيطي، تمثيلي لواقع
> معقّد** قوامه **قدرة تخييلية وإنشائيّة للعقل العلمي** تسمح له بابتكار **بنية مفهومية
> ونظريّات** تفسّر الواقع **لا كما يحدث أو كما يبدو**، وإنّما **تفسيرا افتراضيّا** بشفرات أو
> بعبارات جبريّة، **تفسير ما يوجد بما لا يوجد أو تفسير المرئي باللامرئي**.

**■ Encadré 4 — البعد التداولي**

> أدركت أنّ **النمذجة** ذات **بعد تداولي** في معنى **براغماتي** يتحقّق بإنشاء نموذج هو **تبسيط
> لمركّب** وصياغته **صوريّا في نسق رمزي** له **صلاحيته النظريّة وانتظامه الذاتي**، ولكنّه
> **قابل للاستعمال في مجالات مختلفة : الاقتصادي والاجتماعي والعضوي**، استعمالا موسّعا يؤكّد أنّ
> **النموذج يقوم على علاقة معلومة–تنظيم**.

**■ Encadré 5 — le gain et sa limite (le nœud problématique)**

> تبيّنت أنّ **إنشاء النماذج** يمثل شكلا من **التعقّل المبهر**، مكّن العقل من **السيطرة على غموض
> الواقع وتعقيداته**، و**مساعدة العلم على التطوّر**. وتبيّنت أن هذا **الغنم المعرفي** لا يخفي
> **محدودية النماذج على صعيد إبستيمولوجي** من حيث أنها **ليست إلا إمكانا لتعقل الواقع** تعقلا
> هو في الآن نفسه **خصوصيّا** سمته **التنوع والتعدّد** و**كونيّا لا يدرك وحدة الواقع في استحالة
> وجود نموذج موحّد**، الأمر الذي يثير **مشكل العلاقة بين فعل النمذجة ومطلب الحقيقة**.

**■ Encadré 6 — la mise en garde éthique et téléologique**

> أدركت أنّ **النمذجة** بوصفها **اختزالا وتبسيطا وتأمثلا وتصوّرا لا تاريخانيّا**، تطرح **مشكل
> الغايات** وتحمل على **استعادة سؤال المعنى** في موقف **تظنّن على النمذجة**، ينبّه إلى **نسيان
> الإيتيقي أو الغائي** ويحذّر من **مخاطر الإفراط في التبسيط والاختزال** الذي يحوّل **مشروع
> العلم بما هو معرفة الحكمة** إلى **لعبة مجّانية** أو **" عقيدة "** وبالتالي **تستحيل النمذجة
> إلى مجرّد وسيلة تحكّم**.

##### Bornes de scope

- ✅ **INCLUS** (tranche p.251-270, intégral) : la نافذة دعائم complète — les **2 تحديدات
  مفهوميّة** (الواقع، البراديغم) avec leurs trois entrées (لغة / اصطلاحا / فلسفيا وإبستمولوجيا),
  leurs **distinctions** et leurs rubriques **« قيل في … »** (6 citations attribuées au total) ;
  les **2 سياقات فكريّة** (السييارنيطيقا، الإبستيمولوجيا البنائية) ; les 4 encadrés
  **لمزيد التعمّق** (sites + bibliographies) ; la نافذة **كيفيّات للتفكير** avec ses **4 تمارين**
  et leurs encadrés **توضيح** verbatim ; la نافذة **نصّ مطوّل** (Popper, *أسطورة الإطار*, ch. 8)
  avec son **découpage marginal en 15 mouvements** ; les **مختصرات** verbatim (6 encadrés).
- ⛔ **EXCLU — n'est pas dans cette tranche** : les نوافذ **مدخل** et **سندات التفكير في المسألة**
  du مبحث 2 (p.215-250, traitées ailleurs) ; le مبحث suivant (à partir de p.271).
- ⛔ **EXCLU — n'existe pas dans le manuel à ces pages** : **aucun questionnaire imprimé
  n'accompagne le نصّ مطوّل** (p.264-269). Contrairement au gabarit habituel, il n'y a ni
  « أسئلة » ni « مهام » à la fin de l'extrait : le guidage est assuré **uniquement** par les
  repères marginaux qui nomment chaque mouvement de l'argumentation (relevés ci-dessus) et par
  la numérotation des lignes de 5 en 5. La p.269, dernière page de la نافذة, ne porte que deux
  illustrations légendées.
- ⛔ **EXCLU volontairement (R-2)** : le texte de Popper n'est pas recopié — seules figurent des
  citations courtes attribuées et la restitution structurale.
- ⛔ **Pas de QCM, pas de question générée** : ce lot est une transcription.

##### Incertitudes

- **p.257** — classification des systèmes, 2ᵉ base : la source imprime littéralement
  « ونظم **غير خطية لا يعتمد في معالجتها طريقة خاصة** ». Vérifié à 300 dpi : la lecture est
  certaine, mais l'énoncé est **contre-intuitif** (on attendrait « … *بد أن* يعتمد … طريقة خاصة »
  ou « … طريقة *عامة* »). Transcrit **verbatim** ; possible coquille de la source `[sic]`.
- **p.264** — couverture reproduite : le nom de l'éditeur scientifique se lit **مارك أ. نوترنو**
  `[?]` (scan de couverture usé ; la graphie pourrait être نوثرنو). Le millésime **2003** est
  confirmé par la mention imprimée p.265 (« أفريل/ماي 2003 ») ; sur la couverture le dernier
  chiffre est peu net.
- **p.255 / p.257 / p.259** — les listes **لمزيد التعمّق** sont transcrites telles qu'imprimées,
  y compris les translittérations arabes des noms propres (أندري أمبار، لويس كوفينيال،
  دفيد أورال، سالين لفانتان، رولان أومناس، جون لوي لوموانيو). Aucune identification latine n'a
  été ajoutée : le manuel ne l'imprime pas.
- **p.261** — la référence du سند est imprimée « **ج. ق. قرانجي، الاحتمالي والممكن والعرضي،
  ص 236** » ; les initiales latines correspondantes ne sont pas imprimées.
- **p.265-268** — la numérotation des lignes imprimée en marge (5, 10, … 135) a été utilisée pour
  situer les mouvements ; les bornes indiquées dans le tableau sont **approchées à la ligne
  près** lorsque le repère marginal chevauche deux paragraphes.

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

- ⚠️ **PROFONDEUR RÉELLE — `mixte` : ossature partout, génération sur UN chapitre.**
  - **L'ossature** — la page de titre et son verso (p.1–2), le التقديم (p.3), la خارطة الكتاب
    (p.4–5), l'ouverture du محور 1 (p.6) et le **فهرس intégral** (p.404–408). Le §2 et le §4 en
    dérivent : ils donnent le **scope, la structure et les plages de pages** exacts, ainsi que
    l'inventaire nominatif des **113 سندات** (auteur + titre + page).
  - **Le مبحث 2 « العلم بين الحقيقة والنمذجة » (p.215–270) à PROFONDEUR DE GÉNÉRATION**, intégral :
    les deux organigrammes officiels, la نافذة مدخل complète, les **16 سندات** décrits un par un
    (تمهيد verbatim, référence bibliographique imprimée, thèse reformulée, هوامش, notice d'auteur,
    مهامّ verbatim), les **تحديدات** الواقع et البراديغم avec leur gabarit لغة/اصطلاحا/فلسفيا et
    **leurs distinctions explicites**, les **سياقات فكريّة** (السييارنيطيقا, الإبستيمولوجيا
    البنائيّة), les 4 exercices de **كيفيّات التفكير** avec leurs encadrés توضيح, le **نصّ مطوّل**
    de بوبير restitué par ses 15 repères marginaux (texte non recopié — R-2) et les 6 encadrés de
    **مختصرات** verbatim.
    ⇒ **`chapitresGeneration: ["03-ilm-haqiqa-namdhaja"]`** : ce chapitre, et lui seul, est
    générable (R-5 lu au chapitre).

  **Ce qui n'est PAS transcrit** : p.7–214 et p.271–402, soit les **quatre autres chapitres**
  (1.1 الآنيّة والغيريّة, 1.2 الخصوصيّة والكونيّة, 3.1 الدّولة, 3.2 الأخلاق). Le LOT B y reste
  **interdit**.

- **Écarts relevés entre le فهرس et les pages** (le فهرس n'est pas toujours exact — s'en méfier
  pour les chapitres non encore lus) :
  - le nom de `Hans FREUDENTHAL` est imprimé sous **trois graphies** : « فرويندتال » au فهرس,
    **هانز فرودونتال** au سند 9 (p.237), **فرودنتال** au سند 13 (p.244) ;
  - سند 11 (رونيه توم, p.240) : le فهرس écrit « شروط صلاحيّة النموذج », la page imprime
    **شروط صلاحية النموذج** (sans šadda) ;
  - 2.3.1 تحديدات s'étend jusqu'à **p.255** (البراديغم occupe p.254–255), et non p.252–253.
- **Deux irrégularités du gabarit**, à ne pas prendre pour des trous de transcription :
  - la **نافذة نصّ مطوّل du مبحث 2 ne porte AUCUN questionnaire imprimé** (ni أسئلة ni مهام) —
    contrairement au gabarit habituel ; le guidage tient aux seules annotations marginales et à la
    numérotation des lignes. La p.269 n'est que deux illustrations légendées ;
  - la double page par سند **n'est pas systématique** : les سندات 9 et 13 tiennent sur une seule
    page, le 10 déborde sur p.238–239 ; les سندات 11, 12, 13 et 16 n'ont **aucun** encadré هامش.
- **Quatre notices d'auteur sont des renvois** à un autre سند (10→7, 13→9, 14→7, et le هامش 3 du
  سند 14→11) : la génération devra les résoudre plutôt que de les citer telles quelles.
- `[?]` p.245 : portrait non légendé sur un texte à deux voix (فانفلي / لوموانيو) — attribution
  indéterminable. `[sic]` relevés : « الأنساق العلامات » (p.228) et la pagination `pp 521-621`
  de René Thom (p.241), tous deux confirmés à 300 dpi ; « Karl POPER » avec un seul P (p.264) ;
  `Van Frassen`, `Maxwel`, « أكتشف », « البشرى », « هيّ ».
- ⚠️ **R-7 NON FAITE sur le مبحث 2.** La relecture indépendante par sondage dirigé (T-8) n'a pas
  eu lieu : le registre porte donc `r7: null` et le statut reste `partielle` — jamais
  `validee-r7`. Elle doit être menée **avant toute promotion**, et de préférence avant le LOT B.
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
  **Le مبحث 2 est fait** (p.215–270, profondeur de génération). Ordre de reprise conseillé pour
  les quatre chapitres restants — du plus court au plus long, pour amener une classe au générable
  au plus vite : **3.2 الأخلاق** (p.347–402, 56 p.), puis **3.1 الدّولة** (p.271–346, 76 p.), puis
  **1.2 الخصوصيّة والكونيّة** (p.115–214, 100 p.), puis **1.1 الآنيّة والغيريّة** (p.6–114, 109 p.).
  **Ne pas relire** p.1–6, **p.215–270** ni p.404–408 (T-2/R-4).
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
