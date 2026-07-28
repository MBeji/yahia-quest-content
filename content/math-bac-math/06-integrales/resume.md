# 📜 Résumé : Intégrales

- **Aire sous la courbe** : f continue et positive sur [a, b], F primitive de f ⟹ l'aire (en u.a) entre C_f, l'axe des abscisses et x = a, x = b vaut F(b) − F(a), noté ∫ₐᵇ f(x)dx ; le résultat ne dépend pas de la primitive choisie.
- **Intégrale d'une fonction continue** : ∫ₐᵇ f(x)dx = [F(x)]ₐᵇ = F(b) − F(a), sans hypothèse de signe ni d'ordre ; la variable est **muette** (∫ₐᵇ f(x)dx = ∫ₐᵇ f(t)dt).
- **Propriétés algébriques** : ∫ₐᵃ f = 0 ; ∫ₐᵇ f = −∫_bᵃ f ; **Chasles** ∫ₐᶜ f + ∫_cᵇ f = ∫ₐᵇ f ; **linéarité** ∫ₐᵇ (αf + βg) = α∫ₐᵇ f + β∫ₐᵇ g (réflexe : regrouper deux intégrales pour simplifier).
- **Intégrales et inégalités** : f ≥ 0 ⟹ ∫ₐᵇ f ≥ 0 (stricte si f ne s'annule qu'en un nombre fini de points) ; h ≤ f ≤ g ⟹ ∫h ≤ ∫f ≤ ∫g ; |∫ₐᵇ f| ≤ ∫ₐᵇ |f|. La réciproque est fausse : ∫f ≥ 0 n'implique pas f ≥ 0.
- **Aires** : aire sous C_f = ∫ₐᵇ |f(x)|dx (découper aux changements de signe) ; aire entre deux courbes = ∫ₐᵇ |f(x) − g(x)|dx (étudier le signe de f − g avant tout calcul).
- **Calculs** : par une primitive (reconnaître u′uⁿ, u′/(2√u), u′/u²…) ; **intégration par parties** ∫ₐᵇ f g′ = [fg]ₐᵇ − ∫ₐᵇ f′g (f = le facteur qui se simplifie en dérivant) ; **méthode des rectangles** pour encadrer quand aucune primitive n'est connue.
- **Valeur moyenne** : f̄ = 1/(b − a) · ∫ₐᵇ f(x)dx ; le rectangle de côtés (b − a) et f̄ a l'aire de la partie sous la courbe ; **inégalité de la moyenne** m ≤ f ≤ M ⟹ m ≤ f̄ ≤ M ; il existe c ∈ [a, b] avec f̄ = f(c).
- **Volume de révolution** : f continue et positive sur [a, b], rotation autour de (Ox) ⟹ V = π ∫ₐᵇ f²(x)dx (section = disque de rayon f(x)) ; c'est **f²**, jamais f. Exemple : la sphère, V = 4πR³/3.
- **Fonctions définies par une intégrale** : F(x) = ∫ₐˣ f(t)dt est la primitive de f qui s'annule en a, donc F′ = f ; plus généralement, si F(x) = ∫ₐ^{u(x)} f(t)dt alors F′(x) = f(u(x))·u′(x).
- **Parité et périodicité** : sur un intervalle centré en 0, f impaire ⟹ ∫_{−a}ᵃ f = 0, f paire ⟹ ∫_{−a}ᵃ f = 2∫₀ᵃ f ; f de période T ⟹ ∫ₐ^{a+T} f = ∫₀ᵀ f (attention : |sin| et |cos| sont de période π).
- **Suites d'intégrales** : encadrer l'intégrande pour la convergence (ex. 0 ≤ ∫₀¹ x^{n+1}/(1 + x²)dx ≤ 1/(n + 2) → 0) ; une IPP fournit la relation entre Iₙ et Iₙ₊₂ (Wallis : Iₙ₊₂ = ((n + 1)/(n + 2))Iₙ) ; calculer les premiers termes pour amorcer.
