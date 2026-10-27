# 🚗 La boîte de vitesses : adapter, choisir, immobiliser

> 💡 «Un moteur ne sait tourner efficacement que dans une plage étroite de vitesses. La boîte apprend à la voiture à démarrer en force, puis à filer sans forcer. Et quand elle s'arrête, un petit tambour l'empêche de repartir seule.»

Ce chapitre poursuit le thème « Transmission de puissance », après l'embrayage et le tour. Le support est la **maquette d'une boîte de vitesses d'automobile à commande manuelle** : cinq vitesses avant, une marche arrière, trois arbres. Elle est accompagnée d'un **frein à tambour de stationnement** avec son levier. La maquette est fragile : on la manipule à tour de rôle, en présence du professeur.

> 🗡️ Les schémas de ce cours sont des **schémas de principe**, redessinés pour expliquer. Le dessin d'ensemble du manuel (échelle 1:2, 38 repères) n'est pas reproduit ici, et le manuel ne donne aucun corrigé. Quand un point relève d'un **principe** de mécanique plutôt que du dessin, ou d'une **illustration** aux nombres inventés, le texte le dit.

## 🚗 Où est la boîte ? La chaîne de puissance de l'automobile

Une automobile à deux roues motrices arrière démarre en côte, puis file sur autoroute. Le moteur, lui, tourne dans une plage de vitesses assez étroite, alors que les roues doivent tourner tantôt très lentement avec beaucoup d'effort, tantôt vite. Quelque chose doit adapter ce que donne le moteur à ce que demandent les roues. Quoi, et comment le lit-on sur un schéma ?

::: figure La chaîne de puissance, lue de haut en bas. La puissance P sort du moteur à la vitesse de rotation Nm, traverse l'embrayage, puis la boîte (en vert) la livre adaptée, en P' et N', au pont qui la répartit entre les deux roues motrices arrière
<svg viewBox="0 0 460 340"><title>Chaîne de puissance de l'automobile à deux roues motrices arrière</title><rect x="20" y="6" width="150" height="24" fill="#fef9c3" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><text x="95" y="23" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Énergie chimique</text><line x1="95" y1="30" x2="95" y2="45" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><polygon points="95,52 91.8,45 98.2,45" fill="#0f172a"/><rect x="20" y="52" width="150" height="38" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><text x="95" y="76" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Moteur</text><text x="188" y="75" font-size="12" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Transformer l'énergie</text><line x1="95" y1="90" x2="95" y2="109" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><polygon points="95,116 91.8,109 98.2,109" fill="#0f172a"/><rect x="20" y="116" width="150" height="38" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><text x="95" y="140" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Embrayage</text><text x="188" y="139" font-size="12" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Transmettre ou non la puissance</text><line x1="95" y1="154" x2="95" y2="173" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><polygon points="95,180 91.8,173 98.2,173" fill="#0f172a"/><rect x="20" y="180" width="150" height="38" fill="#bbf7d0" stroke="#0f172a" stroke-width="2.2" stroke-linejoin="round"/><text x="95" y="204" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Boîte de vitesses</text><text x="188" y="203" font-size="12" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Adapter le couple et la vitesse</text><line x1="95" y1="218" x2="95" y2="237" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><polygon points="95,244 91.8,237 98.2,237" fill="#0f172a"/><rect x="20" y="244" width="150" height="38" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><text x="95" y="268" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Pont</text><text x="188" y="261" font-size="12" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Répartir la vitesse sur les deux</text><text x="188" y="276" font-size="12" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">roues motrices arrière</text><text x="108" y="107" font-size="11" font-weight="600" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">P, Nm</text><text x="108" y="171" font-size="11" font-weight="600" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">P, Nm</text><text x="108" y="235" font-size="11" font-weight="600" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">P', N'</text><line x1="95" y1="282" x2="95" y2="301" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><polygon points="95,308 91.8,301 98.2,301" fill="#0f172a"/><rect x="20" y="308" width="150" height="26" fill="#fef9c3" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><text x="95" y="326" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Roues motrices arrière</text></svg>
:::

Chaque bloc du schéma remplit **une fonction** ; celle de la boîte est écrite à côté du bloc vert. Les lettres P, Nm, P' et N' suivent la puissance d'étage en étage : P est la puissance, N une vitesse de rotation en tr/min, Nm celle du moteur (la lettre N suivie de m, à ne pas lire « N·m », unité d'un couple).

::: definition La boîte de vitesses
La **boîte de vitesses** est un système mécanique de **transmission de puissance** : elle permet d'obtenir plusieurs **rapports de vitesses** entre le moteur et les roues motrices. Elle est formée de plusieurs éléments qui, en se déplaçant, changent le rapport. Sa fonction technique : **adapter le couple et la vitesse**.
:::

Pour la ranger dans un schéma de niveau A-0, on place chaque information dans la zone qui lui convient.

::: figure L'actigramme A-0 de la boîte : la puissance entre à gauche et ressort à droite, adaptée ; le choix du conducteur arrive par le haut ; le système est nommé sous le cadre
<svg viewBox="0 0 460 190"><title>Actigramme A-0 de la boîte de vitesses</title><rect x="150" y="70" width="160" height="80" fill="#e2e8f0" stroke="#0f172a" stroke-width="2.5" stroke-linejoin="round"/><text x="230" y="106" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Adapter le couple</text><text x="230" y="124" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">et la vitesse</text><line x1="30" y1="110" x2="143" y2="110" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><polygon points="150,110 143,113.2 143,106.8" fill="#0f172a"/><text x="90" y="88" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Puissance</text><text x="90" y="101" font-size="12" font-weight="600" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(P, Nm)</text><line x1="310" y1="110" x2="423" y2="110" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><polygon points="430,110 423,113.2 423,106.8" fill="#0f172a"/><text x="370" y="88" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Puissance</text><text x="370" y="101" font-size="12" font-weight="600" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(P', N')</text><line x1="230" y1="18" x2="230" y2="63" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><polygon points="230,70 226.8,63 233.2,63" fill="#0f172a"/><text x="242" y="36" font-size="12" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Choix de la vitesse</text><text x="242" y="50" font-size="12" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(position du levier)</text><text x="230" y="176" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Boîte de vitesses</text></svg>
:::

::: exemple Remplir l'actigramme A-0 de la boîte (illustration)
Fonction globale : adapter le couple et la vitesse.
1. **À gauche**, la **matière d'œuvre entrante** : la **puissance mécanique** fournie par l'embrayage, de vitesse Nm. C'est elle que la boîte transforme.
2. **À droite**, la **matière d'œuvre sortante** : la même puissance, **adaptée** (P', N'), qui part vers le pont.
3. **En haut**, les **données de contrôle**, ce qui commande : le **choix de la vitesse**, fait par le conducteur avec le levier. Il ne traverse pas la boîte, il décide de ce qu'elle fait.
4. **Sous le cadre**, le système : la **boîte de vitesses**.

:::

::: verifie
Sur le schéma de la chaîne, quel bloc précède la boîte, et quelle fonction remplit-il ?
---
C'est l'**embrayage** : il **transmet ou non** la puissance du moteur à la boîte. C'est lui qu'on coupe un instant pour changer de vitesse.
:::

::: piege Adapter n'est pas amplifier
On croit parfois que la boîte « donne plus de puissance » en première. Elle **ne crée pas** de puissance : quand elle fait tourner la sortie plus lentement que l'entrée, le **couple** augmente en échange, et inversement. Aux pertes près, la puissance P' ne dépasse pas P.
:::

## 🔢 Le rapport de transmission : combien de tours pour un tour ?

Le pignon (5) de la boîte compte 20 dents ; la roue (6) qui l'attend sur l'arbre intermédiaire en compte 43. Quand le pignon fait un tour, 20 dents passent devant la roue.

Mais la roue a 43 dents à faire passer pour un tour complet. Fait-elle plus ou moins d'un tour ?

::: definition Le rapport de transmission
Le **rapport de transmission** r compare la vitesse de la sortie à celle de l'entrée :

$$ r = N sortie / N entrée $$

Pour un engrenage, avec Z le nombre de dents :

$$ r = Z menante / Z menée $$

Pour plusieurs engrenages en série, on **multiplie** les rapports : N sortie = N entrée × r1 × r2 × … Dans cette section, on ne donne que la **valeur** de r ; le sens de rotation est traité dans la suivante.
:::

| Paire | Roue menante | Roue menée | r | Lecture |
| --- | --- | --- | --- | --- |
| (5) → (6) | 20 dents | 43 dents | 20 / 43 ≈ 0,465 | la sortie tourne moins vite : réduction |

Une ligne du tableau est **une paire** de roues : la menante entraîne, la menée est entraînée ; dans un train, la menée d'un étage est solidaire de la menante de l'étage suivant.

::: exemple De la paire (5, 6) à la vitesse de l'arbre intermédiaire
1. **Un tour d'entrée** : r = 20 / 43 ≈ 0,465. La roue fait donc 0,465 tour, **moins d'un tour** : elle a plus de dents à faire passer.
2. **Une vitesse** : l'arbre d'entrée tourne à Nm = 3 000 tr/min, l'embrayage étant embrayé. N = 3 000 × 20 / 43 ≈ **1 395 tr/min**. Le rapport se multiplie à la vitesse d'entrée, parce que r est un quotient sortie sur entrée.
3. **Deux étages** (illustration) : un pignon de 24 dents mène une roue de 60 dents, puis un pignon de 16 dents mène une roue de 40 dents. r1 = 24 / 60 = 0,4 et r2 = 16 / 40 = 0,4.
4. Le rapport total est r = 0,4 × 0,4 = **0,16**, donc 1 000 tr/min à l'entrée donnent **160 tr/min** : chaque étage agit sur la vitesse que lui laisse le précédent, donc on multiplie.

:::

::: piege Deux roues d'un même arbre ne forment pas une paire
Sur l'arbre intermédiaire, la roue (6) et le pignon (32) **tournent ensemble**, à la même vitesse : (6) est menée par (5), (32) mène la roue suivante. Écrire 43 / 15 pour « passer de (6) à (32) » n'a aucun sens : on ne forme un quotient qu'entre deux roues qui **s'engrènent**.
:::

::: methode Calculer le rapport d'un train
1. **Repérer** les paires qui s'engrènent, dans l'ordre où la puissance les traverse.
2. **Écrire** pour chaque paire Z menante / Z menée.
3. **Multiplier** les quotients.
4. **Appliquer** : N sortie = N entrée × r.

Si la menante a plus de dents que la menée, r est supérieur à 1 : la sortie tourne **plus vite** que l'entrée.
:::

::: verifie
Un pignon de 25 dents mène une roue de 40 dents ; l'arbre d'entrée tourne à 800 tr/min. Que valent r et la vitesse de la roue ?
---
r = 25 / 40 = **0,625** : on met la menante au numérateur. La roue tourne à 800 × 0,625 = **500 tr/min**, moins vite, car elle a plus de dents.
:::

## ↩️ La marche arrière : une roue de renvoi pour inverser le sens

Pour reculer, la sortie doit tourner dans l'autre sens, alors que le moteur ne sait tourner que dans un sens. Rien n'a changé dans le moteur : tout se joue dans le train de roues.

Que fait chaque engrènement au sens de rotation, et où l'inversion se cache-t-elle ?

::: definition Sens de rotation dans un train
Quand deux roues s'engrènent **par l'extérieur**, la roue menée tourne en **sens contraire** de la menante. Dans une chaîne de n engrènements extérieurs, le sens de sortie est **inversé si n est impair**, **conservé si n est pair**. Une **roue de renvoi** est une roue intermédiaire, parfois un bloc de deux roues solidaires comme (33, 34), que l'on ajoute pour obtenir ce changement de sens.
:::

::: figure Le train de la marche arrière, à plat. Chaque ligne de cercles tangents est un engrènement ; les pointillés relient deux roues du même arbre. Les rayons sont proportionnels aux nombres de dents ; les flèches donnent le sens, de l'entrée (5) à la sortie (31)
<svg viewBox="0 0 460 312"><title>Marche arrière : trois engrènements en série, cercles primitifs proportionnels aux nombres de dents</title><path d="M138.8 70 L138.8 170" stroke="#94a3b8" stroke-width="2" stroke-dasharray="6 4" fill="none"/><path d="M185 170 L185 245" stroke="#94a3b8" stroke-width="2" stroke-dasharray="6 4" fill="none"/><circle cx="138.8" cy="70" r="53.8" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><circle cx="60" cy="70" r="25" fill="#bbf7d0" stroke="#0f172a" stroke-width="2"/><circle cx="138.8" cy="170" r="18.8" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><circle cx="185" cy="170" r="27.5" fill="#fed7aa" stroke="#0f172a" stroke-width="2"/><circle cx="185" cy="245" r="27.5" fill="#fed7aa" stroke="#0f172a" stroke-width="2"/><circle cx="268.8" cy="245" r="56.2" fill="#e9d5ff" stroke="#0f172a" stroke-width="2"/><path d="M74.2 58.1 L71.9 55.8 L69.2 54 L66.3 52.6 L63.2 51.8 L60 51.5 L56.8 51.8 L53.7 52.6 L50.8 54 L48.1 55.8 L45.8 58.1 L44 60.8 L42.6 63.7 L41.8 66.8 L41.5 70 L41.8 73.2 L42.6 76.3 L44 79.2 L45.8 81.9 L48.1 84.2 L50.7 86 L53.7 87.4 L56.8 88.2 L60 88.5 L63.2 88.2" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><polygon points="67.1,87.5 60.6,92.3 59.4,85.2" fill="#0f6e56"/><text x="60" y="74" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><path d="M108.3 95.6 L104.3 89.9 L101.4 83.6 L99.6 76.9 L99 70 L99.6 63.1 L101.4 56.4 L104.3 50.1 L108.3 44.4 L113.2 39.5 L118.9 35.6 L125.1 32.6 L131.8 30.8 L138.8 30.2 L145.7 30.8 L152.4 32.6 L158.6 35.6 L164.3 39.5 L169.2 44.4 L173.2 50.1 L176.1 56.4 L177.9 63.1 L178.5 70 L177.9 76.9 L176.1 83.6" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><polygon points="174.8,87.3 173.9,79.3 180.6,81.8" fill="#0f6e56"/><text x="138.8" y="74" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><path d="M128.1 178.9 L126.7 176.9 L125.7 174.7 L125.1 172.4 L124.9 170 L125.1 167.6 L125.7 165.3 L126.7 163.1 L128.1 161.1 L129.8 159.4 L131.8 158 L134 157 L136.3 156.3 L138.8 156.1 L141.2 156.3 L143.5 157 L145.7 158 L147.7 159.4 L149.4 161.1 L150.8 163.1 L151.8 165.3 L152.4 167.6 L152.6 170 L152.4 172.4 L151.8 174.7" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><polygon points="150.5,178.4 149.5,170.5 156.3,172.9" fill="#0f6e56"/><text x="138.8" y="174" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">32</text><path d="M200.6 156.9 L198.1 154.4 L195.2 152.4 L192 150.9 L188.5 150 L185 149.7 L181.5 150 L178 150.9 L174.8 152.4 L171.9 154.4 L169.4 156.9 L167.4 159.8 L165.9 163 L165 166.5 L164.7 170 L165 173.5 L165.9 177 L167.4 180.2 L169.4 183.1 L171.9 185.6 L174.8 187.6 L178 189.1 L181.5 190 L185 190.3 L188.5 190" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><polygon points="192.4,189.4 186,194.2 184.7,187.1" fill="#0f6e56"/><text x="185" y="174" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">33</text><path d="M200.6 231.9 L198.1 229.4 L195.2 227.4 L192 225.9 L188.5 225 L185 224.7 L181.5 225 L178 225.9 L174.8 227.4 L171.9 229.4 L169.4 231.9 L167.4 234.8 L165.9 238 L165 241.5 L164.7 245 L165 248.5 L165.9 252 L167.4 255.2 L169.4 258.1 L171.9 260.6 L174.8 262.6 L178 264.1 L181.5 265 L185 265.4 L188.5 265" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><polygon points="192.4,264.4 186,269.2 184.7,262.1" fill="#0f6e56"/><text x="185" y="249" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">34</text><path d="M236.9 271.8 L232.7 265.8 L229.6 259.2 L227.8 252.2 L227.1 245 L227.8 237.8 L229.6 230.8 L232.7 224.2 L236.9 218.2 L242 213.1 L247.9 209 L254.5 205.9 L261.5 204 L268.8 203.4 L276 204 L283 205.9 L289.6 209 L295.5 213.1 L300.6 218.2 L304.8 224.2 L307.9 230.8 L309.7 237.8 L310.4 245 L309.7 252.2 L307.9 259.2" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><polygon points="306.5,262.9 305.6,255 312.4,257.4" fill="#0f6e56"/><text x="268.8" y="249" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">31</text><text x="60" y="36" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">entrée (1)</text><line x1="141.8" y1="130" x2="176" y2="121" stroke="#475569" stroke-width="1.1"/><text x="178" y="124" font-size="11" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">arbre intermédiaire (35)</text><text x="177" y="209" font-size="11" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">renvoi (33 + 34)</text><text x="228.8" y="180" font-size="11" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">sortie (36)</text></svg>
:::

Dans le schéma, on lit trois engrènements : (5) avec (6), (32) avec (33), (34) avec (31). Les roues (6) et (32) sont sur l'arbre intermédiaire (35), les roues (33) et (34) forment le renvoi.

::: exemple La marche arrière de la boîte (paires données par le manuel)
Nombres de dents : Z5 = 20, Z6 = 43, Z32 = 15, Z33 = 22, Z34 = 22, Z31 = 45.
1. **Le trajet** : (5) mène (6), puis (32) mène (33), puis (34) mène (31). Le trajet est une suite de paires, comme pour tout train.
2. **Le rapport** : 20 / 43 × 15 / 22 × 22 / 45. Les deux 22 se **simplifient**, car (33) et (34) ont le même nombre de dents : il reste 20 × 15 / (43 × 45) = 300 / 1 935 ≈ **0,155**.
3. **Le sens** : trois engrènements extérieurs, donc un nombre **impair** : la sortie tourne en sens **inverse** de l'entrée.
4. **La vitesse** : avec Nm = 3 000 tr/min, N = 3 000 × 0,155 ≈ **465 tr/min**, en sens inverse.

:::

::: piege Le renvoi change le sens, pas toujours la vitesse
On croit que des roues en plus « ralentissent » parce que leurs dents entrent dans le calcul. Ici elles s'y annulent, mais **seulement parce que** Z33 = Z34 = 22. Une roue intermédiaire seule se simplifie toujours ; deux roues solidaires de nombres de dents différents ne se simplifieraient pas, et le rapport changerait.
:::

::: propriete Un nombre pair pour avancer, impair pour reculer
Pour qu'une vitesse avant **conserve** le sens du moteur, il lui faut un nombre **pair** d'engrènements extérieurs. La marche arrière en compte **trois** : c'est ce qui la fait reculer.
:::

::: verifie
Un train comporte cinq engrènements extérieurs. La sortie tourne-t-elle dans le sens de l'entrée ?
---
**Non** : cinq est impair, donc le sens est inversé. Chaque engrènement inverse le sens ; quatre inversions se compensent deux à deux, la cinquième reste.
:::

## 🕹️ Choisir une vitesse : du levier au baladeur

Tu déplaces le levier (21) d'une position à l'autre, et le rapport change. Pourtant ta main ne touche aucune roue dentée.

Qui reçoit ton geste, qui le transmet, et qu'est-ce qui, au bout, change le chemin de la puissance ?

::: definition Fourchette, baladeur, point mort
Un **baladeur** est une pièce qui **coulisse** le long d'un arbre pour changer le chemin de la puissance : selon sa position, il met en service l'une ou l'autre des roues voisines, ou aucune. Une **fourchette**, dont les branches se logent dans une gorge du baladeur, le déplace. Le **levier de changement de vitesses** commande les fourchettes.

Au **point mort**, le baladeur ne relie **aucune** roue à l'arbre : l'arbre de sortie n'est pas entraîné, donc le rapport de transmission est **nul** (r = 0).
:::

::: figure Le même baladeur (vert), déplacé par sa fourchette (orange) entre deux roues (bleues) qui tournent librement sur l'arbre. Première vue : point mort. Deuxième et troisième vues : décalé à gauche, puis à droite, il emboîte ses crabots dans ceux de la roue voisine et la lie à l'arbre. Schéma de principe
<svg viewBox="0 0 460 130"><title>Un baladeur et sa fourchette : point mort, accouplement à gauche, accouplement à droite</title><g transform="translate(10 0)"><rect x="0" y="52" width="140" height="12" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="6" y="30" width="30" height="56" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="36" y="36" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="36" y="52" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="36" y="68" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="104" y="30" width="30" height="56" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="98" y="44" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="98" y="60" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="98" y="76" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="50" y="44" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="50" y="60" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="50" y="76" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="84" y="36" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="84" y="52" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="84" y="68" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="56" y="34" width="28" height="48" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="65" y="6" width="10" height="26" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="61" y="28" width="18" height="8" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><text x="70" y="104" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Point mort</text><text x="70" y="119" font-size="10.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">aucune roue accouplée</text></g><g transform="translate(158 0)"><rect x="0" y="52" width="140" height="12" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="6" y="30" width="30" height="56" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="36" y="36" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="36" y="52" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="36" y="68" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="104" y="30" width="30" height="56" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="98" y="44" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="98" y="60" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="98" y="76" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="36" y="44" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="36" y="60" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="36" y="76" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="70" y="36" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="70" y="52" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="70" y="68" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="42" y="34" width="28" height="48" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="51" y="6" width="10" height="26" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="47" y="28" width="18" height="8" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><text x="70" y="104" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Baladeur à gauche</text><text x="70" y="119" font-size="10.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">roue de gauche accouplée</text></g><g transform="translate(306 0)"><rect x="0" y="52" width="140" height="12" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="6" y="30" width="30" height="56" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="36" y="36" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="36" y="52" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="36" y="68" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="104" y="30" width="30" height="56" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="98" y="44" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="98" y="60" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="98" y="76" width="6" height="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="64" y="44" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="64" y="60" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="64" y="76" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="98" y="36" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="98" y="52" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="98" y="68" width="6" height="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="70" y="34" width="28" height="48" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="79" y="6" width="10" height="26" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="75" y="28" width="18" height="8" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><text x="70" y="104" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Baladeur à droite</text><text x="70" y="119" font-size="10.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">roue de droite accouplée</text></g></svg>
:::

La nomenclature de la maquette compte **trois baladeurs** (12, 24, 30) et **trois fourchettes** (11, 23, 29). En manœuvrant le levier, on obtient **six positions de marche** et le point mort :

| Position du levier | Nombre | Rapport r | Sens de sortie |
| --- | --- | --- | --- |
| Point mort | 1 | 0 | la sortie n'est pas entraînée |
| 1, 2, 3, 4, 5 | 5 vitesses avant | valeurs positives, différentes | celui du moteur |
| MA | 1 marche arrière | valeur absolue de r, positive (le sens est donné à part) | inversé |

::: exemple Passer une vitesse, geste après geste (principe)
1. **Débrayer** : on appuie sur la pédale, la puissance du moteur est coupée. C'est nécessaire parce que les pièces qui vont s'engager ne doivent plus être poussées par le moteur.
2. **Déplacer le levier (21)** : il s'articule sur sa **rotule (19)**, logée dans le carter (38), ce qui lui laisse deux directions : choisir la fourchette, puis la pousser.
3. **La fourchette** déplace le baladeur le long de son arbre : seule la fourchette touche le baladeur.
4. **Le baladeur** relie à l'arbre la roue choisie : le chemin de la puissance change, donc le rapport change.
5. **Rembrayer** : la puissance repasse par le chemin choisi.

:::

::: piege Le point mort n'est pas un rapport égal à 1
On croit que « rien ne bouge » veut dire « la sortie suit l'entrée ». C'est l'inverse : au point mort **rien ne relie** la sortie à l'entrée. Le rapport est **0**, pas 1, et l'arbre de sortie reste libre.
:::

::: verifie
Un baladeur se trouve à égale distance de ses deux roues voisines, sans en toucher aucune. À quelle position du levier cela correspond-il, et que vaut r ?
---
Au **point mort** : aucune roue n'est reliée à l'arbre de sortie, donc **r = 0**.
:::

## 🧩 Qui guide quoi ? Les solutions technologiques de la boîte

Dans la boîte, chaque pièce mobile ne doit bouger que d'une seule façon : les arbres tournent sans se déplacer, le baladeur glisse sans basculer, la fourchette pousse sans tourner.

Pour chaque mouvement permis, une pièce l'autorise et interdit tous les autres. Comment les reconnaître, et quelle liaison chacune réalise-t-elle ?

::: methode Trouver la solution d'une fonction de guidage (principe)
1. **Nommer** le mouvement autorisé : une rotation seule, ou une translation seule.
2. **En déduire la liaison** : rotation seule, un **pivot** ; translation seule, une **glissière**.
3. **Choisir la solution habituelle** : des **roulements** pour un pivot ; une **tige**, des **cannelures** ou une clavette pour une glissière.
4. **Chercher ce qui provoque** le mouvement : un guidage l'autorise, il ne le provoque pas.
:::

| Fonction | Liaison | Solution habituelle (principe) |
| --- | --- | --- |
| Guider en rotation un arbre | pivot | roulements ; la nomenclature compte 4 roulements de type BC (4) |
| Guider en translation une roue ou un baladeur qui coulisse sur son arbre, comme la roue (31) sur l'arbre de sortie (36) | glissière | cannelures, qui l'entraînent aussi en rotation |
| Guider en translation un coulisseau | glissière | une tige : la nomenclature compte 3 coulisseaux (22) et 3 tiges (28) |
| Déplacer un baladeur | aucune : c'est une commande | une fourchette, commandée par le levier |

Les trois premières lignes disent **ce qui est permis** ; la dernière dit **ce qui pousse**.

::: exemple Lire les pièces de la boîte
1. L'**arbre d'entrée (1)** tourne dans le carter sans se déplacer : rotation seule, donc un **pivot**, réalisé par des roulements.
2. Un **baladeur** glisse le long de son arbre et tourne avec lui : translation seule par rapport à l'arbre, donc une **glissière**, par exemple par cannelures.
3. Le **pignon (5)** et la **roue (6)** ne sont pas guidés l'un par rapport à l'autre : leurs dents sont en contact, c'est un **engrènement**, qui transmet la rotation d'un arbre à l'autre.

:::

::: piege Une glissière ne déplace rien
Guider un baladeur en translation, ce n'est pas le déplacer : les cannelures **permettent** le glissement, mais c'est la **fourchette**, poussée par le levier, qui le provoque. Sans fourchette, le baladeur resterait où il est.
:::

::: verifie
Un coulisseau doit aller et venir sans tourner. Quelle liaison a-t-il avec la pièce qui le guide ?
---
Une **glissière** : une translation seule est autorisée, la rotation est interdite. La solution habituelle est une tige sur laquelle il coulisse.
:::

## 🦷 Le crabotage : transmettre par obstacle, sans glisser

À l'embrayage, la puissance passe par frottement : le disque presse le volant et peut glisser.

Dans la boîte, quand le baladeur relie une roue à son arbre, on ne veut **aucun** glissement : la roue doit tourner exactement avec l'arbre. Comment lier deux pièces sans qu'elles puissent glisser l'une sur l'autre ?

Ce chapitre étudie le cas du **crabotage**, que le manuel demande pour la 3ᵉ vitesse. Pour d'autres positions, l'engagement peut se faire autrement : la paire (34, 31) de la marche arrière s'engage par glissement de la roue (31). Les paires de chacune des cinq vitesses avant ne sont pas calculées ici : elles se lisent sur le schéma cinématique du manuel, qui n'est pas reproduit dans ce chapitre.

::: definition Crabotage et adhérence
Le **crabotage** est un accouplement par **obstacle** : des dents frontales, les **crabots**, taillées sur deux pièces, s'emboîtent comme des doigts entrelacés. Tant qu'elles sont emboîtées, les deux pièces tournent ensemble, **sans glissement**.

L'accouplement par **adhérence**, celui de l'embrayage à disque, utilise au contraire le **frottement** : il peut glisser.
:::

::: figure Gros plan sur les crabots. À gauche, les dents de la roue (bleue) et celles du baladeur (vert) se font face sans se toucher : la roue tourne librement. À droite, elles sont entrelacées : l'une ne peut plus tourner sans entraîner l'autre
<svg viewBox="0 0 460 138"><title>Gros plan sur les crabots : séparés, puis emboîtés</title><g transform="translate(20 0)"><rect x="0" y="28" width="52" height="64" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="26" y="64" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">roue</text><rect x="52" y="34" width="12" height="8" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="52" y="50" width="12" height="8" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="52" y="66" width="12" height="8" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="88" y="42" width="12" height="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="88" y="58" width="12" height="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="88" y="74" width="12" height="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="100" y="28" width="52" height="64" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="126" y="64" font-size="10.5" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">baladeur</text><text x="76" y="112" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Crabots séparés</text><text x="76" y="127" font-size="10.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">la roue tourne librement</text></g><g transform="translate(260 0)"><rect x="0" y="28" width="52" height="64" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="26" y="64" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">roue</text><rect x="52" y="34" width="12" height="8" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="52" y="50" width="12" height="8" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="52" y="66" width="12" height="8" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="52" y="42" width="12" height="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="52" y="58" width="12" height="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="52" y="74" width="12" height="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><rect x="64" y="28" width="52" height="64" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="90" y="64" font-size="10.5" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">baladeur</text><text x="58" y="112" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Crabots emboîtés</text><text x="58" y="127" font-size="10.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">roue et baladeur tournent ensemble</text></g></svg>
:::

La roue et le baladeur de ce gros plan sont ceux de la figure du baladeur, vus de plus près.

| | Obstacle | Adhérence |
| --- | --- | --- |
| Principe | **obstacle** : des formes qui s'emboîtent | **frottement** : des surfaces pressées |
| Glissement | aucun | possible au-delà d'une limite |
| Exemples | crabots d'un baladeur (le crabotage), clavette, cannelures | disque d'embrayage, garnitures d'un frein |

::: exemple Obstacle ou adhérence ?
1. Le **disque d'embrayage** pressé contre le volant : c'est du **frottement**, donc de l'**adhérence** ; il peut patiner un instant, ce qui permet la mise en charge progressive.
2. Les **crabots du baladeur** emboîtés dans la roue : une forme barre le chemin de l'autre, donc de l'**obstacle** ; aucun glissement n'est possible.
3. Une **clavette** dans ses rainures (chapitre sur les assemblages) : elle fait obstacle à la rotation, donc de l'**obstacle**, comme des cannelures.

:::

::: piege On débraye avant d'emboîter les crabots
Passer une vitesse sans débrayer force les crabots à s'emboîter pendant que le moteur pousse : ils se heurtent, avec le grincement bien connu. Avec l'adhérence, un glissement absorbe l'écart entre les deux pièces ; avec l'obstacle, **rien ne peut glisser**, donc on supprime d'abord la poussée du moteur.
:::

::: verifie
Pour la 3ᵉ vitesse, que le manuel étudie, la liaison entre le baladeur et la roue est-elle obtenue par crabotage ou par adhérence ? Pourquoi ?
---
Par **crabotage** : le baladeur lie la roue à l'arbre par des crabots qui s'emboîtent (obstacle), sans frottement ni glissement.
:::

## ⚙️ Quatre types d'engrenages : l'orientation des arbres, la forme des dents

Regarde les roues de la boîte : toutes ont des dents, mais certaines les ont droites, d'autres inclinées.

Sur le chariot élévateur du chapitre sur les assemblages, un pignon conique changeait même la direction de l'arbre. Quelles différences comptent vraiment, et comment les nomme-t-on ?

::: definition Quatre types d'engrenages
On classe un engrenage selon la position des arbres et la forme des dents :
- **extérieur à denture droite** : arbres parallèles, dents parallèles à l'axe ;
- **hélicoïdal** : arbres le plus souvent parallèles, dents inclinées en hélice ;
- **intérieur** : une roue a ses dents à l'intérieur d'une couronne, et les deux roues tournent dans le **même sens** ;
- **conique** : arbres qui se coupent, souvent à angle droit, dents taillées sur des cônes.
:::

::: figure Les quatre types d'engrenages vus de côté, ou en coupe pour l'engrenage intérieur. Seuls les deux premiers relient des arbres parallèles par l'extérieur, comme dans la boîte
<svg viewBox="0 0 460 295"><title>Quatre types d'engrenages : dentures droites, hélicoïdales, intérieures et coniques</title><g transform="translate(0 0)"><g transform="translate(0 0)"><rect x="60" y="22" width="44" height="70" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="104" y="22" width="44" height="70" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="68" y1="24" x2="68" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="76" y1="24" x2="76" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="84" y1="24" x2="84" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="92" y1="24" x2="92" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="100" y1="24" x2="100" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="112" y1="24" x2="112" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="120" y1="24" x2="120" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="128" y1="24" x2="128" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="136" y1="24" x2="136" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="144" y1="24" x2="144" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="82" y1="14" x2="82" y2="100" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="7 3 2 3"/><line x1="126" y1="14" x2="126" y2="100" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="7 3 2 3"/><text x="104" y="136" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Extérieur à denture droite</text></g></g><g transform="translate(230 0)"><g transform="translate(0 0)"><rect x="60" y="22" width="44" height="70" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="104" y="22" width="44" height="70" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="61" y1="40.8" x2="68" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="61" y1="62.4" x2="76" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="61" y1="83.9" x2="84" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="66" y1="92" x2="92" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="74" y1="92" x2="100" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="82" y1="92" x2="103" y2="35.5" stroke="#0f172a" stroke-width="1.2"/><line x1="90" y1="92" x2="103" y2="57" stroke="#0f172a" stroke-width="1.2"/><line x1="98" y1="92" x2="103" y2="78.5" stroke="#0f172a" stroke-width="1.2"/><line x1="112" y1="92" x2="105" y2="73.2" stroke="#0f172a" stroke-width="1.2"/><line x1="120" y1="92" x2="105" y2="51.6" stroke="#0f172a" stroke-width="1.2"/><line x1="128" y1="92" x2="105" y2="30.1" stroke="#0f172a" stroke-width="1.2"/><line x1="136" y1="92" x2="110" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="144" y1="92" x2="118" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="147" y1="78.5" x2="126" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="147" y1="57" x2="134" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="147" y1="35.5" x2="142" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="82" y1="14" x2="82" y2="100" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="7 3 2 3"/><line x1="126" y1="14" x2="126" y2="100" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="7 3 2 3"/><text x="104" y="136" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Hélicoïdal</text></g></g><g transform="translate(0 150)"><g transform="translate(0 0)"><circle cx="104" cy="58" r="60" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><circle cx="104" cy="58" r="52" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><line x1="156" y1="58" x2="150" y2="58" stroke="#0f172a" stroke-width="1.4"/><line x1="155.2" y1="67" x2="149.3" y2="66" stroke="#0f172a" stroke-width="1.4"/><line x1="152.9" y1="75.8" x2="147.2" y2="73.7" stroke="#0f172a" stroke-width="1.4"/><line x1="149" y1="84" x2="143.8" y2="81" stroke="#0f172a" stroke-width="1.4"/><line x1="143.8" y1="91.4" x2="139.2" y2="87.6" stroke="#0f172a" stroke-width="1.4"/><line x1="137.4" y1="97.8" x2="133.6" y2="93.2" stroke="#0f172a" stroke-width="1.4"/><line x1="130" y1="103" x2="127" y2="97.8" stroke="#0f172a" stroke-width="1.4"/><line x1="121.8" y1="106.9" x2="119.7" y2="101.2" stroke="#0f172a" stroke-width="1.4"/><line x1="113" y1="109.2" x2="112" y2="103.3" stroke="#0f172a" stroke-width="1.4"/><line x1="104" y1="110" x2="104" y2="104" stroke="#0f172a" stroke-width="1.4"/><line x1="95" y1="109.2" x2="96" y2="103.3" stroke="#0f172a" stroke-width="1.4"/><line x1="86.2" y1="106.9" x2="88.3" y2="101.2" stroke="#0f172a" stroke-width="1.4"/><line x1="78" y1="103" x2="81" y2="97.8" stroke="#0f172a" stroke-width="1.4"/><line x1="70.6" y1="97.8" x2="74.4" y2="93.2" stroke="#0f172a" stroke-width="1.4"/><line x1="64.2" y1="91.4" x2="68.8" y2="87.6" stroke="#0f172a" stroke-width="1.4"/><line x1="59" y1="84" x2="64.2" y2="81" stroke="#0f172a" stroke-width="1.4"/><line x1="55.1" y1="75.8" x2="60.8" y2="73.7" stroke="#0f172a" stroke-width="1.4"/><line x1="52.8" y1="67" x2="58.7" y2="66" stroke="#0f172a" stroke-width="1.4"/><line x1="52" y1="58" x2="58" y2="58" stroke="#0f172a" stroke-width="1.4"/><line x1="52.8" y1="49" x2="58.7" y2="50" stroke="#0f172a" stroke-width="1.4"/><line x1="55.1" y1="40.2" x2="60.8" y2="42.3" stroke="#0f172a" stroke-width="1.4"/><line x1="59" y1="32" x2="64.2" y2="35" stroke="#0f172a" stroke-width="1.4"/><line x1="64.2" y1="24.6" x2="68.8" y2="28.4" stroke="#0f172a" stroke-width="1.4"/><line x1="70.6" y1="18.2" x2="74.4" y2="22.8" stroke="#0f172a" stroke-width="1.4"/><line x1="78" y1="13" x2="81" y2="18.2" stroke="#0f172a" stroke-width="1.4"/><line x1="86.2" y1="9.1" x2="88.3" y2="14.8" stroke="#0f172a" stroke-width="1.4"/><line x1="95" y1="6.8" x2="96" y2="12.7" stroke="#0f172a" stroke-width="1.4"/><line x1="104" y1="6" x2="104" y2="12" stroke="#0f172a" stroke-width="1.4"/><line x1="113" y1="6.8" x2="112" y2="12.7" stroke="#0f172a" stroke-width="1.4"/><line x1="121.8" y1="9.1" x2="119.7" y2="14.8" stroke="#0f172a" stroke-width="1.4"/><line x1="130" y1="13" x2="127" y2="18.2" stroke="#0f172a" stroke-width="1.4"/><line x1="137.4" y1="18.2" x2="133.6" y2="22.8" stroke="#0f172a" stroke-width="1.4"/><line x1="143.8" y1="24.6" x2="139.2" y2="28.4" stroke="#0f172a" stroke-width="1.4"/><line x1="149" y1="32" x2="143.8" y2="35" stroke="#0f172a" stroke-width="1.4"/><line x1="152.9" y1="40.2" x2="147.2" y2="42.3" stroke="#0f172a" stroke-width="1.4"/><line x1="155.2" y1="49" x2="149.3" y2="50" stroke="#0f172a" stroke-width="1.4"/><circle cx="133" cy="58" r="20" fill="#bbf7d0" stroke="#0f172a" stroke-width="2"/><line x1="153" y1="58" x2="158" y2="58" stroke="#0f172a" stroke-width="1.4"/><line x1="150.3" y1="68" x2="154.7" y2="70.5" stroke="#0f172a" stroke-width="1.4"/><line x1="143" y1="75.3" x2="145.5" y2="79.7" stroke="#0f172a" stroke-width="1.4"/><line x1="133" y1="78" x2="133" y2="83" stroke="#0f172a" stroke-width="1.4"/><line x1="123" y1="75.3" x2="120.5" y2="79.7" stroke="#0f172a" stroke-width="1.4"/><line x1="115.7" y1="68" x2="111.3" y2="70.5" stroke="#0f172a" stroke-width="1.4"/><line x1="113" y1="58" x2="108" y2="58" stroke="#0f172a" stroke-width="1.4"/><line x1="115.7" y1="48" x2="111.3" y2="45.5" stroke="#0f172a" stroke-width="1.4"/><line x1="123" y1="40.7" x2="120.5" y2="36.3" stroke="#0f172a" stroke-width="1.4"/><line x1="133" y1="38" x2="133" y2="33" stroke="#0f172a" stroke-width="1.4"/><line x1="143" y1="40.7" x2="145.5" y2="36.3" stroke="#0f172a" stroke-width="1.4"/><line x1="150.3" y1="48" x2="154.7" y2="45.5" stroke="#0f172a" stroke-width="1.4"/><circle cx="133" cy="58" r="2.5" fill="#0f172a"/><circle cx="104" cy="58" r="2.5" fill="#0f172a"/><text x="104" y="136" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Intérieur à denture droite</text></g></g><g transform="translate(230 150)"><g transform="translate(0 0)"><line x1="50" y1="40" x2="130" y2="40" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="7 3 2 3"/><line x1="120" y1="30" x2="120" y2="110" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="7 3 2 3"/><polygon points="108,28 108,52 80,80 80,0" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><polygon points="108,52 132,52 160,80 80,80" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="80" y1="10" x2="74" y2="10" stroke="#0f172a" stroke-width="1.6"/><line x1="90" y1="80" x2="90" y2="86" stroke="#0f172a" stroke-width="1.6"/><line x1="80" y1="25" x2="74" y2="25" stroke="#0f172a" stroke-width="1.6"/><line x1="105" y1="80" x2="105" y2="86" stroke="#0f172a" stroke-width="1.6"/><line x1="80" y1="40" x2="74" y2="40" stroke="#0f172a" stroke-width="1.6"/><line x1="120" y1="80" x2="120" y2="86" stroke="#0f172a" stroke-width="1.6"/><line x1="80" y1="55" x2="74" y2="55" stroke="#0f172a" stroke-width="1.6"/><line x1="135" y1="80" x2="135" y2="86" stroke="#0f172a" stroke-width="1.6"/><line x1="80" y1="70" x2="74" y2="70" stroke="#0f172a" stroke-width="1.6"/><line x1="150" y1="80" x2="150" y2="86" stroke="#0f172a" stroke-width="1.6"/><text x="104" y="136" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Conique</text></g></g></svg>
:::

::: exemple Classer les roues de la boîte
1. Les trois arbres de la boîte sont **parallèles** (principe d'une boîte à engrenages cylindriques) : le type **conique**, qui exige des arbres concourants, est écarté.
2. La roue (34), à denture **droite** (donnée du manuel), donne le type **extérieur à denture droite**.
3. Les roues (16) et (17), à dentures **hélicoïdales** (donnée du manuel), donnent le type **hélicoïdal**.
4. Un engrenage **intérieur** exige une couronne : aucune pièce de la nomenclature n'est désignée ainsi, on ne le retient pas.

:::

::: piege Des dents inclinées ne font pas un engrenage conique
Les dents d'une roue hélicoïdale sont inclinées, celles d'une roue conique sont taillées sur un cône : on confond parfois les deux. Ce qui fait un engrenage **conique**, c'est l'**angle entre les arbres**, qui se coupent ; un engrenage hélicoïdal relie ici des arbres parallèles.
:::

::: propriete Droite ou hélicoïdale ?
| | Denture droite | Denture hélicoïdale |
| --- | --- | --- |
| Fonctionnement | les dents entrent en contact d'un coup : plus bruyant | contact progressif : plus silencieux |
| Effort sur les arbres | radial seulement | radial **et axial** (poussée) |
| Engagement par glissement le long de l'arbre | facile : pas de poussée axiale | gênée par la poussée axiale |

Application, par principe : une roue qu'on engage en la faisant **coulisser**, comme la roue (31) de la marche arrière qui s'engage avec (34), est de préférence droite : (31) et (34) sont donc droites. Une paire qui reste en prise et doit être silencieuse, comme (16) et (17), est hélicoïdale ; sa poussée axiale est alors reprise par les roulements des arbres, qui doivent être choisis pour la supporter (un roulement à billes à contact radial seul la supporte mal).
:::

::: verifie
Deux arbres se coupent à angle droit en un point. Quel type d'engrenage faut-il choisir ?
---
Un engrenage **conique** : les arbres se coupent, et ses dents sont taillées sur des cônes. Les engrenages à dentures droite ou hélicoïdale relient des arbres parallèles.
:::

## 🤝 Quand deux roues peuvent-elles s'engrener ? Les conditions d'engrènement

Essaie d'engrener une roue aux grosses dents avec une roue aux petites dents : elles se bloquent, même sur des arbres bien placés.

Qu'est-ce qui doit être pareil entre deux roues pour qu'elles tournent ensemble sans se gêner ?

::: definition Module et conditions d'engrènement
Le **module** m est un nombre qui mesure la **taille des dents**. Deux roues extérieures peuvent s'engrener si :
- **denture droite** : elles ont le **même module** ;
- **denture hélicoïdale** : elles ont le **même module**, le **même angle d'inclinaison** des dents (angle d'hélice) et des **hélices de sens contraires**, l'une à droite et l'autre à gauche.

Le nombre de dents n'est pas une condition : c'est justement lui qui fixe le rapport r. L'angle de pression des dents est normalisé, on ne le compare pas ici.
:::

::: figure Trois paires de roues vues de côté. Dentures droites : même module suffit. Hélices contraires, de même angle : les dents se rejoignent au contact. Hélices de même sens : au contact, les dents se croisent au lieu de se rejoindre
<svg viewBox="0 0 460 132"><title>Conditions d'engrènement : dentures droites, hélices contraires, hélices de même sens</title><g transform="translate(0 0)"><rect x="12" y="22" width="44" height="70" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="56" y="22" width="44" height="70" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="20" y1="24" x2="20" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="28" y1="24" x2="28" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="36" y1="24" x2="36" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="44" y1="24" x2="44" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="52" y1="24" x2="52" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="64" y1="24" x2="64" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="72" y1="24" x2="72" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="80" y1="24" x2="80" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="88" y1="24" x2="88" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="96" y1="24" x2="96" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="34" y1="14" x2="34" y2="100" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="7 3 2 3"/><line x1="78" y1="14" x2="78" y2="100" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="7 3 2 3"/><text x="78" y="108" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Dentures droites</text><text x="78" y="122" font-size="10" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">même module</text><text x="78" y="14" font-size="16" font-weight="700" text-anchor="middle" fill="#16a34a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">✓</text></g><g transform="translate(150 0)"><rect x="12" y="22" width="44" height="70" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="56" y="22" width="44" height="70" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="13" y1="40.8" x2="20" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="13" y1="62.4" x2="28" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="13" y1="83.9" x2="36" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="18" y1="92" x2="44" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="26" y1="92" x2="52" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="34" y1="92" x2="55" y2="35.5" stroke="#0f172a" stroke-width="1.2"/><line x1="42" y1="92" x2="55" y2="57" stroke="#0f172a" stroke-width="1.2"/><line x1="50" y1="92" x2="55" y2="78.5" stroke="#0f172a" stroke-width="1.2"/><line x1="64" y1="92" x2="57" y2="73.2" stroke="#0f172a" stroke-width="1.2"/><line x1="72" y1="92" x2="57" y2="51.6" stroke="#0f172a" stroke-width="1.2"/><line x1="80" y1="92" x2="57" y2="30.1" stroke="#0f172a" stroke-width="1.2"/><line x1="88" y1="92" x2="62" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="96" y1="92" x2="70" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="99" y1="78.5" x2="78" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="99" y1="57" x2="86" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="99" y1="35.5" x2="94" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="34" y1="14" x2="34" y2="100" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="7 3 2 3"/><line x1="78" y1="14" x2="78" y2="100" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="7 3 2 3"/><text x="78" y="108" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Hélices contraires</text><text x="78" y="122" font-size="10" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">même angle et même module</text><text x="78" y="14" font-size="16" font-weight="700" text-anchor="middle" fill="#16a34a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">✓</text></g><g transform="translate(300 0)"><rect x="12" y="22" width="44" height="70" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="56" y="22" width="44" height="70" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="13" y1="40.8" x2="20" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="13" y1="62.4" x2="28" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="13" y1="83.9" x2="36" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="18" y1="92" x2="44" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="26" y1="92" x2="52" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="34" y1="92" x2="55" y2="35.5" stroke="#0f172a" stroke-width="1.2"/><line x1="42" y1="92" x2="55" y2="57" stroke="#0f172a" stroke-width="1.2"/><line x1="50" y1="92" x2="55" y2="78.5" stroke="#0f172a" stroke-width="1.2"/><line x1="57" y1="40.8" x2="64" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="57" y1="62.4" x2="72" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="57" y1="83.9" x2="80" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="62" y1="92" x2="88" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="70" y1="92" x2="96" y2="22" stroke="#0f172a" stroke-width="1.2"/><line x1="78" y1="92" x2="99" y2="35.5" stroke="#0f172a" stroke-width="1.2"/><line x1="86" y1="92" x2="99" y2="57" stroke="#0f172a" stroke-width="1.2"/><line x1="94" y1="92" x2="99" y2="78.5" stroke="#0f172a" stroke-width="1.2"/><line x1="34" y1="14" x2="34" y2="100" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="7 3 2 3"/><line x1="78" y1="14" x2="78" y2="100" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="7 3 2 3"/><text x="78" y="108" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Hélices de même sens</text><text x="78" y="122" font-size="10" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">elles ne peuvent pas s'engrener</text><text x="78" y="14" font-size="16" font-weight="700" text-anchor="middle" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">✗</text></g></svg>
:::

Au contact, les dents des deux roues doivent être **parallèles** : c'est ce qui impose des hélices de sens contraires. Sur le dessin, les faces visibles de deux cylindres tracent « / » et « \ », et les dents se rejoignent au contact.

::: exemple Ces deux roues peuvent-elles s'engrener ? (nombres d'illustration)
1. Roue A : module 2, denture droite ; roue B : module 2, denture droite. **Même module** : oui, même si leurs nombres de dents diffèrent.
2. Roue C : module 2, hélice à droite de 20° ; roue D : module 2, hélice à droite de 20°. Même module, même angle, mais hélices de **même sens** : non.
3. Roue D' : module 2, hélice à **gauche** de 20°. Avec C, les trois conditions sont remplies : oui.
4. Roue E : module 2,5, denture droite, avec A (module 2) : modules **différents**, non.

:::

::: piege Le même nombre de dents n'est pas une condition
On croit qu'il faut deux roues « pareilles ». Si elles avaient le même nombre de dents, r vaudrait 1 et la paire ne changerait pas la vitesse : ce qui doit être **identique**, c'est le **module** (et, pour des hélices, l'angle). Quant aux hélices, elles doivent être de sens **contraires**, pas parallèles : ce sont les dents au contact qui doivent l'être.
:::

::: verifie
Deux roues hélicoïdales de module 3 ont toutes deux une hélice à gauche de 15°. Peuvent-elles s'engrener ?
---
**Non** : le module et l'angle conviennent, mais les hélices ont le **même sens**. Il faudrait une des deux roues à hélice **à droite**.
:::

## 📈 La courbe N'36 = f(N'1) : une droite dont la pente est r

Le manuel trace, pour chaque vitesse, le **nombre de tours** N'36 de l'arbre de sortie en fonction du nombre de tours N'1 de l'arbre d'entrée. Ce ne sont pas des vitesses en tr/min, mais des nombres de tours. Pour la deuxième vitesse, il donne un point : quand l'entrée fait 2,5 tours, la sortie en fait 0,64. Quelle courbe passe par là, et que dit-elle du rapport ?

::: figure Le point relevé par le manuel pour la deuxième vitesse (2,5 ; 0,64) est sur la droite b. Les droites a et c sont des droites d'illustration, pour comparer les pentes
<svg viewBox="0 0 460 300"><title>Courbes N'36 = f(N'1) : le point du manuel sur la droite b, deux droites d'illustration</title><line x1="62" y1="254" x2="62" y2="24" stroke="#e2e8f0" stroke-width="1"/><text x="62" y="270" font-size="11" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="124.3" y1="254" x2="124.3" y2="24" stroke="#e2e8f0" stroke-width="1"/><text x="124.3" y="270" font-size="11" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="186.7" y1="254" x2="186.7" y2="24" stroke="#e2e8f0" stroke-width="1"/><text x="186.7" y="270" font-size="11" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="249" y1="254" x2="249" y2="24" stroke="#e2e8f0" stroke-width="1"/><text x="249" y="270" font-size="11" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="311.3" y1="254" x2="311.3" y2="24" stroke="#e2e8f0" stroke-width="1"/><text x="311.3" y="270" font-size="11" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="373.7" y1="254" x2="373.7" y2="24" stroke="#e2e8f0" stroke-width="1"/><text x="373.7" y="270" font-size="11" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="436" y1="254" x2="436" y2="24" stroke="#e2e8f0" stroke-width="1"/><text x="436" y="270" font-size="11" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="62" y1="254" x2="436" y2="254" stroke="#e2e8f0" stroke-width="1"/><text x="56" y="258" font-size="11" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="62" y1="231" x2="436" y2="231" stroke="#e2e8f0" stroke-width="1"/><text x="56" y="235" font-size="11" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,2</text><line x1="62" y1="208" x2="436" y2="208" stroke="#e2e8f0" stroke-width="1"/><text x="56" y="212" font-size="11" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,4</text><line x1="62" y1="185" x2="436" y2="185" stroke="#e2e8f0" stroke-width="1"/><text x="56" y="189" font-size="11" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,6</text><line x1="62" y1="162" x2="436" y2="162" stroke="#e2e8f0" stroke-width="1"/><text x="56" y="166" font-size="11" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,8</text><line x1="62" y1="139" x2="436" y2="139" stroke="#e2e8f0" stroke-width="1"/><text x="56" y="143" font-size="11" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="62" y1="116" x2="436" y2="116" stroke="#e2e8f0" stroke-width="1"/><text x="56" y="120" font-size="11" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,2</text><line x1="62" y1="93" x2="436" y2="93" stroke="#e2e8f0" stroke-width="1"/><text x="56" y="97" font-size="11" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,4</text><line x1="62" y1="70" x2="436" y2="70" stroke="#e2e8f0" stroke-width="1"/><text x="56" y="74" font-size="11" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,6</text><line x1="62" y1="47" x2="436" y2="47" stroke="#e2e8f0" stroke-width="1"/><text x="56" y="51" font-size="11" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,8</text><line x1="62" y1="24" x2="436" y2="24" stroke="#e2e8f0" stroke-width="1"/><text x="56" y="28" font-size="11" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><path d="M62 254 H444 M62 254 V16" fill="none" stroke="#0f172a" stroke-width="2"/><polygon points="450,254 442,250 442,258" fill="#0f172a"/><polygon points="62,10 58,18 66,18" fill="#0f172a"/><text x="432" y="288" font-size="11.5" font-weight="600" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N'1 (tours de l'arbre d'entrée)</text><text x="70" y="10" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N'36 (tours de sortie)</text><line x1="62" y1="254" x2="311.3" y2="24" stroke="#2563eb" stroke-width="2.6" stroke-linecap="round"/><text x="309.3" y="16" font-size="13" font-weight="700" text-anchor="middle" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">a</text><line x1="62" y1="254" x2="436" y2="77.4" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><text x="434" y="69.4" font-size="13" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">b</text><line x1="62" y1="254" x2="436" y2="150.5" stroke="#dc2626" stroke-width="2.6" stroke-linecap="round"/><text x="434" y="142.5" font-size="13" font-weight="700" text-anchor="middle" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">c</text><path d="M217.8 254 V180.4 H62" fill="none" stroke="#0f6e56" stroke-width="1.4" stroke-dasharray="5 4"/><circle cx="217.8" cy="180.4" r="4.5" fill="#0f6e56" stroke="#ffffff" stroke-width="1.5"/><text x="217.8" y="248" font-size="11" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2,5</text><text x="68" y="175.4" font-size="11" font-weight="700" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,64</text></svg>
:::

La droite **b** part de l'origine et passe par le point repéré par ses pointillés : son abscisse 2,5 est N'1, son ordonnée 0,64 est N'36.

::: exemple Relever r sur le point du manuel
1. **Lire le point** : N'1 = 2,5 tours à l'entrée, N'36 = 0,64 tour à la sortie.
2. **Calculer r** = N'36 / N'1 = 0,64 / 2,5 = **0,256**. Le quotient est le même en tout point de la droite, puisqu'elle passe par l'origine ; c'est aussi sa pente.
3. **Tracer** : on joint l'origine et le point. Pour N'1 = 5, on lit N'36 = 5 × 0,256 = **1,28**.
4. **Confronter au calcul** : un train dont le calcul donne r = 0,4 × 0,5 = 0,2 prévoit N'36 = 2 pour N'1 = 10. Une lecture à 1,9 donne r = 0,19 : l'écart de 0,1 tour est une graduation du graphique du manuel (axe vertical gradué de 0,1 en 0,1, plus fin que la figure ci-dessus) : il vient de la **lecture**, pas du calcul.

:::

::: piege La droite la plus raide n'est pas la première vitesse
La première vitesse est la plus **démultipliée** : sa sortie tourne le moins, son rapport est le plus petit, sa droite est la **moins raide**. La cinquième vitesse a la droite la plus raide. Et on lit r = N'36 / N'1, jamais l'inverse.
:::

::: propriete Courbe, rapport et comparaison
Pour une vitesse donnée, N'36 = r × N'1 : la courbe est une **droite passant par l'origine, de pente r**. Plus la droite est raide, plus r est grand. Deux méthodes donnent r : la **méthode graphique** (un point lu) et la **méthode analytique** (le calcul sur les dents). Elles concordent **à la précision de lecture près**, soit une graduation (0,1 tour sur le graphique du manuel) ; un écart bien plus grand signale une erreur.
:::

::: verifie
Une droite passe par l'origine et par le point (N'1 = 6 ; N'36 = 0,9). Que valent r, puis N'36 pour N'1 = 10 ?
---
r = 0,9 / 6 = **0,15**, puis N'36 = 10 × 0,15 = **1,5**. On garde le même quotient, puisque la droite passe par l'origine.
:::

## 🛑 Le frein de stationnement à tambour : de la main à la roue

Voiture arrêtée en pente, moteur coupé : tu tires le levier à main et elle ne bouge plus.

Entre ta main et la roue, une chaîne de pièces transmet ton effort jusqu'à un tambour qui doit cesser de tourner. De quelles pièces cette chaîne se compose-t-elle, et dans quel ordre l'effort les traverse-t-il ?

::: definition Le frein à tambour
Un **frein** ralentit ou immobilise une pièce en rotation en transformant son énergie en chaleur par **frottement**. Dans un **frein à tambour**, deux **mâchoires**, portant chacune une **garniture** (le matériau qui frotte), sont appuyées contre la face intérieure d'un **tambour**, pièce liée à la roue.
:::

::: figure Coupe d'un frein à tambour en position libre : les garnitures (en brun) restent à petite distance du tambour. Les noms sont ceux de la maquette ; le dessin est un schéma de principe
<svg viewBox="0 0 460 300"><title>Coupe d'un frein à tambour en position libre, avec ses cinq éléments nommés</title><g transform="translate(215 150)"><circle cx="0" cy="0" r="120" fill="#cbd5e1" stroke="#0f172a" stroke-width="2.2"/><circle cx="0" cy="0" r="102" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><g transform="rotate(0 13.9 78.8)"><path d="M15.6 -88.6 A90 90 0 0 1 15.6 88.6 L12.5 70.9 A72 72 0 0 0 12.5 -70.9 Z" fill="#94a3b8" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><path d="M16.7 -94.5 A96 96 0 0 1 16.7 94.5 L15.6 88.6 A90 90 0 0 0 15.6 -88.6 Z" fill="#a16207" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/></g><g transform="rotate(-0 -13.9 78.8)"><path d="M-15.6 88.6 A90 90 0 0 1 -15.6 -88.6 L-12.5 -70.9 A72 72 0 0 0 -12.5 70.9 Z" fill="#94a3b8" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><path d="M-16.7 94.5 A96 96 0 0 1 -16.7 -94.5 L-15.6 -88.6 A90 90 0 0 0 -15.6 88.6 Z" fill="#a16207" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/></g><rect x="-24" y="84" width="48" height="9" fill="#475569" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><circle cx="13.9" cy="78.8" r="4" fill="#0f172a"/><circle cx="-13.9" cy="78.8" r="4" fill="#0f172a"/><polyline points="-49.3,63 -43.1,63 -40,68 -33.9,58 -27.7,68 -21.5,58 -15.4,68 -9.2,58 -3.1,68 3.1,58 9.2,68 15.4,58 21.5,68 27.7,58 33.9,68 40,58 43.1,63 49.3,63" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><g transform="rotate(0 0 -74.8)"><ellipse cx="0" cy="-74.8" rx="13.2" ry="25" fill="#fde68a" stroke="#0f172a" stroke-width="1.8"/></g><circle cx="0" cy="-74.8" r="3" fill="#0f172a"/><circle cx="0" cy="0" r="4" fill="#0f172a"/></g><line x1="300" y1="78.7" x2="351" y2="36" stroke="#475569" stroke-width="1.3"/><circle cx="300" cy="78.7" r="2.6" fill="#475569"/><text x="355" y="40" font-size="13" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Tambour</text><line x1="306" y1="169.3" x2="351" y2="146" stroke="#475569" stroke-width="1.3"/><circle cx="306" cy="169.3" r="2.6" fill="#475569"/><text x="355" y="150" font-size="13" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Garniture</text><line x1="267.1" y1="212" x2="351" y2="248" stroke="#475569" stroke-width="1.3"/><circle cx="267.1" cy="212" r="2.6" fill="#475569"/><text x="355" y="252" font-size="13" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Mâchoire</text><line x1="215" y1="75.2" x2="76" y2="20" stroke="#475569" stroke-width="1.3"/><circle cx="215" cy="75.2" r="2.6" fill="#475569"/><text x="20" y="24" font-size="13" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Came</text><line x1="215" y1="213" x2="76" y2="272" stroke="#475569" stroke-width="1.3"/><circle cx="215" cy="213" r="2.6" fill="#475569"/><text x="20" y="276" font-size="13" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Ressort</text></svg>
:::

Le tambour est la grande couronne grise, les deux mâchoires sont à l'intérieur, la came est entre leurs extrémités du haut.

::: exemple Compléter le graphe des éléments du freinage (principe)
Le manuel nomme : levier, tirant, biellette, tige réglable, bras, came, mâchoires, tambour.
1. Le **levier** reçoit l'effort de la main : c'est le **départ**.
2. Une **tringlerie** (tirant, biellette, tige réglable) transmet l'effort de proche en proche. L'ordre exact de ces trois pièces se vérifie sur la maquette.
3. Le **bras** fait tourner la **came**.
4. La **came** écarte les **mâchoires**.
5. Les **mâchoires**, par leurs garnitures, frottent sur le **tambour** : c'est lui le dernier maillon, la pièce qu'on freine.

:::

::: piege La garniture est sur la mâchoire, pas sur le tambour
On colle parfois la garniture sur le tambour. C'est l'inverse : la garniture, matériau d'usure, est fixée sur la **mâchoire** ; le tambour est la surface **contre** laquelle elle frotte.
:::

::: verifie
Quelle pièce transmet l'effort de la came au tambour ?
---
Les **mâchoires**, par leurs garnitures : la came les écarte, et ce sont elles qui frottent sur le tambour.
:::

## ↔️ Le frein en action : commande, action radiale, ressort de rappel

Relâché, le levier laisse la roue libre ; tiré, il la bloque.

Dans le tambour, que bouge-t-il vraiment, dans quelle direction, et qu'est-ce qui remet tout en place quand on relâche ?

::: definition Commande et mode d'action
La **commande** est la manière dont l'effort est fourni. Ici, la commande est **manuelle** : la main tire un levier, et une tringlerie transmet l'effort **mécaniquement**.

Le **mode d'action** est la direction dans laquelle les surfaces de friction sont pressées. L'action est **radiale** quand l'effort de serrage est dirigé selon un rayon, ici vers l'extérieur contre la paroi du tambour ; elle est **axiale** quand il est parallèle à l'axe de rotation (par exemple un frein à disque, cité comme repère).
:::

::: figure À gauche, levier relâché : le ressort a rappelé les mâchoires, la came est au repos et les garnitures sont décollées. À droite, levier tiré : la came a tourné et écarté les mâchoires contre le tambour. Schéma de principe
<svg viewBox="0 0 460 236"><title>Le frein à tambour libre, puis freiné : les mâchoires s'écartent contre le tambour</title><g transform="translate(115 105) scale(0.82)"><circle cx="0" cy="0" r="120" fill="#cbd5e1" stroke="#0f172a" stroke-width="2.2"/><circle cx="0" cy="0" r="102" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><g transform="rotate(0 13.9 78.8)"><path d="M15.6 -88.6 A90 90 0 0 1 15.6 88.6 L12.5 70.9 A72 72 0 0 0 12.5 -70.9 Z" fill="#94a3b8" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><path d="M16.7 -94.5 A96 96 0 0 1 16.7 94.5 L15.6 88.6 A90 90 0 0 0 15.6 -88.6 Z" fill="#a16207" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/></g><g transform="rotate(-0 -13.9 78.8)"><path d="M-15.6 88.6 A90 90 0 0 1 -15.6 -88.6 L-12.5 -70.9 A72 72 0 0 0 -12.5 70.9 Z" fill="#94a3b8" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><path d="M-16.7 94.5 A96 96 0 0 1 -16.7 -94.5 L-15.6 -88.6 A90 90 0 0 0 -15.6 88.6 Z" fill="#a16207" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/></g><rect x="-24" y="84" width="48" height="9" fill="#475569" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><circle cx="13.9" cy="78.8" r="4" fill="#0f172a"/><circle cx="-13.9" cy="78.8" r="4" fill="#0f172a"/><polyline points="-49.3,63 -43.1,63 -40,68 -33.9,58 -27.7,68 -21.5,58 -15.4,68 -9.2,58 -3.1,68 3.1,58 9.2,68 15.4,58 21.5,68 27.7,58 33.9,68 40,58 43.1,63 49.3,63" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><g transform="rotate(0 0 -74.8)"><ellipse cx="0" cy="-74.8" rx="13.2" ry="25" fill="#fde68a" stroke="#0f172a" stroke-width="1.8"/></g><circle cx="0" cy="-74.8" r="3" fill="#0f172a"/><circle cx="0" cy="0" r="4" fill="#0f172a"/></g><text x="115" y="212" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Levier relâché</text><text x="115" y="227" font-size="11" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">mâchoires rappelées</text><g transform="translate(345 105) scale(0.82)"><circle cx="0" cy="0" r="120" fill="#cbd5e1" stroke="#0f172a" stroke-width="2.2"/><circle cx="0" cy="0" r="102" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><g transform="rotate(4.3 13.9 78.8)"><path d="M15.6 -88.6 A90 90 0 0 1 15.6 88.6 L12.5 70.9 A72 72 0 0 0 12.5 -70.9 Z" fill="#94a3b8" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><path d="M16.7 -94.5 A96 96 0 0 1 16.7 94.5 L15.6 88.6 A90 90 0 0 0 15.6 -88.6 Z" fill="#a16207" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/></g><g transform="rotate(-4.3 -13.9 78.8)"><path d="M-15.6 88.6 A90 90 0 0 1 -15.6 -88.6 L-12.5 -70.9 A72 72 0 0 0 -12.5 70.9 Z" fill="#94a3b8" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><path d="M-16.7 94.5 A96 96 0 0 1 -16.7 -94.5 L-15.6 -88.6 A90 90 0 0 0 -15.6 88.6 Z" fill="#a16207" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/></g><rect x="-24" y="84" width="48" height="9" fill="#475569" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><circle cx="13.9" cy="78.8" r="4" fill="#0f172a"/><circle cx="-13.9" cy="78.8" r="4" fill="#0f172a"/><polyline points="-50.3,65.7 -44,65.7 -40.9,70.7 -34.6,60.7 -28.3,70.7 -22,60.7 -15.7,70.7 -9.4,60.7 -3.1,70.7 3.1,60.7 9.4,70.7 15.7,60.7 22,70.7 28.3,60.7 34.6,70.7 40.9,60.7 44,65.7 50.3,65.7" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><g transform="rotate(79.8 0 -74.8)"><ellipse cx="0" cy="-74.8" rx="13.2" ry="25" fill="#fde68a" stroke="#0f172a" stroke-width="1.8"/></g><circle cx="0" cy="-74.8" r="3" fill="#0f172a"/><circle cx="0" cy="0" r="4" fill="#0f172a"/></g><text x="345" y="212" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Levier tiré</text><text x="345" y="227" font-size="11" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">mâchoires écartées</text></svg>
:::

| Levier | Mâchoires | Tambour |
| --- | --- | --- |
| Non actionné | rapprochées par le ressort, garnitures décollées | **tourne** avec la roue |
| Actionné | écartées par la came, garnitures contre le tambour | **fixe**, immobilisé |

::: exemple Un serrage, puis un desserrage
1. **On tire le levier** : la tringlerie, le bras et la came transmettent l'effort ; la came tourne.
2. **La came écarte** le haut des mâchoires : elles pivotent vers l'extérieur et leurs garnitures touchent le tambour. L'effort est **radial**.
3. **Le frottement immobilise** le tambour : de tournant, il devient fixe, et la roue ne tourne plus. Le **ressort**, au passage, est tendu.
4. **On relâche** : la tringlerie, le bras et la came ne poussent plus ; le **ressort rappelle** les mâchoires vers le centre, et la came revient avec elles ; les garnitures se décollent et le tambour est de nouveau libre.

:::

::: piege Le ressort ne freine pas
Le ressort ne participe pas au serrage : on tire **contre** lui. Son rôle est d'assurer le **rappel** : sans lui, les mâchoires resteraient en frottement sur le tambour après le desserrage, et le frein chaufferait en roulant.
:::

::: verifie
Levier relâché, le tambour est-il fixe ou tournant ? Et qui ramène les mâchoires à leur place ?
---
Le tambour **tourne** avec la roue, puisque les garnitures sont décollées. C'est le **ressort** qui rappelle les mâchoires quand on relâche le levier.
:::

## 🧭 La méthode qui reste : six marches

Devant une boîte ou un frein inconnu, tu reprends toujours cet ordre :

1. **Situer** : la boîte adapte le couple et la vitesse, entre l'embrayage et le pont ; chaque pièce n'a qu'un mouvement permis (pivot, glissière) et une pièce qui le provoque.
2. **Calculer** : écrire les paires dans l'ordre, multiplier Z menante / Z menée, puis N sortie = N entrée × r.
3. **Compter** les engrènements extérieurs : pair, le sens est conservé ; impair, il est inversé.
4. **Suivre la commande** : levier, fourchette, baladeur, crabotage ; au point mort, r = 0.
5. **Classer** les roues (droite, hélicoïdale, intérieure, conique) et vérifier les conditions d'engrènement.
6. **Lire** la courbe : une droite de pente r. Pour le frein : levier, tringlerie, bras, came, mâchoires, tambour, avec action **radiale** et ressort de **rappel**.

::: retenir
Une boîte **adapte** le couple et la vitesse par un **rapport r = Z menante / Z menée**, multiplié d'étage en étage ; chaque engrènement extérieur **inverse** le sens ; le baladeur et la fourchette changent le chemin (par **crabotage** dans le cas étudié) ; un frein à tambour presse ses mâchoires **radialement**, et son **ressort** les rappelle.
:::

> 🏆 La boîte est maîtrisée : tu sais la calculer, la commander et l'arrêter. La suite du thème t'attend, avec d'autres façons de transmettre une rotation.
