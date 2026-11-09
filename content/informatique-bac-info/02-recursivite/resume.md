# 📜 Résumé : La récursivité

- **Sous-programme récursif** : il s'appelle lui-même, directement dans son corps ou à travers d'autres sous-programmes qui le rappellent ; directe (P appelle P), indirecte (P → P1 → … → P) ou croisée (sous-programmes qui s'appellent mutuellement) ; appeler un autre sous-programme ne suffit pas
- **Cas particulier, cas général** : analyse par cas, avec un Si … Sinon obligatoire ; la valeur du cas particulier est le résultat du plus petit problème (0 pour une somme, 1 pour un produit)
- **Convergence** : les arguments doivent se rapprocher d'une condition d'arrêt qui les attrape tous, sinon l'exécution est infinie ; un test réussi sur une valeur ne prouve rien
- **Trace d'exécution** : descente jusqu'au cas particulier, puis remontée où les calculs en attente s'effectuent ; `Factorielle (n)` lance n + 1 appels
- **Pile** : chaque appel empile sa propre valeur du paramètre ; lisibilité d'un côté, limite de mémoire et débordement de pile de l'autre
- **Chaînes** : `Copy` réduit la chaîne ; `Palindrome` retire deux caractères avec `Length (ch) - 2` et s'arrête si `Length (ch) < 2` ou si les extrémités diffèrent ; `Inverse` en retire un
- **Tableaux** : un appel traite un sous-tableau T[deb..fin] ; le tri par sélection place le maximum en deb et s'arrête quand deb < fin est faux ; la dichotomie suppose un tableau trié et compare à T[milieu]
- **Itératif et récursif** : la dérécursification passe de l'auto-appel à la boucle ; pour corriger un module, on vérifie le cas particulier, la relation de récurrence et la convergence, jamais les seuls cas d'arrêt
