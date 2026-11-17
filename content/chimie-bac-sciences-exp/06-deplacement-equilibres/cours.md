# 🎚️ Déplacement des équilibres — quand le système répond à la perturbation

> 💡 «Un système en équilibre ne se laisse pas pousser sans réagir : il réplique, mais il ne revient jamais tout à fait à son état de départ.»

Une brosse à dents pour enfant change de couleur selon la température de l'eau qui la mouille : un système chimique y est déplacé par la chaleur, et l'on voudrait savoir dans quel sens, sans refaire l'expérience. Huit notions donnent la réponse : l'effet de la pression, celui de la concentration, celui de la température, l'énoncé de la loi de modération avec ses limites, les conditions d'évolution (Π et K) quand la loi se tait, la lecture d'une température sur K ou sur τ_f, le calcul du nouvel équilibre et le compromis industriel. On suppose acquis le tableau d'avancement (chapitre 1), l'équilibre dynamique et τ_f (chapitre 4), la fonction des concentrations Π et la constante K (chapitre 5), et la distinction entre réaction exothermique et réaction endothermique.

## 🗜️ La pression : comprimer un système gazeux fermé

Une seringue bouchée contient un mélange gazeux de dioxyde d'azote NO₂, brun-orangé, et de tétraoxyde de diazote N₂O₄, incolore, à l'équilibre 2 NO₂(g) ⇄ N₂O₄(g) (1), à température ambiante. On enfonce brusquement le piston et on le maintient : la teinte devient aussitôt plus foncée, puis s'éclaircit en quelques secondes, sans retrouver sa teinte de départ.
Pourquoi ces deux temps, et dans quel sens l'équilibre se déplace-t-il ?

::: definition
**Quantité de matière gazeuse n_g** — C'est la somme des quantités de matière des seuls constituants gazeux. À température et volume fixés, l'équation d'état des gaz parfaits PV = n_g·R·T montre que la pression P est proportionnelle à n_g : une réaction qui fait diminuer n_g fait diminuer P.
:::

::: figure Allure schématique (sans échelle) de [NO₂], dont dépend l'intensité de la teinte brune : saut immédiat à la compression en t₁, puis baisse partielle jusqu'à c₂, qui reste supérieure à c₁
<svg viewBox="0 0 340 236"><title>Concentration en NO₂ après une compression : saut puis baisse partielle</title><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="330" y="206" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t</text><text x="60" y="12" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">[NO₂]</text><line x1="54" y1="130" x2="326" y2="130" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5 4"/><line x1="54" y1="96" x2="326" y2="96" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5 4"/><line x1="120" y1="190" x2="120" y2="30" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 4"/><polyline points="54,130 120,130 120,60 126,64.5 132,68.4 138,71.9 144,74.9 150,77.5 156,79.8 162,81.8 168,83.6 174,85.2 180,86.5 186,87.7 192,88.7 198,89.6 204,90.4 210,91.1 216,91.7 222,92.3 228,92.7 234,93.1 240,93.5 246,93.8 252,94.1 258,94.3 264,94.5 270,94.7 276,94.9 282,95 288,95.1 294,95.2 300,95.3 306,95.4 312,95.5 318,95.6 324,95.6" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round"/><text x="48" y="134" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">c₁</text><text x="48" y="100" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">c₂</text><text x="120" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t₁</text><text x="126" y="44" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">compression</text></svg>
:::

::: exemple Interpréter la compression, puis prévoir la détente

1. À la compression, le volume diminue sans qu'aucune réaction n'ait eu le temps de se produire : les quantités de matière sont inchangées, donc [NO₂] = n(NO₂)/V augmente aussitôt, et la teinte, qui croît avec [NO₂], s'intensifie. C'est le saut de la courbe en t₁.
2. Dans l'équation (1), les constituants gazeux comptent 2 mol à gauche et 1 mol à droite : la réaction directe diminue n_g.
3. À T et V constants, PV = n_g·R·T : si n_g diminue, P diminue. La réaction directe s'oppose donc à la hausse de pression : c'est elle qui se produit.
4. Elle consomme NO₂ : [NO₂] baisse après le saut et la teinte s'éclaircit, jusqu'au nouveau palier c₂. Ce palier reste au-dessus de c₁ : la réaction atténue la hausse de pression sans l'annuler.
5. Pour une détente, la pression tend à diminuer : c'est la réaction qui augmente n_g, soit N₂O₄ → 2 NO₂, qui se produit. La teinte pâlit d'abord par dilution immédiate, puis fonce un peu.

:::

::: piege
**Erreur : lire la teinte juste après la compression comme la réponse de l'équilibre.** On voit le mélange foncer et l'on conclut que N₂O₄ s'est transformé en NO₂, donc que l'équilibre s'est déplacé dans le sens inverse. L'erreur tente parce qu'une teinte plus foncée évoque « plus de NO₂ » ; mais ce saut vient seulement du volume réduit, qui concentre les mêmes molécules. La réponse du système se lit après le saut : la teinte s'éclaircit, donc NO₂ est consommé.
:::

::: propriete
**Effet d'une variation de pression** — À température constante, dans un système fermé initialement en équilibre, une hausse de pression fait se produire la réaction qui diminue n_g, et une baisse de pression celle qui augmente n_g. Dans les deux cas, la réponse modère la variation de pression causée par la perturbation.
Cas : 3 H₂(g) + N₂(g) ⇄ 2 NH₃(g) compte 4 mol de gaz à gauche et 2 à droite, donc une hausse de pression favorise la réaction directe ; CO(g) + H₂O(g) ⇄ CO₂(g) + H₂(g) en compte 2 de chaque côté, donc la pression ne déplace pas l'équilibre.
Cas limite : seuls les constituants gazeux comptent. Dans CaCO₃(s) ⇄ CaO(s) + CO₂(g), il y a 0 mol de gaz à gauche et 1 mol à droite : une hausse de pression favorise la réaction inverse.
:::

::: verifie À toi : un autre équilibre gazeux
À température constante, on comprime le système fermé 2 CO(g) + O₂(g) ⇄ 2 CO₂(g) à l'équilibre. Dans quel sens se déplace l'équilibre ?

---

Les constituants gazeux comptent 3 mol à gauche (2 + 1) et 2 mol à droite. Une hausse de pression fait se produire la réaction qui diminue n_g : c'est la réaction directe, 2 CO + O₂ → 2 CO₂.
:::

::: retenir
À T constante dans un système fermé, une hausse de pression déplace l'équilibre dans le sens qui diminue n_g, une baisse dans le sens qui l'augmente ; si n_g est le même des deux côtés, aucun déplacement.
:::

## 💧 La concentration : ajouter ou retirer une espèce

Dans un tube, les ions fer (III) Fe³⁺ et thiocyanate SCN⁻ forment l'ion thiocyanatofer (III) FeSCN²⁺, rouge sang : Fe³⁺ + SCN⁻ ⇄ FeSCN²⁺ (2). La teinte ne change plus avec le temps : le système est en équilibre. On ajoute quelques gouttes d'une solution concentrée de thiocyanate de potassium, et le rouge s'intensifie.
Que devient le thiocyanate ajouté, et que se passerait-il si l'on faisait disparaître des ions Fe³⁺ ?

::: definition
**Réaction annexe** — C'est une seconde réaction, provoquée volontairement, qui consomme une espèce de l'équilibre et fait ainsi diminuer sa concentration : précipitation, neutralisation, complexation ou oxydoréduction. Quelques gouttes d'une solution concentrée ajoutent une espèce sans changer sensiblement le volume.
:::

::: figure Allure schématique (sans échelle) : après l'ajout en t₁, [SCN⁻] saute puis redescend jusqu'à c₂, sans retrouver c₁ ; [FeSCN²⁺] monte de d₁ à un nouveau palier d₂
<svg viewBox="0 0 340 236"><title>Concentrations en SCN⁻ et FeSCN²⁺ après un ajout de SCN⁻</title><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="330" y="206" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t</text><text x="60" y="12" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">concentrations</text><line x1="54" y1="130" x2="326" y2="130" stroke="#2563eb" stroke-width="1.1" stroke-dasharray="5 4"/><line x1="54" y1="106" x2="326" y2="106" stroke="#2563eb" stroke-width="1.1" stroke-dasharray="5 4"/><line x1="54" y1="176" x2="326" y2="176" stroke="#dc2626" stroke-width="1.1" stroke-dasharray="5 4"/><line x1="54" y1="150" x2="326" y2="150" stroke="#dc2626" stroke-width="1.1" stroke-dasharray="5 4"/><line x1="110" y1="190" x2="110" y2="30" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 4"/><polyline points="54,130 110,130 110,56 116,61.7 122,66.7 128,71.1 134,75.1 140,78.6 146,81.7 152,84.4 158,86.9 164,89 170,90.9 176,92.6 182,94.2 188,95.5 194,96.7 200,97.7 206,98.7 212,99.5 218,100.2 224,100.9 230,101.5 236,102 242,102.4 248,102.8 254,103.2 260,103.5 266,103.8 272,104 278,104.3 284,104.5 290,104.6 296,104.8 302,104.9 308,105 314,105.2 320,105.3 326,105.3" fill="none" stroke="#2563eb" stroke-width="2.5" stroke-linejoin="round"/><polyline points="54,176 110,176 116,173.3 122,170.9 128,168.7 134,166.8 140,165.1 146,163.5 152,162.1 158,160.9 164,159.7 170,158.7 176,157.8 182,157 188,156.3 194,155.6 200,155.1 206,154.5 212,154.1 218,153.6 224,153.3 230,152.9 236,152.6 242,152.4 248,152.1 254,151.9 260,151.7 266,151.5 272,151.4 278,151.2 284,151.1 290,151 296,150.9 302,150.8 308,150.7 314,150.6 320,150.6 326,150.5" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-linejoin="round"/><text x="48" y="134" text-anchor="end" font-size="11" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">c₁</text><text x="48" y="110" text-anchor="end" font-size="11" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">c₂</text><text x="48" y="180" text-anchor="end" font-size="11" font-weight="700" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">d₁</text><text x="48" y="154" text-anchor="end" font-size="11" font-weight="700" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">d₂</text><text x="110" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t₁</text><text x="118" y="44" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ajout de SCN⁻</text><text x="318" y="98" text-anchor="end" font-size="11" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">[SCN⁻]</text><text x="318" y="142" text-anchor="end" font-size="11" font-weight="700" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">[FeSCN²⁺]</text></svg>
:::

::: exemple Prévoir le déplacement pour deux perturbations

1. Dans l'équation (2), la réaction directe consomme Fe³⁺ et SCN⁻ et forme FeSCN²⁺ ; la réaction inverse fait l'inverse.
2. On ajoute SCN⁻ : [SCN⁻] augmente, c'est la seule concentration nettement modifiée, donc la loi s'applique. La réponse est la réaction qui diminue [SCN⁻] : la réaction directe.
3. Elle forme FeSCN²⁺, d'où le rouge plus intense. Sur la figure, [SCN⁻] ne retombe qu'à c₂, au-dessus de c₁ : le thiocyanate ajouté n'est consommé qu'en partie.
4. On ajoute maintenant quelques gouttes de soude : les ions HO⁻ précipitent des ions Fe³⁺ sous forme de Fe(OH)₃, réaction annexe qui fait diminuer [Fe³⁺].
5. La réponse est la réaction qui augmente [Fe³⁺] : la réaction inverse, FeSCN²⁺ → Fe³⁺ + SCN⁻. La teinte rouge pâlit.

:::

::: piege
**Erreur : croire que le système annule la perturbation.** On dit que, après l'ajout de SCN⁻, [SCN⁻] retrouve sa valeur initiale c₁. L'erreur tente parce que « modérer » ressemble à « compenser » ; mais la réponse atténue seulement la variation. Sur la figure, [SCN⁻] se stabilise à c₂, strictement supérieure à c₁, tandis que [FeSCN²⁺] a bien augmenté.
:::

::: propriete
**Effet d'une variation de concentration** — À température constante, si une perturbation augmente la concentration d'une espèce d'un système en équilibre, la réaction qui diminue cette concentration se produit ; si elle la diminue, la réaction qui l'augmente se produit. Ajouter un réactif ou retirer un produit favorise donc la réaction directe ; ajouter un produit ou retirer un réactif favorise la réaction inverse.
Cas limite : la loi ne vaut que si la perturbation ne modifie nettement qu'une seule concentration. Verser un grand volume d'eau dilue toutes les espèces dissoutes à la fois : elle ne s'applique plus (notion 5).
:::

::: verifie À toi : un autre équilibre en solution
La solution rose Co(H₂O)₆²⁺ + 4 Cl⁻ ⇄ CoCl₄²⁻ + 6 H₂O contient aussi l'ion CoCl₄²⁻, bleu. On ajoute quelques gouttes d'acide chlorhydrique concentré, qui apporte des ions Cl⁻. Dans quel sens se déplace l'équilibre, et que devient la teinte ?

---

[Cl⁻] augmente : la réaction qui diminue [Cl⁻] se produit, c'est la réaction directe, qui consomme Cl⁻ et forme CoCl₄²⁻. La solution bleuit.
:::

::: retenir
À T constante, une espèce ajoutée est consommée par la réaction qui la consomme, une espèce retirée est reformée par la réaction qui la forme ; la réponse atténue la variation sans l'annuler.
:::

## 🌡️ La température : chauffer ou refroidir à pression constante

Un ballon fermé contient le mélange de l'équilibre (1), 2 NO₂ ⇄ N₂O₄, sous pression atmosphérique constante, d'un brun pâle à froid. On le plonge dans un bain-marie chaud : la teinte brune se renforce ; dans de la glace, elle pâlit.
Pourquoi la température seule déplace-t-elle l'équilibre, et dans quel sens ?

::: definition
**Réaction exothermique, réaction endothermique** — Une transformation exothermique tend à élever la température du système où elle se produit ; une transformation endothermique tend à l'abaisser. Quand une réaction est exothermique, la réaction inverse est endothermique, et réciproquement.
:::

::: figure L'équilibre (1) : la réaction directe (+1) est exothermique, donc la réaction inverse (−1) est endothermique ; chauffer fait se produire (−1), refroidir fait se produire (+1)
<svg viewBox="0 0 340 206"><title>Équilibre 2 NO₂ ⇄ N₂O₄ : la réaction exothermique et la réaction endothermique</title><rect x="14" y="62" width="96" height="60" rx="8" fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="1.6"/><rect x="230" y="62" width="96" height="60" rx="8" fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="1.6"/><text x="62" y="88" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2 NO₂</text><text x="62" y="108" text-anchor="middle" font-size="11" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">brun</text><text x="278" y="88" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N₂O₄</text><text x="278" y="108" text-anchor="middle" font-size="11" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">incolore</text><line x1="122" y1="76" x2="218" y2="76" stroke="#0f6e56" stroke-width="2.5"/><polygon points="222,76 212,71 212,81" fill="#0f6e56"/><line x1="218" y1="108" x2="122" y2="108" stroke="#d97706" stroke-width="2.5"/><polygon points="118,108 128,103 128,113" fill="#d97706"/><text x="170" y="64" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(+1) exothermique</text><text x="170" y="128" text-anchor="middle" font-size="11" font-weight="700" fill="#d97706" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(−1) endothermique</text><text x="170" y="166" text-anchor="middle" font-size="11" font-weight="700" fill="#d97706" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">chauffer : la réaction (−1) se produit</text><text x="170" y="188" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">refroidir : la réaction (+1) se produit</text></svg>
:::

::: exemple Prévoir l'effet d'un bain chaud puis d'un bain de glace

1. La réaction directe (+1) est exothermique ; la réaction inverse (−1) est donc endothermique.
2. Le bain chaud tend à élever la température, à pression constante dans un système fermé : la réponse est la réaction qui tend à l'abaisser, la réaction endothermique (−1).
3. Elle transforme N₂O₄ en NO₂ : [NO₂] augmente et la teinte brune se renforce, comme on l'observe.
4. Le bain de glace tend à abaisser la température : la réponse est la réaction exothermique (+1). NO₂ est consommé et la teinte pâlit.

:::

::: piege
**Erreur : croire qu'une réaction endothermique élève la température.** On dit qu'on chauffe, donc que le système favorise la réaction qui dégage de la chaleur, l'exothermique. L'erreur tente parce que « chauffer » et « dégager de la chaleur » vont ensemble dans le langage courant ; mais le système répond en modérant la hausse, c'est-à-dire par la transformation qui abaisse la température : la réaction endothermique, qui absorbe de la chaleur.
:::

::: propriete
**Effet d'une variation de température** — À pression constante, dans un système fermé initialement en équilibre, une hausse de température fait se produire la réaction endothermique, et une baisse la réaction exothermique. Dans les deux cas, la réponse modère la variation de température.
Cas : pour la réaction directe exothermique de la synthèse de NH₃, une hausse de température favorise la réaction inverse ; pour la réaction directe endothermique Co(H₂O)₆²⁺ + 4 Cl⁻ ⇄ CoCl₄²⁻ + 6 H₂O, elle favorise la réaction directe.
Cas limite : l'estérification est athermique : la température n'est pas un facteur d'équilibre pour elle et ne modifie que la vitesse.
:::

::: verifie À toi : la synthèse de l'ammoniac
La réaction directe de N₂(g) + 3 H₂(g) ⇄ 2 NH₃(g) est exothermique. À pression constante, on chauffe le système fermé à l'équilibre. Dans quel sens se déplace l'équilibre ?

---

Une hausse de température fait se produire la réaction endothermique. La réaction directe est exothermique, donc l'inverse est endothermique : l'équilibre se déplace dans le sens inverse, NH₃ se décompose.
:::

::: retenir
À P constante dans un système fermé, chauffer fait se produire la réaction endothermique, refroidir la réaction exothermique ; la réaction inverse d'une exothermique est endothermique.
:::

## ⚖️ La loi de modération : énoncé et domaine de validité

Trois expériences ont donné la même réponse : la pression, la concentration et la température, une fois perturbées, ont chacune provoqué la réaction qui tend à diminuer la variation subie. Le vaporeformage du méthane, qui fabrique le dihydrogène industriel, CH₄(g) + H₂O(g) ⇄ CO(g) + 3 H₂(g) (3), endothermique dans le sens direct, offre plusieurs perturbations à prévoir d'un coup.
Une seule règle suffit-elle, et jusqu'où va-t-elle ?

::: definition
**Loi de modération** — Si, dans un système initialement en équilibre chimique, une perturbation fait varier la température (à pression constante, système fermé), la pression (à température constante, système fermé) ou la concentration d'une entité chimique (à température constante), le système subit en réponse la réaction qui tend à modérer cette variation. La température, la pression et les concentrations sont des facteurs d'équilibre.
:::

| Perturbation                                   | Réaction qui se produit en réponse       |
| ---------------------------------------------- | ---------------------------------------- |
| hausse de pression (T constante, fermé)        | celle qui diminue n_g                    |
| baisse de pression (T constante, fermé)        | celle qui augmente n_g                   |
| hausse de température (P constante, fermé)     | la réaction endothermique                |
| baisse de température (P constante, fermé)     | la réaction exothermique                 |
| ajout d'une espèce (T constante)               | celle qui consomme cette espèce          |
| retrait d'une espèce (T constante)             | celle qui forme cette espèce             |

::: exemple Appliquer la loi à l'équilibre (3)

1. Hausse de température à pression constante : la réponse est la réaction endothermique, c'est-à-dire la réaction directe. Il se forme plus de CO et de H₂.
2. Hausse de pression à température constante : les constituants gazeux comptent 2 mol à gauche et 4 mol à droite, donc la réaction qui diminue n_g est la réaction inverse.
3. Ajout de vapeur d'eau à température et volume constants : la réponse est la réaction qui consomme H₂O, la réaction directe.
4. Retrait d'une partie du dihydrogène : la réponse est la réaction qui forme H₂, la réaction directe.
5. Ajout d'un catalyseur : aucun déplacement. Il accélère les deux réactions de la même façon et l'équilibre est atteint plus vite, avec la même composition : c'est un facteur cinétique, pas un facteur d'équilibre.

:::

::: piege
**Erreur : appliquer la loi à une dilution.** On ajoute de l'eau à la solution rouge de FeSCN²⁺ et l'on raisonne : « les concentrations ont baissé, le système va produire ce qui a baissé ». L'erreur tente parce qu'une dilution ressemble à une baisse de concentration ; mais toutes les espèces dissoutes baissent à la fois, donc il n'existe aucune réaction qui rétablisse « la » concentration : la loi ne désigne aucun sens. Il faut alors comparer Π et K (notion 5).
:::

::: propriete
**Domaine de validité** — La loi s'applique à un système initialement en équilibre, quand un seul facteur varie : la pression et la température pour un système fermé, une concentration seulement si l'effet immédiat de la perturbation ne modifie nettement qu'une concentration. Elle ne concerne pas les variations de volume ou de quantité de matière dues à un ajout de solvant, comme une dilution, ni un système hors équilibre. Un catalyseur ne déplace pas l'équilibre.
Cas limite : si la pression et la température varient en même temps, les deux réponses peuvent s'opposer et la loi ne tranche pas.
:::

::: verifie À toi : deux facteurs à la fois
Pour 2 NO₂ ⇄ N₂O₄, de réaction directe exothermique, on comprime le système fermé et on le chauffe en même temps. La loi de modération permet-elle de prévoir le sens de déplacement ?

---

Non. La compression favorise la réaction directe, qui diminue n_g, tandis que le chauffage favorise la réaction inverse, endothermique : les deux réponses s'opposent. La loi ne vaut que si un seul facteur varie.
:::

::: retenir
Pour un seul facteur perturbé (P ou T d'un système fermé, une concentration), le système fermé en équilibre répond par la réaction qui modère la variation ; ni dilution, ni catalyseur, ni deux facteurs à la fois.
:::

## 📐 Les conditions d'évolution : Π et K quand la loi se tait

À l'équilibre (2), Fe³⁺ + SCN⁻ ⇄ FeSCN²⁺, une solution contient [Fe³⁺] = [SCN⁻] = 4,0·10⁻³ mol·L⁻¹ et [FeSCN²⁺] = 1,6·10⁻³ mol·L⁻¹. On y ajoute le triple de son volume en eau distillée. La loi de modération est muette sur ce cas.
Le système évolue-t-il encore, et dans quel sens ?

::: definition
**Fonction des concentrations Π et constante K (rappel du chapitre 5)** — Pour une équation a A + b B ⇄ c C + d D, la fonction des concentrations est Π = [C]ᶜ·[D]ᵈ / ([A]ᵃ·[B]ᵇ), calculé avec les concentrations du moment, en mol·L⁻¹ et sans le solvant ; pour un gaz, la concentration est n/V. À l'équilibre, Π prend la valeur K, constante qui ne dépend que de la température. Π et K s'écrivent sans unité.
:::

Les concentrations avant et juste après la dilution, avant toute évolution :

|                        | [Fe³⁺] (mol·L⁻¹) | [SCN⁻] (mol·L⁻¹) | [FeSCN²⁺] (mol·L⁻¹) |
| ---------------------- | ---------------- | ---------------- | ------------------- |
| avant l'ajout d'eau    | 4,0·10⁻³         | 4,0·10⁻³         | 1,6·10⁻³            |
| juste après l'ajout    | 1,0·10⁻³         | 1,0·10⁻³         | 4,0·10⁻⁴            |

::: exemple Prévoir l'effet de la dilution par les conditions d'évolution

1. Avant l'ajout, le système est en équilibre, donc Π = K : Π = 1,6·10⁻³ / (4,0·10⁻³ × 4,0·10⁻³) = 1,6·10⁻³ / 1,6·10⁻⁵ = 1,0·10² = K.
2. Le volume est multiplié par 4 : chaque concentration est divisée par 4, ce qui donne les valeurs de la dernière ligne du tableau.
3. Juste après l'ajout, Π′ = 4,0·10⁻⁴ / (1,0·10⁻³ × 1,0·10⁻³) = 4,0·10⁻⁴ / 1,0·10⁻⁶ = 4,0·10² = 4 K.
4. K ne dépend que de la température, qui n'a pas changé : K vaut toujours 1,0·10². Comme Π′ > K, le système évolue dans le sens inverse, FeSCN²⁺ → Fe³⁺ + SCN⁻, jusqu'à ce que Π retombe à K.
5. La solution rouge pâlit donc plus que la seule dilution ne l'explique.

:::

::: piege
**Erreur : croire que Π baisse puisque toutes les concentrations baissent.** On conclut que Π < K et que le système évolue dans le sens direct. L'erreur tente parce que chaque concentration est divisée par 4 ; mais Π est un quotient : le numérateur est divisé par 4, le dénominateur par 4 × 4 = 16, et le quotient est donc multiplié par 4.
:::

::: propriete
**Conditions d'évolution** — À température constante, K est constante. Si Π < K, le système évolue dans le sens direct ; si Π > K, dans le sens inverse ; si Π = K, il est en équilibre et n'évolue pas.
Cas : en ajoutant SCN⁻, on augmente le dénominateur de Π, donc Π < K et le système évolue dans le sens direct, comme la loi de modération le prévoit ; en divisant par 2 le volume d'un mélange 2 NO₂ ⇄ N₂O₄, Π = [N₂O₄]/[NO₂]² est divisé par 2, donc Π < K : sens direct, comme pour la pression.
Cas limite : pour l'équilibre (2), diluer en multipliant le volume par n multiplie Π par n, quel que soit n > 1 : une dilution déplace toujours cet équilibre dans le sens inverse.
:::

::: verifie À toi : diluer une solution de cobalt
Pour Co(H₂O)₆²⁺ + 4 Cl⁻ ⇄ CoCl₄²⁻ + 6 H₂O, on dilue par 2 la solution à l'équilibre. Écrire Π (l'eau est le solvant), dire par quel facteur il est multiplié, puis donner le sens d'évolution.

---

Π = [CoCl₄²⁻] / ([Co(H₂O)₆²⁺]·[Cl⁻]⁴). Le numérateur est divisé par 2, le dénominateur par 2 × 2⁴ = 32 : Π est multiplié par 32/2 = 16. Donc Π > K et le système évolue dans le sens inverse, vers Co(H₂O)₆²⁺ : la solution vire au rose.
:::

::: retenir
Π < K : sens direct ; Π > K : sens inverse ; K ne dépend que de T, et une dilution se traite par Π, non par la loi de modération.
:::

## 📉 Lire l'effet de la température sur K ou sur τ_f

On a mesuré le taux d'avancement final τ_f de la décomposition d'un gaz, à pression constante, pour plusieurs températures. Les points sont des valeurs d'illustration, pas des mesures réelles.
Peut-on dire, sans calorimètre, si cette décomposition est exothermique ou endothermique ?

::: figure Taux d'avancement final en fonction de la température : τ_f croît de 0,12 à 400 °C jusqu'à 0,55 à 600 °C (valeurs d'illustration)
<svg viewBox="0 0 340 236"><title>Taux d'avancement final en fonction de la température</title><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="330" y="222" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">θ (°C)</text><text x="60" y="12" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τ<tspan dy="3" font-size="8">f</tspan></text><line x1="81.2" y1="26" x2="81.2" y2="190" stroke="#e2e8f0" stroke-width="1"/><text x="81.2" y="204" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">300</text><line x1="135.6" y1="26" x2="135.6" y2="190" stroke="#e2e8f0" stroke-width="1"/><text x="135.6" y="204" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">400</text><line x1="190" y1="26" x2="190" y2="190" stroke="#e2e8f0" stroke-width="1"/><text x="190" y="204" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">500</text><line x1="244.4" y1="26" x2="244.4" y2="190" stroke="#e2e8f0" stroke-width="1"/><text x="244.4" y="204" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">600</text><line x1="298.8" y1="26" x2="298.8" y2="190" stroke="#e2e8f0" stroke-width="1"/><text x="298.8" y="204" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">700</text><line x1="54" y1="157.2" x2="326" y2="157.2" stroke="#e2e8f0" stroke-width="1"/><text x="48" y="161.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,2</text><line x1="54" y1="124.4" x2="326" y2="124.4" stroke="#e2e8f0" stroke-width="1"/><text x="48" y="128.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,4</text><line x1="54" y1="91.6" x2="326" y2="91.6" stroke="#e2e8f0" stroke-width="1"/><text x="48" y="95.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,6</text><line x1="54" y1="58.8" x2="326" y2="58.8" stroke="#e2e8f0" stroke-width="1"/><text x="48" y="62.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,8</text><line x1="54" y1="26" x2="326" y2="26" stroke="#e2e8f0" stroke-width="1"/><text x="48" y="30" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,0</text><polyline points="81.2,183.4 135.6,170.3 190,140.8 244.4,99.8 298.8,62.1" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round"/><circle cx="81.2" cy="183.4" r="3.5" fill="#0f6e56"/><circle cx="135.6" cy="170.3" r="3.5" fill="#0f6e56"/><circle cx="190" cy="140.8" r="3.5" fill="#0f6e56"/><circle cx="244.4" cy="99.8" r="3.5" fill="#0f6e56"/><circle cx="298.8" cy="62.1" r="3.5" fill="#0f6e56"/></svg>
:::

::: exemple Déduire le caractère énergétique d'une réaction

1. Sur la courbe, τ_f passe de 0,12 à 400 °C à 0,55 à 600 °C : la décomposition est plus avancée à chaud, donc la hausse de température favorise la réaction directe.
2. Une hausse de température fait se produire la réaction endothermique : la décomposition est donc endothermique, et la réaction inverse, la formation, exothermique.
3. Même raisonnement avec K. Pour H₂(g) + I₂(g) ⇄ 2 HI(g), on lit K = 67 à 350 °C et K = 50 à 450 °C (valeurs arrondies) : K diminue quand T augmente.
4. La hausse de température défavorise donc la réaction directe : celle-ci n'est pas la réaction endothermique, elle est exothermique.

:::

::: piege
**Erreur : juger le caractère énergétique sur la valeur de τ_f plutôt que sur sa variation.** On voit τ_f = 0,78, proche de 1, et l'on conclut que la réaction est très exothermique. L'erreur tente parce qu'une réaction très avancée « dégage beaucoup » dans l'imagination ; mais τ_f mesure l'avancement, pas l'énergie échangée. Seule la variation de τ_f ou de K avec la température renseigne, et son sens.
:::

::: propriete
**Lire τ_f ou K en fonction de T** — À pression constante, si τ_f ou K de la réaction directe augmente avec la température, la réaction directe est endothermique ; s'il diminue, elle est exothermique.
Cas : si l'on sait la réaction directe endothermique, une baisse de τ_f d'un état à l'autre indique que la température a baissé.
Cas limite : pour une solution, dont le volume reste pratiquement inchangé, juste après un changement de température la composition et les concentrations n'ont pas encore bougé, donc Π garde sa valeur alors que K a changé. Pour une réaction directe exothermique que l'on chauffe, K diminue et Π > K : le système évolue dans le sens inverse.
:::

::: verifie À toi : un autre gaz
Pour A(g) ⇄ B(g) + C(g), à pression constante, τ_f = 0,20 à 300 K et τ_f = 0,35 à 350 K. La réaction directe est-elle exothermique ou endothermique ?

---

τ_f augmente avec la température : la hausse de température favorise la réaction directe. Elle fait se produire la réaction endothermique, donc la réaction directe est endothermique.
:::

::: retenir
Si τ_f ou K de la réaction directe croît avec T, elle est endothermique ; s'il décroît, elle est exothermique.
:::

## 🧮 Calculer la composition du nouvel équilibre

Dans un récipient fermé de volume constant V = 2,00 L, à température constante, l'équilibre COCl₂(g) ⇄ CO(g) + Cl₂(g) (4) contient 0,16 mol de COCl₂, 0,20 mol de CO et 0,20 mol de Cl₂. On ajoute 0,20 mol de CO ; au nouvel équilibre, la quantité totale de gaz mesurée vaut 0,71 mol.
Dans quel sens le système évolue-t-il, et quelle est la composition du nouvel équilibre ?

::: definition
**Nouvel état initial** — C'est la composition juste après la perturbation, avant toute évolution : l'ancien équilibre, modifié par la perturbation. C'est la première ligne du tableau d'avancement qui décrit le retour à l'équilibre.
:::

::: figure Quantités de matière avant et après l'ajout de CO en t₁ : n(CO) saute de 0,20 mol à 0,40 mol puis redescend à 0,35 mol, tandis que n(COCl₂) monte de 0,16 mol à 0,21 mol et n(Cl₂) baisse de 0,20 mol à 0,15 mol
<svg viewBox="0 0 340 236"><title>Quantités de CO, COCl₂ et Cl₂ avant et après l'ajout de CO</title><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="330" y="206" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t</text><text x="60" y="12" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">n (mol)</text><line x1="54" y1="157.2" x2="326" y2="157.2" stroke="#e2e8f0" stroke-width="1"/><text x="48" y="161.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,1</text><line x1="54" y1="124.4" x2="326" y2="124.4" stroke="#e2e8f0" stroke-width="1"/><text x="48" y="128.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,2</text><line x1="54" y1="91.6" x2="326" y2="91.6" stroke="#e2e8f0" stroke-width="1"/><text x="48" y="95.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,3</text><line x1="54" y1="58.8" x2="326" y2="58.8" stroke="#e2e8f0" stroke-width="1"/><text x="48" y="62.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,4</text><line x1="54" y1="26" x2="326" y2="26" stroke="#e2e8f0" stroke-width="1"/><text x="48" y="30" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,5</text><line x1="120" y1="190" x2="120" y2="26" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 4"/><text x="120" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t₁</text><polyline points="54,124.4 120,124.4 120,58.8 126,60.8 132,62.6 138,64.2 144,65.6 150,66.8 156,67.8 162,68.8 168,69.6 174,70.3 180,70.9 186,71.4 192,71.9 198,72.3 204,72.7 210,73 216,73.3 222,73.5 228,73.7 234,73.9 240,74.1 246,74.2 252,74.3 258,74.4 264,74.5 270,74.6 276,74.7 282,74.8 288,74.8 294,74.9 300,74.9 306,74.9 312,75 318,75 324,75" fill="none" stroke="#2563eb" stroke-width="2.5" stroke-linejoin="round"/><polyline points="54,124.4 120,124.4 126,126.4 132,128.2 138,129.8 144,131.2 150,132.4 156,133.4 162,134.4 168,135.2 174,135.9 180,136.5 186,137 192,137.5 198,137.9 204,138.3 210,138.6 216,138.9 222,139.1 228,139.3 234,139.5 240,139.7 246,139.8 252,139.9 258,140 264,140.1 270,140.2 276,140.3 282,140.4 288,140.4 294,140.5 300,140.5 306,140.5 312,140.6 318,140.6 324,140.6" fill="none" stroke="#d97706" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="7 4"/><polyline points="54,137.5 120,137.5 126,135.5 132,133.7 138,132.1 144,130.7 150,129.5 156,128.5 162,127.6 168,126.8 174,126.1 180,125.4 186,124.9 192,124.4 198,124 204,123.7 210,123.3 216,123.1 222,122.8 228,122.6 234,122.4 240,122.3 246,122.1 252,122 258,121.9 264,121.8 270,121.7 276,121.6 282,121.6 288,121.5 294,121.5 300,121.4 306,121.4 312,121.4 318,121.3 324,121.3" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round"/><text x="128" y="42.4" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ajout de CO</text><text x="320" y="68.2" text-anchor="end" font-size="11" font-weight="700" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">CO</text><text x="320" y="114.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">COCl₂</text><text x="320" y="155.8" text-anchor="end" font-size="11" font-weight="700" fill="#d97706" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Cl₂</text></svg>
:::

Tableau d'avancement de la réaction qui se produit, ici la réaction inverse CO + Cl₂ → COCl₂ :

|                               | COCl₂    | CO       | Cl₂      |
| ----------------------------- | -------- | -------- | -------- |
| juste après l'ajout (mol)     | 0,16     | 0,40     | 0,20     |
| nouvel équilibre (mol)        | 0,16 + x | 0,40 − x | 0,20 − x |

::: exemple Du nouvel état initial au nouvel équilibre

1. Juste après l'ajout : n(CO) = 0,20 + 0,20 = 0,40 mol. Concentrations (V = 2,00 L) : [COCl₂] = 0,080 mol·L⁻¹, [CO] = 0,20 mol·L⁻¹, [Cl₂] = 0,10 mol·L⁻¹.
2. K se calcule à l'ancien équilibre : [COCl₂] = 0,080, [CO] = [Cl₂] = 0,10, donc K = 0,10 × 0,10 / 0,080 = 0,125.
3. Π′ = 0,20 × 0,10 / 0,080 = 0,25 > K : le système évolue dans le sens inverse, CO + Cl₂ → COCl₂, ce que la loi de modération prévoit aussi pour un ajout de CO.
4. Le tableau ci-dessus, écrit avec l'avancement x de la réaction qui se produit, ici l'inverse, donne une quantité totale de gaz de 0,76 − x.
5. On mesure 0,71 mol au nouvel équilibre : 0,76 − x = 0,71, donc x = 0,05 mol, soit n(COCl₂) = 0,21 mol, n(CO) = 0,35 mol et n(Cl₂) = 0,15 mol.
6. Contrôle : Π = (0,35/2,00)(0,15/2,00) / (0,21/2,00) = 0,175 × 0,075 / 0,105 = 0,125 = K. Le quotient est revenu à K.

:::

::: piege
**Erreur : écrire le tableau à partir de l'ancien équilibre.** On met 0,20 mol de CO dans la ligne initiale, comme avant l'ajout. La quantité totale vaut alors 0,56 − x, et avec 0,71 mol on obtiendrait x = −0,15 mol, un avancement négatif absurde pour la réaction choisie. L'erreur tente parce que l'ancien équilibre est la seule composition donnée en début d'énoncé ; mais la ligne initiale décrit le système juste après la perturbation, ajout compris.
:::

::: methode Calculer le nouvel équilibre
1. Écrire la composition juste après la perturbation, ajout ou retrait compris.
2. Calculer Π avec cette composition et le comparer à K, pour donner le sens d'évolution.
3. Tracer le tableau d'avancement dans ce sens, avec x positif pour la réaction qui se produit.
4. Trouver x avec la donnée de l'énoncé (quantité totale, quantité d'une espèce) ou avec K.
5. Calculer la composition finale, puis vérifier que Π = K.
:::

::: verifie À toi : un autre ajout
Même équilibre (4), mêmes quantités. On ajoute cette fois 0,20 mol de Cl₂ au lieu de CO. Calculer Π juste après l'ajout et donner le sens d'évolution.

---

Après l'ajout, n(Cl₂) = 0,40 mol, soit [Cl₂] = 0,20 mol·L⁻¹, les autres concentrations étant [COCl₂] = 0,080 et [CO] = 0,10 mol·L⁻¹. Π = 0,10 × 0,20 / 0,080 = 0,25 > K = 0,125 : le système évolue dans le sens inverse.
:::

::: retenir
Le nouveau tableau part de la composition juste après la perturbation ; on compare Π à K pour le sens, on trouve x avec une donnée, et au nouvel équilibre Π = K.
:::

## 🏭 Le compromis industriel : rendement contre vitesse

L'ammoniac NH₃, que l'on fabrique par N₂(g) + 3 H₂(g) ⇄ 2 NH₃(g) (5), de réaction directe exothermique, sert surtout à fabriquer des engrais. D'après la loi de modération, il faudrait refroidir pour augmenter la quantité d'ammoniac ; or l'industriel travaille vers 450 °C.
Pourquoi choisit-il une température qui n'est pas la plus favorable au taux d'avancement final, c'est-à-dire au rendement à l'équilibre ?

::: figure Allure schématique (sans échelle) : le rendement à l'équilibre diminue quand la température augmente, la vitesse de réaction augmente ; la température retenue est un compromis entre les deux courbes
<svg viewBox="0 0 340 236"><title>Rendement à l'équilibre et vitesse de réaction en fonction de la température</title><line x1="54" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="54" y1="190" x2="54" y2="18" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="54,14 50,22 58,22" fill="#0f172a"/><text x="330" y="206" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">T</text><polyline points="54,50 62,51.6 70,53.7 78,56 86,58.4 94,61 102,63.7 110,66.5 118,69.4 126,72.3 134,75.3 142,78.4 150,81.5 158,84.7 166,87.9 174,91.2 182,94.5 190,97.9 198,101.3 206,104.7 214,108.2 222,111.7 230,115.2 238,118.8 246,122.4 254,126.1 262,129.7 270,133.4 278,137.1 286,140.9 294,144.7 302,148.5 310,152.3 318,156.1 326,160" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round"/><polyline points="54,176 62,175.5 70,174.6 78,173.3 86,171.8 94,169.9 102,167.9 110,165.6 118,163.2 126,160.5 134,157.7 142,154.6 150,151.4 158,148.1 166,144.6 174,140.9 182,137.1 190,133.1 198,129 206,124.8 214,120.4 222,115.9 230,111.2 238,106.4 246,101.5 254,96.5 262,91.4 270,86.1 278,80.7 286,75.2 294,69.6 302,63.9 310,58 318,52.1 326,46" fill="none" stroke="#d97706" stroke-width="2.5" stroke-linejoin="round"/><line x1="220" y1="190" x2="220" y2="24" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 4"/><text x="220" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">T retenue</text><text x="60" y="40" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">rendement</text><text x="322" y="34" text-anchor="end" font-size="11" font-weight="700" fill="#d97706" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">vitesse</text></svg>
:::

Taux d'avancement final de la synthèse (5), mélange de départ stœchiométrique, valeurs arrondies d'illustration :

| θ (°C) | P = 100 atm | P = 300 atm |
| ------ | ----------- | ----------- |
| 300    | 0,68        | 0,83        |
| 450    | 0,28        | 0,52        |
| 600    | 0,07        | 0,19        |

::: exemple Lire le tableau puis justifier les conditions industrielles

1. À P fixée, τ_f diminue quand θ augmente (0,68 ; 0,28 ; 0,07 à 100 atm) : la hausse de température favorise la réaction inverse, donc la synthèse est exothermique.
2. À θ fixée, τ_f augmente avec P (0,28 puis 0,52 à 450 °C) : la hausse de pression favorise la réaction directe, ce qui concorde avec les 4 mol de gaz à gauche et 2 mol à droite.
3. Pour le meilleur rendement, il faudrait donc une basse température et une forte pression.
4. Mais à basse température la réaction est très lente (facteurs cinétiques, chapitre 3) : l'équilibre ne serait atteint qu'au bout d'un temps beaucoup trop long.
5. On travaille donc à température élevée, vers 450 °C, avec un catalyseur qui accélère la réaction sans changer τ_f, et à très forte pression, de l'ordre de plusieurs centaines d'atmosphères, pour compenser la perte de rendement.

:::

::: piege
**Erreur : croire que le catalyseur améliore le rendement.** On l'ajoute parce que « le catalyseur fait produire plus d'ammoniac ». L'erreur tente parce que l'on obtient plus vite plus d'ammoniac ; mais le catalyseur accélère les deux réactions de la même façon : l'état d'équilibre et τ_f restent les mêmes, seul le temps pour l'atteindre diminue.
:::

::: propriete
**Compromis industriel** — Un facteur qui améliore le rendement peut ralentir la réaction, et inversement : l'industriel choisit les conditions qui donnent un bon taux d'avancement final en un temps raisonnable. Une forte pression compense la perte de rendement due à la température ; la température est un compromis ; le catalyseur ne joue que sur la vitesse.
Cas limite : pour une réaction athermique comme l'estérification, la température ne change pas τ_f : on chauffe seulement pour aller plus vite.
:::

::: verifie À toi : le méthanol
La synthèse CO(g) + 2 H₂(g) ⇄ CH₃OH(g) est exothermique. Quelles conditions de température et de pression donnent le meilleur taux d'avancement final, et pourquoi n'utilise-t-on pas la température la plus basse possible ?

---

La réaction directe est exothermique et diminue n_g (3 mol de gaz à gauche, 1 à droite) : le meilleur τ_f s'obtient à basse température et à forte pression. À très basse température la réaction est trop lente pour atteindre l'équilibre en un temps raisonnable, d'où une température plus élevée et un catalyseur.
:::

::: retenir
Un bon rendement ne suffit pas : on choisit une température élevée et un catalyseur pour la vitesse, une forte pression pour le rendement, et le catalyseur ne change pas τ_f.
:::

> 🏆 Tu sais désormais prévoir le sens d'un déplacement, le justifier par Π et K quand la loi se tait, et chiffrer le nouvel équilibre. Le thème suivant s'appuiera sur ces équilibres pour étudier les réactions acide-base.
