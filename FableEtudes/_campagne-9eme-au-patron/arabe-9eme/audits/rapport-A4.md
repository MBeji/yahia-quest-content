# Rapport d'audit A4 — arabe 9ᵉ, chapitres 09, 10, 07, 08 (auditeur indépendant)

Date : 2026-10-12. Corpus `/home/user/yahia-quest-content/content/arabic/`. Sources qui font foi :
101909 (notes `lecture-n/plan.md`, `appareil.md`, `ecart-n.md` + pages en image au besoin),
101908 (notes `lecture/L*.md`), fiche `programme/9eme-base/arabe.md` (§2 ter, §4, §6).

Rapport écrit au fil de l'eau, un chapitre après l'autre.

## Contrôles initiaux (avant toute correction)

- `content:check` : vert (120 matières, 0 erreur).
- `content:qa | grep arabic/(09|10|07|08)-` : **aucune ligne** (0 erreur, 0 avertissement sur les 4 chapitres).
- `content:tranche --chapters 09,10,07,08` : 147 questions, clé strictement la plus longue **0/147**, clés a 35 · b 38 · c 38 · d 36, 0 paire proche.
- `prettier --check` sur les `.json` des 4 chapitres : conforme.
- Scan maison : 0 chiffre indo-arabe, 0 `**` dans prompt/option/explication, 0 nombre coupé ; renvois « الأولى » à vérifier dans 08 (cf. §08).

## 09-al-intaj-al-kitabi — الحجاج: الأطروحة والحجج وسيرورة الحجاج

**Questions re-résolues : 34/34** (quiz 5, 01-pratique 6, 02-boss 5, 04-defi 6, 05-tadrib 6, 06-defi-concours 6).
Toutes les clés sont justes et uniques ; aucun distracteur défendable trouvé, y compris sur les paires
qui se touchent : حجّة / مثال (quiz Q3, 01 Q2), سلطة / واقعيّة (quiz Q4, 01 Q4, 06 Q2), استقراء /
استنباط / قياس (04 Q4), تفسير / تعليل (04 Q5, 06 Q2), ثلاثيّة / منقوصة (06 Q4 : aucune option « نصّ
الأطروحتين » n'y crée de double réponse), « نوع النصّ بحسب الأطروحة » (02 Q2 : les options « وحدها »
rendent la clé unique).

**Fidélité 101909** (vérifiée contre `appareil.md` §4, et p. 142 décodée pour القياس) :
- vocabulaire exact : الأطروحة المثبتة (المدعومة) / المدحوضة (المقابلة) — jamais « المعارضة » ; طرفا
  الحجاج p. 13 ; سيرورة الحجاج et إستراتيجيّة الحجاج p. 12 ; البنية ثلاثيّة / منقوصة (« الركن الغائب ») /
  نصوص الأطروحتين p. 63 ; الإقناع / التأثير p. 12, 141 ; sept familles d'مؤشّرات p. 13 ; cinq صيغ
  تعبيريّة p. 189 ; canevas p. 313–314 (حوار مؤطّر سرديًّا ; دحض + أطروحة بديلة) ; encadrés تذكّر / اعلم
  p. 315 (موضوع حياتيّ / أدبيّ) ; وحدة تشخيصيّة p. 6–8 (وضع البداية، الحدث القادح، سياق التحوّل، وضع الختام ;
  وظائف الوصف).
- types de حجج conformes à p. 12 ; le شاهد rangé sous السلطة ; القياس défini « استنتاج نتيجة من
  مقدّمتين » avec l'exemple de Socrate — c'est exactement la glose imprimée p. 142 (أرسطو), et p. 143 fait
  classer une « حجّة القياس » : fidèle.
- coquille p. 13 « خلاصة صفوة القول » non reprise (deux expressions séparées). Hors-manuel (نصّ تفسيريّ /
  إيعازيّ) relégué en « 🚀 للتوسّع », sans item (vérifié : aucun item n'y touche).
- écart 101908 ↔ 101909 sur « إذْ » et « حتّى » : signalé dans la note sous le tableau de la section
  « المؤشّرات (1) » ; aucun item ne repose sur ces deux emplois. Cohérent avec le ch. 15 (الاستدراك défini
  mot pour mot comme au ch. 15 ; « إذْ » فجئيّة suivie de مبتدأ وخبر comme au ch. 15).

**Erreur corrigée (1)** :
- `cours.md`, section « الإنتاج (2): دحض أطروحة… », `::: exemple`, pas 3 : la حجّة « لن ينجحَ من حفظَ ولم
  يفهمْ إذا جاءه سؤالُ تطبيقٍ » était étiquetée **(واقعيّةٌ)** alors qu'elle n'expose ni واقعة, ni مشاهدة,
  ni تجربة (définition p. 12 et « أسئلة الكشف » du cours lui-même) : c'est un raisonnement général.
  `(واقعيّةٌ)` → `(عقليّةٌ)`.

**Remarques (non corrigées)** :
1. [MINOR] Note sous le tableau « المؤشّرات (1) » : « «إذْ» الفجئيّة التي يليها مبتدأٌ وخبرٌ **بعدَ
   حدثٍ مفاجئٍ** » — la formule place le حدث مفاجئ avant « إذْ » ; mieux : « …التي تُدخِلُ حدثًا مفاجئًا،
   ويليها مبتدأٌ وخبرٌ ».
2. [MINOR] Tension non explicitée entre « المثال = واقعة ملموسة بعينها » (méthode des trois questions) et
   « الحجّة الواقعيّة = وقائع ومشاهدات وتجارب شخصيّة » (types) : le cours ne dit nulle part qu'une واقعة
   est **مثال** quand elle illustre une حجّة déjà énoncée et **حجّة واقعيّة** quand elle sert seule de
   preuve à la أطروحة (ce que font, correctement, quiz Q3 et 01 Q4). Une phrase dans le `propriete` des
   types lèverait l'ambiguïté (les items, eux, sont univoques).
3. [MINOR] استنباط / قياس : la définition du استنباط (« من حكم عامّ إلى حالة خاصّة ») couvre aussi le
   syllogisme ; seul le critère « مقدّمتان + نتيجة » sépare le قياس. Aucun item n'oppose استنباط et
   قياس comme seules options défendables (04 Q4 porte sur le استقراء) — à garder ainsi.
4. [MINOR] « البنية » : le cours range « نصّ الأطروحتين » comme 3ᵉ type de structure tout en disant
   (exemple de la section) qu'un texte peut être à la fois ثلاثيّ et « نصّ أطروحتين » ; p. 63 range les
   الأطروحتان dans la classification « حسب بنيتها » et مدحوضة / مدعومة dans celle « حسب نوع الأطروحة ».
   Sans conséquence sur les items actuels (aucun ne met « ثلاثيّة » et « نصّ الأطروحتين » en concurrence).
5. [MINOR] Patron : 14 sections, toutes aux sept temps dans l'ordre (ancrage + question, `definition`,
   tableau + phrase-pont, `exemple`, `piege`, `propriete`/`methode` avec حالة حدّيّة, `verifie`,
   `retenir`) ; mais une vingtaine de pas d'exemples donnent leur raison par « ← » sans le mot « لأنّ »
   (ex. سيرورة pas 2–3, البنية pas 1–3, الإقناع pas 1–2, الإنتاج 1 pas 2, 3, 5). 14 notions > 8 : la
   scission « cours du حجاج / production » déjà signalée par la fiche §6 reste une décision humaine.
6. [MINOR] Exemple de la section « البنية » : « (3) و(4) و(5) ثلاثُ حججٍ في (4) منها مثالٌ » est
   ambigu (la (4) est-elle une حجّة qui contient un مثال, ou un مثال ?).
7. [MINOR] Titre de `02-boss` « ⚔️ زعيم الفصل: الإنتاج الكتابي المتقدّم » : hérité de l'ancien chapitre ;
   4 items sur 5 portent sur l'analyse (ترتيب الحجج، نوع النصّ، التقابل، التأثير). Proposition :
   « ⚔️ زعيم الفصل: الحجاجُ تحليلًا وإنتاجًا » (métadonnée : non modifiée). `04-defi` sans ⭐.
8. [MINOR] `propriete` des صيغ تعبيريّة : « هذه الصيغ من وسائل التأثير في الغالب » n'est pas dans
   p. 189 (صيغ الوثوق et التأكيد servent autant le إقناع) ; formulation d'auteur, sans item qui en dépende.

**Langue** : arabe correct et vocalisé, registre adapté à 14–15 ans, chiffres occidentaux, aucun `**` dans
les items. **Items** : clés réparties (quiz b d a c b ; exercices équilibrés), 0 clé strictement la plus
longue, distracteurs = vraies confusions (أطروحة/حجّة/مثال/استنتاج ; miroir « ليست / إنّ » de 05 Q2 ;
reformulation vs citation pour صياغة الأطروحة), aucun renvoi positionnel, pas de quasi-doublon.

**Verdict 09 : conforme après corrections** (1 correction de cours). **Clarté : 5/5.**

## 10-fahm-wa-intaj — دراسة نصّ حجاجيّ: الفهم وبناء المعنى

**Questions re-résolues : 44/44** (quiz 8, 01-tamrin 6, 02-tamrin 6, 03-boss 6, 04-defi 6, 05-tadrib 6,
06-defi-concours 6). 42 clés justes et uniques d'emblée ; **2 items à double réponse défendable**, corrigés.

**Gestes de l'épreuve 2023–2026** — tous enseignés (une section chacun, texte court original dans le cours
ET dans chaque prompt) et tous testés : قسّم النصّ وفق بنيته الحجاجيّة (quiz Q1 ; 01 Q1, Q2, Q5, Q6 ;
05 Q1 ; 06 Q1) ; صُغ الأطروحة المثبتة / المدحوضة (quiz Q2 ; 01 Q3, Q4 ; 03 Q1 implicite ; 04 Q5, Q6 ; 06 Q2) ;
حجّة داعمة / داحضة (quiz Q4 ; 02 Q2 ; 03 Q2 ; 05 Q2 ; 06 Q3 avec la concession « صحيحٌ أنّ … غيرَ أنّ ») ;
نوع الحجّة + قرينة (quiz Q5 ; 02 Q3–Q6 ; 04 Q3 ; 05 Q4 ; 06 Q4) ; معنى المؤشّر (quiz Q6 ; 03 Q3 ; 04 Q1 ;
05 Q4) ; حجّة / مثال (quiz Q3 ; 02 Q1 ; 04 Q4) ; المفردة في سياقها (quiz Q8 ; 03 Q6 ; 04 Q2 ; 05 Q5 ; 06 Q5) ;
الإقناع / التأثير (quiz Q7 ; 03 Q4 ; 05 Q3) ; أبدي رأيي (03 Q5 ; 05 Q6 ; 06 Q6). « الفكرة العامّة » et
« النّبرة » n'apparaissent qu'une fois, dans la note d'ouverture du cours (aucun item ne les attend) ; aucune
explication ne renvoie à une option par sa lettre ou son rang.

**Erreurs corrigées (2 items + 1 phrase de cours)** :
1. `exercices/04-defi.json` Q4 (« أيُّ العباراتِ الآتيةِ حجّةٌ حقيقيّةٌ تدعمُ الأطروحةَ؟ ») — **double réponse** :
   la تجربة شخصيّة « ففي مشروعِ الفريقِ … أنجزْنا في أسبوعٍ ما كانَ يُنجزُه فردٌ في شهرٍ » venait AVANT la
   seule حجّة générale (« والسببُ أنّ الأعباءَ تتوزّعُ… ») et après une simple reprise de la أطروحة : par la
   règle du cours lui-même (« واقعةُ المشاهدةِ … حجّةٌ واقعيّةٌ إن قامتْ وحدَها دليلًا »), elle était défendable
   comme حجّة واقعيّة. Correction : ordre du texte inversé (la حجّة générale d'abord, puis l'expérience qui
   l'illustre), options et clé inchangées.
   Avant : « …أفضلُ من العملِ الفرديِّ. ففي مشروعِ الفريقِ الذي شاركتُ فيه أنجزْنا في أسبوعٍ ما كانَ يُنجزُه
   فردٌ في شهرٍ. والسببُ أنّ الأعباءَ تتوزّعُ فيُنجزُ كلٌّ ما يُتقنُه. »
   Après : « …أفضلُ من العملِ الفرديِّ. فالأعباءُ تتوزّعُ فيُنجزُ كلٌّ ما يُتقنُه. وفي مشروعِ الفريقِ الذي
   شاركتُ فيه أنجزْنا في أسبوعٍ ما كانَ يُنجزُه فردٌ في شهرٍ. » ; explication : « …واقعةٌ بعينِها فهي مثالٌ » →
   « …واقعةٌ بعينِها جاءتْ بعدَ الحجّةِ توضّحُها فهي مثالٌ ».
2. `exercices/06-defi-concours.json` Q6 (« إلى أيِّ حدٍّ وُفِّقَ الكاتبُ… حكمٌ معلَّلٌ يستندُ إلى حججِ
   النصِّ؟ ») — **double réponse** : le distracteur « وُفِّقَ؛ لأنّه نوّعَ حججَه بين قولِ لاعبٍ مشهورٍ وإحصائيّةٍ »
   appliquait correctement un critère que le cours enseigne (التنوّع) à un fait vrai du texte : c'était, à la
   lettre, « un jugement motivé fondé sur les حجج du texte » (contrairement aux distracteurs des items jumeaux
   03 Q5 et 05 Q6, qui reposent sur un principe faux). Correction : le distracteur porte désormais le principe
   faux qu'il encodait implicitement → « وُفِّقَ؛ لأنّ حجّتَيه متنوّعتانِ، والتنوّعُ وحدَه يكفي للإقناعِ »
   (l'explication disait déjà « التنوّعُ وحدَه فلا يكفي إن غابتِ الصلةُ »). Clé inchangée (a), non la plus longue.
3. `cours.md`, section « أبدي رأيي », phrase-pont sous le tableau des critères — pour que l'item 2 soit soluble
   depuis le cours : « …ويُطبّقُهما على النصِّ. » → « …ويُطبّقُهما على النصِّ؛ ولا يُغني معيارٌ عن الصلةِ: حججٌ
   متنوّعةٌ لا تخدمُ الأطروحةَ لا تُقنعُ. »

**Remarques (non corrigées)** :
1. [MINOR] « لم يُوفَّقْ إلى حدٍّ بعيدٍ » (cours, `exemple` de « أبدي رأيي », pas 1 et 4 ; explication de
   03 Q5) : quatrième formule, ambiguë (« pas beaucoup » ou « largement pas ? »), alors que la `definition`
   vient de poser trois positions nettes (« وُفِّقَ إلى حدٍّ بعيدٍ / إلى حدٍّ ما / لم يُوفَّقْ ») ; écrire « لم يُوفَّقْ ».
2. [MINOR] `04-defi` Q5 : la clé « كثيرٌ من الشبابِ يقرؤونَ ما يفيدُهم… » est, dans le texte, introduite par
   la فاء d'تعليل après « وهذا تعميمٌ ظالمٌ » (la position du كاتب au sens strict) ; l'item reste univoque (les
   trois autres options sont fausses d'étendue ou sont la مدحوضة), mais il prend une حجّة pour la أطروحة. Une
   option « ليس كلُّ الشبابِ عازفينَ عن القراءةِ » serait plus juste (réécriture d'item : non faite).
3. [MINOR] Tableau « نوع الحجّة » : la ligne « عقليّة منطقيّة | مقدّمات ونتيجة | «كلُّ … وهذا … فهذا …» »
   ne couvre que le قياس/استنباط ; le استقراء (cas → loi) n'y a pas de قرينة (aucun item du 10 ne le teste ; le
   09 l'enseigne).
4. [MINOR] Le découpage « الأطروحة = المدحوضة + المثبتة » (01 Q5, cours) est la convention annoncée par la
   fiche §6, cohérente avec le 09 ; non vérifiée sur un barème officiel.
5. [MINOR] Distracteurs faibles dans les items « مرادف » : « يَمْنَعُ » (03 Q6), « يُقَرِّبُ / يُسَهِّلُ » (04 Q2,
   antonymes) ne correspondent à aucun sens du mot ; les autres distracteurs de ces items sont, eux, de vrais
   sens concurrents du même verbe (حَمَلَ، ضَرَبَ، سلَّمَ، أثارَ).
6. [MINOR] Gabarit répété « ليس/لا يكفي … بل … → صُغِ المدحوضة » : 01 Q4, 04 Q6, `verifie` du cours (et 09
   04-defi Q3) — textes différents, pas de doublon, mais même cadre de tâche quatre fois.

**Patron** : 9 sections (8 gestes + synthèse « نصّ واحد وأسئلة الامتحان بالترتيب »), chacune ouverte sur une
situation + question, puis `definition` (sauf la synthèse, qui est une méthode), tableau + phrase-pont,
`exemple` à pas justifiés (« لأنّ » presque partout), `piege`, `methode` avec حالة حدّيّة, `verifie`
jumeau, `retenir`. Tous les exemples, pièges et `verifie` re-résolus : justes (dont « يعدّ » = يعتبر / يحصي,
« أقام » = قدّم / مكث, l'analyse complète du texte de la فلاحة en huit questions). `resume.md` : 9 puces en
miroir. **Cohérence 09 ↔ 10** : mêmes définitions (أطروحة، حجّة داعمة/داحضة، مثال، cinq types, sept familles
d'مؤشّرات, الإقناع/التأثير, بنية ثلاثيّة/منقوصة/أطروحتان), mêmes listes d'outils ; le 10 ajoute la règle
« واقعة = مثال si elle suit une حجّة générale, حجّة واقعيّة si elle prouve seule » qui manque au 09 (cf.
remarque 09-2). Faits vérifiés : المدرسة الصادقيّة 1875, القمر 1969.

**Verdict 10 : conforme après corrections. Clarté : 5/5.**

