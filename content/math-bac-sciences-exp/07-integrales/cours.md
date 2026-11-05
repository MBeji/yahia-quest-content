# ⚔️ Intégrales — l'aire qui révèle la primitive

> 💡 «Une aire, c'est une soustraction de primitives qui s'ignore.»

Au Xe siècle, Thabit Ibn Qurra cherchait l'aire sous une parabole, c'est-à-dire ce que nous écrivons ∫₀ᵃ √(px)dx ; il lui fallait un artifice astucieux pour chaque courbe. Toi, tu disposes de l'arme forgée au chapitre précédent : les **primitives**. Huit notions te mènent de l'aire sous une courbe jusqu'aux fonctions définies par une intégrale : la définition et le calcul, les propriétés algébriques, les aires, les inégalités, l'intégration par parties, la valeur moyenne, les volumes de révolution. On suppose acquis les primitives (chapitre 6) et la dérivation d'une composée (chapitre 3).

## 🏰 L'aire sous une courbe : naissance de l'intégrale

Dans un repère orthogonal, trace la droite d'équation y = x + 2 entre x = −2 et x = 0. La partie P limitée par la droite, l'axe des abscisses et les droites x = −2 et x = 0 est un triangle rectangle de base 2 et de hauteur 2, donc d'aire 2 × 2 / 2 = 2. Les unités du repère sont libres : il faut d'abord dire dans quelle unité on compte.
Et si la courbe n'était pas une droite, comment trouver l'aire d'une telle partie ?

::: figure La droite C_f et la partie P : un triangle d'aire 2 u.a, limité par l'axe des abscisses et les droites x = −2 et x = 0
<svg viewBox="0 0 340 230"><title>Droite y = x + 2 et triangle limité par l'axe des abscisses, x = −2 et x = 0</title><line x1="24" y1="170.8" x2="328" y2="170.8" stroke="#0f172a" stroke-width="1.6"/><line x1="237.1" y1="206" x2="237.1" y2="7" stroke="#0f172a" stroke-width="1.6"/><polygon points="328,170.8 320,166.8 320,174.8" fill="#0f172a"/><polygon points="237.1,7 233.1,15 241.1,15" fill="#0f172a"/><polygon points="99,170.8 168.1,122.1 237.1,73.4 237.1,170.8 168.1,170.8 99,170.8" fill="#0f6e56" fill-opacity="0.22"/><polyline points="57.6,200 175,117.2 292.4,34.5" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="99" y1="170.8" x2="99" y2="170.8" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><text x="99" y="192.7" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><text x="247.5" y="192.7" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="219.9" y="73.4" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="288.9" y="24.7" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text><text x="181.9" y="146.4" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">P</text></svg>
:::

Sur la figure, la droite C_f passe par (−2 ; 0) et (0 ; 2) : la partie P est le triangle coloré entre elle et l'axe, de base 2 et de hauteur 2.

::: definition
**Unité d'aire** (u.a) — Le plan est muni d'un repère orthogonal (O, i⃗, j⃗). L'unité d'aire est l'aire du rectangle de dimensions ‖i⃗‖ et ‖j⃗‖.
:::

Une primitive de f(x) = x + 2 est F(x) = x²/2 + 2x + 1. On calcule F(0) − F(−2) = 1 − (−1) = 2 : le nombre trouvé par la géométrie. Une autre primitive donnerait-elle la même chose ? Oui, car deux primitives d'une même fonction sur un intervalle diffèrent d'une constante.

::: propriete
**Propriété** — Soit f continue sur un intervalle I. Si F et G sont deux primitives de f sur I, alors pour tous réels a et b de I : F(b) − F(a) = G(b) − G(a).
Raison : F − G est constante sur I, donc F(b) − G(b) = F(a) − G(a), et il suffit de réarranger.
:::

::: definition
**Intégrale d'une fonction continue et positive** — Soit f continue et positive sur [a, b] et F une primitive de f sur [a, b]. L'aire, en u.a, de la partie du plan limitée par la courbe de f, l'axe des abscisses et les droites x = a et x = b est le réel F(b) − F(a). Ce réel s'appelle l'**intégrale de f de a à b** et se note ∫ₐᵇ f(x)dx.
:::

::: exemple Du triangle à une courbe : calculer une aire par une primitive

1. Avec f(x) = x + 2 sur [−2, 0] (continue et positive) et F(x) = x²/2 + 2x + 1 : ∫₋₂⁰ (x + 2)dx = F(0) − F(−2) = 1 − (−1) = 2 u.a, comme le triangle.
2. Avec une autre primitive, G(x) = x²/2 + 2x : G(0) − G(−2) = 0 − (−2) = 2 u.a. Le choix de la primitive ne change pas le résultat (propriété ci-dessus).
3. Courbe non droite : f(t) = 1/t² sur [−2, −1], continue et positive. Une primitive est F(t) = −1/t (on contrôle : F′(t) = 1/t²). D'où l'aire ∫₋₂⁻¹ dt/t² = F(−1) − F(−2) = 1 − 1/2 = 1/2 u.a.
4. Contrôle de plausibilité : sur [−2, −1], f varie de 1/4 à 1 et l'intervalle a pour longueur 1, donc l'aire est entre 1/4 et 1 : 1/2 convient.
5. Conversion : si ‖i⃗‖ = 2 cm et ‖j⃗‖ = 1 cm, alors 1 u.a = 2 cm², et l'aire 1/2 u.a vaut 1 cm².

:::

::: piege
**Erreur : prendre F(b) seul pour l'aire.** Avec F(x) = x²/2 + 2x + 1, on lit F(0) = 1 ; avec G(x) = x²/2 + 2x, on lit G(0) = 0. Deux primitives, deux « aires » : F(b) seul dépend du choix de la primitive, donc ne mesure rien. L'erreur tente parce que F(b) est « la valeur au bout ». Seule la différence F(b) − F(a) ne dépend pas de la primitive ; elle vaut 2 dans les deux cas.
:::

::: verifie À toi : l'aire sous une droite
Calculer l'aire, en u.a, de la partie limitée par la courbe de f(x) = 4 − x, l'axe des abscisses et les droites x = 0 et x = 3.

---

f est continue et positive sur [0, 3] (4 − x ≥ 1). Une primitive est F(x) = 4x − x²/2, donc l'aire vaut F(3) − F(0) = (12 − 9/2) − 0 = 15/2 u.a. Contrôle : c'est un trapèze de bases f(0) = 4 et f(3) = 1 et de hauteur 3, d'aire (4 + 1)/2 × 3 = 15/2 ✓.
:::

::: retenir
Pour f continue et positive sur [a, b], l'aire sous la courbe vaut F(b) − F(a), notée ∫ₐᵇ f(x)dx, quelle que soit la primitive F choisie, et se compte en u.a.
:::

## 🧮 L'intégrale d'une fonction continue : calcul, Chasles et linéarité

Prends f(x) = x² − 1 sur [1/2, 1] : la courbe passe sous l'axe, donc f n'est plus positive et le mot « aire » ne convient plus. Le calcul F(b) − F(a), lui, reste faisable.
Garde-t-il un sens, et que devient-il quand on coupe l'intervalle ou qu'on additionne deux fonctions ?

::: definition
**Intégrale d'une fonction continue** — Soit f continue sur un intervalle I, a et b dans I, F une primitive de f sur I. L'intégrale de f entre a et b est le réel ∫ₐᵇ f(x)dx = F(b) − F(a), noté aussi [F(x)]ₐᵇ (« F(x) pris entre a et b »). La lettre x est une **variable muette** : ∫ₐᵇ f(x)dx = ∫ₐᵇ f(t)dt. On parle d'intégrale de f sur [a, b] lorsque a ≤ b, ou encore de a à b, ou entre a et b.
:::

::: exemple Calculer une intégrale par une primitive

1. f(x) = x² − 1 sur [1/2, 1]. Une primitive est F(x) = x³/3 − x (F′(x) = x² − 1 ✓).
2. F(1) = 1/3 − 1 = −2/3 et F(1/2) = 1/24 − 1/2 = −11/24.
3. ∫ f = F(1) − F(1/2) = −2/3 + 11/24 = −16/24 + 11/24 = −5/24. Le résultat est négatif : f est négative sur [1/2, 1], et l'intégrale n'est pas une aire.
4. Autre forme : f(x) = sin 2x / cos³2x sur [0, π/6]. On pose u(x) = cos 2x, donc u′(x) = −2 sin 2x et f = −(1/2) u′ u⁻³. Comme u′u⁻³ a pour primitive u⁻²/(−2), une primitive de f est F(x) = 1/(4 cos²2x) (contrôle par dérivation ✓).
5. F(π/6) = 1/(4 × 1/4) = 1 car cos(π/3) = 1/2 ; F(0) = 1/4. D'où ∫₀^{π/6} f = 1 − 1/4 = 3/4.

:::

::: piege
**Erreur : inverser les bornes sans changer le signe.** Avec f(x) = x² − 1, on a vu ∫_{1/2}¹ f = −5/24. Si l'on écrit ∫₁^{1/2} f = −5/24 aussi, on se trompe : F(1/2) − F(1) = −11/24 + 2/3 = +5/24. L'erreur tente parce que « les mêmes deux nombres » semblent donner « le même résultat ». Échanger les bornes change le signe, et la lettre muette ne doit jamais se confondre avec une borne : on écrit ∫₀ˣ f(t)dt, jamais ∫₀ˣ f(x)dx.
:::

::: propriete
**Propriétés algébriques** — Soit f continue sur I et a, b, c dans I. ∫ₐᵃ f(x)dx = 0 ; ∫ₐᵇ f(x)dx = −∫_bᵃ f(x)dx ; **relation de Chasles** : ∫ₐᶜ f(x)dx + ∫_cᵇ f(x)dx = ∫ₐᵇ f(x)dx.
**Linéarité** — Si f et g sont continues sur [a, b] et α, β réels : ∫ₐᵇ (αf + βg)(x)dx = α∫ₐᵇ f(x)dx + β∫ₐᵇ g(x)dx.
Elles viennent d'une primitive F : (F(c) − F(a)) + (F(b) − F(c)) = F(b) − F(a), et αF + βG est une primitive de αf + βg. Cas limite : c n'a pas besoin d'être entre a et b.
:::

::: exemple Chasles et linéarité

1. f continue avec ∫₋₁² f = 3 et ∫₄² f = −5. On retourne la seconde (bornes échangées) : ∫₂⁴ f = 5. Chasles donne ∫₋₁⁴ f = ∫₋₁² f + ∫₂⁴ f = 3 + 5 = 8.
2. On veut ∫₁² x²/(x + 1)² dx + ∫₁² (2x + 1)/(x + 1)² dx. Aucune n'est calculable à vue, mais par linéarité la somme est ∫₁² (x² + 2x + 1)/(x + 1)² dx = ∫₁² 1 dx = [x]₁² = 1.

:::

::: verifie À toi : une forme u′/u²
Calculer ∫₀^{π/6} sin x / cos²x dx.

---

On pose u(x) = cos x, donc u′(x) = −sin x et sin x / cos²x = −u′/u². Une primitive de u′/u² est −1/u, donc une primitive de f est F(x) = 1/cos x (contrôle : F′(x) = sin x / cos²x ✓). D'où F(π/6) − F(0) = 2/√3 − 1 = (2√3 − 3)/3 ≈ 0,15.
:::

::: retenir
∫ₐᵇ f(x)dx = [F(x)]ₐᵇ = F(b) − F(a), de signe quelconque ; échanger les bornes change le signe, Chasles coupe un intervalle, la linéarité s'applique à une somme et à un facteur constant.
:::

## 📐 Aires : signe quelconque et entre deux courbes

Sur [−2, 3], la courbe de x ↦ x³ passe sous l'axe pour x < 0 puis au-dessus pour x > 0. L'intégrale compte la partie du dessous en négatif ; l'aire, elle, est toujours positive.
Comment passer de l'intégrale à l'aire d'une partie du plan, et que devient la règle entre deux courbes ?

::: definition
**Aire, fonction de signe quelconque** — Soit f continue sur [a, b]. L'aire, en u.a, de la partie du plan limitée par l'axe des abscisses, la courbe de f et les droites x = a et x = b est le réel ∫ₐᵇ |f(x)|dx.
:::

::: exemple Découper là où le signe change

1. f(x) = x³ sur [−2, 3] est négative sur [−2, 0] et positive sur [0, 3] : on coupe en 0 (Chasles).
2. Sur [−2, 0], |x³| = −x³, de primitive −x⁴/4 : [−x⁴/4]₋₂⁰ = 0 − (−4) = 4. Sur [0, 3], [x⁴/4]₀³ = 81/4.
3. L'aire vaut 4 + 81/4 = 97/4 = 24,25 u.a.
4. En comparaison, ∫₋₂³ x³ dx = [x⁴/4]₋₂³ = 81/4 − 4 = 65/4 = 16,25 : ce bilan algébrique n'est pas l'aire.

:::

Pour deux courbes C_f et C_g, on remplace f par f − g : la distance verticale entre les courbes.

::: definition
**Aire entre deux courbes** — Soit f et g continues sur [a, b]. L'aire, en u.a, de la partie du plan limitée par C_f, C_g et les droites x = a et x = b est le réel ∫ₐᵇ |f(x) − g(x)|dx.
:::

::: figure Les courbes de f(x) = x et de g(x) = x³ se croisent en x = 0 : deux parties A₁ et A₂ de part et d'autre, à calculer séparément
<svg viewBox="0 0 340 240"><title>Courbes de f(x) = x et g(x) = x³ sur [−1/2 ; 1], deux parties colorées de part et d'autre de x = 0</title><line x1="24" y1="132.9" x2="328" y2="132.9" stroke="#0f172a" stroke-width="1.6"/><line x1="148.6" y1="216" x2="148.6" y2="7" stroke="#0f172a" stroke-width="1.6"/><polygon points="328,132.9 320,128.9 320,136.9" fill="#0f172a"/><polygon points="148.6,7 144.6,15 152.6,15" fill="#0f172a"/><polygon points="82.7,144.2 86,142.6 89.3,141.2 92.6,139.9 95.9,138.7 99.2,137.7 102.5,136.8 105.8,136 109.1,135.4 112.4,134.8 115.7,134.3 119,133.9 122.3,133.6 125.6,133.4 128.9,133.2 132.2,133.1 135.5,133 138.8,132.9 142,132.9 145.3,132.9 148.6,132.9 148.6,132.9 145.3,135.2 142,137.4 138.8,139.7 135.5,142 132.2,144.2 128.9,146.5 125.6,148.8 122.3,151 119,153.3 115.7,155.6 112.4,157.8 109.1,160.1 105.8,162.4 102.5,164.7 99.2,166.9 95.9,169.2 92.6,171.5 89.3,173.7 86,176 82.7,178.3" fill="#b45309" fill-opacity="0.22"/><polygon points="148.6,132.9 151.9,130.6 155.2,128.4 158.5,126.1 161.8,123.8 165.1,121.6 168.4,119.3 171.7,117 175,114.8 178.3,112.5 181.6,110.2 184.9,108 188.2,105.7 191.5,103.4 194.8,101.2 198.1,98.9 201.4,96.6 204.7,94.4 208,92.1 211.2,89.8 214.5,87.6 217.8,85.3 221.1,83 224.4,80.8 227.7,78.5 231,76.2 234.3,74 237.6,71.7 240.9,69.4 244.2,67.2 247.5,64.9 250.8,62.6 254.1,60.3 257.4,58.1 260.7,55.8 264,53.5 267.3,51.3 270.6,49 273.9,46.7 277.2,44.5 280.5,42.2 280.5,42.2 277.2,48.8 273.9,55.1 270.6,61.1 267.3,66.8 264,72.1 260.7,77.2 257.4,82 254.1,86.5 250.8,90.7 247.5,94.6 244.2,98.3 240.9,101.8 237.6,105 234.3,108 231,110.8 227.7,113.3 224.4,115.7 221.1,117.8 217.8,119.8 214.5,121.6 211.2,123.2 208,124.6 204.7,125.9 201.4,127.1 198.1,128.1 194.8,129 191.5,129.8 188.2,130.5 184.9,131 181.6,131.5 178.3,131.9 175,132.2 171.7,132.4 168.4,132.6 165.1,132.7 161.8,132.8 158.5,132.9 155.2,132.9 151.9,132.9 148.6,132.9" fill="#0f6e56" fill-opacity="0.22"/><polyline points="43.2,205.5 169.7,118.4 296.3,31.3" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><polyline points="30,199 34.3,192.1 38.6,185.6 42.9,179.7 47.2,174.2 51.5,169.2 55.8,164.6 60.1,160.3 64.4,156.5 68.8,153.1 73.1,150 77.4,147.2 81.7,144.8 86,142.6 90.3,140.8 94.6,139.2 98.9,137.8 103.2,136.6 107.5,135.7 111.8,134.9 116.1,134.3 120.4,133.8 124.7,133.4 129,133.2 133.3,133 137.7,133 142,132.9 146.3,132.9 150.6,132.9 154.9,132.9 159.2,132.9 163.5,132.8 167.8,132.6 172.1,132.4 176.4,132.1 180.7,131.6 185,131 189.3,130.2 193.6,129.3 197.9,128.2 202.2,126.8 206.5,125.2 210.9,123.4 215.2,121.2 219.5,118.8 223.8,116.1 228.1,113.1 232.4,109.6 236.7,105.9 241,101.7 245.3,97.1 249.6,92.1 253.9,86.7 258.2,80.8 262.5,74.4 266.8,67.5 271.1,60.1 275.4,52.2 279.8,43.7 284.1,34.6 288.4,24.9" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="82.7" y1="178.3" x2="82.7" y2="144.2" stroke="#0f172a" stroke-width="1.2" stroke-dasharray=""/><line x1="280.5" y1="132.9" x2="280.5" y2="42.2" stroke="#0f172a" stroke-width="1.2" stroke-dasharray=""/><text x="82.7" y="198.2" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1/2</text><text x="280.5" y="151" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="161.8" y="151" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="188.2" y="80.3" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text><text x="260.7" y="94.8" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_g</text><text x="113" y="143.8" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A₁</text><text x="221.1" y="114.8" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A₂</text></svg>
:::

Sur la figure, f(x) = x (noir) et g(x) = x³ (vert) se coupent en x = 0 : c'est là que f − g change de signe, et c'est là qu'on coupe l'intervalle [−1/2, 1] en deux parties A₁ et A₂.

::: exemple Aire entre y = x et y = x³ sur [−1/2, 1]

1. f(x) − g(x) = x − x³ = x(1 − x)(1 + x). Sur [−1/2, 1], les facteurs 1 − x et 1 + x sont positifs : le signe est celui de x.
2. Sur [−1/2, 0], f − g ≤ 0 : A₁ = ∫\_{−1/2}⁰ (x³ − x)dx = [x⁴/4 − x²/2]\_{−1/2}⁰ = 0 − (1/64 − 1/8) = 7/64.
3. Sur [0, 1], f − g ≥ 0 : A₂ = ∫₀¹ (x − x³)dx = [x²/2 − x⁴/4]₀¹ = 1/4.
4. L'aire totale vaut 7/64 + 1/4 = 23/64 u.a.

:::

::: piege
**Erreur : intégrer f − g sans étudier son signe.** Sur [−1/2, 1], ∫ (x − x³)dx = [x²/2 − x⁴/4]_{−1/2}¹ = 1/4 − (1/8 − 1/64) = 9/64, et non 23/64 : sur [−1/2, 0], les deux courbes sont dans l'ordre inverse et leur écart se retranche au lieu de s'ajouter. L'erreur tente parce que la formule « courbe du haut moins courbe du bas » est vraie sur chaque morceau, jamais d'un seul bloc quand les courbes se croisent. Étudie le signe de f − g, puis coupe à chaque croisement.
:::

::: verifie À toi : intégrale nulle, aire non nulle
Calculer ∫₀³ (x² − 2x)dx, puis l'aire de la partie limitée par la courbe de x ↦ x² − 2x, l'axe des abscisses et les droites x = 0 et x = 3.

---

∫₀³ (x² − 2x)dx = [x³/3 − x²]₀³ = 9 − 9 = 0. Mais x² − 2x = x(x − 2) est négative sur [0, 2] et positive sur [2, 3] : sur [0, 2], ∫ (2x − x²)dx = [x² − x³/3]₀² = 4/3 ; sur [2, 3], ∫ (x² − 2x)dx = 0 − (−4/3) = 4/3. L'aire vaut 4/3 + 4/3 = 8/3 u.a : l'intégrale nulle vient d'une compensation, pas d'une aire nulle.
:::

::: retenir
L'aire entre l'axe et C_f est ∫|f| et l'aire entre C_f et C_g est ∫|f − g| : on étudie le signe, on coupe à chaque changement, et on intègre morceau par morceau.
:::

## 🛡️ Intégrales et inégalités : encadrer sans calculer

Pose uₙ = ∫₀¹ xⁿ⁺¹/(1 + x²) dx. Aucune primitive de xⁿ⁺¹/(1 + x²) ne figure dans ta table pour n quelconque. Pourtant, pour n = 100, on te demande où se trouve u₁₀₀.
Peut-on situer une intégrale en encadrant seulement ce qu'il y a sous le signe ∫ ?

::: propriete
**Propriétés** — Soit f, g, h continues sur [a, b], avec a < b.
Positivité : si f ≥ 0 sur [a, b], alors ∫ₐᵇ f(x)dx ≥ 0 ; et si f ≥ 0 ne s'annule qu'en un nombre fini de points, alors ∫ₐᵇ f(x)dx > 0.
Comparaison : si h ≤ f ≤ g sur [a, b], alors ∫ₐᵇ h(x)dx ≤ ∫ₐᵇ f(x)dx ≤ ∫ₐᵇ g(x)dx.
Valeur absolue : |∫ₐᵇ f(x)dx| ≤ ∫ₐᵇ |f(x)|dx.
Raison : une primitive d'une fonction positive est croissante ; on l'applique à f − h, g − f, puis à −|f| ≤ f ≤ |f|.
:::

::: exemple Situer u₁₀₀ sans la calculer

1. Pour x dans [0, 1], 1 + x² ≥ 1, donc 1/(1 + x²) ≤ 1 ; comme xⁿ⁺¹ ≥ 0, on a 0 ≤ xⁿ⁺¹/(1 + x²) ≤ xⁿ⁺¹.
2. La comparaison donne 0 ≤ uₙ ≤ ∫₀¹ xⁿ⁺¹ dx = [xⁿ⁺²/(n + 2)]₀¹ = 1/(n + 2).
3. Pour n = 100 : 0 ≤ u₁₀₀ ≤ 1/102 ≈ 0,0098. Le nombre 0 approche u₁₀₀ à moins de 10⁻² près.
4. Comme 1/(n + 2) tend vers 0, le théorème de l'encadrement donne : uₙ tend vers 0.

:::

::: piege
**Erreur : lire la positivité à l'envers.** Si ∫ₐᵇ f(x)dx ≥ 0, on ne peut pas conclure que f ≥ 0. Contre-exemple : f(x) = x − 1 sur [0, 3] donne ∫₀³ (x − 1)dx = [x²/2 − x]₀³ = 3/2 ≥ 0, alors que f(0) = −1. L'erreur tente parce que le théorème a l'air d'une équivalence. Il n'est valable que dans un sens : f ≥ 0 entraîne ∫ f ≥ 0.
:::

Quand on connaît la monotonie de f, on peut encadrer l'aire par des rectangles : c'est la méthode des rectangles, utile quand aucune primitive n'est disponible. Pour f décroissante sur [1, 2], coupons en deux intervalles de longueur 0,5 : sur chacun, le rectangle de hauteur la plus petite valeur reste sous la courbe, celui de la plus grande valeur la dépasse.

::: figure Deux rectangles verts sous la courbe de 1/x et deux rectangles orange qui la dépassent encadrent l'aire entre x = 1 et x = 2
<svg viewBox="0 0 340 240"><title>Courbe de 1/x sur [1 ; 2] avec deux rectangles verts sous la courbe et deux rectangles orange au-dessus</title><line x1="24" y1="192.9" x2="328" y2="192.9" stroke="#0f172a" stroke-width="1.6"/><line x1="30" y1="216" x2="30" y2="7" stroke="#0f172a" stroke-width="1.6"/><polygon points="328,192.9 320,188.9 320,196.9" fill="#0f172a"/><polygon points="30,7 26,15 34,15" fill="#0f172a"/><polygon points="102.5,192.9 175,192.9 175,50.6 102.5,50.6" fill="none" fill-opacity="0.28" stroke="#b45309" stroke-width="1.6"/><polygon points="175,192.9 247.5,192.9 247.5,98 175,98" fill="none" fill-opacity="0.28" stroke="#b45309" stroke-width="1.6"/><polygon points="102.5,192.9 175,192.9 175,98 102.5,98" fill="#0f6e56" fill-opacity="0.28" stroke="#0f6e56" stroke-width="1.6"/><polygon points="175,192.9 247.5,192.9 247.5,121.8 175,121.8" fill="#0f6e56" fill-opacity="0.28" stroke="#0f6e56" stroke-width="1.6"/><polyline points="80.8,25.5 84.5,30.4 88.2,35.1 92,39.5 95.7,43.6 99.5,47.6 103.2,51.3 107,54.8 110.7,58.2 114.5,61.4 118.2,64.5 122,67.4 125.7,70.2 129.4,72.9 133.2,75.4 136.9,77.9 140.7,80.3 144.4,82.5 148.2,84.7 151.9,86.8 155.7,88.8 159.4,90.7 163.2,92.6 166.9,94.4 170.6,96.1 174.4,97.8 178.1,99.4 181.9,100.9 185.6,102.5 189.4,103.9 193.1,105.3 196.9,106.7 200.6,108 204.4,109.3 208.1,110.6 211.9,111.8 215.6,113 219.3,114.1 223.1,115.2 226.8,116.3 230.6,117.3 234.3,118.4 238.1,119.4 241.8,120.3 245.6,121.3 249.3,122.2 253.1,123.1 256.8,124 260.5,124.8 264.3,125.6 268,126.5 271.8,127.3 275.5,128 279.3,128.8 283,129.5 286.8,130.2 290.5,130.9 294.3,131.6 298,132.3 301.8,133 305.5,133.6" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><text x="138.8" y="64.8" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R₁</text><text x="211.2" y="81.9" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R₂</text><text x="138.8" y="150.2" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r₁</text><text x="211.2" y="161.6" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r₂</text><text x="102.5" y="207.2" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="175" y="207.2" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,5</text><text x="247.5" y="207.2" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="291" y="104.7" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text></svg>
:::

Sur la figure, les rectangles verts r₁ et r₂ sont sous la courbe et les rectangles orange R₁ et R₂ la dépassent : l'aire cherchée est coincée entre les deux sommes.

::: exemple Encadrer A = ∫₁² dx/x par deux rectangles

1. f(x) = 1/x est décroissante sur [1, 2] : sur [1 ; 1,5], elle va de f(1) = 1 à f(1,5) = 2/3 ; sur [1,5 ; 2], de 2/3 à f(2) = 1/2.
2. Sommes par défaut : r₁ + r₂ = 0,5 × 2/3 + 0,5 × 1/2 = 1/3 + 1/4 = 7/12.
3. Sommes par excès : R₁ + R₂ = 0,5 × 1 + 0,5 × 2/3 = 1/2 + 1/3 = 5/6.
4. Donc 7/12 ≤ A ≤ 5/6, soit 0,583 ≤ A ≤ 0,833. Avec 5 intervalles de longueur 0,2, l'encadrement se resserre.

:::

::: verifie À toi : encadrer une intégrale
Pour n ≥ 1, wₙ = ∫₀¹ xⁿ/(1 + x) dx. Montrer que 0 ≤ wₙ ≤ 1/(n + 1), puis donner la limite de wₙ.

---

Pour x dans [0, 1], 1 + x ≥ 1, donc 0 ≤ xⁿ/(1 + x) ≤ xⁿ. La comparaison donne 0 ≤ wₙ ≤ ∫₀¹ xⁿ dx = 1/(n + 1). Comme 1/(n + 1) tend vers 0, le théorème de l'encadrement donne lim wₙ = 0.
:::

::: retenir
Si h ≤ f ≤ g sur [a, b] (a < b), alors ∫h ≤ ∫f ≤ ∫g : on encadre l'intégrande, puis on intègre l'encadrement ; |∫f| ≤ ∫|f| ; la réciproque de la positivité est fausse.
:::

## 🔮 L'intégration par parties : quand l'intégrande est un produit

Calcule ∫₀^{π/2} t sin t dt. Aucune formule de ta table ne primitive un produit comme t sin t, et la linéarité ne sait que sommer.
Que dire d'une intégrale dont l'intégrande est le produit de deux fonctions ?

::: propriete
**Intégration par parties** — Soit f et g dérivables sur [a, b], de dérivées f′ et g′ continues. Alors ∫ₐᵇ f(t)g′(t)dt = [f(t)g(t)]ₐᵇ − ∫ₐᵇ f′(t)g(t)dt.
Raison : (fg)′ = f′g + fg′ ; on intègre de a à b chaque terme et la linéarité sépare les deux.
Choix : f est le facteur qui se simplifie en dérivant (t, t²), g′ celui dont on connaît une primitive (sin, cos).
:::

::: exemple Un produit t × sin t, puis t² × cos t

1. On veut I = ∫₀^{π/2} t sin t dt. On pose f(t) = t (f′ = 1) et g′(t) = sin t (g(t) = −cos t).
2. La formule donne I = [−t cos t]₀^{π/2} + ∫₀^{π/2} cos t dt. Le crochet vaut −(π/2) × 0 − 0 = 0.
3. Reste ∫₀^{π/2} cos t dt = [sin t]₀^{π/2} = 1, donc I = 1.
4. On veut K = ∫₀^{π/2} t² cos t dt. On pose f(t) = t² (f′ = 2t) et g′(t) = cos t (g(t) = sin t) : K = [t² sin t]₀^{π/2} − 2∫₀^{π/2} t sin t dt.
5. Le crochet vaut π²/4, et l'intégrale restante est I = 1 : K = π²/4 − 2.

:::

::: piege
**Erreur : permuter les rôles.** Pour I, on pose f(t) = sin t et g′(t) = t, donc g(t) = t²/2 : la formule donne [(t²/2) sin t] − ∫ (t²/2) cos t dt, et l'intégrale restante est plus compliquée que celle du départ. L'erreur tente parce que les deux facteurs sont primitivables. On choisit pour f celui que la dérivation simplifie, ici t, dont la dérivée est 1.
:::

::: verifie À toi : une intégration par parties
Calculer ∫₀^π t cos t dt.

---

On pose f(t) = t (f′ = 1) et g′(t) = cos t (g(t) = sin t) : le facteur t se simplifie en dérivant. La formule donne ∫₀^π t cos t dt = [t sin t]₀^π − ∫₀^π sin t dt = (0 − 0) − [−cos t]₀^π = −2.
:::

::: retenir
∫ₐᵇ fg′ = [fg]ₐᵇ − ∫ₐᵇ f′g : on dérive le facteur qui se simplifie et on primitive l'autre ; deux passages s'enchaînent pour t², et le crochet se calcule aux bornes.
:::

## 🎯 Valeur moyenne et inégalité de la moyenne

Une voiture parcourt une route avec une vitesse variable. À quelle vitesse constante devrait-elle rouler pour couvrir la même distance dans le même temps ? Cette vitesse « lissée » est la moyenne de la vitesse sur l'intervalle de temps.
Comment définir la moyenne d'une fonction continue sur [a, b], et que dire de sa position ?

::: definition
**Valeur moyenne** — Soit f continue sur [a, b], a < b. La valeur moyenne de f sur [a, b] est le réel f̄ = 1/(b − a) × ∫ₐᵇ f(x)dx.
:::

::: figure Le rectangle orange de hauteur 2/π a la même aire que la partie sous la courbe du cosinus entre 0 et π/2
<svg viewBox="0 0 340 230"><title>Courbe du cosinus sur [0 ; π/2] et rectangle de hauteur 2/π de même aire</title><line x1="24" y1="174.5" x2="328" y2="174.5" stroke="#0f172a" stroke-width="1.6"/><line x1="69.5" y1="206" x2="69.5" y2="7" stroke="#0f172a" stroke-width="1.6"/><polygon points="328,174.5 320,170.5 320,178.5" fill="#0f172a"/><polygon points="69.5,7 65.5,15 73.5,15" fill="#0f172a"/><polygon points="69.5,46.9 74.7,47 79.9,47.3 85.1,47.8 90.3,48.5 95.4,49.3 100.6,50.4 105.8,51.7 111,53.1 116.1,54.8 121.3,56.6 126.5,58.6 131.7,60.8 136.8,63.2 142,65.7 147.2,68.4 152.4,71.3 157.5,74.3 162.7,77.5 167.9,80.8 173.1,84.3 178.3,87.9 183.4,91.6 188.6,95.5 193.8,99.5 199,103.6 204.1,107.8 209.3,112.1 214.5,116.6 219.7,121.1 224.8,125.7 230,130.3 235.2,135.1 240.4,139.9 245.5,144.7 250.7,149.6 255.9,154.5 261.1,159.5 266.3,164.5 271.4,169.5 276.6,174.5 276.6,174.5 271.4,174.5 266.3,174.5 261.1,174.5 255.9,174.5 250.7,174.5 245.5,174.5 240.4,174.5 235.2,174.5 230,174.5 224.8,174.5 219.7,174.5 214.5,174.5 209.3,174.5 204.1,174.5 199,174.5 193.8,174.5 188.6,174.5 183.4,174.5 178.3,174.5 173.1,174.5 167.9,174.5 162.7,174.5 157.5,174.5 152.4,174.5 147.2,174.5 142,174.5 136.8,174.5 131.7,174.5 126.5,174.5 121.3,174.5 116.1,174.5 111,174.5 105.8,174.5 100.6,174.5 95.4,174.5 90.3,174.5 85.1,174.5 79.9,174.5 74.7,174.5 69.5,174.5" fill="#0f6e56" fill-opacity="0.18"/><polygon points="69.5,174.5 276.6,174.5 276.6,93.3 69.5,93.3" fill="#b45309" fill-opacity="0.16" stroke="#b45309" stroke-width="1.8"/><polyline points="69.5,46.9 74.7,47 79.9,47.3 85.1,47.8 90.3,48.5 95.4,49.3 100.6,50.4 105.8,51.7 111,53.1 116.1,54.8 121.3,56.6 126.5,58.6 131.7,60.8 136.8,63.2 142,65.7 147.2,68.4 152.4,71.3 157.5,74.3 162.7,77.5 167.9,80.8 173.1,84.3 178.3,87.9 183.4,91.6 188.6,95.5 193.8,99.5 199,103.6 204.1,107.8 209.3,112.1 214.5,116.6 219.7,121.1 224.8,125.7 230,130.3 235.2,135.1 240.4,139.9 245.5,144.7 250.7,149.6 255.9,154.5 261.1,159.5 266.3,164.5 271.4,169.5 276.6,174.5" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><text x="69.5" y="192.3" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="276.6" y="192.3" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">π/2</text><text x="43.2" y="93.3" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2/π</text><text x="214.5" y="69.9" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text></svg>
:::

Sur la figure, la courbe de cos sur [0, π/2] a pour aire 1 u.a ; le rectangle orange, de largeur π/2 et de hauteur f̄ = 2/π, a la même aire. Ce que la courbe dépasse au-dessus du rectangle comble ce qui lui manque en dessous.

::: exemple Calculer une valeur moyenne

1. f(x) = 3x − 1 sur [0, 2] : ∫₀² (3x − 1)dx = [3x²/2 − x]₀² = 6 − 2 = 4.
2. On divise par la longueur b − a = 2 : f̄ = 4/2 = 2. Et f(1) = 2 : pour une fonction affine, la moyenne est atteinte au milieu.
3. f(x) = cos x sur [0, π/2] : ∫₀^{π/2} cos x dx = [sin x]₀^{π/2} = 1, donc f̄ = 1/(π/2) = 2/π ≈ 0,64.
4. Remarque : la moyenne arithmétique des extrémités vaut (1 + 0)/2 = 0,5, et n'est pas f̄.

:::

::: propriete
**Inégalité de la moyenne** — Soit f continue sur [a, b], a < b, et m, M deux réels. Si m ≤ f(x) ≤ M pour tout x de [a, b], alors m ≤ f̄ ≤ M. Il en résulte qu'il existe c dans [a, b] tel que f̄ = f(c).
Raison : on intègre m ≤ f ≤ M et l'on divise par b − a > 0 ; pour c, f([a, b]) = [min f ; max f] contient f̄ (valeurs intermédiaires).
Cas limite : si f est constante égale à k, on peut prendre m = M = k, et alors f̄ = k.
:::

::: exemple Encadrer deux intégrales

1. ∫₀¹ dx/(1 + x²) : sur [0, 1], 1 ≤ 1 + x² ≤ 2, donc 1/2 ≤ 1/(1 + x²) ≤ 1. La longueur est 1, donc 0,5 ≤ ∫₀¹ dx/(1 + x²) ≤ 1.
2. ∫₀^{1/2} dx/√(1 − x²) : sur [0, 1/2], 3/4 ≤ 1 − x² ≤ 1, donc 1 ≤ 1/√(1 − x²) ≤ 2/√3. La longueur est 1/2, donc 1/2 ≤ ∫ ≤ 1/√3 = √3/3.

:::

::: piege
**Erreur : oublier de diviser par b − a.** Pour f(x) = 3x − 1 sur [0, 2], on trouve ∫ = 4 et l'on annonce « f̄ = 4 », alors que f̄ = 4/2 = 2, qui est d'ailleurs f(1). L'erreur tente parce que l'intégrale est le calcul « long » et le résultat « fini ». Une moyenne se divise toujours par la longueur de l'intervalle.
:::

::: verifie À toi : moyenne et point moyen
Calculer la valeur moyenne de f(x) = x³ sur [0, 2], puis trouver c de [0, 2] tel que f(c) = f̄.

---

∫₀² x³ dx = [x⁴/4]₀² = 4, donc f̄ = 4/2 = 2. On résout c³ = 2 : c = ∛2 ≈ 1,26, qui appartient bien à [0, 2], comme le prévoit le corollaire.
:::

::: retenir
f̄ = 1/(b − a) × ∫ₐᵇ f ; m ≤ f ≤ M entraîne m ≤ f̄ ≤ M, donc m(b − a) ≤ ∫ₐᵇ f ≤ M(b − a) ; et f̄ est une valeur prise par f.
:::

## 🧊 Volumes de solides de révolution

Un cylindre de rayon 2 et de hauteur 3 a pour volume π × 2² × 3 = 12π : c'est la rotation autour de (Ox) du segment y = 2, pour x de 0 à 3. Si le rayon varie le long de l'axe, chaque tranche reste un disque, mais de rayon f(x).
Comment « additionner » ces disques pour obtenir le volume ?

::: definition
**Volume d'un solide de révolution** — L'espace est muni d'un repère orthonormé (O, i⃗, j⃗, k⃗). Soit f continue et positive sur [a, b]. Le volume du solide engendré par la rotation autour de (Ox) de l'arc AB d'équation y = f(x), a ≤ x ≤ b, est V = π∫ₐᵇ f²(x)dx.
:::

::: figure Le solide engendré par l'arc AB : chaque section perpendiculaire à (Ox) est un disque de rayon f(x)
<svg viewBox="0 0 340 210"><title>Solide engendré par la rotation de l'arc y = √x autour de l'axe (Ox) ; une section est un disque</title><path d="M30 105 L36.2 93 L42.4 88 L48.6 84.2 L54.8 81 L61 78.1 L67.2 75.6 L73.4 73.2 L79.6 71 L85.8 69 L92 67 L98.2 65.1 L104.4 63.4 L110.6 61.7 L116.8 60 L123 58.5 L129.2 56.9 L135.4 55.5 L141.6 54 L147.8 52.6 L154 51.3 L160.2 49.9 L166.4 48.6 L172.6 47.4 L178.8 46.1 L185 44.9 L191.2 43.7 L197.4 42.6 L203.6 41.4 L209.8 40.3 L216 39.2 L222.2 38.1 L228.4 37 L234.6 36 L240.8 34.9 L247 33.9 L253.2 32.9 L259.4 31.9 L265.6 30.9 L271.8 30 L278 29 L278 181 L271.8 180 L265.6 179.1 L259.4 178.1 L253.2 177.1 L247 176.1 L240.8 175.1 L234.6 174 L228.4 173 L222.2 171.9 L216 170.8 L209.8 169.7 L203.6 168.6 L197.4 167.4 L191.2 166.3 L185 165.1 L178.8 163.9 L172.6 162.6 L166.4 161.4 L160.2 160.1 L154 158.7 L147.8 157.4 L141.6 156 L135.4 154.5 L129.2 153.1 L123 151.5 L116.8 150 L110.6 148.3 L104.4 146.6 L98.2 144.9 L92 143 L85.8 141 L79.6 139 L73.4 136.8 L67.2 134.4 L61 131.9 L54.8 129 L48.6 125.8 L42.4 122 L36.2 117 L30 105 Z" fill="#0f6e56" fill-opacity="0.12"/><line x1="14" y1="105" x2="322" y2="105" stroke="#0f172a" stroke-width="1.6"/><polygon points="324,105 316,101 316,109" fill="#0f172a"/><polyline points="30,105 36.2,93 42.4,88 48.6,84.2 54.8,81 61,78.1 67.2,75.6 73.4,73.2 79.6,71 85.8,69 92,67 98.2,65.1 104.4,63.4 110.6,61.7 116.8,60 123,58.5 129.2,56.9 135.4,55.5 141.6,54 147.8,52.6 154,51.3 160.2,49.9 166.4,48.6 172.6,47.4 178.8,46.1 185,44.9 191.2,43.7 197.4,42.6 203.6,41.4 209.8,40.3 216,39.2 222.2,38.1 228.4,37 234.6,36 240.8,34.9 247,33.9 253.2,32.9 259.4,31.9 265.6,30.9 271.8,30 278,29" fill="none" stroke="#0f6e56" stroke-width="2.6"/><polyline points="30,105 36.2,117 42.4,122 48.6,125.8 54.8,129 61,131.9 67.2,134.4 73.4,136.8 79.6,139 85.8,141 92,143 98.2,144.9 104.4,146.6 110.6,148.3 116.8,150 123,151.5 129.2,153.1 135.4,154.5 141.6,156 147.8,157.4 154,158.7 160.2,160.1 166.4,161.4 172.6,162.6 178.8,163.9 185,165.1 191.2,166.3 197.4,167.4 203.6,168.6 209.8,169.7 216,170.8 222.2,171.9 228.4,173 234.6,174 240.8,175.1 247,176.1 253.2,177.1 259.4,178.1 265.6,179.1 271.8,180 278,181" fill="none" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="4 3"/><ellipse cx="185" cy="105" rx="9" ry="60.1" fill="#b45309" fill-opacity="0.2" stroke="#b45309" stroke-width="1.8"/><line x1="185" y1="105" x2="185" y2="44.9" stroke="#b45309" stroke-width="1.6"/><ellipse cx="278" cy="105" rx="9" ry="76" fill="none" stroke="#0f6e56" stroke-width="1.6"/><text x="191" y="75" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f(x)</text><text x="30" y="123" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">A</text><text x="296" y="75" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="185" y="123" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">x</text><text x="315" y="123" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a">(Ox)</text></svg>
:::

Sur la figure, la section par le plan d'abscisse x est un disque de rayon f(x) (en orange), donc d'aire π f²(x) : intégrer cette aire de a à b donne le volume.

::: exemple Un arc de racine, un arc d'hyperbole

1. L'arc y = √x, 0 ≤ x ≤ 4, tourne autour de (Ox). Ici f²(x) = x.
2. V = π∫₀⁴ x dx = π[x²/2]₀⁴ = 8π ≈ 25,1.
3. L'arc y = 1/x, 1 ≤ x ≤ 3. Ici f²(x) = 1/x².
4. V = π∫₁³ dx/x² = π[−1/x]₁³ = π(1 − 1/3) = 2π/3.

:::

::: piege
**Erreur : intégrer f au lieu de f².** Pour y = √x, on écrit V = π∫₀⁴ √x dx = π × 16/3 = 16π/3, alors que la bonne valeur est 8π. L'erreur tente parce que « intégrer la courbe » est le geste familier de ce chapitre. Le rayon du disque est f(x), son aire est πf²(x) : c'est le carré qu'on intègre.
:::

::: verifie À toi : un cône tronqué
L'arc y = x + 1, 0 ≤ x ≤ 2, tourne autour de (Ox). Calculer le volume engendré.

---

f(x) = x + 1 est continue et positive, f²(x) = (x + 1)². Une primitive est (x + 1)³/3, donc V = π[(x + 1)³/3]₀² = π(27 − 1)/3 = 26π/3. Contrôle : c'est un cône tronqué de rayons 1 et 3 et de hauteur 2, de volume π × 2 × (1 + 3 + 9)/3 = 26π/3 ✓.
:::

::: retenir
Le solide de révolution engendré par y = f(x) sur [a, b] autour de (Ox) a pour volume π∫ₐᵇ f²(x)dx : on intègre l'aire d'un disque, donc le carré de la hauteur.
:::

## 🌀 Fonctions définies par une intégrale, parité et périodicité

On fixe la borne du bas et on laisse varier celle du haut : G(x) = ∫₁ˣ (sin t)/t dt. Aucune formule connue ne donne une primitive de (sin t)/t, et pourtant G est bien une fonction de x.
Peut-on la dériver, et que gagne-t-on à l'étudier quand la fonction est paire, impaire ou périodique ?

::: propriete
**Fonction définie par une intégrale** — Soit f continue sur un intervalle I et a dans I. La fonction F : x ↦ ∫ₐˣ f(t)dt est la primitive de f sur I qui s'annule en a. Elle est donc dérivable sur I et F′(x) = f(x).
Raison : avec une primitive G de f, F(x) = G(x) − G(a), et F(a) = 0.
Conséquence : si u est dérivable et si les valeurs de u restent dans I, la fonction x ↦ F(u(x)) est une composée, de dérivée u′(x) × f(u(x)).
:::

::: exemple Dériver sans calculer la primitive

1. F(x) = ∫₀ˣ dt/(1 + t²) est définie et dérivable sur ℝ, avec F′(x) = 1/(1 + x²) > 0 : F est strictement croissante et F(0) = 0. De même G(x) = ∫₁ˣ (sin t)/t dt est dérivable sur ]0, +∞[ et G′(x) = (sin x)/x.
2. Soit H(y) = ∫₀ʸ dt/√(1 − t²) sur [0, 1[, avec H′(y) = 1/√(1 − y²). Posons g(x) = H(sin x) sur [0, π/2[ (sin x reste dans [0, 1[).
3. Par composée, g′(x) = cos x × H′(sin x) = cos x / √(1 − sin²x) = cos x / cos x = 1 car cos x > 0 sur [0, π/2[.
4. Avec g(0) = H(0) = 0, on obtient g(x) = x. En x = π/6, sin x = 1/2 : ∫₀^{1/2} dt/√(1 − t²) = g(π/6) = π/6.

:::

Pour une fonction continue sur un intervalle centré en 0 ou périodique, deux résultats évitent tout calcul.

::: propriete
**Parité** — Soit f continue sur un intervalle I centré en 0 et a dans I. Si f est impaire, ∫₋ₐᵃ f(x)dx = 0 ; si f est paire, ∫₋ₐᵃ f(x)dx = 2∫₀ᵃ f(x)dx.
**Périodicité** — Soit f continue sur ℝ et de période T. Pour tout réel a, ∫ₐᵃ⁺ᵀ f(t)dt = ∫₀ᵀ f(t)dt.
Raison : l'aire à gauche de 0 est l'image de l'aire à droite par symétrie ; la période T répète le même motif sur chaque intervalle de longueur T.
:::

::: exemple Parité et période

1. ∫₋₁¹ t⁵/(t⁶ + 1) dt : le numérateur est impair et le dénominateur pair, l'intégrande est impair, donc l'intégrale est nulle.
2. ∫₋₁¹ |t³ + t| dt : la fonction t ↦ |t³ + t| est paire, et t³ + t ≥ 0 sur [0, 1] : 2∫₀¹ (t³ + t)dt = 2(1/4 + 1/2) = 3/2.
3. ∫₀^{20π} |sin x| dx : |sin| a pour période π et ∫₀^π sin x dx = [−cos x]₀^π = 2 ; il y a 20 périodes dans [0, 20π] : 20 × 2 = 40.

:::

::: piege
**Erreur : garder la parité en passant à la valeur absolue.** La fonction t ↦ t³ + t est impaire, donc ∫₋₁¹ (t³ + t)dt = 0 ; mais |t³ + t| est paire, et ∫₋₁¹ |t³ + t| dt = 3/2, non 0. L'erreur tente parce que la valeur absolue semble « ne rien changer à la symétrie ». Elle change la parité : la valeur absolue d'une fonction impaire est paire.
:::

::: verifie À toi : une intégrale à borne variable
Soit K(x) = ∫₀^{x²} dt/(1 + t²) sur ℝ. Calculer K′(x), puis donner le sens de variation de K.

---

On pose F(y) = ∫₀ʸ dt/(1 + t²), dérivable sur ℝ avec F′(y) = 1/(1 + y²), et u(x) = x² : K = F∘u. Par composée, K′(x) = u′(x) × F′(u(x)) = 2x/(1 + x⁴). Ce signe est celui de x : K décroît sur ]−∞, 0], croît sur [0, +∞[, avec un minimum K(0) = 0.
:::

::: retenir
Pour f continue, x ↦ ∫ₐˣ f(t)dt est la primitive de f qui s'annule en a ; une intégrale sur [−a, a] vaut 0 pour une fonction impaire et 2∫₀ᵃ pour une fonction paire ; sur une période, l'intégrale ne dépend pas du départ.
:::

> 🏆 Septième porte franchie, héros : tu lis une aire comme une différence F(b) − F(a), tu la coupes par Chasles, tu l'encadres sans la calculer, tu la retournes par parties, tu en tires une moyenne, un volume, une fonction nouvelle. Les fonctions logarithme et exponentielle t'attendent — et même ∫₁² dx/x, l'aire que tu n'as pu qu'encadrer aujourd'hui, y trouvera enfin son nom.
