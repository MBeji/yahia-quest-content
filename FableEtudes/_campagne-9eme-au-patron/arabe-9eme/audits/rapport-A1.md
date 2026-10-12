# Rapport d'audit A1 — arabe 9ᵉ (`content/arabic/`) : 15, 04, 16, 17

Auditeur indépendant (aucun de ces chapitres écrit par moi). Corpus : `/home/user/yahia-quest-content`,
branche `wip/arabe-9eme-patron` (HEAD `5ac7dfc9`). Sauvegarde de l'état initial :
`…/ar9/audit/A1/backup/`.

Sources lues en entier avant l'audit : mandat `audit-A1.md`, `b-common.md`, `b-new.md`, briefs N15/B04/N16/N17 ;
notes `L3, L9, L15, L23, L29, L36, L40, L47, L54, L65, L72, L77, L83` ; `ecart-1.md`, `ecart-2.md` ;
`lecture-n/ecart-n.md`, `plan.md` (+ passages utiles d'`appareil.md`) ; fiche `9eme-base/arabe.md` §2 ter, §4, §6 ;
référentiels `content-audit/SKILL.md`, `course-explanation.md`, `course-quality.md`, `language-track.md`,
`quality-bar.md`, `math-and-notation.md`, `correction-cle-longue.md`.

(Rapport écrit au fil de l'eau, chapitre après chapitre.)

## Contrôles de départ (avant toute correction)

`content:check` vert (arabic : 19 chapitres, 562 questions) ; `content:qa` : 0 constat sur 15, 04, 16, 17 ;
`content:tranche --chapters 15,04,16,17` : clé strictement la plus longue 0/140, positions a 33 · b 36 · c 37 · d 34,
0 paire proche (contre toute la matière), 0 gabarit ; Prettier `--check` vert sur les `.json`.

---

## Chapitre 15 — `15-al-alaqat-bayna-al-jumal` (L3, L9, L15, L23)

**Questions re-résolues : 35/35** (quiz 5 + 5 × 6), à l'aveugle puis confrontées à la clé : **35 clés justes, aucune
ambiguïté bloquante.** Explications conformes à la clé, aucun renvoi positionnel, pas de `**`.

### Erreurs corrigées (cours.md)

1. § « أمّا وإذا وإذن وأي », `::: exemple`, pas 2 : « …تعرضُ مشهدًا مفاجئًا، ويصحُّ «فإذْ». » → « …ويصحُّ «إذْ». »
   — « فإذْ » n'est pas une forme de la فجئيّة (la خلاصة p.19 donne إذ، إذا، وإذا، فإذا ; le مدخل VI fait remplacer
   إذا/وإذا par « إذْ » ; « فإذْ » est, dans l'usage, causal). Le `::: verifie` de la même section et l'item
   03-revision Q4 disaient déjà « إذْ ».
2. § « حروف الجمع », 2ᵉ `::: piege` : « «انقطعَ التّيّارُ، ثمّ غرقَ الحيُّ في الظّلامِ» تُفهمُ فيها الجملتانِ حدثَينِ
   متباعدَينِ **لا صلةَ بينَهما** » → « تُفهمُ فيها **مهلةٌ بينَ الحدثَينِ ولا تقولُ إنّ الأوّلَ سببُ الثّاني** » — « ثمّ »
   relie (الجمع مع التّرتيب والتّراخي, خلاصة 5 p.12 et la définition du cours lui-même) : dire qu'elle pose deux
   faits « sans lien » contredisait la règle enseignée trois blocs plus haut.

### Remarques (non corrigées)

- **Fidélité** : les خلاصات L3 (5 points), L9 (5), L15 (6), L23 (3) sont toutes servies, dans le métalangage du
  manuel (حرف استئناف / عطف, الجمع بدون ترتيب, جمع المستبعد, التّراخي, الفجئيّة, طلب التّعيين, جملة مختزلة,
  المحلّ الشّاغر, الصّيغة المنجزة). إذ = فجئيّة seulement ✓ ; إغراء / تحذير absents des items, nommés une fois dans
  « 🚀 للتوسّع » ✓ ; la phrase à ناسخ reste اسميّة ✓ (cohérent avec `01` §« الجملة الاسمية والجملة الفعلية » :
  « تبقى اسمية إذا دخل عليها ناسخ »). Aucune coquille du manuel reprise.
- **« أمّا » — قالب** : le cours (définition, retenir, piège, résumé, explications 03-revision Q3 et 04-defi Q4) pose
  « أمّا + المبتدأ + فـ + الخبر » comme LE moule. C'est le moule du guide 501902 (p.22, « أمّا (محلّ مبتدأ) فـ(محلّ
  خبر) »), donc pas une faute de source ; mais le manuel révisé fait travailler « فأمّا اليتيمَ فلا تقهرْ » (تمرين 2
  p.20, اليتيمَ n'est pas مبتدأ) et « أمّا بعدُ فـ… » (تطبيق 5). Suggestion : « وأكثرُ قوالبِها… ». Aucun item n'est
  faux pour autant (tous les items en أمّا ont un مبتدأ).
- **« 🚀 للتوسّع »** : « قد تدخلُ الباءُ زائدةً للتّأكيدِ على الخبرِ بعدَ «إذا» الفجئيّةِ: «فإذا هو بشيخٍ يقتربُ» » —
  le guide (ملاحظة p.23) dit « المبتدأ أو الخبر » ; l'exemple canonique porte la باء sur le premier nom
  (« كنّا نتجوّل إذا برجلٍ عليه نور ») ; « فإذا هو بشيخٍ » se lit plutôt « هو مُفاجَأٌ بشيخٍ » (باء non زائدة). Sans
  item ; à reformuler si l'on retouche l'encadré.
- **Patron** : 9 sections, toutes T1 (situation + question) → definition → tableau → exemple → piège → propriete/methode
  avec cas-limite → verifie (1 ou 2) → retenir ; résumé en miroir (9 puces). Six pas d'exemple n'écrivent pas
  « لأنّ » (le raisonnement y est) : l.169 (§ استئناف/عطف, pas 2), l.310 (§ أو/إمّا/أم, pas 4), l.538–540 (§ الحذف,
  pas 2–4), l.603 (§ الحذف في الفعليّة والاسميّة, pas 1).
- **Items** : distracteurs = vraies confusions (rang lu sur la forme, حال/مفعول فيه pris pour اعتراض, حتّى de غاية,
  ثمّ pour la cause, استدراك sur un attendu, élément restant pris pour le محذوف). Deux distracteurs faibles :
  05-entrainement Q3 d (« خبرٌ للفاعلِ «الحاجُّ» » — un فاعل n'a pas de خبر) et c (« مفعولٌ فيه… »). 02-boss Q5 d
  (« حرفُ عطفٍ يفيدُ طلبَ تعيينِ… ») est le nom classique de « أم المتّصلة » : faux selon le critère du manuel
  (le cours l'enseigne : ce que relie le حرف le nomme ; خلاصة 4 p.19 « ورد الثّاني في جملة استئنافيّة ») ; à garder en
  tête si un élève formé à la grammaire classique conteste. 03-revision Q6 : l'explication dit « لا فعلٌ تامٌّ »
  (ناقص/تامّ n'est enseigné qu'au chapitre 02, plus loin dans l'ordre) — mineur. 02-boss Q1 : l'explication nomme
  « الجارّ والمجرور » (forme) là où la méthode demande la fonction — mineur.
- **Titres** : 01-pratique « …ورتبتُها وأوّلُ أدواتِ الرّبطِ » ne dit pas sa Q6 (الجملة المختزلة) — mineur.
- Métadonnées identiques à la maquette 13 ; clés a/b/c/d réparties ; rampe non décroissante (03-revision : d3 en
  fin d'un exercice ⭐⭐, comme la maquette).

**Verdict : conforme après corrections. Clarté : 4/5** (cours précis et très bien construit ; sections longues — 7 sur
9 entre 46 et 57 lignes non vides — et denses pour un élève de 14 ans).

---

## Chapitre 04 — `04-al-asalib` (L29, L36, L40)

**Questions re-résolues : 35/35** (quiz 5 + 5 × 6 : 01, 02, 04, 05, 06) : **35 clés justes.** Aucun distracteur
« منصوب / النّصب » défendable par « في محلّ نصب » : les seuls « نصب » proposés pour un منادى le sont sur des formes
visiblement fautives (« يا حارسُ البستانِ », « يا أيُّها المسافرَ ») ou sous la question « أيّ المنادَيات يُنصَب؟ »
(quiz Q2) dont le verbe est celui de la خلاصة p.33 (« ينصب المنادى إذا كان مركّبا إضافيّا »).

### Erreur corrigée

1. `quiz.json` Q5 (معنى سياقيّ du أمر, clé « الالتماس ») — **deux réponses défendables** : « قال تلميذ **لأستاذه**:
   «أَعِدْ شَرْحَ الدَّرْسِ مِنْ فَضْلِكَ» » ; selon la rhétorique classique (enseignée au lycée et dans la plupart des
   références), un أمر « من الأدنى إلى الأعلى » est un **دعاء** — distracteur présent. Correction minimale :
   « لأستاذه » → « **لزميله** » dans l'énoncé, et dans l'explication « يطلب من أستاذه » → « يطلب من زميله », « لا إلى
   الأستاذ » → « لا إلى الزّميل ». Entre pairs, « الالتماس » est la seule lecture, dans le cadre du manuel (الدّعاء =
   طلب من الله, خلاصة p.38 ; الالتماس = « طلب بليّن وتحبّب », guide p.98) comme dans le cadre classique.

### Remarques (non corrigées)

- **Fidélité** : خلاصات L29 (définition, 5 أدوات avec قرب/بعد « حسّا أو معنى », مفرد / تركيب جزئيّ بالإضافة · بالنّعت ·
  بالوصل, **حكم المنادى الرّفع** pour علم مفرد · نكرة مقصودة · معرّف بأل (أيّها/أيّتها), النّصب pour مركّب إضافيّ ·
  نكرة موصوفة غير مقصودة, الاستغاثة et النّدبة comme معانٍ du نداء « في بعض المقامات »), L36 (définition, له / عليه,
  تامّة مثبتة/منفيّة, فعليّة مختزلة) et L40 (définitions, 4 صيغ du أمر dont « بعض العبارات », صيغة وحيدة du نهي ± نون
  التّوكيد, 9 معانٍ سياقيّة) toutes servies. « أ » ajoutée, « آ » retirée, l'interrogation partie au 16 ;
  « مبنيّ على الضّمّ في محلّ نصب », « شبيه بالمضاف », التّعجّب/المدح والذّمّ/الإغراء/التّحذير/الاختصاص seulement
  dans « 🚀 للتوسّع », sans item ✓. Aucune coquille reprise (« VI » pour IV, « المتّكلم »…).
- **Doctrine du الالتماس dans le cours** : la `::: methode` du § « معاني الأمر والنّهي » dit « متساويان **أو أدنى
  يطلب من الأعلى بتلطّف** (التماس) » — cohérent avec le manuel (الدّعاء ne s'adresse qu'à Dieu) mais contraire à la
  règle classique (أدنى → أعلى = دعاء). À garder en tête ; plus aucun item ne repose sur ce cas.
- **Cohérence 04 ↔ 15 (le حذف)** : « جملة فعليّة مختزلة » du دعاء = un des types de 15 (« حذف الفعل والفاعل ») ; même
  règle « ما بقي يُنطق كما كان ». Petite imprécision : l'exemple « رَزَقَكُمُ اللهُ نَجَاحًا بَاهِرًا ← نَجَاحًا بَاهِرًا »
  fait aussi tomber le premier objet « كم » (l'exemple et le `verifie` le disent, la définition, la propriété, le
  retenir et le résumé ne disent que « الفعل والفاعل ») — pas faux, incomplet. « جملة إسناديّة تامّة » est glosée
  « ففيها فعل وفاعل » : une دعاء nominale (« السّلامُ عليكم ») n'y entre pas — mineur.
- **Indices de forme (MAJOR de qualité, clé juste)** : 01-pratique Q2 (« ما نوع الدّعاء في «رَحِمَ اللهُ وَالِدَكَ»؟ ») —
  deux options (« أمر بالقيام بفعل », « نداء لتنبيه المخاطَب ») nient la prémisse de l'énoncé (c'est un دعاء) : choix
  réduit à له / عليه. 05-tadrib Q3 (« ما ركنا جملة النّدبة… ») — l'énoncé nomme la ندبة, deux options commencent par
  « حرف نداء للاستغاثة ». À réécrire en lot qualité (« ما العمل اللّغويّ وما نوعه؟ » ou des distracteurs du même
  champ).
- **Patron** : 12 sections (seuil R-13 dépassé, déjà signalé fiche §6 : scission naturelle النّداء / الدّعاء + الأمر
  والنّهي), toutes au patron complet ; « لأنّ » manque aux pas l.428, l.431 (§ أبنية الدّعاء) et l.482 (§ الأمر
  والنّهي) ; deux `propriete` sans cas-limite explicite (§ النّداء, § الأمر والنّهي). Résumé : 12 puces ✓.
- **Titres / métadonnées hérités** (non touchés, hors mandat) : quiz « اختبار فهم الدرس » et trois exercices sans
  indicateur ⭐ ; 04-defi « دقائق الأساليب **وإعرابها** » alors que le chapitre ne teste plus d'إعراب ; numérotation
  01, 02, 04, 05, 06 (pas de 03).

**Verdict : conforme après correction. Clarté : 4/5** (registre simple, exemples de la vie de l'élève ; douze sections
font un chapitre long).

---

## Chapitre 16 — `16-al-istifham` (L47, L54, L65)

**Questions re-résolues : 35/35** : **35 clés justes.** Doctrine نعم / بلى du manuel (خلاصة p.50 : « ألم تفعل ؟ — نعم
(لم أفعل) = إثبات النّفي ; بلى (فعلت) = إبطال النّفي ») tenue partout, sans aucun distracteur « لا، لم أفعل » après
une question négative (le seul cas où l'usage courant contesterait).

### Erreurs corrigées

1. `exercices/05-entrainement.json` Q5 — **distracteur défendable** : « ما الذي يفيد التسوية في «سَوَاءٌ عَلَيْنَا
   أَنَجَحْتَ أَمْ رَسَبْتَ»؟ » (clé « الاسم «سَوَاءٌ» », distracteur « الهمزة «أَ» »). La grammaire classique nomme
   précisément cette hamza « همزة التّسوية » : un élève ou un correcteur formé à elle peut défendre l'option. Énoncé
   → « ما الذي **يدلّ بمعناه على** التسوية في … ؟ » : seul « سواء » porte l'égalité par son sens (خلاصة p.61 :
   « ويستفاد ذلك من أفعال أو أسماء… (يستوي، سيّان، سواء…) »), la hamza et « أم » étant des pièces du tour. Options,
   clé et explication inchangées (l'explication disait déjà « لا تفيدان التسوية وحدهما »).
2. `cours.md`, encadré « 🚀 للتوسّع » : « تسمّي كتب البلاغة الاستفهام **بـ«هل» أو الهمزة** طلبَ «التصديق»، والاستفهام
   **بأسماء الاستفهام** طلبَ «التصوّر» أو «التعيين» » → « …الاستفهام **عن مضمون الجملة** طلبَ «التصديق»، والاستفهام
   **عن عنصر منها (باسم استفهام، أو بالهمزة مع «أم»)** طلبَ «التصوّر» أو «التعيين» ». La phrase rangeait la hamza
   dans le seul تصديق : faux en rhétorique (« أزيدٌ عندك أم عمرو؟ » = تصوّر), contraire au guide (p.60 : « الهمزة …
   كما يُطلب به تعيين عنصر ») et au chapitre 15 (« أم » = طلب التّعيين après la hamza).

3. `exercices/04-defi.json` Q3 (fonction de « كيف ») — **renvoi positionnel** dans l'explication : « …فتكون «كيف»
   حالًا **في الثاني** وخبرًا **في الأخيرين**. » (les options sont mélangées à l'affichage) → « …حالًا **مع «مسرعًا»**
   وخبرًا **مع «متعب» و«نشيطًا»**. » (trouvé à la reprise, par un balayage des ordinaux dans les quatre chapitres ; les
   autres « الأولى / الثّانية » des explications désignent des phrases de l'énoncé, ce qui est permis).

### Remarques (non corrigées)

- **Fidélité** : L47 (عمل لغويّ مستخبر, أ / هل, صدارة et rang vis-à-vis du حرف استئناف « أَوَ / وَهَلْ » — construit au
  مدخل II —, مثبتة / منفيّة : استخبار / تذكير بمعلوم / استخبار عن متوقّع, نعم · إي · لا · بلى), L54 (7 أسماء, محلّ
  إعرابيّ lu par le جواب, كيف خبر/حال/مفعول مطلق, أين/متى خبر/مفعول فيه, عدم اليقين par درى/علم/عرف/رأى منفيّة,
  عجب/حار/احتار, تُرى ; التّسوية سيّان/سواء/يستوي + همزة + أم/أو) et L65 (مركّب الجرّ en صدارة, متمّمات du فعل,
  valeurs مفعوليّة / سببيّة / ظرفيّة / ابتداء وانتهاء الغاية / حاليّة, خبر مقدّم dans la phrase sans verbe) toutes
  servies dans le métalangage du manuel. Coquilles évitées : « أيّ » معربة (écart voulu, brief), aucune phrase
  nominale dite فعليّة, « حار » sans chadda, تصديق/تصوّر seulement en note. « ما / كيف + معرفة = خبر » appliqué
  (« ما لونُ الحقيبة؟ », « كيف أخوك؟ », « كيف الحصانُ…؟ »). La chute de l'alif (لِمَ، بِمَ، فيمَ، عمَّ…) n'est donnée
  qu'en « للتوسّع » (le manuel la pratique sans l'énoncer) ; aucun item ne la teste ✓.
- **Exemple discutable** (§ المثبتة والمنفيّة, `::: exemple`) : « أَلَمْ تُرَتِّبْ حَقِيبَتَكَ؟ » dit par une mère qui
  VOIT la valise ouverte est classé « تذكير بشيء معلوم ». Par élimination c'est juste (elle connaît la réponse), mais le
  « معلوم » y est négatif et le tour se lit comme un reproche ; le prototype du manuel (« أَلَمْ نُطْعِمْكَ؟ » — بلى) rappelle
  un fait POSITIF, comme le T1 du cours (« أَلَمْ أُنَبِّهْكَ…؟ ») et l'item 01-pratique Q4. Suggestion : prendre un fait
  positif.
- **Règle trop large** (§ وظيفة اسم الاستفهام, `propriete`) : « إذا جاء بعد «مَن» أو «ما» فعل لا فاعل ظاهر له فالاسم
  مبتدأ » — contre-exemple « ما يقولُ؟ » (فاعل مستتر renvoyant à un tiers : « ما » مفعول به). Aucun item ne bute dessus.
- **Usage** : quiz Q2 garde « نَعَمْ، كَتَبْتُهُ » comme distracteur — erreur au regard du manuel et de la tradition
  dominante (une minorité admet نعم pour confirmer après un تقرير, et l'usage courant la dit) ; la clé « بَلَى،
  كَتَبْتُهُ » reste la seule conforme, l'item est sain.
- **Distracteurs faibles** : 05-entrainement Q1 (« «طَرِيقٍ» », « «نَسْلُكُ» » pour « ce qui exprime l'incertitude »)
  s'éliminent à vue.
- **Patron** : 9 sections complètes et dans l'ordre, cas-limite partout, résumé 9 puces ✓ ; « لأنّ » absent de dix pas
  d'exemple (l.32, 86–87, 141, 200, 364, 419, 421, 477–478) — le raisonnement y est.
- Métadonnées conformes à la maquette 13 ; titres cohérents avec les contenus.

**Verdict : conforme après corrections. Clarté : 4/5** (le plus lisible des quatre : situations proches de l'élève,
tableaux qui « montrent » la fonction par le جواب ; quelques consignes longues).

---

## Chapitre 17 — `17-ash-shart` (L72, L77, L83)

**Questions re-résolues : 35/35.** 33 clés justes d'emblée ; **2 items fautifs** (02-boss Q4 et 04-defi Q2), tous deux
bâtis sur le même contresens que le cours : un « اسم شرط » placé **après un verbe**. Le manuel l'exclut en toutes
lettres (خلاصة p.80 : « لا يقع اسم الشّرط بعد فعل أو حرف ناسخ ») et par ses exemples (مدخل I p.77 : « يَرْبَحُ مَنْ
حَاسَبَ نفسَه », « أَكْتُبُ ما تكتبُ » = موصولة, opposées à « مَنْ يُحاسبْ نفسَه يربحْ », « ما تكتبْ أكتبْ ») ; en grammaire
classique aussi, un اسم شرط garde la صدارة et ne peut être régi par le verbe qui le précède. Vérifié sur l'image des
pages 73, 77 et 80.

### Erreurs corrigées

1. `cours.md` § « اسمُ شرطٍ أم اسمٌ موصولٌ » — la définition glosait « لا يقعُ بعد فعلٍ أو حرفٍ ناسخٍ **(كانَ وأخواتِها،
   إنّ وأخواتِها)** », réduisant « فعل » aux نواسخ, et le tableau posait « **ينجحُ مَنْ يَجتهِدْ في دروسِهِ** — إمكانٌ —
   اسمُ شرطٍ — الأوّلُ مرفوعٌ لأنّه تقدّمَ، والواردُ بعد «مَنْ» مجزومٌ ». Corrigé : glose → « (مثل «ينجحُ» أو «كانَ») …
   (مثل «إنّ») » ; seconde définition « بعد ناسخٍ » → « بعد فعلٍ أو ناسخٍ » ; tableau ramené à trois lignes justes
   (« مَنْ يَجتهِدْ في دروسِهِ يَنجَحْ » اسم شرط في الصّدارة / « ينجحُ مَنْ يَجتهِدُ في دروسِهِ » اسم موصول بعد فعل / « إنّ مَنْ
   يَجتهِدُ ينجحُ » بعد ناسخ) et phrase-pont réécrite ; `retenir` et `resume.md` « لا بعد ناسخٍ » → « لا بعد فعلٍ أو
   ناسخٍ ».
2. `exercices/02-boss.json` Q4 — énoncé « ما الفرقُ في المعنى بين «يُكرِمُ المعلّمُ مَنْ يَجتهِدُ…» و«**يُكرِمُ المعلّمُ
   مَنْ يَجتهِدْ في دروسِهِ**»؟ » : la seconde phrase est agrammaticale selon le manuel. → « …و«**مَنْ يَجتهِدْ في دروسِهِ
   يُكرِمْهُ المعلّمُ**»؟ » ; options et clé (b) inchangées ; explication réécrite (« وقعتْ «مَنْ» بعد فعلٍ فهي اسمٌ موصولٌ…
   تتصدّرُ «مَنْ» الجملةَ فهي اسمُ شرطٍ… فموضعُ «مَنْ» وحركةُ آخرِ الفعلِ هما اللّذانِ يغيّرانِ المعنى »).
3. `exercices/04-defi.json` Q2 — « أيُّ الجملِ الآتيةِ صحيحةٌ وفيها «مَنْ» اسمُ شرطٍ؟ » : clé a « **يَتعَبُ مَنْ يَسهَرْ
   ليلًا** » fausse (اسم شرط après un verbe) et **aucune option juste**. Option a → « **مَنْ يَسهَرْ ليلًا يَتعَبْ** » (clé
   inchangée) ; explication réécrite. Item désormais parallèle au quiz Q4 (même savoir-faire, autres mots, plus le
   critère de validité porté par « إنّ مَنْ يَسهَرْ… يَتعَبْ ») — parallèle voulu, à enrichir plus tard d'un tour d'élite
   (اسم شرط مجرور, « على مَنْ … »).
4. `cours.md` § « حرف الشّرط «إنْ» » et `resume.md` — le cours enseignait, et faisait produire dans son `verifie`, le
   جواب avancé suivi de « إنْ » + **مضارع مجزوم** : « تنجحُ إنْ تُراجعْ دروسَكَ », « ينجحُ أخي إنْ يجتهدْ ». Le manuel ne
   l'avance qu'avec un ماضٍ (p.73 : « يَقتُلُني بمعصيةٍ إنْ عَصَيْتُه », « هل يقتلُني الأميرُ إنْ عَصَيْتُهُ ؟ ») et la grammaire
   classique réserve le مضارع à la poésie quand le جواب est tu. → « تنجحُ إنْ **راجعتَ** دروسَكَ » (pas 4 de l'exemple,
   propriété, piège), « ينجحُ أخي **إنِ اجتهدَ** » (verifie), avec « والأفصحُ حينئذٍ أنْ يليَ «إنْ» فعلٌ ماضٍ » ; résumé
   aligné. Les règles énoncées (مضارع مجزوم après « إنْ », جواب avancé non jussif) restent exactes.
5. **Métalangage** (cohérence avec le 15, L9 خلاصة 1 : un حرف qui relie deux phrases est un حرف استئناف) : quiz Q1,
   option a « …ويربطَ بينهما **بحرفِ العطفِ** الفاءِ » → « **بحرفِ الاستئنافِ** الفاءِ », et explication « يربطُ بينهما
   **حرفُ العطفِ** » → « **حرفُ الاستئنافِ** » ; 05-entrainement Q2, explication « و«ثمّ» **حرفُ عطفٍ** لا يقومُ مقامَ فاءِ
   الرّبطِ » → « و«ثمّ» **تفيدُ التّرتيبَ والتّراخيَ** ولا تقومُ مقامَ فاءِ الرّبطِ ».

### Remarques (non corrigées)

- **Fidélité** : L72 (تعليق حدث بحدث, رئيسيّ / ثانويّ, حرفا الشّرط, « مركّب حرفيّ » = « مفعول الشّرط », « جواب الشّرط »
  « المسمّى عادة », إنْ = deux ممكنان, لو = غير متحقّق في الماضي + ممتنع لامتناعه, ماضٍ مثبت ou لم + مضارع, لام du
  جواب, فاء الرّبط « عند الحاجة »), L77 (10 أسماء et leurs sens, صدارة, « مركّب موصوليّ » et sa fonction, مهما / كيفما
  حال, ظروف مفعول فيه, جزم sauf après إذا, pas de جزم du مضارع avancé, اسم شرط مجرور « بمَنْ تَثِقْ أَثِقْ ») et L83
  (افتراض الممكن passé / futur, متى, افتراض الممتنع, استنتاج par إنْ / إذا, قرائن) tous servis. Coquilles évitées
  (« لامتناع », pas de لولا) ; « فعل الشّرط / أداة جازمة » seulement en « للتوسّع » ✓.
- **Vigilance مهما / متى / أينما** : aucun item ne demande la fonction de « مهما » (حال pour le manuel, مفعول به ou
  مبتدأ pour la tradition — la note « للتوسّع » le dit) ; « متى », « أينما », « حيثما » = ظرفيّة / مفعول فيه, conformes.
  03-revision Q5 (« كيفما يَصِلُ أخي نَفرَحُ » distracteur) est faux dans les deux cadres (manuel : جزم ; tradition :
  verbes identiques exigés).
- **Règle de fonction trop étroite** (§ وظيفة اسم الشّرط) : « مع «مَنْ، ما، أيّ»: مفعولٌ به إنْ نقصَ الرّئيسيَّ مفعولٌ،
  وإلّا فمبتدأٌ » échoue sur « أيَّ خروجٍ تخرجْ أخرجْ » (manuel p.77 : مفعول مطلق) et laisse « أيَّ كتابٍ تَقرَأْ تَستفِدْ »
  (exemple du § أسماء الشّرط), dont « أيَّ » est visiblement منصوب, classé مبتدأ. La définition cite aussi « فاعل »
  (liste du manuel) qu'aucun cas à صدارة ne peut produire. Aucun item n'en dépend.
- 04-defi Q5 (« ce qui fixe le temps de «إنْ» » → « السّياق ») : juste, mais l'exemple passé du manuel porte un indice
  formel, « فإنْ **كانَ** بقيَ… » ; le cours pourrait le nommer.
- § « أُوظّفُ », pas 1 : « …لأنّ السّهرَ ممكنٌ **ولم يتحقّقْ بعدُ** » alors que le frère « يسهرُ » déjà — mineur.
- **Patron** : 11 sections au patron complet + « للتوسّع » ; « لأنّ » absent d'une vingtaine de pas d'exemple (l.32,
  139–140, 194, 255–258, 381–383, 440, 497–498, 550–551) ; titre en « 🔗 » (le gabarit dit « ⚔️ ») ; « للتوسّع » en
  section `##` placée avant le « 🏆 » final (ailleurs, après) — mineurs. Résumé : 11 puces en miroir ✓.
- Métadonnées conformes à la maquette 13 ; clés 9 / 9 / 9 / 8.

**Verdict : conforme après corrections. Clarté : 4/5** (progression sémantique très claire — وجوب / إمكان / امتناع /
استنتاج —, scènes familières ; quelques blocs denses en métalangage du manuel).

---

## Synthèse

| Chapitre | Questions re-résolues | Défauts d'items trouvés | Corrections faites | Verdict | Clarté |
| --- | --- | --- | --- | --- | --- |
| 15 العلاقات بين الجمل | 35 | 0 | 2 (cours) | conforme après corrections | 4/5 |
| 04 النّداء والدّعاء والأمر والنّهي | 35 | 1 item à deux réponses (quiz Q5) | 1 | conforme après correction | 4/5 |
| 16 الاستفهام | 35 | 1 distracteur défendable, 1 renvoi positionnel | 3 | conforme après corrections | 4/5 |
| 17 الشّرط | 35 | 2 items fautifs (02-boss Q4, 04-defi Q2) | 5 groupes | conforme après corrections | 4/5 |

**140 questions re-résolues ; 11 fichiers modifiés** (15 cours ; 04 quiz ; 16 cours, 04-defi, 05-entrainement ; 17 cours,
résumé, quiz, 02-boss, 04-defi, 05-entrainement). Aucun nombre de questions, aucun `id`, aucune clé, aucune
métadonnée changés. Aucune écriture git. Ni 09 ni `11-annales-subur` touchés.

**Contrôles finaux** (depuis le moteur) : `content:check` vert (arabic 19 chapitres / 562 questions) ; `content:qa` :
0 constat sur 15, 04, 16, 17 ; `content:tranche --chapters 15,04,16,17` : clé strictement la plus longue 0/140, clés
a 33 · b 36 · c 37 · d 34, 0 paire proche, 0 gabarit ; Prettier `--check` vert sur les `.json` (aucun `--write`
nécessaire ; les `.md` non passés à Prettier).

**Cohérence entre chapitres** : 15 ↔ 01 (phrase à ناسخ = اسميّة) ✓ ; 04 ↔ 15 (جملة فعليّة مختزلة, « ما بقي يُنطق كما
كان ») ✓ ; 16 ↔ 15 (« أم » = طلب التّعيين après la hamza : rétabli dans la note du 16) ✓ ; 17 ↔ 15 (حرف استئناف entre
deux phrases : rétabli au 17) ✓.

**À arbitrer par l'orchestrateur ou le propriétaire** (rien de faux, mais à décider) : la doctrine du الالتماس dans la
`methode` du 04 (« أدنى يطلب من الأعلى » = التماس) ; l'exemple « ألم ترتّب حقيبتك؟ » du 16 ; la règle de fonction
de « أيّ » au 17 ; le moule « أمّا + مبتدأ + فـ + خبر » posé comme unique au 15 ; les items à indices de forme du 04
(01-pratique Q2, 05-tadrib Q3).
