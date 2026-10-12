# Figures de la mission 36 (2013 ex4) : coordonnées exactes, scènes par question.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from geo import *
from figlib import Fig, INK, ACC, MUTED

O = pt(0, 0); A = pt(-3, 0); B = pt(3, 0); C = pt(0, 3)
D = sym(A, C)
G = inter(B, C, O, D)
E = mid(B, D)
M_EC = mid(E, C)   # milieu de [EC]
M_OC = mid(O, C)   # milieu de [OC]

# --- vérifications des données officielles
assert same(O, mid(A, B)) and perp(O, C, A, B) and zero(d2(O, C) - 9)
assert same(D, pt(3, 6)) and same(G, pt(1, 2)) and same(E, pt(3, 3))
assert same(G, centroid(A, B, D))
assert collinear(A, G, E) and between(E, B, D)
assert perp(A, B, B, D) and zero(d2(B, D) - 36) and zero(d2(A, E) - 45)
assert same(inter(A, E, O, D), G)

PTS = {"A": A, "B": B, "O": O, "C": C, "D": D, "G": G, "E": E, "M": M_EC, "N": M_OC}
FIT = ["A", "B", "D", "O", "C"]


def base(fit=FIT, W=300, H=250):
    return Fig(PTS, W=W, H=H, margin=34, fit=fit)


def tri_ABD(f, color=INK, width=2.4):
    f.poly(["A", "B", "D"], color=color, width=width)


def svg_q1():
    f = base()
    f.seg("A", "B"); f.seg("O", "C", color=ACC, ext0=0.0, ext1=0.0); f.seg("A", "D")
    for n in "ABODC": f.dot(n)
    f.dot("C", ACC)
    for n in "ABO": f.label(n)
    f.label("C", ACC); f.label("D")
    return f.svg("النقاط A و B و O و C و D في المستوي")


def svg_q2():
    f = base(); tri_ABD(f)
    f.seg("B", "C", color=ACC); f.seg("O", "D", color=ACC)
    f.ticks("A", "O", 1); f.ticks("O", "B", 1)
    for n in "ABDOC": f.dot(n)
    f.dot("G", ACC)
    for n in "ABDOC": f.label(n)
    f.label("G", ACC)
    return f.svg("المثلّث ABD والمستقيمان (BC) و (OD) المتقاطعان في G")


def svg_q3():
    f = base(); tri_ABD(f)
    f.seg("B", "C", color=MUTED, width=1.6, dash="5 4"); f.seg("O", "D", color=MUTED, width=1.6, dash="5 4")
    f.seg("A", "E", color=ACC)
    for n in "ABDOC": f.dot(n)
    f.dot("G", ACC); f.dot("E", ACC)
    for n in "ABDOC": f.label(n)
    f.label("G", ACC); f.label("E", ACC)
    return f.svg("المثلّث ABD ومركز ثقله G والمستقيم (AG) الذي يقطع [BD] في E")


def svg_q4():
    f = base(); tri_ABD(f)
    f.seg("O", "C", color=ACC, width=2.4)
    f.ticks("A", "O", 1); f.ticks("O", "B", 1)
    for n in "ABDOC": f.dot(n)
    for n in "ABDOC": f.label(n)
    return f.svg("المثلّث ABD والقطعة [OC] الواصلة بين O و C")


def svg_q5():
    f = base(); tri_ABD(f)
    f.seg("A", "E", color=ACC)
    f.right_angle("B", "A", "D")
    f.ticks("B", "E", 1); f.ticks("E", "D", 1)
    for n in "ABD": f.dot(n)
    f.dot("E", ACC)
    for n in "ABD": f.label(n)
    f.label("E", ACC)
    return f.svg("المثلّث ABD القائم في B و E منتصف [BD]")


def svg_q6():
    f = base(); tri_ABD(f)
    f.seg("O", "C", color=ACC, width=2.4)
    for n in "ABDOC": f.dot(n)
    for n in "ABDOC": f.label(n)
    return f.svg("المثلّث ABD والقطعة [OC] الواصلة بين O و C")


def svg_q7():
    f = base(); tri_ABD(f)
    f.seg("A", "E", color=ACC)
    f.right_angle("B", "A", "D")
    for n in "ABD": f.dot(n)
    f.dot("G", ACC); f.dot("E", ACC)
    for n in "ABD": f.label(n)
    f.label("G", ACC); f.label("E", ACC)
    return f.svg("المثلّث ABD القائم في B ومركز ثقله G والمستقيم (AG) الذي يقطع [BD] في E")


def svg_q8():
    f = base(); tri_ABD(f, color=MUTED, width=1.6)
    f.fill(["O", "E", "D", "C"], ACC, 0.12)
    f.poly(["O", "E", "D", "C"], color=INK, width=2.4)
    f.ticks("A", "O", 1); f.ticks("O", "B", 1)
    f.ticks("B", "E", 2); f.ticks("E", "D", 2)
    f.ticks("A", "C", 3); f.ticks("C", "D", 3)
    for n in "ABD": f.dot(n, MUTED)
    for n in "OEC": f.dot(n, ACC)
    for n in "ABD": f.label(n)
    for n in "OEC": f.label(n, ACC)
    return f.svg("المثلّث ABD ومنتصفات أضلاعه O و E و C والرباعي OEDC")


def svg_q9():
    f = base(); tri_ABD(f, color=MUTED, width=1.6)
    f.poly(["O", "E", "D", "C"], color=INK, width=2.4)
    f.seg("O", "D", color=ACC); f.seg("E", "C", color=ACC)
    for n in "ABD": f.dot(n, MUTED)
    for n in "OEC": f.dot(n)
    f.dot("M", ACC)
    for n in "ABD": f.label(n)
    for n in "OEC": f.label(n)
    f.label("M", ACC)
    return f.svg("متوازي الأضلاع OEDC وقطراه [OD] و [EC] المتقاطعان في M")


def svg_q10():
    f = base(); tri_ABD(f)
    f.poly(["O", "E", "C"], color=ACC, width=2.2)
    f.ticks("A", "O", 1); f.ticks("O", "B", 1)
    f.ticks("B", "E", 2); f.ticks("E", "D", 2)
    f.ticks("A", "C", 3); f.ticks("C", "D", 3)
    for n in "ABD": f.dot(n)
    for n in "OEC": f.dot(n, ACC)
    for n in "ABD": f.label(n)
    for n in "OEC": f.label(n, ACC)
    return f.svg("المثلّث ABD ومنتصفات أضلاعه O و E و C والقطع التي تصل بينها")


def svg_q11():
    f = base(); tri_ABD(f, color=MUTED, width=1.6)
    f.poly(["O", "E", "C", "A"], color=MUTED, width=1.6)
    f.fill(["O", "E", "C"], ACC, 0.12)
    f.poly(["O", "E", "C"], color=INK, width=2.4)
    f.seg("E", "A", color=ACC, width=2.4)
    for n in "ABD": f.dot(n, MUTED)
    for n in "OEC": f.dot(n)
    f.dot("G", ACC)
    for n in "ABD": f.label(n)
    for n in "OEC": f.label(n)
    f.label("G", ACC)
    return f.svg("المثلّث OEC والمستقيم (EG) الذي يمرّ من G")


def svg_q12():
    f = base(); tri_ABD(f, color=MUTED, width=1.6)
    f.fill(["O", "E", "C"], ACC, 0.12)
    f.poly(["O", "E", "C"], color=INK, width=2.4)
    f.seg("O", "D", color=ACC, width=2.2); f.seg("E", "A", color=ACC, width=2.2)
    for n in "ABD": f.dot(n, MUTED)
    for n in "OEC": f.dot(n)
    f.dot("G", ACC)
    for n in "ABD": f.label(n)
    for n in "OEC": f.label(n)
    f.label("G", ACC)
    return f.svg("المثلّث OEC والمستقيمان (OG) و (EG)")


if __name__ == "__main__":
    import json
    out = {"questions": []}
    for fn in (svg_q1, svg_q2, svg_q3, svg_q4, svg_q5, svg_q6, svg_q7, svg_q8, svg_q9, svg_q10, svg_q11, svg_q12):
        out["questions"].append({"prompt": "Q " + fn.__name__ + "\n" + fn(), "difficulty": 1})
    json.dump(out, open("tmp/m36_figs.json", "w", encoding="utf-8"), ensure_ascii=False)
    print("figures ok")
