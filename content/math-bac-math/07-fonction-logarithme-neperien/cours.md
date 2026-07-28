# ⚔️ Logarithme népérien — l'aire qui change les produits en sommes

> 💡 «Additionner est plus facile que multiplier : celui qui trouve la fonction qui transforme les produits en sommes tient la clé du calcul.»

Au chapitre précédent, une intégrale t'a résisté. Tu as encadré ∫₁² dx/x entre 7/12 et 5/6 par la méthode des rectangles, sans jamais pouvoir la calculer : aucune des primitives du chapitre 5 ne donne 1/x. En 1544 déjà, Michael Stifel avait remarqué qu'en alignant une progression arithmétique (…, −1, 0, 1, 2, 3, …) sur une progression géométrique (…, 1/2, 1, 2, 4, 8, …), **le produit d'en bas devient la somme d'en haut**. Napier (1614), Briggs (1624) et Bürgi (1620) en ont tiré les premières tables de logarithmes. Ce chapitre paie la dette du chapitre 6 : cette aire manquante porte enfin un nom, et ce nom est **ln**.

## 🏰 L'aire sous l'hyperbole : la fonction ln naît d'une intégrale

Tu sais déjà (chapitre 6) que si f est continue sur un intervalle I et a ∈ I, alors x ↦ ∫ₐˣ f(t)dt est **la primitive de f qui s'annule en a**. Applique-le à f : t ↦ 1/t, continue sur ]0, +∞[, avec a = 1. La primitive existe donc, même si aucune formule du chapitre 5 ne la produit — il suffit de lui donner un nom.

> **Définition — fonction logarithme népérien** — « On appelle fonction logarithme népérien et on note ln, la fonction x ↦ ln x = ∫₁ˣ 1/t dt, x > 0. »

Quatre conséquences tombent immédiatement de cette définition :

| Résultat                                    | D'où il vient                                            |
| ------------------------------------------- | -------------------------------------------------------- |
| ln est définie, continue et dérivable sur ]0, +∞[ | c'est une primitive de t ↦ 1/t sur ]0, +∞[          |
| ln′(x) = 1/x pour tout x > 0                | dérivée d'une primitive                                  |
| ln est **strictement croissante** sur ]0, +∞[ | sa dérivée 1/x est strictement positive                |
| ln 1 = 0                                    | ∫₁¹ 1/t dt = 0                                           |

Pour x > 1, ln x est **l'aire** (en u.a) comprise entre l'hyperbole y = 1/t, l'axe des abscisses et les droites t = 1, t = x. Pour 0 < x < 1, les bornes sont dans l'ordre inverse : l'intégrale change de signe, donc ln x < 0.

::: figure Pour x > 1, ln x est exactement l'aire coincée sous l'hyperbole y = 1/t entre t = 1 et t = x.
<svg viewBox="0 0 340 215"><polygon points="110,180 110,135 123,144 137.5,150 151,154 165,157.5 192.5,162 220,165 220,180" fill="#0f6e56" fill-opacity="0.18"/><path d="M45 180 H335" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M55 198 V55" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M335 180 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M55 55 l-3.5 7 l7 0 z" fill="#0f172a"/><path d="M85 98 L93.5 116 L100 125 L110 135 L123 144 L137.5 150 L151 154 L165 157.5 L192.5 162 L220 165 L247 167 L275 169 L302 170 L330 171" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><line x1="110" y1="135" x2="110" y2="180" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="220" y1="165" x2="220" y2="180" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="110" y="195" text-anchor="middle" fill="#0f172a">1</text><text x="220" y="195" text-anchor="middle" fill="#0f172a">x</text><text x="47" y="195" text-anchor="middle" fill="#0f172a">O</text><text x="160" y="174" text-anchor="middle" fill="#0f6e56">ln x</text><text x="272" y="158" fill="#0f6e56">y = 1/t</text></g></svg>
:::

_Exemple détaillé — encadrer ln 2 à la main._ Partage [1, 2] en trois intervalles de longueur 1/3. Sur chacun, 1/t est **décroissante** : le rectangle bâti sur la valeur de droite minore, celui bâti sur la valeur de gauche majore.

$$ (1/3)(f(4/3) + f(5/3) + f(2)) ≤ ln 2 ≤ (1/3)(f(1) + f(4/3) + f(5/3)) $$

$$ (1/3)(3/4 + 3/5 + 1/2) = 37/60 ≤ ln 2 ≤ (1/3)(1 + 3/4 + 3/5) = 47/60 $$

Soit 0,617 ≤ ln 2 ≤ 0,783. _Contrôle_ — la calculatrice donne ln 2 ≈ 0,693 : c'est bien dans l'encadrement, et c'est aussi le nombre que le chapitre 6 avait seulement su coincer entre 7/12 ≈ 0,583 et 5/6 ≈ 0,833. La dette est payée ✓.

::: figure Les trois rectangles verts minorent l'aire, les trois rectangles pointillés la majorent : ln 2 est pris en tenaille entre 37/60 et 47/60.
<svg viewBox="0 0 340 215"><g fill="#0f6e56" fill-opacity="0.18" stroke="#0f6e56" stroke-width="1.4"><rect x="70" y="102.5" width="73.33" height="82.5"/><rect x="143.33" y="119" width="73.34" height="66"/><rect x="216.67" y="130" width="73.33" height="55"/></g><g fill="none" stroke="#b45309" stroke-width="1.6" stroke-dasharray="5 4"><rect x="70" y="75" width="73.33" height="110"/><rect x="143.33" y="102.5" width="73.34" height="82.5"/><rect x="216.67" y="119" width="73.33" height="66"/></g><path d="M40 185 H325" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M325 185 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M70 75 L106.7 90.7 L143.3 102.5 L180 111.7 L216.7 119 L253.3 125 L290 130" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="70" y="202" text-anchor="middle" fill="#0f172a">1</text><text x="143.33" y="202" text-anchor="middle" fill="#0f172a">4/3</text><text x="216.67" y="202" text-anchor="middle" fill="#0f172a">5/3</text><text x="290" y="202" text-anchor="middle" fill="#0f172a">2</text><text x="248" y="68" fill="#0f172a">y = 1/t</text></g></svg>
:::

## ⚡ Comparer, résoudre : ln est une bijection

La stricte croissance se transforme en **outil de résolution**. Elle donne à la fois le sens direct et la réciproque.

> **Encadré** — « Soit a et b deux réels strictement positifs. ln a > ln b, si et seulement si, a > b. ln a = ln b, si et seulement si, a = b. ln a = 0, si et seulement si, a = 1. ln a > 0, si et seulement si, a > 1. ln a < 0, si et seulement si, 0 < a < 1. »

On établira plus bas que ln n'est pas majorée et tend vers −∞ en 0⁺ ; avec la continuité, le théorème des valeurs intermédiaires donne alors :

> **Théorème** — « La fonction ln réalise une bijection strictement croissante de ℝ*₊ sur ℝ. L'unique solution de l'équation ln x = 1 est le réel noté e. Ainsi, ln e = 1. Les calculatrices donnent des valeurs approchées du réel e, e ≈ 2,71828… »

Que e soit compris entre 2 et 3 se lit sur les encadrements : ln 2 ≤ 47/60 < 1, tandis qu'un découpage de [1, 3] en huit rectangles donne ln 3 ≥ 1 (on trouve ln 3 ≈ 1,099).

**Méthode en trois temps** pour toute équation ou inéquation en ln : (1) écrire les **conditions d'existence**, (2) ramener les deux membres à la forme ln A et ln B, (3) appliquer la bijection ou la croissance.

_Exemple détaillé_ — résoudre ln(x² + x + 1) = 0. Le trinôme x² + x + 1 a pour discriminant 1 − 4 = −3 < 0 : il est toujours strictement positif, l'équation existe sur ℝ. Or ln A = 0 ⟺ A = 1 :

$$ x² + x + 1 = 1 ⟺ x² + x = 0 ⟺ x(x + 1) = 0 $$

Solutions : **x = 0 et x = −1**. _Contrôle_ — pour x = −1, x² + x + 1 = 1 − 1 + 1 = 1 et ln 1 = 0 ✓.

_Exemple détaillé_ — résoudre ln(2x − 5) ≤ ln x. Conditions : 2x − 5 > 0 et x > 0, donc x > 5/2. La croissance donne 2x − 5 ≤ x, soit x ≤ 5. L'ensemble des solutions est **]5/2, 5]**. _Contrôle_ — pour x = 3 : ln 1 = 0 ≤ ln 3 ≈ 1,099 ✓ ; pour x = 6 : ln 7 ≈ 1,946 > ln 6 ≈ 1,792, exclu ✓.

_Exemple détaillé_ — résoudre (ln x)² + 2 ln x = 3 sur ]0, +∞[. On pose X = ln x : X² + 2X − 3 = 0, de racines X = 1 et X = −3. Puis on remonte, en utilisant ln e = 1 et ln(1/e³) = −ln(e³) = −3 :

$$ ln x = 1 ⟺ x = e     et     ln x = −3 ⟺ x = 1/e³ $$

Solutions : **{1/e³ ; e}**, soit environ {0,0498 ; 2,718}.

> ⚠️ Ne jamais «simplifier par ln». De ln(1 − x) = ln(2 + x) on tire 1 − x = 2 + x **seulement après** avoir écrit 1 − x > 0 et 2 + x > 0 ; ici x = −1/2, qui vérifie bien les deux conditions. Une solution obtenue hors du domaine est une fausse solution.

## 🧮 Les propriétés algébriques : le produit devient une somme

C'est la propriété historique, celle de Stifel. Sa démonstration est un bijou : à a > 0 fixé, les fonctions x ↦ ln(ax) et x ↦ ln x ont **la même dérivée** sur ]0, +∞[ (à savoir a/(ax) = 1/x), donc elles diffèrent d'une constante c ; en x = 1 on trouve c = ln a.

> **Théorème** — « Soit a et b deux réels strictement positifs. ln(a.b) = ln a + ln b. ln(a/b) = ln a − ln b. ln(1/b) = −ln b. »

> **Théorème** — « Soit a un réel strictement positif. • Pour tout entier p, ln(aᵖ) = p ln a • Pour tout entier p ≥ 2, ln(ᵖ√a) = (1/p) ln a. »

| Écriture         | Se transforme en   | Exemple                                     |
| ---------------- | ------------------ | ------------------------------------------- |
| ln(ab)           | ln a + ln b        | ln 6 = ln 2 + ln 3                          |
| ln(a/b)          | ln a − ln b        | ln(3/2) = ln 3 − ln 2                       |
| ln(1/b)          | −ln b              | ln(1/e) = −1                                |
| ln(aᵖ), p ∈ ℤ    | p ln a             | ln(e⁻²) = −2                                |
| ln(ᵖ√a), p ≥ 2   | (1/p) ln a         | ln(√e) = 1/2                                |

_Exemple détaillé_ — exprimer ln 108 et ln(81/8) à l'aide de ln 2 et ln 3. On factorise d'abord : 108 = 4 × 27 = 2²·3³ et 81/8 = 3⁴/2³.

$$ ln 108 = 2 ln 2 + 3 ln 3 ≈ 2(0,693) + 3(1,099) = 4,682 $$

$$ ln(81/8) = 4 ln 3 − 3 ln 2 ≈ 4,394 − 2,079 = 2,315 $$

_Contrôle_ — 81/8 = 10,125 et ln 10,125 ≈ 2,315 ✓.

_Exemple détaillé_ — simplifier ln(⁵√(2³)) et ln(⁴√e · ³√e). Pour le premier, on applique la racine p-ième au nombre a = 2³ : ln(⁵√(2³)) = (1/5)ln(2³) = (3/5)ln 2 ≈ 0,416. Pour le second, on transforme d'abord le produit en somme :

$$ ln(⁴√e · ³√e) = ln(⁴√e) + ln(³√e) = 1/4 + 1/3 = 7/12 $$

_Exemple détaillé (l'usage type)_ — quel est le plus petit entier naturel n tel que (1/2)ⁿ ≤ 10⁻⁴ ? On applique ln, qui est croissante, puis la règle de la puissance entière :

$$ n ln(1/2) ≤ −4 ln 10 ⟺ −n ln 2 ≤ −4 ln 10 ⟺ n ≥ 4 ln 10 / ln 2 ≈ 9,2103/0,6931 ≈ 13,29 $$

Donc **n = 14**. _Contrôle_ — 2¹³ = 8192 donne 1,22 × 10⁻⁴ (trop grand) et 2¹⁴ = 16384 donne 6,1 × 10⁻⁵ ✓. De même, le plus petit n avec (√2)ⁿ ≥ 10⁵ est n = 34, car (√2)³⁴ = 2¹⁷ = 131072 et (√2)³³ ≈ 92682.

> ⚠️ **ln(a + b) n'est PAS ln a + ln b.** Seul le **produit** devient une somme. Et attention au signe : ln(x²) = 2 ln|x|, pas 2 ln x — pour x < 0, ln x n'existe même pas.

## 📈 Limites, variations et courbe de ln

Trois arguments suffisent à décrire ln entièrement.

**1. ln n'est pas majorée.** Sur [2^k, 2^{k+1}], qui est de longueur 2^k, on a 1/t ≥ 1/2^{k+1} ; donc ∫_{2^k}^{2^{k+1}} dt/t ≥ 2^k/2^{k+1} = 1/2. En recollant les n morceaux par la relation de Chasles, ln(2ⁿ) = ∫₁^{2ⁿ} dt/t ≥ n/2, qui dépasse tout réel. Comme ln est croissante, lim_{x→+∞} ln x = +∞.

**2. Le comportement en 0⁺ se déduit par symétrie.** Les fonctions x ↦ ln x et x ↦ −ln(1/x) ont la même dérivée sur ]0, +∞[ et la même valeur en 1 : elles sont égales. Quand x → 0⁺, 1/x → +∞, donc lim_{x→0⁺} ln x = −∞. L'axe des ordonnées est **asymptote verticale**.

**3. ln croît moins vite que x.** Pour t ≥ 1 on a 1/t ≤ 1/√t ; en intégrant de 1 à x : ln x ≤ [2√t]₁ˣ = 2√x − 2. D'où 0 ≤ (ln x)/x ≤ 2/√x pour x ≥ 1, et le théorème des gendarmes conclut.

> **Théorème** — « lim_{x→+∞} ln x = +∞ ; lim_{x→0⁺} ln x = −∞ ; lim_{x→+∞} (ln x)/x = 0 ; lim_{x→1} (ln x)/(x − 1) = 1. »

La dernière limite est simplement le **nombre dérivé de ln en 1** : (ln x − ln 1)/(x − 1) → ln′(1) = 1. _Contrôle_ — pour x = 1,01 : ln(1,01)/0,01 ≈ 0,00995/0,01 = 0,995 ✓.

Le tableau de variation tient en une ligne : ln croît strictement de −∞ (en 0⁺) à +∞, en s'annulant en 1. La tangente T à la courbe au point d'abscisse 1 a pour coefficient directeur ln′(1) = 1 et passe par (1, 0) :

$$ T : y = x − 1 $$

::: figure La courbe de ln traverse l'axe en x = 1, passe par (e, 1), longe l'axe des ordonnées en −∞ et reste toujours sous sa tangente y = x − 1.
<svg viewBox="0 0 340 240"><path d="M40 150 H335" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M60 232 V25" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M335 150 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M60 25 l-3.5 7 l7 0 z" fill="#0f172a"/><path d="M76 174 L204 46" fill="none" stroke="#b45309" stroke-width="1.8" stroke-dasharray="6 4"/><path d="M66 226 L70 205 L76 187 L84 170 L92 159 L100 150 L110 141 L120 134 L140 122 L160 113 L180 106 L200 100 L220 95 L260 86 L300 78 L320 75" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round"/><line x1="60" y1="110" x2="169" y2="110" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="169" y1="110" x2="169" y2="150" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><g fill="#0f6e56"><circle cx="100" cy="150" r="3.5"/><circle cx="169" cy="110" r="3.5"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="52" y="166" text-anchor="middle" fill="#0f172a">O</text><text x="100" y="166" text-anchor="middle" fill="#0f172a">1</text><text x="169" y="166" text-anchor="middle" fill="#0f172a">e</text><text x="50" y="114" text-anchor="middle" fill="#0f172a">1</text><text x="303" y="70" fill="#0f6e56">C_ln</text><text x="196" y="40" text-anchor="end" fill="#b45309">y = x − 1</text></g></svg>
:::

Cette position relative n'est pas un dessin : la fonction g(x) = 1 − x + ln x a pour dérivée g′(x) = (1 − x)/x, donc un maximum en 1 où g(1) = 0. Ainsi g ≤ 0, c'est-à-dire :

$$ ln x ≤ x − 1     pour tout x > 0, avec égalité seulement en x = 1 $$

> 🗡️ **Construire la tangente sans calcul.** Soit A(a, ln a) un point de la courbe, H son projeté sur l'axe des ordonnées et K le point où la tangente en A coupe cet axe. La tangente en A s'écrit y = (1/a)(x − a) + ln a, donc y_K = ln a − 1 et y_H − y_K = **1**, quel que soit a. Place H, descends d'une unité : tu tiens K, donc la tangente.

## 🔮 Croissances comparées : ln perd toujours

Contre n'importe quelle puissance de x, le logarithme est le plus lent. C'est le résultat qui débloque presque toutes les formes indéterminées du chapitre.

> **Théorème** — « Pour tous entiers naturels non nuls n et m, lim_{x→+∞} lnⁿx/xᵐ = 0 et lim_{x→0⁺} xᵐ lnⁿx = 0. »

(La notation lnⁿx désigne (ln x)ⁿ.) La démonstration ramène tout au cas connu (ln y)/y → 0 : en posant y = ⁿ√(xᵐ), on a ln x = (n/m)ln y et xᵐ = yⁿ, donc

$$ (ln x)ⁿ/xᵐ = ((n/m) × (ln y)/y)ⁿ → 0 $$

Le second résultat s'obtient en remplaçant x par 1/y : xᵐ(ln x)ⁿ = (−1)ⁿ(ln y)ⁿ/yᵐ.

_Exemple détaillé_ — calculer lim_{x→+∞} (ln x)/(¹⁰√x). On pose y = ¹⁰√x, donc x = y¹⁰ et ln x = 10 ln y. Quand x → +∞, y → +∞ :

$$ (ln x)/(¹⁰√x) = 10 × (ln y)/y → 0 $$

_Contrôle_ — pour x = 10²⁰ : ln x ≈ 46,05 et ¹⁰√x = 100, quotient ≈ 0,46 ; pour x = 10⁴⁰ : 92,1/10000 ≈ 0,009. La descente est lente mais réelle ✓.

_Exemple détaillé_ — calculer lim_{x→+∞} (x − ln x). C'est une forme «+∞ − ∞» ; on met x en facteur :

$$ x − ln x = x(1 − (ln x)/x) → +∞ × (1 − 0) = +∞ $$

_Exemple_ — lim_{x→0⁺} x²(ln x)³ = 0 (croissance comparée, m = 2, n = 3) ; lim_{x→+∞} x⁴(1 − (ln x)⁵) = **−∞** (le facteur x⁴ tend vers +∞, le facteur 1 − (ln x)⁵ vers −∞) ; lim_{x→+∞} ln(2x + 3)/(3x + 4) = 0.

> ⚠️ **Le piège du 0⁺.** lim_{x→0⁺} (ln x)/x n'est **pas** 0 : ici ln x → −∞ **et** 1/x → +∞, les deux poussent dans le même sens, donc la limite est **−∞** (pour x = 10⁻³ : −6907,8). La croissance comparée ne s'applique qu'au produit xᵐ(ln x)ⁿ, où x^m écrase le logarithme. En revanche lim_{x→0⁺} (ln x + 1/x) = **+∞**, car ln x + 1/x = (1/x)(x ln x + 1) et x ln x → 0.

## 🛡️ Les fonctions ln(u) et ln|u|

En composant ln avec une fonction u, on fabrique la moitié des fonctions étudiées au bac. Le théorème de dérivation des composées donne la même formule dans les deux cas.

> **Théorème** — « Soit u une fonction dérivable sur un intervalle I et telle que u(x) > 0, pour tout réel x dans I. Alors la fonction f : x ↦ ln(u(x)) est dérivable sur I et f′(x) = u′(x)/u(x), pour tout x dans I. »

> **Théorème** — « Soit u une fonction dérivable sur un intervalle I et telle que u(x) ≠ 0, pour tout réel x dans I. Alors la fonction f : x ↦ ln|u(x)| est dérivable sur I et f′(x) = u′(x)/u(x), pour tout x dans I. »

La différence est **uniquement dans l'ensemble de définition** : ln(u) exige u > 0, ln|u| se contente de u ≠ 0. La dérivée, elle, est la même.

_Exemple détaillé_ — soit f(x) = ln(x² + x − 2). On résout d'abord u(x) > 0 : x² + x − 2 = (x + 2)(x − 1), positif à l'extérieur des racines. Donc D_f = ]−∞, −2[ ∪ ]1, +∞[, et sur chacun de ces intervalles :

$$ f′(x) = (2x + 1)/(x² + x − 2) $$

_Contrôle numérique_ — en x = 2 : la formule donne 5/4 = 1,25 ; le taux d'accroissement entre 2 et 2,01 vaut (ln 4,0501 − ln 4)/0,01 ≈ 1,247 ✓.

_Exemple détaillé_ — soit f(x) = ln|1 − x⁴|. Ici u ≠ 0 ⟺ x⁴ ≠ 1 ⟺ x ≠ 1 et x ≠ −1 : D_f = ℝ \ {−1 ; 1}. Avec u′(x) = −4x³ :

$$ f′(x) = −4x³/(1 − x⁴) $$

_Contrôle numérique_ — en x = 2 : la formule donne −32/(−15) ≈ 2,133 ; le taux d'accroissement entre 2 et 2,01 vaut ≈ 2,139 ✓.

_Exemple détaillé (étude complète)_ — soit f(x) = ln((x − 2)/(x + 1)) + x. Le quotient est strictement positif pour x < −1 ou x > 2 : D_f = ]−∞, −1[ ∪ ]2, +∞[. Avec u = (x − 2)/(x + 1), on a u′ = 3/(x + 1)², donc u′/u = 3/((x + 1)(x − 2)) et :

$$ f′(x) = 1 + 3/(x² − x − 2) = (x² − x + 1)/(x² − x − 2) $$

Le numérateur a pour discriminant −3 < 0 : il est toujours positif. Le dénominateur (x + 1)(x − 2) est positif sur D_f. Donc **f est strictement croissante sur chacun des deux intervalles**. Aux bornes : f → −∞ quand x → −∞ (car u → 1 donc ln u → 0), f → +∞ quand x → −1⁻, f → −∞ quand x → 2⁺, f → +∞ quand x → +∞. Comme f(x) − x = ln u → 0 en ±∞, la droite **y = x est asymptote oblique** aux deux branches.

> ⚠️ Résoudre u(x) > 0 **avant** de dériver. Écrire f′(x) = u′/u sur un intervalle où u s'annule ou change de signe est la faute la plus coûteuse du chapitre : la fonction n'y existe pas.

## 🧊 Deux primitives qui manquaient au chapitre 5

Le théorème de dérivation se lit à l'envers : c'est un théorème de primitives, et il comble le trou laissé par le chapitre 5 (aucune primitive de 1/x, aucune de u′/u).

> **Corollaire** — « Soit u une fonction dérivable sur un intervalle I et telle que u(x) ≠ 0, pour tout réel x dans I. Alors la fonction f : x ↦ u′(x)/u(x) admet pour primitive sur I la fonction f : x ↦ ln|u(x)| + k, où k est une constante réelle. »

> **Théorème** — « La fonction x ↦ x ln x − x est une primitive de la fonction x ↦ ln x sur ℝ*₊. »

La seconde se vérifie en une ligne : (x ln x)′ = ln x + x × (1/x) = ln x + 1, donc (x ln x − x)′ = ln x ✓.

_Exemple détaillé_ — primitive de f(x) = x/(1 − x²) sur ]1, +∞[. On reconnaît u = 1 − x², u′ = −2x, donc f = −(1/2)·u′/u. Une primitive est F(x) = −(1/2)ln|1 − x²| = −(1/2)ln(x² − 1) sur ]1, +∞[. _Vérification par dérivation_ : F′(x) = −(1/2)·2x/(x² − 1) = x/(1 − x²) ✓.

_Exemple détaillé_ — primitive de f(x) = (x + 1)/(3x − 2) sur ]−∞, 2/3[. Le degré du numérateur égale celui du dénominateur : on divise d'abord. Comme x + 1 = (1/3)(3x − 2) + 5/3 :

$$ f(x) = 1/3 + (5/3)/(3x − 2)     donc     F(x) = x/3 + (5/9)ln|3x − 2| $$

_Vérification_ : F′(x) = 1/3 + (5/9)·3/(3x − 2) = 1/3 + (5/3)/(3x − 2) = (x + 1)/(3x − 2) ✓.

_Exemple détaillé_ — primitive de f(x) = 1/(x ln x) sur ]1/e, 1[. Ici u(x) = ln x et u′(x) = 1/x : f = u′/u. Une primitive est F(x) = ln|ln x| = ln(−ln x), puisque ln x est **négatif** sur ]1/e, 1[.

_Exemple détaillé (IPP avec ln)_ — calculer ∫₁^e x ln x dx. On pose f(t) = ln t (qui se simplifie en dérivant) et g′(t) = t, donc g(t) = t²/2 :

$$ ∫₁^e t ln t dt = [t²/2 · ln t]₁^e − ∫₁^e (t/2)dt = e²/2 − [t²/4]₁^e = e²/2 − e²/4 + 1/4 = (e² + 1)/4 $$

Soit ≈ (7,389 + 1)/4 ≈ **2,097**. _Contrôle_ — sur [1 ; e] ≈ [1 ; 2,718], l'intégrande t ln t va de 0 à e ≈ 2,718 ; une aire d'environ 2,1 sur une largeur 1,72 est cohérente ✓. Au passage, ∫₁^e ln x dx = [x ln x − x]₁^e = 0 − (−1) = **1**.

## 👑 Encadrements, suites et la constante d'Euler

Le geste-clé du bac : quand une somme ou une intégrale résiste, **encadrer 1/t** puis intégrer.

_Exemple détaillé (l'encadrement fondamental)_ — pour x > 0, sur l'intervalle [x, x + 1] de longueur 1 on a 1/(x + 1) ≤ 1/t ≤ 1/x. En intégrant :

$$ 1/(x + 1) ≤ ln(x + 1) − ln x ≤ 1/x $$

_Contrôle_ — pour x = 1 : 1/2 ≤ ln 2 ≈ 0,693 ≤ 1 ✓.

_Exemple détaillé (la série harmonique diverge)_ — soit Sₙ = 1 + 1/2 + … + 1/n. L'encadrement précédent avec x = k donne 1/k ≥ ln(k + 1) − ln k. En sommant de k = 1 à n, la somme télescope :

$$ Sₙ ≥ ln(n + 1) → +∞ $$

Donc (Sₙ) **diverge** vers +∞, même si son terme général tend vers 0. _Contrôle_ — pour n = 10 : S₁₀ ≈ 2,929 et ln 11 ≈ 2,398 ✓.

_Exemple détaillé (la constante d'Euler)_ — posons Tₙ = Sₙ − ln n et Rₙ = S_{n−1} − ln n pour n ≥ 2. L'encadrement donne T_{n+1} − Tₙ = 1/(n + 1) − (ln(n + 1) − ln n) ≤ 0 : (Tₙ) **décroît**. De même R_{n+1} − Rₙ = 1/n − (ln(n + 1) − ln n) ≥ 0 : (Rₙ) **croît**. Enfin Tₙ − Rₙ = 1/n → 0 : les deux suites sont **adjacentes**. Leur limite commune est la constante d'Euler γ ≈ 0,5772 ; l'écart 1/n donne un encadrement d'amplitude 10⁻³ dès n ≥ 1000 (T₁₀₀₀ ≈ 0,57772).

_Exemple détaillé (suite d'intégrales)_ — soit uₙ = ∫₀¹ xⁿ ln(x + 2)dx, n ≥ 1. Pour x ∈ [0, 1] on a 2 ≤ x + 2 ≤ 3, donc ln 2 ≤ ln(x + 2) ≤ ln 3. En multipliant par xⁿ ≥ 0 et en intégrant :

$$ ln 2 × 1/(n + 1) ≤ uₙ ≤ ln 3 × 1/(n + 1)     donc     lim_{n→+∞} uₙ = 0 $$

Le premier terme se calcule par parties, en choisissant astucieusement g(t) = (t² − 4)/2 (dont la dérivée est bien t) pour que le quotient se simplifie :

$$ u₁ = [(t² − 4)/2 · ln(t + 2)]₀¹ − ∫₀¹ (t − 2)/2 dt = −(3/2)ln 3 + 2 ln 2 + 3/4 ≈ 0,488 $$

_Contrôle_ — l'encadrement donne (ln 2)/2 ≈ 0,347 ≤ u₁ ≤ (ln 3)/2 ≈ 0,549 : la valeur 0,488 y est bien ✓.

> 🗡️ **Le réflexe complet** : pour la convergence, encadre l'intégrande ; pour la valeur, intègre par parties en posant **f = ln** (c'est toujours lui qui se simplifie en dérivant) ; pour une somme, compare chaque terme à ∫ dt/t.

> 🏆 Septième porte franchie, héros. L'aire que le chapitre 6 n'avait pu qu'encadrer porte enfin un nom : ln. Tu sais la dériver, la composer, la primitiver, l'utiliser pour casser un produit, résoudre une inéquation, dompter une suite. Il te reste un dernier échange : ln transforme les produits en sommes — quelle fonction fait le trajet inverse et change les sommes en produits ? Le chapitre 8 te présentera sa réciproque, l'exponentielle.
