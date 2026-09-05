# Valorisation des manuels élèves officiels — la doctrine de reprise

> **Portée.** Ce fichier dit **quoi faire de chaque type de contenu d'un manuel élève du CNP** :
> une leçon, un encadré « à retenir », un exemple résolu, une figure, un tableau, et surtout les
> **centaines d'exercices** que chaque manuel porte. Il est normatif pour toute campagne de
> contenu d'une matière **école** dont le manuel figure au corpus (`cnp-officiel/`). Il ne
> remplace aucune barre existante : `quality-bar.md` (questions), `course-quality.md` (cours),
> `course-figures.md` (figures), `math-and-notation.md` (notation) s'appliquent **intégralement**
> à une reprise. Reprendre un exercice n'exonère d'aucun gate.
>
> Étude : `FableEtudes/21-valorisation-manuels/ETUDE.md`.

> **Pourquoi ce fichier existe.** Les manuels du CNP sont la matière pédagogique la plus riche et
> la plus légitime du marché : calibrés par les auteurs du programme, connus des élèves, reconnus
> des parents. L'app en exploitait deux usages — matière première de transcription, et affichage
> documentaire (la carte « Manuel officiel », la galerie « Pages du manuel »). Entre les deux,
> le pont **pédagogique** manquait. Au moment de l'étude : **267 PDF élève sur le disque, et zéro
> question du catalogue rattachée à un exercice de manuel.** Pas par difficulté technique — le
> moteur couvre déjà presque toutes les formes d'exercices imprimées — mais parce que **rien ne
> disait comment traiter un exercice, une figure, un encadré**. Chaque campagne le redécidait.

---

## 0. La règle qui prime : ce qu'on reprend, et ce qu'on ne copie pas

**Verbatim toléré pour les énoncés techniques courts non créatifs** — une consigne de calcul
standard (« Calcule le PGCD de 24 et 36 »), une formulation qui n'appartient à personne.
**Adaptation partout ailleurs** : reformulation, mêmes données. C'est l'arbitrage Q-1 du
2026-07-20, et c'est une **posture de risque assumée, pas un avis juridique**.

Trois interdits ne bougent pas, quel que soit le régime (R-11) :

- **jamais de bitmap ni de scan** de manuel dans le contenu versionné — les scans vivent
  exclusivement dans les buckets privés gated (`manuel-eleve`, `manuel-pages`) ;
- **jamais de reprise verbatim d'un extrait littéraire** cité par un manuel de langue : ce sont
  des œuvres d'auteurs sous droits propres. Les questions se réécrivent autour de la notion, ou
  sur des textes originaux maison ;
- **jamais de corrigé de guide enseignant recopié**. L'explication est toujours originale (R-2).

---

## 1. Les trois régimes de reprise

Le régime se décide **avant** d'écrire, et il détermine si la reprise se **trace**.

| régime            | ce que c'est                                                                                                                                   | tracé ? |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **(a) directe**   | l'énoncé est auto-suffisant et se mappe tel quel : mêmes données, consigne éventuellement reformulée a minima pour la forme cible               | ✅ oui  |
| **(b) adaptée**   | même substance, **mêmes données**, transformation de forme : décomposition en étapes, ajout de distracteurs, cloze-isation, figure redessinée | ✅ oui  |
| **(c) variante**  | même notion, **données changées** — pour multiplier les items, éviter un support non reproductible, ou contourner une contrainte de verbatim   | ❌ non  |

**(b) est le régime par défaut.** Le (c) n'est pas une reprise : c'est du contenu maison inspiré
du manuel. Le tracer gonflerait la couverture d'exercices que le manuel ne reconnaîtrait pas.

⚠️ **Changer les données, c'est changer de régime — jamais « corriger » une reprise en silence.**
Si le manuel comporte une erreur avérée, la question est reprise **corrigée** ET l'écart est
consigné dans la fiche programme §6 (Incertitudes). On ne reproduit jamais une erreur, et on ne
la masque jamais non plus.

---

## 2. La taxonomie fermée — que faire de chaque contenu du manuel

Grille alignée sur le `DocumentModel` de ScribeKit (`heading` / `paragraph` / `list` / `table` /
`figure` / `exercise`).

| #   | contenu du manuel                                                                | destination app (formats **existants** uniquement)                                                                                                                                                        |
| --- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | leçon, paragraphes de cours                                                      | `cours.md` **réécrit** (voix produit, jargon officiel conservé) — jamais copié                                                                                                                              |
| 2   | encadré de savoir (définition, théorème, propriété, règle, méthode, « retenir ») | bloc `::: definition\|propriete\|methode\|retenir` + carte `resume.md` + question d1–2 si testable (**R-8**)                                                                                                 |
| 3   | exemple résolu                                                                   | bloc `::: exemple` / `::: methode`, réécrit — **gisement n° 1 de variantes d1**                                                                                                                             |
| 4   | vocabulaire, lexique                                                             | cartes résumé + `matching` terme↔définition + cloze ; `short_answer` désormais disponible (é20)                                                                                                             |
| 5   | figure, schéma, graphique                                                        | **SVG redessiné** (`course-figures.md`) — côté cours et côté questions                                                                                                                                      |
| 6   | photo / planche documentaire (SVT, histoire…)                                    | schéma SVG **simplifié** si la notion est schématisable ; sinon la question se rédige auto-suffisante, la planche restant consultable via la galerie « Pages du manuel » (gated). **Jamais de bitmap** |
| 7   | tableau de données                                                               | table markdown (cours) ; format « lecture de document/données » (question)                                                                                                                                  |
| 8   | **exercices**                                                                    | → le mapping du §3                                                                                                                                                                                          |
| 9   | activité d'exploration (ouverture de chapitre, manipulation)                     | histoire-problème séquentielle quand elle se raconte ; sinon ⛔ **non transposable**, et on l'écrit                                                                                                        |
| 10  | exercices de synthèse / annales de fin de manuel                                 | palier d3–d4 des `prof-*` (au lycée : tier `NN-annales-bac`)                                                                                                                                                |

---

## 3. Le mapping des exercices — par **forme de la réponse attendue**

C'est la forme de la réponse, pas le thème, qui décide du format. Chaque cible ci-dessous a sa
**correction automatique native** — aucune ne demande de moteur nouveau.

| forme dans le manuel                          | format app                                                                                | remarque                                                                                    |
| --------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| QCM imprimé                                   | `mcq`                                                                                       | options du manuel conservées ; complétées à **≥ 3 distracteurs-misconceptions** s'il n'en a que 2 |
| calcul / réponse numérique / mesure           | `numeric` (`{value, tolerance?, unit?}`)                                                    | tolérance selon la grandeur ; unité annoncée dans le `prompt`                                |
| « relie / associe »                           | `matching`                                                                                  | natif                                                                                           |
| « ordonne / classe / range »                  | `ordering`                                                                                  | natif                                                                                           |
| « coche toutes les bonnes réponses »          | `multi`                                                                                     | sous-ensemble propre, 2 à 5                                                                    |
| « complète » (texte à trous)                  | **`short_answer`** (é20 livrée) ; cloze `mcq` en repli                                      | la version native supprime la devinette                                                        |
| vrai / faux avec justification                | vrai/faux motivé                                                                            | la justification vit dans `explanation`                                                        |
| exercice sur figure / document                | QCM visuel SVG · lecture de document                                                        | figure **redessinée** (R-7) ; jamais « voir p. X »                                             |
| problème à sous-questions (a, b, c…)          | **histoire-problème séquentielle** — 1 question par étape, dans l'ordre de l'énoncé         | le format le plus fréquent en maths/physique ; chaque étape auto-suffisante                    |
| « démontre / rédige / justifie »              | **décomposition en jalons** (`mcq`/`numeric` : hypothèses → outil → étape clé → conclusion) | la rédaction libre n'est pas notée                                                             |
| construction géométrique, manipulation réelle | ⛔ **non transposable v1**                                                                  | listé dans la fiche **avec sa raison** — aucune couverture silencieuse (R-4)                   |

---

## 4. Les douze règles

- **R-1 — Fidélité des données.** Une reprise conserve l'énoncé-substance : mêmes valeurs, mêmes
  objets, même contexte, même exigence. Changer les données = régime (c), jamais une « reprise
  corrigée » silencieuse.
- **R-2 — L'explication est toujours originale.** Mini-leçon conforme à `quality-bar.md` (règle,
  application, piège nommé dès d3). Jamais un corrigé recopié.
- **R-3 — Auto-suffisance.** Une question reprise se résout **entièrement à l'écran**. « Voir le
  manuel p. X » n'est jamais une dépendance de résolution : la référence est un plus de confiance,
  pas un support requis.
- **R-4 — Traçabilité déclarée.** Tout exercice app qui reprend ≥ 1 exercice du manuel porte le
  champ `manuel` (§5) avec ses `items`. Une **variante** ne se trace pas.
- **R-5 — Anti-duplication & cumul.** Avant toute reprise : audit de l'échelle existante du
  chapitre (`generation-pipeline.md`). Une reprise ne doublonne jamais une question existante ;
  elle remplit un palier manquant ou s'ajoute au `NN` libre suivant — **jamais de renommage ni de
  renumérotation** (les UUID sont dérivés des slugs).
- **R-6 — Calibration sur l'échelle app.** Un exercice repris est re-calibré ⭐1–4 selon
  `rewards-and-modes.md` : les exercices d'application peuplent d1–d2, les problèmes de synthèse
  d3 ; le d4 reste le territoire des `prof-*`. La reprise ne convertit jamais un palier libre en
  palier plafond.
- **R-7 — Figures.** Toute reprise « sur figure » embarque la figure **redessinée en SVG inline**,
  fidèle à la _fonction_ (mêmes données, mêmes relations), pas au pixel. Doctrine `course-figures.md`
  intégrale : figure VRAIE (coordonnées re-dérivées, double-solve), qui **ne fuit jamais la clé**,
  `viewBox` obligatoire, jamais de `<image>`.
- **R-8 — Complétude des savoirs.** Tout encadré de savoir du périmètre d'un chapitre doit exister
  dans l'app : bloc typé dans `cours.md` **et** carte dans `resume.md` ; s'il est testable, au
  moins une question d1–2 l'interroge.
- **R-9 — Ancrage chapitre.** Toute matière école dont le manuel figure au corpus déclare
  `chapter.manuel {code, pages}` sur **chacun** de ses chapitres. C'est ce qui alimente la galerie
  de pages et le rapport de couverture. Les codes viennent du `CATALOGUE.md` du corpus.
- **R-10 — Langue & notation.** Contenu école monolingue dans la langue officielle d'instruction.
  La reprise **convertit** la typographie vers le standard app : chiffres occidentaux 0–9 même
  quand le manuel imprime ٠١٢٣, équations LTR, unités SI, U+00A0 dans les groupes de chiffres
  (`math-and-notation.md`). Fidélité au **contenu mathématique**, pas à la typographie.
- **R-11 — Droits.** Voir le §0 : jamais de bitmap, jamais d'extrait littéraire verbatim, jamais
  de corrigé enseignant recopié.
- **R-12 — Registre du badge.** ⛔ **Sans objet** : l'arbitrage Q-2 du 2026-07-20 a décidé que la
  provenance manuel **n'est pas affichée à l'élève**. La traçabilité reste interne — auteurs et
  rapport de couverture. Aucun badge, aucune mention player, aucune clé i18n. La règle est
  conservée numérotée pour que l'étude et cette doctrine restent lisibles ensemble.

---

## 5. Comment se trace une reprise

Dans le fichier de la mission — `exercices/*.json`, et **lui seul** (ni `quiz.json`, qui gate la
compréhension du cours, ni les questions individuelles) :

```jsonc
{
  "title": "⭐⭐ Les exercices du manuel — Thalès",
  // …champs existants inchangés…
  "manuel": {
    "code": "222104P01", // optionnel — hérite de chapter.json `manuel.code` si absent
    "pages": "68-71", // optionnel — même grammaire que le chapitre
    "items": ["ex. 12", "ex. 13", "ex. 15a"], // REQUIS, 1 à 30, libellés ≤ 40 caractères
  },
}
```

- **`items` est requis** : un `manuel` sans item ne dit ni ce qui est repris, ni ce qui reste.
- **`code` s'hérite** du chapitre. S'il n'est résoluble nulle part, `content:check` **échoue** —
  une reprise qui ne nomme aucun manuel ne trace rien.
- Les `items` sont des **libellés de numérotation** (« ex. 12 »), jamais un indice de réponse.
- Le rapport de couverture (`npm run content:audit`) croise ces items avec ce que le **manifeste
  de programme** déclare du manuel, et rend `repris / déclaré` plus la liste nominale de ce qui
  reste. Il est **advisory** : une campagne en cours n'est pas une régression.

---

## 6. Trois exemples

**Maths — un problème à sous-questions (le cas le plus fréquent).**
Le manuel : « ABC est un triangle. M ∈ [AB] et N ∈ [AC] tels que (MN) ∥ (BC). AM = 4, AB = 6,
AC = 9. **a.** Calcule AN. **b.** Sachant BC = 12, calcule MN. » → **histoire-problème
séquentielle**, deux questions `numeric` dans l'ordre de l'énoncé, chacune rappelant le contexte
en une ligne (l'étape b ne suppose pas qu'on a lu l'étape a à l'écran précédent), figure SVG
redessinée à coordonnées re-dérivées, sans étiquette qui donne la réponse. Régime **(b) adaptée**,
tracé `items: ["ex. 14a", "ex. 14b"]`.

**SVT — une planche documentaire.**
Le manuel : une photographie de coupe de feuille, légendée, suivie de « Annote le schéma ». La
photo ne se reprend pas (R-11). Deux issues : si la notion est **schématisable**, un SVG simplifié
et une question `matching` légende↔structure ; sinon la question se rédige auto-suffisante
(« Dans une coupe de feuille, quelle structure porte les stomates ? ») et la planche authentique
reste consultable dans la galerie « Pages du manuel ». Dans les deux cas, la question se résout à
l'écran (R-3).

**Langue — un exercice sur un texte d'auteur.**
Le manuel : un extrait de roman sous droits, suivi de questions de compréhension. **L'extrait ne
se reprend pas** (R-11), donc les questions qui en dépendent non plus. Ce qui se reprend, c'est
la **notion travaillée** : si l'exercice interroge l'accord du participe passé, on écrit un texte
maison portant les mêmes occurrences. Régime **(c) variante** — donc **non tracé** : ce n'est plus
une reprise, et le rapport de couverture ne doit pas prétendre le contraire.

---

## 7. Ce qui n'est pas transposable, et pourquoi on l'écrit

Une construction à la règle et au compas, une manipulation de laboratoire, une mesure sur le
terrain : l'app ne les note pas, et prétendre le contraire serait pire que les omettre. Ces
exercices sont **listés dans la fiche programme avec leur raison** — c'est ce qui distingue « on
a choisi de ne pas le faire » de « personne ne l'a vu ». Une couverture partielle assumée vaut
mieux qu'un taux flatteur obtenu en oubliant ce qui résiste.
