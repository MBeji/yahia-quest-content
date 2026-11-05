# 📜 Résumé : Dérivabilité

- **Nombre dérivé et tangente** : f′(a) = lim x→a (f(x) − f(a))/(x − a) ; tangente y = f′(a)(x − a) + f(a) ; approximation affine f(a + h) ≈ f(a) + f′(a)h ; si f′(a) = 0, tangente horizontale y = f(a).
- **Gauche, droite, intervalle** : f dérivable en a ⟺ f′_g(a) = f′_d(a) ; sinon point anguleux (deux demi-tangentes) ; un taux qui tend vers ±∞ donne une demi-tangente verticale (√x en 0) ; la continuité en a ne suffit pas.
- **Calcul des dérivées** : (xⁿ)′ = nxⁿ⁻¹, (1/xⁿ)′ = −n/xⁿ⁺¹, (sin(ax + b))′ = a cos(ax + b), (cos(ax + b))′ = −a sin(ax + b), (tan(ax + b))′ = a(1 + tan²(ax + b)) ; (fg)′ = f′g + g′f ; (f/g)′ = (f′g − g′f)/g² ; (g∘f)′ = f′ × g′∘f, d'où (uⁿ)′ = nu′uⁿ⁻¹ et (√u)′ = u′/(2√u) pour u > 0.
- **Théorème de Rolle** : f continue sur [a ; b], dérivable sur ]a ; b[, f(a) = f(b) ⟹ il existe c de ]a ; b[ avec f′(c) = 0 ; sans dérivabilité (|x| sur [−1 ; 1]) la conclusion tombe.
- **Accroissements finis** : f continue sur [a ; b], dérivable sur ]a ; b[ ⟹ f(b) − f(a) = f′(c)(b − a) pour un c de ]a ; b[ ; si m ≤ f′ ≤ M, alors m(b − a) ≤ f(b) − f(a) ≤ M(b − a) ; si |f′| ≤ M, alors |f(b) − f(a)| ≤ M|b − a|.
- **Sens de variation** : f′ > 0 ⟹ f strictement croissante, f′ < 0 ⟹ strictement décroissante ; f′ ≥ 0 ne s'annulant sur aucun intervalle ouvert suffit encore ; continue sur [a ; b] et monotone sur ]a ; b[ ⟹ monotone sur [a ; b].
- **Extrema locaux** : f dérivable avec un extremum local en a ⟹ f′(a) = 0 (condition nécessaire) ; f′ qui s'annule en a en changeant de signe ⟹ extremum local en a ; f′(a) = 0 sans changement de signe (x³ en 0) ne donne aucun extremum.
- **Dérivées successives et inflexion** : f″ = (f′)′, f⁽ⁿ⁾ = (f⁽ⁿ⁻¹⁾)′ ; si f″ s'annule en a en changeant de signe, A(a ; f(a)) est un point d'inflexion : la courbe traverse sa tangente ; f″(a) = 0 seul ne suffit pas (x⁴ en 0).
