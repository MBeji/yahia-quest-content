# Figures de la mission 37 (2016 ex4) : deux demi-cercles, coordonnées exactes.
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from geo import *
from figlib import Fig, INK, ACC, MUTED

A = pt(0, 0); B = pt(6, 0); C = pt(8, 0)
I = mid(A, B); O = mid(A, C)
D = pt(3, 3)              # médiatrice de [AB] ∩ demi-cercle de diamètre [AB]
E = pt(4, 4)              # (AD) ∩ demi-cercle de diamètre [AC]
F = inter(B, D, O, E)
G = centroid(A, B, D)
N = mid(O, A)
H = foot(G, D, N)
K1 = mid(E, C)

# --- vérifications des données officielles
assert on_circle(D, I, 3) and perp(I, D, A, B) and dist(D, A) == dist(D, B) == 3 * sqrt(2)
assert perp(D, A, D, B)
assert collinear(A, D, E) and on_circle(E, O, 4) and perp(E, A, E, C) and dist(E, A) == dist(E, C) == 4 * sqrt(2)
assert same(F, pt(4, 2)) and same(F, mid(O, E)) and dist(O, F) == 2 and between(F, B, D)
assert same(G, pt(3, 1)) and same(N, pt(2, 0))
assert collinear(N, G, F) and same(G, mid(N, F))
assert same(H, pt(R(12, 5), R(6, 5))) and collinear(B, G, H) and perp(B, G, D, N)

PTS = {"A": A, "B": B, "C": C, "I": I, "O": O, "D": D, "E": E, "F": F, "G": G, "N": N, "H": H}
FIT = ["A", "C", "E"]


def base(W=300, H_=190):
    return Fig(PTS, W=W, H=H_, margin=26, fit=FIT)


def semis(f, which="both", color=MUTED, width=1.5):
    if which in ("both", "small"):
        f.arc("I", 3, 0, 180, color=color, width=width)
    if which in ("both", "big"):
        f.arc("O", 4, 0, 180, color=color, width=width)


def svg_q1():
    f = base(); semis(f, "small", INK, 2.2)
    f.seg("A", "B"); f.seg("I", "D", color=ACC, ext0=0.0, ext1=0.0)
    f.poly(["A", "B", "D"], color=INK, width=2.4)
    f.ticks("A", "I", 1); f.ticks("I", "B", 1)
    for n in "ABI": f.dot(n)
    f.dot("D", ACC)
    for n in "ABI": f.label(n)
    f.label("D", ACC)
    return f.svg("نصف الدائرة التي قطرها [AB] والموسّط العمودي للقطعة [AB] والنقطة D والمثلّث ABD")


def svg_q2():
    f = base(); semis(f, "small", MUTED, 1.5)
    f.poly(["A", "B", "D"], color=INK, width=2.4)
    f.right_angle("D", "A", "B")
    f.ticks("D", "A", 1); f.ticks("D", "B", 1)
    for n in "AB": f.dot(n)
    f.dot("D", ACC)
    for n in "AB": f.label(n)
    f.label("D", ACC)
    return f.svg("المثلّث ABD القائم ومتقايس الضلعين رأسه D")


def svg_q3():
    f = base(); semis(f, "both", MUTED, 1.5)
    f.seg("A", "C"); f.poly(["A", "E", "C"], color=INK, width=2.4)
    f.seg("A", "D", color=ACC, width=2.4); f.seg("D", "B", color=MUTED, width=1.6, dash="5 4")
    f.right_angle("E", "A", "C")
    for n in "ABC": f.dot(n)
    f.dot("D", ACC); f.dot("E", ACC)
    for n in "ABC": f.label(n)
    f.label("D", ACC); f.label("E", ACC)
    return f.svg("نصفا الدائرتين والمثلّث AEC القائم في E والنقطة D على المستقيم (AE)")


def svg_q4():
    f = base(); semis(f, "big", MUTED, 1.5)
    f.seg("A", "C"); f.poly(["A", "E", "C"], color=INK, width=2.4)
    f.right_angle("E", "A", "C")
    f.ticks("E", "A", 1); f.ticks("E", "C", 1)
    for n in "AC": f.dot(n)
    f.dot("E", ACC)
    for n in "AC": f.label(n)
    f.label("E", ACC)
    return f.svg("المثلّث AEC القائم ومتقايس الضلعين رأسه E")


def svg_q5():
    f = base(); semis(f, "both", MUTED, 1.4)
    f.seg("A", "C", width=2.0)
    f.seg("O", "E", color=INK, width=2.2); f.seg("B", "D", color=ACC, width=2.4)
    f.poly(["A", "D", "E"], color=MUTED, width=1.4, closed=False)
    for n in "ABCO": f.dot(n)
    f.dot("D", ACC); f.dot("E", ACC); f.dot("F", ACC)
    for n in "ABCO": f.label(n)
    f.label("D", ACC); f.label("E", ACC); f.label("F", ACC)
    return f.svg("نصفا الدائرتين والقطعتان [OE] و [BD] المتقاطعتان في F")


def svg_q6():
    f = base(); semis(f, "small", MUTED, 1.5)
    f.poly(["A", "B", "D"], color=INK, width=2.4)
    f.right_angle("D", "A", "B")
    f.seg("D", "I", color=ACC, width=2.4)
    for n in "AB": f.dot(n)
    f.dot("I"); f.dot("D")
    f.dot("G", ACC)
    for n in "ABID": f.label(n)
    f.label("G", ACC)
    return f.svg("المثلّث ABD القائم في D ومنتصف وتره I ومركز ثقله G")


def svg_q7():
    f = base(); semis(f, "both", MUTED, 1.3)
    f.seg("A", "C", width=2.0)
    f.poly(["A", "D", "E"], color=MUTED, width=1.4, closed=False)
    f.fill(["E", "F", "G", "D"], ACC, 0.12)
    f.poly(["E", "F", "G", "D"], color=INK, width=2.4)
    f.seg("O", "E", color=MUTED, width=1.4)
    f.seg("D", "I", color=MUTED, width=1.4)
    for n in "ABCOI": f.dot(n, MUTED)
    f.dot("D"); f.dot("E")
    f.dot("F", ACC); f.dot("G", ACC)
    for n in "ABCO": f.label(n)
    f.label("D"); f.label("E"); f.label("F", ACC); f.label("G", ACC)
    return f.svg("الرباعي EFGD ونصفا الدائرتين")


def svg_q8():
    f = base(); semis(f, "big", MUTED, 1.3)
    f.seg("A", "C", width=2.0)
    f.poly(["O", "A", "E"], color=INK, width=2.4)
    f.seg("N", "F", color=ACC, width=2.4)
    f.ticks("N", "A", 1); f.ticks("N", "O", 1)
    f.ticks("O", "F", 2); f.ticks("F", "E", 2)
    for n in "AC": f.dot(n)
    f.dot("O"); f.dot("E")
    f.dot("N", ACC); f.dot("F", ACC)
    for n in "ACO": f.label(n)
    f.label("E"); f.label("N", ACC); f.label("F", ACC)
    return f.svg("المثلّث OAE والنقطتان N و F منتصفا [OA] و [OE]")


def svg_q9():
    f = base(); semis(f, "both", MUTED, 1.3)
    f.seg("A", "C", width=2.0)
    f.poly(["A", "D", "E"], color=MUTED, width=1.4, closed=False)
    f.poly(["E", "F", "G", "D"], color=INK, width=2.2)
    f.seg("N", "F", color=ACC, width=2.4, ext0=0.0, ext1=0.0)
    f.seg("O", "E", color=MUTED, width=1.4)
    for n in "ABCO": f.dot(n, MUTED)
    f.dot("D"); f.dot("E")
    for n in "NF": f.dot(n, ACC)
    f.dot("G", ACC)
    for n in "ABCO": f.label(n)
    f.label("D"); f.label("E"); f.label("N", ACC); f.label("F", ACC); f.label("G", ACC)
    return f.svg("الرباعي EFGD والنقطتان N و F ومركز الثقل G")


def svg_q10():
    f = base(); semis(f, "both", MUTED, 1.3)
    f.seg("A", "C", width=2.0)
    f.poly(["A", "D", "E"], color=INK, width=2.2, closed=False)
    f.poly(["E", "F", "G", "D"], color=ACC, width=2.4)
    for n in "AC": f.dot(n, MUTED)
    f.dot("D"); f.dot("E")
    f.dot("F", ACC); f.dot("G", ACC)
    for n in "AC": f.label(n)
    f.label("D"); f.label("E"); f.label("F", ACC); f.label("G", ACC)
    return f.svg("متوازي الأضلاع EFGD والنقطتان A و D على المستقيم (AE)")


def svg_q11():
    f = base(); semis(f, "small", MUTED, 1.3)
    f.seg("A", "B", width=2.0)
    f.fill(["D", "N", "B"], ACC, 0.10)
    f.poly(["D", "N", "B"], color=INK, width=2.4)
    f.seg("D", "I", color=MUTED, width=1.4); f.seg("N", "G", color=MUTED, width=1.4, ext1=0.0)
    f.poly(["A", "D"], color=MUTED, width=1.4, closed=False)
    for n in "ABNI": f.dot(n)
    f.dot("D")
    f.dot("G", ACC)
    for n in "ABNID": f.label(n)
    f.label("G", ACC)
    return f.svg("المثلّث DNB ومركز ثقل المثلّث ABD النقطة G")


def svg_q12():
    f = base()
    f.seg("N", "B", width=2.0)
    f.poly(["D", "N", "B"], color=INK, width=2.4)
    f.seg("B", "G", color=ACC, width=2.2); f.seg("G", "H", color=ACC, width=2.2)
    for n in "BN": f.dot(n)
    f.dot("D")
    f.dot("G", ACC); f.dot("H", ACC)
    for n in "BND": f.label(n)
    f.label("G", ACC); f.label("H", ACC)
    return f.svg("المثلّث DNB والنقطة G ومسقطها العمودي H على (DN)")


if __name__ == "__main__":
    import json
    out = {"questions": []}
    for fn in (svg_q1, svg_q2, svg_q3, svg_q4, svg_q5, svg_q6, svg_q7, svg_q8, svg_q9, svg_q10, svg_q11, svg_q12):
        out["questions"].append({"prompt": "Q " + fn.__name__ + "\n" + fn(), "difficulty": 1})
    json.dump(out, open("tmp/m37_figs.json", "w", encoding="utf-8"), ensure_ascii=False)
    print("figures ok")
