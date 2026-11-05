# ⚔️ Fonctions primitives — remonter de la dérivée à la fonction

> 💡 «Dériver, c'est lire la vitesse sur la position ; primitiver, c'est retrouver la position quand on ne connaît que la vitesse.»

Jusqu'ici, on partait d'une fonction pour calculer sa dérivée. Ce chapitre fait le chemin inverse : on connaît la dérivée, on cherche la fonction. Huit notions, de la définition aux techniques de réécriture, avec un fil rouge : un chariot qui roule sur un rail rectiligne, à la vitesse v(t) = 6t − 4 (en m/s) à l'instant t (en s), et dont on cherche la position x(t) (en m).

## 🎯 Primitive d'une fonction

Un chariot roule sur un rail rectiligne. Sa vitesse est v(t) = 6t − 4, et l'on sait que la vitesse est la dérivée de la position : x′ = v. On essaie x(t) = 3t² − 4t, puis x(t) = 3t² − 4t + 10.
Quelle fonction x convient, et comment s'en assurer sans se tromper de sens ?

::: definition
Soit f et F deux fonctions définies sur un intervalle I. **F est une primitive de f sur I** si F est dérivable sur I et si F′(x) = f(x) pour tout x de I.
:::

::: exemple La position du chariot

1. On veut une fonction x telle que x′ = v. On dérive la candidate x(t) = 3t² − 4t, qui est un polynôme donc dérivable sur ℝ.
2. x′(t) = 3 × 2t − 4 × 1 = 6t − 4, car (t²)′ = 2t et (t)′ = 1.
3. Donc x′(t) = v(t) pour tout réel t : x est une primitive de v sur ℝ.
4. La fonction x₂(t) = 3t² − 4t + 10 convient aussi : la dérivée d'une constante est 0, donc x₂′(t) = 6t − 4 = v(t).

:::

::: exemple Le même outil, sans situation

1. F(x) = x⁴ − 2x² + 7 est-elle une primitive de f(x) = 4x³ − 4x sur ℝ ? F est un polynôme, donc dérivable sur ℝ.
2. F′(x) = 4x³ − 2 × 2x + 0 = 4x³ − 4x, car (x⁴)′ = 4x³, (x²)′ = 2x et la dérivée de 7 est 0.
3. F′(x) = f(x) pour tout réel x : oui, F est une primitive de f sur ℝ.

:::

::: piege
**Erreur : vérifier en dérivant f au lieu de F.** Pour F(x) = x³ et f(x) = 3x², on calcule f′(x) = 6x, on constate que 6x ≠ x³ et l'on conclut que F n'est pas une primitive. L'erreur tente parce que « dériver » est le geste qu'on connaît, et qu'on l'applique à la fonction donnée en premier. Le sens correct est de dériver la candidate : F′(x) = 3x² = f(x), donc F est bien une primitive de f.
:::

::: propriete
F est une primitive de f sur I si et seulement si F′ = f sur I : f est la dérivée de F. Pour vérifier une primitive, on dérive la candidate F et l'on retrouve f.
Cas limite : F doit être dérivable en **tout** point de I. Soit f(x) = 3x² sur ℝ et F(x) = x³ + 1 pour x ≥ 0, F(x) = x³ − 1 pour x < 0. On a F(0) = 1 mais F(x) tend vers −1 quand x tend vers 0 par valeurs négatives : F n'est pas continue en 0, donc pas dérivable en 0, et ce n'est pas une primitive de f sur ℝ, bien que F′(x) = 3x² pour tout x ≠ 0.
:::

::: verifie À toi : une primitive d'une puissance
Vérifier que G(x) = (x² + 3)³ est une primitive de g(x) = 6x(x² + 3)² sur ℝ.

---

On dérive G, pas g : G est dérivable sur ℝ comme composée de polynômes, et G′(x) = 3(x² + 3)² × (x² + 3)′ = 3(x² + 3)² × 2x = 6x(x² + 3)². On retrouve g(x) pour tout réel x, donc G est une primitive de g sur ℝ.
:::

::: retenir
F est une primitive de f sur I quand F est dérivable sur I et F′ = f : on le vérifie en dérivant F.
:::

## 🧬 Toutes les primitives d'une fonction : F + c

Le chariot de la section précédente a deux positions possibles, 3t² − 4t et 3t² − 4t + 10, qui donnent la même vitesse : tout dépend d'où il est parti. On se demande combien de fonctions x vérifient x′ = v, comment elles se ressemblent, et si une vitesse plus compliquée admet toujours une position.

::: figure Trois positions possibles du chariot, c = 3, c = 0 et c = −2 : les courbes se déduisent l'une de l'autre par une translation verticale, et leurs tangentes en t = 1 sont parallèles, de pente v(1) = 2
<svg viewBox="0 0 352 250">
<title>Trois courbes de x(t) = 3t² − 4t + c, pour c = 3, 0 et −2, et leurs tangentes parallèles au point d'abscisse t = 1</title>
<line x1="42" y1="176" x2="346" y2="176" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="346,176 338,180 338,172" fill="#0f172a"/>
<line x1="52" y1="244" x2="52" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="52,14 56,22 48,22" fill="#0f172a"/>
<line x1="156" y1="173" x2="156" y2="179" stroke="#0f172a" stroke-width="1.2"/>
<line x1="260" y1="173" x2="260" y2="179" stroke="#0f172a" stroke-width="1.2"/>
<line x1="49" y1="111" x2="55" y2="111" stroke="#0f172a" stroke-width="1.2"/>
<line x1="49" y1="46" x2="55" y2="46" stroke="#0f172a" stroke-width="1.2"/>
<line x1="156" y1="98" x2="156" y2="234.5" stroke="#64748b" stroke-width="1.4" stroke-dasharray="5 4"/>
<polyline points="52,202 57.2,204.5 62.4,206.81 67.6,208.92 72.8,210.84 78,212.56 83.2,214.09 88.4,215.42 93.6,216.56 98.8,217.5 104,218.25 109.2,218.8 114.4,219.16 119.6,219.32 124.8,219.29 130,219.06 135.2,218.64 140.4,218.02 145.6,217.21 150.8,216.2 156,215 161.2,213.6 166.4,212.01 171.6,210.22 176.8,208.24 182,206.06 187.2,203.69 192.4,201.12 197.6,198.36 202.8,195.4 208,192.25 213.2,188.9 218.4,185.36 223.6,181.62 228.8,177.69 234,173.56 239.2,169.24 244.4,164.72 249.6,160.01 254.8,155.1 260,150 265.2,144.7 270.4,139.21 275.6,133.52 280.8,127.64 286,121.56 291.2,115.29 296.4,108.82 301.6,102.16" fill="none" stroke="#d97706" stroke-width="2.8"/>
<polyline points="52,176 57.2,178.5 62.4,180.81 67.6,182.92 72.8,184.84 78,186.56 83.2,188.09 88.4,189.42 93.6,190.56 98.8,191.5 104,192.25 109.2,192.8 114.4,193.16 119.6,193.32 124.8,193.29 130,193.06 135.2,192.64 140.4,192.02 145.6,191.21 150.8,190.2 156,189 161.2,187.6 166.4,186.01 171.6,184.22 176.8,182.24 182,180.06 187.2,177.69 192.4,175.12 197.6,172.36 202.8,169.4 208,166.25 213.2,162.9 218.4,159.36 223.6,155.62 228.8,151.69 234,147.56 239.2,143.24 244.4,138.72 249.6,134.01 254.8,129.1 260,124 265.2,118.7 270.4,113.21 275.6,107.52 280.8,101.64 286,95.56 291.2,89.29 296.4,82.82 301.6,76.16" fill="none" stroke="#0f6e56" stroke-width="2.8"/>
<polyline points="52,137 57.2,139.5 62.4,141.81 67.6,143.92 72.8,145.84 78,147.56 83.2,149.09 88.4,150.42 93.6,151.56 98.8,152.5 104,153.25 109.2,153.8 114.4,154.16 119.6,154.32 124.8,154.29 130,154.06 135.2,153.64 140.4,153.02 145.6,152.21 150.8,151.2 156,150 161.2,148.6 166.4,147.01 171.6,145.22 176.8,143.24 182,141.06 187.2,138.69 192.4,136.12 197.6,133.36 202.8,130.4 208,127.25 213.2,123.9 218.4,120.36 223.6,116.62 228.8,112.69 234,108.56 239.2,104.24 244.4,99.72 249.6,95.01 254.8,90.1 260,85 265.2,79.7 270.4,74.21 275.6,68.52 280.8,62.64 286,56.56 291.2,50.29 296.4,43.82 301.6,37.16" fill="none" stroke="#2563eb" stroke-width="2.8"/>
<line x1="114.4" y1="225.4" x2="197.6" y2="204.6" stroke="#0f172a" stroke-width="2.4"/>
<circle cx="156" cy="215" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<line x1="114.4" y1="199.4" x2="197.6" y2="178.6" stroke="#0f172a" stroke-width="2.4"/>
<circle cx="156" cy="189" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<line x1="114.4" y1="160.4" x2="197.6" y2="139.6" stroke="#0f172a" stroke-width="2.4"/>
<circle cx="156" cy="150" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="149" y="169" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="260" y="169" text-anchor="middle" fill="#0f172a" font-size="11">2</text><text x="45" y="115" text-anchor="end" fill="#0f172a" font-size="11">5</text><text x="45" y="50" text-anchor="end" fill="#0f172a" font-size="11">10</text><text x="344" y="191" text-anchor="end" fill="#0f172a" font-size="12">t</text><text x="60" y="22" text-anchor="start" fill="#0f172a" font-size="12">x</text><text x="162" y="242.5" text-anchor="start" fill="#0f172a" font-size="11">t = 1</text><text x="307.6" y="41.16" text-anchor="start" fill="#2563eb" font-size="12">c = 3</text><text x="307.6" y="80.16" text-anchor="start" fill="#0f6e56" font-size="12">c = 0</text><text x="307.6" y="106.16" text-anchor="start" fill="#d97706" font-size="12">c = −2</text></g>
</svg>
:::

Chaque courbe est celle de t ↦ 3t² − 4t + c : changer c, c'est décaler la courbe verticalement. En t = 1, la tangente de chacune a pour pente x′(1) = v(1) = 6 − 4 = 2 : le décalage ne change pas la vitesse.

::: exemple Toutes les positions possibles

1. x(t) = 3t² − 4t est une primitive de v(t) = 6t − 4 sur ℝ (section précédente).
2. Soit y une autre primitive de v sur ℝ. Alors (y − x)′ = y′ − x′ = v − v = 0 sur ℝ.
3. Une fonction dont la dérivée est nulle sur un intervalle est constante sur cet intervalle : y − x = c, donc y(t) = 3t² − 4t + c.
4. Réciproquement, chaque fonction 3t² − 4t + c est une primitive de v, puisque la dérivée de c est 0.

:::

::: piege
**Erreur : écrire « la primitive de v est 3t² − 4t » comme si elle était unique.** On ajoute rarement la constante parce que la première fonction trouvée « marche ». Mais 3t² − 4t + 10 marche aussi, et 3t² − 4t − 7 également : il y en a une infinité. Il faut écrire l'ensemble de toutes les primitives, {3t² − 4t + c ; c ∈ ℝ}, ou dire « une primitive de v ».
:::

::: propriete
**Existence** (théorème admis) : toute fonction continue sur un intervalle I admet des primitives sur I.
**Ensemble des primitives** : si F est une primitive de f sur I, alors f admet une infinité de primitives sur I, qui sont toutes de la forme F + c, c étant un réel quelconque : l'ensemble est {F + c ; c ∈ ℝ}.
Cas limite : l'intervalle est indispensable. Soit f(x) = 1/x² sur ℝ*, qui n'est pas un intervalle, et F(x) = −1/x. La fonction G égale à −1/x + 1 pour x > 0 et à −1/x pour x < 0 est dérivable en tout x non nul avec G′ = f, comme F. Pourtant G − F vaut 1 sur ]0 ; +∞[ et 0 sur ]−∞ ; 0[ : ce n'est pas une constante.
:::

::: exemple Le même outil, sans situation

1. On sait que F(x) = x³ − x est une primitive de f(x) = 3x² − 1 sur ℝ. Les primitives de f sur ℝ sont donc les fonctions x³ − x + c, avec c réel.
2. x ↦ x³ − x + 5 en est une (c = 5).
3. x ↦ x³ − 2x + 5 n'en est pas une : sa dérivée est 3x² − 2, différente de f, et la différence avec F n'est pas constante.

:::

::: verifie À toi : une autre primitive ?
On sait que x ↦ x⁴ − 3x est une primitive de f(x) = 4x³ − 3 sur ℝ. Les fonctions x ↦ x⁴ − 3x + 2 et x ↦ x⁴ − 2x sont-elles aussi des primitives de f ?

---

La première est de la forme F + c avec c = 2 : sa dérivée est 4x³ − 3 + 0 = f(x), c'est une primitive. La seconde diffère de F par x, qui n'est pas une constante : sa dérivée est 4x³ − 2 ≠ f(x), ce n'est pas une primitive.
:::

::: retenir
Si F est une primitive de f sur un intervalle I, les primitives de f sur I sont exactement les F + c, c réel ; toute fonction continue sur I en possède.
:::

## 📌 Une primitive imposée : la condition initiale

Parmi toutes les positions 3t² − 4t + c du chariot, une seule est la sienne. On apprend qu'il passe au point d'abscisse 2 m à l'instant t = 1 s.
Quelle valeur de c choisir, et en existe-t-il toujours une seule ?

::: exemple La position du chariot, à partir d'un passage connu

1. Les positions possibles sont x(t) = 3t² − 4t + c (section précédente).
2. La condition x(1) = 2 s'écrit 3 − 4 + c = 2, donc c − 1 = 2 et c = 3.
3. x(t) = 3t² − 4t + 3. Contrôle : x(1) = 3 − 4 + 3 = 2 ✓.
4. Le chariot est donc en x(3) = 27 − 12 + 3 = 18 m à l'instant t = 3 s.

:::

On retrouve cette idée avec une aire. Dans un repère orthonormé, la droite D : y = 2x, un point A de D d'abscisse x > 0 et le point B(x ; 0) délimitent un triangle OAB.

::: figure Le triangle OAB sous la droite D : y = 2x, dessiné pour x = 3 : base x, hauteur 2x, aire S(x) = x²
<svg viewBox="0 0 340 262">
<title>Le triangle OAB sous la droite D : y = 2x, avec A(3 ; 6) et B(3 ; 0)</title>
<polygon points="48,214 132,46 132,214" fill="#d97706" fill-opacity="0.22" stroke="#d97706" stroke-width="2.4"/>
<line x1="38" y1="214" x2="300" y2="214" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="300,214 292,218 292,210" fill="#0f172a"/>
<line x1="48" y1="226" x2="48" y2="8" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="48,8 52,16 44,16" fill="#0f172a"/>
<line x1="48" y1="214" x2="160" y2="-10" stroke="#0f6e56" stroke-width="3"/>
<line x1="76" y1="211" x2="76" y2="217" stroke="#0f172a" stroke-width="1.2"/>
<line x1="104" y1="211" x2="104" y2="217" stroke="#0f172a" stroke-width="1.2"/>
<line x1="132" y1="211" x2="132" y2="217" stroke="#0f172a" stroke-width="1.2"/>
<line x1="160" y1="211" x2="160" y2="217" stroke="#0f172a" stroke-width="1.2"/>
<line x1="45" y1="158" x2="51" y2="158" stroke="#0f172a" stroke-width="1.2"/>
<line x1="45" y1="102" x2="51" y2="102" stroke="#0f172a" stroke-width="1.2"/>
<line x1="45" y1="46" x2="51" y2="46" stroke="#0f172a" stroke-width="1.2"/>
<path d="M 123 214 L 123 205 L 132 205" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="132" cy="46" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="132" cy="214" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="48" cy="214" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="39" y="229" text-anchor="middle" fill="#0f172a" font-size="13">O</text><text x="135" y="230" text-anchor="middle" fill="#0f172a" font-size="13">B</text><text x="123" y="38" text-anchor="middle" fill="#0f172a" font-size="13">A</text><text x="90" y="242" text-anchor="middle" fill="#0f172a" font-size="12">base : x</text><text x="140" y="134" text-anchor="start" fill="#0f172a" font-size="12">hauteur : 2x</text><text x="152" y="34" text-anchor="start" fill="#0f6e56" font-size="12">D : y = 2x</text><text x="76" y="228" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="104" y="228" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="160" y="228" text-anchor="middle" fill="#0f172a" font-size="10">4</text><text x="41" y="162" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="41" y="106" text-anchor="end" fill="#0f172a" font-size="10">4</text><text x="41" y="50" text-anchor="end" fill="#0f172a" font-size="10">6</text></g>
</svg>
:::

::: exemple Une aire qui est une primitive

1. La base OB mesure x et la hauteur AB mesure 2x, donc l'aire est S(x) = (1/2) × x × 2x = x².
2. S′(x) = 2x = f(x) en prenant f(x) = 2x : S est une primitive de f sur [0 ; +∞[.
3. Les primitives de f sont les x² + c, et S(0) = 0 : S est celle qui vaut 0 en 0, c'est-à-dire c = 0. Pour x = 3, l'aire du triangle de la figure est S(3) = 9.

:::

::: piege
**Erreur : ajouter la valeur imposée à la primitive trouvée, au lieu de la comparer.** Pour le chariot, on voit F₀(1) = 3 − 4 = −1 avec F₀(t) = 3t² − 4t, et x(1) doit valoir 2. On écrit c = 2 + (−1) = 1, d'où x(t) = 3t² − 4t + 1. L'erreur tente parce que « + c » invite à additionner. Mais cette fonction donne x(1) = 0, pas 2. La constante comble l'écart : c = 2 − (−1) = 3.
:::

::: propriete
Soit f continue sur un intervalle I, a un réel de I et b un réel. Il existe **une seule** primitive F de f sur I telle que F(a) = b.
Méthode : on écrit une primitive F₀, on pose F = F₀ + c, on résout F₀(a) + c = b, donc c = b − F₀(a).
Cas limite : a doit appartenir à I, et l'intervalle compte. Pour f(x) = −1/x², la primitive qui s'annule en −1 sur ]−∞ ; 0[ est x ↦ 1/x + 1 (car F(−1) = −1 + 1 = 0), et celle qui s'annule en 1 sur ]0 ; +∞[ est x ↦ 1/x − 1 : deux constantes différentes pour la même formule 1/x.
:::

::: exemple Le même outil, sans situation

1. Soit f(x) = 3x² − 2 sur ℝ et F la primitive de f telle que F(1) = 4.
2. Une primitive de f est F₀(x) = x³ − 2x (dérivée : 3x² − 2). Donc F = F₀ + c.
3. F₀(1) = 1 − 2 = −1, donc −1 + c = 4 et c = 4 − (−1) = 5.
4. F(x) = x³ − 2x + 5. Contrôle : F(1) = 1 − 2 + 5 = 4 ✓.

:::

::: verifie À toi : une condition en un point négatif
Déterminer la primitive F de f(x) = 4x³ − 6x sur ℝ telle que F(−1) = 2.

---

Une primitive est F₀(x) = x⁴ − 3x² (dérivée : 4x³ − 6x). On pose F = F₀ + c. Comme F₀(−1) = 1 − 3 = −2, la condition donne −2 + c = 2, donc c = 4 et F(x) = x⁴ − 3x² + 4. Contrôle : F(−1) = 1 − 3 + 4 = 2 ✓.
:::

::: retenir
Une primitive qui prend la valeur b en a existe et est unique : c = b − F₀(a).
:::

## 📚 Les primitives des fonctions usuelles

On connaît les dérivées de x³, de 1/x, de √x, de sin et de cos. Lues à l'envers, elles fournissent des primitives. Mais que fait-on pour xⁿ avec n quelconque, pour 1/√x ou pour cos(3x + π/4) ?

::: exemple Trois lectures à l'envers

1. f(x) = x⁵. Comme (x⁶)′ = 6x⁵, on divise par 6 : F(x) = x⁶/6. On augmente l'exposant de 1 et on divise par le nouvel exposant.
2. f(x) = 1/√x sur ]0 ; +∞[. Comme (√x)′ = 1/(2√x), la fonction 2√x a pour dérivée 1/√x : F(x) = 2√x.
3. f(x) = cos(3x + π/4). Comme (sin(3x + π/4))′ = 3cos(3x + π/4) (composée, facteur 3), on divise par 3 : F(x) = (1/3) sin(3x + π/4).
4. f(x) = 1 + tan²(3x). Comme (tan 3x)′ = 3(1 + tan²(3x)), on divise par 3 : F(x) = (1/3) tan(3x), sur tout intervalle où cos(3x) ≠ 0.

:::

::: piege
**Erreur : recopier la ligne « cos a pour primitive sin » sans tenir compte de l'intérieur.** On écrit que x ↦ sin(3x) est une primitive de cos(3x). L'erreur tente parce que le tableau de base ne montre pas de 3. Mais (sin 3x)′ = 3cos(3x), pas cos(3x). Il faut diviser par le coefficient de x : (1/3) sin(3x).
:::

::: propriete
Dans le tableau, c désigne un réel quelconque : toutes les primitives sont F + c. On note tan x (aussi tg x dans le manuel) et cotan x pour la cotangente.

| f(x) | une primitive F(x) | sur l'intervalle |
| --- | --- | --- |
| a (constante) | ax | ℝ |
| xⁿ, n entier ≥ 1 (dont x) | xⁿ⁺¹/(n + 1) | ℝ |
| xⁿ, n entier ≤ −2 (dont 1/x²) | xⁿ⁺¹/(n + 1) | ]−∞ ; 0[ ou ]0 ; +∞[ |
| 1/√x | 2√x | ]0 ; +∞[ |
| cos x | sin x | ℝ |
| sin x | −cos x | ℝ |
| 1/cos²x, c'est-à-dire 1 + tan²x | tan x | tout intervalle où cos x ≠ 0 |
| 1/sin²x, c'est-à-dire 1 + cotan²x | −cotan x | tout intervalle où sin x ≠ 0 |
| cos(ax + b), a ≠ 0 | (1/a) sin(ax + b) | ℝ |
| sin(ax + b), a ≠ 0 | −(1/a) cos(ax + b) | ℝ |
| 1 + tan²(ax + b), a ≠ 0 | (1/a) tan(ax + b) | tout intervalle où cos(ax + b) ≠ 0 |
| 1 + cotan²(ax + b), a ≠ 0 | −(1/a) cotan(ax + b) | tout intervalle où sin(ax + b) ≠ 0 |

Cas limite : la formule divise par n + 1, elle exclut donc n = −1. La fonction 1/x n'a pas de primitive dans ce tableau : elle sera construite plus loin dans le cours.
:::

::: verifie À toi : un sinus décalé
Donner une primitive de f(x) = sin(4x − π/3) sur ℝ.

---

Dans la ligne sin(ax + b), a = 4 et b = −π/3. Comme (cos(4x − π/3))′ = −4 sin(4x − π/3), il faut diviser par −4 : F(x) = −(1/4) cos(4x − π/3). Contrôle : F′(x) = −(1/4) × (−4 sin(4x − π/3)) = f(x).
:::

::: retenir
On lit le tableau des dérivées à l'envers ; pour cos(ax + b) et sin(ax + b), on divise par le coefficient a de x.
:::

## ➕ La linéarité : primitiver terme à terme

La vitesse du chariot s'écrit v(t) = 6t − 4 = 6 × t + (−4) × 1. On connaît une primitive de t, qui est t²/2, et une de 1, qui est t.
Peut-on primitiver chaque morceau, puis recombiner avec les mêmes coefficients ?

::: exemple Retrouver la position du chariot

1. Une primitive de t est t²/2 et une primitive de 1 est t.
2. On recombine avec les coefficients de v : 6 × t²/2 + (−4) × t = 3t² − 4t.
3. On reconnaît x(t), la primitive de la section 1 : la méthode donne bien la bonne fonction.

:::

::: exemple Le même outil, sans situation

1. Soit f(x) = 6x² + 3cos(2x) − 4/x² sur ]0 ; +∞[. On primitive chaque terme du tableau.
2. 6x² a pour primitive 6 × x³/3 = 2x³ ; 3cos(2x) a pour primitive 3 × (1/2) sin(2x) = (3/2) sin(2x) ; −4/x² a pour primitive −4 × (−1/x) = 4/x.
3. F(x) = 2x³ + (3/2) sin(2x) + 4/x. Contrôle : F′(x) = 6x² + 3cos(2x) − 4/x² ✓.

:::

::: piege
**Erreur : primitiver un produit facteur par facteur.** Pour f(x) = x × x² = x³, on multiplie les primitives de chaque facteur : (x²/2) × (x³/3) = x⁵/6. L'erreur tente parce que la linéarité marche pour les sommes. Mais (x⁵/6)′ = 5x⁴/6 ≠ x³. La bonne primitive est x⁴/4. La linéarité ne concerne que les sommes et les multiples par une constante.
:::

::: propriete
Soit f et g continues sur I, α et β deux réels, F et G des primitives de f et g sur I. Alors αF + βG est une primitive de αf + βg sur I. En effet (αF + βG)′ = αF′ + βG′ = αf + βg.
Cas limite : si F et G sont deux primitives de la même fonction f, alors F + G est une primitive de 2f et non de f (α = β = 1, g = f). Une primitive de f est (F + G)/2.
:::

::: verifie À toi : une somme de trois termes
Donner une primitive de h(x) = 5x⁴ − 2 sin(3x) + 7 sur ℝ.

---

On primitive terme à terme : 5x⁴ donne 5 × x⁵/5 = x⁵ ; −2 sin(3x) donne −2 × (−(1/3) cos(3x)) = (2/3) cos(3x) ; 7 donne 7x. Donc H(x) = x⁵ + (2/3) cos(3x) + 7x. Contrôle : H′(x) = 5x⁴ − 2 sin(3x) + 7 ✓.
:::

::: retenir
Une primitive de αf + βg est αF + βG ; cela vaut pour les sommes et les constantes, jamais pour les produits.
:::

## 🔗 Reconnaître u′uⁿ et u′/√u

Dérivons (x² + 4)³ : on obtient 3(x² + 4)² × 2x. La dérivée d'une puissance de u contient un facteur u′. Lue à l'envers, cette égalité permet de primitiver f(x) = x(x² + 4)², qui contient x = (1/2) × 2x.
Comment reconnaître cette structure et en déduire la primitive ?

::: exemple Puissance d'une fonction

1. f(x) = x(x² + 4)². On pose u(x) = x² + 4, donc u′(x) = 2x.
2. f(x) = (1/2) × 2x × (x² + 4)² = (1/2) u′ u², car on fait apparaître u′ en compensant par 1/2.
3. Une primitive de u′u² est u³/3, car (u³)′ = 3u′u².
4. F(x) = (1/2) × u³/3 = (1/6)(x² + 4)³. Contrôle : F′(x) = (1/6) × 3(x² + 4)² × 2x = x(x² + 4)² ✓.

:::

::: exemple Avec une fonction trigonométrique

1. f(x) = sin x cos³x. On pose u(x) = cos x, donc u′(x) = −sin x.
2. f(x) = −u′ u³, car −u′ = sin x.
3. Une primitive de u′u³ est u⁴/4, donc F(x) = −u⁴/4 = −cos⁴x/4. Contrôle : F′(x) = −4cos³x × (−sin x)/4 = sin x cos³x ✓.

:::

::: exemple Exposant négatif et racine

1. f(x) = 2x/(x² + 1)² sur ℝ. Avec u(x) = x² + 1, qui ne s'annule jamais, u′(x) = 2x : f = u′/u² = u′u⁻². Une primitive de u′u⁻² est u⁻¹/(−1) = −1/u : F(x) = −1/(x² + 1).
2. f(x) = x/√(x² + 9) sur ℝ. Avec u(x) = x² + 9 > 0, u′(x) = 2x : f = (1/2) u′/√u. Comme (√u)′ = u′/(2√u), une primitive de u′/√u est 2√u, donc F(x) = (1/2) × 2√u = √(x² + 9).

:::

::: piege
**Erreur : appliquer la règle des puissances à u comme si u était x.** Pour f(x) = (2x + 1)², on écrit que F(x) = (2x + 1)³/3. L'erreur tente parce que la règle « puissance + 1, divisé par le nouvel exposant » est celle de x. Mais ici u(x) = 2x + 1 et u′(x) = 2 est absent : F′(x) = 2(2x + 1)² ≠ f(x). Il faut compenser le facteur u′ : f = (1/2) u′u², donc F(x) = (2x + 1)³/6.
:::

::: propriete
Soit u dérivable sur I.
- f = u′uⁿ, avec n entier différent de −1 : F = uⁿ⁺¹/(n + 1). Si n < 0, u ne doit pas s'annuler sur I. Cela couvre u′/u² (F = −1/u) et u′/uⁿ pour n ≥ 2 (F = −1/((n − 1)uⁿ⁻¹)).
- f = u′/√u, avec u > 0 sur I : F = 2√u.

Cas limite : n = −1 est exclu (u′/u n'a pas de primitive par cette règle), et n = 1 dans u′/uⁿ aussi, car n − 1 = 0.
:::

::: verifie À toi : une puissance cubique
Déterminer une primitive de f(x) = x²(x³ + 1)³ sur ℝ.

---

On pose u(x) = x³ + 1, donc u′(x) = 3x². Alors f = (1/3) u′u³, car on fait apparaître 3x². Une primitive de u′u³ est u⁴/4, donc F(x) = (1/3) × (x³ + 1)⁴/4 = (x³ + 1)⁴/12. Contrôle : F′(x) = (4/12)(x³ + 1)³ × 3x² = x²(x³ + 1)³ ✓.
:::

::: retenir
Pour u′uⁿ, on repère u et u′, on compense la constante manquante, et l'on obtient uⁿ⁺¹/(n + 1) ; pour u′/√u, la primitive est 2√u.
:::

## 🧩 Produit, quotient, composée : (uv)′, (u/v)′, (v∘u)′

Dérivons x sin x : on obtient sin x + x cos x. Lue à l'envers, cette égalité donne une primitive de sin x + x cos x. Le produit, le quotient et la composée ont chacun leur dérivée, donc chacun donne une forme à reconnaître.
Quelles sont ces trois formes, et comment les repérer ?

::: exemple Un produit

1. f(x) = sin x + x cos x. On pose u(x) = x et v(x) = sin x, donc u′(x) = 1 et v′(x) = cos x.
2. u′v + v′u = sin x + x cos x = f(x) : f est la dérivée du produit uv.
3. F(x) = uv = x sin x. Contrôle : F′(x) = sin x + x cos x ✓.

:::

::: exemple Un quotient

1. f(x) = (1 − x²)/(x² + 1)². On pose u(x) = x et v(x) = x² + 1, qui ne s'annule jamais.
2. (u′v − v′u)/v² = (1 × (x² + 1) − 2x × x)/(x² + 1)² = (1 − x²)/(x² + 1)² = f(x).
3. F(x) = u/v = x/(x² + 1).

:::

::: exemple Une composée

1. f(x) = 3x² sin(x³). On pose u(x) = x³, donc u′(x) = 3x², et v′ = sin, donc v = −cos.
2. f(x) = u′(x) × (v′∘u)(x) = 3x² sin(x³).
3. F(x) = (v∘u)(x) = −cos(x³). Contrôle : F′(x) = sin(x³) × 3x² ✓.

:::

::: piege
**Erreur : oublier le signe quand la composée contient sin.** Pour f(x) = 3x² sin(x³), on écrit F(x) = cos(x³). L'erreur tente parce que « sin donne cos » est un réflexe. Mais (cos(x³))′ = −sin(x³) × 3x² = −f(x). La primitive de sin est −cos : F(x) = −cos(x³).
:::

::: propriete
Soit u et v dérivables.
- f = u′v + v′u : F = uv.
- f = (u′v − v′u)/v², avec v qui ne s'annule pas sur I : F = u/v.
- f = (v′∘u) × u′ : F = v∘u.

Cas limite : si la forme n'apparaît qu'à une constante près, on compense comme à la section précédente. Par exemple f(x) = x sin(x²) = (1/2) × 2x × sin(x²) donne F(x) = −(1/2) cos(x²).
:::

::: verifie À toi : un autre quotient
Déterminer une primitive de g(x) = (4 − x²)/(x² + 4)² sur ℝ, en posant u(x) = x et v(x) = x² + 4.

---

On calcule u′v − v′u = 1 × (x² + 4) − 2x × x = 4 − x², qui est le numérateur de g, avec le dénominateur v² = (x² + 4)². Donc g = (u′v − v′u)/v² et G(x) = u/v = x/(x² + 4).
:::

::: retenir
Trois formes de dérivées donnent trois primitives : uv pour u′v + v′u, u/v pour (u′v − v′u)/v², v∘u pour (v′∘u)u′.
:::

## 🛠️ Réécrire avant de primitiver

Soit f(x) = (x² + 1)². On pourrait y voir u² avec u = x² + 1, mais u′ = 2x est absent et x n'est pas une constante : la règle de la section précédente ne s'applique pas. Quand aucune forme n'apparaît, on réécrit f pour la transformer en somme de termes connus.
Quelles réécritures sont utiles, et comment les mener ?

::: exemple Développer

1. (x² + 1)² = (x²)² + 2 × x² × 1 + 1² = x⁴ + 2x² + 1, par l'identité remarquable (a + b)² = a² + 2ab + b².
2. Chaque terme est dans le tableau : x⁴ → x⁵/5, 2x² → 2x³/3, 1 → x.
3. F(x) = x⁵/5 + 2x³/3 + x. Contrôle : F′(x) = x⁴ + 2x² + 1 ✓.

:::

::: exemple Transformer un produit de sinus et cosinus

1. f(x) = sin 5x cos x. Les formules d'addition donnent sin(a + b) + sin(a − b) = 2 sin a cos b.
2. Avec a = 5x et b = x : sin 6x + sin 4x = 2 sin 5x cos x, donc f(x) = (1/2)(sin 6x + sin 4x).
3. Chaque terme est dans le tableau : F(x) = (1/2)(−cos 6x/6 − cos 4x/4) = −cos 6x/12 − cos 4x/8.

:::

::: exemple Une puissance de sinus

1. f(x) = sin³x. On écrit sin³x = sin x × sin²x = sin x (1 − cos²x) = sin x − sin x cos²x, car sin²x + cos²x = 1.
2. sin x a pour primitive −cos x. Pour sin x cos²x, avec u = cos x et u′ = −sin x, on a sin x cos²x = −u′u², de primitive −cos³x/3.
3. F(x) = −cos x − (−cos³x/3) = −cos x + cos³x/3. Contrôle : F′(x) = sin x − cos²x sin x = sin x (1 − cos²x) = sin³x ✓.

:::

::: piege
**Erreur : développer un carré en oubliant le double produit.** On écrit (x² + 1)² = x⁴ + 1, puis F(x) = x⁵/5 + x. L'erreur tente parce que le carré « passe » sur chaque terme. Mais (a + b)² = a² + 2ab + b² : le terme 2x² manque, et la dérivée de F est x⁴ + 1 ≠ f(x).
:::

::: methode Réécrire f avant de primitiver
1. Développer ou découper : (x⁴ − 1)/x² = x² − 1/x², puis primitiver chaque terme (F(x) = x³/3 + 1/x sur ]0 ; +∞[).
2. Transformer un produit de sinus et de cosinus en somme avec les formules d'addition : sin a cos b = (1/2)[sin(a + b) + sin(a − b)] et cos a cos b = (1/2)[cos(a + b) + cos(a − b)].
3. Pour sin³x ou cos³x, écrire sin³x = sin x (1 − cos²x) et cos³x = cos x (1 − sin²x), puis reconnaître u′uⁿ.
4. Pour une fraction annoncée sous la forme ax + b + c/(x − 1)², développer (ax + b)(x − 1)² + c et identifier les coefficients avec ceux du numérateur. Pour f(x) = (2x³ − 3x² + 4)/(x − 1)², on trouve a = 2, b = 1, c = 3 : (2x + 1)(x² − 2x + 1) + 3 = 2x³ − 3x² + 4. D'où f(x) = 2x + 1 + 3/(x − 1)² et F(x) = x² + x − 3/(x − 1) sur ]1 ; +∞[.

Toute réécriture se contrôle en dérivant le résultat.
:::

::: verifie À toi : un autre produit
Déterminer une primitive de f(x) = sin 6x cos 2x.

---

Avec a = 6x et b = 2x : sin 8x + sin 4x = 2 sin 6x cos 2x, donc f(x) = (1/2)(sin 8x + sin 4x). Chaque terme est dans le tableau : F(x) = (1/2)(−cos 8x/8 − cos 4x/4) = −cos 8x/16 − cos 4x/8. Contrôle : F′(x) = (1/2)(sin 8x + sin 4x) = f(x).
:::

::: retenir
Quand aucune forme n'apparaît, on développe, on découpe ou on linéarise pour retomber sur des termes du tableau, puis on contrôle en dérivant.
:::

> 🏆 Les huit portes sont franchies : tu sais vérifier une primitive, décrire toutes les primitives, fixer la constante, utiliser le tableau, la linéarité, les formes composées et les réécritures. Prochaine étape : donner un nom à la primitive de 1/x.
