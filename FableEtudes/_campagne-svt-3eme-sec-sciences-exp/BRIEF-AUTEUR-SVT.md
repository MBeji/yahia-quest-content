# Consigne commune — auteur d'un chapitre neuf, SVT 3ème secondaire Sciences expérimentales

Tu écris **un seul chapitre**, en entier et d'un seul passage, dans le corpus /home/user/yahia-quest-content. Le moteur est cloné dans /home/user/engine, et son dossier `content/` est un lien vers ce corpus. D'autres auteurs écrivent en même temps les autres chapitres de la tranche : ne touche jamais à leurs dossiers.

## Ta source unique : la fiche
- Fichier : /home/user/yahia-quest-content/content/programmes-officiels/programme/3eme-sec-sciences-exp/svt.md
- Lis la section de ton chapitre (indiquée dans ton message) et la partie du §6 qui le concerne : erreurs scientifiques du manuel, contradictions internes, valeurs lues à l'œil.
- N'ouvre aucun PDF.
- Le programme officiel gagne : rien d'inventé, rien hors des bornes ✅/⛔.
- **Une erreur du manuel marquée `[sic]` ne se reprend jamais.** Écris la version scientifiquement juste, ou évite le point.
- Quand le manuel se contredit, n'en fais pas une question.
- Une valeur lue à l'œil sur un graphique ne devient jamais une clé exacte.

## Ce que tu lis avant d'écrire
1. Règles d'écriture (dossier /home/user/yahia-quest-content/.claude/skills/) :
   - `content-engine/SKILL.md`
   - `content-engine/references/` : `content-schema.md`, `quality-bar.md`, `course-explanation.md` (patron de notion), `course-quality.md`, `course-figures.md`, `style-guide.md`, `rewards-and-modes.md`, `expert-exercises.md`
   - `content-ecole-tn/SKILL.md`
   - `prof-svt-lycee/SKILL.md`
2. **Modèle de forme** dans la même section de lycée : un chapitre récent complet, par exemple /home/user/yahia-quest-content/content/chimie-bac-sciences-exp/01-avancement-reaction-chimique/ (chapter.json, cours.md, resume.md, quiz.json, quatre exercices). Pour le ton SVT, survole aussi /home/user/yahia-quest-content/content/svt-1ere-sec/.
3. **Les chapitres déjà écrits de cette matière** : /home/user/yahia-quest-content/content/svt-3eme-sec-sciences-exp/, s'il y en a. Ne reprends pas leurs tâches.

## Ce que tu écris
Dossier : /home/user/yahia-quest-content/content/svt-3eme-sec-sciences-exp/<ton slug>/

- **`chapter.json`** :
  - `title` : titre avec sous-titre, dans le style des chapitres du corpus ;
  - `description` : liste précise des notions ;
  - `displayOrder` : ton numéro de chapitre ;
  - `sources` : d'abord « Programme officiel — Sciences de la vie et de la Terre, 3ème année de l'enseignement secondaire (section Sciences expérimentales), CNP Tunisie ; manuel élève 225333 (<titre du chapitre>, p.X–Y) », puis « Transcription du programme officiel — content/programmes-officiels/programme/3eme-sec-sciences-exp/svt.md (§T<n>) ».
- **`cours.md`**, au patron de notion. Pour chaque notion : ancrer → nommer → voir → exemple résolu → erreur typique → règle → `::: verifie`.
  - Au plus 8 notions.
  - En SVT, l'« exemple résolu » est souvent **l'exploitation d'un document** : un tableau de résultats ou une expérience, avec la démarche analyser → interpréter → conclure. Reprends les documents de la fiche (données exactes, source citée) ou des données d'illustration annoncées comme telles.
  - Figures en SVG inline selon `course-figures.md` : schémas légendés, graphiques avec axes et unités, tableaux. Chaque légende ne cite que ce qui est dessiné.
- **`resume.md`** : une puce par notion, dans l'ordre du cours.
- **`quiz.json`**.
- **Les quatre exercices**, dans `exercices/` : `01-pratique.json`, `02-boss.json`, `03-revision.json`, `04-defi.json`. Le défi monte vers l'exploitation de documents et le raisonnement expérimental, comme dans les exercices du manuel de la fiche.
- **Aucune mission d'examen** : il n'y a pas d'examen national en 3ème secondaire.

## Défauts récurrents à éviter (mesurés par les audits de 2026)
- Cours qui se contredit (tableau, exemple, piège, résumé).
- Règle énoncée en absolu.
- Distracteur absurde, contredit par l'énoncé, ou synonyme d'un autre.
- Clé la plus longue, la plus courte, ou seule marquée.
- Option « consensus ».
- Explication qui cite le rang d'une option.
- Question qui en révèle une autre, ou qui rejoue le `::: verifie`.
- Difficulté 3 sur du rappel.
- Notion testée mais non enseignée.
- Plus de 8 notions.
- Légende qui cite un repère absent du dessin.
- Valeur d'illustration non annoncée comme telle.

Refais chaque calcul (ration, énergie, bilan ATP, débits rénaux, proportions génétiques, âges radiométriques…). Un script Python est le bienvenu pour vérifier.

## Validation : obligatoire, sur ton seul chapitre
Lance depuis /home/user/engine :
```
npm run content:check
npm run content:qa:strict
npm run content:figures:check
npm run content:tranche -- --changed --fresh --strict-lessons
```
- 0 erreur dans ton chapitre ; les warnings qui le concernent sont traités.
- Si une étiquette `misconceptionTag` nouvelle est nécessaire, ajoute-la à /home/user/yahia-quest-content/content/misconceptions.json, au format existant. D'autres auteurs peuvent l'écrire en même temps : relis le fichier juste avant, et fais un remplacement ciblé.
- Ne lance ni `content:gates`, ni `content:catalogue`, ni `content:build`.
- Pas de SQL, pas de commit, pas de changement de branche.

## Rapport final
- Les fichiers écrits.
- Les notions.
- Le nombre de questions par fichier.
- La sortie résumée des commandes.
- Tes doutes : erreur du manuel évitée, borne interprétée.
