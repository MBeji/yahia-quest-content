# 📜 Résumé : Les oscillations électriques forcées

- **Régime forcé** : le GBF (excitateur) impose sa fréquence N au circuit RLC série (résonateur) ; en régime permanent i oscille à N, non à N₀. Impédance Z = U_m / I_m, en ohm. Avec la masse en M, u_R₀ = R₀·i est l'image de i ; les amplitudes se lisent de l'axe à la crête, en tenant compte des sensibilités.
- **Déphasage** : Δφ = φ₂ − φ₁ et |Δφ| = 2π·Δt / T ; Δt = 0 concordance, T/4 quadrature (π/2), T/2 opposition (π) ; la grandeur dont le maximum arrive la première est en avance.
- **Mise en équation** : u = R·i + L·di/dt + (1/C)·∫ i·dt avec R = R₀ + r ; le second membre u(t) n'est pas nul et entretient les oscillations ; seule la solution permanente i = I_m·sin(ωt + φ) est utilisée.
- **Construction de Fresnel** : R·I_m (angle φ), Lω·I_m (φ + π/2) et I_m/(Cω) (φ − π/2) se composent en U_m ; Z = √(R² + (Lω − 1/(Cω))²), tg φ = (1/(Cω) − Lω) / R, cos φ = R/Z ; inductif si N > N₀ (i en retard), capacitif si N < N₀ (i en avance).
- **Résonance d'intensité** : N = N₀ = 1/(2π√(LC)), Z = R minimale, I_m0 = U_m / R maximale, i en phase avec u ; N₀ ne dépend pas de R, qui règle la finesse du pic (aiguë si R petite, floue si R grande).
- **Surtension** : à la résonance, Q = U_Cm / U_m = Lω₀ / R = (1/R)·√(L/C) avec R = R₀ + r ; surtension si Q > 1, d'autant plus forte que la résonance est aiguë ; risques de claquage et d'étincelles ; on la limite en augmentant R.
- **Puissance moyenne** : p = UI·cos φ − UI·cos(2ωt + φ), de période T/2 ; P = UI·cos φ = R·I² en watt, avec U et I efficaces ; UI est la puissance apparente (V·A) ; résonance de puissance à N₀, où P₀ = U²/R.
- **Facteur de puissance** : cos φ = R/Z ; pour P et U imposées, I = P/(U·cos φ) et les pertes en ligne valent R_l·P² / (U²·cos²φ) : elles diminuent quand cos φ augmente, d'où l'exigence cos φ > 0,8.
