# Journal du lecteur — anglais 9ᵉ, lot C07 à C18 (sessions 2023 à 2018 ; générale et technique)

Étape G2. Lecture du 2026-10-16. Conventions : § 0 du journal pilote `JOURNAL-lecture-C01-C06.md`, reprises à la lettre
(grain des lignes, n°exo, barème décimal gardé, chapitres par type d'exercice, jetons HP, étages, texte support résumé).
Les douze PDF sont des scans sans couche texte (`pdftotext` rend 0 octet) : lecture en vision, 150 DPI, une fois par
page, aucun détail relu à plus haute définition. Les douze sha256 téléchargés (`curl -g`, http, sans `-k`) égalent ceux
de `docs.json`. Aucune écriture git, ni `gisement.json`, ni `lignes.tsv`, rien sous `content/english/` hors les
douze transcriptions du lot.

## 1. Documents lus

| id | session | filière | sha256 (= registre ?) | pages | lecture | lignes | transcription |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C07 | 2023 | générale | 3efd1ebb1d2f84cfab6d9997b6cfe79ab8d9441eb0cc2eba33ee740e986d344c (oui) | 4 | vision | 5 | `english/2023-generale.md` |
| C08 | 2023 | technique | 35d683cb399816e4c678d4f4012467c05996063238e39e014610df434a922171 (oui) | 4 | vision | 5 | `english/2023-technique.md` |
| C09 | 2022 | générale | e3af153858bcac9d4de850cef83ea9d2a8a5b89829c29ce72670cea5dd695c82 (oui) | 4 | vision | 5 | `english/2022-generale.md` |
| C10 | 2022 | technique | dff721cbdb210b7e69885154351ab195baa0cd0159cfe21c330866a4864c2017 (oui) | 4 | vision | 5 | `english/2022-technique.md` |
| C11 | 2021 | générale | d0bf86fcb201e03166079c8a13a54629360376068abcfe301c3d692ca4864d7a (oui) | 4 | vision | 5 | `english/2021-generale.md` |
| C12 | 2021 | technique | b6706fd55bb732b158d15c9ef89e216004f9ee49e66340b05119a192fdf16ae3 (oui) | 4 | vision | 5 | `english/2021-technique.md` |
| C13 | 2020 | générale | 6bbaa28a79bb2787c4c250e55058151a21e02dda743fefd6abb43ca65e0538ff (oui) | 4 | vision | 5 | `english/2020-generale.md` |
| C14 | 2020 | technique | 7a94d53f811bd9b6b40d96c6f65fe751451a63aa755d4ae0178c0a137239270e (oui) | 4 | vision | 5 | `english/2020-technique.md` |
| C15 | 2019 | générale | 9287b36d9470ef9e83a98798b441b23b2eb9ec504edba9220bcf00125be6aaf6 (oui) | 4 | vision | 5 | `english/2019-generale.md` |
| C16 | 2019 | technique | 7d3d3dd67500697917f22d678d8c063b364db0d3e67172fdad0a551294f109eb (oui) | 4 | vision | 5 | `english/2019-technique.md` |
| C17 | 2018 | générale | 9f7e1a46bcc03aef525f604fc9cb9a5240d9db038bbaadfd736d874db677f264 (oui) | 4 | vision | 5 | `english/2018-generale.md` |
| C18 | 2018 | technique | 06c27408fb1d5de2b0fe3b85136bda2a356ab571b34c8e2a0dd8f964cf6a721c (oui) | 4 | vision | 5 | `english/2018-technique.md` |

Transcriptions sous `/home/user/wt-en/content/programmes-officiels/examens-nationaux/9eme-base/english/`. Snapshots
locaux (hors dépôt ; texte support complet, questions renvoyées à la transcription) :
`/tmp/claude-0/enlec/snapshots/C{07..18}.txt`. Lignes : `…/lecture-9eme/anglais/lines/C{07..18}.tsv` + `.meta`
(60 lignes). Validation : depuis `/home/user/eng-svtses`, `npm run content:gisement:lignes -- --subject english
--grade 9eme-base --content /home/user/wt-en/content <12 .tsv>` : **60 valides, 0 fautive** (une ligne reprise après un
premier passage : archétype de 17 mots, plafond du validateur 16). `/home/user/wt-en` ne porte pas le moteur : c'est
pourquoi la commande est lancée depuis `eng-svtses` avec `--content`.

## 2. Format de l'épreuve : stable sur 2018-2023, avec des variantes

Même ossature que le lot pilote (1 h, coefficient 1 ; générale 6 + 8 + 6, technique 8 + 7 + 5 ; texte support en page 1,
questions en page 2, langue en page 3, rédaction en page 4 ; 3 exercices de langue partout ; 5 questions de reading
partout). Aucun format réellement étranger : les écarts sont des variantes d'ordre ou de forme, rangées au plus proche du
§ 0.

| session / filière | texte (nature, mots, §) | reading | langue (dans l'ordre imprimé) | writing |
| --- | --- | --- | --- | --- |
| 2023 G | amitié entre un jeune et une voisine âgée (web, 230 m., 3 §) | 6 : idée, V/F, synonyme, **adjectif descriptif**, avis | banque 3 ; choix 3 ; appariement 2 | article de conseils pour rester actif (6, 10 l.) |
| 2023 T | électricienne de 19 ans (web, 165 m., 3 §) | 8 : titre, V/F, **valeur d'un modal (conseil)**, synonyme / mots à relever (3 pts) | banque 2.5 ; choix 2.5 ; appariement 2 | article : récit d'une construction collective et sentiments (5, 8 l.) |
| 2022 G | contrat d'amendes pour adolescents (presse, 235 m., 3 §) | 6 : idée, mots à relever (2), synonyme, référent, avis (« If I were… ») | banque 3 ; choix 2.5 ; **mots à mettre en forme 2.5, sans appariement** | post d'opinion + moyens de changer (6, 10 l.), **grille 2+2+2** |
| 2022 T | parcours d'une styliste, 1ʳᵉ personne (presse, 170 m., 3 §) | 8 : titre, **appariement §/idées (3)**, synonymes (2), « used to », référent | banque 2.5 ; choix 2.5 ; appariement 2 | post sur la cyberdépendance et conseils (5, 8 l.), **grille 2+2+1** |
| 2021 G | une journée sans mobile, 1ʳᵉ personne (presse, 230 m., 3 §) | 6 : titre, V/F, synonyme, référent, préférence | banque 3 ; choix 3 ; appariement 2 | article pour convaincre de participer (6, 10 l.), **grille 2+2+2** |
| 2021 T | apprenti menuisier (site de carrières, **155 m.**, 3 §, texte court) | 8 : idée, V/F, mots à relever (2), référent, synonymes (2) | banque 2.5 ; **appariement 2 ; choix 2.5** | article de description d'un projet (5, 8 l.), **grille 2+2+1** |
| 2020 G | jeune aidante familiale (presse, 210 m., **4 §**) | 6 : idée, référent, synonyme, mots à relever (2), avis hypothétique ; **pas de V/F** | banque 3 ; choix 3 ; appariement 2 | article « l'école dont je rêve » (6, 10 l.) |
| 2020 T | camionnette transformée en logement (presse, 170 m., 3 §) | 8 : idée, V/F, mots à relever (3), référent, synonyme | banque 2.5 ; **appariement 2 ; choix 2.5** | article sur la sécurité à l'atelier (5, 8 l.) |
| 2019 G | conductrice qui ramasse les déchets, 1ʳᵉ personne (260 m., 3 §) | 6 : idée, **réponse courte rédigée**, mots à relever (2), référent, avis | banque 3 ; **appariement 2 ; choix 3** | article sur les risques de la restauration rapide (6, 10 l.) |
| 2019 T | adolescent dépendant d'Internet (site de santé, 175 m., 3 §) | 8 : idée, V/F, **deux référents (2)**, synonyme, mots à relever (2) | banque 2.5 ; appariement 2 ; choix 2.5 | **lettre** à une amie : conseils d'économie d'eau et d'énergie (5, 8 l.), cadre « Dear … / Yours, » |
| 2018 G | élève sans cadeau (livre d'anecdotes, 245 m., **4 §**) | 6 : idée, mots à relever (2), **réponse courte**, référent, avis ; pas de V/F | banque 3 ; appariement 2 ; choix 3 | post de forum contre la triche + solutions (6, 10 l.) |
| 2018 T | première mécanicienne d'un pays, 1ʳᵉ personne (presse, 175 m., 3 §) | 8 : idée, mots à relever (2), V/F, synonyme, **deux référents (2)** | banque 2.5 ; appariement 2 ; choix 2.5 | **lettre** à un correspondant : matières et équipement (5, 8 l.), cadre « Dear … / Yours, » |

Traits par session, repérés à la lecture :
- **Ordre des exercices de langue** : la séquence banque → choix → appariement du pilote (2026-2024) tient en 2023, 2022
  (sauf C09), 2021 G et 2020 G ; **elle s'inverse** (banque → appariement → choix) pour 2021 T, 2020 T, 2019 G et T,
  2018 G et T. Le n°exo restant un rang d'ordre, l'appariement est donc l'exercice 3 (et non 4) sur ces sept épreuves :
  les lignes suivent l'ordre imprimé.
- **Format différent** : C09 (2022 G) n'a **pas d'appariement** ; ses trois exercices sont banque 3, choix 2.5 et mots à
  mettre en forme 2.5 (comme C03 en 2025). C13 (2020 G) et C17 (2018 G) ont un texte à **quatre** paragraphes.
- **Grille de notation imprimée** pour la rédaction, avec trois critères (adhésion à la tâche, lexique et grammaire,
  mécanique) : en 2022 (2+2+2 en G, 2+2+1 en T) et 2021 (idem). Absente avant 2021 et après 2022 (donc en 2023 et au-delà).
- **Rédaction en lettre** (2019 T, 2018 T) avec cadre pré-rempli (« Dear Asma, » / « Yours, Wahid / Wahida » ;
  « Dear Ahmed, » / « Yours, Ali / Alia ») : classée comme une production écrite ordinaire, UNE ligne, dernière du
  document ; les formules de lettre sont dites au piège.
- Le reading technique de 8 points comprend presque toujours une question de **mots à relever à recopier du texte** (2 ou
  3 points : 2021 T, 2020 T, 2019 T, 2018 T, 2023 T) ; la générale en a une en 2022, 2020, 2019 et 2018 (2 points).
- **Pagination imprimée** : « Page 1 sur 4 » en 2023-2022 ; « 1/4 » en 2021-2018.

## 3. Notions par chapitre (lot C07-C18, 60 lignes)

| chapitre | lignes où il apparaît |
| --- | --- |
| 01 present tenses | jamais testé comme tel (cloze : « remains », « gather » rangés lexique) |
| 02 past tenses (+ present perfect) | C07#2 (came), C08#2 (became), C08#5 (récit), C09#2 (found), C09#4 (launch), C12#4 (gained), C13#3 (didn't work), C16#4 (was working), C17#2 (forgotten), C18#4 (for/since, have been living) |
| 03 future | jamais |
| 04 modals | production : C07, C09, C10, C14, C15, C16, C17 (conseiller, proposer, dire quoi faire) ; C10#2 (would, could après modal) ; reading : C08 q4 (should = conseil), non comptée |
| 05 conditionals | C11#2 (if / unless), C17#4 (« if you don't, then you will regret ») |
| 06 passive voice | jamais testé en langue (présent seulement dans les stems d'appariement C17#3) |
| 07 reported speech | jamais |
| 08 relatives & comparatives | C07#2 (who), C07#3 (more, what), C10#3 (more), C11#2 (biggest, if), C11#3 (cheaper, itself…), C12#2 (which), C15#4 (most) |
| 09 reading & writing | douze readings, douze writings, tous les appariements, les lexicaux |
| 10 exam-style | non employé |

Sur douze sessions, les trois seuls chapitres vraiment sollicités en langue sont le passé (10 lignes), les relatifs et
comparatifs (7) et la production à valeur modale (8) ; le conditionnel n'apparaît que deux fois (C11, C17) et le passif,
le futur, le discours rapporté et le présent jamais. Cumulé avec le pilote (2024-2026), le discours rapporté et le futur
ne sont **jamais** testés en langue sur 2018-2026 ; le passif une seule fois (C03#2).

**Part HP** : aucune ligne entièrement HP ; **12 lignes sur 60** portent un jeton HP en complément :
`HP:word-formation` (7 : C07#3, C09#3, C09#4, C10#3, C13#3, C15#4, C17#4) et `HP:gerund` (7 : C08#3, C09#3, C10#2,
C16#2, C16#4, C17#4, C18#4). Aucun mot-clé nouveau n'a été créé. Le programme en vigueur reste conforme (aucune consigne
vieillie, aucune ligne marquée `[hors programme en vigueur]`).

## 4. Conventions nouvelles ou précisées (au plus proche du § 0 ; à valider par le pilote)

- **Pronoms** (personnels, objets, réfléchis : them / him / her, themselves, itself, « own ») : rangés en `09` comme les
  déterminants du § 0 (C08#3, C11#3, C15#4, C17#4, C18#2, C18#4), pas en HP.
- **Forme verbale après un verbe ou une préposition** (infinitif avec « to », base, gérondif, participe) : un seul jeton,
  `HP:gerund`, par proximité, même quand la forme visée est l'infinitif ou le participe (C08#3 « to protect », C10#2
  « working », C16#4 « doing », C17#4 « to wake », C18#4 « build »). Si le pilote préfère un mot-clé distinct
  (`HP:verb-pattern`), ces cinq lignes sont à rebaptiser.
- **Adjectif / adverbe / nom de même racine** (social-society-socially, choice-choose, challenge-challenging, advice-advise) :
  `HP:word-formation`, comme au pilote.
- **« what » en proposition d'objet** (« see what was going on », C13#2) : non compté en `08` (interrogatif, pas
  un relatif) ; en revanche le choix « what / which / who » de C07#3 est maintenu en `08` car l'exercice porte aussi
  un comparatif (« more »).
- **Conjonction conditionnelle** « if / unless » en lacune, et le futur après « if you don't » : `05`
  (C11#2, C17#4) ; les cadres « If I were… » de C09 et C13 (reading, question 5) ne sont pas comptés, comme au pilote.
- **Appariement qui embarque une notion** (C17#3 : comparatif, passif, if, relatif, « ought to » dans les stems) : `09`
  seul, la tâche étant un appariement de sens.
- **Modal en cloze** (C10#2 : « would … », « could … » exigent un verbe à la base) : `04` ajouté.
- **Valeur d'un modal en reading** (C08 q4 « should » = conseil) : `09` seul, comme C02 q3 au pilote.
- **Production écrite** : `04+09` quand la consigne demande de **conseiller, proposer, dire ce qu'on doit faire** (C07, C09,
  C10, C14, C15, C16, C17) ; `02+09` pour un récit au passé (C08) ; `09` seul pour persuader (C11), décrire (C12, C13,
  C18) ; aucun `03` : les consignes de projet futur de ces douze sessions sont des descriptions au présent.
- **Étage** : reading `d1` en technique sans rien d'autre qu'un repérage (C12, C14, C16, C18), `d2` en technique avec
  valeur grammaticale (C08 « should », C10 « used to ») et en générale (avis justifié) ; cloze à banque `d1` quand il est
  presque 100 % lexical ou à indice de forme (C12#2, C14#2, C18#2), sinon `d2` ; mots à mettre en forme `d3` (C09#4) ;
  writing générale 10 lignes `d3`, technique 8 lignes `d2`. Aucun `d4`.

## 5. Doutes de classement (à trancher par le pilote)

- **C13#3 et C09#3** : « didn't work / worked / hasn't worked » et « challenge / challenging / challenged » mêlent passé
  et dérivation ; classés `02` (+ `HP:word-formation`) pour C13#3, `09` + 2 HP pour C09#3 (la moitié des items est un
  choix de classe de mot ou de forme).
- **C07#2 et C11#2** : cloze à banque dont un seul item pointe une notion (who ; if / unless ; biggest). Chapitre
  grammatical ajouté selon la règle « au moins un item », `09` conservé (≥ moitié lexicale).
- **C17#4** : cinq notions en six items (infinitif, so/too, vocabulaire, wish, advise, will regret). `HP:wish` (« I wish I
  could ») n'a pas été créé : l'item est un choix de verbe lexical, rangé `09`. À reconsidérer si le pilote veut compter
  « wish + passé » comme notion absente.
- **C16#2 et C14#2** : cloze quasi lexical à un item de forme verbale (« ways of producing … constructing ») : `HP:gerund`
  ajouté pour C16#2, non pour C14#2 (aucune forme à produire).
- **Reading 2022 G (C09) et 2020 G (C13)** : questions 5 formulées à l'hypothétique (« If I were Katrina's son… », « Would
  you be as caring… if your parents ever had… ») : `09` seul comme au pilote ; le signal conditionnel de type 2 existe
  donc en 2025, 2026, 2022 et 2020.
- **Rédaction C09** : consigne « exprimer son opinion et suggérer des moyens de changer » ; ligne `04+09` (moyens d'agir).

## 6. Coquilles imprimées conservées dans les transcriptions et difficultés

Coquilles : C09 « 2, Circle the right option » (virgule au lieu du point), « Berrera » ; C10 « write your answers »
sans majuscule, « Few months later » (sans article) ; C14 « £10.000 » (point des milliers), « 3m long, 2m high, and just 1.5 wide » (sans unité à la
dernière mesure), « how it would look like » dans le texte ; C15 « Reader's Digest » : auteur imprimé « John Kurczewski » ;
C16 « md1health.com » et « Adapted from: » avec deux-points ; C17 « Was he exaggerating ? » et ponctuation à la française
(« ? », « : » précédés d'une espace) ; C17-C18 « NE RIEN ECRIRE ICI » sans accent ; mention « Durée : 1 heure » (et non
« 1h ») en 2018. La question 1 de C16 dit « The text is about » (sans « mainly »).

Difficultés : aucune de lecture. Les scans 2023-2019 sont nets ; ceux de 2018 (C17, C18) sont de moindre résolution
(jaunissement, légère granularité) mais intégralement lisibles à 150 DPI ; aucun item `[illisible]`. Un transparent de
la page recto se lit en fantôme sur plusieurs scans, sans effet. La transcription ne reproduit aucun corrigé (aucun
n'est publié avec ces sujets) ; les cadres de rédaction ne sont pas comptés ligne à ligne (consigne imprimée seule).
Nombres de mots des textes comptés sur les snapshots (arrondis à 5, numéros de paragraphe inclus) : 230, 165, 235, 170,
230, 155, 210, 170, 260, 160 (C16 compté à 159), 235, 175 (C18 compté à 176).
