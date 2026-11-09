# ⚔️ Les bases de numération — un même nombre, plusieurs écritures

> 💡 «Un nombre ne change pas quand on le réécrit dans une autre base : seule son écriture change.»

Un ordinateur compte avec deux chiffres, un humain avec dix, un électronicien avec seize. Ce chapitre apprend à lire un nombre dans n'importe quelle base et à passer d'une base à une autre, en pseudo-langage et en Pascal. Sept notions : le système de numération, les conversions par regroupement de bits (hexadécimal vers binaire, binaire vers octal, puis les deux sens inverses), puis les conversions par puissances et par divisions successives (base B vers décimal, décimal vers base B, base B1 vers base B2). Les chapitres précédents, surtout le calcul de `Mod` et `Div`, sont supposés connus.

## 🔢 Les systèmes de numération : base et chiffres

L'écriture 1011 se lit-elle « mille onze » ? En binaire elle désigne le nombre onze, comme la suite du chapitre le montrera. Sans la base, une écriture ne dit pas quel nombre elle représente.
Quels chiffres a-t-on le droit d'écrire dans une base donnée ?

::: definition
Un **système de numération** est une méthode de comptage fondée sur une **base** N, entier supérieur ou égal à 2. Le système a exactement N **chiffres**, de 0 à N − 1. On note la base en indice : (1011)₂.
Quatre bases servent en informatique : le binaire (base 2), l'octal (base 8), le décimal (base 10) et l'hexadécimal (base 16). En base 16, les lettres A, B, C, D, E, F représentent les valeurs 10, 11, 12, 13, 14, 15.
:::

| base | nom         | chiffres                    |
| ---- | ----------- | --------------------------- |
| 2    | binaire     | 0 et 1                      |
| 8    | octal       | 0 à 7                       |
| 10   | décimal     | 0 à 9                       |
| 16   | hexadécimal | 0 à 9, puis A à F (10 à 15) |

Dans une base plus grande, le même nombre s'écrit avec autant de chiffres ou moins : 255 s'écrit (11111111)₂ avec huit chiffres, (377)₈ avec trois et (FF)₁₆ avec deux.

::: exemple Quelles bases acceptent l'écriture 4075 ?

1. Le plus grand chiffre de 4075 est 7.
2. Une base N a des chiffres de 0 à N − 1 : il faut N − 1 ≥ 7, donc N ≥ 8.
3. Les bases 8, 10, 12 et 16 conviennent ; la base 2 ne convient pas.

:::

Pour manipuler les chiffres en Pascal, deux fonctions suffisent : `Valeur_Chiffre` donne la valeur d'un caractère (le code ASCII de A est 65, d'où 65 − 55 = 10) et `Convert` fait le chemin inverse.

```pascal
Function Valeur_Chiffre (c : Char) : Integer;
Begin
  If c In ['0'..'9'] Then Valeur_Chiffre := Ord (c) - 48
  Else Valeur_Chiffre := Ord (UpCase (c)) - 55;
End;

Function Convert (v : Integer) : Char;
Begin
  If v < 10 Then Convert := Chr (48 + v)
  Else Convert := Chr (55 + v);
End;
```

::: piege
**Erreur : lire 1011 comme « mille onze » dans toutes les bases.** On lit les chiffres comme du décimal, par habitude. L'erreur tente parce que le décimal est la seule base de la vie courante. Mais (1011)₂ vaut onze, pas mille onze : la base fait partie de l'écriture, et une écriture sans base ne désigne aucun nombre précis.
:::

::: propriete
Dans la base N, le nombre N s'écrit 10 : (10)₂ = 2, (10)₈ = 8, (10)₁₆ = 16.
Cas limite : une lettre ne peut apparaître que dans une base supérieure à 10 (la lettre A exige N ≥ 11), et le chiffre N lui-même n'existe jamais dans la base N.
:::

::: verifie À toi : la plus petite base
Quelle est la plus petite base dans laquelle on peut écrire 1C ?

---

C vaut 12, donc il faut N − 1 ≥ 12, soit N ≥ 13. La plus petite base possible est 13. Parmi les bases courantes 2, 8, 10 et 16, seule la base 16 convient.
:::

::: retenir
Une base N est un entier au moins égal à 2 ; ses chiffres vont de 0 à N − 1, avec les lettres A à F pour 10 à 15 ; une écriture n'a de sens qu'avec sa base.
:::

## 🔡 Hexadécimal vers binaire : 4 bits par chiffre

La suite de bits 1111000101 est longue et facile à mal recopier. Un chiffre hexadécimal vaut de 0 à 15 : 16 valeurs, et 4 bits en donnent exactement 2⁴ = 16.
Peut-on remplacer chaque chiffre hexadécimal par 4 bits, sans calcul ?

::: definition
**Hexadécimal vers binaire** : chaque chiffre hexadécimal se code sur **4 bits**. On convertit les chiffres un à un, de gauche à droite, on les met bout à bout, puis on supprime les **zéros superflus du début**.
:::

| chiffre | A    | B    | C    | D    | E    | F    |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- |
| valeur  | 10   | 11   | 12   | 13   | 14   | 15   |
| 4 bits  | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |

Pour les chiffres de 0 à 9, on écrit la valeur sur 4 bits : 5 donne 0101, 9 donne 1001.

::: exemple Convertir (3C5)₁₆ en binaire

1. 3 donne 0011, C vaut 12 donc donne 1100, 5 donne 0101.
2. Bout à bout : 0011 1100 0101.
3. On supprime les zéros du début : 1111000101.

:::

```pascal
Function Bits (v, nb : Integer) : String;
Var i : Integer; ch : String;
Begin
  ch := '';
  For i := 1 To nb Do
  Begin
    ch := Convert (v Mod 2) + ch;
    v := v Div 2;
  End;
  Bits := ch;
End;

Function Conv_Bin (hex : String) : String;
Var i : Integer; ch : String;
Begin
  ch := '';
  For i := 1 To Length (hex) Do
    ch := ch + Bits (Valeur_Chiffre (hex[i]), 4);
  While (Length (ch) > 1) And (ch[1] = '0') Do Delete (ch, 1, 1);
  Conv_Bin := ch;
End;
```

`Bits (v, nb)` écrit v sur exactement nb bits, en ajoutant chaque reste à gauche de la chaîne.

::: piege
**Erreur : ne pas remplir chaque chiffre sur 4 bits.** Pour B03, on écrit 1011, puis 0, puis 11 : 1011011. L'erreur tente parce que les zéros semblent inutiles. Mais seuls les zéros du **début du résultat** sont superflus ; ceux de l'intérieur occupent leur place. Le bon résultat est 1011 0000 0011, soit 101100000011, sur 12 bits et non 7.
:::

::: propriete
Un nombre de n chiffres hexadécimaux donne au plus 4 × n bits.
Cas limite : (0)₁₆ donne 0000. La boucle de suppression doit s'arrêter au dernier caractère (`Length (ch) > 1`), sinon la chaîne devient vide.
:::

::: verifie À toi : hexadécimal vers binaire
Convertir (7E)₁₆ en binaire.

---

7 donne 0111 et E vaut 14, donc donne 1110. Bout à bout : 0111 1110. On supprime le zéro du début : 1111110.
:::

::: retenir
Chaque chiffre hexadécimal se convertit en exactement 4 bits (valeurs A à F : 10 à 15) ; on met les groupes bout à bout et on supprime seulement les zéros du début du résultat.
:::

## 🧩 Binaire vers octal : groupes de 3 bits

Le nombre binaire 1011011 compte sept bits. Un chiffre octal vaut de 0 à 7 : 8 valeurs, soit 2³, donc 3 bits.
Comment découper une suite de bits pour lire directement les chiffres octaux ?

::: definition
**Binaire vers octal** : on découpe le nombre en groupes de **3 bits, en partant de la droite**. Si le dernier groupe (celui de gauche) est incomplet, on le **complète par des 0 à gauche**. Un groupe abc vaut 4 × a + 2 × b + c : c'est un chiffre octal.
:::

| groupe        | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| chiffre octal | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |

::: exemple Convertir (1011011)₂ en octal

1. En partant de la droite : 011, puis 011, puis il reste 1.
2. On complète le dernier groupe : 001.
3. 001 vaut 1, 011 vaut 3, 011 vaut 3 : le résultat est (133)₈.

:::

```pascal
Function Conv_Oct (bin : String) : String;
Var i, j, l, v : Integer; oct, g : String;
Begin
  While Length (bin) Mod 3 <> 0 Do bin := '0' + bin;
  oct := '';
  l := Length (bin);
  For i := 1 To Length (bin) Div 3 Do
  Begin
    g := Copy (bin, l - 2, 3);
    v := 0;
    For j := 1 To 3 Do v := v * 2 + Valeur_Chiffre (g[j]);
    oct := Convert (v) + oct;
    l := l - 3;
  End;
  Conv_Oct := oct;
End;
```

La boucle `Tant que` complète la chaîne à gauche jusqu'à une longueur multiple de 3 ; `Copy (bin, l - 2, 3)` prend les 3 derniers bits non traités, et `l` recule de 3 à chaque tour.

::: piege
**Erreur : découper depuis la gauche.** On coupe 1011011 en 101, 101, 1 et on lit 5, 5, 1 : (551)₈. L'erreur tente parce qu'on lit de gauche à droite. Mais le poids d'un bit se mesure depuis le bit de droite : seul le découpage depuis la droite aligne les groupes sur les puissances de 8. (551)₈ vaut 361, alors que (1011011)₂ et (133)₈ valent 91.
:::

::: propriete
Un nombre binaire de n bits donne n / 3 chiffres octaux, arrondi à l'entier supérieur.
Cas limite : si n est déjà un multiple de 3, aucun zéro n'est ajouté (la boucle `Tant que` ne s'exécute pas).
:::

::: verifie À toi : binaire vers octal
Convertir (110101)₂ en octal.

---

On a 6 bits, un multiple de 3 : pas de zéro à ajouter. En partant de la droite : 101 vaut 5, puis 110 vaut 6. Le résultat est (65)₈.
:::

::: retenir
Pour passer du binaire à l'octal, on groupe les bits par 3 depuis la droite, on complète à gauche par des 0, et chaque groupe devient un chiffre de 0 à 7.
:::

## 🔄 Octal vers binaire et binaire vers hexadécimal

On sait passer de l'hexadécimal au binaire (4 bits par chiffre) et du binaire à l'octal (groupes de 3). Les deux sens inverses reprennent les mêmes idées.
Comment passer de l'octal à l'hexadécimal sans effectuer de calcul ?

::: definition
**Octal vers binaire** : chaque chiffre octal devient un groupe de **3 bits**.
**Binaire vers hexadécimal** : on découpe en groupes de **4 bits depuis la droite**, on complète le dernier groupe par des 0 à gauche, et chaque groupe donne un chiffre hexadécimal (10 à 15 s'écrivent A à F).
:::

::: exemple Convertir (751)₈ en hexadécimal par le binaire

1. 7 donne 111, 5 donne 101, 1 donne 001 : le binaire est 111101001, soit 9 bits.
2. Depuis la droite : 1001, puis 1110, puis il reste 1, complété en 0001.
3. 0001 vaut 1, 1110 vaut 14 donc E, 1001 vaut 9 : le résultat est (1E9)₁₆.

:::

```pascal
Function Oct_Bin (oct : String) : String;
Var i : Integer; ch : String;
Begin
  ch := '';
  For i := 1 To Length (oct) Do
    ch := ch + Bits (Valeur_Chiffre (oct[i]), 3);
  While (Length (ch) > 1) And (ch[1] = '0') Do Delete (ch, 1, 1);
  Oct_Bin := ch;
End;

Function Conv_Hex (bin : String) : String;
Var i, j, l, v : Integer; hex, g : String;
Begin
  While Length (bin) Mod 4 <> 0 Do bin := '0' + bin;
  hex := '';
  l := Length (bin);
  For i := 1 To Length (bin) Div 4 Do
  Begin
    g := Copy (bin, l - 3, 4);
    v := 0;
    For j := 1 To 4 Do v := v * 2 + Valeur_Chiffre (g[j]);
    hex := Convert (v) + hex;
    l := l - 4;
  End;
  Conv_Hex := hex;
End;
```

`Oct_Bin` reprend `Conv_Bin` avec 3 bits au lieu de 4 ; `Conv_Hex` reprend `Conv_Oct` avec des groupes de 4, et `Convert` fournit les lettres.

::: piege
**Erreur : passer de l'octal à l'hexadécimal en recopiant les chiffres.** (751)₈ deviendrait « 751 » en hexadécimal. L'erreur tente parce que les chiffres 0 à 7 existent dans les deux bases. Mais (751)₈ vaut 489, alors que (751)₁₆ vaut 1873. Les deux bases ne se lisent pas chiffre à chiffre l'une dans l'autre : on passe par les bits.
:::

::: propriete
Un chiffre octal vaut 3 bits, un chiffre hexadécimal 4 bits : la conversion octal vers hexadécimal passe le plus simplement par le binaire.
Cas limite : l'hexadécimal n'utilise jamais plus de chiffres que l'octal pour un même nombre, mais il peut en utiliser moins : (5)₈ = (5)₁₆ n'a qu'un chiffre dans chaque base, alors que (777)₈ = (1FF)₁₆ garde trois chiffres et (7777)₈ = (FFF)₁₆ passe de quatre chiffres à trois.
:::

::: verifie À toi : octal vers hexadécimal
Convertir (35)₈ en hexadécimal, en passant par le binaire.

---

3 donne 011 et 5 donne 101 : le binaire est 011101, soit 11101 sans le zéro du début. On le découpe depuis la droite : 1101, puis 01 complété en 0001. 0001 vaut 1 et 1101 vaut 13 donc D : le résultat est (1D)₁₆.
:::

::: retenir
Octal vers binaire : 3 bits par chiffre. Binaire vers hexadécimal : groupes de 4 bits depuis la droite, complétés à gauche. Octal et hexadécimal communiquent le plus simplement par le binaire.
:::

## ⚖️ Base B vers décimal : somme des chiffres par puissances

Dans 307, le 3 vaut trois centaines, soit 3 × 10², le 0 ne compte pour rien et le 7 vaut sept unités. Le poids d'un chiffre dépend de sa place. En base 8, la « centaine » ne vaut plus 100 mais 8² = 64.
Comment calculer la valeur décimale d'un nombre écrit dans une autre base ?

::: definition
**Base B vers décimal** : le chiffre de **rang** i pèse Bⁱ, le rang 0 étant le chiffre de **droite**. La valeur de (cₖ … c₁ c₀) en base B est :
cₖ × Bᵏ + … + c₁ × B¹ + c₀ × B⁰.
:::

::: exemple Convertir (2AF)₁₆ en décimal

1. F est au rang 0, A au rang 1, 2 au rang 2. Les lettres valent F = 15 et A = 10.
2. Valeur = 2 × 16² + 10 × 16¹ + 15 × 16⁰.
3. 512 + 160 + 15 = 687.

:::

```pascal
Function Puiss (b, k : Integer) : LongInt;
Var p : LongInt; j : Integer;
Begin
  p := 1;
  For j := 1 To k Do p := p * b;
  Puiss := p;
End;

Function Conv_10 (ch : String; b : Integer) : LongInt;
Var i : Integer; total : LongInt;
Begin
  total := 0;
  For i := Length (ch) Downto 1 Do
    total := total + Valeur_Chiffre (ch[i]) * Puiss (b, Length (ch) - i);
  Conv_10 := total;
End;
```

La boucle part du chiffre de droite : son rang est `Length (ch) - i`, qui vaut 0 pour `i = Length (ch)`. Une fois en décimal, le nombre se manipule comme un entier : pour savoir si un binaire est divisible par un autre, on convertit les deux avec `Conv_10`, puis on teste le reste avec `Mod`.

::: piege
**Erreur : numéroter les rangs depuis la gauche.** Pour (14)₈, on calcule 1 × 8⁰ + 4 × 8¹ = 33, en donnant la puissance 0 au premier chiffre lu. L'erreur tente parce qu'on compte en lisant de gauche à droite. Mais le rang 0 est celui du chiffre de **droite** : (14)₈ = 1 × 8¹ + 4 × 8⁰ = 12. C'est le rôle de `Length (ch) - i` dans le code.
:::

::: propriete
Un nombre de n chiffres en base B est compris entre Bⁿ⁻¹ (écriture 100…0) et Bⁿ − 1 (tous les chiffres valent B − 1) : (FF)₁₆ = 16² − 1 = 255.
Cas limite : le résultat doit tenir dans un `LongInt`, au plus 2 147 483 647. Huit chiffres hexadécimaux peuvent le dépasser : (FFFFFFFF)₁₆ vaut 4 294 967 295.
:::

::: verifie À toi : base B vers décimal
Quelle est la valeur décimale de (305)₇ ?

---

Les rangs : 5 au rang 0, 0 au rang 1, 3 au rang 2. Valeur = 3 × 7² + 0 × 7¹ + 5 × 7⁰ = 147 + 0 + 5 = 152.
:::

::: retenir
(cₖ … c₀) en base B vaut cₖ × Bᵏ + … + c₀ × B⁰ : le rang 0 est le chiffre de droite, et les lettres A à F valent 10 à 15.
:::

## ➗ Décimal vers base B : divisions successives

Pour écrire 37 en binaire, on se demande combien de fois 2 entre dans 37 et ce qui reste, puis on recommence avec le quotient, jusqu'à ne plus rien avoir à diviser.
Dans quel ordre lire les restes ainsi obtenus ?

::: definition
**Décimal vers base B (divisions successives)** : on divise N par B, puis le quotient par B, et ainsi de suite jusqu'à un **quotient nul**. Les **restes**, lus **du dernier au premier**, sont les chiffres du résultat.
:::

| division | quotient | reste |
| -------- | -------- | ----- |
| 37 ÷ 2   | 18       | 1     |
| 18 ÷ 2   | 9        | 0     |
| 9 ÷ 2    | 4        | 1     |
| 4 ÷ 2    | 2        | 0     |
| 2 ÷ 2    | 1        | 0     |
| 1 ÷ 2    | 0        | 1     |

Les restes dans l'ordre obtenu sont 1, 0, 1, 0, 0, 1 ; lus à l'envers, ils donnent (100101)₂.

::: exemple Convertir 750 en hexadécimal

1. 750 = 46 × 16 + 14, reste 14 (E).
2. 46 = 2 × 16 + 14, reste 14 (E).
3. 2 = 0 × 16 + 2, reste 2 : le quotient est nul, on s'arrête.
4. Restes dans l'ordre : E, E, 2 ; lus à l'envers : (2EE)₁₆.

:::

```pascal
Const RMAX = 15;
Type Tab = Array [1..RMAX] Of Integer;

Procedure Ranger (n, b : Integer; Var restes : Tab; Var r : Integer);
Begin
  r := 0;
  Repeat
    r := r + 1;
    restes[r] := n Mod b;
    n := n Div b;
  Until n = 0;
End;

Procedure Renverser (Var restes : Tab; r : Integer);
Var i, t : Integer;
Begin
  For i := 1 To r Div 2 Do
  Begin
    t := restes[i];
    restes[i] := restes[r - i + 1];
    restes[r - i + 1] := t;
  End;
End;
```

`Ranger` range les restes et compte `r` ; `Renverser` échange le 1er avec le r-ième, le 2e avec l'avant-dernier, jusqu'au milieu. Il reste à écrire `Convert (restes[i])` pour i de 1 à r, du premier au dernier : le tableau renversé donne alors le résultat dans le bon ordre.

::: piege
**Erreur : lire les restes dans l'ordre où on les obtient.** Pour 37, on lit 1, 0, 1, 0, 0, 1 de haut en bas : 101001. L'erreur tente parce qu'on lit un tableau de haut en bas. Mais le premier reste est le chiffre des unités, le **dernier** est le chiffre de gauche : 101001 vaut 41, alors que 100101 vaut 37.
:::

::: propriete
La boucle `Répéter … Jusqu'à n = 0` s'exécute autant de fois que le résultat a de chiffres. Avec RMAX cases, le plus grand nombre rangeable en base B est B puissance RMAX, moins 1 : en base 2 avec RMAX = 15, c'est 2¹⁵ − 1 = 32 767.
Cas limite : pour N = 0, `Répéter` produit un seul reste, 0 ; un `Tant que n ≠ 0` ne produirait aucun chiffre.
:::

::: verifie À toi : décimal vers base B
Écrire 90 en base 4.

---

90 = 22 × 4 + 2, reste 2. 22 = 5 × 4 + 2, reste 2. 5 = 1 × 4 + 1, reste 1. 1 = 0 × 4 + 1, reste 1. Les restes dans l'ordre sont 2, 2, 1, 1 ; lus à l'envers, ils donnent (1122)₄.
:::

::: retenir
On divise par B jusqu'à un quotient nul ; les restes, lus du dernier au premier, forment le résultat ; les restes de 10 à 15 s'écrivent A à F.
:::

## 🔗 De la base B1 à la base B2 en passant par le décimal

Comment passer de la base 7 à la base 5 ? Aucune de ces bases n'est une puissance de l'autre : le regroupement de bits ne s'applique pas. Mais on sait déjà aller de n'importe quelle base vers le décimal, et du décimal vers n'importe quelle base.
Peut-on enchaîner les deux conversions ?

::: definition
**Base B1 vers base B2** (2 ≤ B1 ≤ 16 et 2 ≤ B2 ≤ 16) : on convertit d'abord le nombre de la base B1 vers le **décimal** (chiffre × puissance de B1), puis on convertit ce nombre décimal vers la base B2 (**divisions successives** par B2).
:::

::: exemple Convertir (54)₇ en base 5

1. Vers le décimal : 5 × 7 + 4 = 39.
2. 39 = 7 × 5 + 4, reste 4. 7 = 1 × 5 + 2, reste 2. 1 = 0 × 5 + 1, reste 1.
3. Restes dans l'ordre : 4, 2, 1 ; lus à l'envers : (124)₅. Contrôle : 1 × 25 + 2 × 5 + 4 = 39 ✓.

:::

```pascal
Function Conv_B2 (n : LongInt; b : Integer) : String;
Var ch : String;
Begin
  ch := '';
  Repeat
    ch := Convert (n Mod b) + ch;
    n := n Div b;
  Until n = 0;
  Conv_B2 := ch;
End;

Function Conversion (ch : String; b1, b2 : Integer) : String;
Begin
  Conversion := Conv_B2 (Conv_10 (ch, b1), b2);
End;
```

Le reste est ajouté à **gauche** de `ch` : la chaîne se construit déjà dans le bon ordre, sans `Renverser`.

::: piege
**Erreur : lire le nombre de départ comme s'il était décimal.** Pour (54)₇ vers la base 5, on divise 54 par 5 : restes 4, 0, 2, donc 204. L'erreur tente parce que 5 et 4 se lisent « cinquante-quatre ». Mais (54)₇ vaut 39, pas 54 ; (204)₅ vaut 54. Sauter l'étape vers le décimal change le nombre.
:::

::: propriete
Si B1 = B2, le résultat est le nombre de départ ; si B1 vaut 10, `Conv_10` renvoie le nombre tel quel.
Cas limite : `ch` doit commencer **vide**, jamais avec un espace, sinon l'espace resterait collé à la fin du résultat ; et la valeur décimale intermédiaire doit tenir dans un `LongInt`.
:::

::: verifie À toi : de B1 à B2
Convertir (1F)₁₆ en base 8.

---

Vers le décimal : 1 × 16 + 15 = 31. Puis 31 = 3 × 8 + 7, reste 7 ; 3 = 0 × 8 + 3, reste 3. Les restes dans l'ordre sont 7, 3 ; lus à l'envers : (37)₈.
:::

::: retenir
Pour passer de B1 à B2, on convertit d'abord vers le décimal, puis du décimal vers B2 par divisions successives ; sauter la première étape revient à lire le nombre comme du décimal.
:::

> 🗡️ Devant une conversion, demande-toi d'abord : « les deux bases sont-elles des puissances de 2 ? » Si oui, regroupe les bits ; sinon, passe par le décimal.

> 🏆 Porte franchie ! Tu sais lire un nombre dans n'importe quelle base et le convertir, par les bits ou par le décimal. Prochaine arène : les algorithmes d'approximation.
