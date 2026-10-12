# Double résolution mission 40 : coordonnées exactes (sympy) + chemins du cours (formules du repère, Pythagore, quadrilatères).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from geo import *
from sympy import sqrt, Rational as R, simplify, symbols, S, Abs, solve, Eq
import m40_figs as F

O, I, J, B, C, K, A, P, E, H = F.O, F.I, F.J, F.B, F.C, F.K, F.A, F.P, F.E, F.H


def ok(cond, msg):
    assert cond, "ÉCHEC : " + msg
    print("  ok :", msg)


print("Q1  milieu de [BC]")
mBC = mid(B, C)
ok(same(mBC, K) and same(mBC, pt(R(-4 + 2, 2), 0)), "milieu de [BC] = (−1 ; 0) = K")
for nm, d in (("(−2 ; 0)", pt(-4 + 2, 0)), ("(3 ; 0)", pt(R(2 - (-4), 2), 0)), ("(6 ; 0)", pt(2 - (-4), 0))):
    ok(not same(d, mBC), f"distracteur {nm} ≠ milieu")
ok(R(4 + 2, 2) == 3 and R(2 - (-4), 2) == 3, "(3 ; 0) = (4 + 2)/2 = (2 − (−4))/2 (deux chemins vers la même valeur fausse)")
ok(len({-2, -1, 3, 6}) == 4 and not any(z in {x + y for x in (-2, -1, 3, 6) for y in (-2, -1, 3, 6) if x != y} and False for z in (-2, -1, 3, 6)), "quatre valeurs distinctes")
vals = [-2, -1, 3, 6]
ok(not any(vals[k] == vals[i] + vals[j] or vals[k] == vals[i] - vals[j] for k in range(4) for i in range(4) for j in range(4) if len({i, j, k}) == 3), "aucune option n'est somme ou différence de deux autres")

print("Q2  abscisse ≠ longueur")
OB, OC, BC = dist(O, B), dist(O, C), dist(B, C)
ok(B[0] == -4 and OB == 4 and OC == 2 and BC == 6, "xB = −4 ; OB = 4 ; OC = 2 ; BC = 6")
ok(OB != -4 and BC != -4 + 2 and BC != OB - OC and BC == OB + OC and collinear(O, B, C) and between(O, B, C), "OB = −4, BC = −2, BC = OB − OC fausses ; BC = OB + OC (O entre B et C)")

print("Q3  OA")
y = symbols("y", positive=True)
solA = solve(Eq(d2(pt(0, y), C), 12), y)
ok(solA == [2 * sqrt(2)], f"A(0 ; y>0) avec AC² = 12 : y = {solA}")
ok(simplify(sqrt(12 - 4) - 2 * sqrt(2)) == 0 and perp(O, A, O, C), "OA = √(AC² − OC²) = 2√2 (triangle rectangle en O)")
ok(sqrt(12 + 4) == 4 and 12 - 4 == 8 and simplify(2 * sqrt(3) - 2 - 2 * sqrt(2)) != 0, "distracteurs : 4 = √(12 + 4) ; 8 = OA² ; 2√3 − 2 ≠ 2√2")
vals = [8, 4, 2 * sqrt(2), 2 * sqrt(3) - 2]
ok(len({simplify(v) for v in vals}) == 4, "quatre valeurs distinctes")

print("Q4  coordonnées de A")
ok(simplify(sqrt(8) - 2 * sqrt(2)) == 0 and same(A, pt(0, 2 * sqrt(2))) and A[1] > 0, "OA² = 8, A ∈ [OJ) ⇒ A(0 ; 2√2)")
ok(d2(pt(2 * sqrt(2), 0), O) == 8 and pt(2 * sqrt(2), 0)[1] == 0 and not collinear(O, J, pt(2 * sqrt(2), 0)), "(2√2 ; 0) : bonne longueur mais sur (OI), pas sur [OJ)")
ok(d2(pt(0, 4), O) == 16 != 8 and d2(pt(0, 8), O) == 64 != 8 and R(8, 2) == 4, "(0 ; 4) : OA² = 16 ; (0 ; 8) : OA² = 64 ; 4 = 8/2")

print("Q5  AB")
ok(simplify(dist(A, B) - 2 * sqrt(6)) == 0 and d2(A, B) == 24, "AB = √24 = 2√6 (coordonnées)")
ok(simplify(sqrt(16 + 8) - 2 * sqrt(6)) == 0 and simplify(sqrt(24) - sqrt(4 * 6)) == 0, "Pythagore OA² + OB² = 8 + 16 = 24")
ok(simplify(sqrt(16 - 8) - 2 * sqrt(2)) == 0 and simplify(6 * sqrt(2) - sqrt(24)) != 0 and simplify(sqrt(72) - 6 * sqrt(2)) == 0, "distracteurs : 24 = AB² ; 2√2 = √(16 − 8) ; 6√2 = √72 ≠ √24")
vals = [24, 2 * sqrt(2), 6 * sqrt(2), 2 * sqrt(6)]
ok(len({simplify(v) for v in vals}) == 4 and not any(simplify(vals[k] - vals[i] - vals[j]) == 0 or simplify(vals[k] - vals[i] + vals[j]) == 0 for k in range(4) for i in range(4) for j in range(4) if len({i, j, k}) == 3), "valeurs distinctes ; aucune somme/différence de deux autres")

print("Q6  OCAE parallélogramme")
ok(same(P, pt(0, sqrt(2))) and same(P, mid(O, A)) and same(P, mid(C, E)), "P(0 ; √2) milieu de [OA] et de [CE]")
ok(not same(mid(O, C), mid(A, E)), "[OC] et [AE] n'ont pas le même milieu (option c fausse)")
ok(simplify(dist(O, C) - 2) == 0 and simplify(dist(A, E) - 2) == 0, "OC = AE = 2 (prémisse vraie de l'option d)")
ok(par(O, C, A, E) and par(O, E, C, A), "OCAE : côtés opposés parallèles (parallélogramme)")
# contre-exemple à « un seul couple de côtés opposés égaux suffit » : trapèze isocèle
a1, b1, c1, d1 = pt(0, 0), pt(4, 0), pt(3, 2), pt(1, 2)
ok(simplify(dist(a1, d1) - dist(b1, c1)) == 0 and not par(a1, d1, b1, c1) and not same(mid(a1, c1), mid(b1, d1)), "contre-exemple : trapèze isocèle (un couple de côtés égaux, pas un parallélogramme)")

print("Q7  E")
ok(same(E, pt(-2, 2 * sqrt(2))) and same(E, pt(2 * P[0] - C[0], 2 * P[1] - C[1])), "E = (2xP − xC ; 2yP − yC) = (−2 ; 2√2)")
for nm, d in (("(2 ; 2√2)", pt(2, 2 * sqrt(2))), ("(1 ; √2/2)", pt(1, sqrt(2) / 2)), ("(4 ; −√2)", pt(4, -sqrt(2)))):
    ok(not same(d, E), f"distracteur {nm} ≠ E")
ok(same(pt(2, 2 * sqrt(2)), pt(C[0] + A[0] - O[0], C[1] + A[1] - O[1])), "(2 ; 2√2) = C + A − O : sommet opposé à O (sommets mal ordonnés)")
ok(same(pt(1, sqrt(2) / 2), mid(C, P)), "(1 ; √2/2) = milieu de [CP]")
ok(same(pt(4, -sqrt(2)), sym(P, C)), "(4 ; −√2) = symétrique de P par rapport à C (rôles inversés)")

print("Q8  OAEH rectangle")
ok(same(H, pt(-2, 0)) and collinear(O, I, H) and perp(E, H, O, I), "H(−2 ; 0) projeté de E sur (OI)")
ok(same(mid(O, E), pt(-1, sqrt(2))) and same(mid(A, H), pt(-1, sqrt(2))), "milieux de [OE] et [AH] = (−1 ; √2)")
ok(simplify(dist(O, E) - 2 * sqrt(3)) == 0 and simplify(dist(A, H) - 2 * sqrt(3)) == 0, "OE = AH = 2√3")
ok(simplify(dist(O, A) - dist(E, H)) == 0 and simplify(dist(O, A) - 2 * sqrt(2)) == 0 and simplify(dist(O, H) - dist(A, E)) == 0 and dist(O, H) == 2, "OA = EH = 2√2 ; OH = AE = 2")
ok(simplify(2 * (dist(O, A) + dist(O, H)) - (4 + 4 * sqrt(2))) == 0, "périmètre = 4 + 4√2")
ok(perp(O, A, O, H) and perp(A, E, O, A) and perp(E, H, H, O), "trois angles droits en O, A, H (donc rectangle)")
# contre-exemples : parallélogramme non rectangle (milieu commun, côtés opposés égaux) ; trapèze rectangle (un angle droit)
p1, p2, p3, p4 = pt(0, 0), pt(1, 2), pt(3, 2), pt(2, 0)
ok(same(mid(p1, p3), mid(p2, p4)) and simplify(dist(p1, p2) - dist(p3, p4)) == 0 and not perp(p1, p2, p1, p4), "contre-exemple : parallélogramme non rectangle (diagonales de même milieu, côtés opposés égaux)")
t1, t2, t3, t4 = pt(0, 0), pt(0, 2), pt(1, 2), pt(3, 0)
ok(perp(t1, t2, t1, t4) and not perp(t2, t3, t3, t4) and not same(mid(t1, t3), mid(t2, t4)), "contre-exemple : trapèze rectangle (un angle droit seulement)")

print("Q9  KA")
ok(same(mid(B, C), K) and simplify(dist(K, A) - 3) == 0 and simplify(sqrt((0 - (-1)) ** 2 + (2 * sqrt(2)) ** 2) - 3) == 0, "KA = √(1 + 8) = 3")
ok(d2(K, A) == 9 and simplify(sqrt(8 - 1) - sqrt(7)) == 0 and simplify(1 + 2 * sqrt(2) - 3) != 0, "distracteurs : 9 = KA² ; √7 = √(8 − 1) ; 1 + 2√2 ≠ 3")

print("Q10  E appartient au cercle de diamètre [BC]")
ok(dist(K, B) == 3 and dist(K, C) == 3 and same(K, mid(B, C)), "centre K, rayon 3")
ok(dist(K, H) == 1 and simplify(dist(H, E) - 2 * sqrt(2)) == 0 and perp(K, H, H, E), "KH = 1 ; HE = 2√2 ; KHE rectangle en H")
ok(d2(K, E) == 1 + 8 == 9 and dist(K, E) == 3, "KE² = 1 + 8 = 9 ⇒ KE = 3 = KB : E sur le cercle")
ok(between(H, B, C) and perp(E, H, B, C), "H ∈ [BC] et (EH) ⊥ (BC) : prémisses vraies de l'option « perpendiculaire seule »")
Eb = pt(-2, 1)
ok(between(H, B, C) and perp(Eb, H, B, C) and d2(K, Eb) == 2 and d2(K, Eb) != 9, "contre-exemple : E' = (−2 ; 1) vérifie les mêmes prémisses mais n'est pas sur le cercle")
Mo = mid(O, E)
rad = dist(Mo, O)
ok(same(Mo, pt(-1, sqrt(2))) and simplify(rad - sqrt(3)) == 0 and all(simplify(dist(Mo, X) - sqrt(3)) == 0 for X in (O, A, E, H)), "cercle de diamètre [OE] : centre (−1 ; √2), rayon √3, passe par O, A, E, H")
ok(simplify(dist(Mo, B) - sqrt(3)) != 0 and not same(Mo, K), "ce cercle n'est PAS le cercle de diamètre [BC] (B n'y est pas ; centres différents)")
ok(simplify(dist(H, E) - 3) < 0 and simplify(dist(H, E) - 2 * sqrt(2)) == 0 and simplify(dist(H, Eb)) == 1 and 1 < 3, "EH = 2√2 < 3 est vrai mais E' (EH' = 1 < 3) n'est pas sur le cercle : l'argument « EH < rayon » ne prouve rien")
ok(R(-4) < H[0] < 2, "abscisse de H (−2) entre celles de B (−4) et C (2)")
print("M40 : toutes les vérifications passent")
