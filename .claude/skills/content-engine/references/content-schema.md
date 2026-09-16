# Content schema — exact file shapes & constraints

Source of truth: `src/shared/content/schema.ts` (Zod) + `src/shared/content/loader.ts` (file
layout). Anything that fails validation never reaches the DB. **Read this before writing any file.**

## Directory layout (loader.ts)

```
content/
  <subject-id>/                 # a dir is a SUBJECT iff it contains subject.json
    subject.json                # REQUIRED
    NN-<slug>/                  # a dir is a CHAPTER iff it contains chapter.json; dir name = chapter slug
      chapter.json              # REQUIRED
      cours.md                  # REQUIRED, non-empty after trim → chapters.lesson_content
      resume.md                 # REQUIRED, non-empty after trim → chapters.summary
      quiz.json                 # REQUIRED (mandatory comprehension gate)
      exercices/                # OPTIONAL (French spelling). Each *.json = one exercise
        NN-<slug>.json          # filename minus ".json" = exercise slug
```

- Subjects/chapters are discovered by the presence of `subject.json` / `chapter.json`.
- `NN-` numeric prefixes only sort the folders on disk; the real ordering in-app is `displayOrder`.
- The chapter **directory name** is its slug; the exercise **filename** (minus `.json`) is its slug.
- `quiz` is a **reserved exercise slug** (the compiled quiz uses it) — never create `exercices/quiz.json`.
- IDs are deterministic UUIDv5 from slug paths (`subjectId/chapterSlug/exerciseSlug/qN`). Stable
  slugs ⇒ in-place updates; renames ⇒ delete+recreate.

## subject.json

| Field             | Type         | Required    | Constraint                                                                                                                                                                                              |
| ----------------- | ------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`              | string       | yes         | kebab-case `^[a-z][a-z0-9-]*$`, unique. Becomes `subjects.id` literally                                                                                                                                 |
| `nameFr`          | string       | yes         | non-empty. The only display name — write it in the subject's **own `contentLanguage`** (ar→`الرياضيات`, en→`English`, fr→`Français`). Field name is legacy (DB compat); the value is native, not French |
| `description`     | string       | yes         | non-empty                                                                                                                                                                                               |
| `attribute`       | string       | yes         | non-empty (RPG attribute label, e.g. "Force", "Logique")                                                                                                                                                |
| `colorToken`      | string       | yes         | non-empty, maps to a CSS var (e.g. `subject-math`)                                                                                                                                                      |
| `icon`            | string       | yes         | non-empty, a lucide icon name (e.g. `GraduationCap`)                                                                                                                                                    |
| `displayOrder`    | number       | yes         | positive integer                                                                                                                                                                                        |
| `contentLanguage` | enum         | yes         | `"ar"` \| `"fr"` \| `"en"` — the one language the content is written in (drives RTL)                                                                                                                    |
| `themeId`         | string       | yes         | kebab-case, FK → an existing `themes.id` (see themes-and-trilingual.md)                                                                                                                                 |
| `gradeSlug`       | string\|null | no (→null)  | school subjects only (e.g. `9eme-base`); `null` for standalone themes                                                                                                                                   |
| `isPremium`       | boolean      | no (→false) | **legacy/secondary** — premium is now decided **per parcours**, not by this flag                                                                                                                        |

There is **no** `nameEn`/`nameAr` — `nameFr` is the single display-name field, and you write it in the
subject's `contentLanguage` (the "Fr" in the name is legacy only). There is **no** per-language text
anywhere else.

> **Premium is per-parcours, not per-subject — but dormant in the current free phase.** Access is
> governed by the parcours a subject resolves to (its theme+grade) and enforced server-side by
> `resolve_exercise_access` — not by `isPremium`. The `isPremium` flag is legacy and no longer read
> by the gate; leave it `false`/omit it. Every parcours is currently `is_premium=false` (2026-06-21
> pivot + étude 15 Q-2), so **nothing is gated today**. The **free preview** (the chapter
> comprehension quiz + every difficulty-1 mission) is what would still show on a premium parcours if
> one is ever reactivated (frozen étude `FableEtudes/01-paiement-en-ligne`). See CLAUDE.md "Access
> gate".

## chapter.json

| Field          | Type     | Required | Constraint                                                                            |
| -------------- | -------- | -------- | ------------------------------------------------------------------------------------- |
| `title`        | string   | yes      | non-empty (in the subject's language)                                                 |
| `description`  | string   | yes      | non-empty                                                                             |
| `displayOrder` | number   | yes      | positive integer                                                                      |
| `sources`      | string[] | no (→[]) | each ref ≥3 chars — URLs/citations you actually used (hybrid sourcing)                |
| `manuel`       | object   | no       | `{ code, pages }` — official student-textbook pages covering this chapter (see below) |

> Subject-level sibling: `subject.json` accepts an optional `manuels` array —
> `[{ "code": "102306" }]`, one entry per PDF volume with an optional `label`
> (e.g. `"الجزء الأول"`) — compiled into `subjects.manuel_refs` and surfaced as
> the login-gated « Manuel officiel » card on the subject page. PDFs are
> uploaded out-of-band (`scripts/manuel/upload-pdf.mjs`, private bucket
> `manuel-eleve`, path `<code>.pdf`).

`cours.md` and `resume.md` are separate files, not fields.

### `manuel` — official student-textbook (manuel élève) pages

For school content (`content-ecole-tn`), a chapter MAY link to the pages of the **official CNP
student textbook** that cover it, so the app can show them under the course (login-gated
"Pages du manuel" gallery). Shape:

```json
"manuel": { "code": "103304", "pages": "12-15" }
```

| Field   | Type   | Constraint                                                                                                            |
| ------- | ------ | --------------------------------------------------------------------------------------------------------------------- |
| `code`  | string | alphanumeric `[A-Za-z0-9_-]+` — the CNP **manuel élève** book code (not the teacher guide)                            |
| `pages` | string | 1-based page expression: a single page, an inclusive range, or a comma list — `"12"`, `"12-15"`, `"12-15, 18, 20-21"` |

The build expands `pages` into a sorted, de-duplicated `pageNumbers[]` and stores
`{ code, pages, pageNumbers }` in `chapters.manuel_ref` (JSONB). Optional and additive — omit it
when the mapping is unknown. The page **images** are served from a separate access-controlled
bucket; this field carries only the metadata.

## Question object (shared by quiz.json and exercise files)

Questions are a **discriminated union on `type`**. Omitting `type` means `mcq` — every
pre-existing file stays valid unchanged. Les six types natifs sont livrés et TOUS authorables :
`mcq`, `numeric`, `ordering`, `matching`, `multi` (`docs/interactive-question-types.md`) et
`short_answer` — la **question libre sans réponses proposées** (étude 20 lot 7, arena#654), qui
rouvre la clôture « no more native types » de cette spec.

**`mcq` (default) — the classic QCM:**

| Field           | Type     | Required | Constraint                                                                      |
| --------------- | -------- | -------- | ------------------------------------------------------------------------------- |
| `type`          | string   | no       | `"mcq"` (or omitted)                                                            |
| `prompt`        | string   | yes      | non-empty                                                                       |
| `options`       | option[] | yes      | **2–6** items (use 4). Each `{ id: string≥1, text: string≥1 }`                  |
| `correctOption` | string   | yes      | must equal one of the option **ids** (not the text, not an index)               |
| `explanation`   | string   | yes      | non-empty (revealed by the hint consumable). Aim ≥25 chars — see quality-bar.md |
| `difficulty`    | number   | no       | integer 1–3 (untagged → treated as 2). Questions are emitted easiest→hardest    |

Cross-field rules (Zod refine): option **ids must be unique**; `correctOption` ∈ option ids.
Convention: option ids `a`,`b`,`c`,`d`.

**Optional `misconceptionTag` per distractor (mcq only — étude 04, moteur adaptatif).** Any
_wrong_ option may carry `"misconceptionTag": "<id>"` naming the error a student who picks it is
making. It is **server-only diagnostics**: `sql-builder` routes it into the `questions.distractor_tags`
map and **strips it from `options`** (it never reaches the client — R-1), so the correct option must
stay **untagged** (Zod errors otherwise). The id must be **namespaced by subject** (`math.frac.add-denominators`)
and **declared in the registry `content/misconceptions.json`** (`content:qa` errors on an unknown or
undeclared tag). The registry maps each id → `{ subject, labels: { fr, en, ar } }` (the student-facing
wording; the tag itself is never displayed). Tagging is **optional and progressive** — leave distractors
untagged when the error isn't crisp; the `prof-*` trap taxonomies are the natural source of tags. Only
`mcq` resolves telemetry (the wire choice equals the option id), so only `mcq` options take the field.

**La règle de décision — tagger ou laisser muet (étude 30, lot 0bis).** « Optionnel et progressif »
ne veut pas dire « au jugé » : le champ vide est une **décision**, pas un reste de campagne. Le lot 0
de é30 avait taggé `math` 9ᵉ sans trancher les 297 questions restées muettes ; le lot 0bis les a lues
une à une et en a fixé la règle. Un distracteur reçoit son `misconceptionTag` **si et seulement s'il
est reconstructible** : on sait nommer une erreur du registre ET montrer le chemin qui mène **de
l'énoncé à CETTE option exactement**. Trois portes donnent ce oui, dans cet ordre :

| porte  | ce qui la déclenche                                                                                                                                                          | exemple mesuré                                                                                                                            |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **R1** | l'`explanation` **nomme déjà** l'erreur et dit quelle option elle produit (« الخطأ الشائع … فيخرج X »)                                                                        | « قلب النسبة (AM = 12 × 9/6 = 18) » ⇒ l'option `18 cm` prend `math.geo.thales-rapport-inverse`                                             |
| **R2** | **tout le jeu** de distracteurs est construit sur une seule erreur                                                                                                            | les trois couples faux d'un système vérifient **exactement une** des deux équations ⇒ `math.alg.systeme-verification-partielle` sur les trois |
| **R3** | l'option est le calcul juste avec **une** opération nommée inversée ou omise, sans autre lecture possible                                                                     | `πrh` au lieu de `πr²h` ⇒ `math.mes.rayon-non-eleve-au-carre`                                                                              |

Et on **laisse muet** — sans y revenir — dans ces trois cas, qui ne sont pas des échecs :

- le **nombre de remplissage** : une valeur proche qu'aucun geste identifiable ne produit (elle
  n'est là que pour faire quatre options) ;
- l'**ambiguïté** : deux erreurs différentes mènent à la même option. Un mauvais tag enseigne une
  fausse erreur — il coûte plus cher que pas de tag du tout ;
- l'**erreur réelle mais sans entrée** au registre, et **non récurrente**. Le registre est un
  vocabulaire fermé : on ne l'étend que si l'erreur revient dans **≥ 3 questions distinctes** et se
  dit en **une phrase adressée à l'élève**. En dessous du seuil : muet, et on note l'erreur pour la
  campagne suivante.

Deux conséquences à connaître avant de viser un chiffre :

1. **100 % n'est pas la cible.** Sur `math` 9ᵉ, la règle appliquée aux 818 questions plafonne à
   **81 % (662/818)** — les 156 restantes sont des muettes **statuées**, pas des impayés. Une
   couverture qui monterait au-delà signalerait un tag posé au jugé, pas un corpus mieux tenu.
2. **Le premier tag manquant est souvent le plus commun.** Le lot 0bis a dû ouvrir
   `math.alg.reponse-a-l-autre-inconnue` — « tu donnes une autre grandeur que celle demandée » — qui
   sert **54 fois** à lui seul. C'est une erreur de **lecture d'énoncé**, pas de compétence : elle est
   donc déclarée **sans** `competency` (le champ est optionnel exactement pour ça), et le bloc de
   correction nomme l'erreur sans proposer d'exercice. Avant d'écarter une erreur parce qu'elle
   « n'est pas mathématique », vérifier qu'elle n'est pas simplement de ce type-là.

**`numeric` — native free numeric entry (no options, no elimination):**

| Field                 | Type   | Required | Constraint                                                                                                                                       |
| --------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `type`                | string | yes      | `"numeric"`                                                                                                                                      |
| `prompt`              | string | yes      | non-empty. **State the expected unit and precision in the prompt** ("en cm²", "arrondi au centième")                                             |
| `answerKey.value`     | number | yes      | the canonical answer (finite; standard Western-digit notation)                                                                                   |
| `answerKey.tolerance` | number | no       | accepted absolute deviation; **omit for exact** (0). Keep it proportionate — `content:qa` errors when tolerance ≥ \|value\| and warns above 25 % |
| `answerKey.unit`      | string | no       | informative label only — the student never types the unit; the hint lives in the prompt                                                          |
| `explanation`         | string | yes      | same bar as mcq; **echo the canonical value** in the worked solution                                                                             |
| `difficulty`          | number | no       | same semantics as mcq                                                                                                                            |

The student types a plain number (`-`, `.` or `,` decimal); the server scores
`abs(x − value) ≤ tolerance` via `score_answer`. Use `numeric` when options would give the
answer away by elimination (calculs, mesures, résultats d'équations); keep `mcq` when the
distractors themselves teach (misconception encoding — see expert-exercises.md).

**`ordering` — native drag-&-drop sequencing (B2):**

| Field             | Type     | Required | Constraint                                                                                  |
| ----------------- | -------- | -------- | ------------------------------------------------------------------------------------------- |
| `type`            | string   | yes      | `"ordering"`                                                                                |
| `options`         | option[] | yes      | **3–6** steps to arrange (shuffled at render). Ids alphanumeric (`a`…, no `,`/`:`/spaces)   |
| `answerKey.order` | string[] | yes      | the correct id sequence — must be an **exact permutation** of the option ids (Zod-enforced) |
| `explanation`     | string   | yes      | justify the ORDER (why this step before that one), not just restate it                      |

Scoring is an exact sequence match, all-or-nothing. Step texts must be unambiguous and
mutually distinct (`content:qa` errors on duplicates) and each step self-contained — never
"then…" phrasing that only works in one position.

**`matching` — native drag-&-drop pair alignment (B2):**

| Field             | Type     | Required | Constraint                                                                                                               |
| ----------------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| `type`            | string   | yes      | `"matching"`                                                                                                             |
| `options`         | option[] | yes      | the fixed left items (**ids `l1`,`l2`…**) + the movable right items (**ids `r1`,`r2`…**), 2–6 of each, balanced          |
| `answerKey.pairs` | [l,r][]  | yes      | the correct left→right associations — must pair every left with every right **exactly once** (a bijection, Zod-enforced) |
| `explanation`     | string   | yes      | state each association and why                                                                                           |

Scoring is set equality of the pairs, all-or-nothing. Every right item must be a plausible
partner for more than one left item — otherwise the exercise solves itself.

**`multi` — native multi-select judgment (B3, "select ALL that apply"):**

| Field               | Type     | Required | Constraint                                                                                                                                      |
| ------------------- | -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`              | string   | yes      | `"multi"`                                                                                                                                       |
| `options`           | option[] | yes      | **3–6** candidates (checkboxes). Ids alphanumeric (`a`…, no `,`/`:`/spaces)                                                                     |
| `answerKey.correct` | string[] | yes      | **2–5** ids — the correct candidates. Must be a **proper subset**: at least one option must be wrong, or "select ALL" is vacuous (Zod-enforced) |
| `explanation`       | string   | yes      | justify EACH correct candidate and why the wrong one(s) don't qualify                                                                           |

Scoring is set equality of the checked ids, all-or-nothing (no partial credit). The client
renders the explicit **"select ALL that apply"** instruction — never omit it or the item
reads as an ordinary single-choice QCM and becomes unfair. Use `multi` for judgment items
where more than one option is legitimately correct (properties, classifications); a `multi`
item with exactly one intended correct answer should be an `mcq` instead.

Prefer these three native types (`ordering`/`matching`/`multi`) over the QCM-encoded
permutation/multi-select formats for new content.

**`short_answer` — native free-TEXT question (étude 20 lot 7, "question libre") :**

Aucune proposition n'est affichée : l'élève **tape** sa réponse dès la première rencontre. Le
serveur la corrige par un test d'appartenance déterministe à `{ canonique } ∪ acceptedAnswers`,
après normalisation (casse, espaces, accents, tashkeel, hamza, chiffres arabo-indiens).

| Field                              | Type     | Required | Constraint                                                                                                    |
| ---------------------------------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------- |
| `type`                             | string   | yes      | `"short_answer"`                                                                                              |
| `prompt`                           | string   | yes      | non-empty et **auto-suffisant** — aucune allusion à des propositions qui n'existent pas                        |
| `answerKey.text`                   | string   | yes      | la réponse canonique — 1–60 caractères, **≤ 6 mots**, une seule ligne, toujours acceptée sans être répétée     |
| `acceptedAnswers`                  | string[] | no       | les AUTRES formulations justes (voir ci-dessous) — ≤ 24 entrées                                                |
| `expectedMistakes[].text`          | string   | no       | une erreur qu'on SAIT fréquente, en toutes lettres — ≤ 6 entrées ; le pendant du distracteur tagué             |
| `expectedMistakes[].misconceptionTag` | string | no      | id du registre `content/misconceptions.json` (même vocabulaire fermé que les distracteurs `mcq`)              |
| `explanation`                      | string   | yes      | même barre que `mcq`, **mais elle ne doit pas contenir la réponse littérale** (l'indice la révélerait)         |
| `difficulty`                       | number   | no       | même sémantique que `mcq`                                                                                     |

**Les contraintes d'autorat sont BLOQUANTES** (`content:qa`, étude 20 R-12) — une `short_answer`
hors clous n'est pas « imparfaite », elle est **injouable** : l'élève ne peut pas taper la réponse.

- **charset tapable** : la réponse normalisée doit matcher `^[a-z0-9.ء-ي]+$` ;
- **pas de contenu riche** (`<svg`, `<img`, `![`, `$$`, `http`) ni de **symbole mathématique de
  structure** (`= < > ^ √ × ÷ ± ≤ ≥ ≠ ≈ → ∈ ∪ ∩`, exposants/indices Unicode) dans `answerKey.text` ;
- **un nombre pur ⇒ erreur** : c'est le type `numeric` qu'il faut (il a la tolérance et le pavé
  numérique). En maths, la question libre porte donc un **terme**, pas un résultat ;
- **énoncé auto-suffisant** : la liste close « lequel / parmi / suivant(e)s / ci-dessous / intrus /
  which of / following / below / مما يلي / من بين / أي من » est une **erreur** dans un `prompt`.
  ⚠️ Piège mesuré : en arabe, « أي » au sens de « c'est-à-dire » suivi de « من » (« …، أي من مجموع
  إلى جداء ») déclenche la garde. Reformuler (« فنحوّل مجموعًا إلى جداء ») — la garde ne lit pas le
  sens ;
- `expectedMistakes` : tag déclaré au registre, texte non vide une fois normalisé, jamais égal à la
  canonique ni à un autre.

**`acceptedAnswers` — le champ partagé (étude 20).** Il vit sur la `short_answer` (toujours actif)
et sur la `mcq` **éligible au mode Rappel** (`content:qa` avertit ailleurs, erreur sur les autres
types). On y écrit les formulations **également justes** : paraphrases, synonymes exacts, positions
équivalentes, translittérations latines de l'arabe (mono-mot par défaut).

- **R-4, la règle qui prime** : une entrée ne doit **jamais** égaler, une fois normalisée, un élément
  déclaré faux de la même question (distracteur `mcq`, `expectedMistakes` d'une `short_answer`).
  `content:qa` la rejette ; vérifier **avant** d'écrire — le gate est le filet, pas la méthode.
- **N'écrivez pas les variantes du Tier A.** L'article (`ال` en tête, `le/la/l'`, `the/a/an`) et les
  contractions anglaises sont dérivées **mécaniquement au build** de la canonique. Les écrire à la
  main est du bruit qui consomme la borne des 24. Corollaire : « المنوال » n'a pas besoin de
  « منوال », mais « المتطابقات الشهيرة » face à « متطابقة شهيرة » est une vraie variante.
- **Une variante n'est pas une variante orthographique.** La normalisation plie déjà la vocalisation,
  la casse, les espaces, `ة`/`ه`, `أإآ`/`ا`, `ى`/`ي` : « تحت الكرسيّ » et « تحت الكرسي » sont **le
  même mot** pour le moteur, et `content:qa` refuse le doublon.
- Le champ est **optionnel** : une réponse peut légitimement n'avoir aucune variante (R-13 vit dans
  la revue, pas dans le gate).

**Doctrine d'usage (étude 20 R-13/R-14).**

- **Née complète** : la question libre naît avec son ensemble accepté et, si le diagnostic a de la
  valeur, ses erreurs attendues taguées — pas dans une campagne de rattrapage ultérieure.
- **Où** : dans les **exercices** de tous les thèmes ; dans les quiz des thèmes **non scolaires**
  avec parcimonie ; **jamais dans un `quiz.json` du thème école** (il gate la progression du
  chapitre — on n'y met pas la forme la plus exigeante).
- **Combien** : la mission reste **mixte** — la saisie libre complète le QCM, elle ne le remplace
  pas (**≤ ~1/3** des questions d'une mission).
- **Ce qu'elle vise** : les questions dont la forme naturelle est la **production** (nommer une
  notion, un théorème, une méthode, une propriété) et que le QCM dégraderait en reconnaissance.
- **Pas de conversion** : on n'échange **jamais** un `mcq` existant contre une `short_answer` (é20
  Q-5). On **ajoute**.
- ⚠️ **Ajouter, c'est ajouter EN FIN DE TRI.** L'identifiant d'une question est un UUIDv5 de
  `subjectId/chapterSlug/exerciseSlug/qN`, où `N` est son rang **après tri par `difficulty`**.
  Insérer une question moins difficile que les autres **décale** les identifiants de toutes celles
  qui suivent : le compilateur supprime les anciennes lignes et en crée de nouvelles, emportant les
  tentatives, la télémétrie et les échéances de rappel espacé. Donner à la question ajoutée une
  `difficulty` **≥ au maximum du fichier** — et le vérifier.

### Figures (inline SVG) in questions

Any question field (`prompt`, an option's `text`, `explanation`) is a plain string, but it may embed
**one** `<svg>…</svg>` block to carry a figure (geometry diagrams, IQ matrices, shape sequences,
visual answer options). The renderer splits the field into its text and the SVG, sanitizes the SVG
(DOMPurify SVG profile — drawing primitives only), and shows the figure; surrounding text renders
normally. No schema/DB change is needed (it is just markup inside the string), and it round-trips
through the pipeline unchanged.

**The rendering contract (author to it):** the renderer always draws the figure on a **white "paper"
surface** (white background, dark default text colour), sized to a **definite width** the renderer
controls — ~256px max for a prompt, a ~64px box for an option — and scaled by the SVG's **`viewBox`**.
So: author every figure as if it sits **on white paper**, and let the `viewBox` (not width/height
attributes) drive the size.

Rules for authoring figures:

- **Self-contained SVG only.** Use a `viewBox`, and drawing primitives: `path`, `rect`, `circle`,
  `ellipse`, `line`, `polyline`, `polygon`, `g`, `text`, `tspan`, gradients/patterns. **Forbidden /
  stripped:** `<script>`, `<style>`, `<foreignObject>`, `<a>`, `<image>`, `<use>`, any `on*` handler,
  any `href`/`xlink:href`, external URLs. No raster images — vectors only.
- **Always set a `viewBox`** (e.g. `viewBox="0 0 100 100"`) and **do not rely on `width`/`height`
  attributes** for sizing — the renderer controls the on-screen size. A `viewBox`-less SVG has no
  aspect ratio and collapses.
- **Dark ink on the white paper for outlines.** Draw strokes/outlines with dark, opaque ink —
  `currentColor` (preferred: it inherits the dark default text colour), `#1f2937`, `#222`, `#0f172a`.
  **Never make the figure's primary marks white or near-white** (`#fff`, very light greys/pastels):
  on the white surface they are invisible.
- **Colour is encouraged — especially for young grades.** Fills survive sanitization and render in
  colour, so fill shapes with bright, saturated hues _inside_ their dark outlines (a green tree, an
  orange fish, a yellow sun, a red apple, a blue water drop). The only rule is **colour fills, dark
  outline** — keep a dark `stroke` so every shape stays legible on the white paper. For primary
  (≈ 1ère–3ème) prefer playful, recognizable, colourful illustrations over bare grey geometry; for
  abstract geometry (angles, axes, number lines, older maths) neutral dark ink is fine.
- **One `<svg>` per field.** A figure-only option is just its `<svg>` (no text needed); a stimulus is
  `prompt` text + one `<svg>`.
- Keep figures compact and legible (a `viewBox` around `0 0 100 100`–ish, explicit dark `stroke`/`fill`,
  readable when scaled to ~64px for options / ~256px max for prompts).
- The answer to a visual item must be **unambiguous and derivable from the figure alone**.

## quiz.json

| Field       | Type       | Required | Constraint                                                                                             |
| ----------- | ---------- | -------- | ------------------------------------------------------------------------------------------------------ |
| `title`     | string     | no       | if present, non-empty                                                                                  |
| `questions` | question[] | yes      | **3–10** (use 5). Difficulty skews 1–2 (comprehension check; gates exercises for school subjects only) |

Compiled to a `mode='quiz'`, `display_order=0` exercise with fixed rewards (20 XP / 5 coins) —
you do **not** author quiz rewards.

## exercices/\*.json

| Field          | Type       | Required | Constraint                                                                                                    |
| -------------- | ---------- | -------- | ------------------------------------------------------------------------------------------------------------- |
| `title`        | string     | yes      | non-empty (RPG-flavored, see style-guide.md)                                                                  |
| `difficulty`   | number     | yes      | integer **1–4** (1 easy · 2 medium · 3 boss · 4 élite; 3–4 are the dormant premium-gate ceiling per parcours) |
| `mode`         | enum       | yes      | `"practice"` \| `"boss"` \| `"challenge"` (never `"quiz"`)                                                    |
| `xpReward`     | number     | yes      | positive integer — use the canonical table (rewards-and-modes.md)                                             |
| `rewardCoins`  | number     | yes      | non-negative integer                                                                                          |
| `displayOrder` | number     | yes      | positive integer (match the filename `NN`)                                                                    |
| `questions`    | question[] | yes      | **1–50** (use 6)                                                                                              |

## Defaults you may omit

`gradeSlug` (→null), `isPremium` (→false), `chapter.sources` (→[]), `quiz.title`, question
`difficulty`. Everything else listed as required must be present.

## Course pattern fields (étude 35)

Two OPTIONAL fields, read by the gate only — never emitted in SQL, never read at runtime.

```jsonc
// <subject>/subject.json — the subject has finished its campaign and holds to the pattern.
// Posted at the LAST lot of that campaign, never before: it turns the pattern checks of
// `content:qa` from warnings into errors for this subject alone.
{ "coursePattern": "notion" }

// <subject>/<chapter>/chapter.json — the classic mistakes this chapter's COURSE corrects,
// named with the tags of content/misconceptions.json. `content:qa` refuses a tag unknown to
// the registry, and a tag no distractor of this chapter carries — the course would be
// fighting an error the exercises never measure.
{ "coursePitfalls": ["math.fn.image-calculee-par-somme"] }
```

And one block in `cours.md`, the ninth of the vocabulary — the only one whose body has two sides:

```markdown
::: verifie
The question: a completion example, or a twin problem.
---
The answer, folded by the reader, restating the reasoning — not just the result.
:::
```

The first `---` alone on its line splits it. Both sides must carry text, or the renderer shows
everything and `content:qa` errors. Never in `resume.md`. Full doctrine: `course-explanation.md`.
