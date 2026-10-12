# Figures de la mission 40 (2019 ex4) : repère orthonormé (O ; I ; J), B(−4 ; 0) C(2 ; 0) K(−1 ; 0) A(0 ; 2√2), E, H, cercle de diamètre [BC].
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from geo import *
from sympy import sqrt, Rational as R, simplify, symbols
from figlib import Fig, INK, ACC, MUTED, fnum

GRID = "#e2e8f0"
TICK = "#475569"

O = pt(0, 0); I = pt(1, 0); J = pt(0, 1)
B = pt(-4, 0); C = pt(2, 0); K = pt(-1, 0)
A = pt(0, 2 * sqrt(2))
P = mid(O, A)
E = sym(C, P)
H = foot(E, O, I)

# --- vérifications des données officielles et des résultats de l'exercice
assert dist(B, C) == 6 and same(mid(B, C), K)
assert simplify(dist(A, C) - 2 * sqrt(3)) == 0 and perp(O, A, O, C) and between(A, O, pt(0, 10)) and A[1] > 0
assert simplify(dist(O, A) - 2 * sqrt(2)) == 0 and simplify(dist(A, B) - 2 * sqrt(6)) == 0
assert same(E, pt(-2, 2 * sqrt(2))) and same(H, pt(-2, 0))
assert same(mid(O, A), mid(C, E))                      # OCAE : diagonales [OA] et [CE] de même milieu P
assert simplify(dist(O, C) - dist(A, E)) == 0 and simplify(dist(O, E) - dist(C, A)) == 0
assert same(mid(O, E), mid(A, H)) and simplify(dist(O, E) - dist(A, H)) == 0   # OAEH : diagonales de même milieu, égales
assert perp(O, A, O, H) and perp(E, H, O, H) and perp(A, E, O, A)
assert simplify(dist(K, A) - 3) == 0 and simplify(dist(K, E) - 3) == 0 and simplify(dist(K, B) - 3) == 0 and simplify(dist(K, C) - 3) == 0

PTS = {"O": O, "I": I, "J": J, "B": B, "C": C, "K": K, "A": A, "P": P, "E": E, "H": H}


def _tx(f, x, y, text, size=11, weight=400, color=TICK, anchor="middle", dx=0.0, dy=0.0):
    px = f.P((x, y))
    return (f'<text x="{fnum(px[0] + dx)}" y="{fnum(px[1] + dy)}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{color}" '
            f'paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round" direction="ltr" unicode-bidi="isolate">{text}</text>')


def frame(f, xr, yr, grid=True, numbers=True, xticks=None, yticks=None, units=True, ticks=True, jside=1):
    """repère orthonormé : grille légère, axes à flèche, graduations ; les extrémités xr, yr sont celles des axes."""
    xs = range(math.ceil(xr[0]), math.floor(xr[1]) + 1)
    ys = range(math.ceil(yr[0]), math.floor(yr[1]) + 1)
    if grid:
        d = " ".join(f"M{fnum(f.P((x, yr[0]))[0])} {fnum(f.P((x, yr[0]))[1])} V{fnum(f.P((x, yr[1]))[1])}" for x in xs)
        d += " " + " ".join(f"M{fnum(f.P((xr[0], y))[0])} {fnum(f.P((xr[0], y))[1])} H{fnum(f.P((xr[1], y))[0])}" for y in ys)
        f.fills.append(f'<path d="{d}" fill="none" stroke="{GRID}" stroke-width="1"/>')
    a0, a1 = f.P((xr[0], 0)), f.P((xr[1], 0))
    b0, b1 = f.P((0, yr[0])), f.P((0, yr[1]))
    f.fills.append(f'<path d="M{fnum(a0[0])} {fnum(a0[1])} H{fnum(a1[0] - 6)} M{fnum(b0[0])} {fnum(b0[1])} V{fnum(b1[1] + 6)}" fill="none" stroke="{INK}" stroke-width="1.8"/>')
    f.fills.append(
        f'<path d="M{fnum(a1[0] + 3)} {fnum(a1[1])} L{fnum(a1[0] - 7)} {fnum(a1[1] - 4.5)} L{fnum(a1[0] - 7)} {fnum(a1[1] + 4.5)} Z '
        f'M{fnum(b1[0])} {fnum(b1[1] - 3)} L{fnum(b1[0] - 4.5)} {fnum(b1[1] + 7)} L{fnum(b1[0] + 4.5)} {fnum(b1[1] + 7)} Z" fill="{INK}"/>'
    )
    f.edges.append((a0, a1)); f.edges.append((b0, b1))
    if ticks:
        d = ""
        for x in xs:
            if x != 0:
                p = f.P((x, 0)); d += f"M{fnum(p[0])} {fnum(p[1] - 3)} V{fnum(p[1] + 3)} "
        for y in ys:
            if y != 0:
                p = f.P((0, y)); d += f"M{fnum(p[0] - 3)} {fnum(p[1])} H{fnum(p[0] + 3)} "
        f.marks.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.2"/>')
    if numbers:
        for x in (xticks if xticks is not None else xs):
            if x != 0:
                f.marks.append(_tx(f, x, 0, str(x).replace("-", "−"), dy=17))
        for y in (yticks if yticks is not None else ys):
            if y != 0:
                f.marks.append(_tx(f, 0, y, str(y).replace("-", "−"), dx=-13, dy=4))
    # O, I, J
    f.marks.append(_tx(f, 0, 0, "O", size=14, weight=700, color=INK, dx=-9, dy=15))
    if units:
        f.dot("I"); f.dot("J")
        f.marks.append(_tx(f, 1, 0, "I", size=14, weight=700, color=INK, dx=0, dy=-8))
        f.marks.append(_tx(f, 0, 1, "J", size=14, weight=700, color=INK, dx=9 * jside, dy=-3))
    f.dot("O")


def base(xr=(-4.7, 3.5), yr=(-1.0, 3.6), W=330, H_=215, margin=10):
    # points d'ajustement : coins du cadre
    pts = dict(PTS)
    pts["LL"] = (xr[0], yr[0]); pts["UR"] = (xr[1], yr[1])
    f = Fig(pts, W=W, H=H_, margin=margin, fit=["LL", "UR"])
    return f, xr, yr


# ---------------------------------------------------------------------------------------------- Q1 : milieu de [BC]
def svg_mid():
    f, xr, yr = base(yr=(-1.0, 1.9), H_=150)
    frame(f, xr, yr, yticks=[-1, 1])
    f.seg("B", "C", color=ACC, width=3.0)
    f.dot("B", ACC); f.dot("C", ACC)
    f.label("B", ACC, dir=90); f.label("C", ACC, dir=90)
    return f.svg("المعلّم المتعامد المتجانس (O ; I ; J) والنقطتان B و C على محور الفواصل والقطعة [BC]")


# ---------------------------------------------------------------------------------------------- Q2 : longueurs sur l'axe
def svg_len():
    f, xr, yr = base(yr=(-1.0, 1.9), H_=150)
    frame(f, xr, yr, yticks=[-1, 1])
    f.seg("O", "B", color=INK, width=3.0)
    f.seg("O", "C", color=ACC, width=3.0)
    f.dot("B", INK); f.dot("C", ACC)
    f.label("B", INK, dir=90); f.label("C", ACC, dir=90)
    return f.svg("المعلّم المتعامد المتجانس (O ; I ; J) والنقطتان B و C على محور الفواصل والقطعتان [OB] و [OC]")


# ---------------------------------------------------------------------------------------------- Q3 : OA par Pythagore (sans graduations)
def svg_oa():
    f, xr, yr = base(xr=(-0.8, 3.0), yr=(-0.8, 3.7), W=270, H_=215)
    frame(f, xr, yr, grid=False, numbers=False, ticks=False)
    f.poly(["O", "C", "A"], color=INK, width=2.4)
    f.right_angle("O", "C", "A")
    f.dot("C"); f.dot("A", ACC)
    f.label("C", INK, dir=300); f.label("A", ACC, dir=45)
    return f.svg("المعلّم المتعامد المتجانس والمثلّث OAC القائم في O")


# ---------------------------------------------------------------------------------------------- Q4 : coordonnées de A (sans graduations)
def svg_a():
    f, xr, yr = base(xr=(-1.4, 1.8), yr=(-0.8, 3.7), W=240, H_=215)
    frame(f, xr, yr, grid=False, numbers=False, ticks=False)
    f.seg("O", "A", color=ACC, width=3.0)
    f.dot("A", ACC)
    f.label("A", ACC, dir=20)
    return f.svg("المعلّم المتعامد المتجانس (O ; I ; J) والنقطة A من نصف المستقيم [OJ)")


# ---------------------------------------------------------------------------------------------- Q5 : AB
def svg_ab():
    f, xr, yr = base(xr=(-4.8, 1.2), yr=(-0.8, 3.7), W=300, H_=200)
    frame(f, xr, yr, grid=False, numbers=False, ticks=False)
    f.poly(["O", "A", "B"], color=INK, width=2.4)
    f.seg("A", "B", color=ACC, width=3.0)
    f.right_angle("O", "B", "A")
    f.dot("B"); f.dot("A", ACC)
    f.label("B", INK, dir=270); f.label("A", ACC, dir=45)
    return f.svg("المعلّم المتعامد المتجانس والمثلّث OAB القائم في O والقطعة [AB]")


# ---------------------------------------------------------------------------------------------- Q6 : OCAE parallélogramme
def svg_par():
    f, xr, yr = base(xr=(-3.0, 3.0), yr=(-0.8, 3.7), W=300, H_=215)
    frame(f, xr, yr, grid=False, numbers=False, ticks=False, jside=-1)
    f.poly(["O", "C", "A", "E"], color=INK, width=2.4)
    f.seg("O", "A", color=ACC, width=2.0, dash="5 4"); f.seg("C", "E", color=ACC, width=2.0, dash="5 4")
    for n in ("C", "A", "E"): f.dot(n)
    f.dot("P", ACC)
    f.label("C", INK, dir=300); f.label("A", INK, dir=45); f.label("E", INK, dir=135); f.label("P", ACC, dir=45)
    return f.svg("المعلّم المتعامد المتجانس والرباعي OCAE وقطراه [OA] و [CE] المتقاطعان في P")


# ---------------------------------------------------------------------------------------------- Q7 : coordonnées de E (E non dessiné)
def svg_e():
    f, xr, yr = base(xr=(-3.0, 3.0), yr=(-0.8, 3.7), W=300, H_=215)
    frame(f, xr, yr, grid=False, numbers=False, ticks=False, jside=-1)
    f.seg("C", "P", color=ACC, width=2.4)
    f.dot("C", INK); f.dot("P", ACC)
    f.label("C", INK, dir=300); f.label("P", ACC, dir=90)
    return f.svg("المعلّم المتعامد المتجانس والنقطتان C و P")


# ---------------------------------------------------------------------------------------------- Q8 : OAEH rectangle
def svg_rect():
    f, xr, yr = base(xr=(-3.0, 2.2), yr=(-0.8, 3.7), W=290, H_=215)
    frame(f, xr, yr, grid=False, numbers=False, ticks=False)
    f.poly(["O", "A", "E", "H"], color=INK, width=2.4)
    f.right_angle("O", "A", "H")
    f.right_angle("H", "O", "E")
    f.dot("A"); f.dot("E", ACC); f.dot("H", ACC)
    f.label("A", INK, dir=45); f.label("E", ACC, dir=135); f.label("H", ACC, dir=270)
    return f.svg("المعلّم المتعامد المتجانس والرباعي OAEH حيث H المسقط العمودي للنقطة E على (OI)")


# ---------------------------------------------------------------------------------------------- Q9 : KA
def svg_ka():
    f, xr, yr = base(xr=(-4.7, 3.0), yr=(-0.8, 3.7), W=330, H_=215)
    frame(f, xr, yr, grid=False, numbers=False, ticks=False)
    f.seg("K", "A", color=ACC, width=3.0)
    f.seg("B", "C", color=MUTED, width=1.6)
    f.dot("B", MUTED); f.dot("C", MUTED); f.dot("K", ACC); f.dot("A", ACC)
    f.label("B", MUTED, dir=90); f.label("C", MUTED, dir=90); f.label("K", ACC, dir=270); f.label("A", ACC, dir=45)
    return f.svg("المعلّم المتعامد المتجانس والقطعة [BC] ومنتصفها K والقطعة [KA]")


# ---------------------------------------------------------------------------------------------- Q10 : E sur le cercle de diamètre [BC]
def svg_circle():
    f, xr, yr = base(xr=(-4.9, 3.1), yr=(-3.4, 3.7), W=330, H_=295)
    frame(f, xr, yr, grid=False, numbers=False, ticks=False)
    f.circle("K", 3.0, color=MUTED, width=1.8)
    f.poly(["O", "A", "E", "H"], color=MUTED, width=1.4)
    f.seg("E", "H", color=ACC, width=2.4)
    f.right_angle("H", "E", "C")
    f.dot("A", MUTED)
    f.dot("B", INK); f.dot("C", INK); f.dot("K", INK); f.dot("E", ACC); f.dot("H", ACC)
    f.label("B", INK, dir=135); f.label("C", INK, dir=45); f.label("K", INK, dir=300); f.label("E", ACC, dir=120); f.label("H", ACC, dir=270); f.label("A", MUTED, dir=45)
    return f.svg("المعلّم المتعامد المتجانس والمستطيل OAEH والدائرة التي قطرها [BC] والنقطة E والمسقط العمودي H")


FIGS = (svg_mid, svg_len, svg_oa, svg_a, svg_ab, svg_par, svg_e, svg_rect, svg_ka, svg_circle)

if __name__ == "__main__":
    import json
    out = {"questions": []}
    for fn in FIGS:
        out["questions"].append({"prompt": "Q " + fn.__name__ + "\n" + fn(), "difficulty": 1})
    json.dump(out, open("tmp/m40_figs.json", "w", encoding="utf-8"), ensure_ascii=False)
    print("figures ok ; P =", P, " E =", E, " H =", H)
