# Poste de travail — ce qu'il faut faire installer (demande à l'admin PC)

> **À qui ça s'adresse** : l'administrateur du PC. La page se lit et s'envoie telle quelle — chaque
> ligne dit **pourquoi** l'outil est demandé et **ce qui casse sans lui**, pour qu'aucune demande
> n'ait l'air gratuite.
>
> **Contexte du poste** : Windows 11, travail en **Git Bash**, projet « Na9ra Nal3ab » (académie
> d'apprentissage pour le programme scolaire tunisien). Deux dépôts GitHub sont clonés côte à côte
> (le corpus privé et le moteur public) plus un utilitaire de transcription ; toutes les
> vérifications tournent en local avant d'être rejouées par la CI GitHub.
>
> **Ce qui a déjà coûté du temps, faute de droits** : `winget` bloqué par UAC le 2026-06-12 — la
> CLI GitHub a dû être installée en **zip portable** avec un PATH bricolé ; et `jq`, absent,
> renvoie du **vide silencieux** que les scripts de surveillance lisent comme « aucune PR, aucun
> check » (pièges documentés dans le moteur, `docs/agents/poste-windows.md`).

⚠️ Les identifiants `winget` ci-dessous sont ceux du dépôt public ; les confirmer d'un
`winget search <nom>` avant l'installation. Rien n'exige d'installer **pour** l'utilisateur : lui
donner le droit d'installer et de mettre à jour ces paquets suffit, et évite un ticket à chaque
montée de version.

---

## 1. Le strict nécessaire — 4 logiciels

Sans ces quatre-là, rien ne démarre.

| Logiciel                | Version              | `winget install`         | Pourquoi / ce qui casse sans lui                                                                                                                                                            |
| ----------------------- | -------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Node.js**             | **24.x** (LTS)       | `OpenJS.NodeJS.LTS`      | Fait tourner **toutes** les vérifications du projet (`content:check`, `content:qa:strict`, `content:audit:strict`, `programme:check`) et l'utilitaire de transcription. Le dépôt épingle 24. |
| **Git for Windows**     | dernière             | `Git.Git`                | Git **et Git Bash** — c'est le shell dont Claude Code se sert sous Windows. Sans lui, l'outil retombe sur PowerShell et une partie du flux ne marche plus pareil.                            |
| **Claude Code**         | dernière             | `Anthropic.ClaudeCode`   | L'outil de travail lui-même (assistant en ligne de commande). S'auto-met à jour en arrière-plan — voir le §5 réseau.                                                                        |
| **GitHub CLI (`gh`)**   | dernière             | `GitHub.cli`             | Ouvre les *pull requests*, lit l'état des vérifications, déclenche la publication du contenu. Aujourd'hui en zip portable faute de droits : à réinstaller proprement, avec un PATH machine.  |

Deux précisions qui évitent des heures perdues :

- **Node 24, et un seul Node.** Ne pas installer de gestionnaire de versions (fnm, nvm-windows) en
  parallèle — ou alors le figer sur 24. Le poste a déjà servi un **Node 22** masqué derrière un
  shim fnm alors que Node 24 était installé : la conséquence a été une erreur d'analyse
  incompréhensible, dans un fichier sans rapport, et un diagnostic refait de zéro (2026-08-26).
- **Git for Windows : cocher « Enable symbolic links »** pendant l'installation. Les deux dépôts
  se branchent l'un dans l'autre par lien ; sans cette option, git matérialise un lien en fichier
  texte de 9 octets et l'échec est **silencieux**.

## 2. Très utile — petit coût, gros bénéfice

| Logiciel                | `winget install`               | Pourquoi                                                                                                                                                          |
| ----------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **jq**                  | `jqlang.jq`                    | **Absent aujourd'hui.** Les scripts qui lisent du JSON rendent alors du vide *sans erreur* : la surveillance affirme « aucune PR », « aucun check », et c'est faux. |
| **Windows Terminal**    | `Microsoft.WindowsTerminal`    | Onglets, et surtout un rendu UTF-8 correct : le corpus est trilingue **français / anglais / arabe**, avec de l'écriture de droite à gauche.                        |
| **Visual Studio Code**  | `Microsoft.VisualStudioCode`   | Relire les modifications, les figures SVG et l'arabe avant publication. L'extension Claude Code s'y branche.                                                       |
| **PowerShell 7**        | `Microsoft.PowerShell`         | Les jonctions de dossiers et les scripts d'installation ; meilleur support UTF-8 que le PowerShell 5 livré avec Windows.                                          |

## 3. Seulement pour travailler sur l'application — pas pour le contenu

À ne demander que si le travail touche au moteur (le site) et pas seulement au contenu pédagogique.

| Logiciel                            | `winget install`               | Pourquoi                                                                                        |
| ----------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------- |
| **Supabase CLI**                    | `Supabase.CLI`                 | Migrations et types de la base de données.                                                       |
| **PostgreSQL 17** (client + serveur) | `PostgreSQL.PostgreSQL.17`     | Rejouer la suite de tests base **sans Docker** — c'est le chemin retenu par le projet.           |
| **Docker Desktop** *(à éviter)*      | `Docker.DockerDesktop`         | Uniquement si le chemin sans Docker ne suffit plus. Lourd, souvent refusé en entreprise : le projet s'en passe volontairement. |

## 4. Réglages Windows — aussi importants que les installations

Ce sont eux qui demandent des droits d'administrateur, plus que les logiciels.

1. **Mode développeur activé** — *Paramètres → Confidentialité et sécurité → Espace développeurs*.
   Permet les liens symboliques réels ; sans lui il faut passer par des jonctions PowerShell à
   chaque mise en place.
2. **Exclusions antivirus / EDR** sur les dossiers de travail :
   - le dossier du projet (les deux clones), en particulier tout `node_modules` ;
   - `%USERPROFILE%\.claude` ;
   - le cache npm (`%LOCALAPPDATA%\npm-cache`).
   Une installation de dépendances écrit **des dizaines de milliers de petits fichiers** ; leur
   indexation à chaud a déjà fait échouer des vérifications qui passaient seules cinq minutes plus
   tard.
3. **Ne pas bloquer `node.exe`, `claude.exe`, `git.exe`, `gh.exe`** dans les règles EDR /
   contrôle applicatif.
4. **Politique d'exécution PowerShell** : `RemoteSigned` pour l'utilisateur (installateurs et
   scripts de mise en place).
5. **Droits d'écriture** sur le dossier de travail **et** sur le répertoire global npm, sans
   élévation — l'installation de paquets globaux ne doit pas exiger d'être administrateur.
6. **Laisser passer les mises à jour** : Claude Code se met à jour tout seul en arrière-plan ;
   `winget upgrade` doit rester utilisable par l'utilisateur.

## 5. Réseau — domaines à autoriser sur le proxy / pare-feu

C'est le point qui bloque le plus souvent en entreprise, et le plus discret : sans ces domaines,
les logiciels s'installent mais ne fonctionnent pas.

**Pour Claude Code** (liste officielle, `code.claude.com/docs/en/network-config`) :

| Domaine                         | Sert à                                                    |
| ------------------------------- | ---------------------------------------------------------- |
| `api.anthropic.com`             | les requêtes vers le modèle — **indispensable**            |
| `claude.ai` · `claude.com` · `platform.claude.com` | connexion au compte (OAuth)             |
| `downloads.claude.ai`           | installation et mises à jour automatiques                  |
| `registry.npmjs.org`            | dépendances et extensions                                  |
| `raw.githubusercontent.com`     | notes de version                                           |
| `code.claude.com`               | consultation de la documentation                           |
| `mcp-proxy.anthropic.com`       | connecteurs (Gmail, GitHub…) — si utilisés                 |
| `*.frame.claudeusercontent.com` | affichage des pages générées (*artifacts*) — si utilisées  |
| `storage.googleapis.com`        | métadonnées des extensions                                 |

**Pour le projet** :

| Domaine                                                                     | Sert à                                                        |
| --------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `github.com` · `api.github.com` · `codeload.github.com` · `objects.githubusercontent.com` | clones, *pull requests*, état des vérifications |
| `registry.npmjs.org`                                                        | installation des dépendances                                   |
| `www.cnp.com.tn` · `edunet.tn`                                              | manuels et programmes officiels tunisiens (les sources)        |
| `www.na9ranal3ab.tn` · `*.supabase.co`                                      | vérifier la production après publication                       |

**Si le proxy déchiffre le TLS** (inspection SSL) : installer le certificat racine de
l'entreprise **dans le magasin Windows** (Claude Code le lit) et fournir le chemin du `.pem` pour
Node/npm — sans ça, chaque installation de dépendance échoue sur une erreur de certificat. Ne
jamais désactiver la vérification TLS pour contourner.

## 6. Machine

- **16 Go de RAM** recommandés. Mesuré sur ce poste : sous ~3 Go libres, les vérifications
  échouent en donnant des erreurs qui ressemblent à des régressions du code (2026-08-19).
- **20 Go d'espace disque libre** : les deux dépôts, leurs dépendances et les PDF sources.
- Processeur x64 (ou ARM64).

## 7. Ce qui **ne** se demande **pas** à l'admin

Pour éviter les allers-retours : ces points ne sont pas de son ressort.

- L'**abonnement Claude** (Pro ou Max) — compte personnel, pas une licence à acheter par la DSI.
- L'**accès au dépôt privé** — invitation GitHub à demander à Mohamed.
- Les **clones, dépendances et liens entre dépôts** — la session Claude Code les met en place
  elle-même une fois les outils installés (recette : `FableEtudes/METHODE-GENERATION-CONTENU.md`
  § Phase 0).

---

## Message prêt à envoyer

> Bonjour,
> Pour mon projet personnel de développement, j'ai besoin des logiciels suivants sur mon poste
> Windows 11 — tous gratuits, tous en source publique reconnue :
>
> ```powershell
> winget install OpenJS.NodeJS.LTS        # Node.js 24 (LTS)
> winget install Git.Git                  # Git + Git Bash — cocher « Enable symbolic links »
> winget install Anthropic.ClaudeCode     # Claude Code (assistant en ligne de commande)
> winget install GitHub.cli               # GitHub CLI
> winget install jqlang.jq                # jq
> winget install Microsoft.WindowsTerminal
> winget install Microsoft.VisualStudioCode
> winget install Microsoft.PowerShell     # PowerShell 7
> ```
>
> Et trois réglages qui comptent autant que les installations :
>
> 1. activer le **mode développeur** (Paramètres → Confidentialité et sécurité → Espace développeurs) ;
> 2. **exclure de l'antivirus** mon dossier de travail, `%USERPROFILE%\.claude` et le cache npm ;
> 3. autoriser sur le proxy : `api.anthropic.com`, `claude.ai`, `claude.com`,
>    `platform.claude.com`, `downloads.claude.ai`, `code.claude.com`, `registry.npmjs.org`,
>    `github.com`, `api.github.com`, `codeload.github.com`, `objects.githubusercontent.com`,
>    `raw.githubusercontent.com`, `www.cnp.com.tn`, `edunet.tn`.
>
> Merci d'avance.
