# Audit en aveugle — lot SVT-L04 (gisement 9ᵉ, SVT, examens nationaux)

Auditeur indépendant (n'a rien écrit de ce qui est audité). Commencé le 2026-10-11, coupé par la limite de session, repris de zéro et terminé le 2026-10-12.

## État d'avancement

- [x] Prompt lu
- [x] Skill content-audit invoqué, consigne gisement-auditeur.md lue en entier (bloc L14/L16 compris) — reprise du 12-10 après coupure du 11-10
- [x] Contexte : cours ch.01, 02, 05, 07, 08, 09, 10, 11 lus sur origin/main (edb6e795) ; registre et 969 questions publiées + 54 des lots L02/L03 indexés
- [x] PDF officiels (C01 2026, C02 2025, C03 2024, C04 2022, C05 2021) lus, figures regardées à 300 dpi
- [x] 09/07 (2026 ex.1) — réserve mineure
- [x] 09/08 (2025 ex.5) — défaut majeur (renvoi à une figure absente en Q3/Q4)
- [x] 09/09 (2024 ex.3) — réserve mineure
- [x] 10/07 (2021 ex.1) — réserve mineure
- [x] 11/07 (2025 ex.1) — défaut majeur (fréquence du lieu en Q3)
- [x] 11/08 (2022 ex.3) — réserve mineure
- [x] 11/09 (2021 ex.3) — réserve mineure (+ erreur du cours 11 hors périmètre)
- [x] Étiquettes nouvelles (familles A et B) — § 8
- [x] Doublons, fuites, rendu arabe, figures en Chromium — § 9 à 12
- [x] Chiffre final — § 13 (audit terminé le 12-10)

---

## Cadre de l'audit

- Corpus `origin/main` = `edb6e795` (fetch du 12-10) ; arbre de travail lu tel quel. Empreintes sha256 des sept fichiers prises au début de la reprise (`/tmp/audit-svt-l04/work/sha-start.txt`).
- Résolution à l'aveugle : extraction sans `correctOption`/`answerKey`/`explanation`/`misconceptionTag` (script `blind.py`), réponses consignées dans `/tmp/audit-svt-l04/work/blind-answers.txt` AVANT la levée des clés.
- `content:tranche --subject sciences-vie-terre --chapters 09,10,11 --fresh` (moteur, lecture seule) : 31 questions neuves ; clé strictement la plus longue 0/23 mcq ; positions a 6 · b 6 · c 6 · d 5 ; paires proches (Jaccard ≥ 0,45) 0 ; candidats gabarit 0.
- Doublons cherchés dans 969 questions SVT publiées (`origin/main`) + 54 questions des lots L02/L03 de l'arbre de travail.

## 1. `09-al-ikhraj/exercices/07-examen-2026-ex1-…-ammoniac.json` (2026 ex.1, QCM)

Transcription et PDF (C01 p. 1) concordent : les quatre QCM officiels sont repris un pour un, options officielles intactes (Q2 complétée), clés officielles conservées (nerfs → d, enzymes → d, contraction → b, ammoniac → c).

| Q | ma réponse (aveugle) | clé du fichier | verdict | motif |
| --- | --- | --- | --- | --- |
| Q1 (d1) contraction ventriculaire | « إلى الشّرايين » | b = « إلى الشّرايين » | OK | ch.07 : « ينقبض البطينان معًا فيتمّ ضخّ الدّم في الشّرايين » |
| Q2 (d2) nerfs rachidiens | « تنتمي إلى الجهاز العصبيّ المحيطيّ كسائر الأعصاب » | d | OK | compléments vérifiés : a, b, c restent fausses pour les nerfs rachidiens |
| Q3 (d2) rôle des enzymes | « تسريع تبسيط الأغذية العضويّة » | a | OK | ch.05 : l'enzyme facilite l'action de l'eau qui simplifie |
| Q4 (d2) sécrétion de l'ammoniac | « الأنبوب البولي » | c | réserve | clé juste ; étiquette inexacte sur d |

Clés fausses : 0/4.

**Vérifications.**
- Q2 (options complétées) : a « تنبثق من المخّ وتصل إلى أعضاء الرّأس والوجه » = traits des nerfs crâniens (cours 01 : crâniens issus de l'encéphale, au service de la tête et du visage) → faux pour les rachidiens ; b « 12 زوجًا موزّعة على طول النّخاع » = hybride (nombre des crâniens, position des rachidiens) : faux pour les deux familles, mais il exécute bien l'erreur de l'étiquette (le nombre 12) ; c « تنبثق من البصلة الشّوكيّة الموجودة أسفل المخيخ » = bulbe, partie de l'encéphale (cours 01) → faux pour les rachidiens. Le complément « كسائر الأعصاب » de la clé est vrai (cours 01 : le système périphérique est fait des nerfs). Clé 45 caractères contre 46 pour b : pas la plus longue. Une seule bonne réponse.
- Q3 : options officielles inchangées, clé déplacée ; « أكسدة » (ch.08) et « امتصاص » (ch.05) sont enseignés avant le ch.09.
- Q4 : terme « النّشادر » = celui du cours 09 (tableau et « إفراز بعض المواد كالنّشادر: تفرزها خلايا الأنبوب البوليّ »).
- Étage d2 practice 75/15 honnête pour quatre QCM de connaissance dont deux à piège ; rampe 1,2,2,2 non décroissante ; titre conforme (« 🏛️ مناظرة 2026 · التمرين 1 ⭐⭐: … »), il nomme des notions, aucun résultat ; displayOrder 7.
- Programme : Q1 ch.07, Q2 ch.01, Q3 ch.05 (+ ch.08 pour l'oxydation), Q4 ch.09 : tout est antérieur ou égal au ch.09.
- Rendu : arabe pur, aucun chiffre arabo-indien, aucune formule.

**Défauts.**
- [mineur] **Q4 option d « القناة الجامعة » — étiquette `bio.excr.etape-du-nephron-confondue` à retirer.** Le libellé (« Tu attribues une variation à la mauvaise étape : plasma → urine primitive juge la filtration ; urine primitive → finale, réabsorption ou sécrétion ») corrige une erreur d'ÉTAPE ; l'élève qui choisit d sait que l'ammoniac est ajouté entre urine primitive et urine finale (c'est bien une sécrétion), il se trompe de STRUCTURE (lieu où l'on mesure l'urine finale pris pour le lieu de la sécrétion). Le libellé ne nomme pas cette erreur ; aucune étiquette existante ne la nomme → option muette. Sur a « الكبيبة » et b « محفظة بومان », l'étiquette est acceptable : l'élève place l'ajout de l'ammoniac à l'étape de filtration, ce que corrige la première moitié du libellé (et l'explication raisonne bien en variation 0 → 0 → 0,5).
- [mineur] **Q1 explication, mécanisme de piège imprécis et verbe d'écrit.** « الخلط بين الانقباضين فيُكتب «البطينين» أو «الأذينتين» » : confondre les deux contractions donne « les ventricules » (destination de la contraction auriculaire), pas « les oreillettes » ; et l'élève ne « écrit » rien dans un QCM. Remplacer la dernière phrase par : « الخطأ الشائع: الخلط بين الانقباضين فيُختار «إلى البطينين»، وهو مقصد الانقباض الأذينيّ، أو إغفال انغلاق الصمّامات الأذينيّة-البطينيّة فيُختار «إلى الأذينتين»، أو عكس اتّجاه الدّم فيُختار «إلى الأوردة» لأنّها الأوعية المتّصلة بالقلب. » (les trois options citées par leur texte, aucune lettre ; le renvoi aux valvules est au cours 07 ; aucune autre question de la tranche n'en dépend).
- [réserve, sans correction exigée] **Doublon d'idée entre annales (Q3).** Le même fait est posé par `08-at-tanaffus/exercices/09-examen-2020-ex1…` Q2 (lot L03, arbre de travail : « تقوم الأنزيمات الموجودة في العصارات الهاضمة بـ: », mêmes pièges fragmentation et absorption, mêmes étiquettes) et par `05-al-hadm/exercices/02-tamrin.json` Q1 (publié : « ما دور الأنزيم في الهضم الكيميائيّ بدقّة؟ », piège fragmentation). Pas quasi identique (libellés et troisième distracteur différents : « أكسدة » ici, « الأغذية المعدنيّة » en 2020), et les deux reprises sont fidèles à leur sujet : acceptable selon la règle du lot, à arbitrer par l'orchestrateur si le donjon du palier tire les deux.
- Doublons d'idée annoncés par l'auteur, vérifiés : Q4 contre `09-al-ikhraj/exercices/02-tamrin.json` Q4 et `quiz.json` Q3 (interprétation du tableau 0 → 0 → 0,5, options différentes) : pas un doublon. Q2 contre `01-wadhifat-al-ittisal/exercices/02-tamrin.json` Q4 (nerf optique et sciatique → système périphérique) : pas un doublon.

**Verdict 09/07 : réserve mineure** (0 clé fausse ; 1 étiquette à retirer, 1 explication à préciser).

## 2. `09-al-ikhraj/exercices/08-examen-2025-ex5-…-constance-milieu-interieur.json` (2025 ex.5)

Transcription et PDF (C02 p. 4, Document 4) relus ; figure redessinée comparée au scan à 300 dpi et rendue dans Chromium (polices de l'app, conteneurs `ltr` et `rtl`).

| Q | ma réponse (aveugle) | clé du fichier | verdict | motif |
| --- | --- | --- | --- | --- |
| Q1 (d2) zones (أ)/(ب) | « (أ): محفظة بومان ؛ (ب): الأنبوب البولي » | c | réserve | clé juste ; une phrase de l'explication enseigne une inférence fausse |
| Q2 (d2) identité X/Y | « X: الجليكوز ؛ Y: النّشادر » | d | OK | X = 1 g/L (glucose du tableau du cours), Y = 0 → 0,5 (ammoniac) |
| Q3 (d3) rôle envers X et Y | « X filtré puis réabsorbé ; Y non filtré, sécrété » | b | ERREUR de forme (majeur) | clé juste ; l'énoncé renvoie à une figure absente |
| Q4 (d3) constance du milieu intérieur | « يرشّح البلازما ثمّ يعيد إلى الدّم ما ينفع… » | a | ERREUR de forme (majeur) | idem Q3 ; explication imprécise |

Clés fausses : 0/4.

**Figure (Q1 = Q2, deux copies identiques).** Graduations justes (100 unités pour 1 g/L : 0 → y 150, 0,5 → y 100, 1 → y 50) ; quatre zones de 60 unités (46-106-166-226-286). X = 1 jusqu'à x 166 (fin de (أ)), chute et atteint 0 à x 196 (milieu exact de (ب) ; sur le scan, 0 est atteint un peu après le milieu : écart négligeable) ; Y = 0 jusqu'à x 166, atteint 0,5 à x ≈ 190 (40 % de (ب) ; scan ≈ 38 %) ; croisement vers 0,45 (scan ≈ 0,49). Valeurs, unités (g/L), styles (X plein, Y pointillé) fidèles. Rien ne déborde du `viewBox` (mesuré dans les deux sens) ; `check-figures` sans constat ; arabe hors `<title>` limité aux glyphes « أ » et « ب » (admis par `course-figures.md` : « A label is a glyph (`أ`…) »). La figure ne donne aucune clé (ni nom de zone ni nom d'élément). Seules (أ) et (ب) sont étiquetées : la glomérule et le canal collecteur se déduisent de l'ordre donné dans l'énoncé (Q1 le dit « من اليسار إلى اليمين » ; Q2 seulement par l'ordre d'énumération — déductible car أ est à gauche de ب).

**Vérifications.**
- Plans 2×2 : Q1 (أ) ∈ {tube (a, b), capsule (c, d)}, (ب) ∈ {tube (a, c), capsule (b, d)} ; Q2 X ∈ {protides (a, c), glucose (b, d)}, Y ∈ {urée (a, b), ammoniac (c, d)} ; Q3 X ∈ {sécrété (a, d), réabsorbé (b, c)}, Y ∈ {sécrété (a, b), réabsorbé (c, d)}. Chaque valeur de case figure exactement deux fois ; le vote case par case ne reconstruit pas la clé ; les options à deux erreurs (Q1 b, Q2 a, Q3 d) sont muettes.
- Q2 se résout sans Q1 (valeurs de la glomérule et du canal collecteur + tableau du cours 09 : glucose 1 → 0, ammoniac 0 → 0,5, protides 80, urée 0,3). Aucun distracteur n'est vrai sous les données.
- Q1 options a et d (« même structure deux fois », point 5 de l'auteur) : fausses, non réfutables à la seule lecture (il faut savoir que la capsule précède le tube). Q1 se résout aussi par le seul ordre anatomique, sans lire les courbes — comme la question officielle ; acceptable en d2.
- Étiquettes : Q3 a et c `etape-du-nephron-confondue` exactes (variation urine primitive → finale attribuée à la mauvaise opération) ; Q4 b `filtration-selective` exacte (filtre qui « trie » le nuisible de l'utile). Q4 c et d muettes : aucune étiquette existante ne nomme « tout ce qui est filtré est rejeté » ni « l'urine reste constante » — juste.
- Fuites : les explications de Q1 et Q3 ne nomment ni le glucose ni l'ammoniac ; celle de Q4 cite l'eau, les sels et l'urée (pas l'ammoniac) — aucune ne donne la clé de Q2 si elle est vue avant. L'explication de Q2 (glucose, ammoniac) précède logiquement Q3, dont l'énoncé ne redonne pas les identités : la chaîne est légitime.
- Étage d3 boss 120/30 honnête : deux d3 réels (rôle de deux éléments non nommés d'après les données ; explication de la constance). Rampe 2,2,3,3. Titre conforme, sujet sans résultat ; displayOrder 8.
- Fidélité : 1-أ (analyse, identités, zones) → Q1 + Q2, l'analyse passe dans les explications ; 1-ب → Q3 ; 2 → Q4. Aucune sous-question perdue ; données identiques (1 ; 0 ; 0,5 g/L ; « شخص سليم »).
- Doublons : idée commune avec `09-al-ikhraj/exercices/02-tamrin.json` Q3-Q4 et `quiz.json` Q3-Q4 (glucose 1/1/0 réabsorbé, ammoniac 0/0/0,5 sécrété : mêmes données que le tableau du cours). Q3 ici combine deux éléments non nommés en plan 2×2 sur lecture de courbe : pas quasi identique, acceptable.

**Défauts.**
- [majeur] **Q3 et Q4 : l'énoncé renvoie à une figure qu'il ne porte pas.** Les deux énoncés commencent par « تبيّن الوثيقة تطوّر تركيز عنصرين (X) و(Y) … وهي من اليسار إلى اليمين: … » alors que la figure n'est que dans Q1 et Q2. Le donjon tire Q3 ou Q4 seule : l'élève lit « la document montre… de gauche à droite » sans document. Le gabarit `FIGURE_REFERENCE` du moteur ne reconnaît pas « الوثيقة » : aucun gate ne le voit. Les données sont bien redonnées en lignes, donc la question reste soluble (pas critique). Remplacer, dans Q3 ET Q4, la première phrase par : « قِيس لدى شخص سليم تركيزُ عنصرين (X) و(Y) في عيّنات سوائل أُخذت من أربع مناطق متتالية في الكلية: الكبيبة ثمّ المنطقة (أ) ثمّ المنطقة (ب) من النّيفرون ثمّ القناة الجامعة. وهذه النّتائج: » — puis garder les trois lignes de lectures et la question. (Vérifié : ne nomme ni les zones ni les éléments, ne change aucune donnée, ne rend aucun distracteur vrai.)
- [mineur] **« على مسار البول » (Q1, Q3, Q4 et `<title>` de la figure).** La glomérule contient du sang (plasma), pas de l'urine ; l'explication de Q2 compare d'ailleurs la valeur de la glomérule à celle du plasma. Pour Q1, remplacer la première phrase par : « تبيّن الوثيقة تطوّر تركيز عنصرين (X) و(Y) في عيّنات سوائل أُخذت لدى شخص سليم من أربع مناطق متتالية في الكلية، وهي من اليسار إلى اليمين: الكبيبة ثمّ المنطقة (أ) ثمّ المنطقة (ب) من النّيفرون ثمّ القناة الجامعة. » ; dans le `<title>`, « على مسار البول » → « في الكلية ». (Q3/Q4 : voir le correctif majeur ci-dessus, qui l'intègre.)
- [mineur] **Q1 explication : inférence fausse.** « وبما أنّ تركيب سائلي المنطقتين مختلف، فلا يمكن أن تكونا البنية نفسها. » enseigne une règle fausse (la composition varie le long du même tube : dans (ب) même, X passe de 1 à 0). Remplacer cette phrase par : « فالمنطقة «ب» ليست محفظة بومان، لأنّ سائل المحفظة هو البول الأوّليّ الذي لم يتغيّر بعد ؛ والمنطقة «أ» ليست من الأنبوب البوليّ، لأنّ ما رُشِّح يتجمّع في المحفظة قبل أن يدخل الأنبوب. » et, dans « الخطأ الشائع », « رغم اختلاف تركيب سائليهما » → « مع أنّ سائل الأولى لم يتغيّر وسائل الثّانية تغيّر ». (Ne nomme ni glucose ni ammoniac ; aucune fuite vers Q2/Q3.)
- [mineur] **Q4 explication : « ثمّ إفراز وإخراج لفضلات كالبولة تُطرح في البول ».** Le cours 09 donne l'urée comme exemple d'EXCRÉTION et l'ammoniac comme exemple de SÉCRÉTION ; associer « إفراز » à l'urée est inexact. Remplacer par : « ثمّ إفراز فضلات من الدّم إلى البول، وإخراج فضلات سامّة كالبولة في البول النّهائيّ » (ne nomme pas l'ammoniac, pour ne pas livrer la clé de Q2 dans un tirage où Q4 précède Q2).
- Rendu : la figure est rendue en `dir="ltr"` par `SvgFigure` (moteur `origin/main`), les ancres `start`/`end` des étiquettes restent donc justes en interface arabe (vérifié en rendu `ltr` ; le basculement observé avec un `SvgFigure` sans `dir` ne concerne que l'ancien moteur local).

**Verdict 09/08 : défaut majeur** (0 clé fausse ; renvoi à une figure absente dans Q3 et Q4 ; trois mineurs).

## 3. `09-al-ikhraj/exercices/09-examen-2024-ex3-…-trois-prelevements.json` (2024 ex.3)

Transcription et PDF (C03 p. 2, Document 2, scan à 300 dpi) relus ; figure rendue dans Chromium (`ltr` et `rtl`).

| Q | ma réponse (aveugle) | clé du fichier | verdict | motif |
| --- | --- | --- | --- | --- |
| Q1 (d1, mcq 2×2) unité × organe | « النّيفرون ؛ الكلية » | d | réserve | clé juste ; deux options incohérentes s'éliminent sans la figure |
| Q2 (d2, matching) légendes 1-4 | 1 → tube urinaire, 2 → canal collecteur, 3 → capsule de Bowman, 4 → glomérule | l1-r3, l2-r4, l3-r2, l4-r1 | OK | conforme au document officiel |
| Q3 (d2, multi) fonctions du néphron | {a, c, e, f} | {a, c, e, f} | OK | 4 vraies sur 6, conformes aux quatre fonctions du cours 09 |
| Q4 (d3, matching) trois prélèvements | (أ) → capsule, (ب) → canal collecteur, (ج) → glomérule | l1-r2, l2-r3, l3-r1 | réserve | clé juste ; « على مسار البول » inexact pour la glomérule |

Clés fausses : 0/4.

**Figure (Q1 sans numéros = Q2 numérotée).** Tracé conforme au Document 2 : deux artérioles rouges qui convergent sur un peloton rouge dans une capsule jaune, tube sinueux, boucle en U profonde, arceau qui se jette dans un gros tube vertical à deux courts embranchements. Repères vérifiés sur les coordonnées : pointe de « 3 » en (77 ; 59), à 23 unités du centre de la capsule (paroi entre les rayons 22 et 28) → capsule ; pointe de « 4 » en (66 ; 93), sur le bord du peloton (rayon 15) → glomérule ; pointe de « 1 » en (207 ; 44), bord supérieur de l'arceau (courbe à y ≈ 47, trait de 9) → tube urinaire juste avant le canal, comme sur le scan ; pointe de « 2 » à x 255, à 3 unités du canal (236-252) → canal collecteur. Aucune étiquette de nom, rien ne donne une clé ; `<title>` neutre (ne nomme pas le néphron). Aucun débordement (`ltr`, `rtl`), `check-figures` sans constat.

**Vérifications.**
- Q2 et Q4 : appariements uniques ; chaque élément de droite est un partenaire plausible pour plusieurs éléments de gauche (capsule/glomérule, tube/canal ; profils d'échantillons voisins) ; rien ne se devine par élimination avant le dernier couple. Q4 est autonome (positions nommées, pas de numéros : ne livre pas les couples de Q2).
- Q3 : quatre vraies (filtration, réabsorption, sécrétion « كالنّشادر », excrétion « كالبولة والحمض البوليّ ») = la liste du cours 09 ; b (stockage → vessie) et d (transport → uretères) fausses. Le nombre se sait par le cours (« أربع وظائف »), pas par la forme (la vraie a est la plus courte des six).
- Fidélité : légendes 1-4 → Q2 (mêmes repères aux mêmes endroits) ; tableau unité/organe/fonctions → Q1 + Q3 ; trois échantillons des positions 2, 3, 4 → Q4 par NOMS (canal collecteur, capsule, glomérule = positions 2, 3, 4 officielles), données de présence identiques. Aucune sous-question perdue.
- Étage d3 boss 120/30 : acceptable mais à la borne basse — une seule d3 réelle (Q4 : trois profils × trois opérations), Q1 est un acquis immédiat. Rampe 1,2,2,3 ; titre conforme (« … الوحدة الوظيفيّة للكلية — تسمية أجزائها ووظائفها وتحليل ثلاث عيّنات » ne livre aucune clé) ; displayOrder 9.
- Doublons : idée commune avec `09-al-ikhraj/exercices/02-tamrin.json` Q1 (« ما وظائف النّيفرون الأربع بالتّرتيب؟ ») : format et distracteurs différents, acceptable. Aucune question publiée de légendes sur figure au ch.09.

**Défauts.**
- [mineur] **Q1 : plan 2×2 sur deux termes liés.** « النّيفرون ؛ المعي الدّقيق » et « الخملة المعويّة ؛ الكلية » sont incohérentes (un néphron n'est pas dans l'intestin) et tombent sans regarder la figure : la question se réduit à « الخملة المعويّة ؛ المعي الدّقيق » contre la clé. Correctif (reste 2×2, chaque valeur deux fois, l'option à deux erreurs muette, toutes cohérentes dans l'appareil urinaire du ch.09) : a « الكبيبة ؛ المثانة » · b « النّيفرون ؛ المثانة » · c « الكبيبة ؛ الكلية » · d « النّيفرون ؛ الكلية » (clé inchangée, 18 caractères contre 19 pour b : pas la plus longue). Explication : « يمثّل الرّسم النّيفرون كاملًا، وهو الوحدة الوظيفيّة للكلية، ويبلغ عدده قرابة المليون في كلّ كلية. أمّا الكبيبة فجزء من النّيفرون لا الوحدة كلّها، والمثانة كيس يخزن البول مؤقّتًا ولا نيفرون فيها. الخطأ الشائع: تسمية الوحدة باسم أحد أجزائها، أو نسبتها إلى المثانة لأنّ البول يتجمّع فيها. » (Vérifié : ne dit pas quel élément dessiné est la glomérule — aucune fuite vers Q2 ; toutes les notions au cours 09.)
- [mineur] **Q4 énoncé : « في ثلاثة مواضع على مسار البول في الكلية ».** La glomérule contient du plasma (c'est justement ce que trahissent les protides de l'échantillon (ج)). Remplacer par « في ثلاثة مواضع من الكلية ».
- Rendu : figure en `dir="ltr"` (moteur `origin/main`), ancres justes ; rien ne déborde.

**Verdict 09/09 : réserve mineure** (0 clé fausse).

## 4. `10-an-nudj-al-jinsi/exercices/07-examen-2021-ex1-…-ovocyte.json` (2021 ex.1, QCM)

Transcription et PDF (C05 p. 1) concordent ; QCM repris dans l'ordre officiel, clés officielles conservées (d, b, a, d → ici b, d, a, c).

| Q | ma réponse (aveugle) | clé du fichier | verdict | motif |
| --- | --- | --- | --- | --- |
| Q1 (d2) respiration cellulaire | « تحوّل الطّاقة الكامنة بالمغذّيات الخلويّة إلى طاقة قابلة للاستعمال » | b | OK | cours 08 ; compléments de c et d restent faux |
| Q2 (d2) sang riche en O₂ | « الوريد الرّئويّ » | d | OK | cours 07 (piège du vaisseau défini par son contenu) |
| Q3 (d2) petite circulation | « قلب أيمن ← شريان رئويّ ← رئتان ← أوردة رئويّة ← قلب أيسر » | a | réserve | clé juste ; option c muette qui mérite une étiquette existante |
| Q4 (d2) fin de la maturation de l'ovocyte | « إثر دخول حيوان منويّ إليها » | c | réserve | clé juste ; recoupe fortement 10/04-defi Q4 |

Clés fausses : 0/4.

**Vérifications.**
- Q1 : options officielles allongées — c « … بعد تفكيك المغذّيات الخلويّة » (l'O₂ est consommé, pas rejeté) et d « … لبناء المغذّيات الخلويّة داخل الخليّة » (la respiration ne construit pas) restent fausses ; a (« المعدنيّة ») inchangée ; la clé (62 car.) n'est plus la plus longue (d : 70). Une seule bonne réponse.
- Q3 : plan 2×2 des options officielles (sens D→G ou G→D × artère d'abord ou veines d'abord), chaque valeur deux fois, l'option à deux erreurs (b, trajet entièrement inversé) muette. Les flèches « ← » (U+2190, non miroir) se lisent dans le sens de la lecture arabe ; mêmes longueurs pour les quatre options.
- Q4 : options « en situations » toutes fausses selon le cours 10 (maturation achevée seulement à l'entrée du spermatozoïde ; ovocyte libéré à un stade avancé non achevé ; il ne « mûrit » pas dans l'utérus).
- Programme : Q1 ch.08, Q2-Q3 ch.07, Q4 ch.10 ; « البويضة » est le terme du cours.
- Étage d2 practice 75/15 et rampe 2,2,2,2 honnêtes (Q2 et Q3 sont presque des d1, sans conséquence). Titre conforme ; displayOrder 7.
- Étiquette posée : Q2 a `bio.circ.artere-sang-oxygene` exacte.

**Défauts.**
- [mineur] **Q3 option c (« قلب أيمن ← أوردة رئويّة ← رئتان ← شريان رئويّ ← قلب أيسر ») muette, alors qu'une étiquette existante nomme exactement l'erreur** : appeler « veines » le vaisseau qui porte le sang chargé de CO₂ du cœur droit aux poumons et « artère » celui qui ramène le sang oxygéné, c'est définir le vaisseau par son contenu → `bio.circ.artere-sang-oxygene` (« l'artère sort du cœur, la veine y entre »). Porte R1 : l'explication nomme déjà l'erreur (« تبديل اسمي الوعاءين … مع أنّ الشّريان يخرج من القلب والوريد يدخل إليه »). À poser. (L'option d, côtés du cœur inversés, pourrait porter `bio.circ.oreillettes-inversees` — les veines pulmonaires y aboutissent au cœur droit — mais le libellé n'en nomme que la moitié : muette défendable.)
- [mineur] **Explications de Q3 et Q4 : « فيُكتب » et citations d'options qui n'existent pas.** Q4 cite « «في المبيض» أو «قبل الإباضة» », textes officiels courts, alors que les options de la mission sont « في المبيض لحظة تحرّرها منه » et « قبل الإباضة أثناء نموّ الجريب » ; et l'élève ne « écrit » pas dans un QCM. Q4 : remplacer « فيُكتب «في المبيض» أو «قبل الإباضة» » par « فيُختار «في المبيض لحظة تحرّرها منه» أو «قبل الإباضة أثناء نموّ الجريب» ». Q3 : « فيُكتب مسار » → « فيُختار مسار ».
- [réserve, à arbitrer] **Q4 recoupe fortement `10-an-nudj-al-jinsi/exercices/04-defi.json` Q4** (publié, même chapitre) : « متى ينتهي نضج البويضة؟ », même clé (« إثر دخول حيوان منويّ »), deux pièges sur trois communs (avant l'ovulation ; l'utérus), explications différentes. Pas quasi identique au sens de la règle du lot (options et explications distinctes) ; c'est toutefois le recoupement le plus fort de la tranche, dans le même chapitre : si l'orchestrateur veut l'éviter, c'est la question publiée (non officielle) qu'il faut faire évoluer, pas la reprise officielle.
- Doublons d'idée annoncés, vérifiés : Q2-Q3 contre `07-ad-dawaran/exercices/08-examen-2020-ex3…` (matching des vaisseaux, couleurs des vaisseaux : formats différents) et `07-ad-dawaran/exercices/03-boss.json` Q1 (trajet de la petite circulation en flèches, un piège commun, granularité ventricule/oreillette) : pas quasi identiques.
- Observation (sans correction) : Q1 a (« المغذّيات الخلويّة المعدنيّة ») pourrait porter `bio.alim.vitamines-energetiques` si l'élève croit que les minéraux donnent de l'énergie ; l'explication la présente comme une inattention de lecture — deux chemins vers la même option : muette défendable.

**Verdict 10/07 : réserve mineure** (0 clé fausse).

## 5. `11-ad-dawra-al-jinsiya/exercices/07-examen-2025-ex1-…-phase-luteale.json` (2025 ex.1, QCM)

Transcription et PDF (C02 p. 1) concordent. Ordre changé (officiel 3, 1, 2, 4) ; clés officielles conservées (ألياف عصبيّة ; في المعي الدّقيق ; اتّساع مساحة التّبادل ; يتكوّن الشّبيك الرّحمي).

| Q | ma réponse (aveugle) | clé du fichier | verdict | motif |
| --- | --- | --- | --- | --- |
| Q1 (d1) capillaires | « اتّساع مساحة التّبادل » | c | OK | cours 07 (« مساحة واسعة وجدار رقيق وجريان بطيء ») |
| Q2 (d2) substance blanche de la moelle | « ألياف عصبيّة » | a | réserve | clé juste ; distracteur officiel « خلايا عصبيّة رابطة » jamais enseigné |
| Q3 (d2) maltose → glucose | « في المعي الدّقيق بمفعول العصارة المعويّة » | d | ERREUR de forme (majeur) | clé juste et conforme au cours 05 ; le lieu de la clé se trahit par sa fréquence |
| Q4 (d2) phase lutéale | « يتكوّن الشّبيك الرّحمي في بطانة الرّحم » | b | OK | cours 11 (lutéale = prémenstruelle ; 37,1 °C) |

Clés fausses : 0/4.

**Vérifications.**
- Q3, clé recomposée (lieu + suc) : c'est bien celle du programme et du cours 05 (« ثمّ سكّر الشّعير ← جليكوز بمفعول العصارة المعويّة » dans l'intestin grêle ; le suc pancréatique ne fait que amidon → maltose, seul le suc intestinal fait maltose → glucose). Les trois distracteurs sont faux et leurs étiquettes `bio.dig.specificite-enzyme-ignoree` exactes (salive et amylase pancréatique → amidon ; suc gastrique → protides ; porte R2).
- Q4 : option c réécrite « تبدأ الغدد الأنبوبيّة في الظّهور » (l'officielle « تظهر الغدد الأنبوبيّة » pouvait passer pour vraie en phase lutéale, où les glandes existent) : la réécriture la rend sans ambiguïté fausse (phase postmenstruelle, cours 11) — bonne adaptation. d (« دون 37 درجة ») fausse : ≈ 37,1 °C après l'ovulation. Étiquettes : c `phases-uterines-confondues` exacte (événement postmenstruel placé après l'ovulation) ; a (« تتهدّم بطانة الرّحم ») acceptable — le libellé dit « Tu décales les phases utérines » et sa correction (« la dentelle se forme en phase prémenstruelle, après l'ovulation ») répond bien à ce qui se passe en phase lutéale, même si sa dernière proposition (« pas en phase postmenstruelle ») ne concerne que c.
- Q1 et Q2 : options officielles ; aucune n'est vraie ; muettes faute d'étiquette existante (voir § Étiquettes nouvelles : familles B et A).
- Étage d2 practice 75/15 et rampe 1,2,2,2 honnêtes ; titre conforme ; displayOrder 7. Programme : Q1 ch.07, Q2 ch.01, Q3 ch.05, Q4 ch.11.
- Doublons d'idée annoncés, vérifiés : Q2 contre `01-wadhifat-al-ittisal/quiz.json` Q3 (« ممّ تتكوّن المادّة البيضاء في النّخاع الشّوكيّ؟ », options différentes) ; Q1 contre `07-ad-dawaran/exercices/03-boss.json` Q4 et `quiz.json` Q7 (les trois propriétés des capillaires en une option) ; Q3 contre `05-al-hadm/exercices/08-examen-2022-ex4…` Q2 (expérience en tube) ; Q4 contre `11-ad-dawra-al-jinsiya/quiz.json` Q4 et `05-tadrib.json` Q3 (sens inverse). Aucun quasi identique.

**Défauts.**
- [majeur] **Q3 : « في المعي الدّقيق » figure dans deux options (c et la clé d), « في الفم » et « في المعدة » une fois chacune.** Le vote sur le lieu reconstruit la moitié de la clé et réduit la question à c/d sans connaissance (règle « aucune valeur ne trahit la clé par sa fréquence »). Correctif (chaque lieu deux fois, chaque suc une fois, tous cohérents avec le cours 05 qui dit que la salive « يتواصل مفعوله قليلًا » dans l'estomac) : a « في المعدة بمفعول العصارة المعديّة » [`bio.dig.specificite-enzyme-ignoree`] · b « في المعدة بمفعول اللّعاب » [`bio.dig.specificite-enzyme-ignoree`] · c « في المعي الدّقيق بمفعول العصارة المعثكليّة » [`bio.dig.specificite-enzyme-ignoree`] · d « في المعي الدّقيق بمفعول العصارة المعويّة » (clé, 38 caractères contre 40 pour c). Explication : « يتحوّل النّشا إلى سكّر الشّعير بمفعول اللّعاب في الفم، ويتواصل هذا المفعول قليلًا في المعدة، ثمّ بمفعول العصارتين المعثكليّة والمعويّة في المعي الدّقيق ؛ أمّا سكّر الشّعير فيُبسَّط إلى جليكوز في المعي الدّقيق بمفعول العصارة المعويّة وحدها. ولكلّ أنزيم مادّته وحدها: أميلاز اللّعاب وأميلاز العصارة المعثكليّة يعملان على النّشا، والعصارة المعديّة تعمل على البروتيدات. الخطأ الشائع: عدّ كلّ عصارة قادرة على تبسيط كلّ سكّر، فيُنسب تبسيط سكّر الشّعير إلى اللّعاب أو إلى العصارة المعثكليّة لأنّهما تبسّطان النّشا، أو إلى العصارة المعديّة لأنّ المعدة موضع الهضم الأشهر. » (Vérifié : aucune option vraie ; le piège officiel « salive » est gardé ; seul le lieu officiel « في الفم » disparaît, ce qu'impose l'équilibre.)
- [mineur] **Q2 d « خلايا عصبيّة رابطة » : notion qu'aucun cours (ch.01 à 11) n'enseigne** (l'arc réflexe du ch.02 a cinq éléments, sans neurone d'association) ; l'explication l'affirme en substance grise. L'option reste réfutable par le cours 01 (« ولا تحتوي [البيضاء] على أجسام خلويّة ») : pas bloquant. Garder l'option officielle (la remplacer par « خلايا عصبيّة … بأجسامها » ferait chevaucher l'option « أجسام خلويّة ») et corriger seulement l'explication : « وكذلك الخلايا العصبيّة الرّابطة » → « وكذلك الخلايا العصبيّة «الرّابطة» التي تصل بين خليّتين داخل النّخاع: هي خلايا كاملة، وأجسامها الخلويّة لا توجد في المادّة البيضاء ».
- [mineur] **Q1 explication : « فيُكتب سمك الجدار أو ارتفاع الضّغط »** → « فيُختار «سمك جدارها» أو «ارتفاع الضّغط داخلها» ».
- Observation : Q1 a « سمك جدارها » (officiel) se lit « l'épaisseur de leur paroi » ; un élève pointilleux pourrait y voir la minceur. L'explication tranche (« سمك الجدار … من خاصّيّات الشّرايين ») ; si l'on veut lever l'ambiguïté : « جدارها السّميك ».

**Verdict 11/07 : défaut majeur** (0 clé fausse ; indice de fréquence en Q3).

## 6. `11-ad-dawra-al-jinsiya/exercices/08-examen-2022-ex3-…-ovulation.json` (2022 ex.3)

Transcription et PDF (C04 p. 2, Document 2 à 300 dpi) relus ; figures rendues dans Chromium (`ltr`, `rtl`).

| Q | ma réponse (aveugle) | clé du fichier | verdict | motif |
| --- | --- | --- | --- | --- |
| Q1 (d1) événement du dessin أ | « الإباضة » | b | réserve | clé juste ; l'explication donne le critère qui apparie 2 et 3 dans Q2 |
| Q2 (d2, matching) éléments 1-4 | 1 → ovocyte, 2 → follicule rompu, 3 → follicule mûr, 4 → corps jaune | l1-r3, l2-r2, l3-r1, l4-r4 | OK | conforme au document officiel |
| Q3 (d2, ordering) par noms | follicule mûr → follicule rompu → corps jaune | b, c, a | OK | une seule suite |
| Q4 (d2, mcq 2×2) phases | mûr : folliculaire ; corps jaune : lutéale | a | OK | cours 11 |
| Q5 (d2, mcq 2×2) devenir sans fécondation | ovocyte : dégénère vers 24 h ; corps jaune : régresse puis disparaît | c | OK | cours 10 et 11 |

Clés fausses : 0/5.

**Figures.** Dessin أ (Q1 seul, puis dans Q2) : anneau ouvert en haut (arc de rayon 29, centre (244 ; 78) dans Q2), quatre tirets qui jaillissent, petite cellule au-dessus — conforme au scan. Flèche 1 : pointe à x 253, bord de la cellule à 251,5 → ovocyte. Flèche 2 : pointe à 33 unités du centre, dans la paroi (rayons 23,75 à 34,25) → paroi du follicule rompu. Dessin ب : anneau fermé à relief interne en haut à droite portant la cellule → follicule mûr, repère 3 sous le dessin sans flèche comme sur le scan. Dessin ج : masse jaune lobée à cavité centrale → corps jaune, repère 4. Ordre de gauche à droite ج-ب-أ (sujet lu de droite à gauche), annoncé par le `<title>`. Aucune étiquette de nom ; titres neutres (« خليّة جنسيّة خارج جدار مفتوح ») ; aucun débordement ; `check-figures` sans constat. Le « 3 » de Space Grotesk a un sommet plat (même rendu en `ltr` et `rtl`) : pas un miroir.

**Vérifications.**
- Fidélité : les cinq items officiels sont présents (1 noms → Q2 ; 2 ordre → Q3 ; 3 événement → Q1 ; 4 phases → Q4 ; 5 devenir → Q5). Q3, Q4, Q5 posés par NOMS : autonomes, sans fuite des couples de Q2 (point 6 de l'auteur confirmé pour Q2 → Q3).
- Plans 2×2 : Q4 (follicule mûr ∈ {folliculaire a, c ; lutéale b, d} ; corps jaune ∈ {lutéale a, d ; folliculaire b, c}) et Q5 (ovocyte ∈ {rejeté avec les règles a, d ; dégénère b, c} ; corps jaune ∈ {persiste a, b ; régresse c, d}) : chaque valeur deux fois, options à deux erreurs (Q4 b, Q5 a) muettes, aucun vote ne reconstruit la clé. Clé de Q5 (60 car.) non la plus longue (b : 74).
- Distracteurs faux dans le fait : « تُطرح مع دم الحيض » contredit le cours 10 (l'ovocyte « اضمحلّت » en ~24 h) ; « يبقى ويواصل إفراز الهرمونات » est le cas de la grossesse (cours 11). Vocabulaire enseigné : « الجريب المنفجر » (cours 11), « الجريب النّاضج », « الجسم الأصفر », « البويضة ».
- Étage d2 practice 75/15, rampe 1,2,2,2,2 : honnêtes (Q2 est facile — « المنفجر » et « الأصفر » se lisent sur le dessin — mais pas au point de mentir sur la rampe). Titre conforme ; displayOrder 8.
- Étiquettes : aucune posée ; aucune étiquette existante n'est exacte pour Q1, Q4, Q5 (muettes justes).
- Doublons : aucune question publiée des ch.10-11 ne porte de figure ni de type interactif ; aucune ne demande le devenir conjoint ovocyte/corps jaune (11/quiz Q9 traite le cas avec fécondation).

**Défauts.**
- [mineur] **Q1 explication : fuite en avant vers Q2 (et Q3).** « أمّا نموّ الجريب فيكون جداره مغلقًا » donne le critère paroi fermée / paroi ouverte qui apparie 3 et 2 dans Q2, émise juste après (d1 → d2) ; « أو قراءة الجدار الذي بقي على أنّه جسم أصفر » nomme la paroi restante. Impact faible (les noms se lisent presque sur la figure), mais évitable. Remplacer l'explication par : « يبيّن الرّسم أ خروج الخليّة الجنسيّة الأنثويّة من المبيض عبر جدار انفتح: هذه هي الإباضة، وهي إحدى ظاهرتي الدّورة الجنسيّة. أمّا نموّ الجريب وتكوّن الجسم الأصفر فلا تخرج خلالهما أيّ خليّة من المبيض، والإلقاح لا يحدث في المبيض بل في قناة البيض. الخطأ الشائع: عدّ الخليّة الخارجة من المبيض علامة على إلقاح، مع أنّ الإلقاح يتمّ بعد ذلك في قناة البيض. » (Vérifié : ne décrit plus l'aspect du follicule mûr, ne place plus le corps jaune dans le temps — rien pour Q2 ni Q3 ; les deux réfutations sont vraies.)
- Observation : l'explication de Q4 (« يتحوّل … ما تبقّى من الجريب المنفجر إلى جسم أصفر ») redonne l'ordre de Q3 ; Q3 précède Q4 dans l'émission (même difficulté, ordre du fichier) : sans conséquence sur la route quête, inhérent au savoir commun.

**Verdict 11/08 : réserve mineure** (0 clé fausse).

## 7. `11-ad-dawra-al-jinsiya/exercices/09-examen-2021-ex3-…-cycle-et-ovulation.json` (2021 ex.3)

Transcription et PDF (C05 p. 2-3 : Document 3 et calendrier à 300 dpi) relus ; cinq figures rendues dans Chromium ; calculs de dates refaits par script (`datetime`).

| Q | ma réponse (aveugle) | clé du fichier | verdict | motif |
| --- | --- | --- | --- | --- |
| Q1 (d1, matching 2 paires) titres | (أ) → ovocyte, (ب) → spermatozoïde | l1-r2, l2-r1 | OK | — |
| Q2 (d1, matching) légendes 4-6 | 4 → acrosome, 5 → mitochondries, 6 → flagelle | l1-r2, l2-r3, l3-r1 | OK | conforme au scan |
| Q3 (d2, matching) légendes 1-3 | 1 → chromosomes, 2 → cytoplasme, 3 → globule polaire | l1-r2, l2-r3, l3-r1 | réserve | clé juste ; terme non officiel « الجسم القطبيّ » |
| Q4 (d2, mcq 2×2) lieu × durée de vie | ovaire / ~24 h ; tubes séminifères / 3 à 4 j | a | OK | cours 10 |
| Q5 (d2) durée du cycle | 26 jours | c | réserve | clé juste ; mécanisme du distracteur 25 mal nommé (et cours 11 fautif, voir § Hors périmètre) |
| Q6 (d3) dates d'ovulation | 17-18 juillet et 12-13 août | b | OK | règle du cours et calcul vérifiés |

Clés fausses : 0/6.

**Calendrier (point de l'auteur).** Scan relu à 300 dpi : règles du 6 au 10 juillet (6 = dimanche, 7-10 = lundi-jeudi), du 1ᵉʳ au 5 août (vendredi-mardi) et du 27 au 31 août ; 1ᵉʳ juillet = mardi, 1ᵉʳ août = vendredi. Le SVG redessiné colore exactement ces 15 cases ; 1ᵉʳ juillet en 2ᵉ colonne, 6 juillet en 7ᵉ, 1ᵉʳ août en 5ᵉ (semaines lundi → dimanche) : données identiques. La lecture n'est pas perdue : chaque case porte sa date, les mois sont situés par l'énoncé (« جويلية في أعلى … ثمّ أوت في أسفلها », 31 jours donnés en Q5 et visibles en Q6), aucun jour de la semaine n'est utile aux questions. Q5 et Q6 portent la même figure, qui ne marque aucune date d'ovulation.

**Calculs (script).** Cycles : 1ᵉʳ août − 6 juillet = 26 j ; 27 août − 1ᵉʳ août = 26 j. Ovulation : règle du cours L − 14 = j 12 → 17 juillet / 12 août ; « 14 jours avant les règles suivantes » → 18 juillet / 13 août ; milieu du cycle (j 13) → 18 juillet / 13 août ; mythe « jour 14 » → 19 juillet / 14 août (aucune option). Distracteurs : Q5 a 22 = 10 juillet → 1ᵉʳ août (fin des règles, exact pour l'étiquette) ; d 30 = 6 juillet → 5 août (ou 1ᵉʳ → 31 août : autre période) ; b 25 = 31 − 6 sans compter le 6 ; Q6 a = jour de fin des règles et lendemain, c = fin des règles + 13/14 j, d = deux jours avant les règles suivantes ; dans les quatre options de Q6 les deux fourchettes sont espacées de 26 j (aucune ne s'élimine par incohérence).

**Point (1) de l'auteur (fourchettes de Q6).** Acceptable et même nécessaire : le cours dit « يوم 14 قبل النّهاية » (L − 14 → 17) et « تُحسب رجوعًا من الحيض الموالي » (→ 18) ; une date unique rendrait l'autre défendable. Aucune option adjacente. Limite à savoir : avec un cycle de 26 j, le milieu du cycle (18 juillet) tombe dans la clé et le mythe « jour 14 » (19 juillet) n'a pas d'option, si bien que l'item ne peut pas distinguer la règle du cours de l'erreur « la plus dangereuse du chapitre » — c'est inhérent aux données officielles, et l'explication le dit honnêtement (« وهذا يقارب الصّحيح هنا … لكنّه لا يصحّ عمومًا »). Ne PAS ajouter `ovulation-au-milieu-du-cycle` : décision de l'auteur juste. Ne pas ajouter d'option « 19-20 juillet » : adjacente à la clé, elle ouvrirait un débat à un jour près.

**Point (2) de l'auteur (Q3).** Confirmé sur le scan : « -1 » vise l'extrémité basse de la barre sombre oblique (chromosomes sur le fuseau), « -2 » la zone claire sous la barre (cytoplasme), « -3 » le petit corps ovale noir entre la cellule et l'enveloppe renflée (globule polaire). Le SVG reproduit ces positions : pointe de 1 à ~4 unités de l'extrémité basse de la barre (77 ; 81)-(95 ; 99), pointe de 2 dans le cytoplasme (24,7 du centre, rayon 32,5), pointe de 3 dans l'ovale noir, centré à 33,1 du centre, donc hors du cytoplasme et sous l'enveloppe — conforme à la définition donnée dans l'énoncé.

**Figures Q1-Q2.** Spermatozoïde et ovocyte fidèles au scan (tête noire, calotte jaune, point, col, anneaux empilés, queue en U terminée par un filament ; ovocyte à couronne, enveloppe jaune, membrane mauve). Flèches de Q2 : 5 à 2 unités des anneaux, 6 à 1,8 unité de la queue, 4 à la jonction calotte/contour de la tête. Aucun nom dessiné, aucun débordement, `check-figures` sans constat.

**Vérifications.**
- Fidélité : 1-أ → Q2 + Q3 ; 1-ب → Q1 ; 1-ج → Q4 ; 2-أ → Q5 ; 2-ب → Q6. Rien d'écarté. Seule perte, mineure : le lieu de formation de l'ovocyte (« المبيض ») est commun aux quatre options de Q4, il n'est donc plus testé.
- Q4 : plan 2×2 (durées justes a, c / inversées b, d ; tubes séminifères a, b / épididyme c, d), chaque valeur deux fois, l'option à deux erreurs (d) muette ; étiquettes b `durees-de-vie-inversees` et c `lieux-des-gametes-confondus` exactes. Clé à égalité de longueur avec b, pas strictement la plus longue.
- Q5 : étiquettes a `compte-depuis-la-fin-des-regles` exacte ; d `valeur-d-une-autre-grandeur` (30 j) acceptable — deux chemins, mais tous deux « une autre période » (6 juillet → 5 août ; 1ᵉʳ → 31 août), ce que nomme le libellé. b (25) muette : pas d'étiquette « oubli du premier jour » au registre.
- Q6 : c `compte-depuis-la-fin-des-regles` acceptable (le décompte part de la fin des règles ; l'explication le dit) ; a et d muettes.
- Programme : notions des ch.10 et 11 ; « الجسم القطبيّ » défini dans l'énoncé de la seule question qui l'emploie (Q3) ; la lecture d'un calendrier est enseignée (cours 11 « كيف يُحسب طول دورة من روزنامة »).
- Étage d3 boss : défendable mais à la borne basse — une seule d3 (Q6), deux d1 quasi immédiates (Q1, Q2). Rampe 1,1,2,2,2,3. Titre conforme (« الخليّتان الجنسيّتان وقراءة روزنامة الدّورة الجنسيّة » ne livre rien) ; displayOrder 9.
- Fuites : Q2 et Q3 nomment la cellule (« لحيوان منويّ », « لبويضة ») et donnent donc la clé de Q1 si elles sont tirées avant elle au donjon — inhérent et sans portée (Q1 est une reconnaissance immédiate). L'explication de Q6 redonne 26 j (clé de Q5), émise après Q5.
- Doublons : aucune question publiée de lecture de calendrier ni de légendes de gamètes (ch.10-11 n'ont ni figure ni type interactif publiés).

**Défauts.**
- [mineur] **Q3 : « الجسم القطبيّ » n'est pas le terme des sujets officiels de 9ᵉ**, qui écrivent « الكريّة القطبيّة » (2025 ex.3 : « الكريّة القطبيّة الأولى / الثانية » ; 2024 ex.4 : « الكريتان القطبيّتان ») ; aucun contenu du corpus n'emploie « الجسم القطبيّ ». Remplacer partout dans Q3 (énoncé, option r1, explication) : définition « الكريّة القطبيّة خليّة صغيرة جدًّا تنفصل عن البويضة أثناء نضجها وتبقى لاصقة بها خارج سيتوبلازمها. » ; r1 « الكريّة القطبيّة » ; explication « العنصر 3 هو الكريّة القطبيّة: الجسم البيضويّ الأسود الصّغير … ».
- [mineur] **Q3 explication : « أو الخلط بين الجسم القطبيّ وأكروزوم الحيوان المنويّ لأنّه جسم صغير أيضًا »** nomme l'acrosome comme « petit corps » du spermatozoïde : indice pour le couple 4 → acrosome de Q2 si Q3 est tirée avant Q2 au donjon, et confusion peu crédible. Supprimer ce membre de phrase (garder « الخطأ الشائع: تسمية المنطقة الفاتحة نواة »).
- [mineur] **Q5 explication : mécanisme du distracteur 25 mal nommé.** « أو التّوقّف عند آخر الشّهر فيُكتب 25 يومًا » : s'arrêter à la fin de juillet en comptant le 6 donne 26, pas 25. Le 25 vient de « 31 − 6 = 25 » sans compter le premier jour. Remplacer par : « أو حساب 31 − 6 = 25 دون عدّ يوم 6 نفسه، وهو اليوم الأوّل من الدّورة، فيُختار 25 يومًا ». (Cette erreur est précisément celle de la vérification du cours 11 — voir § Hors périmètre.) Et « فيُكتب » → « فيُختار » dans les trois cas.
- Observation : l'acrosome (calotte jaune) déborde au-dessus du contour de la tête dans Q1 et Q2, alors qu'il est sous la membrane sur le scan et que le cours 10 le range dans la tête ; lisible, sans effet sur la clé — à corriger seulement si la figure est retouchée.

**Verdict 11/09 : réserve mineure** (0 clé fausse).

---

## 8. Étiquettes

### 8.1 Les 22 placements de l'auteur (libellés lus sur `origin/main`)

| mission · question · option | étiquette | jugement |
| --- | --- | --- |
| 09/07 Q2 a, b, c | `bio.nerv.nerfs-craniens-et-rachidiens-confondus` | exactes (traits crâniens prêtés aux rachidiens : encéphale, 12 paires, tête/visage) |
| 09/07 Q3 c | `bio.dig.absorption-dans-la-digestion` | exacte |
| 09/07 Q3 d | `bio.dig.fragmentation-prise-pour-digestion` | acceptable (fragmentation mécanique prise pour l'action enzymatique) |
| 09/07 Q4 a, b | `bio.excr.etape-du-nephron-confondue` | acceptables (ajout de l'ammoniac placé à l'étape de filtration) |
| 09/07 Q4 d (canal collecteur) | `bio.excr.etape-du-nephron-confondue` | **inexacte → à retirer** : l'élève sait que c'est une sécrétion, il se trompe de structure (lieu de mesure de l'urine finale) ; aucune étiquette existante ne le nomme |
| 09/08 Q3 a, c | `bio.excr.etape-du-nephron-confondue` | exactes |
| 09/08 Q4 b | `bio.excr.filtration-selective` | exacte |
| 10/07 Q2 a | `bio.circ.artere-sang-oxygene` | exacte |
| 11/07 Q3 a, b, c | `bio.dig.specificite-enzyme-ignoree` | exactes (porte R2) |
| 11/07 Q4 a | `bio.cycle.phases-uterines-confondues` | acceptable (« Tu décales les phases utérines » ; la correction dit ce qui se passe après l'ovulation) |
| 11/07 Q4 c | `bio.cycle.phases-uterines-confondues` | exacte |
| 11/09 Q4 b | `bio.repro.durees-de-vie-inversees` | exacte |
| 11/09 Q4 c | `bio.repro.lieux-des-gametes-confondus` | exacte |
| 11/09 Q5 a | `bio.cycle.compte-depuis-la-fin-des-regles` | exacte (22 = 10 juillet → 1ᵉʳ août) |
| 11/09 Q5 d | `bio.lecture.valeur-d-une-autre-grandeur` | acceptable (30 = 6 juillet → 5 août ou 1ᵉʳ → 31 août : « autre période ») |
| 11/09 Q6 c | `bio.cycle.compte-depuis-la-fin-des-regles` | acceptable (décompte parti de la fin des règles) |

`ovulation-au-milieu-du-cycle` non posée en 11/09 Q6 : **juste** (le milieu du cycle, 18 juillet, tombe dans la clé). Aucune option de `multi`, `matching` ou `ordering` n'est étiquetée. Aucune option à deux erreurs n'est étiquetée.

**Option muette qui mérite une étiquette existante** : 10/07 Q3 c (« قلب أيمن ← أوردة رئويّة ← رئتان ← شريان رئويّ ← قلب أيسر ») → `bio.circ.artere-sang-oxygene` (porte R1). Les autres muettes sont justes (erreur sans entrée au registre, ou deux chemins vers la même option : 10/07 Q1 a, Q3 d, Q4 d ; 11/09 Q5 b).

### 8.2 Familles que l'auteur dit manquer

Comptage fait sur les 969 questions SVT de `origin/main` + la tranche (recherche normalisée sans voyelles brèves) ; aucun des deux identifiants n'existe (ni sur `origin/main`, ni dans l'arbre de travail).

**A. `bio.nerv.substances-grise-blanche-confondues` — à créer (3 questions distinctes, seuil atteint).**
Placements vérifiés un à un, tous muets aujourd'hui : `01-wadhifat-al-ittisal/quiz.json` Q3 a (« من أجسام خلويّة عصبيّة وتغصّناتها » pour la substance blanche) ; `01-wadhifat-al-ittisal/exercices/01-tamrin.json` Q4 a (« نقل السّيالة العصبيّة على مسافات طويلة » comme rôle de la grise) ; 11/07 Q2 b, c, d (dendrites, corps cellulaires, « خلايا عصبيّة رابطة » dans la blanche). Aucun autre placement exact (01/03-boss Q4, 01/06-defi-concours Q6, 01/quiz Q7 : erreurs voisines non exactes ; 01/02-tamrin Q3 et 01/quiz Q4 relèvent de `substance-grise-toujours-dehors`). Le libellé proposé nomme exactement les trois erreurs. Retouche conseillée pour coller au vocabulaire du cours (« السّيالة العصبيّة », non « الرّسالة ») :
- fr : « Tu mélanges ce que contiennent et font les deux substances : la grise renferme les corps cellulaires et les dendrites (elle traite le message nerveux), la blanche les fibres à gaine graisseuse (elle le transporte). »
- en : « You mix up what the two matters hold and do: grey matter holds the cell bodies and dendrites (it processes the nerve message), white matter holds the fibres with fatty sheaths (it carries it). »
- ar : « تخلط بين محتوى المادّتين ودورهما: السّنجابيّة تحوي الأجسام الخلويّة والتّغصّنات وتعالج السّيالة العصبيّة، والبيضاء تحوي الألياف ذات الأغمدة الدّهنيّة وتنقلها. »

**B. `bio.circ.capillaire-comme-l-artere` — à créer (3 questions distinctes, seuil atteint).**
Placements vérifiés, tous muets aujourd'hui : `07-ad-dawaran/exercices/03-boss.json` Q4 a (« قلّة عددها وسمك جدارها وسرعة الجريان ») et c (« ضغطها المرتفع وسمكها ») ; `07-ad-dawaran/quiz.json` Q7 a (« سمك الجدار وارتفاع الضّغط وسرعة الجريان ») ; 11/07 Q1 a, b, d. Le libellé proposé est exact pour 07/quiz Q7 a, 07/03-boss Q4 c et 11/07 Q1 ; pour 07/03-boss Q4 a il ne corrige pas « قلّة عددها » : ajouter le nombre à la correction (cours 07 : « أوعية كثيرة جدًّا ورقيقة جدًّا ») :
- fr : « Tu donnes au capillaire les traits de l'artère (paroi épaisse, pression élevée, écoulement rapide) : les capillaires sont très nombreux, leur paroi est très mince, la pression y est basse et le sang y coule lentement, ce qui favorise les échanges. »
- en : « You give the capillary the artery's traits (thick wall, high pressure, fast flow): capillaries are very numerous, their wall is very thin, the pressure is low and blood flows slowly, which favours exchanges. »
- ar : « تنسب إلى الشّعيرة الدّمويّة صفات الشّريان (جدار سميك وضغط مرتفع وجريان سريع): الشّعيرات كثيرة جدًّا وجدارها رقيق جدًّا، والضّغط فيها منخفض والدّم يسري فيها ببطء، فيتيسّر التّبادل. »
(07/quiz Q7 b « قلّة عددها واتّساع قطرها » reste muette : le diamètre n'est pas nommé. L03 08/07 Q3 b-d prêtent « paroi épaisse / écoulement rapide » à la villosité et à l'alvéole, pas au capillaire : hors famille.)

## 9. Doublons et fuites entre missions

- **Dans la tranche (néphron 09/07-09/08-09/09 ; cycle 11/07-11/08-11/09)** : aucun gabarit répété (`content:tranche` : 0 paire proche, 0 candidat gabarit). Le même fait revient sous trois formes officielles différentes : « l'ammoniac est sécrété par le tube urinaire » (09/07 Q4 ; 09/08 Q2-Q3 ; 09/09 Q3 option e et Q4) — l'option vraie e de 09/09 Q3 énonce mot pour mot la clé de 09/07 Q4 ; et « l'ovocyte vit ~24 h » (11/08 Q5, 11/09 Q4). Réserve d'orchestration seulement (items officiels distincts, missions d'étages différents).
- **Avec les missions publiées et les lots L01-L03** : 10/07 Q4 contre 10/04-defi Q4 (le recoupement le plus fort, voir § 4) ; 09/07 Q3 contre L03 08/09 Q2 et 05/02-tamrin Q1 (voir § 1) ; 10/07 Q3 contre 07/03-boss Q1 ; 09/08 Q3 contre 09/02-tamrin Q3-Q4 ; 09/09 Q3 contre 09/02-tamrin Q1. Aucun n'est quasi identique au sens de la règle du lot.
- **Fuites relevées** : 11/08 Q1 → Q2 (explication, § 6) ; 11/09 Q3 → Q2 (explication, § 7) ; 09/08 Q3-Q4 sans figure (§ 2). Aucune décimale de vérification, aucune coche ✓ après un distracteur, aucun titre qui livre une clé.

## 10. Rendu arabe

- Toutes les chaînes à chiffres ou lettres latines du lot passées dans `splitMathRuns` / `isolateLtrRuns` / `isDisplayEquation` de `origin/main` (moteur `618147d7`, extrait sans toucher à l'arbre local, qui est en retard) puis rendues dans Chromium (polices de l'app) en page `rtl` et en page `ltr`. Seuls « (X) » et « (Y) » sont isolés ; les calculs purement numériques des explications (« 31 − 6 + 1 = 26 », « 26 − 14 = 12 ») restent natifs et se lisent de droite à gauche avec la phrase, comme le veut `bidi.ts`. Aucune ligne de formule seule, aucune virgule arabe entre valeurs nues, aucun chiffre arabo-indien, aucun espace simple entre groupes de chiffres, aucune occurrence de « على الشكل التالي ».
- Dans le lecteur de quête (`PageShell dir="rtl"` pour une matière arabe) et dans la question du donjon (`dir="rtl"` si l'énoncé contient de l'arabe), tout s'affiche dans l'ordre du texte source, y compris « X: البروتيدات ؛ Y: البولة », les flèches « ← » de 10/07 Q3 et les fourchettes de dates de 11/09 Q6.
- [mineur, robustesse] Les champs qui COMMENCENT par une lettre latine (09/08 Q2 et Q3 : options « X: … ؛ Y: … » ; 09/08 Q3 : explication « X: تركيزه … ») ne reçoivent pas `dir="rtl"` (`isRtlText` lit la première lettre) : sur les écrans sans conteneur `rtl` — bloc « question fatale » de fin de donjon, résultats d'examen — ils suivent la langue de l'interface et, en interface française, s'affichent « X: ؛ البروتيدات Y: البولة » et « X: » rejeté en fin de ligne (rendu vérifié). Correctif de contenu sûr : commencer par un mot arabe — explication de 09/08 Q3 : « العنصر X: تركيزه في المنطقة «أ» … » (rendu vérifié) ; options : « العنصر X: … ؛ العنصر Y: … » si l'on veut les protéger aussi (même ajout dans les quatre options : les longueurs relatives ne changent pas). Cause racine côté moteur (à router) : ces écrans devraient utiliser `hasArabicLetters`.
- Figures : `SvgFigure` rend désormais la figure en `dir="ltr"` (`origin/main`) ; les ancres `start`/`end` des étiquettes sont donc justes dans toutes les interfaces.

## 11. Figures (onze, toutes comparées au scan et rendues)

| figure | verdict |
| --- | --- |
| 09/08 Q1 = Q2 (courbes X/Y) | vraie (graduations, valeurs 1 / 0 / 0,5, zones, croisement) ; ne donne aucune clé ; glomérule et canal collecteur non étiquetés (ordre donné par l'énoncé) |
| 09/09 Q1 (néphron nu) | vraie, neutre |
| 09/09 Q2 (néphron numéroté) | vraie ; quatre repères aux positions du scan |
| 11/08 Q1 (dessin أ) | vraie, neutre |
| 11/08 Q2 (trois structures numérotées) | vraie ; repères 1-4 aux positions du scan |
| 11/09 Q1 (deux gamètes) | vraie ; acrosome à cheval sur le contour de la tête (observation) |
| 11/09 Q2 (spermatozoïde numéroté) | vraie ; même observation |
| 11/09 Q3 (ovocyte numéroté) | vraie ; repères 1-3 aux positions du scan, globule polaire hors du cytoplasme |
| 11/09 Q5 = Q6 (calendrier) | vraie ; 15 cases de règles identiques au scan |

Aucun élément ni attribut interdit (`check-figures` : aucun constat sur les sept fichiers), arabe hors `<title>` limité à des glyphes d'une lettre (أ, ب, ج), rien ne déborde du `viewBox` (mesure `getBBox` en `ltr` et `rtl`), aucune figure à l'échelle de la solution.

## 12. Hors périmètre, à router (constaté pendant l'audit)

- **[critique pour le cours 11] Vérification fausse dans `11-ad-dawra-al-jinsiya/cours.md` (ligne 49 sur `origin/main`)** : « من يوم 5 إلى نهاية الشّهر: 30 − 5 = 25 يومًا، ثمّ يومان (1 و2) من الشّهر الموالي ← **27 يومًا** ». Du 5 au 30 inclus il y a 26 jours ; la durée est 28 (= (30 + 3) − 5, la définition même que donne le cours). Cette méthode erronée, appliquée à 11/09 Q5, donne (31 − 6) + 0 = 25 = le distracteur b : un élève qui suit le cours se trompe en toute bonne foi. La clé 26 de la mission est juste ; c'est le cours qui doit être corrigé : « من يوم 5 إلى نهاية الشّهر: 30 − 5 + 1 = 26 يومًا، ثمّ يومان (1 و2) من الشّهر الموالي ← **28 يومًا**. » (vérifié par script : 28).
- **Convention à un jour près sur la date d'ovulation, non harmonisée** : le cours dit « يوم 14 قبل النّهاية » (L − 14) ; le libellé de `bio.cycle.ovulation-au-milieu-du-cycle` dit « 14 jours avant les règles suivantes, soit la durée du cycle moins 14 » (par le calendrier, 14 jours avant le premier jour des règles suivantes = jour L − 13) ; `13-tandhim-al-wiladat/quiz.json` Q3 étiquette « le jour 13 » d'un cycle de 26 j comme l'erreur du milieu du cycle, tandis que la clé de 11/09 Q6 contient ce jour (18 juillet). Proposition de libellé : fr « Tu places toujours l'ovulation au milieu du cycle : elle a lieu 14 jours avant la fin du cycle, soit le jour « durée du cycle moins 14 ». » ; en « You always put ovulation mid-cycle: it happens 14 days before the end of the cycle, i.e. on day cycle length minus 14. » ; ar « تضع الإباضة دائمًا في منتصف الدّورة: تقع قبل نهاية الدّورة بـ14 يومًا، أي في اليوم «طول الدّورة ناقص 14». »
- **Moteur** : `FIGURE_REFERENCE` (`scripts/content/qa-checks.ts`, testé sur le texte brut) ignore « الوثيقة » ; y ajouter « الوثيقة » précédée d'un verbe de présentation (« تبيّن / تمثّل / تبرز / تقيس الوثيقة », avec ou sans chadda) — l'erreur n'est levée que si le champ n'a pas de SVG — aurait attrapé 09/08 Q3-Q4. Et les écrans « question fatale » du donjon et résultats d'examen devraient décider la direction avec `hasArabicLetters` (§ 10).

## 13. Chiffre final

- Questions auditées : **31** (7 fichiers), toutes re-résolues à l'aveugle avant lecture des clés.
- Clés fausses : **0**.
- Défauts critiques : **0** dans la tranche (1 critique hors périmètre : la vérification du cours 11).
- Défauts majeurs : **2** (3 questions) — 09/08 Q3 et Q4 (énoncé renvoyant à une figure absente) ; 11/07 Q3 (lieu de la clé trahi par sa fréquence).
- Défauts mineurs : **16** — 09/07 : étiquette Q4 d, explication Q1 ; 09/08 : « على مسار البول » (Q1, `<title>`), inférence de l'explication Q1, « إفراز … كالبولة » (explication Q4) ; 09/09 : plan 2×2 incohérent Q1, « على مسار البول » Q4 ; 10/07 : étiquette à poser Q3 c, explications Q3-Q4 (« فيُكتب », citations) ; 11/07 : « خلايا عصبيّة رابطة » non enseigné (explication Q2), « فيُكتب » (explication Q1) ; 11/08 : fuite de l'explication Q1 vers Q2 ; 11/09 : terme « الكريّة القطبيّة » (Q3), acrosome dans l'explication Q3, mécanisme du 25 (explication Q5) ; robustesse « X: » de 09/08 (Q2, Q3). Ils touchent 12 questions hors des 3 majeures : 09/07 Q1, Q4 ; 09/08 Q1 ; 09/09 Q1, Q4 ; 10/07 Q3, Q4 ; 11/07 Q1, Q2 ; 11/08 Q1 ; 11/09 Q3, Q5.
- Questions à reprendre : **15** (3 pour majeur, 12 pour mineur) ; étiquettes : 1 à retirer (09/07 Q4 d), 1 à poser (10/07 Q3 c), 2 familles nouvelles à créer (A, B : 5 + 6 placements).
- Verdicts : 09/07 réserve mineure · 09/08 **défaut majeur** · 09/09 réserve mineure · 10/07 réserve mineure · 11/07 **défaut majeur** · 11/08 réserve mineure · 11/09 réserve mineure.
