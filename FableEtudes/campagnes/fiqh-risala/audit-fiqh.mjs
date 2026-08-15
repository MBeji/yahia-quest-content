/**
 * Audit complémentaire de la matière `fiqh` — ce que le gate du moteur ne voit pas :
 * conformité de l'échelle des missions, fuite par la longueur de la bonne option,
 * options citées par lettre, plafond de difficulté, doublons de questions, position
 * de la clé. Lecture seule. Sortie : un rapport, un code retour (0 = rien de bloquant).
 */
import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const SUBJ = "D:/11-coding/YahiaAcademy/yahia-quest-content/content/fiqh";

/** L'échelle canonique (rewards-and-modes.md, ladder par défaut). */
const LADDER = {
  "01-pratique.json": { mode: "practice", difficulty: 1, xpReward: 50, rewardCoins: 10, displayOrder: 1 },
  "02-boss.json": { mode: "boss", difficulty: 3, xpReward: 120, rewardCoins: 30, displayOrder: 2 },
  "03-revision.json": { mode: "practice", difficulty: 2, xpReward: 70, rewardCoins: 15, displayOrder: 3 },
  "04-defi.json": { mode: "challenge", difficulty: 4, xpReward: 300, rewardCoins: 60, displayOrder: 4 },
  "05-tathbit.json": { mode: "boss", difficulty: 3, xpReward: 120, rewardCoins: 30, displayOrder: 5 },
};
const REQUIRED = ["chapter.json", "cours.md", "resume.md", "quiz.json"];

const errors = [];
const warns = [];
const err = (w, m) => errors.push(`[error] ${w} — ${m}`);
const warn = (w, m) => warns.push(`[warn]  ${w} — ${m}`);

/** « الجواب ب » / « الخيار (ج) » / « option b » : ne désigne rien, les options sont mélangées. */
const LETTER_REF =
  /(?:الجواب|الإجابة|الخيار|الاختيار|البديل|الفقرة)\s*(?:هو\s*|هي\s*)?[:：]?\s*[(«"']?\s*[أابجدﺏ]\s*[)»"']?(?:\s|$|[.،؛])|\boption\s+[a-d]\b/i;

const norm = (s) => s.replace(/[\u064B-\u0652\u0670]/g, "").replace(/\s+/g, " ").trim();

const chapters = existsSync(SUBJ)
  ? readdirSync(SUBJ, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name).sort()
  : [];

let totalQ = 0;
let keyLongest = 0;
const keyPos = {};
const seenGlobal = new Map();

for (const ch of chapters) {
  const dir = join(SUBJ, ch);
  for (const f of REQUIRED) if (!existsSync(join(dir, f))) err(ch, `fichier manquant : ${f}`);
  const exDir = join(dir, "exercices");
  const exFiles = existsSync(exDir) ? readdirSync(exDir).filter((f) => f.endsWith(".json")).sort() : [];
  for (const want of Object.keys(LADDER)) {
    if (!exFiles.includes(want)) err(ch, `mission manquante : exercices/${want}`);
  }
  for (const extra of exFiles) if (!(extra in LADDER)) warn(ch, `mission hors échelle : exercices/${extra}`);

  const seenChapter = new Map();
  /** @type {[string, any][]} */
  const files = [];
  if (existsSync(join(dir, "quiz.json"))) files.push(["quiz.json", null]);
  for (const f of exFiles) files.push([`exercices/${f}`, LADDER[f]]);

  for (const [rel, spec] of files) {
    let data;
    try {
      data = JSON.parse(readFileSync(join(dir, rel), "utf8"));
    } catch (e) {
      err(ch, `${rel} : JSON invalide — ${e.message}`);
      continue;
    }
    const isQuiz = rel === "quiz.json";
    if (spec) {
      for (const [k, v] of Object.entries(spec)) {
        if (data[k] !== v) err(ch, `${rel} : ${k} = ${JSON.stringify(data[k])}, attendu ${JSON.stringify(v)}`);
      }
    }
    const qs = data.questions ?? [];
    const wantCount = isQuiz ? 5 : 6;
    if (qs.length !== wantCount) err(ch, `${rel} : ${qs.length} questions, attendu ${wantCount}`);
    if (!data.title) err(ch, `${rel} : titre manquant`);
    else if (!/[⭐]/.test(data.title)) warn(ch, `${rel} : le titre ne porte pas ses ⭐`);

    qs.forEach((q, i) => {
      const w = `${ch}/${rel}#${i + 1}`;
      totalQ++;
      if (q.type && q.type !== "mcq") { warn(w, `type non-mcq : ${q.type}`); return; }
      if (q.misconceptionTag || q.competencies || q.acceptedAnswers)
        err(w, "champ de registre interdit (misconceptionTag / competencies / acceptedAnswers)");
      if (q.difficulty != null && (q.difficulty < 1 || q.difficulty > 3))
        err(w, `difficulty de question = ${q.difficulty} (plafond 3)`);
      const opts = q.options ?? [];
      if (opts.length !== 4) err(w, `${opts.length} options, attendu 4`);
      const correct = opts.find((o) => o.id === q.correctOption);
      if (!correct) { err(w, `correctOption "${q.correctOption}" ne pointe aucune option`); return; }
      keyPos[q.correctOption] = (keyPos[q.correctOption] ?? 0) + 1;

      const lens = opts.map((o) => o.text.length);
      if (correct.text.length === Math.max(...lens) && new Set(lens).size > 1) keyLongest++;

      if (!q.explanation || q.explanation.trim().length < 15) err(w, "explication absente ou trop courte");
      else if (LETTER_REF.test(q.explanation)) err(w, `explication qui désigne une option par sa lettre : « ${q.explanation.slice(0, 70)}… »`);

      // L'énoncé ne doit pas contenir la bonne réponse mot pour mot.
      if (norm(correct.text).length > 12 && norm(q.prompt).includes(norm(correct.text)))
        err(w, "l'énoncé contient littéralement la bonne réponse");

      const key = norm(q.prompt);
      if (seenChapter.has(key)) err(w, `question déjà posée dans ${seenChapter.get(key)}`);
      else seenChapter.set(key, rel);
      if (seenGlobal.has(key)) warn(w, `question identique à ${seenGlobal.get(key)}`);
      else seenGlobal.set(key, `${ch}/${rel}`);
    });
  }
}

const pctLongest = totalQ ? Math.round((keyLongest / totalQ) * 100) : 0;
console.log(`chapitres : ${chapters.length} · questions : ${totalQ}`);
console.log(`clé = option la plus longue : ${keyLongest}/${totalQ} (${pctLongest}%) — hasard ≈ 25%`);
console.log(`position de la clé : ${JSON.stringify(keyPos)}`);
if (pctLongest > 40) warns.push(`[warn]  matière — fuite par la longueur : la clé est la plus longue dans ${pctLongest}% des questions`);
const posVals = Object.values(keyPos);
if (posVals.length && Math.max(...posVals) / (totalQ || 1) > 0.4)
  warns.push(`[warn]  matière — clé trop concentrée sur une position : ${JSON.stringify(keyPos)}`);

for (const l of warns) console.log(l);
for (const l of errors) console.log(l);
console.log(`\n${errors.length} erreur(s), ${warns.length} avertissement(s)`);
process.exit(errors.length ? 1 : 0);
