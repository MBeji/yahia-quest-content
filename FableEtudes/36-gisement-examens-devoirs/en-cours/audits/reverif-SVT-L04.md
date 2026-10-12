# Re-vérification ciblée — lot SVT-L04 (ch. 09-al-ikhraj 07-09, 10-an-nudj-al-jinsi 07, 11-ad-dawra-al-jinsiya 07-09), après correctifs

## État d'avancement

- [x] Versions identifiées : auditée = `HEAD~1` (bbcb3640), corrigée = `HEAD` (7dbc0f75) = arbre de `wt-gis` (aucune modification non commitée sous `content/`)
- [x] Diff structurel champ par champ (sept fichiers) — écrit
- [x] 09/07 · 09/08 · 09/09 · 10/07 · 11/07 · 11/08 · 11/09 — écrits
- [x] Écarts de l'auteur — écrits
- [x] Étiquettes (familles neuves, placements hors lot, existantes posées/retirées) — écrites
- [x] Mesures (tranche, qa) et rendu Chromium — écrits
- [x] Synthèse — écrite (re-vérification terminée)

Second auditeur indépendant (le premier est injoignable), même consigne (`gisement-auditeur.md`). Rien n'est modifié
dans le dépôt : seul ce rapport est écrit ; aucune écriture git.

## Méthode

- Diff champ par champ `HEAD~1` → `HEAD` (script, SVG comparés balise par balise). Champs touchés :
  - 09/07 : explication Q1 ; étiquette Q4 d retirée.
  - 09/08 : énoncé Q1 (phrase d'ouverture) ; `<title>` des figures de Q1 et Q2 (« على مسار البول » → « في الكلية », rien
    d'autre dans les SVG) ; options Q2 et Q3 (« العنصر X: … ؛ العنصر Y: … ») ; énoncés Q3 et Q4 (ouverture sans renvoi à la
    figure) ; explications Q1, Q3, Q4.
  - 09/09 : options a, b, c de Q1 + explication ; énoncé Q4.
  - 10/07 : étiquette Q3 c posée ; explications Q3, Q4.
  - 11/07 : options a, b de Q3 + explication ; explications Q1, Q2.
  - 11/08 : explication Q1.
  - 11/09 : énoncé Q3 (définition), option r1, explication Q3 ; explication Q5.
  - Aucun autre champ (clés, types, difficultés, en-têtes, ordre) n'a bougé.
- Textes appliqués comparés par script aux correctifs de `audit-SVT-L04.md` : tous verbatim, sauf les deux écarts déclarés
  (09/08 Q1, 11/07 Q2). **Aucun écart non déclaré.**
- Re-résolution à l'aveugle de chaque question dont le côté visible a bougé (et des voisines) ; faits contrôlés sur les
  cours d'`origin/main` (ab909cde) : 01 l. 157-159 et 225, 05 l. 253-257, 07 l. 60-62, 112-116, 158-164, 09 l. 61-80, 111,
  159, 210-214 ; manuel 105905 p. 83 et 86 (l'amylase pancréatique donne « 100 % سكّر شعير » à partir de l'amidon : elle
  n'agit pas sur le maltose).
- Libellés lus sur `origin/main:content/misconceptions.json` ; options hors lot relues sur `origin/main`.

## 09/07 (2026 ex.1, practice d2)

| item | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (explication) | b « إلى الشّرايين » | b | OK |
| Q4 d (étiquette retirée) | c « الأنبوب البولي » | c | OK |

- Q1 : les trois citations (« إلى البطينين », « إلى الأذينتين », « إلى الأوردة ») sont les textes exacts des options ; « إغفال
  انغلاق الصمّامات الأذينيّة-البطينيّة » est au cours 07 (l. 113 : elles se ferment au début du انقباض البطينيّ) ; « فيُختار »
  partout ; le trait d'union entre deux mots arabes s'affiche dans l'ordre en `dir=rtl` (rendu vérifié).
- Q4 d muette : juste (erreur de structure, pas d'étape). a, b gardent `etape-du-nephron-confondue` (inchangé, déjà validé).

## 09/08 (2025 ex.5, boss d3)

| item | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (énoncé, explication — écart 1) | c « (أ): محفظة بومان ؛ (ب): الأنبوب البولي » | c | OK |
| Q2 (options « العنصر X: ») | d glucose / ammoniac | d | OK |
| Q3 (énoncé sans figure, options) | b « X réabsorbé ; Y sécrété » | b | OK |
| Q4 (énoncé sans figure, explication) | a | a | OK |

- **Majeur levé.** Q3 et Q4 s'ouvrent maintenant sur « قِيس لدى شخص سليم تركيزُ عنصرين (X) و(Y) … وهذه النّتائج: » : plus
  aucun renvoi à une figure (recherche normalisée de « الوثيقة / الرّسم / المنحنى / الشّكل / الجدول / الخانات » sur les champs
  des sept fichiers sans SVG : 0). Les trois lignes de données sont intactes ; aucun distracteur ne devient vrai.
- Grilles 2×2 recomptées case par case après l'ajout de « العنصر » : Q2 X {protides a, c ; glucose b, d}, Y {urée a, b ;
  ammoniac c, d} ; Q3 X {sécrété a, d ; réabsorbé b, c}, Y {sécrété a, b ; réabsorbé c, d} : chaque valeur deux fois, options à
  deux erreurs (Q2 a, Q3 d) muettes. Longueurs : Q2 clé 39 (c 41), Q3 clé 73 (c 83) — jamais strictement la plus longue.
- Q4 explication : « إفراز فضلات من الدّم إلى البول، وإخراج فضلات سامّة كالبولة في البول النّهائيّ » = cours 09 l. 213-214 ;
  l'ammoniac n'est pas nommé (pas de fuite vers Q2).
- « في الكلية » partout (énoncé Q1, `<title>` des deux figures) : la glomérule n'est plus mise « sur le trajet de l'urine ».
- Fuites : l'explication de Q1 ne nomme ni le glucose ni l'ammoniac et ne dit pas le sens des variations (rien pour Q2 ni Q3).
- Lettres latines : X et Y sont les noms officiels des éléments (et des courbes), pas des repères de position ; aucune
  collision avec les pastilles A-D du portail. Conforme à la décision 6.

**Écart 1 de l'auteur (explication de Q1) — accepté.** Le texte de l'audit est repris, avec « وهي أوّل منطقة بعد الكبيبة »
en fin de la réfutation de (أ) (le raisonnement « ce qui est filtré se rassemble dans la capsule avant le tube » n'exclut le
tube pour (أ) que si l'on rappelle que (أ) suit immédiatement la glomérule : l'ajout ferme l'argument ; « هي » vise la capsule
ou la zone (أ), les deux lectures sont vraies) ; et « الخطأ الشائع » finit par « إعطاء المنطقتين الاسم نفسه دون النّظر إلى
ترتيبهما ولا إلى تغيّر السّائل بعد الكبيبة », qui couvre les options a et d sans réintroduire la règle fausse « deux
compositions différentes ⇒ deux structures ». Juste.
Retouche facultative (non bloquante) : « سائل المحفظة هو البول الأوّليّ الذي لم يتغيّر بعد » peut se lire « l'urine primitive
est le plasma inchangé » (elle a perdu les protides) ; plus précis : « سائل المحفظة هو البول الأوّليّ الذي لم يتغيّر فيه
تركيز X وY بعد الكبيبة ».

## 09/09 (2024 ex.3, boss d3)

| item | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (nouvelles options, explication) | d « النّيفرون ؛ الكلية » | d | **réserve mineure** (fuite de l'explication vers Q3) |
| Q4 (énoncé « من الكلية ») | (أ) capsule, (ب) canal collecteur, (ج) glomérule | l1-r2, l2-r3, l3-r1 | OK |

- Q1, grille 2×2 recomptée : unité {glomérule a, c ; néphron b, d}, organe {vessie a, b ; rein c, d} ; chaque valeur deux
  fois ; a (deux erreurs) muette ; b, c muettes faute d'étiquette exacte (juste) ; aucune option ne s'élimine sans connaissance
  (toutes dans l'appareil urinaire). Clé 18 car. < b 19. « الكبيبة » dans les options ne livre pas le couple 4 → glomérule de
  Q2 (l'option ne désigne aucun élément dessiné).
- **[mineur, introduit par le correctif de l'audit] Explication de Q1 → Q3.** « والمثانة كيس يخزن البول مؤقّتًا ولا نيفرون
  فيها » et « لأنّ البول يتجمّع فيها » réfutent mot pour mot l'option b de Q3 (multi, « تخزين البول مؤقّتًا قبل التّبوّل »),
  dont l'explication dit la même chose (« أمّا خزن البول مؤقّتًا فمن عمل المثانة »). Q1 (d1) précède Q3 (d2) dans la quête :
  fuite en avant sur un des six items. Texte de remplacement (explication entière de Q1), vérifié : ne dit rien du stockage, du
  transport ni d'aucune des six fonctions, ne désigne aucun élément de la figure (rien pour Q2), notions du cours 09 (l. 61,
  111) :
  « يمثّل الرّسم النّيفرون كاملًا، وهو الوحدة الوظيفيّة للكلية، ويبلغ عدده قرابة المليون في كلّ كلية. أمّا الكبيبة فجزء من
  النّيفرون لا الوحدة كلّها، والمثانة عضو آخر من الجهاز البوليّ لا نيفرون فيها، إذ لا توجد النّيفرونات إلّا في الكليتين.
  الخطأ الشائع: تسمية الوحدة باسم أحد أجزائها، أو نسبتها إلى المثانة لأنّها من الجهاز البوليّ أيضًا. »
- Q4 : « في ثلاثة مواضع من الكلية » — juste ; appariement inchangé et unique.

## 10/07 (2021 ex.1, practice d2)

| item | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q3 c (étiquette posée), explication | a | a | OK |
| Q4 (explication) | c « إثر دخول حيوان منويّ إليها » | c | OK |

- Q3 c « قلب أيمن ← أوردة رئويّة ← رئتان ← شريان رئويّ ← قلب أيسر » : une seule erreur dans la grille (sens juste, noms des
  vaisseaux permutés) ; l'élève appelle « veines » le vaisseau du sang chargé de CO₂ qui sort du cœur droit et « artère » celui
  du sang oxygéné : c'est exactement `bio.circ.artere-sang-oxygene` (« Tu définis l'artère par un sang riche en oxygène :
  l'artère sort du cœur, la veine y entre ; l'artère pulmonaire porte un sang chargé de CO₂ »). Porte R1 : l'explication dit
  « مع أنّ الشّريان يخرج من القلب والوريد يدخل إليه ». d (côtés inversés) reste muette, b (deux erreurs) muette : juste.
- Q4 : citations = textes exacts des options a et b ; « فيُختار ».

## 11/07 (2025 ex.1, practice d2)

| item | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (explication) | c « اتّساع مساحة التّبادل » | c | OK |
| Q2 (explication — écart 2) | a « ألياف عصبيّة » | a | OK |
| Q3 (options a, b recomposées, explication) | d « في المعي الدّقيق بمفعول العصارة المعويّة » | d | OK |

- **Majeur levé (Q3).** Lieux : المعدة (a, b) et المعي الدّقيق (c, d), deux fois chacun ; sucs une fois chacun ; le vote par
  lieu ne départage rien, le compte de « العصارة » (a, c, d) non plus. Chaque distracteur est faux et n'a qu'une erreur (le suc ;
  son lieu est cohérent avec lui : cours 05 l. 254, « يتواصل مفعول اللّعاب قليلًا » dans l'estomac) : a suc gastrique (protides),
  b salive (amidon), c suc pancréatique (amidon → maltose : cours 05 l. 256, manuel p. 86). Clé 40 car. < c 42.
- Étiquette `bio.dig.specificite-enzyme-ignoree` sur a, b, c : le libellé (« Tu fais agir une enzyme sur n'importe quel
  aliment : chacune n'agit que sur son substrat (amylase → amidon, trypsine → protides) ») nomme exactement l'erreur des trois
  (amylase salivaire et pancréatique prêtées au maltose ; suc gastrique prêté à un sucre). Porte R2 : « ولكلّ أنزيم مادّته
  وحدها » dans l'explication.
- Explication de Q3 : conforme au cours 05 l. 253-257 ; ne touche aucune autre question du fichier.
- Q1 : citations exactes (« سمك جدارها », « ارتفاع الضّغط داخلها »).

**Écart 2 de l'auteur (explication de Q2) — accepté.** Le texte de l'audit (« … «الرّابطة» التي تصل بين خليّتين داخل النّخاع:
هي خلايا كاملة، وأجسامها الخلويّة لا توجد في المادّة البيضاء ») devient « وكذلك الخلايا العصبيّة الرّابطة، وهي خلايا كاملة
تصل بين خليّتين عصبيّتين داخل النّخاع، وأجسامها الخلويّة لا توجد في المادّة البيضاء التي لا تحتوي إلّا على الألياف ». Le
sens est le même, la phrase est mieux construite (pas de guillemets autour d'un mot, pas de deux-points au milieu), et l'ajout
« لا تحتوي إلّا على الألياف » est la définition du cours 01 (l. 157-159 : la blanche contient les fibres, pas de corps
cellulaires) et rend l'option d réfutable par le cours seul. Cohérent avec le cours 01 l. 225 (un neurone est une seule cellule
qui s'étend de la grise à la blanche : ce sont ses fibres, non la cellule entière, qui sont dans la blanche). Pas de fuite.

## 11/08 (2022 ex.3, practice d2)

| item | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (explication) | b « الإباضة » | b | OK |

- Texte de l'audit verbatim : ne décrit plus le follicule mûr (paroi fermée) ni le corps jaune (paroi restante) — rien pour
  Q2 ni Q3 ; les deux réfutations sont vraies (aucune cellule ne sort pendant la croissance du follicule ni la formation du
  corps jaune ; fécondation dans la trompe). Q2, Q3, Q4, Q5 inchangés.

## 11/09 (2021 ex.3, boss d3)

| item | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q3 (« الكريّة القطبيّة », explication) | 1 → chromosomes, 2 → cytoplasme, 3 → globule polaire | l1-r2, l2-r3, l3-r1 | OK |
| Q5 (explication) | c « 26 يومًا » | c | OK |

- Q3 : terme des sujets officiels, défini dans l'énoncé (accord féminin juste : « خليّة صغيرة جدًّا تنفصل … وتبقى لاصقة ») ;
  plus aucune occurrence de « الجسم القطبيّ » dans le lot ; le membre de phrase sur l'acrosome a disparu (plus de fuite vers Q2).
- Q5 : « حساب 31 − 6 = 25 دون عدّ يوم 6 نفسه، وهو اليوم الأوّل من الدّورة » nomme exactement le mécanisme du 25 ; rendu
  Chromium `dir=rtl` : « 31 − 6 = 25 » s'affiche dans l'ordre source, comme « 31 − 6 + 1 = 26 » déjà validé ; « فيُختار » trois fois.
- **[mineur, préexistant, non relevé par l'audit] Q4 explication : dernier « فيُكتب » du lot.** La décision d'harmoniser
  « فيُكتب » → « فيُختار » (l'élève choisit, il n'écrit pas) a été appliquée partout sauf ici. Remplacer « فيُكتب البربخ مكان
  الأنابيب المنويّة » par « فيُختار البربخ بدل الأنابيب المنويّة ». (Aucune autre occurrence de « يُكتب » dans les sept fichiers :
  recherche normalisée.)

## Étiquettes

### Familles neuves (`etiquettes/SVT-L04.json`) — absentes d'`origin/main`, non posées dans les fichiers : conforme

**A `bio.nerv.substances-grise-blanche-confondues`** (libellé avec « السّيالة العصبيّة », comme arbitré).

| placement | texte (relu sur `origin/main` ou dans le lot) | étiquette actuelle | jugement |
| --- | --- | --- | --- |
| 11/07 Q2 b | « تغصّنات » (dans la blanche) | — | exacte |
| 11/07 Q2 c | « أجسام خلويّة » | — | exacte |
| 11/07 Q2 d | « خلايا عصبيّة رابطة » | — | acceptable : cellules entières (corps compris) mises dans la blanche ; le libellé range les corps cellulaires dans la grise |
| 01/quiz Q3 a | « من أجسام خلويّة عصبيّة وتغصّناتها » (blanche) | aucune (`remplace: null` juste) | exacte |
| 01/01-tamrin Q4 a | « نقل السّيالة العصبيّة على مسافات طويلة » (rôle de la grise) | aucune | exacte (rôle de la blanche prêté à la grise) |

**B `bio.circ.capillaire-comme-l-artere`** (correction avec « très nombreux / كثيرة جدًّا », comme arbitré ; cours 07 l. 158-164).

| placement | texte | étiquette actuelle | jugement |
| --- | --- | --- | --- |
| 11/07 Q1 a | « سمك جدارها » | — | exacte |
| 11/07 Q1 b | « ارتفاع الضّغط داخلها » | — | exacte |
| 11/07 Q1 d | « سرعة حركة الدّم داخلها » | — | exacte |
| 07/03-boss Q4 a | « قلّة عددها وسمك جدارها وسرعة الجريان » | aucune | acceptable : deux traits d'artère + « peu nombreux », que la correction couvre désormais |
| 07/03-boss Q4 c | « ضغطها المرتفع وسمكها » | aucune | exacte |
| 07/quiz Q7 a | « سمك الجدار وارتفاع الضّغط وسرعة الجريان » | aucune | exacte |

Textes, indices de question et d'option, `nom_fichier` et `remplace` du JSON : identiques à `origin/main`. Les clés (11/07
Q1 c, Q2 a ; 01/quiz Q3 c ; 01/01-tamrin Q4 b ; 07/03-boss Q4 b ; 07/quiz Q7 c) ne sont pas touchées. 07/quiz Q7 b (« قلّة
عددها واتّساع قطرها ») reste muette à juste titre.

### Existantes posées ou retirées

- 09/07 Q4 d : `etape-du-nephron-confondue` retirée — juste.
- 10/07 Q3 c : `artere-sang-oxygene` posée — exacte (voir 10/07).
- 11/07 Q3 a, b, c : `specificite-enzyme-ignoree` — exactes (voir 11/07).
- Les douze identifiants posés dans le lot existent tous sur `origin/main` (contrôle par script). Les erreurs « not declared »
  de `content:qa` sur la branche viennent de son registre périmé (`content/misconceptions.json` de `wt-gis` en retard sur
  `origin/main`), pas du lot.

## Mesures et rendu

- `content:tranche -- --subject sciences-vie-terre --chapters 09,10,11 --fresh` (moteur `eng-gis`, contenu = `wt-gis`, lecture
  seule) : 31 questions ; clé strictement la plus longue **0/23** ; positions a 6 · b 6 · c 6 · d 5 ; paires proches **0** ;
  candidats gabarit 0.
- `content:qa -- --subject sciences-vie-terre` : 22 lignes sur les sept fichiers, **toutes** « tag not declared » (registre de
  la branche, voir ci-dessus) ; aucune autre.
- Chromium `dir=rtl` (`isolateLtrRuns` du moteur) : options « العنصر X: … ؛ العنصر Y: … », explication de 09/08 Q3, ouverture de
  Q3/Q4, explication de 11/09 Q5, « الأذينيّة-البطينيّة », options de 09/09 Q1 : ordre affiché = ordre source.
- Observation moteur (préexistante, sans effet de lecture, à router) : « عنصرين (X) و(Y) في » — l'isolat de « (Y) » emporte
  l'espace qui le suit, si bien que l'affichage donne « و (Y)في » ; même rendu dans les quatre énoncés de 09/08 depuis le début.

## Hors périmètre, toujours ouvert

- **Cours 11 l. 49 (sur `origin/main` comme sur la branche)** : « 30 − 5 = 25 يومًا، ثمّ يومان … ← 27 يومًا » (juste : 28).
  Depuis la correction de 11/09 Q5, l'explication appelle **erreur** « 31 − 6 = 25 sans compter le premier jour », qui est
  exactement la méthode de ce cours : l'élève qui suit le cours choisit le distracteur b et lit qu'il s'est trompé. À corriger
  avant ou avec la publication du lot (texte de l'audit § 12, vérifié : 28).

## Synthèse

- **Clés fausses : 0.** Toutes les questions retouchées et leurs voisines re-résolues à l'aveugle = les clés ; grilles 2×2 de
  09/08 Q2-Q3, 09/09 Q1 et 11/07 Q3 recomptées case par case ; aucun distracteur devenu vrai ; aucune clé strictement la plus
  longue.
- **Majeurs : 0 restant** (09/08 Q3-Q4 et 11/07 Q3 levés).
- **Correctifs de l'audit** : les 2 majeurs et les 16 mineurs appliqués, verbatim sauf les deux écarts déclarés, **tous deux
  acceptés**. Aucun écart non déclaré.
- **Mineurs restants : 2**
  1. 09/09 Q1, explication (introduit par le correctif de l'audit) : fuite vers 09/09 Q3 b — texte de remplacement ci-dessus.
  2. 11/09 Q4, explication (préexistant) : « فيُكتب البربخ مكان الأنابيب المنويّة » → « فيُختار البربخ بدل الأنابيب المنويّة ».
- Facultatif : 09/08 Q1, « البول الأوّليّ الذي لم يتغيّر بعد » → « … الذي لم يتغيّر فيه تركيز X وY بعد الكبيبة ».
- Étiquettes : deux familles neuves exactes (placements « acceptables » : 11/07 Q2 d, 07/03-boss Q4 a), JSON fidèle à
  `origin/main` ; existantes posées et retirées toutes justes.

| fichier | verdict |
| --- | --- |
| 09/07 | OK |
| 09/08 | OK (une précision facultative) |
| 09/09 | réserve mineure (explication de Q1) |
| 10/07 | OK |
| 11/07 | OK |
| 11/08 | OK |
| 11/09 | réserve mineure (un mot en Q4) |

**Verdict : livrable une fois les deux mineurs levés (deux remplacements de texte, sans effet sur clé, options ni figure) ;
la correction du cours 11 (hors lot) doit partir avant ou avec la publication.**
