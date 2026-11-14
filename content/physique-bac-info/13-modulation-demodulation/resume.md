# 📜 Résumé : Modulation et démodulation des signaux

- **Porteuse, signal modulant et multiplieur** : la porteuse (N_p très élevée) est modulée en amplitude par u(t) = U_m cos 2πN t, auquel on ajoute U_0 (tension de décalage) ; u_S = k·u₁·u_p avec u₁ = u(t) + U_0 et k = 0,1 V⁻¹ ; N_p ≫ N ; la fréquence annoncée d'une station est celle de la porteuse.
- **Signal modulé et enveloppe** : u_S = k·U_pm·U_0·(1 + (U_m/U_0) cos 2πN t)·cos 2πN_p t, de fréquence N_p ; U_Smax = k·U_pm·(U_0 + U_m) et U_Smin = k·U_pm·(U_0 − U_m) ; l'enveloppe a la forme du signal modulant.
- **Taux de modulation** : m = (U_Smax − U_Smin)/(U_Smax + U_Smin) = U_m/U_0, sans unité ; m < 1 bonne modulation, m = 1 limite, m > 1 surmodulation (U_Smin négative) ; trapèze en mode XY : m = (L − l)/(L + l).
- **Spectre** : trois raies, N_p − N, N_p et N_p + N, de hauteurs mA/2, A et mA/2 avec A = k·U_pm·U_0 ; bande ΔN = 2N ; m = 2 × (latérale)/(centrale) ; aucune raie à N.
- **Détection d'enveloppe** : diode, puis C en parallèle avec R ; C se charge par la diode, se décharge dans R ; T_p ≪ τ = RC ≪ T, donc N_p ≫ N.
- **Lissage et élimination de la composante continue** : passe-bas R'C' avec T_p ≪ R'C' ≪ T (enlève les ondulations) ; passe-haut R''C'' avec R''C'' ≫ T (enlève U_0) ; chaîne : détecteur, passe-bas, passe-haut ; poste AM : antenne et circuit d'accord LC.
- **Modulation de fréquence** : amplitude constante, N_p(t) = N_0 + k·u(t) ; excursion N_p − N_0 = k·u(t), excursion crête k·U_m ; indice β = k·U_m/N ; oscillateur (L, C) à capacité commandée (varicap), quartz pour N_0 ; démodulation FM hors programme.
- **AM ou FM** : AM, amplitude variable, simple, sensible aux parasites, bande 2N ; FM, fréquence variable, peu sensible aux parasites, relais, montage plus complexe, large bande ; on les reconnaît sur l'expression (facteur d'amplitude variable ou phase variable) ; N = ω/2π ; usages : radio, télévision, modem, FSK, DTMF.
