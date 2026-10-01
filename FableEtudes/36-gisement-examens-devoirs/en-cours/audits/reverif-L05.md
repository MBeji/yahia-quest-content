# Re-vérification ciblée — lot L05 (ch. 04, missions 23 à 28)

Statut : **TERMINÉ** — rien n'a été modifié dans les dépôts.

## Verdict

**NO-GO, pour une seule retouche** : 27 Q3, option c. Le texte « 4 − a² » vient de **mon propre audit**. Il vaut 0 en a = 2 et devient négatif sur ]2 ; 4[ : c'est une longueur réfutée par l'intervalle posé dans l'énoncé. Il coïncide en outre avec la clé en a = 1, valeur admissible. Tout le reste est conforme. **GO dès que la retouche ci-dessous est appliquée.**

Retouche exacte, dans `27-examen-2017-generale-ex3-carre-plus-constante-aire-figure-minimum.json`, Q3 :
- option c : `4 − a²` → `(8 − a)/2` (muette).
  - C'est la hauteur mesurée depuis le centre du carré APRT au lieu du sommet R.
  - Valeurs dans ]2 ; 4[ sur tout ]0 ; 4[, donc jamais nulle, négative, ni plus longue que le côté.
  - Égale à la clé seulement en a = 0, qui est exclu.
  - 9 signes contre 5 pour la clé : la clé n'est pas strictement la plus longue.
  - Ne contient pas la chaîne « 4 − a ».
- explication : remplacer `أو طرح مساحة المربّع APRT أي a² بدل طول ضلعه a فيخرج 4 − a².` par `أو قياس الارتفاع من مركز المربّع APRT بدل رأسه R ، والمركز يبعد عن [AB] بـ a/2 ، فيخرج 4 − a/2 أي (8 − a)/2.` (rendu vérifié avec le moteur ec8c637).
- Autres candidats écartés :
  - `(4 + a)/2` : égal à la clé en a = 4/3.
  - `(4 − a)/2`, `4 − a/2` et `√(4 − a)` : contiennent « 4 − a » (vote par sous-chaîne), et `4 − a/2` se lit aussi (4 − a)/2.
  - `√(a² + (4 − a)²)` (longueur RD) : Pythagore n'est enseigné qu'au chapitre 09, après le 04.
  - Tout remplaçant de moins de 5 signes rendrait la clé strictement la plus longue.

## (1) Résolution à l'aveugle des questions modifiées

Repérage des changements par script contre `l05-backup-audited/files/`, sans afficher le contenu.
- **Énoncé ou options modifiés (14)** : 23 Q2 · 24 Q1, Q5, Q6 · 25 Q4, Q5, Q6, Q8, Q9 · 26 Q4 · 27 Q2, Q3, Q5, Q6.
- **Explication ou étiquettes seules** : 24 Q2, 26 Q1, 26 Q7.
- **Déplacées sans changement** : 26 Q5 (ancienne Q4) ; 28 Q6 (ancienne Q8) et 28 Q7. La 28 Q8 (ancienne Q6) passe de d2 à d3.

Réponses à l'aveugle, avant lecture des clés : 23 Q2 a · 24 Q1 c · 24 Q5 b (2x² + 2) · 24 Q6 b · 25 Q4 b · 25 Q5 a · 25 Q6 c · 25 Q8 b (30a − a² = 216) · 25 Q9 12 · 26 Q4 c · 27 Q2 a ((x − 1)² + 7) · 27 Q3 d (4 − a) · 27 Q5 c · 27 Q6 b ({ 1 }).

**Aucune divergence.** Les déplacées concordent aussi (26 Q5 b, 28 Q6 a, 28 Q7 −80, 28 Q8 c). Toutes les options ont été recalculées par sympy, et les 50 égalités des explications modifiées sont justes. `content:check` passe ; `content:qa --strict --subject math` sort à 0, sans aucun avertissement sur le chapitre 04.

## (2) Défauts du premier audit : corrigés ou non

| défaut | état | constat |
|---|---|---|
| M1 — 24 Q5 (clé = A affichée avant) | **corrigé** | Porte sur (x − 1)² + (x + 1)², clé 2x² + 2 affichée nulle part avant ; plan 2×2 complet |
| M2 — 25 Q8 (options sur 60 sans chemin ; clé = A = 0) | **corrigé** | Plus aucune option ne dépend du périmètre (désormais simple contexte) ; clé 30a − a² = 216 absente de tout énoncé antérieur |
| M3 — 25 Q9 (complétion du carré non enseignée) | **corrigé** | L'énoncé donne `a² − 30a + 216 = (a − 15)² − 9` ; reste d3 (a² − b², produit nul, choix) |
| M4 — 26 Q5 (clé = B affichée par Q4) | **corrigé** | Développement désormais en Q4, émis avant tout affichage de B ; « و B = √2 » remplacé par `0² − (1 + √2) × 0 + √2 = √2` |
| M5 — 27 Q2 (clé = E affichée par Q1) | **corrigé** | Choix de la forme « carré plus un nombre » ; (x − 1)² + 7 n'est affichée qu'après (Q5, Q6) |
| M6 — 27 Q6 { −1 } et { 7 } | **corrigé** | `مجموعة فارغة` et `{ 1 + √7 }` (≈ 3,65) : aucune option ne sort de ]0 ; 4[ |
| M6 — 27 Q5 d (a = 0 exclu) | **corrigé** | `S تساوي 11 عند a = 3 ، و 11 ≥ 7 ، إذن S ≥ 7` : 3 est dans l'intervalle, S(3) = 11 juste, 3 n'est pas une option de Q6 |
| M6 — 27 Q3 c « 4 + a » | **partiel** | Remplacé par `4 − a²`, lui-même réfuté par l'intervalle : voir le verdict |
| M7 — 28 Q8 (clé = A = 0 juste après Q7) | **corrigé** | L'équation transformée est désormais Q6, émise avant Q7 ; aucun énoncé antérieur n'affiche x² − 18x + 1 |
| m1 — étage de 23 | **corrigé** | d2 practice 75/15, titre ⭐⭐ |
| m3 — rendu de l'explication de 26 Q1 | **corrigé** | `3 × (3x) = 9x` s'affiche tel quel |
| m4 — étiquettes | **corrigé** | Voir (5) |
| m5 — titre de 28 | **corrigé** | « تعميل بمتطابقة » |
| m6 — ∅ en 25 Q6 | **corrigé** | `مجموعة فارغة` dans l'option et dans l'explication |
| m7 — libellés | **corrigé** | Aucune occurrence restante de « نعلم أنّه لكلّ عدد حقيقي » (remplacée par « … صحيحة لكلّ عدد حقيقي x ، وهي: »), « زوج مرتّب » (→ « ثنائية »), « القوى التنازلية », « تعميل بفرق مربّعين » ; 24 Q1 reformulée |
| m8 — comparaison de 28 en d3 | **corrigé** | Voir (3) |
| m2 — 27 Q4 (optionnel) | refusé par l'auteur | Accepté : c'était optionnel, et c'est l'étape officielle 2a |
| 28 Q11 | laissé tel quel | Accepté : simple observation, donnée officielle |

## (3) Défauts éventuellement introduits par les correctifs

- **Clé strictement la plus longue** : 0 sur 38 QCM (fonctions du moteur).
- **Positions de clé** : [10, 12, 10, 6], dans la bande.
- **Paires proches ≥ 0,45** : aucune, ni dans la tranche ni avec les chapitres 02, 03, 04, 17 et leurs quiz. Voisin maximal d'une question modifiée : 0,38 (24 Q5 ↔ 23 Q1).
- **Candidats gabarit** : aucun entre chapitres. Un seul cadre intra-chapitre atteint 0,60 (25 Q4 ↔ 27 Q5), à cause de la formule d'introduction désormais commune ; tâches différentes, sans effet sur le gate.
- **Vote par composante et plans 2×2** :
  - Complets et neutres : 24 Q5 (terme en x × constante), 25 Q8 (signe × a² ou 2a), 26 Q1 (trois étiquettes distinctes, sans option à deux erreurs), 26 Q4 (inchangé).
  - 27 Q2 : « (x − 1)² » figure dans trois options sur quatre, mais les constantes 7, 9, 4 et 8 sont toutes distinctes, donc aucune reconstruction ; seule l'option c, en (x − 2)², se distingue, et c'est un distracteur.
  - 27 Q6 : le chiffre 1 figure dans { 1 } et { 1 + √7 }, un indice faible (50 %).
- **Option somme ou différence de deux autres** : aucune, sauf 27 Q3, dont la clé « 4 − a » est « 4 » moins « a ». C'était déjà le cas au premier audit, et le remplaçant proposé est lui aussi une combinaison de 4 et de a, donc ne donne plus la clé seule.
- **Prémisse ou intervalle niés** :
  - 27 Q5 et Q6 : conformes.
  - 25 Q8 : conforme ; le périmètre est dans l'énoncé et aucune option ne le contredit ni n'en dépend.
  - 27 Q3 c : **non conforme** (verdict).
- **Fuites après les réordonnancements** :
  - 26 : le développement de Q4 et l'énoncé de Q5 permettent de déduire B(√2) = 0 (B = (x − 1)(x − √2)). Lien « déduire » normal ; aucune clé n'est écrite dans un énoncé ou une explication antérieurs.
  - 28 : l'explication de Q6 ne donne pas k = −80 ; Q7 ne livre rien à Q8 ; les « 81 et 80 » de l'explication de Q8 étaient déjà dans celle de Q5, émise avant.
  - Rampe de 28 : 2 ×7 puis 3 ×4, non décroissante.
- **Énoncé qui livre la méthode ou la clé** : 25 Q8 (« ننشر الجداء a(30 − a) ») et 25 Q9 (forme canonique) donnent la méthode à dessein, c'était le correctif ; aucune clé n'est donnée. Tous les énoncés se lisent seuls.
- **Égalité fausse dans une explication** : aucune.
- **Figures** : SVG de 27 Q3 et Q4 inchangés ; 27 Q4 est identique octet pour octet.
- **Écart de l'auteur en 25 Q8** : **l'auteur a raison.** Mon jeu {30a + a², 30a − a, 30a − 2a, 30a − a²} laissait voter : signe « − » dans trois options, terme « a² » dans deux, ce qui reconstruisait la clé. Le sien, {+, −} × {a², 2a}, est neutre. « 30a + a² » cumule deux erreurs, muette à juste titre.
- **Décision m8 (comparaison de 28 en d3)** : honnête. Il faut enchaîner trois notions : deux inverses ont le même signe (enseigné en 17), b > 0 donc a > 0, et ajouter 4√5 garde l'ordre. La rampe tient, sans fuite créée.
- **Observation non bloquante** : l'explication de 27 Q5 (« مع أنّه ينعدم عند انعدام أساسه »), émise avant Q6, réfute d'avance l'option « مجموعة فارغة » et oriente vers a − 1 = 0. C'est le lien voulu par le sujet (2b puis 2c) et la correction même de l'erreur. On peut l'adoucir en « مع أنّ المربّع قد يساوي 0 », sans obligation.

## (4) Rendu arabe

origin/main du moteur est désormais à ec8c637 : **#1141 est mergée**, ainsi que #1137 à #1139. Simulation `isolateLtrRuns` puis bidi-js en paragraphe RTL, sur les 155 lignes des six fichiers corrigés :
- **0 formule mal rendue** ;
- #1141 ne modifie l'isolation d'**aucune** ligne de la tranche (aucune incise arabe fermée ou ouverte par une formule) ;
- le correctif `3 × (3x) = 9x` est bien rendu, comme ma phrase de remplacement pour 27 Q3.

## (5) Étiquettes, lues sur origin/main

| placement | étiquette | nomme exactement l'erreur ? |
|---|---|---|
| 26 Q1 c `x + 2/3` | `math.int.produit-signes-negatifs` (élargie : signes contraires → négatif) | **oui** : (1/3) × (−2) pris positif |
| 26 Q1 d `9x − 6` | `math.frac.fraction-d-un-nombre-multipliee-au-lieu-de-divisee` | **oui** : multiplier par 3 au lieu de prendre le tiers |
| 26 Q7 b `{ −1 ; 3 + √2 }` | `math.alg.produit-nul-racine-signe-non-oppose` | **oui** : (x − 1) lu −1 ; l'explication est harmonisée |
| 25 Q8 a `30a + a² = 216` | `math.int.produit-signes-negatifs` | **oui** : a × (−a) pris positif, a étant une longueur |
| 25 Q8 c `30a − 2a = 216` | `math.num.operation-inverse-appliquee` | **oui** : a + a au lieu de a × a (« une somme au lieu d'un produit ») |
| 25 Q8 d `30a + 2a = 216` | muette | juste : deux erreurs |
| 24 Q5 a `2x²` | `math.alg.carre-difference-signes` | oui : (x − 1)² = x² − 2x − 1. Même ambiguïté bénigne qu'au premier audit, via (a − b)² = a² − b² |
| 24 Q5 d `2x² + 4x + 2` | `math.alg.carre-difference-signes` | **oui** : double produit de signe positif |
| 24 Q5 c `2x² + 4x` | muette | juste : deux erreurs |
| 27 Q2 b `(x − 1)² + 9` | `math.alg.carre-difference-signes` | **oui** : (x − 1)² = x² − 2x − 1, d'où 8 + 1 |
| 27 Q2 c `(x − 2)² + 4` | `math.alg.double-produit-sans-facteur-2` | **oui** : on croit que le terme du milieu de (x − 2)² vaut −2x (ab au lieu de 2ab) |
| 27 Q2 d `(x − 1)² + 8` | muette | juste : aucune étiquette du registre ne nomme l'oubli du − 1 |
| 23 Q5 b `4x(2x + 1)` (en attente) | `math.alg.facteur-commun-terme-non-divise` | **oui** : terme non divisé par le facteur, comme l'analogue publié 04/17 Q5 b |
| 23 Q5 c `(2x + 1)(2x − 1)` (en attente) | `math.alg.facteur-commun-reste-oublie` | **oui** : « un terme égal au facteur commun laisse 1 » |
| 25 Q6 a `مجموعة فارغة` | `math.alg.produit-nul-et-au-lieu-de-ou` (conservée) | oui |
| 24 Q2 a `3x² − 1204` | retirée | conforme à la demande |

Les deux étiquettes en attente existent sur origin/main mais pas dans le registre de l'arbre de travail (632 entrées contre 642) : les poser après rebasage, comme prévu par `pending-tags/L05.json`, qui ne crée aucune étiquette nouvelle.
