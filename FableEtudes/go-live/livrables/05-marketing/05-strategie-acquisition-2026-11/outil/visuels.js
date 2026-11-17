// Atelier visuels Na9ra Nal3ab : génère les visuels sociaux (PNG) aux polices et couleurs du site.
// Usage : node visuels.js <dossier public/fonts du dépôt> <dossier de sortie>
// Pour un nouveau visuel : ajouter une entrée au tableau `cards` (name, w, h, html).
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const b64 = (f) => 'data:font/woff2;base64,' + fs.readFileSync(path.join(process.argv[2], f)).toString('base64');
const FONTS = process.argv[2];   // dossier des polices de la marque
const OUT = process.argv[3];     // dossier de sortie
const css = `
@font-face{font-family:'Orbitron';font-weight:500 900;src:url('${b64('orbitron-latin-var.woff2')}') format('woff2');}
@font-face{font-family:'Space Grotesk';font-weight:400 700;src:url('${b64('space-grotesk-latin-var.woff2')}') format('woff2');}
@font-face{font-family:'Noto Kufi Arabic';font-weight:600 700;src:url('${b64('noto-kufi-arabic-var.woff2')}') format('woff2');}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100%}
body{background:#f6fbf8;color:#16302b;font-family:'Space Grotesk','Noto Kufi Arabic',sans-serif;position:relative;overflow:hidden}
.stripe{position:absolute;left:0;top:0;bottom:0;width:20px;background:#0f6e56}
.c1{position:absolute;right:-190px;top:-170px;width:620px;height:620px;border-radius:50%;background:rgba(15,110,86,.085)}
.c2{position:absolute;right:120px;bottom:-330px;width:560px;height:560px;border-radius:50%;background:rgba(15,110,86,.06)}
.wrap{position:absolute;inset:0;padding:84px 84px 76px 104px;display:flex;flex-direction:column}
.brand{display:flex;align-items:baseline;gap:22px;direction:ltr}
.brand .lat{font-family:'Orbitron';font-weight:800;font-size:44px;color:#0f6e56;letter-spacing:.5px}
.brand .ar{font-family:'Noto Kufi Arabic';font-weight:700;font-size:40px;color:#4b5f59}
.chip{display:inline-block;align-self:flex-start;margin-top:54px;padding:12px 28px;border-radius:999px;border:3px solid #0f6e56;color:#0f6e56;font-weight:700;font-size:30px}
.rtl{direction:rtl;text-align:right;font-family:'Noto Kufi Arabic','Space Grotesk',sans-serif}
.rtl .chip,.chip.rtl{align-self:flex-start}
h1{font-weight:700;line-height:1.22;color:#16302b}
h1 em{font-style:normal;color:#0f6e56}
h1.ar{font-family:'Noto Kufi Arabic','Space Grotesk',sans-serif;font-size:92px;line-height:1.38}
h1.fr{font-family:'Orbitron','Space Grotesk',sans-serif;font-weight:800;font-size:82px;line-height:1.16;letter-spacing:.5px}
.sub{margin-top:36px;font-size:40px;line-height:1.5;color:#4b5f59;font-weight:500}
.sub.ar{font-family:'Noto Kufi Arabic','Space Grotesk',sans-serif;font-weight:600;font-size:40px;line-height:1.7}
.grow{flex:1}
.foot{display:flex;align-items:center;justify-content:space-between;direction:ltr;gap:24px}
.pill{background:#0f6e56;color:#fff;font-weight:700;font-size:30px;padding:20px 34px;border-radius:999px;white-space:nowrap}
.pill.ar{font-family:'Noto Kufi Arabic','Space Grotesk',sans-serif;direction:rtl}
.url{font-family:'Space Grotesk';font-weight:700;font-size:30px;color:#0f6e56;white-space:nowrap}
.q{margin-top:40px;font-family:'Noto Kufi Arabic','Space Grotesk',sans-serif;font-weight:700;font-size:54px;line-height:1.6;color:#16302b}
.m{direction:ltr;unicode-bidi:isolate;display:inline-block;font-family:'Space Grotesk';font-weight:700}
.opts{margin-top:44px;display:grid;grid-template-columns:1fr 1fr;gap:26px}
.opt{display:flex;align-items:center;gap:22px;background:#fff;border:3px solid #cfe3dc;border-radius:26px;padding:26px 30px;font-size:44px;font-weight:700;font-family:'Noto Kufi Arabic','Space Grotesk',sans-serif}
.opt b{flex:none;width:68px;height:68px;border-radius:50%;background:#e4f1ec;color:#0f6e56;display:flex;align-items:center;justify-content:center;font-size:36px}
.note{margin-top:40px;font-family:'Noto Kufi Arabic','Space Grotesk',sans-serif;font-weight:600;font-size:34px;color:#4b5f59;line-height:1.6}
ul.pts{margin-top:44px;list-style:none;display:flex;flex-direction:column;gap:26px}
ul.pts li{display:flex;align-items:center;gap:24px;font-family:'Noto Kufi Arabic','Space Grotesk',sans-serif;font-weight:700;font-size:44px;line-height:1.5}
ul.pts li i{flex:none;width:60px;height:60px;border-radius:50%;background:#0f6e56;color:#fff;font-style:normal;display:flex;align-items:center;justify-content:center;font-family:'Space Grotesk';font-size:32px}
.story .wrap{padding:210px 84px 250px 104px}
.story h1.ar{font-size:104px}
.story .sub.ar{font-size:46px}
`;
const brand = `<div class="brand"><span class="lat">Na9ra Nal3ab</span><span class="ar">نقرا نلعب</span></div>`;
const footAr = `<div class="foot"><span class="url">www.na9ranal3ab.tn</span><span class="pill ar">مجانًا · دون تسجيل</span></div>`;
const footFr = `<div class="foot"><span class="pill">100 % gratuit · sans inscription</span><span class="url">www.na9ranal3ab.tn</span></div>`;
const shell = (inner, cls = '') => `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body class="${cls}"><div class="stripe"></div><div class="c1"></div><div class="c2"></div><div class="wrap">${inner}</div></body></html>`;
const optsAr = (o) => `<div class="opts rtl">${o.map((t, i) => `<div class="opt"><b>${['أ','ب','ج','د'][i]}</b><span class="m">${t}</span></div>`).join('')}</div>`;

const css2 = `
.opts.one{grid-template-columns:1fr;gap:18px;margin-top:34px}
.opts.one .opt{padding:18px 26px;font-size:38px}
.opts.one .opt b{width:58px;height:58px;font-size:30px}
.opt .t{font-family:'Noto Kufi Arabic','Space Grotesk',sans-serif}
.h2{margin-top:44px;font-family:'Noto Kufi Arabic','Space Grotesk',sans-serif;font-weight:700;font-size:64px;line-height:1.5;color:#0f6e56}
.box{margin-top:36px;background:#fff;border:3px solid #cfe3dc;border-radius:28px;padding:36px 40px;font-family:'Noto Kufi Arabic','Space Grotesk',sans-serif;font-weight:700;font-size:44px;line-height:1.75;color:#16302b}
.box .m{font-size:46px}
.warn{margin-top:30px;background:#fdf3e7;border:3px solid #f0c996;border-radius:28px;padding:32px 40px;font-family:'Noto Kufi Arabic','Space Grotesk',sans-serif;font-weight:700;font-size:40px;line-height:1.75;color:#5a3b10}
.pager{position:absolute;right:84px;top:92px;font-family:'Space Grotesk';font-weight:700;font-size:28px;color:#7b8f89}
`;
const shell2 = (inner, cls = '') => shell(inner, cls).replace('</style>', css2 + '</style>');
const optsArText = (o) => `<div class="opts one rtl">${o.map((t, i) => `<div class="opt"><b>${['أ','ب','ج','د'][i]}</b><span class="t">${t}</span></div>`).join('')}</div>`;
const plan = (chip, items, note) => shell2(`${brand}
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">${chip}</span>
      <h1 class="ar" style="margin-top:44px;font-size:78px">خطّة المراجعة<br><em>لهذا الأسبوع</em></h1>
      <ul class="pts">${items.map((t, i) => `<li><i>${i + 1}</i><span>${t}</span></li>`).join('')}</ul>
      <p class="note">${note}</p>
      <div class="grow"></div>
    </div>${footAr}`);

const cards = [
  { name: '01-test-parents-ar', w: 1080, h: 1350, html: shell2(`${brand}
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">اختبار المستوى</span>
      <h1 class="ar" style="margin-top:44px">في 7 دقائق،<br><em>اعرف مستوى ابنك</em><br>في الرياضيات</h1>
      <p class="sub ar">10 أسئلة · عدد على 20<br>والدروس التي تحتاج إلى مراجعة</p>
      <div class="grow"></div>
    </div>${footAr}`) },
  { name: '02-test-parents-fr', w: 1080, h: 1350, html: shell2(`${brand}
      <span class="chip">Test de niveau</span>
      <h1 class="fr" style="margin-top:48px">Où en est<br>ton enfant ?<br><em>10 questions<br>pour le savoir.</em></h1>
      <p class="sub">Une note sur 20, les chapitres à revoir,<br>et par où commencer. En 7 minutes.</p>
      <div class="grow"></div>${footFr}`) },
  { name: '03-question-lundi-6e', w: 1080, h: 1350, html: shell2(`${brand}
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">سؤال الإثنين · السنة السادسة · مناظرة 2017</span>
      <p class="q">سار فلّاح 40 دقيقة<br>بمعدّل سرعة <span class="m">60 km/h</span><br>كم كيلومترًا قطع؟</p>
      ${optsAr(['2400 km','40 km','1,5 km','100 km'])}
      <p class="note">اكتب جوابك في التعاليق. الحلّ مع الشرح هذا المساء.</p>
      <div class="grow"></div>
    </div>${footAr}`) },
  { name: '04-question-lundi-9e', w: 1080, h: 1350, html: shell2(`${brand}
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">سؤال الإثنين · السنة التاسعة</span>
      <p class="q">إذا كان <span class="m">a − b = 5</span> و <span class="m">ab = 3</span><br>فما قيمة <span class="m">a² + b²</span> ؟</p>
      ${optsAr(['19','31','25','28'])}
      <p class="note">اكتب جوابك في التعاليق. الحلّ مع الشرح هذا المساء.</p>
      <div class="grow"></div>
    </div>${footAr}`) },
  { name: '05-defi-weekend-9e', w: 1080, h: 1350, html: shell2(`${brand}
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">تحدّي نهاية الأسبوع · السنة التاسعة</span>
      <h1 class="ar" style="margin-top:44px">10 أسئلة<br>في الرياضيات.<br><em>كم تتحصّل على 20؟</em></h1>
      <p class="sub ar">اختبر نفسك في 7 دقائق،<br>ثمّ تحدَّ أصدقاءك بالرابط نفسه.</p>
      <div class="grow"></div>
    </div>${footAr}`) },
  { name: '06-bac-entraine-toi-fr', w: 1080, h: 1350, html: shell2(`${brand}
      <span class="chip">Bac 2027</span>
      <h1 class="fr" style="margin-top:48px">Arrête de regarder.<br><em>Entraîne-toi.</em></h1>
      <p class="sub">Des exercices par chapitre,<br>corrigés tout de suite.<br>Maths, physique, techno, info, philo.</p>
      <div class="grow"></div>${footFr}`) },
  { name: '07-enseignants-ar', w: 1080, h: 1350, html: shell2(`${brand}
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">للمعلّمين والأساتذة</span>
      <h1 class="ar" style="margin-top:44px;font-size:70px">اختبار قصير لكلّ درس،<br><em>مطابق للكتاب المدرسي</em></h1>
      <p class="sub ar">ترسله إلى قسمك برابط واحد.<br>الدروس قابلة للطباعة، والتمارين مع الإصلاح.</p>
      <div class="grow"></div>
    </div>${footAr}`) },
  { name: '08-cinq-preuves-ar', w: 1080, h: 1350, html: shell2(`${brand}
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <h1 class="ar" style="margin-top:56px;font-size:84px">راجع <em>وأنت تلعب</em></h1>
      <ul class="pts">
        <li><i>1</i><span>مجاني، ودون تسجيل</span></li>
        <li><i>2</i><span>مطابق للبرنامج الرسمي التونسي</span></li>
        <li><i>3</i><span>تمارين مع الإصلاح والشرح</span></li>
        <li><i>4</i><span>مواضيع مناظرتي السادسة والتاسعة</span></li>
        <li><i>5</i><span>الوليّ يتابع تقدّم ابنه يومًا بيوم</span></li>
      </ul>
      <div class="grow"></div>
    </div>${footAr}`) },
  { name: '09-story-test-ar', w: 1080, h: 1920, html: shell2(`${brand}
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">اختبار المستوى</span>
      <h1 class="ar" style="margin-top:60px">10 أسئلة.<br><em>كم تتحصّل<br>على 20؟</em></h1>
      <p class="sub ar">7 دقائق، دون تسجيل.<br>اضغط على الرابط.</p>
      <div class="grow"></div>
    </div>${footAr}`, 'story') },
  { name: '10-question-lundi-6e-partage', w: 1080, h: 1350, html: shell2(`${brand}
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">سؤال الإثنين · السنة السادسة</span>
      <p class="q" style="font-size:40px;margin-top:34px">وزّعنا 250 كتابًا بالتساوي على 8 رفوف،<br>ووضعنا الباقي في صندوق.<br>كم كتابًا في كلّ رفّ، وكم في الصندوق؟</p>
      ${optsArText(['في كلّ رفّ 30، وفي الصندوق 10','في كلّ رفّ 31، وفي الصندوق 4','في كلّ رفّ 32، وفي الصندوق 6','في كلّ رفّ 31، وفي الصندوق 2'])}
      <div class="grow"></div>
    </div>${footAr}`) },
  { name: '11-question-lundi-9e-denombrement', w: 1080, h: 1350, html: shell2(`${brand}
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">سؤال الإثنين · السنة التاسعة</span>
      <p class="q">كم عددًا يتكوّن<br>من رقمين فرديّين مختلفين؟</p>
      ${optsAr(['25','20','45','10'])}
      <p class="note">اكتب جوابك في التعاليق. الحلّ مع الشرح هذا المساء.</p>
      <div class="grow"></div>
    </div>${footAr}`) },
  { name: '12-plan-semaine-6e', w: 1080, h: 1350, html: plan('السنة السادسة · رياضيات', ['الأعداد الطبيعية','العمليّات على الأعداد الطبيعية','الأعداد العشرية'], 'ربع ساعة في اليوم: درس قصير، ثمّ تمرين مع الإصلاح.') },
  { name: '13-plan-semaine-9e', w: 1080, h: 1350, html: plan('السنة التاسعة · رياضيات', ['التعداد والحساب','الأعداد الحقيقية','الجذور التربيعية'], 'ربع ساعة في اليوم: درس قصير، ثمّ تمرين مع الإصلاح.') },
  { name: '14-sujet-corrige-9e-1', w: 1080, h: 1350, html: shell2(`${brand}<span class="pager">1 / 3</span>
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">الموضوع المصلَّح · مناظرة التاسعة 2018</span>
      <p class="q">ما إحداثيّتا منتصف القطعة <span class="m">[AC]</span><br>علمًا أنّ <span class="m">A(1 ; −1)</span> و <span class="m">C(1 ; 1)</span> ؟</p>
      ${optsAr(['(1 ; 0)','(2 ; 2)','(1 ; 1)','(2 ; 0)'])}
      <p class="note">فكّر قبل أن تمرّ إلى الصورة الموالية.</p>
      <div class="grow"></div>
    </div>${footAr}`) },
  { name: '14-sujet-corrige-9e-2', w: 1080, h: 1350, html: shell2(`${brand}<span class="pager">2 / 3</span>
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">الموضوع المصلَّح · مناظرة التاسعة 2018</span>
      <p class="h2">الحلّ</p>
      <div class="box">إحداثيّتا منتصف قطعة هما معدّلا إحداثيّتي طرفيها:<br><span class="m">((1 + 1)/2 ; (−1 + 1)/2) = (1 ; 0)</span></div>
      <p class="note">الجواب الصحيح: <span class="m">(1 ; 0)</span></p>
      <div class="grow"></div>
    </div>${footAr}`) },
  { name: '14-sujet-corrige-9e-3', w: 1080, h: 1350, html: shell2(`${brand}<span class="pager">3 / 3</span>
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">الموضوع المصلَّح · مناظرة التاسعة 2018</span>
      <p class="h2">الخطأ الشائع</p>
      <div class="warn">جمع الإحداثيّات دون القسمة على 2:<br>نجد <span class="m">(2 ; 0)</span> بدل <span class="m">(1 ; 0)</span></div>
      <p class="sub ar" style="margin-top:44px">الموضوع كاملًا، سؤالًا بسؤال، مع الإصلاح والشرح على الموقع.</p>
      <div class="grow"></div>
    </div>${footAr}`) },
  { name: '15-defi-vacances-ar', w: 1080, h: 1350, html: shell2(`${brand}
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">عطلة الشتاء · 14 – 27 ديسمبر</span>
      <h1 class="ar" style="margin-top:44px">تحدّي العطلة:<br><em>اختبار في كلّ مادّة</em></h1>
      <p class="sub ar">قارن أعدادك ببطاقة أعدادك،<br>واعرف من أين تبدأ الثلاثي الثاني.</p>
      <div class="grow"></div>
    </div>${footAr}`) },
  { name: '16-bulletin-parents-ar', w: 1080, h: 1350, html: shell2(`${brand}
    <div class="rtl" style="display:flex;flex-direction:column;flex:1">
      <span class="chip">للأولياء</span>
      <h1 class="ar" style="margin-top:44px;font-size:84px">وصلت بطاقة الأعداد؟<br><em>اعرف من أين تبدأ المراجعة</em></h1>
      <p class="sub ar">اختبار المستوى: 7 دقائق، مادّة بمادّة،<br>والدروس التي تحتاج إلى مراجعة.</p>
      <div class="grow"></div>
    </div>${footAr}`) },
];
(async () => {
  const browser = await chromium.launch();
  for (const c of cards) {
    const page = await browser.newPage({ viewport: { width: c.w, height: c.h }, deviceScaleFactor: 1 });
    await page.setContent(c.html, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(250);
    await page.screenshot({ path: path.join(OUT, c.name + '.png') });
    await page.close();
    console.log('ok', c.name);
  }
  await browser.close();
})();
