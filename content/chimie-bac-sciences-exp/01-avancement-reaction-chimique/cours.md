# ⚗️ Avancement d'une réaction chimique — compter combien de fois la réaction a marché

> 💡 «Une réaction chimique se raconte avec un seul nombre : combien de fois elle a eu lieu.»

Une feuille verte jaunit en automne : sa chlorophylle se dégrade et démasque d'autres pigments. Est-ce une transformation chimique ou un simple changement d'aspect ? Peut-on chiffrer la quantité dégradée, et en combien de temps ? Huit notions te donnent les outils : le vocabulaire du système, l'écriture d'une équation redox, l'avancement, le tableau descriptif et le réactif limitant, la comparaison entre calcul et mesure, la rapidité d'une transformation, le temps de demi-réaction, et les méthodes qui permettent de suivre l'avancement. On suppose acquis les couples oxydant/réducteur, l'écriture d'une équation chimique et la relation n = C × V.

## 🧪 Système et transformation chimique : de quoi parle-t-on ?

Un clou de fer plongé dans de l'eau salée se couvre de rouille en quelques jours ; un glaçon posé à côté fond en quelques minutes. Les deux « changent », mais un seul donne naissance à quelque chose de nouveau.
Comment trancher, et que faut-il délimiter avant de pouvoir en parler ?

::: definition
**Système chimique** — Portion de l'Univers qu'on décide d'étudier, séparée du reste par des frontières réelles (la paroi d'un bécher) ou imaginaires. Tout ce qui est en dehors forme le **milieu extérieur**, aussi appelé environnement. Les **constituants** du système sont les entités chimiques (molécules, ions, atomes) qu'on cite pour décrire son contenu.
:::

::: definition
**Transformation chimique** — Évolution d'un système où les quantités de matière de certains constituants changent et où de nouvelles entités apparaissent. On la modélise par une **réaction chimique**, que l'on symbolise par une équation : la transformation est ce qu'on observe, la réaction est le modèle qu'on écrit.
:::

::: exemple Classer quatre évolutions
Système : un bécher et son contenu. On se demande, à chaque fois, si de nouvelles entités apparaissent.

1. Un glaçon fond : l'entité H₂O reste la même, seule sa phase change. C'est un changement d'état, donc physique.
2. Une tige de fer se dilate à la chaleur : aucune entité nouvelle n'apparaît, seule la taille change. Physique.
3. Un clou rouille : le fer et le dioxygène disparaissent, un oxyde de fer apparaît. Des entités nouvelles : chimique.
4. Des ions Pb²⁺ rencontrent des ions I⁻ : un solide jaune apparaît. Chimique, modélisée par Pb²⁺ + 2 I⁻ → PbI₂(s).

:::

::: piege
**Erreur : appeler « chimique » tout phénomène qui change d'aspect.** L'eau qui se solidifie change d'aspect, de volume et de température, et pourtant c'est toujours de l'eau : le critère est l'apparition d'entités nouvelles, pas l'aspect. De même, une fusion ne se modélise pas par une réaction chimique : l'équation d'une réaction décrit une transformation chimique, pas un changement d'état.
:::

::: verifie À toi : classer deux évolutions
On étire un ressort en acier ; on laisse un morceau de zinc dans de l'acide chlorhydrique, et des bulles de dihydrogène se dégagent. Laquelle est une transformation chimique, et pourquoi ?

---

Le zinc dans l'acide : le zinc disparaît, des ions Zn²⁺ et du dihydrogène apparaissent, donc de nouvelles entités se forment. L'étirement du ressort ne crée aucune entité nouvelle : c'est un changement de forme, donc physique.
:::

::: retenir
Une transformation est chimique quand de nouvelles entités apparaissent ; on la modélise par une réaction, écrite sous forme d'équation.
:::

## 🔋 Écrire l'équation d'une réaction d'oxydoréduction

Une solution d'ions Fe²⁺ est à peine verdâtre ; on y verse du permanganate, violet, et la couleur disparaît au début. On connaît les deux couples en jeu, MnO₄⁻/Mn²⁺ et Fe³⁺/Fe²⁺, en milieu acide.
Comment obtenir l'équation de la réaction, avec les bons coefficients, à partir des deux couples ?

::: exemple Une équation redox en cinq gestes
Couples : MnO₄⁻/Mn²⁺ et Fe³⁺/Fe²⁺, milieu acide.

1. L'oxydant d'un couple réagit avec le réducteur de l'autre : MnO₄⁻ (oxydant, il capte des électrons) avec Fe²⁺ (réducteur, il en cède).
2. Demi-équation de l'oxydant : on équilibre O avec H₂O, H avec H₃O⁺, puis la charge avec e⁻. Cela donne MnO₄⁻ + 8 H₃O⁺ + 5 e⁻ ⇄ Mn²⁺ + 12 H₂O (charge : −1 + 8 − 5 = +2 des deux côtés).
3. Demi-équation du réducteur : Fe²⁺ ⇄ Fe³⁺ + e⁻.
4. Les électrons captés doivent égaler les électrons cédés : on multiplie la seconde demi-équation par 5.
5. On additionne : les électrons s'éliminent. MnO₄⁻ + 5 Fe²⁺ + 8 H₃O⁺ → Mn²⁺ + 5 Fe³⁺ + 12 H₂O. Contrôle des charges : −1 + 10 + 8 = +17 à gauche, 2 + 15 = +17 à droite.

:::

::: piege
**Erreur : écrire un seul de chaque et laisser les charges déséquilibrées.** L'écriture MnO₄⁻ + Fe²⁺ + 8 H₃O⁺ → Mn²⁺ + Fe³⁺ + 12 H₂O tente parce qu'elle « semble » équilibrée en atomes, mais ses charges valent +9 à gauche et +5 à droite. Il faut multiplier par 5 la demi-équation du fer pour que les 5 électrons captés par MnO₄⁻ soient tous cédés.
:::

::: methode
**De deux couples à une équation.** (1) Oxydant du premier couple, réducteur du second. (2) Une demi-équation par couple : O avec H₂O, H avec H₃O⁺, charge avec e⁻. (3) Multiplier chaque demi-équation pour égaliser les électrons. (4) Additionner et vérifier la conservation des atomes et des charges.
Les ions H₃O⁺ interviennent comme un réactif : sans milieu acide, cette réaction n'a pas lieu.
:::

::: verifie À toi : un oxydant à six électrons
La demi-équation de l'oxydant du couple Cr₂O₇²⁻/Cr³⁺ est Cr₂O₇²⁻ + 14 H₃O⁺ + 6 e⁻ ⇄ 2 Cr³⁺ + 21 H₂O. Écrire l'équation avec le réducteur du couple I₂/I⁻.

---

La demi-équation du réducteur est 2 I⁻ ⇄ I₂ + 2 e⁻. L'oxydant capte 6 e⁻ alors que cette demi-équation en cède 2 : on la multiplie par 3 pour égaliser. On additionne : Cr₂O₇²⁻ + 6 I⁻ + 14 H₃O⁺ → 2 Cr³⁺ + 3 I₂ + 21 H₂O. Charges : −2 − 6 + 14 = +6 à gauche, +6 à droite.
:::

::: retenir
Une équation redox s'écrit à partir de deux demi-équations dont on égalise les électrons avant de les additionner.
:::

## 🔢 L'avancement x : un seul nombre pour toute la réaction

Dans de l'acide, un morceau de zinc dégage des bulles de dihydrogène : à chaque « tour » de la réaction, un Zn disparaît, deux H₃O⁺ disparaissent, un H₂ apparaît. Chaque constituant varie de sa propre quantité.
Comment résumer l'état de la transformation par un seul nombre qui vaut pour tous les constituants à la fois ?

::: definition
**Avancement x** — Nombre de fois, exprimé en mol, que la réaction a eu lieu depuis l'état initial. Pour a A + b B → c C + d D, quand l'avancement vaut x, a·x mol de A et b·x mol de B ont disparu, c·x mol de C et d·x mol de D sont apparues.
Si la transformation se fait à volume V constant dans une seule phase, l'**avancement volumique** est y = x / V, en mol·L⁻¹.
:::

Pour Zn + 2 H₃O⁺ → Zn²⁺ + H₂ + 2 H₂O, voici ce que fait un avancement x = 0,010 mol à chaque constituant.

| constituant | coefficient | variation pour x = 0,010 mol |
| ----------- | ----------- | ---------------------------- |
| Zn          | 1 (réactif) | −0,010 mol                   |
| H₃O⁺        | 2 (réactif) | −0,020 mol                   |
| Zn²⁺        | 1 (produit) | +0,010 mol                   |
| H₂          | 1 (produit) | +0,010 mol                   |

Dans le tableau, le coefficient de chaque ligne est celui de l'équation : x est le même pour tous, les variations ne diffèrent que par ce coefficient.

::: exemple Du dihydrogène recueilli à l'avancement
Équation : Zn + 2 H₃O⁺ → Zn²⁺ + H₂ + 2 H₂O. À une date t, 0,020 mol de H₂ se sont dégagées.

1. H₂ apparaît avec le coefficient 1 : x = n(H₂) / 1 = 0,020 mol (pour un produit, x = n formée / coefficient).
2. H₃O⁺ disparaît avec le coefficient 2 : n(H₃O⁺) disparue = 2 × x = 0,040 mol (pour un réactif, disparue = coefficient × x).
3. Zn²⁺ apparaît avec le coefficient 1 : n(Zn²⁺) = 0,020 mol.
4. Ici le système compte trois phases (zinc solide, solution, gaz) : on n'y définit pas d'avancement volumique. Pour une réaction en une seule phase à volume constant, par exemple S₂O₈²⁻ + 2 I⁻ → 2 SO₄²⁻ + I₂ dans 0,50 L, x = 0,020 mol donne y = x / V = 0,040 mol·L⁻¹.

:::

::: piege
**Erreur : prendre la quantité d'un constituant pour l'avancement.** « 0,040 mol de H₃O⁺ ont disparu, donc x = 0,040 mol » tente parce qu'on a la valeur sous la main. Mais x caractérise la réaction entière, pas un constituant : il faut diviser par le coefficient 2, d'où x = 0,040 / 2 = 0,020 mol.
:::

::: propriete
**Relation entre x et les quantités.** x = (n_i(A) − n(A)) / a = (n_i(B) − n(B)) / b = n(C) / c = n(D) / d. La quantité disparue ou apparue, divisée par le coefficient, donne le même x pour tous les constituants.
Cas limite : un coefficient égal à 1 (Zn, Zn²⁺, H₂ ci-dessus) donne x égal à la quantité apparue ou disparue, ce qui ne doit pas faire oublier la division quand le coefficient vaut 2 ou plus.
:::

::: verifie À toi : de la quantité formée à l'avancement
Équation : S₂O₈²⁻ + 2 I⁻ → 2 SO₄²⁻ + I₂. À une date t, 6,0×10⁻⁴ mol de SO₄²⁻ se sont formées. Calculer x et la quantité de I⁻ disparue.

---

SO₄²⁻ est un produit de coefficient 2 : x = 6,0×10⁻⁴ / 2 = 3,0×10⁻⁴ mol. I⁻ est un réactif de coefficient 2 : n(I⁻) disparue = 2 × x = 6,0×10⁻⁴ mol.
:::

::: retenir
L'avancement x est le nombre de fois que la réaction a eu lieu ; il vaut la quantité disparue ou apparue d'un constituant divisée par son coefficient.
:::

## 📊 Tableau descriptif, avancement maximal et réactif limitant

On verse 50,0 mL de nitrate de plomb à 0,10 mol·L⁻¹ sur 50,0 mL d'iodure de potassium à 0,15 mol·L⁻¹ : un précipité jaune se forme jusqu'à ce qu'il manque un ion. Les ions Pb²⁺ sont les moins nombreux au départ.
Lequel manquera pourtant le premier, et quelle quantité de précipité obtient-on au plus ?

::: definition
**Avancement maximal x_max** — Valeur de x calculée en supposant la réaction poussée jusqu'à l'épuisement d'un réactif. Ce réactif est le **réactif limitant** : celui dont la quantité tombe à zéro en premier.
Le **tableau descriptif** suit les quantités de matière des constituants à l'état initial, en cours de transformation (avancement x) et à l'état final.
:::

Voici le tableau descriptif de Pb²⁺ + 2 I⁻ → PbI₂(s), quantités en mol ; le solvant n'y figure pas.

| état     | avancement | Pb²⁺             | I⁻                 | PbI₂  |
| -------- | ---------- | ---------------- | ------------------ | ----- |
| initial  | 0          | 5,0×10⁻³         | 7,5×10⁻³           | 0     |
| en cours | x          | 5,0×10⁻³ − x     | 7,5×10⁻³ − 2x      | x     |
| final    | x_max      | 5,0×10⁻³ − x_max | 7,5×10⁻³ − 2 x_max | x_max |

Chaque ligne du tableau applique la relation de la notion précédente : pour I⁻, le coefficient 2 donne 7,5×10⁻³ − 2x.

::: exemple Qui s'épuise le premier ?

1. Quantités initiales : n_i(Pb²⁺) = 0,10 × 50,0×10⁻³ = 5,0×10⁻³ mol ; n_i(I⁻) = 0,15 × 50,0×10⁻³ = 7,5×10⁻³ mol (n = C × V, volume en litres).
2. Aucune quantité ne peut devenir négative : 5,0×10⁻³ − x ≥ 0 donne x ≤ 5,0×10⁻³ mol ; 7,5×10⁻³ − 2x ≥ 0 donne x ≤ 3,75×10⁻³ mol.
3. x ne peut dépasser la plus petite des deux bornes : x_max = 3,75×10⁻³ mol. C'est I⁻ qui s'épuise : I⁻ est le réactif limitant.
4. Composition finale (réaction totale) : n(Pb²⁺) = 5,0×10⁻³ − 3,75×10⁻³ = 1,25×10⁻³ mol ; n(I⁻) = 0 ; n(PbI₂) = 3,75×10⁻³ mol.

:::

::: piege
**Erreur : désigner comme limitant le réactif dont la quantité initiale est la plus petite.** Ici Pb²⁺ (5,0×10⁻³ mol) est moins abondant que I⁻ (7,5×10⁻³ mol), et pourtant il en reste à la fin. La comparaison juste se fait entre n_i / coefficient : 5,0×10⁻³ / 1 contre 7,5×10⁻³ / 2 = 3,75×10⁻³, plus petit.
:::

::: methode
**Trouver x_max.** (1) Calculer chaque n_i par n = C × V. (2) Pour chaque réactif, résoudre n_i − coefficient × x ≥ 0, soit x ≤ n_i / coefficient. (3) x_max est la plus petite de ces bornes ; le réactif correspondant est limitant. (4) Reporter x_max dans la ligne finale.
Cas limite : si deux réactifs donnent la même borne, ils s'épuisent ensemble (proportions stœchiométriques). Le solvant (l'eau) et un réactif en très large excès, comme H₃O⁺ d'une solution fortement acide, ne sont pas suivis : leur colonne porte un tiret, ou on les omet.
:::

::: verifie À toi : un permanganate et un oxalate
Équation : 2 MnO₄⁻ + 5 H₂C₂O₄ + 6 H₃O⁺ → 2 Mn²⁺ + 10 CO₂ + 14 H₂O, avec H₃O⁺ en large excès. On mélange 20,0 mL de MnO₄⁻ à 0,010 mol·L⁻¹ et 30,0 mL de H₂C₂O₄ à 0,020 mol·L⁻¹. Calculer x_max et dire quel réactif est limitant.

---

n_i(MnO₄⁻) = 0,010 × 20,0×10⁻³ = 2,0×10⁻⁴ mol et n_i(H₂C₂O₄) = 0,020 × 30,0×10⁻³ = 6,0×10⁻⁴ mol. Bornes : 2,0×10⁻⁴ / 2 = 1,0×10⁻⁴ mol pour MnO₄⁻ et 6,0×10⁻⁴ / 5 = 1,2×10⁻⁴ mol pour H₂C₂O₄. Donc x_max = 1,0×10⁻⁴ mol et MnO₄⁻ est limitant.
:::

::: retenir
x_max est la plus petite des bornes n_i / coefficient ; le réactif qui la donne est le réactif limitant.
:::

## ⚖️ Avancement final : le calcul contre la mesure

Dans un mélange, la composition finit par ne plus bouger, mais les deux réactifs sont toujours là. Le calcul de x_max disait pourtant qu'ils pouvaient disparaître.
Comment comparer ce que le calcul prévoit et ce que la mesure donne ?

::: definition
**Avancement final x_f** — Valeur de x à l'état final, déduite de la composition mesurée. Elle est toujours inférieure ou égale à x_max, qui est une valeur calculée.
Une réaction est **totale** si x_f = x_max (un réactif limitant disparaît), et **limitée** si x_f < x_max : aucun réactif ne disparaît entièrement.
:::

::: figure Le plateau mesuré x_f reste sous la valeur calculée x_max : la réaction est limitée (valeurs d'illustration)
<svg viewBox="0 0 340 240"><title>Courbe x en fonction de t : le plateau x_f reste sous la valeur calculée x_max</title><line x1="52" y1="200" x2="52" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="97" y1="200" x2="97" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="142" y1="200" x2="142" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="187" y1="200" x2="187" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="232" y1="200" x2="232" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="277" y1="200" x2="277" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="322" y1="200" x2="322" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="200" x2="322" y2="200" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="170.3" x2="322" y2="170.3" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="140.7" x2="322" y2="140.7" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="111" x2="322" y2="111" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="81.3" x2="322" y2="81.3" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="51.7" x2="322" y2="51.7" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="22" x2="322" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="200" x2="332" y2="200" stroke="#0f172a" stroke-width="1.6"/><line x1="52" y1="200" x2="52" y2="12" stroke="#0f172a" stroke-width="1.6"/><polygon points="332,200 324,196 324,204" fill="#0f172a"/><polygon points="52,10 48,18 56,18" fill="#0f172a"/><line x1="52" y1="200" x2="52" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="52" y="216" text-anchor="middle" font-size="11" fill="#0f172a">0</text><line x1="97" y1="200" x2="97" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="97" y="216" text-anchor="middle" font-size="11" fill="#0f172a">10</text><line x1="142" y1="200" x2="142" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="142" y="216" text-anchor="middle" font-size="11" fill="#0f172a">20</text><line x1="187" y1="200" x2="187" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="187" y="216" text-anchor="middle" font-size="11" fill="#0f172a">30</text><line x1="232" y1="200" x2="232" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="232" y="216" text-anchor="middle" font-size="11" fill="#0f172a">40</text><line x1="277" y1="200" x2="277" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="277" y="216" text-anchor="middle" font-size="11" fill="#0f172a">50</text><line x1="322" y1="200" x2="322" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="322" y="216" text-anchor="middle" font-size="11" fill="#0f172a">60</text><line x1="48" y1="200" x2="52" y2="200" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="204" text-anchor="end" font-size="11" fill="#0f172a">0</text><line x1="48" y1="170.3" x2="52" y2="170.3" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="174.3" text-anchor="end" font-size="11" fill="#0f172a">2</text><line x1="48" y1="140.7" x2="52" y2="140.7" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="144.7" text-anchor="end" font-size="11" fill="#0f172a">4</text><line x1="48" y1="111" x2="52" y2="111" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="115" text-anchor="end" font-size="11" fill="#0f172a">6</text><line x1="48" y1="81.3" x2="52" y2="81.3" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="85.3" text-anchor="end" font-size="11" fill="#0f172a">8</text><line x1="48" y1="51.7" x2="52" y2="51.7" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="55.7" text-anchor="end" font-size="11" fill="#0f172a">10</text><line x1="48" y1="22" x2="52" y2="22" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="26" text-anchor="end" font-size="11" fill="#0f172a">12</text><text x="326" y="232" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a">t (min)</text><text x="58" y="12" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a">x (10⁻² mol)</text><line x1="52" y1="51.7" x2="322" y2="51.7" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><line x1="52" y1="100.6" x2="322" y2="100.6" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><polyline points="52,200 54.2,195.9 56.5,192.1 58.8,188.3 61,184.7 63.2,181.3 65.5,178 67.8,174.9 70,171.8 72.2,168.9 74.5,166.1 76.8,163.5 79,160.9 81.2,158.4 83.5,156.1 85.8,153.8 88,151.6 90.2,149.6 92.5,147.6 94.8,145.6 97,143.8 99.2,142 101.5,140.4 103.8,138.7 106,137.2 108.2,135.7 110.5,134.3 112.8,132.9 115,131.6 117.2,130.3 119.5,129.1 121.8,127.9 124,126.8 126.2,125.7 128.5,124.7 130.8,123.7 133,122.8 135.2,121.9 137.5,121 139.8,120.2 142,119.4 144.2,118.6 146.5,117.9 148.8,117.2 151,116.5 153.2,115.9 155.5,115.2 157.8,114.6 160,114.1 162.2,113.5 164.5,113 166.8,112.5 169,112 171.2,111.5 173.5,111.1 175.8,110.7 178,110.3 180.2,109.9 182.5,109.5 184.8,109.1 187,108.8 189.2,108.4 191.5,108.1 193.8,107.8 196,107.5 198.2,107.2 200.5,107 202.8,106.7 205,106.5 207.2,106.2 209.5,106 211.8,105.8 214,105.6 216.2,105.4 218.5,105.2 220.8,105 223,104.8 225.2,104.6 227.5,104.5 229.8,104.3 232,104.2 234.2,104 236.5,103.9 238.8,103.7 241,103.6 243.2,103.5 245.5,103.4 247.8,103.3 250,103.2 252.2,103.1 254.5,103 256.8,102.9 259,102.8 261.2,102.7 263.5,102.6 265.8,102.5 268,102.4 270.2,102.4 272.5,102.3 274.8,102.2 277,102.2 279.2,102.1 281.5,102 283.8,102 286,101.9 288.2,101.9 290.5,101.8 292.8,101.8 295,101.7 297.2,101.7 299.5,101.6 301.8,101.6 304,101.6 306.2,101.5 308.5,101.5 310.8,101.4 313,101.4 315.2,101.4 317.5,101.3 319.8,101.3 322,101.3" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><text x="317.5" y="51.7" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x_max</text><text x="317.5" y="100.6" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x_f</text></svg>
:::

Sur la figure, la droite pointillée haute est x_max, calculé ; le plateau de la courbe est x_f, mesuré.

::: exemple Un mélange équimolaire qui ne s'épuise pas
Équation : A + B → C + D. On mélange 0,10 mol de A et 0,10 mol de B. À l'état final, la mesure donne n(C) = 0,067 mol.

1. Calcul : 0,10 / 1 pour A comme pour B, donc x_max = 0,10 mol.
2. Mesure : C apparaît avec le coefficient 1, donc x_f = 0,067 mol.
3. Composition finale : n(A) = 0,10 − 0,067 = 0,033 mol, non nul ; il en reste autant de B.
4. Comparaison : x_f = 0,067 mol est inférieur à x_max = 0,10 mol, donc la réaction est limitée.

:::

::: piege
**Erreur : croire qu'une transformation qui s'arrête a épuisé un réactif.** Cela tente parce que, dans les calculs du tableau, on s'arrête toujours à un réactif nul. Or x_max est une borne calculée, pas ce qui se passe en vrai : si x_f < x_max, la transformation s'arrête sans que rien ne manque.
:::

::: propriete
**Totale ou limitée.** On compare x_f, déduit de la mesure, à x_max, déduit du calcul. Totale : x_f = x_max, un réactif limitant a une quantité finale nulle. Limitée : x_f < x_max, aucun réactif n'est nul à la fin.
Cas limite : « pratiquement totale » désigne x_f égal à x_max à la précision de la mesure.
:::

::: verifie À toi : totale ou limitée ?
Équation : E + F → G + H. On mélange 0,040 mol de E et 0,040 mol de F ; à l'état final, il reste 0,010 mol de E. Calculer x_max et x_f, puis conclure.

---

Calcul : 0,040 / 1 pour chacun, donc x_max = 0,040 mol. Mesure : E a disparu de 0,040 − 0,010 = 0,030 mol, donc x_f = 0,030 / 1 = 0,030 mol. Comme x_f < x_max, la réaction est limitée : il reste du réactif.
:::

::: retenir
x_f vient de la mesure, x_max du calcul : si x_f < x_max, la réaction est limitée et aucun réactif ne s'épuise.
:::

## ⏱️ Transformations rapides et lentes, cinétique chimique

On verse de la soude sur de l'acide additionné d'un indicateur : il vire à l'instant. On plonge du zinc dans l'acide : des bulles de dihydrogène se forment pendant plusieurs minutes.
Qu'est-ce qui distingue ces deux transformations, et comment suivre l'une et pas l'autre ?

::: definition
**Transformation rapide ou lente** — Une transformation est **rapide** si la durée entre l'état initial et l'état final est inférieure à la persistance rétinienne (environ le dixième de seconde) ou au temps de réponse des appareils courants. Elle est **lente** si elle dure assez pour être suivie avec les sens ou avec les techniques de mesure habituelles.
La **cinétique chimique** est l'étude de l'évolution des systèmes chimiques au cours du temps.
:::

::: exemple Classer quatre transformations

1. H₃O⁺ + OH⁻ → 2 H₂O avec un indicateur : le virage est immédiat, donc rapide.
2. Pb²⁺ + 2 I⁻ → PbI₂(s) : le solide jaune apparaît dès le contact des solutions, donc rapide.
3. Zn + 2 H₃O⁺ → Zn²⁺ + H₂ + 2 H₂O : le dégagement de H₂ progresse sur plusieurs minutes, donc lente ; on la suit en recueillant le gaz.
4. S₂O₈²⁻ + 2 I⁻ → 2 SO₄²⁻ + I₂ : la solution jaunit puis brunit sur de longues minutes, donc lente ; on la suit à la couleur du diiode.

:::

::: piege
**Erreur : confondre « lente » et « limitée ».** Une transformation lente peut très bien aller jusqu'au bout, comme le zinc dans l'acide tant qu'il reste du zinc. La rapidité répond à « en combien de temps ? », le caractère total ou limité à « jusqu'où ? » : ce sont deux questions séparées.
:::

::: verifie À toi : rapide ou lente ?
Une solution violette de permanganate acidifiée se décolore en 4 minutes lorsqu'on y ajoute de l'acide oxalique. Cette transformation est-elle rapide ou lente, et comment la suivre ?

---

Quatre minutes dépassent largement la persistance rétinienne : la transformation est lente. On peut la suivre à l'œil, grâce à la couleur violette de MnO₄⁻ qui s'estompe, sans technique de mesure particulière.
:::

::: retenir
Une transformation est rapide si elle échappe à l'œil et aux appareils usuels, lente sinon ; la cinétique étudie son évolution dans le temps.
:::

## 🕰️ Le temps de demi-réaction t₁/₂

On suit une transformation pendant une demi-heure : l'avancement monte vite, puis ralentit jusqu'à se stabiliser.
Comment résumer la rapidité de cette montée par une durée facile à lire sur la courbe ?

::: definition
**Temps de demi-réaction t₁/₂** — Durée au bout de laquelle l'avancement atteint la moitié de sa valeur finale x_f.
:::

::: figure Pour lire t₁/₂ : on trace x_f/2, puis on descend verticalement sous la courbe (valeurs d'illustration)
<svg viewBox="0 0 340 240"><title>Courbe x en fonction de t, avec x_f, x_f/2 et le point de lecture de t demi-réaction</title><line x1="52" y1="200" x2="52" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="97" y1="200" x2="97" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="142" y1="200" x2="142" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="187" y1="200" x2="187" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="232" y1="200" x2="232" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="277" y1="200" x2="277" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="322" y1="200" x2="322" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="200" x2="322" y2="200" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="164.4" x2="322" y2="164.4" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="128.8" x2="322" y2="128.8" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="93.2" x2="322" y2="93.2" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="57.6" x2="322" y2="57.6" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="22" x2="322" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="200" x2="332" y2="200" stroke="#0f172a" stroke-width="1.6"/><line x1="52" y1="200" x2="52" y2="12" stroke="#0f172a" stroke-width="1.6"/><polygon points="332,200 324,196 324,204" fill="#0f172a"/><polygon points="52,10 48,18 56,18" fill="#0f172a"/><line x1="52" y1="200" x2="52" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="52" y="216" text-anchor="middle" font-size="11" fill="#0f172a">0</text><line x1="97" y1="200" x2="97" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="97" y="216" text-anchor="middle" font-size="11" fill="#0f172a">5</text><line x1="142" y1="200" x2="142" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="142" y="216" text-anchor="middle" font-size="11" fill="#0f172a">10</text><line x1="187" y1="200" x2="187" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="187" y="216" text-anchor="middle" font-size="11" fill="#0f172a">15</text><line x1="232" y1="200" x2="232" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="232" y="216" text-anchor="middle" font-size="11" fill="#0f172a">20</text><line x1="277" y1="200" x2="277" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="277" y="216" text-anchor="middle" font-size="11" fill="#0f172a">25</text><line x1="322" y1="200" x2="322" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="322" y="216" text-anchor="middle" font-size="11" fill="#0f172a">30</text><line x1="48" y1="200" x2="52" y2="200" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="204" text-anchor="end" font-size="11" fill="#0f172a">0</text><line x1="48" y1="164.4" x2="52" y2="164.4" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="168.4" text-anchor="end" font-size="11" fill="#0f172a">1</text><line x1="48" y1="128.8" x2="52" y2="128.8" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="132.8" text-anchor="end" font-size="11" fill="#0f172a">2</text><line x1="48" y1="93.2" x2="52" y2="93.2" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="97.2" text-anchor="end" font-size="11" fill="#0f172a">3</text><line x1="48" y1="57.6" x2="52" y2="57.6" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="61.6" text-anchor="end" font-size="11" fill="#0f172a">4</text><line x1="48" y1="22" x2="52" y2="22" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="26" text-anchor="end" font-size="11" fill="#0f172a">5</text><text x="326" y="232" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a">t (min)</text><text x="58" y="12" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a">x (10⁻³ mol)</text><line x1="52" y1="57.6" x2="322" y2="57.6" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><line x1="52" y1="128.8" x2="97" y2="128.8" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><line x1="97" y1="200" x2="97" y2="128.8" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><polyline points="52,200 54.2,195.1 56.5,190.5 58.8,185.9 61,181.6 63.2,177.3 65.5,173.3 67.8,169.3 70,165.5 72.2,161.8 74.5,158.3 76.8,154.9 79,151.5 81.2,148.3 83.5,145.3 85.8,142.3 88,139.4 90.2,136.6 92.5,133.9 94.8,131.3 97,128.8 99.2,126.4 101.5,124 103.8,121.8 106,119.6 108.2,117.5 110.5,115.4 112.8,113.5 115,111.6 117.2,109.7 119.5,107.9 121.8,106.2 124,104.6 126.2,103 128.5,101.4 130.8,99.9 133,98.5 135.2,97.1 137.5,95.8 139.8,94.5 142,93.2 144.2,92 146.5,90.8 148.8,89.7 151,88.6 153.2,87.5 155.5,86.5 157.8,85.5 160,84.6 162.2,83.7 164.5,82.8 166.8,81.9 169,81.1 171.2,80.3 173.5,79.5 175.8,78.8 178,78 180.2,77.4 182.5,76.7 184.8,76 187,75.4 189.2,74.8 191.5,74.2 193.8,73.6 196,73.1 198.2,72.6 200.5,72.1 202.8,71.6 205,71.1 207.2,70.6 209.5,70.2 211.8,69.8 214,69.3 216.2,68.9 218.5,68.6 220.8,68.2 223,67.8 225.2,67.5 227.5,67.1 229.8,66.8 232,66.5 234.2,66.2 236.5,65.9 238.8,65.6 241,65.3 243.2,65.1 245.5,64.8 247.8,64.6 250,64.3 252.2,64.1 254.5,63.9 256.8,63.7 259,63.5 261.2,63.3 263.5,63.1 265.8,62.9 268,62.7 270.2,62.5 272.5,62.4 274.8,62.2 277,62.1 279.2,61.9 281.5,61.8 283.8,61.6 286,61.5 288.2,61.3 290.5,61.2 292.8,61.1 295,61 297.2,60.9 299.5,60.7 301.8,60.6 304,60.5 306.2,60.4 308.5,60.3 310.8,60.2 313,60.2 315.2,60.1 317.5,60 319.8,59.9 322,59.8" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="97" cy="128.8" r="3.6" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/><text x="317.5" y="57.6" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x_f</text><text x="55.6" y="128.8" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x_f/2</text></svg>
:::

Sur la figure, la droite pointillée haute est le plateau x_f ; l'horizontale basse est x_f/2, et le point marqué donne t₁/₂ en abscisse.

::: exemple Lire t₁/₂ sur une courbe

1. Le plateau de la courbe donne x_f = 4,0×10⁻³ mol (au-delà, x ne varie plus).
2. La moitié vaut x_f / 2 = 2,0×10⁻³ mol.
3. On trace l'horizontale à 2,0×10⁻³ mol jusqu'à la courbe, puis on lit l'abscisse du point : t₁/₂ = 5 min.
4. Contrôle : à t = 10 min, soit 2 t₁/₂, la courbe donne x = 3,0×10⁻³ mol, encore inférieur à x_f : à 2 t₁/₂ la transformation n'est pas terminée.

:::

::: piege
**Erreur : doubler t₁/₂ pour obtenir la durée de la transformation.** « t₁/₂ = 5 min, donc la fin est à 10 min » tente parce que « demi » appelle « deux fois ». Or la courbe ralentit en approchant de x_f : à 10 min il manque encore le quart de x_f. La moitié de la durée d'observation n'est pas non plus t₁/₂ : ce qui compte est la moitié de x_f, pas celle du temps.
:::

::: propriete
**Lire et utiliser t₁/₂.** Sur une courbe x = f(t), on lit l'abscisse du point d'ordonnée x_f/2. Sur la courbe de la concentration d'un produit, proportionnelle à x pour un volume constant, on cherche la moitié de la valeur finale de cette concentration. Le temps de fin t_f est en général différent de 2 t₁/₂.
Usage : un t₁/₂ très court impose une méthode de suivi physique ; un t₁/₂ de plusieurs minutes laisse le choix entre une méthode chimique et une méthode physique.
:::

::: verifie À toi : lire un t₁/₂
Une courbe montre x = 1,2×10⁻² mol de plateau, atteint vers 45 min ; on y lit x = 6,0×10⁻³ mol à 8 min. Donner t₁/₂ et dire si la réaction est terminée à 16 min.

---

x_f / 2 = 6,0×10⁻³ mol correspond à t = 8 min, donc t₁/₂ = 8 min. À 16 min = 2 t₁/₂, le plateau n'est atteint que vers 45 min : la réaction n'est pas terminée, car t_f est en général différent de 2 t₁/₂.
:::

::: retenir
t₁/₂ est la durée pour atteindre x_f / 2 ; il situe la rapidité de la montée mais ne donne pas la date de fin.
:::

## 🔬 Suivre l'avancement : méthodes chimiques et physiques

Dans un bécher, la réaction S₂O₈²⁻ + 2 I⁻ → 2 SO₄²⁻ + I₂ forme du diiode lentement. Pour tracer x en fonction de t, il faut connaître la quantité formée à chaque date.
Comment la mesurer sans arrêter la transformation : en détruisant un peu de matière, ou en mesurant une grandeur reliée aux concentrations ?

::: definition
**Titrer (ou doser)** — Déterminer la concentration d'une entité en solution grâce à une réaction de dosage, qui doit être totale, rapide et spécifique de l'entité à doser. À l'équivalence, les réactifs ont été introduits en proportions stœchiométriques ; un indicateur coloré signale ce moment.
Les méthodes **physiques** mesurent une grandeur liée aux concentrations : conductance G (ions), pH (H₃O⁺), absorbance (espèce colorée), volume ou masse (gaz dégagé, précipité).
:::

::: figure Droite d'étalonnage G = f(C) : la droite passe par l'origine, et G = 4,90 mS donne C = 0,35 mol·L⁻¹ (valeurs d'illustration)
<svg viewBox="0 0 340 240"><title>Droite d'étalonnage G en fonction de C passant par l'origine, avec la lecture de C pour G = 4,90 mS</title><line x1="52" y1="200" x2="52" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="97" y1="200" x2="97" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="142" y1="200" x2="142" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="187" y1="200" x2="187" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="232" y1="200" x2="232" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="277" y1="200" x2="277" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="322" y1="200" x2="322" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="200" x2="322" y2="200" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="155.5" x2="322" y2="155.5" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="111" x2="322" y2="111" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="66.5" x2="322" y2="66.5" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="22" x2="322" y2="22" stroke="#cbd5e1" stroke-width="0.8"/><line x1="52" y1="200" x2="332" y2="200" stroke="#0f172a" stroke-width="1.6"/><line x1="52" y1="200" x2="52" y2="12" stroke="#0f172a" stroke-width="1.6"/><polygon points="332,200 324,196 324,204" fill="#0f172a"/><polygon points="52,10 48,18 56,18" fill="#0f172a"/><line x1="52" y1="200" x2="52" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="52" y="216" text-anchor="middle" font-size="11" fill="#0f172a">0,0</text><line x1="97" y1="200" x2="97" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="97" y="216" text-anchor="middle" font-size="11" fill="#0f172a">0,1</text><line x1="142" y1="200" x2="142" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="142" y="216" text-anchor="middle" font-size="11" fill="#0f172a">0,2</text><line x1="187" y1="200" x2="187" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="187" y="216" text-anchor="middle" font-size="11" fill="#0f172a">0,3</text><line x1="232" y1="200" x2="232" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="232" y="216" text-anchor="middle" font-size="11" fill="#0f172a">0,4</text><line x1="277" y1="200" x2="277" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="277" y="216" text-anchor="middle" font-size="11" fill="#0f172a">0,5</text><line x1="322" y1="200" x2="322" y2="204" stroke="#0f172a" stroke-width="1.2"/><text x="322" y="216" text-anchor="middle" font-size="11" fill="#0f172a">0,6</text><line x1="48" y1="200" x2="52" y2="200" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="204" text-anchor="end" font-size="11" fill="#0f172a">0</text><line x1="48" y1="155.5" x2="52" y2="155.5" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="159.5" text-anchor="end" font-size="11" fill="#0f172a">2</text><line x1="48" y1="111" x2="52" y2="111" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="115" text-anchor="end" font-size="11" fill="#0f172a">4</text><line x1="48" y1="66.5" x2="52" y2="66.5" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="70.5" text-anchor="end" font-size="11" fill="#0f172a">6</text><line x1="48" y1="22" x2="52" y2="22" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="26" text-anchor="end" font-size="11" fill="#0f172a">8</text><text x="326" y="232" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a">C (mol·L⁻¹)</text><text x="58" y="12" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a">G (mS)</text><line x1="52" y1="91" x2="209.5" y2="91" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><line x1="209.5" y1="200" x2="209.5" y2="91" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/><polyline points="52,200 322,13.1" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="97" cy="168.8" r="3.6" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/><circle cx="142" cy="137.7" r="3.6" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/><circle cx="187" cy="106.5" r="3.6" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/><circle cx="232" cy="75.4" r="3.6" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/><circle cx="277" cy="44.2" r="3.6" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/></svg>
:::

Sur la figure, la proportionnalité entre G et C (droite par l'origine) permet de lire C pour une conductance mesurée ; la valeur de pH se convertit par [H₃O⁺] = 10⁻ᵖᴴ, et l'absorbance, sans unité, est proportionnelle à l'épaisseur traversée et à la concentration.

::: exemple Deux façons de trouver x
**Par le pH.** Zn + 2 H₃O⁺ → Zn²⁺ + H₂ + 2 H₂O, dans 100 mL à volume constant. Le pH passe de 1,00 à 2,00.

1. [H₃O⁺]₀ = 10⁻¹ = 0,10 mol·L⁻¹, donc n₀ = 0,10 × 0,100 = 1,0×10⁻² mol.
2. À t, [H₃O⁺] = 10⁻² = 1,0×10⁻² mol·L⁻¹, donc n = 1,0×10⁻³ mol.
3. Il a disparu 1,0×10⁻² − 1,0×10⁻³ = 9,0×10⁻³ mol de H₃O⁺, de coefficient 2 : x = 4,5×10⁻³ mol.

**Par un titrage.** Dans la réaction S₂O₈²⁻ + 2 I⁻ → 2 SO₄²⁻ + I₂, on dose aussitôt une prise de 10,0 mL d'un mélange de 100,0 mL par du thiosulfate à 0,020 mol·L⁻¹ ; l'équivalence est à 12,0 mL.

1. Réaction de dosage : I₂ + 2 S₂O₃²⁻ → S₄O₆²⁻ + 2 I⁻ ; n(S₂O₃²⁻) versée = 0,020 × 12,0×10⁻³ = 2,4×10⁻⁴ mol.
2. À l'équivalence, le coefficient 2 du thiosulfate donne n(I₂) = 2,4×10⁻⁴ / 2 = 1,2×10⁻⁴ mol dans la prise.
3. Le mélange est dix fois plus grand que la prise : n(I₂) = 1,2×10⁻³ mol, et comme le coefficient de I₂ vaut 1, x = 1,2×10⁻³ mol.

:::

::: piege
**Erreur : prendre n(I₂) égal à la quantité de thiosulfate versée.** « 2,4×10⁻⁴ mol de thiosulfate, donc 2,4×10⁻⁴ mol de diiode » tente parce que les deux sont dosés « mole pour mole ». Mais l'équation I₂ + 2 S₂O₃²⁻ consomme deux thiosulfate par diiode : il faut diviser par 2.
:::

::: methode
**Déduire x d'une mesure.** (1) Relier la grandeur mesurée à la quantité n d'un constituant. (2) Calculer la quantité disparue ou apparue entre l'état initial et la date t. (3) La diviser par le coefficient. (4) Tenir compte du volume réel : prise d'essai ou mélange entier.
Variante, le titrage au fil de l'eau : on ajoute le thiosulfate dans le mélange même, avec de l'empois d'amidon ; après p ajouts de volume V₀ et de concentration C₀, x = p × C₀ × V₀ / 2. Exemple : p = 6, C₀ = 0,20 mol·L⁻¹, V₀ = 0,50 mL donnent x = 6 × 0,20 × 0,50×10⁻³ / 2 = 3,0×10⁻⁴ mol. L'ajout modifie le volume : il doit rester petit devant le volume du mélange.
:::

::: verifie À toi : un titrage sur une prise
Dans une prise de 20,0 mL d'un mélange de 200 mL, on dose le diiode formé par du thiosulfate à 0,010 mol·L⁻¹ ; l'équivalence est à 9,0 mL. Calculer l'avancement dans le mélange entier (le coefficient de I₂ dans l'équation est 1).

---

n(S₂O₃²⁻) = 0,010 × 9,0×10⁻³ = 9,0×10⁻⁵ mol ; le coefficient 2 donne n(I₂) = 4,5×10⁻⁵ mol dans la prise. Le mélange est dix fois plus grand : n(I₂) = 4,5×10⁻⁴ mol, donc x = 4,5×10⁻⁴ mol.
:::

::: retenir
On suit x en titrant un constituant (réaction de dosage) ou en mesurant une grandeur physique liée aux concentrations ; il faut toujours remonter à n puis à x par le coefficient.
:::

> 🏆 Premier chapitre franchi, héros : tu sais délimiter un système, écrire une équation redox, compter l'avancement par le coefficient, trouver x_max et le réactif limitant, opposer calcul et mesure, lire un t₁/₂ et choisir comment suivre une transformation. Les chapitres suivants mettront ces temps en nombres : la vitesse, l'équilibre.
