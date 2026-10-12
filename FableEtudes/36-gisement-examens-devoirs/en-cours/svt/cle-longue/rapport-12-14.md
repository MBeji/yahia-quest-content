# Rapport — fuite « clé la plus longue », SVT 9e, chapitres 12 à 14

## 12-takawwun-al-janin — 58 % (37/64) -> 0 % (0/64)

Parade 1 (clé raccourcie à la réponse nue ou à l'essentiel, justification laissée à l'explication) sur : quiz 2, 6, 7, 8, 10 ; 01-tamrin 1, 4, 6 ; 02-tamrin 2 ; 04-defi 3 ; 05-tadrib 1, 2, 3, 4, 5 ; 06 1 à 6.
Parade 2 (distracteurs étoffés, même forme, faux, même erreur plausible) sur : quiz 5 ; 01-tamrin 2, 5 ; 02-tamrin 3, 4, 6 ; 03-boss 1, 2, 3, 5 ; 04-defi 1, 2, 4, 5, 6 ; 05-tadrib 6.
Détails : voir `git diff` du corpus (`wip/svt-9eme-cle-longue`).
- quiz 8 : explication complétée (le stock de fer non reconstitué entre deux grossesses quittait la clé).
- 03-boss 2 : explication citait « الأخيرة » (dernière fonction) -> remplacé par le texte.

## 13-tandhim-al-wiladat — 80 % (37/46) -> 0 % (0/46)

Parade 1 (clé raccourcie, même vérité à la lettre) : quiz 6, 7, 9, 10 ; 01-tamrin 5 ; 02-tamrin 1, 2, 5 ; 03-boss 2, 4 ; 04-defi 1, 2, 4, 5 ; 05-tadrib 1, 2 ; 06-defi-concours 2, 3, 5.
Parade 2 (distracteurs étoffés, même forme, faux) : tous les autres (quiz 5 ; 01-tamrin 1, 2, 6 ; 02-tamrin 3 ; 03-boss 3, 5, 6 ; 04-defi 3, 6 ; 05-tadrib 3 à 6 ; 06 1, 4, 6).
- 02-tamrin 4 (nombre) : clé « نحو 99 % » (au lieu de « أكثر من 99 % ») et distracteurs laissés en « نحو N % » : évite de créer un indice de forme.
- 03-boss 6 : la clé garde les trois effets (le prompt dit « الثّلاثيّ »).
- 05-tadrib 4 : distracteur « سبعة أيّام » (non enseigné) remplacé par « امتناع » (terme du cours).
- Laissé : paire proche quiz 3 ↔ 03-boss 1 (jour d'ovulation, cycle de 26 j : exercice parallèle quasi identique), préexistant, à arbitrer.

## 14-al-amrad-al-manqula — 87 % (40/46) -> 0 % (0/46)

Parade 1 : quiz 2, 4, 6, 7, 8, 10 ; 01-tamrin 4, 5, 6 ; 02-tamrin 3 ; 03-boss 2, 3, 4 ; 04-defi 1, 3, 4, 5, 6 ; 05-tadrib 3, 4, 5, 6 ; 06 1 à 6.
Parade 2 : quiz 1, 9 ; 01-tamrin 2, 3 ; 02-tamrin 2, 4, 5, 6 ; 03-boss 1, 5, 6 ; 05-tadrib 2.
- Indice de forme préexistant supprimé : 04-defi 5 (seule clé en « بسبب » face à trois « لأنّ ») ; 04-defi 4 (seule clé en « تحت تأثير » face à trois « ب… »).
- 04-defi 1 : distracteur contradictoire (« لا » + raison fausse) remplacé par « نعم » + même raison fausse.
- Paire proche quiz 4 ↔ 03-boss 2 créée par les clés raccourcies identiques : levée (quiz 4 « تقدّم إلى طوره الثّاني »). Reste : quiz 6 ↔ 01-tamrin 4 (cellules ت4, 0,68 -> 0,52), préexistant.

## Défauts préexistants non corrigés (hors mandat)
- Positions de clé déséquilibrées (ch12 a22·b26·c11·d5 ; ch13 a20·b20·c4·d2 ; ch14 a24·b14·c6·d2) : `correctOption` interdit de bouger, cosmétique car mélange à l'affichage.
- Les chiffres/ordinaux d'« الأولى/الثّانية » restants dans les explications désignent des étapes ou phases, jamais des options.

## Vérifications finales
`npx prettier --check` des 21 fichiers : vert ; `content:check` : 120 matières, 0 erreur ; `content:qa:strict --subject sciences-vie-terre` : 0 erreur, 7 avertissements (aucun dans 12-14) ; `content:tranche` : 0/64, 0/46, 0/46.
