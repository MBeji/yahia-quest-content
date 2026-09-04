# CLAUDE.md — yahia-quest-content (corpus privé)

> Repo **privé** né de l'étude 24 (scission moteur public / corpus privé). Il porte le
> **corpus pédagogique** (`content/`), les **skills de génération** (`.claude/skills/`) et les
> **études** (`FableEtudes/`). Le **moteur** (app, pipeline de build, docs techniques) vit
> dans le repo public [MBeji/yahia-quest-arena](https://github.com/MBeji/yahia-quest-arena) —
> son CLAUDE.md reste canonique pour tout ce qui est code, conventions et Definition of Done.

> ⭐ **Règle qui prime sur tout le reste — zéro intervention technique du propriétaire**
> (posée le 2026-08-23, valable sur les trois dépôts) : Mohamed donne le besoin, les priorités,
> les choix et les arbitrages ; la session exécute de bout en bout — commandes, code, base,
> tests, PR, garde-fous. Une **demande de permission est une validation manuelle** : si une
> action est autorisée, on la fait et on rend compte. Texte canonique, avec le test
> décision/exécution, l'échelle de traitement (faire → **supprimer le besoin** → harnais →
> rendre visible → remonter) et le tableau des murs :
> [`docs/agents/zero-intervention.md`](https://github.com/MBeji/yahia-quest-arena/blob/main/docs/agents/zero-intervention.md)
> du moteur. Corollaire vérifié ici : une ligne « en attente d'un humain » se **constate**
> avant d'être crue — sur les cinq de `STATUS.md`, deux étaient fausses.

- **Propriété intellectuelle** : tous droits réservés — le `LICENSE-CONTENT.md` du moteur
  s'applique intégralement à ce dépôt.
- **Authoring** : le flux de référence est `FableEtudes/METHODE-GENERATION-CONTENU.md` — ouvrir
  la session sur CE repo, ajouter le moteur public (`add_repo MBeji/yahia-quest-arena`),
  éditer `content/`, laisser `content-ci` valider.
- **Gates en local / session** — deux clones **côte à côte** : ce repo et `../engine` (le moteur).
  **Deux** liens sont nécessaires, pas un : les scripts résolvent `content/` **et**
  `.claude/skills/…/programmes-officiels/` relativement à la racine du **moteur**.

  ```bash
  # depuis la racine de CE repo
  rm -rf ../engine/content ../engine/.claude/skills
  ln -s "$PWD/content"        ../engine/content
  ln -s "$PWD/.claude/skills" ../engine/.claude/skills
  # puis depuis ../engine :
  npm ci && npm run content:check && npm run content:qa:strict &&
    npm run content:audit:strict && npm run programme:check
  ```

  Recette complète (jonctions Windows, contrôles, pièges) :
  `FableEtudes/METHODE-GENERATION-CONTENU.md` § Phase 0.1. Ce que le **poste** doit porter avant
  cette recette (logiciels, réglages Windows, domaines à autoriser sur le proxy — la liste à
  remettre à un admin PC) : `FableEtudes/POSTE-DE-TRAVAIL.md`.

- **Lancer une campagne** : `/campagne` (skill `.claude/skills/campagne/`) — état des lieux
  vérifié, question à l'humain sur le couple à traiter, puis déroulé de la chaîne. Il ne choisit
  jamais le couple : l'outillage donne les faits, l'arbitrage reste humain.

- **CI** : `.github/workflows/content-ci.yml` fait exactement cela (double checkout + les deux
  liens). Il porte aussi, **depuis l'étude 32 lot 2**, `harness:check --corpus` : les invariants
  du harness appliqués à CE dépôt (spec des 43 skills, Unicode invisible, budget de ce fichier,
  YAML strict, épinglage des Actions). C'est ce qui a permis de **supprimer `pin-check.yml`**,
  qui ré-écrivait en bash une règle du moteur — deux implémentations d'une même règle divergent,
  ce dépôt l'a vu trois fois sur le test « zéro job ». `content-audit.yml` (garde pédagogique)
  tourne mer. + sam. et exige le secret `CLAUDE_CODE_OAUTH_TOKEN` valide.
- **Ouverture des PR** : `.github/workflows/auto-pr.yml` (depuis #226) ouvre la PR de **toute**
  branche poussée, puis **dispatche ses checks**. Cette dispatch n'est pas un confort : la garde
  anti-boucle de GitHub empêche une PR ouverte par le `GITHUB_TOKEN` de faire tourner ses checks,
  donc `content-ci` ne démarrerait jamais sur elle — et `automerge` refusant, à raison, de
  merger un SHA sans aucun check run, la PR dormirait. D'où son `workflow_dispatch`.
  ⚠️ **Ce refus laissait une trace trompeuse, et elle a coûté trois fois.** GitHub enregistrait
  quand même un run `pull_request` — sorti à **ZÉRO job**, en `failure`. Il n'avait rien évalué,
  mais il ressemblait à un gate rouge sur `gh pr checks`, et à « un run existe » pour qui compte
  les runs. #280 y a lu un doublon qui s'annulait (il n'y a jamais eu de course) ; #291 en a tiré
  une garde qui a **gelé la chaîne entière** une journée (#297) ; #293 a compté 37 de ces fantômes
  comme des « gardes en échec ». Un seul test tranchait, toujours le même :
  `gh run view <id> --json jobs --jq '.jobs | length'` — **0 ⇒ ce run n'a rien évalué.**
  ✅ **La cause est supprimée depuis l'étude 32 (lot 1)** : `content-ci`, `roadmap-sync` et
  `automerge` déclarent `types:` SANS `opened`, l'événement qui faisait naître ces runs. Mesuré
  sur la PR #343 juste avant le correctif : trois runs `pull_request` en `failure`, zéro job
  chacun, pendant que les vrais tournaient en `workflow_dispatch`. Un invariant de
  `harness:check --corpus` fait désormais **échouer la CI** si un workflow d'ici réécoute
  `opened` — sans quoi la correction ne tiendrait qu'à la mémoire de la prochaine session.
  ⚠️ **Le test « zéro job » reste en place**, et ce n'est pas un oubli : dans `auto-pr.yml` il ne
  détecte pas un fantôme mais décide s'il faut dispatcher (sans lui, chaque branche repaie ses
  checks en double), et dans `guard-watch.yml` il coûte un appel d'API par run rouge pour que
  l'alarme dise vrai même si quelqu'un remet `opened` un jour. Retirer un filet parce que sa
  cause est absente, c'est très exactement le geste de #291.
  Sans ce ramassage, une session qui pousse puis s'arrête laisse sa branche sans PR :
  **8 branches `claude/*` étaient dans ce cas au 2026-08-24, jusqu'à cinq semaines.**
  ⚠️ Il exige le réglage `Settings > Actions > General > Workflow permissions >`
  « Allow GitHub Actions to create and approve pull requests » (activé le 2026-08-24). S'il
  manque, auto-pr **n'échoue pas** — il ouvre une issue `auto-pr-hs` et sort en 0, à dessein :
  `automerge` exigeant tous les checks verts, un rouge permanent ici bloquerait **toutes** les
  PR du dépôt.
- **Un rouge programmé se voit** : `.github/workflows/guard-watch.yml` (#226) relève toutes les
  6 h les runs rouges des 8 dernières heures et tient **une** issue `garde-rouge`, refermée dès
  qu'une fenêtre est verte. Il existe parce que quatre des cinq gardes d'ici savent ouvrir une
  issue pour ce qu'elles **constatent**, mais aucune n'a de filet pour son propre **plantage** —
  et parce que le moteur a laissé `report-triage.yml` mourir 26 jours en criant dans un onglet
  que personne n'ouvrait. ⚠️ Il filtre **côté serveur** (`--created` + `--status`) : filtrer une
  fenêtre en local après `gh run list --limit 100` rend « 0 rouge » d'un air vert, ces 100 runs
  ne couvrant qu'**1 h 13** sur un dépôt actif (mesuré sur le moteur, #230).
- **Chaîne de merge** : `.github/workflows/automerge.yml` merge (squash) toute PR dont **tous**
  les checks sont verts. Il raisonne par **état, pas par événement** : chaque déclenchement (fin
  d'un workflow de PR, événement `pull_request`, push sur `main`) rebalaye l'état complet de
  TOUTES les PR ouvertes, et le merge lui-même réessaie sur les échecs transitoires. La première
  version n'évaluait une PR qu'une fois, à la fin du dernier workflow de PR : #167 (marquée
  « ready » 54 s après avoir été vue en draft) et #162 (merge perdu sur `Base branch was
  modified`, une autre PR ayant merge entre-temps) sont restées vertes et ouvertes deux jours,
  sans que rien ne les relise jamais — corrigé par #182. En touchant à ce workflow, garder
  l'invariant : **l'événement dit quand regarder, jamais quoi regarder.** On s'y soustrait
  comme sur le moteur : PR en draft, branche `wip/`/`draft/`/`rescue/`, ou label
  `no-automerge`. ⚠️ Ce n'est
  pas un gate **opposable** : sur un compte Free, les rulesets ne sont pas disponibles sur un
  dépôt privé (`403 — Upgrade to GitHub Pro or make this repository public`), donc aucun check
  n'est *requis* et une PR rouge reste mergeable à la main. Le workflow automatise le bon
  geste, il n'interdit pas le mauvais — l'en-tête du fichier dit ce qu'il faudrait pour ça.
  ⚠️ **En touchant à ce workflow** : son bloc `permissions:` **remplace** le défaut du dépôt, il
  ne s'y ajoute pas — toute portée non listée tombe à `none`, pas à `read`. Un appel `gh` vers une
  surface non déclarée répond `403 Resource not accessible by integration`. C'est ce qui a cassé
  le premier usage réel de la chaîne (2026-07-26, #26) : `checks: read` manquait, et le workflow
  dont le métier est de lire les checks était le seul à ne pas pouvoir les lire. Toute nouvelle
  API appelée par le script exige donc sa portée dans le bloc. Aucun PAT n'est nécessaire ici —
  `GITHUB_TOKEN` suffit, et reste au moindre privilège.
- **Le contenu ne voyage pas en migrations** : `content:emit` → `sql/content/<subject>.sql`,
  appliqué en prod par `apply-content.yml` (`workflow_dispatch`, journalisé dans
  `content_releases`). Ne jamais committer de SQL ici, ni de migration dans le moteur.
  ⚠️ **Merger ne publie pas.** `apply-content.yml` est désarmé volontairement (lot 3a) : aucun
  merge, aucun push ne déclenche une application. Une PR de contenu mergée n'est donc **pas** en
  prod tant qu'un humain n'a pas dispatché — et une application lancée quelques minutes *avant*
  un merge fige l'ancienne version sans que rien ne le dise. Vécu le 2026-08-01 sur
  `math-bac-math` : application à 19:11 depuis `891c864`, PR #104 mergée à 19:27 en `67e3dd7`,
  et la prod a servi le contenu périmé deux jours. C'est pourquoi `content-drift.yml` existe :
  garde en **lecture seule** (elle n'applique rien) qui compare `content_releases` à `main`
  chaque jour à 06:40 UTC et à chaque push touchant `content/`, et tient **une** issue
  `content-drift` ouverte tant qu'un sujet est en retard — refermée d'elle-même une fois l'écart
  comblé. En fin de session de contenu : vérifier que cette issue est close, pas seulement que
  la PR est mergée.
