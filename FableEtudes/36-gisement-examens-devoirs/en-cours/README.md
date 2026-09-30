# Missions d'examen, maths 9ᵉ : travaux en cours (point de sauvegarde du 2026-09-30, mis à jour à 07:00 UTC)

Cette branche `wip/…` **ne se merge pas**. Elle met à l'abri des lots non audités ou en cours
de correction pendant qu'une limite d'usage hebdomadaire (levée le 2026-10-03 à 12:00 UTC) peut
empêcher de lancer des agents. Chaque lot se livre, une fois audité et contre-vérifié, par une
branche fraîche depuis `main` : on y copie ses fichiers, on rejoue les gates, on met le registre
à jour, puis on publie (`apply-content.yml`, `subjects: math`).

## État des lots (2026-09-30, 08:00 UTC) — plan : `plan/plan-examens-v5.json`, listes : `plan/assign-Lxx.md`

Livrés et publiés (privé#589, #595, #597, #598, #599) : L19 (chapitre 20), L01 (17), L02 (03), L06 (07), L11 (09). Les étiquettes d'erreur manquantes de L02, L06 et L11 ont été créées en un passage (privé#601 ; outil `outils/apply-tags.py`, listes dans `etiquettes/`).

| Lot | Chapitre | Fichiers | État |
|---|---|---|---|
| L03 | 03 | 21 à 26 | auteur terminé ou presque ; fichiers de cette branche = état à 08:00 ; audit à faire |
| L04 | 04 | 17 à 22 | auteur terminé (38 questions) ; audit à l'aveugle en cours |
| L07 | 07 | 18 à 24 | fichiers écrits ; audit à faire |
| L12 | 09 | 23 à 29 | auteur en cours (1 fichier sur 7 à 08:00) |
| L05, L08, L09, L10, L13 à L18 | | | à lancer, un auteur par chapitre à la fois, plages NN du plan |

Aussi à faire, une fois les lots livrés :
- créer en **un seul passage** les étiquettes d'erreur manquantes (les auteurs n'en créent pas : `misconceptions.json` est partagé) et les poser sur les options concernées ;
- compléter les cours qui n'enseignent pas ce que l'examen teste : chapitre 04 (|X| ≤ a ⟺ −a ≤ X ≤ a), chapitre 07 (étendue, classe modale, effectifs cumulés, polygone, médiane graphique, « الموسّط ») ;
- lots de devoirs restants : G2 (chapitre 04, 5 missions) et I (chapitre 09, 5 missions), à numéroter après les lots d'examen de leur chapitre.

## Ce que contient le dossier

- `plan/` : le plan des 19 lots, une liste par lot, le gabarit de consigne d'un auteur (`prompt-template.md`) et celle du lot L11 (`prompt-L11.md`).
- `audits/` : les rapports d'audit à l'aveugle déjà rendus (L01, L06).
- `outils/` : les scripts du registre (`registre-add.py`, `registre-set.py`, `registre-docs.py`), `gen-exam-assign.py` (génère les listes) et `add-source-line.py` (ligne `sources[]` d'un `chapter.json`).

Le contrôle anti-copie des devoirs en ligne exige les transcriptions lues (`pilot/snapshots`,
`gisement/9eme-math/snapshots`), qui ne sont pas versionnées.
