/**
 * Extraction du matn de « الرسالة » d'Ibn Abî Zayd al-Qayrawânî (m. 386 h.)
 * depuis shamela.ws/book/11373 — texte du Xe siècle, domaine public.
 * Écrit un fichier par page dans pages/, puis un fichier par باب dans babs/.
 */
import { mkdir, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const OUT = join(HERE, "risala");
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36";

/** Les 45 أبواب et leur page de départ (index du livre, relevé sur la page du livre). */
const BABS = [
  [1, "باب ما تنطق به الألسنة وتعتقده الأفئدة من واجب أمور الديانات"],
  [7, "باب ما يجب منه الوضوء والغسل"],
  [10, "باب طهارة الماء والثوب والبقعة وما يجزىء من اللباس في الصلاة"],
  [12, "باب صفة الوضوء ومسنونه ومفروضه وذكر الاستنجاء والاستجمار"],
  [17, "باب في الغسل"],
  [20, "باب فيمن لم يجد الماء وصفة التيمم"],
  [23, "باب في المسح على الخفين"],
  [25, "باب في أوقات الصلاة وأسمائها"],
  [28, "باب في الأذان والإقامة"],
  [30, "باب صفة العمل في الصلوات المفروضة وما يتصل بها من النوافل والسنن"],
  [40, "باب في الإمامة وحكم الإمام والمأموم"],
  [43, "باب جامع في الصلاة"],
  [51, "باب في سجود القرآن"],
  [53, "باب في صلاة السفر"],
  [55, "باب في صلاة الجمعة"],
  [57, "باب في صلاة الخوف"],
  [58, "باب في صلاة العيدين والتكبير أيام منى"],
  [61, "باب في صلاة الخسوف"],
  [63, "باب في صلاة الاستسقاء"],
  [65, "باب ما يفعل بالمحتضر وفي غسل الميت"],
  [68, "باب في الصلاة على الجنائز والدعاء للميت"],
  [71, "باب في الدعاء للطفل والصلاة عليه وغسله"],
  [73, "باب في الصيام"],
  [78, "باب في الاعتكاف"],
  [80, "باب في زكاة العين والحرث والماشية وما يخرج من المعدن وذكر الجزية"],
  [84, "باب في زكاة الماشية"],
  [87, "باب في زكاة الفطر"],
  [89, "باب في الحج والعمرة"],
  [96, "باب في الضحايا والذبائح والعقيقة والصيد والختان وما يحرم من الأطعمة والأشربة"],
  [102, "باب في الجهاد"],
  [105, "باب في الأيمان والنذور"],
  [110, "باب في النكاح والطلاق والرجعة والظهار والإيلاء واللعان والخلع والرضاع"],
  [120, "باب في العدة والنفقة والاستبراء"],
  [125, "باب في البيوع وما شاكل البيوع"],
  [136, "باب في الوصايا والمدبر والمكاتب والمعتق وأم الولد والولاء"],
  [140, "باب في الشفعة والهبة والصدقة والحبس والرهن والعارية والوديعة واللقطة والغصب"],
  [145, "باب في أحكام الدماء والحدود"],
  [156, "باب في الأقضية والشهادات"],
  [163, "باب في الفرائض"],
  [173, "باب جمل من الفرائض والسنن الواجبة والرغائب"],
  [184, "باب في الفطرة والختان وحلق الشعر واللباس وستر العورة وما يتصل بذلك"],
  [187, "باب في الطعام والشراب"],
  [190, "باب في السلام والاستئذان والتناجي والقراءة والدعاء وذكر الله والقول في السفر"],
  [196, "باب في التعالج وذكر الرقى والطيرة والنجوم والخصاء والوسم والكلاب والرفق بالمملوك"],
  [199, "باب في الرؤيا والتثاوب والعطاس واللعب بالنرد وغيرها والسبق بالخيل والرمي وغير ذلك"],
];

const decode = (s) =>
  s
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");

/** Renvoie { pageNum, paragraphs[] } ou null si la page n'existe pas. */
async function fetchPage(id) {
  const res = await fetch(`https://shamela.ws/book/11373/${id}`, { headers: { "User-Agent": UA } });
  if (!res.ok) return null;
  const html = await res.text();
  const open = html.indexOf('<div class="nass');
  if (open === -1) return null;
  const tagEnd = html.indexOf(">", open);
  const pageNum = (html.slice(open, tagEnd).match(/data-page-num="(\d+)"/) || [])[1] ?? String(id);
  // Le corps du باب s'arrête au conteneur des pages chargées à la suite.
  const stop = html.indexOf('id="appended_pages"', tagEnd);
  const body = html.slice(tagEnd + 1, stop === -1 ? html.length : stop);
  const paragraphs = [...body.matchAll(/<p\b[^>]*>([\s\S]*?)<\/p>/g)]
    .map(([, inner]) =>
      decode(inner.replace(/<[^>]+>/g, ""))
        .replace(/\s+/g, " ")
        .trim(),
    )
    .filter((t) => t.length > 0);
  return { pageNum, paragraphs };
}

/** Dernière page du livre : on avance tant que la page répond. */
async function findLastPage(from) {
  let last = from;
  for (let id = from; id < from + 40; id++) {
    const p = await fetchPage(id);
    if (!p || p.paragraphs.length === 0) break;
    last = id;
  }
  return last;
}

await mkdir(join(OUT, "babs"), { recursive: true });

const lastPage = await findLastPage(BABS[BABS.length - 1][0]);
console.log(`dernière page du livre : ${lastPage}`);

const pages = new Map();
const ids = Array.from({ length: lastPage }, (_, i) => i + 1);
const CONCURRENCY = 4;
for (let i = 0; i < ids.length; i += CONCURRENCY) {
  const slice = ids.slice(i, i + CONCURRENCY);
  const got = await Promise.all(slice.map((id) => fetchPage(id).then((p) => [id, p])));
  for (const [id, p] of got) if (p) pages.set(id, p);
  process.stdout.write(`\rpages ${Math.min(i + CONCURRENCY, ids.length)}/${ids.length}`);
  await new Promise((r) => setTimeout(r, 120));
}
console.log("");

let missing = ids.filter((id) => !pages.has(id));
console.log(`pages récupérées : ${pages.size}/${ids.length}${missing.length ? ` — manquantes : ${missing.join(", ")}` : ""}`);

const manifest = [];
for (let b = 0; b < BABS.length; b++) {
  const [start, title] = BABS[b];
  const end = b + 1 < BABS.length ? BABS[b + 1][0] - 1 : lastPage;
  const chunks = [];
  for (let id = start; id <= end; id++) {
    const p = pages.get(id);
    if (!p) continue;
    chunks.push(`<!-- ص ${p.pageNum} (shamela ${id}) -->\n\n${p.paragraphs.join("\n\n")}`);
  }
  const num = String(b + 1).padStart(2, "0");
  const text = chunks.join("\n\n");
  const header = `# ${title}\n\n> باب ${b + 1}/45 — الرسالة لابن أبي زيد القيرواني (ت 386 هـ)\n> المصدر: https://shamela.ws/book/11373 — الصفحات ${start}–${end}\n\n---\n\n`;
  await writeFile(join(OUT, "babs", `${num}.md`), header + text + "\n", "utf8");
  manifest.push({ num: b + 1, title, startPage: start, endPage: end, chars: text.length });
}

await writeFile(join(OUT, "manifest.json"), JSON.stringify(manifest, null, 2), "utf8");
console.log("\nباب | صفحات | حجم");
for (const m of manifest) console.log(`${m.num} | ${m.startPage}-${m.endPage} | ${m.chars}`);
