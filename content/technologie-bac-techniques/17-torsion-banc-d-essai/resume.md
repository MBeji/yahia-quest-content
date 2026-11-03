# 📜 Résumé : le banc d'essai de torsion

- **Le thème** — un **solide déformable** change de forme sous les actions qu'il reçoit ; la **sollicitation** est la manière dont elles le chargent, la déformation en est l'effet. Séquences du thème : **torsion simple**, flexion plane simple, sollicitations composées ; compétences CD 1.7 (retrouver les sollicitations) et CD 2.1 (dimensionner et vérifier la résistance).
- **Le banc** — éprouvette de 8 mm de diamètre, tenue d'un côté, vrillée de l'autre par un levier r chargé d'une force F ; x est la longueur libre, α l'angle relatif de torsion lu au comparateur (un tour d'aiguille = 1°). **Torsion simple** : deux couples égaux et opposés, d'axe confondu avec la ligne moyenne.
- **Moment de torsion** — **Mt = F × r** ; F en N et r en mm donnent des **N·mm** (1 N·m = 1 000 N·mm). Le support de charge (2,5 N) compte dans F.
- **Mt et α** — dans le domaine élastique, **α est proportionnel à Mt** : Mt = k × α, droite passant par l'origine ; le zéro du comparateur se règle **avant** de charger, et k est plus grand pour l'acier que pour l'aluminium.
- **α et la longueur** — à Mt constant, **α est proportionnel à x** ; l'**angle unitaire de torsion** **θ = α / L** (en rad/mm) ne dépend pas de la longueur choisie.
- **Module G** — **G = Mt × L / (α × I₀)** avec **α en radians** et I₀ = π × d⁴ / 32 pour une section pleine ; valeurs théoriques acier 80 GPa, laiton 37 GPa, aluminium 28 GPa (1 GPa = 1 000 N/mm²).
- **Contrainte tangentielle** — **τ = (Mt / I₀) × ρ** : nulle au centre, maximale au bord (ρ = R = d / 2) ; **τmax = Mt / (I₀ / R)**, avec I₀ / R = π × d³ / 16 pour une section pleine.
- **Résistance** — **τmax ≤ Rpg avec Rpg = Reg / s** ; on compare toujours à Rpg, jamais à Reg, et d³ ≥ 16 × Mt / (π × Rpg), arrondi **par excès**.
- **Rigidité** — **θ ≤ θlimite**, fixé par l'expérience ; d⁴ ≥ 32 × Mt / (π × G × θlimite). Le diamètre retenu vérifie les deux conditions.
- **La méthode, en six marches** — charger, décrire la section, mesurer, identifier la matière, calculer la contrainte, conclure.
