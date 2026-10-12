// usage: node render_figs.mjs <mission.json> <out.png> [cols=3] [scale=1.6]
import { readFileSync } from "node:fs";
import { pathToFileURL } from "node:url";
const ENGINE = "/home/user/eng-gisement";
const { chromium } = await import(pathToFileURL(`${ENGINE}/node_modules/playwright/index.mjs`).href);
const [, , src, out, colsArg, scaleArg] = process.argv;
const cols = Number(colsArg || 3), scale = Number(scaleArg || 1.5);
const d = JSON.parse(readFileSync(src, "utf8"));
let cells = "";
d.questions.forEach((q, i) => {
  const m = q.prompt.match(/<svg[\s\S]*?<\/svg>/);
  const t = (q.prompt.replace(/<svg[\s\S]*?<\/svg>/, "").trim().split("\n").pop() || "").slice(0, 70);
  if (m) cells += `<div class="c"><div class="n">Q${i + 1} d${q.difficulty} — ${t.replace(/</g, "&lt;")}</div>${m[0]}</div>`;
  (q.options || []).forEach((o) => { const mo = o.text.match(/<svg[\s\S]*?<\/svg>/); if (mo) cells += `<div class="c"><div class="n">Q${i + 1} opt ${o.id}</div>${mo[0]}</div>`; });
});
const html = `<!doctype html><meta charset=utf8><style>body{margin:8px;background:#fff;font-family:sans-serif}
.g{display:grid;grid-template-columns:repeat(${cols},${Math.round(300 * scale)}px);gap:10px}
.c{border:1px solid #ccc;padding:4px}.n{font:11px monospace;color:#444;direction:rtl;white-space:nowrap;overflow:hidden}
svg{width:${Math.round(300 * scale)}px;height:auto;background:#fff;display:block}</style><div class=g>${cells}</div>`;
const browser = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const page = await browser.newPage({ viewport: { width: Math.round(cols * (300 * scale + 14) + 30), height: 900 } });
await page.setContent(html);
await page.waitForTimeout(200);
await page.screenshot({ path: out, fullPage: true });
await browser.close();
console.log("ok", out);
