# 📜 Résumé : Suites réelles

- **Sens de variation** : (uₙ) est croissante si uₙ₊₁ ≥ uₙ pour tout n, décroissante si uₙ₊₁ ≤ uₙ ; on étudie le signe de uₙ₊₁ − uₙ, ou le rapport uₙ₊₁/uₙ à 1 pour des termes strictement positifs, ou le sens de f si uₙ = f(n), ou une récurrence ; jamais sur les premiers termes seulement.
- **Majorée, minorée, bornée** : un réel M (majorant) ou m (minorant) limite tous les termes ; bornée équivaut à |uₙ| ≤ M ; croissante n'entraîne pas majorée, et un majorant n'est pas forcément atteint.
- **Limite** : lim uₙ = ℓ réel signifie que (uₙ) converge ; si uₙ = f(n) et f(x) → ℓ en +∞, alors uₙ → ℓ ; qⁿ → +∞ si q > 1, → 0 si −1 < q < 1, sans limite si q ≤ −1 ; convergente entraîne bornée, mais bornée n'entraîne pas convergente.
- **Opérations** : somme, produit et quotient comme pour les fonctions ; formes indéterminées +∞ − ∞, 0 × ∞, ∞/∞, 0/0 levées par le terme dominant, la quantité conjuguée ou un changement de variable ; si uₙ → ℓ et f est continue en ℓ, alors f(uₙ) → f(ℓ).
- **Suites monotones bornées (admis)** : croissante et majorée converge ; décroissante et minorée converge ; le théorème donne l'existence de la limite, pas sa valeur, et un majorant n'est pas la limite.
- **Suite récurrente uₙ₊₁ = f(uₙ)** : on prouve l'encadrement par récurrence puis la monotonie ; si (uₙ) converge vers ℓ et f est continue en ℓ, alors f(ℓ) = ℓ ; l'encadrement m ≤ uₙ ≤ M donne m ≤ ℓ ≤ M et désigne la bonne solution.
- **Suite auxiliaire** : pour uₙ₊₁ = a uₙ + b, avec ℓ = b/(1 − a), vₙ = uₙ − ℓ est géométrique de raison a ; uₙ = ℓ + v₀aⁿ ; somme géométrique v₀(1 − q^{n+1})/(1 − q), qui compte n + 1 termes ; la limite de uₙ n'est pas celle de vₙ.
- **Comparaison et gendarmes** : uₙ ≤ vₙ et uₙ → +∞ donnent vₙ → +∞ ; vₙ ≤ uₙ ≤ wₙ avec vₙ et wₙ de même limite ℓ donnent uₙ → ℓ ; |uₙ| ≤ vₙ et vₙ → 0 donnent uₙ → 0.
