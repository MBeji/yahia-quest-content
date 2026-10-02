# Audit indépendant — tranche SVT-L01 (SVT 9ᵉ, gisement, examens nationaux)

Statut : TERMINÉ — 36/36 questions re-résolues à l'aveugle, 0 clé fausse, 11 défauts majeurs
(11 questions à reprendre), 14 mineurs. Verdict : à corriger avant livraison (voir « Chiffre
final » en fin de rapport).

Périmètre : 6 missions, 36 questions (02/07, 02/08, 05/07, 05/08, 07/07, 07/08), arbre de travail
de `/home/user/yahia-quest-content` au 2026-10-02 ; cours, résumés, registre `bio.*` (95 id) et
manifeste lus sur `origin/main` (23a2b43f) ; transcriptions 2020/2021/2022/2024 de l'arbre de
travail ; PDF officiels C03 (2024), C04 (2022), C05 (2021), C06 (2020) — empreintes sha256
identiques à celles des transcriptions — rendus à 110 et 300 dpi et regardés page par page.
Méthode : chaque question re-résolue à l'aveugle (énoncé + options affichés sans clé ni
explication par script) AVANT lecture de la clé ; figures rendues dans Chromium ; chaînes mixtes
passées dans `isolateLtrRuns` / `splitMathRuns` (`bidi.ts` d'arena `origin/main`, #1152).

## Avancement

- [x] 02/07 (2024 ex.5)
- [x] 02/08 (2021 ex.4)
- [x] 05/07 (2021 ex.2)
- [x] 05/08 (2022 ex.4)
- [x] 07/07 (2024 ex.1)
- [x] 07/08 (2020 ex.3)

---

## 02/07 — `02-al-af3al-al-in3ikasiya/exercices/07-examen-2024-ex5-nerf-sciatique-sectionne-bouts-central-peripherique.json`

En-tête : « 🏛️ مناظرة 2024 · التمرين 5 ⭐⭐⭐: تنبيه طرفَي عصب النّسا المقطوع عند ضفدعة نخاعيّة »,
d3 boss 120/30, displayOrder 7 — conforme (patron, table canonique, sujet = notions, aucun résultat).
Rampe 2,2,3,3,3,3 non décroissante. Étage d3 honnête (Q3–Q6 combinent arc réflexe + coupure +
lecture des deux bouts).

| Q | type | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | mcq d2 | b | b | OK | sensitif bloqué à la coupure ; étiquette d exacte |
| 2 | mcq d2 | d | d | OK (mineur) | fibres motrices du bout périphérique ; faute d'arabe en a |
| 3 | mcq d3 | a | a | OK | bout central → moelle → ordres ; étiquettes c, d exactes |
| 4 | mcq d3 | c | c | RÉSERVE (majeur) | 2 distracteurs sur 3 contredits par l'énoncé |
| 5 | mcq d3 | b | b | RÉSERVE (majeur) | doublon de fait avec Q6 |
| 6 | multi d3 | {a,d,e} | {a,d,e} | RÉSERVE (majeur) | d + e = clé de Q5 mot pour mot ; a ⟺ d ∧ e |

Fidélité au sujet 2024 ex.5 : les trois expériences et leurs résultats sont exacts (vérifiés sur
la transcription ET sur le PDF C03 p. 4, Doc 7) ; le découpage exp. 1 → Q1, exp. 2 → Q2,
exp. 3 → Q3 (les trois membres fléchis) + Q4 (la jambe droite non fléchie) ne perd rien de la
sous-question 1. La sous-question 2 (« استنتج دور عصب النسا … وحدّد طبيعة أليافه ») est une seule
idée : la scinder en Q5 (rôle) + Q6 (nature) crée le doublon ci-dessous. Notions données dans
chaque énoncé qui les emploie : bout périphérique « أي طرفه المتّصل بالسّاق » (Q2, Q6), bout
central « أي طرفه المتّصل بالنّخاع الشّوكيّ » (Q3, Q4, Q6), Q5 n'emploie que « المتّصل بـ… » : OK.
« ضفدعة نخاعيّة », « سيالة جاذبة/نابذة », « ألياف حسّيّة/حركيّة », « عصب مزدوج » : cours 01/02.

Figure (4 SVG, même grenouille ; rendues) : vue dorsale, moelle = bande rose, nerfs bleus, coupure
visible (lacune + deux traits) sur la CUISSE droite du dessin, P au bout distal (Q2), C au bout
proximal (Q3, Q4), aiguille sur le pied droit (Q1) ; viewBox 0 0 300 290, rien ne déborde, arabe
dans `<title>` seulement, aucun élément interdit, aucune clé dessinée. Conforme au Doc 6 du PDF
(coupure du nerf de la patte du côté droit du dessin, au niveau de la cuisse), à une réserve près
(mineur ci-dessous).

### Défauts

**[MAJEUR] Q4 — deux distracteurs sur trois s'éliminent par l'énoncé.** L'énoncé pose « انثنت
كلّ الأطراف ما عدا السّاق اليمنى ». Option a « … فلم يولّد أيّ أمر » nie cette prémisse (si la moelle
n'avait produit aucun ordre, rien n'aurait fléchi — l'explication le dit elle-même : « بدليل انثناء
الأطراف الأخرى ») ; option d « والانثناء يستلزم تنبيهًا مباشرًا للطّرف » est démentie par les trois
membres qui ont fléchi sans être stimulés. Reste un duel b/c. Correctif (vérifié : aucun ne nie
de prémisse, les deux sont faux dans le fait, la clé c = 76 car. n'est pas la plus longue) :
- a → « الألياف الحسّيّة لعصب النّسا الأيمن مقطوعة، فلا تنقل الأمر الحركيّ من النّخاع إلى عضلات السّاق »
  (94 car.), `misconceptionTag: "bio.nerv.sensitif-et-moteur-confondus"` (libellé exact : faire
  porter l'ordre moteur par les fibres sensitives) ;
- d → « قطعُ العصب أفقد عضلات السّاق اليمنى قدرتها على التّقلّص، فلم تستجب للأمر » (72 car.), muette
  (faux : la coupure ne paralyse pas le muscle, cf. cours 02, tableau et ::: verifie « العضلة
  والنّاقل الحركيّ سليمان ») ;
- explication, remplacer les deux derniers pièges par : « الخطأ الشّائع: جعل الألياف الحسّيّة ناقلة
  للأمر الحركيّ، وهي تنقل السّيالة نحو النّخاع لا منه ؛ أو الظنّ أنّ النّخاع يستثني السّاق التي قُطع
  عصبها، وهو لا يعلم بالقطع لأنّ القطع يقع بعده في طريق الأمر ؛ أو الظنّ أنّ القطع شلّ عضلات السّاق،
  والعضلة لا تفقد قدرتها على التّقلّص بقطع عصبها: ما ينقصها هو الأمر الذي لم يبلغها. »

**[MAJEUR] Q5 ↔ Q6 — doublon de fait (et fuite mutuelle dans le donjon).** Les bonnes options d et e
de Q6 (« يحتوي على ألياف تنقل السّيالة الحسّيّة من الجلد نحو النّخاع الشّوكيّ » / « … الحركيّة من النّخاع
الشّوكيّ نحو العضلات ») sont la clé b de Q5 coupée en deux, presque mot pour mot ; « حركيّة فقط » est
posé dans les deux ; l'explication de Q6 énonce la clé de Q5 et réciproquement (tirage aléatoire du
donjon). De plus a (« مزدوج: ألياف حسّيّة وألياف حركيّة ») ⟺ d ∧ e : le multi se réduit à « c est-il
faux ? », et le triplet « مزدوج / حسّيّة فقط / حركيّة فقط » rend la clé « les deux » que l'auteur voulait
éviter. Correctif (garde 6 questions et la sous-question « طبيعة أليافه ») : Q6 devient un `mcq`
qui porte la seule idée neuve, « chaque bout contient les deux sortes de fibres » :
- a (clé) « عصب مزدوج: في كلّ من طرفيه المقطوعين ألياف حسّيّة وألياف حركيّة » (63 car.) ;
- b « ألياف حسّيّة فقط، لأنّ تنبيه الطّرف المركزيّ أحدث انثناء » (56) ;
- c « ألياف طرفه المركزيّ حسّيّة كلّها، وألياف طرفه المحيطيّ حركيّة كلّها » (67 — la plus longue n'est
  pas la clé ; a et c sont les deux options « les deux sortes », b et d les deux « فقط » : la forme
  ne départage plus) ;
- d « ألياف حركيّة فقط، لأنّ تنبيه الطّرف المحيطيّ أحدث انثناء » (56) ; `correctOption: "a"` ;
- explication : « تنبيه الطّرف المحيطيّ أحدث انثناء السّاق اليمنى: في العصب ألياف حركيّة. وتنبيه
  الطّرف المركزيّ أحدث انثناء الأطراف الأخرى بعد مرور الرّسالة بالنّخاع: في العصب ألياف حسّيّة. فهو
  عصب مزدوج، وأليافه تمتدّ من النّخاع الشّوكيّ إلى السّاق، فيقطع القطعُ كلّ ليف إلى جزأين: في كلّ
  طرف من الطّرفين ألياف من النّوعين. الخطأ الشّائع: قراءة كلّ تجربة على أنّها تكشف طبيعة نصف العصب ؛
  أو القول «حسّيّة فقط» وهو يتجاهل نتيجة تنبيه الطّرف المحيطيّ، أو «حركيّة فقط» وهو يتجاهل نتيجة
  تنبيه الطّرف المركزيّ. »
  Variante acceptable : fondre Q5 et Q6 en une seule question (mission à 5 questions).
  Recouvrement résiduel (« sensitif + moteur ») inhérent à la sous-question officielle : accepté.

**[MINEUR] Q1–Q3 → Q5 (fuite en avant structurelle).** Les explications de Q1 (« سيالة حسّيّة جاذبة
يحملها عصب النّسا نحو النّخاع الشّوكيّ ») et de Q2 (« ينبّه الألياف الحركيّة … سيالة نابذة نحو عضلات
السّاق ») énoncent ensemble la clé de Q5 avant qu'elle ne soit posée (route quête : Q1, Q2 en d2
passent devant). C'est la dépendance « interpréter puis conclure » du sujet officiel lui-même ; aucun
correctif exigé, mais elle s'ajoute au doublon Q5/Q6 : raison de plus pour n'avoir qu'UNE question
de conclusion « sensitif + moteur ».

**[MINEUR] Q2 a — faute d'arabe.** « بلغت السّيالة المولَّدة النّخاع الشّوكيّ، فأصدر منه أمرًا بانثناء
السّاق » (sujet de « أصدر » introuvable : la moelle ne peut être à la fois sujet et « منه »). Remplacer
par « بلغت السّيالة المولَّدة النّخاع الشّوكيّ، فأصدر أمرًا بانثناء السّاق ».

**[MINEUR] Figure — pattes postérieures fléchies en « Z ».** Le Doc 6 montre les pattes postérieures
allongées vers le bas ; la figure les dessine pliées au genou, alors que Q4 parle d'une jambe qui
« reste allongée » (« بقاء السّاق اليمنى ممدودة ») et que Q2 décrit sa flexion. Redessiner les deux
pattes postérieures allongées vers le bas, comme dans le Doc 6, en gardant la coupure sur la cuisse
droite du dessin, les repères C (bout proximal) et P (bout distal) et l'aiguille de Q1 sur le pied
droit — puis re-rendre les quatre figures (direction de correction, pas de tracé fourni).

Étiquettes : Q1 d `bio.nerv.cerveau-dans-l-arc-reflexe` exacte ; Q2 c, Q3 c `bio.nerv.sensitif-et-
moteur-confondus` exactes ; Q3 d `cerveau-dans-l-arc-reflexe` exacte (une grenouille « نخاعيّة » est
sans cerveau : distracteur de connaissance, pas d'élimination à vue faute de définition dans l'énoncé de
Q3 — acceptable) ; Q5 a `sensitif-et-moteur-confondus` exacte (sens des deux messages inversé).
Muettes justifiées : Q1 a, c ; Q2 a, b ; Q3 b ; Q4 b ; Q5 c, d.
Notation/rendu : aucune chaîne isolée par `isolateLtrRuns` (seules les lettres P, C), aucun chiffre
arabo-indien, aucune lettre d'option dans les explications, aucune clé strictement la plus longue.

---

## 02/08 — `02-al-af3al-al-in3ikasiya/exercices/08-examen-2021-ex4-hypotheses-stimulations-coupes-moelle-epiniere.json`

En-tête : « 🏛️ مناظرة 2021 · التمرين 4 ⭐⭐⭐⭐: فرضيّات وتجارب ومقطعا نخاع شوكيّ عند ضفدعتين », d4
challenge 300/60, displayOrder 8 — conforme. Rampe 2,2,3,3,3,3. Étage d4 : défendable (problème
principal de la 2ᵉ partie, chaîne hypothèses → test → preuve microscopique), mais au plancher : même
rampe que 02/07 classée d3, et les défis publiés du chapitre sont tout en d3 ; il ne tient que si Q6
exige vraiment la figure (voir défaut ci-dessous — corrigé, il le justifie).

| Q | type | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | mcq d2 | d | d | OK | trois étiquettes exactes |
| 2 | multi d2 | {a,c,d,f} | {a,c,d,f} | OK (mineur) | e « بصرها » est du remplissage |
| 3 | mcq d3 | c | c | RÉSERVE (majeur) | quasi-doublon de 02/07 Q2 (même figure, mêmes pièges) |
| 4 | mcq d3 | a | a | OK (mineur) | b mérite `cause-sans-temoin` ; l'énoncé livre la clé de Q2 |
| 5 | multi d3 | {a,d,f} | {a,d,f} | OK (mineur) | figure fidèle sauf densité des fibres de Y (zone 1) |
| 6 | mcq d3 | b | b | RÉSERVE (majeur) | a et c contredits par l'énoncé ; la figure n'est pas nécessaire |

Fidélité au sujet 2021 ex.4 : données exactes (exp. 1 « عدّة مرّات … بنفس الطّريقة », exp. 2
bout périphérique → flexion, Doc 7 X = (أ), Y = (ب)). 1a → Q1, 1b → Q2, 2a → Q3, 2b → Q4, 3a → Q5,
3b → Q6 : rien de perdu. Le Doc 5 remplacé par le texte : acceptable (il ne porte aucune donnée
de plus). Notions données : zone 1 = substance grise, zone 2 = substance blanche dans Q5 ET Q6 ;
bout périphérique « أي طرفه المتّصل بالسّاق » (Q3), « طرفه المحيطيّ المتّصل بالسّاق » (Q4),
« لطرف عصب النّسا المقطوع المتّصل بالسّاق » (Q6) : OK.

**Point (2) de l'auteur — confirmé.** L'exp. 2 ne teste que le conducteur moteur EN AVAL de la
coupure ; « conducteur moteur et muscle innocentés » est la logique du sujet officiel ET du cours 02
(tableau « تنبيه طرف العصب المتّصل بالسّاق → النّاقل الحركيّ سليم », ::: verifie « العضلة والنّاقل
الحركيّ سليمان ») : la mission ne doit pas s'en écarter ; aucune option ne propose le segment moteur
proximal, et l'explication de Q4 dit littéralement « ولا يختبر إلّا ما بعده ». « ألياف المادة البيضاء » :
juste — les petits éléments serrés de la zone 2 du Doc 7 (anneau + point central) sont la coupe
transversale des fibres myélinisées, et le cours 01 définit la substance blanche par ses fibres.

Figures. Q3 : la grenouille de 02/07 Q2, OCTET POUR OCTET (seul `<title>` change). Q5 = Q6 (même
SVG) : X à gauche, Y à droite (le PDF met X à droite — sans conséquence, les lettres sont dessinées) ;
zone 1 grise / zone 2 blanche séparées en pointillé, repères ① ② ; X : 4 étoiles + 1 polygone = 5
grandes cellules (PDF : 5) ; Y : 1 étoile plus petite (PDF : 1) ; zone 2 : X dense, Y clairsemée
avec traits courts et points (PDF : idem). viewBox 0 0 340 214, rien ne déborde, textes X, Y, 1, 2
seulement, aucun élément interdit, aucune clé dessinée.

### Défauts

**[MAJEUR] Q3 ↔ 02/07 Q2 — quasi-doublon dans le même chapitre.** Même expérience (stimulation du
bout périphérique P du sciatique coupé), même figure (SVG identique hors `<title>`), même idée-clé
(message moteur jusqu'au muscle sans passer par le centre), deux pièges sur trois identiques
(« le message atteint le centre » — a dans les deux ; « fibres sensitives jusqu'au muscle » — 02/07 c,
02/08 d), explications qui réfutent les mêmes erreurs. Les deux annales recyclent la même donnée,
mais ici la question elle-même est la même (critère du lot : mêmes options, mêmes pièges, mêmes
explications). Correctif : supprimer 02/08 Q3 (mission à 5 questions, rampe 2,2,3,3,3) — son
contenu (« تنبيه الطّرف المحيطيّ يتجاوز المستقبلات والنّاقل الحسّيّ والمركز ») est déjà la
justification de la clé de Q4 et de son explication. (Réécrire Q3 sous l'angle « ce que prouve la
flexion » en ferait le miroir de Q4 : « éléments innocentés » / « hypothèses retenues » — à éviter.)

**[MAJEUR] Q6 — deux distracteurs éliminés par l'énoncé, la figure devient inutile.** L'énoncé
redonne le résultat de l'exp. 2 (« لكنّها تثنيها عند التّنبيه المباشر لطرف عصب النّسا المقطوع
المتّصل بالسّاق ») : c « شُلّت عضلة السّاق، فلا تتقلّص مهما كان التّنبيه … » le nie mot pour mot, a
(conducteur moteur) est écarté par le même résultat ; d (cerveau) tombe par le cours. La clé sort
par élimination SANS regarder X et Y — or la sous-question 3b porte justement sur le Doc 7. Les
deux hypothèses que l'exp. 2 laisse debout (récepteurs, conducteur sensitif) ne sont pas proposées.
Correctif (vérifié : clé b = 74 car., pas la plus longue ; chaque distracteur reste faux comme réponse
à la question posée, aucun ne nie une prémisse) :
- fin de l'énoncé → « ما التّفسير الأرجح، بالاعتماد على مقارنة الرّسمين X وY، لعدم انثناء ساق
  الضّفدعة (ب) عند تنبيه جلدها؟ » ;
- a → « تضرّرت المستقبلات الحسّيّة بجلد السّاق، فلا تتولّد سيالة حسّيّة عند تنبيهه » (74 car.),
  `bio.demarche.cause-sans-temoin` ;
- c → « تضرّرت الألياف الحسّيّة لعصب النّسا، فلا تبلغ الرّسالة الحسّيّة النّخاع الشّوكيّ » (80 car.),
  `bio.demarche.cause-sans-temoin` (ici le libellé est exact : accuser un élément qu'aucune
  comparaison ne désigne, alors que la comparaison témoin X / Y désigne la moelle) ;
- b (clé) et d (`cerveau-dans-l-arc-reflexe`) inchangés ;
- explication → « تنبيه الطّرف المحيطيّ يُحدث الانثناء، فالنّاقل الحركيّ والعضلة سليمان والعطب في
  موضع آخر من القوس. والمقارنة بين الرّسمين هي التي تسمّيه: يبيّن الرّسم Y، بمقارنته بالرّسم X،
  أنّ النّخاع الشّوكيّ للضّفدعة التي دهستها الدّرّاجة متضرّر، وهو المركز العصبيّ الذي يتلقّى الرّسالة
  الحسّيّة ويولّد منها الأمر الحركيّ ؛ فلا أمر يصدر وتبقى السّاق ممدودة. الخطأ الشّائع: اتّهام
  المستقبلات أو الألياف الحسّيّة لعصب النّسا، والمقطعان لا يدلّان على تلفها بل على تلف النّخاع ؛ أو
  إدخال الدّماغ، وهو ليس من عناصر القوس الانعكاسيّ النّخاعيّ. »
  (Explication volontairement sans les comptes « 5 contre 1 » : ils livreraient la clé de Q5 dans le
  donjon.) Au passage, l'étiquette actuelle `cause-sans-temoin` de a et c est inexacte : l'erreur
  exécutée y est de garder une hypothèse que le résultat redonné dans l'énoncé vient d'écarter.

**[MINEUR] Q2 e — remplissage.** « تضرّر بصرها فلم ترَ مصدر التّنبيه » ne tente personne après le
chapitre. Remplacer par « امتنعت الضّفدعة (ب) بإرادتها عن ثني ساقها » (41 car. ; faux : le réflexe
est involontaire, cours 01/02 ; erreur du registre `reflexe-pris-pour-volontaire`, non étiquetable
en multi). Explication : remplacer « وأمّا البصر فلا علاقة له بحركة تنتج عن تنبيه كهربائيّ للجلد »
par « وأمّا الإرادة فلا دخل لها في فعل انعكاسيّ، وهو يحدث دون قرار ».

**[MINEUR] Q4 b — option muette qui mérite une étiquette existante.** « تلف المركز العصبيّ وحده،
لأنّ التّجربة استبعدت كلّ ما عداه » = désigner une cause sans comparaison qui la distingue (l'exp. 2 ne
sépare pas le centre des récepteurs ni du conducteur sensitif) ; l'explication la nomme déjà
(« حصر العطب في المركز دون سند ») — porte R1 : ajouter `bio.demarche.cause-sans-temoin`. (d reste
muette : deux lectures possibles, inversion sensitif/moteur ou maintien de ce qui est innocenté.)

**[MINEUR] Q4 → Q2 (donjon).** L'énoncé de Q4 liste les cinq hypothèses ; dans un tirage où Q4
précède Q2, il livre la clé de Q2 (les quatre éléments de l'arc proposés, ni cerveau ni vue).
Dépendance inhérente à l'enchaînement officiel 1b → 2b ; ordre quête correct (Q2 d2 avant Q4 d3).
Aucun correctif exigé.

**[MINEUR] Figure Q5/Q6 — fidélité de la zone 1 de Y.** Le PDF montre la substance grise de Y
remplie de fibres ondulées (plus que dans X) ; la figure en met 4. Aucune clé n'en dépend ; à
aligner sur le PDF (une quinzaine de traits ondulés fins dans la zone 1 de Y).

Étiquettes : Q1 a `reflexe-pris-pour-volontaire`, b `inne-pris-pour-acquis`, c `vitesse-comme-
critere` — exactes ; Q3 b `cerveau-dans-l-arc-reflexe`, d `sensitif-et-moteur-confondus` — exactes ;
Q6 d `cerveau-dans-l-arc-reflexe` exacte ; Q6 a, c : voir ci-dessus. Rendu : chaînes X, Y, P, 1, 2
non isolées, ordre affiché conforme dans Chromium `dir=rtl` (Q5 énoncé et explication, Q6 énoncé,
Q5 f rendus).

---

## 05/07 — `05-al-hadm/exercices/07-examen-2021-ex2-appareil-digestif-sucs-digestifs-villosite.json`

En-tête : « 🏛️ مناظرة 2021 · التمرين 2 ⭐⭐: أعضاء الجهاز الهضميّ وعصاراتها والبنية المجهريّة لجدار
المعي الدّقيق », d2 practice 75/15, displayOrder 7 — conforme ; le sujet ne nomme pas la villosité
(clé de Q4) : bien. Rampe 1,1,2,2,2. Étage d2 honnête (identification et rappel, une seule
combinaison en Q3).

| Q | type | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | matching d1 | 1-المعدة, 2-المعثكلة, 3-المرارة, 4-المعي الدّقيق | idem | OK | vésicule définie dans l'énoncé |
| 2 | mcq d1 | b | b | OK | étiquette d exacte |
| 3 | mcq d2 | a | a | OK | vrai plan 2×2 lieu × rôle ; étiquette c exacte |
| 4 | mcq d2 | c | c | RÉSERVE (majeur) | le vote terme à terme reconstruit la clé |
| 5 | multi d2 | {a,d,e} | {a,d,e} | RÉSERVE (majeur) | explication contraire au sujet officiel ; c s'élimine par « مجهريّة » |

Fidélité au sujet 2021 ex.2 : Doc 1 et Doc 2 comparés au PDF C05 p. 2. Doc 1 refait : foie non
numéroté, 1 = estomac (flèche dans la poche), 2 = pancréas (flèche à son extrémité effilée),
3 = vésicule biliaire (petite poche au foie ; dans le PDF elle est dessinée DANS le contour du foie,
ici à son bord — sans conséquence), 4 = intestin grêle (tube du bas) : conforme. Doc 2 refait :
villosité en doigt de gant, un seul rang de cellules à noyau, bordure en brosse, vaisseau rouge à
gauche, bleu à droite, réseau capillaire, chylifère jaune axial fourchu : conforme (les deux
encoches « cellules caliciformes » du PDF sont omises — sans conséquence). viewBox 0 0 300 340 et
0 0 260 310, textes 1–4 seulement, aucun élément interdit ; l'œsophage et l'intestin sortent du
cadre comme dans le PDF. Découpage 1a → Q1, 1b → Q2 (estomac) + Q3 (bile), 2a+2b → Q4, 2c → Q5 :
rien de perdu. La vésicule est définie dans les deux énoncés qui l'emploient (Q1, Q3).
« besides digestion » (2b) non repris : acceptable — à condition de ne pas affirmer le contraire
(voir Q5).

### Défauts

**[MAJEUR] Q4 — le vote terme à terme donne la clé.** « الخملة المعويّة » figure dans b et c,
« امتصاص المغذّيات الخلويّة » dans a et c : l'intersection est c, sans rien savoir. Correctif : plan
2×2 nom {خملة، خميلة} × fonction {امتصاص، استحلاب} — garder a, b, c et remplacer
d → « الخميلة: استحلاب الدّهنيّات إلى قطيرات » (38 car., double erreur, muette). Après correctif
chaque terme figure deux fois, la clé (42) n'est pas la plus longue (b = 46). Explication : remplacer
la phrase des pièges par « الخطأ الشّائع: الخلط بين الخملة والخميلة، وهي أصغر منها بكثير وتوجد على
حافّة كلّ خليّة ماصّة ؛ أو إسناد دور الصّفراء، وهو الاستحلاب، إلى جدار المعي. » (l'actuelle
« إسناد … دور التّفتيت الميكانيكيّ إلى جدار المعي » est en outre inexacte : le cours attribue au
mur de l'intestin le brassage par sa couche musculaire).

**[MAJEUR] Q5 — explication contraire au sujet officiel.** « والخملة لا تفرز أنزيمات هاضمة، فالهضم
تتمّه العصارات قبل الامتصاص » : le sujet 2021 (2b) pose au contraire « بالإضافة إلى دورها في وظيفة
الهضم تؤدّي هذه البنية وظيفة أخرى », et les cellules des villosités portent bien des enzymes
digestives. Omettre l'incise du sujet est acceptable, enseigner le contraire ne l'est pas. Le
distracteur f reste faux pour une autre raison (on ne « découpe » pas des nutriments, produits finaux).
Correctif : remplacer la phrase par « والمغذّيات الخلويّة نواتج نهائيّة للهضم، فهي تعبر الجدار كما
هي ولا تُفكَّك أثناء عبورها. »

**[MINEUR] Q5 c — distracteur éliminé par l'énoncé.** « طولها من 7 إلى 8 أمتار » contredit
« بنية مجهريّة » de l'énoncé. Remplacer par « كلّ المغذّيات تعبرها إلى الدّم، ولا وعاء لمفاويّ فيها »
(53 car. ; faux : chylifère axial jaune sur la figure, lipides surtout vers la lymphe — cours 05 ;
erreur du registre `graisses-par-le-sang`, non étiquetable en multi), et dans l'explication
remplacer « والطّول من 7 إلى 8 أمتار طول المعي الدّقيق كلّه لا طول هذه البنية المجهريّة » par « وفيها،
إلى جانب الشّعيرات الدّمويّة، وعاء لمفاويّ مركزيّ تسلكه الدّهنيّات أساسًا، فلا تعبر المغذّيات كلّها
إلى الدّم ».

**[MINEUR] Q5 → Q4 (donjon).** L'explication de Q5 (« وهي الخملة المعويّة، هي الامتصاص ») livre la
clé de Q4 si Q5 sort avant ; ordre quête correct. Inhérent (Q5 suppose la fonction connue) : aucun
correctif exigé.

Étiquettes : Q2 d `bio.dig.specificite-enzyme-ignoree` exacte ; Q3 c `bio.dig.bile-avec-enzymes`
exacte ; Q3 b (deux erreurs) muette à bon droit ; Q3 d muette (pas d'entrée « lieu de stockage »).
Q2 a et c (suc juste d'un AUTRE organe) : `bio.lecture.valeur-d-une-autre-grandeur` serait
plausible (« autre élément »), mais l'explication nomme une erreur de connaissance (« نسبة عصارة إلى
غير العضو الذي يفرزها ») : deux lectures, muettes acceptées. Rendu : seuls des chiffres isolés
(1–4, « من 7 إلى 8 ») — ordre correct, aucune isolation nécessaire.

---

## 05/08 — `05-al-hadm/exercices/08-examen-2022-ex4-digestion-huile-olive-maltose-devenir-du-glucose.json`

En-tête : « 🏛️ مناظرة 2022 · التمرين 4 ⭐⭐⭐⭐: هضم سكّر الشّعير وزيت الزّيتون ومصير المغذّيات في
المعي الدّقيق », d4 challenge 300/60, displayOrder 8 — conforme. Rampe 2,2,2,3,3,3,3,3,3. Étage d4 :
justifié (problème de 8 points, deux expériences, synthèse en Q8–Q9). Difficultés : Q5 (nommer (س)
parmi quatre liquides) et Q6 (lecture d'un histogramme dont les valeurs sont imprimées) sont des d2
de fond portés en d3 ; pour Q5 c'est le prix de l'ordre (en d2 elle passerait devant Q4 et
livrerait « الصّفراء ») — acceptable, à ne pas multiplier.

| Q | type | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | multi d2 | {a,c,f} | {a,c,f} | OK (mineur) | trois paires « une seule juste » : le compte se déduit |
| 2 | mcq d2 | d | d | RÉSERVE (majeur) | explication : « المعثكليّة … نوعيّة للنّشا وللبروتيدات » contredit Q3, Q8, Q9 |
| 3 | mcq d2 | d | d | OK | étiquettes a, c exactes |
| 4 | mcq d3 | c | c | RÉSERVE (majeur) | a et d contredisent l'énoncé |
| 5 | mcq d3 | b | b | OK | (س) ≠ sucs ajoutés : donné |
| 6 | multi d3 | {a,c,e,f} | {a,c,e,f} | RÉSERVE (majeur) | f et l'explication livrent la clé de Q7 ; graduations brouillées en RTL |
| 7 | mcq d3 | c | c | OK (mineur) | tableau Markdown non rendu |
| 8 | matching d3 | كبد→r2, معثكلة→r4, معي→r1, معدة→r3 | idem | OK | bijection unique |
| 9 | ordering d3 | c,e,b,a,d | c,e,b,a,d | OK | une seule suite |

Calculs refaits par script : 80 + 20 = 50 + 50 = 10 + 90 = 100 ; hauteurs des barres
(1,66 px par %) : 80 → 132,8 ; 20 → 33,2 ; 50 → 83 ; 10 → 16,6 ; 90 → 149,4 — exactes.
Fidélité au sujet 2022 ex.4 (PDF C04 p. 3–4) : contenus des tubes, 37 °C, 30 min, résultats
(tube 1 : glucose, huile, AG + « كحول دهنيّة » ; tube 2 : sans huile), histogramme 80/20, 50/50,
10/90 : exacts. « غليسيرول » pour « كحول دهنيّة » : acceptable (vocabulaire du cours). Doc 3 (dessin
des tubes) remplacé par tableau/énoncés : acceptable, il ne porte rien d'autre. Valeurs imprimées
sur l'histogramme (le PDF n'en imprime pas) : acceptable dans l'app (Q7 redonne de toute façon les
valeurs), mais Q6 n'exerce plus la lecture d'échelle. Découpage 1 → Q1, 2a–d → Q2–Q5, 3a → Q6,
3b → Q7, 4 → Q8 + Q9 : rien de perdu. (س) « ليس إحدى هاتين العصارتين » donné en Q5 : OK (Q4 n'en a
pas besoin, son option b le règle).

**Point (3) de l'auteur — `bile-avec-enzymes` sur Q4 b : acceptable.** Le libellé n'est montré
qu'à la correction de fin de mission (`QuestReviewList`, arena `origin/main`), où Q5 a déjà nommé
(س) ; l'erreur exécutée — prêter à (س) des enzymes que les sucs n'auraient pas — est bien celle du
libellé. Aucune fuite pendant le jeu.

### Défauts

**[MAJEUR] Q2 — explication fausse et contraire à la mission.** « أمّا أنزيمات العصارة المعثكليّة
فنوعيّة للنّشا وللبروتيدات » dit, à la lettre, que le suc pancréatique ne touche pas aux lipides ;
or Q3 (« بتيسير من أنزيمات العصارتين »), Q8 (r4 « إفراز عصارة تفكّك أنزيماتها الزّيت » ↔ المعثكلة)
et Q9 e reposent sur ses enzymes lipolytiques. Correctif : remplacer la phrase par « أمّا العصارة
المعثكليّة فأنزيمها الذي يعمل على السّكّريات يفكّك النّشا إلى سكّر الشّعير، ولا يفكّك سكّر الشّعير. »
(conforme au cours 05 : « سكّر الشّعير ← جليكوز بمفعول العصارة المعويّة »).

**[MAJEUR] Q4 — deux distracteurs contredisent l'énoncé.** a « … ما بقي من زيت الزّيتون في الأنبوب
الأوّل » : (س) n'a été ajouté qu'au second tube (« أُضيف إلى الثّاني وحده ») ; d « يرفع حرارة الأنبوب
الثّاني » : les deux tubes sont dans le même bain à 37 °C (l'explication le dit). Reste b/c.
Correctif (vérifié : clé c = 60 car., a = 60 et d = 66 — la clé n'est pas la plus longue ;
aucun ne nie de prémisse ; tous deux faux — le tube 1 contient déjà de l'eau et a déjà digéré tout
le maltose) :
- a → « يضيف ماءً إلى الأنبوب الثّاني، فيتمّ بفضله تفكيك الزّيت كلّه » (étiquette : voir
  « étiquettes manquantes », `bio.dig.eau-sans-enzyme` proposée) ;
- d → « يفكّك سكّر الشّعير بدل العصارتين، فتتفرّغ أنزيماتهما لتفكيك الزّيت » (muette : deux erreurs,
  enzymes dans (س) + non-spécificité) ;
- explication : remplacer « أو الظنّ أنّه يزيد الماء أو الحرارة، والأنبوبان في الحمّام نفسه عند
  الحرارة نفسها » par « أو الظنّ أنّه يزيد الماء، والمحلول مائيّ أصلًا ؛ أو أنّه يتولّى تفكيك سكّر
  الشّعير فيُفرغ الأنزيمات للزّيت، والحال أنّ الأنبوب الأوّل فكّك سكّر الشّعير كلّه دون (س)، وأنّ
  أنزيم سكّر الشّعير لا يعمل على الزّيت. »

**[MAJEUR] Q6 → Q7 — fuite en avant.** L'option juste f (« ما ينقص من نسبة الجليكوز في المعي الدّقيق
يظهر في الوريد … ») et l'explication (« فما ينقص من أحد المكانين يظهر في الآخر، ولا يضيع منه شيء »)
énoncent le devenir du glucose — clé de Q7 (passage intestin → sang), qui la suit (même d3, ordre
de fichier). L'analyse (3a) ne doit pas faire la déduction (3b). Correctif : f → « مجموع النّسبتين
يساوي 100 في كلّ مرّة » (37 car., vrai : 80 + 20, 50 + 50, 10 + 90) ; dans l'explication, remplacer
« والأهمّ أنّ مجموعهما ثابت: … = 100 ؛ فما ينقص من أحد المكانين يظهر في الآخر، ولا يضيع منه شيء. »
par « ومجموعهما يساوي 100 في كلّ مرّة: 80 + 20 = 100 ، و50 + 50 = 100 ، و10 + 90 = 100. », et
« أو الاكتفاء بوصف كلّ سلسلة على حدة دون ربط النقص بالزيادة » par « أو وصف سلسلة واحدة وإهمال
الأخرى » (rendu Chromium vérifié).

**[MAJEUR] Q6 — figure : graduations traversées par l'axe dans le lecteur.** Les sept `<text>`
de l'axe vertical (0…100 et « % ») sont en `text-anchor="end"` à x = 38. Le lecteur d'exercice
pose `dir="rtl"` sur toute la page d'une matière arabe (`exercise-player.tsx`, `PageShell
dir={isRtlSubject ? "rtl" : undefined}`) : le SVG hérite de `direction: rtl`, « end » devient le
bord gauche, et les nombres débordent à droite sur l'axe (rendu Chromium : « 1|00 », « 8|0 »… ;
en LTR ils sont justes). Correctif vérifié dans les deux sens : `x="28"` et `text-anchor="middle"`
pour ces sept textes (0, 20, 40, 60, 80, 100 et « % »).

**[MINEUR] Q1 — nombre de bonnes réponses déductible.** Trois paires (huile a/b, glucose c/d,
AG-glycérol e/f) avec une seule écriture juste par paire : le compte (3) se lit sur la forme.
Correctif : d → « سكّر الشّعير لا يظهر في نتائج أيّ من الأنبوبين » (vrai : aucun des deux résultats
ne le porte) ; clé {a, c, d, f} ; explication : ajouter « ولا يبقى سكّر الشّعير في أيّ من الأنبوبين،
فقد تفكّك كلّه. ».

**[MINEUR] Q1 et Q7 — tableaux Markdown dans un énoncé.** `RichField` ne rend pas les tableaux :
les lignes « | … | » s'affichent brutes et « | --- | --- | --- | » passe en bloc d'équation centré
(`isDisplayEquation` → vrai) ; l'ordre des valeurs reste juste (vérifié), mais c'est illisible sur
téléphone et hors usage du corpus (une seule occurrence publiée ; les missions d'examen de maths
écrivent une ligne par rangée). Correctifs (rendus dans Chromium, ordre de lecture juste) :
- Q7 : « بعد أن تناول شخص محلولًا من الجليكوز، قيست نسبة الجليكوز المئويّة في المعي الدّقيق وفي
  الوريد المتّصل به بعد 1 ثمّ 3 ثمّ 5 ساعات:\nفي المعي الدّقيق: 80 ، 50 ، 10\nفي الوريد المتّصل به:
  20 ، 50 ، 90\nما مصير الجليكوز، وما الظّاهرة التي حدثت في مستوى المعي الدّقيق؟ » ;
- Q1 : « وُضع الأنبوبان 1 و2 في حمّام ماريّ عند 37 درجة لدراسة مصير سكّر الشّعير وزيت الزّيتون في
  المعي الدّقيق:\nالأنبوب 1: سكّر الشّعير + زيت الزّيتون + العصارة المعثكليّة + العصارة المعويّة\n
  الأنبوب 2: محتوى الأنبوب 1 نفسه + قطرات من سائل (س)\nالنّتائج بعد 30 دقيقة:\nفي الأنبوب 1: جليكوز ،
  زيت الزّيتون ، أحماض دهنيّة وغليسيرول\nفي الأنبوب 2: جليكوز ، أحماض دهنيّة وغليسيرول\nأيّ المقارنات
  التّالية بين نتائج الأنبوبين صحيحة؟ ».

**[MINEUR] Notion non enseignée.** « les sucs pancréatique et intestinal digèrent les lipides » n'est
dans aucun cours (le cours 05 ne nomme que l'amylase et la trypsine « منها ») ; Q3 et Q4 le donnent
par les données (acides gras dans le tube sans (س)), Q9 e l'écrit, Q8 se résout par élimination.
Acceptable dans la mission ; à signaler au cours 05 (une ligne sur l'action des sucs sur les
lipides), hors périmètre.

**[MINEUR] Options muettes qui méritent une étiquette existante (porte R1, l'explication nomme
l'erreur).** Q5 a (« العصارة المعديّة ») et c (« اللّعاب ») → `bio.dig.specificite-enzyme-ignoree`
(« دون النّظر إلى المادّة التي تعمل عليها ») ; Q7 b (« … ظاهرة الهضم ») → `bio.dig.absorption-dans-
la-digestion` (« وهي مرحلة تالية للهضم لا جزء منه »).

Étiquettes posées : Q2 a `bio.demarche.cause-sans-temoin` (la chaleur accusée sans tube témoin —
exacte), b `bio.dig.specificite-enzyme-ignoree` (exacte), c `bio.dig.enzyme-agit-seule` (exacte) ;
Q3 a `bio.dig.unites-structurales-confondues`, c `enzyme-agit-seule` (exactes) ; Q4 b : voir
point (3). Q3 b, Q4 a (corrigée) et Q5 d (« l'eau seule digère ») : étiquette nouvelle proposée
ci-dessous (`bio.dig.eau-sans-enzyme`). Rendu : les chaînes de calcul de l'explication de Q6
s'affichent dans l'ordre source.

---

## 07/07 — `07-ad-dawaran/exercices/07-examen-2024-ex1-digestion-proteides-milieu-interieur-nerfs-craniens-villosite.json`

En-tête : « 🏛️ مناظرة 2024 · التمرين 1 ⭐⭐: هضم البروتيدات والوسط الدّاخليّ والأعصاب القحفيّة
والخملات المعويّة », d2 practice 75/15, displayOrder 7 — conforme. Rampe 2,2,2,3. Étage d2 honnête
(trois rappels, une combinaison en Q4). Quatre questions : c'est le QCM officiel entier (plancher
anti-rush 16 s) — acceptable. Placement en 07 : juste (Q2 et Q4 exigent le cours 07, Q3 le 01,
Q1 le 05 — tous antérieurs ou égaux dans le manifeste).

| Q | type | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | mcq d2 | d | d | OK | vrai 2×2 bouche × intestin ; étiquette c exacte |
| 2 | mcq d2 | b | b | OK | 9 % + 21 % = 30 % ; étiquettes c, d exactes |
| 3 | mcq d2 | c | c | OK | étiquette d exacte |
| 4 | mcq d3 | a | a | OK | vrai 2×2 sens × vaisseau ; شُرين/وُريد définis |

Fidélité au sujet 2024 ex.1 (PDF C03 p. 1) : énoncés et options conformes à la transcription, aux
adaptations déclarées près, que j'approuve toutes : Q1 — l'option officielle ج était la seule sans
« الفم » (clé lisible sur la forme) ; le remplacement par « المعدة وحدها » donne un vrai plan 2×2
(bouche oui/non × intestin oui/non, estomac partout) : vote nul. Q2 — « فقط، دون اللّمف » rend a
fausse sans ambiguïté (l'officielle « الدّم والسّائل الخلالي » était à moitié vraie) ; 70 % = secteur
cellulaire, 21 % = secteur interstitiel, 9 + 21 = 30 (recalculé) ; la coche ✓ suit 30, qui n'est
aucune option. Q4 — l'officielle « شعيرات دمويّة مرتبطة بشُرين » était vraie à la lettre (les
capillaires sont reliés aux deux) : le couple « يغادرها الدّم عبر وُريد / شُرين » × sens du passage
forme un 2×2 où chaque terme est vrai une fois sur deux ; titre et énoncé sans « امتصاص » : bien.
« البروتيدات » pour « البروتينات » : vocabulaire du cours.

Doublons : Q2 redemande le fait de la mission publiée `07-ad-dawaran/exercices/04-defi.json` Q1
(« ممّ يتكوّن الوسط الدّاخليّ؟ », même clé) mais avec les pièges officiels (pourcentages des
secteurs) qui n'y sont pas : pas quasi identique, accepté. Aucun autre recouvrement (publié ou
tranche).

Rendu : options c, d « قرابة 70 % » / « 21 % » natives, explication « (9 %) », « (21 %) » isolées par
le moteur — positions mesurées dans Chromium : ordre de lecture conforme dans les deux cas.

Aucun défaut.

---

## 07/08 — `07-ad-dawaran/exercices/08-examen-2020-ex3-coeur-phases-cycle-cardiaque-circulation.json`

En-tête : « 🏛️ مناظرة 2020 · التمرين 3 ⭐⭐⭐: القلب وأطوار الدّورة القلبيّة والدّورة الدّمويّة », d3
boss 120/30, displayOrder 8 — conforme. Rampe 1,2,2,2,3,3. Étage d3 : au plancher (quatre questions
d1–d2 sur six) ; il tient parce que Q2 (six paires) et Q4 (six stations) sont notées tout-ou-rien et
que Q5/Q6 portent les deux vrais pièges du sujet. Pas malhonnête, mais un d2 practice serait
défendable aussi.

| Q | type | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | matching d1 | 1-وريد رئويّ, 2-بطين أيسر, 3-أبهر, 4-سينيّة | idem | OK | figure : voir B |
| 2 | matching d2 | 1-صغرى, 2-كبرى, ش.رئويّ, أوردة رئويّة, أبهر, أجوفان | idem | OK | portée des accolades donnée |
| 3 | mcq d2 | d | d | OK | vrai 2×2 phase × état des valves |
| 4 | ordering d2 | b,f,d,e,a,c | idem | OK | une seule suite |
| 5 | mcq d3 | a | a | OK (figure à corriger) | B = systole auriculaire, confirmé sur le PDF |
| 6 | mcq d3 | c | c | OK | étiquette b exacte ; vote nul sur les vaisseaux pulmonaires |

**Point (1) de l'auteur — CONFIRMÉ sur le PDF C06 p. 2 (rendu à 400 dpi, oreillettes de A et B
juxtaposées).** Phase A : oreillettes larges et rondes à paroi mince, plancher des oreillettes
fermé, ventricules à paroi épaisse et cavité étroite, feuillets sigmoïdes ouverts (« Y » central,
crochets contre les parois) → systole ventriculaire. Phase B : les deux oreillettes sont plus
ÉTROITES et leurs parois externes nettement plus ÉPAISSES qu'en A, les feuillets auriculo-
ventriculaires pendent dans des ventricules larges à paroi plus mince, le zigzag ferme les
sigmoïdes → systole auriculaire. Une diastole générale montrerait des oreillettes relâchées
(larges, minces) : ce n'est pas le dessin. Q5 n'est pas à refaire ; son option-clé (« أضيق … وجدارهما
سميك ») décrit exactement le PDF.

Fidélité au sujet 2020 ex.3 : 1 → Q1 (repères : 1 = petit tube supérieur droit = veine
pulmonaire, 2 = cavité inférieure droite = ventricule gauche, 3 = vaisseau qui monte puis s'incurve
à droite = aorte, 4 = zigzag = valvules sigmoïdes — conformes au PDF), 2 → Q3 (A) + Q5 (B), 3a+3b →
Q2, 3c → Q4 + Q6 : rien de perdu. Doc 3 refait (Q2, Q4) : poumons en haut, cœur, « R » pour
« أذينة يمنى » sur la cavité supérieure gauche du dessin, muscle rouge, un seul vaisseau poumon droit
du dessin → oreillette gauche (veine pulmonaire, comme le dit l'explication de Q2), accolades 1
(poumons → cœur) et 2 (cœur → muscle) : conforme. Notions données dans chaque énoncé qui les
emploie : « مرسوم من الأمام » (Q1, Q3, Q5), convention des valves (Q3 — Q5 n'en a pas besoin,
ses options portent sur les oreillettes), portée des accolades (Q2), R (Q2, Q4), rouge/bleu (Q6) :
OK. SVG : viewBox présents, tous les `<text>` en `text-anchor="middle"` (pas de bascule RTL),
arabe dans `<title>` seulement, aucun élément interdit.

### Défauts

**[MAJEUR] Figure B (Q1, Q5) — valves auriculo-ventriculaires dessinées fermées.** Dans B,
chaque oreillette est un rectangle fermé et chaque ventricule commence par un trait horizontal
(« M25 122 H78 … », « M92 122 H142 … ») : oreillette et ventricule sont deux boîtes séparées par
deux traits et une bande de paroi. Selon la convention que pose Q3 (« يُرسم الصمّام المغلق خطًّا
يسدّ الممرّ »), B montre donc des valves auriculo-ventriculaires FERMÉES — contraire au PDF (passage
ouvert, feuillets pendants), à la physiologie de la systole auriculaire et à l'explication de Q5
(« وتنفتح الصمّامات الأذينيّة-البطينيّة في الطّورين معًا »). Les feuillets noirs pendants ne suffisent
pas : le passage reste barré. Correctif (rendu vérifié dans Chromium : passage ouvert, feuillets
pendants, oreillettes toujours plus étroites et plus épaisses que dans A) — dans le groupe
`translate(6,30)` de Q1 ET de Q5, remplacer les quatre éléments
`<rect x="36" y="92" width="42" height="26" rx="9" …/><rect x="92" y="92" width="42" height="26"
rx="9" …/><path d="M25 122 H78 V178 Q78 204 51.5 204 Q25 204 25 178 Z" …/><path d="M92 122 H142
V179.0 Q142 204 117.0 204 Q92 204 92 179.0 Z" …/>` par deux cavités continues :
`<path d="M45 92 H69 Q78 92 78 101 V178 Q78 204 51.5 204 Q25 204 25 178 V122 H36 V101 Q36 92 45 92 Z"
fill="#ffffff" stroke="#0f172a" stroke-width="1.7"/><path d="M101 92 H125 Q134 92 134 101 V122 H142
V179 Q142 204 117 204 Q92 204 92 179 V101 Q92 92 101 92 Z" fill="#ffffff" stroke="#0f172a"
stroke-width="1.7"/>` (feuillets, bourrelets et zigzag inchangés).

**[MINEUR] Figures A et B — pas de chambre de chasse.** Les gros vaisseaux s'arrêtent au bord
supérieur du bloc cardiaque, entre les oreillettes, sans communiquer avec les ventricules : en A,
les sigmoïdes « ouvertes » n'ouvrent sur rien. Le PDF fait descendre les racines artérielles entre
les oreillettes jusqu'aux ventricules. Aucune clé n'en dépend ; à reprendre en même temps que le
correctif ci-dessus (un canal blanc de chaque ventricule jusqu'à la base de son artère).

Étiquettes : Q6 b `bio.circ.artere-sang-oxygene` exacte (artères en rouge, veines en bleu). Muettes
à bon droit : Q3 a (deux erreurs), b (lecture des valves inversée — pas d'entrée), c ; Q5 b, c, d.
Vote : Q3 et Q5 sont de vrais plans 2×2 (vote nul) ; Q6 : aorte rouge et caves bleues à 3 contre 1,
mais vote nul sur les deux vaisseaux pulmonaires — le vote ne laisse que b et c, c'est-à-dire
exactement le piège visé. Rendu : lettres A, B, R et chiffres seuls, rien d'isolé.
Doublons : le parcours de Q4 recoupe le quiz publié du chapitre (Q6, parcours d'une hématie,
format QCM) et l'idée de Q6 recoupe `06-defi-concours` Q4 ; formats, options et pièges différents :
pas quasi identiques. Aucune question publiée ne fait lire une phase sur une figure.

---

## Transversal

### Gates (lancés en lecture seule depuis l'arbre du moteur, corpus déjà branché)

- `content:check` (`build.ts --check`, n'écrit rien) : 0 erreur ; `sciences-vie-terre` 21 chapitres,
  129 missions, 774 questions (les six missions comprises) ; registre : 853 étiquettes.
- `content:qa --subject sciences-vie-terre` : 0 erreur, 7 avertissements, AUCUN dans les six fichiers
  (lettres d'option dans des explications publiées de 02-manaa, 04-zalazil, 05-barakin ; un chapitre
  sans domaine).
- `content:tranche --chapters 02,05,07` : sur les 36 questions neuves, aucune clé strictement la
  plus longue (recompté par script, question par question) et aucune paire proche (les 5 paires
  ≥ 0,45 et les 64 % de clés longues signalés sont toutes dans le publié). Jaccard maison sur
  énoncé + options : 0,35 au plus entre questions de la tranche, 0,24 au plus contre le SVT publié.
  Ces mesures lexicales ne voient pas les deux doublons signalés (02/07 Q5↔Q6, 02/07 Q2↔02/08 Q3) :
  ils sont sémantiques (même figure, même idée-clé, mêmes pièges).
- Balayages : aucun chiffre arabo-indien, aucun LaTeX, aucun nombre à espace simple, aucune virgule
  arabe dans une notation, aucune lettre ni ordinal d'option dans les explications, aucune
  occurrence de « على الشكل التالي », tout renvoi à une figure accompagné de son SVG.

### Doublons

(a) Missions publiées des chapitres 02, 05, 07 : aucune quasi identique ; recouvrements de fait
acceptés (07/07 Q2 ↔ 07/04-defi Q1 ; 07/08 Q4 ↔ quiz 07 Q6 ; 07/08 Q6 ↔ 07/06-defi-concours Q4).
(b) Entre les six missions : 02/07 Q2 ↔ 02/08 Q3 (MAJEUR, voir 02/08) ; 02/07 Q5 ↔ Q6 (MAJEUR, voir
02/07). Digestion et villosité reviennent dans 05/07, 05/08, 07/07 sous des angles différents
(organes, expérience, QCM) : pas de gabarit répété. (c) Autres chapitres de SVT : rien au-dessus de
0,24 ; aucun recouvrement de question.

### Fuites (bilan)

En avant (ordre quête) : 05/08 Q6 → Q7 (MAJEUR) ; 02/07 Q1–Q3 → Q5 et 05/08 Q4 → Q5 (inhérentes à
l'enchaînement officiel « interpréter puis conclure », « rôle puis nom » ; mineures, sans correctif
exigé). Donjon (tirage au hasard) : 02/07 Q5 ↔ Q6 (traité par le correctif du doublon), 02/08 Q4 → Q2,
05/07 Q5 → Q4 (inhérentes, mineures). Aucune décimale ni coche ✓ qui livrerait un verdict ; la seule
coche (07/07 Q2, « = 30 ✓ ») suit une valeur qui n'est aucune option.

### Étiquettes : les cinq familles que l'auteur dit manquer (seuil : ≥ 3 questions distinctes,
tranche + SVT publié, recherche par motif sur toutes les options fausses)

| famille | questions distinctes | décision |
|---|---|---|
| lire un état de valve à l'envers selon la phase | 1 (07/08 Q3) | muette |
| cavité étroite prise pour la relâchée (ou l'inverse) | 1 (07/08 Q5) | muette |
| **l'eau seule digère, sans enzyme** | **4** (05/08 Q3 b, Q4 a, Q5 d ; publié 05-al-hadm/03-boss Q3 c « أنّ الماء يهضم اللّحم ») | **étiquette nouvelle** |
| action d'une sécrétion dans l'organe qui la stocke | 1 (05/07 Q3, options b et d) | muette |
| mauvaise voie accusée (sensitive/motrice) par rapport à la coupure | 2 (02/07 Q1 a, Q4 a ; 02/08 Q6 a est une autre erreur) — 1 seule après le correctif de 02/07 Q4 | muette |

Étiquette proposée : `bio.dig.eau-sans-enzyme` (famille `bio.dig`, sans compétence, comme
`bio.lecture.valeur-d-une-autre-grandeur`) —
fr « Tu crois que l'eau suffit à digérer : elle découpe les molécules, mais seulement si une enzyme facilite son action. » ;
en « You think water alone digests food: it splits the molecules, but only when an enzyme facilitates its action. » ;
ar « تظنّ أنّ الماء وحده يهضم الغذاء: الماء يفكّك الجزيئات، لكن بتيسير من أنزيم لا بدونه. »
(miroir exact de `bio.dig.enzyme-agit-seule`). À poser sur 05/08 Q3 b, Q4 a (texte corrigé),
Q5 d ; et, hors périmètre, sur le publié 05/03-boss Q3 c.

Toutes les étiquettes posées existent dans le registre d'`origin/main` ; inexactes : 02/08 Q6 a
et c (corrigées par le correctif de Q6). Options muettes qui méritent une étiquette existante :
02/08 Q4 b (`cause-sans-temoin`), 05/08 Q5 a, c (`specificite-enzyme-ignoree`), 05/08 Q7 b
(`absorption-dans-la-digestion`).

### Programme et ordre d'enseignement

Toutes les notions relèvent du chapitre de la mission ou d'un chapitre antérieur du manifeste
(07/07 en 07 : Q1 ← 05, Q3 ← 01, Q2 et Q4 ← 07). Notions hors cours données dans CHAQUE énoncé qui
les emploie : vérifié une à une (bouts central/périphérique, zones 1/2, vésicule, شُرين/وُريد, (س),
vue de face, convention des valves, accolades, R, code des couleurs). Une notion testée ni
enseignée ni donnée en toutes lettres : l'action des sucs pancréatique et intestinal sur les
lipides (05/08, mineur — Q8 se résout par élimination, Q3/Q4 la tirent des données).
« besides digestion » (2021 ex.2, 2b) non repris : acceptable, à condition de corriger
l'explication de 05/07 Q5 qui affirme le contraire.

---

## Chiffre final

- Questions auditées : **36** (02/07 : 6 · 02/08 : 6 · 05/07 : 5 · 05/08 : 9 · 07/07 : 4 · 07/08 : 6),
  toutes re-résolues à l'aveugle avant lecture de la clé.
- Clés fausses : **0** (36/36 conformes) — aucun défaut critique.
- Défauts majeurs : **11** — 02/07 Q4 (prémisses niées), 02/07 Q5↔Q6 (doublon), 02/08 Q3 (doublon de
  02/07 Q2), 02/08 Q6 (figure inutile, prémisses), 05/07 Q4 (vote), 05/07 Q5 (explication contraire
  au sujet), 05/08 Q2 (explication fausse), 05/08 Q4 (prémisses niées), 05/08 Q6 → Q7 (fuite en
  avant), 05/08 Q6 (graduations en RTL), 07/08 figure B (valves A-V fermées).
- Questions à reprendre : **11** — 02/07 Q4, Q6 ; 02/08 Q3 (à supprimer), Q6 ; 05/07 Q4, Q5 ;
  05/08 Q2, Q4, Q6 ; 07/08 Q1, Q5 (même figure B).
- Défauts mineurs : **14** (dont 3 fuites inhérentes sans correctif exigé) + 1 étiquette nouvelle
  proposée.
- Mission sans défaut : 07/07.
- Points (1), (2), (3) de l'auteur : (1) B = systole auriculaire confirmé sur le PDF — Q5 reste ;
  (2) logique officielle confirmée, conforme au cours 02 ; (3) `bile-avec-enzymes` sur 05/08 Q4 b
  acceptable (libellé montré seulement à la correction de fin de mission).

Verdict : **à corriger avant livraison**. Aucune réponse de l'auteur n'est invalidée ; une clé ne
change de forme que là où le correctif refait la question (02/07 Q6 devient un `mcq` de clé a ;
05/08 Q1 passe à {a, c, d, f} ; 02/08 Q3 disparaît). Les correctifs majeurs sont fournis en texte
exact, vérifiés par script (longueurs, prémisses) et dans Chromium pour les figures, tableaux et
chaînes ; trois mineurs de figure (pattes de 02/07, fibres de Y en 02/08, chambre de chasse en
07/08) ne donnent qu'une direction, à re-rendre par l'auteur.
