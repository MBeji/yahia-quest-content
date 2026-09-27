# Quality bar — what makes content pass and what makes it good

Two layers gate content. Layer 1 (Zod) is a hard fail — invalid content never compiles. Layer 2
(`content:qa`) catches answer-key defects. Beyond both, there is a pedagogical bar that no tool can
enforce but that defines the product's value — hold yourself to it.

## Layer 1 — structural (Zod, always hard-fails, run via `content:check`)

- Quiz 3–10 questions; exercise 1–50 questions; options 2–6 per question.
- Option **ids unique**; `correctOption` must equal one of the option ids.
- Difficulty: question 1–3, exercise 1–4. `xpReward` > 0; `rewardCoins` ≥ 0; `displayOrder` > 0.
- Subject `id`/`themeId` kebab-case; `contentLanguage` ∈ {ar,fr,en}.

## Layer 2 — answer-key heuristics (`content:qa` / `content:qa:strict`)

`content:qa` is advisory (always exits 0). `content:qa:strict` exits 1 only on **errors**. There is
exactly one error-level check; the rest are warnings. Fix all errors; fix warnings unless there's a
real reason not to.

1. **[ERROR] Duplicate option texts** — two options with the same text (after folding Arabic-Indic
   digits and stripping whitespace). This is the only check that fails `--strict`. Every option must
   be textually distinct.
2. **[warn] Answer value not echoed** — for a _short, non-Arabic, numeric_ correct answer (≤24 chars),
   the number(s) must also appear in the explanation. Always restate the computed answer in the
   explanation.
3. **[warn] Thin explanation** — explanation `< 25` characters. Write explanations of at least a full
   sentence; aim well past 25 chars.
4. **[warn] Explanation contradicts the key** — the explanation names a _different_ option (a–f) as
   correct, or calls the _correct_ option wrong. Keep the explanation consistent with `correctOption`.
   (Exempt for "find the error / intruder / odd-one-out" prompts, where the correct answer is itself
   the wrong item.)

Note: there is **no** automated check for duplicate _questions_, banned content, answer-position
balance, or difficulty distribution — you own those by judgment (below).

## Layer 3 — the pedagogical bar (judgment; this is the real value)

- **Every distractor encodes a specific, named misconception** — a sign error, a confused rule, a
  classic trap. No filler/obviously-absurd options. The wrong answers should be tempting to a student
  who half-understands.
- **Explanations teach.** State the rule, apply it to this item (show the computation with a `✓`
  check on harder questions), and on boss/challenge items name the common trap ("الخطأ الشائع…" /
  "le piège courant…") explaining why the plausible wrong answer fails.
- **Difficulty ramps within an exercise** (start at 1, end near the exercise's tier ceiling) and the
  quiz skews easy (difficulty 1–2) since it only gates comprehension.

  ⚠️ **La rampe est ce qui tient une chaîne décomposée en place — ce n'est pas de la coquetterie.**
  Le compilateur émet les questions **triées par `difficulty`**, à égalité dans l'ordre d'écriture
  (`sql-builder` : `(a.q.difficulty ?? 2) - (b.q.difficulty ?? 2) || a.i - b.i`). Donc un exercice
  **décomposé** — une question par étape du raisonnement, chaque étape s'appuyant sur la précédente —
  est **silencieusement réordonné** dès que sa rampe redescend : une étape d2 écrite après une d3
  passe devant elle, et la chaîne que l'élève lit n'est plus celle qu'on a écrite. **Aucun gate ne
  le voit** : le contenu est valide, il se lit simplement de travers. Deux sorties, toutes deux
  bonnes : réordonner les questions pour que la rampe soit non décroissante dans l'ordre de lecture
  voulu (le départage stable la reproduit alors exactement), ou ouvrir la mission par les acquis
  faciles de toutes les chaînes avant les chaînes elles-mêmes. **Jamais** relever la difficulté
  d'une étape réellement facile pour la forcer à sa place : cela ment à la rampe et au palier.
  Mesuré le 2026-09-13 sur les missions « décomposer pédagogiquement » de math 9ème — deux fichiers
  sur trois avaient une rampe qui redescendait avant correction.
- **Age- and grade-appropriate presentation.** Beyond _being on syllabus_ (scope) and _being tagged at
  the right difficulty_ (ramp), every item must _read_ as written for the learner's developmental stage:
  vocabulary, sentence length, the real-world contexts/scenarios it leans on, the magnitude of the
  numbers, and the cognitive load (steps to hold in mind) all fit the audience. The audience is the
  **school grade** — primary `1ère…6ème année de base` ≈ 6–12 yo, collège `7ème…9ème` ≈ 12–15, secondary
  through `Bac` ≈ 15–18 — or, for non-school themes, the **declared level** (CEFR band for languages,
  the difficulty tier elsewhere). A 1ère/2ème-année prompt uses short sentences, small numbers, and
  concrete familiar contexts (animals, toys, the classroom, sharing sweets); a Bac or C1 prompt may be
  dense and abstract. Defects even when the notion is on-syllabus: vocabulary above the grade, adult or
  irrelevant scenarios for young children (taxes, mortgages, workplace), numbers/abstraction past the
  grade's range, a childish or condescending register for teens, or any mature/unsafe theme for the age.
- **Balance the answer key** — spread `correctOption` across a/b/c/d as a tidiness habit, but know it
  is cosmetic: the engine **shuffles option order at display** (per-attempt Fisher-Yates), so the key
  letter is never player-visible. The leak that survives shuffling is **content-based** — never let the
  correct option be recognisable as the longest, most-detailed, or only-one-with-a-justification answer
  (see "Homogeneous options" below). That is the rule that actually matters.
- **No duplicate or near-duplicate questions** within or across a chapter's exercises.
- **Respect the anti-rush floor**: an attempt under `4s × question count` earns nothing and doesn't
  satisfy the gate, so keep enough questions (quiz 5, exercise 6) that a genuine attempt clears it.
- **Factual accuracy**: verify non-trivial facts via web search and cite them in `chapter.json`
  `sources[]`. For the school program, fidelity to the official syllabus overrides everything
  (see content-ecole-tn).
- **Language purity**: write entirely in the subject's `contentLanguage`. The only non-content-language
  tokens allowed are math/LaTeX symbols, folder slugs, `mode` values, and source URLs.
- **Standard notation everywhere**: Western digits (0–9) and standard LTR equations/units in **all**
  languages — Arabic content never uses Arabic-Indic digits or arabized formulas. Hard rule; see
  `math-and-notation.md`.

## Question craft — what an irreproachable QCM item looks like

Beyond the distractor/explanation rules above, every item must pass these craft checks:

- **One stem, one task, one defensible answer.** The prompt asks exactly one thing and is
  self-contained (solvable without seeing the options first, for computation items). If two options
  could be argued correct, rewrite the item.
- **Clear, minimal cognitive load.** The stem reads cleanly on the first pass: as short as the task
  allows, one sentence where possible, no nested clauses or back-references that force re-reading, no
  irrelevant data that doesn't bear on the answer, no undefined symbol/abbreviation. The reader spends
  their effort on the _notion being tested_, not on decoding the wording. A prompt that is correct and
  on-syllabus but convoluted, padded, or ambiguous-until-you-see-the-options still fails this check —
  simplify the phrasing or split the task.
- **Linguistically well-formed and idiomatic.** Every prompt and option must read as natural,
  grammatically correct prose in the content language — read each one aloud; if a native speaker
  would stumble, rewrite it. In Arabic in particular: correct agreement, and **dual pronouns
  (`هما`, `بينهما`, `كلاهما`) only when there are exactly two referents** — never a dangling dual
  over an enumerated set of three or more. The question clause must parse unambiguously on first
  read, with a clear referent. ✗ `ثلاثة أعمدة … أيّها بينهما في الطول؟` (dual `هما` over three
  columns — incoherent) → ✓ `… أيّها ليس الأقصر ولا الأطول؟`. Avoid calque/translationese
  constructions (e.g. the bare `لا واحد` for "none" — write idiomatic `لا شيء` / `ولا واحد منها`,
  or better, a real distractor).
- **No meta-options.** Never options that reference the _other options_ — "all of the above",
  "none of the above" / "aucune de ces réponses" / "لا شيء ممّا سبق", "a and b", "I don't know".
  Four real, independent candidate answers. (A substantive "nothing / zero / none-of-the-world"
  answer — `لا شيء` meaning _nothing happens_, `0`, `aucun jour` — is a legitimate real answer, not
  a meta-option; the ban is only on options that defer to the answer list itself.)
- **Negative stems are rare and bolded.** Prefer positive phrasing; if you must ask "which is
  **not**…", bold/emphasize the negation so it cannot be skimmed past (and remember such prompts
  exempt the contradiction check — don't overuse them).
- **Homogeneous options.** Same grammatical form, same order of magnitude of length and detail.
  The correct answer must not be recognizable as the longest, most precise, or most hedged option.
- **Deterministic option order.** Sort numeric options ascending (or descending — consistently);
  order text options logically (chronological, alphabetical, or by length). Randomizing the _key_
  is the engine's job via your key balance — the _display_ order should look deliberate.
- **No option leaks.** An option must not be contradicted or confirmed by the wording of the stem
  or of another option; distractors must not overlap (two options that mean the same thing).
- **No form clue — the key must not be findable without the notion.** Length is only the first
  leak (`content:tranche`, blocking in the Content CI since 2026-09-23). The six others below were
  each found by an independent audit of `arabic-8eme` (corpus #531 → #555, 877 questions), and
  none of them is caught by a gate:
  1. **A marker present in the key and absent from the distractors** — a term (« بدل مطابق »,
     « في محلّ »), an ellipsis « … », quotation marks, « الخطأ إغفال » — or **the only fully
     vocalised option** (the vocalised one is then the odd one out). Whatever the key carries,
     at least one distractor carries too.
  2. **A key that is the union of the distractors** — « أشدُّ حُمرةً » when one distractor says
     « أشدُّ » and another « حُمرةً » : the student picks the option that shares the most with the
     others. Build distractors that are wrong on _one_ axis each, not halves of the key.
  3. **A distractor contradicted by what the student sees** — « مبتدأ مرفوع » on a word ending in
     a fatha, « مضاف » on a word with tanwīn, « مزيد » for « ماتَ », or an option that denies a
     premise the stem states (« دونَ مساعدٍ » when the stem says the auxiliary verb is there). It
     is eliminated on sight and tests nothing. Make it wrong about the function, consistent with
     the visible case and with the stem.
  4. **A notion not yet taught** — in a distractor, a key or an explanation. The order is the
     chapter order of the subject (folder prefixes) plus the previous grades. « حال » as a
     distractor in chapter 21 when الحال is chapter 23: the student can neither choose it
     knowingly nor rule it out.
  5. **A compound stem the key only half answers** — « ما الإعراب الكامل » / « ما نوعه وما
     علّته » with a key reduced to one half, or a key that is the only option giving a cause.
     Either the key keeps both parts and every distractor has the same structure, or the stem
     asks for one thing.
  6. **A key true only if read generously** — « الخطأ أنّ «كاد» للمقاربة » says the error IS the
     rule. Read every key the way a student takes it: literally. (« الخطأ إغفال أنّ… »)
- **Explanations name options by their text, never by their letter.** Options are shuffled on
  every surface: « الخطأ الشائع (b) », « la réponse d », « الأولى / الثالثة » point the student at a
  random option in the one place meant to correct them. `content:qa` warns on letters since
  2026-09-27 (`qa-option-refs.ts`); ordinals (« الأولى ») are yours to catch.
- **No mirror question, no de facto duplicate.** Two items of the same exercise with the same
  options and inverted keys (« حوّل إلى ما أفعلَه » / « … إلى أفعِلْ بـه » on the same sentence)
  hand each other their answer. Two items with the same four options and the same key under
  two stems are one question asked twice. `content:tranche` lists near pairs; reading them is
  the auditor's job (method B3), rewriting one of each pair is the author's.
- **Difficulty tag is honest.** A d1 question is answerable by a student who just read the course;
  a d3 question requires combining ≥2 notions or a multi-step computation. Don't tag for ordering
  convenience.
- **Illustrate what the question is ABOUT — a spatial/visual item without a figure is a defect.**
  This is the question-side of `course-quality.md` Axis 5. If the item is about a **shape, an angle,
  a triangle, a circle, a solid, a coordinate/vector plane, a graph to read, a scientific diagram, a
  figure/table to interpret**, it carries an inline `<svg>` — reading the figure is the skill, and
  the words-only version forces the pupil to build the picture in their head before they can even
  start. Full doctrine (families, drawing rules, per-cycle vertex naming, colour for young grades):
  **`course-figures.md`** (one shared doctrine for courses and questions). Three hard rules:
  - **Only where it SERVES (never decoration).** A pure computation — «calculer lim x→2 (3x²−5)»,
    «3/4 + 1/2» — gets **no** figure: a graph there is noise, or it hands over the answer (the
    horizontal asymptote _is_ the limit). Illustrate the _visual_ items, not every item.
  - **The figure must be TRUE.** Points announced on a segment are on it, parallels are parallel, a
    right angle is 90°, a plotted curve passes through the stated values. A figure that contradicts
    its statement makes a correct question **unanswerable** — worse than no figure. Re-derive the
    coordinates; double-solve the item _on the figure_.
  - **The figure must not LEAK the key.** A question figure shows the _scene_, never the answer: no
    answer-word label, no marked correct option. A figure may live in the **options** (visual QCM:
    "which piece completes the pattern?") — then all four options carry a comparable figure, none
    marked. And for a "how many solutions" item, draw the _forced_ crossings, not one that quietly
    argues for the wrong count (a single crossing under a "unique solution is false" stem is a trap).
  - **Young grades (≈ 1ère–3ème, 6–8 ans) — illustrate almost everything**, colourfully and
    concretely (a bird above a tree, a ball in a box), because a 6-year-old barely reads. This is the
    HIGHEST illustration priority in the catalogue, not the lowest.

## Self-verification protocol — run it BEFORE `content:check`/`content:qa`

The automated layers catch structure, not correctness. Before running the checks, do a **blind
verification pass** over every file you wrote:

1. **Re-solve every question yourself, without looking at `correctOption`**, then compare. Any
   mismatch = fix the item (don't just flip the key — understand which was wrong).
2. **Re-read each explanation against the key**: it must assert the keyed option and only that one,
   restate the computed value (numeric answers), and not accidentally validate a distractor.
3. **Tally the answer key** across each exercise and across the chapter: no letter > ~40% of items,
   every letter used at least once per exercise where possible.
4. **Scan for duplicates / near-duplicates** (same fact or computation re-asked with cosmetic
   changes) within and across the chapter's exercises and quiz.
5. **Scan notation**: zero Arabic-Indic digits, true minus `−` in formulas, standard units, and —
   in `ar` content — **no plain space inside grouped numbers** (`\d \d{3}` outside `<svg>` must be
   zero; use U+00A0, else the bidi algorithm swaps the groups at render time — see
   `math-and-notation.md`).
6. **Check the ramp**: per-question difficulty is non-decreasing within each exercise and matches
   the exercise tier; the quiz stays at d1–2.
7. **Figure sweep** (§ Question craft, "Illustrate what the question is about"): list every item
   whose notion is spatial/visual (shape, angle, solid, repère/vecteur, graph-reading, diagram,
   figure/table to interpret) — each must carry an `<svg>`, or you note why a figure would not
   serve. For every figure present, **double-solve the item on the figure** (it must be TRUE and
   must not leak the key). For a young-grade (1ère–3ème) file, expect a figure on nearly every item.

Only after this pass run `content:check` and `content:qa:strict`. To audit _existing_ content with
the same rigor, use the **`content-audit`** skill.

## Non-academic content — every correction is a mini-lesson

For **non-school programs** (culture-générale, muscle-cerveau, language tracks), the explanation is a
**mini-lesson, not a verdict**. Whether the student answered right or wrong, the correction must leave
them knowing more than before:

- State the correct answer and **why** it is correct.
- **Add 1–2 extra facts / context** around it — for culture-générale a date, a cause, a related
  figure, a "le savais-tu ?"; for languages the rule plus a clean example; for brain-training the
  method and why it works.
- Briefly say why the tempting wrong option is wrong (the misconception), so a wrong answer still teaches.

The goal: even a missed question grows the user's general culture and is memorable. Keep it concise
(2–4 sentences), accurate (verify facts via web, cite in `chapter.json` `sources[]`), and never
contradict the key. This is on top of the ≥25-char / no-duplicate-options rules above.
