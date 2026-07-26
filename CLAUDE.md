# CLAUDE.md — yahia-quest-content (corpus privé)

> Repo **privé** né de l'étude 24 (scission moteur public / corpus privé). Il porte le
> **corpus pédagogique** (`content/`), les **skills de génération** (`.claude/skills/`) et les
> **études** (`FableEtudes/`). Le **moteur** (app, pipeline de build, docs techniques) vit
> dans le repo public [MBeji/yahia-quest-arena](https://github.com/MBeji/yahia-quest-arena) —
> son CLAUDE.md reste canonique pour tout ce qui est code, conventions et Definition of Done.

- **Propriété intellectuelle** : tous droits réservés — le `LICENSE-CONTENT.md` du moteur
  s'applique intégralement à ce dépôt.
- **Authoring** : le flux `FableEtudes/METHODE-GENERATION-CONTENU.md` est inchangé — ouvrir
  la session sur CE repo, ajouter le moteur public (`add_repo MBeji/yahia-quest-arena`),
  éditer `content/`, laisser `content-ci` valider.
- **Gates en local / session** (deux clones côte à côte, ce repo et `engine/` = le moteur) :
  `rm -rf engine/content && ln -s "$PWD/content" engine/content`, puis depuis `engine/` :
  `npm ci`, `npm run content:check`, `npm run content:qa:strict`,
  `npm run content:audit:strict`.
- **CI** : `.github/workflows/content-ci.yml` fait exactement cela (double checkout +
  symlink). `content-audit.yml` (garde pédagogique hebdo) s'active quand le secret
  `CLAUDE_CODE_OAUTH_TOKEN` est configuré — recommandé au lot 4, quand ce repo devient
  l'unique source du contenu.
- **Chaîne de merge** : `.github/workflows/automerge.yml` merge (squash) toute PR dont **tous**
  les checks sont verts, dès la fin du dernier workflow de PR. On s'y soustrait comme sur le
  moteur : PR en draft, branche `wip/`/`draft/`/`rescue/`, ou label `no-automerge`. ⚠️ Ce n'est
  pas un gate **opposable** : sur un compte Free, les rulesets ne sont pas disponibles sur un
  dépôt privé (`403 — Upgrade to GitHub Pro or make this repository public`), donc aucun check
  n'est *requis* et une PR rouge reste mergeable à la main. Le workflow automatise le bon
  geste, il n'interdit pas le mauvais — l'en-tête du fichier dit ce qu'il faudrait pour ça.
- ⚠️ **Transition (étude 24, lots 2 → 4)** : tant que le retrait du corpus public n'est pas
  fait, le contenu s'édite **encore dans le repo public** ; ce repo est un miroir
  (importé de `yahia-quest-arena@ef43487`). Après le lot 4, il devient l'unique source et
  cette note est supprimée.
