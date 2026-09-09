# 📜 Résumé : Suites géométriques

- **Définition** : (Uₙ) est **géométrique de raison q** lorsque **Uₙ₊₁ = q Uₙ** pour tout entier naturel n — on **multiplie** toujours par le même réel, on n'ajoute pas. Des termes consécutifs sont dits **en progression géométrique**. Test unique : le quotient **uₙ₊₁/uₙ** ne dépend pas de n. Un pourcentage devient un facteur : +5 % ⇒ ×1,05 ; −1 % ⇒ ×0,99.

::: figure Deux suites parties du même terme : l'une ajoute 3 à chaque pas, l'autre multiplie par 2. Elles se rejoignent encore au rang 2, puis la multiplicative décroche — la raison d'une suite géométrique multiplie, elle n'ajoute pas
<svg viewBox="0 0 240 170">
<path d="M36 20 L36 146 M28 140 L214 140" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<polyline points="40,133.13 82,122.81 124,112.5 166,102.19 208,91.88" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<polyline points="40,133.13 82,126.25 124,112.5 166,85 208,30" fill="none" stroke="#0f6e56" stroke-width="2.4"/>
<g fill="#0f172a"><circle cx="40" cy="133.13" r="3"/><circle cx="82" cy="122.81" r="3"/><circle cx="124" cy="112.5" r="3"/><circle cx="166" cy="102.19" r="3"/><circle cx="208" cy="91.88" r="3"/></g>
<g fill="#0f6e56"><circle cx="82" cy="126.25" r="3"/><circle cx="166" cy="85" r="3"/><circle cx="208" cy="30" r="3"/></g>
<g font-size="12" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="218" y="26" fill="#0f6e56">×2</text>
<text x="220" y="96" fill="#0f172a">+3</text>
<text x="40" y="156" fill="#0f172a">0</text><text x="82" y="156" fill="#0f172a">1</text><text x="124" y="156" fill="#0f172a">2</text><text x="166" y="156" fill="#0f172a">3</text><text x="208" y="156" fill="#0f172a">4</text>
</g>
</svg>
:::

- **Terme général** : **Uₙ = U₀ qⁿ** (q ≠ 0), et plus généralement **Uₙ = Uₚ qⁿ⁻ᵖ**, en particulier **Uₙ = U₁ qⁿ⁻¹**. L'exposant compte des **pas** (n − p), pas des rangs. Exemples : u₀ = 2, q = 5 ⇒ u₃ = 2 × 5³ = 250 ; u₂ = 4, q = 3 ⇒ u₆ = 4 × 3⁴ = 324. Reconnaître une suite géométrique, c'est l'écrire sous la forme u₀ qⁿ : √(7ⁿ) = (√7)ⁿ a pour raison √7.
- **Deux raisons possibles** : si le calcul donne q avec un exposant **pair**, il y a deux solutions. v₃ = 12 et v₅ = 48 donnent q² = 4, donc **q = 2 ou q = −2**.
- **Représentation graphique** : on place les points **Aₙ(n ; uₙ)**. Le point d'abscisse 0 donne **u₀** ; le quotient de deux ordonnées **consécutives** donne **q** (2 ; 6 ; 18 ; 54 ⇒ u₀ = 2 et q = 3).
- **Somme de n termes consécutifs** (q ≠ 1) : **S = a × (1 − qⁿ)/(1 − q)**, où a est le premier terme et **n le nombre de termes**. **Si q = 1, S = na.** Identité associée : **1 + q + … + qⁿ = (1 − qⁿ⁺¹)/(1 − q)**, et n + 1 si q = 1. Exemple à connaître : 1 + 2 + 4 + … + 2⁹ = 2¹⁰ − 1 = **1023** (10 termes, pas 9).
- **Moyenne géométrique** : si a, b, c sont consécutifs, **b² = ac** ; pour des termes positifs, **b = √(ac)**. Exemple : 3 ; b ; 27 ⇒ b = 9. À ne pas confondre avec la moyenne arithmétique (a + c)/2.
- **Comportement des termes** : |q| > 1 ⇒ ils grandissent sans limite ; |q| < 1 ⇒ ils se rapprochent de 0 ; q = 1 ⇒ suite constante ; **q < 0 ⇒ les signes alternent**. Décroître n'implique pas une raison négative (16 ; 8 ; 4 a pour raison 1/2). Un **rang seuil** se cherche par puissances successives à la calculatrice : 0,9⁶ = 0,531… et 0,9⁷ = 0,478… ⇒ 7 étapes pour passer sous la moitié.
- **Applications** : loyer de 200 dinars à +5 % par an (200 ; 210 ; 220,50 ; …) ; intérêts composés — 8000 dinars donnent 8320 à 4 % par an, mais 8323,20 à 2 % par semestre ; pression atmosphérique à −1 % par 100 m ; aires de carrés emboîtés (divisées par 2 à chaque étape).
- **Enrichissement** : les grains de blé de l'échiquier totalisent **2⁶⁴ − 1** ; un **nombre parfait** s'écrit N = 2ⁿ(2ⁿ⁺¹ − 1) avec 2ⁿ⁺¹ − 1 premier (**nombre de Mersenne**), d'où 6, 28, 496, 8128 ; si uₙ₊₁ = uₙ + 3, alors vₙ = 2^uₙ est géométrique de raison 2³ = 8.
