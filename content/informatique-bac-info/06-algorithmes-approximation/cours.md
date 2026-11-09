# ⚔️ Les algorithmes d'approximation — s'approcher d'une valeur sans jamais l'atteindre

> 💡 «Toute science exacte est dominée par la notion d'approximation.» (Bertrand Russell)

Certains nombres n'ont pas d'écriture finie : π, e, la solution de sin(x) = 1 − x, l'aire sous une courbe sans primitive connue. Un **algorithme d'approximation** en calcule une valeur approchée en un temps raisonnable, en répétant un calcul jusqu'à ce que le résultat ne bouge presque plus. Ce chapitre apprend huit notions : le point fixe, le schéma d'arrêt avec Epsilon, π par Euler, π par Wallis, les séries alternées, e par les factorielles, l'aire par les rectangles et par les trapèzes.

## 🎯 Le point fixe d'une fonction

Pour résoudre sin(x) = 1 − x, on ne sait pas isoler x. Mais avec f(x) = 1 − sin(x), l'équation devient f(x) = x : on cherche un nombre que f laisse en place.
Comment le trouver par le calcul ?

::: definition
Un **point fixe** de f est un nombre x tel que f(x) = x.
On choisit un départ arbitraire U0, puis on calcule U(n+1) = f(U(n)). Si cette suite converge, c'est nécessairement vers un point fixe de f. On s'arrête quand deux termes consécutifs xpre et xact diffèrent de moins de Epsilon, en comptant les itérations dans i.
:::

```pascal
Const Epsilon = 1E-5;
Var xact, xpre : Real; i : Word;

Function f (x : Real) : Real;
Begin
  f := 1 - Sin (x);
End;

BEGIN
  xact := 1; i := 0;
  Repeat
    xpre := xact; xact := f (xact); i := i + 1;
  Until Abs (xact - xpre) < Epsilon;
  WriteLn ('Point fixe : ', xact:10:6, ' après ', i, ' itérations');
END.
```

::: exemple Un point fixe à la main
Soit f(x) = 1 + x/2, avec U0 = 1.

1. U1 = 1 + 1/2 = 1,5, puis U2 = 1,75, U3 = 1,875 et U4 = 1,9375.
2. Les écarts valent 0,5 puis 0,25, 0,125 et 0,0625 : ils diminuent de moitié, la suite se rapproche de 2.
3. Vérification : f(2) = 1 + 1 = 2, donc 2 est bien un point fixe ✓.

Pour sin(x) = 1 − x, le programme ci-dessus affiche 0,510969 après 83 itérations.
:::

::: piege
**Erreur : chercher les zéros de f au lieu de f(x) = x.** Pour f(x) = 1 + x/2, on résout f(x) = 0 et l'on trouve −2. L'erreur tente parce que « résoudre » évoque « égal à zéro ». Mais un point fixe vérifie f(x) = x : f(−2) = 0 et non −2, alors que f(2) = 2.
:::

::: propriete
Si la suite converge, sa limite est un point fixe, mais rien ne garantit qu'elle converge.
Cas limite : f(x) = 2x − 1 a pour point fixe 1. Depuis U0 = 2, on obtient 3, 5, 9, … : les écarts 1, 2, 4, … grandissent et la boucle ne s'arrête pas. Depuis U0 = 1, f(1) = 1 et la boucle s'arrête dès la première passe.
:::

::: verifie À toi : un point fixe
Trouver le point fixe de f(x) = 4 − x/3, puis calculer U1 et U2 depuis U0 = 0.

---

Le point fixe vérifie x = 4 − x/3, donc 4x/3 = 4 et x = 3. Ensuite U1 = 4 − 0 = 4 et U2 = 4 − 4/3 = 8/3 ≈ 2,667 : la suite oscille autour de 3 en s'en approchant.
:::

::: retenir
Un point fixe vérifie f(x) = x ; on l'approche par U(n+1) = f(U(n)) en s'arrêtant quand deux termes consécutifs sont proches, si la suite converge.
:::

## 🧮 Le schéma d'arrêt : deux termes consécutifs et Epsilon

Tous les programmes de ce chapitre calculent un terme après l'autre et s'arrêtent quand ils ne bougent presque plus : l'écart entre deux termes consécutifs a déjà servi au chapitre 4, ici on retient le rôle d'Epsilon et ses écritures en Pascal.
Comment écrire ce schéma, et quelle valeur donner à Epsilon ?

::: definition
**Epsilon** est l'erreur tolérée : le seuil sous lequel deux termes consécutifs sont jugés égaux. On le déclare en constante.
Schéma : initialiser le premier terme ; **Répéter** (garder l'ancien terme dans S1, calculer le nouveau dans S2) **Jusqu'à** écart < Epsilon.
En Pascal, `1E-4` vaut 1 × 10⁻⁴, mais `10E-4` vaut 10 × 10⁻⁴ = 10⁻³ : le chiffre avant le E est un multiplicateur.
:::

```pascal
Const Epsilon = 1E-1;
Var S1, S2, T : Real;
BEGIN
  S2 := 1; T := 1;
  Repeat
    S1 := S2; T := T / 2; S2 := S1 + T;
  Until S2 - S1 < Epsilon;
  WriteLn (S2:8:4);
END.
```

::: exemple Suivre la somme 1 + 1/2 + 1/4 + …
Ici Epsilon = 1E-1, soit 0,1.

1. Départ : S2 = 1, T = 1.
2. Passe 1 : T = 0,5, S2 = 1,5, écart 0,5. Passe 2 : T = 0,25, S2 = 1,75, écart 0,25.
3. Passe 3 : T = 0,125, S2 = 1,875, écart 0,125, encore supérieur à 0,1.
4. Passe 4 : T = 0,0625, S2 = 1,9375, écart 0,0625 < 0,1 : arrêt, le programme affiche 1.9375 ✓.

:::

::: piege
**Erreur : écrire 10E-4 pour 10⁻⁴.** On lit « dix puissance moins quatre ». L'erreur tente parce que le E ressemble à la puissance de 10 et que le 10 semble en faire partie. Mais `10E-4` vaut 10 × 10⁻⁴ = 10⁻³, dix fois trop grand : le programme s'arrête trop tôt. Pour 10⁻⁴, on écrit `1E-4` ou `0.0001`.
:::

::: propriete
Le test compare deux termes consécutifs, il ne mesure pas l'erreur sur la limite. Avec Epsilon = 1E-4, le programme Pi_Euler (section suivante) affiche 3,1319 alors que π ≈ 3,1416 : l'erreur, environ 0,0097, est bien plus grande que Epsilon.
Cas limite : `S2 - S1 < Epsilon` suppose S2 ≥ S1. Si les termes changent de signe, il faut `Abs (S2 - S1)`.
:::

::: verifie À toi : lire un Epsilon
Quelle valeur décimale désignent `1E-3` et `10E-5` ?

---

`1E-3` vaut 0,001. `10E-5` vaut 10 × 10⁻⁵ = 10⁻⁴ = 0,0001.
:::

::: retenir
On répète jusqu'à ce que l'écart entre deux termes consécutifs soit inférieur à Epsilon ; `1E-4` vaut 10⁻⁴, `10E-4` vaut 10⁻³, et cet écart ne mesure pas l'erreur.
:::

## 🥧 π par la formule d'Euler

Euler a montré que π²/6 = 1 + 1/2² + 1/3² + 1/4² + … : en additionnant des inverses de carrés, la somme se rapproche de π²/6 ≈ 1,6449.
Comment en tirer π, et à quelle vitesse ?

::: definition
On cumule S = 1 + 1/2² + … + 1/n², puis π ≈ √(6 × S).
Algorithme `Pi_Euler` : S2 ← 1 et i ← 2 ; Répéter S1 ← S2, S2 ← S1 + 1/i², i ← i + 1 ; Jusqu'à √(6 × S2) − √(6 × S1) < Epsilon ; afficher √(6 × S2). Le test porte sur l'estimation de π, pas sur S.
:::

```pascal
Const Epsilon = 1E-4;
Var S1, S2 : Real; i : LongInt;
BEGIN
  S2 := 1; i := 2;
  Repeat
    S1 := S2;
    S2 := S1 + 1 / Sqr (i);
    i := i + 1;
  Until Sqrt (6 * S2) - Sqrt (6 * S1) < Epsilon;
  WriteLn (Sqrt (6 * S2):10:6);
END.
```

::: exemple Trois passes à la main

1. Départ : S2 = 1 (le terme 1/1²) et i = 2.
2. Passe 1 : S2 = 1 + 1/4 = 1,25, puis i = 3. Passe 2 : S2 = 1,25 + 1/9 ≈ 1,3611, puis i = 4.
3. Passe 3 : S2 = 1,3611 + 1/16 ≈ 1,4236, puis i = 5.
4. Estimation : √(6 × 1,4236) = √8,5417 ≈ 2,9226, encore loin de π ✓. Avec Epsilon = 1E-4, le programme s'arrête après 97 passes sur 3,131883.

:::

::: piege
**Erreur : afficher S2 au lieu de √(6 × S2).** À l'arrêt, le programme affiche 1,6348. L'erreur tente parce que S2 est la variable calculée dans la boucle. Mais S tend vers π²/6 ≈ 1,6449 : il faut multiplier par 6 puis prendre la racine carrée pour obtenir π.
:::

::: propriete
La convergence est lente : 97 passes ne donnent que 3,1319, exact au dixième seulement.
Cas limite : S2 vaut déjà 1, le terme i = 1. Partir avec i ← 1 compterait ce terme deux fois et donnerait √12 ≈ 3,46 après la première passe.
:::

::: verifie À toi : suivre l'indice
Après 6 passes de `Pi_Euler`, que vaut i et quel est le dernier terme ajouté ?

---

Chaque passe augmente i de 1 depuis 2 : après 6 passes, i = 8. Le dernier terme ajouté correspond à i = 7, soit 1/7² = 1/49.
:::

::: retenir
Euler : on additionne 1/i² à partir de i = 2 avec S2 = 1, puis π ≈ √(6 × S2) ; la convergence est lente.
:::

## ✖️ π par la formule de Wallis

Wallis écrit π/2 comme un produit de fractions : π/2 = 2/1 × 2/3 × 4/3 × 4/5 × 6/5 × 6/7 × …
Comment fabriquer ces facteurs un par un ?

::: definition
Les facteurs ont un numérateur pair Num et un dénominateur impair Den. À tour de rôle, Num puis Den augmentent de 2 : 2/1, 2/3, 4/3, 4/5, 6/5, 6/7, …
Algorithme `Pi_Wallis` : P2 ← 2 (le facteur 2/1), i ← 2, Num ← 2, Den ← 3 ; Répéter P1 ← P2, P2 ← P1 × Num/Den, puis Num + 2 si i Mod 2 = 0, sinon Den + 2, i ← i + 1 ; Jusqu'à |2 × P2 − 2 × P1| < Epsilon ; afficher 2 × P2.
:::

```pascal
Const Epsilon = 1E-4;
Var P1, P2 : Real; i, Num, Den : LongInt;
BEGIN
  P2 := 2; i := 2; Num := 2; Den := 3;
  Repeat
    P1 := P2;
    P2 := P1 * (Num / Den);
    If i Mod 2 = 0 Then Num := Num + 2 Else Den := Den + 2;
    i := i + 1;
  Until Abs (2 * P2 - 2 * P1) < Epsilon;
  WriteLn (2 * P2:10:6);
END.
```

::: exemple Quatre passes à la main

1. Passe 1 (i = 2) : P2 = 2 × 2/3 ≈ 1,3333 ; i est pair, donc Num = 4.
2. Passe 2 (i = 3) : P2 = 1,3333 × 4/3 ≈ 1,7778 ; i est impair, donc Den = 5.
3. Passe 3 (i = 4) : P2 = 1,7778 × 4/5 ≈ 1,4222 ; Num = 6.
4. Passe 4 (i = 5) : P2 = 1,4222 × 6/5 ≈ 1,7067 ; Den = 7. L'estimation 2 × P2 vaut 3,4133 : elle oscille autour de π ✓.

:::

::: piege
**Erreur : additionner les fractions.** L'encadré « Retenons » du manuel écrit π/2 = 2/1 + 2/3 + 4/3 + … avec des signes +, ce qui est une coquille. L'erreur tente parce qu'on vient d'additionner des termes avec Euler. Mais une somme 2, 2,67, 4, 4,8, 6, … grandit sans limite, alors que le produit tend vers π/2. Wallis multiplie.
:::

::: propriete
La convergence est très lente : avec Epsilon = 1E-4, le programme exécute environ 31 000 passes pour afficher 3,141543.
Cas limite : `/` rend un réel. Avec `Num Div Den`, 2 Div 3 vaut 0 : P2 devient 0 et le programme affiche 0.
:::

::: verifie À toi : l'alternance
Quel facteur utilise la passe 5 ? Que valent Num et Den à la fin de cette passe ?

---

La passe 5 (i = 6) utilise Num/Den = 6/7. Comme i = 6 est pair, Num passe à 8 ; Den reste 7. Les valeurs sont donc Num = 8 et Den = 7.
:::

::: retenir
Wallis est un produit de facteurs Num/Den, avec Num ou Den augmenté de 2 selon la parité de i ; on affiche 2 × P2 et la convergence est très lente.
:::

## ➕ Les séries alternées : π/4 et le sinus

π/4 = 1 − 1/3 + 1/5 − 1/7 + … : un terme positif, puis un négatif, et ainsi de suite.
Comment faire changer le signe à chaque passe ?

::: definition
La série de Leibniz a pour terme U(n) = (−1)ⁿ / (2n + 1), avec U0 = 1. On cumule les termes dans S, puis π ≈ 4 × S.
Pour alterner, on garde une variable `Signe` valant 1 au départ et l'on exécute `Signe := -Signe` à chaque passe. Le signe change aussi dans le sinus : sin(x) = x − x³/3! + x⁵/5! − x⁷/7! + …
:::

```pascal
Const Epsilon = 1E-4;
Var S1, S2 : Real; n, Signe : LongInt;
BEGIN
  S2 := 1; n := 0; Signe := 1;
  Repeat
    S1 := S2; n := n + 1; Signe := -Signe;
    S2 := S1 + Signe / (2 * n + 1);
  Until Abs (S2 - S1) < Epsilon;
  WriteLn (4 * S2:8:4);
END.
```

::: exemple Quatre passes à la main

1. Départ : S2 = 1, n = 0, Signe = 1.
2. Passe 1 : Signe = −1, S2 = 1 − 1/3 ≈ 0,6667. Passe 2 : Signe = 1, S2 = 0,6667 + 1/5 ≈ 0,8667.
3. Passe 3 : S2 = 0,8667 − 1/7 ≈ 0,7238. L'estimation 4 × S2 vaut 2,895 ✓.
4. L'écart Abs (S2 − S1) vaut 1/(2n + 1) : il passe sous 10⁻⁴ pour n = 5000, et le programme affiche 3.1418.

:::

::: piege
**Erreur : oublier d'alterner le signe.** On additionne 1 + 1/3 + 1/5 + 1/7 et l'on trouve 4 × 1,676 ≈ 6,70 après trois passes. L'erreur tente parce que le terme général semble ne dépendre que de 2n + 1. Mais le facteur (−1)ⁿ doit changer le signe à chaque terme : sans lui, la somme croît au lieu de se stabiliser vers π/4 ≈ 0,785. Le sujet de Bac 2001 du manuel imprime lui-même sin(x) = x + x³/3! + x⁵/5! + … sans alterner : c'est une coquille, il faut alterner.
:::

::: propriete
La série converge lentement : 5000 passes donnent 3,1418, une erreur de l'ordre de 2 × 10⁻⁴.
Cas limite : sans `Abs`, le test `S2 - S1 < Epsilon` est vrai dès qu'un terme est négatif. Ici, après la passe 1, S2 − S1 = −1/3 : le programme s'arrête avec 4 × 0,6667 ≈ 2,67.
:::

::: verifie À toi : cumuler une série alternée
Que vaut 4 × S après 4 passes, c'est-à-dire pour 1 − 1/3 + 1/5 − 1/7 + 1/9 ?

---

S = 1 − 0,3333 + 0,2 − 0,1429 + 0,1111 ≈ 0,8349. Donc 4 × S ≈ 3,3397 : encore loin de π, mais l'écart décroît à chaque terme.
:::

::: retenir
Une série alternée se programme avec un `Signe` inversé à chaque passe ; π ≈ 4 × (1 − 1/3 + 1/5 − …), et le test d'arrêt exige une valeur absolue.
:::

## 🔢 e par les factorielles

Le nombre e ≈ 2,71828 se calcule par 1 + 1/1! + 1/2! + 1/3! + … : les termes chutent très vite.
Comment calculer 1/i! à chaque passe ?

::: definition
La **factorielle** vaut n! = 1 × 2 × … × n, avec 0! = 1. On l'obtient par une fonction `Fact` à boucle `For`.
Algorithme `e_Fact` : S2 ← 1 (le terme 1/0!), i ← 0 ; Répéter S1 ← S2, i ← i + 1, S2 ← S1 + 1/Fact (i) ; Jusqu'à S2 − S1 < Epsilon. L'écart S2 − S1 est le dernier terme ajouté, 1/i!.
:::

```pascal
Const Epsilon = 1E-4;
Var S1, S2 : Real; i : LongInt;

Function Fact (Nb : LongInt) : LongInt;
Var F, j : LongInt;
Begin
  F := 1;
  For j := 1 To Nb Do F := F * j;
  Fact := F;
End;

BEGIN
  S2 := 1; i := 0;
  Repeat
    S1 := S2; i := i + 1;
    S2 := S1 + 1 / Fact (i);
  Until S2 - S1 < Epsilon;
  WriteLn (S2:12:8, ' après ', i, ' passes');
END.
```

::: exemple Suivre e_Fact avec Epsilon = 1E-2

1. Départ : S2 = 1. Passe 1 : S2 = 1 + 1/1! = 2, écart 1.
2. Passe 2 : S2 = 2 + 1/2 = 2,5. Passe 3 : S2 = 2,5 + 1/6 ≈ 2,6667. Passe 4 : S2 = 2,6667 + 1/24 ≈ 2,7083, écart 0,0417.
3. Passe 5 : S2 = 2,7083 + 1/120 ≈ 2,7167, écart 0,0083 < 0,01 : arrêt après 5 passes.
4. Comparaison : e ≈ 2,71828, donc l'erreur est de 0,0016. Avec 1E-4, le programme s'arrête après 8 passes sur 2,71827877 ✓.

:::

::: piege
**Erreur : partir de S2 ← 0.** On oublie que le premier terme est 1/0! = 1. L'erreur tente parce qu'une somme démarre souvent à 0. Mais le programme affiche alors 1,71827877 au lieu de 2,71827877 : il manque ce terme 1. L'initialisation S2 ← 1 le range à l'avance.
:::

::: propriete
La convergence est rapide : 8 passes suffisent pour 1E-4, contre 97 pour Euler et environ 31 000 pour Wallis.
Cas limite : dans un `LongInt`, 13! = 6 227 020 800 dépasse 2 147 483 647. La version récursive `Fact (Nb) = Nb × Fact (Nb − 1)`, avec `Fact (0) = 1`, déborde de même.
:::

::: verifie À toi : un terme de la série
Quel terme ajoute la passe i = 6 ? Quel écart S2 − S1 le test lit-il à cet instant ?

---

La passe 6 ajoute 1/6! = 1/720 ≈ 0,00139. Cet écart S2 − S1 est précisément ce terme.
:::

::: retenir
e se calcule par la somme 1/i! en partant de S2 = 1 ; l'écart S2 − S1 est le dernier terme et la série converge très vite.
:::

## 🟦 Les rectangles : calculer une aire

Pour une fonction sans primitive connue, l'intégrale de f entre a et b, l'aire sous la courbe, ne se calcule pas exactement.
Comment l'approcher par des rectangles ?

::: definition
On découpe [a ; b] en n intervalles de largeur h = (b − a) / n. Sur chacun, un rectangle de largeur h remplace l'aire sous la courbe. Sa hauteur est f(point gauche), f(point droit) ou f(point milieu) de l'intervalle.
Résultat : (somme des hauteurs) × h. Le programme `Meth_Rec` du manuel code le **point milieu** : x ← a + h/2, puis x ← x + h à chaque rectangle.
:::

::: figure Deux rectangles au point milieu sous la courbe de f(x) = 1/(1 + x²) : largeur 2, hauteurs f(2) = 0,2 et f(4) ≈ 0,0588
<svg viewBox="0 0 340 260">
<line x1="40" y1="220" x2="320" y2="220" stroke="#0f172a" stroke-width="1.5"/>
<line x1="40" y1="220" x2="40" y2="20" stroke="#0f172a" stroke-width="1.5"/>
<rect x="85" y="160.0" width="90" height="60.0" fill="#0f6e56" fill-opacity="0.12" stroke="#0f6e56"/>
<rect x="175" y="202.4" width="90" height="17.6" fill="#0f6e56" fill-opacity="0.12" stroke="#0f6e56"/>
<line x1="130" y1="220" x2="130" y2="160.0" stroke="#94a3b8" stroke-dasharray="4 3"/>
<line x1="220" y1="220" x2="220" y2="202.4" stroke="#94a3b8" stroke-dasharray="4 3"/>
<line x1="85" y1="220" x2="85" y2="225" stroke="#0f172a"/><text x="85" y="240" font-size="12" text-anchor="middle" fill="#0f172a">1</text>
<line x1="130" y1="220" x2="130" y2="225" stroke="#0f172a"/><text x="130" y="240" font-size="12" text-anchor="middle" fill="#0f172a">2</text>
<line x1="175" y1="220" x2="175" y2="225" stroke="#0f172a"/><text x="175" y="240" font-size="12" text-anchor="middle" fill="#0f172a">3</text>
<line x1="220" y1="220" x2="220" y2="225" stroke="#0f172a"/><text x="220" y="240" font-size="12" text-anchor="middle" fill="#0f172a">4</text>
<line x1="265" y1="220" x2="265" y2="225" stroke="#0f172a"/><text x="265" y="240" font-size="12" text-anchor="middle" fill="#0f172a">5</text>
<line x1="35" y1="160.0" x2="40" y2="160.0" stroke="#0f172a"/><text x="32" y="164.0" font-size="11" text-anchor="end" fill="#0f172a">0,2</text>
<line x1="35" y1="100.0" x2="40" y2="100.0" stroke="#0f172a"/><text x="32" y="104.0" font-size="11" text-anchor="end" fill="#0f172a">0,4</text>
<path d="M85.0,70.0 L87.2,77.3 L89.5,84.3 L91.8,90.8 L94.0,97.0 L96.2,102.9 L98.5,108.5 L100.8,113.7 L103.0,118.6 L105.2,123.3 L107.5,127.7 L109.8,131.8 L112.0,135.7 L114.2,139.4 L116.5,142.9 L118.8,146.2 L121.0,149.2 L123.2,152.2 L125.5,154.9 L127.8,157.5 L130.0,160.0 L132.2,162.3 L134.5,164.5 L136.8,166.6 L139.0,168.6 L141.2,170.5 L143.5,172.3 L145.8,174.0 L148.0,175.6 L150.2,177.2 L152.5,178.6 L154.8,180.0 L157.0,181.3 L159.2,182.6 L161.5,183.8 L163.8,185.0 L166.0,186.1 L168.2,187.1 L170.5,188.1 L172.8,189.1 L175.0,190.0 L177.2,190.9 L179.5,191.7 L181.8,192.5 L184.0,193.3 L186.2,194.1 L188.5,194.8 L190.8,195.5 L193.0,196.1 L195.2,196.7 L197.5,197.4 L199.8,197.9 L202.0,198.5 L204.3,199.1 L206.5,199.6 L208.8,200.1 L211.0,200.6 L213.2,201.0 L215.5,201.5 L217.8,201.9 L220.0,202.4 L222.3,202.8 L224.5,203.2 L226.8,203.5 L229.0,203.9 L231.2,204.3 L233.5,204.6 L235.7,204.9 L238.0,205.3 L240.2,205.6 L242.5,205.9 L244.8,206.2 L247.0,206.5 L249.3,206.7 L251.5,207.0 L253.8,207.3 L256.0,207.5 L258.2,207.8 L260.5,208.0 L262.8,208.2 L265.0,208.5 L267.2,208.7 L269.5,208.9 L271.8,209.1 L274.0,209.3 L276.2,209.5 L278.5,209.7 L280.8,209.9 L283.0,210.1 L285.2,210.2 L287.5,210.4" fill="none" stroke="#0f6e56" stroke-width="2.5"/>
<circle cx="130" cy="160.0" r="3.5" fill="#0f172a"/>
<circle cx="220" cy="202.4" r="3.5" fill="#0f172a"/>
<text x="136" y="152.0" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" font-size="12" fill="#0f172a">f(2) = 0,2</text>
<text x="220" y="192.4" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" font-size="12" fill="#0f172a">f(4) ≈ 0,0588</text>
<text x="130" y="206" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" font-size="12" fill="#0f172a">h = 2</text>
<text x="325" y="240" font-size="12" fill="#0f172a">x</text>
</svg>
:::

Dans la figure, chaque rectangle couvre un intervalle de largeur 2 et sa hauteur est lue sous la courbe à son milieu, x = 2 puis x = 4.

```pascal
Function f (x : Real) : Real;
Begin
  f := 1 / (1 + Sqr (x));
End;

Function Rectangles (a, b : Real; n : Integer) : Real;
Var Somme, h, x : Real; k : Integer;
Begin
  Somme := 0; h := (b - a) / n; x := a + h / 2;
  For k := 1 To n Do
  Begin
    Somme := Somme + f (x);
    x := x + h;
  End;
  Rectangles := Somme * h;
End;
```

::: exemple f(x) = 1/(1 + x²) sur [1 ; 5] avec n = 2

1. Largeur : h = (5 − 1) / 2 = 2. Les milieux sont x = 2 puis x = 4.
2. Hauteurs : f(2) = 0,2 et f(4) = 1/17 ≈ 0,0588. Somme ≈ 0,2588.
3. Aire : 0,2588 × 2 ≈ 0,5176. La valeur exacte est 0,5880 (arctan 5 − arctan 1) ✓.
4. Au point gauche (x = 1 et 3), on obtient (0,5 + 0,1) × 2 = 1,2 ; au point droit (x = 3 et 5), 0,2769.

:::

::: piege
**Erreur : lire `Meth_Rec` comme un point gauche.** L'encadré « Retenons » du manuel parle de « point gauche », donc l'on croit que le programme part de x = a. Mais la première hauteur est f(a + h/2) : le programme est du point milieu. Sur l'exemple, le point gauche donne 1,2 et le point milieu 0,5176, très différents.
:::

::: propriete
La fonction f(x) = 1/(1 + x²) est décroissante sur [1 ; 5] : le point gauche surestime (1,2), le point droit sous-estime (0,2769), le point milieu est entre les deux (0,5176). Pour une fonction croissante, c'est l'inverse.
Cas limite : la méthode suppose b > a et n ≥ 1, car si b ≤ a, h est nul ou négatif, et si n = 0, (b − a)/n est une division par zéro ; le manuel contrôle la saisie avec `Until b1 > a1` et `Until n1 > 0`.
:::

::: verifie À toi : le premier milieu
Pour a = 0, b = 6 et n = 3, que valent h et le premier x de `Rectangles` ?

---

h = (6 − 0) / 3 = 2. Le premier x vaut a + h/2 = 0 + 1 = 1 (puis 3 et 5).
:::

::: retenir
Les rectangles remplacent l'aire par n rectangles de largeur h = (b − a)/n ; `Meth_Rec` utilise le point milieu x = a + h/2, et le résultat est Somme × h.
:::

## 📐 Les trapèzes : une aire plus fidèle

Un rectangle ignore la pente de la courbe sur son intervalle. En joignant les deux extrémités de l'arc par un segment, on obtient un trapèze.
Comment calculer l'aire de ces trapèzes ?

::: definition
Sur [aᵢ ; aᵢ₊₁] de largeur h, le trapèze a pour bases f(aᵢ) et f(aᵢ₊₁) : son aire vaut h × (f(aᵢ) + f(aᵢ₊₁)) / 2.
L'aire cherchée est la somme de ces n trapèzes, avec aᵢ = a + i × h et h = (b − a) / n.
:::

::: figure Deux trapèzes sous la courbe de f(x) = 1/(1 + x²) : sommets (1 ; 0,5), (3 ; 0,1) et (5 ; 0,0385), chaque arc remplacé par un segment
<svg viewBox="0 0 340 260">
<line x1="40" y1="220" x2="320" y2="220" stroke="#0f172a" stroke-width="1.5"/>
<line x1="40" y1="220" x2="40" y2="20" stroke="#0f172a" stroke-width="1.5"/>
<polygon points="85,220 85,70.0 175,190.0 175,220" fill="#0f6e56" fill-opacity="0.12" stroke="#0f6e56"/>
<polygon points="175,220 175,190.0 265,208.4 265,220" fill="#0f6e56" fill-opacity="0.12" stroke="#0f6e56"/>
<line x1="85" y1="220" x2="85" y2="225" stroke="#0f172a"/><text x="85" y="240" font-size="12" text-anchor="middle" fill="#0f172a">1</text>
<line x1="130" y1="220" x2="130" y2="225" stroke="#0f172a"/><text x="130" y="240" font-size="12" text-anchor="middle" fill="#0f172a">2</text>
<line x1="175" y1="220" x2="175" y2="225" stroke="#0f172a"/><text x="175" y="240" font-size="12" text-anchor="middle" fill="#0f172a">3</text>
<line x1="220" y1="220" x2="220" y2="225" stroke="#0f172a"/><text x="220" y="240" font-size="12" text-anchor="middle" fill="#0f172a">4</text>
<line x1="265" y1="220" x2="265" y2="225" stroke="#0f172a"/><text x="265" y="240" font-size="12" text-anchor="middle" fill="#0f172a">5</text>
<line x1="35" y1="160.0" x2="40" y2="160.0" stroke="#0f172a"/><text x="32" y="164.0" font-size="11" text-anchor="end" fill="#0f172a">0,2</text>
<line x1="35" y1="100.0" x2="40" y2="100.0" stroke="#0f172a"/><text x="32" y="104.0" font-size="11" text-anchor="end" fill="#0f172a">0,4</text>
<path d="M85.0,70.0 L87.2,77.3 L89.5,84.3 L91.8,90.8 L94.0,97.0 L96.2,102.9 L98.5,108.5 L100.8,113.7 L103.0,118.6 L105.2,123.3 L107.5,127.7 L109.8,131.8 L112.0,135.7 L114.2,139.4 L116.5,142.9 L118.8,146.2 L121.0,149.2 L123.2,152.2 L125.5,154.9 L127.8,157.5 L130.0,160.0 L132.2,162.3 L134.5,164.5 L136.8,166.6 L139.0,168.6 L141.2,170.5 L143.5,172.3 L145.8,174.0 L148.0,175.6 L150.2,177.2 L152.5,178.6 L154.8,180.0 L157.0,181.3 L159.2,182.6 L161.5,183.8 L163.8,185.0 L166.0,186.1 L168.2,187.1 L170.5,188.1 L172.8,189.1 L175.0,190.0 L177.2,190.9 L179.5,191.7 L181.8,192.5 L184.0,193.3 L186.2,194.1 L188.5,194.8 L190.8,195.5 L193.0,196.1 L195.2,196.7 L197.5,197.4 L199.8,197.9 L202.0,198.5 L204.3,199.1 L206.5,199.6 L208.8,200.1 L211.0,200.6 L213.2,201.0 L215.5,201.5 L217.8,201.9 L220.0,202.4 L222.3,202.8 L224.5,203.2 L226.8,203.5 L229.0,203.9 L231.2,204.3 L233.5,204.6 L235.7,204.9 L238.0,205.3 L240.2,205.6 L242.5,205.9 L244.8,206.2 L247.0,206.5 L249.3,206.7 L251.5,207.0 L253.8,207.3 L256.0,207.5 L258.2,207.8 L260.5,208.0 L262.8,208.2 L265.0,208.5 L267.2,208.7 L269.5,208.9 L271.8,209.1 L274.0,209.3 L276.2,209.5 L278.5,209.7 L280.8,209.9 L283.0,210.1 L285.2,210.2 L287.5,210.4" fill="none" stroke="#0f6e56" stroke-width="2.5"/>
<circle cx="85" cy="70.0" r="3.5" fill="#0f172a"/>
<circle cx="175" cy="190.0" r="3.5" fill="#0f172a"/>
<circle cx="265" cy="208.4" r="3.5" fill="#0f172a"/>
<text x="93" y="66.0" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" font-size="12" fill="#0f172a">(1 ; 0,5)</text>
<text x="183" y="182.0" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" font-size="12" fill="#0f172a">(3 ; 0,1)</text>
<text x="261" y="198.4" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" font-size="12" fill="#0f172a">(5 ; 0,0385)</text>
<text x="325" y="240" font-size="12" fill="#0f172a">x</text>
</svg>
:::

Dans la figure, chaque trapèze s'appuie sur l'axe et sur le segment qui joint deux points de la courbe.

```pascal
{ avec la même fonction f }
Function Trapezes (a, b : Real; n : Integer) : Real;
Var Somme, h : Real; k : Integer;
Begin
  h := (b - a) / n;
  Somme := 0;
  For k := 0 To n - 1 Do
    Somme := Somme + (f (a + k * h) + f (a + (k + 1) * h)) / 2;
  Trapezes := Somme * h;
End;
```

::: exemple f(x) = 1/(1 + x²) sur [1 ; 5] avec n = 2

1. Largeur : h = 2, et les points sont 1, 3 et 5. Valeurs : f(1) = 0,5, f(3) = 0,1, f(5) ≈ 0,0385.
2. Premier trapèze : (0,5 + 0,1) / 2 = 0,3. Second : (0,1 + 0,0385) / 2 ≈ 0,0692.
3. Aire : (0,3 + 0,0692) × 2 ≈ 0,7385.
4. C'est la moyenne du point gauche (1,2) et du point droit (0,2769) ✓. L'exacte vaut 0,5880.

:::

::: piege
**Erreur : prendre h = (a + b) / n.** Pour a = 1, b = 5, n = 2, on trouve h = 3 au lieu de 2. L'erreur tente parce que a et b sont les deux bornes et que l'on pense à les combiner par une somme. Mais h est la longueur de [a ; b] divisée par n : on soustrait. Avec h = 3, les trapèzes couvriraient [1 ; 7].
:::

::: propriete
Quand n grandit, les deux méthodes se rapprochent de l'aire exacte 0,5880. Pour cette fonction :

| n   | point milieu | trapèzes |
| --- | ------------ | -------- |
| 2   | 0,5176       | 0,7385   |
| 5   | 0,5752       | 0,6138   |
| 10  | 0,5848       | 0,5945   |

Cas limite : avec n = 1, le trapèze n'utilise que f(a) et f(b), et l'estimation est très grossière.
:::

::: verifie À toi : un trapèze
Quelle est l'aire du trapèze sur [2 ; 4] pour f(x) = x² ?

---

h = 2, f(2) = 4 et f(4) = 16. L'aire vaut 2 × (4 + 16) / 2 = 20.
:::

::: retenir
Un trapèze a pour aire h × (f(aᵢ) + f(aᵢ₊₁)) / 2 avec h = (b − a)/n ; la somme des trapèzes approche l'aire, de mieux en mieux quand n grandit.
:::

> 🗡️ Devant une approximation, pose toujours trois questions : quel est le premier terme, quel est le suivant, et quel écart autorise-t-on avant de s'arrêter ?

> 🏆 Porte franchie ! Tu sais approcher un point fixe, π, e et une aire. Prochaine arène : les algorithmes avancés.
