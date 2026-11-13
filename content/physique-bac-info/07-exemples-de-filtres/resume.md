# 📜 Résumé : Exemples de filtres

- **Courbe de réponse** : T = U_Sm/U_Em et G = 20 log T ; la coupure est à G₀ − 3 dB (U_Smo/√2) et la bande passante regroupe les fréquences où G ≥ G₀ − 3 dB. Un filtre passif a T ≤ 1 et G ≤ 0 dB ; la coupure n'est pas une fréquence « arrêtée ».
- **Passe-bas RC (mesures)** : sortie aux bornes de C ; N_h = 1/(2πRC), inversement proportionnelle à R et à C ; bande [0 ; N_h] ; pente −20 dB par décade, soit −6 dB par octave ; décade = rapport 10, octave = rapport 2.
- **Passe-bas RC (théorie)** : u_S + RC·du_S/dt = u_E ; T = 1/√(1 + (N/N_h)²), G = −10 log(1 + (N/N_h)²), tg Δφ = −N/N_h avec −π/2 < Δφ < 0 ; Δφ = −π/4 à N_h ; T = Z_C/Z.
- **Passe-bas actif** : A.O. idéal, R₀ en entrée, R₁ ∥ C en retour ; T₀ = R₁/R₀, G₀ = 20 log(R₁/R₀), N_h = 1/(2πR₁C) indépendante de R₀ ; amplification possible si R₁ > R₀ ; 90° ≤ Δφ ≤ 180°, Δφ = 135° à N_h.
- **Passe-haut CR** : sortie aux bornes de R ; RC·du_S/dt + u_S = RC·du_E/dt ; N_b = 1/(2πRC), bande [N_b ; +∞[ ; T = 1/√(1 + (N_b/N)²), tg Δφ = N_b/N, Δφ = +π/4 à N_b, sortie en avance ; pente +20 dB par décade aux basses fréquences.
- **Passe-bande RLC (mesures)** : sortie aux bornes de R₀ ; U_Sm maximale à N₀ = 1/(2π√(LC)) ; bande [N_b ; N_h], (N_b + N_h)/2 ≈ N₀ ; Δφ change de signe : avance pour N < N₀, nul à N₀, retard pour N > N₀.
- **Passe-bande RLC (théorie)** : T = T₀/√(1 + Q²(x − 1/x)²) avec Q = Lω₀/R, x = N/N₀, T₀ = R₀/R ; ΔN = N₀/Q ; sélectif si Q ≫ 1, avec N_b ≈ N₀ − ΔN/2 et N_h ≈ N₀ + ΔN/2 ; Δφ = −45° à N_h et +45° à N_b ; équation du second ordre.
- **Reconnaître un filtre** : limites de Z_C = 1/Cω et Z_L = Lω pour le type ; ordre = plus haute dérivée de u_S (RC, CR, passe-bas actif : 1 ; RLC : 2) ; passif si T ≤ 1, actif si A.O. alimenté ; A.O. non inverseur : T₀ = 1 + R₁/R₂ (admis).
