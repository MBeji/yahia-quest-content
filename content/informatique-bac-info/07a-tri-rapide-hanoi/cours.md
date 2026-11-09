# ⚔️ Le tri rapide et les tours de Hanoï — diviser pour mieux régner

> 💡 «Un grand problème se découpe en deux plus petits, et le découpage se résout en s'appelant lui-même.»

Ce chapitre présente huit notions : le tri rapide (principe, trace d'une partition, écriture en Pascal, choix du pivot et pire cas), les tours de Hanoï (règle et idée récursive, séquences et procédure Pascal, nombre de déplacements) et le tri comptage. Les deux premiers sujets s'appuient sur la récursivité, le troisième prolonge les tris par comparaison. Les tableaux sont numérotés à partir de 1 et triés en ordre croissant.

## 🎯 Le tri rapide : pivot, partition, récursion

Pour ranger un tas de copies par note, tu en tires une et tu fais deux tas : les notes inférieures ou égales d'un côté, les notes supérieures de l'autre. Cette copie est alors à sa place définitive, et il reste deux tas plus petits à ranger de la même façon.
Sur un tableau, où l'on ne sait qu'échanger des cases, comment faire ce découpage, et pourquoi suffit-il de le répéter ?

::: definition
Le **tri rapide** (QuickSort, ou tri de Hoare) est un tri **récursif**. On choisit un élément, le **pivot** (ici le premier élément du sous-tableau), et l'on réorganise le sous-tableau par échanges : les valeurs inférieures ou égales au pivot vont à sa gauche, les valeurs supérieures à sa droite. Cette opération est la **partition**. Le pivot est alors à sa **place définitive**, et l'on recommence sur chacun des deux côtés tant qu'il contient au moins deux éléments.
:::

::: exemple Une partition de [14, 5, 20, 9, 3, 17, 11]

1. Le pivot est T[1] = 14. Parmi les six autres valeurs, 5, 9, 3 et 11 sont inférieures ou égales à 14 : il y en a 4.
2. Ces 4 valeurs occupent les cases 1 à 4 et le pivot la case 1 + 4 = 5, car il se place juste après elles : T = [3, 5, 11, 9, 14, 17, 20].
3. Le pivot est à sa place définitive : à sa gauche 3, 5, 11, 9 sont inférieurs ou égaux à 14, à sa droite 17 et 20 sont supérieurs.
4. Il reste deux appels récursifs, un sur les cases 1 à 4 et un sur les cases 6 à 7, chacun plus petit que le tableau de départ ✓.

:::

::: piege
**Erreur : croire que la partition trie les deux côtés.** On regarde [3, 5, 11, 9, 14, 17, 20], on voit le pivot bien placé et l'on conclut « le tableau est trié ». L'erreur tente parce que cet exemple est presque rangé. Mais la partition ne garantit que la place du pivot et la séparation entre « inférieur ou égal » et « supérieur » : à gauche, 11 est encore avant 9. Les deux côtés restent à trier par les appels récursifs.
:::

::: propriete
Après la partition de T[g..d], le pivot est en case m. T[g..m − 1] ne contient que des valeurs ≤ pivot, T[m + 1..d] que des valeurs > pivot, et m = g + (nombre de valeurs ≤ pivot parmi T[g + 1..d]).
Cas limites : si aucune valeur n'est ≤ pivot, m = g et le côté gauche est vide ; une valeur égale au pivot reste à sa gauche ; un sous-tableau d'un seul élément est déjà trié, et c'est ce qui arrête la récursivité.
:::

::: verifie À toi : placer le pivot
Pour T = [9, 14, 4, 12, 2, 16, 7], le pivot est 9. Dans quelle case se place-t-il, et quelles valeurs sont à sa gauche ?

---

Parmi les six autres valeurs, 4, 2 et 7 sont inférieures ou égales à 9 : il y en a 3, donc le pivot va en case 1 + 3 = 4. À sa gauche se trouvent 4, 2 et 7 (dans un ordre que la partition ne trie pas), à sa droite 14, 12 et 16, tous supérieurs à 9.
:::

::: retenir
Le tri rapide place un pivot à sa place définitive par une partition (≤ à gauche, > à droite), puis recommence sur chaque côté.
:::

## 🔍 Suivre une partition pas à pas

La partition travaille avec deux indices : **i** avance depuis la gauche à la recherche d'une valeur trop grande pour rester à gauche du pivot, **j** recule depuis la droite à la recherche d'une valeur trop petite pour rester à droite.
Prenons T = [10, 6, 13, 8, 19, 2, 1, 31, 3, 11] avec le pivot 10 : comment les indices avancent-ils, et quand s'arrêtent-ils ?

::: figure État de départ : le pivot est en case 1, i commence en case 2 et j en case 10
<svg viewBox="0 0 400 130">
<title>Tableau [10, 6, 13, 8, 19, 2, 1, 31, 3, 11] numéroté de 1 à 10 : pivot 10 en case 1, indice i sous la case 2, indice j au-dessus de la case 10</title>
<text x="38" y="16" font-size="12" text-anchor="middle" fill="#0f172a">pivot</text>
<text x="362" y="16" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">j</text>
<polygon points="362,38 355,24 369,24" fill="#dc2626" stroke="#0f172a" stroke-width="1.2"/>
<rect x="20" y="40" width="36" height="36" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/>
<text x="38" y="63" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">10</text>
<rect x="56" y="40" width="36" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="74" y="63" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">6</text>
<rect x="92" y="40" width="36" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="110" y="63" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">13</text>
<rect x="128" y="40" width="36" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="146" y="63" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">8</text>
<rect x="164" y="40" width="36" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="182" y="63" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">19</text>
<rect x="200" y="40" width="36" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="218" y="63" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">2</text>
<rect x="236" y="40" width="36" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="254" y="63" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">1</text>
<rect x="272" y="40" width="36" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="290" y="63" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">31</text>
<rect x="308" y="40" width="36" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="326" y="63" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">3</text>
<rect x="344" y="40" width="36" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="362" y="63" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">11</text>
<text x="38" y="92" font-size="10" text-anchor="middle" fill="#0f172a">1</text>
<text x="74" y="92" font-size="10" text-anchor="middle" fill="#0f172a">2</text>
<text x="110" y="92" font-size="10" text-anchor="middle" fill="#0f172a">3</text>
<text x="146" y="92" font-size="10" text-anchor="middle" fill="#0f172a">4</text>
<text x="182" y="92" font-size="10" text-anchor="middle" fill="#0f172a">5</text>
<text x="218" y="92" font-size="10" text-anchor="middle" fill="#0f172a">6</text>
<text x="254" y="92" font-size="10" text-anchor="middle" fill="#0f172a">7</text>
<text x="290" y="92" font-size="10" text-anchor="middle" fill="#0f172a">8</text>
<text x="326" y="92" font-size="10" text-anchor="middle" fill="#0f172a">9</text>
<text x="362" y="92" font-size="10" text-anchor="middle" fill="#0f172a">10</text>
<polygon points="74,98 67,112 81,112" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<text x="74" y="126" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">i</text>
</svg>
:::

Dans la figure, l'indice i parcourt le tableau de gauche à droite à partir de la case 2 et l'indice j de droite à gauche à partir de la case 10 : ils vont se croiser quelque part, et c'est à cet endroit que le pivot se range.

::: exemple La partition de [10, 6, 13, 8, 19, 2, 1, 31, 3, 11]

1. i part de 2 : 6 ≤ 10, i avance en 3, où 13 > 10 l'arrête. j part de 10 : 11 > 10, j recule en 9, où 3 ≤ 10 l'arrête. 13 est trop grand pour la gauche et 3 trop petit pour la droite, on les échange : T = [10, 6, 3, 8, 19, 2, 1, 31, 13, 11], puis i = 4 et j = 8.
2. 8 ≤ 10 : i avance en 5, où 19 > 10 l'arrête. 31 > 10 : j recule en 7, où 1 ≤ 10 l'arrête. On échange 19 et 1 : T = [10, 6, 3, 8, 1, 2, 19, 31, 13, 11], puis i = 6 et j = 6.
3. 2 ≤ 10 : i avance en 7 et dépasse j = 6. Les indices se sont croisés, la recherche est finie, et toutes les cases 2 à 6 contiennent des valeurs ≤ 10.
4. On échange le pivot T[1] avec T[j] = T[6], la dernière case des valeurs ≤ 10 : T = [2, 6, 3, 8, 1, 10, 19, 31, 13, 11] ✓. Le pivot est en case 6, avec 5 valeurs ≤ 10 à sa gauche et 4 valeurs > 10 à sa droite.

:::

::: piege
**Erreur : échanger le pivot avec T[i] à la fin.** À la sortie, i vaut 7 et T[7] = 19 : on échange T[1] et T[7] et l'on obtient [19, 6, 3, 8, 1, 2, 10, 31, 13, 11]. L'erreur tente parce que i est l'indice qui a travaillé en dernier. Mais i a dépassé la zone des valeurs ≤ 10 : T[7] est supérieur au pivot et se retrouve à sa gauche, où il n'a pas sa place. C'est T[j], dernière case des valeurs ≤ pivot, qu'il faut échanger avec le pivot.
:::

::: methode
Partition de T[g..d] avec le pivot T[g] :

1. i ← g + 1 et j ← d.
2. Tant que i ≤ j : si T[i] ≤ pivot, i avance ; sinon, si T[j] > pivot, j recule ; sinon on échange T[i] et T[j], puis i avance et j recule.
3. Quand i > j, on échange T[g] et T[j] ; le pivot est en case m = j.

Cas limite : si toutes les valeurs sont > pivot, j recule jusqu'en g et le pivot reste en place (T = [4, 9, 7, 8] : m = 1).
:::

::: verifie À toi : une partition complète
Fais la partition de T = [9, 4, 12, 2, 15, 7] avec le pivot 9 : quel est le premier échange, et quel tableau obtient-on à la fin ?

---

i avance sur 4 (≤ 9) et s'arrête en case 3 sur 12 ; j s'arrête tout de suite en case 6 sur 7 (≤ 9). On échange 12 et 7 : [9, 4, 7, 2, 15, 12], puis i = 4, j = 5. 2 ≤ 9 : i avance en 5 ; 15 > 9 : j recule en 4, et i > j. On échange le pivot avec T[4] = 2 : T = [2, 4, 7, 9, 15, 12], le pivot est en case 4.
:::

::: retenir
La partition fait avancer i tant que T[i] ≤ pivot, reculer j tant que T[j] > pivot, échange les valeurs mal placées, puis échange le pivot avec T[j].
:::

## 💻 Le tri rapide en Pascal

Tu sais partitionner à la main. Un programme doit le faire sur n'importe quel sous-tableau T[g..d], puis recommencer des deux côtés du pivot.
Quelles procédures écrire, et à quelle condition la récursivité s'arrête-t-elle ?

::: definition
Le tri rapide s'écrit avec deux procédures : `Partition` range le pivot et rend sa case m, `Tri_Rapide (T, g, d)` trie le sous-tableau T[g..d]. Pour trier T[1..n], on appelle `Tri_Rapide (T, 1, n)`. La récursivité s'arrête quand g ≥ d, c'est-à-dire pour zéro ou un élément.
:::

```pascal
Type Tab = Array [1..100] Of Integer;

Procedure Partition (Var T : Tab; g, d : Integer; Var m : Integer);
Var pivot, i, j, aux : Integer;
Begin
  pivot := T[g]; i := g + 1; j := d;
  While i <= j Do
    If T[i] <= pivot Then i := i + 1
    Else If T[j] > pivot Then j := j - 1
    Else
    Begin
      aux := T[i]; T[i] := T[j]; T[j] := aux;
      i := i + 1; j := j - 1;
    End;
  aux := T[g]; T[g] := T[j]; T[j] := aux;
  m := j;
End;

Procedure Tri_Rapide (Var T : Tab; g, d : Integer);
Var m : Integer;
Begin
  If g < d Then
  Begin
    Partition (T, g, d, m);
    Tri_Rapide (T, g, m - 1);
    Tri_Rapide (T, m + 1, d);
  End;
End;
```

::: exemple Les appels pour T = [4, 2, 5, 1, 3]

1. `Tri_Rapide (T, 1, 5)` : g < d, donc `Partition` : le pivot 4 va en case 4 et T = [1, 2, 3, 4, 5]. Deux appels suivent : (1, 3) et (5, 5).
2. `Tri_Rapide (T, 1, 3)` : nouvelle partition, le pivot 1 reste en case 1 (aucune valeur plus petite). Elle appelle (1, 0), vide, puis (2, 3).
3. `Tri_Rapide (T, 2, 3)` : le pivot 2 reste en case 2, puis les appels (2, 1) et (3, 3) ne font rien. Les appels (5, 5) et (1, 0) s'arrêtent aussi, car g ≥ d.
4. Trois partitions ont suffi et T est trié ✓.

:::

::: piege
**Erreur : oublier le test If g < d.** On écrit directement `Partition` puis les deux appels. L'erreur tente parce que la partition « sait » s'arrêter quand il n'y a rien à faire. Mais sur un sous-tableau vide, comme T[3..2], `Partition` rend m = 2, et l'appel `Tri_Rapide (T, m + 1, d)` est `Tri_Rapide (T, 3, 2)`, identique à l'appel de départ : la récursivité ne se termine jamais. Avant même cela, l'appel (g, m − 1) descend jusqu'à lire T[0], hors du tableau, et `Partition` sur T[3..2] modifie des cases hors du sous-tableau.
:::

::: propriete
`Partition` ne touche que les cases g à d, et chaque appel récursif porte sur un sous-tableau plus petit, puisque le pivot est exclu : la récursivité se termine toujours, pourvu que le test g < d soit présent et que g et d désignent des cases de T.
Cas limites : pour n = 1, `Tri_Rapide (T, 1, 1)` ne fait rien ; pour n = 2, une seule partition suffit à trier ; des doublons sont gérés, car « ≤ pivot » les laisse à gauche.
:::

::: verifie À toi : compter les partitions
Combien de partitions `Tri_Rapide (T, 1, 3)` fait-il pour T = [3, 1, 2], et que contient T après la première ?

---

Le pivot 3 est le plus grand : i parcourt tout, puis le pivot est échangé avec T[3] et T = [2, 1, 3], avec m = 3. L'appel (1, 2) fait une seconde partition : le pivot 2 passe en case 2 et T = [1, 2, 3]. Les autres appels, (1, 1), (3, 2) et (4, 3), ne font rien : deux partitions en tout.
:::

::: retenir
`Tri_Rapide (T, g, d)` ne fait quelque chose que si g < d : il partitionne, puis s'appelle sur T[g..m − 1] et T[m + 1..d].
:::

## ⚖️ Le choix du pivot et le pire cas

Un jury a sept copies déjà classées de la plus faible à la meilleure et prend toujours la première, la plus faible, comme pivot : aucune copie n'est plus faible, le tas de gauche est vide et celui de droite garde six copies. Il recommencera donc presque autant de fois qu'il y a de copies.
Le choix du pivot compte-t-il, et quel tableau est le plus défavorable ?

::: definition
Avec le premier élément pour pivot, le **pire cas** est un tableau déjà trié : chaque partition ne retire que le pivot, un côté est vide et l'autre garde tous les autres éléments. Le cas favorable est celui où le pivot coupe le sous-tableau en deux moitiés comparables. Plus le tableau est mélangé, plus le premier élément a de chances de tomber près du milieu des valeurs : en général, l'efficacité du tri rapide croît avec le désordre.
On mesure le travail par le **nombre de partitions**, c'est-à-dire d'appels avec g < d.
:::

::: exemple Deux tableaux de 7 valeurs distinctes

1. T = [1, 2, 3, 4, 5, 6, 7] : le pivot 1 est le plus petit, donc m = 1. Il reste 6, puis 5, 4, 3 et 2 éléments à partitionner : 6 partitions en tout, le maximum pour 7 éléments.
2. T = [4, 1, 3, 2, 6, 5, 7] : le pivot 4 coupe en [2, 1, 3] et [6, 5, 7], de 3 éléments chacun, car T devient [2, 1, 3, 4, 6, 5, 7].
3. [2, 1, 3] a pour pivot 2 : il se place en case 2 et T = [1, 2, 3]. [6, 5, 7] a pour pivot 6 : il se place en case 6 et T = [5, 6, 7] : 3 partitions en tout ✓.

:::

::: piege
**Erreur : croire qu'un tableau déjà trié est le plus facile pour le tri rapide.** Pour l'insertion, un tableau trié ne coûte rien, et l'on transfère cette idée. L'erreur tente parce que le tableau semble n'avoir « rien à faire ». Mais le pivot, premier élément, est alors le plus petit : la partition échoue à couper le tableau et le tri rapide fait ses 6 partitions pour 7 éléments, tandis que [4, 1, 3, 2, 6, 5, 7], en désordre, n'en fait que 3.
:::

::: propriete
Le pivot du milieu limite ce défaut : on échange T[(g + d) Div 2] avec T[g] avant la partition, puis on procède comme d'habitude. Pour T = [1, 2, 3, 4, 5, 6, 7], le pivot est 4 et il y a 3 partitions au lieu de 6.
Cas limites : aucun choix fixe n'élimine le pire cas pour tous les tableaux ; un tableau dont toutes les valeurs sont égales fait 6 partitions pour 7 éléments avec le pivot du milieu comme avec le premier, car « ≤ pivot » envoie tout à gauche. Dans le pire cas, les appels s'empilent sur n niveaux, ce qui peut déborder la pile pour un grand tableau.
:::

::: verifie À toi : un tableau décroissant
Combien de partitions le tri rapide, avec le premier élément pour pivot, fait-il sur T = [8, 7, 6, 5, 4, 3, 2, 1] ?

---

Le pivot 8 est le plus grand : il va en case 8 et T = [1, 7, 6, 5, 4, 3, 2, 8]. Puis le pivot 1 est le plus petit : il reste en case 1. Chaque partition ne retire qu'un pivot, donc les sous-tableaux ont 8, 7, 6, 5, 4, 3, 2 éléments : 7 partitions, le maximum pour 8 éléments. Un tableau décroissant est un pire cas, comme un tableau croissant.
:::

::: retenir
Avec le premier élément pour pivot, un tableau déjà trié est le pire cas (n − 1 partitions) ; un pivot qui coupe en deux moitiés est le meilleur.
:::

## 🗼 Les tours de Hanoï : la règle et l'idée récursive

Trois piquets portent n disques de diamètres tous différents, empilés du plus grand en bas au plus petit en haut. Il faut transporter la pile sur un autre piquet, un disque à la fois, sans jamais poser un disque sur un plus petit. Mais le grand disque est coincé sous tous les autres.
Par où commencer ?

::: definition
Les **tours de Hanoï** (jeu imaginé par le mathématicien français Édouard Lucas) : trois piquets A, B et C, numérotés 1, 2 et 3 en Pascal, et n disques empilés sur le **piquet de départ**. Il faut les amener sur le **piquet cible** en s'aidant du **piquet intermédiaire**, avec deux règles : un seul disque à la fois, et jamais sur un disque plus petit. On cherche le **minimum de déplacements**.
:::

::: figure Pour n = 3, de A vers B : les deux petits disques sont garés sur C, le grand disque 3 peut enfin passer de A vers B
<svg viewBox="0 0 400 190">
<title>Trois piquets A, B, C : le disque 3 seul sur A, B vide, les disques 2 puis 1 empilés sur C, flèche du disque 3 vers B</title>
<line x1="10" y1="150" x2="390" y2="150" stroke="#0f172a" stroke-width="2"/>
<rect x="67" y="50" width="6" height="100" fill="#94a3b8" stroke="#0f172a" stroke-width="1"/>
<rect x="197" y="50" width="6" height="100" fill="#94a3b8" stroke="#0f172a" stroke-width="1"/>
<rect x="327" y="50" width="6" height="100" fill="#94a3b8" stroke="#0f172a" stroke-width="1"/>
<rect x="20" y="132" width="100" height="18" fill="#fca5a5" stroke="#0f172a" stroke-width="1.6"/>
<text x="70" y="146" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f172a">3</text>
<rect x="295" y="132" width="70" height="18" fill="#bae6fd" stroke="#0f172a" stroke-width="1.6"/>
<text x="330" y="146" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f172a">2</text>
<rect x="310" y="114" width="40" height="18" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/>
<text x="330" y="128" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f172a">1</text>
<line x1="80" y1="100" x2="184" y2="100" stroke="#0f6e56" stroke-width="2.5"/>
<polygon points="194,100 182,93 182,107" fill="#0f6e56" stroke="#0f6e56" stroke-width="1"/>
<text x="70" y="174" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">A</text>
<text x="200" y="174" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">B</text>
<text x="330" y="174" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">C</text>
</svg>
:::

Dans la figure, C est le piquet intermédiaire : il garde les n − 1 = 2 petits disques le temps que le disque 3 passe de A, piquet de départ, à B, piquet cible.

::: exemple Hanoï pour n = 2, de A vers B

1. Le disque 2 est coincé sous le disque 1. On déplace d'abord les n − 1 = 1 disques du dessus vers l'intermédiaire : le disque 1 va de A vers C.
2. A ne porte plus que le disque 2 et B est vide : le disque 2 va de A vers B, sans rien gêner.
3. Il reste à poser le disque 1 sur le disque 2, ce que les règles permettent car 1 < 2 : le disque 1 va de C vers B ✓. En tout 3 déplacements : A vers C, A vers B, C vers B.

:::

::: piege
**Erreur : envoyer les petits disques directement sur la cible.** Pour n = 2, on commence par poser le disque 1 sur B, « puisque c'est là que la pile doit finir ». L'erreur tente parce qu'on veut avancer vers le but. Mais B porte alors le disque 1 et le disque 2 ne peut plus s'y poser, car il serait au-dessus d'un plus petit. Les petits disques se garent sur le piquet intermédiaire, jamais sur la cible.
:::

::: propriete
Pour amener n disques du départ à la cible : (1) déplacer les n − 1 disques du dessus du départ vers l'intermédiaire ; (2) déplacer le plus grand disque du départ vers la cible ; (3) déplacer les n − 1 disques de l'intermédiaire vers la cible. Les étapes (1) et (3) sont le même problème avec un disque de moins et des rôles de piquets échangés.
Cas limite : pour n = 1, un seul déplacement, car les étapes (1) et (3), de 0 disque, ne font rien.
:::

::: verifie À toi : même problème, autres piquets
Pour n = 2, le piquet de départ est B, la cible est C et l'intermédiaire est A. Quels sont les déplacements ?

---

Le disque 1 est le seul à gêner le disque 2 : il se gare sur l'intermédiaire, de B vers A. Le disque 2 va de B vers la cible C. Le disque 1 revient de A vers C, sur le disque 2. Les déplacements sont B vers A, B vers C, A vers C, soit 3 déplacements.
:::

::: retenir
Hanoï se résout en trois temps : n − 1 disques vers l'intermédiaire, le grand disque vers la cible, n − 1 disques vers la cible.
:::

## 🔁 Hanoï : séquences et procédure Pascal

Pour n = 3, la méthode demande de résoudre deux fois le cas n = 2, avec les rôles des piquets échangés. À la main c'est lourd.
Et si une procédure s'appelait elle-même pour les deux sous-problèmes ?

::: definition
La procédure `Hanoi (n, depart, cible, inter)` affiche les déplacements qui amènent n disques du piquet `depart` vers le piquet `cible` en s'aidant de `inter`. L'appel `Hanoi (3, 1, 2, 3)` règle le cas de 3 disques du piquet 1 vers le piquet 2.
:::

```pascal
Procedure Hanoi (n, depart, cible, inter : Byte);
Begin
  If n > 0 Then
  Begin
    Hanoi (n - 1, depart, inter, cible);
    WriteLn ('Disque du piquet ', depart, ' vers le piquet ', cible);
    Hanoi (n - 1, inter, cible, depart);
  End;
End;
```

::: exemple Hanoï pour n = 3, de A vers B par C

1. `Hanoi (3, A, B, C)` appelle d'abord `Hanoi (2, A, C, B)` : les deux petits disques vont de A vers C en s'aidant de B. Cet appel affiche A vers B, A vers C, B vers C.
2. Le disque 3 est libre : la procédure affiche A vers B.
3. `Hanoi (2, C, B, A)` amène les deux petits disques de C vers B en s'aidant de A : C vers A, C vers B, A vers B ✓.
4. La séquence complète compte 7 déplacements : A vers B, A vers C, B vers C, A vers B, C vers A, C vers B, A vers B.

:::

::: piege
**Erreur : garder les mêmes rôles dans le premier appel récursif.** On écrit `Hanoi (n - 1, depart, cible, inter)` au lieu de `Hanoi (n - 1, depart, inter, cible)`. L'erreur tente parce que les deux appels ressemblent à l'appel d'origine. Mais pour n = 2, de A vers B, la procédure affiche alors A vers B, A vers B, C vers B : le grand disque est posé sur le petit disque déjà arrivé en B, ce que la règle interdit. Le premier appel doit garer les n − 1 disques sur l'intermédiaire.
:::

::: propriete
Dans `Hanoi`, le deuxième paramètre est toujours le départ et le troisième la cible. Le premier appel échange cible et intermédiaire, le second échange départ et intermédiaire. La procédure se termine pour tout n entier ≥ 0, car n diminue de 1 à chaque appel et n = 0 n'affiche rien.
Cas limite : `Hanoi (1, 1, 2, 3)` n'affiche qu'une ligne, car les deux appels sur 0 disque ne font rien.
:::

::: verifie À toi : lire un appel
Quelles lignes `Hanoi (2, 3, 1, 2)` affiche-t-il ? Les paramètres sont n, depart, cible, inter.

---

Le départ est 3, la cible est 1 et l'intermédiaire est 2. Le premier appel `Hanoi (1, 3, 2, 1)` affiche 3 vers 2 : le petit disque se gare sur l'intermédiaire. La procédure affiche ensuite 3 vers 1 pour le grand disque, puis `Hanoi (1, 2, 1, 3)` affiche 2 vers 1. Les lignes sont 3 vers 2, 3 vers 1, 2 vers 1.
:::

::: retenir
`Hanoi (n, depart, cible, inter)` appelle `Hanoi (n − 1, depart, inter, cible)`, affiche le déplacement du grand disque, puis appelle `Hanoi (n − 1, inter, cible, depart)`.
:::

## 🔢 Combien de déplacements ? 2ⁿ − 1 et la légende

Selon une légende, des moines déplacent 64 disques sacrés, un par seconde, et le monde finira quand le dernier sera en place. Avant de les croire, il faut compter : n = 1 demande 1 déplacement, n = 2 en demande 3, n = 3 en demande 7.
Y a-t-il une loi, et que donne-t-elle pour 64 disques ?

| Disques n         | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Déplacements u(n) | 1   | 3   | 7   | 15  | 31  | 63  | 127 | 255 |

Chaque valeur est le double de la précédente plus 1 : 2 × 7 + 1 = 15. C'est la méthode récursive qui l'explique : u(n − 1) déplacements pour garer les petits disques, 1 pour le grand, u(n − 1) pour les remettre, soit u(n) = 2 × u(n − 1) + 1.

::: exemple Du tableau à la formule, puis à la légende

1. Pour n = 4 : 7 + 1 + 7 = 15 déplacements, et 15 = 2⁴ − 1.
2. Pour n = 9, à partir de u(8) = 255 : u(9) = 2 × 255 + 1 = 511 = 2⁹ − 1.
3. Pour n = 64, la formule donne 2⁶⁴ − 1 = 18 446 744 073 709 551 615 déplacements, environ 1,8 × 10¹⁹.
4. À un déplacement par seconde, avec 31 536 000 secondes par an (365 jours), cela fait environ 585 milliards d'années, plus de quarante fois l'âge de l'Univers (environ 14 milliards d'années) : la prophétie n'a rien d'inquiétant ✓.

:::

::: piege
**Erreur : croire qu'un disque de plus ajoute un nombre fixe de déplacements.** On lit 1, 3, 7 et l'on prévoit 11 pour n = 4, en ajoutant 4 comme de 3 à 7. L'erreur tente parce que les trois premières valeurs paraissent régulières. Mais un disque de plus double le travail : il faut deux fois la pile précédente, plus le grand disque. Donc u(4) = 2 × 7 + 1 = 15, et de n à n + 1 on ajoute 2ⁿ déplacements.
:::

::: propriete
Le nombre de déplacements de la méthode récursive est u(n) = 2ⁿ − 1, et on admet que c'est le minimum. Si u(n − 1) = 2ⁿ⁻¹ − 1, alors u(n) = 2 × (2ⁿ⁻¹ − 1) + 1 = 2ⁿ − 1.
Pour compter en Pascal, on met une variable `nb : LongInt` à 0 avant l'appel et on écrit `nb := nb + 1` après chaque `WriteLn` de `Hanoi`.
Cas limites : pour n = 0, 0 déplacement, soit 2⁰ − 1 ; un `LongInt` va jusqu'à 2 147 483 647 = 2³¹ − 1, donc `nb` suffit jusqu'à n = 31 et déborde dès n = 32.
:::

::: verifie À toi : n = 11
Sachant que 10 disques demandent 1023 déplacements, combien en faut-il pour 11 disques ? Vérifie avec la formule.

---

Pour 11 disques, on garde 1023 déplacements pour garer les 10 petits disques, 1 pour le grand disque et 1023 pour les remettre : 2 × 1023 + 1 = 2047. La formule donne 2¹¹ − 1 = 2048 − 1 = 2047, le même résultat.
:::

::: retenir
Hanoï demande 2ⁿ − 1 déplacements : un disque de plus double le travail, d'où l'impossibilité pratique de la légende des 64 disques.
:::

## 🧮 Le tri comptage

Un professeur a noté 8 élèves sur 20 : [12, 15, 12, 9, 15, 15, 18, 9]. Les notes sont des entiers de 0 à 20 : plutôt que de comparer les élèves entre eux, il peut compter combien d'élèves ont chaque note.
Comment un simple décompte permet-il de reconstruire la liste triée ?

::: definition
Le **tri comptage** (ou tri casier) s'applique à des **entiers compris entre 0 et une valeur maximale connue vmax**. On crée un tableau intermédiaire `occ[0..vmax]`, rempli de zéros, où `occ[v]` compte les occurrences de la valeur v. On parcourt T pour compter, puis on reconstruit T en écrivant, pour v croissant, la valeur v exactement `occ[v]` fois.
Il ne compare jamais deux éléments entre eux ; il gère les doublons.
:::

```pascal
Const vmax = 20;
Type Tab = Array [1..100] Of Integer;

Procedure Tri_Comptage (n : Integer; Var T : Tab);
Var occ : Array [0..vmax] Of Integer;
    v, k, i : Integer;
Begin
  For v := 0 To vmax Do occ[v] := 0;
  For i := 1 To n Do occ[T[i]] := occ[T[i]] + 1;
  k := 0;
  For v := 0 To vmax Do
    For i := 1 To occ[v] Do
    Begin
      k := k + 1;
      T[k] := v;
    End;
End;
```

::: exemple Trier [12, 15, 12, 9, 15, 15, 18, 9]

1. Après le décompte, `occ[9]` = 2, `occ[12]` = 2, `occ[15]` = 3, `occ[18]` = 1 et toutes les autres cases valent 0 : le total est 2 + 2 + 3 + 1 = 8, comme n.
2. La reconstruction parcourt v de 0 à 20 : les cases vides n'écrivent rien, v = 9 écrit deux fois 9, v = 12 deux fois 12, v = 15 trois fois 15 et v = 18 une fois 18.
3. T = [9, 9, 12, 12, 15, 15, 15, 18] ✓ : les valeurs sont lues dans l'ordre des indices de `occ`, donc déjà rangées.

:::

::: piege
**Erreur : écrire le nombre d'occurrences au lieu de la valeur.** À la reconstruction, on écrit `T[k] := occ[v]`. L'erreur tente parce que `occ[v]` est le nombre que l'on vient de manipuler. Mais l'indice v est la valeur à ranger et `occ[v]` seulement le nombre de fois où l'écrire : on obtiendrait [2, 2, 2, 2, 3, 3, 3, 1] au lieu de [9, 9, 12, 12, 15, 15, 15, 18].
:::

::: propriete
Le tri comptage exige des valeurs entières dans [0, vmax] ; la taille de `occ` dépend de vmax, pas de n. Ne pas confondre avec le comptage du chapitre sur les tris, qui place chaque élément selon le nombre de valeurs strictement inférieures et suppose des valeurs distinctes : ici le tableau d'occurrences accepte les doublons.
Cas limites : une valeur négative ou supérieure à vmax donne un indice hors de `occ` ; pour des valeurs allant jusqu'à un million, `occ` aurait un million de cases, ce qui rend la méthode peu adaptée.
:::

::: verifie À toi : décompter
Trie T = [5, 2, 5, 17, 2, 5, 11] par tri comptage. Quelles cases de `occ` sont non nulles, et que devient T ?

---

`occ[2]` = 2, `occ[5]` = 3, `occ[11]` = 1 et `occ[17]` = 1, car chaque valeur est comptée à l'indice égal à sa valeur ; le total vaut 7. La reconstruction écrit 2 deux fois, 5 trois fois, 11 puis 17 : T = [2, 2, 5, 5, 5, 11, 17].
:::

::: retenir
Le tri comptage compte les occurrences de chaque valeur dans `occ[0..vmax]`, puis réécrit chaque valeur v exactement `occ[v]` fois, dans l'ordre des indices.
:::

> 🗡️ Pour reconnaître une trace de partition, cherche le pivot : valeurs ≤ pivot à gauche, valeurs > pivot à droite, pivot jamais déplacé avant l'échange final. Pour Hanoï, vérifie qu'aucun déplacement ne pose un grand disque sur un petit.

> 🏆 Porte franchie ! Tu sais couper un tableau autour d'un pivot, déplacer une tour de disques par récursion et trier par décompte. Prochaine arène : l'optimisation gloutonne et le retour sur trace.
