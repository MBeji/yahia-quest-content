# Correction B1 — 09-oeil-vision · 12-dhaw · 01-air

Tous les défauts de `audits/audit-B1.md` sont appliqués avec le texte de l'auditeur, sauf adaptations ci-dessous. Aucun défaut refusé.

## 09-oeil-vision
- 03-revision q6 (prompt, explication), q8 (acceptedAnswers +5) : appliqués.
- 05-entrainement q2 (scène de la piscine, étiquette sur c) : appliqué.
- 04-defi q5 (prompt, explication), q8 (explication, acceptedAnswers +6), q2 d : appliqués, étiquette retirée.
- 02-boss q3 c : étiquette retirée.
- chapter.json : « والخلط المائي » ajouté.

## 12-dhaw
- quiz q5, 01-pratique q4 / q8, 02-boss q2 / q4 / q6 : remplacés. Items `manuel` retirés (pratique : pages 18 ; boss : pages 19).
- cours : exemple de classification réécrit (4 lignes) ; phrase sur la Lune ajoutée dans la propriété de 🌫️ ; résumé puce 3 complété.
- 05-entrainement q7 (opticien, c muette), 03-revision q8 (acceptedAnswers +4) : appliqués.

## 01-air
- E-7a complet :
  - section de cours « ☠️ » insérée avant le 🏆, et 🏆 complété ;
  - 8ᵉ puce du résumé ;
  - chapter.json : description, source guide p.73, `coursePitfalls` + `eveil.air.co-et-co2-confondus` (id déjà au registre, non touché) ;
  - quiz q7 et 05 q8 ajoutées ; 05 q4 : explication retouchée.
- 01-pratique q2 : prompt, explication ; item « ص 34 » retiré.
- 02-boss q2 (reprise 6 ب), q4, q6 : remplacés ; item « ص 55 · 6 ب » retiré.
- 03-revision q3 et q2 a : remplacés.
- 04-defi q6 : b et c muettes ; `manuel` « أجرّب 4 (5) ».
- Mineurs « cours § 🌍 » (plante en boîte fermée) et « 03-revision q7 » : acceptés tels quels (l'auditeur ne demande aucune action).

## Fiche `eveil.md`
Quatre endroits corrigés (§ 2 و2, § 6.1 point 12, § 4 bis point 1, § 7.20) avec le texte exact de l'audit. `programme:check` ✓ ; prettier ✓.

## Points à signaler
- 01-pratique q2 (nouveau prompt : manfakh avec fuite bouchée) : même objet que l'ancrage du cours (pompe de roue), mais scène différente (fuite bouchée). Texte de l'auditeur gardé.
- 12-dhaw 01-pratique q5 : l'option « البلّور المطروق » reste proche de la ligne 3 du nouvel exemple (« بلّور باب الحمّام المطروق »), ce que prescrit l'audit.

## Ids proposés
Aucun nouvel id. Les ids de l'audit § 2 restent muets, sauf `eveil.air.co-et-co2-confondus` (existant, utilisé).

## Gates
- `content:check` ✓, `content:qa` ✓ (0 clé suspecte), `content:figures:check` ✓.
- `content:tranche --fresh --strict-longest --strict-lessons` ✓ : clé la plus longue 0/34, paires proches 0, patron 0 en recul. Positions de clé : a 12 · b 10 · c 8 · d 4, un avertissement non bloquant.
- prettier `--check` ✓ (3 chapitres + fiche).
- Rendu Chromium 360 px de `01-air` et `12-dhaw` (cours + résumé) : largeur de page 360, aucun débordement, tableaux à 360. Aucune figure SVG touchée ; une capture pleine page existe mais est illisible à l'échelle, la vérification est donc la mesure de largeur. Aucune vérification visuelle des légendes.
