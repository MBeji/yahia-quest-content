# 📜 Résumé : le banc d'essais de flexion — mesurer la flèche, vérifier la résistance

- **Le support** — banc d'essais de flexion : éprouvette sur deux appuis A (articulé) et B (à rouleaux), comparateur à cadran au milieu, charges suspendues (support 2,5 N, masses 5 N et 10 N). Compétences CD 1.7 et CD 2.1.
- **Flexion, portée, flèche** — une poutre sur deux appuis, chargée perpendiculairement à sa ligne moyenne, est en **flexion plane simple**. **Portée L** = distance entre A et B (pas la longueur de la barre) ; **flèche f** = déplacement vertical lu au comparateur ; **déformée** = forme de la ligne moyenne.
- **Moment quadratique** — **IGz** en mm⁴, par rapport à l'axe neutre Gz. Rectangle : **IGz = b × h³ / 12**, avec h dans le sens de la charge ; cercle : **IGz = π × d⁴ / 64**. Une barre sur chant plie bien moins qu'à plat (20 × 6 mm : 4 000 contre 360 mm⁴).
- **f et la charge** — **f = k × F** : la flèche est proportionnelle à F, la droite passe par l'origine ; k en mm/N. On remet le comparateur à zéro support accroché.
- **f et la portée** — **f = k × L³** (f / L³ constant, f(L³) est une droite). Formule standard : **f = F × L³ / (48 × E × IGz)**, charge au milieu ; f est inversement proportionnelle à E et à IGz.
- **Réactions et moment** — **RA = F × b / L**, **RB = F × a / L**, **Mfmax = F × a × b / L** sous la charge, nul aux appuis. Poutre de la partie B : RA = 9 N, RB = 6 N, Mfmax = 1 800 N·mm. Mf se garde en N·mm.
- **Contrainte normale** — **σ = Mf × y / IGz**, **σmax = Mfmax / (IGz / v)**, avec v = d / 2 pour un cercle. Nulle sur l'axe neutre, maximale aux fibres extrêmes (compression dessus, traction dessous). Partie B : σmax ≈ 35,8 MPa.
- **Condition de résistance** — **Rpe = Re / s**, **σmax ≤ Rpe** (Re = 240 MPa, s = 3, Rpe = 80 MPa, rapport ≈ 0,45 : la poutre résiste). Elle ne dit rien de la flèche.
- **Valider** — mêmes données pour le calcul, la simulation (Winflex) et l'essai ; comparer Mfmax, σmax et fmax ; écart relatif ; le palpeur se pose en D, point le plus bas, entre C et le milieu quand la charge est décentrée.
- **La méthode, en sept marches** — lire l'essai → section et IGz → lois de la flèche → réactions → moment → contrainte → verdict et validation.
