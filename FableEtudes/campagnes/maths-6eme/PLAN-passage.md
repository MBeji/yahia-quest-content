# Maths 6ᵉ — passage unique (mise à niveau des 24 chapitres, 2 chapitres neufs, gisement)

> Ouvert le 2026-10-19 après le LOT A (#734, fiche `validee-r7`). Branche `wip/maths-6eme-un-passage`
> (worktree `wt-m6`). Les 24 chapitres sont servis en production (parcours `concours-6eme`) : on les
> **met à niveau** depuis la fiche profonde, on ne les réécrit pas ; ni slug ni `displayOrder`
> existant ne change (le chapterId dérive du slug, les étoiles acquises en dépendent).

## 1. Ce que le passage corrige ou ajoute

1. **Écarts fiche ↔ chapitre servi** : chaque notion de la fiche (leçons rattachées au chapitre,
   §2, §2 octies–terdecies, bornes §3.2) enseignée et exercée ; rien de ⛔ ; les **errata** (§6.1)
   — aucune donnée fautive reprise ; les **reprises** du manuel 102609 et des épreuves officielles
   du guide déclarées (`manuel` sur l'exercice quand les données sont identiques).
2. **Arbitrages M1–M4** (PLAN.md § 3) : M1 كسر × كسر au ch. 13 ; M2 couronne au ch. 21 ; M3 180°
   jamais demandée ; M4 deux chapitres neufs — `25-perimetre-figure-composee` (leçon 24,
   ص 67–69) et `26-diagrammes-batons` (critère مع 1 du T2, p.182), écrits au patron.
3. **Gisement** (étude 36) : 17 sujets du concours de maths (2008–2026 ; 2011, 2014 introuvables,
   `http://6web.edunet.tn/<année>/math.pdf`, 2 p. chacun) repris et cités ; devoirs vague 1 en salle
   blanche.

## 2. Lots

| Lot | Qui | Quoi |
| --- | --- | --- |
| D0 | sonnet | registre du gisement `sources-externes/web-6eme-base-math/` : 17 sujets (sha256), vague 1 de 9 devoirs |
| B1 | sonnet | mise à niveau `01`–`06` |
| B2 | sonnet | mise à niveau `07`–`12` |
| B3 | sonnet | mise à niveau `13`, `14`, `15`, `22`, `24` + neuf `26-diagrammes-batons` |
| B4 | sonnet | mise à niveau `16`–`19` |
| B5 | sonnet | mise à niveau `20`, `21`, `23` + neuf `25-perimetre-figure-composee` |
| D1–D2 | sonnet | lecture des sujets et devoirs, plan des missions |
| C | sonnet | missions d'examen et de devoirs |
| Audit | opus | par lot, à l'aveugle |
| E | pilote | gates, livraison, publication `math-6eme`, drift, registre `publiee`, PILOTAGE |
