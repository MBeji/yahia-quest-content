# 📜 Résumé : Probabilités

- **Probabilité conditionnelle** : p(B/A) = p(A ∩ B)/p(A), on divise par la probabilité de l'événement que l'on sait réalisé. p(B/A) et p(A/B) sont deux nombres différents : dans le cours, 7/15 ≈ 0,467 et non 56/70 = 0,8.
- **Composées et arbre pondéré** : p(A ∩ B) = p(A) × p(B/A) ; sur un arbre on multiplie le long d'un chemin et la somme des branches d'un nœud vaut 1. Sans remise, le deuxième tirage se conditionne au premier : 5/8 × 4/7 = 5/14, pas (5/8)².
- **Indépendance** : A et B sont indépendants si p(A ∩ B) = p(A) × p(B), ce qui équivaut à p(B/A) = p(B) quand p(A) ≠ 0. Indépendants et incompatibles s'opposent : deux incompatibles de probabilités non nulles ne sont jamais indépendants.
- **Probabilités totales** : pour une partition (Aᵢ), p(B) = Σ p(B/Aᵢ) × p(Aᵢ), c'est la somme des chemins de l'arbre qui aboutissent à B. Les taux se pondèrent par les parts : 2,9 % dans le cours, non la moyenne simple 3,33 %.
- **Formule de Bayes** : p(A/B) = p(A) × p(B/A) / [p(A) × p(B/A) + p(Ā) × p(B/Ā)], elle inverse le conditionnement. Une alerte qui détecte 80 % des dossiers à risque ne donne pas 80 % de dossiers réellement à risque : le cours trouve 8/17 ≈ 0,47.
- **Loi et espérance** : une variable aléatoire associe un réel à chaque issue, sa loi est le tableau (xᵢ ; pᵢ) de somme 1, et E(X) = Σ xᵢpᵢ. Pour un gain algébrique on soustrait la mise ; E(X) = 0 équitable, > 0 favorable, < 0 défavorable.
- **Variance et écart type** : V(X) = E(X²) − [E(X)]² ≥ 0 et σ(X) = √V(X), dans l'unité de X. Dans le cours, V = 0,81 et σ = 0,9 : la racine se prend à la fin, et E(X²) se diminue de [E(X)]².
- **Schéma de Bernoulli et loi binomiale** : n épreuves identiques et indépendantes à deux issues donnent p(X = k) = C(n ; k) pᵏ qⁿ⁻ᵏ, E(X) = np et V(X) = npq. Le facteur C(n ; k) compte les ordres des succès ; « au moins un » se calcule par 1 − qⁿ. Un test de contrôle accepte les succès dans [E(X) − 2σ(X) ; E(X) + 2σ(X)].
