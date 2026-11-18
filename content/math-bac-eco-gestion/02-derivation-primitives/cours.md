# ⚔️ Dérivation et primitives — optimiser le profit, remonter jusqu'au coût total

> 💡 «La dérivée mesure à quelle vitesse une grandeur change ; la primitive fait le chemin inverse : à partir de la vitesse, elle retrouve la grandeur.»

Bienvenue, héros de l'Économie et gestion. Un chef d'entreprise veut savoir combien coûte un objet de plus, quand son coût moyen cesse de baisser et pour quelle production son bénéfice est maximal : trois questions auxquelles la dérivée répond. Huit étapes te mènent du nombre dérivé aux primitives : nombre dérivé et point anguleux, opérations, composée, réciproque, variations et extremums, dérivée seconde, accroissements finis, primitives. On suppose acquis le calcul des limites et la continuité (chapitre 1), fonction réciproque comprise. Les études complètes de fonctions viendront au chapitre suivant.

## 🧭 Nombre dérivé, tangente et point anguleux

Un atelier de poterie fabrique x objets par semaine ; son coût total est C(x) = x² + 20x dinars. Il en fabrique 10 : combien lui coûtera, à peu près, l'objet suivant ? Entre 10 et 10 + h objets, le coût moyen de chaque objet ajouté est (C(10 + h) − C(10))/h.
Que devient ce nombre quand h devient aussi petit qu'on veut ?

::: definition
Soit f définie sur un intervalle ouvert I et x₀ un réel de I. **f est dérivable en x₀** si le **taux d'accroissement** (f(x) − f(x₀))/(x − x₀) a une limite **finie** ℓ quand x tend vers x₀ :

$$ lim x→x₀ (f(x) − f(x₀))/(x − x₀) = ℓ $$

Ce réel est le **nombre dérivé** f′(x₀). En ne regardant que x > x₀ (resp. x < x₀), la limite est le nombre dérivé à droite **f′d(x₀)** (resp. à gauche **f′g(x₀)**), et f est dérivable en x₀ si et seulement si f′g(x₀) = f′d(x₀), valeur finie.

f est **dérivable sur ]a ; b[** si elle l'est en tout point de ]a ; b[, et **sur [a ; b]** si elle l'est sur ]a ; b[, à droite en a et à gauche en b.
:::

::: figure La sécante (AM), de pente 42, pivote autour de A et devient la tangente, de pente 40, quand M glisse vers A
<svg viewBox="0 0 340 250"><title>Courbe de C : x ↦ x² + 20x, point A(10 ; 300), tangente de pente 40 et sécante (AM) de pente 42 avec M(12 ; 384)</title><polyline points="46.0,224.0 50.0,222.2 54.0,220.4 58.0,218.6 62.0,216.7 66.0,214.8 70.0,212.9 74.0,210.9 78.0,208.9 82.0,206.8 86.0,204.8 90.0,202.6 94.0,200.5 98.0,198.3 102.0,196.1 106.0,193.8 110.0,191.5 114.0,189.2 118.0,186.8 122.0,184.4 126.0,182.0 130.0,179.5 134.0,177.0 138.0,174.5 142.0,171.9 146.0,169.3 150.0,166.7 154.0,164.0 158.0,161.3 162.0,158.5 166.0,155.8 170.0,152.9 174.0,150.1 178.0,147.2 182.0,144.3 186.0,141.3 190.0,138.3 194.0,135.3 198.0,132.2 202.0,129.1 206.0,126.0 210.0,122.8 214.0,119.6 218.0,116.4 222.0,113.1 226.0,109.8 230.0,106.5 234.0,103.1 238.0,99.7 242.0,96.2 246.0,92.8 250.0,89.2 254.0,85.7 258.0,82.1 262.0,78.5 266.0,74.8 270.0,71.1 274.0,67.4 278.0,63.6 282.0,59.8 286.0,56.0 290.0,52.1 294.0,48.2 298.0,44.3 302.0,40.3 306.0,36.3 310.0,32.3 314.0,28.2 318.0,24.1 322.0,19.9 326.0,15.8" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="206.0" y1="129.5" x2="306.0" y2="37.6" stroke="#64748b" stroke-width="1.8" stroke-dasharray="6 4"/><line x1="146.0" y1="180.2" x2="306.0" y2="40.2" stroke="#b45309" stroke-width="2.4"/><line x1="246.0" y1="92.8" x2="246.0" y2="224.0" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><line x1="286.0" y1="56.0" x2="286.0" y2="224.0" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><circle cx="246.0" cy="92.8" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="238.0" y="86.8" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><circle cx="286.0" cy="56.0" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="277.0" y="50.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><text x="152.0" y="193.4" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente : pente 40</text><text x="152.0" y="215.2" text-anchor="start" font-size="11" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">sécante (AM) : pente 42</text><text x="66.0" y="31.5" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><line x1="40" y1="224.0" x2="336" y2="224.0" stroke="#0f172a" stroke-width="1.6"/><line x1="46.0" y1="230" x2="46.0" y2="6" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,224.0 329,220.5 329,227.5" fill="#0f172a"/><polygon points="46.0,6 42.5,13 49.5,13" fill="#0f172a"/><text x="332.0" y="217.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="54.0" y="18.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="246.0" y1="221.0" x2="246.0" y2="227.0" stroke="#0f172a" stroke-width="1.3"/><text x="246.0" y="239.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="286.0" y1="221.0" x2="286.0" y2="227.0" stroke="#0f172a" stroke-width="1.3"/><text x="286.0" y="239.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12</text><line x1="43.0" y1="92.8" x2="49.0" y2="92.8" stroke="#0f172a" stroke-width="1.3"/><text x="40.0" y="96.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">300</text><line x1="43.0" y1="56.0" x2="49.0" y2="56.0" stroke="#0f172a" stroke-width="1.3"/><text x="40.0" y="60.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">384</text></svg>
:::

La pente de la sécante (AM) est le taux d'accroissement entre 10 et 12 : (384 − 300)/(12 − 10) = 42. Quand M glisse vers A, cette pente tend vers celle de la tangente orange : c'est le nombre dérivé C′(10), que l'exemple calcule.

::: exemple L'objet suivant, à 10 objets : C(x) = x² + 20x
1. C(10) = 100 + 200 = 300. Le taux entre 10 et 10 + h est (C(10 + h) − C(10))/h.
2. C(10 + h) = (10 + h)² + 20(10 + h) = 300 + 40h + h², donc le taux vaut (40h + h²)/h = 40 + h pour h ≠ 0 : on simplifie par h avant de passer à la limite.
3. lim h→0 (40 + h) = 40, un réel : C est dérivable en 10 et C′(10) = 40. Passer de 10 à 11 objets coûte environ 40 dinars de plus (le calcul exact donne C(11) − C(10) = 41).
4. La tangente en A(10 ; 300) a pour pente 40 : y = 40(x − 10) + 300 = 40x − 100.

:::

Et quand la pente n'est pas la même des deux côtés ? Un atelier paie son eau g(x) = 2x dinars jusqu'à 3 m³, puis g(x) = 3x − 3 au-delà : la tranche suivante est plus chère, mais les deux formules se raccordent au point A(3 ; 6), car 2 × 3 = 6 et 3 × 3 − 3 = 6.

::: figure En A(3 ; 6), la courbe a deux demi-tangentes de pentes différentes : 2 à gauche et 3 à droite
<svg viewBox="0 0 340 230"><title>Courbe de g (deux morceaux de droites) et, au point A(3 ; 6), demi-tangentes de pentes 2 à gauche et 3 à droite</title><line x1="40.0" y1="204.0" x2="183.0" y2="132.8" stroke="#7c3aed" stroke-width="3"/><line x1="183.0" y1="132.8" x2="326.0" y2="25.9" stroke="#b45309" stroke-width="3"/><line x1="183.0" y1="132.8" x2="278.3" y2="85.2" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="6 4"/><line x1="111.5" y1="186.2" x2="183.0" y2="132.8" stroke="#b45309" stroke-width="1.5" stroke-dasharray="6 4"/><line x1="183.0" y1="132.8" x2="183.0" y2="204.0" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><circle cx="183.0" cy="132.8" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="174.0" y="125.8" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="49.5" y="106.6" text-anchor="start" font-size="11" font-weight="700" fill="#7c3aed" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pente 2</text><text x="230.7" y="31.8" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pente 3</text><line x1="34" y1="204.0" x2="336" y2="204.0" stroke="#0f172a" stroke-width="1.6"/><line x1="40.0" y1="210" x2="40.0" y2="6" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,204.0 329,200.5 329,207.5" fill="#0f172a"/><polygon points="40.0,6 36.5,13 43.5,13" fill="#0f172a"/><text x="332.0" y="197.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="48.0" y="18.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="183.0" y1="201.0" x2="183.0" y2="207.0" stroke="#0f172a" stroke-width="1.3"/><text x="183.0" y="219.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="326.0" y1="201.0" x2="326.0" y2="207.0" stroke="#0f172a" stroke-width="1.3"/><text x="326.0" y="219.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="37.0" y1="132.8" x2="43.0" y2="132.8" stroke="#0f172a" stroke-width="1.3"/><text x="34.0" y="136.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="37.0" y1="25.9" x2="43.0" y2="25.9" stroke="#0f172a" stroke-width="1.3"/><text x="34.0" y="29.9" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">15</text></svg>
:::

Les deux demi-droites tracées en A sont les limites des sécantes : celle de droite a pour pente g′d(3), celle de gauche g′g(3).

::: exemple La facture d'eau en x = 3
1. g(3) = 6. Pour x < 3, g(x) = 2x : le taux (2x − 6)/(x − 3) vaut 2, donc g′g(3) = 2.
2. Pour x > 3, le taux (3x − 3 − 6)/(x − 3) = (3x − 9)/(x − 3) vaut 3, donc g′d(3) = 3.
3. 2 ≠ 3 : g n'est pas dérivable en 3, bien qu'elle y soit continue. La courbe a un **point anguleux** en A, avec les demi-tangentes y = 2x (à gauche) et y = 3x − 3 (à droite).

:::

::: piege Écrire la tangente y = f′(x₀)x + f(x₀)
Pour l'atelier de poterie, on écrit y = 40x + 300. Cela tente parce que, dans y = mx + p, le nombre m est la pente et que f(x₀) = 300 ressemble à une ordonnée à l'origine. Mais 300 est l'ordonnée au point d'abscisse 10, pas en 0 : la droite y = 40x + 300 passe par (10 ; 700), pas par A(10 ; 300). La bonne équation décale de x₀ : y = 40(x − 10) + 300 = 40x − 100.
:::

::: propriete
- Si f est dérivable en x₀, sa courbe admet au point M₀(x₀ ; f(x₀)) une **tangente** de pente f′(x₀), d'équation y = f′(x₀)(x − x₀) + f(x₀).
- Théorème (admis) : toute fonction dérivable en x₀ est continue en x₀.
- Si f est dérivable à droite (resp. à gauche) en x₀, sa courbe admet une **demi-tangente** d'équation y = f′d(x₀)(x − x₀) + f(x₀) pour x ≥ x₀ (resp. avec f′g(x₀) pour x ≤ x₀). Deux demi-tangentes de pentes différentes : point anguleux.
- Pour une fonction définie par deux formules, on contrôle d'abord que les valeurs se raccordent, puis on compare les deux taux.

Cas limite : la réciproque du théorème est fausse, g est continue en 3 sans y être dérivable. Si le taux tend vers +∞ ou −∞, la demi-tangente est verticale : √x, de taux 1/√x, n'est pas dérivable à droite en 0.
:::

::: verifie
Un transporteur facture h(x) = 4x dinars jusqu'à 2 colis, puis h(x) = 2x + 4 au-delà. La fonction h est-elle dérivable en 2 ?

---

On contrôle d'abord le raccord : h(2) = 8 et 2 × 2 + 4 = 8, donc h est continue en 2. À gauche, le taux vaut (4x − 8)/(x − 2) = 4 : h′g(2) = 4. À droite, il vaut (2x + 4 − 8)/(x − 2) = (2x − 4)/(x − 2) = 2 : h′d(2) = 2. Comme 4 ≠ 2, h n'est pas dérivable en 2 : point anguleux, demi-tangentes y = 4x (à gauche) et y = 2x + 4 (à droite).
:::

::: retenir
f′(x₀) est la limite du taux d'accroissement et la pente de la tangente y = f′(x₀)(x − x₀) + f(x₀) ; f est dérivable en x₀ exactement quand f′g(x₀) = f′d(x₀), valeur finie, et dérivable entraîne continue, mais pas l'inverse.
:::

## 🔮 Fonction dérivée, opérations, coût moyen et élasticité

Pour une briqueterie, le coût total de x milliers de briques est C(x) = 2x² + 30x + 98 dinars ; le coût moyen par millier est CM(x) = C(x)/x. Il baisse d'abord, puis remonte à cause des frais qui grandissent avec la production.
Comment dériver ce quotient, et le coût marginal C′ répond-il à la question ?

::: definition
Soit f dérivable sur un intervalle I. La **fonction dérivée** de f est la fonction f′, définie sur I, qui à tout réel x de I associe le nombre dérivé f′(x). Le **coût marginal** est, par convention, Cm = C′ : il approche le coût de la production d'une unité supplémentaire. Le **coût moyen** est CM(x) = C(x)/x, le coût par unité produite.
:::

Les dérivées usuelles se démontrent par le taux d'accroissement, comme dans la section précédente :

| f(x) | f′(x) | sur |
| --- | --- | --- |
| k (constante) | 0 | ℝ |
| ax + b | a | ℝ |
| xⁿ (n entier) | nxⁿ⁻¹ | ℝ si n ≥ 1, ]−∞ ; 0[ et ]0 ; +∞[ si n ≤ −1 |
| √x | 1/(2√x) | ]0 ; +∞[ |

::: exemple Le coût moyen de la briqueterie : CM(x) = C(x)/x
1. On pose u(x) = 2x² + 30x + 98 et v(x) = x, donc u′(x) = 4x + 30 et v′(x) = 1. Le quotient est dérivable là où v ne s'annule pas, donc sur ]0 ; +∞[.
2. (u/v)′ = (u′v − uv′)/v², donc CM′(x) = ((4x + 30)x − (2x² + 30x + 98))/x².
3. Le numérateur vaut 4x² + 30x − 2x² − 30x − 98 = 2x² − 98, donc CM′(x) = (2x² − 98)/x² = 2 − 98/x².
4. Contrôle : CM(x) = 2x + 30 + 98/x, dont la dérivée est bien 2 − 98/x².

:::

::: definition
L'**élasticité** de la demande D au prix p est E(p) = p × D′(p)/D(p). Elle donne, à peu près, le pourcentage de variation de la demande quand le prix augmente de 1 %.
:::

::: exemple L'élasticité de D(p) = 1200/(p + 2)
1. D(p) = 1200 × 1/(p + 2) : avec v(p) = p + 2 et v′ = 1, (1/v)′ = −v′/v² donne D′(p) = −1200/(p + 2)².
2. E(p) = p × D′(p)/D(p) = p × (−1200/(p + 2)²) × (p + 2)/1200 = −p/(p + 2).
3. À p = 8 dinars, E(8) = −8/10 = −0,8 : une hausse de 1 % du prix fait baisser la demande d'environ 0,8 %.

:::

::: piege Confondre la dérivée du coût moyen et le coût marginal
Pour la briqueterie, on écrit CM′(x) = C′(x) = 4x + 30. Cela tente parce que « le coût marginal est la dérivée du coût ». Mais C′ est la dérivée du coût **total** ; le coût moyen est le quotient C(x)/x et se dérive avec la règle du quotient : CM′(x) = 2 − 98/x². Test en x = 7 : 4x + 30 = 58 > 0 annoncerait un coût moyen croissant, alors que CM′(7) = 2 − 98/49 = 0.
:::

::: propriete
Soient f et g dérivables sur I et λ un réel. Alors λf, f + g et fg sont dérivables sur I et :
- (λf)′ = λf′ ; (f + g)′ = f′ + g′ ; (fg)′ = f′g + fg′.
- En tout x de I où g(x) ≠ 0 : (1/g)′ = −g′/g² et (f/g)′ = (f′g − fg′)/g².
- Toute fonction polynôme est dérivable sur ℝ, toute fonction rationnelle sur chaque intervalle de son ensemble de définition.

Cas limite : la dérivée d'un produit n'est pas le produit des dérivées, et l'ensemble de dérivabilité peut être plus petit que l'ensemble de définition (√x est définie en 0, pas dérivable en 0).
:::

::: verifie
Dériver f(x) = (x − 4)/(x + 2) et préciser les intervalles de dérivabilité.

---

Avec u(x) = x − 4 (u′ = 1) et v(x) = x + 2 (v′ = 1), f′(x) = (u′v − uv′)/v² = ((x + 2) − (x − 4))/(x + 2)² = 6/(x + 2)². La fonction est dérivable là où x + 2 ≠ 0, donc sur ]−∞ ; −2[ et sur ]−2 ; +∞[. Le numérateur commence par u′v : écrit à l'envers, il donnerait −6.
:::

::: retenir
(fg)′ = f′g + fg′ et (f/g)′ = (f′g − fg′)/g² : le coût moyen C/x se dérive comme un quotient, pas comme C′, et l'élasticité E(p) = p D′(p)/D(p) se lit comme un pourcentage.
:::

## 🔗 Dérivée d'une composée

Dans une usine, le coût de fonctionnement vaut K(x) = √(x² + 16) milliers de dinars pour x centaines d'articles. La racine porte sur x² + 16, pas sur x : la formule (√x)′ = 1/(2√x) ne suffit plus.
Comment dériver une fonction fabriquée en deux temps ?

::: definition
La **composée** de f par g, notée g ∘ f, est la fonction x ↦ g(f(x)) : on applique f d'abord, puis g au résultat.
:::

::: exemple Le coût K(x) = √(x² + 16)
1. K = g ∘ u avec u(x) = x² + 16, qui est strictement positive, et g(t) = √t. La fonction extérieure est g, l'intérieure est u.
2. g′(t) = 1/(2√t) et u′(x) = 2x.
3. On dérive l'extérieure en gardant l'intérieure, puis on multiplie par la dérivée de l'intérieure : K′(x) = g′(u(x)) × u′(x) = (1/(2√(x² + 16))) × 2x = x/√(x² + 16).
4. À x = 3 : K(3) = 5 et K′(3) = 3/5 = 0,6 : le coût croît d'environ 0,6 millier de dinars par centaine d'articles de plus.

:::

::: exemple Deux puissances
1. f(x) = (x² + 3x)⁴ : avec u(x) = x² + 3x et n = 4, f′(x) = 4 × u′(x) × u(x)³ = 4(2x + 3)(x² + 3x)³.
2. g(x) = 1/(x − 1)⁵ = (x − 1)⁻⁵ sur ]1 ; +∞[ : avec u(x) = x − 1, u′ = 1 et n = −5, g′(x) = −5 × 1 × (x − 1)⁻⁶ = −5/(x − 1)⁶.

:::

::: piege Oublier la dérivée de l'intérieur
Pour f(x) = (x² + 3x)⁴, on écrit f′(x) = 4(x² + 3x)³. Cela tente parce que la règle (xⁿ)′ = nxⁿ⁻¹ ressemble à celle-ci. Mais l'intérieur x² + 3x n'est pas x : il manque le facteur u′(x) = 2x + 3. En x = 1, la bonne pente est 4 × 5 × 4³ = 1280, la formule oubliée donne 4 × 4³ = 256.
:::

::: propriete
- Si f est dérivable sur I et g dérivable sur un intervalle contenant f(I), alors g ∘ f est dérivable sur I et (g ∘ f)′(x) = g′(f(x)) × f′(x).
- Pour n entier : (fⁿ)′ = n f′ fⁿ⁻¹, avec f ≠ 0 si n ≤ −1.
- Si f > 0 sur I : (√f)′ = f′/(2√f).
- Rappel : sin et cos sont dérivables sur ℝ, avec sin′(x) = cos x et cos′(x) = −sin x ; par composition, (sin(ax + b))′ = a cos(ax + b) et (cos(ax + b))′ = −a sin(ax + b).

Cas limite : √f n'est pas dérivable là où f s'annule : √(x − 2) est dérivable sur ]2 ; +∞[ seulement, alors qu'elle est définie en 2.
:::

::: verifie
Dériver h(x) = √(7 − 2x) et donner son intervalle de dérivabilité.

---

Avec u(x) = 7 − 2x, u′ = −2 et (√u)′ = u′/(2√u) : h′(x) = −2/(2√(7 − 2x)) = −1/√(7 − 2x). Il faut u(x) > 0, soit x < 7/2 : h est dérivable sur ]−∞ ; 7/2[. Oublier le facteur −2 de l'intérieur aurait donné 1/(2√(7 − 2x)), de signe contraire.
:::

::: retenir
(g ∘ f)′ = g′(f) × f′ : on dérive l'extérieur en gardant l'intérieur, puis on multiplie par la dérivée de l'intérieur ; (fⁿ)′ = n f′ fⁿ⁻¹ et (√f)′ = f′/(2√f) en sont les cas particuliers.
:::

## 🔄 Dérivée d'une fonction réciproque

La demande d'un article est q = D(p) = 400 − 5p² unités, pour un prix p compris entre 0 et 8 dinars. Le vendeur veut l'inverse : quel prix fixer pour écouler q unités, et à quelle vitesse ce prix doit-il changer quand q varie ?
Peut-on dériver cette fonction « prix en fonction de la quantité » sans la calculer ?

::: definition
Si f est continue et strictement monotone sur un intervalle I, elle réalise une bijection de I sur f(I). Sa **fonction réciproque** f⁻¹ associe à tout y de f(I) l'unique x de I tel que f(x) = y.
:::

::: exemple La pente du prix en q = 220
1. D est continue et strictement décroissante sur [0 ; 8] : c'est une bijection de [0 ; 8] sur [80 ; 400], car D(8) = 80 et D(0) = 400.
2. L'antécédent de 220 : 400 − 5p² = 220 donne p² = 36, donc p = 6 (p est positif).
3. D′(p) = −10p, donc D′(6) = −60, non nul.
4. (D⁻¹)′(220) = 1/D′(6) = −1/60 ≈ −0,017 : pour une unité de plus à vendre, le prix doit baisser d'environ 0,017 dinar.

:::

::: piege Évaluer la dérivée au mauvais point
On calcule 1/D′(220) = 1/(−2200). Cela tente parce que la formule dit « 1 sur la dérivée » et que l'on cherche une dérivée en 220. Mais D′ se calcule à l'**antécédent** : (D⁻¹)′(220) = 1/D′(6) = −1/60, car 220 est une quantité, pas un prix : D n'est même pas définie en 220.
:::

::: propriete
Soit f continue et strictement monotone sur un intervalle ouvert I, dérivable en x₀ de I avec f′(x₀) ≠ 0. Alors f⁻¹ est dérivable en y₀ = f(x₀) et :

$$ (f⁻¹)′(y₀) = 1/f′(x₀) $$

Cas limite : si f′(x₀) = 0, la tangente en x₀ est horizontale et la courbe de f⁻¹, symétrique, a une tangente verticale : f⁻¹ n'est pas dérivable en f(x₀). Pour D en p = 0, D′(0) = 0 : le prix n'est pas dérivable en q = 400.
:::

::: verifie
La fonction g(x) = x⁵ + x est une bijection de ℝ sur ℝ. Calculer (g⁻¹)′(2).

---

On cherche l'antécédent de 2 : g(1) = 1 + 1 = 2, donc x₀ = 1. Puis g′(x) = 5x⁴ + 1, donc g′(1) = 6, non nul. Alors (g⁻¹)′(2) = 1/g′(1) = 1/6. On a bien évalué g′ en 1, l'antécédent, et non en 2.
:::

::: retenir
Si f′(x₀) ≠ 0, (f⁻¹)′(f(x₀)) = 1/f′(x₀) : on cherche l'antécédent de y, on dérive en ce point, puis on prend l'inverse ; si f′(x₀) = 0, f⁻¹ n'est pas dérivable en f(x₀).
:::

## 📈 Signe de la dérivée, variations et extremums

Une menuiserie vend x centaines de chaises par mois ; son bénéfice mensuel, en milliers de dinars, est B(x) = −x³ + 9x² − 15x − 10 pour x entre 0 et 6. À partir de combien de chaises le bénéfice monte-t-il, et pour quelle production est-il maximal ?
Le signe de B′ va répondre.

::: exemple Les variations du bénéfice B
1. B est un polynôme, donc dérivable sur [0 ; 6], et B′(x) = −3x² + 18x − 15 = −3(x − 1)(x − 5).
2. B′ est un trinôme de coefficient dominant −3 < 0, de racines 1 et 5 : il est négatif sur [0 ; 1[, positif sur ]1 ; 5[ et négatif sur ]5 ; 6].
3. On en déduit les variations, avec B(0) = −10, B(1) = −17, B(5) = 15 et B(6) = 8 :

| Intervalle | Signe de B′ | Variations de B |
| --- | --- | --- |
| [0 ; 1] | négatif | décroît de −10 à −17 |
| [1 ; 5] | positif | croît de −17 à 15 |
| [5 ; 6] | négatif | décroît de 15 à 8 |

4. Le bénéfice maximal est 15 milliers de dinars, atteint pour x = 5, soit 500 chaises.

:::

::: exemple Le coût moyen minimal de la briqueterie
1. On a vu CM′(x) = (2x² − 98)/x² = 2(x − 7)(x + 7)/x² sur ]0 ; +∞[.
2. Pour x > 0, x + 7 > 0 et x² > 0 : CM′ a le signe de x − 7, négatif avant 7 et positif après.
3. CM décroît puis croît : son minimum est CM(7) = 14 + 30 + 14 = 58 dinars par millier.
4. Le coût marginal en 7 vaut C′(7) = 4 × 7 + 30 = 58 : au minimum du coût moyen, coût marginal et coût moyen sont égaux.

:::

::: piege Croire que f′(x₀) = 0 donne toujours un extremum
Pour f(x) = x³, on a f′(0) = 0 et l'on conclut « il y a un minimum en 0 ». Cela tente parce que, pour B, les extremums sont aux points où B′ s'annule. Mais f′(x) = 3x² reste positive de part et d'autre de 0 : f est croissante sur ℝ et n'a aucun extremum. Il faut que f′ **change de signe**.
:::

::: propriete
Soit f dérivable sur un intervalle I.
- f est croissante sur I si et seulement si f′ ≥ 0 sur I ; décroissante si et seulement si f′ ≤ 0 ; constante si et seulement si f′ = 0.
- Si f admet un extremum relatif en un point x₀ intérieur à I, alors f′(x₀) = 0. Si f′ s'annule en x₀ en changeant de signe, f(x₀) est un extremum relatif.
- Application : la recette de x unités vendues au prix unitaire p est R(x) = px et le bénéfice est B(x) = R(x) − C(x) = px − C(x), donc B′(x) = p − C′(x) : le bénéfice est maximal là où le coût marginal vaut le prix.

Cas limite : un extremum atteint à une borne de l'intervalle n'annule pas forcément f′ : B décroît juste après 0, donc B(0) = −10 est un maximum relatif, alors que B′(0) = −15 ≠ 0.
:::

::: verifie
Le bénéfice d'un fabricant est B(x) = −x³ + 6x² + 15x pour x dans [0 ; 8]. Pour quelle valeur de x est-il maximal, et que vaut ce maximum ?

---

B′(x) = −3x² + 12x + 15 = −3(x − 5)(x + 1). Sur [0 ; 8], x + 1 > 0, donc B′ a le signe de −3(x − 5) : positif avant 5, négatif après. B croît jusqu'à x = 5, puis décroît : le maximum est B(5) = −125 + 150 + 75 = 100. On vérifie les bords : B(0) = 0 et B(8) = −512 + 384 + 120 = −8, tous deux plus petits.
:::

::: retenir
Le signe de f′ donne le sens de variation, et un extremum se trouve où f′ s'annule en changeant de signe ; pour un bénéfice B = px − C, le maximum est où C′(x) = p, et le coût moyen est minimal là où il égale le coût marginal.
:::

## 🌀 Dérivée seconde et point d'inflexion

Reprenons le bénéfice B(x) = −x³ + 9x² − 15x − 10 : sa pente B′(x) mesure la vitesse à laquelle le bénéfice progresse, et cette vitesse n'est pas constante. Elle est faible près de x = 1, grande au milieu, faible de nouveau près de 5.
À quelle production le bénéfice progresse-t-il le plus vite ?

::: definition
Si f′ est dérivable sur I, f est **deux fois dérivable** sur I et la **dérivée seconde** f″ est la dérivée de f′. Un **point d'inflexion** de la courbe de f est un point où la tangente traverse la courbe.
:::

::: figure Au point d'inflexion I(3 ; −1), la tangente de pente 12 traverse la courbe de B
<svg viewBox="0 0 340 270"><title>Courbe de B sur [0 ; 6] et, au point d'inflexion I(3 ; −1), tangente de pente 12 qui traverse la courbe</title><polyline points="40.0,180.5 44.1,187.8 48.2,194.3 52.3,200.0 56.3,205.1 60.4,209.4 64.5,213.1 68.6,216.1 72.7,218.4 76.8,220.2 80.9,221.4 84.9,222.0 89.0,222.1 93.1,221.7 97.2,220.8 101.3,219.4 105.4,217.5 109.5,215.3 113.5,212.6 117.6,209.5 121.7,206.1 125.8,202.4 129.9,198.3 134.0,193.9 138.1,189.3 142.1,184.4 146.2,179.3 150.3,174.0 154.4,168.5 158.5,162.9 162.6,157.1 166.7,151.2 170.7,145.3 174.8,139.2 178.9,133.1 183.0,127.0 187.1,120.9 191.2,114.8 195.3,108.7 199.3,102.8 203.4,96.9 207.5,91.1 211.6,85.5 215.7,80.0 219.8,74.7 223.9,69.6 227.9,64.7 232.0,60.1 236.1,55.7 240.2,51.6 244.3,47.9 248.4,44.5 252.5,41.4 256.5,38.7 260.6,36.5 264.7,34.6 268.8,33.2 272.9,32.3 277.0,31.9 281.1,32.0 285.1,32.6 289.2,33.8 293.3,35.6 297.4,37.9 301.5,40.9 305.6,44.6 309.7,48.9 313.7,54.0 317.8,59.7 321.9,66.2 326.0,73.5" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="111.5" y1="234.1" x2="254.5" y2="19.9" stroke="#b45309" stroke-width="2.2"/><circle cx="183.0" cy="127.0" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="193.0" y="119.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I</text><text x="209.2" y="195.4" text-anchor="start" font-size="10" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente en I : y = 12x − 37</text><text x="54.3" y="226.9" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><line x1="34" y1="121.1" x2="336" y2="121.1" stroke="#0f172a" stroke-width="1.6"/><line x1="40.0" y1="246" x2="40.0" y2="6" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,121.1 329,117.6 329,124.6" fill="#0f172a"/><polygon points="40.0,6 36.5,13 43.5,13" fill="#0f172a"/><text x="332.0" y="114.1" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="48.0" y="18.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="87.7" y1="118.1" x2="87.7" y2="124.1" stroke="#0f172a" stroke-width="1.3"/><text x="87.7" y="136.1" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="183.0" y1="118.1" x2="183.0" y2="124.1" stroke="#0f172a" stroke-width="1.3"/><text x="183.0" y="136.1" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="278.3" y1="118.1" x2="278.3" y2="124.1" stroke="#0f172a" stroke-width="1.3"/><text x="278.3" y="136.1" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="37.0" y1="180.5" x2="43.0" y2="180.5" stroke="#0f172a" stroke-width="1.3"/><text x="34.0" y="184.5" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−10</text><line x1="37.0" y1="61.6" x2="43.0" y2="61.6" stroke="#0f172a" stroke-width="1.3"/><text x="34.0" y="65.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text></svg>
:::

Avant I, la courbe passe au-dessus de la tangente, après I, elle passe en dessous : la tangente la traverse. La pente 12 est la plus grande pente de toute la courbe, ce que l'exemple démontre.

::: exemple L'inflexion du bénéfice B
1. B′(x) = −3x² + 18x − 15 et B″(x) = −6x + 18 : B est un polynôme, donc deux fois dérivable.
2. B″(x) = 0 si et seulement si x = 3 ; B″ > 0 sur [0 ; 3[ (B′ croît) et B″ < 0 sur ]3 ; 6] (B′ décroît).
3. B″ s'annule en 3 en changeant de signe : I(3 ; −1) est un point d'inflexion, car B(3) = −27 + 81 − 45 − 10 = −1. La pente est maximale en 3 : B′(3) = 12, le bénéfice progresse le plus vite autour de 300 chaises.
4. La tangente en I est y = 12(x − 3) − 1 = 12x − 37 et B(x) − (12x − 37) = −(x − 3)³ change de signe en 3 : elle traverse bien la courbe.

:::

::: piege Croire que f″(x₀) = 0 suffit
Pour f(x) = x⁴, on a f″(x) = 12x², donc f″(0) = 0, et l'on conclut « point d'inflexion en O ». Cela tente parce que, pour B, l'inflexion est là où B″ s'annule. Mais f″(x) = 12x² reste positive de part et d'autre de 0 : la tangente en O, l'axe des abscisses, laisse la courbe au-dessus d'elle des deux côtés. Il faut que f″ **change de signe**.
:::

::: propriete
- Théorème (admis) : si f est deux fois dérivable sur un intervalle ouvert I contenant x₀ et que f″ s'annule en x₀ en changeant de signe, alors M₀(x₀ ; f(x₀)) est un point d'inflexion de la courbe.
- Si f″ > 0 sur I, la pente f′ croît ; si f″ < 0, elle décroît.
- Application : le coût marginal est Cm = C′, donc Cm′ = C″ : il est minimal là où C″ s'annule en passant du négatif au positif, point d'inflexion de la courbe du coût total.

Cas limite : f″(x₀) = 0 sans changement de signe ne donne aucun point d'inflexion (x⁴ en 0).
:::

::: verifie
Le coût total d'une usine est C(x) = x³ − 12x² + 50x milliers de dinars pour x tonnes. Pour quelle quantité le coût marginal est-il minimal, et que vaut ce minimum ?

---

Cm(x) = C′(x) = 3x² − 24x + 50, donc Cm′(x) = C″(x) = 6x − 24 : négatif avant 4, positif après. Le coût marginal est minimal en x = 4, avec Cm(4) = 48 − 96 + 50 = 2. Comme C″ change de signe en 4, la courbe de C a un point d'inflexion en I(4 ; 72), car C(4) = 64 − 192 + 200 = 72.
:::

::: retenir
f″ est la dérivée de f′ : un point d'inflexion apparaît là où f″ s'annule en changeant de signe, pas quand f″ s'annule seulement ; le coût marginal est minimal à l'inflexion de la courbe du coût total.
:::

## ⚖️ Théorème et inégalités des accroissements finis

Une usine passe d'un coût de 0 à un coût de 8 milliers de dinars quand sa production monte de 0 à 200 pièces : le coût a donc crû de 4 milliers par centaine de pièces en moyenne. Dans notre modèle simplifié, C(x) = x³ pour x en centaines de pièces.
Existe-t-il un niveau de production où le coût marginal vaut exactement cette moyenne de 4 ?

::: figure La corde (AB) de pente 4 et la tangente parallèle en P : une pente instantanée égale à la pente moyenne
<svg viewBox="0 0 340 250"><title>Courbe de x ↦ x³ sur [0 ; 2], corde (AB) de pente 4 et tangente parallèle en P d'abscisse environ 1,155</title><polyline points="40.0,185.7 43.6,185.7 47.2,185.7 50.8,185.7 54.4,185.6 58.0,185.6 61.6,185.6 65.2,185.5 68.8,185.4 72.4,185.3 76.0,185.1 79.5,185.0 83.1,184.7 86.7,184.5 90.3,184.2 93.9,183.9 97.5,183.5 101.1,183.0 104.7,182.6 108.3,182.0 111.9,181.4 115.5,180.7 119.1,180.0 122.7,179.2 126.3,178.3 129.9,177.3 133.5,176.3 137.1,175.2 140.7,174.0 144.3,172.7 147.9,171.3 151.5,169.8 155.1,168.2 158.6,166.5 162.2,164.7 165.8,162.8 169.4,160.8 173.0,158.7 176.6,156.4 180.2,154.1 183.8,151.6 187.4,148.9 191.0,146.2 194.6,143.3 198.2,140.3 201.8,137.1 205.4,133.8 209.0,130.3 212.6,126.7 216.2,123.0 219.8,119.1 223.4,115.0 227.0,110.7 230.6,106.3 234.2,101.8 237.7,97.0 241.3,92.1 244.9,87.0 248.5,81.7 252.1,76.2 255.7,70.6 259.3,64.7 262.9,58.7 266.5,52.4 270.1,46.0 273.7,39.3 277.3,32.5 280.9,25.4 284.5,18.1 288.1,10.6 291.7,2.9" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="40.0" y1="185.7" x2="268.8" y2="48.3" stroke="#64748b" stroke-width="1.8" stroke-dasharray="6 4"/><line x1="120.1" y1="190.5" x2="268.8" y2="101.2" stroke="#b45309" stroke-width="2.4"/><line x1="268.8" y1="48.3" x2="268.8" y2="185.7" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><line x1="172.1" y1="159.2" x2="172.1" y2="185.7" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><circle cx="40.0" cy="185.7" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="50.0" y="178.7" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><circle cx="268.8" cy="48.3" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="259.8" y="45.3" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><circle cx="172.1" cy="159.2" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="166.1" y="149.2" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">P</text><text x="91.5" y="72.4" text-anchor="start" font-size="11" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">corde (AB) : pente 4</text><text x="91.5" y="93.0" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente en P : pente 4</text><line x1="34" y1="185.7" x2="336" y2="185.7" stroke="#0f172a" stroke-width="1.6"/><line x1="40.0" y1="226" x2="40.0" y2="6" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,185.7 329,182.2 329,189.2" fill="#0f172a"/><polygon points="40.0,6 36.5,13 43.5,13" fill="#0f172a"/><text x="332.0" y="178.7" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="48.0" y="18.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="154.4" y1="182.7" x2="154.4" y2="188.7" stroke="#0f172a" stroke-width="1.3"/><text x="154.4" y="200.7" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="268.8" y1="182.7" x2="268.8" y2="188.7" stroke="#0f172a" stroke-width="1.3"/><text x="268.8" y="200.7" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="37.0" y1="117.0" x2="43.0" y2="117.0" stroke="#0f172a" stroke-width="1.3"/><text x="34.0" y="121.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="37.0" y1="48.3" x2="43.0" y2="48.3" stroke="#0f172a" stroke-width="1.3"/><text x="34.0" y="52.3" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text></svg>
:::

La corde relie A(0 ; 0) et B(2 ; 8) ; en faisant glisser une droite de pente 4 sous la courbe, on la voit toucher la courbe en un point P, où la tangente est parallèle à (AB).

::: exemple Le niveau de production c : C(x) = x³ sur [0 ; 2]
1. C est continue sur [0 ; 2] et dérivable sur ]0 ; 2[ (polynôme) : le théorème s'applique.
2. Le taux moyen vaut (C(2) − C(0))/(2 − 0) = 8/2 = 4.
3. C′(c) = 3c² = 4 donne c² = 4/3, soit c = 2/√3 ≈ 1,155 ; la solution négative est hors de ]0 ; 2[.
4. Il existe donc un niveau c ≈ 1,155, soit environ 115 pièces, où le coût marginal vaut exactement 4.

:::

::: exemple Encadrer √5 avec f(x) = √x sur [4 ; 5]
1. f est continue sur [4 ; 5] et dérivable sur ]4 ; 5[, avec f′(x) = 1/(2√x).
2. Pour 4 < x < 5, on a 2 < √x < 3, donc 1/6 < f′(x) < 1/4 : on prend m = 1/6 et M = 1/4.
3. L'inégalité donne m ≤ (f(5) − f(4))/(5 − 4) ≤ M, c'est-à-dire 1/6 ≤ √5 − 2 ≤ 1/4.
4. Donc 13/6 ≤ √5 ≤ 9/4 ; en effet √5 ≈ 2,236, entre 2,167 et 2,25.

:::

::: piege Prendre pour c le milieu de [a ; b]
Pour C(x) = x³ sur [0 ; 2], on choisit c = 1, le milieu, et l'on écrit « C′(1) = 4 ». Cela tente parce que, pour une parabole, le point cherché est bien le milieu. Mais ici C′(1) = 3 ≠ 4 : le théorème affirme qu'un c existe, pas qu'il est au milieu, ni qu'il est unique. On le trouve en résolvant C′(c) = taux moyen.
:::

::: propriete
Soit f continue sur [a ; b] et dérivable sur ]a ; b[.
- Théorème (admis) : il existe au moins un c de ]a ; b[ tel que f′(c) = (f(b) − f(a))/(b − a).
- Si m ≤ f′(x) ≤ M pour tout x de ]a ; b[, alors m ≤ (f(b) − f(a))/(b − a) ≤ M.
- Si |f′(x)| ≤ k pour tout x de l'intervalle, alors |f(b) − f(a)| ≤ k|b − a|. Par exemple, pour f(x) = 3 + 2/x sur [1 ; +∞[, |f′(x)| = 2/x² ≤ 2, donc |f(b) − f(a)| ≤ 2|b − a|.

Cas limite : la dérivabilité sur tout ]a ; b[ est nécessaire. La fonction |x| sur [−1 ; 1] a un taux moyen nul, mais |x| n'est pas dérivable en 0 et sa dérivée ne s'annule jamais.
:::

::: verifie
Avec C(x) = x³ sur [0 ; 3], existe-t-il un c de ]0 ; 3[ où C′(c) est égale au taux moyen ? Le calculer.

---

C est continue sur [0 ; 3] et dérivable sur ]0 ; 3[. Le taux moyen vaut (27 − 0)/(3 − 0) = 9. On résout 3c² = 9, donc c² = 3 et c = √3 ≈ 1,73, qui appartient bien à ]0 ; 3[ (la racine négative −√3 est exclue). Là encore c n'est pas le milieu 1,5.
:::

::: retenir
Pour f continue sur [a ; b] et dérivable sur ]a ; b[, une tangente est parallèle à la corde : f′(c) = (f(b) − f(a))/(b − a) pour un c (pas forcément le milieu) ; et m ≤ f′ ≤ M donne m ≤ taux moyen ≤ M, donc m(b − a) ≤ f(b) − f(a) ≤ M(b − a).
:::

## 🧮 Primitives

Une entreprise connaît son coût marginal, Cm(x) = 6x + 20 dinars par objet, et ses coûts fixes : 500 dinars, même sans produire. Elle veut le chemin inverse de la dérivation : retrouver le coût total C(x) dont la dérivée est Cm.
Comment remonter d'une dérivée à la fonction, et la réponse est-elle unique ?

::: definition
Soient f et F deux fonctions définies sur un intervalle I. **F est une primitive de f sur I** si F est dérivable sur I et si F′(x) = f(x) pour tout x de I.

Toute fonction continue sur un intervalle y admet une primitive (théorème admis). Si F est une primitive de f, les primitives de f sont les fonctions F + k, avec k réel constant ; et pour x₀ de I et y₀ réel donnés, une seule primitive vérifie F(x₀) = y₀ (théorème admis).
:::

::: exemple Le coût total à partir du coût marginal
1. On cherche C avec C′(x) = 6x + 20 : 3x² a pour dérivée 6x et 20x a pour dérivée 20, donc C(x) = 3x² + 20x + k.
2. Toute autre primitive diffère de celle-ci d'une constante : la constante k n'est pas fixée par Cm.
3. Les coûts fixes imposent C(0) = 500, donc k = 500 : c'est la primitive unique prenant la valeur 500 en 0.
4. C(x) = 3x² + 20x + 500. Contrôle : C′(x) = 6x + 20 ✓ ; par exemple C(10) = 300 + 200 + 500 = 1000 dinars.

:::

::: piege Oublier la constante
On répond C(x) = 3x² + 20x. Cela tente parce que cette fonction a bien pour dérivée 6x + 20 et que l'on cherche « une primitive ». Mais elle donne C(0) = 0 : ce coût ignore les 500 dinars de coûts fixes. Une primitive est définie à une constante près, et c'est la condition donnée qui la fixe.
:::

Les primitives usuelles et les formes à reconnaître se lisent dans les deux tableaux, et ils se vérifient en dérivant.

| f(x) | Une primitive F(x) | Intervalle |
| --- | --- | --- |
| c (constante) | cx | ℝ |
| x | x²/2 | ℝ |
| xⁿ (n entier, n ≥ 1 ou n ≤ −2) | xⁿ⁺¹/(n + 1) | ℝ si n ≥ 1, ]−∞ ; 0[ ou ]0 ; +∞[ si n ≤ −2 |
| 1/x² | −1/x | ]−∞ ; 0[ ou ]0 ; +∞[ |
| 1/√x | 2√x | ]0 ; +∞[ |

| Forme de f | Une primitive | Condition |
| --- | --- | --- |
| u′ | u | aucune |
| u′/u² | −1/u | u(x) ≠ 0 |
| uⁿu′ (n entier, n ≠ −1, n ≠ 0) | uⁿ⁺¹/(n + 1) | u(x) ≠ 0 si n ≤ −2 |
| u′/√u | 2√u | u(x) > 0 |

Pour F + G et αF, on a : si F et G sont des primitives de f et g, alors F + G est une primitive de f + g et αF est une primitive de αf.

::: exemple Reconnaître la forme
1. f(x) = 6x(x² + 1)³ : avec u(x) = x² + 1 et u′(x) = 2x, f = 3 × u′u³. Une primitive est F(x) = 3 × u⁴/4 = (3/4)(x² + 1)⁴ ; on compense par un facteur **constant**, ici 3.
2. g(x) = x/√(x² + 9) : avec u(x) = x² + 9 > 0 et u′ = 2x, g = (1/2) × u′/√u. Une primitive est G(x) = (1/2) × 2√u = √(x² + 9).
3. Contrôle de 1 : F′(x) = 3(x² + 1)³ × 2x = 6x(x² + 1)³ ✓.

:::

::: exemple Se ramener aux formes : f(x) = (2x² + 4x + 5)/(x + 1)² sur ]−1 ; +∞[
1. On cherche a et b avec f(x) = a + b/(x + 1)², soit a(x + 1)² + b = 2x² + 4x + 5. Comme a(x² + 2x + 1) + b = ax² + 2ax + a + b, on trouve a = 2 puis 2 + b = 5, donc b = 3.
2. f(x) = 2 + 3/(x + 1)², donc F(x) = 2x − 3/(x + 1) + k, car u′/u² = 1/(x + 1)² a pour primitive −1/u.
3. Contrôle : F′(x) = 2 + 3/(x + 1)² ✓.

:::

::: propriete
- Pour primitiver, on reconnaît une forme u′uⁿ, u′/u² ou u′/√u, ou l'on décompose en une somme de formes usuelles ; on **vérifie en dérivant**.
- Le facteur manquant est un nombre qu'on compense, jamais une expression en x.
- On primitive terme à terme une somme, mais il n'existe pas de règle simple pour un produit ni pour un quotient : on décompose d'abord, jamais numérateur et dénominateur séparément.

Cas limite : 1/x² n'est pas définie en 0, donc ses primitives −1/x + k se cherchent séparément sur ]−∞ ; 0[ et sur ]0 ; +∞[, et la constante k peut y être différente ; on travaille sur un seul intervalle à la fois.
:::

::: verifie
Le coût marginal est Cm(x) = 8x + 30 dinars par pièce et les coûts fixes valent 250 dinars. Donner le coût total C(x).

---

Une primitive de 8x + 30 est 4x² + 30x, donc C(x) = 4x² + 30x + k. Comme C(0) = 250, k = 250 et C(x) = 4x² + 30x + 250. Contrôle : C′(x) = 8x + 30 ✓ et C(10) = 400 + 300 + 250 = 950 dinars.
:::

::: retenir
F est une primitive de f si F′ = f, et elle est unique à une constante près, que fixe une condition F(x₀) = y₀ ; on reconnaît u′uⁿ, u′/u² ou u′/√u, on décompose si besoin, et on vérifie en dérivant.
:::

> 🏆 Tu maîtrises la pente et le chemin inverse : tu sais lire un coût marginal, optimiser un bénéfice et remonter jusqu'au coût total. Prochaine étape : l'étude complète de fonctions, où tout se rassemble.
