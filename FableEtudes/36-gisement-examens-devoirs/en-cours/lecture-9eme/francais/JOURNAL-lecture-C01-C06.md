# Journal du lecteur — français 9ᵉ, lot C01 à C06 (sessions 2026, 2025, 2024 ; générale et technique)

Étape G2. Lot 1 : les conventions ci-dessous valent pour les autres lots français (C07 et suivants).
Lecture du 2026-10-16. Les six PDF sont des scans sans couche texte (`pdftotext` rend 4 octets) :
lecture en vision, 150 DPI, une fois par page. Les six sha256 téléchargés égalent ceux de `docs.json`.

## 0. CONVENTIONS FIXÉES (à reprendre par les autres lots)

**Grain des lignes** (une ligne = un exercice ou une partie notée) :
- **Compréhension** : UNE ligne pour toute la partie (texte + questions), n°exo `1`, barème = total de la partie
  (7 en générale, 8 en technique), étapes = nombre de questions numérotées (sous-questions a/b comprises quand
  elles se justifient séparément). Chapitre : `09-comprehension-production-ecrite` seul.
- **Langue** : UNE ligne par question numérotée imprimée (1, 2, 3, 4), barème = points imprimés de la question
  (a + b additionnés : 0,5 + 0,5 = 1). Tous les totaux de question étant entiers, aucun décimal n'entre dans la colonne barème.
- **Production écrite** : UNE ligne, dernière du document.
- **n°exo = rang d'ordre dans l'épreuve** (`\d+[a-z]?` exigé par le validateur) : compréhension = 1, puis les
  questions de langue 2, 3, 4, 5, puis la production. La numérotation imprimée « II.1, II.2… » est donc décalée
  de +1 pour la langue : `n°exo = n° imprimé de langue + 1`. Les sous-questions ne reçoivent pas de suffixe.
- `étage` : compréhension et langue d'application directe = `d1` ; question de langue à deux notions ou à
  transformation = `d2`/`d3` ; production écrite = `d3`. Aucun `d4` en français (pas de preuve, pas d'enchaînement
  de chapitres à calcul).

**Chapitres** (jamais `10-annales-sujets-types` ; compétences toujours `-`, aucun registre) :
- compréhension → `09-comprehension-production-ecrite` ;
- production écrite → `08-types-de-textes-et-production-ecrite+09-comprehension-production-ecrite`, plus
  `06-concordance-des-temps` quand la consigne impose un récit au passé (« raconte », « fais le récit »), plus
  `04-discours-direct-et-indirect` quand elle impose de rapporter un dialogue ; pas de 06 pour un texte au présent
  ou au futur (« décris ton projet ») ;
- synonyme, sens en contexte, emploi d'un mot en phrase personnelle, polysémie → `07-lexique-et-figures-de-style` ;
- enrichissement du groupe nominal (épithète, complément du nom, relative) → `11-groupe-nominal-et-attribut`
  (+ `02-propositions-subordonnees` si une relative est demandée) ;
- phrase complexe par subordination (cause, but, conséquence/intensité) → `02-propositions-subordonnees` ;
- conjugaison → `05-modes-et-temps-verbaux`, plus `06-concordance-des-temps` quand le choix du temps dépend
  du rapport entre deux actions (antériorité, durée/événement, présent/passé) ;
- adverbes en -ment, homophones (quand/quant/qu'en) → `14-homophones-et-adverbes-en-ment` ;
- changement de sujet (genre, personne) → `13-les-accords` (+ `12-reprises-et-pronoms-complements` si un pronom
  complément ou un participe placé après un complément antéposé est en jeu) ;
- forme négative → `01-types-et-formes-de-phrases` ; connecteurs/indicateurs temporels d'un récit → `08`
  (hésitation avec 06 : voir § 4).

**Barème** : toujours en points entiers dans les lignes ; la transcription garde `0,5`/`1,5` tels qu'imprimés.

**Texte de compréhension long** : transcrit mot pour mot dans la section « Texte support (page 1) » de la
transcription (avec chapeau en italique, appels de notes ¹ ² ³, notes de bas de page en fin de section, signature
d'auteur/œuvre/éditeur/année) ; les coupures de l'éditeur `[...]` sont reproduites ; jamais recopié dans les lignes
ni les snapshots hors `/tmp`.

**Cases à cocher** : `[case]` après chaque proposition ; mot souligné imprimé → `__mot__` + note entre crochets.
**Lignes de pointillés de réponse** : `........` dans la transcription (pas comptées).
**En-tête de transcription** : même YAML que SVT (`source: officiel`, `examen`, `matiere: Français`, `session`,
`filiere`, `page`, `fichier`, `consulte_le: 2026-10-16`, `sha256`, `lecture: vision`) ; l'examen se cite sous son
intitulé imprimé en français (« Examen du Diplôme de Fin de l'Enseignement de Base Général/Technique »).
**Coquilles imprimées** : conservées telles quelles (voir § 3), jamais corrigées en silence.
**Durée** : celle imprimée (2 h générale, 1 h technique).

## 1. Documents lus

| id | session | filière | sha256 (= registre) | pages | lecture | lignes | transcription |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | 2026 | générale | 5cafa2e4ae3eac1a9d7574de6d573236536d7efa3280700f1dca0ce557702c2c | 4 | vision | 6 | `french/2026-generale.md` |
| C02 | 2026 | technique | 78f39014f46cdbfb460cd0fa2e28ec8ef675567e3eb7a0bb0bbb724989afe922 | 4 | vision | 5 | `french/2026-technique.md` |
| C03 | 2025 | générale | 1fa230c20ea00dceddbc66aefbd25369341ec5ab88feb8f9ebc1ec6e06c67643 | 4 | vision | 6 | `french/2025-generale.md` |
| C04 | 2025 | technique | 410e7dd9b5e85b7f9698e50f41dcf581f8492659bca24d6ebd91c0afd37b55e8 | 4 | vision | 5 | `french/2025-technique.md` |
| C05 | 2024 | générale | e38d3a4a45526c9814a046c1a19b98b41e128e07259f27117e0810c696d6858a | 4 | vision | 6 | `french/2024-generale.md` |
| C06 | 2024 | technique | 4cfedc88ecd719c6085fa54a404581959830cf086ef74ba33c2b0e6cac98bfef | 4 | vision | 5 | `french/2024-technique.md` |

Transcriptions sous `/home/user/wt-fr/content/programmes-officiels/examens-nationaux/9eme-base/french/`.
Snapshots locaux : `/tmp/claude-0/frlec/snapshots/C0{1..6}.txt`. Lignes : `lines/C0{1..6}.tsv` + `.meta`
(33 lignes ; `content:gisement:lignes --subject french --grade 9eme-base` : 33 valides, 0 fautive, manifeste de 15
chapitres de `wt-fr`/corpus principal ; le manifeste de `wt-gis/content` n'a encore que 10 chapitres).

## 2. Format de l'épreuve (identique sur les trois sessions)

- Un texte support narratif d'environ 300 à 400 mots (extrait de roman ou de nouvelle, avec chapeau, notes de
  vocabulaire ¹…⁵, auteur/œuvre/éditeur/année), au verso duquel (pages 2 à 4) suivent les questions.
- **Générale** (2 h, coeff. 1) : Compréhension 7 + Langue 6 + Production écrite 7 = 20.
- **Technique** (1 h, coeff. 1) : Compréhension 8 + Langue 6 + Production écrite 6 = 20. Compréhension plus guidée
  (cases à cocher à justifier), production « dizaine de lignes » au lieu de « vingtaine ».
- Langue (6 points) : 3 à 4 questions numérotées, la dernière ou l'avant-dernière toujours « adverbes en -ment »
  (générale 2024, 2025) ou une conjugaison. Une question lexicale en tête (synonyme / sens en contexte).

| session / filière | texte (nature) | compréhension | langue (par question) | production |
| --- | --- | --- | --- | --- |
| 2026 G | récit à la 1re personne (artiste avant son concert) | 3 questions, 7 pts | lexique 1 ; enrichir GN 2 ; conjuguer futur antérieur/imparfait 2 ; quand/quant/qu'en 1 | raconter un exploit d'un ami (7) |
| 2026 T | récit 3e personne + dialogue (sport) | QCM justifiés, réaction, activités (8) | sens en contexte 2 ; changer le sujet 2 ; passé composé 2 | raconter la réussite d'un ami sportif (6) |
| 2025 G | portrait au récit (serveuse) | vrai/faux, qualités, raisons, avenir (7) | locution + emploi 1 ; subordination cause/but 2 ; futur simple/antérieur 2 ; adverbes en -ment 1 | rapporter un dialogue avec son père (7) |
| 2025 T | récit 3e personne (école) | QCM justifiés, raison, comportements (8) | sens en contexte 2 ; présent/passé composé 2 ; changer le sujet 2 | décrire son projet d'avenir (6) |
| 2024 G | récit à la 1re personne (violon) | 4 questions, 7 pts | synonyme + polysémie 1 ; simple→complexe cause/conséquence 2 ; imparfait/passé simple 2 ; adverbes en -ment 1 | récit + description (7) |
| 2024 T | récit à la 1re personne (amitié d'école) | QCM justifiés, actions, raison (8) | sens en contexte 2 ; indicateurs temporels 2 ; forme négative 2 | récit + portrait (6) |

## 3. Notions de langue par chapitre (lot C01-C06, 33 lignes)

| chapitre | lignes où il apparaît |
| --- | --- |
| 01 types et formes de phrases | C06 (forme négative) |
| 02 propositions subordonnées | C01 (relative), C03 (cause/but), C05 (cause/conséquence d'intensité) |
| 03 voix active et passive | jamais testée sur ce lot |
| 04 discours direct et indirect | C03 production (dialogue rapporté) |
| 05 modes et temps | C01, C02, C03, C04, C05 (futur simple/antérieur, imparfait, passé simple, passé composé, présent) |
| 06 concordance des temps | quasi toutes les conjugaisons et les productions racontées |
| 07 lexique et figures | les six sessions (synonyme, sens en contexte, polysémie) ; aucune figure de style |
| 08 types de textes et production | les six productions ; C06 connecteurs temporels |
| 09 compréhension et production | les six compréhensions et les six productions |
| 11 groupe nominal et attribut | C01 (enrichir un GN) |
| 12 reprises et pronoms compléments | C02 (« le félicitent », « lui font »), C04 |
| 13 les accords | C02, C04 (changement de sujet) |
| 14 homophones et adverbes en -ment | C01 (quand/quant/qu'en), C03, C05 (adverbes) ; C03 et C05 identiques de forme |
| 15 article de presse et lettre | jamais |
| 10 annales | non employé |

**HP : aucun.** Toutes les notions testées entrent dans la liste des 14 chapitres notionnels. Chapitres jamais
testés ici : 03 (passif) et 15 (article de presse et lettre) ; 04 une seule fois. Part HP : 0 ligne sur 33.
Chaque notion de langue d'examen tombe dans le programme en vigueur.

Coquilles imprimées conservées dans les transcriptions : C02 (langue 2) « il est impatient » avec « il » en
minuscule après un point ; C03 (production) « Il t'explique, qu'en plus de l'amour… » avec virgule fautive ;
C05 (texte) « révélation¹.. » avec double point. Aucune consigne n'a vieilli : le passé simple (C05) et le futur antérieur (C01, C03) restent au programme.

## 4. Doutes de classement (à trancher par le pilote)

- **Connecteurs temporels** (C06 langue 2) : classé `08` + `06`. Si le pilote préfère un classement `06` seul ou un
  chapitre « connecteurs » (absent de la liste), reclasser ; HP écarté, le chapitre 06 est « temps du récit ».
- **Compréhension** : un seul chapitre `09`, sans distinction entre inférence et relevé ; les consignes qui
  demandent de « justifier par un indice textuel » sont constantes sur les six sessions.
- **Sens en contexte avec QCM** (C02, C04, C06) classé `d1`, contre `d2` en C01/C05 où l'élève doit produire
  (synonyme + phrase personnelle).

## 5. Difficultés

Aucune de lecture : six scans nets, aucune zone illisible. Un transparent de la page imprimée au verso se lit en
fantôme sur les pages 2 et 4 de plusieurs scans (texte de la page voisine), sans effet sur la transcription.
Le téléchargement HTTP direct a réussi sans proxy particulier ; sha identiques au registre.
