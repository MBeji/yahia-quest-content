/**
 * ⚠️ Les seuils sont BAS À DESSEIN (6 caractères par citation, 5 par fragment) : un seuil de
 * 12 laissait passer « أربع فأقلّ » (11 car.), contraction silencieuse de « أربع ركعات فأقل ».
 * Les remonter recrée l'angle mort — ne le fais pas pour réduire le bruit.
 *
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

/**
 * Les textes d'un chapitre rendus à l'élève et susceptibles de porter des « … » :
 * l'énoncé, le texte de chaque option, l'explication. Ils comptent exactement autant
 * que le cours — c'est là qu'un locuteur fictif ou une formule coranique tronquée passe
 * le plus facilement pour du matn.
 */
function collectQuestionFields(chDir) {
  const out = [];
  const files = ["quiz.json"];
  const exDir = join(chDir, "exercices");
  if (existsSync(exDir)) for (const f of readdirSync(exDir)) files.push(`exercices/${f}`);
  for (const rel of files) {
    const fp = join(chDir, rel);
    if (!existsSync(fp)) continue;
    let j;
    try {
      j = JSON.parse(readFileSync(fp, "utf8"));
    } catch {
      continue;
    }
    (j.questions ?? []).forEach((q, i) => {
      const where = `${rel}#${i + 1}`;
      if (q.prompt) out.push([`${where}.prompt`, q.prompt]);
      if (q.explanation) out.push([`${where}.explanation`, q.explanation]);
      for (const o of q.options ?? []) if (o.text) out.push([`${where}.option.${o.id}`, o.text]);
    });
  }
  return out;
}

const perChapter = new Map();
let totalQuotes = 0;
const samples = [];
const missingMatn = [];

for (const ch of readdirSync(S, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name).sort()) {
  const matnPath = join(BABS, `${ch.slice(0, 2)}.md`);
  // Un matn manquant NE DOIT PAS être un chapitre sauté en silence : sans cette
  // garde, le chapitre compte 0 écart et le rapport passe au vert sans avoir rien
  // comparé. Le dossier risala/babs/ n'est pas versionné — il se produit par
  // `node extract-risala.mjs` — donc le cas est la règle, pas l'exception.
  if (!existsSync(matnPath)) {
    missingMatn.push(`${ch} (attendu : ${matnPath})`);
    continue;
  }
  // Les marqueurs de page de l'extracteur coupent les citations qui enjambent
  // une page : les retirer AVANT de normaliser, sinon on invente des écarts.
  const rawMatn = readFileSync(matnPath, "utf8").replace(/<!--[^>]*-->/g, " ");
  const matn = norm(rawMatn);
  let ok = 0, bad = 0;

  // ⚠️ Les CHAMPS DE QUESTIONS comptent autant que le cours. Ne lire que cours.md et
  // resume.md cachait la moitié des emplois fautifs de « … » (audit du 2026-08-15) :
  // locuteurs fictifs, mots isolés, formules coraniques tronquées vivaient dans les
  // énoncés et les explications, hors de portée du contrôle.
  const sources = [];
  for (const f of ["cours.md", "resume.md"]) {
    const fp = join(S, ch, f);
    if (existsSync(fp)) sources.push([f, readFileSync(fp, "utf8")]);
  }
  sources.push(...collectQuestionFields(join(S, ch)));

  for (const [f, body] of sources) {
    for (const m of body.matchAll(/«([^»]{6,})»/g)) {
      const parts = m[1].split(/\s*(?:\.\.\.|…)\s*/).map(norm).filter((x) => x.length >= 5);
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

if (missingMatn.length) process.exit(2);
