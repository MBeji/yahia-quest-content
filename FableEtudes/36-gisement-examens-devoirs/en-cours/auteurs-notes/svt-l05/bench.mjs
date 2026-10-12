// Banc de rendu RTL (Chromium, dir=rtl) des textes d'une mission : reproduit RichField / OptionContent
// (splitMathRuns, isDisplayEquation, .math-run) du moteur et mesure l'ordre visuel des formules.
//
// usage : node --experimental-strip-types bench-rtl.mjs <fichier.json> <sortie.png> [largeur=400] [q1,q2,...]
//   - imprime, pour chaque champ (énoncé, option, explication), les segments non arabes à opérateur
//     dont l'ordre visuel est inversé par rapport à l'ordre logique (signe d'une formule brouillée) ;
//   - écrit une capture pleine page (les questions demandées, ou toutes).
import { readFileSync } from "node:fs";
import { pathToFileURL } from "node:url";

const ENGINE = "/home/user/eng-svt5";
const { chromium } = await import(pathToFileURL(`${ENGINE}/node_modules/playwright/index.mjs`).href);
// bidi.ts de l'origin/main du moteur (arena#1160 : « 30° = OI/OB » isole) copie dans engine-latest/ ; BIDI=ancien pour l'ancien clone
const BIDI = process.env.BIDI === "ancien" ? `${ENGINE}/src/shared/lib/bidi.ts` : "/home/user/eng-svt5/src/shared/lib/bidi.ts";
const { splitMathRuns, isDisplayEquation } = await import(pathToFileURL(BIDI).href);

const [, , src, out, widthArg, qsArg] = process.argv;
if (!src || !out) {
  console.error("usage: node --experimental-strip-types bench-rtl.mjs <fichier.json> <sortie.png> [largeur] [q1,q2,...]");
  process.exit(2);
}
const W = Number(widthArg || 400);
const only = qsArg ? new Set(qsArg.split(",").map(Number)) : null;
const data = JSON.parse(readFileSync(src, "utf8"));

const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const stripSvg = (s) => s.replace(/<svg[\s\S]*?<\/svg>/gi, "").trim();

function renderRuns(text) {
  const runs = splitMathRuns(text);
  if (runs.length === 1 && !runs[0].math) return esc(text);
  return runs
    .map((r) => (r.math ? `<span class="math-run${r.nowrap ? " math-run-tight" : ""}">${esc(r.text)}</span>` : esc(r.text)))
    .join("");
}
function renderLines(text) {
  const lines = text.split("\n").filter((l) => l.trim() !== "");
  if (lines.length <= 1) return renderRuns(text);
  return lines
    .map((l) => (isDisplayEquation(l) ? `<span class="math-equation">${esc(l.trim())}</span>` : `<span class="block">${renderRuns(l)}</span>`))
    .join("");
}

const isMathExpression = (t) =>
  /^[\s0-9a-zA-Z+\-−*/=²³¹⁰⁴⁵⁶⁷⁸⁹⁺⁻₀₁₂₃₄₅₆₇₈₉₊₋√×÷(){}[\]<>≤≥≠≈≡±∞π°′″.,;:|^_%∈∉∋∌⊂⊃⊄⊅⊆⊇⊈⊉⊊⊋∪∩∅ℝℕℤℚℂ∥⊥∠→⟶⟵⟹⟺Ωµ∆∑∏∫]+$/u.test(t.trim());
let cards = "";
data.questions.forEach((q, i) => {
  const n = i + 1;
  if (only && !only.has(n)) return;
  const type = q.type || "mcq";
  let opts = "";
  for (const o of q.options || []) {
    const od = isMathExpression(stripSvg(o.text)) ? "ltr" : "rtl";
    opts += `<div class="opt chk" data-id="Q${n}-${o.id}" dir="${od}"><span class="lbl">${o.id})</span><span>${renderRuns(stripSvg(o.text))}</span></div>`;
  }
  cards += `<div class="card"><h4 dir="ltr">Q${n} [${type}] d${q.difficulty}</h4>
    <div class="chk prompt" data-id="Q${n}-prompt" dir="rtl">${renderLines(stripSvg(q.prompt))}</div>
    ${opts}
    <div class="chk expl" data-id="Q${n}-expl" dir="rtl">${renderLines(q.explanation)}</div></div>`;
});

const html = `<!doctype html><html lang="ar" dir="rtl"><meta charset="utf8"><style>
body{font-family:"DejaVu Sans","FreeSerif",sans-serif;font-size:16px;margin:8px;background:#fff;color:#111}
.card{border:1px solid #bbb;border-radius:8px;padding:8px;margin:10px 0;width:${W}px;box-sizing:border-box}
.block{display:block}
.math-run{direction:ltr;unicode-bidi:isolate}
.math-run-tight{white-space:nowrap}
.math-equation{display:block;margin:.6rem 0;text-align:center;white-space:nowrap;direction:ltr;unicode-bidi:isolate;max-width:100%;overflow-x:auto}
.opt{margin:5px 0}.lbl{font-weight:700;direction:ltr;display:inline-block;margin-inline-end:6px}
.expl{margin-top:8px;color:#333;font-size:15px;border-top:1px dashed #ccc;padding-top:6px}
h4{margin:0 0 6px 0;color:#555;font:12px monospace}
</style><body>${cards}</body></html>`;

const browser = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const page = await browser.newPage({ viewport: { width: W + 40, height: 800 } });
await page.setContent(html);
await page.waitForTimeout(300);

const report = await page.evaluate(() => {
  const AR = /[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]/u;
  const OPS = /[=<>≤≥∥⊥∠/×÷+−√²³∈⊂]/u;
  const TRIM = /^[\s.,،:؛؟!✓)\]]+|[\s.,،:؛؟!✓(\[]+$/gu;
  const problems = [];
  for (const el of document.querySelectorAll(".chk")) {
    const id = el.getAttribute("data-id");
    const chars = [];
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) {
      if (node.parentElement && node.parentElement.classList.contains("lbl")) continue;
      const t = node.nodeValue;
      for (let k = 0; k < t.length; k++) {
        const r = document.createRange();
        r.setStart(node, k);
        r.setEnd(node, k + 1);
        const rects = r.getClientRects();
        const rc = rects.length ? rects[0] : null;
        chars.push({ ch: t[k], x: rc ? rc.left + rc.width / 2 : null, y: rc ? rc.top + rc.height / 2 : null, h: rc ? rc.height : 0 });
      }
    }
    let seg = [];
    const flush = () => {
      // retire la ponctuation de bord (point final, virgule arabe, coche)
      let a = 0, b = seg.length;
      while (a < b && /[\s.,،:؛؟!✓)\]]/u.test(seg[a].ch)) a++;
      while (b > a && /[\s.,،:؛؟!✓(\[]/u.test(seg[b - 1].ch)) b--;
      const core = seg.slice(a, b);
      const txt = core.map((c) => c.ch).join("");
      const vis = core.filter((c) => c.x !== null && !/[\s°]/u.test(c.ch));
      while (vis.length && /[()\[\]]/u.test(vis[0].ch)) vis.shift();
      while (vis.length && /[()\[\]]/u.test(vis[vis.length - 1].ch)) vis.pop();
      if (vis.length >= 2 && OPS.test(txt) && /[A-Za-z]/.test(txt)) {
        let bad = 0;
        for (let i = 1; i < vis.length; i++) {
          const p = vis[i - 1], q = vis[i];
          if (Math.abs(p.y - q.y) < 0.6 * (p.h || 16) && q.x < p.x - 0.5) bad++;
        }
        if (bad > 0) problems.push({ id, text: txt, reversedSteps: bad, of: vis.length - 1 });
      }
      seg = [];
    };
    for (const c of chars) {
      if (AR.test(c.ch)) flush();
      else seg.push(c);
    }
    flush();
  }
  return problems;
});

await page.screenshot({ path: out, fullPage: true });
await browser.close();
if (!report.length) console.log(`bench-rtl : aucune formule brouillée (largeur ${W})`);
else {
  console.log(`bench-rtl : ${report.length} segment(s) à l'ordre visuel inversé (largeur ${W})`);
  for (const p of report) console.log(`  ${p.id}  « ${p.text} »  (${p.reversedSteps}/${p.of} pas inversés)`);
}
