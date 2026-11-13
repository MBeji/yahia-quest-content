# ⚔️ L'analyse de l'évolution du stock — le tableau de bord du magasinier

> 💡 «Un stock ne se juge pas à son montant, mais à son poids dans l'entreprise et à la vitesse à laquelle il se renouvelle.»

La Papeterie Salma vend des cahiers et des fournitures scolaires. Sa gérante veut savoir si ses rayons sont bien gérés : trop pleins, ils coûtent cher ; presque vides, ils font perdre des clients. Ce chapitre lui donne sept outils de lecture : la part des stocks dans l'actif, le stock moyen, les achats consommés, le coefficient de rotation, la durée du stockage, l'interprétation de ces ratios et le stock moyen d'un approvisionnement régulier.

Les données de l'année N de la Papeterie Salma (en dinars, D), reprises tout au long du chapitre. Les chiffres de ce chapitre sont des valeurs choisies pour s'entraîner, pas des données réelles d'une entreprise.

| Donnée                              | Fin de l'année N-1 | Fin de l'année N |
| ----------------------------------- | ------------------ | ---------------- |
| Stock de marchandises               | 40 000 D           | 60 000 D         |
| Total des actifs (bilan fonctionnel) | 200 000 D          | 250 000 D        |

Les achats de marchandises de l'année N s'élèvent à 320 000 D. Les entreprises du même secteur ont, en moyenne, une part des stocks de 22 % et un coefficient de rotation de 7,2. En N-1, le coefficient de rotation de la Papeterie Salma était de 7.

## ⚖️ La part des stocks dans l'actif : pèse-t-il trop lourd ?

Au 31/12/N, la Papeterie Salma détient 60 000 D de stock dans un bilan de 250 000 D. Ce stock est-il « gros » ?
Un chiffre isolé ne le dit pas : il faut le rapporter à quelque chose.

::: definition
Un **ratio** compare deux grandeurs de l'entreprise en divisant l'une par l'autre ; on ne le calcule que si ce rapport a un sens économique. La **part des stocks dans l'actif** mesure le poids du stock dans le patrimoine de l'entreprise. Plus elle augmente, plus l'entreprise mobilise de ressources pour financer et détenir ses stocks.

Part des stocks = Stocks ÷ Total des actifs
:::

::: exemple La part des stocks de la Papeterie Salma

1. Année N : stocks 60 000 D, total des actifs 250 000 D — on rapporte le stock à tout ce que possède l'entreprise.
2. 60 000 ÷ 250 000 = 0,24, soit 24 %.
3. Année N-1 : 40 000 ÷ 200 000 = 0,20, soit 20 % — même calcul, année précédente, pour voir l'évolution.
4. Le secteur est à 22 % : en N, la Papeterie Salma est au-dessus de la moyenne, et elle y est arrivée en montant.

:::

::: piege Lire la hausse de la part comme une hausse des stocks
On écrit « la part passe de 20 % à 25 %, donc le stock a augmenté ». Cela tente parce que ratio et stock vont souvent dans le même sens. Mais une quincaillerie dont le stock tombe de 50 000 D à 45 000 D, alors que son actif total tombe de 250 000 D à 180 000 D, voit sa part monter de 20 % à 25 % alors que son stock a baissé : c'est le total qui a fondu plus vite. On lit le ratio, mais on vérifie aussi les deux montants.
:::

::: verifie
Une quincaillerie a 36 000 D de stocks pour 120 000 D d'actifs au total. Le secteur est à 35 %. Quelle est la part de ses stocks, et se situe-t-elle au-dessus ou au-dessous du secteur ?

---

Part des stocks = 36 000 ÷ 120 000 = 0,30, soit 30 %. Elle est au-dessous des 35 % du secteur : le stock pèse moins lourd que chez ses concurrents.
:::

::: retenir
Part des stocks = Stocks ÷ Total des actifs ; on la compare à l'année précédente et au secteur.
:::

## 📏 Le stock moyen : un seul chiffre pour toute l'année

Le stock de la Papeterie Salma était de 40 000 D au début de l'année et de 60 000 D à la fin. Entre les deux, il a varié.
Quel chiffre résume le niveau du stock sur l'année ?

::: definition
Le **stock moyen** (SM) est la moyenne du **stock initial** (SI, relevé au bilan de début d'exercice) et du **stock final** (SF, relevé au bilan de fin d'exercice).

SM = (SI + SF) ÷ 2
:::

::: exemple Le stock moyen de la Papeterie Salma

1. SI = 40 000 D (bilan de fin N-1, donc début de N) et SF = 60 000 D (bilan de fin N).
2. SI + SF = 40 000 + 60 000 = 100 000 D — on additionne les deux relevés.
3. SM = 100 000 ÷ 2 = 50 000 D — le milieu entre les deux relevés.

:::

::: piege Retenir seulement le stock final
On écrit « le stock de l'année est de 60 000 D ». Cela tente parce que c'est le chiffre du dernier bilan, le plus récent. Mais l'entreprise a démarré l'année avec 40 000 D : prendre 60 000 D seul surestime le stock porté pendant l'année. Le stock moyen est 50 000 D.
:::

::: verifie
Un commerçant avait 18 000 D de stock au début de l'année et 30 000 D à la fin. Quel est son stock moyen ?

---

SM = (18 000 + 30 000) ÷ 2 = 48 000 ÷ 2 = 24 000 D.
:::

::: retenir
Stock moyen = (stock initial + stock final) ÷ 2 : les deux relevés, jamais un seul.
:::

## 🧾 Les achats consommés : ce qui est réellement sorti du stock

En N, la Papeterie Salma a acheté pour 320 000 D de marchandises. Mais son stock a grossi de 20 000 D : tout ce qui a été acheté n'est donc pas parti.
Quel montant est réellement sorti des rayons ?

::: definition
Le montant **A** est le coût de ce qui a été vendu ou consommé dans l'année :

- pour des marchandises : le coût d'achat des marchandises vendues ;
- pour des matières premières : le coût d'achat des matières consommées ;
- pour des produits fabriqués : le coût de production des quantités vendues.

Pour des marchandises ou des matières, on le calcule ainsi :

A = Achats + SI − SF
:::

::: exemple Les achats consommés de la Papeterie Salma

1. Au départ, le magasin contient 40 000 D (SI) et il reçoit 320 000 D d'achats : 360 000 D étaient disponibles.
2. À la fin, 60 000 D (SF) sont encore là : ils n'ont pas été consommés.
3. A = 320 000 + 40 000 − 60 000 = 300 000 D — le disponible moins ce qui reste.

:::

::: piege Inverser les deux stocks
On écrit « A = 320 000 − 40 000 + 60 000 = 340 000 D ». Cela tente parce qu'on pense « variation de stock » sans se demander dans quel sens. Mais le stock final est ce qui reste : on le retranche. Ici le stock a augmenté, donc il est sorti moins que ce qu'on a acheté, et non plus.
:::

::: propriete
- Le stock augmente (SF > SI) : A est plus petit que les achats.
- Le stock diminue (SF < SI) : A est plus grand que les achats.
- Le stock ne bouge pas (SF = SI) : A est égal aux achats.
- Pour des produits finis, on applique le même raisonnement au coût de production de la période : coût de production des produits vendus = coût de production de la période + SI − SF.
:::

::: verifie
Une boutique avait 25 000 D de stock au début de l'année, a acheté pour 180 000 D et termine avec 15 000 D. Quel montant a-t-elle vendu, au coût d'achat ?

---

A = 180 000 + 25 000 − 15 000 = 190 000 D. Le stock a diminué de 10 000 D : il est sorti 10 000 D de plus que ce qui a été acheté.
:::

::: retenir
A = Achats + stock initial − stock final : on mesure ce qui est sorti, pas ce qui est entré.
:::

## 🔁 Le coefficient de rotation : combien de fois le stock se renouvelle

La Papeterie Salma a vendu pour 300 000 D de marchandises (au coût d'achat) avec un stock moyen de 50 000 D.
Combien de fois l'équivalent de son stock moyen est-il passé par la caisse dans l'année ?

::: definition
Le **coefficient de rotation** (r) compte combien de fois, sur l'année, l'entreprise a vendu ou consommé l'équivalent de son stock moyen.

r = A ÷ SM
:::

::: exemple La rotation de la Papeterie Salma

1. A = 300 000 D (calculé plus haut) : ce qui est sorti dans l'année.
2. SM = 50 000 D : le stock porté en moyenne.
3. r = 300 000 ÷ 50 000 = 6 — le stock moyen s'est renouvelé 6 fois dans l'année.

:::

::: piege Mettre les achats au numérateur
On écrit « r = 320 000 ÷ 50 000 = 6,4 ». Cela tente parce que les achats sont donnés directement, alors que A demande un calcul. Mais les achats mesurent ce qui est entré, pas ce qui est sorti : le coefficient de rotation se calcule avec A, d'où r = 6.
:::

::: verifie
Un grossiste a un stock initial de 30 000 D, un stock final de 42 000 D et des achats de 282 000 D. Quel est son coefficient de rotation ?

---

SM = (30 000 + 42 000) ÷ 2 = 36 000 D. A = 282 000 + 30 000 − 42 000 = 270 000 D. r = 270 000 ÷ 36 000 = 7,5.
:::

::: retenir
r = A ÷ SM : le nombre de fois où le stock moyen est vendu ou consommé dans l'année.
:::

## ⏱️ La durée du stockage : combien de jours reste la marchandise

Un coefficient de 6 parle de « fois par an ». La gérante préfère un langage de jours.
Combien de temps un article reste-t-il en moyenne dans le magasin avant de partir ?

::: definition
La **durée du stockage** est le nombre de jours moyen pendant lesquels le stock est détenu. On compte l'année commerciale à 360 jours.

Durée du stockage = 360 ÷ r
:::

::: exemple La durée du stockage de la Papeterie Salma

1. r = 6 : le stock se renouvelle 6 fois en 360 jours.
2. Chaque renouvellement dure donc 360 ÷ 6 — on partage l'année en 6 périodes égales.
3. Durée = 60 jours : la marchandise reste en moyenne deux mois en rayon.

:::

::: piege Multiplier au lieu de diviser
On écrit « durée = 360 × 6 = 2 160 jours ». Cela tente parce que 360 et r sont les deux seuls nombres sous les yeux. Mais 2 160 jours font six ans : un stock qui se renouvelle 6 fois par an ne peut pas rester six ans. Plus la rotation est rapide, plus la durée est courte : on divise, 360 ÷ 6 = 60 jours.
:::

::: propriete
- Plus r est élevé, plus la durée du stockage est courte, et inversement.
- La durée n'est pas toujours entière : avec r = 7, 360 ÷ 7 ≈ 51,4, soit environ 51 jours.
- Une rotation d'une fois par an donne 360 jours : le stock met l'année entière à se renouveler.
:::

::: verifie
Le coefficient de rotation d'une entreprise est de 7,5. Quelle est la durée de son stockage ?

---

Durée = 360 ÷ 7,5 = 48 jours. Le stock se renouvelle donc tous les 48 jours en moyenne.
:::

::: retenir
Durée du stockage = 360 ÷ r : une rotation rapide donne une durée courte.
:::

## 🔍 Interpréter : comparer, puis conclure

La Papeterie Salma a r = 6 et une durée de 60 jours. Est-ce bon ou mauvais ? Un ratio seul ne répond pas.
Il faut un point de comparaison.

::: definition
Les ratios de rotation sont des **indicateurs de gestion**. On les interprète de deux façons : **dans le temps** (l'année précédente) et **entre entreprises** du même secteur (la moyenne du secteur). Un stock important **immobilise des fonds** et engendre des **coûts de possession** : loyer du local, assurance, détérioration ou démarque, et intérêt de l'argent bloqué dans les rayons.
:::

::: exemple Le diagnostic de la Papeterie Salma

1. En N-1, r = 7, donc une durée de 360 ÷ 7 ≈ 51 jours ; en N, r = 6, donc 60 jours : la rotation ralentit.
2. Le secteur est à r = 7,2, soit 360 ÷ 7,2 = 50 jours : la Papeterie Salma garde ses articles 10 jours de plus que la moyenne.
3. Sa part des stocks est passée de 20 % à 24 %, au-dessus des 22 % du secteur : les deux ratios disent la même chose.
4. Conclusion : le stock devient lourd et lent ; l'entreprise vend moins vite ou achète trop, et ses coûts de possession augmentent.

:::

::: piege Juger un ratio sans point de comparaison
On écrit « r = 6, c'est faible ». Cela tente parce que 6 paraît petit à côté de 360. Mais un coefficient ne vaut que comparé : la même valeur peut être normale pour un vendeur de meubles et très lente pour un épicier, dont les produits se périment. On compare toujours à l'année précédente et au secteur avant de conclure.
:::

::: propriete
- En principe, plus le stock tourne vite, plus les frais de stockage sont faibles ; l'entreprise a intérêt à un coefficient élevé et à une durée courte.
- Ce principe a une limite : un stock proche de zéro expose à la rupture, c'est-à-dire à des ventes perdues faute de marchandise.
- La rotation dépend aussi de la nature des produits : un article saisonnier ne tourne pas comme un produit de consommation courante.
- Quand r d'un produit fini varie, c'est souvent le signe que le rythme des ventes a changé ; on vérifie aussi si le niveau du stock a bougé.
:::

::: verifie
Une entreprise a r = 5 cette année contre 4,5 l'an dernier ; le secteur est à 4. Que peut-on conclure sur sa gestion du stock ?

---

Elle tourne plus vite que le secteur (5 contre 4) et plus vite qu'avant (5 contre 4,5) : durées de 72 jours (360 ÷ 5) contre 90 jours pour le secteur. Sa gestion du stock est plutôt favorable, à condition de vérifier qu'elle ne frôle pas la rupture.
:::

::: retenir
Un ratio se lit par comparaison, avec l'année précédente et avec le secteur ; un stock lent immobilise des fonds et coûte cher.
:::

## 🚚 Le stock moyen d'un approvisionnement régulier : combien de commandes ?

La Papeterie Salma consomme régulièrement 12 000 rames de papier par an. Si elle les commande en une seule fois, elle immobilise 12 000 rames en janvier.
Et si elle commande plus souvent, le stock moyen change-t-il ?

::: definition
Quand la consommation est **régulière** et que chaque livraison arrive au moment où le stock est vide, le stock descend de la quantité commandée jusqu'à zéro, puis remonte d'un coup. Pour une consommation annuelle Q répartie en N commandes égales (attention : ici N est un nombre de commandes, pas l'année), chaque commande porte sur Q ÷ N et le stock moyen est :

SM = Q ÷ (2 × N)
:::

::: exemple Les rames de papier de la Papeterie Salma

1. N = 1 : une commande de 12 000 rames, le stock va de 12 000 à 0, donc en moyenne 6 000 rames (la moitié).
2. N = 2 : deux commandes de 12 000 ÷ 2 = 6 000 rames ; le stock va de 6 000 à 0, donc en moyenne 3 000 rames.
3. N = 4 : quatre commandes de 3 000 rames ; en moyenne 1 500 rames — on retrouve 12 000 ÷ (2 × 4).
4. Chaque fois que le nombre de commandes double, le stock moyen est divisé par deux : commander plus souvent allège le stock.

:::

::: piege Confondre la quantité commandée et le stock moyen
On écrit « avec 4 commandes, le stock moyen est de 12 000 ÷ 4 = 3 000 rames ». Cela tente parce que 3 000 est bien la taille d'une commande. Mais le stock ne reste pas à 3 000 : il descend de 3 000 à 0, donc son niveau moyen est la moitié, 1 500 rames.
:::

::: verifie
Une entreprise consomme régulièrement 7 200 kg de farine par an et passe 6 commandes égales. Quel est son stock moyen ?

---

Chaque commande porte sur 7 200 ÷ 6 = 1 200 kg ; le stock va de 1 200 à 0, donc SM = 1 200 ÷ 2 = 600 kg, soit 7 200 ÷ (2 × 6).
:::

::: retenir
Pour une consommation régulière Q et N commandes : SM = Q ÷ (2 × N) ; avec une seule commande, SM = Q ÷ 2.
:::
