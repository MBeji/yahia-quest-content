# ⚙️ Faire parler le plan — la perceuse sensitive

> 💡 «Un dessin d'ensemble ne se regarde pas : il se décode. Vingt-cinq repères, et toute la machine se met à parler.»

Au chapitre précédent, tu ouvrais une machine par ses **chaînes fonctionnelles**. Il te manquait le document que le technicien a réellement entre les mains : le **dessin d'ensemble**. Ce chapitre t'apprend à le lire, puis à en tirer les trois documents qui font vivre un mécanisme — le **graphe de montage et de démontage** pour l'entretenir, la **cotation fonctionnelle** pour le fabriquer juste, le **dessin de définition** pour usiner chaque pièce. Le support est une **perceuse sensitive**, et son plan ne cache rien : tout est là, il faut savoir regarder.

## 🗺️ Lire un dessin d'ensemble : deux étapes, jamais une seule

Un dessin d'ensemble est destiné à mettre en évidence **comment des pièces sont assemblées les unes avec les autres**, afin de comprendre le fonctionnement d'un système. On ne le déchiffre pas repère par repère, au hasard.

::: definition Les deux étapes de la lecture
La lecture d'un dessin d'ensemble se base sur **deux étapes** :

- **Lecture synthétique** : observation globale des **vues** et de leurs **correspondances**, et acquisition d'une **idée sur la nomenclature**.
- **Lecture analytique**, qui se conduit sur trois plans :
  - **analyse fonctionnelle** : identifier la **matière d'œuvre entrante**, la **matière d'œuvre sortante** et la **fonction globale** ;
  - **analyse du fonctionnement** : la **chaîne cinématique**, les **liaisons**, les **composants** ;
  - **analyse des solutions constructives** : se faire une idée de l'**approche techno-économique** des choix du constructeur.
:::

> 🗡️ L'ordre n'est pas décoratif. Qui plonge d'emblée sur un repère isolé se noie ; qui balaie d'abord l'ensemble sait ensuite **où** regarder et **quoi** y chercher.

## 🏭 Le support : la perceuse sensitive

La perceuse sensitive est une **machine-outil** servant à réaliser des opérations de **perçage**. Elle se compose essentiellement d'un **moteur électrique**, d'un **système de transmission de mouvement**, d'une **colonne**, d'une **broche** et d'un **mandrin** portant l'outil, et d'un **étau** pour le maintien de la pièce.

Applique-lui tout de suite l'analyse fonctionnelle : sa **fonction globale** est de **percer une pièce** ; la **matière d'œuvre entrante** est la **pièce non percée**, la **matière d'œuvre sortante** la **même pièce, percée**. Ne confonds jamais la matière d'œuvre, que le système *transforme*, avec l'énergie, qu'il *consomme*.

Le dessin d'ensemble étudié ici représente **partiellement** la partie de **transmission de puissance** de la perceuse, ainsi que le **mécanisme de commande de déplacement de la broche**. Son cartouche annonce l'**échelle 3:5** : 3 mm sur le papier pour 5 mm sur la machine, donc une **réduction** — une longueur réelle se multiplie par 3 ÷ 5 pour être dessinée, et les petits détails sont repris à part à l'**échelle 1:1**, en vraie grandeur. Sa nomenclature compte **25 repères** : c'est ton dictionnaire, garde-la sous les yeux.

| Rep. | Nbr. | Désignation                                          | Matière       |
| ---- | ---- | ---------------------------------------------------- | ------------- |
| 1    | 2    | Roulement à une rangée de billes à contact radial    | 100 Cr 6      |
| 2    | 1    | Bague entretoise                                     | C60           |
| 3    | 1    | Bâti                                                 | EN GJL 250    |
| 4    | 1    | Fourreau (porte la crémaillère)                      | C35           |
| 5    | 1    | Broche                                               | C35           |
| 6    | 1    | Anneau élastique pour arbre                          |               |
| 7    | 1    | Rondelle plate                                       |               |
| 8    | 2    | Roulement à une rangée de billes à contact radial    | 100 Cr 6      |
| 9    | 1    | Bague entretoise                                     | C60           |
| 10   | 1    | Anneau élastique pour alésage                        |               |
| 11   | 1    | Moyeu                                                | 36 Ni Cr Mo16 |
| 12   | 1    | Poulie étagée                                        | Al Si 10 Mg   |
| 13   | 1    | Pignon                                               | C35           |
| 14   | 1    | Anneau élastique pour arbre                          |               |
| 15   | 1    | Boîtier                                              | EN GJL 200    |
| 16   | 4    | Vis à tête cylindrique à six pans creux              |               |
| 17   | 1    | Écrou spécial                                        |               |
| 18   | 1    | Écrou-frein                                          |               |
| 19   | 1    | Vis sans tête à six pans creux à téton long          |               |
| 20   | 1    | Anneau élastique pour arbre                          |               |
| 21   | 1    | Couvercle                                            | C60           |
| 22   | 1    | Ressort spiral                                       | 60 Si Cr 7    |
| 23   | 2    | Écrou hexagonal                                      |               |
| 24   | 3    | Bras de commande                                     | S235          |
| 25   | 1    | Coussinet                                            | Cu Sn 8       |

Deux mouvements cohabitent, et il ne faut jamais les confondre : l'outil **tourne**, et l'outil **descend**.

::: figure Deux chaînes, deux mouvements : en haut la puissance descend jusqu'au foret, en bas la commande manuelle fait plonger la broche — et le ressort spiral (22) la ramène.
<svg viewBox="0 0 460 212">
<g font-size="10" font-weight="700" fill="#0f6e56"><text x="6" y="28">Transmission de puissance : l'outil tourne</text><text x="6" y="130">Commande de descente : l'outil avance</text></g>
<g fill="#0f6e56" opacity="0.12"><rect x="6" y="44" width="74" height="38" rx="5"/><rect x="96" y="44" width="92" height="38" rx="5"/><rect x="204" y="44" width="74" height="38" rx="5"/><rect x="294" y="44" width="74" height="38" rx="5"/><rect x="384" y="44" width="70" height="38" rx="5"/><rect x="6" y="146" width="98" height="38" rx="5"/><rect x="116" y="146" width="74" height="38" rx="5"/><rect x="206" y="146" width="104" height="38" rx="5"/><rect x="326" y="146" width="112" height="38" rx="5"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><rect x="6" y="44" width="74" height="38" rx="5"/><rect x="96" y="44" width="92" height="38" rx="5"/><rect x="204" y="44" width="74" height="38" rx="5"/><rect x="294" y="44" width="74" height="38" rx="5"/><rect x="384" y="44" width="70" height="38" rx="5"/><rect x="6" y="146" width="98" height="38" rx="5"/><rect x="116" y="146" width="74" height="38" rx="5"/><rect x="206" y="146" width="104" height="38" rx="5"/><rect x="326" y="146" width="112" height="38" rx="5"/><path d="M80 63 H90"/><path d="M188 63 H198"/><path d="M278 63 H288"/><path d="M368 63 H378"/><path d="M104 165 H106"/><path d="M190 165 H196"/><path d="M310 165 H316"/><path d="M382 184 V198 H258 V186"/></g>
<g fill="#0f172a"><polygon points="96,63 86,58 86,68"/><polygon points="204,63 194,58 194,68"/><polygon points="294,63 284,58 284,68"/><polygon points="384,63 374,58 374,68"/><polygon points="116,165 106,160 106,170"/><polygon points="206,165 196,160 196,170"/><polygon points="326,165 316,160 316,170"/><polygon points="258,184 253,194 263,194"/></g>
<g font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a"><text x="43" y="60">Moteur</text><text x="43" y="73">électrique</text><text x="142" y="60">Poulie étagée</text><text x="142" y="73">(12) + courroie</text><text x="241" y="67">Moyeu (11)</text><text x="331" y="67">Broche (5)</text><text x="419" y="60">Mandrin,</text><text x="419" y="73">foret</text><text x="55" y="162">Bras de</text><text x="55" y="175">commande (24)</text><text x="153" y="169">Pignon (13)</text><text x="258" y="162">Crémaillère du</text><text x="258" y="175">fourreau (4)</text><text x="382" y="162">Translation de</text><text x="382" y="175">la broche (5)</text></g>
<text x="320" y="209" font-size="10" font-weight="700" text-anchor="middle" fill="#0f6e56">ressort spiral (22)</text>
</svg>
:::

- **L'outil tourne** : le moteur entraîne par **courroie** la **poulie étagée (12)** ; la poulie est encastrée sur le **moyeu (11)**, qui entraîne la **broche (5)**, donc le mandrin et le foret. La poulie est *étagée* pour offrir plusieurs vitesses de rotation : on déplace la courroie d'un gradin à l'autre.
- **L'outil descend** : l'opérateur tire un **bras de commande (24)** ; le bras fait tourner le **pignon (13)**, qui engrène sur la **crémaillère** taillée sur le **fourreau (4)** ; le fourreau descend et emmène la broche avec lui. Dès qu'on lâche le bras, le **ressort spiral (22)**, logé dans le **couvercle (21)**, se détend et **ramène l'ensemble en position haute**.

## 🔗 Du dessin aux liaisons

L'analyse du fonctionnement, c'est traduire des traits en **liaisons**. Trois solutions constructives portent tout le mécanisme.

**1. Guider en rotation.** Deux **roulements à billes** montés de part et d'autre d'une **bague entretoise**, qui fixe leur écartement : les roulements (1) et la bague (2) pour la broche, les roulements (8) et la bague (9) pour le moyeu. Là où l'effort est faible, un simple **coussinet (25)** en bronze Cu Sn 8 suffit — pièce d'usure, peu coûteuse, **interchangeable**, qui s'use à la place de l'arbre et du logement.

**2. Guider en translation *et* entraîner en rotation d'un seul coup : le carré.** Le moyeu (11) tourne, mais la broche (5) doit aussi **coulisser** dans le moyeu pendant la descente. Un tronçon **carré** résout les deux problèmes à la fois.

::: figure Coupe transversale du guidage : le profil carré empêche la broche (5) de tourner dans le moyeu (11) hachuré, mais la laisse coulisser librement le long de l'axe.
<svg viewBox="0 0 220 200">
<path d="M110 22 A78 78 0 1 1 109.9 22 Z M68 58 H152 V142 H68 Z" fill="#0f6e56" opacity="0.10" fill-rule="evenodd"/>
<path d="M36.72 73.28 L83.28 26.72 M32.92 88.08 L98.08 22.92 M32 100 L68 64 M74 58 L110 22 M32.69 110.3 L68 75 M85 58 L120.3 22.69 M34.48 119.5 L68 86 M96 58 L129.5 24.48 M37.14 127.9 L68 97 M107 58 L137.9 27.14 M40.53 135.5 L68 108 M118 58 L145.5 30.53 M44.56 142.4 L68 119 M129 58 L152.4 34.56 M49.17 148.8 L68 130 M140 58 L158.8 39.17 M54.35 154.7 L68 141 M151 58 L164.7 44.35 M60.07 159.9 L78 142 M152 68 L169.9 50.07 M66.35 164.6 L89 142 M152 79 L174.6 56.35 M73.22 168.8 L100 142 M152 90 L178.8 63.22 M80.71 172.3 L111 142 M152 101 L182.3 70.71 M88.91 175.1 L122 142 M152 112 L185.1 78.91 M97.94 177.1 L133 142 M152 123 L187.1 87.94 M108 178 L144 142 M152 134 L188 98.03 M119.6 177.4 L187.4 109.6 M133.7 174.3 L184.3 123.7 M156 163 L173 146" fill="none" stroke="#0f172a" stroke-width="0.9"/>
<rect x="68" y="58" width="84" height="84" fill="#bfdbfe"/>
<circle cx="110" cy="100" r="78" fill="none" stroke="#0f172a" stroke-width="2"/>
<rect x="68" y="58" width="84" height="84" fill="none" stroke="#0f172a" stroke-width="2"/>
<g font-size="15" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="110" y="45">11</text><text x="110" y="106">5</text></g>
</svg>
:::

> 🗡️ Toute forme **non circulaire** — carré, hexagone, cannelures, clavette glissante — réalise le même exploit : elle **arrête la rotation** relative tout en **laissant la translation** libre. Le carré est simplement le moins cher à usiner.

**3. Arrêter une rotation parasite.** Le **fourreau (4)** est cylindrique : dans son logement du **bâti (3)**, il pourrait à la fois coulisser **et** tourner — c'est une liaison **pivot glissant**, à deux degrés de liberté. Or s'il tournait, la crémaillère se dégagerait du pignon. On lui ajoute donc une **vis sans tête à téton long (19)**, dont le téton s'engage dans une **rainure** usinée le long du fourreau, et qu'un **écrou-frein (18)** empêche de se desserrer sous les vibrations. La rotation disparaît : la liaison devient une **glissière**, à un seul degré de liberté.

::: figure Sans la vis (19), le fourreau pourrait tourner dans le bâti : ce serait un pivot glissant. Le téton engagé dans la rainure supprime la rotation et ne laisse que la translation.
<svg viewBox="0 0 360 232">
<rect x="36" y="106" width="290" height="68" fill="#0f6e56" opacity="0.12"/>
<path d="M66 106 L73.5 96 L81 106 L88.5 96 L96 106 L103.5 96 L111 106 L118.5 96 L126 106 L133.5 96 L141 106 L148.5 96 L156 106 L163.5 96 L171 106 L178.5 96 L186 106" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M36 106 H66 M186 106 H326 M36 106 V174 M326 106 V174 M36 174 H244 M268 174 H326" fill="none" stroke="#0f172a" stroke-width="2"/>
<rect x="16" y="174" width="324" height="28" fill="#0f6e56" opacity="0.10"/>
<path d="M16 175 L17 174 M16 186 L28 174 M16 197 L39 174 M22 202 L50 174 M33 202 L61 174 M44 202 L72 174 M55 202 L83 174 M66 202 L94 174 M77 202 L105 174 M88 202 L116 174 M99 202 L127 174 M110 202 L138 174 M121 202 L149 174 M132 202 L160 174 M143 202 L171 174 M154 202 L182 174 M165 202 L193 174 M176 202 L204 174 M187 202 L215 174 M198 202 L226 174 M209 202 L237 174 M220 202 L248 174 M231 202 L259 174 M242 202 L270 174 M253 202 L281 174 M264 202 L292 174 M275 202 L303 174 M286 202 L314 174 M297 202 L325 174 M308 202 L336 174 M319 202 L340 181 M330 202 L340 192" fill="none" stroke="#0f172a" stroke-width="0.9"/>
<rect x="16" y="174" width="324" height="28" fill="none" stroke="#0f172a" stroke-width="2"/>
<circle cx="126" cy="58" r="38" fill="#fde68a" stroke="#0f172a" stroke-width="2"/>
<g fill="none" stroke="#0f172a" stroke-width="1.4"><path d="M126 20 V30 M164 58 H154 M126 96 V86 M88 58 H98 M153 31 L146 38 M153 85 L146 78 M99 85 L106 78 M99 31 L106 38"/></g>
<path d="M126 58 L58 22" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
<circle cx="54" cy="20" r="7" fill="#0f172a"/>
<path d="M244 174 V158 H268 V174" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<rect x="248" y="160" width="16" height="42" fill="#fde68a" stroke="#0f172a" stroke-width="2"/>
<rect x="240" y="202" width="32" height="14" fill="#0f6e56" opacity="0.2"/>
<rect x="240" y="202" width="32" height="14" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M240 90 H330" fill="none" stroke="#0f6e56" stroke-width="2"/>
<g fill="#0f6e56"><polygon points="234,90 244,85 244,95"/><polygon points="336,90 326,85 326,95"/></g>
<g fill="none" stroke="#0f172a" stroke-width="1"><path d="M292 186 H266"/><path d="M292 213 H272"/></g>
<g font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="300" y="146">4</text><text x="52" y="196">3</text><text x="142" y="82">13</text><text x="70" y="16">24</text><text x="296" y="190">19</text><text x="296" y="217">18</text></g>
</svg>
:::

**4. Encastrer : par obstacle ou par adhérence ?**

::: definition Les deux façons d'encastrer
- **Par obstacle** : une **forme** s'oppose au mouvement — clavette, goupille, cannelures, ergot, téton.
- **Par adhérence** : un **serrage** crée entre les surfaces un frottement suffisant — vis de pression, écrou serrant contre un épaulement, emmanchement conique, frettage.
:::

Sur la perceuse, la nomenclature ne comporte **ni clavette, ni goupille, ni cannelure**. L'encastrement entre le **moyeu (11)** et la **poulie étagée (12)** ne peut donc pas être obtenu par obstacle : c'est l'**écrou spécial (17)** qui plaque la poulie contre l'épaulement du moyeu, et le couple passe par le **frottement** ainsi créé. Cet encastrement est réalisé **par adhérence**.

> ⚠️ Le piège classique : croire qu'une vis fait toujours un obstacle. Une vis **serre**, donc elle crée de l'**adhérence** ; il n'y a obstacle que si son corps est **ajusté** dans un perçage, ou si un **téton** entre dans une rainure — ce qui est justement le rôle de (19), et pas celui de l'écrou (17).

## 🧰 Le graphe de montage et de démontage

::: definition À quoi servent ces graphes
Le graphe de montage et celui de démontage sont des outils donnant un **ordre chronologique** pour :

- le **montage** d'un ensemble neuf ;
- le **démontage** et le **remontage** d'un mécanisme dans les interventions de **maintenance**.
:::

Mise en situation : dans le cadre d'une **maintenance corrective**, l'équipe d'entretien doit changer le **ressort (22) défectueux**. Comment procéder ? On trace d'abord le **graphe de démontage**, dit **filogramme** : une colonne verticale portant le **repère d'ordre**, sur laquelle se détachent les pièces déposées, dans l'ordre, avec l'outillage nécessaire.

::: figure Le filogramme se lit de haut en bas : chaque cran du repère d'ordre dépose une pièce, jusqu'à isoler le ressort (22) à remplacer. Ce qui n'a pas été touché forme le sous-ensemble restant.
<svg viewBox="0 0 420 258">
<g font-size="10" font-weight="700" fill="#0f6e56"><text x="6" y="14">Repère</text><text x="6" y="27">d'ordre</text><text x="290" y="20">Outillage</text></g>
<rect x="86" y="8" width="128" height="28" rx="4" fill="#0f6e56" opacity="0.16" stroke="#0f172a" stroke-width="2"/>
<path d="M150 36 V214" fill="none" stroke="#0f172a" stroke-width="2"/>
<g fill="none" stroke="#0f172a" stroke-width="2"><path d="M150 62 H196"/><path d="M150 102 H196"/><path d="M150 142 H196"/><path d="M150 182 H216"/></g>
<g fill="#0f172a"><polygon points="206,62 196,57 196,67"/><polygon points="206,102 196,97 196,107"/><polygon points="206,142 196,137 196,147"/><polygon points="226,182 216,177 216,187"/></g>
<g fill="#bfdbfe" stroke="#0f172a" stroke-width="2"><rect x="206" y="48" width="48" height="28" rx="4"/><rect x="206" y="88" width="48" height="28" rx="4"/><rect x="206" y="128" width="64" height="28" rx="4"/><rect x="226" y="168" width="48" height="28" rx="4"/></g>
<rect x="76" y="214" width="148" height="30" rx="4" fill="#0f6e56" opacity="0.16" stroke="#0f172a" stroke-width="2"/>
<g font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a"><text x="150" y="27">Perceuse sensitive</text><text x="230" y="67">23'</text><text x="230" y="107">23</text><text x="238" y="147">21 + 22</text><text x="250" y="187">22</text><text x="150" y="233">Sous-ensemble restant</text></g>
<g font-size="11" font-weight="700" text-anchor="end" fill="#0f6e56"><text x="142" y="58">1</text><text x="142" y="98">2</text><text x="142" y="138">3</text><text x="142" y="178">3.1</text></g>
<g font-size="9" fill="#0f172a"><text x="290" y="67">Clé plate de 8 (deux clés)</text><text x="290" y="107">Clé plate de 8</text><text x="290" y="147">Manuelle</text><text x="290" y="187">Extracteur de ressort</text></g>
</svg>
:::

Lis-le : on dépose d'abord le **contre-écrou (23')**, puis l'**écrou (23)**, puis à la main le **couvercle (21) avec le ressort (22)** ; on **extrait** enfin le ressort du couvercle. Le reste de la machine n'a pas été touché : c'est le **sous-ensemble restant**.

> ⚠️ « Prévoir deux clés » n'est pas un luxe. Un **contre-écrou** est bloqué contre l'écrou qu'il freine : il faut **maintenir** l'un pendant qu'on **desserre** l'autre, sinon les deux tournent ensemble sans se séparer.

::: propriete La règle d'or du remontage
Le **montage reprend le démontage à l'envers** : la dernière pièce déposée est la première remontée. Le graphe de montage se dessine en **râteau** — une ligne de progression horizontale sur laquelle chaque composant vient se greffer dans l'ordre.
:::

::: figure Le râteau de montage se lit de gauche à droite : le ressort (22) entre d'abord dans le couvercle (21) pour former un sous-ensemble, qui se pose ensuite sur la machine avant l'écrou (23) puis le contre-écrou (23').
<svg viewBox="0 0 420 180">
<text x="6" y="18" font-size="10" font-weight="700" fill="#0f6e56">Ordre de montage</text>
<path d="M96 140 H340" fill="none" stroke="#0f172a" stroke-width="2.5"/>
<polygon points="352,140 338,134 338,146" fill="#0f172a"/>
<g fill="none" stroke="#0f172a" stroke-width="2"><path d="M144 54 V66 H196 V54"/><path d="M170 66 V76"/><path d="M170 102 V140"/><path d="M252 102 V140"/><path d="M314 102 V140"/></g>
<g fill="#0f172a"><polygon points="170,140 165,130 175,130"/><polygon points="252,140 247,130 257,130"/><polygon points="314,140 309,130 319,130"/></g>
<g fill="#bfdbfe" stroke="#0f172a" stroke-width="2"><rect x="124" y="28" width="40" height="26" rx="4"/><rect x="176" y="28" width="40" height="26" rx="4"/><rect x="136" y="76" width="68" height="26" rx="4"/><rect x="232" y="76" width="40" height="26" rx="4"/><rect x="292" y="76" width="44" height="26" rx="4"/></g>
<g fill="#0f6e56" opacity="0.16"><rect x="8" y="122" width="88" height="36" rx="4"/><rect x="352" y="122" width="64" height="36" rx="4"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><rect x="8" y="122" width="88" height="36" rx="4"/><rect x="352" y="122" width="64" height="36" rx="4"/></g>
<g font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a"><text x="144" y="46">22</text><text x="196" y="46">21</text><text x="170" y="94">21 + 22</text><text x="252" y="94">23</text><text x="314" y="94">23'</text></g>
<g font-size="9" font-weight="700" text-anchor="middle" fill="#0f172a"><text x="52" y="138">Sous-ensemble</text><text x="52" y="151">restant</text><text x="384" y="138">Ensemble</text><text x="384" y="151">perceuse</text></g>
</svg>
:::

## 📏 La cotation fonctionnelle

::: definition Le but de la cotation fonctionnelle
Un mécanisme est constitué de nombreuses pièces. Pour qu'il puisse fonctionner correctement, certaines **conditions** doivent être respectées : **jeux, dépassements, serrages**. La cotation fonctionnelle a pour but :

- de définir les **cotes nominales** et les **IT** (intervalles de tolérance) de chaque pièce afin que ces conditions soient respectées — et donc d'assurer l'**interchangeabilité** des pièces d'un mécanisme ;
- de **minimiser les coûts de fabrication** en donnant les **plus larges tolérances possibles** aux cotes à fabriquer.
:::

Une condition ne tient jamais à une seule pièce : elle se **ferme** sur une suite de cotes, la **chaîne de cotes**. On part d'une face de la condition et on revient à l'autre en passant par une seule cote par pièce.

::: figure La condition J se referme sur la chaîne A, B, C : J = A − B − C. Le jeu est dessiné volontairement exagéré — sinon on ne le verrait pas.
<svg viewBox="0 0 400 210">
<g fill="#0f6e56" opacity="0.12"><rect x="30" y="60" width="28" height="72"/><rect x="312" y="60" width="28" height="72"/><rect x="30" y="132" width="310" height="20"/></g>
<path d="M30 66 L36 60 M30 75 L45 60 M30 84 L54 60 M30 93 L58 65 M30 102 L58 74 M30 111 L58 83 M30 120 L58 92 M30 129 L58 101 M36 132 L58 110 M45 132 L58 119 M54 132 L58 128 M312 63 L315 60 M312 72 L324 60 M312 81 L333 60 M312 90 L340 62 M312 99 L340 71 M312 108 L340 80 M312 117 L340 89 M312 126 L340 98 M315 132 L340 107 M324 132 L340 116 M333 132 L340 125 M30 140 L38 132 M30 149 L47 132 M36 152 L56 132 M45 152 L65 132 M54 152 L74 132 M63 152 L83 132 M72 152 L92 132 M81 152 L101 132 M90 152 L110 132 M99 152 L119 132 M108 152 L128 132 M117 152 L137 132 M126 152 L146 132 M135 152 L155 132 M144 152 L164 132 M153 152 L173 132 M162 152 L182 132 M171 152 L191 132 M180 152 L200 132 M189 152 L209 132 M198 152 L218 132 M207 152 L227 132 M216 152 L236 132 M225 152 L245 132 M234 152 L254 132 M243 152 L263 132 M252 152 L272 132 M261 152 L281 132 M270 152 L290 132 M279 152 L299 132 M288 152 L308 132 M297 152 L317 132 M306 152 L326 132 M315 152 L335 132 M324 152 L340 136 M333 152 L340 145" fill="none" stroke="#0f172a" stroke-width="0.9"/>
<path d="M30 60 H58 V132 H312 V60 H340 V152 H30 Z" fill="none" stroke="#0f172a" stroke-width="2"/>
<rect x="58" y="80" width="140" height="52" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/>
<rect x="198" y="80" width="99" height="52" fill="#fde68a" stroke="#0f172a" stroke-width="2"/>
<g fill="none" stroke="#0f172a" stroke-width="1"><path d="M58 154 V200 M198 154 V200 M297 154 V200 M312 154 V182"/><path d="M297 74 V86 M312 74 V86"/></g>
<g fill="none" stroke="#0f172a" stroke-width="1.2"><path d="M64 176 H306" /><path d="M64 196 H192"/><path d="M204 196 H291"/></g>
<g fill="#0f172a"><polygon points="58,176 68,172 68,180"/><polygon points="312,176 302,172 302,180"/><polygon points="58,196 68,192 68,200"/><polygon points="198,196 188,192 188,200"/><polygon points="198,196 208,192 208,200"/><polygon points="297,196 287,192 287,200"/></g>
<path d="M304.5 78 V64" fill="none" stroke="#0f172a" stroke-width="1"/>
<g font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="185" y="172">A = 60 ± 0,05</text><text x="120" y="192">B = 35 ± 0,03</text><text x="248" y="192">C = 24,80 ± 0,02</text><text x="308" y="60">J</text><text x="128" y="112">B</text><text x="248" y="112">C</text></g>
</svg>
:::

::: propriete Les deux règles de la chaîne de cotes
$$ J maxi = Σ(cotes +) maxi − Σ(cotes −) mini $$
$$ IT(J) = IT(A) + IT(B) + IT(C) + … $$
Une cote **positive** est parcourue dans le sens de la condition, une cote **négative** en sens inverse. Les tolérances s'**ajoutent** toujours : elles ne se compensent jamais. Plus la chaîne est **longue**, plus chaque cote doit être **serrée** — et plus la pièce coûte cher.
:::

::: exemple Calcul de la cote C
On impose 0,1 ≤ J ≤ 0,3, avec A = 60 ± 0,05 et B = 35 ± 0,03.
IT(J) = 0,2 ; IT(A) = 0,1 ; IT(B) = 0,06 ⇒ IT(C) = 0,2 − 0,1 − 0,06 = **0,04**.
J maxi = A maxi − B mini − C mini ⇒ 0,3 = 60,05 − 34,97 − C mini ⇒ C mini = 24,78.
J mini = A mini − B maxi − C maxi ⇒ 0,1 = 59,95 − 35,03 − C maxi ⇒ C maxi = 24,82.
Vérification : 24,82 − 24,78 = 0,04 ✓ On écrit **C = 24,80 ± 0,02**.
:::

Sur la perceuse, la condition **JA** du boîtier de commande obéit à la même mécanique. Sa chaîne fait intervenir quatre cotes — A3 sur le bâti (3), A13 sur le pignon (13), A20 sur l'anneau élastique (20) et A25 sur le coussinet (25) — avec 0 ≤ JA ≤ 0,2 ; A3 = 58 ± 0,02 ; A20 = 1h11 ; A25 = 2 ± 0,02.

- IT(A3) = 0,04 et IT(A25) = 0,04.
- **A20 = 1h11** se lit dans le tableau ISO : cote nominale 1 mm, donc l'intervalle **IT11 = 0,06 mm** (valable pour toutes les dimensions jusqu'à 3 mm) ; la position **h** impose un **écart supérieur nul**. Donc A20 = 1 (0 / −0,06) et IT(A20) = 0,06.
- Il reste : IT(A13) = 0,2 − 0,04 − 0,06 − 0,04 = **0,06** ✓

> 🗡️ Retiens le réflexe : **d'abord les IT, ensuite les extrêmes**. La somme des IT te donne immédiatement la tolérance qui reste au fabricant ; si elle tombe négative, la condition est **impossible** et il faut resserrer une autre cote.

## ✏️ Le dessin de définition et les coupes particulières

::: definition Le dessin de définition
Il représente **une seule pièce** d'un ensemble ou d'un sous-ensemble. Il définit **complètement et sans ambiguïté** les exigences auxquelles doit satisfaire le produit, et prépare sa fabrication par cinq informations : la **matière**, la **forme**, la **cotation dimensionnelle**, les **spécifications géométriques**, et la **qualité de l'état des surfaces** à obtenir.
:::

Pour montrer l'intérieur d'une pièce, on est parfois obligé d'utiliser des **coupes** et des **sections**.

| Représentation                      | Quand l'employer                                              | Ce qu'elle évite                                                     |
| ----------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Demi-coupe**                      | pièces **symétriques**                                        | la représentation des détails cachés ; on voit intérieur + extérieur |
| **Coupe à plans parallèles**        | formes situées dans des plans **parallèles**                  | une vue supplémentaire en coupe, ou des détails cachés               |
| **Coupe brisée à plans sécants**    | formes situées dans des plans **concourants** (sécants)       | une vue oblique supplémentaire et une représentation **déformée**    |
| **Section sortie**                  | montrer la seule matière coupée, à l'extérieur de la vue      | l'encombrement de la vue par des traits inutiles                     |
| **Section rabattue**                | idem, mais rabattue **sur** la vue, en **trait fin**          | une vue ou une section supplémentaire                                |

::: figure La demi-coupe d'une pièce symétrique : à gauche l'extérieur, sans aucun trait caché ; à droite la matière coupée, hachurée. L'axe sépare les deux moitiés.
<svg viewBox="0 0 260 200">
<path d="M152 40 H200 V70 H175 V160 H152 Z" fill="#0f6e56" opacity="0.10"/>
<path d="M152 46 L158 40 M152 54 L166 40 M152 62 L174 40 M152 70 L182 40 M160 70 L190 40 M168 70 L198 40 M176 70 L200 46 M184 70 L200 54 M192 70 L200 62 M152 72 L154 70 M152 80 L162 70 M152 88 L170 70 M152 96 L175 73 M152 104 L175 81 M152 112 L175 89 M152 120 L175 97 M152 128 L175 105 M152 136 L175 113 M152 144 L175 121 M152 152 L175 129 M152 160 L175 137 M160 160 L175 145 M168 160 L175 153" fill="none" stroke="#0f172a" stroke-width="0.9"/>
<path d="M130 40 H60 V70 H85 V160 H130" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M130 40 H200 V70 H175 V160 H130" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M152 40 V160" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M130 32 V186" fill="none" stroke="#0f172a" stroke-width="1" stroke-dasharray="14 4 3 4"/>
<g font-size="10" font-weight="700" text-anchor="middle" fill="#0f6e56"><text x="86" y="24">vue extérieure</text><text x="184" y="24">coupe</text></g>
</svg>
:::

::: figure La coupe à plans parallèles : le plan se décale d'un cran pour attraper les deux perçages. Sur la coupe A-A, le trait d'axe marque le changement de plan et les hachures sont décalées de part et d'autre.
<svg viewBox="0 0 380 218">
<rect x="30" y="20" width="320" height="90" fill="none" stroke="#0f172a" stroke-width="2"/>
<circle cx="90" cy="45" r="14" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<circle cx="270" cy="85" r="14" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M12 45 H150 V85 H368" fill="none" stroke="#0f172a" stroke-width="1" stroke-dasharray="14 3 3 3"/>
<path d="M12 45 H34 M132 45 H150 M150 45 V62 M150 68 V85 M150 85 H168 M346 85 H368" fill="none" stroke="#0f172a" stroke-width="3.5"/>
<path d="M12 45 V58 M368 85 V98" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<g fill="#0f172a"><polygon points="12,64 7,52 17,52"/><polygon points="368,104 363,92 373,92"/></g>
<g font-size="12" font-weight="700" fill="#0f172a"><text x="4" y="38">A</text><text x="360" y="78">A</text></g>
<g fill="#0f6e56" opacity="0.10"><rect x="30" y="140" width="46" height="56"/><rect x="104" y="140" width="152" height="56"/><rect x="284" y="140" width="66" height="56"/></g>
<path d="M30 148 L38 140 M30 157 L47 140 M30 166 L56 140 M30 175 L65 140 M30 184 L74 140 M30 193 L76 147 M36 196 L76 156 M45 196 L76 165 M54 196 L76 174 M63 196 L76 183 M72 196 L76 192 M104 146 L110 140 M104 155 L119 140 M104 164 L128 140 M104 173 L137 140 M104 182 L146 140 M104 191 L150 145 M108 196 L150 154 M117 196 L150 163 M126 196 L150 172 M135 196 L150 181 M144 196 L150 190 M150 149.5 L159.5 140 M150 158.5 L168.5 140 M150 167.5 L177.5 140 M150 176.5 L186.5 140 M150 185.5 L195.5 140 M150 194.5 L204.5 140 M157.5 196 L213.5 140 M166.5 196 L222.5 140 M175.5 196 L231.5 140 M184.5 196 L240.5 140 M193.5 196 L249.5 140 M202.5 196 L256 142.5 M211.5 196 L256 151.5 M220.5 196 L256 160.5 M229.5 196 L256 169.5 M238.5 196 L256 178.5 M247.5 196 L256 187.5 M284 141.5 L285.5 140 M284 150.5 L294.5 140 M284 159.5 L303.5 140 M284 168.5 L312.5 140 M284 177.5 L321.5 140 M284 186.5 L330.5 140 M284 195.5 L339.5 140 M292.5 196 L348.5 140 M301.5 196 L350 147.5 M310.5 196 L350 156.5 M319.5 196 L350 165.5 M328.5 196 L350 174.5 M337.5 196 L350 183.5 M346.5 196 L350 192.5" fill="none" stroke="#0f172a" stroke-width="0.9"/>
<path d="M30 140 H76 M104 140 H256 M284 140 H350 M30 196 H76 M104 196 H256 M284 196 H350 M30 140 V196 M350 140 V196 M76 140 V196 M104 140 V196 M256 140 V196 M284 140 V196" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M150 134 V202" fill="none" stroke="#0f172a" stroke-width="1" stroke-dasharray="14 3 3 3"/>
<text x="190" y="214" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a">A-A</text>
</svg>
:::

::: figure Deux façons de placer une section. En 1, la section rabattue est tracée en trait fin directement sur la vue ; en 2, la section sortie est dessinée à l'extérieur, dans le prolongement du plan de coupe.
<svg viewBox="0 0 320 230">
<path d="M46 71 H290 V119 H46" fill="#0f6e56" opacity="0.10"/>
<circle cx="46" cy="95" r="26" fill="#0f6e56" opacity="0.10"/>
<path d="M46 69 H290 V121 H46" fill="none" stroke="#0f172a" stroke-width="2"/>
<circle cx="46" cy="95" r="26" fill="none" stroke="#0f172a" stroke-width="2"/>
<circle cx="46" cy="95" r="11" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<path d="M138 74 L143 69 M138 81 L150 69 M138 88 L157 69 M138 95 L162 71 M138 102 L162 78 M138 109 L162 85 M138 116 L162 92 M140 121 L162 99 M147 121 L162 106 M154 121 L162 113 M161 121 L162 120" fill="none" stroke="#0f172a" stroke-width="0.7"/>
<rect x="138" y="69" width="24" height="52" fill="none" stroke="#0f172a" stroke-width="1"/>
<path d="M250 56 V134" fill="none" stroke="#0f172a" stroke-width="1" stroke-dasharray="14 3 3 3"/>
<path d="M250 56 V70 M250 120 V134" fill="none" stroke="#0f172a" stroke-width="3.5"/>
<path d="M250 60 H266 M250 130 H266" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<g fill="#0f172a"><polygon points="272,60 260,55 260,65"/><polygon points="272,130 260,125 260,135"/></g>
<g font-size="12" font-weight="700" fill="#0f172a"><text x="276" y="54">B</text><text x="276" y="146">B</text></g>
<path d="M238 151 L241 148 M238 158 L248 148 M238 165 L255 148 M238 172 L262 148 M238 179 L262 155 M238 186 L262 162 M238 193 L262 169 M238 200 L262 176 M245 200 L262 183 M252 200 L262 190 M259 200 L262 197" fill="none" stroke="#0f172a" stroke-width="0.9"/>
<rect x="238" y="148" width="24" height="52" fill="none" stroke="#0f172a" stroke-width="2"/>
<text x="250" y="218" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a">B-B</text>
<g font-size="14" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="150" y="58">1</text><text x="288" y="176">2</text></g>
</svg>
:::

> ⚠️ **Coupe ≠ section.** La coupe montre **tout ce qui se trouve derrière** le plan ; la section ne montre **que la matière coupée**, rien d'autre. Et n'oublie jamais la règle des plans sécants : on ne dessine **pas** les parties cachées dans le plan rabattu, et la partie non alignée **pivote** pour être présentée en **vraie grandeur**.

## 💻 La modélisation numérique (3D et 2D)

La **modélisation tridimensionnelle** consiste à créer, par un **logiciel de modélisation 3D**, un objet en trois dimensions — par **ajout**, **soustraction** et **modification** de ses constituants — pour arriver ensuite à la représentation de cet objet en **2D**. Le fourreau (4) et le moyeu (11) que tu viens de décoder se modélisent ainsi : un cylindre, un perçage soustrait, une denture ajoutée, et les vues 2D tombent toutes seules.

## 🔤 Rappel : lire la désignation des matériaux

Chaque matière de la nomenclature raconte pourquoi la pièce est faite ainsi.

| Désignation      | Comment la lire                                                                     | Sur la perceuse                        |
| ---------------- | ----------------------------------------------------------------------------------- | -------------------------------------- |
| **C35**, **C60** | acier **non allié** : 0,35 % et 0,60 % de carbone (le nombre ÷ 100)                 | broche (5), fourreau (4) ; couvercle (21) |
| **S235**         | acier de construction : limite d'élasticité minimale Re = 235 MPa                   | bras de commande (24)                  |
| **100 Cr 6**     | acier **faiblement allié** : 1,00 % de carbone ; chrome 6 ÷ 4 = 1,5 %               | bagues des roulements (1) et (8)       |
| **36 Ni Cr Mo16**| acier faiblement allié : 0,36 % de carbone ; nickel 16 ÷ 4 = 4 %, plus Cr et Mo     | moyeu (11)                             |
| **60 Si Cr 7**   | acier à ressort : 0,60 % de carbone ; silicium 7 ÷ 4 = 1,75 %, plus du chrome       | ressort spiral (22)                    |
| **EN GJL 250**   | fonte à **graphite lamellaire** : résistance minimale à la traction Rm = 250 MPa    | bâti (3) ; EN GJL 200 pour le boîtier (15) |
| **Al Si 10 Mg**  | alliage d'**aluminium** de fonderie : 10 % de silicium, avec du magnésium            | poulie étagée (12)                     |
| **Cu Sn 8**      | alliage de **cuivre** (bronze) : 8 % d'étain                                        | coussinet (25)                         |

> 🗡️ Le diviseur dépend de l'élément : **4** pour Cr, Ni, Si, Mn, Co, W ; **10** pour Al, Cu, Mo, Ti, V ; **100** pour P, S, N. Et dans un acier **non allié** (lettre C), seul le carbone est chiffré, divisé par 100.

> 🏆 Le plan ne te résiste plus, héros. Tu sais le lire en deux temps, y voir des liaisons plutôt que des traits, en tirer l'ordre d'un démontage, fermer une chaîne de cotes et choisir la coupe qui montre ce qu'il faut montrer. C'est exactement le métier du technicien en bureau d'études — et c'est ce que l'épreuve du bac te demandera, la nomenclature à la main.
