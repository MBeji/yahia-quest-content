# 🧪 Variation du pH au cours d'une réaction acide-base — lire une courbe de dosage

> 💡 «Une courbe de dosage est le portrait d'une réaction : son saut dit où elle s'achève, son pH dit de quoi la solution est faite.»

Un détartrant du commerce contient de l'acide chlorhydrique, un déboucheur de la soude : comment connaître leur concentration exacte sans rien deviner ? On verse une solution de concentration connue dans la solution à doser et l'on suit le pH. Huit notions permettent de lire cette courbe : le caractère total de la réaction, le dosage d'un acide fort par une base forte, le repérage de l'équivalence, le dosage d'un acide faible, celui d'une base faible, le calcul d'une concentration, le choix d'un indicateur coloré et la solution tampon. On suppose acquis le pH et Kₑ (chapitre 8), Kₐ et pKₐ (chapitre 7), le tableau d'avancement et τ_f (chapitre 1).

## 🔗 Une réaction acide-base est pratiquement totale

On verse 10,0 mL de soude à 2,0·10⁻² mol·L⁻¹ dans 25,0 mL d'acide éthanoïque CH₃CO₂H à 2,0·10⁻² mol·L⁻¹ : le pH-mètre affiche 4,57.
La soude a-t-elle réagi en totalité, et peut-on s'appuyer sur cette réaction pour doser ?

::: definition
**Réaction de dosage** — Réaction entre l'espèce dosée et l'espèce versée. Pour l'acide éthanoïque et la soude, CH₃CO₂H + OH⁻ → CH₃CO₂⁻ + H₂O (les ions Na⁺, inertes, sont omis). Sa constante est K = [CH₃CO₂⁻]/([CH₃CO₂H]·[OH⁻]) = Kₐ/Kₑ.
Une réaction est pratiquement totale si son taux d'avancement final τ_f est voisin de 1 ; dans ce chapitre, K > 10⁴ suffit pour la déclarer totale.
:::

Le tableau d'avancement relie les quantités au pH mesuré (quantités en mol, H₂O en excès) :

| état | CH₃CO₂H | OH⁻ | CH₃CO₂⁻ |
| --- | --- | --- | --- |
| initial | 5,0·10⁻⁴ | 2,0·10⁻⁴ | 0 |
| final | 5,0·10⁻⁴ − x_f | 2,0·10⁻⁴ − x_f | x_f |

::: exemple Montrer que la réaction est pratiquement totale

1. Le pH de 4,57 donne [H₃O⁺] = 10^(−4,57) = 2,7·10⁻⁵ mol·L⁻¹, donc [OH⁻] = Kₑ/[H₃O⁺] = 10⁻¹⁴/2,7·10⁻⁵ = 3,7·10⁻¹⁰ mol·L⁻¹, car le produit ionique relie les deux concentrations.
2. Le volume du mélange est 25,0 + 10,0 = 35,0 mL : la quantité finale d'ions OH⁻ vaut 3,7·10⁻¹⁰ × 35,0·10⁻³ = 1,3·10⁻¹¹ mol, car n = [OH⁻]·V.
3. Les ions OH⁻ sont le réactif limitant : x_max = 2,0·10⁻⁴ mol, et x_f = 2,0·10⁻⁴ − 1,3·10⁻¹¹ ≈ 2,0·10⁻⁴ mol, car il reste à peine quelques 10⁻¹¹ mol d'OH⁻.
4. Alors τ_f = x_f/x_max ≈ 1 : la réaction est pratiquement totale. La constante le confirme : K = Kₐ/Kₑ = 10^(−4,75)/10⁻¹⁴ = 10^(9,25) = 1,8·10⁹, très supérieure à 10⁴.

:::

::: piege
**Erreur : croire qu'une réaction totale fait disparaître les deux réactifs.** On lit « totale » et l'on pense qu'il ne reste plus d'acide dans le mélange. L'erreur tente parce que le mot suggère « tout » ; mais seul le réactif limitant disparaît : ici, il reste 5,0·10⁻⁴ − 2,0·10⁻⁴ = 3,0·10⁻⁴ mol d'acide éthanoïque, et c'est ce reste qui fixe le pH à 4,57.
:::

::: propriete
**Les trois réactions de dosage** — Acide fort + base forte : H₃O⁺ + OH⁻ → 2 H₂O, K = 1/Kₑ = 10¹⁴. Acide faible + base forte : K = Kₐ/Kₑ = 10^(14 − pKₐ). Base faible + acide fort : K = 1/Kₐ = 10^(pKₐ). Dans chaque cas K dépasse 10⁴ : la réaction est pratiquement totale et convient à un dosage.
Cas : pour NH₃ + H₃O⁺ → NH₄⁺ + H₂O, pKₐ = 9,25 donne K = 10^(9,25) = 1,8·10⁹.
Cas limite : une réaction dont K serait inférieure à 10⁴ ne consommerait pas tout le réactif limitant et ne conviendrait pas au dosage.
:::

::: verifie À toi : la réaction de dosage de l'ammoniac
L'acide chlorhydrique dose l'ammoniac selon NH₃ + H₃O⁺ → NH₄⁺ + H₂O, avec pKₐ(NH₄⁺/NH₃) = 9,25. Quelle est la constante K, et la réaction est-elle utilisable pour un dosage ?

---

La réaction est l'inverse de l'acidité de NH₄⁺ : K = 1/Kₐ = 10^(pKₐ) = 10^(9,25) = 1,8·10⁹. Cette valeur dépasse 10⁴ : la réaction est pratiquement totale et utilisable.
:::

::: retenir
Les réactions de dosage ont K > 10⁴ (K = 10¹⁴, Kₐ/Kₑ ou 1/Kₐ) : le réactif limitant disparaît (τ_f ≈ 1), l'autre réactif subsiste en partie.
:::

## 📈 Un acide fort dosé par une base forte : saut de pH et équivalence

On dose 20,0 mL d'acide chlorhydrique à 5,0·10⁻² mol·L⁻¹ avec de la soude à 4,0·10⁻² mol·L⁻¹ versée à la burette, un pH-mètre étalonné plongé dans le bécher.
Quel volume de soude faut-il verser pour neutraliser tout l'acide, et que fait le pH en chemin ?

::: definition
**Équivalence acido-basique** — État du mélange où l'acide et la base sont en proportions stœchiométriques. Pour un monoacide et une monobase, n_A = n_B, soit C_A·V_A = C_B·V_E, où V_E est le volume de base versé à l'équivalence.
Pour HCl et NaOH, la réaction est H₃O⁺ + OH⁻ → 2 H₂O. Sur la courbe pH = f(V_B), le **saut de pH** est la variation brusque autour de V_E ; le point d'équivalence E a pour coordonnées (V_E ; pH_E).
:::

::: figure Dosage de 20,0 mL de HCl à 5,0·10⁻² mol·L⁻¹ par NaOH à 4,0·10⁻² mol·L⁻¹ (allure calculée) : le saut de pH est centré sur E (25,0 mL ; 7)
<svg viewBox="0 0 340 236"><title>Dosage d'un acide fort par une base forte : pH en fonction du volume de base versé</title><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/>
<line x1="54" y1="190" x2="54" y2="16" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="336,190 328,186 328,194" fill="#0f172a"/>
<polygon points="54,12 50,20 58,20" fill="#0f172a"/>
<line x1="54" y1="190" x2="54" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="54" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text>
<line x1="122" y1="190" x2="122" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="122" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text>
<line x1="190" y1="190" x2="190" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="190" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text>
<line x1="224" y1="190" x2="224" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="224" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">25</text>
<line x1="258" y1="190" x2="258" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="258" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text>
<line x1="326" y1="190" x2="326" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="326" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text>
<line x1="50" y1="190" x2="54" y2="190" stroke="#0f172a" stroke-width="1.2"/>
<text x="46" y="194" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text>
<line x1="50" y1="106" x2="54" y2="106" stroke="#0f172a" stroke-width="1.2"/>
<text x="46" y="110" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7</text>
<line x1="50" y1="22" x2="54" y2="22" stroke="#0f172a" stroke-width="1.2"/>
<text x="46" y="26" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">14</text>
<text x="326" y="221" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">V_B (mL)</text>
<text x="60" y="10" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pH</text>
<line x1="54" y1="106" x2="224" y2="106" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5 4"/><line x1="224" y1="190" x2="224" y2="106" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5 4"/>
<polyline points="54,174.39 56,174.25 58,174.11 60,173.98 62,173.84 64,173.7 66,173.57 68,173.43 70,173.29 72,173.16 74,173.02 76,172.88 78,172.75 80,172.61 82,172.47 84,172.34 86,172.2 88,172.06 90,171.92 92,171.79 94,171.65 96,171.51 98,171.37 100,171.22 102,171.08 104,170.94 106,170.8 108,170.65 110,170.51 112,170.36 114,170.21 116,170.07 118,169.92 120,169.76 122,169.61 124,169.46 126,169.3 128,169.15 130,168.99 132,168.83 134,168.66 136,168.5 138,168.33 140,168.16 142,167.99 144,167.81 146,167.63 148,167.45 150,167.27 152,167.08 154,166.89 156,166.7 158,166.5 160,166.29 162,166.08 164,165.87 166,165.65 168,165.43 170,165.2 172,164.96 174,164.71 176,164.46 178,164.2 180,163.93 182,163.64 184,163.35 186,163.04 188,162.72 190,162.39 192,162.03 194,161.66 196,161.26 198,160.84 200,160.38 202,159.89 204,159.36 206,158.78 208,158.13 210,157.39 212,156.55 213.8,155.68 214,155.57 214.65,155.21 215.5,154.7 216,154.37 216.35,154.13 217.2,153.5 218,152.84 218.05,152.79 218.9,151.97 219.75,151.01 220,150.69 220.6,149.83 221.45,148.32 222,147.04 222.3,146.19 222.64,145.02 222.75,144.57 222.87,144.07 222.98,143.52 223.09,142.9 223.15,142.56 223.21,142.2 223.32,141.4 223.43,140.44 223.55,139.28 223.66,137.78 223.77,135.66 223.89,132.06 224,106 224.11,79.94 224.23,76.35 224.34,74.23 224.45,72.73 224.57,71.58 224.68,70.63 224.79,69.82 224.85,69.47 224.91,69.13 225.02,68.52 225.13,67.97 225.25,67.48 225.36,67.02 225.7,65.87 226,65.03 226.55,63.77 227.4,62.28 228,61.45 228.25,61.14 229.1,60.2 229.95,59.41 230,59.37 230.8,58.73 231.65,58.13 232,57.9 232.5,57.59 233.35,57.11 234,56.77 234.2,56.67 236,55.85 238,55.08 240,54.42 242,53.84 244,53.32 246,52.86 248,52.43 250,52.05 252,51.69 254,51.37 256,51.06 258,50.78 260,50.51 262,50.26 264,50.02 266,49.8 268,49.58 270,49.38 272,49.19 274,49.01 276,48.83 278,48.66 280,48.5 282,48.35 284,48.2 286,48.06 288,47.92 290,47.79 292,47.66 294,47.54 296,47.42 298,47.3 300,47.19 302,47.08 304,46.98 306,46.88 308,46.78 310,46.68 312,46.59 314,46.5 316,46.41 318,46.32 320,46.24 322,46.16 324,46.08" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round"/>
<circle cx="224" cy="106" r="5" fill="#d97706" stroke="#ffffff" stroke-width="1.2"/><text x="234" y="122" text-anchor="start" font-size="13" font-weight="700" fill="#d97706" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><text x="178" y="100" text-anchor="end" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pH = 7</text></svg>
:::

Avant V_E, le réactif limitant est OH⁻ : il reste de l'acide et le pH reste bas, en montant lentement. Après V_E, le réactif limitant est H₃O⁺ : l'excès de soude impose un pH élevé. Au point E de la figure, V_E se lit en abscisse et pH_E en ordonnée.

::: exemple Calculer V_E et dire ce que contient le bécher

1. À l'équivalence, n_A = n_B, donc C_A·V_A = C_B·V_E, d'où V_E = C_A·V_A/C_B = 5,0·10⁻² × 20,0/4,0·10⁻² = 25,0 mL.
2. Pour V_B = 10,0 mL (avant V_E), la base ajoutée est entièrement consommée : OH⁻ est limitant, il reste de l'acide, le mélange est acide.
3. Pour V_B = 30,0 mL (après V_E), tout l'acide est consommé : H₃O⁺ est limitant, il reste de la soude, le mélange est basique.
4. À V_E, rien ne reste de H₃O⁺ ni de OH⁻ en excès : tout se passe comme si l'on avait dissous du chlorure de sodium dans l'eau. Les ions Na⁺ et Cl⁻ sont inertes, la solution est neutre : pH_E = 7 à 25 °C.

:::

::: piege
**Erreur : écrire C_A·V_A = C_B·V_B pour un volume de base quelconque.** À V_B = 10,0 mL, on calcule C_A = 4,0·10⁻² × 10,0/20,0 = 2,0·10⁻² mol·L⁻¹ au lieu de 5,0·10⁻² mol·L⁻¹. L'erreur tente parce que la relation est encadrée dans le cours ; mais elle exprime n_A = n_B, vraie seulement à l'équivalence : avant V_E, la base versée n'a consommé qu'une partie de l'acide.
:::

::: propriete
**Acide fort et base forte** — À l'équivalence, C_A·V_A = C_B·V_E et le pH vaut 7 à 25 °C. Le mélange est acide avant V_E et basique après. Le saut de pH est d'autant plus grand que les concentrations sont grandes.
Cas : avec des concentrations dix fois plus petites, le volume V_E ne change pas pour un même rapport C_A/C_B ; le saut est plus petit, et pH_E reste égal à 7.
:::

::: verifie À toi : une concentration inconnue
On dose 10,0 mL d'acide chlorhydrique de concentration inconnue par de la soude à 2,0·10⁻² mol·L⁻¹ ; l'équivalence est atteinte pour V_E = 15,0 mL. Quelle est la concentration C_A ?

---

À l'équivalence C_A·V_A = C_B·V_E, donc C_A = C_B·V_E/V_A = 2,0·10⁻² × 15,0/10,0 = 3,0·10⁻² mol·L⁻¹. Le volume V_E est celui lu à l'équivalence, et non un volume versé quelconque.
:::

::: retenir
Acide fort + base forte : C_A·V_A = C_B·V_E à l'équivalence seulement, pH_E = 7 à 25 °C, mélange acide avant V_E et basique après.
:::

## 🎯 Repérer l'équivalence : tangentes parallèles et courbe dérivée

Autour de E, la courbe est presque verticale : poser le point « à l'œil » donne un pH_E qui varie d'une personne à l'autre.
Comment obtenir les coordonnées de E de façon reproductible ?

::: definition
**Point d'inflexion** — Point d'une courbe où la concavité change de sens. Sur une courbe de dosage, c'est le point I du saut de pH, voisin du point d'équivalence E.
**Méthode des tangentes parallèles** : on trace la tangente en un point A de la partie basse de la courbe, puis la tangente parallèle en un point B de la partie haute ; on trace une droite sécante qui coupe ces deux tangentes en M et N ; la parallèle aux tangentes passant par le milieu de [MN] recoupe la courbe en I.
**Méthode de la courbe dérivée** : au point d'inflexion, la dérivée dpH/dV passe par un extremum ; un logiciel trace cette courbe et l'abscisse de l'extremum donne V_E.
:::

::: figure Tangentes parallèles en A et B (bleu), sécante verticale qui les coupe en M et N, parallèle (orange) passant par le milieu de [MN] : elle recoupe la courbe en I
<svg viewBox="0 0 340 236"><title>Méthode des tangentes parallèles appliquée à la courbe d'un dosage acide fort / base forte</title><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/>
<line x1="54" y1="190" x2="54" y2="16" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="336,190 328,186 328,194" fill="#0f172a"/>
<polygon points="54,12 50,20 58,20" fill="#0f172a"/>
<line x1="54" y1="190" x2="54" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="54" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text>
<line x1="122" y1="190" x2="122" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="122" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text>
<line x1="190" y1="190" x2="190" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="190" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text>
<line x1="224" y1="190" x2="224" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="224" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">25</text>
<line x1="258" y1="190" x2="258" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="258" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text>
<line x1="326" y1="190" x2="326" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="326" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text>
<line x1="50" y1="190" x2="54" y2="190" stroke="#0f172a" stroke-width="1.2"/>
<text x="46" y="194" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text>
<line x1="50" y1="106" x2="54" y2="106" stroke="#0f172a" stroke-width="1.2"/>
<text x="46" y="110" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7</text>
<line x1="50" y1="22" x2="54" y2="22" stroke="#0f172a" stroke-width="1.2"/>
<text x="46" y="26" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">14</text>
<text x="326" y="221" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">V_B (mL)</text>
<text x="60" y="10" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pH</text>
<polyline points="54,174.39 56,174.25 58,174.11 60,173.98 62,173.84 64,173.7 66,173.57 68,173.43 70,173.29 72,173.16 74,173.02 76,172.88 78,172.75 80,172.61 82,172.47 84,172.34 86,172.2 88,172.06 90,171.92 92,171.79 94,171.65 96,171.51 98,171.37 100,171.22 102,171.08 104,170.94 106,170.8 108,170.65 110,170.51 112,170.36 114,170.21 116,170.07 118,169.92 120,169.76 122,169.61 124,169.46 126,169.3 128,169.15 130,168.99 132,168.83 134,168.66 136,168.5 138,168.33 140,168.16 142,167.99 144,167.81 146,167.63 148,167.45 150,167.27 152,167.08 154,166.89 156,166.7 158,166.5 160,166.29 162,166.08 164,165.87 166,165.65 168,165.43 170,165.2 172,164.96 174,164.71 176,164.46 178,164.2 180,163.93 182,163.64 184,163.35 186,163.04 188,162.72 190,162.39 192,162.03 194,161.66 196,161.26 198,160.84 200,160.38 202,159.89 204,159.36 206,158.78 208,158.13 210,157.39 212,156.55 213.8,155.68 214,155.57 214.65,155.21 215.5,154.7 216,154.37 216.35,154.13 217.2,153.5 218,152.84 218.05,152.79 218.9,151.97 219.75,151.01 220,150.69 220.6,149.83 221.45,148.32 222,147.04 222.3,146.19 222.64,145.02 222.75,144.57 222.87,144.07 222.98,143.52 223.09,142.9 223.15,142.56 223.21,142.2 223.32,141.4 223.43,140.44 223.55,139.28 223.66,137.78 223.77,135.66 223.89,132.06 224,106 224.11,79.94 224.23,76.35 224.34,74.23 224.45,72.73 224.57,71.58 224.68,70.63 224.79,69.82 224.85,69.47 224.91,69.13 225.02,68.52 225.13,67.97 225.25,67.48 225.36,67.02 225.7,65.87 226,65.03 226.55,63.77 227.4,62.28 228,61.45 228.25,61.14 229.1,60.2 229.95,59.41 230,59.37 230.8,58.73 231.65,58.13 232,57.9 232.5,57.59 233.35,57.11 234,56.77 234.2,56.67 236,55.85 238,55.08 240,54.42 242,53.84 244,53.32 246,52.86 248,52.43 250,52.05 252,51.69 254,51.37 256,51.06 258,50.78 260,50.51 262,50.26 264,50.02 266,49.8 268,49.58 270,49.38 272,49.19 274,49.01 276,48.83 278,48.66 280,48.5 282,48.35 284,48.2 286,48.06 288,47.92 290,47.79 292,47.66 294,47.54 296,47.42 298,47.3 300,47.19 302,47.08 304,46.98 306,46.88 308,46.78 310,46.68 312,46.59 314,46.5 316,46.41 318,46.32 320,46.24 322,46.16 324,46.08" fill="none" stroke="#0f6e56" stroke-width="2.2" stroke-linejoin="round"/>
<line x1="81.2" y1="173.04" x2="312.4" y2="153.87" stroke="#2563eb" stroke-width="1.4"/>
<line x1="122" y1="61.6" x2="326" y2="44.68" stroke="#2563eb" stroke-width="1.4"/>
<line x1="224" y1="28" x2="224" y2="190" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5 4"/>
<line x1="164" y1="112.14" x2="284" y2="102.2" stroke="#d97706" stroke-width="1.6" stroke-dasharray="6 3"/>
<circle cx="135.6" cy="168.53" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/><text x="125.6" y="160.53" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><circle cx="277.51" cy="48.7" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/><text x="287.51" y="62.7" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><circle cx="224" cy="161.2" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/><text x="233" y="153.2" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><circle cx="224" cy="53.14" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/><text x="235" y="47.14" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N</text><circle cx="224" cy="107.17" r="3.6" fill="#d97706" stroke="#ffffff" stroke-width="1.2"/><text x="212" y="123.17" text-anchor="middle" font-size="12" font-weight="700" fill="#d97706" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I</text></svg>
:::

Les tangentes en A et B sont parallèles, le segment [MN] est coupé en son milieu, et I se trouve au milieu du saut de pH : ses coordonnées sont celles de E.

::: exemple Appliquer la méthode sur la courbe de la notion précédente

1. On choisit A à V_B = 12,0 mL, sur la partie basse, et on trace la tangente en A : elle est presque horizontale.
2. On cherche B sur la partie haute, vers 33 mL, où la tangente a la même pente : les deux tangentes sont parallèles, car la construction n'est valable qu'avec des parallèles.
3. La sécante verticale V_B = 25 mL coupe les tangentes en M (pH voisin de 2,4) et N (pH voisin de 11,4) : le milieu de [MN] a pour ordonnée (2,4 + 11,4)/2 = 6,9.
4. La parallèle passant par ce milieu recoupe la courbe en I, de coordonnées voisines de (25,0 ; 7) : on lit V_E = 25,0 mL et pH_E ≈ 7, ce que le calcul C_A·V_A/C_B = 25,0 mL confirme.

:::

::: piege
**Erreur : tracer des tangentes non parallèles.** On trace la tangente en A, puis une droite quelconque touchant la partie haute de la courbe. L'erreur tente parce qu'une tangente se trace facilement partout ; mais le milieu de [MN] n'a de sens que si les deux tangentes sont parallèles : sinon la parallèle menée par ce milieu coupe la courbe loin de E.
:::

::: propriete
**Deux méthodes approchées** — La méthode des tangentes parallèles et celle de la courbe dérivée donnent des valeurs approchées de V_E et de pH_E. Sur la courbe dérivée, V_E est l'abscisse de l'extremum de dpH/dV, maximum si le pH croît et minimum si le pH décroît.
Cas : sur une courbe dont le pH décroît, la dérivée est négative et V_E se lit à son minimum.
:::

::: verifie À toi : lire V_E sur la dérivée
Pour un dosage de 20,0 mL d'acide chlorhydrique par de la soude à 0,10 mol·L⁻¹, la courbe dérivée dpH/dV présente un maximum à 18,4 mL. Quelle est la concentration de l'acide ?

---

Le maximum de la dérivée donne V_E = 18,4 mL. À l'équivalence, C_A·V_A = C_B·V_E, donc C_A = 0,10 × 18,4/20,0 = 9,2·10⁻² mol·L⁻¹.
:::

::: retenir
V_E et pH_E se repèrent par deux tangentes parallèles (milieu de [MN]) ou par l'extremum de la courbe dérivée dpH/dV ; ces valeurs sont approchées.
:::

## 🧪 Un acide faible dosé par une base forte : pH = pKₐ à la demi-équivalence

Même burette, même soude à 4,0·10⁻² mol·L⁻¹, mais 20,0 mL d'acide éthanoïque à 5,0·10⁻² mol·L⁻¹ à la place de l'acide chlorhydrique.
Le pH à l'équivalence est-il encore 7 ? Et que peut-on lire d'autre sur la courbe ?

::: definition
**Dosage d'un acide faible par une base forte** — La réaction CH₃CO₂H + OH⁻ → CH₃CO₂⁻ + H₂O est pratiquement totale, et V_E = C_A·V_A/C_B. La **demi-équivalence** est l'état obtenu pour V_B = V_E/2 : la moitié de l'acide a été transformée, donc [CH₃CO₂⁻] = [CH₃CO₂H].
Avec Kₐ = [CH₃CO₂⁻][H₃O⁺]/[CH₃CO₂H], cette égalité donne [H₃O⁺] = Kₐ, soit pH = pKₐ.
:::

::: figure Dosage de 20,0 mL d'acide éthanoïque à 5,0·10⁻² mol·L⁻¹ par NaOH à 4,0·10⁻² mol·L⁻¹ (allure calculée) : S est la demi-équivalence, E l'équivalence
<svg viewBox="0 0 340 236"><title>Dosage d'un acide faible par une base forte : demi-équivalence S et équivalence E</title><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/>
<line x1="54" y1="190" x2="54" y2="16" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="336,190 328,186 328,194" fill="#0f172a"/>
<polygon points="54,12 50,20 58,20" fill="#0f172a"/>
<line x1="54" y1="190" x2="54" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="54" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text>
<line x1="122" y1="190" x2="122" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="122" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text>
<line x1="190" y1="190" x2="190" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="190" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text>
<line x1="258" y1="190" x2="258" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="258" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text>
<line x1="326" y1="190" x2="326" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="326" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text>
<line x1="50" y1="190" x2="54" y2="190" stroke="#0f172a" stroke-width="1.2"/>
<text x="46" y="194" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text>
<line x1="50" y1="106" x2="54" y2="106" stroke="#0f172a" stroke-width="1.2"/>
<text x="46" y="110" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7</text>
<line x1="50" y1="22" x2="54" y2="22" stroke="#0f172a" stroke-width="1.2"/>
<text x="46" y="26" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">14</text>
<text x="326" y="221" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">V_B (mL)</text>
<text x="60" y="10" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pH</text><line x1="54" y1="133" x2="139" y2="133" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5 4"/><line x1="139" y1="190" x2="139" y2="133" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5 4"/><line x1="54" y1="87.42" x2="224" y2="87.42" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5 4"/><line x1="224" y1="190" x2="224" y2="87.42" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5 4"/><line x1="54" y1="106" x2="326" y2="106" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="2 3"/><polyline points="54,153.64 56,151.98 58,150.45 60,149.11 62,147.95 64,146.95 66,146.07 68,145.28 70,144.58 72,143.94 74,143.35 76,142.81 78,142.3 80,141.83 82,141.38 84,140.96 86,140.55 88,140.17 90,139.8 92,139.44 94,139.1 96,138.77 98,138.45 100,138.13 102,137.83 104,137.53 106,137.24 108,136.96 110,136.68 112,136.41 114,136.14 116,135.87 118,135.61 120,135.35 122,135.1 124,134.84 126,134.59 128,134.34 130,134.09 132,133.85 134,133.6 136,133.36 138,133.11 140,132.87 142,132.62 144,132.38 146,132.13 148,131.88 150,131.63 152,131.38 154,131.13 156,130.88 158,130.62 160,130.36 162,130.1 164,129.83 166,129.56 168,129.29 170,129.01 172,128.72 174,128.43 176,128.13 178,127.83 180,127.51 182,127.19 184,126.85 186,126.5 188,126.14 190,125.77 192,125.38 194,124.97 196,124.53 198,124.07 200,123.59 202,123.06 204,122.49 206,121.88 208,121.19 210,120.43 212,119.56 213.8,118.66 214,118.55 214.65,118.17 215.5,117.65 216,117.32 216.35,117.07 217.2,116.43 218,115.76 218.05,115.71 218.9,114.88 219.75,113.9 220,113.58 220.6,112.71 221.45,111.19 222,109.91 222.3,109.05 222.64,107.88 222.75,107.42 222.87,106.92 222.98,106.37 223.09,105.75 223.15,105.41 223.21,105.06 223.32,104.25 223.43,103.3 223.55,102.14 223.66,100.65 223.77,98.57 223.89,95.17 224,87.42 224.11,79.67 224.23,76.28 224.34,74.2 224.45,72.71 224.57,71.56 224.68,70.62 224.79,69.82 224.85,69.46 224.91,69.13 225.02,68.51 225.13,67.97 225.25,67.47 225.36,67.02 225.7,65.87 226,65.02 226.55,63.77 227.4,62.28 228,61.45 228.25,61.13 229.1,60.2 229.95,59.41 230,59.37 230.8,58.73 231.65,58.13 232,57.9 232.5,57.59 233.35,57.11 234,56.77 234.2,56.67 236,55.85 238,55.08 240,54.42 242,53.84 244,53.32 246,52.86 248,52.43 250,52.05 252,51.69 254,51.37 256,51.06 258,50.78 260,50.51 262,50.26 264,50.02 266,49.8 268,49.58 270,49.38 272,49.19 274,49.01 276,48.83 278,48.66 280,48.5 282,48.35 284,48.2 286,48.06 288,47.92 290,47.79 292,47.66 294,47.54 296,47.42 298,47.3 300,47.19 302,47.08 304,46.98 306,46.88 308,46.78 310,46.68 312,46.59 314,46.5 316,46.41 318,46.32 320,46.24 322,46.16 324,46.08" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round"/>
<circle cx="139" cy="133" r="5" fill="#2563eb" stroke="#ffffff" stroke-width="1.2"/><circle cx="224" cy="87.42" r="5" fill="#d97706" stroke="#ffffff" stroke-width="1.2"/><text x="147" y="149" text-anchor="start" font-size="13" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S</text><text x="233" y="101.42" text-anchor="start" font-size="13" font-weight="700" fill="#d97706" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><text x="62" y="127" text-anchor="start" font-size="10" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4,75</text><text x="62" y="81.42" text-anchor="start" font-size="10" font-weight="700" fill="#d97706" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8,55</text><text x="139" y="206" text-anchor="middle" font-size="1" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"></text></svg>
:::

Le point S (12,5 mL ; 4,75) donne le pKₐ du couple, le point E (25,0 mL ; 8,55) donne pH_E : la courbe monte lentement, passe par une zone presque plate autour de S, puis saute à E.

::: exemple Exploiter la courbe de l'acide éthanoïque

1. V_E = C_A·V_A/C_B = 5,0·10⁻² × 20,0/4,0·10⁻² = 25,0 mL, et V_E/2 = 12,5 mL.
2. À 12,5 mL, [CH₃CO₂⁻] = [CH₃CO₂H] : Kₐ = [H₃O⁺] et pH = pKₐ = 4,75, valeur lue en S.
3. À l'équivalence, on a dissous 5,0·10⁻² × 20,0 = 1,0 mmol d'éthanoate de sodium dans 45,0 mL : C_E = 1,0/45,0 = 2,2·10⁻² mol·L⁻¹. Na⁺ est inerte, CH₃CO₂⁻ est une base faible : CH₃CO₂⁻ + H₂O ⇄ CH₃CO₂H + OH⁻ produit des ions OH⁻, donc pH_E > 7.
4. Pour une base faible faiblement ionisée, pH_E = ½ (pKₑ + pKₐ + log C_E) = ½ (14 + 4,75 − 1,65) = 8,55, car log (2,2·10⁻²) = −1,65 : la valeur calculée rejoint celle de la courbe.

:::

::: piege
**Erreur : lire le pKₐ à l'équivalence.** On repère E sur la courbe et l'on écrit pKₐ = 8,55. L'erreur tente parce que E est le point remarquable de la courbe ; mais à V_E il ne reste plus d'acide, la solution est celle de la base faible CH₃CO₂⁻ : le pKₐ se lit à la demi-équivalence, là où [acide] = [base], soit 4,75.
:::

::: propriete
**Acide faible et base forte** — À l'équivalence, le pH est supérieur à 7 à 25 °C (le sel contient une base faible) : pH_E = ½ (pKₑ + pKₐ + log C_E), avec C_E = C_A·V_A/(V_A + V_E). À la demi-équivalence, pH = pKₐ.
Cas : à même C_E, un acide de pKₐ plus grand (plus faible) donne un pH_E plus élevé.
:::

::: verifie À toi : la demi-équivalence de l'acide nitreux
On dose 25,0 mL d'acide nitreux HNO₂ (pKₐ = 3,3) à 4,0·10⁻² mol·L⁻¹ par de la soude à 5,0·10⁻² mol·L⁻¹. Quel est le pH du mélange après versement de 10,0 mL de soude ?

---

V_E = C_A·V_A/C_B = 4,0·10⁻² × 25,0/5,0·10⁻² = 20,0 mL. Le volume versé, 10,0 mL, est V_E/2 : on est à la demi-équivalence, [acide] = [base] et pH = pKₐ = 3,3.
:::

::: retenir
Acide faible + base forte : pH_E > 7 à 25 °C ; pH = pKₐ à V_E/2 (là où [acide] = [base]) et non à V_E.
:::

## 🧴 Une base faible dosée par un acide fort : la courbe descend

Un produit ménager contient de l'ammoniac NH₃. On en dose 25,0 mL à 4,0·10⁻² mol·L⁻¹ avec de l'acide chlorhydrique à 5,0·10⁻² mol·L⁻¹.
Le pH part haut et descend : où est l'équivalence, et vaut-il encore 7 ?

::: definition
**Dosage d'une base faible par un acide fort** — La réaction NH₃ + H₃O⁺ → NH₄⁺ + H₂O est pratiquement totale (K = 1/Kₐ = 1,8·10⁹), et V_E = C_B·V_B/C_A, où V_B est le volume de base dosée et V_A le volume d'acide versé. À la demi-équivalence, V_A = V_E/2 : [NH₃] = [NH₄⁺], donc pH = pKₐ(NH₄⁺/NH₃) = 9,25.
:::

::: figure Dosage de 25,0 mL d'ammoniac à 4,0·10⁻² mol·L⁻¹ par HCl à 5,0·10⁻² mol·L⁻¹ (allure calculée) : S est la demi-équivalence, E l'équivalence
<svg viewBox="0 0 340 236"><title>Dosage d'une base faible par un acide fort : demi-équivalence S et équivalence E</title><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/>
<line x1="54" y1="190" x2="54" y2="16" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="336,190 328,186 328,194" fill="#0f172a"/>
<polygon points="54,12 50,20 58,20" fill="#0f172a"/>
<line x1="54" y1="190" x2="54" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="54" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text>
<line x1="99.33" y1="190" x2="99.33" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="99.33" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text>
<line x1="144.67" y1="190" x2="144.67" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="144.67" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text>
<line x1="190" y1="190" x2="190" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="190" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">15</text>
<line x1="235.33" y1="190" x2="235.33" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="235.33" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text>
<line x1="280.67" y1="190" x2="280.67" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="280.67" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">25</text>
<line x1="326" y1="190" x2="326" y2="194" stroke="#0f172a" stroke-width="1.2"/>
<text x="326" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text>
<line x1="50" y1="190" x2="54" y2="190" stroke="#0f172a" stroke-width="1.2"/>
<text x="46" y="194" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text>
<line x1="50" y1="106" x2="54" y2="106" stroke="#0f172a" stroke-width="1.2"/>
<text x="46" y="110" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7</text>
<line x1="50" y1="22" x2="54" y2="22" stroke="#0f172a" stroke-width="1.2"/>
<text x="46" y="26" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">14</text>
<text x="326" y="221" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">V_A (mL)</text>
<text x="60" y="10" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pH</text><line x1="54" y1="79" x2="144.67" y2="79" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5 4"/><line x1="144.67" y1="190" x2="144.67" y2="79" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5 4"/><line x1="54" y1="124.58" x2="235.33" y2="124.58" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5 4"/><line x1="235.33" y1="190" x2="235.33" y2="124.58" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5 4"/><line x1="54" y1="106" x2="326" y2="106" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="2 3"/><polyline points="54,58.94 56,60.34 58,61.66 60,62.86 62,63.92 64,64.86 66,65.69 68,66.44 70,67.12 72,67.74 74,68.32 76,68.85 78,69.34 80,69.81 82,70.24 84,70.66 86,71.06 88,71.43 90,71.79 92,72.14 94,72.48 96,72.8 98,73.11 100,73.42 102,73.72 104,74 106,74.29 108,74.56 110,74.83 112,75.1 114,75.36 116,75.61 118,75.86 120,76.11 122,76.36 124,76.6 126,76.84 128,77.08 130,77.32 132,77.55 134,77.78 136,78.02 138,78.25 140,78.48 142,78.71 144,78.94 146,79.17 148,79.4 150,79.63 152,79.86 154,80.09 156,80.32 158,80.55 160,80.79 162,81.03 164,81.27 166,81.51 168,81.75 170,82 172,82.25 174,82.51 176,82.76 178,83.03 180,83.3 182,83.57 184,83.85 186,84.14 188,84.43 190,84.73 192,85.04 194,85.36 196,85.7 198,86.04 200,86.4 202,86.77 204,87.17 206,87.58 208,88.02 210,88.48 212,88.97 214,89.51 216,90.08 218,90.72 220,91.42 221.73,92.1 222,92.21 222.87,92.59 224,93.12 225.13,93.7 226,94.19 226.27,94.35 227.4,95.08 228,95.51 228.53,95.92 229.67,96.9 230,97.23 230.8,98.1 231.93,99.63 232,99.74 233.07,101.77 233.52,102.95 233.67,103.41 233.82,103.91 233.97,104.46 234,104.56 234.12,105.08 234.2,105.42 234.28,105.78 234.43,106.59 234.58,107.54 234.73,108.7 234.88,110.19 235.03,112.29 235.18,115.76 235.33,124.58 235.48,133.4 235.64,136.86 235.79,138.95 235.94,140.44 236,140.95 236.09,141.59 236.24,142.54 236.39,143.34 236.47,143.7 236.54,144.03 236.69,144.65 236.84,145.19 237,145.69 237.15,146.14 237.6,147.3 238,148.14 238.73,149.39 239.87,150.88 240,151.03 241,152.03 242,152.86 242.13,152.96 243.27,153.75 244,154.2 244.4,154.43 245.53,155.03 246,155.26 246.67,155.57 247.8,156.05 248,156.13 248.93,156.49 250,156.87 252,157.51 254,158.08 256,158.59 258,159.04 260,159.46 262,159.84 264,160.19 266,160.52 268,160.83 270,161.11 272,161.38 274,161.64 276,161.88 278,162.1 280,162.32 282,162.52 284,162.72 286,162.91 288,163.09 290,163.26 292,163.42 294,163.58 296,163.73 298,163.88 300,164.02 302,164.16 304,164.29 306,164.42 308,164.54 310,164.66 312,164.78 314,164.89 316,165 318,165.11 320,165.21 322,165.31 324,165.41 326,165.5" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round"/>
<circle cx="144.67" cy="79" r="5" fill="#2563eb" stroke="#ffffff" stroke-width="1.2"/><circle cx="235.33" cy="124.58" r="5" fill="#d97706" stroke="#ffffff" stroke-width="1.2"/><text x="153.67" y="71" text-anchor="start" font-size="13" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S</text><text x="244.33" y="116.58" text-anchor="start" font-size="13" font-weight="700" fill="#d97706" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><text x="62" y="73" text-anchor="start" font-size="10" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">9,25</text><text x="62" y="118.58" text-anchor="start" font-size="10" font-weight="700" fill="#d97706" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5,45</text></svg>
:::

Le point S (10,0 mL ; 9,25) donne le pKₐ du couple NH₄⁺/NH₃, le point E (20,0 mL ; 5,45) donne pH_E : l'équivalence est ici dans la partie acide de l'échelle.

::: exemple Exploiter la courbe de l'ammoniac

1. V_E = C_B·V_B/C_A = 4,0·10⁻² × 25,0/5,0·10⁻² = 20,0 mL, et V_E/2 = 10,0 mL.
2. À 10,0 mL, [NH₃] = [NH₄⁺] et pH = pKₐ = 9,25, valeur lue en S.
3. À l'équivalence, on a dissous 4,0·10⁻² × 25,0 = 1,0 mmol de chlorure d'ammonium dans 45,0 mL : C_E = 2,2·10⁻² mol·L⁻¹. Cl⁻ est inerte, NH₄⁺ est un acide faible : NH₄⁺ + H₂O ⇄ NH₃ + H₃O⁺ produit des ions H₃O⁺, donc pH_E < 7.
4. Pour un acide faible faiblement ionisé, pH_E = ½ (pKₐ − log C_E) = ½ (9,25 + 1,65) = 5,45 : la valeur calculée rejoint celle de la courbe.

:::

::: piege
**Erreur : appliquer à la base faible la règle de l'acide faible.** On retient « à l'équivalence, le pH est supérieur à 7 » et l'on prévoit pH_E > 7 pour l'ammoniac. L'erreur tente parce que le mot « faible » est le même ; mais le sel formé contient ici un acide faible, NH₄⁺, et non une base faible : le pH_E est inférieur à 7, soit 5,45.
:::

::: propriete
**Base faible et acide fort** — À l'équivalence, le pH est inférieur à 7 à 25 °C (le sel contient un acide faible) : pH_E = ½ (pKₐ − log C_E), avec C_E = C_B·V_B/(V_B + V_E). À la demi-équivalence, pH = pKₐ du couple acide/base : c'est le pKₐ de l'acide conjugué de la base dosée, non son pK_b.
Cas : la courbe décroît, donc la dérivée dpH/dV est négative.
:::

::: verifie À toi : la triméthylamine
On dose 20,0 mL de triméthylamine (CH₃)₃N à 0,10 mol·L⁻¹ par de l'acide chlorhydrique à 0,10 mol·L⁻¹ ; pKₐ((CH₃)₃NH⁺/(CH₃)₃N) = 9,8. Quel est le pH après versement de 10,0 mL d'acide, et la solution à l'équivalence est-elle acide ou basique ?

---

V_E = 0,10 × 20,0/0,10 = 20,0 mL : 10,0 mL est V_E/2, donc pH = pKₐ = 9,8. À l'équivalence, la solution contient l'acide faible (CH₃)₃NH⁺ et l'ion inerte Cl⁻ : elle est acide, pH_E < 7.
:::

::: retenir
Base faible + acide fort : pH_E < 7 à 25 °C ; pH = pKₐ (de l'acide conjugué) à V_E/2.
:::

## 🧮 De V_E à la concentration : dosage, dilution et concentration massique

La bouteille d'un vinaigre indique un degré, mais on veut le vérifier. Ce vinaigre est trop concentré pour être dosé tel quel : on le dilue 50 fois.
Comment remonter du volume équivalent à la teneur du vinaigre d'origine ?

::: definition
**Dosage et concentrations** — La solution de concentration connue est versée à la burette (le manuel la nomme « solution titrée ») ; l'autre est la solution dosée. À l'équivalence, C_A·V_A = C_B·V_E.
Quand la solution dosée a été diluée F fois, C₀ = F·C_dil, car la dilution conserve la quantité de matière. La concentration massique est C_m = C·M. Le **degré acétique** d'un vinaigre est la masse d'acide éthanoïque, en g, contenue dans 100 mL de vinaigre.
:::

::: exemple Le degré d'un vinaigre

On dilue le vinaigre 50 fois ; 20,0 mL de la solution diluée sont dosés par de la soude à 5,0·10⁻² mol·L⁻¹ ; V_E = 12,0 mL ; M(CH₃CO₂H) = 60 g·mol⁻¹.

1. C_dil = C_B·V_E/V_A = 5,0·10⁻² × 12,0/20,0 = 3,0·10⁻² mol·L⁻¹, car C_A·V_A = C_B·V_E.
2. C₀ = 50 × 3,0·10⁻² = 1,5 mol·L⁻¹, car la solution diluée contient la même quantité d'acide dans un volume 50 fois plus grand.
3. C_m = C₀·M = 1,5 × 60 = 90 g·L⁻¹, car la concentration massique est la concentration molaire multipliée par la masse molaire.
4. Dans 100 mL de vinaigre, il y a 90 × 0,100 = 9,0 g d'acide : le vinaigre est à 9,0°.

:::

::: piege
**Erreur : oublier le facteur de dilution.** On s'arrête à C_dil = 3,0·10⁻² mol·L⁻¹ et l'on annonce 3,0·10⁻² × 60 = 1,8 g·L⁻¹, soit 0,18°. L'erreur tente parce que le calcul du dosage donne déjà « une concentration » ; mais elle est celle de la solution diluée : il faut la multiplier par 50 pour retrouver le vinaigre d'origine.
:::

::: propriete
**Ce que la dilution change et ne change pas** — Ajouter de l'eau dans le bécher avant le dosage ne modifie pas la quantité de matière à doser : V_E reste le même. Pour un acide faible dosé par une base forte (ou une base faible par un acide fort), le pH à la demi-équivalence reste égal au pKₐ, tandis que le pH initial et le pH à l'équivalence changent. Pour un acide fort dosé par une base forte, pH_E reste égal à 7 ; seuls le pH initial et la hauteur du saut changent.
Cas : pour un acide faible dosé par une base forte, la dilution du bécher fait monter le pH initial et baisser pH_E.
:::

::: verifie À toi : un détartrant dilué
Un détartrant à l'acide chlorhydrique est dilué 10 fois. On dose 10,0 mL de la solution diluée par de la soude à 0,10 mol·L⁻¹ : V_E = 12,5 mL. Quelle est la concentration du détartrant d'origine ?

---

C_dil = C_B·V_E/V_A = 0,10 × 12,5/10,0 = 0,125 mol·L⁻¹ ; le détartrant d'origine, 10 fois plus concentré, a pour concentration C₀ = 10 × 0,125 = 1,25 mol·L⁻¹.
:::

::: retenir
C_A·V_A = C_B·V_E donne la concentration de la solution dosée ; multiplier par le facteur de dilution pour l'échantillon d'origine, puis par M pour la concentration massique.
:::

## 🌈 L'indicateur coloré : choisir celui dont la zone de virage contient pH_E

Sans pH-mètre, on repère l'équivalence par un changement de couleur : quelques gouttes d'indicateur suffisent.
Mais un indicateur qui convient pour doser de l'acide chlorhydrique convient-il pour doser l'acide éthanoïque ?

::: definition
**Indicateur coloré de pH** — Acide faible dont la teinte diffère de celle de sa base conjuguée ; on l'emploie en petite quantité. Sa **zone de virage** est l'intervalle de pH où les deux formes coexistent ; la **teinte sensible** est la teinte prise dans cette zone. Un indicateur est dit **convenable** pour un dosage si sa zone de virage contient le pH à l'équivalence.
:::

| indicateur | zone de virage | forme acide | forme basique |
| --- | --- | --- | --- |
| bleu de bromophénol | 3,0 à 4,6 | jaune | bleu |
| rouge Congo | 3,0 à 5,0 | bleu | rouge |
| hélianthine | 3,1 à 4,4 | rouge | jaune |
| rouge d'éthyle | 4,0 à 5,8 | incolore | rouge |
| rouge de méthyle | 4,8 à 6,0 | rouge | jaune |
| rouge de phénol | 6,0 à 6,8 | jaune | rouge |
| bleu de bromothymol | 6,0 à 7,6 | jaune | bleu |
| rouge de crésol | 7,0 à 8,8 | jaune | rouge |
| phénolphtaléine | 8,2 à 10,0 | incolore | violet |

::: figure Zones de virage de quatre indicateurs ; les trois droites verticales marquent le pH à l'équivalence des dosages de HCl (7), de l'acide éthanoïque (8,55) et de l'ammoniac (5,45)
<svg viewBox="0 0 340 230"><title>Zones de virage de quatre indicateurs colorés et pH à l'équivalence de trois dosages</title><line x1="197.75" y1="32" x2="197.75" y2="190" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="5 3"/><line x1="221" y1="32" x2="221" y2="190" stroke="#2563eb" stroke-width="1.6" stroke-dasharray="5 3"/><line x1="244.25" y1="32" x2="244.25" y2="190" stroke="#d97706" stroke-width="1.6" stroke-dasharray="5 3"/><text x="8" y="57" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">hélianthine</text><rect x="162.5" y="44" width="19.5" height="18" fill="#7c3aed" fill-opacity="0.3" stroke="#0f172a" stroke-width="1.4"/><text x="8" y="91" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">rouge de méthyle</text><rect x="188" y="78" width="18" height="18" fill="#7c3aed" fill-opacity="0.3" stroke="#0f172a" stroke-width="1.4"/><text x="8" y="125" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">bleu de bromothymol</text><rect x="206" y="112" width="24" height="18" fill="#7c3aed" fill-opacity="0.3" stroke="#0f172a" stroke-width="1.4"/><text x="8" y="159" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">phénolphtaléine</text><rect x="239" y="146" width="27" height="18" fill="#7c3aed" fill-opacity="0.3" stroke="#0f172a" stroke-width="1.4"/><line x1="116" y1="190" x2="330" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="116" y1="190" x2="116" y2="194" stroke="#0f172a" stroke-width="1.2"/><text x="116" y="207" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="146" y1="190" x2="146" y2="194" stroke="#0f172a" stroke-width="1.2"/><text x="146" y="207" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="176" y1="190" x2="176" y2="194" stroke="#0f172a" stroke-width="1.2"/><text x="176" y="207" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="206" y1="190" x2="206" y2="194" stroke="#0f172a" stroke-width="1.2"/><text x="206" y="207" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="236" y1="190" x2="236" y2="194" stroke="#0f172a" stroke-width="1.2"/><text x="236" y="207" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="266" y1="190" x2="266" y2="194" stroke="#0f172a" stroke-width="1.2"/><text x="266" y="207" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="296" y1="190" x2="296" y2="194" stroke="#0f172a" stroke-width="1.2"/><text x="296" y="207" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12</text><line x1="326" y1="190" x2="326" y2="194" stroke="#0f172a" stroke-width="1.2"/><text x="326" y="207" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">14</text><text x="326" y="222" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pH</text><circle cx="197.75" cy="190" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1.2"/><circle cx="221" cy="190" r="4" fill="#2563eb" stroke="#ffffff" stroke-width="1.2"/><circle cx="244.25" cy="190" r="4" fill="#d97706" stroke="#ffffff" stroke-width="1.2"/><text x="193.75" y="28" text-anchor="end" font-size="10" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5,45</text><text x="221" y="28" text-anchor="middle" font-size="10" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7</text><text x="248.25" y="28" text-anchor="start" font-size="10" font-weight="700" fill="#d97706" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8,55</text></svg>
:::

Chaque droite verticale ne traverse qu'une zone de virage : le rouge de méthyle pour 5,45, le bleu de bromothymol pour 7, la phénolphtaléine pour 8,55.

::: exemple Choisir l'indicateur du dosage de l'acide éthanoïque

1. Pour le dosage de l'acide éthanoïque par la soude, pH_E = 8,55 (notion précédente) : on cherche la zone de virage qui contient 8,55.
2. L'hélianthine (3,1 à 4,4) et le rouge de méthyle (4,8 à 6,0) ont fini de virer bien avant l'équivalence : ils sont éliminés.
3. Le bleu de bromothymol (6,0 à 7,6) a une zone qui se termine sous pH_E : il vire un peu avant l'équivalence et ne convient pas.
4. La phénolphtaléine (8,2 à 10,0) a une zone qui contient 8,55 : elle est convenable, et la teinte passe de l'incolore au rose-violet à l'équivalence.

:::

::: piege
**Erreur : prendre le bleu de bromothymol pour tous les dosages.** On le choisit parce que sa zone de virage est autour de 7, « le pH neutre ». L'erreur tente parce que 7 semble le pH naturel d'une équivalence ; mais pH_E = 7 seulement pour un acide fort et une base forte : pour l'acide éthanoïque (8,55) ou l'ammoniac (5,45), la zone du bleu de bromothymol ne contient pas pH_E.
:::

::: propriete
**Choix d'un indicateur** — L'indicateur convenable est celui dont la zone de virage contient pH_E ; on le choisit donc après avoir prévu pH_E (7 pour acide fort/base forte, supérieur à 7 pour acide faible/base forte, inférieur à 7 pour base faible/acide fort).
Cas : pour pH_E = 7, le bleu de bromothymol (6,0 à 7,6) convient.
:::

::: verifie À toi : l'indicateur du dosage de l'ammoniac
Pour le dosage de l'ammoniac par l'acide chlorhydrique (pH_E = 5,45), quel indicateur du tableau convient parmi l'hélianthine, le rouge de méthyle, le bleu de bromothymol et la phénolphtaléine ?

---

Il faut une zone de virage qui contient 5,45. L'hélianthine (3,1 à 4,4) vire trop tôt, le bleu de bromothymol (6,0 à 7,6) et la phénolphtaléine (8,2 à 10,0) sont au-dessus de 5,45 ; le rouge de méthyle (4,8 à 6,0) contient 5,45 : il est convenable.
:::

::: retenir
Un indicateur est convenable si sa zone de virage contient pH_E ; on prévoit pH_E (7, supérieur à 7 ou inférieur à 7) avant de choisir.
:::

## 🛡️ La solution tampon : un pH qui résiste

Pour étalonner un pH-mètre, on le plonge dans une solution dont le pH reste stable même si l'on y verse un peu d'acide ou de base.
Comment un mélange peut-il résister à ces ajouts ?

::: definition
**Solution tampon** — Mélange d'un acide faible et de sa base conjuguée en quantités du même ordre, dont le pH varie très peu par ajout modéré d'acide ou de base, et par dilution modérée.
Son pH vaut pH = pKₐ + log ([base]/[acide]) ; si [base] = [acide], pH = pKₐ.
On obtient un tampon : en mélangeant l'acide faible et sa base conjuguée ; ou en ajoutant une base forte à un acide faible jusqu'au voisinage de la demi-équivalence ; ou en ajoutant un acide fort à une base faible jusqu'au voisinage de la demi-équivalence.
:::

La zone presque plate de chaque courbe, autour de S dans les deux figures de dosage, est justement le domaine où le mélange se comporte en tampon.

::: exemple Préparer un tampon et tester l'ajout de soude

On mélange 40,0 mL d'acide éthanoïque à 0,10 mol·L⁻¹ et 60,0 mL d'éthanoate de sodium à 0,10 mol·L⁻¹ (pKₐ = 4,75).

1. Les quantités sont n(acide) = 4,0·10⁻³ mol et n(base) = 6,0·10⁻³ mol : elles sont du même ordre, le mélange est un tampon.
2. Le volume est commun, donc [base]/[acide] = n(base)/n(acide) = 1,5 et pH = 4,75 + log 1,5 = 4,75 + 0,176 = 4,926, soit 4,93.
3. On ajoute 1,0 mL de soude à 0,10 mol·L⁻¹, soit 1,0·10⁻⁴ mol d'ions OH⁻ : ils consomment l'acide, n(acide) = 3,9·10⁻³ mol et n(base) = 6,1·10⁻³ mol, donc pH = 4,75 + log (6,1/3,9) = 4,75 + 0,194 = 4,944 : le pH a varié de 0,02 environ.
4. La même quantité de OH⁻ dans 101 mL d'eau pure donnerait [OH⁻] = 1,0·10⁻⁴/0,101 = 9,9·10⁻⁴ mol·L⁻¹, soit pH = 11,0 : l'eau pure varie de 4 unités, le tampon de 0,02 environ.

:::

::: piege
**Erreur : croire que le pH d'un tampon est égal au pKₐ quelles que soient les quantités.** On annonce pH = 4,75 pour le mélange précédent. L'erreur tente parce que pH = pKₐ est la relation retenue à la demi-équivalence ; mais elle suppose [base] = [acide] : ici le rapport vaut 1,5 et le pH est 4,93.
:::

::: propriete
**Tampon** — pH = pKₐ + log ([base]/[acide]) ; le pH est voisin du pKₐ quand les deux formes ont des concentrations proches, et égal au pKₐ si elles sont égales. Les trois modes de préparation mènent au même mélange acide faible/base conjuguée.
Cas : le mélange de 20,0 mL d'ammoniac et de 10,0 mL d'acide chlorhydrique de même concentration est à la demi-équivalence : pH = pKₐ(NH₄⁺/NH₃).
:::

::: verifie À toi : un tampon à l'ammoniac
On mélange 20,0 mL d'ammoniac à 0,10 mol·L⁻¹ et 10,0 mL d'acide chlorhydrique à 0,10 mol·L⁻¹ (pKₐ(NH₄⁺/NH₃) = 9,25). Ce mélange est-il un tampon, et quel est son pH ?

---

HCl consomme 1,0·10⁻³ mol de NH₃ sur 2,0·10⁻³ mol : il reste 1,0·10⁻³ mol de NH₃ et il se forme 1,0·10⁻³ mol de NH₄⁺. Les deux formes sont en quantités égales : c'est un tampon, à la demi-équivalence, et pH = pKₐ = 9,25.
:::

::: retenir
Tampon = acide faible + base conjuguée en quantités du même ordre ; pH = pKₐ + log ([base]/[acide]), égal à pKₐ si les quantités sont égales.
:::

> 🏆 Tu sais désormais lire une courbe de dosage : le saut donne V_E et donc la concentration, la demi-équivalence donne le pKₐ, le pH à l'équivalence guide le choix de l'indicateur, et le mélange acide faible/base conjuguée explique l'effet tampon.
