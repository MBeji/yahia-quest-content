# 🧩 La maquette de train épicycloïdal : de la cote à la pièce

> 💡 «Un dessin n'est qu'une promesse : c'est la gamme, la machine et le programme qui en font une pièce. Ce chapitre suit une maquette, du train d'engrenages jusqu'à l'imprimante 3D.»

Ce chapitre poursuit le thème « Obtention des pièces », ouvert avec le bateau à pédales, avec le **projet 1** du manuel : la **maquette d'un train épicycloïdal**, entraînée à la main par un volant (le dossier de réalisation guidée, en 20 étapes, p.257 à 280). Les premières étapes (besoin, fonctions de service, FAST) reprennent l'analyse fonctionnelle des premiers chapitres, et le calcul de résistance est celui du thème précédent. On retient ici **huit notions**, celles qui mènent du dessin à la pièce : le train, la cote tolérancée, la chaîne de cotes, la gamme, la mise en position, le contrat de phase, le programme ISO et la fabrication additive. La synthèse du thème est portée par le chapitre suivant.

> 🗡️ Le manuel ne donne aucun corrigé : seules les règles standard de la mécanique sont enseignées. Quand une valeur vient du manuel, le texte le dit (« donnée du manuel », « imprimé »). Quand elle est choisie pour s'entraîner, il parle d'**illustration**. Les schémas sont des **schémas de principe**, redessinés pour expliquer.

> 🛡️ **Sécurité, rappelée par le manuel.** Pour un taraudage ou un filetage à la main sur le tour, on **ne met pas le tour sous tension**. L'impression 3D se fait en présence du professeur, et on **simule** un programme avant d'usiner.

## 🪐 Un train, trois fonctions, six rapports

La maquette se manœuvre à la main : le volant tourne à **90 tr/min**. Pourtant le même train d'engrenages peut rendre 22,5 tr/min, 120 tr/min, ou même tourner à l'envers.

Qu'est-ce qui décide de la vitesse de sortie ?

::: definition Le train épicycloïdal et ses quatre pièces
Un **train épicycloïdal** (ou **train planétaire**) est un train d'engrenages dont au moins une roue, le **satellite**, a un mouvement épicycloïdal par rapport au carter fixe : elle tourne sur elle-même et autour de l'axe du train. Sur la maquette :

- le **planétaire** (26), au centre : 18 dents ;
- trois **satellites** (25) de 18 dents, portés par les arbres du **porte-satellite** (11) ;
- la **couronne** (31) : 54 dents à l'intérieur, 72 à l'extérieur.

Les trois pièces d'axe commun, planétaire, couronne et porte-satellite, peuvent tourner chacune à sa vitesse. Les satellites ne se glissent entre planétaire et couronne que si le nombre de dents le permet :

$$ Z couronne = Z planétaire + 2 × Z satellite $$

Ici 18 + 2 × 18 = 54 : la condition est remplie.
:::

::: figure Le train de la maquette vu de face. Chaque satellite (vert) touche le planétaire (jaune) et la couronne (bleue) : c'est ce que dit la condition d'engrènement. Les trois pièces d'axe commun sont le planétaire, la couronne et le porte-satellite (orange). Les dents ne sont pas dessinées
<svg viewBox="0 0 420 262"><title>Train épicycloïdal vu de face : planétaire, trois satellites, couronne et porte-satellite</title><circle cx="210" cy="130" r="108" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8"/><circle cx="210" cy="130" r="81" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><circle cx="210" cy="76" r="27" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8"/><circle cx="163.2" cy="157" r="27" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8"/><circle cx="256.8" cy="157" r="27" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8"/><line x1="210" y1="130" x2="210" y2="76" stroke="#ea580c" stroke-width="5" stroke-linecap="round"/><line x1="210" y1="130" x2="163.2" y2="157" stroke="#ea580c" stroke-width="5" stroke-linecap="round"/><line x1="210" y1="130" x2="256.8" y2="157" stroke="#ea580c" stroke-width="5" stroke-linecap="round"/><circle cx="210" cy="76" r="4.5" fill="#fdba74" stroke="#0f172a" stroke-width="1.4"/><circle cx="163.2" cy="157" r="4.5" fill="#fdba74" stroke="#0f172a" stroke-width="1.4"/><circle cx="256.8" cy="157" r="4.5" fill="#fdba74" stroke="#0f172a" stroke-width="1.4"/><circle cx="210" cy="130" r="27" fill="#fde68a" stroke="#0f172a" stroke-width="1.8"/><circle cx="210" cy="130" r="3" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><line x1="84" y1="40" x2="128" y2="84" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="4" y="38" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">couronne (31)</text><line x1="233.4" y1="116.5" x2="330" y2="70" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="332" y="66" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">planétaire (26)</text><line x1="144.2" y1="176" x2="70" y2="208" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="4" y="222" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">satellite (25)</text><line x1="244.6" y1="150" x2="330" y2="226" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="416" y="240" font-size="9.5" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">porte-satellite (11)</text></svg>
:::

Dans la formule, Z planétaire est le 18 du disque jaune et Z couronne le 54 de l'anneau bleu ; à module égal, les diamètres sont proportionnels aux nombres de dents : le diamètre de la couronne vaut celui du planétaire plus deux diamètres de satellite, un de chaque côté.

Trois pièces d'axe commun, une seule relation entre leurs vitesses (la formule de Willis, vue avec le palan) : si on en connaît deux, la troisième s'en déduit. Selon ce qu'on impose, le train rend trois services, que le manuel distingue :

- **transmettre et adapter** (1 entrée, 1 sortie) : on **bloque** une des trois pièces, ce qui donne un réducteur ou un multiplicateur compact ;
- **transmettre et répartir** (1 entrée, 2 sorties) : le même moteur alimente deux récepteurs dont les vitesses diffèrent, comme dans une transmission de véhicule ;
- **transmettre et combiner** (2 entrées, 1 sortie) : deux moteurs se partagent une sortie, comme dans un véhicule hybride.

La maquette est du premier type. Que valent ses six rapports possibles ?

::: exemple Les six rapports de la maquette (données du manuel : Z planétaire = 18, Z couronne = 54, Ne = 90 tr/min)
On note r = Ns / Ne le rapport de la sortie à l'entrée.

1. **Couronne bloquée, entrée sur le planétaire, sortie sur le porte-satellite.** r = 18 / (18 + 54) = 0,25, donc Ns = 0,25 × 90 = **22,5 tr/min**. Les satellites roulent dans la couronne immobile : le porte-satellite fait un tour pour quatre du planétaire.
2. **Même blocage, entrée et sortie échangées.** r = 1 / 0,25 = 4, donc Ns = **360 tr/min**. On lit la même liaison dans l'autre sens, le rapport s'inverse.
3. **Planétaire bloqué.** Couronne vers porte-satellite : r = 54 / (54 + 18) = 0,75, soit **67,5 tr/min**. Porte-satellite vers couronne : r = 72 / 54 ≈ 1,33, soit **120 tr/min**.
4. **Porte-satellite bloqué.** Les satellites ne font que renvoyer le mouvement : planétaire vers couronne, r = −18 / 54 = −1/3, soit **−30 tr/min** ; couronne vers planétaire, r = −54 / 18 = −3, soit **−270 tr/min**.

:::

| Pièce bloquée   | Entrée → sortie              |     r | Ns pour Ne = 90 tr/min |
| --------------- | ---------------------------- | ----: | ---------------------: |
| couronne        | planétaire → porte-satellite |  0,25 |                   22,5 |
| couronne        | porte-satellite → planétaire |     4 |                    360 |
| planétaire      | couronne → porte-satellite   |  0,75 |                   67,5 |
| planétaire      | porte-satellite → couronne   |  1,33 |                    120 |
| porte-satellite | planétaire → couronne        | −0,33 |                    −30 |
| porte-satellite | couronne → planétaire        |    −3 |                   −270 |

::: piege Un rapport négatif n'est pas un rapport plus petit
Devant −3 et 0,25, on est tenté de dire que −3 est « le plus lent », puisqu'il est négatif. Le signe ne dit que le **sens** : −3 veut dire que la sortie tourne en sens inverse **et trois fois plus vite** (−270 tr/min pour 90 à l'entrée). C'est la valeur **sans le signe** qu'on compare à 1.
:::

::: propriete Réducteur, multiplicateur, inverseur

- Si |r| < 1, la sortie est plus lente que l'entrée : **réducteur**. Si |r| > 1 : **multiplicateur**.
- Si r < 0, la sortie tourne en sens contraire de l'entrée : **inverseur**. Sinon, le train est non-inverseur.
- Échanger l'entrée et la sortie, la même pièce restant bloquée, change r en 1 / r.
- Cas limite : sur cette maquette, aucun des six rapports ne vaut ±1, donc aucune configuration ne transmet la vitesse sans la changer.

:::

::: verifie
Un train a 16 dents au planétaire et 64 à la couronne. Le porte-satellite est bloqué, le planétaire reçoit 100 tr/min et la couronne est la sortie. Que vaut Ns, et de quel type de transmission s'agit-il ?
---

Porte-satellite bloqué : les satellites renvoient le mouvement, donc r = −Z planétaire / Z couronne = −16 / 64 = −0,25, et Ns = −0,25 × 100 = **−25 tr/min**. |r| < 1 : réducteur ; r < 0 : inverseur. C'est un réducteur inverseur.
:::

## 📏 Lire une cote tolérancée et un ajustement

Sur le dessin de définition de l'arbre planétaire (27), on lit Ø10f7, Ø9g6 et Ø8g6 ; sur le porte-satellite (11), Ø10H7 et Ø16H7. Aucune pièce ne sort de la machine à exactement 10,000 mm.

Entre quelles limites l'accepte-t-on, et deux pièces voisines se montent-elles avec du jeu ?

::: definition Cote tolérancée, intervalle de tolérance et jeu
Une cote porte une valeur **nominale** et deux **écarts**, supérieur et inférieur, comptés à partir du nominal. La pièce est bonne si sa cote réelle reste entre la **cote maxi** (nominal + écart supérieur) et la **cote mini** (nominal + écart inférieur). L'**intervalle de tolérance** IT est leur différence :

$$ IT = cote maxi − cote mini $$

Le manuel explicite quelques écarts : Ø10H7 = Ø10 (+0,015 / 0), Ø10f7 = Ø10 (−0,013 / −0,028), Ø9g6 = Ø9 (−0,005 / −0,014). La lettre **majuscule** désigne un alésage, la **minuscule** un arbre ; le chiffre est la **qualité** : plus il est petit, plus la tolérance est serrée.
:::

::: figure Zones de tolérance d'un alésage Ø10H7 et d'un arbre Ø10f7, en micromètres (1 µm = 0,001 mm) à partir du nominal. Le rectangle bleu est l'alésage, le vert l'arbre ; l'arbre est entièrement sous le nominal, l'alésage entièrement au-dessus, d'où un jeu dans tous les cas
<svg viewBox="0 0 340 220"><title>Zones de tolérance d'un alésage Ø10H7 et d'un arbre Ø10f7, en micromètres, avec le jeu mini et le jeu maxi</title><line x1="24" y1="96" x2="316" y2="96" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="6 4"/><text x="316" y="90" font-size="9.5" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0 = Ø10</text><rect x="60" y="51" width="70" height="45" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="210" y="135" width="70" height="45" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="52" y="54.5" font-size="9.5" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+15</text><text x="52" y="99.5" font-size="9.5" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="288" y="138.5" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−13</text><text x="288" y="183.5" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−28</text><line x1="170" y1="96" x2="170" y2="135" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="170 135 168.1 130.4 171.9 130.4" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="176" y="119" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">jeu mini 13</text><line x1="150" y1="51" x2="150" y2="180" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="150 180 148.1 175.4 151.9 175.4" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="144" y="119" font-size="9.5" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">jeu maxi 43</text><line x1="130" y1="51" x2="156" y2="51" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="3 3"/><line x1="210" y1="180" x2="144" y2="180" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="3 3"/><text x="95" y="43" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">alésage H7</text><text x="245" y="196" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">arbre f7</text></svg>
:::

Les bords du rectangle bleu sont les écarts +15 et 0 de l'alésage H7 ; ceux du rectangle vert sont les écarts −13 et −28 de l'arbre f7. Les deux flèches de la figure sont le jeu mini et le jeu maxi qu'on calcule maintenant.

::: exemple Les limites de Ø10H7 et de Ø10f7, puis leur jeu (illustration de montage)
Le manuel ne dit pas quelles pièces s'emboîtent : pour s'entraîner, on monte un arbre Ø10f7 dans un alésage Ø10H7.

1. **Alésage.** Mini 10 + 0 = 10,000 ; maxi 10 + 0,015 = 10,015 ; IT = 0,015.
2. **Arbre.** Maxi 10 − 0,013 = 9,987 ; mini 10 − 0,028 = 9,972 ; IT = 0,015.
3. **Jeu mini** = alésage mini − arbre maxi = 10,000 − 9,987 = 0,013 : c'est le montage le plus serré.
4. **Jeu maxi** = alésage maxi − arbre mini = 10,015 − 9,972 = 0,043 : c'est le montage le plus lâche.
5. **Conclusion.** Le jeu mini est positif : tout arbre entre dans tout alésage, l'ajustement est **avec jeu**.

:::

::: piege Le jeu n'est pas l'IT
On lit parfois « H7, +0,015 » comme « le jeu vaut 0,015 ». C'est l'IT de l'alésage, qui mesure la dispersion d'**une** pièce. Le jeu se construit avec **deux** pièces et varie de 0,013 à 0,043. Et pour le jeu mini, on prend l'alésage **mini** et l'arbre **maxi** : mettre les deux mini donne 10,000 − 9,972 = 0,028, qui n'est ni l'un ni l'autre.
:::

::: propriete Jeu mini, jeu maxi et somme des IT

- Jeu mini = alésage mini − arbre maxi ; jeu maxi = alésage maxi − arbre mini.
- Jeu maxi − jeu mini = IT alésage + IT arbre : 43 − 13 = 30 = 15 + 15.
- Si le jeu mini est **négatif**, certains montages serrent : l'ajustement n'est plus « avec jeu » garanti.
- Une cote symétrique se lit de la même façon : 69 ±0,05 va de 68,95 à 69,05 (IT = 0,10) ; 6 (+0,1 / 0) va de 6,0 à 6,1.

:::

Les cotes sans écart ne sont pas libres pour autant : le dessin porte **Tolérances générales ISO 2768-mk**, qui fixe une tolérance par défaut, et **Ra 3,2**, qui limite la rugosité moyenne à 3,2 µm, vérifiée à la plaquette rugotest.

::: verifie
Un arbre Ø8g6 (−0,005 / −0,014) est monté, pour s'entraîner, dans un alésage Ø8H7 (+0,015 / 0). Que valent le jeu mini et le jeu maxi ?
---

Arbre : maxi 8 − 0,005 = 7,995 ; mini 8 − 0,014 = 7,986. Alésage : mini 8,000 ; maxi 8,015. **Jeu mini** = 8,000 − 7,995 = **0,005** (alésage mini, arbre maxi). **Jeu maxi** = 8,015 − 7,986 = **0,029** (alésage maxi, arbre mini). Contrôle : 0,029 − 0,005 = 0,024 = 0,015 + 0,009, la somme des deux IT.
:::

## 🔗 Du jeu fonctionnel à la cote de fabrication

Sur la maquette, l'arbre porte-roue (32) doit tourner dans le palier (4) en gardant un peu de jeu dans le sens de l'axe : le manuel le nomme **Ja**. Aucune pièce ne porte Ja : il naît de la différence entre la cote a32 de l'arbre et la somme de cinq autres cotes.

Comment le calculer, et comment en tirer la précision demandée à la machine ?

::: definition La chaîne de cotes de Ja
Le **jeu fonctionnel axial Ja** assure le guidage en rotation de l'arbre porte-roue (32) par rapport au palier (4). Sa **chaîne de cotes** enferme dans la cote a32 de l'arbre la rondelle plastique (35), le coussinet (5), le palier (4), le second coussinet (5′) et l'anneau élastique (34). Le manuel l'écrit :

$$ a32 = Ja + a35 + a5 + a4 + a5′ + a34 $$

d'où le jeu :

$$ Ja = a32 − (a35 + a5 + a4 + a5′ + a34) $$
:::

::: figure La chaîne de cotes de Ja, à l'échelle de l'illustration qui suit. La barre orange est la cote a32 de l'arbre ; en dessous, les cinq pièces enfermées, repérées comme à la nomenclature ; l'espace libre à droite est le jeu Ja
<svg viewBox="0 0 340 172"><title>Chaîne de cotes du jeu axial Ja : la cote a32 de l'arbre enferme la rondelle 35, le coussinet 5, le palier 4, le coussinet 5 prime et l'anneau 34</title><rect x="29" y="30" width="282" height="22" fill="#fed7aa" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="170" y="45" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">a32 (arbre porte-roue)</text><text x="27" y="22" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"></text><rect x="29" y="86" width="10" height="22" fill="#e9d5ff" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><text x="34" y="124" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">35</text><rect x="39" y="86" width="30" height="22" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><text x="54" y="124" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><rect x="69" y="86" width="200" height="22" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><text x="169" y="124" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><rect x="269" y="86" width="30" height="22" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><text x="284" y="124" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5′</text><rect x="299" y="86" width="7" height="22" fill="#fde68a" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><text x="302.5" y="124" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">34</text><rect x="306" y="86" width="5" height="22" fill="#ffffff" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round" stroke-dasharray="3 2"/><line x1="29" y1="52" x2="29" y2="86" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="3 3"/><line x1="311" y1="52" x2="311" y2="86" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="3 3"/><line x1="308.5" y1="148" x2="308.5" y2="110" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="308.5 110 310.4 114.6 306.6 114.6" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="308.5" y="162" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Ja</text><text x="29" y="78" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">cotes qui s'empilent</text></svg>
:::

La barre orange est le a32 de la formule, les cinq rectangles sont les cinq cotes soustraites, et le vide est Ja : plus les pièces sont longues, plus il se réduit.

::: exemple Le jeu Ja et ses limites (valeurs d'illustration, le manuel ne les donne pas)
Cotes : a32 = 28,2 ±0,1 ; a35 = 1 ±0,05 ; a5 = 3 ±0,05 ; a4 = 20 ±0,05 ; a5′ = 3 ±0,05 ; a34 = 0,7 ±0,05.

1. **Jeu nominal.** Ja = 28,2 − (1 + 3 + 20 + 3 + 0,7) = 28,2 − 27,7 = **0,5**.
2. **Ja maxi** : l'arbre le plus long avec les cinq pièces les plus courtes. 28,3 − (0,95 + 2,95 + 19,95 + 2,95 + 0,65) = 28,3 − 27,45 = **0,85**.
3. **Ja mini** : l'arbre le plus court avec les cinq pièces les plus longues. 28,1 − (1,05 + 3,05 + 20,05 + 3,05 + 0,75) = 28,1 − 27,95 = **0,15**.
4. **Contrôle.** 0,85 − 0,15 = 0,70 = 0,2 (arbre) + 5 × 0,1 (pièces) : les IT de la chaîne s'additionnent.
5. **Conclusion.** Ja mini est positif : même dans le pire cas, l'arbre reste libre.

:::

::: piege Le jeu maxi ne vient pas de cotes toutes au maxi
Mettre tout à son maxi donne 28,3 − 27,95 = 0,35 : ce n'est ni le maxi (0,85) ni le mini (0,15). Pour le jeu maxi, la cote qui **enferme** (a32) est maxi et celles qui sont **enfermées** sont mini ; pour le jeu mini, c'est l'inverse.
:::

La même arithmétique sert à **fabriquer**. Une **cote machine** (Cm) est une dimension que la machine réalise en une opération, en réglant la position de l'outil depuis une surface de référence. Une **cote outil** (Co) est donnée par l'outil lui-même : le manuel note Cm1 = 79 ±0,5 pour la première face dressée, et Co8 = 3,3 ±0,1 pour le foret de 3,3 mm.

Quand une cote du dessin n'est pas réalisée directement, c'est la **différence de deux cotes machine** qui la fournit : sa tolérance est alors la somme des leurs.

::: exemple De la cote du dessin aux cotes machine (illustration)
Le dessin demande, entre un épaulement S et la face B, une cote de 21 ±0,1. En phase, on règle la face B à Cm(B) = 78 ±0,05 et l'épaulement S à Cm(S) = 57 ±0,05, tous deux mesurés depuis la même face A.

1. **Nominal.** 78 − 57 = 21 : la cote du dessin est bien la différence.
2. **Tolérance obtenue.** IT = 0,10 + 0,10 = 0,20, soit 21 ±0,10 : exactement ce que demande le dessin.
3. **Conséquence.** Chaque cote machine doit être **plus serrée** que la cote qu'elle construit : à ±0,10 chacune, on obtiendrait 21 ±0,20.

:::

::: propriete Les IT d'une chaîne s'additionnent
L'IT de la cote condition est la **somme des IT** de toutes les cotes de la chaîne. Plus la chaîne a de maillons, plus chacun doit être serré. Cas limite : une chaîne d'un seul maillon a l'IT de cette cote, sans rien d'autre à additionner.
:::

::: verifie
Dans la chaîne de Ja, on remplace les deux coussinets par d'autres, de 3 ±0,1 chacun. Que devient Ja mini, les autres cotes étant inchangées ?
---

On reprend le cas de Ja mini : arbre le plus court, pièces les plus longues. Les pièces maxi valent 1,05 + 3,1 + 20,05 + 3,1 + 0,75 = 28,05, donc Ja mini = 28,1 − 28,05 = **0,05**. Il reste positif, mais il a perdu 0,10 : les IT des deux coussinets ont chacun augmenté de 0,05.
:::

## 🗂️ La gamme de fabrication : phases, ordre, surépaisseur

L'arbre planétaire (27) part d'un barreau de PVC scié, de Ø12 et de 80 mm de long. Il doit sortir avec ses portées Ø10f7, Ø9g6 et Ø8g6, un trou taraudé, un filetage et une rainure.

Par quoi commencer, et dans quel ordre enchaîner ?

::: definition Gamme, phase et opération
La **gamme de fabrication** est la liste **ordonnée** des phases qui transforment le brut en pièce finie. Une **phase** regroupe ce qu'on fait sur un poste, avec une mise en position donnée ; une **opération** est l'usinage d'une surface (dresser, charioter, percer…). Les numéros vont de dix en dix (10, 20, 30…) pour qu'on puisse en intercaler. Le manuel la présente sur la _feuille d'avant-projet d'étude de fabrication_, établie par le bureau des méthodes.
:::

| Phase | Poste            | Ce qu'on y fait (d'après la feuille du manuel)                                    |
| ----- | ---------------- | --------------------------------------------------------------------------------- |
| 10    | contrôle         | le brut scié : Ø12, L = 80, au pied à coulisse au 1/50                            |
| 20    | tournage         | dresser la face 1, charioter Ø10f7 puis Ø9g6, chanfreiner, centrer, percer à Ø3,3 |
| 30    | taraudage manuel | tarauder M4 (taraud ébauche, demi-finition, finition), tour hors tension          |
| 40    | tournage         | dresser l'autre face, charioter Ø8g6, faire la gorge, chanfreiner                 |
| 50    | filetage manuel  | fileter M8 à la filière, tour hors tension                                        |
| 60    | fraisage         | rainurer, à la micro-fraiseuse, avec une fraise à deux lèvres Ø3                  |

La colonne de gauche donne l'ordre de passage ; celle de droite dit ce qui change à chaque poste.

::: exemple Préparer le brut et le trou taraudé de l'arbre (valeurs du manuel, sauf les passes)

1. **Surépaisseur au rayon.** Le brut est à Ø12, la plus grosse portée finie à Ø10 : on enlève (12 − 10) / 2 = **1 mm** de chaque côté, car le brut est plus gros que la pièce.
2. **Surépaisseur en longueur.** 80 − 78 = 2 mm : le manuel dresse la première face à 79, puis l'autre face à 78, soit **1 mm par face**.
3. **Ébauche, demi-finition, finition.** On enlève la plus grande part en ébauche, qui va vite, puis on réserve une petite dernière passe pour tenir la cote tolérancée et l'état de surface Ra 3,2.
4. **Diamètre du trou.** Pour un taraudage M4, pas de 0,7 mm : Ø foret = 4 − 0,7 = **3,3 mm**, le Co8 du manuel. On centre d'abord : l'avant-trou guide le foret.
5. **Pas de démontage entre le perçage et le taraudage.** Les phases 20 et 30 ont le même référentiel : le taraud suit l'axe du trou, qui reste centré.

:::

::: piege Percer à Ø4 pour tarauder M4
Le diamètre nominal M4 est celui du filet fini, pas celui du trou. Un trou de Ø4 n'a plus de matière pour le filet : le taraud n'accroche rien. On perce au **diamètre moins le pas** : 3,3 mm.
:::

::: methode Ordonner une gamme

1. **Contrôler le brut** d'abord : une pièce hors dimension se refuse avant d'être usinée.
2. **Dégrossir avant de finir** : ébauche, demi-finition, puis finition de la surface tolérancée.
3. **Garder le même référentiel** pour les opérations qui doivent rester coaxiales : perçage, puis taraudage.
4. **Finir par ce qui s'appuie sur des surfaces déjà finies** : la rainure, au fraisage, vient en dernier.

Il n'existe pas une seule gamme possible : on choisit celle qui limite les changements de poste.
:::

::: verifie
On veut tarauder M6 (pas de 1 mm) : quel diamètre de foret, et dans quel ordre se placent le centrage, le perçage et le taraudage ?
---

Diamètre de foret = diamètre nominal − pas = 6 − 1 = **5 mm** : le trou ne doit pas avoir le diamètre du filet fini. L'ordre est **centrer** (l'avant-trou guide le foret), **percer** à 5 mm, puis **tarauder**.
:::

## 📌 Mettre la pièce en position

Sur le tour, la même pièce repasse au mandrin à chaque phase. Pour que la cote usinée soit la même d'une pièce à l'autre, il faut qu'elle prenne toujours la même position.

Comment la définit-on, et combien de contacts faut-il ?

::: definition Degrés de liberté et mise en position
Une pièce libre a **six degrés de liberté** : trois translations et trois rotations. Un contact **ponctuel** en supprime un ; on compte donc la mise en position en **points** :

| Liaison de mise en position | Points |
| --------------------------- | -----: |
| appui plan                  |      3 |
| appui linéaire              |      2 |
| appui ponctuel              |      1 |
| centrage court              |      2 |
| centrage long               |      4 |

Ces contacts forment le **référentiel de mise en position** de la phase. Le **serrage** vient ensuite : il **maintient** les contacts contre l'effort de coupe.
:::

::: figure Arbre tenu au tour. Le centrage long (points 1 à 4) guide l'arbre sur une grande longueur dans le mandrin ; l'appui ponctuel 5 arrête sa translation le long de l'axe. Symboles simplifiés
<svg viewBox="0 0 340 176"><title>Arbre tenu au tour : centrage long par les points 1 à 4 et appui ponctuel 5 sur l'extrémité</title><rect x="24" y="56" width="56" height="60" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="80" y="66" width="210" height="40" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><line x1="14" y1="86" x2="310" y2="86" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="10 3 2 3"/><text x="52" y="48" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">mandrin</text><line x1="96" y1="118" x2="196" y2="118" stroke="#0f172a" stroke-width="3.5" stroke-linecap="round"/><line x1="106" y1="106" x2="106" y2="118" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="106" y1="118" x2="106" y2="126" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round"/><circle cx="106" cy="134" r="8" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/><text x="106" y="137.5" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="134" y1="106" x2="134" y2="118" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="134" y1="118" x2="134" y2="126" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round"/><circle cx="134" cy="134" r="8" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/><text x="134" y="137.5" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="164" y1="106" x2="164" y2="118" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="164" y1="118" x2="164" y2="126" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round"/><circle cx="164" cy="134" r="8" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/><text x="164" y="137.5" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="190" y1="106" x2="190" y2="118" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="190" y1="118" x2="190" y2="126" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round"/><circle cx="190" cy="134" r="8" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/><text x="190" y="137.5" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><rect x="290" y="70" width="8" height="32" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><line x1="298" y1="86" x2="304" y2="86" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><circle cx="312" cy="86" r="8" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/><text x="312" y="89.5" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><text x="146" y="160" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">centrage long</text><text x="312" y="112" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">appui</text><text x="312" y="124" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ponctuel</text></svg>
:::

Les points 1 à 4 sont les quatre points du centrage long du tableau, et le 5 est l'appui ponctuel : le référentiel imprimé dans le manuel pour les phases 20 et 30 est « centrage long (1, 2, 3, 4), appui ponctuel (5), serrage ».

::: exemple Compter les points de deux mises en position

1. **Arbre au tour** (phases 20 et 30 du manuel) : centrage long 4 + appui ponctuel 1 = **5 points**. Reste la rotation de l'arbre autour de son axe : elle ne change la position d'aucune de ses surfaces, et c'est la broche qui l'entraîne.
2. **Pièce prismatique sur une table** : appui plan 3 + appui linéaire 2 + appui ponctuel 1 = **6 points**, tous les degrés de liberté sont supprimés.

:::

::: piege Serrer n'est pas positionner
Serrer plus fort ne remplace pas un contact manquant : le serrage ne supprime **aucun** degré de liberté, il garde la pièce plaquée contre ses appuis. C'est le référentiel qui place la pièce, pas la force du mandrin.
:::

::: propriete Au plus six points
On ne peut pas supprimer plus de six degrés de liberté. Au-delà de six points, la pièce est **sur-contrainte** : deux appuis se disputent la même position, la pièce se déforme au serrage et le placement n'est plus reproductible.
:::

::: verifie
Un disque est posé sur un appui plan, puis centré par un centrage court. Combien de degrés de liberté sont supprimés, et lequel reste libre ?
---

Appui plan 3 + centrage court 2 = **5 degrés** supprimés. Reste la **rotation du disque autour de son axe** : elle ne change rien à sa position puisque le disque est de révolution.
:::

## 📋 Le contrat de phase : régler la coupe

Pour exécuter la phase 40 de l'arbre, il ne suffit pas de savoir quoi usiner : le contrat de phase dit à quelle vitesse tourne la broche, de combien l'outil entre dans la matière à chaque passe et à quelle allure il avance.

Comment s'enchaînent ces réglages ?

::: definition Le contrat de phase et ses éléments de coupe
Le **contrat de phase** détaille une phase : mise en position, croquis, opérations dans l'ordre, outillage de fabrication et de vérification, et **éléments de coupe** :

- **Vc** (m/min) : la vitesse de coupe, liée à la vitesse de rotation N (tr/min) par Vc = π × D × N / 1 000, avec D en mm ;
- **f** : l'avance, en mm par tour pour le tournage ;
- **a** (mm) : la **profondeur de passe**, l'épaisseur de matière enlevée à chaque passe ;
- **Vf** (mm/min) : la vitesse d'avance, qui se déduit de f et de N.

$$ Vf = f × N $$

Le contrat du manuel note N = 800 tr/min pour la plupart des opérations de tournage (400 pour les chanfreins) et des profondeurs de passe a de 0,1 à 0,2 mm. Ses colonnes f et Vf sont laissées vides : c'est à l'élève de les remplir.
:::

::: exemple Réduire une portée de Ø10 à Ø8 sur 40 mm (illustration, sauf N)
On prend N = 800 tr/min, valeur imprimée au contrat, et f = 0,1 mm/tr, choisi pour s'entraîner.

1. **Matière à enlever.** (10 − 8) / 2 = **1 mm** au rayon.
2. **Répartition en trois passes.** Ébauche a = 0,6, demi-finition a = 0,3, finition a = 0,1 : 0,6 + 0,3 + 0,1 = 1,0. Les diamètres successifs sont 8,8, 8,2 puis 8,0.
3. **Vitesse d'avance.** Vf = 0,1 × 800 = **80 mm/min**.
4. **Durée d'une passe** sur 40 mm : 40 / 80 = 0,5 min, soit **30 s** ; les trois passes prennent 90 s, retours non compris.
5. **Vitesse de coupe atteinte.** À Ø10, Vc = π × 10 × 800 / 1 000 ≈ 25,1 m/min ; à Ø8, elle tombe à 20,1 : à N constant, Vc baisse avec le diamètre.

:::

::: piege La profondeur de passe se compte sur le rayon
Une passe de a = 0,6 mm enlève 0,6 mm **de chaque côté** : le diamètre baisse de **1,2 mm**. Écrire 10 − 0,6 = 9,4 après la première passe est l'erreur la plus fréquente : le tour donne en réalité 10 − 2 × 0,6 = 8,8 ; qui compte en diamètre prend des passes deux fois trop profondes et passe sous la cote.
:::

::: propriete Du tournage au fraisage

- En tournage, a se compte au rayon : le diamètre baisse de **2 × a** ; Vf = f × N.
- En fraisage, l'avance se donne souvent **par dent** : f = fz × z, avec z le nombre de dents, et Vf = fz × z × N.
- Cas limite : la fraise à deux lèvres du manuel a z = 2 ; avec f = 0,1 mm/tr (le F.1 du programme de la phase 60), fz = 0,05 mm/dent, et à 2 000 tr/min (illustration), Vf = 200 mm/min.

:::

::: verifie
On passe de Ø12 à Ø10 en deux passes, d'abord a = 0,8 puis a = 0,2. Quel est le diamètre après la première passe, et après la seconde ?
---

Chaque passe agit des deux côtés : après la première, 12 − 2 × 0,8 = **10,4 mm** ; après la seconde, 10,4 − 2 × 0,2 = **10,0 mm**. Contrôle : 0,8 + 0,2 = 1,0 mm de rayon, soit les 2 mm de diamètre à enlever.
:::

## 💻 Le programme ISO : de la trajectoire aux lignes

Le micro-tour et la micro-fraiseuse sont à commande numérique : ils exécutent un programme, ligne après ligne.

Comment passe-t-on d'un parcours d'outil dessiné à des lignes que la machine comprend ?

::: definition Programme ISO (code G) et origine pièce
Un **programme ISO**, ou **gcode**, est une suite de lignes numérotées (N10, N20…) faites de mots :

- **G** : la nature du mouvement. **G00** est un déplacement **rapide**, hors matière ; **G01** est une **interpolation linéaire**, en ligne droite à l'avance programmée **F** (donnée en mm/tr avec **G95**) ;
- **M** : les fonctions auxiliaires. **M03** lance la broche dans le sens horaire ; **M02** termine le programme ;
- **S** : la vitesse de broche (S1500 = 1 500 tr/min) ; **T** : l'outil ;
- **X, Y, Z** : les coordonnées du point à atteindre, comptées depuis l'**origine pièce** (OP) choisie par le programmeur.

Le **%** en tête marque le début du programme.
:::

Le programme imprimé par le manuel est celui de la **douille taraudée (30)**, une petite pièce de PVC tournée au micro-tour, dont la portée est à Ø10 (X = 5, en rayon).

::: figure Le parcours de la phase 20 de la douille, dans le repère (Z, X) de l'origine pièce. La partie grisée est le demi-profil fini ; le trait plein est le déplacement en G01, qui suit le contour ; les pointillés sont le retour en G00 hors matière. OP est l'origine pièce, Z = 0 sur l'axe, 1 mm devant la face dressée ; l'échelle de X est dilatée, ce qui fait paraître le chanfrein à 45° plus raide
<svg viewBox="0 0 480 236"><title>Parcours de l'outil de la phase 20 de la douille : points A à G, usinage en trait plein et déplacement rapide en pointillés</title><line x1="20" y1="200" x2="470" y2="200" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="10 3 2 3"/><text x="466" y="214" font-size="9.5" font-weight="500" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">axe</text><polygon points="42 200 42 100 204 100 210 110 210 200" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.0" stroke-linejoin="round" stroke-linecap="round"/><polyline points="210 40 210 200 210 110 204 100 42 100 42 40" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><polyline points="42 40 462 40" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 4"/><circle cx="210" cy="40" r="3.2" fill="#fde68a" stroke="#0f172a" stroke-width="1.2"/><circle cx="210" cy="200" r="3.2" fill="#fde68a" stroke="#0f172a" stroke-width="1.2"/><circle cx="210" cy="110" r="3.2" fill="#fde68a" stroke="#0f172a" stroke-width="1.2"/><circle cx="204" cy="100" r="3.2" fill="#fde68a" stroke="#0f172a" stroke-width="1.2"/><circle cx="42" cy="100" r="3.2" fill="#fde68a" stroke="#0f172a" stroke-width="1.2"/><circle cx="42" cy="40" r="3.2" fill="#fde68a" stroke="#0f172a" stroke-width="1.2"/><circle cx="462" cy="40" r="3.2" fill="#fde68a" stroke="#0f172a" stroke-width="1.2"/><text x="200" y="34" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="210" y="216" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="220" y="122" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><text x="200" y="91" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><text x="42" y="116" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><text x="42" y="31" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text><text x="462" y="31" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">G</text><line x1="222" y1="200" x2="222" y2="140" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="222 140 223.9 144.6 220.1 144.6" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="228" y="146" font-size="10" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">X</text><line x1="360" y1="222" x2="440" y2="222" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/><polygon points="440 222 435.4 223.9 435.4 220.1" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><text x="448" y="226" font-size="10" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Z</text><line x1="300" y1="18" x2="330" y2="18" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/><text x="336" y="21.5" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">G01 : usinage, à l'avance F</text><line x1="300" y1="32" x2="330" y2="32" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="6 4"/><text x="336" y="35.5" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">G00 : déplacement rapide</text><circle cx="222" cy="200" r="2.6" fill="#dc2626"/><text x="230" y="214" font-size="10" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">OP</text></svg>
:::

Les points A à G de la figure sont ceux des lignes N30 à N90 du tableau.

::: exemple Lire le programme de la phase 20 de la douille (programme imprimé au manuel)

| Ligne                  | Ce qu'elle commande                 | Point (X, Z) |
| ---------------------- | ----------------------------------- | ------------ |
| `N10 S1500 M03`        | broche à 1 500 tr/min, sens horaire |              |
| `N20 G95 T1 D1 M6`     | avance en mm/tr, choix de l'outil   |              |
| `N30 G00 X8 Z-1`       | approche rapide, hors matière       | A (8 ; −1)   |
| `N40 G01 X0 Z-1 F0.04` | dressage de la face, jusqu'à l'axe  | B (0 ; −1)   |
| `N50 G01 X4.5 Z-1`     | retour le long de la face           | C (4,5 ; −1) |
| `N60 G01 X5 Z-1.5`     | chanfrein de 0,5 sur 45°            | D (5 ; −1,5) |
| `N70 G01 X5 Z-15`      | chariotage de la portée             | E (5 ; −15)  |
| `N80 G01 X8 Z-15`      | dégagement radial                   | F (8 ; −15)  |
| `N90 G00 X8 Z20`       | retour rapide, hors matière         | G (8 ; 20)   |
| `N100 M02`             | fin du programme                    |              |

La portée est de Ø10 et le programme l'atteint à **X5** : sur ce micro-tour, X est donc un **rayon**. Le chanfrein de la ligne N60 avance de 0,5 en X et de 0,5 en Z : c'est un chanfrein de 0,5 × 45°.

:::

::: piege G00 ne coupe pas, G01 ne se lance pas à vide
Un G00 dirigé vers la matière enfonce l'outil à pleine vitesse : le déplacement rapide sert à **approcher et dégager**, jamais à usiner. Inversement, un G01 sans avance F n'a pas de vitesse de coupe définie. C'est pourquoi on **simule** le programme avant d'usiner.
:::

::: methode Écrire un programme de phase

1. **Choisir l'origine pièce** et la garder pour tous les points.
2. **Relever les points** du parcours dans un tableau (X, Z) ; le départ et l'arrivée sont **hors matière**.
3. **Ouvrir** : % puis S et M03, l'outil et l'unité d'avance (G95).
4. **Approcher** en G00, **usiner** en G01 avec F, **dégager** en G00.
5. **Fermer** par M02.
6. **Dans l'atelier** : ouvrir Mach 3 avec le bon profil, écrire, **simuler**, appeler l'enseignant, puis usiner.

:::

::: verifie
Sur la même portée Ø10 commençant à la face Z = −1, on veut un chanfrein de 1 × 45° au lieu de 0,5 × 45°. Quelles sont les deux lignes qui le décrivent ?
---

X est un rayon : la portée est à X5, donc le chanfrein de 1 part de X = 5 − 1 = 4 sur la face. Il avance aussi de 1 en Z, jusqu'à Z = −1 − 1 = −2. Les lignes sont **N50 G01 X4 Z-1** puis **N60 G01 X5 Z-2**.
:::

## 🖨️ La fabrication additive : du modèle à la pièce

Le porte-satellite (11) de la maquette, en PLA, n'est pas usiné dans un brut : on l'imprime.

Quelles étapes séparent l'idée de la pièce, et que devient la pièce de l'une à l'autre ?

::: definition Fabrication additive et chaîne numérique
L'usinage **enlève** de la matière à un brut ; la **fabrication additive** en **ajoute**, ici en déposant un filament de PLA fondu, couche par couche. La fiche de fabrication du manuel suit trois étapes :

1. **Conception** (logiciels 3D et 2D) : modéliser la pièce en 3D à l'échelle 1, puis la **mailler** et l'exporter en **.STL** ;
2. **Tranchage** (Repetier-Host, Slicer, Cura…) : régler la **densité de remplissage** et le type d'adhésion au plateau, trancher, puis exporter en **.Gcode** vers la carte SD ;
3. **Impression** : imprimante sous tension, carte SD insérée, lancement, toujours en présence de l'enseignant.

:::

::: figure La chaîne de la fabrication additive. Les deux premières cases décrivent la forme de la pièce ; le tranchage la découpe en couches ; le fichier .Gcode donne les mouvements de l'imprimante
<svg viewBox="0 0 468 124"><title>Chaîne de la fabrication additive : modèle 3D, maillage STL, tranchage, programme Gcode, imprimante 3D</title><rect x="8" y="40" width="80" height="46" fill="#e9d5ff" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="48" y="60" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Modèle 3D</text><text x="48" y="108" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">la forme</text><line x1="88" y1="63" x2="100" y2="63" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="100 63 95.4 64.9 95.4 61.1" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><rect x="100" y="40" width="80" height="46" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="140" y="60" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Maillage</text><text x="140" y="75" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(.STL)</text><text x="140" y="108" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">la forme</text><line x1="180" y1="63" x2="192" y2="63" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="192 63 187.4 64.9 187.4 61.1" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><rect x="192" y="40" width="80" height="46" fill="#fde68a" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="232" y="60" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Tranchage</text><text x="232" y="108" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">en couches</text><line x1="272" y1="63" x2="284" y2="63" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="284 63 279.4 64.9 279.4 61.1" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><rect x="284" y="40" width="80" height="46" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="324" y="60" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Programme</text><text x="324" y="75" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(.Gcode)</text><text x="324" y="108" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">les mouvements</text><line x1="364" y1="63" x2="376" y2="63" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="376 63 371.4 64.9 371.4 61.1" fill="#0f172a" stroke="#0f172a" stroke-width="0.6" stroke-linejoin="round"/><rect x="376" y="40" width="80" height="46" fill="#fed7aa" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="416" y="60" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Imprimante</text><text x="416" y="108" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">la pièce</text><text x="240" y="22" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">du modèle à la pièce</text></svg>
:::

Chaque case de la figure est un état de la pièce ou une étape de la fiche, et les extensions .STL et .Gcode nomment les deux fichiers qui circulent.

::: exemple Choisir le procédé de trois pièces de la maquette

1. **Arbre planétaire (27)**, PVC, surfaces cylindriques tolérancées (f7, g6) : il part d'un barreau scié et se **tourne**, puis se rainure au fraisage.
2. **Trou taraudé M4** : après perçage, on **taraude** : c'est l'outil (le taraud) qui donne le filet.
3. **Porte-satellite (11)**, PLA, trois bras à 120° : la fiche du manuel le fabrique par **fabrication additive** à partir d'un filament.

:::

::: piege Le .STL n'est pas le programme de l'imprimante
Le **.STL** décrit la **forme** de la pièce par un maillage de petits triangles ; il ne contient aucun mouvement. C'est le **tranchage** qui le transforme en couches et en **.Gcode**, le seul fichier que l'imprimante exécute. Mettre le .STL sur la carte SD ne lance rien d'utile.
:::

::: propriete Remplissage, durée et solidité
Une **densité de remplissage** plus forte rend la pièce plus **solide**, plus **lourde** et plus **longue** à imprimer ; une plus faible l'allège et la raccourcit. Cas limite : le .Gcode parle un langage proche du programme d'usinage (G00, G01…), mais il ne décrit que les mouvements d'un fil déposé, pas la forme de la pièce.
:::

::: verifie
Un porte-satellite imprimé avec une faible densité de remplissage est trop fragile. Que règle-t-on, à quelle étape de la fiche, et qu'y perd-on ?
---

On augmente la **densité de remplissage**, réglée au **tranchage** : la pièce devient plus solide, mais plus lourde et plus longue à imprimer.
:::

## 🧭 La méthode qui reste : huit marches

Devant la fabrication d'une pièce de la maquette, tu reprends toujours cet ordre :

1. **Choisir la configuration du train** : bloquer une pièce, lire r = Ns / Ne, comparer |r| à 1 et regarder son signe.
2. **Lire les cotes tolérancées** : cote maxi, cote mini, IT ; jeu mini = alésage mini − arbre maxi, jeu maxi = alésage maxi − arbre mini.
3. **Fermer la chaîne de cotes** : a32 − Σ des cotes enfermées, maxi contre mini, et les IT s'additionnent.
4. **Écrire la gamme** : contrôler, dégrossir, finir, garder le référentiel, et percer au diamètre moins le pas avant de tarauder.
5. **Mettre en position** : 6 degrés de liberté, au plus 6 points, le serrage ne fait que maintenir.
6. **Régler la coupe** : Vf = f × N, a au rayon, le diamètre baisse de 2 × a.
7. **Programmer** : G00 hors matière, G01 avec F, X au rayon, simuler avant d'usiner.
8. **Choisir le procédé** : enlever de la matière (tournage, fraisage) ou en ajouter (impression), avec un .STL qui décrit la forme et un .Gcode qui la fabrique.

::: retenir
Un **train épicycloïdal** change vitesse et sens selon la pièce bloquée ; une pièce se **tolérance** (jeu mini = alésage mini − arbre maxi) ; les IT d'une **chaîne de cotes** s'additionnent ; la **gamme** ordonne les phases ; **au plus six points** positionnent une pièce ; **Vf = f × N**, avec une passe a au rayon ; **G00** approche, **G01** usine ; et le **.STL** décrit la forme que le **.Gcode** fabrique.
:::

> 🏆 Du train d'engrenages à l'imprimante, tu sais lire un dossier de fabrication. La suite du thème t'attend, avec les synthèses.
