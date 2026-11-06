# ⚔️ Fonctions exponentielles — la fonction qui change les sommes en produits

> 💡 «Le logarithme change les produits en sommes ; son inverse fait le chemin retour, et c'est lui qui décrit tout ce qui croît ou décroît en proportion de lui-même.»

Bienvenue, héros de la section Sciences de l'informatique. Euler (1707-1783) a donné au nombre e son nom, en rapport avec la fonction exponentielle qu'il décrit. Huit étapes te mènent de sa définition à l'étude d'une fonction du bac : définition et règles de calcul, équations et inéquations, dérivée et primitives, limites et courbe, approximation par un programme, puissances rationnelles, exponentielle de base a, étude de fonctions. On suppose acquis le logarithme népérien (chapitre 6), les limites (chapitre 2), les dérivées et les primitives (chapitre 4) et l'étude de fonctions (chapitre 5).

## 🏰 La fonction exponentielle et ses règles de calcul


Au chapitre 6, tu as résolu ln x = 4 en écrivant x = e⁴, avec un exposant entier. Pourtant ln est une bijection de ]0 ; +∞[ sur ℝ : pour tout réel y, même −0,4 ou 1/2, un seul x > 0 vérifie ln x = y.
Comment nommer cet antécédent quand y n'est pas entier, et dans quel ensemble vit-il ?

::: definition
La **fonction exponentielle**, notée **exp**, est la bijection réciproque de ln : exp est définie sur ℝ et prend ses valeurs dans ]0 ; +∞[. On note exp(x) = eˣ.

$$ y = eˣ ⟺ x = ln y   (x ∈ ℝ, y > 0) $$

$$ ln(eˣ) = x pour tout réel x ;  e^(ln x) = x pour tout x > 0 $$
:::

| Ce que l'on lit | D'où cela vient |
| --- | --- |
| eˣ > 0 pour tout réel x | exp prend ses valeurs dans ]0 ; +∞[, l'ensemble de départ de ln |
| e⁰ = 1 et e¹ = e | ln 1 = 0 et ln e = 1 |
| exp est strictement croissante | la réciproque d'une fonction strictement croissante l'est aussi |

La première ligne sera la plus utile : une exponentielle n'est jamais nulle ni négative.


La première ligne sera la plus utile : une exponentielle n'est jamais nulle ni négative.

::: exemple Lire exp avec ln
1. e^(ln 5) = 5 : ln 5 est un réel et e^(ln x) = x pour tout x > 0.
2. ln(e^(−0,4)) = −0,4 : ln(eˣ) = x pour tout réel x, négatif ou non.
3. e^(1/2) = √e : ln √e = ½ ln e = ½, donc √e est l'antécédent de ½ par ln, c'est-à-dire e^(1/2).

:::

::: piege Confondre la réciproque exp avec l'inverse 1/ln
Pour eᵃ = 5, on écrit « a = 1/ln 5 ≈ 0,62 ». Cela tente parce que « réciproque » évoque l'inverse 1/x. Mais la réciproque défait ln : eᵃ = 5 ⟺ a = ln 5 ≈ 1,61, et e^0,62 ≈ 1,86 ≠ 5. L'inverse de ln 5 est un nombre ; la réciproque de ln est une fonction, exp.
:::

Reste à savoir calculer avec eˣ.

Pour les puissances entières, 2³ × 2⁴ = 2⁷ : les exposants s'additionnent. Que devient le produit eᵃ × eᵇ, puisque ln change un produit en somme ?

::: exemple Preuve : eᵃ × eᵇ = e^(a+b)
1. On pose X = eᵃ et Y = eᵇ : par définition, ln X = a et ln Y = b.
2. ln(XY) = ln X + ln Y = a + b, d'après la propriété fondamentale de ln (chapitre 6).
3. XY > 0 a pour logarithme a + b, donc XY = e^(a+b), puisque ln x = y ⟺ x = eʸ.
4. eᵇ × e^(−b) = e⁰ = 1, donc e^(−b) = 1/eᵇ ; puis e^(a−b) = eᵃ × e^(−b) = eᵃ/eᵇ.

:::

::: propriete
Pour tous réels a et b :

| Écriture | devient | Exemple |
| --- | --- | --- |
| eᵃ × eᵇ | e^(a+b) | e² × e⁵ = e⁷ |
| e^(−b) | 1/eᵇ | e^(−3) = 1/e³ |
| eᵃ/eᵇ | e^(a−b) | e⁵/e² = e³ |
| (eᵃ)ⁿ, n entier relatif | e^(na) | (e²)³ = e⁶ |
| ⁿ√(eᵃ), n entier ≥ 1 | e^(a/n) | √(e⁴) = e² |

Pour la dernière ligne, (e^(a/n))ⁿ = e^a, donc e^(a/n) est bien la racine n-ième de eᵃ.

Cas limite : l'exposant n de (eᵃ)ⁿ est un entier, et eᵃ + eᵇ ne se simplifie pas en une seule exponentielle.
:::

::: exemple Simplifier pour tout réel x
1. e^(3x) × e^(1−x) = e^(3x+1−x) = e^(2x+1), car les exposants s'additionnent.
2. (eˣ)² = e^(2x), car (eᵃ)ⁿ = e^(na).
3. Le quotient e^(2x+1)/e^(2x) = e^(2x+1−2x) = e, car les exposants se soustraient : l'expression e^(3x) × e^(1−x)/(eˣ)² vaut e pour tout x.
4. e^(x+2) − eˣ = eˣ × e² − eˣ = eˣ(e² − 1), en factorisant eˣ : une différence d'exponentielles se factorise, elle ne s'écrit pas en une seule.

:::

::: piege Croire que eᵃ + eᵇ = e^(a+b)
Pour a = b = 1, on écrit « e + e = e^(1+1) = e² ». Cela tente parce que le produit eᵃ × eᵇ devient e^(a+b). Mais e + e = 2e ≈ 5,44, alors que e² ≈ 7,39. Seul le produit se transforme en somme d'exposants : une somme d'exponentielles se factorise.
:::

::: verifie
Simplifier B = e^(4x) × e^(−x)/e^(2x+3), pour tout réel x.

---

e^(4x) × e^(−x) = e^(3x), car on additionne les exposants. Puis e^(3x)/e^(2x+3) = e^(3x−(2x+3)) = e^(x−3), car on soustrait les exposants en mettant le dénominateur entre parenthèses.
:::

::: retenir
exp est la réciproque de ln : y = eˣ ⟺ x = ln y, ln(eˣ) = x, e^(ln x) = x pour x > 0 ; eˣ > 0, e⁰ = 1, e¹ = e. Et eᵃ × eᵇ = e^(a+b), e^(−b) = 1/eᵇ, eᵃ/eᵇ = e^(a−b), (eᵃ)ⁿ = e^(na) pour n entier ; en revanche eᵃ + eᵇ ≠ e^(a+b).
:::

## 🛡️ Équations et inéquations exponentielles

Supposons que le niveau de charge d'un téléphone soit modélisé par C(t) = 100 e^(−0,1t) (en %), où t est le temps en heures. Au bout de combien de temps la charge tombe-t-elle à 40 % ?
L'inconnue est dans un exposant : aucune règle de calcul ne l'en sort, mais ln le fait.

::: exemple Charge à 40 %
1. 100 e^(−0,1t) = 40 ⟺ e^(−0,1t) = 0,4, en divisant par 100.
2. 0,4 > 0 : l'équation eᵘ = 0,4 a une seule solution, u = ln 0,4, car exp est une bijection de ℝ sur ]0 ; +∞[. Donc −0,1t = ln 0,4.
3. t = −10 ln 0,4 = 10 ln 2,5 ≈ 10 × 0,9163 = 9,16 heures. Contrôle : e^(−0,916) ≈ 0,40 ✓.

:::

::: propriete
Pour tous réels a, b et k :

- eᵃ = eᵇ ⟺ a = b, et eᵃ ≤ eᵇ ⟺ a ≤ b : exp est strictement croissante, donc injective et elle conserve l'ordre ;
- si k > 0 : eˣ = k ⟺ x = ln k, et eˣ > k ⟺ x > ln k ;
- si k ≤ 0 : eˣ = k n'a aucune solution, et eˣ > k est vraie pour tout réel x.

Cas limite : k = 1 donne eˣ = 1 ⟺ x = ln 1 = 0, et k = 0 : eˣ = 0 n'a pas de solution.
:::

::: exemple Quatre résolutions
1. e^(2x−1) = e^(x+4) ⟺ 2x − 1 = x + 4 ⟺ x = 5, car eᵃ = eᵇ ⟺ a = b : **S = {5}**.
2. eˣ = −2 : une exponentielle est strictement positive, donc **S = ∅**.
3. e^(3x) ≥ 5 ⟺ 3x ≥ ln 5, car exp conserve l'ordre, soit x ≥ (ln 5)/3 ≈ 0,54 : **S = [(ln 5)/3 ; +∞[**.
4. e^(2x) + eˣ − 6 = 0. On pose X = eˣ, avec X > 0 : X² + X − 6 = (X + 3)(X − 2) = 0, donc X = −3 ou X = 2. La valeur −3 est rejetée (X > 0), et eˣ = 2 donne **x = ln 2**.

:::

::: piege Prendre ln de chaque terme d'une somme
Pour eˣ + 3 = 8, on écrit « x + ln 3 = ln 8 », donc x = ln 8 − ln 3 = ln(8/3) ≈ 0,98. Cela tente parce que ln transforme un produit en somme. Mais ln(eˣ + 3) ≠ ln(eˣ) + ln 3 : on isole d'abord l'exponentielle, eˣ = 5, et x = ln 5 ≈ 1,61.
:::

::: methode
Pour résoudre une équation ou une inéquation avec exp :

1. isoler l'exponentielle : eᵘ = k, ou eᵘ = eᵛ ;
2. si k > 0, appliquer ln (ou l'équivalence eᵃ = eᵇ ⟺ a = b) ; si k ≤ 0, conclure sans calcul ;
3. pour un trinôme en eˣ, poser X = eˣ avec X > 0, résoudre en X, rejeter les valeurs X ≤ 0, puis revenir à x = ln X ;
4. pour une inéquation, exp conserve l'ordre ; mais diviser par un nombre négatif renverse l'inégalité.

Cas limite : e^(−2x) < 3 ⟺ −2x < ln 3 ⟺ x > −(ln 3)/2 : la division par −2 renverse le sens.
:::

::: verifie
Résoudre dans ℝ : e^(2x) − 4eˣ − 5 = 0.

---

On pose X = eˣ > 0 : X² − 4X − 5 = (X − 5)(X + 1) = 0, donc X = 5 ou X = −1. La valeur −1 est rejetée car une exponentielle est positive, et eˣ = 5 donne x = ln 5. On a posé X, résolu, rejeté puis revenu à x.
:::

::: retenir
eᵃ = eᵇ ⟺ a = b, eˣ = k ⟺ x = ln k pour k > 0 et aucune solution pour k ≤ 0 ; pour un trinôme en eˣ, on pose X = eˣ et l'on rejette X ≤ 0.
:::

## 🔮 Dériver et primitiver avec exp

Une cuve se remplit à une vitesse égale, à chaque instant, à la quantité déjà présente : plus il y en a, plus elle monte vite. Existe-t-il une fonction égale à sa propre dérivée ?
Le chapitre 4 donne l'outil : si f est dérivable et f′ ne s'annule pas, sa réciproque g est dérivable et g′(y) = 1/f′(g(y)).

::: exemple La dérivée de exp et de e^u
1. exp est la réciproque de ln, dont la dérivée 1/y ne s'annule jamais sur ]0 ; +∞[ : exp est dérivable sur ℝ.
2. Pour y = eˣ : (exp)′(x) = 1/((ln)′(y)) = 1/(1/y) = y = eˣ. Donc exp′ = exp.
3. Si u est dérivable, e^u est une composée : (e^u)′ = u′ × e^u, comme pour toute composée (chapitre 4).
4. Pour f(x) = e^(x²−3x), u(x) = x² − 3x et u′(x) = 2x − 3 : f′(x) = (2x − 3)e^(x²−3x).

:::

::: propriete
- exp′ = exp sur ℝ ; comme exp est strictement positive, elle est strictement croissante.
- Si u est dérivable sur I, (e^u)′ = u′e^u sur I.
- Une primitive de u′e^u est e^u. En particulier, pour a ≠ 0, une primitive de x ↦ e^(ax+b) est x ↦ (1/a)e^(ax+b).

Cas limite : u(x) = x donne u′ = 1 et retrouve exp′ = exp ; u(x) = −x donne (e^(−x))′ = −e^(−x).
:::

::: exemple Primitives par reconnaissance
1. f(x) = 3e^(3x−1) : avec u = 3x − 1, u′ = 3 et f = u′e^u, donc F(x) = e^(3x−1).
2. g(x) = x e^(x²) : avec u = x², u′ = 2x et g = ½ u′e^u, donc G(x) = ½ e^(x²).
3. h(x) = e^(−2x) : avec u = −2x, u′ = −2 et h = −½ u′e^u, donc H(x) = −½ e^(−2x).
4. Contrôle de G : (½ e^(x²))′ = ½ × 2x × e^(x²) = x e^(x²) ✓.

:::

::: piege Oublier le facteur u′
On écrit « (e^(5x))′ = e^(5x) », parce que exp′ = exp. Cela tente parce que l'exponentielle semble « se dériver toute seule ». Mais e^(5x) est e^u avec u = 5x : (e^(5x))′ = u′e^u = 5e^(5x). Seule x ↦ eˣ, où u′ = 1, est sa propre dérivée.
:::

::: methode
Pour une primitive de x ↦ (ax + b)e^(cx) (c ≠ 0), on la cherche de la même forme, F(x) = (αx + β)e^(cx). Alors F′(x) = (αc x + α + βc)e^(cx), et l'on identifie les coefficients.

Exemple : f(x) = (4x − 2)e^(2x), c = 2. Il faut 2α = 4 et α + 2β = −2, donc α = 2 et β = −2 : F(x) = (2x − 2)e^(2x). Contrôle : F′(x) = 2e^(2x) + 2(2x − 2)e^(2x) = (4x − 2)e^(2x) ✓.

Cas limite : si c = 0, f(x) = ax + b est un polynôme, sans exponentielle.
:::

::: verifie
Trouver par identification une primitive de g(x) = (6x + 1)e^(3x).

---

On cherche G(x) = (αx + β)e^(3x), donc G′(x) = (3αx + α + 3β)e^(3x). Il faut 3α = 6, soit α = 2, et α + 3β = 1, soit β = −1/3 : G(x) = (2x − 1/3)e^(3x). On a identifié le coefficient de x, puis le terme constant.
:::

::: retenir
exp′ = exp, (e^u)′ = u′e^u et x ↦ e^u est une primitive de u′e^u ; une primitive de (ax + b)e^(cx) se cherche sous la forme (αx + β)e^(cx).
:::

## 📈 Limites, variations et courbe de exp

Comparons eˣ et x² : le quotient eˣ/x² vaut environ 220 en x = 10, puis 1,2 × 10⁶ en x = 20 et 1,2 × 10¹⁰ en x = 30. L'exponentielle écrase la puissance, au moins sur ces valeurs.
Que devient eˣ aux deux extrémités de ℝ, et l'écrasement se produit-il toujours ?

::: exemple Établir les limites
1. En +∞ : pour M > 0, eˣ > M ⟺ x > ln M, car exp est croissante ; dès que x dépasse ln M, eˣ dépasse M, donc eˣ → +∞.
2. En −∞ : eˣ = 1/e^(−x) et e^(−x) → +∞, donc eˣ → 0.
3. eˣ/x en +∞ : on pose y = eˣ, donc x = ln y et y → +∞ ; eˣ/x = y/ln y → +∞, car (ln y)/y → 0 (chapitre 6).
4. (eˣ − 1)/x en 0 est le taux d'accroissement de exp en 0, qui tend vers exp′(0) = e⁰ = 1.
5. x eˣ en −∞ : avec X = −x → +∞, x eˣ = −X/e^X = −1/(e^X/X) → 0.
6. (e^(2x) − 1)/x = 2 × (e^(2x) − 1)/(2x) : avec h = 2x → 0, (e^h − 1)/h → 1, donc la limite est 2.

:::

::: propriete
- lim x→+∞ eˣ = +∞ et lim x→−∞ eˣ = 0 : l'axe des abscisses est asymptote à gauche.
- lim x→+∞ eˣ/x = +∞ et lim x→−∞ x eˣ = 0 ; plus généralement, pour tout entier n ≥ 1, lim x→+∞ eˣ/xⁿ = +∞ et lim x→−∞ xⁿ eˣ = 0.
- lim x→0 (eˣ − 1)/x = 1.

| x | −∞ | | +∞ |
| --- | --- | --- | --- |
| eˣ | 0 | ↗ | +∞ |

Cas limite : eˣ ne s'annule jamais, 0 est une limite et non une valeur atteinte.
:::

::: figure Les courbes de exp et de ln sont symétriques par rapport à la droite y = x ; celle de exp passe par (0 ; 1) et longe l'axe des abscisses à gauche
<svg viewBox="0 0 340 262"><title>Les courbes de exp et de ln sont symétriques par rapport à la droite y = x ; celle de exp passe par (0 ; 1) et longe l'axe des abscisses à gauche</title><line x1="40" y1="165" x2="335.6" y2="165" stroke="#0f172a" stroke-width="1.6"/><line x1="130" y1="247.8" x2="130" y2="9.8" stroke="#0f172a" stroke-width="1.6"/><polygon points="335.6,165 328.6,161.5 328.6,168.5" fill="#0f172a"/><polygon points="130,9.8 126.5,16.8 133.5,16.8" fill="#0f172a"/><text x="329.6" y="158" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="138" y="21.8" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="58" y1="162" x2="58" y2="168" stroke="#0f172a" stroke-width="1.3"/><text x="58" y="180" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="94" y1="162" x2="94" y2="168" stroke="#0f172a" stroke-width="1.3"/><text x="94" y="180" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="166" y1="162" x2="166" y2="168" stroke="#0f172a" stroke-width="1.3"/><text x="166" y="180" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="202" y1="162" x2="202" y2="168" stroke="#0f172a" stroke-width="1.3"/><text x="202" y="180" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="238" y1="162" x2="238" y2="168" stroke="#0f172a" stroke-width="1.3"/><text x="238" y="180" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="274" y1="162" x2="274" y2="168" stroke="#0f172a" stroke-width="1.3"/><text x="274" y="180" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="310" y1="162" x2="310" y2="168" stroke="#0f172a" stroke-width="1.3"/><text x="310" y="180" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="127" y1="237" x2="133" y2="237" stroke="#0f172a" stroke-width="1.3"/><text x="124" y="241" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="127" y1="201" x2="133" y2="201" stroke="#0f172a" stroke-width="1.3"/><text x="124" y="205" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="127" y1="129" x2="133" y2="129" stroke="#0f172a" stroke-width="1.3"/><text x="124" y="133" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="127" y1="93" x2="133" y2="93" stroke="#0f172a" stroke-width="1.3"/><text x="124" y="97" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="127" y1="57" x2="133" y2="57" stroke="#0f172a" stroke-width="1.3"/><text x="124" y="61" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="127" y1="21" x2="133" y2="21" stroke="#0f172a" stroke-width="1.3"/><text x="124" y="25" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="47.2" y1="247.8" x2="281.2" y2="13.8" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 3"/><polyline points="40,162.04 41.18,161.95 42.36,161.84 43.54,161.74 44.72,161.63 45.9,161.52 47.08,161.4 48.26,161.28 49.44,161.16 50.62,161.03 51.81,160.9 52.99,160.76 54.17,160.62 55.35,160.47 56.53,160.32 57.71,160.17 58.89,160.01 60.07,159.84 61.25,159.67 62.43,159.49 63.61,159.31 64.79,159.12 65.97,158.92 67.15,158.72 68.33,158.51 69.51,158.29 70.69,158.07 71.87,157.84 73.05,157.6 74.24,157.35 75.42,157.1 76.6,156.83 77.78,156.56 78.96,156.28 80.14,155.99 81.32,155.69 82.5,155.38 83.68,155.06 84.86,154.73 86.04,154.38 87.22,154.03 88.4,153.66 89.58,153.29 90.76,152.9 91.94,152.49 93.12,152.07 94.3,151.64 95.48,151.2 96.67,150.74 97.85,150.26 99.03,149.77 100.21,149.26 101.39,148.74 102.57,148.2 103.75,147.64 104.93,147.06 106.11,146.46 107.29,145.84 108.47,145.2 109.65,144.54 110.83,143.86 112.01,143.16 113.19,142.43 114.37,141.68 115.55,140.9 116.73,140.1 117.91,139.27 119.1,138.41 120.28,137.52 121.46,136.61 122.64,135.66 123.82,134.68 125,133.67 126.18,132.63 127.36,131.55 128.54,130.43 129.72,129.28 130.9,128.09 132.08,126.86 133.26,125.59 134.44,124.27 135.62,122.91 136.8,121.51 137.98,120.06 139.16,118.56 140.34,117.02 141.53,115.42 142.71,113.76 143.89,112.06 145.07,110.29 146.25,108.47 147.43,106.58 148.61,104.63 149.79,102.62 150.97,100.54 152.15,98.39 153.33,96.17 154.51,93.88 155.69,91.51 156.87,89.06 158.05,86.53 159.23,83.91 160.41,81.21 161.59,78.41 162.77,75.53 163.96,72.55 165.14,69.46 166.32,66.28 167.5,62.99 168.68,59.59 169.86,56.07 171.04,52.44 172.22,48.69 173.4,44.81 174.58,40.81 175.76,36.67 176.94,32.39 178.12,27.97 179.3,23.4 180.48,18.68 181.66,13.8" fill="none" stroke="#0f6e56" stroke-width="2.8"/><polyline points="133.61,247.8 135.26,234.25 136.91,224.42 138.56,216.71 140.21,210.37 141.86,204.98 143.51,200.29 145.16,196.14 146.81,192.42 148.46,189.05 150.11,185.97 151.76,183.13 153.41,180.5 155.06,178.04 156.71,175.75 158.36,173.59 160.01,171.55 161.66,169.63 163.31,167.8 164.96,166.06 166.61,164.4 168.26,162.81 169.91,161.29 171.56,159.83 173.21,158.43 174.86,157.08 176.51,155.78 178.16,154.53 179.81,153.31 181.46,152.14 183.11,151 184.76,149.9 186.41,148.83 188.06,147.8 189.71,146.79 191.36,145.81 193.01,144.85 194.66,143.92 196.31,143.01 197.96,142.13 199.61,141.26 201.26,140.42 202.91,139.6 204.56,138.79 206.21,138 207.86,137.23 209.51,136.48 211.16,135.74 212.81,135.01 214.46,134.3 216.11,133.61 217.76,132.92 219.41,132.25 221.06,131.59 222.71,130.95 224.36,130.31 226,129.69 227.65,129.07 229.3,128.47 230.95,127.88 232.6,127.29 234.25,126.72 235.9,126.16 237.55,125.6 239.2,125.05 240.85,124.51 242.5,123.98 244.15,123.45 245.8,122.94 247.45,122.43 249.1,121.93 250.75,121.43 252.4,120.94 254.05,120.46 255.7,119.99 257.35,119.52 259,119.05 260.65,118.59 262.3,118.14 263.95,117.7 265.6,117.26 267.25,116.82 268.9,116.39 270.55,115.97 272.2,115.55 273.85,115.13 275.5,114.72 277.15,114.31 278.8,113.91 280.45,113.52 282.1,113.12 283.75,112.73 285.4,112.35 287.05,111.97 288.7,111.59 290.35,111.22 292,110.85 293.65,110.49 295.3,110.13 296.95,109.77 298.6,109.42 300.25,109.06 301.9,108.72 303.55,108.37 305.2,108.03 306.85,107.7 308.5,107.36 310.15,107.03 311.8,106.7 313.45,106.38 315.1,106.05 316.75,105.73 318.4,105.42 320.05,105.1 321.7,104.79 323.35,104.48 325,104.18 326.65,103.88 328.3,103.57 329.95,103.28 331.6,102.98" fill="none" stroke="#b45309" stroke-width="2.8"/><circle cx="130" cy="129" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="166" cy="165" r="4" fill="#b45309" stroke="#0f172a" stroke-width="1"/><text x="138" y="123" text-anchor="start" fill="#0f6e56" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(0 ; 1)</text><text x="172" y="191" text-anchor="start" fill="#b45309" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(1 ; 0)</text><text x="186" y="44" text-anchor="start" fill="#0f6e56" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = eˣ</text><text x="284.8" y="87.6" text-anchor="start" fill="#b45309" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = ln x</text><text x="246.6" y="28.6" text-anchor="start" fill="#64748b" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = x</text></svg>
:::

Le point (0 ; 1) du dessin traduit e⁰ = 1 ; l'axe des abscisses qui borde la courbe de exp à gauche traduit lim x→−∞ eˣ = 0 ; la symétrie d'axe y = x traduit que exp et ln sont réciproques.

::: piege Croire que x¹⁰⁰ l'emporte sur eˣ parce que 100¹⁰⁰ ≫ e¹⁰⁰
Pour x = 100, 100¹⁰⁰ = 10²⁰⁰ alors que e¹⁰⁰ ≈ 2,7 × 10⁴³ : on conclut « lim eˣ/x¹⁰⁰ = 0 ». Cela tente parce que la puissance est bien plus grande en ce point. Mais une limite se juge à l'infini, pas en une valeur : pour x = 1 000, e¹⁰⁰⁰ ≈ 10⁴³⁴ dépasse 1 000¹⁰⁰ = 10³⁰⁰. Pour tout n, lim eˣ/xⁿ = +∞.
:::

::: exemple Lever une forme indéterminée en factorisant
1. lim x→+∞ (eˣ − 3x) est du type +∞ − ∞. On écrit eˣ − 3x = x(eˣ/x − 3) : eˣ/x → +∞, donc le facteur tend vers +∞ et la limite est +∞.
2. lim x→−∞ x² e^(2x) : avec X = 2x → −∞, x² e^(2x) = (X²/4)e^X = ¼ × X²e^X, qui tend vers ¼ × 0 = 0.

:::

::: verifie
Calculer lim x→+∞ (eˣ − x²).

---

La forme est +∞ − ∞. On factorise : eˣ − x² = eˣ(1 − x²/eˣ). Comme x²/eˣ → 0 (comparaison de eˣ et de x²), le facteur entre parenthèses tend vers 1, et eˣ → +∞ : la limite est +∞. On factorise le terme dominant.
:::

::: retenir
eˣ → +∞ en +∞ et → 0 en −∞ ; eˣ/xⁿ → +∞ en +∞ et xⁿeˣ → 0 en −∞ ; (eˣ − 1)/x → 1 en 0 ; la courbe de exp est la symétrique de celle de ln par rapport à y = x.
:::

## 🖥️ Approcher eˣ par un programme

Une calculatrice affiche e² ≈ 7,389, alors qu'elle ne sait faire que des additions et des multiplications.
Comment obtenir eˣ avec ces seules opérations, à une précision ε choisie ?

On admet que eˣ est approché par la somme 1 + x/1! + x²/2! + x³/3! + … + xⁿ/n!, d'autant mieux que n est grand. Un programme ajoute ces termes un à un :

```
S ← 1 ; p ← 1 ; f ← 1 ; i ← 1
répéter
    p ← p × x ; f ← f × i
    S ← S + p/f ; i ← i + 1
jusqu'à |p/f| ≤ ε
afficher S
```

::: exemple Suivre le programme pour x = 2 et ε = 0,5
1. Tour 1 : p = 2, f = 1, S = 3, terme 2 > 0,5. Tour 2 : p = 4, f = 2, S = 5, terme 2 > 0,5.
2. Tour 3 : p = 8, f = 6, S ≈ 6,333, terme ≈ 1,333. Tour 4 : p = 16, f = 24, S ≈ 7,000, terme ≈ 0,667.
3. Tour 5 : p = 32, f = 120, S ≈ 7,267, terme ≈ 0,267 ≤ 0,5 : le programme s'arrête et affiche 7,267, proche de e² ≈ 7,389.

:::

::: methode
1. À chaque tour, p est multiplié par x et f par i : au tour i, p = xⁱ et f = i!, donc p/f est le terme xⁱ/i!.
2. S reçoit ce terme : après le tour i, S = 1 + x/1! + … + xⁱ/i!.
3. Le programme s'arrête au premier terme dont la **valeur absolue** est au plus ε ; pour x < 0 les termes changent de signe, d'où |p/f|.

Cas limite : x = 0 donne p/f = 0 dès le premier tour, et le programme affiche S = 1 = e⁰.
:::

::: verifie
Quelle valeur le programme affiche-t-il pour x = −1 et ε = 0,1 ?

---

Les termes p/f valent −1, 1/2, −1/6 puis 1/24, et S passe par 0 ; 0,5 ; 0,333 ; 0,375. Au tour 4, |1/24| ≈ 0,042 ≤ 0,1 : le programme affiche 0,375, proche de e⁻¹ ≈ 0,368. Sans la valeur absolue, le premier terme −1 aurait tout arrêté.
:::

::: retenir
Au tour i, p = xⁱ et f = i! : le programme ajoute xⁱ/i! à S et s'arrête au premier terme de valeur absolue au plus ε ; S approche eˣ.
:::

## 🔬 Puissances rationnelles et croissances comparées

Au chapitre 6, ln(xⁿ) = n ln x, donc xⁿ = e^(n ln x) pour x > 0 et n entier. Cette écriture garde un sens quand n est remplacé par une fraction.
Que vaut alors 8^(2/3), et les règles des puissances entières restent-elles vraies ?

::: definition
Pour x > 0 et r rationnel, **xʳ** (« x puissance r ») est défini par :

$$ xʳ = e^(r ln x) $$

On a donc ln xʳ = r ln x, et xʳ > 0. Pour n entier ≥ 1, x^(1/n) = ⁿ√x ; et x^(p/q) est la racine q-ième de xᵖ.
:::

::: exemple Calculer sans calculatrice
1. 8^(2/3) = e^((2/3) ln 8) = e^((2/3) × 3 ln 2) = e^(2 ln 2) = e^(ln 4) = 4, car ln 8 = 3 ln 2.
2. 27^(−2/3) = (27^(1/3))^(−2) = 3^(−2) = 1/9, car 27^(1/3) = ³√27 = 3 et (aʳ)^(r′) = a^(rr′).
3. 2^(1/2) × 2^(3/2) = 2^(1/2+3/2) = 2² = 4, car les exposants s'additionnent.
4. Pour a > 0 : a^(5/6)/a^(1/3) = a^(5/6−2/6) = a^(1/2) = √a, car les exposants se soustraient.

:::

::: piege Lire un exposant fractionnaire comme « puissance puis division »
On écrit « 8^(2/3) = 8²/3 = 64/3 ». Cela tente parce que 2/3 se lit « 2 divisé par 3 ». Mais 8^(2/3) = e^((2/3) ln 8) = (8^(1/3))² = 2² = 4 : le dénominateur 3 désigne une racine cubique, le numérateur 2 une puissance. De même 9^(1/2) est la racine carrée de 9, soit 3, et non 9/2.
:::

::: propriete
Pour a > 0, b > 0 et r, r′ rationnels :

| Règle | Exemple |
| --- | --- |
| aʳ × a^(r′) = a^(r+r′) | 4^(1/2) × 4^(3/2) = 4² = 16 |
| aʳ/a^(r′) = a^(r−r′) | 16^(3/4)/16^(1/4) = 16^(1/2) = 4 |
| (aʳ)^(r′) = a^(rr′) | (8^(2/3))^(3/2) = 8 |
| (ab)ʳ = aʳ × bʳ | (4 × 9)^(1/2) = 2 × 3 = 6 |
| (a/b)ʳ = aʳ/bʳ | (1/8)^(1/3) = 1/2 |

Cas limite : tout est soumis à a > 0 et b > 0 ; pour x ≤ 0, xʳ n'est pas défini par e^(r ln x). Et r = 0 donne x⁰ = e⁰ = 1.
:::

::: exemple Appliquer les comparaisons
1. (ln x)/xʳ en +∞ : ln x = (1/r) ln xʳ, donc (ln x)/xʳ = (1/r) × (ln X)/X avec X = xʳ → +∞, et (ln X)/X → 0.
2. lim x→0⁺ x^(1/3) ln x = 0 : avec X = 1/x → +∞, x^(1/3) ln x = −(ln X)/X^(1/3), qui tend vers 0 d'après l'étape 1 avec r = 1/3.
3. lim x→+∞ eˣ/x^(5/2) = +∞ (comparaison énoncée ci-dessous), et son inverse : lim x→+∞ x^(5/2) e^(−x) = 0.

:::

::: propriete
Pour r rationnel > 0 : lim x→+∞ (ln x)/xʳ = 0, lim x→0⁺ xʳ ln x = 0 et lim x→+∞ eˣ/xʳ = +∞.
:::

::: verifie
Calculer 32^(2/5), puis lim x→0⁺ x^(1/4) ln x.

---

32^(1/5) = 2 car 2⁵ = 32, donc 32^(2/5) = (32^(1/5))² = 2² = 4. Pour la limite, la comparaison xʳ ln x → 0 en 0⁺ s'applique avec r = 1/4 > 0 : la limite est 0. On a calculé la racine d'abord, puis élevé à la puissance du numérateur.
:::

::: retenir
xʳ = e^(r ln x) pour x > 0 et r rationnel, avec les mêmes règles que les puissances entières ; x^(1/n) = ⁿ√x ; et ln x/xʳ → 0, xʳ ln x → 0 en 0⁺, eˣ/xʳ → +∞.
:::

## 📐 L'exponentielle de base a et les modèles

Sur un étang, une population de nénuphars double chaque jour : elle compte 2ⁿ nénuphars au bout de n jours. Mais combien au bout de 3 jours et demi ?
L'exposant entier ne suffit plus : on voudrait aˣ pour tout réel x, pour décrire toute grandeur qui se multiplie par un même facteur à intervalles réguliers.

::: definition
Pour a > 0 et x réel, on pose **aˣ** = e^(x ln a). La fonction x ↦ aˣ est l'**exponentielle de base a** (a ≠ 1 ; pour a = 1 elle est constante, égale à 1).

$$ aˣ = e^(x ln a) $$
:::

Le signe de la dérivée est celui de ln a : pour a > 1, aˣ est strictement croissante ; pour 0 < a < 1, strictement décroissante. Toutes les courbes passent par (0 ; 1). Comme (1/2)ˣ = 2^(−x), les courbes de 2ˣ et de (1/2)ˣ sont symétriques par rapport à l'axe des ordonnées.

::: figure Les courbes de 2ˣ et de (1/2)ˣ passent toutes deux par (0 ; 1) et sont symétriques par rapport à l'axe des ordonnées
<svg viewBox="0 0 340 250"><title>Les courbes de 2ˣ et de (1/2)ˣ passent par (0 ; 1) et sont symétriques par rapport à l'axe des ordonnées</title><line x1="34" y1="208" x2="316.8" y2="208" stroke="#0f172a" stroke-width="1.6"/><line x1="170" y1="231.8" x2="170" y2="5.1" stroke="#0f172a" stroke-width="1.6"/><polygon points="316.8,208 309.8,204.5 309.8,211.5" fill="#0f172a"/><polygon points="170,5.1 166.5,12.1 173.5,12.1" fill="#0f172a"/><text x="310.8" y="201" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="178" y="17.1" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="68" y1="205" x2="68" y2="211" stroke="#0f172a" stroke-width="1.3"/><text x="68" y="223" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−3</text><line x1="102" y1="205" x2="102" y2="211" stroke="#0f172a" stroke-width="1.3"/><text x="102" y="223" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="136" y1="205" x2="136" y2="211" stroke="#0f172a" stroke-width="1.3"/><text x="136" y="223" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="204" y1="205" x2="204" y2="211" stroke="#0f172a" stroke-width="1.3"/><text x="204" y="223" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="238" y1="205" x2="238" y2="211" stroke="#0f172a" stroke-width="1.3"/><text x="238" y="223" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="272" y1="205" x2="272" y2="211" stroke="#0f172a" stroke-width="1.3"/><text x="272" y="223" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="167" y1="174" x2="173" y2="174" stroke="#0f172a" stroke-width="1.3"/><text x="164" y="178" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="167" y1="140" x2="173" y2="140" stroke="#0f172a" stroke-width="1.3"/><text x="164" y="144" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="167" y1="106" x2="173" y2="106" stroke="#0f172a" stroke-width="1.3"/><text x="164" y="110" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="167" y1="72" x2="173" y2="72" stroke="#0f172a" stroke-width="1.3"/><text x="164" y="76" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="167" y1="38" x2="173" y2="38" stroke="#0f172a" stroke-width="1.3"/><text x="164" y="42" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><polyline points="34,205.88 35.87,205.79 37.74,205.71 39.61,205.62 41.48,205.52 43.35,205.43 45.22,205.33 47.09,205.23 48.96,205.12 50.83,205.01 52.7,204.89 54.57,204.77 56.44,204.64 58.31,204.51 60.18,204.38 62.05,204.24 63.92,204.09 65.79,203.94 67.66,203.78 69.53,203.62 71.4,203.44 73.27,203.27 75.14,203.08 77.01,202.89 78.88,202.69 80.75,202.49 82.62,202.27 84.49,202.05 86.36,201.82 88.23,201.58 90.1,201.33 91.97,201.07 93.84,200.8 95.71,200.52 97.58,200.23 99.45,199.93 101.32,199.62 103.19,199.29 105.06,198.95 106.93,198.6 108.8,198.24 110.67,197.86 112.54,197.46 114.41,197.05 116.28,196.63 118.15,196.19 120.02,195.73 121.89,195.25 123.76,194.75 125.63,194.24 127.5,193.7 129.37,193.15 131.24,192.57 133.11,191.97 134.98,191.35 136.85,190.7 138.72,190.03 140.59,189.33 142.46,188.61 144.33,187.85 146.2,187.07 148.07,186.26 149.94,185.41 151.81,184.53 153.68,183.62 155.55,182.68 157.42,181.69 159.29,180.67 161.16,179.61 163.03,178.5 164.9,177.36 166.77,176.17 168.64,174.93 170.51,173.64 172.38,172.31 174.25,170.92 176.12,169.48 177.99,167.99 179.86,166.43 181.73,164.81 183.6,163.14 185.47,161.39 187.34,159.58 189.21,157.7 191.08,155.75 192.95,153.72 194.82,151.61 196.69,149.41 198.56,147.14 200.43,144.77 202.3,142.32 204.17,139.76 206.04,137.11 207.91,134.36 209.78,131.5 211.65,128.52 213.52,125.43 215.39,122.23 217.26,118.89 219.13,115.43 221,111.83 222.87,108.1 224.74,104.21 226.61,100.18 228.48,95.99 230.35,91.64 232.22,87.12 234.09,82.42 235.96,77.54 237.83,72.47 239.7,67.2 241.57,61.73 243.44,56.05 245.31,50.14 247.18,44.01 249.05,37.64 250.92,31.02 252.79,24.14 254.66,17" fill="none" stroke="#0f6e56" stroke-width="2.8"/><polyline points="85.34,17 87.21,24.14 89.08,31.02 90.95,37.64 92.82,44.01 94.69,50.14 96.56,56.05 98.43,61.73 100.3,67.2 102.17,72.47 104.04,77.54 105.91,82.42 107.78,87.12 109.65,91.64 111.52,95.99 113.39,100.18 115.26,104.21 117.13,108.1 119,111.83 120.87,115.43 122.74,118.89 124.61,122.23 126.48,125.43 128.35,128.52 130.22,131.5 132.09,134.36 133.96,137.11 135.83,139.76 137.7,142.32 139.57,144.77 141.44,147.14 143.31,149.41 145.18,151.61 147.05,153.72 148.92,155.75 150.79,157.7 152.66,159.58 154.53,161.39 156.4,163.14 158.27,164.81 160.14,166.43 162.01,167.99 163.88,169.48 165.75,170.92 167.62,172.31 169.49,173.64 171.36,174.93 173.23,176.17 175.1,177.36 176.97,178.5 178.84,179.61 180.71,180.67 182.58,181.69 184.45,182.68 186.32,183.62 188.19,184.53 190.06,185.41 191.93,186.26 193.8,187.07 195.67,187.85 197.54,188.61 199.41,189.33 201.28,190.03 203.15,190.7 205.02,191.35 206.89,191.97 208.76,192.57 210.63,193.15 212.5,193.7 214.37,194.24 216.24,194.75 218.11,195.25 219.98,195.73 221.85,196.19 223.72,196.63 225.59,197.05 227.46,197.46 229.33,197.86 231.2,198.24 233.07,198.6 234.94,198.95 236.81,199.29 238.68,199.62 240.55,199.93 242.42,200.23 244.29,200.52 246.16,200.8 248.03,201.07 249.9,201.33 251.77,201.58 253.64,201.82 255.51,202.05 257.38,202.27 259.25,202.49 261.12,202.69 262.99,202.89 264.86,203.08 266.73,203.27 268.6,203.44 270.47,203.62 272.34,203.78 274.21,203.94 276.08,204.09 277.95,204.24 279.82,204.38 281.69,204.51 283.56,204.64 285.43,204.77 287.3,204.89 289.17,205.01 291.04,205.12 292.91,205.23 294.78,205.33 296.65,205.43 298.52,205.52 300.39,205.62 302.26,205.71 304.13,205.79 306,205.88" fill="none" stroke="#b45309" stroke-width="2.8"/><circle cx="170" cy="174" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="204" y="164" text-anchor="start" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(0 ; 1)</text><text x="263.5" y="31.2" text-anchor="start" fill="#0f6e56" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = 2ˣ</text><text x="76.5" y="31.2" text-anchor="end" fill="#b45309" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = (1/2)ˣ</text></svg>
:::

La symétrie du dessin traduit (1/2)ˣ = 2^(−x) ; la courbe verte croît parce que ln 2 > 0, l'orange décroît parce que ln(1/2) < 0.

::: exemple Calculer avec aˣ
1. 2^(7/2) = 2³ × 2^(1/2) = 8√2 ≈ 11,3 : c'est le nombre de nénuphars au bout de 3 jours et demi, car les exposants s'additionnent.
2. (3ˣ)′ = (ln 3) 3ˣ, car 3ˣ = e^(x ln 3) a pour dérivée (ln 3) e^(x ln 3).
3. 5ˣ = 40 ⟺ x ln 5 = ln 40, en prenant ln, soit x = ln 40/ln 5 ≈ 3,689/1,609 ≈ 2,29.
4. 9ˣ − 4 × 3ˣ + 3 = 0. Comme 9ˣ = (3ˣ)², on pose X = 3ˣ > 0 : X² − 4X + 3 = (X − 1)(X − 3) = 0, donc X = 1 ou X = 3, soit **x = 0 ou x = 1**.

:::

Les règles utilisées se résument ainsi :

| Règle (a > 0, b > 0, x et x′ réels) | Pourquoi |
| --- | --- |
| aˣ × a^(x′) = a^(x+x′) et aˣ × bˣ = (ab)ˣ | e^(x ln a) × e^(x′ ln a) = e^((x+x′) ln a), et ln a + ln b = ln(ab) |
| aˣ × a^(−x) = 1 et (aˣ)^(x′) = a^(xx′) | a^(−x) = e^(−x ln a) = 1/aˣ, et (aˣ)^(x′) = e^(x′ ln aˣ) = e^(x′ x ln a) |
| (aˣ)′ = (ln a) aˣ | aˣ = e^u avec u = x ln a et u′ = ln a |


::: piege Dériver aˣ comme une puissance
On écrit « (2ˣ)′ = x × 2^(x−1) ». Cela tente parce que (xⁿ)′ = n xⁿ⁻¹. Mais cette règle suppose la variable en base et un exposant constant. Ici la variable est en exposant : 2ˣ = e^(x ln 2) et (2ˣ)′ = (ln 2) 2ˣ.
:::

::: exemple Demi-vie de l'iode 131 : 8 jours
La quantité est N(t) = N₀ (1/2)^(t/8). Après combien de jours reste-t-il 10 % de N₀ ?
1. N(t)/N₀ = 0,1 ⟺ (1/2)^(t/8) = 0,1.
2. On prend ln : (t/8) ln(1/2) = ln 0,1, soit −(t/8) ln 2 = −ln 10.
3. t = 8 ln 10/ln 2 ≈ 8 × 3,3219 ≈ 26,6 jours. Contrôle : après 24 jours (3 demi-vies) il reste 1/8 = 12,5 %, après 32 jours 6,25 % ✓.

:::

::: methode
Un modèle exponentiel est Q(t) = Q₀ aᵗ. Une grandeur qui varie de p % par période est multipliée par 1 + p/100 à chaque période : a = 1,05 pour +5 %, a = 0,95 pour −5 %. Pour trouver l'instant où Q atteint une valeur, on prend ln des deux membres et l'on divise par ln a, en regardant son signe.

Cas limite : pour 0 < a < 1, ln a < 0 ; la **demi-vie** T vérifie aᵀ = 1/2, donc T = −ln 2/ln a.
:::

::: verifie
Calculer (4ˣ)′ en x = 0, puis résoudre 2ˣ = 12.

---

(4ˣ)′ = (ln 4) 4ˣ, donc en x = 0 la dérivée vaut (ln 4) × 4⁰ = ln 4 ≈ 1,39. Puis 2ˣ = 12 ⟺ x ln 2 = ln 12, donc x = ln 12/ln 2 ≈ 3,58. On a dérivé avec le facteur ln a, puis pris ln des deux membres.
:::

::: retenir
aˣ = e^(x ln a) pour a > 0, avec (aˣ)′ = (ln a) aˣ ; croissante si a > 1, décroissante si 0 < a < 1 ; les courbes de aˣ et (1/a)ˣ sont symétriques par rapport à l'axe des ordonnées ; une équation en exposant se résout avec ln.
:::

## 🎯 Étudier une fonction avec exponentielle

Une fonction mêle un terme affine 2x − 3 et un terme exponentiel e^(−x) : à droite, l'exponentielle s'éteint ; à gauche, elle explose. Que devient la courbe aux deux extrémités, et coupe-t-elle l'axe des abscisses ?

::: exemple Limites et asymptote de f(x) = 2x − 3 + e^(−x)
1. f est définie sur ℝ. En +∞ : e^(−x) → 0 et 2x − 3 → +∞, donc f(x) → +∞.
2. En −∞ : f(x) = e^(−x)(1 + (2x − 3)eˣ) et (2x − 3)eˣ → 0 (car x eˣ → 0), donc le facteur tend vers 1 et f(x) → +∞.
3. f(x) − (2x − 3) = e^(−x) tend vers 0 en +∞ : la droite D : y = 2x − 3 est asymptote oblique en +∞, et la courbe est au-dessus de D puisque e^(−x) > 0.
4. En −∞, f(x)/x = 2 − 3/x + e^(−x)/x, avec e^(−x)/x → −∞ : la courbe a une branche parabolique de direction l'axe des ordonnées.

:::

::: piege Placer l'asymptote oblique à l'autre infini
On affirme « la droite y = 2x − 3 est asymptote en −∞ et en +∞ ». Cela tente parce que 2x − 3 est la partie affine de f. Mais f(x) − (2x − 3) = e^(−x) tend vers 0 en +∞ et vers +∞ en −∞ : D n'est asymptote qu'en +∞. En −∞, la courbe s'éloigne de D.
:::

::: exemple Variations et zéros
1. f′(x) = 2 − e^(−x), car (e^(−x))′ = −e^(−x). Alors f′(x) ≥ 0 ⟺ e^(−x) ≤ 2 ⟺ −x ≤ ln 2 ⟺ x ≥ −ln 2.
2. Le minimum est f(−ln 2) = −2 ln 2 − 3 + e^(ln 2) = −1 − 2 ln 2 ≈ −2,39.
3. f(−2) ≈ 0,39 > 0 et f(−1) ≈ −2,28 < 0 : f est continue et strictement monotone sur [−2 ; −1], donc s'annule une fois (valeurs intermédiaires). De même f(1) ≈ −0,63 < 0 et f(2) ≈ 1,14 > 0 : une autre racine dans ]1 ; 2[.

:::

Les variations se résument ainsi :

| x | −∞ | | −ln 2 | | +∞ |
| --- | --- | --- | --- | --- | --- |
| f′(x) | | − | 0 | + | |
| f(x) | +∞ | ↘ | −1 − 2 ln 2 | ↗ | +∞ |

::: figure La courbe de f monte le long de la droite D à droite, s'en écarte vers le haut à gauche et présente un minimum
<svg viewBox="0 0 300 280"><title>La courbe de f(x) = 2x − 3 + e^(−x) a un minimum, monte le long de sa droite asymptote D à droite et s'en écarte vers le haut à gauche</title><line x1="24" y1="150" x2="232" y2="150" stroke="#0f172a" stroke-width="1.6"/><line x1="105" y1="270" x2="105" y2="8" stroke="#0f172a" stroke-width="1.6"/><polygon points="232,150 225,146.5 225,153.5" fill="#0f172a"/><polygon points="105,8 101.5,15 108.5,15" fill="#0f172a"/><text x="226" y="143" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="113" y="20" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="45" y1="147" x2="45" y2="153" stroke="#0f172a" stroke-width="1.3"/><text x="37" y="165" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="75" y1="147" x2="75" y2="153" stroke="#0f172a" stroke-width="1.3"/><text x="75" y="165" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="135" y1="147" x2="135" y2="153" stroke="#0f172a" stroke-width="1.3"/><text x="135" y="165" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="165" y1="147" x2="165" y2="153" stroke="#0f172a" stroke-width="1.3"/><text x="165" y="165" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="195" y1="147" x2="195" y2="153" stroke="#0f172a" stroke-width="1.3"/><text x="195" y="165" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="102" y1="240" x2="108" y2="240" stroke="#0f172a" stroke-width="1.3"/><text x="99" y="244" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−3</text><line x1="102" y1="210" x2="108" y2="210" stroke="#0f172a" stroke-width="1.3"/><text x="99" y="214" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="102" y1="180" x2="108" y2="180" stroke="#0f172a" stroke-width="1.3"/><text x="99" y="184" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="102" y1="120" x2="108" y2="120" stroke="#0f172a" stroke-width="1.3"/><text x="99" y="124" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="102" y1="90" x2="108" y2="90" stroke="#0f172a" stroke-width="1.3"/><text x="99" y="94" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="102" y1="60" x2="108" y2="60" stroke="#0f172a" stroke-width="1.3"/><text x="99" y="64" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="102" y1="30" x2="108" y2="30" stroke="#0f172a" stroke-width="1.3"/><text x="99" y="34" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="90" y1="270" x2="219" y2="12" stroke="#b45309" stroke-width="1.8" stroke-dasharray="6 3"/><polyline points="29.02,14.4 30.03,24.83 31.03,34.85 32.04,44.47 33.04,53.71 34.05,62.58 35.05,71.09 36.06,79.25 37.07,87.08 38.07,94.58 39.07,101.78 40.08,108.66 41.09,115.26 42.09,121.57 43.09,127.61 44.1,133.38 45.11,138.89 46.11,144.16 47.11,149.19 48.12,153.98 49.12,158.56 50.13,162.91 51.14,167.06 52.14,171 53.15,174.74 54.15,178.3 55.15,181.67 56.16,184.87 57.16,187.89 58.17,190.75 59.18,193.45 60.18,195.99 61.18,198.39 62.19,200.63 63.19,202.74 64.2,204.71 65.2,206.56 66.21,208.27 67.22,209.86 68.22,211.33 69.22,212.69 70.23,213.94 71.24,215.08 72.24,216.11 73.24,217.05 74.25,217.89 75.26,218.63 76.26,219.29 77.27,219.85 78.27,220.33 79.27,220.73 80.28,221.05 81.29,221.3 82.29,221.46 83.3,221.56 84.3,221.59 85.31,221.55 86.31,221.44 87.32,221.28 88.32,221.05 89.33,220.76 90.33,220.42 91.34,220.02 92.34,219.57 93.35,219.07 94.35,218.51 95.35,217.91 96.36,217.27 97.37,216.58 98.37,215.84 99.38,215.06 100.38,214.25 101.39,213.39 102.39,212.49 103.4,211.56 104.4,210.59 105.41,209.59 106.41,208.56 107.42,207.49 108.42,206.39 109.43,205.26 110.43,204.11 111.43,202.92 112.44,201.71 113.45,200.47 114.45,199.21 115.46,197.92 116.46,196.61 117.46,195.27 118.47,193.91 119.48,192.53 120.48,191.13 121.48,189.71 122.49,188.27 123.5,186.82 124.5,185.34 125.51,183.84 126.51,182.33 127.51,180.81 128.52,179.26 129.53,177.7 130.53,176.13 131.54,174.54 132.54,172.94 133.55,171.33 134.55,169.7 135.56,168.06 136.56,166.4 137.57,164.74 138.57,163.06 139.57,161.37 140.58,159.68 141.58,157.97 142.59,156.25 143.6,154.52 144.6,152.79 145.61,151.04 146.61,149.29 147.61,147.52 148.62,145.75 149.63,143.97 150.63,142.19 151.64,140.39 152.64,138.59 153.65,136.78 154.65,134.97 155.66,133.15 156.66,131.32 157.67,129.49 158.67,127.65 159.68,125.8 160.68,123.95 161.69,122.1 162.69,120.23 163.7,118.37 164.7,116.5 165.71,114.62 166.71,112.74 167.71,110.86 168.72,108.97 169.73,107.08 170.73,105.19 171.74,103.29 172.74,101.38 173.75,99.48 174.75,97.57 175.76,95.65 176.76,93.74 177.77,91.82 178.77,89.89 179.77,87.97 180.78,86.04 181.79,84.11 182.79,82.18 183.79,80.24 184.8,78.3 185.81,76.36 186.81,74.42 187.82,72.47 188.82,70.52 189.83,68.58 190.83,66.62 191.83,64.67 192.84,62.71 193.85,60.76 194.85,58.8 195.86,56.84 196.86,54.88 197.87,52.91 198.87,50.95 199.88,48.98 200.88,47.01 201.89,45.04 202.89,43.07 203.9,41.1 204.9,39.13 205.91,37.15 206.91,35.18 207.92,33.2 208.92,31.22 209.93,29.24 210.93,27.26 211.94,25.28 212.94,23.3 213.95,21.32 214.95,19.33 215.96,17.35 216.96,15.36 217.97,13.38" fill="none" stroke="#0f6e56" stroke-width="2.8"/><circle cx="84.21" cy="221.59" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="60" y="244" text-anchor="middle" fill="#0f6e56" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">minimum</text><text x="222" y="44" text-anchor="start" fill="#b45309" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><text x="34" y="42" text-anchor="start" fill="#0f6e56" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text></svg>
:::

Le minimum du dessin est le point d'abscisse −ln 2 du tableau ; la courbe verte se rapproche de la droite D quand x grandit, ce qui traduit la limite e^(−x) → 0.

::: exemple Une courbe en cloche : h(x) = e^(−x²+2x)
1. h = e^u avec u(x) = −x² + 2x, définie sur ℝ, et h > 0. Quand x → ±∞, u → −∞, donc h → 0 : l'axe des abscisses est asymptote des deux côtés.
2. h′(x) = (−2x + 2)e^u a le signe de 2 − 2x : h croît sur ]−∞ ; 1] et décroît sur [1 ; +∞[, avec un maximum h(1) = e.
3. u(2 − x) = −(2 − x)² + 2(2 − x) = −x² + 2x = u(x), donc h(2 − x) = h(x) : la droite x = 1 est axe de symétrie (chapitre 5).

:::

::: methode
Pour étudier f avec exponentielle :

1. domaine ; limites, en utilisant e^u → 0 si u → −∞ et e^u → +∞ si u → +∞, et les comparaisons pour une forme indéterminée ;
2. dérivée par u′e^u ou par la formule du produit, en factorisant e^u : comme e^u > 0, le signe de f′ est celui du facteur restant ;
3. tableau de variation, asymptotes et branches infinies, puis valeurs intermédiaires pour les zéros ;
4. nombre de solutions de f(x) = m : on lit les points communs de la courbe et de la droite horizontale y = m ; la courbe de |f| garde les parties où f ≥ 0 et retourne celles où f < 0 par symétrie d'axe (Ox).

Cas limite : quand f(x) → ±∞, une branche parabolique de direction (Ox) se reconnaît à f(x)/x → 0, et de direction (Oy) à f(x)/x → ±∞.
:::

::: verifie
Pour g(x) = 3x + 2e^(−x), donner l'asymptote oblique en +∞ et le minimum.

---

g(x) − 3x = 2e^(−x) → 0 en +∞ : l'asymptote est y = 3x. Puis g′(x) = 3 − 2e^(−x) s'annule quand e^(−x) = 3/2, soit x = −ln(3/2) = ln(2/3), et g′ > 0 après : le minimum est g(ln(2/3)) = 3 ln(2/3) + 2 × 3/2 = 3 + 3 ln(2/3) ≈ 1,78. On a étudié l'écart avec la droite, puis le signe de g′.
:::

::: retenir
Une étude avec exponentielle suit : domaine, limites (comparaisons), dérivée factorisée par e^u, tableau, asymptotes et branches ; l'asymptote oblique se prouve par une différence qui tend vers 0, à un seul infini si l'autre terme explose.
:::

> 🏆 Septième porte franchie, héros. Tu sais définir et dériver l'exponentielle, résoudre avec elle, la comparer aux puissances, la décliner en aˣ et en xʳ et étudier une fonction qui la contient. Au chapitre 8, le calcul intégral te donnera de nouveaux usages des primitives de u′e^u.
