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

## Lots math 9ᵉ (au 2026-10-01 16 h UTC)

- publiés : L01–L08, L10 à L12, L15 (privé#622, publié et vérifié), L19 ; registre : 149 missions `publiee`.
- livré, en attente de fusion puis de publication : L13 (ch.09 NN30–35, privé#624) — après la fusion : apply-content math,
  vérifier les 3 étapes, content-drift, puis flip L13 → publiee (`spec-pub-L13.json` à écrire : ids du registre en `mergee`).
- en cours : L09 (ch.12 NN16–21 : tour de corrections après audit, auteur ac1b96c173174247c, puis re-vérification par
  l'auditeur a7a8a473446195cd5 ; étiquettes nouvelles à créer par moi : `math.vec.symetrie-regle-confondue`,
  `math.prop.pourcentage-base-erronee`) ; L18 (ch.20 NN22–26 : audit en cours, agent a90ba4d07602584aa ; la mission 27 est
  passée au ch.03 NN31, lot L20) ; L14 (ch.09 NN36–41, auteur a703138b8a79595c8).
- à lancer : L16/L17 (ch.18 NN29+), L20 (ch.03 NN27–31, dont le fichier 31 déjà écrit), L21 (ch.09 NN47–51), L22 (ch.07 NN25,
  ch.12 NN22, ch.18 NN42) ; devoirs G2 (ch.04 NN29–33), I (ch.09 NN42–46).
- suites : refaire le devoir 14 de ch.09, corriger les devoirs 11 et 12 de ch.09 ; cours ch.12 (faux : « repère orthonormé exigé
  pour le milieu » ; (O, I, J) jamais nommé ; enseigne vecteurs et translation) ; cours 04/07/08 ; moteur : équations « 3 − 2x = … »
  et lettres à apostrophe (« M' ») (tâche #53).

## SVT 9ᵉ (matière `sciences-vie-terre`)

- Lecture faite : 6 sessions (2020, 2021, 2022, 2024, 2025, 2026) — transcriptions dans `en-cours/lecture-9eme/svt/officiel/`
  (à versionner sous `content/programmes-officiels/examens-nationaux/9eme-base/sciences-vie-terre/<année>.md` à la
  première livraison SVT), lignes dans `lines/`.
- Lot S-L01 (ch.02/05/07 NN7–8) : auteur af789b7b2beb04d47 en écriture. Plan : 27 missions, 5 lots (`gisement/9eme-svt-plan/plan-examens-v1.json`, planificateur du moteur, 0 fautive) ;
  prompts `prompt-svt-L01..L05.md`, affectations `assign-svt-L01..L05.md`.
- Campagne « 9ᵉ au patron » (autre session, privé#569/#620, entrée de synchronisation de l'ETUDE.md §8) : SVT publiée — 14 chapitres
  du programme en 01–14 (les 7 anciens en 15–21, optionnels), famille d'étiquettes **`bio.*` (95 ids)** disponible : les distracteurs
  SVT s'étiquettent avec `bio.*` (nouvel id seulement s'il manque). Le plan SVT rejoué sur ces chapitres est inchangé (27 missions).
  **Arabe 9ᵉ : en réalignement (manuel 101908) — ne rien y placer** tant que la fusion n'est pas signalée dans §8. Français 9ᵉ :
  réaligné sur le manuel 121905, famille `fr.*` (102 ids). Maths : la campagne ne touche que les chapitres 01 et 02.
- Reste à lire : C07–C24 (2019 à 2001, vérifier d'abord « programme en vigueur »), 6 devoirs (D01–D06, lots S1–S5).

## Arabe, français, anglais 9ᵉ

- Arabe : EN RÉALIGNEMENT, ne rien placer. Français et anglais : lecture des sessions non commencée (listes `docs.json`, `machine-list.tsv`, contexte lecteur dans `lecture-9eme/<matière>/`) ; les registres des couples sont sur `main` (échantillons fixés, privé#574).

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
