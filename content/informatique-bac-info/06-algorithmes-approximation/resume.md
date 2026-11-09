# 📜 Résumé : Les algorithmes d'approximation

- **Point fixe** : x tel que f(x) = x ; on l'approche par U(n+1) = f(U(n)) en s'arrêtant quand |xact − xpre| < Epsilon, si la suite converge (f(x) = 2x − 1 depuis 2 diverge) ; ne pas confondre avec f(x) = 0
- **Schéma d'arrêt** : on répète jusqu'à ce que deux termes consécutifs diffèrent de moins de Epsilon ; en Pascal `1E-4` vaut 10⁻⁴ et `10E-4` vaut 10⁻³ ; l'écart entre deux termes ne mesure pas l'erreur sur la limite
- **π par Euler** : S2 ← 1, i ← 2, on ajoute 1/i², et π ≈ √(6 × S2) (S2 tend vers π²/6) ; avec 1E-4, 97 passes donnent 3,1319
- **π par Wallis** : π/2 = 2/1 × 2/3 × 4/3 × 4/5 × 6/5 × 6/7 × … est un produit ; Num ou Den augmente de 2 selon la parité de i, on affiche 2 × P2 ; environ 31 000 passes pour 1E-4
- **Séries alternées** : π/4 = 1 − 1/3 + 1/5 − 1/7 + … avec un `Signe := -Signe` à chaque passe, π ≈ 4 × S ; le sinus x − x³/3! + x⁵/5! − … alterne aussi ; sans `Abs`, le test s'arrête au premier terme négatif
- **e par les factorielles** : S2 ← 1 (le terme 1/0!), i ← 0, on ajoute 1/Fact (i) ; l'écart S2 − S1 est le dernier terme ; 8 passes pour 1E-4 ; Fact déborde d'un `LongInt` dès 13!
- **Rectangles** : h = (b − a)/n, Somme × h ; `Meth_Rec` code le point milieu (x ← a + h/2, puis x ← x + h), et non le point gauche ; pour f décroissante, le point gauche surestime et le point droit sous-estime
- **Trapèzes** : aire h × (f(aᵢ) + f(aᵢ₊₁))/2 par intervalle, avec h = (b − a)/n (et non (a + b)/n) ; c'est la moyenne du point gauche et du point droit, et l'estimation s'améliore quand n grandit
