/**
 * Fidélité au matn : chaque citation « … » d'un cours/résumé de `fiqh` doit être une
 * sous-chaîne CONTIGUË du باب dont le chapitre est tiré. Attrape la citation recousue
 * (deux fragments non contigus collés) et la citation retouchée (coquille OCR corrigée
 * en silence) — deux défauts qu'aucun gate du moteur ne voit.
 *
 * La comparaison ignore ce que l'auteur du cours a le droit d'ajouter : diacritiques,
 * balisage, ponctuation (le matn n'en a aucune), variantes orthographiques de l'alif,
 * du ya et du ta marbuta.
 */
import { readdirSync, readFileSync, existsSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const S = "D:/11-coding/YahiaAcademy/yahia-quest-content/content/fiqh";
const BABS = join(HERE, "risala/babs");

const norm = (s) =>
  s
    .replace(/[\u064B-\u0652\u0670\u0640]/g, "")
    .replace(/[أإآٱ]/g, "ا")
    .replace(/ى/g, "ي")
    .replace(/ة/g, "ه")
    .replace(/[«»"'*_\u200f\u200e\u061c]/g, "")
    .replace(/[،,؛;:.!؟?()[\]{}—–\-ـ]/g, " ")
    .replace(/\s+/g, " ")
    .trim();

const perChapter = new Map();
let totalQuotes = 0;
const samples = [];

for (const ch of readdirSync(S, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name).sort()) {
  const matnPath = join(BABS, `${ch.slice(0, 2)}.md`);
  if (!existsSync(matnPath)) continue;
  // Les marqueurs de page de l'extracteur coupent les citations qui enjambent
  // une page : les retirer AVANT de normaliser, sinon on invente des écarts.
  const rawMatn = readFileSync(matnPath, "utf8").replace(/<!--[^>]*-->/g, " ");
  const matn = norm(rawMatn);
  let ok = 0, bad = 0;

  for (const f of ["cours.md", "resume.md"]) {
    const p = join(S, ch, f);
    if (!existsSync(p)) continue;
    for (const m of readFileSync(p, "utf8").matchAll(/«([^»]{12,})»/g)) {
      const parts = m[1].split(/\s*(?:\.\.\.|…)\s*/).map(norm).filter((x) => x.length >= 10);
      if (parts.length === 0) continue;
      totalQuotes++;
      const missing = parts.find((part) => !matn.includes(part));
      if (missing) {
        bad++;
        if (samples.length < 12) samples.push(`${ch}/${f} :: ${missing.slice(0, 75)}`);
      } else ok++;
    }
  }
  perChapter.set(ch, { ok, bad });
}

console.log(`citations vérifiées : ${totalQuotes}\n`);
for (const [ch, { ok, bad }] of perChapter) {
  const pct = ok + bad ? Math.round((bad / (ok + bad)) * 100) : 0;
  console.log(`${ch.padEnd(30)} ${String(ok).padStart(3)} contiguës · ${String(bad).padStart(3)} hors matn (${pct} %)`);
}
console.log("\nÉchantillon des écarts :");
for (const s of samples) console.log("  • " + s);
