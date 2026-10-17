# Re-vérification — anglais 9ᵉ, lot L04 (m016–m021)

Base : commit `959fadfc` (branche `wip/gisement-anglais-9eme`, worktree `/home/user/wt-en`), contre l'audit
`audit-anglais-L04.md` (commit `420eda53`). Lu : le diff `420eda53..959fadfc` sur les six fichiers du lot, le
`cours.md`, le `resume.md` et le `chapter.json` du 09, et `content/misconceptions.json` ; le journal
`auteurs-notes/en-L04/CORRECTIONS.md` ; les fichiers hors lot 08/07 (L03) et 07/08 (L06) dans leur état actuel.
Aucune écriture dans `content/`, aucune opération git.

Moteur (`/home/user/eng-en`) :

- `content:check` : vert (1071 étiquettes) ;
- `content:qa:strict -- --subject english` : aucun signal ;
- `content:tranche --chapters 09` : 12/129 clés strictement les plus longues (les 8 cas de L04 sont ceux déjà
  acceptés, § 2.8 de l'audit) ; **21 paires proches, toutes avec `17-devoir`** (hors lot) : la paire 08/07 ↔ 09/11
  à 0,45 a disparu ; un seul groupe gabarit restant (§ 5) ;
- `lot-lint` : les 8 clés longues déjà acceptées et 6 avertissements de rampe (§ 4) ;
- rendu du 09 (`renderLesson` / `renderSummary`, `lang: "en"`, test vitest jetable dans le moteur, supprimé
  ensuite, `git status` du moteur propre) : la ligne sur les prépositions, les deux lignes du tableau, le
  paragraphe « However, / Besides, / Although » dans le bloc `propriete`, le `retenir` et les deux puces du résumé
  sortent en HTML propre (gras, italiques, tableau à trois colonnes).

## 1. Questions modifiées, re-résolues

| question | ma réponse | clé | verdict |
| --- | --- | --- | --- |
| m016 Q4 (énoncé « household chores teach children useful skills ») | for | a | OK, « look after » retiré de l'énoncé et de l'explication |
| m016 Q6 (énoncé « switch off unnecessary lights ») | for | d | OK, l'énoncé ne donne plus la clé ; explication de « about » juste |
| m016 Q11 (explication) | from | b | OK |
| m016 Q12 (énoncé « a creative girl who won a citywide poetry competition ») | of | c | OK, plus de « at » + âge |
| m017 Q1 (« Gilbert has got big plans. » ajouté) | However | a | OK, « Besides » tombe par le sens |
| m017 Q2 (explication) | While | b | OK |
| m017 Q9 (« Jim is a painter. ___ he isn't working today… ») | But | c | OK |
| m017 Q10 (parenthèse retirée) | Although | a | OK, « although » est maintenant au cours |
| m017 Q12 (contexte et citation coupés, explication) | so | a | OK, ni « have been » ni « is leaving » |
| m018 Q11 (citation coupée) | role | c | OK |
| m018 Q12 (2018 G : safe / shy / indifferent) | shy | b | OK, fidèle à la transcription, d2 |
| m019 Q1, Q9, Q10 (énoncés) | appariements inchangés | idem | OK, la note de 2001 dit « two lines » |
| m020 Q1 (f recevable, 4 sur 6) | a, c, e, f | idem | OK |
| m020 Q3 (« Which plan answers the task? ») | d | d | OK |
| m020 Q7 (consigne d'anonymat citée) | d | d | OK, l'option signée est maintenant indéfendable |
| m020 Q9 (étiquette retirée) | b | b | OK |
| m020 Q10 (sans « would », d2) | c, b, a, d | idem | OK, ordre unique |
| m021 Q1 (cadre complet) | c | c | OK |
| m021 Q2 (d et e remplacés) | a, c | idem | OK, quatre gaspillages plausibles et faux |
| m021 Q5 (colonne B réécrite) | l1-r2, l2-r4, l3-r1, l4-r3 | idem | OK, une seule bijection |
| m021 Q12 (consigne citée, d2) | a | a | OK |

**22 questions re-résolues. 0 clé fausse. Le critique et les 14 majeurs sont clos.** Les 11 mineurs sont appliqués
comme proposés, sauf la réserve R1 ci-dessous.

## 2. Cours du 09, résumé, `sources[]` : un défaut, et il vient de mon audit

Les textes appliqués sont ceux de l'audit, mot pour mot. Mais **la page 97 citée n'est pas celle du Student's
Book** : d'après la fiche programme, la « Word list p. 97 » (approve of, dispose of) est dans l'**Activity Book**
(Module 3 Lesson 5, « AB p. 89–97, … Word list p. 97 »). De plus, SB p. 99 est le **tableau du Module 5** et non la
Leçon 5 (SB p. 120–123). L'erreur vient de mon § 2.1, et l'auteur l'a recopiée. Défaut **mineur** (R1), à
corriger :

- `cours.md`, ligne sur les prépositions : remplacer `(Student's Book p. 6, p. 97, p. 99)` par
  `(Student's Book p. 6 and p. 99, Activity Book p. 97)` ;
- `chapter.json`, nouvelle ligne `sources[]` : remplacer par
  `Proceed with English — Student's Book 141906 & Activity Book 141907 (CNP), Module 1 plan (to look after) SB p. 6 ; Module 5 plan (I'm interested in) SB p. 99 ; Module 3 Lesson 5 Word list (approve of, dispose of) AB p. 97`.

R2 (mineur, même origine : mon audit plaçait « however » en SB p. 116) : les connecteurs ajoutés au cours n'ont
pas de ligne `sources[]`. « However » figure dans le Writing two de l'**AB p. 116** (Module 4 Lesson 4), les
connecteurs d'addition dans l'**AB p. 71** (Module 3 Lesson 1, A4). Ligne à ajouter :
`Proceed with English — Activity Book 141907 (CNP), Module 3 Lesson 1 A4 (linkers of addition) AB p. 71 ; Module 4 Lesson 4 Writing two (however) AB p. 116`.
« although » va au-delà du manuel (l'examen l'exige en 2009 G) : à déclarer dans la PR, comme prévu.

Le fond est correct :

- la ligne sur les prépositions est dans le bloc `propriete` de « Word meaning from context », et la puce du résumé
  la reflète ;
- les connecteurs sont présents dans le tableau, dans `propriete` et dans `retenir`, et la puce « Linkers » du
  résumé les reflète ;
- aucun exemple ne reprend une phrase d'examen.

## 3. Étiquette `english.prep.preposition-calquee`

- Elle est au registre avec les trois libellés de l'audit, sans changement.
- Elle est posée sur exactement les 7 options retenues : Q4 b with, Q5 a In, Q7 b from, Q10 b of et c on, Q11 a of,
  Q12 a with. Chacune est un distracteur, aucune n'est une clé.
- Q2 « of » et Q9 « with » restent muettes, comme demandé.
- Toutes les questions sont des QCM. Il n'existe aucun doublon avec une autre étiquette `english.*`. La famille
  couvre 6 questions, donc au moins 3.
- `content:check` lit le registre sans erreur.

**OK.**

## 4. Rampe (6 avertissements de `lot-lint`) : acceptable, rien à lisser

Le compilateur émet les questions **triées par difficulté, de façon stable**
(`src/shared/content/sql-builder.ts` l. 381–385 : `.sort((a, b) => difficulty(a) - difficulty(b) || a.i - b.i)`).
La route montre donc toujours les d2 puis les d3, et le donjon tire au hasard : l'ordre du fichier n'a aucun effet
visible. Les avertissements sont cosmétiques.

J'ai vérifié les fuites en avant dans l'ordre d'émission réel :

- m020 : Q2, Q3, Q6, Q7, Q8, Q9, Q10, puis Q1, Q4, Q5 ;
- m021 : Q1, Q3, Q4, Q5, Q7–Q10, Q12, puis Q2, Q6, Q11.

Aucune explication ne donne la clé d'une question émise après elle. L'explication de m021 Q5 (« the public bus has
the cheapest ticket ») ne tranche pas m021 Q6, qui porte sur « faster than » et sur la logique de la conclusion.

Si l'orchestrateur veut un fichier sans avertissement, il peut placer les questions d3 en fin de fichier dans
l'ordre d'émission ci-dessus, sans autre changement. Les fichiers ne sont pas encore publiés, donc aucun UUID n'est
en jeu. Ce n'est pas exigé.

Réserve R3 (mineur) sur les étages ajoutés au-delà de l'audit. L'auteur a aussi monté en d3 m020 Q4, m020 Q8,
m021 Q2 et m021 Q6 :

- m021 Q6 se justifie : double contrainte, forme du comparatif et logique de la conclusion.
- m021 Q2 se justifie : tout-ou-rien sur 6 énoncés, avec des gaspillages désormais plausibles.
- m020 Q4 est acceptable : le piège de la menace est réel.
- **m020 Q8 ne se justifie pas.** Seule la clé s'adresse aux lecteurs à l'impératif ; les autres sont une liste ou
  des comptes rendus au passé. Il faut la remettre en d2.

m020 garde alors trois d3 (Q1, Q4, Q5) et m021 trois (Q2, Q6, Q11). Les étages boss sont honnêtes.

## 5. Fuites, dans les deux sens

- **08/07 Q2 (L03)** cite maintenant « …children are capable of handling (much / more / most) than we may
  believe. » Le mot « At » n'y est plus et la clé « more » reste unique par « than ». **Fuite close.**
- **m024 Q9 (L06)** cite maintenant « …her ___ and has become an active member in her community. » Le mot
  « proud of » n'y est plus. La clé « choice » reste seule (un nom après « her »), et l'explication ne cite pas
  « proud ». **Fuite close.**
- **m017 Q9 vers m007 Q6** (« got ») : close. **m017 Q12 vers m006 Q12 et m007 Q8** (« is leaving », « have
  been ») : close, dans l'énoncé comme dans l'explication.
- **m018 Q11 vers m023 Q11** (« themselves ») : close. **m016 Q4 vers Q8**, **m016 Q12 vers Q5**, **m016 Q6** (sa
  propre clé) et **m019 Q1** (sa paire 1) : closes.
- Nouveau balayage, en 5-grammes et sur les phrases-clés, de tous les fichiers `english` de la branche (exercices
  et quiz) contre L04, dans les deux sens. Aucune nouvelle fuite. Les recoupements restants sont tous sans clé :
  - même texte d'examen avec d'autres blancs : m017 Q1 / 02/07 Q5 ; m018 Q2 / 02/07 Q1 ; m018 Q12 / 07/08 Q3,
    qui demande « advise », le mot « shy » étant absent de tout autre fichier ;
  - formules d'explication communes (« the verb stays in its base form ») ;
  - cadres de consigne. « look after » figure dans le quiz 09 publié, dans 09/07 et dans une explication de 04/07,
    mais c'est désormais une collocation **enseignée** par le cours 09 (nouvelle ligne) : c'est du renfort, pas une
    fuite.
- Gabarit restant **04/07 Q5 ↔ 09/15 Q1** (« Which of these points are sound arguments… ») : accepté comme
  archétype parallèle voulu (R3 du plan). Les sujets diffèrent, et le nombre de bonnes réponses aussi (3 sur 6
  contre 4 sur 6) : il ne se devine plus d'une mission à l'autre.

## 6. Verdict

- Clés fausses : 0. Critique : 0 restant. Majeurs : 0 restant.
- Mineurs restants : 3, tous des retouches de texte sans effet sur une clé.
  - **R1** : page 97 = AB, et SB p. 99 = tableau du Module 5, dans le cours et dans `sources[]`. L'erreur vient de
    mon audit.
  - **R2** : ligne `sources[]` à ajouter pour les connecteurs (AB p. 71, AB p. 116).
  - **R3** : m020 Q8 à remettre en d2.
- Étiquette : OK. Rampe : acceptable, aucun lissage requis. Fuites : toutes closes, y compris 08/07 et m024 Q9.

**Verdict : L04 prêt à livrer après les trois retouches mineures R1–R3** (aucune nouvelle re-vérification
nécessaire au-delà d'un `content:check`).

## Verdict du pilote (2026-10-17)

R1 (pages SB/AB du cours et de `sources[]`), R2 (ligne `sources[]` des connecteurs) et R3 (m020 Q8 en d2) appliqués par le pilote ; `content:check` vert. **L04 prêt à livrer.**
