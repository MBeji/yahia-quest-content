# 🌊 Les ondes mécaniques progressives — l'énergie voyage, la matière reste

> 💡 «Une vague traverse l'océan d'un bord à l'autre, mais chaque goutte d'eau, elle, ne fait que monter et descendre.»

Jusqu'ici, les oscillateurs (circuits, pendules) vibraient sur place. Ici la vibration se met à voyager : une secousse, imposée en un point d'une corde, d'un ressort, de l'eau ou de l'air, gagne ses voisins et traverse le milieu. Huit notions te mènent de la secousse unique à l'onde entretenue : l'ébranlement, sa nature transversale ou longitudinale, sa célérité, la double périodicité, l'équation horaire d'un point, le déphasage, l'aspect de la corde à un instant donné et le stroboscope. On suppose acquis la période, la fréquence et la pulsation d'une grandeur sinusoïdale : T = 1/N et T = 2π/ω.

## 🌊 L'ébranlement : de l'énergie qui voyage, pas de la matière

Tu laisses tomber un caillou dans une nappe d'eau calme. Une ride circulaire s'élargit autour du point d'impact S, et un bouchon de liège flotte à 60 cm de S.
Quand la ride arrive, le bouchon bouge : est-il emporté jusqu'au bord, et qu'est-ce qui voyage alors ?

::: definition
**Ébranlement** — Un **ébranlement** est une déformation de courte durée imposée localement à un **milieu élastique**, c'est-à-dire un milieu qui reprend de lui-même sa forme initiale après une déformation brève. Il se transmet de proche en proche : chaque point du milieu reproduit le mouvement de son voisin, avec un léger retard.
:::

::: figure La même ride aux dates t₁ < t₂ < t₃ : le cercle s'élargit autour de S pendant que le bouchon M monte et descend sur place ; le trait de plus en plus fin traduit l'affaiblissement de la ride (illustration, sans échelle)
<svg viewBox="0 0 340 216"><title>Rides circulaires créées par une goutte tombée en S aux dates t₁, t₂ et t₃, et bouchon de liège M qui oscille verticalement</title><circle cx="170" cy="108" r="26" fill="none" stroke="#0f6e56" stroke-width="3.2"/><circle cx="170" cy="108" r="52" fill="none" stroke="#0f6e56" stroke-width="2.4"/><circle cx="170" cy="108" r="78" fill="none" stroke="#0f6e56" stroke-width="1.7"/><circle cx="170" cy="108" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="2"/><rect x="216" y="104" width="12" height="8" fill="#d97706" stroke="#0f172a" stroke-width="1.6"/><line x1="236" y1="110" x2="236" y2="84" stroke="#0f172a" stroke-width="1.8"/><polygon points="236,84 239.5,91 232.5,91" fill="#0f172a"/><line x1="236" y1="86" x2="236" y2="112" stroke="#0f172a" stroke-width="1.8"/><polygon points="236,112 232.5,105 239.5,105" fill="#0f172a"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="160" y="126" text-anchor="middle" fill="#0f172a" font-size="14">S</text><text x="220" y="132" text-anchor="middle" fill="#d97706" font-size="14">M</text><text x="135.8" y="87.8" text-anchor="middle" fill="#0f6e56" font-size="12">t₁</text><text x="117.6" y="69.6" text-anchor="middle" fill="#0f6e56" font-size="12">t₂</text><text x="99.4" y="51.4" text-anchor="middle" fill="#0f6e56" font-size="12">t₃</text></g></svg>
:::

Sur la figure, S est le point d'impact, les cercles verts sont la même ride aux dates t₁ < t₂ < t₃, et M est le bouchon, qui oscille sur place.

::: exemple Lire la ride et le bouchon (bouchon M à 60 cm du point d'impact S)

1. Le bouchon monte, descend, puis retrouve sa place : aucune matière n'a suivi la ride. Si l'eau avançait avec la ride, le bouchon serait emporté.
2. Tous les points d'une même ride sont atteints au même instant, et la ride est un cercle de centre S : l'ébranlement se propage dans toutes les directions de la surface. Un point de la surface se repère par deux coordonnées (x, y) : le milieu est **bidimensionnel**.
3. Le bouchon, d'abord immobile, se met à bouger avec un retard sur le point d'impact : il a reçu de l'énergie, transmise par l'eau de proche en proche depuis S.
4. De t₁ à t₃ le cercle s'élargit, mais la même énergie se répartit sur un cercle de plus en plus long : chaque portion de ride en reçoit moins et la ride s'affaiblit. C'est la **dilution de l'énergie**.

:::

::: piege
**Erreur : croire que la ride emporte l'eau et le bouchon vers le bord.** Le bouchon de l'étape 1 revient à sa place. L'erreur tente parce qu'on voit « avancer » quelque chose. Mais ce qui avance est une déformation, pas de l'eau : la propagation transporte de l'énergie sans transporter de matière.
:::

::: propriete
**Ce qui reste vrai** — Un ébranlement se propage dans un milieu matériel élastique : unidimensionnel (corde, ressort : x), bidimensionnel (surface d'un liquide : x, y) ou tridimensionnel (air : x, y, z). Cas limite : dans le vide il n'y a rien pour transmettre la déformation ; un poste de radio placé sous une cloche dont on retire l'air devient inaudible, alors qu'il fonctionne toujours. Le son émis par une petite source est une onde progressive sphérique, qui s'atténue aussi par dilution de l'énergie.
:::

**La houle, une onde qui porte de l'énergie** — Le vent crée à la surface de la mer une succession régulière de vagues, la **houle** : c'est une onde progressive, que l'on caractérise par sa hauteur H, sa période T et sa longueur d'onde λ. Une houle voyage sur de très longues distances sans trop de pertes (ses fronts sont presque rectilignes : l'énergie ne s'y dilue pas comme sur une ride circulaire). Une houle courte (T = 3 s ; H = 0,6 m) transporte une puissance d'environ 1 kW ; une houle longue et haute (T = 11 s ; H = 7,5 m), environ 600 fois plus. C'est cette énergie, et non l'eau, que cherchent à capter les usines houlomotrices.

::: verifie À toi : un autre étang
Une bouée flotte à 5 m de l'endroit où tombe un galet. Que fait la bouée au passage de la ride, de quelle dimension est le milieu, et pourquoi la ride faiblit-elle en s'éloignant ?

---

La bouée monte et descend sur place, sans suivre la ride : seule l'énergie se transmet. La surface de l'eau est un milieu bidimensionnel (deux coordonnées x et y). La ride faiblit parce que la même énergie se répartit sur un cercle de plus en plus long : c'est la dilution de l'énergie.
:::

::: retenir
Un ébranlement est une déformation brève qui se propage dans un milieu élastique ; la propagation transporte de l'énergie sans transporter de matière, et une onde mécanique ne se propage pas dans le vide.
:::

## ↔️ Transversale ou longitudinale : la direction du mouvement des points

Pose une longue corde élastique sur une table et donne une brève secousse vers le haut à son extrémité O : une bosse part vers l'autre bout. Avec un ressort à spires non jointives, comprime quelques spires et lâche-les : une zone comprimée avance.
Dans les deux cas quelque chose avance ; mais comment bougent les points du milieu, par rapport à la direction dans laquelle cela avance ?

::: definition
**Ébranlement transversal, ébranlement longitudinal** — Un ébranlement est **transversal** si la déformation des points du milieu est perpendiculaire à la direction de propagation ; il est **longitudinal** si elle lui est parallèle. Une onde a la nature des ébranlements qui la composent.
:::

::: figure Corde : le point P monte et descend pendant que la bosse avance vers la droite ; ressort : le point Q va et vient le long de l'axe pendant que la zone comprimée avance
<svg viewBox="0 0 340 216"><title>Corde : le point P se déplace perpendiculairement à la propagation ; ressort : le point Q se déplace le long de la propagation</title><polyline points="24,66 26,66 28,66 30,66 32,66 34,66 36,66 38,66 40,66 42,66 44,66 46,66 48,66 50,66 52,66 54,66 56,66 58,66 60,66 62,66 64,66 66,66 68,66 70,66 72,66 74,66 76,66 78,66 80,66 82,66 84,66 86,66 88,66 90,66 92,66 94,66 96,66 98,66 100,65.99 102,65.99 104,65.98 106,65.98 108,65.96 110,65.94 112,65.91 114,65.87 116,65.81 118,65.73 120,65.61 122,65.45 124,65.24 126,64.96 128,64.6 130,64.13 132,63.55 134,62.84 136,61.97 138,60.93 140,59.71 142,58.31 144,56.72 146,54.96 148,53.05 150,51.02 152,48.91 154,46.76 156,44.65 158,42.64 160,40.78 162,39.15 164,37.82 166,36.82 168,36.21 170,36 172,36.21 174,36.82 176,37.82 178,39.15 180,40.78 182,42.64 184,44.65 186,46.76 188,48.91 190,51.02 192,53.05 194,54.96 196,56.72 198,58.31 200,59.71 202,60.93 204,61.97 206,62.84 208,63.55 210,64.13 212,64.6 214,64.96 216,65.24 218,65.45 220,65.61 222,65.73 224,65.81 226,65.87 228,65.91 230,65.94 232,65.96 234,65.98 236,65.98 238,65.99 240,65.99 242,66 244,66 246,66 248,66 250,66 252,66 254,66 256,66 258,66 260,66 262,66 264,66 266,66 268,66 270,66 272,66 274,66 276,66 278,66 280,66 282,66 284,66 286,66 288,66 290,66 292,66 294,66 296,66 298,66 300,66 302,66 304,66 306,66 308,66 310,66 312,66 314,66 316,66" fill="none" stroke="#0f172a" stroke-width="2.6"/><circle cx="170" cy="36" r="4.5" fill="#d97706" stroke="#0f172a" stroke-width="1.4"/><line x1="192" y1="36" x2="192" y2="14" stroke="#d97706" stroke-width="2.4"/><polygon points="192,14 196,22 188,22" fill="#d97706"/><line x1="192" y1="14" x2="192" y2="36" stroke="#d97706" stroke-width="2.4"/><polygon points="192,36 188,28 196,28" fill="#d97706"/><line x1="232" y1="28" x2="300" y2="28" stroke="#0f6e56" stroke-width="2.6"/><polygon points="300,28 291,32.5 291,23.5" fill="#0f6e56"/><line x1="24" y1="160" x2="320" y2="160" stroke="#64748b" stroke-width="1.6"/><line x1="28" y1="140" x2="28" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="40" y1="140" x2="40" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="52" y1="140" x2="52" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="64" y1="140" x2="64" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="76" y1="140" x2="76" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="88" y1="140" x2="88" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="100" y1="140" x2="100" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="112" y1="140" x2="112" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="124" y1="140" x2="124" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="136" y1="140" x2="136" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="140" y1="140" x2="140" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="146" y1="140" x2="146" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="152" y1="140" x2="152" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="158" y1="140" x2="158" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="164" y1="140" x2="164" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="170" y1="140" x2="170" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="176" y1="140" x2="176" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="182" y1="140" x2="182" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="188" y1="140" x2="188" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="194" y1="140" x2="194" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="200" y1="140" x2="200" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="202" y1="140" x2="202" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="214" y1="140" x2="214" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="226" y1="140" x2="226" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="238" y1="140" x2="238" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="250" y1="140" x2="250" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="262" y1="140" x2="262" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="274" y1="140" x2="274" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="286" y1="140" x2="286" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="298" y1="140" x2="298" y2="180" stroke="#0f172a" stroke-width="2.2"/><line x1="310" y1="140" x2="310" y2="180" stroke="#0f172a" stroke-width="2.2"/><circle cx="171" cy="160" r="4.5" fill="#d97706" stroke="#0f172a" stroke-width="1.4"/><line x1="160" y1="128" x2="190" y2="128" stroke="#d97706" stroke-width="2.4"/><polygon points="190,128 182,132 182,124" fill="#d97706"/><line x1="190" y1="128" x2="160" y2="128" stroke="#d97706" stroke-width="2.4"/><polygon points="160,128 168,124 168,132" fill="#d97706"/><line x1="232" y1="200" x2="300" y2="200" stroke="#0f6e56" stroke-width="2.6"/><polygon points="300,200 291,204.5 291,195.5" fill="#0f6e56"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="60" y="30" text-anchor="middle" fill="#0f172a" font-size="13">corde</text><text x="264" y="20" text-anchor="middle" fill="#0f6e56" font-size="12">propagation</text><text x="226" y="44" text-anchor="start" fill="#d97706" font-size="12">point P</text><text x="60" y="120" text-anchor="middle" fill="#0f172a" font-size="13">ressort</text><text x="264" y="192" text-anchor="middle" fill="#0f6e56" font-size="12">propagation</text><text x="175" y="118" text-anchor="middle" fill="#d97706" font-size="12">point Q</text></g></svg>
:::

Sur la figure, la flèche verte donne le sens de propagation et la flèche orange le déplacement d'un point du milieu : perpendiculaire à la propagation pour P, parallèle pour Q.

::: exemple Classer l'onde d'un ressort suspendu (extrémité haute reliée à un vibreur)

Un ressort à spires non jointives pend verticalement, sa partie basse plongée dans l'eau pour absorber l'onde. Son extrémité haute est secouée verticalement par un vibreur. Sous stroboscope on voit des zones alternativement comprimées et dilatées qui descendent le long du ressort.

1. La propagation se fait le long du ressort, vers le bas : sa direction est verticale.
2. Le vibreur pousse et tire l'extrémité de haut en bas : les spires se rapprochent puis s'éloignent selon la verticale, d'où les zones comprimées et dilatées.
3. Les deux directions sont parallèles : l'onde est **longitudinale**. Pour la corde de la figure, le point P bouge perpendiculairement à la propagation : l'onde est transversale.

:::

::: piege
**Erreur : conclure qu'une onde est transversale parce que sa courbe est une sinusoïde.** L'oscilloscope donne une sinusoïde aussi pour un son, qui est pourtant longitudinal. L'erreur tente parce qu'une courbe qui « monte et descend » ressemble à une corde qui ondule. Mais une courbe représente une grandeur en fonction du temps ou de l'abscisse : la nature de l'onde se lit sur le mouvement des points du milieu, comparé à la propagation (étapes 1 à 3).
:::

| Onde | Mouvement des points du milieu | Nature |
| --- | --- | --- |
| Corde tendue, secousse perpendiculaire | perpendiculaire à la propagation | transversale |
| Ressort comprimé le long de son axe | le long de l'axe, comme la propagation | longitudinale |
| Surface de l'eau (ride) | le bouchon monte et descend | transversale |
| Son dans l'air | les molécules d'air vont et viennent selon la propagation | longitudinale |
| Séisme, onde P | compression-dilatation selon la propagation | longitudinale |
| Séisme, onde S | cisaillement, perpendiculaire à la propagation | transversale |

::: propriete
**Ce qui reste vrai** — La nature d'une onde se décide sur la direction du mouvement des points par rapport à la propagation, quel que soit le milieu : le tableau ci-dessus le montre pour six cas. Cas limite : un ressort peut porter les deux natures, selon qu'on le comprime le long de son axe ou qu'on le secoue de côté ; le nom du milieu ne suffit donc pas à conclure.
:::

::: verifie À toi : une corde secouée de côté
Une corde repose sur une table. On secoue brièvement son extrémité vers la gauche, dans le plan de la table et perpendiculairement à la corde : une bosse de côté avance le long de la corde. Quelle est la nature de l'ébranlement ?

---

Les points de la corde se déplacent de côté, perpendiculairement à la direction dans laquelle la bosse avance : l'ébranlement est transversal. La direction du déplacement n'a pas besoin d'être verticale : seule compte sa perpendicularité à la propagation.
:::

::: retenir
Transversale : mouvement des points perpendiculaire à la propagation ; longitudinale : parallèle. La nature se lit sur le mouvement des points, pas sur l'allure de la courbe.
:::

## ⚡ La célérité : à quelle vitesse voyage l'énergie ?

Sur une « échelle de perroquet » (un fil de torsion vertical qui porte des barreaux horizontaux), on tourne le barreau du haut d'un petit angle et on le lâche : la torsion descend de barreau en barreau. Deux capteurs, placés devant deux barreaux distants de d, mesurent la durée Δt du passage.
À quelle vitesse la torsion descend-elle, et de quoi cette vitesse dépend-elle : de la distance, de l'amplitude de la torsion, du milieu lui-même ?

::: definition
**Célérité** — La **célérité** v d'un ébranlement est sa vitesse de propagation, c'est-à-dire la vitesse à laquelle l'énergie se transmet (pas celle d'un morceau de matière). Entre deux capteurs distants de d, elle se calcule par

$$ v = d / Δt $$

en m/s lorsque d est en m et Δt en s.
:::

Voici les mesures faites avec l'échelle ordinaire (d en m, Δt en s) :

| d (m) | 0,20 | 0,40 | 0,60 | 0,80 |
| --- | --- | --- | --- | --- |
| Δt (s) | 0,16 | 0,32 | 0,48 | 0,64 |

En doublant l'angle de torsion initial, la mesure pour d = 0,40 m donne encore Δt = 0,32 s. Avec les masselottes des barreaux écartées de l'axe, ce qui augmente l'inertie du milieu :

| d (m) | 0,20 | 0,40 | 0,60 |
| --- | --- | --- | --- |
| Δt (s) | 0,35 | 0,70 | 1,05 |

Dans les tableaux, chaque durée est proportionnelle à la distance parcourue, et les durées sont plus longues quand l'inertie est plus grande.

::: exemple Exploiter les mesures de l'échelle

1. Échelle ordinaire : 0,20/0,16 = 0,40/0,32 = 0,60/0,48 = 0,80/0,64 = 1,25 m/s. Le quotient d/Δt est le même partout : la célérité est constante dans ce milieu homogène.
2. Torsion doublée, d = 0,40 m : Δt = 0,32 s comme avant, donc v = 1,25 m/s. La célérité ne dépend pas de l'amplitude de l'ébranlement.
3. Masselottes écartées : 0,20/0,35 = 0,40/0,70 = 0,60/1,05 = 0,57 m/s, plus faible que 1,25 m/s. Une plus grande inertie du milieu donne une plus faible célérité.

:::

::: piege
**Erreur : confondre la célérité avec la vitesse des points du milieu.** Un barreau (ou le bouchon de la première notion) oscille : sa vitesse change, s'annule, change de signe. L'erreur tente parce que les deux s'expriment en m/s. Mais la célérité est la même en tout point de ce milieu homogène et à chaque instant (étape 1), fixée par le milieu : c'est la vitesse de propagation de l'énergie.
:::

| Ébranlement | Célérité (m/s, ordre de grandeur) |
| --- | --- |
| à la surface de l'eau | 0,3 |
| le long d'une échelle de perroquet | 1 |
| le long d'une corde | 10 |
| son dans l'air à 20 °C | 342 |
| son dans l'eau à 20 °C | 1500 |
| son dans l'acier | 5000 |
| ondes sismiques | 8000 |

::: propriete
**Ce qui reste vrai** — La célérité dépend de la nature du milieu et de ses propriétés : le long d'une corde, elle augmente avec la tension et diminue quand l'inertie augmente ; pour le son, elle augmente quand le milieu est plus difficile à comprimer, donc plus grande dans les solides que dans les liquides, plus grande dans les liquides que dans les gaz. Elle ne dépend ni de l'amplitude, ni de l'énergie fournie par la source. Cas limite : l'amortissement diminue l'amplitude de l'ébranlement plus que sa célérité ; dans l'air, le son de fréquences différentes se propage à la même célérité.
:::

::: verifie À toi : une corde plus tendue
Un ébranlement parcourt 8,0 m d'une corde en 0,50 s. On tend davantage la corde et on recommence : il met 0,40 s. Calculer les deux célérités et conclure.

---

Avant : v = 8,0/0,50 = 16 m/s. Après : v = 8,0/0,40 = 20 m/s. La célérité augmente avec la tension de la corde : elle dépend des propriétés du milieu.
:::

::: retenir
v = d/Δt est fixée par le milieu (nature, tension, inertie, compressibilité), pas par l'amplitude ni par l'énergie de la source.
:::

## ⏱️ La double périodicité : T dans le temps, λ dans l'espace

Un vibreur de fréquence N = 25 Hz secoue l'extrémité d'une longue corde ; l'autre bout est entouré de coton qui absorbe l'onde. En lumière ordinaire, on ne voit qu'une bande floue. Une photo prise à un instant donné montre pourtant des bosses identiques tous les 20 cm.
Pourquoi ce motif se répète-t-il tous les 20 cm, et qu'est-ce qui fixe cet écart ?

::: definition
**Onde progressive et double périodicité** — Une **onde** est la succession d'ébranlements identiques que la source entretient dans un milieu. Dans un milieu ouvert, c'est-à-dire sans retour de l'onde, elle s'éloigne de la source : elle est **progressive**. Elle est périodique dans le temps, avec la période T de la source (N = 1/T), et périodique dans l'espace, avec la **longueur d'onde** λ, distance parcourue par l'onde pendant une période :

$$ λ = v · T = v / N $$
:::

::: figure Un point de la corde au cours du temps (période T = 40 ms) et la corde entière à un instant donné (période λ = 0,20 m) : deux sinusoïdes de même forme, l'une dans le temps, l'autre dans l'espace (valeurs de l'exemple : N = 25 Hz, v = 5,0 m/s)
<svg viewBox="0 0 340 198"><title>Double périodicité : période temporelle T de 40 ms pour un point de la corde, période spatiale λ de 0,20 m pour la corde entière à un instant donné</title><line x1="30" y1="106" x2="168" y2="106" stroke="#0f172a" stroke-width="1.6"/><polygon points="168,106 160,110 160,102" fill="#0f172a"/><line x1="36" y1="166" x2="36" y2="58" stroke="#0f172a" stroke-width="1.6"/><polygon points="36,58 40,66 32,66" fill="#0f172a"/><polyline points="36,62.52 37.24,63.06 38.48,64.65 39.72,67.26 40.96,70.83 42.2,75.26 43.44,80.44 44.68,86.26 45.92,92.56 47.16,99.2 48.4,106 49.64,112.8 50.88,119.44 52.12,125.74 53.36,131.56 54.6,136.74 55.84,141.17 57.08,144.74 58.32,147.35 59.56,148.94 60.8,149.48 62.04,148.94 63.28,147.35 64.52,144.74 65.76,141.17 67,136.74 68.24,131.56 69.48,125.74 70.72,119.44 71.96,112.8 73.2,106 74.44,99.2 75.68,92.56 76.92,86.26 78.16,80.44 79.4,75.26 80.64,70.83 81.88,67.26 83.12,64.65 84.36,63.06 85.6,62.52 86.84,63.06 88.08,64.65 89.32,67.26 90.56,70.83 91.8,75.26 93.04,80.44 94.28,86.26 95.52,92.56 96.76,99.2 98,106 99.24,112.8 100.48,119.44 101.72,125.74 102.96,131.56 104.2,136.74 105.44,141.17 106.68,144.74 107.92,147.35 109.16,148.94 110.4,149.48 111.64,148.94 112.88,147.35 114.12,144.74 115.36,141.17 116.6,136.74 117.84,131.56 119.08,125.74 120.32,119.44 121.56,112.8 122.8,106 124.04,99.2 125.28,92.56 126.52,86.26 127.76,80.44 129,75.26 130.24,70.83 131.48,67.26 132.72,64.65 133.96,63.06 135.2,62.52 136.44,63.06 137.68,64.65 138.92,67.26 140.16,70.83 141.4,75.26 142.64,80.44 143.88,86.26 145.12,92.56 146.36,99.2 147.6,106 148.84,112.8 150.08,119.44 151.32,125.74 152.56,131.56 153.8,136.74 155.04,141.17 156.28,144.74 157.52,147.35 158.76,148.94 160,149.48" fill="none" stroke="#0f172a" stroke-width="2.4"/><line x1="36" y1="60.52" x2="36" y2="60.52" stroke="#64748b" stroke-width="1"/><line x1="36" y1="48.52" x2="85.6" y2="48.52" stroke="#0f6e56" stroke-width="2.2"/><polygon points="85.6,48.52 78.6,52.02 78.6,45.02" fill="#0f6e56"/><line x1="85.6" y1="48.52" x2="36" y2="48.52" stroke="#0f6e56" stroke-width="2.2"/><polygon points="36,48.52 43,45.02 43,52.02" fill="#0f6e56"/><line x1="85.6" y1="44.52" x2="85.6" y2="112" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="36" y1="44.52" x2="36" y2="62.52" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="60.8" y="42.52" text-anchor="middle" fill="#0f6e56" font-size="12">T = 40 ms</text><text x="36" y="121" text-anchor="middle" fill="#0f172a" font-size="11">0</text><text x="85.6" y="121" text-anchor="middle" fill="#0f172a" font-size="11">40</text><text x="135.2" y="121" text-anchor="middle" fill="#0f172a" font-size="11">80</text><text x="164" y="99" text-anchor="end" fill="#0f172a" font-size="11">t (ms)</text><text x="96" y="190" text-anchor="middle" fill="#0f172a" font-size="11">un point, au cours du temps</text></g><line x1="190" y1="106" x2="328" y2="106" stroke="#0f172a" stroke-width="1.6"/><polygon points="328,106 320,110 320,102" fill="#0f172a"/><line x1="196" y1="166" x2="196" y2="58" stroke="#0f172a" stroke-width="1.6"/><polygon points="196,58 200,66 192,66" fill="#0f172a"/><polyline points="196,62.52 196.99,62.86 197.98,63.89 198.98,65.57 199.97,67.9 200.96,70.83 201.95,74.31 202.94,78.29 203.94,82.7 204.93,87.49 205.92,92.56 206.91,97.85 207.9,103.27 208.9,108.73 209.89,114.15 210.88,119.44 211.87,124.51 212.86,129.3 213.86,133.71 214.85,137.69 215.84,141.17 216.83,144.1 217.82,146.43 218.82,148.11 219.81,149.14 220.8,149.48 221.79,149.14 222.78,148.11 223.78,146.43 224.77,144.1 225.76,141.17 226.75,137.69 227.74,133.71 228.74,129.3 229.73,124.51 230.72,119.44 231.71,114.15 232.7,108.73 233.7,103.27 234.69,97.85 235.68,92.56 236.67,87.49 237.66,82.7 238.66,78.29 239.65,74.31 240.64,70.83 241.63,67.9 242.62,65.57 243.62,63.89 244.61,62.86 245.6,62.52 246.59,62.86 247.58,63.89 248.58,65.57 249.57,67.9 250.56,70.83 251.55,74.31 252.54,78.29 253.54,82.7 254.53,87.49 255.52,92.56 256.51,97.85 257.5,103.27 258.5,108.73 259.49,114.15 260.48,119.44 261.47,124.51 262.46,129.3 263.46,133.71 264.45,137.69 265.44,141.17 266.43,144.1 267.42,146.43 268.42,148.11 269.41,149.14 270.4,149.48 271.39,149.14 272.38,148.11 273.38,146.43 274.37,144.1 275.36,141.17 276.35,137.69 277.34,133.71 278.34,129.3 279.33,124.51 280.32,119.44 281.31,114.15 282.3,108.73 283.3,103.27 284.29,97.85 285.28,92.56 286.27,87.49 287.26,82.7 288.26,78.29 289.25,74.31 290.24,70.83 291.23,67.9 292.22,65.57 293.22,63.89 294.21,62.86 295.2,62.52 296.19,62.86 297.18,63.89 298.18,65.57 299.17,67.9 300.16,70.83 301.15,74.31 302.14,78.29 303.14,82.7 304.13,87.49 305.12,92.56 306.11,97.85 307.1,103.27 308.1,108.73 309.09,114.15 310.08,119.44 311.07,124.51 312.06,129.3 313.06,133.71 314.05,137.69 315.04,141.17 316.03,144.1 317.02,146.43 318.02,148.11 319.01,149.14 320,149.48" fill="none" stroke="#0f172a" stroke-width="2.4"/><line x1="196" y1="48.52" x2="245.6" y2="48.52" stroke="#0f6e56" stroke-width="2.2"/><polygon points="245.6,48.52 238.6,52.02 238.6,45.02" fill="#0f6e56"/><line x1="245.6" y1="48.52" x2="196" y2="48.52" stroke="#0f6e56" stroke-width="2.2"/><polygon points="196,48.52 203,45.02 203,52.02" fill="#0f6e56"/><line x1="245.6" y1="44.52" x2="245.6" y2="112" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="196" y1="44.52" x2="196" y2="62.52" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="220.8" y="42.52" text-anchor="middle" fill="#0f6e56" font-size="12">λ = 0,20 m</text><text x="196" y="121" text-anchor="middle" fill="#0f172a" font-size="11">0</text><text x="245.6" y="121" text-anchor="middle" fill="#0f172a" font-size="11">0,20</text><text x="295.2" y="121" text-anchor="middle" fill="#0f172a" font-size="11">0,40</text><text x="324" y="99" text-anchor="end" fill="#0f172a" font-size="11">x (m)</text><text x="256" y="190" text-anchor="middle" fill="#0f172a" font-size="11">toute la corde, à un instant</text></g><line x1="180" y1="26" x2="180" y2="176" stroke="#e2e8f0" stroke-width="1.4"/></svg>
:::

Sur la figure, les deux courbes ont la même forme : celle de gauche donne l'élongation d'un seul point au cours du temps (période T), celle de droite l'élongation de tous les points au même instant (période λ).

::: exemple De la fréquence du vibreur à la longueur d'onde (corde, N = 25 Hz)

1. T = 1/N = 1/25 = 0,040 s = 40 ms : c'est la période du vibreur, donc de chaque point de la corde.
2. Sur cette corde, v = 5,0 m/s (fixée par le milieu). λ = v·T = 5,0 × 0,040 = 0,20 m = 20 cm, l'écart relevé sur la photo : en une période, l'onde avance de 20 cm et retrouve le même état.
3. On règle le vibreur sur N = 40 Hz, sur la même corde. La célérité ne change pas (le milieu est le même) : λ = v/N = 5,0/40 = 0,125 m = 12,5 cm, et T = 25 ms.
4. Pour un son de 850 Hz dans l'air (v = 340 m/s) : λ = 340/850 = 0,40 m.

:::

::: piege
**Erreur : croire que la fréquence ou la période change quand l'onde passe dans un autre milieu.** Un même haut-parleur émet 850 Hz dans l'air (v = 340 m/s) puis, étanche, dans l'eau (v = 1500 m/s). L'erreur tente parce que « tout change avec le milieu ». Mais la source impose N et T, qui restent égales à 850 Hz et 1,2 ms ; seule la célérité change, donc la longueur d'onde : 0,40 m dans l'air, 1500/850 ≈ 1,8 m dans l'eau.
:::

::: propriete
**Ce qui reste vrai** — T (et N) ne dépendent que de la source, v ne dépend que du milieu, et λ = v·T dépend des deux. Cas limite : si l'on double N sur la même corde, λ est divisée par deux, puisque v ne bouge pas ; si l'on change de milieu à N fixée, λ varie dans le même rapport que v.
:::

::: verifie À toi : des rides sur une cuve
Sur une cuve à ondes, un vibreur de 30 Hz crée des rides ; deux crêtes consécutives sont distantes de 5,0 mm. Calculer T, λ et la célérité v.

---

T = 1/N = 1/30 = 0,033 s. Deux crêtes consécutives sont séparées d'une longueur d'onde : λ = 5,0 mm = 5,0 × 10⁻³ m. Alors v = λ·N = 5,0 × 10⁻³ × 30 = 0,15 m/s.
:::

::: retenir
λ = v·T = v/N : la source fixe T, le milieu fixe v, et la longueur d'onde dépend des deux.
:::

## 📈 L'équation horaire d'un point : la copie retardée de la source

Reprenons la corde du vibreur (N = 25 Hz ; v = 5,0 m/s), absorbée par du coton à son extrémité. La source S démarre à t = 0 en montant : yS(t) = a sin ωt, avec a = 3,0 mm. Un point M se trouve à x = 0,25 m de S.
À quel instant M commence-t-il à bouger, et comment bouge-t-il ensuite ?

::: definition
**Équation horaire de M** — Sans amortissement, M répète le mouvement de S avec le retard θ = x/v : yM(t) = yS(t − θ) pour t ≥ θ, et yM(t) = 0 avant. Avec ω = 2π/T et λ = v·T :

$$ yM(t) = a sin ω(t − θ) = a sin(ωt − 2πx/λ) , t ≥ θ $$
:::

::: figure Diagrammes de mouvement de S (noir) et du point M à x = 0,25 m (vert) : M reste au repos jusqu'à 50 ms puis répète S avec un retard θ = 50 ms (a = 3,0 mm, T = 40 ms)
<svg viewBox="0 0 340 182"><title>Diagrammes de mouvement de la source S en noir et du point M en vert : la courbe de M est celle de S décalée de θ = 50 ms, avec M immobile avant cette date</title><line x1="30" y1="96" x2="334" y2="96" stroke="#0f172a" stroke-width="1.6"/><polygon points="334,96 326,100 326,92" fill="#0f172a"/><line x1="36" y1="158" x2="36" y2="24" stroke="#0f172a" stroke-width="1.6"/><polygon points="36,24 40,32 32,32" fill="#0f172a"/><polyline points="36,96 37.45,89.88 38.9,83.91 40.35,78.24 41.8,73 43.25,68.33 44.7,64.34 46.15,61.13 47.6,58.78 49.05,57.35 50.5,56.87 51.95,57.35 53.4,58.78 54.85,61.13 56.3,64.34 57.75,68.33 59.2,73 60.65,78.24 62.1,83.91 63.55,89.88 65,96 66.45,102.12 67.9,108.09 69.35,113.76 70.8,119 72.25,123.67 73.7,127.66 75.15,130.87 76.6,133.22 78.05,134.65 79.5,135.13 80.95,134.65 82.4,133.22 83.85,130.87 85.3,127.66 86.75,123.67 88.2,119 89.65,113.76 91.1,108.09 92.55,102.12 94,96 95.45,89.88 96.9,83.91 98.35,78.24 99.8,73 101.25,68.33 102.7,64.34 104.15,61.13 105.6,58.78 107.05,57.35 108.5,56.87 109.95,57.35 111.4,58.78 112.85,61.13 114.3,64.34 115.75,68.33 117.2,73 118.65,78.24 120.1,83.91 121.55,89.88 123,96 124.45,102.12 125.9,108.09 127.35,113.76 128.8,119 130.25,123.67 131.7,127.66 133.15,130.87 134.6,133.22 136.05,134.65 137.5,135.13 138.95,134.65 140.4,133.22 141.85,130.87 143.3,127.66 144.75,123.67 146.2,119 147.65,113.76 149.1,108.09 150.55,102.12 152,96 153.45,89.88 154.9,83.91 156.35,78.24 157.8,73 159.25,68.33 160.7,64.34 162.15,61.13 163.6,58.78 165.05,57.35 166.5,56.87 167.95,57.35 169.4,58.78 170.85,61.13 172.3,64.34 173.75,68.33 175.2,73 176.65,78.24 178.1,83.91 179.55,89.88 181,96 182.45,102.12 183.9,108.09 185.35,113.76 186.8,119 188.25,123.67 189.7,127.66 191.15,130.87 192.6,133.22 194.05,134.65 195.5,135.13 196.95,134.65 198.4,133.22 199.85,130.87 201.3,127.66 202.75,123.67 204.2,119 205.65,113.76 207.1,108.09 208.55,102.12 210,96 211.45,89.88 212.9,83.91 214.35,78.24 215.8,73 217.25,68.33 218.7,64.34 220.15,61.13 221.6,58.78 223.05,57.35 224.5,56.87 225.95,57.35 227.4,58.78 228.85,61.13 230.3,64.34 231.75,68.33 233.2,73 234.65,78.24 236.1,83.91 237.55,89.88 239,96 240.45,102.12 241.9,108.09 243.35,113.76 244.8,119 246.25,123.67 247.7,127.66 249.15,130.87 250.6,133.22 252.05,134.65 253.5,135.13 254.95,134.65 256.4,133.22 257.85,130.87 259.3,127.66 260.75,123.67 262.2,119 263.65,113.76 265.1,108.09 266.55,102.12 268,96 269.45,89.88 270.9,83.91 272.35,78.24 273.8,73 275.25,68.33 276.7,64.34 278.15,61.13 279.6,58.78 281.05,57.35 282.5,56.87 283.95,57.35 285.4,58.78 286.85,61.13 288.3,64.34 289.75,68.33 291.2,73 292.65,78.24 294.1,83.91 295.55,89.88 297,96 298.45,102.12 299.9,108.09 301.35,113.76 302.8,119 304.25,123.67 305.7,127.66 307.15,130.87 308.6,133.22 310.05,134.65 311.5,135.13 312.95,134.65 314.4,133.22 315.85,130.87 317.3,127.66 318.75,123.67 320.2,119 321.65,113.76 323.1,108.09 324.55,102.12 326,96" fill="none" stroke="#0f172a" stroke-width="2"/><polyline points="36,96 108.5,96 108.5,96 109.95,89.88 111.4,83.91 112.85,78.24 114.3,73 115.75,68.33 117.2,64.34 118.65,61.13 120.1,58.78 121.55,57.35 123,56.87 124.45,57.35 125.9,58.78 127.35,61.13 128.8,64.34 130.25,68.33 131.7,73 133.15,78.24 134.6,83.91 136.05,89.88 137.5,96 138.95,102.12 140.4,108.09 141.85,113.76 143.3,119 144.75,123.67 146.2,127.66 147.65,130.87 149.1,133.22 150.55,134.65 152,135.13 153.45,134.65 154.9,133.22 156.35,130.87 157.8,127.66 159.25,123.67 160.7,119 162.15,113.76 163.6,108.09 165.05,102.12 166.5,96 167.95,89.88 169.4,83.91 170.85,78.24 172.3,73 173.75,68.33 175.2,64.34 176.65,61.13 178.1,58.78 179.55,57.35 181,56.87 182.45,57.35 183.9,58.78 185.35,61.13 186.8,64.34 188.25,68.33 189.7,73 191.15,78.24 192.6,83.91 194.05,89.88 195.5,96 196.95,102.12 198.4,108.09 199.85,113.76 201.3,119 202.75,123.67 204.2,127.66 205.65,130.87 207.1,133.22 208.55,134.65 210,135.13 211.45,134.65 212.9,133.22 214.35,130.87 215.8,127.66 217.25,123.67 218.7,119 220.15,113.76 221.6,108.09 223.05,102.12 224.5,96 225.95,89.88 227.4,83.91 228.85,78.24 230.3,73 231.75,68.33 233.2,64.34 234.65,61.13 236.1,58.78 237.55,57.35 239,56.87 240.45,57.35 241.9,58.78 243.35,61.13 244.8,64.34 246.25,68.33 247.7,73 249.15,78.24 250.6,83.91 252.05,89.88 253.5,96 254.95,102.12 256.4,108.09 257.85,113.76 259.3,119 260.75,123.67 262.2,127.66 263.65,130.87 265.1,133.22 266.55,134.65 268,135.13 269.45,134.65 270.9,133.22 272.35,130.87 273.8,127.66 275.25,123.67 276.7,119 278.15,113.76 279.6,108.09 281.05,102.12 282.5,96 283.95,89.88 285.4,83.91 286.85,78.24 288.3,73 289.75,68.33 291.2,64.34 292.65,61.13 294.1,58.78 295.55,57.35 297,56.87 298.45,57.35 299.9,58.78 301.35,61.13 302.8,64.34 304.25,68.33 305.7,73 307.15,78.24 308.6,83.91 310.05,89.88 311.5,96 312.95,102.12 314.4,108.09 315.85,113.76 317.3,119 318.75,123.67 320.2,127.66 321.65,130.87 323.1,133.22 324.55,134.65 326,135.13" fill="none" stroke="#0f6e56" stroke-width="2.8"/><line x1="50.5" y1="40.87" x2="50.5" y2="56.87" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="123" y1="40.87" x2="123" y2="56.87" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="50.5" y1="44.87" x2="123" y2="44.87" stroke="#d97706" stroke-width="2.2"/><polygon points="123,44.87 116,48.37 116,41.37" fill="#d97706"/><line x1="123" y1="44.87" x2="50.5" y2="44.87" stroke="#d97706" stroke-width="2.2"/><polygon points="50.5,44.87 57.5,41.37 57.5,48.37" fill="#d97706"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="86.75" y="38.87" text-anchor="middle" fill="#d97706" font-size="12">θ = 50 ms</text><text x="36" y="112" text-anchor="middle" fill="#0f172a" font-size="11">0</text><text x="108.5" y="112" text-anchor="middle" fill="#0f172a" font-size="11">50</text><text x="181" y="112" text-anchor="middle" fill="#0f172a" font-size="11">100</text><text x="253.5" y="112" text-anchor="middle" fill="#0f172a" font-size="11">150</text><text x="326" y="112" text-anchor="middle" fill="#0f172a" font-size="11">200</text><text x="330" y="89" text-anchor="end" fill="#0f172a" font-size="11">t (ms)</text><text x="166.5" y="50.87" text-anchor="middle" fill="#0f172a" font-size="13">yS</text><text x="239" y="50.87" text-anchor="middle" fill="#0f6e56" font-size="13">yM</text></g></svg>
:::

Sur la figure, la courbe verte de M est la courbe noire de S décalée de θ vers la droite, et reste à zéro avant cette date.

::: exemple Écrire et lire l'équation horaire de M (x = 0,25 m)

1. θ = x/v = 0,25/5,0 = 0,050 s = 50 ms. Jusqu'à cette date, le front n'est pas arrivé : yM = 0.
2. T = 40 ms, donc ω = 2π/T = 50π rad/s (≈ 157 rad/s) et λ = v·T = 0,20 m.
3. Pour t ≥ θ : yM(t) = a sin ω(t − θ) = 3,0 × 10⁻³ sin[50π(t − 0,050)].
4. On développe : 50π × 0,050 = 2,5π, donc yM = 3,0 × 10⁻³ sin(50πt − 2,5π). Le sinus a pour période 2π : yM = 3,0 × 10⁻³ sin(50πt − π/2). Contrôle : 2πx/λ = 2π × 1,25 = 2,5π ✓.
5. Sur le diagramme, M retarde sur S de θ = 50 ms = 1,25 T : M vibre comme S en quadrature retard.

:::

::: piege
**Erreur : écrire yM(t) = a sin(ωt + 2πx/λ), avec un signe plus.** L'erreur tente parce qu'on « ajoute la distance parcourue ». Mais M copie S avec du retard : sa phase est plus petite. Test à t = 60 ms, dix millisecondes après l'arrivée de l'onde : la formule juste donne sin(50π × 0,060 − 2,5π) = sin(0,5π) = 1, M est à son maximum, comme S dix millisecondes après son départ ; avec le signe plus, on trouverait sin(5,5π) = −1, absurde.
:::

::: methode
**Instants d'une élongation donnée** — Pour savoir quand M passe par +a/2 en montant : on résout sin ω(t − θ) = 1/2 avec un cosinus positif, soit ω(t − θ) = π/6 + 2kπ, donc t = θ + T/12 + kT. En descendant par +a/2 : ω(t − θ) = 5π/6 + 2kπ, donc t = θ + 5T/12 + kT. De même, pour −a/2, on trouve ω(t − θ) = 7π/6 + 2kπ en descendant et 11π/6 + 2kπ en montant. Pour le point de l'exemple (θ = 50 ms, T = 40 ms) : premier passage par +a/2 en montant à 50 + 3,3 = 53,3 ms.
:::

::: propriete
**Ce qui reste vrai** — Sans amortissement, M a la même amplitude et la même période que S ; seule sa phase initiale dépend de x : φM = φS − 2πx/λ. Cas limite : si x est un multiple de λ, le retard θ est un multiple de T et M vibre comme S, avec seulement un retard.
:::

::: verifie À toi : un point plus éloigné
Même corde, point M′ à x = 0,40 m de la source. Donner θ, l'équation horaire de M′ et comparer son mouvement à celui de S.

---

θ = 0,40/5,0 = 0,080 s = 80 ms = 2T. 2πx/λ = 2π × 2 = 4π : yM′(t) = 3,0 × 10⁻³ sin(50πt − 4π) = 3,0 × 10⁻³ sin(50πt) pour t ≥ 80 ms. M′ vibre en phase avec S (x = 2λ), mais seulement à partir de 80 ms.
:::

::: retenir
yM(t) = a sin ω(t − x/v) = a sin(ωt − 2πx/λ) pour t ≥ x/v, et yM = 0 avant l'arrivée de l'onde.
:::

## 📡 Le déphasage : en phase, en opposition, en quadrature

Un haut-parleur, alimenté par un GBF, émet un son pur de fréquence N = 1250 Hz. Un microphone, placé sur l'axe à la distance d, est relié à la voie Y₂ d'un oscilloscope bicourbe ; la voie Y₁ reçoit la tension du haut-parleur. En éloignant le microphone, la courbe C₂ glisse par rapport à C₁ : tantôt les deux sont en phase, tantôt elles sont en miroir.
À quelles distances ces cas se produisent-ils, et que lit-on d'autre sur l'écran ?

::: definition
**Déphasage** — Le déphasage de M par rapport à la source S est Δφ = φM − φS, soit

$$ Δφ = − 2πx/λ = − 2πθ/T $$

Les vibrations de M et de S sont **en phase** si Δφ = 0 modulo 2π, **en opposition de phase** si Δφ = π modulo 2π, **en quadrature** si Δφ = ±π/2 modulo 2π (retard de phase pour −π/2, avance de phase pour +π/2).
:::

::: figure Oscillogramme bicourbe pour N = 1250 Hz et d = 0,340 m (base de temps 0,2 ms/div) : C₂ est décalée de θ′ par rapport à C₁ ; les amplitudes sont des valeurs d'illustration
<svg viewBox="0 0 308 196"><title>Oscillogramme bicourbe : la courbe C₂ du microphone est décalée de θ′ par rapport à la courbe C₁ du haut-parleur, avec une période de 4 divisions</title><rect x="24" y="14" width="280" height="168" fill="none" stroke="#0f172a" stroke-width="2"/><line x1="52" y1="14" x2="52" y2="182" stroke="#e2e8f0" stroke-width="1"/><line x1="80" y1="14" x2="80" y2="182" stroke="#e2e8f0" stroke-width="1"/><line x1="108" y1="14" x2="108" y2="182" stroke="#e2e8f0" stroke-width="1"/><line x1="136" y1="14" x2="136" y2="182" stroke="#e2e8f0" stroke-width="1"/><line x1="164" y1="14" x2="164" y2="182" stroke="#e2e8f0" stroke-width="1.6"/><line x1="192" y1="14" x2="192" y2="182" stroke="#e2e8f0" stroke-width="1"/><line x1="220" y1="14" x2="220" y2="182" stroke="#e2e8f0" stroke-width="1"/><line x1="248" y1="14" x2="248" y2="182" stroke="#e2e8f0" stroke-width="1"/><line x1="276" y1="14" x2="276" y2="182" stroke="#e2e8f0" stroke-width="1"/><line x1="24" y1="42" x2="304" y2="42" stroke="#e2e8f0" stroke-width="1"/><line x1="24" y1="70" x2="304" y2="70" stroke="#e2e8f0" stroke-width="1"/><line x1="24" y1="98" x2="304" y2="98" stroke="#e2e8f0" stroke-width="1.6"/><line x1="24" y1="126" x2="304" y2="126" stroke="#e2e8f0" stroke-width="1"/><line x1="24" y1="154" x2="304" y2="154" stroke="#e2e8f0" stroke-width="1"/><polyline points="24,98 25.4,93.61 26.8,89.24 28.2,84.93 29.6,80.7 31,76.57 32.4,72.58 33.8,68.74 35.2,65.08 36.6,61.63 38,58.4 39.4,55.42 40.8,52.7 42.2,50.25 43.6,48.1 45,46.26 46.4,44.74 47.8,43.55 49.2,42.69 50.6,42.17 52,42 53.4,42.17 54.8,42.69 56.2,43.55 57.6,44.74 59,46.26 60.4,48.1 61.8,50.25 63.2,52.7 64.6,55.42 66,58.4 67.4,61.63 68.8,65.08 70.2,68.74 71.6,72.58 73,76.57 74.4,80.7 75.8,84.93 77.2,89.24 78.6,93.61 80,98 81.4,102.39 82.8,106.76 84.2,111.07 85.6,115.3 87,119.43 88.4,123.42 89.8,127.26 91.2,130.92 92.6,134.37 94,137.6 95.4,140.58 96.8,143.3 98.2,145.75 99.6,147.9 101,149.74 102.4,151.26 103.8,152.45 105.2,153.31 106.6,153.83 108,154 109.4,153.83 110.8,153.31 112.2,152.45 113.6,151.26 115,149.74 116.4,147.9 117.8,145.75 119.2,143.3 120.6,140.58 122,137.6 123.4,134.37 124.8,130.92 126.2,127.26 127.6,123.42 129,119.43 130.4,115.3 131.8,111.07 133.2,106.76 134.6,102.39 136,98 137.4,93.61 138.8,89.24 140.2,84.93 141.6,80.7 143,76.57 144.4,72.58 145.8,68.74 147.2,65.08 148.6,61.63 150,58.4 151.4,55.42 152.8,52.7 154.2,50.25 155.6,48.1 157,46.26 158.4,44.74 159.8,43.55 161.2,42.69 162.6,42.17 164,42 165.4,42.17 166.8,42.69 168.2,43.55 169.6,44.74 171,46.26 172.4,48.1 173.8,50.25 175.2,52.7 176.6,55.42 178,58.4 179.4,61.63 180.8,65.08 182.2,68.74 183.6,72.58 185,76.57 186.4,80.7 187.8,84.93 189.2,89.24 190.6,93.61 192,98 193.4,102.39 194.8,106.76 196.2,111.07 197.6,115.3 199,119.43 200.4,123.42 201.8,127.26 203.2,130.92 204.6,134.37 206,137.6 207.4,140.58 208.8,143.3 210.2,145.75 211.6,147.9 213,149.74 214.4,151.26 215.8,152.45 217.2,153.31 218.6,153.83 220,154 221.4,153.83 222.8,153.31 224.2,152.45 225.6,151.26 227,149.74 228.4,147.9 229.8,145.75 231.2,143.3 232.6,140.58 234,137.6 235.4,134.37 236.8,130.92 238.2,127.26 239.6,123.42 241,119.43 242.4,115.3 243.8,111.07 245.2,106.76 246.6,102.39 248,98 249.4,93.61 250.8,89.24 252.2,84.93 253.6,80.7 255,76.57 256.4,72.58 257.8,68.74 259.2,65.08 260.6,61.63 262,58.4 263.4,55.42 264.8,52.7 266.2,50.25 267.6,48.1 269,46.26 270.4,44.74 271.8,43.55 273.2,42.69 274.6,42.17 276,42 277.4,42.17 278.8,42.69 280.2,43.55 281.6,44.74 283,46.26 284.4,48.1 285.8,50.25 287.2,52.7 288.6,55.42 290,58.4 291.4,61.63 292.8,65.08 294.2,68.74 295.6,72.58 297,76.57 298.4,80.7 299.8,84.93 301.2,89.24 302.6,93.61 304,98" fill="none" stroke="#0f172a" stroke-width="2.4"/><polyline points="24,126 25.4,125.91 26.8,125.66 28.2,125.23 29.6,124.63 31,123.87 32.4,122.95 33.8,121.87 35.2,120.65 36.6,119.29 38,117.8 39.4,116.18 40.8,114.46 42.2,112.63 43.6,110.71 45,108.72 46.4,106.65 47.8,104.54 49.2,102.38 50.6,100.2 52,98 53.4,95.8 54.8,93.62 56.2,91.46 57.6,89.35 59,87.28 60.4,85.29 61.8,83.37 63.2,81.54 64.6,79.82 66,78.2 67.4,76.71 68.8,75.35 70.2,74.13 71.6,73.05 73,72.13 74.4,71.37 75.8,70.77 77.2,70.34 78.6,70.09 80,70 81.4,70.09 82.8,70.34 84.2,70.77 85.6,71.37 87,72.13 88.4,73.05 89.8,74.13 91.2,75.35 92.6,76.71 94,78.2 95.4,79.82 96.8,81.54 98.2,83.37 99.6,85.29 101,87.28 102.4,89.35 103.8,91.46 105.2,93.62 106.6,95.8 108,98 109.4,100.2 110.8,102.38 112.2,104.54 113.6,106.65 115,108.72 116.4,110.71 117.8,112.63 119.2,114.46 120.6,116.18 122,117.8 123.4,119.29 124.8,120.65 126.2,121.87 127.6,122.95 129,123.87 130.4,124.63 131.8,125.23 133.2,125.66 134.6,125.91 136,126 137.4,125.91 138.8,125.66 140.2,125.23 141.6,124.63 143,123.87 144.4,122.95 145.8,121.87 147.2,120.65 148.6,119.29 150,117.8 151.4,116.18 152.8,114.46 154.2,112.63 155.6,110.71 157,108.72 158.4,106.65 159.8,104.54 161.2,102.38 162.6,100.2 164,98 165.4,95.8 166.8,93.62 168.2,91.46 169.6,89.35 171,87.28 172.4,85.29 173.8,83.37 175.2,81.54 176.6,79.82 178,78.2 179.4,76.71 180.8,75.35 182.2,74.13 183.6,73.05 185,72.13 186.4,71.37 187.8,70.77 189.2,70.34 190.6,70.09 192,70 193.4,70.09 194.8,70.34 196.2,70.77 197.6,71.37 199,72.13 200.4,73.05 201.8,74.13 203.2,75.35 204.6,76.71 206,78.2 207.4,79.82 208.8,81.54 210.2,83.37 211.6,85.29 213,87.28 214.4,89.35 215.8,91.46 217.2,93.62 218.6,95.8 220,98 221.4,100.2 222.8,102.38 224.2,104.54 225.6,106.65 227,108.72 228.4,110.71 229.8,112.63 231.2,114.46 232.6,116.18 234,117.8 235.4,119.29 236.8,120.65 238.2,121.87 239.6,122.95 241,123.87 242.4,124.63 243.8,125.23 245.2,125.66 246.6,125.91 248,126 249.4,125.91 250.8,125.66 252.2,125.23 253.6,124.63 255,123.87 256.4,122.95 257.8,121.87 259.2,120.65 260.6,119.29 262,117.8 263.4,116.18 264.8,114.46 266.2,112.63 267.6,110.71 269,108.72 270.4,106.65 271.8,104.54 273.2,102.38 274.6,100.2 276,98 277.4,95.8 278.8,93.62 280.2,91.46 281.6,89.35 283,87.28 284.4,85.29 285.8,83.37 287.2,81.54 288.6,79.82 290,78.2 291.4,76.71 292.8,75.35 294.2,74.13 295.6,73.05 297,72.13 298.4,71.37 299.8,70.77 301.2,70.34 302.6,70.09 304,70" fill="none" stroke="#0f6e56" stroke-width="2.4"/><line x1="136" y1="64.4" x2="136" y2="131.6" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="164" y1="64.4" x2="164" y2="131.6" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="136" y1="128.8" x2="164" y2="128.8" stroke="#d97706" stroke-width="2.2"/><polygon points="164,128.8 158,131.8 158,125.8" fill="#d97706"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="168" y="143.8" text-anchor="middle" fill="#d97706" font-size="13">θ′</text><text x="296" y="28" text-anchor="end" fill="#0f172a" font-size="13">C₁</text><text x="296" y="44" text-anchor="end" fill="#0f6e56" font-size="13">C₂</text></g></svg>
:::

Sur l'écran, C₁ (noire) est la tension du haut-parleur, C₂ (verte) celle du microphone, et θ′ est le décalage lu entre deux passages montants par zéro, de C₁ puis de C₂.

::: exemple Le microphone à d = 0,340 m du haut-parleur (v = 340 m/s)

1. T = 1/N = 0,80 ms et λ = v/N = 340/1250 = 0,272 m. Avec 0,2 ms/div, T occupe 4 divisions de l'écran.
2. d/λ = 0,340/0,272 = 1,25, donc Δφ = −2π × 1,25 = −2,5π. On retranche 2π : Δφ = −π/2, la vibration du microphone est en quadrature retard sur celle du haut-parleur.
3. Le retard réel du son est θ = d/v = 0,340/340 = 1,00 ms, soit 1,25 T.
4. L'écran ne montre que le reste modulo T : θ′ = θ − T = 0,20 ms = 1 division, ce qui retrouve la figure. Alors Δt = n·T + θ′ avec n = 1 : 1,00 = 0,80 + 0,20 ✓.

:::

::: piege
**Erreur : prendre le décalage lu sur l'écran pour le temps de propagation.** Ici θ′ = 0,20 ms (étape 4) alors que le son a mis 1,00 ms. L'erreur tente parce que c'est le seul décalage qu'on voit. Mais l'écran répète les courbes à chaque période : le décalage visible est le reste modulo T. Avec θ′, on trouverait v = d/θ′ = 0,340/0,00020 = 1700 m/s, cinq fois trop pour de l'air.
:::

| Vibration de M par rapport à S | Δφ (modulo 2π) | Position x de M |
| --- | --- | --- |
| en phase | 0 | x = kλ |
| en opposition de phase | π | x = (2k + 1)λ/2 |
| en quadrature retard | −π/2 | x = (4k + 1)λ/4 |
| en quadrature avance | +π/2 | x = (4k + 3)λ/4 |

::: propriete
**Ce qui reste vrai** — Avec k entier naturel, les positions du tableau sont celles des points effectivement atteints : leur nombre est limité par la longueur de la corde (x ≤ ℓ) ou par le front de l'onde. Pour comparer deux points M₁ et M₂ (x₂ > x₁), on remplace x par x₂ − x₁ : Δφ = φ₂ − φ₁ = −2π(x₂ − x₁)/λ. Deux positions successives du microphone où les courbes sont en phase (elles passent par zéro en même temps, dans le même sens) sont distantes d'une longueur d'onde ; on en tire v = λ·N. Cas limite : la première quadrature avance est à 3λ/4, car à λ/4 la vibration est déjà en retard et non en avance.
:::

::: verifie À toi : mesurer la célérité du son
Un haut-parleur émet à N = 1700 Hz. Les courbes C₁ et C₂ sont en phase (elles passent par zéro en même temps, dans le même sens) pour des positions successives du microphone à 12,0 cm puis 32,0 cm. Calculer λ puis v, et donner la position, entre ces deux-là, où les courbes sont en miroir.

---

Deux positions successives en phase sont séparées de λ : λ = 32,0 − 12,0 = 20,0 cm, donc v = λ·N = 0,200 × 1700 = 340 m/s. Les courbes sont en miroir (opposition de phase) à une demi-longueur d'onde de la première position : 12,0 + 10,0 = 22,0 cm.
:::

::: retenir
Δφ = −2πx/λ = −2πθ/T : en phase pour x = kλ, en opposition pour x = (2k + 1)λ/2, en quadrature retard pour x = (4k + 1)λ/4 ; l'écran ne montre que θ modulo T.
:::

## 📸 L'aspect de la corde à un instant donné : la sinusoïde des espaces et son front

Toujours la corde du vibreur (N = 25 Hz ; v = 5,0 m/s ; a = 3,0 mm), la source ayant démarré à t = 0 en montant. À l'instant t₁ = 110 ms on la photographie devant une règle graduée : elle ne vibre que sur une partie de sa longueur.
Où s'arrête l'onde, et quelle forme a la corde ?

::: definition
**Aspect de la corde et front d'onde** — À un instant t, la corde est une sinusoïde de la variable x, de période λ : yt(x) = a sin(ωt − 2πx/λ), tant que x ≤ xf. Au-delà du **front d'onde**, d'abscisse xf = v·t = n·λ avec n = t/T, la corde est encore au repos.
:::

::: figure Aspect de la corde à t₁ = 110 ms : sinusoïde de période λ = 0,20 m entre la source S et le front d'onde xf = 0,55 m, corde au repos au-delà
<svg viewBox="0 0 340 202"><title>Aspect de la corde à t = 110 ms : sinusoïde de période spatiale 0,20 m entre la source et le front d'onde situé à 0,55 m, corde au repos au-delà</title><line x1="24" y1="99" x2="336" y2="99" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,99 328,103 328,95" fill="#0f172a"/><line x1="30" y1="182" x2="30" y2="12" stroke="#0f172a" stroke-width="1.6"/><polygon points="30,12 34,20 26,20" fill="#0f172a"/><polyline points="30,152.57 30.74,152.47 31.48,152.15 32.22,151.62 32.96,150.89 33.7,149.95 34.44,148.81 35.18,147.47 35.92,145.95 36.66,144.23 37.4,142.34 38.14,140.28 38.88,138.05 39.62,135.67 40.36,133.15 41.1,130.49 41.84,127.71 42.58,124.81 43.32,121.81 44.06,118.72 44.8,115.55 45.54,112.32 46.28,109.04 47.02,105.71 47.76,102.36 48.5,99 49.24,95.64 49.98,92.29 50.72,88.96 51.46,85.68 52.2,82.45 52.94,79.28 53.68,76.19 54.42,73.19 55.16,70.29 55.9,67.51 56.64,64.85 57.38,62.33 58.12,59.95 58.86,57.72 59.6,55.66 60.34,53.77 61.08,52.05 61.82,50.53 62.56,49.19 63.3,48.05 64.04,47.11 64.78,46.38 65.52,45.85 66.26,45.53 67,45.43 67.74,45.53 68.48,45.85 69.22,46.38 69.96,47.11 70.7,48.05 71.44,49.19 72.18,50.53 72.92,52.05 73.66,53.77 74.4,55.66 75.14,57.72 75.88,59.95 76.62,62.33 77.36,64.85 78.1,67.51 78.84,70.29 79.58,73.19 80.32,76.19 81.06,79.28 81.8,82.45 82.54,85.68 83.28,88.96 84.02,92.29 84.76,95.64 85.5,99 86.24,102.36 86.98,105.71 87.72,109.04 88.46,112.32 89.2,115.55 89.94,118.72 90.68,121.81 91.42,124.81 92.16,127.71 92.9,130.49 93.64,133.15 94.38,135.67 95.12,138.05 95.86,140.28 96.6,142.34 97.34,144.23 98.08,145.95 98.82,147.47 99.56,148.81 100.3,149.95 101.04,150.89 101.78,151.62 102.52,152.15 103.26,152.47 104,152.57 104.74,152.47 105.48,152.15 106.22,151.62 106.96,150.89 107.7,149.95 108.44,148.81 109.18,147.47 109.92,145.95 110.66,144.23 111.4,142.34 112.14,140.28 112.88,138.05 113.62,135.67 114.36,133.15 115.1,130.49 115.84,127.71 116.58,124.81 117.32,121.81 118.06,118.72 118.8,115.55 119.54,112.32 120.28,109.04 121.02,105.71 121.76,102.36 122.5,99 123.24,95.64 123.98,92.29 124.72,88.96 125.46,85.68 126.2,82.45 126.94,79.28 127.68,76.19 128.42,73.19 129.16,70.29 129.9,67.51 130.64,64.85 131.38,62.33 132.12,59.95 132.86,57.72 133.6,55.66 134.34,53.77 135.08,52.05 135.82,50.53 136.56,49.19 137.3,48.05 138.04,47.11 138.78,46.38 139.52,45.85 140.26,45.53 141,45.43 141.74,45.53 142.48,45.85 143.22,46.38 143.96,47.11 144.7,48.05 145.44,49.19 146.18,50.53 146.92,52.05 147.66,53.77 148.4,55.66 149.14,57.72 149.88,59.95 150.62,62.33 151.36,64.85 152.1,67.51 152.84,70.29 153.58,73.19 154.32,76.19 155.06,79.28 155.8,82.45 156.54,85.68 157.28,88.96 158.02,92.29 158.76,95.64 159.5,99 160.24,102.36 160.98,105.71 161.72,109.04 162.46,112.32 163.2,115.55 163.94,118.72 164.68,121.81 165.42,124.81 166.16,127.71 166.9,130.49 167.64,133.15 168.38,135.67 169.12,138.05 169.86,140.28 170.6,142.34 171.34,144.23 172.08,145.95 172.82,147.47 173.56,148.81 174.3,149.95 175.04,150.89 175.78,151.62 176.52,152.15 177.26,152.47 178,152.57 178.74,152.47 179.48,152.15 180.22,151.62 180.96,150.89 181.7,149.95 182.44,148.81 183.18,147.47 183.92,145.95 184.66,144.23 185.4,142.34 186.14,140.28 186.88,138.05 187.62,135.67 188.36,133.15 189.1,130.49 189.84,127.71 190.58,124.81 191.32,121.81 192.06,118.72 192.8,115.55 193.54,112.32 194.28,109.04 195.02,105.71 195.76,102.36 196.5,99 197.24,95.64 197.98,92.29 198.72,88.96 199.46,85.68 200.2,82.45 200.94,79.28 201.68,76.19 202.42,73.19 203.16,70.29 203.9,67.51 204.64,64.85 205.38,62.33 206.12,59.95 206.86,57.72 207.6,55.66 208.34,53.77 209.08,52.05 209.82,50.53 210.56,49.19 211.3,48.05 212.04,47.11 212.78,46.38 213.52,45.85 214.26,45.53 215,45.43 215.74,45.53 216.48,45.85 217.22,46.38 217.96,47.11 218.7,48.05 219.44,49.19 220.18,50.53 220.92,52.05 221.66,53.77 222.4,55.66 223.14,57.72 223.88,59.95 224.62,62.33 225.36,64.85 226.1,67.51 226.84,70.29 227.58,73.19 228.32,76.19 229.06,79.28 229.8,82.45 230.54,85.68 231.28,88.96 232.02,92.29 232.76,95.64 233.5,99 233.5,99 326,99" fill="none" stroke="#0f172a" stroke-width="2.6"/><line x1="30" y1="95" x2="30" y2="103" stroke="#0f172a" stroke-width="1.4"/><line x1="104" y1="95" x2="104" y2="103" stroke="#0f172a" stroke-width="1.4"/><line x1="178" y1="95" x2="178" y2="103" stroke="#0f172a" stroke-width="1.4"/><line x1="252" y1="95" x2="252" y2="103" stroke="#0f172a" stroke-width="1.4"/><line x1="326" y1="95" x2="326" y2="103" stroke="#0f172a" stroke-width="1.4"/><line x1="67" y1="96" x2="67" y2="102" stroke="#0f172a" stroke-width="1"/><line x1="141" y1="96" x2="141" y2="102" stroke="#0f172a" stroke-width="1"/><line x1="215" y1="96" x2="215" y2="102" stroke="#0f172a" stroke-width="1"/><line x1="289" y1="96" x2="289" y2="102" stroke="#0f172a" stroke-width="1"/><line x1="26" y1="45.43" x2="34" y2="45.43" stroke="#0f172a" stroke-width="1.4"/><line x1="26" y1="152.57" x2="34" y2="152.57" stroke="#0f172a" stroke-width="1.4"/><line x1="67" y1="22" x2="67" y2="43.43" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="141" y1="22" x2="141" y2="43.43" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="67" y1="24" x2="141" y2="24" stroke="#0f6e56" stroke-width="2.2"/><polygon points="141,24 134,27.5 134,20.5" fill="#0f6e56"/><line x1="141" y1="24" x2="67" y2="24" stroke="#0f6e56" stroke-width="2.2"/><polygon points="67,24 74,20.5 74,27.5" fill="#0f6e56"/><line x1="233.5" y1="162.75" x2="233.5" y2="35.25" stroke="#d97706" stroke-width="1.8" stroke-dasharray="4 3"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="30" y="116" text-anchor="middle" fill="#0f172a" font-size="11">0</text><text x="104" y="116" text-anchor="middle" fill="#0f172a" font-size="11">0,2</text><text x="178" y="116" text-anchor="middle" fill="#0f172a" font-size="11">0,4</text><text x="252" y="116" text-anchor="middle" fill="#0f172a" font-size="11">0,6</text><text x="326" y="116" text-anchor="middle" fill="#0f172a" font-size="11">0,8</text><text x="22" y="49.43" text-anchor="end" fill="#0f172a" font-size="11">+3</text><text x="22" y="156.57" text-anchor="end" fill="#0f172a" font-size="11">−3</text><text x="334" y="91" text-anchor="end" fill="#0f172a" font-size="11">x (m)</text><text x="4" y="9" text-anchor="start" fill="#0f172a" font-size="11">y (mm)</text><text x="104" y="18" text-anchor="middle" fill="#0f6e56" font-size="12">λ = 0,20 m</text><text x="233.5" y="176.75" text-anchor="middle" fill="#d97706" font-size="12">front x<tspan baseline-shift="sub" font-size="9">f</tspan> = 0,55 m</text></g><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="32" y="170.57" text-anchor="middle" fill="#0f172a" font-size="13">S</text></g></svg>
:::

Sur la figure, la sinusoïde a pour période λ entre S et le front xf, et la corde est plate au-delà : ce graphe est celui de y en fonction de x, pas de y en fonction de t.

::: exemple Tracer l'aspect de la corde à t₁ = 110 ms

1. T = 40 ms, donc n = t₁/T = 110/40 = 2,75 et xf = v·t₁ = 5,0 × 0,110 = 0,55 m = 2,75 λ, avec λ = 0,20 m. Pour x > xf, la corde est au repos.
2. ωt₁ = 50π × 0,110 = 5,5π, soit 1,5π modulo 2π. Pour x ≤ xf : y = a sin(1,5π − 2πx/λ) = −a cos(2πx/λ).
3. Contrôle : en x = 0, y = −a, et la source est bien à son minimum à cet instant (yS = a sin 5,5π = −a) ; en x = xf, y = −a cos(5,5π) = 0, le front est au repos ✓.
4. Méthode rapide : on dessine la sinusoïde de période λ en partant du front, juste derrière lequel la corde est au-dessus de l'axe puisque la source a démarré en montant.
5. À t₂ = 130 ms, l'onde a avancé de v(t₂ − t₁) = 5,0 × 0,020 = 0,10 m = λ/2 : xf2 = 0,65 m, et toute la sinusoïde est décalée de 0,10 m vers la droite.

:::

::: piege
**Erreur : lire 0,20 m entre deux crêtes de cet aspect et en faire une période T de 0,20 s.** L'erreur tente parce que la courbe a la même forme que le diagramme de mouvement d'un point. Mais l'abscisse est ici une position : la distance entre deux crêtes est la longueur d'onde λ (étape 1 : λ = 0,20 m, alors que T = 40 ms).
:::

::: methode
**Monter ou descendre ?** — Pour savoir si un point de la corde monte ou descend à l'instant de la photo, on décale la courbe de quelques millimètres vers la droite : le point prend la valeur qu'avait son voisin de gauche, plus proche de la source. Si ce voisin est plus haut, le point monte ; s'il est plus bas, il descend. Sur la figure, le point d'abscisse 0,05 m (y = 0) a un voisin de gauche plus bas : il descend.
:::

::: propriete
**Ce qui reste vrai** — Tant que xf < ℓ, une partie de la corde est au repos ; dès que xf dépasse la longueur de la corde, toute la corde vibre et l'aspect est une sinusoïde complète de période λ. Cas limite : à t < T, l'onde n'a pas encore parcouru une longueur d'onde, et la corde n'est ébranlée que sur un arc de sinusoïde.
:::

::: verifie À toi : un autre instant
Même corde, à t = 90 ms. Calculer xf puis donner y en fonction de x pour x ≤ xf.

---

n = 90/40 = 2,25, donc xf = v·t = 5,0 × 0,090 = 0,45 m = 2,25 λ. ωt = 50π × 0,090 = 4,5π, soit 0,5π modulo 2π : y = a sin(0,5π − 2πx/λ) = a cos(2πx/λ) pour x ≤ 0,45 m ; au-delà la corde est au repos. Contrôle : en x = xf, cos(4,5π) = 0 ✓.
:::

::: retenir
À l'instant t, y(x) = a sin(ωt − 2πx/λ) jusqu'au front xf = v·t = n·λ, corde au repos au-delà ; la période de cette courbe est λ, pas T.
:::

## 🔦 Le stroboscope : figer ou ralentir une onde

La corde du vibreur (N = 25 Hz) vibre trop vite pour l'œil, qui garde une impression lumineuse pendant environ 0,1 s : on ne voit qu'une bande floue. Un stroboscope envoie des éclairs brefs, à intervalles réguliers Te, au lieu d'une lumière continue.
Comment régler Te pour figer la corde, ou pour la voir au ralenti ?

::: definition
**Stroboscopie** — Un stroboscope émet des éclairs de période Te, de fréquence Ne = 1/Te. On observe une **immobilité apparente** lorsque Te = kT, avec k entier non nul, c'est-à-dire Ne = N/k. Si Te est légèrement supérieure à kT, l'onde semble avancer lentement dans le sens réel ; si Te est légèrement inférieure à kT, elle semble avancer lentement en sens inverse.
:::

::: figure Un point qui oscille à 25 Hz (courbe grise) éclairé à 24 Hz (points orange) : d'un éclair au suivant, le point a fait un tour et un tout petit peu plus, d'où un mouvement apparent lent
<svg viewBox="0 0 340 176"><title>Stroboscope à 24 Hz éclairant un point qui oscille à 25 Hz : les éclairs, en orange, saisissent le point presque dans le même état à chaque fois, d'où un mouvement apparent très lent</title><line x1="30" y1="88" x2="336" y2="88" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,88 328,92 328,84" fill="#0f172a"/><line x1="36" y1="156" x2="36" y2="20" stroke="#0f172a" stroke-width="1.6"/><polygon points="36,20 40,28 32,28" fill="#0f172a"/><polyline points="36,37.57 36.74,38.19 37.48,40.03 38.22,43.06 38.96,47.2 39.7,52.34 40.44,58.36 41.18,65.1 41.92,72.41 42.66,80.11 43.4,88 44.14,95.89 44.88,103.59 45.62,110.9 46.36,117.64 47.1,123.66 47.84,128.8 48.58,132.94 49.32,135.97 50.06,137.81 50.8,138.43 51.54,137.81 52.28,135.97 53.02,132.94 53.76,128.8 54.5,123.66 55.24,117.64 55.98,110.9 56.72,103.59 57.46,95.89 58.2,88 58.94,80.11 59.68,72.41 60.42,65.1 61.16,58.36 61.9,52.34 62.64,47.2 63.38,43.06 64.12,40.03 64.86,38.19 65.6,37.57 66.34,38.19 67.08,40.03 67.82,43.06 68.56,47.2 69.3,52.34 70.04,58.36 70.78,65.1 71.52,72.41 72.26,80.11 73,88 73.74,95.89 74.48,103.59 75.22,110.9 75.96,117.64 76.7,123.66 77.44,128.8 78.18,132.94 78.92,135.97 79.66,137.81 80.4,138.43 81.14,137.81 81.88,135.97 82.62,132.94 83.36,128.8 84.1,123.66 84.84,117.64 85.58,110.9 86.32,103.59 87.06,95.89 87.8,88 88.54,80.11 89.28,72.41 90.02,65.1 90.76,58.36 91.5,52.34 92.24,47.2 92.98,43.06 93.72,40.03 94.46,38.19 95.2,37.57 95.94,38.19 96.68,40.03 97.42,43.06 98.16,47.2 98.9,52.34 99.64,58.36 100.38,65.1 101.12,72.41 101.86,80.11 102.6,88 103.34,95.89 104.08,103.59 104.82,110.9 105.56,117.64 106.3,123.66 107.04,128.8 107.78,132.94 108.52,135.97 109.26,137.81 110,138.43 110.74,137.81 111.48,135.97 112.22,132.94 112.96,128.8 113.7,123.66 114.44,117.64 115.18,110.9 115.92,103.59 116.66,95.89 117.4,88 118.14,80.11 118.88,72.41 119.62,65.1 120.36,58.36 121.1,52.34 121.84,47.2 122.58,43.06 123.32,40.03 124.06,38.19 124.8,37.57 125.54,38.19 126.28,40.03 127.02,43.06 127.76,47.2 128.5,52.34 129.24,58.36 129.98,65.1 130.72,72.41 131.46,80.11 132.2,88 132.94,95.89 133.68,103.59 134.42,110.9 135.16,117.64 135.9,123.66 136.64,128.8 137.38,132.94 138.12,135.97 138.86,137.81 139.6,138.43 140.34,137.81 141.08,135.97 141.82,132.94 142.56,128.8 143.3,123.66 144.04,117.64 144.78,110.9 145.52,103.59 146.26,95.89 147,88 147.74,80.11 148.48,72.41 149.22,65.1 149.96,58.36 150.7,52.34 151.44,47.2 152.18,43.06 152.92,40.03 153.66,38.19 154.4,37.57 155.14,38.19 155.88,40.03 156.62,43.06 157.36,47.2 158.1,52.34 158.84,58.36 159.58,65.1 160.32,72.41 161.06,80.11 161.8,88 162.54,95.89 163.28,103.59 164.02,110.9 164.76,117.64 165.5,123.66 166.24,128.8 166.98,132.94 167.72,135.97 168.46,137.81 169.2,138.43 169.94,137.81 170.68,135.97 171.42,132.94 172.16,128.8 172.9,123.66 173.64,117.64 174.38,110.9 175.12,103.59 175.86,95.89 176.6,88 177.34,80.11 178.08,72.41 178.82,65.1 179.56,58.36 180.3,52.34 181.04,47.2 181.78,43.06 182.52,40.03 183.26,38.19 184,37.57 184.74,38.19 185.48,40.03 186.22,43.06 186.96,47.2 187.7,52.34 188.44,58.36 189.18,65.1 189.92,72.41 190.66,80.11 191.4,88 192.14,95.89 192.88,103.59 193.62,110.9 194.36,117.64 195.1,123.66 195.84,128.8 196.58,132.94 197.32,135.97 198.06,137.81 198.8,138.43 199.54,137.81 200.28,135.97 201.02,132.94 201.76,128.8 202.5,123.66 203.24,117.64 203.98,110.9 204.72,103.59 205.46,95.89 206.2,88 206.94,80.11 207.68,72.41 208.42,65.1 209.16,58.36 209.9,52.34 210.64,47.2 211.38,43.06 212.12,40.03 212.86,38.19 213.6,37.57 214.34,38.19 215.08,40.03 215.82,43.06 216.56,47.2 217.3,52.34 218.04,58.36 218.78,65.1 219.52,72.41 220.26,80.11 221,88 221.74,95.89 222.48,103.59 223.22,110.9 223.96,117.64 224.7,123.66 225.44,128.8 226.18,132.94 226.92,135.97 227.66,137.81 228.4,138.43 229.14,137.81 229.88,135.97 230.62,132.94 231.36,128.8 232.1,123.66 232.84,117.64 233.58,110.9 234.32,103.59 235.06,95.89 235.8,88 236.54,80.11 237.28,72.41 238.02,65.1 238.76,58.36 239.5,52.34 240.24,47.2 240.98,43.06 241.72,40.03 242.46,38.19 243.2,37.57 243.94,38.19 244.68,40.03 245.42,43.06 246.16,47.2 246.9,52.34 247.64,58.36 248.38,65.1 249.12,72.41 249.86,80.11 250.6,88 251.34,95.89 252.08,103.59 252.82,110.9 253.56,117.64 254.3,123.66 255.04,128.8 255.78,132.94 256.52,135.97 257.26,137.81 258,138.43 258.74,137.81 259.48,135.97 260.22,132.94 260.96,128.8 261.7,123.66 262.44,117.64 263.18,110.9 263.92,103.59 264.66,95.89 265.4,88 266.14,80.11 266.88,72.41 267.62,65.1 268.36,58.36 269.1,52.34 269.84,47.2 270.58,43.06 271.32,40.03 272.06,38.19 272.8,37.57 273.54,38.19 274.28,40.03 275.02,43.06 275.76,47.2 276.5,52.34 277.24,58.36 277.98,65.1 278.72,72.41 279.46,80.11 280.2,88 280.94,95.89 281.68,103.59 282.42,110.9 283.16,117.64 283.9,123.66 284.64,128.8 285.38,132.94 286.12,135.97 286.86,137.81 287.6,138.43 288.34,137.81 289.08,135.97 289.82,132.94 290.56,128.8 291.3,123.66 292.04,117.64 292.78,110.9 293.52,103.59 294.26,95.89 295,88 295.74,80.11 296.48,72.41 297.22,65.1 297.96,58.36 298.7,52.34 299.44,47.2 300.18,43.06 300.92,40.03 301.66,38.19 302.4,37.57 303.14,38.19 303.88,40.03 304.62,43.06 305.36,47.2 306.1,52.34 306.84,58.36 307.58,65.1 308.32,72.41 309.06,80.11 309.8,88 310.54,95.89 311.28,103.59 312.02,110.9 312.76,117.64 313.5,123.66 314.24,128.8 314.98,132.94 315.72,135.97 316.46,137.81 317.2,138.43 317.94,137.81 318.68,135.97 319.42,132.94 320.16,128.8 320.9,123.66 321.64,117.64 322.38,110.9 323.12,103.59 323.86,95.89 324.6,88 325.34,80.11 326.08,72.41 326.82,65.1 327.56,58.36 328.3,52.34 329.04,47.2 329.78,43.06 330.52,40.03 331.26,38.19 332,37.57" fill="none" stroke="#64748b" stroke-width="1.8"/><polyline points="36,37.57 66.83,39.28 97.67,44.32 128.5,52.34 159.33,62.78 190.17,74.95 221,88 251.83,101.05 282.67,113.22 313.5,123.66" fill="none" stroke="#d97706" stroke-width="1.6" stroke-dasharray="4 3"/><line x1="36" y1="37.57" x2="36" y2="88" stroke="#d97706" stroke-width="1"/><circle cx="36" cy="37.57" r="4.6" fill="#d97706" stroke="#0f172a" stroke-width="1.4"/><line x1="66.83" y1="39.28" x2="66.83" y2="88" stroke="#d97706" stroke-width="1"/><circle cx="66.83" cy="39.28" r="4.6" fill="#d97706" stroke="#0f172a" stroke-width="1.4"/><line x1="97.67" y1="44.32" x2="97.67" y2="88" stroke="#d97706" stroke-width="1"/><circle cx="97.67" cy="44.32" r="4.6" fill="#d97706" stroke="#0f172a" stroke-width="1.4"/><line x1="128.5" y1="52.34" x2="128.5" y2="88" stroke="#d97706" stroke-width="1"/><circle cx="128.5" cy="52.34" r="4.6" fill="#d97706" stroke="#0f172a" stroke-width="1.4"/><line x1="159.33" y1="62.78" x2="159.33" y2="88" stroke="#d97706" stroke-width="1"/><circle cx="159.33" cy="62.78" r="4.6" fill="#d97706" stroke="#0f172a" stroke-width="1.4"/><line x1="190.17" y1="74.95" x2="190.17" y2="88" stroke="#d97706" stroke-width="1"/><circle cx="190.17" cy="74.95" r="4.6" fill="#d97706" stroke="#0f172a" stroke-width="1.4"/><line x1="221" y1="88" x2="221" y2="88" stroke="#d97706" stroke-width="1"/><circle cx="221" cy="88" r="4.6" fill="#d97706" stroke="#0f172a" stroke-width="1.4"/><line x1="251.83" y1="101.05" x2="251.83" y2="88" stroke="#d97706" stroke-width="1"/><circle cx="251.83" cy="101.05" r="4.6" fill="#d97706" stroke="#0f172a" stroke-width="1.4"/><line x1="282.67" y1="113.22" x2="282.67" y2="88" stroke="#d97706" stroke-width="1"/><circle cx="282.67" cy="113.22" r="4.6" fill="#d97706" stroke="#0f172a" stroke-width="1.4"/><line x1="313.5" y1="123.66" x2="313.5" y2="88" stroke="#d97706" stroke-width="1"/><circle cx="313.5" cy="123.66" r="4.6" fill="#d97706" stroke="#0f172a" stroke-width="1.4"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="36" y="122" text-anchor="middle" fill="#0f172a" font-size="11">0</text><text x="110" y="122" text-anchor="middle" fill="#0f172a" font-size="11">100</text><text x="184" y="122" text-anchor="middle" fill="#0f172a" font-size="11">200</text><text x="258" y="122" text-anchor="middle" fill="#0f172a" font-size="11">300</text><text x="332" y="122" text-anchor="middle" fill="#0f172a" font-size="11">400</text><text x="334" y="80" text-anchor="end" fill="#0f172a" font-size="11">t (ms)</text></g></svg>
:::

Sur la figure, la courbe grise est le mouvement réel d'un point, et les points orange sont ce que l'œil retient : d'un éclair au suivant, le point a fait un tour et un tout petit peu plus, d'où une succession lente.

::: exemple Régler le stroboscope sur la corde de N = 25 Hz (T = 40 ms)

1. Ne = 25 Hz : Te = 40 ms = T (k = 1). Entre deux éclairs, chaque point a fait une oscillation exacte et est dans le même état : la corde paraît figée, et on peut mesurer λ avec une règle.
2. Ne = 12,5 Hz : Te = 80 ms = 2T (k = 2). Deux oscillations exactes entre deux éclairs : la corde paraît encore figée.
3. Ne = 24 Hz : Te = 41,7 ms, un peu plus que T. Entre deux éclairs le point a fait une oscillation et un peu plus : on le revoit un peu plus loin dans son cycle, et l'onde paraît avancer lentement dans le sens réel.
4. Ne = 26 Hz : Te = 38,5 ms, un peu moins que T. On revoit le point un peu avant la fin de son cycle : l'onde paraît avancer lentement en sens inverse.
5. Ne = 12 Hz : Te = 83,3 ms, un peu plus que 2T = 80 ms (k = 2) : mouvement lent dans le sens réel.

:::

::: piege
**Erreur : croire qu'un stroboscope un peu plus rapide que la source fait avancer l'onde dans le sens réel**, parce que « plus d'éclairs, plus d'avance ». Pour Ne = 26 Hz (étape 4), Te est plus petite que T, et l'onde paraît reculer. L'erreur tente parce qu'on compare les fréquences. Ce qui décide du sens est la comparaison de Te avec kT : un éclair qui arrive trop tôt montre le point en retard dans son cycle.
:::

::: propriete
**Ce qui reste vrai** — L'immobilité se produit pour Ne = N/k (k = 1, 2, 3…). Cas limite : plus Te est proche de kT, plus le ralenti est lent ; à Te = kT exactement, il devient immobilité.
:::

::: verifie À toi : un vibreur de 60 Hz
Un vibreur oscille à N = 60 Hz ; le stroboscope est réglé sur Ne = 29 Hz. Quelle est l'apparence de l'onde ?

---

T = 1/60 = 16,7 ms et 2T = 33,3 ms. Te = 1/29 = 34,5 ms est un peu supérieure à 2T (k = 2) : l'onde paraît avancer lentement dans le sens réel.
:::

::: retenir
Immobilité si Te = kT (Ne = N/k) ; ralenti dans le sens réel si Te est un peu plus grande que kT, en sens inverse si elle est un peu plus petite.
:::

> 🏆 Quête franchie, héros ! Tu sais distinguer l'énergie qui voyage de la matière qui reste, classer une onde transversale ou longitudinale, calculer une célérité et une longueur d'onde, écrire l'équation horaire d'un point, lire un déphasage et un oscillogramme, tracer l'aspect d'une corde avec son front et régler un stroboscope. Le chapitre suivant tourne ce savoir vers la lumière.
