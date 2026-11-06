# ⚔️ Calcul intégral — remonter la pente jusqu'à l'aire

> 💡 «Une intégrale, c'est une primitive qui a fait ses comptes : deux valeurs soustraites, et tout un cumul mesuré.»

Bienvenue, héros de la section Sciences de l'informatique. Bernhard Riemann (1826-1866) a défini l'intégrale comme la limite de sommes d'aires de petits rectangles ; ton arme est plus directe : la primitive. Huit notions te mènent de la définition d'une intégrale à l'approximation d'une aire par un programme : le calcul par une primitive, Chasles et la linéarité, la reconnaissance des formes avec ln et exp, l'intégration par parties, les inégalités, la valeur moyenne, les aires planes et la méthode des rectangles. On suppose acquis les primitives (chapitre 4), le logarithme (chapitre 6), le théorème d'encadrement (chapitre 1) et la fonction exponentielle (chapitre 7), utilisée ici comme un outil.

## 🏰 L'intégrale : F(b) − F(a), quelle que soit la primitive

Au chapitre 4, tu as vu qu'une fonction continue a une infinité de primitives, qui diffèrent d'une constante. Prends f(x) = 3x² − 4x + 1, avec les primitives F(x) = x³ − 2x² + x et G(x) = x³ − 2x² + x + 7. On trouve F(2) − F(0) = 2 − 0 = 2, et G(2) − G(0) = 9 − 7 = 2.
La différence est la même avec les deux primitives. Peut-on lui donner un nom, et pour quelles fonctions a-t-elle un sens ?

::: definition
**Intégrale.** Soit f continue sur un intervalle I, a et b deux réels de I, et F une primitive de f sur I. L'**intégrale de f entre a et b** est le réel

$$ ∫ₐᵇ f(x)dx = [F(x)]ₐᵇ = F(b) − F(a) $$

Les réels a et b sont les **bornes** ; [F(x)]ₐᵇ se lit « F(x) pris entre a et b » ; la lettre x est une **variable muette** : ∫ₐᵇ f(x)dx = ∫ₐᵇ f(t)dt.
:::

Le choix de F ne compte pas : deux primitives diffèrent d'une constante k, qui disparaît dans (F(b) + k) − (F(a) + k). Et une fonction continue sur [a ; b] y admet toujours une primitive : l'intégrale existe.

::: exemple Calculer une intégrale, avec des bornes dans n'importe quel ordre

1. I = ∫₁² (6x² − 4x + 1)dx : on primitive terme à terme, F(x) = 2x³ − 2x² + x, donc I = F(2) − F(1) = 10 − 1 = 9.
2. J = ∫₃⁵ dt/(t − 1) : t − 1 > 0 sur [3 ; 5], une primitive est ln(t − 1), donc J = ln 4 − ln 2 = ln 2. La lettre t est muette.
3. L = ∫₀¹ e^{2x}dx : comme (e^{2x}/2)′ = e^{2x}, L = (e² − 1)/2.
4. M = ∫₂⁰ 3x²dx = [x³]₂⁰ = 0 − 8 = −8 : la formule F(b) − F(a) vaut aussi quand a > b.

:::

::: piege Intégrer à travers un point où f n'existe pas
Pour ∫₀³ dx/(x − 2), on écrit [ln|x − 2|]₀³ = ln 1 − ln 2 = −ln 2. Cela tente parce que ln|x − 2| est une primitive de 1/(x − 2) de chaque côté de 2. Mais 1/(x − 2) n'est pas définie en 2, qui est dans [0 ; 3] : f n'est pas continue sur [0 ; 3], la définition ne s'applique pas et l'intégrale n'existe pas. Pour que ∫ₐᵇ dx/(x − 2) existe, a et b doivent être du même côté de 2.
:::

::: verifie
Pour quels réels a l'intégrale ∫ₐ⁵ dt/(t + 1) existe-t-elle ? La calculer pour a = 1.

---

La fonction t ↦ 1/(t + 1) est continue sauf en −1. Comme 5 > −1, le segment entre a et 5 ne doit pas contenir −1, donc a > −1. Pour a = 1, t + 1 > 0 et une primitive est ln(t + 1) : l'intégrale vaut ln 6 − ln 2 = ln 3.
:::

::: retenir
∫ₐᵇ f(x)dx = [F(x)]ₐᵇ = F(b) − F(a) pour toute primitive F d'une fonction f continue entre les bornes ; elle ne dépend pas de F, n'existe que si f est continue entre a et b, et sa variable est muette.
:::

## 🧮 Chasles et linéarité : couper et recombiner

La fonction x ↦ |x − 2| n'a pas de formule unique : elle vaut 2 − x pour x ≤ 2 et x − 2 pour x ≥ 2, et aucune ligne de la table de primitives ne la donne d'un bloc.
Comment calculer ∫₀⁵ |x − 2|dx ? Et que devient une intégrale quand on échange les bornes, ou quand on additionne deux fonctions ?

::: exemple Couper là où le signe change : ∫₀⁵ |x − 2|dx

1. Sur [0 ; 2], x − 2 ≤ 0, donc |x − 2| = 2 − x ; sur [2 ; 5], |x − 2| = x − 2.
2. Si F est une primitive de |x − 2|, alors F(5) − F(0) = (F(2) − F(0)) + (F(5) − F(2)) : l'intégrale sur [0 ; 5] est la somme des intégrales sur [0 ; 2] et [2 ; 5].
3. ∫₀² (2 − x)dx = [2x − x²/2]₀² = 4 − 2 = 2 et ∫₂⁵ (x − 2)dx = [x²/2 − 2x]₂⁵ = (12,5 − 10) − (2 − 4) = 4,5.
4. Donc ∫₀⁵ |x − 2|dx = 2 + 4,5 = 6,5. Contrôle : ce sont deux triangles rectangles d'aires 2 × 2/2 = 2 et 3 × 3/2 = 4,5 ✓.

:::

::: exemple Additionner pour simplifier : ∫₀¹ x/(x + 1)dx

1. On connaît I = ∫₀¹ dx/(x + 1) = ln 2. On cherche J = ∫₀¹ x/(x + 1)dx, sans primitive immédiate.
2. Par linéarité, J + I = ∫₀¹ (x + 1)/(x + 1)dx = ∫₀¹ 1dx = 1.
3. Donc J = 1 − ln 2 ≈ 0,31. Contrôle : sur [0 ; 1], 0 ≤ x/(x + 1) ≤ 1/2, donc J est bien entre 0 et 1/2.
4. Avec des données : si ∫₁⁴ f = 7 et ∫₆⁴ f = −2, alors ∫₄⁶ f = 2 (bornes échangées) et ∫₁⁶ f = 7 + 2 = 9 (Chasles).

:::

::: piege Intégrer un produit comme un produit d'intégrales
Pour ∫₀¹ x × x dx, on écrit (∫₀¹ x dx) × (∫₀¹ x dx) = 1/2 × 1/2 = 1/4. Cela tente parce que la linéarité distribue sur une somme. Mais ∫₀¹ x² dx = [x³/3]₀¹ = 1/3 ≠ 1/4. La linéarité ne parle que des sommes et des facteurs constants, jamais d'un produit de fonctions.
:::

::: propriete
**Propriétés.** f et g sont continues sur un intervalle I ; a, k, b, s, t sont des réels de I ; α et β sont des réels.

- ∫ₐᵃ f(x)dx = 0 ;
- **bornes échangées** : ∫ₛᵗ f(x)dx = −∫ₜˢ f(x)dx ;
- **relation de Chasles** : ∫ₐᵏ f(x)dx + ∫ₖᵇ f(x)dx = ∫ₐᵇ f(x)dx ;
- **linéarité** : ∫ₐᵇ (αf + βg)(x)dx = α∫ₐᵇ f(x)dx + β∫ₐᵇ g(x)dx.

Elles viennent d'une primitive F : F(a) − F(a) = 0, F(t) − F(s) = −(F(s) − F(t)), (F(k) − F(a)) + (F(b) − F(k)) = F(b) − F(a), et αF + βG est une primitive de αf + βg. Cas limite : k n'a pas besoin d'être entre a et b.
:::

::: verifie
Calculer ∫₀⁴ |x − 3|dx.

---

|x − 3| = 3 − x sur [0 ; 3] et x − 3 sur [3 ; 4], donc on coupe en 3 (Chasles). ∫₀³ (3 − x)dx = [3x − x²/2]₀³ = 9 − 4,5 = 4,5 et ∫₃⁴ (x − 3)dx = [x²/2 − 3x]₃⁴ = (8 − 12) − (4,5 − 9) = 0,5. Le total est 5, ce que confirment deux triangles d'aires 4,5 et 0,5.
:::

::: retenir
Les bornes échangées changent le signe, Chasles coupe un intervalle en deux (là où la formule change) et la linéarité s'applique à une somme et à un facteur constant, jamais à un produit.
:::

## 🧩 Reconnaître la forme pour primitiver

Voici deux intégrales : ∫₀¹ (2x + 1)e^{x²+x}dx et ∫₁² (2x + 3)/(x² + 3x)dx. Aucune ligne de la table ne les donne telles quelles.
Pourtant chacune cache la dérivée d'une composée, comme au chapitre 4 (u′uⁿ) et au chapitre 6 (u′/u). Comment la reconnaître, puis calculer F(b) − F(a) sans se tromper de facteur ?

::: exemple Reconnaître u′, compenser, évaluer

1. A = ∫₀¹ (2x + 1)e^{x²+x}dx : on pose u(x) = x² + x, donc u′(x) = 2x + 1 et f = u′e^u. Une primitive est F(x) = e^{x²+x}, d'où A = F(1) − F(0) = e² − 1.
2. B = ∫₁² (2x + 3)/(x² + 3x)dx : u(x) = x² + 3x > 0 sur [1 ; 2] et u′(x) = 2x + 3, donc f = u′/u et F(x) = ln(x² + 3x). B = ln 10 − ln 4 = ln(5/2).
3. C = ∫₀¹ x e^{−x²}dx : u(x) = −x², donc u′(x) = −2x. Il manque le facteur −2, une constante : x e^{−x²} = (−1/2)u′e^u et F(x) = −(1/2)e^{−x²}. D'où C = −(1/2)(e^{−1} − 1) = (1 − 1/e)/2.
4. Contrôle de C en dérivant : F′(x) = −(1/2) × (−2x)e^{−x²} = x e^{−x²} ✓.

:::

::: exemple Réécrire avant de primitiver : (x² + 3x + 3)/(x + 1)

1. Aucune forme directe. On cherche a, b, c tels que (x² + 3x + 3)/(x + 1) = ax + b + c/(x + 1). En multipliant par x + 1 : x² + 3x + 3 = ax² + (a + b)x + (b + c).
2. Deux polynômes égaux ont les mêmes coefficients : a = 1, a + b = 3 donc b = 2, et b + c = 3 donc c = 1.
3. Sur ]−1 ; +∞[, la fonction est x + 2 + 1/(x + 1), et ∫₀² f(x)dx = [x²/2 + 2x + ln(x + 1)]₀² = 6 + ln 3.

:::

::: piege Poser u sans compenser le facteur
Pour ∫₀¹ x e^{x²}dx, on pose u = x² et l'on écrit [e^{x²}]₀¹ = e − 1. Cela tente parce que la forme u′e^u saute aux yeux. Mais u′ = 2x et l'intégrande ne contient que x : (e^{x²})′ = 2x e^{x²}, le double de l'intégrande. Comme f = (1/2)u′e^u, la bonne valeur est (e − 1)/2.
:::

Lues à l'envers, les formules de dérivation d'une composée donnent, pour u dérivable de dérivée continue :

| f                       | une primitive                   | condition               |
| ----------------------- | ------------------------------- | ----------------------- |
| u′uⁿ (n entier, n ≠ −1) | uⁿ⁺¹/(n + 1)                    | u ≠ 0 sur I si n ≤ −2   |
| u′/u                    | ln(u) si u > 0, ln(−u) si u < 0 | u ne s'annule pas sur I |
| u′e^u                   | e^u                             | aucune                  |
| u′/√u                   | 2√u                             | u > 0 sur I             |

::: propriete
**Méthode.** On repère u (contenu d'une parenthèse, d'un exposant ou d'un dénominateur), on calcule u′, on compare avec l'intégrande en compensant un facteur **constant**, on contrôle en dérivant, puis on calcule F(b) − F(a). Cas limite : u′/u² a pour primitive −1/u, jamais un logarithme ; et si le facteur manquant dépend de x, la forme est absente.
:::

::: verifie
Calculer ∫₀¹ x²/(x³ + 2)dx.

---

On pose u(x) = x³ + 2, positif sur [0 ; 1], avec u′(x) = 3x². Il manque le facteur constant 3 : x²/(x³ + 2) = (1/3) × u′/u, de primitive (1/3)ln(x³ + 2). L'intégrale vaut (1/3)(ln 3 − ln 2) = (1/3)ln(3/2) ≈ 0,14.
:::

::: retenir
On reconnaît u′uⁿ, u′/u, u′e^u ou u′/√u en posant u et en compensant un facteur constant ; sinon on réécrit (identification des coefficients), on primitive, on contrôle en dérivant, puis on soustrait F(a) à F(b).
:::

## 🔄 L'intégration par parties : un produit à la fois

La dérivée du produit x sin x est sin x + x cos x. Intégrons cette égalité entre 0 et π/2 : [x sin x]₀^{π/2} = π/2, donc ∫₀^{π/2} sin x dx + ∫₀^{π/2} x cos x dx = π/2. Comme ∫₀^{π/2} sin x dx = [−cos x]₀^{π/2} = 1, on obtient ∫₀^{π/2} x cos x dx = π/2 − 1.
Une intégrale sans primitive visible s'est ramenée à une autre que l'on sait calculer : peut-on en faire une règle ?

::: definition
**Intégration par parties.** Soient u et v dérivables sur un intervalle I, de dérivées continues, et a, b deux réels de I :

$$ ∫ₐᵇ u(x)v′(x)dx = [u(x)v(x)]ₐᵇ − ∫ₐᵇ u′(x)v(x)dx $$

Elle vient de (uv)′ = u′v + uv′, intégrée entre a et b.
:::

::: exemple Choisir u et v′, puis dérouler

1. ∫₁ᵉ ln x dx : on pose u = ln x et v′ = 1, donc u′ = 1/x et v = x (on dérive ln, qui n'a pas de primitive connue). On obtient [x ln x]₁ᵉ − ∫₁ᵉ 1dx = e − (e − 1) = 1.
2. ∫₀¹ x²e^{−x}dx : on pose u = x² et v′ = e^{−x}, donc u′ = 2x et v = −e^{−x}. On obtient [−x²e^{−x}]₀¹ + 2∫₀¹ x e^{−x}dx = −1/e + 2K.
3. Pour K = ∫₀¹ x e^{−x}dx : u = x et v = −e^{−x} donnent [−x e^{−x}]₀¹ + ∫₀¹ e^{−x}dx = −1/e + (1 − 1/e) = 1 − 2/e. Un second passage était nécessaire, car x² demande deux dérivations pour disparaître.
4. Donc ∫₀¹ x²e^{−x}dx = −1/e + 2(1 − 2/e) = 2 − 5/e.

:::

::: exemple Une relation de récurrence : Jₙ = ∫₁ᵉ (ln x)ⁿ dx

1. On pose u(x) = (ln x)ⁿ⁺¹ et v′(x) = 1, donc u′(x) = (n + 1)(ln x)ⁿ × 1/x et v(x) = x.
2. Le crochet donne [x(ln x)ⁿ⁺¹]₁ᵉ = e, car ln e = 1 et ln 1 = 0 ; dans l'intégrale, x × (1/x) se simplifie : Jₙ₊₁ = e − (n + 1)Jₙ.
3. Avec J₀ = ∫₁ᵉ 1dx = e − 1 : J₁ = e − J₀ = 1 (on retrouve l'exemple 1) et J₂ = e − 2J₁ = e − 2.

:::

::: piege Écrire « + » devant l'intégrale restante
Pour ∫₀^{π/2} x cos x dx, on pose u = x, v′ = cos x et l'on écrit [x sin x]₀^{π/2} + ∫₀^{π/2} sin x dx = π/2 + 1. Cela tente parce que la dérivée d'un produit est une somme. Mais la formule porte un signe moins : [x sin x]₀^{π/2} − ∫₀^{π/2} sin x dx = π/2 − 1, la valeur trouvée à l'ouverture.
:::

::: propriete
**Choisir u et v′.** On prend pour u le facteur qui se simplifie quand on le dérive (xⁿ, ln x) et pour v′ celui dont on connaît une primitive (eˣ, sin, cos). Un polynôme de degré n demande n passages. Cas limite : pour ln x seul, on prend v′ = 1.
:::

::: verifie
Calculer ∫₀^π x sin x dx.

---

On pose u = x et v′ = sin x, donc u′ = 1 et v = −cos x. La formule donne [−x cos x]₀^π − ∫₀^π (−cos x)dx = π + ∫₀^π cos x dx = π + [sin x]₀^π = π + 0 = π. Le signe moins devant l'intégrale et le signe de v se compensent.
:::

::: retenir
∫ₐᵇ uv′ = [uv]ₐᵇ − ∫ₐᵇ u′v : on dérive le facteur qui se simplifie, on primitive l'autre, on garde le signe moins et l'on répète si besoin ; avec un entier n, on obtient une relation entre Iₙ₊₁ et Iₙ.
:::

## 🛡️ Positivité et comparaison : encadrer sans calculer

L'intégrale ∫₀¹ dx/(1 + x⁴) n'a pas de primitive que l'on sache écrire. On peut pourtant la situer : sur [0 ; 1], 1 ≤ 1 + x⁴ ≤ 2, donc 1/2 ≤ 1/(1 + x⁴) ≤ 1.
Que peut-on en tirer pour l'intégrale, sans la calculer ?

::: exemple Du signe de f au signe de l'intégrale

1. Soit f(x) = 1/(1 + x⁴) > 0 et F une primitive de f. Alors F′ = f > 0, F est croissante, donc F(1) ≥ F(0) : ∫₀¹ f ≥ 0. Avec les bornes échangées, ∫₁⁰ f = F(0) − F(1) ≤ 0.
2. Comparaison : sur [0 ; 1], f(x) − 1/2 ≥ 0, donc ∫₀¹ (f(x) − 1/2)dx ≥ 0. Par linéarité, ∫₀¹ f ≥ ∫₀¹ (1/2)dx = 1/2. De même, 1 − f(x) ≥ 0 donne ∫₀¹ f ≤ 1.
3. Donc 1/2 ≤ ∫₀¹ dx/(1 + x⁴) ≤ 1.

:::

::: exemple Une suite d'intégrales : Jₙ = ∫₁ᵉ (ln x)ⁿ dx, avec Jₙ₊₁ = e − (n + 1)Jₙ

1. Sur [1 ; e], 0 ≤ ln x ≤ 1. En multipliant par (ln x)ⁿ ≥ 0 : 0 ≤ (ln x)ⁿ⁺¹ ≤ (ln x)ⁿ. On intègre : 0 ≤ Jₙ₊₁ ≤ Jₙ, la suite est positive et décroissante.
2. De la relation, (n + 1)Jₙ = e − Jₙ₊₁ ≤ e, car Jₙ₊₁ ≥ 0. Donc 0 ≤ Jₙ ≤ e/(n + 1).
3. Comme e/(n + 1) tend vers 0, le théorème d'encadrement donne lim Jₙ = 0.

:::

::: piege Croire que ∫ ≥ 0 entraîne f ≥ 0
Pour f(x) = x sur [−1 ; 2], ∫₋₁² x dx = [x²/2]₋₁² = 2 − 1/2 = 3/2 ≥ 0, et l'on conclut « f est positive ». Cela tente parce que la positivité de f donne celle de l'intégrale. Mais f(−1) = −1 < 0 : la partie négative sur [−1 ; 0] est compensée par la partie positive. L'implication ne se lit que dans un sens.
:::

::: propriete
**Positivité et comparaison.** f et g sont continues sur [a ; b], avec a ≤ b.

- Si f(x) ≥ 0 pour tout x de [a ; b], alors ∫ₐᵇ f(x)dx ≥ 0.
- Si f(x) ≤ g(x) pour tout x de [a ; b], alors ∫ₐᵇ f(x)dx ≤ ∫ₐᵇ g(x)dx.

Cas limite : la condition a ≤ b est essentielle. Si a > b, échanger les bornes change le signe des deux membres et les inégalités se retournent.
:::

::: verifie
Encadrer K = ∫₀¹ dx/(2 + x²).

---

Sur [0 ; 1], 2 ≤ 2 + x² ≤ 3, donc 1/3 ≤ 1/(2 + x²) ≤ 1/2 (l'inverse renverse l'ordre). On intègre sur un intervalle de longueur 1 : 1/3 ≤ K ≤ 1/2.
:::

::: retenir
Pour a ≤ b, une fonction positive a une intégrale positive et f ≤ g entraîne ∫f ≤ ∫g ; on encadre l'intégrande, puis on intègre. La réciproque est fausse, et avec les bornes échangées le sens se retourne.
:::

## 🎯 Valeur moyenne : l'inégalité et l'égalité de la moyenne

Un robot avance avec la vitesse v(t) = 6√t (en m/s) pendant 4 secondes. Sa position x vérifie x′ = v, donc la distance parcourue est ∫₀⁴ 6√t dt = [4t√t]₀⁴ = 32 m, et sa vitesse moyenne est 32/4 = 8 m/s.
À quel instant la vitesse instantanée vaut-elle exactement 8 m/s ? Un tel instant existe-t-il pour toute fonction continue ?

::: definition
**Valeur moyenne.** Soit f continue sur I, a et b deux réels distincts de I. La **valeur moyenne** de f sur [a ; b] est le réel

$$ f̄ = (1/(b − a)) ∫ₐᵇ f(t)dt = (F(b) − F(a))/(b − a) $$

On lit « f barre ».
:::

::: exemple Valeur moyenne et instant correspondant

1. Pour le robot, f̄ = 32/4 = 8. La vitesse vaut 8 quand 6√c = 8, soit √c = 4/3 et c = 16/9 ≈ 1,78, qui est bien dans [0 ; 4].
2. f(x) = 1/x sur [1 ; 4] : ∫₁⁴ dx/x = ln 4, donc f̄ = (ln 4)/3 ≈ 0,46. Le réel c vérifie 1/c = (ln 4)/3, soit c = 3/ln 4 ≈ 2,16, dans [1 ; 4].
3. f(x) = cos 2x sur [0 ; π] : f̄ = (1/π)[sin 2x/2]₀^π = 0. La valeur moyenne est nulle bien que f ne le soit pas ; c = π/4 convient, car cos(π/2) = 0.

:::

::: piege Prendre la demi-somme des valeurs extrêmes
Pour f(x) = 1/x sur [1 ; 4], on écrit f̄ = (f(1) + f(4))/2 = (1 + 1/4)/2 = 0,625. Cela tente parce que « moyenne » évoque « milieu des extrêmes ». Mais f̄ = (ln 4)/3 ≈ 0,46 : la fonction passe plus de temps près de ses petites valeurs, et la demi-somme n'est la moyenne que pour une fonction affine.
:::

::: propriete
Soit f continue sur [a ; b], avec a < b.

- **Inégalité de la moyenne** : si m ≤ f(x) ≤ M sur [a ; b], alors m ≤ f̄ ≤ M, c'est-à-dire m(b − a) ≤ ∫ₐᵇ f(t)dt ≤ M(b − a). On intègre m ≤ f ≤ M.
- **Égalité de la moyenne** : il existe au moins un réel c de [a ; b] tel que ∫ₐᵇ f(t)dt = (b − a)f(c), c'est-à-dire f̄ = f(c). Preuve : le théorème des accroissements finis appliqué à F donne F(b) − F(a) = (b − a)F′(c) = (b − a)f(c).

Cas limite : ce réel c n'est pas forcément unique, ni forcément le milieu de [a ; b].
:::

::: verifie
Calculer la valeur moyenne de f(x) = x² − 2x + 3 sur [0 ; 3], puis trouver les réels c de [0 ; 3] tels que f(c) = f̄.

---

∫₀³ (x² − 2x + 3)dx = [x³/3 − x² + 3x]₀³ = 9 − 9 + 9 = 9, donc f̄ = 9/3 = 3. Puis c² − 2c + 3 = 3 donne c(c − 2) = 0, soit c = 0 ou c = 2 : les deux sont dans [0 ; 3], l'égalité de la moyenne affirme seulement qu'il en existe au moins un.
:::

::: retenir
f̄ = (1/(b − a))∫ₐᵇ f ; si m ≤ f ≤ M, alors m ≤ f̄ ≤ M ; et il existe c de [a ; b] avec f(c) = f̄, par le théorème des accroissements finis appliqué à une primitive.
:::

## 📐 Aires planes : ∫|f| et ∫|g − f|

Pour f(x) = x² − 2x sur [0 ; 3], on trouve ∫₀³ f = [x³/3 − x²]₀³ = 9 − 9 = 0. Pourtant la courbe ne reste pas sur l'axe : elle passe sous l'axe sur [0 ; 2], puis au-dessus sur [2 ; 3].
Une aire n'est jamais nulle quand la partie n'est pas vide. Que mesure alors l'intégrale, et laquelle mesure l'aire ?

Le plan est rapporté à un repère orthonormé. L'**unité d'aire** (u.a) est l'aire du carré de côté 1 : si l'unité de longueur est 2 cm, 1 u.a = 4 cm².

::: exemple Découper là où le signe change : f(x) = x² − 2x sur [0 ; 3]

1. f(x) = x(x − 2) est négative sur [0 ; 2] et positive sur [2 ; 3] ; une primitive est F(x) = x³/3 − x².
2. ∫₀² f = F(2) − F(0) = (8/3 − 4) − 0 = −4/3 : négatif, car la courbe est sous l'axe. ∫₂³ f = F(3) − F(2) = 0 − (−4/3) = 4/3.
3. Chaque partie a pour aire la valeur absolue de son intégrale : 4/3 + 4/3 = 8/3 u.a, alors que le bilan ∫₀³ f = −4/3 + 4/3 = 0.
4. Avec une unité de 2 cm, 8/3 u.a = (8/3) × 4 = 32/3 cm² ≈ 10,7 cm².

:::

::: propriete
**Théorème (aire sous une courbe).** f est continue sur [a ; b] (a < b). L'aire de la partie limitée par la courbe de f, l'axe des abscisses et les droites x = a et x = b est A = ∫ₐᵇ |f(x)|dx. En particulier : A = ∫ₐᵇ f(x)dx si f ≥ 0 ; A = −∫ₐᵇ f(x)dx si f ≤ 0 ; sinon on coupe là où f change de signe.

**Théorème (aire entre deux courbes).** f et g sont continues sur [a ; b]. L'aire de la partie limitée par leurs courbes et les droites x = a et x = b est A = ∫ₐᵇ |g(x) − f(x)|dx ; si f ≤ g, c'est le domaine D = {M(x ; y) : a ≤ x ≤ b et f(x) ≤ y ≤ g(x)} et A = ∫ₐᵇ (g(x) − f(x))dx.
:::

::: figure Les courbes C_f de f(x) = x² et C_g de g(x) = 2x se croisent en x = 0 et en x = 2 : on découpe [−1 ; 3] en trois, où l'écart g − f change de signe
<svg viewBox="0 0 340 245"><title>Courbes de x ↦ x² et x ↦ 2x sur [−1 ; 3] : trois parties colorées de part et d’autre des croisements en 0 et en 2</title><line x1="18.3" y1="194.0" x2="315.9" y2="194.0" stroke="#0f172a" stroke-width="1.6"/><line x1="102.0" y1="235.8" x2="102.0" y2="9.7" stroke="#0f172a" stroke-width="1.6"/><polygon points="315.9,194.0 307.9,190.0 307.9,198.0" fill="#0f172a"/><polygon points="102.0,9.7 98.0,17.7 106.0,17.7" fill="#0f172a"/><polygon points="40.0,175.0 41.6,175.9 43.1,176.9 44.6,177.7 46.2,178.6 47.8,179.5 49.3,180.3 50.9,181.1 52.4,181.8 53.9,182.6 55.5,183.3 57.1,184.0 58.6,184.7 60.1,185.3 61.7,186.0 63.2,186.6 64.8,187.2 66.3,187.7 67.9,188.3 69.4,188.8 71.0,189.2 72.5,189.7 74.1,190.2 75.7,190.6 77.2,191.0 78.8,191.3 80.3,191.7 81.8,192.0 83.4,192.3 85.0,192.6 86.5,192.8 88.0,193.0 89.6,193.2 91.1,193.4 92.7,193.6 94.2,193.7 95.8,193.8 97.4,193.9 98.9,194.0 100.5,194.0 102.0,194.0 102.0,194.0 100.5,194.9 98.9,195.9 97.4,196.8 95.8,197.8 94.2,198.8 92.7,199.7 91.1,200.7 89.6,201.6 88.0,202.6 86.5,203.5 85.0,204.4 83.4,205.4 81.8,206.3 80.3,207.3 78.8,208.2 77.2,209.2 75.7,210.2 74.1,211.1 72.5,212.1 71.0,213.0 69.4,213.9 67.9,214.9 66.3,215.8 64.8,216.8 63.2,217.8 61.7,218.7 60.1,219.7 58.6,220.6 57.1,221.6 55.5,222.5 53.9,223.4 52.4,224.4 50.9,225.3 49.3,226.3 47.8,227.2 46.2,228.2 44.6,229.2 43.1,230.1 41.6,231.1 40.0,232.0" fill="#0f6e56" fill-opacity="0.22"/><polygon points="102.0,194.0 105.1,192.1 108.2,190.2 111.3,188.3 114.4,186.4 117.5,184.5 120.6,182.6 123.7,180.7 126.8,178.8 129.9,176.9 133.0,175.0 136.1,173.1 139.2,171.2 142.3,169.3 145.4,167.4 148.5,165.5 151.6,163.6 154.7,161.7 157.8,159.8 160.9,157.9 164.0,156.0 167.1,154.1 170.2,152.2 173.3,150.3 176.4,148.4 179.5,146.5 182.6,144.6 185.7,142.7 188.8,140.8 191.9,138.9 195.0,137.0 198.1,135.1 201.2,133.2 204.3,131.3 207.4,129.4 210.5,127.5 213.6,125.6 216.7,123.7 219.8,121.8 222.9,119.9 226.0,118.0 226.0,118.0 222.9,121.8 219.8,125.4 216.7,129.0 213.6,132.4 210.5,135.8 207.4,139.1 204.3,142.3 201.2,145.4 198.1,148.4 195.0,151.2 191.9,154.1 188.8,156.8 185.7,159.4 182.6,161.9 179.5,164.3 176.4,166.6 173.3,168.9 170.2,171.0 167.1,173.1 164.0,175.0 160.9,176.9 157.8,178.6 154.7,180.3 151.6,181.8 148.5,183.3 145.4,184.7 142.3,186.0 139.2,187.2 136.1,188.3 133.0,189.2 129.9,190.2 126.8,191.0 123.7,191.7 120.6,192.3 117.5,192.8 114.4,193.2 111.3,193.6 108.2,193.8 105.1,194.0 102.0,194.0" fill="#b45309" fill-opacity="0.22"/><polygon points="226.0,118.0 227.6,116.1 229.1,114.2 230.7,112.2 232.2,110.2 233.8,108.2 235.3,106.2 236.8,104.1 238.4,102.0 240.0,99.9 241.5,97.8 243.0,95.7 244.6,93.5 246.2,91.3 247.7,89.1 249.2,86.8 250.8,84.6 252.3,82.3 253.9,80.0 255.5,77.6 257.0,75.2 258.5,72.9 260.1,70.5 261.6,68.0 263.2,65.6 264.8,63.1 266.3,60.6 267.9,58.0 269.4,55.5 271.0,52.9 272.5,50.3 274.0,47.7 275.6,45.0 277.1,42.4 278.7,39.7 280.2,37.0 281.8,34.2 283.4,31.4 284.9,28.7 286.5,25.8 288.0,23.0 288.0,80.0 286.5,81.0 284.9,81.9 283.4,82.9 281.8,83.8 280.2,84.8 278.7,85.7 277.1,86.6 275.6,87.6 274.0,88.5 272.5,89.5 271.0,90.5 269.4,91.4 267.9,92.4 266.3,93.3 264.8,94.2 263.2,95.2 261.6,96.1 260.1,97.1 258.5,98.0 257.0,99.0 255.5,100.0 253.9,100.9 252.3,101.9 250.8,102.8 249.2,103.8 247.7,104.7 246.2,105.6 244.6,106.6 243.0,107.5 241.5,108.5 240.0,109.5 238.4,110.4 236.8,111.4 235.3,112.3 233.8,113.2 232.2,114.2 230.7,115.1 229.1,116.1 227.6,117.0 226.0,118.0" fill="#0f6e56" fill-opacity="0.22"/><polyline points="33.8,235.8 37.2,233.7 40.6,231.6 44.0,229.5 47.4,227.4 50.8,225.3 54.3,223.3 57.7,221.2 61.1,219.1 64.5,217.0 67.9,214.9 71.3,212.8 74.7,210.7 78.1,208.6 81.5,206.5 84.9,204.5 88.4,202.4 91.8,200.3 95.2,198.2 98.6,196.1 102.0,194.0 105.4,191.9 108.8,189.8 112.2,187.7 115.6,185.6 119.1,183.5 122.5,181.5 125.9,179.4 129.3,177.3 132.7,175.2 136.1,173.1 139.5,171.0 142.9,168.9 146.3,166.8 149.7,164.7 153.2,162.7 156.6,160.6 160.0,158.5 163.4,156.4 166.8,154.3 170.2,152.2 173.6,150.1 177.0,148.0 180.4,145.9 183.8,143.8 187.3,141.8 190.7,139.7 194.1,137.6 197.5,135.5 200.9,133.4 204.3,131.3 207.7,129.2 211.1,127.1 214.5,125.0 217.9,122.9 221.4,120.8 224.8,118.8 228.2,116.7 231.6,114.6 235.0,112.5 238.4,110.4 241.8,108.3 245.2,106.2 248.6,104.1 252.0,102.0 255.5,100.0 258.9,97.9 262.3,95.8 265.7,93.7 269.1,91.6 272.5,89.5 275.9,87.4 279.3,85.3 282.7,83.2 286.1,81.1 289.5,79.0 293.0,77.0 296.4,74.9 299.8,72.8 303.2,70.7 306.6,68.6" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><polyline points="33.8,171.0 37.0,173.1 40.2,175.1 43.4,177.1 46.7,178.9 49.9,180.6 53.1,182.2 56.3,183.7 59.5,185.1 62.7,186.4 66.0,187.6 69.2,188.7 72.4,189.7 75.6,190.6 78.8,191.3 82.0,192.0 85.3,192.6 88.5,193.1 91.7,193.5 94.9,193.8 98.1,193.9 101.3,194.0 104.6,194.0 107.8,193.8 111.0,193.6 114.2,193.3 117.4,192.8 120.6,192.3 123.9,191.6 127.1,190.9 130.3,190.0 133.5,189.1 136.7,188.0 139.9,186.9 143.2,185.6 146.4,184.3 149.6,182.8 152.8,181.2 156.0,179.6 159.2,177.8 162.4,175.9 165.7,174.0 168.9,171.9 172.1,169.7 175.3,167.4 178.5,165.1 181.7,162.6 185.0,160.0 188.2,157.3 191.4,154.5 194.6,151.6 197.8,148.6 201.0,145.5 204.3,142.3 207.5,139.0 210.7,135.6 213.9,132.1 217.1,128.5 220.3,124.8 223.6,121.0 226.8,117.0 230.0,113.0 233.2,108.9 236.4,104.7 239.6,100.4 242.9,95.9 246.1,91.4 249.3,86.8 252.5,82.0 255.7,77.2 258.9,72.3 262.2,67.2 265.4,62.1 268.6,56.8 271.8,51.5 275.0,46.0 278.2,40.5 281.5,34.8 284.7,29.1 287.9,23.2" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="40.0" y1="175.0" x2="40.0" y2="232.0" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="288.0" y1="23.0" x2="288.0" y2="80.0" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="3 3"/><text x="26.0" y="210.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><text x="226.0" y="210.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="288.0" y="210.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><text x="92.0" y="208.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="300.4" y="97.8" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_g</text><text x="232.2" y="53.4" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text><text x="71.0" y="174.9" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D₁</text><text x="179.5" y="160.9" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D₂</text><text x="260.1" y="106.6" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D₃</text></svg>
:::

Sur la figure, l'écart vertical entre les deux courbes est |g(x) − f(x)| = |2x − x²|, la valeur absolue de la fonction étudiée plus haut ; il change de sens en 0 et en 2, là où les courbes se croisent (les unités des deux axes diffèrent sur le dessin).

::: exemple Aire entre y = x² et y = 2x sur [−1 ; 3]

1. f(x) − g(x) = x² − 2x = x(x − 2) est positif sur [−1 ; 0] (D₁), négatif sur [0 ; 2] (D₂) et positif sur [2 ; 3] (D₃).
2. Avec F(x) = x³/3 − x² : D₁ a pour aire ∫₋₁⁰ (x² − 2x)dx = F(0) − F(−1) = 0 − (−4/3) = 4/3 ; D₂ : −∫₀² (x² − 2x)dx = 4/3 ; D₃ : ∫₂³ (x² − 2x)dx = 4/3.
3. L'aire totale est A = 4 u.a.
4. Aire dépendant d'un paramètre : sous y = 1/x² entre 1 et a (a > 1), A(a) = ∫₁ᵃ dx/x² = [−1/x]₁ᵃ = 1 − 1/a. Quand a tend vers +∞, A(a) tend vers 1 : une partie illimitée peut avoir une aire finie.

:::

::: piege Prendre ∫ f pour l'aire quand f change de signe
Pour f(x) = x² − 2x sur [0 ; 3], on dit « l'aire vaut ∫₀³ f = 0 ». Cela tente parce que l'intégrale « mesure l'aire sous la courbe ». Mais les parties sous l'axe comptent négativement et compensent les autres : l'aire est ∫₀³ |f| = 8/3. L'intégrale n'est l'aire que si f garde un signe constant, au signe près.
:::

::: verifie
Calculer l'aire de la partie limitée par la courbe de f(x) = x² − 4x, l'axe des abscisses et les droites x = 1 et x = 5.

---

f(x) = x(x − 4) est négative sur [1 ; 4] et positive sur [4 ; 5] ; une primitive est x³/3 − 2x². ∫₁⁴ f = (64/3 − 32) − (1/3 − 2) = −9 et ∫₄⁵ f = (125/3 − 50) − (64/3 − 32) = 7/3. L'aire est 9 + 7/3 = 34/3 u.a, alors que ∫₁⁵ f = −20/3.
:::

::: retenir
L'aire sous une courbe est ∫|f| et l'aire entre deux courbes ∫|g − f| : on étudie le signe, on coupe à chaque changement ou croisement, et l'on convertit les u.a en cm² avec le carré de l'unité.
:::

## 🧱 La méthode des rectangles : encadrer et approcher une aire

Comment encadrer l'aire A sous la courbe de f(x) = 1/x entre 1 et 2, avec seulement des aires de rectangles ? La fonction f est décroissante : sur chaque intervalle, son minimum est à droite et son maximum à gauche.
Et peut-on confier ce travail à un programme, pour des centaines de rectangles ?

::: figure Deux rectangles par défaut (verts) sont sous la courbe, deux rectangles par excès (verts et orange) la dépassent : l'aire A est entre les deux sommes
<svg viewBox="0 0 340 205"><title>Courbe de x ↦ 1/x sur [1 ; 2] avec deux rectangles par défaut sous la courbe et deux rectangles par excès qui la dépassent</title><line x1="12.0" y1="175.0" x2="332.0" y2="175.0" stroke="#0f172a" stroke-width="1.6"/><line x1="30.0" y1="187.0" x2="30.0" y2="21.6" stroke="#0f172a" stroke-width="1.6"/><polygon points="332.0,175.0 324.0,171.0 324.0,179.0" fill="#0f172a"/><polygon points="30.0,21.6 26.0,29.6 34.0,29.6" fill="#0f172a"/><polygon points="160.0,175.0 160.0,45.0 225.0,45.0 225.0,175.0" fill="#b45309" fill-opacity="0.22" stroke="#b45309" stroke-width="1.4" stroke-dasharray="4 3"/><polygon points="225.0,175.0 225.0,88.3 290.0,88.3 290.0,175.0" fill="#b45309" fill-opacity="0.22" stroke="#b45309" stroke-width="1.4" stroke-dasharray="4 3"/><polygon points="160.0,175.0 160.0,88.3 225.0,88.3 225.0,175.0" fill="#0f6e56" fill-opacity="0.32" stroke="#0f6e56" stroke-width="1.4"/><polygon points="225.0,175.0 225.0,110.0 290.0,110.0 290.0,175.0" fill="#0f6e56" fill-opacity="0.32" stroke="#0f6e56" stroke-width="1.4"/><polyline points="143.1,25.6 145.2,28.3 147.3,30.9 149.3,33.4 151.4,35.8 153.5,38.2 155.6,40.4 157.7,42.6 159.7,44.7 161.8,46.8 163.9,48.8 166.0,50.7 168.1,52.6 170.1,54.4 172.2,56.2 174.3,57.9 176.4,59.5 178.5,61.2 180.5,62.7 182.6,64.3 184.7,65.8 186.8,67.2 188.9,68.6 190.9,70.0 193.0,71.3 195.1,72.6 197.2,73.9 199.3,75.2 201.3,76.4 203.4,77.5 205.5,78.7 207.6,79.8 209.7,80.9 211.7,82.0 213.8,83.1 215.9,84.1 218.0,85.1 220.1,86.1 222.1,87.0 224.2,88.0 226.3,88.9 228.4,89.8 230.5,90.7 232.5,91.6 234.6,92.4 236.7,93.2 238.8,94.1 240.9,94.9 242.9,95.6 245.0,96.4 247.1,97.2 249.2,97.9 251.3,98.6 253.3,99.3 255.4,100.0 257.5,100.7 259.6,101.4 261.7,102.0 263.7,102.7 265.8,103.3 267.9,104.0 270.0,104.6 272.1,105.2 274.1,105.8 276.2,106.4 278.3,106.9 280.4,107.5 282.5,108.1 284.5,108.6 286.6,109.1 288.7,109.7 290.8,110.2 292.9,110.7 294.9,111.2 297.0,111.7 299.1,112.2 301.2,112.7 303.3,113.2 305.3,113.6 307.4,114.1 309.5,114.5" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><text x="160.0" y="191.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="225.0" y="191.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3/2</text><text x="290.0" y="191.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="30.0" y1="45.0" x2="160.0" y2="45.0" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><text x="26.0" y="49.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="30.0" y1="88.3" x2="160.0" y2="88.3" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><text x="26.0" y="92.3" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2/3</text><line x1="30.0" y1="110.0" x2="160.0" y2="110.0" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><text x="26.0" y="114.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1/2</text><text x="305.6" y="100.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text><text x="40.0" y="191.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text></svg>
:::

Sur [1 ; 3/2], le rectangle par défaut a pour hauteur f(3/2) = 2/3 et celui par excès f(1) = 1, car f décroît ; sur [3/2 ; 2], ce sont f(2) = 1/2 et f(3/2) = 2/3.

::: exemple Encadrer l'aire sous 1/x entre 1 et 2

1. Pour n = 2, h = (2 − 1)/2 = 1/2. Par défaut : h[f(3/2) + f(2)] = (1/2)(2/3 + 1/2) = 7/12. Par excès : h[f(1) + f(3/2)] = (1/2)(1 + 2/3) = 5/6.
2. Donc 7/12 < A < 5/6, soit 0,58 < A < 0,83.
3. Pour n = 4, h = 1/4 : on trouve 0,6345 < A < 0,7595. L'écart entre les deux sommes est h(f(1) − f(2)) = (1/4)(1/2) = 0,125 : il est divisé par 2 quand n est doublé.

:::

::: propriete
**Rectangles.** f est continue et décroissante sur [a ; b], h = (b − a)/n et xₖ = a + kh. Alors

$$ h[f(x₁) + … + f(xₙ)] ≤ ∫ₐᵇ f(x)dx ≤ h[f(x₀) + … + f(xₙ₋₁)] $$

et l'écart entre les deux sommes vaut h(f(a) − f(b)) = (b − a)(f(a) − f(b))/n, qui tend vers 0 quand n augmente. Cas limite : pour f croissante, les deux sommes changent de rôle.
:::

Le programme du manuel calcule autre chose qu'un encadrement : la somme des aires de rectangles de hauteur f au **milieu** de chaque intervalle, une valeur approchée.

```
fonction Rectangles(a, b, n)
    h ← (b − a) / n
    x ← a + h / 2
    somme ← 0
    pour k de 0 à n − 1 :
        somme ← somme + f(x)
        x ← x + h
    retourner somme × h
```

::: exemple Trace pour f(x) = 1/(1 + x²), a = 0, b = 1, n = 2

1. h = 0,5 ; x = 0,25 ; somme = 0.
2. Pour k = 0, somme = 1/(1 + 0,0625) ≈ 0,9412, puis x = 0,75.
3. Pour k = 1, somme ≈ 0,9412 + 1/(1 + 0,5625) = 0,9412 + 0,64 = 1,5812.
4. Le programme renvoie 1,5812 × 0,5 ≈ 0,7906.
5. La valeur exacte est π/4 ≈ 0,7854 : la fonction g = tan est bijective de [0 ; π/4] sur [0 ; 1] et (g⁻¹)′(y) = 1/(1 + y²) (chapitre 4), donc ∫₀¹ dy/(1 + y²) = g⁻¹(1) − g⁻¹(0) = π/4. Ainsi 4 × 0,7906 ≈ 3,16 approche π ; plus n est grand, meilleure est l'approximation.

:::

::: piege Oublier de multiplier par h
On lit dans la trace « somme = 1,5812 » et l'on répond que l'intégrale vaut environ 1,58. Cela tente parce que la boucle ressemble à une somme de valeurs de f. Mais chaque terme est une hauteur : l'aire d'un rectangle est hauteur × largeur h. Sans le facteur h, on obtient plus de 1,5 pour une fonction qui ne dépasse pas 1 sur [0 ; 1].
:::

::: verifie
Que renvoie Rectangles(0, 1, 2) pour f(x) = x² ? Comparer avec la valeur exacte.

---

h = 0,5, les milieux sont 0,25 et 0,75 : somme = 0,0625 + 0,5625 = 0,625, puis 0,625 × 0,5 = 0,3125. La valeur exacte est ∫₀¹ x² dx = 1/3 ≈ 0,3333 : le programme donne une valeur approchée, pas un encadrement.
:::

::: retenir
Pour f décroissante, des rectangles par défaut et par excès encadrent l'aire, avec un écart h(f(a) − f(b)) ; le programme au point milieu renvoie une valeur approchée, somme des hauteurs multipliée par h.
:::

> 🏆 Chapitre franchi, héros : tu calcules une intégrale par une primitive, tu la coupes, la combines et l'encadres, tu intègres un produit par parties, tu mesures valeurs moyennes et aires, et tu fais approcher une aire par un programme. Au chapitre suivant, tu quittes les courbes pour les nombres entiers : l'arithmétique t'attend.
