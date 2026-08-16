# CLAUDE.md — yahia-quest-content (corpus privé)

> Repo **privé** né de l'étude 24 (scission moteur public / corpus privé). Il porte le
> **corpus pédagogique** (`content/`), les **skills de génération** (`.claude/skills/`) et les
> **études** (`FableEtudes/`). Le **moteur** (app, pipeline de build, docs techniques) vit
> dans le repo public [MBeji/yahia-quest-arena](https://github.com/MBeji/yahia-quest-arena) —
> son CLAUDE.md reste canonique pour tout ce qui est code, conventions et Definition of Done.

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
  `FableEtudes/METHODE-GENERATION-CONTENU.md` § Phase 0.1.

- **Lancer une campagne** : `/campagne` (skill `.claude/skills/campagne/`) — état des lieux
  vérifié, question à l'humain sur le couple à traiter, puis déroulé de la chaîne. Il ne choisit
  jamais le couple : l'outillage donne les faits, l'arbitrage reste humain.

- **CI** : `.github/workflows/content-ci.yml` fait exactement cela (double checkout + les deux
  liens). `content-audit.yml` (garde pédagogique) tourne mer. + sam. et exige le secret
  `CLAUDE_CODE_OAUTH_TOKEN` valide.
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
