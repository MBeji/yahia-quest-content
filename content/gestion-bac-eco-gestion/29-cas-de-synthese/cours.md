# 🎓 Les cas de synthèse — un dossier, plusieurs outils

> 💡 « Un cas de synthèse n'apprend rien de nouveau : il demande de choisir, à chaque question, le bon outil parmi ceux que tu connais déjà. »

Le sujet du jour s'appelle « Cartonnerie Ayari » : trois pages d'énoncé, des annexes à remplir, une dizaine de questions qui parlent de production, de coûts, de ventes, d'investissement et de trésorerie. Par où commencer ? Ce chapitre ne contient aucune formule nouvelle. Il donne huit repères : la méthode pour aborder un cas, puis sept familles de questions qui reviennent presque toujours, chacune avec un renvoi au chapitre où l'outil a été appris (chapitres 08 à 28).

Les entreprises et les chiffres de ce chapitre sont des valeurs choisies pour s'entraîner, pas des données réelles. Les montants sont en dinars (D), les décimales s'écrivent avec une virgule, et les grands nombres se lisent par tranches de trois chiffres.

## 🧭 Aborder un cas : lire, découper, choisir l'outil

Un cas de synthèse mélange plusieurs dossiers : chacun est un petit problème indépendant. Si tu calcules avant d'avoir tout lu, tu risques d'utiliser le mauvais chiffre ou de passer à côté d'une donnée donnée plus loin.
Comment reconnaître l'outil que chaque question attend ?

::: definition
Un **cas de synthèse** est un énoncé à plusieurs dossiers, chacun faisant appel à un ou plusieurs chapitres du manuel. La méthode tient en cinq temps :

1. **Lire** tout l'énoncé et les annexes, sans calculer ;
2. **Relever** les données de chaque dossier avec leur unité et leur régime de taxe (hors taxe ou toutes taxes comprises) ;
3. **Associer** chaque question à un outil, grâce au mot-clé de la question ;
4. **Calculer** en notant chaque résultat intermédiaire, car il resservira ;
5. **Commenter** : un chiffre n'est pas une réponse tant qu'on ne dit pas ce qu'il signifie pour l'entreprise.

| La question parle de… | L'outil | Chapitre |
| --- | --- | --- |
| quantités qui occupent entièrement les ateliers | système de plein emploi | 10 |
| coût de production, coût de revient | coûts complets | 08 |
| écart entre prévu et réel | contrôle des coûts | 11 |
| marge sur coût variable, résultat différentiel | coûts partiels | 09 |
| part de marché, taux de croissance | étude de marché, ventes | 13 |
| VAN, capacité d'autofinancement | choix d'investissement | 21 |
| emprunt, annuité, coût d'un financement | mode de financement | 22 |
| encaissements, décaissements, trésorerie | plan et budgets | 28 |

Règle de taxe, en général : les calculs d'exploitation et d'investissement (coûts, marges, coût initial d'un projet) se font **hors taxe** ; un budget de trésorerie se construit **toutes taxes comprises**, puisque c'est la somme réellement payée ou reçue.
:::

::: exemple Découper un énoncé de la Cartonnerie Ayari
Valeurs d'illustration : l'énoncé contient cinq phrases de consigne.

1. « Quelles quantités occupent à plein les deux ateliers ? » : mot-clé « à plein », c'est le plein emploi (chapitre 10).
2. « Que constatez-vous entre le coût prévu et le coût réel ? » : mot-clé « prévu et réel », ce sont les écarts (chapitre 11).
3. « Quelle machine retenir selon la VAN ? » : mot-clé VAN, chapitre 21, avec des montants hors taxe.
4. « Établissez la trésorerie du trimestre » : mot-clé trésorerie, chapitre 28, avec des montants toutes taxes comprises.
5. Chaque réponse sera notée à part : un résultat faux au dossier 1 ne doit pas contaminer le dossier 3.
:::

::: piege Se lancer dans les calculs dès la première ligne
On remplit la première annexe avec les premiers chiffres rencontrés. Cela tente parce que commencer donne l'impression d'avancer. Mais une donnée utile (un taux de TVA, une capacité réduite par une panne) se trouve souvent plus bas dans l'énoncé : un cas se **lit en entier**, puis se découpe.
:::

::: verifie
Une question demande : « Quel emprunt coûte le moins cher à l'entreprise ? » Quel chapitre faut-il rouvrir, et avec quelles données de départ ?

---

Le chapitre 22 sur le choix du mode de financement : on repère les montants empruntés, les taux, les durées et le taux d'actualisation donnés par l'énoncé avant de calculer les coûts.
:::

::: retenir
Cinq temps : lire, relever les données (unité, hors taxe ou TTC), associer chaque question à un outil, calculer en gardant les résultats intermédiaires, commenter.
:::

## 🏭 Production : le plein emploi des ateliers

Dans la Cartonnerie Ayari, deux ateliers travaillent pour deux produits. Une panne vient de réduire la capacité d'un atelier.
Combien d'unités de chaque produit peut-on encore fabriquer ?

::: definition
Quand l'énoncé parle de **plein emploi** (renvoi au chapitre 10), chaque atelier donne une égalité : temps unitaire × quantité, additionnés sur les deux produits, égalent la capacité de l'atelier. On obtient deux équations à deux inconnues, résolues par substitution.

$$ tA1 × x + tA2 × y = capacité de l'atelier A $$
$$ tB1 × x + tB2 × y = capacité de l'atelier B $$

tA1 est le temps unitaire du produit 1 dans l'atelier A, x et y les quantités des deux produits. La marge totale obtenue au plein emploi est la fonction objectif Z = marge bénéficiaire unitaire 1 × x + marge bénéficiaire unitaire 2 × y (chapitre 10).

Trois points d'attention : tous les temps dans la **même unité** que la capacité (minutes converties en heures) ; une capacité réduite de 20 % vaut 80 % de la capacité normale ; on **contrôle** les quantités trouvées dans les deux égalités.
:::

::: exemple Les deux ateliers de la menuiserie Hamdi
Valeurs d'illustration : chaise = 2 h en atelier A et 1 h en atelier B ; table = 1 h en A et 2 h en B. Capacités normales : A 800 h, B 700 h. Une panne ramène chaque atelier à 80 % de sa capacité.

1. Capacités réduites : A = 800 × 0,8 = 640 h ; B = 700 × 0,8 = 560 h.
2. Équations : 2x + y = 640 et x + 2y = 560 (x chaises, y tables).
3. De la première : y = 640 − 2x. Dans la seconde : x + 1 280 − 4x = 560, donc 3x = 720 et x = 240.
4. Alors y = 640 − 480 = 160.
5. Contrôle : 2 × 240 + 160 = 640 ✓ ; 240 + 2 × 160 = 560 ✓. On fabrique 240 chaises et 160 tables.
:::

::: piege Oublier de convertir les minutes ou la panne
On écrit « 30 mn » dans une équation dont la capacité est en heures, ou on garde la capacité normale après une panne. Cela tente parce que l'énoncé donne les chiffres dans cet ordre. Mais l'égalité n'a de sens que dans **une seule unité** et avec la capacité réellement disponible.
:::

::: verifie
Un atelier dispose de 450 h ; chaque lot de seau demande 30 mn et chaque lot de bassine 1 h, et il fabrique 300 lots de seaux. Combien de lots de bassines reste-t-il à plein emploi, si tout le temps de l'atelier sert ?

---

Seaux : 300 × 0,5 = 150 h. Il reste 450 − 150 = 300 h, soit 300 lots de bassines à 1 h chacun.
:::

::: retenir
Plein emploi : une égalité par atelier, temps unitaire × quantité = capacité, dans la même unité ; capacité réduite = capacité × pourcentage restant ; contrôler dans les deux égalités.
:::

## 💰 Coûts : prévu, réel et écarts

La Cartonnerie Ayari a calculé ce que devait coûter une nouvelle caisse. Le mois suivant, elle a constaté un autre coût.
Où l'entreprise a-t-elle gagné ou perdu, et combien reste-t-il sur une commande ?

::: definition
Deux outils s'enchaînent (chapitres 08 et 11).

**Coûts** : le **coût de production** unitaire additionne matières, main-d'œuvre directe et autres charges de fabrication ; le **coût de revient** unitaire y ajoute les frais de distribution (souvent un pourcentage du prix de vente). Le résultat sur une commande est :

$$ résultat = quantité × (prix de vente unitaire − coût de revient unitaire) $$

**Écarts** : toujours **coût réel − coût préétabli**, un écart positif sur une charge est défavorable. Pour un élément :

$$ écart sur coût = (coût unitaire réel − coût unitaire préétabli) × quantité réelle $$
$$ écart sur quantité = (quantité réelle − quantité préétablie) × coût unitaire préétabli $$

La somme des deux donne l'écart global ; le premier signale un problème de prix, le second un problème de consommation.
:::

::: exemple Le pot de miel de l'atelier Bouzid
Valeurs d'illustration : prix de vente 8 D. Prévu par pot : 0,5 kg de miel à 6 D le kg ; emballage 0,400 D ; 0,25 h de main-d'œuvre à 8 D l'heure ; distribution 5 % du prix. Réel : 0,55 kg de miel à 6,40 D le kg ; emballage 0,400 D ; 0,25 h à 8,40 D l'heure.

1. Prévu : miel 3,000 ; emballage 0,400 ; main-d'œuvre 2,000 ; coût de production 5,400 D ; distribution 0,400 ; coût de revient 5,800 D.
2. Réel : miel 0,55 × 6,40 = 3,520 ; emballage 0,400 ; main-d'œuvre 2,100 ; coût de production 6,020 D ; coût de revient 6,420 D.
3. Écart global par pot : 6,420 − 5,800 = +0,620 D, défavorable.
4. Sur le miel : écart sur coût (6,40 − 6) × 0,55 = +0,220 ; écart sur quantité (0,55 − 0,5) × 6 = +0,300 ; total +0,520 D, soit 3,520 − 3,000 ✓.
5. Commande de 2 000 pots : 2 000 × (8 − 6,420) = 3 160 D de résultat.
:::

::: piege Inverser le sens de l'écart ou changer de base
On calcule « prévu − réel » et on conclut qu'un écart négatif est mauvais. Cela tente parce que « prévu » se lit en premier. Mais la règle du manuel est **réel − préétabli** : un écart positif sur une charge est défavorable. De même, l'écart sur quantité se chiffre au coût **préétabli**, l'écart sur coût à la quantité **réelle**.
:::

::: verifie
Un coût préétabli est de 40 D par unité et le coût réel de 43 D ; la quantité réelle est de 500 unités. Quel est l'écart global, et est-il favorable ?

---

(43 − 40) × 500 = +1 500 D : l'écart est positif, donc défavorable.
:::

::: retenir
Coût de revient = coût de production + distribution ; résultat de la commande = quantité × (prix − coût de revient). Écart = réel − préétabli ; écart sur coût à la quantité réelle, écart sur quantité au coût préétabli.
:::

## 📈 Marché : parts de marché et croissance

La direction veut savoir si ses ventes progressent plus vite que celles de ses concurrents.
Comment le mesurer sur plusieurs années ?

::: definition
La **part de marché** d'une année est le chiffre d'affaires de l'entreprise divisé par celui de tout le secteur (entreprise comprise), exprimé en pourcentage (renvoi au chapitre 13).

$$ part de marché = CA de l'entreprise ÷ CA du secteur × 100 $$

Le **taux de croissance** compare une année à la précédente :

$$ taux de croissance = (CA de l'année − CA de l'année précédente) × 100 ÷ CA de l'année précédente $$

Pour prévoir une année, on applique le taux : CA prévu = CA de l'année × (1 + taux). Un taux « supérieur de 5 points » s'ajoute au taux précédent (20 % devient 25 %). Si les ventes progressent moins vite que le secteur, la part de marché baisse ; au même rythme, elle reste stable. Le manuel écrit « supérieur de 5 % » : on le lit comme 5 points de pourcentage.
:::

::: exemple Les trois années de la maison Dhaouadi
Valeurs d'illustration : CA de l'entreprise 900 000, 1 080 000 puis 1 296 000 D ; CA du secteur 6 000 000, 6 750 000 puis 7 200 000 D.

1. Parts de marché : 900 000 ÷ 6 000 000 = 15 % ; 1 080 000 ÷ 6 750 000 = 16 % ; 1 296 000 ÷ 7 200 000 = 18 %.
2. Croissance de la 2e année : (1 080 000 − 900 000) × 100 ÷ 900 000 = 20 % ; de la 3e année : (1 296 000 − 1 080 000) × 100 ÷ 1 080 000 = 20 %.
3. Si l'entreprise vise 5 points de plus (25 %) l'année suivante : 1 296 000 × 1,25 = 1 620 000 D.
4. La part monte chaque année : les ventes (+20 %) progressent plus vite que le secteur (+12,5 % puis +6,7 %).
:::

::: piege Diviser par la mauvaise année
On calcule la croissance en divisant l'augmentation par le chiffre d'affaires de l'année en cours. Cela tente parce que c'est le chiffre le plus récent. Mais la base d'une croissance est l'année **précédente**. De même, on oublie parfois que le CA du secteur contient celui de l'entreprise.
:::

::: verifie
Un fabricant passe de 400 000 à 460 000 D de ventes. Quel est son taux de croissance ?

---

(460 000 − 400 000) × 100 ÷ 400 000 = 15 %.
:::

::: retenir
Part de marché = CA entreprise ÷ CA secteur ; croissance = augmentation ÷ année précédente ; CA prévu = CA × (1 + taux) ; ventes moins rapides que le secteur : part en baisse.
:::

## ⚖️ Rentabilité : marge sur coût variable et choix entre deux hypothèses

L'entreprise hésite entre baisser un prix et lancer une campagne de publicité.
Comment trancher sans se fier à l'intuition ?

::: definition
Avec les coûts partiels (chapitre 09), la **marge sur coût variable** unitaire est :

$$ marge unitaire = prix de vente − coût variable unitaire $$

Le **résultat d'exploitation** est la marge totale (marge unitaire × quantité, additionnée sur les produits) moins les charges fixes.

Pour savoir quel produit est le plus rentable, on compare le **taux de marge sur coût variable** (TMCV = marge sur coût variable ÷ chiffre d'affaires × 100), pas la marge unitaire seule. Pour choisir entre deux hypothèses, on refait le calcul du résultat pour chacune, nouveau prix et nouvelle quantité compris, et l'on ajoute au fixe tout coût de publicité ; on retient le **résultat le plus élevé**.
:::

::: exemple Baisser le prix ou faire de la publicité chez Mrad
Valeurs d'illustration : un seul article, prix 30 D, coût variable 24 D, 8 000 unités, charges fixes 36 000 D.

1. Situation actuelle : marge unitaire 6 D, TMCV 20 % ; marge totale 48 000 D ; résultat 48 000 − 36 000 = 12 000 D.
2. Hypothèse A, prix baissé de 5 % : prix 28,5 D, marge unitaire 4,5 D ; avec 11 000 unités, marge 49 500 D, résultat 13 500 D.
3. Hypothèse B, publicité de 10 000 D : prix inchangé, marge 6 D ; avec 9 500 unités, marge 57 000 D ; fixes 46 000 D, résultat 11 000 D.
4. On retient l'hypothèse A : 13 500 D contre 11 000 D et 12 000 D aujourd'hui.
:::

::: piege Comparer les marges unitaires au lieu des taux de marge sur coût variable
On dit « le produit de 6 D de marge est plus rentable que celui de 5 D ». Cela tente parce que 6 est plus grand que 5. Mais un produit à 5 D de marge sur un prix de 24 D (20,8 %) rapporte plus par dinar vendu qu'un produit à 6 D sur 30 D (20 %). On compare des **taux de marge sur coût variable**.
:::

::: verifie
Un produit se vend 50 D pour un coût variable de 38 D. Quel est son taux de marge sur coût variable ?

---

Marge unitaire 50 − 38 = 12 D ; taux = 12 ÷ 50 = 24 %.
:::

::: retenir
Marge unitaire = prix − coût variable ; résultat = marge totale − charges fixes ; rentabilité comparée par le taux de marge sur coût variable ; entre deux hypothèses, résultat le plus élevé, publicité ajoutée au fixe.
:::

## 🏗️ Investissement : capacité d'autofinancement et VAN

Pour remplacer une vieille machine, la Cartonnerie Ayari étudie un équipement neuf.
Le projet vaut-il son prix une fois les gains ramenés à aujourd'hui ?

::: definition
Avec le choix d'investissement (chapitre 21), le **coût initial** est le prix d'acquisition plus les frais d'installation, hors taxe. On calcule la capacité d'autofinancement (CAF) annuelle :

$$ résultat avant impôt = CA − charges décaissables − dotation $$
$$ CAF = résultat avant impôt × (1 − taux d'impôt) + dotation $$

La dotation linéaire vaut coût initial ÷ durée de vie ; elle est ajoutée car elle ne sort pas de caisse. Si la CAF est constante :

$$ VAN = CAF × [1 − (1 + i)⁻ⁿ] ÷ i − coût initial $$

Une VAN positive signale un projet rentable ; une VAN nulle signifie que le projet rapporte exactement le taux d'actualisation, sans gain supplémentaire ; entre deux projets, on retient la **VAN la plus élevée**. Dans les énoncés, le facteur [1 − (1 + i)⁻ⁿ] ÷ i est souvent donné.
:::

::: exemple La machine neuve de la Cartonnerie Ayari
Valeurs d'illustration : prix 400 000 D et installation 50 000 D hors taxe ; durée 5 ans ; CA 700 000 D par an ; charges décaissables 480 000 D ; impôt 30 % ; taux 9 % ; facteur d'actualisation sur 5 ans à 9 % : 3,8897.

1. Coût initial : 400 000 + 50 000 = 450 000 D ; dotation : 450 000 ÷ 5 = 90 000 D.
2. Résultat avant impôt : 700 000 − 480 000 − 90 000 = 130 000 D ; impôt 39 000 D ; résultat net 91 000 D.
3. CAF : 91 000 + 90 000 = 181 000 D.
4. VAN : 181 000 × 3,8897 − 450 000 = 704 035,7 − 450 000 ≈ 254 036 D, donc projet rentable.
:::

::: piege Oublier d'ajouter la dotation à la fin
On prend le résultat net comme flux annuel. Cela tente parce que « net » ressemble à ce qui reste. Mais la dotation est une charge **sans décaissement** : elle réduit l'impôt, et on la remet dans le flux. De même, le coût initial se prend hors taxe.
:::

::: verifie
Un projet de 200 000 D hors taxe sur 4 ans rapporte une CAF de 60 000 D par an ; le facteur d'actualisation sur 4 ans est 3,24. Quelle est la VAN, et le projet est-il rentable ?

---

60 000 × 3,24 − 200 000 = 194 400 − 200 000 = −5 600 D : VAN négative, projet non rentable.
:::

::: retenir
CAF = résultat avant impôt × (1 − taux) + dotation ; VAN = CAF × facteur − coût initial hors taxe ; VAN > 0 rentable ; entre deux projets, VAN la plus élevée.
:::

## 🏦 Financement : l'emprunt et son tableau d'amortissement

Pour payer l'équipement, la Cartonnerie Ayari emprunte une partie de la somme.
Combien paiera-t-elle chaque année, et que devient la dette ?

::: definition
Le **montant de l'emprunt** est ce qui reste à financer une fois retirées les autres sources prévues par l'énoncé (augmentation de capital, fonds propres qui paient la TVA de l'investissement…). Si la TVA est payée sur fonds propres, l'emprunt couvre le coût hors taxe moins les apports (renvoi au chapitre 22). Chaque année : intérêt = capital restant dû × taux ; amortissement = annuité − intérêt ; capital restant dû final = capital restant dû initial − amortissement (Vp = Vp-1 − Ap).

- **Annuités constantes** : même annuité chaque année,

$$ a = C × i ÷ [1 − (1 + i)⁻ⁿ] $$

- **Amortissements constants** : amortissement = C ÷ n chaque année ; les intérêts, et donc les annuités, diminuent.

Deux emprunts se comparent par la valeur actuelle de ce qu'ils font décaisser, pas par la simple somme des intérêts.
:::

::: exemple L'emprunt de 240 000 D
Valeurs d'illustration : 240 000 D sur 4 ans à 8 %, remboursement à la fin de chaque année.

1. Annuités constantes : a = 240 000 × 0,08 ÷ (1 − 1,08⁻⁴) = 19 200 ÷ 0,26497 ≈ 72 461,0 D.
2. Année 1 : intérêt 240 000 × 0,08 = 19 200 D ; amortissement 72 461,0 − 19 200 = 53 261,0 D ; capital restant dû 186 739,0 D.
3. Année 2 : intérêt 186 739,0 × 0,08 ≈ 14 939,1 D ; amortissement ≈ 57 521,9 D.
4. Amortissements constants : 240 000 ÷ 4 = 60 000 D par an ; intérêt de la 1re année 19 200 D, de la 2e (240 000 − 60 000) × 0,08 = 14 400 D.
:::

::: piege Appliquer le taux au capital initial chaque année
On calcule l'intérêt de la 2e année avec 240 000 D comme en année 1. Cela tente parce que le taux est le même. Mais l'intérêt se calcule sur le capital **restant dû**, qui a déjà baissé de l'amortissement de la 1re année.
:::

::: verifie
Un emprunt de 90 000 D sur 3 ans à 10 % est remboursé par amortissements constants. Quel est l'intérêt de la 2e année ?

---

Amortissement : 90 000 ÷ 3 = 30 000 D. Capital restant dû en début d'année 2 : 60 000 D ; intérêt : 6 000 D.
:::

::: retenir
Intérêt = capital restant dû × taux ; amortissement = annuité − intérêt ; annuités constantes : formule a ; amortissements constants : C ÷ n ; comparer les emprunts par leur valeur actuelle.
:::

## 🧾 Trésorerie : TVA, encaissements, décaissements et commentaire

La Cartonnerie Ayari veut savoir si, avec l'achat de sa machine, elle aura assez d'argent en caisse chaque mois.
Comment le prévoir, et que conseiller si le solde devient négatif ?

::: definition
Le **budget de trésorerie** (chapitre 28) se construit mois par mois, en montants toutes taxes comprises.

- **TVA** : TVA = prix TTC × 18 ÷ 118 ou prix hors taxe × 0,18. TVA à décaisser = TVA collectée (sur les ventes) − TVA déductible (sur les achats) − crédit de TVA antérieur. La TVA déductible porte sur les achats, les charges et les investissements ; si elle dépasse la TVA collectée, l'écart est un crédit de TVA à reporter sur le mois suivant.
- **Encaissements** : chaque vente TTC se répartit selon les délais (comptant, à 30 jours, à 60 jours).
- **Décaissements** : chaque achat et chaque charge de la même manière, plus la TVA du mois précédent, les salaires et les investissements.
- **Solde du mois** = encaissements − décaissements ; **trésorerie finale** = trésorerie initiale + solde.

Un solde négatif se **commente** puis se corrige : obtenir un délai plus long des fournisseurs, escompter des effets, demander un découvert, étaler le paiement d'un investissement.
:::

::: exemple Le premier trimestre de la Cartonnerie Ayari
Valeurs d'illustration : ventes hors taxe : décembre 18 000, janvier 20 000, février 22 000, mars 21 000 D (TVA 18 %), encaissées 40 % comptant et 60 % à 30 jours. Achats hors taxe : 9 000, 10 000, 12 000, 11 000 D, payés à 30 jours. Salaires 5 000 D par mois, charges diverses 1 500 D sans TVA, achat d'une machine de 18 000 D TTC payé comptant en février, TVA payée le mois suivant, trésorerie initiale 6 000 D.

1. Ventes TTC : 21 240 ; 23 600 ; 25 960 ; 24 780 D. Encaissements : janvier 0,4 × 23 600 + 0,6 × 21 240 = 22 184 D ; février 10 384 + 14 160 = 24 544 D ; mars 9 912 + 15 576 = 25 488 D.
2. Achats TTC : 10 620 ; 11 800 ; 14 160 ; 12 980 D. TVA de la machine : 18 000 × 18 ÷ 118 ≈ 2 745,76 D. TVA à décaisser : décembre 3 240 − 1 620 = 1 620 D (versée en janvier) ; janvier 3 600 − 1 800 = 1 800 D (versée en février) ; février 3 960 − 2 160 − 2 745,76 = −945,76 D : crédit de TVA à reporter, rien à verser en mars.
3. Décaissements : janvier 10 620 + 5 000 + 1 500 + 1 620 = 18 740 D ; février 11 800 + 5 000 + 1 500 + 1 800 + 18 000 = 38 100 D ; mars 14 160 + 5 000 + 1 500 = 20 660 D.
4. Soldes : +3 444 ; −13 556 ; +4 828 D. Trésorerie finale : 9 444 ; −4 112 ; +716 D.
5. Commentaire : trésorerie négative en février, à cause de la machine payée comptant ; le crédit de TVA allège mars. Conseils : étaler son paiement, négocier le délai fournisseurs, escompter des effets.
:::

::: piege Mettre des montants hors taxe dans le budget
On encaisse 20 000 D en janvier parce que c'est le chiffre d'affaires hors taxe. Cela tente parce que l'énoncé donne ce montant en premier. Mais le client paie la TVA avec le prix : l'encaissement se calcule sur le **TTC**, et la TVA collectée sera reversée à l'État le mois suivant.
:::

::: verifie
Une entreprise a ventes TTC de 11 800 D, dont elle encaisse 50 % comptant et 50 % le mois suivant. Quelle est la TVA incluse dans ces ventes, et quel montant encaisse-t-elle le mois même ?

---

TVA = 11 800 × 18 ÷ 118 = 1 800 D. Elle encaisse 50 % × 11 800 = 5 900 D le mois même.
:::

::: retenir
Budget en TTC ; TVA = TTC × 18 ÷ 118 ; TVA à décaisser = collectée − déductible − crédit ; solde = encaissements − décaissements ; trésorerie finale = initiale + solde ; solde négatif : commenter et proposer des solutions.
:::

> 🏆 Tu sais maintenant aborder un cas entier : lire, découper, choisir l'outil de chaque question, calculer sans te tromper de taxe et conclure par un conseil.
