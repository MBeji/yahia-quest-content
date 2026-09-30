# Missions d'examen, maths 9ᵉ : travaux en cours (point de sauvegarde du 2026-09-30)

Cette branche `wip/…` **ne se merge pas**. Elle met à l'abri des lots non audités ou en cours
de correction pendant qu'une limite d'usage hebdomadaire (levée le 2026-10-03 à 12:00 UTC) peut
empêcher de lancer des agents. Chaque lot se livre, une fois audité et contre-vérifié, par une
branche fraîche depuis `main` : on y copie ses fichiers, on rejoue les gates, on met le registre
à jour, puis on publie (`apply-content.yml`, `subjects: math`).

## État des lots (plan : `plan/plan-examens-v5.json`, listes : `plan/assign-Lxx.md`)

| Lot | Chapitre | Fichiers | État |
|---|---|---|---|
| L19 | 20 | 17 à 21 | publié (privé#589) |
| L01 | 17 | 09 à 16 | auteur terminé ; correctifs du premier audit appliqués (44 questions) ; **contre-vérification à faire** (l'auditeur a été coupé) |
| L02 | 03 | 15 à 20 | auteur terminé ; **audit commencé** (fichiers 15 à 18 vus), à reprendre ; à arbitrer : volume de la pyramide (16, Q4) |
| L06 | 07 | 10 à 17 | audité (0 clé fausse, 9 majeurs, 18 mineurs : `audits/audit-L06.md`) ; **correctifs à appliquer** puis contre-vérifier ; ces fichiers sont l'état AVANT correctifs |
| L11 | 09 | 16 à 22 | auteur terminé (45 questions) ; **audit à faire** |
| L04 | 04 | 17 à 22 | auteur lancé, rien écrit |
| L03, L05, L07 à L10, L12 à L18 | | | à lancer, un auteur par chapitre à la fois, plages NN du plan |

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
