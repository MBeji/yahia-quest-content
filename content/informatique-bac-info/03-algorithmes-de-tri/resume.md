# 📜 Résumé : Les algorithmes de tri

- **Trier** : ranger les mêmes valeurs dans un ordre donné (croissant, décroissant, alphabétique) ; tri interne sur un tableau en mémoire centrale, tri externe sur de grands fichiers ; « trié » se juge par rapport à l'ordre demandé
- **Tri par sélection** : à l'étape i, échanger T[i] avec le minimum de T[i..n] (`Pos_Min`) ; n − 1 étapes, au plus un échange par étape ; la recherche ne remonte jamais avant la case i
- **Tri à bulles** : permuter les voisins mal rangés, la plus grande valeur restante est fixée en fin à chaque passage ; arrêt au premier passage sans permutation ; le sens du test `>` ou `<` donne l'ordre
- **Tri par insertion** : sauvegarder T[i] dans Tmp, décaler à droite les éléments plus grands, ranger Tmp en T[j + 1] ; efficace sur un tableau presque trié, d'ordre n² en moyenne
- **Tri Shell** : insertion sur des sous-vecteurs de pas p, avec p ← 3p + 1 vers le haut tant que p < n puis p ← p Div 3 vers le bas ; le dernier passage, de pas 1, est indispensable
- **Fusion** : comparer les têtes de deux tableaux triés, recopier la plus petite, puis recopier le reste de l'autre ; n1 + n2 éléments ; le tri par fusion coupe, trie les moitiés, fusionne, au prix d'un tableau intermédiaire
- **Rang et comptage** : rang = 1 + nombre de valeurs strictement supérieures (ex æquo possibles) ; position de comptage = 1 + nombre de valeurs strictement inférieures (valeurs distinctes) ; tableau d'enregistrements plutôt que tableaux parallèles
