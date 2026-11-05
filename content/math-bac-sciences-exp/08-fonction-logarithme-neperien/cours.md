# ⚔️ Logarithme népérien — l'aire qui change les produits en sommes

> 💡 «Additionner est plus facile que multiplier : celui qui trouve la fonction qui transforme les produits en sommes tient la clé du calcul.»

Au chapitre 6, une primitive te manquait : celle de t ↦ 1/t. En 1544, Michael Stifel avait remarqué qu'en alignant la suite arithmétique (…, −1, 0, 1, 2, 3, …) sur la suite géométrique (…, 1/2, 1, 2, 4, 8, …), **le produit d'en bas devient la somme d'en haut** : pour multiplier 8 par 32, on lit les « logarithmes » 3 et 5, on les additionne, 3 + 5 = 8, et l'on retrouve en bas 256 = 8 × 32. Napier (1614), Briggs (1624) et Bürgi (1620) en ont tiré les premières tables. Huit notions te mènent de la définition de **ln** jusqu'aux études de fonctions du bac. On suppose acquis le théorème des valeurs intermédiaires (chapitre 1), les primitives (chapitre 6) et l'intégrale avec l'intégration par parties (chapitre 7).

## 🏰 La fonction ln : une aire devenue fonction

Trace l'hyperbole y = 1/t pour t > 0 et note S(a) l'aire, en u.a, comprise entre elle, l'axe des abscisses et les droites t = 1 et t = a, pour a > 1.
Aucune primitive du chapitre 6 ne donne 1/t, mais l'intégrale sait faire : t ↦ 1/t est continue sur ]0, +∞[, donc x ↦ ∫₁ˣ dt/t existe pour tout x > 0.
Quelles propriétés a cette fonction, et mesure-t-elle toujours une aire ?

::: definition
**Fonction logarithme népérien** — « On appelle fonction logarithme népérien et on note ln, la fonction x ↦ ln x = ∫₁ˣ 1/t dt, x > 0. »
:::

Quatre conséquences tombent immédiatement de cette définition :

| Résultat                                      | D'où il vient                        |
| --------------------------------------------- | ------------------------------------ |
| ln est définie, continue, dérivable sur ]0, +∞[ | c'est une primitive de t ↦ 1/t       |
| ln′(x) = 1/x pour tout x > 0                  | dérivée d'une primitive              |
| ln est **strictement croissante** sur ]0, +∞[ | sa dérivée 1/x est strictement positive |
| ln 1 = 0                                      | ∫₁¹ dt/t = 0                         |

::: figure Pour x > 1, ln x est exactement l'aire coincée sous l'hyperbole y = 1/t entre t = 1 et t = x.
<svg viewBox="0 0 340 215"><polygon points="110,180 110,135 123,144 137.5,150 151,154 165,157.5 192.5,162 220,165 220,180" fill="#0f6e56" fill-opacity="0.18"/><path d="M45 180 H335" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M55 198 V55" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M335 180 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M55 55 l-3.5 7 l7 0 z" fill="#0f172a"/><path d="M85 98 L93.5 116 L100 125 L110 135 L123 144 L137.5 150 L151 154 L165 157.5 L192.5 162 L220 165 L247 167 L275 169 L302 170 L330 171" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><line x1="110" y1="135" x2="110" y2="180" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="220" y1="165" x2="220" y2="180" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="110" y="195" text-anchor="middle" fill="#0f172a">1</text><text x="220" y="195" text-anchor="middle" fill="#0f172a">x</text><text x="47" y="195" text-anchor="middle" fill="#0f172a">O</text><text x="160" y="174" text-anchor="middle" fill="#0f6e56">ln x</text><text x="272" y="158" fill="#0f6e56">y = 1/t</text></g></svg>
:::

::: exemple Encadrer ln 2 à la main, puis situer le réel e

1. Partage [1, 2] en trois intervalles de longueur 1/3. Sur chacun, 1/t est **décroissante** : le rectangle bâti sur la valeur de droite minore l'aire, celui bâti sur la valeur de gauche la majore.
2. Cela donne (1/3)(3/4 + 3/5 + 1/2) ≤ S(2) ≤ (1/3)(1 + 3/4 + 3/5), soit 37/60 ≤ ln 2 ≤ 47/60, donc 0,616 ≤ ln 2 ≤ 0,784. Contrôle : la calculatrice donne ln 2 ≈ 0,693 ✓.
3. Partage maintenant [1, 3] en huit intervalles de longueur 1/4 : les rectangles du bas donnent ln 3 ≥ 1/5 + 1/6 + … + 1/12 ≈ 1,020, donc ln 3 > 1.
4. Ainsi ln 2 < 1 < ln 3. La fonction ln est continue et strictement croissante : le théorème des valeurs intermédiaires fournit un unique réel de ]2, 3[ dont le logarithme vaut 1. On le note **e**, et ln e = 1 (e ≈ 2,71828).

:::

::: figure Les trois rectangles verts minorent l'aire, les trois rectangles pointillés la majorent : ln 2 est pris en tenaille entre 37/60 et 47/60.
<svg viewBox="0 0 340 215"><g fill="#0f6e56" fill-opacity="0.18" stroke="#0f6e56" stroke-width="1.4"><rect x="70" y="102.5" width="73.33" height="82.5"/><rect x="143.33" y="119" width="73.34" height="66"/><rect x="216.67" y="130" width="73.33" height="55"/></g><g fill="none" stroke="#b45309" stroke-width="1.6" stroke-dasharray="5 4"><rect x="70" y="75" width="73.33" height="110"/><rect x="143.33" y="102.5" width="73.34" height="82.5"/><rect x="216.67" y="119" width="73.33" height="66"/></g><path d="M40 185 H325" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M325 185 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M70 75 L106.7 90.7 L143.3 102.5 L180 111.7 L216.7 119 L253.3 125 L290 130" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="70" y="202" text-anchor="middle" fill="#0f172a">1</text><text x="143.33" y="202" text-anchor="middle" fill="#0f172a">4/3</text><text x="216.67" y="202" text-anchor="middle" fill="#0f172a">5/3</text><text x="290" y="202" text-anchor="middle" fill="#0f172a">2</text><text x="248" y="68" fill="#0f172a">y = 1/t</text></g></svg>
:::

::: piege
**Erreur : croire que ln x est une aire pour tout x.** La borne du bas de l'intégrale est **1**, pas 0 : ln 1 = 0, et ln n'existe pas en 0. Pour 0 < x < 1, les bornes de ∫₁ˣ sont dans l'ordre inverse, l'intégrale change de signe et ln x est l'**opposé** de l'aire entre x et 1 : il est négatif. L'erreur tente parce que le dessin de l'aire est facile à retenir, mais il ne vaut que pour x > 1. Pour le signe, un seul réflexe : ln est strictement croissante et ln 1 = 0, donc ln x < 0 sur ]0, 1[ et ln x > 0 sur ]1, +∞[.
:::

::: verifie À toi : lire ln sans la calculer
Donner ln′(4), puis le signe de ln(0,3), en justifiant.

---

ln est la primitive de t ↦ 1/t qui s'annule en 1, donc ln′(4) = 1/4. Puis 0,3 < 1 et ln est strictement croissante, donc ln(0,3) < ln 1 = 0 : le logarithme est négatif, bien que 0,3 soit un nombre positif.
:::

::: retenir
ln x = ∫₁ˣ dt/t pour x > 0 : c'est la primitive de 1/x qui s'annule en 1, donc ln′(x) = 1/x, ln est strictement croissante, ln 1 = 0 ; l'unique réel e de ]2, 3[ vérifie ln e = 1.
:::

## ⚡ Comparer et résoudre : la croissance de ln au travail

Puisque ln est strictement croissante, elle conserve l'ordre : si a < b alors ln a < ln b, et inversement.
Deux réels strictement positifs sont donc égaux, ou rangés dans le même ordre, exactement comme leurs logarithmes.
C'est ce qui permet de résoudre ln(1 − x) = ln(2 + x) en « enlevant » ln. À quelle condition a-t-on le droit de le faire ?

::: propriete
**Encadré** — « Soit a et b deux réels strictement positifs. ln a > ln b, si et seulement si, a > b. ln a = ln b, si et seulement si, a = b. ln a = 0, si et seulement si, a = 1. ln a > 0, si et seulement si, a > 1. ln a < 0, si et seulement si, 0 < a < 1. »
Toutes ces équivalences exigent a > 0 et b > 0 : elles ne s'appliquent qu'**après** avoir écrit les conditions d'existence.
:::

::: methode
**Méthode en trois temps** pour toute équation ou inéquation en ln : (1) écrire les **conditions d'existence** (chaque expression sous un ln est > 0), (2) ramener les deux membres à la forme ln A et ln B, (3) appliquer l'équivalence ou la croissance, puis vérifier que la solution respecte les conditions.
:::

::: exemple Quatre résolutions

1. ln(1 − x) = ln(2 + x). Conditions : 1 − x > 0 et 2 + x > 0, donc −2 < x < 1. L'égalité équivaut à 1 − x = 2 + x, soit x = −1/2, qui est bien dans ]−2, 1[ : **S = {−1/2}**.
2. ln(4 − 3x) > 0. On utilise ln a > 0 ⟺ a > 1 : 4 − 3x > 1, soit x < 1. La condition 4 − 3x > 0 est alors automatique : **S = ]−∞, 1[**.
3. ln(2x − 5) ≤ ln x. Conditions : 2x − 5 > 0 et x > 0, donc x > 5/2. La croissance donne 2x − 5 ≤ x, soit x ≤ 5 : **S = ]5/2, 5]**. Contrôle : x = 3 donne ln 1 = 0 ≤ ln 3 ✓ ; x = 6 donne ln 7 > ln 6, exclu ✓.
4. ln(x² + 1) ≥ 0. On a ln a ≥ 0 ⟺ a ≥ 1 : x² + 1 ≥ 1 ⟺ x² ≥ 0, vrai pour tout réel, et x² + 1 > 0 partout : **S = ℝ**.

:::

::: piege
**Erreur : « enlever » ln sans regarder le domaine.** Dans ln(x − 3) = ln(2x + 1), on écrit x − 3 = 2x + 1 donc x = −4. Mais pour x = −4 on obtient x − 3 = −7 < 0 : ln(−7) n'existe pas. Les conditions d'existence donnent x > 3, et −4 n'y est pas : l'équation n'a **aucune solution**. Une valeur trouvée hors du domaine est une fausse solution, jamais une demi-solution.
:::

::: verifie À toi : une inéquation avec deux conditions
Résoudre ln(5 − x) < ln(x + 1).

---

Conditions : 5 − x > 0 et x + 1 > 0, donc −1 < x < 5. La croissance de ln donne 5 − x < x + 1, soit x > 2. On garde ce qui vérifie les deux : S = ]2, 5[.
:::

::: retenir
Pour a > 0 et b > 0, ln a ⋛ ln b équivaut à a ⋛ b ; on écrit toujours les conditions d'existence d'abord, et l'on rejette toute solution qui les viole.
:::

## 🧮 Les propriétés algébriques : le produit devient une somme

Dans la table de Stifel, 3 et 5 sont les logarithmes de 8 et de 32, et leur somme 8 est le logarithme de 256 = 8 × 32.
Une fonction qui transforme tous les produits en sommes ferait ce travail pour n'importe quels nombres.
Le logarithme népérien le fait-il ? La preuve est un bijou : à a > 0 fixé, x ↦ ln(ax) et x ↦ ln x ont **la même dérivée** a/(ax) = 1/x sur ]0, +∞[, donc elles diffèrent d'une constante c ; en x = 1, ln a = ln 1 + c donne c = ln a.

::: propriete
**Théorème** — « Soit a et b deux réels strictement positifs. • ln(a.b) = ln a + ln b. • ln(a/b) = ln a − ln b. • ln(1/b) = −ln b. • Pour tout entier p, ln(aᵖ) = p ln a. • Pour tout entier p ≥ 2, ln(ᵖ√a) = (1/p) ln a. »
:::

| Écriture         | Se transforme en | Exemple                  |
| ---------------- | ---------------- | ------------------------ |
| ln(ab)           | ln a + ln b      | ln 6 = ln 2 + ln 3       |
| ln(a/b)          | ln a − ln b      | ln(3/2) = ln 3 − ln 2    |
| ln(1/b)          | −ln b            | ln(1/e) = −1             |
| ln(aᵖ), p ∈ ℤ    | p ln a           | ln(e⁻²) = −2             |
| ln(ᵖ√a), p ≥ 2   | (1/p) ln a       | ln(√e) = 1/2             |

::: exemple Exprimer avec ln 2 et ln 3, simplifier avec e

1. Factorise d'abord : 108 = 2² × 3³, donc ln 108 = 2 ln 2 + 3 ln 3 ≈ 2(0,693) + 3(1,099) = 4,682.
2. 81/8 = 3⁴/2³, donc ln(81/8) = 4 ln 3 − 3 ln 2 ≈ 4,394 − 2,079 = 2,315. Contrôle : 81/8 = 10,125 et ln 10,125 ≈ 2,315 ✓.
3. ln(√(1/27)) = (1/2) ln(1/27) = −(1/2) ln 27 = −(3/2) ln 3 ≈ −1,648.
4. Avec ln e = 1 : ln(∛e / √e) = 1/3 − 1/2 = −1/6, et ln(⁴√e · ∛e) = 1/4 + 1/3 = 7/12.

:::

::: exemple Une équation du second degré en ln x, puis un plus petit entier

1. Résoudre (ln x)² − 2 ln x − 3 = 0 sur ]0, +∞[. On pose X = ln x : X² − 2X − 3 = (X − 3)(X + 1) = 0, donc X = 3 ou X = −1. Comme ln(e³) = 3 ln e = 3 et ln(1/e) = −1, les solutions sont **x = e³ et x = 1/e**. Contrôle : 3² − 2 × 3 − 3 = 0 ✓ et (−1)² + 2 − 3 = 0 ✓.
2. Quel est le plus petit entier naturel n tel que (1/2)ⁿ ≤ 10⁻⁴ ? La croissance de ln et la règle de la puissance donnent −n ln 2 ≤ −4 ln 10, donc n ≥ 4 ln 10 / ln 2 ≈ 13,29 : **n = 14**.
3. Quel est le plus petit entier naturel n tel que 2ⁿ ≥ 10⁵ ? Alors n ln 2 ≥ 5 ln 10, donc n ≥ 5 ln 10 / ln 2 ≈ 16,61 : **n = 17**. Contrôle : 2¹⁶ = 65 536 < 10⁵ ≤ 131 072 = 2¹⁷ ✓.

:::

::: piege
**Erreur : « ln(a + b) = ln a + ln b ».** Avec a = 2 et b = 3, ln(2 + 3) = ln 5 ≈ 1,609, alors que ln 2 + ln 3 = ln 6 ≈ 1,792. Seul le **produit** devient une somme. Et attention aux puissances paires : ln(x²) = 2 ln|x|, pas 2 ln x, car pour x < 0 le nombre ln x n'existe même pas.
:::

::: verifie À toi : décomposer un entier
Exprimer ln 72 à l'aide de ln 2 et de ln 3, puis en donner une valeur approchée.

---

72 = 2³ × 3², donc ln 72 = 3 ln 2 + 2 ln 3 ≈ 3(0,693) + 2(1,099) = 2,079 + 2,198 = 4,277 ✓ (la calculatrice donne ln 72 ≈ 4,277).
:::

::: retenir
ln(ab) = ln a + ln b, ln(a/b) = ln a − ln b, ln(aᵖ) = p ln a, ln(ᵖ√a) = (1/p) ln a pour a, b > 0 ; mais ln(a + b) n'est pas ln a + ln b.
:::

## 📈 Limites, variations et courbe de ln

ln 1 000 000 n'est que d'environ 13,8, alors que le nombre a six zéros : ln monte lentement.
S'arrête-t-elle quelque part, ou dépasse-t-elle tout nombre ? Et près de 0, où part-elle ?
Trois arguments répondent, et un quatrième calcule une pente.

**1. ln n'est pas majorée.** Pour tout entier n ≥ 1, sur [2ⁿ, 2ⁿ⁺¹] on a 1/t ≥ 1/2ⁿ⁺¹, donc ∫ de 2ⁿ à 2ⁿ⁺¹ de dt/t ≥ 2ⁿ/2ⁿ⁺¹ = 1/2. La relation de Chasles recolle n morceaux de même nature : ln(2ⁿ) ≥ n/2, qui dépasse tout réel. Comme ln est croissante, lim_{x→+∞} ln x = +∞.

**2. En 0⁺, par symétrie.** Les fonctions x ↦ ln x et x ↦ −ln(1/x) ont la même dérivée 1/x sur ]0, +∞[ et la même valeur 0 en 1 : elles sont égales. Quand x → 0⁺, 1/x → +∞, donc ln x → −∞ : l'axe des ordonnées est **asymptote verticale**.

**3. ln croît moins vite que x.** Pour t ≥ 1, 1/t ≤ 1/√t, donc en intégrant de 1 à x : ln x ≤ 2√x − 2. Alors 0 ≤ (ln x)/x ≤ 2/√x pour x ≥ 1, et le théorème des gendarmes conclut.

**4. Un nombre dérivé.** (ln x − ln 1)/(x − 1) tend vers ln′(1) = 1 quand x → 1.

::: propriete
**Théorème** — « lim_{x→+∞} ln x = +∞. lim_{x→0⁺} ln x = −∞. »

**Théorème** — « lim_{x→1} (ln x)/(x − 1) = 1. lim_{x→+∞} (ln x)/x = 0. »
Comme ln est continue, strictement croissante, de limites −∞ et +∞ aux bornes, **ln réalise une bijection de ]0, +∞[ sur ℝ** : tout réel k a un unique antécédent : l'équation ln x = k a une unique solution. En particulier ln x = 1 a pour unique solution e.
:::

::: figure La courbe de ln traverse l'axe en x = 1, passe par le point (e ; 1) et longe l'axe des ordonnées vers −∞ ; elle monte sans jamais s'arrêter.
<svg viewBox="0 0 340 250">
<title>Courbe de la fonction ln : elle traverse l'axe des abscisses en 1, passe par le point (e ; 1) et plonge vers −∞ le long de l'axe des ordonnées</title>
<line x1="30" y1="140" x2="326" y2="140" stroke="#0f172a" stroke-width="1.6"/>
<line x1="50" y1="248" x2="50" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,140 318,136 318,144" fill="#0f172a"/><polygon points="50,14 46,22 54,22" fill="#0f172a"/>
<line x1="50" y1="100" x2="180.5" y2="100" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<line x1="180.5" y1="100" x2="180.5" y2="140" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<polyline points="54.8,232.1 55.8,224.8 57.2,215.9 59.6,204.4 62,195.5 64.4,188.2 69.2,176.7 74,167.7 78.8,160.4 88.4,148.9 98,140 110,131.1 122,123.8 146,112.3 170,103.3 194,96.1 218,89.9 242,84.5 266,79.8 290,75.6 314,71.8 338,68.3" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="98" cy="140" r="3.5" fill="#0f172a"/><circle cx="180.5" cy="100" r="3.5" fill="#0f172a"/>
<g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">
<text x="42" y="154" text-anchor="end" fill="#0f172a">O</text>
<text x="102" y="156" text-anchor="middle" fill="#0f172a">1</text>
<text x="180.5" y="156" text-anchor="middle" fill="#0f172a">e</text>
<text x="44" y="104" text-anchor="end" fill="#0f172a">1</text>
<text x="284" y="65.6" fill="#0f6e56">C</text>
</g></svg>
:::

::: exemple Des limites qui sont des nombres dérivés

1. lim_{x→3} (ln x − ln 3)/(x − 3) = ln′(3) = **1/3**.
2. lim_{x→e} (ln x − 1)/(x − e) : comme ln e = 1, c'est le nombre dérivé ln′(e) = **1/e**.
3. lim_{x→0} ln(1 + 3x)/x. On pose t = 3x, qui tend vers 0 : ln(1 + t)/t → ln′(1) = 1, donc ln(1 + 3x)/x = 3 × ln(1 + t)/t → **3**.
4. lim_{x→+∞} ln(x⁴)/x = lim 4 ln x / x = **0**, puisque ln(x⁴) = 4 ln x.
5. lim_{x→+∞} ln((1 + x)/(2 + x)) : le quotient tend vers 1 et ln est continue en 1, donc la limite est ln 1 = **0**.

:::

::: piege
**Erreur : « ln monte si lentement qu'elle est bornée ».** ln(10⁹) ≈ 20,7 seulement, et l'on pourrait croire que ln ne dépassera jamais 100. C'est faux : ln(2²⁰⁰) ≥ 200/2 = 100 d'après l'argument 1. Une croissance lente n'est pas une croissance bornée, et lim_{x→+∞} ln x = +∞ est bien une limite infinie.
:::

::: verifie À toi : reconnaître le nombre dérivé
Calculer lim_{x→0} ln(1 − 2x)/x.

---

On pose t = −2x, qui tend vers 0. Alors ln(1 − 2x)/x = (−2) × ln(1 + t)/t, et ln(1 + t)/t tend vers ln′(1) = 1. La limite vaut −2.
:::

::: retenir
ln tend vers +∞ en +∞ et vers −∞ en 0⁺, sans jamais s'arrêter ; (ln x)/x → 0 en +∞ ; (ln x)/(x − 1) → 1 en 1 ; ln est une bijection croissante de ]0, +∞[ sur ℝ.
:::

## 🔮 Croissances comparées : ln perd toujours

En x = 10⁶, ln x vaut environ 13,8 alors que √x vaut 1 000 : le quotient (ln x)/√x est déjà minuscule.
Contre n'importe quelle puissance de x, le logarithme est le plus lent, que ce soit en +∞ ou près de 0.
Comment le montrer pour toutes les puissances à la fois ?

::: propriete
**Théorème** — « Pour tous entiers naturels non nuls n et m, lim_{x→+∞} lnⁿx / xᵐ = 0 et lim_{x→0⁺} xᵐ lnⁿx = 0. »
La notation lnⁿx désigne (ln x)ⁿ. Pour la preuve, on ramène tout au cas connu (ln y)/y → 0 : en posant y = ⁿ√(xᵐ), on a ln x = (n/m) ln y et xᵐ = yⁿ, donc (ln x)ⁿ/xᵐ = ((n/m)(ln y)/y)ⁿ → 0. Le second résultat s'obtient en remplaçant x par 1/y.
:::

::: exemple Cinq limites à démêler

1. lim_{x→+∞} (ln x)/¹⁰√x. On pose y = ¹⁰√x, donc ln x = 10 ln y et la quantité vaut 10 (ln y)/y → **0**. Contrôle : pour x = 10²⁰, 46,05/100 ≈ 0,46 ; pour x = 10⁴⁰, 92,1/10 000 ≈ 0,009 : la descente est lente mais réelle ✓.
2. lim_{x→+∞} (x − ln x), forme « +∞ − ∞ » : x − ln x = x(1 − (ln x)/x), donc la limite est **+∞** × (1 − 0) = +∞.
3. lim_{x→0⁺} (x² + ln³x) : x² → 0 et ln³x → −∞, donc **−∞**. En +∞, lim (x² − ln³x) = lim x²(1 − ln³x/x²) = **+∞**.
4. lim_{x→0⁺} x⁴(1 − ln⁵x) = lim (x⁴ − x⁴ ln⁵x) = 0 − 0 = **0**, par croissance comparée (m = 4, n = 5).
5. lim_{x→0⁺} √x ln x : on pose y = √x, donc ln x = 2 ln y et la quantité vaut 2 y ln y → **0**.

:::

::: piege
**Erreur : appliquer « ln perd » à (ln x)/x en 0⁺.** Ici ln x → −∞ **et** 1/x → +∞ : les deux poussent dans le même sens, donc lim_{x→0⁺} (ln x)/x = **−∞** (pour x = 10⁻³ : −6 907,8). La croissance comparée ne vaut que pour le produit xᵐ lnⁿx, où la puissance de x écrase le logarithme. De même lim_{x→0⁺} (ln x + 1/x) = **+∞**, car ln x + 1/x = (1/x)(x ln x + 1) et x ln x → 0.
:::

::: verifie À toi : une forme avec 1/x²
Calculer lim_{x→0⁺} (1/x² + ln x).

---

On factorise 1/x² : 1/x² + ln x = (1/x²)(1 + x² ln x). Par croissance comparée x² ln x → 0, donc le facteur entre parenthèses tend vers 1, tandis que 1/x² tend vers +∞ : la limite vaut +∞.
:::

::: retenir
(ln x)ⁿ/xᵐ → 0 en +∞ et xᵐ(ln x)ⁿ → 0 en 0⁺ ; en dehors de ce cadre (comme (ln x)/x en 0⁺), on calcule directement ou on factorise.
:::

## 🛡️ Dériver ln(u) et ln|u|

Soit f(x) = ln(x² + x + 2). Le trinôme x² + x + 2 a pour discriminant 1 − 8 = −7 < 0 et son coefficient dominant est positif : il est strictement positif sur ℝ, donc f existe partout.
Le théorème de dérivation des fonctions composées donne alors une formule simple : f′(x) = (2x + 1)/(x² + x + 2).
Cette formule vaut-elle pour tout logarithme d'une fonction, et que devient-elle quand u change de signe ?

::: propriete
**Théorème** — « Soit u une fonction dérivable sur un intervalle I et telle que u(x) > 0, pour tout réel x dans I. La fonction f : x ↦ ln(u(x)) est dérivable sur I et f′(x) = u′(x)/u(x), pour tout x dans I. »
**Corollaire** — « Soit u une fonction dérivable sur un intervalle I et telle que u(x) ≠ 0, pour tout réel x de I. La fonction f : x ↦ ln|u(x)| est dérivable sur I et f′(x) = u′(x)/u(x), pour tout x de I. »
La dérivée est la même dans les deux cas ; seul l'ensemble de définition change : ln(u) exige u > 0, ln|u| se contente de u ≠ 0.
:::

::: exemple Domaine d'abord, dérivée ensuite

1. f(x) = ln(x² + x + 2) sur ℝ : f′(x) = (2x + 1)/(x² + x + 2). Contrôle en x = 1 : la formule donne 3/4 = 0,75 ; le taux entre 1 et 1,01 vaut (ln 4,0301 − ln 4)/0,01 ≈ 0,750 ✓.
2. f(x) = x ln(x²) sur ]−∞, 0[ : en dérivant un produit, f′(x) = ln(x²) + x × 2x/x² = ln(x²) + 2 = 2 ln|x| + 2, soit **f′(x) = 2(1 + ln|x|)**. Contrôle en x = −2 : ln 4 + 2 ≈ 3,386 et 2(1 + ln 2) ≈ 3,386 ✓.
3. f(x) = ln|(x − 1)/x| : u = (x − 1)/x s'annule en 1 et n'existe pas en 0, donc D_f = ℝ \ {0 ; 1}. Avec u′ = 1/x², on a u′/u = (1/x²) × x/(x − 1), soit **f′(x) = 1/(x(x − 1))**. Contrôle en x = 2 : 1/2, et ln|x − 1| − ln|x| a pour dérivée 1 − 1/2 = 1/2 ✓.
4. f(x) = ln((x − 2)/(x + 1)) + x. Le quotient est > 0 pour x < −1 ou x > 2 : D_f = ]−∞, −1[ ∪ ]2, +∞[. Avec u′ = 3/(x + 1)², on trouve f′(x) = 1 + 3/((x + 1)(x − 2)) = (x² − x + 1)/((x + 1)(x − 2)). Le numérateur a pour discriminant −3 < 0 (toujours > 0) et le dénominateur est > 0 sur D_f : **f est strictement croissante sur chaque intervalle**. De plus f(x) − x = ln u → ln 1 = 0 en ±∞ : la droite y = x est asymptote oblique.

:::

::: piege
**Erreur : dériver ln(−x) en −1/x.** Pour x < 0, f(x) = ln(−x) a pour dérivée u′/u = (−1)/(−x) = **1/x**, et non −1/x. Test : en x = −2, f(−2) = ln 2 ≈ 0,693 et f(−1,9) = ln 1,9 ≈ 0,642 : la fonction décroît, de pente voisine de −0,5 = 1/(−2). La dérivée −1/x serait positive ici, ce que la décroissance contredit.
:::

::: verifie À toi : domaine puis dérivée
Donner l'ensemble de définition de f(x) = ln(4 − x²) et calculer f′(x).

---

Il faut 4 − x² > 0, c'est-à-dire −2 < x < 2 : D_f = ]−2, 2[. Avec u = 4 − x² et u′ = −2x, f′(x) = −2x/(4 − x²) sur ]−2, 2[.
:::

::: retenir
f = ln(u) existe là où u > 0 et f = ln|u| là où u ≠ 0 ; dans les deux cas f′ = u′/u, et l'on résout toujours le signe de u avant de dériver.
:::

## 🧊 Primitives de u′/u et de ln, aires et intégrales

Au chapitre 6, aucune formule ne donnait de primitive de 1/x, ni de x/(x² + 1).
Le théorème de dérivation se lit à l'envers : si f = u′/u, alors f est la dérivée de ln|u|.
Et pour ln elle-même ? On dérive x ln x pour voir ce qui apparaît : (x ln x)′ = ln x + x × (1/x) = ln x + 1.

::: propriete
**Corollaire** — « Soit u une fonction dérivable sur un intervalle I et telle que u(x) ≠ 0 pour tout réel x dans I. Les primitives sur I de la fonction x ↦ u′(x)/u(x) sont les fonctions x ↦ ln|u(x)| + k, où k est une constante réelle. »
**Théorème** — « La fonction x ↦ x ln x − x est une primitive de la fonction x ↦ ln x sur ℝ*₊. » En effet (x ln x − x)′ = ln x + 1 − 1 = ln x ✓.
:::

::: exemple Quatre primitives par reconnaissance de u′/u

1. f(x) = x/(1 − x²) sur ]1, +∞[ : u = 1 − x², u′ = −2x, donc f = −(1/2) u′/u et **F(x) = −(1/2) ln|1 − x²| = −(1/2) ln(x² − 1)**. Vérification : F′(x) = −(1/2) × 2x/(x² − 1) = x/(1 − x²) ✓.
2. f(x) = (x + 1)/(x + 3) sur ]−∞, −4[ : degré égal en haut et en bas, on écrit f(x) = 1 − 2/(x + 3), donc **F(x) = x − 2 ln|x + 3| = x − 2 ln(−x − 3)**.
3. f(x) = 1/(x ln x) sur ]0, 1[ : u = ln x et u′ = 1/x, donc **F(x) = ln|ln x| = ln(−ln x)**, car ln x est négatif sur ]0, 1[.
4. f(x) = 2cos(2x)/sin(2x) sur ]0, π/2[ : u = sin 2x > 0 et u′ = 2cos 2x, donc **F(x) = ln(sin 2x)**.

:::

::: exemple Une décomposition, une intégration par parties, une aire, un volume

1. ∫₁² dt/(t(t + 1)) : on vérifie 1/(t(t + 1)) = 1/t − 1/(t + 1) en réduisant au même dénominateur. Alors l'intégrale vaut [ln t − ln(t + 1)]₁² = (ln 2 − ln 3) − (0 − ln 2) = 2 ln 2 − ln 3 = ln(4/3) ≈ 0,288.
2. ∫₁² ln(1 + t)/t² dt, par parties avec f(t) = ln(1 + t) et g′(t) = 1/t², donc g(t) = −1/t : [−ln(1 + t)/t]₁² + ∫₁² dt/(t(1 + t)) = (−(ln 3)/2 + ln 2) + ln(4/3) = **3 ln 2 − (3/2) ln 3 ≈ 0,432**.
3. Soit f(x) = 1 − x + ln x. On a f′(x) = (1 − x)/x : f est maximale en 1, où f(1) = 0, donc **ln x ≤ x − 1** pour tout x > 0. L'aire entre la courbe, l'axe et les droites x = α et x = 1 (0 < α < 1) vaut ∫ de α à 1 de (x − 1 − ln x) dx = [x²/2 − x ln x]_α¹ = 1/2 − α²/2 + α ln α, qui tend vers **1/2** quand α → 0⁺, puisque α ln α → 0.
4. Volume (formule V = π∫ₐᵇ f²(x)dx du chapitre 7) : l'arc de la courbe de ln compris entre x = 1 et x = e, tournant autour de l'axe des abscisses, engendre V = π∫₁ᵉ (ln x)² dx. Une primitive de ln²x est x ln²x − 2x ln x + 2x : sa dérivée vaut ln²x + 2 ln x − 2 ln x − 2 + 2 = ln²x ✓. Donc ∫₁ᵉ ln²x dx = (e − 2e + 2e) − 2 = e − 2 et **V = π(e − 2) ≈ 2,26**. Contrôle : e − 2 ≈ 0,718 > 0, comme il se doit pour l'intégrale d'un carré ✓.

:::

::: piege
**Erreur : oublier la valeur absolue ou le signe.** Une primitive de 1/x sur ]−∞, 0[ est ln|x|, pas « ln x » (qui n'existe pas) ; et quand f est négative sur [α, 1], l'intégrale ∫ f est négative : l'**aire** s'obtient en changeant le signe. Dans l'aire du point 3 de l'exemple précédent, ∫_α¹ f(x) dx = −(1/2 − α²/2 + α ln α) est négatif, l'aire est son opposé.
:::

::: verifie À toi : u′/u avec un facteur
Trouver une primitive de f(x) = x/(x² + 3) sur ℝ.

---

u = x² + 3 est > 0 sur ℝ et u′ = 2x, donc f = (1/2) u′/u. Une primitive est F(x) = (1/2) ln(x² + 3). On vérifie : F′(x) = (1/2) × 2x/(x² + 3) = f(x) ✓. Oublier le facteur 1/2 donnerait une dérivée deux fois trop grande.
:::

::: retenir
Les primitives de u′/u sont ln|u| + k ; une primitive de ln est x ln x − x ; pour une aire sous l'axe, on change le signe de l'intégrale.
:::

## 👑 Étudier une fonction à logarithme : le scénario du bac

Une étude de fonction avec ln suit presque toujours le même scénario : domaine, limites, dérivée, signe de la dérivée, tableau, branches infinies, tracé.
Le signe de f′ n'est souvent pas lisible : il faut alors une **fonction auxiliaire** g, étudiée à part, dont le signe commande celui de f′.
Quels outils des sept notions précédentes servent à quelle étape ?

::: methode
**Étude complète** : (1) domaine et limites aux bornes (croissances comparées) ; (2) dérivée, écrite avec u′/u et, si besoin, f′ = g/(un carré ou une quantité de signe connu) ; (3) variations de g, valeur clé (g(1) = 0, ou valeur imposée par le théorème des valeurs intermédiaires), donc signe de g ; (4) tableau de f ; (5) asymptotes, position par le signe de f − (asymptote) ; (6) tracé.
:::

::: exemple Quand f n'est pas dérivable partout : f(x) = x² ln²x, f(0) = 0

1. **Dérivabilité.** f est dérivable sur ]0, +∞[ comme produit. En 0, le taux (f(x) − f(0))/x = x ln²x tend vers 0 (croissance comparée, m = 1, n = 2) : f est dérivable à droite en 0 et f′_d(0) = 0, courbe à tangente horizontale à l'origine.
2. **Dérivée.** f′(x) = 2x ln²x + x² × 2 ln x × (1/x) = 2x ln x (ln x + 1). Pour x > 0, le signe est celui de ln x (ln x + 1), négatif exactement pour −1 < ln x < 0, c'est-à-dire 1/e < x < 1 (car ln(1/e) = −1).
3. **Valeurs et limite.** f(1/e) = (1/e²) × 1 = 1/e² ≈ 0,135 et f(1) = 0. En +∞, f(x) → +∞ et f(x)/x = x ln²x → +∞ : branche parabolique de direction l'axe des ordonnées.
4. **Tableau.** f croît de 0 à 1/e² sur [0, 1/e], décroît jusqu'à 0 sur [1/e, 1], puis croît vers +∞.

:::

::: figure La courbe de f part de l'origine, monte jusqu'au maximum local 1/e² en x = 1/e, redescend jusqu'à 0 en x = 1, puis monte sans fin en s'ouvrant vers le haut.
<svg viewBox="0 0 340 250">
<title>Courbe de f(x) = x² ln²x sur [0 ; 2,1] : elle part de l'origine, atteint un maximum local 1/e² en 1/e, revient à 0 en 1 puis monte sans limite</title>
<line x1="30" y1="215" x2="326" y2="215" stroke="#0f172a" stroke-width="1.6"/>
<line x1="50" y1="236" x2="50" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,215 318,211 318,219" fill="#0f172a"/><polygon points="50,14 46,22 54,22" fill="#0f172a"/>
<line x1="94.1" y1="205.5" x2="94.1" y2="215" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<line x1="50" y1="205.5" x2="94.1" y2="205.5" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<polyline points="50,215 52.4,214.6 56,213.4 62,211.3 68,209.3 74,207.7 80,206.6 86,205.9 94.2,205.5 104,206 116,207.4 128,209.5 140,211.7 152,213.7 164,214.8 170,215 182,214.2 194,211.6 206,206.9 218,199.5 230,189.1 242,175.4 254,158 266,136.6 278,110.9 290,80.5 302,45.1" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="94.1" cy="205.5" r="3.5" fill="#0f172a"/><circle cx="170" cy="215" r="3.5" fill="#0f172a"/><circle cx="50" cy="215" r="3.5" fill="#0f172a"/>
<g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">
<text x="42" y="229" text-anchor="end" fill="#0f172a">O</text>
<text x="88.1" y="231" text-anchor="middle" fill="#0f172a">1/e</text>
<text x="174" y="231" text-anchor="middle" fill="#0f172a">1</text>
<text x="44" y="209.5" text-anchor="end" fill="#0f172a">1/e²</text>
<text x="276" y="41.1" fill="#0f6e56">C</text>
</g></svg>
:::

::: exemple Une fonction auxiliaire : f(x) = 2 − x + (ln x)/x sur ]0, +∞[

1. **Limites.** En 0⁺ : (ln x)/x → −∞ (ln x → −∞, 1/x → +∞), donc f → −∞. En +∞ : (ln x)/x → 0, donc f(x) se comporte comme 2 − x et tend vers −∞.
2. **Dérivée.** f′(x) = −1 + (1 − ln x)/x² = (1 − x² − ln x)/x² = g(x)/x², avec **g(x) = 1 − x² − ln x**.
3. **Signe de g.** g′(x) = −2x − 1/x < 0 : g est strictement décroissante, et g(1) = 0. Donc g > 0 sur ]0, 1[ et g < 0 sur ]1, +∞[.
4. **Variations.** f croît sur ]0, 1] et décroît sur [1, +∞[ : maximum f(1) = 2 − 1 + 0 = 1.
5. **Asymptote et position.** f(x) − (2 − x) = (ln x)/x → 0 : la droite Δ : y = 2 − x est asymptote en +∞. Le signe de f − Δ est celui de ln x : la courbe est au-dessus de Δ pour x > 1, au-dessous pour 0 < x < 1.

:::

::: piege
**Erreur : lire le signe de f′ sur une expression où il n'est pas visible.** Ici f′(x) = (1 − x² − ln x)/x² : le numérateur mêle un polynôme et un logarithme, et aucun « signe évident » n'existe. Écrire que f′ > 0 « parce que 1 − x² > 0 » oublie le terme −ln x. La fonction auxiliaire g, étudiée avec sa propre dérivée, est la seule voie fiable.
:::

::: verifie À toi : une demi-tangente verticale
Soit f(x) = x ln x pour x > 0 et f(0) = 0. Étudier la dérivabilité de f en 0, puis le minimum de f.

---

Le taux (f(x) − f(0))/x = ln x tend vers −∞ quand x → 0⁺ : f n'est pas dérivable en 0, la courbe a une demi-tangente verticale à l'origine. Pour x > 0, f′(x) = ln x + 1 s'annule en 1/e, négative avant, positive après : le minimum vaut f(1/e) = (1/e) × (−1) = −1/e.
:::

::: retenir
Une étude à logarithme enchaîne limites par croissances comparées, dérivée via u′/u, fonction auxiliaire pour le signe de f′, asymptote et position par le signe de f moins la droite ; la dérivabilité en un point se juge par le taux d'accroissement.
:::

> 🏆 Huitième porte franchie, héros. L'aire sous 1/t, que les primitives du chapitre 6 ne donnaient pas, porte enfin un nom : ln. Tu sais la dériver, la primitiver, résoudre avec elle, et dompter ses limites. Il te reste un dernier échange : ln transforme les produits en sommes — quelle fonction fait le trajet inverse et change les sommes en produits ? Le chapitre 9 te présentera sa réciproque, l'exponentielle.
