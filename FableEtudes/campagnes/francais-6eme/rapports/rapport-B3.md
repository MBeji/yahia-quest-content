# Rapport — lot B3 (05-sauver-la-nature, 06-etre-en-forme)

**Fichiers** : `content/french-6eme/05-sauver-la-nature/` et `06-etre-en-forme/` — chacun : `chapter.json`, `cours.md` (7 sections), `resume.md` (7 cartes), `quiz.json` (5 q.), `exercices/01-pratique` d1 50/10, `02-boss` d3 120/30, `03-revision` d2 70/15, `04-defi` d4 300/60, `05-entrainement` d3 120/30 (6 q. chacun) = 35 questions par chapitre, 70 au total.

**Étiquetage** : ch. 05 69/81 distracteurs de QCM = 85 % ; ch. 06 78/87 = 90 %. Tous les `coursePitfalls` (6 + 6) sont portés par au moins un distracteur.

**Variété** : ch. 05 — 27 QCM, 2 ordering, 2 multi, 1 matching, 3 short_answer ; ch. 06 — 29 QCM, 3 ordering, 3 multi, 1 matching, 1 short_answer (jamais de tag sur ces types, sauf `expectedMistakes` des short_answer).

**Reprises du cahier 121615 déclarées** : ch. 05 `03-revision` (p. 58, 65, 67 : ex. 2 p. 58 en appariement, ex. 1 p. 65, ex. 2, 3 et 4 p. 67 en QCM / réponses libres) ; ch. 06 `03-revision` (p. 70, 72, 79 : ex. 1 et 3 p. 70, ex. 2 p. 72, ex. 2 p. 79). Les phrases sont reprises, les formats adaptés (QCM, multi) ; une question de chaque fichier est une variante.

**Contrôles** (copie d'engine limitée aux deux chapitres) : `content:check` OK (60 questions) ; `content:qa` 0 erreur, 0 avertissement ; `content:tranche --fresh --strict-longest` : clé la plus longue 0 %, patron de notion 0 en recul ; prettier OK ; rendu `renderLesson` / `renderSummary` OK (vitest jetable supprimé).

**Écarts à la fiche / choix** : comparaisons (« froid comme… »), proverbes, charade, rébus, test sur les oiseaux et origami non repris (jeux, pas de notion enseignée). « Plutôt / bientôt » rattachés à la section de vocabulaire. Les compléments de temps et de manière (M7) sont seulement nommés comme réponses à « quand ? » / « comment ? » pour montrer ce qui n'est pas un lieu. Aucun id manquant à proposer au registre.

**Doutes pour l'auditeur** : (1) `pourtant` / `c'est pourquoi` en 05 sans étiquette ; (2) 4 paires proches voulues (questions de lecture sur un même texte support, définitions de vocabulaire) ; (3) groupe gabarit « Écris le verbe entre parenthèses au présent » ×4 : parallèle voulu (cahier p. 67 ex. 4) ; (4) une demi-phrase du cahier p. 58 ex. 2 est regroupée (« de son projet à ses amis ») ; (5) figure SVG du ch. 06 (village de Tulmac) à vérifier visuellement.
