# Audit M3 — missions du gisement, éveil 6ᵉ (chapitres 04, 06, 05)

> Auditeur indépendant (opus), 2026-10-20. Rien n'a été modifié dans `content/`, aucune écriture git.
> J'ai re-résolu toutes les questions à l'aveugle AVANT de lire `rapports/rapport-M3.md`.
> Sources lues : les transcriptions `examens-nationaux/6eme-base/eveil/` (2008–2026) et les PDF (`pdftoppm -r 150/200/300`) pour 2015,
> 2016, 2017, 2021 et 2023 ; les cours, les quiz et les exercices `01`–`05` des chapitres 04, 05, 06 et 03 (le fer) ; la fiche `programme/6eme-base/eveil.md` § 7.37.
> Rendu : Chromium 1194, `dir=rtl`, 360 px, toutes les questions qui ont une figure (21 rendus).

## Verdict : **À CORRIGER**

Aucune clé fausse : **95 questions re-résolues** (et non 91 comme l'écrit le rapport de l'auteur), et ma réponse égale la clé partout. Mais il y a :
- **1 critique** : une double réponse (`06/06` Q4) ;
- **16 majeurs**, presque tous du même ordre : des questions qui redemandent le cours ou les exercices `01`–`05`, des fuites d'une question vers la suivante, et une notion que le cours 05 n'enseigne pas ;
- **8 mineurs**.

Les deux devoirs sont en grande partie absorbés par le patron. Je recommande de **couper `04/09`** (E-1, comme la carte l'avait prévu) et de **réduire `05/09`**.

## Gates (depuis `/home/user/eng-deliver`, lien `content` inchangé)

| gate | résultat |
| --- | --- |
| `content:check` | ✓ 121 sujets valides (EXIT 0) |
| `content:qa -- --subject eveil-scientifique-6eme` | ✓ aucun signalement (EXIT 0) |
| `content:figures:check` | ✓ (EXIT 0) |
| `content:tranche … --chapters 04,05,06 --fresh --strict-longest --strict-lessons` | ✓ clé strictement la plus longue 0/109 ; positions 23/28/28/21 % ; 0 recul de patron ; 1 paire proche `04/06` Q8↔Q9 (0,45) : exercice parallèle voulu (même diagramme officiel, deux repas), **acceptée** |
| `content:gisement:controle` (deux devoirs) | ✓ 0 plage ≥ 8 mots ; 1 plage ≥ 6 mots (`05/09` q4, indicatif) ; 0 donnée commune |
| chiffres arabo-indiens, `\d \d{3}` hors SVG | 0 |

## Doutes de l'auteur : mes réponses

1. **Sens de la flèche** : la mission suit le manuel (« يتغذّى على », la flèche part du mangeur et pointe vers l'aliment ; cours 05 l. 95, et l'audit B3 l'a vérifié sur les pages 110–111 du manuel). C'est conforme. La chaîne 2024 en « غذاء لـ » est normalisée, et son explication le dit. **Mais le rapport de l'auteur se trompe sur 2016** : dans le PDF, les cases se lisent de gauche à droite, « سنبلة → أفعى → فأر → بكتيريا », et **les flèches pointent vers la droite, donc vers les bactéries**. Le sujet emploie la convention « de l'aliment vers le mangeur ». La mission a retourné les flèches sans le dire : voir m-5. La correction attendue reste la même dans les deux conventions (on échange le rat et le serpent), donc la clé de Q10 est juste.
2. **Place des bactéries** : dans les ordres « chacun mange le suivant » (`05/06` Q2 et Q10), les bactéries sont placées EN TÊTE, et chaque énoncé dit qu'elles mangent le cadavre du dernier mangeur. Le cours 05 n'enseigne pas où écrire un décomposeur dans une chaîne ; il dit seulement « تصل آخر السلسلة بأوّلها ». Comme la règle est donnée dans l'énoncé, l'item est recevable. Je propose une phrase à ajouter au cours (m-8).
3. **Le fer et les globules rouges, que le cours 04 ne dit pas** : c'est enseigné au **cours 03** (chapitre antérieur dans le manifeste). Section « فقر الدّم » : la définition dit « قلّة الكريّات الحمراء », et la propriété dit qu'on souffre d'anémie quand le غذاء manque de « مادّة الحديد ». La clé de `04/08` Q4 (« الحديد ضروريّ لصنعها ») s'en déduit en une étape. **Recevable.**
4. **Le milieu et la distinction vivant / non vivant, que le cours 05 ne définit pas** : c'est **confirmé**, et c'est un MAJEUR (M-14). Le guide l'enseigne pourtant (p.143, fiche § 7.37 : « الوسط البيئي … عناصر حيّة وغير حيّة »). Le cours de 5ᵉ n'est pas une couverture suffisante : la règle est que la notion soit enseignée par le chapitre ou par un chapitre antérieur du même manifeste.

À noter aussi : la transcription `2023-unique.md` l. 27 a un défaut. Elle donne six aliments (« fromage blanc… ») alors que le PDF en imprime sept : « جبن وبيض وخبز وزبدة وخسّ وبرتقال وزيت زيتون ». La mission `04/07` suit le PDF, elle est juste. **C'est la transcription qu'il faut corriger**, pas la mission.

---

## Défauts

### CRITIQUE

**C-1 — `06-reproduction-florale/exercices/06-exams-2009-2017-…json` Q4 (2013) : deux réponses défendables.**
Dans le SVG, la fleur 2 a ses étamines ET son pistil sous le غطاء. Or la mission pose elle-même (Q6–Q7, 2015) qu'une fleur isolée qui a ses étamines peut être pollinisée par son propre pollen. Avec cette logique, « في الزهرتين، لأنّ في كلّ منهما مآبر وميسمًا » est défendable. Q4 double aussi `06/02-boss#7` (deux fleurs, la seconde sous un sac : seule la première est pollinisée), et Q5 invente une suite (« بعد أسبوع ») où « فات وقت التأبير » devient défendable à son tour.
- **Correctif recommandé** : supprimer Q4 et Q5. La session 2013 reste reprise par `05/07`, et le geste « une protection empêche l'insecte » (C14#1a) reste porté par Q6–Q7 (2015).
- **Si le pilote garde Q4**, voici le texte vérifié (une seule clé ; la clé n'est pas la plus longue ; rendu contrôlé) :
  - prompt : `مناظرة 2013: خرج زيدان في جولة بين الحقول فرأى النحل يتنقّل بكثافة بين الأزهار. «ألاحظ الرسم وأجيب: يتمّ التأبير في الزهرة رقم ... أعلّل إجابتي.»` + SVG inchangé + `في أيّ زهرة يمكن أن تنقل النحلة طلع زهرة أخرى إلى الميسم، ولماذا؟`
  - options a, c, d inchangées ; b → `في الزهرتين، لأنّ النحلة تدخل تحت الغطاء البلاستيكيّ`
  - explication, ajouter à la fin : `وقد يحدث داخل الغطاء تأبير ذاتيّ بطلع الزهرة نفسها، لكنّ النحلة لا تحمل إليها طلعًا من زهرة أخرى.`
  - Q5, si elle est gardée : supprimer « بعد أسبوع » (`ثمّ نزع زيدان الغطاء البلاستيكيّ عن الزهرة 2 وتركها مكشوفة بين الأزهار نهارًا كاملًا.`), et b → `لا تقترب منها النحلة أبدًا، لأنّها كانت مغطّاة`. Longueurs des options : 46 / 46 / **39** (clé) / 46.

### MAJEURS

**M-1 — `04-nutrition/exercices/06-…json` Q7 (le beurre du grand-père).** Elle redemande `04/02-boss#2` (« الزبدة غذاء حيوانيّ… → أغذية الطاقة، لأنّها من الدهنيات »), avec le même leurre « animal donc construction », ainsi que la ligne « المسنّ… نشاطه قليل » du tableau du cours. Elle attribue aussi à « مناظرة 2018 » une prémisse que le sujet ne contient pas (« متقاعد قليل الحركة », c'est l'ancrage du cours). **Correctif** : supprimer Q7 (la mission passe à 9 q ; la session 2018 garde Q6).

**M-2 — `04/08` Q6 (« ce que traite la vitamine A »).** Son explication résout entièrement Q7 (« فقر الدم تعالجه أملاح الحديد… الفيتامين «أ» يعالج ضعف البصر »). C'est aussi le troisième item sur le même fait, après Q5 et Q7. **Correctif** : supprimer Q6 (la mission passe à 8 q).

**M-3 — `04/09` (devoir), mission entière.** Cinq questions sur sept redemandent le patron :
- Q1 ≈ `01-pratique#8` (lait / pain / agrume ↔ groupe) ;
- Q3 ≈ `02-boss#8` (« أغذية الطاقة أساس النموّ ») ;
- Q4 ≈ `quiz#4` et `03-revision#4` ;
- Q5 ≈ `05-entrainement#4` et le tableau du cours ;
- Q7 (berger, gencives, vitamine C) ≈ l'exemple du cours (les pêcheurs et les conserves), `02-boss#5` et `05-entrainement#7`.

L'auteur la signale lui-même comme « candidate à la coupe ». **Correctif** : **couper m026** (E-1, premier de l'ordre de coupe), et retirer la ligne devoir du `sources[]` de `04/chapter.json`.

**M-4 — `06/06` Q3 ≡ `06/07` Q3.** Les deux demandent de nommer le transport du pollen vers le stigmate d'une autre fleur (التأبير الخلطيّ), avec les mêmes leurres (ذاتيّ, إخصاب). Les deux redonnent le `verifie` du cours (le papillon et le citronnier voisin) et `02-boss#6`, et `06/06` Q1 a la même clé. **Correctif** : supprimer `06/06` Q3 et `06/07` Q3. La consigne 2018 reste reprise par `06/07` Q6 et Q7 ; le dernier blanc de 2017 est le fait de Q1.

**M-5 — `06/06` Q9.** L'explication de Q8 donne la clé de Q9 (« الطلع ينتقل من المئبر إلى الميسم… الإخصاب فاتّحاد حبّة الطلع بالبويضة »), et Q9 redemande `quiz#3`. **Correctif** : supprimer Q9. Après C-1, M-4 et M-5, `06/06` garde Q1, Q2, Q6, Q7 et Q8 (5 q) : c'est mince, mais aucune question n'est redemandée.

**M-6 — `06/07` Q9 (« pourquoi l'abeille est consommatrice »).** L'explication de Q8 contient mot pour mot la clé de Q9 (« لا يصنع غذاءه بنفسه بل يتغذّى على رحيق الأزهار »). Q9 double aussi `05/07` Q7, qui pose la même raison. **Correctif** : supprimer Q9 ; la notion reste portée par `06/07` Q8 (option c) et par `05/07` Q2.

**M-7 — `05-milieu…/exercices/06-…json` Q4 (« le cinquième maillon : une plante verte productrice »).** Elle redemande `05/05-entrainement#2` (« عند أيّ حلقة تنتهي الأسهم ؟ → النبات الأخضر المنتج »). Q3 la vide en plus de son contenu : l'item « عشب صحراويّ » figure parmi les éléments à ordonner, et l'explication de Q3 le dit. **Correctif** : supprimer Q4.

**M-8 — `05/06` Q1 (« quel être vivant est donné par le texte, pas par les photos »).** L'énoncé de Q5 nomme la cochenille et la tient pour « حلقة لا تظهر في الصور » : la réponse de Q1 est donnée. Q1 se lit d'ailleurs sans aucun savoir. **Correctif** : supprimer Q1 (la session 2025 reste reprise par Q5). `05/06` passe à 9 q.

**M-9 — `05/07` Q2 ↔ Q7 (2013, l'abeille), fuite dans les deux sens.** L'énoncé de Q7 écrit « يعتبر النحل مستهلكا من الدّرجة الأولى », ce qui est la clé de Q2. L'explication de Q2 écrit « تتغذّى على رحيق الأزهار، أي على النبات مباشرةً », ce qui est la clé de Q7. Avec le tirage au hasard du donjon, l'une livre toujours l'autre. **Correctif** : supprimer Q7. Q2 garde la raison dans son explication. Q7 doublait aussi `06/07` Q9 (M-6).

**M-10 — `05/07` Q8 ↔ Q9 (2023, la phrase de Chadi).** L'explication de Q8 donne la clé de Q9 (« وهي منتجة »). Les leurres b, c et d de Q8 contredisent le cours à vue (« le végétal n'a pas besoin de lumière », « il ne fabrique pas sa nourriture », « le consommateur fabrique sa nourriture »). **Correctif** : supprimer Q8 et garder Q9 (la phrase corrigée).

**M-11 — `05/07` Q6 ≈ Q10 ≈ Q12.** Les trois questions ont presque la même clé : « تحلّل بقايا الكائنات الميّتة وتحوّلها إلى أملاح معدنيّة ». Elles redonnent aussi le `retenir` du cours (« الفطر والبكتيريا مفكّكات تحلّل… إلى أملاح معدنيّة ») et `01-pratique#6`. **Correctif** : supprimer Q6, garder Q10 (la phrase officielle de 2021), et remplacer Q12 par le texte ci-dessous. Il porte le piège C03#13 (« leur rôle se limite aux maladies ») sous l'angle d'une conséquence, et non d'une définition. J'ai vérifié : une seule clé, des longueurs de 60 / 60 / 65 / 65 (la clé fait 60, elle n'est pas strictement la plus longue), aucune paire proche, et aucune prémisse niée.
  - prompt : `مناظرة 2024: «فسّر دور الكائنات الدّقيقة في الوسط البيئي.» الكائنات الدقيقة هنا كالبكتيريا والفطريّات الّتي تعيش في التربة. قال تلميذ: «هذه الكائنات تسبّب الأمراض فقط، ولو اختفت من التربة لكان الوسط أسلم». ماذا يحدث فعلًا لو اختفت من تربة غابة؟`
  - a (clé) `تتراكم الجثث والبقايا، ولا تعود الأملاح المعدنيّة إلى التربة`
  - b `يصبح الوسط أسلم، لأنّ دورها الوحيد هو إحداث الأمراض للكائنات`
  - c `تكثر الأملاح المعدنيّة في التربة، لأنّ هذه الكائنات كانت تستهلكها`
  - d `لا يتغيّر شيء في الوسط، لأنّ هذه الكائنات لا تُرى بالعين المجرّدة`
  - explication : `الكائنات الدقيقة المفكّكة تحلّل الجثث وبقايا النباتات وتحوّلها إلى أملاح معدنيّة يمتصّها النبات الأخضر. فلو اختفت لتراكمت البقايا ولم تعد هذه الأملاح إلى التربة، فيضعف النبات ثمّ من يتغذّى عليه. فدورها لا يقتصر على إحداث بعض الأمراض، وهي لا تستهلك الأملاح المعدنيّة بل تُرجعها إلى التربة.`
  - pas d'étiquette (aucun id ne couvre C03#13).

**M-12 — `05/08` Q8 (2023, la propagation de la typhoïde).** Les données ajoutées par l'auteur (le sujet n'en donne aucune) reprennent deux ancrages du cours : les légumes arrosés d'eaux usées (exemple « كيف أُصيب فرد العائلة ») et le puits près de l'égout (ancrage de « المحافظة على سلامة الأوساط المائيّة »). De plus, le leurre c (« فيروس ينتقل بالهواء ») porte deux erreurs mais une étiquette. **Remplacement vérifié** (longueurs 55 / 63 / 49 / 42 : la clé n'est pas la plus longue ; chaque option fausse porte une seule erreur, celle de son étiquette) :
  - prompt : `مناظرة 2023: «أفسّر ظاهرة تفشّي مرض الحمّى التّيفيّة بالمنطقة الّتي يسكنها الفلّاح.» في المنطقة قناة مجارٍ مكسورة تصبّ في الوادي، ويملأ السكّان مواجلهم من ماء الوادي في الصيف. أيّ تفسير صحيح؟`
  - a (clé) `تنقل مياه المجاري جرثومة المرضى إلى ماء الوادي فالمواجل`
  - b `المرض لا يصيب إلّا من يشرب من الماجل، فالخضر والذباب لا ينقلانه` — `eveil.eco.eau-polluee-seulement-si-bue`
  - c `سببه فيروس ينتقل بالماء الملوّث إلى سكّان المنطقة` — `eveil.eco.virus-et-bacterie-confondus`
  - d `سببه نقص الفيتامينات في غذاء سكّان المنطقة` (muette)
  - explication : `الحمّى التيفيّة تسبّبها جرثومة تخرج مع فضلات المريض. فإذا انكسرت قناة المجاري وصبّت في الوادي، حمل ماؤه الجرثومة إلى المواجل الّتي يشرب منها السكّان. ولا يقتصر انتقالها على الشرب، فالخضر المسقيّة بماء ملوّث والذباب ينقلانها أيضًا. وسببها جرثومة لا فيروس، وليست من أمراض نقص الغذاء.`

**M-13 — `05/08` Q10 (2009, apparier des symptômes à des maladies).** Elle double `05/04-defi#1`, qui apparie les mêmes trois groupes de symptômes aux mêmes trois maladies, et qui figurait dans la liste « ne pas redemander » de la carte. **Remplacement vérifié** (un QCM sur la seule ligne sans signe distinctif ; longueurs 38 / 34 / 49 / 52 ; rendu RTL contrôlé) :
  - type `mcq`, d2 ; prompt : `مناظرة 2009: «أكتب في الخانات الفارغة أسماء الأمراض التّالية استنادا إلى أعراضها: الكوليرا، البوصفير، الحمّى التيفيّة.» أيّ مرض تدلّ عليه هذه الأعراض: «فشل عضليّ مصحوب بارتعاش وصداع وحمّى مع فقدان شهيّة الأكل ورغبة في التقيّؤ»؟`
  - a `الحمّى التيفيّة، لأنّ فيه حمّى وصداعًا`
  - b `الكوليرا، لأنّ فيه رغبة في التقيّؤ`
  - c (clé) `البوصفير، لأنّ فيه فشلًا عضليًّا وفقدانًا للشهيّة`
  - d `مرض من أمراض نقص الغذاء، لأنّ المريض فقد شهيّة الأكل`
  - explication : `الفشل العضليّ وفقدان الشهيّة من أعراض البوصفير، ولا يظهران في الكوليرا ولا في الحمّى التيفيّة. أمّا الحمّى والصداع فيظهران في الحمّى التيفيّة وفي البوصفير معًا، فلا يكفيان للتمييز. والكوليرا يميّزها التقيّؤ مع الإسهال وآلام الظهر والأطراف، لا مجرّد الرغبة في التقيّؤ. وهذا مرض ينقله الماء الملوّث، لا من أمراض النقص.`

**M-14 — `05/07` Q3 et Q11 : notion non enseignée.** Le cours 05 ne définit ni le « الوسط البيئيّ » ni les « عناصر حيّة / غير حيّة » (aucune occurrence). Q11 n'est résoluble que par cette définition. **Correctif** (préféré) : la session du cours (`content-cours`, au patron) ajoute la notion au cours 05 avant que la mission parte. Voici la base, tirée du guide p.143 : `::: definition` / `**الوسط البيئيّ** مكان تتوفّر فيه خصائص معيّنة (غابة، بحر، صحراء، بحيرة…). يضمّ **عناصر حيّة** (النبات والحيوان والكائنات الدقيقة) و**عناصر غير حيّة** (الماء، التربة، الهواء، الضوء، الحرارة)، وكلّها مرتبطة بعضها ببعض.` / `:::`, avec sa ligne dans `resume.md`. **À défaut**, supprimer Q11 (Q3 se déduit : les bactéries et le plancton végétal sont des « كائنات » dans le cours).

**M-15 — `05/09` (devoir) Q1 : elle redemande `05/quiz#3`.** Même chaîne, « le poulet mange le blé, l'homme mange le poulet → rang 2 ». La carte demandait trois rangs (1, 2, 3) ; le rang 1 manque. **Remplacement vérifié** (rendu RTL contrôlé : les flèches pointent vers l'aliment ; la clé est la plus courte ; aucune fuite vers Q4) :
  - type `mcq`, d1 ; prompt : `أيّ سلسلة غذائيّة يكون فيها الإنسان مستهلكًا من الدرجة الأولى؟ (كلّ سهم يُقرأ «يتغذّى على»)`
  - a `الإنسان ← الدجاجة ← حبوب القمح`
  - b (clé) `الإنسان ← حبوب العدس`
  - c `الإنسان ← الدجاجة ← الجرادة ← العشب الأخضر`
  - d `التمر ← الإنسان` — `eveil.eco.fleche-lue-a-l-envers`
  - explication : `السهم يتّجه نحو الغذاء، ونعدّ الدرجات ابتداءً من النبات المنتج. حبوب العدس نبات، والإنسان يتغذّى عليها مباشرةً فهو مستهلك من الدرجة الأولى. وإذا أكل الدجاجة الّتي أكلت القمح صار من الدرجة الثانية، وإذا أكل دجاجة أكلت جرادة صار من الثالثة. وكتابة السهم من التمر نحو الإنسان تجعل التمر هو الآكل، وهذا مقلوب.`

**M-16 — `05/09` Q6 et Q7 : elles redemandent.** Q6 (les symptômes de la typhoïde) a la clé de `05/08` Q2 (2019) et de la ligne l3 de `04-defi#1`. Q7 (protéger le puits) redonne `05/04-defi#4` (« إبعاد مياه المجاري عن مياه الشرب ») et l'exemple du cours (le puits près de l'égout). **Correctif** : supprimer Q6 et Q7. Le devoir garde Q1 (remplacée), Q2, Q3, Q4 et Q5 (5 q, rangs 1, 2 et 3) ; le geste D07#3 reste porté par Q3.

### MINEURS

- **m-1 — `04/06` Q2 (`short_answer`, سوء التغذية)** : `acceptedAnswers` est vide. La normalisation retire les diacritiques et replie ة→ه, mais ne retire pas l'article. **Correctif** : `"acceptedAnswers": ["سوء تغذية"]`. L'explication ne contient pas la réponse ✓.
- **m-2 — `04/06` Q6** : retirer la prémisse ajoutée. Prompt : `مناظرة 2018: «كوّن وجبة غذاء مناسبة للجدّ ممّا يلي: كسكسي بلحم الضّأن – سلطة خضر – سمك مشويّ – زبدة – برتقال.» أيّ اختيار يكوّن له وجبة متوازنة؟`. Il y a toujours une seule clé : a sans énergie, b sans protection, d sans construction.
- **m-3 — `04/07` Q6 → Q7** : l'explication de Q6 écrit la phrase corrigée de Q7. Remplacer l'explication de Q6 par : `في الإفادة خطآن: الزلاليات ليست المركّب الغالب في أغذية الطاقة، بل توجد في أغذية البناء؛ والزلاليات لا تقي من الأمراض بل تساعد على النموّ، أمّا الوقاية فمن عمل الأملاح المعدنيّة والفيتامينات.` (Q5 redemande aussi la paire « persil » de l'appariement Q4 : c'est toléré, car ce geste ajoute le groupe.)
- **m-4 — `04/08` Q1 et Q9 (E-5)** : la coquille du sujet est corrigée dans la phrase citée, mais aucune explication ne le dit. Ajouter à la fin des deux explications : `وقد صحّحنا في نصّ الإفادة اسم المرض الّذي كُتب في ورقة المناظرة خطأً.` (sans reprendre la coquille).
- **m-5 — `05/06` Q10 (E-5)** : la figure retourne les flèches imprimées (dans le PDF elles vont « سنبلة → أفعى → فأر → بكتيريا ») sans le dire. Ajouter à l'explication : `وفي ورقة المناظرة رُسمت الأسهم من الغذاء إلى الآكل، فأعدنا رسمها بقراءة كتابنا «يتغذّى على»؛ والخطأ واحد في القراءتين: تبديل مكاني الفأر والأفعى.` Corriger aussi le rapport de l'auteur, qui écrit « flèches vers la gauche ».
- **m-6 — `06/06` Q6 (E-5)** : le sac du PDF enveloppe toute la fleur ; la mission le redessine autour du pistil et isole les fleurs. La correction est juste, mais l'explication ne la signale pas. Ajouter : `وفي رسم المناظرة يحيط الكيس بالزهرة كلّها؛ أعدنا رسمه حول المدقّة وحدها وعزلنا الأزهار الثلاث، حتّى لا يبقى إلّا جواب واحد.`
- **m-7 — `05/08` Q4** : le prompt dit « الإفادتين التّاليتين » mais ne cite qu'une affirmation. Écrire `«أصلحْ كلَّ خطإ ورد في الإفادة التّالية: …»`. La lecture de schéma (V4) est conforme.
- **m-8 — cours 05 (signalé pour la session du cours, sans bloquer)** : une phrase sur la place d'un décomposeur dans une chaîne écrite en « يتغذّى على » (« تتغذّى البكتيريا على جثّة آخر الآكلين، فنكتبها قبله »). Elle éviterait d'avoir à répéter la règle dans chaque énoncé (`05/06` Q2 et Q10).

### Vérifiés et sans défaut (extraits)

- Diagramme 2026 (`04/06` Q8–Q10) : les valeurs sont celles du PDF (90/5/5, 50/50/0, 45/20/35) et aucune valeur n'est une clé (V1).
- Tableau 2021 (`04/08` Q8–Q9) : j'ai relu le PDF à 200 dpi ; « 30 ≤ » se lit bien « 30 أو أكثر », donc seule la vitamine D est sous la norme. B1 et B12 ne sont jamais clés (E-8).
- Figure 2017 (`06/06` Q2) : la fleur A (pistil seul) est à droite et la fleur B (étamines) à gauche, comme dans le PDF.
- Cycle 2018 (`06/07` Q7) : la figure est juste.
- Chaîne de Chadi 2023 : les flèches pointent vers la دودة, comme le dit la transcription.
- Légendes `text-anchor="middle"` : lisibles et justes partout dans les rendus (cases centrées, étiquettes sous les fleurs, légendes des diagrammes). Une seule réserve : l'ordre des séries dans les barres du diagramme 2026 va de gauche à droite alors que la légende se lit de droite à gauche. C'est sans effet, car ce sont les couleurs qui distinguent les séries.
- Étiquettes : aucune sur un `multi`, un `ordering` ou un `matching`, et toutes sont exactes. Seuls écarts : le leurre c de `05/08` Q8 porte deux erreurs (corrigé dans M-12), et le leurre a de `04/06` Q7 n'exécute pas l'erreur d'origine (la question est supprimée par M-1).
- Ids proposés par l'auteur : `eveil.nutri.proteines-protegent` porte bien ≥ 3 options (`04/07` Q6, Q7 et l'ancienne `04/09` Q6) ; c'est au pilote de le poser. Les autres restent sous le seuil.

## Tableau de re-résolution (ma réponse = clé partout)

| fichier | q. | verdict |
| --- | ---: | --- |
| `04/06` | 10 | Q1–Q6, Q8–Q10 OK (Q2 m-1, Q6 m-2) · Q7 M-1 |
| `04/07` | 9 | toutes OK (Q6 m-3) |
| `04/08` | 9 | OK sauf Q6 M-2 (Q1/Q9 m-4) |
| `04/09` | 7 | clés justes ; mission à couper (M-3) |
| `06/06` | 9 | Q1, Q2, Q6–Q8 OK (Q6 m-6) · Q4 C-1 · Q5 C-1 · Q3 M-4 · Q9 M-5 |
| `06/07` | 9 | OK sauf Q3 M-4, Q9 M-6 |
| `05/06` | 11 | OK sauf Q1 M-8, Q4 M-7 (Q10 m-5) |
| `05/07` | 12 | Q1–Q5, Q9, Q10 OK · Q6 et Q12 M-11 · Q7 M-9 · Q8 M-10 · Q3 et Q11 M-14 |
| `05/08` | 12 | OK sauf Q8 M-12, Q10 M-13 (Q4 m-7) |
| `05/09` | 7 | Q2–Q5 OK · Q1 M-15 · Q6 et Q7 M-16 |

**Total : 95 questions auditées, 0 clé fausse, 1 critique, 16 majeurs, 8 mineurs. Questions à reprendre : 26** (15 suppressions, plus `05/07` Q11 si le cours n'est pas complété ; 4 remplacements ; et la mission `04/09` de 7 questions coupée en entier).
