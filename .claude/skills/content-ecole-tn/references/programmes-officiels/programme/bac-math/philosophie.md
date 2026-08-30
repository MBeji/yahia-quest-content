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
>   **p.271–402 — tout le محور 3 (مبحث 3.1 الدّولة et مبحث 3.2 الأخلاق), à profondeur de génération**,
>   p.404–408 (فهرس الكتاب intégral).
>   **Transcrit le** : 2026-08-04 → 2026-08-23. **Statut** : **`partielle` / profondeur `mixte`** —
>   ossature sur tout le programme, **profondeur de génération sur 3 chapitres sur 5** : le مبحث 2
>   et les deux مباحث du محور 3. ⚠️ Le محور 3 **n'a pas encore passé sa R-7** (voir §6).
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

#### مبحث 1.1 — الآنيّة والغيريّة — transcription PARTIELLE (p.6–74, سندات 1→29)

> ✅ **Portée : p.6–74** — l'ouverture du **محور 1** (p.6), la **نافذة مدخل intégrale** (p.7–14 :
> les trois وضعيّات استكشافيّة — غرامشي, أبيكتات, باسكال — et الأبعاد الإشكاليّة), et la
> **نافذة سندات intégrale** (p.15–74) : les **29 سندات**, un par un, à profondeur de génération.
> ⛔ **Ne sont PAS transcrits** : la نافذة دعائم (p.75–99), la نافذة كيفيّات التفكير (p.100–103),
> le نصّ مطوّل de **ديكارت** — *التأمّلات الميتافيزيقيّة*, التأمّل الثاني (p.104–112) — et les
> مختصرات (p.113).
> Ce مبحث **n'est donc pas encore générable** : il ne figure pas dans `chapitresGeneration`.
> **Source** : manuel élève `210402` (كتاب الفلسفة — السّنة الرّابعة من التّعليم الثانوي —
> الشّعب العلميّة, CNP).
>
> ✅ **Ce que la tranche p.47–74 débloque** : les notices d'auteur de **بودريار** (p.60) et de
> **فرويد** (p.64), cibles des deux renvois du مبحث 3.2 qui pointaient jusqu'ici dans le vide.
>
> ⚠️ **Assemblé de TROIS lectures indépendantes** — p.6–39, p.40–46, p.47–74. Les deux dernières
> ont livré leur bloc § Notes ; **la première a été coupée avant le sien.** La tranche **p.6–39**
> n'a donc **pas d'inventaire d'anomalies propre** : c'est le trou connu de ce chapitre, à couvrir
> en priorité par la R-7.
>
> ⚠️ **Un constat né de la confrontation des fragments, qu'aucun lecteur seul ne pouvait faire** :
> le **سند 16 (سارتر)** porte **deux encadrés-citation, un par page** — « إنّ الخجل هو بالطبيعة
> اعتراف… » (p.46) et « أخجل من نفسي كما أظهر للآخرين » (p.47). Chacun des deux transcripteurs
> n'en voyait qu'un et en concluait, à tort, que l'autre page n'en portait pas. Vérifié sur les
> deux pages. **Le gabarit « un encadré par سند » n'est pas une règle de ce manuel.**
>
> ⚠️ **Numérotation** : « 1.1 » est une convention de la fiche. Le manuel imprime une pastille
> **`1`** à côté du titre `الآنيّة والغيريّة` — c'est le **مبحث 1 du محور 1**.

---

##### § Ouverture du محور 1 — الإنساني بين الكثرة والوحدة — p.6

**Page de garde du محور** (page pleine, sans texte courant).

- **Bandeau-titre (crème, en haut)** : **الإنساني بين الكثرة والوحدة**
- **Illustration** : photographie/peinture de **masques de théâtre** (un grand masque blanc souriant
  au premier plan sur fond bleu, un masque bleu à bouche ouverte à droite, un petit masque bleu et
  un losange rouge en bas à gauche). Cadre noir double.
- **Pastille bleue** : **1** — numéro du مبحث qui s'ouvre.
- **Cartouche ovale vert** : **الإنيّة والغيرية**
  ⚠️ Graphie imprimée : `الإنيّة` (avec shadda sur le ي) mais `الغيرية` **sans** shadda. Vérifié à 600 dpi.
- **Colonne bleue des notions du مبحث** (5 notions, de haut en bas) :
  **التّاريخ · الجسد · الذات · اللاّوعي · الوعي**

**Encadré-citation d'ouverture (cadre rouge, colonne de droite) — verbatim** :
> يا أحبّاء الإنسانيّة وأحبّاء ما هو أقدس الأشياء لديها! اقبلوا ما يبدو لكم أنّه الأكثر جدارة
> بالاعتقاد، وذلك بعد تمحيص صادق، سواء تعلّق الأمر بوقائع أو بمبادئ تعود إلى العقل. لكن لا تنكروا
> على العقل ما يجعله الخير الأسمى على وجه البسيطة، أي امتيازه بأنه المحكّ الأخير للحقيقة، وإلاّ
> كنتم غير جديرين بهذه الحرّيّة، وفقدتموها بالتّأكيد وحمّلتم، زيادة على ذلك، عبء هذه النّكبة لتلك
> الطّائفة الكبيرة من الأبرياء الذين لولا ذلك لكانوا على استعداد لممارسة حرّيتهم بشكل قانونيّ، ومن
> ثمّ بشكل نهائيّ أيضا من أجل خير هذا العالَم.

**Attribution imprimée sous l'encadré (2 lignes)** :
> ▲ **امنوال كانط**
> **ما التوجه في التفكير؟**

⚠️ Graphie du prénom telle qu'imprimée : **`امنوال`** (et non `إمانويل`), vérifié à 600 dpi.
⚠️ Le titre est imprimé **ما التوجه في التفكير؟** — pas de tashkîl, pas de « ه » d'orientation.
Aucune référence bibliographique (ni éditeur, ni page, ni ligne latine) n'accompagne cet encadré.

---

##### § نافذة 1.1.1 — مدخل إلى التفكير في المسألة — p.7-14

###### Page d'ouverture de la نافذة — p.7

- **Titre de la نافذة (bandeau en haut à droite, sur deux lignes)** : **مدخل إلى** / **التفكير في المسألة**
- **Illustration** : sculpture monochrome ocre — **un homme assis sur un rocher, penché en avant,
  la main au menton** (posture du penseur), un outil/burin posé sur la pierre.
- **Encadré-citation (cadre rouge, colonne de droite) — verbatim** :
> " من أنا؟ هل أعرف نفسي؟ وصلوا إلى القمر يفتحون صفحة جديدة في سفر التكوين الإنساني. سرت قليلا،
> تعلّمت قليلا. امتلكت ثروة كالبحر، وأنا الآن واضع يديَّ على أرض يجري فيها الذهب أنهارا. حاولت أن
> أخرج من بدائيّتي الزراعيّة إلى عالم الصناعة والآلة. حاولت أن أدخل العالم الحديث... "
- **Attribution imprimée (2 lignes)** :
> ▲ **أدونيس**
> **فاتحة لنهاية القرن**

Aucune référence bibliographique complète, aucune ligne latine.

---

###### وضعيّة استكشاف أولى — أنطونيو غرامشي — p.8-9

- **Numérotation imprimée** : pastille rouge **1**, bandeau gris **وضعية استكشاف أولى :**
- **Auteur tel qu'imprimé** : signature du texte **أنطونيو غرامشي** ; notice marginale **غرامشي**.
  Deux graphies sur la même page.
- **Consigne « أستحضر تمثلاتي… » (encadré vert clair, en haut à droite)** :
> **أستحضر تمثلاتي…**
> ... وأقترح جوابا عن السؤال ˝ ما الإنسان؟ ˝ :
  (suivi de **2 lignes pointillées** à remplir par l'élève.)
- **Bandeau gris de consigne** : **أتابع التفكير: أقرأ النص بتأنٍّ، أتأمل الصورة، وأفكر…**
- **Illustrations (p.8)** : (a) **portrait photographique** de Gramsci en médaillon, en tête du
  texte ; (b) **image en couleurs** (profil de visage humain dessiné par des traits de lumière
  jaunes et rouges sur fond sombre), avec sa consigne propre.
- **Consigne de l'image (verbatim)** :
> ▲أتأمل هذه الصورة، أتأولها وأتثبّت إن كانت تعكس التساؤلات التي طرحها غرامشي.

**Thèse (reformulée)** : la question « qu'est-ce que l'homme ? » est la question première et
fondamentale de la philosophie, mais elle **ne se laisse pas résoudre en cherchant une définition
de l'homme dans chaque individu pris à part** : ce qui importe n'est pas l'homme particulier.
Demander « qu'est-ce que l'homme ? », c'est en réalité demander **ce que l'homme peut devenir** —
s'il peut maîtriser son propre destin, se « faire » et se créer une vie. Gramsci pose donc que
**l'homme est le mouvement de ses actes**, que la question **n'est ni abstraite ni « objective »**
mais naît de notre réflexion sur nous-mêmes et sur les autres, et qu'elle vise à savoir, dans les
conditions de la vie **présente**, dans quelles limites nous sommes les « fabricants » de nous-mêmes,
de notre vie et de notre destin.

**Source imprimée (3 lignes, sous le texte)** :
> **أنطونيو غرامشي**
> **من كتاب " غرامشي: دراسات مختارة "**
> **منشورات** وزارة الثقافة، دمشق 1972، ص 184 — 185

⚠️ Ponctuation vérifiée à 1200 dpi : c'est bien une **virgule arabe** `،` après `1972`, non un point.
⚠️ Aucune ligne bibliographique en caractères latins pour ce texte.

**Notice marginale (verbatim, p.8, à gauche sous l'image)** :
> ◄ **غرامشي** : (1891—1937) مفكر إيطالي، ماركسي النزعة، حوكم في عهد الفاشية (1926) وأودع السجن
> حيث توفي.

⚠️ Intervalle **(1891—1937)** — vérifié à 1200 dpi. Ordre **correct** (naissance puis mort) dans le
sens de lecture arabe. *Aucune* inversion ici (voir § Notes, « fausses pistes »).

**المهامّ (verbatim, p.9 — encadré rose, 6 puces)** :
- ما الذي يجعل السؤال عن الإنسان يحوز هذه المكانة في الفلسفة؟
- هل يمثّل هذا السّؤال جزءا من اهتماماتي؟ أعلّل جوابي؟
- أحدّد الدلالات المختلفة التي يمكن أن يحملها السؤال عن الإنسان؟ أمتضاربة هي أم متكاملة؟
- إذا كان السّؤال: ما الإنسان؟ " ليس سؤالا مجرّدا وموضوعيّا " فهل يمكن أن أبحث له عن جواب مجرّد وموضوعيّ؟
- إذا كان هذا السؤال قديما في الفلسفة فما الذي يبرر إعادة طرحه اليوم ؟ أحرر فقرة أبحث فيها عن راهنيّة هذا السؤال.
- في ضوء المهام التي أنجزتها، هل حافظ جوابي الذي اقترحته في البداية على وجاهته أم أحتاج إلى مراجعته؟ أعلّل جوابي.

**Illustration (p.9, sous l'encadré des مهامّ)** : reproduction d'un **tableau** (fond brun et bleu
gris, un **œil** émergeant d'un visage partiellement recouvert d'une matière jaune, deux
**empreintes de pieds** vert-jaune dans la partie droite, cadre jaune ; signature de l'artiste en
bas à droite, **illisible** à 600 dpi). Aucune légende, aucun cartel imprimé.

---

###### وضعيّة استكشاف ثانية — أبيكتات — p.10-11

- **Numérotation imprimée** : pastille rouge **2**, bandeau gris **وضعية استكشاف ثانية :**
- **Auteur tel qu'imprimé** : signature **أبيكتات** ; notice **أبيكتات** + ligne latine
  **`EPICTETE`** ; la ligne latine de source porte **`Epictète`**. Le mot **الطاغيّة** désigne
  l'interlocuteur, non un auteur.
- **Bandeau gris de consigne** : **أقرأ النص وأتابع الحوار الدائر بين الطاغيّة وأبيكتات:**
- **Illustration** : **gravure ancienne** — buste de profil d'un vieillard barbu drapé, portant en
  haut la légende gravée **`EPICTETVS`** (graphie latine avec V, lisible à 600 dpi).

**Thèse (reformulée)** : ce n'est pas le tyran qui enchaîne l'homme, ce sont **ses propres
opinions**. Un homme libre par nature **ne peut être troublé ni empêché par un autre que par sa
propre volonté** ; face à la menace « je vais t'enchaîner la jambe », celui qui donne du prix à sa
jambe supplie, mais celui pour qui seule sa volonté a du prix répond : « enchaîne-la ». Le maître ne
peut asservir que le corps : **l'esclave est celui qui prend son corps pour lui-même**, et le tyran
qui croit posséder un homme ne possède que « ce cadavre qu'est mon corps ».

**Source imprimée (2 lignes)** :
> **أبيكتات، محاورات، من كتاب " الرواقيون "**
> `Epictète`, *`Entretiens`*,`in Les Stoïciens, La Pléiade, Gallimard. p. 853`

**هامش (1 note, encadré vert, en marge basse de la p.10) — verbatim** :
> **(1) زوس** `Zeus` — إله الآلهة في الميثولوجيا الإغريقيّة. يتّصف بالصرامة والعدل.

**الكاتب (notice, p.10 — bandeau rose « الكاتب : ») — verbatim** :
> **أبيكتات** `EPICTETE` ( 50 — 130 ) : كنية لأحد الفلاسفة الرواقيين، وتعني في اللغة الإغريقيّة
> العبد أو الخادم. يكمن جوهر مذهبه الأخلاقي في دعوته إلى الحريّة الداخليّة، إذ يعتبر أن السيّد سيّد
> أهوائه وآرائه والعبد عبد أهوائه وآرائه، لذلك أقرّ بحريّة الإنسان المطلقة سواء كان على العرش أو
> مقيّدا بالأغلال. وتكمن السعادة لديه في الـ " أتاراكسيا " `Ataraxie` وهي سكينة النفس الناشئة عن
> العيش وفق مبادئ العقل أي في توافق مع قوانين الطبيعة. وتعبّر فلسفته عن الاحتجاج السلبي للمقهورين
> ضدّ العبوديّة.

⚠️ Intervalle **( 50 — 130 )** — vérifié à 600 dpi, ordre correct. Aucune mention « ق.م / م ».

**المهامّ (p.11) — bandeau gris : « المهـام: أتقمّص الأدوار »** — trois blocs.

**Bloc de droite — « أتقمّص دور الطاغيّة… » (5 puces, verbatim)** :
- ما الذي يبرّر قولي: " سأقيّد رجلك ".
- لِمَ عليَّ أن أنتزع من هذا العبد اعترافه بي سيّدا؟
- لِمَ يقتضي هذا الانتزاع تعذيب الجسد؟
- لقد قهرتني لامبالاة هذا العبد. ماذا عليّ أن أفعل حتى أحطّم قدرته على التحمّل، وهو العبد؟
- لِمَ لا أجد حرجا أخلاقيّا في ممارسة التعذيب؟

**Bloc de gauche — « أتقمّص دور أبيكتات… » (5 puces, verbatim)** :
- لِمَ لا يزعجني أن يقيّد هذا الطاغية رجلي؟
- لِمَ يستحيل عليه أن يكون سيّدا عليّ؟
- كيف لي أن أبدّد أوهامه حول ما تكونه ذاتيّتي؟
- يعتقدني عبدا وأنا الحرّ، كيف لي أن أُقنعه بهذا؟
- يعتقد نفسه سيّدا وهو العبد، كيف لي أن أُقنعه بهذا؟

**Bloc vert du bas — « أستعيد موقعي وأفكّر من جديد… » (4 puces, verbatim)** :
- أستخلص وجه التعارض بين صورتَيْ الإنسان لدى الطاغية وأبيكتات؟
- أيّ الصورتين تعكس تمثّلي لذاتي؟
- كيف لي أن أبني صورة أراها جديرة بإنسانيّة الإنسان؟
- أصوغ بعض الأسئلة التي تمكّنني من التقدّم في اتجاه بناء صورة كلّية للإنسان يرتضيها معي الطاغيّة
  وأبيكتات في آن.

⚠️ **Le titre du bandeau est imprimé `المهـام` (sans shadda)** en p.11, alors qu'il est `المهـامّ`
(avec shadda) dans les encadrés roses des p.9 et p.13. Variante imprimée, non corrigée.

---

###### وضعيّة استكشاف ثالثة — باسكال — p.12-13

- **Numérotation imprimée** : pastille rouge **3**, bandeau gris **وضعية استكشاف ثالثة :**
- **Auteur tel qu'imprimé** : signature **باسكال** ; notice marginale **باسكال** ; ligne latine
  **`Blaise Pascal`** ; encadré-citation p.13 signé **باسكال**.
- **Consigne « أستحضر تمثلاتي… » (encadré gris, en haut à droite)** :
> **أستحضر تمثلاتي…**
> أحبّ الكثيرين من حولي، لكن ما الذي أحبّه فيهم؟
  (suivi de **3 lignes pointillées**.)
- **Bandeau gris de consigne** : **أتابع التفكير: أقرأ النص قراءة متأنيّة وأفكّر في مضمونه ….**
- **Illustration** : **gravure** — portrait de Blaise Pascal en buste, longue chevelure, main
  repliée sous le menton (médaillon inséré dans le texte, p.12).

**Thèse (reformulée)** : celui qui, à la fenêtre, regarde passer les gens **n'aime personne « pour
lui-même »** — il ne pense pas à moi en propre. Aimer quelqu'un pour sa beauté n'est pas l'aimer
vraiment, puisque la petite vérole, qui tue la beauté **sans** tuer la personne, mettrait fin à cet
amour ; il en va de même si l'on m'aime pour la justesse de mon jugement ou la vivacité de ma
mémoire, car **je peux perdre ces qualités sans me perdre moi-même**. Où est donc ce moi, **s'il
n'est ni dans le corps ni dans l'âme** ? On n'aime jamais **la substance** d'une personne, seulement
des **qualités empruntées et périssables** ; il ne faut donc pas se moquer de ceux qui recherchent
les honneurs et les titres.

**Source imprimée (2 lignes)** :
> **باسكال، خواطر، فقرة 323**
> `Blaise Pascal`, *`Pensées`*, `in œuvres, Le Seuil, p. 591`

**Notice marginale (encadré vert, p.12) — verbatim** :
> **باسكال** (1623—1662) — عالم وفيلسوف فرنسي. اهتمّ بالبحث العلمي منذ حداثة سنّه ( 16 سنة ).
> اخترع آلة حسابية وهو في السنّ 19 من عمره ( 1642 ).

⚠️ Intervalle **(1623—1662)** — ordre correct.
⚠️ Il n'y a **pas** d'encadré هوامش pour cette وضعيّة (aucune note appelée dans le texte de la p.12).

**المهامّ (verbatim, p.13 — encadré rose, 6 puces)** :
- " الصفات والخصال ": إلامَ يُحيل هذان المعنيان؟
- أية علاقة لهما بتجربة الحبّ؟
- أيّة منزلة لهما في تحديد حقيقة الذات الإنسانيّة؟
- هل تفترض تجربة الحبّ تصوّرا ضمنيّا للإنسان؟
- أعود إلى تمثّلاتي الأوّلية وأكشف عمّ تفترضه من تصوّر للإنسان.
- فيم يُربك موقف باسكال تصوّري للإنسان؟ وفي أيّ اتجاه يمكن إعادة تأسيس هذا التصوّر؟ أعبّر عن هذا
  الاتجاه في صيغة أسئلة.

**Illustration (p.13)** : image bleue — **silhouette de tête humaine** de profil, sombre, portant en
son centre un **grand point d'interrogation** clair, sur fond bleu ciel.

**Encadré-citation (p.13, cadre rose, à droite de l'image)** :
> " أين هيّ إذن هذه الأنا إن لم تكن في الجسم ولا في النفس؟ "
> — **باسكال**

⚠️ Graphie imprimée **`هيّ`** (avec shadda) dans l'encadré, comme dans le corps du texte p.12.

---

###### الأبعاد الإشكاليّة للمسألة — p.14

Page-atelier entièrement **à remplir par l'élève** (aucun contenu doctrinal imprimé).

- **Titre (bandeau)** : **الأبعاد الإشكاليّة للمسألة** — précédé, à gauche, d'un carré rose portant
  un **« ؟ »**.
- **Bandeau gris de consigne** : **أستعيد تأملاتي السابقة تأسيسا للمتابعة وأُنجز المهام التاليّة:**

**Tâche 1 (bandeau rose, n° 1)** :
> " مَنْ أكون ؟ " ما قيمة هذا السؤال ؟
  → bloc vert de **3 lignes pointillées**.

**Tâche 2 (bandeau rose, n° 2)** :
> ما هي أهمّ الأسئلة التي يمكن أن أطرحها في علاقة…
  → **deux colonnes** vertes, chacune numérotée **1 à 5** (lignes pointillées terminées par « ؟ ») :
  colonne de droite **مع ذاتي؟** — colonne de gauche **مع الغير؟**
  → bandeau orange sous les deux colonnes :
> أنتبه، في صياغة الأسئلة، إلى معاني: التاريخ، الجسد، الذات، اللاوعي، الوعي.

⚠️ Ici les notions sont imprimées **sans shadda** (`التاريخ`, `اللاوعي`), alors que la page
d'ouverture du محور (p.6) imprime `التّاريخ` et `اللاّوعي`. Variante de graphie interne au chapitre.

**Tâche 3 (bandeau rose, n° 3)** :
> أشتغل على الأسئلة: أوّلف بينها، أميّز بين مستويات طرحها وأصوغها في مشكلات فلسفية:
  → bloc vert de **3 lignes** numérotées 1 à 3.
  → bandeau orange :
> أنتبه، في صياغة المشكلات، إلى التمفصل المنطقي بينها، راهنيّتها، وانهمامي بها…

**Tâche 4 (bandeau rose, n° 4)** :
> أحدد رهاناتي من التفكير في هذه المشكلات
  → bloc vert de **3 lignes** numérotées 1 à 3.

---

##### § نافذة 1.1.2 — سندات للتفكير في المسألة — p.15-46 (et au-delà)

###### Page d'ouverture de la نافذة — p.15

- **Titre de la نافذة (bandeau en haut à droite, sur deux lignes)** : **نافذة سندات** / **للتفكير في المسألة**
- **Illustration 1 (haut)** : photographie d'un **document manuscrit ancien** (encre brune, écriture
  anglaise cursive, bord brûlé) sur lequel reposent des **lunettes rondes** à monture noire.
- **Encadré-citation 1 (cadre rouge)** :
> " علينا أن نتعلّم من جديد أن نبصر، أن نتصوّر، أن نفكّر وأن نفعل. نحن لا نعرف الدّرب ولكنّنا نعرف
> أنه يُنحت بفعل المسير .. "
> ▲ **ادغار موران**
> **البدء الجديد**

⚠️ Graphie imprimée **`ادغار موران`** (sans hamza sur le alif). Le même auteur reviendra au
**سند 13** sous la graphie **موران** (voir p.40).

- **Illustration 2 (bas)** : image — **silhouette humaine noire debout à l'intérieur d'un anneau /
  d'une sphère orange** ouverte, sur fond de ciel bleu et de sol clair.
- **Encadré-citation 2 (cadre rouge)** :
> " إنّ قدرة الإنسان على امتلاك الأنا في تمثّله تسمو به غاية السمو فوق سائر الكائنات الحيّة الأخرى
> على وجه الأرض، وبذلك يكون شخصا ".
> **كانط**

Aucune des deux citations ne porte de référence bibliographique.

---

###### سند 1 — فويرباخ / Ludwing FEUERBACH — « الوعي ميزة إنسانيّة » — p.16-17

- **Auteur tel qu'imprimé** : signature du texte **فويرباخ** ; ligne latine **`Ludwing FEUERBACH`** ;
  notice **الكاتب** : **فويرباخ: ( 1804 – 1872 )**. Encadré-citation p.17 signé **فويرباخ**.
  ⚠️ À l'intérieur même de la notice, la graphie **flotte** : `فويرباخ` et **`فيورباخ`**
  (dont `فيورباخيين`). Les deux formes coexistent sur la même page. Vérifié à 600 dpi.
  ⚠️ **`Ludwing`** [sic] sur la ligne latine — vérifié à 600 dpi (la forme usuelle est *Ludwig*).
- **Titre du سند** : **الوعي ميزة إنسانيّة**
- **Source imprimée (2 lignes)** :
  **فويرباخ، ماهيّة المسيحيّة.**
  `Ludwing FEUERBACH, L'Essence du Christianisme, ch 1, Gallimard, 1960`
- **Illustrations** : (p.16) **portrait photographique** de Feuerbach, barbu, en médaillon dans le
  texte ; (p.17) **photographie couleur d'un chimpanzé** en posture de « penseur », main au menton,
  sur fond de feuillage vert ; à sa droite, **dessin au crayon** du buste d'un homme âgé au front
  dégarni, de face.

**التمهيد (verbatim)** :
> يبدو أنّ مطلب تعريف الإنسان مطلب عسير نظرا لطبيعته الملتبسة والملغزة ، و لعلّ في هذا العُسر ما
> يدفعنا إلى مقارنته بما ليس هو عسانا نمسك بما ينير سبيل البدء في تعريفه.

**Thèse (reformulée)** : à la question « quelle est la différence essentielle entre l'homme et
l'animal ? », la réponse la plus simple et la plus répandue est : **la conscience**. Mais Feuerbach
distingue deux sens. Au sens large — sentiment de soi, discrimination des choses sensibles,
perception et jugement des choses extérieures — **la conscience ne peut pas être refusée à
l'animal**. Au sens strict, elle **n'appartient qu'à l'être qui prend son propre genre et sa propre
essence pour objet** : l'animal est bien objet pour lui-même en tant qu'**individu** (d'où son
sentiment de soi) mais **non** en tant qu'**espèce** — et c'est pourquoi la conscience lui manque.
D'où : là où il y a conscience il y a science, et la science est conscience des espèces. L'animal
n'a qu'une vie **simple** (vie intérieure et vie extérieure ne font qu'un), l'homme a une vie
**double** ; il pense, c'est-à-dire qu'il **s'adresse à autrui et se parle à lui-même**. L'animal ne
peut accomplir aucune fonction générique sans un autre individu hors de lui ; l'homme, **sans la
présence d'aucune autre personne**, accomplit la fonction générique de la pensée et de la parole.
L'homme est donc **à lui-même un « je » et un « tu » à la fois** : s'il peut occuper la place de
l'autre, c'est précisément parce que son objet n'est pas son individualité mais son genre et son
essence.

**الهامش (verbatim, p.17 — encadré rose « الهامش », 1 seule note)** :
> 1– لاحظ التقارب الاشتقاقي في اللسان الفرنسي بين `" science "` `" conscience "`

⚠️ Sur la page, les deux termes latins sont composés **sans « و » ni virgule** entre eux, et le mot
`conscience` est imprimé **à gauche** de `science` : dans le sens de lecture arabe (droite→gauche),
`science` vient donc en premier. Vérifié à 600 dpi.

**الكاتب (notice, p.16-17) — verbatim** :
> **فويرباخ: ( 1804 – 1872 )** — فيلسوف مادي ألماني، وقع فصله من الجامعة بسبب كتابه " أفكار حول
> الموت والخلود " ( 1830 ). وقد تطورت آراؤه حول الموقف من الدين من أفكار الشبان إلى المادية، وقد
> أثر إعلانه المادية ودفاعه عنها تأثيرا عظيما على معاصريه. وكتب **أنغلز** عن أثر كتاباته " كان
> الحماس عاما وصرنا جميعا فيورباخيين دفعة واحدة " .. وكان نقد **فويرباخ** لتصوّر هيغل المثالي لجوهر
> الإنسان ورده الإنسان إلى وعي الذات النقطة المبدئية في تطور فكر **فيورباخ** الفلسفي كما ظهر في
> مؤلفه " في نقد الفلسفة الهيغلية " ( 1839 )، غير أنه لم يتابع السير على خط ماديّ متماسك إذ كان
> يعتبر الإنسان فردا مجردا، كائنا بيولوجيا محضا، وظل **فيورباخ** صاحب مواقف مثالية، وهي مثالية بدت
> واضحة بشكل خاص في فهمه للتاريخ وللأخلاق، فقد كان يعتبر الدين اغترابا وتحققا موضوعيا للسمات
> الإنسانية التي كان يعزو إليها جوهرا خارقا للطبيعة في كتابه " جوهر المسيحية " ( 1841 ). فالإنسان
> يزدوج ويتأمل جوهره في الله، وهكذا يكون الدين وعي الذات اللاواعي لدى الإنسان. وذهب إلى أن التربية
> هي الملاذ للتحرر من الدين " أسس فلسفة المستقبل " ( 1843 )، أما فيما يتعلق بالأخلاق " الموضوعات
> الجارية لإصلاح الفلسفة " ( 1842 ) فقد حدد مبادئه الأخلاقية اعتمادا على سعي الإنسان الغريزي إلى
> السعادة، وكان يعتقد أن تحقيقها ممكن شريطة أن يحدّ كل فرد وبطريقة عقلية من مطالبه وأن يحب الآخرين،
> والأخلاق التي بناها **فيورباخ** مجرّدة وأبدية.

⚠️ Intervalle **( 1804 – 1872 )** — ordre correct, vérifié à 600 dpi.
⚠️ Les titres d'œuvres cités dans la notice sont imprimés **en couleur** (bleu ciel), sans ligne
latine ni éditeur.

**المهام (verbatim, p.17 — encadré rose « المهـام », 7 puces)** :
- بأيّ معنى يتحدّث فويرباخ عن وعي لدى الحيوان؟
- هل من تماثل بين الوعي لدى الحيوان والوعي لدى الإنسان؟ أعلّل جوابي.
- أستخلص دلالة " الوعي الإنساني " وتمظهراته.
- كيف أفهم قول الكاتب " فالإنسان هو بالنسبة إلى نفسه أنا وأنت في آن " ؟
- هل من وجاهة في القول بالوعي محدّدا نوعيّا للإنسان؟
- هل تساعدني مقاربة الكاتب لتفكيك علاقة الكثرة بالوحدة حين تتعلّق بالشأن الإنساني؟
- أستحضر دلالة " للكلّي " وأتبيّن في ضوئها قيمة الوعي بالنسبة إلى الإنسان. أحرّر فقرة في الغرض.

**Encadré-citation (p.17, cadre rose, entre les deux images)** :
> " ما الفرق الأساسي بين الإنسان والحيوان؟ "
> **فويرباخ**

---

###### سند 2 — ابن طفيل — « الذّاتُ نَفْسٌ » — p.18-19

- **Auteur tel qu'imprimé** : signature **ابن طفيل** ; notice **ابن طفيل** ; encadré-citation p.19
  signé **ابن طفيل**. **Aucune ligne latine** (convention du manuel pour les auteurs arabes).
  ⚠️ Le corps de la notice écrit une fois **`بن طفيل`** sans « ا » (`استمدّ بن طفيل شهرته`).
- **Titre du سند** : **الذّاتُ نَفْسٌ** (imprimé entièrement vocalisé).
- **Source imprimée (1 seule ligne)** :
  **ابن طفيل. حي بن يقظان؛ منشورات دار الآفاق الجديدة بيروت، ط2, ص 178 — 179**
  ⚠️ Ponctuation imprimée irrégulière : un **point** après `ابن طفيل`, un **point-virgule** après
  `حي بن يقظان`, et une **virgule latine `,`** (non arabe) après `ط2`.
- **Illustration** : **dessin au trait** (encre) d'un visage d'homme de trois quarts, coiffé, avec
  une **inscription manuscrite arabe** en bas à droite du cadre — non déchiffrable à 600 dpi.

**التمهيد (verbatim)** :
> اقترن التفكير في الإنسان بالتفكير فيما ليس هو، وكأنّه شرط الذات للمرور إلى ذاتها. قد يتحوّل حينها
> الوعي بالذات إلى ضرب من استلهام للمطلق يمّحي فيه طلبا للإثبات.

**Thèse (reformulée)** : ayant saisi l'Être absolu nécessaire **par son essence même**, le
personnage découvre que cette essence par laquelle il l'a saisi **n'est pas corporelle** et
qu'aucune propriété des corps ne peut lui convenir : tout ce qu'il perçoit du dehors de lui-même,
du côté de la corporéité, **n'est pas** la vérité de son essence. Son corps lui devient alors sans
importance. Examinant si cette essence noble peut périr, se corrompre et se dissoudre, il conclut
que **corruption et dissolution sont des propriétés des corps** — qui quittent une forme pour en
revêtir une autre (l'eau devenue air, la terre devenue plante). Ce qui **n'est pas un corps**, ce
qui **n'a pas besoin d'un corps** pour subsister et qui est exempt de toute corporéité, **ne peut
donc absolument pas être conçu comme corruptible**.

**الهامشان (verbatim, p.19 — encadré rose « الهامشان », 2 notes)** :
> 1– " حي بن يقظان " هو بطل القصّة الخيالية التي وضعها ابن طفيل.
> 2– يعود الضمير إلى " واجب الوجود " ويعني الله أو " الموجود الشريف "، ويُسمّى واجب الوجود لأنّ
> وجوده يكون من ذاته ولا يحتاج إلى شيء أصلا ( الجرجاني، التعريفات ). وهو " الذي لا يمكن أن يكون
> وجوده من غيره "، ويقابله " ممكن الوجود، " وهو " الذي متى فُرض غير موجود أو موجود لم يعرض عنه
> محال " ( ابن سينا، رسالة الحدود ).

⚠️ Guillemet mal placé dans la note 2, tel qu'imprimé : **`" ممكن الوجود، "`** — la virgule tombe
**à l'intérieur** du guillemet fermant.

**الكاتب (notice, p.18) — verbatim** :
> **ابن طفيل: ( 500 – 581 هـ )؛ ( 1102 – 1185 )** — هو أبو بكر بن محمد بن طفيل القيسي، فيلسوف أندلسي
> اشتغل بالطبّ وعمل وزيرا لدى الخليفة أبي يعقوب يوسف ثاني خلفاء الموحدين في مراكش. استمدّ بن طفيل
> شهرته من جهده الشخصي في طلب العلم واستخرج جلّ علمه من الكتب حتّى غدا من أعلام العصر المعدودين. كان
> سببا في شرح ابن رشد لفلسفة أرسطو وقد ساعده على تأليف كتاب " الكليات في الطب " تميّز بآرائه في
> الفلك وقيل إنّه كان طبيبا بارعا. ضمّن آراءه الفلسفيّة كتابه المشهور " حي بن يقظان " المصنّف الوحيد
> الذي عرف عنه لقلة إنتاجه على غزارة علمه، وفيه بسط مبادئ الفلسفة المشرقيّة وبيّن اختلافه عن فلاسفة
> الإسلام في مسائل عديدة، مما جعله فيلسوفا متفرّدا.

⚠️ **Double intervalle** hégirien puis grégorien : `( 500 – 581 هـ )؛ ( 1102 – 1185 )` — le second
**sans** la lettre `م` (contrairement à celui d'Ibn Sina, p.20, qui porte `1037م`). Ordres corrects.

**المهام (verbatim, p.19 — encadré rose, 7 puces)** :
- أيّهما يشترط الآخر: إدراك الذات أم إدراك " واجب الوجود "؟
- كيف أفهم هذا التشريط؟
- ما طبيعة الذات عند ابن طفيل؟
- ما حقيقة الجسم منظورا إليه من جهة النفس؟
- ماذا يترتّب عن القول بفساد الجسم حين يتعلّق الأمر بحقيقة الإنسان؟
- بأيّ معنى يُقال عن الجسم إنّه غيريّة؟
- هل أجد في تمثّلاتي ما يتقارب مع أطروحة ابن طفيل؟ أحرّر فقرة في الغرض.

**Illustration (p.19)** : photographie retravaillée en orange et noir — **silhouettes de personnes
marchant de face**, cernées de traits de lumière qui évoquent des flammes.

**Encadré-citation (p.19, cadre rose, à droite de l'image)** :
> " إنّ الفساد والاضمحلال إنّما هو من صفات الأجسام... "
> **ابن طفيل**

---

###### سند 3 — ابن سينا — « في إثبات الإنيّة » — p.20-21

- **Auteur tel qu'imprimé** : signature **ابن سينا** ; notice **ابن سينا** ; encadré-citation p.21
  signé **ابن سينا**. **Aucune ligne latine.**
- **Titre du سند** : **في إثبات الإنيّة**
- **Source imprimée (1 seule ligne)** :
  **ابن سينا، الإشارات والتنبيهات، القسم الثاني ( الطبيعيات ). طبعة سليمان دنيا 1957. ص 320**
- **Illustration** : **portrait peint** d'Avicenne de profil, turban blanc et vêtement sombre
  (médaillon inséré dans le texte, p.20).

**التمهيد (verbatim)** :
> تخبرنا التجربة اليوميّة عن وجودٍ ما نحتلّه في العالم، لكنّ تعيين هذا الوجود وإدراكه عقلا يقتضي
> فيما يقتضي رجوع النفس إلى ذاتها تفحّصا في إنيّتها بما يجعل الذات مليئة بذاتها لا تهزّها عوارض.

**Thèse (reformulée)** : reviens à toi-même et considère — sain, ou même dans certains de tes états
altérés — que **tu ne peux pas être inattentif à l'existence de ton essence, ni cesser de
l'affirmer**, pas même dans le sommeil ou l'ivresse. Suppose maintenant que tu aies été créé d'un
coup, entier et bien constitué, mais **placé de telle sorte que tu ne voies pas tes membres, qu'ils
ne se touchent pas, écartés et suspendus un instant dans un air libre** : tu te trouverais **ignorant
de toute chose sauf de l'affirmation de ta propre ipséité**. Ce qui perçoit **n'est donc pas** ce que
tu perçois par les sens : si tu étais dépouillé de ton apparence et si tes membres changeaient, tu
resterais **toi**. Ibn Sina écarte enfin l'objection selon laquelle « je n'affirme mon essence que
par mon acte » : un acte **absolu** ne prouverait qu'un agent quelconque, non toi ; et un acte
**propre** suppose déjà ton essence, comprise **avant** lui. Donc **ton essence est affirmée non par
l'acte** — elle est ce par quoi l'acte est affirmé.

**هوامش** : **aucun encadré de notes** pour ce سند (ni p.20 ni p.21). Le texte contient en revanche
plusieurs **coupes imprimées** notées `( ... )`.

**الكاتب (notice, p.20-21) — verbatim** :
> **ابن سينا: ( 370 – 429 هـ )؛ ( 980 – 1037م )** — هو أبو علي **الحسن** بن سينا، فيلسوف وطبيب من
> أصل فارسي. تربّى في بيت له " اشتغال بخدمة الدولة "، وتلقى العلوم العقليّة والشرعيّة في بيت أبيه
> وحصّل بنفسه علما غزيرا حينما أذن له الأمير نوح بن منصور بالدخول في دار كتبه. كان ابن سينا فيلسوفا
> موسوعيّا غزير الإنتاج تلتقي في تآليفه جميع المذاهب. فقد مزج بمهارة بين آراء تنوّعت مصادرها من
> إسلاميّة إلى فارسيّة، إلى آراء اليونانيين وخاصّة أرسطو وأفلاطون وأفلوطين... غير أنّه في كلّ هذا
> متفرّد بحكمته المشرقيّة أو نظريّته في التصوّف " فلسفة خاصّة به " كما يؤكّد ذلك بنفسه في كتابه
> " منطق المشرقيين ". كان لابن سينا أثره العميق في الثقافة الإنسانيّة خاصّة بما صنّفه في مجال الطبّ
> " القانون في الطب " والذي ظل مرجعا للأطباء طيلة قرون. لابن سينا كتاب جامع وموسوعة فلسفيّة سمّاها
> " الشفاء " وله أيضا كتاب " النجاة " و " الإشارات والتنبيهات " ورسائل عديدة ( رسالة الطير، رسالة
> القدر، رسالة في النفس الناطقة... ) ومختصرات كتبها في مواضيع شتى.

⚠️ **`أبو علي الحسن بن سينا`** — la notice imprime **`الحسن`**, vérifié à 600 dpi (la forme usuelle
est *الحسين*). Anomalie de la source, non corrigée ici.
⚠️ Intervalles `( 370 – 429 هـ )؛ ( 980 – 1037م )` — ordres corrects, vérifiés à 600 dpi.

**المهام (verbatim, p.21 — encadré rose, 7 puces)** :
- على أيّ وجه تُدرك الذات ذاتها ؟
- ما دلالة صورة " الإنسان المعلّق " في سياق حجاج الكاتب على ثبوت الإنيّة ؟
- هل يستلزم تأكيد الإنيّة توسّط الجسم؟
- ما قيمة التمييز بين " الفعل المطلق " و " الفعل الخاص " في إثبات الإنيّة ؟
- كيف أفْهَمُ هذه العبارة " إنّ فعلك... هو ذاتك عينها " ؟
- أيّ معنى للإنيّة يمكن أن أستخلصه من النصّ؟
- هل لي أن أمتحن وجاهة رؤية ابن سينا في ضوء تمثّلي لذاتي ؟

**Illustration (p.21)** : peinture surréaliste — **un homme en équilibre sur les mains, en appui sur
une sphère mouchetée** posée au bord de l'eau, ciel violet et nuages jaunes.

**Encadré-citation (p.21, cadre rose, à droite de l'image)** :
> " ... وفُرِضَ أنّها على جملة من الوضع والهيئة بحيث لا تُبصَرُ أجزاؤها، ولا تتلامس أعضاؤها بل هي
> منفرجة ومعلقة لحظةً ما في هواء طلق... "
> **ابن سينا**

---

###### سند 4 — ديكارت / DESCARTES — « في يقين الكوجيتو » — p.22-23

- **Auteur tel qu'imprimé** : signature **ديكارت** ; ligne latine **`DESCARTES`** ; notice
  **روني ديكارت: ( 1596 – 1650 )**. Encadré-citation p.23 signé **ديكارت**.
  ⚠️ Trois graphies sur deux pages (`ديكارت` / `DESCARTES` / `روني ديكارت`).
- **Titre du سند** : **في يقين الكوجيتو**
- **Source imprimée (2 lignes)** :
  **ديكارت، التأملات، التأمّل الثاني؛ ترجمة عثمان أمين**
  `DESCARTES, Méditations, Méditation seconde, in œuvres et Lettres, éd.Gallimard, ,pp 772 - 872`
  ⚠️ La ligne latine porte **deux virgules consécutives** avant `pp` (`Gallimard, ,pp`) et une
  pagination **`772 - 872`** (100 pages pour une seule *Méditation*). Les deux vérifiés à 600 dpi ;
  reproduits tels quels.
- **Illustrations** : (p.22) **portrait peint** de Descartes en buste, longue chevelure noire et col
  blanc ; (p.23) **photographie d'une sculpture** — figure humaine nue, ramassée sur elle-même, bras
  repliés, sur fond de drapé.

**التمهيد (verbatim)** :
> بدأت الحداثة بإعلان تصوّر جديد للعالم لم يعد الإنسان، في صورته القديمة، قادرا على التوافق معه. وقد
> كان على الفلسفة أن تضطلع بمهمّة بناء تصوّر جديد للإنسان يؤسّس لذات تجد يقينها في ذاتها وتطلب
> التوافق مع العالم بالسيادة عليه.

⚠️ Le texte s'ouvre sur une formule **imprimée en couleur (cyan)** dans le corps même du texte :
**`أنا كائن، وأنا موجود:`** — mise en évidence typographique, non un titre.

**Thèse (reformulée)** : « je suis, j'existe » est certain — mais **combien de temps ?** Aussi
longtemps que je pense : car s'il se pouvait que je cesse entièrement de penser, **je cesserais du
même coup d'exister**. Je n'admets donc rien qui ne soit nécessairement vrai : je **ne suis** rien
d'autre, à parler exactement, qu'**une chose qui pense** — un esprit, un entendement, une raison,
mots dont j'ignorais le sens auparavant. Et cette chose qui pense est celle qui doute, conçoit,
affirme, nie, veut, ne veut pas, imagine aussi et sent. Descartes s'objecte le rêve et
l'imagination : **la puissance d'imaginer ne me fait pas connaître ce que je suis** et n'est pas
inséparable de mon existence ; de même, sentir, c'est encore **le même moi qui pense**. Même si ce
que je vois et entends n'était qu'apparence trompeuse, **il reste certain qu'il me semble voir,
entendre, avoir chaud** — et cela, proprement, s'appelle **sentir**, et ce n'est rien d'autre que
**penser**. Conclusion imprimée : je commence à me connaître moi-même avec **plus de clarté et de
distinction** qu'auparavant.

**هوامش** : **aucun encadré de notes** pour ce سند (ni p.22 ni p.23). Deux coupes `(...)` imprimées
dans le texte.

**الكاتب (notice, p.23) — verbatim** :
> **روني ديكارت: ( 1596 – 1650 )** — فيلسوف وعالم ( في الفيزياء والرياضيّات ) فرنسي يُعدّ رائد
> الحداثة ومؤسس العلم الحديث، حصل على الإجازة في الحقوق ( 1616 ) ليتفرّغ للبحوث العلميّة والفلسفيّة
> بداية من سنة 1618 ˝ مادام لا شيء يستطيع أن يعوّض الرغبة الجامحة في تعلّم كيفيّة التمييز بين
> الصّواب والخطأ من أجل أن ننظر بوضوح أثناء الممارسة والفعل وأن نمشي بخطى ثابتة كما يقول. اهتمّ
> بالكشف عن قواعد سداد العقل في أحكامه ( " قواعد لتوجيه العقل "؛ كُتب سنة 1628 ونُشر سنة 1701 ).
> تواصل اهتمامه بالجانب المنهجي في " مقالة الطريقة " ( 1637 ) الذي كُتب بالفرنسيّة، على غير عادة
> الفلاسفة، رغبة منه في توسيع دائرة الفكر الفلسفي. رسم ديكارت في هذا الكتاب قواعد التفكير السليم
> بدءا من البداهة وانتهاء إلى المراجعة مرورا بالتحليل والتركيب. وانتهى في " تأمّلات ميتافيزيقيّة "
> ( 1641 ) إلى التأكيد على أن العقل ليس عليه إلاّ أن يعوّل على نفسه لبلوغ الحقيقة في خصوص الوعي
> بالذات وعلاقة النفس بالجسد محدّدا منزلة الإله من خلال ما يسمّيه بـ " الضمان الإلهي ". وفي سنة
> 1644 صدر كتابه " مبادئ الفلسفة " الذي عرض فيه للعموم نسقه الفلسفي ثمّ في 1649 " انفعالات النفس "
> الذي طوّر فيه نظريّة في التحكّم في انفعالات النفس على قاعدة تصوّر لعلاقة النفس بالجسد. أمّا في
> " رسالة في الإنسان " ( 1662 ) فقد سعى ديكارت إلى تحطيم المفاهيم الأساسيّة للفيزياء القديمة وسحب
> الآليّة على الظواهر البيولوجية بما في ذلك الجسم الإنساني. وفي " رسائله مع الأميرة اليزابيت "
> ( من 1643 إلى 1649 ) تعرّض إلى أغلب القضايا التي اهتمّ بها ( النفس، الجسد، الاختيار الحرّ،
> الإلهيات... ).

⚠️ **Guillemet ouvrant jamais refermé** : la citation ouverte après `سنة 1618` (`˝ مادام لا شيء…`)
ne reçoit **aucun guillemet de fermeture** ; la phrase se poursuit jusqu'à `كما يقول.`. Vérifié à
600 dpi sur trois lignes consécutives.
⚠️ Intervalle `( 1596 – 1650 )` — ordre correct.

**المهام (verbatim, p.23 — encadré rose, 6 puces)** :
- أيّة علاقة يقيمها الكاتب بين الوجود والتفكير؟
- كيف أفهم الطابع اليقيني للكوجيتو؟
- أرصد الحجج التي تؤكّد جوهريّة الوعي.
- أحدِّدُ خصائص طبيعة الأنا.
- أحدِّدُ منزلةَ كلٍّ من الفكر والجسم في تحديد دلالة الإنيّة.
- أستخلص دلالة الغيريّة في فلسفة ديكارت.

**Encadré-citation (p.23, cadre rose, à droite de la sculpture)** :
> " أنا أفكّر إذن أنا موجود ".
> **ديكارت**

---

###### سند 5 — هيغل / HEGEL — « تحقّقُ الوعي » — p.24-25

- **Auteur tel qu'imprimé** : signature **هيغل** ; ligne latine **`HEGEL`** ; notice
  **فريديريك هيغل: ( 1770 – 1831 )**. Encadré-citation p.25 signé **هيغل**.
- **Titre du سند** : **تحقّقُ الوعي**
- **Source imprimée (2 lignes)** :
  **هيغل ، علم الجمال**
  `HEGEL, Esthétique, PUF, p 21`
  ⚠️ Espace avant la virgule dans la ligne arabe (`هيغل ، علم الجمال`), tel qu'imprimé.
- **Illustration** : **portrait peint** de Hegel de trois quarts, cheveux gris (médaillon dans le
  texte, p.24) ; (p.25) **photographie** d'une statue **Chac Mool** (figure allongée, tête tournée)
  au milieu d'une forêt de **colonnes de pierre** sous un ciel bleu — aucun cartel imprimé.

**التمهيد (verbatim)** :
> إنّ القول بماهيّة ثابتة للإنسان من شأنه أن يجعل ما لَحِقَ الوعي من تبدلات مستغلقا على الفهم. ولعلّ
> الانتباه إلى قيمة التاريخ وفعله ما يبدّد بعض ما التبس، خاصّة إذا اعتبرناه مقوّما للوعي لا مجرّد
> وحدة قيس.

**Thèse (reformulée)** : l'homme est un être doué de conscience et de pensée : quel que soit son
mode d'existence, **il est un être pour soi**. Les choses de la nature **n'existent que d'une seule
manière, immédiate** ; l'homme, parce qu'il est esprit, a une **existence double** — il existe
d'un côté comme les choses de la nature, et de l'autre **il existe aussi pour soi**, il se
contemple, se représente à lui-même, se pense ; et il n'est esprit que par cette activité. Cette
conscience de soi s'acquiert de **deux manières** : (1) **théoriquement**, en se repliant sur la
conscience de tous les mouvements du cœur humain, en se contemplant et en se représentant ce qui le
caractérise comme essence, puis en ne se reconnaissant que dans ce qu'il tire **de sa propre
profondeur**, non dans les données reçues du dehors ; (2) **pratiquement**, par son activité —
poussé à se découvrir dans ce qui lui est immédiatement donné et offert du dehors. Il y parvient en
**transformant les choses extérieures**, en les marquant du sceau de son intériorité et en n'y
retrouvant plus que ses propres déterminations. Ainsi l'homme dispose librement de ce qui est
extérieur **en tant que soi**, **ôte au monde son caractère d'étrangeté** et ne jouit des choses
**que parce qu'il y trouve une forme extérieure de sa propre réalité**. Ce besoin est déjà inscrit
dans les premiers penchants de l'enfant : le petit garçon qui jette des pierres dans la rivière et
s'émerveille des **cercles** qui se forment dans l'eau jouit en réalité d'un spectacle **qu'il a
obtenu de sa propre activité**.

**هوامش** : **aucun encadré de notes** pour ce سند (ni p.24 ni p.25).

**الكاتب (notice, p.24-25) — verbatim** :
> **فريديريك هيغل: ( 1770 – 1831 )** — فيلسوف ألماني من أهمّ فلاسفة القرن التاسع عشر وأكثرهم تأثيرا
> في الفكر المعاصر. اشتغل بالتدريس منذ سنة 1801 بجامعة " يانا " `Iena`. اهتمّ في " فينومينولوجيا
> الرّوح " ( 1807 ) بتاريخ الوعي بما هو تاريخ النفس وقد أصبحت وعيا، واصفا المراحل التي قطعتها
> ومحدّدا الصور المختلفة التي اتخذتها والتي تحقّقت بفضل التفكير. وفي الأجزاء الثلاثة من " علم
> المنطق " ( 1812 – 1816 ) يتخطّى هيغل المنطق الرياضي في اتجاه منطق شامل لكلّ تفكير ممكن ولكلّ صورة
> من صور الفكر، متجاوزا بذلك التعارض القديم بين صورة التفكير ومادّته. صدر له سنة 1817 كتاب " موسوعة
> العلوم الفلسفيّة "، وفيه رسم لقرّائه الخيط الناظم لدروسه الفلسفيّة. وسعى، من جهة أخرى، إلى التوحيد
> بين وجهين في السلوك الإنساني فصلت بينهما الفلسفة الكانطيّة: الحقّ الذي يُلزم الإرادة من خارج
> والواجب الذي تلتزم به الإرادة من الداخل. وقد أراد بهذا التوحيد الجمع بين الموضوعي والذاتي ضمن ما
> يسمّيه بالأخلاقيّة الموضوعيّة ( " مبادئ فلسفة الحقّ "؛ 1821 ). وفي " علم الجمال " ( 1832 ) عرّف
> الفنّ بما هو وحدة بين الواقعي والمجرّد واعتبره تجاوزا للطبيعة والمنطق في آن. واهتمّ كذلك بالدين
> وبيّن أنه تماما كالفلسفة يطمح إلى التعبير عن المطلق لكنه لا يفعل ذلك باعتماد التأمّل المفهومي شأن
> الفلسفة بل بواسطة التمثلات والمشاعر ( " دروس في فلسفة الدّين "؛ 1832 ). أمّا في " دروس في تاريخ
> الفلسفة " ( 1833 – 1836 ) فقد عرض إمكانيّة التفكير في تاريخ الفلسفة عبر إجلاء الوحدة من الكثرة
> ( كثرة الأنساق الفلسفيّة ) معتبرا الفلسفة أرقى صور الوعي الذي يتمكّن من تجاوز التحقق في الدين
> والفن. والثابت لدى هيغل أنّ تاريخ الإنسانيّة بأكمله هو تعبير عن صيرورة تحقّق الفكر ( " دروس في
> فلسفة التاريخ "؛ 1837 ).

⚠️ Intervalles `( 1770 – 1831 )`, `( 1812 – 1816 )`, `( 1833 – 1836 )` — tous dans le bon ordre.
⚠️ Le nom de l'université est imprimé **`" يانا " Iena`** — translittération arabe + forme latine.

**المهام (verbatim, p.25 — encadré rose, 7 puces)** :
- بأيّ معنى يقول الكاتب عن الوجود الإنساني إنه " وجود مزدوج " ؟
- يتحدّث الكاتب عن طريقتين يكتسب بهما الإنسان الوعي بالذات: ما دلالتهما؟
- هل من تناقض بين القول بأن الإنسان كائن وُهب وعيا وبين القول بأنه يكتسب هذا الوعي؟
- أستخلص قيمة التاريخ في تشكّل الوعي.
- أيّة علاقة يقيمها الكاتب بين الحريّة ونزع الغرابة عن العالم والتمتّع بالأشياء؟ أستثمر مثال الولد
  الصغير في بلورة جوابي.
- أيّ معنى للإنيّة يمكن استخلاصه من النصّ؟ أتبيّن وجوه الجدّة فيه.
- هل الحريّة في علاقتها بالوعي شرط أم رهان؟ أحرّر فقرة في الغرض.

**Encadré-citation (p.25, cadre rose, à droite de la photographie)** :
> " لا يتمتّع (الإنسان) بالأشياء إلاّ لأنّه يعثر فيها على شكل خارجيّ لحقيقته الخاصة ".
> **هيغل**

⚠️ Le mot **(الإنسان)** est imprimé **entre parenthèses** dans la citation : ajout du manuel pour
expliciter le sujet, non retiré ici.

---

###### سند 6 — ج. ج. روسّو / J. J. ROUSSEAU — « التوق إلى الاكتمال » — p.26-27

- **Auteur tel qu'imprimé** : signature **ج. ج. روسّو** ; ligne latine **`J. J. ROUSSEAU`** ;
  notice **ج.ج روسّو : ( 1712 – 1778 )** (sans point après le second `ج`) ; encadré-citation p.27
  signé **روسّو** ; le corps de la notice écrit **لروسّو**.
- **Titre du سند** : **التوق إلى الاكتمال**
- **Source imprimée (3 lignes)** :
  **ج. ج. روسّو؛ مقالة حول أصل اللامساواة بين البشر وأسسها.**
  `J. J. ROUSSEAU,`
  `Discours sur l'origine et les fondements de l'inégalité parmi les hommes,1755`
  ⚠️ Pas d'espace après la virgule finale (`hommes,1755`), tel qu'imprimé.
  ⚠️ Le titre arabe de la source (`مقالة حول أصل اللامساواة`) diverge de celui donné dans la notice
  de la même page (`مقالة في أصل اللامساواة بين البشر وأسسها`) : **حول** vs **في**.
- **Illustration** : **portrait peint** de Rousseau en buste, perruque blanche, veste sombre
  (médaillon dans le texte, p.26).

**التمهيد (verbatim)** :
> اقتضى تحديد الإنسانيّ في الإنسان تمييزه عن الحيوان. وكثيرا ما قام الوعي بأداء هذا الدور. لكنّنا
> إذا طلبنا مزيد الدقّة والتعمّق في تحديد الإنسانيّ تبيّنت لنا محدوديّة أدائه، ممّا يضطرّنا إلى
> التفكير في أفق يتجلّى فيه الإنسانيّ على نحو أكثر إشراقا.

**Thèse (reformulée)** : puisque toutes les difficultés qui entourent la question laissent place à
la discussion sur ce qui distingue l'homme de l'animal, Rousseau met en avant **une autre qualité,
très spécifique, qui les distingue et sur laquelle on ne peut pas discuter : la faculté de se
perfectionner** (`ملكة التوق إلى الاكتمال`). Aidée des circonstances, elle développe
successivement toutes les autres facultés, et **elle réside en nous autant dans l'espèce que dans
l'individu** — alors que l'animal, au bout de quelques mois, est ce qu'il sera toute sa vie, et son
espèce au bout de mille ans ce qu'elle était la première année de ces mille ans. Pourquoi
**l'homme seul est-il sujet à devenir imbécile ?** N'est-ce pas qu'il **retourne** ainsi à son état
primitif, tandis que la bête, qui **n'a rien acquis** et n'a donc rien à perdre, reste toujours
avec son instinct ? Rousseau y voit une conséquence **triste** : il faut reconnaître que cette
faculté distinctive et **illimitée** est **la source de presque tous les malheurs de l'homme** ;
c'est elle qui l'arrache, avec le temps, à cet état originel où il aurait coulé des jours paisibles
et innocents ; c'est elle qui, à la longue, **fait de lui le tyran de lui-même et de la nature**,
en faisant éclore avec les siècles ses lumières et ses erreurs, ses vices et ses vertus.

**الهامش (verbatim, p.27 — encadré rose « الهامش », 1 seule note)** :
> 1– " المسائل ": ويُقصد بها مجموع القضايا التي دار حولها جدل يتعلّق بما يميّز الإنسان عن الحيوان
> وما يميّز إنسانا عن آخر.

**الكاتب (notice, p.26-27) — verbatim** :
> **ج.ج روسّو : ( 1712 – 1778 )** — كاتب وفيلسوف فرنسي من أصل سويسري، عاش في عصر التنوير وكانت له
> علاقات متينة بالموسوعيين ومع ذلك ناهض تطوّر العلوم وتراكم الثروات خاصّة في كتاباته الأولى
> ( " مقالة في العلوم والفنون " ؛ 1751 - " مقالة في أصل اللامساواة بين البشر وأسسها "؛ 1755 ). أمّا
> كتاباته اللاحقة فقد جاءت **أكثرا** تفاؤلا. وفي " في العقد الاجتماعي " ( كُتب سنة 1762 أي قبل عشرين
> سنة من قيام الثورة الفرنسيّة ) يتجاوز روسّو الفلاسفة القائلين بالحق الطبيعي رافضا أن تكون الحريّة
> الثمن الذي يدفعه المواطن مقابل الأمن. فالحريّة لا يمكن أن تكون موضوع مبادلة لأنّ التفريط فيها هو
> بمثابة التفريط في إنسانيّة الإنسان. واستخلص أن الإرادة العامّة هي الأساس الشرعي لكل دولة مدنيّة.
> أما في " إميل أو في التربيّة " ( 1762 ) فقد عرض روسّو نظريّة معاصرة في التربية جاء فيها أنّ
> المجتمع يمثل عاملا مؤثرا في تكوين شخصيّة الفرد ودعا إلى تمكين الطفل من الإسهام الفعلي في بناء
> تكوّنه الشخصي. وكانت لروسّو كتابات عديدة ذات توجّه قبل رومنطيقي منها " هيلويز الجديدة " ( 1761 )
> و " الاعترافات ".

⚠️ **`أكثرا تفاؤلا`** [sic] — alif surnuméraire (forme attendue `أكثر`). Vérifié à 600 dpi.
⚠️ **`قبل عشرين سنة من قيام الثورة الفرنسيّة`** — imprimé tel quel et vérifié à 600 dpi ; l'écart
entre 1762 et 1789 est de **27** ans, non 20. Affirmation de la source, non corrigée.
⚠️ Intervalle `( 1712 – 1778 )` — ordre correct.

**المهام (verbatim, p.27 — encadré rose, 6 puces)** :
- عن أيّة ملكة إنسانيّة يتحدّث الكاتب ؟ وما قيمتها ؟
- أيّة قيمة للمقارنة التي يقيمها الكاتب بين الإنسان والحيوان ؟
- في أيّ معنى يكون " توق الإنسان إلى الاكتمال " أساسا لجدارته ؟
- هل من تناقض بين التوق إلى الاكتمال والوضع البائس الذي يمكن أن يكون عليه الإنسان ؟
- أيّة صورة **للأنيّة** يمكن تحديدها في ضوء توق الإنسان إلى الاكتمال؟
- هل أرى في محيطي ما يُعَدُّ من تجليات هذه الملكة؟ أحرر فقرة في الغرض ؟

⚠️ 5ᵉ puce : le manuel imprime **`للأنيّة`** (alif **avec hamza au-dessus**), et non `للإنيّة`
comme partout ailleurs dans le chapitre. Vérifié à 600 dpi.
⚠️ 6ᵉ puce : elle se termine par un **point d'interrogation** alors qu'elle est une consigne
(`أحرر فقرة في الغرض ؟`), tel qu'imprimé.

**Illustration (p.27)** : photographie en noir et blanc — **deux silhouettes** en contre-jour sur
une pente sombre très inclinée (l'une debout, main sur la hanche ; l'autre penchée sur un
trépied/outil), ciel de nuages clairs.

**Encadré-citation (p.27, cadre rose, à droite de la photographie)** :
> " ... إنها ملكة التوق إلى الاكتمال... وتكمن لدينا في النوع بقدر ما تكمن في الفرد ".
> **روسّو**

---

###### سند 7 — أ. شوبنهاور / Arthur SCHOPENHAUER — « التاريخ ذاكرة الوعي » — p.28-29

- **Auteur tel qu'imprimé** : signature **أ. شوبنهاور** ; ligne latine **`Arthur SCHOPENHAUER`** ;
  notice **شوبنهاور : ( 1788 – 1860 )**. Encadré-citation p.29 signé **شوبنهاور**.
- **Titre du سند** : **التاريخ ذاكرة الوعي**
- **Source imprimée (3 lignes)** :
  **أ. شوبنهاور. العالم بما هو إرادة وتمثّل**
  `Arthur SCHOPENHAUER, Le Monde comme volonté et représentation,`
  `supplément au livre III, éd. PUF, ,1978 pp. 1185 - 1186`
  ⚠️ **Deux virgules consécutives** avant le millésime (`PUF, ,1978`) — même tic typographique qu'au
  سند 4 (`Gallimard, ,pp`). Vérifié à 600 dpi.
  ⚠️ Le titre arabe de la source (`العالم بما هو إرادة وتمثّل`) diverge de celui donné dans la notice
  de la p.29 (`العالم كإرادة وتمثل`).
- **Illustration** : **portrait peint** de Schopenhauer jeune, chevelure bouclée, col haut
  (médaillon dans le texte, p.28) ; (p.29) **photomontage** — profil de visage se détachant sur un
  fond de **ciel étoilé** rose et violet, avec une **horloge** en haut à droite.

**التمهيد (verbatim)** :
> إذا كانت الحداثة، في بداية تشكّلها، قد اقتضت أن يكون الإنسان " مملكة داخل مملكة " فإنّ الوعي بقيمة
> التاريخ في تحديد ما هو إنسانيّ في الإنسان أفضى إلى الوعي بتاريخيّة الإنسان وتاريخيّة وعيه، إذ لا
> معنى لإنسان لا يتأثّر بالتاريخ ولا يؤثّر فيه، وكأنّ تاريخ الوعي يتماهى مع الوعي بالتاريخ.

**Thèse (reformulée)** : **l'histoire est à l'espèce humaine ce que la raison est à l'individu.**
Grâce à sa raison, l'homme **n'est pas** enfermé dans les limites étroites du présent visible comme
l'est l'animal : il connaît aussi le passé dans son extension la plus lointaine, comme origine du
présent auquel il se rattache ; **cette connaissance seule** lui donne l'intelligence claire du
présent et lui permet même d'anticiper l'avenir. À l'inverse, l'animal — dont la connaissance est
sans réflexion, bornée à l'intuition donc au présent — reste **ignorant, apathique, désarmé,
esclave**, même apprivoisé parmi les hommes. De même, **un peuple qui ne connaît pas son histoire**
est borné au présent de la génération actuelle : il ne comprend ni sa nature ni son existence
propre et ne peut les rapporter à un passé qui les expliquerait ; il est donc **moins capable
d'anticiper l'avenir**. **Seule l'histoire donne à un peuple une conscience pleine de lui-même** :
elle est la conscience réfléchie du genre humain. D'où le rôle de la **langue** (condition
nécessaire de la raison individuelle) et de l'**écriture** : l'existence effective de cette raison
de l'humanité **ne commence qu'avec l'écriture**, comme la raison individuelle **ne commence
qu'avec la parole**. L'écriture restaure l'unité de cette conscience de l'espèce **que la mort
brise et fragmente sans cesse** : elle permet au petit-fils de reprendre et d'achever la pensée
conçue par l'aïeul, elle pare à la dissolution du genre humain en une infinité d'individus
éphémères et, par là, **fait front au temps** dans sa fuite irrésistible, qu'accompagne son
compagnon, **l'oubli**.

**هوامش** : **aucun encadré de notes** pour ce سند (ni p.28 ni p.29). Une coupe `(...)` imprimée.

**الكاتب (notice, p.29) — verbatim** :
> **شوبنهاور : ( 1788 – 1860 )** — فيلسوف ألماني من عائلة ثرية، اهتم بالفلسفة وكان تلميذا
> **لفيخته**، كان للقائه بفلسفة كانط (1810) من ناحية، والبوذية من ناحية أخرى ( 1814 )، أثر كبير على
> تكوينه الفلسفي، كما عُرف بنقده اللاذع **لهيغل** الذي قال عنه " كاتب لأشياء سخيفة ومفسد للأدمغة ".
> لم يعرف تدريسه في برلين النجاح ( فقد اختار التدريس في نفس توقيت دروس **هيغل** ) فانقطع عنه سنة
> 1833 لكتابة " الإرادة في الطبيعة " ( 1836 ). ثم أصدر كتاب " المشكلان الأساسيان للإيتيقا " (1841)،
> وكان عليه أن ينتظر نهاية حياته ليعرف النجاح مع صدور كتابه الأخير " تكملة وحذف " ( 1851 ) والذي
> تضمن تأملاته في تاريخ الفلسفة والأخلاق. ضد الأنساق الفلسفية، أراد **شوبنهاور** أن يكون صاحب فكر
> متفرد، يعتبر أن جوهر العالم يقوم على إرادة الحياة بما هي إرادة كلية وعمياء ( " العالم كإرادة
> وتمثل "، 1818 ). من الكانطية احتفظ **شوبنهاور** بفكرة أن العالم كما يظهر لنا ليس سوى تمثلات، ولكنه
> جعل من التمثل واقعا في ذاته قابلا للمعرفة في العالم ويسميه إرادة. فالإرادة هي المعرفة الماقبلية
> للعالم، والعالم هو المعرفة المابعدية للإرادة. إن فكرة الإرادة الحرة والعمياء واللاعقلانية قادته
> إلى ضرب من اليأس. وباختزاله الفعل الأخلاقي للإنسان في مبدأي الأنانية والشفقة يكون **شوبنهاور** قد
> عرّف الإنسان لا كذات واعية بأفعالها، وإنما كمسرح لانفعالات لاواعية، وهو مبحث اهتم به الفكر الفلسفي
> المعاصر خاصّة مع نيتشه وأفضى إلى قطيعة مع الفكر الفلسفي التقليدي. أثرت كتاباته خاصة في **فاغنار**
> ونيتشه.

⚠️ Intervalle `( 1788 – 1860 )` — ordre correct. Graphie **`فاغنار`** pour Wagner, telle qu'imprimée.

**المهام (verbatim, p.29 — encadré rose, 5 puces)** :
- أحلّل وجوه التماثل التي يقيمها الكاتب بين منزلة العقل بالنسبة إلى الفرد ومنزلة التاريخ بالنسبة إلى
  النوع الإنساني وأتبيّن دلالاتها.
- في أي معنى أفهم التمييز الذي يُقيمه الكاتب بين الإنسان والحيوان؟
- " وحده التاريخ يمنح شعبا وعيا تامّا بذاته ": أتبيّن قيمة التاريخ في تحقق الإنيّة.
- أتبيّن منزلة الكلام بالنسبة إلى وحدة الوعي لدى الفرد ومنزلة الكتابة بالنسبة إلى وحدة الوعي الخاص
  بالجنس البشري.
- كيف يكون الوعي تاريخيّا من ناحيّة ويتصدّى للزمن من ناحيّة أخرى؟

⚠️ Dernière puce : `ناحيّة` est imprimé **avec shadda** (deux fois), là où le mot s'écrit
habituellement `ناحية`.

**Encadré-citation (p.29, cadre rose, à droite du photomontage)** :
> " يقوم التاريخ بالنسبة إلى النوع الإنساني مقام العقل بالنسبة إلى الفرد ".
> **شوبنهاور**

---

###### سند 8 — هنري برغسون / Henri BERGSON — « الوعي والديمومة » — p.30-31

- **Auteur tel qu'imprimé** : signature **هنري برغسون** ; ligne latine **`Henri BERGSON`** ;
  notice **برغسون: (1859 – 1941)**. Encadré-citation p.31 signé **برغسون**.
- **Titre du سند** : **الوعي والديمومة**
- **Source imprimée (2 lignes)** :
  **هنري برغسون، الطاقة الروحيّة**
  `Henri BERGSON, L'Energie spirituelle, Alcan p 5.`
  ⚠️ `L'Energie` **sans accent** sur le E, tel qu'imprimé.
- **Illustration** : **portrait photographique** de Bergson en noir et blanc (médaillon dans le
  texte, p.30) ; (p.31) **photomontage** — homme en costume, **les yeux bandés**, mains levées
  paumes en avant, entouré de **cadrans d'horloges**, d'un **avion** et d'un panneau d'aéroport
  (`TOKYO / NEW… / ATLA… / LOS… / MIAMI`).

**التمهيد (verbatim)** :
> لأنّ الحيوان لا يملك وعيا، فإنّه لا يقدر على تجاوز أفق لحظته ولا ينشد إلى ماض ولا يستشرف مستقبلا.
> ولأنّ ما يقع تحت حواسه لا يترك له أثرا لكونه ممتلئا بغريزته، فإنّه لا يملك ذاكرة، ولأنّه كذلك كان
> حيوانا. ومتى قابلناه بالإنسان أمكن لنا أن نتبيّن بوضوح دور الذاكرة في تشكّل وعي الإنسان. ولأنّه
> كذلك كان إنسانا.

**Thèse (reformulée)** : sans prétendre définir la conscience par quelque chose de moins clair
qu'elle-même, Bergson la caractérise par son trait le plus apparent : **conscience signifie d'abord
mémoire**. Cette mémoire peut être de faible ampleur — ne retenir qu'une mince part du passé, voire
seulement ce qui vient d'arriver — mais elle est présente dans tous les cas : **sans elle il n'y
aurait pas de conscience**. Une conscience qui **ne retiendrait rien** de son passé et s'oublierait
sans cesse s'évanouirait et renaîtrait à chaque instant. **Toute conscience est donc mémoire** :
conservation et accumulation du passé dans le présent. Mais **toute conscience est aussi
anticipation de l'avenir** : la pensée s'occupe de ce qui est surtout du côté de ce qui va être,
l'attention est attente, et **il n'y a pas de conscience sans une certaine attention à la vie** ;
l'avenir nous attire, et cette attraction ininterrompue qui nous fait avancer sur le chemin du
temps est aussi ce qui nous fait agir — **tout acte est ouverture sur l'avenir**. Retenir ce qui
n'est plus et anticiper ce qui n'est pas encore : **telle est la fonction première de la
conscience**. Il n'y aurait aucun présent pour la conscience si le présent se réduisait à l'instant
mathématique — pure limite théorique entre passé et avenir, qu'on peut à la rigueur concevoir mais
jamais percevoir. **Ce que nous percevons réellement est une certaine épaisseur de durée**, faite de
deux parties : notre passé immédiat et notre avenir imminent.

**الهامش (verbatim, p.31 — encadré rose « الهامش », 1 seule note)** :
> 1– " الديمومة `La durée` " انظر نافذة دعائم للتفكير؛ تحديدات وتمييزات مفهوميّة: الزّمان.

⚠️ **Renvoi interne au manuel**, transcrit tel quel et **non résolu** : il pointe vers une
**نافذة دعائم للتفكير** (rubrique « تحديدات وتمييزات مفهوميّة », entrée `الزّمان`), hors de la
tranche p.6-46.

**الكاتب (notice, p.31) — verbatim** :
> **برغسون: (1859 – 1941)** — من أبرز الفلاسفة الفرنسيين في بداية القرن العشرين، تحصّل على جائزة
> نوبل للآداب (1928) جاءت فلسفته ردّا على الثوابت ذات الأصول الكانطيّة والوضعيّة التي هيمنت على
> الميتافيزيقا في القرن التاسع عشر. ففي أطروحته " مقالة في المعطيات المباشرة للوعي " (1889) يؤكّد
> برغسون أنّ العلم لا يمكنه تفسير الوعي والحياة الباطنيّة لأنّها من طبيعة غير ماديّة، فالعالم
> الباطني للوعي يتميّز بالديمومة والصيرورة والحريّة، أي بطابع كيفي، في حين أنّ عالم المادة الخارجي
> يتميّز بالعطالة والمكان وبصفات كميّة وبالخضوع للقوانين. لم يتخلّ **برغسون** عن هذه الأفكار بل عمل
> على تطويرها في " المادة والذاكرة " (1896) حيث بيّن أنّ العقل لا يُختزَل في مجرّد نشاط للدماغ الذي
> ليس إلا حيزا للذكاء العملي أو هو " عضو الانتباه إلى الحياة " العمليّة، في حين أن الأنشطة النفسيّة
> العليا مثل الذاكرة، تؤكّد اختراق العقل للمادّة. لذلك يؤكّد **برغسون** في " التطوّر الخلاق " ( 1907 )
> أنّ الحياة قوّة روحيّة، وثبة حيويّة حرّة ومبدعة تنفذ إلى المادة والروح على حدّ السواء. وتبعا لذلك
> ينقد العقل والذكاء المفهومي، إذ لا يرى في الذكاء سوى أداة عمليّة تمكّن من تمثل الواقع تمثّلا آليّا
> وكميّا ( العلم ) والسيطرة عليه ( التقنية )، في مقابل الحدس بما هو امتداد للوثبة الحيويّة والذي
> يمكّن من النفاذ إلى الحقيقة على نحو مباشر. وانتهى في " الديمومة والتزامن " ( 1922 ) إلى التمييز
> بين الزمن الرياضي والزمن النفسي. كما كانت **لبرغسون** اهتمامات أخلاقيّة ضمّنها كتابه " منبعا
> الأخلاق والدّين " ( 1932 ) الذي ميّز فيه بين الأخلاق المغلقة (أخلاق الإلزام) والأخلاق المفتوحة
> ( أخلاق نداء الإنسانيّة ).

⚠️ Intervalle `(1859 – 1941)` — ordre correct.

**المهام (verbatim, p.31 — encadré rose, 5 puces)** :
- أيّة صلة يقيمها الكاتب بين الوعي وتجربة الحياة؟
- ما هي وظيفة الوعي؟ هل في الوعي ما يؤسس لهذه الوظيفة؟
- " ما ندركه فعلا هو نوع من كثافة الديمومة ": كيف أفهم هذا القول؟ وأية علاقة ممكنة بين تحقّق الإنيّة
  والزمن؟
- أمتحن تصوّر برغسون بالتساؤل عما إذا كنت قادرا على استحضار كلّ ما خزّنته ذاكرتي؟
- إذا كان " كلّ وعي ذاكرة " فكيف أفهم حينئذ النسيان؟

**Encadré-citation (p.31, cadre rose, sous le photomontage)** :
> " الاحتفاظ بما لم يعد موجودا واستباق ما لم يوجد بعدُ، تلك هي إذن وظيفة الوعي الأولى "
> **برغسون**

⚠️ **Discordance interne au texte imprimé, p.30 (dernière phrase)** : le manuel écrit
`إنّ الوعي همزة وصل بين ما كان وما سيكون، وجسر يصل الماضي بالحاضر.` — la première moitié dit
« entre ce qui a été et ce qui sera », la seconde « un pont qui relie le passé **au présent** ».
Les deux moitiés ne disent pas la même chose. Vérifié mot à mot à 600 dpi ; **non corrigé**.

---

###### سند 9 — أفلاطون / PLATON — « الجسد الوضيع » — p.32-33

- **Auteur tel qu'imprimé** : signature **أفلاطون** ; ligne latine **`PLATON`** ; notice
  **أفلاطون: ( 427 – 348 ق. م )**. Encadré-citation p.33 signé **أفلاطون**.
- **Titre du سند** : **الجسد الوضيع**
- **Source imprimée (2 lignes)** :
  **أفلاطون، محاورة الفيدون.**
  `PLATON; Le Phédon, 66 b - 66 e. éd, Les Belles Lettres, 1963`
  ⚠️ **Point-virgule** après `PLATON` (les autres سندات portent une virgule) et ponctuation
  irrégulière autour de `66 e. éd,`. Vérifié à 600 dpi.
- **Illustrations** : (p.32) **photographie d'un buste de marbre** de Platon, barbu, dans le texte ;
  (p.33) **miniature enluminée médiévale** — un homme allongé, la tête soutenue par un personnage,
  sous un arbre à **fleurs rouges** où se tient un **oiseau**, fond rouge et cadre grenat ; à sa
  gauche, **petite vignette bleue** représentant des **mains** jointes/serrées.

**التمهيد (verbatim)** :
> إذا صحّ أنّ الإنسان كائن وعي وتفكير ألا تهتزّ عندنا هذه القناعة ونحن نشاهد وقائع الجهل والرّذيلة
> تنتشر من حولنا؟ قد نحتاج في حلّ هذه المفارقة إلى اتهام كيان نجعله غريبا عنا وطارئا علينا.

**Thèse (reformulée)** : tant que nous avons un corps et que notre âme y est mêlée, **nous
n'obtiendrons jamais assez ce que nous désirons — la vérité**. Le corps apporte mille peines : non
seulement les nécessités de la vie, mais les maladies, obstacles nouveaux qui barrent notre marche
vers la vérité. Il nous emplit d'amours, de désirs, de craintes et de chimères innombrables, si
bien que **nous ne pouvons pas avoir une seule pensée saine**. Guerres, séditions et batailles
**n'ont pas d'autre cause que le corps et ses exigences** : c'est pour acquérir des biens qu'on se
bat, et si l'on veut des biens c'est à cause du corps dont nous sommes les esclaves — et voilà
pourquoi nous n'avons pas le loisir de philosopher. Pire encore : quand nous parvenons enfin à un
peu de repos et que nous nous tournons vers un objet de pensée, **le corps s'immisce de nouveau
dans nos recherches** et y sème un trouble qui nous rend **incapables de discerner la vérité**. À
l'inverse, il est prouvé que **si nous voulons connaître purement quelque chose, il nous faut nous
en séparer** et regarder les choses en elles-mêmes avec l'âme seule ; alors nous obtiendrons ce que
nous prétendons aimer — la pensée — **une fois morts, et non durant notre vie**. Ceux qui
s'adonnent vraiment à la philosophie **s'exercent à mourir**, et l'idée de la mort leur est **moins
effrayante** qu'aux autres.

**هوامش** : **aucun encadré de notes** pour ce سند (ni p.32 ni p.33).

**الكاتب (notice, p.33) — verbatim** :
> **أفلاطون: ( 427 – 348 ق. م )** — كنية لفيلسوف يوناني هو **أرسطوكلاس**. ولد في أسرة أرستقراطيّة
> وتتلمذ في البداية على السفسطائيين و**كراتيل** قبل أن يتعرّف على سقراط وعمره عشرون سنة ويتعلّق به
> حتى إعدامه. كان لإعدام سقراط التأثير البالغ على شخصيّة أفلاطون ورأى فيه شاهدا على فساد الدولة
> فاهتمّ بالشأن السياسي وكتب فيه أهمّ محاوراته: " الجمهوريّة " ( 385 – 370 ق م ) بحث فيها عن ماهيّة
> العدالة وعن أسس جمهوريّة فاضلة أو " دولة عادلة "، كما عرض فيها نظريّته في المعرفة من خلال
> " أمثولة الكهف " الشهيرة ( الكتاب السابع من الجمهوريّة ). وعمّق نظرياته السياسية في محاورات أخرى
> ( " القوانين " و " السياسي " ). ونعثر في " الثياتيتوس " و " المينون " و " المأدبة " و " فيدروس "
> على جوانب من نظريّة أفلاطون في المعرفة التي تقوم على مبدأ " التذكّر " الذي يقتضي " التوليد " ضمن
> جدل صاعد تسلك فيه النفس طريق العلم بدءا بالظنّ مرورا بالرياضيات وصولا إلى أعلى درجات المعرفة وهي
> المعرفة الحدسيّة للمعقولات. كتب أفلاطون ثمان وعشرين كتابا على مدى أربعين سنة في شكل محاورات جعل
> فيها سقراط محاورا دائما وتختصّ كلّ محاورة بموضوع يُصاغ في مستهلّ كل محاورة في شكل سؤال: ما
> العدالة ؟ ( الجمهوريّة )، ما العلم؟ ( ثياتيتوس ). بعد تجربة فاشلة إلى جانب طاغيّة **سراقسطة** من
> أجل بناء دولة عادلة تجسّم نظريّته في " حكم الفيلسوف "، استقرّ أفلاطون في أثينا لينشأ
> " أكاديميّة " للعلوم يدرّس فيها فلسفته دون أن يكفّ عن محاولاته في تحقيق حلمه السياسي قرب
> " دونيس الشاب ".

⚠️ **`سراقسطة`** — graphie imprimée, vérifiée à 600 dpi lettre à lettre (س ر ا ق س ط ة). Le
contexte (le tyran, « دونيس الشاب » = Denys le Jeune) désigne **Syracuse**, dont la forme arabe
usuelle est `سرقوسة` ; `سرقسطة` est habituellement **Saragosse**. Graphie **reproduite telle
quelle**, non corrigée.
⚠️ Intervalles `( 427 – 348 ق. م )` et `( 385 – 370 ق م )` — ordres corrects (décroissants, av. J.-C.).
Noter la **variante interne** : `ق. م` avec point la 1ʳᵉ fois, `ق م` sans point la 2ᵉ.
⚠️ `لينشأ` [sic] pour `لينشئ`, tel qu'imprimé.

**المهام (verbatim, p.33 — encadré rose, 5 puces)** :
- بأيّ معنى أفهم " تورّط النفس بالجسد " ؟
- كيف يكون الجسد عقبة أمام سعينا إلى الحقيقة والفضيلة ؟
- أستخلص منزلة الجسد من خلال موقف الكاتب، مبيّنا علاقته بإثبات الإنيّة.
- كيف أفهم دعوة الكاتب إلى " الموت " ؟
- هل أجد في موقف الكاتب وجاهة أستأنس بها في تعقّل جسدي ؟

**Encadré-citation (p.33, cadre rose)** :
> " انظر إلى الحروب والفتن والمعارك، ليس لها من باعث غير الجسد ومطالبه ".
> **أفلاطون**

---

###### سند 10 — مالبرانش / Nicolas De MALEBRANCHE — « الجسم امتداد » — p.34-35

- **Auteur tel qu'imprimé** : signature **مالبرانش** ; ligne latine **`Nicolas De MALEBRANCHE`** ;
  notice **مالبرانش: (1638 – 1715)**. Encadré-citation p.35 signé **مالبرانش**.
  ⚠️ La graphie imprimée est **`مالبرانش`** (avec **ا**), vérifiée à 600 dpi — **et non** `مالبرونش`
  comme l'annonce le **فهرس**. La page fait foi. Le même nom réapparaît sous la forme `لمالبرانش`
  dans la notice de Spinoza (p.37).
- **Titre du سند** : **الجسم امتداد**
- **Source imprimée (3 lignes)** :
  **مالبرانش، في البحث عن الحقيقة**
  `Nicolas De MALEBRANCHE ,`
  `De la recherche de la vérité; Gallimard, Bibliothèque de la Pléïade;  1979; pp 90 - 91`
  ⚠️ **Espace avant la virgule** (`MALEBRANCHE ,`), **`Pléïade`** avec **tréma sur le i** [sic]
  (forme attendue *Pléiade*), et **double espace** avant `1979`. Vérifiés à 600 dpi.
- **Illustration** : (p.34) **portrait peint** de Malebranche, tons orangés, coiffe sombre
  (médaillon dans le texte) ; (p.35) **photomontage** — buste/bras humain **ouvert sur des circuits
  électroniques et des câbles** colorés, traversé de traits lumineux jaunes.

**التمهيد (verbatim)** :
> إنّ الانفعالات التي نعيشها تربك تفكيرنا حين نصرّ على تغييب الجسم وخسّه، حتى التبس علينا نصيب كلّ
> من النفس والجسم فيما نحسّ. حاجتنا إلى رفع هذا الالتباس قد لا تتحقّق إلاّ بمعاودة التفكير بالجسم من
> جهة العلاقة التي تصله بالنّفس .

**Thèse (reformulée)** : supposons d'abord que nous distinguions bien l'âme du corps par les
attributs positifs qui conviennent à ces deux substances. **Le corps n'est qu'étendue en longueur,
largeur et profondeur**, et toutes ses propriétés se réduisent au repos, au mouvement et à une
infinité de figures. Deux choses sont alors évidentes : d'abord l'idée d'étendue représente **une
substance**, puisque nous pouvons penser l'étendue **sans penser à rien d'autre** ; ensuite cette
idée **ne peut représenter que** des rapports de distance ou des rapports successifs ou continus —
c'est-à-dire des mouvements et des figures — car dans l'étendue nous **ne voyons que ce qu'elle
contient**. Divisons donc l'étendue en parties, au repos ou en mouvement les unes par rapport aux
autres : nous percevons clairement les relations entre ces parties, mais **nous ne pourrons jamais
concevoir** que ces relations soient joie, douleur, chaleur, saveur, couleur ou quelque autre
qualité sensible — bien que nous éprouvions ces qualités quand notre corps subit des changements.
Exemple imprimé : je sens de la douleur quand une épine me pique le doigt ; mais **le trou qu'elle
y fait n'est pas la douleur** — le trou est dans le doigt et se perçoit clairement, tandis que la
douleur est **dans l'âme**, car c'est elle qui la ressent profondément et que la douleur altère de
façon très pénible. Il ne faut donc attribuer au corps **que** les propriétés dites plus haut ;
inversement, **l'âme est ce « moi » qui pense, sent et veut** : la substance qui contient tous les
changements dont j'ai un sentiment intérieur et qui **ne peuvent durer que dans l'âme qui les
ressent**. Ainsi **il ne faut attribuer à l'âme aucune propriété distincte de ses diverses pensées**.

**هوامش** : **aucun encadré de notes** pour ce سند (ni p.34 ni p.35).

**الكاتب (notice, p.35) — verbatim** :
> **مالبرانش: (1638 – 1715)** — فيلسوف فرنسي، تابع دراسة الفلسفة (1654 – 1656) ثم دراسة علم اللاهوت
> ( 1656 – 1659)، ليصبح رجل دين ( 1660 ) وأنهى بقيّة حياته في كنيسة. مثّلت قراءته لمؤلفات ديكارت
> منطلق كتاباته الفلسفية والعلمية التي تُوّجت بنشر كتابه " في البحث عن الحقيقة " ( 1674 ) وركّز فيه
> على طبيعة الأفكار من ناحية و على كيفية استخدام الإنسان لعقله لتجنب الخطأ. والخطأ في تصوره هو أن
> نحكم بأن حقيقة الأشياء تكمن فيما تدركه الحواس وفيما تتمثّله المخيلة، قائلا إن مهمّة الحواس ليست
> الإدراك. كما نشر كتاب " بحث في الأخلاق " (1683) وهو مرجع لقيادة السّلوك حيث حدد واجبات الإنسان بما
> هو فرد وعضو في عائلة وفي مجتمع وفي دولة. أصدر أيضا كتابا بعنوان " محاورات حول الميتافيزيقا
> والدّين " (1688) وتضمّن نفس الأفكار التي وردت في مؤلَّفه " البحث عن الحقيقة " ( حقيقة الأفكار
> وموضوعات العقل المباشرة ومسألة وحدة النفس والجسم وقوانينها ) غير أنه تميّز بطريقة عرضه (الحوار)
> ومثّل **تيودور** مالبرانش ليقدّم العون لمحاوريه حتّى يكتشفوا الحقيقة. عمل مالبرانش في كتاباته على
> التوفيق بين فيزياء معلمه **ديكارت** وميتافيزيقا **القديس أوغسطين** حتّى قيل عنه إنّه تبنى
> الديكارتية ثم كيّفها لتكون متوافقة مع الدين.

⚠️ Intervalles `(1638 – 1715)`, `(1654 – 1656)`, `( 1656 – 1659)` — ordres corrects. Noter
l'espacement irrégulier des parenthèses, tel qu'imprimé.

**المهام (verbatim, p.35 — encadré rose, 6 puces)** :
- أيّ دلالة للتمييز بين النفس والجسم في ضوء حديث الكاتب عن " جوهرين "؟
- ما المقصود " بالامتداد "؟
- الانفعالات: هل تردّ إلى الجسم أم إلى النفس؟ أعلّل إجابتي.
- هل يمكن أن نميّز بوضوح بين الإحساس والتفكير؟
- أيّة رؤية للإنيّة يستبطنها تعريف الجسم بما هو امتداد؟
- أقارن بين تحديد الإنسان في منظور الكاتب وبين ما اكتسبته من تحديدات أخرى.

**Encadré-citation (p.35, cadre rose, à droite du photomontage)** :
> " ليس الجسم سوى امتداد بالطول والعرض والعمق ".
> **مالبرانش**

---

###### سند 11 — سبينوزا / SPINOZA — « في وحدة النفس والجسد » — p.36-37

- **Auteur tel qu'imprimé** : signature **سبينوزا** ; ligne latine **`SPINOZA`** ; notice
  **سبينوزا: ( 1632 – 1677 )**. Encadré-citation p.37 signé **سبينوزا**.
- **Titre du سند** : **في وحدة النفس والجسد**
- **Source imprimée (3 lignes)** :
  **سبينوزا ؛ علم الأخلاق، الجزء الثاني، حاشيّة القضيّة 13. ص 103 – 104**
  **ترجمة جلال الدين سعيد.**
  `SPINOZA,Traité de la nature humaine, 1737; L1 ,ed. Aubier- Montaigne t1; 1973; pp 342 -343`

⚠️⚠️ **ANOMALIE MAJEURE, vérifiée à 600 dpi** : la **ligne latine attribuée à Spinoza est en réalité
la référence de HUME** — *Traité de la nature humaine*, 1737, L.1, éd. Aubier-Montaigne t.1, 1973,
pp. 342-343 — **la même référence, au caractère près, que celle imprimée sous le سند 17 (د. هيوم,
p.48)**. La ligne arabe, elle, est bien celle de Spinoza (*علم الأخلاق*, partie II, scolie de la
proposition 13, p.103-104, trad. جلال الدين سعيد). Les deux lignes de la même source **ne renvoient
pas au même livre ni au même auteur**. Constat, non corrigé.

- **Illustration** : (p.36) **portrait dessiné** de Spinoza, longs cheveux noirs et col blanc
  (médaillon dans le texte) ; (p.37) **peinture** — homme torse nu **assis en tailleur** sur une
  étoffe rouge, deux **faisceaux de lumière blanche** croisant sa poitrine, fond bleu nuit.

**التمهيد (verbatim)** :
> يبدو أنّ تفكيرنا في الإنسان قد انبنى على جهل بالجسد ومستطاعه، جهل ولّد أوهاما رسمت صورة تجد
> أساسها النظري في تصوّر ثنائيّ للإنسان. وقد لا تتبدّد هذه الأوهام إلاّ بإعادة التفكير في الجسد
> والنفس معا.

**Thèse (reformulée)** : l'homme est composé d'une âme et d'un corps, et **le corps humain existe
tel que nous le sentons**. De là nous comprenons non seulement que l'âme humaine **est unie au
corps**, mais aussi ce qu'il faut entendre par cette union — étant entendu que **nul ne peut en
avoir une idée adéquate et distincte s'il ne connaît d'abord la nature de notre corps**. L'idée de
toute chose en Dieu, cause de cette chose, se fonde en effet de la même manière que l'idée de
l'existence du corps humain. Mais **on ne peut nier** que les idées diffèrent entre elles comme
diffèrent leurs objets, et que certaines sont plus excellentes et supérieures aux autres **dans la
mesure où leur objet est plus excellent et plus réel**. Déterminer ce qui distingue l'âme humaine
des autres âmes et ce qui la rend supérieure exige donc de connaître la nature de son objet,
c'est-à-dire **la nature du corps humain**. Règle générale imprimée : **plus un corps est capable,
comparé aux autres, d'agir et de pâtir de nombreuses manières à la fois, plus son âme est capable
de connaissance distincte** ; et plus les actes d'un corps dépendent de lui seul, moins d'autres
corps l'aidant à agir, plus son âme est capable de connaissance distincte. De là nous pouvons
connaître la supériorité d'une âme sur les autres — et comprendre pourquoi **nous ne connaissons
notre propre corps que d'une manière très confuse**.

**الهامش (verbatim, p.37 — encadré rose « الهامش », 1 seule note)** :
> 1– **الله**: الله والطبيعة في فلسفة سبينوزا شيء واحد، فالله هو الطبيعة منظور إليه من جهة الامتداد
> والطبيعة هيّ الله منظور إليها من جهة الفكر. وهو جوهر لامتناه يتأسس على فكرة وحدة الوجود التي يقول
> بها سبينوزا.

**الكاتب (notice, p.36-37) — verbatim** :
> **سبينوزا: ( 1632 – 1677 )** — " بنيدكت " أو " باروخ " سبينوزا فيلسوف هولاندى أبواه من أصل اسباني
> وُلد بأمستردام، وتربّى ليتحدث الإسبانية، والبرتغالية، والعبرية. صار فيلسوفا فذا وذلك بشهادة
> **هيغل** الذي قال فيه " لا وجود للفلسفة دون سبينوزا ". بعد نقده للاهوت تحوّل عنه لدراسة العلوم
> الإنسانية. تلقى عن طبيب مبدأ وحدة الوجود. طُرد من مقر إقامته بأمستردام من قبل الطائفة اليهودية على
> خلفية رفضه التخلي عن مبدأ وحدة الوجود وأقام مع أحد أصدقائه في ضواحي المدينة أين غيّر اسمه العبري
> " باروخ " إلى ما يقابله باللاتينية " بنيدكت " هناك بدأ يكتب ويناقش وشيئا فشيئا ذاع صيته، فعرض
> عليه الإقامة بفرنسا، ثم منصب أستاذ الفلسفة بجامعة " **هيدلبورغ** " لكنه كان يؤثر العيش في هدوء
> ويخشى على حريته وتفكيره أن يتأثرا بالسلطان والمنصب. كان ميالا للحياة البسيطة بطبعه وبتأثير فلسفته،
> حتى لقبوه بالقديس المدني. من أهم مؤلفاته " المبادئ الفلسفية لديكارت " (1660)، فكان سببا في مزيد
> انتشار صيته، أراد كذلك أن يكتب شيئا يقدم به منهجه من طراز " المنطق الجديد " **لبيكون**، و " مقال في
> المنهج " **لديكارت**، و " البحث عن الحقيقة " **لمالبرانش**، فكتب " رسالة في إصلاح الذهن " لكنه لم
> يكملها فنشرت ناقصة بعد وفاته. أما " رسالة في اللاهوت والسياسة " فقد أعلن فيه رأيه في الدين
> والاجتماع ونشره سنة (1670) رغم نصح أصدقائه بعدم نشره. أما جماع كتبه فقد كان " الأخلاق "
> (1675 – 1677) كان يطلع أصدقاؤه على ما ينجزه من فصول. سار فيه على منوال هندسي يليق بمذهب وحدة
> الوجود، وينزل فيه من الواحد إلى الكثرة، ومن الكل إلى الأجزاء. وإذا كان الجزء الذي يتناول الأخلاق
> لا يفوق خمس الكتاب إلا انه أطلق عليه اسم " الأخلاق " ليدل على اتجاهه الأخلاقي ويرمز بالاسم إلى
> العمل كغاية لكل نظر. واختياره المنهج الاستدلالي الهندسي ليس تقليدا للفلاسفة الذين كتبوا في المنهج
> بل لأنه يؤمن بأن صدق القضية لا يظهر إلا إذا عرضت بوصفها جزءا من نظام استدلالي عام.

⚠️ Intervalles `( 1632 – 1677 )` et `(1675 – 1677)` — ordres corrects.
⚠️ `هولاندى` (avec **ى** final), `اسباني` (sans hamza), `إلا انه` (sans hamza) — tels qu'imprimés.
⚠️ La notice **mentionne le سند 10** de la même نافذة (`" البحث عن الحقيقة " لمالبرانش`) : lien
interne au chapitre, imprimé.

**المهام (verbatim, p.37 — encadré rose, 4 puces)** :
- أيّ معنى للقول باتّحاد النّفس والجسم ؟
- لماذا تمثّل معرفة طبيعة الجسم شرط إدراك واضح لهذا الاتحاد ؟
- أستخلص دلالة الجسم عند سبينوزا.
- هل تمكّنني رؤية الكاتب من وعي أعمق لتصوّري لإنيّتي ؟

⚠️ **4 puces seulement** — c'est le سند le moins doté en مهامّ de la tranche p.6-46.

**Encadré-citation (p.37, cadre rose, à droite de la peinture)** :
> " لا يعرف أحد تركيبة الجسم بقدر كبير من الدقّة بحيث يمكن له أن يُفسّر كلّ وظائفه ".
> **سبينوزا**

---

###### سند 12 — هيغل — « الجسد تجسيد للحرية » — p.38-39

- **Auteur tel qu'imprimé** : signature **هيغل** ; **aucune ligne latine** pour ce سند (à la
  différence du سند 5, qui portait `HEGEL`). Notice **الكاتب** : **RENVOI** (voir ci-dessous).
  Deux encadrés-citations, p.38 et p.39, tous deux signés **هيغل**.
- **Titre du سند** : **الجسد تجسيد للحرية**
- **Source imprimée (2 lignes, arabe seulement)** :
  **هيغل، أصول فلسفة الحق، ص 158 – 159**
  **ترجمة إمام عبد الفتاح إمام، المجلّد 1. دار التنوير، لبنان، ط 2. 1983**
- **Illustrations** : (p.38) **portrait gravé/peint** de Hegel de trois quarts, dans le texte ;
  **peinture** — une jambe chaussée traînant une **chaîne et un boulet**, sur un **damier**, fond
  orange incandescent ; (p.39) **photographie noir et blanc** — **deux mains levées, poignets
  menottés**.

**التمهيد (verbatim)** :
> قد يكون من الممكن الزعم بأنّ الوعي حينما يباشر نفسه لا يحتاج إلى الجسد وسيطا ولكن حينما يتعلّق
> الأمر بعلاقة الذات بالآخرين قد يبدو من العسير تمثّل الوعي أساسا لهذه العلاقة دون توسّط الجسم.

**Thèse (reformulée)** : **dans la mesure où le corps est immédiatement existant, il n'est pas
conforme à l'esprit** ; pour devenir l'organe naturel et le moyen vivant de l'esprit, **il faut
d'abord que l'esprit en prenne possession**. Mais **aux yeux d'autrui**, quant à l'essence, je suis
**un être libre dans mon corps**, tant que ma possession de ce corps est immédiate. Parce que je
suis, en tant que vivant, un être qui vit **à l'intérieur de son corps**, cette existence vivante
**ne doit pas être maltraitée ni traitée comme une bête de somme**. Et tant que je suis vivant, mon
âme (concept de l'âme, ou terme plus élevé : **l'être libre**) **et mon corps ne sont pas
séparés** — car mon corps est **l'incarnation de ma liberté** et c'est par lui que je sens et que
j'éprouve. Il n'y a donc **qu'un raisonnement vicieux** à séparer l'âme du corps au point de dire
que « la chose en soi », l'âme, **ne serait ni touchée ni atteinte** quand le corps est maltraité,
tandis que l'existence incarnée serait soumise au pouvoir d'un autre. Certes, **je peux me replier
au-dedans de moi**, faire de mon corps quelque chose d'extérieur et regarder les sentiments
particuliers comme hors de moi : **je peux même être libre tout en étant enchaîné**. Mais cela,
**c'est ma volonté propre** ; pour autrui, j'existe **dans mon corps**, et ma liberté, du point de
vue des autres, **se confond avec mon existence déterminée**. Conclusion imprimée : **le mal
infligé à mon corps est un mal qui m'est infligé à moi aussi**.

**الهامش (verbatim, p.39 — encadré rose « الهامش », 1 seule note)** :
> 1– **شخص آخر**: يشير هيغل إلى بحث **مارتان لوثر** عنوانه " في الحريّة المسيحيّة " والذي ذهب فيه
> إلى القول بأنّ " الروح لا تتأثّر ولا تُمسّ عندما تساء معاملة البدن، أو عندما يخضع شخص لقوّة شخص
> آخر " .
> ( عن المترجم )

⚠️ Cette note est la seule de la tranche à porter la mention de provenance **( عن المترجم )**.

**الكاتب (p.39) — RENVOI, transcrit tel quel et NON résolu** :
> **هيغل: أنظر التعريف به المصاحب للسند عدد 5**

⚠️ **Premier et seul RENVOI de la tranche p.6-46** (les 11 autres سندات portent une notice
complète). Graphie imprimée `أنظر` (avec hamza sur alif), et non `انظر`.

**المهام (verbatim, p.39 — encadré rose, 7 puces)** :
- أيّة علاقة يراها الكاتب بين الرّوح والجسم؟
- بأيّ معنى أفهم قول الكاتب أنا " كائن يحيا داخل جسدي "؟
- لماذا اعتبر الكاتب الاستدلال الذي " يفرّق بين النفس والجسم " استدلالا فاسدا؟
- على أيّ وجه يكون الجسد تعيّنا للوجود الحر؟
- هل تتحدّد إنّيتي من خلال الصورة الّتي أحملها عن ذاتي أم من خلال الصورة الّتي يرسمها الآخر عنّي؟
- أتبيّن منزلة الآخر في تحديد الإنيّة.
- أستحضر موقف أبيكتات من الطاغيّة ( الوضعيّة الاستكشافيّة الثانيّة ) وأقارنه بموقف هيغل. أحرر فقرة
  في الغرض.

⚠️ La dernière puce **renvoie explicitement à la وضعيّة استكشاف ثانية (p.10-11)** — lien interne
imprimé entre les deux نوافذ.
⚠️ `الثانيّة` avec shadda, tel qu'imprimé (cf. `ناحيّة` p.29).

**Encadré-citation n°1 (p.38, cadre rose, à droite de la peinture)** :
> " يمكن أن أكون حرّا حتّى وإن كنت مقيّدا بالأغلال ".
> **هيغل**

**Encadré-citation n°2 (p.39, cadre rose, à droite de la photographie)** :
> " فالأذى الذي يُوجّه إلى جسدي هو أذى موجّه إليّ أيضا ".
> **هيغل**

⚠️ **Ce سند porte DEUX encadrés-citations** (un par page). Il n'est pas le seul : le **سند 16**
en porte deux aussi (p.46 et p.47) — constat établi après coup, en confrontant les deux fragments.

---

###### سند 13 — ادڤار موران / Edgar MORIN — « مركزيّة الذات » — p.40-41

- **Auteur tel qu'imprimé** : ligne de source arabe **ادڤار موران** (avec **ڤ**, fā' à **trois
  points**, vérifié à 600 dpi) ; ligne latine **`Edgar MORIN`** ; notice **موران: (1921)** ;
  **موران** dans le corps de la notice (p.40 et p.41) ; **موران** au هامش 2 ; encadré-citation
  p.41 signé **موران**. Notice **complète** (aucun renvoi).
- **Titre du سند** : **مركزيّة الذات**
- **Source imprimée (2 lignes, arabe puis latine)** :
  **ادڤار موران، مقدمة للتفكير المركّب**
  **Edgar MORIN;** *Introduction à la pensée complexe,* éd Seuil, 2005, pp 88 - 89
- **Illustrations** : (p.40) **photographie noir et blanc** insérée dans le corps du texte, en
  haut à gauche — un homme âgé **assis**, chemise claire, **mains croisées** posées sur la
  jambe ; (p.41) **image en couleurs** (pastel/photo) en bas à gauche — des **figurines humaines
  orange et rouges** dressées sur de petits socles ronds sur un fond **jaune vif**, chacune
  projetant une **longue ombre** ; une figurine **grise** se détache seule en bas à droite.

**التمهيد (verbatim)** :
> مثّلت " مركزيّة الذات " سمة الحداثة لما تضمنته من تأكيد لمنزلة جديدة للإنسان تلائم وضعه الجديد في
> العالم. ومع هذا لا تحمل هذه العبارة دلالة واحدة خاصّة حين أصبح الآخر شريكنا الدائم في الوجود.

**Thèse (reformulée)** : être un sujet **ne signifie ni être conscient ni avoir affects et
sentiments** — et cela **bien que** la subjectivité humaine se développe, de toute évidence, par
eux. C'est **occuper le centre de son monde propre et remplir la place du « moi »** : tout le monde
peut dire « أنا », mais **nul ne peut le dire à la place d'un autre**, pas même de son jumeau
monozygote qui lui ressemble en tout. Cette مركزيّة des sujets est **paradoxale** — le sujet y est
**autonome et dépendant en même temps**, « presque tout » pour lui-même et **« presque rien » au
regard de l'univers** —, et elle est assez large pour loger dans ce centre **parents, enfants et
concitoyens**, jusqu'au sacrifice de sa propre vie ; d'où l'exigence, imprimée en conclusion, d'une
**conception complexe du sujet**.

⚠️ Les deux **appels de note** sont placés dans le corps : **(1)** après `وجنيسه`, **(2)** après
`مركزيّة الذات`.

**الهامشان (verbatim, p.41 — encadré rose ; le titre est au DUEL, `الهامشان`, pour 2 notes)** :
> 1– **جنيسه**: المقصود به توأما حقيقيا ناتجا عن انقسام بويضة واحدة.
> 2– لا تُفهم عبارة " **مركزيّة الذات**" على المعنى الديكارتي للدلالة على وحدة الذات، وإنّما تُفهم في
> إطار تصور موران " للمركّب " .

⚠️ Le هامش 2 est une **mise en garde conceptuelle** : il **récuse** la lecture cartésienne de
l'expression et la rapporte au « **المركّب** » de Morin.

**الكاتب (p.40-41) — notice COMPLÈTE, verbatim** :
> **موران: (1921)**
> فيلسوف فرنسي معاصر عُرف بنشاطه السياسي: مناصرة السلام ومناهضة إعادة تسليح ألمانيا ثم اشتراكه
> فيما بعد في جمعية مناهضي حرب الجزائر. وبمساعدة **جورج فريدمان** انظم إلى " **المركز الوطني
> للبحوث الاجتماعيّة** " ( 1951 )، حيث تمكن من تطوير أبحاثه وإثرائها. كان شغوفا بالصّحافة فأسس
> مجلّة "**الحجج**" ( 1956 ) ثمّ " **مركز بحوث الاتصالات الجماهيريّة** " مع **رولان بارت**. كما
> دفعه شغفه بالسينما ( التي تمثّل عنده البعد اللاعقلاني في المجتمع التقني ) إلى الاهتمام بدراسة
> أساطير الزمن الراهن التي وجد فيها ما يسميه بإيديولوجــيا العصــر ( " النجوم "، 1957).
> وكعالم اجتماع خيّر **موران** متابعة الأحداث والتي رأى في تناولها ما يؤسس لعلم اجتماع الحاضر،
> فركّز اهتمامه على " أزمة الحضارة " الناشئة عن التصنيع الأعمى الذي أدّى إلى انقلاب القيم وضياع
> الإنسان. من ذلك أنه قام بتحليل أحداث ماي 1968 ونشر دراساته في جريدة " **كاليفورنيا** " (1970).
> لكنّ طرافة أعماله ستتأكّد بالخصوص في سعيه إلى تأسيس أنثروبولوجيا تجد جذورها في البيولوجي وظّف
> فيها معطيات علميّة مختلفة من البيولوجيا وعلم الإحاثة وعلم الاجتماع الحيواني والعلوم الإنسانيّة
> قصد بناء خطاب حول الإنسان يراعي تعقّده ( " وحدة الإنسان "، 1974 ). إنّ هذه الأبحاث ستعيّن
> إضافته الابستيمولوجيّة الأساسيّة وتتمثل في مفهوم " نموذج المركّب " الذي أورده في " العلم والضمير "
> (1982) حيث بيّن أنّ العلوم، على اختلاف مواضيعها، تواجه اليوم " المركّب " ممّا يضطرّها إلى وصل
> الموضوع بمحيطه وربطه بمن يلاحظه وتناوله باعتباره نظاما ومعالجة التناقضات التي تسكنه. هذه القضايا
> سيعيد تناولها بأكثر عمق في كتابه " المنهج " ( 1977 – 1991 ) حيث ينبّه إلى كون الواقع مركّبا على
> اعتبار أن الإنسان هو في آن كائن بيولوجي وفاعل اجتماعي وأن في الطبيعة ينشأ النظام من الفوضى كما
> تنشأ الفوضى من النظام.

⚠️ **Notice la plus longue de la tranche p.6-46** : elle court sur **deux pages** (bas de p.40,
haut de p.41), séparée par le pied de page — c'est la seule notice du مبحث dans ce cas.
⚠️ **Quatre titres d'œuvres sont imprimés en BLEU CYAN** (`النجوم`, `وحدة الإنسان`,
`العلم والضمير`, `المنهج`) alors que `الحجج` et `كاليفورنيا` sont en **noir gras** : la
distinction typographique n'est pas systématique.
⚠️ **`انظم`** [sic] — la forme attendue est `انضمّ` (avec ض) ; le manuel imprime bien un **ظ**,
vérifié à 600 dpi.
⚠️ **`إيديولوجــيا العصــر`** — kashidas d'allongement dans le corps du mot, tels qu'imprimés
(justification).
⚠️ Noms propres cités dans la notice : **جورج فريدمان** (Georges Friedmann), **رولان بارت**
(Roland Barthes) — **aucune graphie latine** n'est donnée pour eux.

**المهام (verbatim, p.41 — encadré, 5 puces)** :
- أحدد التعريف الذي يستبعده الكاتب للذاتيّة.
- ماذا يعني أن يكون المرء ذاتا في نظر الكاتب؟
- أيّ دلالة لمركزيّة الذات يقدّمها الكاتب؟ هل تفيد تناقضا بين الفردي والكوني؟
- " أن يكون المرء ذاتا هو أن يكون مستقلا في ذات الوقت الذي يكون فيه تابعا ": هل من سبيل لحلّ هذه
  المفارقة؟
- هل يدفعني موقف الكاتب إلى مراجعة نمطحضوري في العالم؟

⚠️ **`نمطحضوري`** [sic] — **espace manquante** entre `نمط` et `حضوري`, vérifiée à 600 dpi puis à
600 dpi × 3 (les deux mots sont **soudés**, alors que les autres blancs de la même ligne sont
nets).
⚠️ La 4ᵉ puce **re-cite le texte du سند entre guillemets** (procédé déjà vu au سند 11) ; la
citation y est **légèrement reformulée** par rapport au corps (`في ذات الوقت الذي يكون فيه تابعا`
pour `وتابعا في الوقت ذاته`).

**Encadré-citation (p.41, cadre rose, sous l'image jaune)** :
> " أن يكون المرء ذاتا معناه أن يحتلّ موقعا " .
> **موران**

---

###### سند 14 — مرلوبونتي / M. MERLEAU- PONTY — « تجربة الجسد » — p.42-43

- **Auteur tel qu'imprimé** : ligne de source arabe **مرلوبونتي** ; ligne latine
  **`M. MERLEAU- PONTY`** ; notice **موريس مرلوبونتي (1908—1961)** ; **مرلوبونتي** dans le corps
  de la notice ; encadré-citation p.43 signé **مرلوبونتي**. Notice **complète** (aucun renvoi
  d'auteur), mais **close par un renvoi de lecture** vers une autre نافذة (voir ci-dessous).
- **Titre du سند** : **تجربة الجسد**
- **Source imprimée (2 lignes, arabe puis latine)** :
  **مرلوبونتي، فينومينولوجيا الإدراك**
  **M. MERLEAU- PONTY** ,*Phénoménologie de la perception* , éd. Gallimard, pp.230-231
- **Illustrations** : (p.42) **photographie noir et blanc** insérée en haut à gauche du corps du
  texte — **portrait d'homme** en veste et cravate, cheveux plaqués en arrière, regard vers
  l'objectif ; (p.43) **peinture en couleurs** en bas de page — un **homme nu debout dans un
  cylindre de verre lumineux**, main levée contre la paroi, et **trois figures nues** debout sur
  un **sol de bois** à sa gauche, sous un **ciel strié mauve et orangé** ; aucune légende, aucun
  nom d'artiste imprimé.

**التمهيد (verbatim)** :
> انتظم القول في الإنسان ضمن أفق يؤسّس الوجود على الفكر ولا يُنزّل الجسد في أفضل الأحوال سوى منزلة
> موضوع يواصل عيش الغربة التي فرضناها عليه. لم يبدد هذا الأفق كلّ ما استغلق علينا في شأن فهمنا
> لحقيقة ذواتنا ما دمنا نشعر في معيشنا اليومي بعلاقة حميميّة تصلنا بجسدنا.

**Thèse (reformulée)** : la tradition cartésienne nous a habitués à **congédier l'objet** : la
posture réflexive « purifie » d'un même coup l'idée du corps et celle de l'âme, en définissant le
corps comme **somme de parties sans intérieur** et l'âme comme un être **entièrement présent à
soi, sans distance**. Or l'expérience du **corps propre** (`الجسد الخاص`) révèle, **à l'inverse**,
un **mode d'existence ambigu** : vision, motricité et sexualité **ne peuvent pas** être reliées
entre elles ni au monde extérieur par des rapports **causaux**. Donc **le corps n'est pas un
objet**, et pour la même raison **ma conscience de lui n'est pas une pensée** : je ne peux ni le
décomposer ni le recomposer pour m'en faire une idée claire, son unité reste **implicite et
ambiguë**. Il est en permanence **autre que ce qu'il est** — à la fois sexualité et liberté,
enraciné dans la nature à l'instant même où la culture le transforme, **ni clos sur soi ni jamais
dépassé**. Il n'y a **pas d'autre voie** pour connaître le corps humain que de **le vivre**, et
« je suis mon corps » au moins dans la mesure où j'ai un acquis. L'expérience du corps propre
**s'oppose** ainsi au mouvement réflexif qui **ne nous donne que** la pensée du corps ou le corps
dans l'idée, **et non** l'expérience du corps ni le corps tel qu'il est.

⚠️ Le texte imprime en toutes lettres l'expression conclusive **« الجسد بمثابة ذات طبيعيّة، مخطّطا
مؤقّتا لكلّ كياني »** — reprise telle quelle par la 5ᵉ puce des مهامّ.

**هوامش** : **AUCUN encadré هامش** pour ce سند — ni p.42 ni p.43 ; **aucun appel de note** dans le
corps du texte (vérifié à 600 dpi sur les quatre bandeaux de la page).

**الكاتب (p.43) — notice COMPLÈTE, verbatim** :
> **موريس مرلوبونتي (1908—1961)**
> فيلسوف فرنسي معاصر وواحد من أهم فلاسفة الفينومينولوجيا، اشتغل أستاذا بالمعاهد والجامعات. توفي
> مبكّرا ورغم ذلك ترك موروثا فلسفيا هاما تشهد به أهم مؤلَّفاته التي نذكر منها " فينومينولوجيا
> الإدراك " ( 1945) وفيه قدّم تصوّره عن فينومينولوجيا وجوديّة تؤكّد أولويّة " **أنا موجود** " على
> " **أنا أفكّر** " وذلك وجه من استعادة مطلب هوسرل المتمثّل في " **العودة إلى الأشياء** " الذي
> يعني مع مرلوبونتي العودة إلى العالم قبل معرفته وإلى الذات بما هي حضور في العالم، وهو بذلك يراجع
> **الكوجيتو الديكارتي** مراجعة مكّنته من التأكيد على أنّ الوجود في العالم هو وجود جسدي. أمّا
> كتابه " العلامات " ( 1960 ) فمثّل رؤية جديدة للتاريخ والسياسة كما عايشها. وفي كتابه " العين
> والعقل " ( 1964 ) اهتمّ بمسألة الفنّ عامّة والرسم خاصّة مبيّنا أنّ الرّسم يعبّر عن علاقاتنا
> بالوجود الذي يصيّره الأثر الفنّي مرئيّا، دون أن يفهم ذلك على أنّ الفنّ محاكاة لشيء ما لأنّ
> الفنّ ليس شيئا آخر غير التجلّي وما به يحصل التعبير عن دروب الصمت. أمّا في كتابه " المرئي
> واللامرئي " ( 1964 ) فقد فتح السبيل إلى أنطلوجيا أصيلة تجاوز فيها ثنائيّة الذات – الموضوع
> مركّزا على وصف انفتاحنا على العالم، ويعدّ مفهوم **الجسد الخاص** مركزيّا في هذا المؤلَّف بما هو
> تجاوز للتقابل بين الجسد الموضوعي والجسد الظاهراتي.
> **لمزيد التعمّق انظر نافذة دعائم للتفكير، سياقات فكريّة: الفينومينولوجيا.**

⚠️ **Renvoi de lecture, imprimé en BLEU CYAN, dernière ligne de la notice** :
`لمزيد التعمّق انظر نافذة دعائم للتفكير، سياقات فكريّة: الفينومينولوجيا.` — **transcrit tel quel,
non résolu**. C'est le **premier renvoi vers une نافذة** (et non vers un autre سند) de la
tranche p.6-46.
⚠️ **Titres en BLEU CYAN** dans la notice : `فينومينولوجيا الإدراك`, `العلامات`, `العين والعقل`,
`المرئي واللامرئي` ; **`هوسرل`** est lui aussi en bleu (seul nom propre traité ainsi). En **noir
gras** : `أنا موجود`, `أنا أفكّر`, `العودة إلى الأشياء`, `الكوجيتو الديكارتي`, `الجسد الخاص`.
⚠️ Graphie **`أنطلوجيا`** (et non `أنطولوجيا`), telle qu'imprimée.

**المهام (verbatim, p.43 — encadré, 5 puces)** :
- أستحضر التحديد الديكارتي للجسد.
- أحدّد، انطلاقا من النصّ، دلالتي " الجسد الموضوع " و " الجسد الخاص " .
- كيف أفهم قول الكاتب " تكشف تجربة الجسد الخاص نمط وجود ملتبس " ؟
- أيّ فارق بين " الجسد في الفكرة " و " الجسد على حقيقته " ؟
- الجسد " مخطط مؤقّت لكلّ كياني ": أمتحن هذه الفكرة في ضوء فهمي لجسدي؟ أحرّر فقرة في الغرض.

⚠️ La 1ʳᵉ puce **renvoie implicitement à Descartes** (سند 6) sans le nommer : `التحديد الديكارتي
للجسد`.
⚠️ La 5ᵉ puce est composée avec un **point d'interrogation là où l'on attendrait un point**
(`أمتحن هذه الفكرة في ضوء فهمي لجسدي؟`), tel qu'imprimé.

**Encadré-citation (p.43, cadre rose double filet, à droite de la peinture)** :
> " تكشـف لنا تجربة الجســد الخاص نمط وجود ملتبس " .
> **مرلوبونتي**

---

###### سند 15 — إيمانيول ليفيناس / Emmanuel LEVINAS — « الجسد إحساس بالهويّة » — p.44-45

- **Auteur tel qu'imprimé** : ligne de source arabe **إيمانيول ليفيناس** ; ligne latine
  **`Emmanuel  LEVINAS`** (avec **double espace** entre prénom et nom, vérifié à 600 dpi) ;
  notice **إيمانيول ليفيناس: ( 1905 )** ; **ليفيناس** dans le corps de la notice (p.45) ;
  encadré-citation p.45 signé **ليفيناس**. Les **deux** graphies arabes longues sont
  **identiques** (`إيمانيول`, jamais `إيمانويل`) — vérifié à 600 dpi × 4 sur les deux
  occurrences. Notice **complète** (aucun renvoi).
- **Titre du سند** : **الجسد إحساس بالهويّة**
- **Source imprimée (2 lignes, arabe puis latine)** :
  **إيمانيول ليفيناس، تأملات حول فلسفة هتلر**
  **Emmanuel  LEVINAS;** *Quelques réflexions sur la philosophie de l'hitlérisme*
- **Illustrations** : (p.44) **photographie noir et blanc** insérée en haut à gauche du corps —
  **portrait d'homme âgé**, cheveux clairs dégarnis, costume sombre et cravate ; (p.45) **image
  en couleurs** en bas de page — une **silhouette humaine bras écartés**, lumineuse (jaune et
  blanc), superposée à un **globe terrestre**, cerclée d'**anneaux violets et bleus** sur fond
  noir ; aucune légende.

**التمهيد (verbatim)** :
> أُعتبر الجسد ولوقت طويل عرضا يتبع النفس ويثقل كاهلها ولكن رغم هوانه عندها، فقد ظلّ قوة تقاوم
> احتقارها ويفاجئها باستمرار بغرابته من جهة ما هو جسميّة حتى كان الاعتراف به هويّة للذات ما نزال
> نطلبها فلا ندركها. فماذا يعني أن نكون أجسادا؟

**Thèse (reformulée)** : le texte **expose d'abord la thèse qu'il combat**. Selon
« **التأويل القديم** », avoir un corps c'est le **supporter comme un objet du monde extérieur** :
il pèse sur Socrate comme les chaînes dans la prison d'Athènes, il l'emprisonne « comme le tombeau
qui l'attend », il **est l'obstacle** qui brise l'élan libre de la pensée et la ramène aux
conditions terrestres — **mais un obstacle à surmonter**. Ce sentiment de l'**étrangeté éternelle**
du corps a nourri le christianisme puis le libéralisme moderne, et a maintenu l'idéal ascétique.
**La thèse de l'auteur commence ici** : le corps **n'est pas seulement** cet intrus éternel, et
l'interprétation classique **rabaisse** (`يحطّ`) le **sentiment d'identité** qui nous lie à notre
corps — sentiment que certaines circonstances rendent plus aigu. Le corps **n'est pas seulement**
le plus proche et le plus familier des objets du monde, il **ne fait pas que** régir notre vie
psychique, notre humeur et notre activité : **au-delà de ces évidences naïves** se tient le
sentiment d'identité. Ne nous affirmons-nous pas dans cette **chaleur singulière** qui jaillit de
notre corps **avant** l'éclosion du moi qui prétendra s'en distinguer ? Les **liens du sang** ne
résistent-ils pas à toute épreuve bien avant l'éveil de l'intelligence ? D'où la conclusion
imprimée : dans une **discipline sportive dangereuse**, dans un exercice audacieux poussé jusqu'à
une perfection presque irréelle et **qui menace de mort**, **toute dualité entre le moi et le corps
doit disparaître**.

⚠️ **Les négations sont ici des « ne… pas seulement »** (`ليس … فحسب`, `ليس … فقط ولا هو`,
`فهو لا يتحكّم … فحسب`) : elles **ajoutent** au corps, elles ne le nient pas. Les deux dernières
questions sont **rhétoriques** (`ألا نُثبت…؟`, `ألا تصمد…؟`) et **affirment** ce qu'elles
interrogent.
⚠️ Les deux **appels de note** sont dans le corps : **(1)** après `سقراط`, **(2)** après
`عصر النهضة`.

**الهامشان (verbatim, p.45 — encadré, titre au DUEL `الهامشان`, 2 notes)** :
> 1– **سقراط** : فيلسوف يوناني ( 469—399 ق م )، تتلمذ عليه أفلاطون الذي جعله الشخصيّة الأساسيّة
> لمحاوراته. عرف باستعماله أسلوب الحوار وطريقة التوليد. أُعدم بسبب آرائه.
> 2– **عصر النهضة** : هو عصر بداية الحداثة الأوروبيّة الذي انطلق مع الإصلاح الديني وتعزّز مع نشأة
> العلم الحديث.

⚠️ Intervalle `( 469—399 ق م )` — **ordre correct** (décroissant, av. J.-C.), vérifié à 600 dpi.
Le manuel écrit ici **`ق م`** sans points, alors qu'il écrit **`ق. م`** ailleurs (سند 9).
⚠️ La note 1 ne donne **aucune graphie latine** pour Socrate, et **ne nomme pas** le dialogue.

**الكاتب (p.44-45) — notice COMPLÈTE, verbatim** :
> **إيمانيول ليفيناس: ( 1905 )**
> فيلسوف فرنسي من أصل ليتواني، تأثّر بهوسرل وكتب عنه " نظريّة الحدس في فينومينولوجيا هوسرل "
> ( 1930 ). فساهم في نشر فكره بفرنسا. احتفظ من فلسفة هوسرل بمنهج التحليلات القصديّة كما تأثّر
> بهيدغر ثمّ اتخذ منه مسافة نقديّة ليتفرّد، في ضوء تجربته مع النازيّة، بأفكاره في **الإيتيقا**
> التي يقدّمها على **الأنطلوجيا** خلافا لهيدغر. والفكرة المحوريّة لفلسفته تدور حول مقولة الآخر من
> حيث هو تجربة أساسيّة ينتفي خارجها كلّ معنى. فالآخر أو " **وجه الآخر** " يمثّل أمرا لا مردّ له
> لشخصي ولكينونتي، يحملني على احترامه وبدونه لا أعرف منزلتي. من أهمّ كتاباته الأخرى: " اكتشاف
> الوجود مع هوسرل وهيدغر " (1949) وقد استحضر فيه الجذور الفينومينولوجيّة لفلسفة الوجود كالقول
> بالعودة إلى الأشياء – هوسرل – والانتباه لمعنى فعل الوجود – هيدغر –. " الشموليّة واللانهائي "
> (1961) وفيه ينقد الشموليّة من جهة طلبها المعرفة المطلقة كما تظهر خاصّة مع فلسفة هيغل، ويؤكّد أن
> التجربة الأساسيّة للإنسان إنّما تكمن في العلاقة البيناذاتيّة، ويعدُّ هذا الكتاب دفاعا على
> الذاتيّة المؤسّسة على فكرة اللاتناهي من جهة علاقة الأنا بالآخر. وفي " إنسانيّة الإنسان الآخر "
> (1972) يقترح ليفيناس إنشاء إيتيقا جديرة بالإنسان قوامها تبادل المسؤوليّة بين الأنا والآخر. وفي
> " الإيتيقا واللانهائي " (1982) يستعرض مسيرته الفلسفيّة التي انتهت به إلى اعتبار الإيتيقا الفلسفة
> الأولى عن جدارة.

⚠️ **`( 1905 )` — année de naissance SEULE**, sans année de mort, alors que la notice cite un
ouvrage de 1982 : c'est la **seule notice de la tranche p.40-46 dont l'intervalle est ouvert**
(même cas que `موران: (1921)` au سند 13). Transcrit tel quel, **non complété**.
⚠️ **Titres en BLEU CYAN** : `نظريّة الحدس في فينومينولوجيا هوسرل`, `اكتشاف الوجود مع هوسرل
وهيدغر`, `الشموليّة واللانهائي`, `إنسانيّة الإنسان الآخر`, `الإيتيقا واللانهائي`. En **noir
gras** : `الإيتيقا`, `الأنطلوجيا`, `وجه الآخر`.
⚠️ Graphie **`الأنطلوجيا`** (comme `أنطلوجيا` au سند 14, et non `الأنطولوجيا`).
⚠️ **`دفاعا على الذاتيّة`** [sic] tel qu'imprimé (la rection attendue est `دفاعا عن`).
⚠️ Termes techniques relevés : **البيناذاتيّة** (intersubjectivité), **اللاتناهي** (l'infini),
**التحليلات القصديّة** (analyses intentionnelles), **مقولة الآخر**.

**المهام (verbatim, p.45 — encadré, 7 puces)** :
- أستحضر مثالا من تاريخ الفلسفة عن التأويل القديم للجسد.
- في ضوء الإحالة الواردة في النص على سقراط، أحدد دلالة تشبيه الجسد بالسجن.
- متى يصبح إحساسنا بالجسد إحساسا حادّا؟
- أيّ دور للجسد في الإحساس بالهويّة؟
- أستخرج الحجج التي ساقها الكاتب للتأكيد على ضرورة زوال الثنائيّة بين الأنا والجسد.
- أيّ دلالة للإنيّة في ضوء دعوة الكاتب إلى ضرورة زوال الثنائيّة؟
- هل يتوافق شعوري بهويتي مع ما ذهب إليه الكاتب؟

⚠️ **7 puces — le سند le mieux doté en مهامّ de la tranche p.40-46** (à égalité avec le سند 12,
p.38-39).

**Encadré-citation (p.45, cadre rose double filet, à droite de l'image du globe)** :
> " ففي مؤسّسة رياضيّة خطرة وفي تمرين جريء تبلغ فيه الحركات درجة إتقان تكاد تكون خياليّة تنذر
> بالموت، ينبغي أن تزول كلّ ثنائيّة بين الأنا والجسد " .
> **ليفيناس**

⚠️ **L'encadré-citation le plus long de la tranche p.6-46** — 6 lignes composées ; il reprend
**mot pour mot la phrase finale du texte** du سند.

---

###### سند 16 — ج. ب. سارتر / SARTRE — « تجربة الخجل » — p.46 (suite p.47)

- **Auteur tel qu'imprimé** : ligne de source arabe **ج. ب. سارتر** (initiales séparées par des
  points, vérifié à 600 dpi × 3) ; ligne latine **`SARTRE`** **seul, sans prénom ni initiales** ;
  encadré-citation p.46 signé **سارتر**. La notice **الكاتب** n'est **pas** sur p.46.
- **Titre du سند** : **تجربة الخجل**
- **Source imprimée (2 lignes, arabe puis latine)** :
  **ج. ب. سارتر، الوجود والعدم**
  **SARTRE;** *L'Etre et le Néant,* 3e partie, I, 1, éd. Gallimard. pp 265 - 266
- **Illustrations** : (p.46, haut) **photographie en couleurs**, fortement postérisée, insérée
  dans le corps du texte — **homme âgé à lunettes**, costume sombre et cravate, **parlant dans un
  micro** ; (p.46, bas) **grande image en couleurs** occupant le bas de page — **visage
  solarisé** coupé en deux, **magenta/rouge** d'un côté, **bleu-violet** de l'autre, **deux yeux**
  fortement contrastés (l'un cerclé de bleu, l'autre jaune) et des **traits de lumière**
  rayonnants ; aucune légende, aucun nom d'artiste imprimé.

**التمهيد (verbatim)** :
> إذا كانت " نظرة كلب إليّ لا تحرجني " ( مرلوبونتي ) فإنّ نظرة الآخر إليّ تربكني مادام يشاركني
> الوجود ويحملني على الاعتراف به في الوقت الذي أعمل فيه على تأكيد ذاتيّتي.

⚠️ Ce التمهيد **cite nommément مرلوبونتي** (سند 14, p.42-43) entre parenthèses : **lien interne
imprimé** entre deux سندات voisins.

**Thèse (reformulée)** : la honte, dans sa **structure originelle**, est **honte devant
quelqu'un**. Un geste maladroit ou vulgaire me colle à la peau ; **il ne m'appartient pas** de le
juger ni de le condamner, je n'ai qu'à le vivre. Mais je lève la tête : **quelqu'un était là et
m'a vu**. Je saisis aussitôt la grossièreté de mon geste et la honte me saisit — **j'ai honte de
moi tel que j'apparais à autrui**. Par cette apparition d'autrui, je me trouve prêt à me juger
**comme on juge une chose**, parce que **c'est comme chose que j'apparais aux autres**. Et
pourtant, cette chose apparue à autrui **n'est pas une image falsifiée dans un esprit** : le texte
écarte explicitement cette hypothèse, **dont la conséquence serait** que l'image « serait imputée
tout entière aux autres » et **ne me « toucherait » pas** — je n'éprouverais alors qu'agacement ou
colère, comme devant un mauvais portrait qui me prête une laideur qui n'est pas la mienne,
**sans en être remué jusqu'à la moelle**. Conclusion imprimée : **la honte est par nature un
aveu** — l'aveu que **je suis tel que les autres me voient**.

⚠️ **Piège de lecture signalé** : la phrase `إنّ هذه الصورة ستُسنَدُ كليّا إلى الآخرين ولن
" تؤثَّر " فيّ` **n'est pas** la thèse de l'auteur — c'est la **conséquence de l'hypothèse qu'il
vient de rejeter** (`ليس صورة مزيّفة في فكر`). Vérifié à 600 dpi × 3 : les guillemets encadrent
bien le seul mot `تؤثَّر`, et la négation `ولن` porte sur lui.
⚠️ Le texte porte **deux coupes éditoriales** notées `( ... )` (après `بكلّ بساطة`, et après
`فيعتريني الخجل`) et **une insertion entre crochets** `[ بهذا ]` (ajout du traducteur, non
signalé comme tel).
⚠️ **Aucun appel de note** dans le corps ; **aucun encadré هامش** sur p.46.

**Encadré-citation (p.46, cadre rose, à droite de la grande image)** :
> " إن الخجل هو بالطبيعة اعتراف. اعتراف بأنّي أكون كما يراني الآخرون " .
> **سارتر**

⚠️ **Cet encadré-citation est bien imprimé p.46** (à droite de la grande image du bas) : il
reprend **mot pour mot les deux dernières phrases du texte**.
⚠️ **Mais il n'est pas le seul de ce سند.** La p.47 en porte un SECOND, à côté d'une peinture de
deux masques de théâtre : « أخجل من نفسي كما أظهر للآخرين » — **سارتر**. Vérifié sur les deux
pages par l'orchestrateur. Le سند 16 porte donc **deux encadrés-citation, un par page**.

⚠️ **Suite p.47 — notice الكاتب, مهامّ et encadré-citation déjà transcrits (fragment ch1b).**

---

##### § Notes, anomalies et incertitudes — fragment ch1a, tranche p.40-46

**Ce que la tranche contient — compté sur les pages, pas déduit**

| سند | auteur imprimé (arabe / latin) | titre | étendue **réelle** | notice الكاتب | encadré هوامش | مهامّ | encadrés-citation |
| :-- | :-- | :-- | :-- | :-- | :-- | :-: | :-: |
| 13 | ادڤار موران / `Edgar MORIN` | مركزيّة الذات | **p.40-41** (2 p.) | **complète**, à cheval **p.40→p.41** | **oui** — titre `الهامشان`, **2** notes (p.41) | **5** | **1** (p.41) |
| 14 | مرلوبونتي / `M. MERLEAU- PONTY` | تجربة الجسد | **p.42-43** (2 p.) | **complète** (p.43) + **renvoi de lecture** vers une نافذة | **AUCUN** | **5** | **1** (p.43) |
| 15 | إيمانيول ليفيناس / `Emmanuel  LEVINAS` | الجسد إحساس بالهويّة | **p.44-45** (2 p.) | **complète**, à cheval **p.44→p.45** | **oui** — titre `الهامشان`, **2** notes (p.45) | **7** | **1** (p.45) |
| 16 | ج. ب. سارتر / `SARTRE` | تجربة الخجل | **p.46** (+ suite p.47) | **absente de p.46** → p.47 | **AUCUN** sur p.46 | **0** sur p.46 → p.47 | **1** (p.46) |

- **4 سندات**, **0 renvoi d'auteur** dans cette tranche : les trois notices présentes sont
  **complètes**. C'est l'inverse du مبحث 3.2 (13 renvois sur 18) et la suite de la tendance du
  مبحث 1.1 (1 seul renvoi sur les 12 premiers سندات).
- **2 encadrés هوامش sur 4 سندات** ; **4 notes** au total, toutes p.41 et p.45.
- **17 puces de مهامّ** comptées (5 + 5 + 7) sur p.41, p.43, p.45.
- **4 encadrés-citation**, un par سند, tous signés du nom court de l'auteur.
- **Deux notices sur trois sont à cheval sur deux pages** (13 et 15) : le pied de page les coupe.
- **Règle du titre des هوامش, vérifiée sur 3 boîtes** : le manuel accorde le titre au **nombre de
  notes** — `الهامش` (singulier) pour 1 note p.39, `الهامشان` (**duel**) pour 2 notes p.41 et p.45.
- **Contrôle du فهرس** : pour cette tranche il est **exact** — numéros 13-16, auteurs
  (موران / مرلوبونتي / ليفيناس / سارتر), titres et pages de départ (40, 42, 44, 46) correspondent
  tous à la page. Seule nuance : le فهرس n'emploie que les **noms courts**, là où les pages
  donnent aussi les prénoms.

**Anomalies réelles de la source — chacune vérifiée à 600 dpi**

1. **p.41, مهامّ, 5ᵉ puce — `نمطحضوري`** : **espace manquante** entre `نمط` et `حضوري`. Vérifié à
   600 dpi puis agrandissement ×3 : les deux mots sont **soudés**, alors que les blancs voisins de
   la même ligne (`… في العالم؟`) sont nets. **Seule espace réellement absente de la tranche.**
2. **p.40, notice سند 13 — `انظم`** : composé avec **ظ** ; la forme attendue est `انضمّ` (ض).
   Vérifié à 600 dpi ×3.
3. **p.42, ligne latine du سند 14** — quatre défauts de composition sur une seule ligne :
   `M. MERLEAU- PONTY` (**espace après le trait d'union**), `PONTY ,Phénoménologie` (**virgule
   collée au titre et précédée d'une espace**), `perception , éd.` (**espace avant la virgule**),
   `pp.230-231` (**pas d'espace après `pp.`**). Vérifié à 600 dpi ×3.
4. **p.44, ligne latine du سند 15** — `Emmanuel  LEVINAS` avec **double espace** ; et la référence
   s'arrête au titre : **ni éditeur, ni date, ni pages**. C'est la **seule référence de la
   tranche** qui n'en donne aucune.
5. **p.46, ligne latine du سند 16** — `L'Etre et le Néant` : **`Etre` sans accent circonflexe** ;
   et `éd. Gallimard.` **point** au lieu de virgule avant `pp 265 - 266`. Vérifié à 600 dpi ×2.
6. **p.45, notice سند 15 — `دفاعا على الذاتيّة`** : rection attendue `دفاعا عن`.
7. **p.45, هامش 1 — `ق م` sans points**, là où le manuel écrit `ق. م` au سند 9 (p.32-33). Les deux
   formes coexistent dans le même مبحث.
8. **p.43, مهامّ, 5ᵉ puce** — **point d'interrogation** là où un point est attendu :
   `أمتحن هذه الفكرة في ضوء فهمي لجسدي؟ أحرّر فقرة في الغرض.`
9. **Écart avec la consigne de tranche (et non avec la source)** : l'**encadré-citation du
   سند 16 est bien imprimé p.46**, à droite de la grande image, et non p.47. Seuls la notice
   **الكاتب** et les **مهامّ** de ce سند passent p.47.

**Fausses pistes écartées — ce que j'ai cru voir et qui n'y était pas**

1. **Le « point » avant chaque ب initial — 3 fausses coquilles évitées.** À 150 dpi *et* à 600 dpi
   en vue large, `الموضوع.بمحيطه` et `وربطه.بمن` (p.41) puis `و.بمساعدة` (p.40) paraissent porter
   un **point en pleine phrase**. Agrandissement 600 dpi ×5, avec deux témoins sur la même ligne —
   le ب **médial** de `ربطه` (point sous la lettre) et le ب **initial** de `بالسينما` p.40 — :
   c'est **le point diacritique du ب lui-même**, posé au bord droit de la lettre, qui tombe dans le
   blanc inter-mots parce que le ب ne se lie pas à droite. **Aucun point n'est imprimé.**
2. **`إلىالاهتمام` (p.40) et `فيذات` (p.41)** : lus soudés à 150 dpi. À 600 dpi l'espace est
   **présente**, seulement resserrée par la justification. C'est le contraste avec ces deux cas
   qui a permis d'établir que `نمطحضوري` (anomalie 1) l'est réellement.
3. **`الأيحاث` (p.41)** : lu ainsi à 150 dpi ; à 600 dpi le manuel imprime bien **`الأبحاث`**.
4. **L'intervalle du « المنهج » (p.41) cru inversé.** Le rendu écran donne `1991` à gauche et
   `1977` à droite, ce qui ressemble aux intervalles retournés que ce manuel produit ailleurs.
   **Calibration** : la notice de **مرلوبونتي** (p.43) porte `(1908—1961)` — dates certaines — et
   se rend visuellement `1961—1908`. Donc, **dans ce PDF, le nombre logiquement premier s'affiche
   à DROITE**. L'intervalle du « المنهج » est **dans le bon ordre** : `( 1977 – 1991 )`. **Pas de
   `[sic]`.** ⚠️ Étalon réutilisable pour les tranches suivantes.
5. **`إيمانويل` vs `إيمانيول` (p.44)** : soupçon de double graphie entre la ligne de source et la
   tête de notice. À 600 dpi ×4 sur **les deux** occurrences : `إيمانيول` dans les deux cas.
   **Aucune variante.**

**Intervalles de dates — vérifiés un à un**

| Lieu | Tel qu'imprimé (ordre **logique**) | Rendu **visuel** | Verdict |
| :-- | :-- | :-- | :-- |
| p.40, tête de notice سند 13 | `موران: (1921)` | — | **intervalle ouvert** — naissance seule, pas de date de mort |
| p.41, notice سند 13 (« المنهج ») | `( 1977 – 1991 )` | `1991 – 1977` | **ordre correct** |
| p.43, tête de notice سند 14 | `(1908—1961)` | `1961—1908` | **ordre correct** — **étalon de la tranche** |
| p.44, tête de notice سند 15 | `إيمانيول ليفيناس: ( 1905 )` | — | **intervalle ouvert** — naissance seule, alors que la notice cite un ouvrage de 1982 |
| p.45, هامش 1 سند 15 (سقراط) | `( 469—399 ق م )` | `399—469 ق م` | **ordre correct** (décroissant, av. J.-C.) |

**Aucun intervalle retourné dans cette tranche.** Les dates **isolées** (aucune n'est un
intervalle) : 1951, 1956, 1957, 1968, 1970, 1974, 1982 (p.40-41) ; 1945, 1960, 1964, 1964 (p.43) ;
1930, 1949, 1961, 1972, 1982 (p.44-45). Les seuls autres nombres composés en intervalle sont des
**pages** : `pp 88 - 89` (p.40), `pp.230-231` (p.42), `pp 265 - 266` (p.46).

**Variantes de graphie des noms propres**

- **Morin — 3 formes** : `ادڤار موران` (ligne de source, avec **ڤ** à trois points) · `Edgar MORIN`
  (latine) · `موران` (tête de notice, corps, هامش 2, encadré).
- **Merleau-Ponty — 3 formes** : `مرلوبونتي` (ligne de source, corps de notice, encadré, **et
  التمهيد du سند 16 p.46**) · `موريس مرلوبونتي` (tête de notice) · `M. MERLEAU- PONTY` (latine).
- **Levinas — 3 formes** : `إيمانيول ليفيناس` (ligne de source **et** tête de notice, identiques) ·
  `ليفيناس` (corps de notice, encadré) · `Emmanuel  LEVINAS` (latine).
- **Sartre — 3 formes** : `ج. ب. سارتر` (ligne de source, initiales pointées) · `SARTRE` (latine,
  **sans prénom ni initiales**) · `سارتر` (encadré).
- **Cités sans aucune graphie latine** : `جورج فريدمان`, `رولان بارت` (p.40) · `هوسرل` (p.43,
  p.44-45) · `هيدغر` (p.44-45) · `هيغل` (p.45) · `سقراط`, `أفلاطون` (p.45). Descartes n'apparaît
  que par l'adjectif : `الديكارتي` (p.41 هامش 2, p.43 مهامّ), `الكوجيتو الديكارتي` (p.43).
- **Termes translittérés relevés tels quels** : `الإيتيقا` · `أنطلوجيا` / `الأنطلوجيا` (p.43 et
  p.44 — **même graphie sans و après le ط** aux deux endroits, donc graphie de maison et non
  coquille isolée) · `الابستيمولوجيّة` · `الفينومينولوجيا` / `فينومينولوجيا` · `البيناذاتيّة` ·
  `اللاتناهي` · `القصديّة` · `الشموليّة`.

**Incertitudes résiduelles**

- **Aucun `[?]`** : les quatre pages sont entièrement lisibles à 600 dpi ; rien n'a été deviné.
- **Images non attribuées** : les quatre images en couleurs (p.41, p.43, p.45, p.46) ne portent
  **ni légende ni nom d'artiste**. Elles sont décrites, **jamais attribuées**.
- **Renvoi non résolu** (سند 14, p.43) : `لمزيد التعمّق انظر نافذة دعائم للتفكير، سياقات فكريّة:
  الفينومينولوجيا.` — la نافذة visée est hors de la tranche p.40-46 ; transcrite telle quelle.
- **Suite du سند 16** : notice **الكاتب** et **مهامّ** sont p.47, hors tranche (fragment ch1b).
- **Sens du texte du سند 16** : la phrase `ستُسنَدُ كليّا إلى الآخرين ولن " تؤثَّر " فيّ` est la
  **conséquence de l'hypothèse rejetée**, pas la thèse de l'auteur. Signalé en clair dans le corps
  de la fiche pour que la génération de contenu ne l'inverse pas.


##### § نافذة 1.1.2 — سندات للتفكير في المسألة — p.47–74 (**suite** : سندات 17→29)

###### سند 17 — د. هيوم / دافيد هيوم — « هل الأنا وهم؟ » — p.48-49

- **Auteur tel qu'imprimé** : ligne de source **د. هيوم** ; ligne latine **`D. HUME`** ; notice
  **الكاتب** : **دافيد هيوم ( 1711 – 1776 )**. Encadré-citation signé **هيوم**.
  ⚠️ Trois graphies pour le même auteur sur deux pages (`د. هيوم` / `هيوم` / `دافيد هيوم`).
- **Titre du سند** : **هل الأنا وهم؟**
- **Source imprimée** :
  **د. هيوم، رسالة في الطبيعة االبشريّة** — `االبشريّة` [sic] : **alif doublé**, vérifié à 600 dpi.
  `D. HUME Traité de la nature humaine, 1737; L 1,éd. Aubier- Montaigne t1; 1973; pp 342 -343`
  ⚠️ Le millésime **1737** de la ligne latine **diverge** de la notice de la page suivante, qui
  date la *رسالة في الطبيعة البشريّة* de **1739-1740**. Divergence **imprimée**, constatée, non corrigée.
- **Illustration** : portrait gravé/peint de Hume (vignette insérée dans le texte, p.48).

**التمهيد (verbatim)** :
> يستمد الأنا يقينه بذاته من الفكر بما هو جوهر سمته الثبات و الديمومة حتّى صار بداهة لا يرقى إليها
> الشك، لكن لَوْ جاز أن نمتحن الأنا على قاعدة التجربة أو الانطباعات الحسيّة ، مجال التعاقب والتحوّل ،
> لانحلّت حينها فكرة البداهة وحلّ الارتياب محلّ اليقين .

**Thèse (reformulée)** : contre les philosophes qui croient saisir à chaque instant, avec une
évidence supérieure à toute démonstration, un « moi » simple et identique, Hume oppose l'expérience
même dont ils se réclament : **aucune impression constante et invariable** ne peut fonder cette
idée — douleur, plaisir, passions et sensations **se succèdent** et ne coexistent jamais toutes.
L'idée du moi **ne peut donc dériver d'aucune de ces impressions ni d'aucune autre** : une telle
idée **n'existe pas**. Quand il pénètre au plus profond de ce qu'il nomme « moi », Hume ne rencontre
jamais qu'une perception sensible particulière ; là où les perceptions s'interrompent (sommeil
profond), il n'a plus le sentiment de soi et peut dire qu'il n'existe pas.

**هوامش** : **aucun encadré de notes** pour ce سند (ni p.48 ni p.49).

**الكاتب (notice, p.49)** :
> **دافيد هيوم ( 1711 – 1776 )** — فيلسوف انقليزي، ولد في إدمبرة ويعدّ أحد وجوه المذهب الخبري.
> وكانت فلسفته نقديّة تتجه نحو نقد العقلانيّة كما تُفهم لدى ديكارت خاصّة. ضمّن هيوم كتابه
> « رسالة في الطبيعة البشريّة » (1739 – 1740) أهمّ أفكاره واعتبره « محاولة لتطبيق المنهج التجريبي على
> الموضوعات الأخلاقيّة ». فقد وضع في هذا المؤلَّف أسس « علم بالإنسان » موضوعه الطبيعة البشرية وبسط فيه
> أيضا آراءه في « أصل الأفكار » والإدراكات ليساهم بقول متفرّد في أهمّ انشغالات الخبريين من قبله، وذلك
> بالإقرار بأن الأفكار ليست إلا نسخ للانطباعات الحسيّة، ممّا يعني رفض القول بالأفكار المجرّدة والفطريّة
> وفكرة الهويّة الخالصة وذلك على أساس ما يُجمع عليه سائر الخبريين بأنّ التجربة هي مصدر المعرفة الوحيد.
> أمّا في خصوص معرفتنا بالطبيعة فلا تتعدى الوقائع الجزئيّة ممّا ينتج عنه ريبيّة بشأن العلم
> والميتافيزيقا. وفي مؤلَّف عن الدين « محاورات حول التاريخ الطبيعي للدين » (1779) عالج هيوم مسألة
> الاعتقاد الديني بروحه الريبيّة رافعا لبسا شائعا بين « الدين الوضعي » و« الدين الطبيعي ». لهيوم
> مصنّفات فلسفيّة أخرى أهمّها « محاولات فلسفيّة في الذهن البشري » أو « بحث في الذهن البشري » (1748)…

**المهام (verbatim, 5 puces)** :
- أستحضر التصوّرات التي يعتزم الكاتب دحضها من خلال عيّنة سبق أن درستها؟
- أحلل دلالة التناقض الذي يواجه به الكاتب خصومه.
- ما الذي يشرّع للكاتب رفض اعتبار الأنا فكرة أو انطباعا؟
- إذا أنكرت أن يكون الفكر قوام وجودي، فما الذي يشهد على وجودي؟ أستأنس بالنصّ لفكّ هذا الحرج؟
- هل يستوجب تصوّر الكاتب مراجعة لدلالة الإنيّة؟

**Encadré-citation (p.49, cadre rose, à côté d'une photographie — silhouette noire d'un homme bras
écartés sur fond orange granuleux)** :
> " فلا تستطيع فكرة الأنا أن تنتُج عن أيّ من هذه الانطباعات ولا من غيرها، وبالنتيجة لا وجود لمثل
> تلك الفكرة ".
> — **هيوم**

⚠️ Le corps du texte (p.48) porte la **même** phrase sous une forme légèrement différente
(`فلا يمكن أن تنتُج فكرة الأنا عن أيّ من هذه الانطباعات ولا عن غيرها`) : l'encadré n'est donc **pas**
un copier-coller strict du texte. Vérifié à 600 dpi.

---

###### سند 18 — كارل ماركس و ف. انغلز — « هل الوعي كيان مستقل؟ » — p.50-52

⚠️ **Ce سند occupe TROIS pages** (50, 51, 52) : texte + تمهيد p.50, notice **الكاتبان** p.51,
هامشان + مهامّ + encadré p.52. La double page n'est pas la règle.

- **Auteurs tels qu'imprimés** : ligne de source **كارل ماركس وف. انغلز** ; ligne latine
  **`Karl MARX et F. ENGELS`**. Notice : titre **الكاتبان** (duel), puis **ماركس: (1818 – 1883)** et
  **فيدريك انغلز (1820 – 1895)**. Encadré-citation signé **ماركس**.
- **Titre du سند** : **هل الوعي كيان مستقل؟**
- **Source imprimée** : **كارل ماركس وف. انغلز، الايديولوجيا الألمانيّة** —
  `Karl MARX et F. ENGELS; L'Idéologie allemande, éd. sociales` (pas de pagination imprimée).
- **Illustration** : portrait photographique de Marx (vignette dans le texte, p.50) ; portrait
  photographique d'Engels (vignette dans la notice, p.51).

**التمهيد (verbatim)** :
> إذا كان الموقف التأمّلي قد أولى الوعي منزلة الجوهر والمبدأ والمحدّد لماهيّة الإنسان فإنّ معاينة واقع
> الإنسان تدفعنا إلى التظنّن على الوعي حين نكتشف شروط تكوّنه والارتياب في صورة للإنسان تتحدّد باستقلال
> عن نشاطه المادي.

**Thèse (reformulée)** : la production des idées, des représentations et de la conscience est
d'emblée liée à l'activité matérielle et aux rapports matériels entre les hommes — elle est
« la langue de la vie réelle ». Ce sont les hommes **réels et agissants**, conditionnés par un
développement déterminé de leurs forces productives, qui produisent leurs représentations ; la
conscience **ne peut jamais être autre chose que l'être conscient**, et l'être des hommes est le
procès réel de leur vie. À l'inverse de la philosophie allemande, qui descend du ciel sur la terre,
Marx et Engels **montent de la terre au ciel** : ils partent de l'activité réelle. Morale, religion,
métaphysique et formes de la conscience **perdent alors toute autonomie : elles n'ont ni histoire
ni développement propres**. Conclusion imprimée : **ce n'est pas la conscience qui détermine la
vie, mais la vie qui détermine la conscience.**

**الهامشان (verbatim, p.52 — 2 notes, appelées `(1)` et `(2)` dans le texte p.50)** :
> 1– **الايديولوجيا**: هي منظومة من الأفكار تدعي الحياد ولكنها بالنسبة إلى ماركس تترجم في الحقيقة
> واقعا اقتصاديا واجتماعيا. وتستعمل في هذا السياق للدلالة على الوعي الزائف بهذا الواقع.
> 2– **الفلسفة الألمانية**: المقصود بها فلسفة هيغل التي تؤكد على أولوية الوعي بما هو محدّد للوجود الواقعي.

**الكاتبان (notice, p.51 — deux notices distinctes)** :
> **ماركس: (1818 – 1883)** — فيلسوف ألماني من عائلة ثرية، درس القانون والفلسفة وانتمى إلى حلقة
> الهيغليين اليساريين مما يدلّل على أنّ الفكر الماركسي تطوّر كنتاج لنقد الإرث الهيغلي. بدأ ماركس في
> كتابه « نقد فلسفة الحق عند هيغل » (1844) إلى قلب الجدل الهيغلي بإبراز
> أن أشكال الوعي هي نتاج العلاقات والشروط المادية للبشر. عرف النفي منذ سنة 1845 إذ نفي إلى باريس ومنها
> إلى بروكسال ثم إلى لندن حيث توفي سنة 1883. أنتج، استنادا إلى أطروحات فيورباخ، تصورا ماديا للتاريخ
> طوّره بمعيّة رفيقه أنغلز في نقد الفلسفة الألمانية (« الإيديولوجيا الألمانية »، 1846) وحدّد فيه الأسس
> الفلسفية للماركسية وللمادية التاريخية وبلور نظريّته في الملكيّة الخاصّة والصراع الطبقي. في حين تعلق
> الأمر في « بؤس الفلسفة » (1847) بنقد فلسفة البؤس لبرودون. كما أصدر مع **أنغلز** « بيان الحزب
> الشيوعي » (1848) لخّص فيه الأطروحات الأساسية للماركسية في لغة مبسطة ( العمل المأجور – رأس المال –
> التبادل الحر – تاريخ المجتمع – تاريخ الصراع الطبقي ). يُعدُّ « رأس المال » ( الكتاب الأول منه نشر
> في حياته 1867) أهم أثر **لماركس** أما الكتاب الثاني والثالث فقد نشرهما أنغلز سنتي 1885 و1894 نقد
> فيه الاقتصاديين الإنقليزيين ( **سميث وريكاردو** ) وحدد فيه دلالة الربح وفائض القيمة مؤكدا على مظاهر
> استغلال العمل وواقع اغترابه الذي رصده ماركس في كل المجالات: الاقتصادي والديني والسياسي والإيديولوجي.
> غير أن الاغتراب الاقتصادي اعتبر الصورة الجوهرية للاغتراب مادام يمسّ الشروط المادية للوجود ولذلك أكد
> **ماركس** أن تحليل التحولات التاريخية ينبغي أن يكون بالأساس تحليلا للبنى التحتية ( علاقات وأدوات
> وقوى الإنتاج ) التي تحدد البنية الفوقية ( أشكال الوعي المختلفة ). كتب أيضا و في نفس القضايا:
> « العمل المأجور ورأس المال » (1848)؛ « أسس نقد الاقتصاد السياسي » (1857 – 1858)؛ « مخطوطات 1848 » ؛
> ومع رفيقه أنغلز كتب أيضا « العائلة المقدّسة » (1845). وانتهى في معظم كتاباته إلى التأكيد على أنّ
> الصراع الاجتماعي الراهن بين طبقة الرأسماليين والطبقة العاملة ( البروليتاريا ) سيفضي إلى ثورة عارمة
> تقود الطبقة العاملة إلى السلطة لتأسيس المجتمع الشيوعي الذي ينتفي فيه الصراع الطبقي بانتفاء الملكيّة
> الخاصّة لوسائل الانتاج وتحلّ الحريّة محلّ الاستعباد والاغتراب.
>
> **فيدريك انغلز (1820 – 1895)** — فيلسوف وعالم اقتصاد ألماني، التقى بماركس سنة 1844 وأسّس معه
> الأمميّة الأولى (1864). ساهم معه في تأليف بعض الكتب، كما كانت له مؤلَّفاته الخاصّة ونذكر منها
> « ضدّ دوهرينغ » (1878) الذي بيّن فيه دور العنف في التاريخ واعتبره عاملا رئيسيّا في تحقيق التوافق بين
> البنية الفوقيّة السياسيّة والبنية التحتيّة الاقتصاديّة؛ وكذلك « أصل العائلة والملكيّة الخاصّة والدّولة »
> (1884) الذي قرأ فيه المعطيات الأنثروبولوجيّة المتوفّرة في عصره قراءة تستند إلى مبادئ الماركسيّة.

**Renvoi imprimé sous la notice (p.51, en bleu — verbatim)** :
> لمزيد التعمّق انظر نافذة دعائم للتفكير، سياقات فكريّة: فلسفة التاريخ.

**المهام (verbatim, 6 puces, p.52)** :
- ما المقصود بـ " علاقات الناس الماديّة" وبأيّ معنىتمثّل أساس إنتاج الوعي؟ *(`معنىتمثّل` collé [sic],
  vérifié à 600 dpi)*
- ما معنى أن يكون كيان البشر سيرورة الحياة الواقعيّة؟
- كيف أفهم هذه المماثلة التي يقيمها الكاتب بين الإيديولوجيا وشبكيّة العين؟
- فيم تختلف نظريّة ماركس عن السائد في الفلسفةالألمانيّة؟ *(`الفلسفةالألمانيّة` collé [sic])*
- ما دلالة استعمال الكاتب لمفهوم " الدماغ "؟
- " ليس الوعي هو الذي يحدد الحياة بل إنّ الحياة هي التي تحدد الوعي ": هل يدفعونا هذا القول إلى
  مراجعة مشكل العلاقة بين الإنيّة والغيريّة في تحديد الإنسان؟ *(`يدفعونا` [sic] pour `يدفعنا`,
  vérifié à 600 dpi)*

**Encadré-citation (p.52, à côté d'une image — visage humain composé de vues aériennes de villes et
de circuits imprimés)** :
> " ليس الوعي هو الذي يحدد الحياة بل إنّ الحياة هي التي تحدّد الوعي. "
> — **ماركس**

---

###### سند 19 — فريدريك نيتشه — « الوعي نتاج التواصل » — p.53-54

- **Auteur tel qu'imprimé** : ligne de source **فريدريك نيتشه** ; ligne latine
  **`Friedrich NIETZSCHE`** ; notice **الكاتب** : **نيتشه: ( 1844 – 1900 )**. Encadré signé **نيتشه**.
  ✅ Ordre des dates **vérifié à 600 dpi** : il est **correct** (1844 puis 1900), ce n'est **pas** un
  des intervalles inversés du manuel.
- **Titre du سند** : **الوعي نتاج التواصل**
- **Source imprimée** (trois lignes) :
  **فريدريك نيتشه، المعرفة المرحة**
  `ترجمة حسان بورقية – محمد الناجي، أفريقيا الشرق، 2000، ص 216 – 217 ( مع مراجعة لجنة التأليف )`
  `Friedrich NIETZSCHE; Le Gai Savoir, Gallimard, 1982, pp 252 - 253`
  ⚠️ Mention explicite d'une **révision de la traduction par la commission de rédaction du manuel** —
  le texte arabe imprimé n'est donc pas strictement celui de l'édition citée.
- **Illustration** : portrait photographique de Nietzsche (vignette dans le texte, p.53).

**التمهيد (verbatim)** :
> على افتراض أن حضور الوعي سمة وجودنا المميّزة فإنّ مشكل الوعي لا يُختزل في حضوره من عدمه وإنّما
> يتّصل أساسا بأصله وقيمة هذا الأصل وكيفيّة تقييمه: أساس للوجود أو عرض من أعراضه، مبدأ أو نتاج،
> حقيقة وجود أو وهم فلاسفة.

**Thèse (reformulée)** : nous pouvons penser, sentir, vouloir, nous souvenir, agir — **sans que
rien de cela ait besoin d'« entrer dans notre conscience »** ; la vie entière est possible sans se
réfléchir. Si la conscience est pourtant là, c'est que sa finesse et sa force sont toujours
proportionnelles à la **faculté de communiquer** (`ملكة التواصل`), elle-même dépendante du **besoin
de communiquer** (`حاجة التواصل`) — non celui de l'individu isolé, mais celui d'espèces entières et
de générations que la nécessité a contraintes à s'entendre vite et finement. La conscience
**ne s'est développée que sous la pression du besoin de communication**, et **n'a été nécessaire et
utile que dans les relations d'homme à homme**, singulièrement entre celui qui commande et celui
qui obéit. Elle **n'est donc, en gros, qu'un réseau de liens entre les hommes** ; un homme vivant
isolé, comme un fauve, aurait pu s'en passer.

**هوامش** : **aucun encadré de notes** pour ce سند (ni p.53 ni p.54).

**الكاتب (notice, p.54)** :
> **نيتشه: ( 1844 – 1900 )** — فيلسوف ألماني، من أسرة من القساوسة، لكنه كان شديد الإلحاد. تأثر
> **بشبنهاور** لتشاؤمه ولكنه انقلب عليه ليعتنق فلسفة الحياة. عُيّن سنة 1869 أستاذا في جامعة « بال »
> ليدرس **الفيلولوجيا** و لم يكن قد حصل على الدكتوراه، ولكنه سرعان ما قطع مع مسيرته الجامعية لأسباب
> صحية، والتي انتهت به بعد عطاء غزير في الكتابة إلى الجنون. وتعد كتاباته أحد أهم الكتابات في تاريخ
> الفلسفة، التي أحدثت قلبا جذريا لمفاهيم كانت سائدة في الفكر الفلسفي وبصورة خاصة ما تعلق منها بالأخلاق.
> « ولادة التراجيديا » (1872) أول كتاب له ضمنه أهم محاور اهتماماته الفلسفية، إذ يتناول التراجيديا
> الإغريقية ليؤكد مجد الإغريق لأنهم واجهوا مآسي الحياة و لم يهربوا منها بإنكار إرادتهم مثلما
> فعل « بوذا ». ويتناول في كتابه « المعرفة المرحة » (1882) مسائل تتصل بهدف الحياة والعلم، ومعنى الخلق
> الفني، وأصل المنطق، كما يعرض تصورا لحياة جديدة أكثر نبلا و قوة. ويعد كتابه « هكذا حدث زراديشت »
> (1885) الأكثر شهرة وأبلغ ما كتب في مجال الفلسفة والذي تميز فيه نيتشه بأسلوب كتابة استثنائي ويتعلــق
> الكتاب بالنبــي « زراديشت » [لسان حال نيتشه] يتوجه بالخطاب إلى الناس لتنويرهم وإنقاذهم، والناس ليسوا
> سوى معاصري نيتشه الضعفاء، الذين لا طموح لهم، والذين يخشون مغامرات العقل الكبرى، وقد عُد كتاب
> « ما وراء الخير والشر » (1886) التأسيس النيتشوي لأخلاق جديدة والتي تتجاوز التصورات القديمة للأخلاق
> وللخير والشر، ويتضمن الكتاب نقدا لاذعا للمسيحية التي لا ترى في الأخلاق سوى نفيا للحياة وإعداما لها،
> ويتواصل نظره الأخلاقي في كتابه « جنيالوجيا الأخلاق » (1887) والذي بحث فيه نيتشه عن أصل القيم
> الأخلاقية التي تعلن الزهد في الحياة وتنكر الغرائز والتي جعلت من العبيد أسيادا، ليقدم بذلك جنيالوجيا
> نقدا للدين وللقيم الحضارية السائدة، ويميز في هذا المجال بين ثقافة الأقوياء أو السادة التي ترد إلى
> القوى الفعالة والتي تعبر عن نفسها في إرادة الاقتدار وثقافة العبيد والضعفاء التي ترد إلى القوى
> الإرتكاسية وتعبر عن نفسها في إرادة الانحطاط والعدم، ليبشر بالإنسان الأسمى، المقابل الأرضي للإله.

**المهام (verbatim, 5 puces)** :
- ما دلالة التفكير عند نيتشه؟ و لم لا تحتاجه الحياة حتّى تكون ممكنة؟
- فيم يحرج موقف نيتشه الفيلسوف الحديث؟
- من يتبع الآخر: الوعي أم التواصل؟ أعلّل جوابي استنادا على حجج الكاتب.
- أيّ تعريف للوعي ينتهي إليه الكاتب؟
- في ضوء أطروحة الكاتب وحجاجه: أيّة منزلة بقيت للوعي في تحديد الإنيّة؟

**Encadré-citation (p.54, à gauche des مهامّ, sous une reproduction picturale — grappe de visages
d'époque baroque)** :
> " فالوعي ليس إجمالا إلاّ شبكة من الروابط بين النّاس ".
> — **نيتشه**

---

###### سند 20 — لويس ألتوسير — « الاعتراف الإيديولوجي » — p.55-56

- **Auteur tel qu'imprimé** : ligne de source **لويس ألتوسير** ; ligne latine
  **`Louis ALTHUSSER`** ; notice **الكاتب** : **ألتوسير: (1918 – 1990)**. Encadré signé **ألتوسير**.
- **Titre du سند** : **الاعتراف الإيديولوجي**
- **Source imprimée** : **لويس ألتوسير، الإيديولوجيا وأجهزة الدولة الإيديولوجيّة** —
  `Louis ALTHUSSER; Idéologie et appareils idéologiques de l'Etat, in Position, Editions sociales, pp. 111 - 113`
- **Illustration** : portrait photographique d'Althusser (vignette dans le texte, p.55).

**التمهيد (verbatim)** :
> نعيش تجربتنا مع الآخر بعفويّة من خلال ممارسة يوميّة سمتها العفويّة دون أن ننتبه إلى حقيقة هذه
> الممارسة وطبيعة الوعي الذي يتشكّل بفعلها، وحين نسائلها نكتشف أن ما خفي كان أعظم

*(la phrase du تمهيد est imprimée **sans point final** ; constaté, non corrigé.)*

**Thèse (reformulée)** : nos gestes quotidiens les plus banals — répondre « c'est moi ! » derrière
une porte fermée, saluer une connaissance dans la rue en lui serrant la main — sont des
**rituels matériels de la reconnaissance idéologique**. Par eux, « vous » et « moi » sommes
**toujours-déjà** des sujets : des sujets au plein sens du mot, individuels, réels, distincts et
irremplaçables. Écrire et lire ce texte relève du même rituel. Mais cette reconnaissance
ininterrompue **ne nous donne que la « conscience » de notre pratique perpétuelle des rituels de la
reconnaissance idéologique — elle ne nous en donne pas la connaissance (la science) du mécanisme**.

**هوامش** : **aucun encadré de notes** pour ce سند (ni p.55 ni p.56).

**الكاتب (notice, commencée p.55 et terminée p.56 — verbatim)** :
> **ألتوسير: (1918 – 1990)** — ولد بالجزائر، نال التبريز في الفلسفة سنة 1948. اشتغل بالتدريس إلى حدود
> سنة1980. قضى سنواته العشر الأخيرة بمصحة نفسية حيث توفي سنة 1990. انتمى **ألتوسير** إلى الحزب الشيوعي
> الفرنسي سنة 1948 وعُدَّ قارئا مجددا للماركسية في كتابه من « أجل ماركس » (1960 – 1965) وكتابه
> « قــراءة رأس المــال » (1965) – أهم مؤلَّفاته على الصعيد السياسي والفلسفي –. ركز في أعماله هذه لا على
> الدور الذي على الفلسفة أن تضطلـع به فقط، وإنما على بيــان أن الفلسفة الماركسيــة، وبصورة خاصة نظرية
> التاريخ، تحتاج إلى إعادة تشكيل في قسم كبير منها، حيث يتوسل ألتوسير مفاهيم البنية والسببية البنيوية،
> إذ توجد في نظره بنية خاصة للعلم، والمجتمع في كليته يتكون من بنى متعددة وجب إدراك العلاقات القائمة
> بينها. كما نشر **ألتوسير** مؤلفين لتوضيح كتاباته « الفلسفة وفلسفة العلماء العفوية » و « عناصر نقد ذاتي »
> (1974) الأول استعاد دروسا قدمها سنة 1967 وفيها يعرّف الفلسفة في مقابل العلم وعمل على بيان كيف أن
> ممارسة العلماء تتضمن فلسفة عفوية. أما في كتابه الثاني فقد قدم قراءة نقدية لأطروحات كتابيه من أجل
> ماركس و قراءة رأس المال. كما جمع ألتوسير مختلف مقالاته في مؤلف بعنوان « مواقف » (1976).

**المهام (verbatim, 4 puces, p.56)** :
- " الاعتراف ": وضعيّة نعيشها، أيّ معنى لها في علاقة بالآخر وما هيّ تجلياتها من خلال الأمثلة الواردة
  في النصّ؟
- ما دلالة ممارستنا لطقوس الاعتراف الإيديولوجي؟ وهل تمنحنا هذه الممارسة وعيا بذواتنا؟
- ما الفارق بين أن نحقّق الوعي بالاعتراف الإيديولوجي وبين أن نتمكّن من معرفة آليّة هذا الاعتراف؟
- فيم يغيّر هذا الموقف لألتوسير من فكرة الغيريّة التي تكوّنت لديّ؟

**Encadré-citation (p.56, à côté d'une photographie en fausses couleurs — deux mains qui se serrent)** :
> المصافحة " ممارسة طقوسيّة ماديّة تعبّر عن الاعتراف الإيديولوجي في الحياة اليوميّة ".
> — **ألتوسير**

⚠️ Cet encadré est le seul du chapitre à **commencer hors guillemets** (`المصافحة`, le mot du
manuel) avant d'ouvrir la citation d'Althusser.

---

###### سند 21 — م. فوكو / ميشال فوكو — « الجسد في لعبة السلطة » — p.57-58

- **Auteur tel qu'imprimé** : ligne de source **م. فوكو** ; ligne latine **`M. FOUCAULT`** ;
  notice **الكاتب** : **ميشال فوكو: ( 1926 – 1984 )**.
- **Titre du سند** : **الجسد في لعبة السلطة**
- **Source imprimée** : **م. فوكو، المراقبة والمعاقبة** —
  `M. FOUCAULT, Surveiller et punir, éd. Gallimard 1975, pp. 32 - 33`
- **Illustration** : portrait photographique de Foucault (vignette dans le texte, p.57).

**التمهيد (verbatim)** :
> قد يتبادر إلى الأذهان أنّ عصر إقصاء الجسد وتهميشه قد ولّى، فصورة الجسد أو الجسد بما هو صورة تملأ
> المكان، ولكنّها صورة بقدر ما توحي بالاحتفاء به وإنعاشه تضمر استبعاده واستعباده سبيلا للسيطرة على
> الإنسان وتدجينه.

**Thèse (reformulée)** : l'histoire de la micro-physique du pouvoir pénal est une **généalogie de
l'âme moderne**. ⚠️ **Il ne faut PAS dire que l'âme est une illusion ou un effet idéologique** :
elle est **réellement existante**, produite en permanence autour du corps, à sa surface et en lui,
par le fonctionnement d'un pouvoir exercé sur ceux qu'on punit — et plus largement sur ceux qu'on
surveille, dresse et corrige : fous, enfants, écoliers, colonisés, et tous ceux qu'on fixe à un
appareil de production et qu'on surveille leur vie durant. Cette âme **ne naît pas** pécheresse et
punissable, comme celle de la théologie chrétienne : elle naît **des procédures mêmes** du châtiment,
de la surveillance, de la punition et de la contrainte. Elle **n'est pas une substance** : elle est
l'élément où s'articulent des effets de pouvoir et la référence d'un savoir — et ce savoir, à son
tour, conduit et soutient les effets de ce pouvoir. Sur cette base ont été construits les concepts
de `نفس`, `ذاتية`, `شخصيّة`, `وعي`, puis des techniques et des discours scientifiques, et enfin les
revendications de l'humanisme moral. ⚠️ **Erreur à ne pas commettre** : on n'a **pas** remplacé
l'âme, illusion des théologiens, par un homme réel. **L'homme dont on nous parle et qu'on nous
invite à libérer est lui-même l'effet d'un assujettissement bien plus profond.** Une « âme »
l'habite et le pousse à l'existence, elle-même pièce de la maîtrise que le pouvoir exerce sur le
corps. L'âme est le **produit et l'instrument d'une anatomie politique** : **l'âme est la prison du
corps.**

**الهامشان (verbatim, p.58 — 2 notes, appelées `(1)` et `(2)` dans le texte p.57)** :
> 1– **الجينيالوجيا**: أو النِسَابيّة وهي البحث في قيمة الأصل وأصل القيمة، وهو منهج اعتمده نيتشه في نقده
> للفلسفات الميتافيزيقيّة.
> 2– **اللاهوتيون**: إشارة إلى أصحاب الفكر الديني في نظرهم إلى الإنسان بما هو نفس وتحديدهم للنفس بما
> هي روح إلهي.

**الكاتب (notice, p.58)** :
> **ميشال فوكو: ( 1926 – 1984 )** — فيلسوف فرنسي، مارس تفكيرا فلسفيا قريبا من الابستمولوجيا لكن
> تحكمه خلفية تاريخيّة تعنى بتاريخ الفكر وتكونه. تكشف كتاباته الأولى: « تاريخ الجنون في العصر
> الكلاسيكي » (1961)، « ولادة المصحة » (1963)، « الكلمات والأشياء » (1966)، « حفريات المعرفة » (1969)،
> عن انشغال ثابت: تكوّن العلوم الإنسانية والدور الذي تقوم به الممارسات السلطوية. اعتبر كتاب
> « الكلمات والأشياء » الكتاب الذي منح فوكو الشهرة، فعلاوة على ما تضمنه من نقد لمفهوم الإنسان وصورته
> في العلوم الإنسانية، تمّيز بالتطرق إلى تاريخ الأفكار الذي يسميه **فوكو بالأركيولوجيا**. والأرضية التي
> تتجذّر فيها امكانات التفكير هذه يسميها **فوكو « الابستيمي »** والذي يصفها بعرض الضوابط المفهومية
> المستخدمة في كل خطاب. ولعل قيمة هذه المعالجة تكمن في الاهتمام بشبكة العلاقات التي تشكل الحياة
> الإنسانية، فما يبيّنه **فوكو** في كتاباته هو انبثاث السلطة اللامتناهي في المجتمعات المعاصرة، وولادة
> الانضباط الذي يحدد الأفعال ويفصلها وفي نفس الوقت يولّد المعرفة (« المراقبة والمعاقبة »، 1975). أمّا
> كتابه « إرادة المعرفة » (1976) فيمثل الجزء الأول من مؤلف ضخم لتاريخ الجنسانية، والذي حال موته دون
> إتمامه، ويتضمن أطروحة جدّ مجددة مفادها أنّ الغرب لم يكبت الجنسانية فحسب وإنما جعل منها موضوع علم،
> لينتهي بوضع التحليل النفسي ضمن منطوق إرادة المعرفة وإرادة المراقبة ما دام منطوق الجنسانيّة لا يتمّ
> التفكير فيه إلا انطلاقا من تقنيات السلطة. هكذا يبدو أن **فوكو** يحتل في الفلسفة المعاصرة منزلة جد
> هامة، إذ يعد أول مفكر منح للفلسفة مواضيع جديدة.

**المهام (verbatim, 5 puces, p.58)** :
- أستحضر تصوّري لدلالة السلطة وأمتحنه من خلال النظر في مفهوم السلطة كما يرد في النصّ.
- أتبيّن دلالة النفس كما وردت في النص وأنتبه إلى طرافة مقاربة الكاتب.
- أحدّد علاقة التلازم بين مفهوم النفس وما يسمّيه الكاتب " تكنولوجيا السلطة على الجسد ".
- أتبيّن العلاقة التي يقيمها الكاتب بين المعرفة والسلطة وأستحضر أمثلة من معيشي توضّح هذه العلاقة.
- قيل " الجسد قبر النفس " ويقول فوكو " النفس سجن الجسد ": أقارن بين الموقفين وأكشف عن ضمنيات
  كليهما. ماذا أستخلص؟

**Encadré-citation** : **AUCUN**. La p.58 se termine sur les مهامّ ; ce سند est **le premier du
chapitre sans encadré-citation**. Constaté, pas déduit.

---

###### سند 22 — ج. بودريار / جون بودريار — « استثمار الجسد » — p.59-60

> ⭐ **سند de référence** : deux notices d'auteur du **مبحث 3.2** renvoient explicitement ici
> (« راجع التعريف … في السند عدد 22 »). **La notice ci-dessous est celle qu'elles appellent.**

- **Auteur tel qu'imprimé** : ligne de source **ج. بودريار** ; ligne latine **`Jean  BAUDRILLARD`**
  (double espace imprimé) ; notice **الكاتب** : **جون بودريار: (1929 – 2007 )**. Encadré signé
  **ج. بودريار**.
  ⚠️ Trois graphies dans le même سند : `ج. بودريار` / `جون بودريار` / `Jean BAUDRILLARD`.
  La forme de la notice est **جون** (et non `جان`).
- **Titre du سند** : **استثمار الجسد**
- **Source imprimée** : **ج. بودريار، مجتمع الاستهلاك** —
  `Jean  BAUDRILLARD, Société de consommation,Folilo - Essais  1975, p.201`
  ⚠️ **`Folilo`** [sic] — vérifié à 600 dpi ; il s'agit manifestement de la collection **Folio**,
  mais le manuel imprime bien `Folilo`. Anomalie **réelle** de la source, pas une erreur de lecture.
- **Illustration** : portrait photographique de Baudrillard (vignette dans le texte, p.59).

**التمهيد (verbatim)** :
> يمثّل الجسد اليوم المشهد الأكثر حضورا في ثقافة الإشهار والاستهلاك، ممّا يؤشّر على ضرب من الاعتراف به
> و كأنّه غدا جزءا من الأنظمة الرمزيّة لا من جهة كونه فضاء حريّة وحقل معنى بل من جهة كونه قلعة استعباد
> وفضاء استثمار .

**Thèse (reformulée)** : parmi toutes les armes de la consommation, la plus belle, la plus précieuse
et la plus éclatante — celle qui les résume toutes — c'est **le corps**. Sa « redécouverte », après
des siècles de puritanisme, sous le signe de la libération physique et sexuelle, sa présence
massive dans la publicité et la mode, le culte de l'hygiène, de la diététique et de la thérapeutique,
l'obsession de la jeunesse, de l'élégance, de la virilité et de la féminité, les soins, les régimes
et les pratiques sacrificielles qui s'y attachent, le mythe du **plaisir** (`اللذة`) qui les enveloppe :
tout atteste que le corps est devenu **objet de salut** et qu'il **a pris la place de l'âme** dans sa
fonction morale et idéologique. La publicité nous rappelle sans cesse, à la manière des cantiques
religieux, que **nous ne possédons qu'un corps et qu'il nous faut le sauver**. Pendant des siècles on
s'est acharné à persuader les hommes qu'ils **n'avaient pas** de corps — sans jamais y parvenir
vraiment — ; aujourd'hui on s'acharne, avec méthode, à les persuader **de** leur corps. Mais
l'évidence du corps **n'en est pas une** : le statut du corps est **un fait de culture**, et le mode
d'organisation du rapport au corps reflète, dans toute culture, le mode d'organisation du rapport
aux choses et aux rapports sociaux — dans une société capitaliste, le statut de la propriété privée
s'applique aussi au corps. Dans le contexte traditionnel, on **ne trouve pas** chez le paysan
d'investissement **narcissique** de son corps ni de perception spectaculaire de celui-ci, mais une
vision **instrumentale / magique** liée au travail et au rapport à la nature. Ce que Baudrillard veut
établir : les structures actuelles de production/consommation induisent chez le sujet une pratique
**double et disjointe (mais très liée)** de son propre corps — le corps comme **capital** et le corps
comme **fétiche** (ou objet de consommation). Dans les deux cas, **loin d'être exclu ou oublié, le
corps est investi** — aux deux sens du mot `الاستثمار` : **économique et psychique**.

**الهامش (verbatim, p.60 — UNE seule note, appelée `(1)` dans le texte p.59)** :
> 1– **النرجسيّة**: لفظ مشتق من نرجس وهو عند اليونان اسم لفتى جميل الصّورة أعجب بجمال صورته المنعكسة
> على صفحة الماء فعشقها وأراد معانقتها فغرق. وتُحمل النرجسيّة في أيّامنا على من يغرق في عشق ذاته.
> والمقصود في النص أنّ علاقة القروي بجسده ليست علاقة إعجاب وتعشّق بل ينظر إلى جسده على أنّه مجرّد أداة
> تصله بالطبيعة أثناء عمله.

**الكاتب (notice, p.60 — transcription intégrale, vérifiée à 600 dpi)** :
> **جون بودريار: (1929 – 2007 )** — عالم اجتماع فرنسي اكتست كتاباته طابعا فلسفيّا بارزا حاول فيها
> تشريح المجتمعات المعاصرة بما هي مجتمعات استهلاكيّة. في « نظام الأشياء » (1968) تناول بالدراسة علاقة
> الإنسان بالأشياء مبيّنا أن للشيء بنية خاصّة لوظيفتها دلالة مستقلّة عن استعمالنا للشيء نفسه، ويتساءل
> في سياق ذلك كيف يمكن لنظام منسجم تكنولوجيّا أن يفقد هذا الانسجام في الواقع؟ واصل تأملاته هذه في
> « من أجل نقد الاقتصاد السياسي للعلامة » (1972) ليبني نظريّة في الشيء - العلامة، نقد من خلالها منطق
> الطبقة وبرهن على تكوّن إيديولوجيا الحاجيات وما يتّصل بها من تعظيم يبلغ حد التقديس، وهي إيديولوجيا
> بصدد التوسّع حتّى أنّها تشمل الآثار الفنيّة. وفي « مجتمع الاستهلاك » (1975) تحدّث عن آليات الترغيب في
> الاستهلاك ويخصّ الجسد بالمشهد الأكثر إبهارا من كل الوسائل التي يعتمدها الترويج للاستهلاك. وانتهى في
> « التبادل الرمزي والموت » (1976) إلى التأكيد أنه لم يعد هنالك من تبادل رمزي بين التشكيلات
> الاجتماعيّة الراهنة إلاّ في شكله التسلّطي.

⚠️ Cette notice **ne comporte aucun renvoi sortant** : c'est une notice **autonome et complète**.
Les quatre ouvrages qu'elle nomme, dans l'ordre imprimé : `نظام الأشياء` (1968) ·
`من أجل نقد الاقتصاد السياسي للعلامة` (1972) · `مجتمع الاستهلاك` (1975) · `التبادل الرمزي والموت` (1976).

**المهام (verbatim, 5 puces, p.60)** :
- ما الذي يجعل من الجسد أثمن أسلحة الاستهلاك ؟ أذكر أمثلة على ذلك.
- ما الذي يعنيه الكاتب بأن " منزلة الجسد هي أنّه حدث ثقافة "؟
- ما الفرق بين الاستثمار النرجسي والاستثمار الأداتي للجسد؟
- هل في استثمار الجسد في الدعاية للاستهلاك علامة تحرر أو استلاب؟
- أرصد تأثير ثقافة الإشهار على رؤيتي لذاتي. أحرّر فقرة في الغرض.

**Encadré-citation (p.60, à côté d'une photographie publicitaire — femme en maillot appuyée sur une
berline noire, palmiers et coucher de soleil)** :
> " توجد دعاية تذكرنا بلا انقطاع، على طريقة التراتيل الدينيّة، بأنّنا لا نمتلك إلاّ جسدا وعلينا إنقاذه ".
> — **ج. بودريار**

⚠️ **Mise en page particulière** : la p.60 porte **deux encadrés côte à côte**, `المهام` **à droite**
et `الهامش` **à gauche** (au singulier — une seule note). C'est la seule page de la tranche où les
deux blocs sont ainsi juxtaposés en colonnes.

---

###### سند 23 — ميشال فوكو — « مساءلة الكوجيتو » — p.61-62

- **Auteur tel qu'imprimé** : ligne de source **ميشال فوكو** ; ligne latine **`Michel FOUCAULT`**.
  Encadré signé **فوكو**.
- **Titre du سند** : **مساءلة الكوجيتو**
- **Source imprimée** (trois lignes) :
  **ميشال فوكو، الكلمات والاشياء، ترجمة فريق بإدارة مطاع صفدي، مركز الإنماء القومي، 1989–1990، ص 268 — 2 69 (مراجعة لجنة التأليف )**
  `Michel FOUCAULT, Les mots et les choses, Gallimard, 1966, pp 335 -336`
  ⚠️ Deux anomalies **réelles**, vérifiées à 600 dpi : le titre arabe est imprimé ici
  **`الكلمات والاشياء`** (sans hamza) alors que la notice p.58 imprime `الكلمات والأشياء` ; et la
  pagination arabe est composée **`ص 268 — 2 69`** — espace parasite à l'intérieur de `269` [sic].
  Comme au سند 19, la traduction est déclarée **revue par la commission de rédaction**.
- **Illustration** : le **même** portrait photographique de Foucault qu'au سند 21 (p.57), réemployé.

**التمهيد (verbatim)** :
> لعلّ أهميّة تجربة الشك الديكارتيّة لا تكمن فيما توصّلت إليه من نتائج وأهمّها الكوجيتو فقط، وإنّما كذلك
> في مدّ الفكر الفلسفي بآليّة للتظنّن على كل ما يقدّم كبداهة، فإذا بالشكّ يغزو الحصن الذي لم يطله الشكّ
> الديكارتي لُينقَل الشك في الأشياء إلى الشكّ في الذات نفسها وليستحيل ما كان واضحا وما عُدّ يقينا
> مستشكلا يستوجب النظر والنقد والمساءلة.

**Thèse (reformulée)** : le « je pense » **ne conduit pas** à l'évidence du « je suis ». Dès que
l'« il pense » (`أنا أفكّر`) surgit dans la profondeur — quasi présent, mais mû sur le mode d'une
somnolence trouble —, il devient **impossible** de le faire suivre de « donc je suis ». Foucault peut
dire qu'il est ce langage qu'il parle, où sa pensée se glisse jusqu'à y trouver tout le système de
ses possibilités propres — mais il **n'y est que sous le poids de sédimentations** qu'il ne pourra
jamais rassembler entièrement ; qu'il est ce travail que ses mains accomplissent mais qui lui
échappe, non seulement une fois achevé, mais **avant même d'être commencé** ; qu'il est cette vie
qu'il sent en lui, mais qui l'engloutit dans le temps profond qu'elle traîne, le hisse un instant à
son sommet et l'y noie du même mouvement dans le temps imminent qui annonce sa mort. Il peut dire
tout cela, et **il n'est aucune de ces choses également**. **Le cogito ne mène donc pas à
l'affirmation de l'être ; il ouvre sur une série d'interrogations qui portent sur la question de
l'être** : que dois-je être, moi qui pense et qui suis ma pensée, pour être ce que je ne pense pas,
pour que ma pensée soit ce que je ne suis pas ? Cet être qui scintille — ou plutôt qui luit par
intermittence — dans l'ouverture du cogito **n'est pas donné avant lui ni entièrement à travers lui**.
Reste alors la question de la relation et de la difficile appartenance de l'être et de la pensée, et
celle de l'essence de l'homme — cet être qu'on décrit si aisément comme « ayant une pensée », et qui
est peut-être seul à posséder ceci : **être en relation essentielle et ineffaçable avec le
non-pensé** (`اللامفكّر`). Ainsi naît une forme de pensée **entièrement distante du cogito cartésien
et de l'analyse kantienne**, où l'être de l'homme devient **pour la première fois** objet de la
question, selon la dimension qui tourne la pensée vers le non-pensé et l'articule sur lui.

**الهامش (verbatim, p.62 — UNE seule note, appelée `(1)` dans le texte p.61)** :
> 1– **التحليل الكانطي**: يؤكّد كانط على أنّ الأنا يمكنه أن يعرف فيما يفكّر، كيف يفكّر ولكنه لا يستطيع
> أن يعرف ماهيّة ذاته بذاته إذ أنّ الذات في تصوّره لا تدرك إلاّ من خلال تمثّلاتها.

**الكاتب** — ⚠️ **ce n'est pas une notice mais un RENVOI**, imprimé p.61 sous la référence, verbatim :
> **فوكو: أنظر التعريف الوارد بالسند 21**

(Renvoi **interne** au chapitre : il pointe vers le سند 21 — *الجسد في لعبة السلطة*, p.57-58 — dont la
notice **ميشال فوكو: ( 1926 – 1984 )** est transcrite plus haut dans ce même fragment.)

**المهام (verbatim, 6 puces, p.62)** :
- أستحضر الكوجيتو الديكارتي وأتبيّن العلاقة التي يقيمها بين الفكر والوجود.
- لماذا يعتبر الكاتب أن الـ " أنا أفكّر " " لا يمكن أن يُتبعَ بـ " أنا موجود "؟
- إذا كان الكوجيتو لا يؤدّى بداهة إلى تأكيد الكوجيتو فإلام يؤدّي حسب الكاتب؟
- ماذا يعني القول بأنّ الكوجيتو يجعل الفكر يتّجه إلى اللامفكّر فيه ويتمفصل عليه؟
- هل يمثّل التشكيك في علاقة الفكر بالوجود تشكيكا في الذاتيّة؟
- أستخلص ملامح الإنسان كما يرسمها فوكو.

⚠️ La 3ᵉ puce est imprimée **`إذا كان الكوجيتو لا يؤدّى بداهة إلى تأكيد الكوجيتو`** — le mot
`الكوجيتو` apparaît **deux fois** dans la même question là où le texte source parle de l'aboutissement
à **l'être** (`تأكيد الوجود`). Anomalie de la source : **constatée, non corrigée**.

**Encadré-citation (p.62, à côté d'une illustration — silhouette noire d'un profil humain sur ciel
étoilé, avec un « penseur » filaire jaune assis dedans et un globe terrestre)** :
> " ما يجب أن أكون، أنا الذي يفكّر وأنا الذي أكون فكري، كي أكون ما لا أفكّر وكي يكون فكري ما لست أنا ؟ "
> — **فوكو**

---

###### سند 24 — فرويد — « بنية الجهاز النفسي » — p.63-64

> ⭐ **سند de référence** : deux notices d'auteur du **مبحث 3.2** renvoient explicitement ici
> (« راجع التعريف … في السند عدد 24 »). **La notice ci-dessous est celle qu'elles appellent.**

- **Auteur tel qu'imprimé** : ligne de source **فرويد** ; ligne latine **`Sigmund FREUD`** ;
  notice **الكاتب** : **فرويد: ( 1856 – 1939 )**.
  ⚠️ Le manuel **n'imprime jamais le prénom en arabe** pour cet auteur : ni `سيغموند` ni
  `سيجموند` — toujours `فرويد` seul. Le prénom n'existe que dans la ligne latine.
- **Titre du سند** : **بنية الجهاز النفسي**
- **Source imprimée** : **فرويد، محاضرات جديدة في التحليل النفسي** —
  `Sigmund FREUD, Nouvelles conférences d'introduction à la psychanalyse, éd. Gallimard, 1984, pp 104 - 107`
- **Illustration** : portrait peint de Freud (vignette dans le texte, p.63).
- **Coupures imprimées** : le texte porte **trois `(...)`** marquant des passages omis (fin du §4,
  fin du §5, fin du §6), plus un `(...)` d'ouverture implicite. Ce سند est donc explicitement
  **un montage d'extraits**.

**التمهيد (verbatim)** :
> تعزّز التظنّن على الوعي ببيان لا إجرائيته بشأن أفعال ظلّت ، تحت وَطْأَتِهِ مستعصية على الفهم و ظلّ معها
> الإنسان لغزا يتمنّع عن الانكشاف ما لم نعترف بما يسعى الوعي إلى إخفائه و التستّر عليه اعترافا يشي
> بتحوّل المخفي إلى أساس والظاهر إلى عارض.

**Thèse (reformulée)** : le **moi** (`الأنا`) est **une partie du ça** (`الهو`) modifiée par le
voisinage du monde extérieur et par son influence, rendue apte à recevoir les excitations et à s'en
protéger — comme la couche corticale qui entoure une parcelle de matière vivante. Sa fonction est de
**représenter le monde extérieur auprès du ça**, ce qui est vital pour celui-ci : sans le moi, le ça
se briserait sur le roc de cette force extérieure supérieure, emporté par sa poussée aveugle vers la
satisfaction pulsionnelle. Le moi doit observer le monde extérieur, en former une image fidèle, la
conserver dans ses souvenirs, écarter par l'épreuve de la réalité ce qui vient de sources internes ;
il place l'action sous son contrôle mais **interpose entre le désir et l'acte un délai de réflexion**.
Il **détrône ainsi le principe de plaisir**, qui régnait sans partage sur les processus du ça, et lui
substitue **le principe de réalité**, plus apte à garantir la sécurité et le succès. Grâce au système
perceptif, le moi entretient avec le temps un rapport difficile à décrire : c'est bien du
fonctionnement de ce système que naît l'idée du temps. Mais **ce qui distingue surtout le moi du ça,
c'est sa tendance à la synthèse — à unifier et à totaliser ses processus —, dont le ça est
totalement incapable**. Le moi croît de la perception des pulsions jusqu'à leur maîtrise, mais **il
n'y parvient qu'en réussissant à intégrer le représentant de la pulsion dans un ensemble plus large** :
en langage courant, le moi représente dans la vie psychique la raison et la sagesse, le ça les
passions échappées à leur bride. **Analogie du cavalier** : le cheval fournit l'énergie du mouvement,
le cavalier fixe le but et y dirige l'animal puissant — mais leur rapport **n'est pas toujours
idéal**, car le plus souvent le cavalier se voit contraint d'aller là où sa monture veut le mener.
Enfin : on dit que nul ne peut servir deux maîtres à la fois — or le moi en a **trois**, dont les
exigences sont toujours contradictoires et souvent inconciliables : **le monde extérieur, le surmoi
(`الأنا الأعلى`) et le ça**.

**هوامش** : **aucun encadré de notes** pour ce سند (ni p.63 ni p.64).

**الكاتب (notice, p.64 — transcription intégrale, vérifiée à 600 dpi)** :
> **فرويد: ( 1856 – 1939 )** — طبيب نفسي نمساوي ومؤسس التحليل النفسي، عاش في فيينّا منذ سنّه الرابعة
> و لم يتركها إلا مع الاحتلال النازي حين هاجر إلى لندن حيث توفي. درس الطب واختص في أمراض الجهاز
> العصبي. بدأ حياته العملية في مخبر كباحث في علم أنسجة الجهاز العصبي، ولكن حاجته للمال ألزمته ترك
> المخبر للقيام بفحوص طبية حيث التقى لأول مرة مع من يُعدُّون مرضى عقليين. قام بتربصات في فرنسا مكنته
> شيئا فشيئا من تلمس سبل جديدة لمعالجة المرضى العقليين والتي ستكون سببا في ظهور التحليل النفسي
> ( في حدود سن الأربعين ). قدّم تصوّرا جديدا للإنسان باكتشافه للاّوعي ودور العامل الجنسي في تكوّن
> الشخصيّة أثار من حوله ضجّة كبيرة. كان انتاجه غزيرا وكتب عدة مؤلفات، نذكر منها:
> « مخطط من أجل علم نفس علمي » (1895، ظل غير مكتمل)؛ « بحث في الهيستيريا » ( بالتعاون مع عالم الأعصاب
> جوزيف بروير 1895 )؛ « تفسير الأحلام » (1900)؛ « الحلم وتفسيره » (1901)؛ « الأمراض النفسية في الحياة
> اليومية » (1901)، « ثلاث مقالات حول النظرية الجنسانية » (1905)؛ « خمسة دروس في التحليل النفسي »
> (1909)؛ « الطوطم والحرام » (1913)؛ « مقدمة إلى التحليل النفسي » ( 1917)؛ « مستقبل وهم » (1927)؛
> « قلق في الحضارة » (1929)؛ « موسى والتوحيد » (1939).

**Renvoi imprimé sous la notice (p.64, en bleu — verbatim)** :
> لمزيد التعمّق انظر نافذة دعائم التفكير؛ سياقات فكريّة: التحليل النفسي.

⚠️ Ce renvoi est libellé **`نافذة دعائم التفكير`** ici, alors que le renvoi analogue du سند 18 (p.51)
écrit **`نافذة دعائم للتفكير`** (avec `للـ`). Les deux formes coexistent : **constaté, non uniformisé.**

**المهام (verbatim, 8 puces, p.64 — le سند le plus questionné de la tranche)** :
- أتتبع النص وأحدد مكوّنات الجهاز النفسي.
- أتبيّن كيفيات تكوّن منظمات الجهاز النفسي مميّزا بين ما هو معطى وما هو مكتسب؟
- أيّة علاقة يقيمها الكاتب بين الأنا والزمن؟
- أعتمد المماثلة التي استخدمها الكاتب في النص لأتبيّن طبيعة العلاقة بين الهو والأنا.
- ماذا يترتب على نجاح الأنا أو إخفاقه في مهمّته؟
- كيف يمكّن هذا التصوّر للحياة النفسية من فهم بعض مظاهر السلوك الإنساني التي بقيت مستعصية على الفهم؟
- أستخلص مفهوم اللاوعي وأتبيّن منزلته؟ أحرّر فقرة في الغرض.
- لم مثّل اكتشاف اللاوعي حرجا لفلسفات الوعي؟

**Encadré (p.63-64)** : ⚠️ **il n'y a PAS d'encadré-citation** pour ce سند. À sa place, la p.64 porte
un **dispositif d'écriture** : une photographie en fausses couleurs (profil féminin dédoublé — une
silhouette sombre de profil devant un visage lumineux) surmontant un **cadre rose à quatre lignes de
pointillés à remplir par l'élève**, relié par une **flèche rouge** à une consigne encadrée en rouge :
> أعلّق على الصورة مستأنسا بالنصّ.

C'est le **seul dispositif de ce type** rencontré dans la tranche p.47-74.

---

###### سند 25 — فرويد — « سيادة الأنا ؟ » — p.65-66

- **Auteur tel qu'imprimé** : ligne de source **فرويد** ; ligne latine **`FREUD`** (sans prénom).
- **Titre du سند** : **سيادة الأنا ؟**
- **Source imprimée** :
  **فرويد. موسى والتوحيد، ترجمة جورج طرابيشي، دار الطليعة. بيروت. الطبعة الخامسة 2004. ص 161 – 261. (مع مراجعة اللجنة).**
  `FREUD; Moïse et le Monothéisme, éd,Gallimard`
  ⚠️ **`ص 161 – 261`** — vérifié à 600 dpi : le manuel imprime bien **261**, soit une plage de 100 pages
  pour un extrait d'une page. Anomalie **réelle** de la source (très probablement pour `161 – 162`) :
  **constatée, non corrigée.** Noter aussi `éd,Gallimard` (virgule au lieu du point) et l'absence de
  toute date pour l'édition française.
- **Illustration** : portrait photographique de Freud **différent** de celui du سند 24 (ici, Freud âgé,
  de trois-quarts, en noir et blanc).
- **Ouverture** : le texte s'ouvre sur un **guillemet ouvrant** (`"حين يحاول…`) et se referme
  p.66 — c'est une citation continue, sans coupure `(...)`.

**التمهيد (verbatim)** :
> من النفس بما هي جوهر بسيط إلى الجهاز النفسي بما هو بنية ديناميكيّة: صور تتهاوى وأخرى تنبعث ترجّ
> يقيننا بذواتنا وتحرج ما خلناه علامة حريّة ومؤشّر إرادة، وتُحَذّرُ من ضياع سيادة كانت لنا على أفعالنا لم
> نعد ندري إن كنّا ننسبها إلى أنفسنا على وجه التوهّم أم على وجه التملّك…

**Thèse (reformulée)** : quand le **ça** impose à un être humain une exigence pulsionnelle de nature
**érotique** (`ايروسي`) ou **agressive**, la réponse la plus simple et la plus naturelle du **moi** —
qui dispose des appareils de la pensée et de la motricité — est de la satisfaire par un acte : cette
satisfaction est ressentie comme plaisir, sa non-satisfaction engendre sans nul doute peine, angoisse
et tourment. Le moi peut pourtant **s'abstenir** à cause d'obstacles extérieurs, s'il perçoit que
l'acte l'exposerait à un danger grave. Or ce renoncement à la pulsion, cette soumission au **principe
de réalité**, **n'est en aucun cas source de plaisir** pour l'homme et peut produire une tension
durable, sauf si l'énergie est déchargée en la déplaçant ailleurs. Mais il arrive que le refoulement
porte sur des mobiles **internes** : au cours du développement de l'individu, une part des forces
extérieures inhibitrices est **intériorisée**, et se forme dans le moi une instance qui observe,
surveille et interdit — **le surmoi** (`الأنا الأعلى`). Dès lors, avant de satisfaire les pulsions, le
moi doit compter **non seulement** avec les dangers extérieurs **mais aussi** avec les exigences du
surmoi : les motifs d'abstention se redoublent. Et alors que l'abstention due à des causes
**extérieures** ne produit que de la peine, l'abstention née de causes **internes**, par obéissance au
surmoi, a un **effet économique différent** : à côté de la peine inévitable, elle apporte un gain et
une **satisfaction de substitution** — le moi s'éprouve en extase et en ferveur, il tient son renoncement
à la pulsion sexuelle pour un acte méritoire. Le surmoi est **l'héritier des parents (et des
éducateurs)** qui ont surveillé les actes et les mouvements de l'individu dans ses premières années,
et il en est le représentant ; il maintient le moi sous sa tutelle et exerce sur lui une pression
permanente. Le premier souci du moi reste, comme aux jours de l'enfance, **de ne pas perdre l'amour de
ce maître** : loué, il s'emplit de quiétude ; blâmé et réprimandé, sa conscience morale l'accable.
Quand le moi sacrifie une satisfaction pulsionnelle sur l'autel du surmoi, il en attend en retour
**un surcroît d'amour**, et le sentiment d'avoir mérité cet amour se change en fierté. **Ce sentiment
de sécurité et de contentement n'a pu prendre son caractère narcissique propre que le jour où
l'autorité elle-même est devenue une partie du moi.**

**الهامش (verbatim, p.66 — UNE seule note, appelée `(1)` dans le texte p.65)** :
> 1– **إيروسي**: راجع نافذة دعائم للتفكير، سياقات فكريّة: التحليل النفسي.

⚠️ Cette note est elle-même **un renvoi** vers la نافذة دعائم للتفكير : le manuel ne définit donc
pas `إيروسي` sur place. À résoudre depuis la tranche qui porte les سياقات فكريّة.

**الكاتب** — ⚠️ **ce n'est pas une notice mais un RENVOI**, imprimé p.66, verbatim :
> **راجع التعريف بفرويد في السند عدد 24**

(Renvoi **interne** au chapitre : vers le سند 24 — *بنية الجهاز النفسي*, p.63-64 — dont la notice
**فرويد: ( 1856 – 1939 )** est transcrite plus haut dans ce même fragment.)

**المهام (verbatim, 8 puces, p.66)** :
- أستحضر مكوّنات الجهاز النفسي وأحدد دلالة اللذة متبيّنا دورها في حياتنا النفسيّة.
- هل تقوم الحياة النفسيّة على الانسجام أم على الصّراع؟ أعلّل جوابي.
- يميّز فرويد بين امتناع راجع إلى أسباب خارجيّة وآخر ناشئ عن أسباب داخليّة: أتبيّن الفارق بينهماوأحدد
  أثر كل منهما على الحياة النفسيّة. *(`بينهماوأحدد` collé [sic])*
- ما دلالة الإشباع التعويضي؟ أستحضر أمثلة عن تجليّاته؟
- كيف تولّد التضحيّة بالغرائز مشاعر الاعتزاز والافتخار؟
- أستخلص مهمّة الأنا مبيّنا معنى أن " تصبح السلطة نفسها جزءا من الأنا ".
- هل يفضي هذا التحليل إلى إنكار سيادة الأنا على أفعاله؟
- هل يمكن النظر إلى اللاّوعي بما هو أنا عميق؟

**Encadré (p.66)** : ⚠️ **PAS d'encadré-citation.** À sa place, un **second dispositif d'écriture**
(après celui du سند 24) : une **caricature en noir et blanc signée `ناجي العليّ`** — une pierre
tombale portant l'inscription **« أنا أفكر إذاً أنا موجود »**, un croissant de lune, et un enfant vu
de dos, aux cheveux hérissés, assis parmi les pierres — accompagnée d'une consigne encadrée en rose :
> أتأمّل هذه الصورة وأتأوّلها مستأنسا بما ورد في النص.

C'est **le seul document iconographique signé d'un auteur arabe** de la tranche.

---

###### سند 26 — جيل دولوز — « الآخر بما هو بنية » — p.67-68

- **Auteur tel qu'imprimé** : ligne de source **جيل دولوز** ; ligne latine **`Gilles DELEUZE`** ;
  notice **جيل دولوز (1925 – 1995 )**. Encadré signé **دولوز**.
- **Titre du سند** : **الآخر بما هو بنية**
- **Source imprimée** : **جيل دولوز، منطق المعنى** —
  `Gilles DELEUZE; Logique du sens; éd minuit, 1997, pp 356-357 Gilles`
  ⚠️ **Le prénom `Gilles` est répété en fin de ligne**, après la pagination — vérifié à 600 dpi.
  Anomalie **réelle** de la source (coquille de composition) : **constatée, non corrigée.**
- **Illustration** : portrait photographique de Deleuze (vignette dans le texte, p.67).
- **Coupures imprimées** : le texte porte **quatre `(...)`** — c'est un montage d'extraits.

**التمهيد (verbatim, vérifié à 600 dpi)** :
> قد تقتضي لحظة العبور إلى الآخر تحويله إلى موضوع نُميته في شيئيّته أو إلى ذات هيّ بمثابة الحدّ الذي
> تنهكنا مواجهته حدثا مغايرا نكرهه على الانسحاب عنّا، وكأنّ العالم لا يحتضننا إلاّ لُيُنهينا. لكنّ
> تجربتنا مع الآخر تغيّر وجه حضوره يجعله يعبر إلينا من وراء " ممكن " في تعبيريّة تحوينا حين تحويه.

*(`هيّ` [sic] — shadda parasite sur `هي` ; graphie confirmée à 600 dpi.)*

**Thèse (reformulée)** : on ne peut déterminer ce qu'est autrui qu'en comparant les effets de sa
**présence** originaire aux effets de son **absence**. L'erreur des théories philosophiques est de le
réduire tantôt à un objet particulier dans un champ, tantôt à un autre sujet. Or **autrui n'est ni un
objet de mon champ perceptif, ni un sujet qui me perçoit : il est d'abord la structure du champ
perceptif lui-même**. Quelle est la nature de cette structure ? Celle d'un **monde possible**. Le
visage effrayé est l'expression d'un monde possible effrayant, ou l'expression de quelque chose
d'effrayant dans le monde que je n'ai pas encore perçu. Attention : **le possible n'est pas ici une
simple catégorie désignant quelque chose d'inexistant** — le monde possible exprimé **existe
réellement**, mais **il n'existe pas (dans l'instant présent) hors de celui qui l'exprime**. Le visage
effrayé **ne ressemble pas** à la chose effrayante : il l'enveloppe et la contient comme une chose
autre, sous une forme tordue qui place l'exprimé dans l'exprimant. Et lorsque je saisis à mon tour, à
mon compte, la réalité de ce qu'exprime autrui, **je ne fais rien d'autre qu'expliciter autrui,
développer et incarner le monde possible qui lui correspond**. En somme : **autrui, en tant que
structure, est expression d'un monde possible**, là où le sujet exprimant n'a pas d'existence hors de
ce qui le fait exercer l'acte d'expression.

**الهامش (verbatim, p.68 — UNE seule note, appelée `(1)` dans le texte p.67 ; vérifiée à 600 dpi)** :
> 1– يشير الكاتب هنا إلى ما ذهب إليه ج. ب.، سارتر في " الوجود والعدم " حين جمع بين الحدّين فردّ الآخر
> إلى مجرّد موضوع لنظرتنا في نفس السياق الذي تتحوّل فيه ذاتنا إلى موضوع أمام نظرة الآخر إلينا.

*(Ponctuation imprimée `ج. ب.، سارتر` — la virgule est bien entre les initiales et le nom.)*

**الكاتب (notice, commencée p.67 et terminée p.68 — verbatim)** :
> **جيل دولوز (1925 – 1995 )** — فيلسوف فرنسي، بدأ مسيرته الجامعية سنة 1957 بالسوربون حيث درّس تاريخ
> الفلسفة ثمّ خلف ميشال فوكو بجامعة باريس 8 إلى حدود سنة 1987. اشتهر خاصة بدروسه في الجامعة الشعبية حيث
> يتدافع رسامون وموسيقيون وغيرهم لمتابعة محاضراته. وعلى غرار ميشال فوكو، عُرف دولوز برفضه للفكر الهيغلي
> الذي يمحي الاختلاف اعتمادا على الجدل، إذ في مقابل الجدل الهيغلي ينتصر دولوز في « المعاودة والاختلاف »
> (1968)، وضمن أفق نظر نيتشوي، إلى الإرادة الخلاّقة، إرادة خلق أشكال وقيم أصيلة ووسائط جديدة للخطاب
> الفلسفي، كما يوؤكد وهمية الأنا أو الذات التي اتخذتها الفلسفة المثالية مركزا، وبالقطع مع الموقف
> المركزي لا يظهر سوى حقل غير مسمّى [مجهول/غير معروف] لا أثر فيه للذات وحيث تسود كثرة لا تقبل الاختزال،
> بحيث يمكن للإنسان أن يكون أي شيء ما عدا أن يكون شخصا ولذلك يدعو دولوز إلى تحطيم الأنا وإذابتها لنمكّن
> الإنسان من أن يتكلـم فينا دون هو أو أنا ودون نعوت لتتجلى الكثرة والاختلافات نسيجا كامنا فينا. أمّا في
> « منطق المعنى » (1969) فقد تناول دولوز مشكل اللغة والعبارة والمعنى ملاحظا أن ما يوؤاخذه على بعض
> النظريات الفلسفية هو اختزالها للآخر تارة في موضوع خصوصي وطورا في ذات أخرى، في حين أنّ الآخر أو الغير
> ليس ذاتا مغايرة لذاتي أو موضوعا لذاتي وإنما هو اقتحام لعالم ممكن في حقل محايث بحيث يدفعني الآخر بمجرد
> حضوره على حدس تجارب جديدة، وعلى نقلي إلى المواقع التي يسكنها. وفي كتابه « ضدّ أوديب » (1972)، والذي
> ألفه بمعيّة **فيليكس غاتاري**، يؤكد دولوز على الطابع الإيجابي للرغبة، إذ يرفض اختزال معنى الرغبة في
> الصراع الدائر بين « الأب والأم والطفل » ويعتبر أن اللاوعي ليس مسرحا بل مصنعا أو آلة وظيفتها الأساسية
> هي الإنتاج. أمّا في كتاب « ما الفلسفة ؟ » فقد أكّد فيه كل من دولوز وغاتاري أنّ الفلسفة هي إبداع
> للمفاهيم، وهذا ما يميزها عن العلم والمنطق الذي يشتغل بالدّوال وعن الفن الذي يشتغل بالتمثلات
> والانفعالات فالمفهوم هو ما يمنع الفلسفة من أن تكون مجرّد رأي أو نقاش أو ثرثرة.

⚠️ Cette notice mentionne quatre titres : `المعاودة والاختلاف` (1968) · `منطق المعنى` (1969) ·
`ضدّ أوديب` (1972, avec **فيليكس غاتاري**) · `ما الفلسفة ؟` (**sans date imprimée**).
⚠️ Divergence interne : la ligne de source du سند date `Logique du sens` de **1997** (édition citée),
la notice de **1969** (parution). Les deux chiffres sont imprimés, chacun à sa place.

**المهام (verbatim, 8 puces, p.68)** :
- أحدد معنى النظر إلى الآخر بما هو موضوع.
- أحدد معنى النظر إلى الآخر بما هو ذات أخرى.
- أتبين مكمن الخطأ في النظر إلى الآخر بما هو موضوع أو بما هو ذات.
- بأي معنى يكون الآخر بنية الحقل الإدراكي؟ أستثمر المثال الوارد في النص للإجابة.
- ما دلالة عبارة " العالم الممكن " وكيف تمكّن من معالجة علاقة الذات بالآخر؟
- أحلّل عناصر " التعبير " وأتبيّن قيمتها في علاقة مع العالم الممكن.
- أي تصوّر للغيريّة يمكن استخلاصه من النصّ؟
- هل يمكنني تصور الكاتب من مراجعة طبيعة العلاقة بين الإنية والغيرية؟ أحرر فقرة في الغرض.

**Encadré-citation (p.68, à côté d'une reproduction de tableau — un homme de dos en costume noir et
chapeau melon devant un rideau rouge, doublé de sa propre silhouette découpée en blanc)** :
> " غير أنّ الآخر ليس موضوعا في حقل إدراكي، وليس ذاتا تدركني: إنّه في البدء بنية الحقل الإدراكي ".
> — **دولوز**

---

###### سند 27 — ج. لاكان / جاك لاكان — « في اللاوعي » — p.69-71

⚠️ **Ce سند occupe TROIS pages** (69, 70, 71) : texte + تمهيد + 1ᵉʳ encadré-citation p.69 ; notice
**الكاتب** + الهوامش (3 notes, très longues) p.70 ; مهامّ + **2ᵉ encadré-citation** p.71.
⚠️ **C'est le seul سند de la tranche à porter DEUX encadrés-citation.**

- **Auteur tel qu'imprimé** : ligne de source **ج. لاكان** ; ligne latine **`Jacques  LACAN`**
  (double espace imprimé) ; notice **جاك لاكان : ( 1901 – 1981 )**. Les deux encadrés signés **لاكان**.
- **Titre du سند** : **في اللاوعي**
- **Source imprimée** : **ج. لاكان، كتابات** —
  `Jacques  LACAN, Ecrits, vol,1.1996, éd. du Seuil, coll. Points.  pp. 136 - 137`
  *(`vol,1.1996` — ponctuation de la source telle quelle.)*
- **Illustration** : portrait photographique de Lacan (vignette dans le texte, p.69).

**التمهيد (verbatim)** :
> من " أنا أفكّر أنا موجود " إلى " أفكّر حيث لا أوجد وأوجد حيث لا أفكّر " تنقلب الآفاق لتعلن إزاحة قلعة
> الإنسان ذاتا وإحلاله بنية لاشعوريّة قوامها رمزيّة لغويّة مفتوحة على القول والتأويل.

**Thèse (reformulée)** : **l'inconscient est ce chapitre de mon histoire qui a été effacé, ou
qu'occupe un mensonge** — c'est le chapitre soumis à la censure. **Mais la vérité peut être
retrouvée** : le plus souvent, elle **a été écrite ailleurs**. Lacan énumère **cinq lieux** de cette
écriture :
> – dans les **monuments** commémoratifs (`الآثار (1) التذكاريّة`) : mon corps, noyau de la névrose
>   hystérique, où le symptôme hystérique exhibe la structure d'un langage et se déchiffre comme une
>   inscription qui, une fois recueillie, peut être détruite sans perte grave ;
> – dans les **documents d'archives** (`وثائق الأرشيف (2)`) : mes souvenirs d'enfance, impénétrables
>   comme eux quand je n'en connais pas la provenance ;
> – dans l'**évolution sémantique** (`التطوّر الدلالي (3)`) : le stock lexical qui m'est propre et ses
>   significations, à l'image de mon style de vie et de mon caractère ;
> – dans les **traditions** (`العادات`) : les légendes qui racontent mon histoire sous une forme
>   héroïque ;
> – enfin dans les **résidus** (`البقايا`) que conservent nécessairement les distorsions rendues
>   nécessaires pour raccorder le chapitre falsifié aux chapitres qui l'entourent, et **dont mon
>   interprétation rétablira le sens**.

**الهوامش (verbatim, p.70 — TROIS notes, appelées `(1)`, `(2)`, `(3)` dans le texte p.69 ;
vérifiées à 600 dpi)** :
> 1– **" الآثار "**: تحيلنا إلى ما يسميه **لاكان** " **بمرحلة المرآة** " `le stade du miroir`. مثّل هذا
> المفهوم إضافة حقيقية بالنسبة إلى التحليل النفسي حيث يرى **لاكان** أن هذه المرحلة، التي تمتد منذ
> ولادة الطفل حتى الشهر الثامن عشر، تتضمن بدورها ثلاث مراحل هي :
> أ- يتصرف الطفل وكأن صورته التي تنعكس على المرآة تمثل شخصا آخر حقيقي.
> ب - بعد ذلك يكف عن التعامل مع هذه الصورة كوجود حقيقي فلن يبحث عن الشخص الذي يتخفّى وراء المرآة، وهو
> إلى هنا يتصرف كالقرد.
> ج - في المرحلة الثالثة سيتميز الطفل الإنساني باعترافه أن هذا الآخر ليس إلا صورته.
> كل هذه المراحل تعلن عن المسار التطوري الذي تتعرف من خلاله الذات على هويتها.
>
> 2– **" وثائق الأرشيف "**: يكتسبها الطفل خلال اللحظة الثالثة من مرحلة المرآة حيث يبدأ بالتعرف على
> الأشياء من حوله و الأشخاص " بتبادل النظرات ".
>
> 3– **" التطور الدلالي "** : يعيد **لاكان** التفكير في التصور الفرويدي للمرحلة الأوديبية ويرى أن
> التماهي مع الأم لا يمثل إلا اللحظة الأولى من المرحلة الاوديبية، فالطفل يتماهى مع رغبة الأم في القضيب
> ( لا يقصد به لاكان هنا العضو الجنسي بل دلالته المجازية التي ترمز إلى الأب )، وفي لحظة ثانية يتدخل
> الأب ليحرم الطفل من تماهيه مع الأم ويحرم الأم من القضيب. هذه اللحظة تتمثل في الخضوع لقانون الأب.
> اللحظة الأوديبية الثالثة يتماهى فيها الطفل مع الأب وهنا يدخل في نظام الرمز أي في نظام اللغة. إن
> الدور الأساسي للأب ليس الحماية بل الكلام الذي يعني القانون، فعن طريق اللغة تنشأ المنظومة الرمزية
> للطفل.

⚠️ La graphie du mot « œdipien » **varie dans la même note 3** : `الأوديبية` (avec hamza) puis
`الاوديبية` (sans). Vérifié à 600 dpi.
⚠️ Ce bloc de هوامش est **de loin le plus long de la tranche** : il occupe la moitié inférieure de la
p.70 et constitue à lui seul un **mini-cours sur le stade du miroir et l'Œdipe lacanien**.

**الكاتب (notice, p.70)** :
> **جاك لاكان : ( 1901 – 1981 )** — وُلد بباريس في عائلة كاثوليكيّة برجوازيّة. نال درجة الدكتوراه
> بأطروحة حول « في الذهان العصابي وعلاقاته بالشخصية ». سطع نجمه في أوساط التحليل النفسي عبر المنتديات
> والحلقات الدراسيّة التي شارك فيها. حصل على العضويّة في جمعيّة التحليل النفسي بباريس (1934) وشارك في
> أشغال المؤتمر العالمي السادس عشر للتحليل النفسي. اهتم **لاكان**، في دعوته العودة إلى **فرويد** بعد أن
> تزعزعت مكانته، بتصحيح الانحراف الحاصل في الأوساط التحليليّة بفعل تأويل نظريات فرويد الذي حوّلها إلى
> هيكل مهزوز المضمون. بذلك أعطى بعدا جديدا للتحليل النفسي يعمّق ما ذهب إليه فرويد مستأنسا بمعطيات
> علميّة ألسنية وبنيويّة ورياضيّة. صدر له مؤلَّف تحت عنوان « كتابات » (`Ecrits` 1966) تضمّن أعماله
> الأساسيّة، منها « مرحلة المرآة وتكوّن الأنا » الذي بيّن فيه أن الإنسان ليس سيّد نظام دال وأنّ النظام
> الذي يكوّنه الأنا ينزاح لفائدة ما لم يفلت منه، والشّعار الذي رفعه **لاكان** هو « العودة إلى فرويد »
> وتمثلت الفكـرة الأساسيـة لـعمـله في الفكرتين التاليتين المتلازمتين: اللاوعي هو « خطاب الآخر » و
> « اللاوعي مبني كلغة ». على هذا الأساس يطور خاصة ثلاث عبارات: الرغبة هي رغبة الآخر، النظام الخاص
> يتطور ضمنه كل كائن إنساني تحدده اللغة التي تمثل للفرد دينا يحتاج إلى التسديد، والرغبة هي محرك الحياة
> وحجر الزاوية للاوعي ولا يمكن أن يوجد إلا بعقدة الإخصاء.

**المهام (verbatim, 5 puces, p.71)** :
- أتبيّن دلالة اللاّوعي كما حددها الكاتب؟
- فيم تتميّز هذه الدلالة بالمقارنة مع التحليل الفرويدي؟ أبني جدولا مقارنا.
- ما دلالة قول الكاتب " الحقيقة يمكن العثور عليها من جديد. وفي أغلب الأحيان تكون قد كتبت في موضع آخر "؟
  أستحضر بعض هذه المواضع وأستخلص دلالاتها الرمزيّة.
- من يكون " الآخر " حسب دلالة اللاوعي الواردة في النصّ؟
- إذا كانت تجليّات اللاّوعي رمزيّة فأيّ منزلة للتأويل في كشفها؟

**Encadré-citation n° 1 (p.69, à côté d'un dessin au trait — un homme de dos devant un miroir dont le
reflet porte un point d'interrogation à la place de la tête)** :
> " اللاوعي هو هذا الفصل من تاريخي تمّ محوه أو الذي تحتلّه أكذوبة ".
> — **لاكان**

**Encadré-citation n° 2 (p.71, à côté d'une gravure ancienne sur fond bleu — une main tenant une
plume d'oie, entourée d'arabesques calligraphiques et de canifs à tailler numérotés)** :
> " الحقيقة يمكن العثور عليها من جديد وفي أغلب الأحيان تكون قد كُتبت في موضع آخر ".
> — **لاكان**

---

###### سند 28 — م. مرلوبونتي — « منزلة اللاوعي » — p.72

⚠️ **Ce سند tient sur UNE SEULE PAGE** : titre, تمهيد, texte, source, **الكاتب** (renvoi),
**الهامش** et **المهام** sont tous sur la p.72. **C'est le سند le plus court de la tranche** — la
double page n'est décidément pas la règle.

- **Auteur tel qu'imprimé** : ligne de source **م. مرلوبونتي** ; ligne latine
  **`M. MERLEAU-PONTY`**.
- **Titre du سند** : **منزلة اللاوعي**
- **Source imprimée** : **م. مرلوبونتي، العلامات** —
  `M. MERLEAU-PONTY, Signes, éd. Gallimard 1960, pp. 290`
  *(`pp. 290` — pluriel pour une page unique, tel qu'imprimé.)*
- **Illustration** : portrait photographique de Merleau-Ponty, cigarette à la main (vignette dans le
  texte).
- **Coupure imprimée** : un `(...)` dans la dernière phrase.

**التمهيد (verbatim, vérifié à 600 dpi)** :
> مثّل القول باللاّوعي إهانة لموروث الإنسان عن نفسه أيقضت فيه مطلب معرفة ذاته من جديد، مطلبا لا يحرجه
> تداخل النفسي و الجسدي و يعدّ لفضاء يُتاح فيه القول و التأويل على التأويل .

⚠️ **`أيقضت`** [sic] — pour `أيقظت`. Confusion ض/ظ **réellement imprimée**, vérifiée à 600 dpi.

**Thèse (reformulée)** : « **les faits psychiques ont un sens** », écrivait Freud dans l'un de ses
plus anciens ouvrages. Cela signifie qu'**aucun comportement humain n'est le simple résultat d'un
mécanisme corporel**, et qu'**il n'existe pas non plus, dans la conduite, un noyau spirituel entouré
d'un milieu fonctionnant machinalement** : tous nos mouvements participent, à leur manière, de cette
efficience unique d'interprétation et de signification **que nous sommes nous-mêmes**. De toute façon,
en ramenant les superstructures à des infrastructures pulsionnelles, **Freud s'est efforcé de montrer
qu'il n'existe, dans la vie humaine, ni « bas » ni « dégradé »** ; on ne peut donc aller bien loin en
adoptant une interprétation qui s'appuie sur « ce qui est dégradé ». De même, en interprétant la
conduite par une sorte de fatalité héritée de l'enfance, Freud montre **qu'il y a dans l'enfance une
vie adulte anticipée** : on trouve ainsi, dans les conduites de l'enfant qui contrôle ses sphincters
(`sphinctériennes`), une capacité embryonnaire de choisir, dans ses rapports aux autres, entre la
générosité et l'avarice. Et en interprétant le psychique par le corporel, il dévoile la signification
du corps psychique comme il en dévoile la logique cachée ou latente : **avec la psychanalyse, l'esprit
pénètre dans le corps comme, à l'inverse, le corps pénètre dans l'esprit.**

**الهامش (verbatim, p.72 — UNE seule note, appelée `(1)` dans le texte)** :
> 1– إشارة إلى كتاب فرويد " خمسة دروس في التحليل النفسي" ( 1909 ) حيث كشف في درسه الأوّل أنّ الأعراض
> المرضيّة تزول بمجرّد الوعي بمعناها.

**الكاتب** — ⚠️ **ce n'est pas une notice mais un RENVOI**, imprimé p.72, verbatim :
> **راجع التعريف بمرلوبونتي الوارد بالسند 14**

(Renvoi **hors de cette tranche** : le سند 14 est dans les pages p.6-46 du même مبحث. À résoudre
depuis le fragment ch1a.)

**المهام (verbatim, 6 puces, p.72)** :
- ماذا استخلص الكاتب من قول فرويد " للوقائع النفسيّة معنى " ؟
- أتبيّن دلالة ردّ البنى الفوقيّة إلى بنى تحتيّة غريزيّة.
- أستحضر المثال الوارد في النص وأتبيّن كيف تُخبِرُ الطفولة عن حضور جنيني للرشد.
- أتبيّن الدرس الذي استخلصه الكاتب من تفسير فرويد للنفسي بالجسدي.
- أستحضر أمثلة أستدلّ بها على هذا التداخل بين النفسي والجسدي.
- ألا يفضي القول في الإنسان إلى تأويليّة تضيع فيها حقيقة الإنسان؟ أحرّر فقرة في الغرض.

**Encadré-citation** : **AUCUN**, et **aucune illustration** hors le portrait de l'auteur. Avec le
سند 21 (Foucault), c'est le second سند de la tranche sans encadré-citation ni image d'accompagnement.

**Terme latin imprimé dans le corps du texte arabe** : `(sphinctériennes)` — inséré tel quel, entre
parenthèses, après `بعمليات البول والبِراز`.

---

###### سند 29 — سارتر — « الإنسان مشروع » — p.73-74

- **Auteur tel qu'imprimé** : ligne de source **سارتر** ; ligne latine **`SARTRE`** (sans prénom).
  Encadré signé **سارتر**.
- **Titre du سند** : **الإنسان مشروع**
- **Source imprimée** : **سارتر، نقد العقل الجدلي** —
  `SARTRE; Critique de la raison dialectique, éd. Gallimard, 1960. pp 95 - 96`
- **Illustration** : portrait photographique de Sartre (vignette dans le texte, p.73).
- **Coupures imprimées** : le texte porte **trois `(...)`**.
- **Position** : c'est **le dernier سند** de la نافذة سندات du مبحث 1.1 (n° 29 sur 29).

**التمهيد (verbatim, vérifié à 600 dpi)** :
> إن كان الدرس الفرويدي قد دفعنا إلى مراجعة صورة الإنسان كما توارثناها فحطم نرجسيته وجنون عظمته، فإنّ
> ما نخشاه هو أن نفهم هذا الدرس على أنه يحل الخضوع محل الحرية واللاوعي محل الوعي والجنون محل العقل
> والهشاشة محل المسؤولية. لكّن مادام الإنسان هو من إبداع الإنسان فإنّه لا معنى لإنسان خارج الصورة التي
> يَرتَضِيها لنفسه.

⚠️ **`لكّن`** [sic] — la shadda est portée par le **ك** au lieu du **ن** (`لكنّ`). Vérifié à 600 dpi.

**Thèse (reformulée)** : **l'homme se définit par son projet**. Cet être matériel dépasse en
permanence la situation où il se trouve ; il se révèle et se détermine par le **dépassement**
(`التعالي عليها`) de cette situation, pour s'objectiver par le travail, l'acte et le mouvement.
**Il ne faut pas confondre le projet et la volonté**, même si le projet peut prendre parfois une
forme volontaire : la conscience immédiate, distincte de soi, et cette production permanente de soi
par le travail et la pratique, voilà notre structure propre — **ce n'est ni une volonté, ni un
besoin, ni une passion**. Mais nos besoins, nos passions et nos pensées les plus abstraites relèvent
de cette structure : ils sont **toujours hors d'eux-mêmes, vers…** — c'est ce que nous nommons
l'existence, ce qui **ne désigne pas** une substance stable reposant sur soi, mais une instabilité
permanente, un arrachement du corps entier hors de soi. Et parce que cet élan vers l'objectivation
prend des formes diverses selon les individus, et qu'il nous jette dans un champ de possibles dont
nous réalisons certains à l'exclusion d'autres, nous l'appelons aussi **choix** ou **liberté**.
⚠️ **Attention à ne pas retourner l'argument** : le manuel imprime que ce serait une **faute grave**
de reprocher à Sartre d'introduire ici l'irrationnel, de fabriquer un « commencement premier » sans
lien avec le monde, ou de doter l'homme d'une liberté-**fétiche** (`صنميّة`) — **cette objection ne
peut venir que d'une philosophie mécaniste**. Celui qui la formule veut réduire la **praxis** et
l'invention à la reproduction des données premières de notre vie et expliquer l'œuvre ou l'attitude
par ses seuls facteurs conditionnants ; son désir d'expliquer dissimule une volonté de rendre le
composé semblable au simple, de **nier** la spécificité des structures et de ramener le changement à
l'identité — ce qui est **retomber dans le déterminisme scientiste** (`الحتميّة العلمويّة`). À
l'inverse, la **méthode dialectique** refuse la réduction et procède en sens contraire : elle dépasse
en conservant. Mais les termes de la contradiction dépassée **sont incapables** de rendre compte du
dépassement lui-même ni de la synthèse ultérieure — c'est au contraire celle-ci qui les éclaire et
les rend intelligibles. **La contradiction fondamentale n'est pour nous que l'un des facteurs qui
délimitent et structurent le champ des possibles.** C'est **le choix** qu'il faut interroger si l'on
veut expliquer les possibles de la vie dans leur détail, découvrir leur singularité et comprendre
comment ils ont été vécus : l'effet ou l'acte de l'individu nous révèle le déroulement de ses
conditionnements — c'est **Voltaire, par son choix d'écrire, qui nous éclaire sur le sens de sa peur
enfantine de la mort, et non l'inverse**. **L'homme est, à l'égard de lui-même et des autres, un être
signifiant** (`كائن دالٌّ`), car on ne peut comprendre le moindre de ses mouvements sans dépasser le
présent pur et l'expliquer par l'avenir. Il est en outre **créateur de signes** dans la mesure où il
les utilise — toujours en se devançant lui-même — pour nommer certaines choses comme autres, futures
ou à venir ; mais ces deux opérations se ramènent au dépassement pur et simple. **L'homme produit des
signes parce qu'il est signifiant dans sa vérité même, et il est signifiant parce qu'il est
dépassement dialectique de tout ce qui est simplement donné.** Et **ce que nous nommons liberté, c'est
l'impossibilité de ramener l'ordre culturel à l'ordre naturel.**

**الهوامش (verbatim, p.74 — TROIS notes, appelées `(1)`, `(2)`, `(3)` dans le texte p.73)** :
> 1– **البراكسيس ( `Praxis`)**: مصطلح ماركسي يفيد الطاقة الإنسانية العملية والاجتماعية.
> 2– **العلموية**: توجه يرد إلى غوبلو `Goblot` (1858 – 1935 ) ويعتبر أن العلم وحده نموذج الحقيقة
> والمعرفة وكل ما سواه جهل.
> 3– **فولتير : `Voltaire`** (1694 – 1778) أديب وفيلسوف فرنسي وأحد أهم ممثلي فلسفة التنوير.

✅ Les deux intervalles de dates de ces notes (`1858 – 1935`, `1694 – 1778`) ont été **vérifiés** : ils
sont dans le **bon ordre** — ce ne sont pas des cas d'inversion.

**الكاتب** — ⚠️ **ce n'est pas une notice mais un RENVOI**, imprimé p.74, verbatim :
> **سارتر: انظر التعريف الوارد بالسند 16**

(Renvoi vers le سند 16 du même مبحث, dont la notice **جان بول سارتر: ( 1905 – 1980 )** est imprimée
**p.47** — donc **à l'intérieur de cette tranche**. Elle est transcrite intégralement au § de fin de
ce fragment, « Débordement amont — p.47 ». **Ce renvoi est donc résolu.**)

**المهام (verbatim, 7 puces, p.74)** :
- هل يعد الإنسان لعبة الأحداث والصدفة؟
- أتبيّن دلالة الوجود التي يقدمها سارتر.
- أي موقف يدحضه الكاتب في النص ؟
- ماهيّة الإنسان، هل هي من طبعه أم من إبداعه ؟
- ما دلالة أن يكون الإنسان مشروعا؟
- هل تنتفي مسؤولية الإنسان عن أفعاله في بعض الوضعيات التي يعيشها ؟
- أقارن بين صورة الإنسان كما قدّمها سارتر وصورة الإنسان كما يكشفها اللقاء بالتحليل النفسي؟ أيّ موقع
  أحتله ضمن هاتين الصورتين؟ أحرّر فقرة في الغرض.

**Encadré-citation (p.74, à côté d'une illustration en pastel — deux visages, l'un de face en clair,
l'autre de profil en ocre, découpés et emboîtés comme des pièces de puzzle)** :
> " إنّ الإنسان بالنسبة إلى ذاته وإلى الآخرين كائن دالٌّ ".
> — **سارتر**

---

##### § Notes, anomalies et incertitudes — fragment ch1b (p.47-74)

###### Ce que la tranche p.47-74 contient réellement — compté, pas déduit

| élément | constat |
| --- | --- |
| سندات couverts | **17 → 29**, soit **13 سندات** — plus la fin du سند 16 (p.47) |
| étendue réelle | 17 : p.48-49 · 18 : p.**50-52** · 19 : p.53-54 · 20 : p.55-56 · 21 : p.57-58 · 22 : p.59-60 · 23 : p.61-62 · 24 : p.63-64 · 25 : p.65-66 · 26 : p.67-68 · 27 : p.**69-71** · 28 : p.**72 seule** · 29 : p.73-74 |
| pagination du فهرس | **exacte** pour les 13 سندات (page d'ouverture vérifiée une à une) |
| notices d'auteur complètes | **8** (17, 18 — deux notices, 19, 20, 21, 22, 24, 26, 27) |
| notices remplacées par un **RENVOI** | **4** : 23 → سند 21 · 25 → سند 24 · 28 → سند 14 · 29 → سند 16 |
| سندات **avec** encadré هوامش | **9** sur 13 : 18 (2 notes), 21 (2), 22 (1), 23 (1), 25 (1), 26 (1), 27 (3), 28 (1), 29 (3). Les **4 sans** encadré sont 17, 19, 20, 24 |
| سندات **sans** encadré-citation | **4** : 21 (rien), 24 (dispositif d'écriture à la place), 25 (dispositif d'écriture), 28 (rien) |
| سند à **deux** encadrés-citation | **1** : le سند 27 (لاكان), p.69 et p.71 |
| dispositifs d'écriture (consigne + cadre à remplir / image à commenter) | **2** : p.64 (`أعلّق على الصورة مستأنسا بالنصّ.`) et p.66 (`أتأمّل هذه الصورة وأتأوّلها مستأنسا بما ورد في النص.`) |
| nombre de puces مهامّ | 5 · 6 · 5 · 4 · 5 · 5 · 6 · **8** · **8** · **8** · 5 · 6 · 7 — **il varie de 4 à 8, jamais fixe** |
| renvois « لمزيد التعمّق » vers une autre نافذة | **2** : p.51 (فلسفة التاريخ) et p.64 (التحليل النفسي) — plus le هامش p.66 (التحليل النفسي) |

###### Anomalies **réelles** de la source (toutes vérifiées par agrandissement à 600 dpi)

1. **p.48** — `رسالة في الطبيعة االبشريّة` : **alif doublé** dans `البشريّة`.
2. **p.48 / p.49** — divergence de millésime pour la *رسالة في الطبيعة البشريّة* : la ligne latine
   date **1737**, la notice **1739-1740**. Les deux sont imprimés.
3. **p.52** — trois mots collés dans les مهامّ : `معنىتمثّل`, `الفلسفةالألمانيّة` ; et **`يدفعونا`**
   pour `يدفعنا`.
4. **p.59** — `Folilo - Essais` pour la collection **Folio**.
5. **p.61** — `الكلمات والاشياء` (sans hamza) alors que la notice p.58 imprime `الكلمات والأشياء` ;
   et pagination `ص 268 — 2 69` (espace parasite dans `269`).
6. **p.62** — 3ᵉ puce des مهامّ : `إذا كان الكوجيتو لا يؤدّى بداهة إلى تأكيد الكوجيتو` — `الكوجيتو`
   répété là où le texte parle de `تأكيد الوجود`.
7. **p.66** — `ص 161 – 261` : plage de 100 pages pour un extrait d'une page.
8. **p.66** — `بينهماوأحدد` collé dans les مهامّ.
9. **p.67** — `pp 356-357 Gilles` : le prénom **`Gilles`** répété en fin de ligne bibliographique.
10. **p.67** — `ذات هيّ` : shadda parasite sur `هي`.
11. **p.72** — **`أيقضت`** pour `أيقظت` (confusion ض/ظ) dans le تمهيد.
12. **p.73** — **`لكّن`** : shadda sur le `ك` au lieu du `ن`.
13. **p.55** — le تمهيد du سند 20 se termine **sans point final**.

###### Fausses pistes écartées — ce que j'ai cru voir et qui n'y était PAS

Quatre lectures ont été **infirmées** par agrandissement à 600 dpi ; elles auraient chacune produit
une « anomalie du manuel » **inventée** :

- p.51 — j'avais lu `الجدل الهيغلي الهيغلي` (mot doublé) : **le manuel écrit `الجدل الهيغلي`, une fois.**
- p.54 — j'avais lu `ليوؤكد` : **le manuel écrit `ليؤكد`.**
- p.58 — j'avais lu `تفكيرا فلسفيا قريا` : **le manuel écrit `قريبا`.**
- p.67 — j'avais lu `الحدّ الذي تُهكنا مواجهته` : **le manuel écrit `تنهكنا`** (et `نكرهه`, pas `نكره`).

###### Intervalles de dates — TOUS vérifiés, aucun n'est inversé

Le manuel compose certains intervalles à l'envers ailleurs dans l'ouvrage. **Dans cette tranche, ce
n'est le cas d'aucun** : `1711 – 1776` (Hume), `1818 – 1883` (Marx), `1820 – 1895` (Engels),
`1844 – 1900` (Nietzsche), `1918 – 1990` (Althusser), `1926 – 1984` (Foucault), `1929 – 2007`
(Baudrillard), `1856 – 1939` (Freud), `1925 – 1995` (Deleuze), `1901 – 1981` (Lacan),
`1905 – 1980` (Sartre), `1858 – 1935` (Goblot), `1694 – 1778` (Voltaire). Le rendu **visuel** de ces
parenthèses en contexte RTL affiche l'année la plus tardive à gauche : c'est le comportement bidi
normal, **pas une inversion**. Contrôle croisé fait sur Hume (dates connues, ordre certain).

###### Variantes de graphie des noms propres — à harmoniser en aval

| auteur | formes imprimées dans la tranche |
| --- | --- |
| Hume | `د. هيوم` (source p.48) · `هيوم` (encadré p.49) · `دافيد هيوم` (notice p.49) |
| Marx / Engels | `كارل ماركس وف. انغلز` (source) · `ماركس` / `أنغلز` / `فيدريك انغلز` (notice p.51) — **`انغلز` et `أنغلز` coexistent sur la même page** |
| Nietzsche | `فريدريك نيتشه` (source p.53) · `نيتشه` (notice, encadré) |
| Althusser | `لويس ألتوسير` (source) · `ألتوسير` (notice, encadré) |
| Foucault | `م. فوكو` (source p.57) · `ميشال فوكو` (notice p.58 et source p.61) · `فوكو` (renvoi, encadrés) |
| Baudrillard | `ج. بودريار` (source, encadré) · **`جون بودريار`** (notice p.60) — pas `جان` |
| Freud | `فرويد` **partout**, jamais de prénom arabe |
| Deleuze | `جيل دولوز` (source, notice) · `دولوز` (encadré) |
| Lacan | `ج. لاكان` (source p.69) · `جاك لاكان` (notice p.70) · `لاكان` (encadrés, هوامش) |
| Merleau-Ponty | `م. مرلوبونتي` (source p.72) · `مرلوبونتي` (renvoi) — et `مرلوبونتي` dans la notice de Sartre p.47 |
| Sartre | `سارتر` (source p.73, renvoi, encadré) · **`جان بول سارتر`** (notice p.47) · `ج. ب.، سارتر` (هامش p.68) |

###### Incertitudes résiduelles

- **p.53, ligne 5** : `دون هذا االتفكير` — le mot semble porter un **alif doublé** (`االتفكير`) comme
  p.48 ; lu à 150 dpi seulement, **non revérifié à 600 dpi**. À contrôler avant toute citation
  verbatim de cette ligne.
- **p.67, `لُيُنهينا`** : la vocalisation exacte (damma sur le lâm ou kasra) n'est pas certaine à
  600 dpi ; le squelette consonantique `لينهينا` est sûr.
- **p.70, note 3** : `الأودييية` / `الاوديبية` — la forme avec hamza est nette, la seconde l'est
  moins ; le **fait** de la variation est sûr, la graphie exacte de la seconde occurrence l'est moins.
- Les **numéros de renvoi** (`السند 14`, `السند 16`, `السند 21`, `السند 24`) sont lus sans ambiguïté ;
  ce sont **les cibles** qui doivent être vérifiées dans le fragment ch1a pour `14` et `16`.

###### Débordement amont — p.47 : fin du سند 16 (سارتر)

⚠️ La p.47 **n'ouvre pas** le سند 17 : elle **achève le سند précédent (n° 16, سارتر)**, dont le texte
et le تمهيد sont p.46 (hors de cette tranche). Comme la tranche p.6-46 s'arrête avant, **ce qui suit
serait perdu** ; il est donc consigné ici.

**الكاتب (notice, p.47 — verbatim)** :
> **جان بول سارتر: ( 1905 – 1980 )** — فيلسوف وكاتب فرنسي، وجودي النّزعة، ويُعدّ من أهم فلاسفة القرن
> العشرين. تأثّر بفلسفة **هوسرل وهيدغر** وكذلك بتوجّهات **كيركغارد**. اهتم في البداية بالتحليل النفسي
> الفينومنولوجي كما ورد في كتاباته: « الخيال » (1936)، و« تعالي الأنا » (1937) و« مخطط لنظرية في
> الإحساس » (1939) و« المخيال » (1940). حيث يتجلى تأثر سارتر بالفينومينولوجيا التي قادته إلى تأسيس
> تصور للإنسان بلوره في « الوجود والعدم » (1943)، ويُعدّ هذا الأثر أهم كتابات **سارتر** الفلسفية أكّد
> فيه أن الإنسان هو الكائن الوحيد الذي يوجد لذاته وهو كائن حرّ ومسؤول وعليه أن يختار طريقه بحرّية.
> سنة1944 تخلى سارتر عن التدريس لإدارة مجلة « الأزمنة الحديثة »، مع صديقته **سيمون دي بوفوار**
> والفيلسوف الفينومينولوجي مرلوبونتي، وقد عُرفت هذه المجلة بطابعها السياسي حيث اتخذت من مقاومة كل
> أشكال الاغتراب هدفا لها، انطلاقا من سنة 1950 اقترب **سارتر** من الحزب الشيوعي حيث اعتبر
> « **رفيق درب** » نقدي، فأصدر « نقد العقل الجدلي » (1960) بيّن فيه علاقة الوجودية بالماركسية. وإذا
> كانت الماركسية تنطلق من المجتمع كبنية جدلية مغلقة فإن سارتر يقدم في هذا المؤلف نظرية تعترف بتعقد
> المجتمع ونظامه ولكنه يبني هذا النظام انطلاقا من الذاتية. بعد رفضه جائزة نوبل صدر له مؤلف عن فلوبير
> « أحمق العائلة » (1971. 1972. 1973) والذي تميز بخطاب تأويلي حيث بدا سارتر قريبا من التحليل النفسي
> لكنه على خلاف التحليل النفسي الذي يسلم بوجود لاوعي يستعصي على الذات، يدافع التحليل النفسي الوجودي
> عن اقتران الحدث النفسي بالوعي الذي يعبر دوما على اختيار الذات. توفي **سارتر** سنة 1980 بعد أن عاش
> حياة ملتزمة نموذجية، إذ وقف ضدّ حرب الجزائر وأدان التوسّع السوفياتي في شرق أروبا كما سُجن بألمانيا.
> رفض تسلّم جائزة نوبل (1964). تختزل كتاباته الثقافة الراهنة في مختلف أبعادها إذ تتقاطع في كتاباته
> عناصر مختلفة: وجوديّة، فينومينولوجيّة، تحليليّة وماركسيّة. كما ترك عديد الكتابات غير المنشورة وبصورة
> خاصة الجزء الثاني من مؤلف الوجود والعدم والذي ضمنه تصوره للمسألة الأخلاقية، والجزء الثاني من نقد
> العقل الجدلي والذي لم يُنشر بعدُ. صدر له أيضا في المجال الفلسفي: « الوجوديّة مذهب إنساني » (1946)،
> « وضعيات » ( في عشرة أجزاء من سنة 1947 إلى سنة 1976). وفي المجال الأدبي صدر له: « الغثيان » (1938)؛
> « الذباب » (1943)؛ « الأيادي القذرة » (1948)؛ « ما الأدب؟ » (1948)؛ « الكلمات » (1964)…

**المهام du سند 16 (verbatim, 5 puces, p.47)** :
- عمّ تخبرني تجربة الخجل؟
- ما منزلة الآخر في تحديد كينونتي؟
- هل تصيّرني علاقتي مع الآخر إلى شيء بالضرورة؟
- هل من تطابق بين إحساسي بذاتيتي وبين الصورة التي يحملها الآخر عنّي؟
- هل من تماثل بين " تجربة الحب " (باسكال، الوضعيّة الاستكشافيّة الثالثة) وبين " تجربة الخجل " كما
  يعرضها سارتر؟ أحرّر فقرة في هذا الغرض.

**Encadré-citation du سند 16 (p.47, à côté d'une peinture — deux masques de théâtre, l'un blanc,
l'un noir)** :
> " أخجل من نفسي كما أظهر للآخرين ".
> — **سارتر**

*(Ce bloc est à recoller à la fin du fragment ch1a, sous le سند 16.)*

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
`α = √(5 − 1) / 2` — **tel qu'imprimé** : la barre du radical couvre « 5−1 »,
et non le seul 5.

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

> " إذا كنت تـفـرّق هكـذا بين الاكتـشـاف والاختراع، فأين تضع إذن هذه النتيجة الجديدة المفزعة للتقدّم
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

> ساد اعتقاد بأنّ العمل العلمي هو مجرّد وصف للوقائع يكون كماله بتوفّر شرط موضوعيّة النقل عبر قراءة
> للأحداث قوامها حياد الذّات. ومع ذلك، لنا أن نرتاب في اعتقاد كهذا، تهزّه تصوّرات جديدة لعمل
> العقل العلمي حين يُدرك فاعليّة لا تكتفي بالمعرفة بل تذهب إلى توفير شروط المعرفة.

**الهامشان** (verbatim resserré) :

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

**الهامشان** (verbatim) :

1. **سلسلة ماركوف** : تسمية لمقولة سلسلة الأحداث التي بنى عليها ماركوف أندري أندريفيتش
   (1856—1922) الرّياضي الروسي نظريّته في الكسور المتّصلة.
2. **الثابتات** `Paramètres` : عنصر يؤخذ بعين الاعتبار لتقييم وضعية خاصة وفهم ظاهرة في
   جزئيّاتها، مرادف لعامل `facteur` والثّابتة في الرياضيات كميّة محدّدة تتوقّف عليها دالّة من
   المتغيّرات المستقلّة.

**الكاتب — رودولف كارناب (1891 — 1970)** : ولد في ألمانيا وهو فيلسوف ومنطقي وأحد أبرز مؤسّسي
حلقة فيينا. ينتمي في الآن نفسه إلى الفلسفة الألمانية والأنجلوسكسونية. عالج القضايا الأساسيّة
لإبستيمولوجيا الرياضيات والعلوم الصحيحة. وفي أبرز كتبه « البناء المنطقي للعالم » (1928)، حاول
تطبيق برنامج الظواهرية وهو إعادة بناء العالم من خلال علاقة وحيدة معطاة في التجربة المباشرة.
وقد جعلته عنايته الخاصة بلغة العلوم والفلسفة أحد أبرز الفاعلين في المنعرج اللغوي للفلسفة. من
مؤلّفاته أيضا : « التركيب المنطقي للغة » (1934)، « مدخل إلى علم الدّلالة » (1942)، « الأسس
الفلسفيّة للفيزياء » (1966)…

**المهام** (verbatim) :

- أستخرج دلالة النموذج الرياضي من النص وأبين الفرق بينه وبين النموذج الفيزيائي في القرن التاسع
  عشر، مستحضرا مثالا من تاريخ العلوم.
- ما الذي يفسّر الطابع التبسيطي للنموذج ؟ هل من قيمة لذلك ؟
- بم أفسر تغيّر النموذج ؟ ما هي استتباعات ذلك على قدرة العلم على تفسير الواقع ؟
- كيف أفهم قول الكاتب « إنّ العقل يعمل بالحدس، وغالبا ما يكون مفيدا أن يفكّر العالم بمساعدة
  الصور البصرية » ؟
- أحدّد تبعا لهذا القول، وحسب سياق النص، منزلة التجربة في العلم.
- يتحدث الكاتب عن لزوم الحذر من النموذج، كيف أفهم هذا التّحذير وما الذي يبرره ؟

**Encadré-citation (p.226)** : « إنّ العقل يعمل بالحدس، وغالبا ما يكون مفيدا أن يفكّر العالم
بمساعدة الصور البصريّة » — **كارناب**.

**Illustrations** : p.225 portrait photographique de Carnap ; p.226 atome stylisé (noyau jaune,
orbites bleues) accolé à l'encadré-citation.

##### 2.2 نافذة سندات — suite : سندات 4-16 (p.227-250)

> **Pages lues** : p.227–250 (intégral). **Source** : manuel élève `210402`
> (كتاب الفلسفة — السّنة الرّابعة من التّعليم الثانوي — الشّعب العلميّة, CNP).
> Suite directe de la نافذة سندات du **مبحث 2 — العلم بين الحقيقة والنمذجة** (les سندات 1–3,
> p.220–226, sont décrits plus haut dans la fiche).
>
> **Convention constatée** : chaque سند s'ouvre par un **تمهيد** (chapeau problématisant imprimé
> sur fond rose) suivi du texte et de sa référence bibliographique, puis des encadrés
> **الهامش / الهوامش / الهامشان** (notes), **الكاتب** (notice d'auteur) et **المهام** (consignes de
> travail). ⚠️ L'extension n'est **pas** systématiquement une double page : les سندات 9 (p.237) et 13
> (p.244) tiennent sur une seule page, et le سند 10 déborde sur p.238–239 — la colonne « ص. » ci-dessous donne
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

1. **تحكّمي (سيبارنيطيقي)** : نسبة إلى السيبارنيطيقا `Cybernétique` وهو علم حديث ظهر نوعيا في بداية
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
à interpréter par une équation périodique « فوقية » (transcendante) et « مخصوصة التعقيد », dès lors qu'on remplace les symboles
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
phénomènes. La deuxième loi de Newton — le corps du texte l'écrit en notation **arabe**, `ق = ك.س`
(« القوة هي حاصل ضارب الكتلة في التسارع ») ; la forme latine `f = m.a` n'apparaît que dans le **هامش 2** —
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

**Points saillants du texte** (reformulés) : il **n'est pas** difficile d'expliquer ce que veut dire
**النموذج العلمي** (« ليس من الصّعب أن نفسّر ما يعنيه النموذج العلمي »). Nous nous trouvons devant une situation qui présente une propriété
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
  « **فرودنتال** » (سند 13, p.244) ; le فهرس, lui, donne « فرويندتال » à son entrée n° 9 — mais
  « فرودنتال » à son entrée n° 13 (p.406). Trois graphies pour un
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

**1 — الواقع · `LA Réalité` — p.252-253**

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
- **بشلار** (graphie de la p.257), connu pour avoir forgé **مفهوم العائق الإبستيمولوجي** — ce qui empêche qu'un
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
**نظرية الإعلام** + **السيبارنيطيقا أو نظرية التحكم** (graphie de la p.258) + **نظرية الأنساق**, et qui contient les
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
  **تأليف : كارل. ر. بوبر** · **تحرير : مارك أ. نوترنو** · **ترجمة : أ.د. يمنى طريف
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
> معقّد** قوامه **قدرة تخيلية وإنشائيّة للعقل العلمي** تسمح له بابتكار **بنية مفهومية
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
- **p.264** — couverture reproduite : le nom de l'éditeur scientifique se lit **مارك أ. نوترنو** —
  lecture **confirmée à 900 dpi** par la R-7, le `[?]` est levé. Le millésime **2003** est
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
    - `3.1.3.2` سياقات فكريّة — p.327 : **1 الليبيراليّة** p.327 · **2 الفوضويّة** p.330 · **3 فلسفة العقد الاجتماعي** p.332
  - `3.1.4` نافذة كيفيّات للتفكير — p.335 *(libellé du فهرس ; la page 335 imprime `كيفيات التفكير`, sans `نافذة`)*
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
  | 13  | ستيورات ميل | حريّة الرّأي                  | 301 |
  | 14  | ميشو        | الحق والعنف                   | 303 |
  | 15  | ماركس       | في نقد الحقّ                  | 305 |
  | 16  | أرسطو       | العدالة والإنصاف              | 307 |
  | 17  | أفلاطون     | العدالة والقانون              | 309 |
  | 18  | باسكال      | العدل والقوّة                 | 311 |
  | 19  | راولس       | العدل أساس الطاعة             | 312 |
  | 20  | إيبكتات     | المواطن العالمي               | 314 |
  | 21  | تاسّان      | مواطن العالم المشترك          | 315 |
  | 22  | كاستلاس     | المواطن العالمي الجديد        | 317 |

- **Bornes de scope** :
  - ✅ INCLUS : الدّولة · السّيادة · المواطنة · السّلطة · الحقّ · القانون · العدالة · الشرعيّة · الدّيمقراطيّة ; السّياسة, اللائكيّة, الكليانيّة ; libéralisme, anarchisme, philosophie du contrat social.
  - ⛔ EXCLU : idem — le programme de شعبة الآداب.

#### مبحث 3.1 — الدّولة : السّيادة والمواطنة — transcription p.271-318

> ✅ **Portée : p.271-318, intégral** — page d'ouverture du **محور 3** et du مبحث, la
> **نافذة مدخل إلى التفكير في المسألة** (p.272-277) et la **نافذة سندات للتفكير في المسألة**
> (p.278-318, **22 سندات**).
> **Source** : manuel élève `210402` (كتاب الفلسفة — السّنة الرّابعة من التّعليم الثانوي —
> الشّعب العلميّة, CNP).
>
> ⚠️ **Le brief commun `BRIEF-TRANSCRIPTION.md` annoncé par la consigne n'existait pas** dans le
> scratchpad au moment de la transcription. Les conventions appliquées ici sont celles,
> **constatées**, de `SECTION-mabhath2.md` (même manuel, même gabarit de fiche) et de
> `BRIEF-MATIERE-philosophie-bac.md` : chiffres occidentaux, graphies arabes **telles
> qu'imprimées**, extraits **jamais recopiés** (R-2 — thèse reformulée), تمهيد / هوامش /
> notices / مهامّ **verbatim**.
>
> ⚠️ **Numérotation** : le manuel n'imprime **jamais** « 3.1 ». Il imprime un **`1`** en pastille
> bleue à côté du titre `الدّولة : السّيادة والمواطنة` (p.271) — ce مبحث est le **مبحث 1 du
> محور 3**. Le repère « 3.1 » est une convention de la fiche, pas du manuel.
>
> ⚠️ **Le gabarit « double page par سند » n'est PAS le gabarit de ce مبحث.** Constat : la
> très grande majorité des سندات tiennent sur **une seule page** (texte + تمهيد), et la page
> suivante porte **الكاتب / الهوامش / المهامّ**. Le nombre d'encadrés varie d'un سند à l'autre :
> plusieurs n'ont **aucun** هامش. Le détail page par page est donné plus bas.

---

##### Page d'ouverture du محور 3 et du مبحث — p.271

Bandeau du **محور** (en haut de page, sur fond crème) : **القيم بين النسبي والمطلق**.

Titre du **مبحث**, dans une ellipse verte, précédé d'une pastille bleue portant **`1`** :
**الدّولة : السّيادة والمواطنة**.

**Les 5 concepts du مبحث**, imprimés dans le cartouche bleu sous le titre (dans cet ordre) :

| ordre | concept imprimé |
| --- | --- |
| 1 | **الحقّ** |
| 2 | **الدّيمقراطيّة** |
| 3 | **السّلطة** |
| 4 | **العدالة** |
| 5 | **المواطن العالمي** |

**Encadré de citation** (verbatim) :

> إذا قيل لنا إنّه لأمْر جيّد أن يهلك واحد من أجل الجميع، فإنّي سأُعجب بهذا الحكم إذا صدر عن
> وطني فاضل ووقور يكرّس نفسه طوعا، وبدافع الواجب للموت في سبيل خلاص بلاده. ولكن إذا قصد بذلك
> أنّه من المسموح به للحكومة أن تضحّي ببريء من أجل خلاص الجمهور ـ فإنّي سأعتبر هذه الحكمة إحدى
> أكثر الحِكَم التي اخترعها الطغيان حقارة على الإطلاق، وأكثرها خطأ… وأكثرها خطرا.. وأكثرها
> تعارضا بشكل مباشر مع القوانين الأساسيّة للمجتمع.
> — ▲ **ج. جاك روسّو، الاعترافات**

Illustration : gravure monochrome de la **statue de la Liberté** (torche levée, tablette au
bras), foule à son pied.

---

##### 3.1.1 نافذة مدخل إلى التفكير في المسألة — p.272-277

###### Page de titre de la نافذة — p.272

Titre imprimé : **مدخل إلى التفكير في المسألة**.

**Encadré de citation** (verbatim) :

> "ماذا كانت طبيعة التمايز، وماذا كان طابع التواصل؟ هل يوجد أيّ تعارض بين الغرائز الطبيعيّة
> للفرد والمتطلبات الدائمة للدولة؟ أكان ما يعتبره الفرد عادلا بشكل طبيعي، شيئا آخر غير الذي
> كانت الدولة تفرضه، بصفة دائمة، باعتباره كذلك؟ وإذا كان مثل هذا الاختلاف موجودا، فكيف ظهر ؟…"
> — ▲ **أرنست باركر، أفلاطون وسابقوه**

Illustrations : (a) photomontage surréaliste — un homme souriant en costume, une **chaussure
noire géante** suspendue au-dessus de personnages courbés ou à demi enfouis dans le sable ;
(b) tableau : une **tête de plâtre antique** sur un socle, face à un **plateau de balance** doré
(composition à la Magritte).

###### 1 — وضعية استكشاف أولى — p.273-274

**Consigne imprimée** (verbatim) : *أقرأ النص وأتابع الحوار الدائر بين كليلة ودمنة:*

**Support (p.273)** — un fragment de **dialogue entre كليلة et دمنة** (réplique de كليلة,
réplique de دمنة, réplique finale de كليلة).

**Référence imprimée** (verbatim) :

> الفيلسوف الهندي بيدباً، كليلة ودمنة
> نقله من الفهلويّة إلى العربيّة: **عبد الله بن المقفّع**
> المكتبة الثقافيّة، بيروت — لبنان، ص 115—116

**Thèse (reformulée, R-2)** : كليلة met en garde contre la fréquentation du **سلطان**, comparée
à l'ascension d'une montagne escarpée dont les fruits sont précieux mais qui est le repaire des
fauves — trois choses ne s'y risquent que des téméraires (fréquenter le sultan, confier ses
secrets aux femmes, boire le poison pour l'éprouver). دمنة lui répond que **qui ne s'expose pas
aux dangers n'obtient pas ce qu'il désire**, et que trois entreprises sont hors de portée sans
grande ambition, dont **le service du sultan** ; l'homme vertueux, comme l'éléphant, n'a que
deux places dignes de lui — honoré auprès des rois, ou dévot auprès des ascètes. Le débat
oppose donc **retrait** et **engagement** dans la chose publique.

**هوامش** (encadré `هوامـش :` p.273 — 3 entrées, verbatim resserré) :

1. **كليلة ودمنة** : هما ابنا آوى، كانا ذوي دهاء وأدب. وكان دمنة أشرّهما نفسا وأقلّهما رضاً
   بحاله.
2. **عبد الله بن المقفّع** : كاتب أبي جعفر المنصور العباسي. فارسي الأصل، نشأ بالبصرة في النصف
   الأوّل من القرن الثاني للهجرة. كان عريقا في الفارسيّة وعارفا باللغتين الفهلويّة واليونانيّة.
   توفي في أواسط القرن الثاني للهجرة.
3. **كليلة ودمنة** : هو كتاب في إصلاح الأخلاق وتهذيب النفوس وضعه فيلسوف هندي اسمه **بيدبا** من
   واحد وعشرين قرنا للملك من ملوك الهند اسمه **دبشليم** ذكروا أنّه تولّى الهند بعد فتح
   الاسكندر وطغى وبغى فأراد **بيدبا** إصلاحه وتدريه فألّف هذا الكتاب، وجعل النصح فيه على ألسنة
   البهائم والطيور على عادة الهنود البراهمة في عصورهم القديمة. (انظر تمهيد الكتاب لمحمد
   المرصفي؛ القاهرة، أكتوبر 1912)

**المهام (p.274) — `أتقمّص الأدوار`**, deux colonnes (verbatim) :

**أتقمّص دور كليلة..**

- دمنة، هذا الغرّ؛ كيف لي أن أقنعه بالابتعاد عن الشأن السياسي حتّى لا يحترق بناره؟
- أيّة مخاطر عليّ أن أسوقها حتّى أثنيه عن عزمه؟
- كيف أقنعه بأنّ إصلاح السلطان هو بمثابة طلب ما لا يُطلب؟

**أتقمّص دور دمنة.**

- كليلة، هذا البائس؛ لماذا هو على هذه الحال من الاستسلام؟
- كيف لي أن أقنعه بحقّي في المشاركة في الشأن السياسي؟
- ما العمل حتّى يدرك الغنم الحاصل عن هذا التدخّل؟

**`أستعيد موقعي وأفكّر من جديد…`** (verbatim) :

- فيم يختلف كليلة ودمنة وفيم يتّفقان؟
- أيّهما على صواب: السياسة شأن عام أم شأن خاص؟
- ماذا يترتّب على اللامبالاة بالحياة السياسيّة؟
- ماذا يترتب على المشاركة العامّة في الحياة السياسيّة؟
- هل من منزلة أخرى غير منزلة "السياسي" ومنزلة "الناسك"؟

Illustration (p.274) : photomontage — un **vautour** perché sur une table où est posé un livre
rouge portant `CODE CIVIL`, un **pigeon** à côté.
Encadré-citation (p.274) : « إنّي أخاف عليك من السلطان فإنّ صحبته خطرة » — **كليلة**.

###### 2 — وضعية استكشاف ثانية — p.275-276

**Consigne imprimée** (verbatim) : *أقرأ الوثيقة وأتثبّت في مضامينها…*

**Support (p.275)** — encadré **وثيقة** : **الإعلان العالمي لحقوق الإنسان**, daté en bas
**10 ديسمبر 1948**.

⚠️ **Le manuel n'imprime PAS la Déclaration entière** : il en donne **9 articles choisis**, dans
cet ordre (repérage — le texte lui-même n'est pas recopié ici) :

| article imprimé | objet |
| --- | --- |
| **المادّة الأولى** | naissance libre et égale en dignité et en droits ; raison et conscience ; esprit de fraternité |
| **المادّة الثانية** | jouissance de tous les droits **sans distinction** (race, couleur, sexe, langue, religion, opinion politique, origine, fortune, naissance…), et **sans distinction fondée sur le statut du pays** (indépendant, sous tutelle, non autonome, souveraineté limitée) |
| **المادّة الثالثة** | droit à la vie, à la liberté et à la sûreté de la personne |
| **المادّة الخامسة** | interdiction de la torture et des peines ou traitements cruels, inhumains ou dégradants |
| **المادة الثامنة عشرة** | liberté de pensée, de conscience et de religion — y compris changer de religion, et la manifester seul ou en commun |
| **المادّة التاسعة عشرة** | liberté d'opinion et d'expression, **sans considération de frontières** |
| **المادّة العشرون** | liberté de réunion et d'association pacifiques ; nul ne peut être **obligé** de faire partie d'une association |
| **المادة الثامنة والعشرون** | droit à ce que règne un **ordre social et international** permettant la pleine réalisation des droits proclamés |
| **المادة الثلاثون** | aucune disposition ne peut être interprétée comme autorisant un État, un groupement ou un individu à **détruire** ces droits |

**المهامّ (p.276) — 12 consignes** (verbatim) :

- ما هوّ الإعلان العالمي لحقوق الإنسان؟ وهل اطلعت عليه من قبل؟
- أحدّد، من بين المواد المذكورة، المواد التي لا أقبلها؟ أبرّر جوابي.
- لماذا تحتاج مثل هذه الحقوق إلى تقنين؟
- أستخرج أهمّ الحقوق التي تنصّ عليها الوثيقة وأرتّبها حسب الأهميّة. أبرّر ترتيبي.
- أقارن نتيجة عملي بنتيجة عمل صديقي أو صديقتي وأناقشه (ها) في الأمر.
- أتفق معه (ها) على ترتيب موحّد.
- هل يمكن الاستغناء عن بعض هذه الحقوق؟ ماذا يترتب على ذلك؟
- لو دُعيتُ إلى إثراء هذه الوثيقة بإضافة حقوق أخرى، ماذا أقترح؟
- هل يمكن أن أشكّك في الطابع الكوني لهذه الحقوق؟
- هل أحترم في علاقتي مع محيطي هذه الحقوق؟ أذكر بعض الوقائع.
- ما هيّ المشاكل النظريّة والعمليّة التي يمكن حلّها باحترامنا لهذه الحقوق؟
- من أراه أهلا لحماية هذه الحقوق؟

Illustration (p.276) : reproduction de la **Déclaration des droits de l'homme et du citoyen**
(deux figures allégoriques, œil dans le triangle rayonnant, tables de la Loi) — légende
imprimée en français sous l'image : `Déclaration des droits de l'homme et du citoyen, Musée
Carnavalet, Paris.`
Encadré-citation (p.276) : « لكلّ إنسان حقّ التمتّع بكافّة الحقوق والحريّات الواردة في هذا
الإعلان ».

###### الأبعاد الإشكاليّة للمسألة — p.277

⚠️ Comme au مبحث 2, cette page **n'imprime aucune liste rédigée de dimensions problématiques** :
c'est une **page de méthode + espace de travail vierge** (cadres pointillés à remplir).

**Bloc `1`** — le titre du مبحث éclaté en trois cases : **السّيادة** — **و** — **المواطنة**
(flèche descendante depuis la case centrale « و »), puis les consignes (verbatim) :

- أركّز على أداة العطف وأستحضر العلاقات المنطقيّة التي تفترضها.
- أقيم هذه العلاقات بين "السّيادة" و"المواطنة".
- ماذا يترتّب على كلّ واحدة منها؟

Cadre à remplir : **أستخلص أهمّ الأسئلة التي يمكن أن توجهني في التفكير في هذه العلاقات**
(5 lignes numérotées 1-5, vides).

**Bloc `2`** — les 5 concepts rappelés en bandeau : **الحقّ – الديمقراطيّة – السلطة – العدالة –
المواطن العالمي**, avec deux consignes fléchées (verbatim) :

- ▲ أنتبه إلى هذه المعاني وأتثبّت فيها
- ▼ أستحضر المعاني التي تناقضها

puis deux colonnes à remplir : **أصلها بالسيادة وأستخلص ما يترتب من أسئلة أساسيّة:** /
**أصلها بالمواطنة وأستخلص ما يترتب من أسئلة أساسيّة:** (4 lignes vides chacune).

Cadre final : **أستخلص المشكلات الفلسفيّة وأبيّن الرهان من وراء التفكير فيها.** (5 lignes vides).

---

##### 3.1.2 نافذة سندات للتفكير في المسألة — p.278-318

###### Page de titre de la نافذة — p.278

Titre imprimé (vérifié au zoom) : **نافذة سندات للتفكير في المسألة**.

Deux **encadrés de citation** (verbatim) :

> "… ثمّ إنّ هذا الاجتماع إذا حصل للبشر كما قرّرناه، وتمّ عُمران العالَم بهم، فلا بدّ من وازع
> يدفع بعضَهم عن بعض، لما في طِباعِهم الحيوانيّة من العدوان والظلم… فيكون ذلك الوازع واحدا منهم
> يكون له عليهم الغلبة والسلطان واليد القاهرة حتّى لا يصل أحدٌ إلى غيره بعدوان؛ وهذا هو معنى
> الملك ".
> — ▲ **ابن خلدون، المقدّمة**

> " تستطيع القوّة العسكريّة ممارسة الإكراه على الجسد، لكن تأثيرها على العقول والقلوب يظلّ موضع
> شك ".
> — **تودوروف**

Illustrations : (a) nature morte — codes juridiques rouges, un livre ouvert, des lunettes et une
**balance** dorée ; (b) un **poing menotté** à côté d'une **rose** rose.

###### سند 1 — في السياسي — p.279-280

**التمهيد** (verbatim) :

> إن الاشتغال على مجال ما يقتضي رسم حدوده بتعيين ما يختصّ به وما يفرّقه عمّا سواه. وإذا كان من
> شأن الفكر الفلسفي فهم مجالات الممارسة بوجوهها فإنّه عليه، في حال اهتمامه بالمجال السياسي
> تحديدا، بيان ما يعنيه " السياسي " بالذات وما يميّزه عن الأخلاقي والجمالي…

**Référence imprimée** : **كارل شميت، معنى السّياسي** — `Carl SCHMITT, La notion de politique,
"Coll champs", éd Flammarion, 1992, pp 63-65`.

**Thèse (reformulée, R-2)** : on ne peut définir « le politique » qu'en dégageant ses catégories
propres. Or les autres domaines ont chacun leur couple fondateur — **bien/mal** (moral),
**beau/laid** (esthétique), **utile/nuisible** ou **rentable/non rentable** (économique). Le
critère spécifique du politique, auquel se ramènent les actes politiques et leurs mobiles, est la
**distinction ami/ennemi** (`التمييز بين الصديق والعدو`) : elle a **valeur de critère, non de
définition exhaustive**. Elle est **autonome** — sans se déduire des autres oppositions ni s'y
réduire. L'**ennemi politique** n'est pas nécessairement mauvais moralement, ni laid, ni même un
concurrent économique (on peut avoir intérêt à commercer avec lui) : il suffit qu'il soit
**l'autre, l'étranger**, dont l'existence rend possible un conflit que **les normes générales
préétablies** ne peuvent trancher et qu'**aucun tiers neutre** ne peut arbitrer.

**الهوامش** : ⚠️ **aucun** encadré de note sur ce سند.

**الكاتب — كارل شميت (1888-1985)** (verbatim resserré) : فيلسوف وسياسي وعالم قانون ألماني.
شغل فلاسفة القرن العشرين ولُقّب "بالعقل المعادي لليبراليّة". ينحدر من أسرة كاثوليكيّة ودرس في
برلين ثمّ ستراسبورغ حيث حصل على شهادة الدكتوراه في مجال نظريّة الدّولة. وبداية من 1928 انتقل إلى
التدريس بجامعة برلين التي ألّف فيها أهمّ مؤلّفاته **"معنى السياسي"** (1932) وفيه نقد
الديمقراطيّة والليبراليّة ورأى فيهما إضعافا لسلطة الدّولة. دافع منذ سنة **1930** عن النظام
السياسي القائم على مبدأ الرئاسة الديكتاتوريّة لذلك اعتبره **كارل بوبير** عدوّا لدودا للمجتمع
الليبرالي المفتوح. كتب أيضا : **"اللاهوت السياسي"** (1922)، **"نظرية التشريع"** (1928)،
**"البرلمانية والديمقراطية"** (1923). كما صدر له كتاب **"لوفياتان في نظرية الدولة لتوماس هوبس"**
(1938)، و**"الحرب الأهلية العالمية"** (1953—1973).

**المهام** (verbatim) :

- لِمَ نحتاج إلى التمييز، في مجال الممارسة الإنسانية، بين مجالات مختلفة؟
- أحدّد شروط إمكان تعريف السياسي حسب الكاتب.
- ما هو المعيار المميّز للسياسي وما علاقته بمعايير المجالات الأخرى؟
- أتبيّن دلالة هذا المعيار وأحدّد قيمته في نظر الكاتب.
- أستخلص السمات المميزة للسياسي في ضوء هذا التحديد.
- هل في التمييز بين السياسي والأخلاقي والاقتصادي والجمالي ما ينفي الصّلة بينها؟
- هل تساعدني مقاربة الكاتب على التمييز بين السياسة والسياسي؟

**Encadré-citation (p.280)** : « إن ما يختصّ به السياسي، والذي تُردّ إليه الأفعال السياسية
ودوافعها، هو التمييز بين الصديق والعدو » — **شميت**.

**Illustrations** : p.279 — petit **portrait gravé** en médaillon. ⚠️ **Anomalie** : la gravure
montre un homme âgé du **XIX<sup>e</sup> siècle** (longs favoris blancs, col haut et cravate
nouée) ; ce **n'est pas** Carl Schmitt (1888-1985), et le manuel ne la légende pas.
p.280 — photomontage : un **pistolet** et un **revolver** tenus au-dessus d'une **poignée de
main**, sur fond orangé.

###### سند 2 — حدّ السلطة — p.281

⚠️ **سند tenant sur une seule page** : تمهيد + texte + الكاتب + المهامّ, tout est sur p.281.

**التمهيد** (verbatim) :

> قد تغرينا بداهة الحياة فنخالها كما اعتاد الناس أن يروها، لكن ما أن ندقّق النظر حتّى نكتشف تهافت ما
> ألفناه، ذك [sic] هو حال علاقتنا بالسلطة ، فلحظة تصوّرناها في الدّولة اكتشفنا أنّها أوسع مدى وأدَقّ
> معنى.

**Référence imprimée** : **ميشال فوكو، إرادة المعرفة** — ترجمة مطاع صفدي وجورج أبي صالح، مركز
الإنماء القومي، 1990، ص 101 — 102. `Michel FOUCAULT; La volonté de savoir, éd. Gallimard, 1976,
pp 121-122`.

**Thèse (reformulée, R-2)** : Foucault écarte **trois** identifications courantes du mot
« pouvoir » — (a) l'ensemble des **institutions et appareils** qui garantissent la soumission des
citoyens dans un État, (b) un **mode d'assujettissement** qui, à la différence de la violence,
prendrait la forme d'une **règle**, (c) un **système général de domination** exercé par un
élément ou un groupe sur un autre et traversant tout le corps social. Souveraineté de l'État,
forme de la loi, unité globale d'une domination ne sont que des **formes terminales** du pouvoir,
non ses données premières. Le pouvoir est **la multiplicité des rapports de force** immanents au
domaine où ils s'exercent ; **le jeu** qui, par affrontements et luttes incessants, les
transforme, les renforce ou les inverse ; les **appuis** que ces rapports trouvent les uns dans
les autres, formant chaîne ou système, ou au contraire les **décalages et contradictions** qui
les isolent ; enfin les **stratégies** dont le dessin général se cristallise dans les appareils
d'État, la formulation de la loi et les hégémonies sociales. Conclusion : *le pouvoir n'est ni
une institution, ni une structure, ni une capacité dont certains seraient dotés — c'est le nom
donné à une situation stratégique complexe dans une société donnée.*

**الهوامش** : ⚠️ **aucun** encadré de note.

**الكاتب** : ⚠️ **renvoi, pas de notice** — imprimé verbatim :
**ميشال فوكو : انظر التعريف بالكاتب المصاحب للسند عدد 21 ( الإنيّة والغيريّة )**.

**المهام** (verbatim) :

- أبدأ بتعريف السّلطة كما أتصوّرها.
- يستبعد الكاتب تحديدات مختلفة للسّلطة: أضبطها وأكشف عن المجال المشترك بينها.
- أكشف عن المنطق الذي قاد الكاتب في هذا الاستبعاد.
- أتتبّع النصّ وأتقصّى دلالة السلطة عند الكاتب.
- كيف أفهم، في ضوء التحديدات السابقة، العبارة الأخيرة من النصّ؟
- في ضوء مقاربة الكاتب، هل يمكن اختزال السلطة في الدّولة؟
- أقترح تعريفا جديدا للسلطة وأقارنه بتصوّري السابق.

**Illustration** : p.281 — **photographie de Michel Foucault** (crâne chauve, lunettes, col roulé
blanc), en médaillon.

###### سند 3 — التفكير في السلطة — p.282-283

**التمهيد** (verbatim) :

> السّلطة اختراع بشري، اقترن وجودها بالقوة، يمارسها الإنسان وتمارس عليه، ينجذب إليها بصفتها
> موضوع إغراء وينفر منها كما لو كانت طاعونا مميتا حتى غدت أمرا ملتبسا التفكير فيه" يفقد الصواب ".

*(⚠️ le guillemet fermant de la dernière ligne est **imprimé tel quel**, sans guillemet ouvrant
correspondant.)*

**Référence imprimée** : **بول ريكور، التاريخ والحقيقة** — `Paul RICŒUR; Histoire et Vérité, éd.
Ceres, 1995, pp 133-134`.

**Thèse (reformulée, R-2)** : le pouvoir est **la structure fondamentale du politique** — il
s'insinue dans tous les rapports gouvernant/gouverné, et même à la limite d'une communauté qui
se gouvernerait elle-même sans médiation ni délégation, subsisterait l'écart entre **commandement
et obéissance**. C'est grâce au pouvoir qu'une communauté historique s'organise en État et
devient **capable de décider**. Or c'est aussi le rapport humain le plus **fragile** : il bâtit le
pouvoir de l'homme sur l'homme comme une communication **inégale**, non réciproque, hiérarchique
et non fraternelle. Cette relation est pourtant **fondatrice** de l'histoire — c'est par le
pouvoir que l'homme fait l'histoire — et c'est **la relation même qui forme l'homme et qui n'a
jamais cessé de l'égarer** : d'où la plainte immémoriale des sages contre les grands et les
puissants ; Socrate dessine les traits du **tyran** et concentre en lui l'hostilité à la
philosophie, avant de tomber victime de la **cité injuste**. Alain résume : *« السّلطة تُفقِد
الصّواب »*. Le désir de pouvoir n'est pas orienté vers le **plaisir** : l'amour véritable du
pouvoir a quelque chose de l'**ascèse**, on lui sacrifie le plaisir. Enfin, penser le pouvoir ne
s'épuise pas dans une **méditation morale** sur les passions du pouvoir et leur extirpation :
chacun sent que la pensée tourne ici dans un champ étroit si elle s'emprisonne dans les seuls
mobiles individuels — le problème du despote *« n'est que la projection subjective du problème du
pouvoir »*. Il existe une **maladie du pouvoir** irréductible à la mauvaise volonté des individus,
qui ne se ramène ni à la violence du prince ni à la lâcheté des sujets : violence de l'un et
lâcheté de tous se **conjuguent** en une figure corrompue unique, se renforçant l'une l'autre,
et façonnant en retour **le despote et son vis-à-vis, l'humilié**.

**الهامشان** (verbatim) :

1. **المدينة الجائرة** : إشارة إلى أثينا التي حوكم فيها سقراط وأعدم.
2. **آلان** `Alain` : كنية للفيلسوف الفرنسي إيميل شارتييه `Emile Auguste CHARTIER
   (1868-1951)`.

**الكاتب** : ⚠️ **renvoi, pas de notice** — imprimé verbatim :
**بول ريكور: انظر التعريف بالكاتب المصاحب للسند عدد 21 ( الخصوصيّة والكونيّة )**.

*(⚠️ à noter : les سندان 2 et 3 renvoient tous deux à « السند عدد 21 », mais de **مباحث
différents** — الإنيّة والغيريّة pour Foucault, الخصوصيّة والكونيّة pour Ricœur.)*

**المهام** (p.283, verbatim) :

- ماذا يعني الكاتب حين يعرّف السلطة.بما هي " البنية الأساسية للسياسي"؟
- أيّة علاقة بين السلطة وتاريخ الإنسان ؟
- كيف تشكّل السلطة الإنسان و تضلّه في الوقت نفسه ؟
- كيف أفهم استحضار الكاتب لشخصيّة سقراط؟
- ما قيمة مقاربة السلطة من زاويّة أخلاقيّة؟
- أيّة دلالة لمرض السلطة في نظر الكاتب وهل يعدّه هيكليّا أم عرضيّا؟
- أيّ غنم أحصله من مقاربة الكاتب بشأن التفكير في السّلطة؟

**Encadré-citation (p.283)** : « السّلطة هي البنية الأساسية للسّياسي » — **بول ريكور**.

**Illustrations** : p.282 — **photographie de Paul Ricœur** (homme âgé à lunettes, veste, devant
une bibliothèque). p.283 — reproduction du **Sacre de Napoléon** (David) : l'empereur couronné de
laurier élevant la couronne au-dessus de Joséphine agenouillée.

###### سند 4 — العصبيّة والمُلْك — p.284

⚠️ **سند tenant sur une seule page**.

**التمهيد** (verbatim) :

> لم يخل واقع البشر من سلطان ينشدّون إليه رغبة ورهبة، به يحتمون ومنه يخشون وهم في ذلك لا يدركون
> له أصلا ولا كنها ولا يعلمون من حقيقة فعله إلا أن له غلبةً يطلبُ الجميعُ وُدَّها ومنها يأمنون.

**Titre courant imprimé au-dessus du texte** (intitulé du chapitre de la المقدّمة, verbatim) :
**في أنّ الملك والدولة العامة إنّما يحصلان بالقبيل والعصبيّة**.

**Référence imprimée** : **ابن خلدون، المقدّمة** — طبعة دار العودة 1981، ص 121—122.

**Thèse (reformulée, R-2)** : la **مغالبة** et la **ممانعة** ne s'obtiennent que par la
**عصبيّة** — parce qu'elle seule produit la solidarité du groupe et fait que chacun se sente
atteint par ce qui atteint son compagnon. Or le **مُلْك** est une position **honorée et
convoitée**, qui donne accès à tous les biens et plaisirs de ce monde : il est donc l'objet d'une
**compétition** où nul ne cède à autrui sans y être contraint, d'où conflits, guerre et combats —
et rien de tout cela n'advient sans عصبيّة. Ce fait échappe au **grand nombre** et est
« oublié » : les générations qui vivent longtemps sous une dynastie déjà civilisée ne savent plus
comment Dieu l'a instaurée ; les sujets ne connaissent que les **maîtres de l'État** installés, la
soumission leur est devenue une seconde nature et ils croient pouvoir se passer de la عصبيّة —
c'est le cas, en particulier, des **أهل الأندلس**, chez qui l'oubli de cette عصبيّة, la longueur
de la durée et l'affranchissement de son emprise ont fait s'évanouir la patrie même.

**الهوامش** : ⚠️ **aucun** encadré de note.

**الكاتب** : ⚠️ **renvoi, pas de notice** — imprimé verbatim :
**ابن خلدون : انظر التعريف بالكاتب المصاحب للسند عدد 16 ( الخصوصيّة والكونيّة )**.

**المهام** (verbatim) :

- أحدّد علاقة العصبية بالملك أو الدولة.
- هل من تمييز في النص بين الملك والدولة، بين الدولة والسلطة؟
- ما دلالة القول: " الملك منصب شريف ملذوذ "؟
- هل من تناقض بين القول بشرف الملك واقتضائه الغلبة؟
- يقرن ابن خلدون تعاقب الأجيال وتحولات الدولة: ماذا أفهم من هذه العلاقة؟
- أبحث عن طرافة التفسير الخلدوني لسيادة الدولة في ضوء ما عرفت عن هذا الأمر.
- أمتحن وجاهة القول بفعالية العصبية والقبلية في الحياة السياسية في ضوء واقع الدولة المعاصرة.

**Illustration** : p.284 — **portrait enluminé d'Ibn Khaldoun** (turban blanc, robe bleue, livre
ouvert), en médaillon.

###### سند 5 — الحاجة إلى الدولة — p.285-286

**التمهيد** (verbatim) :

> لم ينشغل الإنسان بالخضوع للدولة من عدمه بقدر انشغاله بتبرير هذا الخضوع. واقتضى التبرير مساءلة
> الدولة عن أصلها وعلّة نشأتها عسانا نتعقّل غايتها وندرك طبيعة حاجتنا إليها.

**Référence imprimée** : **هيوم، رسالة في الطبيعة البشريّة** — `D. HUME; Traité de la nature
humaine. éd Aubier Montaigne, pp 660 - 661`.

**Thèse (reformulée, R-2)** : le **gouvernement** est une invention **très utile**, et même dans
certaines circonstances une nécessité absolue pour l'homme — mais **pas dans toutes** les
circonstances. Il n'est pas impossible que des hommes se maintiennent quelque temps en société
**sans** y recourir. Les hommes préfèrent certes toujours un intérêt **immédiat** à un intérêt
**lointain**, et il leur est difficile de résister à la tentation d'un gain saisissable tout de
suite par crainte d'un mal éloigné ; mais ce défaut est **d'autant moins manifeste** que les biens
et les plaisirs de la vie sont **rares et de peu de valeur**, comme ils le sont toujours à
l'**enfance de la société** — un Indien qui n'a envie ni d'arracher la hutte d'autrui ni de lui
voler son arc jouit déjà de ce qu'il possède, et la chance à la chasse ou à la pêche n'est
qu'accidentelle et passagère, donc peu propre à ébranler la société. Hume se démarque alors
expressément de « certains philosophes » : il est **très loin de croire** que les hommes sont
incapables de vivre en société **sans gouvernement**, et il soutient que les **premières
origines** du gouvernement sont nées de conflits **non pas entre membres d'une même société**
mais **entre sociétés différentes**. Une richesse même faible suffit à produire ce second effet,
alors qu'elle ne suffit pas à produire le premier : les hommes ne redoutent rien tant, de la
guerre et de la violence collective, que la **résistance** qu'ils y rencontrent — et comme cette
résistance est **partagée**, elle leur paraît moins terrible ; comme elle vient d'**étrangers**,
elle leur semble avoir des suites **moins graves** que celle d'hommes qu'ils affrontent seuls,
avec lesquels ils ont d'ordinaire un commerce profitable et sans la société desquels il leur
serait impossible de continuer à vivre. **Ainsi une guerre extérieure, dans une société sans
gouvernement, produit nécessairement la guerre civile.**

**الهوامش** : ⚠️ **aucun** encadré de note.

**الكاتب** : ⚠️ **renvoi, pas de notice** — imprimé verbatim :
**هيوم : انظر التعريف بالكاتب المصاحب للسند عدد 17 ( الإنيّة والغيريّة )**.

**المهام** (p.286, verbatim) :

- بأيّ معنى تعدّ الحكومة اختراعا مفيدا؟
- ما هيّ الحجج التي يسوقها الكاتب لاستبعاد القول بانّ الدولة ضرورة مطلقة؟
- استثمر نافذة سياقات فكريّة ( فلسفة التعاقد ) للكشف عن ضمنيات موقف الكاتب.
- أتبيّن دلالة " مثال الهندي " وأوضّح وظيفته الحجاجيّة.
- أيّ ضرب من الصراع يوجب قيام الدولة؟
- " إنّ حربا خارجيّة في مجتمع بلا حكومة تحدث بالضرورة الحرب الأهليّة ": هل حافظ هذا الحكم على
  راهنيّة ما؟

**Encadré-citation (p.286)** : « إنّني بعيد كلّ البعد عن الاعتقاد، شأن بعض الفلاسفة، أنّ البشر
عاجزون كل العجز على العيش في مجتمع دون حكومة » — **هيوم**.

**Illustrations** : p.285 — **portrait gravé de David Hume** (perruque, habit XVIII<sup>e</sup>).
p.286 — **Napoléon I<sup>er</sup> en costume de sacre** (manteau d'hermine, sceptre, couronne de
laurier), devant un globe et un livre ouvert.

> 🔎 **Renvoi utile pour la génération** : la 3<sup>e</sup> مهمّة de ce سند renvoie explicitement à
> une **نافذة دعائم — سياقات فكريّة : فلسفة التعاقد**. Cette نافذة existe donc dans le مبحث,
> **au-delà de la p.318** (hors de cette tranche).

###### سند 6 — في الدولة — p.287-288

**التمهيد** (verbatim) :

> تحمل الدولة آمال البشر في الذّود عن حقوقهم ودرء الأذيّة عنهم بما يمكّن الإنسان من تحقيق كمال هو
> جدير به. لكن قد لا يكون ذلك أكثر من تمويه تتسلّل من خلاله الرغبة في الاستحواذ على كل شيء
> فيؤول الحقّ الذي تدّعي حفظه إلى مجرّد إجراء يحضر قولا ويغيب فعلا وكأنّ الخير المطلق يُنذِر بشرّ
> مطلق.

**Référence imprimée** : **ميخاييل باكونين، الأعمال الكاملة** — `Mikhaïl BAKOUNINE; In BAKOUNINE,
présentation, choix de textes, Henri Arvon Michel, Seghers. 1996. pp.98 - 99`.

**Thèse (reformulée, R-2)** : à la question « qu'est-ce que l'État ? », métaphysiciens et
juristes répondent : la **chose publique**, les intérêts et le bien communs, le droit de tous,
opposés à la conduite destructrice née des intérêts et des caprices égoïstes de chacun ; l'État
serait **la justice et la moralité incarnées** — d'où l'idée qu'il n'est pas d'acte plus haut ni
de devoir plus grand, pour l'individu, que de se vouer et de se sacrifier, jusqu'à mourir, pour
la victoire et la puissance de l'État. Bakounine renverse la thèse : cette « théologie
politique », exactement comme la théologie religieuse, **dissimule sous de belles apparences des
faits ordinaires et sordides**. L'idée d'État exige en réalité le **sacrifice de la liberté
naturelle** et des intérêts de chacun, ainsi que des intérêts des groupements **relativement
petits** (associations, communes, régions), au nom de l'intérêt et de la liberté de tous et de la
prospérité du « grand tout ». Mais ce « grand tout », qu'est-il en réalité ? Il devrait être la
somme de tous les individus et de toutes les communautés humaines les plus étroites — or il ne
peut l'être, puisqu'on exige justement le sacrifice de tous les intérêts individuels et locaux
pour le composer. Ce n'est donc pas un **ensemble vivant** où chacun respire à son aise et devient
d'autant plus fécond et fort que la liberté de chacun y est plus large ; ce n'est pas la société
humaine naturelle, celle qui **confirme et développe** la vie de chacun par la vie de tous ; c'est
au contraire l'**immolation** de l'individu et des associations locales, la **limite**, la
**négation** de la vie et du droit de toutes les parties qui le constituent, au nom du prétendu
bien de tous. Conclusion : *ce tout, c'est l'État — l'autel de la religion politique sur lequel la
société naturelle est toujours sacrifiée : une universalité prédatrice qui vit d'offrandes
humaines.*

**الهوامش** : ⚠️ **aucun** encadré de note.

**الكاتب — ميخاييل باكونين (1814-1876)** (verbatim resserré) : مفكّر وثوري روسي. التقى
**بماركس وبرودون** بباريس والتحق نهائيّا **بالفوضويّة** (1864) وأنشأ "الحلف العالمي للديمقراطيّة
الاجتماعيّة". أطرده ماركس وأتباعه من " الأمميّة الأولى " (1872). كان من أنصار الملكيّة المشتركة
لوسائل الإنتاج وعارض ملكيّة الدولة. من أهمّ كتاباته: **" في التعاضد "** (1869)، **" كومنة باريس
ومفهوم الدولة "** (1871)، ويبقى كتابه **" الإله والدّولة "** (1871) أهمّ مؤلَّفاته، وفيه دافع عن
فكرته الأساسيّة الرّافضة لكلّ أشكال السلطة ومؤكدا على أن الإنسان لن ينال حريّته إلاّ في مجتمع
حرّ أي مجتمع دون سلطة الدولة. وفي رأيه وُجدت القوانين السياسيّة لإخضاع الإنسان لسلطة الدولة.
والإنسان الحرّ هو الإنسان الذي لا يخضع إلاّ لنفسه وذلك بفضل معرفته بقوانين الطبيعة. فإذا كانت
القوانين السياسيّة تستعبده فإنّ قوانين الطبيعة تحرّره.
**( لمزيد التعمّق انظر نافذة دعائم للتفكير في المسألة، سياقات فكريّة: الفوضويّة )**.

**المهام** (verbatim) :

- أيّ تصوّر للدولة يناقشه الكاتب؟
- ما دلالة عبارة " اللاهوت السياسي " التي يستعملها الكاتب؟
- ما مصير الحقّ في ظلّ الدولة حسب توجّه الكاتب؟
- كيف أفهم التقابل الذي يقيمه الكاتب بين الدولة والمجتمع الطبيعي؟
- أستخلص تصوّر الكاتب للدولة وأفكّر في وجاهته. أحرّر فقرة في الغرض.

**Encadré-citation (p.288)** : « إن هذا الكلّ هو الدولة، مذبح الدين السياسي الذي يُذبح فوقه دوما
المجتمع الطبيعي: إنّه كليّة مفترسة تعيش على قرابين بشريّة » — **باكونين**.

**Illustrations** : p.287 — **portrait peint de Bakounine** (barbe fournie, cheveux longs), en
médaillon. p.288 — photographie d'une **foule de jeunes gens le bras tendu** en salut collectif.

> 🔎 **Second renvoi à la نافذة دعائم** : la notice de Bakounine renvoie à
> **سياقات فكريّة : الفوضويّة** — deuxième سياق فكري attesté du مبحث, également au-delà de p.318.

###### سند 7 — حدّث زرادشت عن الدولة قال… — p.289-290

**التمهيد** (verbatim) :

> كثيرا ما ننشدّ إلى الدولة ونعتبرها شرط إمكان وجودنا، فهي التي حددت ماضينا وتؤمن حاضرنا وترسم
> أفق مستقبلنا، لذلك يربكنا القول بميلاد الإنسان حين تفنى الدولة، فتنقلب خشيتنا من التيه في صورة
> غيابها إلى وهم نسينا أنه كذلك وكأن بين الوهم والحقيقة خيطا رفيعا نسجته عنكبوت.

**Référence imprimée** : **نيتشه، هكذا حدّث زرادشت (1)** — ترجمة فليكس فارس، منشورات المكتبة
الأهليّة — بيروت، ص72— 73 — 47 — 57 ( بتصرّف لجنة التأليف ). `NIETZSCHE; Ainsi parlait
Zarathoustra. éd. Mercure de France, pp 66 -70`.

*(⚠️ la mention **« بتصرّف لجنة التأليف »** — texte remanié par la commission de rédaction — est
imprimée sur ce سند ; c'est le seul de la tranche à la porter.)*

**Thèse (reformulée, R-2)** : Zarathoustra oppose **peuple** et **État**. Il subsiste en quelques
lieux de la terre des peuples et des communautés, mais « chez nous » il n'y a plus que des
États. L'État est **le plus froid des monstres froids** ; il ment froidement, et son mensonge
est celui-ci : *« moi, l'État, je suis le peuple »*. Or les peuples ont été créés par les
**créateurs**, ceux qui ont répandu la foi et l'amour et ont ainsi servi la vie ; ceux qui
tendent des pièges à la multitude, au contraire, **détruisent** pour bâtir des États sur les
ruines, hissent une épée au-dessus du peuple et dressent devant lui cent convoitises. Là où il y
a encore un peuple, l'État n'est pas compris — il est haï comme un **mauvais œil** et vu comme une
transgression des coutumes et des lois. Preuve : chaque peuple a son propre **langage du bien et
du mal**, langage qu'il s'est forgé lui-même dans ses lois et coutumes ; l'État, lui, **ment** en
tout ce qu'il dit du bien et du mal, et **rien de ce qu'il possède ne lui appartient** — tout est
volé. Tout en lui est **faux** : il mord avec des dents empruntées, ses entrailles sont
fabriquées, son emblème n'est qu'un « discours confus » sur le bien et le mal — il tend vers
l'anéantissement et le proclame en appelant ouvertement les prophètes de mort. Trop de gens
viennent au monde, et l'État n'a été inventé que **pour les superflus**, les intrus dans la vie :
voyez comme il les attire, les serre contre sa poitrine, les étouffe de baisers, tandis qu'il
gronde : *« il n'y a rien de plus grand que moi sur la face de la terre, car je suis la main de
la divinité ordonnatrice »*. Ces intrus amassent l'argent : plus leurs trésors grossissent, plus
leur misère grandit ; ils aspirent au pouvoir et se saisissent d'abord de son premier moteur,
**l'argent** — impuissants pourtant. Ils grimpent les uns sur les autres comme des **singes**,
se bousculant dans la boue vers l'**abîme** : chacun rêve du trône, croyant le bonheur assis là,
alors que souvent c'est la boue qui monte au trône, et le trône qui tombe dans la boue. Ce sont
tous des fous furieux, des singes agités escaladant le socle de leur **idole froide**. D'où
l'appel imprimé en fin de page : **« brisez les fenêtres et sautez-en pour vous sauver »**
(`حطّموا النوافذ واقفزوا منها لتنجوا بأنفسكم`) — fuyez le **culte des idoles**, cette
« religion des intrus de la vie » (`عبادة الأصنام … دين الدخلاء على الحياة`) ; c'est **hors** de
l'État que les **grandes âmes** (`كبار النفوس`) trouvent refuge, et la page se clôt sur
**« bienheureux les petits, les pauvres ! »** (`فطوبى لصغار الفقراء!`). ⇒ Ce motif — **retraite
hors de l'État / bénédiction des petits** — porte la مهمّة n° 3 : ne pas le laisser tomber au
resserrement. Là où
finit l'État commence l'homme véritable : y monte le **chant de la nécessité**, aux accents
affranchis de toute soumission et de toute entrave. **Là-bas, aux dernières frontières des États,
arrêtez-vous et levez les yeux, mes frères : ce que vous voyez sous l'arc-en-ciel, c'est le
passage que franchit l'homme supérieur.**

> ⚠️ **Traduction : celle du manuel, et elle seule.** Le manuel imprime la version arabe de
> **فليكس فارس**, explicitement `( بتصرّف لجنة التأليف )` — remaniée par la commission. Les deux
> phrases ci-dessus rendent l'arabe imprimé
> (`فهنالك يتعالى نشيد الضرورة بنغماته المحررة من كلّ مطاوعة وتقييد` ·
> `هنالك عند آخر حدود الدول، قفوا وتطلّعوا، يا إخوتي، إنّما ترون تحت قوس قزح المعبر الذي يجتازه الإنسان الأسمى.`),
> **pas** les formules du Nietzsche français courant (« la mélodie unique et irremplaçable », « les
> ponts du surhumain » au pluriel, l'interrogation rhétorique) : celles-là ne sont **pas** sur la
> page. ⇒ **Ne jamais générer de question à partir d'une autre traduction** : la مهمّة n° 5
> (`أيّة علاقة يقيمها نيتشه بين فناء الدولة وظهور الإنسان الأسمى؟`) porte sur **ce** texte-ci,
> affirmatif et au singulier (`المعبر`).

**الهامش** (une seule note, verbatim resserré) :

1. **زرادشت** `Zarathoustra` : نبي آري ولد حوالي سنة 630 قبل الميلاد، تنسب إليه الديانة
   الزرادشتية وهو دين معظم الفرس قبل الإسلام، أما اليوم فتدين له أقليات في إيران والهند.
   اختلطت حياته بكثير من الأساطير جعلته أسطورة ورمزا. لا شكّ أن في اختيار نيتشه لزرادشت عنوانا
   لمؤلفه دلالة رمزية إذ يُعرَف عن زرادشت النبي نبوغه ونفوره من العادات والتقاليد فضلا عن دعوته
   لإقامة علاقة محبة وتعاون وصداقة بين الإنسان والآلهة بدل علاقة الخوف.

**الكاتب** : ⚠️ **renvoi, pas de notice** — imprimé verbatim :
**نيتشه : انظر التعريف بالكاتب المصاحب للسند عدد 19 ( الإنيّة والغيريّة )**.

**المهام** (p.290, verbatim) :

- أنتبه إلى الأسلوب الذي كُتب به النصّ وأبيّن طرافته شكلا ممكنا للكتابة الفلسفيّة.
- أستخرج جملة المجازات المتصلة بالدولة وأتبيّن دلالتها الرمزيّة.
- من يحتاج الدولة؟ و لِمَ يحتاجها؟
- هل ابتكر الإنسان الدولة من أجل الإنسان؟
- أيّة علاقة يقيمها نيتشه بين فناء الدولة وظهور الإنسان الأسمى؟
- استعمل الكاتب معجميّة أخلاقيّة في وصف الدولة: ألا يعبّر هذا على خرق للسياسي؟
- هل تفضي مقاربة الكاتب إليّ ضرب من العدميّة السياسيّة؟

**Illustration** : p.289 — **photographie de Nietzsche** (moustache, veste sombre), en médaillon.
p.290 : ⚠️ **aucune illustration, aucun encadré-citation**.

###### سند 8 — مراتب الرئاسة — p.291-292

**التمهيد** (verbatim) :

> لأن واقع البشر لا يرتقي أصلا إلى ما ينشدون، فإنهم لا ينفكون عن الحلم يبحثون فيه عن إمكان
> لمدينة "فاضلة" لا مكان فيها للظلم وحافظة لاستمرار السيادة، لكلٍّ فيها حدُّه، يتوحّد فيها الشيء
> وضدّه؛ مدينة يرضاها العقل كاملةً، تحاكي كمالَ ما هو أصلا في السّماء.

**Référence imprimée** : **الفارابي، السياسة المدنية** — سلسلة " عناصر "، دار سيراس للنشر،.
ص 72—73.

**Thèse (reformulée, R-2)** : dans la cité, les rangs de **رئاسة** et de **خدمة** sont
**hiérarchisés** selon la nature (فِطَر) des habitants et selon l'éducation reçue. Le **chef
premier** (الرئيس الأوّل) ordonne les groupes et assigne à chacun le rang qui lui revient — rang
de service ou rang de commandement — de sorte qu'il existe des degrés plus ou moins proches du
sien, jusqu'aux rangs de pur service sans aucune part de commandement. Le chef, après avoir
ordonné ces degrés, fixe une **وصيّة** pour ce qu'il veut imposer aux habitants et la confie aux
plus proches de lui, qui la transmettent à leur tour à ceux qui les suivent, jusqu'au dernier
serviteur. La cité devient alors **un tout dont les parties sont liées, ordonnées, hiérarchisées
en antériorité et postériorité** — elle **ressemble aux existants** (الموجودات), qui commencent au
Premier et descendent jusqu'à la **matière première** et aux **أسطقسات**, liés eux aussi selon la
même solidarité ; et **le gouvernant de la cité est semblable à la Cause première** par laquelle
existent tous les autres existants. Ainsi les rangs de l'existence s'abaissent-ils
progressivement, chacun étant à la fois chef et subordonné, jusqu'aux existants qui n'ont
**aucune** part de commandement et qui sont purement au service d'autrui : la matière première et
les أسطقسات.

**الهامش** (une seule note, verbatim) :

1. **الأسطقسات** : جمع اسطقس، وهو العنصر غير القابل للقسمة.

**الكاتب — أبو نصر الفارابي (257هـ —870م / 393هـ —950م)** (verbatim resserré) : هو **أبو نصر
محمد بن محمد بن أوزلغ** المعروف باسم الفارابي نسبة إلى مكان مولده (فاراب) وهي مدينة تركية. كان
أبوه فارسيا وأمه تركية. تلقى علومه الأولى في مدينة فاراب. ثم انتقل مع أبيه إلى بغداد فصحب
**متى بن يونس النحوي وابن السراج** وتتلمذ **على يوحنا بن حيلان**. ثم صار من دمشق إلى مصر
(338هـ) ثم رجع إلى الشّام وقدم على سيف الدولة الذي أكرمه وضمه إلى بلاطه حتى مات وله من العمر
ثمانين عاما. لُقّب **بالمعلّم الثاني** بعد أرسطو تعبيرا عن منزلته الخاصة. كان أرسطيا في بعض
آرائه المنطقية والطبيعية وأفلاطونيا في الأخلاق والإلهيات والسياسة دون أن يعني هذا عدم تفرده
بآراء حفظت له مكانة متميزة من بين فلاسفة الإسلام. ترك مؤلفات عديدة منها مقدمات ومختصرات ومنها
شروح وتعليقات ومنها تصنيفات خاصة نذكر منها **"كتاب الجمع بين رأيي الحكيمين أفلاطون وأرسطو"**
وقد تعلّق بمحاولة التوفيق بين آراء هذين الفيلسوفين في الطبيعة والإلهيات وغيرها، توفيقا كان
موضوع نقد. وكتابه **" فصوص الحكم "** وكتاب **" آراء أهل المدينة الفاضلة "** وهو كتاب في السياسة،
في أسس المدينة ومراتبها،. ثم **" كتاب السياسة المدنية "** و**" رسالة في السياسة "** و**" تحصيل
السعادة "** و**" كتاب الموسيقى الكبير ورسالة في إحصاء العلوم "** و**" كتاب الحروف "** وغير ذلك…

**المهام** (p.292, verbatim) :

- أستخرج من النص تصور الفارابي للمدينة وأحدد أساس التراتبية فيها.
- ما هو مدلول السيادة لدى الفارابي وإلى من يجب أن تؤول ؟
- أستخلص من تصوّر الفارابي للسيادة دلالة العدالة.
- هل يمكن أن أستخلص أنّ تصوّر الفارابي يعبّر عن منزع طوباويّ لنظام المدينة ؟

**Encadré-citation (p.292)** : « ومراتب أهل المدينة في الرئاسة والخدمة تتفاضل » — **الفارابي**.

**Illustrations** : p.291 — **portrait enluminé d'al-Fârâbî** (turban bleu, barbe blanche), en
médaillon. p.292 — tableau orientaliste, légende imprimée en français :
`Benjamin CONSTANT, Présents d'un pacha. Mulhouse, Musée des Beaux-Arts.`
⚠️ **Homonymie à ne pas confondre** : ce **Benjamin Constant** est le **peintre** Jean-Joseph
Benjamin-Constant, pas le **كونستون** auteur du سند 10.

###### سند 9 — الراعي والرعيّة — p.293-294

**التمهيد** (verbatim) :

> الدولة، كسائر الأجسام، عرضة للأمراض والعلل. علّتها العضال انقلاب السلطة إلى تسلّط وتحوّل
> القوّة إلى استقواء. وجرى المثل " كما تكونون يُولَّى عليكم " دليلا على استكانة في الرعيّة تقبل
> معه جور السلطان.

**Référence imprimée** : **الكواكبي، طبائع الاستبداد** — دار النفائس، بيروت. 1984. ص 52 — 53.

**Thèse (reformulée, R-2)** : le **peuple (العوام)** est la force et la puissance même du
despote : c'est par lui qu'il les assaille, et par eux qu'il domine les autres. Le mécanisme est
une **complicité** : il les capture et ils l'acclament, il confisque leurs biens et ils le
remercient de leur laisser la vie, il les humilie et ils vantent son élévation, il les dresse les
uns contre les autres et ils s'enorgueillissent de sa politique ; s'il dilapide leur argent, ils
disent « il est généreux », s'il tue sans mutiler ils le disent « clément », et il les conduit au
danger de mort et ils lui obéissent par crainte du châtiment — et si quelques **أباة** se
révoltent, la foule les tue elle-même comme s'ils étaient des **بغاة**. Le ressort de tout cela
est **l'ignorance** : le peuple s'égorge de ses propres mains par une peur née de l'ignorance ;
que l'ignorance se lève et la peur disparaît, et **la situation se renverse** — le despote se
mue, en dépit de sa nature, en un intendant honnête qui redoute les comptes, un chef juste qui
craint la vengeance, un père indulgent qui prend plaisir à l'affection. Alors la nation obtient
une vie agréable et douce, prospérité et croissance, gloire et bonheur ; et **le gouvernant y
gagne le plus grand des lots**, lui qui, au temps du despotisme, était le plus malheureux des
hommes, perpétuellement entouré d'ennemis, guetté par la haine, jamais sûr de sa vie un instant.
Car — c'est la thèse centrale — **la peur qu'a le despote de son peuple est plus grande que la
peur qu'a le peuple de sa violence** : sa peur à lui naît d'un **savoir**, la leur d'une
**ignorance** ; il craint une vengeance légitime, ils craignent son emportement ; il craint de
perdre sa vie et son pouvoir, ils craignent pour des miettes de nourriture et pour une patrie que
d'autres, en quelques jours, sauront habiter à leur place. Et plus le despote accroît injustice
et arbitraire, plus grandit sa peur — de ses sujets, de son entourage, et jusqu'à ses propres
hantises et fantasmes ; souvent la vie des despotes faibles de cœur s'achève dans la **folie**.

**الهامشان** (verbatim) :

1. **أباة** : جمع آبٍ وهو الأبيّ أي من يترفّع عن الدنايا وهو أيضا من يعتزّ بنفسه.
2. **بُغاة** : جمع باغٍ وهو الباغي أي الظالم والخارج على القانون.

**الكاتب — عبد الرحمان الكواكبي (1842 — 1902)** (verbatim resserré) : ولد في مدينة حلب. تلقى
دروسه الأولى في حلب وفي أنطاكية تعلم العربية والفارسية وعلوم الدين واطلع على أمهات الكتب في علوم
الطبيعة والرياضيات والتاريخ والفلسفة… واطلع على تراجم لكتب بلغات أجنبية خاصة في مجال السياسة…
شارك في الحياة العامة كصحفي ومحرر في جريدة **" الفرات "** ليصدر صحيفتين **" الشهباء "** و**"
الاعتدال "** نشر فيهما أفكاره الإصلاحية فأزعج السلطات التركية فأقفلت جريدته بعد صدورها بخمسة
أشهر في عام 1887. تقلّد الكواكبي مناصب متعددة واشتغل في المشاريع العمرانية والتجارية. هاجر وتنقل
في سواحل إفريقيا الشرقية والغربية وسواحل آسيا وبلاد العرب والهند حتى سواحل الصين. استقر أساسا
بمصر. اتصل بمعاصريه من رجالات الإصلاح ( محمد رشيد رضا ومحمد كرد علي وغيرهما ). وفي هذه المرحلة
ألّف الكواكبي كتابيه المهمين : **" طبائع الاستبداد "** الذي حلل فيه ظاهرة الاستبداد في صلتها
بالمال والأخلاق والدين وغيرها… ثم كتابه **" أم القرى "** الذي بين فيه أحوال المسلمين وآراءه في
الإصلاح… و في سنة 1902 توفي في القاهرة متأثرا بسم دُسَّ في طعامه بإيعاز من الأتراك.

**المهام** (p.294, verbatim) :

- أتقصّى مظاهر الاستبداد واستتباعاته كما وردت في النص.
- كيف يفسّر الكاتب الاستبداد؟ هل يردّه إلى الرّاعي أم إلى الرعيّة؟
- هل من مستفيد من الاستبداد؟
- هل الاستبداد طبيعة متأصّلة في الدولة أم هو عارض يتّصل بنظام الحكم؟
- هل من حقّ الإنسان أن يقاوم الاستبداد؟ هل من حدود لهذه المقاومة؟
- ما هي شروط الإصلاح السياسي في نظر الكاتب؟ أحدّد مدى وجاهتها في القضاء على الاستبداد.
- هل في تاريخ البشريّة ما يشهد بقبولها للاستبداد أم برفضه؟ أدعّم جوابي بشواهد مختلفة.
- فيمَ تساعدني مقاربة الكاتب على التمييز بين " الرعيّ " و" المواطن "؟

**Illustration** : p.293 — **portrait peint d'al-Kawâkibî** (turban blanc, barbe noire, habit
sombre), en médaillon. p.294 : ⚠️ **aucune illustration, aucun encadré-citation**.

###### سند 10 — في الديمقراطيّة — p.295-296

**التمهيد** (verbatim) :

> تستند الديمقراطيّة على إرادة الشعب وسيادته: يبدو أن هذا أمر محلّ إجماع. لكن أن نجعل سيادته
> مطلقة وغير قابلة للمراجعة، هذا شأن آخر نخشى معه أن نخسر ما جعلنا سلطة الشعب أمينة عليه:
> " حريتنا الشخصيّة ".

**Référence imprimée** : **كونستون ، في الحرية عند المحدثين** — `Benjamin CONSTANT; De la liberté
chez les modernes, éd, Pluriel, Paris 1980`.

⚠️ **Graphie du nom** : le manuel imprime **كونستون** (et non كونستان) partout — dans le corps du
texte, la notice et l'encadré-citation. À conserver telle quelle.

**Thèse (reformulée, R-2)** : reconnaître à la souveraineté du peuple des **limites** n'est pas
la nier — c'est la sauver. Quand on admet qu'elle est **sans bornes**, on crée et on jette dans
la société un degré **excessif** de puissance, un mal en soi **quelles que soient les mains** qui
le détiennent : qu'on le confie à un seul homme, à un groupe ou à tous, on le trouvera également
mauvais. Ce sont les **dépositaires** qu'on accusera, et ils se succéderont selon les
circonstances — monarchie, aristocratie, démocratie, gouvernements mixtes, régime représentatif —
mais l'accusation portera à faux : **ce qu'il faut condamner, ce n'est pas les dépositaires du
pouvoir, c'est son degré**. Il faut frapper l'arme, non le bras qui la tient. Ceux qui, de bonne
foi et par amour de la liberté, ont accordé à la souveraineté du peuple un pouvoir **sans
frontières** se sont trompés par la manière dont leurs idées se sont formées en politique : ils
avaient vu dans l'histoire un petit nombre d'hommes, voire un seul, détenir un pouvoir énorme et
en abuser — mais leur colère s'est portée sur **les détenteurs** du pouvoir et non sur **le
pouvoir lui-même** ; au lieu de le détruire, ils n'ont songé qu'à le **déplacer**. Ce fut une
catastrophe qu'ils prirent pour une conquête : ils ont fait don du pouvoir à la société tout
entière — et naturellement il a transité de la société vers la **majorité**, puis s'est concentré
entre les mains de quelques personnes, souvent d'une seule, et il a commis autant de mal qu'avant.
La conclusion : **il n'existe de souveraineté que limitée et relative**. Là où commence
l'indépendance et l'existence **personnelle** de l'individu s'arrête la juridiction de cette
souveraineté ; si la société franchit cette ligne, elle se rend **plus coupable que le despote**,
lequel n'a d'autre argument que le sabre tranchant — la société ne peut outrepasser sa compétence
sans être **usurpatrice**, ni la majorité sans être **conspiratrice**.

**الهوامش** : ⚠️ **aucun** encadré de note.

**الكاتب — كونستون (1767-1830)** (verbatim resserré) : فيلسوف وروائي ورجل سياسة فرنسي من أصل
سويسري،. لعب دورا سياسيا أكّد فيه معارضته لنابليون وشغل منصب الأمانة العامة للحزب الليبرالي وحظي
بشعبية كبيرة. من مؤلفاته كتاب **" في الحرية عند المحدثيّن "** (1818) الذي عرض فيه الخصائص
المميزة للحرية في معناها الحديث التي تقوم على عدم التعارض بين حرية الفرد ومقتضيات الوجود
الاجتماعي مؤكدا على قيمة **فولتير** كنموذج للحرية في معناها الحديث؛ كما ألف **" الحرية بين
القدامى والمحدثين "** (1819) الذي كشف فيه عن موقفه الليبرالي عارضا مشاهد الرعب التي ميزت فرنسا
سنة 1793 وما تولّد عنها من آلام مؤكدا على تعارضها مع مبادئ الثورة الفرنسية المستوحاة من كتابات
روسو، كما صدر له كتاب **" الدين مأخوذ في أصله وأشكاله وتطوراته "** (1824—1830) دون أن يتمكن من
إتمامه وقد أكّد فيه على الطابع الكوني للظاهرة الدينية وعلى منزلة الدين بما هو قانون أساسي
للطبيعة الإنسانية واعتبره صرخة الروح تجاه المجهول واللانهائي.

**المهام** (p.296, verbatim) :

- ما نسبة سيادة الشعب إلى النظم الديمقراطيّة؟
- ما دلالة سلطة الشعب وما وجه اعتراض الكاتب عليها؟
- ما الغنم الحاصل من الحدّ من سيادة الشعب في نظر الكاتب؟
- كيف يمكن أن يتحقّق التوافق بين السيادة والمواطنة؟
- ما منزلة الأقليّة في حكم الأغلبيّة؟
- "إنسانيّتي " و" مواطنتي ": أيّهما يستلزم الآخر؟

**Encadré-citation (p.296)** : « لا توجد السيادة إلاّ على نمط محدود ونسبي » — **كونستون**.

**Illustrations** : p.295 — **portrait peint de Benjamin Constant** (habit et cravate
XIX<sup>e</sup>), en médaillon. p.296 — photographie d'un **hémicycle parlementaire** en séance.

###### سند 11 — الدولة والشرعيّة — p.297-298

**التمهيد** (verbatim) :

> تعمل كلّ سلطة على تبرير ذاتها حتى يكون لنفوذها القول الفصل فيما يتعلّق بالشأن الإنساني،
> والتمست في ذلك أكثر من سبيل. وكثيرا ما نذهل نحن جميعا، حكّاما ومحكومين، عن كون السلطة، مهما
> بحثنا لها عمّا يشرّعها، تبقى ممارسة؛ ولأنّها ممارسة، يحسن أن ننشدّ إلى أسلوب عملها قبل النظر
> في صفاء حسبها ونبل غرضها.

**Référence imprimée** : **تزفيتان تودوروف، اللانظام العالمي الجديد** — ترجمة وليد السويركي؛
أزمنة، عمّان. ص 52 — 53.

**Thèse (reformulée, R-2)** : qu'est-ce qui rend une politique **légitime** ? Ce n'est pas la
simple **possession** du pouvoir — celui-ci s'obtient le plus souvent par la **violence** (la
guerre d'indépendance a précédé la démocratie américaine comme la révolution de **1789** a précédé
la démocratie française). Et même lorsque le pouvoir est légitime en tant qu'expression de la
**volonté populaire**, il peut s'égarer : l'avis de la **majorité** n'est pas nécessairement
l'avis **éclairé**, et il peut aller à l'encontre de l'esprit de **justice**. La légitimité ne
vient pas non plus des **fins**, si nobles soient-elles, que nous nous fixons nous-mêmes : il y a
toujours le soupçon que les puissants brandissent ces fins pour masquer leurs convoitises réelles.
Où réside donc la légitimité ? Tudorov reprend **Montesquieu** : *« tout pouvoir sans limites ne
saurait être légitime »*. Ce n'est ni l'origine du pouvoir ni sa finalité qui lui confère
légitimité, mais **la manière dont il s'exerce** — c'est-à-dire le fait qu'il **s'impose à
lui-même des bornes** en le **partageant** avec d'autres. Deux conceptions s'affrontent :
l'une relève de l'**unité**, l'autre de la **pluralité** ; la première croit détenir le bien et
en conclut qu'elle a le droit de l'imposer à tous ; la seconde espère elle aussi être la
meilleure, mais **s'y refuse** et estime que le partage et la séparation des pouvoirs valent mieux
que leur réunion — plusieurs partis valent mieux qu'un seul, **même si ce seul était le
meilleur**. À l'intérieur de l'État, la limitation vient de l'**indépendance** des pouvoirs
exécutif, législatif et judiciaire, du **pluralisme partisan**, de la **pluralité des sources
d'information** et de la **reconnaissance des droits des minorités**. À l'échelle
**internationale**, elle vient du respect de la **souveraineté des autres États** — même quand on
a les moyens de les soumettre — et du respect des **accords et traités** — même quand on a les
moyens de les violer. Accepter cette pluralité est le meilleur moyen de protéger
l'**indépendance de chacun** et de s'assurer, à terme, son soutien.

**الهامشان** (verbatim) :

1. **منتسكيو** `(1689 — 1755) Montesquieu`، كاتب ومفكّر فرنسي من عائلة ثريّة يعدّ من مؤسّسي علم
   الاجتماع السكوني، مكّنته سفراته المتعدّدة إلى البلدان الأوروبيّة من التعرّف على مختلف النظم
   السياسيّة وتبيّن أساليب إدارة الحكم ممّا مكّنه من تأليف أهمّ كتبه **" روح القوانين "** (1748)
   الذي حرص فيه على بيان معقوليّة التنوّع التاريخي وتحليل أسس نظم الحكم. من كتاباته أيضا
   **" رسائل فارسيّة "** (1721).
2. ورد في **" رسائل فارسيّة "** لمنتسكيو

*(⚠️ la note 2 est **imprimée sans point final** et sans énoncé complet — elle indique seulement
la provenance de la citation de Montesquieu.)*

**الكاتب** : ⚠️ **renvoi, pas de notice** — imprimé verbatim :
**تزفيتان تودوروف : انظر التعريف بالكاتب المصاحب للسند عدد 8 ( الخصوصيّة والكونيّة )**.

**المهام** (p.298, verbatim) :

- أحدّد المشكل الذي يثيره الكاتب وأتبيّن قيمته.
- أحدّد المواقف التي يستبعدها الكاتب وأتبيّن الحجج التي ساقها في ذلك.
- أعود إلى موقف منتسكيو وأفكّر في قيمة استحضاره من طرف الكاتب.
- ما هو المبدأ الذي تستمدّ منه السلطة شرعيّتها في نظر الكاتب؟
- يميّز الكاتب بين اتّجاهين، يقول الأول بالوحدة والثاني بالتعدّدية: أحلّل حقيقة الفارق بينهما.
- ما هي شروط السياسة الشرعيّة التي يحدّدها الكاتب؟
- هل من تعارض بين شروط سياسة شرعيّة داخلية وشروط سياسة شرعيّة على المستوى الدولي؟
- هل تساعدني مواقف الكاتب على تعقّل بعض ظواهر الوجود الإنساني؟ أحرّر فقرة في الغرض.
- هل أميل إلى القول بالوحدة أم بالتعدديّة؟ أبرّر جوابي.

**Encadré-citation (p.298)** : « يأتي تحديد السلطة، داخل الدولة، من استقلاليّة كلّ من السلطات
التنفيذيّة والتشريعيّة والقضائيّة…. من التعدديّة الحزبيّة وتعدّد مصادر المعلومات ومن الإقرار
بحقوق الأقليات » — **تودوروف**.

**Illustrations** : p.297 — **photographie de Tzvetan Todorov** (cheveux blancs, lunettes), en
médaillon. p.298 — photographie d'une **manifestation** portant une banderole en français
`LIBERTÉ CHÉRIE !`.

###### سند 12 — الحقّ والقانون — p.299-300

**التمهيد** (verbatim) :

> الإفراط في السّلطة والتفريط في الحقّ: حدّان يشغلان الإنسان ويرسمان مجال عِراكه السياسي المنفتح
> دوما على الممكن. عراك يغذّيه أمل الإنسان في اعتدالٍ يقرّ للسّلطة حقّها ويؤمّن للحقّ سلطتَه في
> فضاء سياسي يعمّره مواطنون أحرار لا رعايا مستعبدين.

**Référence imprimée** : **سبينوزا، رسالة في اللاّهوت والسياسة، الفصل 16** — ترجمة . حسن حنفي؛
مراجعة . فؤاد زكريا — دار الهيئة المصريّة العامّة للتأليف والنشر، 1977. ص 384— 385.

**Thèse (reformulée, R-2)** : chaque individu doit **déléguer** à la société toute la puissance
qu'il détient, de sorte que la société possède **seule** le droit naturel absolu sur toute chose,
c'est-à-dire le pouvoir souverain de donner les ordres auxquels chacun doit obéir — soit par
libre choix, soit par crainte du châtiment sévère. Un tel régime s'appelle **démocratie** : elle
est l'**union des hommes en un corps qui détient collectivement un droit absolu sur tout ce qui
est en son pouvoir**. Il en résulte que le détenteur du pouvoir n'est lié par **aucune loi** et
que tous lui doivent obéissance en tout, car ils lui ont délégué — par contrat exprès ou tacite —
toute la puissance qu'ils avaient de se conserver, c'est-à-dire leur droit naturel. S'ils avaient
voulu en garder une part, ils auraient dû se donner en même temps les moyens de la défendre ; ne
l'ayant pas fait, sans quoi la discorde eût éclaté et le pouvoir se serait effondré, ils se sont
soumis à la volonté du souverain, **quelle qu'elle soit**. Mais — c'est le renversement — *le
gouvernant n'acquiert le droit d'ordonner ce qu'il veut qu'**autant qu'il détient réellement le
pouvoir suprême** ; s'il le perd, il perd du même coup le droit d'ordonner, et ce droit passe à
celui — ou à ceux — qui sont capables de s'en emparer et de le conserver.* Voilà pourquoi il est
**rare** que les gouvernants donnent des ordres pleinement contradictoires : leur intelligence et
leur souci de conserver le pouvoir les conduisent à veiller au maximum sur l'**intérêt général** et
à conduire toutes choses selon les **jugements de la raison** — car, comme on l'a dit, nul n'a pu
gouverner longtemps par la **violence**. Quant à l'**État** — le régime où l'intérêt de celui qui
commande **n'est pas** pris pour loi suprême, mais qui veille au contraire à l'intérêt du peuple
**tout entier** — le devoir y est de ne pas compter pour **esclave** celui qui lui obéit, comme
s'il n'y trouvait pas son intérêt propre, mais de le tenir pour **citoyen**. Sur cette base, **les États les plus libres sont
ceux dont les lois s'appuient sur la saine raison** — car chacun y peut, s'il le veut, être libre,
c'est-à-dire vivre par pur choix selon la raison. De même, les **enfants** ne sont pas des
esclaves bien qu'ils doivent obéir aux ordres de leurs parents, parce que les ordres des parents
visent l'intérêt de l'enfant avant tout. La distinction se formule ainsi : **l'esclave** est
contraint d'obéir à des ordres qui servent l'intérêt du maître ; **le fils** exécute des ordres
de ses parents qui servent son propre intérêt ; **le citoyen** exécute les ordres du gouvernant,
lesquels servent l'intérêt **général** — et par conséquent son intérêt propre.

> ⚠️ **Le pivot du سند, à ne pas retourner.** La phrase sur l'État est une **définition positive**
> du régime légitime, pas la description d'un mauvais régime. Texte imprimé (p.299) :
> `أمّا الدولة ونظام الحكم الذي لا تؤخذ فيه مصلحة الأمر بوصفها قانونا أسمى، بل يراعي مصلحة الشعب كله`
> `— فمن الواجب ألاّ يُعدّ من يطيعه عبدا لا يحقّق مصلحته الخاصّة، بل مواطنا.`
> La négation `لا تؤخذ` porte sur **l'intérêt du gouvernant** (il n'est *pas* pris pour loi suprême)
> et `بل يراعي مصلحة الشعب كله` dit ce que ce régime fait **au contraire**. C'est la clé de la 7ᵉ
> مهمّة (`ما وجه التمييز بين العبد والطفل والمواطن؟`) : dans **cet** État-là, celui qui obéit est
> **citoyen**, non esclave.

**الهوامش** : ⚠️ **aucun** encadré de note.

**الكاتب** : ⚠️ **renvoi, pas de notice** — imprimé verbatim :
**سبينوزا : انظر التعريف بالكاتب المصاحب للسند عدد 11. ( الإنيّة والغيريّة )**.

**المهام** (p.300, verbatim) :

- عن أيّ تفويض يتحدّث الكاتب؟ أستثمر ما ورد في نافذة دعائم للتفكير في المسألة، سياقات فكريّة،
  فلسفات التعاقد.
- كيف يعرّف الكاتب الديمقراطيّة؟ أحدّد مستلزمات ممارسة السلطة التي تلائمها.
- حقّ الفرد والمصلحة العامّة: هل من تعارض بينهما في دولة ديمقراطيّة؟
- هل في الخضوع للقانون نفي للحريّة؟
- أيّة علاقة بين سيادة القانون وسيادة العقل؟
- " لم يستطع أحد أن يستمرّ في الحكم طويلا عن طريق العنف ": أحلّل هذا الحكم وأمتحن راهنيّته.
- ما وجه التمييز بين العبد والطفل والمواطن؟
- أستخلص مفهوم المواطن ومنزلته في الدولة الديمقراطيّة.

**Encadré-citation (p.300)** : « تكون أكثر الدول حرية تلك التي تعتمد قوانينها على العقل السليم »
— **سبينوزا**.

**Illustrations** : p.299 — **portrait gravé de Spinoza** (cheveux longs, col blanc), en
médaillon. p.300 — nature morte : **codes juridiques rouges** (`CODE CIVIL`), livre ouvert,
lunettes et **balance** dorée.

> 🔎 **Troisième renvoi à la نافذة دعائم** : la 1<sup>re</sup> مهمّة de ce سند renvoie à
> **سياقات فكريّة, فلسفات التعاقد** (au pluriel ici ; le سند 5 écrivait *فلسفة التعاقد*).

###### سند 13 — حريّة الرأي — p.301-302

**التمهيد** (verbatim) :

> إذا كانت الحياة داخل المجتمع شرط تحقّق إنسانية الإنسان فإنّ الانصياع كليّة إلى قوانين سلطة
> المجتمع وضوابطه قد يصادر حق الفرد، وحق الأقلية في الاختلاف، باسم أغلبيّة حقيقيّة أو مزعومة،
> مما يقتضي رسم حدود حقّ السلطة اعترافا بحق امتلاك حيز شخصي للحياة.

**Référence imprimée** : **ستيوارت ميل، الحرية (الفصل الثاني)** — عن " الفلسفة الحديثة: نصوص
مختارة "، ط: أفريقيا الشرق، ص 113. ترجمة: محمد سبيلا وعبد السلام بن عبد العالي.

**Thèse (reformulée, R-2)** : à supposer même un gouvernement en **accord complet** avec le
peuple, et qui ne songerait à imposer son pouvoir que par la volonté même du peuple, Mill nie
que le peuple ait **le droit** d'exercer ce pouvoir, qu'il l'exerce lui-même ou par son
gouvernement : un tel pouvoir est **illégitime en soi**. Il n'est pas plus légitime chez le
meilleur gouvernement que chez le pire — il est même plus nuisible, et plus nocif encore
lorsqu'il s'impose en **accord** avec l'opinion publique que lorsqu'il la contredit. **Si
l'humanité entière, à l'exception d'un seul homme, partageait un avis, et que cet homme seul
soutenait le contraire, l'humanité n'aurait pas plus le droit de lui imposer le silence que lui
n'aurait le droit d'imposer le sien si le pouvoir était entre ses mains.** Et si une opinion
n'avait de valeur que pour son auteur, en sorte que l'empêcher d'en jouir ne nuirait qu'à lui,
il resterait une différence entre le préjudice qui frappe **le plus grand nombre** et celui qui en
frappe **le plus petit**. Mais empêcher l'homme d'exprimer son opinion est un **mal**, car c'est
dépouiller **l'humanité tout entière** — les générations futures autant que la génération
présente, et ceux qui contestent cette opinion plus encore que ceux qui l'acceptent. Car **si
l'opinion est vraie**, on les prive de la chance d'échanger l'erreur contre le vrai ; **si elle
est fausse**, ils perdent un avantage non moins grand — la perception plus claire et plus vive de
la vérité, produite par le **choc de la vérité avec l'erreur**.

**الهوامش** : ⚠️ **aucun** encadré de note.

**الكاتب — ستيوارت ميل (1806 — 1873 )** (verbatim resserré) : فيلسوف وعالم اقتصاد أنجليزي ،
امتلك ثقافة تاريخية واسعة وتشبّع بدراسة العلوم والقانون. كان للثورة الفرنسية سنة 1830 دور في
إنتاج تيار سياسي ليبرالي النزعة في بريطانيا وعُدَّ ميل أحد أبرز رموزه؛ ظل إلى عدة أعوام يكتب في
صحف تتسم بطابع ليبرالي راديكالي. أشرف طيلة خمس سنوات على إدارة مجلة لندن ووستمنستر الناطقة بلسان
الحزب الراديكالي. تميز ميل بوفرة عطائه، وانكبابه الدائم على العمل والتأليف. من أهم أعماله
**" مذهب المنطق "** (1843)، **" في النفعية "** (1863)، و**" فلسفة ويليام هاملتون "** (1865)، ثم
**" أوغيست كونت والوضعية "** (1865) وفيه جدد المذهب التجريبي على أساس السيكولوجيا، وفي الأخلاق،
عدّل نفعية بنتام ليكيفها مع القانون والسياسة. كتب أيضا **" مقالات في بعض مشاكل الاقتصاد
السياسي "** (1844) و**" مبادئ الاقتصاد السياسي "** (1848)، وفيهما عرض لمبادئ الاقتصاد السياسي،
منظورا إليه بوجه خاص من خلال تطبيقاته على قضايا العصر السياسية والاجتماعية الكبرى. أصدر أيضا
كتاب **" الحرية "** (1859)، وهو كتاب مفعم بالنزعة الليبرالية. شارك في سياسة بريطانيا
وانتُخِب عضوا في مجلس العموم (1865)، وأثار على منبره مسألة حق النساء في الانتخاب وهي مسألة كان
قد طرحها في كتابه **" عبودية النساء "** (1861) الذي أصدره سنة 1869 وهو بمثابة إعلان عقلاني
وبليغ عن الوضع الفعلي للمرأة في التاريخ، وبمثابة هجوم على الاستعباد القانوني التي هي من ضحاياه،
وعلى الأخلاق الإكراهية التي ترغمها على الخضوع للرجل.

*(⚠️ **incohérence imprimée** : le livre `" عبودية النساء "` est daté **(1861)** puis dit publié
**سنة 1869** dans la même phrase. Constat, pas correction.)*

**المهام** (p.302, verbatim) :

- بأيّ معنى ينكر الكاتب على الشّعب الحق في فرض سلطته؟
- ما وجه الضرر في منع الفرد من التعبير عن رأيه؟
- أيّ غُنُم يمكن أن يترتّب على تمكين الفرد من حقّه في التعبير عن رأيه؟
- هل من حقّ سلطة الأغلبيّة أن تقصي حقوق الأقليّات؟ أعلّل جوابي في فقرة قصيرة.
- هل يمكن أن نتصوّر حدّا لحقّ الفرد في التعبير عن رأيه دون إخلال.بمقوّمات النظام الديمقراطي؟

**Encadré-citation (p.302)** : « ولكن منع الإنسان من التعبير عن رأيه شر، لأنّ فيه سلب الإنسانية
كلها » — **ميل**.

**Illustrations** : p.301 — **portrait gravé de John Stuart Mill**, en médaillon. p.302 —
illustration : trois écoliers dont la **bouche est fermée par un cadenas**, une clé et une pomme
rouge tendue au-dessus d'eux.

###### سند 14 — الحقّ والعنف — p.303-304

**التمهيد** (verbatim) :

> كثيرا ما نرفض العنف باسم الحق ونعتبرهما ضدّين لا يجتمعان. ومع هذا قد يحتاج أحدهما الآخر حين
> تقضي الظروف وصلا بينهما لتحقيق غرض لا يؤمّنه الفصل.

**Référence imprimée** : **إيف ميشو، العنف والسياسة، 1978** — `Yves MICHAUD; Violence et
politique, Gallimard. 1978. pp 127 - 129`.

**Thèse (reformulée, R-2)** : on comprend toujours le droit, dans son principe, comme
l'**exclusion de la violence** — ce qui rend légitimes certaines fins, c'est l'usage de moyens
que la **loi** autorise, et la violence ne peut exister qu'**en dehors** du droit. Il subsiste
pourtant une **frayeur** que la violence traverse le droit, lequel l'écarte au nom d'un principe
de **paix des rapports**. Mais il apparaît vite que le droit **redoute** dans la violence le
dommage qu'elle inflige à la paix **moins** qu'il ne redoute la **possibilité d'être violé**.
L'**appareil judiciaire** est l'un des moyens — peut-être le plus efficace — de se prémunir contre
la **vengeance** interminable. Or son principe de justice **contraignante** libère les hommes du
devoir de vengeance tout en étant lui-même, **en son fond, une vengeance** — mais une vengeance
si dense et si puissante qu'elle ne laisse place à aucune contre-vengeance ni à aucune
alimentation de la violence. Là où rites et sacrifices travaillent à empêcher la violence en
« l'adoucissant, en l'évitant, en l'orientant vers un but secondaire », le **droit la rationalise,
la divise et en fait une technique thérapeutique cachée** — c'est-à-dire, lui aussi, **un système
violent contre la violence**. Pour que le droit remplisse sa fonction, cela doit rester
**dissimulé** : nous devons le percevoir comme concerné par la **justice**, et non le percevoir
comme une violence semblable à celle qu'il réprime. C'est pour cette raison que le droit **ne
tolère pas** qu'existe un champ où il puisse être enfreint ; c'est pour cette raison aussi qu'il
doit apparaître **inviolable**. En ce sens, les peines rendent au droit sa **plénitude** : la
férocité des châtiments et l'enflure de l'administration de la loi ont pour fonction de
**montrer l'incongruité du droit** et les défis qui lui sont lancés — **il faut que la force
reste à la loi**.

**الهوامش** : ⚠️ **aucun** encadré de note.

**الكاتب — إيف ميشو : (1944)** (verbatim resserré) : فيلسوف فرنسي معاصر، يُعدُّ مختصّا في فلسفة
**هيوم ولوك** والفلسفة السياسيّة عامّة وبصورة خاصة حول ظاهرة العنف.. نشر العديد من المؤلفات منها
بالخصوص **" العنف "** (1973) و**" العنف والسياسة "** (1978) تناول فيهما العلاقة بين العنف والحق
ومنزلة العنف في الحياة السياسية؛ له أيضا **" تغيّرات في العنف "** (2002) قدّم فيه تشخيصا للواقع
مؤكّدا على المفارقات التي تميز واقعنا المعاصر، واقع تقلص فيه العنف مع أن حضوره أصبح أكثر شدة،
وتيسرت فيه ظروف الحياة ولكنها أصبحت في نفس الوقت أشد عسرا. أمّا كتاب **" إنساني، لا إنساني، مفرط
في الإنساني "** (2002) فقد تناول واقع الإعلام والإشهار الذي ينقلنا إلى واقع سائل وغازي يمنحنا
اللذة وضربا من الرفاه ولكننا مع ذلك نعيش في الغامض واللامحدد.

**المهام** (p.304, verbatim) :

- أحدّد معنى القول " الحق نظام عنيف ضد العنف ".
- ما الذي يحرص الحق على إخفائه؟ هل يعبّر بذلك عن خشيته على نفسه من العنف؟
- كيف أفهم قول الكاتب بأن حرص الحق على الانتصار على العنف أكثر من حرصه على السلم؟
- كيف يكون العنف تقنية علاجية ؟ أستحضر أمثلة عن ذلك.
- أحدّد الفرق بين القوة والعنف. وأبيّن هل يمكن للحق أن يكون نافذا دون قوة.

**Encadré-citation (p.304)** : « يُفهم الحق دوما من جهة مبدئه بصفته إقصاء للعنف » — **إيف ميشو**.

**Illustrations** : p.303 — **photographie d'Yves Michaud** (cheveux gris, chemise bleue), en
médaillon. p.304 — dessin stylisé d'un **juge en robe brandissant un maillet** derrière son
pupitre.

###### سند 15 — في نقد الحقّ — p.305-306

**Auteur tel qu'imprimé** : titre du bloc `الكاتب` → **ماركس** ; ligne de référence →
**كارل ماركس**.

**التمهيد** (verbatim) :

> يُدرَك الإنسان بحقّه، أمّا التشريع فيُفترض فيه أنّه ما به يُكتَسب الحقّ تأنيسا فعليّا للإنسان.
> ومن الغريب أن يغفل التشريع عن تحديد المقصود بالإنسان وتنزيله في سياق عيشه وضغط ظرفه. إذا صحّ
> هذا ألا تتحوّل غرابة النسيان إلى اغتراب للإنسان؟

**Référence imprimée** (verbatim) :

> **كارل ماركس**، المسألة اليهوديّة
> ترجمة . نايلة الصالحي، منشورات الجمل، ألمانيا، 2003. ص 37—41 (بتصرّف لجنة التأليف)
> `Karl MARX; La question juive, 1844. in '' Pages choisies" par M. Rubel, Rivière, p 165`

**Les trois articles cités par le manuel** (reproduits textuellement p.305 — ils occupent près de
la moitié de la page et portent directement 3 des 7 مهامّ) :

> **المادة 2** : « هذه الحقوق (الحقوق الطبيعية والحقوق التي لا تسقط بالتقادم) هي : المساواة، الحريّة، الأمن، والملكيّة ».
> **المادة 6** : « الحريّة هي القدرة التي للإنسان على فعل ما لا يُلحق ضررا بحقوق الآخرين » — ou, selon la formule de l'**إعلان حقوق الإنسان لسنة 1791**, « القدرة على فعل ما لا يلحق ضررا بالآخرين ».
> **المادة 16 (دستور 1793)** : « إن الحقّ في الملكيّة هو الحقّ الذي لكلّ مواطن في أن يتمتّع بممتلكاته والتصرّف فيها على هواه، بعائداته، بثمرة عمله وجهده ».

La limite que la loi trace à la liberté est imagée par le manuel : `كما يرسم وتدُّ السّور الحدودَ
بين حقلين` — « comme le piquet d'une clôture trace la limite entre deux champs ».

**Thèse (reformulée, R-2)** : les « droits de l'homme », distingués des droits du citoyen, ne
sont que les droits du membre de la **société bourgeoise** — l'homme **égoïste**, séparé de
l'homme et de la communauté ; la liberté qu'ils consacrent (art. 2, 6 et 16 ci-dessus, de la
Constitution de 1793) se fonde sur la **séparation** des hommes, non sur leur lien, et trouve son usage
pratique dans la **propriété privée**. L'émancipation politique fait donc de la communauté
politique un simple **moyen** de conserver ces droits et du **citoyen le serviteur** de l'homme
égoïste : l'homme réel y est le **bourgeois**, non le citoyen.

**الهوامش** : ⚠️ **aucun** encadré de note — ni p.305 ni p.306.

**الكاتب** : ⚠️ **renvoi**, pas de notice. Imprimé (verbatim) :
**ماركس : انظر التعريف بالكاتب المصاحب للسند عدد 18 ( الإنيّة والغيريّة )**
→ renvoie au سند 18 du **مبحث الإنيّة والغيريّة** (محور 1), pas au سند 18 du présent مبحث.

**المهام** (p.306, verbatim) :

- من هو الإنسان المتميز عن المواطن حسب النص؟
- ما دلالة الحق في الحرية؟ وما علاقة هذا الحق بالحق في الملكية؟
- من هو إنسان حقوق الإنسان؟
- ما المواطن؟ وما منزلته في إعلان حقوق الإنسان؟
- هل ينبغي أن نستبدل الحديث عن حقوق الإنسان بالحديث عن حقوق المواطن؟
- هل يفيد نقد حقوق الإنسان نقد فكرة الحق ذاتها؟
- أي صورة للإنسان يدافع عنها الكاتب؟

**Encadré-citation (p.306)** : « فلا يتجاوز أيّ ممّا يُسمّى حقوق الإنسان، الإنسان الأناني….
وأخيرا يصبح الإنسان الحقيقي في الواقع ليس الإنسان بما هو مواطن ولكن الإنسان بما هو بورجوازي » —
**ماركس**.

**Illustrations** : p.305 — **portrait photographique de Karl Marx** (cheveux et barbe blancs),
en médaillon en tête de texte. p.306 — photographie couleur : un **passeport bleu de
l'ONU** (emblème du globe et rameaux d'olivier) pincé dans la mâchoire d'un **pied à coulisse**
métallique, sur fond noir.

**Constats de mise en page** : le سند occupe **deux pages**, mais le texte déborde jusqu'au tiers
haut de la p.306 ; `الكاتب` (renvoi) et `المهام` sont sur la p.306. Pas de bloc `الهوامش`.

###### سند 16 — العدالة والإنصاف — p.307-308

**Auteur tel qu'imprimé** : **أرسطو** (bloc `الكاتب` : `أرسطو : ( 384—322 .ق.م):`).

**التمهيد** (verbatim) :

> إنّ أحوال معيشنا تكشف عن وجوه من الظلم والاجحاف تبرر حاجتنا إلى العدالة. وإذا كنا نرغب في
> العدالة في جميع معاملاتنا ونعظّم العادل، فإننا نتطلع مع ذلك إلى الإنصاف ونرتاح إليه دون أن
> ندرك لذلك موجبا ودون أن نتبين فرقا بينهما.

*(⚠️ « الاجحاف » est imprimé sans hamza — graphie de la source, conservée.)*

**Référence imprimée** (verbatim) :

> **أرسطو**، أخلاق نيقوماخوس
> `ARISTOTE; Ethique de Nicomaque. G. F, 1965. p1137 a -1137b`

**Thèse (reformulée, R-2)** : **équitable (المنصف)** et **juste (العادل)** ne sont ni identiques
ni de genres différents — d'où la gêne : on loue l'équité comme supérieure au juste, alors que
l'équitable est **lui-même une espèce du juste**, et non un autre genre. Ce qui crée l'embarras,
c'est que l'équitable est juste **sans l'être selon la loi** : il est la **correction
(تحسين)** de ce qui est juste légalement. Car **toute loi est générale** et ne peut parler avec
exactitude des cas particuliers ; parler en général étant inévitable, la loi ne retient que les
**cas ordinaires**, sans ignorer pour autant sa propre insuffisance.

**الهوامش** : ⚠️ **aucun** encadré de note — ni p.307 ni p.308.

**الكاتب — أرسطو : ( 384—322 .ق.م)** (verbatim resserré ; commence p.307, se poursuit p.308) :
أرسطوطاليس ولد في أسطاجيرا، بشمال اليونان. وكان والده نيقوماخوس طبيب آمينتاس الثاني جد الإسكندر
المقدوني. لما بلغ أرسطو سن الثامنة عشرة التحق بأكاديمية أفلاطون في أثينا (سنة 366 ق.م) ولم يغادر
الأكاديمية إلا عند وفاة معلمه (347 ق. م). وكان أرسطو قد أخذ يتحول قبل ذلك التاريخ شيئا فشيئا عن
مثالية أستاذه وينزع إلى المباحث الطبيعية. وحوالي سنة 342 ق.م أرسل فيليب المقدوني في طلبه ليتولى
تعليم ابنه الإسكندر وهو لم يتجاوز الثالثة عشرة حينذاك. عاد إلى أثينا مرة ثانية حوالي سنة 343 ق.م
وأسّس مدرسته الخاصة أين ألقى أرسطو دروسه في شتى أغراض المعرفة وفي غضون ما يقرب عن 21 سنة فقط ألف
أهم آثاره العلمية والفلسفية والتي شكلت إنتاجا متفردا في تاريخ العقل البشري. وتنقسم آثاره إلى
قسمين: قسم المحاورات والمواعظ والتي اقتفى فيها أسلوب أفلاطون والتي لم يصل منها إلا شذرات أو بعض
أسمائها وقسم ثان هو عبارة عن مباحث في المنطق مثلا **" المقولات "** و**"العبارة"**
و**" التحليلات الأولى والثانية "** و**" الجدل "** و**"المغالطات"**؛ وفي الطبيعيات نذكر مثلا
**" مقالة الطبيعة "** أو ( السماع الطبيعي) و**" كتاب السماء "** … وفي علم النفس كتاب
**" في النفس "** و**" في النوم "** و**" في الأحلام "** و**" تعبير الرؤيا "**؛ وفي البيولوجيا
كتاب **" في علم الحيوان "** …؛ وفي الإلهيات كتابه **" ما بعد الطبيعة "** وفي الأخلاق والسياسة
كتاب **" أخلاق نيقوماخوس "** و**" الأخلاق إلى يوديموس "** وكتاب **"الأخلاق الكبير "**
و**" كتاب السياسة "** و**"دستور أثينا"**؛ أما في الخطابة والشعر فقد ألّف **" في الشعر "**
و**" في الخطابة "** وقد أثرت فلسفة أرسطو تأثيرا واسعا وعميقا في الحضارة العربية والغربية حتى
نهاية القرون الوسطى.

*(⚠️ **incohérence imprimée** : Philippe l'envoie chercher « حوالي سنة 342 ق.م », et le retour à
Athènes est daté **« حوالي سنة 343 ق.م »** — donc *après* coup mais avec une date *antérieure*.
Constat, pas correction.)*

**المهام** (p.308, verbatim) :

- أبيّن وجوه التطابق والاختلاف بين العدالة والإنصاف وأتبيّن من النص موجب تفوق المنصف على العادل.
- يشير النص إلى حرج في التمييز بين العادل والمنصف: أحدّد دواعي هذا الإحراج.
- إذا كانت العدالة مرغوبا فيها، فإن الإنصاف محبذ. كيف أفهم هذا الحكم؟
- أستحضر في سياق معيشي أمثلة للتدليل على حدود التمايز بين العدالة والإنصاف.
- هل يمكن أن أختار بين العدل والإنصاف؟

**Encadré-citation (p.308)** : « إن ما يسبب حرجنا، هو أن من هو منصف وعادل في ذات الوقت، لا يكون
كذلك طبقا للقانون » — **أرسطو**.

**Illustrations** : p.307 — **buste antique d'Aristote** (marbre, monochrome), en médaillon en
tête de texte. p.308 — photographie couleur d'une **balance à deux plateaux en laiton**, chaque
plateau chargé de **livres anciens**, devant une bibliothèque.

**Constats de mise en page** : le texte, la référence et le **début** de la notice d'auteur
tiennent sur la p.307 ; la p.308 porte la **fin** de la notice, les `المهام`, l'illustration et
l'encadré-citation. Pas de bloc `الهوامش`.

###### سند 17 — العدالة والقانون — p.309-310

**Auteur tel qu'imprimé** : **أفلاطون** (référence : `أفلاطون، غورجياس (5)`).
⚠️ Le هامش 1 précise que le texte **expose la position de غورجياس par la bouche de كاليكلاس** —
la thèse défendue n'est donc **pas** celle de Platon.

**التمهيد** (verbatim) :

> إذا كان العيش وفق نظام العقل يعني فيما يعنيه العيش بالتوافق مع نظام الطبيعة وإذا كانت الطبيعة
> تعطي لكبار الأسماك حقّ التهام الصّغير منها، أفلا يقود ذلك إلى الإقرار بحقّ القويّ في الهيمنة
> على الضعيف وكأنّ العقل يضفي مشروعيّة على التفاوت ويجعل من اللامساواة مبدأ العدالة؟

**Référence imprimée** (verbatim) :

> **أفلاطون**، غورجياس (5)
> `PLATON; Gorgias, 483bc-484a. Belles Lettres`

**Thèse (reformulée, R-2)** : la **loi** est l'œuvre des **faibles** et du **grand nombre** ;
c'est pour effrayer les plus forts et les empêcher de l'emporter qu'ils décrètent que toute
supériorité est laide et que l'injustice consiste à vouloir dominer autrui — car il leur suffit
d'être au niveau des autres, faute de pouvoir les égaler en valeur. Or la **nature** montre
partout l'inverse, chez les animaux comme chez les hommes : le **juste**, c'est que le **plus
fort domine le plus faible**, et le supérieur l'emporte. Ceux qui agissent ainsi (Xerxès
attaquant la Grèce, **ou son père attaquant les « Scythes »** — `أوأبوه "السيثيين"`, ce qui donne
son objet au هامش 3) suivent la **vraie nature du droit**, la **loi de la nature** — fût-elle
contraire à la loi que **nous** posons pour dresser, dès l'enfance et comme des lionceaux, les
meilleurs et les plus forts d'entre nous, afin de les asservir par la force de la **prédication
et de l'endoctrinement**.

**الهوامش** (encadré `الهوامش` — **5 entrées** : 1-3 p.309, 4-5 p.310 ; verbatim resserré) :

1. يعرض هذا النصّ موقف **غورجياس** على لسان **كاليكلاس** وهو محاور خيالي **لسقراط**
2. **كزاركساس** `Xerxès` : (519—465ق.م) ملك الفرس (486—465ق.م) ابن داريوس`(Darios)`. الأكبر
   وأتوسّا `Atossa` ابنة سيريس الأكبر `Syrus Le Grand`. اعتلى العرش بعد موت أبيه وقمع الثورة في
   مصر ثم قضى ثلاث سنوات في إعداد أسطول وجيش كبير لمعاقبة الإغريقيين على مساعدتهم الأيونية في
   حربهم مع الفرس. أحرق أثينا بعد فرار اليونانيين منها.
3. **السيث** `Les Scythes` اسم يطلق على سكان منطقة تدعى `Scythie` في شمال البحر الأسود، بلد مقسم
   اليوم بين مولدافيا وأوكرانيا وروسيا الشمالية، وهم قبائل رحل يسكنون سباسب كائنة بين المجر
   الحالية وجبال تركستان.
4. **زوس** `ZEUS` : في الميثولوجيا الإغريقية، إله السماء ورب أرباب الأولمب.
5. **غورجياس** `Gorgias` : (487 —380 ق.م)، سفسطائي يوناني من أصل صقلّي قدم إلى أثينا للدفاع عن
   صقليّة ضدّ أطماع سرقسطة. بقي في أثينا معلّما الخطابة. من أهمّ مؤلّفاته **" اللاوجود "** أو
   **" في الطبيعة "** وفيه نقد فكرة الوجود عند بارمنيدس. و**" غورجياس "** هيّ أيضا محاورة
   أفلاطونيّة موضوعها الخطابة أو فنّ الإقناع الذي يدافع عنه غورجياس في مقابل سقراط الذي يؤسّس
   خطاب الحقيقة.

*(⚠️ deux oddités imprimées, toutes deux dans le هامش 2 : le point après `(Darios)` coupe la
phrase (`ابن داريوس الأكبر وأتوسّا` est la lecture attendue), et **Cyrus le Grand** est
orthographié `سيريس الأكبر / Syrus Le Grand`. Constats, pas corrections.
Le هامش 3 ne porte **aucune** anomalie : `سباسب` est un pluriel arabe régulier de `سبسب`
(« steppe, désert »), et `المجر الحالية` désigne la **Hongrie** actuelle — vérifié au rendu
600 dpi, à comparer au `البحر الأسود` imprimé deux lignes plus haut dans la même note, dont le
tracé est tout autre.)*

**الكاتب** : ⚠️ **renvoi**, pas de notice. Imprimé (verbatim) :
**أفلاطون : انظر التعريف بالكاتب المصاحب للسند عدد 9. ( الإنيّة والغيريّة )**

**المهام** (p.310, verbatim) :

- كيف أفهم القول بأن القانون جُعل من أجل الضعفاء؟
- هل تجد في هذا وجاهة بالنظر إلى واقع البشر؟
- أستخرج من النص فهم غورجياس للعدالة.
- يفضّل غورجياس عدالة القانون الطبيعيّ على عدالة القانون الوضعي: أتتبّع الحجج التي ساقها
  الغورجياس لتأكيد موقفه.
- كيف تتحوّل المساواة إلى جور؟
- أفكّر فيما يستتبع تأسيس العدالة على قانون الطبيعة.

*(⚠️ la 4ᵉ مهمّة imprime bien **« الغورجياس »**, avec article, là où les autres écrivent
« غورجياس ». Constat.)*

**Encadré-citation (p.310)** : « جُعِلَ القانون من أجل الضعفاء ومن أجل الكثرة » — **أفلاطون**.

**Illustrations** : p.309 — **buste antique de Platon** (marbre, monochrome), en médaillon en
tête de texte. p.310 — reproduction d'un tableau, légendée en français
`Jules ADLER, La grève (1899). Pau, Musée des Beaux-Arts.` : une **foule d'ouvriers en grève**
marchant derrière des drapeaux rouges, cheminées d'usine à l'arrière-plan.

**Constats de mise en page** : texte, référence et les **3 premiers** هوامش sur la p.309 ; les
**2 derniers** هوامش, le renvoi `الكاتب`, les `المهام`, l'illustration et l'encadré-citation sur
la p.310. **C'est le premier سند de la tranche à porter un bloc `الهوامش`.**

###### سند 18 — العدل والقوّة — p.311

**Auteur tel qu'imprimé** : **باسكال** (bloc `الكاتب` : `باسكال : (1623 — 1662)`).

**التمهيد** (verbatim) :

> قد يبدو العدل مطلبا إنسانيّا نتمنّى سيادته، وبين ورديّة الأمنيّات وقتامة الواقع نصطدم بسلطان
> القوّة إلى حدّ يغدو معه تحقيق العدل حلم استحالة مادام الضّد يستبعد ضدّه.

**Référence imprimée** (verbatim) :

> **باسكال**، خواطر
> `B. PASCAL; Les Pensées. éd.Gallimard, 1976, pp 1160 - 1161.`

**Thèse (reformulée, R-2)** : il est **juste** de suivre le juste et **nécessaire** de suivre le
plus fort ; or **justice sans force est impuissante** et **force sans justice est tyrannique**.
Il faut donc **joindre** justice et force — rendre le juste fort ou le fort juste. Mais la
justice est **sujette à dispute** tandis que la force est **aisément reconnue et incontestée** :
on n'a donc pas pu donner la force à la justice, la force ayant contesté la justice en la
déclarant injuste et en se déclarant juste elle-même. Faute de pouvoir rendre fort ce qui est
juste, **on a rendu juste ce qui est fort**.

**الهوامش** : ⚠️ **aucun** encadré de note.

**الكاتب — باسكال : (1623 — 1662)** (verbatim resserré) : فيلسوف وعالم فرنسي نبغ منذ حداثة سنّه
إذ بدأ الكتابة و لم يتجاوز عمره السادسة عشر عاما بمقالة في المخروطات ثم ابتكر الآلة الحاسبة بعد
ذلك بسنتين. دافع عن شرعيّة التفكير والتجربة في البحث عن الحقيقة العلميّة، طالما أنّ الفرد،
والإنسانيّة يتطوّران بتراكم المعارف. ويعتبر أنّ غزارة المعرفة لا ترتكز على منهج كوني كما يعتقد
ديكارت. من أهمّ مؤلّفاته **" خواطر "** (1670) قدّم فيه تصوّره للإنسان على خلفيّة دينيّة مسيحيّة
ومن مؤلّفاته أيضا **"في فن الإقناع "** (1728) ثمّ **"في العقل الهندسي "** و**" رسالة في
الخلاء "**.

**المهام** (p.311, verbatim) :

- ما الفرق بين الإقتداء بالقوي والإقتداء بالعادل؟
- ماذا يحدث حين تعوزنا القوّة على فرض قرار عادل؟
- ماذا يحدث حين نلجأ إلى القوّة دون موجبات عادلة؟
- ما الفرق بين أن نجعل القويّ عادلا وبين أن نجعل العادل قويّا؟ أبلور جوابي منتبها إلى استتباعات
  الموقفين.
- لِمَ اعتبر الكاتب الاعتراف بالقوة أيسر والعدالة فضاء نزاع؟
- هل القوّة وحدها قادرة على وضع حدّ للصراع بين البشر؟ أحرّر فقرة في الغرض.

*(⚠️ « الإقتداء » est imprimé avec hamzat qaṭʿ dans les deux occurrences de la 1ʳᵉ مهمّة.
Constat.)*

**Encadré-citation** : ⚠️ **aucun** — la page se referme sur les `المهام`.

**Illustrations** : p.311 — **portrait gravé de Blaise Pascal** (main au menton, cheveux
longs), en médaillon en tête de texte. **Aucune autre illustration.**

**Constats de mise en page** : ⚠️ **سند intégralement contenu sur UNE page** — titre, تمهيد,
texte, référence, `الكاتب` et `المهام` tiennent tous sur la p.311. Pas de `الهوامش`, pas
d'encadré-citation.

###### سند 19 — العدل أساس الطاعة — p.312-313

**Auteur tel qu'imprimé** : **راولس** (bloc `الكاتب` : `راولس : (1921—2002)`).

**التمهيد** (verbatim) :

> بين الحاجة إلى الدولة وواجب الامتثال إلى قوانينها والدعوة إلى التمرّد عليها وعصيانها صورةُ
> جدلٍ مستمر بين الإنسان والدولة أصبح معه الخضوع المطلق والسلطان المطلق بلا معنى إذ لا خير في
> مدينة لا حكم فيها ولا خير في دولة لا تحقّق ما ننشده منها.

**Référence imprimée** (verbatim) :

> **راولس**، نظريّة العدالة
> `J. RAWLS; Théorie de la justice. éd. Seuil, 1985, pp 391 -392.`

**Thèse (reformulée, R-2)** : la question est de savoir **dans quelles circonstances** et
**jusqu'où** nous sommes tenus d'obéir à un régime injuste. Dire qu'on n'y est jamais tenu est
**faux** : l'injustice d'une loi n'est pas, en général, une raison suffisante de ne pas s'y
soumettre — pas plus que la **validité juridique** d'une législation (celle que fixe la
constitution en vigueur) n'est une raison suffisante de s'y conformer. Lorsque la **structure de
base** de la société est suffisamment juste, il faut reconnaître les lois injustes comme
**obligatoires**, à condition qu'elles ne dépassent pas **un certain degré d'injustice**. Tracer
cette limite conduit au problème plus profond de l'**obligation et du devoir politiques**, où
des principes s'opposent — les uns conseillant l'obéissance, les autres le contraire : il faut
donc affronter ces exigences par une **conception des priorités** appropriée, **et dans les
limites du contexte que nous avons retenu** (`وضمن حدود السّياق الذي رجحناه` — restriction
imprimée, à ne pas laisser tomber).

**الهوامش** : ⚠️ **aucun** encadré de note — ni p.312 ni p.313.

**الكاتب — راولس : (1921—2002)** (verbatim resserré) : مفكّر أمريكي ولد ببالطيمور. كان شاهدا على
كارثة **هيروشيما** أثناء قصفها بالقنبلة الذريّة. بعد هذه التجربة رفض أن يصبح ضابطا وغادر الجيش
وأكمل شهادة الدكتوراه في الفلسفة والأخلاق (1946) . أصبح أستاذا بجامعة هافارد `Havard.` و درّس ألى
حدود سنة 1952. من مؤلّفاته **" نظرية العدالة "** (1971)، وقد أعد هذه النظرية في ظروف كانت فيها
شرعية الولايات المتحدة موضع تساؤل مرتبطة بحرب الفيتنام، واحتدام الصراع من أجل الحقوق المدنية،
ولأجل ذلك اعتبرت النص الأهم في الفلسفة السياسية. يتمحور هذا الكتاب حول معاني القيم، والعدالة
والليبرالية. وترتكز نظريته هذه على مبدأين: مبدأ الحرية، أي المساواة وتكافؤ الفرص مع ضمان حريّة
الآخرين. ومبدأ الاختلاف، الذي يجيز التفاوت ولا يتعارض مع مبدأ العدالة. ومن مؤلّفاته أيضا
**" الفرد والعدالة الاجتماعية "** (1988)، **" الليبرالية السياسية "** (1993) وتناول فيهما معاني
الحرية، والعدالة، وحقوق الإنسان وحقوق المواطن…

*(⚠️ trois anomalies imprimées : `هافارد Havard.` — **Havard** pour Harvard ; `ألى` pour `إلى` ;
et « درّس ألى حدود سنة **1952** » placé **après** un doctorat daté 1946 et une chaire à Harvard,
ce qui ne s'ordonne pas. Constats, pas corrections.)*

**المهام** (p.313, verbatim) :

- هل نكون على صواب حين نرفض طاعة نظام جائر؟
- هل في صلاحية قانونية لتشريع ما سبب كاف للامتثال للقانون؟
- ضمن أيّة شروط يمكن الامتثال لقانون جائر؟
- القوانين العادلة والقوانين الجائرة: هل من حدود واضحة للفصل بينها؟ ما معيار هذا التمييز؟
- أستخلص معيار العدل وشروط الطاعة. أحرر فقرة في الغرض.
- ما قيمة التمييز بين مطالب الواجب والإلزام؟
- ما أساس القول بترتيب الأولويات في حلّ مشكل المواجهة بين مطالب الواجب والإلزام السياسيين؟

**Encadré-citation (p.313)** : « يتعلّق الأمر بمعرفة في أي الأحوال و إلى أي مدى نكون ملزمين
بالخضوع إلى نظام جائر » — **راولس**.

**Illustrations** : p.312 — **photographie de John Rawls** (casquette à carreaux, lunettes),
en médaillon en tête de texte. p.313 — photographie couleur : un **loup gueule ouverte** face à
un **ours brun**, en forêt.

**Constats de mise en page** : texte, référence et **toute** la notice d'auteur sur la p.312 ;
la p.313 ne porte **que** les `المهام`, l'illustration et l'encadré-citation. Pas de `الهوامش`.

###### سند 20 — المواطن العالمي — p.314

**Auteur tel qu'imprimé** : **إيبكتات** — **même graphie au فهرس** (p.407, ligne 20), sur la ligne
de référence et dans le bloc `الكاتب`. Il n'y a **aucune divergence** فهرس/page ici (revérifié au
rendu 600 dpi sur les trois occurrences). Translittération latine imprimée : `EPICTETE`.

**التمهيد** (verbatim) :

> قد يكون النظر إلى الإنسان بما هو شخصية قانونية أساس التعامل معه باعتباره مواطنا، غير أن اختزال
> النظر في الإنسان في حدود الوطن الذي ينتمي إليه قد لا يستوفيه حقه أمام تداخل العلاقات والمصالح
> بين الأوطان وأمام نزوعه نحو الكلية والكونية وهو ما يدعونا إلى التفكير في منزلة الإنسان
> السياسية بين النظر إليه بماهو مواطن محلي وبين اعتباره مواطنا عالميا.

**Référence imprimée** (verbatim) :

> **إيبكتات**، محادثات
> `EPICTETE; Entretiens, I,9. éd. Budé, p37`

**Thèse (reformulée, R-2)** : s'il est vrai qu'une **parenté** unit le dieu et les hommes, comme
le prétendent les philosophes, il ne reste aux hommes qu'à **imiter Socrate** — se refuser
toujours à répondre « d'Athènes » ou « de Corinthe » à qui demande leur pays, et dire : **« je
suis citoyen du monde »**. Car on ne doit pas son nom au **coin de terre** où le corps fut jeté à
la naissance, mais à une origine **plus haute**, qui déborde ce coin, la maison et jusqu'au pays
des ancêtres. Et dès lors qu'on a compris que le plus fondamental, le plus important et le plus
**universel** de tout est l'**ordre composé du dieu et des hommes**, rien n'empêche plus de se
dire **citoyen du monde**.

**الهامش** (encadré au **singulier** — `الهامش` — car **une seule** entrée ; verbatim) :

1. **كورنثيّا** : `Corinthie` نسبة إلى كورانثوس أو كورنث `Corinthus` وهي مدينة في بلاد اليونان.

**الكاتب** : ⚠️ **renvoi**, pas de notice. Imprimé (verbatim) :
**إيبكتات : انظر التعريف بالكاتب المصاحب للوضعيّة الاستكشافيّة الثانيّة. ( الإنيّة والغيريّة )**
→ ⚠️ le renvoi vise une **وضعيّة استكشافيّة**, pas un سند ; « انظر » y est imprimé avec une
césure visible (`ا نظر`).

**المهام** (p.314, verbatim) :

- ماذا يعني تعريف الإنسان بأنه مواطن؟ أحدد خصائص المواطنة.
- كيف أفهم إشارة الكاتب إلى القرابة بين الإله والبشر وما علاقتها بالمواطن العالمي؟
- كيف برهن الكاتب على مشروعية قول الإنسان عن نفسه بأنه مواطن عالمي؟
- هل من تعارض بين انتمائي إلى وطن بعينه وبين انتمائي للعالم بما هو وطن للجميع؟
- أيّ قيم تؤسّس لفكرة المواطن العالمي؟
- في أيّ معنى يكون سقراط الأثيني نموذجا للمواطن العالمي؟
- هل حصل أن أحسست بأنّي مواطن عالمي؟ أعلّل جوابي في فقرة.

**Encadré-citation** : ⚠️ **aucun**.

**Illustrations** : p.314 — **portrait gravé d'Épictète** (vieillard barbu, tête voilée), en
médaillon en tête de texte. **Aucune autre illustration.**

**Constats de mise en page** : ⚠️ **سند intégralement contenu sur UNE page** — titre, تمهيد,
texte, référence, `الهامش`, `الكاتب` (renvoi) et `المهام` tiennent tous sur la p.314.

###### سند 21 — مواطن العالم المشترك — p.315-316

**التمهيد** (verbatim) :

> الهويّة الفرديّة، الهويّة الثقافيّة والهويّة السياسيّة: هويّات مختلفة تتقاطع في الإنسان فردا
> وجماعة ويزيدها العيش المشترك تعقيدا فتتعدّد خيارات المرء بحثا عن توازن منشود يعدّ شرط معاودة
> النظر في دلالة مواطنة عالميّة يُفترض فيها تحقّق الإنساني في الإنسان.

**Référence imprimée** : إتيان تاسان، ما الذات السياسيّة؟ —
`Etienne TASSIN; Qu'est-ce qu'un sujet politique? Revue Esprit; Avril 1997. pp 149-150.`

**Thèse (reformulée)** : être citoyen du monde ne signifie pas appartenir à une communauté mondiale
— l'humanité ne s'est jamais voulue une seule communauté. Cela signifie **penser son inscription
particulière dans une communauté à l'horizon du monde commun** : rattacher les droits civils et
politiques au principe « الحقّ في أن يكون لنا حقوق », lequel n'a de sens que rapporté à un monde
commun. Le citoyen mondial n'est donc **pas l'individu privé** mais le **sujet politique** (الذات
السياسيّة), qui découvre et déclare son existence singulière **dans les relations politiques**, en
exposant ses actes et ses paroles dans des espaces publics. Il préfère les principes aux
particularismes, le bien commun au bien du groupe — bref, l'institution républicaine à la réserve
autoritaire des communautés culturelles.

**الهامش** (verbatim) :

> 1 — **حنّا آرنت** `H. ARENDT` انظر " أصول الكليانيّة "، نيويورك 1975. ص 296 وكذلك كتابها
> " الامبرياليّة "، باريس 1982، ص 281؛ تعرّف فيهما الحق في أن يكون لنا حق بقولها " العيش داخل
> بنية حيث يُحكم على المرء في ضوء أفعاله وآرائه ".

**الكاتبة** (notice, verbatim resserré) : **إتيان تاسان** — مفكّرة وأستاذة فلسفة معاصرة، نشرت في
مجلّة « الفكر » مقالا عنوانه « أوروبا : هل هي جماعة سياسيّة؟ » (نوفمبر 1991)؛ كما نشرت فيها
« الهويّة القوميّة والمواطنة السياسيّة » (جانفي 1994). وفي المقال الذي اقتطف منه النصّ تستعيد
مسائل سبقت أن تناولتها في ندوات ومحاضرات ألقتها بالجامعات الوطنيّة **ببوفوتا وقرطاجنّة بكولومبيا**
وجامعة الشيلي وخلال ملتقى عُقد بباريس تحت عنوان « **الحق، الديمقراطيّة والفضاء العمومي** »
(جانفي 1997).

> ⚠️ **Les trois lieux sont sud-américains, pas tunisiens.** `بوفوتا` = **Bogotá** ;
> `قرطاجنّة` = **Cartagena** — la ville **colombienne**, Carthage s'écrivant `قرطاج` ;
> `بكولومبيا` est un locatif (« **en Colombie** ») qui régit les **deux** villes et n'est pas
> le nom d'une université. Lire donc : « les universités nationales de **Bogotá** et de
> **Cartagena, en Colombie**, et l'université du **Chili** ». Vérifié au rendu 600 dpi.
> ⇒ La notice imprimée est **intégralement en arabe** : ne jamais la restituer en français au
> milieu d'un bloc annoncé verbatim — c'est ce basculement qui avait fait dériver les toponymes.

> ⚠️ **Anomalie de la source, non arbitrée** : le manuel intitule l'encadré « **الكاتبة** » et
> emploie le **féminin** tout du long (« مفكّرة وأستاذة … نشرت … تناولتها »). Étienne Tassin est un
> philosophe **masculin**. L'imprimé est recopié tel quel ; ne pas « corriger » en génération, mais
> ne pas non plus bâtir une question sur le genre de l'auteur.

**المهامّ** (verbatim) :

- أيّة دلالة للمواطن العالمي تستبعدها الكاتبة؟ كيف أفسّر هذا الاستبعاد؟
- ما دلالة " العالم المشترك " وما قيمته الإجرائيّة في سياق مقاربة الكاتبة؟
- في أيّ معنى تمثّل كثرة البشر خطرا على الحقّ؟
- لِمَ اعتبرت الكاتبة اكتمال قدر الدولة مشروطا بتجاوز الأمّة لا بتجسّدها؟
- ما دلالة المفاضلات التي تتحدّث عنها الكاتبة؟ أحلّلها وأحدّد قيمتها في تحديد دلالة المواطن العالمي.
- أيّة قرابة بين مفهومي " الذات السياسيّة " و " المواطن العالمي "؟
- هل تتعارض فكرة " المواطن العالمي " مع كوني " مواطنا تونسيا "؟ أحرّر فقرة في الغرض.

**Encadré-citation (p.316)** : « يكون، إذن، مواطنا عالميّا، لا الفرد الخاصّ… بل الذّات السياسيّة
وهي تكشف وجودها الخصوصي وتعلنه داخل العلاقات السياسيّة » — **إتيان تاسان**.

**Illustrations** : p.315 — croquis au trait d'un visage. p.316 — photographie d'un alignement de
**statuettes de la statue de la Liberté** en série.

###### سند 22 — المواطن العالمي الجديد — p.317-318

**التمهيد** (verbatim) :

> اهتزّت في عالمنا اليوم أركان السيادة الوطنيّة في دلالتها التقليديّة واهتزّ معها الشعور بالانتماء
> إلى جماعة ضيّقة بعد أن فقد العالم ذاته اتساعه الذي كان عليه وأضاع حدوده التي رسمها الجنس والعرق
> والدّين. من تبعات ذلك جرى البحث في الجغرافيا السياسيّة الجديدة عن مواطنة جديدة تلائمها.

**Référence imprimée** : ستيفان كاستلاس، العولمة والهجرة، المجلّة الدوليّة للعلوم الاجتماعيّة؛
العدد 156، جوان 1998، ص 209 — `Stephen CASTLES; Mondialisation et migration; Revue internationale
des sciences sociales; N 156, Juin 1998, p 209.`

**Thèse (reformulée)** : le grand succès du modèle de l'État-nation fut le **citoyen démocratique**
— membre de la société, porteur de droits, participant à la législation et à la conduite du
gouvernement. Mais la citoyenneté démocratique porte une **ambiguïté** : elle mêle l'appartenance à
une communauté **politique** (où tous sont égaux, abstraction faite du sexe, de la race, de la
religion) et l'appartenance à une communauté **nationale** (fondée sur des traits culturels
supposés communs). D'où, historiquement, l'absorption de groupes ethniques par effacement de leurs
cultures. Or l'homogénéité culturelle est devenue **impossible** au « temps des migrations » :
frontières poreuses, diversité ethnoculturelle, identités multiples, doubles nationalités. Il faut
donc un **modèle nouveau de citoyenneté mondiale** qui rompe le lien entre appartenance et
territoire : que les individus exercent leurs droits **en tant qu'êtres humains** et non en tant
qu'êtres nationaux — un modèle multiculturel où la diversité ethnique et les identités plurielles
soient reconnues.

⚠️ **Passage à ne pas perdre** — c'est la réponse à la 1ʳᵉ مهمّة (`ولِمَ اعتبر طموحا مشتركا؟`).
Le manuel imprime : `ولم تتحقّق المواطنة الديمقراطيّة إلاّ في عدد محدود من البلدان، وفوق ذلك، حصل
هذا الأمر في الغالب ضمن قيود. لكنّ هذا الطّموح تتقاسمه معظم شعوب العالم.` — la citoyenneté
démocratique **n'a été réalisée que dans un nombre restreint de pays**, et le plus souvent
**sous contraintes** ; mais **cette aspiration, la plupart des peuples du monde la partagent**.

**Pas d'encadré الهامش sur ce سند** (constaté).

**الكاتب** (notice, verbatim resserré) : **ستيفان كاستلاس (1947)** — باحث أنجليزي معاصر وأستاذ
بجامعة أكسفورد. شغل منصب مدير للبحوث المتعلّقة بتعليم المهاجرين وعُرف ببحوثه المتّصلة بالهجرة
وتعدّد الثقافات في المجتمع الأوروبي وأستراليا وآسيا. شغل منصب سفير بريطانيا ومسؤولا في الاتّحاد
الأوروبي. من مؤلّفاته : « العملة المهاجرين والبنية الطبقيّة في أوروبا الشرقيّة » (1973) [sic —
« العملة » pour « العمالة »]، « الإتنيّة والعولمة » (2000)، « ماضي الهجرة والحركة الشعبيّة العالميّة
في العالم المعاصر » (2003).

**المهامّ** (verbatim) :

- ما دلالة " المواطن الديمقراطي " ولِمَ اعتبر طموحا مشتركا؟
- ما هو الغموض الذي يحيط بمفهوم المواطنة الديمقراطيّة وهل يضعنا هذا الغموض أمام مفارقة؟
- لِمَ يظلّ هدف التجانس الثقافي مستشكلا؟ أستحضر مكاسبي المعرفيّة التي حصّلتها في مسألة " الخصوصيّة والكونيّة ".
- هل يمكن تناسي الاختلاف وهل في ذلك غُنْمٌ ما؟
- ما الذي دعا إلى ضرورة البحث عن صيغة جديدة لمفهوم المواطنة ضمن الواقع السياسي الرّاهن؟
- هل تمثّل فكرة المواطنة العالميّة حلاًّ لمشكل الأقليّات والمهاجرين؟
- أستخلص، في ضوء ما ورد في النصّ، دلالة " المواطن العالمي ".

**Encadré-citation (p.318)** : « يلزمنا نموذج جديد للمواطنة العالميّة يمكنه أن يحطّم الرّابطة بين
الانتماء والإقليميّة » — **كاستلاس**.

**Illustrations** : p.317 — portrait photographique de l'auteur. p.318 — photomontage d'un homme en
chemise et cravate dont la tête est un **globe terrestre**, tenant un journal.

> ✅ **Fin de la نافذة سندات du مبحث 3.1** : 22 سندات, p.278-318.
> ⚠️ Le **مهامّ** du سند 22 renvoie explicitement à la مسألة « الخصوصيّة والكونيّة » — c'est-à-dire
> au **مبحث 1.2**, non encore transcrit. Renvoi inter-chapitres imprimé par le manuel.

##### 3.1.3 نافذة دعائم للتفكير في المسألة — p.319-334

> **Pages lues** : p.319–334 (intégral, rendu 200 dpi ; passages douteux revérifiés à 400-450 dpi).
> **Source** : manuel élève `210402P00`, مبحث 3.1 « الدّولة : السّيادة والمواطنة ».
> ⚠️ Ce ne sont **pas les numéros** qui divergent entre le فهرس et les pages, mais les
> **libellés** : le فهرس (p.408) imprime `نافذة كيفيّات للتفكير` (avec le لـ) là où la page 335
> imprime `كيفيات التفكير`, **sans** le mot `نافذة` ; de même le فهرس (p.407) imprime
> `نافذة سندات التفكير في المسألة` là où la page 278 imprime `نافذة سندات للتفكير في المسألة`.
> Les numéros, eux, concordent.

**p.319 — page d'ouverture de la نافذة.** Titre imprimé en écriture calligraphique :
**نافذة دعائم للتفكير في المسألة**. Image : une pile de livres reliés rouge avec une paire de
lunettes posée dessus, sur fond de feuillage (**c'est exactement la même image qu'à la p.251 du
مبحث 2** — le manuel réutilise le visuel d'ouverture des نوافذ دعائم). Encadré-citation
(verbatim) :

> « إن الغاية القصوي من تأسيس الدّولة ليست السيطرة والتسلّط أو إرهاب النّاس وجعلهم يقعون تحت
> نير الآخرين، بل هي تحريرهم من الخوف بحيث يعيش كل فرد في أمان بقدر الإمكان، أي يحتفظ قدر
> الإمكان بحقّه الطبيعي في الحياة دون إلحاق ضرر بغيره ».
> — سبينوزا، *رسالة في اللاهوت والسياسة*

⇒ **Cette citation d'ouverture est la thèse que le نصّ مطوّل (Spinoza, p.339-345) viendra
développer** : la fin de l'État n'est pas la domination mais la libération de la peur.
`[« القصوي »` est imprimé ainsi, avec ي final au lieu de ى — coquille de la source.`]`

Sommaire imprimé en bas de page (deux entrées numérotées, de droite à gauche) :
**1 — تحديدات وتمييزات مفهوميّة** · **2 — سياقات فكريّة**.

⚠️ **Le sommaire n'annonce que 2 entrées**, alors que la فلسفة العقد الاجتماعي (p.332-334) est
imprimée **à l'intérieur de la 2ᵉ** comme son **3ᵉ item** (« 3 – فلسفة العقد الاجتماعي »).
Ce n'est donc **pas** une troisième rubrique de la نافذة.

---

###### 3.1.3.1 تحديدات وتمييزات مفهوميّة — p.320-326

Trois concepts sont définis : **السّياسة** (p.320-321), **اللائكيّة** (p.322-323),
**الكليانية أو التوتاليتارية** (p.324-326).

**Gabarit — il n'est PAS uniforme, contrairement au مبحث 2** :

| Concept | Entrées imprimées | Rubrique « قيل في … » | Tableau مجاورة/مناقضة |
| --- | --- | --- | --- |
| **السّياسة** | ■ لغة · ■ اصطلاحا · ■ فلسفيا | ✅ 6 citations | ⛔ **absent** |
| **اللائكيّة** | ■ لغة · ■ اصطلاحا · ■ فلسفيا | ✅ 6 citations | ✅ p.323 |
| **الكليانية** | **\* التعريف** → ■ لغة · ■ فلسفيا (**pas de اصطلاحا**) | ✅ 8 citations | ✅ p.326 |

Un encadré **\* لمزيد التعمّق** commun aux trois concepts clôt la sous-partie (p.326).

---

**1 — السّياسة · `La politique` — p.320-321**

**■ لغة (verbatim)** :

> **السّياسة** في اللّغة العربية مصدر **« ساس »**، وهي **تنظيم أمور الدّولة وتدبير شؤونها**. وفي
> الإغريقية `Politiké` من `Polis` **وهي المدينة**، وتعني **النشاط الذي ينظّم ويسيّر شؤون
> المدينة** وبشكل عام المجموعة التي **يكوّن أفرادها جسما له نفس المصير**.

*Distinction grecque imprimée — la plus testable de la page* :

> وقد ميّز الإغريق بين **« البوليتيكه »** أو **النّشاط السّياسي الواقعي** و**« البوليتيا »** أو
> **تأسيس نظام ما لتسيير شؤون المدينة**.

⇒ **البوليتيكه = la pratique politique effective** ≠ **البوليتيا = l'institution d'un régime**.

*Côté latin (verbatim)* : أمّا اللاّتينيين فقد استعملوا بشكل تفضيلي عبارات **« بوليكوس »**
`Policus` و**« سيفيليس »** `Civilis` من عبارة **« بوليتكوس »** `Politicus`
و**« الرسبوبليكا »** `Res-Publica` والتي تعني **مجموع الشّؤون السّياسيّة**.

**■ اصطلاحا (verbatim)** :

> تعني **السّياسة** بوجه عام **ما يتّصل بالحكومة والدّولة** في مقابل **أشكال الحياة الاجتماعية
> الأخرى** (إدارة، عدالة، فنّ…) وهي **في طبيعتها نشاط بشريّ**.

⇒ Distinction posée : **السياسة ≠ les autres formes de la vie sociale** (administration,
justice, art).

**■ فلسفيا (verbatim resserré)** :

> تعدّ **السياسة** موضوع **« علم السياسة »** بما هو، في عرف الفلاسفة القدامى، **البحث في أنواع
> الدّول والحكومات، وعلاقة بعضها ببعض، والكلام على المراتب المدنيّة وأحكامها، والاجتماعات
> الإنسانية الفاضلة والرّديئة، ووجوه استبقاء كلّ منها وعلّة زواله**…

Œuvres citées comme sources de ce علم (verbatim, avec les dates imprimées) :
**« كتاب السياسة » لأرسطو (384–322 ق.م)** · **« اللوفياثان » `Léviathan` لهوبس `Hobbes`
(1588–1679)** · **« روح القوانين » لمنتسكيو `Montesquieu` (1689–1755)**.

Suite (verbatim) : وتمثّل السّياسة أيضا مجالا للنشاط الفلسفي تكوّن ما يسمّى **فلسفة السّياسة**
التي تعنى بـ**تحليل مختلف أشكال السّلطة وعلاقتها بالمواطنين وأنظمة الحكم** أو بصورة أضيق
**إنشاء تصور خاصّ للتاريخ والدّولة**.

⇒ **Distinction : علم السياسة ≠ فلسفة السياسة.**

**Les trois distinctions internes que le manuel imprime ensuite (p.320) — le cœur testable** :

1. **الفارابي** : **السّياسة الشرعيّة** (والتي **تستمدّ أحكامها من الدّين**) ≠ **السّياسة
   المدنيّة** (وهي **قسم من الحكمة العمليّة** أي **الحكمة السياسيّة أو علم السّياسة**).
2. **السياسة النّظرية** (تعنى بـ**دراسة الظواهر السّياسيّة المتعلّقة بأحوال الدّول والحكومات**)
   ≠ **السّياسة العمليّة** (تعنى بـ**أساليب ممارسة الحكم في الدّولة لرعاية مصالح النّاس، وتدبير
   شؤونهم وأحوالهم**).
3. **السّياسة** (le substantif) ≠ **السّياسي** : « يطلق على **المنسوب إلى السّياسة**، وإذا كان
   **نعتا لأمر** كان يعني **الأمر المدني المشترك بين المواطنين الخاضعين لقوانين واحدة** ».

**Le présupposé de la politique (verbatim)** :

> **تفترض السّياسة إذن فكرة التّجمع أو الوحدة**، وقد فهم **إيريك فايل** `Eric Weil` (1904–1977)
> السّياسة بما هي **« حياة مشتركة بين البشر حسب البنى الأساسيّة لهذه الحياة »**.

**Les trois métaphores de l'unité politique (p.320-321, verbatim, à cheval sur les deux pages)** :

> تستعمل عبارة **وحدة سياسيّة** و**مجتمع سياسي** للتّدليل على وحدة أو **« جسم متمفصل »** استعارة
> لعبارة **هوبس** أو **« كلية عضويّة »** حسب عبارة **هيغل** `Hegel` (1770–1831)، **وحدة اجتماعية
> لها حياة سياسيّة في إطار علاقة بين حكّام ومحكومين أو بين سلطة حكم ومواطنين**.

**Le glissement péjoratif du mot depuis le 16ᵉ siècle (p.321, verbatim resserré)** :

> غير أنّه ومنذ **القرن السّادس عشر** ظهر استخدام لكلمة **السّياسة** كنعت يستخدم **بغرض المدح
> أحيانا والتحقير أحيانا أخرى** معبّرا عن **الغاية السّياسيّة الحقيرة**، فيحمل على معاني
> **الحيلة والمكيدة وعدم الذمّة**. **والاستعمال الرّاهن للمفهوم لا ينفصل عن هذا الموروث**.

Deux emplois actuels signalés :
- **كنعت** — pour des domaines variés : شؤون السياسة، **الاقتصاد السّياسي**، **الحقوق
  السّياسيّة**…
- **دلالة مجازيّة** — « تعني **الفارق القائم بين مجموع المواطنين ورجال السّياسة** الذين ينظر
  إليهم **كاختصاصيّين منشغلين بالسّلطة** ممّا يطرح مشاكل يعسر حلّها تتصل بالدّيمقراطيات
  (**مشاكل الإعلام والمشاركة**…) ».

**■ قيل في السّياسة (p.321, verbatim, 6 citations)** :

| Auteur (tel qu'imprimé) | Citation |
| --- | --- |
| **أرسطو** | « **الإنسان حيوان سياسي** ». |
| **مورا** | « **السّياسة فنّ الإبقاء على الدّول** ». |
| **بول فاليري** | « السّياسة **فنّ يمنع النّاس من التّدخل في شؤون هي شؤونهم** ». |
| **روسو** | « إنّ الذين يريدون **معالجة الأخلاق والسّياسة كلاهما على حدة** لن يفقهوا من أيّهما شيئا ». |
| **فولتير** | « للأسف يبدو أنّ **السّياسة والحرب** هما **المهنتان الأقرب إلى طبيعة الإنسان** : فإمّا **التفاوض** أو **التّحارب** ». |
| **كانط** | « تقول السّياسة : **كن حذرا كالأفعى**، ولكنّ الأخلاق تضيف (**شرطا مقيّدا**) : **دون رياء، كاليمامة** ». |

Illustrations : p.320, photo d'un défilé de masse en chemises jaunes sur une place, devant un
immeuble portant le visage de **Che Guevara** en ferronnerie (Place de la Révolution, La Havane) ;
p.321, photo d'une manifestation étudiante brandissant des drapeaux rouges et des banderoles en
caractères chinois. Aucune des deux ne porte de légende imprimée.

---

**2 — اللائكيّة · `Laïcité` — p.322-323**

**■ لغة (verbatim)** :

> **اللائكيّة** لفظة **مستحدثة في اللغة العربيّة**، تعرف كذلك **بالعلمانية**، وهي المقابل العربي
> لكلمة `Laïcité` الفرنسية المشتقة من اليونانية `Laikos` أو `Laos` ومن اللاتينية `Laicus` والتي
> تعني **العاميّ أو ابن الشعب أو المدنيّ غير المتعلّم** في مقابل **الكاهن** أو `Le Clerc` التي
> تُطلق على **رجل الدّين الذي تلقى تعليما**.

*Distinctions posées ici — les deux les plus testables de l'entrée* :

1. **اللائكي ≠ الكاهن / `Le Clerc`** (l'homme du peuple non instruit ≠ le clerc formé).
2. **اللائكيّة ≠ الاكليريكية** (verbatim) : « **واللائكيّة هي نقيض الاكليريكية** التي تُعرف
   **كتوجه يقول بضرورة تدخل رجال الدّين في الشؤون العامّة** ».

Sens grec complémentaire imprimé : `Laos` = **وحدة المتساكنين الذين يُنظر لهم ككلّ لا يقبل
القسمة أو التمييز** — d'où : « **تُطلق صفة اللائكي على رجل من الشعب دون أن تميزه أو تجعله في
مقام رفيع : فلا دور معترف به له من قائد المدينة ولا سلطة له لكي يفرض قناعاته على الآخرين** ».

**■ اصطلاحا (verbatim)** :

> تعني **اللائكيّة فصل الدّين عن الدولة** ؛ وعلى هذا الأساس **يتحرّك المفهوم ضمن الحقل السياسي**.
> تسمح لنا الدلالة الاشتقاقية من بيان الدلالة الاصطلاحية إذ **تعلن اللائكيّة وحدة الشعب على أساس
> من الحريّة والمساواة في الحقوق** : **حريّة الاعتقاد التي لا تخضع لأيّ توجيه** و**المساواة فيما
> يتّصل بالقناعات الذاتيّة أو الشخصيّة**، فليس ثمّة **أية أفضلية بين التوحيد أو الإيمان بتعدد
> الآلهة، أو بين الفكر الحرّ والتصوّف**.

**■ فلسفيا (verbatim)** :

> تحيل **اللائكيّة** على **معنى سياسي قانوني**، كما تحيل على **جملة الإشكالات التي تتصل بالتنظيم
> السياسي للمجتمع، وأساس الحقّ المدني** وبصورة خاصّة **بعلاقة الدين بالدولة أو السّلطة الزمنية
> بالسلطة الروحية**.

Développement imprimé (p.322, à cheval sur les deux colonnes) :

- Dans une société laïque **يتم الاعتراف بأي مذهب أو قناعة** mais tout choix religieux ou
  confessionnel reste **مسألة خاصة** ; et ce « privé » se prend **en deux sens** :
  **المعنى الأوّل شخصي وفردي** ; **أمّا الثاني فيكون جمعيّا** — mais **دون أن يحقّ لهذه الجماعة
  أن تكون لسان الشعب أو أن تحتلّ الفضاء السياسي وتمارس من خلاله سلطة إكراه لإتّباع معتقداتها**,
  « إذ يتعلّق الأمر **بتجمّع خاص وليس بالمجتمع في عمومه** ».
- **وحدة الشعب** = **مبدأ للمساواة بين الجميع**, mais une égalité **تتأسس على الوعي الحر**, « بما
  أن **الوعي لا ينبغي ولا يمكن أن يخضع للإكراه** ».
- **وحدة الشّعب se comprend par opposition à** : الاعتراف **بمجموعة أو فريق بامتياز أو حقوق
  استثنائيّة أو خاصّة أو دور قيادي بالنسبة إلى الشعب ككل**.
- Conclusion imprimée (verbatim) : وحدة الشعب **ليس لها من أساس سوى المساواة في حقّ تبني أي عقيدة
  أو مذهب أو اتجاه**، والتي **تمنع أن تصبح عقيدة خاصة معيارا عاما أو أن يكون هذا المعيار قاعدة
  لممارسة النفوذ**.

**Reprise de la définition philosophique et les deux étapes historiques (p.323, verbatim)** :

> تفيد **اللائكية فلسفيا إذن فصل الدّين عن الدولة**، إذ يتمثل **مرجع اللائكية وأساسها** فيما
> **يوحّد الجميع** وما يُعدّ **قاسما مشتركا بين الجميع** بقطع النظر عن **الاختلافات المذهبية أو
> العقدية**.

> لقد اعتبرت **اللائكية سيرورة تحرّر تاريخية**، وهو تحرّر عرف **مرحلتين أساسيتين** :
> **المرحلة الأولى** شهدت **انتقالا من التّسامح المحدود إلى التسامح العام** ؛
> أمّا **المرحلة الثانيّة** فقد شهدت **قطعا مع الحدود والغموض السياسيين لمفهوم التسامح** و**إقامة
> المبدأ التشريعي لأسس الدولة اللائكية**، والذي اعتبر **بمثابة الاعتراف القانوني بحريّة الاعتقاد
> من ناحية وبالمساواة بين المواطنين**، وهو ما أنتج **نقلة حاسمة وضعت الحقوق الأساسية خارج كل
> نفوذ ديني أو اعتباطي**.

**■ قيل في اللائكيّة (p.323, verbatim, 6 citations)** :

| Auteur (tel qu'imprimé) | Citation |
| --- | --- |
| **مونتسكيو** | « **لا ينبغي أبدا أن نحتكم إلى القوانين الإلهيّة فيما ينبغي أن نحتكم فيه إلى القوانين الإنسانية**… فهذان الضربان من القوانين **يختلفان في أصلهما، وفي موضوعهما وفي طبيعتهما** ». |
| **جون لوك** | « إنّ كلّ **سلطة الدولة لا تتعلق إلا بالخيرات المدنية**، وأنّها **مقصورة على رعاية شؤون هذه الدنيا**، وأنّه **لا يحقّ لها أن تمسّ أي شيء يتعلّق بحياة الآخرة** ». |
| **جون جاك روسو** | « يمكن أن نقسّم **الدّين الذي يأخذه المجتمع بعين الاعتبار** إلى **صنفين : دين الإنسان ودين المواطن** ». |
| **باور** | « **يجب إلغاء كل امتياز ديني بوجه عام** بما في ذلك احتكار كنيسة تتمتّع بالامتيازات، وإذا كان البعض أو العديد أو الغالبية العظمى لا تزال تعتقد أنّ عليها أن تؤدّي واجبات دينية، فإنّ هذا الأداء **مسألة خاصّة تماما ومتروكة إليها** ». |
| **ماركس** | « إنّ **تفكيك الإنسان… إلى متديّن ومواطن**، هذا التفكيك **ليس كذبة ضدّ المواطن**، ولا **التفافا على التحرّر السياسي**، إنّه **التحرّر السياسي نفسه**، إنّه **الطريقة السياسية للتحرر من الدين** ». |
| **هنري بينارويز** | « إن **قوة عموميّة متحرّرة من كل تبعية عقديّة** وقادرة تبعا لذلك على **توحيد البشر رغم اختلافاتهم**، **ذاك هو المثل الأعلى للائكية** ». |

**Tableau imprimé p.323 — مفاهيم مجاورة / مفاهيم مناقضة (اللائكيّة)** — l'un des deux tableaux
de distinction de la نافذة, donc du matériau de question directement objectivé :

| **مفاهيم مجاورة** (voisins) | **مفاهيم مناقضة** (contraires) |
| --- | --- |
| العلمانية | الدولة الدينية |
| الليبيرالية | السلطة الروحيّة |
| السلطة الزمنيّة | الطائفية |
| الحق الوضعي | الحقّ الإلهي |
| المواطنة | الرعيّة |

⚠️ Le tableau est en **vis-à-vis ligne à ligne** dans la source ; les couples se lisent
naturellement (**السلطة الزمنيّة ↔ السلطة الروحيّة**, **الحق الوضعي ↔ الحقّ الإلهي**,
**المواطنة ↔ الرعيّة**), mais le manuel **n'imprime aucune flèche d'appariement** : ce sont deux
listes en regard, pas un tableau d'oppositions deux à deux déclaré.

Illustrations : p.322, photo de la statue monumentale **« L'Ouvrier et la Kolkhozienne »** (deux
figures de bronze brandissant faucille et marteau sur fond de ciel) ; p.323, reproduction d'une
peinture allégorique révolutionnaire française (portrait ovale en médaillon au ciel, œil de la
Providence, deux drapeaux tricolores, bonnet phrygien sur une pique, colonne portant des tables
inscrites, obélisque, personnages au premier plan). Aucune légende imprimée.

---

**3 — الكُليانية أو التوتاليتارية · `Totalitarisme` — p.324-326**

⚠️ **Gabarit différent** : la rubrique s'ouvre par un titre **\* التعريف :** puis n'a que
**deux** entrées — **■ لغة** et **■ فلسفيا**. **Il n'y a pas de ■ اصطلاحا.**

**■ لغة (verbatim)** :

> كلمة من **أصل لاتيني `Totus`** وتعني **الكلّ** أو **النسق الذي يرنو نحو الكليّة أو الشموليّة
> والوحدة**، كما تفيد في اللغة العربية **الصفة التي تطلق على أنظمة حكم معينة وأحيانا على فلسفة
> سياسية محددة**.

**■ فلسفيا (verbatim resserré — c'est la définition officielle du chapitre)** :

> تفيد **الكليانية** وصفا يُطلق على **نظريّة اجتماعيّة سياسيّة** أو على **إيديولوجيا** وعلى
> **صورة للتنظيم السياسي للمجتمع** تقوم على **ذوبان الأفراد والمؤسسات والجماعات وانصهارها في
> الكلّ الاجتماعي**، ويمثّل هذا الكلّ **قائد واحد يجمع كل السلطات**، وبذلك تعكس **الكليانيّة
> تجربة هيمنة سياسية بقيادة حزب واحد** إذ يقدّم **النّظام الكلياني صورة اتحاد الدولة والحزب
> لتكون الدولة أداة لتجسيد مشاريع الهيمنة** عبر **نسق من المعتقدات والقناعات والأساطير والطقوس
> والرموز** التي تعكس **معنى الوجود الاجتماعي وغايته**، وهي التي **تُعرّف الخير والشر بشكل قطعي
> وفق مبادئ وقيم الحزب وأهدافه**.

Suite imprimée (p.324) :

- Le régime appelle à **وحدة وطنية ذات طابع صوفي** ; au nom de cette unité, le **الزّعيم** est
  regardé comme **المصدر الأعلى للقوة وكأنّه يمثل إرادة الشّعب**.
- Sur cette base, **أجهزة الرّقابة السياسيّة** écrasent **كل معارض أو مخالف باعتباره يهدد الوحدة
  الوطنية**.
- **لا معنى في صلب هذا النظام لاستقلاليّة أي ميدان من ميادين الحياة الاجتماعية** — الإعلام، الفنّ،
  الدّين، الأخلاق… — « إذ **يجب أن يخضع كل شيء لنفوذ الدولة وتنظيمها فلاشيء يمكن أن يوجد خارج
  الدولة كما لا مكان للفرد خارج تنظيمها** ».

**L'opposition frontale que le manuel imprime (p.324, verbatim) — la distinction la plus
testable** :

> لتبدو **مبادئ الكليانية الضدّ المقابل لما جاءت به الثّورات البرجوازيّة الديمقراطيّة**، مثل
> مبادئ **حقوق الفرد الثابتة كالحرية والمساواة والمواطنة** وغيرها، وهي مبادئ **ترفضها الكليانية
> رفضا قطعيا** إذ **لا معنى لحرية الفرد والمعتقد**، بل ثمة فقط **أفكار صحيحة وأفكار خاطئة وأخرى
> ينبغي استئصالها**.

**Les signes distinctifs du régime totalitaire (p.324, liste imprimée — 9 items)** :
**الإيديولوجيا الرسمية** · **الحزب الواحد الذي يقوده مستبد** · **جهاز الرقابة البوليسي** ·
**إلغاء المنظّمات غير الرسمية** · **العنف العسكري أو شبه العسكري** · **محاصرة وسائل الإعلام
وتوجيهها** · **الرقابة المركزية** · **توجيه الاقتصاد في كليته** · **المشاركة الإلزامية للناس في
مشاريع الدولة**.

**Le trait commun malgré les écarts (verbatim)** : « يُشار بهذه التسمية إلى **أنظمة تتفاوت في عدد
من الخصائص**، إلاّ أنّها **تشترك في صفة احتكار قائد أو زعيم للسّلطة والنفوذ** » — exemples
imprimés : **ايطاليا موسوليني** · **ألمانيا هتلر** · **اسبانيا فرانكو**… وغيرها.

**دولة القائد (verbatim)** : « **لا تعني سوى غياب أية مقاييس واضحة ومعلنة لما هو شرعي أو قانوني
وطغيان مشيئة القائد**، ممّا يجعل **نمط الحكم الكلياني نمطا اعتباطيا نزويا كيفيا**، ممّا **يلغي
مبدأ حكم القانون وسيادته لتحل محله إرادة الفرد** ».

**Le prolongement contemporain — 4 relais nommés (p.324-325)** :

| Penseur (graphie imprimée + latin) | Ce que le manuel lui fait dire |
| --- | --- |
| **ريمون أرون** `Raymond Aron` (1905 – 1983) | Le **المجتمع الصناعي** est une cause de consolidation du pouvoir de l'État, par les changements des **قوى الإنتاج وخاصة التكنولوجيا** ; l'État tend **بحكم طبيعتها إلى الكلية أو الشمولية** parce qu'il est un **« مركبّ عسكري صناعي »** mêlant politique et économie dans un champ **إداري وتقني سلطوي**. L'État moderne **يستوعب المجتمع في كليته** ; l'idéologie du parti **لا تسلّم بوجود نزاعات** ; le régime monopolistique **يعمل بالخوف وبالإيمان**. |
| **هوركهايمر** `Horkheimer` (1895–1973), **مدرسة فرانكفورت** | Les sociétés totalitaires sont **شبيهة بنموذج المجتمع العبودي** — **القسمة النهائية بين القيادة والخضوع** ; la كليانية **تتطابق مع انتصار الأسطورة على العقل** ; critique de la raison contemporaine devenue **كليانيّة** puisque **استحال العقل عقل الدولة، عقلا علميا حسابيا**. |
| **يورغن هابرماس** `Habermas` (1929) | **العلم والتقنية** remplissent aujourd'hui la fonction **إضفاء الشرعيّة على الهيمنة** — que celle-ci s'exerce **باسم الديمقراطيات الليبيرالية أو باسم الأنظمة الاشتراكية** ; dans les deux cas on aboutit à **إلغاء كل احتمال نقدي ورفض القوّة التحررية التي يطلقها الفكر الجدلي**, si bien que la distinction entre régimes démocratiques et totalitaires devient **من قبيل التلاعب بالمصطلحات**. |
| **فوكو** `Foucault` (1926-1984) | Les **المجتمعات الانضباطية** — **مجتمعات مراقبة ومعاقبة واستثمار للإنسان واستعباده** ; on parle désormais de **مجتمعات سلطوية** où le pouvoir est **لامرئيّة** et se définit comme **إستراتيجيا** ou **« فعل في فعل في أفعال راهنة أو مستقبلية »**. |

**ريكور `Ricœur` (1913–2005) — citation imprimée en couleur (verbatim)** :

> « ومن هنا يكون لقولنا **إن الدولة سلطة أو إنها سلطة إرغام** معنى واحد، **لا أتكلم عن دولة قاسية
> ولا عن دولة مستبدة وإنما أتكلم عن الدولة في حد ذاتها** أي **عما يجعل الدولة دولة من خلال أنظمة
> وأشكال مختلفة وحتى متضادة** ».

**جيل دولوز `Deleuze` (1925-1995) — le pas de plus (p.325, verbatim resserré)** :

> بل لعلّنا **تجاوزنا … المجتمعات الانضباطية نحو مجتمعات المراقبة** : فإذا كان الفرد في
> **المجتمعات الانضباطية** يعرف **بإمضائه وبرقم أو عدد تسجيله**، ففي **مجتمع المراقبة** لا يهم
> الإمضاء ولا العدد **وإنما الرقم الذي يعد بمثابة كلمة السر** ؛ ففي حين **تنتظم المجتمعات
> الانضباطية عن طريق الأوامر** فإن **اللغة الرقمية للمراقبة تتحدد عبر الأرقام التي ترسم المنفذ
> إلى المعلومة**. **لم نعد نجد أنفسنا أمام الزوج الفرد – الجمهور** : فالأفراد **أصبحوا أجزاء**
> والجماهير **أصبحت نماذج أو معطيات سوق**.

⇒ **Distinction imprimée : المجتمعات الانضباطية (Foucault) ≠ مجتمعات المراقبة (Deleuze)** —
signature/numéro d'inscription ≠ **chiffre-mot de passe** ; ordres ≠ **langage numérique** ;
couple individu–masse ≠ **« أجزاء » / « معطيات سوق »**. C'est la distinction la plus fine de la
sous-partie.

**■ قيل في الكليانيّة (p.325-326, verbatim, 8 citations)** :

| Auteur (tel qu'imprimé) | Citation |
| --- | --- |
| **منتسكيو** | « يوجد **نوعان من الاستبداد** : الأوّل **مادي** ويتمثل في **العنف الذي تمارسه الدولة**، والثاني هو **الاستبداد بالرأي**، ويتجلى عندما **تفرض الدولة أمورا تزعج الطرق المألوفة في التفكير** ». |
| **دي لابينيه** | « **النظام الكلياني** هو الذي تظهر فيه **السلطات العامّة**، في تنظيمها للبلاد، **نزوعا مستمرا إلى استبدال المبادرات الشخصية للمحكومين بمبادراتها التحكمية الخاصة** ». |
| **لوفور** | « **الدولة الكليانية ليست دولة حيث تسود الاعتباطية**، بل هي **دولة تقوم على مبدأ يرفض الحق، يرفض الممارسة الحرة للتفكير** ». |
| **ماكس فيبر** | « **الدولة هي مجموع الأجهزة والمؤسسات التي تسعى إلى الهيمنة** مدعية أنها تحافظ على التوازن والوحدة في المجتمع لتكون **كل دولة كلية ومركزية حتى وإن ادعت أنها ضمان الحرية** ». |
| **حنّا أرنت** | « **تختلف النظم الكليانية في جوهرها عن مختلف أشكال القمع السياسي الأخرى**… فالنظام الكلياني **يحوّل دوما الطبقات إلى كتل**، **ولا يحل محل نظام الأحزاب دكتاتورية الحزب الواحد وإنما حركة جماهيرية**، **تنقل مركز سلطة الجيش إلى الشرطة** ». |
| **كيرزيو مالبرت** | « في ظل النظام الكلياني، **ما لا يعد ممنوعا يكون إجباريا** ». |
| **ريمون أرون** | « يفترض النظام الكلياني **خمس خصائص أساسية** : **1 –** هو نظام **يحتكر فيه حزب واحد النشاط السياسي**. **2 –** يكون هذا الحزب **مسلحا بإيديولوجيا رسمية** تتسم **بإطلاقية النفوذ** وتمثل **الحقيقة الرسمية للدولة**. **3 –** لنشر هذه الحقيقة الرسمية **تستأثر الدولة بوسائل القوة والإقناع ومجموع وسائل الاتصال** مثل الصحافة المكتوبة والمرئية والمسموعة **لتكون موجهة من قبل الدولة ومن يمثلها**. **4 –** **تخضع الدولة كل الأنشطة والفعاليات الاقتصادية والمهنية** لتكون معبرة عن الدولة، وبما أن الدّولة لا تنفصل عن إيديولوجيتها فإن هذه الأنشطة **تلون بلون الحقيقة الرسمية**. **5 –** بما أن كل نشاط يغدو **فعالية من فعاليات الدولة** وخاضعا للإيديولوجيا الرسمية فإن النظام الكلياني **يقترن بضرورة بسيادة العنف أو الرعب السياسي والإيديولوجي** ». |
| **موسوليني** | « **إن كل شيء في الدولة، لا شيء خارج الدولة، ولا شيء ضدّ الدّولة** ». |

⇒ Les **5 caractéristiques de Raymond Aron** sont numérotées dans la source : c'est la liste
fermée la plus sûre du chapitre.

**Tableau imprimé p.326 — مفاهيم مجاورة / مفاهيم مناقضة (الكليانية)** :

| **مفاهيم مجاورة** (voisins) | **مفاهيم مناقضة** (contraires) |
| --- | --- |
| الشمولية | الديمقراطية |
| الديكتاتورية | الليبيرالية |
| الفاشية | الفوضوية |
| الاستبداد | الفصل بين السلط |
| الحكم المطلق | المواطنة |
| الطغيان | — |

⚠️ **Les deux colonnes n'ont pas le même nombre d'entrées** : **6 voisins** contre **5
contraires** — vérifié à 200 dpi, ce n'est pas une ligne coupée. Aucun appariement ligne à ligne
n'est donc possible ici.

**\* لمزيد التعمّق (p.326)** — un encadré unique à **trois onglets** (bande latérale bleue
portant les mots **السياسة** · **اللائكية** · **الكليانية**), avec les listes de sites telles
qu'imprimées (fautes de frappe de la source comprises) :

- **السياسة** : `Fr.wikipedia.org/wiki/politique` · `Fr.wikipedia.org/wiki/la politique(Aristote)`
  · `www.olats.org/schoffer/defpol.htm` ·
  `Fr.encarta.mcn.com/dictionary/2016024631/politique.html` ·
  `www.aquadesign.be/news/article/8420php`
- **اللائكية** : `Fr.wikipedia.org/wiki/laicité` ·
  `www.assemblée-nationale.fr/cite/jeune/laicité/acceuil/acceuil.asp` · `http://www.laicite.be/`
- **الكليانية** : `www.wikipedia.org/wiki/totalitarisme` ·
  `www.wikibéral.org/wiki/index.php?title=totalitarisme` ·
  `Hypo.ge/dip.etat/ge.ch/www/cliotexte/html/definition_.totalitarisme`

Illustrations p.326 : petite photo (dans la bande d'onglets) d'une employée devant un écran
d'ordinateur ; grande photo d'un **échiquier** dont une main déplace une pièce. Sans légende.

---

###### 3.1.3.2 سياقات فكريّة — p.327-334

Trois courants exposés, **numérotés par le manuel** : **1 – الليبيراليّة** (p.327-329),
**2 – الفوضويّة** (p.330-331), **3 – فلسفة العقد الاجتماعي** (p.332-334).

**Gabarit imprimé (commun aux trois)** : **\* التعريف** → **\* الجهاز المفهومي** →
**\* تنبيهات** → **\* لمزيد التعمّق**. Deux écarts : الليبيرالية met **الجهاز المفهومي avant
تنبيهات** comme les autres, mais **فلسفة العقد** remplace la fin de ses تنبيهات par un renvoi
imprimé **« ( انظر الجدول المصاحب ) »** vers le **tableau comparatif de la p.334**.

---

**1 — الليبيراليّة · `Libéralisme` — p.327-329**

**\* التعريف (verbatim)** :

> **مذهب فكري أو فلسفي سياسي** يعتبر أن **الإجماع الديني لا يمثل شرطا ضروريا لتنظيم اجتماعي
> سليم**، ويدعو إلى **حريّة الفكر حقّا للجميع**، كما يؤكّد على **ضرورة الحدّ من سلطة الدولة قياسا
> لحريات الأفراد**، وظهرت **الليبيراليّة السياسيّة في القرن الثامن عشر نقيضا للمُلكية المطلقة
> والاستبداديّة** وهو ما يعكس موقفا يقوم على **احترام استقلاليّة الآخرين** ويدعو إلى **التسامح
> والثقة في آثار الحرية ونتائجها**. وعلاوة على طابعها السياسي، تُفهم الليبيرالية أيضا بما هي
> **مذهب اقتصادي للمؤسسة الحرّة**، بحيث **لا يمكن للدّولة أن تتدخل في عرقلة قوانين لعبة التنافس**.

⇒ **Deux faces déclarées d'emblée : ليبيرالية سياسيّة / مذهب اقتصادي للمؤسسة الحرّة** — la
distinction sera reprise et systématisée dans les تنبيهات (p.329).

**Les fondateurs (verbatim, dates imprimées)** : **جون لوك (1632 – 1704)** · **روسّو
(1712–1778)** · **ستيوارت ميل (1806 – 1873)**.

**Le noyau commun (verbatim)** : « ورغم الاختلاف القائم بين هؤلاء المنظرين، توجد **قواسم مشتركة
تتمحور حول حرية الفرد** التي تعتبر **جوهر التيار الليبيرالي** ».

**La distinction des deux despotismes (verbatim) — très testable** :

> فالليبيرالي يصبو على نحو خاص إلى **التحرر من التسلط بنوعيه** : **تسلط الدولة (الاستبداد
> السياسي)**، و**تسلط الجماعة (الاستبداد الاجتماعي)**.

**La généalogie tracée par le manuel (p.327)** :

- **ديمقراطيي أثينا في القرن الخامس قبل الميلاد** — ils ont insisté sur **أهمية الفرد والحريات
  الفردية**, avec **بروتاغوراس** : **« الإنسان مقياس كل شيء »**.
- **الرواقيين** — mais sur un autre principe : **وحدة الطبيعة والإنسان ومشاركة جميع البشر فيها** ;
  et surtout l'importance de découvrir **حيزا في الذات الإنسانية لا تستطيع أن تنفذ إليه سلطة
  المجتمع أو أي شكل آخر من أشكال السلطة** — une fois ce for intérieur découvert, l'individu jouit
  d'**قدر من السيادة والحرية لا يتأثر بأي عوامل**.
- **Note de vocabulaire imprimée (verbatim)** : « **ولئن نشأت الليبيرالية وتطورت في القرن السابع
  عشر، فإن لفظتي ليبيرالية وليبرالي لم تصبحا متداولتين إلاّ بداية من القرن التاسع عشر** ».
  ⇒ **Distinction chose / mot** : la doctrine est du 17ᵉ, les mots du 19ᵉ.

**Locke — le raisonnement reconstruit par le manuel (p.327, verbatim resserré)** :

- Contexte : **تاريخ انكلترا في القرن 17** = histoire d'un conflit entre **الملكية الساعية إلى
  الحفاظ على ما اعتبرته حقها المطلق في الحكم** et **القوى البرلمانية المصرّة على الحد من سلطة
  الملوك وإخضاع هذه السلطة لحكم الدستور** ; conflit aggravé par **تداخل النزعات الدينية
  والمذهبية** et par le refus parlementaire de tenir que **الملك يحكم بمشيئة إلهية**.
- L'argument : « **وإذا افترضنا مع لوك أن للإنسان حقوقا طبيعية في الحرية والكرامة، وجب أن نقر
  بأن نسق الحكم الوحيد الذي لا يتعارض مع هذا الافتراض هو الحكم المبني على رضا المحكوم
  وموافقته** ».
- La conséquence institutionnelle : si **الشعب مصدر السلطة الشرعية**, alors **يصبح الحكم مسألة
  أمانة لا مسألة حق** — que le gouvernant prétende ce droit **متوارثا أو هبة من الإله** ; et le
  pouvoir devient **مشروطا حيث يكون الحاكم خاضعا لرقابة المحكوم بشكل دائم**.

⇒ **Distinction imprimée : الحكم أمانة ≠ الحكم حق.**

**La loi que le manuel dégage (p.327-328, verbatim)** : « فكأن **الليبيرالي يفترض وجود علاقة
عكسية بين سلطة الدولة وحرية الفرد** : فكلما **ازدادت سلطة الدولة أصبحت حريات الفرد ضيقة** ».

**Adam Smith — le versant économique (p.328, verbatim resserré)** :

- **أدام سميث (1723 – 1790)** — أكد على **ضرورة الالتزام بالحريات الفردية وخصوصا الحرية
  الاقتصادية** ; **اختزل مهمة الدولة في حماية حقوق المواطن، خصوصا حق الملكية الفردية وتسهيل
  تعامله مع الآخرين**.
- **المحرك الوحيد للإنسان في تصرفاته هو خدمة مصالحه، وإرضاء ذاته** ⇒ le meilleur service de
  l'État est **تسهيل سعي الأفراد خدمة لمصالحهم الخاصة، دون تدخل مفتعل**, « **وكأن هناك يدا خفية
  تحدد الأدوات وتنسق الحركات** ».
- ⇒ **أدرج أدام سميث مبدأ الاقتصاد الحر مبدأ التنافس الحر في الليبيرالية كنظام اقتصادي**.

**Stuart Mill — la réserve sur la loi majoritaire (p.328, verbatim)** :

> ويعتبر الليبيراليون أنه **لا يكفي أن نطلق « شعار الحرية الفردية في ظل سيادة القانون »** إذ
> **يخشى أن يؤدي وضع القانون في يد الأغلبية الديمقراطية إلى تقلص مجال الحرية الفردية وتعاظم شأن
> الدولة** ؛ لذلك دافع **ستيوارت ميل** على ضرورة **الاعتراف بمجال خاص بالفرد** مانحا بذلك الفرد
> **حريّة مطلقة في الحيز الذي يخصه** كما يمنح **الدولة حق التدخل فقط فيما يتعلق بالحيز العام**.

⇒ **Distinction imprimée : الحيز الخاص (liberté absolue de l'individu) ≠ الحيز العام (seul champ
d'intervention légitime de l'État).**

**\* الجهاز المفهومي (p.328, 6 entrées, verbatim)** :

| Concept | Définition imprimée |
| --- | --- |
| **■ الحرية** | « هي **حالة من يفعل ما يشاء وليس ما يشاء الآخر بدلا منه**، وهي أيضا **غياب القيود الخارجيّة**. **فالإنسان الحرّ هو ذاك الذي لا يكون عبدا أو سجينا**. والحريّة من وجهة نظر اجتماعيّة وسياسيّة ليبراليّة هي **حالة الفرد في صلاته مع المجتمع والسّلطة السياسيّة**، وهي **الحقّ المعترف به للفرد وتحدّ من نفوذ الدولة** : **حريّة التفكير، الحرية الشّخصيّة وحريّة الاجتماع**، وهي **تقتضى ما لا يلحق الضرر بالآخرين** ». |
| **■ الفرد** | « هو **الشّخص الذي يعترف له بوجود مستقل وبحقّ التّصرّف وفق إرادته الخاصة والمطلقة**. ويفيد في التصّور اللّيبرالي **الشّكل الأهمّ للواقع والقيمة الأسمى** ». |
| **■ الحق** | Distinction en deux : **الحق الطبيعي** = « ما **يخوّل للإنسان الفرد بموجب طبيعته**، وهو حقّه في **الحريّة والملكيّة** وكلّ ما يعدّ جزءا ممّا يعتبر **حيّزا شخصيا في حياة الفرد** » ; **الحق المدني** = « **التصرّف وفق ما يشرّعه القانون وما يبيحه أو يمنعه** ». |
| **■ التسامح** | « **حالة للفكر وقاعدة للسّلوك** تقضي بالسّماح **لكلّ واحد أن يعبّر عن رأيه بحريّة حتّى وإن كنّا لا نشاركه الرّأي أو نعارضه فيه**، فلا يحق لأحد أن يكون له **امتياز يفرض بموجبه الصمت على الآخر** ». |
| **■ المنافسة** | « **مفهوم اقتصادي بالخصوص**، ويقال أساسا على **العلاقة التي تقوم بين المنتجين والتجّار** والتي تحكمها **قيم المصلحة الخاصة والربح**، ولا يحق للدولة في التصور الليبيرالي **التّدخل إلاّ لتأمين حق الفرد في الملكية والثروة التي يحصّلها من المنافسة الحرّة** ». |
| **■ العدالة** | « **لا تفيد إلغاء التفاوت** وإنما تعني **تكافؤ الفرص** من ناحية و**توفير ما يساعد الفرد على تحقيق الثراء ومزيد الرّفاه** ». |

⇒ **العدالة ≠ إلغاء التفاوت** : c'est la définition la plus contre-intuitive de la liste, donc la
plus discriminante.

**\* تنبيهات (p.328-329, verbatim)** — l'avertissement porte sur la distinction des deux
libéralismes : « **رغم الصلات العضوية القائمة بين الاقتصادي والسّياسي، ورغم القواسم المشتركة
التي توجد بين اللّيبيراليّة السّياسيّة واللّيبيرالية الاقتصاديّة، فبالإمكان التمييز بينهما** » :

- **■ في السّياق السياسي** : la ليبيرالية exprime une position qui, **مع لوك `Locke` ومنتسكيو
  `Montesquieu` (1689 – 1755)**, **يعظّم التّسامح، ويمتدح الحريّة الفرديّة سيّما حرّية التفكير**
  et exige de la protéger **بالحدّ من نفوذ الدّولة وذلك بالتّفرقة بين السّلطات التّشريعيّة
  والتّنفيذيّة والقضائيّة**.
- **■ في السّياق الاقتصادي** : la **اللّيبيرالية الكلاسيكيّة** — **آدم سميث `Adam Smith`**,
  **مالتوس `Malthus` (1766 – 1834)**, **ريكاردو `Ricardo` (1772–1823)**, **ستيوارت ميل
  `John Stuart Mill`** — forme un courant qui **يرفض تدخّل الدّولة في قانون اللّعبة الاقتصاديّة**
  et pose l'existence de **قوانين طبيعيّة بما هي نظام تسيير ذاتي قادر على تأمين التّوازن بين
  العرض والطّلب**, à condition de respecter **المنافسة والملكيّة الخاصّة لوسائل الإنتاج**.
- **على خلاف اللّيبيراليّة الجديدة مع هاياك `Hayek` (1899 – 1992)** — celle-ci **تجيز تدخّلا ما
  للدّولة في الشّأن الاقتصادي، دون أن تلغي مبدأ المنافسة الحرّة أو حريّة المؤسّسة، ودون أن
  تتراجع عن رفضها للخيار الاشتراكي وللدّولانية**.

⇒ **Distinction imprimée : الليبيرالية الكلاسيكيّة ≠ الليبيراليّة الجديدة (هاياك)** — la
seconde **autorise une intervention** de l'État sans renoncer à la concurrence libre ni accepter
le socialisme.

**\* لمزيد التعمّق (p.329, verbatim)** :
**ج. ستيوارت ميل** : *مبادئ الاقتصاد السياسي* ; *في الحريّة* ; *النفعية* ·
**ج. ج. روسّو** : *في العقد الاجتماعي* · **ج. لوك** : *مقالة في الحكم المدني* ;
*رسالة في التسامح* · **أ. سميث** : *بحوث حول طبيعة ثروة الامم وأسبابها* ·
**توكفيل** : *الديمقراطيّة في أمريكا* · **منتسكيو** : *روح القوانين*.

Illustration p.329 : bas-relief circulaire en pierre — figure féminine drapée assise, la main
posée sur une tablette portant l'inscription **`LOI`** (allégorie de la Loi). Sans légende.

---

**2 — الفوضويّة · `Anarchisme` — p.330-331**

**\* التعريف (verbatim)** :

> **تصور سياسي يهدف إلى إنشاء مجتمع دون سلطة أو هيمنة** حيث يكون للأفراد **حرية التصرف والتعاون
> فيما بينهم**.

**Étymologie imprimée (verbatim)** : ويُردّ أصل المصطلح إلى اللغة اللاتينية `Anarcia` المشتق من
اليونانية `An` (**دون**) و`arkhe` والذي يعني **المبدأ الذي يقوم عليه شيء ما والذي يتكوّن منه، أي
جوهره أو طبيعته التي تمنحه قانون صيرورته ووجوده**. ⇒ « **فإن الأصل الاشتقاقي للكلمة يفيد عموما ما
ليس له أصل أو مبدأ موجه**، وهو ما يترجم **بغياب النفوذ أو غياب السلطة السياسية** ».

**La formule-clef (verbatim)** : « في ضوء هذا التحديد يمكننا القول إنّ **الفوضوية تعني النظام دون
قيادة أو قائد** ».

**Ce que le manuel pose comme cœur de toute philosophie anarchiste** : **إرادة تحرير فردية
أو/وجماعية** ; « **فعشق الحرية المتأصل لدى الفوضويين يقودهم للنضال من أجل تحقيق مجتمع أكثر عدلا
حيث تجد الحريات فضاء تحققها بشكل متناغم وتشكل أساس التنظيم الاجتماعي والعلاقات الاقتصادية
والسياسية** ».

**Ce que l'anarchisme refuse et ce qu'il défend (verbatim)** :

> **ترفض الفوضوية بشكل قطعي الفكرة القائلة بضرورة السلطة القهرية والمهيمنة في المجتمع**، وتدافع
> في المقابل على **شكل من التنظيم الاجتماعي والاقتصادي فوضوي، نصير الحرية المطلقة** أي **مؤسس
> على التعاون والمشاركة بدل القهر والهيمنة**.

**L'ennemi commun (verbatim)** : **السلطة والنفوذ والهيمنة والقهر** — d'où **تُعدّ الدولة العدو
الأساسي للفوضويين** : la définition retenue de l'État est ici **« الجهاز الذي يحتكر حق ممارسة
العنف وحق التحكم في الأفراد ( القهر، الإخضاع، الخدمة العسكرية ) »**.

**Le principe philosophique — ce qui fait déborder l'anarchisme hors de la théorie politique
(verbatim)** :

> ولعل أساس هذا الموقف الفوضوي إنما يتحدد في **مبدأ يقوم على رفض كلي لكل ضروب الدوغمائية**، وبهذا
> المبدأ **تتجاوز الفوضوية حدود النظرية السياسية لتعلن انخراطها في الفكر الفلسفي**. وبرفضها كل
> عقيدة **تدعو الفوضوية إلى استقلالية الوعي الأخلاقي**، وتعلن **رفضا للقواعد الأخلاقية التي تحدد
> الفعل وتوجهه**. **فالفعل فيما وراء الخير والشر هو المبدأ الأساسي للسلوك**، إذ **يريد الفوضوي
> أن يكون حرا في أن يفكر بذاته وأن يعبر بحرية عن أفكاره وآرائه**.

**La mise au point contre le contresens (p.330, verbatim) — la distinction la plus testable de la
rubrique** :

> **فلا ينبغي أن تفهم الفوضوية على معنى رفض النظام بل ينبغي أن تفهم على معنى « النظام دون
> سلطة »** على حد عبارة **برودون**.

Précisions imprimées autour :
- Les anarchistes dits **تلقائيين أو عفويين** tiennent que la société **يتحوّل إلى نظام طبيعي
  بشكل تلقائي بمجرّد تحرره من العوائق والموانع الاصطناعية التي تفرضها الدّولة**.
- D'autres jugent que **مفهوم النظام ليس أقل اصطناعا من مفهوم الدولة ذاته** ; d'où : la seule
  manière de sortir de **تراتبية السلطة** est **القضاء على النظام القهري والعمل على منع قيامه**.
- Le moyen proposé : **إقامة تنظيم ذاتي للأفراد عن طريق الفيدراليات** — moyen qui permet
  **مراقبة المؤسسات الاجتماعية الاستبدادية وفضح تبريراتها الإعلامية بصورة مستمرة**.
- **لامركزية النفوذ** signifie **مشاركة كل طرف في الحياة العامّة مع الحفاظ على الاستقلالية
  الفردية**.

**\* الجهاز المفهومي (p.330-331, 5 entrées, verbatim)** :

| Concept | Définition imprimée |
| --- | --- |
| **■ الحرية** | « تُفهم على معنى **استقلالية الإرادة وغياب كل أشكال القهر والإلزام**، وهي بهذا المعنى **حرية مطلقة** ». |
| **■ الدولة** | « **سلطة قهر وهيمنة** بما هي **مؤسسة أو جهاز يحتكر حق ممارسة العنف وحق التحكم في الأفراد وتسييرهم** ». |
| **■ الفرد** | « **كيان سياسي يتحدد وجوده باستقلالية عن كل أشكال الهيمنة**، أو هو **كائن مستقل بذاته، ويتمتع بحرية مطلقة** ». |
| **■ النظام الطبيعي** | « هو **نظام دون سلطة**، أو هو **نظام تسيير ذاتي** سواء عن طريق **التعاونيات أو الفيدراليات**، وهو أيضا ضرب من النظام القائم على **التصرف المباشر في الحياة الخاصة** وعلى **مشاركة الأفراد في الحياة العامة دون أن تمثل هذه المشاركة نفيا للاستقلالية الفردية** ». |
| **■ الملكية** | « هي في عرف الفوضويين **سرقة** » — et surtout la distinction ci-dessous. |

**La distinction الملكية الخاصة / الملكية الفردية (p.331, verbatim) — le point le plus
contre-intuitif de toute la نافذة** :

> ويميّز الفوضويون بين **الملكية الخاصة** و**الملكية الفردية** ؛ وإن كان الفوضويون **لا يرفضون
> الملكية الخاصة بما هي الخير الضروري والحيوي للأفراد** فإنهم **يرفضون الملكية الفردية التي تمثل
> قوام استغلال الإنسان للإنسان وأساس الهيمنة والنفوذ**، بحيث **تفهم الملكية الخاصة على معنى تملك
> شخص ما لذاته** في حين **تفيد الملكية الفردية تملك الآخرين بغاية الحصول على الثروة**.

⚠️ **L'emploi des deux termes est ici l'inverse de l'usage courant** (« الملكية الخاصة » y est
acceptée, « الملكية الفردية » rejetée). C'est bien ce qu'imprime la source, vérifié à 200 dpi.
Toute question sur ce couple doit citer les deux gloses du manuel, pas les mots seuls.

**\* تنبيهات (p.331) — les 3 courants de l'anarchisme (verbatim)** :

> توجد **اتّجاهات فوضويّة عديدة**، ويعدّ **التيّار الفوضوي الاجتماعي** و**التيّار الفوضوي
> الفرداني** و**التيّار الفوضوي البيئوي** **أهم التيّارات في صلب الحركة الفوضوية**.

| Courant | Ce que le manuel lui attribue |
| --- | --- |
| **● التيار الاجتماعي** | La société anarchiste **يمكن أن يتشكّل عبر التعاونيات أو النّظم الجماعية أو المؤسّسات النقابية أو المجالس الاستشاريّة**. Point central : **إلغاء الملكيّة والاستحواذ الجماعي على وسائل الإنتاج**. La فوضويّة اجتماعيّة a été tenue pour **جسرا بين الاشتراكيّة والفردانيّة** (via coopératives, fédérations, conseils) ; son combat : **مقاومة الرأسماليّة من جهة وكل النّظم الاستبداديّة من جهة أخرى**. Chefs de file : **برودون `Proudhon` (1809–1865)** puis **باكونين `Bakounine` (1814 – 1876)**, qui représenta **اتجاه الأغلبية في صلب الأمميّة الأولى** jusqu'à la scission conduite par **ماركس `Marx` (1818 – 1883)**, laquelle **أقصى الفوضويّين البرودونيّين والباكونينيّين**. |
| **● التيّار الفرداني** | **الفرد فقط يمكنه أن يمتلك بشكل مشروع ما يعدّ خيرا خاصّا** ; défense du **حقّ الفرد في التّملّك الخاص والفردي** ; suppression des **المؤسّسات السّلطوية** soit **بالتخلّي عنها** soit **بمحاربتها** ; la **حرّية الفرد** est vue **ضدّا مقابلا لهيمنة المجتمع ومؤسّساته** ; confiance dans les **المؤسّسات الوسيطة المتولّدة عن النّشاط التعاوني بين الأفراد** pour **إفشال مخطّطات الدولة**, **شريطة ألاّ تساهم في فعل الهيمنة**. |
| **● التيار البيئوي أو الايكولوجي** | **يرفض كل أشكال الاقتصاد الصّناعي وكل أشكال الاستغلال التكنولوجي للطبيعة والعالم** ; **قطب ثالث للفكر الفوضوي** proposant **إمّا العودة إلى الطبيعة (العيش في مجتمع بدائي) أو مراقبة الأفراد للتكنولوجيا ومواجهة أشكال استغلالها للطبيعة**. |

**\* لمزيد التعمّق (p.331, verbatim)** : **ريمون آرون** : *من عائلة مقدسة إلى أخرى* ·
**بيار كلاستير** : *المجتمع ضد الدولة* · **كارل ماركس** : *بيان الحزب الشيوعي* ·
**برودون** : *ما الملكية ؟* · **باكونين** : *الإله والدولة*.

---

**3 — فلسفة العقد الاجتماعي · `La philosophie du contrat` — p.332-334**

**\* التعريف (verbatim resserré)** :

> **فلسفة التعاقد أو فلسفة العقد** هي **فلسفة سياسية بالأساس** أو **اتجاه فلسفي سياسي يمتد بين
> القرنين 17 و18**. وتتميز، **رغم الاختلاف بين ممثليها**، بـ**رفض تأسيس الدولة على الحق الإلهي**
> وبالتالي **رفض الدولة الدينية أو اللاهوتية**، كما تعلن **رفضا للطبيعة المدنية للإنسان أي رفض
> الأساس الطبيعي للدولة**.

⇒ **Double refus déclaré : ni fondement divin, ni fondement naturel de l'État.** C'est la
définition la plus discriminante de la rubrique.

**La مسلّمة fondatrice (verbatim)** :

> إذ تتمثل **المسلمة الأساسية التي تقوم عليها فلسفة التعاقد** في اعتبار **الاجتماع الإنساني
> اصطناعا إراديا وليس ظاهرة طبيعية**، وهو ما يقتضي الإقرار بأن **إنشاء المجتمع تم بموجب قرار
> إنساني يتمثل في التعاقد**.

**Les trois définitions emboîtées (verbatim)** :

| Terme | Définition imprimée |
| --- | --- |
| **التعاقد** | « **اتفاق يلتزم بمقتضاه شخص أو عدة أشخاص تجاه شخص أو عدة أشخاص بتقديم شيء ما، أو بعدم القيام بشيء ما** ». |
| **العقد** | « ما يكون **ثنائي الطرف أو متعدد الأطراف**، أي **ما يتضمن التزامات أو تعهدات متبادلة** ». |
| **العقد الاجتماعي** | « **مجموع المواثيق أو المواضعات الأساسية، التي تتضمنها الحياة في المجتمع** على الرغم من كونها **لم تعلن وربما لم تضبط أبدا ضبطا شكليا** ». |

**Ce que vise la philosophie du contrat (verbatim)** : « ولعل الفلسفة السياسية التي تنادي بتأسيس
الدولة على التعاقد إنما تقصد **عقلنة الفعل السياسي** » — l'organisation requise repose sur le
fait que **يضع كل واحد شخصه وما له من قوة أو كامل قدرته على أساس الشراكة، تحت تصرف القيادة العليا
أو الإرادة العامة** en échange d'être traité **بصفته عضوا في الجسم السياسي أو جزءا من كل**.

**La formule du troc contractuel (verbatim)** :

> وهو ما يعني أن **فلسفة التعاقد تستدعي تنازل الأفراد بمقتضى العقد عن بعض حقوقهم الطبيعية أو
> كلّها مقابل اكتسابهم لحقوق مدنية أساسها المساواة والعدل** وما يترتّب عليهما من **شعور بالأمن
> والطمأنينة**.

**Reformulation-synthèse (p.332, verbatim)** :

> إن **فلسفة العقد** إذن **نظرية في نشوء الدولة والقانون** تردّ الاجتماع إلى **اتفاق بين الأفراد،
> يدخلونه بمحض إرادتهم**، و**يتنازلون بمقتضاه عن بعض حقوقهم**، و**يتعهدون فيه باحترام حقوق
> الآخرين وحرياتهم وملكيتهم**.

**حالة الطبيعة — le concept sans lequel rien ne se comprend (p.332, verbatim)** :

- Statut du concept : **فلئن اعتبر لوك `Locke` أن هذه الحالة واقعة تاريخية فإن بقية فلاسفة العقد
  اتخذوا منها فرضية عمل** لإضفاء مشروعية على leur conception politique, donc pour **تأسيس الدولة
  وتأسيس الحاجة إليها وتشريع نفوذها**.
  ⇒ **Distinction imprimée : Locke = fait historique / les autres = hypothèse de travail.**
- Sens : **حالة غياب الدولة أو حالة ما قبل نشأة المجتمع المدني**.
- Contraste : « وإذا كان **نظام الحياة في المجتمع المدني عقلانيا** فإنه في **حالة الطبيعة قائم
  على غلبة الأهواء والانفعالات** ».
- Les deux appuis de la doctrine : **حالة الطبيعة من ناحية** و**طبيعة الإنسان وحقوقه الطبيعية من
  ناحية أخرى**.
- Le double moteur du passage : (1) **طبيعته العدوانية أو طبعه العاطفي أو خضوعه للدوافع
  والانفعالات** ; (2) **حاجة الأفراد إلى الاتحاد في مجتمع بحكم عجزهم على حفظ بقائهم بشكل فردي
  ومستقل** — c'est ce qui **يبرر حتمية الانتقال من حالة الطبيعة إلى الحالة المدنية**.
- Ce que le passage change (verbatim) : **من وضع تغيب فيه الدولة إلى وضع يحتكم إلى سلطة الدولة**,
  ou **من وضع يحتكم إلى سيادة الحق الطبيعي إلى آخر قوامه القانون المدني أو الحق المدني أي الحق
  الذي يضمنه القانون**.
- La logique du contrat (verbatim) : **تعاقد قوامه المنطق الحسابي أو حساب المصالح الذي يقوم على
  جدلية التنازل مقابل تحقيق مكاسب** — mekasib qui **تختلف باختلاف النظر إلى طبيعة الإنسان
  وحاجاته الملحة**.

**\* الجهاز المفهومي (p.333, 8 entrées, verbatim)** :

| Concept | Définition imprimée |
| --- | --- |
| **■ حالة الطبيعة** | « هي **الوضع الذي كان عليه الناس قبل نشأة المجتمع المدني والدولة**، وتقال **في مقابل الحالة المدنية**. وهي **حالة مفترضة أو متصورة تصوّرا عقليا وليست مرحلة تاريخية** ». ⚠️ **Contradiction imprimée, arbitrée ici** : la p.332 écrit que **لوك** tient حالة الطبيعة pour une `واقعة تاريخية` et que **les autres** philosophes du contrat en font une `فرضية عمل` ; la glose du جهاز المفهومي (p.333) énonce en revanche, sans réserve, `وليست مرحلة تاريخية`. La glose vaut donc pour la **doctrine générale du contrat**, **pas** pour Locke. ⚠️ **Ne jamais poser de question fermée** du type « حالة الطبيعة : historique ou hypothétique ? » sans nommer l'auteur. |
| **■ الحق الطبيعي** | « هو **القوة الطبيعية ذاتها** أي **جملة القوى التي منحتها الطبيعة للإنسان**، وهو أيضا **ما يخوّل للإنسان القيام به بموجب الطبيعة أو بموجب القانون الطبيعي** ». |
| **■ الإرادة العامة** | « هي **عمل محض للإدراك** الذي ينظر، **في صمت الأهواء**، إلى **ما يمكن الإنسان أن يطلبه من نظيره، وما يحق لهذا الإنسان أن يطلبه من نظيره، وما يحق لهذا النظير أن يطلبه منه**، كما تفيد **إرادة الجسم الاجتماعي المتحد في مصلحة مشتركة**. والإرادة العامة هي **الأساس الشرعي لكلّ سيادة عند روسو** ». |
| **■ الطبيعة البشرية** | « **مقولة تحيل على معطيات الإنسان الطبيعية والتي تحدد أفعاله وعلاقاته** ». |
| **■ المجتمع المدني** | « **مجتمع القانون والمؤسسات المدنية** في مقابل **المجتمع الذي تحكمه السلطة الدينية أي المجتمع الثيوقراطي**. وتعدّ **الدولة في فلسفة التعاقد مؤسسة من مؤسسات المجتمع المدني ووسيلته لتحقيق مصالح أعضائه**، ويتجسّد المجتمع المدني في **تشريعات تنظم الملكية، وعلاقات الإنتاج، وتوزيع الثروة في المجتمع** ». |
| **■ القانون** | « هو **النظام والنّاموس أو التشريع** الذي يفيد **مجموع القواعد العامة الملزمة والمفروضة على الإنسان** والتي **تحدد حقوقه وواجباته** أو **ما يحق له المطالبة به وما يجب عليه الامتناع عن القيام به** ». |
| **■ القوة** | « **القدرة والشّدة ويقابلها الضعف**، والقوّة **مقابلة للحقّ لأنّها ليست حقّا، وإنّما هي وسيلة للدّفاع عن الحقّ، أو لمنع صاحب الحقّ من التمّتع بحقّه** ». |
| **■ الحرية** | « **نميز بين الحرية الطبيعية بما هي حرية مطلقة والحرية المدنية بما هي حرية نسبية ترتبط بطاعة القانون** ». |

**Les deux distinctions imprimées à l'intérieur de ces entrées — les plus testables** :

1. **الإرادة العامة ≠ إرادة الجميع** (Rousseau, verbatim) : « إذ **تهتمّ الأولى بالمصلحة
   المشتركة، والثانية بالمصلحة الخاصة**، وسميت خاصة لأنها **تفكر في الجزء لا في الكل** وهي لأجل
   ذلك **لا تعبرّ عن المواطنة وإنما عن الأنانية** ».
2. **الطاعة ≠ الخضوع** (verbatim) : « **الطاعة في هذا المعنى تختلف عن الخضوع، إذ أن الإنسان حين
   يطيع القانون لا يطيع سيدا بل يطيع سلطان العقل أو يطيع سلطان نفسه من جهة كونه ساهم في تشريع
   القانون**، إذ أن **الإنسان أنشأ القانون لكي لا يطيع أحدا** ». ⇒ conclusion imprimée :
   **« وعلى هذا الأساس لا تمثل الحرية نقيض الضرورة وإنما نقيض العبودية »**.

**Précision imprimée sur القوة / العنف (p.333, verbatim)** : « **والإفراط في استعمال القوة هو
العنف** إذ يُعدّ **العنف مضادا للرفق، ومرادفا للشدة والقسوة**، **وكلّ فعل شديد يخالف طبيعة الشيء،
ويكون مفروضا عليه من خارج فهو، بمعنى ما، فعل عنيف**، والعنف **يمكن أن يُعدّ شرعيا إذا ما كان
مطابقا للقانون وغير شرعي إذا ما انتهك القانون** ».

**\* تنبيهات (p.333, verbatim)** :

> **رغم وجود قواسم مشتركة بين فلاسفة العقد الاجتماعي، ينبغي التأكيد على ضروب الاختلاف بينهم، وهو
> اختلاف يبلغ حد التناقض أحيانا** سواء في **تحديد طبيعة الدولة** أو في **بلورة غايتها**، وهو ما
> يتجلى من خلال **هذا الجدول المقارن بين نماذج من فلاسفة العقد**.
> **( انظر الجدول المصاحب )**

**\* لمزيد التعمّق (p.333, verbatim)** : **سبينوزا** : *رسالة في اللاهوت والسياسة* ;
*رسالة السياسة* · **روسو** : *في العقد الإجتماعي* ; *في أصل التفاوت بين البشر وأسسه* ·
**هوبس** : *التنين* ; *في المواطن* · **هيغل** : *مبادئ في فلسقة الحق* `[sic — « فلسقة » pour
« فلسفة », coquille de la source]`.

⇒ **Noter** : *رسالة السياسة* (Spinoza) est **l'œuvre du نصّ مطوّل** de la p.339-345, annoncée
ici. Et **هيغل n'est pas un philosophe du contrat** — il figure pourtant dans cette
bibliographie ; le manuel ne le justifie pas.

---

###### Le tableau comparatif des 4 philosophes du contrat — p.334 (pleine page, verbatim)

C'est **la page la plus dense en matière testable de toute la tranche** : 4 auteurs × 6 rubriques,
imprimée sans un mot de commentaire.

En-têtes imprimés (de droite à gauche) : **الفلسفة** ·
**هوبس `Hobbes` 1588-1679** · **روسو `Rousseau` 1712-1778** ·
**لوك `Locke` 1632-1704** · **سبينوزا `Spinoza` 1632-1677**.

**■ حالة الطبيعة**

| Auteur | Cellule (verbatim) |
| --- | --- |
| **هوبس** | حالة **صراع وحرب الكل ضد الكل**، ناتجة عن **طبيعة الإنسان المولع بالحرية والهيمنة**. إذ يُعدُّ **عدوانيا وشريرا بطبعه**. |
| **روسو** | حالة **سلم**، يتميز فيها الإنسان **بضمير عاطفي**، وهو **مسالم وفزع** وأمام كل خطر **يكون الفرار حركته الأولى**، فضلا عن تميزه **بالحرية المطلقة**. |
| **لوك** | حالة **تمتع بالحقوق الطبيعية في ظل سيادة القانون الطبيعي** الذي يضمن **حق الحياة والحرية والملكية**. |
| **سبينوزا** | حالة **تتسم بهيمنة القوي على الضعيف، وسيادة قانون الغاب**، بحكم أن **الحق الطبيعي هو القوة الطبيعية ذاتها**، ولذلك **يمتد الحق بقدر ما تمتد القوة**. |

**■ العقد الاجتماعي**

| Auteur | Cellule (verbatim) |
| --- | --- |
| **هوبس** | **تنازل الأفراد كليا عن كل ما لهم من قوة وحقوق طبيعية لصاحب السيادة**. |
| **روسو** | **تنازل الأفراد عن حقوقهم الطبيعية لصالح الإرادة العامة**. |
| **لوك** | **تنازل الأفراد عن بعض حقوقهم لصالح السلطة المدنية**. |
| **سبينوزا** | **تنازل الأفراد عن تسيير شؤونهم بأنفسهم وفق منطق الانفعال وتنظيم الحياة وفق مقتضيات العقل**، لذلك **لا يمثل العقد تنازلا عن الحق الطبيعي بل تأمينا له**. |

**■ أطراف العقد**

| Auteur | Cellule (verbatim) |
| --- | --- |
| **هوبس** | **الأفراد دون صاحب السيادة**. |
| **روسو** | **بين الأفراد والإرادة العامة التي تعبر عن المجموع**. |
| **لوك** | **بين الأفراد والسلطة الحاكمة**. |
| **سبينوزا** | **بين الأفراد والسلطة الحاكمة**. |

⚠️ **لوك et سبينوزا ont ici la même cellule, mot pour mot** — c'est la seule ligne où deux colonnes
coïncident ; toute question de type « qui dit quoi » doit éviter cette ligne, ou l'utiliser
précisément pour ce qu'elle est (le point où les deux ne se distinguent pas).

**■ التزامات العقد**

| Auteur | Cellule (verbatim) |
| --- | --- |
| **هوبس** | **على الأفراد طاعة الحاكم والذوبان في إرادته مقابل تأمين الأمن والسلام**. |
| **روسو** | **وجوب طاعة الجميع للإرادة العامة مقابل تأمين الحقوق المدنية مثل الحرية والملكية**. |
| **لوك** | **على الحاكم مثل الأفراد الالتزام بالعقد واحترام حق الجميع في الحرية والملكية**. |
| **سبينوزا** | **على الأفراد طاعة القانون مثلما على الحاكم أن يحترم حق الأفراد في الحرية**. |

**■ نظام الحكم**

| Auteur | Cellule (verbatim) |
| --- | --- |
| **هوبس** | **نظام استبدادي والسلطة فيه مطلقة**. **نظام دولة التنين** أو **نظام رئاسي**. |
| **روسو** | **نظام الحكم ديمقراطي مباشر والسلطة فيه مطلقة للإرادة العامة**. **نظام دولة الحق**. |
| **لوك** | **نظام الحكم تمثيلي والسلطة فيه مقيدة برأي الأغلبية في برلمان تقتصر عضويته على أصحاب الممتلكات**. **نظام دولة الوفاق**. |
| **سبينوزا** | **نظام الحكم ديمقراطي**. **نظام دولة الحرية**. |

⇒ Les quatre « noms d'État » sont un quadruplet parfaitement disjoint :
**دولة التنين (هوبس)** · **دولة الحق (روسو)** · **دولة الوفاق (لوك)** · **دولة الحرية
(سبينوزا)**.

**■ غاية الدولة**

| Auteur | Cellule (verbatim) |
| --- | --- |
| **هوبس** | **حفظ الحياة وضمان الأمن والسلام**. |
| **روسو** | **سيادة الشعب وتأمين المصلحة العامة**. |
| **لوك** | **تأمين الخيرات المدنية : الحرية الفردية والملكية الخاصة**. |
| **سبينوزا** | **العيش وفق نظام العقل وضمان الأمن والحرية**. |

⇒ **غاية الدولة عند سبينوزا** est exactement ce que dit la citation d'ouverture de la نافذة
(p.319) et ce que développera le نصّ مطوّل (p.339-345) : la boucle est imprimée par le manuel
lui-même.

##### 3.1.4 نافذة كيفيّات التفكير — p.335-338

> **Pages lues** : p.335–338 (intégral, rendu `hi/t-3xx.png` ≈ 200 dpi ; chaque encadré revérifié
> par recadrage ×3).
> **Source** : manuel élève `210402P00`, مبحث 3.1 « الدّولة : السّيادة والمواطنة ».
> ⚠️ **Écart de gabarit à signaler d'emblée** : la نافذة ne porte **aucun sommaire imprimé** sur sa
> page d'ouverture (contrairement à la نافذة دعائم, p.319, qui en imprime un). Les تمارين ne sont
> pas annoncés : on ne les découvre qu'en tournant la page.

**p.335 — page d'ouverture de la نافذة.** Titre imprimé en écriture calligraphique sur deux lignes,
séparées par un filet rouge : **كيفيات** / **التفكير**. ⚠️ Le mot **نافذة n'est pas imprimé** dans
le titre de la page (il n'apparaît que dans le فهرس) — la page ne dit que « كيفيات التفكير ».

Image pleine page (cadre orange) : **une chouette effraie posée dans l'embrasure d'une vieille
fenêtre à six carreaux**, l'intérieur noir. C'est le visuel d'ouverture de la نافذة كيفيات التفكير
— **la chouette de Minerve**, allusion classique à la philosophie. Aucune légende imprimée.

Encadré-citation en bas de page, avec **portrait photographique de باشلار** (verbatim) :

> « **إنّ فتنة الوضوح السريع فتنة عظمى** ».
> — **باشلار**, *الفكر العلمي الجديد*

⇒ La citation d'ouverture donne le **mot d'ordre méthodologique** de toute la نافذة : se défier de
l'évidence rapide. C'est exactement ce que les quatre مهارات vont opérationnaliser (reconstruire la
question au lieu de la recevoir toute faite).

---

###### Gabarit imprimé des تمارين

La نافذة enchaîne **4 تمارين numérotés** (le chiffre est imprimé en rouge dans un bandeau
« تمرين N » à losanges orangés, en haut à droite). ⚠️ **Le gabarit n'est PAS uniforme** — aucun des
quatre n'a exactement la même composition :

| Bloc imprimé | 1 (p.336) | 2 (p.336-337) | 3 (p.337) | 4 (p.338) |
| --- | :-: | :-: | :-: | :-: |
| **المهارة المستهدفة** | ✅ | ✅ | ✅ | ✅ |
| *consigne dans un encadré propre* | ⛔ | ✅ (« ما دلالة… ») | ⛔ | ✅ (**المهمّة**) |
| **توضيح** | ✅ | ✅ | ✅ | ⛔ |
| **السند** | ✅ (دولوز–قاتاري) | ⛔ | ✅ (هوبس) | ⛔ |
| **المهام** | ✅ (4) | ⛔ | ✅ (5) | ⛔ (**المهمّة**, au singulier) |
| **التمشّيات** | ⛔ | ✅ (4 étapes, cadre jaune) | ⛔ | ✅ (3 مراحل, bulles) |

Trois écarts à retenir :

1. **Le تمرين 2 n'a ni سند ni مهام** : il enchaîne **المهارة → question → توضيح → التمشّيات**.
   C'est le seul purement méthodologique, sans texte à travailler.
2. **Le تمرين 4 est le seul sans توضيح** — et le seul dont la consigne s'appelle **المهمّة** (au
   singulier) et non **المهام**.
3. Les **تمشّيات ne sont imprimées que sur 2 et 4** — et sous **deux formes graphiques
   différentes** : cadre jaune à 4 lignes numérotées implicitement (تمرين 2, p.337) vs **3 bulles
   nommées** (تمرين 4, p.338).

⇒ Les **trois توضيح (تمارين 1, 2, 3) sont la matière la plus directement enseignée de la نافذة** :
ce sont les seuls endroits du chapitre où le manuel dit *comment* on pense, et non *ce que* pense
un auteur.

---

###### تمرين 1 — p.336 · الكشف عمّا يبرّر طرح مشكل فلسفي

**■ المهارة المستهدفة (verbatim)** :

> **الكشف عمّا يبرّر طرح مشكل فلسفي.**

**■ توضيح (verbatim intégral)** :

> تُعرّف **الفلسفة** بكونها **فنّ طرح المشاكل**؛ ومعنى هذا أن **المشكل لا يُطرح بذاته بل يُبنى في
> ضوء جملة من الاعتبارات** من بينها **« المبرّرات »** أي **الدواعي النظريّة والعمليّة** وكذلك
> **الرّهان من وراء التفكير فيه**. وهذا ما يجعل **المشكل الفلسفي مشكلا ذا معنى بالنسبة إلى
> الإنسان**.

⇒ **La distinction la plus testable de la page** : **المشكل لا يُطرح بذاته، بل يُبنى** — le
problème n'est pas donné, il est *construit*. Et les trois composantes de cette construction sont
nommées : **الدواعي النظريّة** · **الدواعي العمليّة** · **الرّهان**.

**■ السند (p.336)** — extrait de **جيل دولوز – قاتاري**, *الرأسماليّة والفُصام*.
Référence imprimée en toutes lettres sous l'encadré :
**G. DELEUZE, F. GUATTARI ; *Capitalisme et Schizophrénie*, t I, éd. de Minuit, 1972, pp. 36-37.**

⛔ Texte sous droits — **non recopié** (R-2). Ce qu'il pose, restitué :

- Le texte part de ce qu'il désigne comme **مشكل الفلسفة السياسيّة الأساسي** — et il l'attribue
  nommément : **« المشكل الذي أحسن سبينوزا طرحه »**, redécouvert ensuite par **رايش** (Reich).
- La formule de ce problème, telle que le manuel l'imprime entre guillemets :
  « **لماذا يناضل الناس من أجل عبوديتهم كما لو كان الأمر متعلّقا بخلاصهم ؟** »
- Le mouvement du texte : ce qui doit étonner n'est **pas** la révolte (voler, faire grève) mais
  **son absence** — que les affamés ne volent pas, que les écrasés ne fassent pas grève ; et que
  les hommes supportent depuis des siècles **الاستغلال والإذلال والاستعباد** au point de les
  **réclamer**, « **لا فقط للآخرين بل لأنفسهم أيضا** ».

⇒ **Ce que le سند illustre de la مهارة** : le problème philosophique n'est pas « la servitude
est-elle un mal ? » (question déjà tranchée), c'est **le renversement de l'étonnement** — c'est le
*désir* de servitude qui est le problème. Le texte est là pour montrer un problème **construit**,
pas reçu.

**■ المهام (p.336, verbatim, telles qu'imprimées)** :

> **المهام :**
> أعيد صياغة المشكل بوضوح.
> – أستحضر بعض الوقائع من المجال السياسي تدفع إلى التفكير فيه
> – ما هيّ الإحراجات النظريّة الكامنة وراء طرحه ؟
> – فيم تساعدني صياغة المشكل كما وردت في النصّ على : **تعقّل الوقائع التي استحضرتها** و**فكّ
> الإحراجات النظريّة التي انتبهت إليها** ؟

⚠️ Typographie de la source : la **première tâche n'a pas de tiret**, les trois suivantes en ont
un ; et « **ما هيّ** » est imprimé avec une **شدّة sur le ي** (pour « ما هي ») — coquille de la
source, laissée telle quelle.

⇒ Les المهام dessinent le **تمشّي (la démarche) en 4 temps** que la مهارة exige :
**1) reformuler le problème** → **2) convoquer des faits politiques qui y poussent** →
**3) dégager les impasses théoriques (الإحراجات) qui le sous-tendent** →
**4) éprouver le gain de la formulation** sur les deux plans à la fois (les faits *et* les
impasses). C'est le seul endroit du chapitre où un تمشّي de ce type est imprimé pas à pas.

---

###### تمرين 2 — p.336 · تحديد دلالة مفهوم

**■ المهارة المستهدفة (verbatim)** :

> **تحديد دلالة مفهوم.**

**■ La consigne, dans son encadré propre (verbatim)** :

> **ما دلالة « المجتمع المدني » ؟**

**■ توضيح (verbatim intégral)** :

> **تقتضي هذه المهارة :**
> – **استبعاد دلالة سابقة** ( سائدة مثلا )
> – **اختيار مرجعيّة نظريّة لاعتمادها في التحديد**.
> – **إبراز الطابع الإجرائي للمفهوم** على اعتبار أن **دلالته تسمح بحلّ مشكل ما**.

⇒ **Les 3 opérations de la définition philosophique, telles que le manuel les numérote** :
**1) écarter un sens antérieur** (typiquement le sens **سائد**, dominant) → **2) choisir une
référence théorique** sur laquelle adosser la définition → **3) faire apparaître le caractère
opératoire (إجرائي) du concept**, c'est-à-dire ce qu'il permet de *résoudre*.

⚠️ C'est la liste fermée la plus sûre de la نافذة : **3 opérations, ni plus ni moins**, et la
troisième porte le critère de validité (**une bonne définition est celle qui résout un problème**).

⚠️ **Aucun سند, aucune مهام pour ce تمرين** — c'est le seul des quatre dans ce cas.
Le concept mis en travail (**المجتمع المدني**) n'est **pas** défini par le manuel ici : il est
donné **comme exercice**, pas comme contenu. ⇒ **La p.336 ne définit pas** المجتمع المدني — elle
le donne à définir. Mais le مبحث le définit **ailleurs**, deux fois : au `الجهاز المفهومي` de
فلسفة العقد (**p.333**) et au ¶1 du نصّ مطوّل (**p.340**). ⇒ C'est **exactement** la
`مرجعيّة نظريّة` que la تمشّية 3 du تمرين 2 demande d'aller chercher : renvoyer l'élève à la
p.333, pas lui dire que la notion n'est pas traitée.

**■ التمشّيات (p.337, cadre jaune à 4 lignes encadrées, verbatim)** — la démarche s'imprime **en
haut de la page suivante**, détachée de son تمرين :

> **التمشّيات :**
>
> 1. **أستحضر دلالة شائعة للمجتمع المدني**.
> 2. **أبحث عن بعض المؤشّرات وأبيّن بها هشاشة هذه الدلالة**.
> 3. **أختار مرجعيّة نظريّة وأحدّد من خلالها دلالة المجتمع المدني**. أراعي في ذلك **التوافق مع
>    المؤشرات التي أثرتها في التمشّي الثاني**.
> 4. **أبيّن إجرائيّة هذه الدلالة من خلال بيان ما تستطيعه لمعالجة مشكل ما**.

⚠️ **Piège de mise en page** : ces التمشّيات ouvrent la p.337, **avant** le bandeau « تمرين 3 ».
Elles appartiennent au **تمرين 2** (le mot **المجتمع المدني** y revient trois fois) — une lecture
page à page les rattacherait à tort au تمرين 3.

⇒ **Correspondance exacte توضيح ↔ تمشّيات** (le manuel opérationnalise ses 3 opérations en 4 pas) :

| Opération du توضيح | Pas de la تمشّية |
| --- | --- |
| **استبعاد دلالة سابقة (سائدة)** | **1** convoquer le sens courant → **2** en montrer la **هشاشة** par des **مؤشّرات** |
| **اختيار مرجعيّة نظريّة** | **3** — avec l'exigence supplémentaire de **cohérence avec les مؤشّرات du pas 2** |
| **إبراز الطابع الإجرائي** | **4** — montrer ce que la définition **permet de traiter** |

⚠️ Le pas 2 est **dédoublé** par rapport au توضيح : écarter le sens dominant ne suffit pas, il faut
**établir sa fragilité par des indices**. C'est la seule exigence que le توضيح ne dit pas et que la
تمشّية ajoute.

---

###### تمرين 3 — p.337 · بيان حدود أطروحة

**■ المهارة المستهدفة (verbatim)** :

> **بيان حدود أطروحة.**

**■ توضيح (verbatim intégral)** :

> – **الأطروحة هي الموقف الذي يدافع عنه الكاتب ويسعى إلى إقامة الحجّة على وجاهته باعتباره حلاًّ
> لمشكل فلسفي مستبعدا بذلك أطروحات أخرى**.
> – **يقتضي بيان حدود الأطروحة في حلّ المشكل :**
> **مواجهتها بوقائع تكذبها**.
> **بيان تناقض داخلي فيها**.
> **بيان تهافت أساسها**.
> **بيان استتباعاتها الخارقة**

⚠️ La quatrième ligne est imprimée **sans point final** — la liste s'arrête net. Vérifié à ×3, ce
n'est pas une ligne coupée.

⇒ **La définition de l'أطروحة est la plus complète du chapitre** — elle tient en 4 traits :
c'est **موقف** · **défendu par un auteur** · **argumenté comme حلّ لمشكل فلسفي** · **et qui, ce
faisant, en écarte d'autres** (`مستبعدا بذلك أطروحات أخرى`). Ce dernier trait est celui qu'on
oublie : une thèse n'est pas seulement ce qu'on soutient, c'est ce qui exclut.

⇒ **Les 4 voies pour montrer les limites d'une thèse — liste fermée, la plus testable de la
نافذة** :

| # | Voie (verbatim) | Ce qu'on attaque |
| :-: | --- | --- |
| 1 | **مواجهتها بوقائع تكذبها** | les **faits** — la thèse est démentie par le réel |
| 2 | **بيان تناقض داخلي فيها** | la **cohérence** — elle se contredit elle-même |
| 3 | **بيان تهافت أساسها** | le **fondement** — son point de départ ne tient pas |
| 4 | **بيان استتباعاتها الخارقة** | les **conséquences** — ce qu'elle entraîne est inacceptable |

⇒ Les 4 sont **disjointes et complètes** : fait / cohérence / fondement / conséquence. C'est le
quadruplet le plus sûr de la tranche, et il vaut pour **n'importe quelle** thèse — donc il est
réutilisable hors du chapitre.

**■ السند (p.337)** — **هوبس**, *اللوفياثان* **(الفصل 30)**.

⛔ Texte sous droits — **non recopié** (R-2). Ce qu'il pose : ôtez l'obéissance (donc la concorde
du peuple) à n'importe quelle forme d'État, et le peuple se dissoudra en peu de temps ; ceux qui se
révoltent **en croyant réformer** la république découvriront qu'ils la **détruisent**. La formule
que retient le manuel : « **أنّهم بذلك يهدمونها** ».

⇒ **Ce que le سند illustre de la مهارة** : une thèse forte (l'obéissance est la condition
d'existence du corps politique) posée assez nettement pour qu'on puisse en chercher les
**حدود** — c'est le matériau, pas la leçon.

**■ المهام (p.337, verbatim, 5 tâches)** :

> **المهام :**
> – **أحدّد القضيّة الخلافيّة التي يدور حولها الجدل**.
> – **أصوغ هذه القضية في شكل سؤال إشكالي**.
> – **أحدّد أطروحة هوبز وأطروحة خصومه**.
> – **أستخلص حجّته على وجاهة موقفه**.
> – **أتبيّن حدود الأطروحة**.

⚠️ **Coquille de la source à ne pas propager** : la référence sous le texte imprime **هوبس** (avec
س), alors que la 3ᵉ tâche, six lignes plus bas, imprime **هوبز** (avec ز). **Les deux graphies
cohabitent sur la même page.** Le reste du chapitre (نافذة دعائم, tableau du contrat p.334) emploie
**هوبس** — c'est la graphie à retenir pour tout le chapitre.

⇒ Le تمشّي des 5 مهام : **isoler la question litigieuse** → **la mettre en forme de سؤال إشكالي**
→ **identifier les deux thèses en présence** (celle de l'auteur *et* celle de ses adversaires) →
**dégager son argument** → **seulement alors, en montrer les limites**. ⇒ **Les limites viennent en
dernier** : le manuel interdit de critiquer avant d'avoir reconstruit.

---

###### تمرين 4 — p.338 · القدرة على التأليف

**■ المهارة المستهدفة (verbatim)** :

> **القدرة على التأليف**

**■ المهمّة (verbatim intégral)** — au singulier, dans son propre encadré :

> **هل تبرّر حاجتنا إلى الأمن التضحيّة بالحريّة ؟**
> **أجيب عن هذا السؤال في فقرة لا تتجاوز العشرين سطرا متبعا في ذلك التمشيات المصاحبة**.

⚠️ **Contrainte de format imprimée** : **20 lignes maximum**. C'est le seul endroit du chapitre où
le manuel chiffre la longueur attendue d'une production.

⇒ La question posée est **exactement le nœud du chapitre** (الأمن ↔ الحريّة) : c'est l'arbitrage
qui oppose la lecture hobbesienne à la lecture spinoziste du contrat, et que le نصّ مطوّل (p.339-345)
va trancher côté Spinoza. Le manuel place donc la production écrite **entre** le سند de هوبس (p.337)
et le texte long de سبينوزا (p.339).

**■ Les 3 مراحل (p.338, bulles orangées, verbatim)** — ce sont les « **التمشيات المصاحبة** »
annoncées par la مهمّة :

**● مرحلة بناء المشكل**

> – **أبيّن ما يبرر معالجة هذا السؤال**.
> – **أشير إلى أهميّة السؤال**.
> – **أستخلص مشكلا فلسفيّا أصوغه بوضوح**.

**● مرحلة بلورة الجواب**

> – **أبيّن دلالة القول بالتضحية بالحريّة من أجل الأمن**.
> – **أستحضر بعض المؤيّدات** ( **تقديم حجة على الأقل** )
> – **أعترض عليه ببيان حدود وجاهته** ( من خلال **الكشف عن ضمنية أو استتباع أو تناقض مع الواقع** ).
> – **أقترح بديلا وأوضّحه**.
> – **أستدل على وجاهته**.

**● مرحلة الاستخلاص**

> – **أستخلص الموقف النهائي**.
> – **أشير إلى قيمته**.

⇒ **C'est le plan officiel de la production philosophique**, en 3 étapes et 10 gestes :
**بناء المشكل (3)** → **بلورة الجواب (5)** → **الاستخلاص (2)**. Rien d'autre dans le chapitre ne
donne ce squelette.

⇒ **Le point le plus fin** : la مرحلة بلورة الجواب est **dialectique et obligatoirement complète** —
elle exige les cinq gestes dans l'ordre : *expliciter* la thèse → *l'appuyer* (au moins **une**
preuve) → *l'objecter* → *proposer une alternative* → *la prouver à son tour*. Un devoir qui
s'arrête à l'objection n'a pas fait la moitié de l'étape.

⚠️ **Le rappel des 3 modes d'objection reprend le توضيح du تمرين 3, mais pas à l'identique** :
ici la parenthèse en nomme **trois** — **ضمنية** (un implicite) · **استتباع** (une conséquence) ·
**تناقض مع الواقع** (un démenti par le réel) — alors que le تمرين 3 en imprimait **quatre**
(faits / contradiction interne / fondement / conséquences). Les listes **ne coïncident pas** :
l'objection par le **تهافت الأساس** disparaît, et le **تناقض داخلي** est remplacé par un
**تناقض مع الواقع**, tandis que la **ضمنية** apparaît ici pour la première fois.
⇒ Ne jamais présenter ces deux listes comme une seule.

⚠️ **La moitié basse de la p.338 est vide** — la نافذة s'arrête là. Aucun encadré
« لمزيد التعمّق », aucune illustration : contrairement à la نافذة دعائم, cette نافذة **ne comporte
ni bibliographie ni sitographie**.

---

##### 3.1.5 نافذة نصّ مطوّل — سبينوزا, *كتاب السّياسة*, الفصل الثّالث — p.339-345

> **Pages lues** : p.339–345 (intégral).
> ⛔ **Le texte de Spinoza n'est pas recopié** (R-2). Ce qui est transcrit ici, c'est
> **l'appareil du manuel** : titre, référence, découpage en paragraphes numérotés, numérotation des
> lignes, et **les repères marginaux — mot pour mot**, car ce sont eux, et non le texte, qui
> constituent la lecture officielle imposée par le manuel.

**p.339 — page d'ouverture.** Titre imprimé en calligraphie sur deux lignes séparées d'un filet
rouge : **نافذة** / **نصّ مطوّل**. ⚠️ Contrairement à la نافذة كيفيات التفكير (p.335), **le mot
« نافذة » EST imprimé ici** — les deux pages d'ouverture du chapitre ne sont pas titrées de la
même façon.

Trois images, dont deux légendées :

| Image | Légende imprimée |
| --- | --- |
| Détail de peinture : **deux mains tournant les pages d'un livre enluminé** (manche rouge, reliure dorée, page ornée d'une miniature) | *aucune* |
| **Couverture du livre** : collection en calligraphie en haut, **كتاب السياسة** · **سبينوزا** · **ترجمة وتقديم جلال الدين سعيد** · **دار الجنوب للنشر** · **تونس** | **▲ رسالة السياسة** |
| **Portrait gravé de Spinoza** (buste, cheveux longs, jabot blanc) | **سبينوزا (1632 – 1677) ► SPINOZA** |

⚠️ **Incohérence de la source, à ne pas lisser** : la **couverture reproduite porte
« كتاب السياسة »**, mais la **légende du manuel dit « رسالة السياسة »**. Le titre courant des
p.340-345 dit, lui aussi, **كتاب السّياسة**. ⇒ **Titre de référence à retenir : كتاب السّياسة** ;
« رسالة السياسة » n'apparaît qu'une fois, dans cette légende.

Encadré-citation (cadre rouge, verbatim) :

> « **يبدو جليّا أنّ الدولة أي حقّ السلطة العليا ، لا يعدو أن يكون إلا حقّ الطبيعة الذي لا يتحدّد
> بقوّة كل شخص بمفرده ، و إنّما بقوّة الجمهور الذي يسلك كما لو كان بدافع روح واحدة** ».
> — **سبينوزا**

⚠️ **Cette citation d'ouverture n'est pas un hors-texte** : c'est **le paragraphe 2 du texte
lui-même** (p.340, lignes 11-13), reproduit à l'identique en vitrine. Le manuel affiche donc
d'avance **la thèse-clef** : *le droit de l'État = le droit de nature déterminé par la puissance de
la multitude, non par celle de chaque individu séparé*.

⚠️ Coquilles de la source dans cet encadré : espaces avant les virgules et le point final, et
**« بمفرده »** est imprimé précédé d'un **point parasite** (`شخص .بمفرده`) — même accident qu'à la
p.340, ligne 12.

---

###### La mise en page du texte long — l'appareil de lecture (p.340-345)

C'est **la strate la plus exploitable de la tranche** : le manuel ne se contente pas de donner un
texte, il **impose son découpage**. Trois dispositifs superposés :

1. **Titre courant + référence.** Sur chaque page : **نصّ مطوّل** en haut à droite, le titre
   **كتاب السّياسة** en calligraphie rose au centre, **الفصل الثالث** à gauche. Sous le titre, un
   encadré jaune de référence (p.340, verbatim) :

   > **ترجمة جلا ل الدّين سعيد**
   > **دار الجنوب للنشر تونس ص48-57**

   ⚠️ Le nom du traducteur est imprimé avec une **coupure parasite** : « جلا ل » au lieu de
   « جلال ». ⇒ Lire **جلال الدّين سعيد**. La pagination de l'édition source est **ص 48-57**.

2. **Paragraphes numérotés en rose** : `1–`, `2–`, `3–`… en tête de chaque paragraphe, dans la
   marge intérieure de la colonne. **C'est la numérotation d'articles de Spinoza lui-même** (le
   *Traité politique* est écrit en articles), reprise telle quelle.

3. **Numérotation des lignes de 5 en 5** (`5`, `10`, `15`, `20`, `25`…) dans la marge de la
   colonne. ⇒ **La citation d'une ligne précise est possible**, et c'est ce que le manuel attend.

4. **Repères marginaux dans une bande jaune**, chacun pointé par **un triangle jaune** vers
   l'endroit exact du texte qu'il commente. ⚠️ Ces repères **ne sont pas des titres de
   paragraphe** : ils ne coïncident pas avec la numérotation en rose. Ce sont les **étapes du
   mouvement argumentatif** telles que le manuel les découpe — c'est **le plan de lecture
   officiel**.

⇒ **Réponse à la question posée par le brief** : oui, le dispositif du مبحث 2 est reconduit ici
(repères marginaux + numérotation des lignes), et il est même **plus riche** : s'y ajoute la
**numérotation des paragraphes en rose**, absente du مبحث 2.

---

###### Le plan de lecture, repère par repère

**p.340 — الفصل الثالث · paragraphes 1 à 3 (lignes 1 à ~28)**

| Repère marginal (verbatim) | Ce qu'il commande |
| --- | --- |
| **تحديد مفهومي : الدولة، المجتمع المدني، المواطن والرعيّ.** | ¶1 — le texte s'ouvre sur **quatre définitions**, pas sur une thèse. |
| **الإعلان عن المبحث الأوّل : حقّ الدولة على المواطنين.** — **– تحديد طبيعة حقّ الدولة وأساسه : قوّة الجمهور.** | ¶1 fin / ¶2 — annonce de l'objet, puis **la thèse-clef** (celle de l'encadré p.339). |
| **تناسب الحق والقوة في علاقة بالفرد والدولة.** | ¶2 fin — le **rapport de proportion** droit/puissance. |
| **المجتمع المدني لا يحتكم إلى سلطة الأهواء.** | ¶3 — ce que la société civile **exclut**. |
| **مخاطر سلطة الأهواء على الفرد والدولة.** | ¶3 fin — les conséquences. |

⇒ **Les 4 définitions liminaires du ¶1, telles que le texte les pose** (c'est le matériau
conceptuel le plus sûr de la page, et il recoupe les تحديدات de la نافذة دعائم) :

| Terme | Ce qu'il désigne dans le texte |
| --- | --- |
| **المجتمع المدني** | le nom donné à **toute دولة**. |
| **المدينة** | le nom donné au **corps de l'État dans son ensemble** (هيئة الدولة بأكملها). |
| **شؤون الدولة** | les **الشؤون العامة** administrées par **صاحب السلطة**. *(Imprimé : `وتُسمَّى الشؤون العامة التي يديرها صاحب السلطة شؤون الدولة.` — le terme **défini** est `شؤون الدولة`, le reste en est la définition.)* |
| **مواطنون** | les hommes **en tant qu'ils jouissent de tous les avantages de la cité selon le droit civil**. |
| **رعايا** | les mêmes, **en tant qu'ils sont tenus d'obéir aux lois de la cité et de se soumettre à ses institutions**. |

⚠️ **La distinction مواطن / رعيّ est la plus testable du texte** : ce ne sont **pas deux groupes de
personnes**, ce sont **deux rapports** — *les mêmes hommes*, considérés du côté du **bénéfice**
(مواطن) ou du côté de l'**obligation** (رعيّ). Une question qui en fait deux populations distinctes
est fausse.

⇒ Le ¶1 annonce aussi les **3 types d'الاجتماع المدني** : **الديمقراطي** · **الارستقراطي** ·
**الملكي** — mais **le texte les met de côté** pour traiter d'abord **الحق الأعلى للمدينة، أي حق
السلطة العليا**. ⇒ Les trois régimes sont **annoncés et non traités** dans l'extrait retenu.

⇒ **¶2, la thèse** : le droit de l'État **ne dépasse pas le droit de nature**, mais ce droit
n'est **pas** mesuré par la puissance de chaque individu séparé — il l'est par **قوّة الجمهور**
agissant « comme mû par un seul esprit ». Conséquence imprimée : le droit de chaque citoyen
**décroît à proportion de l'excès de la puissance de la cité sur la sienne**
(`يتضاءل بقدر تفوّق قوة المدينة على قوّته الشخصية`).

⇒ **¶3, le raisonnement par les trois cas** — c'est un raisonnement **par disjonction exhaustive**,
donc parfaitement restituable : si la cité accorde à quelqu'un le pouvoir de vivre à sa guise,
elle **abdique son propre droit** ; si elle l'accorde à **deux ou plus**, elle introduit **الشقاق**
en elle ; si elle l'accorde à **chacun des citoyens**, elle **se détruit elle-même** et tout
« retourne à l'état de nature » (`تعود الأشياء جميعا إلى طور الطبيعة`).

---

**p.341 — paragraphes 4 à 6 (lignes ~29 à 66)**

| Repère marginal (verbatim) | Ce qu'il commande |
| --- | --- |
| **نشأة الدولة لا تستوجب التنازل عن الطبيعي بل شرط حفظه.** | ¶3 fin — **le point anti-hobbesien du texte**. |
| **تحديد منزلة المواطن في المدينة.** | ¶5 |
| **اعتماد منهج فرضي استنتاجي لبيانها.** | ¶5 — **un repère de méthode**, pas de contenu. |
| **ألاحظ الأسلوب السجالي الذي يعتمده الكاتب** | ¶6 — idem, et **à la 1ʳᵉ personne**. |
| **اعتماد أسلوب الدحض** | ¶6 — idem. |
| **طاعة القانون لا تتعارض مع الحريّة.** | ¶6 fin |

⚠️ **Trois des six repères de cette page ne portent pas sur le contenu mais sur la MANIÈRE** —
`منهج فرضي استنتاجي` · `الأسلوب السجالي` · `أسلوب الدحض`. Et l'un d'eux, **ألاحظ…**, est écrit
**à la première personne** : c'est une **consigne au lecteur**, pas un titre. ⇒ La bande jaune
mélange **deux régimes** : des intertitres analytiques (majoritaires) et de rares **instructions de
lecture**. Ne pas les traiter comme une liste homogène.

⇒ **Le repère le plus important du texte est ici** :
**« نشأة الدولة لا تستوجب التنازل عن الطبيعي بل شرط حفظه »** — la naissance de l'État **n'exige
pas** l'abandon du droit naturel, elle en est la **condition de conservation**. C'est **la ligne de
partage entre Spinoza et Hobbes**, et elle est **imprimée par le manuel lui-même**, donc
objectivée : le tableau de la p.334 le disait déjà (`لا يمثل العقد تنازلا عن الحق الطبيعي بل
تأمينا له`). ⇒ **La boucle p.334 ↔ p.341 est la plus sûre du chapitre.**

Le mouvement des ¶4-6, restitué :

- **¶4** — absurdité de laisser chaque citoyen **interpréter les lois à sa guise** : chacun
  deviendrait **حَكَمًا على أعماله الشخصية**, pourrait justifier n'importe quoi sur un **حقّ وهمي**,
  et organiserait sa vie **على هواه** — « **وهذا مُحال** ».
- **¶5** — d'où le statut du citoyen : **ليس مستقلاًّ وإنّما هو يخضع للمدينة** ; nul n'a le droit de
  décider **par lui-même** ce qui est juste ou injuste, louable ou blâmable, car le corps de l'État
  doit **agir selon une pensée unifiée** et **exprimer la volonté de tous**.
- **¶6 — l'objection et sa réfutation** (c'est là que le repère `أسلوب الدحض` s'applique) :
  *objection* — n'est-il pas contraire à la raison de se soumettre entièrement au jugement d'autrui ?
  *réfutation* — si c'était vrai, l'état civil serait **déraisonnable** et n'aurait pu être institué
  que par des êtres **sans raison** ; or la raison n'enseigne rien de contraire à la nature, et elle
  enseigne **التوق إلى السّلم**. D'où le **renversement** : **كلّما كان عيش المرء على مقتضى العقل،
  أي كلّما كان حرّا، زاد مراعاة لشرائع المدينة** — *plus on est libre, plus on obéit aux lois*.

⇒ **La formule la plus contre-intuitive du texte, donc la plus discriminante** :
**حرّية ↑ ⇒ obéissance aux lois ↑**. Une question qui pose l'inverse (liberté = moins de lois) est
fausse *pour ce texte*, alors qu'elle serait juste pour la ليبيرالية de la p.327
(`علاقة عكسية بين سلطة الدولة وحرية الفرد`). ⇒ **Le chapitre contient les deux thèses opposées, et
c'est exploitable comme tel.**

---

**p.342 — paragraphes 7 et 8 (lignes ~67 à 104)**

| Repère marginal (verbatim) | Portée |
| --- | --- |
| **اثبات توافق قوانين الطبيعة مع قوانين العقل :** | titre de la séquence |
| **– حجّة 1 : على التوافق : الإنسان الأكثر قوّة في حالة الطبيعة هو الذي يحيا بمقتضى العقل.** | ¶7 |
| **– حجّة 2 : منطق الوعد والوعيد بما هو منطق شرائع المدينة ذاته منطق العقل.** | ¶8 |

⚠️ **اثبات** est imprimé **sans hamza** (pour **إثبات**) — coquille de la source.

⇒ **Les حجج sont NUMÉROTÉES par le manuel** (1, 2, puis 3 à la p.343). C'est le seul texte long du
chapitre à recevoir une **numérotation d'arguments** dans la marge : **3 arguments**, tous au
service d'une seule et même conclusion — **قوانين الطبيعة ⇔ قوانين العقل**.

- **¶7 / حجّة 1** — l'homme **le plus puissant et le plus indépendant** à l'état de nature est celui
  qui **vit selon la raison** ; il en va de même de la cité : elle possède puissance et
  indépendance **بقدر ما تتأسس على مبدأ العقل**. La fin la plus haute de la cité est celle que
  **العقل السليم** recommande comme **ما يفيد الناس جميعا**.
- **¶8 / حجّة 2** — les sujets se soumettent **إمّا خوفا … أو حبّا** ; d'où : **les actes que ni
  promesse ni menace ne peuvent obtenir ne relèvent pas des lois de la cité**. Exemples imprimés :
  nul ne peut renoncer à sa **ملكة التمييز والحكم** ; aucune promesse ni menace ne fera croire que
  **الكلّ ليس أعظم من الجزء** ou que **الله غير موجود** ; ni témoigner contre soi, se torturer, tuer
  son père ou sa mère, ou ne pas fuir la mort. ⇒ Prescrire l'impossible, c'est **هذيان** : ce ne
  serait « pas moins vain que de dire qu'un homme a le droit d'être fou et de délirer ».

⇒ **La distinction la plus fine du ¶8** : entre ce que la cité **peut** commander et ce qu'elle
peut seulement **prétendre** commander. La limite n'est pas morale, elle est **de puissance** — et
c'est exactement pourquoi elle est *de droit*, puisque droit et puissance coïncident.

---

**p.343 — paragraphes 9 à 11 (lignes 105 à ~141)**

| Repère marginal (verbatim) | Portée |
| --- | --- |
| **استنتاج : ضرورة استخدام القوّة لردع من يعترض على منطق العقل** | ¶9 (⚠️ imprimé **sans point final**) |
| **– حجّة 3 : شرعيّة الدولة مشروطة باحترام حقّ الجمهور.** | ¶9 |
| **إعلان عن مشكل علاقة الدولة بالدين** (en gras) | ¶10 |
| **طاعة الدولة لا تفضي إلى القضاء على الدين مادامت تستخدم العقل.** | ¶10 |
| **– الدين شأن شخصي.** | ¶10 fin |

- **¶9 / حجّة 3** — les mesures qui provoquent **اغتياظ الجمهور** ne relèvent **pas** du droit de la
  cité : puisque son droit **يتحدّد بقوّة الجمهور**, sa puissance **et** son droit **يضعفان بقدر
  استثارتها للناس ضدّها**. ⇒ **La révolte n'est pas seulement un danger : elle est une diminution du
  DROIT.** C'est la conséquence la plus forte de l'équation droit = puissance.
- ⚠️ **Le texte affirme aussi que la cité craint** : « **إنّ المدينة تخشى بعض المخاطر** », et elle
  est **d'autant moins indépendante que ses motifs de crainte sont plus forts** — exactement comme
  un individu à l'état de nature.
- **¶10 — la question religieuse.** Objection : la vie civile n'abolit-elle pas le culte ?
  Réfutation : **النّفس، من حيث إنّها تستخدم العقل، لا تخضع للسلطة الحاكمة، بل هي مستقلّة** ; ni la
  connaissance ni l'amour de Dieu ne peuvent être soumis à une autorité. La vraie **البرّ والإحسان**
  se manifeste dans **السعي للمحافظة على السّلم وتحقيق الوئام**. Les **الشعائر الدينية** ne servent
  ni ne nuisent à la vraie connaissance de Dieu ⇒ il ne faut pas leur donner une importance qui en
  ferait une cause de **الإخلال بالسلم والأمن العام**. Conclusion imprimée : chacun peut adorer son
  Dieu et travailler à son salut **كفرد** ; mais **نشر الدين** relève **de Dieu ou de l'autorité
  souveraine**.

⚠️ **Ce ¶10 est le point de contact direct avec la تحديدة « اللائكيّة » (p.322-323)** : le texte de
Spinoza dit *littéralement* ce que la نافذة دعائم définissait — la conviction religieuse comme
**مسألة خاصة**, et l'unité du peuple fondée sur ce qui est commun. ⇒ La boucle p.323 ↔ p.343 est
imprimée, et c'est le seul endroit du chapitre où une تحديدة est illustrée par un texte long.

- **¶11** — transition explicite : après le droit de l'autorité souveraine **sur les citoyens**,
  reste à examiner son droit **envers les autres puissances**. ⇒ **C'est la charnière du texte.**

---

**p.344 — paragraphes 12 à 14 (lignes ~142 à 180)**

| Repère marginal (verbatim) | Portée |
| --- | --- |
| **الإعلان عن المبحث الثاني : حقّ الدولة تجاه الدول الأخرى.** (en gras) | ¶11-12 |
| **– استخدام أسلوب المقارنة لتحديد أوجه التماثل والاختلاف بين علاقات الأفراد في « حالة الطبيعة » وعلاقات الدول.** | ¶12 — repère **de méthode** |
| **تعيين حقوق الدّولة :** — **– حقّ الاستقلاليّة.** — **– حقّ مقاومة الاضطهاد.** | ¶12 |
| **تأكيد التناسب بين الحق والقوّة** | ¶13 (⚠️ **sans point final**) |
| **– حقّ الحرب وحقّ السلم** | ¶13 (⚠️ **sans point final**) |

⇒ **La structure du texte est donc explicitement BIPARTITE**, et le manuel l'imprime deux fois :
**المبحث الأوّل = حقّ الدولة على المواطنين** (p.340, ¶1-10) · **المبحث الثاني = حقّ الدولة تجاه
الدول الأخرى** (p.344-345, ¶11-18). C'est **le plan du texte**, donné par la marge — la réponse la
plus sûre à toute question sur « le mouvement du texte ».

⇒ **L'analogie qui commande toute la seconde partie** (repère `أسلوب المقارنة`) : le rapport
**cité ↔ cité** est **comme** le rapport **individu ↔ individu à l'état de nature**. ⚠️ Mais le
texte imprime aussitôt **la limite de l'analogie** — l'écart, pas seulement la ressemblance :
la cité **تبقى قادرة على التصدّي لاضطهاد مدينة أخرى**, alors que l'individu à l'état de nature en
est **incapable** : il est vaincu chaque jour par **النوم**, épuisé par **المرض أو الكرب**, et
finit par céder à **هرم الشيخوخة**. ⇒ **Une comparaison à deux versants** — la question qui ne
retiendrait que la ressemblance manquerait la moitié du repère, qui dit bien
**أوجه التماثل *والاختلاف***.

- **¶12 — les deux droits de l'État, nommés par la marge** : **حقّ الاستقلاليّة** (la cité est
  indépendante quand elle **peut se conserver** et **résister à l'oppression**) et **حقّ مقاومة
  الاضطهاد**. Une cité est **تابعة** dès qu'elle vit dans **الخوف من جبروت** d'une autre, ou qu'elle
  ne peut agir **بمحض إرادتها**, ou qu'elle **a besoin de l'aide** d'une autre pour se conserver.
  ⇒ Corollaire imprimé : deux cités solidaires ont **ensemble** plus de puissance — **et donc plus
  de droit** — que chacune séparément.
- **¶13 — الدّول أعداء بالطبع.** Ceux qui restent au droit de nature et n'entrent pas dans
  **نطاق التمدّن** demeurent **في حالة عداوة**. D'où l'asymétrie décisive :

  | | Ce qu'il faut pour l'exercer |
  | --- | --- |
  | **حقّ الحرب** | **une seule** cité — « **حقّ تملكه كلّ مدينة بصورة فردية** » |
  | **حقّ السّلم** | **deux** cités au moins — « **متوقّفا على رغبة مدينتين اثنتين على الأقل** » |

  ⇒ **C'est la distinction la plus testable de la seconde partie** : la guerre est un droit
  *unilatéral*, la paix un droit *conditionnel*. Une question qui les met sur le même plan est
  fausse.
- **¶14 — la durée de l'alliance.** Elle dure **autant que durent les circonstances qui l'ont fait
  naître** — c'est-à-dire **الخوف** d'un dommage ou **الأمل** d'un avantage. Dès que l'une des deux
  cités **se libère de sa crainte** ou **perd son espoir**, elle redevient libre : chaque cité a
  **الحقّ المطلق كي تنقض التحالف متى شاءت**, et **on ne peut l'accuser de perfidie** — parce que
  **الوضع واحد بالنسبة إلى كلتي المدينتين**, et que **nul ne s'engage pour l'avenir qu'au vu des
  circonstances présentes**.

---

**p.345 — paragraphes 15 à 18 (lignes ~181 à 213) · fin du texte**

| Repère marginal (verbatim) | Portée |
| --- | --- |
| **شروط صلاحيّة التحالفات و حقّ نقضها.** | ¶14-15 |
| **– حقّ المدن في الالتزام المتبادل بقوانين السلم المتّفق عليها.** | ¶15 |
| **البقاء على العهد من جهة الحقّ مبدأ جامع بين الدين والعقل، ومن جهة الواقع متروك لحساب الظرف.** | ¶17 |
| **التأكيد على منزلة مفهوم الطبيعة الإنسانيّة كأساس للتفكير السياسي.** | ¶18 |

- **¶15** — les cités qui ont conclu la paix ont le droit de **trancher les différends** relatifs à
  ses conditions ; **قوانين السّلم ليست خاصّة بإحدى هذه المدن، بل هي شاملة لجميع المدن المتحالفة** ;
  faute d'accord, elles **retournent à l'état de guerre**.
- **¶16 — la loi de proportion inverse, imprimée** : *plus le nombre de cités contractantes
  augmente*, **moins chacune est redoutable** (`قلّ جبروت كل منها على حدة`), **moins elle peut faire
  la guerre**, et **plus son obligation de respecter les clauses de la paix est grande** — donc
  **أقلّ استقلالية وأكثر خضوعا للإرادة العامة للمدن المتحالفة**.
  ⇒ **Formule à retenir : nombre d'alliés ↑ ⇒ puissance de chacun ↓ ⇒ obligation ↑ ⇒ indépendance ↓.**
- **¶17 — tenir parole.** Le respect du pacte est commandé **par la religion et par la saine
  raison** (`يأمر به الدين والعقل السّليم`) — **c'est le principe qui joint les deux**, comme le dit
  le repère. **Mais** : rien dans **الكتاب** n'ordonne de tenir *n'importe quelle* promesse. Exemple
  imprimé : si j'ai promis de garder secrètement un dépôt et que j'apprends qu'il est
  **حصيلة السّرقة**, je ne suis pas tenu ; mon conduite sera droite si je **rends le dépôt à son
  véritable propriétaire**. De même pour l'autorité souveraine : si la raison ou les circonstances
  montrent que l'engagement **يضرّ بسلامة المواطنين عموما**, **من واجبها أن تنقض عهدها**.
  Conclusion : **الكتاب لم يأمر إلاّ على وجه العموم بالبقاء على العهد وترك لكل شخص حريّة الحكم في
  الحالات الاستثنائية**.
  ⚠️ **Le mot الكتاب est imprimé EN GRAS trois fois** dans ce paragraphe (l.196, 203, 206) — seul
  mot du texte à recevoir un enrichissement typographique. Il désigne **l'Écriture**.
  ⇒ **Distinction imprimée : من جهة الحقّ (principe joignant religion et raison) ≠ من جهة الواقع
  (laissé au calcul de la circonstance).** C'est exactement ce que dit le repère marginal, et c'est
  la formule la plus dense de la page.
- **¶18 — la conclusion.** Tout ce qui précède a été établi **انطلاقا من الطبيعة الإنسانيّة
  الضروريّة**, à savoir **الجهد الكوني الذي يسعى بفضله كل البشر إلى حفظ كيانهم** — un effort
  **شائع يبذله الجميع، حكماء كانوا أو جهلاء**. D'où le dernier mot : que l'on tienne les hommes pour
  **يهتدون بالعقل** ou pour **ينقادون للأهواء**, **فالنتيجة واحدة، لأنّ البرهان كليٌّ**.

⇒ **La clef de voûte** : la démonstration ne repose **pas** sur une hypothèse optimiste sur
l'homme. Elle vaut **quelle que soit** l'image qu'on s'en fait — c'est ce que veut dire
**البرهان كليّ**. Une question qui prête à Spinoza une anthropologie « optimiste » manque le
paragraphe final.

---

###### Questions d'accompagnement : il n'y en a AUCUNE

⛔ **La نافذة نصّ مطوّل ne comporte aucun questionnaire imprimé.** Le texte s'arrête à la ligne
~213 (¶18) et **la moitié basse de la p.345 est blanche** : pas de « أسئلة », pas de « مهام »,
pas de « تمشّيات », rien.

⇒ C'est **le même écart de gabarit que sur le مبحث 2** (نصّ مطوّل de بوبير, également sans
questionnaire) : ce n'est donc **pas un accident local**, mais **la règle du manuel pour cette
نافذة**. Vérifié ici sans le présupposer. ⇒ **Il n'y a pas de « questions du manuel » à reprendre
pour Spinoza** — le seul appareil de travail imprimé est **la bande de repères marginaux**.

---

###### Synthèse du plan officiel du texte (à partir de la seule marge)

**Le texte compte 18 paragraphes numérotés et 213 lignes numérotées.** Découpage des pages
(déduit des repères de 5 en 5, vérifié aux quatre charnières) :
**p.340 = l.1-28** · **p.341 = l.29-66** · **p.342 = l.67-104** · **p.343 = l.105-142** ·
**p.344 = l.143-180** · **p.345 = l.181-213**.

| Partie | Repère qui l'ouvre | ¶ | Lignes |
| --- | --- | :-: | --- |
| Préambule — définitions et annonce | **تحديد مفهومي** | 1 | 1-10 |
| **المبحث الأوّل — حقّ الدولة على المواطنين** | **الإعلان عن المبحث الأوّل** | 2-10 | 11-141 |
| … la thèse (droit = puissance de la multitude) | **تحديد طبيعة حقّ الدولة وأساسه : قوّة الجمهور** · puis **تناسب الحق والقوة** | 2 | 11-18 |
| … la société civile ne se règle pas sur les passions | **المجتمع المدني لا يحتكم إلى سلطة الأهواء** · **مخاطر سلطة الأهواء** | 3 | 19-39 |
| … le pacte ne fait pas renoncer au naturel | **نشأة الدولة لا تستوجب التنازل عن الطبيعي بل شرط حفظه** | 3 fin | ~30-39 |
| … absurdité de l'interprétation privée des lois | *(pas de repère propre)* | 4 | 40-44 |
| … le statut du citoyen | **تحديد منزلة المواطن في المدينة** · **اعتماد منهج فرضي استنتاجي** | 5 | 45-52 |
| … réfutation : obéir n'est pas perdre sa liberté | **الأسلوب السجالي** · **أسلوب الدحض** · **طاعة القانون لا تتعارض مع الحريّة** | 6 | 53-73 |
| … preuve de l'accord nature / raison | **اثبات توافق قوانين الطبيعة مع قوانين العقل** → **حجّة 1** | 7 | 74-81 |
| … la limite de ce que la cité peut commander | **حجّة 2** | 8 | 82-106 |
| … la limite du droit de l'État | **استنتاج** + **حجّة 3** | 9 | 107-116 |
| … le cas de la religion | **إعلان عن مشكل علاقة الدولة بالدين** · **طاعة الدولة لا تفضي…** · **الدين شأن شخصي** | 10 | 117-141 |
| **المبحث الثاني — حقّ الدولة تجاه الدول الأخرى** | **الإعلان عن المبحث الثاني** (+ **أسلوب المقارنة**) | 11-18 | 142-213 |
| … charnière | *(annonce)* | 11 | 142-151 |
| … droits de la cité | **تعيين حقوق الدّولة** (استقلاليّة · مقاومة الاضطهاد) | 12 | 152-158 |
| … guerre et paix | **تأكيد التناسب بين الحق والقوّة** · **حقّ الحرب وحقّ السلم** | 13 | 159-168 |
| … durée de l'alliance et droit de la rompre | **شروط صلاحيّة التحالفات و حقّ نقضها** | 14 | 169-185 |
| … lois de paix communes aux alliés | **حقّ المدن في الالتزام المتبادل بقوانين السلم** | 15-16 | 186-194 |
| … tenir parole | **البقاء على العهد من جهة الحقّ … ومن جهة الواقع…** | 17 | 195-206 |
| **Conclusion** | **التأكيد على منزلة مفهوم الطبيعة الإنسانيّة كأساس للتفكير السياسي** | 18 | 207-213 |

⚠️ Les bornes de paragraphe sont **exactes** (relevées sur le numéro rose) ; les regroupements de
repères dans une même ligne du tableau sont **de la fiche** — dans la source, chaque repère a sa
propre flèche vers une ligne précise.

⚠️ **Coquille systématique du rendu de la source, valable sur TOUTES les pages du texte** : un
**point parasite précède les mots amorcés par la préposition بـ** — `شخص .بمفرده` (p.339, p.340
l.12), `يفعل شيئا أو يملك شيئا .بموجب الحق المدني` (p.340), `على القيام .بما يعلم` (p.341),
`يحيا .بمقتضى العقل` (p.342, marge), `.بما هو منطق شرائع المدينة` (p.342, marge),
`فتُقالان .بموجب ذلك` (p.344), `عادت هذه المدن .بموجب ذلك` (p.345). Ce n'est **pas** une
ponctuation : c'est un **artefact de rendu**, à ignorer partout et à ne jamais reproduire.

---

##### 3.1.6 مختصرات — p.346

> **Page lue** : p.346 (intégral, chaque encadré recadré ×2,6 à ×3).
> ⚠️ **C'est le récapitulatif officiel du chapitre** — la matière la plus directement testable de
> toute la tranche. Transcrit **verbatim, encadré par encadré, dans l'ordre imprimé**.

**Mise en page.** Titre **مختصرات** en calligraphie, dans un cartouche blanc posé sur des carrés
vert / rouge / noir (haut de page, à droite). En haut à gauche, une photo encadrée de rouge :
**une plume d'oie noire posée sur des documents anciens** (feuillets manuscrits et imprimés aux
tons dorés) — sans légende. Le tout est enfermé dans **un grand cadre jaune arrondi** qui contient
**7 encadrés blancs à filet noir**, empilés verticalement.

⚠️ **Les encadrés ne sont NI numérotés NI titrés.** Aucun intertitre, aucune puce : sept blocs
successifs, séparés par le seul filet. La numérotation ci-dessous est **de la fiche**, pas du
manuel — elle sert à les citer, elle n'est pas imprimée.

⚠️ **Régime d'énonciation** : tous les encadrés sont écrits **à la première personne du bilan**,
avec trois verbes qui reviennent — **تبيّن لي / تبيّنت** · **أدركت** · **تحقّقت**. Ce n'est pas un
résumé de leçon, c'est **le relevé de ce que l'élève est censé avoir acquis**. C'est aussi ce qui
en fait un excellent gisement de questions : chaque encadré est déjà formulé comme un **acquis
vérifiable**.

---

**■ Encadré 1 — الوجود السياسي et السلطة (verbatim)**

> تبين لي أن **صورة الإنسان لا يمكن أن تكتمل ما لم أستحضر وجوده السياسي**. وأدركت أن **السلطة** هي
> **البنية الأساسية للسياسي**، سواء فهمت السلطة **على معنى القوة** أو **على معنى ما يطلق على وضع
> استراتيجي معين في مجتمع معين**.

Termes en gras dans la source : **وجوده السياسي** · **السلطة**.
⇒ **Deux acquis distincts** : *(a)* l'image de l'homme est **incomplète** sans son existence
politique ; *(b)* **السلطة est la structure de base du politique**, et elle se comprend **de deux
façons** — comme **قوة**, ou comme **وضع استراتيجي** dans une société donnée.
⇒ **La bifurcation قوة / وضع استراتيجي est la distinction la plus testable de l'encadré** — et elle
renvoie à فوكو (p.325 : le pouvoir défini comme **إستراتيجيا**).

---

**■ Encadré 2 — سلطة الدولة, un débat sans fin (verbatim)**

> تبينت أن الحديث عن **سلطة الدولة** **مثير لجدل لا ينتهي**، إذ أدركت **وجهات نظر مختلفة في شأن
> الحاجة إليها، أو في شأن وعودها وحقيقتها**، وهو جدل يدعونا إلى **مزيد تقليب النظر في أساسها وآلية
> فعلها وغاياتها** علنا نظفر بما يسمح لنا **بتقييمها وبيان قيمتها**.

Termes en gras : **سلطة الدولة** · **أساسها وآلية فعلها**.
⇒ **Les 3 axes d'examen que l'encadré ferme** : **الأساس** · **آلية الفعل** · **الغايات** — et
la finalité de cet examen est double : **التقييم** et **بيان القيمة**.
⇒ Les objets de désaccord recensés sont eux aussi au nombre de trois : **الحاجة إليها** ·
**وعودها** · **حقيقتها**.

---

**■ Encadré 3 — la tâche de l'État, c'est le الحق (verbatim)**

> أدركت أن **كل خطاب يتعلّق بالدولة لا يمكن أن يهمل فكرة الحق**، إذ تبين لي أن **مهمة الدولة
> والدور الموكول لها إنما هو تأمين الحق** سواء عدّ هذا الحق **طبيعيا**، أو **مدنيا** أي سواء اعتبر
> الحق حقا **بالنظر إلى طبيعة الإنسان**، أو **بالنظر إلى منزلته المدنية التي يرتضيها لنفسه بما هو
> مواطن**.

Termes en gras : **الحق** · **طبيعيا** · **مدنيا** · **مواطن**.
⇒ **La distinction الحق الطبيعي / الحق المدني est reprise ici telle que la posait le
الجهاز المفهومي de la ليبيرالية (p.328)** — mais avec **le critère explicite de la différence** :
- **طبيعي** = considéré **بالنظر إلى طبيعة الإنسان** ;
- **مدني** = considéré **بالنظر إلى منزلته المدنية التي يرتضيها لنفسه بما هو مواطن**.
⇒ **C'est la formulation la plus nette du chapitre** sur ce couple, parce qu'elle nomme le
**point de vue** qui les sépare, et non seulement leur contenu. Le mot **يرتضيها** est décisif :
le droit civil suppose **un consentement**.

---

**■ Encadré 4 — دولة الحق, démocratie et ses limites (verbatim)**

> أدركت أن **دولة الحق لا يمكن أن تنشأ على القوة**، كما تبينت أن **دولة الحق لا يمكن أن تكون على
> صورة نظام استبدادي**، وهو ما مكنني من **إدراك قيمة الديمقراطية بماهي نظام حكم سياسي**، مثلما
> مكنني من **بيان حدود مثل هذا النظام إذا ما اتخذ من منطق الأغلبية ذريعة لممارسة الهيمنة على
> الأقليات أو الأفراد** ، وأدركت أن **مشروعية سياسة ما تكمن في قبولها للتعددية بما هي خير وسيلة
> لحماية استقلال كل طرف** .

Terme en gras : **الديمقراطية**. ⚠️ La source imprime **espace avant les deux virgules finales**
et **avant le point final** — coquilles de composition.
⇒ **L'encadré le plus dense de la page, et le plus contre-intuitif** : il valorise la démocratie
**et** en marque la limite dans la même phrase. La limite est nommée précisément :
**quand la logique de la majorité (منطق الأغلبية) devient un prétexte (ذريعة) à la domination sur
les minorités ou les individus.**
⇒ **Le critère final de légitimité qu'il pose n'est PAS la majorité, c'est التعدديّة** :
« مشروعية سياسة ما تكمن في **قبولها للتعددية** بما هي **خير وسيلة لحماية استقلال كل طرف** ».
⚠️ Une question qui ferait de la règle majoritaire le critère de légitimité **contredit cet
encadré**. C'est le piège le plus rentable de la page.
⇒ Deux exclusions posées d'entrée, à ne pas confondre : **دولة الحق ≠ née de la force** et
**دولة الحق ≠ régime despotique**.

---

**■ Encadré 5 — la critique doit atteindre jusqu'à l'image de l'homme (verbatim)**

> تبينت أن **الإنسان في حاجة إلى فعل نقد لا ينصب على الواقع السياسي فحسب بل يطال الحق**، ويمتد
> **إلى صورة الإنسان ذاتها** تلك التي **يتغنى بها خطاب الحق وإعلانات حقوق الإنسان**، إذ أدركت أن
> **إنسان حقوق الإنسان قد لا يعني سوى الإنسان الأناني لا الإنسان بما هو مواطن**.

Termes en gras : **حقوق الإنسان** · **مواطن**. ⚠️ La source imprime un **double espace** entre
« ذاتها » et « تلك ».
⇒ **Les 3 degrés de la critique, en gradation imprimée** : **الواقع السياسي** → **الحق** →
**صورة الإنسان ذاتها**. C'est une **échelle**, donc un excellent matériau de remise en ordre.
⇒ **La thèse la plus tranchée de la page** — et elle est marxienne d'inspiration (cf. la citation
de ماركس, p.323) : **إنسان حقوق الإنسان** risque de n'être que **الإنسان الأناني**, non
**الإنسان بما هو مواطن**.
⚠️ Le manuel écrit **قد لا يعني** (« il se peut qu'il ne signifie que… ») — **une modalisation, pas
une affirmation**. Une question qui la durcirait en « les droits de l'homme *sont* l'homme
égoïste » trahirait la source.

---

**■ Encadré 6 — الطاعة contre العدل, et l'équivoque de la justice (verbatim)**

> أدركت أن **علاقة المواطن بالدولة تقوم على واجب الطاعة مقابل تأمينها العدل**، وتبينت ما يثيره
> **الخضوع لنظام جائر** من إشكال، **نظرا للطابع الملتبس للعدل**، إذ بين **العدل** و**المساواة**
> و**الإنصاف** **علاقة تتراوح بين الوصل والفصل**، وتحققت بأن **الإنصاف، وإن كان مرغوبا فيه، فإنه قد
> لا يكون قانونيا**، وأن **العدل قد يشرع للاّمساواة قانونا وللقوة سلطانا** مادام **القانون يعترف
> بالقوي العادل، أكثر من اعترافه بالعادل القوي**.

Termes en gras : **الطاعة** · **العدل** · **المساواة** · **الإنصاف**.
⇒ **L'équation de base du rapport politique, telle que l'encadré la pose** :
**واجب الطاعة ↔ تأمين العدل** — un **échange**, pas une soumission. D'où le problème nommé :
**الخضوع لنظام جائر** (un régime qui n'assure pas sa part).
⇒ **Le triangle العدل / المساواة / الإنصاف** — et la formule exacte du rapport :
**« علاقة تتراوح بين الوصل والفصل »** (ils tantôt se rejoignent, tantôt se séparent). ⚠️ Ni
identité, ni opposition : **une relation variable**. C'est la nuance que toute question doit
respecter.
⇒ **Deux thèses fortes, à retenir mot pour mot** :
1. **الإنصاف قد لا يكون قانونيا** — l'équité peut être désirable **sans être légale**.
2. **العدل قد يشرع للاّمساواة قانونا وللقوة سلطانا** — la justice peut **légaliser l'inégalité** et
   **donner pouvoir à la force**.
⇒ **Le chiasme final est la phrase la plus fine du chapitre entier** :
**« القانون يعترف بالقوي العادل، أكثر من اعترافه بالعادل القوي »** —
la loi reconnaît **le puissant qui est juste** plus que **le juste qui est puissant**.
⚠️ Les deux syntagmes sont composés **des mêmes deux mots dans l'ordre inverse** : c'est
exactement ce qui les rend discriminants — et exactement ce qui les rend faciles à inverser par
erreur. Toute question portant là-dessus doit citer l'ordre imprimé.

---

**■ Encadré 7 — المواطنة, locale et universelle (verbatim)**

> تبينت أنّ **المواطنة هي القيمة التي تحدد منزلة الإنسان السياسية**، وأدركت أنّ **منزلة الإنسان
> بصفته مواطنا محليا لا تنفي أن يكون مواطنا عالميا** وأدركت أن **المواطن العالمي لا يحمل على معنى
> انتمائه إلى جماعة عالمية، إلى إنسانية بلا جنسية**، بل **يحمل على معنى الإنسان الذي يمارس حقوقه من
> جهة كونه كائنا كونيا وليس من جهة كونه كائنا قوميا فقط**.

Termes en gras : **المواطنة** · **مواطنا محليا** · **مواطنا عالميا** · **المواطن العالمي** ·
**كائنا كونيا** · **كائنا قوميا**.
⇒ **La définition officielle de la citoyenneté**, en une ligne :
**المواطنة = القيمة التي تحدد منزلة الإنسان السياسية.**
⇒ **La thèse de compatibilité** : **مواطن محلي et مواطن عالمي ne s'excluent pas** — le second
**ne nie pas** le premier.
⇒ **La correction du contresens, imprimée noir sur blanc** — et c'est le point le plus testable de
l'encadré :

| Ce que le **مواطن عالمي** n'est **PAS** | Ce qu'il **EST** |
| --- | --- |
| **الانتماء إلى جماعة عالمية** | l'homme qui **exerce ses droits** |
| **إنسانية بلا جنسية** | **من جهة كونه كائنا كونيا**, et non **من جهة كونه كائنا قوميا فقط** |

⚠️ **La citoyenneté mondiale n'est donc pas une appartenance mais un POINT DE VUE sur l'exercice
des droits.** Une question qui en ferait une communauté supranationale, ou une apatridie, tombe
exactement dans ce que l'encadré réfute.
⚠️ Noter le **فقط** final : le manuel ne nie pas l'être national, il refuse qu'il soit **le seul**
point de vue.

---

###### Ce que les 7 مختصرات posent, en un tableau

| # | Le nœud de l'encadré | La distinction / formule à retenir |
| :-: | --- | --- |
| 1 | l'homme est incomplet sans son **وجود سياسي** ; **السلطة** = structure de base du politique | **السلطة كقوة** ≠ **السلطة كوضع استراتيجي** |
| 2 | **سلطة الدولة** = objet d'un **جدل لا ينتهي** | à examiner sous 3 angles : **الأساس / آلية الفعل / الغايات** |
| 3 | la tâche de l'État = **تأمين الحق** | **الحق الطبيعي** (طبيعة الإنسان) ≠ **الحق المدني** (المنزلة المدنية المُرتضاة) |
| 4 | **دولة الحق** ≠ force, ≠ despotisme ; valeur **et** limites de la **ديمقراطية** | légitimité = **قبول التعددية**, pas **منطق الأغلبية** |
| 5 | la critique doit atteindre **صورة الإنسان** elle-même | **إنسان حقوق الإنسان** risque d'être **الإنسان الأناني**, non **المواطن** |
| 6 | **الطاعة ↔ العدل** ; caractère **ملتبس** de la justice | **الإنصاف قد لا يكون قانونيا** · **القوي العادل** ≠ **العادل القوي** |
| 7 | **المواطنة** = la valeur qui fixe la place politique de l'homme | **مواطن محلي** compatible avec **مواطن عالمي** ; **كائن كوني** ≠ **كائن قومي فقط** |

⚠️ **Ce que les مختصرات NE reprennent PAS** — et c'est aussi net que ce qu'elles reprennent :
- **rien** sur **اللائكيّة** (تحديدة p.322-323) ;
- **rien** sur **الكليانية** (تحديدة p.324-326) ni sur **الفوضويّة** (p.330-331) ;
- **rien** sur **فلسفة العقد الاجتماعي** ni sur les 4 philosophes du tableau p.334 ;
- **rien** sur **سبينوزا** ni sur le نصّ مطوّل.

En revanche elles introduisent **des couples que la نافذة دعائم n'avait pas traités** :
**العدل / المساواة / الإنصاف**, **الطاعة**, **الديمقراطية / التعدديّة**, **حقوق الإنسان**,
**المواطنة المحليّة / العالميّة**. ⇒ **Les مختصرات ne résument pas les نوافذ : elles bouclent
le مبحث entier**, cours compris. Une fiche qui ne lirait que les نوافذ manquerait la moitié de ce
que ce récapitulatif tient pour acquis.

---

###### Écarts et coquilles relevés sur la tranche p.335-346

| p. | Ce qui est imprimé | Lecture / remarque |
| --- | --- | --- |
| 335 | titre **« كيفيات التفكير »** sans le mot **نافذة** | alors que la p.339 imprime bien **« نافذة / نصّ مطوّل »** |
| 336 | **« ما هيّ الإحراجات »** | شدّة parasite sur le ي — lire **ما هي** |
| 337 | **هوبس** (référence) / **هوبز** (مهام), sur la même page | retenir **هوبس** (graphie du reste du chapitre) |
| 337 | dernière ligne du توضيح 3 (**بيان استتباعاتها الخارقة**) sans point final | non coupée : vérifié |
| 338 | 3 modes d'objection (**ضمنية / استتباع / تناقض مع الواقع**) ≠ les 4 du توضيح 3 | **deux listes distinctes**, à ne pas fusionner |
| 339 | couverture **« كتاب السياسة »** / légende **« رسالة السياسة »** | titre de référence : **كتاب السّياسة** |
| 340 | **« ترجمة جلا ل الدّين سعيد »** | coupure parasite — lire **جلال الدّين سعيد** |
| 342 | **« اثبات »** (marge) | sans hamza — lire **إثبات** |
| 343-345 | plusieurs repères marginaux sans point final | **استنتاج…**, **تأكيد التناسب…**, **حقّ الحرب وحقّ السلم** |
| 340-345 | **point parasite devant les mots en بـ** (`.بمفرده`, `.بمقتضى`, `.بموجب`, `.بما`) | artefact de rendu, systématique, **jamais** à reproduire |
| 346 | espaces avant virgule / point dans l'encadré 4 ; double espace dans l'encadré 5 | composition |
| 335-338 | la نافذة كيفيات التفكير **n'a ni لمزيد التعمّق ni sitographie** | contrairement à la نافذة دعائم |
| 345 | **aucune question d'accompagnement** après le نصّ مطوّل | conforme au مبحث 2 — vérifié, non présupposé |
| 346 | les 7 encadrés des مختصرات **ne sont ni numérotés ni titrés** | la numérotation de cette fiche est ajoutée |

---

###### Fin du مبحث 3.1

La p.346 **clôt le chapitre**. La p.347 ouvre le مبحث suivant
(**الأخلاق : الخير والسّعادة**) avec sa page-titre et sa citation d'ouverture — hors périmètre de
cette tranche.

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

#### مبحث 3.2 — الأخلاق : الخير والسّعادة — transcription p.347-381

> **Portée de ce fragment** : pages imprimées **347 → 381**, intégral — page d'ouverture du مبحث,
> `3.2.1` نافذة مدخل إلى التفكير في المسألة (p.348-351) et `3.2.2` نافذة سندات للتفكير في المسألة
> (p.352-381), soit les **18 سندات** annoncés par le فهرس.
> **Source** : manuel élève `210402` (كتاب الفلسفة — السّنة الرّابعة من التّعليم الثانوي —
> الشّعب العلميّة, CNP), pages rendues en image ; le PDF n'a **pas** de couche texte exploitable
> (encodage de police hérité, glyphes non-Unicode) — tout ce qui suit est de la lecture d'image.
> **Numérotation** : page PDF = page imprimée (vérifié sur p.347, p.348…).
> ⚠️ Ce fragment est une **transcription**, pas une fiche relue : il n'a pas passé sa R-7.
> Un point qui paraît étrange est **signalé**, jamais « corrigé » par déduction.

---

##### Cadre : où ce مبحث se situe dans le manuel

Le bandeau de محور imprimé en haut de la page d'ouverture est **القيم بين النسبي والمطلق** ;
le مبحث y porte le chiffre **2** dans le carré bleu. La désignation « **3.2** » du فهرس se lit donc
« مبحث 2 du محور 3 », et non un titre imprimé sur la page.

⚠️ **Variante de graphie sur le titre lui-même** : la page d'ouverture (p.347) imprime
**« الأخلاق : الخير والسعادة »** — **sans شدّة** sur `السعادة` (vérifié par agrandissement).
Le فهرس écrit `السّعادة`. Les deux formes coexistent dans le manuel ; retenir une graphie et s'y
tenir dans tout le chapitre.

⚠️ Le titre de la seconde نافذة est imprimé **« نافذة سندات / للتفكير في المسألة »** — avec
`للتفكير` (lâm), pas `التفكير` (vérifié par agrandissement p.352).

---

##### Page d'ouverture du مبحث — p.347

- **Bandeau de محور** (en haut, sur fond crème) : **القيم بين النسبي والمطلق**.
- **Titre du مبحث**, dans un ovale vert, précédé du carré bleu **2** :
  **الأخلاق : الخير والسعادة**.
- **Liste de notions** imprimée dans un cartouche bleu vertical sous le titre, dans cet ordre :

  | ordre | notion imprimée |
  | --- | --- |
  | 1 | الحرّية |
  | 2 | الرّفاه |
  | 3 | الفضيلة |
  | 4 | الواجب |
  | 5 | المنفعة |

  ⚠️ Ce cartouche est la seule « carte » du مبحث sur la page d'ouverture : **il n'y a pas
  d'organigramme** ici, contrairement au مبحث 2 (p.215) qui en portait deux. **Constaté, pas déduit.**

- **Illustration** : photographie — silhouette d'un homme bras levés au sommet d'une montagne,
  découpée en noir sur un soleil couchant (dégradé jaune / orange / rouge).

- **Encadré de citation** (cadre rouge, à droite — verbatim) :

  > « فينوس : ما نحن إلاّ سجناء هذه الذات وأنت الذي قالها قبلي يا أبولون.. ألا تذكر.. ألست أنت
  > القائل بجماليون استطاع ما لم نستطع، فسما على ذاته، وحطّم أسوارها — يوم أبدع — وهو الهالك —
  > ذلك الخلود! »
  > — ▲ **توفيق الحكيم، بجماليون**

---

##### `3.2.1` نافذة مدخل إلى التفكير في المسألة — p.348-351

###### Page de titre de la نافذة — p.348

Titre imprimé sur deux lignes séparées par un filet rouge : **مدخل إلى / التفكير في المسألة**.

Deux illustrations : (a) photographie d'un enfant en manifestation portant une pancarte
« **LAISSEZ NOUS RESPIRER** » (texte français, en rouge sur fond blanc) ; (b) photographie d'un
**mannequin articulé en bois** (mannequin de dessinateur) en position de marche, sur fond blanc.

**Encadré de citation** (cadre rouge — verbatim) :

> " قد يعمل بعض النّاس عمل العدول وليس بعادل، ويعمل عمل الشّجعان وليس بشجاع، ويعمل عمل الأعفّاء
> وليس بعفيف. "
> — ▲ **أحمد بن مسكويه، تهذيب الأخلاق**

⚠️ **Graphie** : ici **« أحمد بن مسكويه »**. Le سند 2 (p.354) porte une autre forme du même nom —
voir la fiche de ce سند.

###### وضعية استكشاف أولي — p.349

⚠️ **Tel qu'imprimé** : « **وضعية استكشاف أولي :** » — avec `أولي` (yâ' final), non `أولى`
(vérifié par agrandissement). Le carré rouge en tête porte le chiffre **1**.

- **Bandeau « أستحضر تمثلاتي… »** (encadré vert à droite, consigne à compléter par l'élève sur
  pointillés) — verbatim :
  > … وأقترح جوابا عن السؤال "متى يكون فعلي فعلا أخلاقيّا؟" :

- **Bandeau de consigne** : « أتابع التفكير : أقرأ النص قراءة متأنّية وأفكّر في مضمونه … »

- **Texte support** — **ابن حزم**, *طوق الحمامة في الألفة والألاّف*, دار البحار، بيروت 2000، ص 153.

  **Thèse (reformulée)** : beaucoup d'hommes obéissent à leur âme et désobéissent à leur raison,
  suivant leurs passions contre ce que la religion et la raison saine prescrivent ; c'est que Dieu
  a composé en l'homme **deux natures opposées** — l'une qui ne porte qu'au bien et au beau, dont
  le guide (`قائدها`) est **العدل** et l'organe **العقل** ; l'autre qui ne porte qu'aux appétits et
  ne mène qu'au mal, dont le guide est **الشهوة** et l'organe **النفس**.

- **Notice « الكاتب »** (encadré vert, verbatim resserré) :
  **أبو محمّد علي بن أحمد بن سعيد بن حزم الاندلسي** : ولد بقرطبة سنة 384 هـ/ 994 م وتوفي سنة
  456 هـ/ 1064 م. هو فقيه وأديب ومشارك في التأريخ والأنساب والنحو واللغة والشعر والطب والمنطق
  والفلسفة وغيرها. يعدّ كتابه " طوق الحمامة " من أشهر مؤلّفاته واشتمل على أحاديث طريفة في الحبّ
  ومعانيه وحالاته وأسبابه وأغراضه.

  ⚠️ Imprimé **« الاندلسي »** sans hamza (et non `الأندلسي`).

- **المهامّ** (encadré rose — **verbatim**, 8 puces) :
  - أرصد المفاهيم الواردة في النصّ وأحدّد المجال الذي تتحرّك فيه.
  - أبني جدولا بخانتين أصنّف فيه مختلف المفاهيم وأراعي في ذلك انسجام المفاهيم الواردة في كلّ خانة.
  - أبني أزواجا مفهوميّة متناقضة وأتساءل عن سبيل رفع التناقض القائم بينها.
  - أستخلص السؤال الذي يجيب عنه النصّ.
  - أيّ تصوّر للإنسان تقترحه مقاربة ابن حزم في جوابه عن السؤال؟
  - متى يكون الفعل أخلاقيّا حسب أطروحة الكاتب؟
  - أقارن جوابي الأوّل بما ذهب إليه ابن حزم وأتساءل عن المشكل الذي يمكن أن يترتّب على هذه المقارنة
  - هل من مبرّر للتفكير في الحياة الأخلاقيّة من جديد؟

###### وضعية استكشاف ثانية — p.350

⚠️ **Anomalie de numérotation constatée** : le carré rouge en tête de cette وضعية porte lui aussi
le chiffre **1**, exactement comme celui de la وضعية précédente (p.349) — alors que le titre dit
« ثانية ». **Constaté, non corrigé.**

- **Bandeau « أستحضر تمثلاتي… »** — verbatim :
  > … وأقترح جوابا عن السؤال " هل أحتاج إلى إعادة التفكير في القيم التي تتحكّم في سلوكي؟ "
  > أبرّر جوابي.

- **Bandeau de consigne** : « أتابع التفكير : أقرأ النص قراءة متأنّية وأفكّر في مضمونه … »

- **Texte support** — **روبار مسراهي**, *مقالة في السّعادة، ج 2 (الإيتيقا والسياسة والسّعادة)*.
  Ligne de référence latine imprimée sous la ligne arabe, **verbatim** :
  `Robert MISRAHI; Traité du bonheur, II, Ethique, politique et bonheur. Ed. Seuil, Paris 1983, p 35`

  **Thèse (reformulée)** : la réflexion sur les **fins** est aujourd'hui paralysée par un préjugé
  si banal et si enraciné dans la culture qu'il s'impose comme une évidence — préjugé qui ne porte
  pas sur telle valeur traditionnelle mais sur **la définition même de la morale et de sa
  fonction** : on croit d'ordinaire, en vertu de ce préjugé, que la fonction de la morale
  **reste la même** (`تظلّ هي هي`) à travers l'évolution des idéologies et des mœurs et
  l'évolution historique des valeurs et des idéaux, et qu'elle consiste à **énoncer ce qui
  s'impose** (`بيان ما يلزم`) sur le plan de l'acte, lui-même soumis à l'ordre des fins. Or la
  tâche de la morale consiste, en somme et de façon permanente, à **énoncer la pureté de l'acte
  et son authenticité**, en déterminant les **conditions internes** requises pour qu'il soit tenu
  pour pur et authentique. C'est par
  l'**authenticité de l'intention** (`أصالة القصد`) seule qu'un acte devient bon, digne d'estime, et
  **susceptible d'être universel** (`قابلا لأن يكون كونيّا`).

  ⚠️ **Ne pas intervertir les deux membres.** Ce que la page range du côté du **préjugé**
  (`الحكم المسبق`), c'est la **permanence** de la fonction de la morale à travers l'évolution des
  valeurs, et sa réduction à `بيان ما يلزم`. Le seul « permanent » que la page assume
  (`وبشكل دائم`) porte sur `بيان نقاء الفعل`. Une مهمّة comme
  `كيف أفهم التعارض بين تغيّر القيم وثبات وظيفة الأخلاق؟` devient insoluble si l'on retourne
  l'attribution.

- **Notice « الكاتب »** (encadré vert, verbatim) :
  **روبار ميسراهي** 1926 : فيلسوف فرنسي من أصل تركي، متحصل على شهادة التبريز ودرّس طيلة ثلاثين سنة
  في جامعة باريس الأولى، عرف بكتاباته المتصلة خاصّة بالأخلاق والسياسة.

  ⚠️ **Variante de graphie dans la même page** : la ligne de source imprime **« روبار مسراهي »**,
  la notice imprime **« روبار ميسراهي »**. Le فهرس annonce « مسراهي ». Le سند 18 (p.380) est du même
  auteur — voir sa fiche pour la graphie qui y est retenue.

- **المهامّ** (encadré rose — **verbatim**, 8 puces) :
  - ما معنى أن يكون التفكير في الغايات معطّلا اليوم؟ أحدّد سبب ذلك.
  - ما المقصود بالقيم التقليديّة؟ هل أعثر على مثيل لها في ثقافتي الرّاهنة؟
  - ما وظيفة الأخلاق؟
  - كيف أفهم التعارض بين تغيّر القيم وثبات وظيفة الأخلاق؟
  - ما المقصود بنقاء الفعل وأصالته؟
  - ما هو العنصر الأخلاقي القابل لأن يصير عنصرا كونيّا؟
  - أستحضر مكاسبي من الدروس السابقة وأفكّر في إمكانيّة التوفيق بين الخصوصيّة الثقافيّة وبين ما هو
    كوني في الأخلاق؟
  - أعيد التفكير في جوابي الأوّل في ضوء ما غنمته من المهام التي أنجزتها.

###### الأبعاد الإشكاليّة للمسألة — p.351

Le titre est encadré à gauche par un **carré rose portant « ؟ »** (pictogramme de la rubrique),
symétrique du carré rouge/rose de droite.

Page-outil entièrement à remplir par l'élève (cadres vides et pointillés). Elle est organisée en
**deux blocs numérotés**.

**Bloc 1** — une ligne de trois pastilles vertes, lue de droite à gauche :
**الخير** — **و** (pastille centrale, vert foncé) — **السعادة**, avec une flèche descendante partant
de la pastille centrale vers un bandeau gris de consignes (**verbatim**) :

- أركّز على أداة العطف وأستحضر العلاقات المنطقيّة التي تفترضها.
- أقيم هذه العلاقات بين " الخير " و " السعادة ".
- ماذا يترتّب على كلّ واحدة منها؟

Puis un cadre à 5 lignes numérotées 1→5, avec l'intitulé latéral (encadré vert) :
**أستخلص أهمّ الأسئلة التي يمكن أن توجّهني في التفكير في هذه العلاقات.**

**Bloc 2** — un organigramme à remplir. En tête, un cadre imprime la liste des cinq notions
(la même que la page d'ouverture, sur une seule ligne) :
**الحرّية – الرّفاه – الفضيلة – الواجب – المنفعة**

Sous ce cadre, deux consignes fléchées (**verbatim**) :
- ▲ أنتبه إلى هذه المعاني وأتثبّت فيها.
- ▼ أستحضر المعاني التي تناقضها.

Entre les deux consignes et les colonnes, un **champ blanc à une ligne pointillée** (à remplir)
reçoit les معاني contraires ; deux flèches en repartent vers les colonnes.

Puis deux colonnes de travail, chacune surmontée de sa consigne et suivie d'un cadre à 4 lignes :
- (à droite) **أصلها بالخير وأستخلص ما يترتّب من أسئلة أساسيّة :**
- (à gauche) **أصلها بالسعادة وأستخلص ما يترتب من أسئلة أساسيّة :**

En bas de page, un dernier cadre à 5 lignes, intitulé latéral (encadré vert) :
**أستخلص المشكلات الفلسفيّة وأبيّن الرهان من وراء التفكير فيها.**

⚠️ **Aucune problématique n'est imprimée en toutes lettres sur cette page** : le manuel fait
formuler les problèmes par l'élève. Il n'y a donc **pas** de « أبعاد إشكاليّة » verbatim à citer
pour ce مبحث, seulement la matrice ci-dessus. **Constaté.**

---

##### `3.2.2` نافذة سندات للتفكير في المسألة — p.352-381

###### Page de titre de la نافذة — p.352

Titre imprimé sur deux lignes séparées par un filet rouge : **نافذة سندات / للتفكير في المسألة**.

Deux illustrations : (a) photographie d'un lecteur seul à une table, au milieu d'une grande
bibliothèque aux rayonnages pleins ; (b) photographie très saturée (jaune/orange) d'une jeune femme
souriante entourée de sacs, vêtements et objets de consommation.

**Deux encadrés de citation** (cadres rouges — verbatim) :

> " ثمّة ما يدعو إلى التخوّف من أن ينكر زماننا هو أيضا الفيلسوف في حدّ ذاته وألاّ تكون الفلسفة مرّة
> أخرى إلاّ دخانا في هذا الزّمان. ذلك أنّ التفلسف بحث وهو يقتضي أن تكون ثمّة أشياء تُرى وتُقال ".
> — ▲ **موريس مرلوبونتي، تقريظ الحكمة**

> " إنّ مفاهيم " الجمال " و " العدالة " و " السعادة " العامة، غير القابلة للترجمة، تعكس في الحقيقة
> الضمير التعيس لعالم منقسم على نفسه، يتعالى فيه " ما هو كائن " على " ما يجب أن يكون "، بل
> " يرفضه وينبذه ". "
> — **هربارت ماركوز**

⚠️ Le second encadré est attribué à **هربارت ماركوز** **sans titre d'ouvrage** — contrairement à
tous les autres encadrés de citation du مبحث. **Constaté.**

###### Gabarit réellement observé sur les سندات de ce مبحث

Constaté page par page (pas déduit du مبحث 2) :

- En-tête : carré magenta portant le **numéro**, la mention **« السند : »**, et le **titre du سند**
  en gros caractères.
- **« التمهيد : »** — encadré rose pâle, systématique jusqu'ici, **verbatim** ci-dessous.
- Le texte de l'extrait, appels de note entre parenthèses `(1)`, `(2)`… quand il y a des notes.
- Ligne(s) de source : arabe, parfois **doublée d'une ligne latine** (auteur + titre français + éd.).
- **« الكاتب »** — bandeau magenta : soit une **notice** en encadré vert/blanc, soit un simple
  **renvoi** à un سند d'un autre مبحث (déjà 3 renvois sur les 4 premiers سندات).
- **Encadré de notes** : son titre **s'accorde en nombre** — **« الهامش »** quand il y a une note,
  **« الهامشان »** quand il y en a deux. Plusieurs سندات n'en ont **aucun**.
- **« المهام »** — bandeau magenta + liste à puces carrées, **verbatim** ci-dessous.
  ⚠️ Le bandeau est imprimé **« المهام »** (sans شدّة) dans la نافذة سندات, alors que la نافذة مدخل
  (p.349, p.350) imprime **« المهامّ »**. Variante constatée.
- Beaucoup de سندات se terminent par une **illustration + un encadré de citation** reprenant une
  phrase du texte, attribuée au **seul nom de famille** (« مسكويه », « سبينوزا », « ميل »…).

**La double page n'est pas systématique** : certains سندات tiennent sur une page (سند 1, p.353),
d'autres débordent sur la suivante (سند 2 : p.354-355 ; سند 3 : p.356-357 ; سند 4 : p.358-359).

---

###### سند 1 — أرسطو — « حدّ الفضيلة » — p.353

- **Auteur tel qu'imprimé** : **أرسطو** (ligne de source) ; ligne latine **`ARISTOTE`**.
- **Titre du سند** : **حدّ الفضيلة**
- **Source** : أرسطو؛ أخلاق نيقوماخوس، الكتاب 2. الفصل 1 —
  `ARISTOTE, Ethique de Nicomaque, livre II ch 1, éd. GF, 1965, pp 54-55.`
- **Illustration** : buste antique en marbre (vignette dans le texte).

**التمهيد (verbatim)** :
> فيبدو الإنسان كائنا تتقاذفه الميول والأهواء من جهة، و إرادة الترفع والتسامي من جهة أخرى، وتجعل
> من التوتر سمة وجوده، فبقدر ما يرفض الاستكانة إلى وضع لا يرتضيه، يعمل على أن يرتفع إلى منزلة
> يستحيل معها من إنسان بالقوة إلى إنسان بالفعل، سعي لا يبلغ أوجه ما لم يمتلك مفاتيح الفضيلة
> ومعيارها وآلية تحققها.

**Thèse (reformulée)** : la vertu est une **disposition acquise volontairement**, stable, consistant
à se tenir au **milieu** (`الوسط`) entre deux extrêmes — l'excès (`إفراط`) et le défaut (`تفريط`) —
milieu déterminé par la raison telle que la fixerait l'homme avisé ; ce milieu est un
**sommet quant au bien** (`الحدّ الأقصى` par rapport à la perfection). Mais **tout acte n'admet pas
de milieu** : certains actes (adultère, vol, meurtre, envie, impudence) et certains vices sont
mauvais **en eux-mêmes**, non par excès ou par défaut — il n'y a pas de « juste milieu » du meurtre,
comme il n'y a pas d'excès ni de défaut de tempérance ou de courage.

**هوامش** : **aucun encadré de notes sur cette page.**

**الكاتب** — ⚠️ **ce n'est pas une notice mais un RENVOI**, imprimé verbatim :
> **أرسطو** راجع التعريف بأرسطو في السند عدد 16 ( الدولة: السيادة والمواطنة )

(Renvoi hors de ce مبحث : vers le سند 16 du مبحث « الدولة : السيادة والمواطنة ». À résoudre depuis
la tranche correspondante.)

**المهام (verbatim, 4 puces)** :
- أي معنى للفضيلة يستبعده الكاتب؟ أستخلص تحديده الخاص للفضيلة.
- ماذا يعني تقدير الفضيلة عند أرسطو : هل يكشف عن أخلاق حسابية؟ وأي دلالة لها، أهي رياضية كمية أم
  معياريّة كيفية؟
- أحدّد دلالة " الوسط العدل " مستثمرا أمثلة النص وأكشف عن آلية تحديده.
- أمتحن قيمة التصور الأرسطي للفضيلة ومبدأ الوسط العدل وأتبين حدوده على صعيد التجربة والممارسة.

---

###### سند 2 — أحمد بن مسكويه — « ما الخير؟ » — p.354-355

- **Auteur tel qu'imprimé** : **أحمد بن مسكويه** (ligne de source et notice) ; l'encadré de citation
  final (p.355) l'abrège en **« مسكويه »**. ⚠️ Le فهرس annonce « ابن مسكويه » ; la page de titre de
  la نافذة مدخل (p.348) imprime elle aussi « أحمد بن مسكويه ». **Aucune ligne latine** pour ce سند.
- **Titre du سند** : **ما الخير؟**
- **Source** : أحمد بن مسكويه؛ تهذيب الأخلاق، ص 78—79، منشورات دار مكتبة الحياة، بيروت 1961
- **Illustrations** : (p.354) gravure d'un savant en turban, debout, un livre à la main ;
  (p.355) mosaïque antique — un groupe de philosophes drapés autour d'un maître assis.

**التمهيد (verbatim)** :
> ينشد البشر السعادة بسبل متعددة ولكل له منها نصيب. غير أن إجماعهم عليها غاية قصوى تُطلب في فعل
> الخير هو بقدر اختلافهم حول حقيقتها اختلافا يُردُّ إلى ما يكونه الخير عندهم وصلته بالسعادة.

**Thèse (reformulée)** : le bien, au sens que les Anciens lui donnaient, est **la fin dernière
visée par tous** ; le **bonheur** est un bien, mais un bien **relatif à celui qui l'éprouve** — il y
a un bonheur du cheval distinct de celui de l'homme, chaque être ayant sa perfection propre. D'où
la distinction : le **bien** que tous désirent est un bien **général et par soi**, tandis que le
**bonheur** est **relatif** et diffère selon ceux qui le visent, tandis que le **bien absolu**,
lui, **n'est pas objet de désaccord** (`الخير المطلق غير مختلف فيه`).
Le bonheur au sens propre suppose **intention, réflexion et volonté**
et n'appartient donc qu'aux êtres doués de parole/raison (`النّاطقين`) — ce que l'animal atteint
relève du hasard, non du bonheur. La raison ne pouvant se mouvoir à l'infini, il **faut** une fin
dernière, et le devoir est de **connaître** cette fin ultime des biens pour en faire notre but,
sous peine d'user notre vie à poursuivre ce qui n'est pas un bien.

⚠️ **La négation `غير` porte tout l'argument.** C'est **parce que** le bonheur est relatif à celui
qui le vise (`وهي تختلف بالإضافة إلى قاصديها`) que le bien absolu, lui, **ne l'est pas**
(`فلذلك يكون الخير المطلق غير مختلف فيه`). La laisser tomber renverse la thèse de ابن مسكويه et
détruit le raisonnement.

**الهامشان** (titre de l'encadré imprimé **au duel** — verbatim) :
1. **حدّه**: من التحديد، وهو التعريف.
2. **المتقدمين**: المقصود بالخصوص أرسطوطاليس.

⚠️ Le **هامش n° 2** appelle Aristote **« أرسطوطاليس »** ici, alors que le سند 1 l'imprime
**« أرسطو »**. Variante constatée dans le même مبحث. *(La notice `الكاتب`, p.355, ne nomme jamais
Aristote.)*

**الكاتب** (p.355 — notice pleine, verbatim resserré) :
> **أحمد بن مسكويه** : هوّ أحمد بن محمّد بن يعقوب مسكويه، فيلسوف معاصر للبيروني وابن سينا، وُلد في
> الريّ وتوفّي في أصفهان سنة 421هـ / 1030 م. اشتغل بالطبّ والكيمياء علاوة على الفلسفة، كانت له
> منزلة كبيرة في بلاط البويهيين. كتب بالعربيّة وبالفارسيّة وترك زهاء عشرين مصنّفا. له في الفلسفة
> الأخلاقيّة " تهذيب الأخلاق وتطهير الأعراق "، اهتمّ فيه بصناعة الأفعال الجميلة، وقد كال له نصير
> الدّين الطّوسي الثناء الكبير في مقدّمة كتابه عن الأخلاق. وفي التاريخ له " تجارب الأمم وتعاقد الهمم "
> ولامس فيه أحوال البشر وقد قدّم له بكتاب " الحكمة الخالدة " واشترك مع التوحيدي في كتاب
> " الهوامل والشوامل " وكتب في الأخلاق " الفوز الكبير " و " الفوز الصغير ".

(Les titres d'ouvrages sont imprimés en **bleu** dans la notice.)

**المهام (verbatim, 5 puces)** :
- ما هو تحديد الخير الذي ينسبه الكاتب إلى الأقدمين؟
- ما هي علاقة الخير بالسعادة؟
- كيف أفهم اختلاف السعادة باختلاف قاصديها؟
- هل السعادة شأن الإنسان أم الحيوان؟ أعلل جوابي.
- أفهم الصلة بين الخير المطلق والعقل.

**Encadré de citation final** (p.355, verbatim) :
> " إنّ الخير على ما حدّه وأستحسنه من آراء المتقدّمين هو المقصود من الكلّ، وهو الغاية الأخيرة ".
> — **مسكويه**

---

###### سند 3 — سبينوزا — « الفاضل » — p.356-357

- **Auteur tel qu'imprimé** : **سبينوزا** ; ligne latine **`SPINOZA`**.
- **Titre du سند** : **الفاضل**
- **Source** : سبينوزا، علم الأخلاق، الجزء الرابع، ص 280—284، ترجمة جلال الدّين سعيد، دار الجنوب
  للنشر (1991) — `SPINOZA, Ethique, Partie IV, Coll GF, Flammarion, 1965, pp 238-241`
- **Illustrations** : (p.356) portrait gravé de Spinoza ; (p.357) photographie d'une girouette —
  un homme en costume jaune, chapeau melon et serviette, juché sur la flèche, points cardinaux
  `W N S E`.

**التمهيد (verbatim)** :
> لا غرابة أن ننشد الفضيلة بقدر ما ننبذ الرذيلة، غير أن الطابع الملتبس لمعاني الفضيلة والرذيلة،
> يجعل من المنشود قيمة فضفاضة تحتاج منا نظرا وتدقيقا علّنا نتجاوز الإرباك الذي ينتابنا حين نسأل عن
> الخيط الفاصل بينهما، أو علنا نمسك بالخيط الذي يجعلنا نتحقق مِن الفضيلة دون أن نضطر إلى التغافل
> عن طبيعتنا الخاصة، ودون أن نغض الطرف عن منفعتنا الخاصة.

**Thèse (reformulée)** : nous sommes **vertueux dans l'exacte mesure** où nous cherchons ce qui nous
est utile, c'est-à-dire ce qui **conserve notre être** (`حفظ كياننا`), et impuissants dans la mesure
où nous le négligeons. La vertu **est** la puissance même de l'homme, définie par sa seule essence,
c'est-à-dire par l'effort qu'il déploie pour **persévérer dans son existence**. Agir par vertu, agir
selon la raison, vivre et conserver son être, chercher son utilité propre : ce sont des
**expressions synonymes**. Et l'on n'agit véritablement — au lieu de pâtir — que **par la
connaissance** : mû par des idées inadéquates on est passif, mû par la connaissance on est actif,
et l'acte découle alors de sa **vertu propre**.

**هوامش** : **aucun encadré de notes.**

**الكاتب** — ⚠️ **RENVOI**, imprimé verbatim :
> **سبينوزا** راجع التعريف بسبينوزا في السند عدد 11 (الإنيّة والغيرية)

**المهام** (p.357 — verbatim, 6 puces) :
- أتبين الصلة بين الجهد والفضيلة.
- أي دلالة للمنفعة تتحدد بها الفضيلة حسب الكاتب؟
- يقحم الكاتب المعرفة والعيش وفق ما يمليه العقل في تحقيق الفضيلة. كيف تفهم هذه الصلة؟
- ألا يبدو من التناقض تعريف الفضيلة بالمنفعة وحفظ الكيان وربط تحقيقها بالعيش وفق ما يمليه العقل؟
- أستخلص دلالة الفضيلة.
- أي تصوّر للسعادة يتولّد عن تحديد الكاتب للفضيلة؟

**Encadré de citation final** (p.357, verbatim) :
> " فبقدر ما يجدّ المرء في حفظ كيانه وبقدر ما تكون له القدرة على ذلك، يكون فاضلا ".
> — **سبينوزا**

---

###### سند 4 — ستيوارت ميل — « المنفعة أساس الأخلاق » — p.358-359

- **Auteur tel qu'imprimé** : ⚠️ **deux graphies dans le même سند** — la ligne de source (p.358)
  imprime **« ستيوارت ميل »**, le renvoi الكاتب (p.359) imprime **« ستيوارت مل »** (sans yâ'),
  et l'encadré de citation final abrège en **« ميل »**. Ligne latine : **`Stuart MILL`**.
- **Titre du سند** : **المنفعة أساس الأخلاق**
- **Source** : ستيوارت ميل؛ في النفعية — `Stuart MILL; De l'utilitarisme, 2, p 191`
- **Illustrations** : (p.358) portrait photographique ancien de Mill ; (p.359) photographie —
  quatre silhouettes se tenant par la main courent sur une passerelle, sur fond de ciel orange.

**التمهيد (verbatim)** :
> قد تبدو حياة الإنسان تجربة قوامها جدليّة الألم واللذّة، البؤس والغبطة، نقائض قد لا تفيد استحالة
> أن يكون المرء سعيدا، وإنّما قد تجعل من السعادة جدارة هيّ محصّلة الوعي والجسارة.

**Thèse (reformulée)** : la doctrine qui fait de l'utilité — ou du **principe du plus grand
bonheur** — le fondement de la morale tient les actes pour **bons dans la mesure où ils produisent
du bonheur**, mauvais dans la mesure où ils produisent son contraire ; bonheur signifiant plaisir
et absence de douleur. Contre l'objection qui y voit une « doctrine de pourceaux », Mill répond que
les utilitaristes reconnaissent aux plaisirs de l'**esprit** une supériorité **de qualité**, non
seulement de durée ou d'intensité : l'être doté de facultés supérieures est plus difficile à
satisfaire, mais ne consentirait pas à descendre — d'où la formule reprise en encadré, mieux vaut
être **un homme insatisfait qu'un porc satisfait**, car celui qui ne connaît qu'un côté de la
question ne peut arbitrer. En résumé, la fin suprême est une vie **aussi exempte de douleur que
possible et aussi riche que possible en plaisirs, en quantité comme en qualité** — que l'intérêt
en cause soit le nôtre ou celui d'autrui.

**الهامش** (titre de l'encadré **au singulier** — une seule note, verbatim) :
1. **أبيقور** `Epicure` : ( 270 — 341 ق م) من أبرز الفلاسفة الذريين وهو أحد روّاد ما يسمّى بأخلاق
   اللّذة باعتبار أنّ الخير الأسمى عنده هو اللّذة.

   *(Intervalle composé mort → naissance, comme partout dans ce مبحث — voir
   § Avertissement transversal sur les intervalles de dates. Valeur à retenir : 341 — 270 ق.م.)*

**الكاتب** — ⚠️ **RENVOI**, imprimé verbatim :
> **ستيوارت مل** راجع التعريف بالكاتب في السند عدد 13 (الدولة : السيادة والمواطنة)

**المهام (verbatim, 6 puces)** :
- أستخرج تحديد الكاتب للسعادة وأحدّد المعيار الذي أقيسها به.
- بأيّ معنى تكون المنفعة مبدأ للسعادة وأساسا للفعل الأخلاقي؟
- ما هو أساس المفاضلة بين لذّات العقل ولذّات الجسد؟
- كيف يكون صاحب ملكات تلذّذ أقل أوفر حظّا في تلبية رغباته؟
- هل في جعل المنفعة مبدأ للأخلاق ما يفيد الإفراط في طلب اللذة؟
- كيف أفهم القول " من الأفضل إذن، أن يكون المرء إنسانا غاضبا على أن يكون خنزيرا راضيا "؟

**Encadré de citation final** (p.359, verbatim) :
> " يكون الهدف الأسمى هو حياة خالية أكثر ما يكون من الألم، ثرية قدر المستطاع باللذات كمّا وكيفا ".
> — **ميل**

---

###### سند 5 — كانط — « الإنسان غاية » — p.360-361

- **Auteur tel qu'imprimé** : **أ. كانط** (ligne de source ET renvoi الكاتب) ; l'encadré de citation
  final abrège en **« كانط »**. ⚠️ Le سند 7 (p.364), du même auteur, imprime **« إ. كانط »** —
  initiale différente. **Aucune ligne latine** pour ce سند.
- **Titre du سند** : **الإنسان غاية**
- **Source** : أ. كانط؛ تأسيس ميتافيزيقا الأخلاق — ترجمة عبد الغفّار مكّاوي، منشورات الجمل 2002.
  **ص107 — 901**

  ⚠️ **Tel qu'imprimé : `ص107 — 901`** (vérifié par agrandissement). Le second nombre, `901`, ne peut
  pas être une page de fin après 107 ; il s'agit très probablement de `109` dont les chiffres ont
  été inversés à la composition. **Signalé, non corrigé.**

- **Illustrations** : (p.360) portrait gravé de Kant ; (p.361) illustration en pastel — deux hommes
  aux bras démesurément allongés, l'un remettant une liasse de billets à l'autre.

**التمهيد (verbatim)** :
> قد لا يفهم الأخلاقي إلاّ بما هو شأن إنساني، يرسم صورة الإنسان باعتباره كائنا أخلاقيا في علاقة
> بذاته وبالآخرين، صورة قد تهتزّ حين نستيقظ على ما يجب أن تكون عليه هذه الصّورة من جهة ما هو كائن.

**Thèse (reformulée)** : l'homme — et tout être raisonnable en général — existe comme **fin en soi**,
non comme simple **moyen** dont telle ou telle volonté pourrait user à sa guise ; dans chacun de ses
actes il doit être considéré **en même temps comme une fin**. Les objets des inclinations n'ont
qu'une valeur **conditionnée** — sans les besoins qui les fondent ils n'auraient aucune valeur, et
les inclinations elles-mêmes, sources de besoin, sont si peu désirables que le vœu de tout être
raisonnable est d'en être **entièrement affranchi**. D'où la partition : les êtres **non**
raisonnables, dont l'existence ne dépend pas de notre volonté mais de la nature, n'ont qu'une valeur
**relative** de moyens et se nomment **أشياء** ; les êtres raisonnables se nomment **أشخاص**, parce
que leur nature même les désigne comme **fins en soi**, donc comme ce dont on ne peut user comme
d'un simple moyen — ce qui limite tout arbitraire et fait d'eux **objets de respect**. Ce ne sont
pas des fins **subjectives** (dont la valeur nous viendrait de nos actes) mais des fins
**objectives**, dont l'existence est en elle-même une fin **irremplaçable** ; sans quoi rien
n'aurait jamais de valeur absolue. D'où la formule pratique : **agis de telle sorte que tu traites
l'humanité, en ta personne comme en celle des autres, toujours comme une fin et jamais simplement
comme un moyen.**

**هوامش** : **aucun encadré de notes.**

**الكاتب** — ⚠️ **RENVOI**, imprimé verbatim :
> **أ. كانط** راجع التعريف بكانط في السند عدد 4 (الخصوصيّة والكونيّة)

**المهام** (p.361 — verbatim, 5 puces) :
- في أيّ معنى يكون الإنسان غاية في حدّ ذاته؟
- ما الذي يميّز الشّخص عن الشّيء؟
- ما أساس جدارة فعل يكون موضوعا للاحترام؟
- أحدّد دلالة " غاية " وأميّز بين غاية موضوعية وغاية في حدّ ذاتها.
- هل لا تكونُ القيم أخلاقية بحق، إلا إذا كانت مطلقة؟

**Encadré de citation final** (p.361, verbatim) :
> " الإنسان… يوجد من جهة ما هو هدف في ذاته لا من جهة ماهو مجرّد وسيلة يمكن لهذه الإرادة أو تلك أن
> تستخدمه على هواها ".
> — **كانط**

---

###### سند 6 — كيركغارد — « ما الواجب؟ » — p.362-363

- **Auteur tel qu'imprimé** : **كيركغارد** (ligne de source, notice et encadré final) ;
  ligne latine **`KIERKEGAARD`**.
- **Titre du سند** : **ما الواجب؟**
- **Source** : كيركغارد، مقالة في القلق —
  `KIERKEGAARD, Traité de l'angoisse. éd. Gallimard, 1962, p 92`
- **Illustrations** : (p.362) portrait gravé de Kierkegaard ; (p.363) dessin humoristique — un
  personnage blanc au torse marqué **`MORALE`**, deux petits hommes en noir accrochés à ses bras.

**التمهيد (verbatim)** :
> كثيرا ما يستدعي الحديث عن الأخلاق استحضار مفهوم الواجب الذي يقترن في الأذهان بمنطق الإلزام
> والقهرية بما أنّه يخاطبنا بمنطق الأمر والنهي، غير أنّ النظر إلى الإنسان بما هو كائن أخلاقي قد
> يجعل من هذا التحديد للواجب ملتبسا وإشكاليا سواء من جهة علاقة الإنسان بذاته أو من جهة علاقته
> بالآخرين.

**Thèse (reformulée)** : il est étonnant qu'en parlant du **devoir** nous parlions de quelque chose
d'**extérieur**, alors que le mot lui-même renvoie à quelque chose d'**intérieur** : ce qui m'oblige
selon ma vraie nature, en tant que je suis un individu, entretient avec moi une relation
**intime**. Le devoir n'est pas un simple ordre reçu, c'est ce qui **s'impose au soi** ; l'individu
qui le regarde ainsi prouve qu'il **se tourne vers lui-même**. Le devoir est donc **indivisible**
par rapport à l'individu, en ce qu'il n'existe jamais que dans une relation d'extériorité à des
dispositions particulières, alors qu'il devrait exprimer sa nature propre. Quand l'individu
**enracine le devoir en lui-même**, il approfondit la morale : il n'est plus contraint, l'individu
moral est **réel** et se sent en sécurité et en paix parce que son devoir n'est pas hors de lui mais
en lui. Et plus un homme fonde sa vie en profondeur sur la morale, **moins** il éprouve le besoin
d'en parler sans cesse, de savoir ce qu'elle signifie, ou de revenir à chaque fois vers les autres
pour le savoir.

**هوامش** : **aucun encadré de notes.**

**الكاتب** (p.362 — **notice pleine**, verbatim resserré) :
> **كيركغارد** ( 1855-1813 ) : فيلسوف دنماركي، كانت طفولته فريدة وتنبؤُ عن حياة فريدة، ومن الممكن
> تمييز ثلاثة أطوار في هذه الحياة: الطور الجمالي والطور الأخلاقي والطور الديني، وهو التقسيم الذي
> وضعه بنفسه، وهي لا تفيد تعاقبا في طرائق التفكير طبقا لقاعدة فنّية ولا لقانون أخلاقي أو لإيمان
> ديني، بقدر ما تفيد علاقة وثيقة بين أنماط الفكر وأساليب العيش. بدأ حياته ماجنا، وكان يردّد قول
> **أوغستين** `St. Augustin` (430—354) " كانت أشواك اللذات تنمو فوق رأسي "، ولأنّه كان رجل لذّة،
> فقد كان متمرّدا على الكنيسة، إذ يعتبرها أداة لتبليد العقل. يتمحور تفكيره الفلسفي حول " دراما "
> الوجود الإنساني، قلق الفرد ووحدته إزاء المجموعة، وحول الهيمنة الجليدية للعقل. يعدّ كتاب
> " إمّا…وإمّا " (1843) أحد أبرز مؤلّفاته وقد أثّر في الفكر الوجودي المعاصر الذي استمدّه من تجارب
> حياته. ومن مؤلّفاته سلسلة من المقالات المختلفة حول القلق والنقد والجمال والأدب والموسيقى. ألّف
> أيضا " خوف وزلزال " (1843) و " مقالة في اليأس " (1849). وهي مؤلّفات تتمحور حول تعابيره المباشرة
> وغير المباشرة للصراع اليائس، واللامعقول والمتشنّج الذي يخوض الإنسان غماره ضدّ الخطيئة وضدّ أهوال
> الحياة التي تتأتّى منها.

*(Les deux intervalles sont composés mort → naissance, comme partout dans ce مبحث — voir
§ Avertissement transversal sur les intervalles de dates. Valeurs à retenir : Kierkegaard
1813 — 1855, Augustin 354 — 430.)*

**المهام** (p.363 — verbatim, 6 puces) :
- ما هي طبيعة الواجب في نظر الكاتب؟ أحدّد الفرق بين ضربين من الواجب.
- أيّ غنم يحصل لنا عند توجّهنا لذواتنا؟
- ما الذي ينجرّ عن واجب يُفرَضُ علينا من خارج؟
- أستثمر مكتسباتي حول الواجب وأستخلص طرافة تصوّر الكاتب له.
- ما الذي يستتبع ردّ الواجب إلى نداء الذات في شأن علاقتي بالآخرين؟
- هل أجد صلة بين الحريّة ومفهوم الواجب كما حدده الكاتب؟

**Encadré de citation final** (p.363, verbatim) :
> " يبدو مدهشا جدّا، أنّه حين نتحدّث عن الواجب، نتحدّث عن شيء خارجي ".
> — **كيركغارد**

---

###### سند 7 — كانط — « الأمر الأخلاقي » — p.364-365

- **Auteur tel qu'imprimé** : **إ. كانط** dans la ligne de source (p.364), **أ. كانط** dans le
  renvoi الكاتب (p.365), **كانط** dans l'encadré final. ⚠️ Trois formes pour le même auteur, dans le
  même سند. **Aucune ligne latine.**
- **Titre du سند** : **الأمر الأخلاقي**
- **Source** : إ. كانط؛ تأسيس ميتافيزيقا الأخلاق — ترجمة عبد الغفّار مكّاوي، منشورات الجمل ، 2002.
  ص 113— 115
- **Illustrations** : (p.364) portrait gravé de Kant (autre gravure que celle du سند 5) ;
  (p.365) image de synthèse — une figure humaine métallique agenouillée, bras levés, devant un
  **doigt jaune géant** pointé sur elle.

**التمهيد (verbatim)** :
> قد لا يفهم الضابط الأخلاقي إلاّ بما هو إلزام نخضع له آليّا بموجب مقتضيات الحياة الاجتماعية، أو
> بموجب الانشداد إلى مصلحة ذاتية أو منفعة خاصّة، غير أن اقتران الحديث عن الأخلاقيّ باستحضار معاني
> السموّ والرفعة قد يثير فينا السؤال عن مدى إمكان أن يستحيل الإلزام التزاما، والخضوع طاعة إراديّة،
> تجعل للفعل الأخلاقي حقيقة مغايرة.

**Thèse (reformulée)** : les **impératifs moraux** — qu'ils exigent la conformité des actes à une
législation universelle analogue à l'ordre de la nature, ou qu'ils veuillent que les êtres
raisonnables aient le privilège d'être des **fins en soi** — excluent de leur autorité **tout
mélange d'intérêt** (`كلّ خليط من منفعة`), quel qu'il soit : c'est cette exclusion qui nous les fait
concevoir comme **absolus** (catégoriques). L'affranchissement de tout intérêt est précisément la
**marque distinctive** qui sépare l'impératif absolu de l'impératif **hypothétique** (`الشّرطيّة`).
Une volonté qui obéirait à des lois liées à un intérêt ne pourrait pas être **législatrice
suprême** : elle aurait besoin d'une autre loi pour limiter l'amour de soi et conditionner sa
validité. Le principe de toute volonté humaine comme volonté **universellement législatrice** est
donc, s'il est exact, apte à être un impératif **catégorique** — parce qu'il ne repose sur aucun
intérêt et qu'il est le seul, parmi tous les impératifs possibles, à être **inconditionné**. Ou,
mieux : s'il existe un impératif moral absolu, il ne peut qu'ordonner que tous les actes de l'homme
dérivent d'une volonté qui puisse **en même temps** se prendre elle-même pour objet en tant que
législatrice universelle — alors seulement le principe pratique et l'ordre auquel l'homme obéit sont
**inconditionnés**, parce qu'il n'y a **aucun intérêt** sur lequel ils puissent se fonder.

**هوامش** : **aucun encadré de notes.**

**الكاتب** — ⚠️ **RENVOI**, imprimé verbatim (identique à celui du سند 5) :
> **أ. كانط** راجع التعريف بكانط في السند عدد 4 (الخصوصيّة والكونيّة)

**المهام** (p.365 — verbatim, 7 puces) :
- أحدّد معنى الأمر الأخلاقي وأميّز بين الأمر الشرطي والأمر القطعي.
- كيف أفهم الواجب الأخلاقي في ضوء تحديد الكاتب للأمر الأخلاقي؟
- ما هو المشرّع الأعلى للأمر الأخلاقي؟
- ما الذي يبرّر استبعاد الكاتب للمنفعة في تحديد الفعل الأخلاقي؟
- هل من تعارض بين طاعة الواجب وحريّة الذاّت؟
- إذا سلّمنا بضرورة الفصل بين المنفعة والفعل الأخلاقي، فهل يمكن أن تكون السعادة غاية لهذا الفعل؟
- أمتحن وجاهة الفصل بين الواجب الأخلاقي والمنفعة في ضوء واقع تجربتي بما أنا ذات في علاقة بالآخرين.

**Encadré de citation final** (p.365, verbatim) :
> " إنّ الأوامر الأخلاقيّة…قد استبعدت حقًّا عن سلطانها الآمر، كلّ خليط من منفعة، أيّا كان نوعها ".
> — **كانط**

---

###### سند 8 — إميل دوركايم — « في نقد الواجب » — p.366

⚠️ **سند sur une seule page** — التمهيد, texte, source, الكاتب et المهام tiennent tous sur p.366.
**Ni encadré de notes, ni illustration finale, ni encadré de citation.** La double page n'est donc
décidément pas le gabarit.

- **Auteur tel qu'imprimé** : **إميل دوركايم** ; ligne latine **`E. DURKHEIM`**.
- **Titre du سند** : **في نقد الواجب**
- **Source** : إميل دوركايم، علم الاجتماع والفلسفة —
  `E. DURKHEIM; Sociologie et philosophie, éd. PUF, 1924 pp 63-65.`
- **Illustration** : portrait photographique ancien de Durkheim (vignette dans le texte).

**التمهيد (verbatim)** :
> عادة ما نُجمع على أنّ الخير هو معيار الفعل الأخلاقي، ونسلّم به بداهة. غير أنّ التجربة الأخلاقيّة
> تكشف التباسه حينما تطرح شروط تحققه، التباسا يجعله موضع جدال لا ينتهي.

**Thèse (reformulée)** : l'analyse kantienne de l'acte moral, si juste soit-elle, reste
**insuffisante et inachevée**, car elle n'en découvre qu'**une seule face**. De fait, nous ne pouvons
accomplir un acte qui ne signifierait rien pour nous sous prétexte qu'il est simplement imposé :
poursuivre une fin qui ne nous meut pas, ne nous paraît pas bonne et ne touche pas notre
sensibilité est **psychologiquement impossible**. Il faut donc que la fin morale soit, outre son
caractère **obligatoire** (`الإلزامية`), **désirable et désirée** (`مرغوبا فيها ومطلوبة`) — cette
désirabilité est une propriété **constante de tout acte moral**. Le devoir, ou l'impératif kantien,
n'est qu'**un des deux visages** du réel moral : les deux sont toujours présents et **inséparables**.
Il n'est jamais arrivé qu'un acte procède du seul devoir, car un acte doit toujours se montrer bon
d'une manière ou d'une autre ; inversement, il est peu probable que les deux faces **ne soient pas
désirées**, **puisqu'elles appellent toujours un effort** (`إذ يستدعيان جهدا على الدوام`).
De même, la notion d'**obligation** — première
caractéristique de la vie morale — permet de **critiquer l'utilitarisme**, tandis que la seconde
caractéristique fait apercevoir les **limites de l'explication kantienne** : l'hypothèse kantienne
d'une **hétérogénéité radicale** entre raison et sensibilité rend malaisé de concilier cette
hétérogénéité avec le fait que les fins morales sont, par un de leurs visages, **objets de désir** ;
et si la sensibilité a la même fin que la raison, elle ne s'amoindrit pas en s'y soumettant.

⚠️ **Double garde sur la phrase « inversement… ».** Le manuel imprime
`وبالمقابل ليس من المحتمل ألاّ يكون الوجهان مرغوبا فيهما إذ يستدعيان جهدا على الدوام.` :
(a) la négation `ألاّ` porte sur `يكون … مرغوبا فيهما` — il est peu probable que les deux faces **ne
soient PAS** désirées, ce qui rend leur désirabilité **probable**, non improbable ;
(b) la raison donnée est `إذ يستدعيان جهدا على الدوام` (« puisqu'elles appellent toujours un
effort »), **pas** un soutien mutuel des deux faces, formule absente de la page.

**هوامش** : **aucun encadré de notes.**

**الكاتب** — ⚠️ **RENVOI**, imprimé verbatim :
> **إميل دوركايم** : راجع التعريف بدوركايم في السند عدد 20 ( الخصوصيّة والكونيّة )

**المهام (verbatim, 7 puces)** :
- أستحضر التصوّر الكانطي للفعل الأخلاقي، وأتبيّن وجه اعتراض الكاتب عليه.
- يتحدّث الكاتب عن وجهين للفعل الأخلاقي : أحدّدهما وأتبيّن الصّلة بينهما.
- هل أنّ أخلاقيّة الفعل في ما يستحسنه العقل أم في ما تنشده الرّغبة؟
- هل من تناقض بين اعتبار الخير موضوع إلزام وموضوع رغبة في آن؟
- أستخلص خصائص الظّاهرة الأخلاقيّة حسب الكاتب في ضوء نقده للتصوّر الكانطي.
- أي تصوّر للعقل يفترضه القول إنّ للحساسية الغاية نفسها التي للعقل؟
- أستخلص دلالة الواجب وطبيعته في نظر الكاتب.

---

###### ⚠️ Avertissement transversal — les intervalles de dates sont composés à l'envers

Ce n'est **pas** une anomalie ponctuelle page par page : c'est **une seule convention de
composition** du manuel (couche QuarkXPress en ordre visuel). Partout où un intervalle de dates est
inséré dans ce مبحث, **la borne haute est écrite la première** — autrement dit **mort → naissance**,
l'inverse de l'usage. **Sept** occurrences, une seule exception.

**Convention de ce tableau** : la colonne « ordre imprimé » **nomme** les bornes au lieu de les
recopier. Une chaîne de chiffres recopiée dans un contexte arabe est elle-même retournée par
l'algorithme bidi, si bien qu'un relevé littéral n'est ni lisible ni reproductible — c'est ce qui
avait fait cohabiter ici deux conventions contradictoires. La colonne « valeur à retenir » est
celle que la fiche emploie partout ailleurs.

| page | occurrence | ordre imprimé | valeur à retenir |
| --- | --- | --- | --- |
| p.358 | هامش, أبيقور | mort (270) puis naissance (341) | 341 — 270 ق.م |
| p.362 | notice, كيركغارد | mort (1855) puis naissance (1813) | 1813 — 1855 |
| p.362 | notice, أوغستين | mort (430) puis naissance (354) | 354 — 430 |
| p.375 | notice, دو أولباخ | mort (1789) puis naissance (1723) | 1723 — 1789 |
| p.379 | هامش, توكفيل | mort (1853) puis naissance (1805) | 1805 — 1853 ⚠️ *le manuel donne **1853** ; l'usage donne **1859*** |
| p.389 | سياقات فكريّة, العدميّة, نيتشه | mort (1900) puis naissance (1844) | 1844 — 1900 |
| p.397 | légende de la couverture, نيتشه | mort (1900) puis naissance (1844) | 1844 — 1900 |

**Exception** : p.371 (notice, أبيقور) est le **seul** intervalle composé dans l'ordre attendu —
naissance (341) puis mort (271).
Et ⚠️ **cette notice donne 271 là où le هامش de la p.358 donne 270** pour la mort d'Épicure :
**contradiction interne du manuel**, sur deux pages du même مبحث.

**Cas distinct — ce n'est pas un intervalle de dates** : p.360, ligne de source de كانط, imprime
**`ص107 — 901`**. `901` est la pagination **109** dont les chiffres sont retournés ; la référence
réelle est **ص 107 — 109**. Consigné ici pour qu'on ne le range pas avec les intervalles ci-dessus.

⚠️ **Règle unique, à appliquer partout** : les **blocs verbatim** (هوامش, notices, lignes de
source) **reproduisent l'imprimé** ; le **texte courant et les reformulations normalisent**
(naissance → mort) ; **ce tableau est le seul registre de l'anomalie**. Ne pas rouvrir de ⚠️
locale sur un سند pour ce motif, et **ne jamais bâtir de question sur l'ordre des bornes**.

---

###### سند 9 — نيتشه — « أخلاق القوّة » — p.367-368

- **Auteur tel qu'imprimé** : **نيتشه** ; ligne latine **`NIETZSCHE`**.
- **Titre du سند** : **أخلاق القوّة**
- **Source** : نيتشه، ما وراء الخير والشر —
  `NIETZSCHE. Par- delà le bien et le mal. Mercure de France, p 216 - 217`
- **Illustrations** : (p.367) portrait photographique de Nietzsche ; (p.368) sculpture — un homme
  nu de pierre, jambes écartées au-dessus d'une faille, soutenant une **sphère** au-dessus de sa
  tête, sur ciel violet.

**التمهيد (verbatim)** :
> يتراوح حال النّاس بين قويّ ينزع إلى الغلبة وضعيف يميل إلى الخضوع وكلّ يبرّر حاله، ويتخفّى وراء
> قيم من صنعه، فيلتبس على الناظر أمر الأخلاق فيكون مطلب السؤال عن حقيقة القيم وجدارتها.

**Thèse (reformulée)** : il existe une **morale des maîtres** et une **morale des esclaves**.
L'homme noble se sépare des êtres en qui les sentiments de grandeur et de fierté paraissent niés :
il les méprise. La première opposition morale — noble / vil — n'a pas la même origine que
l'opposition bien / mal, qui vient d'ailleurs. Est méprisé le lâche, le craintif, l'homme du regard
inquiet qui se rabaisse, le chien qui se laisse maltraiter, le mendiant flatteur, et surtout le
**menteur** : c'est un lieu commun de l'aristocratie que le peuple est menteur — « nous, à leur
différence, sommes les véridiques ». L'homme noble possède le sentiment profond qu'il a le **droit
de fixer la valeur** : il ne demande l'assentiment de personne, il décrète que « ce qui m'est
nuisible est nuisible en soi », il sait que c'est lui qui **confère l'honneur** aux choses, il est
**créateur de valeurs** — une telle morale est une **glorification de soi**. On y trouve le sentiment
de plénitude, la puissance qui déborde d'activité, le bonheur de la haute tension, la conscience
d'une richesse qui aime à donner : l'homme noble secourt aussi le malheureux, mais **non par pitié**
— par surabondance de force. Le noble honore en lui la puissance et le pouvoir de se maîtriser ;
inversement, les morales qui font de la pitié, de l'abnégation ou du désintéressement le signe
distinctif de l'acte moral sont l'**exact contraire** de cette morale des nobles, laquelle tient
plutôt à la foi en soi, à la fierté, à l'hostilité et à l'ironie envers l'abnégation et les
« cœurs chaleureux ».

**الهامش** (une note, verbatim) :
1. **فيكينغ** `Wiking` : قراصنة سكندنافيين إجتاحوا أوروبا في القرنين 10 و 11 م .

   ⚠️ **Tel qu'imprimé** : la translittération latine est **`Wiking`** (et non *Viking*), l'arabe
   **`سكندنافيين`** (sans alif initial) et **`إجتاحوا`** (avec hamzat qaṭ'). **Non corrigé.**

**الكاتب** — ⚠️ **RENVOI**, imprimé verbatim :
> **نيتشه** : راجع التعريف بنيتشه في السند عدد 19 (الإنيّة والغيريّة )

**المهام** (p.368 — verbatim, 4 puces) :
- يميّز الكاتب بين أخلاق للأسياد وأخرى للعبيد : أيّ دلالة لهذا التمييز وما أساسه؟
- كيف أفهم علاقة التساوي بين زوج " حسن – سيء " وبين زوج " نبيل – حقير "؟
- ما أصل نقيضة " خير – شر " في نظر الكاتب؟
- هل تمثل المقاربة النيتشوية تكريسا للمفاضلة الأخلاقية أم دعوة للانعتاق والتحرر؟

**Encadré de citation final** (p.368, verbatim) :
> " توجد أخلاق للأسياد وأخرى للعبيد.(…) والإنسان النبيل ينفصل عن الكائنات التي تبدو نقيضا لمشاعر
> العظمة والفخر؛ فهو يحتقرها ".
> — **نيتشه**

---

###### سند 10 — كارل ماركس وانغلز — « الأخلاق والمجتمع » — p.369

⚠️ **سند sur une seule page.** Ni encadré de notes, ni illustration finale, ni encadré de citation.

- **Auteurs tels qu'imprimés** : **كارل ماركس وانغلز** ; ligne latine **`Karl MARX et F. ENGELS`**.
  (Engels rendu **انغلز** en arabe ; le renvoi الكاتب écrit **« ماركس وانغلز »**.)
- **Titre du سند** : **الأخلاق والمجتمع**
- **Source** : كارل ماركس وانغلز، الإيديولوجيا الألمانية —
  `Karl MARX et F. ENGELS; Idéologie allemande, III, p. 77.`
- **Illustration** : portrait photographique de Marx (vignette dans le texte).

**التمهيد (verbatim)** :
> دأب الموروث الفلسفي الكلاسيكي على اعتبار الإنسان ماهية مجرّدة، مما اقتضى استبعاد الأهواء
> واعتبارها أمرا عارضا، غير أن واقع البشر قد يسمح بالتظنّن على هذا التصوّر ويفسح المجال لمساءلة
> دور الأهواء في تأصيل علاقة الإنسان بالحياة والعالم، بل وتحديد منزلته الأخلاقية.

**Thèse (reformulée)** : c'est une **absurdité** de supposer qu'on puisse satisfaire une passion
isolément des autres, ou satisfaire l'individu sans le satisfaire tout entier. Si cette passion
prend un caractère **abstrait et autonome**, si elle m'apparaît comme une force **étrangère** et
que la satisfaction de l'individu se réduit à **une seule** de ses faces, la cause n'est ni la
conscience ni la « bonne volonté », ni un défaut de pensée sur la signification des facultés
morales. La cause doit être rapportée non à la **conscience** mais à l'**existence**, non à la
pensée mais à la **vie** : la cause est la vie concrète de l'individu, elle-même **suspendue aux
conditions matérielles du monde**. Quand les conditions dans lesquelles l'individu vit ne
permettent le développement que d'**une seule** de ses facultés aux dépens des autres, cet individu
ne peut se développer que **d'un seul côté**, mutilé — et **aucune prédication morale n'y changera
rien**. Pour un individu dont la vie couvre un large cercle d'activités et de rapports pratiques
avec le monde, la pensée possède la même **universalité** que tout autre trait de sa vie ;
inversement, l'individu misérable, dont les rapports au monde sont étroits, n'a d'autre issue que de
se réfugier dans la pensée, dont l'abstraction croît à mesure que sa vie s'appauvrit — pensée
désarmée, séparée de lui comme une **force extérieure** qui ne lui offre que la fuite momentanée
hors d'un « monde mauvais » et un plaisir provisoire ; il ne lui reste alors que des désirs qui ne
lui viennent pas de ses rapports au monde mais de sa **constitution physique**, et qui ne se
manifestent que comme **réaction**.

**هوامش** : **aucun encadré de notes.**

**الكاتب** — ⚠️ **RENVOI**, imprimé verbatim :
> راجع التعريف بماركس وانغلز في السند عدد 18 ( الإنيّة والغيريّة )

**المهام (verbatim, 6 puces)** :
- أتبيّن التصوّر الذي ينقده الكاتب بشأن صلة الإنسان بأهوائه.
- أيّة وجاهة للموقف الأخلاقي الذي يقوم على منظور سلبي للأهواء؟
- أحدّد شروط الإشباع الحقيقي للأهواء حسب النص.
- " لن تغيّر أيّة موعظة أخلاقية من الحياة شيئا : " كيف أفهم هذا القول؟
- بأيّ معنى تكون الشروط المادية محددا لنوعية تلبية الرغبة؟
- كيف يمكن لفرد يعيش واقعا بائسا أن يحقق ضربا من المتعة؟

---

###### سند 11 — برغسون — « الحريّة الأخلاقيّة » — p.370

⚠️ **سند sur une seule page.** Ni encadré de notes, ni illustration finale, ni encadré de citation.

- **Auteur tel qu'imprimé** : **برغسون**. **Aucune ligne latine** pour ce سند.
- **Titre du سند** : **الحريّة الأخلاقيّة**
- **Source** (vérifiée par agrandissement) : برغسون، منبعا الأخلاق والدّين، ترجمة **عبد الدّايم** و
  سامي الدّروبي — دار الهيئة المصرية العامة للتأليف والنشر 1971. ص88

  ⚠️ Le traducteur est imprimé **« عبد الدّايم »** (avec yâ'). ⚠️ L'éditeur est imprimé
  **« دار الهيئة المصرية العامة للتأليف والنشر »** — avec un `دار` en tête devant `الهيئة`.
  **Signalé, non corrigé.**

- **Illustration** : portrait photographique de Bergson (vignette dans le texte).

**التمهيد (verbatim)** :
> إذا كانت الحرية شأنا إنسانيا ، بل ما به يكون الإنسان إنسانا، فإن تجربتها على صعيد واقع البشر
> المتسم بالتنوع والتعدد كثيرا ما يفضي إلى الاصطدام بمشكل العلاقة بين حرية الفرد وحرية الغير ؛
> مشكلا قد يكون حله إصلاح المجتمع أو بالأحرى إبداع " أخلاق الامتياز ".

**Thèse (reformulée)** : on dit d'ordinaire que l'individu a droit à la liberté qui **ne nuit pas**
à celle d'autrui ; mais autoriser une liberté nouvelle peut avoir pour effet que les libertés
**empiètent** les unes sur les autres dans la société actuelle, sans qu'il en aille de même dans une
autre société où cette réforme aurait changé les affects et les mœurs. Il est donc **impossible** de
juger a priori, et **quantitativement**, la mesure de liberté qu'on peut accorder à un individu sans
nuire à celle de ses semblables : dès que la quantité change, **la qualité** cesse d'être la même.
De plus, l'**égalité** ne s'obtient qu'aux dépens de la liberté, ce qui obligerait à trancher
laquelle des deux on préfère — question sans réponse générale, puisque sacrifier une liberté est
encore un fait de liberté dès lors que les citoyens y consentent, et que les libertés qui subsistent
après le sacrifice **valent davantage** si l'égalité obtenue a produit une société où l'on respire
mieux et où l'on travaille avec joie. Il faut donc revenir aux **créateurs de morale**
(`مبدعي الأخلاق`), qui pensent par la **pensée** un espace social nouveau, un milieu de vie
meilleur, tel qu'une société qui en aurait fait l'épreuve refuserait de revenir à son état
antérieur : par là seulement se définit le **progrès moral** — qu'on ne peut d'ailleurs reconnaître
qu'**après coup**, quand un sentiment moral neuf est apparu, comparable à une **musique** nouvelle
qui se transmet aux hommes et leur imprime sa marque.

**هوامش** : **aucun encadré de notes.**

**الكاتب** — ⚠️ **RENVOI**, imprimé verbatim :
> **برغسون** راجع التعريف ببرغسون في السند عدد 8 (الإنيّة والغيريّة )

**المهام (verbatim, 6 puces)** :
- أيّ تصوّر للحريّة يضعه النص موضع نقد؟
- بأيّ معنى تعسر المفاضلة بين الحرية والمساواة؟
- أبيّن كيف أن إصلاح المجتمع في اتجاه المساواة له أثر على منزلة الحرية.
- أحدّد مفهوم التقدّم الأخلاقي في النص. هل يحمل على معنى النسبيّة الأخلاقيّة؟
- ماذا يعني النص " بالرجال مبدعي الأخلاق "؟
- هل من تعارض بين أخلاق إبداع وفكرة التزام أخلاقي؟

---

###### سند 12 — أبيقور — « اللذة والسعادة » — p.371

⚠️ **سند sur une seule page.** Ni encadré de notes, ni illustration finale, ni encadré de citation.

- **Auteur tel qu'imprimé** : **أبيقور** ; ligne latine **`EPICURE`**.
- **Titre du سند** : **اللذة والسعادة**
- **Source** : أبيقور، مذهب وقواعد. —
  `EPICURE, Doctrine et maximes. Coll. L'esprit et la main. éd. Hermann, Paris,1965, pp. 77-78.`
- **Illustration** : buste antique en marbre (vignette dans le texte).

**التمهيد (verbatim)** :
> يسعى الإنسان بموجب طبيعته إلى طلب النفع وتجنب الضرر. وإذا كان فيما يحصل له من ضرر ألم، وبالتالي
> شر، فإن في نفعه لذة هي الخير الأسمى، يطلبها غاية لفعله ، كأنّما هي سعادته، وهو الكائن الذي لم
> يوجد ليشقى.

**Thèse (reformulée)** : le **plaisir** est le commencement et la fin de la vie heureuse ; nous
l'avons reconnu comme un bien **premier et conforme à notre nature**, et c'est de lui que nous
partons pour déterminer ce qu'il faut choisir et ce qu'il faut fuir — c'est à lui que nous revenons
quand nous prenons la **sensation** pour règle d'évaluation de tout bien. Mais précisément **parce
que** le plaisir est notre bien premier et naturel, nous **ne recherchons pas tout plaisir** : il
arrive que nous en écartions beaucoup, quand il en résulte pour nous des désagréments plus grands ;
et nous jugeons souvent des douleurs préférables à des plaisirs, lorsqu'un plaisir plus élevé suit
une longue souffrance endurée. Tout plaisir est donc, par sa nature propre, un **bien**, sans qu'il
faille pour autant rechercher tout plaisir ; de même toute douleur est un **mal**, sans qu'il faille
pour autant fuir toute douleur. Dans tous les cas la décision se prend par **comparaison** et par
**examen précis** de l'utile et du nuisible, car il nous arrive de traiter le bien comme s'il était
un mal, et le mal comme s'il était un bien.

**هوامش** : **aucun encadré de notes.**

**الكاتب** (**notice pleine**, verbatim) :
> **أبيقور** (341—271 ق.م) من أبرز الفلاسفة الذريين الإغريق. ظهر شغفه بالفلسفة مبكرا. يمكن اختزال
> حياته في مرحلتين: بدأ حوالي 310 ق.م التدريس وعرف صعوبات حملته على الخروج من أثينا إلى آسيا ليعرف
> نجاحا ويجمع حوله أتباعا جددا متميزين وذوي تأثير. وحوالي 306 ق.م استقر بأثينا و لم يفارقها حتى
> موته. وقد عُدَّ أحد روّاد ما يُسمّى بأخلاق اللّذة.

⚠️ **Ce سند est le seul du مبحث à donner une notice pleine pour un auteur déjà présenté ailleurs
dans le manuel** — Épicure avait déjà été défini dans le **هامش du سند 4** (p.358). Les deux
notices **ne donnent pas la même date de mort** (270 vs 271) : voir l'avertissement transversal
ci-dessus.

**المهام (verbatim, 6 puces)** :
- بأيّ معنى تكون اللّذة خيرا أساسيا وفطريا؟ هل يعني هذا اعتبارها مبدأ للفعل الأخلاقي؟
- أتمثّل حدود التمييز بين اللّذة والألم، وأفهم معنى أن يكون في الألم لذّة.
- أستخرج من النص المعيار الذي يقرّه الكاتب لتقدير الخير والشر. هل يستند هذا المعيار على العقل
  والإرادة أم على الأهواء؟
- على أي أساس يعتبر الكاتب اللّذة " مبدأ وغاية للحياة السعيدة "؟ أحدّد معنى اللّذة التي يعنيها النص.
- أحدّد معنى السعادة من خلال النص وطبيعة علاقتها بالخير.
- هل يحمل القول باللّذة مبدأ للفعل الأخلاقي على معنى الدعوة إلى الإفراط في طلبها؟

---

###### سند 13 — أرسطو — « الخير الأسمى » — p.372

⚠️ **سند sur une seule page.** Ni encadré de notes, ni illustration finale, ni encadré de citation.

- **Auteur tel qu'imprimé** : **أرسطو** ; ligne latine **`ARISTOTE`**.
- **Titre du سند** : **الخير الأسمى**
- **Source** : أرسطو؛ أخلاق نيقوماخوس — `ARISTOTE, Ethique à Nicomaque, VII, 13(2-5), éd. Vrin`

  ⚠️ **Le titre latin diffère de celui du سند 1** : ici **`Ethique à Nicomaque`**, là-bas
  **`Ethique de Nicomaque`** (p.353). Deux formes pour le même ouvrage dans le même مبحث.

- **Illustration** : dessin au trait d'un buste barbu d'Aristote (différent de la vignette du سند 1).

**التمهيد (verbatim)** :
> يبدو أن السعادة قيمة وغاية قصوى يسعى الإنسان إلى تحقيقها، وإذا كان الجميع يشترك في طلبها فإن
> تحديدها وبيان السبل إلى تحقيقها يمثل معضلة شغلت ولا تزال تشغل الفكر الإنساني.

**Thèse (reformulée)** : rien n'empêche que le **bien suprême** soit un certain **plaisir**, même en
admettant que certains plaisirs soient mauvais — de même que le savoir suprême peut porter sur un
objet déterminé alors que certaines sciences sont mauvaises. Puisque chaque disposition a une
activité qui lui convient et qui s'exerce sans obstacle, le bien suprême est nécessairement une
**activité** — celle de l'ensemble de nos dispositions ou celle de l'une d'elles, exercée
**sans entrave** ; et cette activité est un **plaisir**. Aussi la plupart des hommes ont-ils raison
de tenir que la **vie heureuse est une vie de jouissance** et d'établir un lien étroit entre plaisir
et bonheur, car aucune activité n'est achevée si elle est empêchée. Mais le bonheur relève des
activités **complètes**, et l'homme heureux a de surcroît besoin des **biens du corps**, des **biens
extérieurs** et de la **fortune** (`الحظ`), afin que rien ne fasse obstacle de ce côté-là. Contre
ceux qui prétendent qu'on est heureux même sous la torture ou dans les pires malheurs pourvu qu'on
soit bon — thèse que Aristote juge dite « sans intention ou sans intention réfléchie », donc vide de
sens —, il faut admettre qu'on a **besoin de la fortune**, tout en se gardant de la confondre avec
le bonheur : ce sont deux choses **profondément différentes**, la fortune, dès qu'elle excède ses
bornes, faisant même **obstacle** à l'activité. Le plus juste est donc de la nommer **حظّا ملائما**,
dont la définition se dessine à partir de son rapport au bonheur.

**هوامش** : **aucun encadré de notes.**

**الكاتب** — ⚠️ **RENVOI**, imprimé verbatim (identique à celui du سند 1) :
> **أرسطو** : راجع التعريف بأرسطو في السند عدد 16 ( الدولة: السيادة والمواطنة )

**المهام (verbatim, 6 puces)** :
- بأيّ معنى يكون الخير الأسمى لذّة؟
- كيف أفهم قول الكاتب بأنّ " الحياة السّعيدة هي حياة ممتعة "؟
- هل السّعادة شأن العقل أم الرغبة؟ النفس أم الجسد؟
- أيّة صلة بين السّعادة والحظ؟ بأيّ معنى يكون الحظ الملائم شرطا وعائقا؟
- أستخلص قيمة فكرة القدر في تصوّر أرسطو للسعادة، وشروط إمكان تحقّقها؟
- هل في القول بوجود موانع ما يفضي إلى التشكيك في إمكان تحصيلها؟

---

###### سند 14 — ج. ج. روسّو — « سبيل السعادة » — p.373

⚠️ **سند sur une seule page.** Ni encadré de notes, ni illustration finale, ni encadré de citation.

- **Auteur tel qu'imprimé** : **ج. ج. روسّو** ; ligne latine **`J-J.ROUSSEAU`**.
- **Titre du سند** : **سبيل السعادة**
- **Source** : ج. ج. روسّو؛ إميل أو في التربيّة، ترجمة عادل زعيتر، دار المعارف بمصر 1956. ص 109 — 110
  — `J-J.ROUSSEAU; Emile ou de l'éducation, GF, 1966, p 93`

  ⚠️ Les deux lignes de source ne renvoient pas à la même édition ni à la même pagination
  (ص 109—110 de la traduction arabe / p 93 de l'édition GF). **Constaté.**

- **Illustration** : portrait peint de Rousseau (vignette dans le texte).

**التمهيد (verbatim)** :
> يسعى الإنسان إلى السعادة قدر مستطاعه ووفق طاقاته، بيد أنّه كثيرا ما يصطدم، في واقعه الاجتماعي،
> بعوائق تحوّل مسعاه إلى صراع مرير يخلّف، غالبا، آلاما تتفاوت حدّتها بين البشر، إلى حدّ قد نحمل
> فيه على اليأس من إدراك سعادة تامّة خاليّة من الألم، فيكون مبلغ سعادتنا، أن نخفّف من الألم،
> كلّما، وجدنا إلى ذلك سبيلا.

**Thèse (reformulée)** : nous ne connaissons **ni bonheur absolu ni malheur absolu** ; tout est
mêlé en cette vie, on n'y goûte aucun sentiment pur, on n'y demeure pas deux instants dans le même
état, les affections de l'âme ont leurs variations comme le corps ses transformations. Le bien et le
mal nous sont **communs à tous**, mais en **proportions différentes** : le plus heureux est celui
qui souffre le **moins** de peines, le plus malheureux celui qui éprouve le **moins** de joies. Le
bonheur de l'homme ici-bas n'est donc **jamais qu'un état négatif** : il doit se mesurer à la
**moindre quantité de maux** qu'il endure. Tout sentiment de manque dont on ne peut se défaire est
douleur, tout désir suppose une privation, et l'on ne peut être privé sans souffrir : notre misère
tient donc à l'**écart entre nos désirs et nos facultés**, et l'être dont les désirs et les
facultés **s'égalent** est absolument heureux. La sagesse — le chemin du bonheur véritable —
ne consiste **ni** à diminuer nos désirs (car s'ils tombaient au-dessous de notre pouvoir une part
de nos forces resterait inemployée et nous ne jouirions pas de tout notre être), **ni** à étendre
nos facultés (car nos désirs croîtraient d'autant plus, nous rendant plus malheureux) : elle
consiste à **réduire l'écart** entre désirs et puissances, à rendre **égales** la puissance et la
volonté. Alors seulement toutes les forces sont en acte, l'âme reste en paix et l'homme se trouve
dans son meilleur état.

**هوامش** : **aucun encadré de notes.**

**الكاتب** — ⚠️ **RENVOI**, imprimé verbatim :
> **ج. ج. روسّو** : راجع التعريف بروسّو في السند عدد 6 ( الإنيّة والغيريّة )

**المهام (verbatim, 6 puces)** :
- أحدّد من خلال النص ما يعيق تحقيق السّعادة.
- كيف أفهم قول الكاتب " لا تكون سعادة الإنسان في هذه الدنيا، إذن، غير حالة سلبيّة " ؟
- يتحدّث الكاتب عن تقدير للسعادة، وفق أي معيارٍ يجري هذا التقدير؟
- ما شروط تحصيل السعادة حسب روسّو؟
- أفهم معنى " تقليل الفرق بين الرغبات والطاقات " شرطا للسعادة؟
- إذا كان الألم يملأ حياتنا فهل يؤدّي ذلك إلى اليأس من السعادة؟

---

###### سند 15 — دوأولباخ / بارون دو أولباخ — « في مدح التقدم و الرفاه » — p.374-375

- **Auteur tel qu'imprimé** : ⚠️ **trois formes dans le même سند** — la ligne d'attribution (p.374)
  et l'encadré final (p.375) impriment **« دوأولباخ »** en **un seul mot** (vérifié par
  agrandissement) ; la notice (p.375) est titrée **« بارون دو أولباخ »** en trois mots.
  Ligne latine de source : **`Baron d'HOLBACH`** ; ⚠️ la parenthèse latine de la notice imprime
  **`HOLBACH (Paul-Henri DIETRICH, Boron d')`** — **`Boron`**, non *Baron*. **Non corrigé.**
- **Titre du سند** : **في مدح التقدم و الرفاه**
- **Source** : دوأولباخ، نسق الطبيعة، الجزء الأول، الفصل 16. —
  `Baron d'HOLBACH; Le système de la Nature, P I, chap. XVI`
- **Illustrations** : (p.374) portrait gravé de d'Holbach ; (p.375) photomontage — un homme en
  costume clair, bras écartés, **flottant en apesanteur** devant la Terre vue de l'espace.

**التمهيد (verbatim)** :
> إذا كان غنيّا عن البيان التأكيد على ما بذله الإنسان من جهود في اتجاه تحصيل المعارف والعلوم بما
> ينزّله منزلة السّيادة على الطبيعة والعالم، فإنّه لا يمكننا أن ننكر أن هذا السعي الدائم للمعرفة
> يوجّهه مطلب أساسي من داخل الذّات هو إدراك الرفاه سبيلا للسعادة.

**Thèse (reformulée)** : l'homme a commencé par manger les fruits du chêne en disputant les glands
aux bêtes, et il a fini par mesurer le mouvement des astres ; il a inventé le labour, la semaille,
la géométrie ; il s'est couvert de peaux, et en quelques siècles s'est vêtu d'or et de soie ; il
habitait grottes et troncs d'arbres, il est devenu ingénieur et bâtisseur de palais. Son activité
industrieuse croît à mesure que ses **besoins se multiplient** : il est contraint de mettre sa
raison au travail, et l'enchaînement des connaissances le conduit à la **découverte graduelle** de
toutes les sciences et de tous les arts. Ainsi les savoirs qui ne répondaient pas à un besoin sont
devenus nécessaires pour satisfaire une **curiosité née** de ce que rien ne peut rassasier l'homme
tout entier. À toutes les étapes de ce parcours, l'homme est **poussé par sa nature** à améliorer
sans cesse son sort et à accroître son **رفاه**. À ceux qui prétendent que le **sauvage** serait
plus heureux que l'homme **civilisé**, il faut demander : **où serait donc son bonheur ?** Le
sauvage est un enfant robuste mais privé de ressources, d'expérience, de raison et d'industrie ;
il souffre en permanence de la faim et de la misère, il se trouve à chaque instant contraint de
lutter contre les bêtes, il ne connaît d'autre loi que ses désirs, d'autres règles que ses
impulsions du moment, d'autre droit que la force, d'autre vertu que la témérité — c'est un être
impulsif, cruel, brutal, sans frein ni horizon, exposé à chaque instant à devenir victime de sa
propre folie ou de la férocité de ses semblables. La notion de **vie sauvage**, ou d'**état de
nature** vers lequel des rêveurs mélancoliques ont voulu ramener l'humanité et que les poètes ont
chanté comme un **âge d'or**, n'est en vérité que le nom d'états de misère, de sottise et de folie.
Nous ramener à ce stade, ce serait un **retour à l'enfance**, l'oubli de tout savoir et l'abandon
de toutes les lumières que notre raison a su acquérir — et cela alors même que, hélas, notre raison
ne s'est que **fort peu** développée, même chez les nations les plus civilisées.

**هوامش** : **aucun encadré de notes.**

**الكاتب** (p.375 — **notice pleine**, verbatim) :
> **بارون دو أولباخ** : (1789-1723) — `HOLBACH (Paul-Henri DIETRICH, Boron d')` هو فيلسوف فرنسي
> من أصل ألماني موسوعي ومادي النّزعة، كان صديقا لديدرو `Diderot`. ألّف كتاب " نظام الطبيعة "
> وترجم آثار علميّة وفلسفيّة من اللاتينيّة والألمانيّة وغيرها. وهو أيضا جيولوجي وكيميائي. كان
> يلتقي في صالونه الخاص بأبرز وجوه الفلسفة في عصره. مكّنته ثروته الكبيرة من الانصراف إلى التأليف
> فساهم بـ 375 مقالا في موسوعة **ديدرو** (1751) وقد ترك إضافة إلى ذلك مراسلات عديدة في العلم
> والفلسفة..

⚠️ La notice arabe donne le titre du livre **« نظام الطبيعة »** alors que la ligne de source
(p.374) donne **« نسق الطبيعة »** — deux traductions différentes du même titre dans le même سند.

**المهام** (p.375 — verbatim, 5 puces) :
- أتبيّن نمط عيش الإنسان البدائي، ثم أستخلص ما كان يعوزه للسير على درب التطور.
- أكشف عن مكانة العقل والذكاء في الرفع من مستوى العيش.
- أحدّد مميزات الحياة المتحضرة وأقارنها بمفهوم الحياة المتوحشة.
- أي معنى يعطيه الكاتب للرفاه؟
- الرفاه مولّد للسّعادة: أمتحن هذا التشريط في ضوء الحياة الراهنة.

**Encadré de citation final** (p.375, verbatim) :
> " ففي كل المراحل المتطورة والمتباعدة بعضها عن بعض يكون الإنسان مُوجّها بطبيعته، تحثّه باستمرار
> على تحسين مصيره وجعله أكثر رفاه ".
> — **دوأولباخ**

###### سند 16 — حدود السعادة — p.376-377

- **Auteur tel qu'imprimé** : **سغموند فرويد** ; ligne latine **`Sigmund FREUD`**.
- **Titre du سند** : **حدود السعادة**

**التمهيد** (verbatim) :

> إننا لا نفعل غير التذكير بشائع الآراء عند القول: إنّ الناس، كل الناس، يرغبون في السعادة، لكننا
> أيضا قد لا نفعل غير تذكيرهم بواقع الحياة، عند التأكيد على ما يصادفونه من عوائق تنغص عليهم، فإذا
> هم في التعاسة أو يشارفون، بحيث لا مناص لهم إلاّ الطمع في التردد بين هذه وتلك، وضع تقاوم فيه
> الذات متى تألمت، وآخر تسعد فيه متى استمتعت.

**Référence imprimée** : سغموند فرويد، قلق في الحضارة —
`Sigmund FREUD, Malaise dans la civilisation, 1929, Puf.1971.`

**Thèse (reformulée)** : ce que les hommes demandent à la vie, c'est **le bonheur** — et ce but a
deux versants, l'un **négatif** (éviter la douleur et le déplaisir), l'autre **positif** (éprouver
des jouissances intenses) ; au sens étroit, « bonheur » ne désigne que le second. Or ce programme
est **irréalisable** : rien dans l'ordre du monde ne prévoit que l'homme soit « heureux ». Le
plaisir naît d'une satisfaction **brusque** d'un besoin accumulé, donc par nature **épisodique** ;
sa continuation ne donne qu'un contentement tiède. Nos possibilités de bonheur sont **limitées par
notre constitution même**. Le malheur, lui, est bien plus facile à éprouver : il nous menace de
**trois côtés** — notre **corps**, voué au déclin, qui ne peut se passer de la douleur et de
l'angoisse ; le **monde extérieur**, force implacable et destructrice ; et surtout nos **relations
aux autres hommes** — cette dernière souffrance étant peut-être ressentie comme la plus cruelle,
bien qu'on tende à la considérer comme secondaire.

**Pas d'encadré الهامش sur ce سند** (constaté).

**الكاتب** — ⚠️ **RENVOI, pas une notice** : le manuel imprime
« **سغموند فرويد : راجع التعريف بفرويد في السند عدد 24 (الإنيّة والغيرية)** ».

> ✅ **Renvoi résolu.** La notice cible est transcrite dans cette même fiche, au
> **مبحث 1.1, سند 24 (p.64)** : `فرويد: ( 1856 – 1939 )`, طبيب نفسي نمساوي ومؤسس التحليل النفسي.
> ⚠️ Le manuel **n'imprime jamais le prénom en arabe** dans la notice elle-même (`فرويد` seul) ;
> c'est **ce renvoi-ci** qui écrit `سغموند فرويد`. Divergence imprimée, à ne pas lisser.

**المهامّ** (verbatim) :

- أحدّد جواب الكاتب عن السؤال الذي طرحه في بداية النص.
- يتحدث الكاتب عن أهداف لطموح الإنسان ينم عنها بسلوكه. أكشفها وأتبين هل من فارق بينها؟
- يربط الكاتب السّعادة باللّذة، أتبيّن في ضوء هذا الاقتران العوائق التي تحول دون سعادة الإنسان.
- يعتبر الكاتب " أنّ ملكات سعادتنا محدودة أساسا بتكويننا "، أكشف عن أسباب هذه المحدودية باستثمار مكتسباتي من التحليل النفسي.
- " إنّه أيسر علينا بكثير أن نحيا تجربة التعاسة "، أحدد دلالة هذا القول وأتبيّن علاقة السّعادة بالألم.
- أرصد مبررات اعتبار الحضارة عائقا أمام تحقيق السّعادة. هل في هذا القول ما يفيد اليأس من السعادة؟

**Encadré-citation (p.377)** : « لم يدخل في خطة " الخلق " البتة أن يكون الإنسان سعيدا » — **فرويد**.

**Illustrations** : p.376 — portrait photographique de Freud. p.377 — photographie en couleurs
saturées d'un homme la main sur le visage, l'air accablé.

###### سند 17 — في السعادة الجديدة — p.378-379

- **Auteur tel qu'imprimé** : **جان بودريار** ; ligne latine **`Jean BEAUDRILLARD`** ([sic],
  l'usage étant *BAUDRILLARD*).
- **Titre du سند** : **في السعادة الجديدة**

**التمهيد** (verbatim) :

> كثيرا ما تعرف الحضارة المعاصرة بما هي حضارة الوفرة والرفاه، لكل فيها حظ، لكأنّ الإنسان المعاصر
> حقق ما سعى إليه الأوائل وعجزوا عن تحقيقه، وكأنّ ما كان يعدّ مثلا أعلى غدا واقعا متعيّنا، ذاك ما
> تظهره صورة المجتمع المعاصر، صورة سرعان ما تتهاوى، حين نتجاوز السطح، لتنكشف صورة قاتمة تبدو من
> خلالها الحقائق أوهاما، والانتصارات انكسارات.

**Référence imprimée** : جان بودريار، المجتمع الاستهلاكي —
`Jean BEAUDRILLARD, la société de consommation (1970), Gallimard, coll, Idees 1976; pp 59-61`
*(graphie « BEAUDRILLARD » telle qu'imprimée — [sic], l'usage étant « BAUDRILLARD ».)*

**Thèse (reformulée)** : la charge idéologique du mot « bonheur » ne vient pas d'un penchant
naturel de chacun à le rechercher, mais du fait que, **sur le plan socio-historique**, le mythe du
bonheur **recueille et incarne le mythe de l'Égalité** dans les sociétés modernes — toute la fièvre
politique et sociale depuis la révolution industrielle a été convertie en bonheur. D'où une
exigence redoutable : pour porter le mythe de l'égalité, **le bonheur doit être mesurable** — un
bien-être mesurable par des objets et des signes. Le bonheur **intérieur**, celui qui n'a pas
besoin de preuves visibles, est donc d'emblée **exclu** de l'idéal consumériste ; il faut qu'il
« se signifie » selon des critères visibles. De même il est écarté de toute fête ou ferveur
collective, car il s'adosse aux principes individualistes de la Déclaration des droits de l'homme,
qui reconnaît explicitement le droit de **chacun** au bonheur. La « révolution du bien-être » est
l'héritière de la révolution bourgeoise : ayant posé le principe d'égalité sans pouvoir le
réaliser, elle a converti le principe **démocratique** — égalité réelle, capacités,
responsabilités, chances sociales — en **égalité devant l'objet**. C'est une démocratie de la
télévision, de la voiture et de la chaîne stéréo : démocratie apparente et **formelle**, qui masque
l'absence de la démocratie réelle et de l'égalité perdue.

**الهامشان** (verbatim) :

> 1 — **توكفيل** : `Alexis de Tocqueville(1853-1805)` فيلسوف فرنسي، عرف بدفاعه عن الفكر
> الأرستقراطي، وبتأثره بالتجربة الديمقراطية الأمريكية، وبتأكيده على قيم الفردانية التي يميزها عن
> الأنانية.
> 2 — **لائحة حقوق الإنسان** : جملة المبادئ التي أقرها المجلس التأسيسي لسنة 1789 بفرنسا (أنظر نص
> ماركس الوارد في مسألة الدولة: السيادة والمواطنة)

> ⚠️ Le هامش 2 **renvoie au مبحث 3.1**, سند 15 (ماركس, p.305) — renvoi inter-chapitres imprimé,
> celui-ci résoluble puisque le chapitre est transcrit.
> ⚠️ Les dates de Tocqueville sont imprimées **`(1853-1805)`** — sans espace après le nom latin,
> et **mort avant naissance**, comme tous les intervalles de ce مبحث (voir § Avertissement
> transversal). Deux choses distinctes s'y superposent : l'**ordre** des bornes, qui n'est
> qu'une convention de composition, et la borne elle-même — **le manuel donne 1853**, là où
> l'usage donne **1859**. Valeur à retenir : 1805 — 1853, telle que le manuel la fixe. À ne pas
> « corriger » en génération, et à ne pas transformer en question.

**الكاتب** — ⚠️ **RENVOI** : « **جان بودريار: راجع التعريف ببودريار في السند عدد 22 (الإنيّة
والغيريّة)** »

> ✅ **Renvoi résolu.** La notice cible est transcrite dans cette même fiche, au
> **مبحث 1.1, سند 22 (p.60)** : `جون بودريار: (1929 – 2007 )`, عالم اجتماع فرنسي.
> ⚠️ **Le prénom diverge d'un مبحث à l'autre** : ce renvoi imprime `جان`, la notice p.60 imprime
> `جون`. Les deux sont imprimés ; ni l'un ni l'autre ne doit être « corrigé » en génération, et la
> graphie du nom ne doit pas devenir une question.

**المهامّ** (verbatim) :

- أتبيّن الدلالة الإيديولوجية للسّعادة في المجتمع المعاصر.
- أي تحديد للسّعادة يتمّ إقصاؤه في حضارة الاستهلاك؟
- هل يمكن اختزال السّعادة في ما تروّجه الحضارة المعاصرة من علامات؟
- هل تؤمّن الحضارة المعاصرة حقّ الإنسان في السّعادة؟
- أتبيّن العلاقة بين صورة السّعادة والديمقراطية الغائبة والمساواة المفقودة؟
- أستخلص قيمة السّعادة اليوم وسبيل تحقيقها. أحرر فقرة في الغرض.

**Encadré-citation (p.379)** : « لكي تكون حاملة أسطورة المساواة، يجب أن تكون السّعادة قابلة للقيس.
ويجب أن تكون رغد عيش قابلا للقيس بواسطة أشياء وعلامات، ورفاها » — **بودريار**.

**Illustrations** : p.378 — portrait photographique de Baudrillard. p.379 — photographie d'un homme
avachi dans un fauteuil devant un téléviseur, d'où jaillit une gerbe de friandises et d'emballages.

###### سند 18 — الحريّة السعيدة — p.380-381

**التمهيد** (verbatim) :

> اعتاد الناس على طلب الخير نشدانا للسعادة لكأنها لا تفهم إلا في سياق هذا الاقتران، أمر قد لا
> يحافظ على بداهته حالما نفكر في وضع للإنسان يكون فيه فاقدا لحريته، مما قد يبرر مساءلة السعادة من
> جهة علاقتها بالحرية.

- **Auteur tel qu'imprimé** : **روبير مسراهي** (ligne de source) / **روبار مسراهي** (notice) ;
  ligne latine **`Robert Misrahi`**. Voir la note sur les **quatre** graphies, plus bas.
- **Titre du سند** : **الحريّة السعيدة**

**Référence imprimée** : روبير مسراهي؛ مقالة في السعادة، 2: الإيتيقا والسياسة والسعادة —
`Robert Misrahi, Traité du bonheur, II Ethique, politique et bonheur, éd. seuil, Paris p-281-282`

**Thèse (reformulée)** : une société du **bonheur libre** ne décrète pas de façon autoritaire et
sélective l'encouragement d'une culture positive ; elle **décide librement**, selon une logique
interne, de se constituer comme société de **liberté et de joie**. Elle exprime alors par sa culture
un désir de joie, la découverte des voies qui peuvent y mener, et les visages que prend le bien
dans chaque circonstance — car la culture est, pour nous, l'expression du désir le plus profond.
Une culture **fataliste et tragique** traduit un désir de mort ; une société **libérée** traduira
sa lutte contre la mort, la guerre et la servitude, et cherchera en même temps sa liberté agissante
et sa capacité de construire — toujours sous des formes multiples, imprévues, plus riches dans le
réel effectif que dans le discours. Ce **glorieux absolu**, l'auteur l'appelle aussi la **vie vraie**.

**Pas d'encadré الهامش sur ce سند** (constaté).

**الكاتب** (notice, verbatim resserré) : **روبار مسراهي (1926)** — فيلسوف فرنسي من أصل تركي تحصّل
على شهادة التبريز بعد أن تابع دروس « **جانكليفيتش** » و« **بشلار** » و« **مرلوبونتي** ». درّس طيلة
ثلاثين سنة في جامعة باريس الأولى وتميّز بنزعة لائكية وبدفاعه على الحرية كما عرف بكتاباته حول
سبينوزا وخاصة علم الأخلاق (1990). ومن بين أهم مؤلّفاته « **مقالة في السعادة** » (1981-1983) وقد
صدر في جزئين قدّم فيهما نظريّة تؤسس لإيتيقا الحرية السعيدة في علاقة بالإنسان بما هو حرية ورغبة،
كما ألّف « **الوجود والديمقراطية** » (1995) والذي نقد فيه بشكل جذري التصورات التقليدية حول الفرد
والسياسة.

> ⚠️ Graphie du nom **flottante dans le même chapitre — quatre formes** : « **مسراهي** » au titre
> du سند et à la citation (p.381), « **روبار مسراهي** » à la notice (p.380), « **روبير مسراهي** »
> à la référence bibliographique (p.380), et — en amont — « **روبار ميسراهي** » à la notice de la
> 2ᵉ وضعيّة استكشافيّة (**p.350**), où la ligne de source imprime pourtant « روبار مسراهي ».
> Le فهرس annonce « مسراهي ».
> ⚠️ **مسراهي apparaît deux fois dans le chapitre** : il est aussi la 2ᵉ وضعيّة استكشافيّة (p.350).
> Le manuel **ne relie pas explicitement** les deux textes.
> ⚠️ **بشلار** est ici orthographié ainsi (et non « باشلار ») — cohérent avec la p.257 du مبحث 2,
> divergent de la graphie retenue par le cours du chapitre 03. À trancher au moment de générer.

**المهامّ** (verbatim) :

- أحدد دلالة الثقافة وأشكالها حسب الكاتب.
- وفق أي منطق يقرر المجتمع إنشاء ثقافة السّعادة؟
- بأي معنى نفهم أن الظرف محدد للخير؟
- ما هي أشكال تعبير المجتمع المتحرر عن ثقافة السعادة؟
- أي معنى أعطيه للحياة الحقيقية؟

**Encadré-citation (p.381)** : « إنّ المجتمع سيقرّر أن يتشكل بما هو مجتمع حرية وفرح، يقرر بحرية وفق
منطق داخلي؛ فيعبر من خلال ثقافته عن رغبة في الفرح » — **مسراهي**.

**Illustrations** : p.380 — portrait photographique de Misrahi. p.381 — photographie d'une femme
en robe blanche bondissant sur une plage.

> ✅ **Fin de la نافذة سندات du مبحث 3.2** : 18 سندات, p.352-381.
> ⚠️ **Deux des trois derniers سندات (16 et 17) ont pour notice un RENVOI au مبحث 1.1**
> (سند 16 → سند 24 ; سند 17 → سند 22), chapitre **non transcrit** : ces deux renvois resteront
> irrésolus jusque-là. Sur l'ensemble du مبحث, **13 des 18 سندات renvoient** (1, 3, 4, 5, 7, 8, 9,
> 10, 11, 13, 14, 16, 17) et **5 seulement portent une notice pleine** (2, 6, 12, 15, 18).

##### 3.2.3 نافذة دعائم للتفكير في المسألة — p.382-396

> ⚠️ **La plage p.382-396 est celle du فهرس, pas celle des pages.** La نافذة دعائم proprement dite
> couvre **p.382-392** ; **كيفيات التفكير (p.393-396) est traitée par le manuel comme une نافذة
> autonome**, avec son propre bandeau de titre dans le gabarit des autres نوافذ, et le sommaire de
> la p.382 n'annonce que **deux** entrées. Le `3.2.3.3` est une **classification du sommaire
> (فهرس, p.408), pas une donnée de la page** — voir le § *Écart فهرس / pages imprimées* en fin de
> tranche.

> **Pages lues** : p.382–396 (intégral). **Source** : manuel élève `210402` (CNP,
> `210402P00.pdf`), مبحث 3.2 « الأخلاق : الخير والسّعادة ». Images de travail : rendu 150 dpi,
> passages douteux revérifiés à 300 dpi.

**p.382 — page d'ouverture de la نافذة.** Titre imprimé sur deux lignes :
**نافذة دعائم** / **للتفكير في المسألة**. Image : une pile de livres à couverture orange vif,
une paire de lunettes rondes posée dessus, sur un fond de feuillage. Encadré-citation
(verbatim) :

> « وفيما نحن نسأل : **القيم إلى أين ؟** لا يمكننا أن نتجاهل السّؤال الآخر : ماالذي سنصنعه نحن
> بالقيم ؟ إنّ **التهيّؤ للمستقبل يتطلّب بلورة أخلاقيّات من أجل المستقبل**، أخلاقيّات
> للزمن… إنّها **الأخلاقيّات هنا والآن**، لكي يبقى هناك فيما بعد هنا والآن. »
> — ▲ **جييروم بندي**, *القيم إلى أين؟*

Sommaire imprimé en bas de page — **deux entrées numérotées seulement** :
**1 — تحديدات وتمييزات مفهوميّة** · **2 — سياقات فكريّة**.

⚠️ **Écart avec le فهرس (à retenir)** : le sommaire de la page d'ouverture **n'annonce pas** de
troisième entrée « كيفيّات التفكير ». Voir le § *Écart فهرس / pages imprimées* en fin de tranche.

---

###### 3.2.3.1 تحديدات وتمييزات مفهوميّة — p.383-388

Deux concepts sont définis : **الآداب** (p.383-384) et **الإيتيقا** (p.385-388). Bandeau de tête
imprimé en haut de chaque page : **نافذة دعائم للتفكير في المسألة**, puis le sous-titre en
encadré crème **: تحديدات و تمييزات مفهوميّة**.

⚠️ **Le gabarit n'est PAS celui du مبحث 2.** Ici il n'y a que **deux** entrées, pas trois :
**■ لغة** puis **■ فلسفيا** — **il n'y a aucune rubrique « اصطلاحا »** (alors que الواقع et
البراديغم, p.252-255, en avaient une). La rubrique **« ■ قيل في … »** existe bien, en revanche,
et clôt chacun des deux concepts. Le titre de chaque concept est imprimé dans un cartouche rouge
avec, à côté, un cartouche bleu portant l'équivalent latin : **1– الآداب** `Mœurs` ·
**2– الإيتيقا** `Éthique`.

**1 — الآداب · `Mœurs` — p.383-384**

**■ لغة (verbatim, intégral)** :

> **الآداب** جمع **أدب** من **أدب يأدب** وتعني **حسن التربيّة والأخلاق**. ويُستعمل اللفظ
> للدلالة على **معان عدّة** ؛ فيُقال **أدب الكلام**، و**أدب الطّعام**، ويُقصد به **ما يُستحسن
> في طريقة الكلام والطّعام**…

**■ فلسفيا (verbatim, intégral — c'est la définition officielle du concept)** :

> تُطلق عبارة **الآداب** للدلالة على « **الآداب العامّة** » وتدلّ (`Moeurs`) في اللسان الفرنسي
> على **طريقة في الوجود والفعل والإحساس والتفكير**. وهي، من منظور أخلاقي صرف، **طريقة في
> التصرّف وفق ضوابط أخلاقيّة مسلّم بها في وسط اجتماعي معيّن**، وتكون « **آدابا حسنة** » و
> « **آداب سيّئة** » ؛. وتمثّل الآداب، حين تتصل **بشعب أو بفرد**، **خاصيّة مميّزة له**.

Suite de l'entrée (p.383, colonne de droite puis colonne de gauche) — les **quatre thèses** que
le manuel tire de cette définition :

1. **La non-homogénéité des mœurs (لا تجانس الآداب)** — « يؤكّد هذا التحديد الأوّل على **لا
   تجانس الآداب** ». Exemples imprimés : **تاسيت** `Tacite` parle des « **آداب الجرمانيين** »,
   **لابروويار** `La Bruyère` des « **طبائع أو آداب هذا القرن** » ; et le contraste
   ethnographique : nous sourions pour exprimer notre joie d'accueillir un visiteur, alors que
   les **التيبيينبا** `Tupinamba` (« سكّان "تيبي" بالبرازيل ») l'expriment **بالبكاء**.
2. **Deux relativismes en chaîne** :
   - **نسبيّة اتنوغرافيّة، نوعا ما ريبيّة** — les voyageurs (الرحّالة) puis les
     **الإتنولوجيون** y ont conclu en mesurant l'écart des mœurs entre les nations. Formule
     de **باسكال** `Pascal` citée verbatim par le manuel :
     > « **حقيقة من ناحية البيريني، خطأ من ورائه** »
   - **نسبيّة تاريخية أو بالأحرى تاريخانيّة** — « **فآداب معاصرينا ليست آداب أجدادنا** » ; chez
     les **اللاتينيين**, ce qui passe aujourd'hui pour un **انحلال أخلاقي** est mis en regard
     des **آداب الأجداد**.
   - **À l'inverse, dans une perspective évolutionniste** (« ومن منظور تطوّري ( هيمن طويلا
     بموجب ارتباطه **بفكرة التّقدّم** ) ») : les mœurs des **الشّعوب المتحضّرة** sont **أكثر
     رقّة وأكثر « إنسانيّة » من آداب الأوّلين البربريّة** — exemples imprimés : la
     **monogamie (الزّواج الأحاديّ)** comme progrès par rapport à la **polygamie (تعدّد
     الزّوجات)** ; la **soumission et la dépendance (الخنوع والتبعيّة)** qui caractérisaient le
     rapport du **الإقطاعي** à ses **فلاّحين**, rangées parmi les **الآداب السّخيفة** que
     l'homme contemporain a dépassées avec les **أفكار مسبّقة** qui les fondaient.
3. **الآداب ≠ الأخلاق de la philosophie ancienne** — « وتجدر الملاحظة أنّ **الآداب** حينما تكون
   **ممارسة عارضة خاصّة وظرفيّة**، فإنّها **لا تملك أيّة خاصيّة ممّا تسنده الفلسفة القديمة
   للأخلاق** ». Illustration explicite : **فلا علاقة للآداب مثلا بـ« الأمر القطعي » عند كانط**.
4. **La distinction de ليفي بريل — le couple structurant de la page (verbatim)** :

   > وعلى أساس هذه الملاحظة أقام **ليفي بريل** `Lévy - Bruhl` **تقابلا جوهريّا** بين
   > « **المابعد أخلاق** » (`Métamorales`) أو « **الأخلاق النظريّة** » التي تبحث عن « **تأسيس**
   > » قواعد السّلوك على **مبادئ عامّة ما قبليّة وصوريّة**، وبين « **علم الآداب** » الذي يُعنى
   > **بالشروط الموضوعيّة العينيّة للتجربة الأخلاقيّة**، أو هو **الدراسة الاجتماعيّة والوضعيّة
   > للآداب** من حيث هي **آداب أخلاقيّة تنظّم مجتمعا معيّنا**.

   ⇒ **المابعد أخلاق / الأخلاق النظريّة** (fondation *a priori*, formelle, universelle) **≠**
   **علم الآداب** (étude sociale et positive des conditions objectives et concrètes).

5. **La lecture classique — les mœurs comme « règles de vie » (p.383-384)** : à cette
   signification des mœurs *comme principes moraux* s'en ajoute une autre, élaborée par les
   **الفلاسفة الكلاسيكيون** — **أفلاطون**, **منتسكيو**, **هيغل** : les mœurs ne sont pas
   **مجموعا شاذّا غريبا من الممارسات الاعتباطيّة**, elles sont l'ensemble des
   « **قواعد حياة** » qui aident l'individu à maintenir **تفاوتا مناسبا بين مختلف نشاطاته**,
   l'empêchent de **الاستسلام للأهواء** ou de **يتيه في حريّة موهومة**, et assurent en même
   temps **الأمن والانسجام بين الأفراد والجماعات التي تكوّن المجتمع**. D'où l'interdit de
   lecture posé par le manuel : **« فيجب ألاّ ننظر إلى الآداب بصفتها مجموع غير منسجم من العادات
   الغريبة. إنّها تمثّل شروط الحياة الفاضلة »**.

**La distinction décisive de la page — الفضيلة ≠ الآداب (p.384, verbatim)** :

> غير أنّه **يجب أن نميّز الفضيلة عن الآداب**، رغم أنّنا **نحكم على الآداب في علاقتها
> بالفضيلة**. إذ **يمكن للآداب أن تكون سيّئة** حينما **لا تقوم على قصد سليم** أو كانت **لغاية
> السيطرة والتملّك**، فهي بهذا **تتعارض مع الفضيلة**، **والآداب الحسنة لا تتطابق مع الفضيلة**،
> فهي **تقتصر على تطابق بين تصرّف ونموذج ما**، أمّا **الفضيلة فليست مجرّد استعداد للقيام
> بأفعال**، إنّما **تقوم على الذّكاء والدقّة أي القدرة على الاختيار**.

⇒ Le manuel rattache aussitôt cette conception : **« وهذا هو التصوّر الذي وسّعه أرسطو والذي سبق
أن أكّد عليه أفلاطون، وهو ما سمّاه الفارابي بالتعقّل »**.

| Ce qui est distingué | الآداب (même « حسنة ») | الفضيلة |
| --- | --- | --- |
| Ce en quoi elle consiste | **تطابق بين تصرّف ونموذج ما** | **الذّكاء والدقّة أي القدرة على الاختيار** |
| Statut | **استعداد / ممارسة** conforme | **ليست مجرّد استعداد للقيام بأفعال** |
| Peut être mauvaise ? | **oui** (قصد غير سليم · غاية السيطرة والتملّك) | non — c'est le critère du jugement porté sur les mœurs |
| Noms rattachés | — | **أرسطو** (وسّعه) · **أفلاطون** (سبق أن أكّد عليه) · **الفارابي** (سمّاه **التعقّل**) |

**■ قيل في الآداب (p.384, verbatim — 3 encadrés de citation)** :

| Auteur (tel qu'imprimé) | Citation |
| --- | --- |
| **كورنو** | « في **المفهوم الأوسع للكلمة** تشتمل الآداب على **كلّ ما يكاد يتّصل بالاتنولوجيا**، لكننا **لا نعني هنا بالآداب إلاّ ما هو في نظام الوقائع المألوفة والغريزيّة مقابلا في نظام الأفكار** ». |
| *(sans nom imprimé — la citation suit immédiatement celle de كورنو)* | « إنّ **التشريفات المخفّفة للشيخوخة** و**احترام الضيافة** و**تكافل اعضاء الأسرة** `[sic — sans hamza]` هي **سمات من الآداب المتعلّقة تعلّقا واضحا ببعض الأفكار الأخلاقيّة** ». |
| **جون جوبار** | « **تتكوّن الآداب من عادات وتقاليد. تصنع التقاليد الآداب العامّة وتصنع العادات الآداب الخاصّة** ». |

Illustration p.384 (bas de page, pleine largeur, sans légende imprimée) : peinture — un vieil
homme coiffé d'un chapeau et une fillette en robe claire portant ensemble un seau, dans un
sous-bois sombre.

**2 — الإيتيقا · `Ethique` — p.385-388**

**■ لغة (verbatim, intégral)** :

> عبارة من **أصل إغريقي** `Ethikos` من `Ethos` التي تعني **سلوكا أو عادة**، وكان **أرسطو أوّل
> من أدمجها في اللغة الفلسفية**، إذ كان أوّل من تحدّث عن « **إيتيقا نظريّة** » في **التحليلات
> الثانية**، وتعني **الفرع من الفلسفة الذي يهتمّ بدراسة تصرّف الإنسان، والمعايير الأساسيّة
> لتقييم السّلوكات والإختيارات**.

**■ فلسفيّا (verbatim — définition officielle + les trois distinctions qu'elle porte)** :

> **الإيتيقا فرع من الفلسفة موضوعه الأحكام القيمية المتعلّقة بالتمييز بين الخير والشرّ**.
> وتكون **نظريّة ومتّصلة في الغالب ببحث ميتافيزيقي** ( خاصة مع **كانط** )، وتتميّز عن
> « **الإيتيقا المطبّقة** » التي تعنى **بالبحث عن نتائج النظريات الإيتيقية في ظروف معطاة**.

Puis, dans le même paragraphe (p.385) — ce que la philosophie fait, et **ne se contente pas** de
faire : si la philosophie, dans son souci éthique, s'est surtout intéressée à **وصف السّلوك
الأخلاقي والقيم التي توجّهه**, « **فإنّها لم تكتف بذلك، إذ عملت على توفير علامات عن المعايير
والقيم التي يجب احترامها في الفعل** ».

**Les trois distinctions explicites de l'entrée (c'est le cœur testable)** :

| # | Distinction | Ce que le manuel en dit (verbatim resserré) |
| --- | --- | --- |
| 1 | **الإيتيقا (النظريّة) ≠ الإيتيقا المطبّقة** | l'éthique est **نظريّة ومتّصلة في الغالب ببحث ميتافيزيقي** (خاصة مع كانط) ; l'éthique **appliquée** « تعنى بالبحث عن **نتائج النظريات الإيتيقية في ظروف معطاة** ». |
| 2 | **طابع وصفي ≠ طابع معياري** (à l'intérieur de l'éthique) | « ويمكن أن نميّز في **الإيتيقا** بين **طابع وصفي وطابع معياري** ؛ **غير أنّ هذا التمييز هو تمييز منهجي فحسب**، لأنّ **النظريّات الإيتيقية الفلسفية في الواقع تخلط دوما بين هذين الطّابعين** ». ⚠️ distinction **méthodique seulement**, pas réelle. |
| 3 | **الإيتيقا ≠ الأخلاقيّة `Moralité`** — **la distinction de هيغل** | « ويمكن أن نضيف **تمييزا منهجيّا آخر** : تمييز **الإيتيقا** عن **الأخلاقيّة** `Moralité`، وهو **التمييز الذي أقرّه هيغل في كتابه "مبادئ فلسفة الحقّ"** ؛ حيث ذهب إلى أنّ **الأخلاقية تشير إلى الطابع الذاتي للسلوك**، مثال ذلك **نيّة الذات واستعدادها الداخلي** ؛ في حين أنّ **الإيتيقا تشير إلى مجموع القيم الأخلاقية الفاعلة في التاريخ** ( **وتعدّ المؤسّسات مثل الأسرة والمجتمع المدني والدولة لدى هيغل، أشكالا من الإيتيقا** ) ». |

⇒ Récapitulatif de la distinction hégélienne, telle qu'imprimée :

| | **الأخلاقيّة** `Moralité` | **الإيتيقا** |
| --- | --- | --- |
| Ce qu'elle vise | **الطابع الذاتي للسلوك** | **مجموع القيم الأخلاقية الفاعلة في التاريخ** |
| Exemple imprimé | **نيّة الذات واستعدادها الداخلي** | **المؤسّسات** : **الأسرة**, **المجتمع المدني**, **الدولة** |

**L'histoire de l'éthique telle que le manuel la découpe (p.385-387)** — « أمّا في خصوص **نشأة
الإيتيقا** … ». C'est un récit continu, en huit temps :

1. **سقراط والسفسطائيون — l'origine (p.385)** : « يمكن اعتبار **سقراط والسفسطائيين أوّل من طرح
   المشكل الأخلاقي في دلالة فلسفية في القرن الخامس ق.م.** », **نتيجة صعود طبقة من أثرياء
   التجارة هيمنت على طبقة النبلاء الذين لهم حقّ النبالة بالوراثة**. Le point d'appui lexical
   imprimé : **« أغاتوس »** (`agathos`) signifie en grec à la fois **الخير والنبيل**, et
   **« أريت »** (`arete`) signifie **إمّا الفضيلة أو النبل بالدم والوراثة** — « وهذه **مطابقات
   غير بديهية** لدى الفلاسفة في القرن 5 ق.م. ».
2. **Le partage السفسطائيون / سقراط وأفلاطون (p.385)** — l'opposition la plus nette de la page :
   - **السفسطائيون** défendent que **la vertu s'apprend (تعلّم الفضيلة)** parce qu'elle consiste
     en **مجموع قواعد تقنية للحياة في المجتمع** ; le critère de légitimité n'est donc **pas la
     noblesse héréditaire** mais **الوظيفة الإجتماعية للسلوكات وما تضمنه من نجاحات**.
   - **سقراط وأفلاطون**, à l'inverse de cette légitimité **مرتبطة بالظروف وبعوامل عرضية (الغنى
     والحظّ وحذق صناعة الخطابة)**, exigent **وضع معايير أخلاقية على أسس ثابتة يقينية : أفكار
     بفضلها يتعرّف كلّ إنسان عاقل على العادل والجائر**.
   - Nuance imprimée sur **أفلاطون** : il reste attentif au lien vertu/politique souligné par les
     sophistes, **jusqu'à admettre que « الفضائل ليست في متناول الجميع فلكلّ فضيلة ما يناسبها من
     الوظيفة الإجتماعية »** ; mais le critère du bien reste lié **بالأفكار أو المثل** donc
     **ثابتا بثباتها**, et **الخير الأسمى للإنسان أن يترفّع بتأمّل المثل دون غايات عمليّة**.
   - **Postérité imprimée de la thèse platonicienne** : elle a été **منطلقا لنزعة صوفية أو
     زهدية** ; on en trouve la trace **في الفلسفة الإسلامية لدى الفارابي وابن سينا وفي الفلسفة
     المشرقية لدى ابن طفيل وابن باجة**…
3. **أرسطو — la fondation sur la nature (p.386)** : si **أفلاطون** avait fondé l'éthique
   **على شاكلة الرياضيات**, **أرسطو** « **أقرّ بوضوح بأنّ الإيتيقا لا يمكن أن تماثل الرياضيات في
   دقّتها** » et a bâti sa théorie **في صلة بالعادات والتقاليد الموجودة والمؤسّسات السياسية**.
   Son critère n'est **ni** l'efficacité pratique et politique de la conduite (les sophistes)
   **ni** la structure métaphysique de l'être (Platon), mais **مبدأ يجب البحث عنه في
   الإستعدادات والملكات التي لدى البشر بالطبع**. D'où (verbatim) :
   > وهكذا **وللأوّل مرّة تتأسّس الإيتيقا على الطبيعة** في معنى إمّا **المبدأ الداخلي** الذي
   > يحرّك كلّ فرد أو **نظام الكسموس** الذي يحكم حركته وميولاته.

   Corollaire imprimé : **العقل** étant **أرفع الملكات لدى البشر**, « فإنّ **الخير الأسمى
   والكمال والسعادة تتمثّل في استخدامه، أي في فعل التعقّل** وبخاصّة **تعقّل ما هو أسمى وجدير أي
   الإله ذاته** ». Ce que cette fondation résout : **مشكل عدم التمييز بين شرعية ميتافيزيقية وبين
   شرعية مدنية–سياسية لأخلاقية السلوك** — « المشكلات التي عجز عن حلّها المفكّرون قبله ؛
   (**أفلاطون** بالذات) ».
4. **Après la cité — الرواقيّون / الأبيقوريّون (p.386)** : la fin de la **المدينة القديمة** et
   la naissance des empires (**إمبراطورية الإسكندر الأكبر** puis **الإمبراطورية الرومانية**)
   mettent l'éthique en position de chercher sa légitimité **في الجماعة السياسية** ; mais
   **الطبيعة** reste une référence décisive.
   - **الرواقيّون** : la vertu, c'est **أن نحيا وفق الطبيعة**, la nature restant **نظاما صارما
     مرتبطا بعلاقات الضرورة التي لا يمكن الإنفلات عنها** ; d'où un **مثل أعلى إيتيقي** qui durera
     **حتّى سبينوزا** — lequel « حافظ على معنى **إيتيقا كونية تتّجه إلى الإنسانية** على طريقة
     **ابيكتات** و**شيشرون** ».
   - **الأبيقوريّة** : garde le principe de nature **ولكن لا بمعنى النظام وإنّما لعبة قوى
     اعتباطية لا ينتظر منها الإنسان ثوابا ولا عقابا** ; d'où **« البحث عن اللّذة هو الحكمة
     الوحيدة »**, et le principe éthique épicurien : **غياب الإضطرابات أي السكينة**.
5. **L'entrée dans l'éthique moderne (p.386)** : elle commence **حينما انفصلت عن الكلّيات
   الشاملة التي تضمن الشرعية** et qu'apparaît **تصوّر جديد للفرد** (« تشهد بهذا أعمال
   **مونتانيو** مثلا ») ; la conduite morale devient justiciable d'une analyse qui découvre
   **الحركات المتخفيّة** porteuses d'un **خطاب إيتيقي ممكن**. **الإيتيقا الحديثة متجذرة في
   الواقع**, elle cherche **غايات بنّاءة للإلتزام الإنساني**. Son problème propre :
   **العلاقة بين القانون الأخلاقي والقانون الوضعي، أو بين الطبيعة والمجتمع**.
6. **الحقّ الطبيعي · هوبس · لوك · روسو (p.386-387)** :
   - **مذهب الحقّ الطبيعي** fait de la nature **أصلا لقانون فوق القوانين الوضعية، وأساسا
     لتطوّرها**.
   - **هوبس** : la loi est à l'origine **اختراع بشري وضعه الإنسان في حساب المنافع والمضار** ; en
     tenant la conduite humaine pour mue par **غريزة أساسية**, l'éthique pourrait décrire ce que
     l'homme doit suivre **كما تقدر الفيزياء على وصف حركة الأجسام**.
   - **لوك** : une éthique **أقلّ صرامة**, liée aux **تجارب اللّذة والألم المشروطة بالمجتمع
     والثقافة**.
   - **روسو** : il rapporte **الفساد لا إلى طبيعة البشر بل إلى نشأة المجتمع وحقّ الملكية** —
     « بهذا **تردّ الإيتيقا من جديد إلى الطبيعة كما كانت منذ أرسطو ولكن دون أن يكون الإنسان
     حيوانا سياسيا** ؛ ذلك أنّ **حالة المدنيّة هي الأصل في الفساد والشرّ** ». La distinction
     nature/société y recouvre l'opposition **قانون الطبيعة ≠ القوانين الوضعية التي تضعها الدولة
     والتي تختلف حسب الأماكن والأزمان**.
7. **كانط — la charnière (p.387)** : « **ومن هذه الزاوية بالذات يستفيد كانط من روسو في بناء
   إيتيقا مغلقة دشّنت العصر الحديث وفتحت الباب لمرحلة معاصرة طرحت فيها قضايا جديدة** ». Par
   **القول بالطابع الصوري للأمر الأخلاقي** il pousse **à son maximum** la distinction loi de la
   nature / loi positive ; et par ses théories **في الجمال وفلسفة التاريخ** il inaugure
   **التفكير الإيتيقي المعاصر** — celui **الذي لا يشغله التمييز بين الطبيعة والمجتمع وإنّما
   علاقة الإيتيقا بالتاريخ**.
8. **La crise contemporaine (p.387)** — quatre coups portés, dans l'ordre imprimé :
   - **الوضعيّون** (**كونت**, **دوركايم**…) et **الماركسية**, qui introduit l'élément ouvrant
     « **أزمة عامّة** » : **الأيديولوجيا**.
   - **نيتشه**, dans **« جينيالوجيا الأخلاق »** : il réduit les catégories majeures de l'éthique
     — **الخيّر والسيّء، العادل والجائر** — à des **علاقات قوّة ليست إجتماعية بالضرورة بل هي
     فاعلة من داخل الفرد** ; l'individu est **مجال لصراعات ودوافع متناقضة**, et
     **« ليس الوعي إلاّ حاصل هذه الصراعات »**.
   - **التحليل النفسي**, dans le même horizon : le tournant a eu **أثره الحاسم على الإيتيقا**
     car il l'a menée à **ذوبانها بغياب الذات القادرة على الإختيار الأخلاقي** — « فالفرد المسؤول
     الذي يقصده الأمر الأخلاقي **أضحى غير قابل للإمساك به** ».
   - **La riposte** : défendre **مجال التجربة الخلقية** — glosé en marge **( مجال الإعتراف
     الداخلي بالقيم )** — comme **لا يمكن عزله عن حرّية الفرد**. Elle se lit dans
     **الحوار القائم في بداية القرن 20** entre **العلوم الإنسانية** (**ديلتاي**, **ريكور**,
     **جورج سيمال**…) et **فلسفة القيم وحدسية برجسون** — « التي تدعّمت مع **"ج.مور"** ». Ce
     travail rejoint deux courants opposés sur les effets de la société industrielle :
     **مدرسة فرانكفورت** (mise en garde contre **مخاطر اغتراب الذات**) et **هيدغر** (solution
     philosophique pour dépasser **أزمة الذات المتّصلة بالميراث الميتافيزيقي**). Point d'arrivée
     imprimé : **« وفي حقل الهرمينوطيقا أصبحت الإيتيقا مذهبا لتواصل اجتماعي تتفاعل فيه القيم
     والقواعد الفردية والجماعية »**.

**■ قيل في الإيتيقا (p.387, verbatim, 2 citations)** :

| Auteur (tel qu'imprimé) | Citation |
| --- | --- |
| **اينشتاين** | « إنْ أمكن لنا الاتّفاق حول بعض **القضايا الإيتيقيّة الأساسيّة** التي ينتج عنها قضايا أخرى… هذه **الأوّليات الإيتيقيّة تلعب في الأخلاق دورا موازيا للدور الذي تلعبه الأوليات في الرياضيات** ». |
| **رونيه لوسان** | « إنّ **برنامجا كاملا لإيتيقا عقلانيّة كان من قبيل الوعد أكثر منه متحقّقا** بفضل الأخلاق العقلانيّة لأنه، **شأن العلم الإستنتاجي**، اعترض هذه العقلانيّة **تنوّع شديد للتجارب** ». |

**Encadré `* لمزيد التعمّق` (p.388)** — bandeau bleu portant deux onglets, **الآداب** (en haut)
et **الإتيقا** `[sic — orthographié sans le ي, alors que le corps du texte écrit الإيتيقا]`
(en bas), et deux boîtes de liens en regard :

- **Boîte en regard de l'onglet الآداب** : `fr.wikipedia.org/wiki/Éthique` ·
  `www.hapmap.org/ethicalconcerns.html.fr` · `www.fidh.org/rubrique.php3?id_rubrique=252` ·
  `www.evene.fr/citation/mot.ph?mot=ethiques` ·
  `www.unesco.org/courier/2000_03/fr/ethique/intro.htm`
- **Boîte en regard de l'onglet الإتيقا** : `www.evene.fr /ciation/mot/php?mot=moeurs-54k`
  `[sic — espace après .fr, et « ciation »]` · `fr.wikipedia.org/wiki/Coutume-48k` ·
  `www.voltaire-integral.com/Html/00Table/11.html-52k` ·
  `www.linternaute.com/histoire/categorie/112/a/1/histoire_des_m_urs.shtml-79k`

⚠️ **Les deux listes sont interverties par rapport à leurs onglets** : la boîte alignée sur
**الآداب** ne contient que des liens sur l'**éthique**, celle alignée sur **الإتيقا** que des
liens sur les **mœurs** (`moeurs`, `Coutume`, `histoire_des_mœurs`). Relevé tel quel — voir
§ Incertitudes.

Illustrations p.388 : (a) dans le bandeau bleu, photo couleur d'une femme en blouse blanche de
profil devant un écran, dans un laboratoire à stores vénitiens ; (b) en bas de page, pleine
largeur, peinture d'une assemblée ecclésiastique — un homme debout en chaire, bras tendu,
haranguant une assistance d'évêques et de moines en robes blanches, un greffier écrivant au
premier plan (sans légende imprimée).

###### 3.2.3.2 سياقات فكريّة — p.389-392

> **Pages lues** : p.389–392 (intégral). **Source** : manuel élève `210402` (CNP,
> `210402P00.pdf`), مبحث 3.2 « الأخلاق : الخير والسّعادة ». Rendus 300 dpi, colonne par colonne.
> Le folio imprimé = la page PDF (vérifié sur les 15 pages de la tranche).

Deux courants sont exposés : **العدميّة** (p.389-390) et **النفعيّة** (p.391-392). Bandeau de
tête imprimé en haut de p.389 : **نافذة دعائم للتفكير في المسألة**, puis le sous-titre en
encadré crème **سياقات فكريّة**. Chaque courant porte un cartouche bleu numéroté avec son
équivalent latin : **1– العدميّة** `Le nihilisme` · **2- النفعية** `Utilitarisme`.

⚠️ **Le gabarit n'est pas symétrique entre les deux entrées, et il diffère de celui du مبحث 2.**
Sur le مبحث 2 (p.256-259) le gabarit était **\* التعريف → \* الجهاز المفهومي → \* لمزيد التعمّق**.
Ici :

| | **1– العدميّة** (p.389-390) | **2- النفعية** (p.391-392) |
| --- | --- | --- |
| `* التعريف` | **oui** (p.389) | **oui** (p.391) |
| `* الجهاز المفهومي` | **absent** | **oui** (p.392, 3 entrées) |
| `* تنبيهات` | **absent** | **oui** (p.392) — **rubrique inédite**, elle n'existait pas au مبحث 2 |
| `* لمزيد التعمّق` | **absent** | **oui** (p.392, 4 références bibliographiques) |

⚠️ **Ni généalogie datée ni tableau d'opposition** ici — contrairement à
`الإبستيمولوجيا البنائيّة` (مبحث 2, p.257-259) qui imprimait les deux. L'entrée **العدميّة** est
un récit historique continu sans schéma ; l'entrée **النفعية** est un exposé doctrinal suivi
d'un dialogue avec ses adversaires, sans tableau. **Rien à en déduire par analogie** : ce que la
page imprime est ci-dessous.

---

**1 — العدميّة · `Le nihilisme` — p.389-390**

**\* التعريف (p.389)** — l'entrée s'ouvre sur l'étymologie arabe, puis énumère **cinq
significations étiquetées أ / ب / ج / د** (la 5ᵉ n'est pas lettrée : elle enchaîne en haut de la
colonne de gauche).

**■ Étymologie (verbatim, intégral)** :

> **العدمية**: من "**العَدَمُ والعُدْمُ**"، و**العُدْمُ**: فقدان الشيء وذهابه، يعْدُمُه عُدْما،
> فهو عَدِمٌ، و**أَعْدَمَ**، إذا افتقر، و**أَعْدَمَ غيره**، و**العَدَمُ**: الفقر، نقول رجل
> عديم، لا عقل له، وأعدمني الشيء: لم أجده. و**العديم**: الفقير الذي لا مال له… ولا شيء عنده.

**■ Les significations (verbatim — « يمكن أن نعثر على أكثر من دلالة للعدمية »)** :

| # | Sens, tel qu'imprimé |
| --- | --- |
| **أ** | « **مذهب يقول بعدم وجود أي شيء**. » |
| **ب** | « **مذهب ينفي وجود أية حقيقة أخلاقية، أية هيكلية للقيم**. حالة الفكر الذي يفتقر الي هذه الهيكلية، والذي يتساءل: " **ما جدوى ذلك؟** " ولا يمكنه الجواب. » |
| **ج** | **le sens politique russe** — « مذهب **حزب سياسي وفلسفي روسي**، يسمى للمرة الأولى بهذا الاسم في رواية "**تورغنيف**" (**أباء وأبناء**) "**1862**" لجاكوبي » `[sic — « أباء » sans hamza sur le alif]`. |
| **د** | **le sens épistémologique** — « في **نظرية المعرفة** تقوم العدمية على نفي "**كل احتمال معرفي، كل حقيقة عامة يقينية**"، وتقوم **العدمية الميتافيزيقية** على نفي "**كل حقيقة للعالم الخارجي كما هو، نفي كثرة الأشياء**". » |
| *(non lettré, p.389 col. gauche)* | **le sens ontologique** — « **العدميّة هي النظرية التي من خلالها لا وجود للمطلق** ». |

Développement du sens **ج** (p.389, verbatim resserré) : en Russie les **الرجعيون** donnaient le
nom d'**العدميين** aux **الديمقراطيين الثوريين**, leur imputant **انكارا غير مشروط لكل الحضارة
السابقة** ; or ces démocrates révolutionnaires, « **بينما كانوا يرفضون القنانة والنظام
البرجوازي كانوا يضعون برنامجهم الايجابي الخاص ذا المثل العليا الاشتراكية** ». Puis la
distinction attribuée à **لينين** — c'est le seul partage explicite de la page :

> وقد **فرق لينين** بين **العدمية الثورية** كسلب طبيعي لموقف الأنظمة الاجتماعية الرجعية، وبين
> **العدمية الفوضوية لدى المثقفين** الذين اعلنوا "**اعادة تقييم القيم**" أي **انكار كل قواعد
> الأخلاق والعدالة التي وضعتها الحضارة الانسانية**.

⇒ **العدمية الثورية** (négation naturelle du régime réactionnaire) **≠** **العدمية الفوضوية**
(intellectuels — « réévaluation de toutes les valeurs », négation de toute règle morale).

**■ L'histoire du nihilisme telle que le manuel la trace (p.389, col. gauche)** — pas de
généalogie encadrée, mais un récit daté :

1. **Racine antique** : le nihilisme, en tant que « لا وجود للمطلق », **تتجذر في المنظور القديم
   كما يؤكده السفسطائي "غورجياس" وبصفة عامة الشكاك اليونان**.
2. **XIXᵉ siècle — le courant russe** : « **وفي حدود القرن التاسع عشر بدأت العدمية تتشكل كتيار
   فكري قاده مفكرون روس فيما بين 1860 و1870** », marqué par **التشاؤم الميتافيزيقي** face au
   prolongement positiviste d'**أوغست كونت**, et par **الريبية** à l'égard des **القيم التقليدية
   (الأخلاقية، الدينية، الفنية)** ; le tout accompagné d'un **مشروع بناء المجتمع على أسس علمية**.
   Formule imprimée qui résume ce moment :
   > « **إذا كان الله غير موجود، فكل شيء جائز.** »

   ⇒ Conséquence tirée par le manuel : « **تتطابق العدمية لاحقا مع الفردانية الفوضوية التي تهدف
   الي تقويض كل شيء، بما في ذلك الدولة** ».
3. **نيتشه (1844–1900)** — « **أهم مفكر في هذا الصدد** », « **فهو بحق مفكر ما بعد حديث سابق
   لأوانه** ». Deux formules datées, imprimées **en bleu** dans la page :
   > « (1888) **أن العدمية أضحت تدق على الأبواب** »

   > « **الحقيقة هي فقط تبلور أو تصلب الصور المجازية القديمة** »

   Le manuel commente : cette déclaration de 1888 **شكّل مثارا للشكوك والمخاوف في أوروبا** ; et
   la seconde doit se comprendre **في سياق أوروبا التنويرية** comme une exigence de
   **اعادة تذويب الصور المجازية لنبين انها معتقدات بشرية أو وجهة نظر هذه الفئة الاجتماعية أو
   تلك**. Enfin : « **لقد كرس نيتشه حياته للكشف عن خواء الآمال التنويرية** », et le nihilisme a
   représenté **المفهوم النيتشوي الأكثر مطابقة للتعبير عن سيلان الحقيقة أو الواقع
   ولامحدوديتهما**.
4. **Le retournement du soupçon (p.389 fin → p.390)** : « **وعندما تنصب نظرة العقل الحديث،
   المشككة، على العقل نفسه، تتولد العدمية وهي تهاجم العقلانية أينما كانت، في الفن أو في الفلسفة
   أو في العلوم** » — car les systèmes qui se disent rationnels « **هي في الحقيقة أنظمة اقناع** ».
   Et ainsi tombe le masque : la vérité, **كما يقول نيتشه ويستعيدها فوكو**, apparaît **فقط
   كتجليات "لإرادة السلطة"** — celle des « **الذين يدعون يضعون أنفسهم في منزلة أعلى من أولئك
   الذين يدعى عليهم وبذلك يهيمنون عليهم** ».

**■ « موت الإله » et le choix dionysiaque (p.390, verbatim resserré)** :

> لقد **اكتسب نيتشه شهرة كبيرة عندما صرح "بموت الإله"**، ولو أن الكثير يرى ان هذه الصيغة
> **ليست الا تعبيرا مجازيا عن فقدان الأسس الفلسفية ولكنها أيضا تمثل شكلا جادا من أشكال ضد
> الألوهية**. وعلى كل حال فإن نيتشه يعني أنه **لم يعد بإمكاننا التأكد من أي شيء، فالأخلاق كذبة
> والحقيقة وهم**، ولا يبقى أمامنا الا **الخيار الدايونايسي** ( **نسبة الى الإله الإغريقي
> دايونايسوس، إلاه المسرح والخمر** ) `[sic — « إلاه »]` المتمثل في **تقبل العدمية والعيش بدون
> أوهام أو ادعاءات ولكن بتحمس وفرح**.

**■ La distinction structurante de la p.390 — العدمية السلبية ≠ العدمية الايجابية** (c'est le
couple le plus directement testable de l'entrée) :

Le manuel pose d'abord les **deux versants du nihilisme nietzschéen** (p.390, col. droite, bas) :

> إنّ **العدمية في المنظور النيتشوي ذات وجهين**: تعنى في **المقام الأوّل غياب الأهداف التي تسمح
> بإعطاء معنى للحياة الإنسانيّة بشكل قبلي**: " **لا هدف للمستقبل** "، سيما وأن " **الله قد مات**
> ". وهو أمر يتناسب مع ما يلاحظه نيتشه من "**انحدار**" و"**تقهقر القوة الروحية**" لدى الغرب.

Puis, p.390 col. gauche, le **versant actif** et le tableau qu'il permet :

> **على نقيض هذا المعنى السلبي للعدمية يتجلى الوجه النشيط أو الايجابي للعدمية** والمتمثل في أن
> **تحطيم القيم التقليدية والانقلاب عليها يكون بخلق عالم جديد** حيث يتأكد " **اتساع وثراء قوة
> الفكر** ".

| | **العدمية السيئة / السلبية** | **العدمية الايجابية / النشيطة** |
| --- | --- | --- |
| Ce qu'elle fait à l'homme | **تذل وتهمش الإنسان من العمق** · **تصرف كل قوة الإنسان وتعزله إزاء العالم** | **تصغي لصيحات معاناة الانسان** · **تنقذه، وتحرره، تمنحه القوة، تعيد خلق معنى وجوده** |
| Ce qu'elle fait de lui | **تجعل من الإنسان معطى ومن الطبيعة مجال ريبة** ; **كائنا لا يتساءل، لا يهتم الا بصياغة العالم بحسب صورته، ومزاجه** | — |
| Sa formule | « **لم يعد الإنسان كائنا في أفق الصيرورة: إنّه " الإنسان الأخير "** » (imprimé en bleu) | « **يجب تخيل سيزيف سعيدا** » (imprimé entre guillemets) |
| Verdict du manuel | — | « **وقتئذ تكون العدمية فعلا، وفلسفة حكمة** » |

**■ Le nihilisme comme problème, et la lecture marxienne (p.390, col. gauche, verbatim
resserré)** :

> إنّ ما اعتبره **نيتشه** مشكلة بالنسبة إلى **العلوم والفلسفة والميتافيزيقا والأخلاق**، أوعزه
> **ماركس** إلى **آليات النظام البرجوازي**، وبمعنى آخر: في **النظام الرأسمالي** يسمح للسوق
> بتنظيم حياتهم، وحتى حياتهم الداخلية، **وبمعادلة كل شيء بقيمته التجارية — أي التسليع** — نجد
> أنفسنا **نبحث عن الأجوبة المناسبة للأسئلة التي تتعلق بالنجاعة والشرف وحتى الحقيقة في ساحة
> السوق** ؛ ويمكن أيضا أن **نفهم العدمية بهذا المعنى العملي اليومي**.

⇒ **نيتشه** (le nihilisme comme problème des sciences, de la philosophie, de la métaphysique et
de la morale) **↔** **ماركس** (il l'impute aux **آليات النظام البرجوازي** / à la
**تسليع**) — c'est la seule confrontation d'auteurs explicitement construite dans l'entrée.

Illustrations p.390 : (a) col. droite, gravure en noir et blanc — une grande cloche penchée, une
corde nouée, et un crâne en bas à gauche, sur un fond gris texturé (sans légende imprimée) ;
(b) col. gauche, bas de page, photo couleur — une piste de terre rectiligne traversant un
plateau désertique ocre sous un ciel bleu uni, avec **une silhouette humaine seule** au milieu de
la route (sans légende imprimée).

---

**2 — النفعية · `Utilitarisme` — p.391-392**

**\* التعريف (p.391, verbatim, intégral pour la phrase de définition)** :

> **النفعية** مذهب فلسفي **ارتبط بالفلسفة الإنكليزية** وبصورة خاصة بالفيلسوف **جيرمي بنتام**
> `J.Bentham` (1748–1832) **وبتلميذه جون ستيوارت ميل** `J.S.Mill` (1806–1837). **يدافع هذا
> المذهب عن مبدأ المنفعة وأولويته في الحياة الأخلاقية بشكل خاص والحياة الإنسانية عامة**، كما
> **يطلق اسم النفعية على النسق الذي يكمن في إرجاع معنى الصحيح العادل، إلى معنى النافع، وفي جعل
> المنفعة أساسا للحق وللأخلاق**.

⚠️ **Erreur de dates dans la source** : le manuel imprime **(1806–1837)** pour
**جون ستيوارت ميل** `J.S.Mill`. Relevé tel quel — voir § Incertitudes.

**■ Ce que la منفعة n'est pas (verbatim)** :

> **لا يحمل مفهوم المنفعة على معنى المصلحة الشخصية، ولا يفيد تشريعا لمنطق انتهازي** كما قد
> يتبادر إلى الأذهان، إذ **يعتبر مفهوما " هيدونيا "** أي **يتحرك ضمن سياق المذاهب الفلسفية التي
> تجعل من اللذة المحرك الأساسي للتصرفات الإنسانية**، وهي **مذاهب عريقة في تاريخ الفلسفة** يمكن
> أن نستحضر منها **الأبيقورية** على سبيل الذكر.

**■ Le postulat de بنتام — les deux maîtres (verbatim)** :

> إذ **يؤسس بنتام تصوره على التسليم بأن الطبيعة وضعتنا تحت سيطرة سيدين هما اللذة والألم**،
> **يتحكمان في تصرف البشر وسلوكهم**، في **أفعالهم وأقوالهم وتفكيرهم**، **ويمليان علينا ما يجب
> فعله** كما **يحددان معيار الصواب والخطأ، والخير والشرّ**.

**■ Les deux faces de la منفعة (p.391, verbatim — c'est la distinction la plus testable de
l'entrée)** :

| | **الوجه الإيجابي للمنفعة** | **الوجه السلبي (النافع في سلبيته)** |
| --- | --- | --- |
| Définition imprimée | « **القدرة الكافية في غرض معيّن على إنتاج ربح أو نفع أو امتياز أو لذة، أو خير أو سعادة** » | « **القدرة على منع حصول خسارة أو سوء أو ألم أو شرّ أو حزن** » |
| Statut de ces termes | « **وهي معاني مترادفة في لغة دعاة النفعية** » | « **من جهة علاقته بما نعتبره مصلحة** » |

⇒ D'où le **principe** tel que le manuel le formule : « **يعدّ مبدأ المنفعة ما به نكون قادرين
على جلب لذّة لا يعكّرها ألم أو مصاب. وبذلك فالفعل الذي يجلب السّعادة يعدّ فعلا جيّدا وما
يتعارض معها يعدّ سيّئا يجب تجنّبه** ».

**■ Individuel / collectif — le passage à la نفعية اجتماعيّة (p.391, verbatim)** :

> **لا ينبغي أن يفهم من النفعية دفاعا عن المصلحة الفردية في مقابل المصلحة العليا للمجتمع**، إذ
> أنّ **مصلحة المجموعة ليست سوى " مجموع مصالح الأفراد العديدين الذين يؤلفونها "**.

*(la citation entre guillemets est imprimée en bleu dans la page)*

⇒ « **لذلك يغدو من الخلف الحديث عن مصلحة المجموعة دون استحضار مصلحة الفرد، وبذلك فإنّ النفعيّة
تفيد مصلحة الفرد كما المجموعة، وحين تتحوّل إلى نفعية اجتماعيّة، تصبح مبدأ أساسيّا يتمثّل في
مبدأ البحث عن السعادة القصوى للمجموع** ». Et le critère qui en découle : « **على هذا الأساس
يكون تحصيل سعادة الفرد أي لذّة كل فرد من أفراد المجتمع وتحصينه ضدّ الألم الغاية القصوى التي
ينشدها الفرد بأفعاله والمشرّع بقانونه** ».

**■ L'apport propre de ميل `Mill` — la قضيّة الكيفيّة (p.391, verbatim resserré)** :

> **وإذا كان ميل قد تبنى مذهب معلّمه بنتام فإنّه أضاف إليه مفهوم الكيفيّة** أي **مسألة صفات
> اللذات ونوعيّتها**، كما **حرص على تجذير النفعية في التقليد الفلسفي الموغل في القدم معتبرا
> سقراط لا أب الفلسفة وإنّما أب النفعيّة**.

⇒ Deux gestes de Mill, imprimés comme distincts : (1) **ajouter la qualité** (le *combien* de
Bentham devient aussi un *quelle sorte*) ; (2) **enraciner** la doctrine dans la tradition — avec
la formule frappante **سقراط ليس أب الفلسفة بل أب النفعيّة**.

**■ Le dialogue avec les adversaires — trois objections et leurs réponses (p.391, chacune
introduite par un astérisque imprimé `*`)** :

| # | L'objection (telle que le manuel la formule) | La réponse imprimée |
| --- | --- | --- |
| 1 | La نفعية comprise **بما هي إدانة للذّة** | « **فإنّ ميل لا يرى في المنفعة ما يفيد شيئا مناقضا للذّة، بل هي اللذة ذاتها وغياب الألم، إذ يشمل النافع اللذيذ والأنيق والجميل والممتع** ». |
| 2 | La نفعية comprise **بدفاعها عن اللذة بما هي دفاع عن مبدأ غير أخلاقي، عن مبدأ وضيع وأناني** | « **فإنّ إدخال ميل مفهوم الكيف أي مفهوم نوعية اللذات يفيد إقرارا بأنّ هناك لذّات أكثر قيمة من غيرها** » ; en outre **النفعية لا تشرع للأنانية، لأنّ مثلها الأعلى هو تحقيق قدر أكبر من السعادة لقدر أكبر من النّاس**, et « **بالتالي لا تستطيع أن تبلغ مثلها الأعلى، إلاّ حين تدعو إلى النبل الأخلاقي** ». |
| 3 | **السعادة لا يمكن أن تكون غاية الحياة والنشاط البشري، مادامت حلما بعيد المنال** | « **ولكن ميل لا يكتفي بالتبشير بإمكان الوجود السعيد بل يتنبأ بمجتمع سعيد آت بفضل التقدّم** ». |

**■ La conclusion de l'entrée (p.392, verbatim)** :

> **هكذا تؤكد النفعية أن مبدأ المنفعة شأن إنساني يتوافق مع الفضيلة ويتصالح معها، ويتنزل في إطار
> التقدّم الحضاري والعلمي، فتجعله مركز الإيمان بالإنسان وعلمه.**

**\* الجهاز المفهومي (p.392, verbatim, 3 entrées)** :

| Terme | Définition imprimée |
| --- | --- |
| **■ المنفعة** | **القدرة الكافية في غرض معيّن على إنتاج ربح أو نفع أو امتياز أو لذة، أو خير أو سعادة.** |
| **■ اللذة** | **حالة وجدانية من طبيعة حسية تتخذ دلالة إيجابية في السجل الأخلاقي النفعي لتتماهى مع الخير والامتياز والمصلحة والنفع في مقابل الألم بما هو شر أو حزن أو خسارة.** |
| **■ السعادة** | **تفيد تحقيق اللذة وتجنب الألم، وهي حالة رضى تام تستأثر بمجامع الوعي، عبر إرضاء الميول وإشباعها سواء بالتوسع أو بالتكثّف.** |

**\* تنبيهات (p.392)** — rubrique **inédite** (pas de `تنبيهات` au مبحث 2). Elle sert à ne pas
confondre la نفعية avec les doctrines voisines :

> **يتعيّن في إطار تحديد النفعية بما هي نسق فلسفي له خصوصيته تمييزه عن أنساق أخرى تختلف عنه وإن
> تقاطعت معه** مثل **البراغماتية أو الذرائعية**، **ومذهب اللذة كما يعرف مع أبيقور** على سبيل
> المثال.

Puis deux notices, chacune sous puce **■** :

**■ الذرائعية (p.392, verbatim resserré)** — « **مذهب من بين أعلامه شارل بيرس وويليام جيمس
وموريس بلوندال** ». Sa thèse, telle que le manuel la ramasse :

> **يمكن أن نختزل أطروحته في تخليص الفلسفة من اللغو والسفسطة، وذلك بالتفريق، وبمعيار دقيق، بين
> الصيغ الفارغة والصيغ الدّالة حقّا**، كما يرى أنّ **الحقيقة علاقة ملازمة كلّيا للاختبار
> البشري، بحيث تكون المعرفة في خدمة الفعالية**، ويكون **للفكر طابع غائي بالأساس**، إذ أنّ
> **حقيقة قضية ما تكمن في كونها " مفيدة " و" مرضية " و" ناجحة "**، **ويفيد النجاح التوافق الفطري
> بين العقول على ما تؤكد صحته الوقائع الموضوعية الملحوظة جماعيا**.

⇒ Ce que le manuel en conclut (p.392, col. gauche) : « **لذلك تحيل الذرائعية على موقف قريب من
موقف العقلانية، كما يطلق اسم المذهب الذرائعي على عقيدة تقوم على إظهار الحقيقة من خلال الفعل،
تتخطى الظاهرة العادية، وتبيان واقعة لا يمكن تجاهلها، ويؤدّي تحليلها بالضرورة، إلى الانتقال من
المسألة العلمية إلى المسألة الميتافيزيقية** ». Et la raison de la distinguer : « **حيث تتّحد
مبادرة الفاعل وما يعانيه من ردود الفعل ليتخطى الإنسان الظواهر بفعله الإرادي، لذلك يفترض بها أن
تكون موضوع دراسة خاصة، مميزة عن علم الفعالية، أي مميزة عن التقنية النفعية ومنطقها** ».

**■ الأبيقورية (p.392, verbatim resserré)** :

> **تقر الأبيقورية أنّه يتعذّر أن يكون الإنسان سعيدا إن لم يكن حكيما وشريفا وعادلا**، والحكيم
> **يبتغي غاية رفيعة يهدف إليها والمتمثلة في اللذة التي تعد الخير الأول وهو خير يصدر عن ذاته**،
> **وتعد اللذة مبدأ الحياة وغايتها**، أمّا **الألم فشر محض**.

Puis la mise au point qui fait toute la valeur de la notice — **la لذّة épicurienne n'est pas la
منفعة nor le plaisir des sens** :

> **ولكن اللذة مع الأبيقوريين لا تفيد المنفعة، ولا تحيل على الانسياق وراء التمتع بالشهوات، إذ
> تكمن اللذّة القصوى في التقيد بالفضيلة واتباعها** وهو ما يعني **ضرورة الترفع عن طلب بعض الملذات
> كما ليس من الواجب اجتناب الآلام كلّها**، إذ **ما يهم الأبيقوري هو تحقيق سكينة النفس وسلامة
> البدن** حيث **يمتزج الشعور بالطمأنينة والسلام بفاعلية النفس وفاعلية الجسد على نحو يدعوه
> أبيقور بالمزاج الطيب المرح**.

**\* لمزيد التعمّق (p.392, verbatim — 4 références, graphie de la source)** :

| Auteur (tel qu'imprimé) | Ouvrage |
| --- | --- |
| **جيرمي بنتام** | *مدخل إلى مبادئ الأخلاق والتشريع.* |
| **ستيوارت ميل** | *النفعية.* |
| **إيلي هالافي** | *تكوّن الفلسفة الجذرية (الجزء الثاني) تطور المذهب النفعي.* |
| **رنوفييه** | *علم الأخلاق.* |

⚠️ Contrairement au مبحث 2 (p.255 / p.257 / p.259), le `لمزيد التعمّق` de cette page est une
**bibliographie**, pas une liste de sites web. Aucun `لمزيد التعمّق` n'accompagne العدمية.

⚠️ **Aucune illustration sur p.391 ni p.392** — les deux pages sont en texte plein.

---

###### 3.2.3.3 نافذة كيفيّات التفكير — p.393-396

> **Pages lues** : p.393–396 (intégral).

⚠️⚠️ **Écart confirmé entre le فهرس et les pages imprimées — et il va dans le sens inverse de
celui annoncé.** Le فهرس range cette نافذة **à l'intérieur** de la نافذة دعائم. **Les pages
imprimées ne le font pas** : p.393 est une **page d'ouverture de نافذة à part entière** (grand
titre sur deux lignes **كيفيات** / **التفكير**, filet rouge, carrés rose/carmin — la signature
graphique d'une nouvelle نافذة), et **le bandeau vert de tête y est vide** — il ne porte plus
« نافذة دعائم للتفكير في المسألة » comme sur p.383-389. **p.394, p.395 et p.396 ne portent aucun
bandeau de tête du tout.** C'est le même traitement qu'au مبحث 2, où la fiche l'a numérotée
`2.4`, **autonome**, à côté de `2.3` (نافذة دعائم). Je conserve ici la numérotation `3.2.3.3`
demandée par le brief, mais **la source ne la subordonne pas** : à arbitrer à la relecture.

Autres écarts relevés par rapport au مبحث 2 (p.260-263) :

- Le titre imprimé est **كيفيات التفكير** — au مبحث 2 c'était **كيفيات للتفكير** (avec le لـ).
- **La photo d'ouverture est la même** qu'au مبحث 2 (p.260) : une **chouette effraie** perchée
  dans l'encadrement d'une vieille fenêtre en bois, la nuit. Seul l'encadré-citation change.
- **Aucune illustration en p.396** : la moitié basse de la page est vide (au مبحث 2, p.263
  portait une illustration).

**p.393 — page d'ouverture.** Encadré-citation crème avec portrait photographique en noir et
blanc, et le nom **برغسون** sur un onglet orange (verbatim) :

> « **لكي نقاوم المقاومة ونستمسك بالطريق السوي، لا يغوينا عنه هوى أو رغبة أو فائدة، لا بدّ لنا
> أن نقنع أنفسنا بحجج** ».
> — **برغسون**, *منبعا الأخلاق والدّين*

La نافذة comporte **4 تمارين** (p.394-396). Gabarit imprimé, en cartouches orange :
**المهارة المستهدفة** → **توضيح** (l'encadré de méthode) → un support (**السند** / **القضية** /
**المسألة** / **المهمّة**) → **المهام** ou **التمشّيات**. Chaque exercice est ouvert par
**تمرين** suivi de son numéro en rouge, avec le motif de carrés orange.

###### تمرين 1 — p.394

- **المهارة المستهدفة** : **تحديد سياقي للمفاهيم**.
- **توضيح (encadré de méthode, verbatim, intégral)** :
  > تُعدّ **الفلسفة حقلا تنشأ فيه المفاهيم من الكلمات** عبر **عمليّات التحليل والتفكيك
  > والمقارنة وتبيُّن الخواص** بالتمييز فيها بين **الضّروري والعرضي** قصد **بناء معنى وضبط
  > دلالة**.
- **السند** — **ج. ج. روسّو**, *أميل أو التربية*, **ص 111**, **ترجمة عادل زعيتر** ; référence
  latine imprimée sous la référence arabe : **`J. J. ROUSSEAU; Emile ou de l'éducation`**.
  ⚠️ Le même ouvrage est cité **إميل أو في التربيّة** au سند 14 (p.373) et **أميل أو التربية** ici
  (p.394) — deux graphies **et** deux traductions du titre dans le même مبحث. Signalé, non corrigé.
  *Thèse du passage* : **« ضعيف » et « قوي » ne sont pas des propriétés mais des rapports**
  (نسبة) — le rapport entre la puissance d'un être et ses besoins. Est **fort** celui dont la
  force excède les besoins, « **ولو كان حشرة أو دودة** » ; est **faible** celui dont les besoins
  excèdent la force, « **ولو كان فيلا أو أسدا أو فاتحا أو بطلا أو إلها** ». Le manuel imprime
  l'exemple contrasté du **الملك العاصي الذي أنكر طبيعته**, plus faible que **الفاني السّعيد
  الذي يعيش مطمئنّا وفق طبيعته**. Formule pivot citée verbatim :
  > « **ويكون الإنسان قويّا جدّا إذا ما رضي بما هو عليه، ويكون ضعيفا جدّا إذا ما أراد أن يعلو
  > الإنسانيّة** ».

  Conséquence pratique tirée dans le texte : « **ولذا لا تظنّوا أنّكم تزيدون قوّاتكم بزيادة
  طاقاتكم، وعلى العكس تقلّلونها إذا ما زاد زهوكم** » ⇒ le conseil **ولنـنقص قطر دائرتنا، ولنبق
  في المركز كالحشرة في وسط نسيجها** ; alors « **سنكون من الكفاية ما نقضي معه حاجاتنا، ولا يكون
  لدينا من الأسباب ما نتوجّع معه من ضعف، وذلك لأنّنا لن نشعر به مطلقا** ».

  *Concepts mobilisés par le support* (c'est ce que l'exercice fait chercher) : **الضّعف · القوّة
  · النسبة · الحاجة · الطاقة · الطبيعة · السّعادة · الزهو · الإنسانيّة**.
- **المهام (verbatim, 6 consignes)** :
  1. أرصد **المفاهيم الواردة في النص**.
  2. أتبين **العلاقات المنطقيّة القائمة بينها**.
  3. أستأنس **بالأمثلة للمقارنة بينها**.
  4. أستخلص **المفهوم المحوري الذي تنشدّ إليه كل هذه المفاهيم**.
  5. **أحدّد دلالته**.
  6. أتبيّن **طرافته بالمقارنة مع دلالته السائدة**.

###### تمرين 2 — p.394-395

- **المهارة المستهدفة** : **اتّخاذ موقف من قضيّة خلافيّة**.
- **القضية (verbatim)** : « **متى أكون سعيدا** ؟ »
- **توضيح (encadré de méthode, p.394, verbatim, intégral)** :
  > **تقتضي هذه المهارة** :
  > – **تحديد موقف من القضيّة.**
  > – **تقديم بعض الحجج الداعمة لهذا الموقف.**
  > – **استحضار بعض الاعتراضات الممكنة.**
  > – **بيان ما يمكّن من تجاوز هذه الاعتراضات.**
- **التمشّيات (p.395, verbatim — 4 étapes, chacune dans sa propre boîte)** :
  1. **أحدّد دلالة السّعادة وأبيّن شروط إمكان تحقّقها.**
  2. **أسوق بعض الحجج التي تدعم هذه الدلالة.**
  3. **أستحضر بعض الاعتراضات على هذا الموقف وأردّ عليها واحدا واحدا**
     `[sic — pas de point final imprimé]`
  4. **أستخلص ما يمثّل طرافة في الموقف الذي اتخذته.**

###### تمرين 3 — p.395

- **المهارة المستهدفة** : **تحديد الرهان من وراء التفكير في مسألة**.
- **المسألة (verbatim)** : « **هل تكمن أخلاقيّة أفعالي في اتّباع القيم الاجتماعيّة ؟** »
- **توضيح (encadré de méthode, verbatim, intégral — 2 entrées à astérisque)** :
  > \* **الرهان** هو **الخطورة والأهمية** التي يكتسيها **التفكير في مشكل ما**، وما **للموقف الذي
  > سنتخذه منه من طابع حاسم ومصيري** سواء على مستوى **نظري** أو **عملي**.
  > \* يتعلق **بالتبعات النظرية والعملية** الني `[sic — pour « التي »]` يمكن أن يؤول إليها
  > التفكير في هذا المشكل **وانعكاساته المحتملة والمصيرية سياسيا وأخلاقيّا** على مجرى الحياة
  > الواقعية.

  ⇒ Définition officielle du **رهان** : la *gravité* et l'*importance* que prend le fait de
  penser un problème, plus le caractère **décisif et déterminant (حاسم ومصيري)** de la position
  qu'on y prendra, sur le plan **théorique** comme **pratique**.
- **المهام (verbatim, 5 consignes — les 4 dernières sont des questions)** :
  1. **أحدّد الأجوبة المحتملة عن هذا السؤال.**
  2. **أيّة خطورة يمكن أن تترتّب على هذه الأجوبة المحتملة ؟**
  3. **ما صورة المجتمع التي تفترضها هذه الأجوبة ؟**
  4. **هل من شروط سياسيّة تلزم عن هذه الأجوبة ؟**
  5. **ماذا يحصل لو عملت الإنسانيّة جمعاء بجواب من هذه الأجوبة ؟**

###### تمرين 4 — p.396

- **المهارة المستهدفة** : **القدرة على التأليف**.
- ⚠️ **Pas d'encadré `توضيح`** ici : le cartouche **المهمّة** en tient lieu.
- **المهمّة (verbatim)** :
  > **هل نحتاج إلى قيم كونيّة ؟**
  > أجيب عن هذا السؤال في **فقرة لا تتجاوز العشرين سطرا** متبعا في ذلك **التمشيات المصاحبة**.
- **التمشّيات — la méthode de rédaction en 3 مراحل, chacune dans un cartouche orange arrondi
  (verbatim)** :

  **■ مرحلة بناء المشكل**
  - أبيّن **ما يبرر معالجة هذا السؤال**.
  - أشير إلى **أهميّة السؤال**.
  - أستخلص **مشكلا فلسفيّا أصوغه بوضوح**.

  **■ مرحلة بلورة الجواب**
  - أبيّن **دلالة القول بالحاجة إلى قيم كونيّة**.
  - أستحضر **بعض المؤيّدات** ( **تقديم حجة على الأقل** ).
  - **أعترض عليه ببيان حدود وجاهته** ( **من خلال الكشف عن ضمنية أو استتباع أو تناقض مع الواقع** ).
  - **أقترح بديلا وأوضّحه.**
  - **أستدل على وجاهته.**

  **■ مرحلة الاستخلاص**
  - **أستخلص الموقف النهائي.**
  - **أشير إلى قيمته.**

⚠️ **Le gabarit des 3 مراحل est exactement celui du مبحث 2 (p.263)** — mêmes intitulés d'étapes,
même découpage. Seul le contenu de la 2ᵉ étape change (là-bas : النمذجة / الكوني ; ici : les
valeurs universelles) — et il s'y ajoute ici deux consignes que le مبحث 2 n'avait pas :
**أقترح بديلا وأوضّحه** et **أستدل على وجاهته**.

##### 3.2.4 نافذة نصّ مطوّل — نيتشه : أفول الأصنام — p.397-401

**Page d'ouverture (p.397)** — bandeau « نافذة / نصّ مطوّل ». Illustrations : enluminure de mains
feuilletant un livre d'heures ; **couverture du livre** reproduite — `NIETZSCHE` / **فريدريك نيتشه**,
**أفول الأصنام**, ترجمة **حسان بورقيّة** و **محمد الناجي**, éditions **أفريقيا الشرق** ; portrait
photographique de Nietzsche. Légendes : « ▲ أفول الأصنام » et « ▶ **نيتشه (1844-1900)** `NIETZSCHE` ».

**Encadré-citation (p.397, verbatim)** :

> لا يمكن أن نظلّ " شبابا " إلاّ شريطة ألاّ تخلد النّفس للرّاحة، ألاّ يشدّها الشّوق إلى
> الطمأنينة… لا شيء أغرب علينا مما كان يبدو جدّ مطلوب فيما مضى: طمأنينة النّفس
> — **نيتشه**

> ➡️ Le titre annoncé par le فهرس, le corps du texte, sa structure argumentative et la question du
> questionnaire d'accompagnement sont traités dans la section suivante (p.398-401).

###### Le texte de نيتشه — p.398-401 (corps, structure argumentative)

**Titre imprimé en tête de page** : **أفول الأصنام** (en rouge), et en regard, à gauche :
**الأخلاق فضيلة مضادّة**.
✅ Le titre annoncé par le فهرس est **confirmé sur la page**.

**Encadré de référence (p.398, verbatim)** :

> ترجمة
> **حسّان بورقية** — **محمد الناجي**
> **أفريقيا الشرق**
> **الدار البيضاء، ص 35-43**

⚠️ **Droits (R-2)** : le texte de Nietzsche n'est **pas** reproduit ici. Il est restitué par le
**découpage que le manuel imprime lui-même** — 6 sections numérotées et 14 repères marginaux — plus
de courtes citations attribuées.

**Dispositif de lecture** (constaté, identique à celui du مبحث 2) : texte continu **numéroté de 5
en 5 lignes** (l.1 à l.135), découpé en **6 sections numérotées** (1 à 6, en rose), et accompagné en
marge de **14 repères** qui explicitent le mouvement de l'argumentation.
⛔ **Aucun questionnaire imprimé** — ni أسئلة ni مهامّ, comme au مبحث 2. Le seul guidage est
constitué des repères marginaux et de la numérotation des lignes.

**Les 14 repères marginaux, verbatim, dans l'ordre** — c'est le découpage officiel de
l'argumentation :

| # | section | repère (verbatim) | lignes |
| --- | --- | --- | --- |
| 1 | 1 | تحديد مبررات إعادة النّظر في الأخلاق: التّصوّر السّلبي للنزوة واعتبارها ضررا. | ~1-10 |
| 2 | 1 | اعتماد المثال لتدعيم هذه المبررات: تأكيد قيام الأخلاق المسيحية على هذه النظرة السلبية للنزوة وإخصاءها. | ~10-18 |
| 3 | 1 | بيان موجبات الموقف الإستئصالي للنزوة. | ~18-23 |
| 4 | 2 | بيان قيمة هذا الموقف من خلال تقييمه وبيان أصل قيمته وقيمة هذا الأصل. | ~25-40 |
| 5 | 3 | تحديد دلالة الرّوحنة الشبقية على أنّها حبّ. | ~41-50 |
| 6 | 3 | تأكيد إيجابيّة الموقف السلبي من النّزوة من جهة كونه أساسا يشرّع النقد ويجعله أكثر خصوبة. | ~53-66 |
| 7 | 3-4 | تقديم أمثلة على أنّ المثل الأعلى الزّهدي يقوم على وهم وسوء فهم للحياة. | ~67-75 |
| 8 | 4 | تقديم دلالة نقيض للطمأنينة تتمثّل في أنّها تتحقق في الاستجابة للنزوات. | ~75-77 |
| 9 | 4 | النظر إلى فكرة الواجب بما هو عائق عبر بيان التناقض بين الموقف الأخلاقي وغرائز الحياة. | ~82-87 |
| 10 | 5 | تأكيد عقم الموقف الأخلاقي بالنظر إلى قيامه على شروط تضاد الحياة. | ~90-103 |
| 11 | 5 | تأكيد موقف الكاتب بأنّ الأخلاق طبيعة مضادّة للحياة وللإنسان. | ~100-103 |
| 12 | 6 | استخلاص سذاجة أخلاق الواجب. | ~110-120 |
| 13 | 6 | التأكيد على أنّ أخلاق الواجب تفصح عن عرض مرضي نقيض الحياة. | ~120-130 |
| 14 | 6 | الانتهاء إلى تثمين الموقف اللاأخلاقي من جهة انحيازه إلى الإنسان والحياة. | ~135 |

> ⚠️ **14 repères** après recomptage sur les quatre pages (p.398 en porte 4, p.399 deux,
> p.400 cinq, p.401 trois). Le décompte fait foi sur les pages, pas sur une attente de
> régularité.

**Le mouvement d'ensemble (reformulé)** : Nietzsche part du **procédé** de la morale à l'égard des
passions (النزوات) — l'Église ne les *spiritualise* pas, elle les **extirpe** (استئصال), et
« attaquer les passions à la racine, c'est attaquer la vie à la racine » ; sa pratique est donc
**hostile à la vie**. Il montre ensuite que ce remède radical n'est nécessaire qu'aux **dégénérés**,
aux volontés trop faibles pour se modérer. Il oppose à cela la **spiritualisation de la sensualité**
— nommée **amour** — et la spiritualisation de l'**inimitié**, qui fait comprendre la valeur d'avoir
des ennemis : l'Église a toujours voulu détruire ses ennemis, là où « nous, les immoralistes »,
trouvons notre avantage à ce qu'elle subsiste. De là une critique de la « **paix de l'âme** »
(طمأنينة النفس), dont il énumère les visages possibles — souvent un simple malentendu, parfois la
fatigue, la satiété, ou la sécheresse. Puis vient la thèse centrale : toute morale saine est régie
par un **instinct de vie**, tandis que la **morale contre-nature** (الأخلاق المضادّة للطبيعة), celle
qu'on enseigne et vénère, se tourne **contre** les instincts de vie et les condamne. Enfin il
retourne l'accusation : condamner la vie n'est jamais qu'un **symptôme** d'une certaine sorte de
vie — celle qui décline, s'affaiblit, se lasse — et la morale du devoir, en disant à l'homme
« sois ainsi », est une **naïveté**, puisque la réalité offre une profusion inouïe de types et de
formes. « Nous, les immoralistes, sommes la réponse à cette question. »

**Citations courtes, attribuées** (verbatim, extraites du texte imprimé) :

- « إنّ مهاجمة النّزوات من الجذر تعني مهاجمة الحياة من الجذر، إنّ براكسيس الكنيسة معاد للحياة. » (l.22-23)
- « الأخلاق المضادّة للطبيعة، أي تقريبا الأخلاق الملقّنة، الممجّدة، المنصوح بها إلى هذا اليوم، تسير، على العكس تماما، ضدّ غرائز الحياة. » (l.81-83)
- « إنّنا نحن، نحن اللاأخلاقيين، هم الجواب عن هذا السؤال… » (l.135, dernière ligne)

**Noms cités dans le texte** : المسيحية · الكنيسة · العهد الجديد · موعظة على الجبل · براكسيس ·
الشيطان · **شوبنهاور** (l.105) · مملكة الرّبّ.

> ✅ **FIN DU مبحث 3.2 ET DU CORPS DU MANUEL.** La p.402 porte les مختصرات (déjà transcrites) ;
> p.403 est blanche ou non paginée ; le فهرس occupe p.404-408.
> ✅ **Le محور 3 est intégralement transcrit** : مبحث 3.1 (p.271-346) et مبحث 3.2 (p.347-402).

##### 3.2.5 مختصرات — p.402

> **Page lue** : p.402 (intégral). **Récapitulatif officiel du مبحث — reproduit verbatim**, dans
> l'ordre des **5** encadrés imprimés. Illustration : plume d'oie noire sur un manuscrit ancien
> (même vignette que les مختصرات du مبحث 2, p.270).

**■ Encadré 1 — le cadre : l'existence humaine est chargée de valeurs**

> تبيّن لي أن الوجود الإنساني مثقل **بالقيم**، وأنّ صورة الإنسان تظل مبتورة ما لم نقاربها من جهة
> **الوجود الأخلاقي**. وأدركت أن هذا الوجود يقوم على جملة نقائض: **الخير والشرّ**، النافع والضار،
> اللذة والألم، الفضيلة والرّذيلة، السعادة والشقاء…، وهو ما يؤكد جدارة هذا المبحث بالنظر سواء من
> جهة صلته بالإنسان أو من جهة التباس بنية معانيه.

**■ Encadré 2 — الأخلاق et la فضيلة comme juste milieu**

> تبينت أنّ الحديث عن **الأخلاق** يقترن بالحديث عن مطلب **الفضيلة** بما هي استعداد يكتسب
> **إراديّا**، وتقوم على مبدأ الوسط **العدل** الذي لا يقبل إفراطا ولا تفريطا، وأنّ الإنسان الفاضل
> تبعا لذلك هو الذي يحتكم في سلوكه إلى مطلب حفظ كيانه بالتوافق مع ما يمليه **العقل** أي وفقا
> لطبيعته الخاصة.

**■ Encadré 3 — الخير, concept central et litigieux**

> أدركت أنّ **الخير** هو المفهوم المركزي الذي يدور حوله النظر في الأخلاق، وتبيّن لي أنّ لهذا
> المفهوم من الالتباس ما يجعله مثيرا لجدل بين منظّري الأخلاق: بين اعتباره يتماهى مع **المنفعة** مع
> ما يثيره هذا المفهوم من جدل في علاقته بالأخلاقي، واعتباره مبدأ أو غاية في ذاته، مادام الإنسان
> وكلّ كائن عاقل بوجه عام يوجد **كهدف** في ذاته لا كمجرّد وسيلة.

**■ Encadré 4 — الواجب : contrainte externe ou principe intérieur**

> تبينت أن التساؤل عن أساس الفعل الأخلاقي وطبيعته يقتضي استحضار مفهوم **الواجب** الذي قد يقترن
> بمعاني الإلزام والقهريّة بالنظر إلى أساسه الاجتماعي المتعالي والخارجي عن الذّات، مثلما قد ينظر
> إليه بما هو **مبدأ ذاتي** يتأصل ذاتيا، يكون معه الأمر الأخلاقي قطعيا، ولا تتعارض طاعته مع حريّة
> الإنسان واستقلاليّة إرادته، ليستحيل **الإلزام** التزاما والخضوع طاعة والنفور إرادة، مادامت
> الذات هي المشرّعة للواجب، ومادام هذا التشريع يتّخذ من الإنسان غاية قصوى.

**■ Encadré 5 — السّعادة, valeur morale aux sens enchevêtrés**

> أدركت أن **السّعادة** قيمة أخلاقيّة تتداخل في معناها مع معاني الخير والفضيلة واللذة والمنفعة
> بحسب تعدد زوايا النظر وطبيعة المقاربات، إذ قد ينظر إليها بما هي **خير أسمى**، كما قد تفيد معنى
> تحقيق **اللذة** وتجنب الألم، دون أن يحمل هذا المعنى على طلب اللذّة أو تجنّب الألم بكل السبل، أو
> دون أن تفهم السّعادة على معنى الإطلاقية، إذ لا نعرف سعادة مطلقة أو شقاء مطلقا.

> ⚠️ **Cinq encadrés**, et non six comme au مبحث 2 — le nombre n'est pas un invariant du gabarit.
> ✅ **Fin du corps du manuel** : p.402 est la dernière page de contenu ; le فهرس occupe p.404-408.

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
    page, le 10 déborde sur p.238–239 ; les سندات 2, 11, 12, 13 et 16 n'ont **aucun** encadré هامش.
- **Quatre notices d'auteur sont des renvois** à un autre سند (10→7, 13→9, 14→7, et le هامش 3 du
  سند 14→11) : la génération devra les résoudre plutôt que de les citer telles quelles.
- `[?]` p.245 : portrait non légendé sur un texte à deux voix (فانفلي / لوموانيو) — attribution
  indéterminable. `[sic]` relevés : « الأنساق العلامات » (p.228) et la pagination `pp 521-621`
  de René Thom (p.241), tous deux confirmés à 300 dpi ; « Karl POPER » avec un seul P (p.264) ;
  `Van Frassen`, `Maxwel`, « أكتشف », « البشرى », « هيّ ».
- ✅ **R-7 FAITE sur le مبحث 2 — 2026-08-13, portée INTÉGRALE (56/56 pages).** Relecture
  indépendante, contexte vierge, **contre les images du PDF**. Le protocole T-8 prévoyait un
  sondage (≥15 %) ; le relecteur a collationné **41 pages mot à mot** et vérifié les **15 autres**
  au niveau thèse/référence/non-invention, plus 22 re-rendus 300–900 dpi sur les zones douteuses.
  **Verdict : 3 constats substantiels, 5 écarts de fidélité verbatim, 10 constats de forme — les
  18 corrigés.** Le seuil d'escalade (≥3 substantiels) était atteint, mais la relecture intégrale
  qu'il déclenche **avait déjà été faite dans la même passe** : la liste est exhaustive.

  Les 3 substantiels, tous **revérifiés sur la page par l'orchestrateur avant application** (la
  correction prescrite peut elle-même être fautive) :
  1. **p.226 entièrement manquante** — le سند 3 (كارناب) n'avait ni ses 2 هوامش, ni sa notice
     d'auteur, ni ses 6 مهامّ, ni son encadré-citation, alors que la page était déclarée lue.
     **Omission, désormais comblée.**
  2. **p.240, contresens** — la fiche disait « il est difficile d'expliquer ce que veut dire le
     modèle scientifique » ; la page imprime « **ليس من الصّعب** » — *il n'est **pas** difficile*.
     La négation était tombée : le sens était **inversé**.
  3. **p.233, détail inventé** — « équation périodique **du second ordre** » n'est pas imprimé ;
     la page dit « معادلة دوريّة **فوقية مخصوصة التعقيد** ».

  Ce que la R-7 a **confirmé sans écart** : les 16 lignes du tableau des سندات (auteur, titre,
  pages), les 2 تحديدات avec leur gabarit et leurs 6 citations « قيل في … », les 6 مختصرات, les 4
  encadrés توضيح, les 15 repères marginaux du نصّ مطوّل, la numérotation des نوافذ, l'absence de
  chiffres arabo-indiens, et la conformité **R-2** (aucun texte de سند recopié).

  ⚠️ Le statut reste **`partielle`** malgré la R-7 : elle ne porte que sur le مبحث 2, et 4
  chapitres sur 5 restent en ossature. `validee-r7` supposerait la fiche entière.

- **Contrôle par sondage de l'orchestrateur — ce n'est PAS une R-7.** Faute de pouvoir lancer la
  relecture indépendante, 5 pages ont été re-vérifiées **contre les images du PDF** par
  l'orchestrateur. Ce contrôle ne vaut pas R-7 pour deux raisons qu'il faut garder en tête : son
  contexte **n'est pas vierge** (il a lu les rapports des transcripteurs) et l'échantillon — 5
  pages sur 56, ~9 % — est **sous le seuil T-8** (100 % du critique + ≥15 % du reste).
  Résultat : **5 vérifications, 0 erreur.**
  - p.237 — سند 9 : titre « كيف ينشأ النموذج؟ », auteur imprimé **هانز فرودونتال**, référence
    latine `Hans FREUDENTHAL, La sémantique du terme modèle, Paris 1978, pp 159-160`, et le سند
    tient bien **sur une seule page** (تمهيد + texte + الكاتب + المهام), **sans encadré هامش**.
    ✅ conforme, y compris la troisième graphie du nom.
  - p.255 — البراديغم s'étend bien jusqu'à p.255, avec la rubrique **قيل في البراديغم**
    (توماس كوهن, رولان أومناس) et l'encadré **لمزيد التعمّق**. ✅ conforme : le فهرس était bien
    inexact, pas la fiche.
  - p.264 — **`Karl POPER`** est bien imprimé avec **un seul P** (le `[sic]` est justifié) ;
    la page ne porte **aucun questionnaire** ; la couverture reproduite indique
    **عالم المعرفة n° 292 · أبريل/مايو · 2003**. ✅ conforme — le millésime 2003 a été reconfirmé
    à 400 dpi après un doute de lecture à 150 dpi.
  - p.270 — les **6 encadrés de مختصرات** sont bien au nombre de 6. ✅ conforme.
  Ce que ce contrôle **ne dit rien** de : les 13 autres سندات, les thèses reformulées, le gabarit
  لغة/اصطلاحا/فلسفيا des تحديدات, les سياقات فكريّة et les 4 exercices de كيفيّات التفكير.

  > 📌 **Ce que la R-7 a montré ensuite — à retenir pour les prochains chapitres.** Ce contrôle de
  > 5 pages n'a vu **aucun** des 3 constats substantiels que la R-7 a trouvés huit jours plus tard
  > (page entière manquante, contresens par négation tombée, détail inventé). Il n'était pourtant
  > pas bâclé : il était **au mauvais endroit** — il a re-vérifié des faits déjà signalés par les
  > transcripteurs, c'est-à-dire précisément ce qu'ils avaient regardé. Un relecteur en contexte
  > non vierge cherche là où on lui a dit de chercher ; c'est exactement ce que R-7 est faite pour
  > éviter. **Un contrôle d'orchestrateur ne remplace pas une R-7 — il en donne l'illusion.**
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
