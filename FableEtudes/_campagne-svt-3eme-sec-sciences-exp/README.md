# Campagne SVT 3ème sec Sciences expérimentales — dossier de reprise (pause du 2026-11-24)

État à la pause :
- Fiche `content/programmes-officiels/programme/3eme-sec-sciences-exp/svt.md` : **validée R-7** (manuel 225333 lu en entier, 17 chapitres codifiés au manifeste).
- Chapitres **01 à 08 écrits, audités, mergés et publiés** en production (`svt-3eme-sec-sciences-exp`).
- **Reste : ch.09 à 17** (tranche 3 : ch.09-12 ; tranche 4 : ch.13-15 ; tranche 5 : ch.16-17). La tranche 3 a été arrêtée avant toute écriture : aucun fichier partiel.

Pour reprendre (procédure `campagne`, étape 4) :
1. Brancher le moteur (`campagne` étape 1).
2. Récupérer les PDF `225333P01..P03` du Drive dans `~/.cache/yqa-manuels/` seulement si une relecture est nécessaire (les auteurs n'en ont pas besoin : la fiche suffit).
3. Copier les consignes de ce dossier dans le scratchpad, puis relancer `workflow-tranche.js`. Il faut ajuster ses chemins `S` et ses arguments, par exemple pour la tranche 3 : `{"chapters":[{"n":"09","slug":"09-regulation-glycemie","sec":"T1.9","title":"La régulation de la glycémie","pages":"139–154"}, …]}`. Les slugs, sections et pages sont au §4 de la fiche et au manifeste.
4. Après chaque tranche : appliquer les MINOR restants, `content:gates`, commit (avec CATALOGUE et misconceptions), PR, merge, `apply-content.yml` (`subjects: svt-3eme-sec-sciences-exp`), puis `content-drift`.

Contenu du dossier :
- `BRIEF-LECTEUR-SVT.md`, `BRIEF-R7-SVT.md`, `BRIEF-AUTEUR-SVT.md` : consignes des sous-agents.
- `notes-lecture/` : notes des 8 lecteurs (plages, sondages, doutes, slugs).
- `r7/` : les 4 rapports de relecture R-7.
- `audits/` : les constats MINOR restés ouverts après les tranches 1 et 2, tous traités.
