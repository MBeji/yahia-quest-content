# Journal du lecteur — anglais 9ᵉ, lot C19 à C30 (sessions 2017, 2016, 2015, 2013, 2012, 2011 ; générale et technique)

Étape G2, lecture du 2026-10-16. Conventions : § 0 de `JOURNAL-lecture-C01-C06.md`, reprises à la lettre (grain, n°exo 1 / 2-4 / 5,
chapitres, HP, étages, texte support résumé, barèmes décimaux gardés). **Pas de session 2014 dans ce lot** (hors liste). Les douze PDF sont des
scans sans couche texte (`pdftotext` rend 4 octets) : lecture en vision, 150 DPI, une fois par page. Les douze sha256 téléchargés (`curl -g`,
http, sans `-k`) égalent ceux de `docs.json`. Aucune écriture git, rien sous `content/english/` hors les douze transcriptions, ni `gisement.json`
ni `lignes.tsv`.

## 1. Documents lus

| id | session | filière | sha256 (= registre ?) | pages | lecture | lignes | transcription |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C19 | 2017 | générale | 7cdea2f3…14452d6 (oui) | 4 | vision | 5 | `english/2017-generale.md` |
| C20 | 2017 | technique | 56c5eb21…adba (oui) | 4 | vision | 5 | `english/2017-technique.md` |
| C21 | 2016 | générale | ab149ec7…401b (oui) | 4 | vision | 5 | `english/2016-generale.md` |
| C22 | 2016 | technique | 7cbcf3af…4ff (oui) | 4 | vision | 5 | `english/2016-technique.md` |
| C23 | 2015 | générale | 2d5d5a57…3a32 (oui) | 4 | vision | 5 | `english/2015-generale.md` |
| C24 | 2015 | technique | 78cbef86…1db (oui) | 4 | vision | 5 | `english/2015-technique.md` |
| C25 | 2013 | générale | 8ed7a8b8…1d08 (oui) | 4 | vision | 5 | `english/2013-generale.md` |
| C26 | 2013 | technique | aa58d387…2b72 (oui) | 4 | vision | 5 | `english/2013-technique.md` |
| C27 | 2012 | générale | 725e1ab4…37d8 (oui) | 4 | vision | 5 | `english/2012-generale.md` |
| C28 | 2012 | technique | 4b8eabb9…7867 (oui) | 4 | vision | 5 | `english/2012-technique.md` |
| C29 | 2011 | générale | 37a9ad5a…30ac (oui) | 4 | vision | 5 | `english/2011-generale.md` |
| C30 | 2011 | technique | bbecf8b4…4327 (oui) | 4 | vision | 5 | `english/2011-technique.md` |

Sha complets : ceux de `docs.json` (comparés par programme, 12 égalités). Transcriptions sous
`/home/user/wt-en/content/programmes-officiels/examens-nationaux/9eme-base/english/`. Snapshots locaux (hors dépôt) :
`/tmp/claude-0/enlec/snapshots/C{19..30}.txt` (textes supports seuls). Lignes : `lines/C{19..30}.tsv` + `.meta`
(60 lignes ; `content:gisement:lignes --subject english --grade 9eme-base --content /home/user/wt-en/content` : **60 valides, 0 fautive**).
Un premier passage a rejeté 7 archétypes de reading de 17 à 20 mots (limite 16) : raccourcis.

## 2. Format de l'épreuve — ce qui change par rapport au § 0

Trois blocs de l'épreuve, 1 h, coefficient 1, 4 pages, total sur 20 : **générale 6 + 8 + 6, technique 8 + 7 + 5** (identique au pilote, toutes sessions).
Reading = une ligne (n°exo 1), langue = trois exercices (n°exo 2, 3, 4), writing = une ligne (n°exo 5) : la grille du § 0 s'applique partout.
Écarts relevés, rangés au plus proche du § 0 :

- **Nombre de questions de compréhension** : 5 en 2017, 2016, 2015 ; **4 en 2013, 2012, 2011 (générale), 4 en 2013 technique, 6 en 2012 technique, 5 en 2011
  technique**. Étapes = nombre de questions imprimées (4, 5 ou 6).
- **Nature du texte** : article de presse en général ; **lettre** (C23, 2015 G, quatre paragraphes) ; **extrait de roman classique** à la première
  personne (C27, 2012 G) ; **récit de presse en cinq paragraphes numérotés « 1- »…« 5- »** (C29) ; textes de 2013-2012 techniques plus courts
  (120 à 175 mots). C22 (2016 T) : trois paragraphes **non numérotés** à l'impression alors que les questions renvoient aux « paragraph 1/2/3 ».
- **Barèmes** : tous les barèmes de langue imprimés sont en demi-points. Décimaux gardés (2.5, 1.5) : C20#2, C22#2, C23#3, C24#2, C24#4, C26#2, C26#3, C28#2,
  C28#3, C25#4=2 (entier), C30#3=2.5, **C30#4 = 1.5** (appariement de trois items seulement, 3 + 2.5 + 1.5 = 7). Aucun barème par item n'est
  imprimé aux exercices 1 et 2 de C30 : 0.5 par déduction (6 lacunes = 3 ; 5 items = 2.5).
- **Appariement** : de 2013 à 2011 la consigne ajoute « the parts in column A are in the correct order » (C25 ex. 3, C27 ex. 3, C29 ex. 2) ; l'appariement
  vaut 2 ou 2.5 points selon l'effectif (**5 items et 6 parties en B** en C23 et C27, 2.5 points) ; en C26 et C28, ce sont **quatre phrases indépendantes**
  (« get 4 coherent sentences »), non un paragraphe. Rangés tous en `09` seul comme au § 0.
- **Production** : mots d'aide imprimés dans toutes les sessions 2015-2011 (listes de mots ou de formules) ; **lettre ou courriel pré-rempli** (C19, C20, C26,
  C27, C28, C29) ; **dépliant de règles** (C30). Le nombre de lignes (8, 10, 12) varie ; consigne d'anonymat absente en C30.
- **Mise en page ancienne (2013 et antérieures)** : page 1 réduite au texte, en-tête officiel répété en page 2, bandeaux « Ne rien écrire ici » absents ;
  C26 porte un renvoi en arabe (« انظر الصفحة الموالية »). Décimales à virgule en C26 et C28 (« 0,5X5 = 2,5 marks ») et en C29 (« 0,5 x 4 »).
- **Étage** : reading général `d2`, reading technique `d1` (C20, C22, C24, C26, C28, C30), cloze/choix/appariement `d2` ; un cloze 100 % lexical à banque
  (C27 ex. 1) `d1` ; writing générale `d3`, technique `d2`. Aucun `d4`.

| session / filière | reading | langue (par exercice) | writing |
| --- | --- | --- | --- |
| 2017 G | 5 q., 6 pts, article (famille et partage) | lacunes à banque 3 ; appariement 2 ; choix 3 | discours de remerciement (6) |
| 2017 T | 5 q., 8 pts, article (chantier) | banque à 2 intrus 2.5 ; appariement 2 ; choix 2.5 | courriel de conseils (5) |
| 2016 G | 5 q., 6 pts, article (adolescent) | banque 3 ; appariement 2 ; choix 3 | article de conseils (6) |
| 2016 T | 5 q., 8 pts, texte court non numéroté | banque 2.5 ; appariement 2 ; choix 2.5 | article de précaution (5) |
| 2015 G | 5 q., 6 pts, **lettre** | banque 3 ; appariement 2.5 (5 items) ; choix 2.5 | article incitatif avec mots d'aide (6) |
| 2015 T | 5 q., 8 pts | banque 2.5 ; appariement 2 ; choix 2.5 | article de conseils, mots d'aide (5) |
| 2013 G | **4 q.**, 6 pts | banque 3 ; choix 3 ; appariement 2 | article de conseils, mots d'aide (6) |
| 2013 T | **4 q.**, 8 pts | banque 2.5 ; choix 2.5 ; appariement 2 | lettre de conseils (5) |
| 2012 G | **4 q.**, 6 pts, **roman classique** | banque 3 ; choix 2.5 ; appariement 2.5 | courriel d'aide à choisir (6) |
| 2012 T | **6 q.**, 8 pts | banque 2.5 ; choix 2.5 ; appariement 2 | courriel descriptif (5) |
| 2011 G | **4 q.**, 6 pts, 5 paragraphes | banque 3 ; appariement 2 ; choix 3 | lettre de loisirs (6) |
| 2011 T | 5 q., 8 pts | banque 3 ; choix 2.5 ; appariement **1.5** | dépliant de règles (5) |

## 3. Notions par chapitre (lot C19-C30, 60 lignes)

| chapitre | lignes où il apparaît |
| --- | --- |
| 01 present tenses | C24#4 (provides), C25#2 (is), C28#2 (is showing), C28#3 (downloads), C29#4 (check), C30#2 (places) — 6 lignes |
| 02 past tenses (+ present perfect) | C20#2 (has worked), C21#2 (borrowed, gained), C21#4 (found/founded), C22#4 (have learned), C23#4 (were moving), C24#2 (turned), C25#2 (saw), C25#3 (started), C26#2 (hasn't got), C26#3, C27#3 (has done) — 11 lignes |
| 03 future | C27#3 (will join) — 1 ligne |
| 04 modals | C19#2 (might), C20#4 (can't + base), C24#2 (could) ; production : C20, C21, C22, C24, C25, C26, C30 (conseiller, avertir, règles) — 10 lignes |
| 05 conditionals | jamais testé en langue ; reading C21 q5 (« If you were one of… ») rangé `09` seul, voir § 4 |
| 06 passive voice | C20#4 (considered) — 1 ligne |
| 07 reported speech | jamais |
| 08 relatives & comparatives | C19#4 (biggest), C21#2 (bigger), C21#4 (most), C22#2 (larger), C23#2 (as, better), C28#3 (who), C29#2 (faster, who, those), C29#4 (funnier/fun) — 8 lignes |
| 09 reading & writing | douze readings, douze writings, tous les appariements, les lexicaux |
| 10 exam-style | non employé |

**Part HP** : aucune ligne entièrement HP ; **6 lignes sur 60** portent un jeton HP en complément : `HP:word-formation` (C25#3 interested/interesting ; C29#4
careful/carefully/care), `HP:gerund` (C23#2 « before having »), et **deux mots-clés nouveaux** (cas nouveaux, au plus proche des deux fixés) :
`HP:object-pronoun` (pronom personnel complément he/his/him, they/her/them : C26#3, C28#3) et `HP:reflexive-pronoun` (myself/himself/herself : C23#4).
Les pronoms ne sont enseignés par aucun des dix chapitres ; ils restent un signal minoritaire (3 lignes).

Chapitres jamais testés en langue sur 2017-2011 (hors 2014) : 05 et 07 ; 03 et 06 une seule fois chacun. Le profil 2011-2017 est donc plus
« mots et prépositions » que 2024-2026 : appariements, vocabulaire en contexte, collocations (proud of, look for, take care) dominent.

## 4. Doutes de classement (à trancher par le pilote)

- **Valeur modale embarquée dans le reading** : C25 q4 (« have to » = obligation), C28 q5 (« I strongly believe » = opinion/conseil/obligation) testent la fonction
  d'un énoncé, comme C02 q3 et C06 q4 au pilote : gardés `09` seul.
- **Cadre « If you were… »** : C21 q5 (« If you were one of Stephen's supporters, what other action(s) would you take ») appelle un conditionnel irréel, comme C01 q5 et
  C03 q5 au pilote : `09` seul, `HP:conditional-2` non posé (même réserve).
- **Production avec « rules »** (C30) : classée `+04-modals` (règles de sécurité = obligation/interdiction), au plus proche de « conseiller, avertir, dire ce qu'on peut faire » ;
  C27 (« help him decide ») et C28 (« describe ») : `09` seul ; C23 (« encourage », persuasif) : `09` seul. C19 (discours de remerciement au passé) : `09` seul,
  `+02` non ajouté, la consigne n'imposant pas de récit.
- **C22#4** (« hearing problems ») : gérondif + nom, enseigné au guide : rangé `09`, pas de `HP:gerund`. `learned` (have learned) : `02`.
- **C26#2/C25#3** : participes adjectivaux (interested/interesting) rangés `HP:word-formation` comme au pilote (C01#3) ; hésitation faute de chapitre.
- **C21#4 « found / find / founded »** : verbe lexical au prétérit (found = fonder, founded) : `02` retenu (forme passée requise).
- **C27#2** : tous les items sont lexicaux (look for, sell, favourite, share, partner, holidays) : `09` seul, `d1` (cloze à banque guidée tout lexical, cf. C04).
- **C20#2 / C24#2** : « has worked » (present perfect) et « turned » + « could » sont les seuls items grammaticaux d'un cloze presque lexical : `02` (et `04`) ajoutés
  par la règle « au moins un item », `09` conservé car plus de la moitié des items est lexicale.
- **C30#3** : cinq items, tous des prépositions ou des mots de champ lexical (at, welding, tools, workshop, of) : `09` seul.
- **C22 (texte non numéroté)** : questions renvoyant à des paragraphes que le scan ne repère pas ; paragraphes comptés par les alinéas.

## 5. Difficultés

Aucune de lecture : douze scans nets (2017-2015 en jaune ou gris, 2013-2011 en noir et blanc), aucune zone illisible, aucun item `[illisible]`, aucune marque
`[hors programme en vigueur]` posée (les notions testées : prépositions, appariements, temps, comparatifs, modaux, un passif, un futur). Le texte de C27 est un
extrait de roman du XIXᵉ siècle (domaine public) : traité comme les autres textes supports, résumé seul. Aucune consigne n'a vieilli. Aucun corrigé n'est publié avec ces
sujets : les transcriptions ne donnent aucune réponse ; les banques de mots sont reproduites dans l'ordre imprimé. Deux coquilles imprimées conservées telles quelles :
« 2,5 marks » avec virgule et la numérotation « 0,5X5 » (C26, C28, C29) ; « Comosun College » (C24, texte résumé sans cette graphie) ; « stationeries » (C25 ex. 3).
La partie Language de C30 n'imprime aucun barème par item aux exercices 1 et 2.
