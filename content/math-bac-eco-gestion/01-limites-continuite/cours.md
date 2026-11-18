# ⚔️ Limites et continuité — franchir le col sans lever le crayon

> 💡 «Une limite dit où va la courbe ; la continuité dit qu'elle y arrive sans sauter.»

Bienvenue, héros de la section Économie et gestion. Un coût moyen, un bénéfice, un tarif par paliers : pour les étudier, il faut savoir où va une fonction quand x s'approche d'une valeur ou grandit sans fin, et si sa courbe se trace d'un seul trait. Huit étapes t'y conduisent : limite en un point, calcul des limites, limites et ordre, limite d'une composée, continuité, valeurs intermédiaires, bijection et réciproque, lecture économique. Les polynômes, les fonctions rationnelles, √, sin et cos sont supposés connus.

## 🔭 Limite en un point et en l'infini : où va la courbe ?

Un opérateur téléphonique facture un forfait selon le volume x de données en Go : p(x) = 8 + 2x dinars si x < 5, et p(x) = 25 − x dinars si x ≥ 5.
Quand le volume s'approche de 5 Go, le prix se rapproche-t-il d'une seule valeur, qu'on pourrait appeler « le prix en 5 » ?

::: definition
Soit f une fonction définie près de a (sauf peut-être en a). **lim x→a f(x) = ℓ** signifie que f(x) se rapproche autant qu'on veut de ℓ quand x se rapproche de a ; ℓ est un réel, +∞ ou −∞.

La **limite à gauche** lim x→a⁻ f(x) ne regarde que les x < a ; la **limite à droite** lim x→a⁺ f(x) ne regarde que les x > a. On définit de même lim x→+∞ f(x) et lim x→−∞ f(x).
:::

::: figure À gauche de 5 le prix monte vers 18 (cercle vide), à droite il part de 20 (point plein) : deux valeurs voisines de 5 ne se rapprochent pas du même nombre
<svg viewBox="0 0 340 195"><title>Courbe du forfait : le prix tend vers 18 à gauche de 5 Go et part de 20 à droite</title><line x1="40" y1="170" x2="326" y2="170" stroke="#0f172a" stroke-width="1.6"/><line x1="44" y1="174" x2="44" y2="14" stroke="#0f172a" stroke-width="1.6"/><polygon points="326,170 319,166.5 319,173.5" fill="#0f172a"/><polygon points="44,14 40.5,21 47.5,21" fill="#0f172a"/><text x="318" y="164" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="52" y="24" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">p</text><line x1="216.5" y1="167" x2="216.5" y2="173" stroke="#0f172a" stroke-width="1.3"/><text x="216.5" y="185" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="41" y1="66.2" x2="47" y2="66.2" stroke="#0f172a" stroke-width="1.3"/><text x="38" y="70.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">18</text><line x1="41" y1="54.6" x2="47" y2="54.6" stroke="#0f172a" stroke-width="1.3"/><text x="38" y="58.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="44" y1="66.2" x2="216.5" y2="66.2" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><line x1="44" y1="54.6" x2="216.5" y2="54.6" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><line x1="216.5" y1="170" x2="216.5" y2="54.6" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><polyline points="44,123.8 130.2,95 216.5,66.2" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="216.5,54.6 268.2,63.3 320,71.9" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="216.5" cy="66.2" r="4" fill="#ffffff" stroke="#0f6e56" stroke-width="2.3"/><circle cx="216.5" cy="54.6" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="157.8" y="107.8" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">p(x) = 8 + 2x</text><text x="278.6" y="54.4" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">p(x) = 25 − x</text></svg>
:::

::: exemple Le forfait en x = 5 : p(x) = 8 + 2x si x < 5, p(x) = 25 − x si x ≥ 5
1. Pour x < 5, p(x) = 8 + 2x est un polynôme : lim x→5⁻ p(x) = 8 + 2 × 5 = 18.
2. Pour x > 5, p(x) = 25 − x est un polynôme : lim x→5⁺ p(x) = 25 − 5 = 20.
3. 18 ≠ 20 : les deux côtés ne s'accordent pas, donc p n'a pas de limite en 5, bien que p(5) = 20 existe.

:::

::: exemple Deux limites infinies : 1/(x − 2) et 3/(x − 2)² en 2
1. Près de 2, x − 2 est un très petit nombre : son inverse est très grand en valeur absolue, et son signe suit celui de x − 2.
2. À droite de 2, x − 2 > 0 : 1/(x − 2) tend vers +∞ ; à gauche, x − 2 < 0 : il tend vers −∞. Les deux côtés diffèrent : pas de limite en 2.
3. Dans 3/(x − 2)², le carré est positif des deux côtés : la limite est +∞ à gauche comme à droite, donc lim x→2 3/(x − 2)² = +∞.

:::

::: piege Croire que la limite en a est la valeur f(a)
Pour g(x) = (x² − 1)/(x − 1), g n'est pas définie en 1 et l'on conclut « pas de limite en 1 ». Cela tente parce que 0/0 n'a pas de sens. Mais la limite ne regarde que les x différents de 1 : pour ceux-là g(x) = x + 1, qui se rapproche de 2. Donc lim x→1 g(x) = 2, même si g(1) n'existe pas. Réciproquement, p(5) = 20 existe et p n'a pourtant pas de limite en 5.
:::

::: propriete
- lim x→a f(x) existe si et seulement si les limites à gauche et à droite en a existent et sont égales ; la limite est alors leur valeur commune.
- Limites de référence : lim x→±∞ 1/x = 0 ; lim x→0 1/x² = +∞ ; lim x→0⁺ 1/√x = +∞ ; lim x→+∞ √x = +∞ ; lim x→±∞ x² = +∞ ; lim x→+∞ x³ = +∞ et lim x→−∞ x³ = −∞.

Cas limite : x ↦ 1/x tend vers −∞ à gauche de 0 et vers +∞ à droite : elle n'a pas de limite en 0.
:::

::: verifie
Soit g(x) = 3x − 2 si x < 2, g(x) = 10 − 3x si x > 2, et g(2) = 7. Quelle est la limite de g en 2 ?

---

À gauche de 2, lim x→2⁻ (3x − 2) = 3 × 2 − 2 = 4. À droite, lim x→2⁺ (10 − 3x) = 10 − 6 = 4. Les deux limites sont égales : lim x→2 g(x) = 4. La valeur g(2) = 7 n'intervient pas, car la limite ne regarde que les x différents de 2.
:::

::: retenir
Une limite en a existe quand la limite à gauche et la limite à droite sont égales, quelle que soit la valeur de f en a.
:::

## ➕ Calculer une limite : opérations, polynômes et fonctions rationnelles

Une conserverie calcule le coût moyen de fabrication d'une boîte, en dinars, pour x milliers de boîtes : CM(x) = (5x² + 3x + 200)/(x² + 10).
Quand la production devient énorme, le coût moyen se stabilise-t-il ? Au numérateur comme au dénominateur, x² tend vers +∞ : que peut-on écrire d'un quotient « +∞ sur +∞ » ?

::: exemple Limite en +∞ du coût moyen CM(x) = (5x² + 3x + 200)/(x² + 10)
1. Le numérateur et le dénominateur tendent tous deux vers +∞ : le quotient se présente sous la forme ∞/∞, sans conclusion directe.
2. On factorise le terme de plus haut degré : CM(x) = x²(5 + 3/x + 200/x²) / (x²(1 + 10/x²)), puis on simplifie par x² ≠ 0.
3. Il reste (5 + 3/x + 200/x²)/(1 + 10/x²), où 3/x, 200/x² et 10/x² tendent vers 0.
4. Donc lim x→+∞ CM(x) = 5/1 = 5 : le coût moyen se stabilise autour de 5 dinars la boîte.

:::

::: exemple Lever un 0/0 puis un ∞ − ∞
1. lim x→3 (x² − 9)/(x − 3) : numérateur et dénominateur tendent vers 0. On factorise x² − 9 = (x − 3)(x + 3), puis on simplifie par x − 3 ≠ 0 : on obtient x + 3, de limite 6.
2. lim x→+∞ (x − (x² + 1)/(x + 2)) donne ∞ − ∞. On réduit au même dénominateur : (x(x + 2) − (x² + 1))/(x + 2) = (2x − 1)/(x + 2).
3. Ce quotient a pour limite 2/1 = 2 (rapport des termes de plus haut degré) : lim x→+∞ (x − (x² + 1)/(x + 2)) = 2.

:::

::: exemple Un ∞ − ∞ avec une racine : lim x→+∞ (√(x² + 4x) − x)
1. √(x² + 4x) et x tendent tous deux vers +∞ : la différence se présente sous la forme ∞ − ∞.
2. On multiplie et on divise par la quantité conjuguée √(x² + 4x) + x : on obtient (x² + 4x − x²)/(√(x² + 4x) + x) = 4x/(√(x² + 4x) + x).
3. Pour x > 0, √(x² + 4x) = x√(1 + 4/x), donc le quotient vaut 4x/(x(√(1 + 4/x) + 1)) = 4/(√(1 + 4/x) + 1).
4. Comme 4/x tend vers 0, la limite vaut 4/(1 + 1) = 2.

:::

::: exemple Un dénominateur qui tend vers 0 : lim x→2⁺ (x + 1)/(x − 2)
1. Le numérateur x + 1 tend vers 3, qui est positif.
2. À droite de 2, x − 2 est positif et tend vers 0 : on note 0⁺.
3. Un nombre proche de 3 divisé par un très petit nombre positif est très grand et positif : la limite est +∞. Si l'on approchait par la gauche, le dénominateur serait négatif et la limite serait −∞.

:::

::: piege Écrire « +∞ − ∞ = 0 » ou « ∞/∞ = 1 »
Dans x − (x² + 1)/(x + 2), on lit « x tend vers +∞, l'autre terme aussi, donc leur différence tend vers 0 ». Cela tente parce que deux quantités qui grandissent ensemble semblent se compenser. Pourtant la différence peut valoir n'importe quoi : ici elle tend vers 2, et x − x² tend vers −∞. Un résultat de la forme « +∞ − ∞ », « 0 × ∞ », « ∞/∞ » ou « 0/0 » n'a pas de valeur imposée : on transforme l'écriture avant de conclure.
:::

::: propriete
- Somme, produit, quotient : si les limites sont des réels, on effectue l'opération sur les limites (quotient : dénominateur de limite non nulle). Si une limite est infinie, la règle des signes donne l'infini, sauf dans les quatre cas sans conclusion : +∞ − ∞, 0 × ∞, ∞/∞ et 0/0.
- Une différence contenant une racine carrée se transforme par la quantité conjuguée : a − b devient (a² − b²)/(a + b).
- Une fonction polynôme a en ±∞ la limite de son terme de plus haut degré.
- Une fonction rationnelle a en ±∞ la limite du quotient de ses termes de plus haut degré : 0 si le numérateur est de degré plus petit, le quotient des coefficients si les degrés sont égaux, ±∞ si le numérateur est de degré plus grand.

Cas limite : cette règle du plus haut degré ne vaut qu'en ±∞. En un point fini comme 3, on factorise pour lever le 0/0. Autre précaution : √(x²) = |x|, qui vaut −x pour x < 0 ; en −∞, √(x² + x) = −x√(1 + 1/x), et non x√(1 + 1/x).
:::

::: verifie
Calculer lim x→−∞ (9x² + x)/(3x² − 4).

---

Au numérateur et au dénominateur, les termes de plus haut degré sont 9x² et 3x², de même degré : la limite est le quotient des coefficients, 9/3 = 3. On peut le vérifier en factorisant x² : (9 + 1/x)/(3 − 4/x²) tend vers 9/3 = 3, car 1/x et 4/x² tendent vers 0 en −∞.
:::

::: retenir
Un quotient ∞/∞ ou 0/0, une différence ∞ − ∞ se transforment avant de conclure ; en ±∞, on garde le terme de plus haut degré.
:::

## 🛡️ Limites et ordre : coincer une fonction

Les ventes mensuelles d'une boutique de cadeaux, en milliers de dinars, oscillent autour d'un niveau : v(t) = 12 + (sin t)/t pour t mois après l'ouverture, t > 0.
Le sinus oscille sans jamais se fixer : on ne peut pas écrire sa limite en +∞. Mais ses valeurs restent entre −1 et 1. Cela suffit-il à connaître le niveau vers lequel se stabilisent les ventes ?

::: figure La courbe de v oscille mais reste coincée entre 12 − 1/t et 12 + 1/t, qui se resserrent autour de 12
<svg viewBox="0 0 350 195"><title>La courbe de v reste coincée entre 12 − 1/t et 12 + 1/t, qui tendent vers 12</title><line x1="46" y1="170" x2="336" y2="170" stroke="#0f172a" stroke-width="1.6"/><line x1="50" y1="174" x2="50" y2="14" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,170 329,166.5 329,173.5" fill="#0f172a"/><polygon points="50,14 46.5,21 53.5,21" fill="#0f172a"/><text x="328" y="164" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t</text><text x="58" y="24" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v</text><line x1="103.3" y1="167" x2="103.3" y2="173" stroke="#0f172a" stroke-width="1.3"/><text x="103.3" y="185" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="170" y1="167" x2="170" y2="173" stroke="#0f172a" stroke-width="1.3"/><text x="170" y="185" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="236.7" y1="167" x2="236.7" y2="173" stroke="#0f172a" stroke-width="1.3"/><text x="236.7" y="185" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">15</text><line x1="303.3" y1="167" x2="303.3" y2="173" stroke="#0f172a" stroke-width="1.3"/><text x="303.3" y="185" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="47" y1="157.5" x2="53" y2="157.5" stroke="#0f172a" stroke-width="1.3"/><text x="44" y="161.5" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">11</text><line x1="47" y1="95" x2="53" y2="95" stroke="#0f172a" stroke-width="1.3"/><text x="44" y="99" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12</text><line x1="47" y1="32.5" x2="53" y2="32.5" stroke="#0f172a" stroke-width="1.3"/><text x="44" y="36.5" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">13</text><line x1="50" y1="95" x2="330" y2="95" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="2 3"/><polyline points="50,32.5 52.3,41.8 54.7,48.7 57,54 59.3,58.2 61.7,61.7 64,64.5 66.3,66.9 68.7,69 71,70.7 73.3,72.3 75.7,73.6 78,74.8 80.3,75.9 82.7,76.9 85,77.8 87.3,78.6 89.7,79.3 92,79.9 94.3,80.5 96.7,81.1 99,81.6 101.3,82.1 103.7,82.6 106,83 108.3,83.4 110.7,83.7 113,84.1 115.3,84.4 117.7,84.7 120,85 122.3,85.3 124.7,85.5 127,85.8 129.3,86 131.7,86.2 134,86.4 136.3,86.6 138.7,86.8 141,87 143.3,87.2 145.7,87.4 148,87.5 150.3,87.7 152.7,87.8 155,88 157.3,88.1 159.7,88.2 162,88.4 164.3,88.5 166.7,88.6 169,88.7 171.3,88.8 173.7,88.9 176,89 178.3,89.1 180.7,89.2 183,89.3 185.3,89.4 187.7,89.5 190,89.6 192.3,89.6 194.7,89.7 197,89.8 199.3,89.9 201.7,89.9 204,90 206.3,90.1 208.7,90.2 211,90.2 213.3,90.3 215.7,90.3 218,90.4 220.3,90.5 222.7,90.5 225,90.6 227.3,90.6 229.7,90.7 232,90.7 234.3,90.8 236.7,90.8 239,90.9 241.3,90.9 243.7,91 246,91 248.3,91.1 250.7,91.1 253,91.1 255.3,91.2 257.7,91.2 260,91.3 262.3,91.3 264.7,91.3 267,91.4 269.3,91.4 271.7,91.5 274,91.5 276.3,91.5 278.7,91.6 281,91.6 283.3,91.6 285.7,91.7 288,91.7 290.3,91.7 292.7,91.7 295,91.8 297.3,91.8 299.7,91.8 302,91.9 304.3,91.9 306.7,91.9 309,91.9 311.3,92 313.7,92 316,92 318.3,92 320.7,92.1 323,92.1 325.3,92.1 327.7,92.1 330,92.2" fill="none" stroke="#b45309" stroke-width="2.0" stroke-dasharray="5 3" stroke-linejoin="round" stroke-linecap="round"/><polyline points="50,157.5 52.3,148.2 54.7,141.3 57,136 59.3,131.8 61.7,128.3 64,125.5 66.3,123.1 68.7,121 71,119.3 73.3,117.7 75.7,116.4 78,115.2 80.3,114.1 82.7,113.1 85,112.2 87.3,111.4 89.7,110.7 92,110.1 94.3,109.5 96.7,108.9 99,108.4 101.3,107.9 103.7,107.4 106,107 108.3,106.6 110.7,106.3 113,105.9 115.3,105.6 117.7,105.3 120,105 122.3,104.7 124.7,104.5 127,104.2 129.3,104 131.7,103.8 134,103.6 136.3,103.4 138.7,103.2 141,103 143.3,102.8 145.7,102.6 148,102.5 150.3,102.3 152.7,102.2 155,102 157.3,101.9 159.7,101.8 162,101.6 164.3,101.5 166.7,101.4 169,101.3 171.3,101.2 173.7,101.1 176,101 178.3,100.9 180.7,100.8 183,100.7 185.3,100.6 187.7,100.5 190,100.4 192.3,100.4 194.7,100.3 197,100.2 199.3,100.1 201.7,100.1 204,100 206.3,99.9 208.7,99.8 211,99.8 213.3,99.7 215.7,99.7 218,99.6 220.3,99.5 222.7,99.5 225,99.4 227.3,99.4 229.7,99.3 232,99.3 234.3,99.2 236.7,99.2 239,99.1 241.3,99.1 243.7,99 246,99 248.3,98.9 250.7,98.9 253,98.9 255.3,98.8 257.7,98.8 260,98.7 262.3,98.7 264.7,98.7 267,98.6 269.3,98.6 271.7,98.5 274,98.5 276.3,98.5 278.7,98.4 281,98.4 283.3,98.4 285.7,98.3 288,98.3 290.3,98.3 292.7,98.3 295,98.2 297.3,98.2 299.7,98.2 302,98.1 304.3,98.1 306.7,98.1 309,98.1 311.3,98 313.7,98 316,98 318.3,98 320.7,97.9 323,97.9 325.3,97.9 327.7,97.9 330,97.8" fill="none" stroke="#b45309" stroke-width="2.0" stroke-dasharray="5 3" stroke-linejoin="round" stroke-linecap="round"/><polyline points="50,42.4 51.1,44 52.2,45.6 53.2,47.4 54.3,49.2 55.4,51.1 56.5,53.1 57.5,55.1 58.6,57.1 59.7,59.2 60.8,61.4 61.8,63.6 62.9,65.7 64,67.9 65.1,70.1 66.2,72.3 67.2,74.5 68.3,76.7 69.4,78.8 70.5,80.9 71.5,83 72.6,85 73.7,87 74.8,88.9 75.8,90.7 76.9,92.5 78,94.2 79.1,95.8 80.2,97.3 81.2,98.7 82.3,100.1 83.4,101.3 84.5,102.5 85.5,103.5 86.6,104.5 87.7,105.3 88.8,106.1 89.8,106.7 90.9,107.3 92,107.7 93.1,108.1 94.2,108.3 95.2,108.5 96.3,108.6 97.4,108.6 98.5,108.4 99.5,108.3 100.6,108 101.7,107.6 102.8,107.2 103.8,106.8 104.9,106.2 106,105.6 107.1,105 108.2,104.3 109.2,103.6 110.3,102.8 111.4,102 112.5,101.2 113.5,100.4 114.6,99.5 115.7,98.7 116.8,97.8 117.8,97 118.9,96.2 120,95.3 121.1,94.5 122.2,93.8 123.2,93 124.3,92.3 125.4,91.6 126.5,91 127.5,90.3 128.6,89.8 129.7,89.3 130.8,88.8 131.8,88.4 132.9,88 134,87.7 135.1,87.5 136.2,87.3 137.2,87.1 138.3,87 139.4,87 140.5,87 141.5,87.1 142.6,87.2 143.7,87.3 144.8,87.5 145.8,87.8 146.9,88.1 148,88.4 149.1,88.8 150.2,89.2 151.2,89.6 152.3,90.1 153.4,90.6 154.5,91.1 155.5,91.6 156.6,92.1 157.7,92.7 158.8,93.2 159.8,93.7 160.9,94.3 162,94.8 163.1,95.4 164.2,95.9 165.2,96.4 166.3,96.9 167.4,97.4 168.5,97.8 169.5,98.2 170.6,98.6 171.7,99 172.8,99.3 173.8,99.6 174.9,99.9 176,100.1 177.1,100.3 178.2,100.5 179.2,100.6 180.3,100.7 181.4,100.7 182.5,100.7 183.5,100.7 184.6,100.6 185.7,100.5 186.8,100.4 187.8,100.2 188.9,100 190,99.8 191.1,99.5 192.2,99.2 193.2,98.9 194.3,98.6 195.4,98.2 196.5,97.9 197.5,97.5 198.6,97.1 199.7,96.7 200.8,96.3 201.8,95.9 202.9,95.5 204,95.1 205.1,94.7 206.2,94.3 207.2,93.9 208.3,93.5 209.4,93.2 210.5,92.8 211.5,92.5 212.6,92.2 213.7,91.9 214.8,91.7 215.8,91.4 216.9,91.2 218,91.1 219.1,90.9 220.2,90.8 221.2,90.7 222.3,90.6 223.4,90.6 224.5,90.6 225.5,90.6 226.6,90.6 227.7,90.7 228.8,90.8 229.8,90.9 230.9,91.1 232,91.3 233.1,91.5 234.2,91.7 235.2,91.9 236.3,92.2 237.4,92.5 238.5,92.8 239.5,93.1 240.6,93.4 241.7,93.7 242.8,94 243.8,94.3 244.9,94.6 246,95 247.1,95.3 248.2,95.6 249.2,95.9 250.3,96.2 251.4,96.5 252.5,96.8 253.5,97 254.6,97.3 255.7,97.5 256.8,97.7 257.8,97.9 258.9,98.1 260,98.2 261.1,98.3 262.2,98.4 263.2,98.5 264.3,98.6 265.4,98.6 266.5,98.6 267.5,98.6 268.6,98.6 269.7,98.5 270.8,98.4 271.8,98.3 272.9,98.2 274,98 275.1,97.9 276.2,97.7 277.2,97.5 278.3,97.3 279.4,97.1 280.5,96.8 281.5,96.6 282.6,96.3 283.7,96.1 284.8,95.8 285.8,95.5 286.9,95.3 288,95 289.1,94.7 290.2,94.5 291.2,94.2 292.3,94 293.4,93.7 294.5,93.5 295.5,93.3 296.6,93.1 297.7,92.9 298.8,92.7 299.8,92.5 300.9,92.4 302,92.3 303.1,92.2 304.2,92.1 305.2,92 306.3,92 307.4,91.9 308.5,91.9 309.5,91.9 310.6,92 311.7,92 312.8,92.1 313.8,92.2 314.9,92.3 316,92.4 317.1,92.6 318.2,92.7 319.2,92.9 320.3,93.1 321.4,93.3 322.5,93.5 323.5,93.7 324.6,93.9 325.7,94.1 326.8,94.3 327.8,94.6 328.9,94.8 330,95" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="156.7" y="80.1" text-anchor="middle" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12 + 1/t</text><text x="156.7" y="118.9" text-anchor="middle" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12 − 1/t</text><text x="86" y="119.9" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v(t)</text></svg>
:::

::: exemple Limite en +∞ de v(t) = 12 + (sin t)/t
1. Pour tout réel t, −1 ≤ sin t ≤ 1 : le sinus est encadré par deux constantes.
2. On divise par t > 0, ce qui conserve le sens des inégalités : −1/t ≤ (sin t)/t ≤ 1/t.
3. On ajoute 12 aux trois membres : 12 − 1/t ≤ v(t) ≤ 12 + 1/t.
4. Les deux bornes ont pour limite 12 en +∞, car 1/t tend vers 0. Les ventes sont coincées entre elles : lim t→+∞ v(t) = 12.

:::

::: exemple Une minoration suffit pour +∞ : f(x) = 2x + cos x
1. Pour tout x, cos x ≥ −1, donc f(x) ≥ 2x − 1.
2. La fonction x ↦ 2x − 1 tend vers +∞ quand x tend vers +∞.
3. Une fonction supérieure à une fonction qui tend vers +∞ tend aussi vers +∞ : lim x→+∞ f(x) = +∞, sans avoir besoin d'une limite pour cos x.

:::

::: piege Une seule borne, et l'on croit tenir la limite
Pour une fonction f vérifiant f(x) ≤ 10/x pour tout x > 0, on conclut « f est plus petite qu'une fonction qui tend vers 0, donc f tend vers 0 ». Cela tente parce que 10/x tend vers 0. Mais f(x) = −x vérifie bien −x ≤ 10/x, et tend vers −∞ ; la fonction f(x) = −1 + sin x vérifie aussi l'inégalité et n'a pas de limite. Une seule borne ne fixe pas la limite : il en faut une de chaque côté, de même limite.
:::

::: propriete
Soit I un intervalle ouvert contenant x0 ou ayant x0 pour borne (x0 peut être ±∞).
- **Encadrement** : si h(x) ≤ f(x) ≤ g(x) sur I et si h et g ont la même limite ℓ en x0, alors f a pour limite ℓ en x0.
- **Minoration** : si f(x) ≥ h(x) et lim h = +∞, alors lim f = +∞. **Majoration** : si f(x) ≤ h(x) et lim h = −∞, alors lim f = −∞.
- **Comparaison** : si f(x) ≤ g(x) et si f et g ont des limites ℓ et ℓ', alors ℓ ≤ ℓ'.

Cas limite : avec une inégalité stricte f(x) < g(x), on obtient seulement ℓ ≤ ℓ', pas ℓ < ℓ' : par exemple 0 < 1/x pour x > 0, et pourtant les deux limites en +∞ valent 0.
:::

::: verifie
Soit h(x) = 5 + (cos x)/√x pour x > 0. Déterminer lim x→+∞ h(x).

---

Pour tout x > 0, −1 ≤ cos x ≤ 1. En divisant par √x > 0 : −1/√x ≤ (cos x)/√x ≤ 1/√x, puis en ajoutant 5 : 5 − 1/√x ≤ h(x) ≤ 5 + 1/√x. Les deux bornes tendent vers 5 quand x tend vers +∞, donc lim x→+∞ h(x) = 5.
:::

::: retenir
On encadre par deux fonctions de même limite pour une limite finie ; une minoration par une fonction qui tend vers +∞ (une majoration par une fonction qui tend vers −∞) suffit pour l'infini.
:::

## 🔗 Limite d'une fonction composée

Le prix de vente conseillé d'un article s'écrit p(x) = √((9x + 1)/(x + 1)) dinars, où x est le stock en centaines de pièces.
Quand le stock devient très grand, vers quelle valeur se stabilise le prix ? La racine porte sur un quotient qui n'est pas lui-même un prix : comment enchaîner deux limites ?

::: definition
Soit f une fonction définie sur I et g une fonction définie sur J avec f(I) ⊂ J. La **fonction composée g∘f** est définie sur I par (g∘f)(x) = g(f(x)) : on applique f d'abord, puis g. En général g∘f ≠ f∘g.
:::

::: exemple Limite en +∞ du prix p(x) = √((9x + 1)/(x + 1))
1. On pose u(x) = (9x + 1)/(x + 1) et g(y) = √y, de sorte que p = g∘u.
2. Les termes de plus haut degré donnent lim x→+∞ u(x) = 9/1 = 9, et u(x) > 0 pour x > 0.
3. La racine carrée a pour limite √9 = 3 quand y tend vers 9.
4. On enchaîne : lim x→+∞ p(x) = 3. Le prix se stabilise à 3 dinars.

:::

::: exemple Deux composées à carré et à cube
1. lim x→2⁺ (3/(x − 2))² : u(x) = 3/(x − 2) tend vers +∞ (numérateur positif, dénominateur 0⁺), et g(y) = y² tend vers +∞ quand y tend vers +∞ : la limite est +∞.
2. lim x→−∞ (1 − 2x²)³ : u(x) = 1 − 2x² tend vers −∞ (terme de plus haut degré −2x²), et g(y) = y³ tend vers −∞ quand y tend vers −∞ : la limite est −∞.

:::

::: piege Appliquer une racine sans regarder où la composée existe
Pour f(x) = √(2 − x), on écrit « 2 − x tend vers −∞ en +∞, donc √(2 − x) tend vers √(−∞) ». Cela tente parce que 2 − x a bien une limite. Mais √ n'est définie que pour les nombres positifs ou nuls : f n'existe que pour x ≤ 2, donc il n'y a aucune limite à chercher en +∞. En −∞, au contraire, 2 − x tend vers +∞ et lim x→−∞ √(2 − x) = +∞.
:::

::: propriete
- Si lim x→a f(x) = b et lim y→b g(y) = L, alors lim x→a g(f(x)) = L ; a, b et L sont des réels ou ±∞.
- Cas de la racine : si f(x) ≥ 0 et lim f = L (réel), alors lim √f = √L ; si lim f = +∞, alors lim √f = +∞.
- Limites de référence en 0 : lim x→0 (sin x)/x = 1 ; lim x→0 (1 − cos x)/x = 0 ; lim x→0 (1 − cos x)/x² = 1/2. Par composée, lim x→0 (sin 3x)/(3x) = 1, car u(x) = 3x tend vers 0.

Cas limite : le théorème exige que g∘f soit définie près de a. Dans √(1 − x²) en +∞, rien à calculer, le domaine est [−1 ; 1].
:::

::: verifie
Calculer lim x→+∞ √((16x + 5)/(4x − 1)).

---

On pose u(x) = (16x + 5)/(4x − 1) et g(y) = √y. Le quotient des termes de plus haut degré donne lim x→+∞ u(x) = 16/4 = 4, et u(x) est positif pour x grand. La racine a pour limite √4 = 2 en 4 : lim x→+∞ √((16x + 5)/(4x − 1)) = 2.
:::

::: retenir
Pour une composée g(f(x)), on calcule d'abord la limite b de f, puis la limite de g en b, après avoir vérifié que la composée existe.
:::

## 🧵 Continuité : sans lever le crayon

Une société de livraison facture un colis de m kg : L(m) = 3m + 2 dinars si m ≤ 4, et L(m) = 2m + 6 dinars si m > 4.
Entre 3,99 kg et 4,01 kg, la facture reste-t-elle voisine de 14 dinars, ou saute-t-elle d'un coup ? « Sans lever le crayon » ne suffit pas pour trancher : il faut le dire avec des limites.

::: definition
Soit f définie sur un intervalle contenant a. **f est continue en a** si lim x→a f(x) = f(a).

**f est continue à droite en a** si lim x→a⁺ f(x) = f(a) ; **continue à gauche en a** si lim x→a⁻ f(x) = f(a). **f est continue sur un intervalle I** si elle est continue en tout point de I (à droite ou à gauche aux bornes de I qui lui appartiennent).
:::

::: figure En A les deux morceaux se raccordent au point (4 ; 14) ; en B la courbe saute de 14 à 16 : seule la courbe A se trace sans lever le crayon
<svg viewBox="0 0 370 185"><title>Deux tarifs : en A les deux morceaux se raccordent en 14, en B la courbe saute de 14 à 16</title><line x1="36" y1="150" x2="176" y2="150" stroke="#0f172a" stroke-width="1.6"/><line x1="40" y1="154" x2="40" y2="14" stroke="#0f172a" stroke-width="1.6"/><polygon points="176,150 169,146.5 169,153.5" fill="#0f172a"/><polygon points="40,14 36.5,21 43.5,21" fill="#0f172a"/><text x="168" y="144" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">m</text><text x="48" y="24" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">L</text><line x1="114.3" y1="147" x2="114.3" y2="153" stroke="#0f172a" stroke-width="1.3"/><text x="114.3" y="165" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="37" y1="74.2" x2="43" y2="74.2" stroke="#0f172a" stroke-width="1.3"/><text x="34" y="78.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">14</text><line x1="40" y1="74.2" x2="114.3" y2="74.2" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><line x1="114.3" y1="150" x2="114.3" y2="74.2" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><polyline points="40,139.2 77.1,106.7 114.3,74.2" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="114.3,74.2 142.1,57.9 170,41.7" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="114.3" cy="74.2" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="105" y="12" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A : pas de saut</text><line x1="211" y1="150" x2="351" y2="150" stroke="#0f172a" stroke-width="1.6"/><line x1="215" y1="154" x2="215" y2="14" stroke="#0f172a" stroke-width="1.6"/><polygon points="351,150 344,146.5 344,153.5" fill="#0f172a"/><polygon points="215,14 211.5,21 218.5,21" fill="#0f172a"/><text x="343" y="144" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">m</text><text x="223" y="24" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">L</text><line x1="289.3" y1="147" x2="289.3" y2="153" stroke="#0f172a" stroke-width="1.3"/><text x="289.3" y="165" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="212" y1="74.2" x2="218" y2="74.2" stroke="#0f172a" stroke-width="1.3"/><text x="209" y="78.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">14</text><line x1="212" y1="63.3" x2="218" y2="63.3" stroke="#0f172a" stroke-width="1.3"/><text x="209" y="67.3" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">16</text><line x1="215" y1="74.2" x2="289.3" y2="74.2" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><line x1="215" y1="63.3" x2="289.3" y2="63.3" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><line x1="289.3" y1="150" x2="289.3" y2="63.3" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><polyline points="215,139.2 252.1,106.7 289.3,74.2" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="289.3,63.3 317.1,47.1 345,30.8" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="289.3" cy="74.2" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="289.3" cy="63.3" r="4" fill="#ffffff" stroke="#0f6e56" stroke-width="2.3"/><text x="280" y="12" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B : un saut</text></svg>
:::

::: exemple La facture L en m = 4 : L(m) = 3m + 2 si m ≤ 4, L(m) = 2m + 6 si m > 4
1. À gauche, 3m + 2 est un polynôme : lim m→4⁻ L(m) = 3 × 4 + 2 = 14.
2. À droite, 2m + 6 est un polynôme : lim m→4⁺ L(m) = 2 × 4 + 6 = 14.
3. La valeur en 4 vient de la première formule, car 4 ≤ 4 : L(4) = 14.
4. Limite à gauche, limite à droite et L(4) valent 14 : L est continue en 4, la facture ne saute pas.

:::

::: exemple Choisir un paramètre pour raccorder : h(x) = 2x + 1 si x < 3, h(x) = x² − a si x ≥ 3
1. À gauche de 3, 2x + 1 est un polynôme : lim x→3⁻ h(x) = 2 × 3 + 1 = 7.
2. À droite, h(x) = x² − a, et h(3) = 9 − a (la seconde formule porte l'égalité).
3. La continuité en 3 exige 9 − a = 7, donc a = 2.
4. Les polynômes sont continus sur chaque morceau : avec a = 2, h est continue sur ℝ.

:::

::: exemple Où une fonction est-elle continue : f(x) = (3x + 2)/(x² − x − 6)
1. x² − x − 6 = (x − 3)(x + 2) s'annule en 3 et en −2 : f est définie sur ℝ privé de {−2 ; 3}.
2. f est une fonction rationnelle, donc continue sur chaque intervalle de son ensemble de définition : ]−∞ ; −2[, ]−2 ; 3[ et ]3 ; +∞[.
3. Pour une composée comme k(x) = √(x² − 5) en x = 3 : x ↦ x² − 5 est continue en 3, vaut 4 ≥ 0 en 3, et √ est continue en 4 : k est continue en 3.

:::

::: piege Comparer les deux limites mais oublier la valeur en a
Soit q(x) = 4x − 3 si x < 2, q(x) = 13 − 4x si x > 2, et q(2) = 7. On trouve lim x→2⁻ q(x) = 5 et lim x→2⁺ q(x) = 5 et l'on conclut « q est continue en 2 ». Cela tente parce que les deux côtés se rejoignent. Mais la continuité compare ces limites à q(2) = 7 : 5 ≠ 7, la courbe a un trou en (2 ; 5) et un point isolé en (2 ; 7). q n'est pas continue en 2.
:::

::: propriete
- f est continue en a si et seulement si lim x→a⁻ f(x) = lim x→a⁺ f(x) = f(a).
- Somme, produit, produit par un réel, valeur absolue, quotient (dénominateur non nul) et √f (f ≥ 0) de fonctions continues sont continus. Toute fonction polynôme est continue sur ℝ ; toute fonction rationnelle est continue sur chaque intervalle de son ensemble de définition.
- Composée : si f est continue en x0 et g est continue en f(x0), alors g∘f est continue en x0.

Cas limite : ℝ privé de {3} n'est pas un intervalle. Pour appliquer les théorèmes du chapitre (valeurs intermédiaires, bijection), on travaille sur ]−∞ ; 3[ et sur ]3 ; +∞[ séparément.
:::

::: verifie
Soit k(x) = 5 − x si x ≤ 2, et k(x) = x² − b si x > 2. Pour quelle valeur de b la fonction k est-elle continue en 2 ?

---

À gauche, la formule 5 − x porte l'égalité : k(2) = 3 et lim x→2⁻ k(x) = 3. À droite, lim x→2⁺ (x² − b) = 4 − b. La continuité en 2 impose 4 − b = 3, donc b = 1. On a comparé les deux limites avec k(2).
:::

::: retenir
f est continue en a quand limite à gauche, limite à droite et f(a) sont égales ; pour une fonction définie par morceaux, on contrôle les deux côtés et la valeur en a.
:::

## 🌉 Valeurs intermédiaires et dichotomie

Un atelier de maroquinerie produit q dizaines de sacs par mois ; son bénéfice mensuel, en milliers de dinars, est B(q) = −q² + 14q − 20.
Avec 1 dizaine de sacs, B(1) = −7 : l'atelier perd de l'argent. Avec 2 dizaines, B(2) = 4 : il gagne. Entre les deux, le bénéfice passe-t-il forcément par 0, et où se trouve ce seuil de rentabilité ?

::: figure La courbe de B passe du point B(1) sous l'axe au point B(2) au-dessus : sans saut, elle coupe l'axe des abscisses entre 1 et 2, en α
<svg viewBox="0 0 355 195"><title>La courbe de B passe de B(1) négatif à B(2) positif : elle coupe l'axe des abscisses entre 1 et 2</title><line x1="44" y1="106.9" x2="341" y2="106.9" stroke="#0f172a" stroke-width="1.6"/><line x1="48" y1="174" x2="48" y2="9" stroke="#0f172a" stroke-width="1.6"/><polygon points="341,106.9 334,103.4 334,110.4" fill="#0f172a"/><polygon points="48,9 44.5,16 51.5,16" fill="#0f172a"/><text x="333" y="100.9" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">q</text><text x="56" y="19" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><line x1="130" y1="103.9" x2="130" y2="109.9" stroke="#0f172a" stroke-width="1.3"/><text x="130" y="121.9" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="212" y1="103.9" x2="212" y2="109.9" stroke="#0f172a" stroke-width="1.3"/><text x="212" y="121.9" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="294" y1="103.9" x2="294" y2="109.9" stroke="#0f172a" stroke-width="1.3"/><text x="294" y="121.9" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12</text><line x1="45" y1="78.1" x2="51" y2="78.1" stroke="#0f172a" stroke-width="1.3"/><text x="42" y="82.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="45" y1="49.4" x2="51" y2="49.4" stroke="#0f172a" stroke-width="1.3"/><text x="42" y="53.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="45" y1="20.7" x2="51" y2="20.7" stroke="#0f172a" stroke-width="1.3"/><text x="42" y="24.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><line x1="45" y1="135.6" x2="51" y2="135.6" stroke="#0f172a" stroke-width="1.3"/><text x="42" y="139.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−10</text><line x1="45" y1="164.3" x2="51" y2="164.3" stroke="#0f172a" stroke-width="1.3"/><text x="42" y="168.3" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−20</text><polyline points="48,164.3 50.9,158.7 53.7,153.2 56.6,147.9 59.5,142.7 62.4,137.5 65.2,132.5 68.1,127.6 71,122.9 73.8,118.2 76.7,113.6 79.6,109.2 82.4,104.8 85.3,100.6 88.2,96.5 91,92.5 93.9,88.6 96.8,84.9 99.7,81.2 102.5,77.7 105.4,74.2 108.3,70.9 111.1,67.7 114,64.6 116.9,61.6 119.8,58.8 122.6,56 125.5,53.4 128.4,50.8 131.2,48.4 134.1,46.1 137,43.9 139.8,41.8 142.7,39.9 145.6,38 148.4,36.3 151.3,34.6 154.2,33.1 157.1,31.7 159.9,30.4 162.8,29.2 165.7,28.2 168.5,27.2 171.4,26.4 174.3,25.6 177.2,25 180,24.5 182.9,24.1 185.8,23.8 188.6,23.7 191.5,23.6 194.4,23.7 197.2,23.8 200.1,24.1 203,24.5 205.9,25 208.7,25.6 211.6,26.4 214.5,27.2 217.3,28.2 220.2,29.2 223.1,30.4 225.9,31.7 228.8,33.1 231.7,34.6 234.6,36.3 237.4,38 240.3,39.9 243.2,41.8 246,43.9 248.9,46.1 251.8,48.4 254.6,50.8 257.5,53.4 260.4,56 263.2,58.8 266.1,61.6 269,64.6 271.9,67.7 274.7,70.9 277.6,74.2 280.5,77.7 283.3,81.2 286.2,84.9 289.1,88.6 291.9,92.5 294.8,96.5 297.7,100.6 300.6,104.8 303.4,109.2 306.3,113.6 309.2,118.2 312,122.9 314.9,127.6 317.8,132.5 320.7,137.5 323.5,142.7 326.4,147.9 329.3,153.2 332.1,158.7 335,164.3" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="68.5" cy="126.9" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="89" cy="95.4" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="81.1" cy="106.9" r="4" fill="#ffffff" stroke="#b45309" stroke-width="2.3"/><circle cx="301.9" cy="106.9" r="4" fill="#ffffff" stroke="#b45309" stroke-width="2.3"/><text x="80.5" y="142.9" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B(1)</text><text x="81" y="89.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B(2)</text><text x="81.1" y="123.9" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">α</text><text x="301.9" y="97.9" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">β</text></svg>
:::

::: exemple Un seuil de rentabilité entre 1 et 2 : B(q) = −q² + 14q − 20
1. B est un polynôme, donc continue sur [1 ; 2].
2. B(1) = −1 + 14 − 20 = −7 < 0 et B(2) = −4 + 28 − 20 = 4 > 0 : 0 est entre B(1) et B(2).
3. Une fonction continue prend toutes les valeurs entre B(1) et B(2) : l'équation B(q) = 0 a au moins une solution α dans ]1 ; 2[.
4. Sur [1 ; 2], B(q) = 29 − (q − 7)², et (q − 7)² décroît (q − 7 reste négatif et augmente) : B est strictement croissante, donc α est unique.

:::

::: exemple Dichotomie : encadrer α en coupant [1 ; 2] en deux, trois fois
1. Le milieu de [1 ; 2] est 1,5 : B(1,5) = −2,25 + 21 − 20 = −1,25 < 0, de même signe que B(1) ; donc α est dans [1,5 ; 2].
2. Le milieu de [1,5 ; 2] est 1,75 : B(1,75) = −3,0625 + 24,5 − 20 = 1,4375 > 0, de même signe que B(2) ; donc α est dans [1,5 ; 1,75].
3. Le milieu de [1,5 ; 1,75] est 1,625 : B(1,625) = −2,640625 + 22,75 − 20 = 0,109375 > 0 ; donc α est dans [1,5 ; 1,625], d'amplitude 0,125.

:::

::: piege Croire que le théorème donne une solution unique, ou que sa réciproque est vraie
Pour f(x) = x³ − 3x + 1, on a f(−2) = −1 et f(2) = 3 : le théorème garantit une solution, et l'on conclut « il y en a une seule ». Cela tente parce que le signe change une fois entre −2 et 2. Pourtant f(−1) = 3, f(0) = 1, f(1) = −1 : f s'annule dans ]−2 ; −1[, dans ]0 ; 1[ et dans ]1 ; 2[. Sans stricte monotonie, le théorème donne au moins une solution, pas exactement une. Et pour B sur [0 ; 14], B(0) = B(14) = −20 ont le même signe alors que B s'annule deux fois : f(a) × f(b) > 0 n'interdit rien.
:::

::: propriete
- L'image d'un intervalle par une fonction continue est un intervalle ; l'image de [a ; b] est un intervalle fermé [m ; M].
- **Théorème des valeurs intermédiaires** : si f est continue sur [a ; b] et si k est compris entre f(a) et f(b), alors f(x) = k admet au moins une solution dans [a ; b].
- **Corollaire** : si f est continue sur [a ; b] et f(a) × f(b) < 0, alors f(x) = 0 admet au moins une solution dans ]a ; b[. Si de plus f est strictement monotone sur [a ; b], cette solution est unique.
- **Dichotomie** : on coupe [a ; b] en son milieu c ; on garde la moitié où f change de signe ; on recommence jusqu'à l'amplitude voulue.

Cas limite : la continuité est indispensable. f(x) = 1/x vérifie f(−1) = −1 et f(1) = 1, mais ne s'annule jamais, car elle n'est pas définie en 0.
:::

::: verifie
Soit g(x) = x³ + x − 5. Montrer que g(x) = 0 admet une solution unique α dans [1 ; 2], puis dire dans laquelle des deux moitiés, [1 ; 1,5] ou [1,5 ; 2], elle se trouve.

---

g est un polynôme, donc continue ; elle est strictement croissante comme somme de deux fonctions strictement croissantes, x³ et x. De plus g(1) = −3 < 0 et g(2) = 5 > 0 : par le corollaire, g(x) = 0 a une solution unique α dans ]1 ; 2[. Au milieu, g(1,5) = 3,375 + 1,5 − 5 = −0,125 < 0, du signe de g(1) : α est dans [1,5 ; 2].
:::

::: retenir
Une fonction continue qui change de signe sur [a ; b] s'annule entre a et b ; la stricte monotonie rend la solution unique, et la dichotomie l'encadre.
:::

## 🏰 Bijection et fonction réciproque

Un grossiste de fruits secs vend au prix p dinars le kilo (p ≥ 0) ; l'offre, en centaines de kilos, est S(p) = p²/2 + 2.
Le directeur pose la question dans l'autre sens : quel prix p faut-il fixer pour offrir une quantité donnée q, par exemple 10 centaines ? Une quantité correspond-elle à un seul prix ?

::: definition
Si f est strictement monotone sur un intervalle I, chaque valeur de l'intervalle f(I) a **exactement un antécédent** dans I : on dit que f est une **bijection de I sur f(I)**. La fonction qui associe à chaque y de f(I) cet antécédent est la **fonction réciproque** f⁻¹ : y = f(x) équivaut à x = f⁻¹(y), pour x dans I et y dans f(I).
:::

::: figure La courbe orange de la réciproque S⁻¹ est la symétrique de la courbe verte de S par rapport à la droite y = x : le point M(4 ; 10) a pour symétrique M′(10 ; 4)
<svg viewBox="0 0 275 250"><title>La courbe de la réciproque est la symétrique de celle de S par rapport à la droite y = x</title><line x1="38" y1="225" x2="258" y2="225" stroke="#0f172a" stroke-width="1.6"/><line x1="42" y1="229" x2="42" y2="9" stroke="#0f172a" stroke-width="1.6"/><polygon points="258,225 251,221.5 251,228.5" fill="#0f172a"/><polygon points="42,9 38.5,16 45.5,16" fill="#0f172a"/><text x="250" y="219" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">p</text><text x="50" y="19" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">q</text><line x1="112" y1="222" x2="112" y2="228" stroke="#0f172a" stroke-width="1.3"/><text x="112" y="240" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="182" y1="222" x2="182" y2="228" stroke="#0f172a" stroke-width="1.3"/><text x="182" y="240" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="252" y1="222" x2="252" y2="228" stroke="#0f172a" stroke-width="1.3"/><text x="252" y="240" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12</text><line x1="39" y1="155" x2="45" y2="155" stroke="#0f172a" stroke-width="1.3"/><text x="36" y="159" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="39" y1="85" x2="45" y2="85" stroke="#0f172a" stroke-width="1.3"/><text x="36" y="89" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="39" y1="15" x2="45" y2="15" stroke="#0f172a" stroke-width="1.3"/><text x="36" y="19" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12</text><line x1="42" y1="225" x2="252" y2="15" stroke="#0f172a" stroke-width="1.4" stroke-dasharray="6 4"/><polyline points="42,190 43,190 44,189.9 44.9,189.8 45.9,189.6 46.9,189.3 47.9,189 48.8,188.7 49.8,188.2 50.8,187.8 51.8,187.3 52.8,186.7 53.7,186.1 54.7,185.4 55.7,184.6 56.7,183.8 57.7,183 58.6,182.1 59.6,181.1 60.6,180.1 61.6,179.1 62.5,177.9 63.5,176.8 64.5,175.5 65.5,174.2 66.5,172.9 67.4,171.5 68.4,170.1 69.4,168.6 70.4,167 71.3,165.4 72.3,163.7 73.3,162 74.3,160.2 75.3,158.4 76.2,156.5 77.2,154.6 78.2,152.6 79.2,150.5 80.2,148.4 81.1,146.2 82.1,144 83.1,141.8 84.1,139.4 85,137.1 86,134.6 87,132.1 88,129.6 89,127 89.9,124.3 90.9,121.6 91.9,118.9 92.9,116.1 93.8,113.2 94.8,110.3 95.8,107.3 96.8,104.2 97.8,101.2 98.7,98 99.7,94.8 100.7,91.6 101.7,88.3 102.7,84.9 103.6,81.5 104.6,78 105.6,74.5 106.6,70.9 107.5,67.3 108.5,63.6 109.5,59.8 110.5,56 111.5,52.2 112.4,48.2 113.4,44.3 114.4,40.3 115.4,36.2 116.3,32.1 117.3,27.9 118.3,23.6 119.3,19.3 120.3,15" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="77,225 77,224 77.1,223 77.2,222.1 77.4,221.1 77.7,220.1 78,219.1 78.3,218.2 78.8,217.2 79.2,216.2 79.7,215.2 80.3,214.2 80.9,213.3 81.6,212.3 82.4,211.3 83.2,210.3 84,209.3 84.9,208.4 85.9,207.4 86.9,206.4 87.9,205.4 89.1,204.5 90.2,203.5 91.5,202.5 92.8,201.5 94.1,200.5 95.5,199.6 96.9,198.6 98.4,197.6 100,196.6 101.6,195.7 103.3,194.7 105,193.7 106.8,192.7 108.6,191.7 110.5,190.8 112.4,189.8 114.4,188.8 116.5,187.8 118.6,186.8 120.8,185.9 123,184.9 125.2,183.9 127.6,182.9 129.9,182 132.4,181 134.9,180 137.4,179 140,178 142.7,177.1 145.4,176.1 148.1,175.1 150.9,174.1 153.8,173.2 156.7,172.2 159.7,171.2 162.8,170.2 165.8,169.2 169,168.3 172.2,167.3 175.4,166.3 178.7,165.3 182.1,164.3 185.5,163.4 189,162.4 192.5,161.4 196.1,160.4 199.7,159.5 203.4,158.5 207.2,157.5 211,156.5 214.8,155.5 218.8,154.6 222.7,153.6 226.7,152.6 230.8,151.6 234.9,150.7 239.1,149.7 243.4,148.7 247.7,147.7 252,146.7" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="112" y1="50" x2="217" y2="155" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><circle cx="112" cy="50" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="217" cy="155" r="4" fill="#b45309" stroke="#0f172a" stroke-width="1"/><text x="103" y="47" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><text x="225" y="148" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M′</text><text x="203" y="22" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = x</text><text x="82.2" y="23.8" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S</text><text x="208.2" y="204" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S⁻¹</text></svg>
:::

::: exemple L'offre S est une bijection de [0 ; +∞[ sur [2 ; +∞[
1. S(p) = p²/2 + 2 est continue, et p ↦ p² est strictement croissante sur [0 ; +∞[ : S est strictement croissante.
2. Son image est un intervalle qui commence en S(0) = 2 et va jusqu'à lim p→+∞ S(p) = +∞ : S([0 ; +∞[) = [2 ; +∞[.
3. S est donc une bijection de [0 ; +∞[ sur [2 ; +∞[ : chaque quantité q ≥ 2 correspond à un seul prix.

:::

::: exemple Expliciter la réciproque et fixer le prix pour 10 centaines de kilos
1. On résout q = p²/2 + 2 en p : p² = 2q − 4, donc p = √(2q − 4) ou p = −√(2q − 4).
2. Le prix est positif (p ∈ [0 ; +∞[) : on garde p = √(2q − 4). Ainsi S⁻¹(q) = √(2q − 4), définie sur [2 ; +∞[.
3. S⁻¹(10) = √16 = 4 : il faut fixer le prix à 4 dinars. Vérification : S(4) = 16/2 + 2 = 10.

:::

::: piege Confondre f⁻¹ et 1/f
On lit S⁻¹(10) comme « 1 sur S(10) » et l'on écrit 1/52. Cela tente parce que l'exposant −1 évoque l'inverse d'un nombre. Mais f⁻¹ est la fonction qui défait f : S⁻¹(10) = 4, le prix qui donne la quantité 10. L'inverse 1/S(10) = 1/52 est un autre nombre, sans rapport avec le prix.
:::

::: propriete
- Si f est strictement monotone sur I, f est une bijection de I sur f(I), et f⁻¹ varie dans le même sens que f.
- Si de plus f est continue sur I, f(I) est un intervalle et f⁻¹ est continue sur f(I). Pour f strictement croissante : f([a ; b]) = [f(a) ; f(b)] et f(]a ; b[) = ]lim a⁺ f ; lim b⁻ f[. Pour f strictement décroissante, les bornes s'échangent : f([a ; b]) = [f(b) ; f(a)].
- Dans un repère orthonormé, les courbes de f et de f⁻¹ sont symétriques par rapport à la droite y = x : M(x ; y) est sur la courbe de f si et seulement si M′(y ; x) est sur celle de f⁻¹.

Cas limite : la monotonie est indispensable. x ↦ x² n'est pas une bijection de ℝ sur ℝ₊ (2 et −2 ont la même image) ; c'en est une de [0 ; +∞[ sur [0 ; +∞[.
:::

::: verifie
Soit E(p) = 80/(p + 3) sur [0 ; +∞[. Donner l'image de [0 ; +∞[ par E, puis calculer E⁻¹(10).

---

p + 3 est positif et croissant, donc E est strictement décroissante et continue. Son image va de lim p→+∞ E(p) = 0 (borne exclue) jusqu'à E(0) = 80/3 (borne atteinte) : E([0 ; +∞[) = ]0 ; 80/3]. Pour E⁻¹(10), on résout 80/(p + 3) = 10, d'où p + 3 = 8 et p = 5. Vérification : E(5) = 80/8 = 10.
:::

::: retenir
Une fonction continue et strictement monotone sur un intervalle y est une bijection sur son image ; sa réciproque varie dans le même sens et a pour courbe la symétrique de celle de f par rapport à y = x.
:::

## 💰 Lire une limite ou une rupture en économie

Un atelier de couture a pour coût total C(x) = 2x² + 8x + 50, en milliers de dinars, pour x dizaines de pièces ; son coût moyen par dizaine est CM(x) = C(x)/x = 2x + 8 + 50/x pour x > 0.
Que devient ce coût moyen si l'on produit presque rien ? Et si l'on produit énormément ? Que disent ces limites de l'atelier ?

::: figure Le coût moyen CM explose près de 0 puis se rapproche de la droite y = 2x + 8 : l'écart entre les deux courbes devient aussi petit qu'on veut
<svg viewBox="0 0 345 200"><title>Le coût moyen CM se rapproche de la droite y = 2x + 8 quand x grandit et explose près de 0</title><line x1="40" y1="175" x2="326" y2="175" stroke="#0f172a" stroke-width="1.6"/><line x1="44" y1="179" x2="44" y2="9" stroke="#0f172a" stroke-width="1.6"/><polygon points="326,175 319,171.5 319,178.5" fill="#0f172a"/><polygon points="44,9 40.5,16 47.5,16" fill="#0f172a"/><text x="318" y="169" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="52" y="19" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">CM</text><line x1="105.3" y1="172" x2="105.3" y2="178" stroke="#0f172a" stroke-width="1.3"/><text x="105.3" y="190" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="166.7" y1="172" x2="166.7" y2="178" stroke="#0f172a" stroke-width="1.3"/><text x="166.7" y="190" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="228" y1="172" x2="228" y2="178" stroke="#0f172a" stroke-width="1.3"/><text x="228" y="190" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="289.3" y1="172" x2="289.3" y2="178" stroke="#0f172a" stroke-width="1.3"/><text x="289.3" y="190" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="41" y1="135" x2="47" y2="135" stroke="#0f172a" stroke-width="1.3"/><text x="38" y="139" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="41" y1="95" x2="47" y2="95" stroke="#0f172a" stroke-width="1.3"/><text x="38" y="99" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="41" y1="55" x2="47" y2="55" stroke="#0f172a" stroke-width="1.3"/><text x="38" y="59" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><line x1="41" y1="15" x2="47" y2="15" stroke="#0f172a" stroke-width="1.3"/><text x="38" y="19" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><polyline points="44,159 182,141 320,123" fill="none" stroke="#b45309" stroke-width="2.0" stroke-dasharray="5 3" stroke-linejoin="round" stroke-linecap="round"/><polyline points="67,22.7 68.3,29.5 69.5,35.5 70.8,41.1 72.1,46.1 73.3,50.6 74.6,54.8 75.9,58.6 77.1,62.1 78.4,65.3 79.7,68.3 80.9,71.1 82.2,73.7 83.4,76.1 84.7,78.4 86,80.5 87.2,82.4 88.5,84.3 89.8,86 91,87.7 92.3,89.2 93.6,90.7 94.8,92 96.1,93.3 97.4,94.6 98.6,95.7 99.9,96.8 101.2,97.9 102.4,98.9 103.7,99.8 104.9,100.7 106.2,101.6 107.5,102.4 108.7,103.2 110,103.9 111.3,104.6 112.5,105.3 113.8,106 115.1,106.6 116.3,107.2 117.6,107.7 118.9,108.3 120.1,108.8 121.4,109.3 122.7,109.8 123.9,110.2 125.2,110.6 126.5,111.1 127.7,111.4 129,111.8 130.2,112.2 131.5,112.5 132.8,112.9 134,113.2 135.3,113.5 136.6,113.8 137.8,114.1 139.1,114.3 140.4,114.6 141.6,114.9 142.9,115.1 144.2,115.3 145.4,115.5 146.7,115.7 148,115.9 149.2,116.1 150.5,116.3 151.8,116.5 153,116.7 154.3,116.8 155.6,117 156.8,117.1 158.1,117.2 159.3,117.4 160.6,117.5 161.9,117.6 163.1,117.7 164.4,117.8 165.7,117.9 166.9,118 168.2,118.1 169.5,118.2 170.7,118.3 172,118.3 173.3,118.4 174.5,118.5 175.8,118.5 177.1,118.6 178.3,118.6 179.6,118.7 180.8,118.7 182.1,118.8 183.4,118.8 184.6,118.9 185.9,118.9 187.2,118.9 188.4,118.9 189.7,118.9 191,119 192.2,119 193.5,119 194.8,119 196,119 197.3,119 198.6,119 199.8,119 201.1,119 202.4,119 203.6,119 204.9,119 206.1,118.9 207.4,118.9 208.7,118.9 209.9,118.9 211.2,118.8 212.5,118.8 213.7,118.8 215,118.8 216.3,118.7 217.5,118.7 218.8,118.7 220.1,118.6 221.3,118.6 222.6,118.5 223.9,118.5 225.1,118.4 226.4,118.4 227.7,118.3 228.9,118.3 230.2,118.2 231.5,118.2 232.7,118.1 234,118.1 235.2,118 236.5,118 237.8,117.9 239,117.8 240.3,117.8 241.6,117.7 242.8,117.6 244.1,117.6 245.4,117.5 246.6,117.4 247.9,117.4 249.2,117.3 250.4,117.2 251.7,117.1 253,117.1 254.2,117 255.5,116.9 256.8,116.8 258,116.8 259.3,116.7 260.5,116.6 261.8,116.5 263.1,116.4 264.3,116.3 265.6,116.3 266.9,116.2 268.1,116.1 269.4,116 270.7,115.9 271.9,115.8 273.2,115.7 274.5,115.6 275.7,115.5 277,115.4 278.3,115.4 279.5,115.3 280.8,115.2 282.1,115.1 283.3,115 284.6,114.9 285.8,114.8 287.1,114.7 288.4,114.6 289.6,114.5 290.9,114.4 292.2,114.3 293.4,114.2 294.7,114.1 296,114 297.2,113.9 298.5,113.8 299.8,113.6 301,113.5 302.3,113.4 303.6,113.3 304.8,113.2 306.1,113.1 307.4,113 308.6,112.9 309.9,112.8 311.1,112.7 312.4,112.6 313.7,112.5 314.9,112.3 316.2,112.2 317.5,112.1 318.7,112 320,111.9" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="277.1" y="106.4" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">CM</text><text x="283.2" y="144.8" text-anchor="middle" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = 2x + 8</text></svg>
:::

::: exemple Les limites de CM(x) = 2x + 8 + 50/x
1. Près de 0 par la droite : 2x + 8 tend vers 8 et 50/x tend vers +∞ (0⁺ au dénominateur) : lim x→0⁺ CM(x) = +∞.
2. En +∞ : 2x + 8 tend vers +∞ et 50/x vers 0 : lim x→+∞ CM(x) = +∞.
3. L'écart CM(x) − (2x + 8) = 50/x tend vers 0 en +∞ : la courbe se rapproche de la droite y = 2x + 8.
4. Sens économique : les 50 000 dinars de frais fixes pèsent sur très peu de pièces au départ ; pour une grande production, le coût moyen ressemble à 2x + 8, le terme proportionnel à la production.

:::

::: exemple Un saut de coût : C(q) = 2q + 30 si q ≤ 100, C(q) = 1,5q + 120 si q > 100
1. À gauche de 100, lim q→100⁻ C(q) = 2 × 100 + 30 = 230.
2. À droite de 100, lim q→100⁺ C(q) = 1,5 × 100 + 120 = 270.
3. Les limites diffèrent : C n'est pas continue en 100, le coût saute de 40 au passage du seuil.
4. Sens économique : au-delà de 100 unités, il faut ouvrir une seconde chaîne. Les frais fixes passent de 30 à 120 (+90), mais chaque unité coûte 1,5 au lieu de 2 : au seuil, le coût total saute de 90 − 0,5 × 100 = 40.

:::

::: piege Remplacer x par 0 dans un coût moyen
On voudrait connaître « CM(0) » et l'on écrit 2 × 0 + 8 + 50/0, que l'on prend pour les frais fixes 50. Cela tente parce que 50 est bien le coût quand on ne produit rien. Mais CM(x) = C(x)/x n'est pas défini en 0, et ce que l'on étudie est ce qui se passe quand x s'approche de 0 par valeurs positives : le coût de 50 est réparti sur de moins en moins de pièces, d'où +∞ et non 50.
:::

::: propriete
- lim x→0⁺ CM(x) = +∞ traduit des frais fixes répartis sur très peu d'unités.
- lim x→+∞ CM(x) = ℓ réel signifie que le coût moyen se stabilise autour de ℓ ; la droite y = ℓ est asymptote horizontale.
- Si CM(x) − (ax + b) tend vers 0 en +∞, la droite y = ax + b est asymptote oblique : le coût moyen se rapproche d'un coût proportionnel.
- Une fonction de coût dont les limites à gauche et à droite en un seuil diffèrent présente un saut : une rupture de continuité, un palier.

Cas limite : une limite ne dit rien sur la valeur atteinte. CM reste toujours strictement au-dessus de 2x + 8, puisque 50/x > 0, alors que l'écart tend vers 0.
:::

::: verifie
Un atelier a pour coût moyen CM(x) = 3x + 5 + 80/x, pour x > 0. Que valent lim x→0⁺ CM(x) et la limite en +∞ de CM(x) − (3x + 5) ? Qu'en conclure ?

---

Près de 0 par la droite, 3x + 5 tend vers 5 et 80/x vers +∞ : lim x→0⁺ CM(x) = +∞, car les frais fixes de 80 pèsent sur peu d'unités. En +∞, CM(x) − (3x + 5) = 80/x tend vers 0 : la droite y = 3x + 5 est asymptote oblique à la courbe.
:::

::: retenir
Une limite infinie en 0⁺ d'un coût moyen traduit les frais fixes, une asymptote traduit le coût proportionnel, et des limites différentes de part et d'autre d'un seuil traduisent un saut de coût.
:::
