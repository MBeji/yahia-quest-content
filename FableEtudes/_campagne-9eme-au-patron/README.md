# Campagne « 9ᵉ au patron » — dossier de travail versionné (arabe 9ᵉ, maths 9ᵉ 01–02)

Ce dossier rassemble ce qui vivait dans le scratchpad de la session « corriger 9eme cours programme »
(fermée le 2026-10-12 à la fusion des sessions) : sans lui, la reprise devrait tout relire. Les
mandats citent des chemins `/tmp/claude-0/…/scratchpad/ar9/…` : lire `FableEtudes/_campagne-9eme-au-patron/arabe-9eme/…`.

Le pilotage (état, file d'attente, règles anti-doublon) est dans [`../PILOTAGE.md`](../PILOTAGE.md).

## `arabe-9eme/`

| Dossier | Contenu | Correspondance des anciens chemins |
| --- | --- | --- |
| `lecture-101908/` | Une note par leçon du manuel de grammaire révisé (`L<page>.md` : خلاصة verbatim, مدخل, تمارين, bornes, coquilles), `L001-garde-et-fahras.md`, et les quatre tableaux d'écart initiaux `ecart-1..4.md` | `scratchpad/ar9/lecture/` |
| `lecture-101909/` | Manuel de textes « أنوار » : `plan.md`, `appareil.md`, `ecart-n.md` (dont les 11 sujets nationaux) | `scratchpad/ar9/lecture-n/` |
| `mandats/` | Mandat commun des rédacteurs `b-common.md`, gabarit des chapitres neufs `b-new.md`, un brief par chapitre (`brief-N15..N19`, `brief-B02..B12`), mandats de lecture (`brief-lecture.md`, `brief-nusus.md`, `tranche-1..4.md`), `todo-optionnels.md` | `scratchpad/ar9/` |
| `audits/` | Gabarit d'audit `audit-tpl.md` + `make.py` (`python3 make.py A4 <slugs…>` produit `audit-A4.md` à partir de `points-A4.md`), mandats `audit-A1..A4.md`, rapports `rapport-A1..A4.md` | `scratchpad/ar9/audit/` |
| `etiquettes/` | Mandats du vocabulaire d'erreurs `brief-vocab-A.md` / `brief-vocab-B.md`, **proposition de la partie A terminée** : `vocab-arabe9-A.json` (63 ids neufs) et `map-arabe9-A.md` (fiches, précédences, coursePitfalls proposés par chapitre) ; brouillons de l'agent dans `work-A/` | `scratchpad/ar9/tags/` |

## `maths-9eme/`

`brief-recentrage.md` : mandat du recentrage de `01-nombres-reels` et `02-racines-carrees` (fait le
2026-10-12, voir le rapport dans `../PILOTAGE.md` §3).
