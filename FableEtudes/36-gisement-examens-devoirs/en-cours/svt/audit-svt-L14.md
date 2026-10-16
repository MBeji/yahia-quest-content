# Audit indépendant — gisement SVT 9ᵉ, devoirs, lot L14 (salle blanche, T2′)

Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skills `content-audit` puis
`prof-svt-9eme`). Périmètre : 6 missions de devoirs, 41 questions, worktree `/home/user/wt-svtses`
(commit `278d46db`). Aucun fichier audité n'est modifié ; aucune écriture git.

Lu : les cartes `assign-svt-devoirs-L14.md` ; `cours.md` des chapitres 01, 02, 03, 08, 09, 11, 13 sur `origin/main` ;
les missions publiées et les missions d'examen (vague 2) des mêmes chapitres ; `content/misconceptions.json`.
Non lu : sources des devoirs, lignes de lecture, snapshots, notes des auteurs, `sources-externes/`.

Outils :
- `content:gisement:controle` (depuis `eng-svtses`) : **✓ 41 textes, 0 plage ≥ 8 mots, 0 plage ≥ 6 mots, 0 exercice
  source avec 2 ou 3 données communes.** Salle blanche respectée.
- `content:check` : ✓. `content:qa:strict --subject sciences-vie-terre` : 0 erreur (1 avertissement préexistant, domaines).
- `content:tranche` (ch. 02, 03, 07, 09, 11, 13) : clé strictement la plus longue 0/507 ; 3 paires proches, toutes
  internes à 07/10 (Q1↔Q3 0,60 ; Q3↔Q4 0,55 ; Q1↔Q4 0,51).
- Similarité ad hoc (Jaccard) de chaque question du lot contre tout `sciences-vie-terre` (quiz et missions) ;
  relecture manuelle des voisins : deux doublons de fait (11/11 Q5 et Q6).
- Figures rendues dans Chromium (`/opt/pw-browsers/chromium-1194`), 232 px de large, conteneur `dir="ltr"` comme
  `svg-figure.tsx` ; coordonnées relues dans le source.
- Note d'environnement : `node_modules` du moteur était vide ; `npm ci --ignore-scripts` a été lancé dans
  `/home/user/yahia-quest-arena` (dossier ignoré par git, aucune écriture suivie).

Rapport écrit au fil de l'eau (état : terminé).

---

## 1. `03-al-ibsar/exercices/13-devoir-affirmations-et-intrus-neurone-oeil.json` — d2 `practice` 75/15, 7 Q

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | a, b, c | a, b, c | réserve (majeur) | l'explication nomme les méninges comme gaine protectrice : elle donne la clé de Q2 |
| 2 | b | b | OK | intrus univoque, étiquettes exactes |
| 3 | a, b, c, f | a, b, c, f | réserve (majeur) | l'explication dit « الجسم البلّوريّ عدسة شفّافة » : c'est la clé de Q4 |
| 4 | c | c | OK | — |
| 5 | d | d | OK | clé plus longue de 2 caractères seulement (58 contre 56) : négligeable |
| 6 | a | a | OK | la raison de la clé est un fait vrai, pas le critère (SNP) ; on choisit à l'élément |
| 7 | c | c | **majeur** | même savoir que Q2 (méninges = enveloppe, pas des fibres) : l'option et l'explication de Q2 donnent la clé ; grammaire de a |

Exactitude : conforme aux cours 01 et 03 (cellule nerveuse, trois tuniques, cornée prolongeant la sclérotique,
image renversée et plus petite, 12 paires crâniennes). Pas de figure. Rampe 1,1,2,2,2,2,2 : honnête.

## 2. `02-al-af3al-al-in3ikasiya/exercices/10-devoir-enchainement-volontaire-reflexe-lesions.json` — d3 `boss` 120/30, 6 Q

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | b, d, e | b, d, e | OK, mineur | l'explication dit « والتّمدّد إلى المنشفة » (s'allonger), au lieu de « ومدّ اليد » |
| 2 | b | b | **majeur** (autonomie) | « الذي تتبّعناه عند ريم » renvoie à Q1 ; le donjon tire au hasard |
| 3 | d | d | OK, mineur | « وخز الكفّ → انثنت أصابعها » ressemble au réflexe de préhension ; le retrait de la main est le réflexe médullaire du cours |
| 4 | c | c | **majeur** (autonomie) | « عن مشهد ريم: كلّ أفعالها الأخيرة » n'a de sens qu'après Q1 |
| 5 | a, b, c | a, b, c | **majeur** (exactitude) | « عضلات ساقه » : le réflexe rotulien met en jeu un muscle de la cuisse (cours 02 : « عضلة في الوجه الأمامي للفخذ »). Si seuls les muscles de la jambe sont touchés, b n'est pas déductible |
| 6 | (أ)-r1, (ب)-r2, (ج)-r3 | idem | **majeur** (doublon) | (ج) + r3 = exactement le cas de Q5 (corps cellulaires moteurs) : Q5 et son explication donnent la paire |

Observation sans correctif exigé : Q3 (lésion du lobe gauche, réflexe conservé) et Q6 (أ) (lobe droit, jambe gauche)
reposent sur le même raisonnement ; l'explication de Q3 rend la paire (أ)-r1 immédiate. On peut l'accepter dans un
appariement de synthèse.

Liste « ne pas redemander » : respectée (ni les propriétés du réflexe inné, ni la distinction réflexe/sensation de
02/09, ni l'ordre des cinq éléments). La donnée de l'auteur, « sortie motrice commune », est juste et suffisante.
Rampe 1,2,2,2,3,3 : honnête.

## 3. `07-ad-dawaran/exercices/10-devoir-courbes-glucose-intestin-sang-trajet-vers-coeur.json` — d3 `boss` 120/30, 7 Q

La figure, relue dans le source, donne pour la lumière intestinale : 0, 8, 22, **26** (70 min), 14, 6, 2 g/L. Pour le
sang sortant : 1,0, 1,1, 1,6, 2,4, **2,7** (100 min), 2,0, 1,3 g/L. Elle est vraie, cohérente avec les énoncés et ne
marque aucune clé. Valeurs plausibles (glycémie portale de 2,7 g/L après un repas riche en amidon : haute mais
possible).

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | c (70) | c | OK | 70 est le seul point d'option situé entre les graduations 50 et 100 |
| 2 | a | a | OK, mineur | « بين 70 و100 يتناقص في المعي » situe le pic intestinal à 70 min au plus (indice pour Q1, en ordre aléatoire) |
| 3 | 30 | 30 | **majeur** (lecture) | réponse numérique sans options : l'axe n'a ni graduation ni étiquette à 70, l'élève peut lire 65 ou 75 |
| 4 | b (1,7) | b | OK, mineur | « اكتب الجواب » dans un QCM. Distracteurs : 1,4 = 2,7 − 1,3 (180 min), 2,7, 3,7. Explication juste |
| 5 | c | c | OK, mineur | l'explication définit la veine comme le vaisseau qui « entre au cœur », or la veine intestinale va d'abord au foie (Q6). Les valeurs 2,7/1,0 à 100 min répètent la clé de Q4 et le pic de Q3 |
| 6 | b, e, c, f, a, d | idem | OK | la donnée de l'auteur, « foie puis veine cave inférieure », est juste et suffisante ; ordre unique |
| 7 | d | d | OK | — |

**Paires proches Q1/Q3/Q4 (Jaccard 0,51–0,60) : acceptable, pas de reformulation exigée.** La phrase de contexte
commune est imposée par l'autonomie (le donjon tire chaque question seule, avec la même figure). Les trois
questions demandent trois lectures distinctes : date du pic intestinal, délai entre les deux pics, hausse maximale
dans le sang. À justifier au rapport de tranche comme « même document, autres lectures ». Le correctif de Q3
(ci-dessous) fait d'ailleurs baisser le recouvrement Q1↔Q3.

## 4. `09-al-ikhraj/exercices/13-devoir-definitions-respiration-et-excretion.json` — d2 `practice` 75/15, 6 Q

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | l1-r2, l2-r4, l3-r1, l4-r3 | idem | OK | conforme au cours 08 (mouvements involontaires, rythme régulier) |
| 2 | l1-r2, l2-r4, l3-r3, l4-r1 | idem | OK, mineur | r2 « مرور الصّغير » : il manque le nom (« المواد الصّغيرة ») |
| 3 | a | a | OK | a décrit la trachée (2 cm, anneaux cartilagineux), comme le cours 08 |
| 4 | d | d | OK, mineur | explication : « تجتمع فيه البول » ; البول est masculin, il faut « يجتمع » |
| 5 | b, c, f | b, c, f | OK, mineur | 22 ÷ 0,4 = 55 ✓ ; les options e et d ont une étiquette exacte qui n'est pas posée |
| 6 | c | c | OK, mineur | d (« الشّرين النّابذ » sort de la glomérule) réfute l'option fausse de Q4. c ressemble à 09/09 Q3 option e (« إفراز مواد كالنّشادر ») |

Données inventées (NaCl 5,5 → 9, urée 0,4 → 22) : plausibles et proches du tableau du cours (6 → 10 ; 0,3 → 20).
Rampe 1,1,2,2,2,2 : honnête.

## 5. `11-ad-dawra-al-jinsiya/exercices/11-devoir-courbe-progesterone-coupes-ovaire-duree-du-cycle.json` — d3 `boss` 120/30, 7 Q

La courbe, relue dans le source (jour 1 à x = 46, 6,94 px par jour), est basse et plate du jour 1 au jour 16. Elle
monte à partir du jour 17, culmine au jour 24, revient au niveau bas au jour 30. Les règles occupent les jours 1 à 4
et 31 à 35. La figure est vraie. Les coupes d'ovaire sont lisibles à 232 px et ne marquent aucune clé.

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | a | a | **majeur** (fuite) | l'énoncé dit « دورتها الأولى، من اليوم 1 إلى اليوم 30 » : c'est la clé de Q4 (30 jours), avec la même figure |
| 2 | d | d | OK | — |
| 3 | ب, د, أ, ج | idem | OK | rappel follicule/corps jaune juste et suffisant ; le sous-ensemble de 11/08 Q3 est élargi (follicule jeune, corps jaune en régression) |
| 4 | b (30) | b | OK, mineur | les étiquettes « يوم 1 / يوم 31 » rendent la lecture immédiate ; le premier « الحيض » touche l'axe à 232 px |
| 5 | b (16) | b | **majeur** (doublon) | 30 jours → jour 16 est l'exemple résolu du cours 11 (« احسب يوم الإباضة عند امرأة دورتها 30 يومًا ») et répète 11/03-boss Q1 (mêmes options 14/15/16). La figure (montée au jour 17) et l'explication de Q4 (« 15 = de l'ovulation aux règles ») le donnent aussi |
| 6 | c (26) | c | **majeur** (doublon miroir) | ovulation au jour 12 → 26 jours est l'inverse exact de 13/quiz Q3 (26 → jour 12) ; « امرأة أخرى » renvoie à une autre question |
| 7 | c | c | **majeur** (indice de forme + fuite) | chaque option décrit sa coupe : « انخفض » appelle « قلّ إفرازه » sans regarder la figure. De plus, la clé est le dernier terme de l'ordre de Q3, que donne l'explication de Q3 |

Liste « ne pas redemander » : respectée (ni le calendrier de 12/11, ni les phases utérines de 11/10).

## 6. `13-tandhim-al-wiladat/exercices/08-devoir-ovaire-uterus-par-le-sang-et-contraception-hormonale.json` — d4 `challenge` 300/60, 8 Q

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | d | d | OK | dénervation de l'utérus, cycle maintenu : plausible et classique |
| 2 | c | c | OK | greffe sous-cutanée d'un fragment d'utérus : plausible (le cours greffe l'ovaire ; ici l'expérience est symétrique) |
| 3 | a | a | OK, mineur | « بالتّحديد » est trop strict : l'origine ovarienne vient de la combinaison avec l'ablation, pas de la parabiose seule |
| 4 | b | b | OK | une seule comparaison ne fait varier qu'un facteur ; étiquettes `cause-sans-temoin` exactes |
| 5 | b | b | réserve (mineur) | clé la plus courte (40 contre 49–51), une seule fois ; le couple pilule ↔ ovulation est celui de 13/07 Q2, mais la question porte sur le mécanisme, comme le demande la carte |
| 6 | d | d | **majeur** (rappel qui désigne la clé) | « نعلم أنّ الحيض ينتج عن انخفاض تركيز الهرمونات » : la règle du cours 11, donnée avant une courbe qui chute après le jour 21 ; la même phrase est la clé de Q7 |
| 7 | a | a | OK, réserve | b est éliminée par l'explication de Q6 (« فالأقراص لا تلغي الحيض ») ; scientifiquement, le saignement d'arrêt est une hémorragie de privation, mais le cours 13 l'appelle « الحيض » : b est fausse dans le cadre du programme |
| 8 | b, d, f | b, d, f | **majeur** (autonomie + doublon) | « اعتمادًا على ما سبق » renvoie aux questions précédentes ; b = clé de Q5, d = clé de Q6, c = affirmation réfutée en Q7, a = distracteur de Q6 b ; « تتلف المبيضان » (accord) |

La figure de Q6 (courbe des deux hormones de synthèse, prise de pilule puis arrêt) est vraie et ne marque pas la
clé. Les expériences inventées (dénervation, greffe, parabiose, injection continue) sont plausibles et conformes au
raisonnement du cours 11 (§ « المبيض يقود الرّحم »). Rampe 2,3,3,3,3,3,3,3 : conforme à l'usage des `challenge`
du corpus (aucun d4 interne).

---

## Défauts classés et correctifs (textes vérifiés)

Chaque option de remplacement a été mesurée (longueur sans diacritiques) : aucune clé ne devient strictement la plus
longue. Aucune prémisse n'est niée. Chaque texte a été comparé aux autres questions de la mission et aux missions
publiées du sujet, sans fuite trouvée.

### Critiques — 0

Aucune clé fausse : les 41 re-résolutions concordent.

### Majeurs — 12

**M1. 03/13 Q1, explication (fuite vers Q2).**
- Remplacer « والمحور العصبيّ جزء من الخليّة نفسها وليس غلافًا: الذي يحيط بالمراكز العصبيّة ويحميها هو السّحايا. »
- par « والمحور العصبيّ جزء من الخليّة نفسها وليس غلافًا يحيط بها. »

**M2. 03/13 Q3, explication (fuite vers Q4).**
- Remplacer « والجسم البلّوريّ عدسة شفّافة تمرّر الضّوء ولا تلتقطه، فلا مستقبلات فيه. »
- par « والجسم البلّوريّ لا يحمل مستقبلات بصريّة، فلا يحوّل الضّوء إلى سيالة. »

**M3. 03/13 Q7 (même savoir que Q2, clé donnée par Q2).** Remplacer l'option c et l'explication, et corriger
l'accord dans a :
- a : « المادّة البيضاء تحوي أليافًا عصبيّة محاطة بأغماد دهنيّة بيضاء »
- c (clé, inchangée en id) : « المادّة السّنجابيّة في النّخاع الشّوكيّ تحيط بالمادّة البيضاء »
- explication : « العبارة الخاطئة هي القول إنّ المادّة السّنجابيّة في النّخاع الشّوكيّ تحيط بالمادّة البيضاء. فالعكس هو الصّحيح: في النّخاع تكون المادّة السّنجابيّة في الدّاخل والبيضاء حولها، أمّا في المخّ فالسّنجابيّة في الخارج وتكوّن القشرة. والعبارات الثّلاث الأخرى صحيحة: المادّة البيضاء ألياف بأغماد دهنيّة، وللدّماغ اثنا عشر زوجًا من الأعصاب القحفيّة، والصّلبة تتّصل في الأمام بالقرنيّة الشّفّافة. هذا السّؤال من نوع البحث عن العبارة الخاطئة، فالخيار الصّحيح هو العبارة الخاطئة نفسها. »
- Longueurs : a 57, b 48, c 54, d 47. Le fait est enseigné dans le cours 01 (tableau des substances grise et blanche). Pas d'étiquette sur la clé.

**M4. 02/10 Q2 (autonomie).** Nouvel énoncé : « وخزت شوكة إصبع طفل فسحب يده فورًا قبل أن يفكّر. أيّ وصف لسير السّيالة العصبيّة في هذا الفعل الانعكاسيّ صحيح؟ » (options, clé et explication inchangées ; la scène ne recopie plus l'option b de Q1).

**M5. 02/10 Q4 (autonomie).** Énoncé, options c et d, et explication :
- énoncé : « عطس فتى حين دخل غبار أنفه، ثمّ قرّر أن يغلق النّافذة، وتمّ الفعلان في ثوانٍ قليلة. قال زميله: «الفعلان انعكاسيّان لأنّهما تمّا في ثوانٍ قليلة». ما التّصحيح السّليم لهذا الاستدلال؟ »
- c (clé) : « المعيار سبق القرار لا السّرعة، فإغلاق النّافذة بعد قرار فعل إراديّ »
- d : « المعيار هو المنبّه، فكلّ فعل يعقب منبّهًا من الوسط فعل انعكاسيّ » (sans étiquette)
- a et b inchangées (a garde `bio.nerv.vitesse-comme-critere`). Longueurs : a 63, b 67, c 63, d 58.
- explication : « الأفعال الإراديّة يسبقها تفكير ثمّ قرار، أمّا الانعكاسيّة فتحدث دون قرار. والمعيار الفاصل هو سبق القرار وليس مدّة الإنجاز: إغلاق النّافذة جاء بعد قرار فهو إراديّ ولو تمّ في ثوانٍ، أمّا العطاس فيحدث دون قرار. والسّرعة لا تصلح معيارًا، فقد يكون الفعل الإراديّ سريعًا. والعضلات الهيكليّة تنفّذ الأفعال الإراديّة والانعكاسيّة معًا فلا تفرّق بينها. ووجود منبّه لا يكفي، فكثير من الأفعال الإراديّة تأتي ردًّا على منبّه، كما أُغلقت النّافذة بعد دخول الغبار. الخطأ الشائع: جعل السّرعة معيارًا للتّصنيف. »

**M6. 02/10 Q5 (muscle du réflexe rotulien).**
- Dans l'énoncé, remplacer « المتّجهة إلى عضلات ساقه اليسرى. أيّ العبارات التّالية تصف حال هذه السّاق؟ » par « المتّجهة إلى عضلات طرفه السّفليّ الأيسر. أيّ العبارات التّالية تصف حال هذا الطّرف؟ ».
- Option a : « يبقى الإحساس بوخز جلده لأنّ الألياف الحسّيّة لم تُمسّ ».
- Le reste est inchangé. Clé {a, b, c} inchangée.

**M7. 02/10 Q6 (doublon de Q5).** Remplacer le patient (ج), r3 et l'explication :
- l3 : « المريض (ج): لا يحسّ بالوخز، ولا يحرّك ساقه إراديًّا، ولا تنثني ساقه انعكاسيًّا »
- r3 : « قطع عصب النّسا في مستوى الفخذ »
- paires inchangées : l1-r1, l2-r2, l3-r3.
- explication : « المريض (أ) يحسّ ويفعل الانعكاس لكنّه لا يحرّك ساقه بإرادته: القوس الانعكاسيّ النّخاعيّ سليم، والمعطوب هو المركز الإراديّ في قشرة المخّ، وهو الفصّ الجبهيّ الأيمن لأنّ المسار يتقاطع ويصيب الساق اليسرى. المريض (ب) لا يحسّ ولا يحدث عنده الانعكاس، مع بقاء الحركة الإراديّة: العطب في الألياف الحسّيّة وحدها، وهي تخدم الإحساس والقوس الانعكاسيّ معًا، أمّا الألياف الحركيّة فسليمة. المريض (ج) فقد الإحساس والحركة الإراديّة والانعكاس معًا: عصب النّسا عصب مزدوج، فقطعه يقطع الألياف الحسّيّة والحركيّة في آن واحد. الخطأ الشائع: عدّ كلّ شلل إصابة في المخّ. »
- Les trois profils sont distincts. Le nerf mixte est enseigné (cours 01, 02/07 Q6). La distinction réflexe/sensation consciente de 02/09 n'est pas redemandée.

**M8. 07/10 Q3 (lecture de 70 impossible à coup sûr).** Nouvel énoncé, avant la figure :
« تناول فتى وجبة غنيّة بالنّشا عند الدّقيقة 0، ثمّ قِيس تركيز الجليكوز بالغرام في اللّتر في تجويف معاه الدّقيق (المنحنى الأعلى) وفي الدّم الذي يغادر المعي (المنحنى الأسفل)، في الدّقائق 0 و15 و40 و70 و100 و140 و180. كم دقيقة تفصل ذروة تركيز الجليكوز في تجويف المعي عن ذروته في الدّم الخارج منه؟ اكتب العدد بالدّقائق. »
Clé 30 inchangée. Les instants donnés correspondent exactement aux points de la figure.

**M9. 11/11 Q1 (fuite vers Q4).** Nouvel énoncé, avant la figure inchangée :
« تبيّن الوثيقة تغيّر تركيز البروجستيرون، وهو هرمون يفرزه المبيض، في دم امرأة منتظمة الدّورة. في أيّ مجال من الأيّام يبقى تركيزه منخفضًا وثابتًا قبل أن يرتفع؟ »
Options et clé (a) inchangées ; aucune autre option ne satisfait « قبل أن يرتفع ».

**M10. 11/11 Q5 et Q6 (doublons).**
- Q5, énoncé : « امرأة دورتها الجنسيّة منتظمة وتدوم 31 يومًا، واليوم 1 هو أوّل يوم حيض. في أيّ يوم من الدّورة تقع إباضتها؟ »
  - options : a « اليوم 18 », b « اليوم 17 » (clé), c « اليوم 16 » (`bio.cycle.ovulation-au-milieu-du-cycle`), d « اليوم 14 » (`bio.cycle.ovulation-au-milieu-du-cycle`).
  - explication : « الطّور اللّوتينيّ، وهو الممتدّ من الإباضة إلى نهاية الدّورة، ثابت ويدوم 14 يومًا، أمّا الطّور الجريبيّ فمتغيّر. فتُحسب الإباضة رجوعًا من نهاية الدّورة: 31 − 14 = 17، أي في اليوم 17 ✓. القيمة 14 هي إباضة دورة من 28 يومًا، والقيمة 16 تنتج عن وضع الإباضة في منتصف الدّورة، أي نحو نصف 31 يومًا، والقيمة 18 تنتج عن الطّرح من اليوم 32 الذي يفتتح الدّورة الموالية. الخطأ الشائع: وضع الإباضة في منتصف الدّورة. »
  - Une phase folliculaire de 17 jours reste dans la fourchette du cours (11 à 17). Le couple 31 → 17 ne figure nulle part dans le sujet.
- Q6, énoncé : « امرأة منتظمة الدّورة حدثت عندها الإباضة في اليوم 15 من دورتها، واليوم 1 هو أوّل يوم حيض. ما مدّة دورتها الجنسيّة بالأيّام؟ »
  - options : a « 30 », b « 29 » (clé), c « 28 », d « 14 » (`bio.cycle.compte-depuis-l-ovulation`).
  - explication : « من الإباضة إلى نهاية الدّورة يمتدّ الطّور اللّوتينيّ، وهو ثابت ويدوم 14 يومًا. والإباضة في اليوم 15، فمدّة الدّورة 15 + 14 = 29 يومًا ✓. القيمة 14 هي مدّة الطّور اللّوتينيّ وحده، وتنتج عن العدّ من الإباضة لا من أوّل يوم حيض. والقيمة 28 هي المدّة المعتادة للدّورة وليست معطى هذه المرأة. والقيمة 30 تنتج عن إضافة يوم زائد عند العدّ. الخطأ الشائع: عدّ الدّورة منذ الإباضة. »
  - Vérification : jours 16 à 29, soit 14 jours de phase lutéale ✓.

**M11. 11/11 Q7 (descriptions dans les options + fuite depuis Q3).**
- Nouvel énoncé, avec la même figure que Q1 (courbe de progestérone), à la place des coupes : « تبيّن الوثيقة تغيّر تركيز البروجستيرون في دم امرأة منتظمة الدّورة. أُخذ من مبيضها مقطع يظهر فيه جسم أصفر صغير ضامر قلّ إفرازه. في أيّ يوم من دورتها الأولى أُخذ هذا المقطع على الأرجح؟ »
- Options : a « اليوم 8 », b « اليوم 16 », c « اليوم 24 », d « اليوم 29 » (clé), toutes sans étiquette.
- Explication : « الجسم الأصفر لا يتكوّن إلّا بعد الإباضة، ممّا تبقّى من الجريب المنفجر، ثمّ يكبر ويفرز البروجستيرون، وإن لم يحدث إلقاح يضمر فيقلّ إفرازه. فالمقطع المطلوب يوافق فترة انخفاض التّركيز بعد الذّروة، أي اليوم 29 ✓. في اليوم 24 يبلغ التّركيز ذروته، وذلك يوافق جسمًا أصفر كبيرًا في أوج إفرازه لا جسمًا ضامرًا. وفي اليومين 8 و16 يكون التّركيز منخفضًا هو أيضًا، لكنّ ذلك قبل الإباضة، حين لا يوجد في المبيض جسم أصفر أصلًا بل جريب ينمو. الخطأ الشائع: ربط كلّ تركيز منخفض بجسم أصفر ضامر دون الانتباه إلى موقعه من الإباضة. »
- Re-résolution sur la figure : jour 29 ≈ 4,5 (descente) ; jour 24 = pic ; jours 8 et 16 = plateau bas avant la montée du jour 17. Clé unique. Les jours 8 et 16 sont les distracteurs discriminants. Le plateau bas (Q1) est d1, placé avant : pas de fuite en avant.

**M12. 13/08 Q6 et Q8.**
- Q6 : supprimer de l'énoncé la phrase « نعلم أنّ الحيض ينتج عن انخفاض تركيز الهرمونات في الدّم. » (avec l'espace qui la suit). Le reste est inchangé ; la règle est enseignée dans le cours 11 (§ « حيض يأتي من النّقصان »).
- Q8, énoncé : « تتناول امرأة الأقراص المركّبة منذ أشهر: قرص كلّ يوم من اليوم الأوّل لدورتها ولمدّة 21 يومًا، ثمّ تمتنع سبعة أيّام قبل بدء علبة جديدة. أيّ العبارات التّالية صحيحة؟ »
- Q8, options :
  - a « لا يتكوّن في مبيضها جسم أصفر خلال أيّام تناول الأقراص » ✓
  - b « يتكوّن في مبيضها جسم أصفر كبير لأنّ تركيز البروجستيرون في دمها مرتفع » ✗
  - c « تعود الإباضة إلى الحدوث بعد أن تتوقّف المرأة نهائيًّا عن تناول الأقراص » ✓
  - d « يتلف المبيضان نهائيًّا بعد استعمال طويل للأقراص » ✗
  - e « تحميها الأقراص من الأمراض المنقولة جنسيًّا » ✗ `bio.contra.efficacite-vaut-protection-ist`
  - f « تقع إباضتها نحو اليوم 14 من كلّ دورة كما لو لم تتناول الأقراص » ✗
- Q8, clé : {a, c}. Longueurs : 51 / 66 / 63 / 45 / 38 / 60.
- Q8, explication : « تحافظ الأقراص على تركيز مرتفع ثابت للمادّتين المصنّعتين طيلة 21 يومًا، فيختفي التّغيّر الدّوريّ الذي يقود نضج الجريب، فلا تحدث الإباضة في اليوم 14 ولا في غيره. والجسم الأصفر يتكوّن ممّا تبقّى من الجريب المنفجر بعد الإباضة، فإذا غابت الإباضة لم يتكوّن جسم أصفر، والبروجستيرون المرتفع في دمها مصدره الأقراص لا المبيض. وهذا الأثر مؤقّت: لا تتلف الأقراص المبيضين، فتعود الإباضة بعد التّوقّف النّهائيّ. والأقراص لا تحمي من الأمراض المنقولة جنسيًّا، فالواقي وحده حاجز يمنعها. الخطأ الشائع: نسبة كلّ بروجستيرون في الدّم إلى جسم أصفر في المبيض. »
- Q8, vérification : l'option a s'infère (pas d'ovulation, donc pas de corps jaune, cours 11 + 13). Aucune option ne reprend une clé de Q5 à Q7. L'énoncé est autonome.

### Mineurs — 12

1. 02/10 Q1, explication : remplacer « والتّمدّد إلى المنشفة » par « ومدّ اليد إلى المنشفة ».
2. 02/10 Q3 (réflexe de retrait plutôt que flexion des doigts) :
   - énoncé : « فانثنت أصابعها. ما سبب بقاء هذا الانثناء؟ » → « فانسحبت يده. ما سبب بقاء هذا السّحب؟ » ;
   - b : « …يكفي لإنجاز الانثناء كاملًا » → « …يكفي لإنجاز السّحب كاملًا » ;
   - c : « عضلات الأصابع » → « عضلات الذّراع » ;
   - explication : « لكنّ انثناء الأصابع إثر الوخز » → « لكنّ سحب اليد إثر الوخز ».
   - Longueurs : 64 / 64 / 67 / 65, clé d.
3. 07/10 Q4 : « كم بلغت أقصى زيادة له بعد الوجبة؟ اكتب الجواب بالغرام في اللّتر. » → « كم بلغت أقصى زيادة له بعد الوجبة، بالغرام في اللّتر؟ ».
4. 07/10 Q5 :
   - énoncé : « في الدّقيقة 100 » → « في الدّقيقة 140 », et « 2,7 غرام في اللّتر » → « 2,0 غرام في اللّتر » (valeur de la figure à 140 min ; plus de répétition de 2,7) ;
   - explication : « الشّريان وعاء يخرج من القلب، والوريد وعاء يدخل إليه، » → « الشّريان يحمل الدّم من القلب نحو العضو، والوريد يعيده من العضو نحو القلب، ».
5. 07/10 Q2 : la borne « بين 70 و100 » annonce un pic intestinal à 70 min au plus. À tolérer : on lit 70 sur la figure de toute façon.
6. 09/13 Q2 r2 : « مرور الصّغير من بلازما » → « مرور المواد الصّغيرة من بلازما ».
7. 09/13 Q4, explication : « تجتمع فيه البول » → « يجتمع فيه البول ».
8. 09/13 Q5 : poser `bio.excr.filtration-selective` sur e et `bio.excr.etape-du-nephron-confondue` sur d (étiquettes exactes, déjà au registre).
9. 09/13 Q6 :
   - d → « عودة الجليكوز والماء من الأنبوب البوليّ إلى الشّعيرات المحيطة به », avec `bio.excr.etape-du-nephron-confondue` (sécrétion confondue avec réabsorption ; ne réfute plus l'option fausse de Q4) ;
   - explication : « وخروج الدّم من الكبيبة بالشّرين النّابذ مجرّد سير للدّم نحو شعيرات الأنبوب. » → « وعودة الجليكوز والماء إلى الشّعيرات هي إعادة الامتصاص، وهي في الاتّجاه المعاكس للإفراز. ».
   - Longueurs : 67 / 62 / 63 / 61, clé c ni la plus longue ni la plus courte.
10. 11/11 figure (Q1, Q4, M11) : remplacer `<text x="59.9" y="50" font-size="11" font-weight="700" text-anchor="middle" fill="#be123c">الحيض</text>` par `<text x="48.0" y="50" font-size="11" font-weight="700" text-anchor="start" fill="#be123c">الحيض</text>`. Le mot ne chevauche plus l'axe ; au-dessus de la courbe, rien n'est touché.
11. 13/08 Q3 : « ما الذي تثبته هذه التّجربة بالتّحديد؟ » → « ما الاستنتاج الذي تسمح به هذه التّجربة؟ ».
12. 13/08 Q5 : clé la plus courte une fois (40 contre 49–51) ; couple pilule ↔ ovulation déjà apparié en 13/07 Q2. Pas de correctif exigé : la question porte sur le mécanisme (concentration constante → plus de variation cyclique), que demande la carte.

### Observations sans correctif

- 02/10 : Q3 et Q6 (أ) reposent sur le même raisonnement (lésion corticale, voie croisée, réflexe conservé). C'est acceptable dans un appariement de synthèse.
- 13/08 Q7 : l'option b (« ce n'est pas des règles ») est vraie au sens physiologique strict (hémorragie de privation). Le cours 13 nomme ce saignement « الحيض » ; b est donc fausse dans le cadre du programme. Il faut rester cohérent avec le libellé de l'étiquette (voir plus bas).
- 03/13 Q6 : la raison de la clé est un fait vrai, sans le critère (système nerveux périphérique). Ce n'est pas un indice de forme : on choisit à l'élément.

---

## Étiquettes `bio.*` proposées

1. **`bio.contra.regles-supprimees-par-la-pilule` (13/08 Q6 b, Q7 b, Q8 a) — exacte, à créer, avec un libellé
   restreint à la pilule combinée prise 21 jours puis interrompue 7 jours.** En prise continue, la pilule supprime
   réellement les saignements : un libellé général serait faux. Libellés proposés :
   - fr : « Tu crois que la pilule combinée supprime les règles : pendant les jours d'arrêt, la chute des hormones de synthèse fait s'effondrer la muqueuse utérine et les règles surviennent. »
   - ar : « تظنّ أنّ الأقراص المركّبة تلغي الحيض: في أيّام الامتناع ينخفض تركيز المادّتين المصنّعتين فتتهدّم بطانة الرّحم وينزل الحيض. »
   - en : « You think the combined pill abolishes periods: during the pill-free days the synthetic hormones fall, the uterine lining breaks down and a period comes. »
   - Si M12 est appliqué, l'option a de Q8 disparaît : l'étiquette reste sur Q6 b et Q7 b.
2. **`bio.circ.vaisseau-defini-par-sa-teneur` (07/10 Q5) — l'erreur est juste, mais le registre a déjà sa sœur
   `bio.circ.artere-sang-oxygene` (« Tu définis l'artère par un sang riche en oxygène… »).** Recommandation : ne pas
   créer de nouvelle étiquette ; élargir le libellé existant et le poser sur les options a et b de Q5 (et non sur d,
   qui inverse le sens de l'absorption) :
   - fr : « Tu définis l'artère ou la veine par ce que porte son sang (oxygène, nutriments) : l'artère porte le sang du cœur vers un organe, la veine le ramène vers le cœur ; l'artère pulmonaire porte un sang chargé de CO₂. »
   - ar : « تعرّف الشّريان أو الوريد بما يحمله دمه (الأكسيجين أو المغذّيات): الشّريان يحمل الدّم من القلب نحو العضو، والوريد يعيده نحو القلب ؛ والشّريان الرّئويّ يحمل دمًا محمّلًا بثاني أكسيد الكربون. »
   - en : « You define an artery or a vein by what its blood carries (oxygen, nutrients): an artery carries blood from the heart to an organ, a vein brings it back to the heart; the pulmonary artery carries CO₂-laden blood. »
   - Les usages actuels de l'étiquette (oxygène) restent exacts sous ce libellé. Si l'orchestrateur préfère une étiquette distincte, l'id proposé est acceptable avec la même phrase privée de sa dernière proposition.
3. **`bio.cycle.compte-depuis-l-ovulation` (11/11 Q4 d = 15, Q6 d = 14) — exacte, à créer.** Elle est voisine de
   `compte-depuis-la-fin-des-regles` sans la doubler. Avec M10, Q6 d (14) l'exécute toujours. Libellés proposés :
   - fr : « Tu comptes le cycle à partir de l'ovulation : le jour 1 est le premier jour des règles ; de l'ovulation à la fin du cycle, il n'y a que la phase lutéale (14 jours). »
   - ar : « تعدّ الدّورة انطلاقًا من الإباضة: اليوم الأوّل هو أوّل يوم حيض، ومن الإباضة إلى نهاية الدّورة لا يمتدّ إلّا الطّور اللّوتينيّ (14 يومًا). »
   - en : « You count the cycle from ovulation: day 1 is the first day of the period; from ovulation to the end of the cycle there is only the luteal phase (14 days). »

Les étiquettes existantes posées par l'auteur (`bio.nerv.*`, `bio.dig.absorption-dans-la-digestion`,
`bio.lecture.valeur-d-une-autre-grandeur`, `bio.circ.coeur-une-seule-pompe`, `bio.excr.etape-du-nephron-confondue`,
`bio.cycle.*`, `bio.contra.maillon-confondu`, `bio.demarche.cause-sans-temoin`) : libellés relus sur la branche,
toutes exactes pour l'erreur exécutée.

## Étages et rampe

- Les six rampes sont non décroissantes.
- Les étages annoncés (d2/d2/d3/d3/d3/d4) correspondent à la difficulté réelle. 11/11 Q4 est facile pour d2 (jours
  étiquetés sur la figure), sans gravité.
- Les récompenses suivent la table : practice 75/15, boss 120/30, challenge 300/60. Les titres portent les ⭐.

## Bilan chiffré

- Questions auditées : 41. Clés fausses : 0. Critiques : 0.
- Majeurs : 12 (M1 à M12, 15 questions à reprendre).
  - 03/13 : Q1, Q3, Q7.
  - 02/10 : Q2, Q4, Q5, Q6.
  - 07/10 : Q3.
  - 11/11 : Q1, Q5, Q6, Q7.
  - 13/08 : Q6, Q8.
- Mineurs : 12.
- Salle blanche : ✓ (contrôle outillé, 0 plage).
- **Verdict : à corriger avant livraison (fix-first).** Toutes les clés sont justes. Après application de M1 à M12,
  re-vérification rapide des questions touchées.
