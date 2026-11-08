# ⚔️ Les fichiers — faire survivre les données au programme

> 💡 «Une variable meurt avec le programme ; un fichier lui survit.»

Un tableau ou un enregistrement vit dans la mémoire : quand le programme s'arrête, tout disparaît. Un fichier range les données sur un support et les garde d'une exécution à l'autre. Huit notions, avec un fil rouge : les scores 12, 7, 15, 9, 11 des matchs d'un club de robotique, stockés dans un fichier d'entiers nommé `scores`. On suppose acquis les enregistrements (chapitre précédent : un fichier est typé par un enregistrement), les tableaux et les structures Pour, Tant que et Répéter.

## 🗄️ Qu'est-ce qu'un fichier ?

Le club note ses scores dans un tableau : 12, 7, 15, 9, 11. À la fermeture du programme, le tableau disparaît avec la mémoire, et la séance suivante repart de zéro.
Où écrire ces scores pour les retrouver demain, et comment le programme désigne-t-il chacun d'eux ?

::: definition
Un **fichier** est un ensemble structuré de données de même type, nommé et enregistré sur un support lisible par l'ordinateur (disque dur, clé USB, CD…). Il contient des valeurs (fichier de données), des caractères (fichier texte) ou des programmes.
Ses éléments se suivent et sont **numérotés à partir de 0**.
Le **pointeur de fichier** est un entier : le numéro de la position où se fera la prochaine lecture ou écriture. Dans un fichier vide, il vaut 0 et désigne déjà la fin.
:::

::: figure Le fichier des scores : cinq éléments numérotés de 0 à 4, le pointeur désigne l'élément de numéro 2 (valeur 15) et la case « fin » suit le dernier élément
<svg viewBox="0 0 400 104">
<title>Fichier de cinq scores 12, 7, 15, 9, 11 numérotés de 0 à 4, pointeur sur le numéro 2, case fin après le dernier élément</title>
<text x="168" y="14" font-size="12" text-anchor="middle" fill="#0f172a">pointeur = 2</text>
<polygon points="168,36 160,22 176,22" fill="#dc2626" stroke="#0f172a" stroke-width="1.2"/>
<rect x="20" y="40" width="56" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="48" y="63" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">12</text>
<text x="48" y="92" font-size="11" text-anchor="middle" fill="#0f172a">n° 0</text>
<rect x="80" y="40" width="56" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="108" y="63" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">7</text>
<text x="108" y="92" font-size="11" text-anchor="middle" fill="#0f172a">n° 1</text>
<rect x="140" y="40" width="56" height="36" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/>
<text x="168" y="63" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">15</text>
<text x="168" y="92" font-size="11" text-anchor="middle" fill="#0f172a">n° 2</text>
<rect x="200" y="40" width="56" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="228" y="63" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">9</text>
<text x="228" y="92" font-size="11" text-anchor="middle" fill="#0f172a">n° 3</text>
<rect x="260" y="40" width="56" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="288" y="63" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">11</text>
<text x="288" y="92" font-size="11" text-anchor="middle" fill="#0f172a">n° 4</text>
<rect x="320" y="40" width="56" height="36" fill="#ffffff" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="4 3"/>
<text x="348" y="63" font-size="12" text-anchor="middle" fill="#0f172a">fin</text>
</svg>
:::

Dans la figure, le pointeur vaut 2 : la prochaine lecture rendra 15, le troisième score, car le premier porte le numéro 0.

::: exemple Où est le pointeur après deux lectures ?

1. À l'ouverture, le pointeur vaut 0 : il désigne le premier élément, de numéro 0.
2. Une première lecture rend 12, puis avance le pointeur à 1, car chaque lecture avance d'une position.
3. Une seconde lecture rend 7, et le pointeur vaut 2.
4. La lecture suivante rendra 15, l'élément de numéro 2 : le troisième du fichier, pas le deuxième.

:::

::: piege
**Erreur : compter les éléments à partir de 1.** On lit « le pointeur vaut 2 » et l'on en conclut que l'élément pointé est le deuxième, donc 7. L'erreur tente parce que l'on compte « un, deux, trois » dans la vie courante. Mais le premier élément porte le numéro 0 : le numéro 2 est le troisième élément, 15. Un fichier de 5 éléments a les numéros 0 à 4 ; aucun élément n'a le numéro 5.
:::

::: propriete
Un fichier peut être organisé de deux façons.
**Organisation séquentielle** : on ne rejoint un enregistrement qu'en parcourant ceux qui le précèdent, les uns à la suite des autres.
**Organisation relative** (dite aussi directe) : les enregistrements sont contigus et identifiés chacun par un numéro d'ordre.
:::

::: verifie À toi : lire un numéro
Un fichier contient 4, 8, 15, 16, 23 et son pointeur vaut 3. Quelle valeur rend la prochaine lecture, et que vaut ensuite le pointeur ?

---

Les numéros vont de 0 à 4 : 4 porte le numéro 0, 8 le numéro 1, 15 le numéro 2 et 16 le numéro 3. La lecture rend donc 16, puis avance le pointeur à 4, qui désigne l'élément 23.
:::

::: retenir
Un fichier est un ensemble de données de même type sur un support ; ses éléments sont numérotés à partir de 0 et le pointeur est le numéro du prochain élément lu ou écrit.
:::

## ⚖️ Accès séquentiel ou accès direct ?

Pour écouter la quatrième chanson d'une cassette, il faut faire défiler les trois premières. Sur un CD, on tape 4 et le lecteur y saute.
Un fichier se comporte-t-il comme une cassette ou comme un CD ?

::: definition
**Accès séquentiel** : pour lire une information particulière, il faut lire toutes celles qui se trouvent avant elle.
**Accès direct** (dit aussi accès aléatoire) : on atteint l'information voulue en précisant son numéro d'emplacement, son numéro d'ordre.
:::

|                                         | Cassette                                 | CD audio             |
| --------------------------------------- | ---------------------------------------- | -------------------- |
| Type d'accès                            | séquentiel                               | direct               |
| Pour la 4ᵉ chanson                      | passer les 3 premières                   | demander la piste 4  |
| Pour l'élément de numéro i d'un fichier | lire les i éléments précédents, puis lui | préciser le numéro i |

La quatrième chanson est l'élément de numéro 3 : la cassette oblige à franchir les numéros 0, 1 et 2, le CD permet de demander directement le numéro 3.

::: exemple Atteindre la mesure de numéro 599

1. Un fichier contient 1000 mesures, numérotées de 0 à 999. La mesure de numéro 599 est précédée de 599 éléments (numéros 0 à 598).
2. En accès séquentiel, on lit ces 599 éléments, puis le suivant : 600 lectures.
3. En accès direct, on précise le numéro 599, puis on lit : une seule lecture.
4. Pour afficher les 1000 mesures, au contraire, les deux accès passent par chaque élément : le séquentiel suffit.

:::

::: piege
**Erreur : croire que le type d'accès est inscrit dans le fichier.** On dit « ce fichier est séquentiel, on ne pourra jamais lire son élément 599 sans lire les précédents ». L'erreur tente parce que le mot ressemble à une propriété du fichier. Mais l'accès est un choix du programme : selon les instructions qu'il emploie, le même fichier est parcouru depuis le début ou atteint directement par son numéro.
:::

::: propriete
Le programme choisit son accès selon le traitement.
**Séquentiel** : traiter tous les éléments dans l'ordre (afficher, compter, additionner).
**Direct** : atteindre ou modifier un élément dont on connaît le numéro.
Cas limite : pour traiter tous les éléments, l'accès direct n'apporte aucun gain, puisqu'il faut de toute façon passer par chacun.
:::

::: verifie À toi : compter les lectures
Un fichier contient 50 mesures. Combien de lectures faut-il, au minimum, pour obtenir la mesure de numéro 9 en accès séquentiel, puis en accès direct ?

---

La mesure de numéro 9 est précédée de 9 éléments (numéros 0 à 8). En accès séquentiel, il faut les lire tous, puis lire celle-ci : 10 lectures. En accès direct, on précise le numéro 9 et on lit : une seule lecture.
:::

::: retenir
En accès séquentiel on lit tout ce qui précède l'élément voulu ; en accès direct on donne son numéro d'ordre ; c'est le programme, et non le fichier, qui choisit.
:::

## 🏷️ Déclarer un fichier et l'associer à son nom

Le programme parle du fichier des scores sous le nom `scores`, mais le disque le connaît sous le nom `C:/Club/scores.dat`.
Comment le programme sait-il que `scores` est ce fichier, et quel type de données y met-on ?

::: definition
Un fichier a deux noms. Le **nom logique** (ou nom interne) est l'identificateur du fichier dans le programme. Le **nom physique** (ou nom externe) est son nom sur le support, avec son chemin et son extension (`.dat` pour un fichier de données).
**Associer** (Pascal : `Assign`) relie le nom logique au nom physique ; on trouve aussi **Assigner**.
Un type fichier se déclare par `Fichier de type_composants` (Pascal : `File Of`) : tous les composants ont le même type.
:::

En algorithmique, on déclare le type puis l'objet :

```
Type
    F_Entier = Fichier de Entier
```

| Objet  | Type / Nature | Rôle                       |
| ------ | ------------- | -------------------------- |
| scores | F_Entier      | Fichier des scores du club |

En Pascal :

```pascal
Type
  F_Entier = File Of Integer;
Var
  scores : F_Entier;
```

L'association s'écrit une seule fois :

```
Associer (scores, "C:/Club/scores.dat")
```

```pascal
Assign(scores, 'C:/Club/scores.dat');
```

|                | Nom logique                                 | Nom physique                  |
| -------------- | ------------------------------------------- | ----------------------------- |
| Dans l'exemple | scores                                      | C:/Club/scores.dat            |
| Où il vit      | dans le programme                           | sur le disque                 |
| Où on l'écrit  | dans toutes les instructions sur le fichier | une seule fois, dans Associer |

Après l'association, toutes les instructions utilisent `scores` ; le chemin n'apparaît plus. Le manuel sépare les dossiers du chemin par une barre oblique inverse ; Pascal sous Windows accepte aussi la barre oblique simple, que ce cours emploie pour des raisons de notation.

::: exemple Un fichier de joueurs

1. Le club veut garder pour chaque joueur son nom et ses points, deux types différents. Les composants d'un fichier ont tous le même type : on les regroupe dans un enregistrement `Joueur`.
2. Le type fichier a pour composants des `Joueur` : `F_Joueur = File Of Joueur`.
3. On déclare l'objet `joueurs` de type `F_Joueur`, puis on l'associe à `C:/Club/joueurs.dat`.

:::

```pascal
Program Declaration_Joueurs;
Type
  Joueur = Record
    nom : String[20];
    points : Integer;
  End;
  F_Joueur = File Of Joueur;
Var
  joueurs : F_Joueur;
Begin
  Assign(joueurs, 'C:/Club/joueurs.dat');
End.
```

::: piege
**Erreur : croire que Associer crée ou ouvre le fichier.** On écrit `Assign(joueurs, ...)` puis directement `Write(joueurs, j)`. L'erreur tente parce que le nom du fichier vient d'être donné. Mais Associer relie seulement deux noms : rien n'est créé sur le disque, rien n'est ouvert. L'écriture échoue avec une erreur d'exécution tant que le programme n'a pas appelé Recréer ou Ouvrir (section suivante).
:::

::: methode
Pour préparer un fichier :

1. déclarer le type fichier (`File Of` + le type des composants) ;
2. déclarer l'objet de ce type, c'est son nom logique ;
3. l'associer à son nom physique, avant toute ouverture.

Cas limite : si un dossier du chemin n'existe pas, l'ouverture provoque une erreur d'exécution (Runtime error).
:::

::: verifie À toi : un fichier de réels
Déclarer en Pascal un fichier de réels de nom logique `temp`, puis l'associer à `C:/Meteo/temp.dat`.

---

Les composants sont des réels : `Type F_Reel = File Of Real;`. On déclare l'objet `Var temp : F_Reel;`, c'est le nom logique. Puis `Assign(temp, 'C:/Meteo/temp.dat');` relie ce nom logique au nom physique, une seule fois, avant d'ouvrir le fichier.
:::

::: retenir
Un type fichier se déclare par `File Of` suivi du type des composants ; Associer relie le nom logique du programme au nom physique du disque, sans rien ouvrir.
:::

## ✍️ Ouvrir, écrire, lire, fermer

Le club veut enregistrer 12, 7, 15 ce soir et les relire demain.
Entre l'association et la fin du programme, quelles instructions faut-il, et dans quel ordre ?

::: definition
**Recréer** (Pascal : `Rewrite`) ouvre un fichier en effaçant son contenu ; s'il n'existe pas, il est créé.
**Ouvrir** (Pascal : `Reset`) ouvre un fichier existant et remet son pointeur à zéro.
**Ecrire** (`Write`) et **Lire** (`Read`) agissent sur l'élément désigné par le pointeur, puis avancent le pointeur d'une position.
**Fermer** (`Close`) ferme le fichier.
:::

| Algorithmique | Pascal        |
| ------------- | ------------- |
| Recréer (f)   | Rewrite (f);  |
| Ouvrir (f)    | Reset (f);    |
| Ecrire (f, v) | Write (f, v); |
| Lire (f, v)   | Read (f, v);  |
| Fermer (f)    | Close (f);    |

Voici le traitement en algorithmique, puis en Pascal.

```
Associer (scores, "C:/Club/scores.dat")
Recréer (scores)
v ← 12
Ecrire (scores, v)
v ← 7
Ecrire (scores, v)
v ← 15
Ecrire (scores, v)
Fermer (scores)
Ouvrir (scores)
Pour i de 1 à 3 Faire
    Lire (scores, v)
    Ecrire (v)
Fin Pour
Fermer (scores)
```

```pascal
Program Scores_Club;
Type
  F_Entier = File Of Integer;
Var
  scores : F_Entier;
  v, i : Integer;
Begin
  Assign(scores, 'C:/Club/scores.dat');
  Rewrite(scores);
  v := 12;
  Write(scores, v);
  v := 7;
  Write(scores, v);
  v := 15;
  Write(scores, v);
  Close(scores);
  Reset(scores);
  For i := 1 To 3 Do
  Begin
    Read(scores, v);
    WriteLn(v);
  End;
  Close(scores);
End.
```

| Après l'instruction | Pointeur | Contenu du fichier |
| ------------------- | -------- | ------------------ |
| Rewrite             | 0        | vide               |
| Write de 12         | 1        | 12                 |
| Write de 7          | 2        | 12, 7              |
| Write de 15         | 3        | 12, 7, 15          |
| Close puis Reset    | 0        | 12, 7, 15          |
| Read (v vaut 12)    | 1        | 12, 7, 15          |

La colonne Pointeur compte les positions déjà franchies : après trois écritures elle vaut 3, et elle revient à 0 à la réouverture.

::: exemple Écrire puis relire les trois scores

1. `Rewrite` crée le fichier, qui n'existait pas : il est vide et le pointeur vaut 0.
2. Chaque `Write` place la valeur à la position du pointeur, puis l'avance : après trois écritures, le fichier contient 12, 7, 15 et le pointeur vaut 3.
3. `Close` ferme le fichier ; `Reset` le rouvre et remet le pointeur à 0, ce qui permet de lire depuis le premier élément.
4. Les trois `Read` rendent 12, 7, 15, dans l'ordre où ils ont été écrits, et le programme affiche ces trois lignes.

:::

::: piege
**Erreur : relire sans rouvrir.** Après les trois `Write`, on écrit `Read(scores, v)` pour récupérer 12. L'erreur tente parce que 12 vient d'être écrit et semble « sous la main ». Mais le pointeur vaut 3 : il est à la fin, et la lecture demande un élément qui n'existe pas (erreur d'exécution). Il faut fermer, puis ouvrir avec `Reset`, qui remet le pointeur à 0.
:::

::: methode
Un traitement sur fichier suit quatre étapes, dans cet ordre : **Associer**, **Ouvrir** ou **Recréer**, **Lire** ou **Ecrire**, **Fermer**.
Recréer sert à écrire un fichier neuf ; Ouvrir sert à lire ou à modifier un fichier qui existe.
Cas limite : Recréer sur un fichier qui existe déjà détruit son contenu ; on ne l'emploie donc pas pour poursuivre un fichier déjà rempli.
:::

::: verifie À toi : effet d'un Recréer
Le fichier `scores` contient 12, 7, 15. On exécute `Reset(scores)`, deux `Read`, `Close(scores)`, puis `Rewrite(scores)` et `Close(scores)`. Que contient le fichier à la fin ?

---

`Reset` et les deux `Read` ne modifient rien : ce sont des lectures. Mais `Rewrite` ouvre le fichier en effaçant son contenu : après lui, le fichier est vide, et `Close` l'enregistre vide. Les trois scores sont perdus.
:::

::: retenir
On associe, on ouvre (Recréer efface, Ouvrir remet le pointeur à 0), on lit ou on écrit en avançant le pointeur, puis on ferme.
:::

## 🔁 Parcourir un fichier de taille inconnue

Combien de scores atteignent au moins 10 dans `scores` ? Le club ne sait pas combien de matchs sont enregistrés, et le fichier peut même être vide.
Comment une boucle sait-elle qu'elle est arrivée au bout ?

::: definition
**Fin_fichier** (Pascal : `Eof`, pour end of file) est une fonction booléenne : elle retourne VRAI si la fin du fichier est atteinte, c'est-à-dire si le pointeur est placé après le dernier élément.
:::

| Pointeur | Fin_fichier (scores) | Action              |
| -------- | -------------------- | ------------------- |
| 0        | Faux                 | lire 12             |
| 1        | Faux                 | lire 7              |
| 2        | Faux                 | lire 15             |
| 3        | Vrai                 | sortir de la boucle |

Le fichier a trois éléments : Fin_fichier devient vrai quand le pointeur atteint 3, c'est-à-dire juste après la dernière lecture.

```
Associer (scores, "C:/Club/scores.dat")
Ouvrir (scores)
nb ← 0
Tant que Non Fin_fichier (scores) Faire
    Lire (scores, v)
    Si v ≥ 10 Alors
        nb ← nb + 1
    Fin Si
Fin Tant que
Fermer (scores)
Ecrire (nb)
```

```pascal
Program Compter_Bons_Scores;
Type
  F_Entier = File Of Integer;
Var
  scores : F_Entier;
  v, nb : Integer;
Begin
  Assign(scores, 'C:/Club/scores.dat');
  Reset(scores);
  nb := 0;
  While Not Eof(scores) Do
  Begin
    Read(scores, v);
    If v >= 10 Then
      nb := nb + 1;
  End;
  Close(scores);
  WriteLn(nb);
End.
```

::: exemple Compter les scores d'au moins 10

1. `nb` vaut 0 avant la boucle : c'est le compteur, qui part de zéro.
2. Le test de fin vient avant la première lecture : si le fichier est vide, la boucle ne s'exécute pas et `nb` reste 0.
3. Chaque tour lit un élément et avance le pointeur : la condition finit donc par devenir fausse.
4. Pour 12, 7, 15 : 12 ≥ 10 donne nb = 1, 7 ne compte pas, 15 ≥ 10 donne nb = 2 ; le pointeur vaut 3, la boucle s'arrête et le programme affiche 2.

:::

::: piege
**Erreur : lire avant de tester la fin.** On écrit `Répéter Lire (scores, v) … Jusqu'à Fin_fichier (scores)`. L'erreur tente parce que la boucle Répéter est la plus naturelle pour « lire jusqu'au bout ». Mais sur un fichier vide le premier `Lire` demande un élément inexistant : erreur d'exécution. Avec `Tant que Non Fin_fichier`, le test passe avant toute lecture.
:::

Reste le cas d'un fichier qui n'existe pas encore : `Reset` sur un fichier absent provoque une erreur d'exécution, car par défaut la directive `{$I+}` fait surveiller les entrées-sorties par Pascal.

::: methode Ouvrir un fichier qui existe peut-être

1. `{$I-}` : le programme gère lui-même l'erreur d'entrée-sortie, au lieu de s'arrêter.
2. `Reset` essaie d'ouvrir le fichier.
3. `IOResult` (Input Output Result) vaut 0 si la dernière opération a réussi, une autre valeur sinon.
4. Si `IOResult <> 0`, le fichier est absent : `Rewrite` le crée vide.
5. `{$I+}` rétablit la surveillance par défaut.

:::

```pascal
Assign(scores, 'C:/Club/scores.dat');
{$I-}
Reset(scores);
If IOResult <> 0 Then
  Rewrite(scores);
{$I+}
```

Cas limite : un fichier créé ainsi est vide, donc `Fin_fichier` est vrai dès l'ouverture.

::: verifie À toi : additionner les éléments
Écrire la boucle qui calcule la somme des éléments du fichier d'entiers `scores`, qui peut être vide. Que vaut la somme dans ce cas ?

---

On initialise `somme ← 0`, puis `Tant que Non Fin_fichier (scores) Faire`, on lit `v` et on ajoute `somme ← somme + v`. Le test passe avant chaque lecture, donc sur un fichier vide la boucle ne s'exécute pas et la somme reste 0.
:::

::: retenir
On parcourt un fichier de taille inconnue par `Tant que Non Fin_fichier (f)` : le test précède la lecture, ce qui couvre aussi le fichier vide.
:::

## 📍 Accès direct : Pointer, Taille_fichier, Position_fichier

Le juge corrige le quatrième score : 9 devient 14. Relire les trois premiers scores serait inutile.
Comment aller droit à un élément dont on connaît le numéro, et comment éviter de dépasser la fin ?

::: definition
**Pointer** (Pascal : `Seek`) place le pointeur sur l'élément de numéro donné : `Pointer (f, n)`. Pour accéder au n-ième élément, on pointe l'élément n − 1.
**Taille_fichier** (Pascal : `FileSize`) donne le nombre d'éléments du fichier.
**Position_fichier** (Pascal : `FilePos`) donne le numéro de l'élément sur lequel se trouve le pointeur.
:::

::: figure Pointer (scores, 3) place le pointeur sur l'élément de numéro 3, valeur 9 ; la taille du fichier est 5, donc les numéros valides vont de 0 à 4
<svg viewBox="0 0 400 150">
<title>Pointer (scores, 3) place le pointeur sur l'élément de numéro 3, valeur 9 ; Taille_fichier vaut 5 et les numéros valides vont de 0 à 4</title>
<text x="228" y="14" font-size="12" text-anchor="middle" fill="#0f172a">Pointer (scores, 3)</text>
<polygon points="228,36 220,22 236,22" fill="#dc2626" stroke="#0f172a" stroke-width="1.2"/>
<rect x="20" y="40" width="56" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="48" y="63" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">12</text>
<text x="48" y="92" font-size="11" text-anchor="middle" fill="#0f172a">n° 0</text>
<rect x="80" y="40" width="56" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="108" y="63" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">7</text>
<text x="108" y="92" font-size="11" text-anchor="middle" fill="#0f172a">n° 1</text>
<rect x="140" y="40" width="56" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="168" y="63" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">15</text>
<text x="168" y="92" font-size="11" text-anchor="middle" fill="#0f172a">n° 2</text>
<rect x="200" y="40" width="56" height="36" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/>
<text x="228" y="63" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">9</text>
<text x="228" y="92" font-size="11" text-anchor="middle" fill="#0f172a">n° 3</text>
<rect x="260" y="40" width="56" height="36" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.6"/>
<text x="288" y="63" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">11</text>
<text x="288" y="92" font-size="11" text-anchor="middle" fill="#0f172a">n° 4</text>
<rect x="320" y="40" width="56" height="36" fill="#ffffff" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="4 3"/>
<text x="348" y="63" font-size="12" text-anchor="middle" fill="#0f172a">fin</text>
<line x1="20" y1="106" x2="316" y2="106" stroke="#0f172a" stroke-width="1.4"/>
<line x1="20" y1="100" x2="20" y2="112" stroke="#0f172a" stroke-width="1.4"/>
<line x1="316" y1="100" x2="316" y2="112" stroke="#0f172a" stroke-width="1.4"/>
<text x="168" y="127" font-size="12" text-anchor="middle" fill="#0f172a">Taille_fichier (scores) = 5</text>
<text x="168" y="144" font-size="12" text-anchor="middle" fill="#0f172a">numéros valides : 0 à 4</text>
</svg>
:::

Dans la figure, le quatrième score est l'élément de numéro 3, et la taille 5 est le nombre de cases, pas le dernier numéro.

```
Associer (scores, "C:/Club/scores.dat")
Ouvrir (scores)
Pointer (scores, 3)
v ← 14
Ecrire (scores, v)
Fermer (scores)
```

```pascal
Program Corriger_Score;
Type
  F_Entier = File Of Integer;
Var
  scores : F_Entier;
  v : Integer;
Begin
  Assign(scores, 'C:/Club/scores.dat');
  Reset(scores);
  Seek(scores, 3);
  v := 14;
  Write(scores, v);
  Close(scores);
End.
```

::: exemple Corriger le quatrième score

1. `Reset` ouvre le fichier : le pointeur vaut 0.
2. Le quatrième score a le numéro 3 : `Seek(scores, 3)` place le pointeur sur 9.
3. `Write` remplace l'élément pointé, il n'insère rien ; puis le pointeur avance : `FilePos(scores)` vaut 4.
4. Le fichier contient 12, 7, 15, 14, 11 ; sa taille vaut toujours 5.

:::

Pour ajouter un score à la fin, on se place juste après le dernier élément.

```
Associer (scores, "C:/Club/scores.dat")
Ouvrir (scores)
Pointer (scores, Taille_fichier (scores))
v ← 17
Ecrire (scores, v)
Fermer (scores)
```

```pascal
Program Ajouter_Score;
Type
  F_Entier = File Of Integer;
Var
  scores : F_Entier;
  v : Integer;
Begin
  Assign(scores, 'C:/Club/scores.dat');
  Reset(scores);
  Seek(scores, FileSize(scores));
  v := 17;
  Write(scores, v);
  Close(scores);
End.
```

::: exemple Ajouter un score à la fin

1. `FileSize(scores)` vaut 5 : les éléments occupent les numéros 0 à 4.
2. `Seek(scores, 5)` place le pointeur juste après le dernier élément, sur la fin du fichier.
3. `Write` crée alors l'élément de numéro 5 : le fichier contient 12, 7, 15, 9, 11, 17 et sa taille vaut 6.

:::

::: piege
**Erreur : valider un numéro avec OU.** Pour contrôler un numéro `num` saisi, on écrit `Jusqu'à (num ≥ 0) OU (num < Taille_fichier (scores))`. L'erreur tente parce que « plus grand que 0 ou plus petit que la taille » ressemble à la phrase que l'on dit. Mais avec OU, `num = 7` est accepté (7 ≥ 0) et `num = −3` aussi (−3 < 5) : la condition est toujours vraie. Il faut les deux exigences à la fois, donc ET.
:::

::: propriete
Un numéro `num` désigne un élément existant si et seulement si `(num ≥ 0) ET (num < Taille_fichier (f))`. Le programmeur doit faire ce contrôle : le fichier ne l'impose pas.
Pour ajouter à la fin, on pointe `Taille_fichier (f)`.
Cas limite : sur un fichier vide, la taille vaut 0, donc aucun numéro n'est valide pour lire ; le numéro 0, égal à la taille, sert à écrire le premier élément.
:::

::: verifie À toi : suivre le pointeur
Le fichier `scores` contient 12, 7, 15, 9, 11. On exécute `Reset(scores)`, `Seek(scores, 2)`, `Read(scores, v)`. Que valent `v` et `FilePos(scores)` ?

---

Le numéro 2 désigne le troisième élément : 15, donc `v` vaut 15. `Read` avance ensuite le pointeur d'une position : `FilePos(scores)` vaut 3.
:::

::: retenir
Pointer place le pointeur sur un numéro d'ordre, Taille_fichier compte les éléments ; un numéro est valide s'il est supérieur ou égal à 0 ET strictement inférieur à la taille.
:::

## 🧹 Effacer, renommer, tronquer

En fin de saison, le club archive `scores.dat` sous le nom `saison1.dat`, en ne gardant que les trois premiers matchs.
Quelles instructions agissent sur le fichier lui-même plutôt que sur ses éléments ?

::: definition
**Effacer** (Pascal : `Erase`) supprime le fichier du support.
**Renommer** (Pascal : `Rename`) change le nom physique du fichier ; le fichier doit être fermé avant.
**Tronquer** (Pascal : `Truncate`) coupe le fichier à la position courante du pointeur : seuls restent les éléments situés avant le pointeur. Si le pointeur vaut p, il reste p éléments, de numéros 0 à p − 1.
:::

| Numéro                                               | 0     | 1     | 2     | 3     | 4     |
| ---------------------------------------------------- | ----- | ----- | ----- | ----- | ----- |
| Valeur                                               | 12    | 7     | 15    | 9     | 11    |
| Après `Pointer (scores, 3)` puis `Tronquer (scores)` | gardé | gardé | gardé | perdu | perdu |

Le pointeur vaut 3 : les trois éléments des numéros 0, 1 et 2 sont gardés, et ceux des numéros 3 et 4 disparaissent.

```
Associer (scores, "C:/Club/scores.dat")
Ouvrir (scores)
Pointer (scores, 3)
Tronquer (scores)
Fermer (scores)
Renommer (scores, "C:/Club/saison1.dat")
```

```pascal
Program Archiver_Saison;
Type
  F_Entier = File Of Integer;
Var
  scores : F_Entier;
Begin
  Assign(scores, 'C:/Club/scores.dat');
  Reset(scores);
  Seek(scores, 3);
  Truncate(scores);
  Close(scores);
  Rename(scores, 'C:/Club/saison1.dat');
End.
```

::: exemple Archiver les trois premiers matchs

1. `Reset` ouvre le fichier des cinq scores.
2. `Seek(scores, 3)` place le pointeur sur le numéro 3 : tout ce qui est avant est à garder.
3. `Truncate` coupe à cet endroit : il reste 12, 7, 15 et la taille passe de 5 à 3.
4. `Close` précède `Rename`, car on ne renomme qu'un fichier fermé ; ensuite `saison1.dat` contient 12, 7, 15.

:::

::: piege
**Erreur : croire que Tronquer ne retire que l'élément pointé.** On pense que `Pointer (scores, 3)` puis `Tronquer` supprime le 9 seul et qu'il reste 12, 7, 15, 11. L'erreur tente parce que l'on vient de désigner un seul élément. Mais Tronquer coupe à partir de l'élément pointé, inclus : le 9 et le 11 disparaissent, il reste 12, 7, 15.
:::

::: propriete
Effacer supprime le fichier du support et ne se rattrape pas.
Renommer exige un fichier fermé.
Tronquer garde exactement les p premiers éléments, p étant la position du pointeur. Le manuel dit : tout ce qui est au-delà du pointeur est perdu ; le pointeur se trouvant devant l'élément de numéro p, cet élément est perdu lui aussi.
Ces instructions valent aussi bien en accès séquentiel qu'en accès direct.
Cas limites : `Pointer (f, 0)` puis Tronquer vide le fichier ; `Pointer (f, Taille_fichier (f))` puis Tronquer n'enlève rien.
:::

::: verifie À toi : tronquer à une position
Un fichier de 10 éléments (numéros 0 à 9) est ouvert par `Reset`. On exécute `Seek(f, 6)` puis `Truncate(f)`. Quels éléments restent, et que vaut `FileSize(f)` ?

---

Le pointeur vaut 6 : Truncate garde les éléments situés avant lui, donc les numéros 0 à 5, soit 6 éléments. Les éléments des numéros 6 à 9 sont perdus et `FileSize(f)` vaut 6.
:::

::: retenir
Effacer supprime le fichier, Renommer change son nom physique (fichier fermé), Tronquer ne garde que les éléments situés avant le pointeur.
:::

## 📄 Les fichiers texte

Le robot du club tient un journal de bord : une ligne par match, lisible dans un éditeur de texte. Ce ne sont plus des entiers, mais des lignes de caractères.
Comment écrire et relire un fichier fait de lignes ?

::: definition
Un **fichier texte** ne contient qu'une suite de caractères ; l'espace et le retour à la ligne sont des caractères comme les autres. Chaque ligne se termine par le caractère retour chariot (CR) et le texte par la marque de fin de texte (CTRL-Z).
Il se déclare par le mot réservé `Text` (en algorithmique, la nature `Texte`). On l'ouvre en lecture par Ouvrir (`Reset`) et en écriture par Recréer (`Rewrite`).
:::

| Algorithmique        | Pascal              | Rôle                                                                   |
| -------------------- | ------------------- | ---------------------------------------------------------------------- |
| Fin_ligne (f)        | EoLn (f);           | VRAI si l'on est sur la fin de la ligne courante                       |
| Ajouter (f)          | Append (f);         | ouvre le fichier et place le pointeur à la fin : on ne peut qu'ajouter |
| Lire_nl (f, ligne)   | ReadLn (f, ligne);  | lit une ligne, puis pointe la ligne suivante                           |
| Ecrire_nl (f, ligne) | WriteLn (f, ligne); | écrit la ligne, puis la marque de fin de ligne                         |

```
Associer (f, "C:/Club/journal.txt")
Recréer (f)
ligne ← "Match 1 : victoire"
Ecrire_nl (f, ligne)
ligne ← "Match 2 : nul"
Ecrire_nl (f, ligne)
Fermer (f)
Ouvrir (f)
Tant que Non Fin_fichier (f) Faire
    Lire_nl (f, ligne)
    Ecrire (ligne)
Fin Tant que
Fermer (f)
```

```pascal
Program Journal;
Var
  f : Text;
  ligne : String;
Begin
  Assign(f, 'C:/Club/journal.txt');
  Rewrite(f);
  ligne := 'Match 1 : victoire';
  WriteLn(f, ligne);
  ligne := 'Match 2 : nul';
  WriteLn(f, ligne);
  Close(f);
  Reset(f);
  While Not Eof(f) Do
  Begin
    ReadLn(f, ligne);
    WriteLn(ligne);
  End;
  Close(f);
End.
```

::: exemple Écrire puis relire le journal

1. `Rewrite` crée le fichier vide ; chaque `WriteLn` écrit une ligne puis la marque de fin de ligne : deux appels, deux lignes.
2. `Close` puis `Reset` rouvrent le fichier en lecture, pointeur au début de la première ligne.
3. Tant que `Eof` est faux, `ReadLn` lit une ligne entière dans `ligne` et pointe le début de la suivante.
4. L'écran affiche `Match 1 : victoire` puis `Match 2 : nul` ; `Eof` devient vrai après la dernière ligne.

:::

::: exemple Ajouter un match au journal

1. `Append(f)` ouvre le fichier existant et place le pointeur à sa fin : les deux lignes sont conservées.
2. `WriteLn(f, 'Match 3 : victoire')` écrit une troisième ligne après elles.
3. `Close(f)` termine : le journal contient trois lignes. Avec `Rewrite` à la place d'`Append`, les deux premières auraient été effacées.

:::

```pascal
Program Ajouter_Match;
Var
  f : Text;
Begin
  Assign(f, 'C:/Club/journal.txt');
  Append(f);
  WriteLn(f, 'Match 3 : victoire');
  Close(f);
End.
```

::: piege
**Erreur : prendre Fin_ligne pour Fin_fichier.** Pour lire tout le journal caractère par caractère, on écrit `Tant que Non Fin_ligne (f) Faire Lire (f, c)`. L'erreur tente parce que les deux fonctions parlent de « fin ». Mais Fin_ligne ne teste que la ligne courante : la boucle s'arrête à la fin de la première ligne. Pour parcourir tout le fichier, le test reste `Non Fin_fichier (f)`.
:::

::: propriete
On traite un fichier texte ligne par ligne avec Lire_nl et Ecrire_nl.
Ouvrir donne un fichier en lecture, Recréer un fichier en écriture ; Ajouter n'autorise que l'ajout en fin.
Cas limite : Position_fichier (`FilePos`) ne s'applique pas à un fichier texte.
:::

::: verifie À toi : ajouter sans effacer
Le journal contient deux lignes. On exécute `Append(f)`, `WriteLn(f, 'Match 3 : nul')`, `Close(f)`. Que contient-il ? Et si l'on avait écrit `Rewrite(f)` à la place d'`Append(f)` ?

---

`Append` place le pointeur à la fin sans rien effacer : le journal contient les deux lignes d'origine, puis `Match 3 : nul`, soit trois lignes. Avec `Rewrite`, le fichier est effacé à l'ouverture : il ne resterait que `Match 3 : nul`.
:::

::: retenir
Un fichier texte est une suite de lignes lues par Lire_nl et écrites par Ecrire_nl ; Ajouter écrit à la suite sans rien effacer, et Fin_ligne ne dit rien de la fin du fichier.
:::

> 🏆 Tu sais maintenant faire vivre des données au-delà du programme : déclarer, ouvrir, lire, écrire, atteindre un élément et gérer le fichier lui-même. Prochaine étape : appeler ces fichiers depuis des algorithmes de plus en plus ambitieux.
