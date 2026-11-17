# ⚗️ Réactions acide-base — la loi d'action de masse pour classer acides et bases

> 💡 «Une constante d'équilibre ne dit pas à quelle vitesse une réaction se fait, mais jusqu'où elle va.»

Du citron pressé dans l'eau gazeuse aux lacs de cratère chargés de dioxyde de carbone, la chimie des acides et des bases est un transfert d'ion hydrogène que l'on peut chiffrer. Huit notions donnent les moyens de le faire : les couples et la réaction acide-base, l'ionisation propre de l'eau et Kₑ, la loi d'action de masse appliquée aux réactions acide-base, les conditions d'évolution, la force d'un acide ou d'une base mesurée par τ_f, la constante d'acidité Kₐ et le pKₐ, la constante de basicité K_b avec la relation Kₐ·K_b = Kₑ, et le calcul de la constante K d'une réaction acide-base à partir des pKₐ. On suppose acquis le tableau d'avancement (chapitre 1), le taux d'avancement final τ_f (chapitre 4), la fonction des concentrations Π et la constante K (chapitre 5), la définition de Brönsted d'un acide et d'une base et la relation [H₃O⁺] = 10⁻ᵖᴴ.

## 🔄 Le transfert de H⁺ : couples et réaction acide-base

Le lac Nyos, au Cameroun, est un lac de cratère qui renferme beaucoup de dioxyde de carbone dissous. Ce gaz réagit avec l'eau : CO₂ + 2 H₂O ⇄ HCO₃⁻ + H₃O⁺ (1). Dans cette équation, ni le gaz CO₂ ni l'eau ne sont des « acides » ou des « bases » au sens courant du mot.
Quels sont les couples acide/base mis en jeu, et en quoi (1) est-elle une réaction acide-base ?

::: definition
**Couple acide/base, réaction acide-base** — Un acide de Brönsted est une entité chimique, chargée ou non, capable de libérer un ion hydrogène H⁺ ; une base est capable de capter un ion hydrogène H⁺. Un couple acide/base AH/A⁻ réunit un acide et sa base conjuguée, que l'on obtient l'un à partir de l'autre par perte ou gain d'un ion H⁺ : son équation formelle est AH ⇄ A⁻ + H⁺. Une réaction acide-base est un transfert d'ion H⁺ entre l'acide d'un couple et la base d'un autre couple : elle fait donc intervenir nécessairement deux couples.
:::

| Couple acide/base | Équation formelle |
| ----------------- | ----------------- |
| H₃O⁺/H₂O | H₃O⁺ ⇄ H₂O + H⁺ |
| H₂O/OH⁻ | H₂O ⇄ OH⁻ + H⁺ |
| NH₄⁺/NH₃ | NH₄⁺ ⇄ NH₃ + H⁺ |
| CO₂,H₂O/HCO₃⁻ | CO₂,H₂O ⇄ HCO₃⁻ + H⁺ |

::: exemple Retrouver (1) par somme de deux équations formelles

1. Dans (1), CO₂,H₂O perd un ion H⁺ et devient HCO₃⁻ : c'est l'acide d'un couple. L'eau capte cet ion H⁺ et devient H₃O⁺ : c'est la base d'un autre couple.
2. Les deux couples sont donc CO₂,H₂O/HCO₃⁻, d'équation formelle CO₂,H₂O ⇄ HCO₃⁻ + H⁺, et H₃O⁺/H₂O, qu'on écrit ici dans le sens où l'eau capte l'ion : H₂O + H⁺ ⇄ H₃O⁺.
3. On additionne les deux équations : CO₂,H₂O + H₂O + H⁺ ⇄ HCO₃⁻ + H⁺ + H₃O⁺. L'ion H⁺ figure des deux côtés et disparaît, car il ne fait que passer d'une entité à l'autre.
4. Il reste CO₂ + 2 H₂O ⇄ HCO₃⁻ + H₃O⁺, c'est-à-dire (1) : un transfert d'ion H⁺ entre deux couples, donc une réaction acide-base.

:::

::: piege
**Erreur : former les couples avec les deux réactifs, puis avec les deux produits.** Pour HClO + NH₃ ⇄ ClO⁻ + NH₄⁺, on écrit « HClO/NH₃ » et « ClO⁻/NH₄⁺ ». L'erreur tente parce qu'on lit l'équation de gauche à droite et qu'on groupe ce qui est côte à côte ; mais un couple réunit deux entités qui ne diffèrent que d'un ion H⁺. Ici HClO a perdu H⁺ pour devenir ClO⁻ (couple HClO/ClO⁻), et NH₃ l'a gagné pour devenir NH₄⁺ (couple NH₄⁺/NH₃).
:::

::: propriete
**Reconnaître une réaction acide-base** — Une réaction Acide₁ + Base₂ ⇄ Acide₂ + Base₁ met en jeu les couples Acide₁/Base₁ et Acide₂/Base₂ : chacun réunit deux entités qui diffèrent d'un seul ion H⁺, et la somme de leurs équations formelles redonne l'équation de la réaction.
Cas : dans H₂O + H₂O ⇄ H₃O⁺ + OH⁻, une molécule d'eau est l'acide du couple H₂O/OH⁻ et l'autre la base du couple H₃O⁺/H₂O.
Cas limite : Zn(s) + 2 H₃O⁺ → Zn²⁺ + H₂ + 2 H₂O n'est pas une réaction acide-base, bien que H₃O⁺ y figure : aucun ion H⁺ n'est transféré d'un couple à l'autre, ce sont des électrons.
:::

::: verifie À toi : une autre réaction
Dans la réaction HCN + CH₃NH₂ ⇄ CN⁻ + CH₃NH₃⁺, donner les deux couples et leurs équations formelles, puis retrouver l'équation par somme.

---

HCN perd un ion H⁺ et devient CN⁻ : couple HCN/CN⁻, HCN ⇄ CN⁻ + H⁺. CH₃NH₂ le capte et devient CH₃NH₃⁺ : couple CH₃NH₃⁺/CH₃NH₂, CH₃NH₂ + H⁺ ⇄ CH₃NH₃⁺. La somme HCN + CH₃NH₂ + H⁺ ⇄ CN⁻ + H⁺ + CH₃NH₃⁺ donne, après simplification de H⁺, HCN + CH₃NH₂ ⇄ CN⁻ + CH₃NH₃⁺.
:::

::: retenir
Une réaction acide-base est un transfert d'ion H⁺ entre deux couples ; un couple réunit deux entités qui diffèrent d'un seul H⁺, et la somme des équations formelles redonne la réaction.
:::

## 💧 L'ionisation propre de l'eau et le produit ionique Kₑ

De l'eau très pure, placée entre deux électrodes, laisse passer un courant extrêmement faible, mais non nul. À 25 °C, on mesure un pH de 7,0 : elle contient donc quelques ions.
D'où viennent-ils, et combien y en a-t-il ?

::: definition
**Ionisation propre de l'eau, produit ionique Kₑ** — Deux molécules d'eau peuvent réagir l'une sur l'autre : H₂O + H₂O ⇄ H₃O⁺ + OH⁻ (2), réaction acide-base des couples H₃O⁺/H₂O et H₂O/OH⁻. Sa fonction des concentrations est Π = [H₃O⁺]·[OH⁻], et à l'équilibre dynamique Π prend la valeur de la constante d'équilibre, notée Kₑ et appelée produit ionique de l'eau : [H₃O⁺]·[OH⁻] = Kₑ. Kₑ ne dépend que de la température ; à 25 °C, Kₑ = 1,0·10⁻¹⁴.
:::

| θ (°C) | 0 | 25 | 40 | 60 | 80 |
| ------ | --- | --- | --- | --- | --- |
| Kₑ | 1,1·10⁻¹⁵ | 1,0·10⁻¹⁴ | 3,0·10⁻¹⁴ | 1,0·10⁻¹³ | 2,5·10⁻¹³ |

Ce tableau montre que Kₑ augmente avec la température : d'après la loi de modération du chapitre 6, la réaction (2) est donc endothermique. Sa constante est très faible : l'ionisation propre est très limitée, et l'eau reste formée presque uniquement de molécules H₂O.

::: exemple Utiliser Kₑ pour trouver [OH⁻]

1. L'eau pure à 25 °C a un pH de 7,0, donc [H₃O⁺] = 10⁻⁷ mol·L⁻¹. Chaque réaction (2) forme un ion H₃O⁺ et un ion OH⁻ : [OH⁻] = [H₃O⁺] = 1,0·10⁻⁷ mol·L⁻¹, et le produit vaut bien 1,0·10⁻⁷ × 1,0·10⁻⁷ = 1,0·10⁻¹⁴ = Kₑ.
2. Une solution à 25 °C a un pH de 9,00 : [H₃O⁺] = 10⁻⁹ = 1,0·10⁻⁹ mol·L⁻¹. À l'équilibre, [OH⁻] = Kₑ / [H₃O⁺] = 1,0·10⁻¹⁴ / 1,0·10⁻⁹ = 1,0·10⁻⁵ mol·L⁻¹.
3. L'eau pure à 60 °C a toujours [H₃O⁺] = [OH⁻], mais Kₑ = 1,0·10⁻¹³ : [H₃O⁺]² = 1,0·10⁻¹³, d'où [H₃O⁺] = [OH⁻] ≈ 3,2·10⁻⁷ mol·L⁻¹, plus qu'à 25 °C : chauffer l'eau augmente son ionisation.

:::

::: piege
**Erreur : prendre Kₑ = 1,0·10⁻¹⁴ à toute température.** À 60 °C, une solution a [H₃O⁺] = 1,0·10⁻⁶ mol·L⁻¹ et l'on écrit [OH⁻] = 1,0·10⁻¹⁴ / 1,0·10⁻⁶ = 1,0·10⁻⁸ mol·L⁻¹. L'erreur tente parce que la valeur 10⁻¹⁴ est celle que l'on utilise le plus souvent ; mais Kₑ dépend de la température, et la valeur 10⁻¹⁴ n'est valable qu'à 25 °C. À 60 °C, [OH⁻] = 1,0·10⁻¹³ / 1,0·10⁻⁶ = 1,0·10⁻⁷ mol·L⁻¹.
:::

::: propriete
**Produit ionique de l'eau** — Dans toute solution aqueuse à l'équilibre, [H₃O⁺]·[OH⁻] = Kₑ, avec Kₑ qui ne dépend que de la température ; sans précision, la température est 25 °C et Kₑ = 1,0·10⁻¹⁴. Connaître [H₃O⁺] (par le pH) donne [OH⁻] = Kₑ / [H₃O⁺], et réciproquement.
Cas : à 25 °C, [H₃O⁺] = 1,0·10⁻² mol·L⁻¹ donne [OH⁻] = 1,0·10⁻¹² mol·L⁻¹ ; ajouter un acide ou une base dans l'eau ne change pas Kₑ, mais change le partage entre [H₃O⁺] et [OH⁻].
Cas limite : dans l'eau pure, [H₃O⁺] = [OH⁻] = √Kₑ à toute température ; cette valeur vaut 1,0·10⁻⁷ mol·L⁻¹ à 25 °C et 3,2·10⁻⁷ mol·L⁻¹ à 60 °C.
:::

::: verifie À toi : une solution à 40 °C
À 40 °C, Kₑ = 3,0·10⁻¹⁴. Une solution a [H₃O⁺] = 2,0·10⁻⁸ mol·L⁻¹. Calculer [OH⁻] et dire laquelle des deux entités H₃O⁺ et OH⁻ est la plus concentrée.

---

[OH⁻] = Kₑ / [H₃O⁺] = 3,0·10⁻¹⁴ / 2,0·10⁻⁸ = 1,5·10⁻⁶ mol·L⁻¹. Cette valeur est bien supérieure à 2,0·10⁻⁸ mol·L⁻¹ : les ions OH⁻ sont les plus concentrés.
:::

::: retenir
[H₃O⁺]·[OH⁻] = Kₑ à l'équilibre ; Kₑ ne dépend que de la température et vaut 1,0·10⁻¹⁴ à 25 °C ; il augmente avec la température.
:::

## 📊 La loi d'action de masse pour une réaction acide-base

On mélange à parts égales de l'acide nitreux HNO₂ et de l'ammoniac NH₃ : HNO₂ + NH₃ ⇄ NO₂⁻ + NH₄⁺ (3). L'acide cède un ion H⁺ à la base, mais le transfert va-t-il jusqu'au bout ?
Quand tout est fini, reste-t-il beaucoup de HNO₂ et de NH₃ ?

::: definition
**Loi d'action de masse pour une réaction acide-base** — Pour la réaction Acide₁ + Base₂ ⇄ Acide₂ + Base₁, la fonction des concentrations est Π = [Acide₂]·[Base₁] / ([Acide₁]·[Base₂]). À l'équilibre dynamique, Π prend la valeur K, constante qui ne dépend que de la température pour une équation donnée. L'eau, quand elle n'est que le solvant, n'apparaît pas dans Π, et Π et K s'écrivent sans unité.
:::

| Valeur de K | Réaction directe, à partir de quantités égales de réactifs |
| ----------- | ------------------------------------------------------------ |
| très grande (repère : K > 10⁴) | pratiquement totale ; la réaction inverse ne se fait pratiquement pas |
| moyenne (le manuel range ainsi K ≈ 3·10⁻⁵, pour NH₄⁺ + CH₃CO₂⁻) | moyennement limitée : réactifs et produits coexistent en quantités comparables |
| extrêmement faible (ex. Kₑ = 1,0·10⁻¹⁴ ; 2·10⁻¹⁵ pour CH₃NH₃⁺ + Cl⁻ ⇄ CH₃NH₂ + HCl) | extrêmement limitée ; la réaction inverse est pratiquement totale |

::: exemple Que reste-t-il après le mélange de (3) ?

On donne K = 8,9·10⁵ à 25 °C pour (3) (cette valeur se calcule avec la dernière notion du chapitre). On mélange HNO₂ et NH₃ de sorte que [HNO₂]₀ = [NH₃]₀ = 0,10 mol·L⁻¹ juste après le mélange.
1. Π = [NO₂⁻]·[NH₄⁺] / ([HNO₂]·[NH₃]), sans l'eau. K = 8,9·10⁵ est très grande : la réaction directe est pratiquement totale.
2. Les réactifs sont en quantités égales, donc à l'équilibre [HNO₂] = [NH₃] = y, et [NO₂⁻] = [NH₄⁺] = 0,10 − y, pratiquement 0,10 mol·L⁻¹ puisque y est très petit.
3. K = (0,10)² / y², d'où y = 0,10 / √K = 0,10 / 943 ≈ 1,1·10⁻⁴ mol·L⁻¹.
4. Il reste 1,1·10⁻⁴ / 0,10 ≈ 0,11 % des réactifs : l'avancement final est pratiquement égal à l'avancement maximal, et τ_f est pratiquement égal à 1.

:::

::: piege
**Erreur : lire une grande valeur de K comme « la réaction est rapide ».** On dit que, K valant 8,9·10⁵, le transfert est instantané, et que s'il était de 3,2·10⁻⁶ il serait lent. L'erreur tente parce que « grand » évoque « vite » ; mais K ne renseigne que sur le point d'arrivée, pas sur la durée du trajet. Les réactions acide-base sont instantanées quelle que soit K : une K extrêmement faible donne une réaction instantanée mais extrêmement limitée.
:::

::: propriete
**Lire K** — K indique la tendance des réactifs à se convertir en produits : très grande, la réaction directe est pratiquement totale ; moyenne, elle est moyennement limitée ; extrêmement faible, elle est extrêmement limitée, et la réaction inverse est pratiquement totale.
Cas : pour (3), τ_f est voisin de 1 ; pour l'ionisation propre de l'eau, K = Kₑ = 1,0·10⁻¹⁴ est extrêmement faible, et la réaction est extrêmement limitée.
Cas limite : si l'on écrit l'équation à l'envers, NO₂⁻ + NH₄⁺ ⇄ HNO₂ + NH₃, la constante devient 1/K = 1,1·10⁻⁶ : K dépend de la façon d'écrire l'équation.
:::

::: verifie À toi : une constante très faible
Pour NH₄⁺ + HCOO⁻ ⇄ NH₃ + HCOOH, K = 3,2·10⁻⁶ à 25 °C. On mélange NH₄⁺ et HCOO⁻ de sorte que [NH₄⁺]₀ = [HCOO⁻]₀ = 0,10 mol·L⁻¹. Calculer [NH₃] à l'équilibre (en supposant que NH₄⁺ et HCOO⁻ restent pratiquement à 0,10 mol·L⁻¹) et conclure.

---

Avec [NH₃] = [HCOOH] = z, K = z² / (0,10)², d'où z = 0,10 × √(3,2·10⁻⁶) = 0,10 × 1,8·10⁻³ = 1,8·10⁻⁴ mol·L⁻¹. Il se forme 0,18 % de produits : la réaction directe est très limitée.
:::

::: retenir
Π = [Acide₂]·[Base₁] / ([Acide₁]·[Base₂]) vaut K à l'équilibre, sans l'eau ; une K très grande donne une réaction pratiquement totale, une K extrêmement faible une réaction extrêmement limitée, et K ne dit rien de la vitesse.
:::

## 🧭 Les conditions d'évolution : dans quel sens va le mélange ?

On a dans un même bécher de l'acide méthanoïque HCOOH et des ions éthanoate CH₃COO⁻, avec leurs produits : HCOOH + CH₃COO⁻ ⇄ HCOO⁻ + CH₃COOH (4), de constante K = 10 à 25 °C. Dans un état donné, il y a des quantités de chaque espèce, mais pas forcément celles de l'équilibre.
Dans quel sens le système évolue-t-il spontanément ?

::: definition
**Conditions d'évolution spontanée** — Pour une réaction acide-base, on calcule Π avec les concentrations du moment et on la compare à K. Si Π < K, la réaction directe se produit ; si Π > K, la réaction inverse se produit ; si Π = K, le système est en équilibre dynamique et n'évolue pas. Les réactions acide-base sont instantanées : le système atteint pratiquement aussitôt son état d'équilibre.
:::

::: figure Deux des trois états du système (4) sur une échelle logarithmique de Π : S₁ (Π = 1,0) à gauche de K = 10, S₂ (Π = 1,0·10²) à droite ; les flèches indiquent le sens d'évolution vers K
<svg viewBox="0 0 340 150"><title>Π et K sur une échelle logarithmique : deux états de part et d'autre de K</title><line x1="24.0" y1="80.0" x2="314.0" y2="80.0" stroke="#0f172a" stroke-width="1.6"/><polygon points="320,80 312,76 312,84" fill="#0f172a"/><line x1="30.0" y1="76.0" x2="30.0" y2="84.0" stroke="#0f172a" stroke-width="1.4"/><text x="30" y="97" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10⁻¹</text><line x1="97.5" y1="76.0" x2="97.5" y2="84.0" stroke="#0f172a" stroke-width="1.4"/><text x="97.5" y="97" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="165.0" y1="76.0" x2="165.0" y2="84.0" stroke="#0f172a" stroke-width="1.4"/><text x="165" y="97" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="232.5" y1="76.0" x2="232.5" y2="84.0" stroke="#0f172a" stroke-width="1.4"/><text x="232.5" y="97" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10²</text><line x1="300.0" y1="76.0" x2="300.0" y2="84.0" stroke="#0f172a" stroke-width="1.4"/><text x="300" y="97" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10³</text><text x="322" y="72" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Π</text><line x1="165.0" y1="30.0" x2="165.0" y2="84.0" stroke="#0f6e56" stroke-width="1.8" stroke-dasharray="5 4"/><text x="165" y="22" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">K = 10</text><circle cx="97.5" cy="80" r="5" fill="#2563eb" stroke="#0f172a" stroke-width="1.2"/><text x="97.5" y="68" text-anchor="middle" font-size="11" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S₁</text><circle cx="232.5" cy="80" r="5" fill="#dc2626" stroke="#0f172a" stroke-width="1.2"/><text x="232.5" y="68" text-anchor="middle" font-size="11" font-weight="700" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S₂</text><line x1="105.5" y1="108.0" x2="150.0" y2="108.0" stroke="#0f6e56" stroke-width="2.2"/><polygon points="157.0,108 148.0,103.5 148.0,112.5" fill="#0f6e56"/><line x1="224.5" y1="108.0" x2="180.0" y2="108.0" stroke="#d97706" stroke-width="2.2"/><polygon points="173.0,108 182.0,103.5 182.0,112.5" fill="#d97706"/><text x="131.25" y="124" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Π &lt; K : sens direct</text><text x="198.75" y="140" text-anchor="middle" font-size="11" font-weight="700" fill="#d97706" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Π &gt; K : sens inverse</text></svg>
:::

| État | [HCOOH] | [CH₃COO⁻] | [HCOO⁻] | [CH₃COOH] | Π |
| ---- | ------- | --------- | ------- | --------- | --- |
| S₁ | 0,20 | 0,010 | 0,050 | 0,040 | 1,0 |
| S₂ | 0,010 | 0,010 | 0,10 | 0,10 | 1,0·10² |
| S₃ | 0,020 | 0,050 | 0,050 | 0,20 | 10 |

Les concentrations sont en mol·L⁻¹.

::: exemple Prévoir le sens d'évolution de (4) dans trois états

1. Π = [HCOO⁻]·[CH₃COOH] / ([HCOOH]·[CH₃COO⁻]), et K = 10.
2. Dans S₁, Π = (0,050 × 0,040) / (0,20 × 0,010) = 2,0·10⁻³ / 2,0·10⁻³ = 1,0. Comme 1,0 < 10, Π < K : la réaction directe se produit, HCOOH et CH₃COO⁻ se transforment en HCOO⁻ et CH₃COOH.
3. Dans S₂, Π = (0,10 × 0,10) / (0,010 × 0,010) = 1,0·10⁻² / 1,0·10⁻⁴ = 1,0·10². Comme 1,0·10² > 10, Π > K : la réaction inverse se produit.
4. Dans S₃, Π = (0,050 × 0,20) / (0,020 × 0,050) = 1,0·10⁻² / 1,0·10⁻³ = 10 = K : le système est en équilibre et ne change plus.

:::

::: piege
**Erreur : comparer Π à 1 au lieu de la comparer à K.** Dans S₁ on trouve Π = 1,0 et l'on conclut que le système est en équilibre. L'erreur tente parce qu'un quotient égal à 1 évoque l'égalité entre produits et réactifs ; mais l'équilibre est atteint quand Π = K, et ici K = 10. Comme Π = 1,0 est inférieure à K, le système n'est pas à l'équilibre et évolue dans le sens direct.
:::

::: propriete
**Sens d'évolution spontanée** — À température constante, K est fixée. Si Π < K, le sens direct ; si Π > K, le sens inverse ; si Π = K, l'équilibre. La réaction qui se produit fait tendre Π vers K.
Cas : dans de la vapeur d'eau qui vient de se condenser, [H₃O⁺] = [OH⁻] = 0, donc Π = 0 < Kₑ : l'ionisation propre (2) se produit dans le sens direct jusqu'à ce que Π atteigne Kₑ.
Cas limite : si un produit est absent, Π = 0 est inférieur à toute K, et la réaction directe est le seul sens possible, même quand K est très petite.
:::

::: verifie À toi : un état très riche en produits
Pour (3), HNO₂ + NH₃ ⇄ NO₂⁻ + NH₄⁺, K = 8,9·10⁵. Un état contient [NO₂⁻] = [NH₄⁺] = 0,50 mol·L⁻¹ et [HNO₂] = [NH₃] = 1,0·10⁻⁴ mol·L⁻¹. Calculer Π et donner le sens d'évolution.

---

Π = (0,50 × 0,50) / (1,0·10⁻⁴ × 1,0·10⁻⁴) = 0,25 / 1,0·10⁻⁸ = 2,5·10⁷. Cette valeur est supérieure à K = 8,9·10⁵ : le système évolue dans le sens inverse, malgré une K très grande, car il y a trop de produits par rapport à l'équilibre.
:::

::: retenir
Π < K : sens direct ; Π > K : sens inverse ; Π = K : équilibre. On compare Π à K, jamais à 1, et le sens d'évolution est atteint instantanément pour une réaction acide-base.
:::

## 🎯 Acide fort, acide faible : le taux d'avancement final τ_f

Deux solutions d'acide de même concentration C = 1,0·10⁻² mol·L⁻¹ n'ont pas le même pH. Dans l'une, le pH vaut 2,00 ; dans l'autre, 3,38. On voudrait en déduire laquelle contient l'acide le plus « fort », et ce que ce mot veut dire.
Comment un pH mesuré permet-il de chiffrer la force d'un acide ?

::: definition
**Acide fort, acide faible, base forte, base faible** — Un acide AH est fort si sa réaction avec l'eau, AH + H₂O → A⁻ + H₃O⁺, est totale (τ_f = 1) ; il est faible si elle est limitée (τ_f < 1). De même, une base est forte si sa réaction avec l'eau, Base + H₂O → Acide + OH⁻, est totale, et faible si elle est limitée. On mesure le pH, puis on calcule τ_f = x_f / x_max à partir du tableau d'avancement, en négligeant les ions H₃O⁺ ou OH⁻ de l'ionisation propre de l'eau.
:::

Avec x_max = C·V (l'eau est en excès) et x_f = [H₃O⁺]_f·V pour un acide, on obtient τ_f = 10⁻ᵖᴴ / C. Pour une base, les ions OH⁻ formés valent [OH⁻]_f = Kₑ / [H₃O⁺]_f = Kₑ·10ᵖᴴ, d'où τ_f = Kₑ·10ᵖᴴ / C.

Mesures d'illustration (valeurs cohérentes avec l'acide éthanoïque à 25 °C) : pH d'une solution d'acide éthanoïque CH₃COOH à quatre concentrations C.

| C (mol·L⁻¹) | pH | [H₃O⁺] (mol·L⁻¹) | τ_f |
| ----------- | --- | ---------------- | --- |
| 1,0·10⁻¹ | 2,88 | 1,3·10⁻³ | 1,3·10⁻² |
| 1,0·10⁻² | 3,38 | 4,2·10⁻⁴ | 4,2·10⁻² |
| 1,0·10⁻³ | 3,90 | 1,3·10⁻⁴ | 0,13 |
| 1,0·10⁻⁴ | 4,47 | 3,4·10⁻⁵ | 0,34 |

::: figure τ_f en fonction de C (échelle logarithmique) : pour l'acide fort, τ_f vaut 1 à toute concentration ; pour l'acide éthanoïque (mesures du tableau), τ_f est inférieur à 1 et augmente quand C diminue
<svg viewBox="0 0 340 232"><title>τ_f en fonction de C : acide fort et acide éthanoïque</title><line x1="54.0" y1="190.0" x2="322.0" y2="190.0" stroke="#0f172a" stroke-width="1.6"/><line x1="54.0" y1="190.0" x2="54.0" y2="18.0" stroke="#0f172a" stroke-width="1.6"/><polygon points="328,190 320,186 320,194" fill="#0f172a"/><polygon points="54,12 50,20 58,20" fill="#0f172a"/><line x1="54.0" y1="110.0" x2="318.0" y2="110.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54.0" y1="30.0" x2="318.0" y2="30.0" stroke="#e2e8f0" stroke-width="1"/><line x1="86.8" y1="186.0" x2="86.8" y2="194.0" stroke="#0f172a" stroke-width="1.4"/><text x="86.75" y="208" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10⁻⁴</text><line x1="152.2" y1="186.0" x2="152.2" y2="194.0" stroke="#0f172a" stroke-width="1.4"/><text x="152.25" y="208" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10⁻³</text><line x1="217.8" y1="186.0" x2="217.8" y2="194.0" stroke="#0f172a" stroke-width="1.4"/><text x="217.75" y="208" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10⁻²</text><line x1="283.2" y1="186.0" x2="283.2" y2="194.0" stroke="#0f172a" stroke-width="1.4"/><text x="283.25" y="208" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10⁻¹</text><text x="48" y="194" text-anchor="end" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="48" y="114" text-anchor="end" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,5</text><text x="48" y="34" text-anchor="end" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="322" y="222" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C (mol·L⁻¹)</text><text x="60" y="12" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τ_f</text><polyline points="67.1,118.9 69.1,120.7 71.0,122.4 73.0,124.1 75.0,125.8 76.9,127.4 78.9,129.0 80.9,130.6 82.8,132.2 84.8,133.7 86.8,135.3 88.7,136.7 90.7,138.2 92.6,139.6 94.6,141.0 96.6,142.4 98.5,143.7 100.5,145.1 102.5,146.3 104.4,147.6 106.4,148.8 108.4,150.0 110.3,151.2 112.3,152.3 114.3,153.4 116.2,154.5 118.2,155.6 120.2,156.6 122.1,157.6 124.1,158.6 126.1,159.6 128.0,160.5 130.0,161.4 131.9,162.3 133.9,163.1 135.9,164.0 137.8,164.8 139.8,165.5 141.8,166.3 143.7,167.1 145.7,167.8 147.7,168.5 149.6,169.2 151.6,169.8 153.6,170.5 155.5,171.1 157.5,171.7 159.5,172.3 161.4,172.8 163.4,173.4 165.4,173.9 167.3,174.4 169.3,174.9 171.2,175.4 173.2,175.9 175.2,176.4 177.1,176.8 179.1,177.2 181.1,177.6 183.0,178.0 185.0,178.4 187.0,178.8 188.9,179.2 190.9,179.5 192.9,179.9 194.8,180.2 196.8,180.5 198.8,180.8 200.7,181.1 202.7,181.4 204.7,181.7 206.6,182.0 208.6,182.3 210.5,182.5 212.5,182.8 214.5,183.0 216.4,183.2 218.4,183.5 220.4,183.7 222.3,183.9 224.3,184.1 226.3,184.3 228.2,184.5 230.2,184.7 232.2,184.8 234.1,185.0 236.1,185.2 238.1,185.3 240.0,185.5 242.0,185.7 244.0,185.8 245.9,185.9 247.9,186.1 249.8,186.2 251.8,186.3 253.8,186.5 255.7,186.6 257.7,186.7 259.7,186.8 261.6,186.9 263.6,187.0 265.6,187.1 267.5,187.2 269.5,187.3 271.5,187.4 273.4,187.5 275.4,187.6 277.4,187.6 279.3,187.7 281.3,187.8 283.2,187.9 285.2,188.0 287.2,188.0 289.1,188.1 291.1,188.2 293.1,188.2 295.0,188.3 297.0,188.3 299.0,188.4 300.9,188.4 302.9,188.5" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-linejoin="round"/><polyline points="67.1,30.0 69.1,30.0 71.0,30.0 73.0,30.0 75.0,30.0 76.9,30.0 78.9,30.0 80.9,30.0 82.8,30.0 84.8,30.0 86.8,30.0 88.7,30.0 90.7,30.0 92.6,30.0 94.6,30.0 96.6,30.0 98.5,30.0 100.5,30.0 102.5,30.0 104.4,30.0 106.4,30.0 108.4,30.0 110.3,30.0 112.3,30.0 114.3,30.0 116.2,30.0 118.2,30.0 120.2,30.0 122.1,30.0 124.1,30.0 126.1,30.0 128.0,30.0 130.0,30.0 131.9,30.0 133.9,30.0 135.9,30.0 137.8,30.0 139.8,30.0 141.8,30.0 143.7,30.0 145.7,30.0 147.7,30.0 149.6,30.0 151.6,30.0 153.6,30.0 155.5,30.0 157.5,30.0 159.5,30.0 161.4,30.0 163.4,30.0 165.4,30.0 167.3,30.0 169.3,30.0 171.2,30.0 173.2,30.0 175.2,30.0 177.1,30.0 179.1,30.0 181.1,30.0 183.0,30.0 185.0,30.0 187.0,30.0 188.9,30.0 190.9,30.0 192.9,30.0 194.8,30.0 196.8,30.0 198.8,30.0 200.7,30.0 202.7,30.0 204.7,30.0 206.6,30.0 208.6,30.0 210.5,30.0 212.5,30.0 214.5,30.0 216.4,30.0 218.4,30.0 220.4,30.0 222.3,30.0 224.3,30.0 226.3,30.0 228.2,30.0 230.2,30.0 232.2,30.0 234.1,30.0 236.1,30.0 238.1,30.0 240.0,30.0 242.0,30.0 244.0,30.0 245.9,30.0 247.9,30.0 249.8,30.0 251.8,30.0 253.8,30.0 255.7,30.0 257.7,30.0 259.7,30.0 261.6,30.0 263.6,30.0 265.6,30.0 267.5,30.0 269.5,30.0 271.5,30.0 273.4,30.0 275.4,30.0 277.4,30.0 279.3,30.0 281.3,30.0 283.2,30.0 285.2,30.0 287.2,30.0 289.1,30.0 291.1,30.0 293.1,30.0 295.0,30.0 297.0,30.0 299.0,30.0 300.9,30.0 302.9,30.0" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round"/><circle cx="86.8" cy="135.25030801634205" r="4" fill="#dc2626" stroke="#0f172a" stroke-width="1.2"/><circle cx="152.2" cy="170.02989389574782" r="4" fill="#dc2626" stroke="#0f172a" stroke-width="1.2"/><circle cx="217.8" cy="183.39049080629783" r="4" fill="#dc2626" stroke="#0f172a" stroke-width="1.2"/><circle cx="283.2" cy="187.8795262539441" r="4" fill="#dc2626" stroke="#0f172a" stroke-width="1.2"/><circle cx="86.8" cy="30" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/><circle cx="152.2" cy="30" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/><circle cx="217.8" cy="30" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/><circle cx="283.2" cy="30" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/><text x="318" y="22" text-anchor="end" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">acide fort</text><text x="96" y="122" text-anchor="start" font-size="11" font-weight="700" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">acide éthanoïque</text></svg>
:::

::: exemple Classer deux acides et une base d'après leur pH

1. Première solution, de concentration C = 1,0·10⁻² mol·L⁻¹ et de pH 2,00 : [H₃O⁺]_f = 10⁻² = 1,0·10⁻² mol·L⁻¹, donc τ_f = 1,0·10⁻² / 1,0·10⁻² = 1. La réaction avec l'eau est totale : cet acide est fort.
2. Seconde solution, de même concentration et de pH 3,38 : [H₃O⁺]_f = 10⁻³·³⁸ = 4,2·10⁻⁴ mol·L⁻¹, donc τ_f = 4,2·10⁻⁴ / 1,0·10⁻² = 4,2·10⁻² < 1. La réaction est limitée : cet acide est faible, ionisé à 4 % seulement.
3. Solution d'ammoniac NH₃ de concentration C = 2,0·10⁻² mol·L⁻¹ et de pH 10,77 à 25 °C : [H₃O⁺]_f = 10⁻¹⁰·⁷⁷ = 1,7·10⁻¹¹ mol·L⁻¹, donc [OH⁻]_f = 1,0·10⁻¹⁴ / 1,7·10⁻¹¹ = 5,9·10⁻⁴ mol·L⁻¹, et τ_f = 5,9·10⁻⁴ / 2,0·10⁻² = 3,0·10⁻² < 1 : NH₃ est une base faible.

:::

::: piege
**Erreur : comparer la force de deux acides par leur pH quand les concentrations diffèrent.** Une solution d'acide chlorhydrique à 1,0·10⁻³ mol·L⁻¹ a un pH de 3,00 ; une solution d'acide éthanoïque à 1,0·10⁻¹ mol·L⁻¹ a un pH de 2,88. On conclut que l'acide éthanoïque est le plus fort. L'erreur tente parce qu'un pH plus bas évoque un acide plus fort ; mais l'acide éthanoïque est 100 fois plus concentré. Son τ_f vaut 10⁻²·⁸⁸ / 1,0·10⁻¹ = 1,3·10⁻², alors que celui de HCl vaut 10⁻³·⁰⁰ / 1,0·10⁻³ = 1,0 : HCl est fort et l'acide éthanoïque faible.
:::

::: propriete
**Force d'un acide ou d'une base par τ_f** — Acide : τ_f = 10⁻ᵖᴴ / C ; base : τ_f = Kₑ·10ᵖᴴ / C. Si τ_f = 1, l'acide (la base) est fort(e) ; si τ_f < 1, il (elle) est faible. Pour un acide faible, τ_f dépend de la concentration initiale : il augmente quand C diminue.
Cas : HCl à 5,0·10⁻³ mol·L⁻¹ a un pH de 2,30, donc τ_f = 10⁻²·³⁰ / 5,0·10⁻³ = 1,0 : acide fort ; NaOH à 5,0·10⁻³ mol·L⁻¹ a un pH de 11,70, donc τ_f = 1,0·10⁻¹⁴ × 10¹¹·⁷⁰ / 5,0·10⁻³ = 1,0 : base forte.
Cas limite : comme τ_f d'un acide faible varie avec C, on ne peut pas comparer deux acides faibles par leur τ_f si leurs concentrations diffèrent : il faut une grandeur qui ne dépende pas de C (notion suivante).
:::

::: verifie À toi : un acide éthanoïque dilué
On mesure un pH de 3,74 pour une solution d'acide éthanoïque de concentration C = 2,0·10⁻³ mol·L⁻¹. Calculer τ_f et conclure.

---

[H₃O⁺]_f = 10⁻³·⁷⁴ = 1,8·10⁻⁴ mol·L⁻¹, donc τ_f = 1,8·10⁻⁴ / 2,0·10⁻³ = 0,091. Comme τ_f < 1, la réaction avec l'eau est limitée : l'acide éthanoïque est faible, ionisé à 9 % seulement.
:::

::: retenir
Acide : τ_f = 10⁻ᵖᴴ / C ; base : τ_f = Kₑ·10ᵖᴴ / C. τ_f = 1 : fort(e) ; τ_f < 1 : faible. Pour un acide faible, τ_f dépend de C : on ne compare pas la force d'acides de concentrations différentes.
:::

## 📏 La constante d'acidité Kₐ et le pKₐ

Le tableau précédent montre que τ_f de l'acide éthanoïque passe de 0,013 à 0,34 quand on le dilue mille fois, alors que c'est le même acide. Pour comparer deux acides faibles, on voudrait une grandeur qui ne change pas avec C.
Laquelle choisir, et comment ranger tous les acides sur une même échelle ?

::: definition
**Constante d'acidité Kₐ, pKₐ** — On compare tous les acides à un même acide de référence, H₃O⁺, du couple H₃O⁺/H₂O. Pour un couple Acideᵢ/Baseᵢ, on considère la réaction Acideᵢ + H₂O ⇄ H₃O⁺ + Baseᵢ (5). Sa constante d'équilibre est la constante d'acidité Kₐᵢ : Kₐᵢ = [H₃O⁺]·[Baseᵢ] / [Acideᵢ] à l'équilibre dynamique. Elle ne dépend que de la température. On définit pKₐ = −log Kₐ, soit Kₐ = 10⁻ᵖᴷᵃ. Un acide est d'autant plus fort que Kₐ est grande et que pKₐ est faible.
:::

::: figure Échelle des pKₐ à 25 °C (valeurs du manuel) : chaque point porte l'acide de son couple ; à gauche de −1,74 l'acide est fort et sa base conjuguée inerte, entre −1,74 et 15,74 l'acide et la base sont faibles, à droite de 15,74 l'acide est inerte et sa base forte
<svg viewBox="0 0 340 200"><title>Échelle des pKa : zones acide fort, faible, inerte et zones conjuguées</title><rect x="24.0" y="26" width="65.7" height="42" fill="#2563eb" fill-opacity="0.14" stroke="#2563eb" stroke-width="1.2"/><text x="56.865" y="43" text-anchor="middle" font-size="10" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">acide</text><text x="56.865" y="58" text-anchor="middle" font-size="10" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">fort</text><rect x="89.7" y="26" width="183.5" height="42" fill="#0f6e56" fill-opacity="0.14" stroke="#0f6e56" stroke-width="1.2"/><text x="181.5" y="43" text-anchor="middle" font-size="10" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">acide</text><text x="181.5" y="58" text-anchor="middle" font-size="10" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">faible</text><rect x="273.3" y="26" width="55.2" height="42" fill="#64748b" fill-opacity="0.14" stroke="#64748b" stroke-width="1.2"/><text x="300.885" y="43" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">acide</text><text x="300.885" y="58" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">inerte</text><rect x="24.0" y="150" width="65.7" height="42" fill="#2563eb" fill-opacity="0.14" stroke="#2563eb" stroke-width="1.2"/><text x="56.865" y="167" text-anchor="middle" font-size="10" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">base</text><text x="56.865" y="182" text-anchor="middle" font-size="10" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">inerte</text><rect x="89.7" y="150" width="183.5" height="42" fill="#0f6e56" fill-opacity="0.14" stroke="#0f6e56" stroke-width="1.2"/><text x="181.5" y="167" text-anchor="middle" font-size="10" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">base</text><text x="181.5" y="182" text-anchor="middle" font-size="10" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">faible</text><rect x="273.3" y="150" width="55.2" height="42" fill="#64748b" fill-opacity="0.14" stroke="#64748b" stroke-width="1.2"/><text x="300.885" y="167" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">base</text><text x="300.885" y="182" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">forte</text><text x="89.73" y="18" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1,74</text><text x="273.27" y="18" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">15,74</text><line x1="24.0" y1="118.0" x2="330.0" y2="118.0" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,118 328,114 328,122" fill="#0f172a"/><line x1="55.5" y1="114.0" x2="55.5" y2="122.0" stroke="#0f172a" stroke-width="1.4"/><text x="55.5" y="136" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−5</text><line x1="108.0" y1="114.0" x2="108.0" y2="122.0" stroke="#0f172a" stroke-width="1.4"/><text x="108" y="136" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="160.5" y1="114.0" x2="160.5" y2="122.0" stroke="#0f172a" stroke-width="1.4"/><text x="160.5" y="136" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="213.0" y1="114.0" x2="213.0" y2="122.0" stroke="#0f172a" stroke-width="1.4"/><text x="213" y="136" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="265.5" y1="114.0" x2="265.5" y2="122.0" stroke="#0f172a" stroke-width="1.4"/><text x="265.5" y="136" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">15</text><line x1="318.0" y1="114.0" x2="318.0" y2="122.0" stroke="#0f172a" stroke-width="1.4"/><text x="318" y="136" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="334" y="108" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pKa</text><circle cx="34.5" cy="118" r="5" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/><text x="34.5" y="104" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">HCl</text><line x1="89.7" y1="92.0" x2="89.7" y2="113.0" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2 3"/><circle cx="89.7" cy="118" r="5" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/><text x="89.73" y="88" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">H₃O⁺</text><circle cx="128.4" cy="118" r="5" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/><text x="128.37" y="104" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">HSO₄⁻</text><line x1="157.9" y1="92.0" x2="157.9" y2="113.0" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2 3"/><circle cx="157.9" cy="118" r="5" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/><text x="157.875" y="88" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">CH₃COOH</text><circle cx="186.8" cy="118" r="5" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/><text x="186.75" y="104" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">HClO</text><line x1="205.1" y1="92.0" x2="205.1" y2="113.0" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2 3"/><circle cx="205.1" cy="118" r="5" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/><text x="205.125" y="88" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">NH₄⁺</text><circle cx="273.3" cy="118" r="5" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/><text x="273.27" y="104" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">H₂O</text></svg>
:::

::: exemple Mesurer le Kₐ de l'acide éthanoïque

On reprend la solution de C = 1,0·10⁻² mol·L⁻¹ de pH 3,38 (tableau précédent).
1. La réaction (5) s'écrit CH₃COOH + H₂O ⇄ CH₃COO⁻ + H₃O⁺, donc Kₐ = [H₃O⁺]·[CH₃COO⁻] / [CH₃COOH].
2. [H₃O⁺] = 10⁻³·³⁸ = 4,2·10⁻⁴ mol·L⁻¹, et chaque réaction forme autant d'ions CH₃COO⁻ que d'ions H₃O⁺ : [CH₃COO⁻] = 4,2·10⁻⁴ mol·L⁻¹.
3. Le taux d'avancement vaut 4,2·10⁻² : il reste 96 % de l'acide, on peut confondre [CH₃COOH] avec C = 1,0·10⁻² mol·L⁻¹.
4. Kₐ ≈ (4,2·10⁻⁴)² / 1,0·10⁻² = 1,8·10⁻⁵, d'où pKₐ = −log(1,8·10⁻⁵) = 4,75.
5. Cette valeur est comprise entre −1,74 et 15,74 : l'acide éthanoïque est un acide faible, ce que τ_f < 1 avait déjà montré.

:::

::: piege
**Erreur : croire qu'un acide est d'autant plus fort que son pKₐ est grand.** On compare l'acide éthanoïque (pKₐ = 4,75) et l'acide méthanoïque (pKₐ = 3,75) et l'on dit que le premier est le plus fort puisque 4,75 est plus grand. L'erreur tente parce que, d'habitude, « plus grand » veut dire « plus fort » ; mais pKₐ = −log Kₐ varie en sens inverse de Kₐ. Pour le méthanoïque, Kₐ = 10⁻³·⁷⁵ = 1,8·10⁻⁴, supérieure à 1,8·10⁻⁵ : c'est l'acide méthanoïque le plus fort.
:::

::: propriete
**Classer les acides par pKₐ** — Un acide est fort si pKₐ < −1,74, c'est-à-dire s'il est plus fort que H₃O⁺ ; faible si −1,74 < pKₐ < 15,74 ; inerte si pKₐ > 15,74. Un acide fort réagit pratiquement totalement avec l'eau, même quand son Kₐ (10² pour HNO₃) reste loin du repère 10⁴ : ce repère suppose des réactifs en quantités égales, alors que l'eau, solvant, est en très large excès devant l'acide dissous. Il ne reste de l'acide que des traces. Parmi des acides faibles, le plus fort est celui de plus petit pKₐ.
Cas : HCl (pKₐ = −7) et HNO₃ (pKₐ = −2) sont forts ; CH₃COOH (4,75) et NH₄⁺ (9,25) sont faibles ; CH₃OH (pKₐ ≈ 15,9) est inerte.
Cas limite : les deux bornes viennent des couples de l'eau. Pour H₃O⁺/H₂O, l'eau étant ici l'acide ou la base du couple étudié et non plus seulement le solvant, le manuel garde sa concentration : Kₐ = [H₂O] = 55,35 (concentration de l'eau, en mol·L⁻¹), donc pKₐ = −1,74. Pour H₂O/OH⁻, Kₐ = Kₑ / [H₂O] = 1,0·10⁻¹⁴ / 55,35 = 1,8·10⁻¹⁶, donc pKₐ = 15,74.
:::

::: verifie À toi : du Kₐ au pKₐ
Pour le couple HClO/ClO⁻, Kₐ = 3,16·10⁻⁸ à 25 °C. Calculer le pKₐ, classer l'acide HClO et dire s'il est plus fort ou plus faible que l'acide éthanoïque (pKₐ = 4,75).

---

pKₐ = −log(3,16·10⁻⁸) = 7,50. Comme −1,74 < 7,50 < 15,74, HClO est un acide faible. Son pKₐ est supérieur à 4,75 : il est moins fort que l'acide éthanoïque.
:::

::: retenir
Kₐ = [H₃O⁺]·[Base] / [Acide] et pKₐ = −log Kₐ ; plus Kₐ est grande et pKₐ faible, plus l'acide est fort. Fort si pKₐ < −1,74, faible entre −1,74 et 15,74, inerte au-delà.
:::

## 🔗 La constante de basicité K_b et la relation Kₐ·K_b = Kₑ

L'ion cyanure CN⁻ est la base conjuguée de l'acide cyanhydrique HCN, de pKₐ = 9,30. Comme pour les acides, on voudrait un nombre qui classe les bases sur une échelle indépendante de la concentration.
Ce nombre est-il lié au Kₐ du même couple ?

::: definition
**Constante de basicité K_b, pK_b** — On compare toutes les bases à une même base de référence, OH⁻, du couple H₂O/OH⁻. Pour un couple Acideᵢ/Baseᵢ, on considère la réaction Baseᵢ + H₂O ⇄ OH⁻ + Acideᵢ (6). Sa constante d'équilibre est la constante de basicité K_bᵢ : K_bᵢ = [OH⁻]·[Acideᵢ] / [Baseᵢ] à l'équilibre dynamique. On définit pK_b = −log K_b. Une base est d'autant plus forte que K_b est grande et que pK_b est faible.
:::

Pour un même couple, les réactions (5) et (6) ont pour somme la réaction (2) d'ionisation propre de l'eau :

| Réaction | Constante |
| -------- | --------- |
| Acide + H₂O ⇄ H₃O⁺ + Base (5) | Kₐ |
| Base + H₂O ⇄ OH⁻ + Acide (6) | K_b |
| somme : 2 H₂O ⇄ H₃O⁺ + OH⁻ (2) | Kₑ |

Quand on additionne deux équations pour en obtenir une troisième, les constantes se multiplient : Kₐ·K_b = Kₑ, c'est-à-dire pKₐ + pK_b = pKₑ, soit 14 à 25 °C.

::: exemple Passer du pKₐ de HCN au pK_b de CN⁻

1. La réaction (6) de l'ion cyanure s'écrit CN⁻ + H₂O ⇄ OH⁻ + HCN, donc K_b = [OH⁻]·[HCN] / [CN⁻].
2. À 25 °C, pK_b = 14 − pKₐ = 14 − 9,30 = 4,70.
3. Donc K_b = 10⁻⁴·⁷⁰ = 2,0·10⁻⁵.
4. Le pK_b est compris entre −1,74 et 15,74 : CN⁻ est une base faible, comme HCN est un acide faible.
5. Aux extrémités : HCl a un pKₐ de −7, donc le pK_b de Cl⁻ vaut 14 − (−7) = 21 : Cl⁻ est une base inerte. NH₃/NH₂⁻ a un pKₐ de 23, donc le pK_b de NH₂⁻ vaut −9 : NH₂⁻ est une base forte.

:::

::: piege
**Erreur : croire qu'un acide fort a une base conjuguée forte.** On dit que, HCl étant un acide fort, l'ion Cl⁻ est une base forte. L'erreur tente parce que le mot « fort » se répète ; mais Kₐ·K_b = Kₑ est constant : si Kₐ grandit, K_b diminue. HCl a un pKₐ de −7 et Cl⁻ un pK_b de 21 : plus l'acide est fort, plus sa base conjuguée est faible, au point d'être inerte.
:::

::: propriete
**Relation entre la force d'un acide et celle de sa base conjuguée** — Pour un couple, Kₐ·K_b = Kₑ et pKₐ + pK_b = pKₑ : les deux forces varient en sens inverse, et pKₐ suffit à caractériser le couple. Un acide fort est conjugué à une base inerte ; un acide faible, à une base faible ; un acide inerte, à une base forte.
Cas : pour NH₄⁺/NH₃, pKₐ = 9,25 donne pK_b = 4,75 et K_b = 1,8·10⁻⁵ ; pour CH₃COOH/CH₃COO⁻, pK_b = 9,25.
Cas limite : la somme vaut 14 seulement à 25 °C. À 60 °C, pKₑ = 13,0 : pour un acide de pKₐ = 9,30, le pK_b de sa base vaut alors 13,0 − 9,30 = 3,70.
:::

::: verifie À toi : un autre couple
Pour HNO₂/NO₂⁻, pKₐ = 3,30 à 25 °C. Calculer le pK_b et le K_b de NO₂⁻ et classer cette base.

---

pK_b = 14 − 3,30 = 10,70, donc K_b = 10⁻¹⁰·⁷⁰ = 2,0·10⁻¹¹. Comme −1,74 < 10,70 < 15,74, NO₂⁻ est une base faible, conjuguée de l'acide faible HNO₂.
:::

::: retenir
K_b = [OH⁻]·[Acide] / [Base] ; Kₐ·K_b = Kₑ et pKₐ + pK_b = 14 à 25 °C. Acide fort ↔ base inerte, acide faible ↔ base faible, acide inerte ↔ base forte.
:::

## 🧮 La constante K d'une réaction acide-base à partir des pKₐ

Jusqu'ici, la constante K d'une réaction acide-base était donnée. Mélangeons de l'acide éthanoïque et des ions cyanure : CH₃COOH + CN⁻ ⇄ CH₃COO⁻ + HCN (7). On connaît les pKₐ des deux couples, 4,75 et 9,30.
Peut-on en déduire K, et donc prévoir si (7) va loin ?

::: definition
**K d'une réaction acide-base** — Pour Acide₁ + Base₂ ⇄ Acide₂ + Base₁, K = Kₐ₁ / Kₐ₂, où Kₐ₁ est la constante d'acidité du couple Acide₁/Base₁ (celui de l'acide qui est à gauche) et Kₐ₂ celle du couple Acide₂/Base₂. En pKₐ : log K = pKₐ₂ − pKₐ₁.
:::

Pour l'établir, on multiplie le numérateur et le dénominateur de Π par [H₃O⁺] :

| Étape | Expression |
| ----- | ---------- |
| Π de la réaction | [Acide₂]·[Base₁] / ([Acide₁]·[Base₂]) |
| numérateur et dénominateur multipliés par [H₃O⁺] | ([H₃O⁺]·[Base₁] / [Acide₁]) / ([H₃O⁺]·[Base₂] / [Acide₂]) |
| à l'équilibre | Kₐ₁ / Kₐ₂ = K |

::: exemple Calculer K pour (7) et comparer les forces

1. Ici Acide₁ = CH₃COOH (pKₐ₁ = 4,75), Base₂ = CN⁻, Acide₂ = HCN (pKₐ₂ = 9,30), Base₁ = CH₃COO⁻.
2. K = Kₐ₁ / Kₐ₂, donc log K = pKₐ₂ − pKₐ₁ = 9,30 − 4,75 = 4,55, soit K = 10⁴·⁵⁵ = 3,5·10⁴.
3. K est très grande : (7) est pratiquement totale à partir de quantités égales de réactifs.
4. K > 1 : l'acide de gauche, CH₃COOH, est plus fort que HCN, ce que les pKₐ (4,75 < 9,30) avaient déjà indiqué.

:::

::: piege
**Erreur : inverser le rapport, K = Kₐ₂ / Kₐ₁.** On trouve log K = 4,75 − 9,30 = −4,55, soit K = 2,8·10⁻⁵, et l'on conclut que (7) n'avance presque pas. L'erreur tente parce que l'on écrit parfois « produits sur réactifs » en pensant aux pKₐ des produits au numérateur ; mais le rapport est celui de l'acide réactif à l'acide produit : K = Kₐ(acide à gauche) / Kₐ(acide à droite). Ici l'acide à gauche est le plus fort, donc K est grande.
:::

::: propriete
**K d'une réaction acide-base** — K = Kₐ₁ / Kₐ₂ = 10^(pKₐ₂ − pKₐ₁). Si K > 1, l'Acide₁ est plus fort que l'Acide₂ ; si K < 1, c'est l'Acide₂ ; si K = 1, leurs forces sont équivalentes. La somme de deux équations a pour constante le produit des constantes.
Cas : HNO₂ + CH₃COO⁻ ⇄ NO₂⁻ + CH₃COOH a pour log K = 4,75 − 3,30 = 1,45, donc K = 28 : HNO₂ est plus fort que CH₃COOH.
Cas limite : si l'un des deux couples est H₂O/OH⁻, c'est Kₑ qui intervient, non le Kₐ de H₂O/OH⁻ : CH₃COOH + OH⁻ ⇄ CH₃COO⁻ + H₂O a pour K = Kₐ(CH₃COOH) / Kₑ, soit log K = 14 − 4,75 = 9,25.
:::

::: verifie À toi : une autre réaction
Calculer K pour HClO + NH₃ ⇄ ClO⁻ + NH₄⁺ avec pKₐ(HClO) = 7,50 et pKₐ(NH₄⁺) = 9,25, et dire quel acide est le plus fort.

---

Acide₁ = HClO (7,50), Acide₂ = NH₄⁺ (9,25) : log K = 9,25 − 7,50 = 1,75, K = 10¹·⁷⁵ = 56 ; K > 1 : HClO est plus fort que NH₄⁺.
:::

::: retenir
K = Kₐ(acide à gauche) / Kₐ(acide à droite), soit log K = pKₐ(droite) − pKₐ(gauche) ; K > 1 si l'acide de gauche est le plus fort. Avec le couple H₂O/OH⁻, on utilise Kₑ.
:::
