# Audit indépendant — lot L07 (maths 9ᵉ, ch.07, missions 18 à 24, examens techniques 2012, 2013, 2024, 2015, 2016, 2017, 2018) — auditeur a1ba0a6f685c0d237

**Verdict : 0 clé fausse sur 54 questions (re-résolues à l'aveugle), 0 critique, 6 majeurs (forme ou autonomie d'un énoncé).** Débordement des listes d'intervalles : défaut MOTEUR réel (traité à part). Données fidèles aux 7 transcriptions ; figures toutes vraies ; gates : check ✓, qa 0/0, tranche : 0 clé la plus longue, aucune paire proche touchant 18–24, figures ✓.

Étages : 18, 19, 20 d2 practice d'accord ; 21 à 24 d3 boss défendable (l'auditeur juge que les missions publiées 11, 14, 15 — même bloc moyenne/ECC/polygone/médiane en d2 — devraient être d3 : à traiter dans un lot séparé). Rampes non décroissantes.

## Majeurs (correctifs vérifiés par l'auditeur : clé jamais la plus longue, pas de prémisse niée, pas de fuite, bidi OK)

**M1 — 22 Q6, la clé se repère comme intrus** (34, 68, 340 sont des multiples de 34 ; 458 seul ne l'est pas).
- Remplacer l'option « 34 » par « 424 » (390 + 34 : on n'a ajouté que la hausse d'un mètre cube), muette. Ordre : a « 68 » (reponse-a-l-autre-inconnue), b « 340 » (idem), c « 424 » (muette), d « 458 » (clé, id inchangé).
- Dernière ligne de l'explication : « الخطأ الشائع: الاكتفاء بالزيادة دون إضافة ترتيبة النقطة ذات الفاصلة 25، سواء كانت الزيادة من 25 إلى 27 وهي 68، أو على القطعة كلّها وهي 340؛ أو إضافة زيادة متر مكعّب واحد فقط، 390 + 34 = 424، مع أنّ 27 تبعد عن 25 بمترين مكعّبين. »

**M2 — 19 Q6, le vote majoritaire reconstruit la clé** ([3 ; 4[ et [4 ; 5[ dans 3 options sur 4).
- Option b « [2 ; 3[ ، [3 ; 4[ » → « [0 ; 1[ ، [1 ; 2[ ، [2 ; 3[ » (le complémentaire : les non-invités), étiquette math.alg.reponse-a-l-autre-inconnue.
- Explication : « ؛ أو الاكتفاء بالفئتين المحيطتين بالعدد 3 وإهمال آخر فئة في الجدول. » → « ؛ أو اختيار الفئات الثلاث التي تقلّ فيها المدّة عن 3 ساعات، وهي فئات التلاميذ غير المدعوّين. »

**M3 — 23 Q6, un marqueur de forme désigne la clé** (seule la clé se justifie par « لأنّها تجمع تكرارات الفئات كلّها »).
- [a] → « أعلى ترتيبة فيه هي 250، لأنّ 250 هو عدد الفوانيس كلّها » ; étiqueter [b] « 100 » et [c] « 8 » avec math.stat.effectif-cumule-non-cumule (un effectif donné au lieu du cumulé).

**M4 — 22 Q5, l'option [d] « 5 » est réfutée par l'énoncé** (le polygone commence en (5 ; 0)).
- Options : a « 45 » (clé), b « 35 », c « 25 », d « 15 », toutes muettes. L'explication cite déjà 25 parmi les points justes.

**M5 — 22 Q7, l'énoncé ne se lit pas seul** (« نصف عدد العائلات » sans le total, « بنفس الطريقة » renvoie à Q6 ; le donjon tire chaque question isolément au hasard).
- Nouvel énoncé : « الموسّط (الوسيط) هو فاصلة النقطة من مضلّع التكرارات المجمّعة الصاعدة التي ترتيبتها نصف عدد العائلات.\nقرأنا على مضلّع استهلاك ألف عائلة للماء أنّ حوالي 458 عائلة يقلّ استهلاكها عن 27 مترًا مكعّبًا، وأنّ حوالي 560 عائلة يقلّ استهلاكها عن 30 مترًا مكعّبًا.\nبين أيّ عددين يقع الموسّط ؟ » ; reste en d3 (son énoncé redonne la clé de Q6).

**M6 — 24 Q9, technique ni enseignée ni donnée (R-3)** (la médiane graphique n'est définie que dans l'énoncé de Q8).
- Nouvel énoncé : « على القطعة الواصلة بين (2 ; 120) و(4 ; 330) من مضلّع التكرارات المجمّعة الصاعدة يزداد عدد التلاميذ بانتظام، ونصف عدد تلاميذ المدرسة هو 220 تلميذًا.\nالموسّط هو فاصلة النقطة من هذه القطعة التي ترتيبتها 220. ما قيمته بالساعة، مقرّبةً إلى 0,01 ؟ »

## Mineurs
- m1 (18 Q5/Q6) : optionnel (placer Q6 avant Q5) — NON appliqué (le donjon tire au hasard).
- m2 : 22 Q7 est un d2 réel maintenu en d3 (son énoncé donne la clé de Q6) : accepté.
- m3 : facultatif — 23 Q4 explication : supprimer « ، والخانة الأخيرة تساوي عدد الفوانيس كلّها » (livre la clé de Q6) ; 24 Q7 et 23 Q3 : acceptés.
- m4 : 20 Q7 [a] « 915 » : `operation-inverse-appliquee` inexacte → math.alg.reponse-a-l-autre-inconnue ; 21 Q7 [c] « (7 ; 20) » → math.stat.effectif-cumule-non-cumule ([a] « (6 ; 20) » deux erreurs : muette) ; compétences : 20 Q5 → math.mes.durees (si existe), 20 Q7 → math.prop.situations au lieu de math.prop.pourcentages.
- m5 : 20 Q5 coquille « في يومه الافتتاح » → « في يومه الافتتاحي » ; [c] « 50 شهرًا » s'élimine seul (priorité faible).
- m6, m7 : cosmétique / répétitions acceptées.
- m8 : 24 Q8 vote par composantes (fraction dans 3 options sur 4, préfixe « 2 + » dans 2 sur 4). Correctif facultatif : [c] « 2 + 220 × 2 ÷ 330 » → « 4 + (220 − 120) × 2 ÷ (330 − 120) » ; explication : « أو قسمة 220 على 330 دون طرح الترتيبة 120 التي تبدأ منها القطعة » → « أو إضافة الزيادة إلى الفاصلة 4 التي تنتهي عندها القطعة بدل الفاصلة 2 التي تبدأ منها ».
- m9 : 21 Q1 la clé reprend les mots de la définition donnée (accepté en d1).
- m10 : 23 Q1 [a] explication : « ؛ أو الفئة [100 ; 200[ وتكرارها 45 فقط » → « ؛ أو الفئة [100 ; 200[ بخلط أكبر تكرار، وهو 100، بالقيمة 100 التي تبدأ بها هذه الفئة ».

## Débordement des listes d'intervalles (défaut MOTEUR, hors tranche)
Mesuré dans Chromium (polices de l'app, énoncé 20 px) : les énoncés à listes d'intervalles (19 Q3-Q6, 20 Q2-Q6, 21 Q1-Q5/Q8, 22 Q1-Q5, 23 Q1-Q2/Q7, 24 Q1/Q3-Q6/Q8) dépassent la largeur d'un téléphone (278 px à 360 ; 308 à 390 ; 340) de 14 à 582 px ; 18 n'a pas de crochets (« من 0 إلى 99 ») ; options et explications (14 px) : aucun dépassement. Cause : `splitMathRuns` place les espaces entourant un intervalle DANS le span insécable `.math-run-tight`, UAX #14 interdit de couper avant « ، » et après « [ » : plus aucune coupure possible. Même défaut sur les missions publiées 09, 11, 14, 15. Correctif moteur recommandé : émettre les espaces de bord d'un segment mathématique en prose, hors du span (simulé : tous les débordements de prose disparaissent). Repli contenu : une classe par ligne.

## Constats hors tranche (moteur)
- Titres « (تقني) » : dans le rapport parent (`attempt-detail-dialog`, `daily-activity`), `isolateLtrRuns` isole « 2012 ( » et « ) · » : parenthèses retournées ; hub et bannière boss corrects.
- Donjon : `get_dungeon_questions` tire les questions au hasard (`ORDER BY random()`), pas de tri par difficulté : un énoncé qui redonne la clé d'une question précédente (20 Q5→Q4, 22 Q7→Q6, 24 Q4→Q2…) peut la divulguer si elles sortent dans l'ordre inverse ; inhérent aux missions décomposées ; chaque énoncé doit donc se lire seul.
- DOMPurify retire `unicode-bidi` mais garde `direction` : sans effet ici.

## Étiquettes
73 posées (16 distinctes, toutes sur main, jamais sur une clé) : 72 exactes, 1 inexacte (20 Q7 [a]) ; 89 muettes : 37 volontaires confirmées + 52 couvertes par les 19 propositions ; muettes à étiqueter avec l'existant : 21 Q7 [c], 23 Q6 [b] et [c] → effectif-cumule-non-cumule.
Propositions comptées (options / questions) et décision :
- A classe-finissant-au-seuil-comptee : 19 Q6c, 19 Q7c, 22 Q4b, 24 Q6b (4/4) → CRÉER. Libellé : « Tu comptes la classe qui se termine au seuil : « 3 heures ou plus » commence à 3, la classe qui finit à 3 est tout entière en dessous » / « تحسب الفئة التي تنتهي عند الحدّ: شرط «3 ساعات أو أكثر» يبدأ عند 3، والفئة التي تنتهي عند 3 تقع كلّها دونه ».
- B seuil-large-lu-comme-strict : 19 Q6a (1/1) → non.
- C classes-concernees-incompletes : 18 Q6b, 21 Q6b, 22 Q4d, 23 Q5d, 24 Q6d (5/5) → CRÉER, libellé général : « Tu oublies une partie des classes concernées : toutes les classes situées du bon côté du seuil comptent » / « تنسى بعض الفئات المعنيّة: كلّ الفئات الواقعة في الجهة المطلوبة من الحدّ تُحسب ».
- D+E fusion (cumul décalé d'une classe) : 21 Q5c, 23 Q4b, 21 Q7b (D, 3) + 22 Q3a, 24 Q5a (E, 2) = 5 questions → CRÉER (fusion). Libellé : « Tu décales l'effectif cumulé d'une classe : il compte les valeurs strictement inférieures à sa borne supérieure — ni seulement celles d'avant sa borne inférieure, ni aussi celles de la classe suivante ».
- F (18 Q5d), H (18 Q4d), J (18 Q3b), K (18 Q7a), L (21 Q1), M (19 Q2), S (23 Q3), I (20 Q2 a/b, 21 Q2 a/c ; 2 questions), N (21 Q8b, 22 Q7a ; 2) → non (< 3 questions).
- G (ordonnée du polygone prise pour un effectif : 21 Q7, 23 Q6, 24 Q7) : deux erreurs de sens opposés → ne pas créer ; ÉLARGIR l'existante effectif-cumule-non-cumule aux deux sens : « Tu confonds l'effectif d'une classe (ou d'une valeur) et son effectif cumulé : le cumulé additionne tous les effectifs jusqu'à elle, l'effectif ne compte qu'elle » / « تخلط بين تكرار الفئة (أو القيمة) وتكرارها المجمّع: المجمّع يجمع كلّ التكرارات إلى غايتها، والتكرار يعدّها وحدها ».
- P mediane-egale-centre-ou-borne-de-la-classe : 21 Q9a, 22 Q8d, 23 Q7d, 24 Q9c (4/4) → CRÉER. Libellé : « Tu donnes le centre ou une borne de la classe médiane au lieu de chercher l'abscisse où l'effectif cumulé atteint N/2 ».
- O+Q+R fusion « interpolation-mal-posee » : 21 Q9c, 22 Q8a, 23 Q7a, 24 Q8c, 24 Q9a/R… (5 questions) → CRÉER. Libellé : « Tu poses mal l'interpolation de la médiane (point de départ, rapport ou largeur de classe) : médiane = borne inférieure + (N/2 − cumulé à cette borne) ÷ effectif de la classe × amplitude ».
Bilan registre : 5 créations (A, C, D+E, P, interpolation-mal-posee) + 1 élargissement (effectif-cumule-non-cumule).

## Programme (R-3)
Étendue (18 Q2, 20 Q2, 21 Q2), polygone cumulé, médiane graphique, nature de la série (21 Q1) : donnés dans l'énoncé (sauf 24 Q9 : M6). Classe modale, centre, moyenne par classes, pourcentages : au cours ou repris. ECC par classe : définie dans l'énoncé (18 Q4, 21 Q5, 22 Q3, 23 Q4, 24 Q5). Vocabulaire « فاصلة/ترتيبة » vient de la 8ᵉ et du chapitre 12 (après le 07) : comme les missions publiées 10, 11, 14, 15.

## Chiffre final
54 questions ; 0 clé fausse ; à reprendre : 19 Q6, 22 Q5, 22 Q6, 22 Q7, 23 Q6, 24 Q9 ; retouches mineures : 20 Q5, 20 Q7, 21 Q7 ; facultatives : 23 Q4, 23 Q1, 24 Q8 [c].
