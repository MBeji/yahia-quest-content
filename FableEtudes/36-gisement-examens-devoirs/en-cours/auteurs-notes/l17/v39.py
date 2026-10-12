# Double résolution mission 39 : coordonnées exactes (sympy, paramètre a symbolique) + chemins du cours.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from geo import *
from sympy import sqrt, Rational as R, simplify, symbols, expand, solve, Eq, S, Abs, nsimplify, factor
import m39_figs as F

a, x = symbols("a x", positive=True)


def ok(cond, msg):
    assert cond, "ÉCHEC : " + msg
    print("  ok :", msg)


A, B, C = pt(0, 0), pt(4, 0), pt(0, 3)
M = (4 - 4 * a / 5, 3 * a / 5)          # M = B + (a/5)(C − B), BM = a
H = (M[0], S(0)); K = (S(0), M[1])
E = x ** 2 - R(32, 5) * x + 16


def ln(p, q):
    """longueur symbolique pour 0 < a < 5 (Abs(a − 5) = 5 − a)"""
    return simplify(sqrt(d2(p, q))).subs(Abs(a - 5), 5 - a)


print("Q1  E(5)")
ok(E.subs(x, 5) == 9 and 25 - 32 + 16 == 9, "E(5) = 9 (substitution directe)")
ok(R(173, 5) == 25 - R(32, 5) + 16 and 10 - 32 + 16 == -6 and 25 + 32 + 16 == 73, "distracteurs : 173/5 ; −6 ; 73 (les trois erreurs citées)")
ok(len({9, R(173, 5), -6, 73}) == 4, "quatre valeurs distinctes")

print("Q2  BC")
ok(dist(B, C) == 5 and 16 + 9 == 25 and perp(A, B, A, C), "BC = 5 (coordonnées ; Pythagore)")
ok(4 + 3 == 7 and simplify(sqrt(16 - 9) - sqrt(7)) == 0 and 5 not in (7, sqrt(7), 25), "distracteurs : 7 = 4+3 ; √7 = √(16−9) ; 25 = BC²")

print("Q3  développement")
ok(expand((x - R(16, 5)) ** 2) == x ** 2 - R(32, 5) * x + R(256, 25), "(x − 16/5)² = x² − (32/5)x + 256/25")
ok(expand((x - R(16, 5)) ** 2 + R(12, 5) ** 2 - E) == 0, "E = (x − 16/5)² + (12/5)² (identité du sujet)")
ok(R(256, 25) + R(144, 25) == 16 and (256 + 144) // 25 == 16, "constante : (256 + 144)/25 = 400/25 = 16")
for nm, d in (("x² + 256/25", x ** 2 + R(256, 25)), ("x² − (16/5)x + 256/25", x ** 2 - R(16, 5) * x + R(256, 25)), ("x² − 256/25", x ** 2 - R(256, 25))):
    ok(expand(d - (x - R(16, 5)) ** 2) != 0, f"distracteur « {nm} » ≠ (x − 16/5)²")
ok(expand((x - R(16, 5)) ** 2 - (x ** 2 - R(32, 5) * x - R(256, 25))) != 0, "(info) variante de signe exclue des options")

print("Q4  HM")
HM = ln(H, M)
ok(simplify(HM - 3 * a / 5) == 0, "HM = 3a/5 (coordonnées symboliques)")
ok(par(H, M, A, C) and perp(M, H, A, B) and simplify(ln(B, M) - a) == 0, "(HM) ∥ (AC) ; (HM) ⊥ (AB) ; BM = a")
ok(simplify(a / 5 - HM / 3) == 0, "Thalès : BM/BC = HM/AC (a/5 = HM/3)")
for nm, d in (("(5/3)a", 5 * a / 3), ("(4/5)a", 4 * a / 5), ("a − 2", a - 2)):
    ok(simplify(d - HM) != 0, f"distracteur « {nm} » ≠ HM")
ok(solve(Eq(a - 2, 3 * a / 5), a) == [5], "a − 2 = 3a/5 seulement pour a = 5 (exclu : 0 < a < 5)")

print("Q5  propriétés du rectangle AHMK")
AM2 = simplify(d2(A, M)); HK2 = simplify(d2(H, K))
ok(simplify(AM2 - HK2) == 0, "AM = HK (diagonales égales) pour tout a")
KM = ln(K, M); AH = ln(A, H)
ok(simplify(KM - AH) == 0, "KM = AH pour tout a")
ok(par(M, K, A, B), "(MK) ∥ (AB) pour tout a")
perp_cond = simplify(dot(sub(M, A), sub(K, H)))
sols_perp = [v for v in solve(perp_cond, a) if 0 < v < 5]
ok(sols_perp == [R(20, 7)], f"(AM) ⊥ (HK) seulement si a = 20/7 (carré) dans ]0, 5[ : faux en général (solutions {solve(perp_cond, a)})")
sols_eq = [v for v in solve(Eq(HM**2, KM**2), a) if 0 < v < 5]
ok(sols_eq == [R(20, 7)], f"HM = KM seulement si a = 20/7 dans ]0, 5[ : faux en général (solutions {solve(Eq(HM**2, KM**2), a)})")
ok(all(((AH + HM) ** 2 - AM2).subs(a, v) > 0 for v in (R(1, 10), 1, 2, R(5, 2), 4, R(499, 100))), "AM² < (AH + HM)² sur un balayage de a ∈ ]0, 5[ : AM ≠ AH + HM")
ok(simplify(AM2 - (AH ** 2 + HM ** 2)) == 0, "AM² = AH² + HM² (Pythagore dans AHM)")

print("Q6  KM")
ok(simplify(KM - R(4, 5) * (5 - a)) == 0, "KM = (4/5)(5 − a) (coordonnées)")
BH = ln(B, H)
ok(simplify(BH - 4 * a / 5) == 0 and simplify(AH - (4 - BH)) == 0, "chemin 2 : BH = 4a/5 (Thalès) ; AH = 4 − BH = KM")
CM = ln(C, M)
ok(simplify(CM - (5 - a)) == 0 and simplify(KM / 4 - CM / 5) == 0, "chemin 3 : Thalès dans CAB : KM/AB = CM/CB avec CM = 5 − a")
for nm, d in (("(3/5)(5 − a)", R(3, 5) * (5 - a)), ("(3/5)a", 3 * a / 5), ("4 − a", 4 - a)):
    ok(simplify(d - KM) != 0, f"distracteur « {nm} » ≠ KM")
ok(simplify(R(3, 5) * (5 - a) - ln(C, K)) == 0, "(3/5)(5 − a) = CK (segment mal choisi : AC au lieu de AB)")
ok(simplify(3 * a / 5 - HM) == 0 and simplify(4 - a - (4 - BH)).subs(a, 1) != 0, "(3/5)a = HM (résultat intermédiaire) ; 4 − a suppose BH = BM")

print("Q7  HK²")
target = a ** 2 - R(32, 5) * a + 16
ok(simplify(HK2 - target) == 0, "HK² = a² − (32/5)a + 16 (coordonnées)")
ok(expand((3 * a / 5) ** 2 + (R(4, 5) * (5 - a)) ** 2 - target) == 0, "Pythagore HM² + KM² = a² − (32/5)a + 16")
d_b = expand((3 * a / 5) ** 2 + R(16, 25) * (25 + a ** 2)); d_c = expand((3 * a / 5) ** 2 + R(16, 25) * (25 - a ** 2)); d_d = expand((3 * a / 5) ** 2 - (R(4, 5) * (5 - a)) ** 2)
ok(d_b == a ** 2 + 16, "distracteur « a² + 16 » = HM² + (4/5)²(25 + a²)")
ok(d_c == 16 - R(7, 25) * a ** 2, "distracteur « 16 − (7/25)a² » = HM² + (4/5)²(25 − a²)")
ok(d_d == -R(7, 25) * a ** 2 + R(32, 5) * a - 16, "distracteur « −(7/25)a² + (32/5)a − 16 » = HM² − KM²")
for nm, d in (("a²+16", d_b), ("16−(7/25)a²", d_c), ("−(7/25)a²+(32/5)a−16", d_d)):
    ok(expand(d - target) != 0, f"distracteur {nm} ≠ HK²")
# vote par composante : (coef a², coef a, const)
comp = {"cle": (1, -R(32, 5), 16), "b": (1, 0, 16), "c": (-R(7, 25), 0, 16), "d": (-R(7, 25), R(32, 5), -16)}
from collections import Counter
maj = tuple(Counter(v[i] for v in comp.values()).most_common(1)[0][0] for i in range(3))
ok(maj != comp["cle"], f"le vote majoritaire par composante {maj} ne reconstruit pas la clé")

print("Q8  pont AM = 12/5")
sol = solve(Eq(AM2, R(144, 25)), a)
ok(sol == [R(16, 5)] or R(16, 5) in sol, f"AM = 12/5 ⇒ a = 16/5 (solutions {sol})")
a0 = R(16, 5)
ok(HK2.subs(a, a0) == R(144, 25), "HK² = 144/25 pour a = 16/5")
ok(HM.subs(a, a0) == R(48, 25) and HM.subs(a, a0) != R(12, 5) and HM.subs(a, a0) ** 2 != R(144, 25), "HM = 48/25 : « HM = 12/5 » et « HM² = 144/25 » fausses")
ok(HK2.subs(a, a0) != R(12, 5), "« HK² = 12/5 » fausse")

# énoncé abstrait (rectangle AHMK quelconque de diagonale AM = 12/5) : HM < AM strictement, HK = AM
p, q = symbols("p q", positive=True)
ok(simplify(solve(Eq(p ** 2 + q ** 2, R(144, 25)), q)[0] ** 2 - (R(144, 25) - p ** 2)) == 0 and all(R(144, 25) - pv ** 2 < R(144, 25) for pv in (R(1, 10), 1, 2)),
   "rectangle de diagonale 12/5 : HM² = 144/25 − AH² < 144/25 donc HM < 12/5 : « HM = 12/5 » et « HM² = 144/25 » impossibles quelle que soit la forme")
ok(R(144, 25) != R(12, 5), "« HK² = 12/5 » fausse : HK = AM donne HK² = 144/25")

print("Q9  lecture de la forme canonique")
ok(simplify(AM2 - ((a - R(16, 5)) ** 2 + R(144, 25))) == 0, "AM² = (a − 16/5)² + (12/5)² pour tout a")
AMf = lambda v: sqrt(AM2.subs(a, v))
ok(all(AMf(v) >= R(12, 5) for v in (R(1, 10), R(1, 2), 1, 2, R(5, 2), R(16, 5), 4, R(49, 10), R(499, 100))), "AM ≥ 12/5 sur un balayage de a ∈ ]0, 5[")
ok(AMf(R(5, 2)) == R(5, 2) and R(5, 2) > R(12, 5), "au milieu : AM = 5/2 > 12/5 (donc « AM ≤ 12/5 » fausse)")
ok(AMf(2) != R(12, 5), "« AM = 12/5 » n'est pas vraie pour tout a")
ok(simplify(AMf(2) - ((2 - R(16, 5)) + R(12, 5))) != 0, "« AM = (a − 16/5) + 12/5 » fausse (a = 2)")

print("Q10  a")
ok(solve(Eq((a - R(16, 5)) ** 2 + R(144, 25), R(144, 25)), a) == [R(16, 5)] and 0 < R(16, 5) < 5, "a = 16/5 = 3,2 ∈ ]0, 5[")
ok(R(16, 5) == R(32, 10) and float(R(16, 5)) == 3.2, "16/5 = 3,2")
# chemin 2 : relation du cours AH × BC = AB × AC (hauteur 12/5) puis Pythagore dans ABM rectangle en M
alt = R(4 * 3, 5)
ok(alt == R(12, 5) and sqrt(16 - alt ** 2) == R(16, 5), "chemin 2 : hauteur 12/5 = AB × AC/BC ; BM = √(16 − 144/25) = 16/5")
ok(solve(Eq((a - R(16, 5)) ** 2, R(144, 25)), a) == [R(4, 5), R(28, 5)], "distracteurs : (a − 16/5)² = (12/5)² donne 4/5 ou 28/5 (28/5 > 5)")
ok(R(28, 5) > 5 and R(12, 5) != R(16, 5), "28/5 hors intervalle ; 12/5 est la valeur de AM, pas de a")

print("--- Tour de corrections (audit L17) ---")
print("m39-Q2 : options √7, 5, 25/2, 12")
ok(simplify(sqrt(25) - 5) == 0 and R(25, 2) != 5 and 4 * 3 == 12 and simplify(sqrt(16 - 9) - sqrt(7)) == 0, "BC = 5 ; 25/2 = BC²/2 ; 12 = 4 × 3 ; √7 = √(16−9)")
print("m39-Q6 : plan 2×2 {HM, HK} × {² , sans carré} pour la valeur 144/25")
a0 = R(16, 5)
HKv = sqrt(HK2.subs(a, a0)); HMv = HM.subs(a, a0)
ok(HKv == R(12, 5) and HMv == R(48, 25), "a = 16/5 : HK = 12/5, HM = 48/25")
ok(HKv ** 2 == R(144, 25), "HK² = 144/25 (clé)")
ok(HKv != R(144, 25), "HK = 144/25 fausse")
ok(HMv != R(144, 25), "HM = 144/25 fausse")
ok(HMv ** 2 != R(144, 25), "HM² = 144/25 fausse")
# générique : rectangle de diagonale 12/5 : HM < 12/5 donc HM² < 144/25 < 144/25 ... et HM = 144/25 = 5,76 > 12/5 impossible
ok(R(144, 25) > R(12, 5), "144/25 = 5,76 > 12/5 : « HM = 144/25 » et « HK = 144/25 » impossibles (côté/diagonale ≤ 12/5)")
print("m39-Q8 : clé (9/25)a² + (16/25)(5 − a)² et distracteurs")
sq = lambda e: expand(e)
keyx = R(9, 25) * a ** 2 + R(16, 25) * (5 - a) ** 2
ok(simplify(HK2 - keyx) == 0, "HK² = HM² + KM² = (9/25)a² + (16/25)(5 − a)² (coordonnées)")
ok(simplify(HM ** 2 - R(9, 25) * a ** 2) == 0 and simplify(sq(KM ** 2) - sq(R(16, 25) * (5 - a) ** 2)) == 0 if 'KM' in globals() else True, "HM² = (9/25)a² ; KM² = (16/25)(5−a)²")
for nm, e in (("(3/5)a + (4/5)(5−a)", R(3, 5) * a + R(4, 5) * (5 - a)),
              ("(16/25)(5−a)² − (9/25)a²", R(16, 25) * (5 - a) ** 2 - R(9, 25) * a ** 2),
              ("(9/25)a² + (4/5)(5−a)²", R(9, 25) * a ** 2 + R(4, 5) * (5 - a) ** 2)):
    ok(expand(e - HK2) != 0, f"distracteur {nm} ≠ HK²")
print("m39-Q9 a : « AM ≤ 12/5 » fausse (étiquette ordre-inverse-a-tort)")
print("M39 corrections : ok")
print("M39 : toutes les vérifications passent")
