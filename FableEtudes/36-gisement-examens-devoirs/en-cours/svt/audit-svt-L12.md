# Audit indépendant : lot L12 (gisement SVT 9ᵉ, vague 2) : m033 à m037

Auditeur indépendant. Périmètre : `assign-svt-L12.md`, soit 5 missions (chapitres 05, 11 et 12) de
`/home/user/wt-svtses` (branche `wip/gisement-svt-9eme-sessions`, commit `818fdb66`). Rapport écrit
au fil de l'eau. Aucun fichier audité n'a été modifié, aucune écriture git.

Sources lues : transcriptions officielles 2007, 2009, 2011, 2012, 2013, 2015, 2016, 2017, 2018, 2019 ;
`cours.md` et `resume.md` sur `origin/main` ; `misconceptions.json` sur `origin/main` ; missions
publiées, quiz et vague 1 des chapitres 05, 11 et 12.

---

## m033 : `05-al-hadm/exercices/09-examen-2019-ex4-protides-digestion-absorption-croissance-rats.json` (d4, 8 q.)

Fidélité à la transcription 2019 ex. 4 : tubes 1 à 3, courbes 1 et 2 (paliers, croisement vers la
minute 90 et 60 %), tableau 70/55/40, puis 60/85/110 : conforme. Le SVG de Q5 reproduit les points
annoncés (palier de 20 % à 130 min, 100 % à 150 min, croisement à (90 ; 60 %)). La coquille « مثكلة »
a été écrite « المعثكليّة » : correct.


| Q | type | ma réponse | clé | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| 1 | mcq d2 | b | b | réserve | la glose de l'énoncé (« ناتج عن تفكيك جزئيّ ») est la clé mot pour mot ; a nie la glose et la donnée « بقاء البروتيدات » |
| 2 | mcq d2 | c | c | OK | acides aminés ; étiquettes justes |
| 3 | numeric d2 | 70 | 70 | réserve | la clé 70 égale le poids du jour 0 : la lecture fautive « 70 » est comptée juste |
| 4 | mcq d3 | a | a | réserve | l'énoncé reprend la glose « تفكيك جزئيّ » qui livre Q1 |
| 5 | mcq d3 | d | d | réserve | b dit « تتناقص نسبته في الدّم » alors que la courbe 2 monte : écartée à vue ; c (استحلاب) faible |
| 6 | multi d3 | a, b, c | a, b, c | OK | 3 vraies sur 6 ; chaque énoncé vérifié (−15, −15 ; +25, +25 ; min 40 ; 60 > 40) |
| 7 | mcq d3 | b | b | réserve | énoncé « (ناتج هضم البروتيدات) » qui livre Q2 ; explication « وهو مادّة بناء » qui livre Q8 ; a et d faibles ; c redit Q8 |
| 8 | mcq d3 | c | c | réserve | a nie la prémisse de l'énoncé (« الطّاقة غير متوفّرة » quand l'énoncé pose sucres et graisses) |

Étage d4 avec des questions d2–d3 : conforme à l'usage de la vague 1 (05/08, 09/10). Rampe 2-2-2-3-3-3-3-3
non décroissante. Aucun chiffre arabo-indien. Notions : « عديد البيتيد » n'est pas au cours 05 (glosé dans
l'énoncé, à juste titre) ; « أغذية بنّاءة » est au cours 04 (§ classement des aliments) : OK.

### Défauts m033

- **[MAJOR] Q1 : la glose livre la clé.** « عديد البيتيد مادّة وسيطة ناتجة عن تفكيك جزئيّ للبروتيدات » est la
  clé b reformulée (« تفكيكًا جزئيًّا فتنتج عديد البيتيد »), et la même glose, répétée dans Q2 et Q4, livre Q1
  par ces deux questions. L'option a (« تفكيكًا تامًّا… ولا علاقة لعديد البيتيد بها ») nie à la fois la
  glose et la donnée « وجود البروتيدات » du tube 2 : écartée à vue.
  Correctif, dans Q1, Q2 et Q4, remplacer la glose par :
  « (عديد البيتيد: جزيئة أقصر من جزيئة البروتيد) »
  (Q1 : phrase seule « عديد البيتيد جزيئة أقصر من جزيئة البروتيد. »). Le geste « partiel » reste à inférer de
  la présence conjointe des protides et du polypeptide.
  Et remplacer Q1 a par (102 car., la clé b fait 83, c 79 : la clé n'est ni la plus longue ni la plus courte) :
  « كان عديد البيتيد موجودًا أصلًا في فتات اللّحم، والعصارة المعديّة لم تفعل إلّا أن كشفت عنه في الأنبوب 2 »
  (réfutée par le tube 1 témoin, sans polypeptide ; sans étiquette). Ajouter à l'explication : « والأنبوب 1
  الشّاهد لا عديد بيتيد فيه، فهو لم يكن في اللّحم أصلًا. »
- **[MAJOR] Q8 a nie une prémisse.** L'énoncé pose que le régime contient sucres et graisses ; « الطّاقة غير
  متوفّرة في الغذاء » s'élimine sans connaissance, et la question se réduit à b/c/d dont trois commencent par
  « الطّاقة متوفّرة ». Correctif (95 car. ; clé c 100, b 99, d 109 : la clé est 3ᵉ sur 4) :
  a = « الطّاقة متوفّرة في الغذاء، والبروتيدات أغذية واقية يمدّ بها العنصر (×) الجسمَ ليحميه من الأمراض »
  (confusion bâtisseurs / protecteurs, cours 04 § classement). Ajouter à l'explication : « والأغذية الواقية هي
  الفيتامينات والأملاح المعدنيّة والماء، لا البروتيدات. »
- **[MAJOR] Q5 b contredit la figure.** « …فتتناقص نسبته في الدّم » alors que la courbe 2, décrite et
  dessinée, monte. Correctif (102 car. ; clé d 104, a 103, c 105) :
  b = « يتناقص العنصر (×) في المعي لأنّه يُهضم فيه، ويتزايد في الدّم لأنّ الجسم يصنعه: فلا علاقة بين المنحنيين »
  (accepte les deux sens des courbes, nie seulement le lien ; sans étiquette). Dans l'explication, remplacer
  « والمنحنى 2 يتزايد لا يتناقص » par « وتزامن الهبوط والصّعود يربط المنحنيين، فليس الصّعود في الدّم صنعًا مستقلًّا ».
- **[MAJOR] Fuite Q7 → Q8 et Q7 → Q2.** L'explication de Q7 « (وهو مادّة بناء) » est la clé de Q8 ; l'énoncé
  de Q7 « (ناتج هضم البروتيدات) » désigne les acides aminés de Q2. Correctif : supprimer les deux parenthèses
  (Q7 se résout par la seule variable changée, sans elles). La fuite résiduelle de Q8 (« غذاء خالٍ من البروتيدات »
  puis X qui rétablit la croissance) est celle du sujet officiel lui-même : acceptable.
- **[MINOR] Q7 : distracteurs faibles et redite de Q8.** d (« يمنع الفئران من الأكل أصلًا ») est sans
  appui, et c (rôle seulement énergétique) est la croyance que Q8 réfute. Correctif proposé pour d (99 car. ;
  clé b 89, a 97, c 87 : la clé reste 3ᵉ) : « نقص الوزن في الفترة الأولى سببه مرض أصاب الفئران ثمّ شُفيت منه في
  الفترة الثّانية دون علاقة بالغذاء » (même défaut de raisonnement que a : un facteur non varié ; à garder
  sans étiquette). c peut rester.
- **[MINOR] Q3 : clé égale à une donnée.** 110 − 40 = 70 = poids du jour 0 : l'élève qui recopie la première
  valeur du tableau est compté juste. Correctif : « …بين اليوم 40 واليوم 100، بالغرام؟ », clé 45 (85 − 40 ;
  45 n'est aucune valeur du tableau) ; explication : « وزن الفئران 40 غ في اليوم 40 و85 غ في اليوم 100،
  فالزّيادة 85 − 40 = 45 غ. الخطأ الشّائع: أخذ الفرق بين اليومين 80 و100 (25 غ) أو بين اليومين 40 و120 (70 غ). »

**Point signalé : proximité de l'absorption avec 05/08 Q6–Q7.** Voir § fin (tranché avec m034 Q5).

---

## m034 : `05-al-hadm/exercices/10-examens-2017-ex4-et-annales-amidon-salive-suc-gastrique-intestinal.json` (d3, 10 q.)

Fidélité : 2017 ex. 4 (tubes 1–4, courbes A/B : 20 → ~17 g/L à 20 min puis 0 à 60 min, croisement vers
30 min à ~15 g/L, tableau 100/100/5), 2009 ex. 4 (tableau +/−, 15 min, source de A = la bouche), 2007 ex. 4
q3 (salive + eau distillée, 15 min, eau iodée jaune, Fehling rouge brique), 2015 ex. 1 item 3 (oxalate) :
conformes. SVG de Q4 recalculé : courbe 1 à 17,0 g/L à 20 min, croisement vers 28–30 min à ~15 g/L,
courbe 2 à ~20 g/L à 60 min : fidèle. Unités d'axe en latin (« g/L », « min ») dans un SVG arabe : usage
déjà admis en vague 1, pas un défaut.

| Q | type | ma réponse | clé | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| 1 | mcq d2 | b | b | OK | 2×2 propre ; d (« إلى بروتيدات ») faible |
| 2 | mcq d2 | a | a | ERREUR de doublon | = patron 05/02-tamrin Q4 (« ما النّاتج في أنبوب النّشا مع اللّعاب في 37 درجة؟ ») ; mêmes 4 options que m033 Q2 |
| 3 | mcq d2 | c | c | réserve | clé la plus courte (69 contre 76–79) ; fuite reçue de Q10 (« فهلنق السّاخن ↔ الجليكوز وسكّر الشّعير ») |
| 4 | mcq d3 | d | d | OK | 2×2 propre (nom de B × rôle du suc), option à deux erreurs (c) muette |
| 5 | mcq d3 | a | a | réserve | b (« إلى مغذّيات أبسط منه ») nie la prémisse « مغذٍّ بسيط » de l'énoncé ; clé la plus courte (90 contre 106–122) |
| 6 | ordering d3 | a b c d e | a b c d e | réserve | ordre unique ; items a, d, e livrent Q2 (سكّر الشّعير), Q4 (جليكوز + العصارة المعويّة), Q5 (امتصاص) |
| 7 | mcq d3 | c | c | OK | 2×2 propre (A × B), deux options à deux moitiés fausses muettes |
| 8 | mcq d3 | a | a | ERREUR de doublon | même fait que 05/02-tamrin Q2 (amylase sur blanc d'œuf) et quiz Q4 (trypsine sur amidon) ; son énoncé livre la moitié de Q7 ; clé la plus courte (73 contre 82–87) |
| 9 | mcq d3 | b | b | réserve | a (« يحتوي أصلًا على نشا ») recouvre en partie la clé (des restes d'un repas amylacé) |
| 10 | matching d3 | l1-r3, l2-r4, l3-r1, l4-r2 | idem | réserve | livre la clé de Q3 (« محلول فهلنق السّاخن ↔ الجليكوز وسكّر الشّعير ») ; trois paires sur quatre déjà posées en 04 |

Étage d3, rampe 2-2-2-3-3-3-3-3-3-3 : OK. Notions : « سكّر مختزل » (Q9, explication de Q3) n'est pas au
cours (04 et 05 disent « سكّر » ou « جليكوز ») : [MINOR], écrire « سكّر » ou « سكّر كالجليكوز ».

### Défauts m034

- **[MAJOR] Q2 : doublon du patron.** 05/02-tamrin Q4 pose le même fait (amidon + salive à 37 degrés → سكّر
  الشّعير), avec trois des quatre mêmes options ; les quatre options sont aussi celles de m033 Q2 (clé
  différente). Correctif : **supprimer Q2** (Q3 garde « عنصر جديد أ » défini dans son énoncé et reste
  autonome). La mission passe à 9 questions, puis à 8 avec le point suivant.
- **[MAJOR] Q8 : doublon de fait et fuite vers Q7.** « La salive ne digère pas les protides parce que son
  enzyme est spécifique » est déjà posé par 05/02-tamrin Q2 et le quiz Q4 (même geste, autre enzyme), et
  Q7 conclut déjà « لكلّ عصارة مادّتها ». Son énoncé (« عصارة هاضمة أ مصدرها الفم… اختفى النّشا… بقيت
  البروتيدات ») donne la première moitié de Q7. Correctif : **supprimer Q8** (2009 reste représenté par Q7).
- **[MAJOR] Q10 → Q3 (et Q3 → Q10).** La paire « محلول فهلنق السّاخن ↔ الجليكوز وسكّر الشّعير » donne la clé
  de Q3 (Fehling, et chauffé, contre d « دون تسخين ») ; l'explication de Q3 (« ونترات الفضّة كاشف أملاح
  الكلور… ماء اليود فكاشف النّشا ») donne trois paires de Q10. Correctif : remplacer l'appariement par
  l'item officiel de 2015 tel quel, en `mcq` d3 :
  - énoncé : « (مناظرة 2015) نكشف عن أملاح الكلسيوم بإضافة: »
  - options : a « محلول فهلنق السّاخن » (étiquette `bio.alim.reactifs-confondus`) · b « ماء اليود »
    (`bio.alim.reactifs-confondus`) · c « أكسلات الأمونيوم » (clé) · d « نترات الفضّة »
    (`bio.alim.reactifs-confondus`) ; longueurs 19 / 9 / 17 / 12 : la clé n'est ni la plus longue ni la
    plus courte ;
  - explication : « أكسلات الأمونيوم تعطي مع أملاح الكلسيوم راسبًا أبيض لا يسودّ في الضّوء. أمّا نترات
    الفضّة فراسبها الأبيض يسودّ في الضّوء، وماء اليود ومحلول فهلنق لا يعطيان راسبًا أبيض. الخطأ الشّائع:
    الخلط بين الرّاسبين الأبيضين. » (ne dit pas ce que révèle Fehling : aucune fuite vers Q3).
  Et, dans l'explication de Q3, remplacer « ونترات الفضّة كاشف أملاح الكلور » par « ونترات الفضّة لا تكشف
  عن السّكّر ».
  Remarque : l'item est en mcq comme 04/05-tadrib Q1 (chlorures), mais sur un autre fait (calcium), que
  rien ne pose encore en clé : pas un doublon.
- **[MAJOR] Q6 : l'ordre livre Q2 et Q4.** Les items nomment le produit de la salive et celui du suc
  intestinal, donc les clés de Q2 et de Q4 (moitié « جليكوز ») dans le donjon. Ce n'est pas inévitable.
  Correctif (ordre a-b-c-d-e inchangé et toujours unique ; 54 à 74 car.) :
  - a « يبدأ اللّعاب في الفم تفكيك جزء من النّشا إلى ناتج وسيط »
  - b « يعبر ما بقي من النّشا المعدة دون أن تفكّكه العصارة المعديّة » (inchangé)
  - c « تواصل أنزيمات المعي الدّقيق تفكيك ما بقي من النّشا إلى النّاتج الوسيط نفسه »
  - d « يُفكَّك النّاتج الوسيط في المعي الدّقيق إلى الوحدة التّركيبيّة للنّشا »
  - e « تعبر الوحدة التّركيبيّة للنّشا جدار المعي الدّقيق إلى الأوعية الدّمويّة »
  La fuite résiduelle de b vers Q1 et de e vers Q5 est un fait du cours (05 § « تتبّع الخبز »), pas une
  donnée de l'expérience : acceptable. L'explication de Q6 peut garder les noms (elle vient après Q1–Q5
  sur la route).
- **[MAJOR] Q5 : b nie la prémisse.** L'énoncé dit « مغذٍّ بسيط » ; b « تفكّكه… إلى مغذّيات أبسط منه » s'écarte
  à vue, et la clé est la plus courte de 16 caractères. Correctif :
  - énoncé : « (مناظرة 2017) ابتلع شخص 100 غ من سكّر ذائب في الماء (العنصر ب)، ثمّ قيست كمّيّة هذا العنصر في
    مواضع من الأنبوب الهضميّ: » (suite inchangée) ;
  - a (clé, 102 car.) : « العنصر ب لا يتغيّر في المعدة لأنّه بسيط، ثمّ يعبر معظمه جدار المعي الدّقيق إلى الأوعية: ظاهرة الامتصاص » ;
  - c (106 car.) : « يبقى معظمه مخزّنًا في جدار المعي الدّقيق ولا يبلغ الدّم، فتنقص كمّيّته في تجويفه: ظاهرة التّخزين في الجدار » ;
  - b (109) et d (106) inchangés. La clé n'est plus en tête courte que de 4 caractères, sans marqueur.
- **[MINOR] Q9 a recouvre la clé.** « لعاب هذا الشّخص يحتوي أصلًا على نشا » peut se lire comme des restes du
  repas. Correctif (105 car. ; clé b 85, c 88, d 82 : la clé reste 2ᵉ plus courte) :
  a = « تفرز الغدد اللّعابيّة لهذا الشّخص نشا مع اللّعاب، وقد حوّله أنزيمه كلّه إلى سكّر خلال الدّقائق الخمس عشرة ».
- **[MINOR] Q3 : clé la plus courte** (69 contre 76–79). À garder : la clé est la seule, avec d, sans
  « يدلّ على » ; l'allonger de « يدلّ على السّكّر » la rendrait strictement la plus longue (86). Voir le
  constat transversal sur les clés courtes.

**Point signalé : les fuites « inévitables » de la mise en ordre.** Tranché : évitables pour Q2 et Q4
(correctif ci-dessus), résiduelles et acceptables pour Q1 et Q5 (faits du cours).

---

## m035 : `05-al-hadm/exercices/11-examens-2016-ex4-2011-ex4-2012-ex2-anse-ligaturee-roles-intestin.json` (d3, 9 q.)

Fidélité : 2016 ex. 4 (20 mL + 20 mL, tableau −/−, −/−, −/+, −/+, deux heures), 2011 ex. 4 (tableau des trois
tubes ; 95 → 12 g et 5 → 88 g en 90 min), 2012 ex. 2 q1–q2, 2012 ex. 1 item 1 : conformes. Q9 n'a **aucune
source** (voir plus bas).

| Q | type | ma réponse | clé | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| 1 | multi d2 | a, b, e | a, b, e | OK | 3 sur 6 ; chaque énoncé vérifié contre le tableau |
| 2 | mcq d2 | c | c | réserve | d (« الأنزيمات الموجودة في الأنبوب ») suppose des enzymes que le tube 1 n'a pas ; « عديد البيتيد » non glosé |
| 3 | mcq d2 | b | b | OK | définition du cours 05 mot pour mot (« الخميلات: انثناءات دقيقة للغشاء السّيتوبلازميّ ») |
| 4 | mcq d2 | d | d | OK | définition du cours 05 |
| 5 | mcq d3 | a | a | réserve | clé = réunion des clés a + b de Q6 (fuite croisée) |
| 6 | multi d3 | a, b | a, b | ERREUR de fuite | ses deux énoncés justes sont les deux moitiés de la clé de Q5, et l'explication de Q5 les nomme (« هضم » ، « امتصاص ») |
| 7 | mcq d3 | b | b | réserve | d (« فتزايدت كمّيّتها فيه ») contredit le tableau (le contenu de l'intestin baisse) ; clé la plus courte |
| 8 | matching d3 | l1-r3, l2-r1, l3-r2 | idem | réserve | chaque membre droit finit par son produit (« ← جليكوز ») : l'appariement se fait sur le produit seul, la séquence des sucs ne sert à rien ; « غليسيرول » mis pour « كحول دهنيّة » sans déclaration |
| 9 | mcq d3 | a | a | ERREUR de source | expérience inventée, étiquetée « (مناظرة 2016) » ; clé de 42 car. contre 84–94, seule sans « لأنّ » |

Étage d3, rampe 2-2-2-2-3-3-3-3-3 : OK. Q3 : la clé b est celle du cours 05 (« الخميلات » = microvillosités ;
« انثناء مجهريّ لمخاطيّة » = خملة) ; le plan disait « repli de la muqueuse », c'était une lecture du mot
« villosité » ; avec le vocabulaire du cours, b est la seule juste et le terme de 2012 est respecté.

### Défauts m035

- **[MAJOR] Q9 : question inventée attribuée à la session 2016.** Le sujet 2016 n'a qu'une expérience
  (maltose + polypeptide). Une deuxième anse « avec maltose seul » n'est pas dans la transcription : la
  mission présente comme officielle une donnée qui ne l'est pas (consigne G6 § 2 : « chaque donnée de la
  mission est celle de la transcription »). Sur le fond, la prédiction est **juste** (la maltase de la
  paroi donne du glucose, qui traverse ; pas d'acides aminés sans protide) et **dans l'esprit** de 2016,
  mais elle redit Q1/Q5 (son énoncé recopie les résultats de la première expérience), et sa clé est la
  plus courte de moitié (42 contre 84–94, seule sans justification « لأنّ ») : marqueur de forme.
  Correctif : **supprimer Q9**.
- **[MAJOR] Q5 ↔ Q6 : fuite croisée.** Les énoncés justes de Q6 (a « تُفكَّك فيه المغذّيات المعقّدة… »,
  b « تعبر جداره المغذّيات الخلويّة نحو الأوعية ») sont les deux moitiés de la clé de Q5 ; dans le donjon,
  l'une résout l'autre, et sur la route l'explication de Q5 résout Q6. Correctif : **supprimer Q6** (la clé
  de Q5 porte déjà les deux rôles, dans l'ordre hydrolyse puis passage). La mission garde 7 questions :
  Q1, Q2, Q3, Q4, Q5, Q7, Q8.
- **[MAJOR] Q8 : appariement résolu par le produit final.** Les produits (« ← أحماض أمينيّة », « ← غليسيرول
  وأحماض دهنيّة », « ← جليكوز ») sont un rappel de 01-tamrin Q4 / quiz Q6 et suffisent à apparier ; la
  séquence des sucs, objet de la question selon le plan (« les protides digérés en deux temps »), n'est
  jamais nécessaire. Correctif :
  - énoncé : « (مناظرة 2012) تتحوّل الأغذية داخل القناة الهضميّة بمفعول العصارات الهاضمة. أنسب كلّ غذاء إلى العصارات التي تعمل عليه بالتّتابع. »
  - r1 « العصارة المعديّة في المعدة ثمّ العصارتان المعثكليّة والمعويّة في المعي »
  - r2 « العصارتان المعثكليّة والمعويّة في المعي وحدهما »
  - r3 « اللّعاب في الفم ثمّ العصارتان المعثكليّة والمعويّة في المعي »
  (paires inchangées ; chaque membre droit n'a plus qu'une séquence ; unique). L'explication peut garder
  les produits.
- **[MAJOR] Q7 d contredit le tableau.** « انتقلت المغذّيات من الدّم إلى تجويف المعي… فتزايدت كمّيّتها
  فيه » alors que l'intestin passe de 95 à 12 g. Correctif (la clé n'est plus la plus courte) :
  - b (clé, 98 car.) : « ما فقده المعي (83 غ) يساوي ما كسبه الدّم (83 غ): فالمغذّيات عبرت جدار المعي إلى الدّم، أي الامتصاص »
  - d (97 car., sans étiquette) : « ما فقده المعي (83 غ) يساوي ما كسبه الدّم (83 غ): فالمغذّيات عبرت جدار المعي إلى الدّم، أي الإفراز »
  - a (94) et c (92) inchangés. Plan 2×2 : lecture du bilan (juste en b/d, fausse en c) × nom du phénomène
    (juste en b seulement) ; d exécute la confusion de vocabulaire absorption/sécrétion.
  Dans l'explication, remplacer la fin par « …الامتصاص، لا الإفراز الذي تصبّ به الغدد عصاراتها في
  التّجويف. الخطأ الشّائع: أخذ القيمة النّهائيّة 88 مكان التّغيّر 83، أو تسمية العبور إلى الدّم إفرازًا. »
- **[MINOR] Q2.** d présuppose « الأنزيمات الموجودة في الأنبوب » quand le tube 1 n'en a aucune ; et
  « عديد البيتيد » (absent du cours) n'est pas glosé. Correctif : d = « لأنّه بلا عصارة هاضمة، والماء الذي
  فيه يوقف تفكيك المغذّيات المعقّدة ولو أُضيفت إليه الأنزيمات لاحقًا » (101 car. ; clé c 90, a 87, b 99 : la
  clé reste 2ᵉ plus courte) ; glose après le tableau : « (عديد البيتيد: جزيئة أقصر من جزيئة البروتيد) ».

**Point signalé : « غليسيرول » pour « كحول دهنيّة ».** Juste : le glycérol est un alcool (trialcool), et
« كحول دهنيّة » désigne aujourd'hui de longs alcools gras qui ne sont pas des produits de la digestion ; le
cours 05 (tableau des unités) dit « الغليسيرول والأحماض الدّهنيّة ». Mais R7 exige que la modernisation soit
dite dans l'énoncé (« بلغة الكتاب المدرسيّ الحاليّ : … »), et Q8 ne la dit pas. Avec le correctif de Q8
ci-dessus, les produits sortent des options : le terme ne reste que dans l'explication, où « غليسيرول » est
juste sans déclaration.

**Point signalé : la 9ᵉ question (anse avec maltose seul).** Juste et fidèle à l'esprit, mais sans source
et étiquetée 2016 : à supprimer (ci-dessus).

---

## m036 : `11-ad-dawra-al-jinsiya/exercices/10-examens-2015-ex3-2009-ex3-cycle-endometre-phases-synchronie.json` (d2, 7 q.)

Fidélité : 2009 ex. 3 (doc. 2 : huit repères, dont six gardés et renumérotés : col et cavité retirés ;
doc. 3 : coupe à glande enroulée et vaisseau sinueux), 2015 ex. 3 (intervalles 1–5, 5–14, 14–28 ; repères
1 = glandes, 2 = vaisseaux), 2017 ex. 1 item 2 (coupe à glandes tubulaires et vaisseaux, clé « تتزامن مع
الطّور اللّوتيني »), 2009 ex. 1 item 4 (reprise des quatre propositions) : conformes. Rendu Chromium à
232 px (figures de Q1, Q3, Q4, Q6) : lisibles. **Les figures de Q3 et Q6 sont le même dessin** (Q3 avec
repères, Q6 sans).

| Q | type | ma réponse | clé | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| 1 | matching d2 | 1-قناة البيض, 2-المبيض, 3-القمع, 4-المهبل, 5-العضليّة, 6-البطانة | idem | réserve | le trait du repère 6 s'arrête pile sur la limite muscle/muqueuse |
| 2 | mcq d2 | a | a | réserve | clé de 37 car. contre 64–75 : la plus courte de loin ; c ajoute « في الرّحم » qui n'est pas dans le sujet |
| 3 | matching d2 | 1-غدّة, 2-وعاء, 3-العضليّة, 4-التّجويف | idem | réserve | repères 3 et 4 ajoutés au dessin de 2015 (acceptable : couches dessinées) ; l'explication décrit la coupe de Q6 |
| 4 | mcq d2 | b | b | réserve | la clé est livrée par les items de Q7 (« طور ما بعد الحيض (من اليوم 5 إلى 14) »…) |
| 5 | mcq d2 | c | c | réserve | clé de 47 car. contre 63–68 ; l'énoncé décrit le شبيك et sa période (fuite partielle vers Q6) |
| 6 | mcq d3 | a | a | ERREUR de doublon | = 11/05-tadrib Q3 (« الشّبيك… يتكوّن في ») et quiz Q4, que la consigne interdit de redemander ; même dessin que Q3 dont l'explication donne la justification |
| 7 | matching d3 | l1-r2, l2-r3, l3-r1 | idem | réserve | ses membres gauches nomment les phases avec leurs jours : clé de Q4 |

Étage d2 avec Q6–Q7 en d3 : conforme à l'usage (07/07, 08/12 de la vague 1). Rampe 2-2-2-2-2-3-3 : OK.
Notions : toutes au cours 10 ou 11 (« قمع فالوب » au cours 10 § tableau des organes ; « الشّبيك » au cours
11 § phases utérines).

### Défauts m036

- **[MAJOR] Q6 : doublon interdit.** Une coupe à « glandes tubulaires sinueuses entourées d'un réseau dense
  de vaisseaux » → « طور ما قبل الحيض » : c'est 11/05-tadrib Q3 (« الشّبيك الرّحمي — غدد أنبوبيّة ملتوية تحيط
  بها شبكة كثيفة من الأوعية — يتكوّن في ») et le quiz Q4, que l'affectation nomme dans « ne pas
  redemander ». La moitié « justification » du 2×2 n'ajoute rien : la figure est celle de Q3, dont
  l'explication dit « أنبوب طويل ملتوٍ… وهو كثيف في هذه البطانة », et l'énoncé de Q5 la décrit aussi. La
  variante 2017 (« تتزامن مع الطّور اللّوتيني ») ne sauve pas la question : 11/07 Q4 (2025) et 11/04-defi Q5
  la posent déjà, et Q7 aussi. Correctif : **supprimer Q6** ; titre : « 🏛️ مناظرتا 2009 و2015 · بطانة الرّحم
  وطوراها المتزامنان ⭐⭐ » ; retirer 2017 ex. 1 item 2 des sources de la mission dans `gisement.json` (item
  écarté comme doublon). La mission garde 6 questions (Q1–Q5, Q7) : le minimum de R5 est tenu.
- **[MAJOR] Q7 → Q4.** Les membres gauches « طور ما بعد الحيض (من اليوم 5 إلى 14) » et « طور ما قبل الحيض
  (من اليوم 14 إلى 28) » donnent les noms des intervalles ب et ج que Q4 demande. Correctif : l1 « طور
  الحيض », l2 « طور ما بعد الحيض », l3 « طور ما قبل الحيض » (sans les jours) ; énoncé inchangé (il ne
  nomme aucune phase). Les paires restent uniques.
- **[MAJOR] Q2 : clé la plus courte de moitié.** 37 car. contre 64, 74 et 75 : les distracteurs ont été
  allongés, la clé est restée nue. Correctif, reprendre les propositions du sujet 2009 :
  b « تتميّز بحركة ذاتيّة » (19) · c « تتكوّن خلال الطّور اللّوتيني » (28) · d « تعيش أسبوعًا في المسالك
  الجنسيّة الأنثويّة » (42) ; clé a inchangée (37) : 3ᵉ sur 4. Cela retire aussi l'ajout « في الرّحم » de c,
  qui n'est pas dans le sujet et le rendait faux deux fois. L'explication reste juste.
- **[MINOR] Q5 : clé la plus courte** (47 contre 63–68). Correctif : c = « تهيّئ البطانة لاستقبال مضغة
  وتثبيتها فيها وتغذيتها إن حدث إلقاح » (63 car. : à égalité avec b, sous a et d 68).
- **[MINOR] Q1 : repère 6 ambigu.** Le trait (`x2="124" y2="140"`) s'arrête sur le bord gauche de la
  muqueuse (x ≈ 123 à y = 140), à égale distance de la musculeuse (5). Correctif : `x2="131" y2="142"`
  (dans la bande claire, entre le bord ≈ 123 et la cavité ≈ 140). Aucun déplacement d'organe.

**Point signalé : proximité des phases utérines avec 11/05 Q3 et le quiz Q4.** Tranché : **Q4** (nommer
les trois phases sur une courbe d'épaisseur découpée en intervalles) n'est pas un doublon : ni 05-tadrib Q3
ni le quiz Q4 ne demandent de lire la courbe, et 02-tamrin Q6 ne pose que la phase de reconstruction. **Q6**
en est un (ci-dessus, à supprimer). **Q5** frôle le même fait (le شبيك) mais demande son intérêt : c'est
la question 3 de 2015, à garder.

---

## m037 : `12-takawwun-al-janin/exercices/11-examens-2018-ex4-2013-ex5-calendrier-ovaire-endometre-grossesse.json` (d4, 11 q.)

Fidélité : 2018 ex. 4 (calendrier : avril 6–9, mai 2–5 et 28–31, juin sans règles ; femme mariée de 30 ans ;
dessins d'ovaire : avril, follicules à cavité de tailles voisines, ni corps jaune ni ovule ; mai, follicule
mûr, ovule hors de l'ovaire, corps jaune ; juin, corps jaune plus volumineux ; tableau d'épaisseur 4 → 7,4 mm
sur les jours impairs 1–29), 2013 ex. 5 (règles 1–5 avril et 1–5 mai ; plateau ~5,2 mm vers le 20 avril,
~5,3 mm vers le 21 mai, sans baisse au-delà du 30 mai) : conformes. SVG de Q3 (tous les points du tableau)
et de Q11 (chutes à ~1 mm vers le jour 6, plateaux, bandes de règles 1–5) rendus à 232 px : fidèles et
lisibles ; en Q11, les étiquettes de mois « 4 » et « 5 » au-dessus de la courbe se lisent comme des valeurs
d'épaisseur : [MINOR], écrire « أفريل » et « ماي » (l'énoncé les nomme déjà).

| Q | type | ma réponse | clé | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| 1 | mcq d2 | a (26 j) | a | ERREUR de doublon | = 11/09 Q5 (calendrier → cycle de **26** jours), même geste, même nombre |
| 2 | multi d2 | a, b | a, b | réserve | l'énoncé « لا ينضج أيّ منها » livre Q6 ; les deux clés ont le même gabarit de phrase, les trois distracteurs non |
| 3 | multi d2 | a, b, c | a, b, c | OK | 3 sur 6 ; +1 contre +0,4 vérifié ; 6 ≠ 3,7 |
| 4 | mcq d3 | c (13 mai) | c | ERREUR de doublon | = 11/09 Q6 (cycle de 26 jours → jour 12) ; b porte une étiquette alors qu'elle exécute deux erreurs |
| 5 | mcq d3 | b (23 juin) | b | réserve | clé de 29 car. contre 51–56 ; b et c affichent « زائد 26 يومًا » : livrent Q1 |
| 6 | mcq d3 | a | a | ERREUR de fuite | l'énoncé contient la clé (« جريبات… لا ينضج منها شيء » → « لم ينضج أيّ جريب ») |
| 7 | mcq d3 | b (juin) | b | réserve | clé livrée par l'énoncé de Q9 (« قيس سمك بطانة الرّحم في جوان… فتزايد باستمرار ») |
| 8 | multi d3 | a, b | a, b | réserve | « أيّ الفرضيّتين » annonce deux bonnes réponses |
| 9 | mcq d3 | d (حامل) | d | réserve | énoncé qui livre Q7 ; c (« في طور الحيض ») nie la prémisse « دون أن يظهر » |
| 10 | ordering d3 | a b c d e | a b c d e | réserve | ordre unique (nidation vers J+7, avant l'échéance du corps jaune) ; l'énoncé « لدى امرأة حامل… في جوان » donne la clé de Q9 |
| 11 | mcq d3 | c (16 avril, 16 mai) | c | OK | 2×2 propre (jour 16 contre jour du plateau) ; hypothèse déclarée |

Étage d4, rampe 2-2-2-3-…-3 : OK (usage vague 1). Notions : toutes au cours 11 (durée du cycle, J = durée −
14, facteurs « نفسيّة أو صحّيّة أو مناخيّة » au § 1, corps jaune, règles par baisse des hormones) et 12
(fécondation, nidation vers le 7ᵉ jour).

### Défauts m037

- **[MAJOR] Q1 et Q4 : doublons de gabarit de 11/09 Q5–Q6.** Calendrier de règles → cycle de 26 jours → ovulation
  au jour 12 : 11/09 (2021) pose exactement ces deux gestes avec **les mêmes nombres** (26 jours, jour 12),
  et 11/06-defi-concours Q1 le même calcul sur d'autres dates. Le plan a écarté le calendrier de 2012 pour
  ce motif ; celui de 2018 tombe sous la même règle pour ces deux questions. Correctif : **supprimer Q1 et
  Q4.** Q5 garde le calendrier (elle exige la durée du cycle, puis la prévision : geste neuf), et les
  explications de Q4/Q5 qui livraient « 26 » à Q1 n'ont plus de cible. La mission garde 9 questions.
  (Si l'orchestrateur garde Q4 : retirer l'étiquette de b, « اليوم 18… 19 ماي » = fin des règles + 14 jours,
  soit deux erreurs, qui doit rester muette.)
- **[MAJOR] Q6 : la clé est dans l'énoncé (et dans celui de Q2).** « جريبات متقاربة الحجم لا ينضج منها شيء »
  puis la clé « لم ينضج أيّ جريب ». « Aucun ne mûrit » est l'inférence demandée, pas une donnée du dessin
  (la transcription dit : follicules à cavité, tailles voisines). Correctif :
  - Q6 énoncé : « (مناظرة 2018) تبيّن رسوم المبيض لهذه المرأة في أفريل عدّة جريبات ذات تجويف متقاربة الحجم، ولا
    جسم أصفر في المبيض ولا بويضة خارجه، بينما يظهر في رسوم ماي جريب ناضج كبير التّجويف، رغم أنّ حيضها ظهر في
    أفريل أيّام 6 و7 و8 و9. ما السّبب المباشر لغياب الإباضة في أفريل؟ » (options inchangées) ;
  - Q2, ligne d'avril : « في أفريل: عدّة جريبات ذات تجويف متقاربة الحجم، ولا جسم أصفر في المبيض ولا بويضة خارجه ».
  Toutes ces données sont garanties par la transcription.
- **[MAJOR] Q9 → Q7, et Q10 → Q9.** L'énoncé de Q9 dit que l'épaisseur a été mesurée « في جوان » et croît
  sans baisse : c'est la clé de Q7. L'énoncé de Q10 dit « غياب الحيض في جوان لدى امرأة حامل » : c'est la clé
  de Q9. Correctifs :
  - Q9 énoncé (180 car.) : « (مناظرة 2018) هذه المرأة منتظمة الدّورة، ومرّ الموعد المنتظر للحيض في جوان دون أن
    يظهر، وظهر في رسم مبيضها لشهر جوان جسم أصفر أكبر حجمًا منه في ماي. ما حالتها الفيزيولوجيّة الأرجح؟ »
    (le corps jaune plus volumineux suffit à trancher entre retard et grossesse ; la transcription le garantit) ;
  - Q10 énoncé : « (مناظرة 2018) رتّب الأحداث التي تؤدّي إلى غياب الحيض عند حدوث حمل، من أوّلها إلى آخرها. »
    (items inchangés : l'ordre reste unique).
- **[MAJOR] Q9 c nie la prémisse.** « في طور الحيض » quand l'énoncé pose que les règles ne sont pas venues.
  Correctif (84 car. ; clé d 78, b 77, a 88 : la clé reste 2ᵉ plus courte) :
  c = « حامل: البطانة هي التي تفرز الهرمونات فتحافظ على الجسم الأصفر وتمنع ضموره فيغيب الحيض »
  (étiquette `bio.cycle.uterus-autonome` : l'utérus qui commande l'ovaire). Dans l'explication, remplacer
  « وطور الحيض يتهدّم فيه السّمك لا يتزايد » par « والمبيض هو الذي يقود البطانة بهرموناته، لا العكس ».
- **[MAJOR] Q8 : le duel annonce le nombre de bonnes réponses.** « أيّ الفرضيّتين » : on coche deux cases
  sans réfléchir au compte. Correctif : « …أيّ العبارات التّالية فرضيّة وجيهة تفسّر غياب الحيض في جوان؟ »
  (options inchangées).
- **[MINOR] Q2 : gabarit commun aux deux clés.** a et b suivent « يظهر في ماي … ولا يظهر في أفريل », aucun
  distracteur. Correctif pour e : « تظهر في أفريل بويضة خارج المبيض ولا تظهر في ماي » (même gabarit, faux :
  inversion des mois ; 2 bonnes sur 5 inchangé).
- **[MAJOR] Q5 : clé la plus courte de moitié, et vote sur « 26 ».** Clé b « 23 جوان: 28 ماي زائد 26 يومًا »
  (29 car.) contre 51–56 ; b et c affichent « زائد 26 يومًا » (la durée du cycle, clé de Q1). Correctif :
  options en dates nues, a « 25 جوان », b « 23 جوان » (clé), c « 26 جوان » (étiquette
  `bio.cycle.compte-depuis-la-fin-des-regles` gardée : 31 mai + 26), d « 28 جوان » ; toutes de 7 car. Le
  calcul reste dans l'explication, inchangée.

**Points signalés : le calendrier 2018.** Tranché. Le cycle d'avril dure bien 26 jours (6 avril → 2 mai :
24 + 2), comme celui de mai (2 → 28 mai) ; la mission ne l'utilise nulle part, et la « régularité » que pose
Q5 est confirmée par ces deux durées égales. L'absence d'ovulation en avril ne peut se lire que sur le
dessin (le calendrier montre un cycle d'avril normal, terminé par les règles du 2 mai) : c'est bien ce que
demande le sujet (« بالاعتماد على معطيات الوثيقة 3 وعلى إجابتك السابقة » : la comparaison des ovaires), donc
justification acceptable, **à condition** que l'énoncé décrive le dessin et non l'inférence (correctif de
Q6 ci-dessus).

**Points signalés : les dates calculées.** 13 mai : 28 − 2 = 26 jours, 26 − 14 = jour 12, jour 1 = 2 mai →
13 mai : **juste** (mais question à supprimer, doublon). 16 avril : règles le 1ᵉʳ avril puis le 1ᵉʳ mai,
cycle de 30 jours (avril en a 30), 30 − 14 = jour 16 → 16 avril : **juste**. 16 mai : la grossesse empêche
de mesurer le cycle de mai ; l'hypothèse « cycle de mai = cycle d'avril » est la seule qui permette la
réponse, elle est **déclarée dans l'énoncé** (« نفترض أنّ دورة ماي تدوم 30 يومًا مثل دورة أفريل ») et
conforme à « دورة منتظمة » : **juste et honnête**. Le distracteur « 20 أفريل و21 ماي » (début du plateau)
exécute une vraie erreur de lecture.

**Points signalés : les fuites jugées inévitables.** Mise en ordre de m037 (Q10) : sa fuite vers Q9 venait
de l'énoncé (« امرأة حامل… جوان »), **évitable** (correctif ci-dessus) ; ses items (corps jaune maintenu)
restent un fait du cours, acceptable. Explications de Q4/Q5 vers Q1 : sans objet si Q1 et Q4 sont supprimées ;
sinon, sur la route Q1 (d2) passe avant, et seules les options de Q5 posaient problème. Q8 → Q9 :
**acceptable** : Q8 garde deux hypothèses (grossesse **et** retard), elle ne tranche pas ; Q9 tranche par le
corps jaune plus volumineux, donnée absente de Q8.
