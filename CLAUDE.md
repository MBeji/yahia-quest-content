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
  les checks sont verts, dès la fin du dernier workflow de PR. On s'y soustrait comme sur le
  moteur : PR en draft, branche `wip/`/`draft/`/`rescue/`, ou label `no-automerge`. ⚠️ Ce n'est
  pas un gate **opposable** : sur un compte Free, les rulesets ne sont pas disponibles sur un
  dépôt privé (`403 — Upgrade to GitHub Pro or make this repository public`), donc aucun check
  n'est *requis* et une PR rouge reste mergeable à la main. Le workflow automatise le bon
  geste, il n'interdit pas le mauvais — l'en-tête du fichier dit ce qu'il faudrait pour ça.
- **Le contenu ne voyage pas en migrations** : `content:emit` → `sql/content/<subject>.sql`,
  appliqué en prod par `apply-content.yml` (`workflow_dispatch`, journalisé dans
  `content_releases`). Ne jamais committer de SQL ici, ni de migration dans le moteur.
