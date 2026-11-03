# 🎞️ La maquette à came et les synthèses : positionner, fabriquer, contrôler, mouler

> 💡 «Une pièce ne vaut que par la façon dont on la tient, dont on la fabrique et dont on la contrôle. Ce chapitre ferme le thème : un banc à came pour finir le projet, puis deux synthèses pour tout relier.»

Ce chapitre clôt le thème « Obtention des pièces » avec le **projet 2** du manuel, un **banc didactique de mécanisme à came** (p.281 à 284), puis les **deux synthèses** du thème : « obtention des pièces » (p.285-286) et « plasturgie » (p.287-288). On retient ici **huit notions** : la came et son suiveur, le dossier du banc, l'isostatisme, les cotes de fabrication, la mesure par comparaison, les contrôles géométriques, les quatre familles de plastiques et les six procédés de mise en œuvre.

> 🗡️ Le manuel ne donne aucun corrigé, et le projet 2 s'arrête à la nomenclature : seules les règles standard du génie mécanique sont enseignées. Quand une valeur est imprimée dans le manuel, le texte le dit. Quand elle est choisie pour s'entraîner, il parle d'**illustration**. Les schémas sont des **schémas de principe**, redessinés pour expliquer, et la largeur des zones de tolérance y est exagérée.

## 🎞️ La came et son suiveur : un mouvement régulier devient irrégulier

Sur le banc, on tourne un disque gradué à vitesse régulière, et le cadran du comparateur ne suit pas : il reste immobile un moment, puis monte, puis redescend.

Qu'est-ce qui transforme une rotation régulière en un mouvement irrégulier, et comment le mesure-t-on ?

::: definition La commande à came
Une **commande à came** est une **transmission irrégulière** : elle transforme un **mouvement d'entraînement circulaire régulier** en un **mouvement entraîné irrégulier**, avec ou sans pause. Sur le banc :

- la **came** (repère 9) tourne avec le disque gradué (repère 8) : son **contour**, ou **profil**, détermine la loi du mouvement ;
- le **poussoir**, guidé en translation, est l'**élément suiveur** : il reste au contact du profil et en balaie le contour ;
- le **comparateur à cadran** mesure son déplacement ; le disque gradué en degrés donne l'angle de la came.

Le **rayon** du profil est la distance de l'axe de rotation O au point de contact.
:::

::: figure Le banc vu de face. La came en goutte tourne autour de O ; le poussoir (bleu), guidé dans la glissière, appuie sur son profil par le haut. Le cercle de base a le rayon mini, le cercle pointillé extérieur le rayon maxi ; la pointe de la goutte est vers le bas à gauche. Valeurs d'illustration : r mini = 20 mm, r maxi = 28 mm
<svg viewBox="0 0 380 292"><title>Came en goutte et poussoir guidé : rayon mini, rayon maxi et comparateur</title><rect x="172" y="96" width="36" height="34" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="184" y="64" width="12" height="60" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><circle cx="190" cy="40" r="22" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/><line x1="190" y1="23" x2="190" y2="19" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="198.5" y1="25.3" x2="200.5" y2="21.8" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="204.7" y1="31.5" x2="208.2" y2="29.5" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="207" y1="40" x2="211" y2="40" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="204.7" y1="48.5" x2="208.2" y2="50.5" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="198.5" y1="54.7" x2="200.5" y2="58.2" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="190" y1="57" x2="190" y2="61" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="181.5" y1="54.7" x2="179.5" y2="58.2" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="175.3" y1="48.5" x2="171.8" y2="50.5" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="173" y1="40" x2="169" y2="40" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="175.3" y1="31.5" x2="171.8" y2="29.5" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="181.5" y1="25.3" x2="179.5" y2="21.8" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="190" y1="40" x2="197" y2="30" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><line x1="190" y1="62" x2="190" y2="64" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="190 124 196.7 124.4 203.3 125.4 209.8 127.1 216 129.5 222 132.6 227.6 136.2 232.8 140.4 237.6 145.2 241.8 150.4 245.4 156 248.5 162 250.9 168.2 252.6 174.7 253.6 181.3 254 188 253.8 194.7 253.3 201.5 252.3 208.2 250.8 215 248.5 221.8 245.6 228.4 241.9 234.8 237.5 240.7 232.4 246.3 226.7 251.5 220.4 256.2 213.5 260.3 206.1 263.6 198.2 266.3 190 268 181.5 269 172.7 269.2 163.8 268.6 154.9 266.9 146.1 264.1 137.7 259.9 130.1 254.5 123.5 247.9 118.3 240.1 114.6 231.5 112.2 222.6 111.2 213.6 111.1 204.8 111.9 196.2 113.2 188 115.1 180.1 117.8 172.7 121.2 165.7 125.2 159.2 129.7 153.2 134.6 147.8 139.8 142.8 145.2 138.3 151.1 134.4 157.2 131.1 163.5 128.5 170 126.5 176.6 125.1 183.3 124.3" fill="#fde68a" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><circle cx="190" cy="188" r="64" fill="none" stroke="#0f172a" stroke-width="1.0" stroke-dasharray="4 3"/><circle cx="190" cy="188" r="89.6" fill="none" stroke="#0f172a" stroke-width="1.0" stroke-dasharray="4 3"/><circle cx="190" cy="188" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1.0"/><line x1="190" y1="188" x2="254" y2="188" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="254 188 248.5 190.3 248.5 185.7" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="260" y="192" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r mini</text><line x1="190" y1="188" x2="126.6" y2="251.4" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="126.6 251.4 128.9 245.8 132.2 249.1" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="122.6" y="265.4" font-size="9.5" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r maxi</text><text x="168" y="117" font-size="9.5" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">glissière</text><line x1="172" y1="113" x2="170" y2="113" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="204" y="82" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">poussoir</text><text x="220" y="36" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">comparateur</text><text x="182" y="180" font-size="9.5" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text><text x="78" y="88" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">came</text><line x1="84" y1="94" x2="133" y2="150" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/></svg>
:::

Quand le poussoir touche le cercle de base, sa hauteur est la plus basse (rayon mini) ; quand la pointe de la goutte passe sous lui, il est au plus haut (rayon maxi). La différence des deux cercles de la figure est le déplacement du poussoir.

::: exemple Lire le déplacement du poussoir (relevé d'illustration, le manuel ne donne aucune loi de came)
On tourne le disque par pas de 45° et on lit le comparateur, mis à zéro quand le poussoir touche le cercle de base.

| Angle de la came | 0° | 45° | 90° | 135° | 180° | 225° | 270° | 315° | 360° |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Lecture (mm) | 0 | 0 | 0 | 2 | 5 | 8 | 4 | 1 | 0 |

1. **Pause.** De 0° à 90° la lecture reste à 0 : le profil est un arc de cercle centré sur O, son rayon ne change pas, donc le poussoir ne bouge pas.
2. **Levée.** Le maximum est 8 mm : c'est r maxi − r mini = 28 − 20, pas le rayon maxi lui-même.
3. **Irrégularité.** De 90° à 225° (135° de rotation) le poussoir monte de 2, puis 3, puis 3 mm pour 45° chacun : à 30 tr/min, 45° durent 0,25 s, donc il monte à 8 mm/s, puis à 12 mm/s.
4. **Retour.** De 225° à 360° il redescend de 8 mm à 0 : à 360° la lecture vaut de nouveau celle de 0°, car la came a fait un tour complet.

:::

::: piege La levée n'est pas le rayon maxi
Devant r mini = 20 mm et r maxi = 28 mm, on est tenté de répondre « la levée est de 28 mm ». Le poussoir ne part pas de l'axe : il part du cercle de base. Il monte de 28 − 20 = **8 mm**, et c'est ce que lit le comparateur. Tourner à vitesse régulière ne rend pas non plus la montée régulière : la came impose la loi, pas le moteur.
:::

::: propriete Pause et levée
- Pour un poussoir dont l'axe passe par l'axe de la came, la **levée** vaut r maxi − r mini.
- Le poussoir est **en pause** quand le profil est un arc de cercle centré sur l'axe de rotation.
- Le poussoir revient à sa position de départ après un tour : la lecture à 360° est celle de 0°.

Cas limite : une came circulaire, de rayon R mais décalée de e par rapport à l'axe, lève le poussoir de 2e et ne lui laisse jamais de pause.
:::

::: verifie
Une came à poussoir centré a un rayon mini de 15 mm et un rayon maxi de 27 mm ; elle tourne à 20 tr/min. Que vaut la levée, et combien de temps dure un demi-tour ?
---
La levée est r maxi − r mini = 27 − 15 = **12 mm** (le poussoir part du cercle de base, pas de l'axe). À 20 tr/min, un tour dure 60 / 20 = 3 s, donc un demi-tour dure **1,5 s**.
:::

## 📋 Lire le dossier du banc : nomenclature, matières, échelle

Le banc est livré avec quatre documents : un modèle 3D, une vue éclatée, un dessin d'ensemble et une nomenclature. Il faut commander des vis, repérer le disque gradué et savoir en quelle matière les pièces sont faites.

Quel document répond à quelle question ?

::: definition Les documents du dossier
- La **vue éclatée** écarte toutes les pièces le long de leurs axes, avec les **repères 1 à 29** fléchés, sans aucune cote.
- Le **dessin d'ensemble** montre le banc monté à l'échelle **1:3**, en quatre vues : une coupe **A-A**, la vue de face, des coupes **B-B** et **C-C**. Les repères y sont fléchés.
- La **nomenclature** est un tableau à une ligne par repère : **Rep.**, **Nbr.** (le nombre de pièces), **Désignation**, **Matière** et **Observation**.

L'échelle 1:3 est une réduction : 1 mm sur le dessin représente 3 mm sur la pièce.
:::

Extrait de la nomenclature imprimée (29 repères au total) :

| Rep. | Nbr. | Désignation | Matière | Observation |
| ---: | ---: | --- | --- | --- |
| 2 | 1 | Plaque support | PA 6 | |
| 5 | 2 | Coussinet à collerette | CuSn8P | Arbre 14 mm |
| 8 | 1 | Disque gradué | PLA | |
| 9 | 1 | Came | PLA | |
| 11 | 4 | Pied | PLA | |
| 13 | 1 | Semelle | PA 6 | |
| 16 | 1 | Écrou moleté de blocage tambour | PLA | |
| 17 | 1 | Roulement à une rangée de billes à contact radial | | BC 8x22x7. |
| 28 | 6 | Vis à tête cylindrique à six pans creux, M4-16 | | ISO 4762 |

La colonne **Nbr.** se lit avec la colonne **Rep.** : le repère nomme la pièce, le nombre dit combien d'exemplaires il faut.

::: exemple Interroger la nomenclature (réponses lues dans le tableau, échelle en illustration)
1. **Matière du disque gradué (8).** On lit la colonne Matière de la ligne 8 : **PLA**. Le PLA est la matière du filament d'impression 3D du chapitre précédent.
2. **Pièces en PLA.** Repères 8 (1), 9 (1), 11 (4) et 16 (1) : 1 + 1 + 4 + 1 = **7 pièces**, et non 4 : on additionne la colonne Nbr., pas les lignes.
3. **Dimension réelle.** Une pièce mesure 30 mm sur le dessin d'ensemble à l'échelle 1:3 : sa dimension réelle est 30 × 3 = **90 mm**.
4. **Roulement (17).** BC 8x22x7 se lit diamètre intérieur 8, diamètre extérieur 22, largeur 7 (désignation standard d × D × B).

:::

::: piege Un repère n'est pas un nombre de pièces
« Repère 28 : il y a 28 vis », ou « il y a 29 repères, donc 29 pièces ». Le **repère** est une étiquette qui relie une ligne à un fléchage ; le **nombre** est dans la colonne Nbr. Le repère 28 compte **6** vis, et les 29 repères du banc représentent 50 pièces, parce que plusieurs lignes ont un nombre supérieur à 1.
:::

::: propriete Combien de pièces, de quelle matière
- Le nombre de pièces est la **somme de la colonne Nbr.**, pas le nombre de lignes.
- Pour une matière ou une désignation, on additionne les nombres des seules lignes concernées.
- Deux lignes peuvent porter la même désignation : les vis M4-25 des repères 23 et 25 comptent chacune une pièce, soit 2 en tout.

Cas limite : une case Matière **vide** ne veut pas dire « sans matière ». Le manuel ne l'indique pas pour le repère 17 : on ne conclut pas.
:::

::: verifie
Combien de vis M3 le banc compte-t-il, sachant que le repère 14 est une vis M3-6 (2 pièces) et le repère 27 une vis à tête fraisée M3-20 (2 pièces) ? Sur combien de repères ?
---
On additionne les nombres des deux lignes : 2 + 2 = **4 vis M3**, réparties sur **2 repères** (14 et 27). Les têtes sont différentes, mais le filetage est le même : on compte par diamètre de vis.
:::

## 📐 L'isostatisme : six degrés, MIP et MAP

Pour fraiser la semelle du banc, on la pose sur la table de la micro-fraiseuse, puis on en pose une autre, et une autre. Les perçages doivent tomber au même endroit à chaque fois.

Combien de contacts faut-il, et où les placer ?

::: definition Isostatisme, MIP et MAP
L'**isostatisme** est l'élimination des **six degrés de liberté** de la pièce par un ensemble de composants de mise en position, de façon que chaque nouvelle pièce reprenne la **même position** sur son porte-pièce. Dans le repère x, y, z, les six degrés sont trois translations (Tx, Ty, Tz) et trois rotations (Rx, Ry, Rz).

- La **mise en position (MIP)** : les contacts qui suppriment les degrés de liberté.
- Le **maintien en position (MAP)** : le **serrage**, qui garde la pièce contre ses contacts.
:::

::: figure Pièce prismatique en mise en position isostatique. Les points 1, 2 et 3 (bleu, en pointillés : ils sont sous la pièce) forment l'appui plan ; les points 4 et 5 (vert), alignés le long de z sur la face de droite, forment l'appui linéaire ; le point 6 (orange), sur la face de devant, est l'appui ponctuel. Schéma de principe
<svg viewBox="0 0 380 262"><title>Pièce prismatique en mise en position isostatique : appui plan 1, 2, 3, appui linéaire 4, 5, appui ponctuel 6</title><polygon points="70 196 200 196 200 134 70 134" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><polygon points="70 134 200 134 237.8 104.6 107.8 104.6" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><polygon points="200 196 237.8 166.6 237.8 104.6 200 134" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><circle cx="101.2" cy="190.4" r="8" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.4" stroke-dasharray="3 2"/><text x="101.2" y="193.8" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="none" stroke-width="0" stroke-linejoin="round">1</text><circle cx="183.2" cy="190.4" r="8" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.4" stroke-dasharray="3 2"/><text x="183.2" y="193.8" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="none" stroke-width="0" stroke-linejoin="round">2</text><circle cx="163.7" cy="172.9" r="8" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.4" stroke-dasharray="3 2"/><text x="163.7" y="176.3" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="none" stroke-width="0" stroke-linejoin="round">3</text><circle cx="210.8" cy="156.6" r="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.4"/><text x="210.8" y="160" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="none" stroke-width="0" stroke-linejoin="round">4</text><circle cx="228.8" cy="142.6" r="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.4"/><text x="228.8" y="146" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="none" stroke-width="0" stroke-linejoin="round">5</text><circle cx="134" cy="165" r="8" fill="#fed7aa" stroke="#0f172a" stroke-width="1.4"/><text x="134" y="168.4" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="none" stroke-width="0" stroke-linejoin="round">6</text><line x1="34" y1="222" x2="74" y2="222" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="74 222 68.5 224.3 68.5 219.7" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="82" y="226" font-size="10" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><line x1="34" y1="222" x2="34" y2="182" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="34 182 36.3 187.5 31.7 187.5" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="34" y="176" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="34" y1="222" x2="12" y2="239" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="12 239 14.9 233.8 17.8 237.5" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="10" y="250" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">z</text><text x="250" y="62" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1, 2, 3 : appui plan</text><text x="250" y="78" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4, 5 : appui linéaire</text><text x="250" y="94" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6 : appui ponctuel</text><circle cx="240" cy="59" r="4.5" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2"/><circle cx="240" cy="75" r="4.5" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2"/><circle cx="240" cy="91" r="4.5" fill="#fed7aa" stroke="#0f172a" stroke-width="1.2"/></svg>
:::

Le tableau lit la figure : chaque famille de points supprime des degrés précis.

| Contact | Points | Degrés éliminés |
| --- | ---: | --- |
| appui plan (1, 2, 3) | 3 | Ty, Rx, Rz |
| appui linéaire (4, 5) | 2 | Tx, Ry |
| appui ponctuel (6) | 1 | Tz |

::: exemple Deux mises en position imprimées dans le manuel
1. **Pièce prismatique.** 3 + 2 + 1 = **6 points** ; les degrés éliminés sont Ty, Rx, Rz, puis Tx, Ry, puis Tz : les six sont supprimés, donc la pièce est isostatique. Le serrage se fait contre (4, 5).
2. **Pièce cylindrique.** Le manuel donne le même référentiel pour une pièce cylindrique courte et pour une longue : un **centrage long** (points 1, 2, 3, 4), qui élimine Ty, Tz, Ry, Rz, et un **appui ponctuel** (5), qui élimine Tx. Soit 4 + 1 = 5 degrés. (Une pièce courte, comme le disque du chapitre 24, se positionne d'ordinaire par un appui plan et un centrage court ; ce chapitre s'en tient au référentiel imprimé.)
3. **Le sixième.** Reste Rx, la rotation de la pièce autour de son axe : elle ne change la position d'aucune de ses surfaces. Le serrage se fait contre le centrage long.
4. **Surfaces de base.** Les surfaces qui reçoivent les appuis sont les **surfaces de base** (SB). Sur une pièce brute, c'est une **surface de départ** (SD) ; une fois usinée, une face devient une **surface de référence** (SR) pour les phases suivantes.

:::

::: piege Trois points d'appui plan ne suppriment pas trois translations
On lit « 3 points » et on pense « les trois translations ». L'appui plan supprime **une** translation (Ty, perpendiculaire au plan) et **deux** rotations (Rx et Rz, autour des deux axes du plan). C'est le **linéaire**, puis le **ponctuel**, qui suppriment Tx et Tz. Compter les points ne dit pas quels degrés tombent : il faut lire la direction de chaque contact.
:::

::: propriete Ce qu'il faut savoir d'un référentiel
- On n'utilise jamais plus de **six** points : un degré supprimé deux fois rend la pièce **sur-contrainte**.
- Le serrage maintient, il ne supprime aucun degré de liberté.
- On pose l'appui plan sur la plus grande surface, puis le linéaire, puis le ponctuel (règle standard).

Cas limite : une pièce de révolution est bien positionnée à 5 degrés, car la rotation autour de son axe est sans effet sur ses surfaces.
:::

::: verifie
Sur la pièce prismatique de la figure, on retire l'appui plan (1, 2, 3) et on garde les contacts 4, 5 et 6. Combien de degrés de liberté restent libres, et lesquels ?
---
On retire Ty, Rx et Rz de la liste des degrés éliminés : restent éliminés Tx, Ry et Tz. Sont libres **trois degrés** : **Ty, Rx et Rz**. Un contact a besoin d'une direction précise : sans le plan, la pièce n'est plus tenue contre le dessous.
:::

## 🧮 Les cotes de fabrication : machine, outil, appareillage

Le dessin de définition porte des cotes pour le bureau d'études, pas des ordres pour la machine.

Quand on usine une rainure, un épaulement ou un trou, la dimension obtenue vient du déplacement d'un chariot, de la largeur d'une fraise ou de la position d'un montage. D'où vient chacune, et comment les classer ?

::: definition Les trois catégories de cotes de fabrication
Une **cote de fabrication** (Cf) est une dimension que l'on réalise pendant l'usinage. Il y en a trois catégories :

- la **cote machine** (Cm) est réalisée en contrôlant le **déplacement** produit par la machine entre l'outil et la pièce ;
- la **cote outil** (Co) reproduit une **dimension de l'outil** ou un **réglage de l'outil** ;
- la **cote appareillage** (Ca) résulte des dimensions d'un **appareillage** : un montage d'usinage, un canon de perçage.
:::

::: figure Les trois origines d'une cote de fabrication, schémas de principe. À gauche, la machine déplace l'outil de la longueur Cm ; au centre, la fraise à trois tailles fixe elle-même la largeur Co de la rainure ; à droite, le canon de perçage du montage fixe la position Ca du trou
<svg viewBox="0 0 390 214"><title>Trois origines d'une cote de fabrication : déplacement de la machine, largeur de l'outil, position du canon de perçage</title><text x="66" y="16" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">cote machine Cm</text><rect x="18" y="90" width="100" height="40" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><polygon points="64 40 82 40 82 70 73 90 64 70" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><line x1="18" y1="60" x2="18" y2="140" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="3 3"/><line x1="73" y1="90" x2="73" y2="150" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="2 2"/><line x1="73" y1="146" x2="18" y2="146" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="18 146 23.5 143.7 23.5 148.3" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><line x1="18" y1="146" x2="73" y2="146" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="73 146 67.5 148.3 67.5 143.7" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="45.5" y="162" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Cm</text><text x="66" y="188" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">déplacement de l'outil</text><text x="66" y="202" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">réglé sur la machine</text><text x="193" y="16" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">cote outil Co</text><rect x="145" y="90" width="100" height="40" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="183" y="52" width="20" height="52" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="183" y="90" width="20" height="14" fill="#ffffff" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round" stroke-dasharray="3 2"/><line x1="175" y1="146" x2="183" y2="146" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="183 146 177.5 148.3 177.5 143.7" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><line x1="211" y1="146" x2="203" y2="146" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="203 146 208.5 143.7 208.5 148.3" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><line x1="183" y1="106" x2="183" y2="150" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="2 2"/><line x1="203" y1="106" x2="203" y2="150" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="2 2"/><text x="193" y="162" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Co</text><text x="193" y="188" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">largeur de la fraise</text><text x="193" y="202" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">= largeur de la rainure</text><text x="320" y="16" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">cote appareillage Ca</text><rect x="268" y="100" width="108" height="30" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="276" y="72" width="92" height="28" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="276" y="58" width="14" height="42" fill="#94a3b8" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="328" y="66" width="16" height="6" fill="#94a3b8" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="326" y="60" width="4" height="12" fill="#94a3b8" stroke="#0f172a" stroke-width="1.0" stroke-linejoin="round"/><rect x="342" y="60" width="4" height="12" fill="#94a3b8" stroke="#0f172a" stroke-width="1.0" stroke-linejoin="round"/><line x1="336" y1="20" x2="336" y2="72" stroke="#0f172a" stroke-width="3.0" stroke-linecap="round"/><line x1="290" y1="142" x2="336" y2="142" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="336 142 330.5 144.3 330.5 139.7" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><line x1="336" y1="142" x2="290" y2="142" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="290 142 295.5 139.7 295.5 144.3" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><line x1="290" y1="100" x2="290" y2="148" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="2 2"/><line x1="336" y1="72" x2="336" y2="148" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="2 2"/><text x="313" y="158" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Ca</text><text x="320" y="188" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">position du canon</text><text x="320" y="202" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">de perçage du montage</text></svg>
:::

Chaque flèche de la figure est une cote de fabrication, et son origine est écrite dessous : le déplacement, l'outil, le montage.

::: exemple Classer trois dimensions (usinages d'illustration)
1. **Un épaulement dont la longueur est réglée par la course du chariot.** La dimension vient du **déplacement** de la machine : cote machine (Cm).
2. **Une rainure fraisée à la fraise à trois tailles, de la largeur de la fraise.** La dimension est celle de l'**outil** : cote outil (Co).
3. **Deux trous percés à travers un canon de perçage fixé au montage.** La position des trous vient de l'**appareillage** : cote appareillage (Ca).

:::

Il arrive que la cote de fabrication ne coïncide avec aucune cote du dessin de définition : c'est une **cote transférée**. Elle se déduit des cotes du dessin par addition ou soustraction.

::: exemple Transférer une cote (valeurs d'illustration, le manuel n'imprime que ses propres cotes)
La machine règle l'outil depuis la face 1 : Cf1 = 40 ±0,2 jusqu'à la face 3. Le dessin demande **B = 12 ±0,3** entre la face 2 et la face 3. La machine règle les faces 2 et 3 depuis la face 1, pas l'écart B entre elles : elle réalise Cf2, de la face 1 à la face 2.

1. **Nominal.** B = Cf1 − Cf2, donc Cf2 = 40 − 12 = **28**.
2. **Tolérance.** Les IT d'une chaîne s'additionnent : IT de B = IT de Cf1 + IT de Cf2, soit 0,6 = 0,4 + IT de Cf2, donc IT de Cf2 = **0,2**, c'est-à-dire **28 ±0,1**.
3. **Contrôle.** B maxi = 40,2 − 27,9 = 12,3 et B mini = 39,8 − 28,1 = 11,7 : on retrouve 12 ±0,3.

:::

::: piege Reporter la cote du dessin telle quelle
On règle Cf2 à 12 ±0,3, parce que « le dessin dit 12 ±0,3 ». Mais la machine mesure depuis la face 1 : cette cote-là n'est pas B. De plus, ni Cf1 ni Cf2 ne peuvent avoir la tolérance de B : elles se **partagent** son IT, et chacune doit être plus serrée que B.
:::

::: propriete Ce que la cote transférée change
- Le nominal se déduit par différence (ou somme) des cotes de fabrication.
- La tolérance de la cote du dessin est la **somme** des tolérances des cotes de fabrication : il faut donc la partager.
- Cas limite : si la cote de fabrication coïncide avec une cote du dessin, il n'y a pas de transfert, on la reprend telle quelle.
:::

::: verifie
Cf1 = 50 ±0,1 depuis la face 1 jusqu'à la face 3, et le dessin demande B = 15 ±0,25 entre la face 2 et la face 3. Quelle est la cote de fabrication Cf2, de la face 1 à la face 2 ?
---
Nominal : Cf2 = 50 − 15 = 35. IT de B = 0,5 = IT de Cf1 (0,2) + IT de Cf2, donc IT de Cf2 = 0,3 : **Cf2 = 35 ±0,15**. Contrôle : B maxi = 50,1 − 34,85 = 15,25 et B mini = 49,9 − 35,15 = 14,75.
:::

## 🔍 Mesurer par comparaison : le comparateur et la cale étalon

Vingt pièces de 60 mm doivent être contrôlées l'une après l'autre. Un pied à coulisse oblige à relire une graduation à chaque pièce, et l'œil se fatigue.

Comment contrôler vite une série de pièces identiques ?

::: definition Métrologie et contrôle par comparaison
La **métrologie** rassemble les techniques qui permettent de réaliser des mesures, de les interpréter et d'assurer leur fiabilité. Le **contrôle par comparaison** compare chaque pièce à une **cale étalon**, de même longueur nominale, au moyen d'un **comparateur** posé sur un **marbre**. Le comparateur ne mesure pas la longueur : il donne l'**écart** entre la pièce et la cale.
:::

::: figure Montage de contrôle par comparaison, schéma de principe. Le comparateur est réglé à zéro sur la cale étalon, puis déplacé sur la pièce à contrôler ; marbre, cale et pièce reposent sur le même plan
<svg viewBox="0 0 380 258"><title>Contrôle par comparaison : comparateur, pièce à contrôler, cale étalon et marbre</title><rect x="14" y="214" width="352" height="20" fill="#94a3b8" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="190" y="248" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">marbre</text><rect x="34" y="56" width="14" height="158" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="34" y="56" width="98" height="12" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><circle cx="132" cy="44" r="22" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/><line x1="132" y1="27" x2="132" y2="23" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="140.5" y1="29.3" x2="142.5" y2="25.8" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="146.7" y1="35.5" x2="150.2" y2="33.5" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="149" y1="44" x2="153" y2="44" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="146.7" y1="52.5" x2="150.2" y2="54.5" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="140.5" y1="58.7" x2="142.5" y2="62.2" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="132" y1="61" x2="132" y2="65" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="123.5" y1="58.7" x2="121.5" y2="62.2" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="117.3" y1="52.5" x2="113.8" y2="54.5" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="115" y1="44" x2="111" y2="44" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="117.3" y1="35.5" x2="113.8" y2="33.5" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="123.5" y1="29.3" x2="121.5" y2="25.8" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="132" y1="44" x2="132" y2="29" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><line x1="132" y1="66" x2="132" y2="150" stroke="#0f172a" stroke-width="3.0" stroke-linecap="round"/><circle cx="132" cy="152" r="3" fill="#0f172a" stroke="#0f172a" stroke-width="1.0"/><rect x="92" y="154" width="80" height="60" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="240" y="154" width="80" height="60" fill="#fde68a" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="132" y="190" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pièce</text><text x="132" y="202" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">à contrôler</text><text x="280" y="190" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">cale</text><text x="280" y="202" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">étalon</text><text x="172" y="28" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">comparateur</text><line x1="132" y1="130" x2="280" y2="130" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="5 3"/><line x1="268" y1="130" x2="281" y2="130" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><polygon points="281 130 275.5 132.3 275.5 127.7" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><line x1="280" y1="130" x2="280" y2="150" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="5 3"/><text x="206" y="122" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">même longueur nominale</text></svg>
:::

La cale et la pièce posent sur le marbre et ont la même longueur nominale : l'écart lu sur le cadran est donc la différence entre elles.

::: exemple Contrôler une pièce de 60 mm (valeurs d'illustration, 1 division = 0,01 mm)
La cote à respecter est 60 ±0,05 ; on dispose d'une cale étalon de 60,000 mm.

1. **Zéro.** On pose le comparateur sur la cale et on règle le cadran à 0 : la cale vaut 60,000 mm, c'est la référence.
2. **Première pièce.** On pose le comparateur sur la pièce : la lecture est **+0,04**. La pièce mesure 60 + 0,04 = **60,04 mm**, entre 59,95 et 60,05 : elle est **bonne**.
3. **Deuxième pièce.** La lecture est **−0,07** : 60 − 0,07 = **59,93 mm**, sous 59,95 : elle est **rebutée**.

:::

::: piege La lecture n'est pas la longueur
Voir « +0,04 » sur le cadran et noter « la pièce mesure 0,04 mm », ou oublier le signe. Le cadran donne un **écart** par rapport à la cale ; la longueur est **cale + écart**, et un écart négatif est une pièce plus courte que la cale.
:::

::: propriete Ce que le comparateur permet, et ce qu'il exige
- Il ne mesure que de **petits écarts** autour de la longueur de la cale : la cale étalon doit avoir la longueur nominale de la pièce.
- La fiabilité du résultat est celle de la cale : si la cale est fausse, toutes les pièces le sont.
- Cas limite : si l'on déplace le comparateur ou qu'on change de cale, il faut régler de nouveau le zéro.
:::

::: verifie
Une cote est 45 ±0,03 ; la cale étalon vaut 45,000 mm. Le comparateur, remis à zéro sur la cale, lit −0,04 sur une pièce. La pièce est-elle bonne ?
---
La longueur est cale + écart = 45 − 0,04 = **44,96 mm**. La limite basse est 45 − 0,03 = 44,97 : 44,96 est en dessous, la pièce est **rebutée**.
:::

## 📏 Contrôler la forme : parallélisme, perpendicularité, coaxialité

Deux pièces ont la même longueur, au centième près, et pourtant l'une est inclinée : elle ne se monte pas.

Comment contrôler autre chose qu'une longueur ?

::: definition Trois contrôles géométriques
Une **tolérance géométrique** s'écrit dans un cadre : un symbole, une valeur, une **référence** (une lettre).

- Le **parallélisme** (⫽ 0,1 | A) : la surface doit rester entre **deux plans parallèles** à la référence A, distants de 0,1.
- La **perpendicularité** (⊥ 0,1 | B) : la surface doit rester entre deux plans distants de 0,1, **perpendiculaires** à B.
- La **coaxialité** (Ø 0,1 | C) : l'axe de la portée doit rester dans un **cylindre de diamètre 0,1**, d'axe C.
:::

::: figure Les trois zones de tolérance, largeurs exagérées. La zone bleue est l'espace permis : entre deux plans pour le parallélisme (a) et la perpendicularité (b), un cylindre pour la coaxialité (c). Les traits noirs sont une surface réelle, ou un axe réel, qui doit y rester
<svg viewBox="0 0 400 180"><title>Zones de tolérance de parallélisme, de perpendicularité et de coaxialité, largeur de zone exagérée</title><text x="66" y="16" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">parallélisme</text><rect x="14" y="118" width="104" height="18" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="66" y="131" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><line x1="14" y1="46" x2="118" y2="46" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="5 3"/><line x1="14" y1="66" x2="118" y2="66" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="5 3"/><rect x="14" y="46" width="104" height="20" fill="#bfdbfe" fill-opacity="0.55" stroke="none"/><polyline points="14 60 42 53 70 57 98 51 118 55" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><line x1="130" y1="46" x2="130" y2="66" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><polygon points="130 66 127.7 60.5 132.3 60.5" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><line x1="130" y1="66" x2="130" y2="46" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><polygon points="130 46 132.3 51.5 127.7 51.5" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="66" y="156" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">surface entre deux plans</text><text x="66" y="170" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">parallèles à A</text><text x="200" y="16" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">perpendicularité</text><rect x="148" y="118" width="104" height="18" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="160" y="131" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><line x1="186" y1="30" x2="186" y2="118" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="5 3"/><line x1="206" y1="30" x2="206" y2="118" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="5 3"/><rect x="186" y="30" width="20" height="88" fill="#bfdbfe" fill-opacity="0.55" stroke="none"/><polyline points="193 118 197 90 194 62 199 30" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><text x="200" y="156" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">surface entre deux plans</text><text x="200" y="170" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">perpendiculaires à B</text><text x="330" y="16" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">coaxialité</text><circle cx="330" cy="78" r="44" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.6"/><circle cx="330" cy="78" r="20" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="4 3"/><line x1="300" y1="78" x2="360" y2="78" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="9 3 2 3"/><line x1="330" y1="48" x2="330" y2="108" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="9 3 2 3"/><circle cx="337" cy="72" r="3" fill="#0f172a" stroke="#0f172a" stroke-width="1.0"/><text x="330" y="144" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><text x="330" y="112" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">zone Ø</text><text x="330" y="156" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">axe dans un cylindre</text><text x="330" y="170" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">coaxial à l'axe C</text></svg>
:::

Chaque zone bleue est la tolérance de 0,1 du cadre correspondant : la surface ou l'axe réel doit tenir en entier dans la zone.

::: exemple Trois pièces à contrôler (relevés d'illustration, hors le Δx = 0,06 imprimé)
Chaque pièce se pose sur sa référence, sur le marbre, et on promène le comparateur.

1. **Parallélisme ⫽ 0,1 | A.** L'écart entre la plus grande et la plus petite lecture est 0,13 : au-dessus de 0,1, la pièce est **non conforme**.
2. **Perpendicularité ⊥ 0,1 | B.** L'écart relevé est **Δx = 0,06** : en dessous de 0,1, **conforme**.
3. **Coaxialité Ø 0,1 | C.** On tourne la pièce sur la référence : la lecture varie de 0,12 en un tour. L'axe est excentré de la moitié, **0,06** ; la zone, de diamètre 0,1, n'admet que 0,05 : **non conforme**.

:::

::: piege Ø 0,1 n'autorise pas 0,1 d'excentration
Pour la coaxialité, on compare l'excentration à 0,1 et on déclare la pièce bonne. La zone est un **cylindre de diamètre 0,1** : de l'axe de référence au bord, il n'y a que 0,05. Et la lecture du comparateur, qui varie de part et d'autre de l'axe, vaut **deux fois** l'excentration : elle se compare directement à 0,1.
:::

::: propriete Lire un écart
- Parallélisme et perpendicularité : l'écart relevé doit rester inférieur ou égal à la valeur du cadre.
- Coaxialité : l'excentration admise est la **moitié** de la valeur du cadre ; la variation totale du comparateur sur un tour vaut le double de l'excentration, pour une pièce parfaitement ronde.
- Cas limite : un écart exactement égal à la valeur du cadre est encore conforme.
:::

::: verifie
Une coaxialité est donnée Ø 0,08 | C. Le comparateur varie de 0,07 en un tour sur une pièce supposée parfaitement ronde. La pièce est-elle conforme ?
---
L'excentration est 0,07 / 2 = 0,035, et la zone admet 0,08 / 2 = 0,04 : 0,035 est inférieure. Ou bien on compare directement la variation 0,07 à 0,08 : elle est inférieure aussi. La pièce est **conforme**.
:::

## 🧴 Les quatre familles de plastiques

Une brosse à dents, une poignée de casserole, une semelle de sabot, un casque de football américain : quatre objets en « plastique ».

Comment les range-t-on, et qu'est-ce qui les distingue ?

::: definition Plasturgie et les quatre familles
La **plasturgie** est la transformation du plastique en objets par différentes techniques de transformation des polymères (extrusion, injection, impression 3D, thermoformage...). Les matières plastiques se transforment **sous la chaleur et la pression** et se rangent en quatre familles :

- les **thermoplastiques** (TP) se ramollissent à la chaleur, durcissent en refroidissant et peuvent être remis en forme : ils sont **recyclables** ;
- les **thermodurcissables** (TD) prennent une forme **définitive** après polymérisation : solides, très résistants, **non recyclables** ;
- les **élastomères** présentent des propriétés **élastiques** et supportent de **grandes déformations avant rupture** (caoutchoucs, élastomères spéciaux et très spéciaux) ;
- les **composites** sont faits d'**au moins deux matériaux de nature différente**, et possèdent les propriétés de l'ensemble.
:::

| Famille | Objet du manuel | Ce qui la reconnaît |
| --- | --- | --- |
| thermoplastique | brosse à dents | refondable, recyclable |
| thermodurcissable | bouton noir (molette) | forme définitive |
| élastomère | sabot souple | s'étire et reprend sa forme |
| composite | casque | deux matériaux de nature différente |

::: exemple Classer quatre objets (objets d'illustration)
1. Un jouet qui se ramollit sous l'eau très chaude et se remoule : il redevient moulable à chaque chauffage, c'est un **thermoplastique**.
2. Une poignée de casserole qui noircit sans ramollir : sa forme est **définitive**, c'est un **thermodurcissable**.
3. Un joint qui s'étire de plusieurs fois sa longueur puis reprend sa forme : grande déformation sans rupture, c'est un **élastomère**.
4. Une coque en fibres de verre noyées dans une résine : deux matériaux de nature différente, c'est un **composite** (règle standard : une matrice et un renfort).

:::

::: piege Un composite n'est pas un plastique plus solide
« Composite » ne veut pas dire « plus dur » : c'est une façon de **combiner**. Superposer deux couches du même matériau n'en fait pas un, car il faut deux **natures différentes**. Les plastiques les plus souvent associés dans un composite sont les thermodurcissables et les thermoplastiques ; le gain vient de l'association, pas du nom.
:::

::: propriete Du besoin à la famille
- Une pièce à recycler par refonte : **thermoplastique**.
- Une pièce solide, à forme définitive : **thermodurcissable**.
- Une pièce qui se déforme beaucoup sans casser : **élastomère**.
- Une pièce qui cumule des propriétés de plusieurs matériaux : **composite**.

Cas limite : un composite associe souvent un thermodurcissable à des fibres ; on le range parmi les composites, car c'est l'association qui définit sa famille.
:::

::: verifie
Une pièce se ramollit à la chaleur, durcit en refroidissant, et peut être remoulée plusieurs fois. Dans quelle famille la range-t-on, et peut-on la recycler ?
---
Elle redevient moulable à chaque chauffage : c'est un **thermoplastique**. Cette propriété la rend **recyclable**, car on peut la refondre pour en refaire une pièce.
:::

## 🏭 Les six procédés de mise en œuvre

Un prototype unique, un bouchon, une bouteille légère, un bidon, une barquette, une coque : six objets, six façons de les obtenir.

Quel procédé pour quelle pièce, et comment le reconnaître ?

::: definition Les six procédés du manuel
- **Impression 3D** (fabrication additive) : crée un objet en trois dimensions avec une imprimante 3D.
- **Injection** : la matière fluidifiée est injectée sous forte pression dans l'empreinte du moule.
- **Injection-soufflage** : essentiellement pour les thermoplastiques ; flacons à volume très précis et bouteilles légères.
- **Extrusion-soufflage** : combine l'extrusion et le soufflage, à partir d'une **paraison** (un tube de matière extrudé) placée entre deux demi-moules.
- **Thermoformage** : une plaque est chauffée pour la ramollir, puis mise en forme sur un moule ; elle redurcit en refroidissant.
- **Rotomoulage** : pour des corps creux de toutes dimensions ; poudre ou liquide dans un moule fermé et chauffé, mis en double rotation.
:::

::: figure L'extrusion-soufflage en cinq phases. La paraison (orange) est extrudée entre les deux demi-moules ouverts ; les demi-moules se ferment et l'air gonfle la matière, qui épouse l'empreinte ; elle refroidit (bleu), puis la pièce est éjectée. Schéma de principe
<svg viewBox="0 0 400 164"><title>Extrusion-soufflage en cinq phases : paraison, gonflage, formage, refroidissement, éjection</title><rect x="10" y="50" width="24" height="70" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="56" y="50" width="24" height="70" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="34" y="26" width="22" height="14" fill="#94a3b8" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="40" y="40" width="10" height="66" fill="#fdba74" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><text x="45" y="152" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1 paraison</text><rect x="90" y="50" width="32" height="70" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="122" y="50" width="32" height="70" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="112" y="26" width="22" height="14" fill="#94a3b8" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="110" y="50" width="26" height="60" fill="#ffffff" stroke="#0f172a" stroke-width="1.0"/><rect x="114" y="50" width="18" height="56" fill="#fdba74" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><line x1="123" y1="6" x2="123" y2="24" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="123 24 120.7 18.5 125.3 18.5" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="123" y="152" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2 gonflage</text><rect x="168" y="50" width="32" height="70" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="200" y="50" width="32" height="70" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="190" y="26" width="22" height="14" fill="#94a3b8" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="188" y="50" width="26" height="60" fill="#ffffff" stroke="#0f172a" stroke-width="1.0"/><rect x="188" y="50" width="26" height="60" fill="#fdba74" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><line x1="201" y1="6" x2="201" y2="24" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="201 24 198.7 18.5 203.3 18.5" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="201" y="152" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3 formage</text><rect x="246" y="50" width="32" height="70" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="278" y="50" width="32" height="70" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="268" y="26" width="22" height="14" fill="#94a3b8" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="266" y="50" width="26" height="60" fill="#ffffff" stroke="#0f172a" stroke-width="1.0"/><rect x="266" y="50" width="26" height="60" fill="#93c5fd" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><text x="279" y="152" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4 refroidissement</text><rect x="318" y="50" width="18" height="70" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="378" y="50" width="18" height="70" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="346" y="26" width="22" height="14" fill="#94a3b8" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="344" y="98" width="26" height="40" fill="#93c5fd" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><text x="357" y="152" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5 éjection</text></svg>
:::

::: figure Le thermoformage sur une ligne en sept étapes : la plaque vient d'une bobine, elle est préchauffée puis chauffée, formée, découpée, puis les pièces sont empilées et conditionnées. Schéma de principe
<svg viewBox="0 0 380 164"><title>Ligne de thermoformage en sept étapes : bobine, préchauffage, chauffage, formage, découpe, empilage, conditionnement</title><rect x="10" y="28" width="80" height="46" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><text x="50" y="47" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="none" stroke-width="0" stroke-linejoin="round">1</text><text x="50" y="64" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Bobine</text><rect x="102" y="28" width="80" height="46" fill="#fed7aa" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><text x="142" y="47" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="none" stroke-width="0" stroke-linejoin="round">2</text><text x="142" y="64" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Préchauffage</text><rect x="194" y="28" width="80" height="46" fill="#fdba74" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><text x="234" y="47" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="none" stroke-width="0" stroke-linejoin="round">3</text><text x="234" y="64" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Chauffage</text><rect x="286" y="28" width="80" height="46" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><text x="326" y="47" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="none" stroke-width="0" stroke-linejoin="round">4</text><text x="326" y="64" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Formage</text><rect x="56" y="108" width="80" height="46" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><text x="96" y="127" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="none" stroke-width="0" stroke-linejoin="round">5</text><text x="96" y="144" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Découpe</text><rect x="148" y="108" width="80" height="46" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><text x="188" y="127" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="none" stroke-width="0" stroke-linejoin="round">6</text><text x="188" y="144" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Empilage</text><rect x="240" y="108" width="80" height="46" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><text x="280" y="127" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="none" stroke-width="0" stroke-linejoin="round">7</text><text x="280" y="144" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Conditionnement</text><line x1="90" y1="51" x2="102" y2="51" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="102 51 96.5 53.3 96.5 48.7" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><line x1="182" y1="51" x2="194" y2="51" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="194 51 188.5 53.3 188.5 48.7" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><line x1="274" y1="51" x2="286" y2="51" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="286 51 280.5 53.3 280.5 48.7" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><polyline points="326 74 326 88 96 88 96 107" fill="none" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><polygon points="96 108 93 102 99 102" fill="#0f172a" stroke="#0f172a" stroke-width="0.6"/><line x1="136" y1="131" x2="148" y2="131" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="148 131 142.5 133.3 142.5 128.7" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><line x1="228" y1="131" x2="240" y2="131" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="240 131 234.5 133.3 234.5 128.7" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/></svg>
:::

Les deux figures montrent ce qui change : le soufflage part d'un **tube**, le thermoformage d'une **plaque**. L'injection-soufflage part, elle, d'une ébauche injectée.

::: exemple Un procédé par objet (objets et séries d'illustration)
1. **Un prototype unique.** Aucun moule : l'**impression 3D**, couche par couche.
2. **Une barquette à paroi mince.** Elle part d'une plaque : le **thermoformage**. La plaque est chauffée puis formée sur un moule, et la découpe détache la barquette de la plaque (elle laisse des chutes, règle standard).
3. **Une bouteille légère, en grande série.** Le manuel retient l'**injection-soufflage**. On injecte d'abord une ébauche, puis on la souffle.
4. **Un bidon creux.** L'**extrusion-soufflage** : une paraison extrudée, fermée dans un moule, gonflée.
5. **Une grande pièce creuse.** Le **rotomoulage** : la poudre est mise dans un moule fermé et chauffé, mis en double rotation ; il n'y a aucune perte de matériau, toute la matière peut être recyclée à 100 %.

:::

::: piege Injection-soufflage ou extrusion-soufflage : regarder le départ
Les deux noms se terminent par « soufflage » et les deux gonflent la matière dans un moule. Ce qui les sépare est ce que l'on **souffle** : une ébauche **injectée** d'un côté, une **paraison extrudée** de l'autre. De même, le thermoformage ne part pas d'une matière fondue, mais d'une **plaque** que la chaleur ramollit : il faut donc un matériau qui se ramollit à la chaleur, c'est-à-dire un thermoplastique (règle standard).
:::

::: propriete Un coup d'œil sur les six procédés
| Procédé | Départ | Forme obtenue |
| --- | --- | --- |
| Impression 3D | filament, couche par couche | pièce unique ou prototype |
| Injection | matière fluidifiée | pièce moulée dans l'empreinte |
| Injection-soufflage | ébauche injectée | flacon, bouteille légère |
| Extrusion-soufflage | paraison extrudée | corps creux soufflé |
| Thermoformage | plaque chauffée | pièce formée sur un moule |
| Rotomoulage | poudre ou liquide | corps creux de toutes dimensions |

Cas limite : deux procédés peuvent produire une bouteille, l'injection-soufflage et l'extrusion-soufflage ; c'est le départ, ébauche injectée ou paraison extrudée, qui les distingue.
:::

::: verifie
Un pot de yaourt à paroi mince est fabriqué à partir d'une bobine de plaque. Quel procédé, et quelle étape suit immédiatement le formage ?
---
Il part d'une plaque chauffée puis formée sur un moule : c'est le **thermoformage**. Sur la ligne, l'étape qui suit le formage est la **découpe**, qui détache les pots de la plaque avant l'empilage.
:::

## 🧭 La méthode qui reste : huit marches

Devant la fabrication d'une pièce, de la came au plastique, tu reprends toujours cet ordre :

1. **Comprendre le mouvement** : une came transforme une rotation régulière en mouvement irrégulier ; la levée est r maxi − r mini.
2. **Lire le dossier** : repère, nombre, désignation, matière ; on additionne la colonne Nbr., et à l'échelle 1:3 la dimension réelle vaut 3 fois celle du dessin.
3. **Positionner** : six degrés de liberté, appui plan (Ty, Rx, Rz), linéaire (Tx, Ry), ponctuel (Tz) ; le serrage maintient.
4. **Choisir la cote de fabrication** : machine, outil ou appareillage, et transférer en partageant la tolérance.
5. **Contrôler une longueur** : cale étalon + écart du comparateur.
6. **Contrôler une forme** : parallélisme, perpendicularité, et pour la coaxialité l'excentration admise est la moitié de la valeur du cadre.
7. **Ranger le matériau** : thermoplastique, thermodurcissable, élastomère, composite.
8. **Choisir le procédé** : impression 3D, injection, injection-soufflage, extrusion-soufflage, thermoformage, rotomoulage.

::: retenir
Une **came** convertit une rotation régulière en mouvement irrégulier (levée = r maxi − r mini) ; l'**isostatisme** supprime six degrés avec 3 + 2 + 1 points ; une **cote de fabrication** vient de la machine, de l'outil ou de l'appareillage ; un **comparateur** donne l'écart à une cale étalon ; une **coaxialité Ø 0,1** admet 0,05 d'excentration ; les **quatre familles** de plastiques se distinguent par leur comportement, et chacun des **six procédés** par son départ.
:::

> 🏆 Du banc à came à la coque rotomoulée, tu sais positionner, fabriquer, contrôler et mouler : le thème « Obtention des pièces » est bouclé.
