# العربية / Arabe — 2ème année secondaire, section Lettres (شعبة الآداب) · programme officiel CNP

> **Sources** (manuel élève seul — **pas de guide enseignant au corpus** pour ce couple matière/niveau) :
>
> - **Manuel élève, tome 1** : « **عيون الأدب — لتلاميذ السنة الثانية من التعليم الثانوي — الجزء الأوّل** »
>   (الجمهوريّة التّونسيّة، وزارة التّربية، المركز الوطني البيداغوجي). **تأليف** : منية قاره بيبان (متفقّدة أولى
>   للمدارس الإعداديّة والمعاهد)، سامي الرحموني (متفقد المدارس الإعداديّة والمعاهد)، مجيد الشارني (متفقد أوّل
>   للمدارس الإعداديّة والمعاهد)، محمد المومني (مدرّس مبرّز). **تقويم** : الهادي بوحوش، الصّادق بن عمران (متفقّدان
>   عامّان للتربية). Fichier `201202P00.pdf` — **256 pages**. **Pages lues** : voir §6.
> - **Manuel élève, tome 2** : même titre, « **الجزء الثّاني** » (mêmes auteurs/évaluateurs/éditeur).
>   Fichier `201203P00.pdf` — **288 pages**. **Pages lues** : voir §6.
>
> **Transcrit le** : 2026-07-30. **Chapitrage re-grainé le** : 2026-07-30. **Statut** : transcription fidèle
> **partielle** — **le seul المحور الأوّل (الشّعر الجاهلي, tome 1, p.5–83) est transcrit à profondeur de**
> **génération** (chaque texte, chaque rubrique du جهاز البيداغوجي, encadrés et ورقات منهجيّة verbatim, bornes
> ✅/⛔) ; il porte à lui seul **5 des 13 chapitres** du chapitrage (§4), un par **ورقة منهجيّة**. Les **8 autres
> chapitres sont codifiés au chapitrage (§4) avec leurs bornes de pages CONSTATÉES**, mais **non encore
> transcrits** — fiche **reprenable** (cf. registre `suivi/2eme-sec-lettres.json`, LA source de vérité de la
> couverture).
> ⚠️ **Génération (LOT B) RESTREINTE** : R-5 se lisant **au chapitre** depuis la décision du 2026-07-29, les
> **seuls chapitres `01-gharad-shiri`, `02-gharad-fakhr`, `03-gharad-madh`, `04-gharad-ritha` et
> `05-gharad-ghazal` sont générables** — ce sont les cinq chapitres du محور الأوّل, dont la transcription est
> déjà à profondeur de génération ; les 8 autres restent interdits tant que leur section n'est pas transcrite.
> La liste fait foi dans `chapitresGeneration` du registre, et `programme:check` la vérifie contre le
> chapitrage du manifeste.
>
> **Langue CONSTATÉE** : **arabe** (page de titre, corps du manuel, appareil pédagogique — intégralement en
> arabe ; conforme à `docs/lycee-architecture.md` §4). **gradeSlug** : `2eme-sec-lettres`.
> **subject id** attendu : `arabic-2eme-sec-lettres`.
>
> ⚠️ **Manuel PARTIELLEMENT sectionné — fait vérifié, à retenir avant toute réutilisation.** Le manuel n'est
> **pas dédoublé par شعبة au catalogue CNP** — un seul code par tome (`201202`, `201203`), contrairement à
> l'histoire (`207202` « شعبتي الآداب و الاقتصاد والخدمات » vs `207271` « شعبتي العلوم و تكنولوجيا الإعلاميّة »)
> et à la géographie (`206203` vs `206271`) — et **sa page de titre ne mentionne aucune شعبة** (« لتلاميذ السنة
> الثانية من التعليم الثانوي », sans plus). **Mais** le tome 2 porte **deux محاور خامس explicitement
> sectionnés dans leur titre même** (relevés au فهرس p.285–286 et sur les pages de garde p.102 et p.174) :
>
> - « **المحور الخامس (المسلك الآداب) : من أشكال القصّ العربيّ الحديث : الرّواية** » — p.102–173
>   (نجيب محفوظ، خان الخليلي) → **c'est celui de cette fiche** ;
> - « **المحور الخامس (المسلك : العلوم/تكنولوجيا الإعلاميّة/الاقتصاد والخدمات) : النصّ المسرحي : بجماليون للحكيم** »
>   — p.174–237 → **hors scope de la section Lettres** (⛔ voir §4).
>
> **Conséquence** : les محاور 1 à 4, le التواصل الشفويّ et les ورقات لغويّة sont **communs aux quatre sections
> de 2ème sec** ; seul le محور 5 diverge. Le chapitrage étant donc **structurellement** différent d'une section
> à l'autre, `docs/lycee-architecture.md` §2 impose des **répertoires de contenu séparés dès le départ**
> (pas de `compileTo`). ⚠️ Côté registre, une source ne peut être revendiquée que par **une** fiche (R-4) :
> une future fiche `2eme-sec-eco-services`/`2eme-sec-info` devra **renvoyer à celle-ci** (ou citer les tomes
> en `sourcesLibres`), jamais revendiquer `201202`/`201203`.

## 1. Cadre & compétences (المقدّمة, tome 1 p.3–4 et tome 2 p.3–4 — texte identique)

Le manuel ne comporte **aucun cadre de compétences formalisé** (pas de « الكفاية المستهدفة » ni de
« المعايير » : c'est le rôle du guide enseignant, **absent du corpus**). Les finalités sont portées par la
**مقدّمة**, adressée à l'élève et signée « المؤلِّفون ». Elle annonce deux blocs (marqués par un astérisque) :

- **« طبيعة المادّة »** — l'arabe y est présenté comme une branche du champ des langues, « ينعقد على التّواصل
  مهارة لا تمام لها إلاّ بالقراءة والكتابة والمشافهة » : un **ثالوث** de trois compétences dont la structure du
  manuel est le décalque —
  - **مهارة القراءة** : « انتقاء لمنتخبات من عيون أدبنا العربيّ قديمه وحديثه منظومه ومنثوره » — d'où le titre du
    manuel (« لعلّه السرّ الأوّل في تسمية الكتاب ») ; منتخبات voulues « وفيّةً لأهداف البرنامج مستجيبةً لما
    تحتاجان إليه في مثل هذه السنّ محترمةً لما حصل لديكما من مكتسبات ».
  - **مهارة الكتابة** : « حاضرة في جلّ نصوص الكتاب الأدبيّة إن لم نقل كلّها » via des activités « تستدعي التدوين
    وتتطلّب الفهم والتّفكيك والتّصميم فالتّحرير », et via les **ورقات منهجيّة**, à double visée : donner « مفاتيح
    للقراءة » (approches أغراضيّة / أجناسيّة / تاريخيّة / أدبيّة عامّة) et faire acquérir « آليّات في التحليل يُبنى
    بها التّحرير » — nommément « **التحليلَ الأدبيَّ والمقالَ ودراسةَ النصّ** » (les trois exercices scolaires visés).
  - **مهارة التّواصل الشّفويّ** : « المهيمنة على القضايا الحضاريّة », adossée à des supports choisis pour être
    « مدعاة للتّحليل والاختلاف في المواقف », dans le respect de « آداب الحوار ومقتضياته » et d'un « استعمال سليم
    للّسان العربي ». Cet objectif est prolongé par les **ورقات لغويّة**, « منطلقا وحصيلة » des leçons de langue,
    pour « مزيد التمكّن من نظام لغتنا العربيّة وآليّاتها النّظميّة ».
- **« أهداف المادّة »** — « تأصيل المتعلّم في هويّته الحضاريّة، والإسهام في نحت شخصيّته نحتا ينبذ التعصّب
  والانغلاق ويؤمن بالانفتاح الخلاّق على الآخر وثقافته، وتمكينه من الأدوات المنهجيّة والفكريّة التي تجعله
  "يتعلّم كيف يتعلّم" ».

La مقدّمة précise aussi que le manuel « ينتسب إلى جيل جديد من البرامج » et qu'il est « **مسار أوّل من مسارات
عِشرة** » (premier volume d'une série qui accompagne l'élève au-delà de l'année).

**Le جهاز البيداغوجي est explicitement décrit** dans la مقدّمة (tome 1 p.4) comme une progression en cinq
temps, et c'est **exactement** l'appareil qui encadre chaque texte du manuel (§3) : « تذليل صعوبات المعجم »
(→ rubrique `اعرف`, « منطلقه ردّ الكلمة إلى جذرها فصيغتها وحضورها القاموسيّ والسّياقيّ في النصّ ») → « الحفز على
التفكيك مرحلة تأسيسيّة » (→ `فكّك`) → « الدّعوة إلى تحليل لا تُدرك فيه دلالات النصّ ومقاصده إلّا بالانطلاق من
مبانيه » (→ `حلّل`) → « التّقويم مرقى عرفانيّا » (→ `قوّم`) → « التوسّع سبيلا لتجاوز النصّ وتوسيع آفاق القراءة »
(→ `توسّع`).

## 2. Plan annuel (المخطّط السّنوي)

⚠️ **Aucune répartition annuelle ou trimestrielle (توزيع سنوي / ثلاثي) n'est imprimée dans les deux tomes**
(vérifié sur les pages liminaires p.1–8 des deux tomes, et sur les 4 pages de la مقدّمة). Le manuel ne fournit
qu'un **ordre** — celui des محاور — et pas un calendrier. Le séquençage trimestriel devra venir d'une source
externe (guide enseignant absent du corpus, ou fichiers école).

La structure annuelle **constatée** est donc :

| ordre | unité                                                                         | tome | pages       |
| ----- | ----------------------------------------------------------------------------- | ---- | ----------- |
| 1     | المحور الأوّل : الشّعر الجاهلي                                                | 1    | p.5–83      |
| 2     | المحور الثاني : التجديد في الشّعر العربيّ في القرن الثاني للهجرة              | 1    | p.85–173    |
| 3     | المحور الثالث : من أشكال القصّ في الأدب العربيّ القديم — النّـادرة            | 1    | p.174–222   |
| 4     | التواصل الشفويّ (1)                                                           | 1    | p.223–241   |
| 5     | ورقات لغويّة (1)                                                              | 1    | p.242–252   |
| 6     | المحور الرابع : الرّومنطيقيّة في الأدب العربيّ                                | 2    | p.5–101     |
| 7     | المحور الخامس **(المسلك الآداب)** : الرّواية — خان الخليلي                    | 2    | p.102–173   |
| —     | _(المحور الخامس المسلك العلوم/تكنولوجيا/الاقتصاد : بجماليون — ⛔ HORS SCOPE)_ | 2    | _p.174–237_ |
| 8     | التواصل الشفويّ (2)                                                           | 2    | p.238–265   |
| 9     | دلالات الصيغ الصرفيّة (ورقات لغويّة 2)                                        | 2    | p.266–283   |

⚠️ **Cette table est l'ordre des UNITÉS du manuel (9), pas le chapitrage (13).** Depuis la décision du
2026-07-30, l'unité 1 (المحور الأوّل, 79 pages et 16 نصوص مختارة) est éclatée en **cinq chapitres, un par
ورقة منهجيّة** — voir §4, qui est la seule table à faire foi pour `manifest/2eme-sec-lettres.json`.

Chaque محور suit rigoureusement le même montage (constaté sur les cinq محاور) : **page de titre** →
**فهرس المحور** (tableau à 3 colonnes : `ترتيب النّصوص` · `العنوان` · `مراكز الاهتمام`, **sans numéros de page**)
→ garde « **نصوص تمهيديّة** » puis les textes introductifs (critique/histoire littéraire, chacun clos par un
encadré `مراكز الاهتمام`) → garde « **نصوص مختارة** » puis les textes littéraires, chacun avec l'appareil complet
(§3) et entrecoupés de **ورقات منهجيّة** « كيف أقرأ : … » → garde « **نصوص تكميليّة** » puis les textes
complémentaires (critique moderne, `مراكز الاهتمام`) → **ثبت بيبليوغرافي** de clôture.

## 3. Notes pédagogiques / méthode (démarche constatée dans le manuel)

**Appareil attaché à CHAQUE texte choisi** (relevé identique sur les 16 textes du محور 1) :

1. **`تمهيد`** — encadré d'entrée en matière : contexte historique/biographique ou citation d'un critique
   ancien, avec sa référence. C'est lui qui installe le pacte de lecture du texte.
2. **`اعرف`** — élucidation lexicale, en sous-rubriques : **`الأعلام`** (personnes), **`الأماكن`** (toponymes,
   quand il y en a), **`الشـرح`** (glossaire mot → glose, numéroté et renvoyant aux appels du poème ;
   4 à 20 entrées par texte). Conforme à la مقدّمة : la glose part du **جذر** puis de la **صيغة**.
3. **`فكّـك`** — consignes de segmentation du texte (découper en unités, repérer les articulations,
   nommer les mouvements) : la « مرحلة تأسيسيّة » annoncée.
4. **`حلّـل`** — 2 à 5 consignes d'analyse, toujours **adossées aux « مباني »** (lexique, champs sémantiques,
   syntaxe, images, rythme) avant la « دلالة ».
5. **`قـوّم`** — une consigne d'évaluation/jugement (souvent : discuter une thèse, apprécier une valeur).
6. **`توسّـع`** — élargissement : comparaison avec un autre texte, tableau à compléter (appariement de
   proverbes p.48, tableaux de sens p.62/p.68), recherche documentaire.
7. **`إضاءات`** — encadré de langue/rhétorique : un fait de langue ou une figure relevée dans le texte
   (ex. `الالتفات` p.58 ; `ردّ الأعجاز على الصدور`, `الجناس` p.64 ; `لا أبا لك`, `الإيجاز` p.71) ; parfois un
   **tableau de تقطيع** (scansion : p.75, sur le vers 4 — 4 colonnes segment / schéma / تفعيلة / grammaire).
   Ailleurs le تقطيع est **demandé sans corrigé**, en consigne de `توسّع` (p.24, p.54, p.71).
8. **`شذرات`** — citation critique de clôture (ancienne ou moderne), avec référence complète
   (ابن رشيق، العمدة ; قدامة بن جعفر، نقد الشعر ; أبو هلال العسكري، ديوان المعاني ; طه حسين ; ريجيس بلاشير ;
   توفيق بكار ; حسين الواد ; وهب أحمد روميّة ; كمال أبو ديب ; أدونيس).

**ورقات منهجيّة** — intercalées entre les textes, toutes titrées « **كيف أقـرأ : …** », bâties sur le même
gabarit : **حدّ الغرض** (définition du genre/غرض) + un ou deux **tableaux `مراكز الاهتمام`** (motifs regroupés
par familles, étiquetées verticalement) + une liste de **`وظائف`** (fonctions du غرض). Celles du محور 1 :
`الغرض الشعريّ` (p.34), `غرض الفخر` (p.44), `غرض المدح` (p.52), `غرض الرثاء` (p.59), `غرض الغزل` (p.65),
`غرض الهجاء` (p.150 — **محور 2**, et non محور 1 : voir §4, le sort de الهجاء). **Ces cinq ورقات du محور 1 sont
exactement le grain du chapitrage retenu** (§4) : un chapitre par ورقة. Le tome 1 en compte 10, le tome 2 également 10 (فهرس الورقات المنهجيّة,
p.256 et p.287) — celles du tome 2 portent sur le **récit** (المكان، السّرد، الشّخصيّة القصصيّة، الزّمن) et sur le
**théâtre** (النصّ المسرحي، أقسام المسرحيّة، الحوار المسرحيّ، وظائف الحوار، الإشارات الرّكحيّة، الشّخصيّة المسرحيّة).

**Textes تمهيديّة / تكميليّة** — prose critique, sans `اعرف`/`فكّك`/`حلّل`/`قوّم` : ils se closent seulement sur un
encadré **`مراكز الاهتمام`** (3 puces) et portent des **notes de bas de page** référencées. Ils ne sont donc pas
des supports d'exercice de langue mais des apports de savoir (histoire littéraire, théorie de la قصيدة).

**Iconographie** — chaque محور intègre des planches pleine page **légendées et référencées** (cartes
historiques p.7–8 du tome 1 ; مشجّر أنساب القبائل p.17–18 ; peintures : الحبيب بلال p.20, فرانز مارك p.72,
…) recensées dans un **فهرس الرّسوم** en fin de tome (p.256 ; p.288).

**Notation & pièges** — chiffres **occidentaux** dans le manuel comme ici (numéros de vers, de notes, de
pages). Les vers sont imprimés **hémistiche par hémistiche** (صدر / عجُز) : toute restitution doit conserver
la césure. Les textes sont **entièrement vocalisés** (شكل) : la vocalisation est porteuse d'information
(إعراب) et fait partie du texte officiel.

## Chapitres transcrits

Le premier محور du manuel « عيون الأدب » (tome 1, code CNP 201202) couvre les pages 5 à 83 et se compose de **22 textes** répartis en trois sections — **3 نصوص تمهيديّة** (p.10–16, prose critique et historique), **16 نصوص مختارة** (p.22–75, poésie jahilite avec l'appareil pédagogique complet) et **3 نصوص تكميليّة** (p.77–81, prose critique ancienne et moderne) — auxquels s'ajoutent **5 ورقات منهجيّة** intitulées « كيف أقـرأ : … » (p.34, 44, 52, 59, 65). Le montage est régulier : chaque texte مختار porte un mètre (البحر) indiqué entre parenthèses, une référence bibliographique en pied de texte, et un جهاز pédagogique en rubriques fixes — `تمهيد :` → les vers numérotés → `اعرف` (`الأعلام :` / `الأماكن :` / `الشـرح :`) → `فكّك` → `حلّل` → `قوّم` → `توسّع` → `إضاءات` → `شذرات` — annoncé dès l'avant-propos p.4 en cinq termes verbatim : « تذليل صعوبات المعجم » — « الحفز على التفكيك » — « الدّعوة إلى تحليل » — « التّقويم » — « التوسّع ». Les 3 textes تمهيديّة et les 3 textes تكميليّة, eux, n'ont **aucune** rubrique de questions : ils se ferment sur un seul encadré, « مراكز الاهتمام ». Le **فهرس du محور (p.6)** donne pour chaque texte son ordre (« ترتيب النّصوص »), son titre (« العنوان ») et ses « مراكز الاهتمام », mais **aucun numéro de page** : la pagination des textes n'est reconstituable que par parcours du manuel.

> **Grain du chapitrage — décision de Mohamed du 2026-07-30.** Ce محور n'est **pas** un chapitre
> unique : il est éclaté en **cinq chapitres, un par ورقة منهجيّة « كيف أقـرأ »** (p.34, 44, 52, 59, 65) — le découpage que le manuel s'impose à lui-même. Motif : 79 pages et 16 نصوص مختارة en un seul
> chapitre donneraient soit un chapitre démesuré soit un chapitre superficiel, et re-découper **après**
> génération casserait les slugs, qui sont l'identité d'un chapitre (progression élève, répétition
> espacée, tentatives y sont rattachées).
>
> ⚠️ **Le sort de الهجاء.** Le manuel retient **cinq** أغراض — المدح، الفخر، الغزل، الرثاء، **الهجاء**
> (ورقة « الغرض الشعريّ », p.34) — mais seuls **quatre** ont une ورقة منهجيّة dans ce محور. **الهجاء n'en a**
> **pas** : aucun نصّ مختار ne lui est consacré (le فهرس p.6 n'en porte aucun), et sa propre ورقة
> « كيف أقـرأ : غرض الهجاء » se trouve **p.150, dans le محور الثاني** (cf. §3). Il n'y a donc **pas de**
> **6ᵉ chapitre pour الهجاء** : il est nommé — et seulement nommé — là où le manuel le nomme, au chapitre
> **C1** qui porte la ورقة p.34 (liste des cinq أغراض ; « لا تحتاج مداخل استهلاليّة كغرضي الرثاء والهجاء ») et,
> incidemment, dans le `حلّل` 4 du texte 4 p.33 (« بعض المعاني الهجائية ») ; il sera traité au fond dans
> `06-tajdid-shir-qarn-thani`, le chapitre qui contient sa ورقة.
>
> Les cinq sections C1→C5 **redistribuent** la transcription intégrale déjà établie — aucun texte n'est
> réécrit, aucun n'est perdu. Les blocs **transversaux** (Concepts / notions, Vocabulaire officiel,
> Textes & exemples types, Bornes de scope) et le **ثبت بيبليوغرافي** de clôture sont relevés sur
> l'**ensemble** du محور : ils restent groupés en **C1** et valent pour les cinq chapitres.

## C1 Chapitre 1 — المحور الأوّل : الشّعر الجاهلي — الغرض الشعريّ (`01-gharad-shiri`, tome 1, p.5–34 et p.76–83, transcrit à profondeur de génération)

Chapitre de la **notion générale** : ce que le manuel installe avant tout غرض particulier. Il réunit ce
que le manuel place **avant** la première ورقة منهجيّة — l'ouverture du محور (p.5–9, dont le فهرس p.6 et les
deux cartes p.7–8), les **3 نصوص تمهيديّة** (p.10–16) et les planches généalogiques (p.17–18), la garde
« نصوص مختارة » et la notice de طرفة بن العبد (p.19–21), les **4 textes de la معلّقة de طرفة** (p.22–33,
le seul poème lu comme un parcours complet طلل → نسيب → راحلة → فخر → حكمة), puis la **ورقة منهجيّة**
« كيف أقرأ : الغرض الشعريّ » (p.34) qui clôt ce parcours — et, en fin de محور, les **3 نصوص تكميليّة**
(p.76–81) sur la **بنية القصيدة** et le **الرّحيل** ainsi que le **ثبت بيبليوغرافي** (p.82–83). Le
rattachement des تكميليّة ici est **constaté**, non arbitraire : ils portent sur les أقسام القصيدة, sur le
débat ancien/moderne autour de la بنية et sur le هاجس الرّحيل — exactement l'objet de la ورقة p.34 (مداخل
الأغراض، المقدّمات، المقام الشعريّ) — et le `قوّم` du texte 4 (p.33) renvoie nommément l'élève au
« النص التكميلي الأوّل لابن قتيبة ».

- **Montage (fidèle au manuel)** :

  - **Ouverture** (p.5–9) :
    - **p.5** — page de titre du محور (planche décorative) : bandeau bleu « المحــــور الأوّل », sous-titre magenta « الشّعر الجاهليّ ». Aucun texte courant, aucune pagination imprimée. Borne d'ouverture du محور.
    - **p.6** — « فهــرس المحــور الأوّل », bandeau bleu « الشّعر الجاهلي », tableau à 3 colonnes (« ترتيب النّصوص » | « العنوان » | « مراكز الاهتمام ») réparti en trois sections dont les en-têtes sont imprimés « I – النصوص التمهيدية », « II- النصوص المختارة », « III- النصوص التكميليّة ».

      **I – النصوص التمهيدية**

      | N°  | العنوان                   | مراكز الاهتمام                                              |
      | --- | ------------------------- | ----------------------------------------------------------- |
      | 1   | في معنى الجاهليّة         | – مدلول الجاهليّة في المعاجم والقرآن وبعض القراءات النقدية  |
      | 2   | رواية الشّعر في الجاهليّة | – طرائق انتقال الشعر الجاهلي من طور الرواية إلى طور التدوين |
      | 3   | من مظاهر التنوّع القبلي   | – القبائل المترحّلة والقبائل المقيمة                        |

      **II- النصوص المختارة** (les 4 premiers titres sont regroupés sous l'accolade « معلّقة طرفة بن العبد »)

      | N°  | العنوان                      | مراكز الاهتمام                        |
      | --- | ---------------------------- | ------------------------------------- |
      | 1   | لخولة أطلال                  | –الاستهلال الطّللي والنسيب            |
      | 2   | عوجاء مرقال                  | –صفة الرّاحلة ووظائفها                |
      | 3   | ثلاث هنّ من عيشة الفتى       | –غرض الفخر : اللهو ومفهوم الفتوّة     |
      | 4   | ستبدي لك الأيام ما كنت جاهلا | –غرض الفخر : تفصيل المناقب            |
      | 5   | لنا الدّنيا ومن أضحى عليها   | –الفخر بالقبيلة                       |
      | 6   | أغشى الوغى وأعفّ عند المغنم  | –الفخر بالذات                         |
      | 7   | ليس على ناري حجاب            | –الفخر بالمحامد والشّيم               |
      | 8   | إنّي مانع جاري               | –مدح المآثر                           |
      | 9   | ضرّاب الكماة                 | –مدح الفروسيّة والشّيم                |
      | 10  | حامي العرين                  | –الرّثاء : التفجع والتأبين            |
      | 11  | تلَف مُقيمٌ                  | –الرّثاء : التفجع والتّأمّل           |
      | 12  | بدا لي وجه نُعْمٍ            | –النّسيب : مكوّناته ومعانيه           |
      | 13  | يا طائر البان                | –الغزل : أحوال المحبّ                 |
      | 14  | تداويت منها بها              | –صفة الخمرة وصورة مجالس الشراب        |
      | 15  | من حكم الجاهليّين            | –الحكمة : منظومة القيم عند الجاهليّين |
      | 16  | الخير بنواصي الخيل معصوب     | –صفة الخيل وصلتها بعالم الصحراء       |

      **III- النصوص التكميليّة**

      | N°  | العنوان                                                   | مراكز الاهتمام                                 |
      | --- | --------------------------------------------------------- | ---------------------------------------------- |
      | 1   | في بنية القصيدة                                           | – أقسام القصيدة وعلل انتظامها عند ابن قتيبة    |
      | 2   | هيكل القصيدة الجاهلية بين التراث النقدي والدراسات الحديثة | – المواقف من بنية القصيدة العربية قديما وحديثا |
      | 3   | هاجس الرحيل في الشعر الجاهلي                              | – تجليّات الرّحيل ودلالاته                     |

    - **p.7** — planche pleine page, carte historique en couleurs de la péninsule arabique et du Croissant fertile, deux encarts et une boîte de légende. Légende verbatim : « توزيع القبائل العـربيّة قبل ظهور الإسلام » / « المرجع : د. حسين مؤنس. » / « أطلس تاريخ الإسلام – القاهرة – الزهراء للإعلام العربي – ط 1 – 1987 ». Toponymes lisibles dans les encarts : « دولة الروم »، « دولة الغسّاسنة ». ⚠️ **ILLISIBLE** : la quasi-totalité des noms de tribus et de lieux portés sur la carte, la boîte de légende et le contenu des cartons (caractères manuscrits très fins).
    - **p.8** — seconde carte pleine page, carton de légende en haut à gauche. Légende verbatim : « الأحلاف القبليّة العـربيّة قبل ظهور الإسلام » / « المرجع : د. حسين مؤنس. » / « أطلس تاريخ الإسلام – القاهرة – الزهراء للإعلام العـربي – ط 1 – 1987 » (millésime lu 1987, identique à p.7). Zone nommée lisible : « منطقة عوالي نجد ». ⚠️ **ILLISIBLE** : noms de tribus/lieux et texte intégral du carton de légende.
    - **p.9** — page de titre de rubrique (planche décorative), calligraphie magenta : « نصوص تمهيديّة ». Ouverture de la section I.

  - **I – النصوص التمهيدية** (p.9–18) :

    **Texte تمهيدي 1 — « في معنى الجاهليّة »** · auteur **د. محمد عثمان علي** · référence (bloc signature p.12) : « د. محمد عثمان علي » / « في آداب ما قبل الإسلام » / « المكتبة العلميّة العالميّة—ط 4 . ليبيا، 1994 ص ص 11-13 » · **p.10–12** · prose (ni mètre ni décompte de vers).
    - **Incipit verbatim** : « درج جمهور الباحثين في الأدب – قديما وحديثا – على تسمية أدب العصر الذي يسبق الإسلام بالأدب الجاهليّ، ووصفوا أصحاب هذا الأدب بالجاهليّين، وذلك تبعا لمصطلح الجاهلية الذي أطلق على عهد ما قبل الإسلام منذ الأيّام الأولى للبعثة النبويّة. »
    - Contenu notionnel : la thèse est que le mot « الجاهليّة » est un terme forgé avec l'islam pour séparer deux époques, et qu'il dérive non pas de الجهل contraire de العلم mais de السّفه / الغضب / النزق.
      - Définition d'**ابن منظور** (lexicographique, note 1) : « الحال التي كان عليها العرب قبل الإسلام من الجهل باللّه تعالى ورسوله، وشرائع الدين، والمفاخرة بالأنساب، والكبر،والتجبّر وغير ذلك » — notes de bas de page verbatim : « 1– لسان العرب : ((مادة جهل)). » / « 2– السيرة الحلبية : ج2، ص 33. » / « 3– تاج العروس : مادة ((جهل)). » ; hadith cité : « إنَّكَ امرُؤٌ فيكَ جَاهِلِيّة » ; les surnoms « أبي جهل » / « أبي الحكم ».
      - **Les 4 occurrences coraniques du mot** (p.11, citées entre ﴿…﴾) : آل عمران « … يَظُنُّونَ باللهِ غَيْرَ الحَقِّ ظَنَّ الجَاهِلِيَّةِ، يَقُولُونَ هَلْ لَنَا مِنَ الأَمْرِ مِنْ شَيْءٍ » (note 4 : « 4 – سورة آل عمران، الآية 154 ») ; المائدة « أَفَحُكْمَ الجَاهِلِيَّةِ يَبْغُونَ، وَمَنْ أَحْسَنُ مِنَ اللَّهِ حُكْمًا لِقَوْمٍ يُوقِنُونَ » (note 5 : « 5 –سورة المائدة، الآية 50 ») ; الأحزاب « وَقَرْنَ في بُيُوتِكُنَّ وَلاَ تَبَرَّجْنَ تَبَرُّجَ الجَاهِلِيَّةِ الأُولَى » (note 6 : « 6– سورة الأحزاب، الآية 33 . ») ; الفتح « إِذْ جَعَلَ الَّذِينَ كَفَرُوا في قُلُوبِهِمْ حَمِيَّةَ الحَمِيَّةَ الجَاهِلِيَّةِ، فَأَنْزَلَ اللَّهُ سَكِينَتَهُ عَلَى رَسُولِهِ وَعَلَى المُؤْمِنِينَ، وَأَلْزَمَهُمْ كَلِمَةَ التَّقْوَى، وَكَانُوا أَحَقَّ بِهَا وَأَهْلَهَا وَكَانَ الله بِكُلِّ شَيْءٍ عَلِيمًا » (note 7 : « 7– سورة الفتح، الآية 26 ») — [sic] la répétition « حَمِيَّةَ الحَمِيَّةَ » est celle du rendu lu.
      - **Citations d'autorité modernes** : **الدكتور جواد علي** — « والرّأي عندي أنّ الجاهليّة من السّفه والحمق والأنفة والخفّة والغضب وعدم الانقياد لحكم وشريعة وإرادة إلهية وما إلى ذلك من حالات انتقصها الإسلامُ » (note 8 : « 8– المُفصَّلُ في تاريخ العرب قبل الإسلام، ط دار العلم للملايين، ج 1.ص 40 . ») ; **الدكتور شوقي ضيف** — « وينبغي أن نعرف أنّ كلمة الجاهليّة التي أطلقت على العصر ليست مشتقّة من الجهل الذي هو ضدّ العلم ونقيضه، وإنّما هي مشتقّة من الجهل بمعنى السّفه والغضب والنزق ، فهي تقابل كلمة الإسلام التي تدلّ على الخضوع والطاعة للّه عزّ وجلّ وما ينطوي فيها من سلوك خلقيّ كريم » (note 9 : « 9– تاريخ الأدب العربيّ، العصر الجاهليّ، ط دار المعارف، مصر، ص 39 . »).
      - **Vers cités** (p.12) : **عمرو بن كلثوم** [sic, graphie du manuel] — « ألا لا يَجْهَلَنْ أَحَدٌ عَلَيْنَا — فَنَجْهَلَ فَوْقَ جَهْلِ الجَاهِلِينَا » (note 10 : « 10ـ طويلة عمرو بن كلثوم، شرح الزوزني، ط دار الجيل، بيروت، ص .178 ») ; transition « وقال الفِنْدُ الزّماني في حماسيته التي اختارها له أبو تمّام: » puis **الفِنْد الزّمانيّ** — « وَبَعْضُ الحِلْمِ عِنْدَ الجَهْـ — ـلِ لِلذِلَّةِ إِذْعَـــــــانُ » (note 11 : « 11– حماسة أبي تمّام، شرح التبزيزي، ط دار العلم، بيروت، ج 1 ص.7 »).
      - Paragraphe de clôture verbatim : « فالأصل المشتقّ منه كلمة "الجاهليّة" قديم، ولكنّ الكلمة مستحدثة ظهرت بظهور الإسلام، وأُطْلِقت كمصطلح يفرق بين عهدين، عهدٍ عرف بالكبر والتجبر والتسلّط والتعصُّب القبليِّ، وعهدٍ جاء بمكارم الأخلاق من تواضع وتسامح ولين في الجانب، وخضوع للّه وانقياد لشريعته… »
    - **Encadré « مراكز الاهتمام » (verbatim intégral)** : « * مدلول كلمة "جاهليّة" في المعاجم. » / « * مدلول كلمة "جاهليّة" في القرآن. » / « * مدلول كلمة "جاهليّة" في بعض القراءات النقديّة. »

    **Texte تمهيدي 2 — « رواية الشّعر في الجاهليّة »** · auteur **د. محمد عثمان علي** · référence (p.14) : « د. محمد عثمان علي » / « في آداب ما قبل الإسلام » / « ص ص 61 – 62 » · **p.13–14** · prose.
    - **Incipit verbatim** : « …كانت الرواية هي الوسيلة العظمى التي وصل عن طريقها الشعر الجاهليّ إلى عصر التدوين، فَقَدْ كان الشاعر الجاهليّ يُنشد قصيدته، ويتلقّاها الناس عنه ويروونها ، وكانت رواية الشعر في الجاهليّة تقوم على دعامتين: »
    - Contenu notionnel : les **trois دعامات** de la transmission orale.
      - **1re دعامة** : « الأولى رواية الشعراء عن بعضهم » — écoles citées : مدرسة أوْس بن حَجَر وزهير بن أبي سُلمى، والحُطَيْئة وكَعْب بن زُهير، وهُدْبَة بن خَشْرَم، وجَمِيل بن مَعْمَر، وكُثَيّر عزَّة (note 1) ; école de أبو دؤاد الإياديّ (avec امرؤ القيس، عُبَيْد بن الأبرص، سُحَيم عبد بني الحَسْحَاس) ; الأعشى transmettant son oncle المُسَيَّب بن عَلَس (note 2) ; les liens طَرَفة بن العَبْد / المُتَلَمِّس / المُرَقَّش الأكبر / أبو ذُؤَيب الهُذَلي / سَاعِدَة بن جُؤيّة الهُذَلي.
      - **2e دعامة** : « والدعامة الثانية رواية القبائل لشعر شعرائها » — vers de satire des بني تغلب (2 vers, note 3) : « أَلْهَى بَنِي تَغْلُبَ عَنْ كُلِّ مَكْرُمَةٍ — قَصِيدَةٌ قَالَهَا عَمْرُو بنُ كُلْثُومِ » / « يُفَاخِرُونَ بِهَا مُذْ كَانَ أَوَّلُــهُمْ — يَـا لَلرِّجَـالِ لِفَخْرٍ غَيْرِ مَسْؤُومِ ».
      - **3e دعامة (verbatim)** : « وبجانب هاتين الدعامتين نجد دعامة ثالثة في رواية الشعر في الجاهلية، ولكنها كانت في درجة أقلّ من رواية الشعراء والقبائل، وكان عمادها حَفَظَةُ الشعر والأخبار، الذين كانوا يتناقلون الشعر وأخبار الشعراء ويذيعون ذلك في مجالس القبائل ومحافلها، وكان هؤلاء من قبائل متعددة يجوبون الفيافي… »
      - **Vers cités** (p.14) : **النابغة الذبياني** à عُيَيْنَة بن حصْن الفَزَارِي (1 vers, note 4) — « أَلِكْنِـي يَا عُيَيْنُ إِلَيْـكَ قَوْلاً — سَتُهْـــدِيهِ الرُّوَاةُ إِلَيْكَ عَنِّـي » ; **حميد بن ثور** (1 vers, note 5) — « قَصَائِدُ تَسْتَحْلِي الرُّوَاةُ نَشِيدَهَا — وَيَلْهُو بِهَا مِنْ لاَعِبِ الحَيِّ زَامِرُ ».
      - Notes de bas de page verbatim : « 1– انظر "في الأدب الجاهليّ" لطه حسين، فقد فصّل الحديث عن هذه المدرسة في ص 297 وما بعدها. » / « 2– الموشّح للمرزباني، ط دار نشر الكتب، القاهرة، ص 51 » / « 3– الشعر والشعراء لابن قتيبة، ج1 ، ص 159 وما يليها. » / « 4– ديوان النابغة، ط دار صادر، بيروت، ص 174 . » / « 5– ديوان حميد بن ثور، ص 89 . »
      - Paragraphe de clôture verbatim : « بهذه الدِّعامات الثلاث وصل الشعر الجاهليّ إلى الإسلام، حملته الأجيال في وفرة وكثرة مترجما عن حياة الجاهليّين، ومعبّرا عن أحداثهم في جميع تفاصيلها الصغيرة والكبيرة، ومصوِّرا لخلاصة فكرهم في حياتهم التي عاشوها في تلك العهود. »
    - **Encadré « مراكز الاهتمام » (verbatim intégral)** : « * رواية الشعراء عن بعضهم بعضًا. » / « * رواية القبائل شعر شعرائها. » / « * رواية حَفَظَةِ الشّعر والأخبار. »

    **Texte تمهيدي 3 — « من مظاهر التنّوع القَبَلِيِّ »** (titre exact tel qu'imprimé) · auteur **د. ناصر الدين الأسد** · référence (p.16) : « د.ناصر الدين الأسد » / « مصادر الشعر الجاهليّ وقيمتها التاريخيّة » / « دار الجيل بيروت، ط. 7. 1988.ص—ص 5 – 10 » · **p.15–16** · prose.
    - **Incipit verbatim** : « القبيلة عند العرب في حاجة إلى دراسة مستفيضة،[…] وبحسبنا أن نشير إلى أنّ الشائع المتعارف أنّ القبيلة كانت في الجاهليّة جماعات من الأعراب البدائيّين، يسكنون الخيام ويقطنون الصحراء، لا همّ لهم إلا الغزو وانتجاع الكلإِ . »
    - Contenu notionnel : réfutation de l'image d'une Arabie exclusivement nomade ; opposition structurante **أهل المدَر / أهل الوبَر**.
      - Tribus sédentaires citées verbatim : « فالأوْسُ والخَزْرَجُ كانتا تسكنان المدينة، وثَقِيف كانت تسكن الطّائِف ، وقُرَيْش البِطَاح تسكن بطحاء مَكَّةَ، وتَغْلب وبَكْرُ وإِيَاد كان بعضها حاضرة تسكن الجزيرة ما بين النهرين، وعبد القَيْس كان منها حاضرة تسكن عُمَان والبَحْرَين ».
      - Distinction structurante verbatim : « وكثيرا ما نجد قبيلة واحدة تحيا حياتين مختلفتين: كان قسم منها يتحضّر ويستقرّ ويسكن المَدَرَ ، على حين يبقى قسم منها باديا من أهل الوبر ، في أطراف القرى والمدن. »
      - **Témoignage antique cité** : **دِيُودُورُوس الصِّقِلِّيّ**, « في القرن الأوّل قبل الميلاد » — « إنّه كان يقطنها جمهور كبير من العرب الرُّحَّل الذين اتّخذوا لأنفسهم حياة الخيام، وكانت لهم قطعان كثيرة من الأغنام، وينصبون مضاربهم في السهول الواسعة المنبسطة.. » ; puis « إنّ الأجزاء الباقية من بلاد العرب المتاخمة للبحر والتي تقع إلى الشّمال من العربيّة السّعيدة وتمتدّ حتّى تجاور سوريّة، يقطنها جمهور من المزارعين والتجّار على اختلاف أنواعهم، يبيعون ما عندهم ويتباعون ما عند غيرهم في مواسم وأسواق تجاريّةٍ…ويتخلّل هذه البلاد كثير من الأنهار، ويهطل عليها مطر غزير في الصيف، فيكون لها بذلك موسمان زراعيّان في السّنة الواحدة. »
      - **Citation d'ابن العبْرِيّ** (p.16, verbatim) : « وأمّا سائر عرب الجاهليّة بعد الملوك فكانوا طبقتين: أهل مدَرَ وأهل وَبَر. فأمّا أهل المدر فهم الحواضر وسكّان القرى ، وكانوا يحاولون المعيشة من الزرع والنخل والماشية والضرب في الأرض للتّجارة. وأمّا أهل الوبر فهم قُطَّان الصَّحَارَى ، وكانوا يعيشون من ألبان الإبل ولحومها، منتجعين الكلأَ، مرتادين لمواقع القَطْرِ، فيُخَيِّمُون هنالك ما ساعدهم الخصب وأمكنهم الرعي ، ثم يتوجهون لطلب العشب وابتغاء المياه فلا يزالون في حِلٍّ وتَرْحَالٍ. »
      - Classement des historiens musulmans, verbatim : « فَهُمْ يقسمون عرب الجاهليّة قسمين رئيسيّين: الملوك، وغير الملوك. ثم يقسمون غير الملوك قسمين رئيسيّين: أهل مدَر وأهل وبَر، ويقسمون أهل المدر إلى زرّاع وتجّار . »
    - **Encadré « مراكز الاهتمام » (verbatim intégral)** : « * استقرار بعض القبائل بأشهر المدن العربية قبل الإسلام. » / « * تصنيف القبائل إلى مقيمة ومترحّلة. » / « * صورة المجتمع القبليّ الجاهليّ عند بعض المؤرّخين القدامى. »

    **Les 2 planches généalogiques (p.17–18)** — titre p.17 : « مشجّر بأنساب القبائل العربيّة وبعض شعرائها ».
    - **p.17 — « (1– القبائل العدنانيّة) »** : عدنان → معدّ → نزار ; نزار → أنمار | مضر | ربيعة | إيّاد ; مضر → خندف | قيس عيلان ; خندف → طابخة (→ مُزينة → **زهير بن أبي سُلمى**) | مدركة (→ هذيل → **أبو ذؤيب الهذليّ**) ; قيس عيلان → خَصَفَةَ (→ بنو سُليم → **الخنساء**) | سعد (→ غطفان → ذبيان → **النّابغة الذبيانيّ** ; عبس → **عنترة بن شدّاد**) ; ربيعة → أسد → وائل → تغلب (→ بنو عتّاب → **عمرو بن كلثوم**) | بكر (→ بنوجحدر → **الأعشى** ; سعد → **طرفة بن العبد**).
    - **p.18 — « (2– القبائل القحطانيّة) »** : قحطان → كهلان | حِمْيَر ; حِمْيَر → مالك → قُضاعَة → نَهد | عُذرة (→ **جميل بن معمر**) | بهراء | كلب (→ **زهير بن جناب**) | جُهينة ; كهلان → الأشعريّون | عَامِلة | لَخْم (→ ملوك الحيرة → **النعمان بن المنذر ممدوح النّابغة الذبياني**) | بجيلة | جُذام | كِنْدة (→ بنو حُجر → **امرؤ القيس**) | همدان | مراد | مَذحج | طيء (→ **حاتم الطّائي**) | الأزْد (→ **الشنْفَرى**).
    - **Référence de la planche (verbatim, p.18)** : « المرجـــــع : أيّام العرب في الجاهليّة (ملحق في أنساب العرب) » / « محمّد أحمد جاد المولى ومحمّد أبو الفضل إبراهيم » / « دار الجيل، بيروت. 1988 ».

  - **II – النصوص المختارة — ouverture de la section et معلّقة طرفة** (p.19–33 ; la section se poursuit aux chapitres C2→C5 jusqu'à p.75) — page de titre de rubrique **p.19** (calligraphie magenta « نصوص مختارة ») ; **p.20** planche iconographique pleine page, légende verbatim : « "واحــــــــة" » / « لوحة للفنّان الحبيب بلال ». **p.21** : notice d'auteur pleine page « طرفة بن العبد », encadré bleu à 3 puces, verbatim intégral :
    - « هو عمرو بن العبد بن سفيان البكريّ، لقّب بطرفة لطول قامته، واشتهر به عند الرواة والنقّاد، نشأ يتيما بين أعمامه وحُرِمَ ميراث أبيه، فعاش عِيشَــة لهو وعبث ، ولمّا شبّ اتّصل بعمرو بن هند ملك الحيرة ومدحه. برع طرفة في الحماسة والفخر والهجاء، وجعل من حياته الخاصّة على قِصرها مصدرا يستقي منه الحِكَم. مات قتيلا ولمّا يبلغ الثّلاثين من عمره، ورجّح الزِّرَكلي أنّ مقتله كان سنة 564 م. »
    - « بقيت قصائد طرفة تُتَداول مشافهةً حتّى جمعها ابن السِكِّيت في القرن الثالث للهجرة وهي في أغلبها من صنف المقطّعات القصيرة. وانصبّ اهتمام النقّاد والشرّاح على معلّقته إذ انتخبها الزوزنيّ في مؤلّفه "شرح المعلّقات السّبع" والقرشيّ في "جمهرة أشعار العرب". »
    - « يبدو غرض الفخر مهيمنا على ديوانه، وكثيرا ما يتّصل بالوصف والتأمّل، لا سيّما في المقطّعات والأبيات المُفْرَدَة. وتكثر في مطوّلاته أسماء الأعلام والمواضع. »

    **Texte 1 — « - 1 - خَوْلَةَ أَطْلَالٌ »** (titre courant bleu : معلّقة طرفة بن العبد) · auteur **طرفة بن العبد** · mètre **(من الطّويل)** · **10 vers** · référence : « معلّقــة طرفة بن العبد / شرح المعلّقات السبع للزوزنيّ تحقيق كرم البستاني / دار صادر، بيروت، د.ت. » (⚠️ « دار صادر » [sic]) · **p.22–24**.
    - **Incipit verbatim** : « لِخَوْلَةَ* أَطْلَالٌ بِبُرْقةٍ1 تَهْمَدُ* — تَلُوحُ كَبَاقِي الوَشْمِ فِي ظَاهِرِ اليَدِ »
    - `تمهيد` — substance : la parenté du النسيب et du الطلل, adossée à une citation de **قدامة بن جعفر** : « وقد يدخل في النسيب التشوّق والتذكّر لمعاهد الأحبّة بالرياح الهابّة والبروق اللاّمعة والحمائم الهاتفة، والخيالات الطائفة وآثار الديار العافية وأشخاص الأطلال الداثرة، وجميعُ ذلك إذا ذُكر احْتِيجَ أن تكون فيه أدلّةٌ على عظيم الحسرة ومُرْمِض الأسف والمنازعة » — référence : « قدامة بن جعفر ، نقد الشعر ص 139. »
    - `اعرف` — **17 entrées de الشـرح** (برقة، حدوج، النواصف، حيزوم، المفايل، أحوى، المرد، شادن، مظاهر، خذول، ربربًا، البرير، أَلْمَى، دعص، إياة، لثاته، لم تكدم) ; **الأعلام** : خولة، المالكية، ابن يامن ; **الأماكن** : تهمد، دَدِ، عدوليّة.
    - `فكّك` : « قطّع هذا النصّ معتمدا البنية معيارا. »
    - `حلّل` : 1. « في النصّ حديث عن المكانِ (الطلل) والإنسان (الحَبيبة)، فما الصّلة بينهما؟ » 2. « استخرج ما عُلِّق بالموصوفات من تشابيه ونعوت ورتّبها حسب مجالاتها. » 3. « قام هذا المقطع من المعلّقة على مقابلة بين معاني الفناء ومعاني البقاء، فما وظيفة ذلك؟ » 4. « تبيّن كيف استرجع الشاعر ماضيه السعيد من خلال حاضره الشقيّ. »
    - `قوّم` : « هل لك أن تستخلص من هذا النصّ أبعاده الرمزيّة معلّلا إجابتك. »
    - `توسّع` : « حلّل البيت التالي تحليلا عروضيّا تامّا ذاكرا ما طرأ عليه من تغييرات : » (vers 5) ; « وزّع موجودات عالم النص من إنسان وحيوان ونبات وجماد على قسمي الاستهلال الطّلليّ والنسيب. »
    - `إضاءات` : (a) la quasi-identité du vers 2 avec un vers de معلّقة امرئ القيس — « ليس بين البيتين خلاف إلاّ في الضّرب » — expliquée par « خاصيّتي الرّواية والمشافهة » ; (b) figure nommée : **استعارة تصريحيّة** (le poète « صرّح بالمشبّه به وغيّب المشبّه ») sur « أحوى … شادن », avec la notion de **قرينة مانعة** et de **مجاز لغويّ**.
    - `شذرات` : **د. أحمد إسماعيل النعيمي / الأسطورة في الشعر العربيّ / قبل الإسلام، ص 265** — le طلل comme « رمز للموت والفناء ».

    **Texte 2 — « - 2 - عَوْجَاءُ مِرْقَالٌ »** · **طرفة بن العبد** · **(من الطويل)** · **12 vers** · référence : « معلّقة طرفة بن العبد / شرح المعلّقات السبع للزوزني » · **p.25–27**.
    - **Incipit verbatim** : « وَإِنِّي لَأُمْضِي الهَمَّ عِنْدَ احْتِضَارِه — بِعَوْجَاءَ1 مِرْقَالٍ2 تَرُوحُ وَتَغْتَــدِي »
    - `تمهيد` — substance : pourquoi la ناقة « تُمضي الهموم » ; deux voies (« بالرّحلة في الصحراء وتأمّل الكون … وباتّخاذ هذه النّاقة قناعا أو معادلا شعريّا له ») — référence : « وهب أحمد روميّة / شعرنا القديم والنقد الجديد – سلسلة عالم المعرفة الكويت / مارس 1996 – العدد 207 – ص183 ».
    - `اعرف` — **15 entrées de الشـرح** (عوجاء، مرقال، سفنّجة، دالج، أتلع، سكّان، بوصي، العلاة، سبت، الماويّتان، حجاجان، قلْت، صفيح، مصمّد، القدّ) ; **الأماكن** : دجلة. Pas de rubrique الأعلام.
    - `فكّك` : « قطّع النصّ متّخذا تدرّج الوصف معيارا. »
    - `حلّل` : 1. « استخرج الموصوفات التي ركّز عليها الشاعر مبيّنا دورها في نحت ملامح الرّاحلة. » 2. « ما المجالات التي استقى منها الشاعر تشابيهه؟ وهل لذلك صلة بواقعه وبيئته؟ » 3. « تفصيل صورة النّاقة كتفصيل صورة الحبيبة في قسم النّسيب، فهل ترى بينهما من علاقة؟ » 4. « أُرصد مظاهر التحوّل من السّكون إلى الحركة مستعينا بما أدركته من النصّ السّابق. »
    - `قوّم` : « كيف تعلّل الانتقال من ذكر الطلل والنسيب إلى وصف الرحلة والرّاحلة ؟ »
    - `توسّع` : « استخرج الحقلين المعجميّين لما يلي: (الماء، الحركة). » ; « حلّل الوجه البيانيّ في البيت الموالي: » (vers 2).
    - `إضاءات` : figure nommée **كناية عن موصوف** (« حذف الشاعر الموصوف وهو العنق وكنّى عنه بصفة هي "أتلع" … وهي وجه من وجوه البيان »).
    - `شذرات` : **أحلام الزعيم / التطوّر الفنيّ في شكل القصيدة وموضوعاتها / جامعة الإسكندريّة، 1977 ص 14.** — la ناقة « رمز للأمومة الخصبة » et expression de « فكرة الفناء ».

    **Texte 3 — « - 3 - ثَلاَثٌ هُنَّ من عِيشَةِ الفَتَى »** · **طرفة بن العبد** · **(من الطويل)** · **17 vers** (1→15 p.28, 16→17 p.29) · référence : « معلّقة طرفة بن العبد / شرح المعلّقات السبع للزوزني » · **p.28–30**.
    - **Incipit verbatim** : « إذا القَوْمُ قالُوا مَنْ فَتَى، خِلْتُ أَنَّني — عُـنِيتُ فَلَمْ أَكْسَــلْ ولمْ أَتَبَلَّـدِ1 »
    - `تمهيد` — substance : la progression de la معلّقة (ديار → نسيب → راحلة → فخر) et le lien entre les متع et le مفهوم الفتوّة, citation incorporée « لقد ولّد الشّعور بمأساة "المصير الإنسانيّ" رغبة جارفة في الردّ على هذا المصير بمبدإ "اللذّة" على اختلاف ضروبها. الحياة وجدت لتعاش… » — référence : « وهب أحمد روميّة / شعرنا القديم والنّقد الجديد – ص183 ».
    - `اعرف` — **20 entrées de الشـرح** (لم أتبلّد، التلاع، يسترفد، مصمّد، نداماي، قينة، قطاب، بضّة، مطروقة، أظآر، ربع، معبّد، غبراء، عوّدي، كميت، مضاف، محنّبا، سيد، الدجن، بهكنة). ⚠️ décalage de numérotation d'une unité entre les renvois du corps et la liste du شرح à partir de مضاف [sic]. Pas de rubrique الأعلام / الأماكن.
    - `فكّك` : « في القصيدة تحوّل من وصف تفاصيل عيشة الفتى إلى الدّفاع عن الفتوّة مذهبا، قطّع النص مستأنسا بتحوّلات الخطاب الشعريّ . »
    - `حلّل` : 1. « ما المعاني التي فخر بها طرفة ؟ » 2. « كان تدخّل الذّات القبلية لتحييد الشاعر وعزله حافزا للدفاع عن مفهوم للحياة ارتضاه لنفسه، استخرج مكوّنات هذا المفهوم ورتّبها حسب مجالاتها. » 3. « لِمَ راوح الشاعر بين المخاطبة والإخبار؟ » 4. « قام النصّ على الإجمال والتفصيل، تبيّن مظاهر ذلك مستخلصا دور هذه الثنائية في بناء معاني الفخر. »
    - `قوّم` : « هل تجد لهذا القسم من غرض الفخر صلة بما سبق من نسيب ورحلة؟ كيف ذلك؟ »
    - `توسّع` : « استخرج ما اتّصل باللفظين التاليين من حقل معجميّ:( اللهو، الجدّ) » ; « تبيّن البنية النحويّة للتركيب التالي: "متى يسترفد القومُ أرْفِدِ" » ; « وازن بين صورتي المرأة حبيبة وقينةً. »
    - `إضاءات` : figure nommée **التشبيه** (« بنى المتكلّم الصورة على التشبيه، وهو وجه من وجوه البيان »), avec la remarque que le verbe « خال » (فعل من أفعال الظن) fait office d'**أداة التشبيه**.
    - `شذرات` : **وهب أحمد روميّة / شعرنا القديم والنّقد الجديد – ص 393** — طرفة face à « مأساة المصير الإنسانيّ » et la valeur du corps dans les لذّات (« شرب الخمرة/الفروسيّة/النساء »).

    **Texte 4 — « - 4 - سَتُبْدِي لَكَ الأَيَّامُ مَا كُنتَ جَاهِلاً »** · **طرفة بن العبد** · **(من الطويل)** · **19 vers** (1→16 p.31, 17→19 p.32) · référence : « معلّقة طرفة بن العبد، شرح المعلّقات السبع للزوزني » · **p.31–33**.
    - **Incipit verbatim** : « أَرَى المَوتَ يَعْتَامُ1 الكِرامَ ويصْطَفِـي — عَقِيلَــةَ مَالِ الفَاحِشِ المُتَشَدِّدِ »
    - `تمهيد` (verbatim intégral) : « يسترسل طرفة في هذا القسم الثاني من غرض الفخر في نعت مناقبه وبيان شمائله، تحدوه في ذلك رغبة عارمة في التميّز عن الآخرين ونحت الكيان الفرد واستخلاص العبر. وليست المفاخر مخايل توسّمها الشاعر في ذاته، بل هي تعبير عن تجربة فتوّة فذّة عاشها فصوّرها في أبيات عيون ،ثمّ استخلص منها في نهاية معلّقته بيتين أرسلهما مثلا شاردا. »
    - `اعرف` — **13 entrées de الشـرح** (يعتام، الضرب، خشاش، كشحي، عضب، معضد، قدي، بلّت، الجلّى، الخنا، ملهّد، وغلا، محتدي) ; **الأماكن** : ضرغد ; **الأعلام** : ابنة معبد. ⚠️ vers 13 : renvoi imprimé « 21 » alors que la glose porte le n° 12 [sic] ; vers 18 imprimé « مَنْ لَمْ تـــزَوَّدِ » avec allongement typographique [sic].
    - `فكّك` : « تخيّر ممّا يلي ما ترتضيه معيارا لتقطيع النصّ : » — « * الإخبار والمخاطبة. / * معاني الفخر. / * بنية الضمائر. (أنا، أنتِ، هو). »
    - `حلّل` : 1. « استخلص طائفة المعاني الفخريّة في هذا النصّ. » 2. « قامت الفخريّة على مقارنة بين الشاعر الفتى ونقيضه، استخرج مواطن التقابل مبيّنا وظيفتها في بنية غرض الفخر. » 3. « افتُتح النصّ ثمّ انغلق بنفس حكميّ، استجل وظائف الحكمة متبيّنا موقف الجاهليّ من الزمن. » 4. « لم يستقم الفخر في هذه القسم من المعلّقة إلاّ بحضور بعض المعاني الهجائية، فكيف ذلك؟ » 5. « بيّن بالاعتماد على العناصر اللغويّة التالية (التراكيب النحويّة، زمن الأفعال، المشتقّات) استعداد القصيدة للانعتاق من خصوصيّة التجربة إلى مطلق الحكمة والمثل. »
    - `قوّم` : « تبيّن صلة هذا النصّ بسابقه. » ; « هل ترى بين أقسام المعلّقة تكاملا وترابطا؟ كيف ذلك؟ (يمكن الاستئناس بشروح النصــوص الثلاثة الأولى، والنص التكميلي الأوّل لابن قتيبة) »
    - `توسّع` : « لم تتغيب المرأة في كلّ أقسـام المعلّقـة فهي حبيبة وقينة وناعية، فهل لك أن تصنف في جدول نعوتهنّ ووظائفهن وعلّة الجمع بينهنّ. » ; « اختزل نصوص المعلّقة في مجموعة من الثنائيات: ( الماضي / الحاضر، السّعاة / الشقاء) » (⚠️ « السّعاة » [sic]).
    - `إضاءات` : le fait littéraire est l'**insertion du مثل dans le poème** — « إيراد الأمثال في الشعر لا يكفل لها الرواج والذيوع وحسب، بل يعدّ ذلك من حلية الشعر وتمامه، وهذه "الأشياء في الشعر إنّما هي نبذ تستحسن ونكت تستظرف" على حدّ تعبير ابن رشيق. »
    - `شذرات` : **كمال أبو ديب / الرؤى المقنعة: نحو منهج بنيوي / في دراسة الشعر الجاهلي، ص265.** — la معلّقة comme unification par l'expérience de la mort (الأطلال / الشادن / الناقة / مجلس الشراب والقينة / القيم الاجتماعية).

  - **ورقة منهجيّة** (p.34) — fiche sur parchemin déroulé, étiquette en coin « ورقة منهجيّة », titre « كيف أقـرأ », sous-titre magenta. La première des cinq ورقات du محور (p.34, 44, 52, 59, 65). Transcription verbatim intégrale.

    ### p.34 — « كيف أقرأ : الغرض الشعريّ »

    > **\* حدّ الغرض الشعريّ**
    >
    > هو انتظام معاني القصيدة حول محور ما تدور عليه الأفكار والصور، وتسند المعاني إلى الجهة التي بيّتها الشاعر في نفسه أو سلك فيها سنّة، فيكون الغرض نتيجة صوغها وتركيبها.
    >
    > **\* مداخل الأغراض الشعريّة**
    >
    > لئن كانت بعض الأغراض الشعريّة لا تحتاج مداخل استهلاليّة كغرضي الرثاء والهجاء، فإنّ بعضها الآخر يحتاج ممهّدات اصطلح عليها باسم المقدّمات، وأهمّها الوقفة الطلليّة والنسيب ووصف الرّحلة، وعلى الشاعر إن رام مديحا أو فخرا ((أن يقدّم بين يدي الغرض موطّئات بهــا يقوم ويستقيم))
    >
    > **\* خطاطة المقام الشعريّ** — schéma en cases et flèches ; contenu des cases, verbatim :
    >
    > - Case sommet : **المقام الشعريّ** (flèches entrantes depuis les deux cercles latéraux, flèche sortante vers الغرض)
    > - Cercle gauche : **المتقبّل / السامع/القارئ**
    > - Cercle droit : **الباتّ / الشاعر**
    > - Case : **الغرض**
    > - Case : **الرّسالة (الخطاب الشعريّ ذاته)**
    > - Case : **السّنن**
    > - Case rattachée au cercle gauche : **خلفيّات السّامع وانتظاراته …**
    > - Case rattachée au cercle droit : **خلفيّات المتكلّم الثقافيّة والعاطفيّة**
    > - Les 4 cases issues de **السّنن** (de droite à gauche telles qu'imprimées) : **المعاني والأفكار والصّور** / **قواعد اللغة** / **النّموذج: مظاهر الاتباع والابتداع** / **المرجع**
    >
    > **\* غراض الشعر العربيّ** [sic — le أ initial de « أغراض » est masqué par le bord déchiré du parchemin]
    >
    > لئن اختلف النقاد القدامى في تصنيف الأغراض وتسمياتها، فإننا نحتفظ في هذا الموضع بخمسة منها قام عليها الشعر، وهي المدح والفخر –لا سيّما الجاهليّ منهما– والغزل والرثاء والهجاء.

  - **III – النصوص التكميليّة** (p.76–81) — page de titre intercalaire **p.76** : « نصوص تكميليّة » (page décorative, frise géométrique à droite, aucun numéro imprimé). ⚠️ Le libellé « III – النصوص التكميليّة » n'apparaît **pas** comme titre imprimé dans cette partie du محور 1 (il figure au فهرس p.6 et, pour le محور 2, p.87). Les 3 textes reçoivent le même traitement que les تمهيديّة : un `الشـرح` (pour le premier seulement) et un encadré « مراكز الاهتمام », sans rubrique de questions.

    **Texte تكميلي 1 — « في بنيَةِ القَصِيدَة »** · auteur **ابن قتيبة** · référence : « ابن قتيبة / الشعر والشعراء / الدّار العربية للكتاب ط3 / 1983 ، ج I ، ص–ص20–21 » · **p.77–78** · prose critique.
    - **Incipit verbatim** : « قال أبو محمّد: سَمِعْتُ بَعضَ أهلِ الأدب يذكرُ أنّ مُقَصِّدَ1 القصيد إنّما ابتدأ بذكرِ الدِّيار والدِّمَن2 والآثار، فبَكَى وشكَا، وخَاطَبَ الرَّبْعَ3. »
    - Contenu notionnel : la **théorie canonique des أقسام القصيدة** — ouverture par les ديار / دمن / آثار (pleurs, plainte, adresse au ربع, arrêt du compagnon) pour amener le souvenir des أهل الظاعنين ; puis le **نسيب** (« فشكَا شدَّةَ الوَجْدِ وألمَ الفراق، وفرط الصَّبابة والشَّوقِ، لِيُميلَ نحْوَهُ القلوبَ ويصرفَ إليهِ الوجوهَ، ويستدعي به إصْغاءَ الأسماعِ إليهِ ») justifié par la nature humaine (« لِمَا قد جعل اللهُ في تركيبِ العبادِ منْ محبَّةِ الغزلِ وإلْفِ النساءِ ») ; puis la **رحلة** (« فرَحَلَ في شِعْرِهِ ، وشكَا النَّصَبَ والسَّهرِ ، وسُرَى اللّيْلِ وحرَّ الهَجِيرِ وإنْضَاءَ الرَّاحلَةِ والبَعير ») ; puis le **مديح** (« فبعثَه على المُكَافأةِ، وهزَّه للسَّمَاحِ، وفضَّلَه على الأشْبَاه، وصغَّر في قَدْرِهِ الجَزيل »). Critère du poète accompli : « فالشَّاعِرِ المُجيد مَنْ سَلَكَ هَذِهِ الأسَاليبَ وعدَلَ بينَ هذهِ الأقْسَام، فلمْ يَجْعَلْ وَاحدًا منها أغلبَ على الشِّعر، ولمْ يُطِلْ فيمِلَّ السَّامعِين، ولمْ يقْطَعْ وبالنفُوس ظمأٌ إلى المَزيدِ. » Il oppose aussi **أهل العمد / أهل المدر** (« لانتقالهم من ماءٍ إلى ماءٍ، وانتجاعهم الكَلأَ، وتتبعهم مَسَاقِط الغيث حيث كان »).
    - **Anecdote finale (نصر بن سيَّار والي خُرَاسانَ لبني أُميّة)** : le رجّاز dont le تشبيب faisait 100 vers pour 10 de مديح ; réplique de نصر — « واللهِ مَا بقَّيْتَ كلمة عذبةً ولا معنًى لطيفًا إلاّ وقدْ شغلْتَهُ عن مَدِيحِي بتَشْبِيبِكَ، فإنْ أردْتَ مديحِي فاقتصِدْ في النَّسيبِ. » ; le vers alors récité — « هلْ تَعْرِفُ الدَّارَ لأمِّ الغَمْرِ — دَعْ ذَا وحَبِّرْ مدْحَةً في نَصْرِ » ; conclusion — « فقَالَ نصْرُ بنُ سيَّار: لا ذلِكَ ولا هذَا ، ولكِن بيْنَ الأمْرَيْنِ. »
    - `الشـرح` (p.78) — **8 entrées** : مقصّد (« إسم فاعل من قولهم : قصّد الشّاعر قصيدته أيْ بناها وأنشاها » [sic « إسم »])، الدّمن، الرّبع، الظاعنون، نازلة العمد (« كناية عن البدو، أمّا أهل المدر فهم الحضر »)، لائطٌ، إنضاء، ذمام.
    - **Encadré « مراكز الاهتمام » (verbatim)** : « * بنية القصيدة عند ابن قتيبة. » / « * دواعي البنية وعلل نظم أقسام القصيدة. » / « * شرط التناسب بين الأقسام . »

    **Texte تكميلي 2 — « هيكل القصيدة الجَاهليّة بين التّراث النّقدي والدّراسَات الحَديثة »** · auteure **د. سوزان ستيتكيفيتش** · référence : « القصيدة العربية وطقوس العبور دراسة في البنية النموذجية / مجلة المجمع اللغوي بدمشق– سوريا عدد60،المجلد 1985،ص–ص 55—58. » · **p.79–80** · étude critique moderne.
    - **Incipit verbatim** : « من المعروف، بل من المسلَّم به، أنّ القصيدة التقليدية مبنيّة على شكل ثلاثيّ مكوّن من النّسيب والرّحيل والفخر/المديح، ومن الصّور الخاصّة بكل جزء من هذه الأجزاء. »
    - Contenu notionnel — thèses successives : (1) la **structure ternaire** (نسيب / رحيل / فخر-مديح) est restée l'énigme de la littérature arabe, dominant « الخيال والإنتاج الشعريّين من العصر الجَاهلِيّ حتى بداية قرننا هذا » ; (2) la cause n'est pas l'étroitesse de l'imagination arabe mais les règles formelles et sémantiques (« ما يسمّى بـ"عمود الشعر" ») : « ما خرج على مفهوم القصيدة– أو لم يلمّح إليه بطريقة ما– لم يعتبر شعرا » ; (3) رثاء et هجاء participent de la même ternarité, avec la citation d'**ابن رشيق** — « الشعر كلّه في ثلاث لفظات... فإذا مدحت قلت أنت، وإذا هجوت قلت لست، وإذا رثيت قلت كنت » et l'ajout de l'auteure « (نستطيع أن نضيف إلى هذه الثلاث رابعة: "وإذا فخرت قلت أنا") » ; (4) deux explications de la **قطعة / مقطوعة** (reste d'une longue قصيدة perdue, ou poème structurellement incomplet mais conçu et compris à la lumière du moule ternaire) : « فليست القصيدة الثلاثية قالبا لنظم الشعر العربي فحسب، إنما هي أساس لاستيعاب الشعر العربي » ; (5) les critiques anciens ont pris ce moule pour mesure sans en discuter les rapports internes — chez **ابن قتيبة** « ليس النسيب إلاَّ حيلة جاذبة تلفت نظر المتلقي، أي وسيلة إغراء » ; chez **الحاتميّ** la comparaison de la قصيدة au corps humain ne viserait que « توازن أجزاء القصيدة وتناسبها دون ما إشارة إلى علاقات دلالية بينها » ; (6) chez les modernes, rejet du moule et substitutions — « الوحدة العضوية عند كولريدج (Coleridge) أو الثنائية الضدية عند البنيويين » ; (7) la thèse de l'auteure : le moule est « بناء عميق مولد للشعر العربي », et les sciences modernes (histoire, archéologie, linguistique comparée, théorie littéraire, psychologie, anthropologie) permettent de s'approcher des sources de la poésie jahilite « أكثر من النقاد القدمــاء ».
    - **Notes de bas de page (verbatim)** : « ابن رشيق القيرواني:«العمدة في محاسن الشعر وآدابه ونقده»، بيروت 1972.ج II ،ص147 . » / « ابن قتيبة: «كتاب الشعر والشعراء»، ليدن 1902. ص14—15 » / « أبو علي محمد بن الحسن الحاتميّ: «حلية المحاضرة في صناعة الشعر». » / « محمود بن سلام الجمحي، «طبقات فحول الشعراء»، القاهرة، 1952. ص22 . »
    - **Encadré « مراكز الاهتمام » (verbatim)** : « * سيطرة البنية الثلاثية على القصيدة العربيّة إنتاجا وتلقيّا. » / « * صلة المقطوعة بالقصيدة. » / « * المواقف من بنية القصيدة العربيّة قديمًا وحديثًا. »

    **Texte تكميلي 3 — « هاجسُ الرّحيل في الشّعر الجَاهِليّ »** · auteur **د. وهب أحمد رومية** · référence : « شعرنا القديم والنقد الجديد / سلسلة عالم المعرفة، العدد207 الكويت، مارس 1996, ص271 - 272 » · **p.81** · étude critique moderne.
    - **Incipit verbatim** : « كانَ الرّحيل هاجسا لا يقرّ ولا يهدأ في ضمير الشاعر الجاهليّ. »
    - Contenu notionnel : le poète jahilite est « راحل أو متأمّل من يرحل وما يرحل: الظعائن، العمر، القبائل، الأهل والرّفاق، الحياة نفسها » ; le رحيل comme **rite de connaissance** (« إنّها رحلة اكتشاف الكون أو العالم أو الحياة، رحلة المعرفة الشّاقة وتذوّق ثمرها المرّ الجميل ») ; la ذات jahilite n'est pas détruite mais « قلقة مأزومة » — « عاشقة للقوّة، مؤمنة بها، حريصة عليها » et « كثيرة الالتفات إلى الآخر ، تتأمّل نفسها في مرآتها الخاصّة، و لا تكفّ عن تأمّلها في مرايا الآخرين » ; conclusion : « إنّها ذات كاملة الأهليّة لتأمّل نفسها، وتأمّل العالم والمجتمع من حولها. »
    - **Vers cités (2)** : « تقُولُ سُلَيْمَى:"لَوْ أَقَمْتَ لَسَرَّنَا" — ولَمْ تَدْرِ أنِّي لِلْمقَامِ أُطَوِّفُ » (introduit par « فكأنّما كان تأبّط شرّا يصوّر روح العصر الشّاعرة حين قَالَ : ») ; « وقَدْ طَوَّفْتُ في الآفَاقِ حَتَّـى — رَضِيتُ مِن الْغَنيمَةِ بالإيَابِ » (attribué à **امرؤ القيس**, introduit par « وكان "امرؤ القيس" يصور عبث هذا الطّواف وخيبته : »).
    - **Encadré « مراكز الاهتمام » (verbatim)** : « * تجلّيات الرّحيل في الشعر الجاهليّ. » / « * البعد المعرفيّ في الرّحيل. » / « * دلالات الرّحيل. »

  - **Clôture** (p.82–83) — **« ثبت بيبليوغرافي »** (bandeau bleu), en trois parties. p.84 est **entièrement blanche** ; le **المحور الثاني** s'ouvre p.85 (page de titre « المحـــور الثّانـي » / « التجديد في الشعر العربيّ في القرن الثاني للهجرة »).

    **1- الكتب (باللسان العربي)** (p.82) — auteur → référence(s), verbatim :
    - **أبو ديب (كمال)** : « – الرّؤى المقنّعة : نحو منهج بنيوي في دراسة الشعر الجاهلي – القاهرة – الهيئة المصريّة العامّة للكتاب 1986 »
    - **أبو سليم ( أنور عليان)** : « – الإبل في الشعر الجاهلي. الرياض. دار العلوم للطباعة. 1983. »
    - **الأسد (ناصر الدّين)** : « – مصادر الشعر الجاهلي وقيمتها التاريخية. بيروت. دار الجيل.1988. »
    - **البطل (علي)** : « – الصورة في الشعر العربي. بيروت. دار الأندلس. 1980 »
    - **البياتي ( عادل)** : « – دراسات في الأدب الجاهلي – الدار البيضاء – دار النشر المغربيّة – 1987 »
    - **الحديثي (بهجت عبدالغفور)** : « – دراسات في الشعر العربي القديم. بغداد.مطابع التعليم العالي.1990. »
    - **حسين (طه)** : « 1– حديث الأربعاء. ج1.القاهرة. دار المعارف.(د.ت). » / « 2– في الأدب الجاهليّ.القاهرة. دار المعارف. »
    - **الخطيب (بشرى محمّدعلي)** : « – الرّثاء في الشعر الجاهلي وصدر الإسلام. بغداد. مطبعة الإدارة المحلّية. 1978 »
    - **روميّة (أحمد وهب)** : « – الرّحلة في القصيدة الجاهليّة.مصر . مطبعة المتوسّط.1985. »
    - **الصّائغ (عبد الإله)** : « 1–الخطاب الإبداعي الجاهليّ والصّورة الفنّية.الدّار البيضاء. المركز الثقافي العربي..1997 » / « 2– الزّمن عند الشعراء العرب قبل الإسلام.بغداد. دار الرّشيد للنشر. 1982. »
    - **عبد الرّحمان ( عفيف)** : « – مكتبة العصر الجاهليّ وأدبه. بيروت. دار الأندلس.ط1. 1984. »
    - **عبد الرحمان (نصرت)** : « – الصورة الفنية في الشعر الجاهلي. عمّان.مطبعة وزارة الأوقاف.1986. »
    - **عبد الصّبور (صلاح)** : « – قراءة جديدة لشعرنا القديم. بيروت. دار النّجاح. 1973. »
    - **عبدالله (محمد الصادق حسن)** : « – خصوبة القصيدة الجاهليّة ومعانيها المتجدّدة.القاهرة. دار الفكر العربي.1997 »
    - **عجينة (محمد)** : « – أساطير العرب عن الجاهلية ودلالاتها. بيروت.دار الفارابي. 1994 »
    - **عوض (ريتـا)** : « – الصورة الشعرية في ديوان امرئ القيس. أطروحة دكتورا دولة .الجامعة التونسيّة.1989.–1990. »
    - **الغيضاوي (علي)** : « –الإحساس بالزّمان في الشعر العربي من الأصول حتّى نهاية القرن الثّاني للهجرة ج 1 و 2 – منشورات كلّية الآداب.منّوبة 2001 »
    - **ناصف (مصطفى)** : « 1–قراءة ثانية لشعرنا القديم. بيروت. دار الأندلس. 1981. » / « 2 صوت الشاعر القديم.مصر. الهيئة المصرية العامة للكتاب.1992 »
    - **النعيمي ( أحمد إسماعيل)** : « – الأسطورة في الشعر العربي قبل الإسلام. مصر.دار سينا للنشر.1995. »
    - **الواد (حسين)** : « – جماليّة الأنا في شعر الأعشى الكبير. المغرب الأقصى. المركز الثّقافي العربي – ط1 / 2001 »

    **2- الكتب (بغير اللسان العربي)** (p.83) :
    - **ABDESSELEM (Mohamed)** : « - Le thème de la mort dans la poésie arabe, Tunisie Publications de l'université de Tunis. 1977. »
    - **NALLINO (Carlo)** : « - La littérature arabe des origines à l'époque de la dynastie Umayyade, traduction de Charles Pellat: Paris 1950. »
    - **PELLAT (Charles)** : « - Langue et littérature arabes. Paris, Collection U2. A. Colin. 1970. »

    **3- الدّوريّات** (p.83) :
    - **بريري ( محمد أحمد)** : « –الليل والنّهار في معلّقة امرئ القيس. مجلة فصول المصريّة (قراءة الشعر القديم).المجلّد 14. العدد2.صيف1995 »
    - **بووانو ( إدريس)** : « –كيف تلقّى العرب القدامى الشّعر؟. مجلّة عالم الفكر. الكويت. المجلّد32. العدد2.ديسمبر2003. »
    - **جمعة (حسين)** : « – البيئة الطبيعية في الشعر الجاهليّ. مجلّة عالم الفكر. الكويت. المجلّد25. العدد3.مارس1997. »
    - **داجليش (ك)** : « – بعض ملامح معالجة العاطفة في ديوان الأعشى. ترجمة رفعت سلاّم. مجلة فصول المصريّة (قراءة الشعر القديم).المجلّد 14. العدد2.صيف1995 »
    - **روميّة (وهب أحمد)** : « – شعرنا القديم والنّقد الجديد. سلسلة عالم المعرفة.العدد207. الكويت. مارس 1996. »
    - **ستيتكيفيتش (سوزان)** : « – القصيدة العربية وطقوس العبور :دراسة في البنية النموذجية.مجلّة المجمع اللّغوي بدمشق/سوريا. المجلّد 60.السنة 1985. »
    - **ستيتكيفتش (ياروسلاف)** : « –الاسم والنعت : رموز الحيوان في الشعر العربي القديم. ترجمة حسنة عبد السّميع. مجلة فصول المصريّة (قراءة الشعر القديم) المجلّد14. العدد2.صيف1995. »
    - **فان جلدر(هـ.)** : « –الأنواع في تعارضها : النّسيب والفخر. ترجمة خيري دومه. مجلة فصول المصريّة (قراءة الشعر القديم) المجلّد14. العدد2.صيف 1995. »

- **Blocs transversaux au محور** — relevés sur l'ensemble du محور الأوّل (p.5–83) : ils valent pour les
  cinq chapitres C1→C5 et ne sont pas répétés dans les sections suivantes.

- **Concepts / notions** :

  - **Histoire littéraire et périodisation** : le sens du mot « الجاهليّة » (acception lexicographique, coranique, critique moderne) ; « الجاهليّة » comme terme forgé avec l'islam pour distinguer deux époques ; la dérivation du mot depuis السّفه / الغضب / النزق et non depuis الجهل contraire de العلم ; les 4 occurrences coraniques du mot ; le عصر الجاهليّ comme « منظومة علاميّة » (avec ses سنن et ses أغراض) selon l'avant-propos p.4.
  - **Transmission du texte** : الرواية vs التدوين ; les trois دعامات (رواية الشعراء عن بعضهم / رواية القبائل لشعر شعرائها / حَفَظَة الشعر والأخبار) ; les « مدارس » de transmission ; l'effet de la مشافهة sur la circulation de vers quasi identiques d'un poète à l'autre (إضاءات p.24) ; les variantes de رواية (النحّاس، نسخة الطوسي, p.74) ; la collecte tardive du ديوان de طرفة par ابن السِكِّيت au 3ᵉ siècle de l'hégire ; le rôle des anthologies (شرح المعلّقات السبع للزوزنيّ، شرح القصائد السبع الطوال الجاهليات للأنباري، جمهرة أشعار العرب للقرشيّ، حماسة أبي تمّام).
  - **Société jahilite** : القبيلة, الأحلاف القبليّة ; أهل المدَر / أهل الوبَر ; القبائل المقيمة / المترحّلة ; الملوك / غير الملوك، زرّاع / تجّار ; الأنساب — القبائل العدنانيّة / القحطانيّة ; حرب داحس والغبراء, حرب البسوس ; عكاظ ; les rois (المناذرة / الغساسنة، عمرو بن هند، النعمان بن المنذر) ; les valeurs — الفتوّة، الكرم / الجود، الوفاء، النجدة، الحماية (الجار، الوديعة)، الحميّة، الثأر (الأوتار).
  - **Structure de la قصيدة** : la بنية ثلاثيّة (النسيب / الرحيل / الفخر-المديح) ; الاستهلال الطّلليّ, الوقفة الطلليّة, النسيب, وصف الراحلة/الرحلة, ثم الغرض ; les مقدّمات comme « موطّئات » ; le principe de التناسب بين الأقسام et de عدل بين الأقسام (ابن قتيبة) ; le طلل comme رمز للموت والفناء ; القصيدة vs المقطّعة / القطعة ; le débat موقف النقّاد القدامى / الدراسات الحديثة (الوحدة العضوية، الثنائية الضدية، البناء العميق) ; la comparaison de la قصيدة au corps humain (الحاتميّ) ; « عمود الشعر ».
  - **Les أغراض** : les cinq retenus par le manuel — **المدح، الفخر، الغزل، الرثاء، الهجاء** (p.34) ; leur حدّ, leurs مراكز اهتمام et leurs وظائف (توثيقيّة، اجتماعيّة سياسيّة / اعتباريّة سياسيّة، قيميّة نفسيّة، تأثيريّة، جماليّة، تأسيسيّة) ; النسيب, الغزل البدوي / الغزل الحضريّ ; الرثاء = التفجّع + التأبين ; الحكمة comme المثل سائر ; les خمريّات et le مجلس الشراب ; الحماسيّة ; وصف الخيل / وصف الناقة ; le مقام الشعريّ (schéma p.34 : الباتّ/الشاعر — الرّسالة — المتقبّل/السامع، السّنن، المرجع، النّموذج : الاتباع والابتداع).
  - **Rhétorique (البلاغة)** rencontrée nommément : **التشبيه** (et أركان التشبيه، صنف التشبيه) ; **الاستعارة التصريحيّة** (avec قرينة مانعة, مشبّه / مشبّه به) ; **الاستعارة المكنيّة** ; **الكناية** et **الكناية عن موصوف** ; **المجاز اللّغويّ** vs **المجاز العقليّ** (إسناد مجازي) ; **الجناس** (dont **الجناس الجزئي** et **الترديد** comme espèce de جناس) ; **ردّ الأعجاز على الصدور** ; **التسميط** (الموازنة، حسن التقسيم، التقفية الداخليّة) ; **الالتفات** ; **الترجيع** ; **تأكيد المدح بما يشبه الذمّ** (محسّن معنوي، بديع) ; **مجاورة لفظيّة** ; **مؤاخاة معنويّة** ; **الإيجاز** (قسم من علم المعاني) ; **الطباق والمقابلة** ; **الحقل المعجميّ** / **الحقل الدّلاليّ**.
  - **Prosodie (العروض)** : les mètres présents dans le محور — **الطويل، الكامل، البسيط، الوافر، المتقارب** ; le **تقطيع عروضيّ** avec relevé des « تغييرات » (demandé p.24, p.54, p.71) ; les **تفعيلات** relevées dans le tableau p.75 (« متفعلن فعلن »، « مستفعلن فعلن ») ; l'**إيقاع الداخليّ** et les **ظواهر إيقاعيّة** ; les **صيغ صرفيّة** comme facteur de rythme ; la **ضرورة شعريّة / جواز شعري** (glose de « انعاني », p.63).
  - **Grammaire et morphologie servies par l'appareil** : le retour du mot à sa racine (الجذر) puis à sa صيغة, sa présence قاموسيّة et سياقيّة — principe explicite de la rubrique الشـرح, annoncé p.4 ; صفة مشبّهة، اسم فاعل، اسم مفعول، صيغة مبالغة، اسم آلة، اسم مرّة، مصدر، المشتقّات ; حرف التحضيض / التنديم « هلاّ » ; حرفا الاستقبال « السين » و« سوف » ; « واو ربّ » ; حرف التحقيق « قد » + الناسخ الفعليّ « كان » ; أفعال الظنّ (خال / إخال) ; المفعول المطلق ; الإنشاء الطلبيّ (الدعاء) vs الخبر ; الترخيم (نُعْم، حارِ، حار) ; بنية الضمائر (أنا / أنت / هو / هم) ; بنية الشرط.

- **Vocabulaire officiel** (relevé dans le manuel) : « مراكز الاهتمام » ; « ورقة منهجيّة » ; « كيف أقـرأ » ; « تمهيــد » ; « اعرف » ; « الأعلام » ; « الأماكن » ; « الشـرح » ; « فكّك » ; « حلّل » ; « قوّم » ; « توسّع » ; « إضاءات » ; « شذرات » ; « نصوص تمهيديّة » ; « نصوص مختارة » ; « نصوص تكميليّة » ; « فهرس المحور » ; « ترتيب النّصوص » ; « ثبت بيبليوغرافي » ; « مشجّر بأنساب القبائل العربيّة وبعض شعرائها » ; « تذليل صعوبات المعجم » ; « الحفز على التفكيك » ; « الدّعوة إلى تحليل » ; « التّقويم » ; « التوسّع » ; « الغرض الشعريّ » ; « حدّ الغرض » ; « مداخل الأغراض الشعريّة » ; « المقدّمات » ; « المقام الشعريّ » ; « السّنن » ; « المرجع » ; « النّموذج: مظاهر الاتباع والابتداع » ; « الرّسالة (الخطاب الشعريّ ذاته) » ; « المتقبّل » ; « الباتّ » ; « غرض الفخر » ; « غرض المدح » ; « غرض الرثاء » ; « غرض الغزل » ; « الهجاء » ; « النّسيب » ; « الغزل البدوي » ; « الغزل الحضريّ » ; « الاستهلال الطّللي » ; « الوقفة الطلليّة » ; « الحكمة » ; « التفجّع » ; « التأبين » ; « الفتوّة » ; « معاني القدرة والسطوة » ; « معاني السيادة » ; « النسب وطيب المحتد » ; « الأرومة » ; « السخاء والجـود » ; « البطش والقوّة » ; « النجدة والبأس » ; « الفروسيّة » ; « الوظيفة التوثيقيّة » ; « الوظيفة الاجتماعيّة السياسية » ; « الوظيفة الاعتباريّة السياسية » ; « الوظيفة القيميّة النفسيّة » ; « الوظيفة التأثيريّة » ; « الوظيفة الجماليّة » ; « الوظيفة التّأسيسيّة » ; « الوظيفة النفسيّة » ; « التشبيه » ; « أركان التشبيه » ; « الاستعارة تصريحيّة » ; « استعارة مكنيّة » ; « قرينة مــانعة » ; « المشبّه » ; « المشبّه به » ; « المجاز اللغويّ » ; « المجاز العقليّ » ; « إسناد مجازي » ; « كناية عن موصوف » ; « الأسلوب الكنائـي » ; « وجه من وجوه البيان » ; « الجناس » ; « جناس جزئي » ; « ترديد » ; « ردّ الأعجاز على الصدور » ; « تسميط » ; « الموازنة » ; « حسن التقسيم » ; « التقفية الداخليّة » ; « الالتفات » ; « ترجيع » ; « تأكيد المدح بما يشبه الذمّ » ; « محسّن معنوي » ; « البديع » ; « مجاورة لفظيّة » ; « مؤاخاة معنوية » ; « إيجاز » ; « علم المعاني » ; « الطباق والمقابلة » ; « الحقل المعجميّ » ; « الحقل الدّلاليّ » ; « تقطيع عروضيّ » ; « تحليلا عروضيّا تامّا » ; « ما طرأ عليه من تغييرات » ; « تفعيلة » ; « البحر » ; « من الطّويل » ; « من الكامل » ; « من البسيط » ; « من الوافر » ; « من المتقارب » ; « المعلّقة » ; « المذهّبة » ; « المطلع » ; « المقطّعات » ; « المقطوعة » ; « القطعة » ; « الأبيات المُفْرَدَة » ; « المطوّلات » ; « الطبقة الأولى » ; « شاعر مخضرم » ; « الرواية » ; « المشافهة » ; « التدوين » ; « حَفَظَة الشعر والأخبار » ; « الرُّواة » ; « الشّرّاح » ; « عمود الشعر » ; « البنية الثلاثية » ; « أهل المدَر » ; « أهل الوبَر » ; « نازلة العمد » ; « القبائل المترحّلة » ; « القبائل المقيمة » ; « القبائل العدنانيّة » ; « القبائل القحطانيّة » ; « الأحلاف القبليّة » ; « صفة مشبّهة » ; « اسم فاعل » ; « اسم مفعول » ; « صيغة مبالغة » ; « اسم آلة » ; « اسم مرّة » ; « المشتقّات » ; « الصيغ الصرفيّة » ; « حرف تحضيض » ; « حرف تنديم » ; « حرف استقبال » ; « واو ربّ » ; « حرف التحقيق » ; « الناسخ الفعليّ » ; « أفعال الظن » ; « مفعولا مطلقا » ; « إنشاء طلبيّ » ; « الإنشاء والخبر » ; « الترخيم » ; « جواز شعري من باب الضرورة » ; « بنية الضمائر » ; « الإجمال والتفصيل ».

- **Textes & exemples types (manuel élève)** :
  - **معلّقة طرفة بن العبد** en 4 textes successifs — « خَوْلَةَ أَطْلَالٌ » (p.22), « عَوْجَاءُ مِرْقَالٌ » (p.25), « ثَلاَثٌ هُنَّ من عِيشَةِ الفَتَى » (p.28), « سَتُبْدِي لَكَ الأَيَّامُ مَا كُنتَ جَاهِلاً » (p.31) — le seul poème traité comme un parcours complet (طلل → نسيب → راحلة → فخر → حكمة), avec la notice d'auteur p.21.
  - « لنَا الدُّنيا ومن أضْحَى علَيْهَا », عمرو بن كلثوم (p.35) — la فخريّة tribale par excellence, mètre الوافر.
  - « أغْشَى الوَغَى عند المَغْنَم », عنترة (p.38) et « لَيْسَ عَلَى نَارِي حِجَابٌ », حاتم الطائي (p.41) — les deux visages du فخر : البطش et الجود ; illustration pleine page de la tente et de la marmite p.43.
  - « إنِّي مَانِعٌ جَارِي », الأعشى (p.45) — le مدح adossé au récit du السموأل (وفاء) ; « ضرّابُ الكُمَاةِ », زهير بن أبي سلمى (p.49) — le مدح canonique de هرم بن سنان.
  - « حامِي العرين », الخنساء (p.53) et « تَلَفٌ مُقيمٌ », أبو ذؤيب الهذلي (p.56) — le رثاء sous ses deux faces (تفجّع / تأمّل).
  - « بَدَا لِي وَجهُ نُعْمٍ », النابغة الذبياني (p.60) et « يَا طَائِرَ البَانِ », عنترة (p.63) — النسيب et الغزل.
  - « تَدَاوَيْتُ مِنهَا بهَا », الأعشى (p.66) — la خمرة et le مجلس الشراب ; « مِنْ حِكَمِ الجَاهِلِيِّينَ », زهير (p.69) — les 14 vers de حكمة de sa معلّقة.
  - « الخَيْرُ بِنَوَاصِي الخَيْلِ مَعْصُوبُ », امرؤ القيس (p.73) — la description du cheval et la scène de chasse, avec le tableau de تقطيع du vers 4 (p.75) ; planche Franz Marc p.72 et son bandeau de vers.
  - **Prose critique** : « في بنيَةِ القَصِيدَة », ابن قتيبة (p.77) — le texte de référence sur les أقسام القصيدة, cité en renvoi dans le قوّم du texte 4 (p.33) ; « هيكل القصيدة الجَاهليّة… », سوزان ستيتكيفيتش (p.79) ; « هاجسُ الرّحيل… », وهب أحمد رومية (p.81).
  - **Documents non textuels** : cartes p.7 (توزيع القبائل العربيّة قبل ظهور الإسلام) et p.8 (الأحلاف القبليّة) ; مشجّر الأنساب p.17–18 ; peinture « واحــــــــة » du الحبيب بلال p.20.

- **Bornes de scope** :

  - ✅ **INCLUS** — adossé aux « مراكز الاهتمام » du فهرس p.6, aux encadrés « مراكز الاهتمام » des textes تمهيديّة/تكميليّة et aux 5 ورقات منهجيّة :
    - Le **sens du mot الجاهليّة** dans les dictionnaires, dans le Coran (4 occurrences) et dans quelques lectures critiques modernes (جواد علي، شوقي ضيف).
    - Les **voies de transmission** du شعر جاهلي de la رواية au التدوين : les trois دعامات.
    - La **société tribale** : tribus sédentaires / nomades, أهل المدر / أهل الوبر, l'implantation dans les grandes villes arabes avant l'islam, l'image du milieu tribal chez quelques historiens anciens, la généalogie des tribus عدنانيّة / قحطانيّة et le rattachement des poètes du corpus.
    - Les **cinq أغراض** retenus par le manuel — المدح، الفخر، الغزل، الرثاء، الهجاء — avec pour chacun des quatre traités en ورقة منهجيّة son حدّ, ses مراكز اهتمام (معاني + صفات وصور) et ses وظائف ; les مداخل (الوقفة الطلليّة، النسيب، وصف الرحلة) ; le مقام الشعريّ et ses composants.
    - Les **thèmes-supports du corpus** : الاستهلال الطّللي والنسيب ; صفة الرّاحلة ووظائفها ; le فخر (اللهو ومفهوم الفتوّة، تفصيل المناقب، الفخر بالقبيلة، الفخر بالذات، الفخر بالمحامد والشّيم) ; le مدح (مدح المآثر، مدح الفروسيّة والشّيم) ; le رثاء (التفجع والتأبين، التفجع والتّأمّل) ; le نسيب et le غزل (مكوّناته ومعانيه، أحوال المحبّ) ; صفة الخمرة وصورة مجالس الشراب ; الحكمة : منظومة القيم عند الجاهليّين ; صفة الخيل وصلتها بعالم الصحراء.
    - La **structure de la قصيدة** : ses أقسام et les causes de leur agencement chez **ابن قتيبة**, la condition de تناسب, la position des critiques anciens et modernes sur la بنية (y compris la question de la مقطوعة), et les **تجليّات du الرّحيل** avec sa dimension cognitive.
    - Les **faits de langue, de rhétorique et de prosodie** effectivement nommés par les rubriques `إضاءات` et `توسّع` (liste complète au § Vocabulaire officiel) — c'est le périmètre exact de ce qui est enseignable ici, y compris les exercices de تقطيع عروضيّ et de حقل معجميّ/دلاليّ.
    - Le **lexique glosé** dans les rubriques `الشـرح` (≈ 200 entrées au total sur les 16 textes مختارة + 8 pour le تكميلي 1), avec sa méthode explicite : racine → صيغة → sens lexical → sens en contexte.

  - ⛔ **EXCLU (relève d'un autre chapitre/niveau)** :
    - Le **تجديد du 2ᵉ siècle de l'hégire** — c'est le **محور الثاني**, « التجديد في الشعر العربيّ في القرن الثاني للهجرة », qui ouvre **p.85** ; son فهرس (p.86–87) énumère 2 textes تمهيديّة, 15 مختارة et 3 تكميليّة, avec des مراكز اهتمام propres (الرّسالة الشعريّة، الثورة على القديم وقيمه، المقدّمة الحكميّة، بنية الأرجوزة، الخمر والطبيعة، الصّنعة الشّعريّة، الزّهديّة، بشّار / أبو نواس / أبو العتاهيّة…). Rien de ce périmètre ne doit être généré sur le compte du محور 1 — même quand un fait de langue ou un procédé est commun aux deux.
    - Toute mention de شعراء ou de faits du 2ᵉ siècle apparaissant **incidemment** dans le محور 1 (par exemple les allusions à « شعر عمر وبعض غزليّات بشار » et aux « شعراء القرن الثاني » dans la ورقة منهجيّة du غزل p.65, ou la thèse de la prédominance de l'استعارة « على شعر المحدثين في العصر العبّاسيّ » dans le شذرة p.71) : ces phrases situent le جاهلي par contraste, elles n'ouvrent pas le programme du محور 2.
    - La **نادرة** — objet du **محور الثالث**, hors de la tranche relevée : rien n'en est transcrit ici.
    - La **رومنطيقيّة** — objet du **محور الرابع**, dans le **tome 2** : hors de ce fichier.
    - Le **récit / roman** et le **théâtre** — **tome 2** : hors de ce fichier.
    - Les **zones illisibles**, sur lesquelles **aucune** question ne doit être générée :
      - **p.7** et **p.8** — noms de tribus et de lieux portés sur les deux cartes, contenu des cartons et des boîtes de légende (écriture manuscrite trop fine). Seules les légendes imprimées sous les cartes et leur référence sont sûres.
      - **p.75** — les schémas métriques du tableau de تقطيع (suites de « – » et de « 0 ») : l'ordre exact des symboles n'est pas garanti au pixel.
      - **p.59** et **p.65** — les étiquettes verticales de groupe des tableaux « مراكز الاهتمام » (lectures probables `التفجّع` / `التأبين` p.59 ; `ما اتّصل بالحبيبة` / `ما اتّصل بالفتى العاشق` p.65) : à confirmer sur l'original avant toute exploitation.
      - **p.72** — le premier mot du vers calligraphié du bandeau (lu « والخيرُ ») : ne pas en faire un item.
      - **p.54** — le manuel ne porte **pas** de tableau de تقطيع : il n'y a là qu'une **consigne** de `توسّع` (« قطّع البيت تقطيعا عروضياً: … »), sans corrigé ; rien à générer sur un tableau qui n'existe pas.
    - Les **coquilles et anomalies du manuel**, à ne jamais transformer en item de connaissance : « دار صادر » (p.22, p.35, p.41, p.49, p.53) ; le renvoi 14 absent du corps p.25 ; le décalage de numérotation du شرح p.29 ; le renvoi « 21 » du vers 13 p.31 glosé n° 12 p.32 ; « السّعاة » p.33 ; le أ masqué de « أغراض » p.34 ; les lemmes « ديّك » et « وّار » et la glose « بضمّ الميم » p.47 ; « نهاية الأرب » p.56 ; la référence « العمدة ج 397، » p.60 ; le doublon « حاسّة الشم » p.62 ; « بن » pour « بين » et « فحريّة » pour « فخريّة » p.63–64 ; le lemme « لمنايا » p.70 ; « لأنّه ز أوّل » p.73 ; « بفتح الميم » p.74 ; « الافناء » et « عاملاَ » p.75 ; « إسم » p.78 ; « الالتفاتا » p.58.

## C2 Chapitre 2 — المحور الأوّل : الشّعر الجاهلي — غرض الفخر (`02-gharad-fakhr`, tome 1, p.35–44, transcrit à profondeur de génération)

Chapitre du **غرض الفخر** : les trois فخريّات que le manuel range entre la ورقة « الغرض الشعريّ » et la
ورقة du فخر — « لنَا الدُّنيا ومن أضْحَى علَيْهَا » de عمرو بن كلثوم (p.35, le **الفخر بالقبيلة** selon le فهرس p.6),
« أغْشَى الوَغَى عند المَغْنَم » de عنترة (p.38, le **الفخر بالذات**) et « لَيْسَ عَلَى نَارِي حِجَابٌ » de حاتم
الطائي (p.41, le **الفخر بالمحامد والشّيم**, avec l'illustration pleine page p.43) — puis la **ورقة منهجيّة**
« كيف أقـرأ : غرض الفخر » (p.44) qui les synthétise.

⚠️ **Textes 3 et 4 non rattachés ici, à dessein.** Le فهرس p.6 les étiquette « غرض الفخر » (اللهو ومفهوم
الفتوّة، تفصيل المناقب) mais le manuel les lit **dans la معلّقة de طرفة**, comme deux moments d'un parcours
continu qu'il clôt par la ورقة « الغرض الشعريّ » p.34 — ils restent donc en **C1** avec les deux autres
extraits de la même معلّقة. Le فخر y est déjà à l'œuvre, sa **doctrine** est ici.

- **Montage (fidèle au manuel)** :

  - **النصوص المختارة du chapitre** (p.35–43) :

    **Texte 5 — « لنَا الدُّنيا ومن أضْحَى علَيْهَا »** · auteur **عمرو بن كلثوم التّغلبي** · mètre **(من الوافر)** · **21 vers** · référence : « من معلقة عمرو بن كلثوم – شرح المعلّقات السبع للزوزني / تحقيق كرم البستاني–دار صادر، بيروت،د.ت. » · **p.35–37**.
    - **Incipit verbatim** : « متَـى نـنْقُـلْ إلَى قَـوْمٍ رَحَانَـا — يكُونُوا فِـي اللِّقَاءِ لَـهَا طَحِينَـا »
    - `تمهيد` — substance : l'événement (le meurtre de عمرو بن هند, roi de الحيرة) comme déclencheur d'une fخرية tribale « تقرن البطش والسطوة بالسخاء والكرم » ; le مطلع de la مذهّبة est cité : « ألاَ هُبِّي بِصَحْنِكِ فَاصْبِحِينَا — ولاَ تُبْقِي خُمُورَ الأَنْدَرِينَا ».
    - `اعرف` — **12 entrées de الشـرح** (ثفالها، لهوتها، القرى، مرداة، ونينا، الجلّة، الدّرينا، صالوا، النهاب، قبب، قدرنا، خسفا) ; **الأماكن** : نجد، ذو أراطى ; **الأعلام** : عمرو بن كلثوم بن عتاب، معدّ، بنو الطمّاح ودعميّ، قضاعة.
    - `فكّك` : « في النص مراوحة بين التعريف بالأحوال والإخبار عن الأفعال، قطع القصيدة مستأنسا بهذا المعيار. »
    - `حلّل` : 1. « أبرز القيم التي تدين بها قبيلة الشاعر. » 2. « استخلص مقومات المجتمع الجاهليّ وبين أشكال العلاقات بين القبائل. » 3. « سادت في القصيدة تراكيب بعينها أسهمت إلى حد بعيد في إنشاء النبرة الحماسية الفخرية، حدّدها وبيّن دورها في بناء غرض الفخر. » 4. « في القصيدة تصوير لبنية الجيش، استخرجه وحدّد دوره في بناء المعاني الفخرية. » 5. « الخطاب الفخريّ خطاب تفرّد، فبم توسل الشاعر لتصوير الذات القبلية؟ »
    - `قوّم` : « إلى أيّ مدى تستجيب معاني هذه القصيدة لمفهوم الجاهلية؟(يمكن الاستعانة بالنصّ التمهيدي الأوّل لبناء إجابة معلّلة) »
    - `توسّع` : « تبيّن دور الصيغ الصرفية المعتمدة في إنشاء إيقاع داخليّ لهذه الحماسيّة. » ; « ابحث عن المعاني الفخرية الخاصّة والمشتركة في معلّقة طرفة وقصيدة عمرو بن كلثوم. »
    - `إضاءات` : figure nommée **استعارة تصريحيّة** sur « مرداة » (le مشبّه به, la meule, mis pour la guerre : « وقد صرّح المتكلم بالمشبّه به وغيّب المشبّه »).
    - `شذرات` : **أدونيس، مقدمة للشعر العربي / دار العودة بيروت،1983.ص 29.** — le الكرم comme « الوجه الآخر لكبرياء التمرد » et la فروسية comme « حسّ الكفاح ضد الدهر ».

    **Texte 6 — « أغْشَى الوَغَى عند المَغْنَم »** (titre imprimé sur le texte ; le فهرس p.6 le nomme « أغشى الوغى وأعفّ عند المغنم ») · auteur **عنترة** (عنترة بن شدّاد العبسي) · mètre **(من الكامل)** · **17 vers** · référence : « معلقة عنترة / من ب 38 إلى ب 47،ثم من ب 65 إلى ب 70 / عن "شرح القصائد السبع الطوال الجاهليات" للأنباري / تحقيق عبد السلام محمد هارون، دار المعارف، مصر، ط II، 1969 » · **p.38–40**.
    - **Incipit verbatim** : « وَلَقَدْ شَرِبْتُ مِن المدَامَةِ بَعْدَمَا — ركَـدَ الهَوَاجِـرُ بالمَشُوفِ₁ المُعْلَمِ » ; dernier vers : « ولَقَدْ شَفَى نَفْسِي وأَبْرَأَ سُقْمَهَا — قِيلُ الفَوَارِسِ ويكَ₁₂ عنتَرَ أقْدِمِ »
    - `تمهيد` (verbatim intégral) : « لم يقنع عنترة بالمنزلة التي كان فيها فاتخذ من شمائله وحسن بلائه في الحروب أسبابا ترفعه إلى مصافّ الفتيان والفرسان، وفي فخره نغمة تمجّد الذّات وتجعل الجمـع في حاجة إلى الفرد، ومثل ذلك هذه الأبيات المصطفاة من معلقته الشهيرة التي أنشدها يوم ناوشه أحد بني عبس وعيّره بسواده ومطلعها: هلْ غادَرَ الشُّعَرَاءُ مِن مُتَرَدَّمِ أمْ هلْ عَرَفْتَ الدَّارَ بَعدَ تَوَهُّمِ »
    - `اعرف` — **12 entrées de الشـرح** (المشوف، أزهر، مفدّم، نهد، يجرّد، حومة، لم أخم، يتذامرون، أشطان، لبان، تسربل، ويك) ; **الأعلام** : عنترة بن شدّاد العبسي (« حضـر حرب داحس والغبراء بين قبيلتي عبس وذبيان … توفّي على أشهر الروايات سنة 600م »).
    - `فكّك` : « قام النص على تفصيل وبيان الخصال الحربيّة وتصوير حاجة المقاتلين إلى الشاعر الفارس، وعاقب المتكلّم بين وصف الأحوال وسرد الأعمال.تخيّر مما سبق ما يساعدك على تقطيع النص واتخذه معيارا. »
    - `حلّل` : 1. « ما صلة وصف الخمرة بمفهوم الفتوّة؟ » 2. « في القصيدة تعاقب بين الأحوال والأعمال، استخرج نماذج منها مبيّنا أهميتها التعبيريّة في إنشاء المعاني الفخرية. » 3. « بم تعلّل جمع الشاعر بين السّماحة والبطش؟ » 4. « انغلق النص براحة نفسية وجدها المتكلّم في فعل القتال،فهل لك أن تستخلص ملامح تطور شخصيّة عنترة بين بداية القصيدة ونهايتها. »
    - `قوّم` : « – وازن بين هذه الفخرية وفخرية عمرو بن كلثوم متبيّنا مواضع الائتلاف والاختلاف. »
    - `توسّع` : « – تبيّن أركان التشبيه في المثال التالي: يدْعُـونَ عنتَـرَ والرِّمَـاحُ كَأنَّهَـا أشْطَـان بِـئْـرٍ فِـي لَبَـانِ الأَدْهَـمِ » ; « – اختزل المعاني الفخرية في ثلاث كلمات مفاتيح. »
    - `إضاءات` : (a) le fait de langue **« هلاَّ »** — « تختص بالدخول على الجملة الفعلية المثبتة » : « حرف تحضيض يدخل على المضارع، فَيفيدُ الحضّ على العمل وترك التهـــاون به، كقولك(هلاَّ تعملُ). » et « حرف تنديم يدخل على الماضي، فيكون معناه جعل الفاعل يندم على فوات الأمر والتهاون به، كقولك(هلاَّ اجتهدت). » ; (b) figure nommée **المجاز العقليّ** (« فإسناد الفعل في هذا الموضع مجازي ويدعى المجاز العقليّ،وهو وجه من وجوه البيان »).
    - `شذرات` : **د.وهب أحمد روميّة / شعرنا القديم والنقد الجديد، ص 222.** — la valeur de la force dans le شعر جاهلي, « قعقعة السّــيوف وتقصّد الرماح وصرير الدروع وصهيل الخيل ».

    **Texte 7 — « لَيْسَ عَلَى نَارِي حِجَابٌ »** · auteur **حاتم الطائي** · mètre **(من الطويل)** · **11 vers** · référence : « ديوان حاتم الطائي / دار صادر، لبنان،1981 / ص—ص 62—63 » · **p.41–43**.
    - **Incipit verbatim** : « إذا ما بخيلُ النّاسِ هرَّت كلابُـهُ — وشـقَّ على الضَّيفِ الضّعيفِ عَقُورُها » ; dernier vers : « سَيَبْلغُهَا خَيْـري، ويرجعُ بَعْلُـها — إلَيْـهَا ولَمْ تُقْصَرَ عَلَيَّ سُتُورُها »
    - `تمهيد` (verbatim intégral) : « لم يكن غرض الفخر مقصورا على معاني البطش والفتك، بل من الشعراء من جعل الجـود والسخاء عنوانين للمآثر فكان إتلاف المال معادلا لإهلاك الخصوم يوم اللقاء، وقد تفرد حاتم الطائي بهذه الخلال حتى بلغتنا أخباره قبل أشعاره وصارت مضرب أمثال في المفاضلة فقيل "أجود من حاتم". »
    - `اعرف` — **9 entrées de الشـرح** (أقرّت، يعتريني، أمحلوا، أوثفها، أميرها، عقيرا، أثيرها، مستوبص، يطورها) ; **الأعلام** : حاتم الطائي (« أبو عديّ حاتم بن عبد الله بن سعد الطائيّ … توفي سنة578 للميلاد كما يرى الزّركلي »).
    - `فكّك` : « تجلّت سماحة حاتم في سلوك كلابه وحرصه على الجود وصونه الأعراض، قطّع النص مستعينا بهذه الإيضاحات. »
    - `حلّل` : 1. « أبرز مكارم حاتم الطائي من خلال أحواله وأفعاله. » 2. « عمد الشاعر إلى الأسلوب الكنائـي القائم على التلميح،فما الكنايات التي اعتمدها وما غرضه من ذلك؟. » 3. « راوح الشاعر بين تراكيب مثبتة وأخرى منفيّة، استخلصها وبين دورها في تحديد معاني الفخر. » 4. « قـدّم الشاعر نفسه نموذجا للبذل والسخاء، فهل تجد بين هاتين الخصلتين وبين مفهوم الفتـــوة صلة؟ عَلِّلْ إجابتك. »
    - `قوّم` : « –أجْرِ مقارنةً بين هذه الفخريّــة وسابقتيها، إلامَ تخلص؟ »
    - `توسّع` : « – ابحث في ديوان حاتم عن قصائد أخرى في موضوع الكرم مقارنا بينها وبين نصّ الحال. » ; « – اجعل القصيدة خبرا يروى على لسان أحد ضيوف حاتم ينوّه في شمائل مضيفه وحميد صفاته. »
    - `إضاءات` : (a) fait de langue — **حرفا الاستقبال « السين » و« سوف »** (« يدلّ أولهما على يقين المتكلّم من وقوع الحدث في المستقبل القريب ويدل ثانيهما على وقوعه في المستقبل البعيد ») ; (b) figure nommée **تأكيد المدح بما يشبه الذمّ** — « ويدعى هذا الأسلوب تأكيد المدح بما يشبه الذمّ، وهو محسّن معنوي من باب البديع. »
    - `شذرات` (p.43) : récit d'أخبار حاتم الطائي (la fille de حاتم devant le Prophète) — référence : « من أخبار حاتم الطائي، / نقلا عن "شعراء النصرانية" للأب لويس شيخو / منشورات دار المشرق بيروت، / ط 5 ، 1999، ج1 ،ص 98 . »
    - **Illustration pleine page p.43** : tente bédouine de nuit, tapis, marmite sur le feu, palmiers. Légende = le vers 5 du texte : « وَأُبْـرِزُ قِدْرِي بالفَضَاءِ، قَلِيلُـها يُـرَى غيرَ مضْنون به، وكَثِيرُهَـا ».

  - **ورقة منهجيّة** (p.44) — fiche sur parchemin déroulé, étiquette en coin « ورقة منهجيّة », titre « كيف أقـرأ », sous-titre magenta. Transcription verbatim intégrale.

    ### p.44 — « كيف أقـرأ : غرض الفخر »

    > **\* حدّ غرض الفخر**
    >
    > هو غرض من أغراض الشعر يعدّد فيه الشاعر مناقبه وخصاله مفصّلا ما امتاز به عن غيره من أفعال أو أحوال أو مقال. وقد يخرج الفخر من ذات الفرد أي الشاعر إلى الذات الكبرى أي القبيلة ، فيغدو استذكارا للأمجاد وبيانًا للمكارم.
    >
    > **\* مراكز الاهتمام في غرض الفخر** — tableau à 2 colonnes (col. droite « أهمّ معاني الفخر », col. gauche « أهمّ الصفات والصور ») ; les 3 premières lignes sont regroupées par une cellule verticale intitulée **الفتوّة** :

    | أهمّ معاني الفخر                       | أهمّ الصفات والصور                                                                                     | (groupe) |
    | -------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------- |
    | – البطش والقوّة                        | – تشبيه المتكلّم نفسه بالأسد والسيف وغيرهما.                                                           | الفتوّة  |
    | – النجدة والبأس                        | – صور الدهر والرّحى والصّخر. / – صورة الحرب. / – وصف الخيل.                                            | الفتوّة  |
    | – اللهو وسيلة لبيان المنزلة الاجتماعية | – صورة مجالس الشراب والميسر. / – صورة المرأة حبيبة وقينة.                                              | الفتوّة  |
    | –النسب وطيب المحتد                     | – تمجيد الأعراق واستعارة صورتي البيت والشجرة كناية عن الأرومة.                                         | —        |
    | – السخاء والجـود                       | – تشبيه المتكلّم نفسه بالغيم والسيل.                                                                   | —        |
    | – القدرة على مقارعة الدهر.             | – صورة الصراع بين الإنسان والزمان. / – صورة الرّحيل .                                                  | —        |
    | – الشكوى والتحذير.                     | – بيان إنكار القبيلة فضائله. / – الصبر على المكاره. / – توعّد مبغضيه من أعدائه ومنافسيه من أهله وذويه. | —        |

    > **\* وظائف غرض الفخر** — 5 cellules (de droite à gauche telles qu'imprimées) :

    | الوظيفة التوثيقيّة               | الوظيفة الاجتماعيّة السياسية                        | الوظيفة القيميّة النفسيّة | الوظيفة التأثيريّة                                                    | الوظيفة الجماليّة                      |
    | -------------------------------- | --------------------------------------------------- | ------------------------- | --------------------------------------------------------------------- | -------------------------------------- |
    | تخليد المآثر الفرديّة والجماعيّة | الذبّ عن الذّات القبليّة والذود عن المحارم والمكاسب | إقامة نموذج للبطولة       | بيان حاجة الجماعة إلى الفرد وترغيبها في اتخاذه فارسا أو سيّدا أو رمزا | منافسة الأشباه والنظراء من شعراء الفخر |

- **Concepts, vocabulaire officiel, exemples types et bornes de scope** : voir les **blocs transversaux**
  du chapitre **C1**, relevés sur l'ensemble du محور الأوّل — ils valent aussi pour ce chapitre.

## C3 Chapitre 3 — المحور الأوّل : الشّعر الجاهلي — غرض المدح (`03-gharad-madh`, tome 1, p.45–52, transcrit à profondeur de génération)

Chapitre du **غرض المدح** : les deux مدحيّات que le manuel place entre la ورقة du فخر et la ورقة du مدح —
« إنِّي مَانِعٌ جَارِي » de الأعشى (p.45, **مدح المآثر** selon le فهرس p.6, adossé au récit du وفاء de السموأل)
et « ضرّابُ الكُمَاةِ » de زهير بن أبي سلمى (p.49, **مدح الفروسيّة والشّيم**, le مدح canonique de هرم بن سنان)
— puis la **ورقة منهجيّة** « كيف أقـرأ : غرض المدح » (p.52).

- **Montage (fidèle au manuel)** :

  - **النصوص المختارة du chapitre** (p.45–51) :

    **Texte 8 — « إنِّي مَانِعٌ جَارِي »** · auteur **الأعشى** · mètre **(من البسيط)** · **20 vers** · référence : « الأعشى، الديوان / ط1. دار الجيل، بيروت، 1992 ، / ص— ص 106—109 » · **p.45–48**.
    - **Incipit verbatim** : « شُرَيْـحُ لا تَتْرُكْنِّي بَعْدَمَا عَلِقَـتْ — حِبَـالُكَ اليوْمَ بَعْـدَ القِدِّ أظْفَاري » ; dernier vers : « والصَّبْرُ مِنْهُ قَديمًـا شِيمَةٌ خُلُـقٌ — وَزَنْـدُهُ₈ في الوَفَاءِ الثَّاقِبُ الـوَارِي₉ »
    - `تمهيد` (verbatim intégral) : « لما قفل عَمْرُو بن ثعلبة * من إحدى غزواته لقي الأعشى * فأسره، فاستجار الشاعر بشُرَيح بن السَّمَوْأَل * الذي سارع إلى إجارته. فقال فيه هذه القصيدة يمدحه فيها مذكرا إيّاه بوفاء جدّه الذي حفظ وديعة امرئ القيَس، ولم يهتزّ لأذى الحـارث *، بل ضحّى بولده صونا لقيمــة الوفاء. »
    - `اعرف` — **9 entrées de الشـرح** (حار، ديّك [sic, pour هَدِيَّك]، وّار [sic, pour عَوّار]، أغمار، مذق، أدراعه، ختّار، زنده، الواري) ; **الأعلام** : عمرو بن ثعلبة، الأعشى (ميمون بن قيس، « صنّاجة العرب »، توفي سنة 7هـ)، شريح، السّموأل (« أوفى من السمـــوأل », l'histoire du dépôt d'امرؤ القيس)، الحارث بن ظالم ; **الأماكن** : بانقيا، عدن، الأبلق، تيماء.
    - `فكّك` : « – تخيّر ممّا يلي ما ترتضيه معيارا لتبيّن مقاطع القصيدة وضبط حدودها. » — « * تنوّع الضمائر: أنت – أنا – هو . / * الأساليب: الإنشاء والخبر. / * ثنائية الإجمال والتفصيل. »
    - `حلّل` : 1. « ما صلة الحديث عن الترحال بغرض المدح؟ وما قصد الشاعر من ذلك؟ » 2. « وصف الشاعر خصال السموأل بطريقتين مختلفتين، حدّدهما ثمّ بيّن خصائص كل طريقة والأساليب التي ميّزتها. » 3. « استخلص من النصّ أهمّ القيم التي انعقد عليها المدح مستأنسا بانتقال الشاعر من المخاطبة إلى الإخبار. » 4. « في القصيدة بعض مقوّمات الشّعر القصصي، استخرجها مبيّنا وظائفها. »
    - `قوّم` : « – مجّد الأعشى خصال جدّ الممدوح بَدَلَ وصف فضائل شريحٍ، فكيف تعلّل ذلك ؟ »
    - `توسّع` : « – يضرب المثل في الوفاء بالسموأل فيقال "أوفى من السموأل"، وفي ما يلي أمثال تضرب للدلالة على معاني الخيانة والسخاء والبيان.صلْ كل مثل بالمعنى الذي يناسبه. » — exercice d'appariement (l'ordre imprimé n'est pas la solution) :

      | المثل                  | معناه   |
      | ---------------------- | ------- |
      | أجود من حاتم           | الخيانة |
      | أبلغ من قُسٍّ بن ساعدة | السخاء  |
      | أغدر من قيس بن عاصم    | البيان  |

      puis « – الحقل المعجمي : استخرج من النص الكلمات المتصلة بمجالي القيم المحمودة والقيم المرذولة. » ; « – الحقل الدّلالي : ابحث عن ثلاث دلالات أخرى للفظ "هديّ". »

    - `إضاءات` : (a) la simultanéité de deux procès (« قرن المتكلّم الحدث الرئيسيّ ( جاد وابله) بالحـدث الثّانــويّ (مَا استمطروه)، فدلّ بذلك على تزامن وقوع الحدثين ») ; (b) procédé nommé **الترجيع** — « أن يحكي المتكلّم مراجعة في القول بأوجز عبارة، وأرشق سبك وأسهل لفظ، إمّا في بيت واحد أو في أبيات أوجملة ».
    - `شذرات` : le خبر du المحلّق et de l'Aعشى à عكاظ, avec les 2 vers cités « أرَقْتُ، وَمَا هَذَا السُّهَاد المؤرّقُ وَمَا بِي مِنْ سُقْمٍ وَمَا بِي مُعْشَقُ » et « نَفَى الذمَّ عن آلِ المحَلَّقِ جَفنةٌ كَجَابَية السَّيْحْ العِرَاقيّ تَفْهَقُ » — référence : « ابن رشيق. العمدة . ج 1 ص 123 ».

    **Texte 9 — « ضرّابُ الكُمَاةِ »** · auteur **زهير بن أبي سلمى** · mètre **(من الطويل)** · **15 vers** · référence : « زهير بن أبي سلمى / الديوان ط، دار صادر،بيروت— د.ت، ص23—24. » · **p.49–51**.
    - **Incipit verbatim** : « سَوَاءٌ عَلَيْـهِ أَيَّ حِينٍ أَتَيْـتَـهُ — أَسَاعَـةَ نَحْسٍ تُتَّقَى أَمْ بأَسْعُدِ₁ » ; dernier vers : « تَـزَوَّدْ إلَى يَـوْمِ المَمَاتِ فَإنَّـهُ — وَ لَوْ كَرِهَتْهُ النَّفْسُ، آخِرُ مَوْعِدِ »
    - `تمهيد` — substance : le منوال du المدح, adossé à la citation de **قدامة بن جعفر** « لمّا كانت فضائل الناس من حيث هم ناس على ما عليه أهل الاتفاق في ذلك إنّما هي العقل والعفّة والعدل والشجاعة، كان القاصد للمدح بهذه الأربع مصيبا وبما سواها مخطئا » (note « (1) قدامة بن جعفر، نقد الشعر، ص96 ») ; le مطلع est cité : « غَشِيتُ دِيَارًا بالبَقِيعِ فَثَهْمَدِ دَوَارِسَ قَدْ أَقْوَيْنَ مِنْ أُمِّ مَعْبَدِ ».
    - `اعرف` — **15 entrées de الشـرح** (أسعُد، كماة، لم يعرّد، مدره حرب، رجام، ثمال، طلق، مجلّد، نهكة، حقلّد، رهقا، متهوّد، افتراص، دهش، عارض) ; **الأعلام** : زهير بن أبي سُلْمى (توفي « سنة 611م »)، هرم بن سنان، قيس بن عيلان (renvoi explicite : « انظر مشجّر أنساب القبائل العربية »).
    - `فكّك` : « – اعمد إلى أحد المعايير التّالية فقطّع به النص : » — « * الأساليب: الإنشاء والخبر. / * بنية الضمائر: المخاطبة والإخبار. / * الموضوع: معاني المدح. »
    - `حلّل` : 1. « تواترت في النصّ صيغ صرفية، استخرجها محدّدا أنواعها وقيمتها في رسم صورة الممدوح. » 2. « صنّف المعاني المدحيّة الواردة في النص حسب المجال الذي تنتمي إليه مستخلصا أهمّ القيم التي ميّزت المجتمع الجاهلي. » 3. « تجاور في النصّ المدح والحكمة. وضّح كيف تعالقا وقيمة حضور الحكمة في المدحيّة. » 4. « هل لك أن تستخرج أهمّ وظائف الشاعر من خلال هذه القصيدة. »
    - `قوّم` : « * وازن بين هذه النصّ وسابقه لضبط أهمّ المعاني التي ينعقد عليها المدح. »
    - `توسّع` : « * تبيّن مكوّنات الصورة الشعرية ودلالاتها في الأبيات(6—7—8—9). »
    - `إضاءات` : procédé nommé **الترديد** — « أن يأتي الشاعر بلفظة متعلّقة بمعنى ثمّ يوردها متعلقة بمعنى آخر في البيت نفسه أو في قسم منه » ; exemples relevés par le manuel : (يخلد/ مخلد، وراثة/أورث؛ حمدُ/ حمد، تزوّد / تزوّد) ; « والترديد عند البلاغيّين ضرب من ضروب الجناس. »
    - `شذرات` : **طه حسين، حديث الأربعاء / ط، دار المعارف.بمصر، ج I،ص110.** — pourquoi عمر بن الخطّاب aimait le مدح de زهير (« مدحا صادقا لا يضيف إلى الرجل غير ما فيه ») ; 3 vers cités en éloge de حصن بن حذيفة بن بدر الفزاري, dont « تَرَاهُ إذا مَا جِئْتَهُ مُتَـهَـلِّـلاً كَأَنَّكَ تُعْطِيهِ الّذي أَنْتَ سَائِلُهُ ».

  - **ورقة منهجيّة** (p.52) — fiche sur parchemin déroulé, étiquette en coin « ورقة منهجيّة », titre « كيف أقـرأ », sous-titre magenta. Transcription verbatim intégrale.

    ### p.52 — « كيف أقـرأ : غرض المدح »

    > **\* حدّ غرض المدح**
    >
    > هو غرض من أهمّ أغراض الشعر العربيّ وأقدمها ، وحدّه أن يفصّل المتكلّم شمائل المخاطب وشيمه حتّى يجعله فوق الأشباه والنظراء. ولئن ذهبت فئة من النّقاد إلى كون المعاني المدحية موصولة بالفضائل التي أجمع عليها الناس وهي العقل والعفّة والعدل والشجاعة، فإنّ آخرين قد ألحقوا بهذه الصفات طائفة أخرى من حميد الشيم وكريم الخصال التي تلزم الممدوح في حالي الحرب والسلم ، واشترطوا أن تكون هذه المعاني موقوفة عليه مقترنة به لا سيّما إذا كان الممدوح سيّدا أو ملكا.
    >
    > **\* مراكز الاهتمام في غرض المدح** — tableau (col. droite « أهمّ معاني المدح », col. gauche « أهمّ الصفات والصور ») avec deux cellules verticales de regroupement : **معاني القدرة والسطوة** (3 premières lignes) et **معاني السيادة** (3 dernières) :

    | أهمّ معاني المدح   | أهمّ الصفات والصور                                                                                                                                              | (groupe)             |
    | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
    | – البطش والقوّة    | – تشبيه المتكلّم ممدوحه بالنجم والشمس والأسد والسيف وغيرها.                                                                                                     | معاني القدرة والسطوة |
    | – النجدة والبأس    | – تصوير حاجة الناس إليه. / – تشبيه غضبه بما يعتري البعير الصعب. / – تشبيه هبوبه للنجدة وصون الأعراض بالرياح والأعاصير                                           | معاني القدرة والسطوة |
    | الفروسيّة          | – قدرة الممدوح على اتخاذ الأهوال مطايا. / – بيان تفرّده عند ركوب الخيل وملاعبة الأسنّة. / – صورة الحرب.                                                         | معاني القدرة والسطوة |
    | –النسب وطيب المحتد | – تمجيد الأعراق واستعارة صورتي البيت والشجرة كناية عن الأرومة. / – بيان وسامة الممدوح لعلّة الشرف وكرم الأصل.                                                   | معاني السيادة        |
    | – السخاء والجود    | – تشبيه المتكلّم ممدوحه بالغيم والسيل. / – جعل جوائزه وعطاياه سببا للبعث. / – بيان تهلّل الممدوح وانبساطه عند السّؤال.                                          | معاني السيادة        |
    | – العقل والعفّة    | – نهوضه بواجبات السّيادة +حسن التدبير / – حسن خطاب الممدوح وأخذه بجوامع الكلم. / – بيان تعففه عن الرذائل. / – تشبيه غيرته بما يعتري ذكور حمر الوحش وفحول الإبل. | معاني السيادة        |

    > **\* وظائف غرض المدح** — 5 cellules (de droite à gauche telles qu'imprimées) :

    | الوظيفة التوثيقيّة                                 | الوظيفة الاجتماعيّة السياسية                                       | الوظيفة القيميّة النفسيّة    | الوظيفة التأثيريّة                                                   | الوظيفة الجماليّة                      |
    | -------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------- | -------------------------------------------------------------------- | -------------------------------------- |
    | تخليد مآثر الممدوح + الحطّ من قيمة أعدائه ومنافسيه | بيان حاجة الناس إليه وغناه عنهم + حمل الأفراد على طاعته رغبة ورهبة | إقامة نموذج للبطولة والسيادة | هزّه للسماح والنّوال + استدراجه إلى إثابة المادح والترغيب في اصطناعه | منافسة الأشباه والنظراء من شعراء المدح |

- **Concepts, vocabulaire officiel, exemples types et bornes de scope** : voir les **blocs transversaux**
  du chapitre **C1**, relevés sur l'ensemble du محور الأوّل — ils valent aussi pour ce chapitre.

## C4 Chapitre 4 — المحور الأوّل : الشّعر الجاهلي — غرض الرثاء (`04-gharad-ritha`, tome 1, p.53–59, transcrit à profondeur de génération)

Chapitre du **غرض الرثاء** : les deux مرثيّات que le manuel place entre la ورقة du مدح et la ورقة du رثاء —
« حامِي العرين » de الخنساء (p.53, **الرّثاء : التفجع والتأبين** selon le فهرس p.6) et « تَلَفٌ مُقيمٌ » de
أبو ذؤيب الهذلي (p.56, **الرّثاء : التفجع والتّأمّل**) — puis la **ورقة منهجيّة** « كيف أقـرأ : غـرض الرّثاء »
(p.59).

- **Montage (fidèle au manuel)** :

  - **النصوص المختارة du chapitre** (p.53–58) :

    **Texte 10 — « حامِي العرين »** · auteur **الخنساء** · mètre **(من البسيط)** · **13 vers** · référence : « الخنساء / الديوان ص،ص 58 — 59 / ط —1— دار صادر، بيروت، لبنان، 1996 » · **p.53–55**. Premier texte de رثاء du محور.
    - **Incipit verbatim** : « يا عينُ فيضي بِدَمْعٍ منـك مِغـزَارِ — وابْكي لِصخر بِدَمْعٍ منك مِدْرَارِ » ; dernier vers : « حامي العرينِ لدى الهَيْجَاءِ مُضْطَلِعٌ — يَفْـرِي الرّجَـال بأنياب وأظفـارِ »
    - `تمهيد` (verbatim intégral) : « "وسبيل الرثاء أن يكون ظاهر التّفجّع، بَيِّن الحسرة، مخلوطا بالتلهُّف والأسف والاستعظام..." — ابن رشيق: العمدة، ج 2. ص، 805 »
    - `اعرف` — **7 entrées de الشـرح** (العوّار، الأطمار، ينمي، الأوتار، الخوّار، المريرة، جؤنة القار) ; **الأعلام** : الخنساء (« تماضر بنت عمرو بن الشريد السلميَّة، شاعرة مخضرمة … توفيت على أشهر الروايات سنة 26هـ ، في خلافة عثمان »).
    - `فكّك` : « * تبيّنْ أقسام هذه المرثيّة معتمدا الموضوع معيارا. »
    - `حلّل` : 1. « استخرج من القصيدة خصال المرثيّ وبيّن مدى وفائها لنموذج الفتى الجاهليّ. » 2. « حدّد ملامح الراثية النفسية مستخلصا أبعاد الرثاء العاطفية والقيميّة ؟ » 3. « تعدّدت الضمائر في هذه القصيدة ، فما المعاني التي اكتسبتها المرثية بشيوعـها؟ وما تعليل ذلك ؟ »
    - `قوّم` : « * يذهب بعض النقاد إلى أنّ المعاني الفخرية وثيقة الصلة.بمعاني التأبين فهل تشاطره الرأي؟ علّل إجابتك. »
    - `توسّع` : « * تبيّن أهمّ الصّيغ الصّرفيّة المعتمدة في رسم صورة المرثيّ. » ; « * قطّع البيت تقطيعا عروضياً: يا عينُ فيضي بدمعٍ منك مِغـزارِ وابْكي لِصخر بدمعٍ منك مدرارِ. » ; « * الحقل الدلاليّ:ابحث عن معاني لفظ "عين" . »
    - `إضاءات` : (a) « "لا يبعدنْك اللَّهُ" إنشاء طلبيّ أفاد الدعاء، ويصحّ في تركيبه اعتماد المضارع أو الماضي. » ; (b) figure nommée **استعارة مكنيّة** (« غيّبت المشبّه به وأشـارت إليه ببعض لوازمه … لأنّ المتكلمة كنّت عن الأسد بفعلـه (يفري) وبعـض جـوارحــه (أنياب وأظفار) ») ; (c) fait de langue : « قد » (حرف التحقيق) + « كان » (الناسخ الفعليّ) — « فدلّ ذلك على تأكيد انقضاء كينونة الحدث في الزمن الماضي ».
    - `شذرات` : **ريجيس بلاشير / تاريخ الأدب العربيّ، ترجمة إبراهيم الكيلاني، / الدار التونسية للنشر،تونس، 1968 ج I ،ص458.** — le شعر مأتميّ, le rôle premier de la sœur du héros mort « كما تدلّ على ذلك المراثي الموضوعة باسم الخنساء ».

    **Texte 11 — « تَلَفٌ مُقيمٌ »** · auteur **أبو ذؤيب الهذلي** · mètre **(من الكامل)** · **14 vers** · référence : « أبو ذؤيب الهذلي، ديوان الهُذَليّين، ط.2 مطبعة دار الكتب المصرية 1992، ج I ص ص 1 – 3 » · **p.56–58**.
    - **Incipit verbatim** : « أَمِن المَنُـونِ ورَيْبِـهـا تَتَوجَّـعُ / والدهـرُ لَيْـسَ بِمُعْتب1 مَن يَجْـزَعُ »
    - `تمهيد` (verbatim intégral) : « قد يتعاظم الإحساس بالفقدان لدى الراثي فيكون الرثاء شاجي الأقاويل مُبْكي المعاني مثيرا للتَّبَاريح (( تسليةً لمن عضّته النوائب بأنيابها ، وفرّقت الأحداث بين نفسه وأحبابها، وتأسيةً لمن هوى إلى هذا المَصرع، ونهل من هذا المشرع)) » — référence : « *النويري، نهاية الأرب ج 5. ص 164 » (⚠️ « نهاية الأرب » [sic]).
    - `اعرف` — **12 entrées de الشـرح** (معتب، أقضّ، أودى، هويّ، أعنقوا، غبرت، تميمة، سملت، أتضعضع، مروة، المشرّق، مقنعا) ; **الأعلام** : أبو ذؤيب الهذلي (« شاعر مخضرم من بني هذيل … مات في عهد عثمان بإفريقية سنة 27 هـ »)، أميمة (« ذهب صاحب "العقد الفريد" إلى أنها أمامة، وهي زوج الشاعر »).
    - `فكّك` : « * استهلت القصيدة بحوار، وأعقب ذلك تفصيل للأحوال، ثم التفت الشاعر إلى المخاطب في سياق استدلاليّ حجاجيّ. قطّع المرثية متتبعا تحوّلات الخطاب. »
    - `حلّل` : 1. « استخلص من المرثية آثار الإحساس بالفقدان المادية والنفسية. » 2. « تنازعت الشاعر حالتان أولاهما تدعوه إلى التعبير عن الحسـرة والتلهّـف، وثانيتهما تحمـله على المغالبة والتصبّر، فكيف تجلّتا؟ وما دواعيهما؟ » 3. « حلّل صورة الموت في البيتين الثامن والتاسع. » 4. « تبين المواضع التي راوح فيها الشاعر بين الإخبار بالأوضاع الفردية والإلحاح على المصيـر الأوحد لكلّ كائن مستخلصا الأساليب الموظفة لإدراك هذه الغاية. »
    - `قوّم` : « * هل ترى أن الحديث عن الدهر أكسب هذه المرثية نفسا حِكَميًّا؟ كيف ذلك؟ »
    - `توسّع` : « جِدْ في محفوظك حديثا عن الدهر في آية أو بيت من الشعر أو مثل سائر. » ; « تبيّن صلة هذه المرثية بسابقتها. »
    - `إضاءات` : (a) fait de langue **« إخال »** — « من "خَالَ" وهو فعل من أفعال الظن يدخل على الجملة الاسمية فيعمل في المبتدإ والخبر بالنصب وتصير الجملة فعلية، ويسند إلى ضمير المتكلم في المضارع باعتماد الكسر والإمالة على أشهر الروايات فتقول "إخال" وإن كان القياس "أخال". » ; (b) procédé nommé **الالتفات** [le manuel imprime « الالتفاتا », sic] — « وهو انصراف المتكلم عن المخاطبة إلى الإخبار وعن الإخبار إلى المخاطبة وما يشبه ذلك ، ومن الالتفات الانصراف من معنى يكون فيه إلى معنى آخر ».
    - `شذرات` : le خبر de **متمم بن نويرة** pleurant devant chaque tombe, avec 3 vers cités dont « فَقُلْتُ لَهُ: إنَّ الشَّجَا يَبْعَثُ الشَّجَا / فدَعْنِي، فَهَذَا كلُّـهُ قَبْـرُ مَالِـكِ » et le commentaire « وهذا أبلغ ما قيل في تعظيم الميت » — référence : « أبو هلال العسكري — ديوان المعاني، ص 523. »

  - **ورقة منهجيّة** (p.59) — fiche sur parchemin déroulé, étiquette en coin « ورقة منهجيّة », titre « كيف أقـرأ », sous-titre magenta. Transcription verbatim intégrale.

    ### p.59 — « كيف أقـرأ : غـرض الرّثاء »

    > **\* حدّ غرض الرثاء**
    >
    > الرثاء هو التفجّع على الميّت وتأبينه ، وسبيله "أن يكون بيّن الحسرة مخلوطا بالتلهّف والأسف والاستعظام إذا كان الميّت ملكا أو رئيسا كبيرا"، وأن يستفتح بالدلالة على القصد، ولا يصدّر بنسيب لأنّه مناقض لغرض الرّثاء، لذا وجب أن يكون شاجي الأقاويل ،مثيرا للتباريح. وللرّاثي أن يجعل في ثنايا التفجّع والتمجيد حديثا عن الدهر أو حكمة جامعا بذلك بين الاختبار والاعتبار، ملحّا على جلال الرزيّة وهول المصاب.
    >
    > **\* مراكز الاهتمام في غرض الرثاء** — tableau à 2 colonnes (« أهمّ معاني الرّثاء » | « أهمّ الصفات والصور »), lignes regroupées par deux accolades verticales.

    ⚠️ **ILLISIBLE p.59** — les deux étiquettes verticales de groupe (colonne d'extrême droite) sont en très petit corps, à la verticale ; lecture probable mais NON certaine : groupe 1 (lignes 1–3) ≈ `التفجّع`, groupe 2 (lignes 4–7) ≈ `التأبين`. À confirmer sur l'original.

    | أهمّ معاني الرّثاء | أهمّ الصفات والصور                                                                                                     |
    | ------------------ | ---------------------------------------------------------------------------------------------------------------------- |
    | البكاء والإعوال    | – صورة الدموع ومجلس النّوائح.                                                                                          |
    | الحزن والحسرة      | – وصف التلهّف والانقطاع عن الدنيا وما يعرو الرّاثي من ذهول ودهش.                                                       |
    | شكوى الدّهر        | – ضرب المثل في ذلك بالأسـود الخادرة فـي الغياض والعقبان والوعول الممتنعة في قلل الجبال وحمر الوحش المتصرّفة في القفار. |
    | النسب وطيب المحتد  | – تمجيد الأعراق واستعارة صورتي البيت والشجرة كناية عن الأرومة. – بيان وسامة المرثيّ لعلّة الشرف وكرم الأصل.            |
    | البطش والبأس       | – تصوير تعطّل الغزو بعد هلاك المرثيّ وجراءة الأعداء على أهله وقبيلته. – استذكار الأمجاد والبطولات.                     |
    | النجدة             | – إجابة الصّريخ وإغاثة الملهوف.                                                                                        |
    | الجود والسّخاء     | – وصف نواله وعطاياه للميسورين والشعراء والمعوزين.                                                                      |
    | الحكمة             | – صورة الموت / – تمنّي الديمومة من خلال استعارات الصخر والحجر. / – تحذير المخاطب وتنبيهه إلى حتميّة المصير.            |
    | الدّعاء            | – صورة انسكاب مياه الهطل على قبر المرثيّ، وقد استبدل هذا المعنى بالدعاء بالرحمة وصور الجنان بظهور الإسلام.             |

    > **\* وظائف غرض الرّثاء** — 4 encadrés (ordre de lecture droite → gauche) :
    >
    > 1. `الوظيفة التوثيقيّة` : « تخليد صورة المرثيّ في الذّاكرة الجماعيّة »
    > 2. `الوظيفة الاعتباريّة السياسية` : « بيان فداحة المصاب وكون الرّزيّة جماعيّة + بيان حالة الخواء التي خلّفها الموت. »
    > 3. `الوظيفة القيميّة النفسيّة` : « وفاء الرّاثي للمرثيّ + تصوير حالة العجز والقصور أمام الدّهر »
    > 4. `الوظيفة التأثيريّة` : « حثّ أفراد القبيلة على اتخاذ الفقيد رمزا »

- **Concepts, vocabulaire officiel, exemples types et bornes de scope** : voir les **blocs transversaux**
  du chapitre **C1**, relevés sur l'ensemble du محور الأوّل — ils valent aussi pour ce chapitre.

## C5 Chapitre 5 — المحور الأوّل : الشّعر الجاهلي — غرض الغزل (`05-gharad-ghazal`, tome 1, p.60–75, transcrit à profondeur de génération)

Chapitre du **غرض الغزل** : les deux textes que le manuel place entre la ورقة du رثاء et la ورقة du غزل —
« بَدَا لِي وَجهُ نُعْمٍ » de النابغة الذبياني (p.60, **النّسيب : مكوّناته ومعانيه** selon le فهرس p.6) et
« يَا طَائِرَ البَانِ » de عنترة (p.63, **الغزل : أحوال المحبّ**) — puis la **ورقة منهجيّة** « كيف أقـرأ :
غـرض الغزل » (p.65), et enfin la **queue des نصوص مختارة** (p.66–75).

⚠️ **Les trois derniers نصوص مختارة relèvent d'aucune ورقة منهجيّة** — c'est un fait du manuel, pas un choix :
« تَدَاوَيْتُ مِنهَا بهَا » de الأعشى (p.66, **صفة الخمرة وصورة مجالس الشراب**), « مِنْ حِكَمِ الجَاهِلِيِّينَ » de
زهير (p.69, **الحكمة : منظومة القيم عند الجاهليّين**) et « الخَيْرُ بِنَوَاصِي الخَيْلِ مَعْصُوبُ » de امرؤ القيس
(p.73, **صفة الخيل وصلتها بعالم الصحراء**, avec la planche Franz Marc p.72). Le manuel les range **après** la
dernière ورقة, en queue de la section « نصوص مختارة », sans en ouvrir de nouvelle : ils sont donc rattachés à
ce chapitre-ci, **là où le manuel les range**, et non redistribués au jugé. À signaler au LOT B : ils ne sont
pas du غزل — ce sont les trois **satellites** du محور (خمريّة, حكمة, وصف الخيل).

- **Montage (fidèle au manuel)** :

  - **النصوص المختارة du chapitre** (p.60–64) :

    **Texte 12 — « بَدَا لِي وَجهُ نُعْمٍ »** · auteur **النابغة الذبياني** · mètre **(من البسيط)** · **13 vers** · référence : « النابغة الذبياني — الديوان، ط 1 الدار التونسية للنشر 1968. ص–ص 146–148. » · **p.60–62**.
    - **Incipit verbatim** : « وقَدْ أرَاني ونعمًا لاهِيَيْن مَعًـا / والدَّهرُ والعَيْـش لم يهْمُمْ بإمْـرَارِ1 »
    - `تمهيد` — citation d'**ابن رشيق** : « وللشعراء مذاهب في افتتاح القصائد بالنسيب لما فيه من عطف القلوب واستدعاء القبول بحسب ما في الطّباع من حبّ الغزل والميـل إلى اللّهو والنّساء، وإنما ذلك استدراج لما بعده » ; le مطلع est cité : « عُوجُوا فَحَيُّوا لِنُعْمٍ دِمْنَةَ الدَّار / مَاذَا تُحَيُّونَ من نُؤْيٍ وأَحْجَارْ » — référence imprimée « ابن رشيق،العمدة ج 397، . » (⚠️ inversion tome/page [sic]).
    - `اعرف` — **9 entrées de الشـرح** (إمرار، حاجي، الزاري، أكوار، أسعدها، افتضال، دعص، مشمولة، مشتار) ; **الأعلام** : النابغة الذبياني (« زياد بن معاوية بن سعد بن ذبيان … وكان مُحكّمًا في عكاظ تأتيه الشعراء فتعرض عليه أشعارها … توفّي على أشهر الروايات سنة 604م »)، نُعْمٌ (« ترخيم لاسم العلم نُعْمَى وهي حبيبة الشاعر »)، حارِ (« ترخيم لاسم الحارث ، وهو خليل الشاعر »).
    - `فكّك` : « اتّخذ مواضيع الوصف معيارا لتقطيع النصّ. »
    - `حلّل` : 1. « تبيّن خصائص الحبيبة الخَلقيّة والخُلُقيّة. » 2. « قامت علاقة الشاعر بنعمى على اتصال مفقود وانفصال موجود،فما أثر ذلك في نفسيّته؟ » 3. « استعار الشاعر لحبيبته صورا متعدّدة، استخرجها محدّدا دورها ووظائفها. » 4. « للقرائن الزمنيّة دور في تقلّب أحوال الشاعر، فكيف ذلك ؟ »
    - `قوّم` : « * يرى ابن قتيبة أن النّسيب إنما هو عدّة الشاعر "ليميل نحوه القلوب، ويصرف إليه الوجوه، ويستدعي به إصغاء الأسماع إليه"، فإلى أيّ مدى أفلح النّابغة في ذلك؟ علّل إجابتك. »
    - `توسّع` : « – الحقل المعجميّ:استخرج من النصّ ما اتَّصَلَ.بمجال "الطبيعة". » ; « – وظّف الشاعر مجموعة من الحواسّ لوصف نعمى، ضَعْ مكونات الوصف حسب مجال الحاسّة: » — tableau à 4 cases (droite → gauche) :

      | حاسّة النظر | حاسّة الشم | حاسّة الشم | حاسّة السمع |
      | ----------- | ---------- | ---------- | ----------- |
      |             |            |            |             |

      ⚠️ « حاسّة الشم » est imprimée **deux fois** (2ᵉ et 3ᵉ cases) — [sic].

    - `إضاءات` : (a) fait de langue **المفعول المطلق** sur « سقيًا ورعيًا » (« والتقدير "سُقِيت سَقْيًا ورعيْتِ رعْيًا" ») ; (b) procédé nommé **مجاورة لفظيّة** (la reprise de « الأقدار » au vers 6, « دون أن يكون ذلك لغوا لا يحتاج إليه في المعنى »).
    - `شذرات` : définition du النسيب par **قدامة بن جعفر** — « هو ما كثرت فيه الأدلّة على التهالك في الصبابة، وتظاهرت فيه الشواهد على إفراط الوجد واللوعة، وما كان فيه من التصابي والرقّة أكثر مما يكون فيه من الخشن والجلادة… فإذا كان النسيب كذلك فهو المُصاب به الغرض. » — référence : « قدامة بن جعفر ، نقد الشعر. ص 139.. »

    **Texte 13 — « يَا طَائِرَ البَانِ »** · auteur **عنترة** · mètre **(من البسيط)** · **8 vers** · référence : « عنترة، الديوان — دار مكتبة الهلال – لبنان،ط.1، 1988 ص–ص،120–121 » · **p.63–64**.
    - **Incipit verbatim** : « يا طائرَ البَانِ1 قدْ هيَّجتَ أحْزَانِي / وزدتَنِي طرَبًا2 يا طائِـرَ البَانِ »
    - `تمهيد` (verbatim intégral) : « درجت كتب تاريخ الأدب على تقديم عنترة من خلال معلقته، فصورته نموذجا للفتى السيّد والبطل المقاتل، أما كتب السير فاتخذت مادة من حياته جعلت سداها مواقفه الغرامية وشدّة تعلقه بابنة عمه عبلة، وإن لم يهلك عزيزا في ساحـة الوغى فقد أماته البين عشقا كما هو الحال في هذه القطعة، لذلك دُعي فارس الحروب والقلوب. »
    - `اعرف` — **4 entrées de الشـرح** (البان، طربا، ناشدتك، انعاني — cette dernière glosée « جواز شعري من باب الضرورة لاستقامة الوزن، وصوابه انعني، والنعي خبر الموت ») ; **الأماكن** : أرض الحجاز (« هي البلاد الواقعة بن الشام ونجد وتهامة » ⚠️ « بن » pour « بين » [sic])، عالج ونعمان. Pas de rubrique الأعلام.
    - `فكّك` : « * اتخذ الشاعر من الطائر مثيرا للأحزان في بداية الغزليّة ثم انتدبه بعد ذلك سفيرا يبثُّ الحبيبة أشواقه. اعتمد نظام الانتقال من وظيفة الإثارة إلى وظيفة السِّفارة في تبيّن مقاطع النصّ. »
    - `حلّل` : 1. « استخلص من النص الملامح العاطفيّة لكلٍّ من الشاعر والطائر. » 2. « ما المعاني الغزلية التي ألحّ عليها الشاعر؟ » 3. « يشكل الحـب والمـوت طرفي المعادلة فـي هذه الغزلية، أيُعزَى ذلك إلى الوفاء أم إلى خيبة الرجاء؟ علّل إجابتك. » 4. « في القصيدة أساليب إنشائية ، استخرجها وحدد دورها في إكساب النص بعدا ترسّليا شفويا. »
    - `قوّم` : « وازن بين هذه الغزلية ومقطع النسيب في قصيدة النّابغة، إلام تخلص؟ »
    - `توسّع` : « – الحقل المعجمي:استخرج من النص الألفاظ المتصلة.بمجال ((الشَّجَنِ)). » ; « – اعقد مُقَارَنَةً بين فحريّة عنترة وغزليّتهِ مستخْلِصًا مَا يَلِي : » (⚠️ « فحريّة » pour « فخريّة » [sic]) — « أ – عنترة الفارس (الأعمال والأحوال) » / « ب – عنترة العاشق (الأعمال والأحوال) ».
    - `إضاءات` : (a) procédé nommé **ردّ الأعجاز على الصدور** (le تركيب ندائيّ « يا طائر البان » ouvre le صدر et clôt le عجز) ; (b) **جناس جزئي** fondé sur le son ن au vers 3 — « وقد وظف الشاعر هذا الصوت لتكثيف معاني الحزن وتعبئة طاقات النصّ الإبلاغية ».
    - `شذرات` : **توفيق بكار. "شعريات عربية" — دار الجنوب للنشر، تونس،ص33** — « عنترة … في هذا القصيد رجلان في واحد: العاشق والشاعر، أي الإنسان والفنَّان ».

  - **ورقة منهجيّة** (p.65) — fiche sur parchemin déroulé, étiquette en coin « ورقة منهجيّة », titre « كيف أقـرأ », sous-titre magenta. Transcription verbatim intégrale.

    ### p.65 — « كيف أقـرأ : غـرض الغزل »

    > **\* حدّ غرض الغزل**
    >
    > الغزل من قولهم غزل الرّجل يغْزُلُ غزْلاً، وتغزّل فلان بفلانة وغازلها أي أحسن الحديث إليها واستمالها. ومن النقّاد من رأى أنّ هذا الغرض لم يستقلّ إلاّ في منتصف القرن الأوّل للهجرة. وسبيله أن يعمد المتغزّل إلى بيان صفات حبيبته فيفصّلها ويجعل من تعلّقه بها سببا لأشواقه ووجده طلبا للوصال وإمعانا في بيان التذلّل والحاجة إليها ، وقد قرن أغلب شعراء الغزل من العذريّين خاصّة بين معنيي الحبّ والموت في إطار معادلة عاطفيّة، غير أنّ هذا الفعل عند شعراء القرن الثاني أصبح دالاًّ على سنّة شعرية وقلّما عبّر عن عاطفة متقرّحة.
    >
    > **× مراكز الاهتمام في غرض الغزل** — deux tableaux jumelés : `الغزل البدوي` (droite) et `الغزل الحضريّ` (gauche), chacun à colonnes « أهمّ المعاني الغزليّة » | « أهمّ الصفات والصّور », lignes regroupées par accolades verticales.

    ⚠️ **ILLISIBLE p.65** — étiquettes verticales des groupes (petit corps, à la verticale). Lecture probable : dans les deux tableaux, groupe 1 ≈ `ما اتّصل بالحبيبة` (côté حضريّ : `ما اتّصل بالمرأة الحبيبة أو القينة`) et groupe 2 ≈ `ما اتّصل بالفتى العاشق`. À confirmer sur l'original.

    **الغزل البدوي**

    | أهمّ المعاني الغزليّة | أهمّ الصفات والصّور                                                                                                |
    | --------------------- | ------------------------------------------------------------------------------------------------------------------ |
    | الجمال                | – تشبيه المرأة بالظبي والشادن والمها وغيرها. / – وصف القوام والوجه والعينين والثغر. / – نفي وجود النظائر والأشباه. |
    | النّسب وطيب المحتد    | – تمجيد الأعراق.                                                                                                   |
    | المنزلة الاجتماعيّة   | – ذكر الشرف والسؤدد والمنعة.                                                                                       |
    | الصفات الأخلاقيّة     | – نفي الفحش ووصف الشمائل. / – الدّلال والإخلاف والصدّ والامتناع.                                                   |
    | اللّوعة والشوق        | – وصف الشاعر ما يجد من عناء البعد وحرقة الفراق.                                                                    |
    | التهالك والصبابة      | – بيان تتالي الأسقام النفسيّة والجسديّة.                                                                           |
    | الوفاء وحفظ العهد     | – مقابلة الصدّ والهجر بالإقبال والوفاء والتضحية.                                                                   |
    | الذّكرى               | – تبيّن صورة الحبيبة في الخيالات الطائفة والرياح الهابّة والبروق اللامعة والحمائم الهاتفة.                         |

    **الغزل الحضريّ**

    | أهمّ المعاني الغزليّة                     | أهمّ الصفات والصّور                                                                                                          |
    | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
    | الجمال                                    | – إجراء استعارات في الرّياحين والورود وعذب المياه مع شعراء القرنين الأوّل والثاني.                                           |
    | حسن الحديث                                | – القدرة على مخاطبة الندمان وإطرابهم بالأدب والغناء. / – حذق القينة صناعتها وتقليبها أحوال السامعين. / – طلاوة لسان الحبيبة. |
    | المنزلة الاجتماعيّة                       | – ذكر الشرف والسؤدد والمنعة.                                                                                                 |
    | تحميل الحبيبة مسؤوليّة هلاك العـاشق وتلفه | – اعتبار العاشق نفسه ضحيّة ألحاظ الحبيبة والأقدار. / – طلب الديّة والقَوَدِ.                                                 |
    | الإلحاح في طلب الوصل                      | – تعليل الشاعر نفسه بقرب انقلاب المنشود موجودا.                                                                              |
    | تعدّد المغامرات العاطفيّة                 | – يلمح هذا المعنى في شعر عمر وبعض غزليّات بشار. / – اعتبار الغزل ضربا من السلوك الحاذق.                                      |

    > **\* وظائف غرض الغزل** — 4 encadrés (droite → gauche) :
    >
    > 1. `الوظيفة التّأسيسيّة` : « بناء نموذج للجمال النّسائي »
    > 2. `الوظيفة الجماليّة` : « بيان الشّاعر قدرته على ركوب الغرض »
    > 3. `الوظيفة النفسيّة` : « استمالة الحبيبة + بيان شقاء العاشق الدنِف.بما يجد من صبابة ولوعة. »
    > 4. `الوظيفة التأثيريّة` : « جعل السامع المخاطب ظهيرا للشّاعر »

  - **Queue des نصوص مختارة, après la dernière ورقة منهجيّة** (p.66–75) — aucune ورقة ne leur est consacrée :

    **Texte 14 — « تَدَاوَيْتُ مِنهَا بهَا »** · auteur **الأعشى** · mètre **(من المتقارب)** · **13 vers** · référence : « ديوان الأعشـى — دار الجيل، لبنان – ط 1 ـ 1992 ص–ص 37–38 » · **p.66–68**.
    - **Incipit verbatim** : « وكأس شَربْتُ عَلَـى لـذَّةٍ / وأخْـرَى تَدَاوَيْتُ منْهَا بهَا »
    - `تمهيد` (verbatim intégral) : « عالج الأعشى أكثر الفنون الشعرية القديمة حتى جعله النقاد في الطبقة الأولى. ولم يشُذَّ عن غيره عند الركوب إلى الأغراض إذ كان يشبِّبُ ويرحلُ، جريا على السنّة والعرف، لكنه فاق معاصريه بنعت الخمرة ووصف مجالس الشراب وتصوير مباهج الحياة التي كان منقطعا إليها. »
    - `اعرف` — **8 entrées de الشـرح** (كميت، قُصّابها، مزهر، أزرى، الصنج، الخندريس، تناخي، الحبرات) ; **الأعلام** : « يزيد وعبد المسيح وقيس: من سادات نجران وكانوا نصارى. » ; **الأماكن** : أثافت، كعبة نجران.
    - `فكّك` : « * تدرّج النصّ من وصف مجلس اللّهو إلى بيان تعلّق المتكلّم بالرحلة في طلب "الإمتاع والمؤانسة" قطّع النّصّ متّخذا هذا التدرّج معيارا. »
    - `حلّل` : 1. « حدّد مكونات مجلس اللّهو مستخلصًا منها سمات رقيق العيش. » 2. « تكاملت اللذّات في الوحدة الأولى من النصّ، فهل ترى لذلك صلة.بمعنى الحياة عند الجاهليّين؟ » 3. « مثّلت الخمرة وسيلة لاختراق حدود المكان بذلك ميثاقا محدثة أساسه طلب المتع ومنادمة الشَّرْب، فهل لك أن تستخلص منزلة الخمرة ووظائفها عند الأعـشى؟ » (⚠️ phrase imprimée telle quelle, ordre des mots surprenant [sic]) 4. « تجلّت في النص بعض معاني الفخر والمدح، استخلصها وبين دورها في رسم ملامح الندامى. »
    - `قوّم` : « * وازن بين صفة الخمرة عند الأعشى ونعتها عند طرفة. »
    - `توسّع` : « – ابحث في كتب التاريخ عن الأنشطة الثقافيّة والتجاريّة التي كان مركزها نجران بأرض اليمن. » ; « – رتّب في جدول تجعل أقسامه على عدد الحواسّ الخمس مثيرات المتع مستأنسا.بما جاء في القصيدة. » — tableau à 5 cases (droite → gauche) :

      | متعة النّظر | متعة الشمّ | متعة الذّوق | متعة السّمع | متعة اللّمس |
      | ----------- | ---------- | ----------- | ----------- | ----------- |
      |             |            |             |             |             |

    - `إضاءات` : (a) fait de langue **واو ربّ** — « وقد أدخل المتكلم على الاسم النكرة واو ربّ، وهو حرف جرّ أفاد التكثير ، ولا يدخلُ إلا على منكَّر ولا يتعلق إلا.بمتأخرٍ. » ; (b) procédé nommé **مؤاخاة معنوية** (l'inversion de l'ordre réel : « جعل الشاعر العصر تاليا للقطف »).
    - `شذرات` : **حسين الواد، "جماليّة الأنا في شعر الأعشى الكبير" — المغرب، المركز الثقافي العربي – 2001.ص 85** — la خمرة comme « باب المعيشة », le système « محوره الأنا والخمرة ».

    **Texte 15 — « مِنْ حِكَمِ الجَاهِلِيِّينَ »** · auteur **زهير بن أبي سلمى** (extrait de sa معلّقة) · mètre **(من الطويل)** · **14 vers** · référence : « من معلقة زهير بن أبي سلمى — شرح المعلقات السبع لأبي عبد الله الحسين الزوزني، دار الكتب العلمية، لبنان، –د.ت – ص ص 69 – 72 » · **p.69–71**.
    - **Incipit verbatim** : « سَئمْتُ تَكَاليفَ الحَيَاةِ ومَنْ يَعِـشْ / ثمَانِينَ حوْلاً– لاَ أَبَا لَكَ– يـسْأَمِ »
    - `تمهيد` (verbatim intégral) : « لم يخل الأدب الجاهلي من أبعاد تأمّليّة، إذ قد يعنُّ للشاعر أن يستصفيَ من التَّجارب التي عاشها طائفة من القواعد والرُّؤَى، فيحكّك اللفظ ويصوّب المعنى حتى تنقاد العبارة فتحيط بالعبرة لتؤول أمثالا سائرة وحِكَمًا يعود إليها الناس ويرتضونها ناموس حياة.وهذا ما فعله زهير في معلّقته التي اصطفينا منها الأبيات الموالية ومطلعها: أَمِنْ أُمِّ أوْفَى دِمْنَةٌ لـمْ تَكَلَّـمِ / بِحَوْمَانَـةِ الـدَّراجِ فالمُتَثَلَّـمِ »
    - `اعرف` — **10 entrées de الشـرح** (خبط، عشواء، يصانع، منسم، يفره، لمنايا [sic, l'entrée du vers est « المنايا »]، الزِّجاج، لهذم، خليقة، سفاه). Pas de rubrique أعلام / أماكن.
    - `فكّك` : « – بنيت القصيدة على كيفيّة تحصيل الإيلاف داخل الإطار القبليّ وأشكال درء النزاع والخلاف خارجه ثم بيان مفهوم الفتوّة الحقّ. قطّع القصيدة مستأنسا بهذه التفريعات. »
    - `حلّل` : 1. « كيف تكشف الحكم التي تضمّنها النص عن نظام القيم وأنماط العلاقات بين الجاهليين؟ » 2. « صَنِّفْ هذه الحِكَم حسب المجالات( السلّم والحرب) ثم حسب الحقول (الطبائع، السلوك، الصفات، المواقف) » 3. « من أهداف النص الاحتجاج لبعض القواعد في سياسة الذات وسياسة الآخر،فما معالم هذه السياسة وما جدواها ؟ » 4. « شاعت في النص تراكيب تلازمية، تبينها واذكر مدى مناسبتها لمعنى الحكمة. »
    - `قوّم` : « سعى الشاعر إلى الخروج من رِبقِ التَّجارب الفرديّة الخاصّة إلى أفق المعايير العامّة، فهل تراه أفلح في ذلك؟ »
    - `توسّع` : « – قطّع البيت التالي تقطيعا عروضيا مستخرجا ما طرأ عليه من تغييرات. » (vers 1) ; « – استأنس بقصيدة زهير بن أبي سلمى لاستخلاص الأوامر والنواهي التي جاء بها، ثمّ بيّن مدى ملاءمتها لمفهوم "المنظومة القيميّة" »
    - `إضاءات` : (a) « "لا أبا لك" تركيب اسمي أفاد الدعاء، وورد معترضا بين طرفي تركيب الشرط. » ; (b) « "كائن ترى من صامت لك معجب" اسم مركب من كاف التشبيه وأيٍّ المنونة ولذلك جاز الوقف عليها بالنون. » ; (c) procédé nommé **الإيجاز** — « وقد سكّ الشاعر كلّ هذه المعاني في عبارة تخفّفت من الزّوائد التركيبيّة، لذلك يعدّ هذا الأسلوب إيجازًا، وهو قسم من أقسام علم المعاني. »
    - `شذرات` : **وهب أحمد روميّة — شعرنا القديم والنّقد الجديد، ص160/161.** — زهير « مصلحا وداعية سلام » ; le vers cité « وأعلمُ علمَ اليومِ والأمس قبلَه / ولكنّني عنْ علمِ مَا في غدٍ عمِ » ; l'usage insistant du **الطباق والمقابلة** chez زهير, et la thèse : « سيطر التشبيه على أدب العصر الجاهليّ، وسيطرت الاستعارة على شعر المحدثين في العصر العبّاسيّ، وسيطر البديع وفنونه على أدب العصور المتأخّرة ».
    - **p.72 — planche pleine page** : tableau de chevaux rouges. Légende verbatim : « لوحة للرسّام الألماني فرانز مارك (Franz Marc) 1880 - 1916 ». Bandeau bleu en bas de page portant un vers calligraphié : « والخيرُ مَا طَلَعَتْ شمْسٌ ومَا غَرُبَتْ / مُطلَّقٌ بِنَوَاصِي الْخَيْلِ مَعْصُوبُ » (⚠️ premier mot lu « والخيرُ », à vérifier sur l'original).

    **Texte 16 — « الخَيْرُ بِنَوَاصِي الخَيْلِ مَعْصُوبُ »** · auteur **امرؤ القيس الكِنْدي** · mètre **(من البسيط)** · **15 vers** · référence : « الديوان، دار الكتب العلمية / ص – ص 46–47 » · **p.73–75**.
    - **Incipit verbatim** : « قدْ أَشهدُ الغَارَةَ الشَعْوَاءَ تَحمِلُنـــي — جرداءُ معْرُوقةُ اللّحْيَيْن سرْحُــوب » ; vers 15 : « والخيرُ مَا طَلَعَتْ شمسٌ ومَا غَرُبَتْ — مُطلَّقٌ بنَواصِـي الخيلِ مَعصُوبُ »
    - `تمهيد` (verbatim intégral) : « اتفق أغلب النقاد القدامى على تقديم امرئ القيس على غيره من الشعراء لقدرته على الأخذ بالوجوه وجعل السمع بصرًا لدقّة الوصف ووضوحِ الصّورةِ وإصابةِ التّشبيه ، وإنّما حمل لواء الشّعر لأنّه ز أوّل من وقف بالديار وعَرَصاتها، واغتدى والطير في وُكنَاتِها، ووصف الخيل بصفاتها.» (⚠️ « لأنّه ز أوّل » [sic] ; la citation ne s'ouvre pas).
    - `اعرف` — **17 entrées de الشـرح** (معروقة اللحيين، سرحوب، غرب، زوراء، تجبيب، ضرم، جذم، زيَم، مقبوب، ضارحة، مَلْحُوب، مضطمر، غربيب، صقعاء، شناخيب، الدَفُّ، مُطلَّقٌ) — la glose de غربيب cite le Coran ﴿وَمِنَ الجِبَالِ جُدَدٌ بِيضٌ وَحُمْرٌ مُخْتَلِفٌ ألوانُها وغرَابِيبُ سُودٌ﴾ « سورة فاطر، الآية 27 » ; celle de مُطلَّقٌ signale des variantes de رواية : « وفي رواية النحّاس "مُطلّبٌ"، وفي نسخة الطوسي "معْقوده" » ; celle de صقعاء : « وفي رواية النحاس سفعاء وهي العقاب » ; ⚠️ glose de غرب : « الغرب بفتح الميم وتسكين الرّاء » [sic — le mot n'a pas de ميم]. **الأعلام** : امرؤ القيس الكِنْدي (« حندج بن حجر بن الحارث … ولقبه الملك الضلِيل وذو القروح … وتذهب طائفة من الدارسين إلى أنّه أوّل من ابتدع الوقفة الطللِيّة وشبّب ورحل في شعره . توفّي على أشهر الروايات سنة 565م »).
    - `فكّك` : « تدرّج الوصف من اللوحة إلى المشهد. قطّع القصيدة معتمدا هذا التمشي معيارا. »
    - `حلّل` : 1. « استخلص أوصاف الفرس مبينا مدى وفائها لصورة المطيّة في الشعر الجاهليّ؟ » 2. « لم يكتف الشاعر بتقديم صورة لفرسه بل عقب على ذلك بمشهد صيد، فما الغاية من ذلك؟ علّل إجابتك. » 3. « قام الوصف على التداعي والانتقال من عالم البهائم الأليفة إلى عالم السباع الضارية، فهل ترى في ذلك بعدا رمزيّا؟ كيف ذلك؟ » 4. « ما وظائف الصفات الدالة على الأحوال والأفعال المتصلة بالأعمال؟ » 5. « استخرج من القصيدة الظواهر الإيقاعيّة متبيّنا دورها في جعل الصورة نامية. »
    - `قوّم` : « أوجد الشاعر بين حركة راحلته في المكان ومصارعة الذئب عوامل الافناء صلةً، فإلى أيّ مدى يصحّ القول إنّ الرحلة والصّراع عاملاَ بقاء عند الجاهليّ ؟ » (⚠️ « الافناء », « عاملاَ » [sic]).
    - `توسّع` : « * ابحث في ديوان امرىء القيس عن أوصاف للحيوان وحشيّه وأليفِهِ. » ; « –عيّن صنف التشبيه في البيت التالي : كأنَّهَا حين فاضَ المَاءُ واحْتَفَلَتْ — صَقْعَاءُ لاحَ لَهَا بالقَفْرَةِ الذِّيــبُ »
    - `إضاءات` : (a) citation du **الثّعالبيّ**, « فقه اللغة », donnant « ضروبا من عدو الفرس منها التَّقريبُ والخبب والإحضار والخِنَاف والارتِجَال والعَنَق والهمْلَجة » ; (b) figure nommée **كناية عن موصوف** (« غيّب امرؤ القيس اسم الموصوف وأشار إليه بلازمة من لوازمه … «جرداء معروقة اللحيين» ») ; (c) un **tableau de تقطيع** portant sur le vers 4 (4 colonnes : segment / schéma / تفعيلة / grammaire) :

      | segment (de droite à gauche) | schéma      | تفعيلة       | grammaire |
      | ---------------------------- | ----------- | ------------ | --------- |
      | خِنَافُها ضرمٌ               | – 0 – 0 0 – | متفعلن فعلن  | مبتدأ خبر |
      | وجرْيُها جَذِمٌ              | – 0 – 0 0 – | متفعلن فعلن  | مبتدأ خبر |
      | ولَحْمُها زِيَمٌ             | – 0 – 0 0 – | متفعلن فعلن  | مبتدأ خبر |
      | والبَطنُ مَقْبُوبُ           | – 0 – – –   | مستفعلن فعلن | مبتدأ خبر |

      ⚠️ **ILLISIBLE partiel p.75** — les schémas métriques (suites de « – » et de « 0 ») sont lus au mieux ; l'ordre exact des symboles n'est pas garanti. Conclusion fléchée sous le tableau, procédé nommé **التسميط** : « وزّع الشاعر أجزاء البيت معتمدا الموازنة وحسن التقسيم، فقد حافظ على النظام النحوي ذاته (مبتدأ،خبر) وعضد ذلك بالتقفية الداخليّة، وجعل الألفاظ على أوزان صرفيّة منتخبة، ويُعدّ ذلك في عرف النقد تسميطًا. »

    - `شذرات` : « قال العلماء بالشعر: إنّ امرأ القيس لم يتقدّم الشعراء لأنه قال ما لم يقولوا، ولكنه سبق إلى أشياء فاستحسنها الشعراء، فاتبعوه فيها؛ لأنه قيل: أول من لطف المعاني، ومن أول من استوقف على الطلــول، ووصف النساء بالظباء والمها والبيض، وشبه الخيل بالعقبان والعصيّ، وفرق بين النسيب وما سواه من القصيدة، وقرب مآخذ الكلام، فقيّد الأوابد، وأجاد الاستعارة والتشبيه » — référence : « ابن رشيق. العمدة / ج1،ص.202 ».

- **Concepts, vocabulaire officiel, exemples types et bornes de scope** : voir les **blocs transversaux**
  du chapitre **C1**, relevés sur l'ensemble du محور الأوّل — ils valent aussi pour ce chapitre.

## 4. Chapitrage retenu (→ alimente `manifest/2eme-sec-lettres.json`)

Chapitrage complet du manuel pour la **section Lettres** (**13 chapitres**, deux tomes).
Colonne **transcription** : ✅ = transcrit à profondeur de génération dans la présente fiche ; ⏳ = chapitre
codifié (bornes constatées) mais **non encore transcrit** (cf. §6). Colonne **opt.** : ✔ = `optional: true`
au manifeste (voir la note sous la table).

Le **محور الأوّل est éclaté en cinq chapitres, un par ورقة منهجيّة** (décision du 2026-07-30, cf. le chapeau
de « Chapitres transcrits ») ; les huit autres unités sont décalées d'autant.

| #   | slug                        | notion (unité officielle)                                                              | manuel élève (code · pages)  | transcription | opt. |
| --- | --------------------------- | -------------------------------------------------------------------------------------- | ---------------------------- | ------------- | ---- |
| 1   | `01-gharad-shiri`           | المحور الأوّل : الشّعر الجاهلي — الغرض الشعريّ                                         | `201202` · p.5–34 et p.76–83 | ✅            | —    |
| 2   | `02-gharad-fakhr`           | المحور الأوّل : الشّعر الجاهلي — غرض الفخر                                             | `201202` · p.35–44           | ✅            | —    |
| 3   | `03-gharad-madh`            | المحور الأوّل : الشّعر الجاهلي — غرض المدح                                             | `201202` · p.45–52           | ✅            | —    |
| 4   | `04-gharad-ritha`           | المحور الأوّل : الشّعر الجاهلي — غرض الرثاء                                            | `201202` · p.53–59           | ✅            | —    |
| 5   | `05-gharad-ghazal`          | المحور الأوّل : الشّعر الجاهلي — غرض الغزل                                             | `201202` · p.60–75           | ✅            | —    |
| 6   | `06-tajdid-shir-qarn-thani` | المحور الثاني : التجديد في الشّعر العربيّ في القرن الثاني للهجرة                       | `201202` · p.85–173          | ⏳            | —    |
| 7   | `07-nadira`                 | المحور الثالث : من أشكال القصّ في الأدب العربيّ القديم — النّـادرة                     | `201202` · p.174–222         | ⏳            | —    |
| 8   | `08-tawasul-shafawi-1`      | التواصل الشفويّ (1) : العلاقات بين الشّباب — المرئيّ والمكتوب                          | `201202` · p.223–241         | ⏳            | ✔    |
| 9   | `09-waraqat-lughawiya-1`    | ورقات لغويّة (1) : التعبير عن الزمان في اللغة العربيّة — التركيب التلازميّ             | `201202` · p.242–252         | ⏳            | ✔    |
| 10  | `10-romantiqiya`            | المحور الرابع : الرّومنطيقيّة في الأدب العربيّ                                         | `201203` · p.5–101           | ⏳            | —    |
| 11  | `11-riwaya-khan-al-khalili` | المحور الخامس (المسلك الآداب) : الرّواية — خان الخليلي لنجيب محفوظ                     | `201203` · p.102–173         | ⏳            | —    |
| 12  | `12-tawasul-shafawi-2`      | التواصل الشفويّ (2) : التقدّم العلمي والتّكنولوجي إلى أين؟ — حوار الحضارات             | `201203` · p.238–265         | ⏳            | ✔    |
| 13  | `13-waraqat-lughawiya-2`    | دلالات الصيغ الصرفيّة : الجذر والصيغ والأوزان — صيغ الأفعال المزيدة — دلالات بعض الصيغ | `201203` · p.266–283         | ⏳            | ✔    |

> **Grain du محور الأوّل — bornes constatées, pas un prorata.** Chaque borne se lit dans la fiche : les cinq
> **ورقات منهجيّة** « كيف أقـرأ » tombent en **p.34, 44, 52, 59, 65** et chacune **clôt** la série de textes
> qu'elle synthétise. D'où le découpage : C1 = ouverture + 3 نصوص تمهيديّة + معلّقة طرفة (textes 1–4) + ورقة
> p.34, **et** les 3 نصوص تكميليّة + le ثبت (p.76–83) ; C2 = textes 5–7 + ورقة p.44 ; C3 = textes 8–9 + ورقة
> p.52 ; C4 = textes 10–11 + ورقة p.59 ; C5 = textes 12–13 + ورقة p.65 **et** les textes 14–16 (p.66–75), que
> le manuel range après la dernière ورقة sans en ouvrir de nouvelle.
>
> **⚠️ Pas de chapitre pour الهجاء.** Le manuel retient cinq أغراض (المدح، الفخر، الغزل، الرثاء، **الهجاء**,
> ورقة p.34) mais n'en dote que **quatre** d'une ورقة منهجيّة dans ce محور. Aucun نصّ مختار de الهجاء au
> فهرس p.6 ; sa ورقة « كيف أقـرأ : غرض الهجاء » est **p.150**, donc dans le **محور الثاني**. Il est donc nommé
> en C1 (avec la ورقة qui l'énumère) et traité au fond dans `06-tajdid-shir-qarn-thani` — **jamais** comme un
> 6ᵉ chapitre.
>
> **`optional: true` (décision du 2026-07-30)** sur les quatre chapitres **non littéraires** —
> `08-tawasul-shafawi-1`, `09-waraqat-lughawiya-1`, `12-tawasul-shafawi-2`, `13-waraqat-lughawiya-2`. Ils
> restent **codifiés et traçables** au programme officiel, mais ne comptent plus comme **chapitres manquants**
> dans l'audit de couverture : le QCM est un mauvais véhicule pour du débat oral et des fiches de langue, et la
> matière doit pouvoir être servie sans eux.

> **Bornes CONSTATÉES, pas dérivées.** Les pages de garde de **tous** les محاور ont été lues (tome 1 : p.5, 85,
> 174, 223, 242 ; tome 2 : p.5, 102, 174, 238, 266) ainsi que les pages de clôture (ثبت بيبليوغرافي). C'est
> important : le **فهرس ne donne que la première page de chaque texte**, décalée de 2 à 4 pages par rapport à
> la page de titre du محور (ex. محور 4 : garde p.5, premier texte p.8 ; محور 5 آداب : garde p.102, premier
> texte p.105). Ne pas re-dériver les bornes du فهرس. Seule exception résiduelle : la fin du chapitre 7 (p.173)
> est **déduite** de la garde du محور suivant, vue en p.174.
>
> **⛔ EXCLU du chapitrage** — le **المحور الخامس du المسلك العلوم / تكنولوجيا الإعلاميّة / الاقتصاد والخدمات**
> (« النصّ المسرحي : بجماليون للحكيم », `201203` p.174–237, avec ses 6 ورقات منهجيّة sur le théâtre). Il n'est pas
> au programme de la section Lettres : il alimentera, le jour venu, les fiches
> `2eme-sec-sciences`/`2eme-sec-info`/`2eme-sec-eco-services`, pas celle-ci.

## 5. Sources croisées

- **Manuel élève, tome 1** : `201202` — « عيون الأدب … الجزء الأوّل » (source de scope **et** de contenu :
  textes, appareil pédagogique, ورقات منهجيّة, bibliographies ; pages par chapitre en §4). 256 pages.
- **Manuel élève, tome 2** : `201203` — même ouvrage, الجزء الثّاني. 288 pages.
- **Guide enseignant** : **non disponible au corpus** pour ce couple (aucun code enseignant d'arabe 2ème sec
  au catalogue) ⇒ le manuel élève **fait référence**, comme pour les mathématiques 2ème sec sciences.
  Conséquence assumée : ni « الكفاية المستهدفة » ni « المعايير » ni توزيع سنوي (cf. §1, §2).
- **Taybah / séquençage trimestriel** : rien pour ce couple ⇒ le séquençage reste **inconnu** (à ne pas
  inventer).
- **Divergences signalées** : aucune divergence de scope à ce stade. Le seul écart notable est **interne au
  manuel** : la 6ᵉ unité du tome 2 est annoncée « ورقات لغويّة » au فهرس (p.287) alors que sa page de garde
  (p.266) porte « **دلالات الصيغ الصرفيّة** » et un découpage en trois volets (`الجذر والصيغ والأوزان`,
  `صيغ الأفعال المزيدة`, `دلالات بعض الصيغ`, ce dernier numéroté `3-1 … 3-6`) qui ne recoupe pas exactement les
  trois entrées du فهرس. Le chapitrage retient le libellé de la **page de garde** (plus précis) en citant les
  deux. À trancher définitivement quand ce chapitre sera transcrit.

## 6. Incertitudes / à revérifier

- **Profondeur atteinte (arrêt propre, budget de session)** : **المحور الأوّل intégral** (tome 1, p.5–83 :
  3 textes تمهيديّة, 16 textes choisis dont les 4 extraits de la معلّقة, 5 ورقات منهجيّة, 3 textes تكميليّة,
  ثبت بيبليوغرافي), à **profondeur de génération**. **Reste à transcrire** : tome 1 p.85–252 (محاور 2 et 3,
  التواصل الشفويّ 1, ورقات لغويّة 1) et tome 2 p.5–101 + p.102–173 + p.238–283 (محور 4, محور 5 آداب,
  التواصل الشفويّ 2, دلالات الصيغ الصرفيّة). Reprise : lire le tome 1 **à partir de la p.91** et le tome 2
  **à partir de la p.9**, sans refaire le محور الأوّل (R-4).
- **Pages lues, par source (plages réelles)** :
  - `201202` (256 p.) : **p.1–90** (liminaires + مقدّمة + محور 1 intégral + page de titre/فهرس du محور 2 +
    garde نصوص تمهيديّة + premier texte du محور 2), **p.169–176**, **p.221–225**, **p.240–244**, **p.248–256**
    (les lots hors محور 1 sont des **sondages de bornes** : gardes de محور, ثبت بيبليوغرافي, فهارس de fin —
    ils fixent le chapitrage, ils **ne** valent **pas** transcription).
  - `201203` (288 p.) : **p.1–8**, **p.99–106**, **p.174–180**, **p.234–240**, **p.264–268**, **p.279–288**
    (uniquement des **sondages de bornes** + les فهارس de fin ; **aucun** texte du tome 2 n'est transcrit).
- **Pagination** : les numéros cités sont les **pages imprimées**, qui coïncident avec les **pages physiques
  du PDF** (offset nul vérifié sur les deux tomes : couverture = page 1, مقدّمة = page 3, فهرس النّصوص =
  p.253 / p.284). ⚠️ Les **pages de garde de محور ne portent pas de numéro imprimé** : leur numéro est déduit
  de la séquence continue (ex. tome 1 : 222 → [223] → 224).
- **Rendu vision** : PNG à **200–300 dpi** (helper `cnp-officiel/render.sh` ; 150 dpi insuffisant pour la
  vocalisation et les cellules de tableau, 250–300 dpi excellent). ⚠️ **La couche-texte de ces deux PDF est
  inexploitable** : `pdftotext` rend du mojibake (police arabe mappée sur de l'ASCII latin) — contrairement
  aux manuels de maths dont la prose s'extrait proprement. **La vision est ici l'unique voie.**
- **Zones illisibles rencontrées** (signalées, non comblées) :
  - `201202` p.7 et p.8 — les **cartes historiques** (« توزيع القبائل العربيّة قبل ظهور الإسلام »,
    « الأحلاف القبليّة العربيّة قبل ظهور الإسلام », réf. د. حسين مؤنس، أطلس تاريخ الإسلام، الزهراء للإعلام العربي،
    ط 1، 1987) : les noms de tribus et de lieux ainsi que les boîtes de légende sont en très petits caractères
    manuscrits, non déchiffrables même à 250 dpi. Seuls quelques toponymes sont lus (« دولة الروم »،
    « دولة الغسّاسنة »، « منطقة عوالي نجد »). **Ne pas générer de question sur ces cartes.**
  - `201202` p.75 — le **tableau de تقطيع** (schémas métriques en suites de `–` et `0`) : l'ordre exact des
    symboles n'est **pas garanti**. **Ne pas générer de question de scansion à partir de ce tableau.**
    (Aux p.24, p.54 et p.71 le تقطيع est seulement **demandé en consigne**, sans corrigé imprimé : il n'y a
    donc là aucune réponse officielle sur laquelle appuyer une clé.)
  - `201202` p.44, p.59, p.65, p.72 — étiquettes **verticales** de groupes dans les tableaux des ورقات
    منهجيّة, et un vers calligraphié : lues après recadrage/rotation, avec un doute résiduel signalé en place
    (p.59 : `التفجّع` / `التأبين` ; p.65 : `ما اتّصل بالحبيبة` / `ما اتّصل بالفتى العاشق` ; p.72 : premier mot du
    vers lu « والخيرُ ») — lectures **probables**, à confirmer avant d'en faire une clé de QCM.
- **Coquilles du manuel** relevées et conservées `[sic]` (jamais corrigées) : `201202` p.22 et p.35
  (« دار صادر » pour دار صادر/Ṣādir), p.25 (renvoi de note 14 absent du corps), p.29 (décalage d'une unité
  entre renvois et gloses du شرح), p.31/32 (renvoi « 21 » au vers 13 vs glose n° 12), p.33 (« السّعاة »),
  p.47 (شرح n° 2 lemme « ديّك » ; n° 3 « العوّار بضمّ الميم » sur un mot sans ميم), p.62 (« حاسّة الشم »
  imprimée deux fois), p.63 (« بن » pour بين), p.64 (« فحريّة »), p.70 (« لمنايا »), p.73 (« لأنّه ز أوّل »),
  p.74 (« بفتح الميم »), p.75 (« الافناء », « عاملاَ »), p.78 (« إسم »), p.86 (« الشبّاب »).
- **Point de structure à connaître** : le libellé « III – النصوص التكميليّة » **n'est pas imprimé** comme titre
  dans le محور 1 — la garde p.76 ne porte que « نصوص تكميليّة » ; le libellé numéroté apparaît dans les فهارس.
  Ne pas en déduire une différence de statut entre les محاور.
- **TRANCHÉ par Mohamed le 2026-07-30** (les deux points restés en suspens à la transcription) :
  - (a) le **grain du chapitrage** — le محور 1 (79 pages, 16 نصوص مختارة) n'est **plus** un chapitre unique :
    il est éclaté en **cinq chapitres, un par ورقة منهجيّة** (`01-gharad-shiri`, `02-gharad-fakhr`,
    `03-gharad-madh`, `04-gharad-ritha`, `05-gharad-ghazal`), le découpage que le manuel s'impose à lui-même.
    Les 8 autres unités sont décalées (9 → 13 chapitres). ⚠️ **الهجاء n'a PAS de chapitre** : cinq أغراض
    retenus, quatre ورقات seulement, sa ورقة est p.150 (محور 2) — cf. §4.
  - (b) le **statut des 4 chapitres non littéraires** (التواصل الشفويّ ×2, ورقات لغويّة ×2, désormais numérotés
    8, 9, 12, 13) — ils passent **`optional: true`** au manifeste : codifiés et traçables, mais plus comptés
    comme chapitres manquants dans l'audit de couverture.
- **Reste ouvert (signalé, non tranché ici)** : les **textes 14, 15 et 16** (p.66–75 : خمريّة de الأعشى, حكمة de
  زهير, وصف الخيل de امرئ القيس) ne relèvent d'**aucune** ورقة منهجيّة — le manuel les range après la dernière
  ورقة, en queue des « نصوص مختارة ». Ils sont donc rattachés à **C5 (غرض الغزل)**, là où le manuel les place,
  mais ils ne sont **pas** du غزل. Un LOT B qui voudrait leur donner un chapitre propre (« satellites » du
  محور) devra le décider **avant** génération : après, le slug est figé.
