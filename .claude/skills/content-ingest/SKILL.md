---
name: content-ingest
description: >-
  Ingest a SOURCE document (teacher PDF, polycopié, annales, a CNP manual or guide,
  a scan) into the content pipeline WITHOUT leaving the gated flow — sources from the
  `cnp-officiel` Drive folder, text layer first (§ Source et lecture) — and run the GISEMENT
  mode (étude 36):
  official national exam papers and online devoirs turned into exercises, couple by
  couple. Use whenever the user wants to « ingérer un PDF / document source »,
  « transcrire un manuel / une annale et en faire du contenu », « exploiter les
  concours et les devoirs en ligne », or to
  run the source→content path for the CNP corpus. Layers: text layer (Drive, 0 API
  key; ScribeKit optional, to scaffold) → AGENT vision only for what text misses
  (NO API key) → confront the official program → hand off to the generation
  skills. It TRANSCRIBES and
  ORCHESTRATES, it never writes content itself; output is always versioned content/
  files on a branch + gates + review, never a direct DB write. Defers to
  content-engine and content-ecole-tn.
---

# content-ingest — ingestion source → contenu (Drive, texte d'abord, vision en dernier)

**Rôle.** Amener un **document source arbitraire** jusqu'au **pipeline de contenu**, **entièrement à
l'intérieur du flux à gates**. Tu **transcris fidèlement, tu ne génères jamais** ; la génération
pédagogique reste chez les skills existants. Même famille que `curriculum-architect` : tu produis la
**transcription/fiche** + tu **orchestres**, tu ne dupliques pas le cœur de génération.

Docs : **[`FableEtudes/METHODE-GENERATION-CONTENU.md`](../../../FableEtudes/METHODE-GENERATION-CONTENU.md)
(LA méthode de référence source → fiche → contenu → prod — boucle, lots, profils de source, charte
tokens T-1…T-10 ; ce skill l'applique nativement)** +
[`FableEtudes/12-studio-ingestion`](../../../FableEtudes/12-studio-ingestion/ETUDE.md) (le canal) +
[`FableEtudes/13-moteur-transcription`](../../../FableEtudes/13-moteur-transcription/ETUDE.md) (le moteur
**ScribeKit**, devenu facultatif le 2026-11-03). Défère à `content-engine` (schéma, barre qualité,
récompenses, style, notation) et à `content-ecole-tn` (fidélité au programme officiel + recette).

## Source et lecture — la procédure (décision de Mohamed du 2026-11-03)

### Où sont les sources : le dossier Drive `cnp-officiel`

- <https://drive.google.com/drive/folders/1ZUUgEx71bKFsXulk_WL7cSfNxc6U9tmX>, dossier du compte Google
  du projet : **tout le corpus CNP** (375 PDF, base 1ʳᵉ–9ᵉ et secondaire 1ʳᵉ–Bac, élève et enseignant).
- Le connecteur **Google Drive** de la session doit être sur **le compte propriétaire du dossier** ;
  un autre compte voit « Requested entity was not found ».
- **Le site du CNP n'est plus la source** : injoignable depuis une session cloud (`content:manuel:fetch`
  → `curl 35`, mesuré le 2026-11-03). `content:manuel:fetch` ne sert plus que sur un poste local.

| Élément du dossier | Usage |
| --- | --- |
| `index.csv` | **l'inventaire**, à lire d'abord : `cycle,classe,type,code,file,bytes,status` (cycle 1 = base, 2 = secondaire ; classe 4 du cycle 2 = **Bac**). Codes = ceux de `suivi/corpus-cnp.json`. |
| `manuels/` | les PDF, `asasi/c<classe>/{eleve,enseignant}/` et `secondaire/…`, nommés `<code><tome>.pdf`. |
| `_txt/` | couches texte **déjà extraites** (`<code><tome>-<slug>.txt`). |
| `_render/`, `_render_lo/` | pages **déjà rendues** en PNG (`<code><tome>-NNN.png`). |
| `_transcriptions-wip/` | transcriptions brutes en cours (même contrat que `programmes-officiels/_tranches-wip/`). |

Trouver un fichier : `search_files` avec `title = '<code><tome>.pdf'`, jamais une navigation dossier par
dossier. Un fichier fraîchement versé peut mettre quelques minutes à être indexé : chercher à nouveau
avant de conclure qu'il manque, et seulement alors le demander à Mohamed.

### Lire au moindre coût : l'échelle L0 → L3

Chaque page se lit au **premier barreau qui suffit**. La vision est le dernier barreau, plus le cas général.

| Barreau | Quand | Comment |
| --- | --- | --- |
| **L0** texte déjà extrait | `_txt/<code><tome>-*.txt` existe | `read_file_content` sur le `.txt` |
| **L1** couche texte du PDF | manuel en **français / anglais** (secondaire scientifique, Bac) | `read_file_content` sur le PDF |
| **L2** couche texte décodée | manuel **arabe** à polices propriétaires (sortie brouillée `jÉØµdG øe…`) | `read_file_content`, puis la table glyphe → lettre de la fiche (`programme/6eme-base/arabe.md` § 7, `programme/1ere-base/arabe.md` § 7-2) |
| **L3** vision | formules, vecteurs, fractions, tableaux, figures, encadrés vocalisés, pages sans texte, **et** le sondage ci-dessous | PNG de `_render/` lu avec **Read** (à défaut `render.sh`) |

Mesures (2026-11-03) : L1 sur `222422P00` (maths Bac lettres) rend le manuel entier en 79 475 caractères,
prose et consignes propres, formules et figures dégradées ; L2 sur `501603P00` rend 107 612 caractères de
glyphes que la table de la fiche 6ᵉ décode (0 glyphe inconnu sur 899 pages), harakat non fiables.

- Au-delà d'environ 80 000 caractères, `read_file_content` écrit son résultat dans un **fichier local**
  (JSON `{fileContent, title, viewUrl}`) : le traiter avec `python3 -I`/`jq`, **dans un sous-agent**.
- Le texte n'a **pas de marqueur de page fiable** : ancrer chaque passage sur le numéro imprimé, le
  vérifier sur le PNG de `_render/`.
- **Jamais** `download_file_content` sur un PDF (il revient en base64 dans la conversation).
- **Pas de clé API** : la vision L3 est celle de l'agent (abonnement). Le `--provider anthropic` de
  ScribeKit exige une clé facturée : seulement si l'humain en fournit une et le demande.
- **ScribeKit est facultatif** : seulement pour échafauder une fiche neuve (`scribekit app-cnp`) et
  valider le manifeste.

### Ce qui compte comme « lu » au registre

Une page lue en L0, L1 ou L2 **compte comme lue** (`pagesLues` de `suivi/<grade>.json`) dès qu'un
**sondage image** l'a validée : **au moins une page sur dix** de la plage, choisies parmi les plus denses
(tableaux, encadrés, exercices), confrontées au PNG, **0 écart substantiel** (mot ou nombre faux, ligne
sautée, ordre inversé). Un écart ⇒ la section entière est sondée ; trois ⇒ elle passe en L3. Le sondage
se note dans la fiche (pages, écarts). Cette règle remplace celle du 2026-09-22 (« une couverture par
décodage n'est pas une lecture ») : une fiche à 100 % maintenue `partielle` pour ce seul motif (5ᵉ et 6ᵉ
arabe) passe à `complete` une fois le sondage fait et noté.

### Les trois couches du travail

1. **Lire** — l'échelle ci-dessus, et **transcrire fidèlement** (chiffres 0-9, LTR, jamais
   d'arabo-indiens ; `[?]` pour l'illisible, `[sic]` pour la coquille ; **rien d'inventé**).
2. **Fiche** — profondeur de génération (R-5), confrontée au programme (R-3), au registre (R-4).
3. **Génération** — hand-off à `content-ecole-tn`/wrappers + `content-cours` + `content-interactif` +
   `prof-*`. Tu ne génères pas toi-même.

Le **modèle** de chaque sous-agent (lecteur, auteur, auditeur…) se choisit par la table du skill
`campagne` § 3 bis.

## Règles (non négociables)

- **R-1 — Rien ne contourne le pipeline.** Sortie = TOUJOURS des fichiers `content/` (ou une transcription
  `programme/…`) sur une branche + gates (`content:check` / `content:qa:strict` / `content:audit`) + revue
  humaine. **Aucune écriture DB**, aucun skip d'audit.
- **R-2 — Provenance & droits.** Chaque source porte auteur / origine / autorisation ; un document sous
  droits sans autorisation est **refusé**. Les `chapter.sources[]` citent le document. Doute ⇒ **STOP**.
  **Les sujets officiels des examens nationaux** (concours de 6ᵉ, concours de 9ᵉ, baccalauréat, toutes
  sessions) sont du **corpus officiel** (décision du 2026-09-28, étude 27 Q-6) : tu les transcris comme
  un manuel CNP, sans autorisation à demander, et tu les cites. D'un site qui les ré-héberge, tu ne
  prends que le sujet ; son corrigé et ses commentaires, comme le devoir d'un établissement, restent une
  source web.
  **Source du WEB** (site de devoirs, blog d'enseignant, portail d'annales) : profil `source-web` de la
  méthode — déclare le **tier** avant le premier token. T0 (veille), T1 (lien sortant) et T2′ (génération
  inspirée) ne demandent aucune autorisation ; seule la **transcription (T2)** en exige une, écrite. Tu
  n'es appelé que pour T2 : sans autorisation en main, **tu ne transcris pas** — tu produis une fiche de
  veille et tu passes la main aux skills de génération. `content:qa` vérifie l'absence de reprise verbatim
  (étude 27 R-8), donc une copie « discrète » échouera le gate, pas la revue.
- **R-3 — Programme d'abord.** Pour une matière scolaire, confronter la fiche à la **transcription CNP**
  (`programme/<grade>/<matière>.md`) si elle existe ; divergence de scope ⇒ le **programme officiel gagne**,
  signaler l'écart (règle `content-ecole-tn`).
- **R-4 — Vérifie l'existant AVANT toute campagne, dans le REGISTRE.** L'état de transcription vit dans
  `programmes-officiels/suivi/<grade>.json` (statuts normés, couverture en plages de pages, profondeur),
  validé en CI par `npm run programme:check` — `programme/_INDEX.md` n'est qu'une **vue générée**
  (`programme:index`), ⛔ jamais éditée à la main. Une entrée `complete`/`validee-r7`/`promue` = **déjà
  fait** ; `partielle` = **compléter** (les plages manquantes sont listées), jamais refaire. Vérifie aussi
  qu'aucune autre session ne tient déjà le couple — par le **scan à trois pattes** du skill `campagne`
  (§ 1 bis : worktrees, branches non mergées, PR ouvertes, en grepant le nom FR **et** le préfixe de
  sujet) ; un grep sur un préfixe de branche comme `feat/transcription-*` rend vide à tort. Le check CI
  rejette un même PDF revendiqué par deux fiches — les incidents de doublons (2026-07-12 collège,
  2026-07-17 vague-A) ne peuvent plus passer. En cas de doublon hérité : comparer, garder la meilleure
  copie, documenter dans le registre.
- **R-5 — Standard de fiche : « profondeur de génération », jamais un résumé.** Une fiche destinée à
  alimenter la génération pédagogique doit décrire **chaque activité/exercice individuellement** (énoncé,
  données, ce qui est demandé), reproduire **verbatim** les encadrés de règles/lois officielles, relever le
  vocabulaire officiel, et poser des bornes de scope INCLUS/EXCLU — modèle de référence :
  `programme/1ere-sec/mathematiques.md`. Une fiche « first-pass » (structure + objectifs seulement, sans ce
  niveau de détail) doit être étiquetée comme telle et **jamais confondue avec une fiche prête pour la
  génération** — l'écart de qualité entre les deux est la cause directe d'un contenu généré médiocre.
- **R-6 — Une session = une matière, lecture intégrale obligatoire.** Ne jamais plafonner arbitrairement
  la lecture d'une source (l'incident du 2026-07-10 a lu 15-76 % des sources avant d'écrire, plafonné à
  70 000 caractères par manuel, produisant une fiche truffée d'inventions). Traiter plusieurs matières dans
  la même fenêtre de contexte dilue le budget de lecture par matière et bâcle chaque fiche — un lot batch
  de 10 fiches en une nuit est le signe qu'on va trop vite. Une matière incomplète mais honnêtement étiquetée
  (« profondeur : modules 1-4 faits, 5-7 en first-pass ») vaut mieux qu'un lot complet mais bâclé.
- **R-7 — Vérification indépendante avant promotion.** Une fiche produite par une session/agent ne devient
  la référence canonique (`programme/<grade>/<matière>.md`, cochée dans `_INDEX.md`) qu'après relecture par
  un second agent qui re-vérifie contre la source elle-même (pas contre la fiche) — pas seulement contre son
  propre travail. Protocole (sondage dirigé, règle T-8 de la méthode) : 100 % du critique (encadrés
  verbatim, chapitrage/manifeste, zones `[?]`) + ≥15 % des pages restantes ; ≥3 erreurs substantielles ⇒
  re-lecture intégrale.
- **Fidélité, pas de génération.** La lecture (texte ou vision) **transcrit** ; difficulté / calibrage / QCM
  / cours = **génération** (couche 3), jamais ici.

## Workflow

0. **Cadrage.** Quel document ? Cible (thème / grade / matière) ? Droits (R-2) ? Les PDF : `index.csv`
   du Drive puis `search_files` par titre (§ Source et lecture).
1. **Lire** au moindre coût, L0 → L1 → L2 → L3, et transcrire par tranches de 10–20 pages au format final
   (T-2), directement dans la fiche `programme/<g>/<matière>.md` (gabarit `_TEMPLATE.md`) — ou, pour une
   fiche neuve, après l'échafaudage facultatif `scribekit app-cnp <guide.pdf> <manuel.pdf> --grade
   <gradeSlug> --subject <id> --lang <ar|fr|en> -o <programmes-officiels>` (source libre :
   `scribekit transcribe <inputs…> --profile markdown`).
2. **Sonder** chaque plage lue par le texte (§ Ce qui compte comme « lu ») et noter le sondage.
3. **Fiche + confrontation CNP (R-3).** Compléter la fiche (périmètre, notions, exemples, exercices du
   document, bornes) ; pour le scolaire, confronter au `programme/<grade>/<matière>.md`.
4. **Registre.** Mettre à jour `suivi/<grade>.json` (statut normé, profondeur, plages `pagesLues` par
   source, r7) et régénérer la vue : `npm run programme:index` + `npm run programme:check` (0 erreur) ;
   si ScribeKit a servi, `scribekit qa` aussi.
5. **Hand-off génération.** Invoquer les skills de génération pour produire `cours.md` / `resume.md` /
   `quiz.json` / `exercices/*` à partir de la transcription — ce que devient chaque contenu du manuel
   (exercice, figure, encadré) et ce qui se trace est normé par
   `content-engine/references/manuel-valorisation.md` — puis suivre la recette `content-ecole-tn`
   (`npm run content:gates -- --tranche` → PR de fichiers `content/` seuls → revue → merge → **publication
   par dispatch** d'`apply-content.yml`, méthode § B3 ; jamais `content:build`, aucune migration).
   **Livraison par tranches de ≤4 chapitres complets** — commit local par chapitre, une PR par tranche,
   jamais une matière entière retenue non poussée (méthode, T-10 ; interruption ⇒ sauvegarde `wip/`).

## Mode gisement — examens nationaux et devoirs en ligne (étude 36)

Quand la demande est d'**exploiter les sujets d'examen et les devoirs publiés en ligne** d'un
couple classe × matière, tu déroules le pipeline de l'étude 36 (fusion des études 12 et 27), dans
cet ordre : qualifier → fixer l'échantillon **avant** de lire → lire → carte et écart → plan →
écrire → prouver → livrer et publier → mesurer. Deux régimes, jamais mélangés :

- **sujet d'examen national** (concours de 6ᵉ, de 9ᵉ, bac) : corpus officiel (R-2). Tu le
  transcris fidèlement sous `programmes-officiels/examens-nationaux/<classe>/<matière>/<session>.md`
  et chaque exercice devient une mission qui le **reprend** et le **cite** ;
- **devoir ou série d'un site** : `source-web`, tier T2′. Salle blanche : le lecteur rend une
  ligne anonyme par exercice, l'auteur écrit une mission neuve par archétype distinct sans jamais
  voir la source, et le contrôle local contre les snapshots (hors git) le prouve.

Le déroulé, les commandes et le registre du couple : [`references/gisement.md`](references/gisement.md).
Les consignes de rôle, à passer telles quelles aux sous-agents :
[`gisement-lecteur.md`](references/gisement-lecteur.md),
[`gisement-auteur-devoir.md`](references/gisement-auteur-devoir.md),
[`gisement-auteur-examen.md`](references/gisement-auteur-examen.md),
[`gisement-auditeur.md`](references/gisement-auditeur.md). Dans ce mode aussi, tu orchestres :
les missions s'écrivent avec les skills `prof-*`, jamais par toi.

## STOP (escalade — ne re-designe jamais en silence)

- Doute sur les **droits** d'une source ⇒ STOP (R-2).
- Scan **illisible** / manuscrit ⇒ signaler, **ne pas deviner** (fidélité).
- Divergence transcription ↔ programme officiel ⇒ le **programme gagne**, signaler (R-3).
- Tentation d'utiliser une **clé API** alors que l'abonnement suffit ⇒ ne pas le faire ; rester
  **agent-in-the-loop**.
- Besoin d'un **format de contenu inexistant** ⇒ signalement vers l'étude 03 / le catalogue, jamais un
  format ad hoc.
- Budget de lecture/contexte insuffisant pour finir une matière en profondeur ⇒ **STOP proprement** à la
  fin de la dernière section traitée, étiquette clairement ce qui reste en first-pass (R-6) ; ne bâcle
  jamais le reste pour "finir".

Défère toujours à **CLAUDE.md** / **ARCHITECTURE.md** et aux `docs/*.md` normatifs.
