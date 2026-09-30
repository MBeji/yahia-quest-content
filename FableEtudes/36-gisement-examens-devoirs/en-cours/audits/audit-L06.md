# Audit indépendant : tranche gisement, maths 9ᵉ, chapitre 07 (8 missions d'examen, 46 QCM)

**Résultat : 46 questions auditées, 0 clé fausse, 0 défaut critique. 9 questions sont à reprendre (défauts majeurs) et 18 corrections mineures sont proposées.** Aucun fichier du dépôt n'a été modifié.

**Méthode.**
- Skill `content-audit` et consigne `gisement-auditeur.md` appliqués.
- Chaque question a été extraite sans `correctOption`, explication ni tags, résolue jusqu'au bout, puis seulement comparée à la clé du fichier.
- Les données ont été confrontées aux 8 transcriptions ; celles de l'arbre de travail sont identiques à `origin/main`.
- Les 24 points des 4 polygones ont été recalculés à partir des coordonnées SVG.
- Les gabarits ont été comparés aux missions publiées 01 à 09 (lues sur `origin/main`) et entre les 8 missions.
- `content:qa` a été lancé depuis le moteur : 0 erreur et 0 avertissement sur les fichiers 10 à 17.
- `content:tranche --chapters 07` : aucune clé strictement la plus longue dans la tranche, aucune paire lexicale proche impliquant 10 à 17. Les doublons trouvés ci-dessous sont des gabarits où seuls les nombres changent ; la mesure lexicale ne peut pas les voir.
- Le rendu arabe a été vérifié en exécutant la fonction du moteur `isolateLtrRuns` (`bidi.ts`) sur les chaînes suspectes.

**Contrôles sans défaut pour les 8 fichiers :**
- En-têtes : d2, `practice`, 75/15, `displayOrder` 10 à 17.
- Titres au format exact : « 🏛️ مناظرة <année> · التمرين <N> ⭐⭐: … », et « (تقني) » pour 16 et 17.
- Numéros d'exercice conformes aux transcriptions ; rampes internes non décroissantes.
- Notation : chiffres latins, pas de LaTeX, groupes de chiffres en U+00A0, pas de virgule arabe dans une notation entre crochets.
- Aucune explication ne cite une option par sa lettre ; aucun item des transcriptions n'est marqué hors programme.
- `chapter.json` : une seule ligne ajoutée dans `sources[]`, conforme ; rien d'autre ne change dans ce fichier.

## Tableaux par fichier

Légende du verdict : **OK** = clé juste et sans remarque ; **OK (m)** = clé juste, avec un point mineur ; **OK → Mx** = clé juste, mais la question est à reprendre (voir la liste des défauts majeurs).

### 10 — 2009 ex. 4 (téléphones), 5 questions
| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | 4 | b = 4 | OK | plus grand effectif (33) → valeur 4 |
| 2 | 3 | c = 3 | OK | rangs 50 et 51 entre les cumuls 22 et 52 |
| 3 | 2 ; 10 ; 22 ; 52 ; 85 ; 100 | a | OK | — |
| 4 | 52 | b = 52 | OK → M1 | clé déjà donnée ; gabarit identique à M14 Q4 et M15 Q4 |
| 5 | 48 % | c | OK | 100 − 52 ; « plus de 3 » exclut 3 |

Figure : points (0;2) (1;10) (2;22) (3;52) (4;85) (5;100), tous exacts. Aucune clé n'est marquée ; l'arabe n'apparaît que dans `<title>`.

### 11 — 2012 ex. 5 (habitants), 6 questions
| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | 1000 | c | OK (m) | le distracteur 1100 = « 5 × 220 » est artificiel |
| 2 | 33,4 | b | OK | 33 400 ÷ 1000 |
| 3 | 0,22 ; 0,71 ; 0,92 ; 0,98 ; 1 | d | OK (m) | « مرتّبة تصاعديًّا » est ambigu |
| 4 | « 71 % ont moins de 40 ans » | a | OK (m) | étiquettes de (c) et (d), voir mineurs |
| 5 | 31,4 | c | OK (m) | 20 + 20 × 28/49 = 31,43 ; le terme « موسّط » de l'examen manque |
| 6 | 92 % | b | OK | doublon exact de M14 Q6 (corrigé côté M14, voir M4) |

Figure : (0;0) (20;22) (40;71) (60;92) (80;98) (100;100), exacte.

### 12 — 2013 ex. 1 (QCM), 6 questions
| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | b = 0 ou b = 5 | d | OK | — |
| 2 | rang 5 | b | OK | — |
| 3 | 16 | c | OK | — |
| 4 | a = 2, b = 0 | a | OK | somme des chiffres 36, unité 0 |
| 5 | 39 | b | OK (m) | justification de 38,5 artificielle |
| 6 | 40 % | d | OK | 16/40 |

Fidélité : les 3 items officiels sont intacts (données et 3 options officielles chacun), avec une 4ᵉ option ajoutée. Les questions préparatoires Q1 à Q3 viennent d'abord, et l'ordre officiel 1-2-3 est conservé en Q4 à Q6.

### 13 — 2016 ex. 1 (QCM), 6 questions
| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | 3, 4 et 5 | a | OK → M2 | l'option (b) « 3 و4 » est éliminée à vue |
| 2 | 22 | c | OK (m) | 88 et 2200 dépassent les 25 matchs |
| 3 | \|x\| < 1/3 | d | OK (m) | (a) sans étiquette alors qu'une étiquette exacte existe |
| 4 | ]−1/3 ; 1/3[ | a | OK | la technique n'est pas enseignée, mais elle est déductible du rappel donné |
| 5 | a = 3, b = 6, c = 0 | d | OK → M3 | un vote majoritaire chiffre par chiffre redonne la clé |
| 6 | 2 | b | OK (m) | le mot officiel « التراكمي » est perdu |

Rien n'est perdu ni déformé : les 3 options officielles de chaque item sont présentes. Seul changement de forme : le séparateur « , » des intervalles devient « ; », convention de l'app.

### 14 — 2017 ex. 5 (oliviers), 6 questions
| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | [40 ; 60[ | c | OK (m) | « (كغ) : » mal rendu ; distracteur de remplissage [0 ; 20[ ; même gabarit que M15 Q1 |
| 2 | 54,4 | b | OK | voir M5 (doublon exact avec M15 Q2) |
| 3 | 348 | d | OK (m) | les classes ne sont pas redonnées ; même gabarit que la mission publiée 09 Q5 |
| 4 | 104 | c | OK (m) | lecture directe d'un point, difficulté réelle d1 |
| 5 | 54,1 | b | OK (m) | « الموسّط » manque |
| 6 | 60 % | b | OK → M4 | doublon exact de M11 Q6 |

Figure : (0;0) (20;20) (40;104) (60;240) (80;348) (100;400), exacte.

### 15 — 2019 ex. 5 (augmentations de salaire), 6 questions
| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | [150 ; 200[ | b | OK (m) | « (بالدينار): » mal rendu ; distracteur de remplissage [200 ; 250[ |
| 2 | 162,5 | c | OK → M5 | pièges et explication identiques à M14 Q2 |
| 3 | 25 ; 40 ; 70 ; 90 ; 100 | d | OK (m) | même gabarit que M10 Q3 |
| 4 | 70 | b | OK → M6 | identique à M14 Q4 et à M10 Q4 |
| 5 | 166,7 | c | OK (m) | « الموسّط » manque |
| 6 | 40 % | b | OK (m) | (c), l'événement contraire, sans étiquette |

Figure : (50;0) (100;25) (150;40) (200;70) (250;90) (300;100), exacte. L'axe horizontal commence à 50 sans marque de coupure (optionnel).

### 16 — 2010 technique ex. 2 (bouteilles d'eau), 5 questions
| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | type ج | a | OK | — |
| 2 | augmenter le type ج | d | OK → M7 | seule option qui nomme « ج », comme l'énoncé |
| 3 | 100 | c | OK (m) | « 500 مليمًا » (accord) |
| 4 | rangs 50 et 51 | a | OK → M8 | copie de la mission publiée 09 Q7 ; l'énoncé présuppose deux rangs |
| 5 | 450 | d | OK | cumuls 45 puis 80 |

La question 3 de la transcription porte bien sur la médiane, comme l'auteur le signale.

### 17 — 2011 technique ex. 2 (visiteurs d'un site), 6 questions
| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | 100 | a | OK | l'étendue est définie dans l'énoncé |
| 2 | 40 | b | OK (m) | « 1200 زائرًا » (accord) |
| 3 | 245 000 | c | OK → M9 | rendu cassé du modèle de couple |
| 4 | 49 | c | OK | réserve sur 40 833,3, voir la section étiquettes |
| 5 | 3200 | b | OK | — |
| 6 | 64 % | b | OK (m) | chaque distracteur = celui de Q5 divisé par 50 |

La scission de la moyenne en deux étapes (Q3 puis Q4) est fidèle.

## Défauts classés

### Critiques
Aucun : 0 clé fausse, 0 donnée infidèle, 0 figure fausse.

### Majeurs (9 questions à reprendre)

**M1 — M10 Q4 : la clé est déjà donnée, et le gabarit est répété.**
- L'explication de Q2 écrit « ومن لهم 3 هواتف على الأكثر هم 22 + 30 = 52 عائلة ». C'est l'énoncé et la clé de Q4.
- La clé de Q3 contient aussi 52. Le gabarit (lecture directe d'un point ; pièges : effectif, point précédent, point suivant) est celui de M14 Q4 et M15 Q4.
- **Correctif : Q4 réécrite, figure inchangée, clé en `b`.**
  - Énoncé : « يمثّل المضلّع التالي التكرارات المجمّعة الصاعدة لعدد الهواتف المحمولة لدى 100 عائلة: فاصلة كلّ نقطة هي عدد الهواتف، وترتيبتها هي عدد العائلات التي لها هذا العدد من الهواتف على الأكثر.\nبقراءة المضلّع، كم عائلة لها 3 أو 4 هواتف ؟\n<svg…> »
  - Options : a « 85 » [`math.alg.reponse-a-l-autre-inconnue`] · b « 63 » · c « 33 » · d « 30 ».
  - Explication : « «3 أو 4 هواتف» تعني العائلات التي لها 4 هواتف على الأكثر ما عدا التي لها هاتفان على الأكثر: نطرح ترتيبة الفاصلة 2 من ترتيبة الفاصلة 4، أي 85 − 22 = 63 عائلة ✓، وهو ما يعطيه الجدول أيضًا: 30 + 33 = 63. الخطأ الشائع: الاكتفاء بترتيبة الفاصلة 4 دون طرح، فنجد 85؛ أو طرح ترتيبة الفاصلة 3 بدل 2، فنجد 85 − 52 = 33 وتسقط العائلات التي لها 3 هواتف؛ أو الوقوف عند الفاصلة 3، فنجد 52 − 22 = 30 وتسقط العائلات التي لها 4 هواتف. »

**M2 — M13 Q1 : l'option (b) « 3 و4 » est éliminée à vue.**
- Elle contredit « ثلاثة أعداد معيّنة » dans l'énoncé.
- **Correctif :** remplacer (b) par « 3 و4 و6 » (étiquette inchangée).
- Dans l'explication, remplacer « أو الاكتفاء بمعياري القسمة على 12 (أي 3 و4) ونسيان 5 (والعدد 12 نفسه لا يقبل القسمة على 15). » par « أو الاكتفاء بقواسم 12، أي 3 و4 و6، ونسيان 5: العدد 12 نفسه يقبل القسمة على 3 و4 و6 ولا يقبلها على 15. »

**M3 — M13 Q5 : la clé est l'union de moitiés de deux distracteurs.**
- La 4ᵉ option ajoutée par l'auteur, (a) « a = 3 و b = 1 و c = 2 », crée une majorité a = 3. Avec b = 6 et c = 0 (majoritaires déjà), un vote chiffre par chiffre reconstruit la clé (3, 6, 0) sans aucun calcul. Les 3 options officielles laissaient une égalité sur a.
- **Correctif :** (a) devient « a = 5 و b = 1 و c = 6 ». Somme des chiffres 48, bc = 16 divisible par 4, c = 6 : l'option n'échoue que sur le critère de 5, l'étiquette reste juste.
- Dans l'explication, remplacer « و a = 3 و b = 1 و c = 2 يعطي c = 2 فلا يقبل العدد القسمة على 5. » par « و a = 5 و b = 1 و c = 6 يعطي c = 6 فلا يقبل العدد القسمة على 5، مع أنّ مجموع أرقامه 48 و bc = 16 مضاعف للعدد 4. »

**M4 — M14 Q6 est un doublon exact de M11 Q6.**
- Même grille de classes [0 ; 20[ … [80 ; 100[, même seuil « moins de 60 ».
- Mêmes trois pièges : classe suivante incluse, arrêt à 40, classe [40 ; 60[ seule. Même phrase d'explication.
- **Correctif :** (c) « 34 % » devient « 40 % » [`math.alg.reponse-a-l-autre-inconnue`].
- Explication : « يكون الإنتاج أقلّ من 60 كغ في الفئات الثلاث الأولى وحدها، أمّا الفئة [60 ; 80[ فتبدأ عند 60 كغ ولا تدخل: 20 + 84 + 136 = 240 شجرة من 400، فالاحتمال 240 ÷ 400 = 0,6 = 60 % ✓. الخطأ الشائع: 40 % = (108 + 52) ÷ 400 هو احتمال الحدث المعاكس، أي إنتاج 60 كغ أو أكثر؛ و26 % = 104 ÷ 400 يتوقّف عند 40 كغ؛ و87 % = 348 ÷ 400 يضمّ الفئة [60 ; 80[. »

**M5 — M15 Q2 est un doublon exact de M14 Q2.**
- Mêmes pièges : division par 5 ; moyenne des centres sans pondération, qui coïncide avec le centre de la classe modale ; bornes inférieures. L'explication est la même, seuls les nombres changent.
- **Correctif :** options a « 3250 » · b « 187,5 » · c « 175 » · d « 162,5 » ; `correctOption` passe à « d ». La valeur 137,5 disparaît. 187,5 = (100 × 25 + 150 × 15 + 200 × 30 + 250 × 20 + 300 × 10) ÷ 100.
- Phrase des erreurs : « الخطأ الشائع: 187,5 = (100 × 25 + 150 × 15 + 200 × 30 + 250 × 20 + 300 × 10) ÷ 100 يعوّض كلّ فئة بطرفها الأكبر بدل مركزها؛ و175 = (75 + 125 + 175 + 225 + 275) ÷ 5 يأخذ معدّل المراكز دون ترجيحها بعدد العمّال، وهو هنا مركز الفئة المنوال أيضًا؛ و3250 = 16 250 ÷ 5 يقسم على عدد الفئات بدل عدد العمّال 100، فيعطي زيادة تتجاوز أكبر طرف 300. »

**M6 — M15 Q4 est identique à M14 Q4 (et à M10 Q4).**
- **Correctif : passer à une lecture inverse**, qui prépare aussi Q5. Figure inchangée, clé en `b`.
  - Énoncé : « يمثّل المضلّع التالي التكرارات المجمّعة الصاعدة للزيادة في المرتب الشهري لـ 100 عامل: فاصلة كلّ نقطة هي قيمة زيادة بالدينار، وترتيبتها هي عدد العمّال الذين تقلّ زيادتهم عنها.\nبقراءة المضلّع، ما القيمة بالدينار التي تقلّ عنها زيادات 70 عاملًا بالضبط ؟\n<svg…> »
  - Options : a « 250 » · b « 200 » · c « 150 » · d « 70 » [`math.vec.coordonnees-point-inversees`].
  - Explication : « نبحث عن النقطة التي ترتيبتها 70 ثمّ نقرأ فاصلتها: هي 200، فـ 70 عاملًا (25 + 15 + 30) تقلّ زياداتهم عن 200 دينار ✓. الخطأ الشائع: 150 هو الطرف الأصغر للفئة [150 ; 200[، والتكرار المجمّع لفئة يُقرأ عند طرفها الأكبر؛ و250 فاصلة النقطة الموالية التي ترتيبتها 90؛ و70 هي الترتيبة نفسها، أي عدد عمّال لا قيمة زيادة. »
- Ce choix ne fuit rien : 70 ne concerne pas Q6 (seuil 150), et Q5 donne déjà le point (200 ; 70).

**M7 — M16 Q2 : la clé est la seule option qui nomme « ج », le type que cite l'énoncé.**
- **Correctif :** options a « يزيد كمّية النوع الأرخص ثمنًا » · b « يزيد كمّية النوع الأغلى ثمنًا » [`mode-et-valeur-maximale-confondus`, conservée] · c « يشتري من الأنواع الأربعة كمّيات متساوية » · d « يزيد كمّية النوع الأكثر مبيعًا » (clé).
- L'élève doit maintenant comprendre que الأكثر رواجًا = الأكثر مبيعًا.
- L'explication reste valable ; remplacer seulement « النوع د لأنّه الأغلى أو النوع أ لأنّه الأرخص » par « النوع الأغلى أو النوع الأرخص ».

**M8 — M16 Q4 copie la mission publiée 09 Q7, et son énoncé fournit un indice.**
- Mêmes quatre motifs d'options (n/2 et n/2+1 ; n/2−1 et n/2 ; n/2 seul ; (n+1)/2), même étiquette, explication quasi mot pour mot ; seul n passe de 40 à 100.
- De plus, « ما رتبتا القيمتين اللتين يُحسب معدّلهما » annonce deux rangs, ce qui élimine à vue (c) et (d).
- **Correctif :**
  - Énoncé : « نرتّب القوارير المباعة، وعددها 100، تصاعديًّا حسب ثمنها.\nعند أيّ رتبة أو رتبتين نقرأ الوسيط (الموسّط) ؟ »
  - Options : a « الرتبتان 50 و51 » (clé) · b « الرتبتان 49 و50 » · c « الرتبة 50 وحدها » [étiquette conservée] · d « الرتبتان 2 و3 ». L'option (d) remplace « الرتبة 50,5 » : c'est l'erreur de ranger les 4 prix sans leurs effectifs, la même qui donne 425 en Q5.
  - Explication : « نرتّب أثمان القوارير المئة كلّها، لا الأثمان الأربعة المختلفة وحدها. عددها 100 عدد زوجي، فالوسيط (الموسّط) هو معدّل القيمتين ذواتَي الرتبتين 100 ÷ 2 = 50 و50 + 1 = 51 ✓. الخطأ الشائع: ترتيب الأثمان الأربعة دون تكراراتها، فتصير الرتبتان الوسطيان 2 و3؛ أو الاكتفاء بالرتبة 50 وحدها؛ أو النزول رتبة واحدة إلى الرتبتين 49 و50. »

**M9 — M17 Q3 : de l'arabe à l'intérieur d'un groupe de notation entre parenthèses.**
- La ligne est « أزواج (المدّة بالدقيقة ; عدد الزائرين) : (20 ; 1200) و… ».
- Vérifié avec `isolateLtrRuns` : la « ) » de fermeture est absorbée dans le bloc gauche-à-droite `) : (20 ; 1200)`. La parenthèse du modèle ne se ferme pas avant le premier couple, et une parenthèse parasite apparaît après les deux-points.
- **Correctif :** remplacer cette ligne par les deux lignes utilisées en Q1 et Q4 :
  « المدّة الزمنية بالدقيقة : 20 ، 40 ، 60 ، 80 ، 100 ، 120\nعدد الزائرين : 1200 ، 2000 ، 850 ، 450 ، 300 ، 200 »

### Mineurs

1. **Terminologie, voir aussi la section dédiée.**
   - Ajouter « (الموسّط) » à la première mention du médian en M11 Q5, M14 Q5 et M15 Q5, par exemple « الوسيط (الموسّط) هو العمر الذي… ».
   - En M13 Q6, écrire « التواتر المجمّع الصاعد (التراكمي الصاعد) » : c'est le mot du sujet 2016.
2. **M11 Q1 :** remplacer 1100 par 100 [`math.stat.population-et-caractere-confondus`].
   - Options triées : a 100 · b 490 · c 980 · d 1000, clé d.
   - Explication : remplacer « و1100 = 5 × 220 يفترض… » par « و100 هو الطرف الأكبر لآخر فئة عمرية، أي قيمة من قيم الميزة لا عدد من السكّان. »
3. **M11 Q3 et M14 Q3 : ordre ambigu des effectifs.**
   - M11 : « تكرارات الفئات الخمس، من أصغر الأعمار إلى أكبرها، هي 220 و490 و210 و60 و20، والتكرار الكلّي 1000. »
   - M14, qui ne redonne pas les classes : « تكرارات الفئات [0 ; 20[ و [20 ; 40[ و [40 ; 60[ و [60 ; 80[ و [80 ; 100[ هي على الترتيب 20 و84 و136 و108 و52. »
4. **M11 Q4 :**
   - (d) est étiquetée `effectif-cumule-non-cumule` dans le mauvais sens : l'élève lit un cumul comme la part de la classe. Retirer l'étiquette.
   - (c) (axes échangés) devrait recevoir `math.vec.coordonnees-point-inversees` : l'explication nomme déjà l'erreur (règle R1).
5. **M12 Q5, explication de 38,5 :** remplacer la phrase « تسجيل كلّ مقاس مرّة واحدة… » par « أو أخذ منتصف أصغر مقاس وأكبره (36 + 41) ÷ 2 = 38,5 ». On peut alors l'étiqueter `math.stat.mediane-au-milieu-des-extremes`.
6. **M13 Q3 :**
   - (a) devrait recevoir `math.alg.transposition-sans-changer-signe`. Remplacer « أو ضمّ العددين بدل طرح أحدهما من الآخر فنجد 5/3 » par « أو نقل 2/3 إلى الطرف الآخر دون تغيير إشارته: 1 + 2/3 > |x|، فنجد |x| < 5/3 ».
   - L'étiquette de (b) parle de crochets alors que l'option est une inégalité : utiliser `seuil-strict-borne-incluse` si elle est créée.
7. **Étiquettes manquantes (règle R1).** Ces trois options devraient recevoir `math.alg.reponse-a-l-autre-inconnue` :
   - M10 Q5 (b) 52 % : oubli du complément ;
   - M13 Q6 (d) 22 : résultat intermédiaire ;
   - M15 Q6 (c) 60 % : événement contraire.
8. **M13 Q2 :** 88 et 2200 dépassent les 25 matchs de l'énoncé, donc s'éliminent sans la notion. C'est acceptable pour une question préparatoire, mais 2200 peut devenir 12 (= 100 − 88 lu comme un nombre de matchs).
9. **M14 Q4 :** la lecture est directe (règle de lecture donnée, points étiquetés), donc d1 en réalité ; elle reste d2 seulement pour garder sa place. Remplacer « لهذه السلسلة : … وترتيبتها هي عدد الأشجار التي يقلّ إنتاجها عنه » par « لإنتاج 400 شجرة زيتون: … وترتيبتها هي التكرار المجمّع الصاعد الموافق له ». L'élève applique alors lui-même la définition de Q3.
10. **Gabarits d'explication recopiés** (espace de pièges étroit, donc voisinage légitime) : M14 Q1 et M15 Q1, M10 Q3 et M15 Q3, M14 Q3 et la mission publiée 09 Q5. Il suffit de réécrire les explications avec d'autres mots. Les distracteurs [0 ; 20[ (M14 Q1) et [200 ; 250[ (M15 Q1) ne portent aucune erreur identifiable.
11. **M14 Q6 :** la clé « 60 % » fait écho à « 60 كغ » dans l'énoncé. C'est une coïncidence des données officielles ; simple réserve.
12. **M15, figure :** ajouter une marque de coupure près de l'origine de l'axe horizontal (optionnel).
13. **Accords nombre–nom :**
    - M16 Q3 : « 350 و400 و450 و500 مليمًا » devient « … و500 مليم » ;
    - M17 Q2 : « قضّى 1200 زائرًا » devient « قضّى 1200 زائر ».
14. **M17 Q6 :** remplacer (d) 24 % par 36 % [`math.alg.reponse-a-l-autre-inconnue`]. Dans l'explication, remplacer « و24 % = 1200 ÷ 5000 هي نسبة المدّة 20 وحدها » par « و36 % = 1800 ÷ 5000 هي نسبة من قضّوا ساعة أو أكثر، أي المتمّم ».
15. **M17 Q5 :** retirer la compétence `math.prob.frequence-et-chance`, la question est un simple dénombrement.
16. **Parenthèses d'unité collées aux données.** Le moteur déplace la parenthèse dans le bloc de la formule. Écrire l'unité sans parenthèses :
    - M14 Q1 : « الإنتاج (كغ) : » devient « الإنتاج بالكيلوغرام : » ;
    - M15 Q1 : « (بالدينار): » devient « بالدينار: » ;
    - M11 Q2, M14 Q2, M15 Q2 : l'unité placée après le dernier intervalle passe avant la liste des classes ;
    - M14 Q6 : « (بالكيلوغرام). » devient « …، والإنتاج بالكيلوغرام. » ;
    - M11 Q3 : voir le point 3 ;
    - M13 Q6 : « 3 (نسبة … على الأكثر) » devient « 3، أي نسبة … على الأكثر، ».
17. **M10 et M16 n'ont que 5 questions** (6 dans le modèle standard ; le seuil anti-précipitation reste respecté). Simple observation.
18. **Renvois à une question précédente :**
    - M14 Q4 : « لهذه السلسلة » (corrigé par le point 9) ;
    - M15 Q4 : « لهذه السلسلة » (corrigé par M6) ;
    - M11 Q4 et Q5 : « هذا الحيّ » ; remplacer par « سكّان حيّ ».

## Doublons

**(a) Avec les missions publiées :**
- M16 Q4 copie 09 Q7 : défaut majeur, voir M8.
- M14 Q3 reprend le gabarit de 09 Q5 (cumul d'une seule classe ; pièges : classe seule, classe précédente, sens décroissant) : mineur, point 10.
- Les questions moyenne (M11, M14, M15 Q2) partagent 2 pièges sur 3 avec 09 Q3 : voisines légitimes.
- Aucun jeu de données publié n'est repris.

**(b) Entre les huit missions :**
- **Vrais doublons** (mêmes pièges, même explication, seuls les nombres changent) :
  - M14 Q2 et M15 Q2 (voir M5) ;
  - M14 Q4, M15 Q4 et M10 Q4 (voir M6 et M1) ;
  - M11 Q6 et M14 Q6 (voir M4).
- Les correctifs proposés laissent quatre angles distincts pour les lectures de polygone : intervalle (M10), sens d'un point (M11), lecture directe (M14), lecture inverse (M15). Ils laissent aussi trois jeux de pièges différents pour les Q6.
- **Voisines légitimes :**
  - Les Q5 (médiane approchée) de M11, M14 et M15 : le sous-sujet se répète d'une session à l'autre. Le piège « oubli de la borne » est inhérent ; les deux autres pièges diffèrent en partie.
  - M11 Q3 (en fréquences), M14 Q3 (une seule classe) et M11 Q1 (effectif total) ont des angles propres.
  - M14 Q1 / M15 Q1 et M10 Q3 / M15 Q3 : même gabarit, mais l'espace de pièges est étroit (point 10).
- Aucune mission ne diffère d'une autre par ses seuls nombres une fois M4 à M6 appliqués.

## Les quatre étiquettes proposées par l'auteur

1. **`borne-de-classe-au-lieu-du-centre`**
   - Présente en M11 Q2 (d) 23,4, M14 Q2 (d) 44,4 et M15 Q2 (d) 137,5, toutes avec la borne **inférieure**.
   - Même erreur dans la mission publiée 09 Q3 : (a) 15,25 borne inférieure et (d) 25,25 borne supérieure, non étiquetées. Cela fait 5 occurrences.
   - L'intitulé doit viser « une des bornes ». Proposition : fr « Tu remplaces chaque classe par l'une de ses bornes au lieu de son centre : le centre est la moyenne des deux bornes » ; ar « تعوّض كلّ فئة بأحد طرفيها بدل مركزها: مركز الفئة هو معدّل طرفيها ».
   - **À créer.**
2. **`somme-ponderee-divisee-par-le-nombre-de-classes`**
   - Présente en M14 Q2 (a) 4352 (÷ 5 classes), M15 Q2 (a) 3250 (÷ 5 classes) et M17 Q4 (a) 40 833,3.
   - Pour M17, le libellé est inexact : c'est une division par 6 valeurs distinctes d'une série discrète, pas par des classes.
   - C'est exactement « الخطأ الأشهر » du cours (§ المعدّل), qui n'a aujourd'hui aucune étiquette. Proposition : `math.stat.moyenne-divisee-par-le-nombre-de-valeurs`, fr « Tu divises la somme des produits par le nombre de valeurs (ou de classes) au lieu de l'effectif total » ; ar « تقسم مجموع الجداءات على عدد القيم (أو الفئات) بدل التكرار الكلّي ».
   - Réserve : les trois valeurs sortent largement de l'étendue des données. Elles s'éliminent par la vérification que le cours enseigne (la moyenne est entre la plus petite et la plus grande valeur). C'est acceptable comme piège qui récompense cette vérification.
   - **À créer, avec ce libellé généralisé.**
3. **`seuil-strict-borne-incluse`**
   - **Exacte** pour M10 Q5 (a) 78 % (« plus de 3 » compté avec 3), M17 Q5 (a) 4050 et M17 Q6 (a) 81 % (« moins d'une heure » compté avec 60 min).
   - Meilleure aussi que l'étiquette actuelle pour M13 Q3 (b) |x| ≤ 1/3. Pour M13 Q4 (c), l'étiquette existante `intervalle-borne-mal-incluse` reste la bonne.
   - **Inexacte** pour M11 Q6 (a) 98 %, M14 Q6 (a) 87 % et M15 Q6 (d) 70 %. Là, l'élève ajoute toute la classe [60 ; 80[ ou [150 ; 200[, c'est-à-dire qu'il lit le cumul à la borne suivante ; ce n'est pas « la borne incluse ». Soit on les laisse sans étiquette, soit on crée une seconde entrée (3 occurrences), par exemple fr « Tu comptes la classe qui commence au seuil : « moins de 60 » s'arrête à la borne 60, la classe [60 ; 80[ est au-dessus ».
   - Ne s'applique pas à M12 Q3 (d) 29 : on y ajoute une valeur au-delà du seuil, pas une borne.
   - Libellé proposé : fr « Tu inclus la borne alors que l'inégalité est stricte : « plus de 3 » exclut 3, « moins de 60 » exclut 60 » ; ar « تُدخل الحدّ والمتراجحة صارمة: «أكثر من 3» لا تشمل 3، و«أقلّ من 60» لا تشمل 60 ».
   - **À créer**, pour 3 ou 4 occurrences exactes.
4. **`interpolation-borne-inferieure-oubliee`**
   - Présente en M11 Q5 (d) 11,4, M14 Q5 (d) 14,1 et M15 Q5 (d) 16,7, et elle décrit exactement l'erreur.
   - Proposition : fr « Tu calcules le décalage dans la classe mais oublies d'y ajouter sa borne inférieure » ; ar « تحسب الزيادة داخل الفئة وتنسى إضافة طرفها الأصغر ».
   - **À créer.**

Une entrée non proposée par l'auteur est récurrente : `math.stat.cumul-croissant-decroissant-confondus`. On la trouve en M10 Q3 (d), M11 Q3 (c), M11 Q4 (b), M14 Q3 (b), M15 Q3 (c) et dans la mission publiée 09 Q5 (b), soit 6 fois.

## Programme et ordre d'enseignement

- Tout ce qui est testé relève du chapitre 07 ou de chapitres antérieurs : 15 (divisibilité par 12, 15 et 4), 01 (le symbole ∪), 19 (|x|), 04 (intervalles, inéquations). Aucun vecteur, aucune translation.
- **Donnés dans les énoncés, et vérifiés un par un :**
  - l'étendue (M17 Q1) ;
  - la classe modale, « الفئة المنوال » (M14 Q1, M15 Q1) ;
  - le sens d'un point du polygone cumulé (M10 Q4 et Q5, M14 Q4, M15 Q4 ; pour M11 Q4, via la définition donnée en Q3) ;
  - la procédure d'interpolation (Q5 de M11, M14 et M15) ;
  - « |x| est la distance de x à 0 » (M13 Q4) ;
  - la fréquence cumulée et le cumul croissant d'une classe (M11 Q3, M13 Q2 et Q6, M14 Q3, M15 Q3).
- **Une seule technique testée n'est ni enseignée ni donnée telle quelle :** traduire |x| < a en intervalle ]−a ; a[ (M13 Q4). Elle est au programme officiel (manuel, ch. 7, encadré 5) mais ne figure pas dans les cours 04 et 19 de l'app. Elle reste déductible du rappel « distance à 0 » et de la notation des intervalles du chapitre 04 ; c'est acceptable pour la mission.
- **Lacunes de cours hors tranche, à signaler :**
  - Le cours du chapitre 07 n'enseigne pas des notions que le manuel CNP (ch. 8, p. 112 à 119) enseigne : المدى, الفئة المنوال (nommée), le terme officiel الموسّط, التكرار/التواتر التراكمي الصاعد والنازل, les polygones cumulés, la médiane graphique d'une série continue.
  - Le cours du chapitre 04 n'a pas « |x| < a ⟺ x ∈ ]−a ; a[ ».

## Terminologie : « الوسيط (الموسّط) »

- La formule est cohérente avec le cours : le terme appris, « الوسيط », vient en premier, et le terme de l'examen suit entre parenthèses.
- « الموسّط » est aussi le terme du manuel officiel (« الموسّط (Med) », p. 114 et 119). C'est donc le cours qui s'écarte de la terminologie officielle ; il faudrait l'y introduire (hors tranche).
- Dans la tranche, l'usage est irrégulier : M10, M12 et M16 l'emploient ; M11, M14 et M15 ne l'emploient pas, alors que leurs sujets disent « موسّط » (mineur 1).
- Même remarque pour « المجمّع (التراكمي) » : le terme officiel apparaît en M10 et M11, pas ailleurs.

## Hors périmètre : rendu du texte arabe

Dans le moteur, `isolateLtrRuns` et `splitMathRuns` placent dans le bloc gauche-à-droite une parenthèse ou des deux-points collés à une formule. Par exemple, « … = 100 ✓ (والأخير … ) » affiche la « ( » avant la formule. Ce motif est systémique : 61 explications de maths déjà publiées l'utilisent. Je ne l'ai donc pas compté comme défaut de la tranche, sauf M9 (de l'arabe dans une notation entre parenthèses) et le mineur 16 (énoncés). Il est à corriger côté moteur : retirer des bords du bloc les crochets et parenthèses non appariés.

## Bilan chiffré

- 46 questions auditées, toutes re-résolues à l'aveugle.
- 0 clé fausse, 0 défaut critique.
- 4 figures justes (24 points recalculés), aucune ne marque la clé.
- 9 questions à reprendre, défauts majeurs : M10 Q4, M13 Q1, M13 Q5, M14 Q6, M15 Q2, M15 Q4, M16 Q2, M16 Q4, M17 Q3.
- 18 corrections mineures, essentiellement du texte et des étiquettes.
- Fidélité aux sujets officiels respectée partout : données, unités, ordre des sous-questions ; les trois points signalés par l'auteur (Q3 de 2010 technique = médiane ; moyenne de 2011 technique en deux étapes ; 4ᵉ options et questions préparatoires de 2013 et 2016) sont vérifiés, sans perte, sauf le mot « التراكمي » de 2016.
- Aucun fichier du dépôt modifié.