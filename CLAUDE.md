# CLAUDE.md — yahia-quest-content (corpus privé)

> Repo **privé** né de l'étude 24 : le **corpus pédagogique** (`content/`), les **skills de
> génération** (`.claude/skills/`) et les **études** (`FableEtudes/`). Le **moteur** (app,
> pipeline de build, docs techniques) vit dans
> [MBeji/yahia-quest-arena](https://github.com/MBeji/yahia-quest-arena) — son `AGENTS.md` reste
> canonique pour le code, les conventions et la Definition of Done. Ce fichier ne dit que ce
> qui est propre à CE dépôt.

⭐ **Zéro intervention technique du propriétaire** (règle des trois dépôts) : Mohamed donne le
besoin, les priorités et les arbitrages ; la session exécute de bout en bout. Demander une
permission est une validation manuelle. Une ligne « en attente d'un humain » se **constate**
avant d'être crue. Texte canonique :
[`docs/agents/zero-intervention.md`](https://github.com/MBeji/yahia-quest-arena/blob/main/docs/agents/zero-intervention.md).

- **Propriété intellectuelle** : tous droits réservés (`LICENSE-CONTENT.md` du moteur).
- **Authoring** : méthode de référence `FableEtudes/METHODE-GENERATION-CONTENU.md`. Ouvrir la
  session ici, `add_repo MBeji/yahia-quest-arena`, éditer `content/`, laisser `content-ci`
  valider. Campagne : `/campagne` — il donne les faits, **l'humain choisit le couple**.
- **Ne jamais committer de SQL ici, ni de migration de contenu dans le moteur** :
  `content:emit` → `sql/content/<subject>.sql`, appliqué par `apply-content.yml`.

## Gates en local — les SEPT étages de `content-ci`

Deux clones côte à côte : ce repo et `../engine` (le moteur), reliés par UN lien.

```bash
# depuis la racine de CE repo
rm -rf ../engine/content && ln -s "$PWD/content" ../engine/content
# puis depuis ../engine, dans l'ordre de la CI :
npm ci && npm run content:check && npm run content:catalogue &&
  npm run content:qa:strict && npm run content:figures:check &&
  npm run content:audit:strict && npm run programme:check &&
  npm run harness:check -- --corpus
```

⚠️ `content:catalogue` **régénère `content/CATALOGUE.md`**, que la CI compare par
`git diff --exit-code` : tout chapitre neuf le périme — **le committer**. Détails (Windows,
pièges) : `FableEtudes/METHODE-GENERATION-CONTENU.md` § Phase 0.1 ; poste :
`FableEtudes/POSTE-DE-TRAVAIL.md`.

⚠️ **TLS en session** : le CNP sert son certificat feuille seul (`curl` sort en 60).
`cat ../engine/scripts/cloud/ca-chain/*.pem /root/.ccr/ca-bundle.crt > /tmp/cnp-ca.pem`, puis
`CURL_CA_BUNDLE` / `NODE_EXTRA_CA_CERTS` dessus — le hook du moteur ne tourne pas ici. Jamais
`-k` ni `NODE_TLS_REJECT_UNAUTHORIZED=0`.

## Chaîne PR → merge → prod

Chaque workflow porte son historique et ses pièges dans son en-tête — le lire avant d'y toucher.

- **`auto-pr.yml`** ouvre la PR de toute branche poussée puis **dispatche ses checks** (une PR
  ouverte par `GITHUB_TOKEN` ne lance pas les siens). Exige le réglage « Allow GitHub Actions
  to create and approve pull requests » ; s'il manque, il ouvre une issue `auto-pr-hs` et sort
  en 0.
- **`automerge.yml`** merge (squash) toute PR dont **tous** les checks sont verts. Il raisonne
  par **état, pas par événement** : l'événement dit quand regarder, jamais quoi regarder. On
  s'y soustrait par PR draft, branche `wip/`/`draft/`/`rescue/` ou label `no-automerge`. Pas un
  gate opposable (pas de ruleset sur un dépôt privé Free). Son bloc `permissions:` **remplace**
  le défaut : toute nouvelle API appelée exige sa portée.
- **Aucun workflow n'écoute `pull_request: opened`** (il ferait naître des runs fantômes à zéro
  job) — `harness:check --corpus` le fait échouer. Un run rouge se juge avec
  `gh run view <id> --json jobs --jq '.jobs | length'` : **0 ⇒ il n'a rien évalué.**
- **`guard-watch.yml`** tient une issue `garde-rouge` sur les runs rouges des 8 dernières heures
  (filtre côté serveur, jamais après `--limit`).
- ⭐ **Un lot n'est pas fini au merge, il est fini en production.** Merger ne publie pas :
  `apply-content.yml` est désarmé à dessein. La session qui merge du contenu le **publie** dans
  la foulée (`workflow_dispatch`, `subjects` toujours renseigné — vide = tout le corpus, ~45 min)
  et vérifie « Appliquer », « Vérifier en base », « Journaliser ». Jamais d'application lancée
  avant le merge (elle fige l'ancienne version). `content-drift.yml` compare
  `content_releases` à `main` et tient une issue `content-drift` : en fin de session, vérifier
  qu'elle est close.
- `content-audit.yml` (mer. + sam.) exige le secret `CLAUDE_CODE_OAUTH_TOKEN` valide.
