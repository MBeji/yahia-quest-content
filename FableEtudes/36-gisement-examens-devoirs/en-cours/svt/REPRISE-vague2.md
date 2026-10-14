# Reprise — SVT 9ᵉ vague 2 (pause du 2026-10-14, ~13 h 25 UTC)

- **Fait** : sessions C07–C24 lues et transcrites (`wip/gisement-svt-9eme-sessions`, registre : 23 `lu`) ;
  plan v2 (`svt/PLAN-v2.md`, `plan-examens-v2.json`) : 16 missions m028–m043 en 3 lots ;
  les 16 missions sont **écrites** (L11 : 01/02/03/07/13 ; L12 : 05/11/12 ; L13 : 08/09), gates verts
  par auteur, commit `818fdb66` sur `wip/gisement-svt-9eme-sessions`.
- **Interrompu** : les trois audits opus à l'aveugle (prompt `svt/prompt-svt-v2-auditeur.md`,
  rapports partiels éventuels `svt/audit-svt-L1N.md`). À relancer tels quels (lire le rapport partiel
  s'il existe), avec les points d'auteur listés dans les rapports des auteurs (notes
  `auteurs-notes/svt-L1N/NOTES.md`).
- **Ensuite** : corrections (auteurs) → re-vérif ciblée → livraison (branche fraîche depuis
  `origin/main` : missions, `chapter.json` 01 et 13, transcriptions C07–C24, registre m028–m043
  `mergee`, `lignes.tsv` à compléter des 72 lignes C07–C24, `fiche.md`, PILOTAGE) → merge →
  `apply-content` `subjects=sciences-vie-terre` → drift → bascule `publiee`.
- **Moteur** : `/home/user/eng-svtses` lit `/home/user/wt-svtses/content`.
