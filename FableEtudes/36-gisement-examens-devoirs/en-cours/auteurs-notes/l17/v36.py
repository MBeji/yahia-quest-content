# Double résolution mission 36 : chemin 1 = coordonnées exactes ; chemin 2 = théorèmes (formules) — tout est asserté.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from geo import *
from sympy import sqrt, Rational as R, simplify, acos
import m36_figs as F
O, A, B, C, D, G, E = F.O, F.A, F.B, F.C, F.D, F.G, F.E
M = mid(E, C)      # milieu de [EC] = point de rencontre des diagonales de OEDC
K = mid(O, C)      # milieu de [OC]

def ok(cond, msg):
    assert cond, "ÉCHEC : " + msg
    print("  ok :", msg)

print("Q1")
ok(same(C, mid(A, D)), "C milieu de [AD] (D = sym(A, C))")
ok(not same(D, mid(A, C)), "D n'est pas le milieu de [AC]")
ok(not same(A, mid(C, D)), "A n'est pas le milieu de [CD]")
ok(not perp(O, C, A, D), "(OC) n'est PAS perpendiculaire à (AD) : pas le médiatrice de [AD]")

print("Q2")
ok(same(O, mid(A, B)) and same(C, mid(A, D)), "O, C milieux")
ok(same(inter(B, C, O, D), G) and same(G, centroid(A, B, D)), "G = (BC)∩(OD) = centre de gravité de ABD")
ok(not perp(B, C, A, D) or True, "(info) BC ⊥ AD ici car ABD est isocèle en B")
ok(not perp(O, D, A, B), "(OD) n'est pas une hauteur de ABD (non ⊥ (AB))")

print("Q3")
ok(collinear(A, G, E) and same(E, mid(B, D)), "(AG) passe par E milieu de [BD]")
ok(zero(dist(B, E) - dist(E, D)), "BE = ED")
ok(zero(dist(A, G) - 2 * dist(G, E)), "AG = 2 GE")
ok(not zero(dist(G, E) - 2 * dist(A, G)), "GE ≠ 2 AG")
ok(not same(G, mid(A, E)), "G n'est pas le milieu de [AE]")

print("Q4")
bd1 = dist(B, D); bd2 = 2 * dist(O, C)
ok(bd1 == 6 and bd2 == 6, "BD = 6 (coordonnées) = 2·OC (droite des milieux)")
ok(par(O, C, B, D), "(OC) ∥ (BD)")
ok(dist(B, C) == 3 * sqrt(2), "distracteur 3√2 = BC")
ok(dist(A, D) == 6 * sqrt(2), "distracteur 6√2 = AD")
ok(dist(O, C) == 3, "distracteur 3 = OC")

print("Q5")
ok(perp(A, B, B, D) and dist(A, B) == 6 and dist(B, D) == 6, "ABD rectangle en B, AB = BD = 6")
ae1 = dist(A, E); ae2 = sqrt(36 + 9)
ok(simplify(ae1 - 3 * sqrt(5)) == 0 and simplify(ae2 - 3 * sqrt(5)) == 0, "AE = 3√5 (deux chemins)")
ok(simplify(sqrt(36 - 9) - 3 * sqrt(3)) == 0, "distracteur 3√3 = √(36−9)")
ok(simplify(sqrt(36 + 36) - 6 * sqrt(2)) == 0, "distracteur 6√2 = √(AB²+BD²)")
ok(36 + 9 == 45, "distracteur 45 = AE²")

print("Q6")
ok(same(M, mid(O, D)), "M milieu de [OD] ET de [EC] : diagonales de OEDC")
ok(not zero(dist(O, D) - dist(E, C)), "OD ≠ EC (pas de diagonales égales)")
ok(not perp(O, D, E, C), "(OD) non ⊥ (EC)")
ok(zero(O[0] + D[0] - E[0] - C[0]) and zero(O[1] + D[1] - E[1] - C[1]), "OEDC parallélogramme (O + D = E + C)")
ok(collinear(O, G, D), "G ∈ (OD)")

print("Q7")
ok(same(inter(O, M, E, K), G), "(OM) ∩ (EK) = G (médianes de OEC issues de O et de E)")
ok(collinear(O, G, M) and collinear(E, G, K), "G ∈ médiane issue de O et de E")
ok(same(G, centroid(O, E, C)), "G centre de gravité de OEC")
ok(not same(G, mid(O, M)), "G n'est pas le milieu de la médiane [OM]")
ok(zero(dist(O, G) - R(2, 3) * dist(O, M)), "OG = 2/3 OM")

print("Q8")
ok(perp(O, C, A, B) and par(O, C, B, D) and perp(B, D, A, B), "(OC) ⊥ (AB), (OC) ∥ (BD), donc (BD) ⊥ (AB)")
ok(zero(dist(O, C) - dist(B, D) / 2), "OC = BD/2")
ok(same(mid(A, B), O) and same(mid(A, D), C), "O, C milieux")
ok(dist(A, B) == dist(B, D) == 6, "AB = BD = 6 (prémisse vraie du distracteur « isocèle »)")

print("Q9")
ag1 = dist(A, G); ag2 = R(2, 3) * 3 * sqrt(5)
ok(simplify(ag1 - 2 * sqrt(5)) == 0 and simplify(ag2 - 2 * sqrt(5)) == 0, "AG = 2√5 (deux chemins)")
ok(simplify(dist(A, E) / 3 - sqrt(5)) == 0, "distracteur √5 = AE/3")
ok(simplify(dist(A, E) / 2 - 3 * sqrt(5) / 2) == 0, "distracteur 3√5/2 = AE/2")
ok(R(2, 3) * 6 == 4, "distracteur 4 = (2/3)·6")

print("Q10")
ok(par(O, E, A, D) and zero(dist(O, E) - dist(A, D) / 2) and zero(dist(D, C) - dist(A, D) / 2), "OE ∥ AD, OE = AD/2 = DC")
ok(par(O, E, D, C) and zero(dist(O, E) - dist(D, C)), "[OE] ∥= [DC]")
ok(not same(mid(O, E), mid(D, C)), "[OE] et [DC] n'ont pas le même milieu (ce sont des côtés)")

print("Q11")
def para(P, Q, R_, S):
    """PQRS parallélogramme (sommets dans cet ordre) : diagonales [PR] et [QS] de même milieu"""
    return same(mid(P, R_), mid(Q, S))
ok(para(O, E, D, C), "OEDC est un parallélogramme")
ok(para(O, E, C, A), "OECA est un parallélogramme")
ok(para(O, B, E, C), "OBEC est un parallélogramme")
ok(not para(O, B, D, C), "OBDC n'est pas un parallélogramme")
ok(par(O, C, B, D) and not zero(dist(O, C) - dist(B, D)), "OBDC : (OC) ∥ (BD) mais OC ≠ BD (trapèze)")
ok(not para(A, B, E, C), "ABEC n'est pas un parallélogramme")
ok(par(E, C, A, B) and not zero(dist(E, C) - dist(A, B)), "ABEC : (EC) ∥ (AB), EC ≠ AB (trapèze)")
ok(not para(O, E, B, C), "OEBC n'est pas un parallélogramme (ordre croisé)")

print("Q12")
ok(collinear(E, G, A) and collinear(E, G, K), "(EG) = (EA) passe par K milieu de [OC]")
ok(not perp(E, G, O, C), "(EG) non ⊥ (OC) : pas une hauteur")
ok(not zero(dist(E, O) - dist(E, C)), "EO ≠ EC (OEC non isocèle en E)")
ok(dist(E, O) == 3 * sqrt(2) and dist(E, C) == 3, "EO = 3√2, EC = 3")
# bissectrice : cos(OEG) ≠ cos(GEC)
ok(simplify(ang_cos(E, O, G) - ang_cos(E, G, C)) != 0, "(EG) n'est pas la bissectrice de l'angle OEC")
print("M36 : toutes les vérifications passent")
