# Prompt commun — auteur d'un lot du gisement arabe 9ᵉ (étude 36)

Tu es l'AUTEUR d'un lot du gisement : arabe 9ᵉ (matière `arabic`, items en arabe, élèves de 14–15 ans, année du concours), missions tirées des **sujets officiels de l'examen national de 9ᵉ** (corpus officiel : reprise fidèle et citée des textes et des questions).

## Lire d'abord
1. `/home/user/yahia-quest-content/.claude/skills/content-ingest/references/gisement-auteur-examen.md` EN ENTIER (pièges relevés aux audits compris) et `gisement.md` ; charge les skills `prof-arabe-9eme`, `content-ecole-tn`, `content-engine` (et `content-interactif` pour les types natifs).
2. Le plan : `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/arabe/PLAN.md` (règles §1, consignes d'auteur §3 « Pour les prompts d'auteur », écarts §4) et TA liste `assign-arabe-L0N.md` (même dossier).
3. Les transcriptions officielles : `/home/user/wt-argis/content/programmes-officiels/examens-nationaux/9eme-base/arabic/<session>.md` — seule source ; tu ne lis aucun PDF, aucun site.
4. Les chapitres où tu écris : `cours.md`, `resume.md`, `chapter.json`, et les missions existantes `exercices/01…06-*.json` (forme ; ne pas répéter leurs formulations).
5. Les audits des lots des autres matières, pour les défauts à éviter : `…/en-cours/audits/audit-L22.md`, `audit-SVT-L05.md`, `audit-T23-I.md` (fuites vers une autre question — le donjon tire les questions seules —, clé reconnaissable à sa forme ou par vote, doublons du publié, notions non enseignées sans définition, renvois positionnels, distracteurs que l'énoncé contredit).

## Où écrire
- Arbre de travail : `/home/user/wt-argis` (branche `wip/gisement-arabe-9eme`). Tu n'écris QUE tes fichiers de mission (`content/arabic/<chapitre>/exercices/<NN>-examen-*.json`, numéros et `displayOrder` de ta liste) et la ligne `sources[]` du `chapter.json` concerné si elle manque (texte exact au §3 du PLAN). D'autres auteurs écrivent en même temps dans d'AUTRES chapitres de cet arbre : n'y touche pas.
- Moteur : `/home/user/eng-argis` (lien `content` → `/home/user/wt-argis/content`) : `npm run -s content:check`, `content:qa 2>&1 | grep "arabic/"`, `content:tranche -- --subject arabic --chapters <NN>`, `npx prettier --ignore-path /dev/null --check content/arabic/…` (chemins relatifs), rendu `dir=rtl` (Chromium, `/opt/pw-browsers`).
- Notes AU FIL DE L'EAU : `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/arabe/auteurs-notes/L0N/NOTES.md` (une coupure de quota peut tomber à tout moment).

## Règles propres à l'arabe
- Chaque question dit sa session (« مناظرة 2025 ») quand la mission en mêle plusieurs, et redonne la phrase officielle qu'elle travaille ; un texte long se cite par extrait, référence de l'auteur telle qu'imprimée.
- Vocalisation et graphies telles que transcrites ; une coquille d'origine se signale au rapport, jamais corrigée en silence.
- Métalangage DU MANUEL (101908 / 101909) dans les items : celui des `cours.md` du chapitre ; un terme absent du cours est défini dans l'énoncé ou évité.
- Types natifs où la consigne l'appelle (`matching`, `ordering`, `multi`, `short_answer` pour une forme courte et unique avec `acceptedAnswers` vocalisées et non vocalisées) ; sinon QCM à 4 options, clé jamais strictement la plus longue, aucune réunion de deux distracteurs, chiffres occidentaux.
- Étiquettes : le registre `arabe.*` existe (`content/misconceptions.json`, ids posés sur les 19 chapitres) — pose un id EXISTANT quand son libellé dit exactement l'erreur du distracteur ; sinon muet. Une famille neuve se PROPOSE dans `…/en-cours/arabe/etiquettes-L0N.json`, jamais posée.
- Rien de `HP:` (§4 du PLAN) dans un item.

## Avant de rendre
Double résolution de chaque question (une seule juste, c'est la clé) ; contrôles moteur ci-dessus (rien de rouge qui nomme tes fichiers ; tranche : 0 clé strictement la plus longue sur tes questions) ; rendu `dir=rtl` de chaque question. Aucune écriture git. Rapport final court en français : fichiers, questions, types, adaptations, étiquettes, points « à vérifier par l'auditeur », contrôles.
