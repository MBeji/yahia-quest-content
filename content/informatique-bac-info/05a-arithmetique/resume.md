# 📜 Résumé : L'arithmétique

- **PGCD par la différence** : tant que a ≠ b, on retranche le plus petit du plus grand ; la valeur finale commune est le PGCD ; il faut a et b au moins égaux à 1, sinon la boucle ne s'arrête pas
- **PGCD récursif** : cas particulier a = b (résultat a), sinon appel sur (a − b, b) ou (a, b − a) ; sans le test a = b, l'appel ne s'arrête jamais
- **Arrangements Aₙᵖ** : p-uplets d'éléments distincts, l'ordre compte ; Aₙᵖ = n × (n − 1) × … × (n − p + 1) = n! / (n − p)! ; boucle décroissante de n à n − p + 1, en Réel ; Aₙⁿ = n!
- **Combinaisons Cₙᵖ** : parties de p éléments, sans ordre ; Cₙᵖ = Aₙᵖ / p! = n! / (p! × (n − p)!) ; sans la division par p!, on a un arrangement
- **Combinaisons récursives** : Cₙᵖ = 1 si p = 0 ou p = n, sinon Cₙ₋₁ᵖ + Cₙ₋₁ᵖ⁻¹ ; les deux cas d'arrêt sont nécessaires
- **Divisibilité par 3 et par 9** : la somme des chiffres doit l'être ; le nombre est lu comme une chaîne, `Val` convertit chaque caractère ; un multiple de 9 est un multiple de 3, jamais l'inverse
- **Divisibilité par 2, 4, 5, 10 et 25** : unités pour 2, 5 et 10 ; deux derniers chiffres pour 4 et 25 (`m Mod 100`) ; divisible par 6 si divisible par 2 et par 3
- **Chiffre inconnu** : écrire le nombre en fonction de u, traduire la règle en condition, essayer les valeurs de 0 à 9 avec une boucle ; avec deux inconnues, deux boucles imbriquées
