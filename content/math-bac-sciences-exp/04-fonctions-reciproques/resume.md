# 📜 Résumé : Fonctions réciproques

- **Bijection** : f réalise une bijection de I sur f(I) si, pour tout y de f(I), l'équation f(x) = y a une **unique** solution dans I ; **f strictement monotone sur I ⟹ bijection** (la continuité seule ne suffit pas). L'image se lit avec les valeurs et les limites aux bornes, bornes échangées si f décroît.
- **Fonction réciproque** : f⁻¹ associe à y de f(I) l'unique antécédent dans I ; **f(x) = y ⟺ f⁻¹(y) = x** ; f⁻¹∘f = id sur I et f∘f⁻¹ = id sur f(I) ; f⁻¹ ≠ 1/f. Pour expliciter : résoudre y = f(x) en x et garder la solution qui est dans I (f(x) = 1/x est sa propre réciproque sur ]0, +∞[).
- **Miroir** : en repère orthonormé, C_f et C_{f⁻¹} sont symétriques par rapport à **Δ : y = x** ; (a, b) ∈ C_f ⟺ (b, a) ∈ C_{f⁻¹} ; une asymptote horizontale de C_f devient verticale pour C_{f⁻¹}, et réciproquement ; f(a) = a ⟹ (a, a) est sur les deux courbes.
- **Continuité et sens** : f continue et strictement monotone sur I ⟹ f⁻¹ continue et strictement monotone sur f(I), **dans le même sens que f**.
- **Dérivée** : si f′(a) ≠ 0 et b = f(a), alors **(f⁻¹)′(b) = 1/f′(a)** ; sur f(I), (f⁻¹)′(y) = 1/f′(f⁻¹(y)). Si f′(a) = 0 : tangente horizontale de C_f ⟹ tangente verticale de C_{f⁻¹}, donc f⁻¹ non dérivable en b ; une tangente verticale de C_f donne une tangente horizontale de C_{f⁻¹}.
- **Racine nᵉ** (n ≥ 2) : réciproque de x ↦ xⁿ sur ℝ₊, strictement croissante de ℝ₊ sur ℝ₊, notée ⁿ√x ; **y = xⁿ ⟺ x = ⁿ√y** pour x, y positifs ; ⁿ√ ne s'applique qu'à des réels positifs.
- **Radicaux** (a, b ≥ 0) : ⁿ√(aⁿ) = a ; (ⁿ√a)ⁿ = a ; ⁿ√(ab) = ⁿ√a·ⁿ√b ; ⁿ√(a/b) = ⁿ√a/ⁿ√b ; **ⁿ√a = ⁿᵖ√(aᵖ)** (même indice pour comparer) ; (ⁿ√a)ᵖ = ⁿ√(aᵖ) ; ⁿ√(ᵖ√a) = ⁿᵖ√a ; jamais ⁿ√(a + b) = ⁿ√a + ⁿ√b.
- **Dérivée de ⁿ√** : continue sur [0, +∞[, dérivable sur ]0, +∞[ avec **(ⁿ√x)′ = 1/(n·ⁿ√(xⁿ⁻¹))** ; non dérivable à droite en 0 (demi-tangente verticale) ; pour x > 1, ⁶√x < ⁴√x < ∛x, et l'inverse pour 0 < x < 1.
