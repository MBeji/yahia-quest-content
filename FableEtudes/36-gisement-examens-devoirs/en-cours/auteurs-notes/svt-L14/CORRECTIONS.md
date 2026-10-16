# Corrections L14 (audit-svt-L14.md) — appliquées

Sources de génération : /tmp/claude-0/svt-v2/L14/gen/m1..m6.py (fichiers régénérés). Aucun chapter.json touché.

- M1, M2, M3 (03/13 Q1, Q3, Q7) : appliqués tels quels (clé de Q7 : « السّنجابيّة في النّخاع تحيط بالبيضاء », sans « الشّوكيّ » pour que la clé ne soit pas la plus longue : 52 contre 61/51/52).
- M4, M5, M6, M7 (02/10 Q2, Q4, Q5, Q6) : appliqués ; minors 1 et 2 aussi.
- M8 (07/10 Q3), minors 3 et 4 (Q4 reformulée ; Q5 passée à la minute 140, 2,0 g/L, définition artère/veine par la direction) ; étiquette `bio.circ.artere-sang-oxygene` sur Q5 a et b.
- M9, M10, M11 (11/11 Q1, Q5 → 31 jours/jour 17, Q6 → jour 15/29 jours, Q7 → jour de la courbe) ; figure : étiquette « الحيض » de gauche déplacée (x=48, start), rendue en Chromium 232 px.
- M12 (13/08 Q6 phrase retirée, Q8 réécrit) ; minor 11 ; étiquette `regles-supprimees-par-la-pilule` posée sur Q6 b et Q7 b (pas sur le multi).
- Minors 6–9 (09/13) appliqués. Minor 8 : e et d de Q5 sont dans un multi, donc sans étiquette (impossible).
- Registre : créé `bio.contra.regles-supprimees-par-la-pilule` ; libellé de `bio.circ.artere-sang-oxygene` élargi (grep : les 9 options qui la portent parlent d'oxygène/direction, restent exactes).
- `bio.cycle.compte-depuis-l-ovulation` non créée ; 11/11 Q6 d (14) reste muette.

Écarts : 13/08 Q5 clé la plus courte de 1 caractère (51 contre 52–53) ; 11/11 Q4/Q5/Q6 et 07/10 Q4 : options numériques, longueurs égales ; positions de clé 11/11 : b ×3 (cosmétique, ordre mélangé à l'affichage). 07/10 paires proches Q1/Q3/Q4 (0,47–0,53) : même document, autres lectures.
Contrôles : content:check ✓ (1061 étiquettes), qa:strict 0 erreur, tranche (clé la plus longue 0/393), gisement:controle ✓.
