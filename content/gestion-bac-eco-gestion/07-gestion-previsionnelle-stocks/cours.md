# ⚔️ La gestion prévisionnelle des stocks — quand commander, et combien

> 💡 «Bien gérer un stock, ce n'est ni en avoir peu, ni en avoir beaucoup : c'est le renouveler au bon moment, en bonne quantité.»

Mabrouk Bureautique est un grossiste de cartouches d'encre. Son responsable des achats doit répondre à trois questions : à partir de quel niveau de stock passer commande, combien de commandes faire dans l'année, et à quelles dates. Ce chapitre lui donne six outils : les niveaux de stock, les deux coûts qui s'opposent, le tableau des coûts, la formule de Wilson, le lot économique avec ses dates, et la lecture sur graphique.

Les données de Mabrouk Bureautique, reprises tout au long du chapitre. Les chiffres sont des valeurs choisies pour s'entraîner, pas des données réelles d'une entreprise.

| Donnée                                         | Valeur            |
| ---------------------------------------------- | ----------------- |
| Consommation annuelle régulière (Q)            | 1 800 cartouches  |
| Prix d'achat d'une cartouche                   | 20 D              |
| Délai d'approvisionnement (commande → livraison) | 15 jours          |
| Coût de passation d'une commande (p)           | 100 D             |
| Taux de possession annuel (i)                  | 0,20 par dinar de stock |

La valeur de la consommation annuelle est donc C = 1 800 × 20 = 36 000 D. L'année commerciale compte 360 jours.

## 🚦 Les niveaux de stock : à quel moment commander ?

Si Mabrouk attend que son rayon soit vide pour commander, son fournisseur met encore 15 jours à livrer : pendant ces 15 jours, plus aucune cartouche à vendre, c'est une **rupture de stock**.
À quel niveau faut-il donner le signal de commande ?

::: definition
Le responsable des stocks suit plusieurs **niveaux de stock** :

- le **stock maximum** : la quantité à ne pas dépasser, pour éviter le surstockage et des coûts inutiles ;
- le **stock minimum** : la quantité consommée pendant le délai d'approvisionnement, ce qui permet de recevoir la livraison au moment où le stock devient nul ;
- le **stock de sécurité** : une réserve en plus du stock minimum, pour se protéger d'un retard de livraison ou d'une hausse brusque des besoins ;
- le **stock d'alerte** : stock minimum + stock de sécurité ;
- le **stock outil**, ou stock moyen : le stock dont l'entreprise dispose en moyenne ; il immobilise des fonds.

Exemple : si l'entreprise consomme 5 unités par jour et que le fournisseur livre en 15 jours, elle consomme 75 unités pendant le délai : c'est son stock minimum.

L'**état du stock** se calcule ainsi : stock initial + entrées − sorties.
:::

::: exemple Les niveaux de stock de Mabrouk Bureautique

1. Consommation par jour : 1 800 ÷ 360 = 5 cartouches — la consommation étant régulière, c'est la même chaque jour.
2. Stock minimum = 5 × 15 = 75 cartouches — ce que Mabrouk vend pendant les 15 jours de livraison.
3. Mabrouk garde en plus une réserve de sécurité de 30 cartouches : stock d'alerte = 75 + 30 = 105 cartouches.
4. Il commande donc dès que son stock tombe à 105. Si la livraison arrive à temps, il lui reste alors 30 cartouches, la réserve intacte.

:::

::: piege Commander au stock minimum alors qu'une réserve existe
On écrit « je commande quand il reste 75 cartouches, c'est le stock minimum ». Cela tente parce que le stock minimum couvre exactement le délai. Mais si le fournisseur a 6 jours de retard, il manque 6 × 5 = 30 cartouches : le stock est vide pendant 6 jours. Dès qu'une réserve de sécurité existe, le signal part au stock d'alerte, 105 cartouches ; sans réserve, le stock minimum suffit.
:::

::: verifie
Une papeterie vend régulièrement 4 ramettes par jour ; son fournisseur livre en 10 jours et elle garde une réserve de sécurité de 25 ramettes. Quel est son stock minimum, et à quel niveau commande-t-elle ?

---

Stock minimum = 4 × 10 = 40 ramettes. Stock d'alerte = 40 + 25 = 65 ramettes : c'est à ce niveau qu'elle commande, puisqu'elle détient une réserve de sécurité.
:::

::: retenir
Stock d'alerte = stock minimum + stock de sécurité : le minimum couvre le délai, la sécurité couvre l'imprévu.
:::

## 💰 Deux coûts qui s'opposent : passer commande, garder du stock

Commander souvent évite de garder beaucoup de cartouches, mais chaque commande demande du travail. Commander rarement réduit le travail, mais il faut ranger, surveiller et financer un gros stock.
Quels frais faut-il distinguer ?

::: definition
- Le **coût de passation** (ou de lancement) d'une commande regroupe les frais engagés à chaque commande : téléphone, secrétariat, vérification, négociation, courrier, documentation. En général, on le considère constant quel que soit le montant de la commande. On le note p.
- Le **coût de possession** (ou de détention) du stock regroupe les frais liés au fait de garder du stock : location ou amortissement des hangars et du matériel de manutention, personnel de manutention, d'entretien et de gardiennage, intérêts des emprunts qui financent l'achat du stock, assurance des marchandises stockées, vieillissement des articles. On l'exprime par un **taux de possession** i : le coût annuel de possession pour 1 D de stock.
- Le **coût total d'approvisionnement** est la somme du coût de passation et du coût de possession sur une période.
:::

::: exemple Les coûts de Mabrouk Bureautique

1. Le loyer du magasin est engagé parce que Mabrouk garde du stock : coût de possession.
2. L'appel au fournisseur et le courrier de confirmation sont engagés à chaque commande : coût de passation.
3. Avec 8 commandes dans l'année, le coût de passation est 8 × 100 = 800 D — chaque commande coûte la même chose.
4. Avec un stock moyen de 2 250 D et i = 0,20, le coût de possession est 2 250 × 0,20 = 450 D.
5. Coût total d'approvisionnement = 800 + 450 = 1 250 D.

:::

::: piege Croire qu'une grosse commande coûte plus cher à passer
On écrit « une commande de 500 cartouches coûte plus cher à passer qu'une commande de 50 ». Cela tente parce qu'on pense à la facture du fournisseur. Mais la facture d'achat n'est pas un frais de passation : le téléphone, le courrier et la vérification coûtent à peu près la même chose pour 50 ou 500 cartouches. Le coût de passation reste p par commande, et seul le nombre de commandes le fait varier.
:::

::: verifie
Une entreprise passe 12 commandes par an à 45 D de frais chacune. Son stock moyen vaut 8 000 D et son taux de possession est de 0,15. Quel est son coût total d'approvisionnement ?

---

Passation = 12 × 45 = 540 D. Possession = 8 000 × 0,15 = 1 200 D. Total = 540 + 1 200 = 1 740 D.
:::

::: retenir
Coût total = coût de passation (p par commande) + coût de possession (i par dinar de stock détenu).
:::

## 📊 Comment les coûts varient avec le nombre de commandes

Mabrouk hésite : une grosse commande par an, six commandes, douze ?
Comment chaque coût réagit-il quand le nombre de commandes N change ?

::: definition
Quand la consommation est régulière et que chaque livraison arrive à stock nul, la valeur du stock moyen est C ÷ (2 × N), où C est la valeur de la consommation annuelle et N le nombre de commandes égales. On en tire :

- coût total de possession = C × i ÷ (2 × N)
- coût total de passation = N × p
- coût total d'approvisionnement = C × i ÷ (2 × N) + N × p

(La réserve de sécurité, qui ne dépend pas de N, est laissée de côté dans ce calcul.)
:::

::: exemple Le tableau de Mabrouk Bureautique

Avec C = 36 000 D, i = 0,20 et p = 100 D, on calcule chaque ligne : possession = 7 200 ÷ (2 × N), passation = 100 × N.

| N | Possession | Passation | Total d'approvisionnement |
| - | ---------- | --------- | ------------------------- |
| 1 | 3 600 D    | 100 D     | 3 700 D                   |
| 2 | 1 800 D    | 200 D     | 2 000 D                   |
| 3 | 1 200 D    | 300 D     | 1 500 D                   |
| 4 | 900 D      | 400 D     | 1 300 D                   |
| 5 | 720 D      | 500 D     | 1 220 D                   |
| 6 | 600 D      | 600 D     | 1 200 D                   |
| 7 | 514,29 D   | 700 D     | 1 214,29 D                |

1. La possession baisse à chaque ligne : plus on commande, plus le stock moyen est petit.
2. La passation monte à chaque ligne : chaque commande ajoute 100 D.
3. Le total baisse jusqu'à N = 6, puis remonte à N = 7 : le minimum, 1 200 D, est atteint avec 6 commandes.

:::

::: piege Choisir le N qui rend le stock le plus petit
On écrit « à N = 7, le stock moyen est le plus faible, donc c'est le meilleur choix ». Cela tente parce qu'un petit stock paraît signe de bonne gestion. Mais on ne minimise pas la possession seule : à N = 7 le total, 1 214,29 D, dépasse celui de N = 6, 1 200 D. Un stock réduit n'est donc pas forcément le reflet d'une saine gestion.
:::

::: propriete
- Quand N augmente, le coût de possession diminue et le coût de passation augmente.
- Le coût total diminue d'abord, atteint un minimum, puis remonte : c'est une courbe en U.
- Cas limite : avec une seule commande (N = 1), le stock moyen est la moitié de toute la consommation annuelle, ce qui donne le plus gros coût de possession du tableau.
:::

::: verifie
Pour C = 24 000 D, i = 0,25 et p = 150 D, quel est le coût total d'approvisionnement avec N = 4 ?

---

Possession = 24 000 × 0,25 ÷ 8 = 750 D. Passation = 4 × 150 = 600 D. Total = 750 + 600 = 1 350 D.
:::

::: retenir
Avec N commandes : possession = C × i ÷ (2 × N), passation = N × p ; on cherche le N qui rend leur somme minimale.
:::

## 🧮 La formule de Wilson : le nombre optimal de commandes

Construire un tableau ligne par ligne est long, et on peut s'arrêter trop tôt.
Existe-t-il un calcul direct du N qui rend le coût total minimal ?

::: definition
Le **nombre optimal de commandes** N*, ou **cadence d'approvisionnement**, est le nombre de commandes qui rend le coût total d'approvisionnement minimal. La **formule de Wilson** le donne, en cherchant le N qui annule la dérivée du coût total :

N* = √(C × i ÷ (2 × p))

C est la valeur de la consommation de la période, i le taux de possession de la même période et p le coût de passation d'une commande.

D'où vient-elle ? Le coût total est f(N) = C × i ÷ (2 × N) + N × p. Sa dérivée f'(N) = p − C × i ÷ (2 × N²) s'annule quand N² = C × i ÷ (2 × p).
:::

::: exemple Wilson pour Mabrouk Bureautique

1. C × i = 36 000 × 0,20 = 7 200 — la valeur de la consommation, pas le nombre de cartouches.
2. 2 × p = 2 × 100 = 200.
3. 7 200 ÷ 200 = 36, donc N* = √36 = 6 commandes — le même résultat que le tableau.

:::

::: piege Mettre la quantité à la place de la valeur
On écrit « N* = √(1 800 × 0,20 ÷ 200) = √1,8 ≈ 1,3 ». Cela tente parce que 1 800 est le chiffre de la consommation annuelle. Mais la formule compare des dinars : C est la valeur de la consommation, 1 800 × 20 = 36 000 D. Avec la quantité, on trouve moins de 2 commandes au lieu de 6.
:::

::: propriete
- À N*, le coût de passation égale le coût de possession : ici 600 D et 600 D, pour un total minimal de 1 200 D.
- Plus le coût de passation p est élevé, plus N* est petit : on groupe les commandes.
- Plus le taux de possession i est élevé, plus N* est grand : on commande plus souvent pour garder moins de stock.
- Cas limite : si p et i augmentent dans les mêmes proportions, N* ne change pas.
:::

::: verifie
Une entreprise consomme pour 40 000 D par an, avec i = 0,25 et p = 50 D. Quel est son nombre optimal de commandes ?

---

C × i = 40 000 × 0,25 = 10 000 ; 2 × p = 100 ; 10 000 ÷ 100 = 100, donc N* = √100 = 10 commandes.
:::

::: retenir
N* = √(C × i ÷ (2 × p)), avec C en dinars : à l'optimum, passation et possession s'égalisent.
:::

## 📅 Le lot économique et les dates de livraison

Mabrouk sait qu'il doit passer 6 commandes par an.
Combien de cartouches par commande, et tous les combien de temps ?

::: definition
Quand la consommation annuelle est régulière, on commande des quantités égales à intervalles réguliers. Pour une quantité annuelle Q et N* commandes :

- le **lot économique** est q* = Q ÷ N* ;
- les livraisons ont lieu **tous les 12 ÷ N* mois**.
:::

::: exemple La politique d'achat de Mabrouk Bureautique

1. q* = 1 800 ÷ 6 = 300 cartouches — on partage la quantité annuelle entre les 6 commandes.
2. Intervalle = 12 ÷ 6 = 2 mois.
3. Mabrouk commande 300 cartouches tous les 2 mois.
4. Contrôle : 6 × 300 = 1 800 cartouches, toute la consommation de l'année.

:::

::: piege Diviser la valeur au lieu de la quantité
On écrit « q* = 36 000 ÷ 6 = 6 000 cartouches ». Cela tente parce que 36 000 vient d'être utilisé dans la formule de Wilson. Mais 36 000 est une valeur en dinars : 6 000 cartouches à 20 D coûteraient 120 000 D. Le lot se calcule avec la quantité Q, en unités ; la valeur C ÷ N* donne, elle, le montant en dinars de chaque commande, soit 6 000 D.
:::

::: propriete
- Le lot et l'intervalle se calculent tous deux à partir de N*.
- Si N* = 12, on reçoit une livraison par mois ; si N* = 1, une seule livraison dans l'année.
- Le résultat de 12 ÷ N* n'est pas toujours un nombre entier de mois : avec N* = 5, il vaut 2,4 mois.
:::

::: verifie
Une entreprise consomme 2 400 unités par an et son nombre optimal de commandes est de 4. Quel est son lot économique, et tous les combien de mois est-elle livrée ?

---

q* = 2 400 ÷ 4 = 600 unités. Intervalle = 12 ÷ 4 = 3 mois : un lot de 600 unités tous les 3 mois.
:::

::: retenir
q* = Q ÷ N* en unités, et une livraison tous les 12 ÷ N* mois.
:::

## 📈 La résolution graphique : lire N* sur un graphique

Une formule donne le résultat, mais un graphique le montre.
Comment retrouver N* en dessinant les coûts ?

::: definition
On porte en abscisse le nombre de commandes N et en ordonnée les coûts en dinars. On trace trois courbes : le coût de passation N × p (une droite qui monte), le coût de possession C × i ÷ (2 × N) (une courbe qui descend) et le coût total d'approvisionnement, leur somme (une courbe en U). Le nombre optimal de commandes N* est l'**abscisse du point où se coupent passation et possession** ; c'est là que le coût total est minimal.
:::

::: exemple Le graphique de Mabrouk Bureautique

1. À N = 2, la passation vaut 200 D et la possession 1 800 D : à gauche de N*, la possession domine.
2. À N = 12, la passation vaut 1 200 D et la possession 300 D : à droite de N*, la passation domine.
3. À N = 6, les deux valent 600 D : les courbes se coupent, donc N* = 6.
4. Sous ce point, la courbe du total est à 600 + 600 = 1 200 D, son minimum.

:::

::: piege Lire le coût au lieu du nombre de commandes
On écrit « N* = 600 ». Cela tente parce que 600 est le chiffre qui saute aux yeux à l'intersection. Mais 600 se lit sur l'axe des coûts : c'est un montant en dinars. Le nombre de commandes se lit sur l'axe horizontal, soit 6.
:::

::: verifie
Sur un graphique, les courbes de passation et de possession se coupent au point d'abscisse 5 et d'ordonnée 750 D. Que valent N* et le coût total minimal ?

---

N* est l'abscisse du point d'intersection : N* = 5 commandes. À ce point, passation et possession valent chacune 750 D, donc le coût total minimal est 750 + 750 = 1 500 D.
:::

::: retenir
N* se lit en abscisse, au point où passation et possession se coupent, sous le minimum du coût total.
:::
