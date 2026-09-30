# Re-vérification ciblée — lot L07 (ch. 07 statistiques, missions 18–24)

Auditeur indépendant, contexte de l'audit initial. Méthode : questions modifiées extraites SANS clé,
explication ni étiquette, re-résolues, puis dévoilées ; recalculs exacts ; banc bidi (bidi.ts de
origin/main du moteur) + Chromium ; content:tranche ; étiquettes contre origin/main.

_Rédigé au fil de l'eau — sections complétées dans l'ordre._

## 1. Clés des questions modifiées — re-résolues à l'aveugle AVANT lecture

Périmètre des changements (diff par champ contre la copie d'avant correction, sans afficher de clé) :
exactement la liste de l'auteur — 19 Q6 ; 20 Q5, Q7 ; 21 Q7 ; 22 Q5, Q6, Q7 ; 23 Q1, Q4, Q6 ; 24 Q8, Q9.
Aucun en-tête, aucune difficulté, aucun id de clé n'a bougé ; 18 intact.

| Q | ma réponse (aveugle) | clé du fichier | |
|---|---|---|---|
| 19 Q6 | [3 ; 4[ ، [4 ; 5[ | d | ✓ |
| 20 Q5 | 33 سنة و6 أشهر | d | ✓ |
| 20 Q7 | 1765 (0×85 + 1×65 + 2×850) | c | ✓ |
| 21 Q7 | (8 ; 90) | d | ✓ |
| 22 Q5 | 45 (point (45 ; 830) au lieu de 900 ; figure inchangée) | a | ✓ |
| 22 Q6 | 458 (390 + 2 × 34) | d | ✓ |
| 22 Q7 | entre 27 et 30 (458 < 500 < 560) | b | ✓ |
| 23 Q1 | [300 ; 400[ | c | ✓ |
| 23 Q4 | 10، 55، 142، 242، 250 | d | ✓ |
| 23 Q6 | « أعلى ترتيبة فيه هي 250… » | a | ✓ |
| 24 Q8 | 2 + (220 − 120) × 2 ÷ (330 − 120) | a | ✓ |
| 24 Q9 | 2,95 (62/21 = 2,952…) | b | ✓ |

**12/12 clés confirmées, aucune divergence.** Explications recalculées : toutes justes
(22 Q6 : 730 − 390 = 340, 34/m³, 2 × 34 = 68, 390 + 68 = 458, 390 + 34 = 424 ; 22 Q7 : 1000 ÷ 2 = 500 ;
20 Q5 : 0,5 × 12 = 6 ; 20 Q7 : 65 + 1700 = 1765 ; 23 Q4 : 242 + 8 = 250 ; 24 Q9 : 2 + 200 ÷ 210 = 2,95).

## 2. Les six majeurs

| Majeur | État | Constat |
|---|---|---|
| M1 22 Q6 (intrus) | **corrigé** | 68, 340, 424, 458 : la clé n'est plus le seul non-multiple de 34 ; 424 et 458 sont tous deux « 390 + hausse », il faut la notion (2 m³ et non 1) pour choisir. Aucune option n'est somme ou différence de deux autres. Résiduel non bloquant (déjà là avant) : 68 et 340 sont sous 390, l'ordonnée lue à 25 sur la figure, donc éliminables par la seule croissance du polygone. |
| M2 19 Q6 (vote) | **corrigé** | Seule [4 ; 5[ figure dans 3 options, et elle reconstruit le distracteur [a], pas la clé. [3 ; 4[ et [2 ; 3[ sont à 2/4, [0 ; 1[ et [1 ; 2[ à 1/4. Clé à 17 signes contre 27. L'explication couvre la nouvelle option [b]. |
| M3 23 Q6 (marqueur) | **en partie** | La structure « لأنّ N هو … » est maintenant commune aux quatre options. Il reste un indice lexical : le mot « تكرار » est dans les trois distracteurs et absent de la clé. Retouche recommandée ci-dessous (§ 6, R1). [b] et [c] sont correctement étiquetées, [d] est muette. |
| M4 22 Q5 (option réfutée par l'énoncé) | **corrigé** | 45, 35, 25, 15 : aucune n'est réfutée par l'énoncé (seul le point (5 ; 0) y est posé). L'explication cite déjà 15, 25 et 35 comme points justes. |
| M5 22 Q7 (énoncé non autonome) | **corrigé** | Total « ألف عائلة » donné, donc moitié = 500 ; « بنفس الطريقة » supprimé. Reste en d3, après Q6 dont il redonne la clé 458 (ordre respecté). L'explication (1000 ÷ 2 = 500) est cohérente. |
| M6 24 Q9 (R-3) | **corrigé** | La médiane est définie dans l'énoncé (abscisse du point d'ordonnée 220 sur le segment) : la question se lit seule. |

## 3. Nouveaux défauts introduits par les corrections

**N1 — BLOQUANT — 24 Q8 : option réfutée par l'énoncé (c'est mon correctif facultatif m8 qui l'a introduite).**
- L'énoncé pose que le point est « على القطعة الواصلة بين النقطتين (2 ; 120) و(4 ; 330) », donc son abscisse est entre 2 et 4.
- La nouvelle [c] « 4 + (220 − 120) × 2 ÷ (330 − 120) » vaut 4,95 : « 4 + une quantité positive » dépasse 4 et s'élimine sans calcul.
- [b] « (220 − 120) × 2 ÷ (330 − 120) » vaut 0,95 < 2 : elle s'élimine de la même façon. Ce défaut existait avant ; je l'avais manqué au premier audit.
- En l'état, la question se réduit à [a] contre [d].
- Correctif exact : plan 2×2, qui garde toutes les valeurs dans ]2 ; 4[ et empêche le vote (« 2 + » et « 4 − » à 2/4 chacun, « × 2 » à 2/4) :
  - a « 2 + (220 − 120) × 2 ÷ (330 − 120) » (clé, inchangée, 2,95)
  - b « 2 + (220 − 120) ÷ (330 − 120) » (largeur 2 oubliée, 2,48) — étiquette `math.stat.interpolation-mal-posee`, à la place de `interpolation-borne-inferieure-oubliee`
  - c « 4 − (220 − 120) ÷ (330 − 120) » (départ à 4 et largeur oubliée, 3,52) — `math.stat.interpolation-mal-posee` (placement déjà prévu)
  - d « 4 − (220 − 120) × 2 ÷ (330 − 120) » (départ à 4, 3,05) — inchangée, `interpolation-mal-posee`
  - Longueurs : clé 33 = d 33, b et c 29, donc la clé n'est pas strictement la plus longue.
  - Aucune option n'est somme ou différence de deux autres.
  - Pas de fuite : les valeurs de b (2,48) et de d (3,05) sont les distracteurs de Q9, qui suit.
  - Nouvelle phrase d'erreur de l'explication, qui remplace « الخطأ الشائع: … بالجمع. » :
    > الخطأ الشائع: الاكتفاء بالنسبة (220 − 120) ÷ (330 − 120) دون ضربها في عرض القطعة 2؛ أو الانطلاق من الفاصلة 4 بالطرح بدل الانطلاق من الفاصلة 2 بالجمع، مع الضرب في عرض القطعة أو بدونه.

**Aucun autre nouveau défaut :**
- Clé strictement la plus longue : 0 dans 18 à 24 (`content:tranche`).
- Vote : 19 Q6 réglé ; 24 Q8 réglé par N1.
- Somme ou différence : aucune.
- Prémisse niée : seulement 24 Q8 (N1).
- Fuite en avant : aucune. L'énoncé de 22 Q7 redonne 458 après Q6 ; la phrase fautive de l'explication de 23 Q4 est bien supprimée ; l'explication de 23 Q1 ne livre aucune clé.
- Autonomie des énoncés : 22 Q7 et 24 Q9 se lisent maintenant seuls.
- Paires proches : aucune ≥ 0,45. `content:tranche` ne liste que les 12 paires anciennes entre 01 et 05 ; mon Jaccard sur énoncé seul culmine à 0,43 (24 Q8 ↔ Q9), 0,40 avec les options.
- Arithmétique des explications : toute juste.

## 4. Rendu des chaînes modifiées

Testé avec le `bidi.ts` d'`origin/main` du moteur, qui intègre #1137 (espaces de bord hors du run) et #1138 (ponctuation et parenthèses de bord hors du run).
- Seuls des intervalles, des points et deux formules d'explication sont isolés : aucune inversion.
- Les titres « (تقني) » se rendent nativement.
- 19 Q6 [b] se lit de droite à gauche dans l'ordre des classes.
- « … هو 220. » et « 0,01 ؟ » sont corrects.
- Chromium, polices de l'app : **0 débordement** pour tous les énoncés, options et explications du lot, à 278, 308 et 340 px. Le défaut de rendu que j'avais relevé au premier audit est donc résolu côté moteur.

## 5. Étiquettes

**Les 24 placements** portent tous sur des distracteurs muets, jamais sur une clé ni sur une option déjà étiquetée. Couverture en questions distinctes : A 4, C 5, cumul décalé 5, P 4, interpolation 5, toutes ≥ 3.
- **A** (19 Q6 c, 19 Q7 c, 22 Q4 b, 24 Q6 b) : exact. Chaque option compte la classe qui finit au seuil ([2 ; 3[, [25 ; 35[, [2 ; 4[).
- **C** (18 Q6 b, 21 Q6 b, 22 Q4 d, 23 Q5 d, 24 Q6 d) : exact. Chaque option oublie au moins une classe concernée.
- **Cumul décalé** (21 Q5 c, 23 Q4 b : cumul à la borne inférieure ; 22 Q3 a, 24 Q5 a : classe suivante incluse ; 21 Q7 b : cumul 90 posé à 6) : exact, 21 Q7 b compris (le point du cumul de [6 ; 8[ est décalé d'une classe).
- **P** (21 Q9 a, 22 Q8 d, 24 Q9 c : centre ; 23 Q7 d : borne 300) : exact.
- **Interpolation mal posée** (21 Q9 c largeur, 22 Q8 a rapport, 23 Q7 a départ, 24 Q8 d départ, 24 Q9 a largeur) : exact. 24 Q8 c reste valable sur la nouvelle option c de N1 ; **ajouter 24 Q8 b** (nouvelle b de N1). Total : 25 placements.

**Libellés** : les versions fr sont toutes justes, chacune une seule phrase. Quatre retouches de formulation (non bloquantes) :
- **C en** : « on the right side » est ambigu (droite ou bon côté ?). Proposé : « You leave out some of the classes concerned: every class on the required side of the threshold counts ».
- **Cumul décalé en** : « not only … nor … » est bancal. Proposé : « You shift the cumulative count by one class: it counts the values strictly below the class's upper bound — neither just those below its lower bound, nor those of the next class as well ».
- **Cumul décalé ar** : « القيم التي تشمل الفئة التالية » n'a pas de sens (des valeurs ne « contiennent » pas une classe). Proposé : « تُزيح التكرار المجمّع بفئة واحدة: هو يعدّ القيم الأصغر قطعًا من الطرف الأكبر للفئة، لا القيم الأصغر من طرفها الأصغر وحدها، ولا قيم الفئة التالية معها ».
- P et interpolation : justes dans les trois langues (l'ar de l'interpolation décrit correctement a + (N/2 − cumulé) ÷ effectif × largeur).

**Libellé élargi de `math.stat.effectif-cumule-non-cumule`** (les deux sens) : exact.
- **Il reste vrai pour toutes les options qui le portent** : les 16 de `origin/main` (ch. 07 seulement : 01 Q6 a ; 09 Q5 a ; 10 Q3 c ; 11 Q3 a, Q6 d ; 12 Q3 a, Q6 a, c ; 14 Q3 a, Q4 b ; 15 Q3 a, Q6 a ; 17 Q5 c, d, Q6 b) et les 8 du lot (18 Q4 b, 21 Q5 b, 22 Q3 d, 23 Q4 a, 24 Q5 d, 21 Q7 c, 23 Q6 b, c).
  - Toutes donnent l'effectif (ou la fréquence) d'une seule valeur ou classe là où le cumulé était attendu.
  - Réserve antérieure : 6 options de `main` sont des fréquences ou des pourcentages et le libellé dit « effectif ». C'est vrai sur le fond ; « l'effectif (ou la fréquence) » serait plus exact.
- **Version en à ajouter** : « You confuse a class's (or a value's) count with its cumulative count: the cumulative adds up every count up to it, the count covers it alone ».
- **Une fois le libellé élargi**, étiqueter les deux options de sens inverse, aujourd'hui muettes : 18 Q5 [d] (classe au plus grand cumulé prise pour modale) et 24 Q7 [a] (plus petite ordonnée lue comme plus petit effectif).

## 6. Verdict : **NO-GO** — une retouche bloquante (24 Q8), puis GO

**Bloquant**
- **E1. 24 Q8** (fichier `24-examen-2018-technique-ex2-ordinateur-eleves-polygone-mediane.json`, question 8) :
  - option b → « 2 + (220 − 120) ÷ (330 − 120) », étiquette `math.stat.interpolation-mal-posee` (retirer `math.stat.interpolation-borne-inferieure-oubliee`) ;
  - option c → « 4 − (220 − 120) ÷ (330 − 120) », étiquette `math.stat.interpolation-mal-posee` ;
  - a et d inchangées ;
  - dans l'explication, remplacer toute la phrase « الخطأ الشائع: … بالجمع. » par :
    > الخطأ الشائع: الاكتفاء بالنسبة (220 − 120) ÷ (330 − 120) دون ضربها في عرض القطعة 2؛ أو الانطلاق من الفاصلة 4 بالطرح بدل الانطلاق من الفاصلة 2 بالجمع، مع الضرب في عرض القطعة أو بدونه.
  - dans `pending-tags/L07.json`, ajouter `{"file":"24","q":8,"opt":"b","id":"math.stat.interpolation-mal-posee"}`.

**Recommandé, dans le même passage**
- **R1. 23 Q6 [a]** → « أعلى ترتيبة فيه هي 250، لأنّ 250 هو التكرار الكلّي » (50 signes contre 56 pour les distracteurs ; « تكرار » dans les quatre options ; toujours vrai ; aucune fuite).
- **R2. Libellés** : C en, cumul décalé en et ar (textes exacts au § 5) ; ajouter la version en du libellé élargi.
- **R3. Après l'élargissement** : placer `math.stat.effectif-cumule-non-cumule` sur 18 Q5 [d] et 24 Q7 [a].

**Facultatif**
- **O1. 22 Q6** : remplacer « 68 » par « 662 » (730 − 2 × 34 : on part du mauvais bout) donnerait 340, 424, 458, 662, dont trois dans l'intervalle [390 ; 730].
  - Clause d'explication à ajouter : « أو طرح زيادة المترين المكعّبين من ترتيبة النقطة ذات الفاصلة 35، 730 − 68 = 662، مع أنّ 27 تبعد عن 35 بثمانية أمتار مكعّبة ».
  - Non requis.

**Après E1, GO.** Il suffit de re-contrôler 24 Q8 (et 23 Q6 si R1 est appliqué) ; le reste du lot est validé : 54 questions, 54 clés justes, six majeurs traités.
