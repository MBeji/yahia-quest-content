# ⚙️ Dans la tête de la fraiseuse : ce qui tient, ce qui tourne

> 💡 «Une machine n'est pas un tas de pièces : c'est un réseau de liaisons. Pour chaque pièce, une seule question compte — qu'est-ce qui la tient, et qu'est-ce qui la laisse tourner ?»

Nouveau thème, nouvel angle : **Typologie des assemblages**. Jusqu'ici tu lisais des plans ; maintenant tu **justifies des choix de construction** (compétence CD 2.2 : concevoir une solution constructive en justifiant ses choix) et tu apprends à **compléter un schéma cinématique** (CD 3.8). Le thème traite les **liaisons mécaniques** : la fonction **assemblage**, puis la fonction **guidage en rotation** — roulements à une rangée de billes à contact radial (un rappel), puis roulements à contact oblique. Premier support : la **tête universelle de la fraiseuse « MILKO 14 »**, cinq activités (1.1 à 1.5), 50 repères et un dessin d'ensemble à l'échelle 2:5.

## 🧭 Le support : une tête qui pivote, et la chaîne qui entraîne la broche

Une **fraiseuse** est une machine-outil : un **outil tournant**, la fraise, enlève de la matière sur une pièce fixée à la table. Le **mouvement de coupe** est donné à l'outil, le **mouvement d'avance** à la pièce. La tête « MILKO 14 » se compose de **deux parties** qui peuvent pivoter ensemble par rapport au bâti fixe, ou l'une par rapport à l'autre ; en combinant les deux rotations, on donne à la broche **toutes les orientations**.

Question : comment la rotation de l'**arbre d'entrée horizontal** arrive-t-elle jusqu'à la **broche porte-outil (36)** ?

::: definition La chaîne de transmission de la tête
Le manuel la décrit en une phrase : le mouvement est transmis de l'**arbre d'entrée horizontal**, lié à la roue dentée (28), à la **broche (36)** par **un engrenage cylindrique à denture droite (28, 9)** et **deux renvois d'angle à 45° (14, 26) et (22, 42)**. Deux nombres entre parenthèses séparés par une virgule désignent **deux roues en prise** ; un renvoi d'angle est un couple de **roues coniques** qui change la direction de l'axe de rotation (45° + 45° = 90° : de l'horizontale à la verticale).
:::

::: figure Cinq blocs, une seule rotation : dans chaque bloc, les pièces sont solidaires et tournent ensemble ; entre deux blocs, une flèche verte marque une prise de denture
<svg viewBox="0 0 440 338"><rect x="20" y="12" width="210" height="34" rx="5" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><text x="125" y="33" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a">Arbre d'entrée horizontal + roue (28)</text><path d="M125 47 L125 73" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linecap="round"/><polygon points="125,81 121.4,73 128.6,73" fill="#0f6e56"/><text x="240" y="68.0" font-size="11" font-weight="700" text-anchor="start" fill="#0f6e56">engrenage cylindrique (28, 9)</text><rect x="20" y="82" width="210" height="34" rx="5" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><text x="125" y="103" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a">Roue (9) + pignon arbré (14)</text><path d="M125 117 L125 143" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linecap="round"/><polygon points="125,151 121.4,143 128.6,143" fill="#0f6e56"/><text x="240" y="138.0" font-size="11" font-weight="700" text-anchor="start" fill="#0f6e56">renvoi d'angle à 45° (14, 26)</text><rect x="20" y="152" width="210" height="34" rx="5" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><text x="125" y="173" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a">Roues coniques (26) + (22)</text><path d="M125 187 L125 213" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linecap="round"/><polygon points="125,221 121.4,213 128.6,213" fill="#0f6e56"/><text x="240" y="208.0" font-size="11" font-weight="700" text-anchor="start" fill="#0f6e56">renvoi d'angle à 45° (22, 42)</text><rect x="20" y="222" width="210" height="34" rx="5" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><text x="125" y="243" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a">Roue conique (42) + broche (36)</text><path d="M125 257 L125 283" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linecap="round"/><polygon points="125,291 121.4,283 128.6,283" fill="#0f6e56"/><text x="240" y="278.0" font-size="11" font-weight="700" text-anchor="start" fill="#0f6e56">la broche porte l'outil</text><rect x="20" y="292" width="210" height="34" rx="5" fill="#fde68a" stroke="#0f172a" stroke-width="2"/><text x="125" y="313" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a">Mandrin (49) + fraise (50)</text></svg>
:::

::: exemple Suivre le mouvement de l'entrée à la broche

1. L'**arbre d'entrée** est lié à la roue **(28)** : ils tournent ensemble — c'est le point de départ.
2. **(28)** engrène avec **(9)** par la denture droite : la rotation passe au bloc suivant, **en sens inverse**, puisque deux roues cylindriques extérieures en prise tournent à contre-sens.
3. **(9)** est assemblée au pignon arbré **(14)** : elles sont **solidaires**, donc (14) tourne **comme (9)**.
4. **(14)** engrène avec la roue conique **(26)** : premier renvoi d'angle à 45°.
5. **(26)** est assemblée à **(22)** : (22) tourne comme (26). **(22)** engrène avec **(42)** : second renvoi d'angle.
6. **(42)** est assemblée à la **broche (36)**, qui porte le mandrin (49) et la fraise (50) : la rotation est arrivée.

:::

> ⚠️ Ne confonds pas **« en prise »** et **« solidaire »**. (28, 9) sont en prise : deux pièces distinctes, sens opposés. (9) et (14) sont solidaires : une seule classe d'équivalence, même sens. Lire un nombre de dents ou un rapport sur une pièce solidaire d'une autre n'a aucun sens : la liaison, elle, se lit entre blocs.

::: verifie Même chaîne, deux questions
L'arbre d'entrée tourne dans un sens donné. La roue (9) tourne-t-elle dans le même sens que (28) ? Et le pignon arbré (14) par rapport à (9) ?

---

(9) tourne en **sens contraire** de (28) : les deux roues sont en prise par une denture droite extérieure. (14) tourne dans le **même sens** que (9) : elles sont assemblées, donc solidaires, donc une seule classe d'équivalence.
:::

::: retenir
Rotation de l'arbre d'entrée → (28, 9) → (14, 26) → (22, 42) → broche (36) : **en prise** entre blocs, **solidaire** à l'intérieur d'un bloc.
:::

## 🗺️ Lire le plan de la tête : échelle 2:5 et 50 repères

Tu ouvres le dessin d'ensemble : le cartouche annonce « Tête universelle de fraiseuse », **échelle 2:5**, avec le symbole de la méthode de projection européenne.

Question : une fraise de diamètre 50 mm, quelle longueur occupe-t-elle sur le papier — et comment retrouver une dimension réelle à partir du dessin ?

::: definition L'échelle d'un dessin
Une échelle s'écrit **dessin : réel**. Avec **2:5**, deux millimètres de papier représentent cinq millimètres de la machine : c'est une **réduction** de rapport 2 ÷ 5 = 0,4. Pour passer du dessin au réel, on **multiplie par 5 ÷ 2** (2,5) ; pour passer du réel au dessin, on multiplie par 0,4.
:::

La nomenclature compte **50 lignes** (colonnes Rep., Nbr., Désignation, Matière, Observation), et le dessin porte aussi un repère **qui est une lettre**, **E** : il n'a pas de ligne dans la nomenclature, donc on n'en lit pas la désignation — c'est son emplacement et ses contacts qui disent sa fonction. Trois lignes (12, 40 et 45) sont volontairement incomplètes : « Roulement………… » : le type de roulement reste à identifier par l'élève.

::: exemple De la fraise au papier
La fraise à deux tailles fait **50 mm** de diamètre réel.

1. L'échelle est **2:5** : le dessin est plus petit que la réalité.
2. On multiplie le réel par le rapport dessin ÷ réel : 50 × 2 ÷ 5.
3. 50 × 2 = 100, puis 100 ÷ 5 = **20 mm** sur le papier.

:::

> ⚠️ L'erreur classique est de lire **2:5 comme « deux fois plus grand »** ou de multiplier dans le mauvais sens. Un 2:5 ne peut jamais donner un dessin plus grand que la pièce : si ton résultat dépasse la réalité, tu as inversé le rapport.

::: verifie À rebours : du dessin vers la machine
Un détail mesure 30 mm sur le dessin au 2:5. Quelle est sa dimension réelle ?

---

On passe du dessin au réel : on multiplie par 5 ÷ 2. 30 × 5 = 150, puis 150 ÷ 2 = **75 mm**. Contrôle : 75 > 30, un dessin réduit est toujours plus petit que la pièce.
:::

::: retenir
Échelle **dessin : réel** ; 2:5 = réduction (× 0,4 vers le papier, × 2,5 vers la machine). Un repère peut être une **lettre** sans ligne de nomenclature.
:::

## 🔩 Combien de mouvements une liaison supprime-t-elle ?

Activité 1.1 : une rainure de clavette exige de remplacer le mandrin porte-fraise de diamètre 50 mm par un **mandrin à pince**. Avant de démonter : **arrêt d'urgence enclenché, arrêt total de la broche vérifié, gants résistants aux coupures**, et outils rangés à la fin.

Reste la question : qu'est-ce qui, exactement, tient le mandrin dans la broche ?

::: definition Mobilités, liaison complète, liaison partielle
Une pièce libre dans l'espace peut bouger de **six façons**, repérées dans un trièdre : trois **translations** **Tx, Ty, Tz** et trois **rotations** **Rx, Ry, Rz** autour des mêmes axes. Une **liaison** supprime certaines de ces **mobilités**. Quand il n'en reste **aucune**, la liaison est **complète** (un **encastrement**) ; quand il en reste **au moins une**, elle est **partielle** (un pivot laisse une rotation). Un **assemblage** se juge donc par le nombre et la nature des mobilités qu'il supprime.
:::

::: figure Le porte-outil (49) dans le nez de la broche (36), axe Z vertical. Le cône ne laisse que la rotation autour de Z ; le lardon, logé dans sa rainure, bloque cette dernière ; le tirant (35) tire le cône pour le garder plaqué
<svg viewBox="0 0 400 272"><path d="M112 24 L178 24 L178 40 L152 190 L112 190 Z" fill="#ffffff"/><path d="M112 32 L120 24 M112 40 L128 24 M112 48 L136 24 M112 56 L144 24 M112 64 L152 24 M112 72 L160 24 M112 80 L168 24 M112 88 L176 24 M112 96 L178 30 M112 104 L178 38 M112 112 L176.7 47.3 M112 120 L175.1 56.9 M112 128 L173.4 66.6 M112 136 L171.7 76.3 M112 144 L170 86 M112 152 L168.4 95.6 M112 160 L166.7 105.3 M112 168 L165 115 M112 176 L163.3 124.7 M112 184 L161.6 134.4 M114 190 L160 144 M122 190 L158.3 153.7 M130 190 L156.6 163.4 M138 190 L154.9 173.1 M146 190 L153.3 182.7" fill="none" stroke="#334155" stroke-width="0.8"/><path d="M112 24 L178 24 L178 40 L152 190 L112 190 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M268 24 L202 24 L202 40 L228 190 L268 190 Z" fill="#ffffff"/><path d="M202 30 L208 24 M202 38 L216 24 M202.9 45.1 L224 24 M204.1 51.9 L232 24 M205.2 58.8 L240 24 M206.4 65.6 L248 24 M207.6 72.4 L256 24 M208.8 79.2 L264 24 M210 86 L268 28 M211.2 92.8 L268 36 M212.3 99.7 L268 44 M213.5 106.5 L268 52 M214.7 113.3 L268 60 M215.9 120.1 L268 68 M217.1 126.9 L268 76 M218.2 133.8 L268 84 M219.4 140.6 L268 92 M220.6 147.4 L268 100 M221.8 154.2 L268 108 M223 161 L268 116 M224.2 167.8 L268 124 M225.3 174.7 L268 132 M226.5 181.5 L268 140 M227.7 188.3 L268 148 M234 190 L268 156 M242 190 L268 164 M250 190 L268 172 M258 190 L268 180 M266 190 L268 188" fill="none" stroke="#334155" stroke-width="0.8"/><path d="M268 24 L202 24 L202 40 L228 190 L268 190 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M171.1 60 L208.9 60 L228 190 L152 190 Z" fill="#ffffff"/><path d="M152.8 184.8 L158 190 M153.8 177.8 L166 190 M154.8 170.8 L174 190 M155.8 163.8 L182 190 M156.9 156.9 L190 190 M157.9 149.9 L198 190 M158.9 142.9 L206 190 M159.9 135.9 L214 190 M161 129 L222 190 M162 122 L227.7 187.7 M163 115 L226.3 178.3 M164 108 L224.9 168.9 M165 101 L223.5 159.5 M166.1 94.1 L222.2 150.2 M167.1 87.1 L220.8 140.8 M168.1 80.1 L219.4 131.4 M169.1 73.1 L218 122 M170.2 66.2 L216.7 112.7 M172 60 L215.3 103.3 M180 60 L213.9 93.9 M188 60 L212.5 84.5 M196 60 L211.2 75.2 M204 60 L209.8 65.8" fill="none" stroke="#334155" stroke-width="0.8"/><path d="M171.1 60 L208.9 60 L228 190 L152 190 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M138 190 L242 190 L242 214 L138 214 Z" fill="#ffffff"/><path d="M138 210 L142 214 M138 202 L150 214 M138 194 L158 214 M142 190 L166 214 M150 190 L174 214 M158 190 L182 214 M166 190 L190 214 M174 190 L198 214 M182 190 L206 214 M190 190 L214 214 M198 190 L222 214 M206 190 L230 214 M214 190 L238 214 M222 190 L242 210 M230 190 L242 202 M238 190 L242 194" fill="none" stroke="#334155" stroke-width="0.8"/><path d="M138 190 L242 190 L242 214 L138 214 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M170 214 L210 214 L210 262 L170 262 Z" fill="#ffffff"/><path d="M170 258 L174 262 M170 250 L182 262 M170 242 L190 262 M170 234 L198 262 M170 226 L206 262 M170 218 L210 258 M174 214 L210 250 M182 214 L210 242 M190 214 L210 234 M198 214 L210 226 M206 214 L210 218" fill="none" stroke="#334155" stroke-width="0.8"/><path d="M170 214 L210 214 L210 262 L170 262 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M170 8 L210 8 L210 24 L170 24 Z" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><path d="M184 24 L196 24 L196 82 L184 82 Z" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><path d="M184 66 L196 70 M184 72 L196 76 M184 78 L196 82" fill="none" stroke="#0f172a" stroke-width="1"/><rect x="140" y="182" width="10" height="16" fill="#fdba74" stroke="#0f172a" stroke-width="2"/><path d="M190 2 L190 272" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="12 3 3 3" /><text x="70" y="108" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">broche (36)</text><path d="M94 112 L116 120" fill="none" stroke="#0f172a" stroke-width="1" /><text x="300" y="128" font-size="13" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">porte-outil (49)</text><path d="M296 126 L222 126" fill="none" stroke="#0f172a" stroke-width="1" /><text x="262" y="24" font-size="13" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">tirant (35)</text><path d="M258 22 L212 16" fill="none" stroke="#0f172a" stroke-width="1" /><text x="60" y="232" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">lardon</text><path d="M80 224 L142 196" fill="none" stroke="#0f172a" stroke-width="1" /><path d="M318 238 L318 194" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><polygon points="318,186 321.6,194 314.4,194" fill="#0f172a"/><path d="M318 238 L362 238" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><polygon points="370,238 362,241.6 362,234.4" fill="#0f172a"/><circle cx="318" cy="238" r="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><path d="M314.5 234.5 L321.5 241.5 M314.5 241.5 L321.5 234.5" stroke="#0f172a" stroke-width="1.6"/><text x="308" y="186" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Z</text><text x="378" y="242" font-size="13" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">X</text><text x="332" y="256" font-size="13" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Y</text></svg>
:::

Dans la figure, l'axe **Z** est l'axe de la broche : ce que le **cône** supprime se lit par rapport à lui. Chaque **nature de surface** de contact supprime un nombre connu de mobilités. Convention : une translation arrêtée **dans un sens** par la surface est comptée **supprimée** quand un obstacle ou un maintien (tirant, vis, serrage) la retient **dans l'autre sens**.

| Contact (axe Z)                             | Mobilités supprimées                   | Nombre |
| ------------------------------------------- | -------------------------------------- | ------ |
| Appui plan, perpendiculaire à Z             | Tz (un sens), Rx, Ry                   | 3      |
| Centrage court (cylindre court)             | Tx, Ty                                 | 2      |
| Centrage long (cylindre long)               | Tx, Ty, Rx, Ry                         | 4      |
| Cône long                                   | Tx, Ty, Rx, Ry, plus Tz dans un sens   | 5      |
| Lardon dans sa rainure (plan parallèle à Z) | Rz, quand le cône a déjà fait le reste | 1      |

::: exemple Le mandrin dans la broche, mobilité par mobilité

1. **Nature des surfaces** : un cône (le porte-outil dans la broche), puis deux faces planes (le lardon contre les flancs de sa rainure).
2. Le **cône long** supprime **Tx, Ty, Rx, Ry** (il centre et empêche de basculer) et **Tz dans un sens** (il ne peut pas s'enfoncer davantage), l'autre sens étant repris par le **tirant** : 5 mobilités.
3. Il reste **Rz**, la rotation autour de l'axe : seul le cône ne peut pas l'empêcher.
4. Le **lardon** dans sa rainure supprime **Rz** : une mobilité de plus, la sixième.
5. Total : **6**, aucune ne reste : la liaison est **complète**, à condition que le tirant tienne.

:::

> ⚠️ Ne compte pas ce que chaque surface supprimerait **seule** : un lardon seul, par ses deux plans, supprimerait trois mobilités, mais deux sont **déjà supprimées** par le cône. Chaque mobilité se compte **une seule fois** : si ta somme dépasse 6, tu as compté deux fois la même.

::: methode Compter les mobilités d'un assemblage

1. **Nomme** les surfaces en contact et leur **nature** (plane, cylindrique, conique).
2. Pour chacune, **liste** les mobilités qu'elle supprime dans le trièdre (une translation arrêtée dans un sens compte si un maintien la retient dans l'autre).
3. **Ne garde que les nouvelles** : une mobilité déjà supprimée ne se recompte pas.
4. **Conclus** : six supprimées, liaison complète ; sinon liste celles qui restent (une rotation seule : **pivot**).

Cas limite : le carter (2) sur le bâti (1), écrous desserrés, peut être orienté : une rotation reste libre, c'est un pivot. Resserrés, les écrous suppriment cette rotation par **adhérence** : la liaison devient complète.
:::

::: verifie Une roue sur son arbre
Une roue est centrée sur une portée cylindrique **longue** d'axe Z et appuie sur un épaulement plan perpendiculaire à Z. Elle peut encore tourner autour de Z. Combien de mobilités sont supprimées, et quelle liaison obtient-on ?

---

Le centrage long supprime **Tx, Ty, Rx, Ry** (4). L'épaulement apporterait trois mobilités seul, mais Rx et Ry sont déjà comptées : il n'ajoute que **Tz dans un sens**. Total **5** ; il reste **Rz** : c'est une liaison **pivot**, donc partielle.
:::

::: retenir
Six mobilités possibles (Tx, Ty, Tz, Rx, Ry, Rz) ; **zéro restante = liaison complète**. Plan : 3, centrage court : 2, centrage long : 4, cône long : 5 ; chaque mobilité se compte **une seule fois**.
:::

## 📌 Mettre en position, puis maintenir : MIP et MAP

Activité 1.2 : on veut incliner l'axe de la broche de 45° pour usiner une rainure en V. On **desserre légèrement** les écrous (53) et le carter s'oriente ; on les resserre, plus rien ne bouge.

Question : dans cet assemblage, **qui définit la position** et **qui la conserve** ?

::: definition MIP et MAP, rappelés pour les assemblages

- **MIP, mise en position** : donner à une pièce sa position **par les formes** — surfaces planes, cylindriques, coniques en contact, pièces de positionnement (pions, goupilles coniques, bagues de centrage). C'est elle qui supprime les mobilités **géométriquement**.
- **MAP, maintien en position** : **conserver le contact** des surfaces de la MIP, par un **obstacle démontable** (vis, écrou, anneau élastique, tirant) ou par **adhérence** (le serrage).

:::

::: figure Un appui plan et deux pions mettent la pièce en position (MIP, en vert le contact plan) ; la vis, qui traverse un trou de passage plus large qu'elle, ne positionne rien : elle maintient (MAP)
<svg viewBox="0 0 360 240"><path d="M30 170 L330 170 L330 222 L30 222 Z" fill="#ffffff"/><path d="M30 178 L38 170 M30 186 L46 170 M30 194 L54 170 M30 202 L62 170 M30 210 L70 170 M30 218 L78 170 M34 222 L86 170 M42 222 L94 170 M50 222 L102 170 M58 222 L110 170 M66 222 L118 170 M74 222 L126 170 M82 222 L134 170 M90 222 L142 170 M98 222 L150 170 M106 222 L158 170 M114 222 L166 170 M122 222 L174 170 M130 222 L182 170 M138 222 L190 170 M146 222 L198 170 M154 222 L206 170 M162 222 L214 170 M170 222 L222 170 M178 222 L230 170 M186 222 L238 170 M194 222 L246 170 M202 222 L254 170 M210 222 L262 170 M218 222 L270 170 M226 222 L278 170 M234 222 L286 170 M242 222 L294 170 M250 222 L302 170 M258 222 L310 170 M266 222 L318 170 M274 222 L326 170 M282 222 L330 174 M290 222 L330 182 M298 222 L330 190 M306 222 L330 198 M314 222 L330 206 M322 222 L330 214" fill="none" stroke="#334155" stroke-width="0.8"/><path d="M30 170 L330 170 L330 222 L30 222 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M90 100 L270 100 L270 170 L90 170 Z" fill="#ffffff"/><path d="M90 162 L98 170 M90 154 L106 170 M90 146 L114 170 M90 138 L122 170 M90 130 L130 170 M90 122 L138 170 M90 114 L146 170 M90 106 L154 170 M92 100 L162 170 M100 100 L170 170 M108 100 L178 170 M116 100 L186 170 M124 100 L194 170 M132 100 L202 170 M140 100 L210 170 M148 100 L218 170 M156 100 L226 170 M164 100 L234 170 M172 100 L242 170 M180 100 L250 170 M188 100 L258 170 M196 100 L266 170 M204 100 L270 166 M212 100 L270 158 M220 100 L270 150 M228 100 L270 142 M236 100 L270 134 M244 100 L270 126 M252 100 L270 118 M260 100 L270 110 M268 100 L270 102" fill="none" stroke="#334155" stroke-width="0.8"/><path d="M90 100 L270 100 L270 170 L90 170 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="228" y="100" width="24" height="70" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/><rect x="232" y="170" width="16" height="38" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/><path d="M232 176 L248 180 M232 184 L248 188 M232 192 L248 196 M232 200 L248 204" fill="none" stroke="#0f172a" stroke-width="1"/><rect x="110" y="140" width="20" height="55" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><rect x="160" y="140" width="20" height="55" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><rect x="222" y="82" width="36" height="18" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><rect x="232" y="100" width="16" height="106" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><path d="M232 176 L248 180 M232 184 L248 188 M232 192 L248 196 M232 200 L248 204" fill="none" stroke="#0f172a" stroke-width="1"/><path d="M90 170 L110 170 M130 170 L160 170 M180 170 L228 170 M252 170 L270 170" fill="none" stroke="#0f6e56" stroke-width="4" stroke-linecap="round"/><text x="100" y="92" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">pièce</text><text x="70" y="204" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">base</text><text x="150" y="126" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">pions</text><text x="290" y="70" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">vis</text><path d="M284 74 L256 90" fill="none" stroke="#0f172a" stroke-width="1" /><path d="M120 130 L120 144" fill="none" stroke="#0f172a" stroke-width="1" /><path d="M170 130 L170 144" fill="none" stroke="#0f172a" stroke-width="1" /></svg>
:::

L'**appui plan et les deux pions** de la figure se lisent comme la MIP ; la **vis** est la MAP. Les deux sont indispensables, parce qu'un contact plan est **unilatéral** : il empêche de s'enfoncer, jamais de se soulever.

::: exemple Le carter (2) sur le bâti (1)

1. **Écrous desserrés** : le carter s'oriente autour d'un axe. Une rotation est libre : la liaison est **partielle**, un pivot.
2. **Écrous resserrés** : le serrage presse les surfaces et crée de l'**adhérence** : elle supprime la dernière rotation. C'est la **MAP**.
3. Conclusion : les **écrous (53)** et leur visserie assurent le **maintien** ; ce sont les **surfaces** qui définissent la position, et on peut tourner la pièce **uniquement quand la MAP est relâchée**.

:::

> ⚠️ « Si les surfaces sont bien usinées, la pièce reste en place d'elle-même » est faux. Sans MAP, la MIP ne tient que sous le poids de la pièce : une vibration, un choc, et la pièce quitte son appui. Une MIP seule **positionne** ; elle ne **retient** pas.

::: verifie Un élément qui disparaît
Dans la figure, la vis est retirée : la pièce reste posée sur la base, pions engagés. Que reste-t-il de la MIP, que reste-t-il de la MAP ?

---

La **MIP** subsiste : l'appui plan et les pions définissent encore la position. La **MAP** a disparu : rien n'empêche plus la pièce de se soulever. L'assemblage est donc **positionné mais pas tenu**.
:::

::: retenir
**MIP** = position par les formes ; **MAP** = maintien par obstacle ou adhérence. La MIP positionne, la MAP retient : il faut les deux.
:::

## 🔗 Lier en rotation, lier en translation : les solutions d'encastrement

Activité 1.4 : une ou plusieurs dents du pignon arbré (14) sont abîmées. Réparer oblige à changer **toute la pièce**, arbre compris : coût élevé.

Question : quelle solution d'assemblage **démontable** permettrait de ne remplacer que la roue, vite et à moindre coût ?

::: definition Le F.A.S.T. d'une liaison encastrement
La fonction principale est « **Assurer une liaison encastrement** entre l'arbre et la roue conique ». Elle se décompose en deux fonctions techniques : **lier en rotation** (supprimer Rz) et **lier en translation** (supprimer Tz dans les deux sens). Chacune reçoit sa **solution constructive**.
:::

::: figure À gauche, la clavette logée à cheval dans l'arbre et dans le moyeu interdit la rotation ; à droite, l'épaulement d'un côté et l'anneau élastique de l'autre immobilisent le moyeu le long de l'arbre
<svg viewBox="0 0 430 200"><circle cx="100" cy="100" r="62" fill="#fde68a" stroke="#0f172a" stroke-width="2"/><circle cx="100" cy="100" r="34" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><rect x="93" y="60" width="14" height="12" fill="#fdba74" stroke="#0f172a" stroke-width="2"/><circle cx="100" cy="100" r="2.5" fill="#0f172a"/><text x="100" y="190" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">coupe transversale</text><path d="M240 56 L340 56 L340 144 L240 144 Z" fill="#fde68a" stroke="#0f172a" stroke-width="2"/><path d="M208 70 L240 70 L240 130 L208 130 Z" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><path d="M240 86 L400 86 L400 114 L240 114 Z" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><path d="M240 86 L400 86 L400 114 L240 114 Z" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><rect x="260" y="80" width="64" height="12" fill="#fdba74" stroke="#0f172a" stroke-width="2"/><rect x="340" y="78" width="8" height="30" fill="#334155" stroke="#0f172a" stroke-width="1.5"/><rect x="340" y="108" width="8" height="14" fill="#334155" stroke="#0f172a" stroke-width="1.5"/><path d="M194 100 L414 100" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="12 3 3 3" /><text x="224" y="156" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">épaulement</text><path d="M224 144 L224 130" fill="none" stroke="#0f172a" stroke-width="1" /><text x="292" y="48" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">moyeu</text><text x="292" y="74" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">clavette</text><text x="372" y="70" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">anneau élastique</text><path d="M372 76 L346 84" fill="none" stroke="#0f172a" stroke-width="1" /><text x="350" y="162" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">coupe longitudinale</text></svg>
:::

La figure montre les solutions de **S1** du manuel : la clavette parallèle avec ses rainures (coupe transversale, et panneau de droite) ; l'épaulement et l'anneau élastique pour arbre (panneau de droite seulement). **S2** remplace la clavette par des **cannelures**.

| Fonction            | Solutions constructives                                                                                         |
| ------------------- | --------------------------------------------------------------------------------------------------------------- |
| Lier en rotation    | clavette parallèle + rainures ; cannelures ; lardon + rainure ; tenon d'entraînement                            |
| Lier en translation | épaulement + anneau élastique pour arbre ; épaulement + rondelle d'appui + écrou à encoches avec rondelle frein |

::: exemple Compléter le F.A.S.T. d'une roue démontable

1. **Lier en rotation** : on choisit la **clavette parallèle** logée dans une rainure d'arbre et une rainure de moyeu ; elle supprime **Rz**.
2. **Lier en translation, premier sens** : l'**épaulement** de l'arbre arrête la roue d'un côté.
3. **Lier en translation, second sens** : l'**anneau élastique pour arbre**, logé dans une gorge, l'arrête de l'autre côté.

:::

> ⚠️ La clavette **ne lie pas en translation** : une clavette parallèle laisse la roue glisser le long de l'arbre. Sans épaulement ni anneau, la clavette entraîne la roue en rotation et la laisse partir à l'axial.

::: verifie Même question, autre solution
Une poulie doit être liée à son arbre par **cannelures** et ne pas glisser. Complète « lier en rotation » et « lier en translation ».

---

Lier en **rotation** : les **cannelures**, qui transmettent un couple plus élevé qu'une clavette seule. Lier en **translation** : une solution **à ajouter**, par exemple épaulement avec anneau élastique, car les cannelures ne retiennent pas la poulie axialement.
:::

::: retenir
Encastrement = **rotation** (clavette, cannelures, lardon) **+ translation** (épaulement + anneau élastique, ou écrou à encoches + rondelle frein). Clavette, cannelures et lardon ne lient qu'en rotation : il faut leur ajouter une solution de translation (épaulement + anneau élastique, ou écrou à encoches + rondelle frein).
:::

## ⚖️ Choisir entre deux solutions : la grille pondérée

Toujours l'activité 1.4 : deux solutions, **S1** (clavette + rainures) et **S2** (cannelures). L'énoncé demande de les **critiquer et pondérer**, puis de **choisir en justifiant**.

Question : comment trancher quand chacune gagne sur certains points ?

::: definition La grille de critères
Sept critères jugent une solution constructive : **degré de précision de la mise en position**, **intensité des actions mécaniques transmissibles**, **fiabilité**, **maintenabilité**, **encombrement**, **esthétique**, **coût**. Chacun reçoit une note : **0 mauvais, 1 moyen, 2 bien, 3 très bien**. **La note juge la solution sur le critère** : plus elle est haute, mieux c'est — y compris pour le coût, où une solution **économique** reçoit **3**. Le cahier des charges peut aussi **imposer un seuil** sur un critère (par exemple une maintenabilité d'au moins 3) : une solution qui ne l'atteint pas est **écartée**, quel que soit son total.
:::

::: exemple Deux solutions, des notes d'entraînement
Notes **inventées pour l'exercice** : elles ne remplacent pas ton analyse de l'activité.

| Critère                           | S1  | S2  |
| --------------------------------- | --- | --- |
| Précision de la mise en position  | 1   | 3   |
| Actions mécaniques transmissibles | 1   | 3   |
| Fiabilité                         | 2   | 3   |
| Maintenabilité                    | 3   | 2   |
| Encombrement                      | 3   | 2   |
| Esthétique                        | 2   | 2   |
| Coût                              | 3   | 1   |

1. **Totaux** : S1 = 1 + 1 + 2 + 3 + 3 + 2 + 3 = **15** ; S2 = 3 + 3 + 3 + 2 + 2 + 2 + 1 = **16**.
2. S2 gagne d'un point, mais l'énoncé impose de **réduire le coût et le temps de réparation** : les critères **coût** et **maintenabilité**.
3. Sur ces deux critères : S1 totalise 3 + 3 = **6**, S2 totalise 1 + 2 = **3**.
4. **Décision** : on retient **S1**, parce qu'elle gagne sur les critères que la situation impose, même si S2 l'emporte au total général.

:::

> ⚠️ Choisir « celle qui a le plus gros total » est un réflexe trompeur : le total met tous les critères au même niveau, la situation, non. On justifie un choix **par les critères décisifs**, pas par une somme.

::: verifie Même grille, autre contrainte
Avec les mêmes notes, le cahier des charges impose cette fois de **transmettre un couple élevé** avec une **bonne précision**. Quelle solution retient-on ?

---

Les critères décisifs sont les **actions transmissibles** (S1 : 1, S2 : 3) et la **précision de la MIP** (S1 : 1, S2 : 3). S2 totalise 6, S1 totalise 2 : on retient **S2**, les cannelures.
:::

::: retenir
Note de **0 à 3**, haute = bonne (même pour le coût). Total d'abord, **critères imposés** ensuite : c'est eux qui justifient.
:::

## 🎯 Guider en rotation : choisir le roulement selon la charge

Activité 1.5 : la tête comporte plusieurs **liaisons pivot** entre ses organes de transmission, par exemple celle de la broche (36), guidée par **deux roulements**.

Question : comment justifier un type de roulement plutôt qu'un autre ?

::: definition Le guidage en rotation et ses critères
Le **guidage en rotation** est la réalisation concrète d'une **liaison pivot**. Les **roulements** (une bague intérieure, une bague extérieure, des éléments roulants) sont choisis selon **deux critères** : les **charges** à supporter — radiales, axiales, et leurs directions — et la **vitesse** à transmettre.
:::

| Roulement                        | Charges                                                   | Vitesse    |
| -------------------------------- | --------------------------------------------------------- | ---------- |
| Billes à contact radial (rappel) | surtout radiales, un peu d'axial                          | élevée     |
| Billes à contact oblique         | radiales **et** axiales, axiale dans un seul sens         | importante |
| Rouleaux coniques                | radiales et axiales importantes, axiale dans un seul sens | moyenne    |
| Douille à aiguilles              | radiales, très faible encombrement radial                 | —          |
| Butée à aiguilles                | axiales seulement, très faible encombrement axial         | —          |

::: exemple Justifier le choix pour une broche
Une broche de fraiseuse tourne vite, subit l'effort radial de la coupe et un effort axial notable.

1. **Charges** : radiales **et** axiales : le contact radial seul ne convient pas.
2. **Vitesse** : élevée, pas moyenne.
3. Les **rouleaux coniques** conviennent à une vitesse **moyenne** : on les écarte. Reste le **roulement à billes à contact oblique** : radiales et axiales, vitesse importante : c'est le choix justifié.

:::

> ⚠️ Un roulement à contact radial supporte mal une charge axiale importante, et un roulement à contact oblique ne la supporte **que dans un sens**. Dire « il supporte l'axial » sans préciser le sens, c'est la moitié de la justification.

::: verifie Un guidage qui ne reprend que de l'axial
Quel élément choisir pour une charge uniquement axiale, avec peu de place en épaisseur ?

---

La **butée à aiguilles** : charges axiales seulement, faible encombrement axial. La douille à aiguilles, elle, ne reprend que du radial.
:::

::: retenir
Choisir un roulement = **charges** (sens compris) puis **vitesse** : contact oblique pour l'axial à grande vitesse, rouleaux coniques pour l'axial lourd à vitesse moyenne.
:::

## ✖️ Monter une paire de roulements : X, O, arrêts et réglage

Un seul roulement à contact oblique ne bloque l'arbre que dans **un sens** axial.

Question : comment en monter deux pour bloquer dans **les deux sens** — et comment régler leur jeu ?

::: definition Montage en X et montage en O
Les roulements à contact oblique se montent **par paire, en opposition**. La **ligne d'action** de chacun est la droite qui relie ses points de contact. En **montage en X**, les lignes d'action **convergent** vers l'axe ; en **montage en O**, elles **divergent**. Règle du manuel : **généralement**, arbre tournant → montage en X ; moyeu (alésage) tournant → montage en O. Raison : sur un arbre tournant, les bagues intérieures sont serrées sur l'arbre et le réglage se fait par les bagues extérieures, côté logement.
:::

::: figure À gauche, montage en X : les lignes d'action convergent vers l'axe, les bagues extérieures s'appuient sur les couvercles et les bagues intérieures sur la collerette de l'arbre ; la pile de cales entre le couvercle et le logement règle le jeu. À droite, montage en O : elles divergent
<svg viewBox="0 0 580 170"><path d="M20 126 L102 126 L102 150 L20 150 Z" fill="#bfdbfe"/><path d="M20 126 L102 126 L102 150 L20 150 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M102 114 L160 114 L160 150 L102 150 Z" fill="#bfdbfe"/><path d="M102 114 L160 114 L160 150 L102 150 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M160 126 L230 126 L230 150 L160 150 Z" fill="#bfdbfe"/><path d="M160 126 L230 126 L230 150 L160 150 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M74 68 L188 68 L188 98 L74 98 Z" fill="#fde68a"/><path d="M74 68 L188 68 L188 98 L74 98 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M36 68 L66 68 L66 104 L36 104 Z" fill="#e2e8f0"/><path d="M36 68 L66 68 L66 104 L36 104 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M66 98 L74 98 L74 104 L66 104 Z" fill="#e2e8f0"/><path d="M66 98 L74 98 L74 104 L66 104 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="66" y="68" width="8" height="30" fill="#fef3c7" stroke="#0f172a" stroke-width="1.2"/><path d="M68 68 L68 98" fill="none" stroke="#0f172a" stroke-width="1.2" /><path d="M70 68 L70 98" fill="none" stroke="#0f172a" stroke-width="1.2" /><path d="M72 68 L72 98" fill="none" stroke="#0f172a" stroke-width="1.2" /><path d="M188 68 L218 68 L218 104 L188 104 Z" fill="#e2e8f0"/><path d="M188 68 L218 68 L218 104 L188 104 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M74 118 L102 118 L102 126 L74 126 Z" fill="#e2e8f0"/><path d="M74 118 L102 118 L102 126 L74 126 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M74 98 L102 98 L102 106 L74 106 Z" fill="#e2e8f0"/><path d="M74 98 L102 98 L102 106 L74 106 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M160 118 L188 118 L188 126 L160 126 Z" fill="#e2e8f0"/><path d="M160 118 L188 118 L188 126 L160 126 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M160 98 L188 98 L188 106 L160 106 Z" fill="#e2e8f0"/><path d="M160 98 L188 98 L188 106 L160 106 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><circle cx="88.0" cy="112" r="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><path d="M79.9 98 L109.9 150" fill="none" stroke="#b91c1c" stroke-width="1.8" stroke-dasharray="6 3" /><circle cx="174.0" cy="112" r="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><path d="M182.1 98 L152.1 150" fill="none" stroke="#b91c1c" stroke-width="1.8" stroke-dasharray="6 3" /><path d="M10 150 L240 150" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="12 3 3 3" /><path d="M320 114 L374 114 L374 150 L320 150 Z" fill="#bfdbfe"/><path d="M320 114 L374 114 L374 150 L320 150 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M374 126 L488 126 L488 150 L374 150 Z" fill="#bfdbfe"/><path d="M374 126 L488 126 L488 150 L374 150 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M488 114 L530 114 L530 150 L488 150 Z" fill="#bfdbfe"/><path d="M488 114 L530 114 L530 150 L488 150 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M374 68 L488 68 L488 98 L374 98 Z" fill="#fde68a"/><path d="M374 68 L488 68 L488 98 L374 98 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M402 98 L460 98 L460 106 L402 106 Z" fill="#fde68a"/><path d="M402 98 L460 98 L460 106 L402 106 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M374 118 L402 118 L402 126 L374 126 Z" fill="#e2e8f0"/><path d="M374 118 L402 118 L402 126 L374 126 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M374 98 L402 98 L402 106 L374 106 Z" fill="#e2e8f0"/><path d="M374 98 L402 98 L402 106 L374 106 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M460 118 L488 118 L488 126 L460 126 Z" fill="#e2e8f0"/><path d="M460 118 L488 118 L488 126 L460 126 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M460 98 L488 98 L488 106 L460 106 Z" fill="#e2e8f0"/><path d="M460 98 L488 98 L488 106 L460 106 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><circle cx="388.0" cy="112" r="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><path d="M396.1 98 L366.1 150" fill="none" stroke="#b91c1c" stroke-width="1.8" stroke-dasharray="6 3" /><circle cx="474.0" cy="112" r="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><path d="M465.9 98 L495.9 150" fill="none" stroke="#b91c1c" stroke-width="1.8" stroke-dasharray="6 3" /><path d="M310 150 L540 150" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="12 3 3 3" /><text x="130" y="24" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">arbre tournant : montage en X</text><text x="430" y="24" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">moyeu tournant : montage en O</text></svg>
:::

Chaque bague est **arrêtée en translation** : **quatre arrêts** pour une paire (deux bagues intérieures, deux extérieures), dont **un seul règle** le jeu par des **cales de réglage**. Dans le montage en X de la figure, la pile de cales est placée entre le couvercle et le logement : le jeu trop grand se réduit en **retirant de l'épaisseur de cales**, car le couvercle se rapproche et pousse la bague extérieure de son côté vers les billes.

::: exemple Lire un montage type

1. **Ligne d'action** : dans la figure de gauche, les lignes pointillées convergent vers l'axe : montage en **X**.
2. C'est le montage **généralement** retenu pour un **arbre tournant** guidé par deux roulements à contact oblique.
3. **Arrêts** : deux couvercles retiennent les bagues extérieures ; une collerette centrale retient les bagues intérieures : quatre arrêts.
4. **Réglage** : un seul se règle, par les cales sous un couvercle.
5. Au **schéma cinématique**, deux roulements guidant la broche (36) ne forment qu'**une seule liaison pivot** avec le bâti.

:::

> ⚠️ Si les deux roulements sont montés **dans le même sens** (en tandem), leurs lignes d'action sont parallèles : l'arbre est bloqué dans **un seul** sens, et libre dans l'autre. Deux roulements ne suffisent pas, **il faut qu'ils s'opposent**.

::: methode Étudier un guidage en rotation

1. Relever les **charges** (radiales, axiales, sens) et la **vitesse**.
2. Choisir le **type de roulement**.
3. Choisir le **montage** (généralement X pour un arbre tournant, O pour un moyeu tournant).
4. Fixer les **quatre arrêts en translation**, dont un règle.
5. Prévoir le **réglage du jeu**, la **lubrification** et l'**étanchéité**.

:::

::: verifie Deux roulements, un sens
Deux roulements à contact oblique sont montés avec leurs lignes d'action parallèles. Dans quels sens l'arbre est-il retenu ?

---

Dans **un seul sens axial** : tous deux transmettent l'effort dans la même direction. Pour retenir dans les deux sens, il faut les monter **en opposition**, en X ou en O.
:::

::: retenir
Paire de contacts obliques **en opposition** : **X** (généralement arbre tournant, lignes convergentes) ou **O** (généralement moyeu tournant, lignes divergentes) ; **4 arrêts**, **1 réglage** par cales.
:::

## 🛢️ Graisser, étancher, soulever, démonter : ce qui fait durer la tête

La tête ne vit pas que de ses roulements : il faut les **lubrifier**, empêcher la **poussière** d'entrer, et savoir la **soulever** pour la démonter.

Question : quels éléments de la nomenclature s'en chargent, et dans quel ordre démonte-t-on la tête ?

::: definition Les éléments de service
Le **graisseur droit hexagonal M8 (34)**, présent **sept fois**, est un point d'injection de **graisse** : le lubrifiant de la tête est de la **graisse**. Le **joint (46)** assure l'**étanchéité** : il retient le lubrifiant à l'intérieur et laisse la poussière à l'extérieur. Les **cales de réglage** (13, 18, 41) règlent des **positions axiales** et des jeux. L'**anneau de levage mâle M10 (29)** sert à **accrocher la tête** pour la soulever sans l'abîmer.
:::

::: exemple Démonter la tête pour passer en broche horizontale
Activité 1.3 : une fraise disque à trois tailles exige de déposer la tête.

1. **Sécurité** : on enclenche l'**arrêt d'urgence** et on enfile des **gants résistants aux coupures**.
2. On **accroche la tête** par l'**anneau de levage (29)** à un palan : sa masse sera soutenue **avant** qu'on la libère.
3. On **dépose la visserie et les goupilles** qui lient la tête au bâti, avec les **clés appropriées**.
4. On **soulève et dégage** la tête, puis on **range les outils**.

:::

> ⚠️ Libérer les fixations **avant** d'avoir accroché la tête est l'erreur grave : la tête, lourde, n'est plus tenue par rien. Le palan d'abord, la visserie ensuite.

::: verifie Qui fait quoi
Quel élément retient la graisse à l'intérieur et laisse la poussière dehors ? Et quel élément soutient la tête pendant qu'on libère les fixations ?

---

Le **joint (46)** assure l'**étanchéité** ; l'**anneau de levage (29)**, accroché au palan, soutient la tête. Le graisseur, lui, ne retient rien : il **apporte** la graisse.
:::

::: retenir
Graisseur → **graisse** ; joint → **étanchéité** ; cales → **réglage** ; anneau → **levage**. Démontage : **sécurité, levage, visserie, dépose, rangement**.
:::

> 🏆 Tu sais maintenant ce que « assembler » veut dire : chaque pièce de la tête est positionnée par ses formes, retenue par un obstacle ou un serrage, comptée mobilité par mobilité — et tu peux défendre un choix de solution devant un jury. Les pièces ne sont plus des repères sur un plan : ce sont des **liaisons**.
