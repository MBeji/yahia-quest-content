# ⚔️ Notion de polynômes — le degré, les racines et l'art de factoriser

> 💡 «Une racine, et le polynôme se brise en morceaux. Trouve la première, le reste tombe tout seul.»

Tu sais déjà développer, réduire et factoriser une expression littérale. Cette quête change d'échelle : on donne un **nom** à ces expressions — les **polynômes** — et on leur donne un **outil de démolition**. Dès qu'un réel α annule un polynôme, on peut mettre (x − α) en facteur et faire chuter son degré d'une unité. C'est la clé de la résolution des équations de degré 3 et plus, et de toute l'étude des fonctions rationnelles.

## 🔮 Notion de fonction : image, antécédent, ensemble de définition

Un exemple pour démarrer : la **distance de freinage** d'un véhicule roulant à v km/h est donnée par d = 0,2v + v²/150. À 90 km/h, on obtient d = 0,2 × 90 + 90²/150 = 18 + 54 = 72 m. À chaque vitesse correspond **une seule** distance : voilà une fonction.

> **Définition.** Soit E une partie non vide de ℝ. Lorsqu'à tout réel x de E, on associe **au plus un** réel y, on dit qu'on a défini une **fonction** de E vers ℝ. On note f : E → ℝ, x ↦ f(x). L'ensemble D des réels x de E tels que f(x) existe est appelé l'**ensemble de définition** de la fonction f.

**Vocabulaire** : le réel y = f(x) est l'**image** de x par f ; x est un **antécédent** de y par f.

_Exemple détaillé_ : pour f(x) = x² − 3x, l'image de 4 est f(4) = 16 − 12 = **4**. Cherchons les antécédents de 4 : x² − 3x = 4, soit x² − 3x − 4 = 0, soit (x − 4)(x + 1) = 0. Les antécédents de 4 sont donc **4 et −1** : une image est unique, un antécédent ne l'est pas.

Pour l'ensemble de définition, on chasse les valeurs **interdites** : un dénominateur nul, une racine carrée d'un nombre négatif.

| Fonction              | Ensemble de définition |
| --------------------- | ---------------------- |
| x ↦ 3x − 9            | ℝ                      |
| z ↦ √(z − 2)          | [2 ; +∞[               |
| t ↦ −4t² + 2t         | ℝ                      |
| x ↦ (6x − 1)/(2x + 3) | ℝ \ {−3/2}             |

## 🧮 Fonction polynôme, coefficients et degré

> **Définition.** Soient a₀, a₁, …, a₍ₙ₋₁₎ et aₙ des réels. La fonction f définie sur ℝ par f(x) = aₙxⁿ + a₍ₙ₋₁₎x⁽ⁿ⁻¹⁾ + … + a₁x + a₀ est appelée **fonction polynôme**. Les réels aₙ, …, a₀ sont appelés les **coefficients** de la fonction polynôme.

On dit simplement « le polynôme f ». Le **polynôme nul** est celui dont tous les coefficients sont nuls.

> **Définition (degré).** Tout polynôme non nul P a une écriture unique de la forme P(x) = aₙxⁿ + … + a₁x + a₀, avec aₙ ≠ 0. L'entier n est appelé le **degré** du polynôme P, on écrit d°(P) = n. On convient que le polynôme nul n'a pas de degré. Le degré d'un polynôme constant est égal à zéro.

**Vocabulaire officiel** : a₀ est le **terme constant**, a₁x le **terme du 1er degré**, aₙxⁿ le **terme du plus haut degré** — son coefficient aₙ est le **coefficient dominant**. Un polynôme à un seul terme est un **monôme**, un polynôme du 1er degré un **binôme**, un polynôme du 2nd degré un **trinôme**.

_Exemple détaillé_ : P(x) = 4x³ − x² + 7x − 9 est de degré 3 ; son coefficient dominant est 4 et son terme constant est −9. Attention : **le degré n'est pas le nombre de termes** (ici 4 termes, degré 3).

> ⚠️ Toutes les expressions ne sont pas des polynômes. x ↦ |x|, x ↦ √x + 1 et x ↦ (3x − 1)/(x + 2) **ne sont pas** des fonctions polynômes : seules les puissances entières positives de x, multipliées par des réels et additionnées, sont autorisées. En revanche x ↦ −2(x + 1)³ + 5x² − 4x en est un : il suffit de le développer.

## ⚖️ Égalité de deux polynômes : la méthode d'identification

> **Retenir.** Un polynôme est nul **si et seulement si** tous ses coefficients sont nuls. Deux polynômes sont égaux **si et seulement si** ils ont même degré et les coefficients des termes de même degré sont égaux.

C'est la **méthode d'identification** : d'une égalité valable **pour tout réel x**, on tire un système sur les coefficients.

_Exemple détaillé_ : cherchons a, b, c tels que, pour tout x, ax² + bx + c = 2x² + 11 − 10x. On ordonne le membre de droite : 2x² − 10x + 11. Par identification : **a = 2, b = −10, c = 11**.

> ⚠️ Piège classique : f(1) = g(1) et f(4) = g(4) ne prouvent **pas** que f = g. Pour f(x) = 3x² − x + 3 et g(x) = 2x² + 4x − 1, ces deux égalités sont vraies, pourtant f(0) = 3 et g(0) = −1. Une égalité de polynômes se vérifie sur **tout** ℝ, pas sur quelques valeurs.

## ➕ Opérations sur les polynômes

> **Définition.** (f + g)(x) = f(x) + g(x) ; (αf)(x) = α f(x) ; (fg)(x) = f(x) × g(x).

> **Retenir.** Si f et g sont deux polynômes non nuls et α un réel non nul : f + g est un polynôme ; fg est un polynôme et **d°(fg) = d°(f) + d°(g)** ; αf est un polynôme et d°(αf) = d°(f).

Le coefficient dominant d'un produit est le **produit des coefficients dominants**.

_Exemple détaillé_ : f(x) = 2x³ − 5x² + x − 1 (degré 3, coefficient dominant 2) et g(x) = −3x² + 7x − √5 (degré 2, coefficient dominant −3). Alors d°(fg) = 3 + 2 = **5**, et le coefficient dominant de fg est 2 × (−3) = **−6**.

> 🗡️ Le degré d'une **somme**, lui, peut **baisser** : pour f(x) = 3x² − x + 4 et g(x) = −3x² + 2x − 1, on obtient (f + g)(x) = x + 3, de degré 1 et non 2. Les termes de plus haut degré se sont annulés. Pour un produit, cela n'arrive jamais.

## 🎯 Racines et factorisation : l'arme du chapitre

> **Définition.** On dit qu'un réel α est une **racine** (ou un **zéro**) d'un polynôme f si f(α) = 0.

> **Définition.** Le polynôme P est **factorisable** par le polynôme Q s'il existe un polynôme R tel que, pour tout réel x, P(x) = Q(x) × R(x).

Le théorème central du chapitre relie les deux :

$$ α racine de f (degré n ≥ 1) ⟺ f(x) = (x − α) g(x), avec d°(g) = n − 1 $$

Et si l'on connaît **plusieurs** racines α et β, on peut sortir les deux facteurs : f(x) = (x − α)(x − β) g(x) avec d°(g) = n − 2. Plus généralement, avec k racines α₁, …, α_k (k ≤ n) : f(x) = (x − α₁)…(x − α_k) g(x) et d°(g) = n − k.

> **Retenir.** Un polynôme de degré 3 admet **au plus trois** racines ; un polynôme de degré 4 au plus quatre ; un polynôme de degré n (n ≥ 2) admet **au plus n** racines.

> 🗡️ Conséquence à retenir : si un polynôme de degré **inférieur ou égal à n** admet **plus de n** racines distinctes, il ne peut pas être « non nul » — c'est donc le **polynôme nul**, celui dont tous les coefficients sont nuls et qui s'annule en tout réel. C'est l'argument standard pour prouver qu'une identité est vraie partout.

**Comment trouver le quotient g ?** Par **identification**. On cherche une **racine apparente** en testant les valeurs simples : 1, −1, 2, −2, 3…

_Exemple détaillé_ : P(x) = 3x³ + x² + 2x − 6. On teste 1 : P(1) = 3 + 1 + 2 − 6 = 0, donc **1 est racine apparente**. On écrit alors P(x) = (x − 1)(ax² + bx + c) et on développe :
(x − 1)(ax² + bx + c) = ax³ + (b − a)x² + (c − b)x − c.
Par identification avec 3x³ + x² + 2x − 6 : a = 3 ; b − a = 1 donc b = 4 ; c − b = 2 donc c = 6 ; et −c = −6 ✓ (cohérent). Conclusion : **P(x) = (x − 1)(3x² + 4x + 6)**.

_Exemple détaillé (résoudre une équation de degré 3)_ : x³ + 2x² − 5x − 6 = 0. On teste −1 : −1 + 2 + 5 − 6 = 0, donc −1 est racine. Par identification, x³ + 2x² − 5x − 6 = (x + 1)(x² + x − 6) = (x + 1)(x − 2)(x + 3). Le produit est nul si l'un des facteurs l'est : **S = {−3 ; −1 ; 2}**. Le degré est 3, on a trois racines : la liste est complète.

> ⚠️ Une racine α donne le facteur **(x − α)**, avec le signe **opposé** : la racine −3 donne le facteur (x + 3), pas (x − 3). C'est l'erreur de signe la plus fréquente du chapitre.

## 🧊 Une situation concrète : la boîte de volume maximal

Dans une plaque carrée de 60 cm de côté, on découpe à chaque coin un carré de côté x cm, puis on relève les bords pour former une boîte sans couvercle.

::: figure Plaque carrée de 60 cm de côté : on retire un carré de côté x à chaque coin, puis on relève les quatre bords pour obtenir une boîte de hauteur x
<svg viewBox="0 0 340 200">
<rect x="20" y="30" width="130" height="130" fill="#e0f2fe" stroke="#0f172a" stroke-width="2"/>
<g fill="#fecaca" stroke="#b91c1c" stroke-width="1.6" stroke-dasharray="4 3">
<rect x="20" y="30" width="26" height="26"/>
<rect x="124" y="30" width="26" height="26"/>
<rect x="20" y="134" width="26" height="26"/>
<rect x="124" y="134" width="26" height="26"/>
</g>
<g stroke="#0f172a" stroke-width="1.4" stroke-dasharray="5 4" fill="none">
<line x1="46" y1="30" x2="46" y2="160"/>
<line x1="124" y1="30" x2="124" y2="160"/>
<line x1="20" y1="56" x2="150" y2="56"/>
<line x1="20" y1="134" x2="150" y2="134"/>
</g>
<path d="M168 95 L196 95 M188 89 L196 95 L188 101" fill="none" stroke="#0f172a" stroke-width="2"/>
<polygon points="216,112 296,112 296,158 216,158" fill="#e0f2fe" stroke="#0f172a" stroke-width="2"/>
<polygon points="216,112 238,94 318,94 296,112" fill="#bae6fd" stroke="#0f172a" stroke-width="2"/>
<polygon points="296,112 318,94 318,140 296,158" fill="#7dd3fc" stroke="#0f172a" stroke-width="2"/>
<g font-size="12" font-weight="700" fill="#0f172a">
<text x="85" y="180" text-anchor="middle">60 cm</text>
<text x="33" y="48" text-anchor="middle" fill="#b91c1c">x</text>
<text x="310" y="132" text-anchor="middle">x</text>
</g>
</svg>
:::

Le fond mesure (60 − 2x) cm de côté et la hauteur vaut x cm, avec 0 < x < 30. D'où le volume :

$$ V(x) = x(60 − 2x)² = 4x³ − 240x² + 3600x $$

C'est un polynôme de degré 3. On calcule V(10) = 10 × 40² = 16 000 cm³, puis on étudie la différence :

$$ V(x) − V(10) = 4(x − 10)(x² − 50x + 400) = 4(x − 10)²(x − 40) $$

Sur ]0 ; 30[, le carré (x − 10)² est positif ou nul et (x − 40) est **strictement négatif** : la différence est donc toujours **négative ou nulle**, et nulle seulement pour x = 10. Le volume est donc **maximal pour x = 10 cm**, et vaut **16 000 cm³**.

> 🗡️ Retiens la méthode : pour comparer une fonction polynôme à une valeur, on étudie le **signe de la différence** après l'avoir **factorisée**. Un facteur au carré est toujours de signe positif — il ne change jamais le signe du produit.

## 📐 Fonctions rationnelles

> **Définition.** Soit f et g deux fonctions polynômes. La fonction h : x ↦ f(x)/g(x) est appelée **fonction rationnelle**.

Son ensemble de définition est l'ensemble des réels qui **n'annulent pas** le dénominateur. On factorise donc numérateur et dénominateur, puis on simplifie — **sans jamais** réintégrer les valeurs interdites.

_Exemple détaillé_ : h(x) = (x² − 4)/(x² − x − 2). Le dénominateur se factorise en (x − 2)(x + 1) : il s'annule pour x = 2 et x = −1, donc D = ℝ \ {−1 ; 2}. Le numérateur vaut (x − 2)(x + 2), d'où, pour tout x de D :
h(x) = (x − 2)(x + 2) / ((x − 2)(x + 1)) = **(x + 2)/(x + 1)**.
La valeur 2 reste **exclue** de D, même si elle a disparu de l'écriture simplifiée. Pour le signe de h, on dresse un tableau de signes des facteurs (x + 2) et (x + 1) et on applique la règle des signes du quotient.

## 🧭 Aller plus loin : racines, symétrie et sommes télescopiques

Trois techniques d'expert reposent sur tout ce qui précède. Elles arrivent régulièrement en fin de sujet.

**1. Relations entre les coefficients et les racines (degré 3).** Si le polynôme P(x) = ax³ + bx² + cx + d (a ≠ 0) admet **trois racines** α, β et γ, alors P(x) = a(x − α)(x − β)(x − γ). En développant, on obtient a[x³ − (α + β + γ)x² + (αβ + βγ + γα)x − αβγ], puis par identification :

$$ α + β + γ = −b/a ; αβ + βγ + γα = c/a ; αβγ = −d/a $$

Ces trois relations donnent des **sommes symétriques sans résoudre l'équation**. Par exemple 1/α + 1/β + 1/γ = (αβ + βγ + γα)/(αβγ) : il suffit de faire le quotient des deux dernières relations.

_Exemple détaillé_ : P(x) = x³ − 6x² + 11x − 6 = (x − 1)(x − 2)(x − 3), donc α = 1, β = 2, γ = 3. On vérifie α + β + γ = 6 = −(−6)/1 ✓, αβ + βγ + γα = 2 + 6 + 3 = 11 = 11/1 ✓, αβγ = 6 = −(−6)/1 ✓. Et 1/1 + 1/2 + 1/3 = 11/6, qui est bien 11/6 = (αβ + βγ + γα)/(αβγ) ✓.

> ⚠️ Attention aux signes : la somme des racines vaut **−b/a** (signe opposé) et le produit **−d/a** pour un degré 3. Recopier b/a ou d/a est l'erreur la plus fréquente.

**2. Polynômes symétriques de degré 3.** Un polynôme de la forme f(x) = ax³ + bx² + bx + a (les coefficients se lisent à l'identique dans les deux sens) admet **toujours −1 comme racine** : f(−1) = −a + b − b + a = 0. La factorisation est immédiate :

$$ ax³ + bx² + bx + a = (x + 1)(ax² + (b − a)x + a) $$

_Exemple détaillé_ : pour 7x³ − 43x² − 43x + 7, on a a = 7 et b = −43, donc b − a = −50 et l'on obtient (x + 1)(7x² − 50x + 7). Comme 7x² − 50x + 7 = (x − 7)(7x − 1), les racines sont **−1, 1/7 et 7**.

**3. Décomposition en éléments simples et somme télescopique.** On cherche à écrire 1/(x(x + 1)) sous la forme a/x + b/(x + 1). En réduisant au même dénominateur : a(x + 1) + bx = (a + b)x + a, qui doit être égal à 1 pour tout x. Par identification, a = 1 et a + b = 0, donc b = −1 :

$$ 1/(k(k + 1)) = 1/k − 1/(k + 1) $$

Additionnons ces égalités pour k = 1, 2, …, n : chaque terme −1/(k + 1) est effacé par le terme +1/(k + 1) suivant. C'est un **télescopage**, il ne reste que les deux extrémités :

$$ S = 1/(1×2) + 1/(2×3) + … + 1/(n(n + 1)) = 1 − 1/(n + 1) = n/(n + 1) $$

_Exemple détaillé_ : pour n = 4, S = 1/2 + 1/6 + 1/12 + 1/20 = 1 − 1/5 = 4/5 ✓ (vérification directe : 0,5 + 0,1667 + 0,0833 + 0,05 = 0,8).

## 📜 Math et culture : la division suivant les puissances décroissantes

La méthode d'identification n'est pas la seule pour factoriser. On peut aussi **poser la division** d'un polynôme par un autre, exactement comme une division de nombres, en rangeant les termes suivant les **puissances décroissantes**.

_Exemple_ : diviser P(x) = 6x³ + x² + 8x − 5 par 2x − 1. On divise 6x³ par 2x, ce qui donne 3x² ; on retranche 3x²(2x − 1) = 6x³ − 3x², il reste 4x² + 8x − 5 ; on divise 4x² par 2x, ce qui donne 2x ; on retranche 2x(2x − 1) = 4x² − 2x, il reste 10x − 5 ; enfin 10x divisé par 2x donne 5, et 5(2x − 1) = 10x − 5, reste **0**. Conclusion :

$$ 6x³ + x² + 8x − 5 = (2x − 1)(3x² + 2x + 5) $$

> 🏆 Quête franchie, héros : tu sais lire le degré d'un polynôme, identifier ses coefficients, débusquer une racine apparente et la transformer en facteur. Ces armes te suivront jusqu'aux fonctions rationnelles et à toute l'analyse des années suivantes.
