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
>
> ⚠️ **Et surtout — le poste bloque à l'*exécution*, pas à l'installation.** Constaté le
> 2026-09-02 sur `gh.exe`, `fnm.exe` et Bitwarden : le contrôle applicatif du poste réclame une
> autorisation pour tout binaire non approuvé lancé depuis le profil utilisateur. **La § 0
> ci-dessous est donc le vrai ticket** ; le reste de la page ne sert à rien sans elle.

⚠️ Les identifiants `winget` ci-dessous sont ceux du dépôt public ; les confirmer d'un
`winget search <nom>` avant l'installation. Et l'installation n'est que la moitié de la demande :
sur ce poste, c'est l'**approbation à l'exécution** (§ 0) qui décide si l'outil sert à quelque
chose.

---

## 0. Le vrai blocage — le contrôle applicatif

Le poste applique **Avecto / BeyondTrust Privilege Management** (règle
`[PRD]S-TN-C-Avecto-OIT (Default) — Any Application`). Tout exécutable non approuvé ouvre la
fenêtre « Assistance demandée » et réclame un compte du domaine `SOFRECOM` ou un **code de
réponse**. Vu le 2026-09-02 sur `gh.exe`, `fnm.exe` et Bitwarden — tous lancés depuis
`c:\users\mbeji\appdata\local\…`.

Deux conséquences, à poser d'entrée dans le ticket :

- **Installer ne suffit pas.** Un logiciel correctement installé reste bloqué au lancement.
- **Le code de réponse ne suffit pas non plus** : il débloque **une exécution**. Or chaque outil,
  chaque mise à jour automatique et chaque binaire posé par `npm` en redemande un — c'est un
  ticket par lancement, pas une solution.

**Ce qu'il faut demander, en trois points :**

1. **Approuver par éditeur (signature), jamais par empreinte.** Une règle par hash se casse à
   chaque mise à jour et ramène le blocage. Éditeurs concernés : **Anthropic, PBC** ·
   **GitHub, Inc.** · **Microsoft Corporation** · **OpenJS Foundation / Node.js** ·
   **Git for Windows**.
2. **Installer en portée machine** (`winget … --scope machine`, donc `C:\Program Files`) plutôt
   que dans le profil utilisateur : c'est le profil qui déclenche la politique. Possible pour
   Node.js, Git, GitHub CLI, VS Code et PowerShell 7.
3. **Autoriser deux chemins**, sinon l'outillage se rebloque tout seul au fil de l'eau :
   - `%USERPROFILE%\.local\share\claude\versions\*` — Claude Code s'auto-met à jour **dans le
     profil**, avec un binaire signé « Anthropic, PBC » ;
   - le **dossier de travail du projet**, dont ses `node_modules\.bin` — `npm` y pose des
     exécutables tiers qui, autrement, redemandent une autorisation un par un.

**Une demande à retirer** : `fnm` (gestionnaire de versions de Node) sort en *éditeur inconnu* —
il ne passera jamais, et le projet n'en a pas besoin. Node 24 en MSI machine suffit, et évite au
passage le piège du Node 22 masqué (§ 1).

## 1. Le strict nécessaire — 4 logiciels

Sans ces quatre-là, rien ne démarre.

| Logiciel                | Version              | `winget install`         | Pourquoi / ce qui casse sans lui                                                                                                                                                            |
| ----------------------- | -------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Node.js**             | **24.x** (LTS)       | `OpenJS.NodeJS.LTS --scope machine`      | Fait tourner **toutes** les vérifications du projet (`content:check`, `content:qa:strict`, `content:audit:strict`, `programme:check`) et l'utilitaire de transcription. Le dépôt épingle 24. |
| **Git for Windows**     | dernière             | `Git.Git --scope machine`          | Git **et Git Bash** — c'est le shell dont Claude Code se sert sous Windows. Sans lui, l'outil retombe sur PowerShell et une partie du flux ne marche plus pareil.                            |
| **Claude Code**         | dernière             | `Anthropic.ClaudeCode`   | L'outil de travail lui-même (assistant en ligne de commande). S'auto-met à jour en arrière-plan — voir le §5 réseau.                                                                        |
| **GitHub CLI (`gh`)**   | dernière             | `GitHub.cli --scope machine`          | Ouvre les *pull requests*, lit l'état des vérifications, déclenche la publication du contenu. Aujourd'hui en zip portable faute de droits : à réinstaller proprement, avec un PATH machine.  |

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
| **jq**                  | `jqlang.jq`                    | **Absent aujourd'hui.** Les scripts qui lisent du JSON rendent alors du vide *sans erreur* : la surveillance affirme « aucune PR », « aucun check », et c'est faux. Exécutable **non signé**, donc le plus dur à faire approuver : s'il est refusé, on s'en passe — `gh --jq` embarque le même moteur. |
| **Windows Terminal**    | `Microsoft.WindowsTerminal`    | Onglets, et surtout un rendu UTF-8 correct : le corpus est trilingue **français / anglais / arabe**, avec de l'écriture de droite à gauche.                        |
| **Visual Studio Code**  | `Microsoft.VisualStudioCode --scope machine` | Relire les modifications, les figures SVG et l'arabe avant publication. L'extension Claude Code s'y branche.                                                       |
| **PowerShell 7**        | `Microsoft.PowerShell --scope machine` | Les jonctions de dossiers et les scripts d'installation ; meilleur support UTF-8 que le PowerShell 5 livré avec Windows.                                          |

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
| `crt.sectigo.com`                                                           | **indispensable** : le CNP ne sert pas son certificat intermédiaire — sans ce domaine, tout téléchargement du corpus échoue en erreur TLS |
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
> Pour mon projet personnel de développement, j'ai besoin des outils suivants sur mon poste
> Windows 11 — tous gratuits, tous en source publique reconnue. Le poste étant sous **contrôle
> applicatif** (Avecto / BeyondTrust), l'installation seule ne suffit pas : les exécutables lancés
> depuis mon profil sont bloqués (« Assistance demandée »), et le code de réponse ne débloque
> qu'une exécution à la fois.
>
> **1. Les installations, en portée machine autant que possible :**
>
> ```powershell
> winget install OpenJS.NodeJS.LTS --scope machine         # Node.js 24 (LTS)
> winget install Git.Git --scope machine                   # Git + Git Bash — cocher « Enable symbolic links »
> winget install GitHub.cli --scope machine                # GitHub CLI
> winget install Microsoft.VisualStudioCode --scope machine
> winget install Microsoft.PowerShell --scope machine      # PowerShell 7
> winget install Microsoft.WindowsTerminal
> winget install Anthropic.ClaudeCode                      # signé « Anthropic, PBC »
> winget install jqlang.jq                                 # optionnel (non signé)
> ```
>
> **2. Les approbations dans la politique de contrôle applicatif** — par éditeur (signature), pas
> par empreinte, sinon chaque mise à jour rebloque :
>
> - éditeurs à approuver : **Anthropic, PBC** · **GitHub, Inc.** · **Microsoft Corporation** ·
>   **OpenJS Foundation / Node.js** · **Git for Windows** ;
> - chemins à autoriser : `%USERPROFILE%\.local\share\claude\versions\*` (Claude Code s'auto-met
>   à jour dans le profil) et mon dossier de travail, dont ses `node_modules\.bin`.
>
> **3. Et trois réglages :**
>
> 1. activer le **mode développeur** (Paramètres → Confidentialité et sécurité → Espace développeurs) ;
> 2. **exclure de l'antivirus** mon dossier de travail, `%USERPROFILE%\.claude` et le cache npm ;
> 3. autoriser sur le proxy : `api.anthropic.com`, `claude.ai`, `claude.com`,
>    `platform.claude.com`, `downloads.claude.ai`, `code.claude.com`, `registry.npmjs.org`,
>    `github.com`, `api.github.com`, `codeload.github.com`, `objects.githubusercontent.com`,
>    `raw.githubusercontent.com`, `www.cnp.com.tn`, `edunet.tn`, `crt.sectigo.com`.
>
> Merci d'avance.
