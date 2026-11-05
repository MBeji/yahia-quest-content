# ⚔️ Continuité — franchir le pont de Bolzano

> 💡 «Une courbe continue ne saute aucune hauteur : pour passer de bas en haut, elle doit croiser toutes les valeurs intermédiaires.»

Bienvenue, héros de la section Sciences de l'informatique. Ce que le dessin laisse deviner, Bolzano l'a démontré : une courbe tracée d'un seul trait qui passe sous l'axe des abscisses, puis au-dessus, le coupe forcément. Ce théorème est le sommet du chapitre, et il fournit un outil que tu programmeras : la dichotomie. Huit étapes t'y conduisent : continuité en un point, sur un intervalle, prolongement, composée, valeurs intermédiaires, bijection, fonction réciproque et racine nᵉ. On suppose acquis le calcul des limites (chapitre 2).

## 🧵 Continuité en un point : sans lever le crayon

Un parking facture c(t) = 2t dinars pour t ≤ 3 heures, puis la formule change : c(t) = t + 3 pour t > 3.
Le prix saute-t-il d'un coup à l'instant t = 3 ? « Sans lever le crayon » ne permet pas de calculer : il faut le dire avec des limites.

::: definition
Soit f une fonction définie sur un intervalle ouvert I et a un réel de I. **f est continue en a** si et seulement si lim x→a f(x) = f(a).

Si f est définie sur [a ; b[ (ou [a ; +∞[), elle est **continue à droite en a** si lim x→a⁺ f(x) = f(a). Si f est définie sur ]b ; a] (ou ]−∞ ; a]), elle est **continue à gauche en a** si lim x→a⁻ f(x) = f(a).
:::

::: figure Trois courbes au-dessus de l'abscisse 2 : f passe par son point sans coupure, g a un trou, h fait un saut
<svg viewBox="0 0 470 172"><title>Trois courbes au voisinage de l'abscisse 2 : f passe par son point, g a un trou, h fait un saut</title><line x1="36" y1="132" x2="152" y2="132" stroke="#0f172a" stroke-width="1.6"/><line x1="36" y1="132" x2="36" y2="22" stroke="#0f172a" stroke-width="1.6"/><polygon points="152,132 145,128.5 145,135.5" fill="#0f172a"/><polygon points="36,22 32.5,29 39.5,29" fill="#0f172a"/><text x="148" y="125" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="44" y="30" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="94" y1="129" x2="94" y2="135" stroke="#0f172a" stroke-width="1.3"/><text x="94" y="147" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="33" y1="110" x2="39" y2="110" stroke="#0f172a" stroke-width="1.3"/><text x="30" y="114" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="33" y1="88" x2="39" y2="88" stroke="#0f172a" stroke-width="1.3"/><text x="30" y="92" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="33" y1="66" x2="39" y2="66" stroke="#0f172a" stroke-width="1.3"/><text x="30" y="70" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><polyline points="41.8,129.8 45.4,128.4 49,127.1 52.5,125.7 56.1,124.4 59.7,123 63.3,121.7 66.8,120.3 70.4,118.9 74,117.6 77.6,116.2 81.1,114.9 84.7,113.5 88.3,112.2 91.9,110.8 95.4,109.5 99,108.1 102.6,106.7 106.2,105.4 109.8,104 113.3,102.7 116.9,101.3 120.5,100 124.1,98.6 127.6,97.2 131.2,95.9 134.8,94.5 138.4,93.2 141.9,91.8 145.5,90.5 149.1,89.1" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="94" cy="110" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="100" y="132" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f(2) = 1</text><text x="62.1" y="36.8" text-anchor="middle" font-size="14" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f</text><line x1="190" y1="132" x2="306" y2="132" stroke="#0f172a" stroke-width="1.6"/><line x1="190" y1="132" x2="190" y2="22" stroke="#0f172a" stroke-width="1.6"/><polygon points="306,132 299,128.5 299,135.5" fill="#0f172a"/><polygon points="190,22 186.5,29 193.5,29" fill="#0f172a"/><text x="302" y="125" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="198" y="30" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="248" y1="129" x2="248" y2="135" stroke="#0f172a" stroke-width="1.3"/><text x="248" y="147" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="187" y1="110" x2="193" y2="110" stroke="#0f172a" stroke-width="1.3"/><text x="184" y="114" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="187" y1="88" x2="193" y2="88" stroke="#0f172a" stroke-width="1.3"/><text x="184" y="92" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="187" y1="66" x2="193" y2="66" stroke="#0f172a" stroke-width="1.3"/><text x="184" y="70" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><polyline points="195.8,129.8 199.4,128.4 203,127.1 206.5,125.7 210.1,124.4 213.7,123 217.3,121.7 220.8,120.3 224.4,118.9 228,117.6 231.6,116.2 235.1,114.9 238.7,113.5 242.3,112.2 245.9,110.8 249.4,109.5 253,108.1 256.6,106.7 260.2,105.4 263.8,104 267.3,102.7 270.9,101.3 274.5,100 278.1,98.6 281.6,97.2 285.2,95.9 288.8,94.5 292.4,93.2 295.9,91.8 299.5,90.5 303.1,89.1" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="248" cy="110" r="4" fill="#ffffff" stroke="#0f6e56" stroke-width="2.3"/><circle cx="248" cy="88" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="256" y="84" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">g(2) = 2</text><text x="216.1" y="36.8" text-anchor="middle" font-size="14" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">g</text><line x1="344" y1="132" x2="460" y2="132" stroke="#0f172a" stroke-width="1.6"/><line x1="344" y1="132" x2="344" y2="22" stroke="#0f172a" stroke-width="1.6"/><polygon points="460,132 453,128.5 453,135.5" fill="#0f172a"/><polygon points="344,22 340.5,29 347.5,29" fill="#0f172a"/><text x="456" y="125" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="352" y="30" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="402" y1="129" x2="402" y2="135" stroke="#0f172a" stroke-width="1.3"/><text x="402" y="147" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="341" y1="110" x2="347" y2="110" stroke="#0f172a" stroke-width="1.3"/><text x="338" y="114" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="341" y1="88" x2="347" y2="88" stroke="#0f172a" stroke-width="1.3"/><text x="338" y="92" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="341" y1="66" x2="347" y2="66" stroke="#0f172a" stroke-width="1.3"/><text x="338" y="70" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><polyline points="349.8,129.8 352.4,128.8 355,127.8 357.6,126.8 360.2,125.8 362.9,124.8 365.5,123.9 368.1,122.9 370.7,121.9 373.3,120.9 375.9,119.9 378.5,118.9 381.1,117.9 383.7,116.9 386.3,115.9 388.9,115 391.6,114 394.2,113 396.8,112 399.4,111 402,110" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="402" cy="110" r="4" fill="#ffffff" stroke="#0f6e56" stroke-width="2.3"/><polyline points="402,66 404.8,65 407.5,63.9 410.3,62.9 413,61.8 415.8,60.8 418.5,59.7 421.3,58.7 424,57.6 426.8,56.6 429.6,55.5 432.3,54.5 435.1,53.5 437.8,52.4 440.6,51.4 443.3,50.3 446.1,49.3 448.8,48.2 451.6,47.2 454.3,46.1 457.1,45.1" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="402" cy="66" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="394" y="60" text-anchor="end" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">h(2) = 3</text><text x="370.1" y="36.8" text-anchor="middle" font-size="14" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">h</text></svg>
:::

Sur chaque courbe, le point plein est (2 ; valeur en 2) et le cercle vide est un point absent : seule f est continue en 2, car sa limite en 2 est égale à f(2) ; g a pour limite 1 mais g(2) = 2, et h a deux limites différentes de chaque côté.

::: exemple Le prix du parking en t = 3 : c(t) = 2t si t ≤ 3, c(t) = t + 3 si t > 3
1. À gauche de 3, c(t) = 2t est un polynôme, donc continu : lim t→3⁻ c(t) = 2 × 3 = 6.
2. À droite de 3, c(t) = t + 3 est un polynôme : lim t→3⁺ c(t) = 3 + 3 = 6.
3. La valeur en 3 vient de la première formule, car 3 ≤ 3 : c(3) = 6.
4. Limite à gauche, limite à droite et c(3) valent 6 : c est continue en 3, le prix ne saute pas.

:::

::: piege Ne regarder qu'un côté : la partie entière en 2
La partie entière E(x) est le plus grand entier inférieur ou égal à x : E(1,7) = 1 et E(2,3) = 2. En 2, on calcule E(2) = 2 et lim x→2⁺ E(x) = 2, puisque E(x) = 2 sur [2 ; 3[, et l'on conclut « E est continue en 2 ». Cela tente parce que la courbe colle à la valeur de ce côté. Mais E(x) = 1 sur [1 ; 2[, donc lim x→2⁻ E(x) = 1 ≠ 2 : E est continue à droite en 2, pas à gauche, donc pas continue en 2.
:::

::: propriete
- f est continue en a si et seulement si elle est continue à droite et à gauche en a, c'est-à-dire si lim x→a⁻ f(x) = lim x→a⁺ f(x) = f(a).
- Pour une fonction définie par deux formules, on calcule la limite de chaque formule en a et l'on compare avec f(a), donné par la formule qui porte l'égalité (≤ ou ≥).

Cas limite : à l'extrémité d'un intervalle, un seul côté existe. x ↦ √x n'est définie qu'à droite de 0 et y est continue à droite, car lim x→0⁺ √x = 0 = √0.
:::

::: verifie
Soit g(x) = 3x − 1 pour x < 1 et g(x) = x² + 2 pour x ≥ 1. La fonction g est-elle continue en 1 ?

---

À gauche, lim x→1⁻ (3x − 1) = 2 (polynôme). À droite, lim x→1⁺ (x² + 2) = 3, et g(1) = 1² + 2 = 3 car x ≥ 1 donne la seconde formule. Donc g est continue à droite en 1, mais 2 ≠ 3 : elle n'est pas continue à gauche, donc pas continue en 1. On a contrôlé les deux côtés.
:::

::: retenir
f est continue en a quand la limite à gauche, la limite à droite et f(a) sont égales ; pour une fonction à deux formules, on contrôle les deux côtés.
:::

## 🧱 Continuité sur un intervalle et opérations

Une montre numérique affiche le nombre entier de minutes écoulées : à l'instant t, elle montre E(t).
Sur quels intervalles de temps l'affichage change-t-il d'un coup, et sur lesquels reste-t-il « d'un seul trait » ? Et comment éviter de contrôler un à un tous les points d'une formule compliquée ?

::: definition
**f est continue sur ]a ; b[** si elle est continue en tout point de ]a ; b[. **f est continue sur [a ; b]** si elle est continue en tout point de ]a ; b[, continue à droite en a et continue à gauche en b. On définit de même la continuité sur [a ; b[, ]a ; b], [a ; +∞[ et ]−∞ ; a].
:::

::: figure La courbe de E est faite de marches : sur [2 ; 3[, tracée d'un seul trait ; en 3, elle saute de 2 à 3
<svg viewBox="0 0 340 230"><title>Courbe de la partie entière E : des marches, point plein à gauche, cercle vide à droite</title><line x1="20" y1="182.4" x2="320" y2="182.4" stroke="#0f172a" stroke-width="1.6"/><line x1="44.5" y1="204" x2="44.5" y2="14" stroke="#0f172a" stroke-width="1.6"/><polygon points="320,182.4 313,178.9 313,185.9" fill="#0f172a"/><polygon points="44.5,14 41,21 48,21" fill="#0f172a"/><text x="316" y="175.4" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="52.5" y="22" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="105.7" y1="179.4" x2="105.7" y2="185.4" stroke="#0f172a" stroke-width="1.3"/><text x="105.7" y="197.4" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="166.9" y1="179.4" x2="166.9" y2="185.4" stroke="#0f172a" stroke-width="1.3"/><text x="166.9" y="197.4" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="228.2" y1="179.4" x2="228.2" y2="185.4" stroke="#0f172a" stroke-width="1.3"/><text x="228.2" y="197.4" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="289.4" y1="179.4" x2="289.4" y2="185.4" stroke="#0f172a" stroke-width="1.3"/><text x="289.4" y="197.4" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="41.5" y1="139.2" x2="47.5" y2="139.2" stroke="#0f172a" stroke-width="1.3"/><text x="38.5" y="143.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="41.5" y1="96" x2="47.5" y2="96" stroke="#0f172a" stroke-width="1.3"/><text x="38.5" y="100" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="41.5" y1="52.9" x2="47.5" y2="52.9" stroke="#0f172a" stroke-width="1.3"/><text x="38.5" y="56.9" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="44.5" y1="182.4" x2="105.7" y2="182.4" stroke="#0f172a" stroke-width="3.0"/><circle cx="44.5" cy="182.4" r="3.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="105.7" cy="182.4" r="3.8" fill="#ffffff" stroke="#0f172a" stroke-width="2.3"/><line x1="105.7" y1="139.2" x2="166.9" y2="139.2" stroke="#0f172a" stroke-width="3.0"/><circle cx="105.7" cy="139.2" r="3.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="166.9" cy="139.2" r="3.8" fill="#ffffff" stroke="#0f172a" stroke-width="2.3"/><line x1="166.9" y1="96" x2="228.2" y2="96" stroke="#0f6e56" stroke-width="3.0"/><circle cx="166.9" cy="96" r="3.8" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="228.2" cy="96" r="3.8" fill="#ffffff" stroke="#0f6e56" stroke-width="2.3"/><line x1="228.2" y1="52.9" x2="289.4" y2="52.9" stroke="#0f172a" stroke-width="3.0"/><circle cx="228.2" cy="52.9" r="3.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="289.4" cy="52.9" r="3.8" fill="#ffffff" stroke="#0f172a" stroke-width="2.3"/><text x="197.6" y="84" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">[2 ; 3[</text></svg>
:::

Chaque marche a un point plein à gauche et un cercle vide à droite : le point plein (2 ; 2) appartient à la courbe, le cercle vide (3 ; 2) non, car E(3) = 3.

::: exemple Sur quels intervalles E est-elle continue ? (l'affichage de la montre entre 2 et 3 minutes)
1. Sur ]2 ; 3[, E(x) = 2 est constante, donc continue en tout point de cet intervalle.
2. En 2, à droite : lim x→2⁺ E(x) = 2 = E(2), donc E est continue à droite en 2.
3. Ces deux faits donnent la continuité de E sur [2 ; 3[ (point 2 à droite, intérieur continu).
4. En 3, à gauche : lim x→3⁻ E(x) = 2 ≠ 3 = E(3). E n'est pas continue sur [2 ; 3] ni sur ]2 ; 3] : un seul point de rupture suffit.

:::

::: exemple Intervalles de continuité d'un quotient et d'une racine
1. q(x) = (2x − 1)/(x² − 5x + 6) : le dénominateur (x − 2)(x − 3) s'annule en 2 et en 3, donc q est définie sur ℝ privé de {2 ; 3}.
2. q est une fraction rationnelle, continue là où elle est définie : q est continue sur ]−∞ ; 2[, sur ]2 ; 3[ et sur ]3 ; +∞[.
3. r(x) = √(x² − 4x + 3) : x² − 4x + 3 = (x − 1)(x − 3) est positif ou nul si x ≤ 1 ou x ≥ 3 (signe d'un trinôme à l'extérieur de ses racines).
4. Sur chacun de ces intervalles, le polynôme est continu et positif : r est continue sur ]−∞ ; 1] et sur [3 ; +∞[.

:::

::: piege Simplifier d'abord, chercher le domaine ensuite
Pour f(x) = (x² − 9)/(x − 3), on simplifie : f(x) = x + 3, et l'on écrit « f est continue sur ℝ ». Cela tente parce que x + 3 est un polynôme. Mais l'égalité f(x) = x + 3 n'a lieu que pour x ≠ 3 : f n'est pas définie en 3, donc elle ne peut pas y être continue. Elle est continue sur ]−∞ ; 3[ et sur ]3 ; +∞[, et nous verrons plus bas comment recoller le trou.
:::

::: propriete
Soient f et g continues sur un intervalle I.

- f + g, f × g, |f| et k·f (k réel) sont continues sur I.
- Si g ne s'annule pas sur I, alors 1/g et f/g sont continues sur I.
- Si f(x) ≥ 0 pour tout x de I, alors √f est continue sur I.

Conséquences : un polynôme est continu sur ℝ ; une fraction rationnelle est continue sur chacun des intervalles ouverts de son ensemble de définition ; sin et cos sont continues sur ℝ (admis).

Cas limite : ℝ privé de {3} n'est pas un intervalle. On dit « continue sur ]−∞ ; 3[ et sur ]3 ; +∞[ », ou « continue en tout point de ℝ privé de 3 », jamais « continue sur ℝ privé de 3 ».
:::

::: verifie
Donner l'ensemble de définition et les intervalles de continuité de p(x) = x/(|x| − 3).

---

|x| − 3 = 0 pour x = 3 ou x = −3 : p est définie sur ℝ privé de {−3 ; 3}. x ↦ x et x ↦ |x| − 3 sont continues sur ℝ, et le dénominateur ne s'annule pas sur ]−∞ ; −3[, sur ]−3 ; 3[ et sur ]3 ; +∞[ : p y est continue, intervalle par intervalle. On a d'abord cherché où le dénominateur s'annule.
:::

::: retenir
Continue sur un intervalle, c'est continue en chacun de ses points (du bon côté aux extrémités fermées) ; somme, produit, quotient (dénominateur non nul), |f| et √f (f ≥ 0) conservent la continuité.
:::

## 🕳️ Prolongement par continuité : boucher un trou

La fonction f(x) = (x² − 1)/(x − 1) n'est pas définie en 1 : on y obtient 0/0. Mais pour x ≠ 1, x² − 1 = (x − 1)(x + 1), donc f(x) = x + 1 : la courbe est la droite y = x + 1 privée d'un point.
Peut-on recoller ce trou, et avec quelle valeur en 1 ?

::: definition
Soit f définie sur un intervalle I sauf en un point a de I. Si f a en a une limite **réelle** ℓ, la fonction g définie sur I par g(x) = f(x) pour x ≠ a et g(a) = ℓ est continue en a. On l'appelle le **prolongement par continuité** de f en a.
:::

::: figure À gauche la courbe de f a un trou au point (1 ; 2) ; à droite la courbe de g est la même droite avec ce point rempli
<svg viewBox="0 0 400 200"><title>À gauche la courbe de f a un trou au point (1 ; 2) ; à droite la courbe de g est la même droite avec ce point rempli</title><line x1="32" y1="166" x2="182" y2="166" stroke="#0f172a" stroke-width="1.6"/><line x1="69.5" y1="166" x2="69.5" y2="16" stroke="#0f172a" stroke-width="1.6"/><polygon points="182,166 175,162.5 175,169.5" fill="#0f172a"/><polygon points="69.5,16 66,23 73,23" fill="#0f172a"/><text x="178" y="159" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="77.5" y="24" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="107" y1="163" x2="107" y2="169" stroke="#0f172a" stroke-width="1.3"/><text x="107" y="181" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="66.5" y1="91" x2="72.5" y2="91" stroke="#0f172a" stroke-width="1.3"/><text x="63.5" y="95" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><polyline points="39.5,158.5 44.1,153.9 48.8,149.2 53.4,144.6 58,140 62.6,135.4 67.2,130.8 71.9,126.1 76.5,121.5 81.1,116.9 85.8,112.2 90.4,107.6 95,103 99.6,98.4 104.2,93.8 108.9,89.1 113.5,84.5 118.1,79.9 122.8,75.2 127.4,70.6 132,66 136.6,61.4 141.2,56.8 145.9,52.1 150.5,47.5 155.1,42.9 159.8,38.3 164.4,33.6 169,29 173.6,24.4 178.2,19.8" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="107" cy="91" r="4" fill="#ffffff" stroke="#0f6e56" stroke-width="2.3"/><line x1="107" y1="166" x2="107" y2="91" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="32" y1="91" x2="107" y2="91" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><text x="54.5" y="37" text-anchor="middle" font-size="14" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f</text><line x1="228" y1="166" x2="378" y2="166" stroke="#0f172a" stroke-width="1.6"/><line x1="265.5" y1="166" x2="265.5" y2="16" stroke="#0f172a" stroke-width="1.6"/><polygon points="378,166 371,162.5 371,169.5" fill="#0f172a"/><polygon points="265.5,16 262,23 269,23" fill="#0f172a"/><text x="374" y="159" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="273.5" y="24" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="303" y1="163" x2="303" y2="169" stroke="#0f172a" stroke-width="1.3"/><text x="303" y="181" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="262.5" y1="91" x2="268.5" y2="91" stroke="#0f172a" stroke-width="1.3"/><text x="259.5" y="95" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><polyline points="235.5,158.5 240.1,153.9 244.8,149.2 249.4,144.6 254,140 258.6,135.4 263.2,130.8 267.9,126.1 272.5,121.5 277.1,116.9 281.8,112.2 286.4,107.6 291,103 295.6,98.4 300.2,93.8 304.9,89.1 309.5,84.5 314.1,79.9 318.8,75.2 323.4,70.6 328,66 332.6,61.4 337.2,56.8 341.9,52.1 346.5,47.5 351.1,42.9 355.8,38.3 360.4,33.6 365,29 369.6,24.4 374.2,19.8" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="303" cy="91" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><line x1="303" y1="166" x2="303" y2="91" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="228" y1="91" x2="303" y2="91" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><text x="250.5" y="37" text-anchor="middle" font-size="14" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">g</text></svg>
:::

Le point plein de droite est g(1) : son ordonnée 2 est la limite de f en 1, que l'exemple va calculer.

::: exemple Prolonger f(x) = (x² − 1)/(x − 1) en 1
1. En 1, numérateur et dénominateur s'annulent : il faut transformer l'écriture avant de conclure.
2. Pour x ≠ 1, x² − 1 = (x − 1)(x + 1), donc f(x) = x + 1 : on simplifie par le facteur x − 1, non nul.
3. x ↦ x + 1 est continue en 1, donc lim x→1 f(x) = 2 : la limite est un réel.
4. On pose g(1) = 2 : g est continue en 1, et g(x) = x + 1 pour tout x.

:::

::: exemple Une seconde fonction : f(x) = (√(x + 4) − 2)/x en 0
1. En 0 on obtient 0/0, mais il n'y a pas de facteur évident : on multiplie haut et bas par l'expression conjuguée √(x + 4) + 2.
2. (√(x + 4) − 2)(√(x + 4) + 2) = (x + 4) − 4 = x, donc, pour x ≠ 0, f(x) = x/(x(√(x + 4) + 2)) = 1/(√(x + 4) + 2).
3. Cette fraction est continue en 0, son dénominateur valant 4 ≠ 0 : lim x→0 f(x) = 1/4.
4. On pose g(0) = 1/4 : le prolongement existe.

:::

::: piege Croire qu'un 0/0 se prolonge toujours
Soit f(x) = (x − 1)/(x² − 2x + 1). En 1, numérateur et dénominateur s'annulent comme dans l'exemple, et l'on écrit « on simplifie, donc on prolonge ». Mais x² − 2x + 1 = (x − 1)², donc f(x) = 1/(x − 1) pour x ≠ 1 : cette quantité tend vers +∞ à droite de 1 et vers −∞ à gauche. Il n'y a pas de limite réelle, donc pas de prolongement. Un 0/0 est une forme à lever, pas une garantie.
:::

::: propriete
f, définie sur I sauf en a, se prolonge par continuité en a si et seulement si lim x→a f(x) existe et est un **réel** ℓ. Le prolongement g, avec g(a) = ℓ, est alors le seul prolongement de f continu en a : toute autre valeur g(a) = m ≠ ℓ donnerait une fonction non continue en a.

Cas limite : si la limite est infinie, ou si les limites à droite et à gauche diffèrent (|x|/x en 0 vaut −1 à gauche et 1 à droite), aucun prolongement n'existe.
:::

::: verifie
Soit h(x) = (x² + x − 6)/(x − 2) pour x ≠ 2. Se prolonge-t-elle par continuité en 2 ? Avec quelle valeur ?

---

x² + x − 6 = (x − 2)(x + 3) : on factorise pour faire apparaître x − 2. Pour x ≠ 2, h(x) = x + 3, donc lim x→2 h(x) = 5, un réel. Le prolongement existe, avec g(2) = 5.
:::

::: retenir
Un trou se bouche quand la limite en a est un réel ℓ : on pose alors g(a) = ℓ ; limite infinie ou limites différentes, pas de prolongement.
:::

## 🔗 Continuité d'une composée

Deux machines se suivent : la première calcule f(x) = x² − 6x + 8, la seconde prend la racine carrée. En x = 5, f(5) = 3 puis √3. Mais en x = 3, f(3) = −1 et la seconde machine refuse cette entrée.
Quand la chaîne complète est-elle définie, et continue ?

::: definition
Soit f définie sur un intervalle I, g définie sur un intervalle J, avec f(I) ⊂ J. La **composée** g∘f est la fonction définie sur I par (g∘f)(x) = g(f(x)) : on applique d'abord f, puis g.
:::

| x | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| f(x) = x² − 6x + 8 | 3 | 0 | −1 | 0 | 3 |
| √f(x) | √3 | 0 | non défini | 0 | √3 |

La deuxième ligne est la composée de la première avec la racine carrée : elle n'existe que là où f(x) ≥ 0, c'est-à-dire là où f(x) est dans l'ensemble de définition de la racine.

::: exemple Continuité de h(x) = √(x² − 6x + 8)
1. h = g∘f avec f(x) = x² − 6x + 8 et g(y) = √y : on repère la fonction intérieure, celle qu'on calcule d'abord.
2. f(x) = (x − 2)(x − 4) est positif ou nul sur ]−∞ ; 2] et sur [4 ; +∞[, négatif sur ]2 ; 4[ : f(]−∞ ; 2]) ⊂ ℝ₊ et f([4 ; +∞[) ⊂ ℝ₊.
3. f est continue sur ℝ (polynôme) et g est continue sur ℝ₊ : sur chacun de ces deux intervalles, la condition f(I) ⊂ ℝ₊ est remplie.
4. Donc h est continue sur ]−∞ ; 2] et sur [4 ; +∞[.

:::

::: exemple Une composée sans condition à vérifier : k(x) = cos(2x − π/3)
1. k = g∘f avec f(x) = 2x − π/3 et g = cos : on cherche d'abord la fonction intérieure.
2. f est continue sur ℝ (polynôme du premier degré) et g = cos est continue sur ℝ : f(ℝ) ⊂ ℝ est automatique.
3. Donc k est continue sur ℝ.

:::

::: piege Croire qu'une composée de fonctions continues est continue partout
On écrit : « x² − 6x + 8 est continue, √ est continue, donc h(x) = √(x² − 6x + 8) est continue sur ℝ ». Cela tente parce que la règle parle de fonctions continues. Mais h n'est même pas définie sur ]2 ; 4[ : f(3) = −1 < 0. Il faut que f(I) soit contenu dans l'ensemble où g est définie et continue ; ici h est continue sur ]−∞ ; 2] et sur [4 ; +∞[, et sur eux seuls.
:::

::: propriete
- **En un point** : si f est continue en x₀ et si g est continue en f(x₀), alors g∘f est continue en x₀.
- **Sur un intervalle** : si f est continue sur I, g est continue sur J et f(I) ⊂ J, alors g∘f est continue sur I.

Cas limite : la condition f(I) ⊂ J est indispensable. En particulier, la composée de deux fonctions continues sur ℝ est continue sur ℝ.
:::

::: verifie
Montrer que t(x) = √(9 − x²) est continue sur [−3 ; 3].

---

f(x) = 9 − x² est un polynôme, continu sur ℝ. Comme 9 − x² = (3 − x)(3 + x), il est positif ou nul entre ses racines : f([−3 ; 3]) ⊂ ℝ₊, où la racine carrée est continue. Donc t = g∘f est continue sur [−3 ; 3]. On a vérifié f(I) ⊂ J avant d'appliquer la règle.
:::

::: retenir
g∘f est continue là où f est continue et où f(x) reste dans un intervalle où g est continue : toujours vérifier f(I) ⊂ J.
:::

## 🌉 Théorème des valeurs intermédiaires et dichotomie

Soit f(x) = x³ + x − 3. On calcule f(1) = −1 et f(2) = 7 : la courbe est sous l'axe des abscisses en 1 et au-dessus en 2.
A-t-elle forcément coupé l'axe entre les deux ? Et peut-on repérer le point de croisement sans résoudre une équation du troisième degré ?

::: figure La courbe de x³ + x − 3 relie (1 ; −1) à (2 ; 7) sans saut : elle coupe l'axe des abscisses en α et la droite y = 3 en c
<svg viewBox="0 0 340 260"><title>Courbe de x³ + x − 3 entre les points (1 ; −1) et (2 ; 7) : elle coupe l'axe des abscisses en α et la droite y = 3 en c</title><line x1="40" y1="165.5" x2="320" y2="165.5" stroke="#0f172a" stroke-width="1.6"/><line x1="63.3" y1="230" x2="63.3" y2="10" stroke="#0f172a" stroke-width="1.6"/><polygon points="320,165.5 313,162 313,169" fill="#0f172a"/><polygon points="63.3,10 59.8,17 66.8,17" fill="#0f172a"/><text x="316" y="158.5" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="71.3" y="18" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="180" y1="162.5" x2="180" y2="168.5" stroke="#0f172a" stroke-width="1.3"/><text x="180" y="180.5" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="296.7" y1="162.5" x2="296.7" y2="168.5" stroke="#0f172a" stroke-width="1.3"/><text x="296.7" y="180.5" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="60.3" y1="184.5" x2="66.3" y2="184.5" stroke="#0f172a" stroke-width="1.3"/><text x="57.3" y="188.5" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="60.3" y1="108.6" x2="66.3" y2="108.6" stroke="#0f172a" stroke-width="1.3"/><text x="57.3" y="112.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="60.3" y1="32.8" x2="66.3" y2="32.8" stroke="#0f172a" stroke-width="1.3"/><text x="57.3" y="36.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7</text><polyline points="63.3,222.4 66.1,222 68.8,221.5 71.5,221.1 74.2,220.6 76.9,220.2 79.7,219.7 82.4,219.2 85.1,218.8 87.8,218.3 90.6,217.7 93.3,217.2 96,216.7 98.7,216.1 101.4,215.6 104.2,215 106.9,214.3 109.6,213.7 112.3,213 115.1,212.4 117.8,211.6 120.5,210.9 123.2,210.1 125.9,209.3 128.7,208.5 131.4,207.6 134.1,206.7 136.8,205.7 139.6,204.7 142.3,203.7 145,202.6 147.7,201.5 150.4,200.4 153.2,199.2 155.9,197.9 158.6,196.6 161.3,195.2 164.1,193.8 166.8,192.4 169.5,190.9 172.2,189.3 174.9,187.7 177.7,186 180.4,184.2 183.1,182.4 185.8,180.5 188.6,178.6 191.3,176.6 194,174.5 196.7,172.4 199.4,170.2 202.2,167.9 204.9,165.5 207.6,163.1 210.3,160.6 213.1,158 215.8,155.3 218.5,152.6 221.2,149.7 223.9,146.8 226.7,143.8 229.4,140.7 232.1,137.6 234.8,134.3 237.6,130.9 240.3,127.5 243,123.9 245.7,120.3 248.4,116.6 251.2,112.7 253.9,108.8 256.6,104.8 259.3,100.6 262.1,96.4 264.8,92 267.5,87.6 270.2,83 272.9,78.3 275.7,73.6 278.4,68.7 281.1,63.7 283.8,58.5 286.6,53.3 289.3,47.9 292,42.4 294.7,36.8 297.4,31.1 300.2,25.3 302.9,19.3 305.6,13.2 308.3,6.9" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="40" y1="108.6" x2="254" y2="108.6" stroke="#b45309" stroke-width="1.4" stroke-dasharray="5 3"/><line x1="254" y1="165.5" x2="254" y2="108.6" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="180" y1="184.5" x2="180" y2="165.5" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="296.7" y1="165.5" x2="296.7" y2="32.8" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><circle cx="180" cy="184.5" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="296.7" cy="32.8" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="204.9" cy="165.5" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="254" cy="108.6" r="4" fill="#b45309" stroke="#0f172a" stroke-width="1"/><text x="195.9" y="157.5" text-anchor="middle" font-size="14" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">α</text><text x="254" y="181.5" text-anchor="middle" font-size="14" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">c</text><text x="80" y="102.6" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = 3</text><text x="188" y="200.5" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(1 ; −1)</text><text x="288.7" y="36.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(2 ; 7)</text></svg>
:::

Le point α est la solution de f(x) = 0, le point c celle de f(x) = 3 : la courbe passe par toutes les hauteurs comprises entre −1 et 7.

::: exemple Une solution de x³ + x − 3 = 0 dans [1 ; 2], puis un encadrement
1. f(x) = x³ + x − 3 est continue sur [1 ; 2], car c'est un polynôme.
2. f(1) = −1 et f(2) = 7 : 0 est compris entre f(1) et f(2), c'est-à-dire f(1) × f(2) < 0.
3. Par le théorème des valeurs intermédiaires, f(x) = 0 a au moins une solution α dans ]1 ; 2[.
4. À la calculatrice, f(1,2) = −0,072 < 0 et f(1,3) = 0,497 > 0 : le même théorème sur [1,2 ; 1,3] donne α ∈ ]1,2 ; 1,3[.
5. De même f(1,21) = −0,018439 < 0 et f(1,22) = 0,035848 > 0 : α ∈ ]1,21 ; 1,22[, donc α ≈ 1,21 par défaut à 10⁻² près.
6. f est la somme de deux fonctions strictement croissantes, x ↦ x³ et x ↦ x − 3 : si a < b, alors f(a) < f(b). Une fonction strictement croissante ne prend pas deux fois la même valeur, donc α est unique.

:::

::: exemple Un point fixe : f continue de [1 ; 3] dans [1 ; 3]
Soit f continue sur [1 ; 3], avec f(x) ∈ [1 ; 3] pour tout x. On cherche un réel c tel que f(c) = c.
1. On pose g(x) = f(x) − x, continue sur [1 ; 3] : on ramène « f(x) = x » à « g(x) = 0 ».
2. f(1) et f(3) sont dans [1 ; 3] : f(1) ≥ 1 et f(3) ≤ 3, donc g(1) = f(1) − 1 ≥ 0 et g(3) = f(3) − 3 ≤ 0.
3. Donc g(1) × g(3) ≤ 0 : par le théorème des valeurs intermédiaires (si le produit est nul, c'est déjà fait en 1 ou en 3), g s'annule en un réel c de [1 ; 3], et f(c) = c.

:::

::: piege Lire le théorème à l'envers
Pour f(x) = x² − 1 sur [−2 ; 2], f(−2) × f(2) = 3 × 3 > 0, et l'on conclut « f(x) = 0 n'a pas de solution dans [−2 ; 2] ». Cela tente parce que le théorème parle du produit f(a) × f(b). Mais il dit : produit négatif, donc solution ; il ne dit pas l'inverse. Ici f(−1) = f(1) = 0 : deux solutions. Quand le produit est positif, le théorème ne dit rien.
:::

::: propriete
- L'image d'un intervalle par une fonction continue est un intervalle.
- **Théorème des valeurs intermédiaires** : si f est continue sur [a ; b], alors pour tout réel λ compris entre f(a) et f(b), l'équation f(x) = λ a au moins une solution dans [a ; b].
- Si f(a) × f(b) < 0, alors f(x) = 0 a au moins une solution dans ]a ; b[.
- Si de plus f est **strictement monotone** sur [a ; b] (strictement croissante : u < v entraîne f(u) < f(v) ; strictement décroissante : u < v entraîne f(u) > f(v)), cette solution est unique.

Cas limite : « au moins une » ne veut pas dire « une seule » : sans stricte monotonie, x² − 1 s'annule deux fois sur [−2 ; 2].
:::

::: methode Encadrer la solution par dichotomie
Soit f continue et strictement monotone sur [a ; b], avec f(a) × f(b) < 0.
1. Calculer le milieu m = (a + b)/2, puis le signe de f(m) (si f(m) = 0, c'est fini).
2. Si f(m) a le même signe que f(a), la solution est dans [m ; b] ; sinon elle est dans [a ; m].
3. Recommencer sur l'intervalle retenu : son amplitude est divisée par 2 à chaque étape.

:::

| étape | intervalle de départ | milieu m | signe de f(m) | intervalle retenu |
| --- | --- | --- | --- | --- |
| 1 | [1 ; 2] | 1,5 | + (f(m) = 1,875) | [1 ; 1,5] |
| 2 | [1 ; 1,5] | 1,25 | + (f(m) = 0,203125) | [1 ; 1,25] |
| 3 | [1 ; 1,25] | 1,125 | − (f(m) = −0,451172) | [1,125 ; 1,25] |
| 4 | [1,125 ; 1,25] | 1,1875 | − (f(m) = −0,137939) | [1,1875 ; 1,25] |

Après 4 étapes, l'amplitude vaut 1/16 = 0,0625 : 1,1875 < α < 1,25. Le programme Pascal du manuel fait exactement ce travail ; en pseudo-code, avec n étapes :

```
a ← 1 ; b ← 2
pour k de 1 à n − 1 :
    m ← (a + b)/2
    si f(m) = 0 : renvoyer m
    si f(m) a le même signe que f(a) : a ← m
    sinon : b ← m
renvoyer (a + b)/2
```

::: verifie
Montrer que l'équation x³ + 3x − 5 = 0 a une unique solution dans [1 ; 2].

---

f(x) = x³ + 3x − 5 est continue (polynôme) et strictement croissante (somme de deux fonctions strictement croissantes). f(1) = −1 et f(2) = 9, donc f(1) × f(2) < 0 : le théorème des valeurs intermédiaires donne au moins une solution dans ]1 ; 2[, et la stricte croissance la rend unique.
:::

::: retenir
f continue prend toutes les valeurs entre f(a) et f(b) : f(a) × f(b) < 0 garantit une solution de f(x) = 0, unique si f est strictement monotone ; la dichotomie la coince en divisant l'intervalle par 2.
:::

## 🏰 Bijection et image d'un intervalle

Soit g(x) = x² − 2. Combien de solutions l'équation g(x) = 1 a-t-elle dans ℝ ? Et dans ℝ₊ ?
Sur quels intervalles chaque valeur a-t-elle exactement un antécédent ?

::: definition
Soit f une fonction définie sur un intervalle I, à valeurs dans un intervalle J. **f est une bijection de I sur J** si tout élément y de J a un antécédent et un seul dans I : l'équation f(x) = y a une unique solution dans I.
:::

::: figure La droite y = 1 coupe la parabole en deux points sur ℝ ; sur la seule branche x ≥ 0, elle n'en coupe qu'un
<svg viewBox="0 0 340 250"><title>Parabole y = x² − 2 et droite y = 1 : deux points d'intersection sur ℝ, un seul sur la branche x ≥ 0</title><line x1="20" y1="136" x2="320" y2="136" stroke="#0f172a" stroke-width="1.6"/><line x1="170" y1="234" x2="170" y2="10" stroke="#0f172a" stroke-width="1.6"/><polygon points="320,136 313,132.5 313,139.5" fill="#0f172a"/><polygon points="170,10 166.5,17 173.5,17" fill="#0f172a"/><text x="316" y="129" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="178" y="18" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="50" y1="133" x2="50" y2="139" stroke="#0f172a" stroke-width="1.3"/><text x="50" y="151" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="110" y1="133" x2="110" y2="139" stroke="#0f172a" stroke-width="1.3"/><text x="110" y="151" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="230" y1="133" x2="230" y2="139" stroke="#0f172a" stroke-width="1.3"/><text x="230" y="151" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="290" y1="133" x2="290" y2="139" stroke="#0f172a" stroke-width="1.3"/><text x="290" y="151" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="167" y1="206" x2="173" y2="206" stroke="#0f172a" stroke-width="1.3"/><text x="164" y="210" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="167" y1="101" x2="173" y2="101" stroke="#0f172a" stroke-width="1.3"/><text x="164" y="105" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="167" y1="66" x2="173" y2="66" stroke="#0f172a" stroke-width="1.3"/><text x="164" y="70" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><polyline points="26,4.4 29.6,14.4 33.2,24.1 36.8,33.5 40.4,42.7 44,51.7 47.6,60.3 51.2,68.8 54.8,77 58.4,84.9 62,92.6 65.6,100 69.2,107.2 72.8,114.1 76.4,120.8 80,127.3 83.6,133.4 87.2,139.3 90.8,145 94.4,150.4 98,155.6 101.6,160.5 105.2,165.2 108.8,169.6 112.4,173.7 116,177.7 119.6,181.3 123.2,184.7 126.8,187.9 130.4,190.8 134,193.4 137.6,195.8 141.2,197.9 144.8,199.8 148.4,201.5 152,202.9 155.6,204 159.2,204.9 162.8,205.5 166.4,205.9 170,206" fill="none" stroke="#94a3b8" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 3"/><polyline points="170,206 173.6,205.9 177.2,205.5 180.8,204.9 184.4,204 188,202.8 191.6,201.5 195.2,199.8 198.8,197.9 202.4,195.8 206,193.4 209.6,190.8 213.2,187.9 216.8,184.7 220.4,181.3 224,177.7 227.6,173.7 231.2,169.6 234.8,165.2 238.4,160.5 242,155.6 245.6,150.4 249.2,145 252.8,139.3 256.4,133.4 260,127.3 263.6,120.8 267.2,114.1 270.8,107.2 274.4,100 278,92.6 281.6,84.9 285.2,77 288.8,68.8 292.4,60.3 296,51.7 299.6,42.7 303.2,33.5 306.8,24.1 310.4,14.4 314,4.4" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="20" y1="101" x2="320" y2="101" stroke="#b45309" stroke-width="1.5" stroke-dasharray="5 3"/><circle cx="66.1" cy="101" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="273.9" cy="101" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><line x1="66.1" y1="136" x2="66.1" y2="101" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 3"/><line x1="273.9" y1="136" x2="273.9" y2="101" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 3"/><text x="316" y="94" text-anchor="end" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = 1</text><text x="290" y="199.5" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x ≥ 0</text><text x="50" y="199.5" text-anchor="end" font-size="11" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x < 0</text></svg>
:::

Les deux points noirs sont d'abscisses −√3 et √3 : sur ℝ, la valeur 1 a deux antécédents ; sur ℝ₊, un seul.

::: exemple g(x) = x² − 2 est une bijection de ℝ₊ sur [−2 ; +∞[
1. Soit y ∈ [−2 ; +∞[. L'équation x² − 2 = y équivaut à x² = y + 2, avec y + 2 ≥ 0 : elle a des solutions.
2. Ses solutions dans ℝ sont x = √(y + 2) et x = −√(y + 2).
3. Une seule appartient à ℝ₊ : x = √(y + 2). Existence et unicité sont acquises pour tout y de [−2 ; +∞[.
4. Donc g est une bijection de ℝ₊ sur [−2 ; +∞[. Sur ℝ, ce n'est pas le cas : y = 1 a deux antécédents (±√3) et y = −5 n'en a aucun.

:::

::: piege Oublier de vérifier que J est exactement l'ensemble des images
On affirme que sin est une bijection de [0 ; π/2[ sur [0 ; 1], parce que sin est croissante, avec sin 0 = 0 et sin(π/2) = 1. Cela tente parce que 0 et 1 sont les bornes qu'on lit. Mais π/2 n'est pas dans [0 ; π/2[ : la valeur 1 n'est jamais atteinte, donc 1 n'a pas d'antécédent. Sin est une bijection de [0 ; π/2[ sur [0 ; 1[.
:::

::: propriete
- **Théorème** : si f est strictement monotone sur un intervalle I, alors f est une bijection de I sur f(I).
- Si de plus f est continue sur I, f(I) est un intervalle, qui se lit avec les valeurs et les limites aux bornes :

| I | f strictement croissante | f strictement décroissante |
| --- | --- | --- |
| [a ; b] | [f(a) ; f(b)] | [f(b) ; f(a)] |
| [a ; b[ | [f(a) ; lim x→b⁻ f(x)[ | ] lim x→b⁻ f(x) ; f(a)] |
| ]a ; b] | ] lim x→a⁺ f(x) ; f(b)] | [f(b) ; lim x→a⁺ f(x)[ |
| ]a ; b[ | ] lim x→a⁺ f(x) ; lim x→b⁻ f(x)[ | ] lim x→b⁻ f(x) ; lim x→a⁺ f(x)[ |
| ]−∞ ; a] | ] lim x→−∞ f(x) ; f(a)] | [f(a) ; lim x→−∞ f(x)[ |
| ]−∞ ; a[ | ] lim x→−∞ f(x) ; lim x→a⁻ f(x)[ | ] lim x→a⁻ f(x) ; lim x→−∞ f(x)[ |
| [a ; +∞[ | [f(a) ; lim x→+∞ f(x)[ | ] lim x→+∞ f(x) ; f(a)] |
| ]a ; +∞[ | ] lim x→a⁺ f(x) ; lim x→+∞ f(x)[ | ] lim x→+∞ f(x) ; lim x→a⁺ f(x)[ |
| ℝ | ] lim x→−∞ f(x) ; lim x→+∞ f(x)[ | ] lim x→+∞ f(x) ; lim x→−∞ f(x)[ |

Cas limite : une borne ouverte reste ouverte, car la valeur limite est approchée sans être atteinte. La continuité seule ne suffit pas : x ↦ x² est continue sur [−1 ; 2] mais n'y est pas une bijection.
:::

::: exemple Bijection et image pour f(x) = x² − 6x + 10 sur ]−∞ ; 3]
1. f(x) = (x − 3)² + 1. Pour a < b ≤ 3, on a 0 ≤ 3 − b < 3 − a, donc (3 − b)² < (3 − a)² : f(b) < f(a), f est strictement décroissante sur ]−∞ ; 3].
2. f est continue (polynôme) : c'est une bijection de ]−∞ ; 3] sur f(]−∞ ; 3]).
3. f(3) = 1 et lim x→−∞ f(x) = +∞ : la ligne ]−∞ ; a] du tableau, colonne décroissante, donne [f(3) ; +∞[.
4. Donc f est une bijection de ]−∞ ; 3] sur [1 ; +∞[.

:::

::: verifie
Montrer que f(x) = 1/(x − 1) est une bijection de ]1 ; +∞[ sur un intervalle J à préciser.

---

Pour 1 < a < b, 0 < a − 1 < b − 1, donc 1/(a − 1) > 1/(b − 1) : f est strictement décroissante, et continue (quotient). Elle est donc une bijection de ]1 ; +∞[ sur f(]1 ; +∞[). Aux bornes, lim x→1⁺ f(x) = +∞ et lim x→+∞ f(x) = 0 : la ligne ]a ; +∞[, colonne décroissante, donne J = ]0 ; +∞[.
:::

::: retenir
f strictement monotone sur I ⟹ f bijection de I sur f(I) ; si f est continue, f(I) se lit avec les valeurs et limites aux bornes, bornes échangées si f décroît.
:::

## 🪞 Fonction réciproque et symétrie

Reprenons g(x) = x² − 2 sur ℝ₊, bijection sur [−2 ; +∞[ : g(3) = 7. Chaque valeur de [−2 ; +∞[ a un seul antécédent, donc une machine « retour » existe : celle qui, à 7, renvoie 3.
Comment la construire, et que dit sa courbe par rapport à celle de g ?

::: definition
Soit f une bijection d'un intervalle I sur un intervalle J. La **fonction réciproque** de f, notée f⁻¹, est la fonction définie sur J, à valeurs dans I, telle que pour x ∈ J et y ∈ I : y = f⁻¹(x) équivaut à x = f(y).
:::

::: figure La courbe de la réciproque se déduit de celle de g en la repliant le long de la droite Δ : le point M(1 ; −1) devient M′(−1 ; 1)
<svg viewBox="0 0 310 300"><title>Courbes de g (x ↦ x² − 2 sur ℝ₊) et de sa réciproque, symétriques par rapport à la droite Δ : y = x</title><line x1="14" y1="182" x2="294" y2="182" stroke="#0f172a" stroke-width="1.6"/><line x1="122" y1="290" x2="122" y2="10" stroke="#0f172a" stroke-width="1.6"/><polygon points="294,182 287,178.5 287,185.5" fill="#0f172a"/><polygon points="122,10 118.5,17 125.5,17" fill="#0f172a"/><text x="290" y="175" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="130" y="18" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="42" y1="179" x2="42" y2="185" stroke="#0f172a" stroke-width="1.3"/><text x="42" y="197" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="82" y1="179" x2="82" y2="185" stroke="#0f172a" stroke-width="1.3"/><text x="82" y="197" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="162" y1="179" x2="162" y2="185" stroke="#0f172a" stroke-width="1.3"/><text x="162" y="197" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="202" y1="179" x2="202" y2="185" stroke="#0f172a" stroke-width="1.3"/><text x="202" y="197" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="242" y1="179" x2="242" y2="185" stroke="#0f172a" stroke-width="1.3"/><text x="242" y="197" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="282" y1="179" x2="282" y2="185" stroke="#0f172a" stroke-width="1.3"/><text x="282" y="197" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="119" y1="262" x2="125" y2="262" stroke="#0f172a" stroke-width="1.3"/><text x="116" y="266" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="119" y1="222" x2="125" y2="222" stroke="#0f172a" stroke-width="1.3"/><text x="116" y="226" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="119" y1="142" x2="125" y2="142" stroke="#0f172a" stroke-width="1.3"/><text x="116" y="146" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="119" y1="102" x2="125" y2="102" stroke="#0f172a" stroke-width="1.3"/><text x="116" y="106" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="119" y1="62" x2="125" y2="62" stroke="#0f172a" stroke-width="1.3"/><text x="116" y="66" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="119" y1="22" x2="125" y2="22" stroke="#0f172a" stroke-width="1.3"/><text x="116" y="26" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="22" y1="282" x2="290" y2="14" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="6 4"/><polyline points="122,262 123.7,261.9 125.3,261.7 127,261.4 128.6,260.9 130.3,260.3 132,259.5 133.6,258.6 135.3,257.6 136.9,256.4 138.6,255.1 140.3,253.7 141.9,252.1 143.6,250.4 145.2,248.5 146.9,246.5 148.6,244.4 150.2,242.1 151.9,239.7 153.5,237.1 155.2,234.4 156.9,231.6 158.5,228.7 160.2,225.6 161.8,222.3 163.5,218.9 165.2,215.4 166.8,211.8 168.5,208 170.1,204.1 171.8,200 173.5,195.8 175.1,191.5 176.8,187 178.4,182.4 180.1,177.6 181.8,172.7 183.4,167.7 185.1,162.5 186.7,157.2 188.4,151.8 190.1,146.2 191.7,140.5 193.4,134.6 195,128.6 196.7,122.5 198.4,116.2 200,109.8 201.7,103.3 203.3,96.6 205,89.8 206.7,82.8 208.3,75.7 210,68.5 211.6,61.1 213.3,53.6 215,46 216.6,38.2 218.3,30.3 219.9,22.2 221.6,14" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="42,182 45.5,170.1 49.1,165.2 52.6,161.4 56.2,158.2 59.7,155.4 63.3,152.8 66.8,150.5 70.3,148.3 73.9,146.3 77.4,144.4 81,142.5 84.5,140.8 88.1,139.1 91.6,137.5 95.1,135.9 98.7,134.4 102.2,132.9 105.8,131.5 109.3,130.1 112.9,128.8 116.4,127.4 119.9,126.2 123.5,124.9 127,123.7 130.6,122.5 134.1,121.3 137.7,120.1 141.2,119 144.7,117.9 148.3,116.8 151.8,115.7 155.4,114.7 158.9,113.6 162.5,112.6 166,111.6 169.5,110.6 173.1,109.6 176.6,108.6 180.2,107.7 183.7,106.7 187.3,105.8 190.8,104.9 194.3,103.9 197.9,103 201.4,102.1 205,101.3 208.5,100.4 212.1,99.5 215.6,98.7 219.1,97.8 222.7,97 226.2,96.2 229.8,95.3 233.3,94.5 236.9,93.7 240.4,92.9 243.9,92.1 247.5,91.3 251,90.6 254.6,89.8 258.1,89 261.7,88.3 265.2,87.5 268.7,86.8 272.3,86 275.8,85.3 279.4,84.6 282.9,83.8 286.5,83.1 290,82.4" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="162" y1="222" x2="82" y2="142" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="3 3"/><circle cx="162" cy="222" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="82" cy="142" r="4" fill="#b45309" stroke="#0f172a" stroke-width="1"/><text x="175" y="226" text-anchor="start" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><text x="74" y="136" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M′</text><text x="242" y="170" text-anchor="start" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_g</text><text x="250" y="82.8" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_g⁻¹</text><text x="264" y="52" text-anchor="end" font-size="12" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Δ : y = x</text></svg>
:::

M est sur la courbe de g puisque g(1) = −1 ; ses coordonnées échangées donnent M′, sur la courbe de la réciproque : g⁻¹(−1) = 1.

::: exemple Expliciter la réciproque de g(x) = x² − 2
1. g est une bijection de ℝ₊ sur [−2 ; +∞[ (section précédente) : sa réciproque existe.
2. Soit x ∈ [−2 ; +∞[ et y ∈ ℝ₊. x = g(y) équivaut à x = y² − 2, donc à y² = x + 2 : on exprime y en fonction de x.
3. Comme y ≥ 0, on garde la seule racine positive : y = √(x + 2).
4. Donc g⁻¹(x) = √(x + 2) sur [−2 ; +∞[. Vérification : g(3) = 7 et g⁻¹(7) = √9 = 3 ✓.

:::

::: exemple Une réciproque dont l'intervalle compte : f(x) = 3 − √x
1. √x est strictement croissante sur ℝ₊, donc f est strictement décroissante et continue : c'est une bijection de ℝ₊ sur f(ℝ₊) = ]−∞ ; 3].
2. Soit x ∈ ]−∞ ; 3] et y ∈ ℝ₊ : x = 3 − √y équivaut à √y = 3 − x.
3. Comme x ≤ 3, on a 3 − x ≥ 0 : on peut élever au carré, y = (3 − x)².
4. Donc f⁻¹(x) = (3 − x)² sur ]−∞ ; 3]. Vérification : f(4) = 1 et f⁻¹(1) = (3 − 1)² = 4 ✓.

:::

::: exemple Une réciproque déjà rencontrée : sin⁻¹
1. sin est continue et strictement croissante sur [0 ; π/2], de sin 0 = 0 à sin(π/2) = 1 : c'est une bijection de [0 ; π/2] sur [0 ; 1].
2. Sa réciproque, notée sin⁻¹, est définie sur [0 ; 1] à valeurs dans [0 ; π/2].
3. sin(π/6) = 1/2 avec π/6 ∈ [0 ; π/2], donc sin⁻¹(1/2) = π/6 (et non 1/sin(1/2)).

:::

::: piege Confondre f⁻¹ et 1/f
Avec g(x) = x² − 2, on calcule g⁻¹(7) en écrivant 1/g(7) = 1/47. Cela tente parce que l'exposant −1 évoque un inverse. Mais g⁻¹(7) est l'antécédent de 7, c'est-à-dire 3, puisque g(3) = 7. Le nombre 1/g(7) = 1/47 est tout autre chose.
:::

::: propriete
Soit f une bijection de I sur J.

- **Théorème 1** : si f est strictement monotone sur I, f est une bijection de I sur f(I) ; si de plus f est continue sur I, alors f⁻¹ est continue sur f(I).
- **Théorème 2** : f et f⁻¹ ont le même sens de variation ; dans un repère orthonormé, leurs courbes sont symétriques par rapport à la droite d'équation y = x.

Cas limite : la symétrie exige un repère orthonormé. Et « même sens de variation » ne veut pas dire « même signe » : f(x) = x + 10 est positive sur [−1 ; 1], mais f⁻¹(x) = x − 10 est négative sur [9 ; 11].
:::

::: verifie
Soit f(x) = x² − 2x sur [1 ; +∞[ ; on admet que f est une bijection de [1 ; +∞[ sur [−1 ; +∞[. Calculer f(4), puis donner un point de la courbe de f⁻¹.

---

f(4) = 16 − 8 = 8. Par définition, f(4) = 8 équivaut à f⁻¹(8) = 4 : le point (8 ; 4) est sur la courbe de f⁻¹, symétrique de (4 ; 8) par rapport à la droite y = x. On a échangé abscisse et ordonnée.
:::

::: retenir
y = f⁻¹(x) équivaut à x = f(y) : pour expliciter f⁻¹, on résout x = f(y) en y et on garde la solution qui est dans I ; la courbe de f⁻¹ est la symétrique de celle de f par rapport à y = x.
:::

## 🔮 La fonction racine nᵉ

Un capital est multiplié par 16 en 4 ans, avec le même coefficient multiplicateur c chaque année : c⁴ = 16.
Quel est c ? Et comment nommer c quand on a seulement c⁴ = 10 ?

::: definition
Soit n un entier supérieur ou égal à 2. La fonction x ↦ xⁿ est une bijection strictement croissante de ℝ₊ sur ℝ₊. Sa réciproque est la **fonction racine nᵉ**, notée ⁿ√ : ⁿ√ : ℝ₊ → ℝ₊, x ↦ ⁿ√x (« racine nᵉ de x »).

Pour x ≥ 0 et y ≥ 0 : y = ⁿ√x équivaut à x = yⁿ ; on a (ⁿ√x)ⁿ = x et ⁿ√(yⁿ) = y.
:::

| y | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| x = y⁴ | 0 | 1 | 16 | 81 |
| ⁴√x | 0 | 1 | 2 | 3 |

La dernière ligne ramène à la première : ⁴√ défait y ↦ y⁴ sur ℝ₊.

::: exemple Calculer des racines nᵉ
1. c⁴ = 16 avec c ≥ 0 : 2⁴ = 16, donc c = ⁴√16 = 2 (le capital double chaque année).
2. ⁶√729 : on cherche un réel positif dont la puissance 6 vaut 729 ; 3⁶ = 729, donc ⁶√729 = 3.
3. (⁵√7)⁵ = 7 : c'est directement (ⁿ√x)ⁿ = x.
4. ⁷√(3²⁸) : 3²⁸ = (3⁴)⁷ avec 3⁴ ≥ 0, donc ⁷√(3²⁸) = 3⁴ = 81.

:::

::: piege Croire que ⁿ√(yⁿ) = y pour tout réel y
On écrit ⁴√((−2)⁴) = −2. Cela tente parce que racine et puissance semblent se défaire. Mais ⁴√ renvoie un réel positif : (−2)⁴ = 16 et ⁴√16 = 2. La règle ⁿ√(yⁿ) = y n'est vraie que pour y ≥ 0.
:::

::: propriete
Soient a, b ≥ 0 et n, p deux entiers supérieurs ou égaux à 2. Pour identifier une racine, on vérifie que le candidat est positif et que sa puissance n vaut le radicande.

- ⁿ√(aⁿᵖ) = aᵖ
- ⁿ√a × ⁿ√b = ⁿ√(ab), car (ⁿ√a × ⁿ√b)ⁿ = ab et ce produit est positif
- ⁿ√(ᵖ√a) = ⁿᵖ√a : les indices se multiplient
- ⁿᵖ√(aᵖ) = ⁿ√a

Cas limite : la somme ne passe pas sous la racine. √(9 + 16) = 5, alors que √9 + √16 = 7.
:::

::: verifie
Écrire plus simplement ⁹√(5³).

---

9 = 3 × 3 et 5³ = aᵖ avec a = 5 et p = 3. La règle ⁿᵖ√(aᵖ) = ⁿ√a, avec n = 3 et p = 3, donne ⁹√(5³) = ³√5. Vérification par la définition : (³√5)⁹ = ((³√5)³)³ = 5³ et ³√5 est positif ✓.
:::

::: retenir
ⁿ√ est la réciproque de x ↦ xⁿ sur ℝ₊ : y = ⁿ√x équivaut à x = yⁿ pour x, y ≥ 0 ; ⁿ√(yⁿ) = y seulement si y ≥ 0 ; les indices se multiplient, la somme ne passe pas sous la racine.
:::

> 🏆 Pont franchi, héros : tu sais dire qu'une courbe ne saute pas, coincer une solution entre deux nombres, et remonter une fonction par sa réciproque. La dérivation t'attend au chapitre suivant.
