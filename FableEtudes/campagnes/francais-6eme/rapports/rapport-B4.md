# Rapport B4 — chapitres 07-profiter-du-temps-libre et 08-autres-modes-de-vie

Fichiers : `content/french-6eme/07-profiter-du-temps-libre/` et `08-autres-modes-de-vie/` (chapter.json, cours.md, resume.md, quiz.json, exercices 01 à 05).

## Chiffres
- 2 chapitres, 12 fichiers JSON de questions, 70 questions (5 de quiz + 30 d'exercices par chapitre).
- Cours : 8 sections par chapitre, patron de notion complet (ancrage, définition, tableau, exemple raisonné, piège, propriété avec cas-limite, vérifie, retenir) ; résumés à 8 puces (bijection).
- Types : 07 = 25 QCM, 4 multi, 2 ordering, 1 matching, 2 short_answer, 1 numeric ; 08 = 26 QCM, 3 multi, 3 matching, 2 short_answer, 1 ordering.
- Étiquetage des distracteurs QCM : 07 = 50/75 (67 %), 08 = 47/78 (60 %). Jamais sur multi, ordering, matching.
- coursePitfalls : 6 par chapitre, chacun montré dans un bloc `::: piege` et porté par au moins un distracteur (content:qa vert).
- Contrôles (sur un miroir du corpus limité à mes deux dossiers, les autres chapitres étant en cours d'écriture) : `content:check` vert ; `content:qa` et `qa:strict` 0 erreur 0 avertissement ; `content:tranche --fresh --strict-longest --strict-lessons` : clé la plus longue 0/51, 0 paire proche, 0 gabarit, patron de notion 0 en recul ; prettier --check vert ; rendu `renderLesson` / `renderSummary` vérifié par un test jetable (supprimé).

## Reprises du cahier 121615 déclarées (champ `manuel`)
- 07/03-revision : p.85 ex.2a (ordering), p.87 ex.1 et ex.2, p.94 ex.4a (multi).
- 07/05-entrainement : p.93 ex.1 (un item, QCM « neuf → neuve »).
- 08/01-pratique : p.97 ex.1 (multi), p.99 ex.3 (deux items).
- 08/03-revision : p.97 ex.2, p.99 ex.3, p.103 ex.1b, p.108 ex.2.
- 08/05-entrainement (manuel 121614, jeux p.132) : ex.3 (intrus), ex.4 (contraires, matching), ex.5 (proverbe).
Tous les autres items sont des variantes (non tracées), notamment toutes les lettres et tous les récits.

## Écarts à la fiche et choix
- Aucun fait « à arbitrer » ni ⛔ n'est enseigné ou ciblé (F1) ; F5 respecté : aucune question sur l'accord avec avoir. Le cours 08 contient une seule phrase de cas-limite reprenant le constat du manuel p.125 (« avec avoir, le participe ne s'accorde pas avec le sujet »), rangé ✅ aux bornes du §2.8 : l'auditeur peut la retirer si F5 doit être lu plus strictement.
- Le cahier p.108 ex.1 (mélange avoir, imparfait) et p.98 ex.2 (capitales) ne sont pas repris (voir `auteurs-notes/B4/NOTES.md`).
- Aucun id manquant au registre `fr.*` : tout est posé avec les ids existants. Pistes pour une campagne suivante (non ouvertes, seuil de 3 questions non atteint) : « veux/peux avec nous » (terminaison de la mauvaise personne), « par taxi » (préposition de manière).
- `exercices/04-defi` : seuls ordering, matching, multi et short_answer ont des clés non étiquetables ; la part muette vient surtout des distracteurs de conjugaison à autre personne (veulent, pouvons…), laissés muets selon la règle R3.

## Doutes pour l'auditeur
1. 07/03-revision #1 (« Dites-moi votre avis ») : bien vérifier qu'aucune autre option n'est défendable.
2. 07/05 #4 (nombre pensé) : listes de 1 à 15 originales (code binaire), calcul revérifié (6 = 2 + 4).
3. 08/04-defi #6 et 07/03-revision #4 : questions de lecture sur textes courts maison ; vérifier qu'un indice du texte tranche.
4. 08 cours section 7 : proverbe « Petit à petit, l'oiseau fait son nid » et comparaisons animales (taureau, lapin, escargot, gazelle) venues du vocabulaire du manuel p.132 ; le proverbe « Tous les chemins mènent à Rome » n'est que dans l'exercice 05 (reprise).
5. Gabarits : la structure « quel groupe est le complément de temps / de manière » revient dans les deux chapitres (notions parallèles) ; formulations variées pour limiter l'effet de gabarit.
