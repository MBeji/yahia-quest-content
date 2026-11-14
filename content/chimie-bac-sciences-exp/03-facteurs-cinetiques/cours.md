# 🌡️ Principaux facteurs cinétiques — ce qui accélère ou ralentit une réaction

> 💡 «On ne change pas la réaction, on change le temps qu'elle met : tout se joue sur trois leviers, la concentration des réactifs, la température et le catalyseur.»

Une pâte à pain lève en une heure près d'un radiateur, un yaourt se garde une semaine au réfrigérateur, un pot catalytique nettoie les gaz d'échappement en une fraction de seconde : sur la même chimie, les conditions changent tout. Huit notions te donnent la clé : le facteur cinétique, la concentration des réactifs, la température et la trempe, la surface de contact d'un solide, le catalyseur et la catalyse, la catalyse homogène et son mécanisme, les catalyses hétérogène et enzymatique avec la spécificité, puis la lecture de courbes d'avancement. On suppose acquis l'avancement x, le tableau descriptif et le réactif limitant (chapitre 1), la vitesse moyenne, la vitesse instantanée et la tangente (chapitre 2), ainsi que le calcul d'une quantité de matière (n = C·V, n = m/M, V = n·V_m) et la dilution.

## 🎛️ Le facteur cinétique

La réaction support de ce chapitre est l'oxydation des ions iodure par les ions peroxodisulfate : 2 I⁻ + S₂O₈²⁻ → I₂ + 2 SO₄²⁻. À 20 °C, avec des solutions diluées, le diiode met plusieurs minutes à colorer le mélange ; avec exactement les mêmes réactifs, mais dans d'autres conditions, quelques secondes suffisent.
Qu'est-ce qui a changé, et sur quoi cela agit-il : sur la réaction elle-même, ou sur le temps qu'elle met ?

::: definition
**Facteur cinétique** — Un facteur cinétique est un paramètre qui influe sur la vitesse d'évolution d'un système chimique. La nature des réactifs fixe d'abord la rapidité de principe d'une réaction ; les conditions expérimentales la modulent. Les trois principaux facteurs cinétiques sont la concentration des réactifs, la température et le catalyseur.
:::

| facteur cinétique | exemple d'action sur le mélange iodure–peroxodisulfate | effet sur la vitesse |
| --- | --- | --- |
| concentration des réactifs | ajouter de l'eau | elle diminue |
| température | plonger le bécher dans un bain chaud | elle augmente |
| catalyseur | ajouter quelques gouttes d'une solution d'ions Fe²⁺ | elle augmente |

Dans les trois lignes l'équation de la réaction reste la même : un facteur cinétique règle la vitesse, il ne change pas ce qui réagit.

::: exemple Reconnaître le facteur cinétique

On observe trois modifications du mélange 2 I⁻ + S₂O₈²⁻ → I₂ + 2 SO₄²⁻ :

- (A) le bécher est placé dans un bain à 40 °C au lieu de 20 °C : le bleu de l'amidon apparaît plus tôt ;
- (B) on ajoute 50 mL d'eau au mélange : le bleu apparaît plus tard ;
- (C) on ajoute 2 gouttes d'une solution d'ions Fe²⁺ : le bleu apparaît presque aussitôt.

1. En (A), un seul paramètre change, la température (20 °C → 40 °C) : le facteur cinétique est la température, et la vitesse augmente.
2. En (B), les quantités de réactifs sont les mêmes mais le volume est plus grand, donc les concentrations des réactifs diminuent : le facteur est la concentration, et la vitesse diminue.
3. En (C), on ajoute en très petite quantité une espèce absente de l'équation : c'est un catalyseur (notion 5), et la vitesse augmente.
4. Dans les trois cas l'équation est la même : on a agi sur la vitesse, pas sur la réaction.

:::

::: piege
**Erreur : croire qu'un facteur cinétique change ce qu'on obtient à la fin.** On entend « à 40 °C on obtiendrait plus de diiode qu'à 20 °C ». C'est faux : si le mélange contient 2,0·10⁻³ mol de S₂O₈²⁻ (réactif limitant) et 6,0·10⁻³ mol de I⁻, l'avancement maximal vaut x_max = 2,0·10⁻³ mol à 20 °C comme à 40 °C. L'erreur tente parce que « plus rapide » sonne comme « plus efficace » ; en réalité seul le temps pour atteindre x_max change.
:::

::: propriete
**Isoler un facteur** — Pour mettre en évidence l'effet d'un facteur cinétique, on compare deux expériences qui ne diffèrent que par ce facteur. Si deux paramètres changent à la fois, l'écart de durée ne se rattache à aucun des deux.
Cas limite : un facteur cinétique agit sur la vitesse, pas sur l'avancement final x_f d'une transformation totale, qui reste fixé par le réactif limitant.
:::

::: verifie À toi : nommer le facteur
Deux tubes contiennent le même mélange iodure–peroxodisulfate à 20 °C. On ajoute 20 mL d'eau au tube A et 0,5 mL d'une solution d'ions Fe²⁺ à 1,0·10⁻² mol·L⁻¹ au tube B. Quel facteur cinétique agit dans chaque tube, et dans quel sens varie la vitesse ?

---

Tube A : l'eau dilue le mélange, les concentrations des réactifs diminuent, le facteur est la concentration et la vitesse diminue. Tube B : une très petite quantité d'une espèce absente de l'équation est ajoutée, c'est un catalyseur et la vitesse augmente.
:::

::: retenir
Un facteur cinétique (concentration des réactifs, température, catalyseur) modifie la vitesse d'évolution, pas l'avancement final ; on l'isole en ne changeant qu'un paramètre à la fois.
:::

## 🧪 La concentration des réactifs

Dans l'horloge iodométrique, on mélange 20,0 mL de K₂S₂O₈ à 4,0·10⁻² mol·L⁻¹, 2,0 mL de thiosulfate de sodium à 0,100 mol·L⁻¹, 3,0 mL d'empois d'amidon et, à t = 0, 25,0 mL de KI à 0,40 mol·L⁻¹. Le thiosulfate consomme le diiode dès qu'il se forme ; le bleu de l'amidon apparaît quand il est épuisé, donc quand l'avancement x = 1,0·10⁻⁴ mol est atteint, toujours le même puisque la quantité de thiosulfate est toujours la même (chapitre 2). On refait l'expérience en changeant une concentration à la fois (durées choisies pour l'exemple).
Comment calculer les concentrations réellement présentes dans le mélange, et que disent les durées ?

::: definition
**Concentration initiale dans un mélange** — À l'instant du mélange, la quantité de matière de chaque réactif est celle de la solution prélevée, mais elle se répartit dans le volume total du mélange : [X]₀ = C·V / V_total, où C et V sont la concentration et le volume de la solution prélevée.
:::

| bécher | K₂S₂O₈ (20,0 mL) | KI (25,0 mL) | durée avant le bleu |
| --- | --- | --- | --- |
| A | 4,0·10⁻² mol·L⁻¹ | 0,40 mol·L⁻¹ | 40 s |
| B | 2,0·10⁻² mol·L⁻¹ | 0,40 mol·L⁻¹ | 85 s |
| C | 4,0·10⁻² mol·L⁻¹ | 0,10 mol·L⁻¹ | 150 s |

Dans chaque bécher le volume total est le même : c'est ce volume, et non celui de la solution prélevée, qui sert de dénominateur.

::: exemple Comparer A, B et C

1. Volume total : V_total = 20,0 + 2,0 + 3,0 + 25,0 = 50,0 mL, car tout ce qui a été versé se retrouve dans le mélange.
2. Bécher A : n(S₂O₈²⁻) = 4,0·10⁻² × 20,0·10⁻³ = 8,0·10⁻⁴ mol, donc [S₂O₈²⁻]₀ = 8,0·10⁻⁴ / 50,0·10⁻³ = 1,6·10⁻² mol·L⁻¹ ; [I⁻]₀ = 0,40 × 25,0 / 50,0 = 0,20 mol·L⁻¹.
3. Bécher B : [S₂O₈²⁻]₀ = 2,0·10⁻² × 20,0 / 50,0 = 8,0·10⁻³ mol·L⁻¹, [I⁻]₀ = 0,20 mol·L⁻¹. Bécher C : [S₂O₈²⁻]₀ = 1,6·10⁻² mol·L⁻¹, [I⁻]₀ = 0,10 × 25,0 / 50,0 = 5,0·10⁻² mol·L⁻¹.
4. Le même avancement est atteint dans les trois béchers, donc les durées se comparent : 85 s et 150 s sont plus longues que 40 s, les réactions B et C sont plus lentes que A.
5. De A à B, seule [S₂O₈²⁻]₀ diminue ; de A à C, seule [I⁻]₀ diminue : une concentration plus faible ralentit la réaction. Contrôle : v_moy = x/Δt vaut 2,5·10⁻⁶ (A), 1,2·10⁻⁶ (B) et 6,7·10⁻⁷ mol·s⁻¹ (C), valeurs décroissantes.

:::

::: piege
**Erreur : « même quantité de réactif, donc même vitesse ».** Dans le bécher A, on ajoute aussitôt 50,0 mL d'eau : il y a toujours 8,0·10⁻⁴ mol de S₂O₈²⁻ et 1,0·10⁻² mol de I⁻, mais le volume passe à 100,0 mL et les concentrations sont divisées par 2 (8,0·10⁻³ et 0,10 mol·L⁻¹) : le bleu apparaît plus tard que 40 s. L'erreur tente parce que la même quantité de matière donne l'impression de la même « réserve » à consommer. La vitesse suit la concentration, pas la quantité de matière.
:::

::: propriete
**Concentration et vitesse** — En général, la vitesse d'une réaction décroît quand les concentrations des réactifs décroissent.
Interprétation microscopique : les entités sont animées d'une agitation thermique permanente ; une transformation exige des chocs assez énergétiques pour rompre des liaisons et en former de nouvelles, les chocs efficaces. Plus la probabilité des chocs entre réactifs est grande, plus il y a de chocs efficaces pendant une durée donnée. Cette probabilité est grande quand le volume est petit et que le nombre de molécules est élevé : c'est exactement la concentration.
Cas limite : à volume constant, ajouter du réactif augmente la concentration et accélère ; ajouter de l'eau à quantité de matière constante diminue la concentration et ralentit, sans changer l'avancement maximal.
:::

::: verifie À toi : calculer puis comparer
Un bécher D reçoit 10,0 mL de K₂S₂O₈ à 5,0·10⁻² mol·L⁻¹ et 15,0 mL de KI à 0,30 mol·L⁻¹, avec la même quantité de thiosulfate et d'amidon ; le volume total du mélange vaut 50,0 mL. Calculer [S₂O₈²⁻]₀ et [I⁻]₀, puis dire si D est plus rapide ou plus lent que le bécher A.

---

[S₂O₈²⁻]₀ = 5,0·10⁻² × 10,0 / 50,0 = 1,0·10⁻² mol·L⁻¹ et [I⁻]₀ = 0,30 × 15,0 / 50,0 = 9,0·10⁻² mol·L⁻¹. Les deux concentrations sont inférieures à celles de A (1,6·10⁻² et 0,20 mol·L⁻¹) : D est plus lent, le bleu apparaît après plus de 40 s.
:::

::: retenir
La concentration initiale se calcule avec le volume total du mélange, et en général la vitesse décroît quand les concentrations des réactifs décroissent.
:::

## 🔥 La température et la trempe

Trois tubes contiennent le même mélange iodure–peroxodisulfate : l'un est plongé dans un bain à 60 °C, l'autre reste à 20 °C, le troisième est dans de l'eau glacée. Après 2 min, la coloration jaune-brun du diiode est intense dans le premier tube, moyenne dans le deuxième, à peine visible dans le troisième.
Que dit cette observation sur la vitesse, et qu'est-ce qui change à l'échelle des entités chimiques ?

::: figure Courbes d'illustration x(t) du même mélange à 20 °C et à 40 °C : même valeur finale x_max = 6,0 mmol
<svg viewBox="0 0 340 236"><title>Courbes x(t) du même mélange à 20 °C et à 40 °C</title><line x1="54.0" y1="26.0" x2="54.0" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="144.7" y1="26.0" x2="144.7" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="235.3" y1="26.0" x2="235.3" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="326.0" y1="26.0" x2="326.0" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54.0" y1="190.0" x2="326.0" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54.0" y1="149.0" x2="326.0" y2="149.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54.0" y1="108.0" x2="326.0" y2="108.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54.0" y1="67.0" x2="326.0" y2="67.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54.0" y1="26.0" x2="326.0" y2="26.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54.0" y1="190.0" x2="332.0" y2="190.0" stroke="#0f172a" stroke-width="1.6"/><line x1="54.0" y1="190.0" x2="54.0" y2="18.0" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="54.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="144.7" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="235.3" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="326.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><text x="48.0" y="194.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="48.0" y="153.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="48.0" y="112.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><text x="48.0" y="71.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="48.0" y="30.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><text x="334.0" y="218.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (min)</text><text x="60.0" y="12.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x (mmol)</text><line x1="54.0" y1="67.0" x2="326.0" y2="67.0" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4 3"/><polyline points="54.0,190.0 57.4,186.2 60.8,182.5 64.2,179.0 67.6,175.5 71.0,172.2 74.4,169.0 77.8,165.8 81.2,162.8 84.6,159.8 88.0,157.0 91.4,154.2 94.8,151.5 98.2,148.9 101.6,146.4 105.0,144.0 108.4,141.6 111.8,139.3 115.2,137.1 118.6,134.9 122.0,132.8 125.4,130.8 128.8,128.8 132.2,126.9 135.6,125.1 139.0,123.3 142.4,121.6 145.8,119.9 149.2,118.3 152.6,116.7 156.0,115.2 159.4,113.7 162.8,112.2 166.2,110.9 169.6,109.5 173.0,108.2 176.4,106.9 179.8,105.7 183.2,104.5 186.6,103.4 190.0,102.2 193.4,101.2 196.8,100.1 200.2,99.1 203.6,98.1 207.0,97.1 210.4,96.2 213.8,95.3 217.2,94.4 220.6,93.6 224.0,92.8 227.4,92.0 230.8,91.2 234.2,90.5 237.6,89.8 241.0,89.1 244.4,88.4 247.8,87.7 251.2,87.1 254.6,86.5 258.0,85.9 261.4,85.3 264.8,84.7 268.2,84.2 271.6,83.6 275.0,83.1 278.4,82.6 281.8,82.2 285.2,81.7 288.6,81.2 292.0,80.8 295.4,80.4 298.8,80.0 302.2,79.6 305.6,79.2 309.0,78.8 312.4,78.4 315.8,78.1 319.2,77.7 322.6,77.4 326.0,77.1" fill="none" stroke="#1d4ed8" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="54.0,190.0 57.4,179.0 60.8,169.0 64.2,159.8 67.6,151.5 71.0,144.0 74.4,137.1 77.8,130.8 81.2,125.1 84.6,119.9 88.0,115.2 91.4,110.9 94.8,106.9 98.2,103.4 101.6,100.1 105.0,97.1 108.4,94.4 111.8,92.0 115.2,89.8 118.6,87.7 122.0,85.9 125.4,84.2 128.8,82.6 132.2,81.2 135.6,80.0 139.0,78.8 142.4,77.7 145.8,76.8 149.2,75.9 152.6,75.1 156.0,74.4 159.4,73.7 162.8,73.1 166.2,72.6 169.6,72.1 173.0,71.6 176.4,71.2 179.8,70.8 183.2,70.5 186.6,70.2 190.0,69.9 193.4,69.6 196.8,69.4 200.2,69.2 203.6,69.0 207.0,68.8 210.4,68.6 213.8,68.5 217.2,68.4 220.6,68.2 224.0,68.1 227.4,68.0 230.8,67.9 234.2,67.9 237.6,67.8 241.0,67.7 244.4,67.6 247.8,67.6 251.2,67.5 254.6,67.5 258.0,67.4 261.4,67.4 264.8,67.4 268.2,67.3 271.6,67.3 275.0,67.3 278.4,67.3 281.8,67.2 285.2,67.2 288.6,67.2 292.0,67.2 295.4,67.2 298.8,67.1 302.2,67.1 305.6,67.1 309.0,67.1 312.4,67.1 315.8,67.1 319.2,67.1 322.6,67.1 326.0,67.1" fill="none" stroke="#c2410c" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="144.7" y1="190.0" x2="144.7" y2="77.1" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4 3"/><circle cx="144.7" cy="120.5" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><circle cx="144.7" cy="77.1" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><text x="150.7" y="134.5" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3,4</text><text x="150.7" y="71.1" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5,5</text><text x="190.0" y="45.9" text-anchor="middle" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40 °C</text><text x="280.7" y="104.3" text-anchor="middle" font-size="12" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20 °C</text><text x="316.9" y="61.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x_max = 6,0</text><text x="144.7" y="184.0" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t = 10 min</text></svg>
:::

Les deux courbes tendent vers la même valeur x_max = 6,0 mmol, mais celle de 40 °C monte beaucoup plus vite au départ : à t = 10 min, x vaut environ 5,5 mmol à 40 °C contre 3,4 mmol à 20 °C.

::: exemple Lire l'effet de la température sur la figure

1. À t = 10 min, x ≈ 3,4 mmol à 20 °C et x ≈ 5,5 mmol à 40 °C : pour la même durée, Δx est plus grand à 40 °C, donc la transformation y est plus rapide.
2. v_moy(0 ; 10) = x/10 ≈ 0,34 mmol·min⁻¹ à 20 °C et ≈ 0,55 mmol·min⁻¹ à 40 °C, car la vitesse moyenne est Δx/Δt.
3. Pour atteindre x = 4,5 mmol (les trois quarts de x_max), il faut environ 17 min à 20 °C et environ 5,5 min à 40 °C : pour le même Δx, la durée est plus courte à 40 °C.
4. Les deux paliers valent 6,0 mmol : les mélanges contiennent les mêmes réactifs, la température modifie le temps mis, pas x_max.

:::

::: propriete
**Température et vitesse** — En général, la vitesse d'une réaction croît quand la température croît.
Interprétation microscopique : les entités n'ont pas toutes la même énergie cinétique. Quand la température s'élève, l'agitation thermique augmente : les chocs sont plus fréquents et plus énergétiques, donc la probabilité d'un choc efficace est plus grande.
Cas limite : les enzymes (notion 7) n'agissent que dans une plage de température particulière ; la règle « plus chaud, plus rapide » décrit les réactions de ce chapitre sans catalyseur biologique.
:::

::: definition
**Trempe** — La trempe est un refroidissement brusque d'un système chimique dont on veut arrêter l'évolution, par exemple en versant un prélèvement dans de l'eau glacée. L'eau glacée agit sur deux facteurs cinétiques : elle refroidit (température) et elle dilue (concentration).
:::

::: exemple Suivre x par des prélèvements trempés

On suit I⁻/S₂O₈²⁻ dans un mélange de volume V_sln = 60,0 mL. À t = 6 min, on prélève 5,0 mL que l'on verse dans 40,0 mL d'eau glacée, puis on dose I₂ par du thiosulfate à C₃ = 1,0·10⁻² mol·L⁻¹ : l'équivalence est atteinte pour V_E = 9,0 mL, selon I₂ + 2 S₂O₃²⁻ → S₄O₆²⁻ + 2 I⁻.

1. La trempe fige le prélèvement : la température chute et les concentrations sont divisées par (5,0 + 40,0)/5,0 = 9, deux facteurs qui ralentissent la réaction au point que la composition ne change plus pendant le dosage.
2. À l'équivalence, n(S₂O₃²⁻) versé = 2·n(I₂), car l'équation de dosage a le coefficient 2 devant S₂O₃²⁻ : n(I₂) = C₃·V_E/2 = 1,0·10⁻² × 9,0·10⁻³ / 2 = 4,5·10⁻⁵ mol dans le prélèvement.
3. Le prélèvement est une fraction V/V_sln = 5,0/60,0 du mélange : n(I₂) dans tout le mélange = 4,5·10⁻⁵ × 60,0/5,0 = 5,4·10⁻⁴ mol.
4. Le coefficient de I₂ vaut 1 et il n'y en avait pas au départ : x(6 min) = 5,4·10⁻⁴ mol.

:::

::: piege
**Erreur : croire que le froid arrête la réaction.** Un aliment au réfrigérateur (environ 4 °C) se conserve quelques jours, au congélateur (environ −20 °C) plusieurs mois : le froid ralentit beaucoup la réaction, il ne la supprime pas. La trempe fait de même à court terme : la vitesse devient négligeable pendant la durée du dosage, elle n'est pas nulle. L'erreur tente parce que « glacé » évoque l'immobilité.
:::

::: verifie À toi : pourquoi de l'eau glacée
Pourquoi verse-t-on le prélèvement dans de l'eau glacée plutôt que dans de l'eau à 20 °C avant le dosage ?

---

Dans l'eau à 20 °C, on dilue seulement : la concentration diminue, mais la température reste la même et la réaction se poursuit sensiblement. Dans l'eau glacée, la dilution et le refroidissement agissent ensemble : deux facteurs cinétiques ralentissent la réaction, qui devient négligeable pendant le dosage.
:::

::: retenir
En général la vitesse croît avec la température (chocs plus fréquents et plus énergétiques), sans changer x_max ; la trempe refroidit et dilue pour ralentir assez la réaction avant le dosage.
:::

## 🧊 La surface de contact d'un solide

Un comprimé effervescent entier met plusieurs minutes à réagir dans un verre d'eau ; la même masse de comprimé écrasée en poudre réagit en quelques secondes. Même eau, même température, même quantité de matière.
Pourquoi diviser un solide accélère-t-il la réaction ?

::: definition
**Surface de contact** — Quand une réaction se produit à l'interface solide-liquide ou solide-gaz, elle ne se produit qu'à cette interface : elle est d'autant plus rapide que l'interface est grande. Diviser un solide en portions de plus en plus petites augmente sa surface totale.
:::

::: figure Un cube d'arête a coupé en deux pavés a × a × a/2 : la surface totale passe de 6a² à 8a²
<svg viewBox="0 0 340 190"><title>Un cube d'arête a coupé en deux pavés : la surface totale passe de 6a² à 8a²</title><polygon points="28,70 92,70 92,134 28,134" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><polygon points="28,70 50,48 114,48 92,70" fill="#dbeafe" stroke="#0f172a" stroke-width="2"/><polygon points="92,70 114,48 114,112 92,134" fill="#93c5fd" stroke="#0f172a" stroke-width="2"/><text x="60.0" y="152.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">a</text><text x="60.0" y="174.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">cube : S₁ = 6a²</text><line x1="118.0" y1="96.0" x2="160.0" y2="96.0" stroke="#0f172a" stroke-width="2"/><polygon points="166,96 156,91 156,101" fill="#0f172a"/><text x="142.0" y="86.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">coupe</text><polygon points="196,44 260,44 260,76 196,76" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><polygon points="196,44 218,22 282,22 260,44" fill="#dbeafe" stroke="#0f172a" stroke-width="2"/><polygon points="260,44 282,22 282,54 260,76" fill="#93c5fd" stroke="#0f172a" stroke-width="2"/><polygon points="196,118 260,118 260,150 196,150" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><polygon points="196,118 218,96 282,96 260,118" fill="#dbeafe" stroke="#0f172a" stroke-width="2"/><polygon points="260,118 282,96 282,128 260,150" fill="#93c5fd" stroke="#0f172a" stroke-width="2"/><text x="290.0" y="68.0" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">a/2</text><text x="290.0" y="142.0" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">a/2</text><text x="228.0" y="178.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">deux pavés : S₂ = 8a²</text></svg>
:::

Le cube a six faces de surface a², soit 6a². Chaque pavé a deux faces a × a et quatre faces a × a/2, soit 2a² + 2a² = 4a² ; deux pavés font donc 8a², supérieur à 6a².

::: exemple Surface totale d'un cube de 2,0 cm de côté

1. Cube entier : S = 6a² = 6 × (2,0)² = 24 cm², car il a six faces carrées de 4,0 cm².
2. Coupé en deux pavés de 2,0 × 2,0 × 1,0 cm : chacun a 2 × (2,0 × 2,0) + 4 × (2,0 × 1,0) = 8,0 + 8,0 = 16 cm², soit 32 cm² pour les deux, ce que donne aussi 8a² = 32 cm².
3. Coupé en 8 cubes de 1,0 cm de côté : chacun a 6 × (1,0)² = 6,0 cm², soit 48 cm² au total.
4. La matière est la même dans les trois cas, mais la surface passe de 24 à 32 puis à 48 cm² : couper crée de nouvelles faces. En divisant l'arête par 2, on a multiplié la surface par 2.

:::

::: piege
**Erreur : penser que couper un solide ne change pas sa surface, puisque la matière reste la même.** La masse et le volume sont conservés, pas la surface : 24 cm² deviennent 32 puis 48 cm², parce que chaque coupe fait apparaître deux faces nouvelles. L'erreur tente parce qu'on n'a rien ajouté, rien retiré.
:::

::: propriete
**Surface de contact et vitesse** — Pour une réaction à l'interface solide-liquide ou solide-gaz, la réaction est d'autant plus rapide que l'interface est grande ; à masse égale, un solide en poudre réagit plus vite qu'en morceau.
Cas limite : une surface plus grande accélère la réaction mais ne change pas l'avancement maximal, qui dépend de la quantité de solide et non de son état de division.
:::

::: verifie À toi : couper un cube
Un cube de 3,0 cm de côté est coupé en deux pavés égaux. Quelle est sa surface totale avant et après la coupe ? Dans quel état réagit-il le plus vite avec un liquide ?

---

Avant : 6a² = 6 × (3,0)² = 54 cm². Après : 8a² = 8 × (3,0)² = 72 cm². Après la coupe la surface est plus grande, donc la réaction avec un liquide est plus rapide.
:::

::: retenir
À l'interface solide-liquide ou solide-gaz, plus l'interface est grande, plus la réaction est rapide ; diviser un solide augmente sa surface totale.
:::

## 🧬 Le catalyseur et la catalyse

On ajoute 2 gouttes d'une solution d'ions Fe²⁺ (1,0·10⁻² mol·L⁻¹) au mélange 2 I⁻ + S₂O₈²⁻ → I₂ + 2 SO₄²⁻ : le diiode apparaît presque aussitôt. En fin de réaction, on décolore le diiode avec du thiosulfate, puis quelques gouttes de soude donnent un précipité vert d'hydroxyde de fer (II) : les ions fer (II) sont toujours là.
Comment une espèce peut-elle accélérer une réaction sans être consommée, et comment la distinguer d'un réactif ?

::: definition
**Catalyseur** — Un catalyseur est une entité chimique, utilisée en faible proportion, capable d'augmenter la vitesse d'une réaction possible spontanément en son absence. La catalyse est l'action d'un catalyseur sur une réaction.
:::

| | réactif | catalyseur |
| --- | --- | --- |
| figure dans l'équation de la réaction | oui | non |
| sa quantité de matière globalement | elle diminue | elle n'est pas consommée (régénérée) |
| sa quantité à la fin par rapport au début | plus faible | la même |

Le tableau fournit deux tests : on regarde si l'espèce figure dans l'équation, et on compare sa quantité avant et après la réaction.

::: exemple Distinguer un réactif d'un catalyseur

Système 1 : 0,10 g de magnésium (M = 24,3 g·mol⁻¹) réagit avec 20,0 mL d'acide chlorhydrique à 0,50 mol·L⁻¹ selon Mg + 2 H₃O⁺ → Mg²⁺ + H₂ + 2 H₂O ; la réaction est plus rapide avec un acide plus concentré. L'ion H₃O⁺ est-il un catalyseur ?

1. n(Mg) = 0,10 / 24,3 = 4,1·10⁻³ mol et n(H₃O⁺)ᵢ = 0,50 × 20,0·10⁻³ = 1,0·10⁻² mol, car n = m/M et n = C·V.
2. Le magnésium est le réactif limitant, car il en faut 2 × 4,1·10⁻³ = 8,2·10⁻³ mol de H₃O⁺, moins que les 1,0·10⁻² mol disponibles : x_max = 4,1·10⁻³ mol.
3. En fin de réaction, n(H₃O⁺) = 1,0·10⁻² − 2 × 4,1·10⁻³ = 1,8·10⁻³ mol, très inférieur à 1,0·10⁻² mol : H₃O⁺ figure dans l'équation et il est consommé, c'est un réactif. Sa concentration agit comme celle d'un réactif (notion 2), pas comme un catalyseur.
4. Système 2 : I⁻/S₂O₈²⁻ avec Fe²⁺. L'ion Fe²⁺ ne figure pas dans 2 I⁻ + S₂O₈²⁻ → I₂ + 2 SO₄²⁻ et le précipité vert montre qu'on le retrouve en fin de réaction : c'est un catalyseur.

:::

::: piege
**Erreur : prendre pour catalyseur toute espèce qui accélère la réaction.** L'acide H₃O⁺ accélère la réaction du magnésium quand sa concentration augmente, pourtant sa quantité passe de 1,0·10⁻² à 1,8·10⁻³ mol : il est consommé. L'erreur tente parce que « ça accélère » ressemble à la définition. Les deux tests (figurer dans l'équation, quantité finale) départagent un réactif d'un catalyseur.
:::

::: propriete
**Propriétés du catalyseur** — Un catalyseur est utilisé en faible proportion ; il ne rend pas possible une transformation impossible spontanément ; il ne modifie pas la composition du système à la fin de la transformation ; s'il accélère une réaction possible spontanément, il accélère aussi la réaction inverse quand elle est possible spontanément.
Cas limite : la même entité peut jouer deux rôles : H₃O⁺ est un réactif avec le magnésium, mais un catalyseur dans l'hydrolyse du butanoate d'éthyle C₃H₇COOC₂H₅ + H₂O → C₃H₇COOH + C₂H₅OH (réaction lente et limitée, étudiée au chapitre 4), où il ne figure pas dans l'équation. Le rôle se lit dans l'équation de chaque réaction.
:::

::: verifie À toi : réactif ou catalyseur
Dans H₂O₂ + 2 I⁻ + 2 H₃O⁺ → I₂ + 4 H₂O, un mélange contient n(H₃O⁺)ᵢ = 6,0·10⁻³ mol et la réaction atteint x_f = 1,0·10⁻³ mol. L'ion H₃O⁺ est-il un catalyseur ?

---

H₃O⁺ figure dans l'équation avec le coefficient 2 : n(H₃O⁺)_f = 6,0·10⁻³ − 2 × 1,0·10⁻³ = 4,0·10⁻³ mol, différent de la quantité initiale. Il est consommé, c'est donc un réactif et non un catalyseur.
:::

::: retenir
Un catalyseur accélère une réaction possible spontanément, ne figure pas dans l'équation et se retrouve en même quantité à la fin ; un réactif y figure et est consommé.
:::

## 🔁 La catalyse homogène et son mécanisme

Les ions fer (II) Fe²⁺, comme les ions fer (III) Fe³⁺, accélèrent 2 I⁻ + S₂O₈²⁻ → I₂ + 2 SO₄²⁻. Ils sont dissous dans la solution, au milieu des réactifs, et pourtant quelques gouttes suffisent.
Comment le catalyseur participe-t-il à la réaction sans être consommé ?

::: definition
**Catalyse homogène** — La catalyse est homogène lorsque le catalyseur et les réactifs appartiennent à une même phase.
:::

::: figure Cycle du catalyseur : Fe²⁺ est consommé à l'étape 1, puis régénéré à l'étape 2
<svg viewBox="0 0 340 160"><title>Cycle du catalyseur : Fe²⁺ est consommé à l'étape 1 puis régénéré à l'étape 2</title><ellipse cx="52" cy="80" rx="42" ry="24" fill="#dcfce7" stroke="#0f172a" stroke-width="2"/><ellipse cx="288" cy="80" rx="42" ry="24" fill="#fef3c7" stroke="#0f172a" stroke-width="2"/><text x="52.0" y="85.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2 Fe²⁺</text><text x="288.0" y="85.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2 Fe³⁺</text><line x1="100.0" y1="62.0" x2="232.0" y2="62.0" stroke="#0f172a" stroke-width="2.4"/><polygon points="240,62 230,57 230,67" fill="#0f172a"/><text x="170.0" y="30.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">étape 1</text><text x="170.0" y="46.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+ S₂O₈²⁻ → 2 SO₄²⁻</text><line x1="240.0" y1="100.0" x2="108.0" y2="100.0" stroke="#0f172a" stroke-width="2.4"/><polygon points="100,100 110,95 110,105" fill="#0f172a"/><text x="170.0" y="120.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">étape 2</text><text x="170.0" y="136.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+ 2 I⁻ → I₂</text></svg>
:::

À l'étape 1, l'ion Fe²⁺ réagit avec S₂O₈²⁻ et devient Fe³⁺ ; à l'étape 2, Fe³⁺ réagit avec I⁻ et redevient Fe²⁺ : la flèche du bas boucle sur la flèche du haut.

::: exemple Additionner les deux étapes

Étape 1 : 2 Fe²⁺ + S₂O₈²⁻ → 2 Fe³⁺ + 2 SO₄²⁻. Étape 2 : 2 Fe³⁺ + 2 I⁻ → 2 Fe²⁺ + I₂.

1. On additionne membre à membre : 2 Fe²⁺ + S₂O₈²⁻ + 2 Fe³⁺ + 2 I⁻ → 2 Fe³⁺ + 2 SO₄²⁻ + 2 Fe²⁺ + I₂.
2. On simplifie les espèces présentes des deux côtés : 2 Fe²⁺ et 2 Fe³⁺ disparaissent, car ce qui est consommé dans une étape est reformé dans l'autre.
3. Il reste 2 I⁻ + S₂O₈²⁻ → I₂ + 2 SO₄²⁻ : c'est l'équation de la réaction, sans le catalyseur.
4. Contrôle des charges de l'étape 2 : à gauche 2 × (+3) + 2 × (−1) = +4, à droite 2 × (+2) = +4 ✓.
5. Le catalyseur est réactif à l'étape 1 et produit à l'étape 2 : il est régénéré, donc il n'est pas consommé globalement. La réaction lente est remplacée par deux réactions rapides.

:::

::: exemple Deux tubes d'eau oxygénée

On verse 5,0 mL d'eau oxygénée dans chaque tube, puis 1,0 mL de sulfate de fer (III) Fe₂(SO₄)₃ à 0,10 mol·L⁻¹ dans le tube (1) et à 0,50 mol·L⁻¹ dans le tube (2). Un gaz se dégage dans les deux, plus vivement dans (2) ; une bûchette à point incandescent s'y rallume.

1. La bûchette qui se rallume identifie le dioxygène : 2 H₂O₂ → O₂ + 2 H₂O, une réaction très lente sans catalyseur.
2. Fe₂(SO₄)₃ libère 2 Fe³⁺ par unité formulaire, et le volume total vaut 6,0 mL.
3. Tube (1) : [Fe³⁺] = 2 × 0,10 × 1,0 / 6,0 = 3,3·10⁻² mol·L⁻¹ ; tube (2) : [Fe³⁺] = 2 × 0,50 × 1,0 / 6,0 = 0,17 mol·L⁻¹.
4. Le dégagement est plus vif où la concentration en catalyseur est plus grande : l'activité du catalyseur est liée à sa concentration.

:::

::: piege
**Erreur : écrire la seconde étape avec un seul ion iodure.** « 2 Fe³⁺ + I⁻ → 2 Fe²⁺ + I₂ » n'est pas équilibrée : les charges valent 2 × (+3) + (−1) = +5 à gauche mais 2 × (+2) = +4 à droite, et il y a un atome d'iode à gauche pour deux à droite. L'erreur tente parce qu'on recopie le coefficient 2 du fer. La bonne équation est 2 Fe³⁺ + 2 I⁻ → 2 Fe²⁺ + I₂.
:::

::: propriete
**Mécanisme de la catalyse homogène** — Lors d'une catalyse, la réaction globale lente est remplacée par deux ou plusieurs réactions rapides auxquelles participe le catalyseur, d'abord comme réactif puis comme produit : il est régénéré, donc globalement non consommé. L'activité du catalyseur est liée à sa concentration.
Cas limite : on peut introduire Fe²⁺ ou Fe³⁺, car chacun est un maillon du même cycle ; dans les deux cas l'avancement final est le même.
:::

::: verifie À toi : partir de Fe³⁺
On introduit des ions Fe³⁺ au départ, dans le mélange I⁻/S₂O₈²⁻. Quelle étape se produit en premier, et que donne la somme des deux étapes ?

---

Fe³⁺ est le réactif de l'étape 2, qui a lieu en premier : 2 Fe³⁺ + 2 I⁻ → 2 Fe²⁺ + I₂ ; les Fe²⁺ formés réagissent à l'étape 1 et redonnent 2 Fe³⁺. La somme est la même, 2 I⁻ + S₂O₈²⁻ → I₂ + 2 SO₄²⁻ : Fe³⁺ est régénéré, donc catalyseur.
:::

::: retenir
En catalyse homogène, le catalyseur est dans la même phase que les réactifs et suit un cycle : réactif puis produit, donc régénéré ; son activité croît avec sa concentration.
:::

## ⚙️ Les catalyses hétérogène et enzymatique, la spécificité

Dans un pot catalytique, un bloc de céramique recouvert de platine, de palladium et de rhodium transforme en une fraction de seconde le monoxyde de carbone des gaz d'échappement en dioxyde de carbone : le catalyseur est un solide, les réactifs sont des gaz. Ailleurs, un morceau de foie cru plongé dans de l'eau oxygénée la décompose avec un dégagement vif de dioxygène.
Comment classer ces catalyses, et pourquoi un catalyseur ne fait-il pas n'importe quoi ?

::: definition
**Catalyse hétérogène** — La catalyse est hétérogène lorsque le catalyseur et les réactifs appartiennent à des phases différentes. Son activité est d'autant plus grande que la surface de contact entre les réactifs et le catalyseur est grande.
:::

::: definition
**Enzyme et catalyse enzymatique** — Une enzyme est une molécule biologique qui accélère les réactions chimiques du métabolisme : c'est un catalyseur biologique, et son action est une catalyse enzymatique. La catalase, présente dans le sang et dans certains légumes, accélère 2 H₂O₂ → O₂ + 2 H₂O.
:::

| catalyse | catalyseur et réactifs | exemple |
| --- | --- | --- |
| homogène | une seule phase | ions Fe²⁺ dissous dans la solution d'iodure et de peroxodisulfate |
| hétérogène | phases différentes | PbO₂ ou MnO₂ solide dans l'eau oxygénée ; platine solide et gaz d'échappement |
| enzymatique | catalyseur biologique | catalase du foie ou du navet sur l'eau oxygénée |

Le critère de la première colonne est la phase, pas la nature chimique : on compare dans quelle phase se trouvent le catalyseur et les réactifs.

::: exemple Classer quatre catalyses

1. Des cristaux de PbO₂ sont ajoutés à de l'eau oxygénée : PbO₂ est un solide, les réactifs sont en solution aqueuse, donc deux phases : catalyse hétérogène.
2. Des ions Fe³⁺ sont dissous dans l'eau oxygénée : ils sont dans la même solution, donc une seule phase : catalyse homogène.
3. Dans la synthèse N₂(g) + 3 H₂(g) → 2 NH₃(g) à environ 450 °C, on emploie du fer solide : un solide face à des gaz, deux phases : catalyse hétérogène.
4. Du foie cru plongé dans l'eau oxygénée : la catalase est une enzyme, un catalyseur biologique : catalyse enzymatique.
5. Pourquoi la poudre de PbO₂ est-elle plus active ? Un cube de 1,0 cm de côté a une surface de 6,0 cm² ; divisé en 1000 cubes de 1,0 mm de côté, il offre 1000 × 6 × (0,10)² = 60 cm², dix fois plus : en divisant l'arête par 10, on multiplie la surface par 10.

:::

::: piege
**Erreur : confondre phase et espèce chimique.** Les ions Fe³⁺ et H₂O₂ sont des espèces différentes, mais ils sont dans la même solution aqueuse : une seule phase, donc catalyse homogène. L'erreur tente parce qu'on pense « le catalyseur n'est pas un réactif, donc il est à part ». Le critère est la phase, pas l'espèce.
:::

::: propriete
**Spécificité des catalyseurs** — Un catalyseur n'accélère pas de la même manière n'importe quelle réaction. Avec le cuivre, l'éthanol donne C₂H₅OH → CH₃CHO + H₂ ; avec l'alumine Al₂O₃, il donne C₂H₅OH → CH₂=CH₂ + H₂O : le choix du catalyseur oriente la réaction. Les enzymes sont bien plus actives que les catalyseurs chimiques (l'uréase accélère l'hydrolyse de l'urée d'un facteur d'environ 10¹⁴ par rapport à H₃O⁺), agissent à faible concentration, dans des conditions de température et de pH particulières (environ 37 °C et pH 7,4 dans l'organisme), et ne catalysent qu'un type de réaction sur un type de réactif : la saccharase n'hydrolyse que le saccharose, en glucose et fructose.
Cas limite : à l'échelle industrielle, la catalyse permet de travailler à une température moins élevée et de limiter les réactions parasites ; elle ne modifie pas l'avancement final.
:::

::: verifie À toi : classer et expliquer
Du nickel solide en poudre fine catalyse l'hydrogénation d'un composé dissous dans l'éthanol. Quel est le type de catalyse, et pourquoi emploie-t-on le nickel en poudre plutôt qu'en morceau ?

---

Le nickel est solide, le réactif est en solution : deux phases, la catalyse est hétérogène. La poudre offre une surface de contact plus grande avec les réactifs qu'un morceau de même masse, donc une activité plus grande.
:::

::: retenir
La catalyse est homogène (une phase), hétérogène (phases différentes, activité liée à la surface) ou enzymatique (catalyseur biologique), et un catalyseur est spécifique à un type de réaction.
:::

## 📈 Lire des courbes d'avancement

Quatre expériences sont réalisées sur 2 I⁻ + S₂O₈²⁻ → 2 SO₄²⁻ + I₂ ; les courbes [I₂](t) obtenues sont repérées (a) à (d) (courbes d'illustration). Comme I₂ est absent au départ et que son coefficient vaut 1, [I₂] est l'avancement volumique y.

| expérience | [I⁻]₀ (mmol·L⁻¹) | [S₂O₈²⁻]₀ (mmol·L⁻¹) | température |
| --- | --- | --- | --- |
| E1 | 40 | 12 | 20 °C |
| E2 | 80 | 24 | 20 °C |
| E3 | 40 | 12 | 40 °C |
| E4 | 80 | 24 | 40 °C |

Comment attribuer chaque courbe à son expérience, et comment lire la vitesse initiale ?

::: figure Les quatre courbes [I₂](t) et la tangente à l'origine de (b), qui passe par O(0 ; 0) et par le point (8 ; 24)
<svg viewBox="0 0 340 236"><title>Quatre courbes de [I₂] en fonction du temps, repérées (a) à (d), avec la tangente à l'origine de (b)</title><line x1="54.0" y1="26.0" x2="54.0" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="99.3" y1="26.0" x2="99.3" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="144.7" y1="26.0" x2="144.7" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="190.0" y1="26.0" x2="190.0" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="235.3" y1="26.0" x2="235.3" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="280.7" y1="26.0" x2="280.7" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="326.0" y1="26.0" x2="326.0" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54.0" y1="190.0" x2="326.0" y2="190.0" stroke="#e2e8f0" stroke-width="1"/><line x1="54.0" y1="154.9" x2="326.0" y2="154.9" stroke="#e2e8f0" stroke-width="1"/><line x1="54.0" y1="119.7" x2="326.0" y2="119.7" stroke="#e2e8f0" stroke-width="1"/><line x1="54.0" y1="84.6" x2="326.0" y2="84.6" stroke="#e2e8f0" stroke-width="1"/><line x1="54.0" y1="49.4" x2="326.0" y2="49.4" stroke="#e2e8f0" stroke-width="1"/><line x1="54.0" y1="190.0" x2="332.0" y2="190.0" stroke="#0f172a" stroke-width="1.6"/><line x1="54.0" y1="190.0" x2="54.0" y2="18.0" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="54.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="99.3" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="144.7" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="190.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><text x="235.3" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="280.7" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">50</text><text x="326.0" y="204.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><text x="48.0" y="194.0" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="48.0" y="158.9" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="48.0" y="123.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12</text><text x="48.0" y="88.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">18</text><text x="48.0" y="53.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">24</text><text x="334.0" y="218.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (min)</text><text x="60.0" y="12.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">[I₂] (mmol/L)</text><line x1="54.0" y1="49.4" x2="326.0" y2="49.4" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4 3"/><line x1="54.0" y1="119.7" x2="326.0" y2="119.7" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4 3"/><polyline points="54.0,190.0 57.4,184.8 60.8,179.8 64.2,175.0 67.6,170.4 71.0,166.0 74.4,161.7 77.8,157.5 81.2,153.6 84.6,149.7 88.0,146.0 91.4,142.5 94.8,139.1 98.2,135.8 101.6,132.6 105.0,129.5 108.4,126.6 111.8,123.7 115.2,121.0 118.6,118.4 122.0,115.8 125.4,113.4 128.8,111.0 132.2,108.8 135.6,106.6 139.0,104.5 142.4,102.5 145.8,100.5 149.2,98.6 152.6,96.8 156.0,95.1 159.4,93.4 162.8,91.8 166.2,90.2 169.6,88.7 173.0,87.3 176.4,85.9 179.8,84.5 183.2,83.2 186.6,82.0 190.0,80.8 193.4,79.6 196.8,78.5 200.2,77.5 203.6,76.4 207.0,75.4 210.4,74.5 213.8,73.6 217.2,72.7 220.6,71.8 224.0,71.0 227.4,70.2 230.8,69.4 234.2,68.7 237.6,68.0 241.0,67.3 244.4,66.6 247.8,66.0 251.2,65.4 254.6,64.8 258.0,64.2 261.4,63.7 264.8,63.2 268.2,62.7 271.6,62.2 275.0,61.7 278.4,61.3 281.8,60.8 285.2,60.4 288.6,60.0 292.0,59.6 295.4,59.2 298.8,58.9 302.2,58.5 305.6,58.2 309.0,57.9 312.4,57.6 315.8,57.3 319.2,57.0 322.6,56.7 326.0,56.4" fill="none" stroke="#1d4ed8" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="54.0,190.0 57.4,177.4 60.8,166.0 64.2,155.5 67.6,146.0 71.0,137.4 74.4,129.5 77.8,122.4 81.2,115.8 84.6,109.9 88.0,104.5 91.4,99.6 94.8,95.1 98.2,91.0 101.6,87.3 105.0,83.9 108.4,80.8 111.8,78.0 115.2,75.4 118.6,73.1 122.0,71.0 125.4,69.1 128.8,67.3 132.2,65.7 135.6,64.2 139.0,62.9 142.4,61.7 145.8,60.6 149.2,59.6 152.6,58.7 156.0,57.9 159.4,57.1 162.8,56.4 166.2,55.8 169.6,55.2 173.0,54.7 176.4,54.2 179.8,53.8 183.2,53.4 186.6,53.1 190.0,52.7 193.4,52.4 196.8,52.2 200.2,51.9 203.6,51.7 207.0,51.5 210.4,51.3 213.8,51.1 217.2,51.0 220.6,50.9 224.0,50.7 227.4,50.6 230.8,50.5 234.2,50.4 237.6,50.3 241.0,50.2 244.4,50.2 247.8,50.1 251.2,50.0 254.6,50.0 258.0,49.9 261.4,49.9 264.8,49.8 268.2,49.8 271.6,49.8 275.0,49.7 278.4,49.7 281.8,49.7 285.2,49.7 288.6,49.6 292.0,49.6 295.4,49.6 298.8,49.6 302.2,49.6 305.6,49.6 309.0,49.6 312.4,49.5 315.8,49.5 319.2,49.5 322.6,49.5 326.0,49.5" fill="none" stroke="#c2410c" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="54.0,190.0 57.4,187.9 60.8,185.9 64.2,184.0 67.6,182.1 71.0,180.2 74.4,178.4 77.8,176.7 81.2,175.0 84.6,173.4 88.0,171.8 91.4,170.2 94.8,168.8 98.2,167.3 101.6,165.9 105.0,164.5 108.4,163.2 111.8,161.9 115.2,160.7 118.6,159.5 122.0,158.3 125.4,157.1 128.8,156.0 132.2,155.0 135.6,153.9 139.0,152.9 142.4,151.9 145.8,151.0 149.2,150.1 152.6,149.2 156.0,148.3 159.4,147.4 162.8,146.6 166.2,145.8 169.6,145.1 173.0,144.3 176.4,143.6 179.8,142.9 183.2,142.2 186.6,141.5 190.0,140.9 193.4,140.3 196.8,139.7 200.2,139.1 203.6,138.5 207.0,137.9 210.4,137.4 213.8,136.9 217.2,136.4 220.6,135.9 224.0,135.4 227.4,134.9 230.8,134.5 234.2,134.0 237.6,133.6 241.0,133.2 244.4,132.8 247.8,132.4 251.2,132.1 254.6,131.7 258.0,131.3 261.4,131.0 264.8,130.7 268.2,130.3 271.6,130.0 275.0,129.7 278.4,129.4 281.8,129.1 285.2,128.9 288.6,128.6 292.0,128.3 295.4,128.1 298.8,127.8 302.2,127.6 305.6,127.3 309.0,127.1 312.4,126.9 315.8,126.7 319.2,126.5 322.6,126.3 326.0,126.1" fill="none" stroke="#7e22ce" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="54.0,190.0 57.4,182.9 60.8,176.4 64.2,170.7 67.6,165.5 71.0,160.8 74.4,156.7 77.8,152.9 81.2,149.5 84.6,146.5 88.0,143.8 91.4,141.3 94.8,139.1 98.2,137.2 101.6,135.4 105.0,133.8 108.4,132.4 111.8,131.1 115.2,129.9 118.6,128.9 122.0,128.0 125.4,127.1 128.8,126.4 132.2,125.7 135.6,125.1 139.0,124.5 142.4,124.0 145.8,123.6 149.2,123.2 152.6,122.9 156.0,122.5 159.4,122.3 162.8,122.0 166.2,121.8 169.6,121.6 173.0,121.4 176.4,121.2 179.8,121.0 183.2,120.9 186.6,120.8 190.0,120.7 193.4,120.6 196.8,120.5 200.2,120.4 203.6,120.3 207.0,120.3 210.4,120.2 213.8,120.2 217.2,120.1 220.6,120.1 224.0,120.0 227.4,120.0 230.8,120.0 234.2,120.0 237.6,119.9 241.0,119.9 244.4,119.9 247.8,119.9 251.2,119.9 254.6,119.8 258.0,119.8 261.4,119.8 264.8,119.8 268.2,119.8 271.6,119.8 275.0,119.8 278.4,119.8 281.8,119.8 285.2,119.8 288.6,119.8 292.0,119.8 295.4,119.7 298.8,119.7 302.2,119.7 305.6,119.7 309.0,119.7 312.4,119.7 315.8,119.7 319.2,119.7 322.6,119.7 326.0,119.7" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="54.0" y1="190.0" x2="96.3" y2="26.0" stroke="#b91c1c" stroke-width="1.6" stroke-dasharray="5 3"/><circle cx="90.3" cy="49.4" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1"/><text x="95.3" y="63.4" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(8 ; 24)</text><text x="153.7" y="52.4" text-anchor="middle" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(b)</text><text x="280.7" y="77.0" text-anchor="middle" font-size="12" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(a)</text><text x="190.0" y="113.7" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(d)</text><text x="280.7" y="145.2" text-anchor="middle" font-size="12" font-weight="700" fill="#7e22ce" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(c)</text></svg>
:::

Les paliers à 24 et à 12 mmol·L⁻¹ se lisent sur l'axe vertical, et la pente de la tangente en O est la vitesse volumique à t = 0.

::: exemple Attribuer les courbes (a) à (d)

1. Tableau en avancement volumique pour E2 : S₂O₈²⁻ : 24 − y_f ; I⁻ : 80 − 2y_f. Si S₂O₈²⁻ est limitant, y_f = 24 et il reste 80 − 48 = 32 mmol·L⁻¹ de I⁻ : c'est cohérent, donc [I₂]_f = 24 mmol·L⁻¹. De même [I₂]_f = 24 pour E4 et 12 pour E1 et E3 (40 − 24 = 16 ≥ 0).
2. Deux courbes, (a) et (b), tendent vers 24 mmol·L⁻¹ : ce sont E2 et E4. Deux courbes, (c) et (d), tendent vers 12 : ce sont E1 et E3.
3. À palier égal, les deux expériences d'un groupe ont les mêmes concentrations et ne diffèrent que par la température, donc la courbe la plus raide au départ est la plus chaude : (b) est plus raide que (a), donc (b) = E4 et (a) = E2 ; (d) est plus raide que (c), donc (d) = E3 et (c) = E1.
4. Vitesse initiale de (b) : la tangente en O passe par (0 ; 0) et (8 ; 24), de pente 24/8 = 3,0 mmol·L⁻¹·min⁻¹, soit v_vol(0) = 3,0·10⁻³ mol·L⁻¹·min⁻¹.

:::

::: piege
**Erreur : juger la vitesse sur la hauteur du palier.** La courbe (d) s'arrête à 12 mmol·L⁻¹, deux fois plus bas que (a) à 24 mmol·L⁻¹ ; pourtant à t = 5 min, (d) est à environ 6,1 mmol·L⁻¹ et (a) à environ 5,3 : (d) monte plus vite. L'erreur tente parce qu'une courbe haute paraît « plus avancée ». Le palier dit combien de produit se forme (réactif limitant), la pente dit à quelle vitesse.
:::

::: methode
**Attribuer des courbes d'avancement à des expériences** — (1) Pour chaque expérience, on construit le tableau en avancement volumique, on identifie le réactif limitant et on en déduit le palier y_f. (2) On regroupe les courbes de même palier. (3) Dans un groupe, le réactif limitant est le même et seule change une condition qui joue sur la vitesse sans changer le palier (température, catalyseur, concentration d'un réactif en excès) : la courbe la plus raide au départ est la plus favorisée. (4) La vitesse volumique initiale est la pente de la tangente en t = 0, lue sur deux points de cette tangente.
Cas limite : si deux expériences diffèrent par la température et par la concentration à la fois, la pente seule ne dit pas laquelle est la plus rapide sans mesure.
:::

::: verifie À toi : prévoir deux paliers
À même température, l'expérience P a pour [S₂O₈²⁻]₀ = 18 mmol·L⁻¹ et l'expérience Q pour [S₂O₈²⁻]₀ = 9 mmol·L⁻¹, avec [I⁻]₀ = 60 mmol·L⁻¹ dans les deux. Quel palier chaque courbe [I₂](t) atteint-elle, et laquelle est la plus raide au départ ?

---

Dans P, I⁻ permettrait y = 60/2 = 30 mmol·L⁻¹, plus que 18 : S₂O₈²⁻ est limitant, palier 18 mmol·L⁻¹ ; dans Q, 30 est supérieur à 9, palier 9 mmol·L⁻¹. P est la plus concentrée en S₂O₈²⁻ avec [I⁻]₀ identique, donc sa courbe est la plus raide au départ.
:::

::: retenir
Le palier d'une courbe [I₂](t) donne le réactif limitant, la pente de la tangente en t = 0 donne la vitesse initiale, et à palier égal la courbe la plus raide est celle des conditions les plus favorables.
:::

> 🏆 Tu tiens maintenant les trois leviers de la vitesse : concentration, température, catalyseur. Le chapitre suivant ouvre l'équilibre chimique.
