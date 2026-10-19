# Rapport — lot B1 (français 6ᵉ, chapitres 01 et 02)

Auteur : session B1, 2026-10-19. Aucun git.

## Fichiers (`content/french-6eme/`)
- `01-travailler-pour-sepanouir/` : `chapter.json`, `cours.md` (8 notions, 445 lignes), `resume.md` (8 cartes), `quiz.json` (5), `exercices/01-pratique … 05-entrainement` (6 questions chacun).
- `02-communiquer-avec-les-autres/` : mêmes fichiers (`cours.md` 8 notions, 430 lignes).
- Titres, difficultés et récompenses du patron : 01 d1 50/10, 02 boss d3 120/30, 03 révision d2 70/15, 04 défi d4 300/60, 05 entraînement d3 120/30.

## Chiffres
- 35 questions par chapitre (5 quiz + 30), 70 en tout. Types : mcq 49, matching 6, multi 6, ordering 5, short_answer 4 (≤ 1/3 par mission, aucune dans un quiz).
- Taux d'étiquetage des distracteurs de QCM : M1 56/72 = 78 %, M2 67/75 = 89 %. Aucune étiquette sur `multi`/`ordering`/`matching`. Aucun id hors registre (`content:check` vert).
- `coursePitfalls` : M1 6 ids (`gn.nom-propre-commun-confondus`, `reprise.substitut-ne-correspond-pas`, `temps.compose-mal-identifie`, `conj.infinitif-mal-retrouve`, `conj.infinitif-apres-preposition-oublie`, `recit.contradiction-non-vue`) ; M2 6 ids (`det.demonstratif-mal-choisi`, `pronom.possessif-accorde-au-possesseur`, `conj.imperatif-avec-sujet`, `conj.imperatif-s-2e-personne`, `homophone.a-a-confondus`, `recit.element-modificateur`). Chacun est montré dans un bloc `::: piege` et porté par au moins un distracteur du chapitre.
- Contrôles : `content:check` vert ; `content:qa -- --subject french-6eme` 0 erreur, 0 avertissement ; `content:tranche … --fresh --strict-longest` : clé la plus longue 0/49, positions 20/33/22/24 %, paires proches 0, gabarit 0, patron de notion 0 en recul ; `prettier --check` vert ; rendu `renderLesson`/`renderSummary` des 4 fichiers sans `:::` résiduel (vitest jetable supprimé).

## Reprises du cahier / du manuel déclarées (champ `manuel` de l'exercice)
- M1 `01-pratique` (121615P00, p. 4, 7-8) : ex. 1 p. 4 (sous-ensemble), ex. 2 p. 4, ex. 3a p. 7 (+ une phrase ajoutée), ex. 1 p. 7, ex. 3b p. 8.
- M1 `03-revision` (121615P00, p. 9-10, 12) : ex. 1a p. 9, ex. 2a p. 9-10 (légendes raccourcies), ex. 1 p. 12 (titre à retrouver), ex. 2a p. 12.
- M1 `05-entrainement` (121614P00, p. 23) : jeu 4 p. 23 (annonces raccourcies).
- M2 `01-pratique` (121615P00, p. 19) : ex. 1, 2 (en `short_answer`) et 3 (sous-ensemble).
- M2 `02-boss` (121615P00, p. 23) : notice « Mon porte-revues » remise à l'impératif.
- M2 `03-revision` (121615P00, p. 25-26) : ex. 1 p. 25, ex. 2b p. 25, ex. 4a p. 26.
- M2 `04-defi` (121615P00, p. 24) : ex. 3 p. 24.
- M2 `05-entrainement` (121614P00, p. 39) : jeu 1 et jeu 2 p. 39.
- Les reprises partielles ou raccourcies sont des reprises adaptées (régime b) ; le reste est variante, non tracé. Un exercice ne porte qu'un livre : pas de traçabilité croisée 121614/121615 dans le même fichier.

## Écarts à la fiche
- `Impératif négatif` (tableau C, enrichissement) : seulement une phrase d'exemple en cas limite dans le cours M2 ; aucune question ne le cible, bien que le cahier M2 J3 ex. 3 propose une transformation affirmatif/négatif.
- Schéma du récit en M2 : « situation de départ, élément perturbateur, actions, situation finale » (vocabulaire du cahier, fiche §2.10 A) ; en M1 : début, suite, fin (grille du guide). Aucun terme de la grille narratologique ⛔ (équilibre, manque, épreuves).
- Passé composé en M1 : reconnu uniquement (« a/est + participe »), jamais conjugué (borne M1).
- Pas de leçon ni de question sur les textes injonctifs (le « tableau » découpé, la « Une »), les poèmes, la lecture rapide, l'autodictée ni la dictée (pas d'audio) : le projet d'écriture est préparé en fermé (ordonner, repérer les contradictions, choisir le remplaçant ou la fin).
- Poèmes, textes 1 à 6 : citations évitées ; les supports sont des paraphrases écrites pour la question.

## Doutes pour l'auditeur
1. Cours M2, règle du s de l'impératif : reprise de l'encadré du manuel p. 30 (« verbes en -ir ou en -re prennent un s »). Des verbes en -ir comme *ouvrir* (*ouvre*) font exception ; l'ancre du cours évite *ouvre* et la règle est limitée aux modèles du module.
2. M2 `05-entrainement` Q2 (Sandra) : l'ordre *enregistrer avant imprimer* est une déduction (le manuel n'imprime pas de corrigé) ; le cours l'énonce.
3. M1 `05-entrainement` Q2 (mots-outils *soudain*) : trois distracteurs étiquetés `lexique.mot-voisin-du-meme-champ` (même famille de mots-outils) ; étiquette défendable mais proche du jugé. M1 `04-defi` Q2 et `03-revision` Q3 : distracteurs de métiers laissés muets (pas d'erreur reconstructible).
4. M1 `01-pratique` Q4 (multi) et M2 `01-pratique` Q5 (multi) ajoutent une phrase aux données du cahier : adaptées, tracées dans les items de l'exercice.
5. Lexique M1 : le tableau du cours teste 14 métiers ; ceux des annonces du manuel (p. 23) ont été ajoutés au cours pour respecter la règle d'or.
6. Aucun id manquant à proposer au registre.

## Corrections après audit
Tous les correctifs de `audits/audit-B1.md` sont appliqués avec les textes de l'auditeur : C-1 à C-3 (quiz 01 q5, 04-defi q4, 01-pratique q6), M-1 à M-6 (dont s de l'impératif : `retenir`, résumé et ligne *ouvrir* ; Sandra « imprime le document enregistré » avec `manuel.items` réduit à `jeu 1 p. 39` ; Sylvie réécrite), m-1 à m-6, m-8 à m-14 (muets souvent/toujours/parfois/Quatre ; étiquettes retaguées sur 03 q3 et 05 q4 du chap. 02). m-7, m-15 et m-16 : aucune action (observations).
- F8 : exemple d'impératif négatif conservé, aucune question ajoutée.
- F9 : tableaux de plus de 3 colonnes scindés (temps du chap. 01 en deux tableaux ; possessifs, impératif — 6 colonnes, un tableau par paire de verbes —, et a/à du chap. 02). Je n'ai pas mesuré les 4 colonnes en Chromium : scission par prudence.
- Écart assumé : pour m-2 et m-10, les explications des `short_answer` nomment désormais la réponse (texte de l'auditeur), contre la consigne du schéma ; `content:qa` ne les signale pas.
- Contrôles relancés sur le corpus réel : `content:check` vert, `content:qa` sans erreur, `content:tranche` clé la plus longue 0/49, `prettier --check` vert, rendu des cours et résumés sans `:::` ni astérisque (vitest jeté).

## Missions du gisement (lot M1)
Fichiers (`content/french-6eme/`), 66 questions :
- `01/exercices/06-exams-2009-2025-temps-de-la-phrase` (m001, d2, 8 q) ; `07-devoir-classer-les-mots` (m002, 6 q) ; `08-devoir-presenter-un-metier` (m003, 6 q).
- `02/exercices/06-exams-2015-2025-ce-cet-cette-ces-mon-son-leur` (m004, 10 q) ; `07-exams-2009-2026-imperatif-fais-parler` (m005, 11 q) ; `08-exam-2026-lecture-dix-jours-sans-ecran` (m006, 10 q) ; `09-exams-2013-2026-recit-dispute-ecrans` (m007, d3 boss, 8 q) ; `10-devoir-relier-enumerer-rediger` (m008, 7 q).
- `chapter.json` des deux chapitres : lignes `sources[]` examens et devoirs ajoutées. Aucune étiquette créée.

Étiquetage des distracteurs de QCM : m001 20/24, m002 10/12, m003 12/12, m004 16/30, m005 25/30, m006 21/27, m007 13/15, m008 9/12. m004 est bas : possessifs et accord « changer de personne » (votre/vos, mes/mon…) n'ont pas d'id exact (muets honnêtes).

Contrôles : `content:check` vert ; `content:qa` 0 erreur ; `content:tranche` clé la plus longue 0/103, positions 22/30/22/25 % ; `prettier --check` vert ; `content:gisement:controle` sur les 3 fichiers de devoir : 0 plage de 8 mots. Paires proches restantes (4) : les deux vides d'une même phrase officielle (m004 q1-q2, q3-q4, q7-q8) et deux questions sur un même texte de devoir (m008 q1-q3, 0,46) : exercices parallèles voulus, données identiques par construction. Gabarits : 3 groupes « synonyme/contraire d'un texte » partagés avec les chapitres 05, 06, 08 des autres lots (geste imposé par l'épreuve).

Adaptations et écarts :
- m006 q1 : le sujet demande de cocher les personnages qui « rejettent » l'idée ; la clé officielle n'étant pas publiée (Louis se moque, Gordon prédit l'échec, Pablo s'en indigne), la question redonne la consigne puis demande « quel personnage annonce l'échec » (Gordon seul). q3 (qui dit « chouette ») est une déduction ajoutée ; m006 n'a pas de question libre sur « donne deux éléments » : QCM et `multi`.
- m005 : 11 questions (item 2022 réduit à « apprenez » avec « faites » donné pour ne pas redemander `02/02-boss#4`) ; « soyez » : le paradigme d'être est donné dans l'énoncé (rappel), il n'est pas enseigné au chapitre. « venez », « reviens », « apprenez » : formes de verbes d'un chapitre ultérieur ou hors liste, tous donnés ou à choisir parmi les options.
- m008 : les deux appariements sont équilibrés (3/3), le `matching` n'admet pas d'option en trop ; la troisième question est un QCM de vérité d'après le texte (permutation des personnages en leurre).
- m004 q7 : « Cette nuit-là » ; q5 : le blanc « toutes » est donné ; m004 q3-q4 : le blanc « nombreuses » est donné.
- Items écartés : aucun de la carte ; C11#8 et C01#8 hors lot.
- Notions données dans l'énoncé : paradigme de l'impératif d'être (m005), consignes officielles redonnées à chaque question.
- Doutes : m006 q8-q10 (synonymes/contraires) : les clés « stupide », « désagréable », « plaisir » sont ma lecture, le sujet ne publie pas de corrigé ; m003/m002 sont des textes inventés (salle blanche, la carte seule lue).
