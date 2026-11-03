# 📜 Résumé : le touret à meuler et les sollicitations composées

- **Modèle de poutre** — l'ensemble {arbre + poulie + meule} devient une poutre aux points O (meule), A (articulation), G (poids, milieu d'OB), C (rouleaux), B (poulie) ; OA = 100, AC = 240, CB = 90 mm, donc OB = 430 mm et G à 215 mm de O. Liaisons parfaites ; les bras se mesurent depuis le point où l'on écrit les moments.
- **Torsion** — Mt = FT × rm = 110 × 75 = 8 250 N·mm = 8,25 N·m ; équilibre de rotation FT × rm = (T − t) × rp, donc T − t = 375 N ; avec T ≈ 4 t : t = 125 N, T = 500 N, T + t = 625 N. Les brins **s'additionnent en force** (flexion) et **se retranchent en rotation** (torsion). Mt est **constant de O à B**.
- **Réactions** — forces suivant y : RA + RC = 545 N (P compté −30 N, vers le bas) ; moments **en A** : RC ≈ 919,6 N ; RA ≈ −374,6 N, donc dirigée vers le bas. Contrôle par les moments en C.
- **Moment fléchissant** — Mf(x) = somme des moments des forces à gauche de la coupure, par tronçons : 0–100, 100–215, 215–340, 340–430 mm. Valeurs : 0 en O, +11 en A, −19,4 en G, −56,25 en C, 0 en B (N·m). Mf est une droite dans chaque tronçon et vaut 0 aux extrémités libres.
- **Diagrammes** — Mt est un plateau, Mf une ligne brisée ; on lit la **valeur absolue**. La section la plus sollicitée est **C**, et non B, où la plus grande force a un bras nul.
- **Sollicitation composée** — plusieurs sollicitations simples à la fois ; l'arbre subit de la **flexion-torsion**, sans traction ni compression, car aucune action n'est dirigée suivant l'axe.
- **Moment idéal** — Mfi = (1 − 1/(2λ)) × Mf + (1/(2λ)) × √(Mf² + Mt²) ; avec λ = 0,5, Mfi = √(Mf² + Mt²) ≈ 56,85 N·m en C. On n'additionne pas Mf et Mt (64,5 serait trop grand).
- **Diamètre minimal** — σ = Mfi / (π d³ / 32) ≤ Rpe = Re / s = 275 / 2 = 137,5 MPa ; d³ ≥ 32 × Mfi / (π × Rpe), en N·mm et MPa : d ≥ 16,15 mm. Le diamètre du dessin doit être **supérieur ou égal** ; doubler d divise σ par 8.
- **La méthode, en sept marches** — modéliser, équilibrer la rotation, trouver les réactions, calculer Mf, tracer et lire, composer en Mfi, dimensionner.
