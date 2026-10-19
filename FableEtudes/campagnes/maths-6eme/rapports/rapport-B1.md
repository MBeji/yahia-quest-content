# Rapport de l'auteur B1 — maths 6ᵉ, chapitres 01 à 06

Lot : `01-entiers-naturels`, `02-operations-naturels`, `03-nombres-decimaux`, `04-addition-soustraction-decimaux`,
`05-multiplication-division-decimaux`, `06-multiples-communs` (mise à niveau). Table détaillée des écarts, de ce qui a été
fait et des reprises : `auteurs-notes/B1/NOTES.md`. Base de comparaison : commit `07451934`.

## En une phrase

Les six cours étaient déjà au patron et conformes à la fiche (tous les calculs recalculés, aucune coquille) : les
écarts étaient dans les **quiz et exercices** (notions enseignées mais jamais exercées, dont la **division par un décimal
du ch. 05 : zéro question sur 35**) et dans quelques **défauts de question** que seule une relecture complète pouvait voir.

## Chiffres

| chapitre | questions remplacées / corrigées | questions ajoutées | reprises déclarées |
| --- | --- | --- | --- |
| 01 | 7 | 0 | — |
| 02 | 2 | 3 | — |
| 03 | 7 | 0 | — |
| 04 | 8 | 1 | 3 fichiers (ex. 2, 4, 10 du manuel) |
| 05 | 13 | 1 | 4 fichiers (ex. 2 أ, 2 ب, 5, 7 du manuel) + 1 épreuve du guide (T1 sit. 1) |
| 06 | 9 | 2 | 2 fichiers (ex. 4, 6 du manuel) |

Aucun slug, `displayOrder`, nom de fichier, en-tête, étoile ou récompense modifié ; aucun identifiant de question ne
bouge (remplacements au même rang et à la même difficulté, ajouts en fin de fichier à difficulté ≥ au maximum).

## Écarts de fond trouvés et corrigés

- **05** : la division par un décimal (✅, prérequis de 5ᵉ) n'était exercée nulle part → 7 items (quiz Q5 inclus) +
  estimation du produit + zéro intercalaire du quotient + reprise de l'offre à tempérament du T1 (guide p.169, 173–174).
- **04** : terme manquant (ex. 4), estimation, conversion d'unités dans une somme, retenue qui traverse la virgule
  (ex. 2), problème de la balance (ex. 10).
- **06** : somme de deux multiples (quiz), trois nombres (« فأكثر »), intervalle par le PPCM, reste constant,
  reprises ex. 4 et 6, bus et coureurs ; un exercice `multi`.
- **02** : division euclidienne « à l'envers », avec reste de problème (nombre de cars), condition r < b isolée.
- **01 / 03** : milliards (vocabulaire), lecture d'un décimal à zéro intérieur, encadrement entre entiers consécutifs.

## Défauts de question trouvés dans le contenu servi (corrigés)

1. 01 `05-entrainement` Q2 : **deux réponses défendables** (« ثلاثمئة ألفٍ وخمسة آلاف وأربعون » = 305 040 = la clé).
2. 03 `05-entrainement` Q5 : deux options équivalentes (« متساويان » et « 0,408 = 0,41 »).
3. 03 `04-defi` Q5 : « 8,350 » et « 8,35 », même nombre.
4. 01 `04-defi` Q3 : option éliminée à vue par l'énoncé.
5. 03 `05-entrainement` Q6 : « le plus proche de 1,6 » sans borne.
6. **7 clés strictement les plus longues** (01 boss Q1, 02 quiz Q5, 04 quiz Q1, 05 boss Q3 / entr. Q4 / Q5, 06 boss Q5).
7. Rendu : 5 `**gras**` coupés par un retour à la ligne (01 ×1, 05 ×4) affichaient leurs astérisques.

## Contrôles

`content:check` ✓ ; `content:qa --subject math-6eme` : 0 erreur sur le lot (restent 2 erreurs en `19` et 3 avertissements
en `14`, hors lot) ; `content:figures:check` : rien sur le lot ; `content:tranche … --fresh --strict-longest
--strict-lessons` ✓ ; sur les 6 chapitres entiers 0/211 clé la plus longue et 0 paire proche (18 au départ) ; prettier ✓ ;
rendu des cours et résumés : aucun résidu Markdown ; scan de notation : 0.

## Étiquettes à créer (proposition — non créées)

- `math.num.division-virgules-deplacees-inegalement` (seuil de 3 questions atteint : cinq options muettes listées dans les
  notes ; à ajouter ensuite à `coursePitfalls` du ch. 05).
- `math.num.reste-ignore-dans-le-probleme` et `math.mes.unites-melangees-sans-conversion` (une occurrence chacune : seuil non atteint).

## Doutes pour l'auditeur

1. Reprise `أقيّم 10` (04) : le cours utilise déjà les mêmes masses comme ancrage — reconnaissance possible.
2. Reprise T1 (05) déclarée avec le code `502603` (guide) au niveau de l'exercice, comme `14/04-defi` ; offres 1 et 3
   laissées (fractions 1/5 et 1/10, ch. 08 et 13).
3. Les données de ex. 7, 9, 10, 11 et de la situation des bus (leçon 13) sont déjà les exemples du cours `06` : ces items
   ont été réécrits avec d'autres données (variantes, non tracées) pour ne pas redonner la réponse du cours.
4. Non exercés volontairement (◐) : moyenne, problèmes « somme et différence », trois multiples consécutifs de somme donnée.
5. Le commit de sauvegarde du pilote (`c7c0dc06`) contient une version intermédiaire de ce travail ; les fichiers finaux
   sont ceux de l'arbre de travail.
