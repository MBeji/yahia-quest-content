# Journal du lecteur — anglais 6ᵉ, lot C07 à C12 (sessions 2020, 2019, 2018, 2017, 2016, 2015)

Étape G2, lecture du 2026-10-18. Les six PDF sont déjà téléchargés (`snapshots/6web/`) ; leurs sha256 recalculés égalent
ceux de `docs.json`. Scans sans couche texte (`pdftotext` quasi vide) : lecture en vision, une fois par page (150 DPI pour
2018-2020 ; 2015, 2016 et 2017 sont des pages surdimensionnées, 2227 × 2600 pt ou plus, rendues à 1500 px de large).
Aucune écriture git, rien sous `content/english-6eme/`.

## 0. CONVENTIONS APPLIQUÉES

Le § 0 de `JOURNAL-lecture-C01-C06.md` (6ᵉ) n'existait pas à la lecture ; ses six fichiers de lignes (`lines/C01–C06.tsv`)
et le § 0 du lot C14–C19 (même jour) m'ont servi de modèle, avec le § 0 de l'anglais 9ᵉ et la règle D2 du contexte.
**Aucune divergence avec le lot C14–C19**, sauf les deux points d'étage ci-dessous ; à réconcilier avec le pilote :

1. **6 lignes par épreuve** : reading = n°exo 1, barème 6, étapes = nombre de questions de premier niveau (3 sur les six
   sessions) ; langue = n°exo 2, 3, 4 (un par exercice imprimé) ; **« Writing » = deux lignes, n°5 et n°6** (comme C14–C19) :
   la partie ne contient aucune rédaction libre sauf 2019 et 2020, où le second exercice est un courriel guidé
   de quatre phrases (barème 4, étage `d3` comme les courriels C04–C06). Si le pilote garde « writing = UNE ligne » : fusionner
   n°5 et n°6 (barème 6, chapitres cumulés).
2. **Chapitre du reading** (D2) : thème 2020 nouvel élève aidé → `04-caring` ; 2019 école et musique, hobby → `01` ;
   2018 anniversaire (dialogue radio) → `05` ; 2017 anniversaire et cadeaux → `05` ; 2016 deux sœurs et le zoo (like, love
   playing) → `01` ; 2015 famille et routine après l'école (usually, plays) → `01`. Les structures embarquées (présent continu
   « are buying », 2017 ex. 3 « are … / sing » ; « can » ; « has got ») sont notées ici, non ajoutées à la ligne reading.
3. **Mots-clés HP** (ceux du lot C14–C19 et du pilote) : `HP:vocab-hors-guide` (contraires courants hors du champ « old ≠ new »
   de l'unité 07, collocations, maison, pièces, objets, orthographe, vocabulaire de description et de routine),
   `HP:present-continuous`, `HP:there-is-are`, `HP:wh-questions`, `HP:have-has`, `HP:personal-pronouns` (pilote C05). **Un seul
   nouveau** : `HP:going-to` (C08 n°5 : « going to » du futur proche, exclu du guide par la fiche). `HP:have-got` n'est pas posé : l'item
   donne la forme, il ne la teste pas (règle du lot C14–C19), sauf choix explicite have got / has got (C10 ex. 1 → `HP:have-has`).
   Chaque ligne cumule, dans l'ordre du manifeste, les chapitres des notions testées puis les jetons HP.
4. **Étages** (pilote) : reading `d1` (cocher, oui/non, tableau, compléter) ; cloze à banque, choix et appariement `d2` ;
   contraires et lettres en désordre `d1` ; mots en ordre, correction de fautes, dialogue à compléter `d2` ; courriel `d3`.
   Écart avec C14–C19 : ce lot-là classe cloze, choix et appariement en `d1`. À trancher par le pilote ; relire les `d2` en `d1` serait mécanique.
5. **Barème** : entiers partout (1 à 4) ; durée imprimée 45 min (séance de 9 h 30 à 10 h 15 en 2015-2019, « 45 minutes » en 2020) ;
   coefficient 1. Total 6 + 8 + 6 = 20 sur les six sessions.
6. **Texte support** : jamais en entier dans le dépôt. Transcription : référence (aucune imprimée), nombre de paragraphes et de
   mots (compté sur le snapshot), résumé de 2 phrases, mention du PDF officiel. Les phrases lacunaires, banques de mots, dialogues
   à compléter et mots à remettre en ordre sont des items : mot pour mot, lacunes `........`. Les mots imprimés en tête de réponse
   et barrés dans la liste des mots à ordonner (2019, 2020) sont transcrits `~~mot~~`.
7. **En-tête** : même YAML que le 9ᵉ ; `examen` = intitulé de `docs.json` suivi de l'intitulé arabe imprimé (« مناظرة الدخول إلى المدارس
   الإعدادية النموذجية ») ; `consulte_le: 2026-10-18` ; `lecture: vision`.

## 1. Documents lus

| id | session | sha256 (= registre ?) | pages | lecture | lignes | transcription |
| --- | --- | --- | --- | --- | --- | --- |
| C07 | 2020 | dee952d2b0b285844c67c3e8083c2e4bfb1513c6b8b740b27239b65be4bd2b22 (oui) | 2 | vision | 6 | `6eme-base/english/2020-unique.md` |
| C08 | 2019 | 92e9369b292604966377047c8b0809caafdd7303289437d141706bd63fa3bd60 (oui) | 2 | vision | 6 | `2019-unique.md` |
| C09 | 2018 | b9a14850851fbabdc5999389d60ccc2d77676ab7d258ad0858d7cd69ed7ed50c (oui) | 2 | vision | 6 | `2018-unique.md` |
| C10 | 2017 | b806efb38a02845c72b08b1b3d87abd281f00689805d325e475018047bb360af (oui) | 2 | vision | 6 | `2017-unique.md` |
| C11 | 2016 | af93240f8a25ccfe24e3fb99c68c45e7f276c8e0da50566573aecc805c258d35 (oui) | 2 | vision | 6 | `2016-unique.md` |
| C12 | 2015 | 8d48f3e3fb75d279fd09ba83f2c446d0c4cd27a1c30f92c5f64b0e4cd9e3e8a0 (oui) | 2 | vision | 6 | `2015-unique.md` |

Transcriptions sous `/home/user/wt-en6/content/programmes-officiels/examens-nationaux/6eme-base/english/`. Snapshots locaux complets
(texte support entier, hors dépôt) : `/tmp/claude-0/en6lec/snapshots/C{07..12}.txt`. Lignes : `lines/C{07..12}.tsv` + `.meta` ;
`content:gisement:lignes --subject english-6eme --grade 6eme-base --content /home/user/wt-en6/content` : **36 valides, 0 fautive**,
7 chapitres au manifeste.

## 2. Format de l'épreuve (identique sur les six sessions)

- 2 pages, **45 min**, **20 points : I. Reading comprehension (« The questions » en 2015-2018) 6 + II. Language 8 + III. Writing 6**.
- Page 1 : texte support de 75 à 110 mots, sans source imprimée (2018 : dialogue radio de neuf répliques, 80 mots) ; reading = **trois
  questions** de 1 à 3 points : cocher le titre ou la bonne réponse, vrai/faux ou oui/non, compléter une phrase, un tableau ou un
  paragraphe avec des mots du texte, associer (2015).
- Language : toujours 3 exercices : un cloze à banque avec un mot en trop (2 à 3 points ; 2016-2018) ou un choix entre deux ou trois formes
  (2015, 2017, 2019, 2020), des contraires (2015, 2016, 2019 : 2 points) ou un appariement (2015, 2017, 2018, 2020 : 3 points).
- « Writing » : deux exercices de 3 + 3 (2015-2018), 2 + 4 en 2019 et 2020 (mots en ordre, puis un courriel guidé de quatre phrases à
  un correspondant). Sinon : lettres en désordre (2016, 2018), mots en ordre (2015, 2017), correction de fautes (2015, 2017), dialogue à compléter
  (2018), appariement question-réponse (2016).

| session | texte (thème) | reading | langue (par exercice) | « writing » |
| --- | --- | --- | --- | --- |
| 2020 | nouvel élève et club de guitare | 3 q., 6 | appariement 3 ; cloze à banque 2 ; choix 3 | mots en ordre 2 ; courriel sur l'école 4 |
| 2019 | école internationale et leçon de musique | 3 q., 6 | choix 3 ; contraires 2 ; cloze à banque 3 | questions en ordre 2 ; courriel de présentation 4 |
| 2018 | dialogue radio, chanson d'anniversaire | 3 q., 6 | cloze à banque 3 ; choix 2 ; appariement (magasin) 3 | lettres en désordre 3 ; dialogue de la maison 3 |
| 2017 | famille qui prépare un anniversaire | 3 q., 6 | choix 2 ; cloze à banque 3 ; appariement (routine) 3 | correction de fautes 3 ; mots en ordre 3 |
| 2016 | deux sœurs et le zoo | 3 q., 6 | cloze à banque 3 ; contraires 2 ; choix 3 | lettres en désordre 3 ; appariement question-réponse 3 |
| 2015 | famille et routine d'un garçon | 3 q., 6 | choix 3 ; contraires 2 ; appariement 3 | correction de fautes 3 ; questions en ordre 3 |

## 3. Notions par chapitre (lot C07-C12, 36 lignes)

| chapitre | lignes où il apparaît |
| --- | --- |
| 01 entertaining-myself | readings C08, C11, C12 ; C07#4 (and, possessif), #5 (like -ing), #6 ; C08#2 (because), #6 ; C09#2 (like -ing, favourite), #3 (swimming) ; C10#4, #5 (lives), #6 ; C11#2, #4 ; C11#6 ; C12#4, #5 (usually, on/in temps) |
| 02 keeping-fit | C07#2, #5, #6 (How many) ; C08#5, #6 ; C09#3 (can't) ; C11#6 ; C12#6 |
| 03 seasons | C08#3 (cold ≠ hot) ; C09#5 (rainy) |
| 04 caring | reading C07 seul |
| 05 celebrations | readings C09, C10 |
| 06 shopping | C07#2 (vêtements) ; C09#4 (dialogue de magasin) ; C11#5 (clothes) ; C12#6 (would like, phone number) |
| 07 around-the-world | C09#5 (north) ; C10#5 (nationalité) ; C11#3 (new ≠ old) ; C12#2 (from) |

Le passé simple (05, 06), will/won't (03), le comparatif et le superlatif (03, 04, 07), should/must (02), les articles, la suggestion
et l'impératif ne sont **jamais testés** sur 2015-2020 ; l'ensemble tient dans le champ de l'unité I (like, présent, possessifs) et dans le
vocabulaire de base.

## 4. Part HP et « ancien programme »

HP posés sur **22 lignes de 36 (61 %)** : `HP:vocab-hors-guide` 14, `HP:present-continuous` 4, `HP:there-is-are` 4, `HP:wh-questions` 4,
`HP:going-to` 1, `HP:have-has` 1, `HP:personal-pronouns` 1. Les six lignes de reading : aucune HP (thème rattaché à une unité). Les
`.meta` portent `programme: ancien` pour 2020, 2019 et 2017 (4 lignes HP sur 6) et `mixte` pour 2018, 2016 et 2015 (3 ou 4 lignes
HP). Le **présent continu** et **there is/are** sortent du guide actuel (« Learn and Grow ») comme dans le lot C14–C19 ; le lexique de base
(maison, animaux, contraires, routine, description) en est le principal écart. Le noyau reste dans le guide : like + -ing, adverbes de
fréquence, -s du présent, possessifs, how many, would like, vêtements, achats.

## 5. Difficultés et points à arbitrer

- **Ex. « have got »** (C07#2 « I've got », #3 « has got », C10#1) : la structure n'est pas un encadré du guide ; non posée en HP
  quand l'item donne la forme (appariement par sens, choix entre « got / get / go » : le verbe testé est le lexical « got »), posée `HP:have-has`
  dans le seul cas où le choix est entre deux auxiliaires.
- **C07 n°5** (mots en ordre) : un item de présent continu, un d'heure prévue (rangé sans chapitre), un « like + -ing », un « How many … have you got ».
- **C08 n°5** : trois questions avec « going to » (HP:going-to) et un « Are you ready … ? » sans chapitre. Le reading de 2019 est rangé en `01` (hobby,
  matière préférée) ; le thème « école » n'est dans aucune unité.
- **C09 n°6** (dialogue de la maison) : aucun chapitre : « What's there in … », « Where's … », « What colour … ».
- **C11 n°6** : appariement question-réponse qui cumule cinq jetons (le plus lourd du lot) ; « I'm having lunch » en présent continu.
- **Contraires** : « new ≠ old » rangé en 07 (guide, champ « old ≠ new ») ; « cold ≠ hot » en 03 (météo) ; small ≠ big, right ≠ left en HP.
- **Ordre des lettres** : 2018 « town / north / rainy » : town en HP, north en 07, rainy en 03.
- **Coquilles ou particularités imprimées** : 2015 et 2016 en-tête arabe de l'épreuve sur la page 2 (la page 1 n'a pas de cadre d'épreuve en 2016) ;
  2018 : « sister' s » avec espace dans le texte lacunaire ; 2020 : l'adresse du destinataire
  est « Linda.Smith@gmail.uk » ; premier mot déjà imprimé sur la ligne de réponse (barré dans la liste, 2019 et 2020) ; aucun corrigé publié, la transcription ne
  donne aucune réponse.
- **Lisibilité** : bonne sur les douze pages ; aucun `[illisible]`.
