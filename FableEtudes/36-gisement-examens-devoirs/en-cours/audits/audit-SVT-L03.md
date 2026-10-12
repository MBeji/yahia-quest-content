# Audit indépendant (aveugle) — lot SVT-L03, SVT 9ᵉ, chapitre `08-at-tanaffus`, missions 07 à 11

Auditeur : sous-agent indépendant, consigne `content-ingest/references/gisement-auditeur.md` + prompt `prompt-audit-SVT-L03.md`.
Périmètre : `content/sciences-vie-terre/08-at-tanaffus/exercices/07…11-*.json` (31 questions), arbre de travail du 2026-10-10 ~17:55 UTC ; reprise le 2026-10-11 ~10:00 UTC après coupure de session, fichiers audités inchangés (mtime 2026-10-10 17:34 à 17:51).
Méthode : chaque question re-résolue AVANT lecture de la clé (prompts et options extraits par script, clés masquées), puis comparaison ; figures comparées au PDF officiel ; nombres recalculés par script.

> Rapport écrit progressivement : une section par fichier dès qu'elle est terminée.

## État d'avancement

- [x] 07 (2025 ex.2) — section ci-dessous
- [x] 08 (2024 ex.2) — section ci-dessous (reprise du 2026-10-11 après coupure)
- [x] 09 (2020 ex.1) — section ci-dessous
- [x] 10 (2026 ex.4) — section ci-dessous ; section 07 révisée (M-07-2 : fuite Q4 → Q6, nouveau correctif)
- [x] 11 (2020 ex.4) — section ci-dessous
- [x] Transversal (étiquettes, doublons, rendu bidi, familles nouvelles)
- [x] Chiffre final — 31 questions, 0 clé fausse, 9 majeurs, 15 mineurs

---

## Fichier 07 — `07-examen-2025-ex2-structures-d-echange-cellule-et-equation.json` (2025 ex.2, d2 practice 75/15)

En-tête : titre `🏛️ مناظرة 2025 · التمرين 2 ⭐⭐: وظائف التغذية — بنيتان ثمّ خليّة وما يحيط بها` conforme (le sujet nomme les notions, aucun résultat) ; d2 / practice / 75 / 15 / displayOrder 7 conformes ; rampe 1,1,2,2,2,2 non décroissante. Étage d2 honnête (reconnaissance, fonction, propriétés, sens des échanges, nom et équation : rien d'élite).

| Q | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|
| 1 | b (خملة ؛ سنخ) | b | OK | 2×2 propre (chaque terme 2 fois, vote 2-2), d à deux erreurs muette ; clé la plus courte |
| 2 | d (امتصاص ؛ تبادل غازيّ) | d | OK, réserve mineure | 2×2 propre ; c mérite une étiquette existante (voir m-07-1) |
| 3 | a (جدار رقيق ؛ شبكة كثيفة) | a | **réserve majeure** | explication contraire au cours 05 (voir M-07-1) |
| 4 | c | c | OK | vote par substance : glucose 3-1 juste, O₂ 2-2, CO₂ 3-1 FAUX → ne reconstruit pas la clé |
| 5 | a | a | OK | étiquette b exacte |
| 6 | d | d | **défaut majeur** | doublon de fait du quiz publié Q8 et de 04-defi Q3, et pré-résolue par la correction de Q4 (voir M-07-2) |

Figures (rendues en Chromium, comparées au PDF C02 p. 2) : les quatre SVG sont fidèles. Doc 1 : villosité (une rangée de cellules épithéliales, vaisseau axial jaune, artère rouge, veine bleue, réseau en barreaux) et alvéole (sac + conduit à deux flèches d'air opposées, O₂/CO₂ dans le sac, capillaire à hématies, sang qui ENTRE en bas à droite et SORT en haut à gauche, comme le PDF) ; panneaux 1 à droite / 2 à gauche comme le sujet ; la flèche « مغذّيات خلويّة » est omise à juste titre. La variante neutre de Q2 n'a ni O₂/CO₂ ni flèches d'air : la figure ne livre pas la clé (mais voir m-07-3). Doc 2 (Q4) : courant de droite à gauche, CO₂ à gauche, O₂ au milieu, glucose (hexagone) à droite, aucune flèche d'échange — fidèle. Arabe seulement dans `<title>`, aucun élément interdit, `viewBox` présent.

Fidélité : aucune sous-question perdue (1 → Q1 ; 2a → Q2 ; 2b → Q3 ; 3a → Q4 ; 3b → Q5 et Q6). Arbitrage (2) de l'auteur : « السّنخ الرّئويّ » est le bon nom pour CETTE figure (un sac unique ceint d'un seul capillaire, exactement la figure du cours 08 « سنخ رئويّ محاط بشعيرة دمويّة », le cours réservant « حويصلة » à l'unité qui porte plusieurs أسناخ) ; aucune option ne dit « حويصلة », donc l'élève qui a appris ce mot n'est pas piégé : acceptable tel quel.

### Défauts

- **M-07-1 [MAJEUR] Q3, explication contraire au cours 05.** Elle affirme « كلّ من البنيتين تفصل ما يُتبادل عن الدّم بطبقة خلايا واحدة رقيقة » ; le cours 05 (origin/main, l. 302-303) enseigne l'inverse : « لا توجد بينهما إلّا **طبقتان** من الخلايا — الخلايا الماصّة (الظّهاريّة) وخلايا جدار الشّعيرات الدّمويّة » (0,05 mm). La clé (« جدار رقيق من طبقة خلايا واحدة ») reste défendable (c'est le mur PROPRE de chaque structure : l'épithélium de la villosité, une rangée dans la figure ; la paroi de l'alvéole), c'est l'explication qui enseigne un fait faux. Correctif exact (explication entière, vérifiée en Chromium) :
  « لكلّ من البنيتين جدار رقيق من طبقة خلايا واحدة: الخلايا الظّهاريّة في الخملة، وجدار السّنخ الذي لا يتجاوز سمكه 0,5 ميكرون. ولا يفصل ما يُتبادل عن الدّم إلّا هذا الجدار وجدار الشّعيرة: طبقتان من الخلايا في الخملة، نحو 0,05 مم. وتحيط بكلّ منهما أو تخترقها شبكة كثيفة من الشّعيرات الدّمويّة تقرّب الدّم من الوسط المتبادَل معه. أمّا الجدار السّميك العضليّ فمن خصائص القلب والشّرايين (دفع الدّم لا التّبادل)، وأمّا الجريان السّريع فمن خصائص الأوعية الكبيرة، والشّعيرات يبطؤ فيها الجريان فيطول زمن التّبادل. الخطأ الشائع: ظنّ أنّ الجريان السّريع أنجع للتّبادل. »
- **M-07-2 [MAJEUR] Q6, doublon de fait d'un quiz publié ET pré-résolue par la correction de Q4** *(section révisée à la reprise du 2026-10-11 : le correctif « chasse à l'erreur » proposé d'abord est RETIRÉ, voir plus bas)*. (i) Même tâche que le quiz publié Q8 (« ما معادلة الأكسدة الخلويّة؟ », d1) et que 04-defi Q3 (« ما معادلة التنفّس الخلويّ؟ »), même clé, mêmes pièges : équation renversée (quiz b ≈ 07 c), eau en réactif et O₂ en produit (quiz c ≈ 07 a), échange O₂/CO₂ (quiz d ≈ 07 b). (ii) Les missions corrigent chaque réponse aussitôt (retour immédiat) : la correction de Q4 (« الجليكوز والأكسيجين من الوعاء إلى الخليّة، وثنائي أكسيد الكربون من الخليّة إلى الوعاء ») range glucose et O₂ parmi les réactifs et CO₂ parmi les produits, ce qui élimine les trois distracteurs de Q6. Ce que ni Q4 ni la prémisse officielle (« تفاعل منتج للطّاقة ») ne donnent, c'est l'EAU en produit : c'est là qu'il faut faire porter la question. Correctif exact (vérifié par script et en Chromium ; clé `b`, la plus courte ; une seule lacune) :
  - `prompt` : « أكمل معادلة التفاعل المنتج للطّاقة داخل الخليّة :\nالجليكوز + الأكسيجين ← ثنائي أكسيد الكربون + … + طاقة »
  - a « البولة » · **b (clé) « الماء »** · c « الأزوت » · d « الجليكوجين » (toutes fausses : l'urée est un déchet toxique que le sang porte au rein — cours 06 ; l'azote ne participe pas — cours 08 ; le glycogène est la réserve du foie — cours 06 ; aucune n'est éliminable par Q4 ni par la prémisse)
  - `explanation` : « داخل الخليّة يُؤكسَد الجليكوز بالأكسيجين، فتتحرّر الطّاقة ويُطرح ناتجان: ثنائي أكسيد الكربون والماء. فالمعادلة الكاملة: الجليكوز + الأكسيجين ← ثنائي أكسيد الكربون + الماء + طاقة. وليست البولة من نواتج هذا التفاعل: هي فضلة سامّة يحملها الدّم إلى الكلية ولا تنتج عن أكسدة الجليكوز؛ والأزوت لا يشارك في التنفّس، فنسبته ثابتة في هواء الشّهيق وهواء الزّفير؛ والجليكوجين شكل يُخزَّن فيه الجليكوز في الكبد ولا يُطرح. الخطأ الشائع: نسيان الماء، وهو ناتج ثانٍ يرافق ثنائي أكسيد الكربون. »
  - Pourquoi l'ancien correctif est retiré : sa clé (« il manque l'énergie ») était donnée par la prémisse « منتج للطّاقة », et deux de ses distracteurs (O₂ en produit, CO₂ en réactif) tombaient devant la correction de Q4.
  - Limite assumée : la sous-question officielle demande d'ÉCRIRE toute l'équation ; la lacune n'en teste plus qu'un terme, le seul qui ne soit pas déjà livré par Q4 et par l'énoncé. Résidu : dans le donjon (tirage au hasard), l'équation montrée dans l'énoncé laisse déduire en un pas le sens des échanges de Q4 ; c'est le contenu même du cours et de la sous-question officielle, inévitable dès qu'on montre l'équation — moindre mal que l'état actuel, où Q4 livre Q6 sur la route quête. Si l'orchestrateur préfère garder « choisir l'équation », il faut l'assumer comme recoupement avec le quiz et accepter que Q4 la livre.
- **m-07-1 [mineur] Q2, option c muette** alors que l'explication nomme déjà l'erreur (« الخطأ الشائع: عدّ الامتصاص هضمًا ») et qu'elle n'en exécute qu'une (villosité = digestion enzymatique) : porte R1 → `bio.dig.absorption-dans-la-digestion` (même étiquette que l'auteur pose en 09 Q2 d). Option a : erreur « le poumon fabrique l'oxygène » sans entrée au registre (voir la section des familles nouvelles) ; b (deux erreurs) muette à juste titre.
- **m-07-2 [mineur] Q5 → Q6 (indice croisé, pas une fuite de clé)** : l'option d de Q5 (« التركيب الضوئيّ : صنع الجليكوز من ثنائي أكسيد الكربون والماء ») désigne d'avance l'équation renversée de Q6 comme celle de la photosynthèse ; avec le correctif M-07-2, elle rappelle seulement que l'eau entre dans la réaction inverse (indice faible, acceptable).
- **m-07-3 [mineur] Q1 → Q2, la variante neutre ne retient rien** : Q1, émise juste avant Q2, montre déjà O₂/CO₂ dans le sac et les flèches d'air (figure et légende de l'énoncé), donc oriente la fonction de la structure 2 (échange, pas « fabrication » d'O₂). Indice partiel hérité du sujet (le document 1 officiel porte ces mentions avant la question des fonctions) : acceptable, à savoir.

Notation et rendu (rendus via `splitMathRuns` du moteur `origin/main` en Chromium `dir=rtl`) : « O₂ وCO₂ », les équations en mots avec « ← » et « + », les parenthèses de prose : ordre affiché conforme à la source. Aucun chiffre arabo-indien, aucun LaTeX, aucune virgule arabe dans une notation.

**Verdict 07 : défaut majeur (2 majeurs : M-07-1, M-07-2) ; 0 clé fausse.**

---

## Fichier 08 — `08-examen-2024-ex2-coeur-circulation-et-echanges-gazeux.json` (2024 ex.2, d2 practice 75/15)

En-tête : titre `🏛️ مناظرة 2024 · التمرين 2 ⭐⭐: القلب والدّورتان الدّمويّتان والتبادلات الغازيّة اللّازمة للتنفّس` conforme ; d2 / practice / 75 / 15 / displayOrder 8 conformes ; rampe 2,2,2,2. Étage d2 honnête (reconnaissance, chaîne de stations, appariements).

| Q | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|
| 1 | b (1 = sigmoïde, 2 = auriculo-ventriculaire) | b | **défaut majeur** | c et d se réfutent d'elles-mêmes (voir M-08-1) |
| 2 (ordering) | c → e → a → d → b | c, e, a, d, b | OK, réserve mineure | suite unique, stations autonomes ; recoupe ch. 07 (m-08-1) |
| 3 (matching) | 1 → أوردة رئويّة, 2 → أجوفان, 3 → شريان رئويّ, 4 → أبهر | l1-r3, l2-r4, l3-r2, l4-r1 | **défaut majeur** | pré-résolue par la correction de Q2 + quasi-doublon de 07/08 Q2 (M-08-2) |
| 4 (matching) | O₂ alvéoles : air → sang ; CO₂ alvéoles : sang → air ; O₂ muscle : sang → cellules ; CO₂ muscle : cellules → sang | l1-r2, l2-r4, l3-r1, l4-r3 | OK | bijection unique ; chaque élément droit a deux partenaires plausibles |

**Arbitrage (1) de l'auteur — (أ)/(ب) sur le PDF.** J'ai zoomé le scan (C03 p. 2, image source à 240 ppi, rendue à 1200 dpi). La flèche (أ) bute au pied du vaisseau qui descend du poumon vers le cœur (l'artère pulmonaire, issue du ventricule droit), sur sa paroi gauche, à la hauteur où commence la languette auriculo-ventriculaire ; une petite pointe (valvule sigmoïde) est visible à droite du même orifice, au sommet de la cloison. La flèche (ب) bute sur la pointe libre de la longue languette pendue entre l'oreillette droite et le ventricule droit. La lecture de la transcription (« deux points de la même languette ») est possible à cette résolution mais rendrait la question officielle absurde (nommer CHACUN des deux éléments ET donner le rôle de chacun) ; la lecture de l'auteur (1 = sigmoïde à la base de l'artère pulmonaire, 2 = auriculo-ventriculaire droite) est la seule cohérente avec le cours 07 et avec la consigne, et le SVG refait la rend non ambiguë (flèche 1 sur les petites valvules à la base du tronc gauche, flèche 2 sur la languette de l'orifice gauche du dessin, côté cœur droit). **Accepté.** (Hors périmètre : la phrase de `2024.md` sur (أ)/(ب) mériterait d'être nuancée.)

Figures (Chromium + PDF) : cœur (Q1) vrai — quatre cavités, ventricule gauche plus épais, valvules sigmoïdes à la base des deux artères, auriculo-ventriculaires aux deux orifices, cœur droit à gauche du dessin ; rien ne désigne la clé. Schéma des deux circulations (Q3) vrai : 1 poumon → oreillette du côté droit du dessin, 2 muscle → oreillette du côté gauche, 3 ventricule du côté gauche → poumon, 4 ventricule du côté droit → muscle. Les deux figures passent intactes le filtre DOMPurify du moteur (`marker` compris). Débordement mesuré (m-08-3).

### Défauts

- **M-08-1 [MAJEUR] Q1, deux distracteurs qui se contredisent eux-mêmes.** Le plan 2×2 croise le NOM et le RÔLE, or le nom porte le rôle : « صمّام أذينيّ-بطينيّ يمنع رجوع الدّم من الشّريان إلى البطين » (élément 2 de c, élément 1 de d) se réfute à la lecture du mot « أذينيّ-بطينيّ », et la sigmoïde « يمنع رجوع الدّم من البطين إلى الأذينة » contredit le cours 07 (« صمّامات سينيّة … في قاعدة كلّ شريان »). c et d tombent sans figure ni connaissance du cœur ; la question se joue à pile ou face entre a et b. Correctif exact (vérifié : chaque valeur de case deux fois — identification {1 = sigmoïde : b, c ; 1 = AV : a, d}, rôle {« يمنع رجوع » : a, b ; « يدفع بانقباضه » : c, d} ; d à deux erreurs, muette ; longueurs 132 / 132 / 140 / 140, la clé n'est pas la plus longue ; chaque option cohérente avec la position de sa valvule ; rendu Chromium conforme) :
  - c → « العنصر 1 : صمّام سينيّ يدفع بانقباضه الدّم من البطين إلى الشّريان ؛ العنصر 2 : صمّام أذينيّ-بطينيّ يدفع بانقباضه الدّم من الأذينة إلى البطين »
  - d → « العنصر 1 : صمّام أذينيّ-بطينيّ يدفع بانقباضه الدّم من الأذينة إلى البطين ؛ العنصر 2 : صمّام سينيّ يدفع بانقباضه الدّم من البطين إلى الشّريان »
  - `explanation` → « العنصر 1 عند قاعدة الشّريان الذي يخرج من البطين الأيمن: صمّام سينيّ هلاليّ الشّكل، يسمح بمرور الدّم من البطين إلى الشّريان ويمنع رجوعه إلى البطين. والعنصر 2 عند الفتحة بين الأذينة اليمنى والبطين الأيمن: صمّام أذينيّ-بطينيّ، يسمح بمرور الدّم من الأذينة إلى البطين ويمنع رجوعه إلى الأذينة عند انقباض البطين. فلكلّ صمّام اسم موضعه ودور واحد: فرض اتّجاه واحد على الدّم. الخطأ الشائع: تبديل الاسمين بين الموضعين، أو جعل الصّمّام مضخّة: الصّمّام لا ينقبض ولا يدفع الدّم، بل ينفتح وينغلق، والدّفع من انقباض الأذينتين والبطينين. » (le début ne nomme plus « الشّريان الرّئويّ », maillon de la chaîne de Q2.)
- **M-08-2 [MAJEUR] Q3, pré-résolue par Q2 et quasi-doublon de 07/08 Q2.** (i) Les missions corrigent chaque réponse aussitôt (retour immédiat, levier 01) : après Q2, l'élève a sous les yeux l'ordre juste et l'explication « … يخرج بالشّريان الرّئويّ … وتعود به الأوردة الرّئويّة إلى الأذينة اليسرى … الشّريان الأبهر … الوريدين الأجوفين … الأذينة اليمنى » ; il ne lui reste qu'à lire « haut = oreillette, bas = ventricule » sur le schéma. (ii) La publiée 07/08 Q2 (2020 ex.3) apparie déjà les mêmes quatre noms (أبهر، شريان رئويّ، أوردة رئويّة، أجوفان) à quatre vaisseaux définis par leurs attaches, avec la même règle (« الشريان يُعرّف بالاتّجاه ») et le même piège : seule change la présentation des vaisseaux (numéros sur un dessin au lieu de mots). Et l'adaptation s'écarte de la tâche officielle (« أتمم … رسم الدّورة الدّمويّة الصغرى والكبرى » : COMPLÉTER un dessin incomplet). Correctif exact — revenir au dessin incomplet du sujet, cavités lettrées, QCM 2×2 (vérifié par script : A 2×, C 2×, D 2×, B 2× ; quatre options de 79 caractères ; rendu Chromium conforme ; figure passée au filtre DOMPurify, sans débordement) :
  - figure : partir du SVG actuel de Q3 et (1) RETIRER les deux `<path d="M212 84 L212 142" …/>` (veines pulmonaires) et les deux `<path d="M246 216 L280 216 L280 298 L236 298" …/>` (aorte) ; (2) RETIRER les quatre repères `<circle … r="10" …/><text …>1…4</text>` ; (3) AJOUTER avant `</svg>` : `<g font-size="16" font-weight="700" fill="#0f172a" text-anchor="middle"><text x="88" y="170">A</text><text x="100" y="236">B</text><text x="211" y="170">C</text><text x="198" y="236">D</text></g>` ; (4) `<title>` → « رسم مبسّط غير مكتمل لدوران الدّم: الرّئتان في الأعلى، والقلب في الوسط بتجاويفه الأربعة المرموز إليها بالحروف A وB وC وD، والعضلة في الأسفل؛ لم يُرسم إلّا وعاءان: وعاء يصل التجويف B بإحدى الرّئتين، ووعاء يصل العضلة بالتجويف A ». Rien n'est déplacé (A = oreillette du côté gauche du dessin, B = ventricule sous elle, C et D en face).
  - `type` → `mcq` ; `prompt` → « يمثّل الرسم التالي رسمًا مبسّطًا غير مكتمل لدوران الدّم: الرّئتان في الأعلى، والقلب في الوسط ورُمز إلى تجاويفه الأربعة بالحروف A وB وC وD، والعضلة في الأسفل. لم يُرسم إلّا وعاءان: وعاء يصل التجويف B بالرّئة، ووعاء يصل العضلة بالتجويف A.\nلإتمام رسم الدّورتين الصّغرى والكبرى، بين أيّ عنصرين يُرسم كلّ من الوعاءين النّاقصين ؟ » + figure
  - a « الأوردة الرّئويّة بين الرّئة والتجويف A ؛ الشّريان الأبهر بين التجويف D والعضلة » (`bio.circ.oreillettes-inversees`, une seule erreur, libellé exact) · **b (clé)** « الأوردة الرّئويّة بين الرّئة والتجويف C ؛ الشّريان الأبهر بين التجويف D والعضلة » · c « الأوردة الرّئويّة بين الرّئة والتجويف C ؛ الشّريان الأبهر بين التجويف B والعضلة » (muette : aucune étiquette exacte) · d « الأوردة الرّئويّة بين الرّئة والتجويف A ؛ الشّريان الأبهر بين التجويف B والعضلة » (deux erreurs, muette)
  - `explanation` → « الوعاء الآتي من العضلة يصبّ في التجويف A: هو وريد أجوف، فالتجويف A هو الأذينة اليمنى، والتجويف B تحتها هو البطين الأيمن الذي يخرج منه الشّريان الرّئويّ نحو الرّئة. فالقلب الأيمن على يسار الرّسم، والقلب الأيسر على يمينه: التجويف C هو الأذينة اليسرى والتجويف D هو البطين الأيسر. ولإتمام الدّورة الصّغرى تُرسم الأوردة الرّئويّة من الرّئة إلى الأذينة اليسرى C، ولإتمام الدّورة الكبرى يُرسم الشّريان الأبهر من البطين الأيسر D إلى العضلة. الخطأ الشائع: إيصال الأوردة الرّئويّة بالأذينة اليمنى، أو إخراج الأبهر من البطين الأيمن، كأنّ القلب مضخّة واحدة. »
  - Contrôles : aucune option réfutable à l'œil (une oreillette reçoit plusieurs veines, rien n'interdit à l'œil un second départ de B) ; prémisses vraies ; la correction de Q2 donne encore « veines → oreillette gauche », mais il reste la lecture du dessin (repérer l'oreillette gauche à partir de l'arrivée du vaisseau venu du muscle) — c'est précisément la compétence de l'item officiel ; aucun doublon publié (07/08 Q2 nomme des vaisseaux, 07/01-tamrin Q5 et 07/03-boss Q3 sont des QCM de mots sans figure).
- **m-08-1 [mineur] Q2 recoupe le chapitre 07** : même chaîne et même piège (« القلب مضختان منفصلتان ») que la publiée 07/08 Q4 (ordering des stations de la double circulation) et que le quiz 07 Q6 (trajet d'une hématie depuis la veine cave jusqu'à l'aorte). Pas quasi identique (stations et bornes différentes, vaisseaux intégrés) : recoupement assumé de deux annales, à garder.
- **m-08-2 [mineur] Q1, explication → Q2** : « عند قاعدة الشّريان الرّئويّ حيث يخرج من البطين الأيمن » livre un maillon de la chaîne de Q2 (cœur droit → artère pulmonaire). Corrigé dans le texte de M-08-1.
- **m-08-3 [mineur, cosmétique] figure de Q1** : les capuchons ronds des deux troncs supérieurs (`M31 -18 L31 34`, `M169 -18 L169 34`, deux couches chacun) débordent du `viewBox` de 2 unités (4,3 px mesurés à 600 px de large). Correctif sans déplacement : `stroke-linecap="butt"` sur ces quatre chemins.

Étiquettes : aucune posée (Q2 à Q4 ne s'étiquettent pas ; les options de Q1 n'ont pas d'étiquette exacte). Rendu : rien à signaler (« 1 و2 », « أذينيّ-بطينيّ », le point-virgule arabe entre deux membres de prose).

**Verdict 08 : défaut majeur (2 majeurs : M-08-1, M-08-2) ; 0 clé fausse.**

---

## Fichier 09 — `09-examen-2020-ex1-qcm-pouls-enzymes-oxygene-milieu-interieur.json` (2020 ex.1, d2 practice 75/15)

En-tête : titre `🏛️ مناظرة 2020 · التمرين 1 ⭐⭐: أسئلة اختيار من متعدّد — النبض والأنزيمات الهاضمة ونقل الأكسيجين والوسط الداخليّ` conforme ; d2 / practice / 75 / 15 / displayOrder 9 conformes ; rampe 1,2,2,2. Étage d2 honnête (QCM de rappel). Programme : pouls et milieu intérieur (ch. 07), enzymes (ch. 05), transport de l'O₂ (ch. 06 et 08) — tous antérieurs ou égaux à 08 ; « الأقسومة الوعائيّة / الخلاليّة / الخلويّة » est enseigné au cours 07 ; « الكربوكسي هيموغلوبين » = forme de transport du CO₂ dans le cours 08, comme dans l'explication de Q3 (aucune contradiction).

| Q | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|
| 1 | c (نسق دقّات القلب) | c | OK | options officielles conservées |
| 2 | a (تيسير مفعول الماء…) | a | OK, réserve mineure | étiquette de c inexacte (m-09-1) |
| 3 | d (متّحدًا بالهيموغلوبين) | d | **défaut majeur** | deux distracteurs tombent sans la notion (M-09-1) |
| 4 | b (الوعائيّة والخلاليّة) | b | **défaut majeur** | la clé est la seule option sans qualificatif absolu (M-09-2) |

Fidélité : les quatre items du QCM officiel sont là, options officielles reprises (ordre changé). Modifications déclarées : Q3 a et b, Q4 a, c (« وحده/وحدها ») et d (liste explicite) — chacune rend bien une seule réponse juste ; mais deux d'entre elles créent un indice de forme (ci-dessous). Q3 garde « الكربوكسي هيموغلوبين » (option officielle), faux pour l'O₂ selon le cours 08.

### Défauts

- **M-09-1 [MAJEUR] Q3, deux distracteurs éliminés sans la notion.** a « منحلًّا في البلازما وحدها دون ناقل » porte le seul absolu de la question (« وحدها دون ناقل ») ; b « بواسطة خلايا الدّم البيضاء المقاومة للجراثيم » porte sa propre réfutation (la glose dit à l'élève que ces cellules combattent les microbes). Reste un pile-ou-face c/d. Correctif exact (vérifié : longueurs a 50, b 46, c 33, d 36 — la clé n'est pas la plus longue ; aucune option ne devient vraie ; rendu Chromium conforme ; « هيموغلوبين » figure dans a, c et d, pas de marqueur propre à la clé) :
  - a → « منحلًّا أغلبُه في البلازما، وقليله مع الهيموغلوبين » — proportions renversées : exécute EXACTEMENT `bio.sang.plasma-transporte-l-oxygene` (« l'essentiel de l'oxygène »), à garder ;
  - b → « بواسطة الكريّات البيضاء التي تحمله إلى الخلايا » — `bio.sang.fonctions-des-cellules-confondues` reste exacte.
  L'explication actuelle convient telle quelle (elle nomme déjà « ظنّ أنّ البلازما تنقل أغلب الأكسيجين »).
- **M-09-2 [MAJEUR] Q4, la clé est la seule option « non absolue ».** a « …وحدها », c « …وحده », d « كافّة الأقاسيم… » : l'élève rusé écarte les trois absolus et tombe sur b sans rien savoir du milieu intérieur (« وحدها » n'était d'ailleurs pas nécessaire en a : la seule « الأقسومة الخلويّة » est déjà fausse). Correctif exact, une seule retouche (vérifiée : vraie selon le cours 07 — « الأقسومة خارج الخلويّة … وهي الوسط الدّاخليّ ؛ وتشمل … الوعائيّة … والخلاليّة » ; longueurs a 23, b 45, c 20, d 62) :
  - b (clé) → « الأقسومة الوعائيّة والأقسومة الخلاليّة وحدهما » — le qualificatif figure alors dans la clé et dans deux distracteurs, d garde « كافّة ».
- **m-09-1 [mineur] Q2 c, étiquette inexacte.** « تفكيك مختلف أنواع الأغذية المعدنيّة والعضويّة » : collectivement, les enzymes défont bien plusieurs sortes d'aliments ORGANIQUES ; ce que l'option fait de faux, c'est digérer les aliments MINÉRAUX (« لا تُهضم »). `bio.dig.specificite-enzyme-ignoree` (« une enzyme sur n'importe quel aliment… chacune son substrat ») ne nomme pas cette erreur : à retirer (muette ; aucune étiquette existante pour « les minéraux se digèrent »).
- **Cas limite demandé — Q2 b `bio.dig.fragmentation-prise-pour-digestion`** : l'élève qui prête aux enzymes le broyage mécanique confond le mécanique et le chimique, la confusion même que nomme le libellé (« croire que broyer simplifie ») et que portent ses placements publiés (« لأنّ التّقطيع يهضم اللّحم », « تفتيت الغذاء بالأسنان », « أنّ المعدة تطحن اللّحم بتقلّصاتها ») : **acceptée**. Q2 d (`bio.dig.absorption-dans-la-digestion`) : exacte.
- **m-09-2 [mineur] recoupements publiés (assumés, annales voisines)** : Q2 ≈ 05/02-tamrin Q1 (« ما دور الأنزيم في الهضم الكيميائيّ بدقّة؟ », même clé « ييسّر مفعول الماء », même distracteur « يفتّت الغذاء ميكانيكيًّا ») ; Q4 ≈ 07/04-defi Q1 (« ممّ يتكوّن الوسط الدّاخليّ؟ ») et 07/07 Q2 (2024 ex.1). Options différentes (compartiments contre liquides ; minéraux et absorption en plus) : pas quasi identiques, à garder comme reprises officielles.

Rendu : rien à signaler (aucune formule ; « 98,5 % » et « 1,5 % » dans les explications passent). Étiquettes posées : Q2 b exacte (cas limite accepté), Q2 c à retirer, Q2 d exacte, Q3 a et b exactes (et le restent avec le correctif). Options muettes : Q1 (aucune étiquette existante ne convient), Q3 c (confusion des deux hémoglobines : sans entrée), Q4 (aucune).

**Verdict 09 : défaut majeur (2 majeurs : M-09-1, M-09-2) ; 0 clé fausse.**

---

## Fichier 10 — `10-examen-2026-ex4-experiences-tableaux-histogrammes-echanges-gazeux-musculaires.json` (2026 ex.4, d4 challenge 300/60)

En-tête : titre `🏛️ مناظرة 2026 · التمرين 4 ⭐⭐⭐⭐: تجارب وجداول ومدرّجات حول التبادلات الغازيّة والجليكوز في العضلة` conforme ; d4 / challenge / 300 / 60 / displayOrder 10 conformes ; rampe 2,3,3,3,3,3,3,3,3. **Étage** : d4 est au bord haut mais tient — chaîne de neuf étapes sur quatre documents (même calibrage que la publiée 05/08, 2022 ex.4, d4 à 9 questions) ; l'élite repose sur Q2 (volume + fixation du CO₂ → O₂ consommé), Q3 (logique du témoin) et Q9 (synthèse) ; Q4 à Q8 sont des lectures/calculs à plusieurs parties, d3 défendable (Q5 et Q7 frôlent le d2).

| Q | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|
| 1 | c (la fraîche a rejeté du CO₂) | c | OK, réserve mineure | libellé « صار … داكنًا » (m-10-1) ; étiquette b acceptée |
| 2 | b (O₂ consommé, CO₂ fixé) | b | **défaut majeur** | clé repérable par la forme (M-10-1) |
| 3 | d (cellules vivantes) | d | OK | étiquette a exacte |
| 4 | a (1 %) | a | OK | 1,5 ÷ 150 = 0,01 recalculé ; étiquettes b, c, d exactes |
| 5 | c (O₂ : hématies ; CO₂ : plasma) | c | OK | 2×2 propre (chaque valeur 2×, b muette) ; d exacte |
| 6 | d (50/180 ; 40/160) | d | OK | 2×2 propre ; b, c exactes ; a (deux erreurs) muette |
| 7 | d | d | OK, réserve mineure | étiquette c inexacte (m-10-2) |
| 8 | a (0,20 contre 0,08) | a | OK | 0,92 − 0,84 = 0,08 ; 0,92 − 0,72 = 0,20 ; ×2,5 ; b exacte |
| 9 | b | b | **défaut majeur** | l'énoncé livre la clé de Q7 (M-10-2) |

Nombres recalculés par script : O₂ 3 + 197 = 200 et 1,5 + 148,5 = 150 ; 1,5 ÷ 150 = 1 % (3 ÷ 200 = 1,5 %, 148,5 ÷ 150 = 99 %) ; CO₂ 318,5 + 171 = 489,5 ≈ 490 et 350 + 180 = 530 (sommes du tableau = barres « sang entrant / sortant au repos » de l'histogramme) ; part du plasma 65,1 % et 66,0 % (« نحو ثلثيه » juste) ; écarts 200 − 150 = 50, 200 − 20 = 180, 530 − 490 = 40, 650 − 490 = 160 ; glucose 0,08 et 0,20, rapport 2,5. Toutes les données sont celles de `2026.md` et du PDF (C01 p. 3-4).

Figures (Chromium + PDF) : expérience 1 (Q1 et Q2, même SVG) fidèle — à droite le début, à gauche la fin, flèche vers la gauche comme le sujet ; eau de chaux sombre à la fin, liquide coloré monté dans la branche verticale du tube capillaire, niveau du bécher abaissé ; expérience 2 (Q3) : les deux états identiques (muscle bouilli, rien ne bouge). Histogrammes (Q7) : à droite repos (200/490 ; 150/530), à gauche activité (200/490 ; 20/650), comme le PDF ; barres à l'échelle (rapports mesurés 650/490 = 1,33, 150/200 = 0,76 …) et valeurs imprimées ; groupes ① ② définis dans l'énoncé. Rien ne désigne une clé ; arabe seulement dans `<title>` ; filtre DOMPurify intact ; aucun débordement.

Programme : eau de chaux (6ᵉ éveil et SVT 7ᵉ — et rappelée dans Q1 et Q2) ; muscle bouilli = cellules mortes (donné dans Q3) ; témoin (cours 05 « الشّاهدان » et cours 08 pour l'azote) ; débit sanguin (cours 08, « الصّبيب ») ; pourcentage (maths) ; histogramme à deux séries (valeurs imprimées, légende). Rien n'est hors programme ; aucun fait ne contredit le cours (le CO₂ « أساسًا بالبلازما » de Q5 est celui du cours 08).

### Défauts

- **M-10-1 [MAJEUR] Q2, la clé est l'intruse de forme.** Les trois distracteurs finissent par la même proposition « …فنقص حجم الغاز في الوعاء » ; seule la clé ne la porte pas, et seule elle reprend le rappel de l'énoncé (« ماء الجير ثبّته »). Le candidat rusé choisit l'option qui ne ressemble pas aux autres et qui recopie l'énoncé. Correctif exact (vérifié : la queue commune dans les quatre options, « ماء الجير » dans b et c ; longueurs 84 / 102 / 101 / 108, la clé n'est pas la plus longue ; aucune option ne devient vraie ; rendu Chromium conforme ; l'explication actuelle reste juste) :
  - a (inchangée) « الأزوت : استهلكته العضلة لأنّه أكثر غازات هواء الوعاء وفرة، فنقص حجم الغاز في الوعاء »
  - **b (clé)** → « الأكسيجين : استهلكته العضلة، وثبّت ماء الجير ما طرحته من ثنائي أكسيد الكربون، فنقص حجم الغاز في الوعاء »
  - c → « ثنائي أكسيد الكربون : استهلكته العضلة، وثبّت ماء الجير ما بقي منه في الهواء، فنقص حجم الغاز في الوعاء » (toujours fausse : le muscle rejette le CO₂)
  - d → « الأكسيجين وثنائي أكسيد الكربون : استهلكتهما العضلة معًا بالقدر نفسه من هواء الوعاء، فنقص حجم الغاز في الوعاء »
- **M-10-2 [MAJEUR] Q9, l'énoncé livre la clé de Q7.** « في عضلة تنتقل من الرّاحة إلى النّشاط ينخفض تركيز الجليكوز وتركيز الأكسيجين … أكثر ممّا كان، ويرتفع تركيز ثنائي أكسيد الكربون … أكثر ممّا كان » réfute d'avance a et b de Q7 et oriente vers d (l'activité intensifie les deux échanges) ; la route quête est protégée (Q9 vient après Q7), pas le donjon, qui tire au hasard. La relation demandée (respiration cellulaire dans les cellules) n'a pas besoin du contraste repos/activité. Correctif exact (vérifié : longueurs 90 / 106 / 77 / 111, la clé n'est pas la plus longue ; rendu Chromium conforme) :
  - `prompt` → « يدخل الدّم عضلةً ويخرج منها وقد انخفض فيه تركيز الجليكوز وتركيز الأكسيجين، وارتفع فيه تركيز ثنائي أكسيد الكربون.\nما العلاقة التي تفسّر هذه التّغيّرات الثّلاثة معًا ؟ »
  - c → « يتسارع جريان الدّم في العضلة فتتغيّر التّراكيز الثّلاثة دون أن تتدخّل خلاياها »
  - `explanation` : supprimer la phrase « وتشتدّ معًا لأنّ النّشاط يرفع حاجة العضلة إلى الطّاقة. » (même fuite vers Q7 une fois la réponse corrigée) ; le reste est juste.
- **m-10-1 [mineur] Q1, « صار ماء الجير داكنًا »** : le cours de 7ᵉ enseigne que l'eau de chaux « يتكدّر (يصبح أبيض عكرًا) » ; le noir est une convention du dessin officiel. Correctif : « وقد صار ماء الجير داكنًا في الرسم الأيسر. » → « وقد رُسم ماء الجير داكنًا في الرسم الأيسر دلالةً على تعكّره. » (vérifié en Chromium).
- **m-10-2 [mineur] Q7 c, étiquette inexacte (cas limite demandé).** `bio.lecture.valeur-d-une-autre-grandeur` dit « Tu donnes une valeur juste, mais d'une autre grandeur » ; c ne donne aucune valeur, elle tire une conclusion fausse d'une concentration de sortie prise pour une consommation — la même faute que b (concentration d'entrée prise pour l'effet) et que Q8 d, toutes deux muettes. À retirer (ou alors étiqueter les trois, ce que le libellé ne permet pas). Cas limite Q1 b (`bio.demarche.cause-sans-temoin`, « la température a troublé l'eau de chaux ») : **accepté** — l'élève accuse un facteur qu'aucune comparaison n'accuse, exactement comme les placements publiés « أنّ الحرارة وحدها تهضم اللّحم », « الحرارة 37 درجة وحدها فكّكت سكّر الشّعير ».
- **m-10-3 [mineur] Q2 a, option muette voisine d'une étiquette** : « الأزوت : استهلكته العضلة » est la croyance que portent les placements publiés de `bio.resp.azote-constant-lu-comme-erreur` (« أنّ الأزوت يُستهلك… ») ; mais le libellé suppose la lecture d'un 79 % constant que cet énoncé ne donne pas : la laisser muette est défendable.
- **m-10-4 [mineur] recoupements assumés** : Q6 refait sur les mêmes données (×10) le calcul de l'exemple travaillé du cours 08 (« استهلاك 20 − 15 = 5 … 65 − 49 = 16 ») et, pour l'O₂, le quiz Q9 et 04-defi Q5 ; Q5 recoupe 04-defi Q1-Q2 et 09 Q3 (transport de l'O₂). Options et forme différentes (données à lire, plan 2×2) : pas quasi identiques. Vérification demandée par l'auteur : **Q9 n'est pas un doublon** du quiz Q8 ni de 04-defi Q3 (mécanismes en mots, pas d'équation à choisir).

Fuites dans l'ordre d'émission (retour immédiat) : Q1 → Q2 (la correction de Q1 écarte c et d de Q2, mais l'énoncé et la figure de Q2 portent déjà l'eau de chaux troublée) ; Q4 → Q5 (moitié O₂, déjà lisible dans les données de Q5) ; Q6 → Q7 (Q7 est la conclusion des comparaisons de Q6, hérité du sujet 3-أ/ب → 3-ج, et la figure de Q7 porte les mêmes valeurs) : enchaînements du sujet, aucune clé livrée au-delà des données propres de la question suivante.

Rendu : vérifié en Chromium via `splitMathRuns` ; options « 1 % », « 1,5 % » posées LTR par le moteur (`isMathExpression`) ; chaînes « 200 − 150 = 50 », « 0,92 − 0,84 = 0,08 » rendues nativement dans l'ordre de lecture arabe ; « (0,20 ÷ 0,08) », « (3 ÷ 200) » isolées. Rien à signaler.

**Verdict 10 : défaut majeur (2 majeurs : M-10-1, M-10-2) ; 0 clé fausse.**

---

## Fichier 11 — `11-examen-2020-ex4-besoins-energetiques-repas-courbes-et-production-d-energie.json` (2020 ex.4, d4 challenge 300/60)

En-tête : titre `🏛️ مناظرة 2020 · التمرين 4 ⭐⭐⭐⭐: الحاجيّات الطّاقيّة — وجبتان غذائيّتان ومنحنيات وجدول وتفسير إنتاج الطّاقة` conforme (« التمرين 4 » = numérotation de la transcription pour la partie II non numérotée) ; d4 / challenge / 300 / 60 / displayOrder 11 conformes ; rampe 2,2,3,3,3,3,3,3. **Étage** : d4 tient par la chaîne de huit étapes (calcul, jugement quantitatif puis qualitatif, conseils, courbes, tableau, mécanisme), même calibrage que 05/08 ; Q3, Q4, Q5 sont de vrais d3 ; Q6, Q7 et Q8 (surtout après M-11-1, simple rappel du mécanisme) relèvent plutôt du d2 — sans conséquence sur la clé, la retouche de leurs difficultés est facultative.

| Q | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|
| 1 | c (3020) | c | OK | 1500 + 1260 + 260 ; a, b, d exactes |
| 2 | b (720) | b | OK | 3020 − 2300 ; a, c, d exactes |
| 3 | a | a | OK, réserve mineure | c et d mériteraient une étiquette (m-11-3) |
| 4 | d (≈ 42 % / 9 % / 50 %) | d | OK | b et c exactes |
| 5 | c | c | OK | 2×2 propre (chaque conseil 2×, d à deux erreurs muette) ; b exacte |
| 6 | b | b | OK | lecture de courbes |
| 7 | a | a | OK, réserve mineure | « تتضاعف السّرعة مرّتين » ambigu (m-11-1) |
| 8 | c (oxydation progressive) | c | **défaut majeur** | l'énoncé livre les clés de Q7 et de Q6 (M-11-1) |

Nombres recalculés par script : repas 1 = 375 × 4 + 140 × 9 + 65 × 4 = 1500 + 1260 + 260 = 3020 ; repas 2 = 1200 + 900 + 200 = 2300 ; écart 720 (par classes : 300 + 360 + 60) ; distracteurs : masses 580 et écart 130, « 4 pour tout » 2320 et 520, valeurs échangées 4195 (et 3300) donc écart 895 ; parts du repas 1 : 49,7 / 41,7 / 8,6 % (clé « نحو 50 / 42 / 9 % » juste), part MASSIQUE des glucides 64,7 % (« نحو 65 % » de b) ; parts du repas 2 : 52,2 / 39,1 / 8,7 % (les conseils de c pour le jeune 2 — moins de lipides, plus de protides — sont donc fondés) ; tableau : O₂ × 2,75 et énergie × 2,38 quand la vitesse double, ≈ 5 kcal par litre d'O₂ (5,25 ; 5,0 ; 4,55). Données conformes à `2020.md` et au PDF (C06 p. 3-4).

**Courbes (demande de l'auteur), mesurées au pixel sur le PDF à 600 dpi** (graduations 150/300/450/600 repérées, 1 px ≈ 1 unité) : départ commun ≈ 50 (extrapolation des trois segments : 47 à 53) ; courbe 3 ≈ 588 à la minute 10 (juste sous la graduation 600) et ≈ 640 à la minute 20 ; courbe 2 = 300 puis ≈ 343-345 ; courbe 1 = 150, palier. Le SVG trace 55 (départ), 148 → 152, 300 → 345, 592 → 640 : fidèle (départ un peu haut, dans la marge de « نحو 50 ») ; axes, graduations, trait intermédiaire à la minute 5, origine des ordonnées non graduée, styles tireté / pointillé / plein comme le sujet ; unités en notation SI (« mg/min », « min ») et arabe seulement dans `<title>` ; DOMPurify intact ; aucun débordement. L'énoncé dit « نحو 150 و300 و600 » à la minute 10 : juste.

Programme : valeurs 4/9/4 kcal/g, besoins (3000 kcal pour 16 ans dans le cours 04), proportions « نحو النّصف / الثّلث / الخمس » (cours 04) ; le besoin de 3000 kcal est bien redonné dans Q3 et Q5 (seules à l'employer ; Q4 c le cite sans chiffre, sans que sa fausseté en dépende) ; respiration cellulaire (cours 08). Rien d'hors programme ; aucun fait contraire au cours.

### Défauts

- **M-11-1 [MAJEUR] Q8, l'énoncé livre les clés de Q7 et de Q6.** « عند ممارسة نشاط عضليّ يرتفع في العضلة استهلاك الجليكوز واستهلاك الأكسيجين وتزداد الطّاقة المنتَجة » est la conclusion de Q7 (clé a : O₂ et énergie montent ensemble) et une moitié de celle de Q6 (« تكبر كلّما اشتدّ النّشاط ») ; la route quête est protégée (Q8 est la dernière), pas le donjon. Et l'explication renvoie à des documents absents de la question (« كما بيّن الجدول والمنحنيات »). La question officielle (expliquer la production d'énergie dans les cellules) n'a pas besoin de ces données. Correctif exact (vérifié en Chromium ; options inchangées, longueurs 96 / 84 / 97 / 97) :
  - `prompt` → « كيف تُنتَج الطّاقة في مستوى خلايا الجسم ؟ »
  - `explanation` : supprimer la phrase « ولهذا ترتفع الطّاقة المنتَجة مع استهلاك الجليكوز والأكسيجين معًا في النّشاط العضليّ، كما بيّن الجدول والمنحنيات. » ; le reste est juste.
- **m-11-1 [mineur] Q7, explication** : « بين 4 و8 كيلومترات تتضاعف السّرعة مرّتين » peut se lire « double deux fois » (× 4) et oublie « في السّاعة ». Correctif : « بين 4 و8 كيلومترات تتضاعف السّرعة مرّتين بينما » → « من 4 إلى 8 كيلومترات في السّاعة تتضاعف السّرعة، بينما » (vérifié en Chromium).
- **Question (4) de l'auteur — « 4 kcal/g pour les trois classes » (Q1 b, Q2 c) sous `bio.alim.valeurs-energetiques-confondues`** : **exact**. L'erreur exécutée est « le gramme de lipides compté à 4 », que le libellé corrige en toutes lettres (« 1 غ دهنيّات = 9 ») et que le registre étiquette déjà ainsi (04/02-tamrin Q1 a « 4 » pour les lipides, quiz 04 « 4 كيلو حريرة »). Remarque de registre, facultative : le libellé arabe dit « تخلط » (confondre), le français « Tu échanges » / l'anglais « You swap » sont plus étroits que l'usage — « Tu confonds » / « You mix up » le couvriraient exactement. Q1 d et Q2 a (valeurs échangées) : exactes.
- **[info] étiquettes déjà posées, toutes exactes** : Q1 a et Q2 d (masse au lieu d'énergie), Q4 b (part massique au lieu de part énergétique) → `bio.lecture.valeur-d-une-autre-grandeur` ; Q4 c et Q5 b (juger au seul total) → `bio.alim.quantite-sans-qualite` ; Q8 a (combustion) → `bio.resp.respiration-combustion`.
- **m-11-3 [mineur] Q3, c et d muettes alors que la porte R1 est ouverte** : l'explication nomme l'erreur et ce qu'elle produit (« الخطأ في الحساب بتطبيق قيمة واحدة على الأصناف أو تبديل القيم بينها فتبدو الوجبتان كلتاهما دون الحاجة أو فوقها ») : « les deux sous 3000 » (c) sort du « 4 pour tout » (2320 et 1800), « les deux au-dessus » (d) des valeurs échangées (4195 et 3300) → `bio.alim.valeurs-energetiques-confondues` sur c et d.
- **m-11-4 [mineur] recoupements dans la tranche (pas quasi identiques)** : Q8 reprend l'idée-clé de 07 Q5 (« أكسدة تدريجيّة ») avec deux pièges voisins (combustion étiquetée, enzymes digestives) et un piège de 10 Q9 (« le glucose sert à bâtir le muscle ») ; Q6 et 10 Q8 montrent tous deux que la consommation de glucose croît avec l'activité (données et représentations différentes). Angles distincts, à garder ; la respiration cellulaire revient en tout quatre fois dans la tranche (07 Q5, 07 Q6, 10 Q9, 11 Q8).

Rendu : vérifié (ordre visuel calculé caractère par caractère en Chromium) — « (375 + 140 + 65) × 4 = 2320 », « (75 + 40 + 15) × 4 = 520 », « (50 %) », « (580) » s'affichent dans l'ordre source ; les chaînes « 375 × 4 = 1500 » restent natives (lecture arabe correcte). Rien à signaler.

**Verdict 11 : défaut majeur (1 majeur : M-11-1) ; 0 clé fausse.**

---

## Transversal

### Étiquettes — bilan des 26 placements de l'auteur (libellés lus sur `origin/main`)

| étiquette | placements | verdict |
|---|---|---|
| `bio.resp.respiration-combustion` | 07 Q5 b, 11 Q8 a | exactes |
| `bio.dig.fragmentation-prise-pour-digestion` | 09 Q2 b | acceptée (cas limite, même confusion mécanique/chimique que ses placements publiés) |
| `bio.dig.specificite-enzyme-ignoree` | 09 Q2 c | **à retirer** (l'erreur exécutée est « les minéraux se digèrent ») |
| `bio.dig.absorption-dans-la-digestion` | 09 Q2 d | exacte |
| `bio.sang.plasma-transporte-l-oxygene` | 09 Q3 a, 10 Q5 d | exactes (09 Q3 a le devient tout à fait avec le correctif M-09-1) |
| `bio.sang.fonctions-des-cellules-confondues` | 09 Q3 b | exacte |
| `bio.demarche.cause-sans-temoin` | 10 Q1 b, 10 Q3 a | exactes (10 Q1 b : cas limite accepté) |
| `bio.lecture.valeur-d-une-autre-grandeur` | 10 Q4 b, c, d ; 10 Q6 b, c ; 10 Q8 b ; 11 Q1 a ; 11 Q2 d ; 11 Q4 b | exactes |
| idem | 10 Q7 c | **à retirer** (aucune valeur donnée : inférence fausse) |
| `bio.alim.valeurs-energetiques-confondues` | 11 Q1 b, d ; 11 Q2 a, c | exactes (« 4 pour tout » = lipides comptés à 4, usage déjà établi au registre) |
| `bio.alim.quantite-sans-qualite` | 11 Q4 c, 11 Q5 b | exactes |

Aucune option à deux erreurs n'est étiquetée ; aucune question `ordering`/`matching` ne porte d'étiquette. Options muettes qui méritent une étiquette EXISTANTE : 07 Q2 c → `bio.dig.absorption-dans-la-digestion` ; 11 Q3 c et d → `bio.alim.valeurs-energetiques-confondues` (porte R1) ; 08 Q3 a du correctif M-08-2 → `bio.circ.oreillettes-inversees`. Facultatif : 10 Q2 a (`bio.resp.azote-constant-lu-comme-erreur`, voisine).

### Familles nouvelles (comptées par grep sur tout le SVT de `origin/main` + la tranche)

- **(2) `bio.resp.appareil-fabrique-l-oxygene` — À CRÉER.** Trois questions distinctes l'exécutent exactement : tranche 07 Q2 option a (« البنية 2 : صنع الأكسيجين الذي تحتاجه الخلايا ») ; publiés `08-at-tanaffus/exercices/01-tamrin.json` Q6 option c (« تحويل الهواء إلى أكسيجين ») et `08-at-tanaffus/exercices/06-defi-concours.json` Q3 option b (« لأنّ رئته تصنع الأكسيجين »). (L'étiquette primaire `eveil.resp.poumons-fabriquent-oxygene` existe, mais dans l'espace `eveil` et avec « الحويصلات » pour les alvéoles, que le cours 08 réserve à autre chose : ne pas la réemployer en SVT.) Libellés de l'auteur à deux retouches près (accord du pronom en français ; « فقط » mal placé en arabe), vérifiés en Chromium :
  - fr « Tu crois que les voies respiratoires ou le poumon fabriquent l'oxygène : ils ne font que le prélever dans l'air (21 %) et le céder au sang à travers la paroi des alvéoles. »
  - en « You think the airways or the lungs make oxygen: they only take it from the air (21%) and pass it to the blood across the alveolar wall. »
  - ar « تظنّ أنّ المسالك التنفّسيّة أو الرّئة تصنع الأكسيجين: إنّما تأخذه من الهواء (21 %) وتمرّره إلى الدّم عبر جدار السّنخ. »
- **(1) `bio.resp.equation-respiration-a-l-envers` — à créer SOUS UN LIBELLÉ ÉLARGI.** Telle que proposée, elle couvre exactement quiz Q8 option b et 04-defi Q3 option b (publiés) et 07 Q6 option c (tranche) : trois questions, seuil atteint ; mais le correctif M-07-2 fait disparaître 07 Q6 c (retour à deux), et 07 Q5 d (« التركيب الضوئيّ » nommé comme réaction de la cellule) n'écrit aucune équation à l'envers : le libellé proposé ne la nomme pas. Un libellé « respiration et photosynthèse confondues » couvre exactement les quatre placements et tient le seuil quel que soit le sort de 07 Q6 ; identifiant proposé `bio.resp.respiration-photosynthese-confondues` (la photosynthèse est enseignée en SVT 7ᵉ) :
  - fr « Tu confonds la respiration cellulaire avec la photosynthèse, sa réaction inverse : dans la cellule, le glucose et l'oxygène sont consommés, le dioxyde de carbone et l'eau rejetés, et de l'énergie est libérée. »
  - en « You confuse cellular respiration with photosynthesis, its reverse reaction: in the cell, glucose and oxygen are used up, carbon dioxide and water given off, and energy released. »
  - ar « تخلط بين التنفّس الخلويّ والتركيب الضوئيّ، وهو التفاعل المعاكس له: داخل الخليّة يُستهلك الجليكوز والأكسيجين، ويُطرح ثنائي أكسيد الكربون والماء، وتتحرّر الطّاقة. »
  - placements : `08-at-tanaffus/quiz.json` Q8 option b, `08-at-tanaffus/exercices/04-defi.json` Q3 option b, tranche 07 Q5 option d (+ 07 Q6 option c si la forme actuelle est gardée).
- Aucune autre erreur muette n'atteint trois questions dans la tranche (« le glucose sert à bâtir le muscle » : 10 Q9 d et 11 Q8 b, deux seulement) : muettes.

### Doublons — bilan

- Entre missions de la tranche : aucun doublon de gabarit (aucune paire de missions qui ne diffère que par ses nombres). Notions qui reviennent sous des angles distincts : respiration cellulaire ×4 (07 Q5, 07 Q6, 10 Q9, 11 Q8), transport de l'O₂ (09 Q3, 10 Q5), glucose consommé selon l'activité (10 Q8, 11 Q6) — signal, pas défaut.
- Avec le chapitre 08 publié : 07 Q6 ≈ quiz Q8 / 04-defi Q3 (**M-07-2**) ; 10 Q6 refait l'exemple travaillé du cours (m-10-4) ; vérification demandée : 10 Q9 et 11 Q8 ne doublonnent ni le quiz Q8 ni 04-defi Q3.
- Avec les chapitres 04 à 07 et le lot L01 : 08 Q3 ≈ 07/08 Q2 (**M-08-2**) ; 08 Q2 recoupe 07/08 Q4 et le quiz 07 Q6 (m-08-1) ; 09 Q2 ≈ 05/02-tamrin Q1, 09 Q4 ≈ 07/04-defi Q1 et 07/07 Q2 (m-09-2) ; rien avec 05/07 et 05/08.
- Mesures du moteur (`content:tranche --chapters 08`) : 0 paire proche impliquant 07-11 (les deux paires signalées sont entre missions déjà publiées) ; clé strictement la plus longue : 0 sur les 28 QCM de la tranche (le 49 % affiché vient des missions publiées du chapitre) ; positions de clé de la tranche équilibrées.

### Gates et rendu

- `content:check` passe ; `content:qa --subject sciences-vie-terre` : 0 erreur, aucun avertissement sur 07-11 ; balayages : aucun chiffre arabo-indien, aucun LaTeX, aucun séparateur de milliers en espace simple, aucune virgule arabe dans une notation (les deux parenthèses à virgule arabe de 10 Q3 sont de la prose), aucune « على الشكل التالي », aucun renvoi par lettre ou à une autre question.
- Rendu arabe : chaque fichier rendu via `splitMathRuns` du moteur (`origin/main`, arena#1137-#1145 compris) en Chromium `dir=rtl`, ordre visuel des isolats vérifié caractère par caractère ; aucune chaîne affichée dans un autre ordre que la source ; aucune ligne de formule seule refusée par `isDisplayEquation`.
- Figures : onze champs à figure, neuf SVG distincts (07 Q1 = 07 Q3, 10 Q1 = 10 Q2), tous contrôlés au PDF ; tous passent le filtre DOMPurify du moteur sans perte ; un seul débordement de `viewBox` (2 unités, m-08-3).

### Réponses aux quatre arbitrages demandés

1. (أ)/(ب) de 2024 : lecture de l'auteur confirmée sur le PDF (sigmoïde à la base de l'artère pulmonaire ; auriculo-ventriculaire droite) — voir 08.
2. « السّنخ الرّئويّ » pour la structure 2 : acceptable, c'est le terme du cours pour cette figure — voir 07.
3. Recoupements avec le chapitre publié : 10 Q9 et 11 Q8 ne sont pas des doublons ; 07 Q6 en est un (M-07-2).
4. « 4 kcal/g pour les trois classes » sous `bio.alim.valeurs-energetiques-confondues` : exact — voir 11.

---

## Chiffre final

- **Questions auditées : 31** (07 : 6 · 08 : 4 · 09 : 4 · 10 : 9 · 11 : 8), toutes re-résolues à l'aveugle avant lecture des clés.
- **Clés fausses : 0.** Défauts critiques : 0.
- **Défauts majeurs : 9, sur 9 questions à reprendre** : 07 Q3 (explication), 07 Q6, 08 Q1, 08 Q3, 09 Q3, 09 Q4, 10 Q2, 10 Q9, 11 Q8 — chacun avec son texte de remplacement exact, vérifié par script et en Chromium.
- **Défauts mineurs : 15** (m-07-1 à m-07-3, m-08-1 à m-08-3, m-09-1, m-09-2, m-10-1 à m-10-4, m-11-1, m-11-3, m-11-4), dont 2 étiquettes à retirer (09 Q2 c, 10 Q7 c) et 4 options muettes à étiqueter avec une étiquette existante.
- **Étiquettes nouvelles proposées : 2** — `bio.resp.appareil-fabrique-l-oxygene` (3 placements) et `bio.resp.respiration-photosynthese-confondues` (libellé élargi de la proposition de l'auteur, 3 à 4 placements).
- Verdicts par fichier : 07 défaut majeur · 08 défaut majeur · 09 défaut majeur · 10 défaut majeur · 11 défaut majeur. **Verdict global : à corriger avant livraison** (aucune clé fausse, mais neuf questions à reprendre).
