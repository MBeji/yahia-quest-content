# ⚔️ Le choix des quantités à fabriquer — plein emploi, quantité optimale et sous-traitance

> 💡 « Une machine qui s'arrête coûte autant qu'une machine qui tourne : le tout est de savoir quoi lui faire fabriquer. »

Les Ateliers Mahrsia fabriquent deux meubles en bois : des chaises (C) et des tables (T). Chaque meuble passe par deux ateliers, la découpe puis la finition, dont le temps disponible est limité. Le gérant se demande combien de chaises et de tables lancer chaque mois, et que faire si les clients en demandent davantage. Huit notions, dans l'ordre où elles s'enchaînent.

Les chiffres de ce chapitre sont des valeurs choisies pour s'entraîner, pas des données réelles d'une entreprise. Les montants sont en dinars (D). Sauf mention contraire, la production d'un mois est entièrement vendue.

## 🔎 Les contraintes de capacité et le plein emploi

Les Ateliers Mahrsia disposent chaque mois d'un temps de travail limité dans chaque atelier. Le service technique a relevé le temps que chaque meuble y passe.

| Meuble | Atelier de découpe | Atelier de finition |
| ------ | ------------------ | ------------------- |
| Une chaise | 2 h | 1 h |
| Une table | 3 h | 2 h |
| Capacité mensuelle | 1 200 h | 700 h |

Peut-on fabriquer autant de chaises et de tables qu'on le souhaite ?

::: definition
Une **contrainte** est une limite que la production ne peut pas dépasser : les contraintes techniques sont les heures disponibles dans un atelier, le nombre de machines ou d'ouvriers, la quantité de matière première ; les contraintes commerciales viennent du marché. La **capacité** est la quantité maximale de travail (heures, kilogrammes) qu'une ressource peut fournir sur la période.

Une contrainte s'écrit comme une **inéquation** : consommation unitaire (temps ou kilogrammes) × quantité, additionnées sur les produits, doivent rester inférieures ou égales à la capacité.

Le **plein emploi** est la situation où chaque atelier est utilisé à 100 % de sa capacité : les inéquations deviennent des égalités.
:::

::: exemple Écrire les contraintes des Ateliers Mahrsia

1. Découpe : une chaise prend 2 h, une table 3 h, d'où 2 C + 3 T ≤ 1 200.
2. Finition : une chaise prend 1 h, une table 2 h, d'où C + 2 T ≤ 700.
3. Le plein emploi correspond à 2 C + 3 T = 1 200 et C + 2 T = 700.

:::

Les temps peuvent être donnés en minutes alors que la capacité est en heures : il faut tout exprimer dans la même unité avant d'écrire l'inéquation.

::: exemple Convertir des minutes en heures

Une chaise de bureau demande 45 mn de découpe, la capacité étant de 1 200 h.

1. 45 mn = 45 ÷ 60 = 0,75 h.
2. Le coefficient de la chaise dans l'inéquation vaut donc 0,75, et non 45.

:::

::: piege Mélanger minutes et heures dans une même inéquation
On écrit « 45 C + 3 T ≤ 1 200 » parce que les chiffres sont sous les yeux dans le tableau. Cela tente parce que l'énoncé donne parfois le temps d'une ligne en minutes et celui d'une autre en heures. Mais une inéquation additionne des temps : tous doivent être dans la même unité que la capacité, ici l'heure (45 mn = 0,75 h).
:::

::: verifie
Un atelier d'emballage dispose de 900 h par mois. Une boîte demande 1,5 h et un coffret 2 h. Écrivez la contrainte, puis dites ce que devient l'inéquation en cas de plein emploi.

---

Contrainte : 1,5 B + 2 K ≤ 900. En plein emploi : 1,5 B + 2 K = 900.
:::

::: retenir
Une contrainte de capacité s'écrit temps unitaire (ou kg de matière) × quantité, additionnés, ≤ capacité, dans la même unité que la capacité. Le plein emploi remplace ≤ par =.
:::

## 🧮 La quantité optimale par la méthode algébrique

Chez Mahrsia, deux ateliers imposent chacun une égalité en plein emploi. Les deux égalités ont deux inconnues, C et T : comment trouver les quantités qui les vérifient en même temps ?
Essayer des quantités au hasard serait long : le gérant cherche la combinaison exacte qui remplit les deux ateliers.

::: definition
La **méthode algébrique** résout le système formé par les égalités de plein emploi : on exprime une inconnue en fonction de l'autre dans une équation, puis on la remplace dans la seconde. Les quantités trouvées sont les **quantités optimales** de plein emploi.
:::

::: exemple Résoudre le système de Mahrsia

1. Système : 2 C + 3 T = 1 200 et C + 2 T = 700.
2. De la seconde : C = 700 − 2 T.
3. On remplace dans la première : 2 (700 − 2 T) + 3 T = 1 200, soit 1 400 − T = 1 200, d'où T = 200.
4. Alors C = 700 − 2 × 200 = 300.
5. Contrôle dans les deux ateliers : 2 × 300 + 3 × 200 = 1 200 h et 300 + 2 × 200 = 700 h : les deux ateliers sont pleins.

:::

::: piege Ne contrôler qu'une seule contrainte
On résout, on trouve C = 300 et T = 200, et on s'arrête. Cela tente parce que le calcul paraît fini. Mais une erreur de calcul sur une équation passe inaperçue : on remplace toujours les quantités dans les deux égalités. Si l'une des deux ne donne pas la capacité, le calcul est faux.
:::

::: verifie
Deux contraintes d'un atelier de reliure donnent A + B = 300 et 2 A + B = 500. Quelles sont les quantités de plein emploi ?

---

De la première : B = 300 − A. Dans la seconde : 2 A + 300 − A = 500, donc A = 200 et B = 100. Contrôle : 200 + 100 = 300 et 400 + 100 = 500.
:::

::: retenir
La méthode algébrique résout les égalités de plein emploi par substitution ; on contrôle le résultat dans les deux contraintes.
:::

## 📐 La méthode graphique et les segments de capacité

Le gérant de Mahrsia veut aussi voir la situation sur un dessin. Comment tracer chaque contrainte avec deux points seulement ?
Le calcul donne un seul point, mais il ne montre pas les autres combinaisons possibles : un dessin les rassemble toutes.

::: definition
Sur un graphique, chaque produit a son axe. Une contrainte donne un **segment de capacité**, tracé à partir de ses deux extrémités : la quantité maximale si l'atelier ne fabrique que le premier produit, puis si l'atelier ne fabrique que le second. Chaque extrémité s'obtient en divisant la capacité par le temps unitaire du produit.

La **zone des solutions possibles** (zone d'acceptabilité) est la surface située sous les deux segments et entre les deux axes : toute combinaison qui s'y trouve respecte les deux contraintes. Les deux segments se coupent au point de plein emploi.
:::

::: exemple Tracer les deux segments de Mahrsia

Axe horizontal : chaises ; axe vertical : tables.

| Atelier | Seulement des chaises | Seulement des tables |
| ------- | --------------------- | -------------------- |
| Découpe | 1 200 ÷ 2 = 600 | 1 200 ÷ 3 = 400 |
| Finition | 700 ÷ 1 = 700 | 700 ÷ 2 = 350 |

1. Chaque segment relie ses deux extrémités : (600 ; 0) à (0 ; 400) pour la découpe, (700 ; 0) à (0 ; 350) pour la finition.
2. Les deux segments se croisent au point E (300 ; 200), celui de la méthode algébrique.
3. La zone des solutions possibles a pour sommets O (0 ; 0), (600 ; 0), E (300 ; 200) et (0 ; 350).

:::

::: piege Lire la zone au-dessus des segments
On colorie la surface au-dessus des deux droites, ou on prend le sommet (700 ; 0). Cela tente parce que le segment de finition va plus loin sur l'axe des chaises. Mais une inéquation « ≤ » désigne les points situés sous le segment, et c'est le segment le plus bas qui limite : 700 chaises dépasseraient la découpe, qui n'en permet que 600.
:::

::: verifie
Un atelier de peinture dispose de 480 h. Un vase y passe 2 h et une assiette 3 h. Quelles sont les deux extrémités de son segment de capacité ?

---

Seulement des vases : 480 ÷ 2 = 240. Seulement des assiettes : 480 ÷ 3 = 160. Extrémités : (240 ; 0) et (0 ; 160).
:::

::: retenir
Une extrémité de segment = capacité ÷ temps unitaire du produit ; la zone des solutions possibles est sous les deux segments, et le plein emploi est à leur intersection.
:::

## 💰 La fonction objectif Z et la quantité optimale

Les deux ateliers pleins, combien rapporte la production de Mahrsia ? Une chaise laisse 40 D de marge bénéficiaire, une table 70 D.
Plusieurs combinaisons sont possibles, mais c'est celle des deux ateliers pleins que le gérant veut chiffrer.

::: definition
La **fonction objectif Z** mesure le résultat à optimiser : maximiser le profit, ou minimiser un coût. Pour un profit :

Z = marge bénéficiaire du produit 1 × quantité optimale du produit 1 + marge bénéficiaire du produit 2 × quantité optimale du produit 2

Dans les situations de ce chapitre, on retient comme quantités optimales celles du point de plein emploi.
:::

::: exemple Calculer Z pour Mahrsia

1. Quantités optimales : C = 300 et T = 200.
2. Z = 40 × 300 + 70 × 200 = 12 000 + 14 000 = 26 000 D par mois.

:::

::: piege Multiplier le prix de vente et non la marge
On calcule 120 × 200 pour les tables. Cela tente parce que le prix de vente est la donnée la plus visible. Mais Z mesure le profit : on multiplie la marge bénéficiaire unitaire (70 D pour une table) par la quantité, non le prix de vente. Si l'énoncé donne la marge en % du prix de vente, on calcule d'abord la marge unitaire : 25 % de 6,400 D = 1,600 D.
:::

::: verifie
Une briqueterie dégage 6 D de marge par brique creuse et 9 D par brique pleine. Le plein emploi donne 500 briques creuses et 300 briques pleines. Que vaut Z ?

---

Z = 6 × 500 + 9 × 300 = 3 000 + 2 700 = 5 700 D.
:::

::: retenir
Z = marge unitaire × quantité optimale, additionnés sur les produits. On utilise la marge, jamais le prix de vente.
:::

## 🤝 La sous-traitance : faire ou faire-faire

Le mois suivant, un hôtel commande 260 tables. Mahrsia n'en fabrique que 200 en plein emploi. Au lieu d'acheter une machine, le gérant peut confier une partie des tables à un autre atelier.
Une machine neuve coûterait cher pour un besoin d'un seul mois, et les 60 tables manquantes ne se fabriquent pas toutes seules.

::: definition
Une entreprise a le choix entre **faire** et **faire-faire**. Lorsqu'elle fait faire, elle **sous-traite** : le **donneur d'ordre** confie la fabrication à une entreprise appelée **sous-traitant**, qui travaille selon ses directives. Ses exigences et les normes à respecter sont fixées dans un **cahier des charges**, qui engage les deux parties. La sous-traitance est un cas particulier de l'**impartition** : déléguer à une autre entreprise une activité que l'on pourrait réaliser soi-même.

Une entreprise sous-traite par exemple quand elle est saturée, quand ses coûts ne sont pas compétitifs, ou quand elle refuse d'acheter un équipement pour une quantité qui dépasse son potentiel productif.
:::

::: exemple La situation de Mahrsia

1. Les ateliers de Mahrsia sont saturés : en plein emploi, ils ne fournissent que 200 tables.
2. Le gérant ne veut pas investir dans une nouvelle machine pour une commande occasionnelle.
3. Mahrsia est donc donneur d'ordre : elle écrit un cahier des charges (dimensions, bois, délai) que le sous-traitant devra respecter.

:::

::: piege Croire que le sous-traitant fixe les règles
On écrit « le sous-traitant choisit comment fabriquer, il est un partenaire à égalité ». Cela tente parce que c'est une autre entreprise, avec ses propres machines. Mais son rôle se limite à exécuter le travail demandé selon les indications du donneur d'ordre, ses exigences et ses normes.
:::

::: verifie
Une conserverie, dont les ateliers sont pleins, confie 5 000 boîtes à une usine voisine, qui les fabrique selon un cahier des charges rédigé par la conserverie. Qui est le donneur d'ordre, qui est le sous-traitant ?

---

La conserverie est le donneur d'ordre : elle fixe les normes. L'usine voisine est le sous-traitant : elle exécute selon le cahier des charges.
:::

::: retenir
Sous-traiter, c'est faire faire : le donneur d'ordre fixe les exigences dans un cahier des charges, le sous-traitant exécute. On y recourt notamment quand l'entreprise est saturée.
:::

## ➖ La quantité à sous-traiter

Mahrsia fabrique 200 tables en plein emploi, et l'hôtel en demande 260. Combien de tables faut-il confier au sous-traitant ?
La réponse commande tout le reste : sans la quantité, on ne peut ni chercher d'offres ni chiffrer un coût.

::: definition
La **quantité à sous-traiter** d'un produit est la demande que l'entreprise doit satisfaire moins la quantité qu'elle peut fabriquer elle-même en plein emploi.

Quantité à sous-traiter = quantité demandée − quantité de plein emploi
:::

::: exemple Les tables de l'hôtel

1. Quantité demandée : 260 tables ; quantité de plein emploi : 200 tables.
2. À sous-traiter : 260 − 200 = 60 tables.
3. L'hôtel ne commande pas de chaises en plus : les 300 chaises de plein emploi couvrent les ventes habituelles, rien à sous-traiter.

:::

::: piege Comparer la demande à la capacité d'un seul atelier
On calcule « 260 tables, la découpe en permet 400, donc rien à sous-traiter ». Cela tente parce que le segment de la découpe est lu seul, sans voir l'autre atelier. Mais la capacité réelle est celle du plein emploi des deux ateliers à la fois, puisque les chaises occupent aussi du temps : ici 200 tables.
:::

::: verifie
Une usine de jouets fabrique 1 120 puzzles en plein emploi. Un distributeur en commande 1 450. Quelle quantité faut-il sous-traiter ?

---

1 450 − 1 120 = 330 puzzles.
:::

::: retenir
Quantité à sous-traiter = demande − quantité de plein emploi. Elle se calcule produit par produit.
:::

## 🔍 Choisir le sous-traitant

Trois ateliers proposent de fabriquer les 60 tables. Mahrsia exige une livraison avant le 20 du mois. Chaque offre indique, par table, la main-d'œuvre directe, les frais de fabrication et le délai.

| Offre | Main-d'œuvre | Frais de fabrication | Coût de fabrication | Livraison |
| ----- | ------------ | -------------------- | ------------------- | --------- |
| Sous-traitant 1 | 14,000 D | 22,500 D | 36,500 D | le 12 |
| Sous-traitant 2 | 13,500 D | 21,000 D | 34,500 D | le 18 |
| Sous-traitant 3 | 12,800 D | 20,400 D | 33,200 D | le 26 |

::: definition
On choisit un sous-traitant en trois temps : d'abord on **élimine** les offres qui ne respectent pas une exigence de l'entreprise, comme le délai de livraison ; puis on **compare le coût de fabrication unitaire** (main-d'œuvre directe + frais de fabrication) des offres restantes ; enfin on applique les autres règles de l'énoncé (par exemple préférer le plus proche si l'écart de prix est faible, ou tenir compte du mode de règlement).
:::

::: exemple Retenir une offre pour Mahrsia

1. Livraison exigée avant le 20 : le sous-traitant 3 (le 26) est éliminé, même s'il est le moins cher.
2. Restent les sous-traitants 1 et 2 : 36,500 D contre 34,500 D par table.
3. Le sous-traitant 2 est le moins cher et respecte le délai : on le retient.

:::

::: piege Retenir le moins cher sans regarder le délai
On écrit « le sous-traitant 3 coûte 33,200 D, c'est le meilleur ». Cela tente parce que la comparaison des prix saute aux yeux. Mais une offre livrée après la date exigée ne sert pas : elle est éliminée avant de comparer les prix.
:::

::: verifie
Un atelier de confection exige une livraison avant le 10. Offres par pièce : A 7,200 D livrée le 8 ; B 6,800 D livrée le 12 ; C 7,500 D livrée le 5. Quelle offre retenir ?

---

B est éliminée (le 12 dépasse le 10). Entre A (7,200 D) et C (7,500 D), on retient A, la moins chère.
:::

::: retenir
Choisir un sous-traitant : éliminer d'abord les offres hors délai, comparer ensuite les coûts unitaires des autres, appliquer enfin les règles de l'énoncé (proximité, règlement).
:::

## 🧾 Le coût de revient de la quantité sous-traitée

Mahrsia fournit elle-même le bois au sous-traitant 2 : 8 kg par table, achetés 3,400 D le kg, avec 0,100 D de frais d'approvisionnement par kg. Chaque table sous-traitée coûte 2,500 D de frais de distribution et se vend 120 D. Le gérant a-t-il intérêt à sous-traiter ?
Le prix payé au sous-traitant ne dit pas tout : le bois fourni et la livraison aux clients pèsent aussi dans le coût.

::: definition
Le **coût de revient de la quantité sous-traitée** rassemble tout ce que le donneur d'ordre paie pour la livrer à ses clients : la matière première qu'il fournit (au coût d'achat, frais d'approvisionnement compris), la main-d'œuvre directe et les frais de fabrication facturés par le sous-traitant, et les frais de distribution. On le compare au prix de vente unitaire.
:::

::: exemple Les 60 tables sous-traitées

1. Matière : 8 kg × (3,400 + 0,100) = 8 × 3,500 = 28,000 D par table, soit 60 × 28,000 = 1 680 D.
2. Main-d'œuvre : 60 × 13,500 = 810 D ; frais de fabrication : 60 × 21,000 = 1 260 D.
3. Frais de distribution : 60 × 2,500 = 150 D.
4. Coût de revient = 1 680 + 810 + 1 260 + 150 = 3 900 D, soit 3 900 ÷ 60 = 65,000 D par table.
5. Prix de vente 120 D, supérieur à 65,000 D : sous-traiter est rentable. Si le coût avait dépassé le prix de vente, on y renoncerait, sauf raison commerciale.

:::

::: piege Oublier la matière fournie par le donneur d'ordre
On additionne seulement 13,500 + 21,000 + 2,500 = 37,000 D, la facture du sous-traitant plus la distribution. Cela tente parce que ces trois lignes figurent dans les offres. Mais la matière fournie par Mahrsia est aussi un coût de la quantité sous-traitée : sans elle, le coût de revient paraît trop faible (37,000 D au lieu de 65,000 D).
:::

::: verifie
Une savonnerie sous-traite 100 cartons. Le sous-traitant facture 6,000 D de main-d'œuvre et 9,000 D de frais par carton ; la savonnerie fournit 4 kg d'huile à 2,500 D le kg (frais d'approvisionnement compris) et paie 1,000 D de distribution par carton. Quel est le coût de revient total ?

---

Par carton : 4 × 2,500 + 6,000 + 9,000 + 1,000 = 26,000 D. Pour 100 cartons : 2 600 D.
:::

::: retenir
Coût de revient de la quantité sous-traitée = matière fournie + main-d'œuvre et frais facturés par le sous-traitant + distribution ; on le compare au prix de vente unitaire.
:::
