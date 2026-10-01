# État de reprise du gisement 9ᵉ (point de sauvegarde — mis à jour le 2026-10-01 vers 10 h UTC)

> Ce fichier est écrit pour la session qui reprend sans relire l'historique. La source de vérité de l'état
> des missions reste `content/programmes-officiels/sources-externes/web-9eme-base-<matière>/gisement.json`
> (registre) sur `main` ; ce qui suit dit **où l'on en est des lots** et **comment on avance**.

## Le geste d'un lot d'examen (math, validé sur dix lots)

1. `gen-exam-assign.py` (math) ou `gen-exam-assign-subj.py` (autres matières) → `assign-<lot>.md` ;
   prompt d'auteur (`prompt-L*.md`, `prompt-svt-L*.md` via `gen-prompt-svt.py`) ; **un auteur par chapitre à la fois**,
   plages de NN explicites, ≤ 4 agents en parallèle ; auteurs/lecteurs sonnet, auditeurs opus.
2. `lot-lint.mjs` sur les fichiers de l'auteur → audit en aveugle (prompt-audit-*.md, consigne `gisement-auditeur.md`)
   → l'auteur applique → **re-vérification ciblée par le même auditeur** (elle trouve toujours du neuf, surtout dans
   les textes de remplacement fournis par l'audit) → livraison.
3. Livraison : `deliver-lot.sh <lot> <chapitre> <NN…>` (worktree frais d'`origin/main`, copie, ligne `sources[]`,
   registre `mergee`, gates), `apply-tags.py` + `mk-pending.py` pour les étiquettes, `registre-set.py` pour
   passer les missions précédentes à `publiee` (specs `spec-pub-*.json`), CATALOGUE.md régénéré **et committé**,
   dernier commit descriptif (le titre du squash = dernier commit), branche `claude/upbeat-knuth-hot71t`,
   une seule PR privée ouverte à la fois.
4. Après le merge : `apply-content.yml` en `workflow_dispatch` `{"subjects":"<matière>","dry_run":"false"}` ;
   vérifier « Appliquer le contenu », « Vérifier que le contenu est bien en base », « Journaliser la release » ;
   puis `content-drift.yml` ; l'issue `content-drift` doit être close.

## Lots math 9ᵉ (au 2026-10-01 10 h UTC)

- publiés : L01–L08, L10 (flip `publiee` à poser à la prochaine livraison : `spec-pub-L10.json`), L11, L12, L19.
- en cours : L13 (ch.09 NN30–35, en audit), L15 (ch.18 NN22–28, en audit), L09 (ch.12 NN16–21, en écriture),
  L18 (ch.20 NN22–27, en écriture).
- à lancer : L14 (ch.09 NN36–41, après L13), L16/L17 (ch.18 NN après L15), L20 (ch.03 NN27–30), L21 (ch.09 NN47–51),
  L22 (ch.07 NN25, ch.12 NN22, ch.18 NN42) ; devoirs G2 (ch.04 NN29–33), I (ch.09 NN42–46).
- suites : refaire le devoir 14 de ch.09 (point mobile, copie les données de l'examen 2015), corriger les devoirs 11 et 12
  de ch.09 ; cours 04/07/08/12 (voir les tâches de la session).

## SVT 9ᵉ (matière `sciences-vie-terre`)

- Lecture faite : 6 sessions (2020, 2021, 2022, 2024, 2025, 2026) — transcriptions dans `en-cours/lecture-9eme/svt/officiel/`
  (à versionner sous `content/programmes-officiels/examens-nationaux/9eme-base/sciences-vie-terre/<année>.md` à la
  première livraison SVT), lignes dans `lines/`.
- Plan : 27 missions, 5 lots (`gisement/9eme-svt-plan/plan-examens-v1.json`, planificateur du moteur, 0 fautive) ;
  prompts `prompt-svt-L01..L05.md`, affectations `assign-svt-L01..L05.md`.
- Pas de famille d'étiquettes SVT dans `misconceptions.json` : distracteurs muets, erreurs décrites au rapport.
- Reste à lire : C07–C24 (2019 à 2001, vérifier d'abord « programme en vigueur »), 6 devoirs (D01–D06, lots S1–S5).

## Arabe, français, anglais 9ᵉ

- Lecture non commencée (listes `docs.json`, `machine-list.tsv`, contexte lecteur dans `lecture-9eme/<matière>/`).

## 6ᵉ

- Rien de lancé ; sondes dans `gisement/6eme-probe` (scratchpad).

## Limites de session (constat du 2026-10-01)

- La limite est « five_hour », par quota consommé et non par durée : quatre agents (deux auditeurs opus + deux auteurs sonnet)
  l'ont épuisée en ~1 h (09:22 → 10:30 UTC), réouverture à 14:20 UTC. La fenêtre précédente avait tenu 01:10 → 05:20.
- À la coupure, tous les agents meurent avec « You've hit your session limit · resets <heure> » : les reprendre par
  `SendMessage` (leur contexte est conservé) APRÈS l'heure de réouverture, en leur demandant d'écrire leurs résultats
  dans les fichiers de rapport au fil de l'eau (un auditeur coupé avant d'avoir écrit perd tout son travail apparent).
- Garder le contexte principal léger : pas de sondage, un tour par événement.

## Pièges à ne pas oublier

- Le pre-push husky ne tourne pas dans un worktree sans `.husky/_` : lancer soi-même lint + typecheck + tests avant de pousser.
- Ne jamais committer ni pousser l'arbre partagé `/home/user/yahia-quest-content` (périmé) : lire/copier seulement.
- Aucun `supabase db push/reset`, aucun dispatch de `db-migrate-prod.yml` ni de `release.yml`.
