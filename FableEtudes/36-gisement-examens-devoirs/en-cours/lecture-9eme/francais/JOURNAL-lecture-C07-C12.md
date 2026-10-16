# Journal de lecture C07-C12 (9e français, sessions 2023, 2022, 2021, générale et technique)

Lot : C07 2023 générale, C08 2023 technique, C09 2022 générale, C10 2022 technique, C11 2021 générale, C12 2021 technique. `JOURNAL-lecture-C01-C06.md` n'existait pas à la prise du lot (constaté dans `lecture-9eme/francais/`, seul `lines/C01-C06.tsv` était là) : conventions reprises des lecteurs voisins (arabe : `1.1`, barème décimal à point, `<u>…</u>`, `……`, nom de fichier `<session>-<filiere>.md`) et du contrôle SVT (archétype <= 12 mots, piège 5-10 mots, aucun chiffre ni mot-nombre).

## Téléchargement et lecture
- `curl -g`, http, dans `/tmp/claude-0/frlec/src/` : six 200. Les six sha256 sont identiques au registre.
- `pdftotext` : 4 octets par fichier, aucune couche texte (scans). Lecture en vision, 150 DPI, 4 pages chacun, bonne lisibilité. Un zoom à 250 DPI sur la signature du texte de C12 (graphie de l'auteur).
- Transcriptions versionnées : `content/programmes-officiels/examens-nationaux/9eme-base/french/{2023,2022,2021}-{generale,technique}.md`. Snapshots hors dépôt : `/tmp/claude-0/frlec/snapshots/C07..C12.txt`.

## Conventions propres au français (à reprendre par les autres lots)
- **Texte support** : page 1 de chaque sujet, transcrit en tête sous `## Texte` (chapeau en italique, notes numérotées par exposants Unicode, source), puis `## Exercice 1 — Compréhension`, `## Exercice 2 — Langue`, `## Exercice 3 — Production écrite`, avec le barème de la partie dans le titre. Le texte n'est pas noté : il n'a pas de ligne.
- **Lignes** : une ligne par **question notée** (compréhension et langue), une ligne pour la **production**. `n°exo` = `partie.question` (`1.3` = compréhension, question 3 ; `2.2` = langue, question 2 ; `3` = production). Barème en points avec un point décimal (`1.5`), sous-questions a/b fusionnées dans la ligne de leur question.
- **Chapitres** : toute la compréhension, y compris le relevé d'indices, va à `09-comprehension-production-ecrite` ; production écrite à `08-types-de-textes-et-production-ecrite` (+ `04-discours-direct-et-indirect` quand le sujet impose de rapporter un dialogue). `10-annales-sujets-types` jamais employé. Pas de registre de compétences : colonne `-`.
- **Mot-nombre** : le contrôle SVT interdit aussi « deux », « trois », « quatre »… dans archétype et piège ; reformulé en « des », « plusieurs ».
- **Cases et lignes** : case vide `[ ]`, ligne de réponse `……`, soulignés `<u>…</u>`.

## Format de l'épreuve (identique sur les six sessions)
- **Générale** : 2 h, coef 1, 20 points = compréhension 7 + langue 6 + production 7.
- **Technique** : 1 h, coef 1, 20 points = compréhension 8 + langue 6 + production 6.
- Un texte narratif littéraire d'une page (extrait d'un roman, avec `[…]` et notes de vocabulaire), questions sur lignes pointillées, aucun document, aucune figure. Production : « une vingtaine de lignes » (générale), « une dizaine de lignes » (technique).
- Réponses écrites directement sur le sujet (lignes pointillées, cadres de note en marge en 2023 seulement).

## Notions de langue testées, par session et chapitre
| session | langue (barème) |
| --- | --- |
| 2023 générale | synonyme d'une locution + emploi (07) ; forme passive puis active (01+03) ; conjugaison après « après que » et avec « pendant que » (05+06) ; adverbes en -ment (14) |
| 2023 technique | sens d'un mot en contexte, deux QCM (07) ; forme négative, deux phrases (01) ; changement de sujet Henri → Sonia avec accords (13+12) |
| 2022 générale | synonyme du verbe + emploi (07) ; rapport de but et de conséquence liée à un degré d'intensité (02) ; imparfait ou passé simple (05+06) ; sans / s'en (14) |
| 2022 technique | synonyme + emploi dans un autre sens (07) ; rapport temporel (02) ; proposition relative remplacée par un adjectif (11+02) |
| 2021 générale | équivalent d'une locution dans le paragraphe (07) ; cause et but (02) ; passé simple ou imparfait (05+06) ; ni / n'y (14) |
| 2021 technique | sens d'un verbe en contexte, deux QCM (07) ; connecteurs et locution temporelle remplacés par un équivalent (07+02) ; remplacement de groupes nominaux par des pronoms (12) |
- Le programme est celui en vigueur : aucune notion `HP:`, aucune ligne `HP`. Notions jamais testées sur ces six sessions : `13-les-accords` hors 2023 technique, `15-article-de-presse-et-lettre`, figures de style (chapitre 07 réduit au lexique), `04` hors production.
- Les productions imposent le discours rapporté en récit (2023, 2022, 2021 générales) ; les techniques demandent un récit descriptif (portrait au travail, patron, sentiments).

## Points d'exactitude et difficultés
1. **C07 3.a** : « après que nous (évaluer) … vous (pouvoir) … » attend un futur antérieur puis un futur simple ; le futur antérieur n'est pas dans la liste du manifeste, rattaché à 05 par prudence : à confirmer au programme avant reprise.
2. **C07 2.b** : « La victime a été secourue » : le sujet de la phrase active n'existe pas ; la consigne appelle un sujet indéfini (« on ») ; réponse à cadrer avant reprise.
3. **C07 3.b** : « dans la cours » (sic, fautes d'impression pour « cour ») imprimé tel quel, transcrit sans correction.
4. **C09 2.4** : la consigne et les blancs fusionnent « sans » et « s'en » ; deux blancs consécutifs forment « sans s'en » ; transcrit tel quel. « A partir » sans accent imprimé en 2.2.
5. **C10 3.a** : « qui a été confectionnée » n'a pas d'adjectif de sens équivalent univoque (« sur mesure » n'est pas un adjectif) ; exercice à reprendre avec prudence. 3.b « qui brillent » → « brillantes », adjectif verbal et accord.
6. **C11** : « Un jour, c'est moi qui le battrais » (conditionnel imprimé dans le texte, pas dans une question) ; question 3 de langue en désordre de temps par rapport au passé simple en jeu : « Avant de passer mon brevet, je (prendre) » appelle un passé simple, forme jugée lourde pour le niveau.
7. **C12** : auteur imprimé « Mary HINGGINS CLARK » (graphie fautive d'origine), transcrit avec [sic]. Titre de section « (8points) » sans espace, conservé.
8. **C11 1.1** : les propositions sont étiquetées a/b/c sous une question elle-même étiquetée 1.a ; transcrit tel quel.
9. Aucun document illisible ou introuvable ; aucun statut à proposer autre que `lu` (transcription faite). Le texte support 2023 générale cite un enfant de dix ans ; sans effet sur la classe.
10. Aucune consigne n'a vieilli ; les sessions 2021-2023 emploient toutes « Examen du Diplôme de Fin de l'Enseignement de Base » (général ou technique).

## Bilan
| id | session | sha256 | exercices | lignes | durée | mode |
| --- | --- | --- | --- | --- | --- | --- |
| C07 | 2023 générale | c9f61992 | 3 | 9 | 120 | vision |
| C08 | 2023 technique | 95110c14 | 3 | 7 | 60 | vision |
| C09 | 2022 générale | 3cefbfd3 | 3 | 9 | 120 | vision |
| C10 | 2022 technique | 1ef93ffa | 3 | 8 | 60 | vision |
| C11 | 2021 générale | a049118f | 3 | 9 | 120 | vision |
| C12 | 2021 technique | 1d48d72c | 3 | 7 | 60 | vision |
