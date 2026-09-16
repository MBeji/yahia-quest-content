# Course & summary quality — the bar for `cours.md` and `resume.md`

The questions have their bar (`quality-bar.md`); this is the equivalent for the **lesson text**.
A chapter's course is what the student reads _before_ being tested — if it is unclear, incomplete,
or unteachable, every downstream question becomes unfair. Both the authoring skill
(`content-cours`) and the audit skill (`content-audit`) grade against the **five** axes below.
`style-guide.md` gives the skeleton/voice; this file defines **what makes the content good**.
A lesson is not only a text: axis 5 (**Illustration**) is as binding as the other four — see
`course-figures.md` for the doctrine, the families that require a figure, and the SVG templates.
And axis 2 is not a preference either: it is the **notion pattern**, specified in
`course-explanation.md` — the order in which a notion arrives, and what each part must carry.

## Axis 1 — Clarté (clarity)

- **One notion per section.** Each `##` section introduces exactly one new concept. If a section
  teaches two rules, split it.
- **Define before use.** Every technical term is defined in the content language at first
  occurrence, using the **official program's terminology** for that grade (never a synonym the
  textbook doesn't use).
- **Short sentences, active voice.** Target ≤ 20 words per sentence in explanatory prose;
  one idea per sentence. Vocabulary calibrated to the grade (a 6ème course reads simpler than Bac).
- **Formulas isolated.** Display formulas on their own line (`$$ … $$` blocks — **plain Unicode
  inside, never LaTeX**: the app has no math renderer); never bury a formula mid-sentence.
  Notation per `math-and-notation.md` (standard digits/LTR everywhere, no `\commands`, no inline
  `$…$`, U+00A0 in Arabic grouped numbers).
- **Tables for structure.** Any classification/taxonomy/conjugation with ≥3 cases becomes a
  markdown table, not a paragraph.

## Axis 2 — Facilité de compréhension (the notion pattern)

> Rewritten 2026-09-16 (étude 35). The two lines this axis used to carry — « concrete before
> abstract » and « every rule has a worked example » — were right and inert: no pattern, no gate,
> no measurement stood behind them, and the corpus stated instead of explaining (maths 9ème: 54
> figure blocks, 1 method block, zero definition/example). The full doctrine, the seven times, the
> rules R-1…R-15 and the templates: **`course-explanation.md`** — read it before writing a lesson.

**One `##` section = one notion, explained in seven times, in this order:**

1. **Ancrer** — a situation the pupil knows, ending on **the question** the notion answers.
2. **Nommer** — the official term and the notation (`::: definition` / `::: propriete`).
3. **Voir** — a representation, plus the sentence tying it to the symbols (`::: figure`, a value
   table, a number line).
4. **Résoudre** — a worked example, **each step with its why** (`::: exemple`), reusing the
   anchor's own numbers.
5. **Distinguer** — the classic mistake, shown, diagnosed, corrected (`::: piege` / `> ⚠️`),
   targeting a tag of the misconception registry declared in `chapter.json` → `coursePitfalls`.
6. **Généraliser** — the rule **after** its example, with one edge case (`::: propriete` /
   `::: methode`).
7. **Vérifier sur place** — a completion example or a twin problem, answer folded
   (`::: verifie`), whose answer restates the reasoning.

Plus the closing `::: retenir` line, mirrored by the summary card.

- **One method at first contact.** Two methods are shown one after the other, never side by side
  in the section that introduces the first.
- **Progression simple → complexe**, at most one new notion per section (cognitive load).
- **A representation is tied to its symbols** by an explicit bridging sentence, or it is wallpaper.

## Axis 3 — Exhaustivité (completeness)

- **Golden rule — no orphan tested notion:** everything the chapter's `quiz.json` and
  `exercices/*.json` assess MUST be teachable from `cours.md` alone. Before finishing, list every
  notion the items test and point to the section that teaches it. A tested-but-untaught notion is
  a **[MAJOR]** audit finding (it makes questions unfair).
- **Full official scope, nothing more.** Cover all the notions of the official chapter for the
  grade (school content — see `content-ecole-tn`), and no off-program material. For non-school
  themes, cover the scope announced by `chapter.json`'s description.
- **Edge cases included.** The boundary/degenerate cases the exercises like to probe (zero,
  equality case, no-solution case, carry in rounding…) are stated in the course, not discovered
  in a correction.
- **Resume ↔ course bijection.** `resume.md` has one bullet per course section (same order),
  each = **bolded concept + one-line essence**. No section unmirrored, no bullet inventing
  material absent from the course.

## Axis 4 — Expérience pédagogique (learning experience)

- **The style-guide skeleton is the vehicle**: epic title + epigraph that motivates ("why this
  matters"), 5–7 emoji-led sections, mid-course `> 🗡️` tips and `> ⚠️` traps, closing `> 🏆`
  that frames the chapter as cleared and teases the next.
- **Motivate before teaching**: the epigraph/intro answers «à quoi ça sert ?» in one punchy line
  (real use, exam stake, or power gained).
- **Right length — counted per NOTION, not per course** (étude 35 R-13): a theory section runs
  **18–40 lines**, so a six-notion course runs **110–240**. Past 240 the chapter splits — a human
  decision, never a silent truncation. `resume.md` stays at ~7–10 bullets, one per section.
  (The former « ~50–75 lines » never described the corpus — maths 9ème runs 82 to 331 — and a
  dead rule is not a rule.)
- **The summary is a standalone revision tool**: a student re-reading only `resume.md` the night
  before recovers every key rule/formula of the chapter. If a bullet is too vague to revise from,
  it fails.
- **Language purity & RTL**: entirely in the subject's `contentLanguage` (per `quality-bar.md`),
  Arabic prose around standard math, fluent and idiomatic — never translated-sounding.

## Axis 5 — Illustration (the visual axis)

> Added 2026-07-14 (étude 18). Its absence was not a detail: with four purely textual axes, an
> audit of the repo found **66 illustrated courses out of 541** and **zero figures in the five
> geometry chapters of 9ème** — the national-exam year. The Thalès course described triangle ABC
> and line (MN) **in words only**. Nothing in this bar asked for a drawing, so nothing drew.
> **A geometry course without an illustration makes no sense.** Full doctrine, families and SVG
> templates: `course-figures.md`.

- **A rule about shapes, space, structure or change is TAUGHT WITH A DRAWING.** Plane geometry,
  circle & angles, coordinates & vectors, solids, trigonometry, measurement of shapes, science
  diagrams (SVT organs/cycles, circuits, optics), timelines and data graphs: the chapter carries at
  least one figure, and each spatial rule has its figure **next to it**, not at the end.
- **Never point at a figure that does not exist.** If the prose says «ci-dessous» / «الشكل المجاور»,
  the `<svg>` is in the file. This is the most damning defect — the pupil is sent to an image that
  isn't there — and `content:qa` fails **strict** on it.
- **The figure must be TRUE.** Points announced on a segment are on it; lines announced parallel are
  parallel; a right angle is 90°. A wrong figure teaches a wrong shape, and no automated gate can
  catch it — re-derive the coordinates before shipping.
- **One figure = one idea.** A figure carrying two notions carries neither.
- **Every course figure is captioned** (`::: figure <légende>`); its number is automatic. The caption
  says what to **see** («le petit triangle AMN est une réduction du grand»), not what the object is
  («un triangle»). It is written in the subject's content language.
- **Labels stay standard and LTR** — Latin vertex names, Western digits, SI units — **even in Arabic
  courses** (`math-and-notation.md`). Arabic prose belongs in the caption, never inside the drawing.
- **The summary is illustrated too** where the notion is visual: a revision card carrying the shape
  beats a card describing it.

## Audit grading (used by content-audit)

Map findings to the standard severities:

- **[BLOCKER]** — factually false statement or rule; course contradicts the answer keys of its
  own quiz/exercises; formula or worked example with a wrong result; **a figure that contradicts
  its own statement** (point off the segment, "parallels" that aren't) — it teaches a wrong shape;
  **a false worked example, classic mistake or check**; **a mistake left uncorrected in the text,
  or repeated in the summary** — the lesson would teach the error.
- **[MAJOR]** — tested-but-untaught notion (golden rule); rule without a worked example;
  **a theory section opening on its definition or its rule** (times 2 or 6 before time 1);
  **an example whose steps carry no why**; **a theory section with no check on the spot**;
  **a classic mistake with no registry tag, or on a misconception no distractor of the chapter
  encodes**; **two methods side by side at first contact**; **a check introducing a new notion**;
  off-program/wrong-grade notion (school); section incomprehensible at grade level; resume bullet
  missing for a section or inventing new material; notation violations (Arabic-Indic digits,
  bidi-unsafe grouped numbers, arabized formulas); language impurity; **a spatial chapter with no
  figure at all**; **a spatial rule stated without its figure**; **prose pointing at a figure the
  file does not contain**.
- **[MINOR]** — style-guide skeleton gaps (missing epigraph/callouts/closing); sentence-length /
  jargon issues; length out of range; weak motivation; table opportunity missed; resume order
  drift; **figure without a caption, figure redundant with the text it sits next to, or a caption
  that names the object instead of saying what to see**; **a representation with no bridging
  sentence, or a figure label that differs from the name used in the text**; **an anchor that
  raises no question**; **narrative decoration inside an explanation block**; **a block over 6
  lines of prose, or a section over 60 lines**; **a general rule stated without an edge case**.

Verdict per chapter: **ship** (no blocker, ≤1 major) or **fix-first**. Report per axis: one line
each for clarté / compréhension / exhaustivité / expérience / **illustration** with the findings
that drove it. On axis 2, report **per section**: which of the seven times are present, in which
order, and whether every example, mistake and check was **re-solved** (no gate can do that — it is
the whole reason a model audit exists on this axis).
