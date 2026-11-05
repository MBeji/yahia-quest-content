# 📜 Résumé : Variables aléatoires

- **Variable aléatoire et loi** : X : E → ℝ associe un nombre à chaque issue ; sa loi est le tableau des pᵢ = p(X = xᵢ), avec p₁ + … + pₙ = 1 car les événements (X = xᵢ) forment une partition de E ; on compte les issues de chaque événement, pas les valeurs, qui ne sont pas équiprobables.
- **Espérance** : E(X) = Σ xᵢpᵢ est la moyenne pondérée par les probabilités, et non la moyenne simple des valeurs ; E(αX) = αE(X) et E(X + Y) = E(X) + E(Y).
- **Variance et écart-type** : V(X) = E(X²) − (E(X))² et σ(X) = √V(X) ; on retranche le carré de l'espérance, et plus σ est grand, plus les valeurs s'écartent de E(X).
- **Fonction de répartition** : F(x) = p(X ≤ x) cumule les probabilités ; la hauteur d'un saut de F est p(X = xᵢ), F(xᵢ) n'est pas p(X = xᵢ), p(X > x) = 1 − F(x), et p(X < a) ne compte pas la valeur a.
- **Loi binomiale** : le nombre de succès de n épreuves identiques et indépendantes suit ℬ(n ; p), avec p(X = k) = Cₙᵏ pᵏ (1 − p)ⁿ⁻ᵏ, E(X) = np et V(X) = np(1 − p) ; des tirages sans remise ne donnent pas une loi binomiale, et « au moins un succès » passe par 1 − (1 − p)ⁿ.
- **Loi uniforme** : sur [a ; b], la densité vaut 1/(b − a), p(c ≤ X ≤ d) = (d − c)/(b − a) et p(X = c) = 0 ; la valeur de la densité est une hauteur, non une probabilité, et F(x) = (x − a)/(b − a) sur [a ; b].
- **Loi exponentielle** : de paramètre λ, la densité est λe^(−λt) sur [0 ; +∞[, p(X ≥ c) = e^(−λc), p(c ≤ X ≤ d) = e^(−λc) − e^(−λd) et F(x) = 1 − e^(−λx) pour x ≥ 0 ; on retrouve λ par λ = −ln q/t₀ quand p(X ≥ t₀) = q.
