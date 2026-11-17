# ⚔️ Le lot économique — combien fabriquer par série

> 💡 «Fabriquer en grande série fait économiser des lancements, mais remplit le magasin : le bon lot est celui où les deux coûts s'équilibrent.»

La Menuiserie Chebbi fabrique des tabourets sur stock. Son chef d'atelier doit décider combien de séries lancer dans l'année, et de quelle taille. Ce chapitre lui donne sept outils : le dilemme des séries, les deux coûts, le coût global, la formule de Wilson, le lot économique avec son rythme, la lecture sur graphique et le pilotage des lots entre un minimum et un maximum de stock.

Les données de la Menuiserie Chebbi, reprises tout au long du chapitre. Les chiffres sont des valeurs choisies pour s'entraîner, pas des données réelles d'une entreprise.

| Donnée                                           | Valeur                    |
| ------------------------------------------------ | ------------------------- |
| Production annuelle régulière (Q)                | 4 800 tabourets           |
| Coût de production unitaire (cu)                 | 25 D                      |
| Coût de lancement d'une série (CL)               | 450 D                     |
| Coût de stockage annuel (t)                      | 12 % de la valeur moyenne |

L'année compte 12 mois. La valeur de la production annuelle est Q × cu = 4 800 × 25 = 120 000 D.

## ⚖️ Pourquoi fabriquer par lots : le dilemme des séries

Un technicien aime les grandes séries : on prépare la machine une fois et on fabrique beaucoup. Mais les tabourets fabriqués d'avance dorment au magasin.
Combien de séries faut-il lancer dans l'année ?

::: definition
Quand une entreprise **fabrique sur stock**, elle produit à l'avance par séries successives appelées **lots**. Le **lot économique** est la quantité à fabriquer par série qui rend le coût global le plus bas.

Deux effets s'opposent :

- plus on lance de séries, plus on paie de lancements ;
- moins on lance de séries, plus chaque lot est grand et plus le stock est gros.
:::

::: exemple Les deux extrêmes de la Menuiserie Chebbi

1. Une seule série de 4 800 tabourets : un seul lancement, 450 D. Mais le stock moyen est de 2 400 tabourets, soit 60 000 D, et le stockage coûte 60 000 × 0,12 = 7 200 D. Total : 7 650 D.
2. Douze séries de 400 tabourets : le stock moyen tombe à 200 tabourets, soit 5 000 D, et le stockage à 600 D. Mais les lancements coûtent 12 × 450 = 5 400 D. Total : 6 000 D.
3. Aucun des deux extrêmes n'est le meilleur : il existe un nombre de séries intermédiaire plus économique.

:::

::: piege Croire qu'un gros lot est toujours rentable
On écrit « une seule série, c'est le plus économique, on ne paie qu'un lancement ». Cela tente parce que le lancement est un frais visible. Mais le stock moyen d'une série unique est énorme : ici le stockage atteint 7 200 D et le total 7 650 D, bien plus que les 6 000 D de douze séries. On ne choisit pas le nombre de séries en regardant un seul des deux coûts.
:::

::: verifie
Un atelier passe de 2 à 8 séries par an pour la même production. Que deviennent son coût de lancement annuel et la taille de ses lots ?

---

Le coût de lancement annuel augmente, car il y a davantage de lancements à payer. Chaque lot devient plus petit : la production est partagée entre 8 séries au lieu de 2, donc le stock moyen, lui, baisse.
:::

::: retenir
Peu de séries : peu de lancements mais un gros stock ; beaucoup de séries : un petit stock mais beaucoup de lancements.
:::

## 💰 Le coût de lancement et le coût de stockage

Pour comparer les séries, il faut chiffrer chacun des deux coûts.
Que contient chacun, et comment varie-t-il ?

::: definition
- Le **coût de lancement** CL est le coût engagé à chaque série : établissement des documents, temps de mise en route, réglage des machines, approvisionnement. Il vaut CL par lot, quelle que soit la taille du lot.
- Le **coût de stockage** (ou de possession) est le coût de détention des produits fabriqués. Il s'exprime par un taux t en pourcentage de la valeur du stock moyen ; on utilise le **taux de possession** i = t ÷ 100.
- Quand la production est régulière et répartie en N lots égaux, le stock passe d'un lot entier à zéro : le **stock moyen** est la moitié d'un lot, **SM = Q ÷ (2 × N)**, et sa valeur est Q × cu ÷ (2 × N).

Hypothèses du modèle : la production annuelle Q est connue avec certitude, elle est régulièrement répartie sur l'année et le taux de stockage est constant.
:::

::: exemple Les coûts de la Menuiserie Chebbi avec 4 séries

1. Chaque lot compte 4 800 ÷ 4 = 1 200 tabourets.
2. Stock moyen : 4 800 ÷ (2 × 4) = 600 tabourets, soit une valeur de 600 × 25 = 15 000 D.
3. Taux de possession : i = 12 ÷ 100 = 0,12. Coût de stockage = 15 000 × 0,12 = 1 800 D.
4. Coût de lancement = 450 × 4 = 1 800 D.

:::

::: piege Prendre le lot entier comme stock moyen
On écrit « le stock moyen, c'est un lot : 1 200 tabourets ». Cela tente parce que le lot est ce qu'on voit arriver au magasin. Mais le stock ne reste pas au niveau d'un lot : il diminue jusqu'à zéro avant la série suivante. Le stock moyen vaut la moitié du lot, 600 tabourets : le stockage serait doublé à tort si l'on prenait 1 200.
:::

::: verifie
Un atelier fabrique 2 400 pièces par an en 3 lots réguliers, à 20 D la pièce, avec un stockage à 10 %. Quelle est la valeur de son stock moyen et le coût de stockage ?

---

Stock moyen = 2 400 ÷ 6 = 400 pièces, soit 400 × 20 = 8 000 D. Coût de stockage = 8 000 × 0,10 = 800 D.
:::

::: retenir
Lancement : CL par série ; stock moyen : Q ÷ (2 × N) ; stockage : taux i = t ÷ 100 sur la valeur du stock moyen.
:::

## 🧮 Le coût global : lancement plus stockage

Il reste à additionner les deux coûts pour savoir ce que coûte une politique de N séries.
Comment écrire ce total en fonction de N ?

::: definition
Le **coût global** CG est la somme du coût de stockage annuel et du coût de lancement annuel :

CG = Q × cu × i ÷ (2 × N) + CL × N

Le premier terme baisse quand N augmente, le second monte.
:::

::: exemple Le tableau de la Menuiserie Chebbi

Ici Q × cu × i = 4 800 × 25 × 0,12 = 14 400, donc CG = 7 200 ÷ N + 450 × N.

| N | Stockage   | Lancement | Coût global |
| - | ---------- | --------- | ----------- |
| 1 | 7 200 D    | 450 D     | 7 650 D     |
| 2 | 3 600 D    | 900 D     | 4 500 D     |
| 3 | 2 400 D    | 1 350 D   | 3 750 D     |
| 4 | 1 800 D    | 1 800 D   | 3 600 D     |
| 5 | 1 440 D    | 2 250 D   | 3 690 D     |
| 6 | 1 200 D    | 2 700 D   | 3 900 D     |
| 7 | 1 028,57 D | 3 150 D   | 4 178,57 D  |

1. Le stockage baisse à chaque ligne, le lancement monte de 450 D à chaque ligne.
2. Le coût global baisse jusqu'à N = 4, puis remonte : le minimum, 3 600 D, correspond à 4 séries.

:::

::: piege Ajouter le coût de production au coût global
On écrit « CG = 120 000 + 7 200 ÷ N + 450 × N ». Cela tente parce que fabriquer coûte de l'argent. Mais Q × cu = 120 000 D est dépensé quel que soit le nombre de séries : il ne change pas avec N et ne sert pas à choisir. Dans la formule, cu sert seulement à valoriser le stock moyen.
:::

::: verifie
Un atelier fabrique 2 000 pièces par an à 15 D, avec un stockage à 10 % et 120 D par lancement. Quel est son coût global avec 5 séries ?

---

Stockage = 2 000 × 15 × 0,10 ÷ 10 = 300 D. Lancement = 5 × 120 = 600 D. Coût global = 300 + 600 = 900 D.
:::

::: retenir
CG = Q × cu × i ÷ (2 × N) + CL × N : le stockage baisse avec N, le lancement monte avec N.
:::

## 📐 La formule de Wilson : le nombre optimal de lots

Le tableau est long à construire, et on peut s'arrêter à côté du minimum.
Existe-t-il un calcul direct du N qui rend CG minimal ?

Ce modèle est le même qu'au chapitre de la gestion prévisionnelle des stocks : seuls les noms changent.

| Achats (gestion des stocks) | Fabrication (ce chapitre)    |
| --------------------------- | ---------------------------- |
| commande                    | lancement d'une série        |
| coût de passation p         | coût de lancement CL         |
| prix d'achat × quantité     | Q × cu                       |
| coût de possession          | coût de stockage             |

::: definition
Le **nombre optimal de lots** N* est le nombre de séries qui rend le coût global minimal. On l'obtient en annulant la dérivée de CG par rapport à N :

CG'(N) = − Q × cu × i ÷ (2 × N²) + CL = 0, donc N² = Q × cu × i ÷ (2 × CL).

C'est la **formule de Wilson** appliquée à la fabrication :

N* = √(Q × cu × i ÷ (2 × CL))
:::

::: exemple Wilson pour la Menuiserie Chebbi

1. Q × cu × i = 4 800 × 25 × 0,12 = 14 400.
2. 2 × CL = 2 × 450 = 900.
3. 14 400 ÷ 900 = 16, donc N* = √16 = 4 séries — le même résultat que le tableau.

:::

::: piege Oublier le coût unitaire dans la formule
On écrit « N* = √(4 800 × 0,12 ÷ 900) = √0,64 = 0,8 série ». Cela tente parce que 4 800 est le chiffre de la production. Mais la formule compare des dinars : il faut la valeur Q × cu = 120 000 D. Avec la quantité seule, on trouve moins d'une série, ce qui n'a aucun sens.
:::

::: propriete
- À N*, le coût de stockage égale le coût de lancement : ici 1 800 D et 1 800 D, pour un coût global minimal de 3 600 D.
- Plus CL est élevé, plus N* est petit : on groupe la production en séries plus grosses.
- Le prix de vente n'intervient pas : seuls Q, cu, i et CL comptent.
- cu et Q figurent au numérateur : un coût unitaire plus élevé ou une production plus grande augmente N*.
- Q peut se déduire des besoins : quantité par produit × nombre de produits, additionnée sur tous les produits fabriqués.
- Cas limite : si Q est multiplié par 4, N* est multiplié par 2 seulement, car N* est une racine.
- La formule vaut tant que les hypothèses tiennent : production régulière, Q connue, taux constant.
- Si N* n'est pas entier, on compare le coût global des deux entiers qui l'encadrent et on retient le moins cher.
:::

::: verifie
Un atelier fabrique 3 200 pièces par an à 10 D, avec un stockage à 20 % et 32 D par lancement. Quel est son nombre optimal de lots ?

---

Q × cu × i = 3 200 × 10 × 0,20 = 6 400 ; 2 × CL = 64 ; 6 400 ÷ 64 = 100, donc N* = √100 = 10 lots.
:::

::: retenir
N* = √(Q × cu × i ÷ (2 × CL)), avec i = t ÷ 100 : à l'optimum, stockage et lancement s'égalisent.
:::

## 📅 Le lot économique et le rythme des lancements

La Menuiserie Chebbi sait qu'il faut 4 séries par an.
Combien de tabourets par série, et à quel rythme ?

::: definition
Quand la production annuelle est régulière, on fabrique des lots égaux à intervalles réguliers. Avec N* lots :

- le **lot économique** est q* = Q ÷ N* ;
- les lancements ont lieu **tous les 12 ÷ N* mois**.
:::

::: exemple Le rythme de la Menuiserie Chebbi

1. q* = 4 800 ÷ 4 = 1 200 tabourets par série.
2. Intervalle = 12 ÷ 4 = 3 mois.
3. La menuiserie lance une série de 1 200 tabourets tous les 3 mois.
4. Contrôle : 4 × 1 200 = 4 800 tabourets, toute la production de l'année.

:::

::: piege Inverser le rapport pour l'intervalle
On écrit « intervalle = 4 ÷ 12 = 0,33 mois ». Cela tente parce qu'on divise deux nombres déjà utilisés. Mais l'année compte 12 mois à répartir entre N* lancements : on divise 12 par N*. Plus N* est grand, plus l'intervalle est court.
:::

::: propriete
- Le lot et l'intervalle se calculent tous deux à partir de N*.
- L'intervalle en jours vaut 360 ÷ N* ou 365 ÷ N*, selon la durée d'année que l'énoncé impose.
- Cas limite : avec N* = 5, l'intervalle vaut 2,4 mois, qui n'est pas un nombre entier de mois.
:::

::: verifie
Une entreprise fabrique 3 600 unités par an et son nombre optimal de lots est de 6. Quel est son lot économique et tous les combien de mois lance-t-elle une série ?

---

q* = 3 600 ÷ 6 = 600 unités. Intervalle = 12 ÷ 6 = 2 mois : une série de 600 unités tous les 2 mois.
:::

::: retenir
q* = Q ÷ N* en unités, et un lancement tous les 12 ÷ N* mois.
:::

## 📈 La lecture graphique : retrouver N* en dessinant

Une formule donne le résultat, un graphique le montre.
Comment retrouver N* avec une courbe ?

::: definition
On porte le nombre de lots N en abscisse et les coûts en dinars en ordonnée. On trace la droite du coût de lancement CL × N, la courbe décroissante du coût de stockage et la courbe en U du coût global. Le nombre optimal N* est l'**abscisse du point où se coupent lancement et stockage** ; le coût global minimal est le double de l'ordonnée de ce point.
:::

::: figure Les trois courbes de la Menuiserie Chebbi : la droite du lancement, la courbe du stockage qui descend et le coût global en U
<svg viewBox="0 0 360 200"><path d="M50 170 L345 170" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M345 170 l-6 -3 l0 6 z" fill="#0f172a"/><path d="M50 175 L50 10" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M50 10 l-3 6 l6 0 z" fill="#0f172a"/><path d="M50.0 170.0 L54.0 169.1 L58.0 168.3 L62.0 167.4 L66.0 166.6 L70.0 165.7 L74.0 164.9 L78.0 164.0 L82.0 163.2 L86.0 162.3 L90.0 161.4 L94.0 160.6 L98.0 159.7 L102.0 158.9 L106.0 158.0 L110.0 157.2 L114.0 156.3 L118.0 155.5 L122.0 154.6 L126.0 153.8 L130.0 152.9 L134.0 152.0 L138.0 151.2 L142.0 150.3 L146.0 149.5 L150.0 148.6 L154.0 147.8 L158.0 146.9 L162.0 146.1 L166.0 145.2 L170.0 144.3 L174.0 143.5 L178.0 142.6 L182.0 141.8 L186.0 140.9 L190.0 140.1 L194.0 139.2 L198.0 138.4 L202.0 137.5 L206.0 136.7 L210.0 135.8 L214.0 134.9 L218.0 134.1 L222.0 133.2 L226.0 132.4 L230.0 131.5 L234.0 130.7 L238.0 129.8 L242.0 129.0 L246.0 128.1 L250.0 127.3 L254.0 126.4 L258.0 125.5 L262.0 124.7 L266.0 123.8 L270.0 123.0 L274.0 122.1 L278.0 121.3 L282.0 120.4 L286.0 119.6 L290.0 118.7 L294.0 117.8 L298.0 117.0 L302.0 116.1 L306.0 115.3 L310.0 114.4 L314.0 113.6 L318.0 112.7 L322.0 111.9 L326.0 111.0 L330.0 110.2" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="5 3"/><path d="M90.0 33.2 L94.0 45.6 L98.0 56.0 L102.0 64.8 L106.0 72.3 L110.0 78.8 L114.0 84.5 L118.0 89.5 L122.0 94.0 L126.0 98.0 L130.0 101.6 L134.0 104.9 L138.0 107.8 L142.0 110.5 L146.0 113.0 L150.0 115.3 L154.0 117.4 L158.0 119.3 L162.0 121.1 L166.0 122.8 L170.0 124.4 L174.0 125.9 L178.0 127.3 L182.0 128.5 L186.0 129.8 L190.0 130.9 L194.0 132.0 L198.0 133.0 L202.0 134.0 L206.0 134.9 L210.0 135.8 L214.0 136.6 L218.0 137.4 L222.0 138.2 L226.0 138.9 L230.0 139.6 L234.0 140.3 L238.0 140.9 L242.0 141.5 L246.0 142.1 L250.0 142.6 L254.0 143.2 L258.0 143.7 L262.0 144.2 L266.0 144.7 L270.0 145.1 L274.0 145.6 L278.0 146.0 L282.0 146.4 L286.0 146.8 L290.0 147.2 L294.0 147.6 L298.0 147.9 L302.0 148.3 L306.0 148.6 L310.0 149.0 L314.0 149.3 L318.0 149.6 L322.0 149.9 L326.0 150.2 L330.0 150.5" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="2 3"/><path d="M90.0 24.7 L94.0 36.2 L98.0 45.7 L102.0 53.7 L106.0 60.3 L110.0 66.0 L114.0 70.8 L118.0 75.0 L122.0 78.6 L126.0 81.8 L130.0 84.5 L134.0 86.9 L138.0 89.0 L142.0 90.9 L146.0 92.5 L150.0 93.9 L154.0 95.2 L158.0 96.2 L162.0 97.2 L166.0 98.0 L170.0 98.8 L174.0 99.4 L178.0 99.9 L182.0 100.3 L186.0 100.7 L190.0 101.0 L194.0 101.2 L198.0 101.4 L202.0 101.5 L206.0 101.6 L210.0 101.6 L214.0 101.6 L218.0 101.5 L222.0 101.4 L226.0 101.3 L230.0 101.1 L234.0 100.9 L238.0 100.7 L242.0 100.5 L246.0 100.2 L250.0 99.9 L254.0 99.6 L258.0 99.2 L262.0 98.9 L266.0 98.5 L270.0 98.1 L274.0 97.7 L278.0 97.3 L282.0 96.8 L286.0 96.4 L290.0 95.9 L294.0 95.4 L298.0 94.9 L302.0 94.4 L306.0 93.9 L310.0 93.4 L314.0 92.8 L318.0 92.3 L322.0 91.7 L326.0 91.2 L330.0 90.6" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linejoin="round"/><path d="M210 170 L210 135.8" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><circle cx="210" cy="135.8" r="4" fill="#0f172a"/><circle cx="210" cy="101.6" r="4" fill="#0f6e56"/><text x="90" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="130" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="170" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><text x="210" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><text x="250" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><text x="290" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="330" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7</text><text x="345" y="185" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N</text><text x="44" y="174.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="44" y="98.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4 000</text><text x="44" y="22.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8 000</text><text x="218" y="151.8" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(4 ; 1 800)</text><text x="218" y="93.60000000000001" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(4 ; 3 600)</text><text x="130" y="27.200000000000017" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">stockage</text><text x="280" y="134.7" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">lancement</text><text x="264" y="85.89" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">coût global</text></svg>
:::

La figure reprend le tableau : la courbe verte en U est la colonne « Coût global », dont le creux de 3 600 D se trouve à N = 4, là où la droite du lancement coupe la courbe du stockage à 1 800 D.

::: exemple Le graphique de la Menuiserie Chebbi

1. À N = 2, le stockage vaut 3 600 D et le lancement 900 D : à gauche de N*, le stockage domine.
2. À N = 7, le lancement vaut 3 150 D et le stockage 1 028,57 D : à droite de N*, le lancement domine.
3. À N = 4, les deux valent 1 800 D : les courbes se coupent, donc N* = 4.
4. Le coût global minimal est 1 800 + 1 800 = 3 600 D.

:::

::: piege Lire l'ordonnée du point d'intersection comme le coût global minimal
On écrit « le coût global minimal est 1 800 D, la valeur du croisement ». Cela tente parce que c'est le point que l'on regarde. Mais cette ordonnée est celle d'un seul des deux coûts. Le coût global est leur somme : 1 800 + 1 800 = 3 600 D.
:::

::: verifie
Sur un graphique, les courbes de lancement et de stockage se coupent au point d'abscisse 5 et d'ordonnée 2 000 D. Que valent N* et le coût global minimal ?

---

N* est l'abscisse du point d'intersection : N* = 5 lots. À ce point, lancement et stockage valent chacun 2 000 D, donc le coût global minimal est 2 000 + 2 000 = 4 000 D.
:::

::: retenir
N* se lit en abscisse au croisement du lancement et du stockage ; le coût global minimal est la somme des deux ordonnées.
:::

## 🏭 Piloter les lots entre un minimum et un maximum de stock

Le chef d'atelier doit aussi décider, trimestre après trimestre, combien de lots lancer pour ne jamais manquer de produits ni encombrer le magasin.
Comment calculer le nombre de lots à lancer ?

::: definition
Le responsable fixe un **stock minimum** (en dessous, risque de rupture) et un **stock maximum** (au-dessus, surstockage). L'état du stock à la fin d'un trimestre est :

stock final = stock au début + production − commandes livrées.

On lance le plus petit nombre entier de lots qui place le stock final entre le minimum et le maximum.
:::

::: exemple Les lots d'un atelier de jouets

Un atelier fabrique par lots de 40 articles. Stock de départ : 100 ; minimum : 60 ; maximum : 160. Commandes : 120, 70 puis 150 articles.

1. Trimestre 1 : 100 + P − 120 ≥ 60 donne P ≥ 80, soit 2 lots ; stock final : 60.
2. Trimestre 2 : 60 + P − 70 ≥ 60 donne P ≥ 70, soit 1,75 lot, donc 2 lots (80 articles) ; stock final : 70.
3. Trimestre 3 : 70 + P − 150 ≥ 60 donne P ≥ 140, soit 3,5 lots, donc 4 lots (160 articles) ; stock final : 80.

Les stocks finaux 60, 70 et 80 restent entre 60 et 160.
:::

::: piege Arrondir le nombre de lots vers le bas
On écrit « 70 articles à produire, soit 1,75 lot, donc 1 lot ». Cela tente parce qu'on arrondit souvent au plus proche. Mais un seul lot donne 40 articles : le stock final tomberait à 60 + 40 − 70 = 30, sous le minimum. Un lot se lance en entier, donc on arrondit au nombre entier supérieur.
:::

::: propriete
- Si le stock de départ moins les commandes est déjà au moins égal au minimum, aucun lot n'est nécessaire.
- Il faut aussi contrôler que le stock final ne dépasse pas le maximum.
:::

::: verifie
Un atelier fabrique par lots de 30 articles. Il débute avec 80 articles, doit finir avec au moins 50 et livre 130 articles. Combien de lots lance-t-il ?

---

80 + P − 130 ≥ 50 donne P ≥ 100, soit 3,33 lots : 4 lots (120 articles). Stock final : 80 + 120 − 130 = 70. Trois lots donneraient 40, sous le minimum.
:::

::: retenir
Stock final = début + production − commandes ; on lance le plus petit nombre entier de lots qui atteint le minimum sans dépasser le maximum.
:::
