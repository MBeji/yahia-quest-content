# 📜 Résumé : Le condensateur et le dipôle RC

- **Condensateur** : deux armatures conductrices séparées par un isolant, le diélectrique. Il garde +q sur une armature et −q sur l'autre ; il se charge sous tension continue et se décharge sur un récepteur. Aucune charge ne franchit le diélectrique, et un condensateur neutre n'a rien à restituer.
- **Intensité algébrique** : on fixe un sens positif, i > 0 si le courant le suit, i < 0 sinon. La charge q est celle de l'armature vers laquelle ce sens pointe, et **i = dq/dt** ; en convention récepteur, les flèches u_C et i sont de sens opposés.
- **Capacité** : **q = C·u_C**, avec C en farads (mF = 10⁻³ F, µF = 10⁻⁶ F, nF = 10⁻⁹ F, pF = 10⁻¹² F). Avec un courant constant I, u_C = (I/C)·t : la pente k du tracé donne C = I/k.
- **Condensateur plan** : C = ε·S/e = ε_r·ε₀·S/e, S en m², e en m, ε₀ ≈ 8,8·10⁻¹² F·m⁻¹. Au-delà de la tension de claquage une étincelle perce le diélectrique ; la tension de service, nominale, reste bien en dessous.
- **Énergie** : E_C = ½·C·u² = q²/(2C) = ½·q·u, en joules. Elle est proportionnelle à C et à u² (doubler u la multiplie par 4), et elle est rendue au circuit lors de la décharge.
- **Charge d'un dipôle RC** : u_C + RC·du_C/dt = E, d'où u_C = E(1 − e^(−t/τ)), q = Q₀(1 − e^(−t/τ)) avec Q₀ = CE, et i = I₀·e^(−t/τ) avec I₀ = E/R. Au départ u_C = 0 et i = I₀ ; à la fin u_C = E et i = 0.
- **Décharge** : u_C + RC·du_C/dt = 0, d'où u_C = E·e^(−t/τ), q = Q₀·e^(−t/τ) et i = −I₀·e^(−t/τ), négatif. L'énergie ½CE² est entièrement dissipée par effet Joule dans R.
- **Constante de temps** : τ = RC, en secondes. À t = τ, u_C vaut 0,63 E en charge et 0,37 E en décharge ; la tangente à l'origine rejoint l'asymptote (ou l'axe des temps) en t = τ. À 1 % près la charge dure 4,6 τ ≃ 5 τ, à 1 ‰ près 6,9 τ ≃ 7 τ.
