# Rapport — lot B3 (05-sauver-la-nature, 06-etre-en-forme)

**Fichiers** : `content/french-6eme/05-sauver-la-nature/` et `06-etre-en-forme/` — chacun : `chapter.json`, `cours.md` (7 sections), `resume.md` (7 cartes), `quiz.json` (5 q.), `exercices/01-pratique` d1 50/10, `02-boss` d3 120/30, `03-revision` d2 70/15, `04-defi` d4 300/60, `05-entrainement` d3 120/30 (6 q. chacun) = 35 questions par chapitre, 70 au total.

**Étiquetage** : ch. 05 69/81 distracteurs de QCM = 85 % ; ch. 06 78/87 = 90 %. Tous les `coursePitfalls` (6 + 6) sont portés par au moins un distracteur.

**Variété** : ch. 05 — 27 QCM, 2 ordering, 2 multi, 1 matching, 3 short_answer ; ch. 06 — 29 QCM, 3 ordering, 3 multi, 1 matching, 1 short_answer (jamais de tag sur ces types, sauf `expectedMistakes` des short_answer).

**Reprises du cahier 121615 déclarées** : ch. 05 `03-revision` (p. 58, 65, 67 : ex. 2 p. 58 en appariement, ex. 1 p. 65, ex. 2, 3 et 4 p. 67 en QCM / réponses libres) ; ch. 06 `03-revision` (p. 70, 72, 79 : ex. 1 et 3 p. 70, ex. 2 p. 72, ex. 2 p. 79). Les phrases sont reprises, les formats adaptés (QCM, multi) ; une question de chaque fichier est une variante.

**Contrôles** (copie d'engine limitée aux deux chapitres) : `content:check` OK (60 questions) ; `content:qa` 0 erreur, 0 avertissement ; `content:tranche --fresh --strict-longest` : clé la plus longue 0 %, patron de notion 0 en recul ; prettier OK ; rendu `renderLesson` / `renderSummary` OK (vitest jetable supprimé).

**Écarts à la fiche / choix** : comparaisons (« froid comme… »), proverbes, charade, rébus, test sur les oiseaux et origami non repris (jeux, pas de notion enseignée). « Plutôt / bientôt » rattachés à la section de vocabulaire. Les compléments de temps et de manière (M7) sont seulement nommés comme réponses à « quand ? » / « comment ? » pour montrer ce qui n'est pas un lieu. Aucun id manquant à proposer au registre.

**Doutes pour l'auditeur** : (1) `pourtant` / `c'est pourquoi` en 05 sans étiquette ; (2) 4 paires proches voulues (questions de lecture sur un même texte support, définitions de vocabulaire) ; (3) groupe gabarit « Écris le verbe entre parenthèses au présent » ×4 : parallèle voulu (cahier p. 67 ex. 4) ; (4) une demi-phrase du cahier p. 58 ex. 2 est regroupée (« de son projet à ses amis ») ; (5) figure SVG du ch. 06 (village de Tulmac) à vérifier visuellement.

## Corrections après audit

Tous les correctifs de `audits/audit-B3.md` sont appliqués avec les textes de l'auditeur : M-1 à M-14, § 5 (copies du cours : 06 boss q1, 06 défi q6, 05 défi q5), m-2 à m-9, m-11 ; M-7 et M-10 avec les ids ajoutés par le pilote (déclarés en `coursePitfalls` : 05 → 9 ids, 06 → 9 ids) ; piège « répétition du nom » transformé en puce de règle ; question « parties de la lettre » du 06 transformée en appariement ; figure de Tulmac remplacée et boss q6 remplacé par la bibliothèque ; F9 : conjugaisons scindées en deux tableaux à 3 colonnes, tableau « complément essentiel » réduit à 3 colonnes, en-têtes raccourcis (« Sujet », « Lieu »).

Écarts : M-13 est étiqueté « 05-entrainement » dans l'audit mais décrit les questions du **06** (régime / appariement) : appliqué au 06-entrainement q1 ; le 05 garde « recycler ». m-10 (étalonnage d2 des deux questions du défi) non appliqué : elles restent d3 pour ne pas casser la rampe 2-2-3-3-3-3 du défi.

Contrôles sur le corpus réel : `content:check` OK ; `content:qa` 0 erreur ; `tranche --fresh --strict-longest` : clé la plus longue 0 %, patron de notion 0 en recul, 3 paires proches voulues (questions de défi sur un même texte) ; prettier OK ; rendu Chromium 360 px : aucun mot coupé dans les tableaux, pas de défilement horizontal, figure de Tulmac lisible (328 px).
