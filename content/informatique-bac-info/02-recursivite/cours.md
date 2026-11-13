# ⚔️ La récursivité — le sous-programme qui s'appelle lui-même

> 💡 «Pour venir à bout d'un grand problème, confie-le à un problème plus petit, jusqu'à ce qu'il tienne dans la main.»

Une boucle répète une action ; un sous-programme récursif la répète en se rappelant lui-même. Ce chapitre apprend à écrire, lire et vérifier de tels sous-programmes, en pseudo-langage algorithmique et en Pascal. Huit notions, avec un fil rouge : la factorielle n! = 1 × 2 × … × n, puis des chaînes et des tableaux.

## 🪆 Un sous-programme qui s'appelle lui-même

Pour calculer 5!, inutile de refaire tout le produit : 5! = 5 × 4!, puis 4! = 4 × 3!, et ainsi de suite jusqu'à 0! = 1. Chaque calcul se ramène au même calcul sur un nombre plus petit.
Un sous-programme peut-il exploiter cette idée en s'appelant lui-même ?

::: definition
Un sous-programme (fonction ou procédure) est **récursif** s'il s'appelle lui-même, directement dans son corps ou à travers d'autres sous-programmes qui le rappellent. Cette méthode s'appelle la **récursivité**. Tout objet défini à partir de lui-même est dit récursif.
**Récursivité directe** : P appelle P.
**Récursivité indirecte** : P appelle P1, qui appelle P2, …, qui finit par rappeler P.
**Récursivité croisée** : plusieurs sous-programmes s'appellent mutuellement.
:::

Voici la factorielle récursive, en algorithme puis en programme Pascal complet.

```
0) Fonction Factorielle (n : Entier non signé) : Entier Long
1) Si (n = 0) Alors Factorielle ← 1
   Sinon Factorielle ← n * Factorielle (n - 1)
   Fin Si
2) Fin Factorielle
```

```pascal
PROGRAM Fact_rec;
Var n : Word;

Function Factorielle (m : Word) : LongInt;
Begin
  If m = 0 Then Factorielle := 1
  Else Factorielle := m * Factorielle (m - 1);
End;

BEGIN
  Write ('n = '); ReadLn (n);
  WriteLn ('n! = ', Factorielle (n));
END.
```

L'appel `Factorielle (m - 1)`, écrit dans le corps de `Factorielle`, est ce qui la rend récursive. Pour reconnaître les types, voici deux fonctions `Pair` et `Impair` (valables pour n ≥ 0), et un couple `Carre` / `Cube` où `Carre (x)` rend x * x et `Cube (x)` rend x * `Carre (x)`.

```
0) Fonction Pair (n : Entier non signé) : Booléen
1) Si n = 0 Alors Pair ← Vrai
   Sinon Pair ← Impair (n - 1)
   Fin Si
2) Fin Pair

0) Fonction Impair (n : Entier non signé) : Booléen
1) Si n = 0 Alors Impair ← Faux
   Sinon Impair ← Pair (n - 1)
   Fin Si
2) Fin Impair
```

::: exemple Reconnaître le type de récursivité

1. `Factorielle` contient l'appel `Factorielle (n - 1)` dans son propre corps : récursivité directe.
2. `Pair` appelle `Impair`, qui rappelle `Pair` : la chaîne d'appels revient à son point de départ, donc récursivité indirecte ; comme les deux fonctions s'appellent mutuellement, elle est aussi croisée.
3. `Cube` appelle `Carre`, mais `Carre` n'appelle ni `Cube` ni `Carre` : la chaîne ne revient jamais à `Cube`, donc aucun des deux n'est récursif.

:::

::: piege
**Erreur : prendre tout sous-programme qui en appelle un autre pour un sous-programme récursif.** On lit « `Cube` appelle `Carre` » et l'on écrit « `Cube` est récursif ». L'erreur tente parce qu'un appel dans le corps ressemble à l'appel récursif. Mais la récursivité exige que la chaîne d'appels revienne au sous-programme de départ : `Cube` appelle `Carre`, qui s'arrête là. Seul `Carre` appelé depuis `Carre`, ou un cycle comme `Pair` → `Impair` → `Pair`, est récursif.
:::

::: verifie À toi : trouver le type
Un sous-programme A appelle B, B appelle C, et C appelle A. Quel est le type de récursivité, et A est-il récursif ?

---

La chaîne A → B → C → A revient à A : A est récursif, bien qu'il ne s'appelle pas lui-même dans son corps, puisque ses appels finissent par le rappeler. Comme P appelle P1 qui appelle P2 qui rappelle P, c'est la récursivité indirecte ; les trois sous-programmes s'appellent en cycle, on parle aussi de récursivité croisée.
:::

::: retenir
Un sous-programme est récursif s'il s'appelle lui-même, directement dans son corps ou à travers d'autres sous-programmes qui finissent par le rappeler.
:::

## 🧩 Cas particulier, cas général : l'analyse par cas

On veut la somme S(m) = 1 + 2 + … + m. On sait que S(4) = 10 et S(3) = 6, donc S(4) = 4 + S(3). La même idée vaut pour tout m, sauf pour le plus petit.
Comment écrire S(m) pour tous les m sans jamais réécrire la somme entière ?

::: definition
Un module récursif se construit par une **analyse par cas**.
**Cas particulier** : un cas assez simple pour être résolu directement, sans appel récursif ; c'est la **condition d'arrêt**.
**Cas général** : un cas où le problème se ramène au même problème, en plus petit, par un **appel récursif**.
La **structure conditionnelle** (Si … Sinon) est donc obligatoire : elle choisit entre les deux.
:::

```
0) Fonction Somme (m : Entier non signé) : Entier Long
1) Si (m = 0) Alors Somme ← 0
   Sinon Somme ← m + Somme (m - 1)
   Fin Si
2) Fin Somme
```

```pascal
Function Somme (m : Word) : LongInt;
Begin
  If m = 0 Then Somme := 0
  Else Somme := m + Somme (m - 1);
End;
```

::: exemple Écrire Somme par cas

1. Cas particulier : pour m = 0, la somme est vide et vaut 0. C'est le plus petit problème, résolu sans appel.
2. Cas général : pour m ≥ 1, S(m) = m + S(m − 1), car S(m − 1) est la même somme sans son dernier terme m.
3. On assemble les deux dans un `Si … Sinon` : la condition `m = 0` choisit le cas particulier, tout autre m prend le cas général.
4. Contrôle : Somme (3) = 3 + Somme (2) = 3 + 2 + Somme (1) = 3 + 2 + 1 + Somme (0) = 3 + 2 + 1 + 0 = 6 ✓.

:::

::: piege
**Erreur : donner au cas particulier la valeur d'une autre fonction.** On écrit `Si m = 0 Alors Somme ← 1`, par habitude de `Factorielle (0) = 1`. L'erreur tente parce que la forme du code est identique. Mais Somme (3) vaut alors 3 + 2 + 1 + 1 = 7 au lieu de 6 : tous les résultats sont décalés de 1. La valeur du cas particulier est le résultat correct du plus petit problème : 0 pour une somme, 1 pour un produit.
:::

::: propriete
Un module récursif contient **au moins un cas particulier** et **au moins un cas général**. Il peut en contenir plusieurs de chaque.
Cas limite : `Palindrome` a deux cas particuliers (chaîne de moins de 2 caractères, extrémités différentes) et `Puissance` a deux cas généraux (exposant négatif, exposant positif).
:::

::: verifie À toi : l'analyse par cas
Donner l'analyse par cas de la somme des carrés SC(m) = 1² + 2² + … + m².

---

Cas particulier : m = 0, la somme est vide et SC(0) = 0. Cas général : pour m ≥ 1, SC(m) = m² + SC(m − 1), car SC(m − 1) est la même somme privée de son dernier terme m². Le cas particulier vaut 0 parce que c'est la valeur d'une somme vide.
:::

::: retenir
Un module récursif se décompose en un cas particulier (condition d'arrêt, résolu directement) et un cas général (appel récursif sur un problème plus petit), choisis par un Si … Sinon.
:::

## 🎯 La convergence : atteindre l'arrêt

On teste `Factorielle` avec un paramètre déclaré `Integer` (entier signé) au lieu de `Word`, et quelqu'un tape n = −1. Les appels reçoivent −1, puis −2, puis −3, … : le paramètre s'éloigne de 0, la condition `m = 0` n'est jamais vraie, et le programme s'effondre sur un débordement de pile.
Qu'est-ce qui garantit que la condition d'arrêt finira par être atteinte ?

::: definition
Un appel récursif **converge** quand, d'un appel au suivant, les arguments se rapprochent d'une condition d'arrêt : la taille du problème diminue à chaque appel. Sans convergence, la suite des appels ne se termine pas.
:::

Pour `Somme`, l'argument vaut m, m − 1, m − 2, …

::: exemple Suivre les arguments de Somme

1. Pour m = 3, les arguments successifs sont 3, 2, 1, 0 : chaque appel diminue m de 1.
2. Un entier naturel qui diminue de 1 à chaque pas atteint 0 en m pas exactement : il ne peut pas sauter par-dessus.
3. L'appel de `Somme (0)` déclenche le cas particulier et la suite d'appels s'arrête : `Somme` converge pour tout m ≥ 0.

:::

```
0) Fonction Prod2 (n : Entier) : Entier Long
1) Si (n = 0) Alors Prod2 ← 1
   Sinon Prod2 ← n * Prod2 (n - 2)
   Fin Si
2) Fin Prod2
```

::: piege
**Erreur : valider une fonction récursive avec une seule valeur.** On teste `Prod2 (4)` : les arguments 4, 2, 0 atteignent l'arrêt et le résultat 4 × 2 × 1 = 8 est juste, donc on conclut « la fonction marche ». L'erreur tente parce qu'un test réussi paraît une preuve. Mais pour `Prod2 (5)`, les arguments 5, 3, 1, −1, −3, … sautent par-dessus 0 : l'arrêt n'arrive jamais. Une condition `n = 0` ne rattrape que les valeurs paires.
:::

::: propriete
Pour prouver la terminaison, on montre que l'argument décroît strictement vers la condition d'arrêt **et** que cette condition attrape tous les arguments atteignables. Une inégalité est souvent plus sûre qu'une égalité : avec `Si n ≤ 1 Alors Prod2 ← 1`, les appels `Prod2 (4)` et `Prod2 (5)` s'arrêtent (8 et 15).
Cas limite : `Puissance (a, n)` avec n < 0 converge parce que son premier appel change le signe : `Puissance (a, -3)` appelle `Puissance (a, 3)`, dont l'exposant décroît ensuite vers 0.
:::

::: verifie À toi : la condition est-elle atteinte ?
`F (n)` vaut 0 si n = 1, et 1 + F (n Div 2) sinon. Pour quels n ≥ 0 l'appel s'arrête-t-il ?

---

Pour n ≥ 1, les arguments n, n Div 2, … diminuent jusqu'à 1 (par exemple 5, 2, 1) et l'arrêt est atteint. Pour n = 0, 0 Div 2 vaut 0 : les arguments restent à 0 et ne valent jamais 1, donc l'appel ne s'arrête pas. La correction est `Si n ≤ 1 Alors F ← 0`, qui attrape aussi 0.
:::

::: retenir
Chaque appel récursif doit rapprocher les arguments d'une condition d'arrêt qui les attrape tous, sinon l'exécution est infinie.
:::

## 🔍 La trace d'exécution

Que renvoie `Factorielle (4)`, et dans quel ordre se font les multiplications ? Le résultat n'est connu qu'à la fin, alors que le premier appel est le premier lancé.
Comment suivre une exécution récursive sans s'y perdre ?

::: definition
La **trace d'exécution** d'un appel récursif liste les appels dans l'ordre : la **descente** (chaque appel lance le suivant, jusqu'au cas particulier), puis la **remontée** (chaque appel reçoit la valeur de celui qu'il a lancé et rend la sienne).
:::

| Appel           | Paramètre m | Calcul en attente       | Valeur rendue |
| --------------- | ----------- | ----------------------- | ------------- |
| Factorielle (4) | 4           | 4 × Factorielle (3)     | 24            |
| Factorielle (3) | 3           | 3 × Factorielle (2)     | 6             |
| Factorielle (2) | 2           | 2 × Factorielle (1)     | 2             |
| Factorielle (1) | 1           | 1 × Factorielle (0)     | 1             |
| Factorielle (0) | 0           | aucun (cas particulier) | 1             |

La descente se lit de haut en bas (m = 4, 3, 2, 1, 0) ; la remontée de bas en haut (1, 1, 2, 6, 24) : les multiplications s'effectuent au retour.

Pour le second exemple, voici `Puissance` : aⁿ pour un réel a et un entier n, négatif ou non (avec a ≠ 0 si n < 0).

```
0) Fonction Puissance (a : Réel ; n : Entier) : Réel
1) Si n = 0 Alors Puissance ← 1
   Sinon Si n < 0 Alors Puissance ← 1 / Puissance (a, -n)
         Sinon Puissance ← a * Puissance (a, n - 1)
   Fin Si
2) Fin Puissance
```

```pascal
Function Puissance (a : Real; n : Integer) : Real;
Begin
  If n = 0 Then Puissance := 1
  Else If n < 0 Then Puissance := 1 / Puissance (a, -n)
  Else Puissance := a * Puissance (a, n - 1);
End;
```

::: exemple Tracer Factorielle (4)

1. Descente : `Factorielle (4)` appelle `Factorielle (3)`, puis (2), puis (1), puis (0). Aucune multiplication n'est encore faite, car chaque produit attend la valeur de l'appel suivant.
2. Cas particulier : `Factorielle (0)` rend 1 sans appeler personne.
3. Remontée : `Factorielle (1)` calcule 1 × 1 = 1, `Factorielle (2)` calcule 2 × 1 = 2, `Factorielle (3)` calcule 3 × 2 = 6, `Factorielle (4)` calcule 4 × 6 = 24.
4. Le résultat final est 24 ✓, après 5 appels (m = 4, 3, 2, 1, 0).

:::

::: exemple Tracer Puissance (2, −3)

1. Le cas n < 0 s'applique : `Puissance (2, -3)` = 1 / `Puissance (2, 3)`, avec l'exposant changé de signe.
2. Descente : `Puissance (2, 3)` = 2 × `Puissance (2, 2)` = 2 × 2 × `Puissance (2, 1)` = 2 × 2 × 2 × `Puissance (2, 0)`.
3. Cas particulier : `Puissance (2, 0)` rend 1, donc `Puissance (2, 3)` = 2 × 2 × 2 × 1 = 8.
4. `Puissance (2, -3)` = 1 / 8 = 0,125 ✓, après 5 appels (exposants −3, 3, 2, 1, 0).

:::

::: piege
**Erreur : compter n appels pour `Factorielle (n)`.** On écrit « `Factorielle (4)` fait 4 appels ». L'erreur tente parce que le paramètre part de 4 et que l'on oublie le dernier. Mais le cas particulier est lui aussi un appel : m = 4, 3, 2, 1, 0 fait 5 appels. Pour n = 0, il y a un seul appel et aucun appel récursif.
:::

::: verifie À toi : tracer Somme (4)
Que renvoie `Somme (4)`, et combien d'appels sont lancés ?

---

Descente : `Somme (4)` appelle (3), puis (2), puis (1), puis (0), soit 5 appels. Cas particulier : `Somme (0)` rend 0. Remontée : 1 + 0 = 1, 2 + 1 = 3, 3 + 3 = 6, 4 + 6 = 10. Les additions se font au retour, et `Somme (4)` rend 10.
:::

::: retenir
Une trace se lit en deux temps : la descente jusqu'au cas particulier, puis la remontée où les calculs en attente s'effectuent ; `Factorielle (n)` lance n + 1 appels.
:::

## 📚 La pile : où attendent les appels

Dans `Factorielle (4)`, le produit 4 × … attend la valeur de `Factorielle (3)`, qui attend celle de `Factorielle (2)`, et ainsi de suite. Chaque appel en attente possède son propre m : 4, 3, 2, 1, puis 0.
Où l'ordinateur garde-t-il toutes ces valeurs de m en même temps ?

::: definition
La **pile** est la zone mémoire où chaque appel dépose ses données (paramètres, variables locales) : à chaque appel, une valeur différente du même paramètre formel est **empilée** ; quand l'appel se termine, ses données sont **dépilées**. Si les appels en attente sont trop nombreux, la pile **déborde** : c'est le débordement de pile.
:::

| Étape | Pile (du plus ancien au plus récent) | Événement                                |
| ----- | ------------------------------------ | ---------------------------------------- |
| 1     | m = 2                                | appel de Somme (2)                       |
| 2     | m = 2, m = 1                         | appel de Somme (1)                       |
| 3     | m = 2, m = 1, m = 0                  | appel de Somme (0) : profondeur maximale |
| 4     | m = 2, m = 1                         | Somme (0) rend 0 et est dépilé           |
| 5     | m = 2                                | Somme (1) rend 1 + 0 = 1 et est dépilé   |
| 6     | vide                                 | Somme (2) rend 2 + 1 = 3 et est dépilé   |

Le tableau suit les mêmes appels que la trace : chaque ligne de la pile est un appel en attente avec son propre m.

::: exemple Suivre la pile de Somme (2)

1. Étapes 1 à 3 : chaque appel empile un nouveau m ; la pile atteint 3 appels (m = 2, 1, 0), c'est la profondeur maximale.
2. Étape 4 : `Somme (0)` est le cas particulier, il rend 0 sans empiler d'autre appel, puis son m = 0 est dépilé.
3. Étape 5 : `Somme (1)` retrouve son propre m = 1 (et non 0), calcule 1 + 0 = 1, puis est dépilé.
4. Étape 6 : `Somme (2)` retrouve m = 2, calcule 2 + 1 = 3 ; la pile est vide et le résultat est 3 ✓.

:::

::: piege
**Erreur : croire que le nouvel appel écrase le paramètre de l'appelant.** On pense qu'après le retour de `Somme (m - 1)`, le m de l'appelant vaut la dernière valeur vue, 0. L'erreur tente parce qu'il n'y a qu'un nom, m, dans le code. Mais chaque appel a son propre m dans la pile : au retour, l'appelant retrouve la valeur qu'il avait avant l'appel (2 pour `Somme (2)`) et calcule 2 + 1.
:::

::: propriete
**Avantage** : un algorithme récursif est généralement plus simple, plus lisible et plus naturel, car il suit la définition du problème.
**Limite** : la mémoire de la pile. `Somme (n)` empile n + 1 appels en même temps ; si ce nombre devient grand, ou sans fin, la pile déborde.
Cas limite : une récursivité sans cas d'arrêt atteint ne tourne pas indéfiniment en silence : la pile se remplit et le programme s'arrête en erreur.
:::

::: verifie À toi : la profondeur de la pile
Combien d'appels de `Factorielle` sont en attente en même temps, au plus, pour `Factorielle (6)` ?

---

Les paramètres successifs sont 6, 5, 4, 3, 2, 1, 0 : au moment du cas particulier, aucun appel n'est encore terminé, donc les 7 appels sont empilés ensemble. La profondeur maximale est 7, soit n + 1 avec n = 6.
:::

::: retenir
Chaque appel empile sa propre valeur du paramètre ; la récursivité est lisible mais limitée par la pile, qui déborde si les appels en attente sont trop nombreux.
:::

## 🔤 La récursivité sur les chaînes

« radar » se lit pareil dans les deux sens. Pour le vérifier sans boucle, on compare la première et la dernière lettre : si elles sont égales, il reste à vérifier « ada », puis « d ».
Comment réduire une chaîne à une chaîne plus courte, jusqu'à un cas trivial ?

::: definition
Un **palindrome** est un mot qui se lit de la même façon dans les deux sens. Relation récursive : une chaîne de moins de 2 caractères est un palindrome ; sinon elle l'est si ses extrémités sont égales **et** si la chaîne privée de son premier et de son dernier caractère l'est aussi.
`Copy (ch, p, k)` (algorithme : `Sous_chaîne`) extrait `k` caractères de `ch` à partir de la position `p` ; `Length (ch)` (algorithme : `Long`) donne la longueur.
:::

```
0) Fonction Palindrome (ch : Chaîne) : Booléen
1) Si Long (ch) < 2 Alors Palindrome ← Vrai
   Sinon Si ch[1] = ch[Long (ch)]
         Alors Palindrome ← Palindrome (Sous_chaîne (ch, 2, Long (ch) - 2))
         Sinon Palindrome ← Faux
   Fin Si
2) Fin Palindrome
```

```pascal
PROGRAM Palindrome_rec;
Var ch : String;

Function Palindrome (ch : String) : Boolean;
Begin
  If Length (ch) < 2 Then Palindrome := True
  Else If ch[1] = ch[Length (ch)]
       Then Palindrome := Palindrome (Copy (ch, 2, Length (ch) - 2))
       Else Palindrome := False;
End;

BEGIN
  Write ('ch = '); ReadLn (ch);
  If Palindrome (ch) Then WriteLn (ch, ' est un palindrome.')
  Else WriteLn (ch, ' n''est pas un palindrome.');
END.
```

```pascal
Function Inverse (ch : String) : String;
Begin
  If ch = '' Then Inverse := ''
  Else Inverse := ch[Length (ch)] + Inverse (Copy (ch, 1, Length (ch) - 1));
End;
```

::: exemple Palindrome et inversion

1. `Palindrome ('abba')` : extrémités 'a' et 'a' égales, donc on rappelle sur `Copy ('abba', 2, 2)` = 'bb'.
2. `Palindrome ('bb')` : extrémités égales, on rappelle sur `Copy ('bb', 2, 0)` = '' (chaîne vide).
3. `Palindrome ('')` : la longueur 0 est inférieure à 2, cas particulier : Vrai. Le résultat remonte : 'abba' est un palindrome ✓.
4. `Inverse ('abc')` rend 'c' + `Inverse ('ab')` = 'c' + 'b' + `Inverse ('a')` = 'c' + 'b' + 'a' + `Inverse ('')` = 'cba' ✓ : ici on retire un seul caractère, le dernier, à chaque appel.

:::

::: piege
**Erreur : retirer un seul caractère dans `Palindrome`.** On écrit `Copy (ch, 2, Length (ch) - 1)`, qui garde tout sauf le premier caractère. L'erreur tente parce que `Inverse` retire bien un seul caractère par appel. Mais `Palindrome` doit ôter les deux extrémités : pour 'radar', on obtient 'adar', dont les extrémités 'a' et 'r' diffèrent, et la fonction répond Faux à tort. Le nombre à copier est `Length (ch) - 2`.
:::

::: propriete
Sur une chaîne, le cas particulier est la chaîne vide ou d'un seul caractère ; le cas général rapproche de lui en retirant un caractère (`Inverse`) ou deux (`Palindrome`) avec `Copy`.
Cas limite : le test est `Length (ch) < 2` et non `= 1`. Pour 'aa', `Copy ('aa', 2, 0)` donne la chaîne vide, de longueur 0 : avec `= 1`, l'appel sur la chaîne vide lirait ch[1], qui n'existe pas : résultat imprévisible (Faux à tort, ou appels sans fin).
:::

::: verifie À toi : tracer Palindrome
Que renvoie `Palindrome ('abca')` ?

---

Les extrémités 'a' et 'a' sont égales, donc on rappelle sur `Copy ('abca', 2, 2)` = 'bc'. Dans 'bc', les extrémités 'b' et 'c' diffèrent : cas particulier Faux. Le résultat remonte tel quel : `Palindrome ('abca')` rend Faux.
:::

::: retenir
Sur une chaîne, on réduit le problème en retirant des caractères avec `Copy` ; `Palindrome` a deux cas d'arrêt (moins de 2 caractères, extrémités différentes).
:::

## 📊 La récursivité sur les tableaux

Pour trier cinq notes par ordre décroissant, on place la plus grande en tête ; il reste alors à trier quatre notes : le même problème, plus petit. Pour chercher un numéro dans un annuaire trié, on ouvre au milieu et on ne garde que la moitié utile.
Comment un sous-programme travaille-t-il sur une partie d'un tableau ?

::: definition
Sur un tableau T, le problème réduit est un **sous-tableau** T[deb..fin] dont la taille fin − deb + 1 diminue à chaque appel.
**Tri par sélection récursif** (le manuel nomme `Max` et `Permuter` les sous-programmes que l'on appelle ici `Pos_Max` et l'échange en ligne) : on place le maximum de T[deb..fin] en position deb, puis on trie T[deb+1..fin].
**Recherche dichotomique récursive** (tableau trié croissant) : on compare m à T[milieu], avec milieu = (deb + fin) Div 2.
:::

```pascal
Type Tab = Array [1..7] Of Integer;

Function Pos_Max (deb, fin : Integer; T : Tab) : Integer;
Var i, M : Integer;
Begin
  M := deb;
  For i := deb + 1 To fin Do If T[i] > T[M] Then M := i;
  Pos_Max := M;
End;

Procedure Tri_Sel_Rec (deb, fin : Integer; Var T : Tab);
Var M, aux : Integer;
Begin
  If deb < fin Then Begin
    M := Pos_Max (deb, fin, T);
    aux := T[deb]; T[deb] := T[M]; T[M] := aux;
    Tri_Sel_Rec (deb + 1, fin, T);
  End;
End;
```

```pascal
Function Dichotomique (deb, fin, m : Integer; T : Tab) : Boolean;
Var milieu : Integer;
Begin
  milieu := (deb + fin) Div 2;
  If m = T[milieu] Then Dichotomique := True
  Else If (m < T[milieu]) And (deb < milieu)
       Then Dichotomique := Dichotomique (deb, milieu - 1, m, T)
  Else If (m > T[milieu]) And (fin > milieu)
       Then Dichotomique := Dichotomique (milieu + 1, fin, m, T)
  Else Dichotomique := False;
End;
```

::: exemple Tri et dichotomie sur de petits tableaux

1. Tri de [3, 8, 1, 9, 5] par `Tri_Sel_Rec (1, 5, T)` : `Pos_Max (1, 5, T)` rend 4, car 9 est le maximum ; on échange T[1] et T[4] ([9, 8, 1, 3, 5]), puis on trie T[2..5] : 8 est déjà en place, 5 passe en T[3], et les appels suivants donnent [9, 8, 5, 3, 1]. À l'appel (5, 5), deb < fin est faux : un seul élément reste, déjà à sa place.
2. Recherche dans [2, 5, 8, 12, 16, 23, 38] : pour 23, `Dichotomique (1, 7, 23, T)` donne milieu = 4 et T[4] = 12 ; 23 > 12 et fin > milieu, donc appel sur (5, 7), où milieu = 6 et T[6] = 23 : Vrai. Pour 7 : milieu = 4, appel sur (1, 3), milieu = 2, T[2] = 5, appel sur (3, 3), milieu = 3, T[3] = 8 : ni 7 < 8 avec deb < milieu, ni 7 > 8, donc Faux.

:::

::: piege
**Erreur : arrêter le tri par un test d'égalité mal choisi.** On écrit « appeler `Tri_Sel_Rec (deb + 1, fin, T)` si `deb + 1 <> fin` ». L'erreur tente parce que, sur cinq éléments, les appels s'arrêtent bien en (4, 5). Mais pour un tableau d'un seul élément (deb = fin = 1), deb + 1 = 2 est différent de 1 : l'appel part sur (2, 1), puis (3, 1), et ne s'arrête jamais. Le test `deb < fin` attrape aussi un sous-tableau vide ou à un élément.
:::

::: propriete
Dans les deux algorithmes, la taille du sous-tableau diminue à chaque appel, et le cas particulier traite un sous-tableau sans travail utile (tri) ou le cas trouvé ou absent (dichotomie). La recherche dichotomique suppose le tableau **trié croissant** et un sous-tableau non vide au premier appel (deb ≤ fin).
Cas limite : quand le sous-tableau n'a qu'un élément (deb = fin), milieu = deb ; si m n'est pas T[deb], aucune des deux gardes `deb < milieu` ou `fin > milieu` n'est vraie, et la réponse est Faux.
:::

::: verifie À toi : une dichotomie
Avec T = [2, 5, 8, 12, 16, 23, 38], que renvoie `Dichotomique (1, 7, 38, T)` ?

---

milieu = (1 + 7) Div 2 = 4 et T[4] = 12. Comme 38 > 12 et fin = 7 > 4, on rappelle sur (5, 7) : milieu = 6, T[6] = 23, et 38 > 23 avec 7 > 6, donc appel sur (7, 7). milieu = 7, T[7] = 38 = m : Vrai.
:::

::: retenir
Sur un tableau, un appel traite un sous-tableau T[deb..fin] plus petit que le précédent ; le tri par sélection s'arrête quand deb < fin est faux, la dichotomie exige un tableau trié.
:::

## 🔁 Itératif ou récursif : traduire et corriger

La somme 1 + 2 + … + m peut se calculer par une boucle qui accumule, ou par un `Somme` qui se rappelle. Les deux donnent le même résultat, mais ne pensent pas de la même façon.
Comment passer de l'une à l'autre, et comment repérer l'erreur dans un sous-programme récursif ?

::: definition
Le **procédé itératif** répète une action avec une boucle ; le **procédé récursif** la répète par auto-appel. Le passage du mode récursif au mode itératif s'appelle la **dérécursification**.
:::

```pascal
Function Somme_It (m : Word) : LongInt;
Var i : Word; S : LongInt;
Begin
  S := 0;
  For i := 1 To m Do S := S + i;
  Somme_It := S;
End;
```

| Récursif (`Somme`)              | Itératif (`Somme_It`)        |
| ------------------------------- | ---------------------------- |
| cas particulier : m = 0 rend 0  | initialisation : S := 0      |
| cas général : m + Somme (m - 1) | corps de boucle : S := S + i |
| le paramètre m décroît vers 0   | le compteur i croît de 1 à m |

Le même passage vaut pour `Factorielle` : l'initialisation `F := 1` reprend le cas particulier 0! = 1, et la boucle `For i := 2 To n Do F := F * i` reprend le cas général.

Pour traduire un algorithme en Pascal : `Fonction F ← valeur` devient `F := valeur`, `Si … Alors … Sinon` devient `If … Then … Else`, `≠` devient `<>`, `Et` devient `And`, `Long` devient `Length` et `Sous_chaîne` devient `Copy`.

```pascal
Function Pair (N : Integer) : Boolean;
Begin
  If N = 0 Then Pair := True
  Else If N = 1 Then Pair := False
  Else Pair := Pair (N - 1);
End;
```

::: exemple Trouver l'erreur dans Pair

1. On teste les cas d'arrêt : `Pair (0)` rend Vrai et `Pair (1)` rend Faux, ce qui est juste.
2. On teste un cas général : `Pair (2)` appelle `Pair (1)` et rend Faux, alors que 2 est pair. La fonction est fausse.
3. La cause est la relation de récurrence : `Pair (N - 1)` recopie la réponse du nombre précédent, alors que la parité change à chaque pas. Pour tout N ≥ 1, la fonction rend Faux.
4. Correction : un nombre a la même parité que N − 2, donc `Pair := Pair (N - 2)` (pour N ≥ 0). Alors `Pair (2)` = `Pair (0)` = Vrai ✓ et `Pair (3)` = `Pair (1)` = Faux ✓.

:::

::: piege
**Erreur : juger une fonction récursive sur ses seuls cas d'arrêt.** On voit que `Pair (0)` et `Pair (1)` sont justes et l'on déclare la fonction correcte. L'erreur tente parce que le cas particulier est la partie facile à lire. Mais le cas général peut être faux alors que les arrêts sont justes : `Pair (2)` le montre. Il faut tester au moins un appel qui passe par le cas général, et suivre sa trace.
:::

::: propriete
Pour détecter une erreur dans un sous-programme récursif, on vérifie dans l'ordre : le cas particulier est correct et couvre tous les cas atteints ; la relation de récurrence est correcte ; l'argument converge. Une récursivité croisée suit la même grille pour chacun des sous-programmes.
Cas limite : même corrigée, `Pair (N - 2)` suppose N ≥ 0 ; pour N = −1, les arguments −1, −3, −5, … s'éloignent de 0 et de 1, et l'appel ne s'arrête pas.
:::

::: verifie À toi : une récursivité croisée
`Pair (n)` vaut Vrai si n = 0, sinon `Impair (n - 1)`. `Impair (n)` vaut Vrai si n = 1, sinon `Pair (n - 1)`. L'appel `Impair (2)` s'arrête-t-il ?

---

`Impair (2)` : n n'est pas 1, donc appel de `Pair (1)`, puis `Impair (0)`. Là encore n n'est pas 1 : appel de `Pair (-1)`, puis `Impair (-2)`, et les arguments s'éloignent de 0 sans jamais valoir 1 : l'appel ne s'arrête pas. Il manque le cas d'arrêt `Si n = 0 Alors Impair ← Faux`.
:::

::: retenir
Un module récursif se traduit en Pascal ligne à ligne ; pour le corriger, on vérifie le cas particulier, la relation de récurrence et la convergence, sans se fier aux seuls cas d'arrêt.
:::

> 🗡️ Tout module récursif se relit avec la même question : « quel est mon cas d'arrêt, et mes arguments s'en rapprochent-ils ? »

> 🏆 Porte franchie ! Tu sais lire, tracer et corriger un sous-programme qui s'appelle lui-même. Prochaine arène : les algorithmes de tri, où la récursivité reviendra en renfort.
