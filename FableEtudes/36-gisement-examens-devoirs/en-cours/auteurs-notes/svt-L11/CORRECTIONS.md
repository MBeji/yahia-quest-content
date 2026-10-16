# Corrections L11 après audit à l'aveugle (audit-svt-L11.md) — tout appliqué

Contrôles finaux : content:check OK ; content:qa : 1 erreur, NON à moi (03-al-ibsar/13-devoir-affirmations-et-intrus-neurone-oeil Q7, markdown `**` — autre auteur) ; content:tranche : 0 paire proche dans mes fichiers (reste quiz#7 ↔ boss#1, publié), clé la plus longue 0 dans mes fichiers ; lot-lint : 0 point sur les 5 fichiers ; figures rendues en Chromium (232 px).

## Cours / résumés (décisions du pilote)
- 01 `cours.md` : bloc `propriete` « بنية العصب » (fibres en حزم, نسيج رابط entre les حزم) inséré avant le `verifie` du § périphérique ; 01 `resume.md` : phrase ajoutée à la ligne du système périphérique. renderLesson/renderSummary : rendu OK (contrôle par tsx). Le bloc ne dit ni quelle coupe est un nerf ni les repères 4-6 : aucune clé de m028 livrée.
- 02 `cours.md` (exemple « العضو المنفّذ ليس دائمًا عضلة », étape 1) : « ملامسة الطّعام لسان الرّضيع تُنبّه مستقبلات حسّيّة في اللّسان » ; 02 `resume.md` : « اللّعاب عند ملامسة الطّعام للّسان ». Écart à déclarer : la glande salivaire reste la clé de 02/01-tamrin Q5 et quiz Q8 (qui parlent, eux, de « شمّ رائحة طعام ») ; le scénario d'odeur n'est plus dans le cours (le pilote est invité à les reformuler si besoin).

## m028 (9 → 6 questions)
- Q5 (sens dans le neurone) supprimée ; Q8 et Q9 déplacées dans m029.
- Q2 (repères 4-6) : énoncé de l'audit (rappel des définitions sans paires) ; r1 « حزمة من الألياف العصبيّة » (décision 3) ; explication « يدلّ على حزمة » ; `<title>` SVG « تفصل بينها مساحة داكنة » ; taquets verticaux à la flèche 5.
- Q3 : l'énoncé ne dit plus « حزم يفصل بينها نسيج » (le cours l'enseigne maintenant) mais « كتل مستديرة … تفصل بينها مساحة داكنة فيها وعاء » ; je n'ai PAS ajouté la phrase « علمًا أنّ … » de l'audit (elle donnait la clé alors que le cours est complété). Lettres أ ب ج sous les trois cases de la figure (lettres arabes sans parenthèses dans le SVG, comme le demandait l'audit : écart à la règle « arabe seulement dans title »).
- Q4 : énoncé allégé (plus de description des coupes, pour ne pas livrer Q3) ; explication de l'audit.
## m029 (9 → 9)
- Supprimées : Q5 (chronologie), Q9 (éléments de l'arc). Reçues : ex-m028 Q8 (influx moteur ; phrase sur fibres retirée ; explication réécrite sans la règle des fibres) et ex-m028 Q9 (récepteur ; énoncé sans « تتأثّر بالمنبّهات ») placées après Q2.
- Q1 : énoncé sans scénario (« … عند الإنسان وعند الحيوان ») — variante de l'audit sans « لاإراديّ » qui aurait donné a.
- Q2 : f = « تهيئة الهضم بإفراز اللّعاب عند ملامسة الطّعام للّسان » ; exemples ajoutés à c (كاختيار إجابة في امتحان) et e (كركوب الدّرّاجة).
- 2007 q1 : clé « فعل انعكاسيّ فطريّ، لأنّ الرّجل جذب ساقه تلقائيًّا دون قرار مسبق ». Écart : j'ai ajouté « عصبيّة » aux quatre chemins de la Q4 (ألياف عصبيّة حسّيّة/حركيّة) pour que la clé ne soit pas la plus courte (ex aequo avec b).
- ex-Q9 : clé allongée (« المنبّه الخارجيّ الذي يتأثّر به ») pour qu'elle ne soit plus la plus courte.
- Q7 (moelle) : « (أُضيف السّهمان إلى رسم المناظرة.) ».
## m030 (7 → 6)
- Q4 (choroïde) supprimée. Q1 explication ; Q2 énoncé + explication ; Q3 énoncé/options/explication (œil seul) ; Q6 explication + « (انطلاقًا من مناظرة 2017) » ; Q7 première phrase de l'explication : tous de l'audit.
- Écart : Q6 (rayons) options allongées (التّجمّع/التّباعد « المتوازية ») pour que la clé ne soit ni la plus courte ni la plus longue (36 car. ; 43/29/31).
## m031 (8 → 7)
- Q8 supprimée. Q2 : options a/c réduites à l'état + explication ; Q3 : c remplacée (« ينتقل الدّم من البطينين إلى الأذينتين عبر صمّامات أذينيّة بطينيّة مفتوحة ») + explication ; Q6 : repères 7/8 de l'audit (figure) + énoncé sans les lieux ; Q7 : explication de l'audit.
- Écarts : énoncé de Q7 réduit à « ما دور الصمّامات الأذينيّة البطينيّة في القلب ؟ » (il donnait le lieu des AV, utile à Q6) ; énoncé de Q2 reformulé (« ينقبض البطينان معًا أثناء الانقباض البطينيّ. أيّ العبارات … صحيحة في هذا الطّور ؟ ») car la paire Q1/Q2 montait à 0,46 au contrôle de proximité.
## m032 (8 → 6)
- Q2 (définition de l'إلقاح) supprimée (étiquettes plusieurs-spermatozoides-entrent et fecondation-reduite-a-l-entree disparaissent). Q1 : b = menstruation + explication (الحيض). Q5+Q6 fusionnées en un appariement à 5 paires (numérotation du sujet, figure de l'audit reconstruite avec mon générateur — mêmes dessins, 2 rangées) ; Q8 sans « فيتضاعف ».
- Écart : la phrase finale de l'explication de Q1 (« … الإباضة والإلقاح لأنّهما يُذكران معًا ») a été remplacée par « … الإباضة والحيض لأنّهما يقعان في الدّورة نفسها ».
## Étiquettes
- Retirées avec leurs questions : plusieurs-spermatozoides-entrent, fecondation-reduite-a-l-entree, (m028) sens-du-message-inverse sur l'ex-Q5. Aucune nouvelle.
