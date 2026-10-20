# Notes de l'auteur B1 — maths 6ᵉ, chapitres 01 à 06 (mise à niveau)

> Lot B1 : `01-entiers-naturels` … `06-multiples-communs`. Autorité : fiche `programme/6eme-base/maths.md`
> (§1 bis, §2 quater / quinquies / octies / undecies, §3.2, §4, §6.1, §6.4) et PLAN.md § 3 (M1–M4).
> Méthode : lecture complète de chaque chapitre (cours, résumé, quiz, 5 exercices), recalcul de TOUTES les
> valeurs (cours et questions), table des écarts, puis corrections. Une question remplacée garde son rang et
> sa difficulté (l'identifiant d'une question dérive de son rang après tri par difficulté) ; une question
> ajoutée est en fin de fichier, à `difficulty` ≥ au maximum du fichier : aucun identifiant ne bouge.
> Fichiers modifiés : `chapter.json`, `quiz.json`, `exercices/*.json` de chaque chapitre, et deux `cours.md`
> (01 et 05, mise en forme seule). Base de comparaison : commit `07451934`.

## Constat d'ensemble (avant toute modification)

- Les six **cours** sont déjà au patron de notion (campagne « tranche nombres », é35) et **conformes à la
  fiche** : chaque notion des thèmes `الأعداد الطبيعيّة الكبيرة` → `المضاعفات` y est enseignée (ancrer → nommer →
  voir → exemple résolu → erreur typique → règle → `::: verifie`). Tous les calculs des cours ont été
  recalculés : **aucune coquille de contenu**. La **division par un décimal** (corrigée au §2 le 2026-09-23)
  est bien enseignée au cours `05` (section 6). Aucune section de cours n'est à ajouter ; aucune règle n'est
  contraire à la fiche.
- Aucun errata (§6.1, n° 1, 7, 8, 9, 10) n'est repris dans ces chapitres ; aucune incohérence §6.4 n'est
  reprise ; rien de ⛔ (ni calcul littéral, ni ÷ de fractions, ni volume) ; la somme des angles (M3) est sans
  objet ici. Moyenne (◐) et problèmes « somme et différence » (◐) : non demandés comme item.
- `content:check`, `content:qa` et `content:tranche` étaient verts au départ : les écarts sont de
  **substance** (ce que le cours enseigne et que le quiz / les exercices n'exercent pas) et de **forme**
  (doublons, paires proches, deux défauts de clé, 7 clés strictement les plus longues).
- Un seul défaut de **rendu** dans les cours : un `**gras**` coupé par un retour à la ligne dans une citation
  `>` ou dans la réponse d'un `::: verifie` s'affiche avec ses astérisques (5 occurrences : 01 ×1, 05 ×4) —
  corrigé (la coupure est déplacée avant le gras). Contrôle par vitest jetable sur `renderLesson` /
  `renderSummary` : plus aucun `**`, `_`, `:::` ni `$$` dans les 6 cours et 6 résumés.

## Table des écarts et ce qui a été fait

### 01-entiers-naturels
| # | écart | fait |
| --- | --- | --- |
| 1-1 | **deux réponses défendables** — `05-entrainement` Q2 : l'option « ثلاثمئة ألفٍ وخمسة آلاف وأربعون » vaut 300 000 + 5 000 + 40 = 305 040, comme la clé | option a remplacée par « ثلاثمئة ألفٍ وخمسمئة وأربعون » (300 540) ; explication réécrite |
| 1-2 | `04-defi` Q3 : « 01 234 » éliminé à vue par l'énoncé (« لا يبدأ بالصفر ») | parenthèse retirée de l'énoncé ; « 01 234 » devient le piège du zéro initial |
| 1-3 | 7 clés strictement les plus longues dont `02-boss` Q1 | Q1 interroge désormais le rang du chiffre 2 (clé « مئات الآلاف », plus courte que « عشرات الآلاف ») |
| 1-4 | paires proches (rang d'un chiffre ×3 ; deux lectures de grands nombres) | `01-pratique` Q1 → valeur d'un chiffre (4 805) ; `02-boss` Q2 → écriture en chiffres ; `03-revision` Q1 → nom du 4ᵉ صنف |
| 1-5 | la classe des **milliards** (vocabulaire, Q-10) jamais interrogée | `03-revision` Q1 (vocabulaire seul, aucun nombre ≥ 10⁹) |
| 1-6 | `05-entrainement` Q5 : même gabarit que `02-boss` Q4 (28 617) | habillage « زوّار موقع » |
| 1-7 | `chapter.json` : pas de renvoi à la fiche dans `sources[]` | ajouté |
| 1-8 | rendu : gras coupé dans le `verifie` de la section 2 | corrigé dans `cours.md` |

### 02-operations-naturels
| # | écart | fait |
| --- | --- | --- |
| 2-1 | vocabulaire du résultat interrogé 3 fois (paire à 0,80) | `03-revision` Q1 devient le vocabulaire de la **division euclidienne** (135 = 12 × 11 + 3, القاسم) |
| 2-2 | la division euclidienne n'est exercée qu'avec un diviseur à 1 chiffre, jamais « à l'envers » (a = b × q + r), jamais avec un reste de problème ni avec la condition r < b isolée | +3 questions : cars (250 élèves, 45 places → 6), dividende retrouvé (12 × 25 + 7), « laquelle de ces quatre écritures est la division euclidienne de 1 000 par 24 ? » |
| 2-3 | `quiz` Q5 : clé strictement la plus longue | distracteur remplacé (« 8 × 10 + 10 × 3 ») |
| 2-4 | `sources[]` | ajouté (+ §2 octies leçons 22–23, guide p.192) |

### 03-nombres-decimaux
| # | écart | fait |
| --- | --- | --- |
| 3-1 | `05-entrainement` Q5 : deux options disent la même chose (« متساويان » et « 0,408 = 0,41 ») | trois options > / = / < |
| 3-2 | `04-defi` Q5 : « 8,350 » et « 8,35 » sont le même nombre (distracteurs confondus) | « 8,3005 » |
| 3-3 | `05-entrainement` Q6 : « le plus proche de 1,6 » sans borne | énoncé borné aux nombres proposés |
| 3-4 | lecture d'un décimal à 3 chiffres jamais interrogée (révision 1) | `02-boss` Q1 → lire 3,408 (zéro intérieur) |
| 3-5 | encadrement entre deux **entiers consécutifs** non exercé (révision 2, ex. 4 أ) | `03-revision` Q3 → 599,09 (4 paires consécutives) |
| 3-6 | composition 7 + 0,3 + 0,008 non exercée (le zéro qui garde la rangée) ; paire à 0,54 | `05-entrainement` Q2 remplacé |
| 3-7 | gabarit « كم جزءًا من المئة في العدد » commun à `12` | `03-revision` Q6 reformulé |
| 3-8 | `sources[]` | ajouté |

### 04-addition-soustraction-decimaux
| # | écart | fait |
| --- | --- | --- |
| 4-1 | le **terme manquant** (leçon 1, ex. 4) est enseigné mais jamais avec la donnée du manuel | `04-defi` Q1 = ex. 4 (9,13 = … + 8,09), distracteurs = les trois erreurs de soustraction posée |
| 4-2 | l'**estimation par arrondi** (ex. 3 أ) est enseignée et absente du quiz et des exercices | `quiz` Q3 (62,4 − 18,75) et `04-defi` Q4 (36,4 + 5,75) |
| 4-3 | **conversion d'unités dans une somme** (ex. 6), enseignée à la méthode du dernier cours, jamais exercée | `02-boss` Q2 (2,4 m + 15 cm) |
| 4-4 | opérations posées à décimales inégales, retenue qui traverse la virgule (ex. 2) | `03-revision` Q2 (100,1 − 99,98) et Q5 (9,9 + 91,09) = reprises |
| 4-5 | problème en chaîne de la **balance** (ex. 10) jamais exercé | `05-entrainement` +1 question numérique (reprise) |
| 4-6 | `04-defi` Q4 « somme de 3 masses » taguée d3 pour un seul pas | remplacée par l'estimation (d3 : arrondi + somme) |
| 4-7 | `quiz` Q1 : clé strictement la plus longue ; gabarit « المطروح منه والفرق » commun à `02` | option c allongée ; `04-defi` Q2 reformulé |
| 4-8 | `sources[]` | ajouté (+ révision 3, guide p.80–82) |

### 05-multiplication-division-decimaux
| # | écart | fait |
| --- | --- | --- |
| 5-1 | **la division PAR un décimal (✅, prérequis de 5ᵉ, leçon 3 ex. 2 ب / 4 / 5)** est enseignée au cours mais n'est exercée par **aucune** des 35 questions ni par le quiz | 7 items de division par un décimal — quiz Q5 (7,5 ÷ 0,5), ÷ 0,1 (15), ÷ 0,01 (36,8), 3,6 ÷ 0,4, prix au kilo (9 ÷ 0,75), déduction de 44 × 36 (1 584 ÷ 4,4), mille marin (10,186 ÷ 1,852) — plus 48,36 ÷ 12 (zéro intercalaire du quotient) et 22,18 × 0,01 |
| 5-2 | l'**estimation** (leçon 3, ex. 3) enseignée, jamais exercée | `04-defi` Q1 (4,8 × 6,1) |
| 5-3 | 7 items « décimal × naturel à 1 chiffre » presque identiques ; `02-boss` Q6 « 9 ÷ 100 » tagué d3 | remplacés par les items de 5-1 (rang et difficulté conservés) |
| 5-4 | épreuve du T1 (guide p.169, 173–174, situation 1) jamais exploitée | `05-entrainement` +1 question numérique : coût total de l'offre à tempérament (342,750 d comptant + 6 acomptes, +5,750 d par acompte → 1 015,5 d). Offres 1 et 3 laissées : elles supposent 1/5 et 1/10 d'une quantité (ch. 08, 13) |
| 5-5 | 3 clés strictement les plus longues (`02-boss` Q3, `05-entrainement` Q4 et Q5) | un distracteur remplacé par un voisin de même longueur |
| 5-6 | `chapter.json` : description sans la division par un décimal ; `sources[]` | mis à jour |
| 5-7 | rendu : 4 gras coupés dans `cours.md` | corrigés |

### 06-multiples-communs
| # | écart | fait |
| --- | --- | --- |
| 6-1 | `quiz` Q5 identique (1,00) à `02-boss` Q1 (« 0 est multiple de… ») | `quiz` Q5 → **somme de deux multiples** (12 + 30 = 42) ; `quiz` Q3 reformulé (paires 0,53 / 0,47) |
| 6-2 | somme / différence de deux multiples, « multiple d'un multiple » : enseignés (ex. 5), presque jamais exercés | `quiz` Q5 (+ `04-defi` Q4 existant) |
| 6-3 | huit items « PPCM de deux petits nombres » (paires à 0,53–0,63) ; aucun reste constant, aucun intervalle par le PPCM, aucune reprise de ex. 4 / 6 | `02-boss` Q3 → **multi** (6 et 9) ; `02-boss` Q6 → 3ᵉ multiple commun de 8 et 12 ; `04-defi` Q3 = ex. 4 (4, 6, 8 sous 130 → 5) ; `05-entrainement` Q2 = ex. 6 (150 et 200 → 600) et Q5 = reste constant (61) |
| 6-4 | le titre de la leçon dit « فأكثر » : un seul item à trois nombres | `04-defi` Q2 (4, 6, 10 → 60) + Q3 (ex. 4) |
| 6-5 | situations de bus / de coureurs (ex. 10, 11, أقيّم مكتسباتي) | `05-entrainement` +2 questions numériques ; les données du manuel étant déjà les exemples du cours, elles sont réécrites avec d'autres données (variantes, non tracées) |
| 6-6 | `02-boss` Q5 : clé strictement la plus longue | option a remplacée (« 15 مضاعفٌ للعدد 3 والعدد 4 ») |
| 6-7 | `sources[]` | ajouté |

## Reprises déclarées (champ `manuel` d'exercice, mêmes données)

| fichier | code · pages | items |
| --- | --- | --- |
| 04 `03-revision` | 102609 · 4-7 | أقيّم 2 (100,1 − 99,98) ; أقيّم 2 (9,9 + 91,09) |
| 04 `04-defi` | 102609 · 4-7 | ex. 4 (9,13 = … + 8,09) |
| 04 `05-entrainement` | 102609 · 4-7 | أقيّم 10 (الميزان) |
| 05 `01-pratique` | 102609 · 10-13 | ex. 2 أ (22,18 × 0,01) ; ex. 2 ب (15 : 0,1) |
| 05 `02-boss` | 102609 · 10-13 | ex. 2 ب (48,36 : 12) ; ex. 5 (1584 : 4,4) |
| 05 `04-defi` | 102609 · 10-13 | ex. 7 (10,186 km = 5,5 ميل) |
| 05 `05-entrainement` | **502603** · 169, 173-174 | T1 الوضعية 1 (العرض الثاني) |
| 06 `04-defi` | 102609 · 35-37 | ex. 4 (4 و 6 و 8 تحت 130) |
| 06 `05-entrainement` | 102609 · 35-37 | ex. 6 (150 و 200) |

Variantes (données changées, donc non tracées) : 05 `05-entrainement` Q2 (36,8 ÷ 0,01), 06 `02-boss`, `04-defi` Q2,
`05-entrainement` Q5/Q7/Q8, tous les items d'estimation.

## Étiquettes : propositions (rien n'a été créé — `misconceptions.json` n'est pas de mon périmètre)

- `math.num.division-virgules-deplacees-inegalement` — « tu déplaces la virgule du dividende et celle du diviseur
  d'un nombre de rangs différent » (pitfall du cours `05`, section 6). **Seuil de 3 questions atteint** : options
  muettes à étiqueter si l'id est créé — `05` `quiz` Q5 (1,5), `03-revision` Q4 (0,9), `03-revision` Q6 (0,12),
  `02-boss` Q6 (36), `04-defi` Q3 (0,55). Il pourrait alors entrer dans `coursePitfalls` de `05`.
- `math.num.reste-ignore-dans-le-probleme` — « tu donnes le quotient et tu oublies qu'un reste exige un car de plus »
  (02 `02-boss` Q7, option 5 ; une seule occurrence pour l'instant : seuil non atteint).
- `math.mes.unites-melangees-sans-conversion` — « tu additionnes 1,5 m et 30 cm comme s'il s'agissait de la même
  unité » (04 `02-boss` Q2, option 17,4 ; une occurrence : seuil non atteint).

## Contrôles passés

`content:check` ✓ · `content:qa --subject math-6eme` 0 erreur sur le lot (les 2 erreurs et 3 avertissements qui
restent sont dans `14` et `19`, hors lot) · `content:figures:check` rien sur le lot · `content:tranche --fresh
--strict-longest --strict-lessons` ✓ (0/47 clé la plus longue, 0 paire proche, patron en recul 0) ; sur les 6 chapitres
entiers : 0/211 clés les plus longues, 0 paire ≥ 0,45 · `prettier --check` ✓ · rendu des cours : 0 résidu Markdown ·
scan de notation (chiffres arabo-indiens, groupes de chiffres sans U+00A0, LaTeX, `$`) : 0.

## Doutes pour l'auditeur

1. **Reprise `أقيّم 10` (ch. 04)** : le cours `04` utilise les mêmes masses (38,5 ; 45,5 ; 42,75 ; total 126,75) comme
   ancrage de la section « خاصّيات الجمع ». La question demande de les retrouver par différences, mais un élève qui
   se souvient du cours reconnaît 42,75. Gardée parce que c'est la reprise la plus proche du manuel qui n'exige ni
   lettre ni schéma en barres (◐).
2. **Code 502603 au niveau de l'exercice (ch. 05)** : le schéma décrit `code` comme le manuel élève ; la même pratique
   existe déjà à `14/04-defi` (T2). `content:check` l'accepte.
3. **Quiz du ch. 05** : Q5 passe de « ÷ 100 » à « ÷ décimal » — la division par 10/100/1000 reste interrogée au Q2 du quiz
   (× 10) et dans les exercices.
4. **Question `multi` (06 `02-boss` Q3)** : 5 options, 3 correctes ; le moteur affiche « sélectionne toutes les bonnes
   réponses » (comme `07`, `09`).
5. **Distribution des clés** : a 28 % · b 25 % · c 30 % · d 17 % sur les 210 QCM des six chapitres (le mélange à l'écran
   la rend invisible).
6. Un point de la fiche **non exercé volontairement** : « trois multiples consécutifs de somme donnée » (ex. 8, §2 quinquies
   écart 6) — méthode du schéma en barres, ◐ Q-5.
7. L'enchaînement des acomptes (ch. 05) reste sur ≤ 3 étapes officielles ; la deuxième méthode (981 + 6 × 5,75) est la
   voie abrégée du corrigé (où « 891 » est une coquille pour 981).
