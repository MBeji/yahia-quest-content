# Re-vérification ciblée — lot L08 (maths 9ᵉ, ch. 12-repere-plan, missions 10 à 15) après correctifs

Auditeur indépendant (même rôle que l'audit initial, `audit-L08.md`). Règles suivies :
- résolution à l'aveugle avant la lecture des clés ;
- aucune confiance dans les notes de l'auteur ni dans l'arbitrage ;
- attaque des textes nouveaux, y compris ceux que j'ai fournis.

Je n'ai modifié aucun fichier des dépôts.

Statut : **TERMINÉ**. État relu : les fichiers sur disque, datés 2026-10-01 05:01. Comparaison avec
`l08-backup-audited`. Registre lu sur `origin/main` du corpus (`4f72f94b`). Moteur lu sur `origin/main`
de l'arène (`ce46894c`, qui contient #1142).

## 0. Verdict global

- **Clés : 32/32 justes.** Résolution à l'aveugle d'abord, avec une seconde méthode pour chaque
  question modifiée. Aucune clé fausse, aucun distracteur juste, aucune question à deux réponses.
- **Le lot n'est PAS livrable tel quel.** Il reste 5 correctifs (2 majeurs, 3 mineurs) sur 5
  questions : 11 Q1, 11 Q3, 11 Q6, 12 Q5 et 14 Q2. Le § 2 donne le texte exact de chacun ; tous ont
  passé les contrôles de rendu et de forme.
  - Quatre de ces défauts viennent de **mes propres textes** du premier audit, que l'auteur a
    appliqués fidèlement : R1 (M1), R3 (m2), R4 (M4) et R5 (M7).
  - Le cinquième (R2) est **préexistant** : je l'ai manqué au premier audit.
- **Aucun défaut dans les adaptations de l'auteur.** Sa reformulation de 15 Q1 est même meilleure
  que mon texte : j'avais écrit l'égalité fausse « 1 − 3√3 = −2√3 », il a écrit « (1 − 3)√3 = −2√3 »,
  vraie, qui montre le mécanisme.
- **Une fois R1 à R5 appliqués, le lot est livrable**, à deux conditions sur les étiquettes (§ 4) :
  - aligner `content/misconceptions.json` de l'arbre sur `origin/main` avant le commit, car cinq
    placements n'y sont exacts qu'avec les libellés élargis ;
  - ajouter `math.stat.mediane-lue-sans-ranger` au registre, puis l'étiqueter sur 10 Q4 (c).

## 1. Verdict par question modifiée (et par question où un défaut subsiste)

| question | ce qui a changé | verdict |
| --- | --- | --- |
| 10 Q1 | réécrite (M2) : énoncé, options, explication ; (a) étiquetée | OK |
| 10 Q2 | inchangée | OK (M9 reste un défaut du cours 12, hors tranche) |
| 10 Q3 (ex-Q4) | (c) et (d) étiquetées | OK |
| 10 Q4 (ex-Q5) | explication (m5) | OK ; (c) « 34 » à étiqueter `mediane-lue-sans-ranger` |
| ex-10 Q3 | écartée (M3) | OK : aucune référence restante ; titre et rampe 1, 1, 2, 2 cohérents |
| **11 Q1** | réécrite (M1) | **DÉFAUT MAJEUR R1** (vient de mon texte) |
| 11 Q2 | (a) étiquetée | OK |
| **11 Q3** | inchangée | **DÉFAUT MAJEUR R2** (ligne d'énoncé ; manqué au premier audit) |
| 11 Q4 | (a) étiquetée | OK |
| 11 Q5 | inchangée | OK |
| **11 Q6** | (a) et explication (m2) | **R2** (même ligne d'énoncé) **+ R3 mineur** (option a, vient de mon texte) |
| 12 Q1 | énoncé (m1) ; (c) étiquetée | OK |
| 12 Q2 à Q4 | inchangées | OK |
| **12 Q5** | énoncé (M4) | **DÉFAUT MINEUR R4** (vient de mon texte) |
| 12 Q6 | (b) et explication (M5 + M10) | OK |
| 13, titre | « مراكز فئات الأعمار » | OK |
| 13 Q1 | inchangée | OK |
| 13 Q2 | explication (M11) | OK : le contournement est devenu inutile depuis #1142, mais il est inoffensif, on le garde |
| 13 Q3 | explication ; (a) étiquetée | OK |
| 13 Q4 | explication ; (b) « 12 » ré-étiquetée | OK |
| ex-13 Q5 | écartée (M8) | OK : aucune référence restante ; titre cohérent |
| 14 Q1, Q3, Q4, Q6 | inchangées | OK |
| **14 Q2** | énoncé et explication (M7) | **DÉFAUT MINEUR R5** (vient de mon texte) |
| 14 Q5 | explication (m6) ; (d) étiquetée | OK |
| 15 Q1 | (a) et explication (M6) | OK |
| 15 Q2, Q3 | étiquettes | OK |
| 15 Q4 | explication (M10) ; (d) étiquetée | OK |
| 15 Q5 | (d) étiquetée | OK |
| 15 Q6 | inchangée | OK |

## 2. Défauts et textes de remplacement exacts

Chaque remplacement ci-dessous vise une sous-chaîne qui n'apparaît qu'**une seule fois** dans son
champ (vérifié par script). Aucun ne touche le `<svg>` de 11, qui reste identique octet pour octet.
Chaque texte a passé quatre contrôles :
1. la segmentation `splitMathRuns` / `isDisplayEquation` d'`origin/main` `ce46894c` : aucune paire
   de parenthèses coupée, aucune formule collée à de la prose latine ;
2. l'ordre réel à l'écran dans Chromium (`dir="rtl"`) ;
3. les contrôles de forme (clé pas strictement la plus longue, pas de somme ni de différence, pas de
   vote) ;
4. la vérité de chaque égalité.

### R1 — MAJEUR — 11 Q1 : les options forment des paires renversées ; c'est le sens de lecture qui choisit la réponse (mon texte M1)

Les options sont des couples nus séparés par la virgule arabe :
- (a) « −2 ، 3 » (clé) ;
- (b) « 2 ، −3 » ;
- (c) « −3 ، 2 » ;
- (d) « 3 ، −2 ».

L'option non isolée hérite du sens `rtl` de la page. À l'écran (de gauche à droite), (a) s'affiche
donc « 3 ، −2 » et (d) « −2 ، 3 ». Or l'ensemble est fermé par renversement : (a) renversée donne
(d), (b) renversée donne (c).

Un élève qui lit bien la figure (A = −2, B = 3) mais lit le couple de gauche à droite, réflexe des
formules, cherche « −2 ، 3 » à l'écran. Il coche alors (d), et il est compté faux. La question
mesure le sens de lecture autant que le savoir.

Le corpus publié utilise bien la virgule arabe dans des listes d'options (« 6 ، 16 ، 19 ، 20 »), mais
jamais avec la clé renversée présente parmi les options.

Correctif : étiqueter chaque valeur. Le plan 2×2 (sens × origine) est conservé :
- les quatre options font la même longueur ;
- les valeurs de xA sont toutes distinctes, celles de xB aussi ;
- les signes (−, +) et (+, −) sont à égalité, les grandeurs |xA| = 2 et 3 aussi ;
- les quatre options restent muettes.

À l'écran, (a) se lit « xB = 3 ، xA = −2 » : c'est juste dans les deux sens de lecture.

- options :
  - a `xA = −2 ، xB = 3` (clé) ;
  - b `xA = 2 ، xB = −3` ;
  - c `xA = −3 ، xB = 2` ;
  - d `xA = 3 ، xB = −2`.
- explanation, texte complet :
  `فاصلة نقطة هي عدد التدريجات التي تفصلها عن الأصل O ، بإشارة موجبة في جهة I (فاصلتها 1) وسالبة في الجهة المعاكسة. النقطة A تبعد عن O بتدريجتين في الجهة المعاكسة لجهة I ففاصلتها −2 ، والنقطة B تبعد عنها بثلاث تدريجات في جهة I ففاصلتها 3 ✓. الخطأ الشائع: عكس الاتّجاه الموجب فنجد xA = 2 و xB = −3 ؛ أو العدّ انطلاقًا من I بدل O فنجد xA = −3 و xB = 2 ؛ أو ارتكاب الخطأين معًا فنجد xA = 3 و xB = −2.`
- prompt : inchangé. « على الترتيب » devient redondant mais reste inoffensif ; la figure n'est pas
  touchée.

### R2 — MAJEUR — 11 Q3 et 11 Q6, énoncés : « AM = 2/3 AB » s'affiche « AB AM = 2/3 » (préexistant, manqué au premier audit)

Pourquoi le moteur casse cette ligne :
- La ligne « AM = 2/3 AB » est seule sur sa ligne et ne contient pas d'arabe.
- `isDisplayEquation` la refuse : rien ne rattache le « AB » final à la formule.
- `splitMathRuns` (chemin `splitLtrProse`) isole alors « AM = 2/3 » et laisse « AB » dans la prose.
- Dans le champ `dir="rtl"`, cette prose passe à gauche de l'isolat.

Mesuré dans Chromium, l'écran montre « AB AM = 2/3 ». Ce sont la donnée centrale des deux questions
et la clé de lecture de 11 Q3. En prose (explications), la même écriture se rend juste : seule la
ligne isolée est touchée.

Correctif : la mission écrit déjà « AM = 2/3 × AB » en 11 Q5 et en 11 Q6. Avec ce signe, la ligne
devient une ligne-équation, centrée et LTR, et se lit « AM = 2/3 × AB » dans Chromium.

- 11 Q3, prompt : remplacer la ligne `AM = 2/3 AB` par `AM = 2/3 × AB` (une occurrence, entre
  `بحيث` et `أيّ طريقة`).
- 11 Q6, prompt : remplacer la ligne `AM = 2/3 AB` par `AM = 2/3 × AB` (une occurrence, entre
  `بحيث` et `ما الفاصلة`).
- 11 Q3, explanation : l'aligner sur l'énoncé, puisqu'elle le cite (« الكتابة … »). Texte complet :
  `الكتابة AM = 2/3 × AB تعني أنّ AM يساوي جزأين من الأجزاء الثلاثة المتقايسة التي نقسم إليها القطعة [AB] ، ونأخذ الجزأين انطلاقًا من A لأنّ AM تُقاس من A ✓ ؛ فيبقى جزء واحد بين M و B. الخطأ الشائع: أخذ جزء واحد فقط فنجد AM = 1/3 × AB ؛ أو تقسيم القطعة إلى جزأين متقايسين فنجد منتصفها وAM = 1/2 × AB ؛ أو اعتبار 2/3 طولًا مطلقًا بدل كسر من الطول AB ، فتبعد M عن A بمقدار 2/3 سنتمتر فقط.`

### R3 — mineur — 11 Q6 (a) « −4/3 » : paire d'opposés avec la clé (mon texte m2)

Les options sont −4/3, −1/3, 4/3 (clé) et 10/3.
- Le vote par grandeur donne 4/3 (deux voix contre une) et range la clé dans la paire ±4/3.
- (d) 10/3 sort de [AB] (10/3 > 3 = xB).

Celui qui écarte 10/3 à vue tombe donc sur la paire qui contient la clé. J'avais noté cette paire
comme une « réserve assumée » au premier audit ; je reviens sur ce jugement.

Correctif : (a) devient `1/2`, qui reste muette. C'est l'erreur « M pris pour le milieu », la même
que l'option (b) de 11 Q3. Les contrôles sur {1/2, −1/3, 4/3, 10/3} :
- 1/2 est dans [AB] ;
- les grandeurs sont toutes distinctes ;
- aucune option n'est la somme ou la différence de deux autres (toutes les combinaisons ont été
  vérifiées) ;
- la clé « 4/3 » n'est pas strictement la plus longue.

Que 1/2 soit aussi la clé de 11 Q2 n'est pas une fuite : c'est un distracteur, et les calculs
diffèrent.

- option : a `1/2`.
- explanation, texte complet :
  `نقرأ على الشكل فاصلتَي A و B : −2 و 3 ، فـ AB = 5 سنتمترات و AM = 2/3 × 5 = 10/3 سنتمترًا. M من القطعة [AB] وتبعد عن A بمقدار 10/3 نحو B ، فنضيف هذا البعد إلى فاصلة A : xM = −2 + 10/3 = 4/3 ✓. تحقّق : بعد M عن A هو 4/3 − (−2) = 10/3 ✓. الخطأ الشائع: الاكتفاء بحساب البعد AM = 10/3 وكتابته على أنّه الفاصلة ، وننسى أنّ A ليست الأصل ؛ أو الخلط بين M ومنتصف القطعة [AB] فنجد xM = (−2 + 3) ÷ 2 = 1/2 ؛ أو القياس انطلاقًا من B بدل A فنجد 3 − 10/3 = −1/3.`

Je garde (d) 10/3, par exception assumée. C'est l'erreur la plus fréquente (AM rendu comme
abscisse), et son étiquette `reponse-a-l-autre-inconnue` (« un résultat intermédiaire ») est exacte.
Aucune valeur de cette erreur ne tombe dans [AB] : appliquer sans exception la règle « pas d'option
hors domaine » obligerait à perdre ce distracteur, ce que je déconseille. À arbitrer.

### R4 — mineur — 12 Q5, énoncé : le repère (C, A, D) n'est pas orienté (mon texte M4)

Mon texte décrit chaque axe par sa droite et sa longueur unité, mais pas par son sens. Rien n'y
impose A(1 ; 0) plutôt que A(−1 ; 0), ni D(0 ; 1) plutôt que D(0 ; −1). La clé (1/2 ; 0) n'est donc
unique que par les options.

Le cours 01, deuxième dans l'ordre R-3 et bien avant le 12, définit le terme « **النقطة الواحدية** »
(le point d'abscisse 1), et l'explication de la question l'emploie déjà. Le correctif reprend ce terme, ce qui fixe à la
fois l'unité et le sens, sans écrire les coordonnées.

- prompt, deuxième ligne : remplacer
  `ونذكّر أنّ المعيّن (C, A, D) أصله C ، ومحور فواصله المستقيم (CA) ووحدته الطول CA ، ومحور ترتيباته المستقيم (CD) ووحدته الطول CD.`
  par
  `ونذكّر أنّ المعيّن (C, A, D) أصله C ، والنقطة الواحديّة على محور فواصله (CA) هي A ، والنقطة الواحديّة على محور ترتيباته (CD) هي D.`
- prompt complet :
  `ليكن ABCD متوازي أضلاع ، ونذكّر أنّ قطريه [AC] و [BD] لهما المنتصف نفسه وهو مركزه I.\nونذكّر أنّ المعيّن (C, A, D) أصله C ، والنقطة الواحديّة على محور فواصله (CA) هي A ، والنقطة الواحديّة على محور ترتيباته (CD) هي D.\nما إحداثيّتا I في المعيّن (C, A, D) ؟`
- Options, clé et explication sont inchangées.

### R5 — mineur — 14 Q2, explication : « ✓ » collé à « 20 », qui est le distracteur (d) (mon texte M7)

Le texte actuel dit « … من تكرار كلّي قدره 20 ✓ ». À l'écran, la coche marque 20, et l'élève qui a
coché (d) 20 la lit comme une validation. La coche doit suivre 13.

- explanation : remplacer
  `فالعدد 13 المقابل للقيمة 0 هو عدد مرّات ظهور القيم −2 و −1 و 0 ، من تكرار كلّي قدره 20 ✓ ، أي القيم التي لا تتجاوز 0.`
  par
  `فالعدد المقابل للقيمة 0 هو عدد مرّات ظهور القيم −2 و −1 و 0 ، أي القيم التي لا تتجاوز 0 ، وهو 13 ✓ من تكرار كلّي قدره 20.`
- explanation complète :
  `التكرار المجمّع الصاعد عند قيمة هو مجموع تكرارات القيم الأصغر منها أو المساوية لها : فالعدد المقابل للقيمة 0 هو عدد مرّات ظهور القيم −2 و −1 و 0 ، أي القيم التي لا تتجاوز 0 ، وهو 13 ✓ من تكرار كلّي قدره 20. الخطأ الشائع: قراءة التكرار المجمّع للقيمة الموالية ، فالعدد 18 يوافق القيمة 1 أي القيم التي لا تتجاوز 1 ؛ أو استعمال الاتّجاه المعاكس فتُعدّ مرّات ظهور القيم التي لا تقلّ عن 0 فنجد 11 ؛ أو إعطاء التكرار الكلّي 20.`

## 3. Contrôles systématiques sur les 32 questions

- **Clés.** 32/32, résolues à l'aveugle avant lecture (table dans l'annexe).
- **Égalités des explications modifiées : toutes vraies.** Je les ai recalculées une à une :
  - 10 Q4 : (7 + 1) ÷ 2 = 4 ;
  - 11 Q6 : −2 + 10/3 = 4/3, 4/3 − (−2) = 10/3, −2 + 2/3 = −4/3, 3 − 10/3 = −1/3 ;
  - 12 Q6 : |−2 − (−√2)| = |√2 − 2|, 2 = √4, |−2| + |√2| = 2 + √2, |−√2| = √2 ;
  - 13 Q2 : les cinq centres, et les cinq moitiés de borne ;
  - 13 Q3 : −(1 − √2) = −1 + √2 = √2 − 1, (1 − √2) + (1 + √2) = 2, (1 + √2) + (√2 − 1) = 2√2 ;
  - 13 Q4 : 3a + 6 = 3 × (a + 2) ; 14, 34, 54, 74 et 94 ne sont pas multiples de 4 ;
  - 14 Q5 : 13 − 9 = 4, 18 − 13 = 5, 5 + 4 + 4 + 5 + 2 = 20 ;
  - 15 Q1 : 3√3 = √27, |1 − 3√3| = 3√3 − 1, (1 − 3)√3 = −2√3, |−2√3| = 2√3 ;
  - 15 Q4 : |√3 − (−√3)| = 2√3, 2 × √3 = 2√3, √3 + (−√3) = 0, √3 × √3 = 3, AB² = 12, 4 = 2².

  Les explications inchangées avaient été recalculées au premier audit.
- **Clé strictement la plus longue : 0/32** (script, et `content:tranche`).
- **Option somme ou différence de deux autres : 0** (script sur toutes les options numériques ; à la
  main pour 13 Q1, littérale).
- **Vote par composante.** Il ne reconstruit aucune clé. Pour les coordonnées et les listes :
  - 12 Q5 donne (1 ; 0), un distracteur ;
  - 14 Q4 donne (−2 ; ?) ;
  - 14 Q1 donne (? ; 0) ;
  - 13 Q2 donne (10, 20, ?, …) ;
  - 11 Q1 est à égalité partout.

  Pour les grandeurs, deux paires d'opposés contenant la clé sont inhérentes à l'erreur « signe non
  testé » : 12 Q6 (√2 − 2, 2 − √2) et 15 Q1 (1 − 3√3, 3√3 − 1). La troisième (11 Q6) a été
  introduite par mon texte, d'où R3.
- **Prémisse ou domaine.**
  - Les seules options hors domaine sont des erreurs dont l'élimination exige le savoir testé : les
    distances ou valeurs absolues négatives √2 − 2 et 1 − 3√3 supposent de tester le signe.
  - Exception assumée : 11 Q6 (d) 10/3 (voir R3).
- **Fuites.**
  - Route de quête (ordre du fichier, rampes croissantes) : aucune explication ne donne la clé
    d'une question suivante. 10 Q1 ne calcule pas 5/√5, 14 Q2 ne donne pas 4, 15 Q1 ne parle de
    2√3 que comme valeur d'un distracteur.
  - Donjon (tirage au hasard) : aucun énoncé ne contient la clé d'une autre question. Les liens
    d'étape restent les mêmes qu'au premier audit, notamment l'explication de 10 Q3 qui redonne la
    méthode de 10 Q1. Ils sont inhérents et acceptables, puisque 10 Q1 n'est plus un quasi-doublon.
- **Énoncés lisibles seuls** : oui. 12 Q5 l'est après R4.
- **Rampes non décroissantes** :
  - 10 : 1, 1, 2, 2 ;
  - 11 : 1, 1, 1, 1, 2, 2 ;
  - 12 : 1, 2, 2, 2, 2, 2 ;
  - 13 : 1, 1, 2, 2 ;
  - 14 : 1, 1, 2, 2, 2, 2 ;
  - 15 : 1, 1, 2, 2, 2, 2.
- **Métadonnées** : les six missions sont en d2, `practice`, 75 XP / 15 pièces, `displayOrder` 10 à
  15. Elles comptent 4 + 6 + 6 + 4 + 6 + 6 = 32 questions.
- **R-3.** Aucun vecteur, aucune translation : ni « شعاع », ni « انسحاب », ni flèche. Les techniques
  non enseignées sont données dans l'énoncé : 12 Q5 (repère, après R4), 13 Q3 (symétrie par rapport
  à (OJ)), 12 Q5 et 14 Q4 (milieu commun des diagonales).
- **Missions à 4 questions.**
  - 10 : le titre « معادلة بجذر وتوازي مستقيمين في المعيّن ووسيط سلسلة » couvre Q1/Q3, Q2 et Q4.
  - 13 : le titre « تناظر حول محور في المعيّن وقابلية القسمة ومراكز فئات الأعمار » couvre Q3, Q1/Q4
    et Q2.
  - Aucun texte ne renvoie à une question écartée. La phrase « لحساب معدّل الأعمار » de 13 Q2 motive
    les centres de classe, elle se lit seule.
  - Le nom de fichier de 13 garde « moyenne-classes ». Il est interne, et la mission n'est pas
    publiée : aucune action nécessaire.
- **Figure de 11** : identique octet pour octet dans les six questions (sha256 b0f34235…). Elle est
  juste : traits espacés de 24 px, A = −2, O = 0, I = 1, B = 3.

## 4. Étiquettes (libellés relus sur `origin/main`)

Les 23 identifiants posés dans 10 à 15 existent dans l'arbre et sur `origin/main`. Chaque placement
nomme l'erreur exécutée décrite par l'explication.

Les **cinq placements** cités par la consigne ne sont exacts qu'avec le libellé ÉLARGI
d'`origin/main`. Avec celui de l'arbre, ils sont inexacts :
- `operation-inverse-appliquee` (« … une division au lieu d'une multiplication (ou l'inverse) ») :
  - 10 Q1 (a), qui multiplie au lieu de diviser ;
  - 10 Q3 (d) 5√5, qui lit x ÷ √5 ;
  - 11 Q2 (a) −5/2, qui soustrait au lieu d'additionner.
- `moins-devant-parenthese` (« … qu'à une partie des termes ») : 13 Q3 (a), où −(1 − √2) est lu
  1 + √2.
- `effectif-cumule-non-cumule` (« l'effectif d'une valeur et son effectif cumulé ») : 14 Q5 (d) 13.

**Il faut donc synchroniser `content/misconceptions.json` sur `origin/main` (645 identifiants contre
632) avant le commit.** Le `build --check` actuel passe, mais il valide l'existence des identifiants,
pas l'exactitude des libellés.

Exacts avec les deux libellés :
- 10 Q3 (c) (x√5 lu x + √5 : « une somme au lieu d'un produit ») ;
- 11 Q4 (a) et 15 Q4 (d) (addition au lieu d'une soustraction) ;
- 12 Q1 (c) et (d), 13 Q4 (b) « 12 » et (d) « 4 » (`critere-divisibilite-mal-choisi` ; pour « 12 »,
  même choix que le précédent publié 03/15 Q4 (c), relu) ;
- 13 Q3 (c) ;
- 15 Q1 (a) (`termes-semblables-par-coefficient`, emploi publié en 03/15, 03/17, 03/18, 03/21, 03/23,
  03/24 et 03/25) ;
- 15 Q2 (a) et 15 Q3 (b) (`racine-et-carre-confondus`, précédents 03/18 et 03/20) ;
- 15 Q5 (d) (`difference-carres-second-terme-non-eleve-au-carre`) ;
- 12 Q6 (b) (`reponse-a-l-autre-inconnue`, OA donné pour AB, même emploi que 11 Q4 (c)).

Les options muettes le restent à bon droit :
- les deux erreurs combinées : 10 Q1 (d), 11 Q1 (d) ;
- les erreurs sans étiquette exacte : 10 Q1 (b), 11 Q1 (b) et (c), 11 Q6 (a) proposée 1/2 et (b).

Nouvel identifiant **`math.stat.mediane-lue-sans-ranger`** : accepté.
- Quatre questions distinctes, dont les trois questions publiées, relues sur `origin/main` :
  - 07/12-examen-2013 Q5 (d) « 40 », 5ᵉ valeur non rangée de 37, 36, 38, 39, **40** ;
  - 20/07-devoir Q3 (b) « أخذ القيمة الرابعة كما سُجّلت » ;
  - 20/07-devoir Q4 (d) « 15 », 4ᵉ valeur non rangée de 12, 17, 9, **15**.
- 10 Q4 (c) « 34 » est la 4ᵉ valeur non rangée de 31, 32, 31, **34**.
- Le libellé proposé (fr, en, ar) et la compétence `math.stat.moyenne-mediane` conviennent.

En attente dans les notes de l'auteur :
- `facteur-commun-signe-change` sur 14 Q3 (a) et 14 Q6 (c) est exact (« 27 − 2 » devenu « 27 + 2 ») ;
  à poser après la synchronisation.
- 14 Q4 (d) reste muette tant que `parallelogramme-sommets-mal-ordonnes` garde son libellé vectoriel.

Coquille dans `pending-tags/L08.json` : la note écrit « critere-divisibilite-mal-choisi sur … 13 Q4 c
(« 12 ») ». La lettre est **b** ; le fichier est juste.

## 5. Rendu (moteur `origin/main` `ce46894c`)

- arena#1142, fusionnée à 05:08 après les correctifs de l'auteur (05:01), répare la régression
  #1141 (M11). Je l'ai vérifié : `(80 + 100) ÷ 2 = 90 ✓ (…)` garde ses deux parenthèses. Le
  contournement de 13 Q2 n'est plus nécessaire, et il reste juste.
- Dans les six fichiers, aucune paire de parenthèses n'est coupée par une frontière d'isolat. Le
  seul défaut d'affichage restant est R2.
- **Constat moteur hors tranche, à remonter.** Le défaut de R2 touche aussi **12 lignes publiées**.
  Le mécanisme est le même : une ligne sans arabe, refusée par `isDisplayEquation`, découpée en isolat
  plus prose latine, puis inversée par `dir="rtl"`. Ordre affiché à l'écran (Chromium) :
  - 07/13-examen-2016 Q3 et Q4 : « 1 − |x| > 2/3 » s'affiche « > 2/3 |x| 1 − » ;
  - 04/15 Q5 et Q6 : « |x| ≤ 2 » et « |x| < 3 » s'affichent « ≤ 2 |x| » et « < 3 |x| » ;
  - 03/15 Q3 : « N = 5bababa4 » s'affiche « 5bababa4 N = » ;
  - 03/06 Q6 : « «4x² − 25 = (2x − 5)²» », dont une parenthèse est coupée ;
  - 18/20 Q7 : « |X| ≤ a ⟺ −a ≤ X ≤ a » s'affiche « ≤ a ⟺ −a ≤ X ≤ a |X| » ;
  - svt 04/02 Q3 et 04/04 Q1 : « e = 1,6 × 10⁻¹⁹ C » s'affiche « C e = … » ;
  - svt 05/04 Q2, 05/04 Q3 et 09/02 Q2 : équations chimiques mêlées.

  Piste : rendre toute ligne sans lettre arabe d'un champ RTL comme un seul isolat LTR, ou élargir
  `isDisplayEquation`.

## 6. Gates (moteur, en lecture seule, `content` → arbre du corpus)

- `build.ts --check --subject math` passe : 20 chapitres, 287 exercices, 1 975 questions,
  632 étiquettes.
- `qa.ts --subject math` : 0 erreur. Les 18 avertissements concernent d'autres chapitres ; aucun ne
  touche le chapitre 12.
- `tranche.ts --chapters 12` : aucune clé strictement la plus longue dans 10 à 15, et aucune paire
  proche ne concerne 10 à 15.

## 7. Ce que l'auteur ne pouvait pas savoir

- #1142 a été fusionnée après ses correctifs. M11 est désormais réglé dans le moteur.
- R2 tient au comportement du moteur sur une ligne isolée sans arabe. Seul un rendu navigateur le
  montre, et le premier audit l'a manqué.
- R1, R3, R4 et R5 viennent de mes propres textes du premier audit.
  - R1 : le plan 2×2 en couples nus est fermé par renversement.
  - R3 : j'avais accepté la paire ±4/3.
  - R4 : le sens des axes n'est pas fixé.
  - R5 : la coche est placée sur 20.
- La lettre « c » pour 13 Q4 dans `pending-tags/L08.json` est une coquille pour « b ».

## Annexe — Journal de progression

- Diff champ par champ (fichiers actuels contre `l08-backup-audited`) : les changements
  correspondent à la liste annoncée. 10 et 13 passent à 4 questions ; aucune autre question ne
  disparaît. Seul écart : 10 Q4 (c) « 34 » reste muette, l'identifiant `mediane-lue-sans-ranger`
  étant en attente.
- Figure de 11 : identique octet pour octet dans les six questions (sha256 b0f34235…, la même que
  l'état audité). Relecture au pixel : A = −2, O = 0, I = 1, B = 3.
- Résolution à l'aveugle des 32 questions, consignée avant lecture des clés, avec une seconde
  méthode pour chaque question modifiée :

| mission | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | ÷ √5 (c) ; 2ᵉ méthode : seule x√5 ÷ √5 donne x | (OJ) | x = √5 ; 2ᵉ : √5·√5 = 5 | 32 | — | — |
| 11 | −2 ، 3 ; 2ᵉ : pixels (84 − 132)/24 = −2, (204 − 132)/24 = 3 | 1/2 | 3 parts, 2 depuis A | 5 | 10/3 | 4/3 ; 2ᵉ : −2 + 2/3 × 5 |
| 12 | a = 2 ou 6 ; 2ᵉ : 70…79, seuls 72 et 76 | 9 | 15 | (6 ; 0) | (1/2 ; 0) ; 2ᵉ : B(1 ; −1), milieu de [BD] | 2 − √2 ; 2ᵉ : OB − OA = 2 − √2 |
| 13 | 3a + 6 | 10, 30, 50, 70, 90 | A et C | 6 | — | — |
| 14 | (1 ; 0) | 13 ; 2ᵉ : 5 + 4 + 4 | 27²⁰¹⁷ × 25 | (−1 ; −2) | 4 | 15 |
| 15 | 3√3 − 1 ; 2ᵉ : 3√3 ≈ 5,196 > 1 | 3 − 4√3 | 2 − √3 | 2√3 | (n − 4)(n + 4) | 15 |

- Clés lues ensuite :
  - 10 : c, a, b, d ;
  - 11 : a, b, a, d, c, c ;
  - 12 : a, c, c, b, d, d ;
  - 13 : d, a, b, c ;
  - 14 : a, b, d, c, b, d ;
  - 15 : c, b, c, b, a, d.

  **32/32 conformes.**
- Moteur relu : `ce46894c` (#1142) ; segmentation et Chromium refaits sur les 6 fichiers et sur
  tous les textes de remplacement.
- Libellés `origin/main` relus pour les 23 identifiants employés, et pour
  `facteur-commun-signe-change` et `parallelogramme-sommets-mal-ordonnes`. Questions publiées de
  `mediane-lue-sans-ranger` et précédent 03/15 Q4 relus sur `origin/main`.
- Contrôles de forme par script (32 questions), gates, rédaction : faits.
