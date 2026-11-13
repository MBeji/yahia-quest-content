# 📜 Résumé : Conversion de signaux

- **Signaux analogique et logique** : analogique = valeur continue, sensible au bruit, difficile à mémoriser ; logique = deux niveaux, V_cc (état 1) et 0 V (état 0) ; un signal numérique, formé de signaux logiques, se mémorise et se traite sans altération ; on revient à l'analogique en bout de chaîne.
- **Mot binaire** : [N] = [a_(n−1) … a₁ a₀], N = Σ 2^j·a_j (a₀ = poids faible) ; N_max = 2ⁿ − 1 et 2ⁿ combinaisons.
- **C.N.A. et C.A.N.** : C.N.A. : mot [N] vers u_S = k·N (k en V) ou i_S = k'·N ; C.A.N. : u_E vers mot, N = K·u_E (K en V⁻¹) ; le C.A.N. suit le capteur, le C.N.A. précède l'actionneur.
- **C.N.A. à résistances pondérées** : R_j = 2^(n−j−1)·R ; I_j = a_j·U_ref/R_j ; u_S = −R'·i = k·N avec k = −R'U_ref/(2^(n−1)·R) ; l'A.O. impose 0 V au nœud et convertit le courant en tension ; sommateur inverseur : u_S = −R'·Σ(V_k/R_k).
- **Pleine échelle, quantum, résolution** : P.E. = |k|·(2ⁿ − 1) ; q = P.E./(2ⁿ − 1) = |k| ; r = 1/2ⁿ ; on choisit U_ref pour que P.E. reste inférieure à la saturation de l'A.O.
- **Caractéristique de transfert** : points u_S = f(N) alignés sur une droite passant par l'origine, de pente k ; sortie positive si U_ref < 0 (ou un A.O. inverseur de plus) ; aucune valeur intermédiaire.
- **Réseau R-2R** : deux valeurs de résistances, R et 2R ; u_S = −(R'U_ref/16R)·N à 4 bits (démonstration hors programme) ; le réseau pondéré est simple mais exige des résistances à rapports élevés.
- **C.A.N.** : quantification (nombre fini de niveaux) puis codage (mot par niveau) ; principe : comparer u_E à la sortie d'un C.N.A. rebouclé ; 2ⁿ mots possibles.
