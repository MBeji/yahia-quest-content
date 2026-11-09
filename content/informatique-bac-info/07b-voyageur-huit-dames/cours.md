# ⚔️ Le voyageur de commerce, les huit dames et le retour sur trace — optimiser et explorer

> 💡 «Quand la meilleure route est trop longue à chercher, on suit une règle simple ; quand la règle ne suffit pas, on explore, et on sait revenir en arrière.»

Dernier palier du programme : deux problèmes difficiles, résolus en Pascal avec des tableaux et de la récursivité (chapitre 2). Le voyageur de commerce se règle par une stratégie gloutonne, puis par d'autres approches ; les huit dames s'attaquent par le retour sur trace. Huit notions, avec deux fils rouges : un circuit de cinq villes, puis un échiquier.

## 🗺️ Le voyageur de commerce et la ville la plus proche

Un livreur doit passer une seule fois par cinq villes, puis rentrer à son point de départ, en roulant le moins possible. Les distances entre villes, en km, sont données dans un tableau (distances fictives).
Quelle règle simple lui permet de construire un itinéraire ?

::: definition
Le **problème du voyageur de commerce** consiste à visiter n villes, une et une seule fois chacune, puis à revenir à la ville de départ, en minimisant la distance totale (ou le temps, ou le coût). Le trajet obtenu s'appelle un **circuit**.
La **stratégie de la ville la plus proche** : à chaque étape, aller à la ville **non visitée** la plus proche de la **ville en cours**. C'est une stratégie **gloutonne** : on prend la meilleure décision du moment et on ne la remet jamais en cause.
:::

| Distance | 1   | 2   | 3   | 4   | 5   |
| -------- | --- | --- | --- | --- | --- |
| 1        | 0   | 27  | 13  | 14  | 9   |
| 2        | 27  | 0   | 31  | 26  | 20  |
| 3        | 13  | 31  | 0   | 6   | 19  |
| 4        | 14  | 26  | 6   | 0   | 18  |
| 5        | 9   | 20  | 19  | 18  | 0   |

::: exemple Suivre la stratégie depuis la ville 1

1. Ville en cours 1 ; non visitées 2, 3, 4, 5 à 27, 13, 14 et 9 : on va en 5, car 9 est la plus petite distance depuis la ville en cours.
2. Ville en cours 5 ; non visitées 2, 3, 4 à 20, 19 et 18 : on va en 4.
3. Ville en cours 4 ; non visitées 2 et 3 à 26 et 6 : on va en 3.
4. Ville en cours 3 ; il ne reste que la ville 2, à 31 : on y va, sans autre choix possible.
5. Tout est visité : retour de 2 à 1, soit 27. Longueur : 9 + 18 + 6 + 31 + 27 = 91 ✓.

:::

::: figure Le circuit 1 → 5 → 4 → 3 → 2 puis retour en 1 : chaque flèche porte sa distance (9, 18, 6, 31, 27), soit 91 en tout ; schéma non à l'échelle
<svg viewBox="0 0 400 240">
<title>Trajet 1, 5, 4, 3, 2 puis retour en 1 ; les cinq segments mesurent 9, 18, 6, 31 et 27</title>
<line x1="215" y1="45" x2="315" y2="93" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="315,93 305,93 308,85" fill="#0f172a"/>
<text x="274" y="64" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">9</text>
<line x1="323" y1="116" x2="292" y2="184" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="292,184 292,174 300,178" fill="#0f172a"/>
<text x="320" y="156" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">18</text>
<line x1="268" y1="200" x2="132" y2="200" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="132,200 141,196 141,204" fill="#0f172a"/>
<text x="200" y="217" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">6</text>
<line x1="108" y1="184" x2="77" y2="116" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="77,116 85,122 77,126" fill="#0f172a"/>
<text x="80" y="156" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">31</text>
<line x1="85" y1="93" x2="185" y2="45" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="185,45 178,53 175,45" fill="#0f172a"/>
<text x="126" y="64" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">27</text>
<circle cx="200" cy="38" r="17" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/>
<text x="200" y="43" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">1</text>
<circle cx="330" cy="100" r="17" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="330" y="105" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">5</text>
<circle cx="285" cy="200" r="17" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="285" y="205" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">4</text>
<circle cx="115" cy="200" r="17" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="115" y="205" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">3</text>
<circle cx="70" cy="100" r="17" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="70" y="105" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">2</text>
</svg>
:::

Dans la figure, la dernière flèche (2 vers 1, longueur 27) est le retour au départ : elle fait partie du circuit.

::: piege
**Erreur : croire que la ville la plus proche à chaque étape donne le circuit le plus court.** On trouve 91 et on conclut « c'est le minimum ». L'erreur tente parce que chaque choix est le meilleur sur le moment. Mais ces choix imposent la fin du circuit : la ville 2, laissée pour la fin, coûte 31 puis 27. Le circuit 1, 3, 4, 2, 5 puis retour en 1 mesure 13 + 6 + 26 + 20 + 9 = 74, soit 17 de moins.
:::

::: propriete
La stratégie de la ville la plus proche construit toujours un circuit valable en n − 1 choix, mais **sans garantie de minimum**.
Cas limite : le résultat dépend de la ville de départ. Depuis la ville 4, la même règle donne 4, 3, 1, 5, 2 puis retour en 4 : 6 + 13 + 9 + 20 + 26 = 74.
:::

::: verifie À toi : appliquer la règle
Quatre villes : d(1, 2) = 8, d(1, 3) = 15, d(1, 4) = 6, d(2, 3) = 10, d(2, 4) = 13, d(3, 4) = 11. Appliquer la stratégie depuis la ville 2 : quel trajet, et quelle longueur retour compris ?

---

Depuis 2, les distances aux villes 1, 3, 4 sont 8, 10 et 13 : on va en 1. Depuis 1, les villes 3 et 4 sont à 15 et 6 : on va en 4. Depuis 4, il reste la ville 3, à 11. Trajet 2, 1, 4, 3, puis retour de 3 à 2 : 8 + 6 + 11 + 10 = 35.
:::

::: retenir
Le voyageur de commerce cherche un circuit passant une fois par chaque ville ; la ville non visitée la plus proche à chaque étape est une stratégie gloutonne, qui ne garantit pas le plus court circuit.
:::

## 🧱 Les structures Distance, Visite et Trajet

Pour appliquer la règle, le programme doit se souvenir de trois choses : les distances entre toutes les villes, les villes déjà visitées, et l'ordre de visite.
Comment ranger ces informations dans des tableaux, et comment en tirer le circuit ?

::: definition
Les villes sont repérées par leurs numéros 1 à n (n ≤ NbMax = 20). Trois structures :
**Distance** : matrice carrée n × n, Distance[i, j] est la distance de la ville i à la ville j (Distance[i, i] = 0).
**Visite** : vecteur de n booléens, Visite[j] vaut Vrai si la ville j est déjà visitée ; il commence à Faux.
**Trajet** : vecteur de n entiers, Trajet[k] est le numéro de la k-ième ville visitée.
:::

```pascal
Const NbMax = 20;
Type Dist = Array [1..NbMax, 1..NbMax] Of Integer;
     Visit = Array [1..NbMax] Of Boolean;
     Traj = Array [1..NbMax] Of Integer;

Procedure Former_Trajet (n, depart : Integer; Distance : Dist; Var Visite : Visit; Var Trajet : Traj);
Var i : Integer;
Begin
  For i := 1 To n Do Visite[i] := False;
  Trajet[1] := depart;
  Visite[depart] := True;
  For i := 2 To n Do
  Begin
    Trajet[i] := Ville_proche_non_visit (Trajet[i - 1], n, Distance, Visite);
    Visite[Trajet[i]] := True;
  End;
End;

Function Longueur (n : Integer; Distance : Dist; Trajet : Traj) : Integer;
Var i, s : Integer;
Begin
  s := 0;
  For i := 1 To n - 1 Do s := s + Distance[Trajet[i], Trajet[i + 1]];
  Longueur := s + Distance[Trajet[n], Trajet[1]];
End;
```

`Former_Trajet` fait n − 1 choix grâce à `Ville_proche_non_visit`, étudiée à la section suivante (dans le programme, elle se place avant `Former_Trajet`). `Longueur` ajoute le retour `Distance[Trajet[n], Trajet[1]]`, car `Trajet` ne le contient pas.

::: exemple Les trois tableaux sur le circuit de la section précédente (n = 5, départ 1)

1. Début : `Visite` vaut Faux partout, puis `Trajet[1] = 1` et `Visite[1] = Vrai`, car le départ est déjà visité.
2. i = 2 : la ville en cours est `Trajet[1] = 1` ; le choix est 5, donc `Trajet[2] = 5` et `Visite[5] = Vrai`.
3. i = 3 : la ville en cours est `Trajet[2] = 5` ; le choix est 4, donc `Trajet[3] = 4` et `Visite[4] = Vrai`.
4. Avant i = 4, `Visite` vaut (Vrai, Faux, Faux, Vrai, Vrai) : seules 2 et 3 restent à choisir, depuis `Trajet[3] = 4`.

:::

::: piege
**Erreur : oublier `Visite[depart] := True`.** La ville de départ reste alors « non visitée ». Comme Distance[1, 1] = 0 est plus petit que toute autre distance, la première ville choisie depuis la ville 1 est la ville 1 elle-même : on obtient le trajet 1, 1, 5, 4, 3 sur notre exemple, avec la ville 2 jamais visitée.
:::

::: propriete
`Trajet` contient chaque numéro de 1 à n exactement une fois ; le retour au départ se compte à part, dans `Longueur`.
Cas limite : pour n = 1, la boucle de i = 2 à n ne s'exécute pas, `Trajet` ne contient que le départ et `Longueur` rend Distance[1, 1] = 0.
:::

::: verifie À toi : la longueur d'un trajet
Avec le tableau des distances de la section précédente, que rend `Longueur` pour n = 5 et le trajet 2, 5, 1, 3, 4 ?

---

La fonction additionne les quatre trajets consécutifs : Distance[2, 5] = 20, Distance[5, 1] = 9, Distance[1, 3] = 13, Distance[3, 4] = 6, soit 48 ; puis elle ajoute le retour Distance[4, 2] = 26. Résultat : 48 + 26 = 74.
:::

::: retenir
Distance donne les distances, Visite marque les villes déjà prises, Trajet garde l'ordre ; le retour au départ n'est pas dans Trajet, il s'ajoute au calcul de la longueur.
:::

## 🔎 Ville_proche_non_visit : un minimum sous condition

Au milieu du circuit, le livreur est en 4 et ne peut aller que vers les villes encore non visitées. Pour retrouver la plus proche, le programme doit chercher un minimum, mais seulement parmi certaines villes.
Comment écrire cette recherche d'un minimum avec une condition ?

::: definition
`Ville_proche_non_visit (c, …)` rend le numéro de la ville **non visitée** j qui rend Distance[c, j] minimal, où c est la **ville en cours**.
Méthode : 1) prendre pour candidate la première ville non visitée ; 2) parcourir les villes suivantes et remplacer la candidate par toute ville non visitée **strictement** plus proche de c ; 3) rendre la candidate.
:::

```pascal
Function Ville_proche_non_visit (c, n : Integer; Distance : Dist; Visite : Visit) : Integer;
Var j, ind : Integer;
Begin
  ind := 1;
  While Visite[ind] Do ind := ind + 1;
  For j := ind + 1 To n Do
    If (Not Visite[j]) And (Distance[c, j] < Distance[c, ind]) Then ind := j;
  Ville_proche_non_visit := ind;
End;
```

::: exemple Le troisième choix du circuit : c = 5, Visite = (Vrai, Faux, Faux, Faux, Vrai)

1. `ind` devient la première ville non visitée, la ville 2 ; Distance[5, 2] = 20.
2. j = 3 : non visitée et 19 < 20, donc `ind` devient 3.
3. j = 4 : non visitée et 18 < 19, donc `ind` devient 4.
4. j = 5 : déjà visitée, on l'ignore. La fonction rend 4 ✓.

:::

::: piege
**Erreur : mesurer les distances depuis le rang de l'étape.** On écrit Distance[i, j], où i est le numéro de l'étape, au lieu de Distance[c, j]. L'erreur tente parce que i est déjà dans la boucle de `Former_Trajet`. Mais à l'étape 3, Distance[3, j] vaut 31, 0 et 6 pour j = 2, 3, 4 : la fonction rendrait la ville 3 (distance 0 d'elle-même) au lieu de 4. Appliquée à chaque étape, depuis la ville 1, l'erreur donne toujours le trajet 1, 2, 3, 4, 5, qui ignore les distances.
:::

::: propriete
La condition combine deux tests : la ville est non visitée **et** strictement plus proche de c que la candidate.
Cas limite : en cas d'égalité, le test strict conserve la première ville rencontrée, celle de plus petit numéro. La fonction suppose qu'il reste une ville non visitée ; `Former_Trajet` ne l'appelle que n − 1 fois, donc c'est toujours vrai.
:::

::: verifie À toi : suivre la fonction
Avec le tableau des distances de la première section, que rend la fonction pour c = 2 et Visite = (Vrai, Vrai, Faux, Faux, Vrai) ?

---

La première ville non visitée est 3, donc `ind` vaut 3 et Distance[2, 3] = 31. Pour j = 4, la ville est non visitée et Distance[2, 4] = 26 < 31 : `ind` devient 4. Pour j = 5, la ville est déjà visitée. La fonction rend 4.
:::

::: retenir
Ville_proche_non_visit cherche un minimum sous condition : parmi les villes non visitées, la plus proche de la ville en cours c, avec un test strict.
:::

## 🧭 Autres approches : insertion et énumération

La stratégie de la ville la plus proche a donné 91 alors qu'un circuit de 74 existe. Deux autres idées s'offrent à nous.
Comment construire un meilleur circuit, et comment être certain d'avoir le plus court ?

::: definition
**Insertion** : on part de l'itinéraire 1, 2 (aller et retour), puis on insère chaque ville suivante P (3, 4, …, n) entre deux villes consécutives a et b de l'itinéraire, y compris entre la dernière et la première, à la place qui allonge le moins : coût = d(a, P) + d(P, b) − d(a, b). En cas d'égalité, on garde la dernière place trouvée en parcourant de gauche à droite.
**Énumération** : on liste tous les trajets possibles, on calcule la longueur de chacun et on garde le plus court. Avec un départ fixé, il y a (n − 1) ! trajets : 24 pour 5 villes.
:::

::: exemple L'insertion sur le tableau des distances de la première section

1. Itinéraire 1, 2. Pour la ville 3, les deux places coûtent 13 + 31 − 27 = 17 : égalité, on garde la dernière, d'où 1, 2, 3.
2. Ville 4 : entre 1 et 2, 14 + 26 − 27 = 13 ; entre 2 et 3, 26 + 6 − 31 = 1 ; entre 3 et 1, 6 + 14 − 13 = 7. Le plus petit coût est 1, d'où 1, 2, 4, 3.
3. Ville 5 : les quatre places coûtent 2, 12, 31 et 15 ; la première gagne, d'où 1, 5, 2, 4, 3.
4. Longueur : 9 + 20 + 26 + 6 + 13 = 74. Ici l'insertion trouve 74, mais rien ne le garantit en général.

:::

::: piege
**Erreur : oublier de retrancher d(a, b) dans le coût d'insertion.** On compare d(a, P) + d(P, b). L'erreur tente parce qu'on ne regarde que les nouveaux segments. Mais l'ancien segment a-b disparaît : pour la ville 4, on obtiendrait 40, 32 et 20 et on la placerait entre 3 et 1, d'où 1, 2, 3, 4 au lieu de 1, 2, 4, 3.
:::

::: propriete
Seule l'énumération garantit le plus court circuit, car elle examine tous les trajets ; l'insertion et la ville la plus proche sont des stratégies sans garantie.
Cas limite : le nombre de trajets explose : 120 pour 6 villes, 362 880 pour 10 villes. Chaque circuit apparaît deux fois, parcouru dans les deux sens.
:::

::: verifie À toi : compter les trajets
Combien de trajets partent d'une ville fixée pour 7 villes ?

---

Après le départ, les 6 autres villes se visitent dans n'importe quel ordre : 6 choix, puis 5, puis 4, et ainsi de suite, soit 6 × 5 × 4 × 3 × 2 × 1 = 720 trajets, c'est-à-dire (7 − 1) !.
:::

::: retenir
L'insertion ajoute chaque ville à la place qui allonge le moins l'itinéraire ; seule l'énumération des (n − 1) ! trajets garantit le plus court.
:::

## 🔢 Les permutations dans l'ordre lexicographique

Pour énumérer, il faut lister tous les ordres de visite des villes 1 à n, sans en oublier ni répéter. Pour 3 villes, on peut écrire 123, 132, 213, 231, 312, 321 : l'ordre est celui du dictionnaire.
Comment passer d'une permutation à la suivante, sans les garder toutes en mémoire ?

::: definition
Dans l'**ordre lexicographique**, on compare deux permutations comme deux mots : à la première position où elles diffèrent. On part de (1, 2, …, n) ; la dernière est (n, …, 1). Pour passer de T à la suivante (sujet du baccalauréat 1992) :

1. i = le plus grand indice tel que T[i − 1] < T[i] (s'il n'y en a aucun, T est la dernière) ;
2. j = le plus grand indice tel que T[i − 1] < T[j] ;
3. permuter T[i − 1] et T[j] ;
4. renverser T[i], …, T[n].

:::

```pascal
Function PGI (T : Tab) : Integer;
Var i, r : Integer;
Begin
  r := 0;
  For i := 2 To n Do If T[i - 1] < T[i] Then r := i;
  PGI := r;
End;

Function PGJ (T : Tab; r : Integer) : Integer;
Var j, s : Integer;
Begin
  s := 0;
  For j := r To n Do If T[r - 1] < T[j] Then s := j;
  PGJ := s;
End;
```

Ici `n` est la taille de la permutation et `Tab` un tableau de n entiers ; `PGI` rend 0 quand T est la dernière permutation, et `PGJ (T, r)` s'utilise avec r = `PGI (T)`.

::: exemple Le successeur de (1, 3, 4, 2)

1. Étape 1 : 1 < 3 et 3 < 4, mais 4 > 2 : le plus grand indice est i = 3 (T[2] = 3 < T[3] = 4).
2. Étape 2 : T[2] = 3 est inférieur à T[3] = 4, mais pas à T[4] = 2 : j = 3.
3. Étape 3 : on permute T[2] et T[3], d'où (1, 4, 3, 2).
4. Étape 4 : on renverse T[3], T[4] : (1, 4, 2, 3) ✓.

:::

::: piege
**Erreur : oublier de renverser la fin.** Après la permutation, on s'arrête à (1, 4, 3, 2). L'erreur tente parce que l'échange semble avoir « fait avancer » la permutation. Mais la fin T[3], T[4] était décroissante, donc la plus grande possible ; il faut la remettre croissante pour obtenir la plus petite permutation qui suive. Sans cela, on saute (1, 4, 2, 3), qui précède (1, 4, 3, 2).
:::

::: propriete
En répétant le successeur depuis (1, 2, …, n), on liste les n ! permutations, une fois chacune, jusqu'à ce que `PGI` rende 0.
Cas limite : pour (n, …, 1), aucun T[i − 1] n'est inférieur à T[i] ; `PGI` rend 0 et la liste est terminée.
:::

::: verifie À toi : un successeur
Quel est le successeur de (2, 4, 3, 1) ?

---

Étape 1 : 2 < 4 mais 4 > 3 et 3 > 1, donc i = 2. Étape 2 : le plus grand j tel que T[1] = 2 < T[j] est j = 3, car T[3] = 3 mais T[4] = 1. Étape 3 : on permute T[1] et T[3], d'où (3, 4, 2, 1). Étape 4 : on renverse T[2], T[3], T[4], d'où (3, 1, 2, 4).
:::

::: retenir
Le successeur lexicographique se calcule en quatre étapes : PGI, PGJ, permutation, renversement ; la liste s'arrête quand PGI rend 0.
:::

## ♛ Les huit dames : la contrainte, la représentation et le test

On veut placer 8 dames sur un échiquier de 8 cases sur 8, de sorte qu'aucune ne puisse prendre une autre. Une dame menace toute sa ligne, toute sa colonne et ses deux diagonales.
Comment représenter un placement pour qu'un programme teste les menaces, sans dessiner l'échiquier ?

::: definition
Le **problème des n dames** : placer n dames sur un échiquier n × n sans que deux dames soient sur la même ligne, la même colonne ou la même diagonale.
Il y a une dame par ligne : on les range dans un tableau T, où T[i] est le **numéro de la colonne** de la dame de la ligne i. Deux dames ne peuvent alors jamais partager une ligne.
:::

Voici un échiquier 4 × 4 où les lignes 1 et 2 portent des dames (T[1] = 2 et T[2] = 4). On cherche une colonne pour la ligne 3.

::: figure Dames en ligne 1 colonne 2 et ligne 2 colonne 4 : en ligne 3, seule la case de la colonne 1 est libre (ok) ; les trois autres sont menacées (×)
<svg viewBox="0 0 280 250">
<title>Échiquier 4 par 4 : dames en ligne 1 colonne 2 et ligne 2 colonne 4 ; en ligne 3, seule la colonne 1 est libre</title>
<text x="70.0" y="18" font-size="13" text-anchor="middle" fill="#0f172a">1</text>
<text x="122.0" y="18" font-size="13" text-anchor="middle" fill="#0f172a">2</text>
<text x="174.0" y="18" font-size="13" text-anchor="middle" fill="#0f172a">3</text>
<text x="226.0" y="18" font-size="13" text-anchor="middle" fill="#0f172a">4</text>
<text x="30" y="57.0" font-size="13" text-anchor="middle" fill="#0f172a">1</text>
<text x="30" y="109.0" font-size="13" text-anchor="middle" fill="#0f172a">2</text>
<text x="30" y="161.0" font-size="13" text-anchor="middle" fill="#0f172a">3</text>
<text x="30" y="213.0" font-size="13" text-anchor="middle" fill="#0f172a">4</text>
<rect x="44" y="26" width="52" height="52" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.2"/>
<rect x="96" y="26" width="52" height="52" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.2"/>
<rect x="148" y="26" width="52" height="52" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.2"/>
<rect x="200" y="26" width="52" height="52" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.2"/>
<rect x="44" y="78" width="52" height="52" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.2"/>
<rect x="96" y="78" width="52" height="52" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.2"/>
<rect x="148" y="78" width="52" height="52" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.2"/>
<rect x="200" y="78" width="52" height="52" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.2"/>
<rect x="44" y="130" width="52" height="52" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.2"/>
<rect x="96" y="130" width="52" height="52" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.2"/>
<rect x="148" y="130" width="52" height="52" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.2"/>
<rect x="200" y="130" width="52" height="52" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.2"/>
<rect x="44" y="182" width="52" height="52" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.2"/>
<rect x="96" y="182" width="52" height="52" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.2"/>
<rect x="148" y="182" width="52" height="52" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.2"/>
<rect x="200" y="182" width="52" height="52" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="122.0" cy="52.0" r="17" fill="#dc2626" stroke="#0f172a" stroke-width="1.6"/>
<text x="122.0" y="57.0" font-size="14" font-weight="bold" text-anchor="middle" fill="#ffffff" stroke="#0f172a" stroke-width="0.6">D</text>
<circle cx="226.0" cy="104.0" r="17" fill="#dc2626" stroke="#0f172a" stroke-width="1.6"/>
<text x="226.0" y="109.0" font-size="14" font-weight="bold" text-anchor="middle" fill="#ffffff" stroke="#0f172a" stroke-width="0.6">D</text>
<rect x="47" y="133" width="46" height="46" fill="#bbf7d0" stroke="#0f6e56" stroke-width="2"/>
<text x="70.0" y="161.0" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">ok</text>
<rect x="99" y="133" width="46" height="46" fill="#fecaca" stroke="#b91c1c" stroke-width="2"/>
<text x="122.0" y="163.0" font-size="22" font-weight="bold" text-anchor="middle" fill="#7f1d1d">×</text>
<rect x="151" y="133" width="46" height="46" fill="#fecaca" stroke="#b91c1c" stroke-width="2"/>
<text x="174.0" y="163.0" font-size="22" font-weight="bold" text-anchor="middle" fill="#7f1d1d">×</text>
<rect x="203" y="133" width="46" height="46" fill="#fecaca" stroke="#b91c1c" stroke-width="2"/>
<text x="226.0" y="163.0" font-size="22" font-weight="bold" text-anchor="middle" fill="#7f1d1d">×</text>
</svg>
:::

Dans la figure, T[1] = 2 et T[2] = 4 : les dames sont à la ligne 1, colonne 2 et à la ligne 2, colonne 4.

Pour savoir si la case de la ligne 3 et de la colonne col est menacée par la dame de la ligne j, on compare : même colonne si T[j] = col ; même diagonale si l'écart de colonnes Abs (T[j] − col) est égal à l'écart de lignes 3 − j.

::: exemple Tester les quatre cases de la ligne 3

1. Colonne 1 : avec j = 1, Abs (2 − 1) = 1 est différent de 3 − 1 = 2 ; avec j = 2, Abs (4 − 1) = 3 est différent de 1 : libre.
2. Colonne 2 : T[1] = 2 : même colonne que la dame de la ligne 1, menacée.
3. Colonne 3 : avec j = 2, Abs (4 − 3) = 1 = 3 − 2 : même diagonale que la dame de la ligne 2, menacée.
4. Colonne 4 : T[2] = 4 : même colonne que la dame de la ligne 2, menacée.

:::

::: piege
**Erreur : ne tester que les colonnes.** On vérifie T[j] = col et on place la dame en colonne 3, dont aucune dame n'occupe la colonne. L'erreur tente parce que la diagonale se voit moins bien qu'une colonne dans un tableau. Mais Abs (4 − 3) = 1 = 3 − 2 : la dame de la ligne 2 menace cette case en diagonale.
:::

::: propriete
Une dame placée à la ligne lig, colonne col, est **menacée** par la dame de la ligne j (j < lig) si :
T[j] = col (même colonne) ou Abs (T[j] − col) = lig − j (même diagonale).
Cas limite : pour la ligne 1, aucune dame n'est encore placée, donc aucune comparaison : toutes les colonnes sont libres.
Le critère ne change pas par symétrie de l'échiquier : si T est une solution, T'[i] = n + 1 − T[i] (symétrie par rapport à l'axe vertical) en est une aussi, car les colonnes restent distinctes et les écarts de colonnes sont conservés.
:::

::: verifie À toi : une diagonale
Six dames : T[1] = 5, T[2] = 2, T[3] = 6. La case de la ligne 4, colonne 4 est-elle menacée ?

---

Avec j = 1 : Abs (5 − 4) = 1 est différent de 4 − 1 = 3, et 5 est différent de 4. Avec j = 2 : Abs (2 − 4) = 2 = 4 − 2, donc la dame de la ligne 2 la menace en diagonale. La case est menacée (inutile de tester j = 3).
:::

::: retenir
T[i] est la colonne de la dame de la ligne i ; une case (lig, col) est menacée si T[j] = col ou si Abs (T[j] − col) = lig − j pour une ligne j déjà placée.
:::

## ↩️ Le retour sur trace

On place les dames ligne après ligne, en prenant à chaque ligne la première colonne libre. Pour quatre dames, la première en colonne 1 et la deuxième en colonne 3 mènent à une ligne 3 sans aucune case libre.
Que faire quand on est bloqué : s'arrêter, tout recommencer, ou revenir un peu en arrière ?

::: definition
Le **retour sur trace** (en anglais **backtracking**) consiste à revenir légèrement en arrière sur des décisions prises afin de sortir d'un blocage.
Pour les dames : si une ligne n'a aucune case libre (**impasse**), on **abandonne la branche** : on revient à la ligne précédente et on essaie la colonne libre suivante ; s'il n'y en a plus, on remonte encore.
:::

::: exemple La recherche pour quatre dames

| T déjà placé | Colonnes libres de la ligne suivante | Décision                                        |
| ------------ | ------------------------------------ | ----------------------------------------------- |
| (1)          | 3 et 4                               | on place 3                                      |
| (1, 3)       | aucune                               | impasse : retour, on essaie 4                   |
| (1, 4)       | 2                                    | on place 2                                      |
| (1, 4, 2)    | aucune                               | impasse : retours jusqu'à la ligne 1, colonne 2 |
| (2)          | 4                                    | on place 4                                      |
| (2, 4)       | 1                                    | on place 1                                      |
| (2, 4, 1)    | 3                                    | solution (2, 4, 1, 3)                           |

:::

La suite de la recherche (colonnes 3 puis 4 à la ligne 1) trouve la seconde solution, (3, 1, 4, 2) : le problème a 2 solutions pour n = 4.

::: piege
**Erreur : croire qu'une impasse prouve qu'il n'y a pas de solution.** La branche (1, 3) est bloquée et l'on conclut que la dame de la ligne 1 ne peut pas aller en colonne 1. L'erreur tente parce que le blocage est bien réel. Mais il ne condamne que cette branche, pas le problème : (1, 4) est encore possible, puis (2, 4, 1, 3) existe. On abandonne la branche, jamais la recherche.
:::

::: propriete
Le retour sur trace explore toutes les branches : une impasse n'abandonne que la dernière décision. Le problème n'a aucune solution quand toutes les branches échouent.
Cas limite : pour n = 2 et n = 3, toutes les branches échouent : aucune solution.
:::

::: verifie À toi : une impasse immédiate
Pour trois dames, la dame de la ligne 1 est en colonne 2. Que se passe-t-il à la ligne 2 ?

---

Les trois colonnes sont menacées : T[1] = 2 menace la colonne 2 (même colonne) et, avec Abs (2 − 1) = 1 = 2 − 1 et Abs (2 − 3) = 1 = 2 − 1, les colonnes 1 et 3 (diagonales). La ligne 2 est une impasse : on abandonne cette branche et on passe à la colonne 3 de la ligne 1.
:::

::: retenir
Le retour sur trace revient en arrière dès qu'une impasse apparaît et essaie la décision suivante ; il explore toutes les branches.
:::

## 🧮 Place_dame : le placement récursif et le comptage

Le retour en arrière est précisément ce que fait la récursivité : quand un appel se termine, l'appel précédent reprend et passe à la colonne suivante. Il reste à écrire la procédure et à compter les solutions.
Comment la récursivité place-t-elle les dames et compte-t-elle les solutions ?

::: definition
`Place_dame (T, lig)` place les dames des lignes lig à nbd, celles des lignes 1 à lig − 1 étant déjà posées.
**Cas particulier** : lig = nbd + 1, toutes les dames sont placées : une solution de plus.
**Cas général** : pour chaque colonne col de 1 à nbd, si la case n'est pas menacée, on pose `T[lig] := col` et on appelle `Place_dame (T, lig + 1)`.
:::

```pascal
Const nbd = 8;
Type Tab = Array [1..nbd] Of Integer;
Var TD : Tab; solution : LongInt;

Function Menace (T : Tab; lig, col : Integer) : Boolean;
Var j : Integer; m : Boolean;
Begin
  m := False;
  For j := 1 To lig - 1 Do
    If (T[j] = col) Or (Abs (T[j] - col) = lig - j) Then m := True;
  Menace := m;
End;

Procedure Place_dame (Var T : Tab; lig : Integer);
Var col : Integer;
Begin
  If lig = nbd + 1 Then solution := solution + 1
  Else
    For col := 1 To nbd Do
      If Not Menace (T, lig, col) Then
      Begin
        T[lig] := col;
        Place_dame (T, lig + 1);
      End;
End;
```

Le programme principal met `solution` à 0, appelle `Place_dame (TD, 1)` puis affiche `solution` : 92 pour nbd = 8. L'abandon d'une branche est le simple retour de l'appel ; `T[lig]` est écrasé à l'essai suivant, sans rien défaire. Le manuel écrit la même chose avec une étiquette, `GoTo suivant` et `Continue` ; le `If Not Menace` s'en passe.

::: exemple Compter les solutions pour nbd = 4

1. L'appel `Place_dame (TD, 1)` parcourt la table de la section précédente : chaque ligne essayée de 1 à 4 est un appel, et chaque colonne libre en lance un autre.
2. Au total, 1 appel avec lig = 1, puis 4, 6, 4 et 2 appels avec lig = 2, 3, 4 et 5 : 1 + 4 + 6 + 4 + 2 = 17 appels.
3. Seuls les deux appels avec lig = 5 atteignent le cas particulier et ajoutent 1 à `solution` : `solution` vaut 2 ✓.

:::

| n         | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| solutions | 1   | 0   | 0   | 2   | 10  | 4   | 40  | 92  |

| n         | 9   | 10  | 11    | 12     | 13     | 14      | 15        |
| --------- | --- | --- | ----- | ------ | ------ | ------- | --------- |
| solutions | 352 | 724 | 2 680 | 14 200 | 73 712 | 365 596 | 2 279 184 |

::: piege
**Erreur : arrêter la récursion une ligne trop tôt.** On écrit `If lig = nbd Then solution := solution + 1`. L'erreur tente parce que nbd est « la dernière ligne ». Mais l'appel avec lig = nbd n'a pas encore posé la dame de la dernière ligne : le programme compte des placements de nbd − 1 dames, soit 4 pour nbd = 4 au lieu de 2.
:::

::: propriete
Le nombre de solutions ne suit pas une règle simple : 4 pour n = 6 mais 40 pour n = 7, et il croît très vite ensuite.
Cas limite : n = 1 a une solution (une dame sur une case) ; n = 2 et n = 3 n'en ont aucune.
:::

::: verifie À toi : compter les appels
Pour nbd = 2, combien d'appels de `Place_dame` (le premier compris) et combien de solutions ?

---

L'appel avec lig = 1 essaie les colonnes 1 et 2, toutes libres : 2 appels avec lig = 2. Dans chacun, les deux colonnes sont menacées (même colonne, ou diagonale). Aucun appel n'atteint lig = 3. Total : 1 + 2 = 3 appels, et aucune solution.
:::

::: retenir
Place_dame place une dame par ligne ; elle compte une solution quand lig = nbd + 1 ; l'appel qui se termine fait le retour sur trace, et 92 solutions pour n = 8.
:::

> 🏆 Dernier boss franchi : tu sais choisir entre règle simple et exploration, et ramener l'exploration à une récursivité. Le chapitre est conquis ; il te reste les missions pour le prouver.
