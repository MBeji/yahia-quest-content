# ⚔️ L'arithmétique — PGCD, dénombrement et règles de divisibilité

> 💡 «Avant de calculer, regarde le nombre : il te dit déjà presque tout.»

Ce chapitre apprend à faire des mathématiques avec des algorithmes : trouver le plus grand diviseur commun de deux nombres, compter des choix, et reconnaître en un coup d'œil si un nombre se partage exactement. Huit notions, en pseudo-langage algorithmique et en Pascal ; la récursivité du chapitre 2 est supposée connue. Les conversions entre bases de numération sont l'objet d'un autre chapitre.

## 🧮 Le PGCD par la méthode de la différence

Un couloir mesure 22 dm sur 6 dm. On veut le couvrir de dalles carrées entières, sans aucune découpe, les plus grandes possible. Le côté d'une dalle doit diviser 22 et 6.
Comment trouver ce plus grand côté sans lister tous les diviseurs ?

::: definition
Le **PGCD** de deux entiers positifs non nuls a et b est leur **P**lus **G**rand **C**ommun **D**iviseur : le plus grand entier qui divise a et b.
La **méthode de la différence** : tant que a ≠ b, on remplace le plus grand des deux par la différence a − b (ou b − a). Quand a = b, cette valeur commune est le PGCD.
:::

Tout diviseur commun de a et b divise aussi leur différence, et réciproquement : remplacer le plus grand par la différence ne change donc pas le PGCD. Voici la suite des couples pour 22 et 6.

| étape | a   | b   |
| ----- | --- | --- |
| début | 22  | 6   |
| 1     | 16  | 6   |
| 2     | 10  | 6   |
| 3     | 4   | 6   |
| 4     | 4   | 2   |
| 5     | 2   | 2   |

La dernière ligne a = b = 2 : le plus grand côté de dalle est 2 dm.

::: exemple Dérouler la méthode sur 22 et 6

1. 22 > 6 : a devient 22 − 6 = 16, car le PGCD du couple ne change pas.
2. 16 > 6 : a devient 10. Puis 10 > 6 : a devient 4.
3. Maintenant 4 < 6, c'est b le plus grand : b devient 6 − 4 = 2.
4. 4 > 2 : a devient 2. On a a = b = 2 : la boucle s'arrête, PGCD (22, 6) = 2.
5. Contrôle : les diviseurs de 22 sont 1, 2, 11, 22 et ceux de 6 sont 1, 2, 3, 6 ; le plus grand commun est bien 2 ✓.

:::

```
0) Fonction Pgcd (a, b : Entier) : Entier
1) Tant que (a ≠ b) Faire
      Si (a > b) Alors a ← a - b
      Sinon b ← b - a
      Fin Si
   Fin Tant que
2) Pgcd ← a
3) Fin Pgcd
```

::: piege
**Erreur : retrancher toujours b de a, sans comparer.** On écrit `a ← a - b` à chaque tour, par habitude de « la différence ». L'erreur tente parce que, pour 22 et 6, les premières étapes marchent. Mais pour a = 6 et b = 22, a devient 6 − 22 = −16, puis −38, puis −60 : a s'éloigne de b et la boucle ne s'arrête jamais. Il faut retrancher le plus petit du plus grand, d'où le `Si (a > b)`.
:::

::: propriete
La méthode de la différence s'arrête toujours quand a et b sont des entiers **strictement positifs** : chaque tour fait baisser a + b, et a et b restent au moins égaux à 1.
Cas limite : avec b = 0, `Pgcd (5, 0)` ne s'arrête jamais, puisque a ← 5 − 0 laisse a inchangé.
:::

::: verifie À toi : dérouler la méthode
Donner la suite des couples (a, b) pour 18 et 12, puis le PGCD.

---

18 > 12 : a devient 18 − 12 = 6, couple (6, 12). Alors b est le plus grand : b devient 12 − 6 = 6, couple (6, 6). On a a = b : PGCD (18, 12) = 6. Chaque pas retranche le plus petit du plus grand, sans changer le PGCD.
:::

::: retenir
Le PGCD de a et b (entiers au moins égaux à 1) se trouve en retranchant le plus petit du plus grand tant que a ≠ b ; la valeur finale commune est le PGCD.
:::

## 🔁 Le PGCD récursif

Relis le tableau : chaque ligne est le PGCD d'un couple plus petit que la ligne précédente. PGCD (22, 6) est égal à PGCD (16, 6), qui est égal à PGCD (10, 6)…
Cette chaîne peut-elle s'écrire comme une fonction qui s'appelle elle-même ?

::: definition
**Relation récursive du PGCD** :
Si a = b, alors PGCD (a, b) = a (cas particulier).
Sinon, si a > b, alors PGCD (a, b) = PGCD (a − b, b).
Sinon, PGCD (a, b) = PGCD (a, b − a) (cas général : un problème plus petit).
:::

::: exemple Évaluer la relation sur 9 et 6

1. 9 ≠ 6 et 9 > 6 : PGCD (9, 6) = PGCD (3, 6), car a est remplacé par 9 − 6.
2. 3 ≠ 6 et 3 < 6 : PGCD (3, 6) = PGCD (3, 3), car b est remplacé par 6 − 3.
3. 3 = 3 : cas particulier, PGCD (3, 3) = 3. On remonte : PGCD (9, 6) = 3 ✓.

:::

```
0) Fonction Pgcd (a, b : Entier) : Entier
1) Si (a = b) Alors Pgcd ← a
   Sinon Si (a > b) Alors Pgcd ← Pgcd (a - b, b)
   Sinon Pgcd ← Pgcd (a, b - a)
   Fin Si
2) Fin Pgcd
```

```pascal
Function Pgcd (n, m : Integer) : Integer;
Begin
  If n = m Then Pgcd := m
  Else If n > m Then Pgcd := Pgcd (n - m, m)
  Else Pgcd := Pgcd (n, m - n);
End;
```

Le test `n = m` est le cas particulier ; chacune des deux autres branches est un appel sur un couple dont la somme a baissé.

::: piege
**Erreur : oublier le cas a = b.** On écrit seulement `Si (a > b) Alors Pgcd (a - b, b) Sinon Pgcd (a, b - a)`. L'erreur tente parce que les deux appels semblent couvrir tous les cas. Mais pour (3, 3), le `Sinon` appelle Pgcd (3, 0), qui rappelle Pgcd (3, 0) sans fin : le débordement de pile arrive. Le cas a = b est précisément la condition d'arrêt.
:::

::: verifie À toi : le PGCD récursif
Évaluer PGCD (8, 12) avec la relation récursive.

---

8 ≠ 12 et 8 < 12 : PGCD (8, 12) = PGCD (8, 4), car b est remplacé par 12 − 8. Puis 8 > 4 : PGCD (8, 4) = PGCD (4, 4). Enfin 4 = 4 : cas particulier, PGCD = 4.
:::

::: retenir
Le PGCD récursif a un cas particulier (a = b, résultat a) et deux appels sur un couple plus petit ; sans le test a = b, l'appel ne s'arrête jamais.
:::

## 🎖️ Les arrangements Aₙᵖ

Un club compte 5 élèves. On désigne dans l'ordre un président, un secrétaire et un trésorier, trois élèves différents. Pour le président, 5 choix ; pour le secrétaire, il en reste 4 ; pour le trésorier, 3 : 5 × 4 × 3 = 60 listes.
Comment compter de même pour n élèves et p postes, et le programmer ?

::: definition
Un **arrangement** de p éléments d'un ensemble E de n éléments est un **p-uplet d'éléments distincts** de E : l'ordre compte. Leur nombre se note Aₙᵖ (A(n, p) dans les programmes), avec 1 ≤ p ≤ n.
$$ Aₙᵖ = n × (n − 1) × (n − 2) × … × (n − p + 1) = n! / (n − p)! $$
:::

Le produit a exactement p facteurs : le premier est n, le dernier est n − p + 1. Pour n = 5 et p = 3, les facteurs sont 5, 4 et 3, comme dans le club : A₅³ = 60.

::: exemple Calculer A₈² par la formule

1. Il y a p = 2 facteurs, en partant de n = 8 : le premier est 8, le dernier est 8 − 2 + 1 = 7.
2. A₈² = 8 × 7 = 56.
3. Contrôle par la factorielle : 8! / 6! = 40 320 / 720 = 56 ✓.

:::

```
0) Fonction Arrange (n, p : Entier) : Réel
1) ar ← 1
   Pour i de n à n - p + 1 (pas = -1) Faire
      ar ← ar * i
   Fin Pour
2) Arrange ← ar
3) Fin Arrange
```

```pascal
Function Arrange (n, p : Integer) : Real;
Var i : Integer; ar : Real;
Begin
  ar := 1;
  For i := n Downto n - p + 1 Do ar := ar * i;
  Arrange := ar;
End;
```

La variable `ar` et la fonction sont **réelles** : 13! = 6 227 020 800 dépasse déjà le plus grand `LongInt` (2 147 483 647), et un arrangement grandit très vite. Avec l'`Integer` (16 bits) du manuel, A₈⁸ = 8! = 40 320 déborde déjà.

::: piege
**Erreur : prendre un arrangement pour une combinaison, ou l'inverse.** Pour choisir 3 élèves parmi 5 sans postes, on écrit 5 × 4 × 3 = 60. L'erreur tente parce que le produit est le même. Mais une même équipe de 3 apparaît dans 3! = 6 ordres différents : 60 compte chaque équipe 6 fois. L'arrangement compte des listes ordonnées ; si l'ordre ne compte pas, c'est une combinaison (notion suivante).
:::

::: propriete
Aₙ¹ = n (un seul facteur). Aₙⁿ = n! : c'est le nombre de façons d'ordonner n éléments, donc d'écrire les anagrammes d'un mot dont les n lettres sont toutes différentes. Pour n ≥ 2, Aₙⁿ⁻¹ = Aₙⁿ : Aₙⁿ⁻¹ s'arrête au facteur 2, et le facteur 1 qui lui manque ne change pas le produit.
Cas limite : si une lettre se répète, deux anagrammes peuvent être le même mot, et ce comptage est trop grand.
:::

::: verifie À toi : un arrangement
Combien de façons y a-t-il de classer 1er et 2e parmi 6 coureurs ?

---

L'ordre compte (le 1er n'est pas le 2e) : c'est un arrangement avec n = 6 et p = 2. A₆² = 6 × 5 = 30, car il y a 6 choix pour le 1er et il en reste 5 pour le 2e.
:::

::: retenir
Aₙᵖ = n × (n − 1) × … × (n − p + 1) = n! / (n − p)! compte les p-uplets d'éléments distincts ; la boucle Pour décroissante va de n à n − p + 1 et se programme en Réel.
:::

## 🤝 Les combinaisons Cₙᵖ

Dans le même club de 5 élèves, on forme maintenant une équipe de 3, sans postes : l'ordre ne compte plus. Les 60 listes ordonnées comptent chaque équipe 3! = 6 fois (les 6 ordres possibles des 3 membres).
Combien d'équipes distinctes, et comment le programmer ?

::: definition
Une **combinaison** de p éléments d'un ensemble E de n éléments est une **partie** de E formée de p éléments : l'ordre ne compte pas. Leur nombre se note Cₙᵖ (C(n, p) dans les programmes), avec 0 ≤ p ≤ n.
$$ Cₙᵖ = Aₙᵖ / p! = n! / (p! × (n − p)!) $$
:::

Pour n = 5 et p = 3, le manuel résume les trois dénombrements dans un tableau.

| dénombrement             | l'ordre compte ? | formule       | valeur |
| ------------------------ | ---------------- | ------------- | ------ |
| permutations de 3 objets | oui              | p!            | 6      |
| arrangements A₅³         | oui              | n! / (n − p)! | 60     |
| combinaisons C₅³         | non              | Aₙᵖ / p!      | 10     |

On passe de 60 à 10 en divisant par 6 : on regroupe les 6 ordres d'une même équipe en une seule.

::: exemple Calculer C₅³ de deux façons

1. Par les arrangements : A₅³ = 5 × 4 × 3 = 60, puis on divise par p! = 3! = 6 : 60 / 6 = 10, car chaque équipe est comptée 6 fois.
2. Par les factorielles : 5! / (3! × 2!) = 120 / (6 × 2) = 10 ✓.
3. Il y a donc 10 équipes de 3 élèves parmi 5.

:::

```
0) Fonction Comb (n, p : Entier) : Réel
1) Comb ← Arrange (n, p) / Fact (p)
2) Fin Comb
```

```pascal
Function Fact (p : Integer) : Real;
Var i : Integer; r : Real;
Begin
  r := 1;
  For i := 2 To p Do r := r * i;
  Fact := r;
End;

Function Comb (n, p : Integer) : Real;
Begin
  Comb := Arrange (n, p) / Fact (p);
End;
```

`Fact (p)` rend p! en réel (la factorielle est supposée connue) et `Arrange` est la fonction de la notion précédente.

::: piege
**Erreur : oublier de diviser par p!.** On calcule `Comb ← Arrange (n, p)`, donc 60 pour C₅³ au lieu de 10. L'erreur tente parce que Arrange est déjà écrit et donne un nombre « plausible ». Mais ce nombre compte les listes ordonnées. Il faut diviser par p! pour ne garder qu'une équipe par groupe de p! ordres.
:::

::: propriete
Cₙ⁰ = 1 (une seule partie vide) et Cₙⁿ = 1 (la partie pleine). Cₙ¹ = n.
Cas limite : on étend `Arrange` à p = 0 (hors de son domaine 1 ≤ p ≤ n) ; la boucle ne tourne pas et rend 1, et `Fact (0)` vaut 1 : la formule donne bien Cₙ⁰ = 1.
:::

::: verifie À toi : une combinaison
Combien de comités de 2 personnes peut-on former parmi 6 ?

---

L'ordre ne compte pas : c'est une combinaison, n = 6 et p = 2. On part de A₆² = 6 × 5 = 30 listes ordonnées et on divise par 2! = 2, car chaque comité est compté 2 fois : C₆² = 15 comités.
:::

::: retenir
Cₙᵖ = Aₙᵖ / p! = n! / (p! × (n − p)!) compte les parties de p éléments, sans ordre ; on calcule Arrange (n, p) / Fact (p).
:::

## 🌳 Les combinaisons récursives

Reprenons les équipes de p élèves parmi n, et isolons une élève, Sana. Une équipe ne contient pas Sana : on choisit p élèves parmi les n − 1 autres. Ou elle la contient : il reste p − 1 coéquipiers à choisir parmi les n − 1 autres.
Cela donne-t-il une relation entre Cₙᵖ et des nombres plus petits ?

::: definition
**Relation récursive de Cₙᵖ** :
Si p = 0 ou p = n, alors Cₙᵖ = 1 (cas particulier).
Sinon Cₙᵖ = Cₙ₋₁ᵖ + Cₙ₋₁ᵖ⁻¹ (cas général : sans Sana, puis avec Sana).
:::

::: exemple Évaluer C₄² par la relation

1. p = 2 n'est ni 0 ni 4 : C₄² = C₃² + C₃¹.
2. C₃² = C₂² + C₂¹ = 1 + C₂¹ (car p = n = 2) ; C₂¹ = C₁¹ + C₁⁰ = 1 + 1 = 2. Donc C₃² = 1 + 2 = 3.
3. C₃¹ = C₂¹ + C₂⁰ = 2 + 1 = 3.
4. C₄² = 3 + 3 = 6 ✓, ce que donne aussi 4! / (2! × 2!) = 24 / 4 = 6.

:::

```
0) Fonction Comb (n, p : Entier) : Réel
1) Si (p = 0) ou (p = n) Alors Comb ← 1
   Sinon Comb ← Comb (n - 1, p) + Comb (n - 1, p - 1)
   Fin Si
2) Fin Comb
```

```pascal
Function Comb (n, p : Integer) : Real;
Begin
  If (p = 0) Or (p = n) Then Comb := 1
  Else Comb := Comb (n - 1, p) + Comb (n - 1, p - 1);
End;
```

La fonction n'a aucune multiplication : le résultat n'est qu'une somme de 1 renvoyés par les cas particuliers. C'est la relation du triangle de Pascal, vue au chapitre 04.

::: piege
**Erreur : ne tester que p = 0.** On écrit `Si (p = 0) Alors Comb ← 1 Sinon …`, en pensant que p finit toujours par baisser jusqu'à 0. L'erreur tente parce que p baisse dans le second appel. Mais le premier appel `Comb (n - 1, p)` garde p et fait baisser n : on arrive à n = p, où p ne vaut pas 0, et les appels continuent avec n négatif, sans fin. Le test p = n est indispensable.
:::

::: propriete
Dans le cas général, p n'est ni 0 ni n, donc 1 ≤ p ≤ n − 1. Les deux appels portent sur n − 1 et gardent p ou p − 1 entre 0 et n − 1 : ils restent dans le domaine, et n baisse d'une unité à chaque appel jusqu'à un cas particulier.
Cas limite : un appel avec p > n n'est pas dans le domaine et ne s'arrête jamais.
:::

::: verifie À toi : la relation récursive
Évaluer C₃¹ avec la relation récursive.

---

p = 1 n'est ni 0 ni 3 : C₃¹ = C₂¹ + C₂⁰. Pour le premier terme, C₂¹ = C₁¹ + C₁⁰ = 1 + 1 = 2, car p = n = 1 et p = 0 sont des cas particuliers. Le second terme C₂⁰ vaut 1 (p = 0). Donc C₃¹ = 2 + 1 = 3, comme n = 3 pour Cₙ¹.
:::

::: retenir
Cₙᵖ = 1 si p = 0 ou p = n, sinon Cₙ₋₁ᵖ + Cₙ₋₁ᵖ⁻¹ ; les deux cas d'arrêt sont nécessaires pour que les appels s'arrêtent.
:::

## ➕ Divisibilité par 3 et par 9 : la somme des chiffres

Tu veux savoir si 4 725 se partage en 3 parts égales, sans poser la division. Un nombre de plusieurs chiffres est long à diviser, surtout à la main ou dans un programme.
Existe-t-il un signe qui se lit directement sur les chiffres ?

::: definition
Un entier n est **divisible** par un entier m si le reste de la division euclidienne de n par m est nul. Une **règle de divisibilité** est une suite d'opérations simples qui reconnaît cela sans effectuer la division.
**Par 3** : n est divisible par 3 si la somme de ses chiffres est divisible par 3.
**Par 9** : n est divisible par 9 si la somme de ses chiffres est divisible par 9.
:::

La raison se lit sur l'écriture décimale : 4 725 = 4 × 1 000 + 7 × 100 + 2 × 10 + 5 = 4 × 999 + 7 × 99 + 2 × 9 + (4 + 7 + 2 + 5). Les nombres 999, 99 et 9 sont divisibles par 3 et par 9 : il ne reste que la somme des chiffres 4 + 7 + 2 + 5 à tester.

::: exemple Tester 4 725

1. Somme des chiffres : 4 + 7 + 2 + 5 = 18.
2. 18 = 3 × 6 est divisible par 3 : donc 4 725 est divisible par 3.
3. 18 = 9 × 2 est divisible par 9 : donc 4 725 est aussi divisible par 9.
4. Contrôle : 4 725 = 9 × 525 ✓. Son dernier chiffre est 5, et pourtant il est divisible par 3 : le dernier chiffre ne dit rien ici.

:::

Un nombre peut avoir des dizaines de chiffres : le programme le lit comme une **chaîne** et parcourt ses caractères, `Val` convertissant chaque caractère en nombre (e vaut 0 si la conversion réussit).

```pascal
Function Div_3 (ch : String) : Boolean;
Var i, nb, e, somme : Integer;
Begin
  somme := 0;
  For i := 1 To Length (ch) Do
  Begin
    Val (ch[i], nb, e);
    somme := somme + nb;
  End;
  Div_3 := somme Mod 3 = 0;
End;
```

Pour la divisibilité par 9, seule la dernière ligne change : `somme Mod 9 = 0`.

::: piege
**Erreur : juger la divisibilité par 3 sur le dernier chiffre.** On lit 4 725, on voit 5, et l'on dit « 5 n'est pas multiple de 3, donc non ». L'erreur tente parce que, pour 2 et 5, le dernier chiffre décide. Mais 4 725 = 3 × 1 575. Pour 3 et 9, tous les chiffres comptent : on les additionne.
:::

::: propriete
Tout multiple de 9 est un multiple de 3 (9 = 3 × 3), mais la réciproque est fausse : 543 a pour somme 12, divisible par 3 mais pas par 9, et 543 = 3 × 181 sans être un multiple de 9.
Cas limite : la somme elle-même peut être grande (99 999 a pour somme 45) ; on teste alors cette somme avec `Mod`.
:::

::: verifie À toi : 3 et 9
2 586 est-il divisible par 3 ? par 9 ?

---

La somme des chiffres vaut 2 + 5 + 8 + 6 = 21. 21 = 3 × 7 est divisible par 3 : 2 586 l'est (2 586 = 3 × 862). 21 = 2 × 9 + 3 n'est pas divisible par 9 : 2 586 ne l'est pas.
:::

::: retenir
Un entier est divisible par 3 (resp. par 9) si la somme de ses chiffres l'est ; un multiple de 9 est un multiple de 3, jamais l'inverse.
:::

## 🔚 Divisibilité par 2, 4, 5, 10 et 25 : les derniers chiffres

Dans 36 748, on cherche si le nombre se coupe en 2 parts égales, ou en 4. Cette fois, regarder tous les chiffres paraît inutile : 10 est un multiple de 2, 5 et 10, et 100 est un multiple de 4 et de 25.
Quels chiffres suffisent à décider ?

::: definition
**Par 2** : le chiffre des unités est 0, 2, 4, 6 ou 8.
**Par 5** : le chiffre des unités est 0 ou 5.
**Par 10** : le chiffre des unités est 0.
**Par 4** : le nombre formé par les deux derniers chiffres est divisible par 4.
**Par 25** : le nombre formé par les deux derniers chiffres est divisible par 25 (00, 25, 50 ou 75).
:::

La raison : n = 100 × k + r, où r est le nombre formé par les deux derniers chiffres. 100 × k est divisible par 4 et par 25, donc n l'est exactement quand r l'est. De même, 10 × k + u se décide sur le chiffre des unités u pour 2, 5 et 10.

| nombre | par 2 | par 4    | par 5 | par 10 | par 25   |
| ------ | ----- | -------- | ----- | ------ | -------- |
| 8 350  | oui   | non (50) | oui   | oui    | oui (50) |
| 9 124  | oui   | oui (24) | non   | non    | non      |
| 7 775  | non   | non (75) | oui   | non    | oui (75) |

::: exemple Tester 36 748

1. Par 2 : le chiffre des unités est 8, pair : oui.
2. Par 5 et par 10 : l'unité n'est ni 0 ni 5 : non.
3. Par 4 : les deux derniers chiffres forment 48 = 4 × 12 : oui. Contrôle : 36 748 = 4 × 9 187 ✓.
4. Par 25 : 48 n'est pas 00, 25, 50 ou 75 : non.

:::

```pascal
Function Div_4 (m : LongInt) : Boolean;
Begin
  Div_4 := (m Mod 100) Mod 4 = 0;
End;

Function Div_5 (m : LongInt) : Boolean;
Begin
  Div_5 := (m Mod 10 = 0) Or (m Mod 10 = 5);
End;
```

`m Mod 100` extrait les deux derniers chiffres, `m Mod 10` le dernier. Le manuel écrit aussi `(2 * m) Mod 10 = 0` pour la divisibilité par 5 : c'est un test équivalent.

::: piege
**Erreur : appliquer la règle de 4 au seul dernier chiffre.** On lit 3 112, on voit 2, et l'on dit « 2 n'est pas multiple de 4, donc non ». L'erreur tente parce que, pour 2, 5 et 10, un seul chiffre suffit. Mais 3 112 = 4 × 778. Inversement 3 114 se termine par 4, multiple de 4, et n'est pas divisible par 4 (14 n'est pas multiple de 4).
:::

::: propriete
Les règles de 2, 5 et 10 se lisent sur 1 chiffre ; celles de 4 et 25 sur 2 chiffres. Un nombre est divisible par 6 s'il l'est à la fois par 2 et par 3.
Cas limite : si les deux derniers chiffres sont 00, le nombre est divisible par 4 et par 25 ; si le nombre n'a qu'un chiffre, 8 se lit « 08 » et 8 est multiple de 4.
:::

::: verifie À toi : les derniers chiffres
52 800 est-il divisible par 4 ? par 25 ? par 10 ?

---

Les deux derniers chiffres forment 00, soit 0 = 4 × 0 = 25 × 0 : 52 800 est divisible par 4 et par 25. Son chiffre des unités est 0 : il est divisible par 10 (et par 2 et par 5).
:::

::: retenir
2, 5 et 10 se décident sur le chiffre des unités, 4 et 25 sur les deux derniers chiffres ; 3 et 9 sur la somme de tous les chiffres.
:::

## 🔍 Chercher un chiffre inconnu

Un numéro de ticket est écrit 571u : le dernier chiffre u est effacé, mais on sait que le nombre est divisible par 4. Quelles valeurs de u sont possibles ?
Comment trouver tous les candidats sans les essayer à la main ?

::: methode Chercher les chiffres inconnus

1. Écrire le nombre en fonction du chiffre inconnu, ici n = 5 710 + u.
2. Choisir la règle qui convient et la traduire en condition sur u.
3. Essayer toutes les valeurs de 0 à 9 avec une boucle Pour.
4. Garder, et afficher, celles où la condition est vraie.

:::

::: exemple Trouver u pour 571u divisible par 4

1. Règle de 4 : les deux derniers chiffres 1u, soit 10 + u, doivent être divisibles par 4.
2. Parmi 10, 11, …, 19, les multiples de 4 sont 12 et 16 : donc u = 2 ou u = 6.
3. Contrôle : 5 712 = 4 × 1 428 et 5 716 = 4 × 1 429 ✓.

:::

```pascal
For u := 0 To 9 Do
  If Div_4 (5710 + u) Then WriteLn (u, ' ', 5710 + u);
```

Ce programme affiche `2 5712` puis `6 5716`.

::: piege
**Erreur : tester seulement la divisibilité de u par 4.** On retient u = 0, 4, 8, les multiples de 4. L'erreur tente parce que u est « le dernier chiffre » et que la règle parle des derniers chiffres. Mais la règle de 4 porte sur les **deux** derniers chiffres : u = 4 donne 5 714 = 4 × 1 428 + 2, qui n'est pas divisible par 4.
:::

::: propriete
Avec deux chiffres inconnus c et u, on imbrique deux boucles : 10 × 10 = 100 nombres sont testés. Avec la règle de 3 ou de 9, la condition porte sur la somme c + u + (la somme des chiffres connus).
Cas limite : u est un chiffre, donc u ≤ 9 : jamais 10.
:::

::: verifie À toi : deux chiffres inconnus
n = 62c4u est divisible par 9. Que doit valoir c + u ?

---

La somme des chiffres vaut 6 + 2 + c + 4 + u = 12 + c + u. Comme c + u va de 0 à 18, cette somme va de 12 à 30, et seuls 18 et 27 sont des multiples de 9. Donc c + u = 6 ou c + u = 15 ; on trouve 11 couples (c ; u) en tout : 7 pour la somme 6 et 4 pour la somme 15.
:::

::: retenir
Pour un chiffre inconnu, on écrit le nombre en fonction de u, on traduit la règle en condition, puis on essaie les 10 valeurs de 0 à 9 avec une boucle.
:::

> 🗡️ Devant un nombre à tester, demande-toi d'abord : « quels chiffres la règle regarde-t-elle ? » Le dernier, les deux derniers, ou tous.

> 🏆 Porte franchie ! Tu sais calculer un PGCD, compter des arrangements et des combinaisons, et lire la divisibilité sur les chiffres. Prochaine arène : les conversions entre bases de numération.
