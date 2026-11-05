# 📜 Résumé : Fonction réciproque

- **Restriction** : la restriction de f à I garde la formule de f sur une partie I du domaine ; on la choisit là où f est strictement monotone (on coupe aux points où le sens de variation change, ou pour supprimer une valeur absolue).
- **Image d'un intervalle** : f continue et strictement monotone sur I ⟹ f(I) est l'intervalle dont les extrémités sont les valeurs ou limites de f aux extrémités de I, rangées dans le sens de la monotonie ; crochet fermé ⟺ valeur atteinte ; sans monotonie, pas de lecture borne à borne.
- **Bijection et réciproque** : f strictement monotone sur I ⟹ bijection de I sur f(I) ; y = f(x) ⟺ x = f⁻¹(y) ; f⁻¹ est définie sur f(I), varie dans le même sens que f et est continue si f l'est ; pour l'expliciter, on calcule J = f(I) puis on résout f(x) = y en gardant la solution de I ; f⁻¹ n'est pas 1/f.
- **Symétrie** : dans un repère orthonormé, les courbes de f et de f⁻¹ sont symétriques par rapport à Δ : y = x ; M(a ; b) sur la courbe de f ⟺ M′(b ; a) sur celle de f⁻¹ ; sans repère orthonormé, pas de miroir.
- **Racine n-ième** : ⁿ√x est la réciproque de xⁿ sur [0 ; +∞[ : y = ⁿ√x ⟺ yⁿ = x ; (ⁿ√x)ⁿ = x ; lim ⁿ√x = +∞ et lim ⁿ√x / x = 0 en +∞ ; x^(1/n) = ⁿ√x et x^(p/q) = (x^p)^(1/q).
- **Dérivée en un point** : f dérivable en x₀ avec f′(x₀) ≠ 0 ⟹ (f⁻¹)′(y₀) = 1/f′(x₀) = 1/f′(f⁻¹(y₀)) ; on évalue f′ à l'antécédent x₀, jamais en y₀.
- **Dérivée sur un intervalle** : f′ ne s'annule pas sur I ⟹ f⁻¹ dérivable sur f(I) et (f⁻¹)′ = 1/(f′∘f⁻¹) ; si f′(x₀) = 0, f⁻¹ n'est pas dérivable en f(x₀) (tangente verticale) ; (ⁿ√x)′ = ⁿ√x/(nx) sur ]0 ; +∞[ ; pour la réciproque de tan, (h⁻¹)′(x) = 1/(1 + x²).
