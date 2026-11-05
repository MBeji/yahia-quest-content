# ⚔️ Continuité et limites — la clé des valeurs intermédiaires

> 💡 «Une courbe continue ne saute jamais une valeur : pour aller de bas en haut, elle doit croiser chaque hauteur entre les deux.»

Bienvenue, héros de la section Sciences expérimentales. En 1817, Bolzano cherchait une preuve rigoureuse de ce qui semble évident sur un dessin : une courbe d'un seul trait qui passe sous l'axe puis au-dessus le traverse forcément. Ce théorème des valeurs intermédiaires est le sommet de ce chapitre. Huit étapes t'y conduisent : continuité, prolongement, calcul de limites, composées, comparaison, valeurs intermédiaires, solution unique avec dichotomie, puis image d'un intervalle.

## 🧵 Continuité : la courbe d'un seul trait

Une fonction est définie par deux formules : f(x) = 2x − 1 pour x ≤ 1, puis f(x) = x/2 + 1/(2x) pour x > 1.
Les deux morceaux se rejoignent-ils en x = 1, ou y a-t-il un saut ? Dire « sans lever le crayon » ne suffit pas pour calculer : il faut le dire avec des limites.

::: definition
Soit f une fonction définie sur un intervalle ouvert I contenant a. **f est continue en a** lorsque lim x→a f(x) = f(a), c'est-à-dire lorsque trois nombres sont égaux :

$$ lim x→a⁻ f(x) = lim x→a⁺ f(x) = f(a) $$

f est **continue sur un intervalle ouvert I** si elle est continue en tout réel de I. Elle est **continue sur [a ; b]** si elle est continue sur ]a ; b[, à droite en a et à gauche en b.
:::

::: figure Les deux morceaux de la courbe se rejoignent au point (1 ; 1) : pas de saut, la fonction est continue en 1
<svg viewBox="0 0 340 230"><title>Courbe d'une fonction définie par deux formules, qui se raccordent au point d'abscisse 1</title><path d="M30.0 121.5 H326.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M81.4 208.0 V14.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M326.0 121.5 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M81.4 14.0 l-3.5 7 l7 0 z" fill="#0f172a"/><line x1="160.3" y1="118.5" x2="160.3" y2="124.5" stroke="#0f172a" stroke-width="1.4"/><text x="160.3" y="136.5" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="239.2" y1="118.5" x2="239.2" y2="124.5" stroke="#0f172a" stroke-width="1.4"/><text x="239.2" y="136.5" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="318.1" y1="118.5" x2="318.1" y2="124.5" stroke="#0f172a" stroke-width="1.4"/><text x="318.1" y="136.5" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="78.4" y1="193.2" x2="84.4" y2="193.2" stroke="#0f172a" stroke-width="1.4"/><text x="75.4" y="197.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="78.4" y1="85.7" x2="84.4" y2="85.7" stroke="#0f172a" stroke-width="1.4"/><text x="75.4" y="89.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="78.4" y1="49.8" x2="84.4" y2="49.8" stroke="#0f172a" stroke-width="1.4"/><text x="75.4" y="53.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="324.0" y="115.5" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="89.4" y="22.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="160.3" y1="204.0" x2="160.3" y2="85.7" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="34.0" y1="85.7" x2="160.3" y2="85.7" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><path d="M37.9 196.8 L38.5 196.4 L39.0 195.9 L39.5 195.4 L40.0 195.0 L40.5 194.5 L41.0 194.1 L41.5 193.6 L42.0 193.1 L42.5 192.7 L43.0 192.2 L43.6 191.7 L44.1 191.3 L44.6 190.8 L45.1 190.3 L45.6 189.9 L46.1 189.4 L46.6 189.0 L47.1 188.5 L47.6 188.0 L48.1 187.6 L48.6 187.1 L49.2 186.6 L49.7 186.2 L50.2 185.7 L50.7 185.3 L51.2 184.8 L51.7 184.3 L52.2 183.9 L52.7 183.4 L53.2 182.9 L53.7 182.5 L54.3 182.0 L54.8 181.5 L55.3 181.1 L55.8 180.6 L56.3 180.2 L56.8 179.7 L57.3 179.2 L57.8 178.8 L58.3 178.3 L58.8 177.8 L59.4 177.4 L59.9 176.9 L60.4 176.5 L60.9 176.0 L61.4 175.5 L61.9 175.1 L62.4 174.6 L62.9 174.1 L63.4 173.7 L63.9 173.2 L64.4 172.8 L65.0 172.3 L65.5 171.8 L66.0 171.4 L66.5 170.9 L67.0 170.4 L67.5 170.0 L68.0 169.5 L68.5 169.0 L69.0 168.6 L69.5 168.1 L70.1 167.7 L70.6 167.2 L71.1 166.7 L71.6 166.3 L72.1 165.8 L72.6 165.3 L73.1 164.9 L73.6 164.4 L74.1 164.0 L74.6 163.5 L75.2 163.0 L75.7 162.6 L76.2 162.1 L76.7 161.6 L77.2 161.2 L77.7 160.7 L78.2 160.2 L78.7 159.8 L79.2 159.3 L79.7 158.9 L80.2 158.4 L80.8 157.9 L81.3 157.5 L81.8 157.0 L82.3 156.5 L82.8 156.1 L83.3 155.6 L83.8 155.2 L84.3 154.7 L84.8 154.2 L85.3 153.8 L85.9 153.3 L86.4 152.8 L86.9 152.4 L87.4 151.9 L87.9 151.5 L88.4 151.0 L88.9 150.5 L89.4 150.1 L89.9 149.6 L90.4 149.1 L91.0 148.7 L91.5 148.2 L92.0 147.7 L92.5 147.3 L93.0 146.8 L93.5 146.4 L94.0 145.9 L94.5 145.4 L95.0 145.0 L95.5 144.5 L96.0 144.0 L96.6 143.6 L97.1 143.1 L97.6 142.7 L98.1 142.2 L98.6 141.7 L99.1 141.3 L99.6 140.8 L100.1 140.3 L100.6 139.9 L101.1 139.4 L101.7 138.9 L102.2 138.5 L102.7 138.0 L103.2 137.6 L103.7 137.1 L104.2 136.6 L104.7 136.2 L105.2 135.7 L105.7 135.2 L106.2 134.8 L106.8 134.3 L107.3 133.9 L107.8 133.4 L108.3 132.9 L108.8 132.5 L109.3 132.0 L109.8 131.5 L110.3 131.1 L110.8 130.6 L111.3 130.2 L111.9 129.7 L112.4 129.2 L112.9 128.8 L113.4 128.3 L113.9 127.8 L114.4 127.4 L114.9 126.9 L115.4 126.4 L115.9 126.0 L116.4 125.5 L116.9 125.1 L117.5 124.6 L118.0 124.1 L118.5 123.7 L119.0 123.2 L119.5 122.7 L120.0 122.3 L120.5 121.8 L121.0 121.4 L121.5 120.9 L122.0 120.4 L122.6 120.0 L123.1 119.5 L123.6 119.0 L124.1 118.6 L124.6 118.1 L125.1 117.6 L125.6 117.2 L126.1 116.7 L126.6 116.3 L127.1 115.8 L127.7 115.3 L128.2 114.9 L128.7 114.4 L129.2 113.9 L129.7 113.5 L130.2 113.0 L130.7 112.6 L131.2 112.1 L131.7 111.6 L132.2 111.2 L132.7 110.7 L133.3 110.2 L133.8 109.8 L134.3 109.3 L134.8 108.9 L135.3 108.4 L135.8 107.9 L136.3 107.5 L136.8 107.0 L137.3 106.5 L137.8 106.1 L138.4 105.6 L138.9 105.1 L139.4 104.7 L139.9 104.2 L140.4 103.8 L140.9 103.3 L141.4 102.8 L141.9 102.4 L142.4 101.9 L142.9 101.4 L143.5 101.0 L144.0 100.5 L144.5 100.1 L145.0 99.6 L145.5 99.1 L146.0 98.7 L146.5 98.2 L147.0 97.7 L147.5 97.3 L148.0 96.8 L148.5 96.3 L149.1 95.9 L149.6 95.4 L150.1 95.0 L150.6 94.5 L151.1 94.0 L151.6 93.6 L152.1 93.1 L152.6 92.6 L153.1 92.2 L153.6 91.7 L154.2 91.3 L154.7 90.8 L155.2 90.3 L155.7 89.9 L156.2 89.4 L156.7 88.9 L157.2 88.5 L157.7 88.0 L158.2 87.6 L158.7 87.1 L159.3 86.6 L159.8 86.2 L160.3 85.7" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><path d="M160.3 85.7 L160.9 85.7 L161.6 85.7 L162.3 85.7 L163.0 85.7 L163.6 85.7 L164.3 85.7 L165.0 85.6 L165.7 85.6 L166.3 85.6 L167.0 85.6 L167.7 85.6 L168.4 85.5 L169.0 85.5 L169.7 85.5 L170.4 85.4 L171.1 85.4 L171.7 85.4 L172.4 85.3 L173.1 85.3 L173.8 85.3 L174.4 85.2 L175.1 85.2 L175.8 85.1 L176.4 85.1 L177.1 85.0 L177.8 85.0 L178.5 84.9 L179.1 84.9 L179.8 84.8 L180.5 84.8 L181.2 84.7 L181.8 84.6 L182.5 84.6 L183.2 84.5 L183.9 84.5 L184.5 84.4 L185.2 84.3 L185.9 84.3 L186.6 84.2 L187.2 84.1 L187.9 84.1 L188.6 84.0 L189.3 83.9 L189.9 83.9 L190.6 83.8 L191.3 83.7 L192.0 83.6 L192.6 83.6 L193.3 83.5 L194.0 83.4 L194.6 83.3 L195.3 83.2 L196.0 83.2 L196.7 83.1 L197.3 83.0 L198.0 82.9 L198.7 82.8 L199.4 82.8 L200.0 82.7 L200.7 82.6 L201.4 82.5 L202.1 82.4 L202.7 82.3 L203.4 82.2 L204.1 82.1 L204.8 82.1 L205.4 82.0 L206.1 81.9 L206.8 81.8 L207.5 81.7 L208.1 81.6 L208.8 81.5 L209.5 81.4 L210.2 81.3 L210.8 81.2 L211.5 81.1 L212.2 81.0 L212.8 80.9 L213.5 80.8 L214.2 80.7 L214.9 80.6 L215.5 80.5 L216.2 80.4 L216.9 80.3 L217.6 80.2 L218.2 80.1 L218.9 80.0 L219.6 79.9 L220.3 79.8 L220.9 79.7 L221.6 79.6 L222.3 79.5 L223.0 79.4 L223.6 79.3 L224.3 79.2 L225.0 79.1 L225.7 79.0 L226.3 78.9 L227.0 78.8 L227.7 78.6 L228.4 78.5 L229.0 78.4 L229.7 78.3 L230.4 78.2 L231.1 78.1 L231.7 78.0 L232.4 77.9 L233.1 77.8 L233.7 77.7 L234.4 77.5 L235.1 77.4 L235.8 77.3 L236.4 77.2 L237.1 77.1 L237.8 77.0 L238.5 76.9 L239.1 76.7 L239.8 76.6 L240.5 76.5 L241.2 76.4 L241.8 76.3 L242.5 76.2 L243.2 76.0 L243.9 75.9 L244.5 75.8 L245.2 75.7 L245.9 75.6 L246.6 75.5 L247.2 75.3 L247.9 75.2 L248.6 75.1 L249.3 75.0 L249.9 74.9 L250.6 74.7 L251.3 74.6 L251.9 74.5 L252.6 74.4 L253.3 74.3 L254.0 74.1 L254.6 74.0 L255.3 73.9 L256.0 73.8 L256.7 73.7 L257.3 73.5 L258.0 73.4 L258.7 73.3 L259.4 73.2 L260.0 73.0 L260.7 72.9 L261.4 72.8 L262.1 72.7 L262.7 72.6 L263.4 72.4 L264.1 72.3 L264.8 72.2 L265.4 72.1 L266.1 71.9 L266.8 71.8 L267.5 71.7 L268.1 71.6 L268.8 71.4 L269.5 71.3 L270.1 71.2 L270.8 71.0 L271.5 70.9 L272.2 70.8 L272.8 70.7 L273.5 70.5 L274.2 70.4 L274.9 70.3 L275.5 70.2 L276.2 70.0 L276.9 69.9 L277.6 69.8 L278.2 69.6 L278.9 69.5 L279.6 69.4 L280.3 69.3 L280.9 69.1 L281.6 69.0 L282.3 68.9 L283.0 68.7 L283.6 68.6 L284.3 68.5 L285.0 68.4 L285.7 68.2 L286.3 68.1 L287.0 68.0 L287.7 67.8 L288.3 67.7 L289.0 67.6 L289.7 67.4 L290.4 67.3 L291.0 67.2 L291.7 67.0 L292.4 66.9 L293.1 66.8 L293.7 66.6 L294.4 66.5 L295.1 66.4 L295.8 66.3 L296.4 66.1 L297.1 66.0 L297.8 65.9 L298.5 65.7 L299.1 65.6 L299.8 65.5 L300.5 65.3 L301.2 65.2 L301.8 65.1 L302.5 64.9 L303.2 64.8 L303.9 64.7 L304.5 64.5 L305.2 64.4 L305.9 64.3 L306.5 64.1 L307.2 64.0 L307.9 63.8 L308.6 63.7 L309.2 63.6 L309.9 63.4 L310.6 63.3 L311.3 63.2 L311.9 63.0 L312.6 62.9 L313.3 62.8 L314.0 62.6 L314.6 62.5 L315.3 62.4 L316.0 62.2 L316.7 62.1 L317.3 62.0 L318.0 61.8 L318.7 61.7 L319.4 61.5 L320.0 61.4 L320.7 61.3 L321.4 61.1 L322.1 61.0" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="160.3" cy="85.7" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="168.3" y="107.7" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f(1) = 1</text><text x="53.7" y="164.9" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2x − 1</text><text x="255.0" y="59.7" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x/2 + 1/(2x)</text></svg>
:::

Le point plein de la figure est (1 ; f(1)) : il se trouve à l'arrivée des deux morceaux, c'est le troisième nombre de l'égalité.

::: exemple Continuité en 1 de f(x) = 2x − 1 (x ≤ 1) et f(x) = x/2 + 1/(2x) (x > 1)

1. À gauche de 1, f(x) = 2x − 1 est un polynôme, continu en 1 : lim x→1⁻ f(x) = 2 × 1 − 1 = 1.
2. À droite de 1, f(x) = x/2 + 1/(2x) est une fraction rationnelle définie en 1, donc continue en 1 : lim x→1⁺ f(x) = 1/2 + 1/2 = 1.
3. La valeur en 1 vient de la première formule (car x ≤ 1) : f(1) = 2 × 1 − 1 = 1.
4. Les trois nombres sont égaux (1 = 1 = 1) : f est continue en 1.

:::

::: piege Croire que la valeur en a et un seul côté suffisent
Soit h(x) = |x − 3|/(x − 3) pour x ≠ 3, et h(3) = 1. À droite de 3, |x − 3| = x − 3 donc h(x) = 1 = h(3) : on conclut trop vite que h est continue en 3. Cela tente parce que la courbe colle à la valeur de ce côté. Mais à gauche, |x − 3| = −(x − 3) donc h(x) = −1 ≠ h(3) : h est continue à droite, pas à gauche, donc pas continue en 3. Il faut vérifier les deux côtés.
:::

::: propriete
- Un polynôme est continu en tout réel ; une fraction rationnelle est continue en tout réel où elle est définie ; cos et sin sont continues sur ℝ.
- Si f et g sont continues en a, alors f + g, f × g et αf (α réel) sont continues en a ; |f| et fⁿ (n ≥ 1) le sont aussi ; 1/f l'est si f(a) ≠ 0 ; f/g l'est si g(a) ≠ 0.
- Si f est positive sur I et continue en a, alors √f est continue en a.

Cas limite : x ↦ 1/x est continue en tout réel non nul, mais n'est pas définie en 0 : la condition f(a) ≠ 0 ou g(a) ≠ 0 est indispensable. Ainsi x ↦ |x² − 3x| + √(x² + 1) est continue sur ℝ : valeur absolue d'un polynôme, plus racine d'un polynôme positif.
:::

::: verifie
Soit f(x) = x + 3 pour x ≤ 1 et f(x) = (x² + 7)/2 pour x > 1. Cette fonction est-elle continue en 1 ?

---

À gauche, lim x→1⁻ (x + 3) = 4 (polynôme). À droite, lim x→1⁺ (x² + 7)/2 = (1 + 7)/2 = 4 (fraction rationnelle définie en 1). Et f(1) = 1 + 3 = 4 car x ≤ 1. Les trois nombres valent 4 : f est continue en 1. On a bien contrôlé les deux côtés et la valeur en 1.
:::

::: retenir
f est continue en a quand limite à gauche, limite à droite et f(a) sont égales ; polynômes, fractions rationnelles (où elles sont définies), sin et cos, et leurs combinaisons, le sont automatiquement.
:::

## 🕳️ Prolongement par continuité : boucher un trou

Un logiciel trace la courbe de f(x) = x + (sin 2x)/x et laisse un trou en x = 0, car le quotient y demande de diviser 0 par 0.
La courbe a-t-elle vraiment un trou, ou peut-on lui donner en 0 la valeur qui la recolle ?

::: definition
Soit f définie sur un intervalle ouvert I sauf en un réel a de I. Si lim x→a f(x) = ℓ avec ℓ **réel**, la fonction g définie sur I par g(x) = f(x) pour x ≠ a et g(a) = ℓ est continue en a : c'est le **prolongement par continuité** de f en a.
:::

::: figure À gauche la courbe de f a un trou en 0 ; à droite la courbe de g est la même avec le point (0 ; 2) rempli, donc continue
<svg viewBox="0 0 380 230"><title>À gauche, la courbe de f a un trou au point d'abscisse 0 et d'ordonnée 2 ; à droite, la courbe de g est la même courbe avec ce point rempli</title><g><path d="M22.0 117.6 H182.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M104.0 208.0 V14.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M182.0 117.6 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M104.0 14.0 l-3.5 7 l7 0 z" fill="#0f172a"/><line x1="48.3" y1="114.6" x2="48.3" y2="120.6" stroke="#0f172a" stroke-width="1.4"/><text x="48.3" y="132.6" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−3</text><line x1="159.7" y1="114.6" x2="159.7" y2="120.6" stroke="#0f172a" stroke-width="1.4"/><text x="159.7" y="132.6" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="101.0" y1="83.1" x2="107.0" y2="83.1" stroke="#0f172a" stroke-width="1.4"/><text x="98.0" y="87.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="180.0" y="111.6" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="112.0" y="22.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="26.0" y1="83.1" x2="104.0" y2="83.1" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><path d="M27.9 184.5 L28.2 184.1 L28.6 183.6 L29.0 183.2 L29.4 182.8 L29.8 182.4 L30.1 182.0 L30.5 181.6 L30.9 181.2 L31.3 180.9 L31.6 180.5 L32.0 180.1 L32.4 179.8 L32.8 179.4 L33.2 179.1 L33.5 178.8 L33.9 178.5 L34.3 178.1 L34.7 177.8 L35.1 177.5 L35.4 177.2 L35.8 177.0 L36.2 176.7 L36.6 176.4 L36.9 176.1 L37.3 175.9 L37.7 175.6 L38.1 175.4 L38.5 175.2 L38.8 174.9 L39.2 174.7 L39.6 174.5 L40.0 174.3 L40.4 174.1 L40.7 173.9 L41.1 173.7 L41.5 173.5 L41.9 173.4 L42.3 173.2 L42.6 173.0 L43.0 172.9 L43.4 172.7 L43.8 172.6 L44.1 172.4 L44.5 172.3 L44.9 172.2 L45.3 172.0 L45.7 171.9 L46.0 171.8 L46.4 171.6 L46.8 171.5 L47.2 171.4 L47.6 171.3 L47.9 171.2 L48.3 171.1 L48.7 170.9 L49.1 170.8 L49.5 170.7 L49.8 170.6 L50.2 170.5 L50.6 170.4 L51.0 170.2 L51.3 170.1 L51.7 170.0 L52.1 169.9 L52.5 169.7 L52.9 169.6 L53.2 169.5 L53.6 169.3 L54.0 169.2 L54.4 169.0 L54.8 168.8 L55.1 168.7 L55.5 168.5 L55.9 168.3 L56.3 168.1 L56.7 167.9 L57.0 167.7 L57.4 167.5 L57.8 167.3 L58.2 167.1 L58.5 166.9 L58.9 166.6 L59.3 166.3 L59.7 166.1 L60.1 165.8 L60.4 165.5 L60.8 165.2 L61.2 164.9 L61.6 164.6 L62.0 164.2 L62.3 163.9 L62.7 163.5 L63.1 163.2 L63.5 162.8 L63.8 162.4 L64.2 162.0 L64.6 161.5 L65.0 161.1 L65.4 160.6 L65.7 160.2 L66.1 159.7 L66.5 159.2 L66.9 158.7 L67.3 158.2 L67.6 157.6 L68.0 157.1 L68.4 156.5 L68.8 155.9 L69.2 155.3 L69.5 154.7 L69.9 154.1 L70.3 153.5 L70.7 152.8 L71.0 152.1 L71.4 151.5 L71.8 150.8 L72.2 150.1 L72.6 149.3 L72.9 148.6 L73.3 147.9 L73.7 147.1 L74.1 146.3 L74.5 145.5 L74.8 144.8 L75.2 143.9 L75.6 143.1 L76.0 142.3 L76.4 141.5 L76.7 140.6 L77.1 139.7 L77.5 138.9 L77.9 138.0 L78.2 137.1 L78.6 136.2 L79.0 135.3 L79.4 134.4 L79.8 133.5 L80.1 132.6 L80.5 131.6 L80.9 130.7 L81.3 129.7 L81.7 128.8 L82.0 127.8 L82.4 126.9 L82.8 125.9 L83.2 125.0 L83.5 124.0 L83.9 123.0 L84.3 122.1 L84.7 121.1 L85.1 120.1 L85.4 119.2 L85.8 118.2 L86.2 117.2 L86.6 116.3 L87.0 115.3 L87.3 114.4 L87.7 113.4 L88.1 112.5 L88.5 111.5 L88.9 110.6 L89.2 109.7 L89.6 108.7 L90.0 107.8 L90.4 106.9 L90.7 106.0 L91.1 105.1 L91.5 104.2 L91.9 103.4 L92.3 102.5 L92.6 101.6 L93.0 100.8 L93.4 100.0 L93.8 99.2 L94.2 98.4 L94.5 97.6 L94.9 96.8 L95.3 96.0 L95.7 95.3 L96.1 94.6 L96.4 93.8 L96.8 93.1 L97.2 92.4 L97.6 91.8 L97.9 91.1 L98.3 90.5 L98.7 89.9 L99.1 89.3 L99.5 88.7 L99.8 88.1 L100.2 87.6 L100.6 87.0 L101.0 86.5 L101.4 86.0 L101.7 85.5 L102.1 85.1 L102.5 84.6 L102.9 84.2 L103.2 83.8 L103.6 83.4" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><path d="M104.4 82.8 L104.8 82.4 L105.1 82.1 L105.5 81.8 L105.9 81.6 L106.3 81.3 L106.6 81.1 L107.0 80.9 L107.4 80.7 L107.8 80.5 L108.2 80.4 L108.5 80.2 L108.9 80.1 L109.3 80.0 L109.7 79.9 L110.1 79.9 L110.4 79.8 L110.8 79.8 L111.2 79.8 L111.6 79.8 L111.9 79.8 L112.3 79.8 L112.7 79.8 L113.1 79.9 L113.5 80.0 L113.8 80.1 L114.2 80.2 L114.6 80.3 L115.0 80.4 L115.4 80.5 L115.7 80.7 L116.1 80.8 L116.5 81.0 L116.9 81.2 L117.3 81.4 L117.6 81.6 L118.0 81.8 L118.4 82.0 L118.8 82.2 L119.1 82.4 L119.5 82.6 L119.9 82.9 L120.3 83.1 L120.7 83.4 L121.0 83.6 L121.4 83.9 L121.8 84.1 L122.2 84.4 L122.6 84.6 L122.9 84.9 L123.3 85.2 L123.7 85.4 L124.1 85.7 L124.5 86.0 L124.8 86.2 L125.2 86.5 L125.6 86.7 L126.0 87.0 L126.3 87.2 L126.7 87.5 L127.1 87.7 L127.5 87.9 L127.9 88.2 L128.2 88.4 L128.6 88.6 L129.0 88.8 L129.4 89.0 L129.8 89.2 L130.1 89.4 L130.5 89.6 L130.9 89.7 L131.3 89.9 L131.6 90.0 L132.0 90.2 L132.4 90.3 L132.8 90.4 L133.2 90.5 L133.5 90.6 L133.9 90.7 L134.3 90.7 L134.7 90.8 L135.1 90.8 L135.4 90.9 L135.8 90.9 L136.2 90.9 L136.6 90.9 L137.0 90.8 L137.3 90.8 L137.7 90.8 L138.1 90.7 L138.5 90.6 L138.8 90.5 L139.2 90.4 L139.6 90.3 L140.0 90.1 L140.4 90.0 L140.7 89.8 L141.1 89.6 L141.5 89.4 L141.9 89.2 L142.3 89.0 L142.6 88.8 L143.0 88.5 L143.4 88.3 L143.8 88.0 L144.2 87.7 L144.5 87.4 L144.9 87.1 L145.3 86.7 L145.7 86.4 L146.0 86.0 L146.4 85.7 L146.8 85.3 L147.2 84.9 L147.6 84.5 L147.9 84.1 L148.3 83.6 L148.7 83.2 L149.1 82.8 L149.5 82.3 L149.8 81.8 L150.2 81.4 L150.6 80.9 L151.0 80.4 L151.3 79.9 L151.7 79.4 L152.1 78.8 L152.5 78.3 L152.9 77.8 L153.2 77.2 L153.6 76.7 L154.0 76.2 L154.4 75.6 L154.8 75.0 L155.1 74.5 L155.5 73.9 L155.9 73.3 L156.3 72.7 L156.7 72.2 L157.0 71.6 L157.4 71.0 L157.8 70.4 L158.2 69.8 L158.5 69.2 L158.9 68.7 L159.3 68.1 L159.7 67.5 L160.1 66.9 L160.4 66.3 L160.8 65.7 L161.2 65.1 L161.6 64.5 L162.0 64.0 L162.3 63.4 L162.7 62.8 L163.1 62.2 L163.5 61.7 L163.9 61.1 L164.2 60.5 L164.6 60.0 L165.0 59.4 L165.4 58.9 L165.7 58.3 L166.1 57.8 L166.5 57.3 L166.9 56.8 L167.3 56.2 L167.6 55.7 L168.0 55.2 L168.4 54.7 L168.8 54.2 L169.2 53.7 L169.5 53.3 L169.9 52.8 L170.3 52.3 L170.7 51.9 L171.1 51.4 L171.4 51.0 L171.8 50.5 L172.2 50.1 L172.6 49.7 L172.9 49.3 L173.3 48.9 L173.7 48.5 L174.1 48.1 L174.5 47.7 L174.8 47.3 L175.2 47.0 L175.6 46.6 L176.0 46.3 L176.4 45.9 L176.7 45.6 L177.1 45.3 L177.5 44.9 L177.9 44.6 L178.2 44.3 L178.6 44.0 L179.0 43.7 L179.4 43.4 L179.8 43.1 L180.1 42.9" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="104.0" cy="83.1" r="4" fill="#ffffff" stroke="#0f6e56" stroke-width="2.3"/><text x="141.1" y="20.9" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f</text></g><g transform="translate(190,0)"><path d="M22.0 117.6 H182.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M104.0 208.0 V14.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M182.0 117.6 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M104.0 14.0 l-3.5 7 l7 0 z" fill="#0f172a"/><line x1="48.3" y1="114.6" x2="48.3" y2="120.6" stroke="#0f172a" stroke-width="1.4"/><text x="48.3" y="132.6" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−3</text><line x1="159.7" y1="114.6" x2="159.7" y2="120.6" stroke="#0f172a" stroke-width="1.4"/><text x="159.7" y="132.6" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="101.0" y1="83.1" x2="107.0" y2="83.1" stroke="#0f172a" stroke-width="1.4"/><text x="98.0" y="87.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="180.0" y="111.6" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="112.0" y="22.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="26.0" y1="83.1" x2="104.0" y2="83.1" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><path d="M27.9 184.5 L28.2 184.1 L28.6 183.6 L29.0 183.2 L29.4 182.8 L29.8 182.4 L30.1 182.0 L30.5 181.6 L30.9 181.2 L31.3 180.9 L31.6 180.5 L32.0 180.1 L32.4 179.8 L32.8 179.4 L33.2 179.1 L33.5 178.8 L33.9 178.5 L34.3 178.1 L34.7 177.8 L35.1 177.5 L35.4 177.2 L35.8 177.0 L36.2 176.7 L36.6 176.4 L36.9 176.1 L37.3 175.9 L37.7 175.6 L38.1 175.4 L38.5 175.2 L38.8 174.9 L39.2 174.7 L39.6 174.5 L40.0 174.3 L40.4 174.1 L40.7 173.9 L41.1 173.7 L41.5 173.5 L41.9 173.4 L42.3 173.2 L42.6 173.0 L43.0 172.9 L43.4 172.7 L43.8 172.6 L44.1 172.4 L44.5 172.3 L44.9 172.2 L45.3 172.0 L45.7 171.9 L46.0 171.8 L46.4 171.6 L46.8 171.5 L47.2 171.4 L47.6 171.3 L47.9 171.2 L48.3 171.1 L48.7 170.9 L49.1 170.8 L49.5 170.7 L49.8 170.6 L50.2 170.5 L50.6 170.4 L51.0 170.2 L51.3 170.1 L51.7 170.0 L52.1 169.9 L52.5 169.7 L52.9 169.6 L53.2 169.5 L53.6 169.3 L54.0 169.2 L54.4 169.0 L54.8 168.8 L55.1 168.7 L55.5 168.5 L55.9 168.3 L56.3 168.1 L56.7 167.9 L57.0 167.7 L57.4 167.5 L57.8 167.3 L58.2 167.1 L58.5 166.9 L58.9 166.6 L59.3 166.3 L59.7 166.1 L60.1 165.8 L60.4 165.5 L60.8 165.2 L61.2 164.9 L61.6 164.6 L62.0 164.2 L62.3 163.9 L62.7 163.5 L63.1 163.2 L63.5 162.8 L63.8 162.4 L64.2 162.0 L64.6 161.5 L65.0 161.1 L65.4 160.6 L65.7 160.2 L66.1 159.7 L66.5 159.2 L66.9 158.7 L67.3 158.2 L67.6 157.6 L68.0 157.1 L68.4 156.5 L68.8 155.9 L69.2 155.3 L69.5 154.7 L69.9 154.1 L70.3 153.5 L70.7 152.8 L71.0 152.1 L71.4 151.5 L71.8 150.8 L72.2 150.1 L72.6 149.3 L72.9 148.6 L73.3 147.9 L73.7 147.1 L74.1 146.3 L74.5 145.5 L74.8 144.8 L75.2 143.9 L75.6 143.1 L76.0 142.3 L76.4 141.5 L76.7 140.6 L77.1 139.7 L77.5 138.9 L77.9 138.0 L78.2 137.1 L78.6 136.2 L79.0 135.3 L79.4 134.4 L79.8 133.5 L80.1 132.6 L80.5 131.6 L80.9 130.7 L81.3 129.7 L81.7 128.8 L82.0 127.8 L82.4 126.9 L82.8 125.9 L83.2 125.0 L83.5 124.0 L83.9 123.0 L84.3 122.1 L84.7 121.1 L85.1 120.1 L85.4 119.2 L85.8 118.2 L86.2 117.2 L86.6 116.3 L87.0 115.3 L87.3 114.4 L87.7 113.4 L88.1 112.5 L88.5 111.5 L88.9 110.6 L89.2 109.7 L89.6 108.7 L90.0 107.8 L90.4 106.9 L90.7 106.0 L91.1 105.1 L91.5 104.2 L91.9 103.4 L92.3 102.5 L92.6 101.6 L93.0 100.8 L93.4 100.0 L93.8 99.2 L94.2 98.4 L94.5 97.6 L94.9 96.8 L95.3 96.0 L95.7 95.3 L96.1 94.6 L96.4 93.8 L96.8 93.1 L97.2 92.4 L97.6 91.8 L97.9 91.1 L98.3 90.5 L98.7 89.9 L99.1 89.3 L99.5 88.7 L99.8 88.1 L100.2 87.6 L100.6 87.0 L101.0 86.5 L101.4 86.0 L101.7 85.5 L102.1 85.1 L102.5 84.6 L102.9 84.2 L103.2 83.8 L103.6 83.4" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><path d="M104.4 82.8 L104.8 82.4 L105.1 82.1 L105.5 81.8 L105.9 81.6 L106.3 81.3 L106.6 81.1 L107.0 80.9 L107.4 80.7 L107.8 80.5 L108.2 80.4 L108.5 80.2 L108.9 80.1 L109.3 80.0 L109.7 79.9 L110.1 79.9 L110.4 79.8 L110.8 79.8 L111.2 79.8 L111.6 79.8 L111.9 79.8 L112.3 79.8 L112.7 79.8 L113.1 79.9 L113.5 80.0 L113.8 80.1 L114.2 80.2 L114.6 80.3 L115.0 80.4 L115.4 80.5 L115.7 80.7 L116.1 80.8 L116.5 81.0 L116.9 81.2 L117.3 81.4 L117.6 81.6 L118.0 81.8 L118.4 82.0 L118.8 82.2 L119.1 82.4 L119.5 82.6 L119.9 82.9 L120.3 83.1 L120.7 83.4 L121.0 83.6 L121.4 83.9 L121.8 84.1 L122.2 84.4 L122.6 84.6 L122.9 84.9 L123.3 85.2 L123.7 85.4 L124.1 85.7 L124.5 86.0 L124.8 86.2 L125.2 86.5 L125.6 86.7 L126.0 87.0 L126.3 87.2 L126.7 87.5 L127.1 87.7 L127.5 87.9 L127.9 88.2 L128.2 88.4 L128.6 88.6 L129.0 88.8 L129.4 89.0 L129.8 89.2 L130.1 89.4 L130.5 89.6 L130.9 89.7 L131.3 89.9 L131.6 90.0 L132.0 90.2 L132.4 90.3 L132.8 90.4 L133.2 90.5 L133.5 90.6 L133.9 90.7 L134.3 90.7 L134.7 90.8 L135.1 90.8 L135.4 90.9 L135.8 90.9 L136.2 90.9 L136.6 90.9 L137.0 90.8 L137.3 90.8 L137.7 90.8 L138.1 90.7 L138.5 90.6 L138.8 90.5 L139.2 90.4 L139.6 90.3 L140.0 90.1 L140.4 90.0 L140.7 89.8 L141.1 89.6 L141.5 89.4 L141.9 89.2 L142.3 89.0 L142.6 88.8 L143.0 88.5 L143.4 88.3 L143.8 88.0 L144.2 87.7 L144.5 87.4 L144.9 87.1 L145.3 86.7 L145.7 86.4 L146.0 86.0 L146.4 85.7 L146.8 85.3 L147.2 84.9 L147.6 84.5 L147.9 84.1 L148.3 83.6 L148.7 83.2 L149.1 82.8 L149.5 82.3 L149.8 81.8 L150.2 81.4 L150.6 80.9 L151.0 80.4 L151.3 79.9 L151.7 79.4 L152.1 78.8 L152.5 78.3 L152.9 77.8 L153.2 77.2 L153.6 76.7 L154.0 76.2 L154.4 75.6 L154.8 75.0 L155.1 74.5 L155.5 73.9 L155.9 73.3 L156.3 72.7 L156.7 72.2 L157.0 71.6 L157.4 71.0 L157.8 70.4 L158.2 69.8 L158.5 69.2 L158.9 68.7 L159.3 68.1 L159.7 67.5 L160.1 66.9 L160.4 66.3 L160.8 65.7 L161.2 65.1 L161.6 64.5 L162.0 64.0 L162.3 63.4 L162.7 62.8 L163.1 62.2 L163.5 61.7 L163.9 61.1 L164.2 60.5 L164.6 60.0 L165.0 59.4 L165.4 58.9 L165.7 58.3 L166.1 57.8 L166.5 57.3 L166.9 56.8 L167.3 56.2 L167.6 55.7 L168.0 55.2 L168.4 54.7 L168.8 54.2 L169.2 53.7 L169.5 53.3 L169.9 52.8 L170.3 52.3 L170.7 51.9 L171.1 51.4 L171.4 51.0 L171.8 50.5 L172.2 50.1 L172.6 49.7 L172.9 49.3 L173.3 48.9 L173.7 48.5 L174.1 48.1 L174.5 47.7 L174.8 47.3 L175.2 47.0 L175.6 46.6 L176.0 46.3 L176.4 45.9 L176.7 45.6 L177.1 45.3 L177.5 44.9 L177.9 44.6 L178.2 44.3 L178.6 44.0 L179.0 43.7 L179.4 43.4 L179.8 43.1 L180.1 42.9" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="104.0" cy="83.1" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="141.1" y="20.9" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">g</text></g></svg>
:::

Le point rempli à droite est g(0) : son ordonnée est la limite de f en 0 que l'exemple va calculer.

::: exemple Prolonger f(x) = x + (sin 2x)/x en 0

1. f est définie sur ℝ privé de 0, et en 0 le quotient sin 2x / x donne 0/0 : il faut transformer avant de conclure.
2. (sin 2x)/x = 2 × (sin 2x)/(2x) — on fait apparaître sin t / t avec t = 2x.
3. Quand x → 0, t = 2x → 0, et on rappelle que lim t→0 (sin t)/t = 1 : donc (sin 2x)/(2x) → 1 (limite d'une composée).
4. lim x→0 f(x) = 0 + 2 × 1 = 2 : la limite est un réel, le prolongement existe.
5. La fonction g définie par g(x) = f(x) si x ≠ 0 et g(0) = 2 est continue en 0.

:::

::: piege Recopier lim sin t / t = 1 sans ajuster l'argument
On écrit « (sin 2x)/x → 1 parce que sin x / x → 1 », et on prolonge avec g(0) = 0 + 1 = 1. Cela tente parce que la formule ressemble à celle du rappel. Mais la limite 1 vaut pour (sin t)/t, avec **le même t en haut et en bas**. Ici le bas est x, non 2x : (sin 2x)/x = 2 × (sin 2x)/(2x) → 2, donc g(0) = 2 et non 1.
:::

::: propriete
f, définie sur I sauf en a, se prolonge par continuité en a si et seulement si lim x→a f(x) existe et est un **réel**. Dans ce cas la valeur du prolongement est cette limite. Pour calculer la limite, on cherche une fonction continue en a qui égale f pour x ≠ a.

Cas limite : si la limite est infinie ou n'existe pas, il n'y a pas de prolongement. x ↦ 1/x² tend vers +∞ en 0, et x ↦ |x|/x vaut −1 à gauche de 0 et 1 à droite : aucune ne se prolonge.
:::

::: verifie
Soit h(x) = (sin 3x)/(2x) pour x ≠ 0. Se prolonge-t-elle par continuité en 0, et avec quelle valeur ?

---

(sin 3x)/(2x) = (3/2) × (sin 3x)/(3x) : on a fait apparaître sin t / t avec t = 3x, qui tend vers 0. Donc lim x→0 h(x) = (3/2) × 1 = 3/2, un réel : on pose h(0) = 3/2. Se contenter de « sin x / x → 1 » aurait donné 1 au lieu de 3/2.
:::

::: retenir
Un trou se bouche quand la limite en a est un réel ℓ : on pose alors g(a) = ℓ ; avec un sinus, on ajuste l'argument pour retrouver (sin t)/t → 1.
:::

## ♾️ Opérations sur les limites et formes indéterminées

On te demande lim x→+∞ (√x − x). Ici √x tend vers +∞ et x aussi : deux géants s'affrontent, l'un retranché de l'autre.
Les règles de calcul suffisent-elles, ou faut-il ruser ?

::: propriete
Dans les tableaux, L et L′ sont des réels ; l'infini obtenu suit la règle des signes.

| lim f | lim g | lim (f + g) | lim (f × g) |
| --- | --- | --- | --- |
| L | L′ | L + L′ | L × L′ |
| L | +∞ ou −∞ | l'infini de g | l'infini de g selon le signe de L (L ≠ 0) |
| +∞ | +∞ | +∞ | +∞ |
| −∞ | −∞ | −∞ | +∞ |
| +∞ | −∞ | **indéterminée** | −∞ |

Pour un quotient f/g : L/L′ si L′ ≠ 0 ; L/(±∞) = 0 ; L/0 avec L ≠ 0 donne un infini dont le signe suit la règle des signes. Pour √f : √L si L ≥ 0 et +∞ si f tend vers +∞.

Les **quatre formes indéterminées** sont (+∞) + (−∞), 0 × ∞, ∞/∞ et 0/0 : les tableaux ne concluent pas, on transforme l'écriture. À l'infini, un **polynôme** a la limite de son terme de plus haut degré, une **fraction rationnelle** celle du quotient des termes de plus haut degré.
:::

::: exemple Limite en +∞ de √x − x
1. √x → +∞ et x → +∞ : c'est la forme (+∞) − (+∞), indéterminée — les tableaux ne servent pas.
2. Pour x > 0, √x = x × (1/√x) : on met le terme dominant x en facteur.
3. √x − x = x × (1/√x − 1) — la différence est devenue un produit.
4. 1/√x → 0, donc 1/√x − 1 → −1 ; et x → +∞.
5. (+∞) × (−1) = −∞ (règle des signes) : lim x→+∞ (√x − x) = −∞.

:::

::: exemple Limite en 1 de (x³ − 3x² + 2x)/(x² − 1)
1. En x = 1, numérateur et dénominateur valent 0 : forme 0/0, indéterminée.
2. x³ − 3x² + 2x = x(x − 1)(x − 2) et x² − 1 = (x − 1)(x + 1) — on fait apparaître le facteur commun x − 1.
3. Pour x ≠ 1, le quotient vaut x(x − 2)/(x + 1) — on simplifie car x − 1 ≠ 0.
4. Cette fraction est continue en 1 : la limite vaut 1 × (−1)/2 = −1/2.

:::

::: piege Écrire (+∞) − (+∞) = 0
On note « √x − x = (+∞) − (+∞) = 0 ». Cela tente parce que deux quantités « identiques » semblent se compenser. Mais ces deux infinis ne grandissent pas à la même vitesse : x écrase √x, et la limite est −∞. Une forme indéterminée n'a pas de valeur imposée : on transforme, puis on conclut.
:::

::: methode Lever une forme indéterminée
1. Repérer la forme (∞ − ∞, 0 × ∞, ∞/∞ ou 0/0) avant de calculer.
2. Choisir l'outil : terme de plus haut degré (polynôme, fraction rationnelle à l'infini) ; mise en facteur du terme dominant ; factorisation puis simplification (0/0 en un réel) ; expression conjuguée (différence de racines).
3. Récrire, puis appliquer les tableaux.

Limite infinie en un réel : on étudie le signe. Par exemple lim x→3 (3/(x − 3)² − 2) = +∞, car (x − 3)² > 0 tend vers 0 par valeurs positives, quel que soit le côté.

Par exemple, pour x > 0, √(x² + 4x) − x = (x² + 4x − x²)/(√(x² + 4x) + x) = 4x/(√(x² + 4x) + x) = 4/(√(1 + 4/x) + 1) → 2 : on multiplie et on divise par l'expression conjuguée.
:::

::: verifie
Calcule lim x→+∞ (x − √x).

---

C'est (+∞) − (+∞), forme indéterminée. Pour x > 0, x − √x = x × (1 − 1/√x), et 1 − 1/√x → 1 tandis que x → +∞ : le produit tend vers +∞. Ici x domine √x ; c'est le signe inverse de l'exemple où −x l'emportait.
:::

::: retenir
Les tableaux d'opérations concluent sauf pour (+∞) + (−∞), 0 × ∞, ∞/∞ et 0/0 ; dans ces cas on factorise, on simplifie ou on utilise le terme dominant avant de conclure.
:::

## 🔗 Composée de deux fonctions

Deux machines se suivent : la première calcule u(x) = 1/x², la seconde v(y) = cos y − y.
On cherche ce que devient f(x) = cos(1/x²) − 1/x² quand x devient très grand : l'entrée de la seconde machine s'approche de 0. La sortie s'approche-t-elle alors de v(0) ?

::: definition
Soit u définie sur I et v définie sur J, avec u(I) ⊂ J. La **fonction composée** v∘u est définie sur I par v∘u(x) = v(u(x)) : on applique d'abord u, puis v.
:::

| x | 1/x² | cos(1/x²) − 1/x² |
| --- | --- | --- |
| 10 | 0,01 | 0,98995 |
| 100 | 0,0001 | 0,9999 |
| 1000 | 0,000001 | 0,999999 |

La colonne du milieu est u(x), qui tend vers 0 ; la dernière est v(u(x)), qui tend vers 1 = cos 0 − 0 = v(0).

::: exemple Limite en +∞ de f(x) = cos(1/x²) − 1/x²
1. On pose u(x) = 1/x² et v(y) = cos y − y : f(x) = v(u(x)).
2. lim x→+∞ u(x) = 0 — l'inverse d'un carré qui grandit tend vers 0.
3. v est continue en 0 (somme de cos et d'un polynôme) : lim y→0 v(y) = v(0) = cos 0 − 0 = 1.
4. Théorème de la limite d'une composée : lim x→+∞ f(x) = 1.

:::

::: piege Composer dans le mauvais ordre
Pour f(x) = cos(πx + 1), on prend u = cos et v(y) = πy + 1. Cela tente parce que « cos » est le mot qu'on lit en premier. Mais on calcule d'abord ce qui est à l'intérieur : u(x) = πx + 1, puis v = cos. À x = 0, f(0) = cos 1 ≈ 0,54, alors que le mauvais ordre donnerait π cos 0 + 1 = π + 1 ≈ 4,14.
:::

::: propriete
- **Continuité** (admise). Si u est continue en a et v continue en u(a), alors v∘u est continue en a. Conséquence : la composée de deux fonctions continues est continue. Ainsi x ↦ sin(x² + π/4) est continue sur ℝ.
- **Limite** (admise). Si lim x→a u(x) = b et lim y→b v(y) = c, alors lim x→a v(u(x)) = c, où a, b, c sont des réels ou ±∞.

Cas limite : b peut être infini. Avec u(x) = x² → +∞ quand x → +∞ et v = √ → +∞, on obtient lim x→+∞ √(x²) = +∞. Si u(x) approche b par valeurs supérieures à b, on utilise la limite de v à droite de b ; par valeurs inférieures, la limite à gauche. Par exemple u(x) = 1 + 1/x tend vers 1 en restant > 1 quand x → +∞, donc lim v(u(x)) = lim y→1⁺ v(y).
:::

::: verifie
Calcule lim x→+∞ (sin(3/x²) + 2/x²).

---

On pose u(x) = 1/x² → 0 et v(y) = sin(3y) + 2y, continue en 0 : f(x) = v(u(x)). Donc lim f = v(0) = sin 0 + 0 = 0. On a identifié la fonction intérieure u (son entrée tend vers 0) avant d'appliquer la continuité de v.
:::

::: retenir
Pour une composée v(u(x)), on cherche d'abord la limite b de l'intérieur u, puis la limite de v en b : lim v(u(x)) = lim y→b v(y).
:::

## 🛡️ Limites et ordre : coincer une fonction

La fonction f(x) = (cos²x + 1)/x oscille sans fin : cos²x n'a pas de limite en +∞, donc on ne peut pas appliquer le tableau des quotients. Pourtant la courbe semble s'écraser sur l'axe des abscisses. Comment le prouver sans calculer la limite du numérateur ?

::: figure La courbe de (cos²x + 1)/x ondule mais reste entre les courbes de 1/x et de 2/x, qui tendent toutes deux vers 0
<svg viewBox="0 0 340 230"><title>Courbe de (cos²x + 1)/x entre les courbes de 1/x et de 2/x</title><path d="M30.0 187.7 H326.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M34.0 208.0 V14.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M326.0 187.7 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M34.0 14.0 l-3.5 7 l7 0 z" fill="#0f172a"/><line x1="94.8" y1="184.7" x2="94.8" y2="190.7" stroke="#0f172a" stroke-width="1.4"/><text x="94.8" y="202.7" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="167.8" y1="184.7" x2="167.8" y2="190.7" stroke="#0f172a" stroke-width="1.4"/><text x="167.8" y="202.7" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="240.8" y1="184.7" x2="240.8" y2="190.7" stroke="#0f172a" stroke-width="1.4"/><text x="240.8" y="202.7" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">9</text><line x1="313.8" y1="184.7" x2="313.8" y2="190.7" stroke="#0f172a" stroke-width="1.4"/><text x="313.8" y="202.7" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12</text><line x1="31.0" y1="133.4" x2="37.0" y2="133.4" stroke="#0f172a" stroke-width="1.4"/><text x="28.0" y="137.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="31.0" y1="79.1" x2="37.0" y2="79.1" stroke="#0f172a" stroke-width="1.4"/><text x="28.0" y="83.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="31.0" y1="24.9" x2="37.0" y2="24.9" stroke="#0f172a" stroke-width="1.4"/><text x="28.0" y="28.9" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><text x="324.0" y="181.7" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="42.0" y="22.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><path d="M37.6 20.4 L38.8 32.1 L40.0 42.2 L41.2 51.1 L42.4 59.0 L43.6 66.1 L44.7 72.4 L45.9 78.0 L47.1 83.2 L48.3 87.9 L49.5 92.2 L50.7 96.1 L51.9 99.7 L53.0 103.1 L54.2 106.2 L55.4 109.0 L56.6 111.7 L57.8 114.2 L59.0 116.6 L60.2 118.8 L61.3 120.8 L62.5 122.8 L63.7 124.6 L64.9 126.4 L66.1 128.0 L67.3 129.6 L68.5 131.1 L69.6 132.5 L70.8 133.8 L72.0 135.1 L73.2 136.3 L74.4 137.4 L75.6 138.6 L76.8 139.6 L78.0 140.6 L79.1 141.6 L80.3 142.5 L81.5 143.4 L82.7 144.3 L83.9 145.1 L85.1 145.9 L86.3 146.7 L87.4 147.4 L88.6 148.2 L89.8 148.9 L91.0 149.5 L92.2 150.2 L93.4 150.8 L94.6 151.4 L95.7 152.0 L96.9 152.5 L98.1 153.1 L99.3 153.6 L100.5 154.1 L101.7 154.6 L102.9 155.1 L104.0 155.6 L105.2 156.0 L106.4 156.5 L107.6 156.9 L108.8 157.3 L110.0 157.7 L111.2 158.1 L112.4 158.5 L113.5 158.9 L114.7 159.3 L115.9 159.6 L117.1 160.0 L118.3 160.3 L119.5 160.7 L120.7 161.0 L121.8 161.3 L123.0 161.6 L124.2 161.9 L125.4 162.2 L126.6 162.5 L127.8 162.8 L129.0 163.1 L130.1 163.3 L131.3 163.6 L132.5 163.8 L133.7 164.1 L134.9 164.3 L136.1 164.6 L137.3 164.8 L138.5 165.1 L139.6 165.3 L140.8 165.5 L142.0 165.7 L143.2 165.9 L144.4 166.2 L145.6 166.4 L146.8 166.6 L147.9 166.8 L149.1 167.0 L150.3 167.2 L151.5 167.3 L152.7 167.5 L153.9 167.7 L155.1 167.9 L156.2 168.1 L157.4 168.2 L158.6 168.4 L159.8 168.6 L161.0 168.7 L162.2 168.9 L163.4 169.0 L164.5 169.2 L165.7 169.4 L166.9 169.5 L168.1 169.7 L169.3 169.8 L170.5 169.9 L171.7 170.1 L172.9 170.2 L174.0 170.4 L175.2 170.5 L176.4 170.6 L177.6 170.8 L178.8 170.9 L180.0 171.0 L181.2 171.1 L182.3 171.3 L183.5 171.4 L184.7 171.5 L185.9 171.6 L187.1 171.7 L188.3 171.8 L189.5 172.0 L190.6 172.1 L191.8 172.2 L193.0 172.3 L194.2 172.4 L195.4 172.5 L196.6 172.6 L197.8 172.7 L198.9 172.8 L200.1 172.9 L201.3 173.0 L202.5 173.1 L203.7 173.2 L204.9 173.3 L206.1 173.4 L207.3 173.5 L208.4 173.6 L209.6 173.6 L210.8 173.7 L212.0 173.8 L213.2 173.9 L214.4 174.0 L215.6 174.1 L216.7 174.2 L217.9 174.2 L219.1 174.3 L220.3 174.4 L221.5 174.5 L222.7 174.6 L223.9 174.6 L225.0 174.7 L226.2 174.8 L227.4 174.9 L228.6 174.9 L229.8 175.0 L231.0 175.1 L232.2 175.2 L233.4 175.2 L234.5 175.3 L235.7 175.4 L236.9 175.4 L238.1 175.5 L239.3 175.6 L240.5 175.6 L241.7 175.7 L242.8 175.8 L244.0 175.8 L245.2 175.9 L246.4 175.9 L247.6 176.0 L248.8 176.1 L250.0 176.1 L251.1 176.2 L252.3 176.3 L253.5 176.3 L254.7 176.4 L255.9 176.4 L257.1 176.5 L258.3 176.5 L259.4 176.6 L260.6 176.7 L261.8 176.7 L263.0 176.8 L264.2 176.8 L265.4 176.9 L266.6 176.9 L267.8 177.0 L268.9 177.0 L270.1 177.1 L271.3 177.1 L272.5 177.2 L273.7 177.2 L274.9 177.3 L276.1 177.3 L277.2 177.4 L278.4 177.4 L279.6 177.5 L280.8 177.5 L282.0 177.6 L283.2 177.6 L284.4 177.7 L285.5 177.7 L286.7 177.7 L287.9 177.8 L289.1 177.8 L290.3 177.9 L291.5 177.9 L292.7 178.0 L293.8 178.0 L295.0 178.0 L296.2 178.1 L297.4 178.1 L298.6 178.2 L299.8 178.2 L301.0 178.2 L302.2 178.3 L303.3 178.3 L304.5 178.4 L305.7 178.4 L306.9 178.4 L308.1 178.5 L309.3 178.5 L310.5 178.6 L311.6 178.6 L312.8 178.6 L314.0 178.7 L315.2 178.7 L316.4 178.7 L317.6 178.8 L318.8 178.8 L319.9 178.9 L321.1 178.9" fill="none" stroke="#7c3aed" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="5 3"/><path d="M36.4 97.2 L37.6 104.0 L38.8 109.9 L40.0 115.0 L41.2 119.4 L42.4 123.4 L43.6 126.9 L44.7 130.0 L45.9 132.9 L47.1 135.5 L48.3 137.8 L49.5 139.9 L50.7 141.9 L51.9 143.7 L53.0 145.4 L54.2 146.9 L55.4 148.4 L56.6 149.7 L57.8 151.0 L59.0 152.1 L60.2 153.2 L61.3 154.3 L62.5 155.3 L63.7 156.2 L64.9 157.0 L66.1 157.9 L67.3 158.6 L68.5 159.4 L69.6 160.1 L70.8 160.8 L72.0 161.4 L73.2 162.0 L74.4 162.6 L75.6 163.1 L76.8 163.7 L78.0 164.2 L79.1 164.7 L80.3 165.1 L81.5 165.6 L82.7 166.0 L83.9 166.4 L85.1 166.8 L86.3 167.2 L87.4 167.6 L88.6 167.9 L89.8 168.3 L91.0 168.6 L92.2 168.9 L93.4 169.2 L94.6 169.6 L95.7 169.8 L96.9 170.1 L98.1 170.4 L99.3 170.7 L100.5 170.9 L101.7 171.2 L102.9 171.4 L104.0 171.6 L105.2 171.9 L106.4 172.1 L107.6 172.3 L108.8 172.5 L110.0 172.7 L111.2 172.9 L112.4 173.1 L113.5 173.3 L114.7 173.5 L115.9 173.7 L117.1 173.8 L118.3 174.0 L119.5 174.2 L120.7 174.3 L121.8 174.5 L123.0 174.7 L124.2 174.8 L125.4 175.0 L126.6 175.1 L127.8 175.2 L129.0 175.4 L130.1 175.5 L131.3 175.7 L132.5 175.8 L133.7 175.9 L134.9 176.0 L136.1 176.2 L137.3 176.3 L138.5 176.4 L139.6 176.5 L140.8 176.6 L142.0 176.7 L143.2 176.8 L144.4 176.9 L145.6 177.0 L146.8 177.1 L147.9 177.2 L149.1 177.3 L150.3 177.4 L151.5 177.5 L152.7 177.6 L153.9 177.7 L155.1 177.8 L156.2 177.9 L157.4 178.0 L158.6 178.1 L159.8 178.1 L161.0 178.2 L162.2 178.3 L163.4 178.4 L164.5 178.5 L165.7 178.5 L166.9 178.6 L168.1 178.7 L169.3 178.8 L170.5 178.8 L171.7 178.9 L172.9 179.0 L174.0 179.0 L175.2 179.1 L176.4 179.2 L177.6 179.2 L178.8 179.3 L180.0 179.4 L181.2 179.4 L182.3 179.5 L183.5 179.5 L184.7 179.6 L185.9 179.7 L187.1 179.7 L188.3 179.8 L189.5 179.8 L190.6 179.9 L191.8 179.9 L193.0 180.0 L194.2 180.1 L195.4 180.1 L196.6 180.2 L197.8 180.2 L198.9 180.3 L200.1 180.3 L201.3 180.4 L202.5 180.4 L203.7 180.5 L204.9 180.5 L206.1 180.5 L207.3 180.6 L208.4 180.6 L209.6 180.7 L210.8 180.7 L212.0 180.8 L213.2 180.8 L214.4 180.9 L215.6 180.9 L216.7 180.9 L217.9 181.0 L219.1 181.0 L220.3 181.1 L221.5 181.1 L222.7 181.1 L223.9 181.2 L225.0 181.2 L226.2 181.3 L227.4 181.3 L228.6 181.3 L229.8 181.4 L231.0 181.4 L232.2 181.4 L233.4 181.5 L234.5 181.5 L235.7 181.5 L236.9 181.6 L238.1 181.6 L239.3 181.6 L240.5 181.7 L241.7 181.7 L242.8 181.7 L244.0 181.8 L245.2 181.8 L246.4 181.8 L247.6 181.9 L248.8 181.9 L250.0 181.9 L251.1 182.0 L252.3 182.0 L253.5 182.0 L254.7 182.0 L255.9 182.1 L257.1 182.1 L258.3 182.1 L259.4 182.2 L260.6 182.2 L261.8 182.2 L263.0 182.2 L264.2 182.3 L265.4 182.3 L266.6 182.3 L267.8 182.3 L268.9 182.4 L270.1 182.4 L271.3 182.4 L272.5 182.4 L273.7 182.5 L274.9 182.5 L276.1 182.5 L277.2 182.5 L278.4 182.6 L279.6 182.6 L280.8 182.6 L282.0 182.6 L283.2 182.7 L284.4 182.7 L285.5 182.7 L286.7 182.7 L287.9 182.7 L289.1 182.8 L290.3 182.8 L291.5 182.8 L292.7 182.8 L293.8 182.9 L295.0 182.9 L296.2 182.9 L297.4 182.9 L298.6 182.9 L299.8 183.0 L301.0 183.0 L302.2 183.0 L303.3 183.0 L304.5 183.0 L305.7 183.1 L306.9 183.1 L308.1 183.1 L309.3 183.1 L310.5 183.1 L311.6 183.2 L312.8 183.2 L314.0 183.2 L315.2 183.2 L316.4 183.2 L317.6 183.2 L318.8 183.3 L319.9 183.3 L321.1 183.3" fill="none" stroke="#b45309" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="5 3"/><path d="M36.4 35.6 L37.0 43.2 L37.6 50.3 L38.1 57.0 L38.7 63.2 L39.3 69.0 L39.8 74.4 L40.4 79.6 L41.0 84.4 L41.6 88.9 L42.1 93.2 L42.7 97.3 L43.3 101.1 L43.8 104.7 L44.4 108.1 L45.0 111.4 L45.5 114.4 L46.1 117.3 L46.7 120.1 L47.3 122.6 L47.8 125.1 L48.4 127.4 L49.0 129.6 L49.5 131.6 L50.1 133.6 L50.7 135.4 L51.2 137.1 L51.8 138.8 L52.4 140.3 L52.9 141.7 L53.5 143.1 L54.1 144.3 L54.7 145.5 L55.2 146.6 L55.8 147.6 L56.4 148.6 L56.9 149.5 L57.5 150.3 L58.1 151.0 L58.6 151.7 L59.2 152.3 L59.8 152.9 L60.3 153.4 L60.9 153.9 L61.5 154.3 L62.1 154.7 L62.6 155.0 L63.2 155.2 L63.8 155.5 L64.3 155.7 L64.9 155.8 L65.5 156.0 L66.0 156.1 L66.6 156.1 L67.2 156.2 L67.8 156.2 L68.3 156.1 L68.9 156.1 L69.5 156.0 L70.0 156.0 L70.6 155.9 L71.2 155.7 L71.7 155.6 L72.3 155.5 L72.9 155.3 L73.4 155.1 L74.0 154.9 L74.6 154.8 L75.2 154.6 L75.7 154.4 L76.3 154.2 L76.9 154.0 L77.4 153.8 L78.0 153.6 L78.6 153.4 L79.1 153.2 L79.7 153.0 L80.3 152.8 L80.8 152.6 L81.4 152.4 L82.0 152.3 L82.6 152.1 L83.1 151.9 L83.7 151.8 L84.3 151.7 L84.8 151.6 L85.4 151.5 L86.0 151.4 L86.5 151.3 L87.1 151.2 L87.7 151.2 L88.2 151.1 L88.8 151.1 L89.4 151.1 L90.0 151.1 L90.5 151.1 L91.1 151.2 L91.7 151.2 L92.2 151.3 L92.8 151.4 L93.4 151.5 L93.9 151.7 L94.5 151.8 L95.1 152.0 L95.7 152.1 L96.2 152.3 L96.8 152.5 L97.4 152.8 L97.9 153.0 L98.5 153.3 L99.1 153.5 L99.6 153.8 L100.2 154.1 L100.8 154.4 L101.3 154.8 L101.9 155.1 L102.5 155.4 L103.1 155.8 L103.6 156.2 L104.2 156.6 L104.8 157.0 L105.3 157.4 L105.9 157.8 L106.5 158.2 L107.0 158.6 L107.6 159.1 L108.2 159.5 L108.7 160.0 L109.3 160.4 L109.9 160.9 L110.5 161.3 L111.0 161.8 L111.6 162.3 L112.2 162.7 L112.7 163.2 L113.3 163.7 L113.9 164.1 L114.4 164.6 L115.0 165.1 L115.6 165.5 L116.1 166.0 L116.7 166.4 L117.3 166.9 L117.9 167.3 L118.4 167.8 L119.0 168.2 L119.6 168.6 L120.1 169.1 L120.7 169.5 L121.3 169.9 L121.8 170.3 L122.4 170.6 L123.0 171.0 L123.6 171.4 L124.1 171.7 L124.7 172.1 L125.3 172.4 L125.8 172.7 L126.4 173.0 L127.0 173.3 L127.5 173.6 L128.1 173.9 L128.7 174.1 L129.2 174.4 L129.8 174.6 L130.4 174.8 L131.0 175.0 L131.5 175.2 L132.1 175.3 L132.7 175.5 L133.2 175.6 L133.8 175.8 L134.4 175.9 L134.9 176.0 L135.5 176.1 L136.1 176.1 L136.6 176.2 L137.2 176.3 L137.8 176.3 L138.4 176.3 L138.9 176.3 L139.5 176.3 L140.1 176.3 L140.6 176.3 L141.2 176.2 L141.8 176.2 L142.3 176.1 L142.9 176.1 L143.5 176.0 L144.0 175.9 L144.6 175.8 L145.2 175.7 L145.8 175.6 L146.3 175.5 L146.9 175.3 L147.5 175.2 L148.0 175.1 L148.6 174.9 L149.2 174.8 L149.7 174.6 L150.3 174.5 L150.9 174.3 L151.5 174.1 L152.0 174.0 L152.6 173.8 L153.2 173.6 L153.7 173.5 L154.3 173.3 L154.9 173.1 L155.4 173.0 L156.0 172.8 L156.6 172.6 L157.1 172.5 L157.7 172.3 L158.3 172.1 L158.9 172.0 L159.4 171.8 L160.0 171.7 L160.6 171.5 L161.1 171.4 L161.7 171.3 L162.3 171.2 L162.8 171.0 L163.4 170.9 L164.0 170.8 L164.5 170.7 L165.1 170.6 L165.7 170.6 L166.3 170.5 L166.8 170.4 L167.4 170.4 L168.0 170.3 L168.5 170.3 L169.1 170.2 L169.7 170.2 L170.2 170.2 L170.8 170.2 L171.4 170.2 L172.0 170.2 L172.5 170.3 L173.1 170.3 L173.7 170.3 L174.2 170.4 L174.8 170.4 L175.4 170.5 L175.9 170.6 L176.5 170.7 L177.1 170.8 L177.6 170.9 L178.2 171.0 L178.8 171.1 L179.4 171.2 L179.9 171.4 L180.5 171.5 L181.1 171.7 L181.6 171.8 L182.2 172.0 L182.8 172.2 L183.3 172.3 L183.9 172.5 L184.5 172.7 L185.0 172.9 L185.6 173.1 L186.2 173.3 L186.8 173.5 L187.3 173.7 L187.9 173.9 L188.5 174.1 L189.0 174.3 L189.6 174.6 L190.2 174.8 L190.7 175.0 L191.3 175.2 L191.9 175.4 L192.4 175.7 L193.0 175.9 L193.6 176.1 L194.2 176.3 L194.7 176.5 L195.3 176.7 L195.9 177.0 L196.4 177.2 L197.0 177.4 L197.6 177.6 L198.1 177.8 L198.7 178.0 L199.3 178.2 L199.9 178.3 L200.4 178.5 L201.0 178.7 L201.6 178.9 L202.1 179.0 L202.7 179.2 L203.3 179.3 L203.8 179.5 L204.4 179.6 L205.0 179.8 L205.5 179.9 L206.1 180.0 L206.7 180.1 L207.3 180.2 L207.8 180.3 L208.4 180.4 L209.0 180.5 L209.5 180.5 L210.1 180.6 L210.7 180.7 L211.2 180.7 L211.8 180.7 L212.4 180.8 L212.9 180.8 L213.5 180.8 L214.1 180.8 L214.7 180.8 L215.2 180.8 L215.8 180.8 L216.4 180.8 L216.9 180.8 L217.5 180.7 L218.1 180.7 L218.6 180.6 L219.2 180.6 L219.8 180.5 L220.3 180.5 L220.9 180.4 L221.5 180.3 L222.1 180.2 L222.6 180.1 L223.2 180.1 L223.8 180.0 L224.3 179.9 L224.9 179.8 L225.5 179.7 L226.0 179.5 L226.6 179.4 L227.2 179.3 L227.8 179.2 L228.3 179.1 L228.9 179.0 L229.5 178.8 L230.0 178.7 L230.6 178.6 L231.2 178.5 L231.7 178.4 L232.3 178.2 L232.9 178.1 L233.4 178.0 L234.0 177.9 L234.6 177.8 L235.2 177.6 L235.7 177.5 L236.3 177.4 L236.9 177.3 L237.4 177.2 L238.0 177.1 L238.6 177.0 L239.1 176.9 L239.7 176.8 L240.3 176.8 L240.8 176.7 L241.4 176.6 L242.0 176.5 L242.6 176.5 L243.1 176.4 L243.7 176.4 L244.3 176.3 L244.8 176.3 L245.4 176.2 L246.0 176.2 L246.5 176.2 L247.1 176.1 L247.7 176.1 L248.3 176.1 L248.8 176.1 L249.4 176.1 L250.0 176.1 L250.5 176.2 L251.1 176.2 L251.7 176.2 L252.2 176.3 L252.8 176.3 L253.4 176.4 L253.9 176.4 L254.5 176.5 L255.1 176.5 L255.7 176.6 L256.2 176.7 L256.8 176.8 L257.4 176.9 L257.9 176.9 L258.5 177.0 L259.1 177.1 L259.6 177.3 L260.2 177.4 L260.8 177.5 L261.3 177.6 L261.9 177.7 L262.5 177.8 L263.1 178.0 L263.6 178.1 L264.2 178.2 L264.8 178.4 L265.3 178.5 L265.9 178.6 L266.5 178.8 L267.0 178.9 L267.6 179.1 L268.2 179.2 L268.7 179.4 L269.3 179.5 L269.9 179.6 L270.5 179.8 L271.0 179.9 L271.6 180.1 L272.2 180.2 L272.7 180.3 L273.3 180.5 L273.9 180.6 L274.4 180.7 L275.0 180.9 L275.6 181.0 L276.2 181.1 L276.7 181.2 L277.3 181.4 L277.9 181.5 L278.4 181.6 L279.0 181.7 L279.6 181.8 L280.1 181.9 L280.7 182.0 L281.3 182.1 L281.8 182.2 L282.4 182.2 L283.0 182.3 L283.6 182.4 L284.1 182.4 L284.7 182.5 L285.3 182.6 L285.8 182.6 L286.4 182.6 L287.0 182.7 L287.5 182.7 L288.1 182.7 L288.7 182.8 L289.2 182.8 L289.8 182.8 L290.4 182.8 L291.0 182.8 L291.5 182.8 L292.1 182.8 L292.7 182.7 L293.2 182.7 L293.8 182.7 L294.4 182.7 L294.9 182.6 L295.5 182.6 L296.1 182.5 L296.6 182.5 L297.2 182.4 L297.8 182.4 L298.4 182.3 L298.9 182.3 L299.5 182.2 L300.1 182.1 L300.6 182.0 L301.2 182.0 L301.8 181.9 L302.3 181.8 L302.9 181.7 L303.5 181.6 L304.1 181.5 L304.6 181.4 L305.2 181.3 L305.8 181.3 L306.3 181.2 L306.9 181.1 L307.5 181.0 L308.0 180.9 L308.6 180.8 L309.2 180.7 L309.7 180.6 L310.3 180.5 L310.9 180.4 L311.5 180.3 L312.0 180.2 L312.6 180.2 L313.2 180.1 L313.7 180.0 L314.3 179.9 L314.9 179.8 L315.4 179.8 L316.0 179.7 L316.6 179.6 L317.1 179.5 L317.7 179.5 L318.3 179.4 L318.9 179.4 L319.4 179.3 L320.0 179.3 L320.6 179.2 L321.1 179.2" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><text x="77.8" y="131.5" text-anchor="middle" font-size="12" font-weight="700" fill="#7c3aed" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2/x</text><text x="109.4" y="188.6" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1/x</text><text x="189.7" y="138.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(cos²x + 1)/x</text></svg>
:::

Les deux courbes en pointillé sont les bornes u(x) = 1/x et v(x) = 2/x de l'exemple ; la courbe verte, enfermée entre elles, les suit vers 0.

::: exemple Limites en +∞ et en −∞ de f(x) = (cos²x + 1)/x
1. Pour tout x, 0 ≤ cos²x ≤ 1, donc 1 ≤ cos²x + 1 ≤ 2 — on encadre le numérateur.
2. Pour x > 0, on divise par x > 0, ce qui garde le sens : 1/x ≤ f(x) ≤ 2/x.
3. lim x→+∞ 1/x = lim x→+∞ 2/x = 0 : les deux bornes ont la même limite 0.
4. f est coincée : lim x→+∞ f(x) = 0.
5. Pour x < 0, on divise par x < 0, ce qui **renverse** les inégalités : 2/x ≤ f(x) ≤ 1/x ; les deux bornes tendent vers 0 en −∞, donc lim x→−∞ f(x) = 0.

:::

::: piege Oublier de renverser les inégalités pour x < 0
Pour x < 0, on écrit « 1/x ≤ f(x) ≤ 2/x ». Cela tente parce qu'on a copié le cas x > 0. Mais en x = −1, f(−1) = (cos²1 + 1)/(−1) ≈ −1,29 alors que 1/x = −1 et 2/x = −2 : −1 ≤ −1,29 est faux. Diviser par un nombre négatif renverse l'ordre : 2/x ≤ f(x) ≤ 1/x.
:::

::: propriete
Soit f, u, v définies sur un intervalle I sauf peut-être en un réel a, et ℓ, ℓ′ des réels. Les inégalités valent pour tout x ≠ a de I.

- Si u(x) ≤ v(x), lim u = ℓ et lim v = ℓ′, alors ℓ ≤ ℓ′.
- **Gendarmes** : si u(x) ≤ f(x) ≤ v(x) et lim u = lim v = ℓ, alors lim f = ℓ.
- Si v(x) ≥ u(x) et lim u = +∞, alors lim v = +∞.
- Si v(x) ≤ u(x) et lim u = −∞, alors lim v = −∞.

Ces résultats restent valables à l'infini, à droite de a et à gauche de a.

Cas limite : si les deux bornes n'ont pas la même limite, l'encadrement ne conclut rien. Une inégalité stricte devient large à la limite : 0 < x² < |x| pour 0 < |x| < 1, mais les deux bornes tendent vers 0, donc « < » devient « ≤ ».
:::

::: verifie
Calcule lim x→−∞ (3 + sin x)/x.

---

Pour tout x, −1 ≤ sin x ≤ 1, donc 2 ≤ 3 + sin x ≤ 4. Pour x < 0, on divise par x < 0 : les inégalités se renversent, 4/x ≤ f(x) ≤ 2/x. Les deux bornes tendent vers 0 quand x → −∞ : par les gendarmes, lim f = 0.
:::

::: retenir
Pour une fonction qui oscille, on l'encadre par deux fonctions de même limite ℓ : elle a alors pour limite ℓ ; attention au sens des inégalités quand on divise par un nombre négatif.
:::

## 🌉 Théorème des valeurs intermédiaires

Un ballon-sonde passe de 3 °C à 25 °C entre 8 h et 14 h, et la température change sans jamais sauter. A-t-il nécessairement fait exactement 10 °C à un moment donné ? Autrement dit, une courbe continue qui va de 3 à 25 passe-t-elle forcément par 10 ?

::: figure La courbe continue de f(x) = 2x − cos x passe de −1 à π sur [0 ; π/2] : elle coupe la droite y = π/6 en au moins un point, d'abscisse α
<svg viewBox="0 0 340 240"><title>Courbe de f(x) = 2x − cos x sur l'intervalle de 0 à π/2 et droite horizontale d'ordonnée π/6</title><path d="M30.0 155.2 H326.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M67.2 218.0 V14.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M326.0 155.2 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M67.2 14.0 l-3.5 7 l7 0 z" fill="#0f172a"/><line x1="171.4" y1="152.2" x2="171.4" y2="158.2" stroke="#0f172a" stroke-width="1.4"/><text x="171.4" y="170.2" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">π/4</text><line x1="275.7" y1="152.2" x2="275.7" y2="158.2" stroke="#0f172a" stroke-width="1.4"/><text x="275.7" y="170.2" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">π/2</text><line x1="64.2" y1="194.4" x2="70.2" y2="194.4" stroke="#0f172a" stroke-width="1.4"/><text x="61.2" y="198.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="64.2" y1="116.0" x2="70.2" y2="116.0" stroke="#0f172a" stroke-width="1.4"/><text x="61.2" y="120.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="64.2" y1="37.5" x2="70.2" y2="37.5" stroke="#0f172a" stroke-width="1.4"/><text x="61.2" y="41.5" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><text x="324.0" y="149.2" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="75.2" y="22.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="34.0" y1="134.6" x2="326.0" y2="134.6" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><path d="M67.2 194.4 L68.1 193.9 L68.9 193.4 L69.8 192.8 L70.7 192.3 L71.5 191.8 L72.4 191.3 L73.3 190.8 L74.1 190.2 L75.0 189.7 L75.9 189.2 L76.7 188.6 L77.6 188.1 L78.5 187.6 L79.3 187.0 L80.2 186.5 L81.1 186.0 L81.9 185.4 L82.8 184.9 L83.7 184.3 L84.6 183.8 L85.4 183.2 L86.3 182.7 L87.2 182.1 L88.0 181.6 L88.9 181.0 L89.8 180.5 L90.6 179.9 L91.5 179.4 L92.4 178.8 L93.2 178.2 L94.1 177.7 L95.0 177.1 L95.8 176.5 L96.7 176.0 L97.6 175.4 L98.5 174.8 L99.3 174.3 L100.2 173.7 L101.1 173.1 L101.9 172.5 L102.8 171.9 L103.7 171.4 L104.5 170.8 L105.4 170.2 L106.3 169.6 L107.1 169.0 L108.0 168.4 L108.9 167.8 L109.7 167.2 L110.6 166.6 L111.5 166.0 L112.4 165.4 L113.2 164.8 L114.1 164.2 L115.0 163.6 L115.8 163.0 L116.7 162.4 L117.6 161.8 L118.4 161.2 L119.3 160.6 L120.2 160.0 L121.0 159.4 L121.9 158.8 L122.8 158.1 L123.6 157.5 L124.5 156.9 L125.4 156.3 L126.3 155.7 L127.1 155.0 L128.0 154.4 L128.9 153.8 L129.7 153.2 L130.6 152.5 L131.5 151.9 L132.3 151.3 L133.2 150.6 L134.1 150.0 L134.9 149.4 L135.8 148.7 L136.7 148.1 L137.5 147.4 L138.4 146.8 L139.3 146.1 L140.2 145.5 L141.0 144.8 L141.9 144.2 L142.8 143.5 L143.6 142.9 L144.5 142.2 L145.4 141.6 L146.2 140.9 L147.1 140.3 L148.0 139.6 L148.8 138.9 L149.7 138.3 L150.6 137.6 L151.4 137.0 L152.3 136.3 L153.2 135.6 L154.1 135.0 L154.9 134.3 L155.8 133.6 L156.7 132.9 L157.5 132.3 L158.4 131.6 L159.3 130.9 L160.1 130.2 L161.0 129.6 L161.9 128.9 L162.7 128.2 L163.6 127.5 L164.5 126.8 L165.3 126.1 L166.2 125.5 L167.1 124.8 L168.0 124.1 L168.8 123.4 L169.7 122.7 L170.6 122.0 L171.4 121.3 L172.3 120.6 L173.2 119.9 L174.0 119.2 L174.9 118.5 L175.8 117.8 L176.6 117.1 L177.5 116.4 L178.4 115.7 L179.2 115.0 L180.1 114.3 L181.0 113.6 L181.8 112.9 L182.7 112.2 L183.6 111.5 L184.5 110.8 L185.3 110.0 L186.2 109.3 L187.1 108.6 L187.9 107.9 L188.8 107.2 L189.7 106.5 L190.5 105.7 L191.4 105.0 L192.3 104.3 L193.1 103.6 L194.0 102.9 L194.9 102.1 L195.7 101.4 L196.6 100.7 L197.5 100.0 L198.4 99.2 L199.2 98.5 L200.1 97.8 L201.0 97.0 L201.8 96.3 L202.7 95.6 L203.6 94.9 L204.4 94.1 L205.3 93.4 L206.2 92.7 L207.0 91.9 L207.9 91.2 L208.8 90.4 L209.6 89.7 L210.5 89.0 L211.4 88.2 L212.3 87.5 L213.1 86.7 L214.0 86.0 L214.9 85.3 L215.7 84.5 L216.6 83.8 L217.5 83.0 L218.3 82.3 L219.2 81.5 L220.1 80.8 L220.9 80.0 L221.8 79.3 L222.7 78.5 L223.5 77.8 L224.4 77.0 L225.3 76.3 L226.2 75.5 L227.0 74.8 L227.9 74.0 L228.8 73.3 L229.6 72.5 L230.5 71.8 L231.4 71.0 L232.2 70.2 L233.1 69.5 L234.0 68.7 L234.8 68.0 L235.7 67.2 L236.6 66.5 L237.4 65.7 L238.3 64.9 L239.2 64.2 L240.1 63.4 L240.9 62.7 L241.8 61.9 L242.7 61.1 L243.5 60.4 L244.4 59.6 L245.3 58.8 L246.1 58.1 L247.0 57.3 L247.9 56.6 L248.7 55.8 L249.6 55.0 L250.5 54.3 L251.3 53.5 L252.2 52.7 L253.1 52.0 L254.0 51.2 L254.8 50.4 L255.7 49.7 L256.6 48.9 L257.4 48.1 L258.3 47.4 L259.2 46.6 L260.0 45.8 L260.9 45.1 L261.8 44.3 L262.6 43.5 L263.5 42.8 L264.4 42.0 L265.2 41.2 L266.1 40.4 L267.0 39.7 L267.9 38.9 L268.7 38.1 L269.6 37.4 L270.5 36.6 L271.3 35.8 L272.2 35.1 L273.1 34.3 L273.9 33.5 L274.8 32.7 L275.7 32.0" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="67.2" cy="194.4" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="275.7" cy="32.0" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><line x1="154.5" y1="155.2" x2="154.5" y2="134.6" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><circle cx="154.5" cy="134.6" r="4" fill="#b45309" stroke="#0f172a" stroke-width="1"/><text x="158.5" y="182.2" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">α</text><text x="324.0" y="127.6" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = π/6</text></svg>
:::

La droite pointillée est la hauteur k = π/6 ; le point orange est la solution α de l'équation f(x) = k.

::: exemple Une solution de 2x − cos x = π/6 dans [0 ; π/2]
1. f(x) = 2x − cos x est continue sur [0 ; π/2] : somme de 2x et de −cos x, continues sur ℝ.
2. f(0) = −1 et f(π/2) = π ≈ 3,14 — on calcule la valeur à chaque bout.
3. k = π/6 ≈ 0,52 est compris entre f(0) = −1 et f(π/2) = π.
4. D'après le théorème des valeurs intermédiaires, l'équation f(x) = π/6 admet au moins une solution α dans [0 ; π/2].
5. On localise une solution : f(π/4) = π/2 − √2/2 ≈ 0,86 > π/6, donc le théorème appliqué sur [0 ; π/4] donne une solution dans ]0 ; π/4[ (l'unicité viendra de la stricte croissance, notion suivante).

:::

::: piege Appliquer le théorème à une fonction qui n'est pas continue
Soit g(x) = 1/x pour x ≠ 0 et g(0) = 1, sur [−1 ; 1] : g(−1) = −1 et g(1) = 1, donc g(−1) × g(1) < 0. Cela tente parce que les valeurs aux bouts sont de signes opposés. Mais g ne s'annule jamais (1/x ≠ 0, et g(0) = 1) : le théorème exige que g soit continue sur [−1 ; 1], et g ne l'est pas en 0.
:::

::: propriete
- L'image d'un intervalle par une fonction continue est un intervalle.
- **Théorème des valeurs intermédiaires.** Soit f continue sur un intervalle I et a < b dans I. Pour tout réel k compris entre f(a) et f(b), l'équation f(x) = k admet **au moins une** solution dans [a ; b]. En particulier, si f(a) × f(b) < 0, l'équation f(x) = 0 a au moins une solution dans ]a ; b[.
- **Signe constant.** Si f est continue sur un intervalle I et ne s'annule en aucun point de I, alors f garde un signe constant sur I. *Preuve* : sinon il existe α < β dans I avec f(α) × f(β) < 0 ; f est continue sur [α ; β], donc s'annule dans [α ; β], ce qui contredit l'hypothèse.

Cas limite : « au moins une » ne veut pas dire « une seule » : le théorème ne compte pas les solutions.
:::

::: exemple Un point fixe sur [0 ; 1]
Soit f continue de [0 ; 1] dans [0 ; 1] ; on cherche x tel que f(x) = x.

1. On pose g(x) = f(x) − x, continue sur [0 ; 1] — on se ramène à une équation g(x) = 0.
2. f(0) ∈ [0 ; 1], donc g(0) = f(0) ≥ 0.
3. f(1) ≤ 1, donc g(1) = f(1) − 1 ≤ 0.
4. Donc g(0) × g(1) ≤ 0 : g s'annule dans [0 ; 1] (si le produit est nul, c'est déjà fait en 0 ou en 1).
5. L'équation f(x) = x admet au moins une solution dans [0 ; 1].

:::

::: verifie
Soit f(x) = 1 + x + x² + x³ + x⁴. Pour x ≠ 1, f(x) = (x⁵ − 1)/(x − 1). Montre que f garde un signe constant sur ℝ et donne ce signe.

---

f est un polynôme, donc continue sur ℝ. Elle ne s'annule jamais : pour x ≠ 1, f(x) = 0 imposerait x⁵ = 1, donc x = 1, ce qui est exclu, et f(1) = 5 ≠ 0. D'après le théorème du signe constant, f garde un signe constant ; comme f(0) = 1 > 0, ce signe est positif.
:::

::: retenir
f continue prend toutes les valeurs comprises entre f(a) et f(b), donc f(a) × f(b) < 0 garantit au moins une solution de f(x) = 0 ; une fonction continue qui ne s'annule pas garde son signe.
:::

## 🎯 Stricte monotonie, solution unique et dichotomie

Le théorème des valeurs intermédiaires promet au moins une solution à x³ + x − 1 = 0 entre 0 et 1.
Peut-elle en avoir deux ? Et comment l'encadrer à un dixième près, sans résoudre l'équation, en faisant travailler la machine ?

::: definition
Soit f définie sur un intervalle I. f est **strictement croissante** sur I si, pour tous a < b de I, f(a) < f(b) ; **strictement décroissante** si f(a) > f(b). Elle est **strictement monotone** si elle est l'un ou l'autre.
:::

::: figure La courbe de x³ + x − 1 monte sans cesse ; les barres montrent les intervalles successifs de la dichotomie qui encadrent α
<svg viewBox="0 0 340 250"><title>Courbe de x³ + x − 1 et intervalles successifs de la dichotomie qui encadrent sa racine</title><path d="M26.0 163.4 H326.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M53.7 228.0 V14.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M326.0 163.4 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M53.7 14.0 l-3.5 7 l7 0 z" fill="#0f172a"/><line x1="172.1" y1="160.4" x2="172.1" y2="166.4" stroke="#0f172a" stroke-width="1.4"/><text x="172.1" y="178.4" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1/2</text><line x1="201.7" y1="160.4" x2="201.7" y2="166.4" stroke="#0f172a" stroke-width="1.4"/><text x="201.7" y="178.4" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5/8</text><line x1="231.3" y1="160.4" x2="231.3" y2="166.4" stroke="#0f172a" stroke-width="1.4"/><text x="231.3" y="178.4" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3/4</text><line x1="290.5" y1="160.4" x2="290.5" y2="166.4" stroke="#0f172a" stroke-width="1.4"/><text x="290.5" y="178.4" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="50.7" y1="203.8" x2="56.7" y2="203.8" stroke="#0f172a" stroke-width="1.4"/><text x="47.7" y="207.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="50.7" y1="123.0" x2="56.7" y2="123.0" stroke="#0f172a" stroke-width="1.4"/><text x="47.7" y="127.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="324.0" y="157.4" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="61.7" y="22.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><path d="M53.7 203.8 L54.3 203.7 L55.5 203.5 L56.6 203.3 L57.7 203.1 L58.9 202.9 L60.0 202.7 L61.1 202.5 L62.3 202.3 L63.4 202.1 L64.5 202.0 L65.7 201.8 L66.8 201.6 L67.9 201.4 L69.1 201.2 L70.2 201.0 L71.3 200.8 L72.5 200.6 L73.6 200.4 L74.7 200.2 L75.9 200.0 L77.0 199.8 L78.1 199.6 L79.3 199.4 L80.4 199.2 L81.6 199.0 L82.7 198.8 L83.8 198.6 L85.0 198.4 L86.1 198.2 L87.2 198.0 L88.4 197.8 L89.5 197.6 L90.6 197.4 L91.8 197.1 L92.9 196.9 L94.0 196.7 L95.2 196.5 L96.3 196.3 L97.4 196.1 L98.6 195.9 L99.7 195.7 L100.8 195.4 L102.0 195.2 L103.1 195.0 L104.2 194.8 L105.4 194.6 L106.5 194.3 L107.7 194.1 L108.8 193.9 L109.9 193.7 L111.1 193.4 L112.2 193.2 L113.3 193.0 L114.5 192.8 L115.6 192.5 L116.7 192.3 L117.9 192.1 L119.0 191.8 L120.1 191.6 L121.3 191.3 L122.4 191.1 L123.5 190.9 L124.7 190.6 L125.8 190.4 L126.9 190.1 L128.1 189.9 L129.2 189.6 L130.3 189.4 L131.5 189.1 L132.6 188.9 L133.7 188.6 L134.9 188.3 L136.0 188.1 L137.2 187.8 L138.3 187.5 L139.4 187.3 L140.6 187.0 L141.7 186.7 L142.8 186.4 L144.0 186.2 L145.1 185.9 L146.2 185.6 L147.4 185.3 L148.5 185.0 L149.6 184.8 L150.8 184.5 L151.9 184.2 L153.0 183.9 L154.2 183.6 L155.3 183.3 L156.4 183.0 L157.6 182.7 L158.7 182.4 L159.8 182.1 L161.0 181.8 L162.1 181.4 L163.2 181.1 L164.4 180.8 L165.5 180.5 L166.7 180.2 L167.8 179.8 L168.9 179.5 L170.1 179.2 L171.2 178.8 L172.3 178.5 L173.5 178.2 L174.6 177.8 L175.7 177.5 L176.9 177.1 L178.0 176.8 L179.1 176.4 L180.3 176.0 L181.4 175.7 L182.5 175.3 L183.7 175.0 L184.8 174.6 L185.9 174.2 L187.1 173.8 L188.2 173.5 L189.3 173.1 L190.5 172.7 L191.6 172.3 L192.8 171.9 L193.9 171.5 L195.0 171.1 L196.2 170.7 L197.3 170.3 L198.4 169.9 L199.6 169.5 L200.7 169.1 L201.8 168.7 L203.0 168.2 L204.1 167.8 L205.2 167.4 L206.4 166.9 L207.5 166.5 L208.6 166.1 L209.8 165.6 L210.9 165.2 L212.0 164.7 L213.2 164.3 L214.3 163.8 L215.4 163.3 L216.6 162.9 L217.7 162.4 L218.8 161.9 L220.0 161.5 L221.1 161.0 L222.3 160.5 L223.4 160.0 L224.5 159.5 L225.7 159.0 L226.8 158.5 L227.9 158.0 L229.1 157.5 L230.2 157.0 L231.3 156.5 L232.5 155.9 L233.6 155.4 L234.7 154.9 L235.9 154.3 L237.0 153.8 L238.1 153.3 L239.3 152.7 L240.4 152.2 L241.5 151.6 L242.7 151.0 L243.8 150.5 L244.9 149.9 L246.1 149.3 L247.2 148.8 L248.3 148.2 L249.5 147.6 L250.6 147.0 L251.8 146.4 L252.9 145.8 L254.0 145.2 L255.2 144.6 L256.3 144.0 L257.4 143.3 L258.6 142.7 L259.7 142.1 L260.8 141.4 L262.0 140.8 L263.1 140.2 L264.2 139.5 L265.4 138.9 L266.5 138.2 L267.6 137.5 L268.8 136.9 L269.9 136.2 L271.0 135.5 L272.2 134.8 L273.3 134.1 L274.4 133.4 L275.6 132.7 L276.7 132.0 L277.9 131.3 L279.0 130.6 L280.1 129.9 L281.3 129.2 L282.4 128.4 L283.5 127.7 L284.7 126.9 L285.8 126.2 L286.9 125.4 L288.1 124.7 L289.2 123.9 L290.3 123.1 L291.5 122.4 L292.6 121.6 L293.7 120.8 L294.9 120.0 L296.0 119.2 L297.1 118.4 L298.3 117.6 L299.4 116.8 L300.5 116.0 L301.7 115.1 L302.8 114.3 L303.9 113.5 L305.1 112.6 L306.2 111.8 L307.4 110.9 L308.5 110.0 L309.6 109.2 L310.8 108.3 L311.9 107.4 L313.0 106.5 L314.2 105.6" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="53.7" y1="100.8" x2="290.5" y2="100.8" stroke="#94a3b8" stroke-width="5" stroke-linecap="butt"/><text x="296.5" y="98.8" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">[0 ; 1]</text><line x1="172.1" y1="79.8" x2="290.5" y2="79.8" stroke="#7c3aed" stroke-width="5" stroke-linecap="butt"/><text x="296.5" y="83.8" text-anchor="start" font-size="11" font-weight="700" fill="#7c3aed" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">[1/2 ; 1]</text><line x1="172.1" y1="58.8" x2="231.3" y2="58.8" stroke="#b45309" stroke-width="5" stroke-linecap="butt"/><text x="237.3" y="62.8" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">[1/2 ; 3/4]</text><line x1="201.7" y1="37.8" x2="231.3" y2="37.8" stroke="#0f6e56" stroke-width="5" stroke-linecap="butt"/><text x="237.3" y="41.8" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">[5/8 ; 3/4]</text><line x1="215.3" y1="211.9" x2="215.3" y2="102.8" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><circle cx="215.3" cy="163.4" r="4" fill="#b45309" stroke="#0f172a" stroke-width="1"/><text x="218.3" y="190.4" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">α</text></svg>
:::

Les barres sont les intervalles du tableau de l'exemple : le départ [0 ; 1], puis les intervalles gardés aux étapes 1, 2 et 3.

::: exemple Encadrer l'unique solution α de x³ + x − 1 = 0 dans [0 ; 1]
1. f(x) = x³ + x − 1 est continue (polynôme). Elle est strictement croissante : si a < b, alors a³ < b³ et a − 1 < b − 1, donc la somme augmente strictement.
2. f(0) = −1 < 0 < 1 = f(1) : le théorème donne une solution α dans ]0 ; 1[, et la stricte croissance interdit d'en avoir deux (a < b entraîne f(a) < f(b), donc f(a) et f(b) ne peuvent pas valoir 0 ensemble).
3. Dichotomie : on coupe l'intervalle en deux et on garde la moitié où f change de signe.

| étape | intervalle | milieu c | f(c) | on garde |
| --- | --- | --- | --- | --- |
| 1 | [0 ; 1] | 1/2 | −3/8 < 0 | [1/2 ; 1] |
| 2 | [1/2 ; 1] | 3/4 | 11/64 > 0 | [1/2 ; 3/4] |
| 3 | [1/2 ; 3/4] | 5/8 | −67/512 < 0 | [5/8 ; 3/4] |
| 4 | [5/8 ; 3/4] | 11/16 | 51/4096 > 0 | [5/8 ; 11/16] |

4. L'amplitude vaut 1 à l'étape 0, puis 1/2, 1/4, 1/8, 1/16 = 0,0625 < 0,1 : 0,625 < α < 0,6875, donc α est encadré à 10⁻¹ près.

:::

::: piege Conclure à l'unicité avec le seul théorème des valeurs intermédiaires
Pour f(x) = x³ − x sur [−2 ; 2], f(−2) = −6 < 0 < 6 = f(2), et on « conclut » que f(x) = 0 a une seule solution. Cela tente parce que le signe change une fois. Mais f(−1) = f(0) = f(1) = 0 : trois solutions. Le théorème donne l'existence ; pour l'unicité il faut la stricte monotonie.
:::

::: propriete
Soit f continue et **strictement monotone** sur I, a < b dans I. Pour tout réel k compris entre f(a) et f(b), l'équation f(x) = k admet **une unique** solution dans [a ; b].

Cas limite : si f(a) × f(b) < 0, l'unique solution de f(x) = 0 est dans ]a ; b[ ; si k = f(a) ou k = f(b), la solution unique est une borne.

**Au tableur** (formules françaises) : on place a dans A, b dans B, le milieu dans C, f(a), f(b), f(c) dans D, E, F. La ligne suivante contient `A3 = SI(F2*E2>0;A2;C2)` et `B3 = SI(F2*E2>0;C2;B2)` : si f(c) a le signe de f(b), la solution est dans [a ; c], sinon dans [c ; b].
:::

::: verifie
Montre que x⁵ + x − 3 = 0 admet une unique solution dans [1 ; 2].

---

f(x) = x⁵ + x − 3 est continue (polynôme) et strictement croissante (somme de x ↦ x⁵ et de x ↦ x − 3, strictement croissantes). f(1) = −1 < 0 et f(2) = 31 > 0. Continue et strictement monotone, avec 0 compris entre f(1) et f(2) : l'équation f(x) = 0 a une unique solution dans [1 ; 2]. L'existence vient du théorème des valeurs intermédiaires, l'unicité de la stricte monotonie.
:::

::: retenir
Continue et strictement monotone : une solution unique pour chaque valeur k entre f(a) et f(b) ; on la localise en coupant l'intervalle en deux, étape après étape.
:::

## 🔭 Image d'un intervalle par une fonction continue

f est continue sur [0 ; 3], avec f(0) = 4 et f(3) = 1. A-t-on forcément f([0 ; 3]) = [1 ; 4] ? Pas si la courbe plonge sous 1 entre les deux. Comment lire l'ensemble de toutes les valeurs prises par f sur un intervalle ?

::: figure La courbe de sin²x sur [−π/6 ; π/6] : f(−π/6) = f(π/6) = 1/4, mais le minimum 0 est atteint au milieu, en x = 0
<svg viewBox="0 0 340 230"><title>Courbe de sin²x entre les abscisses −π/6 et π/6, avec son minimum 0 et son maximum 1/4</title><path d="M32.0 173.1 H326.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M181.0 208.0 V14.0" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M326.0 173.1 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M181.0 14.0 l-3.5 7 l7 0 z" fill="#0f172a"/><line x1="91.7" y1="170.1" x2="91.7" y2="176.1" stroke="#0f172a" stroke-width="1.4"/><text x="91.7" y="188.1" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−π/6</text><line x1="270.3" y1="170.1" x2="270.3" y2="176.1" stroke="#0f172a" stroke-width="1.4"/><text x="270.3" y="188.1" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">π/6</text><line x1="178.0" y1="62.6" x2="184.0" y2="62.6" stroke="#0f172a" stroke-width="1.4"/><text x="165.0" y="66.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1/4</text><text x="324.0" y="167.1" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="189.0" y="22.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="36.0" y1="62.6" x2="326.0" y2="62.6" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="91.7" y1="173.1" x2="91.7" y2="62.6" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="270.3" y1="173.1" x2="270.3" y2="62.6" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><path d="M91.7 62.6 L92.4 64.3 L93.2 65.9 L93.9 67.6 L94.7 69.2 L95.4 70.8 L96.1 72.5 L96.9 74.1 L97.6 75.7 L98.4 77.3 L99.1 78.9 L99.9 80.4 L100.6 82.0 L101.4 83.6 L102.1 85.1 L102.8 86.6 L103.6 88.2 L104.3 89.7 L105.1 91.2 L105.8 92.7 L106.6 94.2 L107.3 95.6 L108.1 97.1 L108.8 98.5 L109.5 100.0 L110.3 101.4 L111.0 102.8 L111.8 104.2 L112.5 105.6 L113.3 107.0 L114.0 108.4 L114.8 109.7 L115.5 111.1 L116.2 112.4 L117.0 113.7 L117.7 115.0 L118.5 116.3 L119.2 117.6 L120.0 118.9 L120.7 120.1 L121.5 121.4 L122.2 122.6 L122.9 123.8 L123.7 125.0 L124.4 126.2 L125.2 127.4 L125.9 128.6 L126.7 129.7 L127.4 130.9 L128.2 132.0 L128.9 133.1 L129.6 134.2 L130.4 135.3 L131.1 136.4 L131.9 137.4 L132.6 138.5 L133.4 139.5 L134.1 140.5 L134.9 141.5 L135.6 142.5 L136.3 143.5 L137.1 144.4 L137.8 145.4 L138.6 146.3 L139.3 147.2 L140.1 148.1 L140.8 149.0 L141.6 149.9 L142.3 150.7 L143.0 151.5 L143.8 152.4 L144.5 153.2 L145.3 154.0 L146.0 154.7 L146.8 155.5 L147.5 156.3 L148.2 157.0 L149.0 157.7 L149.7 158.4 L150.5 159.1 L151.2 159.7 L152.0 160.4 L152.7 161.0 L153.5 161.7 L154.2 162.3 L154.9 162.8 L155.7 163.4 L156.4 164.0 L157.2 164.5 L157.9 165.0 L158.7 165.5 L159.4 166.0 L160.2 166.5 L160.9 167.0 L161.6 167.4 L162.4 167.8 L163.1 168.2 L163.9 168.6 L164.6 169.0 L165.4 169.4 L166.1 169.7 L166.9 170.0 L167.6 170.3 L168.3 170.6 L169.1 170.9 L169.8 171.2 L170.6 171.4 L171.3 171.6 L172.1 171.9 L172.8 172.1 L173.6 172.2 L174.3 172.4 L175.0 172.5 L175.8 172.7 L176.5 172.8 L177.3 172.9 L178.0 172.9 L178.8 173.0 L179.5 173.0 L180.3 173.1 L181.0 173.1 L181.7 173.1 L182.5 173.0 L183.2 173.0 L184.0 172.9 L184.7 172.9 L185.5 172.8 L186.2 172.7 L187.0 172.5 L187.7 172.4 L188.4 172.2 L189.2 172.1 L189.9 171.9 L190.7 171.6 L191.4 171.4 L192.2 171.2 L192.9 170.9 L193.7 170.6 L194.4 170.3 L195.1 170.0 L195.9 169.7 L196.6 169.4 L197.4 169.0 L198.1 168.6 L198.9 168.2 L199.6 167.8 L200.4 167.4 L201.1 167.0 L201.8 166.5 L202.6 166.0 L203.3 165.5 L204.1 165.0 L204.8 164.5 L205.6 164.0 L206.3 163.4 L207.1 162.8 L207.8 162.3 L208.5 161.7 L209.3 161.0 L210.0 160.4 L210.8 159.7 L211.5 159.1 L212.3 158.4 L213.0 157.7 L213.8 157.0 L214.5 156.3 L215.2 155.5 L216.0 154.7 L216.7 154.0 L217.5 153.2 L218.2 152.4 L219.0 151.5 L219.7 150.7 L220.4 149.9 L221.2 149.0 L221.9 148.1 L222.7 147.2 L223.4 146.3 L224.2 145.4 L224.9 144.4 L225.7 143.5 L226.4 142.5 L227.1 141.5 L227.9 140.5 L228.6 139.5 L229.4 138.5 L230.1 137.4 L230.9 136.4 L231.6 135.3 L232.4 134.2 L233.1 133.1 L233.8 132.0 L234.6 130.9 L235.3 129.7 L236.1 128.6 L236.8 127.4 L237.6 126.2 L238.3 125.0 L239.1 123.8 L239.8 122.6 L240.5 121.4 L241.3 120.1 L242.0 118.9 L242.8 117.6 L243.5 116.3 L244.3 115.0 L245.0 113.7 L245.8 112.4 L246.5 111.1 L247.2 109.7 L248.0 108.4 L248.7 107.0 L249.5 105.6 L250.2 104.2 L251.0 102.8 L251.7 101.4 L252.5 100.0 L253.2 98.5 L253.9 97.1 L254.7 95.6 L255.4 94.2 L256.2 92.7 L256.9 91.2 L257.7 89.7 L258.4 88.2 L259.2 86.6 L259.9 85.1 L260.6 83.6 L261.4 82.0 L262.1 80.4 L262.9 78.9 L263.6 77.3 L264.4 75.7 L265.1 74.1 L265.9 72.5 L266.6 70.8 L267.3 69.2 L268.1 67.6 L268.8 65.9 L269.6 64.3 L270.3 62.6" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><path d="M71.2 14.1 L71.4 14.5 L71.6 15.0 L71.8 15.5 L72.0 16.0 L72.2 16.5 L72.4 17.0 L72.6 17.5 L72.8 18.0 L73.0 18.4 L73.2 18.9 L73.4 19.4 L73.6 19.9 L73.8 20.4 L74.0 20.9 L74.2 21.3 L74.4 21.8 L74.6 22.3 L74.8 22.8 L75.0 23.3 L75.2 23.8 L75.4 24.2 L75.6 24.7 L75.8 25.2 L76.0 25.7 L76.2 26.2 L76.4 26.6 L76.6 27.1 L76.7 27.6 L76.9 28.1 L77.1 28.5 L77.3 29.0 L77.5 29.5 L77.7 30.0 L77.9 30.5 L78.1 30.9 L78.3 31.4 L78.5 31.9 L78.7 32.4 L78.9 32.8 L79.1 33.3 L79.3 33.8 L79.5 34.2 L79.7 34.7 L79.9 35.2 L80.1 35.7 L80.3 36.1 L80.5 36.6 L80.7 37.1 L80.9 37.5 L81.1 38.0 L81.3 38.5 L81.5 39.0 L81.7 39.4 L81.9 39.9 L82.1 40.4 L82.3 40.8 L82.4 41.3 L82.6 41.8 L82.8 42.2 L83.0 42.7 L83.2 43.1 L83.4 43.6 L83.6 44.1 L83.8 44.5 L84.0 45.0 L84.2 45.5 L84.4 45.9 L84.6 46.4 L84.8 46.8 L85.0 47.3 L85.2 47.8 L85.4 48.2 L85.6 48.7 L85.8 49.1 L86.0 49.6 L86.2 50.0 L86.4 50.5 L86.6 51.0 L86.8 51.4 L87.0 51.9 L87.2 52.3 L87.4 52.8 L87.6 53.2 L87.8 53.7 L87.9 54.1 L88.1 54.6 L88.3 55.0 L88.5 55.5 L88.7 55.9 L88.9 56.4 L89.1 56.8 L89.3 57.3 L89.5 57.7 L89.7 58.2 L89.9 58.6 L90.1 59.1 L90.3 59.5 L90.5 59.9 L90.7 60.4 L90.9 60.8 L91.1 61.3 L91.3 61.7 L91.5 62.2 L91.7 62.6" fill="none" stroke="#0f6e56" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="3 3"/><path d="M270.3 62.6 L270.5 62.2 L270.7 61.7 L270.9 61.3 L271.1 60.8 L271.3 60.4 L271.5 59.9 L271.7 59.5 L271.9 59.1 L272.1 58.6 L272.3 58.2 L272.5 57.7 L272.7 57.3 L272.9 56.8 L273.1 56.4 L273.3 55.9 L273.5 55.5 L273.7 55.0 L273.9 54.6 L274.1 54.1 L274.2 53.7 L274.4 53.2 L274.6 52.8 L274.8 52.3 L275.0 51.9 L275.2 51.4 L275.4 51.0 L275.6 50.5 L275.8 50.0 L276.0 49.6 L276.2 49.1 L276.4 48.7 L276.6 48.2 L276.8 47.8 L277.0 47.3 L277.2 46.8 L277.4 46.4 L277.6 45.9 L277.8 45.5 L278.0 45.0 L278.2 44.5 L278.4 44.1 L278.6 43.6 L278.8 43.1 L279.0 42.7 L279.2 42.2 L279.4 41.8 L279.6 41.3 L279.7 40.8 L279.9 40.4 L280.1 39.9 L280.3 39.4 L280.5 39.0 L280.7 38.5 L280.9 38.0 L281.1 37.5 L281.3 37.1 L281.5 36.6 L281.7 36.1 L281.9 35.7 L282.1 35.2 L282.3 34.7 L282.5 34.2 L282.7 33.8 L282.9 33.3 L283.1 32.8 L283.3 32.4 L283.5 31.9 L283.7 31.4 L283.9 30.9 L284.1 30.5 L284.3 30.0 L284.5 29.5 L284.7 29.0 L284.9 28.5 L285.1 28.1 L285.3 27.6 L285.4 27.1 L285.6 26.6 L285.8 26.2 L286.0 25.7 L286.2 25.2 L286.4 24.7 L286.6 24.2 L286.8 23.8 L287.0 23.3 L287.2 22.8 L287.4 22.3 L287.6 21.8 L287.8 21.3 L288.0 20.9 L288.2 20.4 L288.4 19.9 L288.6 19.4 L288.8 18.9 L289.0 18.4 L289.2 18.0 L289.4 17.5 L289.6 17.0 L289.8 16.5 L290.0 16.0 L290.2 15.5 L290.4 15.0 L290.6 14.5 L290.8 14.1" fill="none" stroke="#0f6e56" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="3 3"/><circle cx="91.7" cy="62.6" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="270.3" cy="62.6" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="181.0" cy="173.1" r="4" fill="#b45309" stroke="#0f172a" stroke-width="1"/><line x1="177.0" y1="173.1" x2="177.0" y2="62.6" stroke="#b45309" stroke-width="5"/><text x="167.0" y="121.8" text-anchor="end" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f(I)</text></svg>
:::

Le segment orange sur l'axe des ordonnées est l'ensemble des valeurs prises, de 0 à 1/4 : il part du minimum, et pas de f(−π/6).

::: exemple Image de [−π/6 ; π/6] par f(x) = sin²x
1. f est continue sur ℝ (composée de sin et du carré), donc sur le segment I = [−π/6 ; π/6].
2. Sur I, sin est impaire et croissante, donc |sin x| ≤ sin(π/6) = 1/2 et 0 ≤ sin²x ≤ 1/4 — on borne le carré par celui du plus grand |sin x|.
3. sin²0 = 0 est atteint en x = 0, et sin²(±π/6) = 1/4 aux deux bouts : minimum 0, maximum 1/4.
4. Donc f(I) = [0 ; 1/4].

:::

::: piege Croire que f([a ; b]) = [f(a) ; f(b)]
Ici f(−π/6) = f(π/6) = 1/4, et l'on écrirait f(I) = [1/4 ; 1/4] = {1/4}. Cela tente parce que, pour une fonction qu'on a vue croissante, on lit les images aux bouts. Mais f n'est pas monotone sur I : la courbe redescend jusqu'à 0 en x = 0. Il faut le minimum et le maximum, pas les valeurs aux bouts.
:::

::: propriete
- **Segment** : si f est continue sur [a ; b], alors f([a ; b]) = [m ; M], où m est le minimum et M le maximum de f sur [a ; b].
- **Fonction monotone** : si f est continue et strictement monotone sur I, alors f(I) est un intervalle de même nature, obtenu avec les valeurs et limites aux bornes de I :

| I | f strictement croissante | f strictement décroissante |
| --- | --- | --- |
| [a ; b] | [f(a) ; f(b)] | [f(b) ; f(a)] |
| [a ; b[ | [f(a) ; lim f en b⁻[ | ] lim f en b⁻ ; f(a)] |
| [a ; +∞[ | [f(a) ; lim f en +∞[ | ] lim f en +∞ ; f(a)] |
| ]a ; b[ | ] lim f en a⁺ ; lim f en b⁻[ | ] lim f en b⁻ ; lim f en a⁺[ |
| ]a ; b] | ] lim f en a⁺ ; f(b)] | [f(b) ; lim f en a⁺[ |

- **Limite d'une fonction monotone** (admise). Soit f définie sur [a ; b[ (b fini ou infini). Si f est croissante et majorée, f a une limite finie en b ; si elle est croissante et non majorée, f tend vers +∞ en b. Pour une fonction décroissante : limite finie si minorée, −∞ si non minorée.

Cas limite : une borne ouverte reste ouverte dans l'image, car la valeur limite est approchée sans être atteinte.
:::

::: exemple Image de I par f, pour une fonction strictement monotone
1. f(x) = x² − 2x sur I = ]−∞ ; 0] : f est strictement décroissante sur I, f(0) = 0 et lim x→−∞ f(x) = +∞, donc f(I) = [0 ; +∞[.
2. f(x) = 1/x² sur I = [1 ; +∞[ : f est strictement décroissante sur I, f(1) = 1 et lim x→+∞ f(x) = 0, donc f(I) = ]0 ; 1].
3. f(x) = sin x sur I = ]0 ; π/2[ : f est strictement croissante sur I, lim x→0⁺ f(x) = 0 et lim x→π/2⁻ f(x) = 1, donc f(I) = ]0 ; 1[.

Un usage de la limite monotone : f croissante sur [0 ; +∞[ avec f(n) = n + 1 pour tout entier n n'est pas majorée (f(n) dépasse tout réel pour n grand), donc lim x→+∞ f(x) = +∞.
:::

::: verifie
Détermine l'image de [−2 ; 1] par f(x) = x².

---

f est continue sur le segment [−2 ; 1]. Son minimum est 0, atteint en x = 0 à l'intérieur du segment ; son maximum est f(−2) = 4 (car f(1) = 1 < 4). Donc f([−2 ; 1]) = [0 ; 4]. Prendre [f(−2) ; f(1)] = [4 ; 1] n'aurait aucun sens : la fonction n'est pas monotone sur ce segment.
:::

::: retenir
f continue sur [a ; b] a pour image [m ; M] (minimum, maximum) ; si de plus f est strictement monotone, on lit l'image avec les valeurs et les limites aux bornes, et une borne ouverte le reste.
:::

> 🏆 Porte franchie, héros : tu sais lever une indétermination, coincer une limite et capturer une solution entre deux nombres, à la précision voulue. Les suites réelles t'attendent au prochain chapitre.
