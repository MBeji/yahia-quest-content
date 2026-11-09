# 📜 Résumé : Le voyageur de commerce, les huit dames et le retour sur trace

- **Voyageur de commerce** : un circuit qui passe une fois par chaque ville et revient au départ, de longueur minimale ; la ville non visitée la plus proche de la ville en cours est une stratégie gloutonne qui donne un circuit valable mais pas toujours le plus court
- **Distance, Visite, Trajet** : matrice des distances, vecteur de booléens des villes visitées, vecteur de l'ordre de visite ; `Visite[depart]` doit passer à Vrai, et le retour au départ se compte à part dans `Longueur`
- **Ville_proche_non_visit** : minimum sous condition, parmi les villes non visitées, de Distance[c, j] depuis la ville en cours c (jamais depuis le rang de l'étape) ; le test strict garde la première ville en cas d'égalité
- **Insertion et énumération** : l'insertion place chaque ville là où le coût d(a, P) + d(P, b) − d(a, b) est le plus petit ; seule l'énumération des (n − 1) ! trajets garantit le plus court circuit
- **Permutations lexicographiques** : successeur en quatre étapes (plus grand i, plus grand j, permutation, renversement de T[i..n]) ; la liste s'arrête quand PGI rend 0
- **Huit dames** : une dame par ligne, T[i] est la colonne de la dame de la ligne i ; une case (lig, col) est menacée si T[j] = col ou Abs (T[j] − col) = lig − j
- **Retour sur trace** : en cas d'impasse, on revient en arrière, on essaie la colonne libre suivante et l'on explore toutes les branches ; une impasse ne prouve pas l'absence de solution
- **Place_dame** : cas particulier lig = nbd + 1 (une solution de plus), cas général une colonne après l'autre sans menace ; 92 solutions pour n = 8, 2 pour n = 4, aucune pour n = 2 et n = 3
