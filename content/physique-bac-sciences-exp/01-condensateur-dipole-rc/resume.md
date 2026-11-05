# 📜 Résumé : Le condensateur et le dipôle RC

- **Condensateur** : deux armatures conductrices séparées par un isolant (le diélectrique). Il se charge sous une tension continue (+q sur une armature, −q sur l'autre) et se décharge quand on le ferme sur un récepteur ; aucune charge ne traverse le diélectrique, et un condensateur neutre ne se décharge pas.
- **Intensité algébrique** : on choisit un sens positif ; i > 0 si le courant va dans ce sens, i < 0 sinon. La charge q du condensateur est celle de l'armature vers laquelle ce sens est orienté, et **i = dq/dt** : i > 0 en charge, i < 0 en décharge.
- **Capacité** : **q = C·u_C**, C en farads (1 mF = 10⁻³ F, 1 µF = 10⁻⁶ F, 1 nF = 10⁻⁹ F, 1 pF = 10⁻¹² F). À courant constant I, u_C = (I/C)·t : la pente k de la droite donne C = I/k.
- **Condensateur plan** : C = ε·S/e = ε_r·ε₀·S/e, avec ε₀ ≈ 8,85·10⁻¹² F·m⁻¹ ; S et e en m² et en m. La tension de service est nettement inférieure à la tension de claquage (étincelle dans le diélectrique).
- **Énergie** : E_C = ½·C·u² = q²/(2C) = ½·q·u, en joules ; doubler u (ou q) la multiplie par 4, doubler C la double ; elle est restituée à la décharge.
- **Charge d'un dipôle RC** : u_C + RC·du_C/dt = E ; u_C = E(1 − e^(−t/τ)), q = Q₀(1 − e^(−t/τ)) avec Q₀ = CE, i = I₀·e^(−t/τ) avec I₀ = E/R. À t = 0, u_C = 0 mais i = I₀ (pas 0) ; à la fin, u_C = E et i = 0.
- **Décharge** : u_C + RC·du_C/dt = 0 ; u_C = E·e^(−t/τ), q = Q₀·e^(−t/τ), i = −I₀·e^(−t/τ) : le courant est négatif ; toute l'énergie ½CE² est dissipée par effet Joule dans R.
- **Constante de temps** : τ = RC, en secondes. En charge, u_C = 0,63 E à t = τ ; en décharge, u_C = 0,37 E à t = τ ; la tangente à l'origine coupe l'asymptote (ou l'axe des temps) en t = τ ; la charge est terminée à 1 % près en 4,6 τ ≃ 5 τ, à 1 ‰ près en 6,9 τ ≃ 7 τ.
