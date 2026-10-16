# Journal de lecture des devoirs D01-D06 (9e anglais, vague 1, devoir.tn)

Lecteur G2, 2026-10-16. Sources web : rien n'est repris, aucune transcription versionnée. Sorties : `lines/D01..D06.tsv` et `.meta`, snapshots hors dépôt `/tmp/claude-0/devoirs-snapshots/english/<id>.txt`, PDF et rendus dans `/tmp/claude-0/endev/`. Aucune écriture dans `gisement.json`, `lignes.tsv`, `content/` ni git. Conventions : § 0 de `JOURNAL-lecture-C01-C06.md`, étendues aux devoirs (voir « Grain » ci-dessous).

## Téléchargement
- URL de `machine-list.tsv` (`curl -g`, `CURL_CA_BUNDLE=/root/.cache/yqa-ca/ca-bundle.pem`, jamais `-k`) : les six PDF répondent et **les six sha256 égalent le registre**. Aucune URL changée, aucun retour à la `page`.
- `pdftotext` : couche texte propre pour D01, D03, D04, D05 (D01 et D04 : une page-image lue en vision) ; D02 (5 octets) sans couche texte et D06 à police corrompue : lecture en vision, 110 DPI, une fois par page.

| id | créneau | sha256 (début) | pages | lecture | lignes | auteur imprimé | établissement | année imprimée |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D01 | DC1 | 1dfb7304 | 4 | mixte | 5 | Mme Baatour | Abou Zamaa Prep School | 2019-2020 (13 novembre 2019) |
| D02 | DS1 | 673debaa | 5 | vision | 5 | « English Teachers » (filigrane Tadris.TN) | aucun | 2023-2024 |
| D03 | DC2 | 1680cba9 | 3 | pdftotext | 4 | Mme Nadia Abid | Manar 1 Prep School | 2019-2020 |
| D04 | DS2 | 7a288af5 | 4 | mixte | 5 | Bechir Fraoua | Megrine Pioneer Middle School | 2018-2019 |
| D05 | DC3 | 58dad306 | 3 | mixte | 5 | Bechir Fraoua | Megrine Pioneer Middle School | 2018-2019 (avril 2019) |
| D06 | DS3 | 9bf659ec | 2 | vision | 5 | aucun | aucun | 2012-2013 (mai 2013) |

Total : 29 lignes. `content:gisement:lignes --subject english --grade 9eme-base` : 6 fichiers, 29 lignes valides, 0 fautive.

## Grain des lignes (extension du § 0 aux devoirs)
- Le § 0 vaut tel quel : compréhension = une ligne n°1, `09` seul ; langue = une ligne par exercice numéroté, n° imprimé + 1 ; production = dernière ligne ; compétences `-` ; barèmes décimaux gardés (2.5, 3.5).
- **Cas nouveau, l'écoute** (D01, D03, D05) : le contrôle n'a ni compréhension écrite ni production ; son bloc d'écoute de 8 points (questions de compréhension, tableau, orthographe, fonction, prononciation) est traité comme la compréhension : une ligne n°1, `09` seul, étapes = nombre de questions ou de rubriques (6, 6, 8), `d2` (tableau ou valeur grammaticale). Dans D01, l'écoute est imprimée après la langue : le rang n°1 est donné au bloc de compréhension, non à l'ordre d'impression.
- Banque de mots purement lexicale : `09` seul, `d1` (D03-2, D04-2, D05-3, D06-2) ; banque mêlant connecteur, article ou pronom : `d2` (D01-2, D02-3).
- **HP** : `HP:word-formation` (dérivation : behave → behaviour, suspense → suspenseful, fortune → fortunately, particular, succeed, affect, amuse, vacation, adventure) ; `HP:gerund` (forme en -ing exigée après verbe ou préposition : mind doing, passion for making, make way for producing). **Cas nouveau signalé** : D03-3 « leaving » en tête de proposition participiale, rattaché à `HP:gerund` faute de mot-clé dédié. Hors HP, rangés en `09` ou laissés : adjectifs composés (narrow-minded, hard-earned, once-in-a-lifetime), « to fail » après « want somebody » (schéma verbal, non étiqueté), « these/those », « yours ».
- Écriture : D02 « conseiller » et D04 « mettre en garde et encourager » → `04-modals+09` ; D06 « présenter une organisation et sa mission » → `09` seul.

## Écarts au registre
- **D04 et D05** : l'en-tête imprime « Megrine Pioneer Middle School » (collège pilote) ; le registre dit `college: ordinaire`. Le contenu tranche : pilote, alors que la vague 1 devait alterner (ordinaire pour D01, D02, D03, D06 ; pilote pour D04 et D05 : l'alternance prévue est donc rompue en pratique, à signaler au pilote).
- **D02** : le registre note l'auteur `Tadris.TN` ; le document imprime « English Teachers » avec le filigrane de la plateforme : aucun enseignant identifiable.
- **D06** : le registre note l'auteur `galbi-maweheb` (nom de fichier) ; rien n'est imprimé (ni auteur, ni établissement), seulement « Test N: 6, May 2013 ». Année 2012-2013 : antérieure aux devoirs de la plage du programme actuel (les autres vont de 2018-2019 à 2023-2024). Contenu entièrement dans le champ du guide, classé `programme: en vigueur` avec la réserve de date ; au pilote de la garder ou de la remplacer (même arbitrage que D05 du français).
- Années du registre : fin d'année scolaire (D01 2020, D04/D05 2019, D06 2013) : cohérent avec l'impression. D01 : numérotation « Mid of Term Test N:1 » = DC1 ; D05 « Mid-term Test 3 » = DC3 ; D04 « Achievement Test 2 » = DS2 ; D02 « End-of-Term Test N°1 » = DS1 ; D06 « Test N: 6 » = DS3 (3e synthèse, 6e épreuve de l'année) : créneaux concordants.
- Pages : D01 comprend une page de garde vide ; D02 une page de publicité ; D04 inverse l'ordre (texte de lecture en dernière page).

## Plafond par auteur (au plus deux)
Auteurs distincts : Baatour (D01), Abid (D03), Fraoua (D04 et D05, **deux : plafond atteint, respecté**), « English Teachers »/plateforme (D02), anonyme (D06). Aucun auteur n'a plus de deux devoirs. Pour la vague 2 : exclure Fraoua.

## Format des devoirs comparé à l'examen
- Examen (C01-C06) : 1 h, 6 + 8 + 6 (général) : compréhension, langue en trois exercices, production de 10 à 12 lignes.
- **Synthèses (D02, D04, D06)** : même format 6 + 8 + 6, 1 h ; compréhension de cinq ou six questions, trois exercices de langue (2.5 + 3 + 2.5 ; 2.5 + 2.5 + 3 ; 3 + 2.5 + 2.5), production de 6 points (D04 : 14 lignes au plus ; D02 : courriel de conseil ; D06 : images d'appui). Presque identique à l'examen.
- **Contrôles (D01, D03, D05)** : pas de compréhension écrite ni de production ; écoute de 8 points puis langue de 12 points (trois exercices en D03, quatre en D01 et D05). L'écoute avec fonction, orthographe et prononciation n'existe pas à l'examen : 3 lignes (10 %) sans équivalent.
- Le texte de langue des contrôles est plus long (une centaine de mots, D03 plus dense), et la bande son n'est jamais jointe (sauf les deux scripts de D03).

## Notions par chapitre (nombre de lignes sur 29)
- **01-present-tenses** : 5 (D01-3, D01-4, D02-4, D03-3, D03-4). **02-past-tenses** : 5 (D02-2, D04-3, D04-4, D05-2, D05-5, dont le present perfect de D04-4 et D05-5). **03-future** : 0 (absent des six devoirs). **04-modals** : 3 (D02-5, D04-5, D03-3). **05-conditionals** : 0. **06-passive-voice** : 1 (D03-4, participe passif en choix). **07-reported-speech** : 0. **08-relative-clauses-comparatives** : 8 (comparatifs et superlatifs surtout ; relatif en choix D01-3 et D03-4). **09-reading-comprehension-writing** : 23 (compréhension, écoute, vocabulaire en banque, appariements, production).
- Chapitres jamais travaillés : 03, 05, 07, ce qui rejoint le constat de l'examen (le programme porte sur la lecture et le lexique, les structures étant testées par mots à mettre en forme).
- **Part HP** : 6 lignes sur 29 (≈ 21 %) portent un jeton HP (D01-4, D02-4, D03-3, D03-4, D04-4, D05-5), jamais une ligne entièrement HP : 4 avec `HP:word-formation`, 4 avec `HP:gerund`. Même proportion qu'aux sessions récentes de l'examen.
- **Archétypes neufs par rapport aux lignes C01-C06** : écoute avec rubriques fonction, orthographe, prononciation (D01-1, D03-1, D05-1) ; banque purement lexicale (déjà vue en C04) ; appariement avec une proposition en trop (D05-4, D06-3) ; choix parmi trois sur un article scientifique avec participe passif et relatif (D03-4) ; production en courriel de conseil (D02-5) ; présentation d'une organisation à partir d'images (D06-5, seule production `09` sans `04`).

## Difficultés
- D06 : texte extrait illisible ; une coquille d'impression dans les propositions (« humburgers », « bahave » en D02). D05 : une question d'écoute renvoie à tort à un « reading passage » et la bande son manque : lisibilité de l'écoute non vérifiable (lignes décrites d'après les questions seules).
- Anti-copie : archétypes et pièges rédigés en français dans mes mots ; contrôle automatique des suites de trois mots contre les six snapshots : aucune coïncidence.
