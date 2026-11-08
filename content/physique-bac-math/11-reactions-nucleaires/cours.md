# ☢️ Réactions nucléaires — quand le noyau se transforme

> 💡 «Un noyau instable se défait tout seul, un noyau lourd ou léger peut être forcé à se transformer : à chaque fois, charge et nucléons se conservent, et la masse qui disparaît réapparaît en énergie.»

Une centrale nucléaire, un examen d'imagerie médicale, la datation d'un charbon de bois vieux de trois mille ans : trois usages d'une même idée, le noyau change de nature. Huit notions te mènent des rayonnements d'un noyau instable aux énergies libérées par la fission et la fusion : la radioactivité et ses trois rayonnements, les lois de conservation et les équations de désintégration, la loi de décroissance et l'activité, la période, la datation par le carbone 14, la fission, la fusion, puis l'énergie libérée. On suppose acquis le défaut de masse, la relation d'Einstein E = Δm·c² et la conversion entre u, MeV et joule du chapitre précédent.

Sauf indication contraire, on utilise : 1 u = 931,5 MeV·c⁻² ; 1 MeV = 1,60 × 10⁻¹³ J ; 𝒩 = 6,02 × 10²³ mol⁻¹ ; ln 2 = 0,693 ; 1 an = 3,15 × 10⁷ s ; m_n = 1,00867 u.

## ☢️ La radioactivité et ses trois rayonnements

Vers 1899, Becquerel place un sel de radium au fond d'une petite cavité creusée dans un bloc de plomb : un fin faisceau en sort. Il lui fait traverser un champ électrique, et l'écran qui le reçoit porte non pas une tache, mais trois.
Qu'est-ce qui sort de ce noyau, pourquoi le faisceau se sépare-t-il en trois, et qu'est-ce qui arrête chaque rayonnement ?

::: definition
**Radioactivité** — La radioactivité est la transformation **spontanée** d'un noyau instable en un noyau d'une autre espèce chimique, avec émission d'un rayonnement. Le noyau qui se désintègre est le **noyau père**, celui qui se forme est le **noyau fils**. Elle est de nature **nucléaire** : son intensité ne dépend ni de la température, ni de la pression, ni de la combinaison chimique de l'atome. Trois rayonnements en résultent :

- le rayonnement **α** : des noyaux d'hélium ⁴₂He, de charge positive ;
- le rayonnement **β⁻** : des électrons ⁰₋₁e, de charge négative ; un rayonnement **β⁺**, formé de positons ⁰₁e (même masse que l'électron, charge positive), existe pour certains noyaux produits au laboratoire ;
- le rayonnement **γ** : des photons, sans charge.
:::

| Rayonnement | Nature | Charge | Ionisation | Pénétration |
| --- | --- | --- | --- | --- |
| α | noyau d'hélium ⁴₂He | positive | très ionisant | arrêté par une feuille de papier ou quelques centimètres d'air |
| β⁻ | électron ⁰₋₁e | négative | moins ionisant | arrêté par une plaque d'aluminium d'environ 7 mm |
| β⁺ | positon ⁰₁e | positive | comme β⁻ | comme β⁻ |
| γ | photons de très courte longueur d'onde | nulle | peu ionisant | traverse jusqu'à environ 20 cm de plomb ou de béton |

::: figure Un faisceau issu de la source traverse un champ électrique entre une plaque positive (en haut) et une plaque négative (en bas) : α est dévié vers le bas, β⁻ vers le haut, γ n'est pas dévié ; les amplitudes des déviations sont schématiques
<svg viewBox="0 0 340 204">
<title>Un faisceau issu d'une source traverse un champ électrique entre une plaque positive en haut et une plaque négative en bas : le rayonnement α est dévié vers le bas, le rayonnement β moins vers le haut, plus fortement, le rayonnement γ n'est pas dévié</title>
<rect x="8" y="88" width="42" height="24" fill="#cbd5e1" stroke="#0f172a" stroke-width="2"/>
<text x="29" y="128" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">source</text>
<line x1="70" y1="48" x2="230" y2="48" stroke="#ef4444" stroke-width="5"/><line x1="70" y1="152" x2="230" y2="152" stroke="#2563eb" stroke-width="5"/>
<text x="150" y="40" text-anchor="middle" fill="#ef4444" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">plaque +</text><text x="150" y="172" text-anchor="middle" fill="#2563eb" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">plaque −</text>
<line x1="290" y1="20" x2="290" y2="180" stroke="#0f172a" stroke-width="4"/><text x="290" y="196" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">écran</text>
<line x1="50" y1="100" x2="290" y2="100" stroke="#64748b" stroke-width="2.5" stroke-dasharray="6 4"/>
<polyline points="50,100 70,100 70,100 80,100.06 90,100.25 100,100.56 110,101 120,101.56 130,102.25 140,103.06 150,104 160,105.06 170,106.25 180,107.56 190,109 200,110.56 210,112.25 220,114.06 230,116 290,128" fill="none" stroke="#ef4444" stroke-width="2.5"/>
<polyline points="50,100 70,100 70,100 80,99.87 90,99.47 100,98.8 110,97.88 120,96.68 130,95.22 140,93.49 150,91.5 160,89.24 170,86.72 180,83.93 190,80.88 200,77.56 210,73.97 220,70.12 230,66 290,40.5" fill="none" stroke="#2563eb" stroke-width="2.5"/>
<circle cx="290" cy="128" r="4" fill="#ef4444" stroke="#0f172a" stroke-width="1.5"/><circle cx="290" cy="40.5" r="4" fill="#2563eb" stroke="#0f172a" stroke-width="1.5"/><circle cx="290" cy="100" r="4" fill="#64748b" stroke="#0f172a" stroke-width="1.5"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="308" y="132" text-anchor="middle" fill="#ef4444" font-size="14">α</text><text x="310" y="44.5" text-anchor="middle" fill="#2563eb" font-size="14">β⁻</text><text x="308" y="104" text-anchor="middle" fill="#64748b" font-size="14">γ</text></g>
</svg>
:::

Sur la figure, la plaque du haut est positive : une charge négative est attirée vers elle (β⁻), une charge positive est repoussée vers la plaque du bas (α), et un faisceau sans charge file tout droit (γ). Un faisceau β⁺ serait dévié comme α, vers la plaque négative.

::: exemple Lire les trois impacts de l'écran, puis choisir les écrans protecteurs

1. L'impact du centre n'est pas dévié : le champ n'agit pas sur lui, donc ce rayonnement est sans charge. C'est le rayonnement γ, des photons.
2. L'impact du bas est dévié vers la plaque négative : il porte une charge positive, car des charges de même signe que la plaque se repoussent et des charges de signe opposé s'attirent. C'est le rayonnement α, noyaux ⁴₂He.
3. L'impact du haut est dévié vers la plaque positive : il porte une charge négative. C'est le rayonnement β⁻, des électrons.
4. On met sur le trajet une feuille de papier : seuls les α sont arrêtés, car ils sont peu pénétrants (quelques centimètres d'air suffisent).
5. On ajoute une plaque d'aluminium d'environ 7 mm : les β⁻ sont arrêtés à leur tour. Seul le γ subsiste : il faut environ 20 cm de plomb pour l'arrêter.
6. On chauffe la source de 20 °C à 80 °C : le nombre d'impacts par seconde ne change pas, car l'émission vient du noyau et non du cortège d'électrons ni de l'agitation thermique.

:::

::: piege
**Erreur : croire que le rayonnement le plus ionisant est aussi le plus pénétrant.** On pourrait déduire que α, très ionisant, traverse le plus de matière. L'erreur tente parce qu'on associe « puissant » à « loin ». Mais α cède son énergie dès les premiers atomes rencontrés : une feuille de papier l'arrête (étape 4). C'est γ, peu ionisant, qui traverse le plus (étape 5).
:::

::: propriete
**Ce qui reste vrai** — La radioactivité est un phénomène spontané et nucléaire : aucun agent extérieur ne la déclenche et la chimie n'y change rien. Les noyaux lourds (A > 200) émettent le plus souvent un rayonnement α, les noyaux à excès de neutrons un rayonnement β⁻, les noyaux à excès de protons un rayonnement β⁺. Cas limite : le rayonnement γ accompagne en général une désintégration α ou β : il signale un noyau fils formé dans un état excité.
:::

::: verifie À toi : l'aluminium
Une source émet des rayonnements α, β⁻ et γ. On place devant elle une plaque d'aluminium épaisse de 1 cm. Quels rayonnements l'écran derrière la plaque reçoit-il encore ?

---

Les α sont arrêtés par une simple feuille de papier, donc a fortiori par 1 cm d'aluminium. Les β⁻ sont arrêtés par environ 7 mm d'aluminium, donc par 1 cm aussi. Il ne reste que le rayonnement γ, qu'il faut environ 20 cm de plomb pour arrêter.
:::

::: retenir
La radioactivité est la transformation spontanée d'un noyau instable avec émission de α (hélium, positif), β⁻ (électron, négatif), β⁺ (positon, positif) ou γ (photons, sans charge) ; la pénétration croît de α à β puis γ.
:::

## ⚖️ Les lois de conservation et les équations de désintégration

Un noyau de radon 222 (²²²₈₆Rn) émet un rayonnement α. Avant, il y a 222 nucléons dont 86 protons. Après, la particule α emporte 4 nucléons dont 2 protons, et un noyau fils reste.
Comment trouver ce noyau fils sans le chercher dans un tableau, et que dire des autres rayonnements ?

::: definition
**Lois de conservation (Soddy)** — Dans toute réaction nucléaire, la **somme des nombres de charge Z** et la **somme des nombres de masse A** ont la même valeur avant et après, et l'énergie totale se conserve. Une équation de réaction nucléaire s'écrit en respectant ces deux égalités :

- conservation de la charge : ΣZ avant = ΣZ après ;
- conservation du nombre de nucléons : ΣA avant = ΣA après.
:::

| Désintégration | Équation | Noyau fils | Origine |
| --- | --- | --- | --- |
| α | ᴬ_Z X → ⁴₂He + ᴬ⁻⁴_Z₋₂ Y | A − 4 et Z − 2 | noyau lourd |
| β⁻ | ᴬ_Z X → ⁰₋₁e + ᴬ_Z₊₁ Y | A et Z + 1 | un neutron devient un proton : ¹₀n → ¹₁p + ⁰₋₁e |
| β⁺ | ᴬ_Z X → ⁰₁e + ᴬ_Z₋₁ Y | A et Z − 1 | un proton devient un neutron : ¹₁p → ¹₀n + ⁰₁e |
| γ | ᴬ_Z Y∗ → ᴬ_Z Y + γ | A et Z inchangés | le noyau excité retourne à l'état fondamental |

::: exemple Écrire quatre équations, puis remonter une famille radioactive

1. Radon 222, α : A = 222 − 4 = 218 et Z = 86 − 2 = 84. Le noyau fils est le polonium : ²²²₈₆Rn → ⁴₂He + ²¹⁸₈₄Po. Contrôle : 218 + 4 = 222 et 84 + 2 = 86.
2. Phosphore 32, β⁻ : le fils a Z = 15 + 1 = 16 (soufre) et A = 32, car l'électron emporte la charge −1 : ³²₁₅P → ⁰₋₁e + ³²₁₆S. Contrôle de la charge : 15 = −1 + 16.
3. Sodium 22, β⁺ : le fils a Z = 11 − 1 = 10 (néon) : ²²₁₁Na → ⁰₁e + ²²₁₀Ne. Contrôle : 11 = 1 + 10.
4. Sodium 24, β⁻ : il donne du magnésium formé dans un état excité, qui se désexcite en émettant un photon : ²⁴₁₁Na → ⁰₋₁e + ²⁴₁₂Mg∗, puis ²⁴₁₂Mg∗ → ²⁴₁₂Mg + γ.
5. Famille du thorium 232, qui aboutit au plomb stable ²⁰⁸₈₂Pb par x désintégrations α et y désintégrations β⁻. Nombre de masse : 232 = 208 + 4x donc x = 6. Charge : 90 = 82 + 2x − y = 82 + 12 − y donc y = 4.

:::

::: piege
**Erreur : écrire Z − 1 pour une désintégration β⁻.** Pour le phosphore 32, on obtiendrait ³²₁₄Si. L'erreur tente parce que l'électron est négatif et qu'on pense « charge en moins ». Mais l'électron est émis : il emporte −1, donc le noyau fils doit porter une charge de plus pour que le total reste égal à 15 (étape 2) : Z = 16.
:::

::: propriete
**Ce qui reste vrai** — Ce sont les nombres A et Z qui se conservent, pas la masse en unités de masse atomique : ces réactions libèrent de l'énergie, donc la masse diminue (notion 8). Pour trouver x et y dans une chaîne : A donne x (A initial − A final = 4x), puis Z donne y. Cas limite : l'émission γ ne change ni A ni Z, elle ne transforme pas le noyau en un autre élément. La capture d'un neutron par un noyau ajoute 1 à A sans changer Z (²³⁸₉₂U + ¹₀n → ²³⁹₉₂U).
:::

::: verifie À toi : l'azote 13
L'azote 13, ¹³₇N, émet un positon. Écrire l'équation et nommer le noyau fils (Z = 6 : carbone).

---

β⁺ : Z diminue de 1 et A est inchangé, donc Z = 7 − 1 = 6, soit le carbone 13 : ¹³₇N → ⁰₁e + ¹³₆C. Contrôle : 13 = 0 + 13 et 7 = 1 + 6.
:::

::: retenir
Une équation nucléaire conserve la somme des Z et la somme des A : α retire 4 à A et 2 à Z, β⁻ ajoute 1 à Z, β⁺ retire 1 à Z, γ ne change ni A ni Z.
:::

## 📉 La loi de décroissance radioactive et l'activité

Un échantillon contient N₀ = 5,0 × 10⁶ noyaux d'un radioélément à l'instant t = 0. Un compteur Geiger-Müller placé près de lui claque de moins en moins vite à mesure que le temps passe. Pour ce radioélément, la probabilité qu'un noyau se désintègre pendant une seconde est la constante λ = 2,0 × 10⁻³ s⁻¹.
Combien de noyaux restent-ils à l'instant t, et combien de désintégrations se produisent-elles chaque seconde ?

::: definition
**Loi de décroissance et activité** — Pendant une durée très courte dt, le nombre de noyaux qui se désintègrent est proportionnel au nombre N de noyaux présents (loi admise) :

$$ dN = −λ·N·dt $$

Son intégration donne la **loi de décroissance radioactive** N = N₀·e^(−λt), où λ est la **constante radioactive**, en s⁻¹, propre au noyau. L'**activité** A est le nombre de désintégrations par seconde, en becquerel (Bq, 1 Bq = 1 désintégration par seconde) :

$$ A = −dN/dt = λ·N = A₀·e^(−λt) $$

avec A₀ = λ·N₀ l'activité à t = 0.
:::

::: figure N(t) pour N₀ = 5,0 millions de noyaux et λ = 2,0 × 10⁻³ s⁻¹ : la courbe décroît de moins en moins vite et ne touche jamais l'axe du temps
<svg viewBox="0 0 340 240">
<title>Nombre de noyaux N en fonction du temps t : courbe décroissante qui passe par 5,0 millions de noyaux à t = 0, 1,84 million à 500 s et 0,68 million à 1000 s</title>
<line x1="46" y1="200" x2="334" y2="200" stroke="#0f172a" stroke-width="2"/>
<polygon points="334,200 325,204.5 325,195.5" fill="#0f172a"/>
<line x1="46" y1="200" x2="46" y2="22" stroke="#0f172a" stroke-width="2"/>
<polygon points="46,22 50.5,31 41.5,31" fill="#0f172a"/>
<line x1="46" y1="200" x2="46" y2="204" stroke="#0f172a" stroke-width="1.5"/><text x="46" y="217" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text>
<line x1="139.33" y1="200" x2="139.33" y2="204" stroke="#0f172a" stroke-width="1.5"/><text x="139.33" y="217" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">500</text>
<line x1="232.67" y1="200" x2="232.67" y2="204" stroke="#0f172a" stroke-width="1.5"/><text x="232.67" y="217" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1000</text>
<line x1="326" y1="200" x2="326" y2="204" stroke="#0f172a" stroke-width="1.5"/><text x="326" y="217" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1500</text>
<line x1="42" y1="166" x2="46" y2="166" stroke="#0f172a" stroke-width="1.5"/><text x="39" y="170" text-anchor="end" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text>
<line x1="42" y1="132" x2="46" y2="132" stroke="#0f172a" stroke-width="1.5"/><text x="39" y="136" text-anchor="end" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text>
<line x1="42" y1="98" x2="46" y2="98" stroke="#0f172a" stroke-width="1.5"/><text x="39" y="102" text-anchor="end" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text>
<line x1="42" y1="64" x2="46" y2="64" stroke="#0f172a" stroke-width="1.5"/><text x="39" y="68" text-anchor="end" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text>
<line x1="42" y1="30" x2="46" y2="30" stroke="#0f172a" stroke-width="1.5"/><text x="39" y="34" text-anchor="end" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text>
<polyline points="46,30 50.67,38.29 55.33,46.18 60,53.68 64.67,60.82 69.33,67.6 74,74.06 78.67,80.2 83.33,86.05 88,91.6 92.67,96.89 97.33,101.92 102,106.7 106.67,111.25 111.33,115.58 116,119.7 120.67,123.61 125.33,127.34 130,130.88 134.67,134.25 139.33,137.46 144,140.51 148.67,143.41 153.33,146.17 158,148.8 162.67,151.29 167.33,153.67 172,155.93 176.67,158.08 181.33,160.12 186,162.07 190.67,163.92 195.33,165.68 200,167.35 204.67,168.94 209.33,170.46 214,171.9 218.67,173.27 223.33,174.57 228,175.81 232.67,176.99 237.33,178.12 242,179.18 246.67,180.2 251.33,181.16 256,182.08 260.67,182.96 265.33,183.79 270,184.58 274.67,185.33 279.33,186.05 284,186.73 288.67,187.37 293.33,187.99 298,188.58 302.67,189.13 307.33,189.66 312,190.17 316.67,190.65 321.33,191.1 326,191.54" fill="none" stroke="#2563eb" stroke-width="3"/>
<circle cx="46" cy="30" r="4" fill="#d97706" stroke="#0f172a" stroke-width="1.5"/>
<line x1="139.33" y1="137.46" x2="139.33" y2="200" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3"/><line x1="46" y1="137.46" x2="139.33" y2="137.46" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3"/>
<circle cx="139.33" cy="137.46" r="4" fill="#d97706" stroke="#0f172a" stroke-width="1.5"/><text x="147.33" y="129.46" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,84</text>
<line x1="232.67" y1="176.99" x2="232.67" y2="200" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3"/><line x1="46" y1="176.99" x2="232.67" y2="176.99" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3"/>
<circle cx="232.67" cy="176.99" r="4" fill="#d97706" stroke="#0f172a" stroke-width="1.5"/><text x="240.67" y="168.99" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,68</text>
<text x="326" y="232" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (s)</text><text x="52" y="22" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N (10⁶ noyaux)</text>
</svg>
:::

La courbe est une exponentielle décroissante : elle part de N₀ et s'approche de zéro sans l'atteindre. Les trois points (5,0 ; 1,84 et 0,68 million de noyaux) sont ceux de l'exemple ci-dessous.

::: exemple Les noyaux restants et l'activité de l'échantillon (λ = 2,0 × 10⁻³ s⁻¹, N₀ = 5,0 × 10⁶)

1. Activité initiale : A₀ = λ·N₀ = 2,0 × 10⁻³ × 5,0 × 10⁶ = 1,0 × 10⁴ Bq, car l'activité est le produit de λ par le nombre de noyaux.
2. À t = 500 s : λt = 2,0 × 10⁻³ × 500 = 1,0, sans unité. N = 5,0 × 10⁶ × e⁻¹ = 5,0 × 10⁶ × 0,368 = 1,84 × 10⁶ noyaux.
3. Activité à 500 s : A = λ·N = 2,0 × 10⁻³ × 1,84 × 10⁶ = 3,68 × 10³ Bq. On retrouve A₀·e⁻¹ = 1,0 × 10⁴ × 0,368, car A et N décroissent dans le même rapport.
4. À t = 1000 s : λt = 2,0, donc N = 5,0 × 10⁶ × e⁻² = 5,0 × 10⁶ × 0,135 = 6,8 × 10⁵ noyaux.
5. En prenant le logarithme de la loi, ln N = ln N₀ − λt : le tracé de ln N en fonction de t est une droite de pente −λ.

:::

::: piege
**Erreur : croire que le nombre de noyaux diminue de la même quantité à chaque intervalle.** Pendant les 500 premières secondes, 5,0 × 10⁶ − 1,84 × 10⁶ = 3,16 × 10⁶ noyaux disparaissent (étape 2). On pourrait croire qu'il en disparaît autant les 500 suivantes : N(1000) = 5,0 × 10⁶ − 2 × 3,16 × 10⁶ = −1,3 × 10⁶, un nombre négatif, absurde. L'erreur tente parce qu'on pense à un robinet qui coule à débit constant. Mais le débit (l'activité) diminue avec N : les 500 secondes suivantes ne retirent que 1,84 × 10⁶ − 6,8 × 10⁵ = 1,16 × 10⁶ noyaux (étape 4).
:::

::: propriete
**Ce qui reste vrai** — Le rapport A/A₀ est égal à N/N₀, car A = λ·N. N et A sont des exponentielles décroissantes, jamais proportionnelles à t. λ est une constante positive qui ne dépend que du noyau : plus elle est grande, plus la décroissance est rapide. Cas limite : à t = 0 on a N = N₀ et A = A₀ ; à t très grand, N tend vers zéro sans jamais valoir exactement zéro.
:::

::: verifie À toi : un autre radioélément
Un échantillon a pour constante radioactive λ = 1,0 × 10⁻³ s⁻¹ et contient N₀ = 6,0 × 10⁶ noyaux. Calculer son activité initiale, puis le nombre de noyaux à t = 3000 s (e⁻³ = 0,0498).

---

A₀ = λ·N₀ = 1,0 × 10⁻³ × 6,0 × 10⁶ = 6,0 × 10³ Bq. À t = 3000 s : λt = 1,0 × 10⁻³ × 3000 = 3,0, donc N = 6,0 × 10⁶ × e⁻³ = 6,0 × 10⁶ × 0,0498 = 3,0 × 10⁵ noyaux.
:::

::: retenir
N = N₀·e^(−λt) et A = λ·N = A₀·e^(−λt) : le nombre de noyaux et l'activité (en Bq) décroissent exponentiellement, avec A₀ = λ·N₀.
:::

## ⏳ La période radioactive

Après l'accident de Tchernobyl en 1986, des sols de plusieurs régions d'Europe ont été contaminés par du césium 137, de période d'environ 30 ans. Un échantillon de ce sol a aujourd'hui une activité de 4,0 × 10⁶ Bq.
Combien de temps faut-il attendre pour qu'elle soit réduite de moitié, puis de moitié encore, et comment cette durée se relie-t-elle à λ ?

::: definition
**Période radioactive (demi-vie)** — La période T d'un radioélément est la durée au bout de laquelle le nombre de noyaux radioactifs d'un échantillon est divisé par 2. En écrivant N(T) = N₀/2 dans N = N₀·e^(−λt), on obtient e^(−λT) = 1/2, soit :

$$ T = ln 2/λ = 0,693/λ $$

La période caractérise le noyau : elle va de 10⁻¹⁵ s à 10²³ s selon le radioélément.
:::

| Noyau | ²¹⁴₈₄Po | ¹²³₅₃I | ¹³⁷₅₅Cs | ¹⁴₆C | ²³⁸₉₂U |
| --- | --- | --- | --- | --- | --- |
| Période | 1,5 × 10⁻⁴ s | 13,2 h | 30,2 ans | 5730 ans | 4,5 × 10⁹ ans |

::: figure À chaque période T, le nombre de noyaux est divisé par 2 : N₀, N₀/2, N₀/4, N₀/8
<svg viewBox="0 0 340 240">
<title>Nombre de noyaux N en fonction du temps, gradué en périodes T : N₀ à t = 0, N₀/2 à T, N₀/4 à 2T et N₀/8 à 3T</title>
<line x1="46" y1="200" x2="334" y2="200" stroke="#0f172a" stroke-width="2"/>
<polygon points="334,200 325,204.5 325,195.5" fill="#0f172a"/>
<line x1="46" y1="200" x2="46" y2="22" stroke="#0f172a" stroke-width="2"/>
<polygon points="46,22 50.5,31 41.5,31" fill="#0f172a"/>
<line x1="46" y1="200" x2="46" y2="204" stroke="#0f172a" stroke-width="1.5"/><text x="46" y="217" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text>
<line x1="112.5" y1="200" x2="112.5" y2="204" stroke="#0f172a" stroke-width="1.5"/><text x="112.5" y="217" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">T</text>
<line x1="179" y1="200" x2="179" y2="204" stroke="#0f172a" stroke-width="1.5"/><text x="179" y="217" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2T</text>
<line x1="245.5" y1="200" x2="245.5" y2="204" stroke="#0f172a" stroke-width="1.5"/><text x="245.5" y="217" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3T</text>
<line x1="312" y1="200" x2="312" y2="204" stroke="#0f172a" stroke-width="1.5"/><text x="312" y="217" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="400" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4T</text>
<polyline points="46,32 52.65,43.25 59.3,53.75 65.95,63.54 72.6,72.68 79.25,81.21 85.9,89.16 92.55,96.58 99.2,103.51 105.85,109.97 112.5,116 119.15,121.63 125.8,126.87 132.45,131.77 139.1,136.34 145.75,140.6 152.4,144.58 159.05,148.29 165.7,151.75 172.35,154.99 179,158 185.65,160.81 192.3,163.44 198.95,165.89 205.6,168.17 212.25,170.3 218.9,172.29 225.55,174.15 232.2,175.88 238.85,177.49 245.5,179 252.15,180.41 258.8,181.72 265.45,182.94 272.1,184.08 278.75,185.15 285.4,186.15 292.05,187.07 298.7,187.94 305.35,188.75 312,189.5 318.65,190.2 325.3,190.86" fill="none" stroke="#2563eb" stroke-width="3"/>
<circle cx="46" cy="32" r="4" fill="#d97706" stroke="#0f172a" stroke-width="1.5"/><text x="54" y="24" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N₀</text>
<line x1="112.5" y1="116" x2="112.5" y2="200" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3"/><line x1="46" y1="116" x2="112.5" y2="116" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3"/>
<circle cx="112.5" cy="116" r="4" fill="#d97706" stroke="#0f172a" stroke-width="1.5"/><text x="120.5" y="108" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N₀/2</text>
<line x1="179" y1="158" x2="179" y2="200" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3"/><line x1="46" y1="158" x2="179" y2="158" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3"/>
<circle cx="179" cy="158" r="4" fill="#d97706" stroke="#0f172a" stroke-width="1.5"/><text x="187" y="150" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N₀/4</text>
<line x1="245.5" y1="179" x2="245.5" y2="200" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3"/><line x1="46" y1="179" x2="245.5" y2="179" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3"/>
<circle cx="245.5" cy="179" r="4" fill="#d97706" stroke="#0f172a" stroke-width="1.5"/><text x="253.5" y="171" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N₀/8</text>
<text x="326" y="232" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t</text><text x="38" y="20" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N</text>
</svg>
:::

La figure gradue le temps en périodes : à chaque période, N est multiplié par 1/2. Après n périodes, N = N₀/2ⁿ, et il en va de même pour l'activité.

::: exemple Le césium 137 (T arrondie à 30,0 ans pour le calcul, A₀ = 4,0 × 10⁶ Bq)

1. Après 90 ans, soit 3T, l'activité est divisée par 2 trois fois : A = A₀/2³ = 4,0 × 10⁶ / 8 = 5,0 × 10⁵ Bq.
2. En secondes : T = 30,0 × 3,15 × 10⁷ = 9,45 × 10⁸ s, donc λ = 0,693 / 9,45 × 10⁸ = 7,33 × 10⁻¹⁰ s⁻¹, car λ = ln 2 / T.
3. Nombre de noyaux de césium 137 de l'échantillon : N₀ = A₀/λ = 4,0 × 10⁶ / 7,33 × 10⁻¹⁰ = 5,5 × 10¹⁵ noyaux, car A₀ = λ·N₀.
4. Contrôle d'ordre de grandeur : T de l'ordre de 10⁹ s donne λ de l'ordre de 10⁻⁹ s⁻¹ ✓.

:::

::: piege
**Erreur : croire qu'au bout de deux périodes tout l'échantillon a disparu.** On additionne « une moitié disparaît à T, l'autre moitié à 2T ». L'erreur tente parce que 1/2 + 1/2 = 1. Mais à la seconde période, c'est la moitié de ce qui **reste** qui disparaît : à 60 ans l'activité vaut A₀/4 = 1,0 × 10⁶ Bq, et non 0. Elle vaut A₀/8 à 90 ans (étape 1), A₀/16 à 120 ans, sans jamais s'annuler.
:::

::: propriete
**Ce qui reste vrai** — T = ln 2/λ : la période est inversement proportionnelle à λ. Pour une durée t = n·T avec n entier, N = N₀/2ⁿ. Cas limite : pour une durée qui n'est pas un multiple de T, on n'écrit pas « N₀/2^n » avec n entier, mais N = N₀·e^(−λt), c'est-à-dire N = N₀·2^(−t/T).
:::

::: verifie À toi : une période de 12 heures
L'activité d'un échantillon de période T = 12 h est de 8,0 × 10⁶ Bq à t = 0. Quelle est-elle deux jours plus tard ?

---

Deux jours valent 48 h, soit 48 / 12 = 4 périodes : A = A₀/2⁴ = 8,0 × 10⁶ / 16 = 5,0 × 10⁵ Bq.
:::

::: retenir
La période T = ln 2/λ est la durée qui divise N par 2 ; après n périodes, N = N₀/2ⁿ et A = A₀/2ⁿ.
:::

## 🪵 La datation par le carbone 14

Dans une grotte, on trouve un morceau de charbon de bois. Une archéologue veut savoir depuis combien de temps l'arbre a été brûlé. Tant qu'un arbre vit, il assimile du carbone dont une part très faible est du carbone 14, radioactif β⁻ : le rapport ¹⁴₆C / ¹²₆C dans son bois est le même que dans l'air. À sa mort, l'assimilation s'arrête et le carbone 14 qu'il contient se désintègre sans être renouvelé.
Comment passer de la mesure de l'activité du charbon à son âge ?

::: definition
**Datation par le carbone 14** — Pour un échantillon de masse donnée, l'activité du carbone 14 vaut A₀ à la mort de l'organisme (la même que celle d'un échantillon vivant de même masse) et A à l'instant de la mesure, après une durée t. Comme A = A₀·e^(−λt), l'âge est :

$$ t = (T/ln 2)·ln(A₀/A) $$

avec T = 5730 ans la période du carbone 14.
:::

::: exemple Deux échantillons de bois, 13,6 désintégrations par minute et par gramme de carbone pour le bois vivant

1. Premier échantillon : 3,4 désintégrations par minute et par gramme. Rapport A/A₀ = 3,4 / 13,6 = 0,25 = (1/2)², donc t = 2T = 2 × 5730 = 11 460 ans, car l'activité a été divisée par 2 deux fois.
2. Second échantillon : 9,6 désintégrations par minute et par gramme. Le rapport 13,6 / 9,6 = 1,417 n'est pas une puissance de 2, on utilise la formule.
3. t = (5730 / 0,693) × ln 1,417 = 8268 × 0,348 = 2,88 × 10³ ans, car ln 1,417 = 0,348.
4. Contrôle : A/A₀ = 0,706 est entre 1 et 1/2 : l'âge est compris entre 0 et T = 5730 ans ✓.

:::

::: piege
**Erreur : inverser le rapport des activités et trouver un âge négatif.** Si on écrit t = (T/ln 2)·ln(A/A₀), on obtient 8268 × ln(0,706) = −2,88 × 10³ ans, un âge négatif (étape 3). L'erreur tente parce que la loi s'écrit A = A₀·e^(−λt) avec A en tête. Mais en isolant t on change le signe : ln(A/A₀) < 0 donc t = −(1/λ)·ln(A/A₀), soit ln(A₀/A) avec A₀ au numérateur.
:::

::: propriete
**Ce qui reste vrai** — Plus l'objet est ancien, plus A est petit devant A₀ et plus ln(A₀/A) est grand. Cas limite : A = A₀ donne t = 0 (organisme vivant). Au bout d'un très grand nombre de périodes, l'activité du carbone 14 devient trop faible pour être mesurée : pour des objets bien plus vieux, on utilise un radioélément de plus longue période, comme l'uranium 238 (T = 4,5 × 10⁹ ans), qui donne l'âge de la Terre.
:::

::: verifie À toi : un charbon très ancien
Un charbon de bois donne 1,7 désintégration par minute et par gramme de carbone, contre 13,6 pour le bois vivant. Quel est son âge ?

---

A/A₀ = 1,7 / 13,6 = 0,125 = (1/2)³ : l'activité a été divisée par 2 trois fois, donc t = 3T = 3 × 5730 = 17 190 ans.
:::

::: retenir
t = (T/ln 2)·ln(A₀/A) : l'âge se déduit du rapport entre l'activité du carbone 14 d'un échantillon vivant et celle de l'échantillon étudié.
:::

## 💥 La fission nucléaire

Dans le cœur d'un réacteur, un neutron lent frappe un noyau d'uranium 235 : celui-ci se déforme et se casse en deux noyaux plus petits, en libérant au passage deux ou trois neutrons. Ces neutrons peuvent frapper d'autres noyaux d'uranium voisins.
Pourquoi un neutron suffit-il à déclencher une fission, et comment une seule fission peut-elle en provoquer des milliards ?

::: definition
**Fission nucléaire** — La fission est une réaction nucléaire **provoquée** au cours de laquelle un noyau lourd, frappé par un neutron lent, se scinde en deux noyaux plus légers de masses comparables, en libérant des neutrons. Les noyaux qui en sont capables, comme ²³⁵₉₂U, ²³³₉₂U et ²³⁹₉₄Pu, sont dits **fissiles**. L'équation générale est :

$$ ¹₀n + ᴬ_Z X → ᴬ¹_Z₁ X₁ + ᴬ²_Z₂ X₂ + k ¹₀n $$

avec Z₁ + Z₂ = Z et A₁ + A₂ + k = A + 1 (le neutron incident compte dans le bilan).
:::

::: figure Réaction en chaîne, avec deux neutrons libérés par fission : 1 fission, puis 2 fissions, puis 4 neutrons libérés
<svg viewBox="0 0 340 200">
<title>Réaction en chaîne : un neutron provoque une fission qui libère deux neutrons, chacun provoque une nouvelle fission, et quatre neutrons sont libérés</title>
<line x1="6" y1="100" x2="40" y2="100" stroke="#2563eb" stroke-width="2.5"/>
<polygon points="40,100 31,104.5 31,95.5" fill="#2563eb"/>
<circle cx="58" cy="100" r="17" fill="#fed7aa" stroke="#0f172a" stroke-width="2"/><text x="58" y="104" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">U</text>
<line x1="72" y1="90" x2="128" y2="52" stroke="#2563eb" stroke-width="2.5"/>
<polygon points="128,52 123.08,60.78 118.03,53.33" fill="#2563eb"/><line x1="72" y1="110" x2="128" y2="148" stroke="#2563eb" stroke-width="2.5"/>
<polygon points="128,148 118.03,146.67 123.08,139.22" fill="#2563eb"/>
<circle cx="146" cy="46" r="17" fill="#fed7aa" stroke="#0f172a" stroke-width="2"/><text x="146" y="50" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">U</text><circle cx="146" cy="154" r="17" fill="#fed7aa" stroke="#0f172a" stroke-width="2"/><text x="146" y="158" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">U</text>
<line x1="160" y1="38" x2="230" y2="18" stroke="#2563eb" stroke-width="2.5"/>
<polygon points="230,18 222.58,24.8 220.11,16.15" fill="#2563eb"/><line x1="160" y1="54" x2="230" y2="74" stroke="#2563eb" stroke-width="2.5"/>
<polygon points="230,74 220.11,75.85 222.58,67.2" fill="#2563eb"/><line x1="160" y1="146" x2="230" y2="126" stroke="#2563eb" stroke-width="2.5"/>
<polygon points="230,126 222.58,132.8 220.11,124.15" fill="#2563eb"/><line x1="160" y1="162" x2="230" y2="182" stroke="#2563eb" stroke-width="2.5"/>
<polygon points="230,182 220.11,183.85 222.58,175.2" fill="#2563eb"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="24" y="86" text-anchor="middle" fill="#2563eb" font-size="13">n</text><text x="58" y="138" text-anchor="middle" fill="#0f172a" font-size="11">1 fission</text><text x="146" y="10" text-anchor="middle" fill="#0f172a" font-size="11">2 fissions</text><text x="290" y="100" text-anchor="middle" fill="#0f172a" font-size="12">4 neutrons</text><text x="290" y="116" text-anchor="middle" fill="#0f172a" font-size="12">libérés</text></g>
</svg>
:::

La figure suit les neutrons : chaque fission en libère deux (dans l'exemple ci-dessous), qui provoquent chacun une fission, et le nombre de neutrons double à chaque génération. C'est la **réaction en chaîne**. Les fragments des fissions ne sont pas dessinés.

::: exemple Équilibrer deux fissions de l'uranium 235

1. ¹₀n + ²³⁵₉₂U → ⁹⁰₃₈Sr + ¹⁴⁴₅₄Xe + k ¹₀n. Nombre de masse : 1 + 235 = 236 = 90 + 144 + k, donc k = 2. Contrôle de la charge : 92 = 38 + 54 ✓.
2. ¹₀n + ²³⁵₉₂U → ¹⁴¹₅₆Ba + ⁹²_Z Kr + 3 ¹₀n. Nombre de masse : 236 = 141 + 92 + 3 ✓. Charge : 92 = 56 + Z, donc Z = 36, qui est bien celui du krypton.
3. Le neutron est neutre : il n'est pas repoussé par les charges positives du noyau, ce qui lui permet d'y entrer même lent.
4. Si le nombre de fissions par seconde est maintenu constant, la réaction est **contrôlée** (réacteur nucléaire) ; si la chaîne s'emballe sans contrôle, elle est **incontrôlée** (bombe atomique).

:::

::: piege
**Erreur : oublier le neutron incident dans le bilan des nucléons.** Pour l'étape 1, on écrirait 235 = 90 + 144 + k et on trouverait k = 1. L'erreur tente parce que le neutron est un petit nucléon, qu'on ne voit pas comme un « réactif » à côté de l'uranium. Mais il est à gauche de la flèche : la somme des A avant est 1 + 235 = 236, donc k = 2.
:::

::: propriete
**Ce qui reste vrai** — Dans toute fission, la somme des Z des deux fragments est égale à Z du noyau lourd, et la somme des A des fragments et des neutrons émis est A + 1. Plusieurs couples de fragments sont possibles pour un même noyau (étapes 1 et 2). Cas limite : sans neutron incident, un noyau fissile comme ²³⁵U ne se scinde pas ; la fission est une réaction provoquée, pas une radioactivité spontanée.
:::

::: verifie À toi : le plutonium 239
Dans ¹₀n + ²³⁹₉₄Pu → ⁹⁶₃₈Sr + ¹⁴⁰₅₆Ba + k ¹₀n, déterminer k et vérifier la charge.

---

Masse : 1 + 239 = 240 = 96 + 140 + k, donc k = 4. Charge : 94 = 38 + 56 = 94 ✓.
:::

::: retenir
Une fission scinde un noyau lourd, sous l'effet d'un neutron lent, en deux noyaux plus légers et k neutrons : Z₁ + Z₂ = Z et A₁ + A₂ + k = A + 1 ; ces neutrons entretiennent une réaction en chaîne.
:::

## ☀️ La fusion nucléaire

Le Soleil brille depuis plus de quatre milliards d'années. Il est fait surtout d'hydrogène : des noyaux ¹₁H, c'est-à-dire des protons seuls. Aucun noyau lourd ne s'y casse.
Quelle réaction nucléaire alimente le Soleil, et pourquoi ne la voit-on pas se produire dans un récipient à température ambiante ?

::: definition
**Fusion nucléaire** — La fusion est une réaction nucléaire **provoquée** au cours de laquelle deux noyaux légers s'unissent pour former un noyau plus lourd. Comme deux noyaux positifs se repoussent, il faut les lancer l'un contre l'autre à très grande vitesse, donc à des températures de l'ordre de 10⁷ à 10⁸ K.
:::

::: exemple Équilibrer des fusions, dont le cycle du Soleil

1. Deutérium et tritium : ²₁H + ³₁H → ⁴₂He + ¹₀n. Nombre de masse : 2 + 3 = 5 = 4 + 1 ✓. Charge : 1 + 1 = 2 + 0 ✓.
2. Complétons ²₁H + ²₁H → ³₂He + X : A = 4 − 3 = 1 et Z = 2 − 2 = 0, donc X est un neutron ¹₀n.
3. Cycle du Soleil, trois étapes : ¹₁H + ¹₁H → ²₁H + ⁰₁e ; ¹₁H + ²₁H → ³₂He ; ³₂He + ³₂He → ⁴₂He + 2 ¹₁H.
4. Pour obtenir les deux ³₂He de la dernière étape, on fait les deux premières étapes deux fois : 6 noyaux ¹₁H sont consommés, 2 sont rendus à la dernière étape, donc 6 − 2 = 4 sont consommés au total.
5. Bilan : 4 ¹₁H → ⁴₂He + 2 ⁰₁e. Masse : 4 = 4 + 0 ✓. Charge : 4 = 2 + 2 ✓.

:::

::: piege
**Erreur : croire que la fusion se produit spontanément, comme la radioactivité.** On pourrait croire qu'un récipient d'hydrogène finit par donner de l'hélium. L'erreur tente parce qu'on met « réaction nucléaire » et « spontanée » dans le même sac. Mais deux protons se repoussent : sans une température de l'ordre de 10⁷ K (cœur du Soleil) à 10⁸ K (fusion sur Terre), ils ne s'approchent pas assez pour fusionner. La fusion, comme la fission, est provoquée.
:::

::: propriete
**Ce qui reste vrai** — La fusion libère de l'énergie quand les noyaux formés sont plus liés que les noyaux de départ (notion 8). La bombe H utilise une fusion non contrôlée, amorcée par l'explosion d'une bombe atomique à fission. Cas limite : la fusion contrôlée n'est pas encore maîtrisée de façon durable ; la fusion de l'hydrogène dans le Soleil fournit une grande partie de l'énergie que la Terre reçoit, en moyenne de l'ordre de 1 kW par mètre carré de sol.
:::

::: verifie À toi : une fusion avec l'hélium 3
Compléter ²₁H + ³₂He → ⁴₂He + X.

---

Masse : 2 + 3 = 5 = 4 + A donc A = 1. Charge : 1 + 2 = 3 = 2 + Z donc Z = 1. La particule X de nombre de masse 1 et de charge 1 est un proton ¹₁p.
:::

::: retenir
La fusion unit deux noyaux légers en un noyau plus lourd ; elle exige une température de 10⁷ à 10⁸ K pour vaincre la répulsion électrique, comme dans le Soleil, et elle est provoquée.
:::

## ⚡ L'énergie libérée par une réaction nucléaire

Une réaction chimique libère quelques électronvolts par atome. La fission d'un seul noyau d'uranium 235 libère environ 200 MeV, soit une centaine de millions de fois plus.
D'où vient cette énergie, et comment la calculer pour une fission, pour une fusion, puis les comparer ?

::: definition
**Énergie libérée par une réaction** — Dans les désintégrations spontanées, la fission et la fusion étudiées ici, la masse totale des produits est plus petite que celle des réactifs. La **perte de masse** est :

$$ |Δm| = Σm(réactifs) − Σm(produits) $$

et l'énergie libérée est E = |Δm|·c². Avec |Δm| en u, E (MeV) = |Δm| × 931,5. On peut la rapporter à un noyau, à un nucléon, à un gramme ou à une mole.
:::

::: exemple Fission de l'uranium 235 et fusion du deutérium et du tritium

1. Fission ¹₀n + ²³⁵₉₂U → ⁹⁰₃₈Sr + ¹⁴⁴₅₄Xe + 2 ¹₀n, avec m(²³⁵U) = 235,0439 u ; m(⁹⁰Sr) = 89,9077 u ; m(¹⁴⁴Xe) = 143,9382 u ; m(n) = 1,0087 u. Réactifs : 235,0439 + 1,0087 = 236,0526 u. Produits : 89,9077 + 143,9382 + 2 × 1,0087 = 235,8633 u.
2. |Δm| = 236,0526 − 235,8633 = 0,1893 u, donc E = 0,1893 × 931,5 = 176,3 MeV, soit 176,3 × 1,60 × 10⁻¹³ = 2,82 × 10⁻¹¹ J par noyau.
3. Par gramme d'uranium 235 : N = (1,00 / 235) × 6,02 × 10²³ = 2,56 × 10²¹ noyaux, donc E = 2,56 × 10²¹ × 2,82 × 10⁻¹¹ = 7,2 × 10¹⁰ J.
4. Fusion ²₁H + ³₁H → ⁴₂He + ¹₀n, avec m(²H) = 2,01355 u ; m(³H) = 3,01550 u ; m(⁴He) = 4,00150 u ; m(n) = 1,00867 u. |Δm| = (2,01355 + 3,01550) − (4,00150 + 1,00867) = 5,02905 − 5,01017 = 0,01888 u, donc E = 0,01888 × 931,5 = 17,6 MeV.
5. Par nucléon : fission 176,3 / 236 = 0,747 MeV ; fusion 17,6 / 5 = 3,52 MeV. Rapport 3,52 / 0,747 = 4,7.

:::

::: piege
**Erreur : comparer les énergies par noyau et conclure que la fission libère plus.** On compare 176,3 MeV et 17,6 MeV (étapes 2 et 4) et on déclare la fission « 10 fois plus énergétique ». L'erreur tente parce que ce sont les deux nombres qu'on a sous les yeux. Mais la fission met en jeu 236 nucléons et la fusion 5 : par nucléon (étape 5), c'est la fusion qui libère environ 4 à 5 fois plus.
:::

::: propriete
**Ce qui reste vrai** — L'énergie est libérée parce que les noyaux formés sont plus liés : l'énergie de liaison par nucléon, sur la courbe d'Aston, est d'environ 7,6 MeV pour l'uranium et d'environ 8,5 MeV pour les noyaux de la fission (A voisin de 100), et passe de 1,1 MeV pour ²H à environ 7 MeV pour ⁴He dans la fusion. Un noyau plus lié a une masse plus petite : d'où |Δm| > 0. Cas limite : si |Δm| = 0, la réaction ne libère aucune énergie.
:::

::: verifie À toi : le deutérium et l'hélium 3
Calculer l'énergie libérée par ²₁H + ³₂He → ⁴₂He + ¹₁p, avec m(²H) = 2,01355 u ; m(³He) = 3,01493 u ; m(⁴He) = 4,00150 u ; m(p) = 1,00728 u.

---

Réactifs : 2,01355 + 3,01493 = 5,02848 u. Produits : 4,00150 + 1,00728 = 5,00878 u. |Δm| = 5,02848 − 5,00878 = 0,01970 u, donc E = 0,01970 × 931,5 = 18,35 MeV.
:::

::: retenir
E = |Δm|·c² avec |Δm| = Σm(réactifs) − Σm(produits), et E (MeV) = |Δm| (u) × 931,5 ; on compare fission et fusion par nucléon, où la fusion l'emporte.
:::

> 🏆 Quête franchie, héros ! Tu sais reconnaître les rayonnements α, β⁻, β⁺ et γ, écrire les équations de désintégration avec les lois de Soddy, appliquer la loi de décroissance et la période, dater un échantillon par le carbone 14, équilibrer une fission ou une fusion, et calculer l'énergie libérée par la perte de masse. Les noyaux n'ont plus de secret !
