# Journal de lecture des devoirs D01-D06 (9e arabe, vague 1, devoir.tn)

Lecteur G2, 2026-10-18. Sources web : rien n'est repris, aucune transcription versionnée. Sorties : `lines/D01..D06.tsv` et `.meta`, snapshots hors dépôt `/tmp/claude-0/devoirs-snapshots/arabic/<id>.txt` (consignes, barèmes et résumé du texte seulement, textes supports non copiés), PDF et rendus dans `/tmp/claude-0/ardev/`. Aucune écriture dans `gisement.json`, `lignes.tsv` ni git. Conventions : n°exo = rang d'ordre, une ligne par question notée, production = dernière ligne, compétences `-`, `HP:mushtaqqat` et `HP:i3rab-wal-bina` à la place des deux dossiers hors manifeste (consigne du coordinateur).

## Téléchargement
- URL de `machine-list.tsv` valides, `curl -g`, `CURL_CA_BUNDLE=/root/.cache/yqa-ca/ca-bundle.pem`, jamais `-k`. Les six sha256 téléchargés égalent le registre.
- `pdftotext` inutilisable : vide (D02, D04, D06) ou en formes de présentation à ordre brouillé (D01, D03, D05). Les six sont lus en vision à 150 DPI (le texte vocalisé de D03 et D05 se lit sans difficulté).

| id | créneau | sha256 (début) | pages | lecture | lignes | auteur imprimé | établissement | année imprimée |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D01 | DC1 | 9d78ed7a | 3 | vision | 9 | Ramzi Hamdoun | institut privé Ibn Sina | 2021/2022 |
| D02 | DS1 | 7f90811c | 4 | vision | 13 | aucun (plateforme Tadris.TN) | aucun | non imprimée (fichier 2023-2024) |
| D03 | DC2 | 983461cb | 3 | vision | 10 | Taher Chabbi | E.P. El Mezzara | non imprimée (texte daté 2014-01-24, fichier 2013-2014) |
| D04 | DS2 | 10d78d6b | 4 | vision | 16 | aucun (« أساتذة السنوات التاسعة ») | E.P. Hay Ibn Khaldoun | 2016-05-28 (année 2015-2016) |
| D05 | DC3 | 536ed53d | 3 | vision | 8 | Taher Chabbi | E.P. El Mezzara | non imprimée (texte daté 2013-02-26, registre 2014) |
| D06 | DS3 | fefba33c | 3 | vision | 7 | Lotfi Zarrouk | E.P. El Mahatta, Bou Salem | 2018/2019 |

Total : 63 lignes, `content:gisement:lignes` : 6 fichiers, 63 valides, 0 fautive.

## Écarts au registre
- **Auteurs** : le registre n'en porte qu'un (D01) et Tadris.TN (D02) ; l'en-tête donne Chabbi (D03 et D05) et Zarrouk (D06). D04 n'a pas d'enseignant imprimé.
- **D04** : registre 2017 (nom de fichier 2016-2017), la date imprimée 2016-05-28 donne l'année 2015-2016.
- **D03 et D05** : registre 2014 pour les deux ; l'année scolaire n'est imprimée sur aucun des deux, D05 cite un article de février 2013 (probable 2012-2013 ou 2013-2014).
- **D02** : année absente du document ; la 4e page est une publicité (pas d'exercice).
- **Collège** : D01 est un institut privé, que le registre classe « ordinaire » : conforme à l'esprit « non pilote », pas de démenti sur le fond. Aucun document ne s'annonce pilote : l'alternance pilote/ordinaire de D-4 n'est pas tenue (six ordinaires) — le rayon « arabe » de devoir.tn n'offre pas de pilote dans cette vague.
- **Créneaux** : les six correspondent (D02 est un « entraînement à l'examen de synthèse 1 »).

## Plafond par auteur (D-4 : au plus deux)
Chabbi : D03 + D05 = 2 (au plafond). Hamdoun 1, Zarrouk 1 ; D02 et D04 sans auteur. Plafond respecté.

## Année et programme
- D02 (2023-2024) seul relève du programme révisé (appel, souhait, phrase réduite, nom allongé) : `en vigueur`.
- D01 (2021-2022), D03 (2013-2014), D04 (2015-2016), D05 (2012-2014), D06 (2018-2019) précèdent la révision : `mixte`. Leurs notions sont presque toutes au manifeste (استفهام، شرط، دلالة الزمان، العدد، التصغير، النسبة) ; seul D01 mobilise de l'ancien (verbe de transformation, sujet réel) en `HP`.
- La règle D-4 « année scolaire du programme en vigueur » n'est donc tenue que par D02 : à arbitrer par le pilote (cinq devoirs à garder comme sources de signatures ou à remplacer par une vague 2 récente).

## Format
- Contrôles (DC1-DC3) : 1 h, compréhension 4-5 points + langue 10-14 + production 6 (D01 : 4 + 10 + 6 ; D03 : 4 + 10 + 6 ; D05 : 4 + 10 + 6), proches de l'épreuve nationale générale réduite.
- Synthèses (DS1-DS3) : D02 (4 + 6 + 10), D04 (5 + 10 + 5), D06 (4 + 10 + 6). Textes : argumentatifs ou essayistiques ; D01 et D03 portent sur la femme et l'emploi.
- Aucun devoir ne comporte de « الإنشاء العربي » seul ; toutes les épreuves ont compréhension, langue, production.

## Notions par chapitre (lignes)
- **10-fahm-wa-intaj** : compréhension de D01 à D06 (21 lignes en comptant les doubles). **09-al-intaj-al-kitabi** : les six productions, plus l'identification d'arguments (D02, D04, D05).
- **15** : D01 (liaison, 2 lignes), D02 (rang des incises, reprise).
- **04** : D02 seulement (réduite, appel, souhait réduit).
- **16** : D03 (réponse à question négative, deux questions sur un élément).
- **17** : D03 (possibilité, impossibilité), D05 (réécriture à trois outils).
- **18** : D04 (cinq lignes), D05, D06 : dominante des devoirs de synthèse.
- **03** : D01, D04, D05, D06 (fonction d'un complément ou d'une proposition de temps).
- **19** : D04, D06. **12** : D02 (trois lignes). **05** : D03 (deux lignes). **13** : D04, D05 (deux lignes). **14** : D04, D06.
- **02, 07, 08** : jamais.

## Part HP
Sur 63 lignes : 4 lignes comportent un `HP` (D01 : verbe de transformation, sujet réel, schème et racine ; D02-12 : participes actif et passif), soit 6 %, toutes en `mushtaqqat` ou acquis de 7e-8e. Aucune ligne n'est tout `HP` sauf D01-4, D01-7, D01-8. `HP:i3rab-wal-bina` n'est pas employé.

## Difficultés
- Lecture en vision obligatoire (pas de couche texte) ; barèmes décimaux conservés (0.5, 0.75, 1.25 ...) et acceptés par le validateur.
- D03 : trois « 1 » consécutifs dans la marge, rattachés aux sous-questions dans l'ordre imprimé (total 20 vérifié) ; D04 : tableau de trois groupes verbaux compté en une ligne.
- D02-5 (rang des phrases entre crochets) et D02-7 (phrase réduite) : rattachements à 15 et 04 par la terminologie du manuel révisé.
- Anti-copie : archétypes et pièges en français dans mes mots, sans nombre ni personnage ; le snapshot ne transcrit que consignes, barèmes et titres.
