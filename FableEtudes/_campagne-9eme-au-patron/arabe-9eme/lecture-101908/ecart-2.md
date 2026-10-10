# Écart tranche 2 (manuel 101908 p.47–88) ↔ `content/arabic/`

Lu : `04-al-asalib/cours.md` (en entier) + `resume.md` + `chapter.json` ; `01-i3rab-wal-bina/cours.md` (l.30–180) ;
grep `استفهام|شرط|جازم|بلى|جواب ال` sur **tous** les `cours.md`, `quiz.json`, `exercices/*.json` des 14 chapitres
(23 items repérés, lus en entier). Aucun fichier du corpus modifié.

## Vue d'ensemble

| Leçon du manuel | Chapitre(s) | Service |
|---|---|---|
| L47 — الاستفهام عن مضمون الجملة (p.47–53) | `04-al-asalib` § أسلوب الاستفهام | **partiel** |
| L54 — الاستفهام عن عنصر… (p.54–64) | `04-al-asalib` § أسلوب الاستفهام (+ `01` : « أسماء الاستفهام مبنيّة ») | **partiel** (tableau des أدوات oui ; fonctions, عدم اليقين, تسوية non) |
| L65 — اسم الاستفهام المقترن بحرف الجرّ (p.65–71) | aucun (seul « لِمَ » dans un tableau de `04`) | **pas du tout** |
| L72 — الشّرط (1) : إن، لو (p.72–76) | aucun chapitre ; 1 item dans `04/06-defi-concours` (إن تدرسْ تنجحْ) | **pas du tout** (pas une ligne de cours) |
| L77 — الشّرط (2) : أسماء الشّرط (p.77–82) | aucun ; 1 item dans `01/06-defi-concours` (مَن يسعَ… : جزم بحذف حرف العلّة) ; `01/cours.md` l.84 « أسماء… الشرط » مبنيّة | **pas du tout** |
| L83 — الشّرط : الافتراض والاستنتاج (p.83–88) | aucun | **pas du tout** |

**Constat majeur** : sur les 6 leçons de la tranche, la **moitié (le bloc الشّرط, 3 leçons, 17 pages)** n'a
**aucun cours** dans `content/arabic` — le mot « شرط » n'apparaît dans `04/cours.md` que pour « شروط التعجّب ».
Or le شرط est 3 leçons sur 19 du نحو de 9ᵉ, en année de concours. Et le استفهام est servi par **une seule section**
(~45 lignes) là où le manuel lui consacre 3 leçons et 25 pages.

---

## L47 — الاستفهام عن مضمون الجملة → `04-al-asalib` (partiel)

**Ce qui est servi** : هل / الهمزة pour la question « عن الجملة كلّها » à réponse نعم/لا (tableau + definition) —
recoupe la 2ᵉ ligne de la خلاصة p.50.

**Enseigné autrement**
- Métalangage : le chapitre dit « سؤال عن الجملة كلّها » et (resume, items) **« التّصديق / التّعيين »** ; le manuel dit
  « الاستفهام **عن مضمون الجملة** » et n'emploie jamais تصديق/تعيين (« التّعيين » n'apparaît en L54 que comme valeur de **أيّ**).
- Le chapitre définit le استفهام comme « أسلوب » ; le manuel comme « **عمل لغويّ** ينجزه المتكلّم مستخبرا ».

**Absent du chapitre** (enseigné p.48–50) : la **صدارة** du حرف ; **مثبت / منفيّ** dans la question et la valeur du منفيّ
(« تذكير بشيء معلوم أو استخبار عن حصول شيء متوقّع ») ; tout le système des **réponses** : نعم / إي / لا / **بلى**,
« **إثبات النّفي / إبطال النّفي** » (ألم تفعل ؟ — نعم = je n'ai pas fait ; بلى = j'ai fait). **Zéro item sur بلى** dans
tout le corpus — c'est pourtant le cœur de la خلاصة et de 4 exercices sur 9.

**Testé par le chapitre et non enseigné par la leçon en 9ᵉ**
- « هل للتّصديق فقط، والهمزة للتّصديق والتّعيين » (+ « هل لا تدخل على الاسم المفرد ») : 4 items
  (`quiz.json`, `01-pratique`, `02-boss`, `04-defi`). Doctrine classique juste, mais **non au manuel** (la seule trace :
  أَوَ vs وهل, مدخل II p.48).
- 🔴 **Item fautif** `04-al-asalib/exercices/04-defi.json` (« … استخدامًا صحيحًا لهمزة الاستفهام دون هل ») :
  `correctOption: "b"` = « **أيُّهما** أحسنُ خُلُقًا: زيدٌ أم عمرٌو؟ » — cette phrase ne contient **pas** de همزة استفهام
  (أيّ est un اسم استفهام, L54 p.60). L'option qui illustre la règle visée est « **أأنتَ** كتبتَ الدرسَ؟ » (c). Clé à corriger
  (à confirmer par l'auditeur ; non modifiée ici).
- `10-fahm-wa-intaj` (3 items) et `11-annales-subur` (1 item) testent le **استفهام إنكاريّ / تقرير / تحسّر** : le manuel de
  نحو ne nomme pas ces valeurs (seulement « تذكير بشيء معلوم », p.50, et en L54 « عدم اليقين / الحيرة / التّسوية »). Légitime
  au titre de la lecture/rhétorique, à sourcer ailleurs (manuel نصوص 101909).

## L54 — الاستفهام عن عنصر من العناصر المكوّنة للجملة → `04-al-asalib` (partiel)

**Ce qui est servi** : le tableau des أدوات (من، ما، ماذا، متى، أين، كيف، كم، لماذا/لِمَ) avec leur objet (عاقل، غير عاقل،
زمن، مكان، حال، عدد، سبب) ; كم + تمييز منصوب ; `01` dit « أسماء الاستفهام… مبنيّة » (= خلاصة p.60).

**Enseigné autrement**
- Le chapitre glose كيف par « **عن الحال** » ; le manuel : « **الكيفيّة** », fonctions خبر / حال / **مفعول مطلق** (p.60).
- Le chapitre range ماذا et لماذا comme أدوات à part entière ; la خلاصة du manuel ne liste **que 7 noms** (من، ما،
  أيّ+مضاف إليه، كيف، أين، متى، كم) ; لماذا n'y est qu'un « مركّب جرّ مفعول لأجله » (tableau 14 p.60) — c.-à-d. L65.
- **أيّ** (« للتّعيين، عاقل/غير عاقل », avec مضاف إليه obligatoire) **absent** du tableau du chapitre.
- Le manuel lit la question par la **fonction** de l'اسم استفهام (« لاسم الاستفهام… محلّ إعرابيّ… تُسند إليه وظيفته الّتي
  يقتضيها موقعه », p.60 ; 14 tableaux d'analyse) ; le chapitre ne donne **aucun إعراب** d'اسم استفهام.

**Absent du chapitre** : fonction syntaxique de l'اسم (مبتدأ / خبر / مفعول به / حال / مفعول مطلق / مفعول فيه / اسم ناسخ) ;
**الاستفهام المعبّر عن عدم اليقين** (لا أدري كيف… / تُرى…, verbes درى، علم، عرف، رأى منفيّة ; عجب، حار، احتار) ; **التّسوية**
(سواء / سيّان / يستوي + الهمزة + أم/أو) ; « التّحليل في المستوى الأوّل » d'une phrase à استفهام enchâssé
(« مركّب إسناديّ مفعول به »).

**Testé et non enseigné en 9ᵉ** : rien de faux ; seule la dichotomie تصديق/تعيين (ci-dessus). ⚠️ Divergence de lettre : la
خلاصة p.60 dit « أسماء الاستفهام أسماء **مبنيّة** » sans exception ; un contenu fidèle doit savoir que le manuel ne
signale pas que **أيّ** est معربة (son propre tableau 4 la vocalise « أيُّهم » مبتدأ).

## L65 — اسم الاستفهام المقترن بحرف الجرّ → aucun chapitre (pas servi)

Seule trace : « لماذا / لِمَ — عن السبب » dans le tableau de `04`. **Rien** sur : مركّب الجرّ en صدارة ; les 7 حروف (بـ، من،
لـ، على، عن، إلى، حتّى) et leurs valeurs (مفعوليّة، سببيّة، كيفيّة، ابتداء/انتهاء الغاية، مصدر الشّيء، حاليّة، مصاحبة) ;
« مركّب الجرّ… في الجملة الاسميّة الخالية من الفعل… **خبر مقدّم** » (فيمَ جزعك ؟ / بكم التّذكرة ؟) ; la chute de l'alif de
ما (لِمَ، بِمَ، فيمَ، عمَّ، مِمَّ، علامَ، إلامَ، حتّامَ) — ni dans le manuel en règle, ni dans le corpus.

## L72 — الشّرط (1) : حرفا الشّرط (إن)، (لو) → aucun chapitre (pas servi)

**Seul item** : `04-al-asalib/exercices/06-defi-concours.json` — « إنْ تدرسْ تنجحْ : نوع إنْ وإعراب الفعلين » → réponse
« أداة شرط **جازمة** ; تدرسْ **فعل الشرط** مجزوم و تنجحْ **جوابه** مجزوم ». Ce métalangage (**أداة شرط جازمة / فعل الشّرط**)
**n'est pas celui du manuel**, qui dit : « حرف الشّرط » ; « **المركّب الحرفيّ** المعبّر عن الحدث الثّانويّ… يكوّنان معه
**مفعولا يفيد الشّرط** » ; « يقيّد مفعولُ الشّرط الحدثَ الرّئيسيّ المسمّى عادة **جواب الشّرط** » (p.74). Le جزم n'est
d'ailleurs **pas énoncé** dans la خلاصة de L72 (seulement demandé en مدخل II.3 « وجوه الإعراب ») ; il est énoncé en L77 pour
les أسماء.
**Absent** : le cœur sémantique — **حدث رئيسيّ / حدث ثانويّ**, **ممكن / ممتنع** ; **لو** (امتناع لامتناع ; لو + ماضٍ ou
مضارع منفيّ بلم ; لام du جواب) — **zéro occurrence de لو dans le corpus** ; الفاء الرّابطة (pratiquée ex.4 p.76).

## L77 — الشّرط (2) : أسماء الشّرط → aucun chapitre (pas servi)

**Traces** : `01/cours.md` l.84 « أسماء الاستفهام **والشرط** » parmi les مبنيّات ; `01/exercices/06-defi-concours.json`
« مَن يسعَ إلى الخيرِ يجدْ ثمرتَه » → علامة جزم يسعَ = حذف حرف العلّة, « لأنّه **فعل الشرط** بعد مَن ». Juste, mais
c'est la morphologie du جزم qui est testée, pas la leçon.
**Absent** : le tableau des **10 أسماء** (مَن، ما، مهما، أيّ، كيفما، إذا، متى، حيثما، أينما، أنّى) et leurs sens ; « يلزم
اسم الشّرط صدارة الجملة » ; « **لا يقع بعد فعل أو حرف ناسخ** » (→ إنّ مَن يحاسب نفسه يربح = موصول) ; la fonction de
« اسم الشّرط + المركّب الإسناديّ المتعلّق به » (فاعل/مفعول به/مبتدأ ; حال/مفعول مطلق ; مفعول فيه) ; **جزم المضارع sauf
après إذا** ; « لا يجزم المضارع إذا تقدّم على اسم الشّرط » ; اسم الشّرط مجرور بحرف (على مَن تسلّمْ أسلّمْ).
**Enseigné autrement (en cas d'écriture)** : le manuel analyse la protase comme **« مركّب موصوليّ »** porteur d'une fonction
(مبتدأ / مف. به / **حال** pour مهما, p.80) — non comme « اسم شرط جازم مبنيّ في محلّ… + فعل الشّرط + جملة جواب الشّرط في
محلّ جزم ». Un chapitre neuf doit choisir et le dire (le concours corrige-t-il en métalangage du manuel ? — à vérifier sur
les annales).

## L83 — دلالة الشّرط على الافتراض والاستنتاج → aucun chapitre (pas servi)

**Absent en entier** : افتراض الممكن (إنْ, متى ; إنْ + حالة ممكنة في الماضي), افتراض الممتنع (لو), **الاستنتاج** (إنْ / إذا :
حدث ثانويّ معلوم → حدث رئيسيّ مستنتج), l'opposition وجوب / إمكان / امتناع et ses **قرائن**. Leçon purement sémantique,
très exploitable en QCM (« quelle valeur : افتراض ممكن / ممتنع / استنتاج ? »).
`09/10` (إنتاج/فهم) ne la recouvrent pas : aucun item n'y porte sur la valeur d'un شرط.

---

## Ce que le corpus teste et que ces leçons n'enseignent pas en 9ᵉ (synthèse)
1. **تصديق / تعيين** (hamza vs هل) — 4 items `04` : hors manuel نحو 9ᵉ.
2. **أداة شرط جازمة / فعل الشّرط / جواب الشّرط مجزوم** — 2 items (`04/06`, `01/06`) : notion juste, métalangage ≠ manuel
   (« حرف الشّرط » ; « مفعول الشّرط » ; « مركّب موصوليّ »).
3. **استفهام إنكاريّ / تقريريّ / تحسّريّ** — 4 items `10`, `11` : hors manuel نحو (valeurs du manuel : تذكير بمعلوم,
   عدم اليقين/حيرة, تسوية).
4. 🔴 **Une clé fausse** : `04-al-asalib/exercices/04-defi.json`, item « همزة الاستفهام دون هل », clé `b` (phrase en أيّ, sans
   hamza).

## Ce qu'il faudrait (pour décision, rien n'est fait)
- Un chapitre **الشّرط** (3 leçons : إن/لو · أسماء الشّرط · افتراض/استنتاج) — c'est l'écart le plus lourd de la tranche.
- Étoffer **الاستفهام** (ou chapitre propre) : réponses نعم/لا/بلى/إي + إثبات/إبطال النّفي ; fonctions des أسماء ; أيّ ;
  عدم اليقين / التّسوية ; اسم الاستفهام المجرور + خبر مقدّم.
- Trancher le **métalangage** (manuel « مفعول الشّرط / مركّب موصوليّ / حدث رئيسيّ-ثانويّ » vs classique « فعل الشّرط /
  أداة جازمة ») avant d'écrire.
