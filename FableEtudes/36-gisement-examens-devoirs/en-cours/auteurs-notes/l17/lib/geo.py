# geo : géométrie analytique EXACTE (sympy) pour vérifier chaque figure et chaque valeur.
from sympy import Rational as R, sqrt, simplify, S, Symbol, solve, Eq, nsimplify, sympify, Abs, Matrix, symbols

__all__ = ["R", "sqrt", "simplify", "S", "pt", "sub", "add", "scl", "dot", "cross", "d2", "dist", "mid", "sym", "perp", "par",
           "collinear", "inter", "foot", "centroid", "on_circle", "same", "zero", "between", "area_tri", "ang_cos", "Abs", "symbols", "solve"]


def pt(x, y):
    return (sympify(x), sympify(y))


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def scl(k, a):
    return (k * a[0], k * a[1])


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]


def zero(e):
    return simplify(e) == 0


def d2(a, b):
    return simplify(dot(sub(a, b), sub(a, b)))


def dist(a, b):
    return simplify(sqrt(d2(a, b)))


def mid(a, b):
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)


def sym(a, c):
    """symétrique de a par rapport au point c"""
    return (2 * c[0] - a[0], 2 * c[1] - a[1])


def perp(a, b, c, d):
    """(ab) ⊥ (cd)"""
    return zero(dot(sub(b, a), sub(d, c)))


def par(a, b, c, d):
    """(ab) ∥ (cd)"""
    return zero(cross(sub(b, a), sub(d, c)))


def collinear(a, b, c):
    return zero(cross(sub(b, a), sub(c, a)))


def inter(a, b, c, d):
    """intersection des droites (ab) et (cd)"""
    t = symbols("t")
    u = symbols("u")
    sol = solve([a[0] + t * (b[0] - a[0]) - c[0] - u * (d[0] - c[0]), a[1] + t * (b[1] - a[1]) - c[1] - u * (d[1] - c[1])], [t, u], dict=True)
    assert sol, "droites parallèles"
    tt = sol[0][t]
    return (simplify(a[0] + tt * (b[0] - a[0])), simplify(a[1] + tt * (b[1] - a[1])))


def foot(p, a, b):
    """projeté orthogonal de p sur (ab)"""
    ab = sub(b, a)
    t = simplify(dot(sub(p, a), ab) / dot(ab, ab))
    return (simplify(a[0] + t * ab[0]), simplify(a[1] + t * ab[1]))


def centroid(a, b, c):
    return ((a[0] + b[0] + c[0]) / 3, (a[1] + b[1] + c[1]) / 3)


def on_circle(p, c, r):
    return zero(d2(p, c) - r * r)


def same(p, q):
    return zero(p[0] - q[0]) and zero(p[1] - q[1])


def between(p, a, b):
    """p ∈ [ab]"""
    return collinear(a, p, b) and simplify(dot(sub(p, a), sub(p, b))) <= 0


def area_tri(a, b, c):
    return simplify(Abs(cross(sub(b, a), sub(c, a))) / 2)


def ang_cos(v, a, b):
    """cosinus de l'angle (va, vb)"""
    u, w = sub(a, v), sub(b, v)
    return simplify(dot(u, w) / (sqrt(dot(u, u)) * sqrt(dot(w, w))))
