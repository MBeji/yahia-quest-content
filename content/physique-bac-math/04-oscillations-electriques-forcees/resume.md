# 📜 Résumé : Les oscillations électriques forcées

- **Régime forcé et oscilloscope** : le GBF (excitateur) impose sa fréquence N au circuit RLC série (résonateur) ; en régime permanent i oscille à N, non à N₀. Z = U_m / I_m, en Ω. Résistor côté masse : u_R0 = R₀ i est l'image de i ; l'amplitude se lit de l'axe à la crête.
- **Déphasage** : Δφ = φ₂ − φ₁ et |Δφ| = 2π Δt / T ; Δt = 0 concordance, T/2 opposition (±π), T/4 quadrature (±π/2) ; la grandeur dont le maximum arrive la première est en avance ; la phase initiale φ de i est son déphasage par rapport à u.
- **Équation différentielle** : u = R i + L di/dt + (1/C) ∫ i dt avec R = R₀ + r, second membre non nul ; seule la solution du régime permanent est utilisée, le régime transitoire est hors programme.
- **Construction de Fresnel** : les vecteurs R I_m, Lω I_m (avance π/2) et I_m/(Cω) (retard π/2) se composent en U_m ; Z = √(R² + (Lω − 1/(Cω))²), tan φ = (1/(Cω) − Lω) / R, cos φ = R/Z ; inductif si N > N₀ (i en retard, φ < 0), capacitif si N < N₀ (i en avance, φ > 0).
- **Résonance d'intensité** : N = N₀ = 1/(2π√(LC)), Z = R minimale, I_m0 = U_m / R maximale, φ = 0 (i en phase avec u) ; le circuit se comporte comme un résistor R.
- **Influence de la résistance** : N₀ ne dépend pas de R ; R petite donne une résonance aiguë (pic haut, phase qui chute vite), R grande une résonance floue ; radio : résonance aiguë, haute fidélité : résonance floue.
- **Surtension** : à la résonance d'intensité, Q = U_Cm / U_m = Lω₀/R = (1/R)√(L/C) ; surtension si Q > 1, d'autant plus forte que R est faible ; risques de claquage et d'étincelles ; la bobine peut aussi subir une surtension.
- **Puissance** : P = UI cos φ = R I² (W) avec U et I efficaces ; UI est la puissance apparente (V·A), cos φ = R/Z le facteur de puissance ; résonance de puissance à N₀ (P₀ = U²/R) ; pertes en ligne R_l P² / (U² cos² φ), réduites par un cos φ élevé (> 0,8).
