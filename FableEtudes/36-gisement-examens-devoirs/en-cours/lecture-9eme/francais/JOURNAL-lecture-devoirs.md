# Journal de lecture des devoirs D01-D08 (9e français, vague 1, devoir.tn)

Lecteur G2, 2026-10-16. Sources web : rien n'est repris, aucune transcription versionnée. Sorties : `lines/D01..D08.tsv` et `.meta`, snapshots hors dépôt `/tmp/claude-0/devoirs-snapshots/french/<id>.txt`, PDF et rendus dans `/tmp/claude-0/frdev/`. Aucune écriture dans `gisement.json`, `lignes.tsv` ni git. Convention de lignes : § 0 de `JOURNAL-lecture-C01-C06.md` (compréhension une ligne n°1 ; langue une ligne par question ou bloc ; production dernière ligne ; compétences `-`).

## Téléchargement
- Le registre n'a pas de champ `fichier` pour les devoirs : le PDF a été retrouvé depuis la `page` (liens `.pdf` du dossier `base/Doc/…/Français/Devoirs/`), en testant chaque lien jusqu'à l'égalité du sha256. `curl -g`, `CURL_CA_BUNDLE=/root/.cache/yqa-ca/ca-bundle.pem`, jamais `-k`. Les huit sha256 téléchargés égalent le registre.
- `pdftotext` utilisable sur D01, D02, D04, D06, D07, D08 (couche texte propre, snapshot = texte brut) ; D03 sans couche texte (3 octets) et D05 à police corrompue : lecture en vision (150 DPI), snapshots de D03 et D05 limités aux consignes, écrits depuis la lecture visuelle.

| id | créneau | sha256 (début) | pages | lecture | lignes | auteur imprimé | établissement | année imprimée |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D01 | DC1 | d089e695 | 3 | mixte | 5 | M. Khaled | collège pilote de Tozeur | 2014-2015 |
| D02 | DS1 | ae892b7f | 4 | mixte | 7 | Chihaoui | E.P. Khlidia | 2018-2019 |
| D03 | DC2 | ecf6d0e4 | 3 | vision | 6 | M. Boughanmi | E.P. Ibn Nafiss El Ksour | 2018-2019 |
| D04 | DS2 | 20281b69 | 4 | mixte | 6 | Taha Bouazizi | E.P. A.Q. Chebbi, Fahs | 2019-2020 |
| D05 | DC3 | 37648c8e | 3 | vision | 5 | Atef Yousfi | E.P. Avicenne, Oued Ellil | 2011-2012 |
| D06 | DS3 | dbfbd526 | 4 | mixte | 4 | B. Walid | E.P. El Ksour | 2017-2018 |
| D07 | DC4 | 4770544a | 5 | mixte | 6 | Gassoumi Med. L. | collège pilote Ibn Rochd, Kasserine | 2017-2018 |
| D08 | DC5 | 24cf0ec6 | 4 | mixte | 6 | Gassoumi Med. L. | collège pilote Ibn Rochd, Kasserine | 2015-2016 |

Total : 45 lignes, `content:gisement:lignes` : 8 fichiers, 45 valides, 0 fautive.

## Écarts au registre
- **D04** : le champ `auteur` du registre (`E-P-A-Q-Chebbi-Fahs`) est l'établissement ; l'enseignant imprimé est Taha Bouazizi. Sans effet sur le plafond.
- **D05** : l'en-tête imprime l'année 2011-2012 ; le registre dit 2014 (nom de fichier 2013-2014). Hors « année scolaire du programme en vigueur » de D-4, mais l'épreuve et les notions sont celles de l'examen actuel : classé `programme: mixte`, à arbitrer par le pilote (le garder ou le remplacer).
- **Auteurs** : D03 et D06 (Boughanmi) et D07 et D08 (Gassoumi) sont bien du même enseignant, deux chacun : le plafond de deux par auteur est respecté. Les quatre autres sont distincts.
- **Collège** : D01, D07, D08 sont de collèges pilotes (confirmé par l'en-tête) ; D02, D03, D04, D05, D06 sont des écoles préparatoires ordinaires. Aucun démenti.
- **Créneau** : les huit correspondent (D07 et D08 ne portent pas de numéro d'épreuve : seul le nom de fichier donne contrôle 4 et 5). Il n'y a pas de D09 : la vague 1 compte huit devoirs et non neuf.

## Format des devoirs
- Contrôles (DC) : 1 h, 10 + 10 points (compréhension + langue), pas de production écrite : D01, D03, D05, D08. D07 (pilote, 2 h) suit le format d'examen 7 + 6 + 7.
- Synthèses (DS) : trois parties (D02 6 + 7 + 7, D04 7 + 6 + 7, D06 6 + 7 + 7), avec essai : portrait, article de presse, lettre argumentative.
- Textes supports : récit scolaire, reportage de presse (D07), lettre (D08, extrait de lettre du XVIIIe siècle, lexique soutenu au-delà du niveau). Le registre de langue du texte de D08 et de D07 est plus exigeant que les sujets d'examen.

## Notions par chapitre et nouveautés
- **01** : D08 hors ligne propre (négation absente des devoirs). **02** : D01, D02, D03, D05, D06, D08 (temps, but, cause/conséquence, relatives). **03** : D04, D07. **04** : jamais. **05+06** : conjugaison dans toutes les épreuves. **07** : D01, D02, D05, D07, D08. **08+09** : essais D02, D04, D06, D07. **11** : D02, D03. **12** : D04, D07. **13** : D02, D03, D06, D08 (couleur, tout). **14** : D01, D05, D07. **15** : D04 (article), D06 (lettre) : la lettre n'apparaissait qu'en 2011 technique.
- **Archétypes neufs par rapport aux lignes C01-C30** (pas de ligne `HP`, aucune notion hors manifeste) :
  - 02 : transformer des compléments de temps à l'infinitif en subordonnées (D03-4) ; reformuler avec « dès que » et « après que » en donnant le rapport temporel (D01-3, D01-4) ; but ou crainte (D05-2, D05-3) ; cause fausse avec « sous prétexte que » et corrélation (D08-4).
  - 11 : relative et adjectif de même sens dans le sens relative → expansion (D03-3) ; nature et fonction dans un tableau (D02-3).
  - 05+06 : plus-que-parfait contre imparfait (D02-5) ; simultanéité et antériorité avec « pendant que » et « avant que » (D03-6) ; valeur du conditionnel (D06-3).
  - 07 : sélection d'adjectifs dans une liste (D02-2) ; personnification (D08-2).
  - 13 : adjectifs de couleur (D02-6, D03-5).
  - 03 : passif « si possible » avec phrase non passivable (D07-3).
  - 15 : article de presse (D04-6), lettre argumentative (D06-4).
- Archétypes déjà vus aux examens : négation, subordonnée de cause ou de conséquence, pronoms personnels, « tout », s'en/sans, quand/quant/qu'en, adverbes en -ment, futur simple ou antérieur, synonymes en contexte.

## Règle des 30 %
Sur 45 lignes, 19 ont une signature neuve par rapport aux sujets d'examen (≈ 42 %) ; en retirant les huit lignes de compréhension (toutes propres au texte et jugées déjà vues), 19 sur 37, soit ≈ 51 %. Estimation : au-dessus de 30 %, une vague 2 se justifie (la 2e vague devrait viser la négation, le discours rapporté et les chapitres 04, 08, 15, absents ou rares).

## Difficultés
- D05 : police corrompue (texte illisible en extraction), lu en vision ; en-tête dont l'année contredit le registre.
- Barèmes décimaux : quand deux blocs adjacents donnent un entier ils ont été fusionnés (D01, D06, D07, D08) ; sinon la colonne vaut `-` (D03-3, D03-5, D07-2, D07-5) : le barème imprimé est 1,5, 1,25 ou 0,75.
- D06 : question de compréhension 3a porte une coquille (« ma musique ») ; D08 : incohérence 1,5 contre 1 sur l'orthographe .
- Anti-copie : archétypes et pièges rédigés dans mes mots ; contrôle automatique des suites de quatre mots contre les snapshots : seuls des termes de grammaire de consigne reviennent (reformulés pour la production et le passif).
