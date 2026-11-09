# 📜 Résumé : Les bases de numération

- **Système de numération** : une base N est un entier au moins égal à 2 ; ses chiffres vont de 0 à N − 1 ; en base 16, les lettres A à F valent 10 à 15 ; une écriture n'a de sens qu'avec sa base, et le nombre N s'écrit 10 dans la base N
- **Hexadécimal vers binaire** : chaque chiffre se code sur 4 bits, on met les groupes bout à bout, puis on supprime seulement les zéros superflus du début ; valeur d'une lettre : code ASCII − 55
- **Binaire vers octal** : groupes de 3 bits en partant de la droite, dernier groupe complété par des 0 à gauche, chaque groupe est un chiffre de 0 à 7 ; un découpage depuis la gauche est faux
- **Octal vers binaire et binaire vers hexadécimal** : 3 bits par chiffre octal ; groupes de 4 bits depuis la droite pour l'hexadécimal ; octal et hexadécimal communiquent par le binaire, jamais chiffre à chiffre
- **Base B vers décimal** : le chiffre de rang i pèse Bⁱ, le rang 0 étant le chiffre de droite ; Conv_10 parcourt la chaîne de droite à gauche avec le rang `Length (ch) - i`
- **Décimal vers base B** : divisions successives par B jusqu'à un quotient nul ; les restes, lus du dernier au premier, forment le résultat (Ranger, Renverser, Convert) ; un reste de 10 à 15 s'écrit A à F
- **Base B1 vers base B2** : d'abord vers le décimal, puis du décimal vers B2 par divisions successives ; lire le nombre de départ comme du décimal est faux ; la chaîne résultat commence vide
