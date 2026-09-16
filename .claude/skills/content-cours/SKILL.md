---
name: content-cours
description: >-
  Author or rewrite course lessons (cours.md) and summaries (resume.md) for any
  chapter under content/ — specialized in lesson-text quality: clarity, ease of
  understanding, completeness (everything the quiz/exercises test must be taught),
  and learning experience. Use whenever the user wants to write, rewrite, improve,
  clarify, or complete a course or a summary — e.g. "réécris le cours du chapitre X",
  "le résumé n'est pas clair", "améliore la leçon", "le cours ne couvre pas tout",
  "rends ce chapitre plus pédagogique". Works for new chapters (course part) and
  existing ones (safe in-place rewrite). Defers to the content-engine skill —
  especially references/course-quality.md and references/style-guide.md.
---

# content-cours — specialized course & summary authoring

This skill owns the **lesson text**: `cours.md` and `resume.md`. The five quality axes are
defined in `content-engine/references/course-quality.md` (clarté, facilité de compréhension,
exhaustivité, expérience pédagogique, illustration) — **read it first**, along with
`references/course-explanation.md` (**the notion pattern** — the order in which a notion arrives,
and what each part must carry: this is how you write, not an optional extra),
`references/style-guide.md` (skeleton/voice), `references/math-and-notation.md` (notation,
including the Arabic NBSP rule), and the program wrapper if school content (`content-ecole-tn`:
official scope + language of instruction).

## When it applies

- **New chapter**: write the course+summary as part of the full chapter workflow (the rest —
  quiz/exercises — follows content-engine).
- **Rewrite/improve an existing chapter's lesson**: clarity pass, completeness pass, or full
  rewrite. **Safe in-place**: `cours.md`/`resume.md` map to `chapters.lesson_content`/`summary`
  and carry no UUIDs of their own — rewriting them never re-keys anything. Never rename the
  chapter folder.
- **Summary only**: tighten `resume.md` to the bijection rule (one bullet per course section,
  standalone revision value).

## Workflow

1. **Establish the scope to cover — AND the manual's own sequence.** School content: the authoritative scope is the **CNP program**, read
   via the **programme transcription**
   `content/programmes-officiels/programme/<gradeSlug>/<matière>.md` (consume it — it
   already **combines the teacher guide AND the manuel élève**, so it carries both the scope and the
   content/examples to teach; **don't render→vision the `cnp-officiel/` scans**; that's the persistence
   session's job, and if the transcription is missing the unit is blocked on it, see `programme/_INDEX.md`),
   with the Taybah school
   file (`programmes-officiels/<école>/<gradeSlug>.md`) as a secondary cross-check / trimester sequencing —
   plus `chapter.json` sources. Non-school:
   `chapter.json` description. Then — critical — **read the chapter's `quiz.json` and every
   `exercices/*.json` FIRST** and extract the list of notions/edge cases they test: the course must teach
   all of them (golden rule, no orphan tested notion). If an item tests something genuinely off-scope, flag
   it in the report instead of silently teaching off-program material.
   **Two more things to harvest from the transcription, and they decide how you write:** its
   **activities** (« نشاط ») and its **solved exercises** (« تمرين مرفق بحل ») — they are the
   situations the programme itself uses to make each notion appear, and your anchors come from
   them first (rewritten, never copied: `content:qa` runs an anti-verbatim guard over lessons).
   Then `grep` the chapter's own `misconceptionTag`s out of its `quiz.json` and `exercices/*.json`:
   those are the errors your course must show and correct, and you will declare the ones you
   treat in `chapter.json` → `coursePitfalls`.
2. **Plan the sections**: 5–7 sections, one notion each, simple → complexe, each new notion
   anchored on the previous. Place the `> ⚠️` traps where the confusion is born (mirror the
   exercises' distractors).
3. **Write `cours.md` — one section per notion, seven times in order** (`course-explanation.md`):
   **ancrer** (a situation the pupil knows, ending on the question it raises — from the manual's
   activity when there is one) → **nommer** (the official term, the notation alone on its line) →
   **voir** (a representation + the sentence tying it to the symbols) → **résoudre** (a worked
   example reusing the anchor's numbers, **each step with its why** in half a line) →
   **distinguer** (the classic mistake, after a correct example, named, diagnosed, corrected —
   targeting one of the chapter's tags) → **généraliser** (the rule after its example, with an
   edge case) → **vérifier sur place** (`::: verifie`, question above the `---`, folded answer
   below, restating the reasoning). Close with `::: retenir`, one line.
   The definition never opens a section; the general rule never precedes its example; one method
   at first contact. Budget: 18–40 lines per theory section, 110–240 per course.
4. **ILLUSTRATE — a rule about shapes taught without a drawing is a non-conformity**
   (course-quality Axis 5; doctrine, families and copy-paste SVG templates:
   `content-engine/references/course-figures.md`). Go back over the sections you just wrote and ask,
   for each: _is this notion spatial?_ Geometry, circle & angles, repère & vecteurs, solids,
   trigonometry, measurement of shapes, science diagrams (organs, cycles, circuits, optics),
   timelines, data graphs → it gets a figure, **next to its rule**, not at the end.
   Attach it with `::: figure <légende>` + an inline `<svg viewBox="…">`; the number is automatic.
   Three rules that decide whether the figure helps or harms:
   - **it must be TRUE** — re-derive the coordinates (points announced on a segment are on it,
     "parallels" really are parallel, a right angle is 90°). A wrong figure teaches a wrong shape,
     and **no automated gate can catch it**;
   - **one figure = one idea**;
   - **never point at a figure you did not draw** (« ci-dessous », « الشكل المجاور » with no `<svg>`
     = `content:qa` **[error]**).
     Illustrate the **résumé** too when the notion is visual: a revision card carrying the shape beats
     a card describing it.
5. **Write `resume.md`**: one bullet per section, same order, bolded concept + one-line essence,
   7–10 bullets, revisable standalone.
6. **Self-verification (before the checks)** — walk course-quality's **five** axes (Illustration
   included) and, on axis 2, the **nine-point self-check of `course-explanation.md` §6**, section
   by section: the anchor raises a question, the same story runs to the worked example, every step
   carries its why, the mistake is corrected and tagged, the rule follows its example with an edge
   case, the check is a twin with a folded answer restating the reasoning — and **every example,
   mistake and check is re-derived and true** (no gate can do that for you);
   verify the tested-notions list from step 1 is fully covered (cite section per notion);
   verify resume ↔ course bijection; run the notation scans (`[٠-٩]`, `\d \d{3}` in ar, hyphen-minus,
   and the **Arabic comma `،` inside a math bracket group** — `content:qa` fails strict on it, and
   the first pass over the lessons on 2026-07-14 found 46 such violations across 22 files).
   If you changed which notions the course covers, re-check the quiz is still answerable from
   the course alone — and report any quiz/exercise that should be adjusted (don't edit items
   unless asked; that's content-engine/content-audit territory).
7. `npm run content:check` **and `npm run content:qa`** (read the warnings of your own subject:
   the pattern checks C-1…C-6 are yours) — then **stop and report**: chapter(s) touched, the
   notion → times → blocks map, the `coursePitfalls` declared per chapter, the length before and
   after, the tested-notion coverage map, axis-by-axis self-assessment, and the human's build/apply steps
   (a course rewrite changes `chapters` rows → `content:build` + apply before deploy, UUIDs
   stable).

## Quality specifics to honor

- **Trilingual programs**: each sibling subject's course is written natively in its language —
  rewrite siblings independently, never by translation (`themes-and-trilingual.md`).
- **Arabic**: full RTL prose around standard math, U+00A0 inside grouped numbers
  (`math-and-notation.md`), official Arabic terminology of the grade.
- Never weaken: don't shorten a course by dropping tested notions; don't add off-program
  material to "enrich"; don't move the fun into the assessment (RPG stays in titles/narration).
