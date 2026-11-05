# ⚔️ Fonction exponentielle — la courbe qui est sa propre dérivée

> 💡 «Une seule courbe a, en chacun de ses points, une pente égale à sa hauteur. Celui qui la maîtrise tient la croissance, la décroissance et presque toute l'analyse du bac.»

En 1748, Euler se demandait combien d'habitants aurait une province de 100 000 âmes si sa population s'accroissait « tous les ans d'une trentième », et combien vaudrait une dette de 400 000 florins dont on paie 5 % d'intérêt par an. C'est en poussant ces calculs très loin qu'il a rencontré le nombre **e**. Toi, tu arrives par l'autre porte : au chapitre 8 tu as construit **ln**, continue et strictement croissante de ℝ*₊ sur ℝ, et le chapitre 4 t'a appris qu'une telle fonction possède une **réciproque**. Cette réciproque a un nom, c'est l'exponentielle. Huit notions te mènent de sa définition aux études de fonctions du bac. On suppose acquis le théorème des valeurs intermédiaires (chapitre 1), l'inégalité des accroissements finis (chapitre 3), les fonctions réciproques (chapitre 4), les primitives (chapitre 6) et l'intégration par parties (chapitre 7).

## 🏰 exp, la réciproque de ln

Sur la courbe de ln, cherche le réel dont le logarithme vaut 1/2 : la lecture donne environ 1,65, et la calculatrice confirme ln(1,6487) ≈ 0,5.
Comme ln est une bijection de ]0, +∞[ sur ℝ, **tout** réel y possède un unique antécédent par ln.
Comment nomme-t-on la fonction qui, à chaque réel y, rend cet antécédent ?

::: definition
**Fonction exponentielle** — « On appelle fonction exponentielle la fonction réciproque de la fonction logarithme népérien. L'image d'un réel x par la fonction exponentielle est noté [sic] e^x. »
:::

Le départ de exp est l'arrivée de ln, et réciproquement : exp est définie sur **ℝ** tout entier, à valeurs dans **ℝ*₊**. Autrement dit, **e^x existe pour tout réel x et il est toujours strictement positif.**

::: propriete
**Conséquences** — « • Pour tout réel x et pour tout réel strictement positif y, y = e^x ⟺ x = ln y. • Pour tout réel x, ln(e^x) = x. • Pour tout réel x > 0, e^(ln x) = x. • ln e = 1. »
Retiens surtout l'**équivalence** : elle convertit toute équation exponentielle en équation logarithmique, et réciproquement.
:::

::: figure Les courbes de exp (vert) et de ln (orange) se déduisent l'une de l'autre par le pliage le long de Δ : y = x. Le point (0 ; 1) de C_exp, qui traduit e^0 = 1, devient le point (1 ; 0) de C_ln, qui traduit ln 1 = 0.
<svg viewBox="0 0 340 300">
<title>Courbes de exp et de ln, symétriques par rapport à la droite d'équation y = x : le point (0 ; 1) de la première correspond au point (1 ; 0) de la seconde</title>
<line x1="10" y1="210" x2="330" y2="210" stroke="#0f172a" stroke-width="1.6"/><line x1="110" y1="292" x2="110" y2="12" stroke="#0f172a" stroke-width="1.6"/><polygon points="330,210 322,206 322,214" fill="#0f172a"/><polygon points="110,12 106,20 114,20" fill="#0f172a"/><line x1="22.0" y1="298.0" x2="310.0" y2="10.0" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><polyline points="6.0,207.0 7.4,206.9 8.9,206.8 10.3,206.7 11.7,206.6 13.2,206.4 14.6,206.3 16.0,206.2 17.5,206.0 18.9,205.9 20.3,205.7 21.8,205.6 23.2,205.4 24.6,205.3 26.1,205.1 27.5,204.9 28.9,204.7 30.4,204.5 31.8,204.3 33.2,204.1 34.7,203.9 36.1,203.7 37.5,203.5 39.0,203.2 40.4,203.0 41.8,202.7 43.3,202.5 44.7,202.2 46.1,201.9 47.6,201.6 49.0,201.3 50.4,201.0 51.9,200.6 53.3,200.3 54.7,200.0 56.2,199.6 57.6,199.2 59.0,198.8 60.5,198.4 61.9,198.0 63.3,197.5 64.8,197.1 66.2,196.6 67.6,196.1 69.1,195.6 70.5,195.1 71.9,194.6 73.4,194.0 74.8,193.4 76.2,192.8 77.7,192.2 79.1,191.5 80.5,190.9 82.0,190.2 83.4,189.4 84.8,188.7 86.3,187.9 87.7,187.1 89.1,186.3 90.6,185.4 92.0,184.5 93.4,183.6 94.9,182.6 96.3,181.6 97.7,180.6 99.2,179.5 100.6,178.4 102.0,177.2 103.5,176.0 104.9,174.8 106.3,173.5 107.8,172.2 109.2,170.8 110.6,169.4 112.1,167.9 113.5,166.3 114.9,164.7 116.4,163.1 117.8,161.4 119.2,159.6 120.7,157.8 122.1,155.9 123.5,153.9 125.0,151.8 126.4,149.7 127.8,147.5 129.3,145.2 130.7,142.9 132.1,140.4 133.6,137.9 135.0,135.3 136.4,132.5 137.9,129.7 139.3,126.8 140.7,123.8 142.2,120.6 143.6,117.3 145.0,114.0 146.5,110.5 147.9,106.8 149.3,103.1 150.8,99.2 152.2,95.1 153.6,90.9 155.1,86.6 156.5,82.1 157.9,77.4 159.4,72.6 160.8,67.6 162.2,62.4 163.7,57.0 165.1,51.4 166.5,45.6 168.0,39.6 169.4,33.4 170.8,27.0 172.3,20.3 173.7,13.4 175.1,6.2" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="115.5,289.6 116.7,281.5 117.9,274.8 119.2,269.0 120.4,263.9 121.6,259.5 122.8,255.4 124.1,251.8 125.3,248.4 126.5,245.3 127.8,242.4 129.0,239.8 130.2,237.3 131.5,234.9 132.7,232.7 133.9,230.5 135.2,228.5 136.4,226.6 137.6,224.8 138.9,223.1 140.1,221.4 141.3,219.8 142.6,218.2 143.8,216.8 145.0,215.3 146.2,213.9 147.5,212.6 148.7,211.3 149.9,210.1 151.2,208.8 152.4,207.7 153.6,206.5 154.9,205.4 156.1,204.3 157.3,203.3 158.6,202.2 159.8,201.2 161.0,200.3 162.2,199.3 163.5,198.4 164.7,197.5 165.9,196.6 167.2,195.7 168.4,194.9 169.6,194.0 170.9,193.2 172.1,192.4 173.3,191.6 174.6,190.8 175.8,190.1 177.0,189.4 178.3,188.6 179.5,187.9 180.7,187.2 181.9,186.5 183.2,185.8 184.4,185.2 185.6,184.5 186.9,183.9 188.1,183.2 189.3,182.6 190.6,182.0 191.8,181.4 193.0,180.8 194.3,180.2 195.5,179.6 196.7,179.0 198.0,178.5 199.2,177.9 200.4,177.4 201.6,176.8 202.9,176.3 204.1,175.8 205.3,175.3 206.6,174.7 207.8,174.2 209.0,173.7 210.3,173.2 211.5,172.8 212.7,172.3 214.0,171.8 215.2,171.3 216.4,170.9 217.7,170.4 218.9,169.9 220.1,169.5 221.3,169.0 222.6,168.6 223.8,168.2 225.0,167.7 226.3,167.3 227.5,166.9 228.7,166.5 230.0,166.1 231.2,165.7 232.4,165.3 233.7,164.9 234.9,164.5 236.1,164.1 237.4,163.7 238.6,163.3 239.8,162.9 241.0,162.5 242.3,162.2 243.5,161.8 244.7,161.4 246.0,161.1 247.2,160.7 248.4,160.3 249.7,160.0 250.9,159.6 252.1,159.3 253.4,158.9 254.6,158.6 255.8,158.3 257.1,157.9 258.3,157.6 259.5,157.3 260.8,156.9 262.0,156.6 263.2,156.3 264.4,156.0 265.7,155.6 266.9,155.3 268.1,155.0 269.4,154.7 270.6,154.4 271.8,154.1 273.1,153.8 274.3,153.5 275.5,153.2 276.8,152.9 278.0,152.6 279.2,152.3 280.4,152.0 281.7,151.7 282.9,151.4 284.1,151.2 285.4,150.9 286.6,150.6 287.8,150.3 289.1,150.0 290.3,149.8 291.5,149.5 292.8,149.2 294.0,149.0 295.2,148.7 296.5,148.4 297.7,148.2 298.9,147.9 300.1,147.6 301.4,147.4 302.6,147.1 303.8,146.9 305.1,146.6 306.3,146.4 307.5,146.1 308.8,145.9 310.0,145.6" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="110.0" cy="170.0" r="3.5" fill="#0f172a"/><circle cx="150.0" cy="210.0" r="3.5" fill="#0f172a"/>
<g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="102.0" y="224.0" text-anchor="end" fill="#0f172a">O</text><text x="178.0" y="46.0" text-anchor="start" fill="#0f6e56">C_exp</text><text x="262.0" y="140.0" text-anchor="start" fill="#b45309">C_ln</text><text x="222.0" y="28.0" text-anchor="start" fill="#94a3b8">Δ : y = x</text><text x="118.0" y="162.0" text-anchor="start" fill="#0f172a">(0 ; 1)</text><text x="150.0" y="236.0" text-anchor="middle" fill="#0f172a">(1 ; 0)</text></g></svg>
:::

::: exemple Lire et simplifier avec la réciproque

1. Le réel dont le logarithme vaut 1/2 est, par l'équivalence y = e^x ⟺ x = ln y, le réel e^(1/2) ≈ 1,6487 ✓ (c'est la lecture graphique du début).
2. e^0 = 1 parce que ln 1 = 0 ; e^1 = e ≈ 2,718 parce que ln e = 1 ; à la calculatrice, e² ≈ 7,389 et e^(−1) ≈ 0,368. Chaque valeur est strictement positive, et elles croissent avec x ✓.
3. e^(ln 2) = 2, car e^(ln x) = x pour x > 0.
4. e^(−ln 3) : on écrit −ln 3 = ln(1/3), donc e^(−ln 3) = e^(ln(1/3)) = **1/3**. Contrôle : −ln 3 ≈ −1,0986 et e^(−1,0986) ≈ 0,3333 ✓.
5. ln(e^(−2)) = **−2**, car ln(e^x) = x pour tout réel x, signe compris ; et ln(e^(−2 ln 3)) = **−2 ln 3 ≈ −2,197**.

:::

::: piege
**Erreur : « e^(ln x) = x pour tout réel x ».** Avec x = −2, on écrirait e^(ln(−2)) = −2, mais ln(−2) n'existe pas. L'erreur tente parce que ln(e^x) = x est vraie pour **tout** réel x et qu'on croit la relation symétrique. Elle ne l'est pas : e^(ln x) = x exige x > 0, car x doit être dans l'ensemble de définition de ln. Même raison pour e^x = −3 : une exponentielle n'est jamais négative, l'équation n'a aucune solution.
:::

::: verifie À toi : deux simplifications
Simplifier e^(−ln 4), puis ln(e^(3 ln 2)).

---

−ln 4 = ln(1/4), donc e^(−ln 4) = e^(ln(1/4)) = 1/4, car e^(ln x) = x pour x > 0. Puis ln(e^(3 ln 2)) = 3 ln 2 (= ln 8 ≈ 2,079), car ln(e^x) = x pour tout réel x : on rend l'exposant tel quel.
:::

::: retenir
exp est la réciproque de ln, définie sur ℝ à valeurs dans ℝ*₊ : y = e^x ⟺ x = ln y, ln(e^x) = x pour tout x, e^(ln x) = x pour x > 0, e^0 = 1, ln e = 1.
:::

## ⚡ Les règles de calcul de l'exponentielle

À la calculatrice, e^(1/2) ≈ 1,6487 et e^(2/3) ≈ 1,9477 : leur produit vaut environ 3,2113, et e^(1/2 + 2/3) = e^(7/6) ≈ 3,2113 aussi.
Coïncidence ? Le logarithme transformait les produits en sommes.
Que fait l'exponentielle, sa réciproque, dans l'autre sens ? La preuve tient en une ligne : ln(e^a × e^b) = ln(e^a) + ln(e^b) = a + b = ln(e^(a+b)), et ln est injective, donc e^a × e^b = e^(a+b).

::: propriete
**Propriétés** — « Soit deux réels a et b. P₁. e^(a+b) = e^a × e^b, e^(−a) = 1/e^a, e^(a−b) = e^a/e^b. P₂. Pour tout entier n, e^(na) = (e^a)^n. P₃. Pour tout entier naturel q ≥ 2, e^(a/q) = q√(e^a). P₄. Pour tout entier naturel q ≥ 2 et tout entier p, e^((p/q)a) = q√(e^(pa)). »
:::

L'exponentielle fait exactement le chemin inverse de ln :

| ln transforme…        | exp transforme…       |
| --------------------- | --------------------- |
| ln(ab) = ln a + ln b  | e^(a+b) = e^a × e^b   |
| ln(a/b) = ln a − ln b | e^(a−b) = e^a/e^b     |
| ln(aⁿ) = n ln a       | e^(na) = (e^a)^n      |
| ln(q√a) = (1/q) ln a  | e^(a/q) = q√(e^a)     |

::: exemple Tout ramener à une puissance de e

1. Simplifions ⁶√(e²) × e^(3/2). Par P₃, ⁶√(e²) = e^(2/6) = e^(1/3). Par P₁, e^(1/3) × e^(3/2) = e^(1/3 + 3/2) = **e^(11/6)**. Contrôle : ⁶√(e²) ≈ 1,3956 et e^(3/2) ≈ 4,4817, dont le produit vaut 6,2547 ≈ e^(11/6) ✓.
2. Simplifions (√(e^30)/√(e^(−42))) × ¹⁰√(e^(−20)). On a √(e^30) = e^15, √(e^(−42)) = e^(−21) et ¹⁰√(e^(−20)) = e^(−2). Le tout vaut e^(15 − (−21) − 2) = **e^34**. Contrôle : 15 + 21 − 2 = 34 ✓.
3. Vérifions que (e^x − e^(−x))/(e^x + e^(−x)) = (e^(2x) − 1)/(e^(2x) + 1). On multiplie numérateur et dénominateur par e^x, qui est non nul : e^x × e^x = e^(2x) et e^x × e^(−x) = e^0 = 1. Contrôle en x = ln 2, où e^x = 2 : (2 − 1/2)/(2 + 1/2) = 0,6 et (4 − 1)/(4 + 1) = 0,6 ✓.

:::

::: piege
**Erreur : « e^(a+b) = e^a + e^b ».** Avec a = b = 0, le premier membre vaut e^0 = 1 et le second 1 + 1 = 2. De même 2e^(x+y) n'est **pas** e^(2x+2y) : en x = y = 0, on trouve 2 contre 1. Seule la **somme des exposants** devient un **produit** ; le facteur 2 devant l'exponentielle ne se rentre pas dans l'exposant.
:::

::: verifie À toi : tout en une seule puissance
Écrire (e^x)³ × e^(−2x)/e^(x−1) sous la forme e^(…).

---

On ramène tout à une puissance de e et on additionne les exposants : (e^x)³ = e^(3x) par P₂, puis e^(3x) × e^(−2x) = e^x, et diviser par e^(x−1) retranche l'exposant x − 1 : e^(x − (x − 1)) = e^1 = e. Les x s'annulent : l'expression est constante.
:::

::: retenir
e^(a+b) = e^a × e^b, e^(a−b) = e^a/e^b, e^(−a) = 1/e^a, e^(na) = (e^a)^n, e^(a/q) = q√(e^a) : ramener tout à e^(…) et additionner les exposants, jamais e^a + e^b.
:::

## 🛡️ Équations et inéquations avec exponentielle

La réciproque d'une fonction strictement croissante l'est aussi (chapitre 4) : exp conserve donc l'ordre, et elle est bijective de ℝ sur ℝ*₊.
Quand peut-on « enlever » les exponentielles de part et d'autre d'une égalité ?
Et que faire d'une équation qui mêle e^(2x) et e^x ?

::: propriete
Pour tous réels A et B : e^A = e^B ⟺ A = B, et e^A ≤ e^B ⟺ A ≤ B. L'équation e^A = k n'a de solution que si **k > 0** ; alors A = ln k.
:::

::: methode
**Quatre réflexes.** (1) Isoler l'exponentielle, puis écrire les deux membres sous la forme e^A et e^B (une constante c > 0 s'écrit e^(ln c)). (2) Passer aux exposants. (3) Si e^(2x) et e^x coexistent, poser **X = e^x avec X > 0** et résoudre le trinôme en X. (4) Pour une inéquation, **diviser par une exponentielle** est permis (elle est > 0, le sens est conservé), mais jamais par une expression de signe inconnu.
:::

::: exemple Quatre résolutions et une inéquation à condition d'existence

1. e^x = 3 donne x = ln 3 ≈ 1,0986. Et e^(2x+3) = e = e^1 donne 2x + 3 = 1, soit **x = −1**. Contrôle : e^(−2+3) = e ✓.
2. (e^x − 1)(e^x − 2) = 0 : un produit est nul si l'un de ses facteurs l'est, donc e^x = 1 ou e^x = 2, soit **S = {0 ; ln 2}** (ln 2 ≈ 0,693).
3. e^(2x) + e^x − 3 = 0. On pose X = e^x > 0 : X² + X − 3 = 0, de discriminant 13, donc X = (−1 + √13)/2 ≈ 1,303 ou X = (−1 − √13)/2 ≈ −2,303. La seconde racine est **rejetée** (X > 0). Il reste x = ln((−1 + √13)/2) ≈ 0,2645. Contrôle : e^x ≈ 1,3028, e^(2x) ≈ 1,6973, et 1,6973 + 1,3028 − 3 ≈ 0 ✓.
4. e^(3x) ≤ 4e^x. On divise par e^x > 0 : e^(2x) ≤ 4, soit 2x ≤ ln 4 et **x ≤ ln 2**. Contrôle en x = ln 2 : 2³ = 8 et 4 × 2 = 8, égalité à la borne ✓.
5. 2 − e^(1/x) > 0, avec x ≠ 0. Elle équivaut à e^(1/x) < 2, soit 1/x < ln 2. Si x < 0, 1/x est négatif, donc inférieur à ln 2 : tout x < 0 convient. Si x > 0, on multiplie par x et on divise par ln 2 > 0 : x > 1/ln 2 ≈ 1,443. Donc **S = ]−∞ ; 0[ ∪ ]1/ln 2 ; +∞[**. Contrôle : x = −1 donne 2 − e^(−1) ≈ 1,63 > 0 ✓ ; x = 1 donne 2 − e ≈ −0,72 < 0, exclu ✓.

:::

::: piege
**Erreur : garder la racine négative de X.** Dans l'exemple 3, écrire x = ln((−1 − √13)/2) revient à calculer le logarithme de −2,303, qui n'existe pas. L'erreur tente parce que le trinôme en X donne bien deux racines et qu'on les convertit mécaniquement. Mais X est une exponentielle : X > 0. Toute racine X ≤ 0 est rejetée, et l'équation e^x = X n'a de solution que pour la racine positive.
:::

::: verifie À toi : poser X = e^x
Résoudre e^(2x) − 4e^x − 5 = 0.

---

On pose X = e^x > 0 : X² − 4X − 5 = (X − 5)(X + 1) = 0, donc X = 5 ou X = −1. La racine −1 est rejetée (X > 0). Il reste e^x = 5, soit x = ln 5 ≈ 1,609. Contrôle : e^(2x) = 25, et 25 − 20 − 5 = 0 ✓.
:::

::: retenir
e^A = e^B ⟺ A = B et e^A ≤ e^B ⟺ A ≤ B ; e^A = k exige k > 0 ; avec e^(2x) et e^x on pose X = e^x > 0 et l'on rejette toute racine X ≤ 0.
:::

## 🔮 Étude de exp : dérivée, limites, tangente

Quelle est la pente de la courbe de exp en un point d'abscisse x ? Le chapitre 4 donne la dérivée d'une réciproque : (f⁻¹)′(y) = 1/f′(f⁻¹(y)).
Avec f = ln, de dérivée f′(t) = 1/t, et f⁻¹ = exp : exp′(x) = 1/ln′(e^x) = 1/(1/e^x) = e^x.
La pente de la courbe en chaque point est donc égale à la hauteur de ce point. Que deviennent les limites ?

::: propriete
**Théorème** — « • lim_{x→−∞} e^x = 0, lim_{x→+∞} e^x = +∞, lim_{x→+∞} e^x/x = +∞, lim_{x→0} (e^x − 1)/x = 1. • La fonction exponentielle est dérivable sur ℝ et sa fonction dérivée est la fonction x ↦ e^x. La fonction exponentielle est strictement croissante sur ℝ. • La fonction exponentielle est bijective de ℝ sur ℝ*₊. »
:::

| x      | −∞ | →  | +∞ |
| ------ | -- | -- | -- |
| (e^x)′ |    | +  |    |
| e^x    | 0  | ↗  | +∞ |

Deux limites méritent leur preuve.

- **e^x/x → +∞.** On pose X = e^x, donc x = ln X et X → +∞. Alors e^x/x = X/ln X, inverse de (ln X)/X qui tend vers 0 : la limite est +∞. La courbe a une **branche parabolique de direction (Oy)**.
- **(e^x − 1)/x → 1 en 0.** C'est le taux d'accroissement (e^x − e^0)/(x − 0), donc le nombre dérivé de exp en 0, soit e^0 = 1. Contrôle : en x = 0,01, (e^(0,01) − 1)/0,01 ≈ 1,005 ✓.

**La tangente en 0.** Elle a pour équation y = exp′(0)(x − 0) + exp(0), soit **T : y = x + 1**. Posons h(x) = e^x − x − 1 : h′(x) = e^x − 1 est négative sur ]−∞, 0[ et positive sur ]0, +∞[, donc h admet un minimum en 0, où h(0) = 0. Ainsi **e^x ≥ x + 1** pour tout réel x, avec égalité seulement en 0.

::: figure La courbe C de exp reste au-dessus de sa tangente T : y = x + 1 et ne la touche qu'en A(0 ; 1) : on lit d'un coup d'œil l'inégalité e^x ≥ x + 1.
<svg viewBox="0 0 340 270">
<title>Courbe de exp et sa tangente T au point A(0 ; 1), d'équation y = x + 1 : la courbe reste au-dessus de T et la touche seulement en A</title>
<line x1="10" y1="215" x2="330" y2="215" stroke="#0f172a" stroke-width="1.6"/><line x1="140" y1="262" x2="140" y2="12" stroke="#0f172a" stroke-width="1.6"/><polygon points="330,215 322,211 322,219" fill="#0f172a"/><polygon points="140,12 136,20 144,20" fill="#0f172a"/><line x1="44.0" y1="271.0" x2="228.0" y2="87.0" stroke="#b45309" stroke-width="2.2"/><polyline points="12.0,213.4 13.6,213.3 15.2,213.2 16.8,213.2 18.4,213.1 20.0,213.0 21.6,212.9 23.2,212.8 24.9,212.8 26.5,212.7 28.1,212.6 29.7,212.5 31.3,212.4 32.9,212.3 34.5,212.1 36.1,212.0 37.7,211.9 39.3,211.8 40.9,211.6 42.5,211.5 44.1,211.4 45.7,211.2 47.3,211.1 49.0,210.9 50.6,210.7 52.2,210.5 53.8,210.4 55.4,210.2 57.0,210.0 58.6,209.8 60.2,209.6 61.8,209.3 63.4,209.1 65.0,208.9 66.6,208.6 68.2,208.3 69.8,208.1 71.4,207.8 73.1,207.5 74.7,207.2 76.3,206.9 77.9,206.5 79.5,206.2 81.1,205.8 82.7,205.5 84.3,205.1 85.9,204.7 87.5,204.2 89.1,203.8 90.7,203.3 92.3,202.9 93.9,202.4 95.5,201.8 97.2,201.3 98.8,200.7 100.4,200.1 102.0,199.5 103.6,198.9 105.2,198.2 106.8,197.6 108.4,196.8 110.0,196.1 111.6,195.3 113.2,194.5 114.8,193.7 116.4,192.8 118.0,191.9 119.6,191.0 121.3,190.0 122.9,188.9 124.5,187.9 126.1,186.8 127.7,185.6 129.3,184.4 130.9,183.1 132.5,181.8 134.1,180.5 135.7,179.1 137.3,177.6 138.9,176.1 140.5,174.5 142.1,172.8 143.7,171.1 145.4,169.3 147.0,167.4 148.6,165.4 150.2,163.4 151.8,161.3 153.4,159.1 155.0,156.8 156.6,154.4 158.2,151.9 159.8,149.4 161.4,146.7 163.0,143.9 164.6,141.0 166.2,137.9 167.8,134.8 169.5,131.5 171.1,128.0 172.7,124.5 174.3,120.8 175.9,116.9 177.5,112.9 179.1,108.7 180.7,104.3 182.3,99.8 183.9,95.1 185.5,90.2 187.1,85.1 188.7,79.7 190.3,74.2 191.9,68.4 193.6,62.4 195.2,56.2 196.8,49.7 198.4,42.9 200.0,35.8 201.6,28.5 203.2,20.8 204.8,12.9" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="140.0" cy="175.0" r="4" fill="#0f172a"/>
<g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="132.0" y="229.0" text-anchor="end" fill="#0f172a">O</text><text x="212.8" y="34.0" text-anchor="start" fill="#0f6e56">C : y = eˣ</text><text x="238.0" y="104.0" text-anchor="start" fill="#b45309">T : y = x + 1</text><text x="148.0" y="167.0" text-anchor="start" fill="#0f172a">A(0 ; 1)</text></g></svg>
:::

::: propriete
**Théorème** — « Soit m et n deux entiers naturels non nuls, lim_{x→+∞} e^(nx)/x^m = +∞, lim_{x→−∞} x^m e^(nx) = 0. »
Face à une forme indéterminée, **l'exponentielle l'emporte sur toute puissance de x**. En −∞, l'exponentielle écrase la puissance vers 0.
:::

::: exemple Trois limites et une étude

1. lim_{x→+∞} (x² − e^(2x)) est de la forme ∞ − ∞. On factorise : x² − e^(2x) = e^(2x)(x²/e^(2x) − 1). Or x²/e^(2x) → 0 par le théorème, donc la parenthèse tend vers −1 et le produit vers **−∞**. Contrôle en x = 10 : 100 − e^20 ≈ −4,85 × 10⁸ ✓.
2. lim_{x→−∞} x(e^(2x) − e^x) = lim (x e^(2x) − x e^x). Chaque terme est de la forme x^m e^(nx) avec x → −∞, donc tend vers 0 : la limite vaut **0**. Contrôle en x = −10 : −10(e^(−20) − e^(−10)) ≈ 4,5 × 10⁻⁴, proche de 0 ✓.
3. lim_{x→+∞} e^x/(x³ + 1) : on écrit e^x/(x³ + 1) = (e^x/x³) × (x³/(x³ + 1)). Le premier facteur tend vers +∞, le second vers 1 : la limite est **+∞**.
4. Étude de f(x) = x e^x. En −∞, f(x) → 0⁻ par le théorème (m = 1, n = 1) ; en +∞, f → +∞ et f(x)/x = e^x → +∞ (branche parabolique). On a f′(x) = (1 + x)e^x, du signe de 1 + x : minimum f(−1) = −1/e ≈ −0,368. Puis f″(x) = (2 + x)e^x change de signe en −2 : le point I(−2 ; −2e^(−2)) ≈ (−2 ; −0,271) est un **point d'inflexion**, où la tangente a pour pente f′(−2) = −e^(−2) ≈ −0,135.

:::

::: piege
**Erreur : « x e^x → −∞ quand x → −∞ ».** On regarde le facteur x qui tend vers −∞ et on oublie que e^x tend vers 0 : c'est une forme 0 × ∞, indéterminée. Le théorème tranche : x^m e^(nx) → 0. Test numérique : en x = −10, x e^x ≈ −4,5 × 10⁻⁴ ; en x = −20, ≈ −4,1 × 10⁻⁸ : la valeur se **rapproche de 0**, elle ne plonge pas.
:::

::: verifie À toi : une forme ∞ − ∞
Calculer lim_{x→+∞} (e^x − x⁴).

---

La forme est ∞ − ∞. On factorise par l'exponentielle : e^x − x⁴ = e^x(1 − x⁴/e^x). Par croissances comparées (n = 1, m = 4), x⁴/e^x → 0, donc la parenthèse tend vers 1 et le produit vers +∞ : la limite vaut +∞.
:::

::: retenir
(e^x)′ = e^x, exp est strictement croissante, bijective de ℝ sur ℝ*₊ ; lim_{−∞} e^x = 0, lim_{+∞} e^x = +∞ ; tangente en 0 : y = x + 1, et e^x ≥ x + 1 ; e^(nx)/x^m → +∞ en +∞ et x^m e^(nx) → 0 en −∞.
:::

## 🧮 La fonction x ↦ e^(u(x)) : dériver, primitiver, intégrer

Quelle est la pente de x ↦ e^(2x) en 0 ? C'est la composée de u : x ↦ 2x suivie de exp : on s'attend à un facteur 2 devant l'exponentielle.
Le théorème de dérivation des composées donne une règle générale pour dériver, et, lue à l'envers, pour primitiver.
Comment la reconnaître d'un coup d'œil dans une intégrale ?

::: propriete
**Théorème** — « Soit u une fonction dérivable sur un intervalle I. La fonction h : x ↦ e^(u(x)) est dérivable sur I et h′(x) = u′(x)e^(u(x)), x ∈ I. »
**Corollaire** — « Soit u une fonction dérivable sur un intervalle I. Les primitives sur I de la fonction x ↦ u′(x)e^(u(x)) sont les fonctions x ↦ e^(u(x)) + k, k ∈ ℝ. »
:::

::: exemple Dériver, primitiver, intégrer

1. Dérivons f(x) = √x e^√x sur ]0, +∞[. Avec u(x) = √x, u′(x) = 1/(2√x). Par la dérivée d'un produit : f′(x) = (1/(2√x))e^√x + √x × (1/(2√x))e^√x = e^√x(1/(2√x) + 1/2) = **(1 + √x)e^√x/(2√x)**. Contrôle en x = 4 : (1 + 2)e²/4 ≈ 5,542, et le taux d'accroissement numérique donne 5,5418 ✓.
2. Dérivons g(x) = (e^(2x) + 1)/(2e^(2x) + 3). Avec (e^(2x))′ = 2e^(2x) : g′(x) = [2e^(2x)(2e^(2x) + 3) − 4e^(2x)(e^(2x) + 1)]/(2e^(2x) + 3)² = **2e^(2x)/(2e^(2x) + 3)²**. Contrôle en x = 0 : 2/25 = 0,08 ✓ ; g est strictement croissante.
3. Primitive de f(x) = x e^(x²) sur ℝ. Avec u(x) = x², u′(x) = 2x, et x e^(x²) = ½ × 2x e^(x²) : une primitive est F(x) = ½e^(x²). Vérification : F′(x) = ½ × 2x × e^(x²) = x e^(x²) ✓.
4. ∫₀¹ e^(−x+1) dx : avec u(x) = −x + 1, u′ = −1, une primitive de e^(−x+1) est −e^(1−x) ; l'intégrale vaut [−e^(1−x)]₀¹ = −1 + e = **e − 1 ≈ 1,718**. Et ∫₀¹ x e^(x²) dx = [½e^(x²)]₀¹ = (e − 1)/2 ≈ 0,859.
5. ∫₀¹ x e^x dx exige une **intégration par parties** : avec f(x) = x et g′(x) = e^x, I = [x e^x]₀¹ − ∫₀¹ e^x dx = e − (e − 1) = **1**. Pour J = ∫₀¹ x² e^x dx, une seconde IPP donne J = [x² e^x]₀¹ − 2I = e − 2 ≈ 0,718. Contrôle : sur [0, 1], x² ≤ x, donc 0 < J < I ✓.
6. **Deux parties qui reviennent au point de départ.** K = ∫₀^π e^x cos x dx. Avec f = cos x, g′ = e^x : K = [e^x cos x]₀^π + ∫₀^π e^x sin x dx = −e^π − 1 + L. Puis L = ∫₀^π e^x sin x dx = [e^x sin x]₀^π − ∫₀^π e^x cos x dx = 0 − K. Donc K = −e^π − 1 − K, soit **K = −(e^π + 1)/2 ≈ −12,07** : on ne calcule pas K, on résout une équation dont K est l'inconnue.

:::

Quelques primitives à reconnaître d'un coup d'œil :

| f(x)              | u(x)   | primitive F(x)     |
| ----------------- | ------ | ------------------ |
| e^(−3x)           | −3x    | −(1/3)e^(−3x) + k  |
| (2x + 1)e^(x²+x)  | x² + x | e^(x²+x) + k       |
| sin x · e^(cos x) | cos x  | −e^(cos x) + k     |

::: piege
**Erreur : oublier le facteur u′.** On écrit (e^(−3x))′ = e^(−3x), « comme exp ». Elle tente parce que exp est sa propre dérivée. Mais la dérivée de e^(u) est u′e^(u) : ici u′ = −3 et (e^(−3x))′ = **−3e^(−3x)**. Test en x = 0 : la fonction e^(−3x) vaut 1 en 0 et décroît (e^(−0,3) ≈ 0,74 en x = 0,1), donc sa pente est négative, alors que e^(−3x) est positive. Même vigilance pour les primitives : une primitive de e^(−3x) est −(1/3)e^(−3x), jamais e^(−3x) seule.
:::

::: verifie À toi : reconnaître u′e^u
Trouver une primitive de f(x) = x² e^(x³) sur ℝ.

---

Avec u(x) = x³, u′(x) = 3x² et x² e^(x³) = (1/3) × 3x² e^(x³) = (1/3)u′e^u. Une primitive est F(x) = (1/3)e^(x³). Vérification : F′(x) = (1/3) × 3x² × e^(x³) = x² e^(x³) ✓. Oublier le facteur 1/3 donnerait une dérivée trois fois trop grande.
:::

::: retenir
(e^u)′ = u′e^u ; les primitives de u′e^u sont e^u + k ; on reconnaît u′e^u **avant** de penser intégration par parties (∫ x e^(x²) par primitive, ∫ x e^x par parties).
:::

## 📐 Exponentielle de base a

Euler avait posé : une province de 100 000 habitants dont la population augmente chaque année d'un trentième. Après n années, il y a 100 000 × (31/30)ⁿ habitants.
Cette formule a un sens pour n entier. Et pour 2,5 ans, ou pour √2 ans ?
Une idée : écrire aⁿ avec l'exponentielle. Comme e^(ln a) = a pour a > 0, la propriété P₂ donne aⁿ = (e^(ln a))ⁿ = e^(n ln a), vraie pour tout entier n.

::: definition
**Puissance à exposant réel** — « Soit un réel a > 0. Pour tout réel b, on pose a^b = e^(b ln a). »
**Exponentielle de base a** — « Soit un réel a > 0. On appelle fonction exponentielle de base a la fonction x ↦ a^x. »
:::

::: propriete
**Propriétés** — « Pour tous nombres réels strictement positifs a et b et tous réels c et d, a^(c+d) = a^c × a^d ; (a^c)^d = a^(cd) ; a^(−d) = 1/a^d ; a^(c−d) = a^c/a^d ; a^c × b^c = (ab)^c ; a^c/b^c = (a/b)^c. »
**Conséquences** — « Soit un réel a > 0. La fonction x ↦ a^x est dérivable sur ℝ et sa fonction dérivée est la fonction x ↦ (ln a)a^x. La fonction x ↦ a^x est strictement croissante sur ℝ si a > 1. La fonction x ↦ a^x est strictement décroissante sur ℝ si 0 < a < 1. La fonction x ↦ 1^x est une fonction constante. Si a > 1 alors lim_{x→+∞} a^x = +∞ ; lim_{x→−∞} a^x = 0. Si 0 < a < 1 alors lim_{x→+∞} a^x = 0 ; lim_{x→−∞} a^x = +∞. »
La dérivée se retrouve en une ligne : (a^x)′ = (e^(x ln a))′ = (ln a)e^(x ln a) = (ln a)a^x. C'est le **signe de ln a** qui décide : positif si a > 1, négatif si 0 < a < 1.
:::

::: figure Les trois courbes passent par (0 ; 1). Celles de 2ˣ et 3ˣ montent (base > 1), la seconde plus vite pour x > 0 ; celle de (1/2)ˣ descend (base < 1) et est symétrique de celle de 2ˣ par rapport à l'axe des ordonnées.
<svg viewBox="0 0 340 250">
<title>Courbes de x ↦ 2ˣ, 3ˣ et (1/2)ˣ : toutes passent par le point (0 ; 1) ; les bases supérieures à 1 donnent une courbe croissante, la base 1/2 une courbe décroissante</title>
<line x1="10" y1="205" x2="330" y2="205" stroke="#0f172a" stroke-width="1.6"/><line x1="170" y1="240" x2="170" y2="12" stroke="#0f172a" stroke-width="1.6"/><polygon points="330,205 322,201 322,209" fill="#0f172a"/><polygon points="170,12 166,20 174,20" fill="#0f172a"/><polyline points="8.0,204.4 9.7,204.4 11.4,204.4 13.2,204.3 14.9,204.3 16.6,204.3 18.3,204.3 20.0,204.2 21.8,204.2 23.5,204.2 25.2,204.1 26.9,204.1 28.6,204.0 30.4,204.0 32.1,204.0 33.8,203.9 35.5,203.9 37.2,203.8 39.0,203.8 40.7,203.7 42.4,203.7 44.1,203.6 45.8,203.6 47.6,203.5 49.3,203.4 51.0,203.4 52.7,203.3 54.4,203.2 56.1,203.1 57.9,203.1 59.6,203.0 61.3,202.9 63.0,202.8 64.7,202.7 66.5,202.6 68.2,202.5 69.9,202.4 71.6,202.3 73.3,202.2 75.1,202.0 76.8,201.9 78.5,201.8 80.2,201.6 81.9,201.5 83.7,201.4 85.4,201.2 87.1,201.0 88.8,200.9 90.5,200.7 92.3,200.5 94.0,200.3 95.7,200.1 97.4,199.9 99.1,199.7 100.9,199.5 102.6,199.2 104.3,199.0 106.0,198.7 107.7,198.4 109.5,198.2 111.2,197.9 112.9,197.6 114.6,197.2 116.3,196.9 118.1,196.6 119.8,196.2 121.5,195.8 123.2,195.4 124.9,195.0 126.7,194.6 128.4,194.1 130.1,193.7 131.8,193.2 133.5,192.7 135.3,192.2 137.0,191.6 138.7,191.0 140.4,190.4 142.1,189.8 143.9,189.2 145.6,188.5 147.3,187.8 149.0,187.0 150.7,186.3 152.4,185.5 154.2,184.6 155.9,183.7 157.6,182.8 159.3,181.9 161.0,180.9 162.8,179.9 164.5,178.8 166.2,177.7 167.9,176.5 169.6,175.3 171.4,174.0 173.1,172.7 174.8,171.3 176.5,169.8 178.2,168.3 180.0,166.7 181.7,165.1 183.4,163.4 185.1,161.6 186.8,159.7 188.6,157.8 190.3,155.8 192.0,153.7 193.7,151.5 195.4,149.2 197.2,146.8 198.9,144.3 200.6,141.7 202.3,139.0 204.0,136.1 205.8,133.2 207.5,130.1 209.2,126.9 210.9,123.5 212.6,120.0 214.4,116.4 216.1,112.6 217.8,108.6 219.5,104.5 221.2,100.2 223.0,95.7 224.7,91.0 226.4,86.1 228.1,81.0 229.8,75.7 231.6,70.2 233.3,64.4 235.0,58.4 236.7,52.1 238.4,45.5 240.2,38.7 241.9,31.6 243.6,24.1 245.3,16.4 247.0,8.3" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="8.0,202.5 10.0,202.5 11.9,202.4 13.9,202.3 15.8,202.2 17.8,202.1 19.8,202.0 21.7,201.9 23.7,201.8 25.6,201.8 27.6,201.7 29.6,201.6 31.5,201.4 33.5,201.3 35.4,201.2 37.4,201.1 39.4,201.0 41.3,200.9 43.3,200.7 45.3,200.6 47.2,200.5 49.2,200.3 51.1,200.2 53.1,200.0 55.1,199.9 57.0,199.7 59.0,199.6 60.9,199.4 62.9,199.2 64.9,199.1 66.8,198.9 68.8,198.7 70.7,198.5 72.7,198.3 74.7,198.1 76.6,197.9 78.6,197.7 80.5,197.4 82.5,197.2 84.5,197.0 86.4,196.7 88.4,196.5 90.3,196.2 92.3,195.9 94.3,195.7 96.2,195.4 98.2,195.1 100.2,194.8 102.1,194.5 104.1,194.1 106.0,193.8 108.0,193.5 110.0,193.1 111.9,192.7 113.9,192.4 115.8,192.0 117.8,191.6 119.8,191.2 121.7,190.7 123.7,190.3 125.6,189.9 127.6,189.4 129.6,188.9 131.5,188.4 133.5,187.9 135.4,187.4 137.4,186.8 139.4,186.3 141.3,185.7 143.3,185.1 145.2,184.5 147.2,183.9 149.2,183.2 151.1,182.6 153.1,181.9 155.1,181.2 157.0,180.4 159.0,179.7 160.9,178.9 162.9,178.1 164.9,177.3 166.8,176.4 168.8,175.6 170.7,174.7 172.7,173.7 174.7,172.8 176.6,171.8 178.6,170.8 180.5,169.7 182.5,168.6 184.5,167.5 186.4,166.4 188.4,165.2 190.3,164.0 192.3,162.7 194.3,161.4 196.2,160.1 198.2,158.7 200.1,157.3 202.1,155.8 204.1,154.3 206.0,152.7 208.0,151.1 210.0,149.5 211.9,147.8 213.9,146.0 215.8,144.2 217.8,142.4 219.8,140.4 221.7,138.5 223.7,136.4 225.6,134.3 227.6,132.1 229.6,129.9 231.5,127.6 233.5,125.2 235.4,122.8 237.4,120.3 239.4,117.7 241.3,115.0 243.3,112.2 245.2,109.4 247.2,106.5 249.2,103.4 251.1,100.3 253.1,97.1 255.0,93.8 257.0,90.4 259.0,86.9 260.9,83.3 262.9,79.5 264.9,75.7 266.8,71.7 268.8,67.6 270.7,63.4 272.7,59.1 274.7,54.6 276.6,50.0 278.6,45.2 280.5,40.3 282.5,35.3" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="53.0,23.1 55.0,28.6 57.0,33.9 59.0,39.1 61.0,44.1 63.0,49.0 65.0,53.7 67.0,58.3 68.9,62.7 70.9,67.0 72.9,71.2 74.9,75.2 76.9,79.2 78.9,83.0 80.9,86.7 82.9,90.2 84.9,93.7 86.9,97.1 88.9,100.3 90.9,103.5 92.9,106.6 94.9,109.5 96.8,112.4 98.8,115.2 100.8,117.9 102.8,120.6 104.8,123.1 106.8,125.6 108.8,128.0 110.8,130.3 112.8,132.6 114.8,134.8 116.8,136.9 118.8,139.0 120.8,140.9 122.8,142.9 124.7,144.8 126.7,146.6 128.7,148.3 130.7,150.1 132.7,151.7 134.7,153.3 136.7,154.9 138.7,156.4 140.7,157.9 142.7,159.3 144.7,160.7 146.7,162.0 148.7,163.3 150.6,164.6 152.6,165.8 154.6,167.0 156.6,168.1 158.6,169.3 160.6,170.3 162.6,171.4 164.6,172.4 166.6,173.4 168.6,174.3 170.6,175.3 172.6,176.2 174.6,177.0 176.6,177.9 178.6,178.7 180.5,179.5 182.5,180.3 184.5,181.0 186.5,181.7 188.5,182.4 190.5,183.1 192.5,183.8 194.5,184.4 196.5,185.0 198.5,185.7 200.5,186.2 202.5,186.8 204.5,187.4 206.4,187.9 208.4,188.4 210.4,188.9 212.4,189.4 214.4,189.9 216.4,190.3 218.4,190.8 220.4,191.2 222.4,191.6 224.4,192.0 226.4,192.4 228.4,192.8 230.4,193.2 232.4,193.5 234.4,193.9 236.3,194.2 238.3,194.5 240.3,194.8 242.3,195.2 244.3,195.5 246.3,195.7 248.3,196.0 250.3,196.3 252.3,196.6 254.3,196.8 256.3,197.1 258.3,197.3 260.3,197.5 262.2,197.8 264.2,198.0 266.2,198.2 268.2,198.4 270.2,198.6 272.2,198.8 274.2,199.0 276.2,199.2 278.2,199.3 280.2,199.5 282.2,199.7 284.2,199.8 286.2,200.0 288.2,200.1 290.2,200.3 292.1,200.4 294.1,200.6 296.1,200.7 298.1,200.8 300.1,201.0 302.1,201.1 304.1,201.2 306.1,201.3 308.1,201.4 310.1,201.5 312.1,201.6 314.1,201.7 316.1,201.8 318.1,201.9 320.0,202.0 322.0,202.1 324.0,202.2 326.0,202.3 328.0,202.4 330.0,202.4 332.0,202.5" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><circle cx="170.0" cy="175.0" r="4" fill="#0f172a"/>
<g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="162.0" y="219.0" text-anchor="end" fill="#0f172a">O</text><text x="252.8" y="36.0" text-anchor="start" fill="#b45309">y = 3ˣ</text><text x="284.2" y="52.0" text-anchor="start" fill="#0f6e56">y = 2ˣ</text><text x="8.0" y="36.0" text-anchor="start" fill="#0f172a">y = (1/2)ˣ</text><text x="156.0" y="145.0" text-anchor="end" fill="#0f172a">(0 ; 1)</text></g></svg>
:::

::: exemple Population, puissances et équations

1. Chez Euler, 100 000 × (31/30)^100 = 100 000 × e^(100 ln(31/30)) = 100 000 × e^(3,279) ≈ **2 654 874** habitants, soit environ 2,65 millions : en un siècle, la population est multipliée par plus de 26.
2. e^(3 ln 2) = 2³ = **8** ; e^(4 ln(1/2)) = (1/2)⁴ = **1/16** ; e^(−ln(1/2)) = (1/2)^(−1) = **2** ; e^(−2 ln √2) = (√2)^(−2) = **1/2**. Contrôle du premier : 3 ln 2 ≈ 2,079 et e^(2,079) ≈ 8 ✓.
3. Résoudre 10^(x+1) = 2^(−x+2). On passe au logarithme : (x + 1) ln 10 = (2 − x) ln 2, soit x(ln 10 + ln 2) = 2 ln 2 − ln 10, donc x = ln(0,4)/ln 20 ≈ **−0,306**. Contrôle : 10^(0,694) ≈ 4,945 et 2^(2,306) ≈ 4,945 ✓. Et 2^x = 2^(−x+1) donne x = −x + 1, soit **x = 1/2**.
4. lim_{x→±∞} 2^(x²−2x). L'exposant x² − 2x tend vers +∞ dans les deux cas, et la base 2 est > 1 : la limite vaut **+∞** en +∞ comme en −∞. Contrôle en x = −10 : l'exposant vaut 120 et 2^120 est gigantesque ✓.

:::

::: piege
**Erreur : « (a^x)′ = x a^(x−1) ».** Elle tente parce qu'on connaît (xⁿ)′ = n x^(n−1). Mais ici l'exposant est la **variable** et la base est fixe. Avec a = 2 en x = 0 la formule fausse donne 0 ; or 2^x passe de 1 à 2^(0,01) ≈ 1,00696 entre 0 et 0,01, soit une pente de 0,696 ≈ ln 2. La bonne formule est (2^x)′ = (ln 2) 2^x.
:::

::: verifie À toi : même base des deux côtés
Résoudre 3^x = 9^(1−x).

---

On ramène à la base 3 : 9^(1−x) = (3²)^(1−x) = 3^(2−2x), car (a^c)^d = a^(cd). L'égalité 3^x = 3^(2−2x) équivaut à x = 2 − 2x (la fonction t ↦ 3^t est strictement croissante), soit x = 2/3. Contrôle : 3^(2/3) ≈ 2,080 et 9^(1/3) ≈ 2,080 ✓.
:::

::: retenir
a^b = e^(b ln a) pour a > 0 ; (a^x)′ = (ln a)a^x, jamais x a^(x−1) ; a > 1 : croissante, a^x → +∞ en +∞ et → 0 en −∞ ; 0 < a < 1 : décroissante, limites échangées.
:::

## 👑 Fonctions puissances et croissances comparées

Que vaut √(x³) pour x > 0 ? On l'écrit (x³)^(1/2), et l'on aimerait dire x^(3/2).
La même idée que pour a^b, mais cette fois c'est la **base** qui varie, sur ℝ*₊ où ln x existe. Que devient alors l'exposant r quand c'est un rationnel ?

::: definition
**Fonction puissance** — « Soit r un rationnel. On appelle fonction puissance r la fonction x ↦ e^(r·ln x), x > 0. » On la note x^r : « Pour tout rationnel r et tout x > 0, on note e^(r·ln x) = x^r. »
:::

::: propriete
**Théorème** — « Soit r un rationnel. La fonction x ↦ x^r est dérivable sur ℝ*₊ et sa dérivée est la fonction x ↦ r x^(r−1). »
**Corollaire** — « Soit r un rationnel différent de −1. Les primitives sur ℝ*₊ de la fonction x ↦ x^r sont les fonctions x ↦ (1/(r + 1)) x^(r+1) + k, k ∈ ℝ. »
**Limites** — « Si r > 0 alors lim_{x→+∞} x^r = +∞ ; lim_{x→0⁺} x^r = 0. Si r < 0 alors lim_{x→+∞} x^r = 0 ; lim_{x→0⁺} x^r = +∞. »
Les racines du chapitre 4 sont un cas particulier : pour n ≥ 2 et x > 0, ⁿ√x = x^(1/n), car e^((1/n) ln x) = e^(ln ⁿ√x) = ⁿ√x.
:::

::: figure La courbe de x ↦ x^(3/2) (verte) et celle de sa réciproque x ↦ x^(2/3) (orange) sont symétriques par rapport à y = x ; elles se coupent en (1 ; 1), et les points (2 ; 2√2) et (2√2 ; 2) se correspondent.
<svg viewBox="0 0 340 270">
<title>Courbes de x ↦ x^(3/2) et de sa réciproque x ↦ x^(2/3) sur ]0 ; +∞[ : elles sont symétriques par rapport à la droite y = x, et les points (2 ; 2√2) et (2√2 ; 2) se correspondent</title>
<line x1="10" y1="238" x2="330" y2="238" stroke="#0f172a" stroke-width="1.6"/><line x1="40" y1="250" x2="40" y2="12" stroke="#0f172a" stroke-width="1.6"/><polygon points="330,238 322,234 322,242" fill="#0f172a"/><polygon points="40,12 36,20 44,20" fill="#0f172a"/><line x1="40" y1="238" x2="270.0" y2="8.0" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><polyline points="40.0,238.0 41.0,237.9 41.9,237.6 42.9,237.3 43.9,236.9 44.8,236.5 45.8,236.0 46.8,235.5 47.7,235.0 48.7,234.4 49.7,233.7 50.6,233.1 51.6,232.4 52.6,231.7 53.5,231.0 54.5,230.2 55.5,229.4 56.4,228.6 57.4,227.7 58.4,226.9 59.3,226.0 60.3,225.1 61.3,224.1 62.2,223.2 63.2,222.2 64.2,221.2 65.1,220.2 66.1,219.1 67.1,218.1 68.0,217.0 69.0,215.9 70.0,214.8 70.9,213.7 71.9,212.5 72.9,211.4 73.8,210.2 74.8,209.0 75.8,207.7 76.7,206.5 77.7,205.3 78.7,204.0 79.6,202.7 80.6,201.4 81.6,200.1 82.5,198.8 83.5,197.4 84.5,196.1 85.4,194.7 86.4,193.3 87.4,191.9 88.3,190.5 89.3,189.0 90.3,187.6 91.2,186.1 92.2,184.7 93.2,183.2 94.1,181.7 95.1,180.2 96.1,178.6 97.0,177.1 98.0,175.5 99.0,174.0 99.9,172.4 100.9,170.8 101.9,169.2 102.8,167.6 103.8,165.9 104.8,164.3 105.7,162.6 106.7,161.0 107.7,159.3 108.6,157.6 109.6,155.9 110.6,154.2 111.5,152.4 112.5,150.7 113.5,148.9 114.4,147.2 115.4,145.4 116.4,143.6 117.3,141.8 118.3,140.0 119.3,138.2 120.2,136.4 121.2,134.5 122.2,132.7 123.1,130.8 124.1,128.9 125.1,127.0 126.0,125.1 127.0,123.2 128.0,121.3 128.9,119.4 129.9,117.5 130.9,115.5 131.8,113.5 132.8,111.6 133.8,109.6 134.7,107.6 135.7,105.6 136.7,103.6 137.6,101.6 138.6,99.5 139.6,97.5 140.5,95.4 141.5,93.4 142.5,91.3 143.4,89.2 144.4,87.1 145.4,85.0 146.3,82.9 147.3,80.8 148.3,78.7 149.2,76.5 150.2,74.4 151.2,72.2 152.1,70.1 153.1,67.9 154.1,65.7 155.0,63.5 156.0,61.3 157.0,59.1 157.9,56.9 158.9,54.6 159.9,52.4 160.8,50.2 161.8,47.9 162.8,45.6 163.7,43.4 164.7,41.1 165.7,38.8 166.6,36.5 167.6,34.2 168.6,31.8 169.5,29.5 170.5,27.2 171.5,24.8 172.4,22.5 173.4,20.1 174.4,17.7 175.3,15.4 176.3,13.0 177.3,10.6 178.2,8.2 179.2,5.7 180.2,3.3" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="40.0,238.0 41.4,233.4 42.8,230.7 44.2,228.4 45.6,226.4 47.0,224.5 48.4,222.8 49.8,221.1 51.2,219.6 52.6,218.1 54.0,216.6 55.4,215.2 56.8,213.8 58.2,212.5 59.6,211.2 61.0,210.0 62.4,208.7 63.8,207.5 65.2,206.3 66.6,205.2 68.0,204.0 69.4,202.9 70.8,201.8 72.2,200.7 73.6,199.6 75.0,198.6 76.4,197.5 77.8,196.5 79.2,195.5 80.6,194.5 82.0,193.5 83.4,192.5 84.8,191.5 86.2,190.6 87.6,189.6 89.0,188.7 90.4,187.7 91.8,186.8 93.2,185.9 94.6,185.0 96.0,184.1 97.4,183.2 98.8,182.3 100.2,181.4 101.6,180.5 103.0,179.7 104.4,178.8 105.8,178.0 107.2,177.1 108.6,176.3 110.0,175.4 111.4,174.6 112.8,173.8 114.2,172.9 115.6,172.1 117.0,171.3 118.4,170.5 119.8,169.7 121.2,168.9 122.6,168.1 124.0,167.3 125.4,166.6 126.8,165.8 128.2,165.0 129.6,164.2 131.0,163.5 132.4,162.7 133.8,161.9 135.2,161.2 136.6,160.4 138.0,159.7 139.4,158.9 140.8,158.2 142.2,157.5 143.6,156.7 145.0,156.0 146.4,155.3 147.8,154.6 149.2,153.8 150.6,153.1 152.0,152.4 153.4,151.7 154.8,151.0 156.2,150.3 157.6,149.6 159.0,148.9 160.4,148.2 161.8,147.5 163.2,146.8 164.6,146.1 166.0,145.4 167.4,144.7 168.8,144.0 170.2,143.4 171.6,142.7 173.0,142.0 174.4,141.3 175.8,140.7 177.2,140.0 178.6,139.3 180.0,138.7 181.4,138.0 182.8,137.4 184.2,136.7 185.6,136.0 187.0,135.4 188.4,134.7 189.8,134.1 191.2,133.4 192.6,132.8 194.0,132.2 195.4,131.5 196.8,130.9 198.2,130.2 199.6,129.6 201.0,129.0 202.4,128.3 203.8,127.7 205.2,127.1 206.6,126.5 208.0,125.8 209.4,125.2 210.8,124.6 212.2,124.0 213.6,123.4 215.0,122.7 216.4,122.1 217.8,121.5 219.2,120.9 220.6,120.3 222.0,119.7 223.4,119.1 224.8,118.5 226.2,117.9 227.6,117.3 229.0,116.7 230.4,116.1 231.8,115.5 233.2,114.9 234.6,114.3 236.0,113.7 237.4,113.1 238.8,112.5 240.2,111.9 241.6,111.3 243.0,110.8 244.4,110.2 245.8,109.6 247.2,109.0 248.6,108.4 250.0,107.8 251.4,107.3 252.8,106.7 254.2,106.1 255.6,105.5 257.0,105.0 258.4,104.4 259.8,103.8 261.2,103.3 262.6,102.7 264.0,102.1 265.4,101.6 266.8,101.0 268.2,100.4 269.6,99.9 271.0,99.3 272.4,98.7 273.8,98.2 275.2,97.6 276.6,97.1 278.0,96.5 279.4,96.0 280.8,95.4 282.2,94.9 283.6,94.3 285.0,93.8 286.4,93.2 287.8,92.7 289.2,92.1 290.6,91.6 292.0,91.0 293.4,90.5 294.8,89.9 296.2,89.4 297.6,88.9 299.0,88.3 300.4,87.8 301.8,87.2 303.2,86.7 304.6,86.2 306.0,85.6 307.4,85.1 308.8,84.6 310.2,84.0 311.6,83.5 313.0,83.0 314.4,82.4 315.8,81.9 317.2,81.4 318.6,80.9 320.0,80.3" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="140.0" cy="96.6" r="3.5" fill="#0f172a"/><circle cx="181.4" cy="138.0" r="3.5" fill="#0f172a"/><circle cx="90.0" cy="188.0" r="3.5" fill="#0f172a"/><line x1="40.0" y1="96.6" x2="140.0" y2="96.6" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="140.0" y1="96.6" x2="140.0" y2="238.0" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="181.4" y1="138.0" x2="181.4" y2="238.0" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="40.0" y1="138.0" x2="181.4" y2="138.0" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="34.0" y="252.0" text-anchor="end" fill="#0f172a">O</text><text x="134.0" y="86.6" text-anchor="end" fill="#0f6e56">(2 ; 2√2)</text><text x="189.4" y="154.0" text-anchor="start" fill="#b45309">(2√2 ; 2)</text><text x="150.0" y="40.0" text-anchor="end" fill="#0f6e56">y = x^(3/2)</text><text x="310.0" y="81.0" text-anchor="end" fill="#b45309">y = x^(2/3)</text><text x="240.0" y="30.0" text-anchor="start" fill="#94a3b8">y = x</text><text x="100.0" y="186.0" text-anchor="start" fill="#0f172a">(1 ; 1)</text></g></svg>
:::

::: exemple Une étude, trois intégrales, trois limites

1. Soit f(x) = √(x³) sur ℝ*₊. On écrit f(x) = e^((3/2) ln x) = x^(3/2), donc f′(x) = (3/2)x^(1/2) = (3/2)√x > 0 : f est strictement croissante. Avec lim_{0⁺} f = 0 et lim_{+∞} f = +∞, c'est une bijection de ℝ*₊ sur ℝ*₊. Pour trouver sa réciproque, on résout y = x^(3/2), soit x = y^(2/3), donc f⁻¹(y) = y^(2/3). Contrôle : f(4) = √64 = 8 et f⁻¹(8) = 8^(2/3) = 4 ✓.
2. ∫₁² x^(4/3) dx : r + 1 = 7/3, donc [(3/7)x^(7/3)]₁² = (3/7)(2^(7/3) − 1) ≈ **1,731**. Et ∫₀¹ ⁴√x dx = [(4/5)x^(5/4)]₀¹ = **4/5**. Et ∫_{1/2}^1 4x^(−1/5) dx = [5x^(4/5)]_{1/2}^1 = 5(1 − (1/2)^(4/5)) ≈ **2,128**.
3. Limites en 0⁺ et en +∞ : x^(2/3) → 0 en 0⁺ et +∞ en +∞ (exposant > 0) ; x^(−4/3) → +∞ en 0⁺ et 0 en +∞ (exposant < 0).

:::

Les croissances comparées de la section précédente s'étendent aux puissances rationnelles. La preuve de la première ligne : avec y = x^r, ln y = r ln x, donc (ln x)/x^r = (1/r)(ln y)/y → 0.

::: propriete
**Théorème — limites usuelles** — « Soit r un rationnel strictement positif. lim_{x→+∞} ln x / x^r = 0 ; lim_{x→0⁺} x^r ln x = 0 ; lim_{x→+∞} e^x / x^r = +∞. »
Hiérarchie en +∞, du plus lent au plus rapide : **ln x ≪ x^r ≪ e^x**.
:::

::: exemple Croissances comparées avec des exposants rationnels

1. lim_{x→+∞} (x^(1/3) − x^(2/3)). On factorise : x^(2/3)(x^(−1/3) − 1). Le facteur x^(−1/3) − 1 tend vers −1 et x^(2/3) vers +∞ : la limite vaut **−∞**.
2. lim_{x→0⁺} (x^(2/3) − x^(4/3)) ln x = lim (x^(2/3) ln x − x^(4/3) ln x). Chaque terme est de la forme x^r ln x avec r > 0, donc tend vers 0 : la limite est **0**.
3. lim_{x→+∞} (ln x)/2^x. On écrit 2^x = e^(x ln 2) et (ln x)/2^x = ((ln x)/x) × (x/2^x). Le premier facteur tend vers 0 ; pour le second, avec t = x ln 2, x/2^x = (1/ln 2)(t/e^t) → 0. La limite vaut **0**. Contrôle en x = 100 : (ln 100)/2^100 ≈ 3,6 × 10⁻³⁰ ✓.

:::

::: piege
**Erreur : « x^(r+1) est une primitive de x^r ».** Elle tente parce qu'on pense « on augmente l'exposant de 1 ». Or (x^(r+1))′ = (r + 1)x^r, pas x^r. Avec r = 2 : (x³)′ = 3x² et non x². Il faut le facteur **1/(r + 1)** : une primitive de x² est x³/3. Et la formule tombe en défaut pour r = −1, où le facteur serait 1/0 : la primitive de 1/x est ln x.
:::

::: verifie À toi : une forme +∞ − ∞
Calculer lim_{x→+∞} (√x − ln x).

---

La forme est ∞ − ∞. On factorise par √x = x^(1/2) : √x − ln x = √x(1 − (ln x)/√x). Par le théorème (r = 1/2), (ln x)/√x → 0, donc la parenthèse tend vers 1 et le produit vers +∞ : la limite vaut +∞.
:::

::: retenir
x^r = e^(r ln x) pour x > 0 et r rationnel, (x^r)′ = r x^(r−1), primitive x^(r+1)/(r + 1) pour r ≠ −1, ⁿ√x = x^(1/n) ; ln x ≪ x^r ≪ e^x en +∞, et x^r ln x → 0 en 0⁺.
:::

## 🎯 Le scénario du bac : étude à exponentielle et suite récurrente

Un problème de bac enchaîne presque toujours les mêmes étapes : étudier une fonction, la dompter avec une fonction auxiliaire, puis l'utiliser pour une aire ou pour une suite.
Quels outils des sept notions précédentes servent à quelle étape ?
Et comment prouver qu'une suite définie par u_{n+1} = φ(u_n) converge vers la solution de φ(x) = x ?

::: methode
**Étude complète** : (1) domaine et limites aux bornes, par croissances comparées ; (2) dérivée par u′e^u, signe de f′ (souvent via une fonction auxiliaire g) ; (3) tableau ; (4) asymptote D : si f(x) − (ax + b) → 0, la position se lit au signe de cet écart ; (5) tracé. **Suite u_{n+1} = φ(u_n)** : (6) montrer que φ(I) ⊂ I, pour que tous les termes restent dans I ; (7) prouver que φ(x) = x a une solution α dans I (théorème des valeurs intermédiaires) ; (8) si |φ′(x)| ≤ k < 1 sur I, l'inégalité des accroissements finis donne |u_{n+1} − α| ≤ k|u_n − α|, donc |u_n − α| ≤ kⁿ|u₀ − α| → 0.
:::

::: exemple Étude de f(x) = x − 2 + e^(−x/2), asymptote et aire

1. **Dérivée.** f′(x) = 1 − ½e^(−x/2). Elle s'annule quand e^(−x/2) = 2, soit −x/2 = ln 2 et x = −2 ln 2. Comme e^(−x/2) décroît, f′ < 0 avant et f′ > 0 après : f décroît sur ]−∞ ; −2 ln 2] puis croît, avec un minimum f(−2 ln 2) = −2 ln 2 − 2 + 2 = **−2 ln 2 ≈ −1,386**.
2. **Asymptote.** f(x) − (x − 2) = e^(−x/2) → 0 en +∞ : la droite D : y = x − 2 est asymptote oblique, et comme e^(−x/2) > 0, C est **au-dessus** de D.
3. **Aire.** Pour λ > 0, l'aire entre C, D, l'axe des ordonnées et la droite x = λ vaut ∫₀^λ e^(−x/2) dx = [−2e^(−x/2)]₀^λ = 2(1 − e^(−λ/2)), qui tend vers **2 u.a** quand λ → +∞. Contrôle en λ = 4 : 2(1 − e^(−2)) ≈ 1,729, inférieur à 2 ✓.

:::

::: exemple Une suite récurrente : u₀ = 0 et u_{n+1} = h(u_n), avec h(x) = 1 − ½e^x sur I = [0 ; 0,5]

1. **Stabilité.** h′(x) = −½e^x < 0 : h décroît. Avec h(0) = 0,5 et h(0,5) = 1 − ½√e ≈ 0,1756, on a h(I) = [0,1756 ; 0,5] ⊂ I : tous les u_n restent dans I.
2. **Le point fixe.** h(x) = x équivaut à g(x) = 1 − x − ½e^x = 0. g′(x) = −1 − ½e^x < 0, g(0) = 0,5 > 0 et g(0,5) ≈ −0,324 < 0 : par le théorème des valeurs intermédiaires, g s'annule **une seule fois**, en α ≈ 0,315, dans I.
3. **Contraction.** Sur I, |h′(x)| = ½e^x ≤ ½e^(0,5) ≈ 0,824 ≤ 0,83. L'inégalité des accroissements finis donne |u_{n+1} − α| ≤ 0,83|u_n − α|, donc |u_n − α| ≤ 0,83ⁿ × 0,5 → 0 : la suite converge vers α.
4. **Contrôle numérique.** u₁ = 0,5 ; u₂ ≈ 0,1756 ; u₃ ≈ 0,4040 ; u₄ ≈ 0,2511 ; u₅ ≈ 0,3573 ; u₆ ≈ 0,2853 : les termes alternent de part et d'autre de α ≈ 0,315, et |u₆ − α| ≈ 0,03 ≤ 0,83⁶ × 0,5 ≈ 0,163 ✓.

:::

::: figure L'« escalier » de la suite : la courbe C de h (verte, décroissante) coupe la droite y = x en α ; les termes u₁, u₂, u₃, … tournent autour de α en s'en rapprochant.
<svg viewBox="0 0 340 270">
<title>Escalier de la suite définie par u₀ = 0 et u(n+1) = h(u(n)), avec h(x) = 1 − (1/2)eˣ : les termes alternent de part et d'autre de α, abscisse du point où la courbe de φ coupe la droite y = x, et s'en rapprochent</title>
<line x1="10" y1="245" x2="330" y2="245" stroke="#0f172a" stroke-width="1.6"/><line x1="45" y1="256" x2="45" y2="12" stroke="#0f172a" stroke-width="1.6"/><polygon points="330,245 322,241 322,249" fill="#0f172a"/><polygon points="45,12 41,20 49,20" fill="#0f172a"/><line x1="45.0" y1="245.0" x2="285.0" y2="5.0" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><polyline points="45.0,45.0 48.1,46.6 51.2,48.1 54.3,49.7 57.4,51.3 60.5,52.9 63.6,54.5 66.7,56.1 69.8,57.8 72.9,59.4 76.0,61.1 79.1,62.8 82.2,64.5 85.3,66.2 88.4,67.9 91.5,69.7 94.6,71.4 97.7,73.2 100.8,74.9 103.9,76.7 107.0,78.5 110.1,80.3 113.2,82.2 116.3,84.0 119.4,85.9 122.5,87.8 125.6,89.6 128.7,91.6 131.8,93.5 134.9,95.4 138.0,97.4 141.1,99.3 144.2,101.3 147.3,103.3 150.4,105.3 153.5,107.3 156.6,109.4 159.7,111.4 162.8,113.5 165.9,115.6 169.0,117.7 172.1,119.8 175.2,121.9 178.3,124.1 181.4,126.3 184.5,128.5 187.6,130.7 190.7,132.9 193.8,135.1 196.9,137.4 200.0,139.7 203.1,142.0 206.2,144.3 209.3,146.6 212.4,148.9 215.5,151.3 218.6,153.7 221.7,156.1 224.8,158.5 227.9,160.9 231.0,163.4 234.1,165.9 237.2,168.4 240.3,170.9 243.4,173.4 246.5,176.0 249.6,178.6 252.7,181.2 255.8,183.8 258.9,186.4 262.0,189.1 265.1,191.7 268.2,194.4 271.3,197.2 274.4,199.9 277.5,202.7 280.6,205.4 283.7,208.2 286.8,211.1 289.9,213.9 293.0,216.8" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="45.0,245.0 45.0,45.0 245.0,45.0 245.0,174.7 115.3,174.7 115.3,83.4 206.6,83.4 206.6,144.6 145.4,144.6" fill="none" stroke="#b45309" stroke-width="1.8"/><line x1="171.0" y1="119.0" x2="171.0" y2="245.0" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><circle cx="171.0" cy="119.0" r="4" fill="#0f172a"/>
<g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="39.0" y="259.0" text-anchor="end" fill="#0f172a">O</text><text x="281.0" y="21.0" text-anchor="end" fill="#94a3b8">y = x</text><text x="284.0" y="198.0" text-anchor="start" fill="#0f6e56">C</text><text x="245.0" y="261.0" text-anchor="middle" fill="#0f172a">u₁</text><text x="115.3" y="261.0" text-anchor="middle" fill="#0f172a">u₂</text><text x="174.0" y="261.0" text-anchor="middle" fill="#0f172a">α</text><text x="206.6" y="261.0" text-anchor="middle" fill="#0f172a">u₃</text></g></svg>
:::

::: exemple Une aire non bornée en apparence : F(X) = ∫₀^X e^(−x²) dx

1. **Croissance.** L'intégrande est > 0, donc F est strictement croissante sur [0, +∞[.
2. **Majoration.** Pour x ≥ 1, x² ≥ x, donc e^(−x²) ≤ e^(−x). Alors F(X) ≤ ∫₀¹ e^(−x²) dx + ∫₁^X e^(−x) dx. Or ∫₀¹ e^(−x²) dx ≤ 1 et ∫₁^X e^(−x) dx = e^(−1) − e^(−X) ≤ e^(−1) : F(X) ≤ 1 + e^(−1) ≈ 1,368.
3. **Minoration.** Sur [0, 1], e^(−x²) ≥ e^(−1), donc F(X) ≥ ∫₀¹ e^(−x²) dx ≥ e^(−1) ≈ 0,368.
4. **Conclusion.** F est croissante et majorée : elle a une limite finie L, avec e^(−1) ≤ L ≤ 1 + e^(−1), sans que l'on sache calculer F(X) — car x ↦ e^(−x²) n'est pas de la forme u′e^u et n'a pas de primitive exprimable avec les fonctions usuelles.

:::

::: piege
**Erreur : conclure à la convergence parce que φ(α) = α.** Prenons φ(x) = 1 − 2e^x et u₀ = 0. L'équation φ(x) = x a bien une solution α ≈ −0,375. Pourtant u₁ = −1, u₂ ≈ 0,264, u₃ ≈ −1,605, u₄ ≈ 0,598, u₅ ≈ −2,638 : la suite s'**éloigne** de α. La raison : |φ′(α)| = 2e^α ≈ 1,37 > 1. Avoir un point fixe ne suffit pas ; il faut encore un intervalle I stable avec |φ′| ≤ k < 1.
:::

::: verifie À toi : asymptote et position
Pour f(x) = 2x − 1 + e^(−x), montrer que la droite D : y = 2x − 1 est asymptote en +∞ et donner la position de C par rapport à D.

---

f(x) − (2x − 1) = e^(−x), qui tend vers 0 en +∞ : D est asymptote oblique. Comme e^(−x) > 0 pour tout réel x, cet écart est toujours positif : C est au-dessus de D sur ℝ tout entier. En −∞, au contraire, e^(−x) → +∞ et la courbe s'éloigne de D.
:::

::: retenir
Une étude à exponentielle enchaîne limites par croissances comparées, dérivée par u′e^u, fonction auxiliaire pour le signe, asymptote et position par le signe de f moins la droite ; une suite u_{n+1} = φ(u_n) converge vers α si I est stable et |φ′| ≤ k < 1 sur I.
:::

> 🏆 Neuvième porte franchie, héros : tu as retourné ln pour en tirer exp, tu sais qu'elle est sa propre dérivée, qu'elle écrase toute puissance en +∞, qu'elle se dérive et se primitive en e^u, et qu'elle donne un sens à a^b comme à x^r. Il te reste une marche : au chapitre suivant, les équations différentielles feront de l'exponentielle la clé de toutes les évolutions.
