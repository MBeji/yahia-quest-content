# Re-vérification ciblée — L13 (m038–m043) après correction

Commit audité : `40e6fc33` (branche `wip/gisement-svt-9eme-sessions`). Aucun fichier de `content/` modifié, aucune écriture git.
Rapport écrit au fil de l’eau (état : terminé).

Note de traçabilité : les corrections des six fichiers ne sont pas dans `40e6fc33` (ce commit n'ajoute que
`09/13-devoir-*`) mais dans `43530690` (« L11 corrigé après audit… »). Je vérifie l'état de `HEAD` ; à signaler
pour le message de la PR.

## m038 (08/12) — 9 questions

Re-résolution à l'aveugle de toutes les questions (retouchées : Q2, Q3, Q4, Q5, Q9 ex-Q10 ; voisines : Q1, Q6,
Q7, Q8) : 9/9 clés justes. Mes textes sont appliqués à la lettre : clé de Q2 (40, à égalité avec `c`), fin de
l'explication de Q4 (plus de « اتّجاه (1) »), préfixe « (مناظرة 2019، بمعطيات الدّرس) » sur Q3–Q4, titre
« … من الرّئة إلى الكريّة الحمراء ⭐⭐ », Q8 (ex-2010) retirée, ex-Q10 en d2. Plus aucune clé strictement la plus
longue ni la plus courte (0/7). Fuites : l'explication de Q1 garde « الحويصلة … هي العنقود » ; sans l'ex-Q8,
elle ne résout plus rien. Aucune autre fuite trouvée (Q3 n'est plus donnée par Q4).

Frottis rendu dans Chromium à 232 px : l'hématie (163,2 ; 67,0) est retirée ; la pointe de la flèche 2 est dans
le plasma, nettement séparée des hématies. **OK.**

## m039 (08/13) — 6 questions

Re-résolution : Q1 (appariement), Q2 `c`, Q3 `d`, Q4 `b`, Q5 `a`+`b`, Q6 `a` : 6/6 justes. Étiquette de Q2 sur
`b` (exacte), `a` muette ; explications de Q2, Q3, Q4 conformes à mes textes ; Q5 `e` remplacé.

Cloche rendue dans Chromium à 232 px, dans Q1 et dans Q2 : fermée en haut de part et d'autre du bouchon,
membrane bombée vers le haut, ballons petits, flèche vers le haut, aucun fond rigide. Conforme au PDF 2018 et à la
clé. **OK.**

**Écart 5 : m039 Q6 — je tranche : à changer ([MAJOR]).** Une fois mes coupes faites, Q6 reste le **miroir** de Q3
et Q4 (inspiration contre expiration). Son explication (« في الشّهيق يتقلّص الحجاب … وينخفض الضّغط … وارتخاء الحجاب
الحاجز وزيادة الضّغط من سمات الزفير ») donne les clés de Q3 (cause) et de Q4 (pression) quand le donjon la tire
avant elles, et sa clé « تتمطّط الرئتان » reprend le fait du quiz 08 Q1. C'est aussi le seul QCM de la mission dont
la clé est strictement la plus courte (14 contre 21–39 : écart 4). Retouche proposée : garder l'item 2016 (« أثناء
الشّهيق تتمطّط الرّئتان ») comme donnée, mais demander **pourquoi**. Le fait vient du cours 08 (غشاء الجنب ; un trou dans la
paroi empêche la distension) et du dessin (ب) du sujet 2018, qui légende « غشاء الجنب ». Aucune autre question ne
le demande. Texte complet :
- énoncé : `(مناظرة 2016) أثناء الشّهيق تتمطّط الرئتان. ما الذي يجعلهما تتمطّطان مع اتّساع القفص الصدريّ ؟`
- `a` (clé) : `التصاقهما بجدار القفص الصدريّ عبر غشاء الجنب` (44)
- `b` : `تقلّص عضلات في جدار الرئتين فتتّسعان وحدهما` (43), étiquette `bio.resp.poumons-aspirent-l-air`
- `c` : `اندفاع الهواء إليهما بقوّة فينفخهما كالبالون` (44), muette
- `d` : `امتلاء أسناخهما بالدم القادم من القلب فتنتفخان` (46), muette
- explication : `يلتصق غشاء الجنب بالرئتين وبجدار القفص الصدريّ: فإذا اتّسع القفص في الشّهيق جذب الرئتين معه فتتمطّطان، ثمّ يدخل الهواء إليهما. فالهواء لا ينفخهما بل يتبع تمطّطهما، ولا عضلة في جدارهما، والدم يجري في الشّعيرات حول الأسناخ ولا يملؤها. ولهذا يكفي ثقب في جدار القفص لتتوقّف الرئة عن التمطّط. الخطأ الشائع: الظنّ أنّ الرئتين تتّسعان بذاتهما.`
Pour couper la dernière fuite vers cette Q6 (l'explication de Q1, avant elle dans `displayOrder`, élimine `b`) :
dans l'explication de Q1, remplacer « دون أن يتحرّكا بذاتهما، كالرئتين اللّتين لا عضلة فيهما. » par
`دون أن يتحرّكا بذاتهما، كالرئتين.`
Contrôles : la clé n'est ni la plus longue ni la plus courte (44 contre 43, 44, 46) ; une seule réponse juste au
regard du cours ; l'énoncé ne dit pas « pas de muscle » (sinon `b` nierait une prémisse et tomberait à vue) ; ni l'énoncé ni l'explication ne parlent du diaphragme, de la
pression ou du volume au temps de l'expiration, donc aucune fuite vers Q2–Q4. L'étiquette de `b` est exacte (les
poumons se dilatent par leurs propres muscles). Les étiquettes `mecanique-ventilatoire-inversee` de l'ancienne Q6
disparaissent avec elle (la famille reste portée par Q2, Q3, Q4).

## m040 (08/14) — 7 questions

Re-résolution : Q1 `c`, Q2 `d`, Q3 `b` (21,6), Q4 `a`, Q5 `d`, Q6 `c`, Q7 a→e : 7/7 justes. Mes textes sont
appliqués : énoncé de Q3 avec l'oxygène (le « 10 » de `c` devient obtenable, et l'étiquette exacte) ; clés de Q2
(57), Q5 (60) et Q6 (78) : 0/6 clé strictement la plus courte ou la plus longue ; données du doc. 4 sur quatre
lignes « عند … كم/س : … حركة في الدقيقة », rendues dans Chromium `dir=rtl` dans l'ordre source. Pas de fuite
nouvelle : les valeurs de repos de l'énoncé de Q3 sont déjà dans celui de Q4, qui ne demande pas de rapport.

Mineurs restants :
- Q5 : « ما الذي يبيّنه الجدول » alors que les données ne sont plus un tableau → `ما الذي تبيّنه هذه القياسات عن علاقة الإيقاع التنفّسي بسرعة المشي ؟`
- Q6 `b` : « تكثّف الرئتان حركاتهما من تلقاء نفسها » → `تكثّف الرئتان حركاتهما من تلقاء نفسيهما فيرتفع استهلاك العضلات للأكسيجين تبعًا لهما`
  (accord du duel ; 83 caractères ; la clé (78) reste à égalité avec `a` et `d`, ni la plus longue ni la plus courte).

## m041 (09/10) — 7 questions

Re-résolution : Q1 `c`, Q2 `d`, Q3 `a`+`c`+`d`+`e`, Q4 `b`, Q5 `a`, Q6 `d`, Q7 `c` : 7/7 justes. Ex-Q3 retirée ;
Q3 (multi) conforme à mon texte : l'intestin porte deux écritures justes et une fausse, le décompte ne se lit plus
par organe ; explication de Q4 (ex-Q5) sans « أكسدته بالأكسيجين » ; Q7 `a` muette ; phrase sur l'écart 15/53 –
20/49 avec le cours ajoutée à Q1. Aucune clé strictement la plus longue ou la plus courte (0/6).

**Écart 3 (clés rallongées d'un mot) — accepté.** Q2 « … مع هواء الأسناخ نفسها » (65, à égalité avec `a`) et Q5
« … فينتقل الجليكوز منها إلى الدم » (63) : le sens ne change pas, aucune option ne devient la plus longue, et le mot
ajouté ne répète aucun mot propre à la clé.

**Écart 1 (Q6–Q7 en d3, mission d4) — je retire mon majeur ; la mission garde le d4.** Le schéma plafonne la
difficulté d'une question à 3 : ma demande de passer deux questions en d4 était impossible, et c'est mon erreur.
Dans tout le corpus, l'étage d4 est porté par l'en-tête `challenge` et ses questions sont en d2–d3 : 05/09 (le
même type d'exercice de seconde partie, 2019 ex.4) a le profil 2-2-2-3-3-3-3-3, et m041 a 2-2-2-3-3-3-3. Le
contenu justifie l'étage : seconde partie d'examen (R1), quatre organes à croiser, double mécanisme au rein
(consommation + réabsorption totale), chasse à l'erreur sur le sens de la réaction. **OK.**

Mineur restant (déjà noté, sans correctif exigé) : la clé de Q2 suppose que l'échantillon 2 a traversé les
poumons, ce qui oriente Q1 (structure du sujet).

## m042 (09/11) — 9 questions

Re-résolution : 9/9 justes (Q8 `d` : artère = ع, 0,1 ; veine = س, 0,03). Q8 : mes quatre options sont reprises
mot pour mot. L'attribution se répartit à 2 contre 2 et chaque raison n'apparaît qu'une fois : aucune option ne se
contredit plus. La clé (82) est à égalité avec `a`. La phrase ajoutée à l'explication ne résout pas Q9. Q7 :
l'étiquette est passée de `d` à `c`, toutes deux exactes ou muettes comme demandé.

**Écart 4, m042 Q5 (clé « بولة » strictement la plus courte) — accepté.** Les quatre options sont des mots isolés
de 4 à 8 caractères, repris du sujet 2012 ; l'écart d'un caractère avec « نشادر » ne fait pas un indice de forme
(le critère de longueur ne vaut que pour les phrases). Une seule clé courte dans la mission (1/8).

## m043 (09/12) — 6 questions

Re-résolution : Q1, Q3 (appariements), Q2 `c`, Q4 `a`+`b`+`c`, Q5 `d`, Q6 `b` : 6/6 justes. Ex-Q7 retirée ; titre
« مناظرتا 2005 و2007 » ; Q4 `e` → « سعة المثانة … » avec son explication. Figure rendue dans Chromium à 232 px :
repères 3–4 retirés du neurone, flèches 1–2 de A conservées, aucun repère orphelin. L'énoncé de Q2 ne nomme plus
l'unité A.

**[MAJOR] m043 Q2 (nouvelle forme, décision du pilote) : le vote reconstruit la clé.** Options : (CO₂ ; O₂),
(O₂ ; N₂), **(O₂ ; CO₂)**, (N₂ ; CO₂). Pour le gaz 1, O₂ figure 2 fois contre 1 pour CO₂ et 1 pour N₂ ; pour le
gaz 2, CO₂ figure 2 fois contre 1 pour O₂ et 1 pour N₂. Le vote case par case donne (O₂ ; CO₂), la clé, sans
aucun savoir. Correctif : remplacer `d` par `الغاز 1 : ثنائي أكسيد الكربون ؛ الغاز 2 : الأزوت` (48 caractères).
Recompte case par case :
- gaz 1 : O₂ ×2 (`b`, `c`), CO₂ ×2 (`a`, `d`) ;
- gaz 2 : CO₂ ×1, O₂ ×1, N₂ ×2.
Le vote ne donne plus la clé. La clé `c` (51) est à égalité avec `a`. Rendu Chromium vérifié. L'explication
reste juste (« الأزوت لا يشارك … »).

**Écart 2 (le nom de fichier garde « 2001 ») — [MINOR].** Rien ne casse : aucun élève ne voit le nom, et le
fichier n'a jamais été publié, donc aucun identifiant n'est encore figé. Mais le nom annonce une source que la
mission ne contient plus. Correctif recommandé avant la première publication (ensuite le renommage coûterait
l'identité) : `12-examens-2005-ex2-2007-ex1-unites-structurales-fonctionnelles.json`, et retirer 2001 ex.3 des
`sources` de la ligne m043 du registre `gisement.json`. Si le pilote préfère garder le nom, le déclarer au
registre.

Résiduel mineur (inévitable, déjà noté) : les gaz de Q2 désignent l'unité A comme le lieu des échanges gazeux.

## Gates

`content:check` vert. `content:qa:strict` : 0 erreur et 0 avertissement sur les six fichiers L13. Les 3 erreurs
du rapport sont hors périmètre : marques Markdown « ** » dans `03/13-devoir-*` Q7 et `09/13-devoir-*` Q3–Q4
(autre auteur), mais elles **bloqueront la CI** de la branche commune. `content:tranche --chapters 08,09` : 0/167
clé strictement la plus longue ; la seule paire proche est hors lot (quiz 08 #4 ↔ 08/02 #5).

## Bilan de la re-vérification

- Clés fausses : **0** (44 questions re-résolues à l'aveugle).
- Majeurs restants : **2**
  1. m039 Q6 : miroir de Q3–Q4 et doublon du quiz 08 Q1. Remplacement complet ci-dessus (« ما الذي يجعلهما
     تتمطّطان … » ; clé `التصاقهما بجدار القفص الصدريّ عبر غشاء الجنب`), plus une coupe dans l'explication de Q1.
  2. m043 Q2 : le vote case par case reconstruit la clé. `d` → `الغاز 1 : ثنائي أكسيد الكربون ؛ الغاز 2 : الأزوت`.
- Mineurs restants : **3**
  1. m040 Q5 : « الجدول » → `ما الذي تبيّنه هذه القياسات عن علاقة الإيقاع التنفّسي بسرعة المشي ؟`
  2. m040 Q6 `b` : `تكثّف الرئتان حركاتهما من تلقاء نفسيهما فيرتفع استهلاك العضلات للأكسيجين تبعًا لهما`
  3. m043, nom de fichier : renommer en `12-examens-2005-ex2-2007-ex1-unites-structurales-fonctionnelles.json`
     avant la première publication (et retirer 2001 ex.3 du registre), ou bien le déclarer.
- Écarts de l'auteur : 1 accepté (le d4 de m041 tient, et je retire mon majeur) ; 2 mineur (ci-dessus) ;
  3 accepté ; 4 accepté pour m042 Q5, et sans objet pour m039 Q6 si le remplacement est appliqué ; 5 tranché :
  changer Q6.
- Figures : la cloche de m039 (Q1 et Q2) et le frottis de m038 sont conformes dans Chromium à 232 px.

**Verdict : prêt après les 2 majeurs** (les mineurs peuvent suivre dans la même passe). Pas besoin d'une
nouvelle re-vérification complète : un contrôle des deux questions suffit.

## Suite donnée par le pilote (2026-10-16)

Majeurs 1 (m039 Q6 remplacée par le texte de ce rapport + explication de Q1) et 2 (m043 Q2 option d) appliqués
mot pour mot ; mineurs : m040 Q5 énoncé, m040 Q6 b (duel), fichier m043 renommé
`12-examens-2005-ex2-2007-ex1-unites-structurales-fonctionnelles.json` et C24#3 retiré des sources de la mission
au registre (et C09#1.2 retiré de m036, L12). `content:check` vert, prettier propre. Les `**` des devoirs
(`03/13`, `09/13`) relèvent du lot L14, signalés à son auteur. **L13 prêt à livrer.**
