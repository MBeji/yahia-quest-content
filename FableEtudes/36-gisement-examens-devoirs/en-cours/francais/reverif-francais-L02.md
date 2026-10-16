# Re-vérification ciblée — gisement français 9ᵉ, lot L02

Commit `6b2f2d03` (`/home/user/wt-fr`), comparé à `fcea5969` (audit initial :
`audit-francais-L02.md`). Je n'ai lu que le diff et les fichiers, pas le journal de l'auteur.
Aucune écriture dans `content/` ni dans git.

Gates (moteur `/home/user/eng-svtses`) :
- `content:check` est vert ;
- `content:qa --strict` donne 0 erreur et 0 constat sur `french/` ;
- `content:tranche --chapters 01,02,11` : la clé n'est jamais strictement la plus longue (0 sur 139
  questions) ; les positions de clé se répartissent en 27/27/24/22 % ;
- une seule paire proche dans le lot, 02/06 Q1/Q2 à 0,76 (point 6).

## 1. Questions retouchées et voisines, re-résolues à l'aveugle

Toutes mes réponses égalent la clé.

| fichier | Q | ma réponse | clé | verdict |
|---|---|---|---|---|
| 02/06 (m007) | 2 | a | a | OK : la phrase officielle est rétablie |
| 02/06 | 5, 7 (voisines) | b, c | b, c | OK, mais indice de la plus courte (point 5) |
| 02/06 | 10 | b | b | réserve : distracteur a (point 2) |
| 02/07 (m008) | 1, 2, 3, 5 | b, a, c, a | idem | OK : rappels retirés, notions enseignées au cours |
| 02/07 | 8 (neuve) | b | b | réserve : étiquette de d (point 3) |
| 02/08 (m009) | 1, 4, 7, 9 | a, c, b, a | idem | OK |
| 02/09 (m010) | 2 | b | b | OK (point 1) |
| 11/06 (m011) | 1, 4, 5, 6 | a, b, a, c | idem | OK ; Q6 se lit seule |
| 01/06 (m012) | 1, 4, 5, 6, 7, 9 | a, a, d, b, c, d | idem | OK : plus aucun distracteur défendable, explications justes |
| 01/06 | 2, 3, 8 (voisines) | c, b, a | idem | OK |

## 2. Écarts déclarés par l'auteur

1. **m010 Q2, « Après avoir ranger » : accepté.** C'est une vraie faute d'élève (infinitif au lieu
   du participe), meilleure que « Après rangé ». La clé (62 caractères) n'est ni la plus longue ni
   la plus courte, et l'explication est juste.
2. **m007 Q10, « pour l'attendre » : accepté.** C'est un but bien construit, faux par le rapport
   logique ; il remplace utilement la double faute « pour qu'il l'attende ». Il reste un défaut,
   qui vient de **mon** correctif : l'option a (« de parler si vite à sa mère qu'il… ») a elle aussi
   la forme d'une conséquence d'intensité. Seul le sens l'exclut, et l'énoncé ne demande plus la
   fidélité au sens. Fin du prompt → `… on la veut ici liée à un degré d'intensité. Quelle phrase
   complexe convient, sans changer le sens ?` **(mineur M-1)**.
3. **m008 Q8, clé à égalité de longueur (104 = c) : accepté**, puisqu'elle n'est pas strictement la
   plus longue. En revanche, l'étiquette que **j'avais** proposée sur d (« qui j'ai changé… »),
   `fr.relative.qui-que-confondus`, n'est pas exacte. L'erreur n'oppose pas « qui » à « que » : le
   relatif devrait être « dont ». Il faut **retirer l'étiquette de d** et laisser l'option muette
   **(mineur M-2)**.
4. **m012 Q9 en d3 : accepté.** La rampe 2→3 reste monotone, et la mission compte déjà quatre d3
   (Q6–Q9), comme les autres missions d2 du lot.
5. **Clés strictement les plus courtes.** Le critère retenu est l'écart visible à l'écran, pas le
   simple compte.
   - **Rien d'exploitable dans :**
     - 02/06 Q4 (1 caractère sur 85) et Q6 (3 sur 86–91) ;
     - 11/06 Q1, Q2 et Q5 (1 caractère d'écart à chaque fois) ;
     - 02/08 Q3 et Q6, 02/09 Q4 : un mot de liaison seul, 1 à 5 caractères d'écart. La forme courte
       y est la règle même (« faute d'eau », « grâce à »).
     - En 11/06, choisir la plus courte ne donne que 3 réponses justes sur 8.
   - **Deux cas réels en 02/06 :**
     - **Q7** : écart de 6 caractères (55 contre 61 à 70). Il est inhérent : le groupe infinitif est
       plus court qu'une subordonnée.
     - **Q5** : écart de 3 à 8 caractères. Il donne avec Q4, Q6 et Q7 un motif « la plus courte » sur
       4 questions de 02/06 sur 10.

   **Correctifs (mineur M-3), longueurs vérifiées par script :**
   - **Q7, option d** → `Je travaille très dur à l'école afin devenir ingénieur.` (55, égale à la
     clé ; laisser l'option muette). Dans l'explication, remplacer
     `« de peur de » vise à éviter ce qu'on craint, ce qui contredit le désir de devenir ingénieur.`
     par `« afin devenir » oublie le « de » de la locution « afin de ».`
   - **Q5, option c** → `Le silence était dense qu'on entendait le souffle léger des respirations.`
     (73, clé 76). Retirer l'étiquette `fr.logique.rapport-logique-confondu`. L'explication devient :
     `Le degré « très dense » devient « si dense », et la conséquence s'ouvre par « que » : « si… que » + indicatif. Sans degré, « si bien que » ne relie que deux faits ; sans « si », le « que » n'a plus de degré auquel se rattacher et la phrase est fautive ; « Si… » pose une condition au lieu d'un résultat observé.`
     Ce changement allège aussi le gabarit « parce que renversé », répété en Q2, Q9 et Q10.

   Après ces deux correctifs, la clé de 02/06 n'est la plus courte qu'en Q4 et Q6, avec un écart
   imperceptible.
6. **Paire 02/06 Q1/Q2 (0,76) : acceptée comme parallèle voulu.** Le sujet de 2024 G pose la même
   phrase officielle avec deux consignes (a : cause ; b : conséquence d'intensité). Les clés diffèrent,
   et aucune explication ne livre l'autre clé. À justifier au rapport du lot.
7. **Exemples de cours voisins des questions : aucune clé livrée.**
   - « Il ne s'est pas levé », « pas beaucoup de temps », « Il n'a pas faim » et « pas de voiture »
     enseignent les règles que 01/06 Q6, Q8, Q9 et Q4/Q7 appliquent, avec d'autres verbes et d'autres
     noms. C'est le rôle du cours.
   - Les nouveaux exemples ne reprennent aucune phrase du lot (famille, chance, soucis, confiance,
     spectacle, endroit, peines, Ford).
   - « La chaise sur laquelle… » et « la maison près de laquelle… » ne figurent dans aucune option.
     « Il resta, car / donc… » non plus.
   - Le résumé du 02 cite « auquel, duquel… » comme liste de formes. Ce n'est la clé d'aucune question
     isolée, et les options de 02/07 contiennent toujours au moins deux formes composées.

## 3. Décisions du pilote : conséquences

- **Retrait de la concession.** m010 compte 7 questions (plage 6–12 respectée), et la rampe 2,2,2,2,3,3,3
  reste monotone. Ne restent que des distracteurs nommés « concession » (02/06 Q6 « Bien que… »,
  02/08 Q10 « malgré ») : la boîte 🚀 du cours en donne le sens, ce n'est pas un défaut.
- **Titres périmés (mineur M-4).** Ils annoncent des sessions qui ne sont plus dans la mission :
  - **m010** n'a plus que les sessions 2013, 2017, 2020 et 2022 →
    `🏛️ Examens 2013–2022 · le temps : subordonnée, groupe prépositionnel ou gérondif ⭐⭐⭐` ;
  - **m008** n'a aucune question de 2001 (sessions 2005–2018) →
    `🏛️ Examens 2005–2018 · le pronom relatif selon sa fonction : auquel, duquel, dont, à qui ⭐⭐⭐`.

  Les noms de fichiers portent les mêmes années, et celui de m010 contient encore « concession ».
  Comme rien n'est publié, on peut les renommer sans risque d'identifiant :
  - `07-examens-2005-2018-pronom-relatif-selon-la-fonction.json` ;
  - `09-examens-2013-2022-temps-subordonnee-ou-groupe.json`.

  Il faut alors mettre à jour les références dans
  `programmes-officiels/sources-externes/web-9eme-base-french/gisement.json`.
- **Famille « article gardé » non créée.** Les options de 01/06 Q4 et Q7 restent muettes ; c'est
  conforme.

## 4. Ajouts de cours

**Exactitude : juste.**
- Relatif composé : accord, six formes soudées, « à laquelle / de laquelle » non soudées,
  locution en « de » → jamais « dont ».
- « car » et « donc » sont des mots de liaison qui marquent la cause et la conséquence.
- Article → « de » devant le COD, avec les trois cas-limites (« être », adverbe de quantité, nom sans
  article).
- Le pronom reste à l'intérieur de la négation.

**Rendu (`renderLesson` / `renderSummary`, exécutés sur les fichiers) : correct.**
- La ligne « préposition + lequel » tombe dans le bon tableau, en 3 cellules.
- Les deux `::: propriete` sortent en blocs « Propriété », la ligne `> 💡` en bloc « Éclairage ».
- Les deux résumés affichent leurs ajouts dans la bonne carte (« Relative », « Cause », « Forme
  négative »).
- Comparaison avec `origin/main` : le découpage en paragraphes ligne par ligne dans les blocs est
  identique à l'existant, et l'ajout ne crée aucun soulignement brut (« _ » visible).

**Patron : mineur M-5.** Les deux notions neuves sont posées par une règle, sans exemple résolu à
étapes justifiées ni vérification, alors que le patron demande l'un et l'autre (é35 C-1, C-3).
Correctifs courts :
- **02, bloc `::: exemple choisir le pronom relatif en deux étapes`** : après l'étape 3, ajouter
  ```
  4. **Avec une chose après une préposition** : _« il s'assoit **sur** cette chaise »_ ; la
     préposition est _sur_ et l'antécédent une chose, donc **lequel**, accordé avec _chaise_
     (féminin singulier) : _« la chaise **sur laquelle** il s'assoit »_.
  ```
- **01, après le nouveau `::: propriete`** :
  ```
  ::: verifie
  Mets à la forme négative : « Elle mange des dattes. »

  ---

  « Elle **ne** mange **pas de** dattes. » _Des_ précède le COD _dattes_ : après _pas_, il devient _de_.
  :::
  ```

Ni l'un ni l'autre ne reprend une donnée du lot.

**Hors périmètre, pour l'orchestrateur.** Le moteur ne transforme pas en italique un passage
`_« … **gras** … »_` : les traits bas s'affichent tels quels. On en compte 45 dans le cours du 01 et 95
dans celui du 02, autant sur `origin/main` qu'après les ajouts. C'est un défaut préexistant du moteur ou
du corpus, sans lien avec ce lot. Les ajouts de l'auteur, sans traits bas, y échappent.

## 5. Résumé

- **Clés fausses : 0.**
- **Majeurs restants : 0.** Les sept défauts majeurs de l'audit sont corrigés (D-5 par retrait).
- **Mineurs restants : 5**, texte exact ci-dessus :
  - M-1 : 02/06 Q10, ajouter « sans changer le sens » ;
  - M-2 : 02/07 Q8, retirer l'étiquette de d ;
  - M-3 : 02/06 Q5 et Q7, deux options plus courtes contre l'indice de la plus courte ;
  - M-4 : années des titres et des noms de fichiers de m008 et m010 ;
  - M-5 : un exemple au 02 et une vérification au 01.
- **Écarts déclarés** : 1, 3, 4 et 6 acceptés ; 2 accepté avec M-1 ; 5 corrigé sur deux questions,
  rien d'exploitable sur les huit autres ; 7, aucune clé livrée.
- **Verdict : bon pour merge après les mineurs.** Ce sont des retouches de texte, sans re-résolution
  nécessaire : relancer `content:tranche` suffit.
