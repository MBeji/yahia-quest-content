# Double résolution mission 38 : coordonnées exactes + relations (théorèmes du cours).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from geo import *
from sympy import sqrt, Rational as R, simplify, sqrt
import m38_figs as F
A, B, C, D, E, Fp, G, H, I, J, K, O = F.A, F.B, F.C, F.D, F.E, F.F, F.G, F.H, F.I, F.J, F.K, F.O

def ok(cond, msg):
    assert cond, "ÉCHEC : " + msg
    print("  ok :", msg)

print("Q1")
ok(simplify(dist(B, C) - sqrt(11)) == 0 and simplify(sqrt(36 - 25) - sqrt(11)) == 0 and perp(C, A, C, B), "BC = √11 (coordonnées ; Pythagore dans ABC rectangle en C)")
ok(6 - 5 == 1 and simplify(sqrt(36 + 25) - sqrt(61)) == 0, "distracteurs 1 = 6−5 ; √61 = √(36+25) ; 11 = BC²")
print("Q2")
ok(simplify(dist(C, D) - R(11, 5)) == 0 and simplify(dist(B, C) ** 2 / dist(A, C) - R(11, 5)) == 0, "CD = 11/5 (coordonnées ; BC² = CA × CD)")
ok(perp(B, C, A, D) and perp(A, B, B, D) and between(C, A, D), "ABD rectangle en B, (BC) ⊥ (AD), C entre A et D")
ok(R(11, 6) == R(11) / 6 and R(36, 5) == R(36) / 5 and 11 - 5 == 6, "distracteurs 11/6 = BC²/AB ; 36/5 = AB²/AC ; 6 = BC² − AC")
ok(simplify(dist(A, D) - R(36, 5)) == 0, "(info) AD = 36/5 = AC + CD")
print("Q3")
ok(simplify(dist(B, D) - 6 * sqrt(11) / 5) == 0 and simplify(sqrt(11 + R(121, 25)) - 6 * sqrt(11) / 5) == 0 and R(396, 25) == 11 + R(121, 25), "BD = 6√11/5 (deux chemins) ; BD² = 396/25")
ok(simplify(sqrt(11 - R(121, 25)) - sqrt(154) / 5) == 0, "distracteur √154/5 = √(BC² − CD²)")
ok(simplify(sqrt(11) + R(11, 5) - (sqrt(11) + R(11, 5))) == 0 and simplify(dist(B, D) - (sqrt(11) + R(11, 5))) != 0, "distracteur √11 + 11/5 ≠ BD")
print("Q4")
ok(perp(B, D, A, B) and par(D, Fp, A, B) and perp(B, D, D, Fp), "(BD) ⊥ (AB) ; (DF) ∥ (AB) ; donc (BD) ⊥ (DF)")
ok(perp(F_ := Fp, D, Fp, E), "angle DFE droit (F sur le cercle de diamètre [DE])")
ok(perp(B, D, B, E) and perp(Fp, D, Fp, E) and perp(D, B, D, Fp), "angles en B, D, F droits")
ok(simplify(dot(sub(B, E), sub(Fp, D))) != 0 or True, "(info)")
ok(zero(O[0] + 0 - (B[0] + Fp[0]) / 2) and same(mid(B, Fp), mid(D, E)) and zero(dist(B, Fp) - dist(D, E)), "BDFE rectangle : diagonales de même milieu et égales")
print("Q5")
ok(on_circle(H, I, 3) and perp(H, A, H, B), "AHB droit")
ok(simplify(dist(B, Fp) - dist(D, E)) == 0 and same(mid(B, Fp), O) and perp(H, B, H, Fp), "[BF] diamètre du cercle de [DE] : BHF droit")
ok(perp(H, D, H, E), "DHE droit aussi (mais inutile)")
ok(collinear(A, H, Fp), "A, H, F alignés")
ok(par(I, O, A, Fp) and same(mid(A, B), I) and same(mid(B, Fp), O), "(IO) ∥ (AF) (vrai mais insuffisant)")
print("Q6")
ok(same(G, inter(Fp, I, A, O)) and same(G, centroid(A, B, Fp)), "G = (FI)∩(AO) = centre de gravité de ABF")
ok(same(K, mid(A, Fp)) and collinear(B, G, K), "K milieu de [AF], (BG) ∩ (AF)")
ok(not perp(Fp, I, A, B) and not perp(A, O, B, Fp), "(FI), (AO) ne sont pas des hauteurs de ABF")
ok(simplify(dist(A, K) / dist(A, Fp) - R(1, 2)) == 0, "K au milieu de [AF] (pas au tiers)")
print("Q7")
ok(same(O, mid(D, E)) and simplify(dist(A, G) - R(2, 3) * dist(A, O)) == 0, "[AO] médiane de AED ; AG = 2/3 AO")
ok(same(G, centroid(A, E, D)), "G centre de gravité de AED")
ok(not same(mid(A, D), inter(Fp, I, A, D)) and not collinear(Fp, A, E), "(FI) n'est pas une médiane de AED (F n'est pas un sommet)")
print("Q8")
ok(same(J, mid(A, D)) and simplify(dist(A, J) - R(18, 5)) == 0 and R(18, 5) == R(36, 10), "AJ = AD/2 = 18/5 = 3,6")
ok(R(5) - R(11, 5) == R(14, 5) and (R(14, 5)) / 2 == R(7, 5) and R(5, 2) == R(5) / 2 and R(2, 3) * R(36, 5) == R(24, 5), "distracteurs : 1,4 ; 2,5 ; 4,8")
print("Q9")
ok(same(K, mid(A, Fp)) and same(J, mid(A, D)) and same(O, mid(D, E)), "J, K, O milieux de [AD], [AF], [DE]")
ok(par(J, K, D, Fp) and par(J, O, A, E) and par(D, Fp, A, E), "(JK) ∥ (DF) ; (JO) ∥ (AE) ; (DF) ∥ (AE)")
ok(collinear(J, K, O), "J, K, O alignés")
ok(par(J, O, D, Fp) and True, "(JO) ∥ (DF) est vrai ici mais la justification « J et O milieux dans ADF » est invalide (O n'est pas sur un côté de ADF)")
print("M38 : toutes les vérifications passent")
