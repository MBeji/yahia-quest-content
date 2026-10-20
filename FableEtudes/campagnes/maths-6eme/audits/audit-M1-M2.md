# Audit M1 + M2 — maths 6ᵉ, missions du gisement des chapitres 06, 07, 13, 14, 15 (auditeur indépendant, opus)

> Valide pour les 18 missions ci-dessous telles qu'au 2026-10-20 (worktree `wt-m6`, HEAD `a13bb91b`). Ré-auditer si ces
> fichiers bougent. Questions numérotées dans leur fichier (Q1 = première question du JSON). Options `a`…`d` = ids du
> fichier ; **(clé)** marque la bonne option ; « muette » = sans `misconceptionTag`. Chaque question a été re-résolue
> à l'aveugle (script pour toute valeur) AVANT lecture de la clé et des rapports `rapport-M1.md` / `rapport-M2.md`.

## Gates (depuis `/home/user/eng-deliver`, lien `content` → `/home/user/wt-m6/content` inchangé)

- `content:check` ✓ (121 sujets).
- `content:qa -- --subject math-6eme` : 7 erreurs + 8 avertissements, **aucun sur les 18 fichiers du lot** (erreurs au
  `25`, avertissements au `14/03`, `14/04`, `16`, `25` — autres lots).
- `content:figures:check` ✓ (le lot ne contient aucune figure).
- `content:tranche -- --chapters 06,07,13,14,15 --fresh --strict-longest` ✓ : clé strictement la plus longue 0/174 ;
  positions 25/26/26/22 %. 94 paires proches, toutes internes à une même mission (étapes d'un même problème qui
  redonnent les données officielles, règle R1) sauf une (`15/08#2` ↔ `22/09#3`, 0,50 : gestes différents, pas un
  doublon). 0 candidat gabarit, 0 cours en recul.
- `content:gisement:controle` sur les 3 devoirs : **0 plage de 8 mots**, 0 plage de 6, 0 source à 3 données ; 4 items à
  « 2 données communes » (`06/09` Q2, Q8 ; `14/10` Q6, Q7) — petits entiers, indicatif ; je n'ai pas lu les snapshots.
- **Fidélité** : les 12 sessions (2009, 2015–2021, 2023–2026) confrontées à la transcription ET au PDF
  (`pdftoppm -r 150`, page 1 ou 2) : toutes les données, unités et décimaux à trois chiffres sont exacts. Prémisses
  ajoutées, toutes justifiées : « les trois clients sont tous les clients du jour » (2025, implicite au sujet) ; 60 km
  et 3,2 km (valeurs des « أثبتُ أنّ » officiels) ; 144 km, 68 d, 7803 d, 30 d… redonnés dans les étapes suivantes
  (clés d'étapes antérieures, jamais d'une étape postérieure dans l'ordre du fichier).
- **Rendu** : chaînes suspectes passées dans `isolateLtrRuns`/`isolateLtrRunsHtml` puis Chromium `dir=rtl` à 360 px, ordre
  visuel mesuré par `Range.getBoundingClientRect` : voir **C-1** (le seul défaut de rendu du lot). `1/200 000`
  (U+00A0), `(1 km = 100 000 cm)`, fractions, `7,2 د` s'affichent correctement. 0 chiffre arabe-indien, 0 LaTeX,
  `\d \d{3}` toujours en U+00A0.
- `chapter.json` : `sources[]` correct dans les 5 chapitres (ligne « Sujets officiels… » au 06, 13, 14, 15 ; ligne
  « Calibré sur des devoirs publics… » au 06, 07, 14).

## Le point à juger : le pourcentage (et la fraction) donnés dans l'énoncé avant d'être enseignés

**Au `13` (2016, 2015, 2009) — suffisant.** À ce point du manifeste l'élève sait prendre une fraction d'une quantité
(`08` § « كسرٌ من كمّية », `13` § « كسرٌ من كميّة »), retrouver le tout (`13` § « من الجزء إلى الكلّ »), écrire « un
nombre par rapport à un autre » comme fraction (`08` § « عددٌ بالنسبة إلى عدد آخر »), diviser un décimal par un entier
(`05`) et lire 0,15 = 15/100 (`12`). Le rappel « 15 % من عدد تعني 15/100 منه » suffit donc pour 2015 Q5–Q6 ; le
rappel « النسبة المائويّة كسر مقامه 100، مثلًا 1/4 = 25/100 أي 25 % » suffit pour les deux taux (2016 Q7 : 10,2 ÷ 68
= 0,15 ; 2009 Q7 : 37,12 ÷ 116 = 0,32), l'exemple ne livre ni 15 ni 32, et la question de la **base** (2016 Q4, 2009 Q6)
est portée par un QCM dédié dont l'énoncé dit la base officielle (« بالنسبة إلى الثمن الأصلي / الاستهلاك السابق »).
Rien à corriger au `13` sur ce point.

**Au `06` (2018 et aussi 2020) — insuffisant → M-1.** Le rappel « 41 % = 41/100 de ce nombre » présuppose « prendre une
fraction d'un nombre », enseigné au `08`, deux chapitres PLUS LOIN que le `06`. Et le défaut est plus large que le
pourcentage : les deux missions placées au `06` par l'exception E-3 font aussi, **sans aucun rappel**, de la fraction
d'une quantité, de la fraction supérieure à 1 et du retour au tout (`08`, `13`). 10 des 16 questions de ces deux
missions exigent une notion non encore enseignée. Voir M-1 pour les deux issues possibles.

## Défauts classés

### Critique (1)

**C-1 — `07-criteres-divisibilite/exercices/06-devoir-chiffres-manquants-plusieurs-criteres.json`, Q1, Q2, Q3, Q4, Q6 :
le nombre à chiffre manquant s'affiche À L'ENVERS.** Dans une phrase arabe, `8▢5` est EN·ON·EN après une lettre
arabe : les chiffres deviennent AN (règle W2), le ▢ se résout en R (N1) et le groupe est réordonné. Mesure Chromium
(`dir=rtl`, après `isolateLtrRunsHtml`, qui ne l'isole pas) : `2▢4` s'affiche **4▢2**, `8▢5` **5▢8**, `27▢▢`
**▢▢27**. Conséquences : Q1 affiche un nombre qui finit par 8 (« divisible par 5 » devient impossible) ; Q6 affiche
`▢▢27` (unités 7, aucune solution divisible par 2 et 5) ; Q2–Q4 affichent `4▢6`, `4▢2`, `7▢5` (les clés survivent par
symétrie de la somme, mais l'élève lit un autre nombre). **Hors lot, même défaut** dans tout le chapitre 07 :
`cours.md`, `resume.md`, `quiz.json`, `01-pratique`, `02-boss`, `04-defi`, `05-entrainement` (grep `\d▢|▢\d`).
Correctif préférable : **moteur** — faire isoler par `isolateLtrRuns` tout run chiffres+▢ (ajouter ▢ U+25A2 au signal
`BIDI_FLIP_SIGNAL` ou traiter `\d[▢]+\d*|▢+\d` comme une formule à isoler), test de non-régression avec `2▢4`, `27▢▢`,
`▢51`. Repli **contenu** pour la mission (vérifié en Chromium, s'affiche juste), en remplaçant les seuls énoncés :
- Q1 : `مُسح رقم العشرات من عدد مكتوب على بطاقة، فبقي رقم مئاته 8 ورقم آحاده 5. ما أصغر رقم نضعه في خانة العشرات ليقبل العدد القسمة على 5 وعلى 3 معًا؟`
- Q2 : `على بطاقة عدد من ثلاثة أرقام: رقم مئاته 6 ورقم آحاده 4، ورقم عشراته ممسوح. نعلم أنّ العدد يقبل القسمة على 2 وعلى 3 معًا. ما الأرقام التي يمكن أن تكون في خانة العشرات؟ اختر كلّها:`
- Q3 : voir M-3 (nombre changé) — `على بطاقة عدد من ثلاثة أرقام: رقم مئاته 4 ورقم آحاده 1، ورقم عشراته ممسوح. إذا علمنا أنّ العدد يقبل القسمة على 9، فما الرقم الممسوح؟`
- Q4 : `على بطاقة عدد من ثلاثة أرقام: رقم مئاته 5 ورقم آحاده 7، ورقم عشراته ممسوح. نعلم أنّ العدد يقبل القسمة على 3 ولا يقبل القسمة على 9. كم رقمًا مختلفًا يمكن أن يكون الرقم الممسوح؟ اكتب عدد الأرقام فقط.`
- Q6 : `عدد من أربعة أرقام: رقم آلافه 2 ورقم مئاته 7، ورقما عشراته وآحاده ممسوحان. ما أصغر عدد نحصل عليه بملء الخانتين ليقبل القسمة على 2 وعلى 3 وعلى 5 وعلى 9 معًا؟ اكتب العدد فقط.`
Les explications n'accolent jamais ▢ à un chiffre : inchangées (sauf Q3, M-3).

Aucune clé fausse, aucune question à deux réponses, aucune donnée infidèle.

### Majeur (8)

**M-1 — scope du `06` : `07-exam-2020-p2-jouets-restes-egaux.json` Q1, Q4, Q5, Q6, Q8 et
`08-exam-2018-p1-costumes-restes-et-benefice.json` Q2, Q3, Q4, Q7, Q8.** Fraction d'une quantité (3/5, 4/7, 41/100),
fraction > 1 (11/7) et retour au tout (« 2/5 du second = 1920 », « 11/7 du coût = 77 440 ») sont enseignés au `08` et
au `13` ; le `06` n'enseigne aucune fraction, et seul le pourcentage reçoit un rappel (lui-même inutilisable sans la
fraction d'un nombre). Le placement vient de E-3 (pilote) : **à soumettre au pilote**, deux issues :
1. (conseillée) déplacer m002 et m003 au `13` (étape « retrouver le tout », où vont déjà 2016/2015/2009 ; les restes
   égaux y sont une révision du `06`, antérieur), en gardant au `06` m001 (2023) et le devoir, qui n'utilisent que le `06` ;
2. sinon, ajouter un rappel en fin d'énoncé de chaque question citée (vérifié en Chromium, ne contient aucune clé) :
   2020 : `(تذكير: 3/5 عدد يعني أنّنا نقسم هذا العدد 5 أجزاء متساوية ونأخذ منها 3.)` ;
   2018 : `(تذكير: 4/7 الكلفة يعني أنّنا نقسم الكلفة 7 أجزاء متساوية ونأخذ منها 4.)` — le retour au tout (« les
   parts connues ÷ leur nombre, × le dénominateur ») reste alors non enseigné : l'issue 2 est un pis-aller.

**M-2 — options qui nient une prémisse de l'énoncé (éliminées à vue).** Remplacements vérifiés (fausseté recalculée,
longueurs mesurées : la clé n'est jamais strictement la plus longue ; rendu Chromium contrôlé) :
- `06-multiples-communs/…/06-exam-2023-p1…` **Q4** option `a` (« لا يوجد أيّ مضاعف » alors que l'énoncé pose un multiple
  dans l'intervalle) → `يوجد مضاعفان على الأقلّ، لأنّ طول المجال 30 أكبر من 17 ومن 7` (muette ; longueurs 60/76/51/58,
  clé `d` 58). Explication : remplacer la dernière phrase par `وطول المجال 30 أكبر من 17 ومن 7 لا يهمّ، لأنّ القفز بين المضاعفات المشتركة يكون بـ 119 لا بـ 17 ولا بـ 7.`
- `06-multiples-communs/…/07-exam-2020-p2…` **Q7** option `a` « 4811 » (hors de 9600–9700) → `9626` (muette : le reste
  4 ajouté une fois par diviseur, 9614 + 12 ; 9626 = 11 × 875 + 1, faux). Explication : ajouter
  `أو إضافة الباقي 4 مرّة لكلّ قاسم فنجد 9614 + 12 = 9626.`
- `06-multiples-communs/…/09-devoir…` **Q7** option `a` « 98 » (hors de 100–115) → `112` (muette : même reste aux deux
  divisions, mais 4 et non 2 ; 112 = 6 × 18 + 4 = 12 × 9 + 4). Explication : remplacer
  `أو نسيان الحصر بين 100 و115 فنكتب 98` par `أو أخذ عدد باقيه مشترك لكنّه 4 لا 2 فنكتب 112`.
- `13-…/06-exam-2025-p1…` **Q5** option `c` « لا خطأ في قولها… » (l'énoncé demande « ما خطؤها؟ ») →
  `قسمتها صحيحة، لكنّ 30 د هو ثمن الباقة الحمراء لا البيضاء` (muette ; faux : la rouge vaut 36 d ; longueurs
  58→56/54/37/53, clé `d` 53). Explication : ajouter `ولا يصحّ القول إنّ 30 د ثمن لون آخر، فلا لون ثمنه 30 د.`
- `13-…/09-exam-2009-p1…` **Q6** option `d` « لا خطأ في ذلك… » → `كان عليه أن يقسم المبلغ المقتصد على 100 فقط، فالنسبة المائويّة كسر مقامه 100`
  (muette ; l'étiquette `pourcentage-base-erronee` disparaît avec l'option : l'erreur de base est celle que décrit la
  clé ; longueurs 53/58/42/76, clé `b` 58). Explication : remplacer `والضرب أو قلب القسمة لا يعبّران عن نسبة جزء إلى كلّ.`
  par `والضرب أو قلب القسمة لا يعبّران عن نسبة جزء إلى كلّ، والقسمة على 100 وحدها لا تقارن الاقتصاد بأيّ إنفاق.`
- `14-…/07-exam-2024-p2…` **Q4** : `b` « من 1 إلى 100 » et `c` « لا توجد شريحة ممكنة » contredisent l'énoncé (plus de
  136 h, même somme) : il reste deux options. Réécrire en « pourquoi pas la 2ᵉ tranche » (le tableau de l'énoncé est
  gardé) — fin d'énoncé : `… رغم أنّها اختارت عددًا من الساعات أكبر من 136. لماذا لا يمكن أن تقع ساعاتها في الشريحة من 101 إلى 149 ساعة؟` ;
  options : `a` **(clé)** `لأنّ الساعة فيها بـ 7,2 د، فأكثر من 136 ساعة تكلّف أكثر من أمين` ;
  `b` `لأنّ التخفيض فيها أكبر من التخفيض الذي تمنحه الشريحة الثالثة` ;
  `c` `لأنّ ثمن الساعة فيها 7,2 د، وهو أغلى من ثمن الساعة دون أيّ تخفيض` ;
  `d` `لأنّ المبلغ فيها لا يتغيّر بعدد الساعات، فهو ثابت للشريحة كلّها` (toutes muettes ; longueurs 63/60/64/63 ;
  b faux : 1/10 < 20 % ; c faux : 7,2 < 8 ; d faux : 9/10 du coût horaire). Explication :
  `في الشريحة من 101 إلى 149 تكلّف الساعة 9/10 × 8 = 7,2 د، فكلّ ساعة زائدة على 136 تزيد المبلغ، ولا يمكن أن يتساوى المبلغان. تخفيض هذه الشريحة عُشر واحد، أي أقلّ من 20 %، و7,2 د أرخص من 8 د، والمبلغ يُحسب بعدد الساعات في كلّ شريحة. يبقى أن تكون ساعات ياسمين أكثر من 149.`
  (ne contient ni 6,4 ni 153 ; « أكثر من 149 » était déjà la clé de l'ancienne Q4.)
- `14-…/07-exam-2024-p2…` **Q7** : `b` « لا خطأ… » nie la prémisse ; la clé `d` « العدد 136 لا يفوق 136، فالصواب ثمن شريحتها »
  est une phrase tronquée. Options : `a` inchangée (étiquette gardée) ;
  `b` → `كان عليه أن يقسم المبلغ على 8 د، ثمن الساعة دون أيّ تخفيض` (muette ; 979,2 ÷ 8 = 122,4) ;
  `c` → `أخطأ في الحساب نفسه، فحاصل هذه القسمة لا يساوي 136` (muette ; faux, 979,2 ÷ 7,2 = 136) ;
  `d` **(clé)** → `قسم على ثمن ساعة أمين، وساعات ياسمين في شريحة أرخص` (longueurs 47/57/50/50).
  Explication inchangée.

**M-3 — `07-…/06-devoir…` Q3 reprend l'exemple du cours** (`cours.md` l. 300 « العدد 2▢4 », même nombre, critère 9 au
lieu de 3, et 234 y figure déjà). Nombre changé en 441 : énoncé = celui de C-1 Q3 (forme sans ▢) ; options `a` `1`
(étiquette `math.num.critere-divisibilite-mal-choisi` : somme 6, multiple de 3), `b` `4` **(clé)**, `c` `7` (même
étiquette : somme 12), `d` `9` (muette : somme 14) ; `correctOption` `b`. Explication :
`مجموع الرقمين المعروفين 4 + 1 = 5، ويجب أن يصير المجموع مضاعفًا لـ 9: 5 + 4 = 9، والمجموع 18 يتطلّب 13 وهو ليس رقمًا، فالرقم 4 والعدد 441 = 9 × 49. الرقمان 1 و7 يعطيان المجموعين 6 و12، وهما مضاعفان لـ 3 لا لـ 9، فيقبل العدد معهما القسمة على 3 وحدها؛ والرقم 9 يعطي المجموع 14 فلا يقبل العدد القسمة على 3 ولا على 9.`
(441, 411, 471, 491 recalculés ; aucun 4▢1 dans le chapitre.)

**M-4 — `14-…/10-devoir-plan-et-carte-a-l-echelle.json` Q1 redemande le piège du cours** (`cours.md` « ⚠️ القسمة بدل
الضرب حين نعود من الخريطة إلى الحقيقة », 6,7 cm à 1/1 000 000). Remplacement (geste neuf de la carte : lire l'échelle en
km) : `على خريطة سلّمها 1/200 000، كم كيلومترًا في الحقيقة يمثّله 1 cm على الخريطة؟ (1 km = 100 000 cm)` (espaces de
groupe en U+00A0) ; options `a` `0,2 km`, `b` `2 km` **(clé)**, `c` `20 km`, `d` `200 km` (muettes) ; explication :
`السلّم 1/200 000 يعني أنّ 1 cm على الخريطة يمثّل 200 000 cm في الحقيقة. وبما أنّ 1 km = 100 000 cm فإنّ 200 000 cm = 200 000 ÷ 100 000 = 2 km. العدد 200 يقسم على 1000 كأنّ الكيلومتر 1000 cm، والعدد 20 يقسم على 10 000، والعدد 0,2 يقسم على 1 000 000.`
(U+00A0 dans tous les groupes ; difficulté 1 gardée.)

**M-5 — `06-multiples-communs/…/09-devoir…` Q6 redemande `06/04-defi#3`** (« كم مضاعفًا مشتركًا للأعداد 4 و 6 و 8
محصورًا بين 1 و 130؟ » ↔ « كم مضاعفًا مشتركًا … 12 و20 يقع بين 700 و1000؟ » : même tâche, autres nombres).
Remplacement (numeric, difficulté 3) : `كم عددًا محصورًا بين 700 و1000 هو مضاعف للعدد 12 وليس مضاعفًا للعدد 20؟ اكتب عدد هذه الأعداد فقط.` ;
`answerKey.value` 20 ; explication :
`مضاعفات 12 بين 700 و1000 تبدأ بـ 708 = 12 × 59 وتنتهي بـ 996 = 12 × 83، فعددها 83 − 59 + 1 = 25. نُبعد منها المضاعفات المشتركة للعددين 12 و20، وهي مضاعفات 60 (أصغر مضاعف مشترك غير معدوم لهما): 720 و780 و840 و900 و960، أي 5 أعداد. يبقى 25 − 5 = 20 ✓. الخطأ الشائع: نسيان أحد الطرفين عند العدّ (83 − 59 = 24)، أو طرح كلّ مضاعفات 20 الواقعة في المجال بدل المضاعفات المشتركة وحدها.`
(recalculé : 25 multiples de 12, 5 de 60, 20.)

**M-6 — étiquette dont le libellé n'est pas l'erreur : `15-…/06-exam-2026-p2…` Q6**, option `a` « 60 km/h » portant
`math.prop.pourcentage-recopie-comme-resultat` (« 20 % de 80 n'est pas 20 ») : l'option donne la vitesse du camion, une
autre grandeur → `math.alg.reponse-a-l-autre-inconnue`.

### Mineur (14)

1. `07/06-devoir` Q6 (27▢▢ → 2700/2790) suit le cas limite du cours « 72▢0 يعطي 7200 و7290 » (0 et 9 à la fois) :
   acceptable (autre nombre, deux chiffres manquants), à signaler.
2. `06/07-exam-2020` Q3 : la règle « produit = plus petit multiple commun » est donnée puis appliquée telle quelle (la
   question se réduit à 11 × 19 × 23) ; Q4 et Q5 se doublent (4800 puis 2880 = 4800 − 1920). Toléré (étapes prévues
   par la carte).
3. `06/07-exam-2020` Q6 et `13/09-exam-2009` Q4 (`ordering`) ne disent pas leur session : ajouter `(مناظرة 2020) ` /
   `(مناظرة 2009) ` en tête d'énoncé.
4. `06/08-exam-2018` Q3 : l'option `c` « 7/11 » exécute exactement `math.frac.numerateur-denominateur-inverses` → l'étiqueter.
5. `14/09-exam-2019` Q8 : `a` « 125 % » exécute le piège C08#1b (remise prise pour une hausse) → étiqueter
   `math.num.operation-inverse-appliquee` ; `d` « 175 % » n'exécute aucune erreur → `100 %` (muette : la remise oubliée).
6. `15/09-exam-2017` Q8 : `c` « 6 و 43 » (étiquette base 100) suppose « 1 h 15 min », impossible à obtenir puisque l'énoncé
   donne 1 h 55 ; `b` « 7 و 8 » sans mécanisme. Proposé : `c` → `الساعة 6 و 23 دقيقة` (muette : 83 − 60 sans reporter
   l'heure), `b` gardé (muet, faute d'un mécanisme meilleur) ; retirer l'étiquette de `c` et
   adapter la dernière phrase de l'explication.
7. `13/06-exam-2025` Q6/Q7 (jaune, blanche) ne diffèrent que par la couleur, et Q7 (24 d) donne l'essentiel de Q8 (24 ÷ 12) ;
   `14/06-exam-2026` Q2/Q3 (100 puis 300) ; `14/10-devoir` Q2/Q3 (13 km puis 8 km, même calcul) : étapes peu
   informatives, prévues par les cartes.
8. `14/08-exam-2021` Q8 (d3) : l'énoncé prescrit l'opération (« بعد طرح الـ 150 د ») — c'est un 7803 − 150 ; calibrer d2 ou fondre dans Q9.
   Q5 : « 33 % » n'est que l'arrondi de l'erreur (1/3 = 33,33… %), acceptable.
9. `14/06-exam-2026` Q5 : `pourcentage-base-erronee` sur « 20 د » (5 % de 400 caisses) : le libellé parle de prix de
   départ/final, l'erreur est une base de nature différente ; acceptable faute de mieux. Q6 `d` 1200 (=60 × 20) et
   `15/06` Q2 `d` 1000 km : remplissage.
10. `15/07-exam-2023-p3` : la figure du sujet (parcours أ–ب–ج, deux parties) n'est pas redessinée ; Q4 sans étiquette
    (« 18 » = partage égal, piège C04#3b, pas d'id au registre ; « 6 » sans mécanisme) ; Q9 `d` faux à vue (12 > 10).
11. `15/07` Q1 (48 min → 0,8 h) et `15/08` Q1 (1 h 36 → 1,6 h) : même gabarit QCM « conversion, distracteur base 100 »
    dans deux missions du même chapitre, et `15/08` Q1 reprend le piège du cours (l. 239, « 1 سا 30 د = 1,5 لا 1,30 ») avec
    les nombres officiels. Toléré (étape officielle) ; on pourrait passer `15/08` Q1 en numérique (« كم دقيقة … » → 96).
12. Coïncidences officielles qui créditent une réponse fausse : `14/09` Q9 (210 d = aussi le reste de Q4) ; `15/08` Q9
    (pause 12 min = aussi le temps restant de la voiture, Q4). Inévitables (données du sujet), à connaître.
13. `13/08-exam-2015` Q4 `a` « 48,5 د » (46 + 2,5) : distracteur faible.
14. Pièges des cartes sans id au registre (options laissées muettes, correct) : intervalle oublié (119, 9614, 108),
    reste oublié, recette ÷ billets totaux, fraction appliquée aux seules autres parts (48), tout non retrouvé (2/13 de 240,
    2/5 de 45,8 — 18,32 porte `operation-inverse-appliquee`, lecture admissible), mauvaise tranche, retour oublié,
    3/2 lu comme part du total, écart attribué à la table. À proposer au registre (les deux auteurs l'ont signalé).

Fuites : aucune « fuite en avant » dans l'ordre des fichiers (les énoncés ne redonnent que des clés d'étapes
antérieures ; les explications ne livrent aucune clé d'une question postérieure). Les redites de clés antérieures
(72, 68, 57,8, 46, 161, 144, 7803, 30 d, 1 h 55) rendent chaque question autonome au donjon, au prix d'une aide si
l'ordre est tiré au hasard : choix des auteurs, déclaré, accepté.

## Tableaux de re-résolution (ma réponse = clé du fichier, sauf mention)

| fichier | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 06/06 exam 2023 P1 | 119 | 1500 | a | d | 2023 | 15 | | | | | OK ; M-2 (Q4) |
| 06/07 exam 2020 P2 | 2/5 | a | 4807 | 4800 | 2880 | a,b,c,d | 9618 | 1938 | | | OK ; M-1, M-2 (Q7), m2, m3 |
| 06/08 exam 2018 P1 | b | a | 11/7 | c | 598 | 605 | 49 280 | 20 204,8 | | | OK ; M-1, m4 |
| 06/09 devoir | 720 | 360 | 960–1080 | a | a,b,c,d | 5 | 110 | 192 | | | OK ; M-2 (Q7), M-5 |
| 07/06 devoir | 2 | {2,5,8} | 3 | 3 | a,b,c,d | 2700 | | | | | OK ; **C-1**, M-3, m1 |
| 13/06 exam 2025 P1 | 2/3 | a,b,c,d | 72 | 108 | d | 48 | 24 | 2 | | | OK ; M-2 (Q5), m7 |
| 13/07 exam 2016 P1 | 27,2 | 13,6 | 57,8 | c | 68 | 10,2 | 15 | | | | OK |
| 13/08 exam 2015 P1 | a | 46 | 115 | 161 | 138,125 | c | | | | | OK ; m13 |
| 13/09 exam 2009 P1 | 120 | 37,12 | 1560 | a,b,c | 1800 | b | 32 | | | | OK ; M-2 (Q6), m3 |
| 14/06 exam 2026 P1 | 1/4 | 100 | 300 | 9000 | 450 | 30 | 115 | | | | OK ; m7, m9 |
| 14/07 exam 2024 P2 | b | 1088 | 979,2 | a | 6,4 | 153 | d | | | | OK ; M-2 (Q4, Q7) |
| 14/08 exam 2021 P1 | d | 3500 | 7000 | 7803 | 25 % | 50 | b | 7653 | 51,02 | 5102 | OK ; m8 |
| 14/09 exam 2019 P1 | a | 60 | 30 | 210 | 4/7 | 52,5 | 157,5 | 75 % | 210 | | OK ; m5, m12 |
| 14/10 devoir | a | 13 | 8 | 21 | 42 | 4 | c | | | | OK ; M-4, m7 |
| 15/06 exam 2026 P2 | 3/4 | 10 km | 120 | 6 | 60 | 80 | c | 200 | | | OK ; M-6, m9 |
| 15/07 exam 2023 P3 | 0,8 | 8 | 3,2 | 12 | 0,2 | 16 | 40 | 124 | a | | OK ; m10, m11 |
| 15/08 exam 2021 P2 | 1,6 | 128 | 144 | 12 | 28,8 | 72 | 24 | 36 | 12 | | OK ; m11, m12 |
| 15/09 exam 2017 P1 | 40 | 60 | 100 | 3/5 | 60 | d | 115 | a (7 h 23) | | | OK ; m6 |

Chaque distracteur a été recalculé faux ; chaque étiquette exécute son libellé, sauf M-6 (et la lecture lâche de m9).
Étages : examens d3 boss 120/30, devoirs `06/09` d3 boss, `07/06` et `14/10` d2 practice 75/15 — conformes aux cartes
(E-2) ; ≤ 12 questions partout ; titres sans clé ; aucun ⛔/◐, ni Pythagore, ni somme des angles, ni intérêt, ni
partage somme-écart/somme-rapport ; aucun `short_answer` (pas d'`acceptedAnswers` à juger), aucune étiquette sur
`multi`/`ordering`, options à deux erreurs muettes (`14/08` Q7 `d`, `15/06` Q7 `d`).

## Synthèse

| lot | missions | questions | clés fausses | critique | majeur | mineur | questions à reprendre |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| M1 (06, 07, 13) | 9 | 64 | 0 | 1 (5 q.) | 5 | 8 | 19 (dont 10 par M-1, à arbitrer) |
| M2 (14, 15) | 9 | 74 | 0 | 0 | 3 | 8 | 4 |
| **total** | **18** | **138** | **0** | **1** | **8** | **14** | **23** |

**Verdict : à corriger.** Fidélité aux sujets et justesse des 138 clés : sans défaut. Avant publication : C-1 (le
devoir du `07` affiche ses nombres à l'envers — et tout le chapitre 07 avec lui : correctif moteur conseillé), M-2 à M-6
(textes de remplacement fournis ci-dessus, vérifiés par script et en Chromium), et l'arbitrage du pilote sur M-1
(déplacer 2020 P2 et 2018 P1 au `13`, conseillé). Réponse au point posé : le rappel du pourcentage **suffit au `13`**,
**ne suffit pas au `06`**, où manque d'abord la fraction d'une quantité.
