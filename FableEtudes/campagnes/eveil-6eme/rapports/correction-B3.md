# Correction B3 — 04-nutrition · 05-milieu-chaines-alimentaires · 06-reproduction-florale

Audit `audits/audit-B3.md` : tous les défauts appliqués (critiques : 0).

## Défaut par défaut
- **M-1 à M-5, M-16** (04) : appliqués tels quels (boss Q4 ; révision Q4, Q8, Q6-d (m-14) ; défi Q1, Q4, Q8). Clé = jamais la plus longue.
- **M-6, M-7, M-8 (Q1, Q2, Q4, Q6, Q7), M-9, M-10, M-11, M-17, M-19** (05) : appliqués. Adaptation unique : boss Q6, explication « السمكة تتغذّى على الطحالب وهي منتجة » (au lieu de « على النبات », les algues n'étant pas des plantes au sens strict). Quiz Q3 : reformulé en phrases (« يتغذّى الإنسان على الدجاجة… ») pour sortir de la paire proche avec boss Q3 que le remplacement de l'auditeur créait (Jaccard 0,56).
- **M-12, M-18b, m-4, m-5** (06) : appliqués (boss Q4, Q6, Q8, Q2-d, Q5 → tomate 40 graines, options 1/4/40/80 ; défi Q3, tag retiré sur Q6-b).
- **M-13** : 4 endroits corrigés (cours, résumé — texte réel « فهو الحقنة الواقية », quiz Q6, révision Q8).
- **M-14** : boss 04 → `items: ["تقييم 2 · 1-ب"]`. **M-15** : champ `manuel` retiré de 06/03-revision.
- **M-18a** : tag retiré (04 boss Q8-a). **m-1** : tag retiré (04 quiz Q2-d). **m-2, m-3** : `acceptedAnswers` ajoutés (04/05 Q7 ; 06/01 Q9). **m-9, m-10, m-11, m-14** appliqués. **m-13** : « البتلة » en #9d174d.
- **m-6, m-7** : gardés (l'auditeur laisse le choix). **m-8** : voir ids proposés. **m-12** (9 notions par chapitre) : décision de programme, renvoyée à l'humain, rien fusionné ni scindé.

## Ajout du pilote (légendes SVG)
Rendu Chromium 360 px en contexte `dir=rtl` : `text-anchor="start"` partait vers la gauche et « end » vers la droite. Corrigé : 06 fleur (4 légendes de droite → `end`, 4 de gauche → `start`) ; 04 « الماء » → `end`. Les autres légendes (`middle`, cycle 06 « تأبير وإخصاب » `end`, chaînes 05) vérifiées lisibles et sans recouvrement.

## Ids proposés (registre non touché)
`eveil.eco.maillon-retire-sans-effet` (05 § حلقة تغيب) · `eveil.nutri.equilibre-sans-salubrite` (04 § سلامة الغذاء) · `eveil.nutri.groupes-confondus-avec-repas` (04 § الوجبة المتوازنة) · (06 § الثمرة الكاذبة : sans libellé existant, id à créer par le pilote).

## Gates
`content:check` ✓ · `content:qa` ✓ · `content:figures:check` ✓ · `content:tranche … --fresh --strict-longest --strict-lessons` ✓ (0/37 clé la plus longue, 0 paire proche, 0 recul de patron) · prettier `--write` puis `--check` ✓ sur les fichiers des 3 chapitres.
