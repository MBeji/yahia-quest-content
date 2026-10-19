# Notes de l'auteur — lot B2 (`07`–`12`)

> Écrites au fil de l'eau. Pour chaque chapitre : table des écarts, puis ce qui a été fait.
> Convention de jalon : les questions ajoutées sont **en fin de fichier** avec une `difficulty` ≥ au maximum du fichier
> (les identifiants de question dérivent du rang après tri par difficulté : rien d'existant ne se décale).

## 07-criteres-divisibilite (leçons 25–26, ص 70–77)

### Table des écarts (fiche ↔ chapitre servi)

| # | écart | où |
| - | ----- | -- |
| 1 | Cours : **complet** vis-à-vis de la fiche (2, 5, 10, 3, 9, 9 ⇒ 3, combinaisons, chiffre manquant, baisse/hausse extrêmes, **reste sans division**) — aucune section à ajouter, aucune règle fautive | cours.md |
| 2 | Aucune donnée fautive reprise ; errata n° 25–28 (ص 70–72 : « قسمته على 5 », « بين 100 000 », « 1310 ») : le chapitre n'emploie aucune de ces données (les reprises ci-dessous citent les formes corrigées) | — |
| 3 | **Notion de la fiche non exercée** : le **reste lu sans division** (L25 ex 2, 5 ; L26 ex 2, 7) — ni quiz ni exercice ne le demandaient | exercices |
| 4 | **Non exercé** : chiffre manquant avec **toutes les solutions** / nombre de solutions (L25 ex 4, L26 ex 4–5) ; plus grand / plus petit nombre de n chiffres (L25 ex 7, L26 ex 6, 8) ; arrangement de 4 chiffres (L25 ex 9) ; multiples communs de 2 et 5 entre deux bornes (L25 ex 6) ; âge du père (L25 ex 10) | exercices |
| 5 | **Question à méta-option** : « لا يمكن المعرفة » (01-pratique Q6, 03-revision Q2, Q5) et « نعم على 2 فقط » (incohérent) | exercices |
| 6 | **Clé strictement la plus longue** : quiz Q3 (« نعم لأنّ مجموع أرقامه 9 ») ; 02-boss Q2 | quiz, 02 |
| 7 | **Étiquette inexacte** : 02-boss Q3 (27, 81, 18) porte `critere-divisibilite-mal-choisi` alors que l'erreur est de lire « ÷ 3 » sans voir « mais pas ÷ 9 » — laissé muet | 02 |
| 8 | Options numériques non triées (01 Q5, 02 Q6) ; « 1 035 » groupé alors que le cours/manuel écrivent 1035 | 01, 02, 03 |
| 9 | Question quasi jumelle du quiz (234 / 423, mêmes chiffres) | quiz Q3 |

### Fait (07)

- `cours.md`, `resume.md` : inchangés (déjà au patron, tous les points de la fiche couverts, valeurs recalculées une à une). `chapter.json` : `sources[]` complété (fiche §2 quinquies, §3.2, §4, §6.1).
- quiz : Q3 réécrite (clé n'est plus la plus longue, nombre 513 ≠ 234) ; +Q6 (reste sur 5 par l'unité) +Q7 (chiffre manquant, nombre de solutions).
- 01 : Q5 options triées ; Q6 sans méta-option ; +Q7 multi (reprise L26 ex. 3أ), +Q8 (217▢, 2 et 5).
- 02 : Q2 refaite (clé plus la plus longue), Q3 étiquettes retirées, Q6 inversée (« plus grand » 3▢) ; +Q7 multi (14▢), +Q8 reste de 2607 sur 9, +Q9 arrangement 4-3-0-5, +Q10 plus grand nombre de 3 chiffres ÷ 5.
- 03 : Q2 sans méta-option, Q4–Q5 (1035) refaites ; +Q7 multi (÷3 et 9), +Q8 appariement des restes sur 9, +Q9 multiples communs de 2 et 5 entre deux bornes.
- 04 : Q3 sans options absurdes, Q5 (45▢0 : deux solutions), Q6 (plus petit nombre de 4 chiffres ÷9 et ÷5) ; +Q7 reste de 7481 sur 9, +Q8 âge du père.
- 05 : +Q7 pancartes (reprise ex. 2), +Q8 appariement 4-3-0-5, +Q9 plus grand nombre ÷9 et ÷2, +Q10 remise en ordre de la méthode du chiffre manquant.
- Reprises déclarées (`manuel`) : 01 (L26 ex. 3أ, L25 ex. 4ج), 02 (L26 ex. 4, ex. 7ب, L25 ex. 7, ex. 9), 03 (L26 ex. 3ج, ex. 7ب, L25 ex. 6), 04 (L26 ex. 4, 6, 7ب, L25 ex. 10), 05 (L25 ex. 2, 9, L26 ex. 8).

## 08-fractions-sens-lecture (leçon 18, ص 50–54 ; مذكرة 18 ; leçon 40 ex. 1–2)

### Table des écarts

| # | écart | où |
| - | ----- | -- |
| 1 | Cours : complet (partie de l'unité, lecture, demi-droite, comparaison à 1, quotient exact/approché, rapport « بالنسبة إلى », fraction d'une quantité) ; aucune règle fautive, aucune donnée de l'errata 18–19 reprise de travers (600 familles à 3 enfants / 300 à 1 enfant = données du manuel) | cours.md |
| 2 | **Non exercé** : fraction comme **rapport** (40/60, 15/10), partage = quotient (6 pommes / 5 personnes), quotient exact vs approché (9 ÷ 7), lecture en lettres de fractions > 1 (ex. 4), parts égales (cas octogone), fractions d'un **total à déduire** (arbustes 7/24), lecture d'un diagramme (familles) | exercices |
| 3 | **Notion spatiale sans figure** : demi-droite graduée (03-Q5 sans dessin), parties colorées d'une figure (ex. 6), diagramme en bâtons : aucune figure dans aucun exercice | exercices |
| 4 | Question à **option « لا أحد »** (non idiomatique) : 04-Q4 | 04 |
| 5 | Redondance : « ما المقام/البسط » en quiz Q1, 01-Q1, 02-Q1, 05-Q1 (laissé, ce sont des d1 d'entrée) | — |
| 6 | Options numériques non triées (02-Q5) | 02 |
| 7 | **Unité de capacité** : leçon 40 ex. 2 (6 dal, 40 L) demande une conversion que le chapitre ne rappelle pas : la consigne donne « 1 دكل = 10 ل » | 03 |

### Fait (08)

- cours/résumé : inchangés ; `chapter.json` : `sources[]` complété.
- quiz : +Q6 (9 ÷ 7 → 9/7 exact), +Q7 (rapport 10/25).
- 01 : +Q7 (carré en 8 triangles, 3 colorés — figure), +Q8 (6 pommes / 5 personnes), +Q9 appariement lettres ↔ fractions (L18 ex. 4).
- 02 : Q5 options triées ; +Q7 rapport 40/60 (ex. 8), +Q8 arbustes 7/24 (L40 ex. 1), +Q9 multi (12 filles / 18 garçons), +Q10 9 ÷ 7.
- 03 : Q5 remplacée (demi-droite graduée **avec figure**, point à 3/4) ; +Q7 parts inégales (figure), +Q8 6 dal / 40 L (L40 ex. 2).
- 04 : Q4 sans « لا أحد » ; +Q7 diagramme des familles 600/1300 (figure), +Q8 demi-droite (7/4, figure), +Q9 chasse à l'erreur sur le rapport.
- 05 : +Q7 hôtel 100/10 000 (ex. 10), +Q8 bande de 12 parts (3/12, figure), +Q9 grille 6 × 6, 2/3 → 24 cases (ex. 6ب).
- Reprises déclarées : 01 (L18 ex. 4, 7), 02 (L18 ex. 8, L40 ex. 1), 03 (L40 ex. 2), 04 (L18 ex. 9), 05 (L18 ex. 6ب, 10).

## 09-fractions-equivalentes (leçon 28, ص 80–84)

### Table des écarts

| # | écart | où |
| - | ----- | -- |
| 1 | Cours : complet (écritures égales, terme manquant au numérateur ET au dénominateur, réduction, irréductible, « plus grand diviseur commun cherché parmi les diviseurs » sans algorithme, توحيد المقامات d'un couple et d'un entier, séries sous contrainte) ; errata 29–33 : aucune donnée fautive reprise (le cours utilise 3/3, 49/77 sous leur forme corrigée ou pas du tout) | cours.md |
| 2 | **Clé la plus longue** : quiz Q2 (« نفسِ العدد (قاسمٍ مشترك) ») | quiz |
| 3 | **Séparateur arabe « ؛ »** dans des listes de fractions (02-Q6, 04-Q6) — risque bidi | 02, 04 |
| 4 | **Non exercé** : fractions > 1 et réduites en fraction > 1 (72/56 → 9/7), terme manquant au **dénominateur** (55/· = 11/3), erreur « un seul terme divisé » en situation, توحيد المقامات d'un **entier** et d'un couple, séries sous contrainte (ex. 8–9), irréductible par **multi**, conversion دكل → L (ex. 13), proportionnalité par fractions égales (ex. 14), figure (ex. 3) | exercices |
| 5 | **Aucune figure** dans les exercices alors que l'équivalence se voit sur une bande | exercices |
| 6 | Tension fiche : le « PGCD formalisé » est ⛔ (§3.2) ; le cours ne le formalise pas (liste des diviseurs, « le plus grand diviseur commun cherché parmi les diviseurs » ✅) — item `04-defi` Q2 conservé, à trancher par l'auditeur (voir doutes) | 04 |

### Fait (09)

- cours/résumé : inchangés ; `chapter.json` : `sources[]` complété.
- quiz : Q2 refaite (4 options de même forme, clé non la plus longue) ; +Q6 (توحيد المقامات de 1/2 et 1/3).
- 01 : +Q7 (deux bandes — figure, nombre de parts à colorier), +Q8 multi (reprise L28 ex. 6, bloc 1/4).
- 02 : Q6 (séparateur « ; ») ; +Q7 72/56 → 9/7 (ex. 5), +Q8 terme manquant au dénominateur 55/· = 11/3 (ex. 7), +Q9 chasse à l'erreur (5/45 pour 15/45).
- 03 : +Q7 توحيد المقامات de 2 et 3/5 (ex. 11b), +Q8 numérique (2/3 → 22/33), +Q9 séries sous contrainte (5/4, dénominateurs entre 10 et 30 — ex. 8).
- 04 : Q6 (séparateur) ; +Q7 intrus parmi 3/50 (série de l'ex. 14), +Q8 40 دكل → 400 L, 75/400 → 3/16 (ex. 13), +Q9 multi d'irréductibles.
- 05 : +Q7 quadrillage 4 × 4, bordure colorée → 3/4 (ex. 3, figure), +Q8 multi (≡ 3/2, ex. 6), +Q9 numérique 80/48 → 5/3 (ex. 5).
- Reprises déclarées : 01 (L28 ex. 6), 02 (ex. 5, 7), 04 (ex. 13), 05 (ex. 3, 5, 6).

## 10-comparaison-fractions (leçon 29 ص 85–88 + leçon 40 ص 117–121, synthèse codifiée sur ce chapitre)

### Table des écarts

| # | écart | où |
| - | ----- | -- |
| 1 | **Leçon 40 non reflétée** dans `chapter.json` (`manuel.pages` « 85-88 » seul alors que §4 codifie « 85-88 + 117-121 ») ; ses exercices 8, 9, 10, 13 (comparaison à 1 / à un **entier** / même numérateur / **complément à 1** / rangement avec entier et fractions > 1 / défi) jamais exercés tels quels | chapter.json, exercices |
| 2 | **Notion de la fiche non enseignée** : comparer une **fraction à un entier autre que 1** (L40 ex. 8ب : 4 ; 45/11, 25/3 ; 8, 16/5 ; 4) et ranger une liste qui contient un entier (L40 ex. 10 : 25/6, 4, 9/2, 3/4) — le cours ne comparait qu'à 1 | cours.md |
| 3 | Aucune donnée fautive reprise (erratum n° 56 = « أجد » → « أوجد », sans incidence). L29 ex. 5 (« mal posé ») **non repris** | — |
| 4 | **Méta-option** « لا يمكن المعرفة » (02-Q5) et « لا أحد » (03-Q6) | 02, 03 |
| 5 | **Gabarit** : 29 questions sur 30 = « قارن بين X و Y (وحّد على N) » avec les quatre mêmes options ; l'indication « (وحّد على N) » livre la méthode dans les d3/d4 ; le **d4** ne dépasse pas le d2 (aucune question où l'élève choisit sa méthode) | 02, 04, 05 |
| 6 | **Non exercé** : complément à 1 (L40 ex. 9, L29 ex. 2), problème « la nouvelle » (L29 ex. 7), flacons (ex. 8), rouleau de tissu (ex. 9, fraction d'une quantité + comparaison), rangement avec **égalité**/entier, fractions > 1 ensemble | exercices |
| 7 | **Aucune figure** (comparer = voir une bande / une droite) | exercices |

### Fait (10)

- **cours.md** : section **neuve** « مقارنةُ كسرٍ بعددٍ صحيح » au patron (ancre : course de 8 km, 25/3 km ; figure : zoom 8 → 9 en tiers ; exemple en 4 étapes avec leurs pourquoi ; erreur typique à deux faces — « comparaison impossible » [tag déjà au registre et déjà déclaré] et « numérateur seul comparé à l'entier » [pas de tag au registre : proposé] ; `::: methode` ; `::: verifie` ; `::: retenir`) ; le cas limite de l'ordre cite maintenant un entier dans la liste. `resume.md` : +1 puce (8 sections, 8 puces). `chapter.json` : `manuel.pages` « 85-88, 117-121 » (§4), `description`, `sources[]`.
- quiz : +Q6 (4 ; 45/11), +Q7 (complément à 1 : 4/5 ; 6/7).
- 01 : +Q7 (deux bandes 5/6 ; 5/7 — figure), +Q8 (L40 ex. 8أ).
- 02 : Q5 remplacée (méta-option) par le raisonnement d'أمل (L40 ex. 9) ; +Q7 (L40 ex. 8ب, un entier), +Q8 **remise en ordre** (L40 ex. 10, 3/8 ; 5/6 ; 9/7 ; 7/5).
- 03 : Q6 sans « لا أحد » ; +Q7 la nouvelle (L29 ex. 7), +Q8 flacons (L29 ex. 8).
- 04 : Q3 remplacée par une **remise en ordre** (L40 ex. 13, sans indice) ; Q5 remplacée (4 mois de صالح, L29 ex. 2, sans indice) ; +Q7 rouleau de 45 m (L29 ex. 9), +Q8 numérique (entiers < 25/6), +Q9 chasse à l'erreur sur le complément.
- 05 : +Q7 remise en ordre (L40 ex. 10 série 2, un entier dans la liste), +Q8 remise en ordre 3/7 ; 1/2 ; 5/9 (L40 ex. 8د).
- Reprises déclarées : 01 (L40 ex. 8أ), 02 (L40 ex. 9, 8ب, 10), 03 (L29 ex. 7, 8), 04 (L40 ex. 13, L29 ex. 2, 9), 05 (L40 ex. 10, 8د).

## 11-addition-soustraction-fractions (leçons 42 et 57, ص 126–128 et 163–164 ; مذكرة 48 ; T3 situation 1)

### Table des écarts

| # | écart | où |
| - | ----- | -- |
| 1 | Cours : **complet** (même dénominateur, un dénominateur multiple de l'autre, plus petit multiple commun, entier ± fraction, réduction du résultat, plusieurs termes / parenthèses / « بأيسر طريقة », part restante = 1 − somme, somme > 1 impossible, du tout à partir d'une partie) ; chaque valeur re-calculée ; errata n° 58 (L48 pb 1 aire 0,18 هـآ) : non repris | cours.md |
| 2 | **Aucun problème** dans les exercices : les 5 fichiers étaient des calculs isolés « ما ناتج a/b ± c/d », d1–d3, avec l'indication « (وحّد على N) » même au d4 ; aucune question de la leçon 42 (ex. 2, 4, 5, 6, 7, 10), 57, 48, ni de l'épreuve T3 (situation 1) | exercices |
| 3 | **Non exercé** : réduire avant d'additionner (ex. 4), parenthèses (ex. 5), plusieurs fractions de dénominateurs premiers entre eux (26/53 + 2/5), part restante, somme > 1 « impossible », retrouver le tout par une différence de fractions (réservoir, 125 m²), fraction d'une quantité en deux temps | exercices |
| 4 | **Indices de méthode** dans le d4 (`(وحّد على 12/15/20/8)`) | 04 |
| 5 | **Aucune figure** (la somme se voit sur une bande) | exercices |
| 6 | L40 ex. 16 (somme de quatre fractions = 1, retrouver le tout) et L48 pb 2 (salaire du technicien) rattachés à ce chapitre par la fiche (§4 colonne « mobilisent ») jamais repris | exercices |
| 7 | Hors périmètre, **non repris** : × de fractions (L57 ex. 1, relève du ch. `13`), volume en م³ (L57 ex. 4 : borne ⛔) | — |

### Fait (11)

- cours/résumé : inchangés ; `chapter.json` : `sources[]` complété (la leçon 40 ex. 16, la leçon 48 et le T3 y figurent).
- quiz : +Q6 (part restante 3/8).
- 01 : +Q7 (bande bicolore 3/8 + 2/8 — figure), +Q8 (3/2 + 1/3, L42 ex. 3).
- 02 : +Q7 réduire d'abord (L42 ex. 4), +Q8 parenthèses (L42 ex. 5), +Q9 somme > 1 (variante 1/2, 1/3, 1/4), +Q10 fabrique 26/53, 2/5 (L42 ex. 6).
- 03 : +Q7 poisson (3/20 + 1/4 + 2/5, L42 ex. 2), +Q8 reste 48 kg, +Q9 salaire du technicien 9/40 (L48 pb 2).
- 04 : 4 indices « وحّد على N » retirés (Q2, Q4, Q5, Q6, ids inchangés) ; +Q7 réservoir (variante : 3/5 → 11/15, 1200 L → 9000 L), +Q8 les trois frères (T3, fraction du troisième), +Q9 les trois frères (125 m² → 1000 m²). **Reprise de l'épreuve officielle** : `manuel {code 502603, pages 189-194, items T3 sit. 1 أ / ب}`.
- 05 : +Q7 champ 210 آر (L57 ex. 8), +Q8 bac 18 (L42 ex. 7), +Q9 5/8 − 4/7 (L42 ex. 3), +Q10 argent de poche 42 د (L40 ex. 16).
- Reprises déclarées : 01 (L42 ex. 3), 02 (L42 ex. 4, 5, 6), 03 (L42 ex. 2, L48 pb 2), 04 (guide 502603 T3 sit. 1), 05 (L57 ex. 8, L42 ex. 7, 3, L40 ex. 16).

## 12-fractions-decimales (leçon 31, ص 90–92 ; leçon 40 ex. 11–12)

### Table des écarts

| # | écart | où |
| - | ----- | -- |
| 1 | Cours : complet (définition, cas « مقامه 20/50/300 », numérateur entier, fraction décimale ↔ nombre décimal avec zéros, 10 000, réduction, conversion, **« quand possible »**, comparaison fractions + décimaux) ; errata n° 36–37 (L31 ex. 12) : le cours ne reprend pas l'exercice | cours.md |
| 2 | **Non exercé** : le « quand possible » (ex. 4, 10 : 11/7, 4/30, 5/108 impossibles ; 3/12, 3/75 possibles après réduction), le piège 21/300 (ex. 6), le numérateur décimal (ex. 8), dénominateur 10 000, les mesures en deux écritures (ex. 7), le rangement mélangé fractions/décimaux (ex. 9 ; L40 ex. 12ب), un problème | exercices |
| 3 | **Gabarit** : 29 questions sur 30 sont « ما القيمة العشرية للكسر X » / « اكتب Y كسرًا عشريًّا » ; le d4 ne dépasse pas le d2 | 02, 04, 05 |
| 4 | **Aucune figure** (la grille de 100 est la figure naturelle) | exercices |
| 5 | L31 ex. 12 (bibliothèque) : inexploitable tel qu'imprimé, **exploitable avec l'erratum et la lecture 3/10** (fiche §2) — repris en **variante** (non déclarée : le « 3/…0 » est une inférence du rédacteur) | 04 |

### Fait (12)

- cours/résumé : inchangés ; `chapter.json` : `sources[]` complété.
- quiz : +Q6 (qui est fraction décimale : 9/1000, pas 21/300), +Q7 (qui se convertit : 5/8).
- 01 : +Q7 (grille de 100, 35 colorés — figure), +Q8 (3,5 m = 35/10 m, L31 ex. 7).
- 02 : +Q7 piège 21/300 = 0,07 (ex. 6أ), +Q8 numérateur décimal 3,5/10 → 35/100 (ex. 8), +Q9 remise en ordre 1 ; 3/4 ; 0,6 ; 0,5 ; 25/100 (L40 ex. 12ب).
- 03 : +Q7 7/8 = 875/1000 (ex. 3), +Q8 multi « quand possible » (ex. 4), +Q9 3/125 = ?/1000 (ex. 10ب).
- 04 : +Q7 103 m² = 0,0103 hm² (ex. 7), +Q8 bibliothèque 440 livres (variante), +Q9 remise en ordre 0,8 ; 1/2 ; 3/10 ; 1/5 (L40 ex. 12ب).
- 05 : +Q7 3/10 000 = 0,0003 (ex. 6أ), +Q8 405/100 = 4,05 (L40 ex. 12أ), +Q9 25/500 = 5/100 (ex. 10أ), +Q10 209 L = 2,09 hl (ex. 7).
- Reprises déclarées : 01 (L31 ex. 7), 02 (L31 ex. 6أ, 8 ; L40 ex. 12ب), 03 (L31 ex. 3, 4, 10ب), 04 (L31 ex. 7 ; L40 ex. 12ب), 05 (L31 ex. 6أ, 10أ, 7 ; L40 ex. 12أ).
