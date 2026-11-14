# ⚖️ Équilibre chimique — quand deux réactions se limitent l'une l'autre

> 💡 «Quand les quantités cessent de changer, la réaction n'est pas forcément finie : parfois, elle se poursuit... dans les deux sens à la fois.»

L'essence de jasmin est riche en éthanoate de benzyle, un ester que l'on sait fabriquer au laboratoire à partir d'un acide et d'un alcool. Pourtant, quelle que soit la durée du chauffage, il reste toujours de l'acide et de l'alcool dans le ballon : dans un ballon où l'on ne retire rien, la synthèse n'aboutit pas jusqu'au bout. Huit notions expliquent pourquoi : le taux d'avancement final, son calcul à partir d'un pH, la réaction inverse, l'état d'équilibre chimique, l'influence de la composition initiale, l'interprétation à l'échelle des molécules, l'estérification avec l'hydrolyse, et le suivi par dosage. On suppose acquis l'avancement x, le tableau descriptif et le réactif limitant (chapitre 1), la vitesse d'une réaction (chapitre 2) et les facteurs cinétiques (chapitre 3).

## 📏 Le taux d'avancement final : une réaction totale ou limitée

Dans V = 40,0 mL de mélange, on réunit 20,0 mL de peroxodisulfate de potassium à 2,0·10⁻² mol·L⁻¹ et 20,0 mL d'iodure de potassium à 0,10 mol·L⁻¹ : S₂O₈²⁻ + 2 I⁻ → I₂ + 2 SO₄²⁻. Une heure plus tard, le dosage donne n(I₂) = 4,0·10⁻⁴ mol, et cette valeur ne bouge plus.
La réaction est-elle allée « jusqu'au bout », et comment le chiffrer ?

::: definition
**Taux d'avancement final** — L'avancement maximal x_max est la valeur de l'avancement final si le système évolue jusqu'à la disparition du réactif limitant. Le taux d'avancement final est τ_f = x_f / x_max, sans unité. Une réaction est totale (ou pratiquement totale) si τ_f est égal ou proche de 1, et limitée si τ_f est inférieur à 1.
:::

Le tableau descriptif relie les quantités à x :

|                     | S₂O₈²⁻       | 2 I⁻          | I₂  | 2 SO₄²⁻ |
| ------------------- | ------------ | ------------- | --- | ------- |
| état initial (mol)  | 4,0·10⁻⁴     | 2,0·10⁻³      | 0   | 0       |
| état final (mol)    | 4,0·10⁻⁴ − x_f | 2,0·10⁻³ − 2x_f | x_f | 2x_f    |

::: exemple Calculer τ_f pour l'oxydation des ions iodure

1. n(S₂O₈²⁻) = 2,0·10⁻² × 20,0·10⁻³ = 4,0·10⁻⁴ mol et n(I⁻) = 0,10 × 20,0·10⁻³ = 2,0·10⁻³ mol, car n = C·V.
2. S₂O₈²⁻ s'épuise pour x = 4,0·10⁻⁴ mol, I⁻ pour x = 2,0·10⁻³/2 = 1,0·10⁻³ mol : le plus petit est atteint en premier, donc S₂O₈²⁻ est limitant et x_max = 4,0·10⁻⁴ mol.
3. Le coefficient de I₂ vaut 1 et il n'y en avait pas au départ, donc x_f = n(I₂) = 4,0·10⁻⁴ mol.
4. τ_f = 4,0·10⁻⁴ / 4,0·10⁻⁴ = 1 : la réaction est totale, le réactif limitant a disparu.
5. Contrôle : n_f(I⁻) = 2,0·10⁻³ − 2 × 4,0·10⁻⁴ = 1,2·10⁻³ mol, positif, donc I⁻ était bien en excès.

:::

::: piege
**Erreur : calculer x_max avec le mauvais réactif.** Avec I⁻, on trouve x_max = 1,0·10⁻³ mol et τ_f = 4,0·10⁻⁴/1,0·10⁻³ = 0,40, d'où la conclusion fausse « réaction limitée ». L'erreur tente parce que I⁻ est le réactif le plus abondant, donc le plus visible dans le tableau ; mais x_max est celui du réactif limitant, le premier à s'épuiser, ici S₂O₈²⁻.
:::

::: propriete
**Totale ou limitée** — x_f ≤ x_max, donc 0 ≤ τ_f ≤ 1. Si τ_f = 1, le réactif limitant a disparu ; si τ_f < 1, il en reste à la fin, avec les produits formés.
Cas limite : τ_f ne renseigne pas sur la durée : une réaction peut être totale et très lente, ou limitée et très rapide.
:::

::: verifie À toi : classer une réaction
Pour A + B → C, on part de n(A) = 0,040 mol et n(B) = 0,060 mol ; à la fin, n(C) = 0,030 mol. Calculer τ_f et conclure.

---

Les coefficients valent 1 : A s'épuise pour x = 0,040 mol, B pour x = 0,060 mol, donc A est limitant et x_max = 0,040 mol. x_f = n(C) = 0,030 mol, d'où τ_f = 0,030/0,040 = 0,75, inférieur à 1 : la réaction est limitée, il reste 0,010 mol de A.
:::

::: retenir
τ_f = x_f / x_max, avec x_max l'avancement du réactif limitant : τ_f = 1 pour une réaction totale, τ_f < 1 pour une réaction limitée.
:::

## 🧫 Calculer τ_f à partir d'un pH

On dissout 0,30 g d'acide éthanoïque pur CH₃COOH dans de l'eau, pour obtenir V = 250 mL de solution (M = 60 g·mol⁻¹). L'eau distillée a un pH de 7 ; la solution a un pH de 3,20, donc elle contient des ions H₃O⁺ qui n'existaient pas avant.
Quelle fraction des molécules d'acide a réagi avec l'eau ?

::: definition
**Relation du pH** — La concentration en ions hydronium se déduit du pH par [H₃O⁺] = 10^(−pH), en mol·L⁻¹, et la quantité d'ions par n(H₃O⁺) = [H₃O⁺]·V. Pour un acide AH dans l'eau, AH + H₂O → A⁻ + H₃O⁺ ; l'eau, solvant, est en excès, et on néglige les ions H₃O⁺ provenant de l'eau elle-même. Un acide dont la réaction avec l'eau est limitée (τ_f < 1) est dit acide faible.
:::

|                      | CH₃COOH | H₂O   | CH₃COO⁻ | H₃O⁺ |
| -------------------- | ------- | ----- | ------- | ---- |
| état initial (mol)   | n₀      | excès | 0       | 0    |
| état final (mol)     | n₀ − x_f | excès | x_f     | x_f  |

::: exemple Taux d'avancement final de l'ionisation de l'acide éthanoïque

1. n₀ = m/M = 0,30/60 = 5,0·10⁻³ mol. L'eau est en excès : l'acide est le seul réactif qui peut manquer, donc x_max = n₀ = 5,0·10⁻³ mol.
2. [H₃O⁺] = 10^(−3,20) ≈ 6,3·10⁻⁴ mol·L⁻¹, d'après la relation du pH.
3. n(H₃O⁺) = 6,3·10⁻⁴ × 0,250 ≈ 1,6·10⁻⁴ mol. Le coefficient de H₃O⁺ vaut 1 et il n'y en avait pas au départ, donc x_f ≈ 1,6·10⁻⁴ mol.
4. τ_f = 1,6·10⁻⁴ / 5,0·10⁻³ ≈ 3,2·10⁻² : seulement 3,2 % des molécules d'acide ont réagi, la réaction est limitée.
5. Composition finale : n(CH₃COOH) = 5,0·10⁻³ − 1,6·10⁻⁴ ≈ 4,8·10⁻³ mol, et n(CH₃COO⁻) = n(H₃O⁺) ≈ 1,6·10⁻⁴ mol.

:::

::: piege
**Erreur : prendre la concentration pour la quantité de matière.** Avec x_f = 10^(−3,20) = 6,3·10⁻⁴ mol, on trouve τ_f = 6,3·10⁻⁴/5,0·10⁻³ ≈ 0,13, quatre fois trop grand. L'erreur tente parce que 10^(−pH) est le seul nombre fourni par le pH-mètre ; mais il est exprimé en mol·L⁻¹, et il faut le multiplier par le volume V = 0,250 L pour obtenir des moles.
:::

::: propriete
**τ_f d'un acide dans l'eau** — x_max = n₀(AH) = C·V et x_f = 10^(−pH)·V, d'où τ_f = 10^(−pH) / C : le volume se simplifie.
Cas limite : si l'acide réagissait totalement, on aurait [H₃O⁺] = n₀/V = 2,0·10⁻² mol·L⁻¹, soit un pH de 1,70. Le pH mesuré, 3,20, correspond à [H₃O⁺] = 6,3·10⁻⁴ mol·L⁻¹, trente fois moins : l'ionisation est bien partielle.
:::

::: verifie À toi : même démarche avec un autre acide
On dissout 0,23 g d'acide méthanoïque HCOOH (M = 46 g·mol⁻¹) dans de l'eau pour obtenir 100 mL de solution ; le pH vaut 2,60. Calculer τ_f.

---

n₀ = 0,23/46 = 5,0·10⁻³ mol = x_max. [H₃O⁺] = 10^(−2,60) ≈ 2,5·10⁻³ mol·L⁻¹, donc x_f = 2,5·10⁻³ × 0,100 = 2,5·10⁻⁴ mol. τ_f = 2,5·10⁻⁴/5,0·10⁻³ = 5,0·10⁻² : réaction limitée.
:::

::: retenir
[H₃O⁺] = 10^(−pH) puis x_f = [H₃O⁺]·V ; avec x_max = n₀ de l'acide (eau en excès), τ_f = x_f/x_max, et τ_f < 1 : l'acide réagit partiellement.
:::

## 🔁 La réaction inverse et la double flèche

Dans 100 mL d'acide chlorhydrique de pH 2,00 (volume constant), on verse 164 mg d'éthanoate de sodium CH₃COONa (M = 82 g·mol⁻¹), qui libère 2,0·10⁻³ mol d'ions éthanoate CH₃COO⁻. Le pH monte à 4,7.
Les ions éthanoate ont donc fait disparaître des ions H₃O⁺ : quelle réaction l'a permis ?

::: definition
**Réaction directe, réaction inverse** — Une équation lue de gauche à droite décrit la réaction directe, notée (1) ou (+1) ; la réaction de droite à gauche est la réaction inverse, notée (−1). Quand deux réactions inverses se produisent en même temps et se limitent mutuellement, on écrit une double flèche ⇄.
:::

|                              | avant l'ajout | après l'ajout |
| ---------------------------- | ------------- | ------------- |
| pH                           | 2,00          | 4,7           |
| [H₃O⁺] (mol·L⁻¹)             | 1,0·10⁻²      | 2,0·10⁻⁵      |
| n(H₃O⁺) dans 0,100 L (mol)   | 1,0·10⁻³      | 2,0·10⁻⁶      |

::: exemple Trouver la réaction qui consomme les ions H₃O⁺

1. Avant : n(H₃O⁺) = 10^(−2,00) × 0,100 = 1,0·10⁻³ mol ; après : 10^(−4,7) × 0,100 = 2,0·10⁻⁶ mol, car n = [H₃O⁺]·V.
2. Environ 1,0·10⁻³ mol d'ions H₃O⁺ ont disparu : une réaction les consomme, et les seules espèces ajoutées sont les ions éthanoate.
3. Elle s'écrit CH₃COO⁻ + H₃O⁺ → CH₃COOH + H₂O : les ions éthanoate captent les ions hydronium et reforment l'acide.
4. C'est l'inverse de l'ionisation CH₃COOH + H₂O → CH₃COO⁻ + H₃O⁺ vue plus haut : mêmes espèces, lues de droite à gauche.
5. Conclusion : dans une solution d'acide éthanoïque, les ions éthanoate et hydronium formés se recombinent. On écrit CH₃COOH + H₂O ⇄ CH₃COO⁻ + H₃O⁺.

:::

::: piege
**Erreur : appeler « indirecte » la réaction inverse.** Dire que la réaction des ions éthanoate avec les ions hydronium est « la réaction indirecte » de l'ionisation est faux. Un passage de M vers N a pour passage inverse celui de N vers M, par le même chemin parcouru à l'envers ; un chemin indirect ferait un détour par un autre itinéraire. L'erreur tente parce que « inverse » et « indirect » commencent pareil ; mais une réaction indirecte suppose d'autres réactions intermédiaires, ce qui n'est pas le cas ici.
:::

::: propriete
**Lecture d'une équation** — En l'absence d'indication contraire, on lit l'équation de gauche à droite, donc dans le sens direct. Chacune des deux réactions se produit ou non selon les conditions : une réaction est limitée parce que sa réaction inverse se produit aussi.
Cas limite : pour une réaction totale, la réaction inverse est négligeable et on écrit une flèche simple →, comme pour S₂O₈²⁻ + 2 I⁻ → I₂ + 2 SO₄²⁻.
:::

::: verifie À toi : écrire la réaction inverse
Écrire la réaction inverse de HCOOH + H₂O → HCOO⁻ + H₃O⁺, puis dire laquelle des deux est la réaction directe quand on écrit HCOOH + H₂O ⇄ HCOO⁻ + H₃O⁺ sans autre indication.

---

On lit l'équation de droite à gauche : HCOO⁻ + H₃O⁺ → HCOOH + H₂O, c'est la réaction inverse. Sans indication, on lit de gauche à droite : la réaction directe est HCOOH + H₂O → HCOO⁻ + H₃O⁺.
:::

::: retenir
Une réaction est dite directe (gauche → droite) ou inverse (droite → gauche) ; la double flèche ⇄ traduit deux réactions inverses simultanées qui se limitent, et l'inverse n'est pas l'« indirecte ».
:::

## ⚖️ L'état d'équilibre chimique

On suit l'avancement de deux réactions, (A) et (B), qui ont le même avancement maximal x_max = 6,0 mmol. (A) : 6,0 mmol de peroxodisulfate avec un grand excès d'ions iodure. (B) : 6,0 mmol d'acide et 6,0 mmol d'alcool, mélangés pour former un ester et de l'eau. Dans les deux cas, x cesse d'évoluer au bout d'une heure environ.
Est-ce que « les quantités ne bougent plus » veut dire la même chose pour (A) et pour (B) ?

::: definition
**État d'équilibre chimique** — Un système est en état d'équilibre chimique si, en dehors de toute intervention du milieu extérieur, les réactifs et les produits sont présents dans le système et leurs quantités de matière ne changent pas au cours du temps. Si τ_f = 1, le réactif limitant a disparu : l'état final est alors un équilibre d'un autre type, dit équilibre statique.
:::

::: figure Les courbes x(t) des réactions (A) et (B) : la courbe (A) se stabilise sur la ligne pointillée x_max, la courbe (B) se stabilise au-dessous
<svg viewBox="0 0 340 236"><title>Courbes x(t) des réactions (A) et (B)</title><line x1="99.3" y1="26" x2="99.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="144.7" y1="26" x2="144.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="190.0" y1="26" x2="190.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="235.3" y1="26" x2="235.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="280.7" y1="26" x2="280.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326.0" y1="26" x2="326.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="166.6" x2="326" y2="166.6" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="143.1" x2="326" y2="143.1" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="119.7" x2="326" y2="119.7" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="96.3" x2="326" y2="96.3" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="72.9" x2="326" y2="72.9" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="49.4" x2="326" y2="49.4" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="26.0" x2="326" y2="26.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="54.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="99.3" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="144.7" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="190.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><text x="235.3" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="280.7" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">50</text><text x="326.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><text x="48.0" y="194.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="48.0" y="170.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="48.0" y="147.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="48.0" y="123.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><text x="48.0" y="100.3" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><text x="48.0" y="76.9" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><text x="48.0" y="53.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="334.0" y="218.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (min)</text><text x="60.0" y="12.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x (mmol)</text><line x1="54" y1="49.4" x2="326" y2="49.4" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><polyline points="54.0,190.0 56.3,181.5 58.5,173.5 60.8,166.0 63.1,158.9 65.3,152.3 67.6,146.0 69.9,140.2 72.1,134.7 74.4,129.5 76.7,124.7 78.9,120.1 81.2,115.8 83.5,111.8 85.7,108.0 88.0,104.5 90.3,101.1 92.5,98.0 94.8,95.1 97.1,92.3 99.3,89.7 101.6,87.3 103.9,85.0 106.1,82.8 108.4,80.8 110.7,78.9 112.9,77.1 115.2,75.4 117.5,73.9 119.7,72.4 122.0,71.0 124.3,69.7 126.5,68.5 128.8,67.3 131.1,66.2 133.3,65.2 135.6,64.2 137.9,63.3 140.1,62.5 142.4,61.7 144.7,61.0 146.9,60.3 149.2,59.6 151.5,59.0 153.7,58.4 156.0,57.9 158.3,57.4 160.5,56.9 162.8,56.4 165.1,56.0 167.3,55.6 169.6,55.2 171.9,54.9 174.1,54.5 176.4,54.2 178.7,53.9 180.9,53.7 183.2,53.4 185.5,53.2 187.7,52.9 190.0,52.7 192.3,52.5 194.5,52.3 196.8,52.2 199.1,52.0 201.3,51.8 203.6,51.7 205.9,51.6 208.1,51.4 210.4,51.3 212.7,51.2 214.9,51.1 217.2,51.0 219.5,50.9 221.7,50.8 224.0,50.7 226.3,50.6 228.5,50.6 230.8,50.5 233.1,50.4 235.3,50.4 237.6,50.3 239.9,50.3 242.1,50.2 244.4,50.2 246.7,50.1 248.9,50.1 251.2,50.0 253.5,50.0 255.7,50.0 258.0,49.9 260.3,49.9 262.5,49.9 264.8,49.8 267.1,49.8 269.3,49.8 271.6,49.8 273.9,49.8 276.1,49.7 278.4,49.7 280.7,49.7 282.9,49.7 285.2,49.7 287.5,49.7 289.7,49.6 292.0,49.6 294.3,49.6 296.5,49.6 298.8,49.6 301.1,49.6 303.3,49.6 305.6,49.6 307.9,49.6 310.1,49.5 312.4,49.5 314.7,49.5 316.9,49.5 319.2,49.5 321.5,49.5 323.7,49.5 326.0,49.5" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="54.0,190.0 56.3,186.2 58.5,182.5 60.8,179.0 63.1,175.6 65.3,172.4 67.6,169.3 69.9,166.3 72.1,163.4 74.4,160.7 76.7,158.1 78.9,155.5 81.2,153.1 83.5,150.8 85.7,148.6 88.0,146.4 90.3,144.4 92.5,142.4 94.8,140.6 97.1,138.7 99.3,137.0 101.6,135.4 103.9,133.8 106.1,132.2 108.4,130.8 110.7,129.4 112.9,128.0 115.2,126.7 117.5,125.5 119.7,124.3 122.0,123.1 124.3,122.0 126.5,121.0 128.8,120.0 131.1,119.0 133.3,118.1 135.6,117.2 137.9,116.3 140.1,115.5 142.4,114.7 144.7,114.0 146.9,113.3 149.2,112.6 151.5,111.9 153.7,111.3 156.0,110.7 158.3,110.1 160.5,109.5 162.8,109.0 165.1,108.5 167.3,108.0 169.6,107.5 171.9,107.0 174.1,106.6 176.4,106.2 178.7,105.8 180.9,105.4 183.2,105.0 185.5,104.6 187.7,104.3 190.0,104.0 192.3,103.7 194.5,103.4 196.8,103.1 199.1,102.8 201.3,102.5 203.6,102.3 205.9,102.0 208.1,101.8 210.4,101.6 212.7,101.4 214.9,101.1 217.2,101.0 219.5,100.8 221.7,100.6 224.0,100.4 226.3,100.2 228.5,100.1 230.8,99.9 233.1,99.8 235.3,99.6 237.6,99.5 239.9,99.4 242.1,99.2 244.4,99.1 246.7,99.0 248.9,98.9 251.2,98.8 253.5,98.7 255.7,98.6 258.0,98.5 260.3,98.4 262.5,98.3 264.8,98.2 267.1,98.2 269.3,98.1 271.6,98.0 273.9,97.9 276.1,97.9 278.4,97.8 280.7,97.7 282.9,97.7 285.2,97.6 287.5,97.6 289.7,97.5 292.0,97.5 294.3,97.4 296.5,97.4 298.8,97.3 301.1,97.3 303.3,97.2 305.6,97.2 307.9,97.2 310.1,97.1 312.4,97.1 314.7,97.1 316.9,97.0 319.2,97.0 321.5,97.0 323.7,96.9 326.0,96.9" fill="none" stroke="#c2410c" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="271.6" y="36.5" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(A)</text><text x="271.6" y="113.9" text-anchor="middle" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(B)</text><text x="90.3" y="36.5" text-anchor="middle" font-size="12" font-weight="700" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x<tspan baseline-shift="sub" font-size="9">max</tspan></text></svg>
:::

Valeurs lues sur les courbes (en mmol) :

| t (min) | 0 | 10  | 20  | 30  | 40  | 60  |
| ------- | - | --- | --- | --- | --- | --- |
| x (A)   | 0 | 4,3 | 5,5 | 5,9 | 6,0 | 6,0 |
| x (B)   | 0 | 2,3 | 3,2 | 3,7 | 3,9 | 4,0 |

::: exemple Distinguer un équilibre statique d'un équilibre chimique

1. Sur la figure, les deux courbes deviennent horizontales : x_f(A) = 6,0 mmol et x_f(B) = 4,0 mmol, et x_max = 6,0 mmol pour les deux.
2. Pour (A), τ_f = 6,0/6,0 = 1 : le peroxodisulfate limitant a disparu, l'état final est un équilibre statique.
3. Pour (B), τ_f = 4,0/6,0 ≈ 0,67 : n_f(acide) = n_f(alcool) = 6,0 − 4,0 = 2,0 mmol, et n_f(ester) = n_f(eau) = 4,0 mmol.
4. Dans (B), réactifs et produits coexistent avec des quantités constantes : c'est un état d'équilibre chimique.
5. Dans (A), les produits sont là mais plus aucun réactif limitant : la définition de l'équilibre chimique n'est pas remplie.

:::

::: piege
**Erreur : conclure « quantités constantes donc réactif épuisé ».** Dans (B), les quantités n'évoluent plus et pourtant 2,0 mmol d'acide et 2,0 mmol d'alcool subsistent. L'erreur tente parce que, pour une réaction totale, l'arrêt de la courbe signale bien la disparition d'un réactif ; mais une courbe qui se stabilise au-dessous de x_max signale seulement que la réaction est limitée, avec des réactifs encore présents.
:::

::: propriete
**Critère d'équilibre chimique** — Il faut deux conditions réunies : tous les réactifs et tous les produits présents, et des quantités qui ne changent plus sans intervention extérieure. Un système qui évolue, ou qui n'a plus de réactif limitant, n'est pas en équilibre chimique.
Cas limite : une intervention extérieure (ajouter un réactif, par exemple) fait varier les quantités ; la définition ne vaut que si l'on ne touche pas au système.
:::

::: verifie À toi : reconnaître un équilibre chimique
Un mélange d'acide, d'alcool, d'ester et d'eau contient, à 40 min comme à 60 min, 1,5 mmol d'acide, 1,5 mmol d'alcool, 3,5 mmol d'ester et 3,5 mmol d'eau. Peut-on parler d'équilibre chimique ?

---

Les quatre espèces, réactifs et produits, sont présentes, et leurs quantités n'ont pas changé entre 40 et 60 min : si personne n'est intervenu sur le mélange, c'est un état d'équilibre chimique.
:::

::: retenir
Équilibre chimique = réactifs et produits présents, quantités constantes sans intervention ; si τ_f = 1, c'est un équilibre statique, pas un équilibre chimique.
:::

## 🧮 La composition à l'équilibre dépend de la composition initiale

On prépare 1,00 L de deux solutions d'acide méthanoïque : S₁ à C₁ = 1,0·10⁻¹ mol·L⁻¹ (pH 2,38) et S₂ à C₂ = 1,0·10⁻² mol·L⁻¹ (pH 2,90). La solution S₂ est dix fois moins concentrée.
Les molécules d'acide réagissent-elles dans la même proportion dans S₁ et dans S₂ ?

::: definition
**Influence de la composition initiale** — Pour une même réaction limitée, la composition à l'équilibre dépend de la composition initiale : si on change les quantités initiales, on change aussi les quantités finales, donc le taux d'avancement final τ_f.
:::

| solution | C (mol·L⁻¹) | pH   | [H₃O⁺] (mol·L⁻¹) | x_f (mol) | τ_f      |
| -------- | ----------- | ---- | ---------------- | --------- | -------- |
| S₁       | 1,0·10⁻¹    | 2,38 | 4,2·10⁻³         | 4,2·10⁻³  | 4,2·10⁻² |
| S₂       | 1,0·10⁻²    | 2,90 | 1,3·10⁻³         | 1,3·10⁻³  | 1,3·10⁻¹ |

::: exemple Comparer deux dilutions

1. Dans S₁ : n₀ = C₁·V = 1,0·10⁻¹ × 1,00 = 0,10 mol, et [H₃O⁺] = 10^(−2,38) ≈ 4,2·10⁻³ mol·L⁻¹, donc x_f = 4,2·10⁻³ mol.
2. τ_f(S₁) = 4,2·10⁻³/0,10 = 4,2·10⁻² : 4,2 % des molécules ont réagi.
3. Dans S₂ : n₀ = 1,0·10⁻² mol et [H₃O⁺] = 10^(−2,90) ≈ 1,3·10⁻³ mol·L⁻¹, donc x_f = 1,3·10⁻³ mol.
4. τ_f(S₂) = 1,3·10⁻³/1,0·10⁻² = 1,3·10⁻¹ : 13 % ont réagi.
5. La solution la plus diluée a un τ_f trois fois plus grand : la dilution d'un acide faible fait augmenter τ_f.

:::

::: piege
**Erreur : comparer les quantités d'ions au lieu des taux.** S₂ a un pH plus élevé (2,90 contre 2,38) et un x_f plus petit (1,3·10⁻³ contre 4,2·10⁻³ mol) : on conclut à tort que l'acide y est moins ionisé. L'erreur tente parce qu'un pH plus élevé signifie moins d'ions ; mais S₂ contient aussi dix fois moins d'acide au départ, et la bonne comparaison est le taux τ_f = x_f/x_max, plus grand dans S₂.
:::

::: propriete
**Excès et dilution** — Deux constats : la dilution d'un acide faible dans l'eau augmente τ_f ; et un excès de l'un des réactifs augmente aussi τ_f (par rapport au mélange équimolaire, le réactif limitant gardant la même quantité). Exemple d'estérification : 0,150 mol d'acide et 0,150 mol d'alcool donnent x_f = 0,100 mol (τ_f ≈ 0,67), alors que 0,150 mol d'acide et 0,750 mol d'alcool donnent x_f = 0,142 mol (τ_f ≈ 0,95).
Cas limite : x_f peut baisser alors que τ_f monte, comme dans S₂ ; et, même avec cinq fois plus d'alcool, τ_f reste inférieur à 1 : l'excès rapproche de la réaction totale sans l'atteindre.
:::

::: verifie À toi : l'effet d'un excès
Pour CH₃COOH + HCOO⁻ ⇄ CH₃COO⁻ + HCOOH, un mélange de 0,050 mol de chaque réactif donne τ_f = 0,30. Un autre mélange de 0,050 mol de HCOO⁻ et 0,150 mol de CH₃COOH forme, à l'équilibre, 0,025 mol de HCOOH. Calculer τ_f et comparer.

---

HCOO⁻ est limitant (coefficients égaux à 1) : x_max = 0,050 mol. x_f = n(HCOOH) = 0,025 mol, donc τ_f = 0,025/0,050 = 0,50. C'est plus que 0,30 : l'excès de CH₃COOH fait augmenter τ_f.
:::

::: retenir
Pour une réaction limitée, τ_f dépend de la composition initiale : il augmente avec la dilution d'un acide faible et avec un excès de réactif, sans atteindre 1.
:::

## 🔬 À l'échelle des molécules : un équilibre dynamique

À l'équilibre, les quantités ne varient plus. Mais les molécules ne s'immobilisent pas : elles s'agitent sans cesse, se heurtent au hasard, et certains chocs, dits efficaces, rompent et créent des liaisons.
Si rien ne change à notre échelle, que font les deux réactions à l'échelle moléculaire ?

::: definition
**Équilibre dynamique** — On note v(1) la vitesse de la réaction directe et v(−1) celle de la réaction inverse, à l'échelle moléculaire. À l'équilibre, v(1) = v(−1) ≠ 0 : un équilibre chimique est un équilibre dynamique. La vitesse observée à notre échelle est v = |v(1) − v(−1)| (vitesses volumiques, en mol·L⁻¹·s⁻¹).
:::

::: figure Allure schématique (sans échelle) : v(1) diminue, v(−1) augmente, et les deux courbes se rejoignent sur un palier commun non nul
<svg viewBox="0 0 340 236"><title>Allure schématique de v(1) et v(−1) en fonction du temps</title><line x1="326.0" y1="26" x2="326.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="135.3" x2="326" y2="135.3" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="80.7" x2="326" y2="80.7" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="26.0" x2="326" y2="26.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="334.0" y="218.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t</text><text x="60.0" y="12.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v</text><line x1="300.0" y1="190" x2="300.0" y2="26" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><polyline points="54.0,44.2 56.3,47.7 58.5,50.9 60.8,54.0 63.1,56.9 65.3,59.7 67.6,62.3 69.9,64.8 72.1,67.1 74.4,69.3 76.7,71.4 78.9,73.4 81.2,75.3 83.5,77.0 85.7,78.7 88.0,80.3 90.3,81.8 92.5,83.2 94.8,84.5 97.1,85.8 99.3,87.0 101.6,88.1 103.9,89.2 106.1,90.2 108.4,91.2 110.7,92.1 112.9,93.0 115.2,93.8 117.5,94.5 119.7,95.3 122.0,96.0 124.3,96.6 126.5,97.2 128.8,97.8 131.1,98.4 133.3,98.9 135.6,99.4 137.9,99.8 140.1,100.3 142.4,100.7 144.7,101.1 146.9,101.5 149.2,101.8 151.5,102.1 153.7,102.5 156.0,102.8 158.3,103.0 160.5,103.3 162.8,103.6 165.1,103.8 167.3,104.0 169.6,104.2 171.9,104.5 174.1,104.6 176.4,104.8 178.7,105.0 180.9,105.2 183.2,105.3 185.5,105.5 187.7,105.6 190.0,105.7 192.3,105.8 194.5,106.0 196.8,106.1 199.1,106.2 201.3,106.3 203.6,106.4 205.9,106.5 208.1,106.5 210.4,106.6 212.7,106.7 214.9,106.8 217.2,106.8 219.5,106.9 221.7,107.0 224.0,107.0 226.3,107.1 228.5,107.1 230.8,107.2 233.1,107.2 235.3,107.3 237.6,107.3 239.9,107.3 242.1,107.4 244.4,107.4 246.7,107.4 248.9,107.5 251.2,107.5 253.5,107.5 255.7,107.5 258.0,107.6 260.3,107.6 262.5,107.6 264.8,107.6 267.1,107.7 269.3,107.7 271.6,107.7 273.9,107.7 276.1,107.7 278.4,107.7 280.7,107.8 282.9,107.8 285.2,107.8 287.5,107.8 289.7,107.8 292.0,107.8 294.3,107.8 296.5,107.8 298.8,107.8 301.1,107.9 303.3,107.9 305.6,107.9 307.9,107.9 310.1,107.9 312.4,107.9 314.7,107.9 316.9,107.9 319.2,107.9 321.5,107.9 323.7,107.9 326.0,107.9" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="54.0,190.0 56.3,186.9 58.5,183.9 60.8,181.1 63.1,178.3 65.3,175.7 67.6,173.1 69.9,170.6 72.1,168.3 74.4,166.0 76.7,163.8 78.9,161.7 81.2,159.7 83.5,157.7 85.7,155.9 88.0,154.1 90.3,152.3 92.5,150.6 94.8,149.0 97.1,147.5 99.3,146.0 101.6,144.6 103.9,143.2 106.1,141.9 108.4,140.6 110.7,139.3 112.9,138.2 115.2,137.0 117.5,135.9 119.7,134.9 122.0,133.9 124.3,132.9 126.5,131.9 128.8,131.0 131.1,130.2 133.3,129.3 135.6,128.5 137.9,127.8 140.1,127.0 142.4,126.3 144.7,125.6 146.9,124.9 149.2,124.3 151.5,123.7 153.7,123.1 156.0,122.5 158.3,122.0 160.5,121.5 162.8,120.9 165.1,120.5 167.3,120.0 169.6,119.5 171.9,119.1 174.1,118.7 176.4,118.3 178.7,117.9 180.9,117.5 183.2,117.2 185.5,116.8 187.7,116.5 190.0,116.2 192.3,115.9 194.5,115.6 196.8,115.3 199.1,115.0 201.3,114.7 203.6,114.5 205.9,114.2 208.1,114.0 210.4,113.8 212.7,113.6 214.9,113.3 217.2,113.1 219.5,112.9 221.7,112.8 224.0,112.6 226.3,112.4 228.5,112.2 230.8,112.1 233.1,111.9 235.3,111.8 237.6,111.6 239.9,111.5 242.1,111.4 244.4,111.2 246.7,111.1 248.9,111.0 251.2,110.9 253.5,110.8 255.7,110.7 258.0,110.6 260.3,110.5 262.5,110.4 264.8,110.3 267.1,110.2 269.3,110.1 271.6,110.0 273.9,110.0 276.1,109.9 278.4,109.8 280.7,109.8 282.9,109.7 285.2,109.6 287.5,109.6 289.7,109.5 292.0,109.4 294.3,109.4 296.5,109.3 298.8,109.3 301.1,109.2 303.3,109.2 305.6,109.1 307.9,109.1 310.1,109.1 312.4,109.0 314.7,109.0 316.9,108.9 319.2,108.9 321.5,108.9 323.7,108.8 326.0,108.8" fill="none" stroke="#c2410c" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="81.2" y="49.7" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v(1)</text><text x="117.5" y="160.8" text-anchor="start" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v(−1)</text><text x="321.5" y="91.6" text-anchor="end" font-size="12" font-weight="700" fill="#334155" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v(1) = v(−1) ≠ 0</text><text x="300.0" y="180.9" text-anchor="middle" font-size="12" font-weight="700" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">équilibre</text></svg>
:::

Sur la figure, v(−1) part de zéro (il n'y a pas encore de produits) tandis que v(1) part d'une valeur élevée ; quand elles se rejoignent, l'équilibre est atteint.

::: exemple Suivre v(1), v(−1) et v au cours de l'ionisation d'un acide

Les valeurs suivantes (en 10⁻⁵ mol·L⁻¹·s⁻¹) sont choisies pour illustrer, elles ne sont pas mesurées.

1. Au début, seul l'acide est présent : v(−1) = 0 et v(1) = 5,0, donc v = |5,0 − 0| = 5,0 : à notre échelle, la réaction directe se produit.
2. Plus tard, l'acide a diminué et les ions se sont formés : v(1) = 3,5 et v(−1) = 2,5, donc v = |3,5 − 2,5| = 1,0, plus faible : la réaction continue d'avancer, plus lentement.
3. À l'équilibre, v(1) = v(−1) = 3,0, donc v = |3,0 − 3,0| = 0 : la composition n'évolue plus.
4. Les deux vitesses valent encore 3,0, pas 0 : par seconde, la réaction directe fournit autant d'ions que la réaction inverse en consomme.
5. Sur une courbe x(t), la vitesse de la réaction dx/dt (divisée par V, elle devient une vitesse volumique, comparable à v(1) et v(−1)) est la pente de la tangente, calculée sur deux points A et B de cette tangente : v = (x_B − x_A)/(t_B − t_A). Avec A(0 ; 1,0) et B(40 ; 3,0) en mmol et min, v = 2,0/40 = 0,050 mmol·min⁻¹ ; au palier, la tangente est horizontale et la vitesse est nulle.

:::

::: piege
**Erreur : croire qu'à l'équilibre plus aucune réaction ne se produit.** La vitesse observée est nulle (v = 0), mais v(1) = v(−1) = 3,0·10⁻⁵ mol·L⁻¹·s⁻¹ ≠ 0 : les deux réactions se poursuivent. L'erreur tente parce que, à notre échelle, rien ne change et que v = 0 ; mais cette vitesse observée est la différence des deux vitesses moléculaires, et une différence nulle n'implique pas deux termes nuls.
:::

::: propriete
**Trois cas** — Si v(1) > v(−1), la composition évolue dans le sens direct ; si v(1) < v(−1), dans le sens inverse ; si v(1) = v(−1), le système est en équilibre.
Cas limite : à l'échelle macroscopique la vitesse est nulle et la composition invariable ; à l'échelle moléculaire, les deux réactions se produisent en même temps, en sens inverse, avec des vitesses égales et non nulles. Pour les réactions acide-base, l'équilibre est atteint très rapidement, mais d'autres réactions l'atteignent lentement.
:::

::: verifie À toi : lire les deux vitesses
À un instant, v(1) = 8,0·10⁻⁴ et v(−1) = 2,5·10⁻⁴ mol·L⁻¹·min⁻¹. Quelle réaction observe-t-on, et que vaut v ? Plus tard, v(1) = v(−1) = 3,0·10⁻⁴ : que vaut alors v ?

---

v(1) > v(−1) : on observe la réaction directe, avec v = |8,0·10⁻⁴ − 2,5·10⁻⁴| = 5,5·10⁻⁴ mol·L⁻¹·min⁻¹. Plus tard, v = |3,0·10⁻⁴ − 3,0·10⁻⁴| = 0 : le système est à l'équilibre, alors que les deux réactions continuent à 3,0·10⁻⁴ mol·L⁻¹·min⁻¹.
:::

::: retenir
À l'équilibre, v(1) = v(−1) ≠ 0 à l'échelle moléculaire, alors que la vitesse observée v = |v(1) − v(−1)| est nulle.
:::

## 🍯 Estérification et hydrolyse : un équilibre bien réel

On mélange 8,6 mL d'acide éthanoïque pur (ρ = 1,05 g·mL⁻¹, M = 60 g·mol⁻¹) et 8,7 mL d'éthanol pur (ρ = 0,79 g·mL⁻¹, M = 46 g·mol⁻¹), avec un peu d'acide sulfurique, et on chauffe. Au bout d'environ cent minutes, les quantités ne varient plus.
Les deux réactifs ont-ils disparu, et que se passe-t-il si l'on part de l'ester et de l'eau ?

::: definition
**Estérification et hydrolyse** — L'estérification est la réaction entre un acide carboxylique et un alcool, qui donne un ester R−CO₂R' et de l'eau : RCO₂H + R'OH ⇄ RCO₂R' + H₂O. L'hydrolyse de l'ester est sa réaction inverse. Ces deux réactions sont lentes et limitées : elles se limitent mutuellement et conduisent à un équilibre chimique, l'équilibre estérification-hydrolyse.
:::

::: figure Quantité d'ester en fonction du temps : en partant de l'acide et de l'alcool la courbe monte, en partant de l'ester et de l'eau elle descend, et les deux se rejoignent sur la ligne pointillée à 100 mmol
<svg viewBox="0 0 340 236"><title>n(ester) en fonction du temps pour deux mélanges de départ</title><line x1="108.4" y1="26" x2="108.4" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="162.8" y1="26" x2="162.8" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="217.2" y1="26" x2="217.2" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="271.6" y1="26" x2="271.6" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326.0" y1="26" x2="326.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="164.4" x2="326" y2="164.4" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="138.8" x2="326" y2="138.8" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="113.1" x2="326" y2="113.1" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="87.5" x2="326" y2="87.5" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="61.9" x2="326" y2="61.9" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="36.2" x2="326" y2="36.2" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="54.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="108.4" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="162.8" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="217.2" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><text x="271.6" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><text x="326.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">100</text><text x="48.0" y="194.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="48.0" y="142.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">50</text><text x="48.0" y="91.5" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">100</text><text x="48.0" y="40.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">150</text><text x="334.0" y="218.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (min)</text><text x="60.0" y="12.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">n(ester) (mmol)</text><line x1="54" y1="87.5" x2="326" y2="87.5" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><polyline points="54.0,190.0 56.3,185.8 58.5,181.8 60.8,178.0 63.1,174.3 65.3,170.7 67.6,167.3 69.9,164.1 72.1,160.9 74.4,157.9 76.7,155.1 78.9,152.3 81.2,149.7 83.5,147.1 85.7,144.7 88.0,142.4 90.3,140.1 92.5,138.0 94.8,135.9 97.1,133.9 99.3,132.0 101.6,130.2 103.9,128.5 106.1,126.8 108.4,125.2 110.7,123.7 112.9,122.2 115.2,120.8 117.5,119.4 119.7,118.1 122.0,116.9 124.3,115.7 126.5,114.5 128.8,113.4 131.1,112.4 133.3,111.3 135.6,110.4 137.9,109.4 140.1,108.5 142.4,107.7 144.7,106.9 146.9,106.1 149.2,105.3 151.5,104.6 153.7,103.9 156.0,103.2 158.3,102.6 160.5,102.0 162.8,101.4 165.1,100.8 167.3,100.3 169.6,99.7 171.9,99.2 174.1,98.8 176.4,98.3 178.7,97.9 180.9,97.4 183.2,97.0 185.5,96.6 187.7,96.3 190.0,95.9 192.3,95.6 194.5,95.2 196.8,94.9 199.1,94.6 201.3,94.3 203.6,94.1 205.9,93.8 208.1,93.5 210.4,93.3 212.7,93.0 214.9,92.8 217.2,92.6 219.5,92.4 221.7,92.2 224.0,92.0 226.3,91.8 228.5,91.6 230.8,91.5 233.1,91.3 235.3,91.2 237.6,91.0 239.9,90.9 242.1,90.7 244.4,90.6 246.7,90.5 248.9,90.3 251.2,90.2 253.5,90.1 255.7,90.0 258.0,89.9 260.3,89.8 262.5,89.7 264.8,89.6 267.1,89.5 269.3,89.5 271.6,89.4 273.9,89.3 276.1,89.2 278.4,89.2 280.7,89.1 282.9,89.0 285.2,89.0 287.5,88.9 289.7,88.8 292.0,88.8 294.3,88.7 296.5,88.7 298.8,88.6 301.1,88.6 303.3,88.5 305.6,88.5 307.9,88.5 310.1,88.4 312.4,88.4 314.7,88.4 316.9,88.3 319.2,88.3 321.5,88.3 323.7,88.2 326.0,88.2" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="54.0,36.2 56.3,38.3 58.5,40.3 60.8,42.3 63.1,44.1 65.3,45.9 67.6,47.6 69.9,49.2 72.1,50.8 74.4,52.3 76.7,53.7 78.9,55.1 81.2,56.4 83.5,57.7 85.7,58.9 88.0,60.1 90.3,61.2 92.5,62.3 94.8,63.3 97.1,64.3 99.3,65.2 101.6,66.1 103.9,67.0 106.1,67.8 108.4,68.6 110.7,69.4 112.9,70.2 115.2,70.9 117.5,71.5 119.7,72.2 122.0,72.8 124.3,73.4 126.5,74.0 128.8,74.5 131.1,75.1 133.3,75.6 135.6,76.1 137.9,76.5 140.1,77.0 142.4,77.4 144.7,77.8 146.9,78.2 149.2,78.6 151.5,79.0 153.7,79.3 156.0,79.6 158.3,80.0 160.5,80.3 162.8,80.6 165.1,80.8 167.3,81.1 169.6,81.4 171.9,81.6 174.1,81.9 176.4,82.1 178.7,82.3 180.9,82.5 183.2,82.7 185.5,82.9 187.7,83.1 190.0,83.3 192.3,83.5 194.5,83.6 196.8,83.8 199.1,83.9 201.3,84.1 203.6,84.2 205.9,84.4 208.1,84.5 210.4,84.6 212.7,84.7 214.9,84.8 217.2,84.9 219.5,85.1 221.7,85.2 224.0,85.2 226.3,85.3 228.5,85.4 230.8,85.5 233.1,85.6 235.3,85.7 237.6,85.7 239.9,85.8 242.1,85.9 244.4,86.0 246.7,86.0 248.9,86.1 251.2,86.1 253.5,86.2 255.7,86.2 258.0,86.3 260.3,86.3 262.5,86.4 264.8,86.4 267.1,86.5 269.3,86.5 271.6,86.6 273.9,86.6 276.1,86.6 278.4,86.7 280.7,86.7 282.9,86.7 285.2,86.8 287.5,86.8 289.7,86.8 292.0,86.9 294.3,86.9 296.5,86.9 298.8,86.9 301.1,87.0 303.3,87.0 305.6,87.0 307.9,87.0 310.1,87.0 312.4,87.1 314.7,87.1 316.9,87.1 319.2,87.1 321.5,87.1 323.7,87.1 326.0,87.2" fill="none" stroke="#c2410c" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="244.4" y="130.6" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">acide + alcool</text><text x="217.2" y="50.6" text-anchor="middle" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ester + eau</text></svg>
:::

Valeurs lues sur les courbes, n(ester) en mmol :

| t (min)                | 0   | 20  | 40  | 60  | 80  | 100 |
| ---------------------- | --- | --- | --- | --- | --- | --- |
| acide + alcool         | 0   | 63  | 86  | 95  | 98  | 99  |
| ester + eau            | 150 | 118 | 107 | 102 | 101 | 100 |

::: exemple Étudier l'estérification puis l'hydrolyse

1. n(acide) = ρ·V/M = 1,05 × 8,6/60 ≈ 0,150 mol et n(alcool) = 0,79 × 8,7/46 ≈ 0,150 mol : un mélange équimolaire, donc x_max = 0,150 mol.
2. Sur la courbe qui monte, le palier est à n(ester) = 100 mmol, donc x_f = 0,100 mol et τ_f = 0,100/0,150 ≈ 0,67 : estérification limitée.
3. Composition finale : n(ester) = n(eau) = 0,100 mol et n(acide) = n(alcool) = 0,150 − 0,100 = 0,050 mol.
4. En partant de 0,150 mol d'ester et 0,150 mol d'eau, la courbe descend jusqu'au même palier à 100 mmol : x_f = 0,150 − 0,100 = 0,050 mol, donc τ_f = 0,050/0,150 ≈ 0,33.
5. L'état final est identique, avec n(ester) = n(eau) = 0,100 mol et n(acide) = n(alcool) = 0,050 mol. Le rapport K = n(ester)·n(eau) / (n(acide)·n(alcool)) = (0,100 × 0,100)/(0,050 × 0,050) = 4 : le volume se simplifie.

:::

::: piege
**Erreur : penser qu'un mélange équimolaire s'estérifie totalement.** Avec 0,150 mol de chaque réactif, on attend x_f = 0,150 mol, soit 0,150 mol d'ester. On en obtient 0,100 mol, et 0,050 mol de chaque réactif subsiste. L'erreur tente parce que, pour une réaction totale, des quantités stœchiométriques s'épuisent ensemble ; mais l'estérification est limitée, et la réaction inverse (l'hydrolyse) détruit l'ester formé.
:::

::: propriete
**Un seul équilibre, deux chemins** — Partant de l'acide et de l'alcool, ou de l'ester et de l'eau en quantités équimolaires, on atteint le même état d'équilibre. Les deux réactions étant inverses l'une de l'autre, on les écrit avec une double flèche : CH₃CO₂H + CH₃CH₂OH ⇄ CH₃CO₂CH₂CH₃ + H₂O.
Cas limite : pour ces mélanges équimolaires, τ_f(estérification) + τ_f(hydrolyse) = 0,67 + 0,33 = 1, car chacun des deux part de l'un des deux côtés du même état final.
:::

::: verifie À toi : un autre couple acide-alcool
On mélange 0,300 mol d'un acide carboxylique et 0,300 mol d'un alcool : à l'équilibre, on trouve 0,200 mol d'ester. Calculer τ_f et la composition finale.

---

x_max = 0,300 mol et x_f = n(ester) = 0,200 mol, donc τ_f = 0,200/0,300 ≈ 0,67. n(eau) = 0,200 mol et n(acide) = n(alcool) = 0,300 − 0,200 = 0,100 mol.
:::

::: retenir
Estérification et hydrolyse sont lentes, limitées et inverses l'une de l'autre : elles conduisent au même équilibre, par exemple τ_f ≈ 0,67 pour un mélange équimolaire d'acide et d'alcool.
:::

## 🧪 Suivre l'estérification par dosage

On ne peut pas lire l'avancement x directement dans un mélange qui chauffe. On prépare donc dix tubes identiques, chacun avec 5,0 mmol d'acide, 5,0 mmol d'alcool et quelques gouttes d'acide sulfurique, surmontés d'un réfrigérant à air. On les plonge ensemble dans un bain-marie bouillant, puis on en retire un à intervalles réguliers pour le doser.
Comment une simple soude permet-elle de remonter à x ?

::: definition
**Relation de dosage** — Chaque tube retiré est plongé dans l'eau glacée (trempe), ce qui bloque la réaction ; l'acide restant est dosé par la soude de concentration C_B. Le tube témoin, non chauffé, donne le volume V_B0 de départ. La quantité d'acide disparu est n(acide)_disparu = (V_B0 − V_B)·C_B = x.
:::

| rôle                       | pourquoi                                                                           |
| -------------------------- | ---------------------------------------------------------------------------------- |
| bain-marie bouillant       | la température est un facteur cinétique : elle accélère une réaction lente         |
| acide sulfurique           | il joue le rôle de catalyseur : il accélère la réaction                            |
| réfrigérant à air          | il condense les vapeurs de réactifs et de produits qui s'échappent                 |
| eau glacée (trempe)        | elle bloque la réaction pendant le dosage                                          |

Avec C_B = 0,500 mol·L⁻¹, le tube témoin a demandé V_B0 = 14,0 mL, et les autres tubes ont donné :

| t (min)  | 10   | 20  | 30  | 40  | 60  | 80  | 100 |
| -------- | ---- | --- | --- | --- | --- | --- | --- |
| V_B (mL) | 10,8 | 9,2 | 8,3 | 7,8 | 7,4 | 7,3 | 7,3 |

::: exemple Passer de V_B à x puis à τ_f

1. Pour t = 20 min : x = (V_B0 − V_B)·C_B = (14,0 − 9,2)·10⁻³ × 0,500 = 2,4·10⁻³ mol, car chaque mole d'acide disparu fait baisser la quantité de soude nécessaire d'une mole.
2. x_max = 5,0·10⁻³ mol (mélange équimolaire, coefficients égaux à 1). À 20 min, x/x_max = 0,48 : ce n'est pas τ_f, car la réaction n'est pas terminée.
3. V_B ne change plus entre 80 et 100 min (7,3 mL) : c'est le palier. x_f = (14,0 − 7,3)·10⁻³ × 0,500 = 3,35·10⁻³ mol.
4. τ_f = 3,35·10⁻³/5,0·10⁻³ ≈ 0,67.
5. Composition à l'équilibre : n(ester) = n(eau) = 3,35 mmol et n(acide) = n(alcool) = 5,0 − 3,35 = 1,65 mmol.

:::

::: piege
**Erreur : prendre V_B0 = n₀/C_B.** On croit que le tube témoin demande 5,0·10⁻³/0,500 = 10,0 mL, et on trouve x_f = (10,0 − 7,3)·10⁻³ × 0,500 = 1,35·10⁻³ mol au lieu de 3,35·10⁻³ mol. L'erreur tente parce que la soude dose « l'acide » ; mais elle dose aussi l'acide sulfurique du catalyseur, présent en quantité identique dans tous les tubes : le volume V_B0 = 14,0 mL est mesuré, et seule la différence V_B0 − V_B ne dépend plus du catalyseur.
:::

::: propriete
**Méthode du dosage** — Choisir t = 0 quand on plonge les tubes dans le bain chaud, car l'estérification est très lente à température ambiante ; arrêter chaque réaction par la trempe ; calculer x = (V_B0 − V_B)·C_B ; tracer x en fonction de t ; lire x_f quand x cesse de croître, puis τ_f = x_f/x_max.
Cas limite : le tube témoin n'est pas chauffé, donc V_B0 correspond à x = 0 : c'est le point de départ de la courbe, et une valeur V_B supérieure à V_B0 ne peut venir que d'une erreur de manipulation.
:::

::: verifie À toi : un autre dosage
Un tube témoin demande V_B0 = 12,0 mL de soude à 0,250 mol·L⁻¹. Un tube retiré à 30 min en demande V_B = 8,4 mL, et le mélange initial contient 2,0·10⁻³ mol d'acide et d'alcool. Calculer x puis x/x_max.

---

x = (12,0 − 8,4)·10⁻³ × 0,250 = 9,0·10⁻⁴ mol. Le mélange est équimolaire à coefficients 1 : x_max = 2,0·10⁻³ mol, donc x/x_max = 0,45 à 30 min.
:::

::: retenir
x = (V_B0 − V_B)·C_B : le tube témoin donne V_B0, la trempe bloque la réaction, et le palier de x(t) donne x_f puis τ_f = x_f/x_max.
:::

> 🏆 Tu sais désormais lire un équilibre : un taux d'avancement final inférieur à 1, des quantités qui ne bougent plus, et deux réactions qui continuent pourtant, à vitesses égales. Le chapitre suivant mettra un nombre sur cet équilibre.
