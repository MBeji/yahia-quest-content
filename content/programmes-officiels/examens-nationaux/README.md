# Sujets officiels des examens nationaux — transcriptions (étude 36, D-2)

Les sujets des examens nationaux sont du **corpus officiel** (méthode R-2, décision du
2026-09-28, étude 27 Q-6) : on peut les reprendre, en les citant. Ce dossier en garde la
**transcription fidèle**, une session par fichier. C'est le profil de source `examen-national`
de la méthode (§ Profils de source).

- **Chemin** : `<classe>/<matière>/<session>.md`. La session est l'année, suivie de la filière
  quand l'examen en a plusieurs la même année (`2021-generale.md`, `2021-technique.md`). Elle est
  l'année seule quand la filière est unique (`2005.md`).
- **En-tête YAML** : `source: officiel`, `examen`, `matiere`, `session`, `filiere`, `page` (le
  portail du Ministère), `fichier` (l'URL du PDF), `consulte_le`, `sha256`, `lecture`
  (`pdftotext`, `vision` ou `mixte`).
- **Corps** : un `## Exercice N (barème)` par exercice, le texte tel qu'imprimé. Les figures
  sont décrites entre crochets, avec toutes leurs données. Un item illisible est noté
  `[illisible]` ; un item hors du programme en vigueur est marqué
  `[hors programme en vigueur : <notion>]` et ne devient pas une question (R-3).
- **Usage** : chaque exercice devient une mission qui le reprend et le cite (`exercices/NN-examen-<session>-ex<N>-<slug>.json`,
  consigne `content-ingest/references/gisement-auteur-examen.md`). Son état se lit dans le
  registre du couple (`sources-externes/web-<classe>-<matière>/gisement.json`).
- **Hors de la garde anti-verbatim** : elle n'indexe que `sources-externes/` et `_sources/`, et la
  reprise est permise ici.
