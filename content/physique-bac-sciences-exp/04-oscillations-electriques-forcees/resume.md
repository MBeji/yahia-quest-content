# 📜 Résumé : Les oscillations électriques forcées

- **Régime forcé et oscilloscope** : le GBF (excitateur) impose sa fréquence N au circuit RLC série (résonateur) ; en régime permanent i et q oscillent à N, non à N₀. Z = U_m / I_m (Ω), Q_m = I_m / (2πN). Résistor côté masse : u_R0 = R₀ i image de i ; condensateur côté masse : u_C = q/C image de q ; l'amplitude se lit de l'axe à la crête.
- **Déphasage** : Δφ = φ₂ − φ₁ et |Δφ| = 2π Δt / T ; Δt = 0 concordance, T/2 opposition (±π), T/4 quadrature (±π/2) ; la grandeur dont le maximum arrive la première est en avance ; φ_i = φ_q + π/2 (i en quadrature avance sur q).
- **Équation différentielle** : u = R i + L di/dt + q/C avec R = R₀ + r, soit L q″ + R q′ + q/C = u(t), second membre non nul ; seule la solution de régime permanent sinusoïdale est utilisée.
- **Construction de Fresnel** : les vecteurs R I_m, Lω I_m (avance π/2) et I_m/(Cω) (retard π/2) se composent en U_m ; Z = √(R² + (Lω − 1/(Cω))²), tan φ_i = (1/(Cω) − Lω) / R, cos φ_i = R/Z ; inductif si N > N₀ (i en retard), capacitif si N < N₀ (i en avance).
- **Résonance d'intensité** : N = N₀ = 1/(2π√(LC)), Z = R minimale, I_m0 = U_m / R maximale, i en phase avec u ; N₀ ne dépend pas de R ; R petite donne une résonance aiguë, R grande une résonance floue.
- **Résonance de charge** : Q_m maximale à N_r = √(N₀² − R²/(8π²L²)) < N₀, seulement si R² < 2L/C ; sinon Q_m décroît ; q toujours en retard sur u (−π < φ_q < 0).
- **Surtension** : à la résonance d'intensité, Q = U_Cm / U_m = Lω₀/R = (1/R)√(L/C) ; surtension si Q > 1, d'autant plus forte que R est faible ; risques de claquage et d'étincelles ; la tension du condensateur et la tension inductive Lω·I de la bobine, opposées, peuvent dépasser celle du GBF.
- **Puissance** : P = UI cos φ = R I² (W) avec U et I efficaces ; UI est la puissance apparente (V·A), cos φ = R/Z le facteur de puissance ; résonance de puissance à N₀ (P₀ = U²/R) ; pertes en ligne R_l P² / (U² cos² φ), réduites par un cos φ élevé (> 0,8).
