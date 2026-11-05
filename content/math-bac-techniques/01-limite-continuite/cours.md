# ⚔️ Limite et continuité — la forge de l'Analyse

> 💡 «Calculer une limite, c'est savoir où va la courbe ; la continuité, c'est savoir qu'elle ne saute pas en chemin.»

Bienvenue dans l'année du Bac, section Sciences techniques. Tu sais déjà calculer la limite d'un polynôme ou d'une fraction rationnelle, appliquer les opérations sur les limites et reconnaître les formes indéterminées (∞ − ∞, 0 × ∞, ∞/∞, 0/0). Ce chapitre ajoute huit outils pour conclure quand ces règles ne suffisent plus : boucher un trou, coincer une limite, utiliser la monotonie, enchaîner deux fonctions, suivre l'image d'un intervalle, prouver qu'une équation a une solution, l'encadrer, puis décrire les bords d'une courbe.

## 🕳️ Prolongement par continuité : boucher un trou

Un logiciel trace la courbe de f(x) = (x² − x − 6)/(x − 3) et laisse un trou en x = 3, car la formule y donne 0/0. La courbe a-t-elle vraiment un trou, ou peut-on lui donner en 3 la valeur qui la recolle ?
Rappel : f est continue en x₀ lorsque lim x→x₀ f(x) = f(x₀), et les polynômes comme les fractions rationnelles sont continus en tout point où ils sont définis.

::: definition
Soit f continue en tout point d'un intervalle ouvert I, sauf peut-être en x₀. Le **prolongement par continuité** de f en x₀ est la fonction g définie sur I, continue en x₀, telle que g(x) = f(x) pour tout x de I différent de x₀.
:::

::: figure À gauche, f a un trou au point (3 ; 5) ; à droite, g est la même droite avec ce point rempli, donc continue en 3
<svg viewBox="0 0 340 180"><path d="M2.8 150 L138.8 150" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M138.8 150 l-6 -3 l0 6 z" fill="#0f172a"/><path d="M30 160.2 L30 3.8" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M30 3.8 l-3 6 l6 0 z" fill="#0f172a"/><path d="M13 133 L132 14" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M81 150 L81 65" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><path d="M30 65 L81 65" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><text x="81" y="164" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><text x="22" y="69" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><circle cx="81" cy="65" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><text x="120.1" y="112.6" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f</text><path d="M172.8 150 L308.8 150" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M308.8 150 l-6 -3 l0 6 z" fill="#0f172a"/><path d="M200 160.2 L200 3.8" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M200 3.8 l-3 6 l6 0 z" fill="#0f172a"/><path d="M183 133 L302 14" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><path d="M251 150 L251 65" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><path d="M200 65 L251 65" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><text x="251" y="164" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><text x="192" y="69" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><circle cx="251" cy="65" r="4.5" fill="#0f6e56"/><text x="290.1" y="112.6" text-anchor="middle" font-size="14" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">g</text></svg>
:::

Le point rempli de la figure est g(3) : sa hauteur 5 est la limite de f en 3, que l'exemple va calculer.

::: exemple Prolonger f(x) = (x² − x − 6)/(x − 3) en 3

1. f est définie pour x ≠ 3, et en 3 la formule donne 0/0 : forme indéterminée, il faut travailler avant de conclure.
2. x² − x − 6 = (x − 3)(x + 2) — on fait apparaître le facteur x − 3 qui annule le dénominateur.
3. Pour x ≠ 3, f(x) = x + 2 — on peut simplifier car x − 3 ≠ 0.
4. lim x→3 f(x) = lim x→3 (x + 2) = 5 — x + 2 est un polynôme, continu en 3.
5. La fonction g définie par g(x) = f(x) si x ≠ 3 et g(3) = 5 est continue en 3 : le prolongement existe.

:::

::: piege Remplacer x par 3 au numérateur seulement
On lit 3² − 3 − 6 = 0 et on écrit « f(3) = 0 », ou bien « 0/0, donc pas de prolongement ». Cela tente parce que le numérateur s'annule. Mais 0/0 est une forme indéterminée : elle ne dit rien. Après simplification, la limite vaut 5, et c'est elle qu'on pose pour f(3).
:::

::: propriete
f, continue sur I sauf peut-être en x₀, se prolonge par continuité en x₀ si et seulement si lim x→x₀ f(x) existe et est un réel ℓ. Le prolongement est alors g(x₀) = ℓ.

Cas limite : si la limite est infinie (comme celle de 1/x en 0) ou n'existe pas, il n'y a pas de prolongement.

Limites usuelles en 0, pour lever un 0/0 : lim sin(ax)/x = a (donc sin x/x → 1), lim (1 − cos x)/x = 0 et lim (1 − cos x)/x² = 1/2. Ainsi sin(3x)/x se prolonge en 0 par la valeur 3.
:::

::: verifie
Soit f(x) = (2x² − 2)/(x + 1) pour x ≠ −1. Se prolonge-t-elle par continuité en −1, et avec quelle valeur ?

---

2x² − 2 = 2(x − 1)(x + 1), donc f(x) = 2(x − 1) pour x ≠ −1, et la limite en −1 est 2 × (−2) = −4, un réel : on pose f(−1) = −4. Remplacer x par −1 au seul numérateur aurait donné 0, valeur fausse.
:::

::: retenir
Un trou de la forme 0/0 se bouche quand la limite ℓ est finie : on simplifie, on calcule ℓ, puis on pose g(x₀) = ℓ.
:::

## 🥪 Limite et ordre : coincer pour conclure

Un élève marche entre deux surveillants qui rejoignent la même porte : il reste toujours entre eux, où arrive-t-il ? De même, f(x) = x² sin(1/x) oscille sans fin près de 0 et sin(1/x) n'a pas de limite en 0. Peut-on pourtant conclure sur f ?

::: figure La courbe de f oscille, mais reste enfermée entre les paraboles y = −x² et y = x², qui se rejoignent en 0
<svg viewBox="0 0 340 200"><path d="M4.4 100 L335.6 100" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M335.6 100 l-6 -3 l0 6 z" fill="#0f172a"/><path d="M170 192 L170 8" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M170 8 l-3 6 l6 0 z" fill="#0f172a"/><path d="M27.4 11.6 L32 17.2 L36.6 22.6 L41.2 27.9 L45.8 32.9 L50.4 37.8 L55 42.5 L59.6 47 L64.2 51.3 L68.8 55.5 L73.4 59.4 L78 63.2 L82.6 66.8 L87.2 70.2 L91.8 73.4 L96.4 76.4 L101 79.3 L105.6 82 L110.2 84.5 L114.8 86.8 L119.4 88.9 L124 90.8 L128.6 92.5 L133.2 94.1 L137.8 95.5 L142.4 96.7 L147 97.7 L151.6 98.5 L156.2 99.2 L160.8 99.6 L165.4 99.9 L170 100 L174.6 99.9 L179.2 99.6 L183.8 99.2 L188.4 98.5 L193 97.7 L197.6 96.7 L202.2 95.5 L206.8 94.1 L211.4 92.5 L216 90.8 L220.6 88.9 L225.2 86.8 L229.8 84.5 L234.4 82 L239 79.3 L243.6 76.4 L248.2 73.4 L252.8 70.2 L257.4 66.8 L262 63.2 L266.6 59.4 L271.2 55.5 L275.8 51.3 L280.4 47 L285 42.5 L289.6 37.8 L294.2 32.9 L298.8 27.9 L303.4 22.6 L308 17.2 L312.6 11.6" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="5 3"/><path d="M27.4 188.4 L32 182.8 L36.6 177.4 L41.2 172.1 L45.8 167.1 L50.4 162.2 L55 157.5 L59.6 153 L64.2 148.7 L68.8 144.5 L73.4 140.6 L78 136.8 L82.6 133.2 L87.2 129.8 L91.8 126.6 L96.4 123.6 L101 120.7 L105.6 118 L110.2 115.5 L114.8 113.2 L119.4 111.1 L124 109.2 L128.6 107.5 L133.2 105.9 L137.8 104.5 L142.4 103.3 L147 102.3 L151.6 101.5 L156.2 100.8 L160.8 100.4 L165.4 100.1 L170 100 L174.6 100.1 L179.2 100.4 L183.8 100.8 L188.4 101.5 L193 102.3 L197.6 103.3 L202.2 104.5 L206.8 105.9 L211.4 107.5 L216 109.2 L220.6 111.1 L225.2 113.2 L229.8 115.5 L234.4 118 L239 120.7 L243.6 123.6 L248.2 126.6 L252.8 129.8 L257.4 133.2 L262 136.8 L266.6 140.6 L271.2 144.5 L275.8 148.7 L280.4 153 L285 157.5 L289.6 162.2 L294.2 167.1 L298.8 172.1 L303.4 177.4 L308 182.8 L312.6 188.4" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="5 3"/><path d="M27.4 188.3 L32.5 181.8 L37.3 175.6 L41.7 169.8 L45.9 164.3 L49.8 159.2 L53.4 154.4 L56.9 149.8 L60.1 145.5 L63.2 141.4 L66.1 137.6 L68.8 134 L71.4 130.6 L73.9 127.3 L76.2 124.3 L78.5 121.4 L80.6 118.7 L82.6 116.2 L84.6 113.8 L86.5 111.5 L88.2 109.4 L89.9 107.4 L91.6 105.5 L93.2 103.8 L94.7 102.2 L96.1 100.7 L97.5 99.3 L98.9 98 L100.2 96.8 L101.4 95.7 L102.6 94.7 L103.8 93.8 L104.9 93 L106 92.2 L107 91.6 L108.1 91 L109 90.5 L110 90 L110.9 89.6 L111.8 89.3 L112.7 89.1 L113.5 88.9 L114.3 88.7 L115.1 88.6 L115.9 88.6 L116.7 88.6 L117.4 88.7 L118.1 88.7 L118.8 88.9 L119.5 89 L120.1 89.2 L120.8 89.5 L121.4 89.7 L122 90 L122.6 90.3 L123.2 90.7 L123.7 91 L124.3 91.4 L124.8 91.8 L125.4 92.2 L125.9 92.6 L126.4 93 L126.9 93.4 L127.4 93.9 L127.8 94.3 L128.3 94.7 L128.7 95.2 L129.2 95.6 L129.6 96 L130 96.5 L130.4 96.9 L130.8 97.3 L131.2 97.8 L131.6 98.2 L132 98.6 L132.4 99 L132.7 99.3 L133.1 99.7 L133.5 100.1 L133.8 100.4 L134.1 100.7 L134.5 101 L134.8 101.3 L135.1 101.6 L135.4 101.9 L135.7 102.1 L136 102.4 L136.3 102.6 L136.6 102.8 L136.9 103 L137.2 103.1 L137.5 103.3 L137.8 103.4 L138 103.5 L138.3 103.6 L138.5 103.7 L138.8 103.8 L139.1 103.8 L139.3 103.8 L139.5 103.9 L139.8 103.9 L140 103.8 L140.3 103.8 L140.5 103.8 L140.7 103.7 L140.9 103.7 L141.2 103.6 L141.4 103.5 L141.6 103.4 L141.8 103.3 L142 103.2 L142.2 103.1 L142.4 102.9 L142.6 102.8 L142.8 102.7 L143 102.5 L143.2 102.4 L143.4 102.2 L143.5 102 L143.7 101.9 L143.9 101.7 L144.1 101.5 L144.3 101.4 L144.4 101.2 L144.6 101 L144.8 100.8 L144.9 100.7 L145.1 100.5 L145.2 100.4 L145.4 100.2 L145.6 100 L145.7 99.9 L145.9 99.7 L146 99.6 L146.2 99.4 L146.3 99.3 L146.5 99.2 L146.6 99.1 L146.8 98.9 L146.9 98.8 L147 98.7 L147.2 98.6 L147.3 98.5 L147.4 98.5 L147.6 98.4 L147.7 98.3 L147.8 98.3 L148 98.2 L148.1 98.2 L148.2 98.1 L148.3 98.1 L148.5 98.1 L148.6 98.1 L148.7 98.1 L148.8 98.1 L148.9 98.1 L149 98.1 L149.2 98.1 L149.3 98.1 L149.4 98.2 L149.5 98.2 L149.6 98.3 L149.7 98.3 L149.8 98.4 L149.9 98.4 L150 98.5 L150.1 98.6 L150.2 98.6 L150.3 98.7 L150.4 98.8 L150.5 98.9 L150.6 99 L150.7 99 L150.8 99.1 L150.9 99.2 L151.4 99.7 L151.8 100.1 L152.2 100.5 L152.6 100.8 L153 101 L153.4 101.2 L153.7 101.1 L154.1 101 L154.4 100.9 L154.7 100.6 L155 100.3 L155.3 100.1 L155.6 99.8 L155.8 99.5 L156.1 99.4 L156.4 99.3 L156.6 99.2 L156.8 99.3 L157 99.4 L157.3 99.5 L157.5 99.7 L157.7 99.9 L157.9 100.1 L158.1 100.2 L158.2 100.4 L158.4 100.5 L158.6 100.5 L158.8 100.5 L158.9 100.5 L159.1 100.4 L159.2 100.3 L159.4 100.2 L159.5 100 L159.7 99.9 L159.8 99.8 L159.9 99.7 L160.1 99.6 L160.2 99.6 L160.3 99.6 L160.4 99.6 L160.6 99.7 L160.7 99.8 L160.8 99.9 L160.9 100 L161 100.1 L161.1 100.2 L161.2 100.3 L161.3 100.3 L161.4 100.3 L161.5 100.3 L161.6 100.2 L161.7 100.2 L161.8 100.1 L161.9 100 L161.9 99.9 L162 99.8 L162.1 99.8 L162.2 99.8 L162.3 99.7 L162.3 99.8 L162.4 99.8 L162.5 99.8 L162.6 99.9 L162.6 100 L162.7 100 L162.8 100.1 L162.8 100.1 L162.9 100.2 L163 100.2 L163 100.2 L163.1 100.2 L163.2 100.2 L163.2 100.1 L163.3 100.1 L163.3 100 L163.4 99.9 L163.5 99.9 L163.5 99.9 L163.6 99.8 L163.6 99.8 L163.7 99.8 L163.7 99.9 L163.8 99.9 L163.8 99.9 L163.9 100 L163.9 100 L164 100.1 L164 100.1 L164.1 100.1 L164.1 100.1 L164.2 100.1 L164.2 100.1 L164.2 100.1 L170 100 L175.8 99.9 L175.8 99.9 L175.8 99.9 L175.9 99.9 L175.9 99.9 L176 99.9 L176 99.9 L176.1 100 L176.1 100 L176.2 100.1 L176.2 100.1 L176.3 100.1 L176.3 100.2 L176.4 100.2 L176.4 100.2 L176.5 100.1 L176.5 100.1 L176.6 100.1 L176.7 100 L176.7 99.9 L176.8 99.9 L176.8 99.8 L176.9 99.8 L177 99.8 L177 99.8 L177.1 99.8 L177.2 99.9 L177.2 99.9 L177.3 100 L177.4 100 L177.4 100.1 L177.5 100.2 L177.6 100.2 L177.7 100.2 L177.7 100.3 L177.8 100.2 L177.9 100.2 L178 100.2 L178.1 100.1 L178.1 100 L178.2 99.9 L178.3 99.8 L178.4 99.8 L178.5 99.7 L178.6 99.7 L178.7 99.7 L178.8 99.7 L178.9 99.8 L179 99.9 L179.1 100 L179.2 100.1 L179.3 100.2 L179.4 100.3 L179.6 100.4 L179.7 100.4 L179.8 100.4 L179.9 100.4 L180.1 100.3 L180.2 100.2 L180.3 100.1 L180.5 100 L180.6 99.8 L180.8 99.7 L180.9 99.6 L181.1 99.5 L181.2 99.5 L181.4 99.5 L181.6 99.5 L181.8 99.6 L181.9 99.8 L182.1 99.9 L182.3 100.1 L182.5 100.3 L182.7 100.5 L183 100.6 L183.2 100.7 L183.4 100.8 L183.6 100.7 L183.9 100.6 L184.2 100.5 L184.4 100.2 L184.7 99.9 L185 99.7 L185.3 99.4 L185.6 99.1 L185.9 99 L186.3 98.9 L186.6 98.8 L187 99 L187.4 99.2 L187.8 99.5 L188.2 99.9 L188.6 100.3 L189.1 100.8 L189.2 100.9 L189.3 101 L189.4 101 L189.5 101.1 L189.6 101.2 L189.7 101.3 L189.8 101.4 L189.9 101.4 L190 101.5 L190.1 101.6 L190.2 101.6 L190.3 101.7 L190.4 101.7 L190.5 101.8 L190.6 101.8 L190.7 101.9 L190.8 101.9 L191 101.9 L191.1 101.9 L191.2 101.9 L191.3 101.9 L191.4 101.9 L191.5 101.9 L191.7 101.9 L191.8 101.9 L191.9 101.8 L192 101.8 L192.2 101.7 L192.3 101.7 L192.4 101.6 L192.6 101.5 L192.7 101.5 L192.8 101.4 L193 101.3 L193.1 101.2 L193.2 101.1 L193.4 100.9 L193.5 100.8 L193.7 100.7 L193.8 100.6 L194 100.4 L194.1 100.3 L194.3 100.1 L194.4 100 L194.6 99.8 L194.8 99.6 L194.9 99.5 L195.1 99.3 L195.2 99.2 L195.4 99 L195.6 98.8 L195.7 98.6 L195.9 98.5 L196.1 98.3 L196.3 98.1 L196.5 98 L196.6 97.8 L196.8 97.6 L197 97.5 L197.2 97.3 L197.4 97.2 L197.6 97.1 L197.8 96.9 L198 96.8 L198.2 96.7 L198.4 96.6 L198.6 96.5 L198.8 96.4 L199.1 96.3 L199.3 96.3 L199.5 96.2 L199.7 96.2 L200 96.2 L200.2 96.1 L200.5 96.1 L200.7 96.2 L200.9 96.2 L201.2 96.2 L201.5 96.3 L201.7 96.4 L202 96.5 L202.2 96.6 L202.5 96.7 L202.8 96.9 L203.1 97 L203.4 97.2 L203.7 97.4 L204 97.6 L204.3 97.9 L204.6 98.1 L204.9 98.4 L205.2 98.7 L205.5 99 L205.9 99.3 L206.2 99.6 L206.5 99.9 L206.9 100.3 L207.3 100.7 L207.6 101 L208 101.4 L208.4 101.8 L208.8 102.2 L209.2 102.7 L209.6 103.1 L210 103.5 L210.4 104 L210.8 104.4 L211.3 104.8 L211.7 105.3 L212.2 105.7 L212.6 106.1 L213.1 106.6 L213.6 107 L214.1 107.4 L214.6 107.8 L215.2 108.2 L215.7 108.6 L216.3 109 L216.8 109.3 L217.4 109.7 L218 110 L218.6 110.3 L219.2 110.5 L219.9 110.8 L220.5 111 L221.2 111.1 L221.9 111.3 L222.6 111.3 L223.3 111.4 L224.1 111.4 L224.9 111.4 L225.7 111.3 L226.5 111.1 L227.3 110.9 L228.2 110.7 L229.1 110.4 L230 110 L231 109.5 L231.9 109 L233 108.4 L234 107.8 L235.1 107 L236.2 106.2 L237.4 105.3 L238.6 104.3 L239.8 103.2 L241.1 102 L242.5 100.7 L243.9 99.3 L245.3 97.8 L246.8 96.2 L248.4 94.5 L250.1 92.6 L251.8 90.6 L253.5 88.5 L255.4 86.2 L257.4 83.8 L259.4 81.3 L261.5 78.6 L263.8 75.7 L266.1 72.7 L268.6 69.4 L271.2 66 L273.9 62.4 L276.8 58.6 L279.9 54.5 L283.1 50.2 L286.6 45.6 L290.2 40.8 L294.1 35.7 L298.3 30.2 L302.7 24.4 L307.5 18.2 L312.6 11.7" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="170" cy="100" r="3.5" fill="#0f172a"/><text x="289.6" y="14.9" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = x²</text><text x="289.6" y="195.1" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = −x²</text><text x="124" y="82.8" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f</text></svg>
:::

Les deux paraboles en pointillé jouent le rôle des surveillants : leur limite commune en 0 est 0.

::: exemple Limite en 0 de f(x) = x² sin(1/x)

1. Pour x ≠ 0, −1 ≤ sin(1/x) ≤ 1 — un sinus reste toujours entre −1 et 1.
2. −x² ≤ f(x) ≤ x² — on multiplie par x² ≥ 0, ce qui garde le sens des inégalités.
3. lim x→0 (−x²) = 0 et lim x→0 x² = 0 — deux polynômes, continus en 0.
4. lim x→0 f(x) = 0 — f est coincée entre deux fonctions de même limite.

:::

::: piege Croire qu'une inégalité stricte reste stricte à la limite
Pour 0 < |x| < 1, on a x² < |x| ; pourtant lim x→0 x² = lim x→0 |x| = 0 : les deux limites sont égales. En passant à la limite, « < » devient « ≤ » : si f(x) < g(x), alors lim f ≤ lim g, jamais lim f < lim g.
:::

::: propriete
Soit f, g, h définies sur un intervalle ouvert I, sauf peut-être en x₀ ; les inégalités valent pour tout x ≠ x₀ de I.

- **Gendarmes** : si h(x) ≤ f(x) ≤ g(x) et lim h = lim g = ℓ, alors lim f = ℓ.
- **Distance** : si |f(x) − ℓ| ≤ |g(x)| et lim g = 0, alors lim f = ℓ.
- **Infini** : si f(x) ≥ g(x) et lim g = +∞, alors lim f = +∞ ; si f(x) ≤ g(x) et lim g = −∞, alors lim f = −∞.
- **Ordre** : si f(x) ≤ g(x), lim f = ℓ et lim g = ℓ', alors ℓ ≤ ℓ'.

Ces résultats restent vrais quand x tend vers x₀⁺, x₀⁻, +∞ ou −∞. Exemple : 2x + 3 sin x ≥ 2x − 3 et lim x→+∞ (2x − 3) = +∞, donc lim x→+∞ (2x + 3 sin x) = +∞.

Cas limite : si les deux bornes n'ont pas la même limite (ou si l'une n'en a pas), l'encadrement ne conclut rien.
:::

::: verifie
Calcule lim x→+∞ cos x/(x + 1).

---

cos x n'a pas de limite en +∞, le quotient des limites est donc inutilisable. Pour x > 0, |cos x| ≤ 1 donne |f(x)| ≤ 1/(x + 1), et lim x→+∞ 1/(x + 1) = 0 ; par la règle de la distance avec ℓ = 0, lim x→+∞ cos x/(x + 1) = 0.
:::

::: retenir
Quand on ne sait pas calculer f, on la coince : deux bornes de même limite ℓ imposent lim f = ℓ, une borne qui tend vers ±∞ entraîne f, et une inégalité stricte devient large.
:::

## 💧 Fonctions monotones et limites : l'eau qui monte

Une cuve se remplit sans jamais se vider. Au bout de t heures, le niveau est N(t) = 2 − 1/(1 + t) mètres, pour t ≥ 0.
Il monte tout le temps. Dépasse-t-il tout niveau, ou se rapproche-t-il d'un plafond ?

::: definition
Soit f définie sur un intervalle I. f est **majorée** sur I s'il existe un réel M tel que f(x) ≤ M pour tout x de I ; **minorée** s'il existe un réel m tel que m ≤ f(x) pour tout x de I ; **bornée** si elle est majorée et minorée. f est **monotone** sur I si elle est croissante ou décroissante sur I.
:::

::: figure Le niveau N(t) monte sans cesse, mais reste sous la droite y = 2 : il se rapproche d'un plafond
<svg viewBox="0 0 340 200"><path d="M26.4 170 L332.4 170" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M332.4 170 l-6 -3 l0 6 z" fill="#0f172a"/><path d="M40 182 L40 14" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M40 14 l-3 6 l6 0 z" fill="#0f172a"/><path d="M40 50 L322.2 50" fill="none" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="6 4"/><path d="M40 110 L43.5 104.4 L47 99.8 L50.5 95.9 L53.9 92.6 L57.4 89.7 L60.9 87.2 L64.4 84.9 L67.9 83 L71.4 81.2 L74.8 79.6 L78.3 78.2 L81.8 76.9 L85.3 75.7 L88.8 74.6 L92.3 73.6 L95.8 72.7 L99.2 71.9 L102.7 71.1 L106.2 70.4 L109.7 69.7 L113.2 69 L116.7 68.4 L120.2 67.9 L123.6 67.3 L127.1 66.8 L130.6 66.4 L134.1 65.9 L137.6 65.5 L141.1 65.1 L144.6 64.7 L148 64.4 L151.5 64 L155 63.7 L158.5 63.4 L162 63.1 L165.5 62.8 L168.9 62.5 L172.4 62.3 L175.9 62 L179.4 61.8 L182.9 61.5 L186.4 61.3 L189.9 61.1 L193.3 60.9 L196.8 60.7 L200.3 60.5 L203.8 60.3 L207.3 60.1 L210.8 60 L214.2 59.8 L217.7 59.6 L221.2 59.5 L224.7 59.3 L228.2 59.2 L231.7 59 L235.2 58.9 L238.6 58.8 L242.1 58.6 L245.6 58.5 L249.1 58.4 L252.6 58.3 L256.1 58.2 L259.6 58 L263 57.9 L266.5 57.8 L270 57.7 L273.5 57.6 L277 57.5 L280.5 57.4 L283.9 57.3 L287.4 57.2 L290.9 57.2 L294.4 57.1 L297.9 57 L301.4 56.9 L304.9 56.8 L308.3 56.7 L311.8 56.7 L315.3 56.6 L318.8 56.5" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><text x="32" y="54" text-anchor="end" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="32" y="114" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><circle cx="40" cy="110" r="3.5" fill="#0f172a"/><text x="278" y="72.8" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N</text><text x="108" y="184" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="176" y="184" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><text x="244" y="184" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="312" y="184" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><text x="329" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t</text></svg>
:::

La droite pointillée y = 2 est le réel M de la définition : N(t) < 2 pour tout t.

::: exemple Limite en +∞ de N(t) = 2 − 1/(1 + t)

1. N est croissante : si 0 ≤ s < t, alors 1/(1 + s) > 1/(1 + t), donc N(s) = 2 − 1/(1 + s) < 2 − 1/(1 + t) = N(t) — l'inverse de nombres positifs renverse l'ordre.
2. N est majorée par 2 : 1/(1 + t) > 0, donc N(t) < 2 — on retire un nombre positif à 2.
3. Croissante et majorée sur [0 ; +∞[, N a une limite finie ℓ en +∞ — c'est le théorème ci-dessous.
4. lim t→+∞ 1/(1 + t) = 0, donc ℓ = 2 — la limite est le plafond, jamais dépassé.
5. Autre cas : u(x) = 1/(1 − x) sur [0 ; 1[ est croissante (1 − x diminue, son inverse augmente) et non majorée (u(x) > 100 dès que x > 0,99), donc lim x→1⁻ u(x) = +∞.

:::

::: piege Croire que croissante veut dire « tend vers +∞ »
N est croissante, et pourtant sa limite est 2. Cela tente parce qu'elle monte tout le temps. Une fonction croissante tend vers +∞ seulement si elle est non majorée ; sinon sa limite est finie.
:::

::: propriete
Soit f définie sur I = ]a ; b[ (ou ]a ; +∞[).

- Si f est croissante et non majorée sur I, alors lim f = +∞ en b⁻ (ou en +∞).
- Si f est décroissante et non minorée sur I, alors lim f = −∞ en b⁻ (ou en +∞).
- Si f est croissante et majorée (ou décroissante et minorée) sur I, alors f a une limite finie en b⁻ (ou en +∞).

Cas limite : dans le cas fini, la limite existe et ℓ ≤ M pour un majorant M, mais ℓ n'est pas forcément M : N est aussi majorée par 5, sa limite reste 2.
:::

::: verifie
g(x) = 4 − 2/(x + 1) est croissante sur [0 ; +∞[ (même raisonnement que pour N). Que dit le théorème sur sa limite en +∞ ? Calcule-la.

---

g(x) < 4 car on retire 2/(x + 1) > 0 : g est croissante et majorée, donc elle a une limite finie en +∞. Comme lim x→+∞ 2/(x + 1) = 0, cette limite est 4. Le nombre 6 est aussi un majorant de g, mais ce n'est pas la limite.
:::

::: retenir
Croissante et majorée (ou décroissante et minorée) : limite finie ; croissante et non majorée : +∞ ; décroissante et non minorée : −∞.
:::

## 🔗 Limite d'une composée : deux machines à la chaîne

Une première machine transforme x en 9x², une seconde transforme y en √y. Quand l'entrée x approche −2, la première sort des nombres proches de 36, donc la seconde reçoit des nombres proches de 36.
Que sort la chaîne, et peut-on le lire sans refaire tout le calcul ?

::: definition
Soit f définie sur I et g définie sur J, avec f(x) dans J pour tout x de I. La **composée** de f par g est la fonction g∘f (« g rond f ») définie sur I par (g∘f)(x) = g(f(x)).
:::

| x                | −2,1  | −2,01   | −2,001    |
| ---------------- | ----- | ------- | --------- |
| f(x) = 9x²       | 39,69 | 36,3609 | 36,036009 |
| g(f(x)) = √(9x²) | 6,3   | 6,03    | 6,003     |

Quand x tend vers −2, la ligne de f tend vers 36 et la ligne de g∘f tend vers 6 = √36 : la sortie de la chaîne est g appliquée à la limite de f.

::: exemple Limite en −2 de √(9x²)

1. f(x) = 9x² et g(y) = √y, donc √(9x²) = g(f(x)).
2. lim x→−2 9x² = 36 — un polynôme est continu.
3. g est continue en 36 — la racine est continue sur [0 ; +∞[.
4. lim x→−2 √(9x²) = g(36) = 6.

:::

::: exemple Un cas infini : limite en 1⁻ de √((1 + x)/(1 − x))

1. Pour x < 1, (1 + x)/(1 − x) a un numérateur proche de 2 et un dénominateur proche de 0⁺ : sa limite en 1⁻ est +∞.
2. lim y→+∞ √y = +∞ — la racine croît sans borne.
3. lim x→1⁻ √((1 + x)/(1 − x)) = +∞ — la limite de g en ℓ = +∞ donne celle de la composée.

:::

::: piege Simplifier √(9x²) en 3x
Cela tente parce que « √(a²) = a ». Mais pour x = −2, 3x = −6 alors que √(9 × 4) = 6 : une racine est toujours positive, et √(9x²) = 3|x|. La limite en −2 est bien 3 × 2 = 6, pas −6.
:::

::: propriete
Soit f définie sur I, g définie sur J, avec f(x) dans J.

- Si lim f = ℓ et si g est continue en ℓ, alors lim g∘f = g(ℓ).
- Plus généralement, si lim f = ℓ et lim y→ℓ g(y) = ℓ', alors lim g∘f = ℓ', où x₀, ℓ et ℓ' peuvent être finis ou infinis.
- Si f est continue en x₀ et g continue en f(x₀), alors g∘f est continue en x₀. En particulier, √f est continue si f est continue et positive, et |f| est continue si f l'est.
- Changement de variable : lim x→+∞ f(x) existe si et seulement si lim x→0⁺ f(1/x) existe, et elles sont égales (de même −∞ et 0⁻).

Exemple : en posant X = 1/x, x sin(1/x) = sin X / X, qui tend vers 1 quand x → +∞ (X → 0⁺).

Cas limite : si g n'est pas continue en ℓ, la première règle tombe ; il faut alors la limite de g en ℓ.
:::

::: verifie
Calcule lim x→+∞ √((4x + 1)/(x + 1)).

---

La fraction intérieure a pour limite 4 (quotient des termes de plus haut degré : 4x/x = 4). La racine est continue en 4, donc la limite cherchée est √4 = 2.
:::

::: retenir
On calcule la limite de l'intérieur f, puis on applique g : si g est continue en ℓ, le résultat est g(ℓ) ; sinon on utilise la limite de g en ℓ, même infinie.
:::

## 📏 Continuité sur un intervalle et image d'un intervalle

Un capteur mesure une grandeur qui varie sans saut : f(x) = x² − 2x, pour x de −1 à 3. Les deux extrémités donnent la même mesure, 3.
L'ensemble des valeurs prises par le capteur est-il réduit à {3} ? Quelles valeurs prend-il en tout ?

::: definition
f est **continue sur un intervalle** si elle est continue en tout point de cet intervalle ; sur [a ; b], cela signifie continue sur ]a ; b[, continue à droite en a et continue à gauche en b. L'**image** d'un intervalle I par f est l'ensemble f(I) = {f(x) ; x ∈ I} des valeurs prises par f sur I.
:::

::: figure Sur [−1 ; 3], les valeurs prises par f (bande verte sur l'axe des ordonnées) vont de son minimum −1 à son maximum 3
<svg viewBox="0 0 340 215"><path d="M28.8 150 L323.2 150" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M323.2 150 l-6 -3 l0 6 z" fill="#0f172a"/><path d="M130 211.2 L130 0.4" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M130 0.4 l-3 6 l6 0 z" fill="#0f172a"/><path d="M84 48 L87.1 56.9 L90.1 65.5 L93.2 73.8 L96.3 81.8 L99.3 89.6 L102.4 97 L105.5 104.1 L108.5 110.9 L111.6 117.4 L114.7 123.6 L117.7 129.4 L120.8 135 L123.9 140.3 L126.9 145.3 L130 150 L133.1 154.4 L136.1 158.5 L139.2 162.2 L142.3 165.7 L145.3 168.9 L148.4 171.8 L151.5 174.3 L154.5 176.6 L157.6 178.6 L160.7 180.2 L163.7 181.6 L166.8 182.6 L169.9 183.4 L172.9 183.8 L176 184 L179.1 183.8 L182.1 183.4 L185.2 182.6 L188.3 181.6 L191.3 180.2 L194.4 178.6 L197.5 176.6 L200.5 174.3 L203.6 171.8 L206.7 168.9 L209.7 165.7 L212.8 162.2 L215.9 158.5 L218.9 154.4 L222 150 L225.1 145.3 L228.1 140.3 L231.2 135 L234.3 129.4 L237.3 123.6 L240.4 117.4 L243.5 110.9 L246.5 104.1 L249.6 97 L252.7 89.6 L255.7 81.8 L258.8 73.8 L261.9 65.5 L264.9 56.9 L268 48" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><path d="M84 48 L130 48" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><path d="M268 48 L130 48" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><path d="M176 184 L130 184" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><path d="M176 150 L176 184" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><path d="M84 150 L84 48" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><path d="M268 150 L268 48" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><path d="M130 184 L130 48" stroke="#0f6e56" stroke-width="6" stroke-linecap="round" opacity="0.35" fill="none"/><circle cx="84" cy="48" r="4" fill="#0f172a"/><circle cx="176" cy="184" r="4" fill="#0f172a"/><circle cx="268" cy="48" r="4" fill="#0f172a"/><text x="122" y="52" text-anchor="end" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><text x="122" y="188" text-anchor="end" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><text x="82" y="165" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><text x="176" y="143" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="268" y="165" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><text x="247.3" y="85.4" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f</text></svg>
:::

Le point le plus bas de la courbe, d'ordonnée −1, donne le bas de la bande ; les deux extrémités de la courbe, d'ordonnée 3, donnent le haut : f([−1 ; 3]) = [−1 ; 3].

::: exemple Image de [−1 ; 3] par f(x) = x² − 2x

1. f est un polynôme, donc continue sur [−1 ; 3] : f([−1 ; 3]) est un intervalle fermé [m ; M] — théorème ci-dessous.
2. f(x) = (x − 1)² − 1 ≥ −1, avec égalité en x = 1 qui est dans [−1 ; 3] — un carré est positif ; donc m = −1.
3. f(x) − 3 = x² − 2x − 3 = (x + 1)(x − 3) ≤ 0 sur [−1 ; 3], avec égalité en −1 et en 3 — un facteur positif fois un facteur négatif ; donc M = 3.
4. f([−1 ; 3]) = [−1 ; 3].

:::

::: piege Écrire f([a ; b]) = [f(a) ; f(b)]
Ici, cela donnerait [3 ; 3] = {3}. Cela tente parce que les extrémités sont les valeurs faciles à calculer. Mais la courbe descend jusqu'à −1 en x = 1 avant de remonter : rien n'oblige le minimum et le maximum à être atteints aux extrémités. L'égalité f([a ; b]) = [f(a) ; f(b)] est garantie quand f est croissante, pas en général.
:::

::: propriete

- L'image d'un intervalle par une fonction continue est un intervalle.
- L'image de [a ; b] par une fonction continue f est [m ; M], où m et M sont le minimum et le maximum de f sur [a ; b]. Si f est croissante sur [a ; b], c'est [f(a) ; f(b)] ; si elle est décroissante, c'est [f(b) ; f(a)].

Les polynômes, les fractions rationnelles, √ et leurs composées sont continus sur leurs intervalles de définition, par exemple x ↦ √(1 − x²) sur [−1 ; 1].

Cas limite : sans continuité, l'image peut ne pas être un intervalle. Avec h(x) = x si x ≤ 1 et h(x) = x + 2 si x > 1 (un saut en 1), h(ℝ) = ]−∞ ; 1] ∪ ]3 ; +∞[ : les valeurs de 1 à 3 manquent.
:::

::: verifie
Détermine l'image de [0 ; 3] par g(x) = −x² + 2x.

---

g est un polynôme, continu sur [0 ; 3] ; son image est [m ; M]. g(x) = 1 − (x − 1)² ≤ 1, avec égalité en x = 1 qui est dans [0 ; 3] : M = 1. g(x) + 3 = −(x − 3)(x + 1) ≥ 0 sur [0 ; 3], avec égalité en 3 : m = −3. Donc g([0 ; 3]) = [−3 ; 1], et non [g(3) ; g(0)] = [−3 ; 0].
:::

::: retenir
L'image d'un intervalle par une fonction continue est un intervalle ; sur [a ; b], c'est [minimum ; maximum], pas toujours [f(a) ; f(b)].
:::

## 🎯 Théorème des valeurs intermédiaires : une solution existe

À 8 h, un thermomètre à lecture continue indique −2 °C ; à 12 h, il indique 7 °C. A-t-il affiché exactement 0 °C dans l'intervalle ? Et une seule fois ?

::: figure Une courbe continue qui passe de −2 en a = 1 à 7 en b = 2 coupe forcément l'axe des abscisses : au point d'abscisse c
<svg viewBox="0 0 340 235"><path d="M40 125 L299 125" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M299 125 l-6 -3 l0 6 z" fill="#0f172a"/><path d="M40 170 L40 17" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M40 17 l-3 6 l6 0 z" fill="#0f172a"/><path d="M47 162.3 L50.3 161.6 L53.6 160.9 L56.9 160.2 L60.2 159.4 L63.5 158.7 L66.8 157.9 L70.1 157 L73.4 156.2 L76.7 155.3 L80 154.4 L83.3 153.5 L86.6 152.6 L89.9 151.6 L93.2 150.6 L96.5 149.6 L99.8 148.5 L103.1 147.4 L106.4 146.3 L109.7 145.1 L113 143.9 L116.3 142.7 L119.6 141.4 L122.9 140.1 L126.2 138.8 L129.5 137.4 L132.8 136 L136.1 134.6 L139.4 133.1 L142.7 131.6 L146 130 L149.3 128.4 L152.6 126.7 L155.9 125 L159.2 123.3 L162.5 121.5 L165.8 119.7 L169.1 117.8 L172.4 115.9 L175.7 113.9 L179 111.9 L182.3 109.8 L185.6 107.7 L188.9 105.5 L192.2 103.3 L195.5 101 L198.8 98.7 L202.1 96.3 L205.4 93.8 L208.7 91.3 L212 88.8 L215.3 86.2 L218.6 83.5 L221.9 80.8 L225.2 78 L228.5 75.1 L231.8 72.2 L235.1 69.2 L238.4 66.2 L241.7 63.1 L245 59.9 L248.3 56.7 L251.6 53.4 L254.9 50 L258.2 46.6 L261.5 43.1 L264.8 39.5 L268.1 35.9 L271.4 32.2 L274.7 28.4 L278 24.5" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><path d="M110 125 L110 145" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><path d="M110 145 L40 145" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><path d="M250 125 L250 55" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><path d="M250 55 L40 55" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><path d="M156 125 L156 125" fill="none" stroke="#0f6e56" stroke-width="1.2" stroke-dasharray="4 3"/><circle cx="110" cy="145" r="4" fill="#0f172a"/><circle cx="250" cy="55" r="4" fill="#0f172a"/><circle cx="156" cy="125" r="5" fill="#0f6e56"/><text x="34" y="149" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><text x="34" y="59" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7</text><text x="110" y="117" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">a = 1</text><text x="250" y="141" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">b = 2</text><text x="164" y="141" text-anchor="middle" font-size="14" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">c</text><text x="187" y="45" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f</text></svg>
:::

Le point d'abscisse c, où la courbe rencontre l'axe, est une solution de f(x) = 0 : c'est ce que le théorème garantit, sans la calculer.

::: exemple Résoudre x³ + 2x − 5 = 0 dans ]1 ; 2[

On pose f(x) = x³ + 2x − 5.

1. f est un polynôme, donc continue sur [1 ; 2].
2. f(1) = 1 + 2 − 5 = −2 et f(2) = 8 + 4 − 5 = 7, donc f(1) × f(2) = −14 < 0 — les signes sont opposés.
3. 0 est compris entre −2 et 7, donc il existe c dans ]1 ; 2[ tel que f(c) = 0 — c'est le corollaire 1 ci-dessous.
4. x ↦ x³ et x ↦ 2x sont strictement croissantes, donc f l'est aussi — une somme de fonctions strictement croissantes est strictement croissante.
5. Une fonction strictement croissante prend chaque valeur une seule fois : c est l'unique solution dans ]1 ; 2[.

:::

::: piege Lire le corollaire à l'envers
« f(a) × f(b) > 0, donc pas de solution. » Cela tente parce qu'il n'y a pas de changement de signe entre a et b. C'est faux : g(x) = x² − 3x + 2 est continue sur [0 ; 3] avec g(0) = 2 > 0 et g(3) = 2 > 0, et pourtant g(1) = g(2) = 0. Le changement de signe suffit pour l'existence, il n'est pas nécessaire.
:::

::: propriete

- **Théorème des valeurs intermédiaires** : si f est continue sur un intervalle I, si a < b sont dans I et si k est compris entre f(a) et f(b), alors f(x) = k a au moins une solution dans [a ; b].
- **Corollaire 1** : si f est continue sur [a ; b] et f(a) × f(b) < 0, alors f(c) = 0 pour au moins un c de ]a ; b[.
- **Corollaire 2** : si f est continue sur un intervalle et ne s'annule pas, alors elle garde un signe constant.
- **Unicité** : si de plus f est strictement monotone sur [a ; b], ce c est unique.

Cas limite : la continuité est indispensable. 1/x vérifie f(−1) = −1 < 0 < 1 = f(1) sur [−1 ; 1], mais ne s'annule jamais : elle n'est pas définie en 0, donc pas continue sur [−1 ; 1].
:::

::: verifie
Montre que x⁵ + x − 1 = 0 admet une solution unique dans [0 ; 1].

---

On pose f(x) = x⁵ + x − 1, un polynôme donc continu. f(0) = −1 < 0 et f(1) = 1 > 0 : par le corollaire 1, il existe une solution dans ]0 ; 1[. x ↦ x⁵ et x ↦ x sont strictement croissantes, donc f aussi : la solution est unique.
:::

::: retenir
Continue et de signes opposés aux bornes : au moins une solution ; en plus strictement monotone : une seule.
:::

## ✂️ Dichotomie : encadrer une solution

Au jeu du « plus grand / plus petit », on trouve un nombre caché en le coupant en deux à chaque coup. Même idée pour x³ + 2x − 5 = 0 : sa solution α est dans ]1 ; 2[, comment la coincer dans un intervalle de longueur au plus 0,1 sans résoudre l'équation ?

::: figure À chaque étape, on garde la moitié où f change de signe : l'intervalle est divisé par 2 et la solution α reste à l'intérieur
<svg viewBox="0 0 340 225"><path d="M70 40 L320 40" stroke="#0f6e56" stroke-width="5" stroke-linecap="round" opacity="0.55" fill="none"/><circle cx="70" cy="40" r="4" fill="#0f172a"/><circle cx="320" cy="40" r="4" fill="#0f172a"/><text x="62" y="44" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="328" y="44" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="70" y="31" text-anchor="middle" font-size="16" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−</text><text x="320" y="31" text-anchor="middle" font-size="16" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+</text><text x="4" y="44" text-anchor="start" font-size="10" font-weight="700" fill="#94a3b8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">étape 0</text><path d="M70 82 L195 82" stroke="#0f6e56" stroke-width="5" stroke-linecap="round" opacity="0.55" fill="none"/><circle cx="70" cy="82" r="4" fill="#0f172a"/><circle cx="195" cy="82" r="4" fill="#0f172a"/><text x="62" y="86" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="203" y="86" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,5</text><text x="70" y="73" text-anchor="middle" font-size="16" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−</text><text x="195" y="73" text-anchor="middle" font-size="16" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+</text><text x="4" y="86" text-anchor="start" font-size="10" font-weight="700" fill="#94a3b8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">étape 1</text><path d="M132.5 124 L195 124" stroke="#0f6e56" stroke-width="5" stroke-linecap="round" opacity="0.55" fill="none"/><circle cx="132.5" cy="124" r="4" fill="#0f172a"/><circle cx="195" cy="124" r="4" fill="#0f172a"/><text x="124.5" y="128" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,25</text><text x="203" y="128" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,5</text><text x="132.5" y="115" text-anchor="middle" font-size="16" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−</text><text x="195" y="115" text-anchor="middle" font-size="16" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+</text><text x="4" y="128" text-anchor="start" font-size="10" font-weight="700" fill="#94a3b8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">étape 2</text><path d="M132.5 166 L163.8 166" stroke="#0f6e56" stroke-width="5" stroke-linecap="round" opacity="0.55" fill="none"/><circle cx="132.5" cy="166" r="4" fill="#0f172a"/><circle cx="163.8" cy="166" r="4" fill="#0f172a"/><text x="124.5" y="170" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,25</text><text x="171.8" y="170" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,375</text><text x="132.5" y="157" text-anchor="middle" font-size="16" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−</text><text x="163.8" y="157" text-anchor="middle" font-size="16" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+</text><text x="4" y="170" text-anchor="start" font-size="10" font-weight="700" fill="#94a3b8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">étape 3</text><path d="M148.1 208 L163.8 208" stroke="#0f6e56" stroke-width="5" stroke-linecap="round" opacity="0.55" fill="none"/><circle cx="148.1" cy="208" r="4" fill="#0f172a"/><circle cx="163.8" cy="208" r="4" fill="#0f172a"/><text x="140.1" y="212" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,3125</text><text x="171.8" y="212" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,375</text><text x="145.5" y="199" text-anchor="middle" font-size="16" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−</text><text x="163.8" y="199" text-anchor="middle" font-size="16" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+</text><text x="4" y="212" text-anchor="start" font-size="10" font-weight="700" fill="#94a3b8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">étape 4</text><path d="M152.1 24 L152.1 214" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="4 3" fill="none"/><text x="152.1" y="16" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">α</text></svg>
:::

Le signe écrit au-dessus de chaque extrémité est le signe de f en ce point.

::: exemple Encadrer α pour f(x) = x³ + 2x − 5 sur [1 ; 2]

On sait que f est continue, strictement croissante, f(1) = −2 < 0 et f(2) = 7 > 0.

1. Milieu 1,5 : f(1,5) = 1,375 > 0, donc f change de signe entre 1 et 1,5 : 1 < α < 1,5.
2. Milieu 1,25 : f(1,25) ≈ −0,547 < 0, donc f change de signe entre 1,25 et 1,5 : 1,25 < α < 1,5.
3. Milieu 1,375 : f(1,375) ≈ 0,350 > 0, donc 1,25 < α < 1,375.
4. Milieu 1,3125 : f(1,3125) ≈ −0,114 < 0, donc 1,3125 < α < 1,375 — l'amplitude est 0,0625 ≤ 0,1 : on s'arrête.

:::

::: piege Lire « f(c) > 0 » comme « α est à droite de c »
Cela tente parce que positif évoque la droite. Or f est croissante : f(1,5) > 0 signifie que α est à gauche de 1,5. On garde toujours la moitié dont les extrémités ont des signes opposés, jamais le côté deviné d'après un seul signe.
:::

::: methode Dichotomie

1. Vérifier que f est continue sur [a ; b] et que f(a) × f(b) < 0.
2. Calculer le milieu c = (a + b)/2 et le signe de f(c).
3. Garder [a ; c] si f(a) × f(c) < 0, sinon [c ; b] : la moitié où le signe change.
4. Recommencer jusqu'à une amplitude assez petite.

L'amplitude est divisée par 2 à chaque étape : après n étapes, elle vaut (b − a)/2ⁿ. Cas limite : si f(c) = 0, on a trouvé α et on s'arrête. De 1,3125 < α < 1,375, on tire 1,3 < α < 1,4 : 1,3 est une valeur approchée de α par défaut à 0,1 près.
:::

::: verifie
On admet que x⁵ + x − 1 = 0 a une solution unique α dans ]0 ; 1[. Encadre α par deux étapes de dichotomie.

---

Milieu 0,5 : f(0,5) = 0,03125 + 0,5 − 1 = −0,46875 < 0 et f(1) > 0, donc 0,5 < α < 1. Milieu 0,75 : f(0,75) ≈ −0,013 < 0, donc 0,75 < α < 1. Deux étapes donnent 0,75 < α < 1, d'amplitude 0,25 = 1/4.
:::

::: retenir
Dichotomie : on coupe en deux et on garde la moitié où f change de signe ; l'amplitude est divisée par 2 à chaque étape.
:::

## 📈 Comportement asymptotique : les bords de la courbe

Sur l'écran, la courbe de f(x) = (x² − 2x + 3)/(x − 2) semble se coller à deux droites : une verticale près de x = 2, et une oblique quand |x| est grand. Quelles sont ces droites, et comment les trouver par le calcul ?

::: figure La courbe C de f se rapproche de la droite x = 2 près de 2, et de la droite y = x quand x tend vers +∞ ou −∞
<svg viewBox="0 0 340 255"><path d="M20 170 L240 170" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M240 170 l-6 -3 l0 6 z" fill="#0f172a"/><path d="M88 238 L88 13.6" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M88 13.6 l-3 6 l6 0 z" fill="#0f172a"/><path d="M128 238 L128 17" fill="none" stroke="#0f6e56" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 4"/><path d="M24 224.4 L232 47.6" fill="none" stroke="#0f6e56" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 4"/><path d="M28 231.2 L29.1 230.4 L30.2 229.5 L31.3 228.7 L32.4 227.9 L33.6 227.1 L34.7 226.3 L35.8 225.4 L36.9 224.6 L38 223.8 L39.1 223 L40.2 222.2 L41.3 221.4 L42.5 220.6 L43.6 219.8 L44.7 219.1 L45.8 218.3 L46.9 217.5 L48 216.7 L49.1 216 L50.2 215.2 L51.4 214.5 L52.5 213.7 L53.6 213 L54.7 212.2 L55.8 211.5 L56.9 210.8 L58 210 L59.1 209.3 L60.3 208.6 L61.4 207.9 L62.5 207.3 L63.6 206.6 L64.7 205.9 L65.8 205.3 L66.9 204.6 L68 204 L69.2 203.4 L70.3 202.7 L71.4 202.1 L72.5 201.6 L73.6 201 L74.7 200.4 L75.8 199.9 L76.9 199.4 L78.1 198.9 L79.2 198.4 L80.3 197.9 L81.4 197.5 L82.5 197.1 L83.6 196.7 L84.7 196.4 L85.8 196 L87 195.7 L88.1 195.5 L89.2 195.3 L90.3 195.1 L91.4 195 L92.5 194.9 L93.6 194.9 L94.7 194.9 L95.9 195.1 L97 195.2 L98.1 195.5 L99.2 195.9 L100.3 196.4 L101.4 197 L102.5 197.7 L103.6 198.6 L104.8 199.6 L105.9 200.9 L107 202.4 L108.1 204.2 L109.2 206.2 L110.3 208.7 L111.4 211.6 L112.5 215.1 L113.7 219.3 L114.8 224.3 L115.9 230.4 L117 238" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><path d="M137.2 17 L138.4 28.7 L139.5 37.8 L140.7 45 L141.9 50.9 L143.1 55.6 L144.3 59.5 L145.5 62.8 L146.7 65.5 L147.8 67.7 L149 69.6 L150.2 71.2 L151.4 72.5 L152.6 73.6 L153.8 74.5 L155 75.2 L156.1 75.8 L157.3 76.3 L158.5 76.6 L159.7 76.9 L160.9 77 L162.1 77.1 L163.2 77.1 L164.4 77 L165.6 76.9 L166.8 76.7 L168 76.5 L169.2 76.2 L170.4 75.9 L171.5 75.6 L172.7 75.2 L173.9 74.8 L175.1 74.3 L176.3 73.8 L177.5 73.3 L178.7 72.8 L179.8 72.3 L181 71.7 L182.2 71.1 L183.4 70.5 L184.6 69.9 L185.8 69.2 L187 68.6 L188.1 67.9 L189.3 67.2 L190.5 66.5 L191.7 65.8 L192.9 65.1 L194.1 64.4 L195.3 63.7 L196.4 62.9 L197.6 62.2 L198.8 61.4 L200 60.6 L201.2 59.9 L202.4 59.1 L203.6 58.3 L204.7 57.5 L205.9 56.7 L207.1 55.9 L208.3 55 L209.5 54.2 L210.7 53.4 L211.8 52.6 L213 51.7 L214.2 50.9 L215.4 50 L216.6 49.2 L217.8 48.3 L219 47.5 L220.1 46.6 L221.3 45.7 L222.5 44.9 L223.7 44 L224.9 43.1 L226.1 42.2 L227.3 41.4 L228.4 40.5 L229.6 39.6 L230.8 38.7 L232 37.8" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><text x="162" y="27.2" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x = 2</text><text x="222" y="81.6" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = x</text><text x="42" y="193.8" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><text x="128" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="168" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text></svg>
:::

Le trait vertical correspond à une limite infinie en 2, le trait oblique à lim [f(x) − x] = 0.

::: exemple Les asymptotes de f(x) = (x² − 2x + 3)/(x − 2)

1. f est définie sur ℝ privé de 2.
2. En 2⁺, le numérateur tend vers 3 > 0 et le dénominateur vers 0⁺, donc lim f = +∞ ; en 2⁻, le dénominateur tend vers 0⁻, donc lim f = −∞ — règle des signes d'un quotient. La droite x = 2 est asymptote verticale.
3. x² − 2x + 3 = x(x − 2) + 3, donc f(x) = x + 3/(x − 2) — on fait apparaître la partie affine.
4. f(x) − x = 3/(x − 2) tend vers 0 en +∞ et en −∞ : la droite y = x est asymptote oblique des deux côtés.
5. f(x) − x a le signe de x − 2 : la courbe est au-dessus de la droite pour x > 2, en dessous pour x < 2.

:::

::: exemple Sans division : h(x) = √(x² + 6x + 10) en +∞

1. Pour x > 0, h(x)/x = √(1 + 6/x + 10/x²) tend vers 1 : on pose a = 1 — c'est la pente cherchée.
2. h(x) − x = (h(x)² − x²)/(h(x) + x) = (6x + 10)/(h(x) + x), et en divisant par x, (6 + 10/x)/(√(1 + 6/x + 10/x²) + 1) tend vers 6/2 = 3 — on a multiplié par la quantité conjuguée.
3. Donc lim [h(x) − x] = 3 : la droite y = x + 3 est asymptote oblique en +∞.

:::

::: piege Recopier en −∞ l'asymptote trouvée en +∞
Cela tente parce que la formule est la même. Mais pour x < 0, √(x²) = |x| = −x : h(x)/x tend vers −1, et h(x) + x = (6x + 10)/(h(x) − x) tend vers −3. L'asymptote en −∞ est y = −x − 3, pas y = x + 3.
:::

::: methode Étudier une branche infinie en +∞ (de même en −∞)

1. Calculer lim f(x) : si elle est un réel b, la droite y = b est asymptote horizontale (pour une fraction rationnelle, c'est le quotient des termes de plus haut degré).
2. Si lim f(x) = ±∞, calculer a = lim f(x)/x.
3. Si a est un réel non nul, calculer lim [f(x) − ax].
4. Conclure avec le tableau ci-dessous.

Une limite infinie de f en un réel a (à droite ou à gauche) donne l'asymptote verticale x = a.
:::

| Ce qu'on trouve                            | Conclusion                                                      |
| ------------------------------------------ | --------------------------------------------------------------- |
| a = ±∞                                     | branche parabolique de direction l'axe des ordonnées (ex. x²)   |
| a = 0                                      | branche parabolique de direction l'axe des abscisses (ex. √x)   |
| a réel non nul et lim [f(x) − ax] = b réel | asymptote oblique y = ax + b                                    |
| a réel non nul et lim [f(x) − ax] = ±∞     | branche parabolique de direction la droite y = ax (ex. 2x + √x) |

Pour m(x) = 2x + √x : m(x)/x = 2 + 1/√x tend vers 2, mais m(x) − 2x = √x tend vers +∞ : on est dans la dernière ligne.

::: verifie
Montre que la courbe de g(x) = (2x² + 3x + 2)/(x + 1) a une asymptote verticale et une asymptote oblique, et donne-les.

---

En −1, le numérateur tend vers 2 − 3 + 2 = 1 > 0 et le dénominateur vers 0 : la limite est infinie, donc x = −1 est asymptote verticale. On a (2x + 1)(x + 1) = 2x² + 3x + 1, donc g(x) = 2x + 1 + 1/(x + 1). Alors g(x) − (2x + 1) = 1/(x + 1) tend vers 0 en ±∞ : y = 2x + 1 est asymptote oblique.
:::

::: retenir
Limite infinie en un réel a : asymptote x = a ; limite finie b à l'infini : asymptote y = b ; sinon on calcule a = lim f/x puis lim [f(x) − ax].
:::

> 🏆 Huit outils forgés : tu sais boucher un trou, coincer une limite, suivre l'eau qui monte, enchaîner deux machines, lire une image, prouver qu'une solution existe, l'encadrer et décrire les bords d'une courbe. La dérivation va maintenant mesurer la pente de ces courbes en chaque point.
