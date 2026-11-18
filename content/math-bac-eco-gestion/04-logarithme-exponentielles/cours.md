# ⚔️ Logarithme et exponentielles — croissance, intérêts, optimisation

> 💡 «Le logarithme transforme les produits en sommes ; l'exponentielle fait le chemin inverse : à elles deux, elles décrivent tout ce qui croît par pourcentages.»

Bienvenue, héros de l'Économie et gestion. Un capital qui gonfle de 4 % par an, un trafic qui se multiplie chaque mois, un bénéfice qui culmine avant de retomber : ces situations ne se résolvent ni avec des polynômes ni avec des fractions. Huit étapes te donnent les deux fonctions qui les traitent : le logarithme népérien ln et l'exponentielle eˣ, leurs propriétés, leurs limites, leurs dérivées, puis la fonction x ↦ aˣ, les intérêts composés et l'optimisation d'un bénéfice ou d'un coût. On suppose acquis les limites, la dérivation et l'étude de fonctions (chapitres 1 à 3).

## 🧱 Le logarithme népérien : la primitive de 1/x

Une brasserie estime que son coût marginal, pour une production de x hectolitres (x > 0), est 1/x millier de dinars par hectolitre : ce coût marginal baisse quand on produit plus.
Quelle fonction donne le coût total, c'est-à-dire quelle fonction a pour dérivée 1/x ? Aucune puissance de x ne convient : la dérivée de xⁿ est n xⁿ⁻¹, et jamais 1/x.

::: definition
La fonction x ↦ 1/x est continue sur ]0 ; +∞[, donc elle admet des primitives. La **fonction logarithme népérien**, notée **ln**, est la primitive de x ↦ 1/x sur ]0 ; +∞[ qui s'annule en 1.

- ln est définie sur ]0 ; +∞[ et ln(1) = 0.
- ln est dérivable et (ln)′(x) = 1/x ; comme 1/x > 0, ln est strictement croissante.
- Pour x > 0 et y > 0 : ln x = ln y ⟺ x = y, et ln x < ln y ⟺ x < y.
- ln x < 0 ⟺ 0 < x < 1, et ln x > 0 ⟺ x > 1.
:::

::: propriete
Si u est dérivable sur un intervalle I et ne s'annule pas sur I, la fonction ln|u| est dérivable et sa dérivée est u′/u : réciproquement, une primitive de u′/u est ln|u|.
:::

::: exemple Domaine, dérivée et primitive avec ln
1. Le domaine de f(x) = ln(5 − 2x) est l'ensemble des x tels que 5 − 2x > 0, c'est-à-dire x < 5/2 : ]−∞ ; 5/2[. La borne 5/2 est exclue, car ln(0) n'existe pas.
2. Soit g(x) = ln((x + 3)/(x − 1)). Le quotient est strictement positif quand numérateur et dénominateur ont le même signe : x < −3 ou x > 1. Le domaine est ]−∞ ; −3[ ∪ ]1 ; +∞[.
3. Soit h(x) = ln(x² + 4x + 7). Le discriminant de x² + 4x + 7 vaut 16 − 28 = −12 < 0, donc l'expression est toujours positive et h est définie sur ℝ. Avec u(x) = x² + 4x + 7, on a h′(x) = u′(x)/u(x) = (2x + 4)/(x² + 4x + 7).
4. Lue à l'envers, cette dérivée donne une primitive : une primitive de (2x + 4)/(x² + 4x + 7) sur ℝ est ln(x² + 4x + 7). Contrôle : au numérateur on retrouve bien la dérivée du dénominateur.
5. Pour la brasserie, le coût marginal est 1/x, donc le coût total est de la forme ln x + C₀, où C₀ = C(1) est le coût du premier hectolitre. Avec C₀ = 4, produire 10 hectolitres coûte ln 10 + 4 ≈ 2,303 + 4 = 6,30 milliers de dinars.

:::

::: piege Remplacer ln((x + 3)/(x − 1)) par ln(x + 3) − ln(x − 1) sans changer le domaine
Pour g(x) = ln((x + 3)/(x − 1)), on écrit « g(x) = ln(x + 3) − ln(x − 1), donc le domaine est ]1 ; +∞[ ». Cela tente parce que la différence de logarithmes est la règle du cours. Mais cette règle exige que x + 3 et x − 1 soient tous deux positifs. Test : g(−5) = ln((−2)/(−6)) = ln(1/3) existe, alors que ln(−2) n'existe pas. Le domaine de g est plus grand que celui de la différence.
:::

::: propriete
- Pour trouver le domaine de ln(u(x)), on résout u(x) > 0, avec une inégalité stricte.
- Pour résoudre une équation ou une inéquation avec ln, on fixe le domaine d'abord, puis on utilise la stricte croissance de ln.
- Une primitive de u′/u s'écrit ln|u| ; quand u > 0 sur I, on peut écrire ln(u) sans la valeur absolue.

Cas limite : f(x) = ln|x| est définie pour tout x ≠ 0, et sa dérivée 1/x est la même sur ]−∞ ; 0[ que sur ]0 ; +∞[ ; pourtant ln|x| n'est pas définie en 0.
:::

::: verifie
Déterminer le domaine de g(x) = ln(4 − x²) puis calculer g′(x).

---

On résout 4 − x² > 0, soit x² < 4, donc −2 < x < 2 : le domaine est ]−2 ; 2[. Avec u(x) = 4 − x², u′(x) = −2x, donc g′(x) = −2x/(4 − x²). On vérifie le signe : g′ est positive pour x < 0 et négative pour x > 0, ce qui est cohérent avec une courbe qui culmine en 0, où g(0) = ln 4.
:::

::: retenir
ln est la primitive de 1/x qui s'annule en 1 : définie sur ]0 ; +∞[, strictement croissante, de dérivée 1/x, avec ln 1 = 0 ; ln(u) exige u > 0, la dérivée de ln|u| est u′/u et une primitive de u′/u est ln|u|.
:::

## ➕ Les propriétés du logarithme : produit, quotient, puissance

Une confiserie sait que ln 2 ≈ 0,693 et ln 3 ≈ 1,099 (valeurs arrondies). Elle veut estimer ln 12, sans calculatrice, pour comparer deux plans de croissance.
Comment passer de ln 2 et ln 3 à ln 12 ?

::: definition
Pour tous réels a > 0 et b > 0 :

- ln(ab) = ln a + ln b (**propriété fondamentale**) ;
- ln(1/a) = −ln a et ln(a/b) = ln a − ln b ;
- ln(√a) = (1/2) ln a ;
- ln(aⁿ) = n ln a, pour tout entier relatif n.
:::

La propriété fondamentale se démontre ainsi : pour a > 0 fixé, les fonctions x ↦ ln(ax) et x ↦ ln x + ln a ont la même dérivée 1/x, et elles valent toutes deux ln a en x = 1 ; elles sont donc égales.

::: exemple Estimer ln 12, puis résoudre une équation et une inéquation
1. On factorise : 12 = 2² × 3. Alors ln 12 = 2 ln 2 + ln 3 ≈ 2 × 0,693 + 1,099 = 2,485. Contrôle : 2,485 est très proche de la valeur donnée par la calculatrice, ln 12 ≈ 2,4849.
2. Résolvons ln x + ln(x + 2) = ln 15. Le domaine est x > 0, car il faut x > 0 et x + 2 > 0. On regroupe : ln(x(x + 2)) = ln 15, donc x(x + 2) = 15, soit x² + 2x − 15 = 0. Les solutions sont x = 3 et x = −5. Seule x = 3 est dans le domaine : S = {3}.
3. Résolvons ln(3x − 1) ≤ ln(x + 5). Le domaine exige 3x − 1 > 0 et x + 5 > 0, donc x > 1/3. Comme ln est croissante, l'inéquation équivaut à 3x − 1 ≤ x + 5, soit x ≤ 3. L'ensemble des solutions est ]1/3 ; 3].

:::

::: piege Écrire ln(a + b) = ln a + ln b
Pour calculer ln 5 + ln 3, on écrit « ln 5 + ln 3 = ln(5 + 3) = ln 8 ». Cela tente parce que le signe + est déjà là. Mais la somme de deux logarithmes devient le logarithme d'un produit : ln 5 + ln 3 = ln 15. Test : ln 15 ≈ 2,708, alors que ln 8 ≈ 2,079 ; et 1,609 + 1,099 = 2,708 confirme ln 15.
:::

::: propriete
- Le logarithme transforme un produit en somme, un quotient en différence et une puissance en multiple ; il ne dit rien de ln(a + b).
- Dans une équation, on regroupe les ln en un seul, puis on utilise l'injectivité ; on rejette toute solution hors du domaine.
- Dans une inéquation, on garde le sens de l'inégalité, car ln est croissante.

Cas limite : ln(x²) = 2 ln|x| pour tout x ≠ 0 ; l'écriture 2 ln x n'a de sens que pour x > 0, et le domaine des deux membres n'est pas le même.
:::

::: verifie
Résoudre dans ℝ l'équation ln x + ln(x − 3) = ln 4.

---

Le domaine exige x > 0 et x − 3 > 0, donc x > 3. On regroupe : x(x − 3) = 4, soit x² − 3x − 4 = 0, de racines x = 4 et x = −1. Seule x = 4 est dans le domaine. Contrôle : ln 4 + ln 1 = ln 4 + 0 = ln 4.
:::

::: retenir
ln(ab) = ln a + ln b, ln(a/b) = ln a − ln b, ln(1/a) = −ln a, ln(aⁿ) = n ln a, mais ln(a + b) n'est pas ln a + ln b ; on fixe le domaine avant de regrouper, et on rejette les solutions hors du domaine.
:::

## 📈 Limites et variations de ln : le nombre e

Une chaîne de boutiques constate que chaque nouvelle ouverture rapporte moins que la précédente : le chiffre d'affaires cumulé suit une courbe qui monte toujours, mais de plus en plus lentement.
Jusqu'où monte ln, et à quelle vitesse, comparée à x ?

::: definition
ln est une bijection de ]0 ; +∞[ sur ℝ ; l'unique réel dont le logarithme vaut 1 est noté **e**, avec e ≈ 2,718.
:::

::: propriete
- lim ln x = +∞ quand x tend vers +∞, et lim ln x = −∞ quand x tend vers 0 par valeurs positives.
- **Croissances comparées** : lim (ln x)/x = 0 quand x tend vers +∞, et lim x ln x = 0 quand x tend vers 0⁺ ; plus généralement (ln x)/xⁿ tend vers 0 en +∞ et xⁿ ln x tend vers 0 en 0⁺ (n entier, n ≥ 1).
- lim ln(1 + x)/x = 1 quand x tend vers 0, et de même lim (ln x)/(x − 1) = 1 quand x tend vers 1 : c'est le nombre dérivé de ln en 1.
:::

| x | 0 | | 1 | | e | | +∞ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ln x | −∞ | ↗ | 0 | ↗ | 1 | ↗ | +∞ |

La courbe de ln admet l'axe des ordonnées pour asymptote verticale et, en +∞, une branche parabolique de direction l'axe des abscisses, puisque (ln x)/x tend vers 0. Sa tangente au point d'abscisse 1 a pour équation y = x − 1, car ln 1 = 0 et (ln)′(1) = 1.

::: figure La courbe de ln monte sans fin mais de plus en plus lentement ; elle passe par (1 ; 0) et (e ; 1), colle à l'axe des ordonnées près de 0 et a pour tangente en 1 la droite y = x − 1
<svg viewBox="0 0 340 228"><title>Courbe de ln : elle passe par (1 ; 0) et (e ; 1), admet l'axe des ordonnées pour asymptote verticale et la droite y = x − 1 pour tangente en 1</title><line x1="20" y1="100" x2="330" y2="100" stroke="#0f172a" stroke-width="1.6"/><line x1="56" y1="222" x2="56" y2="8" stroke="#0f172a" stroke-width="1.6"/><polygon points="330,100 323,96.5 323,103.5" fill="#0f172a"/><polygon points="56,8 52.5,15 59.5,15" fill="#0f172a"/><text x="322" y="94" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="64" y="18" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="100" y1="97" x2="100" y2="103" stroke="#0f172a" stroke-width="1.3"/><text x="100" y="115" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="175.604" y1="97" x2="175.604" y2="103" stroke="#0f172a" stroke-width="1.3"/><text x="175.604" y="115" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">e</text><line x1="53" y1="60" x2="59" y2="60" stroke="#0f172a" stroke-width="1.3"/><text x="50" y="64" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="56" y1="60" x2="175.604" y2="60" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><line x1="175.604" y1="100" x2="175.604" y2="60" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><polyline points="58.2,138.0 196.8,12.0" fill="none" stroke="#b45309" stroke-width="2.0" stroke-dasharray="5 3" stroke-linejoin="round" stroke-linecap="round"/><polyline points="59.1,206.4 60.0,196.3 60.8,188.3 61.7,181.6 62.6,175.9 63.5,170.9 64.4,166.4 65.2,162.4 66.1,158.8 67.0,155.5 69.2,148.2 73.6,136.7 78.0,127.7 82.4,120.4 86.8,114.3 91.2,108.9 95.6,104.2 100.0,100.0 104.4,96.2 108.8,92.7 113.2,89.5 117.6,86.5 122.0,83.8 126.4,81.2 130.8,78.8 135.2,76.5 139.6,74.3 144.0,72.3 148.4,70.3 152.8,68.5 157.2,66.7 161.6,65.0 166.0,63.3 170.4,61.8 174.8,60.3 179.2,58.8 183.6,57.4 188.0,56.1 192.4,54.7 196.8,53.5 201.2,52.2 205.6,51.0 210.0,49.9 214.4,48.8 218.8,47.7 223.2,46.6 227.6,45.6 232.0,44.5 236.4,43.6 240.8,42.6 245.2,41.7 249.6,40.7 254.0,39.8 258.4,39.0 262.8,38.1 267.2,37.3 271.6,36.4 276.0,35.6 280.4,34.8 284.8,34.1 289.2,33.3 293.6,32.5 298.0,31.8 302.4,31.1 306.8,30.4 311.2,29.7 315.6,29.0 320.0,28.3" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="100.0" cy="100.0" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="175.6" cy="60.0" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="266" y="26" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = ln x</text><text x="204.8" y="16" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = x − 1</text><text x="62" y="214" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">asymptote : x = 0</text></svg>
:::

::: exemple Étudier f(x) = x − 3 ln x sur ]0 ; +∞[
1. En 0⁺, x tend vers 0 et ln x vers −∞, donc −3 ln x tend vers +∞ : f(x) tend vers +∞. La droite x = 0 est asymptote verticale.
2. En +∞, on factorise : f(x) = x(1 − 3(ln x)/x). Comme (ln x)/x tend vers 0, la parenthèse tend vers 1 et f(x) tend vers +∞. Le quotient f(x)/x tend vers 1, et f(x) − x = −3 ln x tend vers −∞ : branche parabolique de direction la droite y = x.
3. La dérivée est f′(x) = 1 − 3/x = (x − 3)/x. Elle est négative sur ]0 ; 3[ et positive sur ]3 ; +∞[.
4. Le minimum vaut f(3) = 3 − 3 ln 3 ≈ 3 − 3,296 = −0,296 : la courbe passe un peu sous l'axe des abscisses.

| x | 0 | | 3 | | +∞ |
| --- | --- | --- | --- | --- | --- |
| f′(x) | | − | 0 | + | |
| f(x) | +∞ | ↘ | 3 − 3 ln 3 | ↗ | +∞ |

:::

::: piege Conclure que (ln x)/x tend vers +∞ parce que ln x tend vers +∞
Pour la limite de (ln x)/x en +∞, on écrit « le numérateur tend vers +∞, donc le quotient aussi ». Cela tente parce qu'un numérateur qui grandit fait grandir une fraction. Mais le dénominateur grandit aussi, et plus vite. Test : pour x = 1 000, (ln x)/x = 6,91/1 000 ≈ 0,007 ; pour x = 1 000 000, on trouve 13,8/1 000 000 ≈ 0,000014. Le quotient tend vers 0.
:::

::: propriete
- En +∞, ln x croît moins vite que toute puissance de x : on factorise par la puissance dominante, comme f(x) = x(1 − 3(ln x)/x) dans l'exemple, pour lever l'indétermination.
- En 0⁺, xⁿ ln x tend vers 0 : la puissance de x l'emporte sur la croissance infinie de ln.
- La courbe de ln n'a ni asymptote horizontale ni oblique, malgré sa croissance de plus en plus lente.

Cas limite : ln x tend bien vers +∞, mais très lentement : il faut x = e^(100), un nombre de 44 chiffres, pour atteindre ln x = 100.
:::

::: verifie
Calculer les limites de g(x) = x − 2 + ln x en 0⁺ et en +∞.

---

En 0⁺, x − 2 tend vers −2 et ln x vers −∞, donc g(x) tend vers −∞. En +∞, x − 2 tend vers +∞ et ln x aussi, donc g(x) tend vers +∞ : il n'y a pas d'indétermination, car les deux termes vont dans le même sens. Comme g′(x) = 1 + 1/x > 0, g est croissante de −∞ à +∞ : elle s'annule une seule fois.
:::

::: retenir
ln tend vers +∞ en +∞ et vers −∞ en 0⁺ ; les croissances comparées (ln x)/x → 0 et x ln x → 0 sont les deux limites à connaître ; ln est une bijection de ]0 ; +∞[ sur ℝ, et e ≈ 2,718 est le réel de logarithme 1.
:::

## 🔄 La fonction exponentielle : la réciproque de ln

Pour la brasserie de la première étape, le coût total (en milliers de dinars, au-dessus du coût du premier hectolitre) d'une production de x hectolitres est y = ln x. Comme ln est une bijection de ]0 ; +∞[ sur ℝ, à chaque niveau y de coût correspond une unique production x > 0, telle que ln x = y.
Comment noter et manier la fonction qui, à y, associe ce x ?

::: definition
La **fonction exponentielle**, notée **exp**, est la fonction réciproque de ln. Pour tout entier relatif n, ln(eⁿ) = n, d'où la notation exp(x) = **eˣ** pour tout réel x.

- eˣ est défini sur ℝ et eˣ > 0 pour tout x ; e⁰ = 1.
- Pour x > 0 et y réel : ln x = y ⟺ x = eʸ ; ln(eˣ) = x pour tout réel x ; e^(ln x) = x pour tout x > 0.
- eˣ = eʸ ⟺ x = y, et eˣ < eʸ ⟺ x < y (exp est strictement croissante).
- e^(a + b) = eᵃ × eᵇ, e^(−a) = 1/eᵃ, e^(a − b) = eᵃ/eᵇ, e^(na) = (eᵃ)ⁿ.
:::

Comme exp est la réciproque de ln, le point (a ; b) est sur la courbe de ln si et seulement si le point (b ; a) est sur celle de exp : les deux courbes sont symétriques par rapport à la droite d'équation y = x.

::: figure Les courbes de eˣ et de ln x sont symétriques par rapport à la droite y = x : le point (0 ; 1) de l'une correspond au point (1 ; 0) de l'autre
<svg viewBox="0 0 250 256"><title>Les courbes de eˣ et de ln x sont symétriques par rapport à la droite y = x : (0 ; 1) sur l'une correspond à (1 ; 0) sur l'autre</title><line x1="8" y1="150" x2="236" y2="150" stroke="#0f172a" stroke-width="1.6"/><line x1="100" y1="248" x2="100" y2="14" stroke="#0f172a" stroke-width="1.6"/><polygon points="236,150 229,146.5 229,153.5" fill="#0f172a"/><polygon points="100,14 96.5,21 103.5,21" fill="#0f172a"/><text x="228" y="144" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="108" y="24" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><polyline points="4.0,246.0 226.4,23.6" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 3" stroke-linejoin="round" stroke-linecap="round"/><line x1="132" y1="147" x2="132" y2="153" stroke="#0f172a" stroke-width="1.3"/><text x="132" y="165" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="97" y1="118" x2="103" y2="118" stroke="#0f172a" stroke-width="1.3"/><text x="94" y="122" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><polyline points="4.0,148.4 7.2,148.2 10.4,148.1 13.6,147.8 16.8,147.6 20.0,147.4 23.2,147.1 26.4,146.8 29.6,146.5 32.8,146.1 36.0,145.7 39.2,145.2 42.4,144.7 45.6,144.2 48.8,143.5 52.0,142.9 55.2,142.1 58.4,141.3 61.6,140.4 64.8,139.3 68.0,138.2 71.2,137.0 74.4,135.6 77.6,134.1 80.8,132.4 84.0,130.6 87.2,128.5 90.4,126.3 93.6,123.8 96.8,121.0 100.0,118.0 103.2,114.6 106.4,110.9 109.6,106.8 112.8,102.3 116.0,97.2 119.2,91.7 122.4,85.6 125.6,78.8 128.8,71.3 132.0,63.0 135.2,53.9 138.4,43.8 141.6,32.6 144.8,20.2 143.6,25.2" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="101.6,246.0 101.8,242.8 101.9,239.6 102.2,236.4 102.4,233.2 102.6,230.0 102.9,226.8 103.2,223.6 103.5,220.4 103.9,217.2 104.3,214.0 104.8,210.8 105.3,207.6 105.8,204.4 106.5,201.2 107.1,198.0 107.9,194.8 108.7,191.6 109.6,188.4 110.7,185.2 111.8,182.0 113.0,178.8 114.4,175.6 115.9,172.4 117.6,169.2 119.4,166.0 121.5,162.8 123.7,159.6 126.2,156.4 129.0,153.2 132.0,150.0 135.4,146.8 139.1,143.6 143.2,140.4 147.7,137.2 152.8,134.0 158.3,130.8 164.4,127.6 171.2,124.4 178.7,121.2 187.0,118.0 196.1,114.8 206.2,111.6 217.4,108.4 229.8,105.2 224.8,106.4" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="100.0" cy="118.0" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="132.0" cy="150.0" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="34" y="138.8" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = eˣ</text><text x="220.8" y="101.04" text-anchor="end" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = ln x</text><text x="64.8" y="204.4" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = x</text></svg>
:::

::: exemple Équations et inéquation avec l'exponentielle
1. Pour e^(2x + 1) = e⁵, on utilise l'injectivité : 2x + 1 = 5, donc x = 2.
2. Pour eˣ = 3, on prend le logarithme : x = ln 3 ≈ 1,099. Contrôle : e^(1,099) est voisin de 3.
3. Pour e^(2x) − 5eˣ + 6 = 0, on pose X = eˣ, avec X > 0 : X² − 5X + 6 = 0 a pour racines X = 2 et X = 3, toutes deux positives. Donc eˣ = 2 ou eˣ = 3, soit S = {ln 2 ; ln 3}.
4. Pour e^(2x) + eˣ − 6 = 0, le même changement donne X² + X − 6 = 0, de racines X = 2 et X = −3. La racine X = −3 est impossible, car eˣ > 0 : seule eˣ = 2 reste, donc S = {ln 2}.
5. Pour la brasserie, un coût y = 3 correspond à ln x = 3, donc x = e³ ≈ 20,09 hectolitres.
6. Pour e^(2x) − 3eˣ + 2 ≤ 0, on pose X = eˣ : X² − 3X + 2 ≤ 0, de racines X = 1 et X = 2. Le trinôme est négatif entre ses racines, donc 1 ≤ eˣ ≤ 2. Comme exp est croissante, on revient à x par ln : 0 ≤ x ≤ ln 2, soit S = [0 ; ln 2].

:::

::: piege Résoudre eˣ = −3 en écrivant x = ln(−3)
Dans l'équation de l'exemple 4, on garde la racine X = −3 et on écrit « eˣ = −3, donc x = ln(−3) ». Cela tente parce que ln est l'outil qui résout les équations en eˣ. Mais ln(−3) n'existe pas, et eˣ est toujours strictement positif : l'équation eˣ = −3 n'a aucune solution. Test : eˣ vaut 0,05 pour x = −3 et 20 pour x = 3, jamais un nombre négatif.
:::

::: propriete
- exp et ln se défont l'une l'autre : ln(eˣ) = x pour tout réel x, mais e^(ln x) = x seulement pour x > 0.
- Pour résoudre une équation du second degré en eˣ, on pose X = eˣ, on résout en X, et on ne garde que les racines X > 0.
- L'équation eˣ = k n'a de solution que pour k > 0, et vaut alors ln k.

Cas limite : e^(ln x) n'existe pas pour x ≤ 0 : on ne simplifie e^(ln(x − 2)) en x − 2 que si x > 2.
:::

::: verifie
Résoudre dans ℝ l'équation e^(3x − 2) = 5.

---

On prend le logarithme des deux membres : 3x − 2 = ln 5, donc x = (2 + ln 5)/3. Valeur approchée : ln 5 ≈ 1,609, donc x ≈ 1,203. Contrôle : 3 × 1,203 − 2 = 1,609 = ln 5 ✓.
:::

::: retenir
exp est la réciproque de ln : eˣ > 0, ln(eˣ) = x pour tout réel x, e^(ln x) = x pour x > 0 ; e^(a + b) = eᵃ eᵇ ; pour une équation du second degré en eˣ, on pose X = eˣ et on garde seulement les racines positives.
:::

## ⚙️ Dérivée et limites de eˣ

Un fabricant de pièces mécaniques modélise la demande de son produit par D(p) = 400 e^(−0,05p), où p est le prix en dinars : la demande s'effondre quand le prix monte.
À quelle vitesse varie cette demande, et que devient-elle pour un prix très élevé ?

::: definition
- exp est dérivable sur ℝ et (eˣ)′ = eˣ ; si u est dérivable sur I, la fonction e^u est dérivable et (e^u)′ = u′ e^u.
- Une primitive de u′ e^u est e^u.
- lim eˣ = +∞ en +∞, lim eˣ = 0 en −∞.
- **Croissances comparées** : lim eˣ/x = +∞ en +∞ (et eˣ/xⁿ aussi) ; lim x eˣ = 0 en −∞ (et xⁿ eˣ aussi).
- lim (eˣ − 1)/x = 1 quand x tend vers 0.
:::

::: exemple Dérivée, limite et primitive avec eˣ
1. Pour D(p) = 400 e^(−0,05p), u(p) = −0,05p et u′ = −0,05, donc D′(p) = −0,05 × 400 e^(−0,05p) = −20 e^(−0,05p) < 0 : la demande décroît. D(p) tend vers 0 quand p tend vers +∞ : la droite y = 0 est asymptote horizontale.
2. Soit f(x) = x e^(−x). On écrit f(x) = x/eˣ : en +∞, eˣ/x tend vers +∞, donc f(x) tend vers 0. Sa dérivée est f′(x) = e^(−x) − x e^(−x) = (1 − x) e^(−x), positive avant 1 et négative après : le maximum vaut f(1) = 1/e ≈ 0,368.
3. Soit g(x) = e^(3x² − 6x). Avec u(x) = 3x² − 6x, u′(x) = 6x − 6, donc g′(x) = (6x − 6) e^(3x² − 6x). Elle s'annule en x = 1, où g(1) = e^(−3) ≈ 0,050 : c'est le minimum de g.
4. Pour la primitive de 6x e^(x²) sur ℝ : avec u(x) = x², u′(x) = 2x, donc 6x e^(x²) = 3 × u′ e^u, et une primitive est 3 e^(x²). Contrôle : (3 e^(x²))′ = 3 × 2x e^(x²) = 6x e^(x²) ✓.

:::

::: piege Oublier u′ dans la dérivée de e^u
Pour (e^(2x))′, on écrit « la dérivée de eˣ est eˣ, donc (e^(2x))′ = e^(2x) ». Cela tente parce que l'exponentielle est égale à sa dérivée. Mais l'exposant 2x se dérive aussi : (e^(2x))′ = 2 e^(2x). Test : en x = 0, e^(2x) passe de 1 à 1,2214 quand x passe de 0 à 0,1 : une pente moyenne proche de 2,2, et non de 1.
:::

::: propriete
- Pour dériver e^u, on garde e^u et on multiplie par u′ ; pour trouver une primitive de u′ e^u, on reconnaît la forme et on écrit e^u.
- En +∞, eˣ l'emporte sur toute puissance de x ; en −∞, xⁿ eˣ tend vers 0.
- La courbe de eˣ admet l'axe des abscisses pour asymptote en −∞ et une branche parabolique de direction l'axe des ordonnées en +∞ ; sa tangente au point d'abscisse 0 a pour équation y = x + 1, car e⁰ = 1 et (eˣ)′ vaut 1 en 0.

Cas limite : la limite en −∞ de x eˣ est 0, alors que la limite en +∞ de x eˣ vaut +∞ ; le sens de x décide de la limite.
:::

::: verifie
Calculer f′(x) pour f(x) = x e^(−2x) et préciser où f est maximale.

---

On dérive un produit : f′(x) = e^(−2x) + x × (−2) e^(−2x) = (1 − 2x) e^(−2x). Comme e^(−2x) > 0, le signe de f′ est celui de 1 − 2x : f croît jusqu'à x = 1/2 puis décroît. Le maximum vaut f(1/2) = (1/2) e^(−1) = 1/(2e) ≈ 0,184.
:::

::: retenir
(eˣ)′ = eˣ et (e^u)′ = u′ e^u, d'où une primitive de u′ e^u : e^u ; eˣ l'emporte sur toute puissance de x en +∞, et xⁿ eˣ tend vers 0 en −∞.
:::

## 🔢 La fonction x ↦ aˣ : les croissances par pourcentage

Un site de vente en ligne voit son trafic se multiplier par 1,8 chaque mois : au bout de x mois, le trafic est multiplié par 1,8ˣ.
Comment définir 1,8ˣ pour un x quelconque, et comment résoudre « 1,8ˣ = 10 » ?

::: definition
Pour a > 0, la **fonction exponentielle de base a** est x ↦ aˣ = e^(x ln a), définie sur ℝ.

- aˣ > 0 et ln(aˣ) = x ln a ; si a = 1, alors 1ˣ = 1.
- aˣ⁺ʸ = aˣ × aʸ, a⁻ˣ = 1/aˣ, aˣ⁻ʸ = aˣ/aʸ et (aˣ)ⁿ = aⁿˣ.
- La dérivée est (aˣ)′ = (ln a) aˣ.
- Si a > 1, ln a > 0 : aˣ est strictement croissante, de limite 0 en −∞ et +∞ en +∞. Si 0 < a < 1, ln a < 0 : aˣ est strictement décroissante, de limite +∞ en −∞ et 0 en +∞.
:::

::: exemple Résoudre avec aˣ
1. Trafic multiplié par 10 : 1,8ˣ = 10 équivaut à x ln 1,8 = ln 10, donc x = ln 10/ln 1,8 ≈ 2,303/0,588 = 3,92 mois.
2. Résolvons 2ˣ = 5^(x − 1). On prend le logarithme : x ln 2 = (x − 1) ln 5, donc x(ln 5 − ln 2) = ln 5 et x = ln 5/ln 2,5 ≈ 1,609/0,916 = 1,756.
3. La fonction f(x) = 0,8ˣ a pour dérivée f′(x) = (ln 0,8) × 0,8ˣ. Comme ln 0,8 ≈ −0,223 < 0, elle est strictement décroissante, et f(x) tend vers 0 en +∞ : une décote de 20 % par an ne mène jamais à zéro, elle s'en approche.
4. Pour 5ˣ = 40, on trouve x = ln 40/ln 5 ≈ 3,689/1,609 = 2,29. Contrôle : 5² = 25 et 5³ = 125, et 2,29 est bien entre 2 et 3.

:::

::: piege Dériver aˣ comme une puissance : (aˣ)′ = x aˣ⁻¹
Pour dériver 2ˣ, on écrit « (2ˣ)′ = x × 2ˣ⁻¹ ». Cela tente parce que la dérivée de xⁿ est n xⁿ⁻¹. Mais ici la variable est l'exposant, pas la base : 2ˣ = e^(x ln 2), donc (2ˣ)′ = (ln 2) 2ˣ. Test en x = 0 : la formule fausse donne 0, alors que 2ˣ passe de 1 à 1,07 entre x = 0 et x = 0,1, soit une pente proche de 0,7 = ln 2.
:::

::: propriete
- aˣ n'a de sens pour tout réel x que si a > 0, et on la calcule toujours par e^(x ln a).
- Pour résoudre aˣ = k (k > 0), on prend le logarithme : x = ln k/ln a ; pour comparer deux bases, on compare ln a et ln b.
- Le sens de variation de aˣ dépend du signe de ln a, donc de la position de a par rapport à 1.

Cas limite : si a = 1, ln a = 0 et 1ˣ = 1 ; l'équation 1ˣ = k n'a pas la forme x = ln k/ln a, puisqu'on diviserait par 0.
:::

::: verifie
Résoudre dans ℝ l'équation 0,5ˣ = 0,1 puis dire si x ↦ 0,5ˣ est croissante.

---

On prend le logarithme : x ln 0,5 = ln 0,1, donc x = ln 0,1/ln 0,5 ≈ (−2,303)/(−0,693) ≈ 3,32. Comme 0,5 < 1, ln 0,5 < 0 et la fonction est strictement décroissante ; ce résultat est cohérent, puisque 0,5³ = 0,125 > 0,1 > 0,0625 = 0,5⁴ place x entre 3 et 4.
:::

::: retenir
aˣ = e^(x ln a) pour a > 0, de dérivée (ln a) aˣ ; croissante si a > 1, décroissante si 0 < a < 1 ; aˣ = k se résout par x = ln k/ln a.
:::

## 💶 Intérêts composés, taux équivalent, durée de placement

Un artisan place 12 000 DT à 6 % par an, les intérêts étant ajoutés au capital chaque année.
Que vaut son capital après 5 ans, et comment calculer le taux mensuel équivalent ou la durée pour doubler ?

::: definition
Un capital C placé à un taux annuel t (écrit en nombre : 6 % = 0,06) pendant n années, à intérêts composés, a pour **valeur acquise** V = C (1 + t)ⁿ. Le **coefficient multiplicateur** annuel est 1 + t.

- Le **taux mensuel équivalent** t′ vérifie (1 + t′)¹² = 1 + t, donc 1 + t′ = (1 + t)^(1/12).
- La **durée** n nécessaire pour atteindre V est n = ln(V/C)/ln(1 + t).
- Le **capital à placer** pour obtenir V est C = V/(1 + t)ⁿ.
:::

::: exemple Valeur acquise, durée de doublement et taux équivalent
1. Valeur acquise : V = 12 000 × 1,06⁵ = 12 000 × 1,338226 ≈ 16 058,71 DT.
2. Doublement à 4 % : 1,04ⁿ = 2 équivaut à n = ln 2/ln 1,04 ≈ 0,6931/0,0392 = 17,67. Si les intérêts ne sont versés qu'en fin d'année, n se compte en années entières : il faut 18 ans, car à 17 ans 1,04¹⁷ ≈ 1,95 n'a pas encore doublé le capital.
3. Taux mensuel équivalent à 9 % par an : 1 + t′ = 1,09^(1/12) = e^(ln(1,09)/12) = e^(0,00718) ≈ 1,00721, donc t′ ≈ 0,72 % par mois.
4. Contrôle de 3 : 1,00721¹² ≈ 1,090, on retrouve bien 9 %.
5. Taux annuel t d'un chiffre d'affaires passé de 80 000 à 116 000 DT en 5 ans : (1 + t)⁵ = 1,45, donc 1 + t = 1,45^(1/5) ≈ 1,0771, soit t ≈ 7,71 %.

:::

::: piege Diviser le taux annuel par 12 pour obtenir le taux mensuel
Pour un taux de 9 % par an, on écrit « 9/12 = 0,75 % par mois ». Cela tente parce que l'année a douze mois. Mais les intérêts se composent : 1,0075¹² = 1,0938, soit 9,38 % sur l'année et non 9 %. Le bon taux mensuel est 0,72 %, car 1,0072¹² = 1,090. La division par 12 ne vaut que pour des intérêts simples.
:::

::: propriete
- La valeur acquise croît comme un exposant : V = C (1 + t)ⁿ = C e^(n ln(1 + t)), de la forme C aⁿ avec a = 1 + t.
- Pour une durée ou un taux inconnu, on isole la puissance, puis on prend ln (durée) ou on prend la racine n-ième (taux).
- Pour passer d'une période à une autre, on compose les coefficients multiplicateurs au lieu d'additionner les taux.

Cas limite : quand les intérêts ne sont capitalisés qu'une fois par an, une durée non entière s'arrondit à l'année supérieure (17 ans ne suffisent pas pour doubler à 4 %) ; avec un taux mensuel équivalent, on peut compter au mois près : 17,67 ans ≈ 17 ans et 8 mois.
:::

::: verifie
Quel capital faut-il placer aujourd'hui à 3 % par an pour disposer de 20 000 DT dans 6 ans ?

---

On cherche C tel que C × 1,03⁶ = 20 000, donc C = 20 000/1,03⁶ = 20 000/1,1941 ≈ 16 749,69 DT. Contrôle : 16 749,69 × 1,1941 ≈ 20 000 ✓. Le capital initial est plus petit que l'objectif, ce qui est cohérent avec un placement qui gonfle.
:::

::: retenir
Valeur acquise V = C (1 + t)ⁿ ; taux mensuel équivalent (1 + t)^(1/12) − 1, jamais t/12 ; durée n = ln(V/C)/ln(1 + t), à arrondir à l'année supérieure si les intérêts sont annuels.
:::

## 🎯 Optimiser avec ln et eˣ : bénéfice et coût minimal

Une savonnerie fabrique x centaines de pains ; son bénéfice, en milliers de dinars, est B(x) = 10 ln x − 2x pour x > 0 : le premier terme est une recette qui s'essouffle, le second un coût qui grandit à vitesse constante.
Pour quelle production le bénéfice est-il maximal, et que vaut-il ?

::: methode Optimiser avec ln ou eˣ
1. Fixer le domaine de la fonction (x > 0 pour un ln).
2. Calculer la dérivée et la mettre sous une forme dont on lit le signe.
3. Résoudre f′(x) = 0, en utilisant ln ou eˣ pour sortir x d'un exposant ou d'un logarithme.
4. Étudier le signe de f′ : le maximum est là où f′ passe de + à −, le minimum là où elle passe de − à +.
5. Calculer la valeur de f en ce point et conclure en unités de l'énoncé.
:::

::: exemple Un bénéfice maximal avec ln et un coût minimal avec eˣ
1. Pour B(x) = 10 ln x − 2x, la dérivée est B′(x) = 10/x − 2 = (10 − 2x)/x. Elle est positive pour x < 5 et négative pour x > 5, donc B est maximal en x = 5, soit 500 pains.
2. Le bénéfice maximal est B(5) = 10 ln 5 − 10 ≈ 16,094 − 10 = 6,094 milliers de dinars, soit environ 6 094 dinars.
3. Un atelier a pour coût de machine f(x) = 3x + 12 e^(−x/2) en milliers de dinars (x en milliers de pièces). La dérivée est f′(x) = 3 − 6 e^(−x/2).
4. f′(x) = 0 équivaut à e^(−x/2) = 1/2, donc −x/2 = ln(1/2) = −ln 2, soit x = 2 ln 2 ≈ 1,386. La dérivée est négative avant, positive après : c'est un minimum.
5. Le coût minimal est f(2 ln 2) = 6 ln 2 + 12 × (1/2) = 6 ln 2 + 6 ≈ 10,159 milliers de dinars.

:::

::: piege Oublier de diviser par le coefficient de l'exposant
Pour résoudre e^(−x/2) = 1/2, on écrit « donc −x = ln(1/2) » ou « x = ln 2 ». Cela tente parce qu'on a pensé à prendre le logarithme. Mais l'exposant est −x/2, pas −x : on obtient −x/2 = −ln 2, donc x = 2 ln 2. Test : e^(−ln 2/2) = 1/√2 ≈ 0,707, qui n'est pas 1/2 ; alors que e^(−(2 ln 2)/2) = e^(−ln 2) = 1/2 ✓.
:::

::: propriete
- Un extremum d'une fonction dérivable se cherche là où f′ s'annule, et se confirme par le changement de signe de f′ ou par les bornes du domaine.
- Avec ln, la dérivée a souvent un dénominateur en x : on réduit au même dénominateur pour lire le signe. Le coût moyen minimal du chapitre précédent se traite de la même façon quand le coût total contient un ln.
- Avec eˣ, la dérivée s'écrit k − m e^(u) : f′ = 0 se résout en prenant ln des deux côtés, en isolant d'abord eᵘ.

Cas limite : si f′ ne change pas de signe en un point où elle s'annule, il n'y a pas d'extremum en ce point, comme x³ en 0.
:::

::: verifie
Un bénéfice vaut B(x) = 8 ln x − 2x (en milliers de dinars, x en centaines d'objets). Pour quelle valeur de x est-il maximal, et que vaut ce maximum ?

---

B′(x) = 8/x − 2 = (8 − 2x)/x, positive pour x < 4 et négative pour x > 4 : le maximum est atteint en x = 4, soit 400 objets. Sa valeur est B(4) = 8 ln 4 − 8 ≈ 11,09 − 8 = 3,09 milliers de dinars. Contrôle : B(3) = 8 ln 3 − 6 ≈ 2,79 et B(5) = 8 ln 5 − 10 ≈ 2,88, tous deux plus petits que 3,09 ✓.
:::

::: retenir
Pour optimiser avec ln ou eˣ : domaine, dérivée mise sous forme lisible, résolution de f′(x) = 0 avec ln ou eˣ (en divisant par le coefficient de l'exposant), changement de signe de f′ pour nommer maximum ou minimum, puis valeur en unités de l'énoncé.
:::
