# 📜 Résumé : Variables aléatoires réelles

- **Variable aléatoire et loi** : X associe un nombre à chaque issue ; sa loi est le tableau des pᵢ = p(X = xᵢ), avec p₁ + … + pₙ = 1 ; on compte les issues de chaque événement (X = xᵢ), pas les valeurs, qui ne sont pas équiprobables.
- **Fonction de répartition** : F(x) = p(X ≤ x) est un escalier croissant, continu à droite, avec p(X > x) = 1 − F(x) et p(a < X ≤ b) = F(b) − F(a) ; la hauteur d'une marche est p(X = xᵢ), et F(xᵢ) n'est pas p(X = xᵢ).
- **Espérance** : E(X) = Σ pᵢxᵢ est la moyenne pondérée par les probabilités, et non la moyenne simple des valeurs ; un jeu est favorable si E(X) > 0, équitable si E(X) = 0, défavorable si E(X) < 0.
- **Variance et écart-type** : V(X) = E(X²) − (E(X))² = Σ pᵢ(xᵢ − E(X))² et σ(X) = √V(X) ; on retranche le carré de l'espérance, et plus σ est grand, plus les valeurs s'écartent de E(X).
- **Loi binomiale** : le nombre de succès de n épreuves de Bernoulli indépendantes suit ℬ(n ; p), avec p(X = k) = Cₙᵏ pᵏ (1 − p)ⁿ⁻ᵏ, E(X) = np et V(X) = np(1 − p) ; des tirages sans remise ne donnent pas une loi binomiale, et « au moins un succès » passe par 1 − (1 − p)ⁿ.
- **Variable continue et densité** : X(Ω) est un intervalle et p(X = a) = 0 ; F(x) = p(X ≤ x) est continue et croissante, la densité est f = F′ ≥ 0, et p(s ≤ X ≤ t) = F(t) − F(s) = ∫ₛᵗ f(x) dx, une aire et non la valeur f(x).
- **Loi uniforme** : sur [a ; b], la densité vaut 1/(b − a) et p(s ≤ X ≤ t) = (t − s)/(b − a) ; E(X) = (a + b)/2 est le milieu, et V(X) = (b − a)²/12.
- **Loi exponentielle** : de paramètre λ, f(t) = λe^(−λt) sur [0 ; +∞[, p(X > t) = e^(−λt), p(a ≤ X ≤ b) = e^(−λa) − e^(−λb), E(X) = 1/λ et V(X) = 1/λ² ; sans mémoire : p(X > s + t sachant X > s) = p(X > t).
