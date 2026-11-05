# ⚔️ Dérivation et primitives — lire la pente, remonter la pente

> 💡 «La dérivée lit la pente d'une courbe en chaque point ; la primitive fait le chemin inverse : à partir des pentes, elle retrouve la courbe.»

Bienvenue, héros de la section Sciences de l'informatique. Newton et Leibniz ont fondé, chacun de leur côté, le calcul différentiel : une machine à lire la vitesse instantanée, la pente d'une courbe, le sommet d'une colline. Douze étapes te mènent du nombre dérivé aux primitives : nombre dérivé, dérivabilité à droite et à gauche, dérivées et opérations, composée, réciproque, accroissements finis, variations, dérivée seconde, puis quatre étapes de primitives. On suppose acquis le calcul des limites (chapitre 2) et la continuité (chapitre 3), fonction réciproque comprise. Les études complètes de fonctions viendront au chapitre suivant.

## 🧭 Nombre dérivé et tangente

Une bille roule sur une pente : elle a parcouru d(t) = t² mètres au bout de t secondes. Entre t = 2 et t = 2 + h, sa vitesse moyenne est (d(2 + h) − d(2))/h.
Quelle est sa vitesse exactement à l'instant t = 2, quand l'intervalle de temps h devient aussi petit qu'on veut ?

::: definition
Soit f définie sur un intervalle ouvert I et x₀ un réel de I. **f est dérivable en x₀** si le quotient (f(x) − f(x₀))/(x − x₀), appelé **taux d'accroissement**, a une limite **finie** ℓ quand x tend vers x₀ :

$$ lim x→x₀ (f(x) − f(x₀))/(x − x₀) = ℓ $$

Le réel ℓ est le **nombre dérivé** de f en x₀ (ou dérivée de f en x₀), noté **f′(x₀)**. En posant x = x₀ + h, on écrit aussi f′(x₀) = lim h→0 (f(x₀ + h) − f(x₀))/h.
:::

::: figure La sécante (AM), de pente 5, pivote autour de A et devient la tangente, de pente 4, quand M glisse vers A
<svg viewBox="0 0 340 250"><title>Courbe de x ↦ x², point A(2 ; 4), tangente de pente 4 en A et sécante (AM) de pente 5 avec M(3 ; 9)</title><line x1="20" y1="187.8" x2="320" y2="187.8" stroke="#0f172a" stroke-width="1.6"/><line x1="57.5" y1="224" x2="57.5" y2="10" stroke="#0f172a" stroke-width="1.6"/><polygon points="320,187.8 313,184.3 313,191.3" fill="#0f172a"/><polygon points="57.5,10 54,17 61,17" fill="#0f172a"/><text x="316" y="180.8" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="65.5" y="18" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="132.5" y1="184.8" x2="132.5" y2="190.8" stroke="#0f172a" stroke-width="1.3"/><text x="132.5" y="202.8" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="207.5" y1="184.8" x2="207.5" y2="190.8" stroke="#0f172a" stroke-width="1.3"/><text x="207.5" y="202.8" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="282.5" y1="184.8" x2="282.5" y2="190.8" stroke="#0f172a" stroke-width="1.3"/><text x="282.5" y="202.8" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="54.5" y1="121.9" x2="60.5" y2="121.9" stroke="#0f172a" stroke-width="1.3"/><text x="51.5" y="125.9" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="54.5" y1="39.6" x2="60.5" y2="39.6" stroke="#0f172a" stroke-width="1.3"/><text x="51.5" y="43.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">9</text><polyline points="23.8,184.5 28.3,185.3 32.9,186 37.4,186.6 42,187.1 46.6,187.4 51.1,187.7 55.7,187.8 60.2,187.8 64.8,187.6 69.4,187.4 73.9,187 78.5,186.5 83.1,185.9 87.6,185.1 92.2,184.3 96.8,183.3 101.3,182.2 105.9,180.9 110.4,179.6 115,178.1 119.6,176.5 124.1,174.8 128.7,173 133.2,171 137.8,168.9 142.4,166.7 146.9,164.4 151.5,161.9 156.1,159.4 160.6,156.7 165.2,153.8 169.8,150.9 174.3,147.9 178.9,144.7 183.4,141.4 188,137.9 192.6,134.4 197.1,130.7 201.7,126.9 206.2,123 210.8,119 215.4,114.8 219.9,110.6 224.5,106.2 229.1,101.6 233.6,97 238.2,92.2 242.8,87.4 247.3,82.3 251.9,77.2 256.4,72 261,66.6 265.6,61.1 270.1,55.5 274.7,49.7 279.2,43.9 283.8,37.9 288.4,31.8 292.9,25.6 297.5,19.2" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="132.5" y1="204.2" x2="297.5" y2="23.2" stroke="#64748b" stroke-width="1.6" stroke-dasharray="6 4"/><line x1="95" y1="220.7" x2="297.5" y2="42.9" stroke="#b45309" stroke-width="2.2"/><line x1="207.5" y1="187.8" x2="207.5" y2="121.9" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="57.5" y1="121.9" x2="207.5" y2="121.9" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="282.5" y1="187.8" x2="282.5" y2="39.6" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="57.5" y1="39.6" x2="282.5" y2="39.6" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><circle cx="207.5" cy="121.9" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="282.5" cy="39.6" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="198.5" y="113.9" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="273.5" y="35.6" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><text x="31.2" y="69.3" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente : pente 4</text><text x="31.2" y="89" text-anchor="start" font-size="11" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">sécante (AM) : pente 5</text><text x="119" y="164" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text></svg>
:::

La pente de la sécante (AM) est le taux d'accroissement de f entre 2 et 3 : (9 − 4)/(3 − 2) = 5. Quand M glisse vers A, cette pente tend vers celle de la tangente orange : c'est le nombre dérivé f′(2) de la définition.

::: exemple La bille à l'instant t = 2 : d(t) = t²
1. Le taux d'accroissement entre 2 et 2 + h est (d(2 + h) − d(2))/h : c'est la vitesse moyenne.
2. d(2 + h) − d(2) = (4 + 4h + h²) − 4 = 4h + h², donc le taux vaut (4h + h²)/h = 4 + h pour h ≠ 0 : on simplifie par h avant de passer à la limite.
3. lim h→0 (4 + h) = 4, un réel : d est dérivable en 2 et d′(2) = 4. La vitesse instantanée de la bille est 4 m/s.
4. La tangente en A(2 ; 4) a pour pente 4 : y = 4(t − 2) + 4 = 4t − 4.

:::

::: exemple Sans contexte : f(x) = x² − 4 en x₀ = −1
1. f(−1) = 1 − 4 = −3, et f(−1 + h) = (1 − 2h + h²) − 4 = −3 − 2h + h².
2. Le taux est (f(−1 + h) − f(−1))/h = (−2h + h²)/h = −2 + h : on soustrait f(−1) pour que h se factorise.
3. lim h→0 (−2 + h) = −2, donc f′(−1) = −2.
4. La tangente en (−1 ; −3) est y = −2(x + 1) − 3 = −2x − 5. Contrôle : pour x = −1, on trouve −2 × (−1) − 5 = −3 ✓.

:::

Un programme ne sait pas passer à la limite : il calcule le taux pour des h de plus en plus petits. Voici l'idée, pour f(x) = √x en x₀ = 4, avec h divisé par 2 à chaque tour :

```
x0 ← 4 ; h ← 1
pour k de 1 à n :
    p ← (f(x0 + h) − f(x0)) / h
    afficher h, p
    h ← h / 2
```

Les valeurs de p sont environ 0,2361 pour h = 1, 0,2426 pour h = 0,5 et 0,2462 pour h = 0,25 : elles s'approchent de f′(4) = 1/(2√4) = 0,25, que la section suivante permettra de retrouver par une formule.

::: piege Écrire la tangente y = f′(x₀)x + f(x₀)
Pour la bille, on écrit y = 4t + 4. Cela tente parce que, dans y = mx + p, le nombre m est la pente et que f(x₀) ressemble à une ordonnée à l'origine. Mais f(x₀) est l'ordonnée au point d'abscisse x₀, pas en 0 : la droite y = 4t + 4 passe par (2 ; 12), pas par A(2 ; 4). La bonne équation décale de x₀ : y = 4(t − 2) + 4 = 4t − 4.
:::

::: propriete
- Si f est dérivable en x₀, sa courbe admet au point M₀(x₀ ; f(x₀)) une **tangente** de pente f′(x₀), d'équation y = f′(x₀)(x − x₀) + f(x₀).
- Théorème (admis) : toute fonction dérivable en x₀ est continue en x₀.

Cas limite : la réciproque est fausse. x ↦ |x| est continue en 0, mais son taux |h|/h vaut 1 pour h > 0 et −1 pour h < 0 : il n'a pas de limite, donc |x| n'est pas dérivable en 0.
:::

::: verifie
Soit f(x) = 3x² − x. Calculer f′(1) par la définition, puis l'équation de la tangente en x₀ = 1.

---

f(1) = 2 et f(1 + h) = 3(1 + 2h + h²) − 1 − h = 2 + 5h + 3h². Le taux est (5h + 3h²)/h = 5 + 3h, qui tend vers 5 : f′(1) = 5. La tangente est y = 5(x − 1) + 2 = 5x − 3 : on décale de x₀ = 1 pour passer par le point (1 ; 2).
:::

::: retenir
f′(x₀) est la limite du taux d'accroissement : c'est la pente de la tangente y = f′(x₀)(x − x₀) + f(x₀), et une fonction dérivable en x₀ y est continue.
:::

## 🗡️ Dérivabilité à droite, à gauche et sur un intervalle

Le profil d'une rampe de skate est la courbe de f(x) = |x² − 4|. En x = 2, la planche arrive par la gauche puis repart vers la droite.
La rampe a-t-elle une seule pente en ce point ?

::: definition
**f est dérivable à droite en x₀** si le taux d'accroissement (f(x) − f(x₀))/(x − x₀) a une limite finie quand x tend vers x₀ par valeurs supérieures (x > x₀). Cette limite est le **nombre dérivé à droite**, noté **f′d(x₀)**. On définit de même la **dérivabilité à gauche** et f′g(x₀), avec x < x₀.

f est dérivable en x₀ si et seulement si elle est dérivable à droite et à gauche en x₀, avec f′d(x₀) = f′g(x₀).

f est **dérivable sur ]a ; b[** si elle l'est en tout point de ]a ; b[ ; **sur [a ; b]** si elle l'est sur ]a ; b[, à droite en a et à gauche en b. On définit de même la dérivabilité sur [a ; b[, ]a ; b], [a ; +∞[ et ]−∞ ; a].
:::

::: figure En A(2 ; 0), la courbe a deux demi-tangentes de pentes différentes : −4 à gauche, 4 à droite
<svg viewBox="0 0 340 230"><title>Courbe de x ↦ |x² − 4| et, au point A(2 ; 0), deux demi-tangentes de pentes −4 à gauche et 4 à droite</title><line x1="20" y1="177.8" x2="320" y2="177.8" stroke="#0f172a" stroke-width="1.6"/><line x1="50.8" y1="200" x2="50.8" y2="10" stroke="#0f172a" stroke-width="1.6"/><polygon points="320,177.8 313,174.3 313,181.3" fill="#0f172a"/><polygon points="50.8,10 47.3,17 54.3,17" fill="#0f172a"/><text x="316" y="170.8" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="58.8" y="18" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="127.7" y1="174.8" x2="127.7" y2="180.8" stroke="#0f172a" stroke-width="1.3"/><text x="127.7" y="192.8" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="204.6" y1="174.8" x2="204.6" y2="180.8" stroke="#0f172a" stroke-width="1.3"/><text x="204.6" y="192.8" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="281.5" y1="174.8" x2="281.5" y2="180.8" stroke="#0f172a" stroke-width="1.3"/><text x="281.5" y="192.8" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><polyline points="27.7,81.3 30.7,80.8 33.7,80.3 36.7,79.9 39.7,79.6 42.6,79.4 45.6,79.2 48.6,79.1 51.6,79.1 54.6,79.2 57.6,79.3 60.6,79.5 63.6,79.8 66.6,80.1 69.6,80.6 72.6,81.1 75.6,81.7 78.5,82.3 81.5,83 84.5,83.8 87.5,84.7 90.5,85.7 93.5,86.7 96.5,87.8 99.5,89 102.5,90.2 105.5,91.6 108.5,93 111.5,94.4 114.4,96 117.4,97.6 120.4,99.3 123.4,101.1 126.4,103 129.4,104.9 132.4,106.9 135.4,108.9 138.4,111.1 141.4,113.3 144.4,115.6 147.4,118 150.3,120.4 153.3,123 156.3,125.6 159.3,128.2 162.3,131 165.3,133.8 168.3,136.7 171.3,139.7 174.3,142.7 177.3,145.8 180.3,149 183.2,152.3 186.2,155.6 189.2,159 192.2,162.5 195.2,166.1 198.2,169.7 201.2,173.5 204.2,177.2 207.2,174.5 210.2,170.5 213.2,166.5 216.2,162.4 219.1,158.3 222.1,154 225.1,149.7 228.1,145.3 231.1,140.9 234.1,136.3 237.1,131.7 240.1,127 243.1,122.3 246.1,117.4 249.1,112.5 252.1,107.5 255,102.5 258,97.3 261,92.1 264,86.9 267,81.5 270,76.1 273,70.6 276,65 279,59.3 282,53.6 285,47.8 287.9,41.9 290.9,36 293.9,29.9 296.9,23.8" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="204.6" y1="177.8" x2="277.7" y2="84" stroke="#b45309" stroke-width="2.4"/><line x1="131.5" y1="84" x2="204.6" y2="177.8" stroke="#7c3aed" stroke-width="2.4"/><circle cx="204.6" cy="177.8" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="204.6" y="167.8" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="285.7" y="86" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pente 4</text><text x="123.5" y="82" text-anchor="end" font-size="11" font-weight="700" fill="#7c3aed" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pente −4</text><text x="267.5" y="35.6" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text></svg>
:::

Les deux segments tracés en A sont les limites des sécantes : celui de droite a pour pente f′d(2), celui de gauche f′g(2). L'exemple calcule ces deux pentes.

::: exemple La rampe en x = 2
1. f(2) = 0. Pour x > 2, x² − 4 > 0 et f(x) = x² − 4 : le taux est (x² − 4)/(x − 2) = x + 2, car x² − 4 = (x − 2)(x + 2). Il tend vers 4 : f′d(2) = 4.
2. Pour −2 < x < 2, x² − 4 < 0 et f(x) = −(x² − 4) : le taux est −(x + 2), qui tend vers −4 : f′g(2) = −4.
3. 4 ≠ −4 : f n'est pas dérivable en 2. La courbe y a un **point anguleux** et deux demi-tangentes, de pentes 4 et −4, bien que f soit continue en 2.

:::

::: exemple Deux formules qui se raccordent : g(x) = x² si x < 2, g(x) = 4x − 4 si x ≥ 2
1. Continuité d'abord : g(2) = 4 × 2 − 4 = 4 (la seconde formule, car x ≥ 2) et lim x→2⁻ x² = 4 : les deux morceaux se rejoignent.
2. À droite, le taux est (4x − 4 − 4)/(x − 2) = 4(x − 2)/(x − 2) = 4, donc g′d(2) = 4.
3. À gauche, le taux est (x² − 4)/(x − 2) = x + 2, qui tend vers 4 : g′g(2) = 4.
4. g′g(2) = g′d(2) = 4 : g est dérivable en 2, et g′(2) = 4. La droite y = 4x − 4 est la tangente à la parabole en (2 ; 4) : les morceaux se raccordent sans pli.

:::

::: piege Comparer les dérivées des deux formules sans contrôler la continuité
Soit f(x) = x² si x < 1 et f(x) = 2x + 3 si x ≥ 1. Les formules x² et 2x + 3 ont pour dérivées 2x et 2, qui valent toutes deux 2 en 1, et l'on conclut « f est dérivable en 1 ». Cela tente parce que, dans l'exemple précédent, des pentes égales donnaient la dérivabilité. Mais f(1) = 5 alors que lim x→1⁻ x² = 1 : f n'est même pas continue en 1, donc pas dérivable. On compare d'abord les valeurs, puis les taux d'accroissement.
:::

::: propriete
- f est dérivable en x₀ si et seulement si f′g(x₀) et f′d(x₀) existent et sont égaux.
- Si f est dérivable à droite (resp. à gauche) en x₀, sa courbe admet en M₀ une **demi-tangente** à droite d'équation y = f′d(x₀)(x − x₀) + f(x₀) avec x ≥ x₀ (resp. à gauche, avec f′g(x₀) et x ≤ x₀).
- Pour une fonction à deux formules, on vérifie la continuité, puis on calcule séparément les deux taux.

Cas limite : si le taux tend vers +∞ ou −∞, f n'est pas dérivable de ce côté et la demi-tangente est verticale. x ↦ √x, de taux 1/√x, n'est pas dérivable à droite en 0.
:::

::: verifie
Soit k(x) = 0 si x < 1 et k(x) = x − 1 si x ≥ 1. La fonction k est-elle dérivable en 1 ?

---

On contrôle d'abord la continuité : k(1) = 0 et lim x→1⁻ 0 = 0, c'est bon. À gauche, le taux vaut 0/(x − 1) = 0 : k′g(1) = 0. À droite, il vaut (x − 1)/(x − 1) = 1 : k′d(1) = 1. Comme 0 ≠ 1, k n'est pas dérivable en 1 : point anguleux, demi-tangentes y = 0 (à gauche) et y = x − 1 (à droite).
:::

::: retenir
f est dérivable en x₀ exactement quand f′g(x₀) = f′d(x₀) (finis) ; on contrôle la continuité avant de comparer les pentes, et un taux infini donne une demi-tangente verticale.
:::

## 🔮 Fonction dérivée, dérivées usuelles et opérations

Pour f(x) = x(x − 3), le plus court est de développer : f(x) = x² − 3x, donc f′(x) = 2x − 3. Mais dériver chaque facteur séparément donnerait 1 × 1 = 1.
Quelle règle fabrique 2x − 3 quand on ne veut pas développer, et comment dériver un quotient ?

::: definition
Soit f dérivable sur un intervalle I. La **fonction dérivée** de f est la fonction f′, définie sur I, qui à tout réel x de I associe le nombre dérivé f′(x).
:::

Les dérivées usuelles se démontrent par le taux d'accroissement, comme dans la première section :

| f(x) | f′(x) | sur |
| --- | --- | --- |
| k (constante) | 0 | ℝ |
| ax + b | a | ℝ |
| xⁿ (n entier ≥ 1) | nxⁿ⁻¹ | ℝ |
| 1/x | −1/x² | ]−∞ ; 0[ et ]0 ; +∞[ |
| √x | 1/(2√x) | ]0 ; +∞[ |

::: exemple Un produit : f(x) = x(x − 3)
1. Par développement : f(x) = x² − 3x est un polynôme, donc f′(x) = 2x − 3.
2. Avec u(x) = x et v(x) = x − 3, on a u′ = 1 et v′ = 1 : le produit u′v′ = 1 ne convient pas.
3. La règle ci-dessous donne (uv)′ = u′v + uv′ = 1 × (x − 3) + x × 1 = 2x − 3 ✓ : on retrouve le résultat du développement.

:::

::: exemple Un quotient : f(x) = (2x − 1)/(3x + 5)
1. Le dénominateur s'annule en −5/3 : f est dérivable sur ]−∞ ; −5/3[ et sur ]−5/3 ; +∞[.
2. u(x) = 2x − 1 et v(x) = 3x + 5, donc u′ = 2 et v′ = 3.
3. f′(x) = (u′v − uv′)/v² = (2(3x + 5) − 3(2x − 1))/(3x + 5)².
4. Le numérateur vaut 6x + 10 − 6x + 3 = 13 : f′(x) = 13/(3x + 5)², positive là où f est définie.

:::

::: exemple Une racine dans un produit : g(x) = (x − 2)√x
1. g est définie sur [0 ; +∞[, mais √x n'est dérivable que sur ]0 ; +∞[ : g′ est cherchée sur ]0 ; +∞[.
2. Avec u(x) = x − 2 et v(x) = √x : u′ = 1 et v′ = 1/(2√x).
3. g′(x) = √x + (x − 2)/(2√x) = (2x + x − 2)/(2√x) = (3x − 2)/(2√x), après mise au même dénominateur (√x = 2x/(2√x)).

:::

::: piege Écrire le numérateur du quotient à l'envers
Pour f(x) = 1/x, on prend u = 1 et v = x, et l'on écrit f′ = (uv′ − u′v)/v² = (1 × 1 − 0 × x)/x² = 1/x². Cela tente parce que ce sont les mêmes deux termes u′v et uv′. Mais 1/x est décroissante sur ]0 ; +∞[ : sa dérivée doit être négative. La règle commence par u′v : (u′v − uv′)/v² = (0 × x − 1 × 1)/x² = −1/x².
:::

::: propriete
Soient f et g dérivables sur I et λ un réel. Alors λf, f + g et fg sont dérivables sur I et :
- (λf)′ = λf′ ; (f + g)′ = f′ + g′ ; (fg)′ = f′g + fg′.
- En tout x de I où g(x) ≠ 0 : (1/g)′ = −g′/g² et (f/g)′ = (f′g − fg′)/g².
- Conséquence : ((ax + b)/(cx + d))′ = (ad − bc)/(cx + d)².

Cas limite : la dérivée d'un produit n'est pas le produit des dérivées ; et l'ensemble de dérivabilité peut être plus petit que l'ensemble de définition (√x est définie en 0, pas dérivable en 0).
:::

::: verifie
Dériver g(x) = (x² + 1)/(x − 2) et préciser l'ensemble de dérivabilité.

---

g est dérivable sur ]−∞ ; 2[ et sur ]2 ; +∞[, car x − 2 ne s'annule qu'en 2. Avec u = x² + 1 (u′ = 2x) et v = x − 2 (v′ = 1) : g′(x) = (2x(x − 2) − (x² + 1))/(x − 2)² = (x² − 4x − 1)/(x − 2)². On a écrit u′v en premier, puis retranché uv′.
:::

::: retenir
(uv)′ = u′v + uv′ et (u/v)′ = (u′v − uv′)/v² (v ≠ 0) : on dérive une somme terme à terme, jamais un produit facteur par facteur.
:::

## 🔗 Dériver une composée : puissances, racines et trigonométrie

Pour f(x) = (3x + 1)², on peut développer : f(x) = 9x² + 6x + 1, donc f′(x) = 18x + 6 = 6(3x + 1). Mais développer (3x + 1)¹⁰ serait interminable.
Existe-t-il une règle qui redonne 6(3x + 1) directement, et qui marche aussi pour la puissance 10 ?

::: exemple Les puissances de 3x + 1
1. On pose u(x) = 3x + 1, donc u′(x) = 3, et f = g∘u avec g(y) = y² : g′(y) = 2y.
2. La règle ci-dessous donne f′(x) = u′(x) × g′(u(x)) = 3 × 2(3x + 1) = 6(3x + 1), le résultat du développement ✓.
3. Pour (3x + 1)¹⁰, g(y) = y¹⁰ et g′(y) = 10y⁹ : la dérivée est 3 × 10(3x + 1)⁹ = 30(3x + 1)⁹, sans rien développer.

:::

::: exemple Une racine : h(x) = √(2x − 1)
1. On pose u(x) = 2x − 1, donc u′(x) = 2. h est définie quand u(x) ≥ 0, mais dérivable seulement quand u(x) > 0, soit sur ]1/2 ; +∞[ (√ n'est pas dérivable en 0).
2. Avec (√u)′ = u′/(2√u) : h′(x) = 2/(2√(2x − 1)) = 1/√(2x − 1).

:::

::: exemple Des fonctions trigonométriques : k(x) = sin²(3x) et l(x) = cos(2x − π/3)
1. k = u² avec u(x) = sin(3x), et u′(x) = 3cos(3x) car (sin(ax + b))′ = a cos(ax + b).
2. k′(x) = 2u′u = 2 × 3cos(3x) × sin(3x) = 6 sin(3x) cos(3x).
3. Pour l, a = 2 et b = −π/3 : l′(x) = −2 sin(2x − π/3), car (cos(ax + b))′ = −a sin(ax + b).

:::

::: piege Oublier le facteur a dans (sin(ax + b))′
Pour f(x) = sin(2x), on écrit f′(x) = cos(2x), en ne retenant que (sin)′ = cos. Cela tente parce que la table donne sin′ = cos. Mais un contrôle numérique contredit ce résultat : le taux d'accroissement de f entre 0 et 0,1 vaut sin(0,2)/0,1 ≈ 1,99, proche de 2 et non de cos(0) = 1. Il manque le facteur 2, dérivée de l'intérieur : f′(x) = 2cos(2x), qui vaut bien 2 en 0.
:::

::: propriete
**Théorème (admis)** : si f est dérivable en x et g dérivable en f(x), alors g∘f est dérivable en x et (g∘f)′(x) = g′(f(x)) × f′(x).

Pour u dérivable, on en déduit :
- (uⁿ)′ = n u′ uⁿ⁻¹ (n entier ≥ 1) ;
- (√u)′ = u′/(2√u), là où u > 0 ;
- (sin x)′ = cos x, (cos x)′ = −sin x, (tan x)′ = 1 + tan²x ;
- (sin(ax + b))′ = a cos(ax + b), (cos(ax + b))′ = −a sin(ax + b), (tan(ax + b))′ = a(1 + tan²(ax + b)), et (√(ax + b))′ = a/(2√(ax + b)).

Cas limite : √u n'est dérivable que là où u > 0, même si u s'annule en un point où √u est définie.
:::

::: verifie
Soit f(x) = √(x² + x + 1). Justifier que f est dérivable sur ℝ et calculer f′(0).

---

Le trinôme u(x) = x² + x + 1 a pour discriminant 1 − 4 = −3 < 0, donc u(x) > 0 pour tout x : √u est dérivable sur ℝ. Alors f′(x) = u′/(2√u) = (2x + 1)/(2√(x² + x + 1)), et f′(0) = 1/(2√1) = 1/2.
:::

::: retenir
(g∘f)′ = f′ × (g′∘f) : on dérive l'extérieur sans toucher à l'intérieur, puis l'on multiplie par la dérivée de l'intérieur ; (√u)′ = u′/(2√u) n'a de sens que pour u > 0.
:::

## 🪞 Dériver une fonction réciproque

Sur ℝ₊, f(x) = x² a pour réciproque f⁻¹(y) = √y. La tangente à C_f en A(2 ; 4) a pour pente f′(2) = 4. La courbe de f⁻¹ est la symétrique de C_f par rapport à la droite y = x.
Quelle est la pente de sa tangente au point symétrique A′(4 ; 2) ? Et que faire quand on ne sait pas écrire la réciproque ?

::: figure Les deux courbes sont symétriques par rapport à y = x, et leurs tangentes aussi : la pente 4 en A devient la pente 1/4 en A′
<svg viewBox="0 0 300 300"><title>Courbes de x ↦ x² et de sa réciproque x ↦ √x, symétriques par rapport à y = x ; tangentes de pentes 4 en A(2 ; 4) et 1/4 en A′(4 ; 2)</title><line x1="14" y1="267" x2="290" y2="267" stroke="#0f172a" stroke-width="1.6"/><line x1="33" y1="286" x2="33" y2="10" stroke="#0f172a" stroke-width="1.6"/><polygon points="290,267 283,263.5 283,270.5" fill="#0f172a"/><polygon points="33,10 29.5,17 36.5,17" fill="#0f172a"/><text x="286" y="260" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="41" y="18" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="80.6" y1="264" x2="80.6" y2="270" stroke="#0f172a" stroke-width="1.3"/><text x="80.6" y="282" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="128.2" y1="264" x2="128.2" y2="270" stroke="#0f172a" stroke-width="1.3"/><text x="128.2" y="282" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="223.4" y1="264" x2="223.4" y2="270" stroke="#0f172a" stroke-width="1.3"/><text x="223.4" y="282" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="30" y1="219.4" x2="36" y2="219.4" stroke="#0f172a" stroke-width="1.3"/><text x="27" y="223.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="30" y1="171.8" x2="36" y2="171.8" stroke="#0f172a" stroke-width="1.3"/><text x="27" y="175.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="30" y1="76.6" x2="36" y2="76.6" stroke="#0f172a" stroke-width="1.3"/><text x="27" y="80.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="18.8" y1="281.2" x2="280.5" y2="19.5" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><polyline points="33,267 35.2,266.9 37.4,266.6 39.5,266.1 41.7,265.4 43.9,264.5 46.1,263.4 48.2,262.1 50.4,260.6 52.6,259 54.7,257.1 56.9,255 59.1,252.7 61.2,250.2 63.4,247.6 65.6,244.7 67.8,241.6 69.9,238.4 72.1,234.9 74.3,231.2 76.4,227.4 78.6,223.3 80.8,219.1 82.9,214.6 85.1,210 87.3,205.1 89.5,200.1 91.6,194.8 93.8,189.4 96,183.7 98.1,177.9 100.3,171.9 102.5,165.6 104.6,159.2 106.8,152.6 109,145.8 111.2,138.7 113.3,131.5 115.5,124.1 117.7,116.5 119.8,108.6 122,100.6 124.2,92.4 126.3,84 128.5,75.4 130.7,66.6 132.9,57.6 135,48.4 137.2,39 139.4,29.4 141.5,19.6" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="33,267 36.6,254 40.1,248.6 43.6,244.5 47.2,241 50.7,238 54.2,235.2 57.8,232.7 61.3,230.3 64.8,228.1 68.4,226 71.9,223.9 75.5,222 79,220.2 82.5,218.4 86.1,216.7 89.6,215.1 93.1,213.5 96.7,211.9 100.2,210.4 103.7,209 107.3,207.5 110.8,206.1 114.3,204.8 117.9,203.4 121.4,202.1 124.9,200.8 128.5,199.6 132,198.3 135.5,197.1 139.1,195.9 142.6,194.8 146.2,193.6 149.7,192.5 153.2,191.3 156.8,190.2 160.3,189.1 163.8,188.1 167.4,187 170.9,186 174.4,184.9 178,183.9 181.5,182.9 185,181.9 188.6,180.9 192.1,180 195.6,179 199.2,178 202.7,177.1 206.2,176.2 209.8,175.3 213.3,174.3 216.9,173.4 220.4,172.5 223.9,171.7 227.5,170.8 231,169.9 234.5,169 238.1,168.2 241.6,167.3 245.1,166.5 248.7,165.7 252.2,164.8 255.7,164 259.3,163.2 262.8,162.4 266.3,161.6 269.9,160.8 273.4,160 276.9,159.2 280.5,158.5" fill="none" stroke="#7c3aed" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="94.9" y1="209.9" x2="142.5" y2="19.5" stroke="#b45309" stroke-width="2"/><line x1="80.6" y1="207.5" x2="280.5" y2="157.5" stroke="#b45309" stroke-width="2"/><circle cx="128.2" cy="76.6" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="223.4" cy="171.8" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="120.2" y="70.6" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="225.4" y="189.8" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A′</text><text x="96.4" y="109.9" text-anchor="end" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pente 4</text><text x="266.2" y="138.3" text-anchor="middle" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pente 1/4</text><text x="97.2" y="145.1" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f</text><text x="175.8" y="206.5" text-anchor="middle" font-size="13" font-weight="700" fill="#7c3aed" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f⁻¹</text><text x="256.7" y="33.8" text-anchor="middle" font-size="11" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = x</text></svg>
:::

La symétrie échange abscisses et ordonnées : monter de 4 quand on avance de 1 devient monter de 1 quand on avance de 4. La pente de f⁻¹ en A′ est donc l'inverse de la pente de f en A.

::: exemple Les nombres de la figure : f(x) = x² sur ℝ₊, (f⁻¹)′(4)
1. f(2) = 4, donc f⁻¹(4) = 2 : l'antécédent de 4 est 2.
2. f′(x) = 2x, donc f′(2) = 4, un nombre non nul.
3. (f⁻¹)′(4) = 1/f′(f⁻¹(4)) = 1/f′(2) = 1/4. Contrôle : f⁻¹ = √ et (√)′(4) = 1/(2√4) = 1/4 ✓.

:::

::: exemple Une réciproque qu'on ne sait pas écrire : f(x) = x³ + x + 1
1. f est somme de fonctions strictement croissantes et continue sur ℝ : c'est une bijection de ℝ sur ℝ (chapitre 3), mais f⁻¹ n'a pas d'expression simple.
2. Pour (f⁻¹)′(3), il faut d'abord l'antécédent de 3 : f(1) = 1 + 1 + 1 = 3, donc f⁻¹(3) = 1.
3. f′(x) = 3x² + 1, donc f′(1) = 4, et (f⁻¹)′(3) = 1/f′(1) = 1/4.

:::

::: exemple La réciproque du sinus : f = sin sur [0 ; π/2]
1. sin est continue et strictement croissante sur [0 ; π/2], d'image [0 ; 1] : c'est une bijection de [0 ; π/2] sur [0 ; 1].
2. On veut (f⁻¹)′(1/2). Comme sin(π/6) = 1/2, f⁻¹(1/2) = π/6.
3. f′(π/6) = cos(π/6) = √3/2, non nul, donc (f⁻¹)′(1/2) = 1/cos(π/6) = 2/√3 = 2√3/3.

:::

::: piege Évaluer f′ au mauvais point
Pour f(x) = x³ + x + 1, on écrit (f⁻¹)′(3) = 1/f′(3) = 1/28. Cela tente parce que le nombre 3 figure dans la question. Mais 3 est la valeur y = f(x) : f′ doit être évaluée à l'antécédent x = f⁻¹(3) = 1. Un test avec f(x) = x² le montre : 1/f′(4) = 1/8, alors que (√)′(4) = 1/4.
:::

::: propriete
Soit f continue et strictement monotone sur I, donc bijection de I sur J = f(I). Si f est dérivable en x₀ de I et si f′(x₀) ≠ 0, alors f⁻¹ est dérivable en y₀ = f(x₀) et :

$$ (f⁻¹)′(y₀) = 1/f′(f⁻¹(y₀)) = 1/f′(x₀) $$

La raison : f⁻¹(f(x)) = x, et dériver cette égalité par la formule de la composée donne (f⁻¹)′(f(x)) × f′(x) = 1.

Cas limite : si f′(x₀) = 0, f⁻¹ n'est pas dérivable en f(x₀) : sa courbe a une tangente verticale. Ainsi x ↦ x² sur ℝ₊ a f′(0) = 0, et sa réciproque √ n'est pas dérivable en 0.
:::

::: verifie
Soit f(x) = x³ + 3x, bijection de ℝ sur ℝ. Calculer (f⁻¹)′(4).

---

On cherche l'antécédent de 4 : f(1) = 1 + 3 = 4, donc f⁻¹(4) = 1. Puis f′(x) = 3x² + 3 et f′(1) = 6, non nul. D'où (f⁻¹)′(4) = 1/f′(1) = 1/6 : on a évalué f′ à l'antécédent 1, pas en 4.
:::

::: retenir
(f⁻¹)′(y) = 1/f′(f⁻¹(y)) quand f′(f⁻¹(y)) ≠ 0 : on cherche d'abord l'antécédent x de y, puis l'on inverse f′(x).
:::

## 📐 Théorème et inégalité des accroissements finis

Un sentier suit la courbe d'équation y = −x² + 6x − 5 (en hectomètres) entre A(1 ; 0) et B(4 ; 3). La route droite [AB] monte de 3 hm pour 3 hm parcourus horizontalement : sa pente est 1.
Existe-t-il un point du sentier où la pente est exactement 1, la pente moyenne ?

::: figure Entre A et B, la tangente au point d'abscisse c est parallèle à la corde (AB) : elles ont la même pente 1
<svg viewBox="0 0 340 250"><title>Courbe de x ↦ −x² + 6x − 5 entre A(1 ; 0) et B(4 ; 3), la corde (AB) de pente 1 et la tangente parallèle au point d'abscisse c</title><line x1="20" y1="161.4" x2="320" y2="161.4" stroke="#0f172a" stroke-width="1.6"/><line x1="20" y1="224" x2="20" y2="10" stroke="#0f172a" stroke-width="1.6"/><polygon points="320,161.4 313,157.9 313,164.9" fill="#0f172a"/><polygon points="20,10 16.5,17 23.5,17" fill="#0f172a"/><text x="316" y="154.4" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="9.6" y="18" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="62.9" y1="158.4" x2="62.9" y2="164.4" stroke="#0f172a" stroke-width="1.3"/><text x="62.9" y="176.4" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="154.7" y1="158.4" x2="154.7" y2="164.4" stroke="#0f172a" stroke-width="1.3"/><text x="154.7" y="176.4" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">c</text><line x1="246.5" y1="158.4" x2="246.5" y2="164.4" stroke="#0f172a" stroke-width="1.3"/><text x="246.5" y="176.4" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="17" y1="62.7" x2="23" y2="62.7" stroke="#0f172a" stroke-width="1.3"/><text x="14" y="66.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><polyline points="50.6,189.1 54.4,180.3 58.1,171.8 61.9,163.5 65.7,155.5 69.4,147.7 73.2,140.2 76.9,132.9 80.7,125.9 84.5,119.1 88.2,112.5 92,106.2 95.7,100.2 99.5,94.4 103.3,88.9 107,83.6 110.8,78.5 114.5,73.7 118.3,69.2 122.1,64.9 125.8,60.8 129.6,57 133.4,53.5 137.1,50.2 140.9,47.1 144.6,44.3 148.4,41.7 152.2,39.4 155.9,37.3 159.7,35.5 163.4,34 167.2,32.6 171,31.6 174.7,30.7 178.5,30.2 182.2,29.8 186,29.8 189.8,29.9 193.5,30.3 197.3,31 201,31.9 204.8,33.1 208.6,34.5 212.3,36.2 216.1,38.1 219.9,40.2 223.6,42.6 227.4,45.3 231.1,48.2 234.9,51.4 238.7,54.8 242.4,58.4 246.2,62.3 249.9,66.4 253.7,70.8 257.5,75.5 261.2,80.4 265,85.5 268.7,90.9 272.5,96.5 276.3,102.4 280,108.6 283.8,114.9 287.6,121.6 291.3,128.5 295.1,135.6 298.8,143 302.6,150.6 306.4,158.5 310.1,166.6 313.9,174.9" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="32.2" y1="177.9" x2="283.3" y2="42.9" stroke="#64748b" stroke-width="1.8"/><line x1="44.5" y1="97.2" x2="203.7" y2="11.6" stroke="#b45309" stroke-width="2.2"/><line x1="154.7" y1="161.4" x2="154.7" y2="38" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="62.9" y1="161.4" x2="62.9" y2="161.4" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="246.5" y1="161.4" x2="246.5" y2="62.7" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="20" y1="62.7" x2="246.5" y2="62.7" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><circle cx="62.9" cy="161.4" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="246.5" cy="62.7" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="154.7" cy="38" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="72.9" y="179.4" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="254.5" y="78.7" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="166.9" y="151.6" text-anchor="start" font-size="11" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(AB) : pente 1</text><text x="140.7" y="26" text-anchor="end" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente : pente 1</text><text x="301.8" y="190.4" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text></svg>
:::

La pente de la corde (AB) est le quotient (f(4) − f(1))/(4 − 1). Le point d'abscisse c de la figure est celui où la tangente est parallèle à cette corde.

::: exemple Le point à pente moyenne
1. f(x) = −x² + 6x − 5 est un polynôme : continue sur [1 ; 4] et dérivable sur ]1 ; 4[.
2. La pente de (AB) est (f(4) − f(1))/(4 − 1) = (3 − 0)/3 = 1.
3. On cherche c dans ]1 ; 4[ avec f′(c) = 1. Or f′(x) = −2x + 6, donc −2c + 6 = 1 et c = 5/2.
4. 5/2 est bien dans ]1 ; 4[ : au point d'ordonnée f(5/2) = 15/4, la tangente est parallèle à (AB).

:::

::: exemple Encadrer √26 sans calculatrice
1. f(x) = √x est continue sur [25 ; 26] et dérivable sur ]25 ; 26[, avec f′(x) = 1/(2√x).
2. Pour 25 < x < 26, on a 5 < √x < 5,1 (car 5,1² = 26,01), donc 1/(2 × 5,1) < f′(x) < 1/(2 × 5), c'est-à-dire 1/10,2 < f′(x) < 1/10.
3. On applique l'inégalité ci-dessous avec b − a = 1 : 1/10,2 ≤ √26 − 5 ≤ 1/10. Comme 1/10,2 > 0,098, on obtient 5,098 ≤ √26 ≤ 5,1.

:::

::: exemple Une inégalité vraie pour tous les réels
1. f(x) = sin x est dérivable sur ℝ et f′(x) = cos x vérifie |f′(x)| ≤ 1 pour tout x.
2. Le corollaire ci-dessous, avec k = 1, donne |sin b − sin a| ≤ |b − a| pour tous réels a et b : le sinus ne varie jamais plus vite que sa variable.

:::

::: piege Croire que c est le milieu de [a ; b]
Dans le premier exemple, c = 5/2 est le milieu de [1 ; 4], et l'on généralise « c = (a + b)/2 ». Cela tente parce que c'est vrai pour une parabole. Mais pour f(x) = x³ sur [0 ; 3], f(3) − f(0) = 27 donne 3c² × 3 = 27, soit c = √3 ≈ 1,73, qui n'est pas le milieu 1,5. Le théorème affirme qu'un c existe ; on le calcule en résolvant f′(c) = (f(b) − f(a))/(b − a).
:::

::: propriete
**Théorème des accroissements finis (admis)** : si f est continue sur [a ; b] et dérivable sur ]a ; b[, il existe au moins un réel c de ]a ; b[ tel que f(b) − f(a) = (b − a) f′(c).

**Inégalité des accroissements finis** : sous les mêmes hypothèses, si m ≤ f′(x) ≤ M pour tout x de ]a ; b[, alors m ≤ (f(b) − f(a))/(b − a) ≤ M.

**Corollaire** : si f est dérivable sur un intervalle I et si |f′(x)| ≤ k sur I, alors |f(b) − f(a)| ≤ k|b − a| pour tous a et b de I.

Cas limite : l'hypothèse de dérivabilité compte. f(x) = |x| sur [−1 ; 2] a pour pente de corde 1/3, mais f′ ne prend que les valeurs −1 et 1 : aucun c ne convient, car f n'est pas dérivable en 0.
:::

::: verifie
Soit f(x) = x³ + x sur [0 ; 2]. Trouver le réel c du théorème des accroissements finis.

---

f(2) − f(0) = 10 − 0 = 10, sur une longueur 2 : la pente de la corde est 5. On résout f′(c) = 3c² + 1 = 5, donc c² = 4/3 et c = 2/√3 ≈ 1,15 (la valeur négative est rejetée : elle n'est pas dans ]0 ; 2[). Ce n'est pas le milieu 1.
:::

::: retenir
Entre a et b, une tangente est parallèle à la corde : f(b) − f(a) = (b − a)f′(c) ; encadrer f′ entre m et M encadre le taux entre m et M, et borner |f′| par k borne |f(b) − f(a)| par k|b − a|.
:::

## 🧗 Signe de la dérivée, variations et extrémums

Le profil d'un sentier de montagne est la courbe de f(x) = (1/3)x³ − (3/2)x² + 2x + 1. On calcule f(0) = 1, f(1) = 11/6 ≈ 1,83, f(2) = 5/3 ≈ 1,67 puis f(3) = 5/2 : le sentier monte, descend, remonte.
Comment le savoir sans tracer la courbe, et où sont le sommet et le creux ?

::: exemple Le tableau de variation du sentier
1. f est un polynôme : f′(x) = x² − 3x + 2 = (x − 1)(x − 2).
2. Un trinôme est positif à l'extérieur de ses racines 1 et 2, et négatif entre elles.
3. Le signe de f′ donne les variations :

| x | ]−∞ ; 1[ | ]1 ; 2[ | ]2 ; +∞[ |
| --- | --- | --- | --- |
| signe de f′ | + | − | + |
| variation de f | croissante | décroissante | croissante |

4. En 1 et en 2, f′ vaut 0, ce qui reste compatible avec f′ ≥ 0 puis f′ ≤ 0 : f est croissante sur ]−∞ ; 1], décroissante sur [1 ; 2], croissante sur [2 ; +∞[.
5. f′ s'annule en 1 en passant de + à − : maximum local f(1) = 11/6. En 2, de − à + : minimum local f(2) = 5/3.

:::

::: exemple Une dérivée toujours positive : f(x) = x³ + 3x
1. f′(x) = 3x² + 3 est strictement positive pour tout réel x, car 3x² ≥ 0.
2. f est donc strictement croissante sur ℝ : elle ne s'arrête jamais de monter, elle n'a aucun extrémum.

:::

::: piege Appliquer le signe de f′ sur un ensemble qui n'est pas un intervalle
Pour f(x) = −1/x sur ℝ*, f′(x) = 1/x² > 0, et l'on conclut « f est strictement croissante sur ℝ* ». Cela tente parce que f′ est positive partout où f est définie. Mais f(−1) = 1 et f(1) = −1 : −1 < 1 et pourtant f(−1) > f(1). La propriété exige un intervalle : f est strictement croissante sur ]−∞ ; 0[ et sur ]0 ; +∞[, séparément.
:::

::: propriete
Soit f dérivable sur un intervalle I.
- Si f′ > 0 sur I, f est strictement croissante sur I ; si f′ < 0, strictement décroissante ; si f′ = 0, constante. (Preuve par le théorème des accroissements finis : pour a < b, f(b) − f(a) = f′(c)(b − a) a le signe de f′(c).)
- f est croissante sur I si et seulement si f′ ≥ 0 sur I ; décroissante si et seulement si f′ ≤ 0.
- **Extrémum** : si f admet un maximum ou un minimum local en a (f(x) ≤ f(a), ou f(x) ≥ f(a), pour x voisin de a), alors f′(a) = 0. Si f′ s'annule en a en changeant de signe, f admet un extrémum local en a.

Cas limite : le sens est direct seulement. x ↦ x³ est strictement croissante, mais f′(0) = 0 ; et f′(0) = 0 ne donne pas d'extrémum, car f′ = 3x² ne change pas de signe.
:::

::: verifie
Dresser le tableau de variation de f(x) = x³ − 12x et donner ses extrémums locaux.

---

f′(x) = 3x² − 12 = 3(x − 2)(x + 2), positive pour x < −2, négative entre −2 et 2, positive pour x > 2. Donc f croît sur ]−∞ ; −2], décroît sur [−2 ; 2], croît sur [2 ; +∞[. Le signe passe de + à − en −2 : maximum local f(−2) = −8 + 24 = 16. Il passe de − à + en 2 : minimum local f(2) = 8 − 24 = −16.
:::

::: retenir
f′ > 0 donne f strictement croissante, f′ < 0 strictement décroissante, sur un intervalle ; un extrémum local d'une fonction dérivable annule f′, mais f′(a) = 0 n'en donne un que si f′ change de signe.
:::

## 🎢 Dérivée seconde et point d'inflexion

Sur un toboggan de profil f(x) = x³ − 3x² + 2x, la pente f′ diminue d'abord, puis augmente. Au moment du changement, la tangente à la courbe traverse la courbe au lieu de rester d'un seul côté.
En quel point cela se produit-il, et comment le repérer par le calcul ?

::: definition
Soit f dérivable sur un intervalle ouvert I, telle que f′ soit dérivable sur I. La **dérivée seconde** de f, notée **f″**, est la dérivée de f′ : f″(x) = (f′)′(x) pour tout x de I.

Un point M₀(x₀ ; f(x₀)) de C_f où la tangente existe et **traverse** la courbe est un **point d'inflexion**.
:::

::: figure En I(1 ; 0), la tangente traverse la courbe : celle-ci passe de l'autre côté de sa tangente
<svg viewBox="0 0 340 240"><title>Courbe de x ↦ x³ − 3x² + 2x et sa tangente y = −x + 1 au point I(1 ; 0) : la courbe est au-dessous de la tangente à gauche de I, au-dessus à droite</title><line x1="20" y1="112.9" x2="320" y2="112.9" stroke="#0f172a" stroke-width="1.6"/><line x1="70" y1="210" x2="70" y2="10" stroke="#0f172a" stroke-width="1.6"/><polygon points="320,112.9 313,109.4 313,116.4" fill="#0f172a"/><polygon points="70,10 66.5,17 73.5,17" fill="#0f172a"/><text x="316" y="105.9" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="78" y="18" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="170" y1="109.9" x2="170" y2="115.9" stroke="#0f172a" stroke-width="1.3"/><text x="170" y="127.9" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="270" y1="109.9" x2="270" y2="115.9" stroke="#0f172a" stroke-width="1.3"/><text x="270" y="127.9" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><polyline points="40,164.1 43.2,156.8 46.5,149.9 49.8,143.5 53,137.5 56.2,132 59.5,126.8 62.7,122.1 66,117.7 69.2,113.7 72.5,110.1 75.7,106.8 79,103.9 82.2,101.3 85.5,99 88.8,97.1 92,95.4 95.2,94 98.5,92.9 101.7,92 105,91.4 108.2,91 111.5,90.9 114.7,90.9 118,91.2 121.2,91.6 124.5,92.2 127.7,93 131,94 134.2,95 137.5,96.2 140.7,97.6 144,99 147.2,100.5 150.5,102.1 153.7,103.8 157,105.6 160.2,107.3 163.5,109.2 166.7,111 170,112.9 173.2,114.7 176.5,116.6 179.7,118.4 183,120.2 186.2,121.9 189.5,123.6 192.8,125.2 196,126.7 199.2,128.1 202.5,129.5 205.8,130.7 209,131.8 212.2,132.7 215.5,133.5 218.7,134.1 222,134.5 225.2,134.8 228.5,134.8 231.7,134.7 235,134.3 238.2,133.7 241.5,132.8 244.7,131.7 248,130.3 251.2,128.6 254.5,126.7 257.8,124.4 261,121.8 264.2,118.9 267.5,115.6 270.8,112 274,108 277.2,103.6 280.5,98.9 283.7,93.8 287,88.2 290.2,82.2 293.5,75.8 296.8,68.9 300,61.6" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="50" y1="44.3" x2="290" y2="181.4" stroke="#b45309" stroke-width="2.2"/><circle cx="170" cy="112.9" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="180" y="103.9" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I</text><text x="110" y="20.3" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente en I</text><text x="294" y="46" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text></svg>
:::

La figure montre la tangente en I(1 ; 0) : à gauche la courbe est sous elle, à droite au-dessus. L'exemple retrouve ce point par f″.

::: exemple Le toboggan : f(x) = x³ − 3x² + 2x
1. f′(x) = 3x² − 6x + 2 et f″(x) = 6x − 6 = 6(x − 1).
2. f″ s'annule en 1 en passant du négatif au positif : f′ diminue jusqu'en 1, puis augmente.
3. f(1) = 1 − 3 + 2 = 0 et f′(1) = 3 − 6 + 2 = −1 : la tangente en I(1 ; 0) est y = −(x − 1) = −x + 1.
4. f(x) − (−x + 1) = x³ − 3x² + 3x − 1 = (x − 1)³, négatif pour x < 1 et positif pour x > 1 : la courbe traverse bien sa tangente en I.

:::

::: exemple Une inflexion en un point plus facile : g(x) = sin(2x)
1. g′(x) = 2cos(2x), puis g″(x) = −4 sin(2x), car (cos(2x))′ = −2 sin(2x).
2. g″ s'annule en 0, positive juste avant (sin(2x) < 0 pour x < 0 proche de 0) et négative juste après.
3. Donc O(0 ; 0) est un point d'inflexion de C_g : sa tangente y = 2x traverse la courbe.

:::

::: piege Conclure à une inflexion dès que f″(x₀) = 0
Pour h(x) = x⁴, h″(x) = 12x² s'annule en 0, et l'on écrit « l'origine est un point d'inflexion ». Cela tente parce que f″ s'annulait aussi en 1 dans l'exemple du toboggan. Mais 12x² reste positive de part et d'autre de 0 : la courbe de x⁴ reste au-dessus de sa tangente y = 0 et ne la traverse pas. Il faut un changement de signe de f″.
:::

::: propriete
Soit f deux fois dérivable sur un intervalle I et x₀ un réel de I. Le point M₀(x₀ ; f(x₀)) est un point d'inflexion de C_f si et seulement si f″ s'annule et change de signe en x₀.

Cas limite : f″ doit exister en x₀. f(x) = 1/x a pour dérivée seconde f″(x) = 2/x³, qui change de signe en 0, mais 0 n'est pas dans l'ensemble de définition : il n'y a pas de point d'inflexion.
:::

::: verifie
Montrer que la courbe de g(x) = x³ + 3x² admet un point d'inflexion et donner sa tangente.

---

g′(x) = 3x² + 6x et g″(x) = 6x + 6 = 6(x + 1), qui s'annule en −1 en changeant de signe : point d'inflexion d'abscisse −1. g(−1) = −1 + 3 = 2 et g′(−1) = 3 − 6 = −3, donc la tangente est y = −3(x + 1) + 2 = −3x − 1. Contrôle : g(x) + 3x + 1 = (x + 1)³ change de signe en −1.
:::

::: retenir
f″ est la dérivée de f′ ; M₀ est un point d'inflexion exactement quand f″ s'annule et change de signe en x₀, et la tangente traverse alors la courbe.
:::

## 🌊 Primitives : remonter de la pente à la fonction

Un drone monte avec la vitesse v(t) = 4t + 3 mètres par seconde, et part de l'altitude x(0) = 10 m. On cherche son altitude x(t) : une fonction dont la dérivée est v.
Combien de fonctions ont pour dérivée 4t + 3, et comment trouver la bonne ?

::: definition
Soit f définie sur un intervalle I. On appelle **primitive** de f sur I toute fonction F dérivable sur I telle que F′(x) = f(x) pour tout x de I.
:::

::: figure Les courbes de F, F + 2 et F − 1 se déduisent l'une de l'autre par une translation verticale : en x = 1, leurs tangentes sont parallèles
<svg viewBox="0 0 340 240"><title>Trois courbes y = x²/2 + λ, translatées verticalement l'une de l'autre, avec en x = 1 trois tangentes parallèles de pente 1</title><line x1="20" y1="162.9" x2="320" y2="162.9" stroke="#0f172a" stroke-width="1.6"/><line x1="149.4" y1="210" x2="149.4" y2="10" stroke="#0f172a" stroke-width="1.6"/><polygon points="320,162.9 313,159.4 313,166.4" fill="#0f172a"/><polygon points="149.4,10 145.9,17 152.9,17" fill="#0f172a"/><text x="316" y="155.9" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="157.4" y="18" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="208.2" y1="159.9" x2="208.2" y2="165.9" stroke="#0f172a" stroke-width="1.3"/><text x="208.2" y="177.9" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><polyline points="31.8,45.3 36.1,49.5 40.4,53.6 44.7,57.5 49,61.3 53.3,64.9 57.6,68.3 62,71.6 66.3,74.7 70.6,77.7 74.9,80.5 79.2,83.2 83.5,85.7 87.8,88 92.2,90.2 96.5,92.2 100.8,94.1 105.1,95.8 109.4,97.3 113.7,98.7 118,99.9 122.4,101 126.7,101.9 131,102.7 135.3,103.3 139.6,103.7 143.9,104 148.2,104.1 152.5,104.1 156.9,103.9 161.2,103.5 165.5,103 169.8,102.4 174.1,101.5 178.4,100.5 182.7,99.4 187.1,98.1 191.4,96.6 195.7,95 200,93.2 204.3,91.3 208.6,89.2 212.9,87 217.3,84.6 221.6,82 225.9,79.3 230.2,76.4 234.5,73.3 238.8,70.1 243.1,66.8 247.5,63.3 251.8,59.6 256.1,55.8 260.4,51.8 264.7,47.6 269,43.3 273.3,38.9 277.6,34.2 282,29.4 286.3,24.5 290.6,19.4" fill="none" stroke="#7c3aed" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="155.3" y1="115.9" x2="261.2" y2="62.9" stroke="#0f172a" stroke-width="1.8"/><circle cx="208.2" cy="89.4" r="3.5" fill="#7c3aed" stroke="#0f172a" stroke-width="1"/><text x="296.6" y="23.4" text-anchor="start" font-size="11" font-weight="700" fill="#7c3aed" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F + 2</text><polyline points="31.8,104.1 36.1,108.4 40.4,112.4 44.7,116.3 49,120.1 53.3,123.7 57.6,127.2 62,130.4 66.3,133.6 70.6,136.5 74.9,139.3 79.2,142 83.5,144.5 87.8,146.8 92.2,149 96.5,151 100.8,152.9 105.1,154.6 109.4,156.1 113.7,157.5 118,158.8 122.4,159.8 126.7,160.7 131,161.5 135.3,162.1 139.6,162.5 143.9,162.8 148.2,162.9 152.5,162.9 156.9,162.7 161.2,162.4 165.5,161.8 169.8,161.2 174.1,160.3 178.4,159.4 182.7,158.2 187.1,156.9 191.4,155.5 195.7,153.8 200,152.1 204.3,150.1 208.6,148 212.9,145.8 217.3,143.4 221.6,140.8 225.9,138.1 230.2,135.2 234.5,132.2 238.8,129 243.1,125.6 247.5,122.1 251.8,118.4 256.1,114.6 260.4,110.6 264.7,106.4 269,102.1 273.3,97.7 277.6,93.1 282,88.3 286.3,83.3 290.6,78.2" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="155.3" y1="174.7" x2="261.2" y2="121.8" stroke="#0f172a" stroke-width="1.8"/><circle cx="208.2" cy="148.2" r="3.5" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="296.6" y="82.2" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text><polyline points="31.8,133.5 36.1,137.8 40.4,141.8 44.7,145.8 49,149.5 53.3,153.1 57.6,156.6 62,159.9 66.3,163 70.6,165.9 74.9,168.8 79.2,171.4 83.5,173.9 87.8,176.2 92.2,178.4 96.5,180.4 100.8,182.3 105.1,184 109.4,185.6 113.7,186.9 118,188.2 122.4,189.2 126.7,190.2 131,190.9 135.3,191.5 139.6,191.9 143.9,192.2 148.2,192.3 152.5,192.3 156.9,192.1 161.2,191.8 165.5,191.3 169.8,190.6 174.1,189.8 178.4,188.8 182.7,187.6 187.1,186.3 191.4,184.9 195.7,183.3 200,181.5 204.3,179.5 208.6,177.5 212.9,175.2 217.3,172.8 221.6,170.2 225.9,167.5 230.2,164.6 234.5,161.6 238.8,158.4 243.1,155 247.5,151.5 251.8,147.8 256.1,144 260.4,140 264.7,135.9 269,131.6 273.3,127.1 277.6,122.5 282,117.7 286.3,112.7 290.6,107.6" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="155.3" y1="204.1" x2="261.2" y2="151.2" stroke="#0f172a" stroke-width="1.8"/><circle cx="208.2" cy="177.6" r="3.5" fill="#b45309" stroke="#0f172a" stroke-width="1"/><text x="296.6" y="111.6" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F − 1</text><line x1="208.2" y1="210" x2="208.2" y2="74.7" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/></svg>
:::

Les trois courbes sont celles de F(x) = x²/2 + λ pour λ = −1, 0 et 2, primitives de f(x) = x : chaque tangente tracée en x = 1 a pour pente f(1) = 1, et elles sont parallèles.

::: exemple L'altitude du drone
1. On cherche x avec x′(t) = 4t + 3. Comme (t²)′ = 2t, (2t²)′ = 4t, et (3t)′ = 3 : x(t) = 2t² + 3t convient.
2. Mais 2t² + 3t + 10 convient aussi, ainsi que 2t² + 3t − 7 : ajouter une constante ne change pas la dérivée.
3. La condition x(0) = 10 choisit : x(0) = 0 + 0 + λ = 10, donc λ = 10 et x(t) = 2t² + 3t + 10. Contrôle : x′(t) = 4t + 3 et x(0) = 10 ✓.

:::

::: exemple Vérifier qu'une fonction est une primitive : F(x) = x/(x² + 1)
1. Pour montrer que F est une primitive de f(x) = (1 − x²)/(x² + 1)² sur ℝ, on dérive F, jamais f : F est dérivable sur ℝ, car x² + 1 > 0.
2. F′(x) = ((x² + 1) × 1 − x × 2x)/(x² + 1)² = (1 − x²)/(x² + 1)² = f(x) pour tout x ✓.

:::

::: piege Oublier la constante, puis conclure à l'impossible
Pour le drone, on prend x(t) = 2t² + 3t et l'on impose x(0) = 10 : on trouve 0 ≠ 10 et l'on écrit « pas de solution ». Cela tente parce que 2t² + 3t est bien une primitive de v. Mais ce n'est qu'une primitive parmi d'autres : toutes s'écrivent 2t² + 3t + λ, et la condition x(0) = 10 fixe λ = 10.
:::

::: propriete
- **Théorème (admis)** : toute fonction continue sur un intervalle I admet une primitive sur I.
- **Théorème** : si F est une primitive de f sur I, toute autre primitive G de f sur I est de la forme G(x) = F(x) + λ, avec λ une constante. En effet (G − F)′ = f − f = 0 sur I, donc G − F est constante.
- **Corollaire** : pour x₀ de I et y₀ réel, f continue admet une **unique** primitive F sur I telle que F(x₀) = y₀.

Cas limite : la fonction nulle a pour primitives les fonctions constantes, et la condition F(x₀) = y₀ choisit la constante y₀.
:::

::: verifie
Déterminer la primitive F de f(x) = 6x² + 4 sur ℝ telle que F(1) = 0.

---

Les primitives de f sont F(x) = 2x³ + 4x + λ (on dérive pour contrôler : 6x² + 4). La condition F(1) = 2 + 4 + λ = 0 donne λ = −6, donc F(x) = 2x³ + 4x − 6. Contrôle : F(1) = 2 + 4 − 6 = 0 ✓.
:::

::: retenir
F est une primitive de f quand F′ = f sur un intervalle ; toutes les primitives diffèrent d'une constante, et une condition F(x₀) = y₀ en isole une seule.
:::

## 📚 Primitives usuelles et linéarité

Dériver sin(3x) donne 3cos(3x). Lue à l'envers, cette formule dit qu'une primitive de cos(3x) est (1/3) sin(3x). Chaque formule de dérivée, lue à l'envers, fournit une formule de primitive.
Comment organiser ces formules pour primitiver une fonction comme 6x² − cos(3x), sans deviner ?

La table donne une primitive de chaque fonction ; on ajoute une constante c pour obtenir toutes les primitives.

| f(x) | une primitive F(x) | sur I |
| --- | --- | --- |
| k (constante) | kx | ℝ |
| ax + b | ax²/2 + bx | ℝ |
| xⁿ (n entier ≥ 1) | xⁿ⁺¹/(n + 1) | ℝ |
| xⁿ (n entier ≤ −2) | xⁿ⁺¹/(n + 1) | ]−∞ ; 0[ ou ]0 ; +∞[ |
| 1/√x | 2√x | ]0 ; +∞[ |
| √x | (2/3)x√x | [0 ; +∞[ |
| cos x | sin x | ℝ |
| sin x | −cos x | ℝ |
| 1 + tan²x = 1/cos²x | tan x | ]−π/2 + kπ ; π/2 + kπ[ |
| cos(ax + b), a ≠ 0 | (1/a) sin(ax + b) | ℝ |
| sin(ax + b), a ≠ 0 | −(1/a) cos(ax + b) | ℝ |

::: exemple Primitiver terme à terme : f(x) = 6x² − cos(3x)
1. 6x² = 6 × x² : la ligne xⁿ avec n = 2 donne x³/3, donc 6x² a pour primitive 6 × x³/3 = 2x³.
2. cos(3x) : la ligne cos(ax + b) avec a = 3 donne (1/3) sin(3x), donc −cos(3x) a pour primitive −(1/3) sin(3x).
3. F(x) = 2x³ − (1/3) sin(3x). Contrôle en dérivant : F′(x) = 6x² − cos(3x) ✓.

:::

::: exemple Des puissances négatives et une racine : f(x) = 5/x² + 1/√x sur ]0 ; +∞[
1. 5/x² = 5x⁻² : la ligne xⁿ avec n = −2 donne x⁻¹/(−1) = −1/x, donc une primitive de 5/x² est −5/x.
2. Une primitive de 1/√x est 2√x.
3. F(x) = −5/x + 2√x. Contrôle : F′(x) = 5/x² + 2 × 1/(2√x) = 5/x² + 1/√x ✓.

:::

::: piege Primitiver un produit facteur par facteur
Pour f(x) = x × x = x², on écrit « une primitive de x est x²/2, donc une primitive de x × x est (x²/2)(x²/2) = x⁴/4 ». Cela tente parce que la somme se primitive terme à terme. Mais (x⁴/4)′ = x³ ≠ x² : la bonne primitive est x³/3. La linéarité ne parle que des sommes et des facteurs constants.
:::

::: propriete
**Linéarité (théorème)** : si F et G sont des primitives de f et g sur I, alors pour tous réels α et β, αF + βG est une primitive de αf + βg sur I. En effet (αF + βG)′ = αF′ + βG′ = αf + βg.

On primitive donc une somme terme à terme, et un facteur constant sort.

Cas limite : xⁿ pour n = −1, c'est-à-dire 1/x, ne figure pas dans la table : sa primitive n'est pas une puissance, elle viendra plus tard.
:::

::: verifie
Déterminer une primitive de f(x) = 4x³ − 1/√x + sin(2x) sur ]0 ; +∞[.

---

4x³ a pour primitive 4 × x⁴/4 = x⁴. 1/√x a pour primitive 2√x, donc −1/√x a pour primitive −2√x. sin(2x) : ligne sin(ax + b) avec a = 2, soit −(1/2) cos(2x). D'où F(x) = x⁴ − 2√x − (1/2) cos(2x). Contrôle : F′(x) = 4x³ − 1/√x + sin(2x) ✓.
:::

::: retenir
Une primitive usuelle se lit dans la table (facteur 1/a pour cos(ax + b), signe moins pour sin) ; une somme et un facteur constant se primitivent terme à terme, jamais un produit.
:::

## 🧩 Formes pratiques : reconnaître u′uⁿ, u′/√u et v′/v²

Dériver (x² + 1)⁴ donne 4 × 2x × (x² + 1)³ = 8x(x² + 1)³. Lue à l'envers, une primitive de 8x(x² + 1)³ est (x² + 1)⁴.
Comment reconnaître, dans une fonction comme 2x(x² + 1)³, la dérivée d'une composée, sans l'avoir devinée ?

Soient u et v des fonctions dérivables sur I dont les dérivées sont continues. On lit les formules de dérivation de la composée à l'envers :

| f | une primitive | condition |
| --- | --- | --- |
| u′ + v′ | u + v | |
| λu′ (λ constante) | λu | |
| u′uⁿ (n entier, n ≠ −1) | uⁿ⁺¹/(n + 1) | u ≠ 0 sur I si n ≤ −2 |
| u′/√u | 2√u | u > 0 sur I |
| v′/v² | −1/v | v ≠ 0 sur I |
| (u′∘v) × v′ | u∘v | |

Une méthode en quatre temps : repérer u (le contenu d'une parenthèse, d'une racine ou d'un dénominateur), calculer u′, comparer u′ au facteur présent dans f (un facteur constant manquant se compense), puis contrôler en dérivant.

::: exemple Puissances : f(x) = 2x(x² + 1)³ et g(x) = sin x cos²x
1. Pour f, on pose u(x) = x² + 1, donc u′(x) = 2x : f = u′u³. La ligne u′uⁿ avec n = 3 donne u⁴/4 : F(x) = (x² + 1)⁴/4. Contrôle : F′ = 4 × 2x(x² + 1)³/4 = f ✓.
2. Pour g, on pose u(x) = cos x, donc u′(x) = −sin x : g = −u′u². Une primitive de u′u² est u³/3, donc G(x) = −cos³x/3. Contrôle : G′(x) = −3cos²x × (−sin x)/3 = sin x cos²x ✓.

:::

::: exemple Racine et quotient : 3/√(2x − 1) et (6x − 3)/(3x² − 3x + 2)²
1. h(x) = 3/√(2x − 1) sur ]1/2 ; +∞[. On pose u(x) = 2x − 1 > 0, u′(x) = 2 : il manque le facteur 2, constant, donc h = (3/2) × u′/√u. D'où H(x) = (3/2) × 2√u = 3√(2x − 1). Contrôle : H′(x) = 3 × 2/(2√(2x − 1)) = h(x) ✓.
2. k(x) = (6x − 3)/(3x² − 3x + 2)² sur ℝ. On pose v(x) = 3x² − 3x + 2, qui ne s'annule jamais (discriminant 9 − 24 < 0), et v′(x) = 6x − 3 : k = v′/v². La ligne v′/v² donne K(x) = −1/(3x² − 3x + 2).

:::

::: piege Oublier de compenser le facteur constant
Pour f(x) = x(x² + 1)³, on pose u = x² + 1 et l'on écrit directement F(x) = (x² + 1)⁴/4. Cela tente parce que la forme u′uⁿ saute aux yeux. Mais u′ = 2x, et f ne contient que x : F′(x) = 4 × 2x(x² + 1)³/4 = 2x(x² + 1)³, le double de f. Comme f = (1/2)u′u³, la bonne primitive est (1/2) × u⁴/4 = (x² + 1)⁴/8.
:::

::: propriete
Quand on pose u, le facteur manquant doit être une **constante** : f = c × u′uⁿ se primitive en c × uⁿ⁺¹/(n + 1). On vérifie toujours le résultat en le dérivant.

Cas limite : si le facteur manquant dépend de x, la forme est absente. (x² + 1)³ n'est pas de la forme u′u³ : il n'y a pas de facteur 2x, et diviser par 2x ne donne pas une primitive. On développe alors.
:::

::: verifie
Déterminer la primitive F de f(x) = x/√(x² + 5) sur ℝ telle que F(2) = 1.

---

On pose u(x) = x² + 5 > 0, u′(x) = 2x : f = (1/2) × u′/√u, donc F(x) = (1/2) × 2√u + c = √(x² + 5) + c. La condition F(2) = √9 + c = 3 + c = 1 donne c = −2 : F(x) = √(x² + 5) − 2. Contrôle : F′(x) = 2x/(2√(x² + 5)) = f(x) ✓.
:::

::: retenir
On reconnaît u′uⁿ, u′/√u ou v′/v² en posant u, en calculant u′ et en compensant un facteur constant ; un facteur manquant qui dépend de x signifie qu'il faut changer de méthode.
:::

## 🧮 Réécrire avant de primitiver : éléments simples

Soit f(x) = (2x³ + 5x² + 4x + 4)/(x + 1)². Aucune formule ne primitive directement un quotient comme celui-ci. Mais on peut montrer que f(x) = 2x + 1 + 3/(x + 1)², et chaque terme se primitive.
Comment trouver les coefficients de cette écriture, quand l'énoncé donne la forme à identifier ?

::: exemple Identifier a, b, c dans f(x) = ax + b + c/(x + 1)²
1. Quand x tend vers +∞, f(x)/x tend vers a. Ici f(x)/x = (2x³ + 5x² + 4x + 4)/(x(x + 1)²) a pour limite 2 (rapport des termes de plus haut degré, 2x³/x³) : a = 2.
2. On multiplie par (x + 1)² : g(x) = (x + 1)² f(x) = 2x³ + 5x² + 4x + 4 = (ax + b)(x + 1)² + c. En x = −1, le produit s'annule : c = g(−1) = −2 + 5 − 4 + 4 = 3.
3. f(0) = 4 par la formule, et f(0) = b + c par la forme : b = 4 − 3 = 1.
4. Donc f(x) = 2x + 1 + 3/(x + 1)². Contrôle en x = 1 : f(1) = 15/4 par la formule, et 2 + 1 + 3/4 = 15/4 par la forme ✓.
5. Une primitive sur ]−1 ; +∞[ est F(x) = x² + x − 3/(x + 1), car une primitive de 1/(x + 1)² est −1/(x + 1).

:::

::: exemple Identifier a et b dans f(x) = (6x + 5)/(3x + 2)³ = a/(3x + 2)² + b/(3x + 2)³
1. On met au même dénominateur : a/(3x + 2)² + b/(3x + 2)³ = (a(3x + 2) + b)/(3x + 2)³ = (3ax + 2a + b)/(3x + 2)³.
2. On identifie avec 6x + 5 : 3a = 6 donne a = 2, et 2a + b = 5 donne b = 1.
3. Avec u(x) = 3x + 2 et u′ = 3, 2/u² = (2/3) × u′/u² a pour primitive −2/(3u), et 1/u³ = (1/3) × u′/u³ a pour primitive (1/3) × u⁻²/(−2) = −1/(6u²).
4. Une primitive sur ]−2/3 ; +∞[ est F(x) = −2/(3(3x + 2)) − 1/(6(3x + 2)²).

:::

::: piege Primitiver le numérateur et le dénominateur séparément
Pour f(x) = 1/x², on écrit « une primitive de 1 est x, une primitive de x² est x³/3, donc F(x) = x/(x³/3) = 3/x² ». Cela tente parce que la linéarité se lit terme par terme. Mais F′(x) = −6/x³, qui n'est pas 1/x² : la primitive d'un quotient n'est pas le quotient des primitives. La bonne réponse se lit dans la table, F(x) = −1/x.
:::

::: propriete
Pour primitiver un quotient dont la forme est donnée, on identifie les coefficients par l'une des méthodes suivantes : limite de f(x)/x en +∞, valeur de (x − x₀)²f(x) en x₀, valeur particulière de f, ou mise au même dénominateur puis égalité des numérateurs. On primitive ensuite terme à terme, et l'on contrôle en dérivant.

Cas limite : les coefficients sont uniques. Deux écritures différentes ax + b + c/(x + 1)² d'une même fonction auraient les mêmes a, b et c.
:::

::: verifie
Déterminer a et b tels que F(x) = (ax + b)/(x² + x + 2) soit une primitive sur ℝ de f(x) = (−2x² − 2x + 3)/(x² + x + 2)².

---

F′(x) = (a(x² + x + 2) − (ax + b)(2x + 1))/(x² + x + 2)² = (−ax² − 2bx + 2a − b)/(x² + x + 2)². On identifie avec le numérateur de f : −a = −2 donne a = 2, −2b = −2 donne b = 1, et 2a − b = 3 se vérifie bien. Donc F(x) = (2x + 1)/(x² + x + 2).
:::

::: retenir
Un quotient dont la forme est donnée se réécrit en identifiant ses coefficients (limite, valeur en un point, ou numérateurs), puis se primitive terme à terme ; jamais numérateur et dénominateur séparément.
:::

> 🏆 Chapitre franchi, héros : tu lis la pente d'une courbe, tu la dérives par les règles, tu en tires les variations et les inflexions, puis tu remontes de la pente à la fonction par les primitives. Les études complètes de fonctions t'attendent au chapitre suivant.
