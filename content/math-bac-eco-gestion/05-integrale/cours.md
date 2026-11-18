# ⚔️ Intégrale d'une fonction continue — cumuler un coût, mesurer une aire, moyenner un prix

> 💡 «L'intégrale additionne une infinité de petits changements : du coût d'un objet de plus, elle tire le coût de toute une production.»

Bienvenue, héros de l'Économie et gestion. Un directeur connaît le coût de l'objet suivant et veut le coût de mille objets ; un analyste veut le prix moyen d'une saison, ou l'aire sous une courbe de ventes. Huit étapes te mènent de la définition aux applications : l'intégrale comme différence de primitives, la relation de Chasles, la linéarité, la comparaison, l'intégration par parties, la valeur moyenne, les aires et enfin les usages économiques. On suppose acquis le calcul des primitives, des dérivées, de ln et de l'exponentielle (chapitres précédents).

## 🧭 L'intégrale comme différence de primitives

Une savonnerie connaît son coût marginal : Cm(x) = 3x² + 2 centaines de dinars par tonne produite. Combien coûte de plus le passage de 1 à 3 tonnes ? Une primitive F de Cm « remonte » du coût marginal vers un coût total, mais elle est connue à une constante près.
Comment obtenir un nombre précis malgré cette constante ?

::: definition
Soient a et b deux réels d'un intervalle I, f une fonction continue sur I et F une primitive de f sur I. L'**intégrale de f entre a et b** est le réel :

$$ ∫ₐᵇ f(t)dt = [F(t)]ₐᵇ = F(b) − F(a) $$

Ce réel **ne dépend pas de la primitive choisie** : deux primitives de f diffèrent d'une constante k, qui s'annule dans la différence (F(b) + k) − (F(a) + k). Les réels a et b sont les **bornes** ; [F(t)]ₐᵇ se lit « F(t) pris entre a et b » ; la lettre t est **muette** : ∫ₐᵇ f(t)dt = ∫ₐᵇ f(x)dx. Si a < b, on parle de l'intégrale de f **sur [a ; b]**.
:::

::: exemple Le coût marginal de la savonnerie : Cm(x) = 3x² + 2
1. Cm est continue sur ℝ, donc l'intégrale existe. Une primitive est F(x) = x³ + 2x.
2. F(3) = 27 + 6 = 33 et F(1) = 1 + 2 = 3.
3. ∫₁³ (3x² + 2)dx = F(3) − F(1) = 33 − 3 = 30 : le passage de 1 à 3 tonnes coûte 30 centaines de dinars de plus, soit 3000 dinars.
4. Autre primitive, G(x) = x³ + 2x + 5 : G(3) − G(1) = 38 − 8 = 30. Le résultat ne change pas.

:::

::: exemple Une exponentielle composée : ∫₀¹ 4x e^(x²) dx
1. Avec u(x) = x², u′(x) = 2x et (e^u)′ = u′e^u, la fonction 4x e^(x²) = 2 × u′e^u a pour primitive F(x) = 2e^(x²).
2. ∫₀¹ 4x e^(x²)dx = F(1) − F(0) = 2e − 2 ≈ 3,44.

:::

::: piege Ne retenir que F(b)
Pour la savonnerie, on écrit « le coût vaut F(3) = 33 centaines de dinars ». Cela tente parce que F est « le coût total » et que 3 est la production visée. Mais F n'est connue qu'à une constante près : avec G = F + 5, on aurait lu 38. Seule la différence F(3) − F(1) = 30 est indépendante du choix, et c'est elle qui mesure le supplément entre 1 et 3 tonnes.
:::

::: propriete
- Primitives à connaître (rappel) : xⁿ ↦ xⁿ⁺¹/(n + 1) pour n ≠ −1 ; 1/x ↦ ln x sur ]0 ; +∞[ ; eˣ ↦ eˣ ; u′eᵘ ↦ eᵘ ; u′/u ↦ ln u si u > 0 ; u′uⁿ ↦ uⁿ⁺¹/(n + 1) ; u′/√u ↦ 2√u.
- Les bornes peuvent être rangées dans n'importe quel ordre : le cas a > b est permis.
- Il faut f **continue sur tout l'intervalle** entre a et b.

Cas limite : f(x) = 1/x n'est pas continue en 0, donc ∫₋₁¹ dx/x n'existe pas : on n'écrit jamais F(1) − F(−1) avec une « primitive » de 1/x qui ne l'est pas sur tout [−1 ; 1].
:::

::: verifie
Calculer ∫₁² (2x + 1)/(x² + x) dx.

---

Avec u(x) = x² + x, u′(x) = 2x + 1 et u > 0 sur [1 ; 2], la fonction est u′/u, de primitive ln u. Donc l'intégrale vaut [ln(x² + x)]₁² = ln 6 − ln 2 = ln 3 ≈ 1,10. La fonction est continue sur [1 ; 2], car x² + x ne s'annule pas entre 1 et 2.
:::

::: retenir
∫ₐᵇ f = F(b) − F(a) pour toute primitive F de f sur un intervalle contenant a et b : la différence ne dépend pas de la primitive, alors que F(b) seule en dépend.
:::

## 🔮 Chasles, inversion des bornes et intégrale nulle

Le stock d'un entrepôt varie à la vitesse v(t) tonnes par jour. Du jour 0 au jour 3, il augmente de 6 tonnes ; du jour 3 au jour 5, il diminue de 2 tonnes. Quelle est sa variation du jour 0 au jour 5, et que dire du chemin retour, du jour 5 au jour 0 ?
Les intégrales se découpent-elles comme les trajets ?

::: propriete
Soit f continue sur un intervalle I, et a, b, c des réels de I.
- **Relation de Chasles** : l'intégrale de a à b est la somme de l'intégrale de a à c et de l'intégrale de c à b (c n'est pas forcément entre a et b).
- ∫ₐᵃ f(t)dt = 0.
- **Inversion des bornes** : l'intégrale de b à a de f est l'opposé de ∫ₐᵇ f.

Ces trois égalités viennent de F(b) − F(a) = (F(c) − F(a)) + (F(b) − F(c)), de F(a) − F(a) = 0 et de F(a) − F(b) = −(F(b) − F(a)).

Cas limite : si f change de signe, l'intégrale ne mesure pas une surface ; pour une valeur absolue, on coupe l'intervalle là où le signe change et on applique Chasles à chaque morceau.
:::

::: exemple La variation du stock : ∫₀⁵ v = ∫₀³ v + ∫₃⁵ v
1. ∫₀³ v = 6 et ∫₃⁵ v = −2.
2. Par Chasles, ∫₀⁵ v = ∫₀³ v + ∫₃⁵ v = 6 + (−2) = 4 : le stock gagne 4 tonnes en cinq jours.
3. Chemin retour : l'intégrale de 5 à 0 de v est −∫₀⁵ v = −4. Et ∫₃³ v = 0 : aucun temps ne s'écoule.

:::

::: exemple Une valeur absolue : ∫₀³ |x − 2| dx
1. |x − 2| = 2 − x pour x ≤ 2 et x − 2 pour x ≥ 2 : on coupe en 2.
2. ∫₀² (2 − x)dx = [2x − x²/2]₀² = 4 − 2 = 2.
3. ∫₂³ (x − 2)dx = [x²/2 − 2x]₂³ = (4,5 − 6) − (2 − 4) = 0,5.
4. Par Chasles, ∫₀³ |x − 2|dx = 2 + 0,5 = 2,5.

:::

::: piege Faire disparaître la valeur absolue
On écrit ∫₀³ |x − 2|dx = ∫₀³ (x − 2)dx = [x²/2 − 2x]₀³ = −1,5. Cela tente parce que la primitive de x − 2 est facile. Mais la valeur absolue change l'expression en 2 : sur [0 ; 2], |x − 2| = 2 − x, pas x − 2. Une intégrale de fonction positive ne peut pas être négative : −1,5 est donc impossible, la bonne valeur est 2,5.
:::

::: verifie
Calculer ∫₀⁵ |2x − 4| dx.

---

Le signe change en x = 2. Sur [0 ; 2], |2x − 4| = 4 − 2x et ∫₀² (4 − 2x)dx = [4x − x²]₀² = 4. Sur [2 ; 5], |2x − 4| = 2x − 4 et ∫₂⁵ (2x − 4)dx = [x² − 4x]₂⁵ = 5 − (−4) = 9. Par Chasles, l'intégrale vaut 4 + 9 = 13. Sans couper en 2, on aurait trouvé ∫₀⁵ (2x − 4)dx = 5, mauvaise réponse.
:::

::: retenir
L'intégrale de a à b est la somme de celles de a à c et de c à b, ∫ₐᵃ f = 0, et inverser les bornes change le signe ; on coupe l'intervalle au point où f change de signe pour intégrer une valeur absolue.
:::

## 🔗 Linéarité de l'intégrale

Deux produits d'une boutique ont des recettes instantanées a(t) et b(t), en milliers de dinars par mois. On connaît ∫₀⁴ a = 12 et ∫₀⁴ b = 5. La recette totale sur quatre mois est-elle la somme des deux intégrales ? Et si une prime de 2 milliers par mois s'ajoute ?
Les intégrales respectent-elles les sommes et les facteurs ?

::: propriete
Soient f et g continues sur I, a et b dans I, α et β deux réels.
- ∫ₐᵇ (f + g) = ∫ₐᵇ f + ∫ₐᵇ g.
- ∫ₐᵇ α f = α ∫ₐᵇ f.
- Donc ∫ₐᵇ (αf + βg) = α∫ₐᵇ f + β∫ₐᵇ g. Pour une constante k, ∫ₐᵇ k dx = k(b − a).

Cas limite : la linéarité ne porte que sur les sommes et les facteurs constants ; l'intégrale d'un produit f × g n'est pas ∫ f × ∫ g.
:::

::: exemple Avec des intégrales données
1. Recette totale : ∫₀⁴ (a + b) = 12 + 5 = 17 milliers de dinars.
2. Avec la prime de 2 milliers par mois : ∫₀⁴ (a + b + 2) = 17 + 2 × 4 = 25 : la constante s'intègre sur la longueur 4 de l'intervalle.
3. Autre cas : ∫₀⁶ f = 8 et ∫₀⁶ g = 3 donnent ∫₀⁶ (2f − g + 1) = 16 − 3 + 6 = 19.

:::

::: exemple Un polynôme : ∫₀² (3x² − 4x + 5)dx
1. Par linéarité, on intègre terme à terme : 3∫₀² x² − 4∫₀² x + 5∫₀² 1.
2. Une primitive est F(x) = x³ − 2x² + 5x, et F(2) = 8 − 8 + 10 = 10, F(0) = 0.
3. Donc ∫₀² (3x² − 4x + 5)dx = 10.

:::

::: piege Intégrer un produit facteur par facteur
On écrit ∫₀¹ x × x dx = ∫₀¹ x dx × ∫₀¹ x dx = 1/2 × 1/2 = 1/4. Cela tente parce que la somme se sépare. Mais ∫₀¹ x²dx = 1/3, et 1/3 ≠ 1/4. Seules les sommes et les facteurs constants se sortent de l'intégrale.
:::

::: verifie
On sait que ∫₁⁵ f = 6 et ∫₁⁵ g = −2. Calculer ∫₁⁵ (4g(x) − f(x) + 3)dx.

---

Par linéarité, l'intégrale vaut 4 × (−2) − 6 + ∫₁⁵ 3dx. La constante 3 s'intègre sur la longueur 5 − 1 = 4 : ∫₁⁵ 3dx = 12. Le résultat est −8 − 6 + 12 = −2.
:::

::: retenir
∫ₐᵇ (αf + βg) = α∫ₐᵇ f + β∫ₐᵇ g et ∫ₐᵇ k dx = k(b − a) ; la linéarité ne s'applique ni aux produits ni aux quotients de fonctions.
:::

## ⚖️ Positivité, comparaison et encadrement

Un contrôleur de gestion veut borner un coût cumulé sans le calculer : il sait seulement que le coût marginal reste entre 3 et 7 dinars sur une production de 10 à 30 unités. Peut-il en déduire un coût supplémentaire minimal et maximal ?
Que dit l'ordre des fonctions sur l'ordre des intégrales ?

::: propriete
Soient f et g continues sur [a ; b], avec **a ≤ b**.
- **Positivité** : si f ≥ 0 sur [a ; b], alors ∫ₐᵇ f ≥ 0.
- **Comparaison** : si f ≤ g sur [a ; b], alors ∫ₐᵇ f ≤ ∫ₐᵇ g.
- **Encadrement** : si m ≤ f ≤ M sur [a ; b], alors m(b − a) ≤ ∫ₐᵇ f ≤ M(b − a).

Cas limite : si les bornes sont inversées (a > b), les inégalités se retournent ; ∫₃⁰ x²dx = −∫₀³ x²dx < 0 alors que x² ≥ 0.
:::

::: exemple Le coût entre 10 et 30 unités
1. On a 3 ≤ Cm ≤ 7 sur [10 ; 30], de longueur 20.
2. Par encadrement, 3 × 20 ≤ ∫₁₀³⁰ Cm ≤ 7 × 20.
3. Le coût supplémentaire est donc compris entre 60 et 140 dinars.

:::

::: exemple Un encadrement de ln 3
1. Pour x dans [1 ; 3], 1/3 ≤ 1/x ≤ 1, et la longueur est 2.
2. Donc 2/3 ≤ ∫₁³ dx/x ≤ 2.
3. Or ∫₁³ dx/x = ln 3 : on obtient 2/3 ≤ ln 3 ≤ 2, ce qui est vrai (ln 3 ≈ 1,10).

:::

::: piege Croire qu'une intégrale positive rend f positive
Pour f(x) = x² − 1 sur [0 ; 2], ∫₀² f = [x³/3 − x]₀² = 8/3 − 2 = 2/3 > 0. Cela tente parce que la positivité va dans ce sens. Mais la réciproque est fausse : f(0) = −1 < 0, la partie négative sur [0 ; 1] est compensée par la partie positive sur [1 ; 2]. La positivité de f donne l'intégrale positive, jamais l'inverse.
:::

::: verifie
Encadrer I = ∫₀² e^(−x) dx sans la calculer, puis comparer avec sa valeur exacte.

---

La fonction e^(−x) est décroissante : sur [0 ; 2], e^(−2) ≤ e^(−x) ≤ 1, et la longueur est 2. Donc 2e^(−2) ≤ I ≤ 2, soit 0,27 ≤ I ≤ 2. La valeur exacte est I = [−e^(−x)]₀² = 1 − e^(−2) ≈ 0,86, qui est bien dans l'encadrement.
:::

::: retenir
Pour a ≤ b, f ≤ g donne ∫ₐᵇ f ≤ ∫ₐᵇ g, et m ≤ f ≤ M donne m(b − a) ≤ ∫ₐᵇ f ≤ M(b − a) ; une intégrale positive ne prouve pas que f est positive.
:::

## 🧮 Intégration par parties

Le bénéfice marginal d'une entreprise est b(x) = (2x + 1)e^(−x). Aucune primitive usuelle ne convient : ce produit d'un polynôme et d'une exponentielle ne ressemble à aucune forme u′eᵘ. Pourtant, en dérivant un produit, on retrouve des termes qui lui ressemblent.
Comment transformer une intégrale difficile en une plus simple ?

::: propriete
Soient u et v deux fonctions dérivables sur [a ; b], dont les dérivées u′ et v′ sont continues. Alors :

$$ ∫ₐᵇ u′(x)v(x)dx = [u(x)v(x)]ₐᵇ − ∫ₐᵇ u(x)v′(x)dx $$

Elle vient de (uv)′ = u′v + uv′, qu'on intègre. On choisit v facile à dériver et u′ facile à primitiver, de façon que ∫ u v′ soit plus simple que l'intégrale de départ.

Cas limite : si l'intégrale obtenue est aussi compliquée, le choix est mauvais, et on échange les rôles ; deux intégrations par parties successives peuvent être nécessaires (pour x²eˣ, par exemple).
:::

::: exemple Le bénéfice cumulé : ∫₀¹ (2x + 1)e^(−x) dx
1. On pose u′(x) = e^(−x), donc u(x) = −e^(−x), et v(x) = 2x + 1, donc v′(x) = 2.
2. Le crochet vaut [−(2x + 1)e^(−x)]₀¹ = −3e^(−1) + 1.
3. ∫₀¹ u v′ = ∫₀¹ (−2e^(−x))dx = −2(1 − e^(−1)), donc −∫₀¹ uv′ = 2(1 − e^(−1)).
4. L'intégrale vaut 1 − 3/e + 2 − 2/e = 3 − 5/e ≈ 1,16. Elle est positive, comme la fonction (2x + 1)e^(−x).

:::

::: exemple Un logarithme : ∫₁ᵉ x² ln x dx
1. On pose u′(x) = x², donc u(x) = x³/3, et v(x) = ln x, donc v′(x) = 1/x : on dérive le logarithme, qu'on ne sait pas primitiver simplement.
2. Le crochet vaut [x³ ln x /3]₁ᵉ = e³/3, car ln e = 1 et ln 1 = 0.
3. ∫₁ᵉ (x³/3)(1/x)dx = ∫₁ᵉ x²/3 dx = (e³ − 1)/9.
4. L'intégrale vaut e³/3 − (e³ − 1)/9 = (2e³ + 1)/9 ≈ 4,57.

:::

::: exemple Deux intégrations par parties : ∫₀¹ x²eˣ dx
1. On pose u′(x) = eˣ, donc u(x) = eˣ, et v(x) = x², donc v′(x) = 2x : I = [x²eˣ]₀¹ − 2∫₀¹ x eˣ dx = e − 2∫₀¹ x eˣ dx.
2. Seconde intégration par parties, avec v(x) = x : ∫₀¹ x eˣ dx = [x eˣ]₀¹ − ∫₀¹ eˣ dx = e − (e − 1) = 1.
3. I = e − 2 ≈ 0,72, positif comme x²eˣ.

:::

::: piege Oublier le signe moins devant la seconde intégrale
Pour ∫₀¹ (2x + 1)e^(−x)dx, on écrit [uv] + ∫ uv′, ce qui donne (1 − 3/e) + (−2)(1 − 1/e) = −1 − 1/e ≈ −1,37. Cela tente parce qu'on ajoute les morceaux d'une dérivée de produit. Mais la formule soustrait : −∫ uv′. Test de signe : la fonction (2x + 1)e^(−x) est positive sur [0 ; 1], son intégrale ne peut pas être négative.
:::

::: verifie
Calculer ∫₀¹ x e^(2x) dx.

---

On pose u′(x) = e^(2x), u(x) = e^(2x)/2 et v(x) = x, v′(x) = 1. Alors I = [x e^(2x)/2]₀¹ − ∫₀¹ e^(2x)/2 dx = e²/2 − [e^(2x)/4]₀¹ = e²/2 − (e² − 1)/4 = (e² + 1)/4 ≈ 2,10. L'intégrale est positive : x e^(2x) ≥ 0 sur [0 ; 1].
:::

::: retenir
∫ₐᵇ u′v = [uv]ₐᵇ − ∫ₐᵇ uv′ : on dérive le facteur qui se simplifie, on primitive l'autre, on n'oublie ni le crochet ni le signe moins.
:::

## 📊 Valeur moyenne d'une fonction

Le prix d'un article baisse au fil des mois : p(t) = 40e^(−0,1t) dinars, pour t entre 0 et 10 mois. Quel est son prix moyen sur ces dix mois ? Faire la moyenne de p(0) et p(10) ne tient pas compte de la forme de la courbe.
Comment moyenner une infinité de valeurs ?

::: definition
Soit f continue sur [a ; b], avec a < b. La **valeur moyenne** de f sur [a ; b] est le réel :

$$ f̄ = 1/(b − a) × ∫ₐᵇ f(t)dt $$

Géométriquement, l'aire sous la courbe égale celle du rectangle de largeur b − a et de hauteur f̄.
:::

::: exemple Le prix moyen sur dix mois : p(t) = 40e^(−0,1t)
1. Une primitive de p est P(t) = −400e^(−0,1t), car (e^(−0,1t))′ = −0,1e^(−0,1t).
2. ∫₀¹⁰ p = P(10) − P(0) = −400e^(−1) + 400 = 400(1 − 1/e) ≈ 252,85.
3. La valeur moyenne est 252,85/10 ≈ 25,28 dinars. Elle est entre p(10) ≈ 14,72 et p(0) = 40, comme attendu.

:::

::: exemple Le prix d'offre moyen : p(q) = 6 + 0,03q²
1. Un producteur propose le prix p(q) = 6 + 0,03q² dinars le kilo pour une quantité q de 10 à 20 tonnes.
2. ∫₁₀²⁰ p = [6q + 0,01q³]₁₀²⁰ = (120 + 80) − (60 + 10) = 130.
3. Moyenne : 130/(20 − 10) = 13 dinars le kilo.

:::

::: piege Moyenner les deux valeurs aux bornes
Pour f(x) = x² sur [0 ; 3], on écrit f̄ = (f(0) + f(3))/2 = 4,5. Cela tente parce que, pour une droite, c'est exact. Mais une courbe n'est pas une droite : ∫₀³ x²dx = 9, donc f̄ = 9/3 = 3, très différent de 4,5. Seule la formule avec l'intégrale tient compte de la forme.
:::

::: propriete
- f̄ × (b − a) = ∫ₐᵇ f : on retrouve l'intégrale en multipliant la moyenne par la longueur.
- Si m ≤ f ≤ M sur [a ; b], alors m ≤ f̄ ≤ M.
- Deux intervalles consécutifs : par Chasles, la moyenne sur [a ; c] est la moyenne des moyennes sur [a ; b] et [b ; c], **pondérée par les longueurs** de ces intervalles.

Cas limite : la valeur moyenne peut ne ressembler à aucune des valeurs aux extrémités ; pour une fonction continue, elle est atteinte en au moins un point de [a ; b] (admis).
:::

::: verifie
Un coût marginal vaut Cm(q) = 0,06q² + 4 pour q de 0 à 10. Calculer sa valeur moyenne sur [0 ; 10].

---

∫₀¹⁰ (0,06q² + 4)dq = [0,02q³ + 4q]₀¹⁰ = 20 + 40 = 60. On divise par 10 − 0 = 10 : la valeur moyenne vaut 6. Elle est entre Cm(0) = 4 et Cm(10) = 10, mais ce n'est pas 7, la moyenne des deux valeurs aux bornes.
:::

::: retenir
f̄ = (1/(b − a)) ∫ₐᵇ f : on divise l'intégrale par la longueur b − a, et on ne moyenne pas les valeurs aux bornes, sauf pour une fonction affine.
:::

## 📐 Aires sous une courbe et entre deux courbes

Un graphique de coût comporte une zone sous l'axe et une zone au-dessus. Pour mesurer la surface totale, on ne peut pas simplement additionner des intégrales : l'une est négative, l'autre positive.
Comment passer d'une intégrale à une aire ?

::: definition
Soit f continue sur [a ; b], avec a ≤ b, et C sa courbe dans un repère orthogonal. L'**aire** du domaine limité par C, l'axe des abscisses et les droites x = a et x = b est, en **unités d'aire** (u.a.), le réel ∫ₐᵇ |f(x)|dx. Une unité d'aire est l'aire du rectangle formé par les deux unités graphiques ; avec 2 cm en abscisse et 3 cm en ordonnée, 1 u.a. = 6 cm².

Pour f et g continues sur [a ; b], l'aire entre leurs courbes est ∫ₐᵇ |f(x) − g(x)|dx.
:::

::: figure La courbe de x² − 4x : un domaine sous l'axe, de 0 à 4, de 32/3 u.a., et un domaine au-dessus, de 4 à 5, de 7/3 u.a.
<svg viewBox="0 0 340 210"><title>Courbe de f(x) = x² − 4x entre 0 et 5 : un domaine sous l'axe, de 0 à 4, et un domaine au-dessus, de 4 à 5</title><polygon points="40,110 40.0,110.0 45.5,117.8 51.0,125.2 56.5,132.2 62.0,138.8 67.5,145.0 73.0,150.8 78.5,156.2 84.0,161.2 89.5,165.8 95.0,170.0 100.5,173.8 106.0,177.2 111.5,180.2 117.0,182.8 122.5,185.0 128.0,186.8 133.5,188.2 139.0,189.2 144.5,189.8 150.0,190.0 155.5,189.8 161.0,189.2 166.5,188.2 172.0,186.8 177.5,185.0 183.0,182.8 188.5,180.2 194.0,177.2 199.5,173.8 205.0,170.0 210.5,165.8 216.0,161.2 221.5,156.2 227.0,150.8 232.5,145.0 238.0,138.8 243.5,132.2 249.0,125.2 254.5,117.8 260.0,110.0 260,110" fill="#fed7aa" stroke="none"/><polygon points="260,110 260.0,110.0 261.4,108.0 262.8,105.9 264.1,103.9 265.5,101.8 266.9,99.7 268.2,97.5 269.6,95.4 271.0,93.2 272.4,91.0 273.8,88.8 275.1,86.5 276.5,84.2 277.9,81.9 279.2,79.6 280.6,77.2 282.0,74.8 283.4,72.4 284.8,69.9 286.1,67.5 287.5,65.0 288.9,62.5 290.2,60.0 291.6,57.4 293.0,54.8 294.4,52.2 295.8,49.5 297.1,46.9 298.5,44.2 299.9,41.5 301.2,38.8 302.6,36.0 304.0,33.2 305.4,30.4 306.8,27.6 308.1,24.7 309.5,21.8 310.9,18.9 312.2,15.9 313.6,13.0 315.0,10.0 315,110" fill="#bbf7d0" stroke="none"/><polyline points="40.0,110.0 42.8,114.0 45.5,117.8 48.2,121.5 51.0,125.2 53.8,128.8 56.5,132.2 59.2,135.6 62.0,138.8 64.8,141.9 67.5,145.0 70.2,147.9 73.0,150.8 75.8,153.6 78.5,156.2 81.2,158.8 84.0,161.2 86.8,163.6 89.5,165.8 92.2,167.9 95.0,170.0 97.8,171.9 100.5,173.8 103.2,175.6 106.0,177.2 108.8,178.8 111.5,180.2 114.2,181.6 117.0,182.8 119.8,183.9 122.5,185.0 125.2,185.9 128.0,186.8 130.8,187.6 133.5,188.2 136.2,188.8 139.0,189.2 141.8,189.6 144.5,189.8 147.2,189.9 150.0,190.0 152.8,189.9 155.5,189.8 158.2,189.6 161.0,189.2 163.8,188.8 166.5,188.2 169.2,187.5 172.0,186.8 174.8,185.9 177.5,185.0 180.2,183.9 183.0,182.8 185.8,181.6 188.5,180.2 191.2,178.8 194.0,177.2 196.8,175.6 199.5,173.8 202.2,171.9 205.0,170.0 207.8,168.0 210.5,165.8 213.2,163.6 216.0,161.2 218.8,158.8 221.5,156.2 224.2,153.6 227.0,150.8 229.8,147.9 232.5,145.0 235.2,141.9 238.0,138.8 240.8,135.6 243.5,132.2 246.2,128.8 249.0,125.2 251.8,121.5 254.5,117.8 257.2,113.9 260.0,110.0 262.8,105.9 265.5,101.8 268.2,97.5 271.0,93.2 273.8,88.8 276.5,84.2 279.2,79.6 282.0,74.8 284.8,69.9 287.5,65.0 290.2,60.0 293.0,54.8 295.8,49.5 298.5,44.2 301.2,38.8 304.0,33.2 306.8,27.6 309.5,21.8 312.2,15.9 315.0,10.0" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="34" y1="110" x2="334" y2="110" stroke="#0f172a" stroke-width="1.6"/><line x1="40" y1="204" x2="40" y2="6" stroke="#0f172a" stroke-width="1.6"/><polygon points="334,110 327,106.5 327,113.5" fill="#0f172a"/><polygon points="40,6 36.5,13 43.5,13" fill="#0f172a"/><line x1="40" y1="107" x2="40" y2="113" stroke="#0f172a" stroke-width="1.3"/><line x1="260" y1="107" x2="260" y2="113" stroke="#0f172a" stroke-width="1.3"/><text x="260" y="102" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="315" y1="107" x2="315" y2="113" stroke="#0f172a" stroke-width="1.3"/><text x="315" y="126" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><text x="150" y="154.0" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">aire 32/3</text><text x="287.5" y="72.0" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7/3</text><text x="95.0" y="200.0" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = f(x)</text><text x="330" y="102" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="48" y="18" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text></svg>
:::

::: exemple Sous la courbe de f(x) = x² − 4x, entre 0 et 5
1. f(x) = x(x − 4) : f ≤ 0 sur [0 ; 4] et f ≥ 0 sur [4 ; 5].
2. Sur [0 ; 4], ∫₀⁴ (4x − x²)dx = [2x² − x³/3]₀⁴ = 32 − 64/3 = 32/3.
3. Sur [4 ; 5], ∫₄⁵ (x² − 4x)dx = [x³/3 − 2x²]₄⁵ = (125/3 − 50) − (64/3 − 32) = 7/3.
4. L'aire est 32/3 + 7/3 = 13 u.a. Avec 2 cm en abscisse et 3 cm en ordonnée, c'est 13 × 6 = 78 cm².

:::

::: exemple Entre deux courbes : f(x) = x² et g(x) = x + 2
1. Les courbes se coupent quand x² = x + 2, soit x² − x − 2 = (x − 2)(x + 1) = 0 : en x = −1 et x = 2.
2. Sur [−1 ; 2], g(x) − f(x) = x + 2 − x² ≥ 0, car g est au-dessus de f entre les points d'intersection.
3. Aire = ∫₋₁² (x + 2 − x²)dx = [x²/2 + 2x − x³/3]₋₁² = 10/3 − (−7/6) = 9/2 = 4,5 u.a.

:::

::: piege Intégrer f sans valeur absolue
Pour la courbe de x² − 4x entre 0 et 5, on calcule ∫₀⁵ (x² − 4x)dx = 125/3 − 50 = −25/3 et on annonce « une aire de −25/3 ». Cela tente parce qu'on a l'intégrale de f. Mais ∫ f est algébrique : la partie sous l'axe compte négativement. Une aire n'est jamais négative : la bonne valeur est 13, en coupant au changement de signe.
:::

::: verifie
Calculer l'aire, en cm², du domaine entre les courbes de f(x) = √x et g(x) = x² sur [0 ; 1], avec une unité graphique de 3 cm sur chaque axe.

---

Pour x dans [0 ; 1], x² ≤ x ≤ √x, donc f ≥ g sur [0 ; 1]. L'aire vaut ∫₀¹ (√x − x²)dx = [2x√x/3 − x³/3]₀¹ = 2/3 − 1/3 = 1/3 u.a. Une unité d'aire mesure 3 × 3 = 9 cm², donc l'aire est 9/3 = 3 cm².
:::

::: retenir
L'aire entre une courbe et l'axe est ∫ₐᵇ |f| et l'aire entre deux courbes est ∫ₐᵇ |f − g| : on coupe aux changements de signe, puis on convertit les u.a. en cm² par le produit des unités graphiques.
:::

## 💰 Applications économiques : du coût marginal au coût total

Le coût marginal est la dérivée du coût total : il donne le coût de l'unité suivante. Inversement, le coût total à x unités est le coût fixe plus l'accumulation des coûts marginaux de 0 à x. L'intégrale sert ainsi à reconstruire un total ; elle sert aussi à calculer une probabilité ou un indice d'inégalité.
Comment une même formule sert-elle à tant de situations ?

::: propriete
- **Coût total** : si Cm = C′ est le coût marginal et C(0) le coût fixe, alors C(x) = C(0) + ∫₀ˣ Cm(t)dt. Les unités doivent être les mêmes avant d'additionner.
- **Densité de probabilité** : si f ≥ 0 est continue sur un intervalle I et d'intégrale égale à 1 sur I tout entier, la probabilité que X soit entre a et b (dans I) est ∫ₐᵇ f(x)dx.
- **Courbe de Lorentz** : une fonction F croissante sur [0 ; 1], avec F(0) = 0 et F(1) = 1, décrit la répartition d'une masse salariale (F(x) = part de la masse salariale reçue par la part x des salariés les moins payés) ; sa courbe reste sous la diagonale (F(x) ≤ x). L'**indicateur de Gini** est γ = 2∫₀¹ (x − F(x))dx : de 0 (égalité parfaite) à 1.

Cas limite : une densité doit avoir ∫ = 1 sur son intervalle, sinon ce n'est pas une densité ; un indicateur de Gini proche de 0 signale une répartition égalitaire, proche de 1 une répartition inégalitaire.
:::

::: exemple Du coût marginal au coût total
1. Une fonderie a pour coût marginal Cm(t) = 3t² − 12t + 15 centaines de dinars par tonne, pour t en tonnes, et des coûts fixes de 2000 dinars.
2. ∫₀⁴ Cm(t)dt = [t³ − 6t² + 15t]₀⁴ = 64 − 96 + 60 = 28 centaines de dinars, soit 2800 dinars.
3. Coût total de 4 tonnes : C(4) = 2000 + 2800 = 4800 dinars.

:::

::: exemple Une probabilité : f(x) = 3x²/64 sur [0 ; 4]
1. Les ventes X d'une semaine, en milliers d'unités, ont pour densité f(x) = 3x²/64 sur [0 ; 4]. ∫₀⁴ 3x²/64 dx = [x³/64]₀⁴ = 1 : f est bien une densité (elle est positive).
2. Probabilité de vendre moins de 2 milliers d'unités : ∫₀² 3x²/64 dx = 8/64 = 1/8.
3. Probabilité d'en vendre plus de 3 milliers : ∫₃⁴ 3x²/64 dx = (64 − 27)/64 = 37/64 ≈ 0,58.

:::

::: exemple Un indicateur de Gini : F(x) = x³
1. F est croissante sur [0 ; 1], F(0) = 0, F(1) = 1 et x³ ≤ x sur [0 ; 1] : c'est une courbe de Lorentz.
2. ∫₀¹ x dx = 1/2 et ∫₀¹ x³dx = 1/4.
3. γ = 2 × (1/2 − 1/4) = 1/2 : la répartition est plutôt inégalitaire.

:::

::: piege Additionner des unités différentes
Pour la fonderie, on écrit C(4) = 2000 + 28 = 2028 dinars. Cela tente parce que les deux nombres sont sous les yeux. Mais 28 est exprimé en centaines de dinars et 2000 en dinars : il faut convertir 28 centaines en 2800 dinars. Le bon total est 4800 dinars.
:::

::: verifie
Un atelier a pour coût marginal Cm(t) = 12t + 30 dizaines de dinars par tonne et des coûts fixes de 500 dinars. Calculer son coût total pour 5 tonnes.

---

∫₀⁵ (12t + 30)dt = [6t² + 30t]₀⁵ = 150 + 150 = 300 dizaines de dinars, soit 3000 dinars. Le coût total est 500 + 3000 = 3500 dinars. Le résultat 500 + 300 = 800 oublie la conversion des dizaines en dinars.
:::

::: retenir
C(x) = C(0) + ∫₀ˣ Cm ; une densité vérifie ∫ = 1 et donne P(a ≤ X ≤ b) = ∫ₐᵇ f ; γ = 2∫₀¹ (x − F(x))dx mesure l'inégalité ; dans tous les cas, on convertit les unités avant d'additionner.
:::
