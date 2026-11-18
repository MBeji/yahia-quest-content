# ⚔️ Suites réelles — placer, prévoir, converger : du loyer qui monte à l'équilibre d'un marché

> 💡 « Une suite raconte une évolution pas à pas : le montant d'une épargne d'une année à l'autre, le nombre d'abonnés d'un mois au suivant. »

Bienvenue, héros de l'Économie et gestion. Un gérant veut savoir ce que vaudra son placement dans dix ans, un directeur si sa clientèle va se stabiliser ou s'effondrer. Huit étapes te mènent des suites les plus simples aux plus fines : arithmétiques et géométriques, suites bornées, sens de variation, convergence, opérations sur les limites, comparaison, puis les deux grandes familles de suites récurrentes. On suppose acquis le calcul des limites de fonctions, les dérivées, ln et l'exponentielle (chapitres précédents).

## 🧭 Suites arithmétiques et géométriques

Un loyer commercial augmente de 12 dinars chaque année ; un capital placé grossit de 4 % chaque année. Dans le premier cas on ajoute toujours la même quantité, dans le second on multiplie toujours par le même coefficient.
Comment calculer le terme de rang 20 sans écrire les dix-neuf précédents ?

::: definition
Une suite (uₙ) est **arithmétique de raison r** si, pour tout entier n, uₙ₊₁ = uₙ + r. Alors uₙ = u₀ + n·r.

Une suite (uₙ) est **géométrique de raison q** si, pour tout entier n, uₙ₊₁ = q·uₙ. Alors uₙ = u₀ · qⁿ.

Pour une suite qui commence au rang 1, on remplace n par n − 1 : uₙ = u₁ + (n − 1)·r, ou uₙ = u₁ · qⁿ⁻¹. La somme S de n termes consécutifs vaut, pour une suite arithmétique, n × (premier terme + dernier terme) / 2 et, pour une suite géométrique de raison q ≠ 1, (premier terme) × (1 − qⁿ) / (1 − q).
:::

::: exemple Une prime croissante : u₀ = 200, r = 15
1. uₙ = 200 + 15n, donc u₁₂ = 200 + 180 = 380.
2. Les douze premiers termes u₀ à u₁₁ ont pour somme 12 × (200 + 365) / 2 = 6 × 565 = 3390.
3. Avec cinq termes d'une suite géométrique de premier terme 3 et de raison 2 : 3 × (1 − 2⁵) / (1 − 2) = 93, soit 3 + 6 + 12 + 24 + 48.

:::

::: exemple Intérêts simples et intérêts composés sur 2000 dinars à 4 % par an
1. **Intérêts simples** : l'intérêt de 80 dinars est calculé chaque année sur le capital de départ. Le capital est arithmétique de raison 80 : Cₙ = 2000 + 80n, donc C₅ = 2400.
2. **Intérêts composés** : les intérêts s'ajoutent au capital et rapportent à leur tour. Le capital est géométrique de raison 1,04 (c'est la valeur acquise vue au chapitre 4, lue ici pas à pas) : Cₙ = 2000 × 1,04ⁿ, donc C₅ = 2000 × 1,04⁵ ≈ 2433,31.
3. L'écart de 33,31 dinars après cinq ans est le gain des « intérêts sur les intérêts ».

:::

::: piege Écrire la raison 0,04 au lieu de 1,04
Pour une hausse de 4 % par an, on écrit q = 0,04. Cela tente parce que « 4 % » s'écrit 0,04. Mais une hausse de 4 % multiplie par 1 + 0,04 = 1,04 ; avec q = 0,04, le capital serait divisé par 25 chaque année. Une baisse de 15 % multiplie, elle, par 1 − 0,15 = 0,85.
:::

::: propriete
- Pour reconnaître la nature d'une suite, on calcule uₙ₊₁ − uₙ (constante ⇒ arithmétique) ou uₙ₊₁ / uₙ (constante ⇒ géométrique, termes non nuls).
- L'indice compte : u₀ est le premier terme, donc uₙ est le (n + 1)-ième terme.

Cas limite : si q = 1, la suite géométrique est constante et sa somme de n termes vaut n × u₀ ; la formule avec 1 − q au dénominateur ne s'applique pas.
:::

::: verifie
Une suite arithmétique vérifie u₀ = 50 et u₈ = 98. Quelle est sa raison, et que vaut u₂₀ ?

---

u₈ = u₀ + 8r donne 98 = 50 + 8r, donc r = 6. Alors u₂₀ = 50 + 20 × 6 = 170. Le résultat 50 + 21 × 6 = 176 compterait un terme de trop, car u₀ est déjà le premier terme.
:::

::: retenir
Arithmétique : on ajoute r, uₙ = u₀ + n·r (intérêts simples). Géométrique : on multiplie par q, uₙ = u₀ · qⁿ (intérêts composés) ; une hausse de t % donne q = 1 + t/100.
:::

## 🔮 Suites majorées, minorées, bornées

Le stock d'un entrepôt oscille d'une semaine à l'autre ; le gérant voudrait un plafond qu'il ne dépassera jamais, et un plancher en dessous duquel il ne descendra jamais.
Comment prouver qu'un plafond tient pour tous les rangs, et pas seulement pour les premiers ?

::: definition
Une suite (uₙ) est **majorée** s'il existe un réel M tel que uₙ ≤ M pour tout n ; elle est **minorée** s'il existe un réel m tel que uₙ ≥ m pour tout n ; elle est **bornée** si elle est à la fois majorée et minorée, c'est-à-dire m ≤ uₙ ≤ M pour tout n.
:::

::: exemple Un encadrement direct : uₙ = (2n + 3) / (n + 1)
1. On écrit uₙ = 2 + 1 / (n + 1).
2. Pour tout n ≥ 0, 0 < 1 / (n + 1) ≤ 1.
3. Donc 2 < uₙ ≤ 3 : la suite est bornée, minorée par 2 et majorée par 3.

:::

::: exemple Par récurrence : u₀ = 1 et uₙ₊₁ = (uₙ + 6) / 2
1. Initialisation : u₀ = 1 ≤ 6.
2. Hérédité : si uₙ ≤ 6, alors uₙ + 6 ≤ 12 et uₙ₊₁ = (uₙ + 6) / 2 ≤ 6.
3. La propriété étant vraie au rang 0 et héréditaire, uₙ ≤ 6 pour tout n : la suite est majorée par 6.

:::

::: piege Conclure après quelques termes
Pour uₙ = n², on calcule u₀ = 0, u₁ = 1, u₂ = 4, u₃ = 9 et on déclare « majorée par 10 ». Cela tente parce que quatre termes sur quatre respectent le plafond. Mais u₄ = 16 le dépasse, et aucun réel ne majore tous les n². Une majoration doit être démontrée pour **tout** n, par un calcul ou par récurrence.
:::

::: propriete
- Une suite arithmétique de raison r > 0 est minorée par u₀ mais n'est pas majorée ; pour r < 0 c'est l'inverse.
- Les majorants et minorants ne sont pas uniques : si M convient, tout réel plus grand convient aussi.

Cas limite : la suite (−1)ⁿ est bornée (−1 ≤ uₙ ≤ 1) sans être convergente ; être bornée ne suffit donc pas à avoir une limite.
:::

::: verifie
Montrer que la suite définie par uₙ = 3 − 1 / (n + 2) est bornée.

---

Pour tout n, 0 < 1 / (n + 2) ≤ 1/2, donc 3 − 1/2 ≤ uₙ < 3, soit 2,5 ≤ uₙ < 3. La suite est minorée par 2,5 et majorée par 3, donc bornée.
:::

::: retenir
Majorée : uₙ ≤ M pour tout n ; minorée : uₙ ≥ m pour tout n ; bornée : les deux. On le prouve pour tous les rangs par un encadrement ou par récurrence, jamais en testant les premiers termes.
:::

## 🪄 Variation d'une suite

Le solde mensuel d'une boutique baisse d'abord, puis remonte. À partir de quel mois peut-on affirmer qu'il ne fait plus que croître ?
Que regarder pour décider si une suite monte ou descend ?

::: definition
Une suite (uₙ) est **croissante** si uₙ₊₁ ≥ uₙ pour tout n, **décroissante** si uₙ₊₁ ≤ uₙ pour tout n, **constante** si uₙ₊₁ = uₙ, et **monotone** si elle est croissante ou décroissante. Trois méthodes :
- le **signe de uₙ₊₁ − uₙ** ;
- pour des termes strictement positifs, la **comparaison de uₙ₊₁ / uₙ à 1** ;
- si uₙ = f(n) avec f croissante (resp. décroissante) sur [n₀ ; +∞[, la suite est croissante (resp. décroissante) à partir de n₀.
:::

::: exemple Par la différence : uₙ = (2n + 1) / (n + 3)
1. uₙ₊₁ − uₙ = (2n + 3) / (n + 4) − (2n + 1) / (n + 3).
2. On réduit au même dénominateur : le numérateur vaut (2n + 3)(n + 3) − (2n + 1)(n + 4) = (2n² + 9n + 9) − (2n² + 9n + 4) = 5.
3. Donc uₙ₊₁ − uₙ = 5 / ((n + 3)(n + 4)) > 0 : la suite est croissante.

:::

::: exemple Par le quotient et par une fonction
1. uₙ = 500 × 0,9ⁿ a des termes strictement positifs et uₙ₊₁ / uₙ = 0,9 < 1 : la suite est décroissante.
2. uₙ = n² − 6n s'écrit f(n) avec f(x) = x² − 6x, f ′(x) = 2x − 6. La fonction f décroît sur [0 ; 3] puis croît sur [3 ; +∞[ : la suite est croissante à partir de n = 3 (u₂ = −8, u₃ = −9, u₄ = −8, u₅ = −5).

:::

::: piege Quotient supérieur à 1, donc croissante
Pour uₙ = −3 × 2ⁿ, le quotient uₙ₊₁ / uₙ vaut 2, supérieur à 1, et on conclut « croissante ». Cela tente parce que la règle du quotient est apprise avec des termes positifs. Mais ici u₀ = −3 et u₁ = −6 : la suite décroît. Avec des termes négatifs, multiplier par un nombre plus grand que 1 éloigne de zéro vers le bas ; on revient alors à la différence uₙ₊₁ − uₙ = uₙ(q − 1).
:::

::: propriete
- Une suite arithmétique est croissante si r > 0, décroissante si r < 0.
- Une suite géométrique de raison q > 0 est monotone ; si q < 0, ses termes changent de signe à chaque rang et elle n'est pas monotone.

Cas limite : la suite (−1)ⁿ n'est ni croissante ni décroissante ; toutes les suites ne sont pas monotones.
:::

::: verifie
Étudier le sens de variation de uₙ = 2n² − 8n.

---

Avec f(x) = 2x² − 8x, f ′(x) = 4x − 8, qui s'annule en x = 2. Donc f décroît sur [0 ; 2] et croît sur [2 ; +∞[. La suite est croissante à partir de n = 2 ; avant, u₀ = 0, u₁ = −6, u₂ = −8 : elle décroît.
:::

::: retenir
Signe de uₙ₊₁ − uₙ ; quotient uₙ₊₁ / uₙ si les termes sont strictement positifs ; ou variation de f(n). Une suite peut décroître au début puis croître : on précise « à partir de quel rang ».
:::

## 🎯 Suites convergentes et divergentes

Un fabricant remarque que son coût moyen par pièce diminue lot après lot, sans jamais passer sous un certain seuil.
Vers quelle valeur se stabilise-t-il, et comment le prouver ?

::: definition
Une suite est **convergente** si elle admet une limite **finie** ℓ ; elle est **divergente** si sa limite est infinie ou si elle n'a pas de limite. Cette limite, quand elle existe, est unique. Repères :
- si uₙ = f(n) et si lim f(x) = ℓ quand x tend vers +∞, alors lim uₙ = ℓ (ℓ fini ou infini) ;
- suite arithmétique de raison r : limite +∞ si r > 0, −∞ si r < 0 ;
- suite géométrique uₙ = u₀ · qⁿ avec u₀ ≠ 0 : limite 0 si −1 < q < 1, limite +∞ ou −∞ (selon le signe de u₀) si q > 1, pas de limite si q ≤ −1 ; suite constante, de limite u₀, si q = 1.

**Théorème (admis)** : une suite croissante et majorée converge ; une suite décroissante et minorée converge.
:::

::: exemple Par une fonction : uₙ = (3n + 1) / (n + 2)
1. Avec f(x) = (3x + 1) / (x + 2), la limite en +∞ est celle du quotient des termes de plus haut degré, 3x / x = 3.
2. Donc lim uₙ = 3 : la suite converge vers 3.

:::

::: exemple Suites géométriques et suite monotone bornée
1. 6 × (−0,8)ⁿ tend vers 0 car −1 < −0,8 < 1 ; 2 × 1,05ⁿ tend vers +∞ ; (−1,2)ⁿ n'a pas de limite car −1,2 ≤ −1.
2. Soit uₙ = 7 − 1 / (n + 1). Elle est croissante (1 / (n + 1) diminue) et majorée par 7 : elle converge. Sa limite est 7 ; elle est inférieure à 8, qui est un majorant, sans lui être égale.

:::

::: piege Croire que −1 donne la limite −1, ou que bornée suffit
Pour uₙ = (−1)ⁿ, on répond « la limite est 1 » ou « −1 ». Cela tente parce que ces deux valeurs reviennent tour à tour. Mais une limite est une valeur dont les termes **s'approchent** pour tous les grands rangs : ici ils alternent entre 1 et −1 et la suite n'a pas de limite. De même, une suite bornée n'est pas forcément convergente.
:::

::: propriete
- Si une suite croissante est majorée par M, sa limite ℓ vérifie ℓ ≤ M, mais pas nécessairement ℓ = M.
- Une suite convergente reste convergente si on décale les indices : uₙ₊₁ et uₙ ont la même limite.

Cas limite : « divergente » ne veut pas dire « tend vers l'infini » : (−1)ⁿ est divergente et pourtant ne tend vers aucun infini.
:::

::: verifie
La suite uₙ = 4 × (0,7)ⁿ est-elle convergente ? Si oui, quelle est sa limite ?

---

C'est une suite géométrique de raison 0,7 comprise entre −1 et 1, donc 0,7ⁿ tend vers 0 et uₙ tend vers 4 × 0 = 0. La suite est convergente, de limite 0. La valeur 4 est son premier terme, pas sa limite.
:::

::: retenir
Convergente : limite finie ; divergente : limite infinie ou absente. Pour qⁿ : −1 < q < 1 donne 0, q > 1 donne +∞, q ≤ −1 n'a pas de limite. Croissante et majorée (ou décroissante et minorée) assure la convergence.
:::

## 🧮 Opérations sur les limites

Une entreprise a des recettes et des charges qui grandissent toutes deux avec le temps ; le bénéfice est leur différence, le taux de marge leur quotient.
Peut-on additionner, multiplier, diviser des limites comme des nombres ?

::: definition
On peut combiner deux suites terme à terme : la **somme** (u + v)ₙ = uₙ + vₙ, le **produit** (uv)ₙ = uₙ × vₙ, le **multiple** (λu)ₙ = λ × uₙ, la **valeur absolue** |u|ₙ = |uₙ|, l'**inverse** (1/v)ₙ = 1 / vₙ et le **quotient** (u/v)ₙ = uₙ / vₙ, ces deux derniers à condition que vₙ ne s'annule jamais.
:::

::: propriete
Si (uₙ) et (vₙ) convergent vers ℓ et ℓ′, alors uₙ + vₙ tend vers ℓ + ℓ′, uₙ × vₙ vers ℓ × ℓ′, et, si ℓ′ ≠ 0, uₙ / vₙ vers ℓ / ℓ′. Les règles des limites de fonctions s'étendent aux limites infinies, avec quatre **formes indéterminées** :
- (+∞) + (−∞) ;
- 0 × (±∞) ;
- (±∞) / (±∞) ;
- 0 / 0.

Pour lever une indétermination, on **factorise le terme dominant** (la plus grande puissance de n, ou la plus grande base dans qⁿ) puis on utilise ses limites connues.
:::

::: exemple Un quotient de puissances : uₙ = (3 × 4ⁿ − 2ⁿ) / (4ⁿ + 1)
1. Numérateur et dénominateur tendent vers +∞ : forme ∞ / ∞.
2. On factorise 4ⁿ : uₙ = 4ⁿ(3 − (1/2)ⁿ) / (4ⁿ(1 + (1/4)ⁿ)) = (3 − (1/2)ⁿ) / (1 + (1/4)ⁿ).
3. Comme (1/2)ⁿ et (1/4)ⁿ tendent vers 0, la limite est 3 / 1 = 3.

:::

::: exemple Une différence de deux infinis
1. uₙ = n² − 3n est de la forme (+∞) − (+∞) ; on factorise : uₙ = n²(1 − 3/n), et 1 − 3/n tend vers 1, donc uₙ tend vers +∞.
2. vₙ = 2ⁿ − 3ⁿ = 3ⁿ((2/3)ⁿ − 1) : 3ⁿ tend vers +∞ et (2/3)ⁿ − 1 vers −1, donc vₙ tend vers −∞.

:::

::: piege Dire que +∞ − ∞ vaut 0
Pour vₙ = 2ⁿ − 3ⁿ, on écrit « les deux termes tendent vers l'infini, ils se compensent, la limite est 0 ». Cela tente parce que a − a = 0. Mais l'infini n'est pas un nombre : ici 3ⁿ grandit bien plus vite que 2ⁿ, et la différence tend vers −∞. Une forme indéterminée n'a pas de valeur imposée : elle se calcule par factorisation.
:::

::: verifie
Déterminer la limite de uₙ = (5n² + 7) / (2n² − n).

---

Forme ∞ / ∞. On factorise n² : uₙ = (5 + 7/n²) / (2 − 1/n). Les termes 7/n² et 1/n tendent vers 0, donc uₙ tend vers 5/2.
:::

::: retenir
Somme, produit, quotient de limites finies : on opère sur les limites. Quatre formes indéterminées (+∞ − ∞, 0 × ∞, ∞ / ∞, 0 / 0) : on factorise le terme dominant avant de conclure.
:::

## ⚖️ Limites et ordre

Un analyste ne connaît pas la formule exacte du rendement d'un fonds, mais il sait qu'il reste coincé entre deux courbes qui se resserrent.
Peut-on conclure sur une suite qu'on ne sait pas calculer, seulement encadrer ?

::: propriete
Soient (uₙ), (vₙ), (wₙ) trois suites, à partir d'un certain rang :
- **Comparaison** : si uₙ ≥ vₙ et si vₙ tend vers +∞, alors uₙ tend vers +∞ (de même avec ≤ et −∞).
- **Encadrement (théorème des gendarmes)** : si vₙ ≤ uₙ ≤ wₙ et si vₙ et wₙ tendent vers la même limite ℓ, alors uₙ tend vers ℓ.
- **Valeur absolue** : si |uₙ − ℓ| ≤ vₙ et si vₙ tend vers 0, alors uₙ tend vers ℓ.
- **Passage à la limite** : si uₙ ≥ 0 à partir d'un certain rang et si uₙ tend vers ℓ, alors ℓ ≥ 0.
:::

::: exemple Un encadrement : uₙ = (2n + sin n) / n
1. Comme −1 ≤ sin n ≤ 1, on a (2n − 1) / n ≤ uₙ ≤ (2n + 1) / n pour n ≥ 1.
2. Les deux bornes valent 2 − 1/n et 2 + 1/n et tendent vers 2.
3. Par encadrement, uₙ tend vers 2.

:::

::: exemple Une comparaison : uₙ = 3ⁿ + (−1)ⁿ
1. Comme (−1)ⁿ ≥ −1, on a uₙ ≥ 3ⁿ − 1.
2. La suite 3ⁿ − 1 tend vers +∞.
3. Par comparaison, uₙ tend vers +∞.

:::

::: piege Garder l'inégalité stricte à la limite
On sait que 1/n > 0 pour tout n, et on conclut « la limite est strictement positive ». Cela tente parce que chaque terme est strictement positif. Mais 1/n tend vers 0 : un passage à la limite ne garantit que ≥ : l'inégalité stricte peut devenir une égalité, comme ici. Un autre piège est d'encadrer par deux suites de limites différentes : le théorème ne conclut alors rien.
:::

::: verifie
Déterminer la limite de uₙ = cos(n) / (n² + 1).

---

Comme |cos n| ≤ 1, on a |uₙ| ≤ 1 / (n² + 1), et 1 / (n² + 1) tend vers 0. Donc uₙ tend vers 0.
:::

::: retenir
Pour une suite qu'on ne sait pas calculer : on l'encadre (même limite des deux côtés), on la compare à une suite qui tend vers l'infini, ou on majore |uₙ − ℓ| par une suite qui tend vers 0. À la limite, les inégalités strictes deviennent larges.
:::

## 🔁 Suites récurrentes uₙ₊₁ = a·uₙ + b

Une boutique en ligne perd chaque mois 30 % de ses clients et en gagne 300 nouveaux. Part-elle vers la disparition, vers l'explosion, ou vers un équilibre ?
Comment exprimer le nombre de clients en fonction du mois, alors que la règle donne chaque mois en fonction du précédent ?

::: definition
Soit la suite définie par u₀ et uₙ₊₁ = a·uₙ + b avec a ≠ 1. Elle n'est en général ni arithmétique ni géométrique. On cherche le **point fixe** ℓ, solution de ℓ = aℓ + b, soit ℓ = b / (1 − a). La suite auxiliaire vₙ = uₙ − ℓ est **géométrique de raison a** (car vₙ₊₁ = a·vₙ), d'où :

uₙ = ℓ + aⁿ(u₀ − ℓ)

Si −1 < a < 1, aⁿ tend vers 0 et uₙ tend vers ℓ.
:::

::: exemple Les clients de la boutique : u₀ = 500 et uₙ₊₁ = 0,7uₙ + 300
1. Point fixe : ℓ = 300 / (1 − 0,7) = 1000.
2. Pour vₙ = uₙ − 1000 : vₙ₊₁ = 0,7uₙ + 300 − 1000 = 0,7uₙ − 700 = 0,7(uₙ − 1000) = 0,7vₙ, avec v₀ = −500.
3. D'où vₙ = −500 × 0,7ⁿ et uₙ = 1000 − 500 × 0,7ⁿ. Contrôle : u₁ = 650 = 0,7 × 500 + 300 et u₂ = 755.
4. Comme 0,7ⁿ tend vers 0, uₙ tend vers 1000 : la clientèle se stabilise, en croissant.

:::

::: figure Les termes montent par marches vers l'intersection avec y = x, le point fixe 1000
<svg viewBox="0 0 340 250"><title>Escalier de la suite u(n+1) = 0,7u(n) + 300 entre la droite y = 0,7x + 300 et la droite y = x</title><line x1="40" y1="230" x2="330" y2="230" stroke="#333"/><line x1="40" y1="230" x2="40" y2="15" stroke="#333"/><line x1="40.0" y1="230.0" x2="316.0" y2="20.0" stroke="#2a9d8f" stroke-width="1.5"/><line x1="40.0" y1="177.5" x2="316.0" y2="30.5" stroke="#e76f51" stroke-width="1.5"/><polyline points="155.0,230.0 155.0,116.3 189.5,116.3 189.5,97.9 213.7,97.9 213.7,85.0 230.6,85.0 230.6,76.0 242.4,76.0 242.4,69.7 250.7,69.7" fill="none" stroke="#264653" stroke-width="1.5"/><line x1="270.0" y1="55.0" x2="270.0" y2="230" stroke="#888" stroke-dasharray="3 3"/><circle cx="270.0" cy="55.0" r="3.5" fill="#264653"/><text x="262.0" y="244" font-size="11">1000</text><text x="149.0" y="244" font-size="11">u₀ = 500</text><text x="256.0" y="32.0" font-size="11" fill="#2a9d8f">y = x</text><text x="246.0" y="52.5" font-size="11" fill="#e76f51">y = 0,7x + 300</text></svg>
:::

::: piege Soustraire b au lieu du point fixe
Avec uₙ₊₁ = 0,7uₙ + 300, on pose vₙ = uₙ − 300. Cela tente parce que 300 est le nombre visible dans la formule. Mais alors vₙ₊₁ = 0,7uₙ = 0,7(vₙ + 300) = 0,7vₙ + 210 : la suite v n'est pas géométrique. Il faut soustraire le point fixe 1000, solution de ℓ = 0,7ℓ + 300.
:::

::: propriete
- Pour a = 1, la suite est arithmétique de raison b ; pour a = 0, elle est constante à partir du rang 1.
- Si a < 0 (et −1 < a), la suite converge en oscillant autour de ℓ.

Cas limite : si u₀ = ℓ, la suite est constante, égale à ℓ à tous les rangs.
:::

::: verifie
Soit u₀ = 2 et uₙ₊₁ = 0,6uₙ + 4. Déterminer uₙ en fonction de n et sa limite.

---

Point fixe : ℓ = 4 / 0,4 = 10. Donc uₙ = 10 + 0,6ⁿ(2 − 10) = 10 − 8 × 0,6ⁿ. Contrôle : u₁ = 10 − 4,8 = 5,2 = 0,6 × 2 + 4. Comme 0,6ⁿ tend vers 0, la limite est 10.
:::

::: retenir
uₙ₊₁ = a·uₙ + b : point fixe ℓ = b / (1 − a), vₙ = uₙ − ℓ géométrique de raison a, uₙ = ℓ + aⁿ(u₀ − ℓ), limite ℓ si −1 < a < 1.
:::

## 🧩 Suites homographiques

Le prix relatif d'un produit se corrige chaque année d'après le prix de l'année précédente par une formule de la forme (au + b) / (cu + d), un quotient d'expressions affines.
Comment traiter une récurrence qui n'est même plus affine ?

::: definition
Une suite **homographique** vérifie uₙ₊₁ = (a·uₙ + b) / (c·uₙ + d). Si elle converge vers ℓ, alors ℓ = (aℓ + b) / (cℓ + d) : on résout cette équation pour trouver les **points fixes**. Si elle en a deux, α et β, la suite auxiliaire vₙ = (uₙ − α) / (uₙ − β) est géométrique. Si elle n'en a qu'un, α, la suite auxiliaire vₙ = 1 / (uₙ − α) est arithmétique. On retrouve alors uₙ en fonction de vₙ, puis sa limite.
:::

::: exemple u₀ = 4 et uₙ₊₁ = (3uₙ + 2) / (uₙ + 4)
1. Points fixes : x(x + 4) = 3x + 2, soit x² + x − 2 = 0, donc x = 1 ou x = −2.
2. On pose vₙ = (uₙ − 1) / (uₙ + 2). Alors vₙ₊₁ = ((3uₙ + 2) − (uₙ + 4)) / ((3uₙ + 2) + 2(uₙ + 4)) = (2uₙ − 2) / (5uₙ + 10) = (2/5)vₙ.
3. La suite v est géométrique de raison 2/5 et de premier terme v₀ = 3/6 = 1/2 : vₙ = (1/2)(2/5)ⁿ, qui tend vers 0.
4. De vₙ(uₙ + 2) = uₙ − 1, on tire uₙ = (1 + 2vₙ) / (1 − vₙ), qui tend vers 1. Contrôle : v₁ = 0,2 et u₁ = 1,4 / 0,8 = 1,75 = (3 × 4 + 2) / (4 + 4).

:::

::: piege Prendre n'importe quel point fixe pour la limite
Les deux solutions 1 et −2 vérifient l'équation, et on choisit −2 « parce qu'elle est plus simple ». Cela tente parce que l'équation n'impose aucun ordre. Mais la limite est unique : ici 0 < vₙ ≤ 1/2, donc uₙ = (1 + 2vₙ) / (1 − vₙ) > 1 à tout rang, donc la limite ne peut pas être −2. L'équation des points fixes donne les limites possibles ; les données de la suite désignent la bonne.
:::

::: propriete
- Il faut que le dénominateur cuₙ + d ne s'annule jamais : on le vérifie sur les premiers termes puis par un encadrement ou une récurrence.
- Si la suite converge, sa limite est un point fixe ; la réciproque est fausse, une suite peut rester loin d'un point fixe sans le rejoindre.

Cas limite : si u₀ est lui-même un point fixe, la suite est constante.
:::

::: verifie
Pour uₙ₊₁ = (5uₙ − 4) / uₙ, quelle équation donne les limites possibles de la suite ?

---

On résout ℓ = (5ℓ − 4) / ℓ, c'est-à-dire ℓ² = 5ℓ − 4, soit ℓ² − 5ℓ + 4 = 0, de solutions 1 et 4. La limite, si elle existe, est l'un de ces deux nombres.
:::

::: retenir
Suite homographique : points fixes par ℓ = (aℓ + b) / (cℓ + d) ; deux points fixes ⇒ vₙ = (uₙ − α) / (uₙ − β) géométrique ; un seul ⇒ vₙ = 1 / (uₙ − α) arithmétique ; la limite est choisie parmi les points fixes grâce aux données.
:::
