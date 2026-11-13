# ⚔️ La gestion comptable des stocks — le registre du gardien du magasin

> 💡 «Un stock a deux visages : des quantités que l'on compte, et une valeur que l'on doit choisir.»

La Huilerie Zied revend des bidons d'huile. Ce chapitre suit ses entrées et ses sorties du mois de mars et apprend à répondre à une seule question : **combien vaut ce qui sort du magasin, et combien vaut ce qui reste ?** Sept outils : le coût d'achat, la fiche de stock, le coût moyen pondéré de fin de période, le coût moyen pondéré après chaque entrée, le premier entré premier sorti (PEPS), le dernier entré premier sorti (DEPS), puis l'effet du choix de méthode sur le résultat.

Les mouvements de mars de la Huilerie Zied, sur l'article « bidon d'huile 5 L » :

| Date  | Mouvement                      | Quantité | Coût unitaire |
| ----- | ------------------------------ | -------- | ------------- |
| 01/03 | Stock initial                  | 300      | 20 D          |
| 04/03 | Sortie (bon de sortie n° 1)    | 100      |               |
| 10/03 | Entrée (bon d'entrée n° 1)     | 300      | 24 D          |
| 15/03 | Sortie (bon de sortie n° 2)    | 300      |               |
| 22/03 | Entrée (bon d'entrée n° 2)     | 200      | 28 D          |
| 28/03 | Sortie (bon de sortie n° 3)    | 250      |               |

Les coûts unitaires de ce tableau sont des coûts d'achat ; les sections suivantes reprennent ce même tableau pour valoriser les sorties.

## 💰 Le coût d'achat : à quel prix un lot entre-t-il en stock ?

Le 10/03, la Huilerie Zied reçoit 300 bidons. La facture du fournisseur indique 6 600 D. Le transporteur a été payé 450 D, et l'équipe du magasin a passé une matinée à réceptionner le lot, ce qui représente 150 D de coût de réception.
À quelle valeur enregistrer ces 300 bidons dans la fiche de stock ?

::: definition
Le **coût d'achat** est la valeur à laquelle une entrée est enregistrée en stock. Il réunit le **prix d'achat**, les **frais externes** (transport, emballages non récupérables) et les **frais internes** (manutention, réception, énergie, loyers du magasin). Un produit fabriqué par l'entreprise entre en stock à son **coût de production** : coût d'achat des matières consommées plus charges de fabrication.
:::

::: exemple Le lot du 10/03

1. Prix d'achat facturé : 6 600 D — c'est la base.
2. Frais externes : le transport, 450 D — l'entreprise le paie pour que le lot arrive (le transport vers les clients n'en fait pas partie : c'est un frais de vente).
3. Frais internes : la réception, 150 D — du travail fait par l'entreprise elle-même.
4. Coût d'achat = 6 600 + 450 + 150 = 7 200 D, soit 7 200 ÷ 300 = 24 D par bidon : c'est le coût unitaire de la fiche.

:::

::: piege Enregistrer le prix de la facture seul
On écrit « 6 600 ÷ 300 = 22 D le bidon », puisque c'est le prix du fournisseur. Cela tente parce que le chiffre est sous les yeux. Mais le lot a coûté aussi 450 D de transport et 150 D de réception : le coût unitaire à retenir est 24 D, et non 22 D.
:::

::: verifie
Une quincaillerie reçoit 50 pots de peinture : facture 900 D, transport 60 D, réception par son personnel 40 D. Quel est le coût d'achat unitaire ?

---

Coût d'achat du lot : 900 + 60 + 40 = 1 000 D (prix d'achat, frais externes, frais internes). Coût unitaire : 1 000 ÷ 50 = 20 D par pot.
:::

::: retenir
Une entrée se valorise au coût d'achat : prix d'achat plus frais externes plus frais internes.
:::

## 📋 La fiche de stock : suivre les quantités, puis les valeurs

Reprenons le tableau de la Huilerie Zied. Le gardien du magasin doit pouvoir dire, après chaque mouvement, combien de bidons restent. Et le comptable veut une valeur à chaque fois.
Où le gardien note-t-il tout cela ?

::: definition
La **fiche de stock** suit un article ligne par ligne. Chaque ligne a trois blocs : **entrées** (bon d'entrée, BE, ou bon de réception, BR), **sorties** (bon de sortie, BS) et **stock existant**. Chacun donne une quantité, un coût unitaire (C.U) et un montant. La première ligne est le **stock initial**, aussi appelé stock à nouveau.
:::

::: exemple Les quantités de mars

1. Départ : 300 bidons.
2. Sortie du 04/03 : 300 − 100 = 200 bidons.
3. Entrée du 10/03 : 200 + 300 = 500 bidons.
4. Sorties et entrée suivantes : 500 − 300 = 200, puis 200 + 200 = 400, puis 400 − 250 = 150 bidons.
5. Contrôle : stock final = 300 + (300 + 200) − (100 + 300 + 250) = 150 bidons — le même résultat.

:::

::: piege Oublier le stock initial dans le contrôle
On écrit « 500 entrés − 650 sortis = −150 ». Cela tente parce que le stock initial ne figure pas parmi les « mouvements ». Mais un stock ne peut pas être négatif : il manque les 300 bidons du départ, car le stock initial s'ajoute aux entrées dans le contrôle. Avec lui, on trouve 150.
:::

::: propriete
Le contrôle vaut en quantités comme en valeurs :

- stock final = stock initial + entrées − sorties ;
- la fiche doit donner ce même résultat que la dernière ligne du stock existant ;
- les quatre méthodes qui suivent valorisent les sorties, donc le stock final ; chacune vérifie cette égalité en valeur.

Cas limite : un mois sans aucune entrée donne un stock final égal au stock initial moins les sorties.
:::

::: verifie
Une fiche débute avec 120 unités. Il entre 80 puis 60 unités, et il sort 150 unités dans le mois. Combien en reste-t-il ?

---

Stock final = 120 + (80 + 60) − 150 = 260 − 150 = 110 unités. Le stock initial est compté avec les entrées, les 150 sortis sont retirés une seule fois.
:::

::: retenir
La fiche de stock suit quantités et valeurs ; stock final = stock initial + entrées − sorties, en quantités comme en valeurs.
:::

## 🧮 Le CUMP de fin de période : un seul coût pour toutes les sorties

Le 04/03, le gardien sort 100 bidons. Mais le comptable ne sait pas encore à quel prix, puisque d'autres lots vont arriver avant la fin du mois.
Peut-on donner à toutes les sorties du mois un même coût, représentatif de tout ce que la Huilerie a eu en main ?

::: definition
Le **coût unitaire moyen pondéré de fin de période** (CUMP de fin de période) se calcule une seule fois, à la clôture, en cumulant le stock initial et toutes les entrées de la période. Toutes les sorties du mois sont ensuite valorisées à ce coût.
:::

$$ CUMP = (Stock initial + Entrées) en valeur ÷ (Stock initial + Entrées) en quantité $$

::: exemple Le CUMP de la Huilerie Zied

1. Valeur cumulée : 6 000 + 7 200 + 5 600 = 18 800 D — le stock initial est inclus.
2. Quantité cumulée : 300 + 300 + 200 = 800 bidons.
3. CUMP = 18 800 ÷ 800 = 23,5 D.
4. Sorties : 100 + 300 + 250 = 650 bidons, valorisés 650 × 23,5 = 15 275 D.
5. Stock final : 150 × 23,5 = 3 525 D. Contrôle : 18 800 − 15 275 = 3 525 D.

:::

::: piege Faire la moyenne simple des trois prix
On écrit « (20 + 24 + 28) ÷ 3 = 24 D ». Cela tente parce que les trois prix sont sur la fiche. Mais les lots n'ont pas la même taille : le lot à 20 D en compte 300, celui à 28 D seulement 200. La moyenne doit être pondérée par les quantités : 23,5 D, et non 24 D.
:::

::: propriete
Le CUMP de fin de période a deux traits :

- il lisse les variations de prix : un seul coût pour tout le mois ;
- il ne peut être calculé qu'à la clôture, donc il retarde la valorisation des sorties ; il faut attendre la dernière entrée ;
- si les prix changent durablement, la valeur du stock s'écarte des prix du moment.

Cas limite : sans aucune entrée dans le mois, le CUMP est le coût unitaire du stock initial.
:::

::: verifie
Un article démarre le mois avec 100 unités à 10 D. Il entre 300 unités à 12 D, et il sort 250 unités. Quel est le CUMP, la valeur des sorties et celle du stock final ?

---

Valeur cumulée : 100 × 10 + 300 × 12 = 1 000 + 3 600 = 4 600 D, pour 400 unités. CUMP = 4 600 ÷ 400 = 11,5 D. Sorties : 250 × 11,5 = 2 875 D. Stock final : 150 × 11,5 = 1 725 D ; contrôle : 4 600 − 2 875 = 1 725 D.
:::

::: retenir
Le CUMP de fin de période divise la valeur cumulée par la quantité cumulée, stock initial inclus ; toutes les sorties du mois en héritent.
:::

## 🔄 Le CUMP après chaque entrée : un coût remis à jour à chaque arrivage

Le comptable de la Huilerie veut connaître la valeur du stock le 18/03, sans attendre fin mars.
Peut-on recalculer un coût moyen dès qu'un lot arrive ?

::: definition
Le **CUMP après chaque entrée** est recalculé à chaque entrée, à partir du stock existant à cet instant. Entre deux entrées, les sorties sont valorisées au dernier CUMP calculé, et elles ne le modifient pas.
:::

$$ CUMP après entrée = Stock en valeur après l'entrée ÷ Stock en quantité après l'entrée $$

| Date  | Mouvement | Quantité | Coût unitaire | Valeur sortie ou entrée | Stock existant : quantité, coût unitaire, valeur |
| ----- | --------- | -------- | ------------- | ------------------- | ------------------------------------------------ |
| 01/03 | Stock initial |       |               |                     | 300 ; 20 ; 6 000                                  |
| 04/03 | Sortie    | 100      | 20            | 2 000               | 200 ; 20 ; 4 000                                  |
| 10/03 | Entrée    | 300      | 24            | 7 200               | 500 ; 22,4 ; 11 200                               |
| 15/03 | Sortie    | 300      | 22,4          | 6 720               | 200 ; 22,4 ; 4 480                                |
| 22/03 | Entrée    | 200      | 28            | 5 600               | 400 ; 25,2 ; 10 080                               |
| 28/03 | Sortie    | 250      | 25,2          | 6 300               | 150 ; 25,2 ; 3 780                                |

::: exemple Le nouveau coût du 10/03

1. Avant l'entrée, le stock existant vaut 200 bidons à 20 D : 4 000 D.
2. L'entrée ajoute 300 bidons à 24 D : 7 200 D. Après elle, le stock vaut 4 000 + 7 200 = 11 200 D pour 500 bidons.
3. Nouveau CUMP : 11 200 ÷ 500 = 22,4 D. Ce coût sert pour la sortie du 15/03, soit 300 × 22,4 = 6 720 D.
4. Au total, les sorties valent 2 000 + 6 720 + 6 300 = 15 020 D, et le stock final 150 × 25,2 = 3 780 D. Contrôle : 6 000 + 7 200 + 5 600 − 15 020 = 3 780 D.

:::

::: piege Cumuler le stock initial sans retirer les sorties déjà faites
Le 10/03, on écrit « (6 000 + 7 200) ÷ (300 + 300) = 22 D ». Cela tente parce que c'est la formule de fin de période. Mais 100 bidons sont déjà partis à 20 D : le stock existant ne vaut plus 6 000 D mais 4 000 D. Le bon calcul donne 22,4 D, et non 22 D.
:::

::: propriete
Avec la méthode après chaque entrée :

- le coût est connu à tout moment, sans attendre la clôture ;
- seule une entrée change le coût ; une sortie le laisse intact et retire simplement des unités à ce coût ;
- le calcul est plus lourd, puisqu'il faut le refaire à chaque entrée.

Cas limite : si une entrée arrive alors que le stock est vide, le nouveau coût est le coût de l'entrée.
:::

::: verifie
Une fiche affiche 100 unités à 10 D. Une entrée de 100 unités à 14 D arrive, puis une sortie de 50 unités, puis une entrée de 150 unités à 16 D. Quel est le CUMP après la dernière entrée ?

---

Après la première entrée : (1 000 + 1 400) ÷ 200 = 12 D. La sortie de 50 unités à 12 D laisse 150 unités à 12 D : 1 800 D. La dernière entrée ajoute 150 × 16 = 2 400 D : 1 800 + 2 400 = 4 200 D pour 300 unités. CUMP = 4 200 ÷ 300 = 14 D.
:::

::: retenir
Après chaque entrée, le nouveau coût est la valeur du stock existant divisée par sa quantité ; les sorties se valorisent au dernier coût calculé.
:::

## 📦 Le PEPS : les premiers arrivés sont les premiers servis

Dans une crémerie, on vend d'abord le lot le plus ancien, pour que rien ne périme.
Pour la Huilerie Zied, cela suggère une autre manière de valoriser : à quel prix sort une quantité qui vient de plusieurs lots ?

::: definition
Le **PEPS** (premier entré, premier sorti, ou FIFO, aussi appelé méthode d'épuisement des lots anciens) valorise les sorties au coût des entrées les plus anciennes, lot après lot, jusqu'à épuisement. Le stock restant est donc valorisé aux coûts des entrées les plus récentes. Il convient aux produits périssables.
:::

::: methode Valoriser une sortie en PEPS

1. Repérer le lot le plus ancien encore en stock.
2. En prélever la quantité demandée, sans dépasser ce que le lot contient.
3. Si la sortie n'est pas couverte, passer au lot suivant, plus récent.
4. Valoriser chaque prélèvement à son propre coût unitaire, puis additionner.

Cas limite : si un seul lot suffit, la sortie est valorisée à son coût, sans mélange.
:::

| Date  | Mouvement | Prélèvement                | Valeur de la sortie | Stock existant après    |
| ----- | --------- | -------------------------- | ------------------- | ----------------------- |
| 04/03 | Sortie 100 | 100 × 20                  | 2 000               | 200 à 20                |
| 10/03 | Entrée 300 à 24 |                      |                     | 200 à 20 ; 300 à 24     |
| 15/03 | Sortie 300 | 200 × 20 + 100 × 24       | 4 000 + 2 400 = 6 400 | 200 à 24              |
| 22/03 | Entrée 200 à 28 |                      |                     | 200 à 24 ; 200 à 28     |
| 28/03 | Sortie 250 | 200 × 24 + 50 × 28        | 4 800 + 1 400 = 6 200 | 150 à 28              |

::: exemple La sortie du 15/03

1. Le lot le plus ancien est celui de 200 bidons à 20 D : on le vide en premier, soit 200 × 20 = 4 000 D.
2. Il manque encore 100 bidons : on passe au lot suivant, à 24 D, soit 100 × 24 = 2 400 D.
3. La sortie vaut 4 000 + 2 400 = 6 400 D ; il reste 200 bidons à 24 D.
4. Au total, les sorties valent 2 000 + 6 400 + 6 200 = 14 600 D, et le stock final 150 × 28 = 4 200 D. Contrôle : 18 800 − 14 600 = 4 200 D.

:::

::: piege Valoriser toute la sortie au prix du premier lot
Pour la sortie du 15/03, on écrit « 300 × 20 = 6 000 D ». Cela tente parce que le lot à 20 D est le plus ancien. Mais ce lot ne contient que 200 bidons : les 100 suivants viennent du lot à 24 D. La sortie vaut 6 400 D, et non 6 000 D.
:::

::: verifie
Le stock contient 120 unités à 15 D (lot ancien) puis 80 unités à 18 D (lot récent). Une sortie de 150 unités est servie en PEPS. Quelle est sa valeur ?

---

Le lot ancien est vidé en premier : 120 × 15 = 1 800 D. Il reste 30 unités à prélever sur le lot récent : 30 × 18 = 540 D. La sortie vaut 1 800 + 540 = 2 340 D.
:::

::: retenir
En PEPS, les sorties partent aux coûts les plus anciens et le stock restant garde les coûts les plus récents.
:::

## 🔃 Le DEPS : les derniers arrivés sont les premiers servis

Imaginons que le gardien prenne toujours le bidon posé en haut de la pile, c'est-à-dire le dernier arrivé.
À quel prix sortent alors les bidons de la Huilerie Zied ?

::: definition
Le **DEPS** (dernier entré, premier sorti, ou LIFO) valorise les sorties au coût des entrées les plus récentes. Le stock restant est valorisé aux coûts des entrées les plus anciennes. Le système comptable le déconseille : il peut gonfler les coûts.
:::

| Date  | Mouvement | Prélèvement               | Valeur de la sortie | Stock existant après    |
| ----- | --------- | ------------------------- | ------------------- | ----------------------- |
| 04/03 | Sortie 100 | 100 × 20                 | 2 000               | 200 à 20                |
| 10/03 | Entrée 300 à 24 |                     |                     | 200 à 20 ; 300 à 24     |
| 15/03 | Sortie 300 | 300 × 24                 | 7 200               | 200 à 20                |
| 22/03 | Entrée 200 à 28 |                     |                     | 200 à 20 ; 200 à 28     |
| 28/03 | Sortie 250 | 200 × 28 + 50 × 20       | 5 600 + 1 000 = 6 600 | 150 à 20              |

::: exemple La sortie du 28/03

1. Le lot le plus récent est celui de 200 bidons à 28 D : on le vide en premier, soit 200 × 28 = 5 600 D.
2. Il manque 50 bidons : on remonte au lot précédent, à 20 D, soit 50 × 20 = 1 000 D.
3. La sortie vaut 5 600 + 1 000 = 6 600 D ; il reste 150 bidons à 20 D.
4. Au total, les sorties valent 2 000 + 7 200 + 6 600 = 15 800 D, et le stock final 150 × 20 = 3 000 D. Contrôle : 18 800 − 15 800 = 3 000 D.

:::

::: piege Valoriser le stock restant aux prix récents
On écrit « il reste 150 bidons, donc 150 × 28 = 4 200 D ». Cela tente parce que les derniers lots sont les plus visibles. Mais en DEPS ce sont justement les derniers lots qui sortent en premier : le stock restant garde les coûts les plus anciens, 150 × 20 = 3 000 D. Les 4 200 D sont la valeur obtenue en PEPS.
:::

::: propriete
Le DEPS inverse le PEPS :

- les sorties sont valorisées aux coûts les plus récents, le stock restant aux plus anciens ;
- on prélève d'abord sur le lot le plus récent, puis sur le lot précédent, et ainsi de suite ;
- le contrôle reste le même : stock initial plus entrées moins sorties.

Cas limite : si une seule entrée suffit à couvrir une sortie, elle est valorisée à ce seul coût.
:::

::: verifie
Un stock contient 100 unités à 10 D, puis une entrée de 100 unités à 12 D. Une sortie de 130 unités est servie en DEPS. Quelle est sa valeur ?

---

Le lot le plus récent part en premier : 100 × 12 = 1 200 D. Il reste 30 unités à prélever sur le lot précédent : 30 × 10 = 300 D. La sortie vaut 1 200 + 300 = 1 500 D.
:::

::: retenir
En DEPS, les sorties partent aux coûts les plus récents et le stock restant garde les coûts les plus anciens.
:::

## ⚖️ Choisir sa méthode : l'effet sur le résultat

La Huilerie Zied a vendu 650 bidons à 30 D l'un, soit 19 500 D de ventes. Le directeur a calculé la valeur des sorties de quatre façons.
Le résultat de mars change-t-il selon la méthode retenue ?

::: definition
La **marge commerciale** est la différence entre le prix de vente et le coût de ce qui est vendu. Le coût des sorties dépend de la méthode de valorisation : changer de méthode change la marge, donc le **résultat**, sans que la réalité de l'activité change.
:::

| Méthode              | Valeur des sorties | Stock final | Marge sur 19 500 D de ventes |
| -------------------- | ------------------ | ----------- | ---------------------------- |
| PEPS                 | 14 600             | 4 200       | 4 900                        |
| CUMP après entrée    | 15 020             | 3 780       | 4 480                        |
| CUMP fin de période  | 15 275             | 3 525       | 4 225                        |
| DEPS                 | 15 800             | 3 000       | 3 700                        |

::: exemple Lire le tableau de la Huilerie

1. Les prix d'achat montent de 20 D à 28 D : c'est une période de hausse.
2. PEPS sort les bidons aux coûts les plus bas : sorties 14 600 D, et marge 19 500 − 14 600 = 4 900 D.
3. DEPS les sort aux coûts les plus hauts : sorties 15 800 D, et marge 19 500 − 15 800 = 3 700 D.
4. L'écart de marge entre les deux méthodes est 4 900 − 3 700 = 1 200 D, soit l'écart de valeur des sorties. Ici, les prix montant régulièrement, les CUMP se placent entre les deux.

:::

::: piege Inverser le sens de l'effet
On écrit « en hausse des prix, le PEPS minore le résultat ». Cela tente parce que le PEPS sort les lots les plus anciens, donc « les plus vieux », comme si cela coûtait plus cher. Mais en hausse, les lots anciens sont les moins chers : les sorties valent moins, le stock restant vaut plus, et le résultat est majoré. Le DEPS fait l'inverse.
:::

::: propriete
L'effet dépend de l'évolution des prix d'achat :

- prix stables : les méthodes donnent les mêmes valeurs ;
- hausse des prix : le PEPS valorise les sorties aux coûts les plus bas, le stock aux plus hauts, et le résultat est majoré ; le DEPS fait l'inverse ;
- baisse des prix : le PEPS valorise les sorties aux coûts les plus hauts, le résultat est minoré ; le DEPS fait l'inverse ;
- le CUMP compense les variations : c'est le procédé le plus souvent utilisé, et la référence du système comptable.

Cas limite : si le stock initial et toutes les entrées ont le même coût unitaire, les quatre méthodes donnent le même résultat.
:::

::: verifie
Les prix baissent : un stock de 100 unités à 30 D reçoit 100 unités à 25 D, puis 100 unités sont vendues 40 D l'une. Quelle méthode, du PEPS ou du DEPS, donne la marge la plus forte, et de combien ?

---

En PEPS, la sortie part au plus ancien, 100 × 30 = 3 000 D : marge 4 000 − 3 000 = 1 000 D. En DEPS, elle part au plus récent, 100 × 25 = 2 500 D : marge 4 000 − 2 500 = 1 500 D. Le DEPS donne la marge la plus forte, de 500 D de plus : en baisse de prix, c'est lui qui sort les lots les moins chers.
:::

::: retenir
En hausse des prix, le PEPS majore le résultat et le DEPS le minore ; en baisse, c'est l'inverse ; le CUMP lisse les variations.
:::
