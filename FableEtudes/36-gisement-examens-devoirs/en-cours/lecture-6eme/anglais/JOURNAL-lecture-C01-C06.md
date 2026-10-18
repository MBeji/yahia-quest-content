# Journal du lecteur — anglais 6ᵉ, lot pilote C01 à C06 (sessions 2026 à 2021, épreuve unique)

Étape G2. Lot pilote : les conventions du § 0 valent pour les deux autres lots d'examens de la 6ᵉ.
Lecture du 2026-10-18. Les six PDF sont des scans sans couche texte (`pdftotext` rend 2 à 4 octets) : lecture en
vision, 150 DPI, une fois par page. Les six sha256 des copies du dossier `snapshots/6web/` égalent ceux de
`docs.json` et du registre. Aucune écriture git, rien sous `content/english-6eme/`, `gisement.json` intact.

## 0. CONVENTIONS FIXÉES (à reprendre par les autres lots)

Reprises telles quelles de la 9ᵉ : n°exo `\d+[a-z]?`, sans suffixe aux sous-questions ; reading = UNE ligne n°1 ; une
ligne par exercice de langue ; compétences `-` ; créneau `concours` ; barème décimal toléré ; texte support jamais
transcrit en entier (référence, nombre de mots, résumé, une citation courte, « texte intégral : PDF officiel,
sha256 au registre ») ; le texte lacunaire d'un exercice de langue est un item, transcrit mot pour mot.

**Grain des lignes** : une ligne par exercice numéroté imprimé, y compris en Writing.
- Reading : n°exo `1`, barème = total de la partie (6), étapes = nombre de questions numérotées (2 à 5 ; 2021 en a 2).
- Language : trois exercices imprimés, n°exo 2, 3, 4 (rang d'ordre), barème = points imprimés.
- **Writing (décision du pilote, 2026-10-18)** : la partie n'est pas une rédaction mais des exercices courts
  (remise en ordre de mots ou de phrases, dialogue, appariement). Une ligne par exercice imprimé : n°exo 5 pour
  l'exercice 1 (2 points). **Quand la session porte en plus une vraie rédaction (paragraphe ou courriel, 4 points),
  elle reste UNE ligne, la dernière : n°exo 6.** Les six sessions 2021-2026 portent toutes cette rédaction : 6 lignes
  par épreuve (2 + 4 en Writing), soit 36 lignes. Une session sans rédaction aurait 5 lignes ou moins.
- Barèmes observés : reading 6, language 3 + 3 + 2 (dans un ordre variable), writing 2 + 4.

**Chapitres** (jamais `HP:` seul sans notion identifiée ; jetons HP après les slugs, slugs dans l'ordre du manifeste) :
- *Reading* : UN seul slug, celui de l'unité dont relève le thème du texte (D2) : soin des autres → `04`, loisirs et
  concours de dessin → `01`, achats → `06`, monuments et pays → `07`, fête de classe → `05`. Une question qui embarque
  une notion (can't, un conseil rapporté) n'ajoute rien.
- *Language* : cumul des chapitres des notions effectivement testées par un item, item par item. Rangements fixés :
  simple past → `05` (jamais `06`, même dans un contexte d'achat) ; will → `03` ; should/must/can/have a + maladie,
  How many/much → `02` ; adverbes de fréquence, -s du présent, possessifs, because, Would you like to/Let's/How about →
  `01` ; superlatif en -est, Verb + er (métier), each other, vocabulaire du soin → `04` ; météo, saisons, noms de
  saisons et contraires de météo → `03` ; vêtements, in/on (lieu), would like, how much → `06` ; have the right to,
  fêtes, date d'anniversaire → `05` ; monuments, salutations, coutumes → `07`. Un item de vocabulaire
  rattaché à une unité prend le chapitre de cette unité.
- *Dialogue à compléter ou à remettre en ordre* : cumul des fonctions des répliques proposées (suggestion `01`,
  demande avec can `02`, will `03`, would like `06`).
- *Writing, rédaction* : chapitre du thème (D2) + chapitre de chaque contenu imposé par la consigne qui relève d'une
  autre unité (météo `03`, vêtements `06`, nourriture `02`, activités `01`) + `05` quand la consigne impose le passé,
  `02` quand elle impose de dire un conseil reçu.
- **Jetons HP fixés (mots-clés)** : `HP:word-formation` (dérivation : two → twice, friend → friendly, invite →
  invitation) ; `HP:ed-ing-adjectives` ; `HP:the-most` (superlatif adverbial « the most ») ; `HP:there-is-are` ;
  `HP:personal-pronouns` (pronoms sujet et complément ; seuls les possessifs sont au guide) ;
  `HP:relative-clauses` ; `HP:have-has` (have, has, have got de possession) ; `HP:present-continuous` (règle du
  contexte) ; `HP:wh-questions`. Un cas nouveau : le noter ici, au plus proche.
- Synonymes et contraires, remise en ordre, appariement ne sont pas des notions : on classe le contenu des mots.

**Étages** (échelle du portail, aucun `d4`) : reading `d1` si seulement choix, vrai/faux ou mots à relever, `d2` dès
qu'il y a une réponse rédigée, un référent, un synonyme ou une chronologie ; cloze à banque, choix de formes,
appariement, remise en ordre de mots, dialogue : `d2` ; mise en forme de mots entre crochets : `d2`, `d3` quand au
moins deux items sont des dérivations (C01 ex. 3) ; rédaction de 4 points : `d3`.

**Format de l'épreuve** : 45 minutes (et non 1 h comme en 9ᵉ), coefficient 1, 20 points : Reading 6 + Language 8 +
Writing 6, sur 2 à 4 pages (la partie « Writing » vaut 2 + 4). Texte support de 105 à 140 mots (un à trois
paragraphes), sans source imprimée. Durée estimée de travail : 45 min.
**En-tête de transcription** : `examen` = intitulé de `docs.json` suivi de l'intitulé arabe imprimé ; `session`, `filiere:
unique`, `consulte_le: 2026-10-18`, `lecture: vision`. Fichier `<année>-unique.md`. Cases `[case]`, pointillés `........`,
mot souligné `__mot__`.

## 1. Documents lus

| id | session | sha256 (= registre ?) | pages | lecture | lignes | transcription |
| --- | --- | --- | --- | --- | --- | --- |
| C01 | 2026 | a4920ef83df6f9019102c0fd3ab5fbd3c94c15db778d7064eef178e0c6d00c3c (oui) | 4 | vision | 6 | `english/2026-unique.md` |
| C02 | 2025 | 4cfa12a00e848fa755722cdac7e2efe96efacaa8b36e0bfeefa267a21d002904 (oui) | 4 | vision | 6 | `english/2025-unique.md` |
| C03 | 2024 | a5c7b22f24874f7f1bcc1cb5b00f4795ed45d67036beec29fb389d99ad1f2923 (oui) | 4 | vision | 6 | `english/2024-unique.md` |
| C04 | 2023 | 883a5e762564e7061e6fbf95d7012203d208b6632d7367d17462ebd7a6677b92 (oui) | 3 | vision | 6 | `english/2023-unique.md` |
| C05 | 2022 | ff6341c0bdb0a376c3e3fa36cd9c4aa8e9e1e750256e8c1ced9abcc300770625 (oui) | 2 | vision | 6 | `english/2022-unique.md` |
| C06 | 2021 | 6b748fc4f1371ad1ed3bcb46843bc2e2dabd5c87d3584f554d72c40a3a4a3cf0 (oui) | 2 | vision | 6 | `english/2021-unique.md` |

Transcriptions sous `/home/user/wt-en6/content/programmes-officiels/examens-nationaux/6eme-base/english/`. Snapshots
(textes complets, hors dépôt) : `/tmp/claude-0/en6lec/snapshots/C<année>.txt`. Lignes : `lines/C0{1..6}.tsv` + `.meta`.
Validation : `content:gisement:lignes --subject english-6eme --grade 6eme-base --content /home/user/wt-en6/content` :
6 fichiers, 36 lignes, 36 valides, 0 fautive (manifeste de 7 chapitres). Ids de ligne : C01 = 2026 … C06 = 2021
(ordre de `docs.json`).

## 2. Format par session

| session | thème du texte | reading | langue (par exercice) | writing |
| --- | --- | --- | --- | --- |
| 2026 | journée du soin, visite à l'hôpital | 4 q. (2+2+1+1) | lacunes à banque 3 ; choix 2 ; mots mis en forme 3 | dialogue à compléter 2 ; paragraphe au passé (météo, animal, soins) 4 |
| 2025 | lectrice gagnant un voyage en Tunisie | 3 q. (3+2+1) | lacunes à banque 3 ; mots mis en forme 3 ; contraire + synonyme 2 | quatre phrases à remettre en ordre 2 ; paragraphe d'achats 4 |
| 2024 | enfant perdu au centre commercial | 4 q. (1+2+2+1) | lacunes à banque 3 ; choix 2 ; mots mis en forme 3 | dialogue de librairie 2 ; courriel de conseils d'un médecin 4 |
| 2023 | fillette et concours de dessin | 4 q. (2+1+2+1) | lacunes à banque 3 ; mots mis en forme 3 ; contraires 2 | dialogue à remettre en ordre 2 ; paragraphe de tâches ménagères 4 |
| 2022 | mère, enfants, voisine aidée | 3 q. (1+2+3) | appariement 3 ; lacunes à banque 3 ; choix 2 | mots remis en ordre 2 ; courriel de vacances 4 |
| 2021 | fête de fin d'année | 2 q. (3+3) | lacunes à banque 3 ; choix 2 ; appariement 3 | phrases remises en ordre 2 ; courriel d'anniversaire 4 |

## 3. Notions par chapitre (36 lignes)

Nombre de lignes portant le chapitre : 01 : 16 ; 02 : 7 ; 03 : 7 ; 04 : 10 ; 05 : 15 (passé simple dans presque toutes
les langues et rédactions, reading 2021) ; 06 : 9 ; 07 : 2 (reading 2025 et mots en ordre 2025). Readings : 04 en 2026 et
2022, 07 en 2025, 06 en 2024, 01 en 2023, 05 en 2021. Le chapitre 07 est le moins sollicité hors reading.

**Part HP** : 11 lignes sur 36 portent un jeton HP (2026 : 3 ; 2025 : 0 ; 2024 : 0 ; 2023 : 1 ; 2022 : 4 ; 2021 : 3).
Une seule ligne n'a que des jetons HP (2021, appariement de questions : `HP:present-continuous+HP:wh-questions`).
Sessions récentes (2024-2026 : 3 lignes, toutes en 2026 ; 2023 : 1). 2022 et 2021 sont `mixte` (there is/are, présent
continu, pronoms personnels, relatives, have got, questions en wh-), très probablement l'ancien manuel ; 2023 à 2026
sont en vigueur et ne sortent du guide que par la dérivation de mots, « -ed/-ing » et « the most ».

## 4. Difficultés et doutes

- **Deux exercices de Writing** : exercice 1 (2 points) en n°exo 5, rédaction en n°exo 6, conformément à la décision du pilote.
- **C01 ex. 4 « [two] → twice »** : classé `HP:word-formation` (dérivation) ; on aurait pu y voir un adverbe de fréquence
  `01`. **C01 ex. 3 « most »** (loved the slide the most) : `HP:the-most`, le guide n'enseigne que le superlatif en -est.
- **C02 ex. 1 « cared for »** : rangé `04` (vocabulaire du soin) ; « celebrated » est un intrus, « right » → `05`.
- **C03 W2** : « Doctor James advised you to do… » invite au discours rapporté (hors guide) ; classé `02+05` car un élève
  répond par should / must / un impératif.
- **C04 ex. 3 « outside »** : le contraire (inside) est un adverbe de lieu absent du guide ; classé `03+04`, non HP.
- **Dialogues d'options (C01, C03)** : les réponses ne sont pas publiées ; le classement suit les fonctions des répliques proposées.
- **Coquilles imprimées** conservées : 2021 « Mr Jack » dans l'item vrai/faux alors que le texte dit « Mr John » ; « 2marks »
  sans espace (2023) ; « ( 2marks ) » ; 2022 « There is (1) one extra word » ; pagination « 1 / 4 » avec espaces (2024,
  2026) ; 2022 et 2021 sans titre de partie « A- THE TEXT » et en-tête officiel imprimé en haut de la page 2.
- Aucune consigne n'a vieilli pour 2023-2026. Aucun corrigé n'est publié : les transcriptions ne donnent aucune réponse.
