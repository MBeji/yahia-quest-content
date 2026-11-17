# ⚖️ Loi d'action de masse — prévoir le sens d'évolution d'un système

> 💡 «Un système qui n'est pas à l'équilibre sait dans quel sens aller : il se rapproche de K, et un simple nombre suffit à le prévoir.»

Dans un erlenmeyer, on réunit à la fois de l'acide éthanoïque, de l'éthanol, de l'éthanoate d'éthyle et de l'eau. Qui est réactif, qui est produit ? Le mélange évolue-t-il, et dans quel sens, sans qu'on ait besoin de faire l'expérience ? Huit notions permettent de répondre : la fonction des concentrations Π, l'eau solvant et la fonction usuelle, le calcul de Π à partir des quantités de matière, la loi d'action de masse et la constante K, la constante de la réaction inverse et d'une somme de réactions, l'intérêt de la valeur de K, la comparaison de Π et de K pour prévoir le sens, et la composition à l'équilibre. On suppose acquis l'avancement x et le tableau descriptif (chapitre 1), ainsi que le taux d'avancement final et l'équilibre dynamique (chapitre 4).

## 🧮 La fonction des concentrations Π

Dans un erlenmeyer, on met 0,20 mol d'acide éthanoïque, 0,20 mol d'éthanol, 0,10 mol d'éthanoate d'éthyle et 0,10 mol d'eau, avec un peu d'acide sulfurique. Les quatre entités sont présentes dès le départ : aucune ne peut être appelée seulement « réactif » ou seulement « produit ».
Comment résumer la composition d'un tel système par un seul nombre, qui dira ensuite s'il évolue ?

::: definition
**Fonction des concentrations Π** — Pour l'équation chimique aA + bB ⇄ cC + dD, dont toutes les entités sont dissoutes dans une seule phase liquide, on définit Π = [C]ᶜ[D]ᵈ / ([A]ᵃ[B]ᵇ). Au numérateur figurent les entités écrites à droite de l'équation, au dénominateur celles écrites à gauche, chacune avec pour exposant son coefficient stœchiométrique. Π est sans dimension : [X] représente la valeur numérique de la concentration molaire de X exprimée en mol·L⁻¹.
:::

Pour l'équation CH₃CO₂H + CH₃CH₂OH ⇄ CH₃CO₂CH₂CH₃ + H₂O, chaque entité occupe une place imposée par son côté de l'équation :

| entité           | côté de l'équation | coefficient | facteur dans Π            |
| ---------------- | ------------------ | ----------- | ------------------------- |
| CH₃CO₂H          | gauche             | 1           | [CH₃CO₂H] au dénominateur |
| CH₃CH₂OH         | gauche             | 1           | [CH₃CH₂OH] au dénominateur |
| CH₃CO₂CH₂CH₃     | droite             | 1           | [CH₃CO₂CH₂CH₃] au numérateur |
| H₂O              | droite             | 1           | [H₂O] au numérateur       |

Chaque ligne du tableau est un facteur de Π : les quatre coefficients valent 1, donc aucun exposant n'apparaît.

::: exemple Écrire Π pour deux équations

1. Pour l'équation de l'erlenmeyer, les entités de droite vont au numérateur et celles de gauche au dénominateur, d'après la règle : Π = [CH₃CO₂CH₂CH₃][H₂O] / ([CH₃CO₂H][CH₃CH₂OH]).
2. Pour S₂O₈²⁻ + 2 I⁻ ⇄ 2 SO₄²⁻ + I₂ (la réaction du chapitre 4, pratiquement totale, écrite ici avec ⇄ pour définir Π, comme dans le manuel), le produit SO₄²⁻ a pour coefficient 2 et l'ion I⁻ aussi.
3. Chaque coefficient devient l'exposant de sa concentration, car 2 ions SO₄²⁻ apportent chacun un facteur [SO₄²⁻] : Π = [SO₄²⁻]²[I₂] / ([S₂O₈²⁻][I⁻]²).
4. Contrôle : S₂O₈²⁻ et I₂ ont un coefficient 1, donc leur exposant 1 ne s'écrit pas.

:::

::: piege
**Erreur : écrire le coefficient en facteur au lieu de l'exposant.** Pour la même équation, on obtient Π = 2[SO₄²⁻][I₂] / ([S₂O₈²⁻]·2[I⁻]), ce qui est faux. L'erreur tente parce que le coefficient 2 se lit devant le symbole dans l'équation ; mais il compte des entités, et chaque entité apporte un facteur : [I⁻] doit être multipliée par elle-même, d'où [I⁻]². Pour [I⁻] = 0,10 mol·L⁻¹, on a [I⁻]² = 0,010 alors que 2[I⁻] = 0,20.
:::

::: propriete
**Π est attachée à une équation écrite** — La règle ne dépend que de l'équation : coefficient 1, pas d'exposant ; coefficient n, exposant n. Écrire la même équation dans l'autre sens change l'expression, qui devient l'inverse.
Cas limite : l'équation CH₃CO₂CH₂CH₃ + H₂O ⇄ CH₃CO₂H + CH₃CH₂OH a pour fonction Π' = [CH₃CO₂H][CH₃CH₂OH] / ([CH₃CO₂CH₂CH₃][H₂O]), égale à 1/Π pour la même composition.
:::

::: verifie À toi : écrire Π
Écrire la fonction des concentrations Π de l'équation 2 Fe³⁺ + Sn²⁺ ⇄ 2 Fe²⁺ + Sn⁴⁺.

---

Les entités de droite, Fe²⁺ (coefficient 2) et Sn⁴⁺ (coefficient 1), vont au numérateur ; celles de gauche, Fe³⁺ (coefficient 2) et Sn²⁺ (coefficient 1), au dénominateur. Chaque coefficient devient un exposant : Π = [Fe²⁺]²[Sn⁴⁺] / ([Fe³⁺]²[Sn²⁺]).
:::

::: retenir
Π = [C]ᶜ[D]ᵈ / ([A]ᵃ[B]ᵇ) : produits au numérateur, réactifs au dénominateur, coefficients en exposants (jamais en facteurs), et Π n'a pas d'unité.
:::

## 💧 L'eau solvant et la fonction usuelle

L'eau pure s'ionise très peu : 2 H₂O ⇄ H₃O⁺ + OH⁻. Avec la règle précédente, Π = [H₃O⁺][OH⁻] / [H₂O]².
Mais que vaut [H₂O], et change-t-elle quand la réaction avance ? Un litre d'eau pure à 25 °C a une masse de 997 g (masse volumique ρ = 997 g·L⁻¹), et M(H₂O) = 18,0 g·mol⁻¹.

::: definition
**Fonction usuelle des concentrations** — Dans une solution aqueuse diluée, l'eau joue le rôle de solvant : sa concentration est constante à température constante, et on ne la fait pas figurer dans l'expression de Π. La fonction ainsi obtenue, qui reste notée Π, s'appelle la fonction usuelle des concentrations. Pour l'ionisation propre de l'eau, Π = [H₃O⁺][OH⁻].
:::

::: exemple Que vaut [H₂O], et que devient Π ?

1. Un litre d'eau pure contient n(H₂O) = m/M = 997/18,0 = 55,4 mol, d'où [H₂O] = ρ/M = 55,4 mol·L⁻¹.
2. Dans une solution d'acide éthanoïque à 0,10 mol·L⁻¹, la réaction avec l'eau consomme au plus 0,10 mol d'eau par litre, car l'acide est le réactif limitant : [H₂O] passe au pire de 55,4 à 55,3 mol·L⁻¹, soit une variation de 0,2 %.
3. Une grandeur qui varie de 0,2 % est constante en pratique : on convient de ne plus écrire [H₂O], donc Π = [H₃O⁺][OH⁻] pour l'eau.
4. Pour HF + H₂O ⇄ F⁻ + H₃O⁺ en solution aqueuse diluée, la même convention donne Π = [F⁻][H₃O⁺] / [HF].

:::

::: piege
**Erreur : supprimer l'eau de Π dans l'estérification.** Écrire Π = [CH₃CO₂CH₂CH₃] / ([CH₃CO₂H][CH₃CH₂OH]) est faux. L'erreur tente parce que l'eau est présente dans tous les mélanges ; mais ici elle n'est pas le solvant, elle est un produit dont la quantité varie. Dans l'erlenmeyer, n(H₂O) vaut 0,10 mol au départ et 0,20 mol quand l'avancement atteint 0,10 mol : elle double, elle n'est pas constante, donc [H₂O] figure dans Π.
:::

::: propriete
**Quand l'eau disparaît de Π** — L'eau n'est omise que si elle est le solvant d'une solution aqueuse diluée. Pour un mélange comme l'estérification, où l'eau est un constituant parmi d'autres, elle figure comme n'importe quelle entité.
Cas limite : dans 2 H₂O ⇄ H₃O⁺ + OH⁻, l'eau est à la fois solvant et réactif : la convention de la fonction usuelle la retire quand même, ce qui donne Π = [H₃O⁺][OH⁻].
:::

::: verifie À toi : écrire la fonction usuelle
Écrire la fonction usuelle Π de CH₃NH₂ + H₂O ⇄ CH₃NH₃⁺ + OH⁻ en solution aqueuse diluée.

---

L'eau est le solvant d'une solution diluée : sa concentration est constante et n'apparaît pas. Les entités de droite, CH₃NH₃⁺ et OH⁻, vont au numérateur, celle de gauche, CH₃NH₂, au dénominateur, avec des coefficients 1 : Π = [CH₃NH₃⁺][OH⁻] / [CH₃NH₂].
:::

::: retenir
L'eau solvant d'une solution aqueuse diluée a une concentration constante (≈ 55,4 mol·L⁻¹) : elle n'entre pas dans la fonction usuelle Π, mais elle y figure quand elle est un constituant du mélange, comme dans l'estérification.
:::

## 🔢 Calculer Π à partir des quantités de matière

Dans l'erlenmeyer, on connaît des quantités de matière (0,20 mol ; 0,20 mol ; 0,10 mol ; 0,10 mol), pas des concentrations : le volume n'est même pas donné.
Peut-on quand même calculer Π, et que devient-elle quand la réaction avance ?

::: definition
**Concentration molaire** — Pour un constituant X d'un système homogène de volume V, [X] = n(X) / V, où n(X) est la quantité de matière de X dissoute dans le système.
:::

Le tableau descriptif donne la composition en fonction de l'avancement x de l'estérification :

|                     | CH₃CO₂H  | CH₃CH₂OH | CH₃CO₂CH₂CH₃ | H₂O      |
| ------------------- | -------- | -------- | ------------ | -------- |
| état initial (mol)  | 0,20     | 0,20     | 0,10         | 0,10     |
| état intermédiaire (mol) | 0,20 − x | 0,20 − x | 0,10 + x     | 0,10 + x |

::: exemple Calculer Π avec les quantités de matière

1. Π = [ester][eau] / ([acide][alcool]) = (n(ester)/V · n(eau)/V) / (n(acide)/V · n(alcool)/V), d'après la définition de [X].
2. Deux facteurs 1/V figurent au numérateur et deux au dénominateur : V se simplifie, donc Π = n(ester)·n(eau) / (n(acide)·n(alcool)), sans connaître V.
3. À l'état initial, Π = (0,10 × 0,10) / (0,20 × 0,20) = 0,25. Contrôle avec un volume quelconque, par exemple V = 40 mL : les concentrations valent 5,0 ; 5,0 ; 2,5 et 2,5 mol·L⁻¹, d'où Π = (2,5 × 2,5) / (5,0 × 5,0) = 0,25.
4. Pour un avancement x, Π = (0,10 + x)² / (0,20 − x)² : elle vaut 1,0 pour x = 0,05 mol et 4,0 pour x = 0,10 mol, car le numérateur grandit et le dénominateur diminue.

:::

| x (mol) | 0    | 0,05 | 0,08 | 0,10 |
| ------- | ---- | ---- | ---- | ---- |
| Π       | 0,25 | 1,0  | 2,25 | 4,0  |

Chaque colonne du tableau est une valeur de x dans la formule Π = (0,10 + x)² / (0,20 − x)² : Π augmente avec l'avancement de l'estérification.

::: piege
**Erreur : utiliser les quantités de matière quand V ne se simplifie pas.** Pour Fe³⁺ + SCN⁻ ⇄ Fe(SCN)²⁺ avec 2,0·10⁻³ mol de Fe³⁺, 1,0·10⁻³ mol de SCN⁻ et 5,0·10⁻⁴ mol de complexe dans V = 0,100 L, le calcul avec les quantités donne Π = 5,0·10⁻⁴ / (2,0·10⁻³ × 1,0·10⁻³) = 250, ce qui est faux. L'erreur tente parce que V a disparu dans l'estérification ; mais ici il y a un facteur 1/V au numérateur et deux au dénominateur. Avec les concentrations 2,0·10⁻² ; 1,0·10⁻² et 5,0·10⁻³ mol·L⁻¹, on trouve Π = 5,0·10⁻³ / (2,0·10⁻² × 1,0·10⁻²) = 25.
:::

::: propriete
**Π en fonction de n et de x** — V se simplifie quand la somme des coefficients est la même à droite et à gauche de l'équation, comme pour l'estérification : Π se calcule alors avec les quantités de matière. Sinon, il faut diviser chaque quantité par V.
Cas limite : si aucun produit n'est présent, Π = 0 ; si un réactif est absent, le dénominateur est nul et Π devient infiniment grande. Π peut donc prendre n'importe quelle valeur de 0 à l'infini.
:::

::: verifie À toi : calculer Π
Un erlenmeyer contient 0,40 mol d'acide éthanoïque, 0,10 mol d'éthanol, 0,20 mol d'éthanoate d'éthyle et 0,30 mol d'eau, en une seule phase. Calculer Π pour l'équation d'estérification.

---

La somme des coefficients vaut 2 des deux côtés : V se simplifie. Π = n(ester)·n(eau) / (n(acide)·n(alcool)) = (0,20 × 0,30) / (0,40 × 0,10) = 0,060 / 0,040 = 1,5.
:::

::: retenir
[X] = n(X)/V ; quand la somme des coefficients est la même des deux côtés (estérification), V se simplifie et Π se calcule avec les quantités de matière, sinon avec les concentrations ; Π va de 0 à l'infini.
:::

## 📏 La loi d'action de masse et la constante K

On prépare trois tubes à 80 °C, avec de l'acide sulfurique comme catalyseur : (1) 0,100 mol d'acide éthanoïque et 0,100 mol d'éthanol ; (2) 0,100 mol d'acide et 0,300 mol d'éthanol ; (3) 0,100 mol d'éthanoate d'éthyle et 0,100 mol d'eau. Après plusieurs heures, la composition ne change plus ; on dose l'acide présent, et on calcule la valeur finale de Π pour l'équation d'estérification (valeurs d'illustration).

| tube | mélange initial                  | avancement final x_f (mol)    | Π à l'équilibre |
| ---- | -------------------------------- | ----------------------------- | --------------- |
| 1    | 0,100 mol d'acide + 0,100 mol d'alcool | 0,0665 (ester formé)    | 3,94            |
| 2    | 0,100 mol d'acide + 0,300 mol d'alcool | 0,0905 (ester formé)    | 4,12            |
| 3    | 0,100 mol d'ester + 0,100 mol d'eau    | 0,0332 (acide formé)    | 4,05            |

Les compositions finales sont très différentes, mais les trois valeurs de Π sont presque égales.
Est-ce un hasard ?

::: definition
**Loi d'action de masse** — À une température donnée, un système chimique est en équilibre lorsque sa composition est invariante et telle que la fonction des concentrations Π est égale à une constante K, indépendante de la composition initiale : c'est la constante d'équilibre. On écrit Πéq = K, avec K = [C]ᶜ[D]ᵈ / ([A]ᵃ[B]ᵇ), les concentrations étant celles de l'état d'équilibre.
:::

::: figure Π(t) pour deux mélanges de départ : la courbe verte monte depuis 0, la courbe orange descend depuis une valeur infinie hors du cadre, et toutes deux se posent sur la ligne pointillée K (courbes calculées pour K = 4, durée choisie pour l'illustration)
<svg viewBox="0 0 340 236"><title>Fonction des concentrations Π en fonction du temps pour deux mélanges de départ</title><line x1="99.3" y1="26" x2="99.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="144.7" y1="26" x2="144.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="190.0" y1="26" x2="190.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="235.3" y1="26" x2="235.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="280.7" y1="26" x2="280.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326.0" y1="26" x2="326.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="149.0" x2="326" y2="149.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="108.0" x2="326" y2="108.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="67.0" x2="326" y2="67.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="26.0" x2="326" y2="26.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="54.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="99.3" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="144.7" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="190.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><text x="235.3" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="280.7" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">50</text><text x="326.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><text x="48.0" y="194.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="48.0" y="153.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="48.0" y="112.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><text x="48.0" y="71.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="48.0" y="30.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><text x="334.0" y="218.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (min)</text><text x="60.0" y="12.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Π</text><line x1="54" y1="108.0" x2="326" y2="108.0" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><polyline points="54.0,190.0 57.0,190.0 60.0,189.8 63.1,189.6 66.1,189.3 69.1,188.9 72.1,188.4 75.2,187.8 78.2,187.0 81.2,186.2 84.2,185.3 87.2,184.2 90.3,183.1 93.3,181.9 96.3,180.5 99.3,179.1 102.4,177.6 105.4,176.0 108.4,174.4 111.4,172.7 114.4,170.9 117.5,169.1 120.5,167.2 123.5,165.3 126.5,163.4 129.6,161.5 132.6,159.6 135.6,157.7 138.6,155.7 141.6,153.8 144.7,151.9 147.7,150.1 150.7,148.2 153.7,146.4 156.8,144.7 159.8,143.0 162.8,141.3 165.8,139.7 168.8,138.1 171.9,136.6 174.9,135.1 177.9,133.7 180.9,132.4 184.0,131.0 187.0,129.8 190.0,128.6 193.0,127.5 196.0,126.4 199.1,125.3 202.1,124.3 205.1,123.4 208.1,122.5 211.2,121.6 214.2,120.8 217.2,120.1 220.2,119.3 223.2,118.6 226.3,118.0 229.3,117.4 232.3,116.8 235.3,116.2 238.4,115.7 241.4,115.2 244.4,114.8 247.4,114.4 250.4,113.9 253.5,113.6 256.5,113.2 259.5,112.9 262.5,112.5 265.6,112.2 268.6,112.0 271.6,111.7 274.6,111.5 277.6,111.2 280.7,111.0 283.7,110.8 286.7,110.6 289.7,110.4 292.8,110.3 295.8,110.1 298.8,109.9 301.8,109.8 304.8,109.7 307.9,109.6 310.9,109.4 313.9,109.3 316.9,109.2 320.0,109.1 323.0,109.1 326.0,109.0" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="124.3,27.9 125.4,30.8 126.5,33.5 127.7,36.2 128.8,38.7 129.9,41.1 131.1,43.4 132.2,45.6 133.3,47.7 134.5,49.7 135.6,51.7 136.7,53.5 137.9,55.3 139.0,57.0 140.1,58.7 141.3,60.2 142.4,61.8 143.5,63.2 144.7,64.6 145.8,66.0 146.9,67.3 148.1,68.5 149.2,69.7 150.3,70.9 151.5,72.0 152.6,73.1 153.7,74.2 154.9,75.2 156.0,76.1 157.1,77.1 158.3,78.0 159.4,78.9 160.5,79.7 161.7,80.5 162.8,81.3 163.9,82.1 165.1,82.8 166.2,83.5 167.3,84.2 168.5,84.9 169.6,85.5 170.7,86.2 171.9,86.8 173.0,87.4 174.1,87.9 175.3,88.5 176.4,89.0 177.5,89.5 178.7,90.0 179.8,90.5 180.9,91.0 182.1,91.5 183.2,91.9 184.3,92.3 185.5,92.8 186.6,93.2 187.7,93.6 188.9,94.0 190.0,94.3 191.1,94.7 192.3,95.0 193.4,95.4 194.5,95.7 195.7,96.0 196.8,96.3 197.9,96.6 199.1,96.9 200.2,97.2 201.3,97.5 202.5,97.8 203.6,98.0 204.7,98.3 205.9,98.5 207.0,98.8 208.1,99.0 209.3,99.2 210.4,99.5 211.5,99.7 212.7,99.9 213.8,100.1 214.9,100.3 216.1,100.5 217.2,100.7 218.3,100.9 219.5,101.0 220.6,101.2 221.7,101.4 222.9,101.5 224.0,101.7 225.1,101.9 226.3,102.0 227.4,102.2 228.5,102.3 229.7,102.4 230.8,102.6 231.9,102.7 233.1,102.8 234.2,103.0 235.3,103.1 236.5,103.2 237.6,103.3 238.7,103.4 239.9,103.5 241.0,103.7 242.1,103.8 243.3,103.9 244.4,104.0 245.5,104.1 246.7,104.1 247.8,104.2 248.9,104.3 250.1,104.4 251.2,104.5 252.3,104.6 253.5,104.7 254.6,104.7 255.7,104.8 256.9,104.9 258.0,105.0 259.1,105.0 260.3,105.1 261.4,105.2 262.5,105.2 263.7,105.3 264.8,105.4 265.9,105.4 267.1,105.5 268.2,105.5 269.3,105.6 270.5,105.6 271.6,105.7 272.7,105.7 273.9,105.8 275.0,105.8 276.1,105.9 277.3,105.9 278.4,106.0 279.5,106.0 280.7,106.1 281.8,106.1 282.9,106.2 284.1,106.2 285.2,106.2 286.3,106.3 287.5,106.3 288.6,106.3 289.7,106.4 290.9,106.4 292.0,106.4 293.1,106.5 294.3,106.5 295.4,106.5 296.5,106.6 297.7,106.6 298.8,106.6 299.9,106.7 301.1,106.7 302.2,106.7 303.3,106.7 304.5,106.8 305.6,106.8 306.7,106.8 307.9,106.8 309.0,106.9 310.1,106.9 311.3,106.9 312.4,106.9 313.5,106.9 314.7,107.0 315.8,107.0 316.9,107.0 318.1,107.0 319.2,107.0 320.3,107.1 321.5,107.1 322.6,107.1 323.7,107.1 324.9,107.1 326.0,107.1" fill="none" stroke="#c2410c" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="235.3" y="138.8" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">acide + alcool</text><text x="235.3" y="79.3" text-anchor="middle" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ester + eau</text><text x="289.7" y="96.7" text-anchor="middle" font-size="12" font-weight="700" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">K</text></svg>
:::

Sur la figure, la ligne pointillée est la constante K de la définition, et les deux courbes sont la fonction Π de mélanges du type des tubes 1 et 3 : l'une l'approche par en dessous, l'autre par au-dessus.

::: exemple Déterminer K à partir des tubes

1. K est la valeur de Π à l'équilibre : pour le tube 1, 0,0665 mol d'ester et d'eau se sont formées, et il reste 0,100 − 0,0665 = 0,0335 mol d'acide et d'alcool.
2. Π = (0,0665 × 0,0665) / (0,0335 × 0,0335) = 3,94, car V se simplifie pour l'estérification.
3. Le tube 2 donne 4,12 et le tube 3 donne 4,05 : les trois valeurs sont voisines de 4, quel que soit le mélange de départ, donc K ≈ 4 à 80 °C.
4. Les écarts viennent des mesures : réactifs non parfaitement purs, concentration de la soude connue avec une précision limitée, un peu d'eau apportée par l'acide sulfurique.

:::

::: piege
**Erreur : écrire Π = K à tout instant.** Pour le tube 1 à t = 0, Π = 0 (il n'y a pas de produit), ce qui est différent de K = 4. L'erreur tente parce que K et Π s'écrivent avec les mêmes concentrations ; mais Π est définie à tout instant, alors que l'égalité Π = K n'est vraie qu'à l'équilibre dynamique.
:::

::: propriete
**K ne dépend que de la température** — Pour une équation écrite et une température données, K a une seule valeur, qui ne dépend ni de la composition initiale ni de la composition finale. La loi d'action de masse est une loi expérimentale, et ce sont les concentrations molaires qui interviennent, non les masses.
Cas limite : Π parcourt toutes les valeurs de 0 à l'infini pendant l'évolution, alors que K reste fixe ; une fois l'équilibre atteint, Π garde cette valeur au cours du temps.
:::

::: verifie À toi : calculer K
À 80 °C, un système d'estérification atteint l'équilibre avec 0,15 mol d'acide, 0,15 mol d'alcool, 0,30 mol d'ester et 0,30 mol d'eau. Calculer K, puis dire s'il faut connaître le mélange de départ pour prévoir cette valeur.

---

À l'équilibre, K = Π = (0,30 × 0,30) / (0,15 × 0,15) = 0,090 / 0,0225 = 4,0. Non : K est indépendante de la composition initiale, elle ne dépend que de la température et de l'équation écrite.
:::

::: retenir
À température donnée, Π prend à l'équilibre une valeur K indépendante de la composition initiale (Πéq = K) ; l'égalité Π = K n'est vraie qu'à l'équilibre, jamais à tout instant.
:::

## 🔄 La constante de la réaction inverse et d'une somme de réactions

L'estérification a pour constante K = 4. L'hydrolyse de l'ester est la même transformation lue dans l'autre sens, et la même transformation se produit parfois en plusieurs étapes.
Quelle est la constante de l'hydrolyse, et comment relier la constante d'une réaction globale à celles de ses étapes ?

::: exemple Inverser une équation, puis additionner deux équations

1. L'estérification CH₃CO₂H + CH₃CH₂OH ⇄ CH₃CO₂CH₂CH₃ + H₂O a pour fonction Π = [ester][eau] / ([acide][alcool]) et pour constante K = 4.
2. L'hydrolyse a pour fonction Π' = [acide][alcool] / ([ester][eau]), qui est l'inverse de Π : à l'équilibre, K' = 1/K = 1/4 = 0,25.
3. Pour la complexation en deux étapes, on donne (1) Fe³⁺ + SCN⁻ ⇄ Fe(SCN)²⁺ avec K₁ = 1,25·10⁵ (valeur à 25 °C) et (2) Fe(SCN)²⁺ + SCN⁻ ⇄ Fe(SCN)₂⁺ avec K₂ = 20 (valeur donnée). L'équation (3) Fe³⁺ + 2 SCN⁻ ⇄ Fe(SCN)₂⁺ est la somme de (1) et de (2).
4. Π₃ = [Fe(SCN)₂⁺] / ([Fe³⁺][SCN⁻]²) = Π₁·Π₂, car la concentration de Fe(SCN)²⁺ se simplifie dans le produit : à l'équilibre, K₃ = K₁·K₂ = 1,25·10⁵ × 20 = 2,5·10⁶.
5. La dissociation Fe(SCN)₂⁺ ⇄ Fe³⁺ + 2 SCN⁻ est l'inverse de (3), donc sa constante vaut 1/K₃ = 4,0·10⁻⁷.

:::

::: piege
**Erreur : additionner les constantes quand on additionne les équations.** Écrire K₃ = K₁ + K₂ ≈ 1,25·10⁵ est faux. L'erreur tente parce que l'équation (3) est la somme de (1) et de (2) ; mais les fonctions se multiplient (Π₃ = Π₁·Π₂), donc les constantes aussi. On trouve K₃ = 2,5·10⁶, vingt fois plus grande que 1,25·10⁵.
:::

::: propriete
**Inverse et somme** — Si l'on inverse une équation, sa fonction devient Π' = 1/Π et sa constante K' = 1/K. Si l'équation (3) est la somme de (1) et de (2), alors Π₃ = Π₁·Π₂ et K₃ = K₁·K₂.
Cas limite : Π₃ = Π₁·Π₂ vient de l'écriture et est vraie à tout instant ; K₃ = K₁·K₂ suppose que les trois réactions sont à l'équilibre dans le même système.
:::

::: verifie À toi : constante d'une somme et de son inverse
On donne Cu²⁺ + NH₃ ⇄ Cu(NH₃)²⁺ avec K₁ = 2,0·10⁴ et Cu(NH₃)²⁺ + NH₃ ⇄ Cu(NH₃)₂²⁺ avec K₂ = 5,0·10³. Calculer la constante de Cu²⁺ + 2 NH₃ ⇄ Cu(NH₃)₂²⁺, puis celle de la réaction inverse.

---

L'équation demandée est la somme des deux équations : les fonctions se multiplient, donc K₃ = K₁·K₂ = 2,0·10⁴ × 5,0·10³ = 1,0·10⁸. La réaction inverse a la fonction inverse : K₃' = 1/K₃ = 1,0·10⁻⁸.
:::

::: retenir
Réaction inverse : K' = 1/K ; somme de deux équations : K₃ = K₁·K₂, et jamais K₁ + K₂.
:::

## 🧭 L'intérêt de la valeur de K

Trois réactions ont, à 25 °C, les constantes suivantes : HF + NH₃ ⇄ F⁻ + NH₄⁺ avec K = 1,07·10⁶ ; l'estérification HCOOH + CH₃CH₂CH₂OH ⇄ HCOOCH₂CH₂CH₃ + H₂O avec K = 4 ; CH₃COOH + H₂O ⇄ CH₃COO⁻ + H₃O⁺ avec K = 1,6·10⁻⁵.
Sans résoudre aucune équation, que peut-on dire de la composition finale de chacune ?

::: definition
**K et réaction totale ou limitée** — Quand K est très grande (supérieure à 10⁴), la réaction est pratiquement totale : son taux d'avancement final τ_f est voisin de 1. Une réaction limitée, de τ_f inférieur à 1, a une constante inférieure à 10⁴.
:::

Pour A + B ⇄ C + D en mélange équimolaire à volume constant, τ_f = √K / (1 + √K), ce qui relie K et τ_f :

| K     | 10⁻⁴  | 1    | 4    | 10⁴   | 10⁶    |
| ----- | ----- | ---- | ---- | ----- | ------ |
| τ_f   | 0,010 | 0,50 | 0,67 | 0,990 | 0,999  |

Les valeurs de τ_f grandissent avec K sans jamais dépasser 1 : K = 4 donne τ_f = 0,67, la valeur de l'estérification du chapitre 4.

::: exemple Prévoir la composition sans second degré

1. HF + NH₃ ⇄ F⁻ + NH₄⁺, en partant de [HF] = [NH₃] = 0,020 mol·L⁻¹ : comme K est très grande, presque tout réagit, donc [F⁻] = [NH₄⁺] ≈ 0,020 mol·L⁻¹ et il reste y = [HF] = [NH₃].
2. K = [F⁻][NH₄⁺] / ([HF][NH₃]) ≈ 0,020² / y² = 1,07·10⁶, d'où y = 0,020 / √(1,07·10⁶) = 1,9·10⁻⁵ mol·L⁻¹, soit 0,1 % de 0,020 : τ_f ≈ 0,999, la réaction est pratiquement totale.
3. CH₃COOH + H₂O ⇄ CH₃COO⁻ + H₃O⁺, pour CH₃COOH à 0,10 mol·L⁻¹ : [CH₃COO⁻] = [H₃O⁺] = y, et [CH₃COOH] = 0,10 − y ≈ 0,10, car K est très petite.
4. K = y² / 0,10 = 1,6·10⁻⁵ (l'eau solvant n'apparaît pas), d'où y = √(1,6·10⁻⁶) = 1,3·10⁻³ mol·L⁻¹ et τ_f = 1,3·10⁻³ / 0,10 = 0,013 : la réaction est limitée, moins de 2 % de l'acide a réagi.

:::

::: piege
**Erreur : croire qu'une constante K très grande rend la réaction rapide.** K n'indique que la composition finale, jamais la durée. L'oxydation des ions iodure par les ions peroxodisulfate (chapitre 4) est pratiquement totale et pourtant elle dure plus d'une heure. L'erreur tente parce que « grande » évoque « vite » ; mais K est un rapport de concentrations à l'équilibre, qui ne contient aucune durée.
:::

::: propriete
**Lire K** — Si K > 10⁴, le réactif limitant a pratiquement disparu et la composition se prévoit sans calcul compliqué ; si K < 10⁴, la réaction est limitée et τ_f est inférieur à 1.
Cas limite : 10⁴ est un repère, pas une frontière nette. Plus K est petite, plus τ_f est faible : K = 4 donne τ_f = 0,67, un mélange où réactifs et produits sont en quantité appréciable, alors que K = 5,0·10⁻³ ne donne que τ_f ≈ 0,07.
:::

::: verifie À toi : classer trois réactions
Trois réactions ont pour constantes K₁ = 8,0·10⁶, K₂ = 5,0·10⁻³ et K₃ = 25. Lesquelles sont pratiquement totales ?

---

Seule la première, car 8,0·10⁶ est supérieure à 10⁴ : τ_f est voisin de 1. Les deux autres sont limitées parce que leur constante est inférieure à 10⁴ : K₂ = 5,0·10⁻³ donne peu de produits, K₃ = 25 laisse des réactifs en quantité appréciable.
:::

::: retenir
K > 10⁴ : réaction pratiquement totale (τ_f voisin de 1) ; K < 10⁴ : réaction limitée (τ_f < 1) ; K décrit la composition finale, jamais la rapidité.
:::

## 🎯 Prévoir le sens d'évolution : comparer Π et K

On prépare à 80 °C trois erlenmeyers d'estérification, de constante K = 4, avec de l'acide sulfurique. Après 10 minutes, on dose l'acide éthanoïque présent (valeurs d'illustration).

| erlenmeyer | acide (mol) | alcool (mol) | ester (mol) | eau (mol) | Π   | acide après 10 min |
| ---------- | ----------- | ------------ | ----------- | --------- | --- | ------------------ |
| S₁         | 0,30        | 0,10         | 0,15        | 0,20      | 1,0 | a diminué          |
| S₂         | 0,20        | 0,10         | 0,20        | 0,40      | 4,0 | n'a pas changé     |
| S₃         | 0,10        | 0,10         | 0,30        | 0,30      | 9,0 | a augmenté         |

L'acide diminue dans un cas, reste constant dans un autre et augmente dans le dernier.
Peut-on prévoir ces trois comportements sans faire l'expérience ?

::: definition
**Conditions d'évolution spontanée** — La réaction possible spontanément est celle qui rapproche Π de K. Si Π < K, c'est la réaction directe ; si Π > K, c'est la réaction inverse ; si Π = K, le système est en équilibre dynamique et il ne se produit aucune transformation à notre échelle.
:::

::: figure Axe des valeurs de Π avec K = 4 : à gauche de K, Π doit grandir et la réaction directe se produit ; à droite de K, Π doit diminuer et la réaction inverse se produit
<svg viewBox="0 0 340 170"><title>Axe des valeurs de Π avec K = 4 : sens de la réaction possible spontanément</title><rect x="50.0" y="58" width="104.0" height="34" fill="#0f6e56" opacity="0.12"/><rect x="154.0" y="58" width="156.0" height="34" fill="#c2410c" opacity="0.12"/><line x1="50.0" y1="75" x2="330" y2="75" stroke="#0f172a" stroke-width="2"/><polygon points="334,75 326,71 326,79" fill="#0f172a"/><line x1="50.0" y1="69" x2="50.0" y2="81" stroke="#0f172a" stroke-width="1.6"/><line x1="76.0" y1="69" x2="76.0" y2="81" stroke="#0f172a" stroke-width="1.6"/><line x1="154.0" y1="69" x2="154.0" y2="81" stroke="#0f172a" stroke-width="1.6"/><line x1="284.0" y1="69" x2="284.0" y2="81" stroke="#0f172a" stroke-width="1.6"/><line x1="154.0" y1="50" x2="154.0" y2="100" stroke="#0f172a" stroke-width="2.4"/><text x="50.0" y="96.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="76.0" y="96.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="284.0" y="96.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">9</text><text x="154.0" y="112.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">K = 4</text><text x="102.0" y="42.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Π &lt; K : sens direct</text><text x="232.0" y="42.0" text-anchor="middle" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Π &gt; K : sens inverse</text><text x="76.0" y="132.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S₁ (Π = 1)</text><text x="284.0" y="132.0" text-anchor="middle" font-size="11" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S₃ (Π = 9)</text><text x="154.0" y="150.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S₂ (Π = 4) : équilibre</text><path d="M84.0 118 L124.0 118" stroke="#0f6e56" stroke-width="2" fill="none"/><polygon points="128.0,118 121.0,114 121.0,122" fill="#0f6e56"/><path d="M276.0 118 L184.0 118" stroke="#c2410c" stroke-width="2" fill="none"/><polygon points="180.0,118 187.0,114 187.0,122" fill="#c2410c"/></svg>
:::

Sur la figure, S₁, S₂ et S₃ sont placés à la valeur de leur Π du tableau, et les flèches montrent que la réaction possible déplace toujours Π vers K.

::: exemple Prévoir le sens pour trois systèmes

1. S₁ : Π = 1,0 est inférieure à K = 4, donc la réaction directe est possible spontanément : l'estérification fait grandir le numérateur de Π et diminuer son dénominateur, donc l'acide diminue.
2. S₃ : Π = 9,0 est supérieure à K = 4, donc c'est la réaction inverse, l'hydrolyse : elle fait diminuer Π, et l'acide augmente.
3. S₂ : Π = 4,0 est égale à K, donc il n'y a aucune évolution à notre échelle : l'acide n'a pas changé, mais les deux réactions se poursuivent à vitesses égales (chapitre 4).
4. Un système acide-base se traite de même. Pour HF + C₂O₄²⁻ ⇄ F⁻ + HC₂O₄⁻ avec K ≈ 10 et [HF] = 0,020 ; [C₂O₄²⁻] = 0,010 ; [F⁻] = 0,10 ; [HC₂O₄⁻] = 0,050 mol·L⁻¹, Π = (0,10 × 0,050) / (0,020 × 0,010) = 25. Comme Π > K, c'est la réaction inverse : HC₂O₄⁻ + F⁻ → HF + C₂O₄²⁻. Une réaction acide-base est très rapide, donc elle se produit dès le mélange.

:::

::: piege
**Erreur : décider du sens en comparant seulement les quantités de produits et de réactifs.** Pour HF + NH₃ ⇄ F⁻ + NH₄⁺ (K = 1,07·10⁶) avec [HF] = [NH₃] = 1,0·10⁻³ et [F⁻] = [NH₄⁺] = 5,0·10⁻² mol·L⁻¹, dire « les produits sont déjà cinquante fois plus concentrés, donc la réaction inverse se produit » est faux. L'erreur tente parce que beaucoup de produits évoque un système « arrivé » ; mais le critère est Π face à K : Π = (5,0·10⁻²)² / (1,0·10⁻³)² = 2,5·10³ est inférieur à K = 1,07·10⁶, donc c'est la réaction directe.
:::

::: propriete
**Π, K et le sens** — À température donnée, K est fixée et c'est Π qui varie jusqu'à la rejoindre. Un système qui reçoit un constituant n'est plus à l'équilibre : Π change, et la réaction qui la ramène vers K se produit. Ces conditions disent quel sens est possible spontanément ; la rapidité relève de la cinétique.
Cas limite : si l'on ajoute 0,20 mol d'eau à S₂ à l'équilibre, n(eau) passe de 0,40 à 0,60 mol et Π = (0,20 × 0,60) / (0,20 × 0,10) = 6,0 devient supérieure à K = 4 : la réaction inverse se produit. Un système sans produit a Π = 0, donc la réaction directe.
:::

::: verifie À toi : prévoir le sens
Pour 2 Fe³⁺ + 2 I⁻ ⇄ I₂ + 2 Fe²⁺ avec K = 1,0·10⁸, un système contient [Fe³⁺] = 0,010 ; [I⁻] = 0,10 ; [I₂] = 1,0·10⁻³ ; [Fe²⁺] = 1,0·10⁻³ mol·L⁻¹. Quelle réaction se produit ?

---

Π = [I₂][Fe²⁺]² / ([Fe³⁺]²[I⁻]²) = (1,0·10⁻³ × (1,0·10⁻³)²) / ((0,010)² × (0,10)²) = 1,0·10⁻⁹ / 1,0·10⁻⁶ = 1,0·10⁻³. Comme Π < K, la réaction directe se produit : les ions Fe³⁺ oxydent les ions iodure en diiode.
:::

::: retenir
Π < K : réaction directe ; Π > K : réaction inverse ; Π = K : équilibre dynamique. On compare toujours Π à K, jamais les quantités de produits et de réactifs entre elles.
:::

## 🧪 La composition à l'équilibre et le taux d'avancement final

On mélange 0,50 mol d'acide éthanoïque et 0,30 mol d'éthanol, avec l'acide sulfurique, à une température où K = 4. Il n'y a ni ester ni eau au départ.
Quelle est la composition finale, et quelle fraction de l'avancement maximal est atteinte ?

::: exemple Du mélange de départ à la composition finale

1. Au départ Π = 0 (pas de produit), donc Π < K : le sens direct est possible. On écrit le tableau : acide 0,50 − x, alcool 0,30 − x, ester x, eau x.
2. À l'équilibre Π = K, donc K = x_f² / ((0,50 − x_f)(0,30 − x_f)) = 4 (V se simplifie), soit x_f² = 4(0,15 − 0,80 x_f + x_f²) et 3 x_f² − 3,20 x_f + 0,60 = 0.
3. Le discriminant vaut 3,20² − 4 × 3 × 0,60 = 3,04, de racine 1,74, donc x_f = (3,20 ± 1,74)/6 : 0,243 mol ou 0,824 mol.
4. L'alcool est le réactif limitant : x_max = 0,30 mol. La racine 0,824 est supérieure à x_max (elle donnerait −0,52 mol d'alcool) : on la rejette, donc x_f = 0,243 mol.
5. Composition : acide 0,257 mol, alcool 0,057 mol, ester = eau = 0,243 mol. Contrôle : Π = 0,243² / (0,257 × 0,057) ≈ 4,0 = K. Enfin τ_f = x_f / x_max = 0,243 / 0,30 = 0,81 : la réaction est limitée.

:::

::: figure Avancement x en fonction du temps : le palier de la courbe est x_f, au-dessous de la ligne pointillée haute x_max (allure choisie pour l'illustration, les valeurs de x_f et de x_max sont celles de l'exemple)
<svg viewBox="0 0 340 236"><title>Avancement x en fonction du temps pour le mélange 0,50 mol d'acide et 0,30 mol d'alcool</title><line x1="99.3" y1="26" x2="99.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="144.7" y1="26" x2="144.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="190.0" y1="26" x2="190.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="235.3" y1="26" x2="235.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="280.7" y1="26" x2="280.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326.0" y1="26" x2="326.0" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="166.6" x2="326" y2="166.6" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="143.1" x2="326" y2="143.1" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="119.7" x2="326" y2="119.7" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="96.3" x2="326" y2="96.3" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="72.9" x2="326" y2="72.9" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="49.4" x2="326" y2="49.4" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="26.0" x2="326" y2="26.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="54.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="99.3" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="144.7" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="190.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><text x="235.3" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="280.7" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">50</text><text x="326.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><text x="48.0" y="194.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,00</text><text x="48.0" y="170.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,05</text><text x="48.0" y="147.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,10</text><text x="48.0" y="123.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,15</text><text x="48.0" y="100.3" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,20</text><text x="48.0" y="76.9" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,25</text><text x="48.0" y="53.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,30</text><text x="48.0" y="30.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,35</text><text x="334.0" y="218.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (min)</text><text x="60.0" y="12.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x (mol)</text><line x1="54" y1="49.4" x2="326" y2="49.4" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><line x1="54" y1="76.3" x2="326" y2="76.3" stroke="#c2410c" stroke-width="1.2" stroke-dasharray="4 3"/><polyline points="54.0,190.0 57.0,183.9 60.0,178.0 63.1,172.5 66.1,167.3 69.1,162.4 72.1,157.8 75.2,153.4 78.2,149.2 81.2,145.3 84.2,141.5 87.2,138.0 90.3,134.7 93.3,131.5 96.3,128.5 99.3,125.7 102.4,123.0 105.4,120.5 108.4,118.1 111.4,115.9 114.4,113.7 117.5,111.7 120.5,109.8 123.5,108.0 126.5,106.3 129.6,104.6 132.6,103.1 135.6,101.7 138.6,100.3 141.6,99.0 144.7,97.8 147.7,96.6 150.7,95.5 153.7,94.5 156.8,93.5 159.8,92.5 162.8,91.7 165.8,90.8 168.8,90.0 171.9,89.3 174.9,88.6 177.9,87.9 180.9,87.3 184.0,86.7 187.0,86.1 190.0,85.6 193.0,85.1 196.0,84.6 199.1,84.2 202.1,83.8 205.1,83.3 208.1,83.0 211.2,82.6 214.2,82.3 217.2,81.9 220.2,81.6 223.2,81.3 226.3,81.1 229.3,80.8 232.3,80.6 235.3,80.3 238.4,80.1 241.4,79.9 244.4,79.7 247.4,79.5 250.4,79.4 253.5,79.2 256.5,79.0 259.5,78.9 262.5,78.7 265.6,78.6 268.6,78.5 271.6,78.4 274.6,78.2 277.6,78.1 280.7,78.0 283.7,77.9 286.7,77.9 289.7,77.8 292.8,77.7 295.8,77.6 298.8,77.5 301.8,77.5 304.8,77.4 307.9,77.3 310.9,77.3 313.9,77.2 316.9,77.2 320.0,77.1 323.0,77.1 326.0,77.0" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="90.3" y="41.0" text-anchor="start" font-size="12" font-weight="700" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x<tspan baseline-shift="sub" font-size="9">max</tspan> = 0,300</text><text x="208.1" y="101.0" text-anchor="middle" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x<tspan baseline-shift="sub" font-size="9">f</tspan> = 0,243</text></svg>
:::

Sur la figure, le palier est le x_f de l'étape 5 et la ligne pointillée haute est le x_max de l'étape 4 : τ_f est le rapport de ces deux hauteurs, ici 0,243 / 0,300.

::: piege
**Erreur : garder la racine la plus grande du second degré.** Prendre x_f = 0,824 mol conduit à n(alcool) = 0,30 − 0,824 = −0,52 mol, ce qui n'a aucun sens. L'erreur tente parce que les deux racines sont des solutions mathématiques de l'équation ; mais l'avancement doit rester compris entre 0 et x_max, et c'est le tableau qui fixe cet intervalle.
:::

::: methode Composition à l'équilibre et τ_f
1. Calculer Π à l'état initial et la comparer à K pour trouver le sens ; compter l'avancement x dans ce sens.
2. Écrire le tableau descriptif en fonction de x.
3. Écrire K = Π(x_f), développer, et mettre l'équation sous la forme a x_f² + b x_f + c = 0.
4. Garder la racine comprise entre 0 et x_max, avec x_max l'avancement du réactif limitant dans ce sens.
5. Calculer la composition, puis τ_f = x_f / x_max.

Cas limite : le calcul se lit aussi à l'envers. Si une courbe x(t) donne le palier x_f = 0,20 mol pour 0,50 mol de chaque réactif, K = Π(x_f) = 0,20² / 0,30² = 0,44.
:::

::: verifie À toi : un mélange du côté des produits
Un système contient 0,10 mol d'acide, 0,10 mol d'alcool, 0,30 mol d'ester et 0,30 mol d'eau, avec K = 4. Trouver le sens, puis la composition à l'équilibre.

---

Π = (0,30 × 0,30) / (0,10 × 0,10) = 9,0 est supérieure à K : c'est la réaction inverse (hydrolyse). Avec x dans ce sens : acide = alcool = 0,10 + x, ester = eau = 0,30 − x. K = ((0,30 − x)/(0,10 + x))² = 4 donne (0,30 − x)/(0,10 + x) = 2, la racine −2 étant impossible car les deux quantités sont positives. Donc 0,30 − x = 0,20 + 2x, soit x = 0,033 mol : acide = alcool = 0,133 mol, ester = eau = 0,267 mol, et Π = (0,267/0,133)² = 4,0.
:::

::: retenir
Composition à l'équilibre : sens par Π et K, tableau en x, K = Π(x_f) en équation du second degré, racine entre 0 et x_max, puis τ_f = x_f / x_max.
:::

> 🏆 Tu sais désormais prévoir : un nombre Π, une constante K, et la comparaison des deux disent quel sens est possible et où le système finira. Les chapitres suivants appliqueront cette comparaison aux réactions acide-base.
