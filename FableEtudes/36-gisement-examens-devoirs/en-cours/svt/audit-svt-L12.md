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
