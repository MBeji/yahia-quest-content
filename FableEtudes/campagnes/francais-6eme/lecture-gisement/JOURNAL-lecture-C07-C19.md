# Journal du lecteur — français 6ᵉ, lot C07 à C19 (sessions 2020 à 2008, épreuve unique)

Étape G2. Deuxième lot d'examens, lecture du 2026-10-19. `C13` (2014) et `C16` (2011) sont introuvables au registre
et n'ont pas été cherchés. Onze documents : dix scans lus en vision (150 DPI, une fois par page), et 2008 avec couche
texte (`pdftotext -layout`, page 5 vérifiée vide). Les onze sha256 des copies de `/tmp/claude-0/fr6g/src/` égalent
ceux de `docs.json` et du registre. Aucune écriture git, rien sous `content/french-6eme/`, `gisement.json` intact.
Conventions du § 0 du journal C01–C06 reprises telles quelles (grain, n°exo = rang, placement F4, jetons HP,
étages) ; seuls les ajouts ci-dessous sont nouveaux.

## 0. CONVENTIONS ET AJOUTS

- **Barème** : dans ce lot AUCUN sujet ne l'imprime sauf 2020 (1 point par question, 2 à la question 4 a + b, 6 + 3 + 3
  + 8 imprimés). Pour 2019 à 2008, colonne `-` partout ; la **production vaut 8 par la convention du lot** (le
  total « 20 » est imprimé en page 1 ou 2 mais pas la répartition) : c'est une inférence, signalée dans chaque `.meta`.
- **Grain** : une question numérotée à sous-parties a/b/c/d reste UNE ligne (2015 Q1 a-d : 5 étapes ; 2016 gram. 1 a/b).
  Rangs : compréhension 1…n, grammaire n+1…, conjugaison, production en dernier. Total 116 lignes : 12 (2020), 11
  (2019), 12 (2018), 9 (2017), 11 (2016), 10 (2015), 10 (2013), 11 (2012), 10 (2010), 10 (2009), 10 (2008).
- **Placement** : compréhension = module du thème du texte ; production = module du thème de la consigne. Elle
  diffère du texte quand la consigne change de thème : 2020 (texte 04, production 02 : recours à Internet), 2018 (texte
  08, production 05 : action contre la pollution), 2009 (texte 03, production 07 : spectacle raté).
- **Jetons HP nouveaux** (à reprendre par les autres lots) : `HP:cod` (« complément d'objet direct » nommé, typologie
  fine exclue § 2.10 D) ; `HP:voix-passive` (accord d'un participe dans une phrase passive, support de tableau C) ;
  jetons déjà fixés réemployés : `HP:pronom-complement`, `HP:adjectif-if-ive`, `HP:discours-indirect`.
- **Étages** : conjugaison à une seule réponse = `d1` (2016 Q9-10, 2009 Q9, 2008 Q9) ; `d3` pour trois réponses ou plus
  mêlant deux notions ; compréhension `d1` une seule fois (2012 Q1, relevé direct).
- **Verbes hors liste** (aucune étiquette de chapitre ajoutée, notés ici) : sourire, attendre, partir, réfléchir,
  entendre, installer… relèvent du 3ᵉ groupe sans verbe-type ; le chapitre porté est celui du temps (`01`).
- **Éléments de forme** : les sujets de 2019 à 2008 impriment « de 8 h à 9 h » (au lieu de « ساعة » ou « ساعة واحدة ») ;
  le coefficient n'apparaît qu'en 2020, 2019, 2018 et 2017 ; le cadre « لا يكتب شيء هنا » manque en 2016 à 2008.

## 1. Documents lus

| id | session | sha256 (= registre ?) | pages | lecture | lignes | transcription |
| --- | --- | --- | --- | --- | --- | --- |
| C07 | 2020 | a64a3c7ab6877705051875db426b441fa58a3f3958b8b5a930092878597b9ec7 (oui) | 4 | vision | 12 | `french/2020-unique.md` |
| C08 | 2019 | 88a2b5b5a3db9df3dba9d98e36d39253a4fd06b8cf77c3434a2fdfd420e8c14a (oui) | 4 | vision | 11 | `french/2019-unique.md` |
| C09 | 2018 | 28cdea068b0069e12c2779e9024e8edb9f609d9269c708def4f7bd88f300344b (oui) | 4 | vision | 12 | `french/2018-unique.md` |
| C10 | 2017 | f7b79ad31598a43749bc9446549c18f028412ed64aae64230502d5eb61740a66 (oui) | 4 | vision | 9 | `french/2017-unique.md` |
| C11 | 2016 | 86426673d670ce29d89a7720407791372573512bab3b2de67168bcaf63dee9ef (oui) | 4 | vision | 11 | `french/2016-unique.md` |
| C12 | 2015 | 5ddf109be933cfec35689de3528129252a991d48bb11424cf5892c1813c85b17 (oui) | 4 | vision | 10 | `french/2015-unique.md` |
| C13 | 2014 | introuvable | - | - | 0 | - |
| C14 | 2013 | b671f618d4575ad5ca1e1150e7cd56bd2275cf06efff33605d61bb37c2553e02 (oui) | 4 | vision | 10 | `french/2013-unique.md` |
| C15 | 2012 | 164079174738d769459cb92deeec6538a5531049f33a516778a39b534e550c3c (oui) | 4 | vision | 11 | `french/2012-unique.md` |
| C16 | 2011 | introuvable | - | - | 0 | - |
| C17 | 2010 | d46788f8eab4270ce0b39d8cff138477e63c90bd68aceacd024c1be8d42fca23 (oui) | 4 | vision | 10 | `french/2010-unique.md` |
| C18 | 2009 | fd5d59fc6f3d668a1622ab915f354a33d46225540e60e391dd7eea28f34cb8ce (oui) | 4 | vision | 10 | `french/2009-unique.md` |
| C19 | 2008 | 174621c2fa6fdda0a7c4cacc44182f5d93975e4c6d20b91afe3efb8b8b305bd9 (oui) | 5 | pdftotext | 10 | `french/2008-unique.md` |

Transcriptions sous `/home/user/wt-fr6b/content/programmes-officiels/examens-nationaux/6eme-base/french/` (texte support
résumé, consignes et items mot pour mot, coquilles conservées). Lignes : `lines/C07 … C19.tsv` + `.meta` (sans C13, C16).
Validation : `content:gisement:lignes --subject french-6eme --grade 6eme-base` : 11 fichiers, 116 lignes, 116 valides,
0 fautive. Aucun corrigé n'est publié : les transcriptions ne donnent aucune réponse.

## 2. Format par session

Une heure (8 h à 9 h), 20 points, 4 pages (5 en 2008, la dernière vide) ; un texte narratif page 1 ; les quatre mêmes
parties, SANS numérotation romaine ni totaux de partie en 2019 à 2008.

| session | texte (thème, module) | compréhension | grammaire | conjugaison | production |
| --- | --- | --- | --- | --- | --- |
| 2020 | arbre et entraide via Internet (04) | 5 q. : détail, 2 indices, cause, synonymes/contraires (2 pts), avis | infinitif après à/sans ; pluriel + démonstratif/possessif ; tableau GN/GV/épithète/attribut | futur ; impératif ; passé composé (prendre, finir, mettre) | récit ≥ 8 phrases, désaccord livre/Internet (02) |
| 2019 | aide à un inconnu (04) | 4 q. : attirance, cause, lexique a/b, espoir | tableau lieu/temps/manière ; genre + accords ; négation | pc avec être + négation ; futur ; impératif | récit ≥ 8 phrases, dispute des parents (04) |
| 2018 | grand-père conteur en classe (08) | 5 q. : vrai/faux + phrase ×2, lexique, avis | attribut ; tableau avec « COD » ; forme affirmative | futur ; impératif sg/pl ; pc d'aller + vouloir | récit ≥ 8 phrases, dialogue + description (05) |
| 2017 | accueil d'une élève muette (03) | 3 q. : coche + phrase, lexique a/b, réaction | tableau ; accords ; compléments non essentiels | futur ; impératif sg/pl (2 q. seulement) | récit ≥ 8 phrases, accepter une camarade (03) |
| 2016 | crayons et exclusion du gris (03) | 4 q. : coche, qui dit, lexique, avis | attribut/épithète + pronom ; lieu + temps | impératif ; pc/futur d'être, pouvoir (4 q.) | récit ≥ 8 phrases, enfant handicapé seul (03) |
| 2015 | aide à un enfant pauvre et aveugle (04) | 3 q. (1 à 4 sous-q.), lexique, avis | tableau 4 fonctions ; accords ; démonstratif/possessif | présent ; pc avec être ; futur | récit ≥ 8 phrases, parents qui aident (04) |
| 2013 | télévision à la maison (02) | 3 q. : détails, lexique, prédiction | tableau 4 fonctions ; accords ; chère maman | présent ; futur ; pc | récit ≥ 8 phrases, ami devant la télé (02) |
| 2012 | chasse aux oiseaux (05) | 4 q. : état, indice, lexique, avis | essentiel/non essentiel ; accords ; dire/réussir | pc et futur ; présent vous ; impératif | récit ≥ 8 phrases, libérer un oiseau (05) |
| 2010 | jeune bricoleur (07) | 3 q. : phrases, lexique ×4, avis | essentiel/non essentiel ; passif invité ; accords | pc ; futur ; présent nous | suite : fin d'une scène ratée (07) |
| 2009 | spectacle d'une élève étrangère (03) | 3 q. : choix, lexique a/b, avis | manière + temps ; accord ; déplacer les compléments | pc ; impératif ; futur de faire | suite : fin d'un spectacle raté (07) |
| 2008 | téléphone portable à l'école (02) | 3 q. : 2 relevés, 4 synonymes, avis | GV + non essentiel ; parole directe ; pronoms | pc ; futur ; vouloir au présent | suite : ce que dit l'enfant aux parents (02) |

Constantes : une question de lexique (synonymes, souvent contraires dès 2020) et une question d'avis en compréhension ;
une production d'au moins huit phrases avec dialogue (une « suite » ou une « fin de scène » en 2010, 2009, 2008).
La compréhension va de 3 à 5 questions ; la conjugaison de 2 à 4 questions (2017 : 2 ; 2016 : 4).

## 3. Notions par chapitre (116 lignes)

Lignes portant le chapitre : 01 : 31 ; 02 : 22 ; 03 : 18 ; 04 : 20 ; 05 : 27 ; 06 : 24 ; 07 : 18 ; 08 : 23. Le temps et les
verbes en -er (01), les compléments (05, 06, 07, 08) et le futur d'aller (06) sont les plus sollicités ; rarement
testés : l'homophonie (aucune occurrence), l'infinitif après à/de/par/pour/sans (une seule fois, 2020 Q6), dire/lire/écrire
(2018 écrire à l'impératif, 2012 dire). **Part HP** : 6 lignes sur 116 portent un jeton (2018 : 1 ; 2016 : 1 ; 2015 : 1 ;
2010 : 1 ; 2008 : 2) ; aucune n'est HP seule. **Programme ancien** : aucun sujet n'est « ancien » au sens fort ; cinq sont `mixte` (2018, 2016, 2015, 2010, 2008, pour une notion hors fiche chacun) et six `en vigueur` (2020, 2019, 2017, 2013, 2012, 2009).

## 4. « Programme ancien » et jetons

- **2018 gram. 2** : « Complément d'objet direct » nommé dans un tableau (typologie fine exclue de la fiche) : `HP:cod`,
  programme ancien ; les compléments de manière et de lieu sont étiquetés `08` et `06`.
- **2016 gram. 1** : « Mon crayon jaune est bien autoritaire. J'aime bien mon crayon jaune. » ; reprise par pronom
  (`HP:pronom-complement`). Le futur de pouvoir (conj. 3) n'est pas enseigné (pouvoir au présent seulement) ; rattaché `08`.
- **2015 gram. 2** : alternance -if/-ive (attentif/attentive) : `HP:adjectif-if-ive`. La grammaire 1 porte un verbe au passé
  simple (« suivit ») sans l'évaluer : pas de `HP:passe-simple`. Le texte est au passé simple (support).
- **2010 gram. 2** : « qu'ils sont invités » → « qu'elle est invitée » : accord dans une phrase passive,
  `HP:voix-passive` (tableau C), `08` pour l'accord avec être.
- **2008 gram. 2 et 3** : la consigne introduite par deux-points demande la parole directe (« Venez accompagnés de l'un
  de vos parents ») : `HP:discours-indirect` (lecture à confirmer) ; pronoms personnels pour éviter les répétitions :
  `HP:pronom-complement`. La session ne propose que des synonymes (pas de contraires).

## 5. Difficultés et doutes

- **Barème** : un seul sujet (2020) imprime les points. Production à 8 par convention pour les dix autres (inférence).
- **2017** : compréhension de 3 questions, conjugaison de 2 : 9 lignes seulement ; vérifié, la page 3 se termine après
  la conjugaison 2 (pas de page manquante).
- **2016 conj. 2** : « La veille, vous ........ tristes » : le passé composé (« avez été », `01+03`) est attendu mais
  l'imparfait (`HP:imparfait`) reste possible ; clé non publiée. Idem pour la phrase de la question 4 de grammaire.
- **2016 gram. 1** : question à deux sous-parties (attribut/épithète, reprise) : une seule ligne (3 étapes).
- **2015 comp. 1 a-d** : quatre sous-questions sous un seul numéro : une ligne, 5 étapes.
- **2013 gram. 3** : « Chère maman » : accord cher/chère (modèle fier/fière, `06`) ; **2009 gram. 1** : « un peu angoissés »
  est apposé au sujet : complément de manière attendu, ambiguïté de nature, rangée `07+08`.
- **2018 gram. 1** : « solides et fortes » devenus « solide » et « fort » : attributs au masculin singulier, `03+06`.
- **Thème du texte** : 2018 (grand-père et désert, `08`, `03` possible), 2009 (élève étrangère moquée, `03`, `08` possible),
  2020 (arbre et Internet : texte `04`, `05` possible), 2015 (aide à un enfant pauvre, `04`).
- **Textes tirés de manuels** : 2016 (« Lecture CP ») et 2015/2013 (même recueil « Sésame » de Francis Imbs, 2005) :
  niveaux de lecture plus bas que la 6ᵉ ; aucune incidence sur les lignes.
- **2008** : couche texte exploitable mais soulignements perdus (compréhension 2) : les expressions visées sont déduites
  des segments laissés vides ; signalé dans la transcription.
- **2009** : copie diffusée avec un bandeau edunet.tn et des pointillés très pâles ; consignes lisibles (lisibilité partielle).
- **Coquilles imprimées** conservées : « A l'école », « Ecoutez », « Ecris la phrase » (majuscule sans accent, 2020, 2018, 2008),
  « Paul arriva ainsi dans une impasse » (2015 : prénom étranger au texte), « le fils du vent » (2012), « Tamara Danblon »,
  « Le printemps de Sam » dans la référence de 2020 pour un texte intitulé « Le printemps de Samy ».
- Aucune consigne n'a vieilli au point d'être fausse : les sujets 2020 à 2008 restent conformes à la fiche, hors les
  notions de la section 4.
