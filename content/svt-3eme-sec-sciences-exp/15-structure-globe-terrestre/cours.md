# 🌍 La structure et la composition du globe terrestre — lire l'intérieur de la Terre

> 💡 «Le forage le plus profond atteint 12 km, et le centre de la Terre est à 6370 km : tout le reste, on le déchiffre grâce aux séismes et aux volcans.»

Personne n'est jamais descendu au cœur de la Terre, et pourtant on sait qu'elle est faite de couches emboîtées, de quoi elles sont faites, et même lesquelles sont liquides. Huit notions montrent comment : le séisme et ses trois sortes d'ondes, le calcul de leur vitesse, les discontinuités et le Moho, le noyau liquide et sa graine solide, le modèle en couches, les produits des volcans, les roches et la composition du globe, enfin l'origine de la chaleur interne. Aucun préacquis particulier : seul compte le calcul d'une vitesse, distance divisée par durée.

## 🌋 Séisme et ondes sismiques : que lit-on sur un sismogramme ?

Le 19 septembre 1979, la station de Zaghouan a enregistré un séisme survenu au large de Zembra. Son tracé n'est pas une ligne agitée au hasard : on y repère trois groupes de secousses, l'un après l'autre.
D'où part un séisme, et pourquoi ses secousses arrivent-elles en trois temps ?

::: definition
**Séisme** — ensemble de secousses du sol, qui libère de l'énergie.
**Foyer** (ou hypocentre) — point d'origine du séisme, situé en profondeur.
**Épicentre** — point de la surface situé à la verticale du foyer.
**Onde sismique** — vibration qui part du foyer dans toutes les directions et se propage dans les roches ; elle emporte une partie de l'énergie libérée.
**Sismographe** (ou sismomètre) — appareil qui enregistre les secousses du sol ; son enregistrement est le **sismogramme**.
:::

::: figure Le séisme naît au foyer, en profondeur ; l'épicentre est le point de la surface à la verticale du foyer ; les ondes partent du foyer en cercles et gagnent les stations
<svg viewBox="0 0 340 215">
<title>Un séisme : foyer en profondeur, épicentre en surface, ondes vers deux stations</title>
<rect x="10" y="45" width="320" height="160" rx="0" fill="#f1f5f9"/>
<circle cx="130" cy="125" r="25" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
<circle cx="130" cy="125" r="50" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
<circle cx="130" cy="125" r="70" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="10" y1="45" x2="330" y2="45" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>
<line x1="130" y1="125" x2="246" y2="49" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/>
<line x1="130" y1="125" x2="64" y2="49" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/>
<line x1="130" y1="125" x2="130" y2="45" stroke="#0f172a" stroke-width="1.5" stroke-dasharray="4 3" stroke-linecap="round"/>
<polygon points="243,45 257,45 250,33" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<polygon points="53,45 67,45 60,33" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<circle cx="130" cy="125" r="5" fill="#b91c1c" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="130" cy="45" r="4" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<text x="142" y="143" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">foyer</text>
<text x="130" y="31" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">épicentre</text>
<text x="250" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">station 1</text>
<text x="60" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">station 2</text>
<text x="206" y="127" text-anchor="start" font-size="9" font-weight="400" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">front d'ondes</text>
</svg>
:::

Sur la figure, le foyer est le point en profondeur d'où partent les cercles, l'épicentre est le point de la surface sur la même verticale, et chaque station reçoit les ondes par son propre trajet.

Un sismogramme montre trois types d'ondes, qui n'ont ni la même nature ni la même vitesse :

| Onde | Nom | Mouvement des particules du sol | Vitesse | Milieux traversés |
| ---- | --- | ------------------------------- | ------- | ----------------- |
| P | ondes primaires, de compression | parallèle au sens de propagation | les plus rapides, enregistrées en premier | solides et liquides |
| S | ondes secondaires, de cisaillement | perpendiculaire au sens de propagation | plus lentes que les P | solides seulement |
| L | ondes lentes, ondes de surface | le long de la surface du sol | les plus lentes | surface du sol |

::: figure Tracé schématique construit avec les temps d'arrivée de la station D : de petites oscillations (P), puis des oscillations plus amples (S), enfin les plus grandes (L)
<svg viewBox="0 0 340 182">
<title>Sismogramme schématique : arrivée des ondes P, S puis L à la station D</title>
<line x1="132.7" y1="50" x2="132.7" y2="128" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3" stroke-linecap="round"/>
<text x="132.7" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">P</text>
<text x="132.7" y="43" text-anchor="middle" font-size="9" font-weight="400" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">7 min 05 s</text>
<line x1="211.2" y1="50" x2="211.2" y2="128" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3" stroke-linecap="round"/>
<text x="211.2" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">S</text>
<text x="211.2" y="43" text-anchor="middle" font-size="9" font-weight="400" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">12 min 30 s</text>
<line x1="285.2" y1="50" x2="285.2" y2="128" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3" stroke-linecap="round"/>
<text x="285.2" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">L</text>
<text x="285.2" y="43" text-anchor="middle" font-size="9" font-weight="400" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">17 min 36 s</text>
<polyline points="30,82 31,82 32,82 33,82 34,82 35,82 36,82 37,82 38,82 39,82 40,82 41,82 42,82 43,82 44,82 45,82 46,82 47,82 48,82 49,82 50,82 51,82 52,82 53,82 54,82 55,82 56,82 57,82 58,82 59,82 60,82 61,82 62,82 63,82 64,82 65,82 66,82 67,82 68,82 69,82 70,82 71,82 72,82 73,82 74,82 75,82 76,82 77,82 78,82 79,82 80,82 81,82 82,82 83,82 84,82 85,82 86,82 87,82 88,82 89,82 90,82 91,82 92,82 93,82 94,82 95,82 96,82 97,82 98,82 99,82 100,82 101,82 102,82 103,82 104,82 105,82 106,82 107,82 108,82 109,82 110,82 111,82 112,82 113,82 114,82 115,82 116,82 117,82 118,82 119,82 120,82 121,82 122,82 123,82 124,82 125,82 126,82 127,82 128,82 129,82 130,82 131,82 132,82 133,83.5 134,86.9 135,85.4 136,80.5 137,77.1 138,78.6 139,83.5 140,86.9 141,85.4 142,80.5 143,77.1 144,78.6 145,83.5 146,86.9 147,85.4 148,80.5 149,77.1 150,78.6 151,83.5 152,86.9 153,85.4 154,80.5 155,77.1 156,78.6 157,83.5 158,86.9 159,85.4 160,80.5 161,77.1 162,78.6 163,83.5 164,86.9 165,85.4 166,80.5 167,77.1 168,78.6 169,83.5 170,86.9 171,85.4 172,80.5 173,77.1 174,78.6 175,83.5 176,86.9 177,85.4 178,80.5 179,77.1 180,78.6 181,83.5 182,86.9 183,85.4 184,80.5 185,77.1 186,78.6 187,83.5 188,86.9 189,85.4 190,80.5 191,77.1 192,78.6 193,83.5 194,86.9 195,85.4 196,80.5 197,77.1 198,78.6 199,83.5 200,86.9 201,85.4 202,80.5 203,77.1 204,78.6 205,83.5 206,86.9 207,85.4 208,80.5 209,77.1 210,78.6 211,83.5 212,89.5 213,96.1 214,96.1 215,89.5 216,79.4 217,70.5 218,67 219,70.5 220,79.4 221,89.5 222,96.1 223,96.1 224,89.5 225,79.4 226,70.5 227,67 228,70.5 229,79.4 230,89.5 231,96.1 232,96.1 233,89.5 234,79.4 235,70.5 236,67 237,70.5 238,79.4 239,89.5 240,96.1 241,96.1 242,89.5 243,79.4 244,70.5 245,67 246,70.5 247,79.4 248,89.5 249,96.1 250,96.1 251,89.5 252,79.4 253,70.5 254,67 255,70.5 256,79.4 257,89.5 258,96.1 259,96.1 260,89.5 261,79.4 262,70.5 263,67 264,70.5 265,79.4 266,89.5 267,96.1 268,96.1 269,89.5 270,79.4 271,70.5 272,67 273,70.5 274,79.4 275,89.5 276,96.1 277,96.1 278,89.5 279,79.4 280,70.5 281,67 282,70.5 283,79.4 284,89.5 285,96.1 286,93.9 287,106.6 288,114.3 289,115.7 290,110.4 291,99.4 292,85 293,70.1 294,57.4 295,49.7 296,48.3 297,53.6 298,64.6 299,79 300,93.9 301,106.6 302,114.3 303,115.7 304,110.4 305,99.4 306,85 307,70.1 308,57.4 309,49.7 310,48.3 311,53.6 312,64.6 313,79 314,93.9 315,106.6 316,114.3 317,115.7 318,110.4 319,99.4 320,85" fill="none" stroke="#0f6e56" stroke-width="1.6" stroke-linejoin="round"/>
<text x="30" y="12" text-anchor="start" font-size="9" font-weight="400" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">station D, séisme d'Arette</text>
<line x1="30" y1="140" x2="320" y2="140" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<line x1="30" y1="140" x2="30" y2="145" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="30" y="157" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">0</text>
<line x1="102.5" y1="140" x2="102.5" y2="145" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="102.5" y="157" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">5</text>
<line x1="175" y1="140" x2="175" y2="145" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="175" y="157" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">10</text>
<line x1="247.5" y1="140" x2="247.5" y2="145" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="247.5" y="157" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">15</text>
<line x1="320" y1="140" x2="320" y2="145" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="320" y="157" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">20</text>
<text x="175" y="174" text-anchor="middle" font-size="10" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">temps depuis le séisme (min)</text>
</svg>
:::

Les repères P, S et L de la figure marquent les trois arrivées : plus une onde est rapide, plus tôt elle arrive.

::: exemple Lire un sismogramme
Station D du séisme d'Arette : les ondes arrivent à 7 min 05 s, 12 min 30 s et 17 min 36 s après le séisme.

1. Analyser : le tracé reste plat jusqu'à 7 min 05 s, puis de petites oscillations apparaissent ; des oscillations plus amples commencent à 12 min 30 s, les plus grandes à 17 min 36 s.
2. Interpréter le premier groupe : toutes les ondes partent du foyer au même instant, donc celle qui arrive la première est la plus rapide. C'est l'onde P.
3. Interpréter le deuxième groupe : l'onde S arrive après la P parce qu'elle est plus lente.
4. Interpréter le dernier groupe : les plus grandes oscillations, qui arrivent en dernier, sont les ondes de surface L, les plus lentes.
5. Conclure : trois arrivées correspondent à trois types d'ondes parties ensemble du foyer, séparées par leurs vitesses. À cette station, les S suivent les P de 12 min 30 s − 7 min 05 s = 5 min 25 s.

:::

::: piege
**Erreur : confondre foyer et épicentre.** Dire que le séisme « naît à l'épicentre » tente parce que c'est là qu'on constate les dégâts et qu'on le place sur une carte. Mais il naît au foyer, en profondeur ; l'épicentre n'est que sa projection sur la surface.
:::

::: propriete
**Trois ondes pour un séisme.** Les ondes P (compression) sont les plus rapides et traversent solides et liquides ; les ondes S (cisaillement) sont plus lentes et ne traversent que les solides ; les ondes L, de surface, sont les plus lentes.
Cas limite : un séisme n'a qu'une seule **magnitude** (échelle de Richter), liée à l'énergie libérée, mais plusieurs **intensités** (échelle de Mercalli, à douze degrés), qui mesurent les effets observés et changent d'un lieu à l'autre.
:::

::: verifie À toi : identifier les arrivées
À la station A du même séisme, le tracé montre de petites oscillations dès 2 min 00 s, des oscillations plus amples à 4 min 00 s et de très grandes à 4 min 24 s. Quelle onde correspond à chaque arrivée ?

---

Les petites oscillations à 2 min 00 s arrivent les premières : ce sont les ondes P, les plus rapides. Les oscillations plus amples à 4 min 00 s sont les ondes S, plus lentes que les P. Les plus grandes, à 4 min 24 s, arrivent en dernier : ce sont les ondes de surface L, les plus lentes.
:::

::: retenir
Un séisme naît au foyer et se lit à l'épicentre ; ses ondes arrivent dans l'ordre P, S, L, et seules les ondes P traversent les liquides.
:::

## ⏱️ Calculer la vitesse des ondes : que révèle la distance ?

Le séisme d'Arette (France, 13 août 1967) a été enregistré par des stations réparties sur le globe. Plus une station est loin de l'épicentre, plus les ondes mettent de temps à l'atteindre, mais pas dans la même proportion pour les trois ondes.
Quelle est la vitesse de chaque onde, et reste-t-elle la même quand la distance augmente ?

::: definition
**Vitesse moyenne** — distance parcourue divisée par la durée du trajet.
:::

$$ v = d ÷ t $$

On exprime d en km, t en s, donc v en km/s. Voici quatre des huit stations, avec les durées mesurées depuis l'heure du séisme :

| Station | Distance à l'épicentre | Ondes L | Ondes P | Ondes S |
| ------- | ---------------------- | ------- | ------- | ------- |
| A | 1000 km | 4 min 24 s | 2 min 00 s | 4 min 00 s |
| D | 4000 km | 17 min 36 s | 7 min 05 s | 12 min 30 s |
| F | 6000 km | 26 min 24 s | 9 min 20 s | 16 min 50 s |
| H | 8000 km | 35 min 12 s | 11 min 20 s | 20 min 50 s |

::: figure Temps d'arrivée en fonction de la distance : L est une droite, P et S sont des courbes qui s'aplatissent ; plus une courbe est pentue, plus l'onde est lente
<svg viewBox="0 0 340 240">
<title>Temps d'arrivée des ondes L, S et P en fonction de la distance, séisme d'Arette</title>
<line x1="115" y1="200" x2="115" y2="32" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/>
<line x1="180" y1="200" x2="180" y2="32" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/>
<line x1="245" y1="200" x2="245" y2="32" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/>
<line x1="310" y1="200" x2="310" y2="32" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/>
<line x1="50" y1="153.3" x2="310" y2="153.3" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/>
<line x1="50" y1="106.7" x2="310" y2="106.7" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/>
<line x1="50" y1="60" x2="310" y2="60" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/>
<line x1="180" y1="200" x2="180" y2="32" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3" stroke-linecap="round"/>
<line x1="310" y1="200" x2="310" y2="32" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3" stroke-linecap="round"/>
<line x1="50" y1="200" x2="316" y2="200" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<line x1="50" y1="200" x2="50" y2="28" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<line x1="50" y1="200" x2="50" y2="204" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="50" y="216" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">0</text>
<line x1="115" y1="200" x2="115" y2="204" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="115" y="216" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">2000</text>
<line x1="180" y1="200" x2="180" y2="204" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="180" y="216" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">4000</text>
<line x1="245" y1="200" x2="245" y2="204" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="245" y="216" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">6000</text>
<line x1="310" y1="200" x2="310" y2="204" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="310" y="216" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">8000</text>
<line x1="46" y1="200" x2="50" y2="200" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="43" y="203" text-anchor="end" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">0</text>
<line x1="46" y1="153.3" x2="50" y2="153.3" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="43" y="156.3" text-anchor="end" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">10</text>
<line x1="46" y1="106.7" x2="50" y2="106.7" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="43" y="109.7" text-anchor="end" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">20</text>
<line x1="46" y1="60" x2="50" y2="60" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="43" y="63" text-anchor="end" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">30</text>
<text x="170" y="232" text-anchor="middle" font-size="10" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">distance à l'épicentre (km)</text>
<text x="50" y="18" text-anchor="start" font-size="10" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">temps d'arrivée (min)</text>
<polyline points="50,200 82.5,179.5 180,117.9 245,76.8 310,35.7" fill="none" stroke="#b91c1c" stroke-width="2" stroke-linejoin="round"/>
<circle cx="82.5" cy="179.5" r="3" fill="#b91c1c" stroke="#ffffff" stroke-width="1"/>
<circle cx="180" cy="117.9" r="3" fill="#b91c1c" stroke="#ffffff" stroke-width="1"/>
<circle cx="245" cy="76.8" r="3" fill="#b91c1c" stroke="#ffffff" stroke-width="1"/>
<circle cx="310" cy="35.7" r="3" fill="#b91c1c" stroke="#ffffff" stroke-width="1"/>
<text x="319" y="39.7" text-anchor="middle" font-size="12" font-weight="700" fill="#b91c1c" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">L</text>
<polyline points="50,200 82.5,190.7 180,166.9 245,156.4 310,147.1" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/>
<circle cx="82.5" cy="190.7" r="3" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="180" cy="166.9" r="3" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="245" cy="156.4" r="3" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="310" cy="147.1" r="3" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<text x="319" y="151.1" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">P</text>
<polyline points="50,200 82.5,181.3 180,141.7 245,121.4 310,102.8" fill="none" stroke="#1d4ed8" stroke-width="2" stroke-linejoin="round"/>
<circle cx="82.5" cy="181.3" r="3" fill="#1d4ed8" stroke="#ffffff" stroke-width="1"/>
<circle cx="180" cy="141.7" r="3" fill="#1d4ed8" stroke="#ffffff" stroke-width="1"/>
<circle cx="245" cy="121.4" r="3" fill="#1d4ed8" stroke="#ffffff" stroke-width="1"/>
<circle cx="310" cy="102.8" r="3" fill="#1d4ed8" stroke="#ffffff" stroke-width="1"/>
<text x="319" y="106.8" text-anchor="middle" font-size="12" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">S</text>
</svg>
:::

Sur la figure, chaque point reprend une ligne du tableau ; la pente d'une courbe mesure des minutes par kilomètre, c'est-à-dire l'inverse d'une vitesse. Les traits en pointillés repèrent 4000 km et 8000 km, les deux distances de l'exemple.

::: exemple Calculer les vitesses à 4000 km et à 8000 km
1. Convertir les durées en secondes, car la vitesse s'exprime en km/s. À la station D : P 7 min 05 s = 425 s, S 12 min 30 s = 750 s, L 17 min 36 s = 1056 s.
2. Diviser la distance par la durée, car v = d ÷ t. À 4000 km : P 4000 ÷ 425 ≈ 9,4 km/s, S 4000 ÷ 750 ≈ 5,3 km/s, L 4000 ÷ 1056 ≈ 3,8 km/s.
3. Refaire le même calcul à la station H, à 8000 km : P 11 min 20 s = 680 s donne 8000 ÷ 680 ≈ 11,8 km/s ; S 20 min 50 s = 1250 s donne 6,4 km/s ; L 35 min 12 s = 2112 s donne 3,8 km/s.
4. Comparer : la vitesse de L reste la même (3,8 km/s, d'où la droite), celle de P passe de 9,4 à 11,8 km/s, celle de S de 5,3 à 6,4 km/s.
5. Interpréter : une vitesse moyenne qui change avec la distance montre que les ondes ne traversent pas un milieu uniforme. Les P et S qui vont loin plongent dans des couches où elles vont plus vite ; les L, qui suivent la surface, gardent leur vitesse.

:::

::: piege
**Erreur : diviser la durée par la distance.** Le calcul 425 ÷ 4000 ≈ 0,11 tente parce qu'on lit d'abord la durée. Mais ce résultat est en s/km, l'inverse d'une vitesse : une onde rapide y donne un petit nombre. La bonne opération est distance ÷ durée.
:::

::: methode
**Calculer une vitesse moyenne.** (1) Convertir la durée en secondes. (2) Diviser la distance en km par cette durée. (3) Comparer les vitesses obtenues à plusieurs distances.
Cas limite : la vitesse obtenue est une moyenne sur tout le trajet. Si elle change avec la distance, c'est le milieu qui n'est pas uniforme.
:::

::: verifie À toi : une vitesse de S
À la station B, à 2000 km, les ondes S arrivent après 7 min 20 s. Calculer leur vitesse moyenne.

---

On convertit : 7 min 20 s = 440 s. On divise la distance par la durée : 2000 ÷ 440 ≈ 4,5 km/s. Cette valeur se place entre 4,2 km/s à 1000 km et 5,3 km/s à 4000 km, ce qui confirme que la vitesse moyenne des S augmente avec la distance.
:::

::: retenir
La vitesse moyenne d'une onde est d ÷ t en km/s ; celle des L reste constante, celle des P et des S augmente avec la distance : le milieu traversé n'est pas uniforme.
:::

## 🔀 Ce qui fait varier la vitesse : les discontinuités et le Moho

Le 8 octobre 1909, à Zagreb, le géophysicien André Mohorovicic examine un sismogramme : les ondes P et S arrivent, puis de nouveau des P et des S. Les deux groupes sont pourtant partis du même foyer au même instant.
Pourquoi un même séisme donne-t-il deux groupes d'ondes décalés ?

::: definition
**Réflexion** — l'onde rebondit sur une surface et repart dans le premier milieu.
**Réfraction** — l'onde franchit la surface et change de direction et de vitesse dans le second milieu.
**Discontinuité** — surface qui sépare deux milieux de nature différente et où la vitesse des ondes varie brusquement.
**Discontinuité de Mohorovicic (Moho)** — discontinuité qui sépare la croûte du manteau.
:::

La vitesse d'une onde dépend du milieu qu'elle traverse. Les mesures dans des roches donnent, pour les ondes S :

| Milieu | Vitesse des ondes S |
| ------ | ------------------- |
| argile | 2,2 km/s |
| granite | 2,4 à 3,2 km/s |
| basalte | 3,5 à 4 km/s |
| péridotite | 4,5 à 7,8 km/s |
| liquide | les ondes S ne s'y propagent pas |

La vitesse dépend de l'état et de la rigidité du milieu ; dans les roches du globe, elle augmente en général avec la profondeur, quand les roches deviennent plus denses et plus rigides. Pour les S, elle est nulle dans un liquide.

::: figure Parti du même foyer, le trajet réfléchi sur la discontinuité est plus long que le trajet direct : il arrive après
<svg viewBox="0 0 340 190">
<title>Deux trajets partis du même foyer : l'un direct, l'autre réfléchi sur une discontinuité</title>
<rect x="10" y="40" width="320" height="90" rx="0" fill="#e2e8f0"/>
<rect x="10" y="130" width="320" height="50" rx="0" fill="#cbd5e1"/>
<line x1="10" y1="40" x2="330" y2="40" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>
<line x1="10" y1="130" x2="330" y2="130" stroke="#0f6e56" stroke-width="2.5" stroke-dasharray="7 4" stroke-linecap="round"/>
<line x1="50" y1="85" x2="290" y2="40" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<polyline points="50,85 130,130 290,40" fill="none" stroke="#c2410c" stroke-width="2" stroke-linejoin="round"/>
<polygon points="283,40 297,40 290,28" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<circle cx="50" cy="85" r="5" fill="#b91c1c" stroke="#0f172a" stroke-width="1.5"/>
<text x="50" y="73" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">foyer</text>
<text x="290" y="20" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">station</text>
<text x="170" y="52" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">trajet direct</text>
<text x="240" y="102" text-anchor="start" font-size="10" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">trajet réfléchi</text>
<text x="15" y="112" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">croûte</text>
<text x="325" y="166" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">manteau</text>
<text x="325" y="124" text-anchor="end" font-size="10" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">discontinuité</text>
</svg>
:::

Sur la figure, le trajet qui rebondit sur la discontinuité est plus long que le trajet direct : à vitesse égale dans la croûte, il arrive plus tard.

::: exemple Expliquer le dédoublement des ondes
1. Constater : un même séisme donne deux groupes P et S, séparés par un décalage.
2. Raisonner sur le départ : les deux groupes partent ensemble du foyer, donc le décalage à l'arrivée vient d'un trajet différent.
3. Raisonner sur le chemin : si le sous-sol était uniforme, les ondes iraient en ligne droite et un seul groupe arriverait. Un second groupe existe, donc une partie des ondes a rencontré une surface sur laquelle elle s'est réfléchie ou réfractée.
4. Conclure : il existe en profondeur une surface séparant deux milieux de propriétés différentes, une discontinuité. Placée entre croûte et manteau, c'est le Moho. Sa profondeur varie d'un endroit à l'autre.

:::

::: piege
**Erreur : prendre une discontinuité pour une couche.** Le Moho semble « un niveau » du globe, comme la croûte ou le manteau, d'où la confusion. Mais une discontinuité est une surface sans épaisseur : elle sépare deux couches, et la vitesse des ondes y change brusquement.
:::

::: propriete
**Vitesse et discontinuité.** La vitesse des ondes P et S dépend du milieu (état solide ou liquide, densité, rigidité). Une variation brusque de vitesse à une profondeur précise signale une discontinuité entre deux milieux de nature différente.
Cas limite : dans un liquide, les ondes S ne se propagent plus du tout ; leur disparition est elle-même un signal.
:::

::: verifie À toi : brusque ou progressive ?
Pourquoi une variation brusque de la vitesse des ondes, et non une variation lente, signale-t-elle une discontinuité ?

---

Une variation lente traduit un milieu dont les propriétés évoluent peu à peu. Un changement brusque à une profondeur précise signifie qu'on passe d'un coup d'un milieu à un autre, de nature différente : il y a donc une surface de séparation, c'est-à-dire une discontinuité.
:::

::: retenir
La vitesse des ondes dépend du milieu ; une variation brusque révèle une discontinuité, surface qui sépare deux milieux, comme le Moho entre croûte et manteau.
:::

## 💧 Gutenberg et Lehmann : un noyau liquide autour d'une graine solide

Sous le Moho, les ondes P et S accélèrent dans l'ensemble (malgré un léger creux dans la zone à faible vitesse). Puis, vers 2900 km de profondeur, les ondes S disparaissent des enregistrements.
Que se passe-t-il à cette profondeur, et pourquoi une autre variation se produit-elle encore vers 5100 km ?

::: definition
**Discontinuité de Gutenberg** (1913) — discontinuité située à 2900 km de profondeur.
**Discontinuité de Lehmann** (1936) — discontinuité située vers 5100 km de profondeur.
**Noyau externe** — enveloppe liquide comprise entre ces deux discontinuités.
**Graine** (ou noyau interne) — noyau solide, de la discontinuité de Lehmann jusqu'au centre du globe.
:::

::: figure Courbes schématiques : à 2900 km, la vitesse des P chute et les S disparaissent ; vers 5100 km, la vitesse des P augmente brusquement et des S réapparaissent
<svg viewBox="0 0 340 232">
<title>Courbes schématiques des vitesses des ondes P et S selon la profondeur</title>
<rect x="50" y="40" width="122.3" height="150" rx="0" fill="#e2e8f0"/>
<rect x="172.3" y="40" width="92.8" height="150" rx="0" fill="#bae6fd"/>
<rect x="265.2" y="40" width="54.8" height="150" rx="0" fill="#fde68a"/>
<line x1="172.3" y1="40" x2="172.3" y2="190" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3" stroke-linecap="round"/>
<line x1="265.2" y1="40" x2="265.2" y2="190" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3" stroke-linecap="round"/>
<line x1="50" y1="190" x2="324" y2="190" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<line x1="50" y1="190" x2="50" y2="36" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<line x1="50" y1="190" x2="50" y2="194" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="50" y="206" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">0</text>
<line x1="92.2" y1="190" x2="92.2" y2="194" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="92.2" y="206" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1000</text>
<line x1="134.4" y1="190" x2="134.4" y2="194" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="134.4" y="206" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">2000</text>
<line x1="176.6" y1="190" x2="176.6" y2="194" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="176.6" y="206" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">3000</text>
<line x1="218.8" y1="190" x2="218.8" y2="194" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="218.8" y="206" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">4000</text>
<line x1="260.9" y1="190" x2="260.9" y2="194" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="260.9" y="206" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">5000</text>
<line x1="303.1" y1="190" x2="303.1" y2="194" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="303.1" y="206" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">6000</text>
<text x="185" y="222" text-anchor="middle" font-size="10" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">profondeur (km)</text>
<text x="14" y="115" text-anchor="middle" font-size="10" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" transform="rotate(-90 14 115)">vitesse des ondes (km/s)</text>
<polyline points="50,120 80,103 120,90 172.3,75 172.3,120 200,116 240,110 265.2,104 265.2,96 320,94" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round"/>
<polyline points="50,150 80,138 120,126 172.3,115 172.3,186 265.2,186 265.2,160 320,158" fill="none" stroke="#1d4ed8" stroke-width="2.5" stroke-linejoin="round"/>
<text x="112" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">P</text>
<text x="112" y="122" text-anchor="middle" font-size="12" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">S</text>
<text x="218.8" y="176" text-anchor="middle" font-size="9" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">S absentes</text>
<text x="111.2" y="53" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">manteau</text>
<text x="218.8" y="53" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">noyau externe</text>
<text x="292.6" y="53" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">graine</text>
<text x="169.3" y="34" text-anchor="end" font-size="9" font-weight="400" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Gutenberg 2900 km</text>
<text x="262.2" y="34" text-anchor="end" font-size="9" font-weight="400" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Lehmann 5100 km</text>
</svg>
:::

Les deux traits verticaux de la figure marquent les profondeurs où les courbes changent brusquement ; ce sont les deux discontinuités qui encadrent le noyau externe.

::: exemple Lire les courbes P et S
1. Analyser à 2900 km : la vitesse des P chute brutalement et les S disparaissent.
2. Interpréter : les S ne traversent pas les liquides alors que les P les traversent, plus lentement. Le milieu devient donc liquide à 2900 km : c'est le noyau externe.
3. Analyser vers 5100 km : la vitesse des P augmente brusquement et des S réapparaissent.
4. Interpréter : les S se propagent de nouveau, donc le milieu redevient solide. C'est la graine, et la discontinuité de Lehmann est la limite noyau externe/graine.
5. Conclure : sous un manteau solide, qui laisse passer les S, se trouve un noyau externe liquide autour d'une graine solide. Ce n'est pas la profondeur qui arrête les S : elles traversent le manteau jusqu'à 2900 km et reviennent plus bas.

:::

Reste une question : la température augmente avec la profondeur, et la graine est plus chaude que le noyau externe, pourtant elle est solide. Les mesures de température et de pression dans le globe, et des expériences sur du fer pur, donnent :

| Profondeur (km) | Température (K) | Pression (millions de bars) | État du fer |
| --------------- | --------------- | --------------------------- | ----------- |
| 2900 | 4500 | 1,3 | liquide |
| 5200 | 5000 | 3,2 | solide |
| 6000 | 5500 | 4 | solide |

Le kelvin (K) est l'unité de température des mesures de ce tableau.

::: exemple Pourquoi seul le noyau externe est-il liquide ?
1. Analyser : de 2900 à 5200 km, la température monte de 4500 à 5000 K et la pression de 1,3 à 3,2 millions de bars ; le fer passe de liquide à solide.
2. Interpréter : une température élevée favorise la fusion, une forte pression favorise l'état solide. Ici la température augmente, et pourtant le fer se solidifie : c'est l'effet de la pression, bien plus forte, qui l'emporte.
3. Conclure : le noyau externe est la seule enveloppe liquide, car sa température permet au fer de fondre sans que la pression soit encore assez forte pour le maintenir solide. Dans la graine, la pression l'emporte.

:::

::: piege
**Erreur : croire que l'état d'une roche ne dépend que de la température.** « Le noyau externe est liquide parce que c'est le plus chaud » tente parce qu'on associe chaleur et fusion. Mais la graine est plus chaude que le noyau externe et reste solide : la pression, très forte, maintient le fer à l'état solide.
:::

::: propriete
**État physique et profondeur.** L'état solide ou liquide d'un matériau dépend à la fois de la température et de la pression : la chaleur favorise le liquide, la pression favorise le solide. Les S disparaissent là où le milieu est liquide et réapparaissent là où il redevient solide.
Cas limite : dans le manteau, très chaud mais sous forte pression, les roches restent solides et laissent passer les S.
:::

::: verifie À toi : le sens des changements
Vers 5100 km, la vitesse des P augmente brusquement et des S réapparaissent. Que dire de l'état du milieu sous cette profondeur, et pourquoi ?

---

Des S réapparaissent : or les S ne traversent que les solides, donc le milieu est solide sous 5100 km. Le saut de vitesse des P montre qu'on a franchi une discontinuité, celle de Lehmann, vers un milieu différent du noyau externe : la graine.
:::

::: retenir
À 2900 km, les S disparaissent car le milieu devient liquide (noyau externe) ; vers 5100 km, ils réapparaissent car la graine est solide, la pression l'emportant sur la température.
:::

## 🧅 Le modèle en couches : croûte, manteau, noyau

On peut maintenant empiler les résultats : les discontinuités découpent le globe en enveloppes concentriques, comme les écailles d'un oignon. Mais il existe un second découpage, selon la rigidité, qui ne coïncide pas avec le premier.
Quelles sont les enveloppes, et en quoi la lithosphère n'est-elle pas la croûte ?

::: definition
**Croûte** — enveloppe externe, au-dessus du Moho ; elle est continentale ou océanique.
**Manteau** — enveloppe comprise entre le Moho et la discontinuité de Gutenberg ; il est supérieur ou inférieur, la limite étant à 670 km de profondeur.
**Noyau** — enveloppe centrale, à partir de 2900 km ; il comprend le noyau externe liquide et la graine solide.
**Zone à faible vitesse (ZFV ou LVZ)** — zone du manteau supérieur où la vitesse des ondes diminue un peu.
**Lithosphère** — couche rigide formée de la croûte et de la partie du manteau supérieur située au-dessus de la ZFV.
**Asthénosphère** — couche plus plastique du manteau, sous la lithosphère.
:::

::: figure Les discontinuités découpent le globe en enveloppes concentriques ; les rayons sont à l'échelle, sauf la croûte dont l'épaisseur est exagérée
<svg viewBox="0 0 340 236">
<title>Les enveloppes du globe terrestre, de la croûte à la graine</title>
<circle cx="88" cy="122" r="84" fill="#fecaca"/>
<circle cx="88" cy="122" r="75.2" fill="#fdba74"/>
<circle cx="88" cy="122" r="45.8" fill="#7dd3fc"/>
<circle cx="88" cy="122" r="16.7" fill="#fde047"/>
<circle cx="88" cy="122" r="84" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="88" cy="122" r="75.2" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="88" cy="122" r="45.8" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="88" cy="122" r="16.7" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="88" cy="122" r="86" fill="none" stroke="#0f6e56" stroke-width="3.5"/>
<line x1="128.4" y1="46.1" x2="192" y2="31" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/>
<circle cx="128.4" cy="46.1" r="2.2" fill="#0f172a"/>
<text x="196" y="33" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">croûte</text>
<text x="196" y="45" text-anchor="start" font-size="8.5" font-weight="400" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">(épaisseur exagérée)</text>
<line x1="152.4" y1="75.2" x2="192" y2="69" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/>
<circle cx="152.4" cy="75.2" r="2.2" fill="#0f172a"/>
<text x="196" y="71" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">manteau supérieur</text>
<text x="196" y="83" text-anchor="start" font-size="8.5" font-weight="400" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">jusqu'à 670 km de profondeur</text>
<line x1="147.1" y1="109.4" x2="192" y2="107" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/>
<circle cx="147.1" cy="109.4" r="2.2" fill="#0f172a"/>
<text x="196" y="109" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">manteau inférieur</text>
<text x="196" y="121" text-anchor="start" font-size="8.5" font-weight="400" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">de 670 à 2900 km</text>
<line x1="118.6" y1="128.5" x2="192" y2="145" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/>
<circle cx="118.6" cy="128.5" r="2.2" fill="#0f172a"/>
<text x="196" y="147" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">noyau externe</text>
<text x="196" y="159" text-anchor="start" font-size="8.5" font-weight="400" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">de 2900 à 5100 km</text>
<line x1="88" y1="122" x2="192" y2="183" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/>
<circle cx="88" cy="122" r="2.2" fill="#0f172a"/>
<text x="196" y="185" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">graine</text>
<text x="196" y="197" text-anchor="start" font-size="8.5" font-weight="400" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">de 5100 km au centre</text>
</svg>
:::

Sur la figure, chaque cercle correspond à une profondeur de discontinuité : 670 km, 2900 km et 5100 km ; les noms à droite sont ceux de la définition.

::: figure Sous la chaîne de montagnes, la croûte continentale s'enfonce en racine : 70 km contre 30 km sous la plaine ; la croûte océanique est bien plus mince (valeurs du manuel, d = densité)
<svg viewBox="0 0 340 186">
<title>Coupe de la croûte océanique et de la croûte continentale, avec leurs épaisseurs et densités</title>
<polygon points="10,50 115,50 105,62 10,62" fill="#bae6fd" stroke="None" stroke-width="2" stroke-linejoin="round"/>
<polygon points="10,69.7 112,69.7 125,83 195,83 230,127 265,83 330,83 330,178 10,178" fill="#fdba74" stroke="None" stroke-width="2" stroke-linejoin="round"/>
<polygon points="10,62 105,62 112,69.7 10,69.7" fill="#86efac" stroke="#0f172a" stroke-width="1" stroke-linejoin="round"/>
<polygon points="105,62 115,50 190,50 230,32 270,50 330,50 330,83 265,83 230,127 195,83 125,83 112,69.7" fill="#fde68a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round"/>
<polyline points="10,69.7 112,69.7 125,83 195,83 230,127 265,83 330,83" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="7 4"/>
<text x="10" y="13" text-anchor="start" font-size="9.5" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">croûte océanique : 7 km, d = 2,9</text>
<line x1="60" y1="17" x2="60" y2="66" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/>
<text x="172" y="13" text-anchor="start" font-size="9.5" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">croûte continentale : d = 2,7</text>
<line x1="175" y1="17" x2="160" y2="66" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/>
<text x="60" y="58" text-anchor="middle" font-size="9" font-weight="400" fill="#075985" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">océan</text>
<text x="150" y="76" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">30 km</text>
<text x="244" y="121" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">70 km</text>
<text x="230" y="26" text-anchor="middle" font-size="9" font-weight="400" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">chaîne de montagnes</text>
<text x="20" y="150" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">manteau supérieur : d = 3,4</text>
<text x="330" y="98" text-anchor="end" font-size="10" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Moho</text>
</svg>
:::

La ligne verte en pointillés de la figure est le Moho : sa profondeur change, de 7 km sous l'océan à 70 km sous la chaîne de montagnes. Selon les sources, la croûte océanique mesure de 5 à 10 km ; la figure retient 7 km.

| Grandeur | Croûte | Manteau | Noyau |
| -------- | ------ | ------- | ----- |
| Température (ordre de grandeur) | 0 à 900 °C | 900 à 4000 °C | 4000 à 5000 °C |
| Densité | 2,7 à 3 | 3,3 à 5,5 | 10 à 12 |
| État | solide | solide | externe liquide, graine solide |

La pression augmente elle aussi avec la profondeur : 1,3 million de bars à 2900 km, 4 millions à 6000 km. Près de la surface, la température monte d'environ 1 °C tous les 30 m.

::: exemple Lire la coupe de la croûte
1. Comparer les épaisseurs : 30 à 70 km pour la croûte continentale, 7 km pour la croûte océanique. La continentale est plus épaisse, surtout sous les montagnes.
2. Comparer les densités : 2,9 pour l'océanique et 2,7 pour la continentale. L'océanique est plus dense. Toutes deux sont moins denses que le manteau supérieur (3,4).
3. Interpréter le Moho : le passage de la croûte au manteau est un passage à un matériau différent, plus dense et plus rigide, où les ondes accélèrent.
4. Situer la lithosphère : elle englobe la croûte et le haut du manteau, donc elle est plus épaisse que la croûte seule.

:::

::: piege
**Erreur : confondre lithosphère et croûte.** Les deux désignent « la partie rigide du dessus », d'où la confusion. Mais la croûte est une enveloppe de composition différente, limitée par le Moho, tandis que la lithosphère comprend la croûte et aussi le haut du manteau.
:::

::: propriete
**Deux découpages.** Par les discontinuités : croûte (continentale, épaisse et peu dense ; océanique, mince et plus dense), manteau, noyau. Par la rigidité : lithosphère rigide sur asthénosphère plus plastique.
Cas limite : la lithosphère n'a pas la même épaisseur partout ; elle est plus mince sous un océan que sous un continent.
:::

::: verifie À toi : lithosphère et Moho
Le Moho est-il la base de la lithosphère ? Y a-t-il du manteau dans la lithosphère ?

---

Non : le Moho sépare la croûte du manteau, alors que la lithosphère comprend la croûte et aussi le haut du manteau. Sa base est la zone à faible vitesse, plus profonde que le Moho. Il y a donc du manteau dans la lithosphère.
:::

::: retenir
Le globe se découpe en croûte, manteau et noyau par les discontinuités, et en lithosphère rigide sur asthénosphère plastique par la rigidité ; la lithosphère contient la croûte et le haut du manteau.
:::

## 🌋 Les volcans : des messagers venus de la profondeur

En 1930, le Stromboli (Italie) a projeté en quelques heures un nuage de cendres, une colonne de gaz de plus de 2,5 km, des blocs de 30 tonnes, des scories incandescentes, puis des coulées de lave qui ont atteint la mer.
D'où vient tout cela, et que révèle-t-il de l'intérieur du globe ?

::: definition
**Volcan** — relief dont le cratère, relié par une cheminée à la profondeur, rejette des matériaux.
**Éruption volcanique** — manifestation au cours de laquelle des matériaux venus des profondeurs sont projetés à la surface.
**Lave** — matériau en fusion qui sort du volcan.
**Scories** — roches légères rejetées par un volcan ; les **bombes** sont des lambeaux de lave projetés qui se solidifient en l'air, les **cendres** du magma pulvérisé ou des matériaux broyés.
:::

::: figure Un volcan rejette des gaz, des produits solides (cendres, bombes) et des produits liquides (coulée de lave) par une cheminée venue de la profondeur ; le panache contient des gaz et des cendres, qui sont solides
<svg viewBox="0 0 340 205">
<title>Coupe d'un volcan : cheminée, cratère, panache de cendres et de gaz, bombes, coulée de lave</title>
<rect x="10" y="150" width="320" height="50" rx="0" fill="#d6c7b0"/>
<polygon points="60,150 150,72 190,72 280,150" fill="#a8a29e" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<rect x="163" y="80" width="14" height="120" rx="0" fill="#f97316" stroke="#0f172a" stroke-width="1.2"/>
<polygon points="150,72 160,80 180,80 190,72" fill="#7c2d12" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/>
<line x1="194" y1="74" x2="272" y2="146" stroke="#dc2626" stroke-width="6" stroke-linecap="round"/>
<ellipse cx="170" cy="50" rx="26" ry="14" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
<ellipse cx="150" cy="38" rx="18" ry="11" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
<ellipse cx="192" cy="36" rx="20" ry="12" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
<ellipse cx="172" cy="26" rx="16" ry="9" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
<circle cx="118" cy="48" r="4.5" fill="#44403c" stroke="#0f172a" stroke-width="1"/>
<circle cx="232" cy="40" r="4.5" fill="#44403c" stroke="#0f172a" stroke-width="1"/>
<circle cx="222" cy="66" r="4.5" fill="#44403c" stroke="#0f172a" stroke-width="1"/>
<text x="170" y="12" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">cendres et gaz</text>
<text x="236" y="32" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">bombes</text>
<text x="100" y="84" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">cratère</text>
<line x1="102" y1="81" x2="152" y2="76" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/>
<text x="210" y="184" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">cheminée</text>
<line x1="208" y1="181" x2="178" y2="172" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/>
<text x="252" y="170" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">coulée de lave</text>
<line x1="262" y1="164" x2="266" y2="146" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/>
<text x="36" y="176" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">socle</text>
</svg>
:::

Sur la figure, la cheminée relie le cratère à la profondeur : tout ce que le volcan rejette passe par elle.

| Produits | Nature |
| -------- | ------ |
| gaz | vapeur d'eau, dioxyde de carbone, sulfure d'hydrogène, oxyde de carbone |
| laves basaltiques | très fluides, pauvres en silice, sorties vers 1200 °C |
| laves rhyolitiques | très visqueuses, riches en silice, sorties vers 800 °C |
| solides | bombes, scories, cendres |

::: exemple Ce que dit l'éruption du Stromboli
1. Relever les produits cités : nuage de cendres, gaz, blocs de 30 tonnes (produits solides), scories incandescentes, coulées de lave.
2. Classer : les gaz, les solides (cendres, blocs, scories) et le liquide (la lave) sont les trois états des produits d'une éruption.
3. Chercher l'origine : tous sortent par le cratère et la cheminée, donc ce sont des matériaux venus de la profondeur.
4. Interpréter la température : les basaltes sortent vers 1200 °C, une température que la surface ne connaît pas ; elle vient de la profondeur, où il fait de plus en plus chaud.
5. Conclure : les rejets volcaniques sont des échantillons de la profondeur, que l'on peut analyser sans y descendre.

:::

::: piege
**Erreur : confondre les deux laves.** On imagine la lave basaltique épaisse parce que le basalte est une roche sombre et dense. En fait la lave basaltique est la plus fluide, la plus chaude (1200 °C) et la plus pauvre en silice ; la lave rhyolitique est visqueuse, riche en silice et moins chaude (800 °C).
:::

::: propriete
**Les volcans, messagers de la profondeur.** Gaz, laves et solides viennent de la profondeur : les laves sont de deux types, basaltique (fluide, pauvre en silice) ou rhyolitique (visqueuse, riche en silice).
Cas limite : les rejets volcaniques ne renseignent que sur les 200 premiers kilomètres environ ; pour le noyau, il faut d'autres méthodes.
:::

::: verifie À toi : une température qui parle
Les basaltes sortent à 1200 °C. Que peut-on en dire de leur lieu d'origine ?

---

Une telle température n'existe pas à la surface. Comme la température augmente avec la profondeur, le matériau vient d'un lieu profond, aussi chaud ou plus chaud que 1200 °C : le volcan ramène donc de la matière chauffée en profondeur.
:::

::: retenir
Un volcan rejette gaz, laves et solides venus de la profondeur ; la lave basaltique est fluide, chaude et pauvre en silice, la rhyolitique visqueuse, plus froide et riche en silice.
:::

## 🪨 Les roches et la composition du globe : granite, basalte, péridotite, fer

Sur les continents on ramasse du granite, au fond des océans on prélève du basalte, et un volcan peut ramener dans une coulée de basalte des enclaves vertes venues de la profondeur.
Peut-on relier ces roches aux couches du globe, et de quoi est fait le noyau, qu'aucune roche n'atteint ?

::: definition
**Granite** — roche claire à gros grains, qui contient du quartz, de l'orthose, du plagioclase et du mica.
**Basalte** — roche sombre, qui contient de l'olivine, du pyroxène et du plagioclase.
**Péridotite** — roche verte riche en olivine, qui contient aussi du pyroxène et du spinelle ; ses minéraux sont dits ferromagnésiens, car ils contiennent du fer et du magnésium.
:::

| Roche | Couche | Aspect | Minéraux |
| ----- | ------ | ------ | -------- |
| granite | croûte continentale | claire, grenue | quartz, orthose, plagioclase, mica |
| basalte | croûte océanique | sombre | olivine, pyroxène, plagioclase |
| péridotite | manteau | verte (olivine) | olivine, pyroxène, spinelle |

Le tableau relie chaque roche à la couche où on la trouve et aux minéraux que l'on y reconnaît au microscope.

::: exemple Relier les roches aux couches
1. Granite : on l'observe sur les continents ; la croûte continentale est faite de granite.
2. Basalte : on le prélève au fond des océans ; la croûte océanique est faite de basalte.
3. Péridotite : les volcans en rapportent des enclaves vertes riches en olivine ; le manteau est fait de péridotite.
4. Comparer les minéraux : l'olivine et le pyroxène se trouvent à la fois dans le basalte et dans la péridotite, alors que le quartz est propre au granite et le spinelle à la péridotite. Les compositions de la croûte et du manteau sont donc différentes.
5. Conclure : croûte continentale, granite ; croûte océanique, basalte ; manteau, péridotite.

:::

::: figure La densité du noyau est voisine de 10 : seuls le cuivre et le fer ont une densité qui l'inclut
<svg viewBox="0 0 340 196">
<title>Densités de quatre éléments chimiques (g/cm³) et densité du noyau</title>
<text x="52" y="47" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Na</text>
<rect x="87.9" y="34" width="17.9" height="18" rx="0" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/>
<text x="52" y="81" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Al</text>
<rect x="123.6" y="68" width="26.8" height="18" rx="0" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/>
<text x="52" y="115" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Cu</text>
<rect x="221.8" y="102" width="71.4" height="18" rx="0" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/>
<text x="52" y="149" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Fe</text>
<rect x="239.6" y="136" width="30.4" height="18" rx="0" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/>
<line x1="248.6" y1="22" x2="248.6" y2="152" stroke="#b91c1c" stroke-width="2" stroke-dasharray="5 3" stroke-linecap="round"/>
<text x="248.6" y="14" text-anchor="middle" font-size="10" font-weight="700" fill="#b91c1c" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">noyau : d = 10</text>
<line x1="70" y1="158" x2="324" y2="158" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<line x1="70" y1="158" x2="70" y2="162" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="70" y="174" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">0</text>
<line x1="105.7" y1="158" x2="105.7" y2="162" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="105.7" y="174" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">2</text>
<line x1="141.4" y1="158" x2="141.4" y2="162" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="141.4" y="174" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">4</text>
<line x1="177.1" y1="158" x2="177.1" y2="162" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="177.1" y="174" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">6</text>
<line x1="212.9" y1="158" x2="212.9" y2="162" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="212.9" y="174" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">8</text>
<line x1="248.6" y1="158" x2="248.6" y2="162" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="248.6" y="174" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">10</text>
<line x1="284.3" y1="158" x2="284.3" y2="162" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="284.3" y="174" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">12</text>
<line x1="320" y1="158" x2="320" y2="162" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="320" y="174" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">14</text>
<text x="195" y="189" text-anchor="middle" font-size="10" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">densité (g/cm³)</text>
</svg>
:::

Les barres de la figure donnent, pour chaque élément, l'intervalle de densité mesuré en laboratoire ; le trait rouge est la densité du noyau.

::: exemple De quoi est fait le noyau ?
1. Comparer les densités : le noyau a une densité voisine de 10. Le sodium (1 à 2) et l'aluminium (3 à 4,5) sont trop légers ; le cuivre (8,5 à 12,5) et le fer (9,5 à 11,2) sont compatibles.
2. Constater les limites : la densité seule ne départage pas le cuivre et le fer, il faut un second critère.
3. Utiliser la vitesse des ondes : Birch mesure en laboratoire la vitesse d'ondes de choc dans des matériaux sous différentes températures et pressions, et la compare à celle des ondes sismiques dans le noyau. Les vitesses du noyau sont voisines de celles du fer.
4. Conclure : le noyau est riche en fer, avec du nickel ; le noyau externe contient aussi du soufre, la graine est faite de fer et de nickel.

:::

::: piege
**Erreur : croire que le manteau est fait de basalte.** Le basalte sort des volcans, d'où l'idée qu'il forme le manteau. Mais le manteau est de la péridotite ; le basalte est la roche de la croûte océanique, qui provient de la fusion de la péridotite.
:::

::: propriete
**Composition par couche.** Croûte continentale : granite. Croûte océanique : basalte. Manteau : péridotite. Noyau : fer et nickel, avec du soufre dans le noyau externe.
Cas limite : seule la partie supérieure de la croûte est observable directement ; le manteau est connu par les rejets volcaniques, le noyau par des méthodes indirectes (densité et vitesse des ondes).
:::

::: verifie À toi : une roche, une couche
Une roche claire à gros grains contient du quartz, de l'orthose et du mica. De quelle roche et de quelle couche vient-elle ? Pourquoi n'est-elle pas du manteau ?

---

Quartz, orthose, plagioclase et mica sont les minéraux du granite, roche de la croûte continentale. Le manteau est fait de péridotite, qui contient de l'olivine, du pyroxène et du spinelle, et pas de quartz : cette roche ne peut donc pas en venir.
:::

::: retenir
Granite pour la croûte continentale, basalte pour la croûte océanique, péridotite pour le manteau ; le noyau est riche en fer et nickel, d'après sa densité et la vitesse des ondes.
:::

## ☢️ L'énergie interne : d'où vient la chaleur, et pourquoi la péridotite fond-elle ?

La lave sort à 1200 °C et le noyau atteint 4000 à 5000 °C. Longtemps on a imaginé un « feu central » au cœur du globe, vestige d'une étoile avortée selon Descartes.
D'où vient réellement cette chaleur, et comment une roche solide comme la péridotite peut-elle donner un magma ?

::: definition
**Désintégration radioactive** — transformation spontanée d'un élément radioactif, comme l'uranium, qui libère de l'énergie surtout sous forme de chaleur (réaction exothermique).
**Fusion par décompression** — fusion d'une roche chaude quand la pression qui la maintenait solide diminue plus vite que sa température.
:::

Les éléments radioactifs sont présents dans les couches du globe. Le manuel chiffre la chaleur dégagée par kilomètre cube de roche et donne les volumes :

| Couche | Volume (10⁹ km³) | Chaleur dégagée (J/s par km³) | Puissance totale (10¹² J/s) |
| ------ | ---------------- | ----------------------------- | --------------------------- |
| croûte continentale | 4,5 | 1700 | 7,65 |
| croûte océanique | 4,0 | 340 | 1,36 |
| manteau | 920 | 30 | 27,6 |
| noyau | 180 | non donnée | non calculable |

::: figure Par km³ la croûte continentale dégage le plus, mais le manteau, bien plus volumineux, fournit la plus grande puissance totale (valeurs calculées à partir du tableau)
<svg viewBox="0 0 340 214">
<title>Puissance thermique totale produite par trois couches du globe</title>
<line x1="50" y1="132" x2="320" y2="132" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/>
<line x1="50" y1="84" x2="320" y2="84" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/>
<line x1="50" y1="36" x2="320" y2="36" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/>
<line x1="50" y1="180" x2="324" y2="180" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<line x1="50" y1="180" x2="50" y2="30" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<line x1="46" y1="180" x2="50" y2="180" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="43" y="183" text-anchor="end" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">0</text>
<line x1="46" y1="132" x2="50" y2="132" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="43" y="135" text-anchor="end" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">10</text>
<line x1="46" y1="84" x2="50" y2="84" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="43" y="87" text-anchor="end" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">20</text>
<line x1="46" y1="36" x2="50" y2="36" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="43" y="39" text-anchor="end" font-size="9" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">30</text>
<text x="50" y="20" text-anchor="start" font-size="10" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">puissance totale (10¹² J/s)</text>
<rect x="85" y="143.3" width="52" height="36.7" rx="0" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/>
<text x="111" y="138.3" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">7,65</text>
<text x="111" y="194" text-anchor="middle" font-size="9.5" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">croûte</text>
<text x="111" y="206" text-anchor="middle" font-size="9.5" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">continentale</text>
<rect x="165" y="173.5" width="52" height="6.5" rx="0" fill="#86efac" stroke="#0f172a" stroke-width="1.5"/>
<text x="191" y="168.5" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1,36</text>
<text x="191" y="194" text-anchor="middle" font-size="9.5" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">croûte</text>
<text x="191" y="206" text-anchor="middle" font-size="9.5" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">océanique</text>
<rect x="245" y="47.5" width="52" height="132.5" rx="0" fill="#fdba74" stroke="#0f172a" stroke-width="1.5"/>
<text x="271" y="42.5" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">27,6</text>
<text x="271" y="206" text-anchor="middle" font-size="9.5" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">manteau</text>
</svg>
:::

Chaque barre de la figure est le produit d'un volume par une chaleur par km³ du tableau ; la dernière colonne du tableau donne les mêmes valeurs.

::: exemple Qui produit l'essentiel de la chaleur ?
1. Lire les valeurs par km³ : 1700 J/s pour la croûte continentale, 30 pour le manteau. Par km³, la croûte continentale dégage environ 57 fois plus (1700 ÷ 30 ≈ 57).
2. Calculer les puissances totales, car le total est le produit du volume par la valeur par km³ : croûte continentale 4,5×10⁹ × 1700 = 7,65×10¹² J/s ; croûte océanique 4,0×10⁹ × 340 = 1,36×10¹² J/s ; manteau 920×10⁹ × 30 = 2,76×10¹³ J/s.
3. Comparer : le manteau dégage 27,6×10¹² J/s, bien plus que chaque croûte. Sur les trois couches chiffrées, il fournit environ les trois quarts de la puissance (27,6 ÷ 36,6 ≈ 75 %).
4. Conclure : par son volume, le manteau produit l'essentiel de l'énergie radioactive, diffusée surtout sous forme de chaleur.

:::

::: piege
**Erreur : croire que la couche qui dégage le plus par km³ dégage le plus au total.** La croûte continentale gagne par km³ (1700 contre 30), d'où la tentation de la désigner. Mais son volume est petit : il faut multiplier par le volume, et le manteau l'emporte (27,6 contre 7,65).
:::

::: exemple Pourquoi la péridotite fond-elle en montant ?
1. Situer la roche : une péridotite du manteau supérieur est chaude et solide, car la pression la maintient à l'état solide.
2. Suivre sa montée rapide : en remontant, la pression qui s'exerce sur elle chute beaucoup, alors que sa température baisse peu, faute de temps pour se refroidir.
3. Conclure : n'étant plus maintenue solide par la pression, une partie de la péridotite fond et donne un magma basaltique, surtout dans les 200 premiers kilomètres.

:::

::: propriete
**Origine de l'énergie interne.** Une partie de la chaleur interne vient de la désintégration d'éléments radioactifs (uranium) présents dans les couches du globe ; le manteau en produit l'essentiel, par son volume. Les basaltes viennent de la fusion de péridotites qui montent rapidement : la pression chute plus vite que la température.
Cas limite : le tableau ne donne aucune valeur pour le noyau ; on ne peut donc pas le comparer aux autres couches.
:::

::: verifie À toi : une puissance totale
Une couche de 100×10⁹ km³ dégage 50 J/s par km³. Quelle puissance totale fournit-elle ?

---

On multiplie la valeur par km³ par le volume, car la puissance totale dépend du volume de la couche : 100×10⁹ × 50 = 5×10¹² J/s.
:::

::: retenir
La chaleur interne vient en partie de la désintégration d'éléments radioactifs, dont le manteau fournit l'essentiel par son volume ; les péridotites qui montent vite fondent par décompression.
:::

> 🏆 Les séismes et les volcans te livrent maintenant la carte de l'intérieur du globe : enveloppes, discontinuités, roches et chaleur. Il reste à comprendre comment ces enveloppes bougent, et c'est la tectonique des plaques, au chapitre suivant.
