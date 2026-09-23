# `content/` — pipeline de contenu pédagogique

> **Propriété intellectuelle** : le contenu de ce dossier (cours, résumés, quiz, exercices,
> corrigés, registres) est protégé — **tous droits réservés**, aucune réutilisation ni
> rediffusion sans autorisation écrite. Voir [`../LICENSE-CONTENT.md`](../LICENSE-CONTENT.md).

Le contenu (matières, chapitres, cours, résumés, exercices) vit ici sous forme
de **fichiers versionnés**. Un générateur les valide puis les compile en
**migrations Supabase idempotentes**. On peut donc compléter / améliorer le
programme en continu, à partir de n'importe quelle source (sites en ligne,
manuels, repos locaux), avec une relecture en PR.

## Arborescence

```
content/
  <matière>/                 # ex. math
    subject.json             # méta matière (langue native, attribut, icône…)
    01-<slug>/               # un dossier par chapitre (préfixe = ordre)
      chapter.json           # titre, description, ordre, sources[]
      cours.md               # cours théorique complet (markdown)
      resume.md              # résumé du cours (markdown)
      quiz.json              # quiz de compréhension OBLIGATOIRE (verrou des exercices)
      exercices/
        01-<slug>.json       # un exercice QCM (questions + explications)
        02-<slug>.json
```

## Format des fichiers

- **`subject.json`** : `id`, `nameFr`, `description`, `attribute`, `colorToken`,
  `icon`, `displayOrder`, `contentLanguage` (`ar` | `fr` | `en`), `themeId`
  (thème d'appartenance — **obligatoire**, ex. `ecole-tn` pour le programme
  scolaire ou `francais` pour un module autonome), `gradeSlug` (niveau dans
  l'échelle du thème, ex. `9eme-base` ; `null` pour les matières indépendantes
  d'un niveau — le slug est résolu en UUID `grades` à la compilation, jamais
  codé en dur), `isPremium?` (dormant : en phase gratuite, la migration
  `20260711100000` force `is_premium = false` sur tous les parcours),
  `manuels?` (**manuel élève officiel CNP**, un objet par tome :
  `[{ "code": "102306" }]` ou
  `[{ "code": "102105P01", "label": "الجزء الأول" }, …]` — compilé dans
  `subjects.manuel_refs` et affiché en carte « Manuel officiel » sur la page
  matière. Le manuel est le livre de la **matière**, pas du chapitre : il se
  nomme donc ici, une fois. Le lien ouvre le document **chez le CNP**, sans
  compte et sans upload — l'adresse est rebâtie à partir du `code` seul, rien
  de plus à écrire pour l'obtenir),
  `compileTo?` (mutualisation lycée — voir plus bas).
- **`chapter.json`** : `title`, `description`, `displayOrder`, `sources` (liste
  d'URLs / références — traçabilité des sources), `gradeSlugs?` (dossier partagé
  uniquement : sections destinataires du chapitre), `domain?` (« section » du
  programme — libellé dans la langue de la matière), `manuel?`
  (`{ "code": "102905", "pages": "18-30" }` — les pages du manuel qui couvrent
  CE chapitre. Compilé dans `chapters.manuel_ref`, il sert la galerie « Pages du
  manuel » sous le cours : des images que **nous** hébergeons, connexion requise.
  À ne pas confondre avec le lien vers le manuel entier, qui vit au niveau de la
  matière),
  `videos?` (0-3 ids du registre `content/videos.json`).
- **`quiz.json`** (obligatoire) : `title?` + `questions[]` (même forme que les
  questions d'exercice). Compilé en exercice `mode='quiz'` ; l'élève doit le
  réussir (≥ `QUIZ_PASS_THRESHOLD_PCT`) pour débloquer les exercices du chapitre.
- **exercice `*.json`** : `title`, `difficulty` (1-4), `mode`
  (`practice` | `boss` | `challenge`), `xpReward`, `rewardCoins`, `displayOrder`,
  `gradeSlugs?` (dossier partagé uniquement), et
  `questions[]` : `{ prompt, options:[{id,text}], correctOption, explanation, difficulty? (1-3) }`.

> ⚠️ **Un `code` de manuel n'est pas du texte libre.** Il est confronté au registre CNP
> (`suivi/corpus-cnp.json`) par `content:qa` : un code absent du corpus est une **erreur**, pas un
> avertissement. Avant, une coquille se soldait par une carte restée vide ; depuis que le code sert
> à construire un lien public, elle se solderait par un 404 devant l'élève. Le nom de fichier se
> déduit du code — tome épelé (`102105P01`) pris tel quel, code nu (`102905`) complété en `P00`.

### Mutualisation entre sections (`compileTo` — étude 16)

Au lycée, plusieurs sections partagent des programmes identiques (tronc commun :
langues, philo, histoire-géo). Une matière partagée s'écrit **une seule fois**
dans un dossier « source » dont le `subject.json` déclare ses cibles :

```jsonc
{
  "id": "anglais-3eme-sec", // id source VIRTUEL (<matière>-<année>) — n'atteint jamais la DB
  // ... pas de gradeSlug racine ...
  "compileTo": [
    { "id": "anglais-3eme-sec-math", "gradeSlug": "3eme-sec-math" },
    { "id": "anglais-3eme-sec-lettres", "gradeSlug": "3eme-sec-lettres", "description": "…" },
  ],
}
```

À la compilation, le dossier devient **un subject par cible** (id
`<matière>-<gradeSlug>` verbatim, migration séparée par cible). `nameFr` /
`description` peuvent être surchargés par cible. Un chapitre ou un exercice
peut restreindre ses sections via `gradeSlugs` (sous-ensemble des cibles —
permet des paliers d3/d4 propres à une section dans le dossier partagé).
Slugs autorisés : le référentiel canonique (`KNOWN_GRADE_SLUGS`,
`src/shared/content/schema.ts`) hors nœuds plats legacy.

**Invariant capital** : les UUID v5 dérivent de l'**identité compilée** (id
cible + slugs), jamais du dossier source. **Forker** une section (lui donner
son dossier dédié en reprenant l'id cible et les slugs de chapitres/exercices)
ne perd donc **aucune progression élève**. Règle de partage : programme
officiel identique (constaté sur transcription) ⇒ partage ; divergence
structurelle ⇒ dossiers séparés ; divergence de profondeur seulement ⇒
partage + `gradeSlugs` par exercice — doctrine complète :
`docs/lycee-architecture.md` §2/§8 et `FableEtudes/16-ouverture-lycee/ETUDE.md` (D-4).

Tout est validé par Zod (`src/shared/content/schema.ts`). Un fichier invalide
n'atteint jamais la base.

**Notation standard dans toutes les langues** : chiffres occidentaux (0-9),
équations en notation internationale (LTR), unités SI — y compris dans le
contenu en arabe (prose arabe autour de maths standard ; jamais de chiffres
arabes-orientaux ٠١٢٣). Règle complète :
`.claude/skills/content-engine/references/math-and-notation.md`. La barre de
qualité des questions (distracteurs, explications, équilibre des clés,
auto-vérification) : `.claude/skills/content-engine/references/quality-bar.md`.

## Commandes

```bash
# depuis le moteur (yahia-quest-arena), corpus branché par le lien `content` :
npm run content:gates -- --tranche    # les 7 étages de la Content CI + les mesures de tranche
npm run content:tranche -- --changed  # seules les mesures de tranche (méthode § B2)
npm run content:check                 # valide tout le contenu (n'écrit rien)
```

> ⛔ **Ne lance jamais `content:build`** (avec ou sans `--subject`) : depuis l'étude 24 le contenu
> ne voyage plus en migrations, et sans `--sql-dir` ce script en écrit dans le dépôt **moteur**
> public — canal mort, et fuite de corpus que `leak:check` bloque. Un commit de contenu ne porte
> que des fichiers `content/`. Pour lire le SQL d'un sujet (facultatif, jamais committé) :
> `node --experimental-strip-types scripts/content/build.ts --subject <id> --sql-dir /tmp/sql-check`
> — un dossier partagé (`compileTo`) y émet un fichier par section cible.

> **Quel skill pour quoi ?** La carte complète du pipeline (skills de base `content-*` pour
> créer/compléter un chapitre vs professeurs `prof-*` pour rehausser le plafond en d3–4, + règles
> cumulatives) est dans `.claude/skills/content-engine/references/generation-pipeline.md`.

Les `id` de chapitres / exercices / questions sont des **UUID v5 déterministes**
dérivés des slugs : régénérer met à jour les lignes en place (pas de doublon),
et le contenu admin retiré est élagué automatiquement (le contenu créé par les
parents n'est jamais touché).

## Schémas explicatifs (figures SVG inline)

Les figures SVG embarquées dans les cours (`cours.md`) et les questions (un `<svg>`
par `prompt`) se créent, se rendent et se vérifient avec l'outillage
[`scripts/content/svg/`](../scripts/content/svg/README.md) :

```bash
npm run content:figures:check                              # lint structurel de toutes les figures
node scripts/content/svg/preview.mjs <fichier> /tmp/out.png # rend en PNG (décode les .json)
```

Points clés : un seul `<svg>` par champ, primitives autorisées par le sanitizer
(`src/shared/lib/figure.ts`), chiffres occidentaux partout, libellés à halo. Pour une
figure de **question**, la règle _answer-safe_ : ne montrer que le **donné**, jamais la
réponse — sinon rester en texte. Détails + `svglib.mjs` : voir le README de l'outillage.

## Workflow DB ↔ code

Le contenu **ne passe plus par les migrations** (étude 24 D-3) : `apply-content.yml` (ce dépôt)
compile chaque sujet en un fichier stable `sql/content/<sujet>.sql` et l'applique — en
**`workflow_dispatch` seulement**, donc **après** le merge et par un geste délibéré (un merge
n'applique rien). Le run garde la cible, prend un `pg_dump`, applique chaque sujet en une
transaction idempotente (rejouer est sûr) et journalise dans `content_releases` ;
`content-drift.yml` signale tout sujet dont `main` a bougé sans application. Procédure :
`FableEtudes/METHODE-GENERATION-CONTENU.md` § B3. On n'applique **jamais** à la main.

