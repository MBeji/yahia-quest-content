# 📜 Résumé : Le tri rapide et les tours de Hanoï

- **Tri rapide** : choisir un pivot (le premier élément), faire la partition (valeurs ≤ pivot à gauche, > pivot à droite), le pivot est alors à sa place définitive ; on recommence sur les deux côtés tant qu'ils ont au moins deux éléments ; la partition ne trie pas les côtés
- **Partition pas à pas** : i avance tant que T[i] ≤ pivot, j recule tant que T[j] > pivot, on échange T[i] et T[j] puis on continue ; quand i > j, on échange le pivot avec T[j] (jamais avec T[i])
- **Tri rapide en Pascal** : `Partition` rend la case m du pivot, `Tri_Rapide (T, g, d)` agit seulement si g < d puis s'appelle sur T[g..m − 1] et T[m + 1..d] ; appel initial `Tri_Rapide (T, 1, n)`
- **Pivot et pire cas** : avec le premier élément pour pivot, un tableau déjà trié (croissant ou décroissant) est le pire cas, n − 1 partitions ; un pivot qui coupe en deux moitiés est le meilleur ; aucun choix fixe n'élimine tous les pires cas
- **Hanoï, la règle** : n disques sur le piquet de départ, un seul disque à la fois, jamais sur un plus petit ; n − 1 disques vers l'intermédiaire, le grand disque vers la cible, n − 1 disques vers la cible
- **Hanoï en Pascal** : `Hanoi (n, depart, cible, inter)` appelle `Hanoi (n − 1, depart, inter, cible)`, affiche un déplacement, puis appelle `Hanoi (n − 1, inter, cible, depart)` ; n = 2 donne 3 déplacements, n = 3 en donne 7
- **Nombre de déplacements** : u(n) = 2 × u(n − 1) + 1 = 2ⁿ − 1, un disque de plus double le travail ; 64 disques à un déplacement par seconde demandent environ 585 milliards d'années ; un `LongInt` compte jusqu'à n = 31
- **Tri comptage** : compter les occurrences de chaque valeur entière de [0, vmax] dans `occ`, puis écrire chaque valeur v exactement `occ[v]` fois dans l'ordre des indices ; accepte les doublons, exige des valeurs bornées
