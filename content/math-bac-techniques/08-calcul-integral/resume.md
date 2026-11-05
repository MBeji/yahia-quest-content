# 📜 Résumé : Calcul intégral

- **Intégrale** : pour f continue sur I et F une primitive de f, ∫ₐᵇ f(x)dx = [F(x)]ₐᵇ = F(b) − F(a), indépendant de la primitive ; on évalue aux deux bornes et on soustrait ; la variable est muette et ∫ₐᵇ k dt = k(b − a).
- **Bornes, Chasles, linéarité** : ∫ₐᵃ f = 0 ; ∫_bᵃ f = −∫ₐᵇ f ; ∫ₐᵇ f = ∫ₐᶜ f + ∫_cᵇ f ; linéarité pour les sommes et les multiples constants, jamais pour les produits ; on coupe une valeur absolue à son changement de signe.
- **Parité et périodicité** : sur [−a ; a], f paire donne 2∫₀ᵃ f et f impaire donne 0 (intervalle symétrique indispensable) ; pour T-périodique, ∫ₐ^{a+T} f = ∫₀ᵀ f.
- **Ordre** : pour a < b, f ≥ 0 donne ∫ f ≥ 0 ; f ≤ g donne ∫ f ≤ ∫ g ; |∫ f| ≤ ∫ |f| ; m ≤ f ≤ M donne m(b − a) ≤ ∫ f ≤ M(b − a).
- **Valeur moyenne** : μ = (1/(b − a))∫ₐᵇ f, atteinte au moins une fois en un c de [a ; b] ; ce n'est pas (f(a) + f(b))/2 en général.
- **Intégration par parties** : ∫ₐᵇ u′v = [uv]ₐᵇ − ∫ₐᵇ uv′ ; on dérive le facteur qui se simplifie, on primitive l'autre ; on peut recommencer, et ln x seul se traite avec u′ = 1.
- **Fonction définie par une intégrale** : x ↦ ∫ₐˣ f(t)dt est la primitive de f qui s'annule en a, de dérivée f(x) (et non f(x) − f(a)).
- **Aire et volume** : l'aire sous C_f vaut ∫ₐᵇ |f| u.a et entre deux courbes ∫ₐᵇ |f − g| u.a (1 u.a = ‖i⃗‖ × ‖j⃗‖) ; le volume de révolution autour de (Ox) vaut V = π∫ₐᵇ (f(x))²dx u.v, repère orthonormé.
