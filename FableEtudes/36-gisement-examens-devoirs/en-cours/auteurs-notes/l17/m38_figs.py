# Figures de la mission 38 (2018 ex4) : cercles de diamètres [AB] et [DE], coordonnées exactes.
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from geo import *
from sympy import sqrt, Rational as R, simplify, solve, symbols
from figlib import Fig, INK, ACC, MUTED

A = pt(0, 0); B = pt(6, 0); I = mid(A, B)
C = pt(R(25, 6), 5 * sqrt(11) / 6)
D = pt(6, 6 * sqrt(11) / 5)
E = pt(R(216, 25), 0)
O = mid(D, E)
F = pt(R(216, 25), 6 * sqrt(11) / 5)
G = inter(A, O, F, I)
K = inter(B, G, A, F)
J = inter(E, G, A, D)
# H : seconde intersection des deux cercles (cercle de centre I rayon 3 ; cercle de centre O rayon DE/2)
r2sq = simplify(d2(D, E) / 4)
x, y = symbols("x y", real=True)
sol = solve([(x - I[0]) ** 2 + (y - I[1]) ** 2 - 9, (x - O[0]) ** 2 + (y - O[1]) ** 2 - r2sq], [x, y], dict=True)
Hs = [(simplify(s[x]), simplify(s[y])) for s in sol]
H = [h for h in Hs if not same(h, B)][0]

# --- vérifications des données officielles
assert on_circle(C, I, 3) and dist(A, C) == 5 and simplify(dist(B, C) - sqrt(11)) == 0 and perp(C, A, C, B)
assert collinear(A, C, D) and perp(B, D, A, B) and between(C, A, D)
assert simplify(dist(C, D) - R(11, 5)) == 0 and simplify(dist(B, D) - 6 * sqrt(11) / 5) == 0 and simplify(dist(A, D) - R(36, 5)) == 0
assert perp(D, E, A, D) and collinear(A, B, E)
assert on_circle(B, O, sqrt(r2sq)) and on_circle(F, O, sqrt(r2sq)) and perp(D, F, D, B) and par(D, F, A, B)
assert same(mid(B, F), O) and same(mid(D, E), O)
assert on_circle(H, I, 3) and on_circle(H, O, sqrt(r2sq)) and collinear(A, H, F)
assert same(K, mid(A, F)) and same(G, centroid(A, B, F)) and same(G, centroid(A, E, D)) and same(J, mid(A, D))
assert collinear(J, K, O)

PTS = {"A": A, "B": B, "I": I, "C": C, "D": D, "E": E, "O": O, "F": F, "G": G, "K": K, "J": J, "H": H,
       "LO": pt(7.32 - 2.4, 1.99), "RO": pt(7.32 + 2.4, 1.99), "T": pt(3, -3), "U": pt(3, 3)}
R1 = 3.0
R2 = float(sqrt(r2sq))
FIT = ["A", "T", "U", "RO", "F"]


def base(W=300, H_=250):
    return Fig(PTS, W=W, H=H_, margin=24, fit=FIT)


def c1(f, color=INK, width=2.0):
    f.circle("I", R1, color=color, width=width)


def c2(f, color=MUTED, width=1.5):
    f.circle("O", R2, color=color, width=width)


def svg_q1():
    f = base(); c1(f)
    f.poly(["A", "B", "C"], color=INK, width=2.4)
    f.seg("A", "B", width=2.4)
    for n in "AB": f.dot(n)
    f.dot("C", ACC); f.dot("I")
    for n in "AB": f.label(n)
    f.label("C", ACC); f.label("I")
    return f.svg("الدائرة التي قطرها [AB] والنقطة C منها والمثلّث ABC")


def svg_q2():
    f = base(); c1(f, MUTED, 1.5)
    f.seg("A", "D", width=2.4); f.seg("B", "D", color=ACC, width=2.4); f.seg("A", "B", width=2.4); f.seg("B", "C", color=INK, width=2.0)
    f.right_angle("B", "A", "D")
    for n in "AB": f.dot(n)
    f.dot("C"); f.dot("D", ACC)
    for n in "ABC": f.label(n)
    f.label("D", ACC)
    return f.svg("الدائرة التي قطرها [AB] والمماسّ في B الذي يقطع (AC) في D")


def svg_q3():
    f = base(); c1(f, MUTED, 1.2)
    f.poly(["B", "C", "D"], color=INK, width=2.4)
    f.right_angle("C", "B", "D")
    f.seg("A", "C", color=MUTED, width=1.4)
    f.dot("B"); f.dot("C"); f.dot("D", ACC); f.dot("A", MUTED)
    for n in "BCD": f.label(n)
    f.label("A", MUTED)
    return f.svg("المثلّث BCD القائم في C")


def svg_q4():
    f = base(); c1(f, MUTED, 1.3); c2(f, MUTED, 1.4)
    f.seg("A", "E", width=2.0); f.seg("A", "D", width=2.0, ext1=0.0)
    f.poly(["B", "D", "F", "E"], color=ACC, width=2.4)
    f.seg("D", "E", color=INK, width=1.8)
    for n in "ABE": f.dot(n)
    f.dot("C", MUTED)
    f.dot("D", ACC); f.dot("F", ACC)
    for n in "ABE": f.label(n)
    f.label("C", MUTED); f.label("D", ACC); f.label("F", ACC)
    return f.svg("الرباعي BDFE والدائرة التي قطرها [DE]")


def svg_q5():
    f = base(); c1(f, INK, 1.8); c2(f, INK, 1.8)
    f.poly(["B", "D", "F", "E"], color=MUTED, width=1.4)
    f.seg("A", "B", width=1.8); f.seg("B", "H", color=ACC, width=2.0)
    for n in "ABDEF": f.dot(n)
    f.dot("H", ACC); f.dot("O"); 
    for n in "ABDEF": f.label(n)
    f.label("H", ACC); f.label("O")
    return f.svg("الدائرتان اللتان قطراهما [AB] و [DE] والمستطيل BDFE ونقطة تقاطعهما H")


def svg_q6():
    f = base()
    f.poly(["A", "B", "F"], color=INK, width=2.4)
    f.seg("F", "I", color=ACC, width=2.2); f.seg("A", "O", color=ACC, width=2.2); f.seg("B", "G", color=ACC, width=2.2, ext1=0.0)
    f.seg("B", "K", color=ACC, width=2.2)
    f.poly(["B", "D", "F", "E"], color=MUTED, width=1.3)
    f.seg("D", "E", color=MUTED, width=1.3)
    for n in "AB": f.dot(n)
    f.dot("F"); f.dot("I"); f.dot("O"); f.dot("G", ACC); f.dot("K", ACC)
    f.dot("D", MUTED); f.dot("E", MUTED)
    for n in "ABFIO": f.label(n)
    f.label("G", ACC); f.label("K", ACC); f.label("D", MUTED); f.label("E", MUTED)
    return f.svg("المستطيل BDFE ومركزه O والمثلّث ABF ونقطة تقاطع (FI) و (AO)")


def svg_q7():
    f = base()
    f.poly(["A", "E", "D"], color=INK, width=2.4)
    f.seg("A", "O", color=ACC, width=2.2)
    f.seg("F", "I", color=MUTED, width=1.3); f.seg("A", "F", color=MUTED, width=1.3); f.seg("B", "F", color=MUTED, width=1.3)
    f.poly(["B", "D", "F", "E"], color=MUTED, width=1.2)
    for n in "AE": f.dot(n)
    f.dot("D"); f.dot("O"); f.dot("G", ACC)
    f.dot("B", MUTED); f.dot("F", MUTED); f.dot("I", MUTED)
    for n in "AEDO": f.label(n)
    f.label("G", ACC); f.label("B", MUTED); f.label("F", MUTED); f.label("I", MUTED)
    return f.svg("المثلّث AED والموسّط [AO] ومركز ثقل المثلّث ABF النقطة G")


def svg_q8():
    f = base()
    f.poly(["A", "E", "D"], color=INK, width=2.4)
    f.seg("E", "J", color=ACC, width=2.2)
    f.seg("A", "O", color=MUTED, width=1.3)
    f.poly(["B", "D", "F", "E"], color=MUTED, width=1.2)
    for n in "AED": f.dot(n)
    f.dot("G", ACC); f.dot("J", ACC)
    f.dot("C", MUTED); f.dot("B", MUTED)
    for n in "AED": f.label(n)
    f.label("G", ACC); f.label("J", ACC); f.label("C", MUTED); f.label("B", MUTED)
    return f.svg("المثلّث AED ومركز ثقله G والمستقيم (EG) الذي يقطع (AD) في J")


def svg_q9():
    f = base()
    f.poly(["A", "D", "F"], color=INK, width=2.4)
    f.seg("D", "E", color=INK, width=2.0); f.seg("A", "E", color=INK, width=2.0)
    f.seg("J", "K", color=ACC, width=2.2); f.seg("J", "O", color=ACC, width=2.2)
    for n in "ADEF": f.dot(n)
    f.dot("J", ACC); f.dot("K", ACC); f.dot("O", ACC)
    for n in "ADEF": f.label(n)
    f.label("J", ACC); f.label("K", ACC); f.label("O", ACC)
    return f.svg("المثلّثان ADF و ADE ومنتصفات J و K و O")


if __name__ == "__main__":
    import json
    out = {"questions": []}
    for fn in (svg_q1, svg_q2, svg_q3, svg_q4, svg_q5, svg_q6, svg_q7, svg_q8, svg_q9):
        out["questions"].append({"prompt": "Q " + fn.__name__ + "\n" + fn(), "difficulty": 1})
    json.dump(out, open("tmp/m38_figs.json", "w", encoding="utf-8"), ensure_ascii=False)
    print("figures ok ; H =", H, " G =", G, " K =", K, " J =", J, " O =", O, " r2 =", R2)
