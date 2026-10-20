# Correction — lot B4 (07-aimants-boussole · 11-effets-courant-electrique · 08-poids)

Tout appliqué tel que fourni par l'auditeur (textes de remplacement validés zod/mesures par lui, re-vérifiés ici par les gates) ; aucun défaut refusé.

## 07-aimants-boussole
- M07-1 quiz Q4, M07-2 01-pratique Q1, M07-3 02-boss Q6 (nord déplacé), M07-4 03-revision Q5, M07-5 04-defi Q3 : appliqués.
- M07-6 : étiquette `eveil.aim.est-ouest-inverses` inexistante : options concernées (quiz Q6 « ج ق », 03-revision Q8 « الرقم 6 », 02-boss Q6 « الرقم 3 ») laissées muettes ; `coursePitfalls` inchangé.
- Mineurs : 01-pratique Q8 (acceptedAnswers + dernière phrase de l'explication) appliqués ; autres mineurs (doublon 03-rev Q8/05 Q9, « أو التّوابل », lettre « ق » à confirmer, guillemets quiz Q6) : acceptés tels quels / non modifiés (choix défendables, sans effet sur les clés) ; lettre « ق » à confirmer en session concours.

## 11-effets-courant-electrique
- M11-1 / E-7b : section « 🔔 الجرس الكهربائيّ » (figure, exemple, verifie, retenir) insérée avant le `> 🏆`, `> 🏆` corrigé, puce de résumé, `description` complétée, 05-entrainement Q8 et Q9 ajoutées (9 questions). Figure revue au rendu Chromium `dir="rtl"`, 360 px : scrollWidth 360, étiquettes م/س/ر/ص lisibles, rien ne déborde.
- M11-2 : `::: verifie` 🫧 remplacé (tube gauche le plus petit) ; 02-boss Q4 « ، ولماذا؟ » ajouté ; `manuel` 02-boss : pages « 125, 138 » + item p.125 n°7.
- M11-3 04-defi Q4 (répulsion) ; M11-4 02-boss Q6 (noyaux retirés, مسامير) ; mineurs 02-boss Q7, 03-rev Q1, 05 Q7 et 01 Q8 (acceptedAnswers) : appliqués.
- M11-5 : `eveil.elec.lampe-seulement-avec-cellule` et `eveil.elec.deux-facteurs-a-la-fois` inexistants : options 04-defi Q7 (« خليّة مخفيّة… ») et 02-boss Q8 (« وشيعة بـ 10 لفّات وخليّة… ») laissées muettes ; `coursePitfalls` inchangé.

## 08-poids
- M08-1 : `direction="ltr"` sur les 13 `start` et 5 `end` du cours et sur les 5 `end` de 01-pratique Q6 ; rendu Chromium 360 px relu : étiquettes lisibles, plus de chevauchement.
- M08-2 `::: verifie` 🌋 (محفظة 20 N) ; M08-3 à M08-13 (01 Q5, 02 Q2/Q3/Q8, 03 Q2/Q5, 04 Q1/Q2/Q3/Q4/Q6) ; M08-14 (05 Q4/Q5/Q6) : appliqués. 02-boss Q8 : options/clé/explication seules changées (énoncé et figure intacts).
- Mineurs : 01 Q3 (قطرة), 01 Q8 (الشاقول), `manuel.items` 02-boss (+6-2, 6-3), tableau 🆚 (« مقدار ليس قوّة »), « الدّيناموتر » uniformisé (04-defi Q7) : appliqués.

## Ids d'étiquettes à créer (muets pour l'instant)
1. `eveil.aim.est-ouest-inverses` (piège « الشرق عن اليسار والغرب عن اليمين », ch. 07) : à poser sur quiz Q6 « ج ق », 03-revision Q8 « الرقم 6 », 02-boss Q6 « الرقم 3 », puis à déclarer dans `coursePitfalls`.
2. `eveil.elec.lampe-seulement-avec-cellule` (ch. 11 ; 04-defi Q7).
3. `eveil.elec.deux-facteurs-a-la-fois` (ch. 11 ; 02-boss Q8).

## Décisions « à l'humain »
Notation de l'Est « ق » (V5 ne fixe pas la lettre ; guide p.176 imprime « شـ »).

## Gates (depuis /home/user/eng-deliver)
`content:check` OK · `content:qa` (« no suspicious answer keys ») OK · `content:figures:check` OK · `content:tranche … --fresh --strict-longest --strict-lessons` OK (clé la plus longue 0/36, paires proches 0, patron 0 en recul) · prettier write puis check OK.
