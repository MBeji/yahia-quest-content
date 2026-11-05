# 📜 Résumé : Statistiques

- **Tableau à double entrée et distributions marginales** : nᵢⱼ est l'effectif de (X = xᵢ et Y = yⱼ) et les totaux des lignes et des colonnes sont les effectifs marginaux, de somme N ; X̄ = (1/N) Σ nᵢ. xᵢ et V(X) = (1/N) Σ nᵢ. xᵢ² − (X̄)², avec les centres des classes pour une série en classes.
- **Nuage de points et point moyen** : le nuage est l'ensemble des points Mᵢⱼ(xᵢ ; yⱼ) affectés de leurs effectifs, et son point moyen est G(X̄ ; Ȳ) ; G se calcule avec les moyennes et n'est pas forcément un point du nuage.
- **Méthode de Mayer** : on range les points par abscisses croissantes, on les partage en deux parties de même effectif (à un près si le nombre de points est impair), on calcule leurs points moyens G₁ et G₂, et la droite (G₁G₂) est la droite de Mayer ; elle passe par G.
- **Covariance** : Cov(X, Y) = (moyenne des produits xᵢyᵢ) − X̄ × Ȳ, et pour un tableau à double entrée (1/N) Σ nᵢⱼ xᵢyⱼ − X̄ × Ȳ ; son signe donne le sens de la liaison, et Cov² voisin de V(X) × V(Y) annonce une relation à peu près affine.
- **Coefficient de corrélation linéaire** : r = Cov(X, Y) / (σ(X) × σ(Y)) est un nombre sans unité de [−1 ; 1] ; 0,75 ≤ |r| justifie un ajustement affine, et r = 0 n'exclut pas une liaison non affine.
- **Droites de régression** : D₁ : y = ax + b avec a = Cov / V(X) et b = Ȳ − aX̄ prévoit Y ; D₂ : x = a'y + b' avec a' = Cov / V(Y) et b' = X̄ − a'Ȳ prévoit X ; toutes deux passent par G, et a × a' = r².
- **Ajustement non affine** : on pose Z = ln Y, Z = √Y ou x = 1/n, on vérifie r sur (X ; Z), on ajuste z = ax + b, puis on revient à Y par la fonction réciproque avant toute prévision.
