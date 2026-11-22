"""Compose content/mock-exams.json — les épreuves par matière de la 9ᵉ.

Sources de vérité lues ici, jamais recopiées à la main :
  - registres du gisement (quelle mission vient de quel exercice de quelle session) ;
  - transcriptions officielles (barème de chaque exercice : « ## Exercice N (X points) ») ;
  - fichiers d'exercice (existence, nombre de questions).
Usage : python3 -I compose-mock-exams.py <content-dir> [--check]
"""
import json, os, re, sys

CONTENT = sys.argv[1]
PARCOURS = "concours-9eme"
reg = {}
report = []

def exo(subject, chapter, slug):
    path = os.path.join(CONTENT, subject, chapter, "exercices", slug + ".json")
    if not os.path.exists(path):
        raise SystemExit(f"exercice introuvable : {path}")
    return f"{subject}/{chapter}/{slug}", len(json.load(open(path, encoding="utf-8"))["questions"])

def add(slug, subject, title, minutes, order, papers):
    total = sum(p["points"] for p in papers)
    nq = sum(p.pop("_q") for p in papers)
    reg[slug] = {"parcours": PARCOURS, "subject": subject, "title": title,
                 "durationMinutes": minutes, "displayOrder": order, "papers": papers}
    report.append(f"{slug:<34} {len(papers)} épreuves  {nq:>3} questions  {total:>3} points  {minutes} min")

def paper(ref, fr, en, ar, points):
    r, q = exo(*ref)
    return {"exercise": r, "label": {"fr": fr, "en": en, "ar": ar}, "points": points, "_q": q}

def gisement(subject):
    d = json.load(open(os.path.join(CONTENT, "programmes-officiels/sources-externes", f"web-9eme-base-{subject}", "gisement.json"), encoding="utf-8"))
    return {x["id"]: x for x in d["documents"]}, d["missions"]

def bareme(subject, session_file):
    """{numéro d'exercice: points ×10} lu dans la transcription officielle."""
    path = os.path.join(CONTENT, "programmes-officiels/examens-nationaux/9eme-base", subject, session_file)
    out = {}
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^## Exercice (\d+) \(([\d.,]+) points?\)", line)
        if m:
            pts = float(m.group(2).replace(",", "."))
            assert abs(pts * 10 - round(pts * 10)) < 1e-9, (path, line)
            out[int(m.group(1))] = int(round(pts * 10))
    return out

def session_exams(subject, name, order0, minutes, sessions, slug_prefix):
    """Une épreuve par session réelle : une mission par exercice du sujet, barème officiel."""
    docs, missions = gisement(subject)
    order = order0
    for year in sessions:
        doc = next((d for d in docs.values() if d.get("nature") == "examen" and d.get("session") == year
                    and d.get("filiere") in ("generale", "unique")), None)
        if doc is None:
            raise SystemExit(f"{subject} {year} : session absente du registre")
        fname = f"{year}-generale.md" if doc["filiere"] == "generale" else f"{year}.md"
        pts = bareme(subject, fname)
        by_ex = {}
        for m in missions:
            if m.get("statut") != "publiee":
                continue
            for s in m.get("sources") or []:
                d, n = s.split("#")
                if d == doc["id"]:
                    if not re.fullmatch(r"\d+", n):
                        raise SystemExit(f"{subject} {year} : mission {m['id']} ne couvre pas un exercice entier ({s})")
                    by_ex[int(n)] = m
        missing = sorted(set(pts) - set(by_ex))
        if missing:
            raise SystemExit(f"{subject} {year} : pas de mission pour l'exercice {missing}")
        assert sum(pts.values()) == 200, (subject, year, pts)
        papers = []
        for n in sorted(pts):
            m = by_ex[n]
            papers.append(paper((subject, m["chapitre"], m["fichier"][:-5]),
                                f"Exercice {n}", f"Exercise {n}", f"التمرين {n}", pts[n]))
        add(f"{slug_prefix}-concours-{year}", subject,
            {"fr": f"{name['fr']} · sujet du concours {year}",
             "en": f"{name['en']} · {year} national exam paper",
             "ar": f"{name['ar']} · موضوع مناظرة {year}"},
            minutes, order, papers)
        order += 1

def title_of(subject, chapter, slug):
    return json.load(open(os.path.join(CONTENT, subject, chapter, "exercices", slug + ".json"), encoding="utf-8"))["title"]

# ---------------------------------------------------------------- ARABE (100+)
AR = {"fr": "Arabe", "en": "Arabic", "ar": "العربيّة"}
AR_CH = "11-annales-subur"
for k in range(1, 5):
    base = 4 + 3 * (k - 1)
    slugs = [f"{base:02d}-ikhtibar-{k}-fahm", f"{base+1:02d}-ikhtibar-{k}-lugha", f"{base+2:02d}-ikhtibar-{k}-intaj"]
    if not all(os.path.exists(os.path.join(CONTENT, "arabic", AR_CH, "exercices", s + ".json")) for s in slugs):
        continue
    t = re.search(r"«(.+)»", title_of("arabic", AR_CH, slugs[0]))
    theme = re.sub(r"[ً-ْ]", "", t.group(1)) if t else ""
    add(f"arabe-9eme-epreuve-{k}", "arabic",
        {"fr": f"Arabe · épreuve blanche n° {k}", "en": f"Arabic · mock paper {k}",
         "ar": f"العربيّة · اختبار تجريبيّ {k}" + (f": «{theme}»" if theme else "")},
        60, 100 + k,
        [paper(("arabic", AR_CH, slugs[0]), "I. Compréhension du texte argumentatif", "I. Understanding the text", "الفهم وبناء المعنى", 40),
         paper(("arabic", AR_CH, slugs[1]), "II. Langue", "II. Language", "اللّغة", 60),
         paper(("arabic", AR_CH, slugs[2]), "III. Production d'un texte argumentatif", "III. Writing", "إنتاج نصّ حجاجيّ", 100)])

AR_ANNALES = [
    (2026, "07-examen-2026-generale-fahm-fann", "11-examen-2026-generale-intaj-dahd-i3tiqad",
     [("18-dalalat-az-zaman", "06-examens-2022-2026-zaman", "دلالة الزّمان", "le temps"),
      ("13-at-tasghir", "06-examens-2025-2026-tasghir-qubayl-fann-shair", "التّصغير", "le diminutif")]),
    (2025, "08-examen-2025-generale-fahm-ilm-wal-amal", "10-examen-2025-generale-intaj-ta3dil-al-mawqif",
     [("19-al-adad-wal-madud", "06-examen-2025-adad-wal-madud", "العدد والمعدود", "le nombre"),
      ("12-al-maqsur-wal-manqus-wal-mamdud", "06-examens-2025-2026-maqsur-mamdud-muthanna-jam3", "المقصور والممدود", "le nom abrégé et prolongé")]),
    (2024, "09-examen-2024-generale-fahm-tabaq-99", "09-examen-2024-generale-intaj-ankar-al-ananiyya",
     [("15-al-alaqat-bayna-al-jumal", "06-examens-2024-2025-rabt-wa-i3tirad", "الرّبط والاعتراض", "les liens entre phrases"),
      ("05-sarf-al-mizan", "07-examens-2024-2026-maani-az-ziyada-istahala-tujammil", "معاني الزّيادة", "les formes augmentées")]),
    (2023, "10-examen-2023-generale-fahm-hayat-bila-fann", "08-examen-2023-generale-intaj-iqna3-bi-athar-al-funun",
     [("14-an-nisba-wal-masdar-as-sinai", "06-examens-2023-2024-nisba-masdar-sinai-inna", "النّسبة والمصدر الصّناعيّ", "la relation"),
      ("16-al-istifham", "06-examens-2023-2026-istifham", "الاستفهام", "l'interrogation")]),
]
for i, (year, fahm, intaj, lang) in enumerate(AR_ANNALES):
    papers = [paper(("arabic", "10-fahm-wa-intaj", fahm), f"I. Compréhension — texte de {year}", f"I. Understanding — {year} text", f"الفهم وبناء المعنى — نصّ {year}", 40)]
    for ch, slug, ar, fr in lang:
        papers.append(paper(("arabic", ch, slug), f"II. Langue — {fr}", "II. Language", f"اللّغة — {ar}", 30))
    papers.append(paper(("arabic", "09-al-intaj-al-kitabi", intaj), f"III. Production — sujet de {year}", f"III. Writing — {year} task", f"إنتاج نصّ حجاجيّ — موضوع {year}", 100))
    add(f"arabe-9eme-annales-{year}", "arabic",
        {"fr": f"Arabe · annales {year} (texte et production de {year}, langue des sessions récentes)",
         "en": f"Arabic · {year} past paper (text and writing task of {year}, language from recent sessions)",
         "ar": f"العربيّة · من مناظرة {year} (نصّ وإنتاج {year}، ولغة الدّورات الأخيرة)"},
        60, 111 + i, papers)

# ------------------------------------------------------------- FRANÇAIS (200+)
FR_CH = "10-annales-sujets-types"
for k in range(1, 5):
    base = 4 + 3 * (k - 1)
    slugs = [f"{base:02d}-epreuve-{k}-comprehension", f"{base+1:02d}-epreuve-{k}-langue", f"{base+2:02d}-epreuve-{k}-production"]
    if not all(os.path.exists(os.path.join(CONTENT, "french", FR_CH, "exercices", s + ".json")) for s in slugs):
        continue
    t = re.search(r"— (.+?) ⭐", title_of("french", FR_CH, slugs[0]))
    theme = t.group(1).strip() if t else ""
    add(f"francais-9eme-epreuve-{k}", "french",
        {"fr": f"Français · épreuve blanche n° {k}" + (f" : « {theme} »" if theme else ""),
         "en": f"French · mock paper {k}",
         "ar": f"الفرنسيّة · اختبار تجريبيّ {k}"},
        60, 200 + k,
        [paper(("french", FR_CH, slugs[0]), "I. Compréhension", "I. Reading comprehension", "فهم النصّ", 70),
         paper(("french", FR_CH, slugs[1]), "II. Langue", "II. Language", "اللّغة", 60),
         paper(("french", FR_CH, slugs[2]), "III. Production écrite", "III. Writing", "الإنتاج الكتابيّ", 70)])

FR_ANNALES = [
    (2026, "06-examen-2026-g-comprehension-artiste-avant-le-concert",
     [("06-concordance-des-temps", "06-examens-2010-2026-imparfait-passe-simple-plus-que-parfait", "les temps du récit"),
      ("11-groupe-nominal-et-attribut", "06-examens-2016-2026-enrichir-le-groupe-nominal", "enrichir le groupe nominal")],
     ("08-types-de-textes-et-production-ecrite", "06-examens-2005-2026-production-reussite-et-portrait")),
    (2025, "07-examen-2025-g-comprehension-portrait-serveuse",
     [("02-propositions-subordonnees", "06-examens-2002-2025-cause-but-consequence-intensite", "cause, but, conséquence"),
      ("14-homophones-et-adverbes-en-ment", "06-examens-2002-2025-former-l-adverbe-en-ment", "l'adverbe en -ment")],
     ("04-discours-direct-et-indirect", "06-examens-2002-2025-production-recit-avec-dialogue")),
    (2023, "08-examen-2023-g-comprehension-enfant-face-a-l-incendie",
     [("03-voix-active-et-passive", "06-examens-2007-2023-voix-active-et-passive", "voix active et passive"),
      ("07-lexique-et-figures-de-style", "07-examens-2019-2026-synonyme-en-contexte-et-autre-sens", "synonyme en contexte")],
     ("09-comprehension-production-ecrite", "11-examens-2009-2025-production-projet-metier-justifier")),
]
for i, (year, comp, lang, prod) in enumerate(FR_ANNALES):
    papers = [paper(("french", "09-comprehension-production-ecrite", comp), f"I. Compréhension — texte de {year}", f"I. Reading — {year} text", f"فهم النصّ — نصّ {year}", 70)]
    for ch, slug, fr in lang:
        papers.append(paper(("french", ch, slug), f"II. Langue — {fr}", "II. Language", "اللّغة", 30))
    papers.append(paper(("french", prod[0], prod[1]), "III. Production écrite — sujets des examens", "III. Writing — exam tasks", "الإنتاج الكتابيّ — مواضيع الامتحانات", 70))
    add(f"francais-9eme-annales-{year}", "french",
        {"fr": f"Français · annales {year} (compréhension de {year}, langue et production des sessions d'examen)",
         "en": f"French · {year} past paper (reading of {year}, language and writing from exam sessions)",
         "ar": f"الفرنسيّة · من امتحان {year} (فهم نصّ {year}، ولغة وإنتاج من دورات الامتحان)"},
        75, 211 + i, papers)

# ------------------------------------------------------- MATHÉMATIQUES (300+)
MATH = {"fr": "Mathématiques", "en": "Mathematics", "ar": "الرياضيات"}
math_sessions = [y for y in (2026, 2025, 2024, 2023, 2022) if "--with-math-2022-2026" in sys.argv] + [2021, 2020, 2019, 2018, 2017]
session_exams("math", MATH, 301, 90, math_sessions, "maths-9eme")

# ----------------------------------------------------------------- SVT (400+)
SVT = {"fr": "SVT", "en": "Life and earth sciences", "ar": "علوم الحياة والأرض"}
session_exams("sciences-vie-terre", SVT, 401, 45, [2026, 2025, 2024, 2022, 2021, 2020], "svt-9eme")

# -------------------------------------------------------------- ANGLAIS (500+)
EN_ANNALES = [
    (2026, "06-exam-2026-g-reading-money-values",
     [("02-past-tenses", "06-exams-2006-2026-present-perfect-or-simple-past", "present perfect or simple past"),
      ("08-relative-clauses-comparatives", "06-exams-2002-2026-relative-pronouns", "relative pronouns")],
     ("04-modals", "07-exams-2011-2026-writing-advise-warn-set-rules")),
    (2025, "07-exam-2025-g-reading-bike-bus",
     [("07-reported-speech", "08-exams-2011-2026-one-root-several-words", "word building"),
      ("08-relative-clauses-comparatives", "08-exams-2002-2026-building-the-comparison", "comparisons")],
     ("09-reading-comprehension-writing", "15-exams-2001-2025-writing-describe-persuade-opinion")),
    (2024, "08-exam-2024-g-reading-young-blind-pianist",
     [("02-past-tenses", "07-exams-2001-2026-simple-past-or-past-progressive", "simple past or past progressive"),
      ("09-reading-comprehension-writing", "13-exams-2018-2026-the-right-word-in-context", "the right word in context")],
     ("02-past-tenses", "08-exams-2002-2023-writing-telling-a-past-event")),
]
for i, (year, reading, lang, writing) in enumerate(EN_ANNALES):
    papers = [paper(("english", "09-reading-comprehension-writing", reading), f"I. Compréhension — texte de {year}", f"I. Reading comprehension — {year} text", f"فهم النصّ — نصّ {year}", 60)]
    for ch, slug, en in lang:
        papers.append(paper(("english", ch, slug), "II. Langue", f"II. Language — {en}", "اللّغة", 40))
    papers.append(paper(("english", writing[0], writing[1]), "III. Production écrite", "III. Writing — exam tasks", "الإنتاج الكتابيّ", 60))
    add(f"anglais-9eme-annales-{year}", "english",
        {"fr": f"Anglais · annales {year} (texte de {year}, langue et production des sessions d'examen)",
         "en": f"English · {year} past paper ({year} reading text, language and writing from exam sessions)",
         "ar": f"الإنجليزيّة · من امتحان {year} (نصّ {year}، ولغة وإنتاج من دورات الامتحان)"},
        60, 501 + i, papers)

print("\n".join(report))
print(f"{len(reg)} examens")
if "--check" not in sys.argv:
    out = os.path.join(CONTENT, "mock-exams.json")
    json.dump(reg, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(out, "a", encoding="utf-8").write("\n")
    print("écrit :", out)
