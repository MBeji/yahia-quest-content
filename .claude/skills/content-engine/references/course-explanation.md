# Course explanation — the notion pattern, and why a lesson explains instead of stating

> **Scope.** This file governs **how a notion is explained** inside `cours.md`: the order in which
> its parts arrive, what each one must carry, and what must never happen. It is the normative
> reference for **axis 2 — Facilité de compréhension** of `course-quality.md`, the same way
> `course-figures.md` is the reference for axis 5. The lesson's skeleton and voice stay in
> `style-guide.md`; notation stays in `math-and-notation.md`; the visual rules stay in
> `course-figures.md`. Do not duplicate them — point here for the ORDER, there for the rest.
>
> **Why this file exists.** Measured on `main`, 2026-09-16, before writing a line of it: the block
> apparatus delivered by étude 18 serves figures and nothing else. Across the 20 courses of maths
> 9ème — the national-exam year — there are **54 `::: figure`, 1 `::: methode`, and zero
> `definition`, `propriete`, `exemple` or `retenir`**. The corpus-wide count was the same shape:
> 362 figures against 26 knowledge blocks (étude 21 §8). And `course-quality.md` axis 2 already
> said « concrete before abstract » and « every rule has a worked example » — in two lines, with
> no pattern, no gate and no measurement behind them. So the courses state. The course on linear
> functions opens on the formal definition and puts its one concrete situation — a taxi fare — at
> line 121 of 138, after every rule, labelled « exemple d'application ». The order is the exact
> reverse of what the bar prescribes, and nothing anywhere noticed.
>
> Étude: `FableEtudes/EtudeRealisé/35-comprendre-la-theorie/ETUDE.md` — it carries the evidence base (annexe A,
> with its verification caveat), the measured state (annexe B) and the arbitrations.

---

## 1. The pattern — seven times, one order

A **notion** is what the programme names and the quiz tests: a definition, a property or theorem,
a method, a formula. **One `##` section = one notion** (axis 1, unchanged). Inside it, the order
is closed:

| #      | the student…                                                                      | how it is written                                                                        |
| ------ | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **T1** | **is anchored** — a situation they know, and **the question** it raises           | prose, 2–4 lines, ending on the question; an anchoring figure if the situation is visual |
| **T2** | **is given the name** — the official word, the notation, alone on its line        | `::: definition` (or `::: propriete` when the notion is a statement)                     |
| **T3** | **sees it** — a representation, and the sentence tying it to the symbols          | `::: figure` (mandatory if spatial), a value table, a number line, a tape diagram        |
| **T4** | **watches it solved** — step by step, **each step with its why**                  | `::: exemple` — 2 to 5 numbered steps; the FIRST example reuses T1's numbers             |
| **T5** | **tells it apart** — the classic mistake, shown, diagnosed, corrected             | `::: piege` or a promoted `> ⚠️` — the wrong step, why it tempts, the right step         |
| **T6** | **generalises** — the rule, after the example, with what varies and what does not | `::: propriete` / `::: methode` + 2–3 short cases including **one edge case**            |
| **T7** | **checks, on the spot** — before moving on                                        | `::: verifie` — a completion example or a twin problem; the answer is **folded**         |
| end    | **keeps one line**                                                                | `::: retenir` — mirrored by the summary card                                             |

Not every notion needs every time; **the order, however, is never negotiable.**

| notion type        | required                                      | recommended | forbidden                                                        |
| ------------------ | --------------------------------------------- | ----------- | ---------------------------------------------------------------- |
| definition         | T1 · T2 · T4 · T7 · retenir                   | T3 · T5     | T2 before T1 — a definition never opens a section                |
| property / theorem | T1 · T3 (if spatial) · T4 · T6 · T7 · retenir | T5          | T6 before T4 — the general rule never precedes its example       |
| method / procedure | T1 · T4 · T6 (`methode`) · T7 · retenir       | T5          | a "figure it out first" opening — a procedure is explained first |
| formula            | T1 · T2 · T4 · T7                             | T3 · T5     | a formula inside the sentence (one formula, one line)            |

**Why this order and no other.** It is the order of the official manual — **نشاط** (activity) →
**encadré** (the boxed rule) → **أطبق** (apply) → **تمرين مرفق بحل** (solved exercise) → **أحوصل**
(wrap-up) — which the app's courses skip: they start at the encadré. And it is the order the
meta-analyses support for **novices** on a new notion, which a 9ème pupil is on every notion they
meet, exam year or not. The pattern keeps the manual's sequence and adds what the evidence adds:
the worked example before the general rule, and the classic mistake contrasted after it.

---

## 1bis. The pattern outside mathematics — grammar, rhetoric, life sciences

Added 2026-09-17, generalising the pattern to the other **9ème concours** subjects (`arabic`,
`french`, `sciences-vie-terre`). The seven times describe **how a novice meets a notion**, not how
a number is computed. Nothing in §1 is discipline-specific except the illustrations. What changes
from one subject to the next is **what fills T3 and T4** — « sees it » and « watches it solved » —
and that is exactly what this section fixes, so that no one has to guess it chapter by chapter.

**The rule that governs the whole section**: a « worked example » is a **reasoning carried out in
front of the student, step by step, each step with its why**. In maths that reasoning is a
computation. It is no less a reasoning when it is an إعراب, a transformation of a sentence, or the
reading of a seismogram — and a lesson that states the rule and stops has taught nothing in any of
the three.

### النحو والبلاغة (`arabic`) — the official guide already prescribes the pattern

The CNP teacher guide (`501902P00`, 18 دروس) states its own method, and it is ours:
**نصّ انطلاق → ملاحظة → قاعدة → خلاصة → إنجاز** — a starting text, observation, the rule, the
wrap-up, production. It is inductive by design: the rule is **read off** an example, never posed
first. Writing to the pattern here is not importing a foreign method, it is finally applying the
guide's own.

| time | what fills it in نحو                                                                                                                                                                            |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| T1   | the **نصّ انطلاق**: one short sentence — ideally the guide's — where the point is visible. The strongest anchor is a **vowel that changes the meaning** (`ما أجملَ` vs `ما أجملُ`)              |
| T2   | `::: definition` — the official term (معرب، مبني، نائب الفاعل), alone on its line                                                                                                               |
| T3   | a **contrast table**: the SAME word in three positions, its ending changing. That table is what a figure is in geometry — no `::: figure`, and the gate no longer asks one of a grammar chapter |
| T4   | `::: exemple` — a **full إعراب**, word by word, each with its **لأنّ**. Never « إعراب: مرفوع » with no reason                                                                                   |
| T5   | `::: piege` — the confusion the quiz's distractors actually encode: الفعل الماضي marked معرب, الجرّ applied to a فعل                                                                            |
| T6   | `::: propriete` — the قاعدة, with its **exception** (the الأسماء الخمسة, the ممنوع من الصرف)                                                                                                    |
| T7   | `::: verifie` — **أعرب** this word, or vowel this ending. The answer folded, and it restates each لأنّ                                                                                          |

⚠️ **R-14's French gloss does NOT apply to `arabic`.** The gloss exists because Tunisian maths
switches to French at lycée, so the pupil who learns الوتر meets _hypoténuse_ a year later. Arabic
grammar is taught in Arabic at lycée too: there is no later French term to hand over, and glossing
المبتدأ or المنصوبات would invent a pairing the pupil will never need. The terms stay Arabic, alone.

### Le français (`french`) — the notion is a transformation

Same shape, one difference: a French grammar notion is almost always an **operation on a sentence**
(active → passive, direct → indirect, tense agreement). The example is therefore the transformation
**carried out**, not its result exhibited.

- **T1** — a sentence the pupil would really write, and the question it raises. The best anchors are
  the ones where the naive answer is wrong: « Il m'a dit qu'il **viendra** » — why does it have to
  be _viendrait_ ?
- **T3** — the **before / after table**, with the moving parts in bold: what the pronoun becomes,
  what the tense becomes, what the time marker becomes. The transformation has to be **seen**.
- **T4** — the transformation in 3–5 steps, each with its why, on ONE sentence carried through.
- **T5** — the interference mistake, which in Tunisia is often a **calque from Arabic or from the
  spoken language**, not an ignorance of the rule. Name it as such.
- ⚠️ **No figure is required, and none should be invented.** The gate stopped asking (it used to,
  wrongly: `01-types-et-formes-de-phrases` was flagged on the word « forme »). A drawing of a
  subordinate clause teaches nothing; the contrast table is this discipline's T3.
- R-14's Arabic gloss does **not** apply here — the subject is written in French throughout.

### علوم الحياة والأرض (`sciences-vie-terre`) — the schema IS the notion

The closest of the three to maths, and the one where T3 carries the most weight.

- **T1** — an **observable** the pupil has met: the ground shakes, a wound heals, a child has their
  grandfather's eyes. The question comes from the observation, never from the vocabulary.
- **T3 — `::: figure`, and it is not optional.** A mechanism, a cycle, a section: a fault that
  slips, a magma chamber, a genetic cross, a cell recognising another. **The notion lives in the
  drawing and the prose annotates it** — the reverse of a maths chapter, where the figure
  illustrates a statement that already stands alone. The gate now knows this family (`SCHEMA`) and
  asks for the figure; before 2026-09-17 it said nothing at all about these seven chapters.
- **T4** — « watched solved » is a **reasoning chain on a real case**: read this seismogram and
  locate the epicentre, do this cross and count the offspring, follow this antigen. Genetics is
  literally computational (an échiquier de croisement is an example with steps); seismology and
  tectonics are chains of inference.
- **T5** — the classic confusions are famous and worth naming: magnitude confused with intensity,
  « la plaque flotte » for « elle coulisse », dominance read as « the stronger trait wins ».
- **T6** — the mechanism stated in general, plus the case that bends it.
- ⚠️ **The manual EXISTS — the fiche does not, and those are two different things.** Corrected
  2026-09-17, same day, after an owner's push-back. The first version of this line read « no
  official source, so anchors come from the observable world, as R-2 allows when there is no
  activity to harvest ». That was **false in its conclusion**: `105905P00` (« علوم الحياة
  والأرض », 208 p., 7,3 MB) is catalogued in the CNP corpus and downloads from
  `www.cnp.com.tn/arabic/PDF/` — which is on the cloud allowlist. What is missing is its
  **transcription fiche**, a task, not an absence. Anchors come from the manual's أنشطة, as
  everywhere else.
- ⚠️ **A cloud session cannot read the PDF off disk**: `cnp-officiel/` is a 2.8 GB sibling of the
  repo, deliberately out of git, and lives only on the workstation. It must be **fetched over
  HTTPS**, and the CNP serves its leaf certificate alone — so the download fails on an
  incomplete chain until the vendored intermediate is in the store. The engine ships the fix:
  `node -e "import('./scripts/cloud/ca-bundle.mjs').then(m => m.buildCaBundle())"` writes a
  combined bundle, then `CURL_CA_BUNDLE=<that file> curl -L <url>`. Without it the failure looks
  like « the book does not exist », and that is exactly the wrong conclusion to draw.

---

## 2. The rules, one by one

### R-1 — One section, one notion, the seven times in order

Required times depend on the notion type (table above). The order depends on nothing.

### R-2 — The anchor is a question, not scenery

T1 states a situation **and the question** the notion will answer (« how much do we pay for x
kilos? »). An anchor that leads to no question is decoration, and decoration inside an explanation
measurably **costs** comprehension (seductive details, annexe A). Where the anchor comes from, in
order of preference:

1. **the manual's own activity** — the « نشاط » of that chapter in
   `content/programmes-officiels/programme/<grade>/<matière>.md`, **rewritten, never copied**
   (`content:qa` runs an anti-verbatim guard over lessons);
2. the pupil's Tunisian everyday — prices, distances, shadows, bills, marks, a football pitch;
3. a prior notion they have already mastered (« you already know how to… »).

### R-3 — The same numbers run through T1 → T3 → T4

Concreteness fades along ONE story: the tomatoes of T1 become the value table of T3 and the worked
example of T4, before T6 writes `f(x) = ax`. **Two examples per rule minimum**: one **dressed** (the
situation) then one **bare** (pure maths). Never the reverse — the bare one first teaches nothing.

### R-4 — Every step of an example carries its why

Half a line, as a **principle label** (« because the image is the price matching the quantity »),
never a paragraph. And never an open prompt without its answer: self-explanation prompts added to
an already explicit maths worked example **reduce** its effect (annexe A). The course answers its
own « why »; the `::: verifie` is where the pupil produces something.

### R-5 — The classic mistake comes after a correct example, never before

It is **named as a mistake in its first line**, shows the wrong step, says **why it tempts**, then
the right step. It targets a misconception from the registry — the same vocabulary the chapter's
distractors use — and the chapter declares it in `chapter.json` → `coursePitfalls`. An uncorrected
mistake in the text, or one repeated in the summary, is a **[BLOCKER]**.

### R-6 — The general rule arrives after its example, with an edge case

`b = 0`, `a < 0`, the zero denominator, the equality case: what the programme tests, the course has
shown (axis 3).

### R-7 — One method at first contact

Two methods are presented **one after the other**, never side by side in the section that
introduces the first: for a pupil who holds neither, comparison is **worse** than sequential study
(annexe A). Comparison belongs in a later synthesis section, once both are owned.

### R-8 — The check is a completion example or a twin problem

Never a new notion. Its answer **restates the reasoning** (the step and its why), not just the
result — feedback is what turns a check into learning. One per theory section, two at most. For a
procedure, the blank step is **the one carrying the principle**, not mechanically the last.

### R-9 — « À retenir » is one line

It becomes the summary card (bijection, axis 3).

### R-10 — The register of a course, not of a trailer

RPG lives in the `#` title, the `> 💡` epigraph and the closing `> 🏆` (style-guide). **Nothing
narrative or decorative inside T2–T7.** A sentence that repeats what the figure shows is deleted.

### R-11 — A representation is tied to the symbols, or it is wallpaper

Any figure, table or number line in T3 is followed by **one bridging sentence** naming the
correspondence (« the slope of the line is the `a` of the formula » / « القطعة AB في الشكل هي a في
الصيغة »). Labels live **inside** the figure, next to their element, never in a separate legend; an
object bears **the same name** in the text, the figure and the formula. This is the single most
neglected practice in international video studies of maths teaching (annexe A).

### R-12 — One new notion per section; a block is 3 to 6 lines

Numbered steps excepted. A section over 60 lines splits.

### R-13 — Budget per notion, and the split trigger is the notion COUNT

A theory section runs **18 to 40 lines**. A course's length is that budget times its number of
notions — nothing else. Five notions ≈ 90–200 lines; ten notions ≈ 180–400. **Both are
conformant**; measure the section, never the file.

This **replaces** the « ~50–75 lines » of the style guide, which never described the corpus — a
dead rule is not a rule. It also **replaces this rule's own first draft**, which derived « 110 to
240 » for a six-notion course and then read that 240 back as an absolute ceiling. Measured on
maths 9ème once lots 2–4 were written: **8 of the 10 chapters at the pattern pass 240**, the
reference mock-up `06-fonctions` (273) among them, while 5 of 10 sit inside the 18–40 band with a
median of 43. The long ones are long because they carry **more notions** — `03-calcul-litteral`
is 10 notions at 39 lines each — not because their notions swell. A rule its own reference
implementation breaks is the dead rule again, one generation later.

**What triggers a split is the notion count, not the line count.** Past about **8 notions** in one
chapter, it goes up as a **curriculum** question — « is this two chapters? » — with the notion
count as the evidence. A human decides; never a silent truncation, and never a verdict read off
`wc -l`. Open candidates on maths 9ème: `03-calcul-litteral` (10), `15-numeration-et-calcul` (10 —
its own text says « هذا الفصل بابان اثنان »), `07-statistiques` (14 sections, before rewrite).

Count prose, not figures: a `<svg>` is one figure however many lines it spans. Neutralising them
moves only three chapters on maths 9ème (`18` 331→177, `08` 185→125, `07` 261→211), all of them
still outside the pattern — but the measure has to be honest before it can arbitrate.

A section **above** the band is the real signal, and the gate already carries it: C-6 refuses a
section past 60 lines, because there it holds two notions. `resume.md` stays at ~7–10 bullets,
one per section.

### R-14 — Official vocabulary, standard notation, RTL

The manual's terms (its « Vocabulaire & terminologie officielle » table), Western digits, LTR
formulas alone on their line, U+00A0 inside grouped Arabic numbers, decimal comma. All of
`math-and-notation.md` applies; nothing here softens it.

**French gloss on first use — and it is a rule, not a tolerance.** Tunisian maths switches to
**French** at lycée: the student who learns الوتر in 9ème meets _hypoténuse_ a year later. So the
first time a key term appears in a chapter, it carries its French equivalent in parentheses —
`**الوتر** (hypoténuse)` — and never again after that. This is not a language mix: the sentence
stays Arabic, the gloss is a label. Rules:

- **Key terms only** — what a definition or a property names: the objects (شعاع → vecteur), the
  operations (التعميل → factorisation), the named theorems (نظرية طاليس → théorème de Thalès).
  Not ordinary words, not emphasis, not a whole phrase.
- **First occurrence in the chapter, once.** A second gloss is noise; the student has the pairing.
- **Never inside `$$…$$`, a table cell, or a figure caption** — the parenthesis breaks the LTR run
  in RTL, and a caption has no room for it.
- **The Arabic term still leads.** The gloss follows it; it never replaces it, and it never opens
  a sentence.

Arbitré par le propriétaire le 2026-09-16 : « tu peux laisser du français si déjà le terme arabe
existe, car en lycée on bascule en français. » Ce qui reste interdit est ce que cette règle n'est
pas : une **phrase** à moitié française au milieu d'une proposition arabe (« ثلاث نسب égales, pas
deux ») — elle casse le sens de lecture et n'est pas un terme.

⚙️ **Et depuis le 2026-09-17, une machine tient cette moitié-là : le contrôle C-7** du gate
(`content:qa`). Il a été écrit parce que la règle avait fui **trois fois** dans la seule campagne
pilote, dont deux après une purge à la main — une règle qu'aucune machine ne tient revient. Ce
qu'il fait : sur une leçon dont le document est arabe, un mot en lettres latines hors d'une
parenthèse, d'un `` ` ``, d'un `$$…$$` ou d'un groupe `[…]` est un constat. Il lit le **script**
des caractères, jamais le sens : il ne sait pas le français de l'anglais, ni une bonne phrase
d'une mauvaise. Il se tait sur la glose entre parenthèses (c'est la règle), sur les points et
théorèmes à majuscule (`ABCD`, `Thalès`), sur les symboles d'unités et les noms de fonctions
(`min`, `dam`, `cos`), et sur une leçon française qui cite un nom arabe. Deux régimes comme les
six autres : `warn` sans `coursePattern`, `error` avec. Mesuré au 2026-09-17 sur les
1 546 fichiers du corpus : **zéro constat** — la règle est tenue, et elle le restera.

⚠️ **Un mot français SEUL compte.** Le premier prototype exigeait deux mots latins consécutifs et
laissait donc passer « ثلاثة عدّات différentes », qui est pourtant exactement la faute. Un
adjectif accroché à une proposition arabe est une phrase à moitié française, pas une étiquette.

### R-15 — What is off-programme stays out

The pattern never adds a notion; it explains the ones that are there (axis 3).

---

## 3. The `::: verifie` block — grammar and traps

```markdown
::: verifie أو un titre libre
La question : un exemple à compléter, ou un problème jumeau.

---

La réponse, qui REDIT le raisonnement : l'étape et son pourquoi.
:::
```

- The **first** `---` alone on its line splits the block. Later ones stay ordinary markdown inside
  the answer.
- **Both sides must carry text.** No separator, or an empty side, and the renderer degrades to a
  plain block — the answer then shows under the question and the check checks nothing.
  `content:qa` errors on it (C-4).
- The answer is folded in a native `<details>`; the reveal label follows the **content language**.
  Printing from the reader unfolds every answer, so a printed course stays complete.
- **Never in `resume.md`.** Revision cards answer, they do not ask (`content:qa` errors).
- The block is authorable as of étude 35 lot 1 (engine). A course written before it renders the
  block as plain text — write it anyway; it is the shape that matters.

> ⚠️ **The Prettier trap — it has cost two cycles (é35 lots 2 and 4).** Prettier reads a closing
> `:::` that follows a list item, or a line indented under one, as a **lazy continuation** of that
> list, and re-indents it to `  :::`. The directive is then never closed, and `content:qa` errors
> on the whole file (46 errors in one pass on lot 4). Applies to a fence after a numbered step, a
> bullet, or a `$$…$$` line indented under a step — precisely the shape every `::: exemple` has.
> **Remedy, and it is the only one that survives a re-run**: leave a **blank line** before the
> closing `:::` whenever the line above it is a list item or is indented. Prettier never indents a
> fence preceded by a blank line. Run `npx prettier --write` on your own files **before** the
> gate, never after it goes green — the format pass is what breaks it, and a green gate on an
> unformatted file proves nothing about what lands in the PR. Same family of trap as the one that
> mangled the Arabic gabarit of the étude: Prettier does not know this vocabulary, so the author
> writes so that reformatting is a no-op.
>
> **Second face of the same trap (é35 lot 7)**: Prettier also **rewrites inside an `<svg>`** — it
> inserted a blank line after the opening tag of the figure in `06-fonctions`. Harmless in SVG
> (whitespace is insignificant there, and `content:figures:check` stays green), but it breaks the
> « byte for byte » invariant the campaign claims for figures. Two consequences: run
> `prettier --check` on a chapter **before** touching it — a file that already fails on `main`
> carries a latent rewrite that your commit will absorb and appear to own; and when you assert that
> figures survived untouched, **verify it**, by extracting the `<svg>` blocks before and after and
> comparing them, not by trusting that you did not edit them.

---

## 4. What the gate enforces, and what it cannot

`content:qa` carries **six structural checks**. They count blocks and lines; they never sniff prose
(a « concrete » opening cannot be detected by regex in three languages, and a wrong guess is worse
than none). Two regimes: `warn` until the subject declares `coursePattern: "notion"` in its
`subject.json` — that is its backlog — then `error` — that is its gate.

| check   | what it refuses                                                                                                                          |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **C-1** | a section posing a rule (`definition`/`propriete`/`methode`) with no `::: exemple`                                                       |
| **C-2** | a section opening straight on its rule — no 2 lines of prose, no anchoring figure                                                        |
| **C-3** | a section showing an example with no `::: verifie`                                                                                       |
| **C-4** | a `::: verifie` without its separator, or with an empty side; a `::: verifie` in a summary                                               |
| **C-5** | a course naming no classic mistake at all; a `coursePitfalls` tag unknown to the registry **or carried by no distractor of the chapter** |
| **C-6** | a section over 60 lines (warn in both regimes — a length is not a fault)                                                                 |

Under `coursePattern`, one more: a course carrying **no knowledge block and no worked example**
fails outright — the flag is a way of writing, not a badge.

**What no gate can catch**, and what `content-audit` therefore grades (axis 2 grid): whether the
anchor is really concrete, whether the « why » of each step says something, whether the mistake is
the one pupils actually make, whether the check is a twin and not a new notion, and whether every
example, mistake and check is **true** — which is why the audit re-solves them blind.

---

## 5. Anti-patterns — what a lesson written to the pattern never does

| anti-pattern                                                     | why it fails                                                                   |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Opening on « **Définition.** A linear function is… »             | The pupil receives a name for something they have not met. T1 exists for this. |
| An « exemple d'application » at the end of the section           | The example is not a reward for having understood; it is HOW one understands.  |
| « f(2) = 6 » with no why                                         | A computation is not an explanation. Each step names the principle it applies. |
| « Explique pourquoi cette étape est permise. » with no answer    | An open prompt without feedback degrades the example's effect (annexe A).      |
| A dragon computing square roots                                  | Decoration inside the explanation measurably costs comprehension.              |
| Two methods side by side on first contact                        | Worse than sequential study for a pupil holding neither.                       |
| « Voir la figure ci-dessus »                                     | The figure sits beside its step, and its labels are inside it (R-11).          |
| A check whose answer is just « 28 »                              | The answer restates the reasoning, or the check teaches nothing.               |
| A mistake shown and left uncorrected, or repeated in the summary | The lesson would teach the error. `[BLOCKER]`.                                 |
| A 300-line course « because the notion is rich »                 | Past 240 lines the chapter splits — a human decision, written down.            |

---

## 6. Self-check before running the gate

Per section, in order:

1. Does it open on a **situation and its question**, not on the rule?
2. Does the **same story** run from the anchor to the worked example?
3. Does **every step** of the example carry its why, in half a line?
4. Is there a **classic mistake**, after a correct example, named, diagnosed, corrected — and is
   its tag in `coursePitfalls`, carried by a real distractor of this chapter?
5. Is the general rule **after** its example, with an edge case?
6. Is there **one `::: verifie`**, its answer folded, restating the reasoning?
7. Is there **one `::: retenir`** line, mirrored by a summary card?
8. Are every example, mistake and check **re-derived and true**? (No gate can do this.)
9. Notation scans (`math-and-notation.md`), figure rules (`course-figures.md`), length (R-13).

Then `npm run content:check` and `npm run content:qa` from the engine, and read the warnings of
your own subject before declaring the work done.
