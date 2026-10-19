# Notes de l'auteur B1 — maths 6ᵉ, chapitres 01 à 06 (mise à niveau)

> Lot B1 : `01-entiers-naturels` … `06-multiples-communs`. Autorité : fiche `programme/6eme-base/maths.md`
> (§1 bis, §2 quater / quinquies / octies / undecies, §3.2, §4, §6.1, §6.4) et PLAN.md § 3 (M1–M4).
> Méthode : lecture complète de chaque chapitre (cours, résumé, quiz, 5 exercices), table des écarts,
> puis corrections ; les questions remplacées gardent leur rang et leur difficulté (l'identifiant d'une
> question dérive de son rang après tri par difficulté), les questions ajoutées sont en fin de fichier
> à `difficulty` ≥ au maximum du fichier (aucun identifiant ne bouge).

## Constat d'ensemble (avant toute modification)

- Les six **cours** sont déjà au patron de notion (campagne « tranche nombres », é35) et **conformes à la fiche** :
  chaque notion des thèmes `الأعداد الطبيعيّة الكبيرة` → `المضاعفات` y est enseignée (ancrer → nommer → voir →
  exemple résolu → erreur typique → règle → `::: verifie`). Tous les calculs des cours ont été recalculés
  (aucune coquille). La **division par un décimal** (corrigée au §2 le 2026-09-23) est bien dans le cours `05`.
- Aucun errata (§6.1, n° 1, 7, 8, 9, 10) n'est repris dans ces chapitres ; aucune incohérence §6.4 n'est reprise ;
  rien de ⛔ ; aucune somme des angles (M3 sans objet ici).
- `content:check`, `content:qa` et `content:tranche` sont verts sur le lot au départ (0 erreur) : les écarts
  sont donc de **substance** (ce que le cours enseigne et que le quiz / les exercices n'exercent pas) et de
  **forme** (paires proches, doublons, une option contredite par l'énoncé).

## Table des écarts

### 01-entiers-naturels
| # | écart | décision |
| --- | --- | --- |
| 1-1 | `04-defi` Q3 : l'option « 01 234 » est contredite par l'énoncé (« لا يبدأ بالصفر ») — éliminée à vue | retirer la parenthèse de l'énoncé : « 01 234 » devient le piège réel (zéro initial) |
| 1-2 | paires proches : `01-pratique#1` ↔ `quiz#3` (rang d'un chiffre, 0,50) et `02-boss#1` ↔ `03-revision#1` (rang, 0,56) | `01-pratique` Q1 devient « valeur du chiffre » ; `03-revision` Q1 devient « nom du 4ᵉ صنف » |
| 1-3 | la classe des **milliards** est nommée au cours (vocabulaire, Q-10) mais jamais interrogée | item de vocabulaire seul (aucun nombre ≥ 10⁹) |
| 1-4 | `chapter.json` : pas de renvoi à la fiche dans `sources[]` | ajouté |

### 02-operations-naturels
| # | écart | décision |
| --- | --- | --- |
| 2-1 | trois items de vocabulaire de résultat (`quiz#1`, `01-pratique#5`, `03-revision#1`), dont une paire à 0,80 | `03-revision` Q1 devient le vocabulaire de la **division euclidienne** (القاسم) |
| 2-2 | la division euclidienne n'est exercée qu'avec un diviseur à un chiffre et jamais « dans l'autre sens » (a = b × q + r) ni avec un reste de problème (nombre de cars) | 3 items ajoutés (cars, retrouver le dividende, « quel est le bon reste ? ») |
| 2-3 | `chapter.json` : renvoi à la fiche | ajouté |

### 03-nombres-decimaux
| # | écart | décision |
| --- | --- | --- |
| 3-1 | `05-entrainement` Q5 : deux options disent la même chose (« متساويان » et « 0,408 = 0,41 ») | trois options > / = / < |
| 3-2 | `05-entrainement` Q6 : « le plus proche de 1,6 » sans borne (1,599… est plus proche) | l'énoncé borne le choix aux nombres proposés |
| 3-3 | la lecture d'un décimal à 3 chiffres (« …جزءًا من الألف ») n'est jamais interrogée (révision 1) | `02-boss` Q1 remplacé (item de lecture) |
| 3-4 | l'encadrement entre deux **entiers consécutifs** (révision 2, ex. 4 أ) n'est pas exercé | `03-revision` Q3 remplacé |
| 3-5 | renvoi à la fiche dans `sources[]` | ajouté |

### 04-addition-soustraction-decimaux
| # | écart | décision |
| --- | --- | --- |
| 4-1 | le **TERME MANQUANT** (leçon 1, ex. 4 : 9,13 = … + 8,09) est enseigné, peu exercé, jamais avec la donnée du manuel | reprise de ex. 4 (`04-defi` Q1) |
| 4-2 | le **TERME MANQUANT** → idem ; la **TRADUCTION D'UNITÉS dans une somme** (ex. 6) : enseignée (méthode du dernier cours), jamais exercée | `02-boss` Q2 remplacé (1,5 m + 30 cm) |
| 4-3 | l'**estimation par arrondi** (ex. 3 أ) est enseignée et absente du quiz et des exercices | 1 item au quiz (Q3) + 1 en `04-defi` (Q4) |
| 4-4 | opérations posées à décimales inégales avec retenue qui traverse la virgule (ex. 2 : 9,9 + 91,09 ; 100,1 − 99,98) | reprise en `03-revision` (Q2, Q5) |
| 4-5 | problème en chaîne de la balance (ex. 10) : jamais exercé | 2 questions numériques ajoutées à `05-entrainement` (reprise) |
| 4-6 | `04-defi` Q4 : « somme de 3 masses » tagué d3 mais à un pas | remplacé par l'estimation (d3) |

### 05-multiplication-division-decimaux
| # | écart | décision |
| --- | --- | --- |
| 5-1 | **la division PAR un décimal (✅, prérequis de 5ᵉ, ex. 2 ب / 4 / 5 de la leçon 3)** est enseignée au cours (section 6) mais **n'est exercée par aucune des 35 questions ni par le quiz** | 8 items (÷ 0,1, ÷ 0,01, ÷ décimal, déduction de 44 × 36, mille marin, prix au kilo) |
| 5-2 | l'**estimation** (leçon 3, ex. 3) est enseignée, jamais exercée | 1 item en `04-defi` |
| 5-3 | 7 items « décimal × naturel à un chiffre » presque identiques ; `02-boss` Q6 « 9 ÷ 100 » tagué d3 | remplacés par les items de 5-1 (rang et difficulté conservés) |
| 5-4 | reprise de l'épreuve du T1 (guide p.169, 173–174, situation 1 : offre à tempérament) jamais exploitée | 3 questions numériques (sans les fractions 1/5 et 1/10, qui viennent au ch. 08) |
| 5-5 | `chapter.json` : description et renvoi à la fiche | mis à jour |

### 06-multiples-communs
| # | écart | décision |
| --- | --- | --- |
| 6-1 | `quiz#5` identique (1,00) à `02-boss#1` (« 0 est multiple de… ») | quiz Q5 devient « somme de deux multiples » |
| 6-2 | somme / différence de deux multiples et « multiple d'un multiple » : enseignés (ex. 5), presque jamais exercés | quiz Q5 ; `04-defi` Q4 existant |
| 6-3 | huit items « PPCM de deux petits nombres » (paires à 0,53–0,63) ; aucun reste constant (ex. 10), aucun intervalle par le PPCM (ex. 7), aucune reprise de ex. 6 / 9 | remplacements ciblés (voir « fait ») |
| 6-4 | le titre de la leçon dit « فأكثر » : un seul item à trois nombres | ex. 9 (7, 12, 42) repris |
| 6-5 | situations de bus / de coureurs (leçon 13, « أقيّم مكتسباتي » et ex. 11) jamais exercées | 2 questions numériques ajoutées à `05-entrainement` |

## Propositions d'étiquettes (non créées — `misconceptions.json` n'est pas de mon périmètre)

- `math.num.reste-ignore-dans-le-probleme` — « tu donnes le quotient et tu oublies qu'un reste exige un car de plus » (2-2, cars).
- `math.num.division-virgules-deplacees-inegalement` — « tu déplaces la virgule du dividende et celle du diviseur d'un nombre de rangs différent » (5-1 ; pitfall du cours `05`, section 6).
- `math.mes.unites-melangees-sans-conversion` — « tu additionnes 1,5 m et 30 cm comme s'il s'agissait de la même unité » (4-2).

## Fait (au fil de l'eau)

_(complété chapitre par chapitre ci-dessous)_
