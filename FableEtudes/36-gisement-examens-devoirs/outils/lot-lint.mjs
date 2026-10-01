// lot-lint : défauts MÉCANIQUES que les audits des lots L05 à L10 ont retrouvés à la main.
// Usage : node lot-lint.mjs <fichier.json> [<fichier.json> …]
// Le moteur de rendu lu est `src/shared/lib/bidi.ts` d'un clone du moteur à jour (arena `main`) : par défaut
// /home/user/yahia-quest-arena, ou le dossier donné par la variable ENGINE. Node ≥ 24 (il importe du TypeScript).
// Conseillé : avant de rendre une tranche. Sorties « à regarder », pas des verdicts.
import fs from "node:fs";
import path from "node:path";
const ENG = process.env.ENGINE ?? "/home/user/yahia-quest-arena";
const B = await import(`${ENG}/src/shared/lib/bidi.ts`);
const ARC = "\\u0600-\\u06FF\\u0750-\\u077F\\u08A0-\\u08FF\\uFB50-\\uFDFF\\uFE70-\\uFEFF";
const AR = new RegExp(`[${ARC}]`, "u");
const DIAC = /[ً-ْٰـ]/gu;
const strip = (s) => s.replace(DIAC, "");
const findings = [];
const flag = (file, q, kind, msg) => findings.push(`${path.basename(file).slice(0, 8)} Q${q} [${kind}] ${msg}`);
const norm = (s) => s.replace(/\s+/g, " ").trim();
for (const file of process.argv.slice(2)) {
  const d = JSON.parse(fs.readFileSync(file, "utf8"));
  const diffs = d.questions.map((q) => q.difficulty ?? 0);
  for (let i = 1; i < diffs.length; i++) if (diffs[i] < diffs[i - 1]) flag(file, i + 1, "rampe", `difficulté ${diffs[i - 1]} → ${diffs[i]} (non décroissante exigée)`);
  d.questions.forEach((q, qi) => {
    const n = qi + 1;
    const opts = q.options ?? [];
    const key = q.correctOption;
    const keyText = opts.find((o) => o.id === key)?.text;
    // 1. clé strictement la plus longue (diacritiques retirés aussi)
    if (keyText) {
      const lens = opts.map((o) => [o.id, strip(o.text).length]);
      const lk = strip(keyText).length;
      if (opts.length > 1 && opts.every((o) => o.id === key || strip(o.text).length < lk)) flag(file, n, "clé-longue", `la clé (${key}, ${lk} car.) est strictement la plus longue : ${JSON.stringify(lens)}`);
    }
    // 2. paires d'options nues séparées par la virgule arabe — se lisent à l'envers dans une page RTL
    for (const o of opts) if (/^[−+-]?[\d.,/√]+\s*[،,]\s*[−+-]?[\d.,/√]+$/u.test(o.text.trim()) && /،/u.test(o.text)) flag(file, n, "paire-nue", `option ${o.id} « ${o.text} » : valeurs non étiquetées séparées par « ، » (lue à l'envers en RTL)`);
    // 3. options en double
    const seen = new Map();
    for (const o of opts) { const k = norm(o.text); if (seen.has(k)) flag(file, n, "double", `options ${seen.get(k)} et ${o.id} identiques`); seen.set(k, o.id); }
    // 4. lignes de formule seules (sans arabe) que le moteur ne pose pas en bloc — champs prompt et explanation
    for (const field of ["prompt", "explanation"]) {
      const text = (q[field] ?? "").replace(/<svg[\s\S]*?<\/svg>/g, "");
      const lines = text.split("\n").filter((l) => l.trim());
      if (lines.length > 1) for (const line of lines) {
        if (AR.test(line)) continue;
        if (B.isDisplayEquation(line)) continue;
        const runs = B.splitMathRuns(line);
        const prose = runs.filter((r) => !r.math).map((r) => r.text).join("").replace(/[\s.,;:]+/g, "");
        if (runs.some((r) => r.math) && prose.length) flag(file, n, "ligne-formule", `${field} : « ${line.trim().slice(0, 60)} » — ligne sans arabe ni équation reconnue, mêlant formule et texte latin (brouillée en RTL)`);
        else if (/[=<>≤≥≠≈]/u.test(line) === false && /[√^|]|\d\s*\(|\)\s*[\d⁰-⁹²³]/u.test(line) && !B.isDisplayEquation(line)) flag(file, n, "ligne-formule?", `${field} : « ${line.trim().slice(0, 60)} » — terme seul non posé en bloc`);
      }
      // la ligne de donnée « AB = 9 cm » (unité collée) seule sur sa ligne
      for (const line of lines) if (!AR.test(line) && /\b[A-Z]{1,3}\s*=\s*[\d.,]+\s*(cm|m|mm|km|°)\b/u.test(line) && !B.isDisplayEquation(line)) flag(file, n, "ligne-unité", `${field} : « ${line.trim().slice(0, 60)} » — donnée à unité collée seule sur sa ligne`);
    }
    // 5. coche ✓ collée à un distracteur : la valeur juste avant « ✓ » est-elle le texte d'une option fausse ?
    const ex = q.explanation ?? "";
    for (const m of ex.matchAll(/(\S+(?:\s\S+){0,3})\s*✓/gu)) {
      const before = norm(m[1]);
      for (const o of opts) {
        if (o.id === key) continue;
        const t = norm(o.text);
        if (t.length >= 1 && (before === t || before.endsWith(" " + t) || before.endsWith("= " + t))) flag(file, n, "coche", `✓ suit « ${before} » = l'option fausse ${o.id} « ${o.text} »`);
      }
    }
    // 6. une explication qui cite la lettre d'une option
    if (/(?:الخيار|الجواب|option|choix)\s*[abcd]\b/u.test(ex) || /\(\s*[abcd]\s*\)/u.test(ex)) flag(file, n, "lettre", "l'explication cite une lettre d'option");
    // 7. options numériques : somme ou différence de deux autres
    const nums = opts.map((o) => ({ id: o.id, v: Number(o.text.replace(/\s/g, "").replace(",", ".").replace("−", "-")) })).filter((x) => Number.isFinite(x.v));
    if (nums.length >= 3) for (const a of nums) for (const b of nums) for (const c of nums) if (a.id < b.id && c.id !== a.id && c.id !== b.id) {
      if (Math.abs(a.v + b.v - c.v) < 1e-9 || Math.abs(Math.abs(a.v - b.v) - c.v) < 1e-9) flag(file, n, "somme", `option ${c.id} = ${a.id} ± ${b.id} (${a.v}, ${b.v}, ${c.v})`);
    }
  });
}
console.log(findings.length ? findings.join("\n") : "lot-lint : rien à signaler");
console.log(`— ${findings.length} point(s) à regarder`);
