# Figures de la mission 41 (2020 ex5) : rectangle ABCD (AB = 8, BC = 4), I sur [CD] (CI = 2), H = (AC) ∩ (BI), O centre, J milieu de [BC], K = (BH) ∩ (OJ), L = (CK) ∩ (OB).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from geo import *
from sympy import sqrt, Rational as R, simplify
from figlib import Fig, INK, ACC, MUTED

# D en haut à gauche, C en haut à droite, B en bas à droite, A en bas à gauche (comme au sujet)
A = pt(0, 0); B = pt(8, 0); C = pt(8, 4); D = pt(0, 4)
O = mid(A, C)
I = pt(6, 4)
H = inter(A, C, B, I)
J = mid(B, C)
K = inter(B, H, O, J)
L = inter(C, K, O, B)

# --- vérifications des données officielles et des résultats de l'exercice
assert dist(A, B) == 8 and dist(B, C) == 4 and same(O, mid(B, D)) and perp(A, B, B, C)
assert between(I, C, D) and dist(C, I) == 2
assert simplify(dist(B, I) - 2 * sqrt(5)) == 0 and simplify(dist(A, C) - 4 * sqrt(5)) == 0
assert same(H, pt(R(32, 5), R(16, 5))) and between(H, A, C) and between(H, B, I)
assert simplify(dist(H, C) / dist(H, A) - R(1, 4)) == 0 and simplify(dist(H, I) / dist(H, B) - R(1, 4)) == 0
assert simplify(dist(H, C) - 4 * sqrt(5) / 5) == 0 and simplify(dist(H, B) - 8 * sqrt(5) / 5) == 0
assert perp(A, C, B, I) and simplify(d2(H, C) + d2(H, B) - 16) == 0
assert same(K, pt(7, 2)) and par(O, J, A, B) and perp(O, J, B, C) and perp(B, K, O, C)
assert same(L, pt(R(32, 5), R(4, 5))) and perp(C, K, O, B) and between(L, O, B)
assert simplify(dist(C, L) - 8 * sqrt(5) / 5) == 0 and simplify(dist(B, L) - 4 * sqrt(5) / 5) == 0
assert simplify(area_tri(C, L, B) - R(16, 5)) == 0 and simplify(area_tri(O, B, C) - 8) == 0

PTS = {"A": A, "B": B, "C": C, "D": D, "O": O, "I": I, "H": H, "J": J, "K": K, "L": L}


def base(W=330, H_=200, margin=26, fit=("A", "B", "C", "D")):
    return Fig(PTS, W=W, H=H_, margin=margin, fit=list(fit))


def rect(f, color=INK, width=2.2, marks=True):
    f.poly(["A", "B", "C", "D"], color=color, width=width)
    if marks:
        for v, a, b in (("A", "B", "D"), ("B", "A", "C"), ("C", "B", "D"), ("D", "A", "C")):
            f.right_angle(v, a, b)


def svg_bi():
    f = base()
    rect(f, INK, 2.2, marks=False)
    f.seg("B", "I", color=ACC, width=3.0)
    f.right_angle("C", "B", "D")
    for n in "ABCD": f.dot(n)
    f.dot("I", ACC)
    for n in "ABCD": f.label(n)
    f.label("I", ACC)
    return f.svg("المستطيل ABCD والنقطة I من [CD] والقطعة [BI]")


def svg_ac():
    f = base()
    rect(f, INK, 2.2, marks=False)
    f.seg("A", "C", color=ACC, width=3.0)
    f.right_angle("B", "A", "C")
    for n in "ABCD": f.dot(n)
    for n in "ABCD": f.label(n)
    return f.svg("المستطيل ABCD وقطره [AC]")


def svg_papillon():
    f = base()
    f.fill(["H", "C", "I"], color=ACC, opacity=0.18)
    f.fill(["H", "A", "B"], color=MUTED, opacity=0.08)
    rect(f, INK, 2.2, marks=False)
    f.seg("A", "C", color=INK, width=2.0); f.seg("B", "I", color=INK, width=2.0)
    for n in "ABCD": f.dot(n)
    f.dot("I", ACC); f.dot("H", ACC)
    for n in "ABCD": f.label(n)
    f.label("I", ACC); f.label("H", ACC)
    return f.svg("المستطيل ABCD والمستقيمان (AC) و (BI) المتقاطعان في H وضعيّة الفراشة")


def svg_hc():
    f = base()
    rect(f, MUTED, 1.4, marks=False)
    f.seg("A", "H", color=INK, width=2.2)
    f.seg("H", "C", color=ACC, width=3.2)
    for n in "ABCD": f.dot(n, MUTED)
    f.dot("H", ACC)
    for n in "ABCD": f.label(n, MUTED)
    f.label("H", ACC)
    return f.svg("القطر [AC] والنقطة H منه والقطعة [HC]")


def svg_hb():
    f = base()
    rect(f, MUTED, 1.4, marks=False)
    f.seg("I", "H", color=INK, width=2.2)
    f.seg("H", "B", color=ACC, width=3.2)
    for n in "ABCD": f.dot(n, MUTED)
    f.dot("I", INK); f.dot("H", ACC)
    for n in "ABCD": f.label(n, MUTED)
    f.label("I", INK); f.label("H", ACC)
    return f.svg("القطعة [BI] والنقطة H منها والقطعة [HB]")


def svg_hbc():
    f = base()
    rect(f, MUTED, 1.4, marks=False)
    f.poly(["H", "B", "C"], color=ACC, width=2.8)
    f.seg("A", "H", color=MUTED, width=1.4); f.seg("H", "I", color=MUTED, width=1.4)
    for n in "AD": f.dot(n, MUTED)
    f.dot("B"); f.dot("C"); f.dot("I", MUTED); f.dot("H", ACC)
    for n in "AD": f.label(n, MUTED)
    f.label("B"); f.label("C"); f.label("I", MUTED); f.label("H", ACC)
    return f.svg("المثلّث HBC داخل المستطيل ABCD")


def svg_oj():
    f = base()
    rect(f, INK, 2.2, marks=False)
    f.seg("A", "C", color=MUTED, width=1.4)
    f.seg("O", "J", color=ACC, width=3.0)
    f.right_angle("B", "A", "C")
    for n in "ABCD": f.dot(n)
    f.dot("O"); f.dot("J", ACC)
    for n in "ABCD": f.label(n)
    f.label("O"); f.label("J", ACC)
    return f.svg("المستطيل ABCD ومركزه O ومنتصف J للضلع [BC] والقطعة [OJ]")


def svg_orthocentre():
    f = base(fit=("O", "B", "C", "J"), W=330, H_=200, margin=28)
    f.poly(["O", "B", "C"], color=INK, width=2.4)
    f.seg("B", "H", color=ACC, width=2.2)
    f.seg("O", "J", color=ACC, width=2.2)
    f.seg("C", "K", color=ACC, width=2.0, dash="5 4")
    f.right_angle("H", "B", "C")
    f.right_angle("J", "O", "B")
    for n in "OBC": f.dot(n)
    f.dot("H", ACC); f.dot("J", ACC); f.dot("K", ACC)
    f.label("O"); f.label("B"); f.label("C"); f.label("H", ACC); f.label("J", ACC); f.label("K", ACC)
    return f.svg("المثلّث OBC والمستقيمان (BH) و (OJ) المتقاطعان في K والقطعة [CK]")


def svg_cl():
    f = base(fit=("O", "B", "C", "J"), W=330, H_=200, margin=26)
    f.poly(["O", "B", "C"], color=INK, width=2.4)
    f.seg("O", "J", color=INK, width=2.0)
    f.seg("C", "L", color=ACC, width=3.0)
    f.right_angle("J", "O", "B")
    f.right_angle("L", "C", "O")
    for n in "OBC": f.dot(n)
    f.dot("J"); f.dot("L", ACC)
    f.label("O"); f.label("B"); f.label("C"); f.label("J"); f.label("L", ACC)
    return f.svg("المثلّث OBC والارتفاعان [OJ] و [CL]")


def svg_clb():
    f = base(fit=("B", "C", "L"), W=300, H_=190, margin=30)
    f.poly(["C", "L", "B"], color=INK, width=2.6)
    f.fill(["C", "L", "B"], color=ACC, opacity=0.12)
    f.right_angle("L", "C", "B")
    f.dot("B"); f.dot("C"); f.dot("L", ACC)
    f.label("B"); f.label("C"); f.label("L", ACC)
    return f.svg("المثلّث CLB القائم في L")


FIGS = (svg_bi, svg_ac, svg_papillon, svg_hc, svg_hb, svg_hbc, svg_oj, svg_orthocentre, svg_cl, svg_clb)

if __name__ == "__main__":
    import json
    out = {"questions": []}
    for fn in FIGS:
        out["questions"].append({"prompt": "Q " + fn.__name__ + "\n" + fn(), "difficulty": 1})
    json.dump(out, open("tmp/m41_figs.json", "w", encoding="utf-8"), ensure_ascii=False)
    print("figures ok ; H =", H, " K =", K, " L =", L, " O =", O)
