# ⚔️ Intégrales — l'aire qui révèle la primitive

> 💡 «Dériver, c'est descendre ; intégrer, c'est remonter. Celui qui sait remonter mesure les aires, les volumes et les moyennes du monde.»

Au Xe siècle, Thabit Ibn Qurra cherchait déjà l'aire sous une parabole — ce que nous écrivons aujourd'hui ∫₀ᵃ √(px) dx. Il lui fallait un « artifice astucieux » ; toi, tu disposes de l'arme que le chapitre des **primitives** t'a forgée. Ici tu vas découvrir qu'une aire n'est rien d'autre qu'une différence F(b) − F(a), et que cette idée simple mesure aussi des volumes, des moyennes et des limites de suites. C'est le chapitre-carrefour de l'analyse : presque chaque problème de bac s'y arrête.

## 🏰 L'aire sous la courbe : naissance de l'intégrale

Le plan est muni d'un repère orthogonal (O, i⃗, j⃗). L'**unité d'aire** (u.a) est l'aire du rectangle de dimensions ‖i⃗‖ et ‖j⃗‖ : toutes les aires de ce chapitre se comptent dans cette unité.

Prends f continue et **positive** sur [a, b]. On veut l'aire 𝒜(t) de la partie comprise entre C_f, l'axe des abscisses et les droites x = a, x = t. Fais grandir t d'un petit h > 0 : la tranche gagnée est coincée entre deux rectangles, d'où hf(t) ≤ 𝒜(t + h) − 𝒜(t) ≤ hf(t + h). En divisant par h et en faisant tendre h vers 0, la continuité de f donne 𝒜′(t) = f(t). **La fonction aire est une primitive de f.**

> **Propriété** — « Soit f une fonction continue sur un intervalle I. Si F et G sont deux primitives de f sur I alors pour tous a et b de I, F(b) − F(a) = G(b) − G(a). »

C'est ce qui rend la définition suivante légitime : le nombre F(b) − F(a) ne dépend pas de la primitive choisie (deux primitives diffèrent d'une constante, qui s'élimine dans la soustraction).

> **Définition — intégrale d'une fonction continue et positive** — « Soit f une fonction continue et positive sur un intervalle [a, b] et F une primitive de f sur [a, b]. L'aire (en u.a) de la partie du plan limitée par la courbe de f, l'axe des abscisses et les droites d'équations x = a et x = b est le réel F(b) − F(a). Le réel F(b) − F(a) est appelé intégrale de f de a à b et est noté ∫ₐᵇ f(x)dx. »

::: figure La partie colorée est l'aire sous C_f entre x = a et x = b : elle vaut exactement F(b) − F(a).
<svg viewBox="0 0 320 210"><polygon points="121,180 121,117 142,107 164,100 186,95 220,92 220,180" fill="#0f6e56" fill-opacity="0.18"/><path d="M40 180 H305" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M50 195 V20" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M305 180 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M50 20 l-3.5 7 l7 0 z" fill="#0f172a"/><path d="M70 150 Q170 70 290 100" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><line x1="121" y1="117" x2="121" y2="180" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="220" y1="92" x2="220" y2="180" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><text x="121" y="195" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">a</text><text x="220" y="195" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">b</text><text x="255" y="88" font-size="12" font-weight="700" fill="#0f6e56">C_f</text><text x="150" y="145" font-size="12" font-weight="700" fill="#0f6e56">∫ₐᵇ f(x)dx</text></svg>
:::

_Exemple détaillé_ — soit f(x) = x² sur [1, 2] : f est continue et positive. Une primitive est F(x) = x³/3 (on vérifie F′(x) = 3x²/3 = x²). Donc l'aire vaut :

$$ ∫₁² x² dx = F(2) − F(1) = 8/3 − 1/3 = 7/3 ≈ 2,33 u.a $$

_Contrôle_ — sur [1, 2], f varie entre 1 et 4, donc l'aire est comprise entre 1 × 1 = 1 et 4 × 1 = 4. La valeur 2,33 est bien dans cet encadrement.

## 🧮 Intégrale d'une fonction continue quelconque

On lâche maintenant l'hypothèse « positive » et l'ordre a < b : la définition se prolonge telle quelle, mais **ce n'est plus une aire**.

> **Définition — intégrale d'une fonction continue** — « Soit f une fonction continue sur un intervalle I, a et b deux réels de I et F une primitive de f sur I. On appelle intégrale de f entre a et b le réel, noté ∫ₐᵇ f(x)dx, défini par ∫ₐᵇ f(x)dx = F(b) − F(a). »

> **Vocabulaire et notations** — « Dans l'écriture ∫ₐᵇ f(x)dx, on peut remplacer la lettre x par n'importe quelle lettre : ∫ₐᵇ f(x)dx = ∫ₐᵇ f(u)du = ∫ₐᵇ f(t)dt. On dit que x est une variable muette. Pour toute primitive F de f, on écrit ∫ₐᵇ f(x)dx = [F(x)]ₐᵇ = F(b) − F(a). »

_Exemple détaillé_ — calculons ∫_{1/2}¹ (x⁴ − 1)dx. Une primitive est F(x) = x⁵/5 − x (dérivée : x⁴ − 1 ✓).

$$ F(1) = 1/5 − 1 = −4/5     et     F(1/2) = 1/160 − 1/2 = −79/160 $$

$$ ∫_{1/2}¹ (x⁴ − 1)dx = −4/5 + 79/160 = (−128 + 79)/160 = −49/160 = −0,30625 $$

_Contrôle_ — sur [1/2, 1] la fonction x⁴ − 1 est négative, entre −0,94 et 0 ; l'intégrale doit donc être négative et de l'ordre de −0,3 sur une largeur 0,5. ✓

_Exemple_ — ∫₀¹ sin(πx)dx : une primitive de sin(πx) est −cos(πx)/π. D'où [−cos(πx)/π]₀¹ = 1/π + 1/π = **2/π ≈ 0,64**.

> ⚠️ La variable d'intégration est **muette** : elle disparaît du résultat. Écrire « ∫₀ˣ f(x)dx » est une faute — on écrit ∫₀ˣ f(t)dt, car x est déjà pris par la borne.

## ⚡ Propriétés algébriques : Chasles et linéarité

> **Propriétés algébriques** — « Soit f continue sur I, a, b et c des réels de I. Alors ∫ₐᵃ f(x)dx = 0 ; ∫ₐᵇ f(x)dx = −∫_bᵃ f(x)dx ; ∫ₐᶜ f(x)dx + ∫_cᵇ f(x)dx = ∫ₐᵇ f(x)dx (relation de Chasles). »

La démonstration tient en une ligne avec une primitive F : F(a) − F(a) = 0 ; F(b) − F(a) = −(F(a) − F(b)) ; et (F(c) − F(a)) + (F(b) − F(c)) = F(b) − F(a).

::: figure Découpée en c, l'aire de gauche plus l'aire de droite reconstituent exactement l'aire de a à b : c'est la relation de Chasles.
<svg viewBox="0 0 320 210"><polygon points="121,180 121,117 142,107 164,100 164,180" fill="#0f6e56" fill-opacity="0.20"/><polygon points="164,180 164,100 186,95 220,92 220,180" fill="#b45309" fill-opacity="0.20"/><path d="M40 180 H305" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M50 195 V20" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M305 180 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M50 20 l-3.5 7 l7 0 z" fill="#0f172a"/><path d="M70 150 Q170 70 290 100" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><line x1="121" y1="117" x2="121" y2="180" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="164" y1="100" x2="164" y2="180" stroke="#0f172a" stroke-width="1.4"/><line x1="220" y1="92" x2="220" y2="180" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><text x="121" y="195" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">a</text><text x="164" y="195" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">c</text><text x="220" y="195" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">b</text><text x="255" y="88" font-size="12" font-weight="700" fill="#0f6e56">C_f</text></svg>
:::

> **Théorème (linéarité)** — « Soit f et g deux fonctions continues sur [a, b]. Pour tous réels α et β, ∫ₐᵇ (αf(x) + βg(x))dx = α∫ₐᵇ f(x)dx + β∫ₐᵇ g(x)dx. »

_Exemple détaillé (linéarité)_ — calculons ∫₁² x²/(x + 1)² dx + ∫₁² (2x + 1)/(x + 1)² dx. Par linéarité, on regroupe sous une seule intégrale :

$$ ∫₁² (x² + 2x + 1)/(x + 1)² dx = ∫₁² (x + 1)²/(x + 1)² dx = ∫₁² 1 dx = [x]₁² = 1 $$

Aucune des deux intégrales n'était calculable telle quelle : c'est leur **somme** qui se simplifie. Retiens ce réflexe, il revient à chaque session.

_Exemple détaillé (couple I, J)_ — soit I = ∫₀^{π/2} sin²x dx et J = ∫₀^{π/2} (cos²x)/2 dx. Alors :

$$ I + 2J = ∫₀^{π/2} (sin²x + cos²x)dx = ∫₀^{π/2} 1 dx = π/2 $$

$$ 2J − I = ∫₀^{π/2} (cos²x − sin²x)dx = ∫₀^{π/2} cos(2x)dx = [sin(2x)/2]₀^{π/2} = 0 $$

De 2J = I et I + 2J = π/2 on tire 2I = π/2, donc **I = π/4** et **J = π/8**. _Contrôle_ : sin²x a pour valeur moyenne 1/2 sur un quart de période, donc I ≈ 0,5 × π/2 ≈ 0,785 = π/4 ✓.

## 🛡️ Intégrales et inégalités

> **Théorème (positivité)** — « Soit f une fonction continue sur [a, b]. Si f est positive sur [a, b], alors ∫ₐᵇ f(x)dx ≥ 0. » (Toute primitive d'une fonction positive est croissante sur [a, b], donc F(b) ≥ F(a).)

> **Corollaire** — « Soit f continue sur [a, b] où a < b. Si f est positive et ne s'annule qu'en un nombre fini de réels de [a, b], alors ∫ₐᵇ f(x)dx > 0. »

> **Corollaire (comparaison)** — « Soit f, g et h trois fonctions continues sur [a, b]. Si h ≤ f ≤ g, alors ∫ₐᵇ h(x)dx ≤ ∫ₐᵇ f(x)dx ≤ ∫ₐᵇ g(x)dx. »

> **Corollaire** — « Si f est une fonction continue sur [a, b], alors |∫ₐᵇ f(x)dx| ≤ ∫ₐᵇ |f(x)|dx. » (Conséquence du précédent appliqué à −|f| ≤ f ≤ |f|.)

> 🗡️ **Encadrer sans calculer** : quand une intégrale résiste au calcul, encadre son **intégrande** puis intègre l'encadrement. C'est la technique n°1 pour étudier une suite d'intégrales.

_Exemple détaillé_ — soit uₙ = ∫₀¹ x^{n+1}/(1 + x²) dx. Pour x ∈ [0, 1], on a 1 + x² ≥ 1, donc :

$$ 0 ≤ x^{n+1}/(1 + x²) ≤ x^{n+1} $$

Par comparaison : 0 ≤ uₙ ≤ ∫₀¹ x^{n+1}dx = [x^{n+2}/(n + 2)]₀¹ = 1/(n + 2). Pour n = 100, 0 ≤ u₁₀₀ ≤ 1/102 ≈ 0,0098 : la valeur 0 approche u₁₀₀ à moins de 10⁻² près. Et comme 1/(n + 2) → 0, la suite (uₙ) **converge vers 0**.

_Exemple (majoration par la valeur absolue)_ — ∫_{−1}¹ x dx = [x²/2]_{−1}¹ = 1/2 − 1/2 = 0, tandis que ∫_{−1}¹ |x| dx = 2∫₀¹ x dx = 1. On a bien |0| ≤ 1 : l'inégalité peut être **très** large quand f change de signe.

> ⚠️ La réciproque de la positivité est **fausse** : ∫ₐᵇ f(x)dx ≥ 0 n'entraîne pas f ≥ 0 sur [a, b]. Contre-exemple : ∫_{−1}¹ x dx = 0 alors que x < 0 sur [−1, 0[.

## 📐 Calculer une aire

Dès que f change de signe, l'intégrale compte les parties situées sous l'axe **négativement**. L'aire, elle, est toujours positive : on intègre |f|.

> **Définition — aire (fonction de signe quelconque)** — « Soit f une fonction continue sur [a, b]. L'aire (en u.a) de la partie du plan limitée par l'axe des abscisses, la courbe de f, les droites d'équations x = a et x = b est le réel ∫ₐᵇ |f(x)|dx. »

_Exemple détaillé_ — soit f(x) = x³ sur [−2, 3]. La fonction est négative sur [−2, 0] et positive sur [0, 3] ; on coupe en 0 (Chasles) :

$$ ∫_{−2}³ |x³| dx = ∫_{−2}⁰ (−x³)dx + ∫₀³ x³ dx = [−x⁴/4]_{−2}⁰ + [x⁴/4]₀³ = 4 + 81/4 = 97/4 = 24,25 $$

Alors que ∫_{−2}³ x³ dx = 81/4 − 16/4 = 65/4 = 16,25. **Les deux nombres diffèrent** : le second n'est pas une aire, c'est un bilan algébrique.

> **Définition — aire entre deux courbes** — « Soit f et g deux fonctions continues sur [a, b]. L'aire (en u.a) de la partie du plan limitée par la courbe de f, la courbe de g et les droites d'équations x = a et x = b est le réel ∫ₐᵇ |f(x) − g(x)|dx. »

_Exemple détaillé_ — aire entre C_f (f(x) = sin x) et C_g (g(x) = cos x) sur [0, π/2]. On étudie le signe de f − g : sin x − cos x s'annule en π/4, est **négatif** sur [0, π/4[ et **positif** sur ]π/4, π/2]. D'où deux morceaux :

$$ ∫₀^{π/4} (cos x − sin x)dx = [sin x + cos x]₀^{π/4} = √2 − 1 $$

$$ ∫_{π/4}^{π/2} (sin x − cos x)dx = [−cos x − sin x]_{π/4}^{π/2} = −1 + √2 = √2 − 1 $$

Aire totale = 2(√2 − 1) = **2√2 − 2 ≈ 0,83 u.a**. _Contrôle_ : l'écart |sin x − cos x| vaut au plus 1 (aux bornes) et 0 en π/4, sur une largeur π/2 ≈ 1,57 ; une aire de l'ordre de 0,8 est cohérente.

> ⚠️ Ne jamais écrire l'aire ∫ₐᵇ (f − g) sans avoir **étudié le signe** de f − g. Si les courbes se croisent, il faut découper l'intervalle en chaque point d'intersection.

## 🔮 Calculs d'intégrales : primitive, parties, rectangles

**a) Au moyen d'une primitive.** C'est la méthode par défaut : reconnaître la forme dérivée.

_Exemple détaillé_ — ∫₀¹ x³/√(x⁴ + 1) dx. On reconnaît u′/(2√u) à un facteur près, avec u(x) = x⁴ + 1 et u′(x) = 4x³. Une primitive est donc F(x) = √(x⁴ + 1)/2. _Vérification par dérivation_ : F′(x) = (1/2) · 4x³/(2√(x⁴ + 1)) = x³/√(x⁴ + 1) ✓.

$$ ∫₀¹ x³/√(x⁴ + 1) dx = √2/2 − 1/2 = (√2 − 1)/2 ≈ 0,21 $$

_Exemples_ — ∫₀³ (5x⁴ − x³ − 2)dx = [x⁵ − x⁴/4 − 2x]₀³ = 243 − 20,25 − 6 = **867/4** ; ∫₀^{π/4} dx/cos²x = [tan x]₀^{π/4} = **1** ; ∫₁² dx/(1 + x)² = [−1/(1 + x)]₁² = −1/3 + 1/2 = **1/6**.

**b) Intégration par parties (IPP).** Quand l'intégrande est un **produit** dont un facteur se simplifie en dérivant (typiquement une puissance de x).

> **Théorème d'intégration par parties** — « Soit f et g deux fonctions dérivables sur [a, b] et telles que leurs dérivées f′ et g′ sont continues sur [a, b]. Alors ∫ₐᵇ f(t)g′(t)dt = [f(t)g(t)]ₐᵇ − ∫ₐᵇ f′(t)g(t)dt. » (On intègre (fg)′ = f′g + g′f.)

_Exemple détaillé_ — calculons ∫₀^{π/2} x sin x dx. On pose f(t) = t (donc f′ = 1) et g′(t) = sin t (donc g(t) = −cos t) :

$$ ∫₀^{π/2} t sin t dt = [−t cos t]₀^{π/2} + ∫₀^{π/2} cos t dt = 0 + [sin t]₀^{π/2} = 1 $$

_Contrôle_ : l'intégrande croît de 0 à π/2 ≈ 1,57 sur une largeur 1,57 ; une valeur de 1 est plausible ✓.

_Exemple détaillé (double IPP)_ — ∫₀^{π/2} x² cos x dx. On pose f(t) = t², g′(t) = cos t, g(t) = sin t :

$$ ∫₀^{π/2} t² cos t dt = [t² sin t]₀^{π/2} − 2∫₀^{π/2} t sin t dt = π²/4 − 2 × 1 = π²/4 − 2 ≈ 0,47 $$

> 🗡️ **Choisir f et g′** : f est le facteur qui **se simplifie** en dérivant (x, x², un polynôme), g′ celui qu'on **sait** primitiver (sin, cos, 1/cos²). Un mauvais choix complique l'intégrale au lieu de la réduire.

**c) Calcul approché — méthode des rectangles.** Quand aucune primitive n'est disponible, on encadre l'aire par des rectangles.

_Exemple détaillé_ — A = ∫₁² dx/x, avec f(x) = 1/x **décroissante** sur [1, 2]. Partageons [1, 2] en 2 intervalles de longueur 0,5. Sur chaque morceau, le rectangle de hauteur la plus petite valeur minore, celui de hauteur la plus grande valeur majore :

$$ 0,5 × f(1,5) + 0,5 × f(2) ≤ A ≤ 0,5 × f(1) + 0,5 × f(1,5) $$

$$ 1/3 + 1/4 = 7/12 ≤ A ≤ 1/2 + 1/3 = 5/6 $$

Soit 0,583 ≤ A ≤ 0,833. En affinant à 5 intervalles de longueur 0,2, l'encadrement se resserre : plus le pas est petit, plus les deux sommes se rapprochent de A.

## 🎯 Valeur moyenne et inégalité de la moyenne

> **Définition — valeur moyenne** — « Soit f une fonction continue sur [a, b] (a < b). On appelle valeur moyenne de f sur [a, b] le réel, noté f̄, défini par f̄ = 1/(b − a) · ∫ₐᵇ f(x)dx. »

> **Interprétation géométrique** — « L'aire (en u.a) de la partie du plan limitée par la courbe de f, les droites d'équations x = a, x = b et y = 0 est égale à celle du rectangle de côtés (b − a) et f̄. » (f continue et positive.)

::: figure Le rectangle de hauteur f̄ a exactement la même aire que la partie sous la courbe : ce qui dépasse au-dessus comble ce qui manque en dessous.
<svg viewBox="0 0 320 210"><polygon points="90,180 90,140 130,116 170,104 210,100 250,104 250,180" fill="#0f6e56" fill-opacity="0.16"/><rect x="90" y="109" width="160" height="71" fill="#b45309" fill-opacity="0.16" stroke="#b45309" stroke-width="1.8"/><path d="M40 180 H305" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M50 195 V20" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M305 180 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M50 20 l-3.5 7 l7 0 z" fill="#0f172a"/><path d="M90 140 Q170 80 250 104" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><text x="90" y="195" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">a</text><text x="250" y="195" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">b</text><text x="58" y="113" font-size="12" font-weight="700" fill="#b45309">f̄</text><text x="262" y="100" font-size="12" font-weight="700" fill="#0f6e56">C_f</text></svg>
:::

_Exemple détaillé_ — f(x) = 3x − 1 sur [0, 2]. On calcule ∫₀² (3x − 1)dx = [3x²/2 − x]₀² = 6 − 2 = 4, donc f̄ = 4/2 = **2**. Or f(1) = 3 − 1 = 2 : ici la moyenne est atteinte au milieu de l'intervalle, ce qui est normal pour une fonction affine.

_Exemple_ — valeur moyenne de cos sur [0, π/2] : ∫₀^{π/2} cos x dx = [sin x]₀^{π/2} = 1, donc f̄ = 1/(π/2) = **2/π ≈ 0,64**.

> **Théorème (Inégalité de la moyenne)** — « Soit f une fonction continue sur [a, b] (a < b). Soit m et M deux réels. Si pour tout x de [a, b], m ≤ f(x) ≤ M, alors m ≤ f̄ ≤ M. »

> **Corollaire** — « Soit f une fonction continue sur [a, b] (a < b). Il existe c ∈ [a, b], tel que f̄ = f(c). »

_Exemple détaillé_ — encadrons ∫₀¹ dx/(1 + x²). Pour x ∈ [0, 1], on a 1 ≤ 1 + x² ≤ 2, donc 1/2 ≤ 1/(1 + x²) ≤ 1. L'inégalité de la moyenne sur [0, 1] (de longueur 1) donne directement :

$$ 0,5 ≤ ∫₀¹ dx/(1 + x²) ≤ 1 $$

(La valeur exacte, obtenue plus bas, est π/4 ≈ 0,785 : elle est bien dans l'encadrement.)

## 🧊 Volumes de solides de révolution

> **Formule du volume** — « L'espace est muni d'un repère orthonormé (O, i⃗, j⃗, k⃗). Soit f une fonction continue et positive sur [a, b]. Le volume V du solide de révolution engendré par la rotation de l'arc AB = {M(x, y) tels que y = f(x) et a ≤ x ≤ b} autour de l'axe (O, i⃗) est le réel V = π ∫ₐᵇ f²(x)dx. »

L'idée : la section du solide par le plan d'abscisse x est un **disque** de rayon f(x), donc d'aire S(x) = πf²(x) ; on « somme » ces disques de a à b.

::: figure Chaque section perpendiculaire à (Ox) est un disque de rayon f(x) : le volume s'obtient en intégrant son aire πf²(x).
<svg viewBox="0 0 320 190"><path d="M70 60 Q170 30 260 55 L260 135 Q170 160 70 130 Z" fill="#0f6e56" fill-opacity="0.13"/><path d="M30 95 H300" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M300 95 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M70 60 Q170 30 260 55" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><path d="M70 130 Q170 160 260 135" fill="none" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="4 3"/><ellipse cx="167.5" cy="95" rx="9" ry="51.25" fill="#b45309" fill-opacity="0.20" stroke="#b45309" stroke-width="1.8"/><line x1="167.5" y1="95" x2="167.5" y2="43.75" stroke="#b45309" stroke-width="1.6"/><text x="174" y="70" font-size="12" font-weight="700" fill="#b45309">f(x)</text><text x="70" y="112" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">a</text><text x="260" y="112" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">b</text><text x="300" y="112" font-size="12" font-weight="700" fill="#0f172a">(Ox)</text></svg>
:::

_Exemple détaillé (la sphère)_ — le demi-cercle supérieur de centre O et de rayon R a pour équation y = f(x) = √(R² − x²), avec x ∈ [−R, R]. Sa rotation autour de (Ox) engendre la sphère de rayon R :

$$ V = π ∫_{−R}^R (R² − x²)dx = π[R²x − x³/3]_{−R}^R = π(2R³ − 2R³/3) = 4πR³/3 $$

On retrouve exactement la formule connue du volume de la boule ✓.

_Exemple détaillé_ — la portion de courbe y = √x, 0 ≤ x ≤ 4, tourne autour de (Ox). Ici f²(x) = x, donc :

$$ V = π ∫₀⁴ x dx = π[x²/2]₀⁴ = 8π ≈ 25,1 $$

> ⚠️ C'est **f²** que l'on intègre, pas f. Écrire V = π∫f est l'erreur la plus fréquente du chapitre — et elle est même dimensionnellement fausse.

## 🌀 Fonctions définies par une intégrale

On fixe la borne du bas et on laisse **varier** celle du haut : on fabrique une nouvelle fonction.

> **Théorème** — « Soit f une fonction continue sur un intervalle I et a un réel de I. Alors la fonction F définie sur I par F(x) = ∫ₐˣ f(t)dt est la primitive de f qui s'annule en a. » **Conséquence** — « F est dérivable sur I et F′(x) = f(x), pour tout x de I. »

C'est le théorème qui **garantit l'existence** d'une primitive pour toute fonction continue, même quand aucune formule ne l'exprime.

_Exemple détaillé_ — F(x) = ∫₀ˣ dt/(1 + t²) est définie et dérivable sur ℝ, avec F′(x) = 1/(1 + x²) > 0 : F est **strictement croissante sur ℝ**, et F(0) = 0. De même G(x) = ∫₁ˣ (sin t)/t dt est dérivable sur ]0, +∞[ avec G′(x) = (sin x)/x.

> **Théorème — dérivée de x ↦ ∫ₐ^{u(x)} f(t)dt** — « Soit f continue sur I, u dérivable sur J telle que u(J) ⊂ I et a un réel de I. Alors F définie sur J par F(x) = ∫ₐ^{u(x)} f(t)dt est dérivable sur J et F′(x) = f(u(x))·u′(x). » (Car F = G∘u avec G : x ↦ ∫ₐˣ f(t)dt.)

_Exemple détaillé_ — soit F(x) = ∫₀^{tan x} dt/(1 + t²) sur [0, π/4]. Ici u(x) = tan x, u′(x) = 1 + tan²x et f(t) = 1/(1 + t²), donc :

$$ F′(x) = 1/(1 + tan²x) × (1 + tan²x) = 1 $$

F est donc affine de pente 1, et F(0) = 0 : **F(x) = x** sur [0, π/4]. En x = π/4 (où tan x = 1), on en déduit un résultat spectaculaire :

$$ ∫₀¹ dt/(1 + t²) = F(π/4) = π/4 ≈ 0,785 $$

_Contrôle_ — c'est bien la valeur annoncée plus haut, et elle respecte l'encadrement 0,5 ≤ … ≤ 1 obtenu par l'inégalité de la moyenne ✓.

> **Théorème — parité** — « Soit f continue sur un intervalle I centré en 0 et a un réel de I. Si f est impaire alors ∫_{−a}ᵃ f(x)dx = 0. Si f est paire alors ∫_{−a}ᵃ f(x)dx = 2∫₀ᵃ f(x)dx. »

> **Théorème — périodicité** — « Soit f continue sur ℝ, périodique de période T. Pour tout réel a, ∫ₐ^{a+T} f(t)dt = ∫₀ᵀ f(t)dt. »

_Exemple détaillé (parité)_ — ∫_{−1}¹ t⁵/(t⁶ + 1) dt : le numérateur est impair, le dénominateur pair, donc l'intégrande est **impair** et l'intégrale vaut **0** — sans le moindre calcul. En revanche ∫_{−1}¹ |t³ + t| dt porte sur une fonction **paire** (valeur absolue d'une fonction impaire), et sur [0, 1] on a t³ + t ≥ 0 :

$$ ∫_{−1}¹ |t³ + t| dt = 2∫₀¹ (t³ + t)dt = 2[t⁴/4 + t²/2]₀¹ = 2(1/4 + 1/2) = 3/2 $$

_Exemple détaillé (périodicité)_ — ∫₀^{20π} |sin x| dx : la fonction |sin| est périodique de période **π** (et non 2π), et ∫₀^π sin x dx = [−cos x]₀^π = 2. L'intervalle [0, 20π] contient 20 périodes, donc l'intégrale vaut 20 × 2 = **40**.

> ⚠️ Avant d'invoquer la parité, vérifie que l'intervalle est **centré en 0**. Et pour |sin| ou |cos|, la période utile est π, pas 2π : c'est le piège classique du comptage de périodes.

## 👑 Suites définies par une intégrale

Beaucoup de problèmes de bac construisent une suite (Iₙ) à partir d'une intégrale dépendant de n. Trois gestes suffisent presque toujours : **encadrer** l'intégrande (pour la convergence), **intégrer par parties** (pour une relation de récurrence), **calculer** les premiers termes.

_Exemple détaillé_ — posons Iₙ = ∫₀^{π/2} xⁿ sin x dx et Jₙ = ∫₀^{π/2} xⁿ cos x dx (n ≥ 1). Une IPP sur Iₙ, avec f(x) = xⁿ et g′(x) = sin x (donc g(x) = −cos x) :

$$ Iₙ = [−xⁿ cos x]₀^{π/2} + n∫₀^{π/2} x^{n−1} cos x dx = 0 + nJₙ₋₁ $$

De même, avec g′(x) = cos x et g(x) = sin x : Jₙ = [xⁿ sin x]₀^{π/2} − n∫₀^{π/2} x^{n−1} sin x dx = **(π/2)ⁿ − nIₙ₋₁**.

Les deux relations s'amorcent avec I₁ = 1 et J₁ = π/2 − 1 (calculés par IPP plus haut). On en déduit en cascade :

$$ I₂ = 2J₁ = π − 2 ≈ 1,14     et     J₂ = (π/2)² − 2I₁ = π²/4 − 2 ≈ 0,47 $$

_Contrôle_ — J₂ = ∫₀^{π/2} x² cos x dx : c'est exactement la valeur trouvée par double IPP dans la section « Calculs d'intégrales » ✓. Deux chemins, un seul nombre.

_Exemple (intégrales de Wallis)_ — soit Iₙ = ∫₀^{π/2} cosⁿt dt. On a I₀ = π/2 et I₁ = 1 ; une IPP donne la récurrence Iₙ₊₂ = ((n + 1)/(n + 2))·Iₙ, d'où I₂ = I₀/2 = π/4, I₃ = (2/3)I₁ = 2/3, I₄ = (3/4)I₂ = 3π/16. Comme 0 ≤ cos^{n+1}t ≤ cosⁿt sur [0, π/2], la suite est **décroissante et positive**, donc convergente.

> 🗡️ **Le réflexe gagnant** : pour la convergence, encadre ; pour la valeur, cherche une **relation entre Iₙ et Iₙ₊₂** (jamais Iₙ₊₁ : la parité de n sépare les deux familles).

> 🏆 Sixième porte franchie, héros : tu sais lire une aire comme une différence F(b) − F(a), la découper par Chasles, l'encadrer sans la calculer, la retourner par parties, en tirer une moyenne, un volume, une suite. Il te reste à conquérir les fonctions ln et exp — et tu verras alors que même ∫₁² dx/x, l'aire que tu n'as pu qu'encadrer aujourd'hui, porte enfin un nom.
