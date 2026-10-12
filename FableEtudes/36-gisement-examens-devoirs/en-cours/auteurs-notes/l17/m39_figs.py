# Figures de la mission 39 (2019 ex3) : triangle ABC rectangle en A (AB = 4, AC = 3), M sur [BC], rectangle AHMK.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from geo import *
from sympy import sqrt, Rational as R, simplify
from figlib import Fig, INK, ACC, MUTED

# A en bas à gauche, B en bas à droite, C en haut à gauche (comme au sujet)
A = pt(0, 0); B = pt(4, 0); C = pt(0, 3)
a_fig = R(2)                       # BM = 2 dans la figure (position quelconque, ni milieu ni pied de la hauteur)
M = (B[0] + (C[0] - B[0]) * a_fig / 5, B[1] + (C[1] - B[1]) * a_fig / 5)
H = foot(M, A, B)
K = foot(M, A, C)

# --- vérifications des données officielles
assert perp(A, B, A, C) and dist(A, B) == 4 and dist(A, C) == 3 and dist(B, C) == 5
assert between(M, B, C) and simplify(dist(B, M) - a_fig) == 0
assert collinear(A, H, B) and perp(M, H, A, B) and collinear(A, K, C) and perp(M, K, A, C)
assert par(H, M, A, C) and par(K, M, A, B)
assert perp(A, H, H, M) and perp(H, M, M, K) and perp(M, K, K, A) and perp(K, A, A, H)   # AHMK rectangle
assert simplify(dist(A, M) - dist(H, K)) == 0

PTS = {"A": A, "B": B, "C": C, "M": M, "H": H, "K": K}
FIT = ["A", "B", "C"]


def base(W=300, H_=250):
    return Fig(PTS, W=W, H=H_, margin=26, fit=FIT)


def tri(f, color=INK, width=2.4):
    f.poly(["A", "B", "C"], color=color, width=width)


def rect(f, color=INK, width=2.2, marks=True):
    f.poly(["A", "H", "M", "K"], color=color, width=width)
    if marks:
        f.right_angle("A", "B", "C")
        f.right_angle("H", "A", "M")
        f.right_angle("K", "A", "M")
        f.right_angle("M", "H", "K")


def svg_bc():
    f = base()
    tri(f, INK, 2.4)
    f.seg("B", "C", color=ACC, width=2.8)
    f.right_angle("A", "B", "C")
    for n in "ABC": f.dot(n)
    for n in "ABC": f.label(n)
    return f.svg("المثلّث ABC القائم في A والوتر [BC]")


def svg_hm():
    f = base()
    tri(f, INK, 2.4)
    f.seg("H", "M", color=ACC, width=2.8)
    f.right_angle("A", "B", "C")
    f.right_angle("H", "A", "M")
    for n in "ABC": f.dot(n)
    f.dot("M", ACC); f.dot("H", ACC)
    for n in "ABC": f.label(n)
    f.label("M", ACC); f.label("H", ACC)
    return f.svg("المثلّث ABC والنقطة M من [BC] والمسقط العمودي H على (AB) والقطعة [HM]")


def svg_rect_diag():
    f = base()
    tri(f, MUTED, 1.4)
    rect(f, INK, 2.4)
    f.seg("A", "M", color=ACC, width=2.0, dash="5 4")
    f.seg("H", "K", color=ACC, width=2.0, dash="5 4")
    for n in "ABC": f.dot(n, MUTED if n in "BC" else INK)
    f.dot("M"); f.dot("H"); f.dot("K")
    for n in "ABC": f.label(n)
    for n in "MHK": f.label(n)
    return f.svg("المستطيل AHMK داخل المثلّث ABC وقطراه [AM] و [HK]")


def svg_km():
    f = base()
    tri(f, MUTED, 1.4)
    rect(f, INK, 2.2)
    f.seg("K", "M", color=ACC, width=3.0)
    for n in "ABC": f.dot(n, MUTED if n in "BC" else INK)
    f.dot("H"); f.dot("K", ACC); f.dot("M", ACC)
    for n in "ABC": f.label(n)
    f.label("H"); f.label("K", ACC); f.label("M", ACC)
    return f.svg("المستطيل AHMK داخل المثلّث ABC والضلع [KM]")


def svg_hk():
    f = Fig(PTS, W=300, H=230, margin=30, fit=["A", "H", "M", "K"])
    f.poly(["A", "H", "M", "K"], color=INK, width=2.0)
    f.poly(["H", "M", "K"], color=ACC, width=2.8)
    f.right_angle("M", "H", "K")
    f.dot("A"); f.dot("H", ACC); f.dot("K", ACC); f.dot("M", ACC)
    f.label("A"); f.label("H", ACC); f.label("K", ACC); f.label("M", ACC)
    return f.svg("المستطيل AHMK والمثلّث HMK القائم في M ووتره [HK]")


def svg_bridge():
    f = base()
    tri(f, MUTED, 1.4)
    rect(f, INK, 2.2)
    f.seg("A", "M", color=ACC, width=3.0)
    f.seg("H", "K", color=MUTED, width=1.6, dash="5 4")
    for n in "ABC": f.dot(n, MUTED if n in "BC" else INK)
    f.dot("H"); f.dot("K"); f.dot("M", ACC)
    for n in "ABC": f.label(n)
    for n in "HK": f.label(n)
    f.label("M", ACC)
    return f.svg("المستطيل AHMK داخل المثلّث ABC والقطر [AM]")


def svg_am():
    f = base()
    tri(f, INK, 2.4)
    f.seg("A", "M", color=ACC, width=3.0)
    f.right_angle("A", "B", "C")
    for n in "ABC": f.dot(n)
    f.dot("M", ACC)
    for n in "ABC": f.label(n)
    f.label("M", ACC)
    return f.svg("المثلّث ABC والنقطة M من [BC] والقطعة [AM]")


def svg_rect_am():
    """rectangle AHMK seul : la diagonale [AM] en relief, l'autre diagonale [HK] en pointillés discrets"""
    f = Fig(PTS, W=300, H=230, margin=30, fit=["A", "H", "M", "K"])
    f.poly(["A", "H", "M", "K"], color=INK, width=2.2)
    f.seg("A", "M", color=ACC, width=3.0)
    f.seg("H", "K", color=MUTED, width=1.6, dash="5 4")
    f.right_angle("A", "K", "H"); f.right_angle("H", "A", "M"); f.right_angle("M", "H", "K"); f.right_angle("K", "A", "M")
    f.dot("A"); f.dot("H"); f.dot("K"); f.dot("M", ACC)
    f.label("A"); f.label("H"); f.label("K"); f.label("M", ACC)
    return f.svg("المستطيل AHMK والقطعة [AM] من رأس إلى الرأس المقابل")


FIGS = (svg_bc, svg_hm, svg_rect_diag, svg_km, svg_hk, svg_rect_am, svg_bridge, svg_am)

if __name__ == "__main__":
    import json
    out = {"questions": []}
    for fn in FIGS:
        out["questions"].append({"prompt": "Q " + fn.__name__ + "\n" + fn(), "difficulty": 1})
    json.dump(out, open("tmp/m39_figs.json", "w", encoding="utf-8"), ensure_ascii=False)
    print("figures ok ; M =", M, " H =", H, " K =", K)
