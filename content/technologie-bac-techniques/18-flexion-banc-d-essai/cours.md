# 🏋️ Le banc d'essais de flexion : mesurer la flèche, vérifier la résistance

> 💡 « Une poutre qui plie ne casse pas pour autant : elle prévient. La flèche, lue au comparateur, et la contrainte, calculée, disent si elle tient, et de combien elle peut encore s'en servir. »

Ce chapitre est la deuxième activité du thème **Comportement des solides déformables**. Le support est un **banc d'essais de flexion**, monté sur le même bâti bleu à deux montants et deux colonnes que le banc de torsion : une éprouvette repose sur **deux appuis mobiles** A et B, un **comparateur à cadran** touche son milieu, des masses sont suspendues. Les charges disponibles sont un support de **2,5 N**, deux masses de **5 N** et une masse de **10 N**. Les éprouvettes sont trois barres d'acier de sections différentes, et trois barres de section circulaire (Ø 8 mm, longueur 600 mm) en acier, en aluminium et en laiton.

Le travail a deux temps. La **partie A** étudie la flèche : comment elle dépend de la charge F, puis de la portée L. La **partie B** valide une poutre de section circulaire (Ø 8 mm, acier) par trois chemins : le calcul, la simulation avec le logiciel **Winflex**, et la mesure sur le banc. Deux compétences sont travaillées, **CD 1.7** et **CD 2.1**.

> 🗡️ Les schémas de ce cours sont des **schémas de principe**, redessinés pour expliquer ; le manuel ne donne aucun corrigé. Les formules de résistance des matériaux que les pages 222 à 226 n'impriment pas (moment quadratique, flèche) sont des formules **standard**, annoncées comme telles ; deux autres, **σmax** et **Rpe**, sont imprimées à la synthèse du thème (p.251) et sont reprises ici parce que la partie B ne se calcule pas sans elles. Quand une valeur est choisie pour s'entraîner, le cours parle d'**illustration**. Les exemples des sections 1 à 4 utilisent une **éprouvette d'illustration** : acier (E = 210 GPa, la valeur que le manuel donne pour l'acier de la partie B), section rectangulaire **20 × 6 mm**, longueur 600 mm ; le manuel ne donne pas les dimensions de ses éprouvettes rectangulaires. Les lettres se notent à plat : IGz pour le moment quadratique, Mf pour le moment fléchissant, σmax, Re et Rpe.

## 🎯 Poser le problème : la poutre, sa charge, sa flèche

Sur le banc, tu poses l'éprouvette sur les appuis et tu accroches une masse en son milieu : la barre plie, de très peu, mais assez pour que le comparateur le mesure. L'activité demande de déterminer, puis de vérifier, qu'une poutre ainsi chargée résiste et ne se déforme pas trop.

Avant de calculer, comment nommer ce que le banc impose et ce qu'il mesure ?

::: definition La flexion, la portée et la flèche
Une poutre posée sur deux appuis et chargée perpendiculairement à sa ligne moyenne se courbe : elle est sollicitée en **flexion plane simple**.

- **A** est un appui articulé, **B** un appui à rouleaux : B laisse la poutre glisser le long de son axe.
- La **portée L** est la distance entre les appuis A et B.
- La **déformée** est la forme que prend la ligne moyenne sous charge.
- La **flèche f** est le déplacement vertical d'un point de la poutre, en mm, lu au comparateur.

:::

::: figure La poutre sur ses deux appuis A et B. En pointillés, la position sans charge ; en trait plein, la déformée sous la charge F. La cote L est la portée, la cote f la flèche au milieu. Le dessin exagère la flèche, qui se compte en dixièmes de millimètre sur le banc
<svg viewBox="0 0 340 150"><title>Poutre sur deux appuis A et B, chargée au milieu : portée L, flèche f</title><line x1="40" y1="70" x2="300" y2="70" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="5 4" /><polygon points="40 71 29 86 51 86" fill="#fde68a" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><line x1="23" y1="86" x2="57" y2="86" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><circle cx="300" cy="78.5" r="7.5" fill="#fde68a" stroke="#0f172a" stroke-width="1.6" /><line x1="283" y1="86" x2="317" y2="86" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><polyline points="40 70 42.6 70.8 45.2 71.7 47.8 72.5 50.4 73.4 53 74.2 55.6 75 58.2 75.8 60.8 76.7 63.4 77.5 66 78.3 68.6 79.1 71.2 79.9 73.8 80.7 76.4 81.5 79 82.2 81.6 83 84.2 83.7 86.8 84.5 89.4 85.2 92 85.9 94.6 86.6 97.2 87.3 99.8 88 102.4 88.6 105 89.2 107.6 89.9 110.2 90.5 112.8 91.1 115.4 91.6 118 92.2 120.6 92.7 123.2 93.2 125.8 93.7 128.4 94.2 131 94.6 133.6 95 136.2 95.4 138.8 95.8 141.4 96.1 144 96.4 146.6 96.7 149.2 97 151.8 97.2 154.4 97.4 157 97.6 159.6 97.7 162.2 97.9 164.8 97.9 167.4 98 170 98 172.6 98 175.2 97.9 177.8 97.9 180.4 97.7 183 97.6 185.6 97.4 188.2 97.2 190.8 97 193.4 96.7 196 96.4 198.6 96.1 201.2 95.8 203.8 95.4 206.4 95 209 94.6 211.6 94.2 214.2 93.7 216.8 93.2 219.4 92.7 222 92.2 224.6 91.6 227.2 91.1 229.8 90.5 232.4 89.9 235 89.2 237.6 88.6 240.2 88 242.8 87.3 245.4 86.6 248 85.9 250.6 85.2 253.2 84.5 255.8 83.7 258.4 83 261 82.2 263.6 81.5 266.2 80.7 268.8 79.9 271.4 79.1 274 78.3 276.6 77.5 279.2 76.7 281.8 75.8 284.4 75 287 74.2 289.6 73.4 292.2 72.5 294.8 71.7 297.4 70.8 300 70" fill="none" stroke="#0f172a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" /><polyline points="40 70 42.6 70.8 45.2 71.7 47.8 72.5 50.4 73.4 53 74.2 55.6 75 58.2 75.8 60.8 76.7 63.4 77.5 66 78.3 68.6 79.1 71.2 79.9 73.8 80.7 76.4 81.5 79 82.2 81.6 83 84.2 83.7 86.8 84.5 89.4 85.2 92 85.9 94.6 86.6 97.2 87.3 99.8 88 102.4 88.6 105 89.2 107.6 89.9 110.2 90.5 112.8 91.1 115.4 91.6 118 92.2 120.6 92.7 123.2 93.2 125.8 93.7 128.4 94.2 131 94.6 133.6 95 136.2 95.4 138.8 95.8 141.4 96.1 144 96.4 146.6 96.7 149.2 97 151.8 97.2 154.4 97.4 157 97.6 159.6 97.7 162.2 97.9 164.8 97.9 167.4 98 170 98 172.6 98 175.2 97.9 177.8 97.9 180.4 97.7 183 97.6 185.6 97.4 188.2 97.2 190.8 97 193.4 96.7 196 96.4 198.6 96.1 201.2 95.8 203.8 95.4 206.4 95 209 94.6 211.6 94.2 214.2 93.7 216.8 93.2 219.4 92.7 222 92.2 224.6 91.6 227.2 91.1 229.8 90.5 232.4 89.9 235 89.2 237.6 88.6 240.2 88 242.8 87.3 245.4 86.6 248 85.9 250.6 85.2 253.2 84.5 255.8 83.7 258.4 83 261 82.2 263.6 81.5 266.2 80.7 268.8 79.9 271.4 79.1 274 78.3 276.6 77.5 279.2 76.7 281.8 75.8 284.4 75 287 74.2 289.6 73.4 292.2 72.5 294.8 71.7 297.4 70.8 300 70" fill="none" stroke="#bfdbfe" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" /><line x1="170" y1="6" x2="170" y2="82" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" /><polygon points="170 90 166.5 82 173.5 82" fill="#0f6e56" stroke="#0f6e56" stroke-width="1" stroke-linejoin="round" /><text x="184" y="22" font-size="14" font-weight="700" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text><line x1="170" y1="98" x2="222" y2="98" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4 3" /><line x1="214" y1="80" x2="214" y2="90" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round" /><polygon points="214 98 210.5 90 217.5 90" fill="#0f6e56" stroke="#0f6e56" stroke-width="1" stroke-linejoin="round" /><line x1="214" y1="88" x2="214" y2="78" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round" /><polygon points="214 70 217.5 78 210.5 78" fill="#0f6e56" stroke="#0f6e56" stroke-width="1" stroke-linejoin="round" /><text x="222" y="88" font-size="14" font-weight="700" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f</text><text x="40" y="106" font-size="14" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="300" y="106" font-size="14" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><line x1="40" y1="130" x2="300" y2="130" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="40" y1="125" x2="40" y2="135" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="300" y1="125" x2="300" y2="135" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="170" y="124" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">L</text></svg>
:::

Dans la figure, **L** est la cote horizontale entre A et B, **f** la cote verticale entre les pointillés et la poutre déformée : ce sont les deux grandeurs que le banc permet de faire varier et de lire.

::: exemple Lire un essai
Une éprouvette de 600 mm est posée sur A et B écartés de 400 mm. Une charge F = 10 N (masse ajoutée, comparateur remis à zéro support en place) est accrochée en son milieu ; le palpeur du comparateur est lui aussi au milieu et affiche **0,176 mm** (valeur d'illustration, éprouvette 20 × 6 mm).

1. La portée est la distance entre les appuis : **L = 400 mm**. La longueur de l'éprouvette (600 mm) n'y entre pas.
2. La charge est au milieu de la portée, donc à 200 mm de chaque appui.
3. Le palpeur est sous la charge : le comparateur donne la flèche à cet endroit, **f = 0,176 mm**. C'est le déplacement vertical du milieu de la poutre.

:::

::: piege La portée n'est pas la longueur de l'éprouvette
L'éprouvette mesure 600 mm, mais les appuis sont réglés à 400 mm : si tu écris L = 600 mm, tu mesures la barre au lieu de mesurer l'écart entre ses appuis. La portée se règle sur le banc ; la longueur de la barre ne change pas quand on déplace A ou B.
:::

::: propriete Où lire la flèche
Quand la charge est au **milieu** de la portée, le point le plus bas de la poutre est lui aussi au milieu : le palpeur y lit la flèche **maximale**. Cas limite : si la charge est ailleurs, le point le plus bas se déplace (section 8).
:::

::: verifie
Une éprouvette de 600 mm repose sur des appuis écartés de 500 mm, la charge F est au milieu. Que valent la portée L et la distance de F à chaque appui ?
---

La portée est la distance entre appuis : **L = 500 mm**, et non la longueur de la barre. La charge est au milieu de cette portée, donc à 500 / 2 = **250 mm** de chaque appui.
:::

## 📐 Le moment quadratique : pourquoi une règle plie à plat et non sur chant

Prends une règle plate de 20 mm de large et 6 mm d'épaisseur, appuyée à ses deux bouts, et pousse en son milieu. À plat, elle plie facilement ; posée sur sa tranche, elle résiste beaucoup mieux, alors que c'est la même matière et la même quantité de matière.

Quelle grandeur de la section explique cette différence, et comment la calcule-t-on ? Le manuel demande de relever b et h, puis de calculer IGz.

::: definition Le moment quadratique IGz
Le **moment quadratique** de la section par rapport à l'axe **Gz**, noté **IGz**, s'exprime en **mm⁴**. Gz est l'**axe neutre** : il passe par le centre de gravité G de la section et il est perpendiculaire au plan de la charge. Plus la matière est loin de cet axe, plus IGz est grand, et moins la poutre plie.

Formules standard (le manuel les suppose connues) :

$$ IGz = b × h³ / 12 $$

pour un rectangle, où **b** est la dimension parallèle à Gz et **h** la dimension dans le sens de la charge ;

$$ IGz = π × d⁴ / 64 $$

pour un cercle de diamètre d.
:::

::: figure La même section de 20 × 6 mm posée à plat (à gauche) et sur chant (à droite). La charge F est toujours verticale ; l'axe neutre Gz reste horizontal. À plat, la hauteur h dans le sens de la charge vaut 6 mm ; sur chant, elle vaut 20 mm
<svg viewBox="0 0 340 208"><title>Même section 20 par 6 posée à plat ou sur chant : b, h et axe Gz</title><rect x="20" y="82" width="120" height="36" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" /><line x1="12" y1="100" x2="142" y2="100" stroke="#0f6e56" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="6 4" /><circle cx="80" cy="100" r="3" fill="#0f6e56" /><text x="18" y="94" font-size="12" font-weight="700" text-anchor="end" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Gz</text><text x="80" y="200" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">à plat</text><rect x="252" y="40" width="36" height="120" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" /><line x1="246" y1="100" x2="304" y2="100" stroke="#0f6e56" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="6 4" /><circle cx="270" cy="100" r="3" fill="#0f6e56" /><text x="306" y="96" font-size="12" font-weight="700" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Gz</text><text x="270" y="200" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">sur chant</text><line x1="80" y1="12" x2="80" y2="52" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round" /><polygon points="80 60 76.5 52 83.5 52" fill="#0f6e56" stroke="#0f6e56" stroke-width="1" stroke-linejoin="round" /><text x="90" y="28" font-size="13" font-weight="700" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text><line x1="270" y1="12" x2="270" y2="28" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round" /><polygon points="270 36 266.5 28 273.5 28" fill="#0f6e56" stroke="#0f6e56" stroke-width="1" stroke-linejoin="round" /><text x="280" y="28" font-size="13" font-weight="700" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text><line x1="20" y1="134" x2="140" y2="134" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="20" y1="129" x2="20" y2="139" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="140" y1="129" x2="140" y2="139" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="80" y="131" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">b = 20</text><line x1="144" y1="82" x2="152" y2="82" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="144" y1="118" x2="152" y2="118" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="148" y1="82" x2="148" y2="118" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="156" y="104" font-size="11" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">h = 6</text><line x1="252" y1="182" x2="288" y2="182" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="252" y1="177" x2="252" y2="187" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="288" y1="177" x2="288" y2="187" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="270" y="176" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">b = 6</text><line x1="234" y1="40" x2="242" y2="40" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="234" y1="160" x2="242" y2="160" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="238" y1="40" x2="238" y2="160" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="232" y="104" font-size="11" font-weight="600" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">h = 20</text></svg>
:::

Sur la figure, **h** est toujours la cote parallèle à la flèche verte de F, et **b** la cote parallèle à Gz : c'est h, élevée au cube, qui pèse dans la formule.

::: exemple Calculer IGz de l'éprouvette d'illustration
Section 20 × 6 mm, deux positions.

1. **À plat** : le côté de 20 mm est parallèle à Gz, donc b = 20 mm ; le côté de 6 mm est dans le sens de la charge, donc h = 6 mm.

$$ IGz = 20 × 6³ / 12 = 20 × 216 / 12 = 360 mm⁴ $$

2. **Sur chant** : on échange les rôles, b = 6 mm et h = 20 mm.

$$ IGz = 6 × 20³ / 12 = 6 × 8 000 / 12 = 4 000 mm⁴ $$

3. Comparaison : 4 000 / 360 ≈ 11,1, soit (20 / 6)². Sur chant, la même barre est environ **onze fois** plus raide.

:::

::: piege h n'est pas la plus grande dimension
Pour la barre posée à plat, écrire h = 20 mm « parce que 20 est le grand côté » donne 4 000 mm⁴ au lieu de 360 mm⁴. h se lit dans le **sens de la charge**, quelle que soit sa taille : à plat, c'est le petit côté.
:::

::: propriete IGz croît comme h³
Pour un rectangle, IGz est proportionnel à b et à **h³** : doubler b double IGz, doubler h le multiplie par 8. Pour un cercle, IGz est proportionnel à **d⁴** : doubler d le multiplie par 16. Cas du manuel : la barre ronde de Ø 8 mm a IGz = π × 8⁴ / 64 = 64 × π ≈ 201,1 mm⁴.
:::

::: verifie
Une section de 10 × 4 mm est posée à plat. Calcule IGz.
---

À plat, la dimension dans le sens de la charge est le petit côté : h = 4 mm, et b = 10 mm. IGz = 10 × 4³ / 12 = 10 × 64 / 12 ≈ **53,3 mm⁴**.
:::

## 📈 La flèche et la charge : f = f(F)

Appuis réglés à 400 mm, tu accroches 5 N, puis 10, 15 et 20 N au milieu, et tu notes chaque fois la flèche. Si tu doubles la charge, la flèche double-t-elle ? Et comment le démontrer avec quatre mesures ?

::: figure Les quatre mesures (F, f) du tableau ci-dessous, placées dans le repère. Elles sont alignées sur une droite qui passe par l'origine : c'est la signature d'une proportionnalité
<svg viewBox="0 0 340 240"><title>Flèche f en fonction de la charge F : points alignés sur une droite passant par l'origine</title><line x1="112.5" y1="200" x2="112.5" y2="30" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="112.5" y1="200" x2="112.5" y2="204" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="112.5" y="216" font-size="10" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="175" y1="200" x2="175" y2="30" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="175" y1="200" x2="175" y2="204" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="175" y="216" font-size="10" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="237.5" y1="200" x2="237.5" y2="30" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="237.5" y1="200" x2="237.5" y2="204" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="237.5" y="216" font-size="10" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">15</text><line x1="300" y1="200" x2="300" y2="30" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="300" y1="200" x2="300" y2="204" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="300" y="216" font-size="10" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="50" y1="160" x2="310" y2="160" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="46" y1="160" x2="50" y2="160" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="43" y="163.5" font-size="10" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,1</text><line x1="50" y1="120" x2="310" y2="120" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="46" y1="120" x2="50" y2="120" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="43" y="123.5" font-size="10" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,2</text><line x1="50" y1="80" x2="310" y2="80" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="46" y1="80" x2="50" y2="80" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="43" y="83.5" font-size="10" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,3</text><line x1="50" y1="40" x2="310" y2="40" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="46" y1="40" x2="50" y2="40" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="43" y="43.5" font-size="10" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,4</text><line x1="50" y1="200" x2="316" y2="200" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><line x1="50" y1="200" x2="50" y2="24" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><line x1="50" y1="200" x2="300" y2="58.9" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" /><circle cx="112.5" cy="164.8" r="4.2" fill="#0f172a" /><circle cx="175" cy="129.6" r="4.2" fill="#0f172a" /><circle cx="237.5" cy="94" r="4.2" fill="#0f172a" /><circle cx="300" cy="58.8" r="4.2" fill="#0f172a" /><text x="180" y="234" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F (N)</text><text x="54" y="18" font-size="12" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f (mm)</text><text x="306" y="50.9" font-size="10" font-weight="600" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">droite</text></svg>
:::

Chaque point de la figure est une colonne du tableau (abscisse F, ordonnée f), et la droite tracée est la loi f = k × F que l'exemple va chercher.

::: exemple Tester la proportionnalité de f et de F
Mesures d'illustration, éprouvette 20 × 6 mm à plat, L = 400 mm (précision d'un millième de millimètre, plus fine que celle d'un vrai cadran) :

| F (N)        | 5      | 10     | 15     | 20     |
| ------------ | ------ | ------ | ------ | ------ |
| f (mm)       | 0,088  | 0,176  | 0,265  | 0,353  |
| f / F (mm/N) | 0,0176 | 0,0176 | 0,0177 | 0,0177 |

1. On calcule le rapport f / F pour chaque charge : c'est la seule façon de voir si f suit F proportionnellement.
2. Les quatre rapports sont égaux à la précision des mesures près : **f est proportionnelle à F**, avec un coefficient d'environ **0,0176 mm/N**.
3. On prévoit : pour F = 12 N, f ≈ 12 × 0,0176 ≈ 0,21 mm.

:::

::: piege Le support de charges pèse aussi
Le support de 2,5 N est déjà accroché avant la première masse. Principe de l'essai, que le manuel ne détaille pas : on remet le comparateur à zéro **avec le support en place**. Sinon la flèche mesurée correspond à F + 2,5 N, et les points ne passent plus par l'origine.
:::

::: propriete La flèche est proportionnelle à la charge
$$ f = k × F $$

k s'exprime en mm/N : c'est la pente de la droite, et elle dépend de la portée, de la section et du matériau (sections suivantes). Cas limites : F = 0 donne f = 0 ; et la proportionnalité vaut tant que le métal reste dans son domaine élastique, c'est-à-dire sans déformation permanente (voir la limite élastique Re, section 7).
:::

::: verifie
Avec k = 0,0176 mm/N, quelle charge donne une flèche de 0,25 mm ?
---

f = k × F donne F = f / k = 0,25 / 0,0176 ≈ **14,2 N**. On a divisé, car la flèche est proportionnelle à la charge : on retrouve la charge en divisant la flèche par la pente.
:::

## 📏 La flèche et la portée : f = f(L)

Charge fixée à 10 N, tu écartes les appuis à 200, 300, 400 puis 500 mm. La flèche grandit, c'est clair ; mais comment : comme L, comme L², comme L³, comme 1/L ? Le manuel te laisse choisir entre quatre formules, f = k/L³, k·L³, k/L ou k·L.

Une courbe qui monte ne dit pas laquelle. Il faut une grandeur dont le rapport avec f reste constant.

::: figure Les mêmes quatre mesures tracées en fonction de L (à gauche) et de L³ (à droite). À gauche les points forment une courbe qui se redresse de plus en plus ; à droite, ils sont alignés sur une droite qui passe par l'origine
<svg viewBox="0 0 340 236"><title>Mêmes mesures tracées en fonction de L (une courbe) et de L cube (une droite)</title><line x1="86" y1="190" x2="86" y2="40" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="86" y1="190" x2="86" y2="194" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="86" y="206" font-size="10" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">200</text><line x1="130" y1="190" x2="130" y2="40" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="130" y1="190" x2="130" y2="194" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="130" y="206" font-size="10" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">400</text><line x1="42" y1="152.5" x2="157" y2="152.5" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="38" y1="152.5" x2="42" y2="152.5" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="35" y="156" font-size="10" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,1</text><line x1="42" y1="115" x2="157" y2="115" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="38" y1="115" x2="42" y2="115" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="35" y="118.5" font-size="10" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,2</text><line x1="42" y1="77.5" x2="157" y2="77.5" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="38" y1="77.5" x2="42" y2="77.5" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="35" y="81" font-size="10" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,3</text><line x1="42" y1="190" x2="163" y2="190" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><line x1="42" y1="190" x2="42" y2="34" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><polyline points="42 190 44.2 190 46.4 190 48.6 190 50.8 189.9 53 189.9 55.2 189.8 57.4 189.6 59.6 189.5 61.8 189.2 64 189 66.2 188.6 68.4 188.2 70.6 187.7 72.8 187.2 75 186.5 77.2 185.8 79.4 184.9 81.6 184 83.8 182.9 86 181.7 88.2 180.4 90.4 179 92.6 177.4 94.8 175.7 97 173.9 99.2 171.8 101.4 169.7 103.6 167.3 105.8 164.8 108 162.1 110.2 159.2 112.4 156.1 114.6 152.9 116.8 149.4 119 145.7 121.2 141.8 123.4 137.7 125.6 133.3 127.8 128.7 130 123.9 132.2 118.8 134.4 113.4 136.6 107.8 138.8 102 141 95.8 143.2 89.4 145.4 82.7 147.6 75.7 149.8 68.4 152 60.8" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linejoin="round" /><circle cx="86" cy="181.8" r="3.8" fill="#0f172a" /><circle cx="108" cy="162.2" r="3.8" fill="#0f172a" /><circle cx="130" cy="124" r="3.8" fill="#0f172a" /><circle cx="152" cy="61" r="3.8" fill="#0f172a" /><text x="102" y="222" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">L (mm)</text><text x="44" y="30" font-size="11" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f (mm)</text><text x="100" y="12" font-size="11" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f(L) : une courbe</text><line x1="257" y1="190" x2="257" y2="40" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="257" y1="190" x2="257" y2="194" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="257" y="206" font-size="10" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">50</text><line x1="302" y1="190" x2="302" y2="40" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="302" y1="190" x2="302" y2="194" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="302" y="206" font-size="10" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">100</text><line x1="212" y1="152.5" x2="327" y2="152.5" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="208" y1="152.5" x2="212" y2="152.5" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="205" y="156" font-size="10" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,1</text><line x1="212" y1="115" x2="327" y2="115" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="208" y1="115" x2="212" y2="115" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="205" y="118.5" font-size="10" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,2</text><line x1="212" y1="77.5" x2="327" y2="77.5" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round" /><line x1="208" y1="77.5" x2="212" y2="77.5" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="205" y="81" font-size="10" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,3</text><line x1="212" y1="190" x2="333" y2="190" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><line x1="212" y1="190" x2="212" y2="34" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><line x1="212" y1="190" x2="324.5" y2="60.8" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" /><circle cx="219.2" cy="181.8" r="3.8" fill="#0f172a" /><circle cx="236.3" cy="162.2" r="3.8" fill="#0f172a" /><circle cx="269.6" cy="124" r="3.8" fill="#0f172a" /><circle cx="324.5" cy="61" r="3.8" fill="#0f172a" /><text x="272" y="222" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">L³ (10⁶ mm³)</text><text x="214" y="30" font-size="11" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f (mm)</text><text x="270" y="12" font-size="11" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f(L³) : une droite</text></svg>
:::

Le panneau de droite a pour abscisse L³ (en millions de mm³) : une droite y signifie que f est proportionnelle à L³, pas à L.

::: exemple Choisir la bonne formule
Mesures d'illustration (éprouvette 20 × 6 mm à plat, F = 10 N) :

| L (mm)             | 200   | 300   | 400   | 500   |
| ------------------ | ----- | ----- | ----- | ----- |
| L³ (10⁶ mm³)       | 8     | 27    | 64    | 125   |
| f (mm)             | 0,022 | 0,074 | 0,176 | 0,344 |
| f / L (10⁻⁴)       | 1,10  | 2,47  | 4,40  | 6,88  |
| f / L³ (10⁻⁹ mm⁻²) | 2,75  | 2,74  | 2,75  | 2,75  |

1. On teste f = k × L : le rapport f / L n'est pas constant, il est multiplié par plus de 6 entre 200 et 500 mm. Cette formule est écartée, de même que k / L (f diminuerait quand L augmente).
2. On teste f = k × L³ : le rapport f / L³ vaut 2,75 × 10⁻⁹ à chaque ligne. Il est constant.
3. La bonne case à cocher est donc **f = k × L³**.

:::

::: piege Une courbe qui monte n'est pas une droite
Voir f croître avec L ne prouve pas f = k × L : une droite ne se reconnaît que si le rapport f / L reste constant, ou si les points sont alignés avec l'origine. Ici, f / L varie de 1,10 à 6,88, et les points de f(L) forment une courbe qui se redresse.
:::

::: propriete La flèche croît comme L³, et dépend de E et de IGz
Pour une charge F au milieu, la formule standard (non imprimée dans les pages 222 à 226) réunit tout ce qu'on a vu :

$$ f = F × L³ / (48 × E × IGz) $$

Les valeurs d'illustration du chapitre sont calculées avec elle (E = 210 000 MPa, IGz = 360 mm⁴). Elle dit que f est proportionnelle à F, à L³, et inversement proportionnelle à E et à IGz. Cas limites : doubler L multiplie f par 8 ; à portée et section égales, une éprouvette d'aluminium (E ≈ 70 GPa, valeur usuelle) plie trois fois plus que l'acier ; sur chant, la barre de la section précédente plie environ onze fois moins qu'à plat.
:::

::: verifie
Les appuis passent de 300 mm à 600 mm, tout le reste étant identique. Par combien la flèche est-elle multipliée ?
---

f est proportionnelle à L³ : L est multipliée par 2, donc f par 2³ = **8**. Doubler la portée ne double pas la flèche, elle devient huit fois plus grande.
:::

## ⚖️ Les réactions d'appuis et le moment fléchissant

La partie B charge une poutre de 500 mm avec F = 15 N posée au point C, à 200 mm de A et à 300 mm de B. Les deux appuis portent-ils la charge à parts égales ?

Et à quel endroit la poutre est-elle le plus sollicitée en flexion ? Il faut deux outils : les réactions d'appuis, puis le moment fléchissant.

::: definition Réactions d'appuis et moment fléchissant
Les **réactions d'appuis** RA et RB sont les forces verticales que les appuis exercent sur la poutre pour la maintenir en équilibre.

Le **moment fléchissant** Mf dans une section est le moment, par rapport à cette section, des forces situées d'un seul côté de celle-ci. Il se calcule ici en N·mm et il est pris en valeur absolue : son signe dépend d'une convention que le manuel n'imprime pas.
:::

::: figure La poutre de la partie B : F en C, les réactions RA et RB (leurs longueurs sont proportionnelles à 9 N et 6 N), puis, dessous, le moment fléchissant le long de la poutre : nul en A et en B, maximal en C
<svg viewBox="0 0 340 305"><title>Poutre AB chargée en C : réactions RA et RB, et diagramme du moment fléchissant</title><line x1="45" y1="62" x2="295" y2="62" stroke="#0f172a" stroke-width="5" stroke-linecap="round" /><line x1="45" y1="62" x2="295" y2="62" stroke="#bfdbfe" stroke-width="2.4" stroke-linecap="round" /><polygon points="45 65 34 79 56 79" fill="#fde68a" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><line x1="28" y1="79" x2="62" y2="79" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><circle cx="295" cy="72" r="7" fill="#fde68a" stroke="#0f172a" stroke-width="1.6" /><line x1="278" y1="79" x2="312" y2="79" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><line x1="145" y1="8" x2="145" y2="51" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" /><polygon points="145 59 141.5 51 148.5 51" fill="#0f6e56" stroke="#0f6e56" stroke-width="1" stroke-linejoin="round" /><text x="153" y="28" font-size="12" font-weight="700" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F = 15 N</text><line x1="45" y1="124" x2="45" y2="89" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round" /><polygon points="45 81 48.5 89 41.5 89" fill="#0f6e56" stroke="#0f6e56" stroke-width="1" stroke-linejoin="round" /><text x="45" y="138" font-size="11" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">RA = 9 N</text><line x1="295" y1="112" x2="295" y2="89" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round" /><polygon points="295 81 298.5 89 291.5 89" fill="#0f6e56" stroke="#0f6e56" stroke-width="1" stroke-linejoin="round" /><text x="295" y="126" font-size="11" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">RB = 6 N</text><circle cx="145" cy="62" r="3.5" fill="#0f172a" /><text x="43" y="54" font-size="13" font-weight="700" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="297" y="54" font-size="13" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="137" y="54" font-size="13" font-weight="700" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><line x1="45" y1="150" x2="145" y2="150" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="45" y1="145" x2="45" y2="155" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="145" y1="145" x2="145" y2="155" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="95" y="144" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">AC = 200</text><line x1="145" y1="150" x2="295" y2="150" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="145" y1="145" x2="145" y2="155" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="295" y1="145" x2="295" y2="155" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="220" y="144" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">CB = 300</text><line x1="45" y1="270" x2="295" y2="270" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><polygon points="45 270 145 180 295 270" fill="#0f6e56" fill-opacity="0.14" stroke="#0f6e56" stroke-width="2.2" stroke-linejoin="round" /><line x1="145" y1="66" x2="145" y2="180" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4 4" /><text x="151" y="174" font-size="11" font-weight="700" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Mf max = 1 800 N·mm</text><text x="45" y="286" font-size="10" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Mf = 0</text><text x="295" y="286" font-size="10" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Mf = 0</text><text x="150" y="304" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Moment fléchissant Mf le long de la poutre</text></svg>
:::

Sous la poutre, la hauteur du triangle en un point est la valeur de Mf en ce point : on lit tout de suite où la flexion est la plus forte.

::: exemple Calculer RA, RB et Mfmax (B.1 a et b)
Poutre de 500 mm, F = 15 N en C, AC = 200 mm, CB = 300 mm.

1. La poutre est en équilibre : les deux réactions portent la charge, donc RA + RB = 15 N.
2. On écrit les moments par rapport à A, pour éliminer RA : RB × 500 = 15 × 200, donc **RB = 6 N**.
3. On en déduit **RA** = 15 − 6 = **9 N**. Contrôle par les moments par rapport à B : RA × 500 = 15 × 300 donne bien 9 N.
4. Entre A et C, en regardant à gauche de la section d'abscisse x : Mf = RA × x = 9 × x, qui croît jusqu'à C.
5. Entre C et B, en regardant à droite : Mf = RB × (500 − x) = 6 × (500 − x), qui décroît jusqu'à 0 en B.
6. En C, les deux expressions donnent 9 × 200 = 6 × 300 : **Mfmax = 1 800 N·mm** = 1,8 N·m.

:::

::: piege Le maximum n'est pas au milieu
Au milieu de la poutre (x = 250 mm), Mf = 6 × 250 = 1 500 N·mm, **moins** que les 1 800 N·mm de C. Le moment fléchissant est maximal **sous la charge**, pas au milieu de la poutre. Et les réactions ne valent F / 2 chacune que si la charge est au milieu : ici RA = 9 N est plus grande que RB = 6 N.
:::

::: propriete Charge ponctuelle sur deux appuis
Pour une charge F à la distance a de A et b de B, avec a + b = L :

$$ RA = F × b / L $$

$$ RB = F × a / L $$

$$ Mfmax = F × a × b / L $$

Le moment est maximal sous la charge et nul aux appuis ; l'appui le plus proche de la charge porte la plus grande réaction. Cas limite, la charge au milieu : RA = RB = F / 2 et Mfmax = F × L / 4.
:::

::: verifie
Une poutre de 400 mm porte F = 20 N à 100 mm de A. Calcule RA, RB et Mfmax.
---

a = 100 mm et b = 300 mm. RA = 20 × 300 / 400 = **15 N** : A est le plus proche de la charge, il porte le plus. RB = 20 × 100 / 400 = **5 N** (et 15 + 5 = 20 N). Mfmax = RA × 100 = **1 500 N·mm**, sous la charge ; on retrouve RB × 300 = 1 500.
:::

## 🔥 La contrainte normale maximale

Plie une règle de plastique : le dessus se raccourcit, le dessous s'allonge, et une fibre intermédiaire garde sa longueur. Tous les points d'une section ne travaillent donc pas pareil.

Où le matériau est-il le plus sollicité, et de combien ? Le manuel demande la contrainte maximale σmax de la poutre de la partie B.

::: definition La contrainte normale σ
La **contrainte normale** σ est la force par unité de surface qui s'exerce perpendiculairement à la section ; elle s'exprime en **MPa**, avec 1 MPa = 1 N/mm². En un point situé à la distance y de l'axe neutre Gz :

$$ σ = Mf × y / IGz $$

Elle est nulle sur l'axe neutre et maximale aux fibres les plus éloignées, à y = v :

$$ σmax = Mf / (IGz / v) $$

La quantité **IGz / v** (en mm³) est le **module de flexion** (le manuel dit « module de rigidité à la flexion »).
:::

::: figure À gauche, la section circulaire de la poutre de la partie B, avec l'axe neutre Gz et la distance v de G à la fibre extrême. À droite, la contrainte σ le long de la hauteur : nulle sur Gz, proportionnelle à la distance y, maximale en valeur absolue en haut (compression) et en bas (traction) pour une charge vers le bas
<svg viewBox="0 0 340 200"><title>Contrainte normale dans une section en flexion : nulle sur l'axe neutre, maximale aux fibres extrêmes</title><circle cx="85" cy="108" r="48" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" /><line x1="23" y1="108" x2="153" y2="108" stroke="#0f6e56" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="6 4" /><circle cx="85" cy="108" r="3" fill="#0f6e56" /><text x="25" y="102" font-size="12" font-weight="700" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Gz</text><text x="93" y="103" font-size="12" font-weight="700" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">G</text><line x1="19" y1="156" x2="85" y2="156" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4 3" /><line x1="27" y1="118" x2="27" y2="148" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><polygon points="27 156 23.5 148 30.5 148" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" /><line x1="27" y1="146" x2="27" y2="116" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><polygon points="27 108 30.5 116 23.5 116" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" /><text x="35" y="136" font-size="12" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v</text><text x="85" y="178" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">section circulaire</text><line x1="245" y1="52" x2="245" y2="164" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><polygon points="245 108 197 60 245 60" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><polygon points="245 108 293 156 245 156" fill="#fdba74" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><line x1="133" y1="60" x2="245" y2="60" stroke="#94a3b8" stroke-width="1" stroke-linecap="round" stroke-dasharray="3 3" /><line x1="133" y1="156" x2="293" y2="156" stroke="#94a3b8" stroke-width="1" stroke-linecap="round" stroke-dasharray="3 3" /><line x1="153" y1="108" x2="303" y2="108" stroke="#0f6e56" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="6 4" /><text x="193" y="63" font-size="12" font-weight="700" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−σmax</text><text x="297" y="159" font-size="12" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+σmax</text><text x="253" y="63" font-size="10" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">compression</text><text x="237" y="159" font-size="10" font-weight="600" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">traction</text><text x="249" y="103" font-size="10" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">σ = 0</text></svg>
:::

Les triangles de droite sont une représentation de σ = Mf × y / IGz : la contrainte est proportionnelle à y, et la fibre la plus éloignée, à la distance v, porte σmax.

::: exemple Calculer σmax de la poutre de la partie B (B.1 c)
Poutre de section circulaire pleine, d = 8 mm, avec Mfmax = 1 800 N·mm.

1. Le moment quadratique du cercle : IGz = π × 8⁴ / 64 ≈ 201,1 mm⁴.
2. La fibre la plus éloignée de l'axe neutre est à un rayon du centre : **v = d / 2 = 4 mm**.
3. Le module de flexion : IGz / v = 201,1 / 4 ≈ 50,3 mm³ (c'est π × d³ / 32).
4. La contrainte maximale, avec Mf **en N·mm** pour obtenir des MPa :

$$ σmax = 1 800 / 50,3 ≈ 35,8 MPa $$

:::

::: piege N·m et N·mm ne se mélangent pas
Écrire Mfmax = 1,8 N·m et IGz en mm⁴ donne 1,8 / 50,3 ≈ 0,036, soit mille fois trop petit. Les mm⁴ et les mm³ imposent des **N·mm** : 1,8 N·m = 1 800 N·mm. Autre faute fréquente : prendre v = d = 8 mm au lieu du rayon, ce qui divise σmax par deux.
:::

::: propriete σmax diminue vite quand la section grossit
Pour un moment donné, σmax est proportionnel à Mf et inversement proportionnel à IGz / v. Pour un cercle :

$$ σmax = 32 × Mf / (π × d³) $$

Doubler le diamètre divise σmax par 8. σmax ne dépend pas du matériau : E n'y figure pas ; un métal plus rigide plie moins mais n'est pas moins contraint. Cas limite : sur l'axe neutre (y = 0), σ est nulle quel que soit Mf.
:::

::: verifie
La barre rectangulaire 20 × 6 mm est posée à plat et soumise à Mf = 1 800 N·mm. Calcule σmax.
---

À plat, h = 6 mm, donc v = h / 2 = 3 mm, et IGz = 360 mm⁴. σmax = Mf × v / IGz = 1 800 × 3 / 360 = **15 MPa**. Le moment est en N·mm et la contrainte sort en MPa.
:::

## ✅ La condition de résistance

σmax vaut 35,8 MPa et le manuel donne pour l'acier une limite élastique Re = 240 MPa. Le résultat est très inférieur : la poutre est-elle sûre ?

Et quelle marge faut-il garder, puisqu'on ne veut jamais s'approcher de la limite ? Il faut une règle de comparaison qui tienne compte de cette marge : le manuel l'appelle la condition de résistance.

::: definition Re, s et Rpe
La **limite élastique Re** (en MPa) est la contrainte au-delà de laquelle le métal garde une déformation permanente. Le **coefficient de sécurité s**, sans unité et supérieur à 1, est la marge que l'on se donne. La **résistance pratique** est :

$$ Rpe = Re / s $$

La poutre résiste en toute sécurité si :

$$ σmax ≤ Rpe $$

Le manuel écrit Rp dans la question de la partie B ; la synthèse du thème écrit Rpe.
:::

::: exemple Conclure sur la poutre de la partie B (B.1 d)
Données du manuel : Re = 240 MPa, s = 3 ; on a trouvé σmax ≈ 35,8 MPa.

1. On calcule la résistance pratique : Rpe = 240 / 3 = **80 MPa**.
2. On forme le rapport demandé : σmax / Rpe = 35,8 / 80 ≈ **0,45**.
3. Ce rapport est inférieur à 1, donc σmax ≤ Rpe : **la poutre résiste en toute sécurité**. Elle utilise environ 45 % de ce qu'on lui autorise.

:::

::: piege Comparer à Re au lieu de Rpe
Avec s = 3, une contrainte de 100 MPa est bien inférieure à Re = 240 MPa, et pourtant 100 est supérieur à Rpe = 80 : la condition n'est **pas** respectée. Le coefficient de sécurité est précisément la marge qu'on retire à Re avant de comparer.
:::

::: propriete Lire le rapport σmax / Rpe
Rapport inférieur à 1 : la poutre résiste ; égal à 1 : c'est la limite ; supérieur à 1 : elle ne résiste pas. Comme σmax est proportionnelle à la charge, on peut chercher la charge limite : pour la poutre de la partie B, σmax = 35,8 MPa à 15 N, donc σmax atteint 80 MPa à 15 × 80 / 35,8 ≈ 33,5 N.

La condition de résistance ne dit rien de la flèche : une poutre peut résister et plier trop. La déformation se juge à part, par la flèche f, avec une limite que fixe le cahier des charges.
:::

::: verifie
Un acier a Re = 240 MPa et on prend s = 2. Une poutre subit σmax = 130 MPa. Résiste-t-elle ?
---

Rpe = Re / s = 240 / 2 = 120 MPa. Comme 130 > 120, le rapport σmax / Rpe ≈ 1,08 dépasse 1 : la poutre **ne résiste pas**, bien que 130 soit inférieur à Re.
:::

## 🔬 Valider : calcul, simulation, mesure

Pour la même poutre de la partie B, tu as trois résultats : le calcul fait à la main, la simulation avec Winflex, la mesure au comparateur. Qu'est-ce qu'on compare, où pose-t-on le palpeur, et à partir de quel écart se méfie-t-on ?

Le logiciel reçoit les mêmes données que le calcul (poutre, appuis, charge, matériau) et le manuel demande d'en relever le moment fléchissant maximal, la contrainte maximale, la flèche maximale et son abscisse AD, au point D.

::: figure La poutre de la partie B sous F en C. D est le point le plus bas de la déformée : il est entre C et le milieu de la poutre, du côté le plus long (CB). Le dessin exagère la flèche
<svg viewBox="0 0 340 176"><title>Charge hors du milieu : le point D le plus bas est entre C et le milieu, du côté le plus long</title><line x1="45" y1="60" x2="295" y2="60" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="5 4" /><polygon points="45 61 34 76 56 76" fill="#fde68a" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><line x1="28" y1="76" x2="62" y2="76" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><circle cx="295" cy="68.5" r="7.5" fill="#fde68a" stroke="#0f172a" stroke-width="1.6" /><line x1="278" y1="76" x2="312" y2="76" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><polyline points="45 60 47.5 61.2 50 62.3 52.5 63.5 55 64.7 57.5 65.8 60 67 62.5 68.1 65 69.2 67.5 70.4 70 71.5 72.5 72.6 75 73.7 77.5 74.8 80 75.8 82.5 76.9 85 77.9 87.5 78.9 90 79.9 92.5 80.9 95 81.9 97.5 82.8 100 83.7 102.5 84.6 105 85.5 107.5 86.3 110 87.1 112.5 87.9 115 88.7 117.5 89.4 120 90.1 122.5 90.7 125 91.4 127.5 91.9 130 92.5 132.5 93 135 93.5 137.5 93.9 140 94.3 142.5 94.7 145 95 147.5 95.3 150 95.5 152.5 95.7 155 95.8 157.5 95.9 160 96 162.5 96 165 96 167.5 95.9 170 95.8 172.5 95.7 175 95.5 177.5 95.4 180 95.1 182.5 94.9 185 94.6 187.5 94.2 190 93.9 192.5 93.5 195 93 197.5 92.6 200 92.1 202.5 91.6 205 91.1 207.5 90.5 210 89.9 212.5 89.3 215 88.7 217.5 88 220 87.3 222.5 86.6 225 85.9 227.5 85.2 230 84.4 232.5 83.6 235 82.8 237.5 82 240 81.2 242.5 80.3 245 79.4 247.5 78.6 250 77.7 252.5 76.8 255 75.8 257.5 74.9 260 74 262.5 73 265 72 267.5 71.1 270 70.1 272.5 69.1 275 68.1 277.5 67.1 280 66.1 282.5 65.1 285 64.1 287.5 63.1 290 62 292.5 61 295 60" fill="none" stroke="#0f172a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" /><polyline points="45 60 47.5 61.2 50 62.3 52.5 63.5 55 64.7 57.5 65.8 60 67 62.5 68.1 65 69.2 67.5 70.4 70 71.5 72.5 72.6 75 73.7 77.5 74.8 80 75.8 82.5 76.9 85 77.9 87.5 78.9 90 79.9 92.5 80.9 95 81.9 97.5 82.8 100 83.7 102.5 84.6 105 85.5 107.5 86.3 110 87.1 112.5 87.9 115 88.7 117.5 89.4 120 90.1 122.5 90.7 125 91.4 127.5 91.9 130 92.5 132.5 93 135 93.5 137.5 93.9 140 94.3 142.5 94.7 145 95 147.5 95.3 150 95.5 152.5 95.7 155 95.8 157.5 95.9 160 96 162.5 96 165 96 167.5 95.9 170 95.8 172.5 95.7 175 95.5 177.5 95.4 180 95.1 182.5 94.9 185 94.6 187.5 94.2 190 93.9 192.5 93.5 195 93 197.5 92.6 200 92.1 202.5 91.6 205 91.1 207.5 90.5 210 89.9 212.5 89.3 215 88.7 217.5 88 220 87.3 222.5 86.6 225 85.9 227.5 85.2 230 84.4 232.5 83.6 235 82.8 237.5 82 240 81.2 242.5 80.3 245 79.4 247.5 78.6 250 77.7 252.5 76.8 255 75.8 257.5 74.9 260 74 262.5 73 265 72 267.5 71.1 270 70.1 272.5 69.1 275 68.1 277.5 67.1 280 66.1 282.5 65.1 285 64.1 287.5 63.1 290 62 292.5 61 295 60" fill="none" stroke="#bfdbfe" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" /><line x1="145" y1="8" x2="145" y2="82" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" /><polygon points="145 90 141.5 82 148.5 82" fill="#0f6e56" stroke="#0f6e56" stroke-width="1" stroke-linejoin="round" /><text x="137" y="26" font-size="14" font-weight="700" text-anchor="end" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text><line x1="170" y1="58" x2="170" y2="120" stroke="#94a3b8" stroke-width="1.1" stroke-linecap="round" stroke-dasharray="3 4" /><text x="192" y="128" font-size="10" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">milieu</text><circle cx="145" cy="95" r="4" fill="#0f172a" /><circle cx="162.7" cy="96" r="4.6" fill="#0f6e56" stroke="#ffffff" stroke-width="1.5" /><text x="139" y="113" font-size="13" font-weight="700" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><text x="166.7" y="116" font-size="13" font-weight="700" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><text x="45" y="96" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="295" y="96" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><line x1="45" y1="134" x2="145" y2="134" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="45" y1="129" x2="45" y2="139" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="145" y1="129" x2="145" y2="139" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="95" y="128" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">AC = 200</text><line x1="45" y1="160" x2="162.7" y2="160" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="45" y1="155" x2="45" y2="165" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><line x1="162.7" y1="155" x2="162.7" y2="165" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><text x="103.9" y="154" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">AD ≈ 235</text></svg>
:::

Sur la figure, C est le point d'application de F et D le point où la flèche est maximale : ils ne sont pas confondus, et AD est l'abscisse que le manuel demande de relever.

::: exemple Comparer la théorie et la mesure (B.2 et B.3)
Poutre Ø 8 mm, acier (E = 210 GPa), F = 15 N en C, L = 500 mm. La théorie standard des poutres place D à AD ≈ 235 mm de A et donne une flèche maximale **fmax ≈ 0,877 mm** (valeurs calculées pour ce cours, que le manuel ne donne pas). Le comparateur, posé en D, affiche **0,90 mm** (valeur d'illustration).

1. On compare grandeur à grandeur : la flèche **maximale** calculée et la flèche lue en D, qui est son point.
2. L'écart relatif se prend par rapport à la valeur de référence : (0,90 − 0,877) / 0,877 ≈ **2,6 %**.
3. Un écart de quelques pour cent est attendu : les appuis ont un peu de jeu, le cadran se lit au centième, et les valeurs réelles diffèrent un peu des valeurs nominales : E du lot d'acier, diamètre réel de la barre (IGz suit d⁴ : 1 % d'écart sur d fait environ 4 % sur f). La mesure **confirme** le calcul.

:::

::: piege Poser le comparateur en C
Sous la charge, en C, la flèche théorique est d'environ 0,853 mm, soit trois pour cent de moins que fmax : un écart du même ordre que ceux de la mesure. On ne peut alors plus distinguer une erreur de mesure d'une erreur de place. Pour comparer à fmax, le palpeur se pose en **D**.
:::

::: methode Valider un résultat de calcul

1. Utiliser les **mêmes données** pour le calcul, la simulation et l'essai : poutre, appuis, charge, matériau.
2. Comparer **grandeur à grandeur** : Mfmax, σmax, fmax, et son abscisse AD.
3. Calculer l'**écart relatif** : écart divisé par la valeur de référence.
4. Conclure : quelques pour cent, la théorie est confirmée ; un écart plus grand, chercher d'abord le jeu des appuis, la lecture du cadran, la valeur de E et le diamètre réel.

:::

::: verifie
Winflex donne σmax = 36,0 MPa et le calcul à la main 35,8 MPa. Quel est l'écart relatif, et est-il surprenant ?
---

Écart = (36,0 − 35,8) / 35,8 ≈ **0,6 %**. Ce n'est pas surprenant : le calcul et la simulation partent des mêmes données et de la même théorie des poutres, ils doivent coïncider à l'arrondi près. C'est la mesure sur le banc, avec ses jeux et sa lecture au cadran, qui s'écarte un peu plus.
:::

## 🧭 La méthode qui reste : sept marches

Devant une poutre sur deux appuis, tu reprends toujours cet ordre :

1. **Lire l'essai** : portée L entre les appuis, charge F, flèche f lue au comparateur.
2. **Section** : relever b et h (ou d) et calculer IGz, avec h dans le sens de la charge.
3. **Lois de la flèche** : f proportionnelle à F, et proportionnelle à L³.
4. **Réactions** : RA = F × b / L, RB = F × a / L.
5. **Moment** : Mfmax = F × a × b / L, sous la charge ; le convertir en N·mm.
6. **Contrainte** : σmax = Mfmax / (IGz / v), avec v = d / 2 pour un cercle.
7. **Verdict** : Rpe = Re / s, puis σmax / Rpe ≤ 1 ; valider par la simulation et l'essai en D.

::: retenir
Une poutre sur deux appuis plie d'une **flèche f** proportionnelle à la charge F et à **L³**, et inversement proportionnelle à E et à **IGz**. La flexion crée un moment **Mfmax = F × a × b / L** sous la charge et une contrainte **σmax = Mfmax / (IGz / v)**, et la poutre résiste si **σmax ≤ Rpe = Re / s**.
:::

> 🏆 Tu sais lire un essai de flexion, prévoir comment la flèche réagit à la charge et à la portée, calculer la contrainte maximale d'une poutre et conclure avec le coefficient de sécurité. La suite du thème combine la flexion avec d'autres sollicitations.
