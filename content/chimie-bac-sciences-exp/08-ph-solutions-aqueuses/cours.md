# 🧪 pH des solutions aqueuses — du nombre mesuré à la concentration

> 💡 «Un pH-mètre ne donne qu'un nombre : l'art du chimiste est d'en tirer la concentration, et de savoir si l'acide ou la base est forte ou faible.»

L'eau d'une piscine doit rester entre pH 7,0 et 7,4 pour être douce et bien désinfectée : comment vérifier ce nombre, et comment l'ajuster, si l'on ne sait pas le relier à ce que contient l'eau ? Huit notions donnent la réponse : la définition du pH, la nature acide, neutre ou basique et la température, le pH d'un acide fort, celui d'une base forte, d'un acide faible, d'une base faible, le pH d'un sel dissous, et l'effet d'une dilution. On suppose acquis l'ionisation propre de l'eau (chapitre 5), le taux d'avancement final τ_f (chapitre 4), les couples acide/base, Kₐ et pKₐ (chapitre 7) et le logarithme décimal.

## 🔢 Le pH : un nombre pour une concentration

Le technicien de la piscine lit 7,2 sur son pH-mètre. Dans l'eau, ce sont pourtant les ions H₃O⁺ qui agissent, et leur concentration s'écrit avec des puissances de 10 négatives peu pratiques à comparer.
Comment passer du pH à la concentration, et inversement, et que devient la concentration en ions OH⁻ ?

::: definition
**pH** — Grandeur sans unité, positive, liée à la concentration des ions hydronium H₃O⁺ d'une solution aqueuse : pH = −log [H₃O⁺], ce qui équivaut à [H₃O⁺] = 10⁻ᵖᴴ (en mol·L⁻¹). La relation n'est pas valable au-delà de 10⁻¹ mol·L⁻¹.
Dans toute solution aqueuse, [H₃O⁺][OH⁻] = Kₑ, avec Kₑ = 10⁻¹⁴ à 25 °C, soit pKₑ = −log Kₑ = 14. On en tire [OH⁻] = Kₑ/[H₃O⁺] = 10^(pH − pKₑ).
On mesure le pH avec un papier indicateur universel, qui n'en donne qu'une valeur approchée, ou avec un pH-mètre préalablement étalonné, qui l'affiche au centième d'unité de pH.
:::

Le tableau ci-dessous relie le pH aux deux concentrations, à 25 °C :

| pH  | [H₃O⁺] (mol·L⁻¹) | [OH⁻] (mol·L⁻¹) |
| --- | ---------------- | --------------- |
| 2   | 10⁻²             | 10⁻¹²           |
| 4   | 10⁻⁴             | 10⁻¹⁰           |
| 7   | 10⁻⁷             | 10⁻⁷            |
| 10  | 10⁻¹⁰            | 10⁻⁴            |
| 12  | 10⁻¹²            | 10⁻²            |

Chaque ligne se lit dans les deux sens : quand le pH augmente de 1, [H₃O⁺] est divisée par 10 et [OH⁻] multipliée par 10, et leur produit reste égal à Kₑ = 10⁻¹⁴.

::: exemple Passer du pH aux concentrations, puis des concentrations au pH

1. L'eau de la piscine a pour pH 7,2, donc [H₃O⁺] = 10^(−7,2) = 10⁻⁸ × 10^(0,8) = 6,3·10⁻⁸ mol·L⁻¹ : c'est la définition lue à l'envers.
2. Le produit ionique donne [OH⁻] = Kₑ/[H₃O⁺] = 10⁻¹⁴ / 6,3·10⁻⁸ = 1,6·10⁻⁷ mol·L⁻¹.
3. Une autre solution a [OH⁻] = 5,0·10⁻³ mmol·L⁻¹. Le pH se définit avec des mol·L⁻¹ : [OH⁻] = 5,0·10⁻⁶ mol·L⁻¹, car 1 mmol = 10⁻³ mol.
4. Alors [H₃O⁺] = 10⁻¹⁴ / 5,0·10⁻⁶ = 2,0·10⁻⁹ mol·L⁻¹, car la définition du pH s'écrit avec [H₃O⁺].
5. Enfin pH = −log (2,0·10⁻⁹) = −(log 2,0 − 9) = 9 − 0,30 = 8,70, car log (a·10ᵇ) = log a + b.

:::

::: piege
**Erreur : calculer le pH avec la concentration en ions OH⁻.** Pour [OH⁻] = 10⁻³ mol·L⁻¹, on écrit pH = −log 10⁻³ = 3 et l'on déclare la solution acide. L'erreur tente parce que la formule « −log » est celle que l'on a sous les yeux ; mais le pH se définit avec [H₃O⁺] : ici [H₃O⁺] = 10⁻¹⁴/10⁻³ = 10⁻¹¹ mol·L⁻¹, donc pH = 11 et la solution est basique.
:::

::: propriete
**Conversion du pH et des concentrations** — À 25 °C, pH = −log [H₃O⁺], [H₃O⁺] = 10⁻ᵖᴴ et [OH⁻] = 10^(pH − 14). Outils du logarithme décimal : log (a·b) = log a + log b ; log (a/b) = log a − log b ; log 10ᵇ = b ; log 1 = 0 ; si log a = b, alors a = 10ᵇ.
Cas : pH = 5,5 donne [H₃O⁺] = 10^(−5,5) = 3,2·10⁻⁶ mol·L⁻¹ ; [OH⁻] = 3,2·10⁻⁹ mol·L⁻¹.
Cas limite : pour une solution plus concentrée que 10⁻¹ mol·L⁻¹, la définition du pH n'est plus valable.
:::

::: verifie À toi : de la concentration au pH
Une solution a pour concentration [H₃O⁺] = 2,5·10⁻⁴ mol·L⁻¹. Quel est son pH ?

---

pH = −log (2,5·10⁻⁴) = −(log 2,5 − 4), car log (a·10ᵇ) = log a + b. Avec log 2,5 = 0,40, on obtient pH = 4 − 0,40 = 3,60.
:::

::: retenir
Le pH vaut −log [H₃O⁺], sans unité ; on retrouve [H₃O⁺] = 10⁻ᵖᴴ et [OH⁻] = Kₑ/[H₃O⁺] = 10^(pH − 14) à 25 °C, avec des concentrations en mol·L⁻¹.
:::

## ⚖️ Acide, neutre ou basique : la frontière est à ½ pKₑ

On chauffe de l'eau pure à 60 °C : le pH-mètre affiche 6,5. Faut-il la déclarer acide, puisque 6,5 est inférieur à 7 ? Une eau pure, qui ne contient rien d'autre que de l'eau, peut-elle être acide ?
Comment trancher la nature d'une solution quand la température change ?

::: definition
**Solution neutre, acide, basique** — Une solution est neutre si [H₃O⁺] = [OH⁻], acide si [H₃O⁺] > [OH⁻], basique si [OH⁻] > [H₃O⁺].
Comme [H₃O⁺][OH⁻] = Kₑ, une solution neutre vérifie [H₃O⁺] = √Kₑ, soit pH = ½ pKₑ.
:::

::: figure Échelle de pH à 25 °C : la frontière entre acide et basique est à ½ pKₑ = 7 ; HCl et NaOH à 10⁻² mol·L⁻¹ y sont placés à pH 2 et 12 (valeurs justifiées plus loin)
<svg viewBox="0 0 340 150"><title>Échelle de pH à 25 °C : acide, neutre, basique</title><rect x="20" y="70" width="150" height="26" fill="#d97706" fill-opacity="0.18"/><rect x="170" y="70" width="150" height="26" fill="#2563eb" fill-opacity="0.18"/><rect x="20" y="70" width="300" height="26" fill="none" stroke="#0f172a" stroke-width="1.6"/><line x1="20" y1="96" x2="20" y2="101" stroke="#0f172a" stroke-width="1.2"/><text x="20" y="114" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="41.4286" y1="96" x2="41.4286" y2="101" stroke="#0f172a" stroke-width="1.2"/><line x1="62.8571" y1="96" x2="62.8571" y2="101" stroke="#0f172a" stroke-width="1.2"/><text x="62.8571" y="114" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="84.2857" y1="96" x2="84.2857" y2="101" stroke="#0f172a" stroke-width="1.2"/><line x1="105.714" y1="96" x2="105.714" y2="101" stroke="#0f172a" stroke-width="1.2"/><text x="105.714" y="114" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="127.143" y1="96" x2="127.143" y2="101" stroke="#0f172a" stroke-width="1.2"/><line x1="148.571" y1="96" x2="148.571" y2="101" stroke="#0f172a" stroke-width="1.2"/><text x="148.571" y="114" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="170" y1="96" x2="170" y2="101" stroke="#0f172a" stroke-width="1.2"/><line x1="191.429" y1="96" x2="191.429" y2="101" stroke="#0f172a" stroke-width="1.2"/><text x="191.429" y="114" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="212.857" y1="96" x2="212.857" y2="101" stroke="#0f172a" stroke-width="1.2"/><line x1="234.286" y1="96" x2="234.286" y2="101" stroke="#0f172a" stroke-width="1.2"/><text x="234.286" y="114" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="255.714" y1="96" x2="255.714" y2="101" stroke="#0f172a" stroke-width="1.2"/><line x1="277.143" y1="96" x2="277.143" y2="101" stroke="#0f172a" stroke-width="1.2"/><text x="277.143" y="114" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12</text><line x1="298.571" y1="96" x2="298.571" y2="101" stroke="#0f172a" stroke-width="1.2"/><line x1="320" y1="96" x2="320" y2="101" stroke="#0f172a" stroke-width="1.2"/><text x="320" y="114" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">14</text><line x1="170" y1="44" x2="170" y2="96" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="4 3"/><text x="170" y="38" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">neutre</text><text x="95" y="87" text-anchor="middle" font-size="11" font-weight="700" fill="#92400e" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">acide</text><text x="245" y="87" text-anchor="middle" font-size="11" font-weight="700" fill="#1e40af" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">basique</text><polygon points="62.9,68 57.9,58 67.9,58" fill="#0f6e56"/><text x="62.8571" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">HCl 10⁻² mol·L⁻¹</text><polygon points="277.1,68 272.1,58 282.1,58" fill="#0f6e56"/><text x="277.143" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">NaOH 10⁻² mol·L⁻¹</text><text x="170" y="134" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pH = ½ pKₑ = 7</text><text x="330" y="126" text-anchor="end" font-size="11" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pH</text></svg>
:::

Cette frontière dépend de pKₑ, donc de la température :

| température | pKₑ  | pH de la solution neutre (½ pKₑ) |
| ----------- | ---- | -------------------------------- |
| 8 °C        | 14,6 | 7,3                              |
| 25 °C       | 14   | 7                                |
| 60 °C       | 13   | 6,5                              |

Sur l'échelle, la frontière est à 7 uniquement parce que pKₑ = 14 à 25 °C ; le tableau montre qu'elle se déplace avec la température.

::: exemple Une même mesure, deux natures

1. Une solution a pour pH 6,7. À 25 °C, la frontière est à ½ pKₑ = 7 et 6,7 < 7 : la solution est acide.
2. À 60 °C, pKₑ = 13 et la frontière est à 6,5. Comme 6,7 > 6,5, la solution est basique.
3. On le vérifie avec les concentrations : [H₃O⁺] = 10^(−6,7) = 2,0·10⁻⁷ mol·L⁻¹ et [OH⁻] = 10^(6,7 − 13) = 5,0·10⁻⁷ mol·L⁻¹, donc [OH⁻] > [H₃O⁺].
4. L'eau pure vérifie [H₃O⁺] = [OH⁻] à toute température : elle est neutre à 60 °C, avec pH = 6,5, alors que 6,5 < 7.

:::

::: piege
**Erreur : décréter « pH inférieur à 7, donc acide » à toute température.** On conclut que l'eau pure à 60 °C, de pH 6,5, est acide. L'erreur tente parce que 7 est la valeur retenue à 25 °C ; mais le seuil est ½ pKₑ, soit 6,5 à 60 °C : l'eau pure y est neutre, avec [H₃O⁺] = [OH⁻].
:::

::: propriete
**Nature et pH** — À toute température, une solution est neutre si pH = ½ pKₑ, acide si pH < ½ pKₑ, basique si pH > ½ pKₑ. À 25 °C, le seuil est 7.
Cas : à 8 °C, pKₑ = 14,6 : une solution de pH 7,1 est acide, car 7,1 < 7,3.
Cas limite : l'eau pure est neutre à toute température ; seul son pH change (7,3 à 8 °C, 6,5 à 60 °C).
:::

::: verifie À toi : l'eau froide
À 8 °C, pKₑ = 14,6. Quel est le pH de l'eau pure ? Une solution de pH 7,1 est-elle acide, neutre ou basique ?

---

L'eau pure est neutre : pH = ½ pKₑ = 7,3. La solution de pH 7,1 est inférieure à ce seuil de 7,3, elle est donc acide, même si 7,1 est proche de 7.
:::

::: retenir
Neutre : pH = ½ pKₑ ; acide : pH < ½ pKₑ ; basique : pH > ½ pKₑ. Le seuil vaut 7 à 25 °C seulement ; l'eau pure est neutre à toute température.
:::

## 💥 L'acide fort : le pH se lit sur la concentration

On plonge un pH-mètre dans des solutions de chlorure d'hydrogène (acide chlorhydrique) de concentration C = 5·10⁻³, 2·10⁻³ et 10⁻⁴ mol·L⁻¹ : il affiche 2,30 ; 2,70 ; 4,00. Les nombres semblent liés à C.
Quelle relation lie le pH d'un acide de ce type à sa concentration ?

::: definition
**Acide fort** — Un acide fort réagit pratiquement totalement avec l'eau : HCl + H₂O → H₃O⁺ + Cl⁻. Pour un monoacide fort de concentration C, la réaction apporte [H₃O⁺] = C, aux ions de l'ionisation propre de l'eau près.
:::

Le tableau confronte les mesures à −log C et au terme dû à l'eau :

| C (mol·L⁻¹)               | 5·10⁻³  | 2·10⁻³  | 10⁻⁴  |
| ------------------------- | ------- | ------- | ----- |
| pH mesuré                 | 2,30    | 2,70    | 4,00  |
| −log C                    | 2,30    | 2,70    | 4,00  |
| [OH⁻] = 10^(pH − 14), eau | 2·10⁻¹² | 5·10⁻¹² | 10⁻¹⁰ |

Les deux premières lignes sont identiques : le pH vaut −log C. La dernière ligne montre pourquoi : les ions de l'eau, 10⁻¹² à 10⁻¹⁰ mol·L⁻¹, pèsent très peu devant C.

::: exemple Du pH à la concentration, dans les deux sens

1. Avec C = 5·10⁻³ mol·L⁻¹, la réaction étant totale, [H₃O⁺] = C = 5·10⁻³ mol·L⁻¹ : une mole d'acide donne une mole d'ions H₃O⁺.
2. Les ions de l'eau valent [OH⁻] = 10^(2,30 − 14) = 2,0·10⁻¹² mol·L⁻¹, soit 4·10⁻¹⁰ fois [H₃O⁺] : c'est inférieur à 0,05, donc négligeable (on néglige x devant y quand x/y ≤ 0,05).
3. Alors pH = −log C = −log (5·10⁻³) = 3 − 0,70 = 2,30 : la mesure est retrouvée.
4. Dans l'autre sens, un pH de 3,4 donne C = 10^(−3,4) = 4,0·10⁻⁴ mol·L⁻¹, car C = 10⁻ᵖᴴ.

:::

::: piege
**Erreur : appliquer pH = −log C à n'importe quel acide.** Pour de l'acide éthanoïque à 10⁻² mol·L⁻¹, on calcule pH = −log 10⁻² = 2,00, alors que le pH-mètre affiche 3,40. L'erreur tente parce que la formule du cadre est courte ; mais elle suppose [H₃O⁺] = C, donc une réaction totale. L'acide éthanoïque, qui réagit peu avec l'eau, relève des acides faibles, notion suivante.
:::

::: propriete
**pH d'un acide fort** — Pour un monoacide fort de concentration C, lorsque les ions de l'eau sont négligeables, pH = −log C et C = 10⁻ᵖᴴ. La condition est pH < 6 (soit C > 10⁻⁶ mol·L⁻¹ environ).
Cas : pour tout monoacide fort, le raisonnement est le même qu'avec HCl.
Cas limite : dans une solution extrêmement diluée (pH > 6), les ions de l'eau ne sont plus négligeables et la relation n'est plus valable ; ce cas est hors programme.
:::

::: verifie À toi : un autre acide fort
Une solution d'acide chlorhydrique a pour concentration C = 4,0·10⁻³ mol·L⁻¹. Quel est son pH ?

---

L'acide est fort et la solution est assez concentrée (C > 10⁻⁶ mol·L⁻¹) : pH = −log C = −log (4,0·10⁻³) = 3 − log 4,0 = 3 − 0,60 = 2,40. On retrouve aussi que pH < 6.
:::

::: retenir
Pour un monoacide fort de concentration C avec pH < 6 : pH = −log C et C = 10⁻ᵖᴴ.
:::

## 🧴 La base forte : le pH grimpe avec la concentration

On plonge le pH-mètre dans des solutions d'hydroxyde de sodium de concentration C = 10⁻², 5·10⁻³ et 2·10⁻⁴ mol·L⁻¹ : il affiche 12,00 ; 11,70 ; 10,30. Cette fois, le pH augmente avec C, à l'inverse d'un acide.
Quelle relation lie ces pH à C ?

::: definition
**Base forte** — Une base forte réagit pratiquement totalement avec l'eau ; l'hydroxyde de sodium se dissocie totalement : NaOH → Na⁺ + OH⁻. Pour une monobase forte de concentration C, la réaction apporte [OH⁻] = C, aux ions de l'ionisation propre de l'eau près.
:::

Les mesures se traduisent en concentrations en ions OH⁻ et H₃O⁺ :

| C (mol·L⁻¹)          | 10⁻²  | 5·10⁻³  | 2·10⁻⁴  |
| -------------------- | ----- | ------- | ------- |
| pH mesuré            | 12,00 | 11,70   | 10,30   |
| [OH⁻] = 10^(pH − 14) | 10⁻²  | 5·10⁻³  | 2·10⁻⁴  |
| [H₃O⁺] = 10⁻ᵖᴴ, eau  | 10⁻¹² | 2·10⁻¹² | 5·10⁻¹¹ |

La ligne [OH⁻] reprend exactement la ligne C : [OH⁻] = C. Les ions H₃O⁺, tous issus de l'eau, sont négligeables devant eux.

::: exemple Du pH à la concentration, dans les deux sens

1. Avec C = 5·10⁻³ mol·L⁻¹, la réaction NaOH → Na⁺ + OH⁻ est totale et Na⁺ ne réagit pas, donc [OH⁻] = C = 5·10⁻³ mol·L⁻¹.
2. Le produit ionique donne [H₃O⁺] = Kₑ/[OH⁻] = 10⁻¹⁴ / 5·10⁻³ = 2,0·10⁻¹² mol·L⁻¹, très inférieure à [OH⁻] : les ions de l'eau sont négligeables.
3. Alors pH = −log (2,0·10⁻¹²) = 12 − 0,30 = 11,70 ; c'est aussi pH = 14 + log C = 14 − 2,30. La mesure est retrouvée.
4. Dans l'autre sens, un pH de 10,6 donne C = 10^(10,6 − 14) = 10^(−3,4) = 4,0·10⁻⁴ mol·L⁻¹, car [OH⁻] = 10^(pH − pKₑ) et [OH⁻] = C.

:::

::: piege
**Erreur : appliquer pH = −log C à une base forte.** Pour C = 5·10⁻³ mol·L⁻¹, on calcule pH = 2,30 et l'on obtient une solution acide à partir d'une base. L'erreur tente parce que la formule de l'acide fort est la première que l'on a apprise ; mais pour une base c'est [OH⁻] = C qui est connue : il faut passer par Kₑ, donc par pKₑ, et pH = 14 + log C = 11,70.
:::

::: propriete
**pH d'une base forte** — Pour une monobase forte de concentration C, lorsque les ions de l'eau sont négligeables, pH = pKₑ + log C et C = 10^(pH − pKₑ). La condition est pH > 8 (soit C > 10⁻⁶ mol·L⁻¹ environ).
Cas : à 25 °C, NaOH à 10⁻² mol·L⁻¹ a pour pH 14 − 2 = 12.
Cas limite : la relation dépend de la température par pKₑ ; à 60 °C, pKₑ = 13 et NaOH à 5·10⁻³ mol·L⁻¹ a pour pH 13 − 2,30 = 10,70.
:::

::: verifie À toi : une autre base forte
Une solution d'hydroxyde de sodium a pour concentration C = 2,5·10⁻² mol·L⁻¹, à 25 °C. Quel est son pH ?

---

La base est forte et le pH sera supérieur à 8 : pH = pKₑ + log C = 14 + log (2,5·10⁻²) = 14 + (0,40 − 2) = 14 − 1,60 = 12,40. Garder pKₑ = 14 évite de retrouver −log C, qui donnerait une valeur acide.
:::

::: retenir
Pour une monobase forte de concentration C avec pH > 8, à 25 °C : pH = 14 + log C et C = 10^(pH − 14).
:::

## 🐢 L'acide faible : la réaction avec l'eau est limitée

Une solution d'acide éthanoïque CH₃CO₂H à 10⁻² mol·L⁻¹ affiche 3,40 au pH-mètre, alors que l'acide chlorhydrique de même concentration affiche 2,00. Visiblement, l'acide éthanoïque libère bien moins d'ions H₃O⁺.
Quelle fraction de l'acide a réagi, et quelle relation lie le pH, C et Kₐ ?

::: definition
**Acide faible** — Un acide faible AH réagit de façon limitée avec l'eau : AH + H₂O ⇄ A⁻ + H₃O⁺, avec un taux d'avancement final τ_f = [A⁻]/C < 1. Le couple AH/A⁻ a pour constante d'acidité Kₐ = [H₃O⁺][A⁻]/[AH] à l'équilibre, et pKₐ = −log Kₐ. Un acide est dit faiblement ionisé si τ_f < 0,05.
:::

::: figure Part de l'acide ayant réagi avec l'eau, à C = 10⁻² mol·L⁻¹ : HCl a réagi en totalité, l'acide éthanoïque à 4 % environ (τ_f = [H₃O⁺]/C = 10^(−3,4)/10⁻²)
<svg viewBox="0 0 340 226"><title>Part des molécules d'acide ayant réagi avec l'eau : acide fort et acide faible à 10⁻² mol·L⁻¹</title><rect x="55" y="40" width="70" height="150" fill="#94a3b8" fill-opacity="0.25"/><rect x="55" y="40" width="70" height="150" fill="#0f6e56" fill-opacity="0.45"/><rect x="55" y="40" width="70" height="150" fill="none" stroke="#0f172a" stroke-width="1.6"/><text x="90" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">HCl</text><text x="90" y="32" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τ<tspan dy="3" font-size="8">f</tspan><tspan dy="-3"> = 1</tspan></text><rect x="205" y="40" width="70" height="150" fill="#94a3b8" fill-opacity="0.25"/><rect x="205" y="184" width="70" height="6" fill="#0f6e56" fill-opacity="0.45"/><rect x="205" y="40" width="70" height="150" fill="none" stroke="#0f172a" stroke-width="1.6"/><text x="240" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">CH₃CO₂H</text><text x="240" y="32" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τ<tspan dy="3" font-size="8">f</tspan><tspan dy="-3"> ≈ 0,04</tspan></text><text x="90" y="120" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ions</text><text x="90" y="136" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">H₃O⁺ + Cl⁻</text><text x="240" y="100" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">acide</text><text x="240" y="114" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">non réagi</text><line x1="275" y1="187" x2="285" y2="187" stroke="#0f6e56" stroke-width="1.4"/><text x="288" y="190" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ions</text></svg>
:::

La barre de HCl est entièrement colorée : τ_f = 1. Celle de l'acide éthanoïque l'est à 4 % seulement : le reste de l'acide est resté sous forme de molécules, d'où [H₃O⁺] bien plus petite que C.

::: exemple Établir la relation du pH et l'appliquer

1. Dans CH₃CO₂H + H₂O ⇄ CH₃CO₂⁻ + H₃O⁺, chaque ion CH₃CO₂⁻ formé accompagne un ion H₃O⁺ (ions de l'eau négligés) : [H₃O⁺] = [CH₃CO₂⁻] = τ_f·C et [CH₃CO₂H] = C(1 − τ_f).
2. La constante d'acidité devient Kₐ = [H₃O⁺]·τ_f/(1 − τ_f). Si τ_f < 0,05, on remplace 1 − τ_f par 1 : Kₐ = [H₃O⁺]·τ_f, donc τ_f = Kₐ/[H₃O⁺] = 10^(pH − pKₐ).
3. On reporte dans [H₃O⁺] = τ_f·C : 10⁻ᵖᴴ = C·10^(pH − pKₐ), soit C = 10^(pKₐ − 2pH) et pH = ½ (pKₐ − log C).
4. Application : C = 10⁻² mol·L⁻¹ et pKₐ = 4,75 donnent pH = ½ (4,75 + 2) = 3,375, soit environ 3,4 : la mesure est de 3,40.
5. Contrôle de l'hypothèse : τ_f = [H₃O⁺]/C = 10^(−3,40)/10⁻² = 4,0·10⁻² < 0,05 (la relation approchée 10^(pH − pKₐ) donne 4,5·10⁻², du même ordre), donc l'approximation était permise.

:::

::: piege
**Erreur : utiliser pH = ½ (pKₐ − log C) sans contrôler τ_f.** Pour l'acide éthanoïque à C = 10⁻⁴ mol·L⁻¹, on obtient pH = ½ (4,75 + 4) = 4,375 et l'on s'arrête, puisque ce pH est inférieur à 6. L'erreur tente parce que la formule est encadrée dans le cours ; mais elle suppose τ_f < 0,05, et ici τ_f = 10^(4,375 − 4,75) = 0,42, très au-dessus : l'acide n'est plus faiblement ionisé et la relation n'est pas utilisable.
:::

::: propriete
**pH d'un acide faible faiblement ionisé** — pH = ½ (pKₐ − log C), C = 10^(pKₐ − 2pH) et τ_f = 10^(pH − pKₐ). Deux conditions : les ions de l'eau sont négligeables (pH < 6) et τ_f < 0,05, c'est-à-dire pH < pKₐ − 1,3.
Cas : à même C, un pKₐ plus petit donne un pH plus bas : l'acide est plus fort.
Cas limite : si le contrôle donne τ_f ≥ 0,05, on ne peut pas utiliser la relation.
:::

::: verifie À toi : l'acide hypochloreux
L'acide hypochloreux HClO a pour pKₐ = 7,5. Quel est le pH d'une solution à C = 4,0·10⁻² mol·L⁻¹, et la relation est-elle utilisable ?

---

pH = ½ (pKₐ − log C) = ½ (7,5 + 1,40) = 4,45, car −log (4,0·10⁻²) = 2 − 0,60 = 1,40. Contrôle : τ_f = 10^(4,45 − 7,5) = 8,9·10⁻⁴ < 0,05 et pH < 6 : les deux conditions sont vérifiées, la relation est utilisable.
:::

::: retenir
Pour un acide faible faiblement ionisé (τ_f < 0,05, pH < 6) : pH = ½ (pKₐ − log C), τ_f = 10^(pH − pKₐ) ; à contrôler après le calcul.
:::

## 🧪 La base faible : les ions OH⁻ viennent d'une réaction limitée

L'éthanoate de sodium CH₃CO₂Na, à 5·10⁻³ mol·L⁻¹, donne 8,25 au pH-mètre : la solution est basique, alors qu'on n'a versé aucune « soude ».
D'où viennent les ions OH⁻, et comment calculer ce pH ?

::: definition
**Base faible** — Une base faible B réagit de façon limitée avec l'eau : B + H₂O ⇄ BH⁺ + OH⁻, avec un taux d'avancement final τ_f = [OH⁻]/C < 1. Son acide conjugué BH⁺ forme le couple BH⁺/B de constante d'acidité Kₐ, et la constante de la réaction de B avec l'eau, K_b, vérifie Kₐ·K_b = Kₑ.
:::

Pour l'ion éthanoate, pKₐ(CH₃CO₂H/CH₃CO₂⁻) = 4,75 et C = 5,0·10⁻³ mol·L⁻¹, la composition à l'équilibre est (calcul fait dans l'exemple ci-dessous) :

| espèce                                | CH₃CO₂⁻               | CH₃CO₂H          | OH⁻              |
| ------------------------------------- | --------------------- | ---------------- | ---------------- |
| concentration à l'équilibre (mol·L⁻¹) | C(1 − τ_f) ≈ 5,0·10⁻³ | τ_f·C = 1,7·10⁻⁶ | τ_f·C = 1,7·10⁻⁶ |

Les ions OH⁻ et l'acide CH₃CO₂H se forment en quantités égales, à raison de τ_f·C ; la base, elle, reste presque entière.

::: exemple Établir la relation du pH et l'appliquer

1. L'éthanoate de sodium se dissout totalement : CH₃CO₂Na → CH₃CO₂⁻ + Na⁺. L'ion Na⁺ ne réagit pas avec l'eau, donc [CH₃CO₂⁻] = C = 5,0·10⁻³ mol·L⁻¹ avant réaction.
2. L'ion éthanoate est la base faible du couple CH₃CO₂H/CH₃CO₂⁻ : CH₃CO₂⁻ + H₂O ⇄ CH₃CO₂H + OH⁻. Ses ions OH⁻ dominent ceux de l'eau si pH > 8, donc [OH⁻] = τ_f·C = 10^(pH − pKₑ).
3. Avec Kₐ·K_b = Kₑ et τ_f < 0,05, on trouve τ_f = 10^(pKₐ − pH). Alors 10^(pKₐ − pH)·C = 10^(pH − pKₑ), d'où C = 10^(2pH − pKₑ − pKₐ) et pH = ½ (pKₑ + pKₐ + log C).
4. Application : pH = ½ (14 + 4,75 + log 5,0·10⁻³) = ½ (18,75 − 2,30) = 8,22, proche des 8,25 mesurés.
5. Contrôle : pH > 8 et τ_f = 10^(4,75 − 8,22) = 3,4·10⁻⁴ < 0,05 ; ce qui donne bien τ_f·C = 1,7·10⁻⁶ mol·L⁻¹ dans le tableau.

:::

::: exemple Le sens inverse : de la mesure à la concentration

1. Une solution d'ammoniac NH₃ a pour pH 10,80 ; le couple NH₄⁺/NH₃ a pour pKₐ = 9,25. NH₃ est une base faible : on utilise C = 10^(2pH − pKₑ − pKₐ).
2. C = 10^(21,6 − 14 − 9,25) = 10^(−1,65) = 2,2·10⁻² mol·L⁻¹.
3. Contrôle : τ_f = 10^(9,25 − 10,80) = 2,8·10⁻² < 0,05 et pH > 8 : le résultat est recevable.

:::

::: piege
**Erreur : utiliser pour une base la formule de l'acide faible.** Pour l'éthanoate de sodium à 5,0·10⁻³ mol·L⁻¹, on calcule pH = ½ (4,75 − log 5,0·10⁻³) = 3,5 et l'on annonce une solution acide. L'erreur tente parce que les deux formules ont le même facteur ½ et le même pKₐ ; mais la base fabrique des ions OH⁻ : il faut ajouter pKₑ et log C, ce qui donne 8,22, une solution basique.
:::

::: propriete
**pH d'une base faible faiblement ionisée** — pH = ½ (pKₑ + pKₐ + log C), C = 10^(2pH − pKₑ − pKₐ) et τ_f = 10^(pKₐ − pH). Deux conditions : les ions de l'eau sont négligeables (pH > 8) et τ_f < 0,05, c'est-à-dire pH > pKₐ + 1,3.
Cas : à même C, plus le pKₐ du couple est grand, plus le pH est élevé : la base est plus forte.
Cas limite : si τ_f ≥ 0,05 au contrôle, la relation n'est pas utilisable.
:::

::: verifie À toi : l'ion cyanure
L'ion cyanure CN⁻ est la base du couple HCN/CN⁻ de pKₐ = 9,3. Quel est le pH d'une solution de cyanure de sodium à C = 5,0·10⁻² mol·L⁻¹, et la relation est-elle utilisable ?

---

CN⁻ est une base faible : pH = ½ (pKₑ + pKₐ + log C) = ½ (14 + 9,3 − 1,30) = 11,00, car log (5,0·10⁻²) = 0,70 − 2 = −1,30. Contrôle : pH > 8 et τ_f = 10^(9,3 − 11,00) = 2,0·10⁻² < 0,05, donc la relation est utilisable.
:::

::: retenir
Pour une base faible faiblement ionisée (τ_f < 0,05, pH > 8) : pH = ½ (pKₑ + pKₐ + log C), τ_f = 10^(pKₐ − pH) ; ne jamais reprendre la formule de l'acide.
:::

## 🧂 Les sels en solution : quel ion fait le pH ?

On dissout du chlorure d'ammonium NH₄Cl, 5,0·10⁻² mol·L⁻¹, dans de l'eau : c'est un simple sel, et pourtant le pH-mètre n'affiche pas la valeur de l'eau pure.
Quel ion réagit avec l'eau, et comment calculer ce pH ?

::: definition
**Ion inerte, ion acide, ion basique** — Un sel se dissout totalement en ses ions. Un ion qui ne réagit pas avec l'eau est inerte (Na⁺, Cl⁻). L'ion ammonium NH₄⁺ est un acide faible (couple NH₄⁺/NH₃) ; les ions éthanoate CH₃CO₂⁻, benzoate C₆H₅CO₂⁻ ou cyanure CN⁻ sont des bases faibles. Seul l'ion qui réagit fixe le pH.
:::

| sel      | ions libérés  | ion qui réagit | nature de cet ion         | solution |
| -------- | ------------- | -------------- | ------------------------- | -------- |
| NaCl     | Na⁺ + Cl⁻     | aucun          | —                         | neutre   |
| NH₄Cl    | NH₄⁺ + Cl⁻    | NH₄⁺           | acide faible (pKₐ = 9,25) | acide    |
| CH₃CO₂Na | CH₃CO₂⁻ + Na⁺ | CH₃CO₂⁻        | base faible (pKₐ = 4,75)  | basique  |

Il suffit de repérer l'ion de la colonne « ion qui réagit » : c'est lui, et lui seul, qui entre dans la formule du pH, avec la concentration C du sel.

::: exemple Le pH du chlorure d'ammonium

1. NH₄Cl → NH₄⁺ + Cl⁻ est totale : [NH₄⁺] = [Cl⁻] = C = 5,0·10⁻² mol·L⁻¹ avant réaction.
2. L'ion Cl⁻, base conjuguée de l'acide fort HCl, est inerte. L'ion NH₄⁺ est un acide faible : NH₄⁺ + H₂O ⇄ NH₃ + H₃O⁺, de pKₐ = 9,25.
3. On applique la formule de l'acide faible avec C = 5,0·10⁻² mol·L⁻¹ : pH = ½ (9,25 − log 5,0·10⁻²) = ½ (9,25 + 1,30) = 5,28.
4. Contrôle : pH < 6 et τ_f = 10^(5,28 − 9,25) = 1,1·10⁻⁴ < 0,05. La solution est acide, comme le prévoit le tableau.

:::

::: exemple Le sens inverse : de la mesure à la concentration

1. Une solution de chlorure d'ammonium a pour pH 5,2. L'ion actif est NH₄⁺, un acide faible : C = 10^(pKₐ − 2pH).
2. C = 10^(9,25 − 10,4) = 10^(−1,15) = 7,1·10⁻² mol·L⁻¹ ; le contrôle donne τ_f = 10^(5,2 − 9,25) = 8,9·10⁻⁵ < 0,05.

:::

::: piege
**Erreur : croire qu'un sel donne toujours une solution neutre.** On annonce que NH₄Cl, « ni acide ni base », laisse l'eau neutre, ou l'on classe Cl⁻ parmi les bases faibles. L'erreur tente parce que la solution contient des ions et pas de molécules d'acide ; mais Cl⁻ est inerte et NH₄⁺ est un acide faible : le pH est inférieur à ½ pKₑ. Seul un sel dont les deux ions sont inertes, comme NaCl, est neutre.
:::

::: propriete
**pH d'un sel** — On repère l'ion qui réagit et l'on prend pour C la concentration du sel. Un ion acide faible suit pH = ½ (pKₐ − log C) ; un ion basique faible suit pH = ½ (pKₑ + pKₐ + log C), avec le pKₐ du couple de cet ion et les mêmes conditions de validité.
Cas : pour CH₃CO₂Na à 5,0·10⁻³ mol·L⁻¹, on retrouve pH = 8,22 ; pour NH₄Cl à 5,0·10⁻² mol·L⁻¹, pH = 5,28.
Cas limite : si les deux ions sont inertes (NaCl), aucune formule ne s'applique et la solution est neutre : pH = ½ pKₑ.
:::

::: verifie À toi : un sel de cyanure
On dissout du cyanure de sodium NaCN. Quel est l'ion qui réagit avec l'eau, et la solution est-elle acide, neutre ou basique ?

---

NaCN se dissout en Na⁺ et CN⁻. Na⁺ est inerte ; CN⁻ est la base faible du couple HCN/CN⁻ et réagit avec l'eau en formant des ions OH⁻. La solution est basique : son pH est supérieur à ½ pKₑ.
:::

::: retenir
Dans un sel dissous, seul l'ion qui réagit avec l'eau fixe le pH : acide faible ou base faible selon l'ion, avec la formule correspondante et C la concentration du sel.
:::

## 💧 La dilution : l'écart de pH dit si l'acide est fort

On prépare deux solutions à 1,0·10⁻² mol·L⁻¹, l'une de HCl, l'autre de HClO (pKₐ = 7,5), puis on les dilue 100 fois : on prélève 10,0 mL à la pipette jaugée, qu'on complète à 1,000 L dans une fiole jaugée. Le pH de HCl passe de 2,00 à 4,00, celui de HClO de 4,75 à 5,75.
Pourquoi ces écarts, 2 et 1, sont-ils différents ?

::: definition
**Dilution n fois** — On prélève un volume V de solution mère à la pipette jaugée, on le verse dans une fiole jaugée de volume n·V et l'on complète à l'eau distillée jusqu'au trait de jauge. La quantité de matière prélevée est conservée, donc la concentration est divisée par n : C′ = C/n, et −log C augmente de log n.
:::

::: figure pH en fonction de −log C pour HCl et pour un acide faible de pKₐ = 7,5 (allure calculée) ; en pointillé, le prolongement vers l'axe des ordonnées, qui coupe celui de l'acide faible à ½ pKₐ
<svg viewBox="0 0 340 236"><title>pH en fonction de −log C : acide fort (pente 1) et acide faible (pente ½)</title><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><line x1="106" y1="190" x2="106" y2="195" stroke="#0f172a" stroke-width="1.2"/><text x="106" y="207" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="158" y1="190" x2="158" y2="195" stroke="#0f172a" stroke-width="1.2"/><text x="158" y="207" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="210" y1="190" x2="210" y2="195" stroke="#0f172a" stroke-width="1.2"/><text x="210" y="207" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="262" y1="190" x2="262" y2="195" stroke="#0f172a" stroke-width="1.2"/><text x="262" y="207" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="314" y1="190" x2="314" y2="195" stroke="#0f172a" stroke-width="1.2"/><text x="314" y="207" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><text x="48" y="207" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="49" y1="167.143" x2="54" y2="167.143" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="171.143" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="49" y1="144.286" x2="54" y2="144.286" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="148.286" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="49" y1="121.429" x2="54" y2="121.429" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="125.429" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="49" y1="98.5714" x2="54" y2="98.5714" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="102.571" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="49" y1="75.7143" x2="54" y2="75.7143" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="79.7143" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="49" y1="52.8571" x2="54" y2="52.8571" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="56.8571" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="49" y1="30" x2="54" y2="30" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="34" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7</text><text x="330" y="220" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−log C</text><text x="60" y="12" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pH</text><line x1="54" y1="190" x2="106" y2="167.143" stroke="#0f6e56" stroke-width="1.8" stroke-dasharray="5 4"/><polyline points="106,167.1 262,98.6" fill="none" stroke="#0f6e56" stroke-width="2.5"/><line x1="54" y1="104.286" x2="106" y2="92.8571" stroke="#d97706" stroke-width="1.8" stroke-dasharray="5 4"/><polyline points="106,92.9 262,58.6" fill="none" stroke="#d97706" stroke-width="2.5"/><circle cx="54" cy="104.3" r="3.5" fill="#d97706"/><text x="62" y="126.286" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">½ pKₐ = 3,75</text><text x="268" y="102.571" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">acide fort</text><text x="256" y="50.5714" text-anchor="end" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">acide faible</text></svg>
:::

La droite de l'acide fort a pour pente 1 : chaque unité de −log C ajoute 1 au pH. Celle de l'acide faible a pour pente ½ et coupe l'axe des ordonnées à ½ pKₐ.

::: exemple Lire fort ou faible dans un écart de pH

1. Dilution 100 fois : V = 10,0 mL dans une fiole de 1,000 L, donc C′ = 1,0·10⁻⁴ mol·L⁻¹ et −log C passe de 2 à 4, soit +log 100 = +2.
2. HCl : pH = −log C, donc le pH augmente de log n = 2, de 2,00 à 4,00.
3. HClO : pH = ½ (pKₐ − log C), donc le pH augmente de ½ log n = 1, de 4,75 à 5,75.
4. Les relations restent valables après dilution : pH < 6 et, pour HClO, τ_f = 10^(5,75 − 7,5) = 1,8·10⁻² < 0,05.
5. Réciproquement, un acide dilué n fois dont le pH augmente de log n est fort, et de ½ log n est faible.

:::

::: piege
**Erreur : croire que tout acide dilué 100 fois gagne 2 unités de pH.** On annonce que HClO passe de 4,75 à 6,75. L'erreur tente parce que l'on a retenu « diviser C par 100 ajoute 2 » avec la formule de l'acide fort ; mais le pH d'un acide faible contient ½ log C, donc il n'augmente que de 1 : 5,75.
:::

::: propriete
**Effet d'une dilution n fois** — Si les relations restent valables, le pH d'un acide fort augmente de log n, celui d'un acide faible de ½ log n ; le pH d'une base forte diminue de log n, celui d'une base faible de ½ log n.
Cas : une base forte de pH 11,00 diluée 100 fois passe à 9,00 ; une base faible de pH 10,50 (pKₐ = 8,0, C = 0,10 mol·L⁻¹) diluée 100 fois passe à 9,50.
Cas limite : une dilution trop forte fait sortir du domaine de validité (pH < 6 pour un acide fort, pH > 8 pour une base forte) : la variation prévue n'est plus observée.
:::

::: verifie À toi : diluer une base
Une solution d'hydroxyde de sodium a pour pH 11,8. On la dilue 1 000 fois. Quel est son pH, et la relation est-elle encore valable ?

---

NaOH est une base forte : le pH diminue de log n = log 1 000 = 3, donc pH = 11,8 − 3 = 8,8. Contrôle : 8,8 est supérieur à 8, les ions de l'eau restent négligeables et la relation est encore valable.
:::

::: retenir
Dilution n fois : acide fort + log n, acide faible + ½ log n ; base forte − log n, base faible − ½ log n, tant que pH < 6 pour un acide et pH > 8 pour une base.
:::

> 🏆 Tu sais désormais relier un pH à une concentration pour un acide ou une base, forte ou faible, contrôler les approximations et lire dans un écart de dilution la force d'un acide. Chaque relation porte avec elle sa condition de validité : c'est elle qu'on vérifie en dernier.
