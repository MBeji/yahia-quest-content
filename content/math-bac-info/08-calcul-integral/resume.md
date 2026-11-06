# 📜 Résumé : Calcul intégral

- **Intégrale** : pour f continue entre a et b, ∫ₐᵇ f(x)dx = [F(x)]ₐᵇ = F(b) − F(a), pour toute primitive F ; la variable est muette. **Piège** : si f n'est pas continue entre les bornes (1/(x − 2) sur [0 ; 3]), l'intégrale n'existe pas.
- **Chasles et linéarité** : ∫ₛᵗ f = −∫ₜˢ f, ∫ₐᵏ f + ∫ₖᵇ f = ∫ₐᵇ f, ∫ₐᵇ (αf + βg) = α∫ₐᵇ f + β∫ₐᵇ g ; pour |f|, on coupe là où le signe change. **Piège** : l'intégrale d'un produit n'est pas le produit des intégrales.
- **Reconnaître la forme** : u′uⁿ, u′/u (ln), u′e^u, u′/√u ; on pose u, on calcule u′, on compense un facteur **constant**, on contrôle en dérivant ; sinon on réécrit (identification des coefficients). **Piège** : ∫₀¹ x e^(1 − x²)dx vaut (e − 1)/2, pas 1 − e.
- **Intégration par parties** : ∫ₐᵇ uv′ = [uv]ₐᵇ − ∫ₐᵇ u′v ; on dérive le facteur qui se simplifie, on primitive l'autre, on répète pour xⁿ ; elle donne des relations de récurrence (Jₙ₊₁ = e − (n + 1)Jₙ). **Piège** : le signe est « moins ».
- **Positivité et comparaison** : pour a ≤ b, f ≥ 0 donne ∫ₐᵇ f ≥ 0 et f ≤ g donne ∫f ≤ ∫g ; on encadre l'intégrande puis on intègre ; avec les bornes échangées, le sens se retourne. **Piège** : ∫ ≥ 0 n'entraîne pas f ≥ 0.
- **Valeur moyenne** : f̄ = (1/(b − a))∫ₐᵇ f ; m ≤ f ≤ M donne m ≤ f̄ ≤ M ; il existe c de [a ; b] tel que f(c) = f̄ (accroissements finis), pas forcément unique. **Piège** : f̄ n'est pas la demi-somme de f(a) et f(b).
- **Aires** : sous la courbe, A = ∫ₐᵇ |f| ; entre deux courbes, A = ∫ₐᵇ |g − f| ; on étudie le signe, on coupe à chaque changement ou croisement ; 1 u.a = (unité)² en cm². **Piège** : ∫ f peut être nulle alors que l'aire ne l'est pas.
- **Méthode des rectangles** : pour f décroissante, h = (b − a)/n, des rectangles par défaut et par excès encadrent l'aire, avec un écart h(f(a) − f(b)) ; le programme au point milieu renvoie somme × h, une valeur approchée (∫₀¹ dx/(1 + x²) = π/4). **Piège** : oublier de multiplier par h.
