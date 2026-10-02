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

## Lots math 9ᵉ (au 2026-10-02 07h40 UTC)

- publiés et vérifiés (3 étapes apply-content + content-drift) : L01–L13 sauf L09 flip, L15, L18, L19 ; registre : 161 missions `publiee`.
  Reste à FLIPPER dans le registre (à la prochaine livraison) : L18 → `spec-pub-L18.json` (privé#628 publié). (L09 et L13 sont déjà flippés.)
- en cours au 2026-10-02 08h50 UTC : les trois auteurs ont rendu (L14 ch.09 NN36–41 62 Q ; L16 ch.18 NN29–35 73 Q ; L20 ch.03 NN27–31 29 Q dont 31 = ex-L18) ; les trois audits opus en aveugle tournent
  (L14 a0755e58afc4f234e, L16 a91e1972bd3cca321, L20 a40053c95bd3fbf21 ; prompts `prompt-audit-L*.md`, rapports `audit-L*.md` dans author/exam ; specs `auditspec/L*.json`).
  À l'audit rendu : arbitrage → SendMessage à l'auteur (L14 a703138b8a79595c8, L16 a86e1adf6dd7a4114, L20 a6b508df10501b321 : ils sont terminés, un envoi les reprend avec leur contexte) → re-vérification ciblée du MÊME auditeur → `deliver-lot.sh` → fusion → apply-content → drift.
  Livraison L20 : créer aussi l'entrée de registre C34#1 (fichier 31) — `gen-spec-lot.py` la prend du plan v6 (lot L20 = m119 + m123..m130) ; basculer L18 → publiee (`spec-pub-L18.json`).
- à lancer : L17 (ch.18 NN36–41, après L16), L21 (ch.09 NN47–48, après L14), L22 (ch.07 NN25, ch.12 NN22, ch.18 NN42 : après
  L16/L17) ; devoirs G2 (ch.04 NN29–33), I (ch.09 NN42–46, après L14/L21).
- suites : refaire le devoir 14 de ch.09, corriger les devoirs 11 et 12 de ch.09 ; cours ch.12 (faux : « repère orthonormé exigé
  pour le milieu » ; (O, I, J) jamais nommé ; enseigne vecteurs et translation) ; cours 04/07/08.
- moteur (arena) : correctif en cours `dir=ltr` sur les figures SVG (ancres text-anchor start/end inversées dans une page arabe ; branche t-fig-ltr, worktree wt-arena-fig, verify dans verify-fig.log) ; 3 correctifs d'affichage livrés le 10-02 (#1150 coefficients et lettres primées, #1149 dungeon RTL par la
  langue du contenu le 10-01, #1152 coche ✓ hors isolat).

## SVT 9ᵉ (matière `sciences-vie-terre`)

- Lecture faite : 6 sessions (2020, 2021, 2022, 2024, 2025, 2026) — transcriptions dans `en-cours/lecture-9eme/svt/officiel/`
  (à versionner sous `content/programmes-officiels/examens-nationaux/9eme-base/sciences-vie-terre/<année>.md` à la
  première livraison SVT), lignes dans `lines/`.
- SVT, lecture versionnée : privé#630 (six transcriptions `2020…2026-generale.md`, `lignes.tsv` 27 lignes, documents C01–C06 `lu/versionnee`, fiche). Outils SVT prêts : `deliver-lot-svt.sh <lot> <chapitre>:<NN,NN> …` (copie, ligne sources[], registre mergee via `MATIERE=sciences-vie-terre gen-spec-lot.py`, gates), `apply-tags.py` (champ `matiere` du pending : `sciences-vie-terre` → sujet `bio`, sans compétence), `add-source-line-svt.py`.
- Lot SVT-L01 (ch.02/05/07 NN7–8, six missions, 36 questions) : auteur FINI (af789b7b2beb04d47), audit opus en cours (ac850d2e96ca57dd5, prompt-audit-SVT-L01.md : l'auditeur peut lire les PDF officiels C03–C06 sous scratchpad/gisement/9eme-sciences-vie-terre/snapshots). À la livraison : `deliver-lot-svt.sh`, puis `apply-tags.py` avec `"matiere":"sciences-vie-terre"` dans le pending, CATALOGUE.md régénéré et committé ; publier avec apply-content `subjects=sciences-vie-terre`. Plan : 27 missions, 5 lots (`gisement/9eme-svt-plan/plan-examens-v1.json`)
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
