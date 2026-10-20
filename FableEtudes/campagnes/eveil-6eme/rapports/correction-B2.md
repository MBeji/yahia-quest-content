# Correction B2 — 02-respiration, 03-sang-circulation, 10-microbes-defense

Source : `audits/audit-B2.md`. Tous les défauts sont appliqués tels que l'auditeur les donne, sauf les adaptations listées ci-dessous. Aucun refus.

## Appliqué (texte de l'auditeur)
- C-1 : 03 `02-boss` q7 réécrite (clé `c`, aucune étiquette).
- M-1 : 02 `cours.md`, 9 `text-anchor="start"` -> `end`.
- M-2 a-g : 02 `02-boss` q2, q3, q7 ; 03 `04-defi` q1, 03 `05-entrainement` q5 ; 10 `03-revision` q1, 10 `02-boss` q4.
- M-3 : 03 `01-pratique` q3 passe à 3 options (a, b, d) ; le schéma l'accepte (`content:check` vert).
- M-4 : 03 `05-entrainement` q3. M-5 : étiquettes retirées sur 03 `01-pratique` q7 (b, c, d).
- M-7 : sel de l'Aïd ajouté au cours 03.
- M-8, M-9, M-12 : 10 `04-defi` q4, 10 `03-revision` q8, 10 `01-pratique` q7.
- M-10, M-11 : 02 `04-defi` q5 et q1 (q1 passe en difficulté 2).
- m-1 : étiquettes supprimées (02 `02-boss` q6 d ; 10 `02-boss` q7 c ; 10 `03-revision` q9 a).
- m-2 : tri stable par difficulté de 02 `03-revision`, 03 `03-revision`, 03 `05-entrainement`, 10 `01-pratique`, 10 `05-entrainement`.
- m-3 (02 quiz q7, 02 `03-revision` q6 et q2, 10 `02-boss` q3), m-4, m-5, m-12, m-13 (cours et résumé 10).

## Adapté
- M-6 : registre non touché. Les options concernées restent muettes (02 quiz q7 a ; 02 `02-boss` q7 b ; 03 quiz q6 b ; 03 `02-boss` q7 b, option b « كريّة بيضاء صغيرة » ; 03 `01-pratique` q7 c). Les trois ids ne sont pas ajoutés aux `coursePitfalls` (ils n'existent pas encore au registre, la validation les refuserait).
- m-9 : l'intitulé proposé dépasse la limite de 40 caractères du schéma (`manuel.items`). Retenu : `الوحدة 3، جذاذة تنشيط 1، النشاط الأوّل` (38 caractères).
- m-2 : le tri stable déplace aussi les `ordering` d2 de 02 `03-revision` (q8) et de 03 `05-entrainement` (q7 matching, q8), qui suivaient des d3 ; l'ordre émis par le compilateur était déjà celui-là.

## Non appliqué (signalé par l'auditeur comme sans correction)
- m-6 (champ `manuel` à ajouter, traçabilité seulement), m-7, m-8, m-10 : l'auditeur les déclare admissibles ou « à signaler ». Non touchés.
- m-11 : étiquette du piège « الشّرايين » : non bloquant, rien à faire.
- La correction de la fiche (العقد اللّمفاويّة présentes au manuel p.72) est faite par le pilote.

## Ids proposés (à créer au registre par un responsable des étiquettes)
Libellés fr/en/ar exacts dans `audits/audit-B2.md` M-6.
- `eveil.resp.respiration-volontaire` -> 02 quiz q7 option a ; à ajouter aux `coursePitfalls` du ch. 02.
- `eveil.resp.monoxyde-sans-odeur-sans-danger` -> 02 `02-boss` q7 option b ; à ajouter aux `coursePitfalls` du ch. 02.
- `eveil.sang.plaquettes-prises-pour-globules-blancs` -> 03 quiz q6 option b, 03 `02-boss` q7 option b, 03 `01-pratique` q7 option c ; à ajouter aux `coursePitfalls` du ch. 03.

## Gates (depuis `/home/user/eng-deliver`)
- `content:check` OK (121 sujets).
- `content:qa -- --subject eveil-scientifique-6eme` OK.
- `content:figures:check` OK.
- `content:tranche` (3 chapitres, `--fresh --strict-longest --strict-lessons`) OK : clé strictement la plus longue 0/62, aucune paire proche, 0 gabarit, 0 cours en recul.
- `prettier --write` puis `--check` sur les trois dossiers : OK.
- Relecture des trois cours : aucun exemple ou `verifie` reposé par les questions neuves.
