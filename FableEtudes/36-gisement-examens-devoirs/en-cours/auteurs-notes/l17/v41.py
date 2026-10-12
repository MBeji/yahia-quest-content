# Double résolution mission 41 : coordonnées exactes (sympy) + chemins du cours (Pythagore et sa réciproque, Thalès en papillon, aires).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from geo import *
from sympy import sqrt, Rational as R, simplify, symbols, S, Eq, solve
import m41_figs as F

A, B, C, D, O, I, H, J, K, L = F.A, F.B, F.C, F.D, F.O, F.I, F.H, F.J, F.K, F.L


def ok(cond, msg):
    assert cond, "ÉCHEC : " + msg
    print("  ok :", msg)


def eqv(x, y):
    return simplify(x - y) == 0


print("Q1  BI")
ok(eqv(dist(B, I), 2 * sqrt(5)) and perp(B, C, C, I) and 16 + 4 == 20, "BI = √20 = 2√5 (coordonnées ; Pythagore dans BCI rectangle en C)")
ok(eqv(sqrt(16 - 4), 2 * sqrt(3)) and 4 + 2 == 6 and 20 == dist(B, I) ** 2, "distracteurs : 2√3 = √(16 − 4) ; 6 = 4 + 2 ; 20 = BI²")
vals = [2 * sqrt(3), 6, 2 * sqrt(5), 20]
ok(len({simplify(v) for v in vals}) == 4 and not any(eqv(vals[k], vals[i] + vals[j]) or eqv(vals[k], vals[i] - vals[j]) for k in range(4) for i in range(4) for j in range(4) if len({i, j, k}) == 3), "valeurs distinctes, aucune somme/différence de deux autres")

print("Q2  AC")
ok(eqv(dist(A, C), 4 * sqrt(5)) and perp(A, B, B, C) and 64 + 16 == 80, "AC = √80 = 4√5")
ok(eqv(sqrt(64 - 16), 4 * sqrt(3)) and 8 + 4 == 12 and dist(A, C) ** 2 == 80, "distracteurs : 4√3 = √(64 − 16) ; 12 = 8 + 4 ; 80 = AC²")
vals = [4 * sqrt(3), 4 * sqrt(5), 12, 80]
ok(len({simplify(v) for v in vals}) == 4 and not any(eqv(vals[k], vals[i] + vals[j]) or eqv(vals[k], vals[i] - vals[j]) for k in range(4) for i in range(4) for j in range(4) if len({i, j, k}) == 3), "valeurs distinctes, aucune somme/différence de deux autres")

print("Q3  rapports (papillon)")
HC, HA, HI, HB, AC, BI = dist(H, C), dist(H, A), dist(H, I), dist(H, B), dist(A, C), dist(B, I)
CI, AB, BC = dist(C, I), dist(A, B), dist(B, C)
ok(par(C, I, A, B) and between(H, A, C) and between(H, B, I), "(CI) ∥ (AB) ; H entre A et C et entre B et I (papillon de sommet H)")
ok(eqv(HC / HA, CI / AB) and eqv(HI / HB, HC / HA) and eqv(HC / HA, R(1, 4)), "vraies : HC/HA = CI/AB ; HI/HB = HC/HA ; HC/HA = 1/4")
ok(not eqv(HC / AC, R(1, 4)) and eqv(HC / AC, R(1, 5)), "fausse : HC/AC = 1/5 ≠ 1/4")
ok(not eqv(HC / HA, CI / BC) and eqv(CI / BC, R(1, 2)), "fausse : CI/BC = 1/2 ≠ HC/HA")
ok(not eqv(HC / HA, AB / CI) and eqv(AB / CI, 4), "fausse : AB/CI = 4 ≠ HC/HA")

print("Q4  HC")
ok(eqv(HC, 4 * sqrt(5) / 5) and eqv(HA, 16 * sqrt(5) / 5) and eqv(HC + HA, AC), "HC = 4√5/5 ; HA = 16√5/5 ; HC + HA = AC")
ok(eqv(AC / 4, sqrt(5)) and not eqv(HC, sqrt(5)), "distracteur √5 = AC/4 (rapport partiel pris pour rapport au tout)")
ok(eqv(HA, 16 * sqrt(5) / 5) and eqv(4 * AC, 16 * sqrt(5)), "distracteurs 16√5/5 = HA ; 16√5 = 4 × AC")
vals = [4 * sqrt(5) / 5, sqrt(5), 16 * sqrt(5) / 5, 16 * sqrt(5)]
ok(len({simplify(v) for v in vals}) == 4 and not any(eqv(vals[k], vals[i] + vals[j]) or eqv(vals[k], vals[i] - vals[j]) for k in range(4) for i in range(4) for j in range(4) if len({i, j, k}) == 3), "valeurs distinctes, aucune somme/différence de deux autres")

print("Q5  HB")
ok(eqv(HB, 8 * sqrt(5) / 5) and eqv(HI, 2 * sqrt(5) / 5) and eqv(HB + HI, BI), "HB = 8√5/5 ; HI = 2√5/5 ; HB + HI = BI")
ok(eqv(BI - BI / 4, 3 * sqrt(5) / 2) and not eqv(HB, 3 * sqrt(5) / 2), "distracteur 3√5/2 = BI − BI/4 (HI pris pour BI/4, puis HB = BI − HI)")
ok(eqv(4 * BI, 8 * sqrt(5)) and not eqv(HB, 8 * sqrt(5)), "distracteur 8√5 = 4 × BI")
vals = [3 * sqrt(5) / 2, 2 * sqrt(5) / 5, 8 * sqrt(5), 8 * sqrt(5) / 5]
ok(len({simplify(v) for v in vals}) == 4 and not any(eqv(vals[k], vals[i] + vals[j]) or eqv(vals[k], vals[i] - vals[j]) for k in range(4) for i in range(4) for j in range(4) if len({i, j, k}) == 3), "valeurs distinctes, aucune somme/différence de deux autres")

print("Q6  (AC) ⊥ (BI)")
ok(eqv(HC ** 2, R(16, 5)) and eqv(HB ** 2, R(64, 5)) and eqv(HC ** 2 + HB ** 2, 16) and eqv(BC ** 2, 16), "HC² + HB² = 16/5 + 64/5 = 16 = BC²")
ok(perp(A, C, B, I) and perp(H, C, H, B) and not perp(B, H, B, C), "angle droit en H (réciproque de Pythagore) ; pas en B")
ok(AB ** 2 + BC ** 2 == 80 == AC ** 2 and perp(A, B, B, C), "AB² + BC² = 64 + 16 = 80 = AC² : ABC rectangle en B (prémisse vraie de l'option « mauvais triangle »)")
ok(eqv(HI ** 2 + HC ** 2, CI ** 2), "(info) HCI est aussi rectangle en H : une autre route valable, volontairement absente des options")

print("Q7  (OJ) ⊥ (BC)")
ok(same(O, mid(A, C)) and same(J, mid(B, C)) and par(O, J, A, B) and perp(O, J, B, C), "O milieu de [AC], J milieu de [BC] : (OJ) ∥ (AB) ⊥ (BC), donc (OJ) ⊥ (BC)")
ok(eqv(dist(O, J), AB / 2) and eqv(dist(O, J), 4) and eqv(BC, 4), "OJ = AB/2 = 4 = BC (prémisse vraie de l'option « longueurs égales »)")
ok(not par(O, J, A, C) and not perp(A, C, B, C), "(OJ) ∦ (AC) ; (AC) non perpendiculaire à (BC) : l'option « côté faux » a une prémisse fausse")
# contre-exemple : parallélogramme avec OJ = BC sans perpendicularité
a2, b2, c2 = pt(0, 0), pt(8, 0), pt(10, 4)
o2, j2 = mid(a2, c2), mid(b2, c2)
ok(simplify(dist(o2, j2) - dist(a2, b2) / 2) == 0 and not perp(o2, j2, b2, c2), "contre-exemple : une égalité de longueurs n'implique pas la perpendicularité")

print("Q8  (CK) ⊥ (OB) : orthocentre du triangle OBC")
ok(collinear(B, K, H) and collinear(B, K, I) and perp(B, K, O, C) and collinear(O, H, C), "(BK) = (BI) ⊥ (AC) = (OC) : altitude de B dans OBC")
ok(collinear(O, K, J) and perp(O, K, B, C), "(OK) = (OJ) ⊥ (BC) : altitude de O dans OBC")
ok(perp(C, K, O, B) and same(K, inter(B, H, O, J)), "(CK) ⊥ (OB) : troisième altitude")
G = centroid(O, B, C)
ok(not same(G, K) and not collinear(C, K, mid(O, B)), "K n'est pas le centre de gravité de OBC ; (CK) n'est pas une médiane (option « médianes » fausse)")
ok(not perp(B, K, O, B) and perp(B, K, O, C), "une seule altitude (BK) ne dit rien de (CK) à elle seule (option « une altitude »)")

print("Q9  CL")
OB, OC, OJ, CL = dist(O, B), dist(O, C), dist(O, J), dist(C, L)
ok(eqv(OB, 2 * sqrt(5)) and eqv(OC, 2 * sqrt(5)) and eqv(OJ, 4) and eqv(BC, 4), "OB = OC = 2√5 ; OJ = 4 ; BC = 4")
ok(eqv(area_tri(O, B, C), 8) and eqv(BC * OJ / 2, 8) and eqv(OB * CL / 2, 8), "aire OBC = (BC × OJ)/2 = 8 = (OB × CL)/2")
ok(eqv(CL, 8 * sqrt(5) / 5) and eqv(16 / OB, CL), "CL = 16/OB = 8/√5 = 8√5/5")
ok(eqv(8 / OB, 4 * sqrt(5) / 5) and not eqv(CL, 4 * sqrt(5) / 5) and eqv(dist(B, L), 4 * sqrt(5) / 5), "distracteur 4√5/5 = 8/OB (aire sans moitié) = BL")
ok(not eqv(CL, 4) and not eqv(CL, 2 * sqrt(5)), "distracteurs 4 (= OJ) et 2√5 (= OB) ≠ CL")
vals = [2 * sqrt(5), 4, 8 * sqrt(5) / 5, 4 * sqrt(5) / 5]
ok(len({simplify(v) for v in vals}) == 4 and not any(eqv(vals[k], vals[i] + vals[j]) or eqv(vals[k], vals[i] - vals[j]) for k in range(4) for i in range(4) for j in range(4) if len({i, j, k}) == 3), "valeurs distinctes, aucune somme/différence de deux autres")
ok(simplify(max(vals) - 4) > 0 and simplify(8 * sqrt(5) / 5 - 4) < 0, "(info) clé ni minimum ni maximum")

print("Q10  aire de CLB")
BL = dist(B, L)
ok(eqv(BL ** 2, R(16, 5)) and eqv(BL, 4 * sqrt(5) / 5) and eqv(BC ** 2 - CL ** 2, BL ** 2) and perp(C, L, L, B), "BL² = 16 − 64/5 = 16/5 ; BL = 4√5/5 (CLB rectangle en L)")
ok(eqv(CL * BL / 2, R(16, 5)) and eqv(area_tri(C, L, B), R(16, 5)) and float(R(16, 5)) == 3.2, "aire CLB = (CL × BL)/2 = 16/5 = 3,2")
ok(eqv(CL * BL, R(32, 5)) and float(R(32, 5)) == 6.4, "distracteur : sans la moitié 32/5 = 6,4")
ok(eqv(BC * CL / 2, 16 * sqrt(5) / 5), "distracteur : BC comme base et CL comme hauteur : 16√5/5 (≠ 16/5)")
print("M41 : toutes les vérifications passent")
