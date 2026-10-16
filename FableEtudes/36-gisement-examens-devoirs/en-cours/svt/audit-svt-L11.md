# Audit indépendant — gisement SVT 9ᵉ, vague 2, lot L11 (m028–m032)

Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skills
`content-audit` + `prof-svt-9eme`). Branche `wip/gisement-svt-9eme-sessions`, commit `818fdb66`
(valide à ce commit — ré-auditer si les fichiers ont bougé). Lecture seule : aucun fichier audité
modifié, aucune écriture git. Rapport écrit au fil de l'eau.

Sources lues : transcriptions officielles `…/examens-nationaux/9eme-base/sciences-vie-terre/<session>-generale.md`,
PDF officiels (9web.edunet.tn) pour les figures, `cours.md`/`resume.md` des chapitres (origin/main),
missions publiées + quiz des chapitres, `misconceptions.json` (origin/main), PLAN-v2 § 1.

---

## m028 — `01-wadhifat-al-ittisal/exercices/07-examens-2018-ex3-et-qcm-coupes-tissu-nerveux-neurone.json`

Étage d2 (9 questions, toutes d2) : honnête. Titre conforme. Données 2018 ex. 3 fidèles à la
transcription et au PDF (vérifié à 300 dpi) ; items 2019-1, 2016-5, 2013-4, 2002-1 fidèles (2002-1 :
propositions a, b, d réécrites comme le demandait le plan).

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 1→corps cellulaire, 2→dendrite, 3→axone | idem | OK | |
| 2 | 4→tissu conjonctif, 5→faisceau, 6→fibre | idem | **ERREUR (majeur)** | l'énoncé donne les trois paires |
| 3 | (أ) grise, (ب) nerf, (ج) blanche | idem | réserve (majeur) | « nerf = fibres en faisceaux » non enseigné au cours 01 |
| 4 | c | c | réserve (majeur) | explication = clé de Q3 |
| 5 | a | a | réserve (majeur) | doublon de quiz Q8 / 05-tadrib Q1 (« ne pas redemander ») |
| 6 | d (3→1) | d | OK | |
| 7 | b | b | OK | |
| 8 | b | b | réserve (majeur) | notion du chapitre 02 (arc réflexe) |
| 9 | d | d | réserve (majeur) | notion du chapitre 02 (rôle du récepteur) |

**Repères 2018 identifiés par position (point signalé) — TRANCHÉ.** PDF 2018 p. 2 relu à 300 dpi :
le trait du repère 4 aboutit dans la travée sombre entre les trois faisceaux (au voisinage d'un petit
vaisseau, mais sur la travée) → « tissu conjonctif » (نسيج رابط/ضامّ) est la lecture juste ; aucune
option « vaisseau » n'est proposée, donc pas d'ambiguïté. Le repère 5 est une flèche à deux pointes
placée sous le faisceau du bas, d'un bord à l'autre → elle désigne **le faisceau** (حزمة ألياف
عصبيّة). L'option « عرض حزمة من الألياف » est défendable mais maladroite : la légende attendue est
« حزمة من الألياف العصبيّة » (correctif ci-dessous).

### Défauts m028

- **[MAJOR] Q2 — l'énoncé livre les trois paires.** « ويملأ الحيّز الذي يفصل بينها نسيج رابط » +
  « الرقم 4 يشير إلى الحيّز الفاصل بين الحزم » → 4 = نسيج رابط ; « 5 سهم … يمتدّ عرض إحدى الحزم » →
  « عرض حزمة » ; « مقاطع الألياف » + « 6 … أحد المقاطع الدّائريّة » → 6 = مقطع ليف. Rien à
  résoudre. Par ailleurs « حزمة » et « نسيج رابط » ne sont enseignés par aucun cours de 01 (grep :
  0 occurrence dans `cours.md`/`resume.md` de 01 ; « نسيج رابط » n'apparaît qu'au cours 09) : il
  faut les définir sans désigner le repère. **Énoncé de remplacement (vérifié : aucune paire
  lisible, notions définies) :**
  > (مناظرة 2018) يبيّن الرّسم مقطعين عرضيّين مجهريّين أُجريا في مستوى الجهاز العصبيّ عند الإنسان: المقطع (ب) في اليمين والمقطع (ج) في اليسار. رُقّمت ثلاثة عناصر: الرقم 4 يشير إلى الحيّز الدّاكن بين الكتل المستديرة في المقطع (ب)، والرقم 5 سهم ذو رأسين طوله عرض إحدى هذه الكتل، والرقم 6 يشير إلى إحدى الدّوائر الصّغيرة ذات النّقطة المركزيّة في المقطع (ج). نذكّر بأنّ الحزمة مجموعة من الألياف العصبيّة المتجمّعة معًا، وأنّ النّسيج الرّابط نسيج يشدّ أجزاء العضو بعضها إلى بعض. أنسب كلّ رقم إلى ما يمثّله.

  Option `r1` : « عرض حزمة من الألياف » → « حزمة من الألياف العصبيّة » (clé inchangée : l1–r3,
  l2–r1, l3–r2). Explication : remplacer « والسّهم 5 يقيس عرض كتلة مستديرة واحدة من مقاطع الألياف،
  أي حزمة » par « والسّهم 5 يمتدّ على عرض كتلة مستديرة واحدة من مقاطع الألياف، فهو يدلّ على حزمة ».
  Titre SVG (`<title>`) : retirer « يفصل بينها نسيج داكن » → « تفصل بينها مساحة داكنة ».
- **[MINOR] Q2 — figure.** La flèche 5 (`M7 57 L49 57`) a exactement la largeur du faisceau
  haut-gauche (cx 28, rx 22) mais flotte 8 unités sous lui, dans la travée sombre, là où pointe aussi
  le 4 : à 232 px elle se lit comme « largeur de la travée ». Ajouter deux taquets verticaux aux bouts,
  alignés sur les bords du faisceau : `<path d="M7 47 v14 M49 47 v14" stroke="#0f172a" stroke-width="1"/>`
  (ne déplace rien, rend la portée lisible).
- **[MAJOR] Q3 — notion non enseignée.** Distinguer (ب) nerf de (ج) substance blanche exige « dans
  le nerf, les fibres sont groupées en faisceaux entourés de tissu conjonctif » : le cours 01 ne
  l'enseigne pas (il définit la substance blanche = fibres à gaine, et le nerf seulement comme
  « ناقل »). Correctif minimal dans l'énoncé, après « … لا جسم خلويّ بينها. » : ajouter
  « علمًا أنّ ألياف العصب تتجمّع في حزم يحيط بها نسيج رابط، بخلاف ألياف المراكز العصبيّة. »
  (la tâche reste : grise vs blanche vs nerf ; la paire (ب)↔nerf devient une application de la règle
  donnée, acceptable en d2). Correctif de fond (hors lot, à l'orchestrateur) : ajouter au cours 01,
  § « المادّة السّنجابيّة والمادّة البيضاء », une ligne sur la structure du nerf (le sujet 2018 la
  suppose).
- **[MINOR] Q3/Q4 — figure sans lettres.** Les trois cases n'ont pas de lettre (أ)(ب)(ج) ; seul
  l'énoncé dit « (أ) في اليمين… ». Ajouter sous chaque case un `<text>` « (أ) », « (ب) », « (ج) »
  (pied de case, comme le PDF).
- **[MAJOR] Q4 — fuite vers Q3.** L'explication « فالأجسام الخلويّة في المادّة السّنجابيّة، ومحاورها
  ألياف تكوّن المادّة البيضاء وتنتظم في حزم داخل العصب » rend, avec l'énoncé de Q4 qui redécrit les
  trois coupes, la clé entière de Q3 (donjon : tirage au hasard). **Explication de remplacement :**
  > الجسم الخلويّ والتّغصّنات والألياف أجزاء من خليّة واحدة هي الخليّة العصبيّة: جسمها الخلويّ في مركز عصبيّ، ومحورها ليف طويل يمتدّ بعيدًا عنه. فالخليّة العصبيّة هي الوحدة التّركيبيّة، وهي أيضًا الوحدة الوظيفيّة لأنّها تنقل السّيالة العصبيّة. الخطأ الشائع: عدّ العصب وحدة تركيبيّة، والعصب مجموعة ألياف أي أجزاء من خلايا كثيرة؛ ونسبة الحماية إلى الخليّة العصبيّة، والحماية دور السّحايا والسّائل الدّماغيّ الشّوكيّ.
- **[MAJOR] Q5 — doublon du publié.** « كيف تسير السّيالة … على العنصر 1 (تغصّنات) … على العنصر 2
  (محور) » est le sens dendrites → corps → axone que la liste interdit de redemander (quiz Q8,
  05-tadrib Q1) ; l'énoncé nomme lui-même « تفرّعاتها القصيرة » / « ليفها الطّويل », il ne reste que
  la règle du quiz. Q6 (2019) applique la même règle avec une donnée neuve (deux neurones).
  Correctif : **supprimer Q5** (la question 3b du sujet 2018 est couverte par Q6). Son explication
  rendait d'ailleurs la règle qui résout Q6.
- **[MAJOR] Q8 et Q9 — notions du chapitre 02.** « تنشأ السّيالة الحركيّة في المركز العصبيّ » et
  « المستقبل يحوّل المنبّه إلى سيالة حسّيّة » sont enseignés par le cours 02 (§ القوس الانعكاسي,
  l. 104–149) ; le cours 01 ne nomme jamais le récepteur ni l'arc (une seule occurrence de
  « المستقبلات الحسّيّة », au § hygiène). En chapitre 01 (premier du manifeste) l'élève ne peut
  pas les résoudre. Correctif : **déplacer Q8 et Q9 dans m029** (chapitre 02), telles quelles
  (aucun doublon dans 02 : vérifié contre quiz et 01–08). m028 tombe alors à 6 questions (Q1, Q2,
  Q3, Q4, Q6, Q7) : conforme à R5.
- Étiquettes m028 : toutes existantes sur `origin/main`, libellés conformes (Q6 a « في الاتّجاهين » =
  « ou dans les deux sens » du libellé ; Q7 a/c = nerf rachidien pris pour crânien ; Q8 a/d = origine
  du message moteur placée côté sensitif). Q7 d « المخيخ » muette : acceptable.
- Indices de forme : aucune clé strictement la plus longue ; Q7 clé 16 car. ex aequo avec
  « البصلة الشّوكيّة ». OK.
- Rendu : figures Q1–Q6 rendues en Chromium (232 px) : lisibles, aucune ne marque la clé.

---

## m029 — `02-al-af3al-al-in3ikasiya/exercices/09-examens-2013-ex2-et-annales-proprietes-reflexe-sensation-consciente.json`

Étage d2 (9 questions d2) : honnête. Titre conforme. Données fidèles : 2013 ex. 2 q3–q4 (le « quatre »
et « trois » imposés ont bien disparu), 2007 ex. 3 q1 et q3, 2016 ex. 3 q2 (figure conforme au PDF :
1 = fibre peau → neurone passant près du ganglion, 4 = fibre neurone du bas → muscle), 2019-2 (options
reprises ; « الجابذة » du sujet lu « الجاذبة » à juste titre), 2010 ex. 2 § 1 (choix réécrits pour une
seule réponse).

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | a, b, d | a, b, d | OK | |
| 2 | a, b, d (+ f contestable) | a, b, d, f | **réserve (majeur)** | f ambiguë ; marqueur « exemple » |
| 3 | c | c | **réserve (majeur)** | clé seule sans « لأنّ », la plus courte (18 car. contre 56–71) |
| 4 | a | a | OK | |
| 5 | b, d, a, c | idem | **réserve (majeur)** | doublon (01-tamrin Q2 + quiz Q9) et ordre donné par l'énoncé |
| 6 | d | d | OK | plan 2×2, option à deux erreurs (c) muette : bien |
| 7 | b | b | OK (mineur) | flèches ajoutées (absentes du PDF) |
| 8 | b | b | OK | |
| 9 | d | d | **réserve (majeur)** | doublon du quiz Q5 et de 01-tamrin Q2 |

### Défauts m029

- **[MAJOR] Q2 — option f défendable dans les deux sens.** « تهيئة الجهاز الهضميّ بإفراز اللّعاب عند
  شمّ رائحة طعام شهيّ » : la salivation à l'odeur d'un mets *connu* (« شهيّ ») est l'exemple type du
  réflexe conditionnel ; or l'énoncé demande les fonctions du réflexe **inné** (« التّلقائيّة »), et le
  critère du cours 01 (« هل يفعله مولود جديد ؟ ») classe f en conditionnel. Le cours 02 la cite comme
  réflexe sans préciser : un bon élève peut la refuser. Remplacer f par un réflexe sécrétoire inné
  sans débat (clé inchangée a, b, d, f) :
  > تهيئة الهضم بإفراز اللّعاب عند ملامسة الطّعام للّسان

  (signalé hors lot : l'exemple du cours 02 l. 240 et du `resume.md` l. 9 « اللّعاب عند شمّ الطّعام »
  porte la même ambiguïté.)
- **[MAJOR] Q2 — marqueur de forme.** Les clés a, d (et f) portent un exemple (« ، كسحب اليد… »,
  « ، كالتّنفّس », « عند… ») ; les distracteurs c et e n'en ont aucun. Ajouter un exemple à chacun :
  c → « اتّخاذ قرارات تسبقها فترة تفكير وإمعان نظر، كاختيار إجابة في امتحان » ;
  e → « اكتساب سلوكات جديدة بالتّعلّم والتّدرّب، كركوب الدّرّاجة ». (b, vraie, reste seule sans
  exemple : le marqueur ne vote plus.)
- **[MAJOR] Q3 — clé reconnaissable à la forme.** Les trois distracteurs donnent une raison
  (« لأنّ… ») ; la clé « فعل انعكاسيّ فطريّ » (18 car.) est nue et la plus courte. **Clé de
  remplacement (64 car. ; distracteurs 56, 67, 71 : ni la plus longue ni la plus courte) :**
  > فعل انعكاسيّ فطريّ، لأنّ الرّجل جذب ساقه تلقائيًّا دون قرار مسبق

  d « فعل إراديّ، لأنّه يُنجَز بعضلات هيكليّة… » est muette : elle exécute pourtant
  `bio.nerv.reflexe-pris-pour-volontaire` — on peut l'étiqueter (mineur).
- **[MAJOR] Q5 — point signalé (proximité 03-boss Q6 et quiz Q9) — TRANCHÉ : à supprimer.** L'énoncé
  pose « يجذب ساقه ثمّ يحسّ بالألم » : la place de c (dernier) est donnée ; il reste b → d → a, qui est
  l'ordre de l'arc (01-tamrin Q2, quiz Q5). Le seul fait neuf de 2007 q3 (« la douleur vient après le
  retrait, chemin plus long ») est la clé du quiz Q9 et de 03-boss Q6. En outre son explication
  (« يحتاج إلى أن تبلغ السّيالة الحسّيّة قشرة المخّ ») rend la clé de Q4. Q4 couvre déjà 2007 q3
  (comment naît la douleur). Correctif : **supprimer Q5**.
- **[MAJOR] Q9 — doublon.** Nommer les 2ᵉ et 5ᵉ éléments de l'arc « مستقبل ← ناقل حسّيّ ← مركز ←
  ناقل حركيّ ← منفّذ » est exactement la clé du quiz Q5 et de 01-tamrin Q2 (et 05-tadrib Q1). La
  partie neuve du texte à trous de 2010 (fait / arc) est déjà prise par Q8. Correctif : **supprimer
  Q9**.
- **Accueil de m028 Q8 et Q9** (cf. m028) : m029 passe à 9 questions (Q1–Q4, Q6–Q8, + ex-m028 Q8, Q9).
  Pour ex-m028 Q8, retirer de l'énoncé la phrase « تنقل ألياف حسّيّة السّيالة العصبيّة نحو المراكز
  العصبيّة، وتنقل ألياف حركيّة السّيالة العصبيّة نحو العضلة. » : dans ce chapitre elle donnerait la
  règle qui résout Q6 et Q7. Énoncé résultant :
  > (مناظرة 2013) يتمثّل فعل انعكاسيّ في ثني طرف خلفيّ لضفدعة إثر تنبيه جلدها. تنشأ السّيالة العصبيّة الحركيّة في مستوى:

  (options, clé b et explication inchangées ; re-résolu : b seule).
- **[MINOR] Q1 → Q3.** L'énoncé de Q1 (« ثني طرف خلفيّ لحيوان استجابة لتنبيه جلده حركة هي فعل
  انعكاسيّ تلقائيّ ») classe une situation jumelle de celle de Q3 (retrait de la jambe après piqûre).
  Fuite faible (autre espèce, autre stimulus). Possible : « (مناظرة 2013) الفعل الانعكاسيّ التّلقائيّ
  نوع من الأفعال اللّاإراديّة. أيّ العبارات التّالية تصف خاصّيّات الفعل الانعكاسيّ التّلقائيّ؟ »
  (re-résolu : a, b, d inchangé ; « لاإراديّ » ne désigne pas b ni d).
- **[MINOR] Q7 — adaptation non déclarée.** Les flèches rouge/bleue orientées sont un ajout : le PDF
  2019 n'a que deux tracés sans pointe (la racine sensitive se reconnaît au ganglion, notion que les
  cours 01–02 n'enseignent pas — l'ajout est donc justifié). R7 demande de le dire : ajouter en fin
  d'énoncé « (أُضيف السّهمان إلى رسم المناظرة.) ».
- Étiquettes m029 : libellés conformes. Q4 d `effecteur-avant-le-centre` : l'option met les muscles
  avant le cortex, qui n'est pas le centre du réflexe ; le libellé (« effecteur avant le centre ou
  arc inversé ») reste acceptable. Q6 a/b `sensitif-et-moteur-confondus` : exact (un conducteur pris
  pour l'autre) ; c (deux erreurs) muette : conforme.
- Multi : Q1 3/6, Q2 4/6 — nombres non devinables.

---

## m030 — `03-al-ibsar/exercices/12-examens-2003-ex3-2017-ex2-oeil-appareil-photo-lentille-divergente.json`

Étage d2 (7 questions d2) : honnête. Titre conforme. Données 2003 ex. 3 fidèles (le repère 4 du
sujet regroupe bien cornée, humeur aqueuse, cristallin, vitré → « الأوساط الشّفّافة ») ; 2017 ex. 2
q1 fidèle (profil : bords épais, centre mince), figure Q5 conforme au PDF. Terme « قصر البصر » :
conforme au manuel.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | chambre→choroïde, film→rétine, diaphragme→iris, objectif→milieux | idem | réserve (majeur) | Q2–Q4 livrent ses paires |
| 2 | c | c | **réserve (majeur)** | énoncé = 2 paires de Q1 ; explication = paires de Q1 |
| 3 | a, c | a, c | **réserve (majeur)** | énoncé ET options = les 4 paires de Q1 ; explication = clé de Q2 |
| 4 | a | a | **réserve (majeur)** | doublon miroir de 01-tamrin Q6 ; 1ʳᵉ moitié = clé de Q2 |
| 5 | d | d | OK | plan 2×2 forme × type |
| 6 | b | b | réserve (majeur) | explication = clé de Q5 ; figure inventée sous « مناظرة 2017 » |
| 7 | b | b | réserve | explication = clé de Q6 ; miroir de 03-boss Q2 / quiz Q6 |

**Point signalé « proximité de m030 Q2/Q3 » — TRANCHÉ.** Q1 à Q4 sont quatre coupes du même tableau
(2003 q2 : partie de l'œil · partie de l'appareil · fonction). Chaque énoncé ou explication rend la
clé d'une autre : l'énoncé de Q3 cite les quatre paires (= clé de Q1), et ses six options n'apparient
que des paires justes ; l'explication de Q1 donne les fonctions (= clés de Q2 et Q3) ; celle de Q3
donne « الشّبكيّة والفلم : استقبال الخيال ، المشيميّة والغرفة المظلمة : عزل » (= clé de Q2) ; Q4 =
choroïde ↔ chambre noire + « تحجب الضّوء » (= clé de Q2) et « تغذّي الشّبكيّة » (= 01-tamrin Q6 :
« الغشاء الذي يكوّن الغرفة المظلمة ويغذّي الشّبكيّة » → المشيميّة, la même paire de faits à l'envers).
Le donjon tirant au hasard, c'est une fuite MAJEURE. Correctif : séparer les trois axes — Q1 =
appareil ↔ œil (sans fonctions), Q2 = fonctions de l'appareil (sans l'œil), Q3 = fonctions de l'œil
(sans l'appareil) — et **supprimer Q4**. m030 passe à 6 questions (R5 tenu).

### Défauts m030 et textes de remplacement

- **[MAJOR] Q1 — explication** (donne les fonctions, et « القزحيّة التي تتوسّط حدقتها » est faux : c'est
  la pupille qui est au centre de l'iris). Remplacement :
  > تُقابَل أجزاء الآلة بأجزاء العين التي تؤدّي الدّور نفسه في تكوين الخيال: الغرفة المظلمة بالمشيميّة، والفلم الحسّاس بالشّبكيّة، والحجاب بالقزحيّة التي تتوسّطها الحدقة، والعدسة بالأوساط الشّفّافة للعين مجتمعة، وأهمّها القرنيّة والجسم البلّوريّ. والمعيار هو الدّور لا الموضع في الرّسم. الخطأ الشائع: مقابلة الفلم بالمشيميّة لأنّها الغشاء الذي يلي الشّبكيّة، أو مقابلة الحجاب بالحدقة وحدها دون القزحيّة التي تحيط بها.
- **[MAJOR] Q2 — énoncé** (options et clé c inchangées ; re-résolu : c seule) :
  > (مناظرة 2003) في آلة التّصوير الشّمسيّ غرفة مظلمة وفلم حسّاس. أيّ الاختيارات التّالية تذكر وظيفة كلّ منهما؟

  **Explication :**
  > الغرفة المظلمة صندوق مغلق يعزل داخل الآلة عن الضّوء الخارجيّ، فلا يدخل الضّوء إلّا من الفتحة التي في مقدّمتها. والفلم الحسّاس هو السّطح الذي يستقبل الخيال في قاع الآلة. أمّا تجميع الأشعّة فمن عمل العدسة، وتعديل كمّيّة الضّوء من عمل الحجاب. الخطأ الشائع: نسبة وظيفة العدسة أو الحجاب إلى الغرفة المظلمة أو إلى الفلم لأنّها كلّها أجزاء في الآلة نفسها.
- **[MAJOR] Q3 — énoncé et options sans l'appareil** (multi, clé inchangée {a, c} ; re-résolu énoncé
  par énoncé : a V, b F, c V, d F, e F, f F) :
  > (مناظرة 2003) تُقارَن العين بآلة التّصوير الشّمسيّ لأنّ أجزاءها تؤدّي وظائف متشابهة. أيّ العبارات التّالية تنسب إلى جزء من العين وظيفته الصّحيحة؟

  a « القزحيّة: تعديل كمّيّة الضّوء الدّاخلة » · b « القزحيّة: استقبال الخيال » · c « الأوساط الشّفّافة:
  تجميع الأشعّة الضّوئيّة وتكوين الخيال » · d « الأوساط الشّفّافة: عزل الدّاخل عن الضّوء الخارجيّ » ·
  e « الشّبكيّة: تعديل كمّيّة الضّوء الدّاخلة » · f « المشيميّة: تجميع الأشعّة الضّوئيّة ».
  **Explication :**
  > القزحيّة تضيّق الحدقة أو توسّعها فتعدّل كمّيّة الضّوء الدّاخلة إلى العين. والأوساط الشّفّافة، وأهمّها القرنيّة والجسم البلّوريّ، تجمّع الأشعّة فيتكوّن الخيال. أمّا الشّبكيّة فلا تعدّل كمّيّة الضّوء، والمشيميّة لا تجمّع الأشعّة، والقزحيّة لا تستقبل الخيال، والأوساط الشّفّافة تُدخل الضّوء ولا تحجبه. الخطأ الشائع: نسبة وظيفة جزء إلى جزء آخر لمجرّد أنّه مجاور له في العين.

  (vérifié : ne nomme aucune pièce de l'appareil, ne donne ni la fonction de la rétine ni celle de la
  choroïde, donc ni Q1 ni Q2.)
- **[MAJOR] Q4 — supprimer** (doublon miroir de 01-tamrin Q6, et clé de Q2 dans sa première moitié).
- **[MAJOR] Q6 — explication** « العدسة التي حافّتاها أسمك من وسطها عدسة مفرّقة » = clé de Q5
  (forme + type). Remplacement :
  > العدسة التي حافّتاها أسمك من وسطها تباعد الأشعّة: بعد خروجها منها تتباعد الأشعّة المتوازية بعضها عن بعض بدل أن تلتقي. أمّا تجمّع الأشعّة في نقطة واحدة فمن خاصّيّة العدسة التي وسطها أسمك من حافّتيها. الخطأ الشائع: توقّع تجمّع الأشعّة في كلّ عدسة.
- **[MINOR] Q6 — provenance.** Le tracé des trois rayons parallèles n'est pas dans le sujet 2017 (q3
  « بيّن كيف تحقّق هذه العدسة إبصارا جيّدا », écartée par le plan) : la question est dérivée, pas
  reprise. Remplacer « (مناظرة 2017) » par « (انطلاقًا من مناظرة 2017) » et le dire au rapport d'auteur.
- **[MAJOR→MINOR] Q7 — explication** « العدسة المفرّقة تباعد الأشعّة قبل دخولها العين » = clé de Q6.
  Remplacement de la première phrase : « العدسة المفرّقة تؤخّر موضع تشكّل الخيال إلى الوراء؛ وهذا ما
  يحتاجه من يتشكّل خيال الأجسام البعيدة في عينه أمام الشّبكيّة، وهو عيب قصر البصر. » (suite inchangée).
- **[réserve] Q7 — miroir de 03-boss Q2** (« ما العدسات التي تصحّح قصر البصر ؟ » → مفرّقة) et du quiz
  Q6. La ligne « défaut corrigé » a été retenue explicitement par le plan : je la laisse à l'arbitrage
  de l'orchestrateur ; si elle est jugée doublon, la mission tombe à 5 et il faut alors lui rendre une
  question (aucune autre ligne de 2017 n'est libre). Distracteurs c « التهاب الملتحمة » et d « انفصال
  الشّبكيّة » : enseignés (cours 03) mais hors de la famille « défaut de réfraction », éliminables à vue
  (MINOR) ; pas d'autre défaut au programme pour les remplacer — garder.
- Étiquette Q7 a `bio.vis.myopie-hypermetropie-inversees` : exacte. Pas d'autre étiquette.
- Indices de forme : Q6 clé la plus courte (27 contre 29–34) — écart faible, une seule occurrence :
  acceptable.

---

## m031 — `07-ad-dawaran/exercices/09-examens-2015-ex2-2011-ex3-coeur-mouton-valvules-trois-phases.json`

Étage d2 (8 questions d2) : honnête. Titre conforme. Données fidèles : 2011 ex. 3 (tableau des trois
phases), 2008-3 fondu dans Q1 (sessions citées toutes deux), 2015 ex. 2 q1–q2, 2012-2 (options reprises
à l'identique). Aucune étiquette `bio.*` dans la mission (le registre n'a pas de famille « valvules ») :
acceptable.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | c | c | OK | |
| 2 | a, b, f | a, b, f | réserve (majeur) | a = clé de Q7 ; b + f = clé de Q8 |
| 3 | a | a | **réserve (majeur)** | distracteur c = clé de Q1 |
| 4 | 1→veines pulmonaires, 2→aorte, 3→oreillette gauche | idem | OK | |
| 5 | 4→artère pulmonaire, 5→veine cave sup., 6→ventricule droit | idem | OK | |
| 6 | d | d | **réserve (majeur)** | figure : la pastille 7 couvre la cible de 8 ; énoncé = miroir de 05-tadrib Q1 |
| 7 | b | b | OK (explication à retoucher) | |
| 8 | b | b | **réserve (majeur)** | déjà entièrement posée par Q2 (b + f) et Q1 a |

**Repères 2015 identifiés par position (point signalé) — TRANCHÉ : justes.** PDF 2015 p. 2 relu : 1 →
l'un des deux courts tubes en haut à droite du dessin (veines pulmonaires), 2 → intérieur du grand
vaisseau blanc central qui naît du côté à paroi épaisse (aorte), 3 → cavité sous les deux courts tubes
(oreillette gauche), 4 → face ovale du vaisseau voisin à gauche (artère pulmonaire — c'est le vaisseau
dont q4 du sujet fait décrire la paroi « artérielle »), 5 → tube en haut à gauche au-dessus de la
cavité de gauche (veine cave supérieure), 6 → cavité basse de gauche (ventricule droit). La figure
refaite respecte « cœur droit à gauche du dessin », paroi épaisse à droite, et les six cibles.

### Défauts m031

- **[MAJOR] Q6 — figure.** La pastille du 7 (`circle cx=80 cy=126`) est posée exactement sur la pointe
  de la valvule auriculo-ventriculaire droite (`M98 106 L80 126`), et le trait du 8 (`x2=82 y2=124`)
  aboutit sous cette pastille : à 232 px, 8 semble désigner le 7, et la cible de 8 est masquée.
  Remplacer les deux groupes de repères par (vérifié en Chromium : 8 dans la cavité basse gauche
  vers la valvule auriculo-ventriculaire, 7 côté droit vers la base du vaisseau gauche, aucun
  chevauchement) :
  ```
  <line x1="144" y1="136" x2="113" y2="121" stroke="#0f172a" stroke-width="1.2"/><circle cx="150" cy="139" r="7" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/><text x="150" y="143" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a">7</text>
  <line x1="66" y1="146" x2="79" y2="127" stroke="#0f172a" stroke-width="1.2"/><circle cx="62" cy="152" r="7" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/><text x="62" y="156" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a">8</text>
  ```
- **[MAJOR] Q6 — énoncé.** « العنصر 7 صمّامات واقعة في قاعدة الشّريانين … والعنصر 8 صمّامات واقعة بين
  الأذينة اليمنى والبطين الأيمن » réduit la question à la définition par le lieu, miroir de 05-tadrib Q1
  (« الصمّامات السّينيّة توجد : في قاعدة كلّ شريان »). Une fois la figure lisible, le lieu se lit sur le
  dessin, comme au sujet. Énoncé de remplacement (options, clé d, explication inchangées) :
  > (مناظرة 2015) يمثّل الرّسم مقطعًا طوليًّا مبسّطًا في قلب خروف منظور من الأمام، والجهة اليمنى للقلب على يسار الرّسم. يشير الرقمان 7 و8 إلى نوعين من الصمّامات.

  (suivi de la figure corrigée et de « أيّ الاختيارات التّالية تسمّي العنصرين 7 و8 على التّرتيب؟ ».)
- **[MAJOR] Point signalé « proximité m031 Q1–Q3 » — TRANCHÉ.** Les trois questions-phases sont
  légitimes (une par ligne du tableau 2011, la consigne du plan) ; deux fuites précises sont à
  corriger :
  - **Q3 c** « يدفع انقباض الأذينتين الدّم إلى البطينين عبر صمّامات أذينيّة بطينيّة مفتوحة وصمّامات
    سينيّة مغلقة » énonce, en le nommant, la clé de Q1. Remplacer c par (72 car. ; clé a 87, b 89,
    d 78 : clé ni la plus longue ni la plus courte ; c reste fausse en diastole) :
    > ينتقل الدّم من البطينين إلى الأذينتين عبر صمّامات أذينيّة بطينيّة مفتوحة

    et l'explication de Q3 par :
    > في الانبساط العامّ يرتخي القلب فيمتلئ: يصبّ الدّم القادم من الأوردة في الأذينتين، ويمرّ منهما إلى البطينين عبر الصمّامات الأذينيّة البطينيّة المفتوحة. وتبقى الصمّامات السّينيّة مغلقة، فلا يعود الدّم من الشّريانين إلى البطينين. والبطينان في هذا الطّور يمتلئان ولا يردّان دمهما إلى الأذينتين. الخطأ الشائع: عدّ الانبساط طورًا يتوقّف فيه الدّم، أو فتح الصمّامات السّينيّة فيه فيعود الدّم إلى البطينين من الشّريانين.
  - **Q2 a et c** portent la conséquence qui est la clé de Q7 (« فلا يرجع الدّم إلى الأذينتين »). Les
    réduire à l'état : a « تنغلق الصمّامات الأذينيّة البطينيّة » (V), c « تبقى الصمّامات الأذينيّة
    البطينيّة مفتوحة » (F) ; clé {a, b, f} inchangée (re-résolu). Explication de Q2 :
    > عندما ينقبض البطينان يرتفع ضغط الدّم فيهما، فتنغلق الصمّامات الأذينيّة البطينيّة وتنفتح الصمّامات السّينيّة، فيسير الدّم من كلّ بطين إلى الشّريان المتّصل به. ولا ينتقل الدّم في هذا الطّور من الأذينتين إلى البطينين، ولا يبقى محبوسًا في البطينين. الخطأ الشائع: إبقاء الصمّامات الأذينيّة البطينيّة مفتوحة في هذا الطّور.
- **[MAJOR] Q8 — redondante, à supprimer.** « تسمح الصمّامات السّينيّة بمرور الدّم من البطين إلى
  الشّريان » est la conjonction de Q2 b (« تنفتح الصمّامات السّينيّة ») et f (« يسير الدّم من كلّ بطين
  إلى الشّريان المتّصل به »), et l'option a de Q1 la redit ; son explication rend à son tour Q2 b.
  Aucune réécriture ne la sépare du tableau 2011, qui est la base. m031 passe à 7 questions.
- **[MINOR] Q7 — explication** « وتنغلق عندما ينقبض البطين » rend Q2 a. Remplacement :
  > الصمّامات الأذينيّة البطينيّة تسمح بمرور الدّم في اتّجاه واحد، من الأذينة إلى البطين، وتمنع رجوعه من البطين إلى الأذينة. وهي لا تنقبض ولا تدفع الدّم، فالذي يدفعه هو انقباض عضلة القلب؛ ولا شأن لها برجوع الدّم إلى الأوردة. وفصل القلب الأيمن عن الأيسر من عمل جدار فاصل لا من عمل الصمّامات. الخطأ الشائع: نسبة دور الجدار الفاصل أو دور عضلة القلب إلى الصمّامات.
- Résidu accepté : Q1 a (« مغلقة ؛ مفتوحة ؛ من البطينين إلى الشّريانين ») décrit, sans la nommer, la
  phase de Q2 — inhérent au plan 2×2 des états de valvules ; pas de correctif.
- Doublons hors mission : 08-examen-2020 Q3 identifie une phase sur figure (non reprise ici, comme le
  voulait la liste) ; 06-defi-concours Q2 (insuffisance mitrale) voisin de Q7 mais autre raisonnement :
  OK.
- Indices de forme : aucune clé strictement la plus longue ni la plus courte. Multi Q2 : 3/6.

---

## m032 — `13-tandhim-al-wiladat/exercices/07-examens-2003-ex2-2006-ex3-2019-ex2-evenements-stades-oeuf-prevention.json`

Étage d2 (8 questions d2) : honnête. Titre conforme, ne livre aucune clé. Données fidèles : 2003 ex. 2
(définition de la nidation reprise du sujet, ligne « lieu » écartée), 2006 ex. 3 q1 (positions A/B/C/D =
أ/ب/ج/د du sujet, contenus conformes ; globules polaires dessinés, ni nommés ni interrogés) et q4
(fondue dans Q3), 2019 ex. 2 q1–q3. « التّوتيّة » et « المضغة » (stade à cavité) = termes du cours 12.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | c | c | réserve (majeur) | distracteur b = clé de Q2 |
| 2 | a | a | **réserve (majeur)** | doublon de 12/01-tamrin Q1 (même clé mot pour mot) ; d = clé de Q1 |
| 3 | ovulation→pilule combinée, fécondation→préservatif, nidation→DIU | idem | OK (réserve) | appariement unique (seul le DIU empêche la nidation) |
| 4 | C, A, B, D | b, d, a, c | OK | |
| 5 | 1→œuf, 2→2 cellules, 3→4 cellules | idem | **réserve (majeur)** | numéros = ordre chronologique d'un document dit « غير مرتّبة » |
| 6 | 4→morula, 5→« المضغة » | idem | **réserve (majeur)** | deux paires : pile ou face ; numéros chronologiques |
| 7 | d | d | OK | |
| 8 | b | b | **réserve (majeur)** | l'énoncé (« يتضاعف ») élimine c à vue |

**Morula placée dans la trompe (point signalé) — TRANCHÉ : acceptable.** Le document 2 du sujet 2019
offre cinq cadres le long de l'oviducte jusqu'à l'endomètre, dont un « à la jonction du tube avec la
paroi utérine » : la morula y est attendue (fin de l'oviducte), la « مضغة » sur l'endomètre. Le cours 12
(table J4 : morula ; J6 : perte de la zone pellucide et nutrition par les sécrétions utérines → « المضغة »)
et la mission publiée 12/07-examen-2026 Q5 (« التّوتيّة … تُشاهَد في قناة البيض ») disent la même chose.
De plus, aucune option ne départage la morula seule (les quatre options la groupent avec les stades 2 et
4 cellules) : la clé d est unique quoi qu'on pense du jour exact de l'entrée dans l'utérus. Ne pas
allonger d (« قرب الرّحم ») : à 120 car. elle est déjà ex aequo avec a, elle deviendrait strictement la plus
longue.

### Défauts m032

- **[MAJOR] Q2 — doublon, à supprimer.** 12/01-tamrin Q1 « ما الإلقاح؟ » a pour clé « اندماج المشيجين
  وانصهار نواتيهما » et pour distracteurs « دخول حيوان منويّ إلى البويضة فحسب », « تحرير البويضة من
  الجريب » : Q2 en est la copie (même clé, mêmes deux erreurs). Le plan l'avait retenue sans voir ce
  doublon du chapitre 12. Son option d (« تحرّر البويضة من الجريب وانتقالها إلى قناة البيض ») était en outre
  la clé de Q1. Les étiquettes `plusieurs-spermatozoides-entrent` et `fecondation-reduite-a-l-entree`
  disparaissent avec elle (familles existantes, aucun seuil en jeu).
- **[MAJOR] Q1 — fuite.** Option b « انصهار نواة الحيوان المنويّ بنواة البويضة في خليّة واحدة » définit la
  fécondation (clé de Q2, et de 12/01-tamrin Q1). Remplacer b par (61 car. ; clé c 52, a 46, d 29 : clé ni
  la plus longue ni la plus courte ; b fausse, c'est la menstruation) :
  > تمزّق بطانة الرّحم وخروجها مع الدّم في بداية الدّورة الجنسيّة

  et, dans l'explication, « أمّا انصهار النّواتين فهو الإلقاح، وانغراس المضغة في بطانة الرّحم هو التّعشيش. »
  → « أمّا تمزّق بطانة الرّحم وخروجها مع الدّم فهو الحيض، وانغراس المضغة في بطانة الرّحم هو التّعشيش. »
- **[MAJOR] Q5 et Q6 — numérotation chronologique et appariement à deux paires.** L'énoncé dit
  « رسومًا غير مرتّبة » mais les numéros suivent l'ordre du développement (1 œuf, 2 deux cellules,
  3 quatre cellules, 4 morula, 5 stade à cavité) : la clé de Q6 se lit au numéro, et Q6 à deux paires est
  un pile ou face. Fusionner Q5 et Q6 en un seul appariement à cinq paires, avec la numérotation du sujet
  (أ=1 quatre cellules, ب=2 stade à cavité, ج=3 œuf, د=4 morula, هـ=5 deux cellules). Énoncé :
  > (مناظرة 2019) تمثّل الوثيقة رسومًا غير مرتّبة لبعض المراحل التي تمرّ بها البويضة إثر إخصابها، وقد رُقّمت من 1 إلى 5. أنسب كلّ رسم إلى اسم المرحلة التي يمثّلها.

  Gauche : l1 « الرسم 1 » … l5 « الرسم 5 ». Droite : r1 « خليّتان », r2 « أربع خلايا », r3 « خليّة-بيضة »,
  r4 « المضغة », r5 « التّوتيّة ». Clé : l1–r2, l2–r4, l3–r3, l4–r5, l5–r1. Explication : concaténer celles
  de Q5 et Q6 en remplaçant les numéros (« الرسم 1 » de Q5 → « الرسم 3 », « الرسم 2 » → « الرسم 5 »,
  « الرسم 3 » → « الرسم 1 », « الرسم 4 » → « الرسم 4 », « الرسم 5 » → « الرسم 2 »). Figure (les dessins
  existants, sans retouche, en deux rangées ; rendue en Chromium à 232 px : lisible, aucun chevauchement
  nouveau) :

  ```
<svg viewBox="0 0 264 184"><title>خمسة رسوم مرقّمة لمراحل تمرّ بها البويضة المخصّبة: 1 بويضة مقسومة إلى أربع خلايا في كلّ منها نواة، 2 حلقة من خلايا محيطيّة تضمّ كتلة من خلايا أكبر في جهة واحدة، 3 خليّة كبيرة بنواة مركزيّة واحدة تحيط بها خلايا صغيرة وجسمان صغيران قرب الغلاف، 4 كتلة كرويّة ممتلئة بخلايا كثيرة صغيرة متراصّة، 5 بويضة مقسومة إلى خليّتين في كلّ منهما نواة</title>
<rect x="0" y="0" width="264" height="184" fill="#ffffff"/>

<ellipse cx="73.0" cy="46.0" rx="3.2" ry="2.2" transform="rotate(90 73.0 46.0)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/><ellipse cx="70.3" cy="57.7" rx="3.2" ry="2.2" transform="rotate(116 70.3 57.7)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/><ellipse cx="62.8" cy="67.1" rx="3.2" ry="2.2" transform="rotate(141 62.8 67.1)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/><ellipse cx="52.0" cy="72.3" rx="3.2" ry="2.2" transform="rotate(167 52.0 72.3)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/><ellipse cx="40.0" cy="72.3" rx="3.2" ry="2.2" transform="rotate(193 40.0 72.3)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/><ellipse cx="29.2" cy="67.1" rx="3.2" ry="2.2" transform="rotate(219 29.2 67.1)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/><ellipse cx="21.7" cy="57.7" rx="3.2" ry="2.2" transform="rotate(244 21.7 57.7)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/><ellipse cx="19.0" cy="46.0" rx="3.2" ry="2.2" transform="rotate(270 19.0 46.0)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/><ellipse cx="21.7" cy="34.3" rx="3.2" ry="2.2" transform="rotate(296 21.7 34.3)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/><ellipse cx="29.2" cy="24.9" rx="3.2" ry="2.2" transform="rotate(321 29.2 24.9)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/><ellipse cx="40.0" cy="19.7" rx="3.2" ry="2.2" transform="rotate(347 40.0 19.7)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/><ellipse cx="52.0" cy="19.7" rx="3.2" ry="2.2" transform="rotate(373 52.0 19.7)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/><ellipse cx="62.8" cy="24.9" rx="3.2" ry="2.2" transform="rotate(399 62.8 24.9)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/><ellipse cx="70.3" cy="34.3" rx="3.2" ry="2.2" transform="rotate(424 70.3 34.3)" fill="#f1f5f9" stroke="#64748b" stroke-width="0.9"/>
<circle cx="46" cy="46" r="24" fill="#fef9c3" stroke="#0f172a" stroke-width="2.6"/><circle cx="46" cy="46" r="5.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/><circle cx="26" cy="30" r="2.3" fill="#e2e8f0" stroke="#0f172a" stroke-width="1"/><circle cx="30" cy="26" r="2.3" fill="#e2e8f0" stroke="#0f172a" stroke-width="1"/>
<circle cx="18" cy="18" r="8" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/><text x="18" y="22" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a">3</text><circle cx="130" cy="46" r="24" fill="#fef9c3" stroke="#0f172a" stroke-width="2.6"/><line x1="130" y1="22" x2="130" y2="70" stroke="#0f172a" stroke-width="2"/>
<circle cx="119" cy="46" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/><circle cx="141" cy="46" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="102" cy="18" r="8" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/><text x="102" y="22" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a">5</text><circle cx="214" cy="46" r="24" fill="#fef9c3" stroke="#0f172a" stroke-width="2.6"/><line x1="214" y1="22" x2="214" y2="70" stroke="#0f172a" stroke-width="2"/><line x1="190" y1="46" x2="238" y2="46" stroke="#0f172a" stroke-width="2"/>
<circle cx="203" cy="35" r="3.8" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="225" cy="35" r="3.8" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="203" cy="57" r="3.8" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="225" cy="57" r="3.8" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="186" cy="18" r="8" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/><text x="186" y="22" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a">1</text>

<g transform="translate(42,92)">

<circle cx="46" cy="46" r="24" fill="#fef9c3" stroke="#0f172a" stroke-width="2.6"/>
<circle cx="46" cy="28" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="46" cy="28" r="1.4" fill="#0f172a"/>
<circle cx="32" cy="37" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="32" cy="37" r="1.4" fill="#0f172a"/>
<circle cx="41" cy="37" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="41" cy="37" r="1.4" fill="#0f172a"/>
<circle cx="50" cy="37" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="50" cy="37" r="1.4" fill="#0f172a"/>
<circle cx="59" cy="37" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="59" cy="37" r="1.4" fill="#0f172a"/>
<circle cx="28" cy="46" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="28" cy="46" r="1.4" fill="#0f172a"/>
<circle cx="37" cy="46" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="37" cy="46" r="1.4" fill="#0f172a"/>
<circle cx="46" cy="46" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="46" cy="46" r="1.4" fill="#0f172a"/>
<circle cx="55" cy="46" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="55" cy="46" r="1.4" fill="#0f172a"/>
<circle cx="64" cy="46" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="64" cy="46" r="1.4" fill="#0f172a"/>
<circle cx="32" cy="55" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="32" cy="55" r="1.4" fill="#0f172a"/>
<circle cx="41" cy="55" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="41" cy="55" r="1.4" fill="#0f172a"/>
<circle cx="50" cy="55" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="50" cy="55" r="1.4" fill="#0f172a"/>
<circle cx="59" cy="55" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="59" cy="55" r="1.4" fill="#0f172a"/>
<circle cx="46" cy="64" r="4.2" fill="#fef3c7" stroke="#0f172a" stroke-width="1"/><circle cx="46" cy="64" r="1.4" fill="#0f172a"/>
<circle cx="18" cy="18" r="8" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/><text x="18" y="22" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a">4</text><circle cx="130" cy="46" r="24" fill="#fefce8" stroke="#0f172a" stroke-width="2.6"/>
<circle cx="151.0" cy="46.0" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="149.7" cy="53.2" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="146.1" cy="59.5" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="140.5" cy="64.2" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="133.6" cy="66.7" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="126.4" cy="66.7" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="119.5" cy="64.2" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="113.9" cy="59.5" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="110.3" cy="53.2" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="109.0" cy="46.0" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="110.3" cy="38.8" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="113.9" cy="32.5" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="119.5" cy="27.8" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="126.4" cy="25.3" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="133.6" cy="25.3" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="140.5" cy="27.8" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="146.1" cy="32.5" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="149.7" cy="38.8" r="2.8" fill="#fde68a" stroke="#0f172a" stroke-width="0.9"/>
<circle cx="136" cy="36" r="4" fill="#fcd34d" stroke="#0f172a" stroke-width="1"/>
<circle cx="142" cy="41" r="4" fill="#fcd34d" stroke="#0f172a" stroke-width="1"/>
<circle cx="134" cy="43" r="4" fill="#fcd34d" stroke="#0f172a" stroke-width="1"/>
<circle cx="140" cy="32" r="4" fill="#fcd34d" stroke="#0f172a" stroke-width="1"/>
<circle cx="144" cy="35" r="4" fill="#fcd34d" stroke="#0f172a" stroke-width="1"/>
<circle cx="138" cy="47" r="4" fill="#fcd34d" stroke="#0f172a" stroke-width="1"/>
<circle cx="102" cy="18" r="8" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/><text x="102" y="22" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a">2</text>
</g>
</svg>
  ```

  m032 passe à 6 questions (Q1, Q3, Q4, Q5 fusionnée, Q7, Q8).
- **[MAJOR] Q8 — option qui nie une prémisse.** « فيتضاعف عدد خلايا الجنين في كلّ مرحلة » élimine c
  (2 puis 3) à vue et dicte la forme de la réponse. Énoncé de remplacement (options et clé b inchangées ;
  re-résolu : b seule selon le cours 12, J1 = 2 cellules, J2 = 4) :
  > (مناظرة 2019) تنقسم الخليّة-البيضة بعد الإلقاح انقسامات متتالية. ما عدد خلايا الجنين بعد يوم من الإخصاب وبعد يومين منه؟
- **[réserve] Q3.** Deux des trois paires sont des clés publiées (quiz Q1 : pilule → ovulation ; quiz Q2 :
  DIU → nidation) ; le plan tient l'appariement des trois pour neuf. Je le laisse passer : la
  troisième paire (préservatif → fécondation) n'est posée nulle part, et l'appariement est unique (le DIU
  tue aussi les spermatozoïdes, mais il est le seul à empêcher la nidation, ce que dit l'explication).
- **[MINOR] Q4.** Lettres latines A–D à la place de أ–د du sujet : sans conséquence de rendu ; à garder si
  c'est la convention des missions précédentes.
- Étiquette Q1 a `bio.repro.ovulation-produit-un-ovule` : exacte.

---

## Contrôles transverses

- `content:check` : 0 erreur (120 matières, 29 060 questions). `content:qa:strict` : sort en 1, mais
  sur des `id` de SVG sans tiret dans **09-al-ikhraj** (hors lot) ; aucun avertissement sur les cinq
  fichiers du lot. `content:figures:check` : 10 problèmes, aucun dans les fichiers du lot.
  `content:tranche` (01, 02, 03, 07, 13) : clé strictement la plus longue 0/445 ; 2 paires proches,
  hors lot ; 0 candidat gabarit.
- Doublons de gabarit entre les cinq missions : aucun (cinq notions distinctes).
- `chapter.json` : la ligne `sources[]` « Sujets officiels de l'examen national… étude 36 » est présente
  dans les cinq chapitres (ajoutée en 01 et 13 par ce lot, déjà là en 02, 03, 07).
- Étiquettes : 11 étiquettes distinctes, toutes existantes sur `origin/main:content/misconceptions.json` ;
  aucune famille nouvelle proposée, donc pas de seuil « 3 questions » à vérifier.
- Rendu : toutes les figures du lot rendues en Chromium dans une colonne de 232 px (`dir=rtl`) ; seuls
  défauts : m031 Q6 (pastilles 7/8) et m028 Q2 (flèche 5), traités ci-dessus.

## Bilan chiffré

| mission | questions auditées | clés fausses | majeurs | mineurs | après correctifs |
| --- | ---: | ---: | ---: | ---: | ---: |
| m028 | 9 | 0 | 5 | 2 | 6 (Q5 supprimée, Q8–Q9 → m029) |
| m029 | 9 | 0 | 5 | 3 | 9 (Q5, Q9 supprimées ; + ex-m028 Q8, Q9) |
| m030 | 7 | 0 | 5 | 3 | 6 (Q4 supprimée) |
| m031 | 8 | 0 | 5 | 1 | 7 (Q8 supprimée) |
| m032 | 8 | 0 | 4 | 1 | 6 (Q2 supprimée, Q5+Q6 fusionnées) |
| **total** | **41** | **0** | **24** | **10** | **34** |

Questions à reprendre : 28 (dont 9 suppressions, déplacements ou fusions). Aucune clé fausse.

## Résumé

- **Clés fausses : 0** sur 41 questions re-résolues à l'aveugle.
- **Majeurs (24)** : surtout des **fuites** entre questions d'une même mission (m030 Q1–Q4 sont quatre
  coupes d'un même tableau, m031 Q2/Q3 donnent les clés de Q1/Q7/Q8, m032 Q1/Q2, m028 Q4 → Q3) ; des
  **doublons du publié** (m028 Q5 = quiz Q8 ; m029 Q5 et Q9 = 01-tamrin Q2 / quiz Q5, Q9 ; m030 Q4 =
  01-tamrin Q6 ; m032 Q2 = 12/01-tamrin Q1) ; **notions du chapitre 02** dans m028 (Q8, Q9 → à déplacer
  dans m029) ; un **énoncé qui livre l'appariement** (m028 Q2) ; deux **indices de forme** (m029 Q3 clé
  nue, m029 Q2 exemples) ; une **figure** (m031 Q6, le 7 masque la cible du 8) ; une **prémisse qui
  élimine** (m032 Q8) ; une **numérotation chronologique** (m032 Q5–Q6).
- **Mineurs (10)** : flèche 5 de m028 Q2, lettres absentes en m028 Q3/Q4, adaptation non déclarée m029 Q7,
  provenance m030 Q6, explications m030 Q7 / m031 Q7, etc.
- **Étiquettes** : toutes existantes, libellés justes ; aucune famille nouvelle.
- **Points signalés** : repères 2015 et 2018 **justes** (PDF relu) ; morula dans la trompe **acceptable**
  (conforme au sujet et au cours, et sans effet sur l'unicité de la clé) ; m029 Q5 **à supprimer** ;
  m030 Q2/Q3 et m031 Q1–Q3 : **fuites réelles**, correctifs fournis.
- **Verdict : à corriger avant publication** (fix-first). Après correctifs, les cinq missions restent
  entre 6 et 9 questions (R5 tenu), toutes d2.
