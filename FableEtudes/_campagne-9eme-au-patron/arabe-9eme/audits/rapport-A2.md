# Rapport d'audit A2 — arabe 9ᵉ : chapitres 18, 02, 03, 19

Auditeur indépendant (je n'ai rédigé aucun de ces chapitres ; je n'ai pas lu les rapports des rédacteurs).
Sources : notes L89, L95, L104, L110, L116, L122, `ecart-3.md`, pages du manuel 101908 vues à l'image
quand une note laissait un doute (101908 p.95, 96, 105 ; 101909 p.178) ; fiche
`programme/9eme-base/arabe.md` (§2 ter, §4, §6 — ses « doutes de la réécriture » recoupent plusieurs constats
ci-dessous : quinze particules, R-13 pour 18 et 19, بسيطة / مركّبة par le خبر, « بعد عشر دقائق » = خبر) ;
mandats `b-common.md`, `b-new.md`, briefs B02, B03, N18, N19.

Contrôles initiaux (avant toute correction), depuis le moteur : `content:check` vert (120 matières) ;
`content:qa` : 0 constat sur `arabic/(18|02|03|19)-` ; `content:tranche` sur les 4 chapitres : clé
strictement la plus longue 0/140, positions a 36 · b 33 · c 36 · d 35, 0 paire proche ; Prettier `--check`
vert sur tous les `.json`. Scans maison : 0 chiffre indien, 0 `**` dans prompt/explication, 0 renvoi
positionnel (les 4 « الثّالثة / الثّانية » relevés dans 19 sont des ordinaux de contenu), 0 nombre à
espace simple, 0 LaTeX.

---

## Chapitre 18 — `18-dalalat-az-zaman` (L89 « دلالة صيغ الفعل على الزّمان » + L95 « دلالة الحروف المقترنة بالفعل على الزّمان »)

**Questions re-résolues : 35** (quiz 5 + 5 exercices × 6). Toutes les clés sont justes et uniques. Cours : les
10 `exemple`, 10 `piege` et 10 `verifie` re-dérivés — tous justes.

### Justesse et fidélité
- Définitions = خلاصات L89 §1–4 et L95 §1–4, fidèlement reformulées ; **aucune coquille du manuel reprise**
  (« انقضاؤه » et non « انقاضاؤه », « المتكلّم », « وقوع » ×2, « حرف ينصب », « لن… عدم وقوع الفعل »).
- **Quinze** particules, comptées juste dans le cours, le résumé et `chapter.json` (la note L95 et le brief
  disaient « 14 » ; la liste du manuel en porte bien 15).
- Incohérence interne de la خلاصة p.99 (لم/لن/لمّا rangés sous « المضارع **المرفوع** ») proprement
  contournée : le cours dit « المضارع » pour ces trois et définit le « المضارع المرفوع » comme celui
  qu'aucun حرف نصب/جزم ne précède.
- « لم » + مضارع = « اليقين من عدم وقوع الفعل في الزّمان الماضي » (= خلاصة ; vérifié p.95–96 : le manuel
  ne qualifie jamais « لم يفعل » de منقضٍ). L'explication de `01-pratique` Q4 (« نفيٌ للحدثِ فلا انقضاءَ
  فيه ») reste compatible ; la clé de cet item est unique.
- « قد » : seul « قد + مضارع = احتمال » est enseigné et testé ; « قد + ماضٍ » renvoyé aux chapitres 02/03
  (qui le traitent bien : « كان قد فعل », « وقد فعل ») et nommé « قد التّحقيق » dans l'encadré 🚀 seulement.
- « لو » = التماس ; le piège la distingue de « لو » الشّرطيّة, enseignée avant (ch. 17, displayOrder 4) :
  renvoi juste. الأمر seulement dans l'encadré 🚀 (conforme aux bornes de L89).
- **اليقين / الاحتمال / الإمكان** : aucune paire défendable — sur les 12 items qui mobilisent ces valeurs,
  « احتمال » et « إمكان » ne figurent jamais ensemble dans les options ; le cours explique la différence de
  métalangage du manuel (« إمكان » pour إنْ/أنْ/كي/حتّى/لام التّعليل, « احتمال » pour قد).
- Métalangage du manuel partout (التماس، تحضيض، طلب القيام / طلب ترك القيام، يقين، احتمال، إمكان، إلى حدّ
  زمان القول، العنصر السّياقيّ / القرائن, « حروف الطّلب » attribué au مدخل). Termes classiques (حرفا
  استقبال، قد التّحقيق، فاء السّببيّة) uniquement dans l'encadré 🚀, sans item.

### Patron et langue
- 10 sections, chacune : situation + question → `definition` → tableau → `exemple` (chaque pas dit
  « لأنّ ») → `piege` → `propriete`/`methode` avec cas-limite → `verifie` jumeau → `retenir` ; la section
  « أوظّف » (méthode) n'a pas de définition, ce qui est conforme au type « méthode ». Aucune section
  au-delà de 60 lignes de contenu (C-6 muet). Résumé : 10 puces en miroir, rien d'inventé.
- Arabe correct, vocalisé là où c'est l'enjeu (« لَمَّا يَحْضُرْ », « لمّا يَصِلِ القطارُ » avec la kasra
  de rencontre des sukūn, « لا تَنْسَ »). Chiffres occidentaux, pas de `**` dans les items.

### Erreur corrigée (1)
1. `exercices/03-revision.json` Q1 — **deux options identiques** (la même paire inversée, donc éliminables
   ensemble) : option d « يَنجَحُ — نَجَحَ » (= option a « نَجَحَ — يَنجَحُ ») → **« نَجاحٌ — إنْجاحٌ »**
   (erreur réelle que le cours traite dans sa حالة حدّيّة du §1 : prendre le مصدر مزيد pour un verbe).
   Explication ajustée : « … وفي «نَجَحَ — يَنجَحُ» لا مصدرَ، وفي «نَجاحٌ — يَنجَحُ» الفعلُ مضارعٌ يدلُّ على
   عدمِ الانقضاءِ، و«نَجاحٌ — إنْجاحٌ» مصدرانِ لا فعلَ فيهما، لأنّ المصدرَ المزيدَ «إنْجاحٌ» حدثٌ بلا زمانٍ
   كالمصدرِ المجرّدِ. » (clé b inchangée, plus courte que les autres options ; tranche, qa, Prettier verts).

### Remarques (non corrigées)
- **[MAJOR, facture] `04-defi` Q5** : l'énoncé dit « بفعلٍ **ماضٍ** » et les trois distracteurs portent un
  مضارع (لِيُساعِدْ، لَمْ يُساعِدْ، سَيُساعِدُ) : l'item se résout à la seule forme du verbe, sans la notion,
  et ne vaut pas un défi. Proposition : garder l'énoncé et prendre des distracteurs au passé —
  « إنْ ساعدتَ زميلَكَ ساعدَكَ » (إمكان, pas طلب), « ساعدتَ زميلَكَ في الواجبِ أمسِ » (sans حرف),
  « وفّقَكَ اللهُ في الواجبِ » (دعاء sans حرف).
- **[MAJOR, facture] `04-defi` Q2** : l'énoncé pose « جملةٌ قد تكونُ دعاءً وقد تكونُ خبرًا », et deux
  distracteurs placent « وفّقَ اللهُ أخاكَ » dans une حكمة ou une قاعدة علميّة — contredits par l'énoncé et
  absurdes pour une phrase adressée à une personne : seule l'option b concurrence la clé. Proposition : deux
  autres contextes de **خبر** (p. ex. « يقولُها أبوكَ وهو يُخبرُ جدَّكَ بنجاحِ أخيكَ في المناظرةِ »).
- [MINOR] items « بالتّرتيب » à trois volets (`04-defi` Q6, `05` Q5, `05` Q6) : la clé porte la valeur
  majoritaire de chaque volet ; un élève qui vote à la majorité la trouve. Inhérent au format, à surveiller.
- [MINOR] faits re-testés : quiz Q3 ↔ `01` Q6 (دعاء ↔ « يُطلَب انقضاؤه في المستقبل », le même fait dans les
  deux sens) ; `02-boss` Q5 ↔ `03-revision` Q5 (« لمّا » = إلى حدّ زمان القول, deux fois).
- [MINOR] cours §4 : « الصّيغتانِ في الصّفِّ الواحدِ مختلفتانِ **ومعناهما واحدٌ** » — à la lettre faux pour la
  ligne « الحكمة » (deux sentences différentes) → « ودلالتُهما على الزّمانِ واحدةٌ ».
- [MINOR] cours §1, `propriete` : « فلا يدخلُ الزّمانُ على المصدرِ لأنّ كلمتَه أطولُ » — portée de la négation
  ambiguë (peut se lire comme une cause) → « فلا يكتسبُ المصدرُ زمانًا لأنّ كلمتَه أطولُ ».
- [MINOR] style : « بينما ينتظرُ سامي النّتائجَ أمسِ… » (aussi `01` Q5 « بينما يدرسُ سامي أمسِ… » et le
  `verifie` « بينما يكتبُ الأستاذُ … البارحةَ … ») — l'adverbe de temps dans la proposition de « بينما » est
  gauche ; plus naturel : « أمسِ، بينما ينتظرُ سامي النّتائجَ…، جاءَهُ صديقُه ».
- [MINOR] l'encadré « 🚀 للتوسّع (خارج كتاب التّاسعة) » porte aussi la note sur الأمر, qui est bien dans le
  livre (مدخل de L89 ; leçon 7 « الأمر والنّهي ») — le texte le dit lui-même ; l'étiquette est un peu large.
- [MINOR] 10 sections (> ~8 notions, R-13) : justifié par les deux leçons du manuel ; à garder en tête si
  une scission est discutée.
- La méthode du §10 (« commence par le حرف ») est une heuristique du chapitre, non du manuel (qui va صيغة →
  انقضاء → سياق) ; la présenter comme correction d'une « erreur » est un peu fort, mais pas faux.

**Verdict : conforme après corrections** (1 correction) — deux défauts de facture MAJOR à reprendre
(`04-defi` Q2, Q5). **Clarté : 5/5.**

---

## Chapitre 02 — `02-an-nawasikh` (L104 « دلالة النّواسخ الفعليّة على الزّمان »)

**Questions re-résolues : 35** (quiz 5 + exercices 01, 02, 04, 05, 06 × 6). Toutes les clés sont justes et
uniques. Cours : 8 sections, 8 `exemple`, 8 `piege`, 8 `verifie` re-dérivés — un `verifie` portait une
affirmation fausse (corrigée ci-dessous).

### Justesse et fidélité
- Définitions = خلاصة p.107 §1–4, fidèlement reformulées : المسند / المسند إليه (« زمان نسبة خبرها إلى
  اسمها ») ; **كينونة** (كان، ليس) / **صيرورة** (صار، أصبح، أضحى، أمسى، **بات**) / **ديمومة** (**ظلّ**، ما زال،
  ما برح، ما فتئ، ما انفكّ، ما دام), listes exactes ; « كان » dans la جملة **بسيطة** (ماضٍ = انقضاء في
  الماضي ; مضارع مرفوع = عدم انقضاء ; أمر = طلب) et **مركّبة** (« كان + قد فعل » = ماضٍ بعيد ; « كان +
  يفعل » = حدث استمرّ في الماضي) ; المقاربة (كاد، أوشك), الشّروع (شرع، أخذ، جعل، طفق), الرّجاء (عسى =
  إمكان في المستقبل).
- **بسيطة / مركّبة définie par le خبر** (« كلمة أو عبارة لا إسناد فيها » / « جملة فعليّة ») : conforme au
  مدخل II vu à l'image p.105 (exemples أ–ج / د–هـ).
- **« كاد » = قَرُبَ ولم يقعْ** (cours, résumé, `01` Q4, `02` Q6, `06` Q3) : conforme ; le manuel dit
  « قرب وقوع الحدث » et demande p.105 « زمان وقوع الفعل المسند **أو عدم وقوعه** ».
- **« ما زال »** = un seul ناسخ, « ما » partie du verbe qui nie l'interruption, pas l'état (cours, `01` Q3,
  `04` Q4) : conforme à la liste du manuel ; l'analyse classique (« ما » نافية, شرط النّفي) est dans
  l'encadré 🚀 seulement. **« بات » = « صار »** (حالة حدّيّة du §5, `02-boss` Q2) : conforme.
- Rien d'hors leçon dans les items : 0 إعراب (seul « المضارع المرفوع », terme du manuel), 0 إنّ وأخواتها,
  0 كان الزّائدة, 0 ناقص/تامّ, 0 « وقت الصّباح/المساء » — tout cela est dans l'encadré 🚀, sans item. La clé
  suspecte signalée par le brief (`04-defi` « جاءَ الذي كانَ مجتهدًا ») n'existe plus.
- Cohérence avec 18 : mêmes termes (انقضاء / عدم انقضاء, المضارع المرفوع, القرينة = العنصر السّياقيّ) ; le
  renvoi du 18 vers 02 pour « قد + ماضٍ » est honoré (« كان + قد فعل ») ; « إمكان » pour عسى comme pour
  إنْ/أنْ au 18, jamais opposé à « احتمال » dans un item.

### Erreur corrigée (1)
1. `cours.md`, section « ⚖️ الكينونةُ في الزّمانِ », `verifie` (l. 219) : « تنفي كينونةَ المنعِ، أي كونَ
   الحديثِ ممنوعًا، **ولا تقولُ إنّه مباحٌ، لأنّ «ليسَ» تنفي الكينونةَ وحدَها** » → « تنفي كينونةَ المنعِ، أي
   كونَ الحديثِ ممنوعًا، **لأنّ «ليسَ» تدلُّ على نفيِ كينونةِ الحدثِ المسندِ إلى اسمِها** ». L'affirmation
   retirée est fausse : ممنوع / مباح sont contradictoires (« ليسَ ممنوعًا » veut dire « مباح ») ; la حالة
   حدّيّة (« ليس » n'affirme pas le contraire du خبر) ne vaut que pour des contraires comme هادئة / صاخبة,
   que la `propriete` emploie à juste titre. (`content:qa` vert après correction.)

### Remarques (non corrigées)
- [MINOR] titres sans indicateur ⭐ : quiz « اختبار فهم الدرس », `01`, `02`, `04`, `05` (seul `06` porte
  ⭐⭐⭐⭐) — les chapitres 18 et 19 les portent tous.
- [MINOR] une même notion (« كان + قد فعل » / « كان + يفعل ») testée 6 fois : quiz Q4, `01` Q6, `02` Q3,
  `04` Q3, `05` Q6, `06` Q2 ; `01` Q6 et `04` Q3 sont proches (même contraste, énoncé nu puis en contexte).
- [MINOR] quiz Q2 reprend la phrase du `verifie` du §2 (« كُنْ صبورًا »), dont la réponse est dépliable.
- [MINOR] distracteurs éliminables à vue : `01` Q5 d « نُفيتْ كينونةُ الحدثِ » et `05` Q3 d « لا حالةَ
  سابقةً، فالجملةُ تنفي الازدحامَ » (aucune négation dans l'énoncé).
- [MINOR] §3, `exemple` : le pas 4 (synthèse) n'a pas de « لأنّ », et le « لأنّ » du pas 3 est circulaire
  (« لأنّ هذا هو ما تدلُّ عليه «كانَ» مع «قد» والماضي »).
- [MINOR] §2, tableau : « القرينة : صيغة الأمر » pour « كُنْ » — la forme n'est pas une قرينة.
- [MINOR] §8 : « ستّةُ نواسخَ في أربعةِ أسطرٍ » — le texte est un seul paragraphe ; le nombre de lignes dépend
  de l'affichage.
- [MINOR] `04-defi` Q5 (et le piège du §4) testent le critère « تاء الفاعل » pour dire que « ليس » est un
  verbe : acquis des années antérieures, absent de L104 (qui range simplement ليس parmi les نواسخ
  فعليّة) ; enseigné dans le chapitre, donc acceptable.

**Verdict : conforme après corrections** (1 correction). **Clarté : 5/5.**

---

## Chapitre 03 — `03-al-mansoubat` (L110 « دلالة بعض الوظائف على الزّمان : المفعول فيه — الحال »)

**Questions re-résolues : 35** (quiz 5 + exercices 01, 02, 04, 05, 06 × 6). Toutes les clés sont justes et
uniques. Cours : 7 sections, 7 `exemple`, 7 `piege`, 7 `verifie` re-dérivés — tous justes.

### Justesse et fidélité
- Définitions = خلاصة p.113 §1–4 : les trois fonctions qui disent le temps (المفعول فيه للزّمان، الحال،
  الخبر) ; التّزامن par عند(ما)، لمّا، حين(ما)، إذا، بين(ما) ; **أسبقيّة الحدث الرّئيسيّ** par قبل (أن، ما) et
  **لاحقيّة** par بعد (أن، ما), toujours lues du point de vue du حدث رئيسيّ (celui de la phrase qui ne
  commence pas par la أداة), comme dans le manuel ; les **cinq valeurs de الحال** (« يفعل » / « وهو يفعل »
  مزامنة لفعل منقضٍ أو غير منقضٍ ; « وقد فعل » قبيل فعل منقضٍ / غير منقضٍ ; « وكان قد فعل » قبل فعل منقضٍ),
  récapitulées dans un tableau.
- **Le خبر porteur de temps est analysé juste partout** : phrases sans verbe (« سفرُ أخي بعدَ ساعةٍ »,
  « الاجتماعُ بعدَ ساعةٍ », « العرضُ بعدَ العشاءِ », « فالقطارُ التّالي بعدَ نصفِ ساعةٍ », « زيارةُ أخي بعدَ
  أسبوعٍ ») ; et « **الحافلةُ تصلُ بعدَ دقيقتَينِ** » (`02-boss` Q6) est bien un **مفعول فيه** rattaché à
  « تصلُ », l'explication opposant « الحافلةُ بعدَ دقيقتَينِ » (خبر). `04-defi` Q6 et `05` Q4 tiennent la même
  ligne (« أخي يسافرُ بعدَ أسبوعٍ » = مفعول فيه).
- Aucune règle d'إعراب classique attendue par un item (0 ظرف، منصوب، نكرة، مشتقّة, « جواب كيف ») : « ظرف »,
  « واو الحال » et les autres منصوبات sont dans l'encadré 🚀 seulement. La définition « الحال وظيفة تبيّن
  هيأة الفاعل أو المفعول به غالبًا » vient du manuel de textes (أنوار p.97, « أتعهّد لغتي ») ; la mention
  🚀 des autres valeurs de الحال (رغم، النّتيجة، الغرض، الظّرفيّة المكانيّة) est conforme à أنوار p.178, vue à
  l'image. Les sources de `chapter.json` sont donc exactes.
- Cohérence : avec 18, « لمّا + ماضٍ = حين / لمّا + مضارع = نفي » et « قد + ماضٍ dans la حال = انقضاء ≠ قد +
  مضارع = احتمال », avec renvoi explicite au ch. 18 ; mêmes termes (منقضٍ / غير منقضٍ, العناصر السّياقيّة).
  Avec 17, « إذا » aussi أداة شرط (renvoi juste). **Avec 19 : aucun « تمييز » ni « معدود » dans le 03**
  (encadré retiré, comme le demandait le brief).

### Erreur corrigée (1)
1. `exercices/04-defi.json` Q3, énoncé : « **الحدثُ الأوّلُ:** غسلَ الطّفلُ يدَيه. **الحدثُ الثّاني:** جلسَ إلى
   المائدةِ. أيُّ الجملِ… والحدثُ الرّئيسيُّ فيها «جلسَ الطّفلُ إلى المائدةِ»؟ » → « **غسلَ الطّفلُ يدَيه
   أوّلًا، ثمّ جلسَ إلى المائدةِ.** أيُّ الجملِ… والحدثُ الرّئيسيُّ فيها «جلسَ الطّفلُ إلى المائدةِ»؟ ».
   L'énoncé employait « الحدث الثّاني » au sens chronologique alors que, dans le métalangage du manuel et
   du chapitre, le حدث ثانٍ est celui qu'introduit la أداة. Il désignait donc le même événement comme
   ثانٍ puis comme رئيسيّ, et sa lecture technique menait au distracteur d (« غسلَ… قبلَ أن يجلسَ »). Clé b,
   options et explication inchangées ; tranche, qa et Prettier verts.

### Remarques (non corrigées)
- [MINOR] titres sans indicateur ⭐ : quiz, `01`, `02`, `04`, `05` (seul `06` porte ⭐⭐⭐⭐).
- [MINOR] `01` Q6, explication : « «مبتسمًا» **اسمُ فاعلٍ** بمعنى «يبتسمُ» » — notion des المشتقّات (retirée
  du livre de 9ᵉ ; ch. 06 affiché après) → « «مبتسمًا» مفردٌ بمعنى «يبتسمُ» ».
- [MINOR → à arbitrer] « المفعول لأجله » apparaît dans la prose du §1 (« فالعلّيّةُ يؤدّيها المفعولُ لأجلِه ») et
  comme distracteur du quiz Q1 (option b, et son explication), en plus de l'encadré 🚀. La fiche (§2 ter)
  range « المفعول المطلق et لأجله » parmi les notions absentes du livre de 9ᵉ, et le brief B03 les veut
  « sans item ». Le cas reste un doute, parce que le مدخل I de L110 fait nommer la fonction de « بحثًا عن تعزية
  لنفسي » (réponse non imprimée). Si l'on tranche pour la lettre du brief : option b → « المفعولُ فيه
  للزّمانِ والحالُ والمفعولُ به » (explication : « والمفعولُ به يقعُ عليه الفعلُ ولا يقولُ زمانًا »), et au §1
  « فالعلّيّةُ في «خوفًا من التّأخّرِ»، والكيفيّةُ يؤدّيها الحالُ في «قلقًا» ».
- [MINOR] items à trois volets (`04-defi` Q2, `05` Q4) : chaque distracteur n'est faux que sur un volet,
  donc la clé porte la valeur majoritaire de chacun.
- [MINOR] `06` Q6 b « خرجَ التّلاميذُ عندما تنتهي الحصّةُ » — discordance de temps visible, éliminable à vue.
- [MINOR] `05` Q1 : distracteurs rallongés (« وحيدًا… الكبيرةِ », « بهدوءٍ… المطلّةِ على الحديقةِ ») face à
  une clé courte (30 car. contre 43–56) ; aucun indice de longueur au sens du gate, mais remplissage visible.
- [MINOR] `exemple` sans « لأنّ » à un pas : §3 pas 2, §4 pas 4 (synthèse), §6 pas 1.

**Verdict : conforme après corrections** (1 correction). **Clarté : 5/5.**

---

## Chapitre 19 — `19-al-adad-wal-madud` (L116 « العدد والمعدود (1) » + L122 « العدد والمعدود (2) »)

**Questions re-résolues : 35** (quiz 5 + 5 exercices × 6). Toutes les clés sont justes et uniques ; trois
**explications** étaient fausses (corrigées ci-dessous). Cours : 11 sections, 11 `exemple`, 11 `piege`,
11 `verifie` re-dérivés (accords, إعراب, ضبط) — tous justes.

### Justesse et fidélité
- Conforme aux خلاصات p.119 et p.125 et au **tableau p.126** : أصليّ / رتبيّ (+ « المرتَّب ») ; formation du
  رتبيّ (2–10 sur فاعِل ; 11–19 : premier élément seul ; العقود والمائة والألف والمليون = forme du أصليّ) ;
  بسيط / مركّب (بالعطف، بالإضافة، بالتّمييز، مزجيّ) ; المطابقة : **directe** pour 1, 2, 11, 12, **inverse**
  pour 3–10, **mixte** pour 13–19, **invariable** pour العقود والمئات والآلاف والملايين (les unités d'un
  composé par عطف suivent leur règle : « خمسٌ وعشرونَ طالبةً ») ; 1–2 = منعوت + نعت ; 3–10, مئات et آلاف
  = مضاف + مضاف إليه (معدود جمع / مفرد مجرور) ; 11–19 et العقود = مميَّز + تمييز (مفرد منصوب) ; 11–19
  « مبنيّ على الفتح بجزأيه » sauf le premier élément de اثنا / اثنتا عشر (إعراب المثنّى) ; العقود = إعراب
  جمع المذكّر السّالم ; رتبيّ 1–10 et مائة / ألف / مليون معرب, 11–19 « مبنيّ على فتح الجزأين » (« الصّفحةِ
  الخامسةَ عشرةَ : نعت في محلّ جرّ »), علاقة نعتيّة أو إضافة, عقود رتبيّة = جمع المذكّر.
- **« تمييز العدد »** : le terme « تمييز » n'est employé que là où le manuel l'emploie (11–19 et العقود) ; le
  معدود de 3–10 est partout un **« مضاف إليه »** (terme du manuel), « تمييز » n'apparaissant pour lui
  qu'une fois, dans l'encadré 🚀 — conforme au brief.
- **« ثلاث مائة » / « ثلاثمائة »** : le cours écrit « ثلاث مائة » comme le manuel et précise « وإن كُتبَ
  أحيانًا كلمةً واحدةً » ; `05` Q1 emploie « ثلاثُمائةٍ » (attaché) comme مركّب بالإضافة, avec la même
  remarque. Cohérent. « مائة » suit l'orthographe du manuel.
- Aucune coquille du manuel reprise : ni « عمر بن الخطّاب… الخليفة الرّابع », ni référence coranique
  chiffrée (« سبع سماوات » et « تسع وتسعون نعجة » sont cités sans numéro de verset).
- Cohérence avec 03 : aucun « تمييز » ni « معدود » dans le 03, et le 03 annonce le 19 en clôture.

### Erreurs corrigées (4)
1. `cours.md` (×3 : piège et `propriete` du §1) et `resume.md` (×1) — **orthographe** : « مباريّات » →
   « **مباريات** » (pluriel de « مباراة », sans chadda ; le reste du corpus écrit « المباريات »).
2. `exercices/02-boss.json` Q1, explication : « … أو تقلبُ العددَ كلَّه **فتعاملُه معاملةَ الأعدادِ من 3 إلى
   10** » → « … أو تقلبُ العددَ كلَّه **فتضعُ مع «لاعبًا» صيغةَ «لاعبةً» ومع «لاعبةً» صيغةَ «لاعبًا»** ».
   L'option qui traite le nombre « comme 3–10 » (les deux parties inversées) est celle que la phrase
   décrit juste avant (« تعكسُ الجزأينِ معًا ») ; la dernière option échange les deux formes.
3. `exercices/04-defi.json` Q3, explication : « فخطأُ «سبعةً» **تذكيرٌ** في غيرِ موضعِه » → « … **تأنيثٌ** في
   غيرِ موضعِه ». Le cours pose « ثلاثةٌ بتاءٍ مؤنّثٌ » : « سبعةً قصّةً » est un تأنيث indu, et le mot
   contredisait le métalangage du chapitre (« أنّثَ / حقُّه التّذكيرُ » en `04` Q6, quiz Q3).
4. `exercices/05-entrainement.json` Q5, explication : « و«أربعونَ» **معطوفٌ عليه** مرفوعٌ » → « و«أربعونَ»
   **معطوفٌ على «خمسةٌ»** مرفوعٌ ». « المعطوف عليه » désigne le premier conjoint (« خمسةٌ ») ; l'explication
   contredisait sa propre clé (« معطوفٌ مرفوعٌ… ») et l'option d de `05` Q2, qui emploie le terme
   correctement.
(Prettier, `tranche` et `qa` verts après corrections.)

### Remarques (non corrigées)
- [MINOR, cohérence 02 ↔ 19] `05` Q6 attend « **خبرُ كانَ** منصوبٌ » (et le §7 dit « ثالثَ… (خبرُ كانَ) »),
  alors que le ch. 02 place l'analyse « ترفعُ الاسمَ وتنصبُ الخبرَ » dans son encadré 🚀 (« خارجَ كتابِ
  التّاسعةِ… دونَ أسئلةٍ »). Nommer la fonction d'un nombre relève bien de L122 (تمارين 3–4) et « خبر كان »
  est un acquis du collège ; mais le message reçu par l'élève est contradictoire. Proposition : un cadre
  sans ناسخ (« صافحتُ خامسَ المتسابقينَ » → مفعول به), ou nuancer la phrase de l'encadré du 02.
- [MINOR] notions affichées plus tard : l'option « بزيادةِ ياءِ نسبةٍ » (quiz Q2), « السّباعيُّ » et
  « منسوبٌ » (`01` Q2) relèvent de النّسبة (ch. 14, displayOrder 12, après le 19).
- [MINOR] `03` Q2, explication : « منصوبٌ **على الظّرفيّةِ** » — terme classique ; celui du manuel est
  « مفعولٌ فيه ».
- [MINOR] `04-defi` Q6 reprend mot pour mot la phrase du piège du §11 (« اشترى المديرُ ستّةَ عشرَ كتبٍ »).
- [MINOR] patron : l'encadré 🚀 est une section `##` (et non un encadré final `>` comme aux 18/02/03) ; au
  §11 (أوظّف) la `methode` précède l'`exemple` ; des pas d'`exemple` sans « لأنّ » (§4 pas 2, §5 pas 1 et 4,
  §6 pas 4–5, §7 pas 3, §11 pas 3).
- [MINOR] 11 sections (> ~8 notions, R-13), justifiées par les deux leçons ; aucune section au-delà de 60
  lignes de contenu.
- [MINOR] §11 : « سبعةَ عشرَ تلميذًا… وفازَ منهم خمسُ تلميذاتٍ » — cinq filles parmi « 17 تلميذًا »
  (masculin d'un groupe mixte) : défendable, mais peut dérouter un élève de 14 ans.
- [doute, sans action] ordinal composé « مبنيّ على فتح الجزأين » : c'est la règle du manuel (p.125–126), que
  le chapitre suit. Certaines grammaires déclinent le premier élément (« الصّفحةِ الخامسةِ عشرةَ »), ce que
  la fiche signale au §6. Le piège du §7 traite cette variante d'erreur, mais il la présente prudemment
  comme « القاعدة في كتاب التّاسعة » ; aucun item ne la propose comme option, donc pas de double clé
  (`03-revision` Q5 et le `verifie` du §7 vérifiés).

**Verdict : conforme après corrections** (4 corrections). **Clarté : 5/5.**

---

## Synthèse

| Chapitre | Questions re-résolues | Clés fausses | Erreurs corrigées | Remarques ouvertes | Verdict | Clarté |
| --- | --- | --- | --- | --- | --- | --- |
| 18 `dalalat-az-zaman` | 35 | 0 | 1 (option en double) | 2 MAJOR de facture (`04-defi` Q2, Q5), MINOR | conforme après corrections | 5/5 |
| 02 `an-nawasikh` | 35 | 0 | 1 (`verifie` faux sur « ليس ») | MINOR | conforme après corrections | 5/5 |
| 03 `al-mansoubat` | 35 | 0 | 1 (énoncé « الحدث الثّاني » contradictoire) | MINOR | conforme après corrections | 5/5 |
| 19 `al-adad-wal-madud` | 35 | 0 | 4 (orthographe ×4 lieux, 3 explications) | MINOR (dont cohérence 02 ↔ 19) | conforme après corrections | 5/5 |
| **Total** | **140** | **0** | **7** | | | |

Contrôles finaux, depuis le moteur : `content:check` vert (120 matières, 28 439 questions) ; `content:qa` :
0 constat sur `arabic/(18|02|03|19)-` ; `content:tranche --chapters 18,02,03,19` : clé strictement la plus
longue 0/140, positions a 36 · b 33 · c 36 · d 35, 0 paire proche (l'outil compare la tranche à tous les
items de la matière `arabic` : aucun quasi-doublon avec un autre chapitre) ; Prettier `--check` vert sur
tous les `.json` des quatre chapitres (aucun `.md` passé à Prettier). Aucune écriture git. Je n'ai touché ni au 10,
ni au 11, ni aux chapitres de l'autre auditeur.
