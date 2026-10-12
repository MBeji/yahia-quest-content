# mission : constructeurs de questions + contrôles mécaniques + écriture JSON (format identique aux missions publiées)
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.dirname(HERE)
REG = json.load(open(os.path.join(WORK, "ref", "misconceptions.origin.json"), encoding="utf-8"))
_comp = json.load(open(os.path.join(WORK, "ref", "competences.origin.json"), encoding="utf-8"))
COMP = {c["id"] for c in _comp["competencies"]}
CHAPTER_DIR = os.environ.get("L17_OUT", "/home/user/wt-gis/content/math/18-quadrilateres/exercices")

DIAC = re.compile("[ً-ْٰـ]")
ARABIC_INDIC = re.compile("[٠-٩۰-۹]")
AR = re.compile("[؀-ۿ]")


def strip_diac(s):
    return DIAC.sub("", s)


def strip_svg(s):
    return re.sub(r"<svg.*?</svg>", "", s, flags=re.S)


class Mission:
    def __init__(self, number, session, ex, slug, title, difficulty=4):
        self.number = number
        self.session = session
        self.ex = ex
        self.slug = slug
        self.title = title
        self.difficulty = difficulty
        self.qs = []

    # ---- constructeurs ---------------------------------------------------------------------------------------------
    def mcq(self, prompt, opts, key, expl, diff, comps, svg=None):
        """opts : liste de (texte, étiquette|None) dans l'ordre d'affichage ; key : indice (0..3) de la bonne option."""
        assert len(opts) == 4, "4 options"
        options = []
        for i, (text, tag) in enumerate(opts):
            o = {"id": "abcd"[i], "text": text}
            if tag:
                assert i != key, "la bonne option reste sans étiquette"
                assert tag in REG, f"étiquette inconnue {tag}"
                o["misconceptionTag"] = tag
            options.append(o)
        p = prompt if svg is None else prompt + "\n" + svg
        self.qs.append({"prompt": p, "options": options, "correctOption": "abcd"[key], "explanation": expl, "difficulty": diff, "competencies": list(comps)})

    def numeric(self, prompt, value, unit, expl, diff, comps, svg=None):
        p = prompt if svg is None else prompt + "\n" + svg
        ak = {"value": value}
        if unit:
            ak["unit"] = unit
        self.qs.append({"type": "numeric", "prompt": p, "answerKey": ak, "explanation": expl, "difficulty": diff, "competencies": list(comps)})

    def multi(self, prompt, opts, correct, expl, diff, comps, svg=None):
        """opts : liste de textes (3..6) ; correct : liste d'indices justes."""
        n = len(opts)
        assert 3 <= n <= 6 and 2 <= len(correct) <= 5 and len(correct) < n
        ids = "abcdef"
        p = prompt if svg is None else prompt + "\n" + svg
        self.qs.append({
            "type": "multi", "prompt": p,
            "options": [{"id": ids[i], "text": t} for i, t in enumerate(opts)],
            "answerKey": {"correct": [ids[i] for i in correct]},
            "explanation": expl, "difficulty": diff, "competencies": list(comps),
        })

    # ---- sortie ----------------------------------------------------------------------------------------------------
    def as_json(self):
        return {
            "title": self.title,
            "difficulty": self.difficulty,
            "mode": "challenge" if self.difficulty == 4 else ("boss" if self.difficulty == 3 else "practice"),
            "xpReward": {4: 300, 3: 120, 2: 75}[self.difficulty],
            "rewardCoins": {4: 60, 3: 30, 2: 15}[self.difficulty],
            "displayOrder": self.number,
            "questions": self.qs,
        }

    def path(self):
        return os.path.join(CHAPTER_DIR, f"{self.number}-examen-{self.session}-ex{self.ex}-{self.slug}.json")

    def write(self, path=None):
        path = path or self.path()
        with open(path, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.as_json(), ensure_ascii=False, indent=2) + "\n")
        return path

    # ---- contrôles -------------------------------------------------------------------------------------------------
    def check(self, verbose=True):
        problems = []

        def bad(i, msg):
            problems.append(f"Q{i + 1}: {msg}")

        ramp = [q["difficulty"] for q in self.qs]
        for i in range(1, len(ramp)):
            if ramp[i] < ramp[i - 1]:
                bad(i, f"rampe {ramp[i - 1]} -> {ramp[i]}")
        if self.difficulty == 4 and 3 not in ramp:
            problems.append("aucune question d3 dans une mission d4")
        keys = []
        for i, q in enumerate(self.qs):
            texts = [q["prompt"], q["explanation"]] + [o["text"] for o in q.get("options", [])]
            full = "\n".join(texts)
            if ARABIC_INDIC.search(full):
                bad(i, "chiffre arabo-indien")
            if re.search(r"\\[a-zA-Z]+", strip_svg(full)) or "$" in strip_svg(full):
                bad(i, "résidu LaTeX / dollar")
            if re.search(r"\d \d{3}", strip_svg(full)):
                bad(i, "groupe de chiffres avec espace simple")
            if re.search(r"\b[A-Za-z]'", strip_svg(full)):
                bad(i, "apostrophe collée à une lettre (nom de point)")
            for grp in re.findall(r"[\(\[\{][^()\[\]{}]*[\)\]\}]", strip_svg(full)):
                if "،" in grp and not AR.search(grp.replace("،", "")):
                    bad(i, f"virgule arabe dans un groupe mathématique : {grp}")
            if len(q["explanation"]) < 25:
                bad(i, "explication trop courte")
            if self.difficulty == 4 and q.get("type") != "multi" and "الخطأ الشائع" not in q["explanation"]:
                bad(i, "« الخطأ الشائع » absent de l'explication (obligatoire en d4)")
            if re.search(r"\(\s*[a-dA-D]\s*\)|الخيار\s*[a-d]\b|الجواب\s*[a-d]\b", q["explanation"]):
                bad(i, "l'explication cite une lettre d'option")
            for c in q["competencies"]:
                if c not in COMP:
                    bad(i, f"compétence inconnue {c}")
            t = q.get("type", "mcq")
            if t == "mcq":
                opts = q["options"]
                key = q["correctOption"]
                keys.append(key)
                kt = next(o["text"] for o in opts if o["id"] == key)
                lens = {o["id"]: len(strip_diac(strip_svg(o["text"]))) for o in opts}
                lk = lens[key]
                if all(lens[o["id"]] < lk for o in opts if o["id"] != key):
                    bad(i, f"la clé est strictement la plus longue {lens}")
                texts_n = [re.sub(r"\s+", " ", o["text"]).strip() for o in opts]
                if len(set(texts_n)) != 4:
                    bad(i, "options en double")
                for o in opts:
                    if "misconceptionTag" in o and o["id"] == key:
                        bad(i, "la clé porte une étiquette")
                # coche collée à un distracteur
                for m in re.finditer(r"(\S+(?:\s\S+){0,3})\s*✓", q["explanation"]):
                    before = re.sub(r"\s+", " ", m.group(1)).strip()
                    for o in opts:
                        if o["id"] == key:
                            continue
                        tt = re.sub(r"\s+", " ", o["text"]).strip()
                        if before == tt or before.endswith(" " + tt) or before.endswith("= " + tt):
                            bad(i, f"✓ suit l'option fausse « {tt} »")
            if t == "multi":
                keys.append("multi")
        if verbose:
            from collections import Counter
            cnt = Counter(k for k in keys if k != "multi")
            print(f"[{self.number}] {len(self.qs)} questions, rampe {ramp}")
            print(f"[{self.number}] clés mcq : {dict(sorted(cnt.items()))}")
            for p in problems:
                print("  !!", p)
            if not problems:
                print("  contrôles mécaniques : rien à signaler")
        return problems

    def review(self, expl=None):
        for i, q in enumerate(self.qs):
            t = q.get("type", "mcq")
            print(f"--- Q{i + 1} [{t}] d{q['difficulty']}")
            print("  P:", strip_svg(q["prompt"]).replace("\n", "\n     "))
            if t == "mcq":
                for o in q["options"]:
                    mark = "*" if o["id"] == q["correctOption"] else " "
                    print(f"   {mark}{o['id']}: {o['text']}  {('<' + o['misconceptionTag'] + '>') if 'misconceptionTag' in o else ''}")
            elif t == "numeric":
                print("   NUM:", q["answerKey"])
            elif t == "multi":
                for o in q["options"]:
                    mark = "*" if o["id"] in q["answerKey"]["correct"] else " "
                    print(f"   {mark}{o['id']}: {o['text']}")
            e = q["explanation"]
            print("  E:", e if expl is None else e[:expl])


def lens_report(m):
    for i, q in enumerate(m.qs):
        if q.get("type", "mcq") == "mcq":
            print(i + 1, {o["id"]: len(strip_diac(strip_svg(o["text"]))) for o in q["options"]}, "clé", q["correctOption"])
