# Re-vérification ciblée L10 — `08-thales`, missions 13 à 20 (après application de l'audit)

> **État : TERMINÉ** (verdict global ci-dessous ; journal de progression en annexe).
>
> - Fichiers : arbre de travail de `/home/user/yahia-quest-content`, `content/math/08-thales/exercices/13…20`
>   (état final de l'auteur, y compris l'en-tête de 19 en d2 practice 75/15 ⭐⭐ et 17 Q3 `a` muette).
> - Référence avant audit : `scratchpad/l10-backup-audited/` ; registre et missions publiées : `origin/main`
>   du corpus à `4f72f94b` (645 identifiants, refetché : inchangé) ; moteur `origin/main` à `ce46894c`
>   (arena#1142) pour `bidi.ts` et les gates ; étiquettes en attente : `scratchpad/pending-tags/L10.json`.
> - Méthode : les 47 questions re-résolues à l'aveugle (script : énoncé + options, sans clé, sans
>   explication, sans étiquette) **avant** toute lecture de clé ; diff mot à mot question par question
>   contre la sauvegarde ; chaque option neuve recalculée sous les données du NOUVEL énoncé ; questions
>   modifiées recalculées par deux méthodes ; figures relues par coordonnées et rendues en Chromium ;
>   rendu arabe simulé avec `splitMathRuns` / `isDisplayEquation` du moteur, positions mesurées ;
>   gates du moteur sur un bac à sable = `origin/main` + les 8 fichiers du lot (aucun fichier des dépôts
>   modifié). Notes de l'auteur non lues (zéro confiance).

## Verdict global

**À corriger avant livraison — 4 défauts, tous à correctif court et exact (textes complets plus bas) :**

| # | où | gravité | origine | objet |
| --- | --- | --- | --- | --- |
| D1 | 17 Q2 | **majeur** | MON texte du 1er audit | le vote terme à terme reconstruit la clé (chaque distracteur ne change qu'un terme de la clé) |
| D2 | 13 Q1 | **majeur** | préexistant, **manqué au 1er audit** (lacune du moteur) | l'énoncé « (3/21)³ », seul sur sa ligne, s'affiche « ³(3/21) » |
| D3 | 19 Q3 | mineur | MON correctif (ligne de données) | « بتعويض هذه الأطوال » ne s'exécute plus et pousse vers 2/6 = FB/4 |
| D4 | 17 Q4, Q6, Q7 | mineur (recommandé) | préexistant en Q4, étendu à Q6 par MON correctif | figure à l'échelle de x = 2 : options de Q4 et Q6 testables en x = 2 |

Tout le reste est **OK** : 47/47 clés retrouvées à l'aveugle ; aucune option neuve vraie sous les données
de son énoncé, aucune prémisse niée, aucune option somme/différence de deux autres, aucune clé strictement
la plus longue, aucune fuite en avant, rampes non décroissantes, aucune notion hors programme ni hors
ordre du manifeste, aucun doublon avec le publié, les deux correctifs déjà repris par l'auteur (17 Q6,
19 Q8) sont justes. Les 3 étiquettes nouvelles passent le seuil (avec une réserve de comptage, § Étiquettes).
**Après D1 à D4 (vérifiés en bac à sable : gates vertes, rendu correct), la tranche est livrable.**

---

## Verdict par question modifiée

### 13 — 2010 technique ex1 (d2 practice 75/15, rampe 2·2·2·2)

| Q | changement | aveugle | clé | verdict |
| --- | --- | --- | --- | --- |
| 1 | — (inchangée) | 1/343 | a | **DÉFAUT D2** (rendu de l'énoncé, préexistant) |
| 2 | « 1 » → « 12,5 » (`racine-confondue-avec-moitie`), « 5 » → `racine-distribuee-sur-somme`, options réordonnées 25 · 12,5 · 7 · 5 | 7 | c | **OK** — 8 + 4,5 = 12,5 ✓ (√ pris pour la moitié : libellé exact) ; √(16 + 9) = 5 (libellé élargi « ou tu fusionnes deux racines ainsi » : exact) ; 25 muette ; ni somme ni différence (7 + 5 = 12 ≠ 12,5) ; clé la plus courte |
| 3 | « 62,5 » → officiel « 47,5 » muet, réordonnées 30 · 40 · 47,5 · 60 | 40 | b | **OK** — 50 ÷ 20 = 2,5 puis 50 − 2,5 = 47,5 ✓. Résidu de vote chiffre à chiffre (dizaine 4 dans 40 et 47,5) **hérité du triplet officiel 30 / 47,5 / 40** : seul un 4ᵉ choix de dizaine 3 le casserait, et aucune erreur réelle ne le produit ; 60 (addition au lieu de soustraction, `operation-inverse-appliquee` exacte) est le bon 4ᵉ. Accepté. |
| 4 | figure : C(285 ; 205) | IJ = AC/2 | d | **OK** — A(70;50), B(40;205), C(285;205) : AB ≈ 158, BC = 245, CA ≈ 265 (scalène net) ; I(55;127,5), J(162,5;205) milieux exacts ; IJ = ½ AC vectoriellement (107,5 ; 77,5) ✓ ; codage simple sur [AB] au milieu de [AI] et [IB], double sur [BC] au milieu de [BJ] et [JC] ✓ ; étiquettes dans le `viewBox` (rendu Chromium) ; énoncé inchangé ; en attente `droite-des-milieux-mauvais-cote` sur `a` (AB porte I) et `b` (BC porte J) : exécution exacte ; `c` (2 × BC) double erreur, muette ✓ |

### 14 — 2011 technique ex3 (d2 practice 75/15, rampe 1·2·2·3)

| Q | changement | aveugle | clé | verdict |
| --- | --- | --- | --- | --- |
| 1 | `b` = points + parallèle + réciproque ; figure sans « نهر » | c | c | **OK** — vrai 2×2 (hypothèses complètes / sans parallèle × directe / réciproque), vote à égalité sur les deux axes ; `b` fausse sans ambiguïté (la réciproque conclut au parallélisme, elle ne donne pas les rapports) ; longueurs a 78 · b 82 · c 71 · d 68 |
| 2, 3 | figure seule (« نهر » retiré) | 1,5/6 = 2/AC · 8 | d · a | **OK** — seul le `<text>` « نهر » a disparu (diff de chaîne), le `<title>` nomme toujours le fleuve ; même SVG dans Q1–Q4 |
| 4 | ancienne Q4 + Q5 → une 2b « en mètres » depuis les données brutes, d3 | 80 | b | **OK** — AC = 2 × 6 ÷ 1,5 = 8 cm, 8 × 1000 = 8000 cm = 80 m ✓ ; 45 (AC/BC = BE/DE ⇒ 4,5 cm, `thales-rapport-inverse`, même mécanisme que 14 Q3 `d`), 800 (÷ 10, `puissance-de-dix-rangs-mal-comptes` exact), 450 (les deux, muette) : plan 2×2, vote nul (chiffres 4/8 et 5/0 à égalité), aucune somme/différence, aucune option vraie ; l'énoncé ne contient ni 1,5/6 = 2/AC, ni 8, ni la réponse de Q1 ; l'explication rappelle les clés de Q2 et Q3, émises AVANT (d2 < d3) ✓ ; énoncé autonome (« المنزلين A و C ») |

### 15 — 2017 technique ex1 (d2 practice 75/15)

| Q | changement | aveugle | clé | verdict |
| --- | --- | --- | --- | --- |
| 1 | `a` « 3 » → `racine-distribuee-sur-somme` | √3 | d | **OK** — √(12 − 3) = 3, exactement le cas « fusion de deux racines » du libellé élargi ; l'explication le décrit |
| 3 | (fichier inchangé) en attente `droite-des-milieux-mauvais-cote` sur `b` 3,5 et `d` 2,5 | 3 | a | **OK** — 3,5 = AC/2 (AC porte J), 2,5 = AB/2 (AB porte I) : exécution exacte |

### 16 — 2003 ex3 (d3 boss 120/30, rampe 1·2·2·2·3·3)

| Q | changement | aveugle | clé | verdict |
| --- | --- | --- | --- | --- |
| 1 | « النقطة أو النقاط » | B seule | b | **OK** — figure inchangée (B dessinée en (3 ; −2), fausse à dessein) |
| 2 | `b` → « (0,5 ; −0,5) » muette + explication | (0 ; 0) | c | **OK** — (−2 + 3)/2 = 0,5 et (2 + (−3))/2 = −0,5 ✓ ; ni extrémité ni somme d'options ; pas de vote par composante (abscisses −4, 0,5, 0, 2 et ordonnées 6, −0,5, 0, 3 toutes distinctes) ; en attente `milieu-difference-au-lieu-de-somme` sur `a` (−4 ; 6) = B − C : couvert par « (ou la différence entière) » |
| 3 | légère reformulation | (0 ; 3) | d | **OK** |
| 4 | « O من [BC] » + `<title>` « O من [CB] » | CO/CB | a | **OK** — seule la chaîne du titre a changé ; l'énoncé ne redonne plus la clé de Q2 |
| 5 | reconstruite d3 depuis les coordonnées : 5 · 6 · 3 · 1,5 | 6 | b | **OK** — deux méthodes : (CA) : y = 3x − 9, y = 3 ⇒ M(4 ; 3), BM = 6 ; Thalès dans CBM, O milieu de [BC] : 3/BM = 1/2 ⇒ 6. 5 = M pris au-dessus de A (M(3 ; 3) n'est pas sur (CA)) ; aucune option ne contredit une donnée ; l'explication ne donne ni M(4 ; 3) (clé de Q6, émise après) ni rien d'autre en avant ; « 12 » et la règle k² ont disparu |
| 6 | sans « BM = 6 » ; explication refait BM par Thalès | (4 ; 3) | c | **OK** — −2 ± 6 ⇒ 4 ou −8, (CA) croissante ⇒ 4 ; contrôle « milieu de [CM] = A » juste ; « معلّم » est le terme du cours 12 ; en attente `position-relative-ignoree` sur `a` (−8 ; 3) : exact (« et de quel côté ») |

### 17 — 2010 générale ex3 (d3 boss 120/30, 7 questions, rampe 1·2·2·2·3·3·3)

| Q | changement | aveugle | clé | verdict |
| --- | --- | --- | --- | --- |
| 2 | étape de développement | x² + 2x + 1 − 9 | d | **DÉFAUT D1** (vote terme à terme) ; étiquettes `a`, `b`, `c` exactes ; égalités de l'explication justes |
| 3 | `a` (x − 8)(x + 10) muette | (x − 2)(x + 4) | c | **OK** — le libellé de `difference-carres-second-terme-non-eleve-au-carre` décrit l'erreur de DÉVELOPPEMENT (« 7 − 2 au lieu de 7 − 4 ») ; ici c'est la factorisation (9 pris pour b au lieu de 3) : la muette est la bonne décision (je retire ma suggestion du 1er audit) |
| 4 | déplacée avant Q5 (texte inchangé) | x/4 = 2/(x + 2) | a | **OK** (voir D4 pour la figure) |
| 5 | solution de A = 0 depuis A = (x + 1)² − 9 seule, d3 | {−4 ; 2} | b | **OK** — (2 + 1)² − 9 = 0 et (−4 + 1)² − 9 = 0 ✓ ; en attente `produit-nul-une-seule-solution` (présente sur `origin/main`) sur `c` {2} : libellé exact pour « الاكتفاء بالعامل الأوّل » ; l'énoncé ne donne pas la factorisation ; l'explication rappelle la clé de Q3 (émise avant) et ne livre pas l'aire |
| 6 | produit en croix depuis la figure ; 2×2 neuf | x² + 2x = 8 | d | **OK** — en x = 2 : `d` 8 = 8 ; `a` x² + 2x = 2x + 8 : 8 ≠ 12 ; `b` x² + 2 = 8 : 6 ≠ 8 ; `c` x² + 2 = 2x + 8 : 6 ≠ 12 — **aucun distracteur vrai en x = 2**, aucun équivalent à la clé ; mécanismes justes (x/(x + 4) = 2/(x + 2) ⇒ x² + 2x = 2x + 8 ; x × (x + 2) → x² + 2) ; vrai 2×2, vote à égalité (membre gauche x² + 2x / x² + 2 ; membre droit 8 / 2x + 8) ; clé non la plus longue. Figure : voir D4 |
| 7 | 3b fusionnée (x depuis (x + 1)² − 9 = 0, puis aire AEF) | 8 | c | **OK** — 16 / 12 (BEF : 6 × 4 ÷ 2) / 8 / 2 (ABC) justes ; Q5 et Q7 ne se donnent pas leurs clés (Q7 donne l'équation, pas l'ensemble ; Q5 ne parle pas d'aire) ; chaînes des figures distinctes (Q4 ≠ Q6 par le `<title>` ; Q7 = ancienne Q8 avec AEF grisé) |

### 18 — 2016 générale ex2 (d3 boss 120/30, 8 questions, rampe 1·2·2·2·2·2·2·3)

| Q | changement | aveugle | clé | verdict |
| --- | --- | --- | --- | --- |
| 3 | (inchangée) en attente `position-relative-ignoree` sur `a` a² − 1 | a² + 1 | d | **OK** — l'explication (« إهمال الشرط M ∉ [OE] فنطرح ») exécute exactement l'erreur |
| 4 | « M من نصف المستقيم [OJ) حيث OM > 1 » | OK/OA = OJ/OM | a | **OK** — OM > 1 met J sur [OM], K sur [OA] ; plus de M(0 ; a² + 1) dans l'énoncé |
| 5 | depuis A(a ; 0), E(0 ; a²), EM = 1, M hors de [OE] ; figure de Q4 | a/(a² + 1) | b | **OK** — Thalès et coordonnées concordent ; `c` (÷ OA) porte `operation-inverse-appliquee`, libellé `origin/main` **confirmé** : « … une division au lieu d'une multiplication (ou l'inverse) » (ar « أو قسمةً بدل الضرب أو العكس ») ; idem Q2 `a` ; E(0 ; a²) est une donnée officielle (fuite S, même classe que Q3 ← Q2) ; le SVG de Q5 est celui de Q4 (B et (BI) ∥ (AE) y figurent sans être nommés : sans conséquence) ; aucune paire proche (tranche) |
| 6 | `a` → `produit-signes-negatifs` | x² − (5/2)x + 1 | c | **OK** — x × (−1/2) pris positif : « signes contraires ⇒ négatif », libellé exact ; 2×2 avec `b`, `d` double muette |
| 8 | Q8 + Q9 + Q10 → une question d'argumentation d3 | a = 2 … I منتصف | a | **OK** — sympy : racines 1/2 et 2, contrôle 2/(4 + 1) = 2/5 ; `a` vraie ; `b`, `c` fausses (1/2 exclu par a > 1 ; pour a = 1/2, I ∉ [OA]) ; `d` fausse (OI ≠ OA vrai mais non pertinent : IA = 1 = OI) ⇒ **une seule réponse défendable** ; 2×2 (valeur de a × jugement), vote à égalité sur le jugement ; longueurs 46 · 51 · 49 · 48 ; « a = 1/2 » dans `b`/`c` contre a > 1 : c'est la contrainte testée (`solution-hors-contrainte-gardee`), pas une prémisse niée par une méta-option ; énoncé : OK = a/(a² + 1) et l'identité sont des données officielles (fuites S, tolérées), la clé de Q7 n'y est pas ; aucune explication antérieure ne donne a = 2 |

### 19 — 2013 technique ex2 (désormais d2 practice 75/15 ⭐⭐, rampe 1·2·2·2·2·2·2·2)

| Q | changement | aveugle | clé | verdict |
| --- | --- | --- | --- | --- |
| en-tête | d2 · practice · 75/15, titre ⭐⭐ | — | — | **OK** (aucun résultat dans le titre) |
| 2 | `c`/`d` : « لأنّ D و E و F على استقامة واحدة » + explication | a | a | **OK** — avec la prémisse « ABCD مستطيل » : (FB) ⊥ (AB) (BEF rectangle en B, E ∈ (AB)) et (AD) ⊥ (AB) ⇒ `a` seule valide ; l'alignement de D, E, F n'implique aucun parallélisme ⇒ `c`, `d` fausses sans ambiguïté ; 2×2, longueurs 94 · 105 · 97 · 108 |
| 3 | « AD = 4 ، DC = 6 ، EB = 2 » + préfixe « AB = DC = 6 ، فـ EA = 6 − 2 = 4 » | 2/4 = FB/4 | d | **DÉFAUT D3** (consigne) ; données conformes au sujet officiel (AD = 4 cm, DC = 6 cm, EB = 2 cm), aucune prémisse contredite, pas de paire proche avec Q4 (tranche) |
| 4 | mêmes données | 2 | b | **OK** — 4 × FB = 8 ⇒ 2 ; 4 × 4 ÷ 2 = 8 ; 4 × 2 ÷ 6 = 4/3 ✓ |
| 5 | `a` 2000 → `reponse-a-l-autre-inconnue` ; « 0,02 m بدل 20 m » | 20 | c | **OK** — résultat intermédiaire en cm : libellé exact (« ou un résultat intermédiaire ») ; rendu bidi de la nouvelle tournure correct |
| 6 | glose « 1 cm ↔ 1000 cm » ; 400 · 200 · 20 · 40 | 200 | b | **OK** — 20 m × 20 m ÷ 2 = 200 ✓ ; 400 sans moitié, 20 = 2 cm² × 10 (`conversion-aire-facteur-errone` : « par 100, pas par 10 », exact), 40 = les deux (muette) : vrai 2×2, vote nul ; glose sans la clé de Q5 ; d2 cohérent avec la mission d2 |
| 7 | reformulée, d2 | 200 × p ≥ 18000 | a | **OK** — l'explication s'arrête à l'inéquation (ne donne pas 90, clé de Q8 émise après) |
| 8 | depuis les données (200 m², 18 000, prix minimum) : 900 · 1/90 · 1/900 · 90 | 90 | d | **OK** — 18000 ÷ 200 = 90 ; 200 × 90 = 18000 ✓ ; 900 est un prix qui suffit mais pas le minimum (faux), 1/90 et 1/900 ne suffisent pas ; aucune option ne contredit les 200 m² ; vrai 2×2 (sens de la division × zéros), triade 9/90/900 supprimée ; énoncé fidèle à la question 4 officielle ; 200 m² est une donnée officielle (« أثبت أنّ … 200m² » : fuite S) |

### 20 — 2025 technique ex3 (désormais d2 practice 75/15 ⭐⭐, rampe 1·1·2·2·2·3)

| Q | changement | aveugle | clé | verdict |
| --- | --- | --- | --- | --- |
| en-tête | d2 · practice · 75/15, ⭐⭐ | — | — | **OK** |
| 3 | « (AB) و (PH) عموديان على (MH) » + préfixe ; options permutées (clé en `d`) | MA/MH = AB/PH | d | **OK** — l'énoncé ne donne plus la clé de Q2 ; 2×2 inchangé |
| 4 | `a` 1/10 → `reponse-a-l-autre-inconnue` | 9/10 | b | **OK** (AH/MH : autre grandeur que celle demandée) |
| 5 | MA = 2700, MH = 3000, PH = 60 + explication | 54 | d | **OK** — 2700/3000 = 9/10, 60 ÷ 10 × 9 = 54 ✓ ; la clé de Q4 n'est plus dans l'énoncé |
| 6 | `b` 54 → `reponse-a-l-autre-inconnue` | 56 | c | **OK** |

---

## Défauts et correctifs exacts

### D1 — 17 Q2 [majeur · indice de forme] — défaut de MON texte

Options actuelles : `a` « x² − 2x + 1 − 9 », `b` « x² + 1 − 9 », `c` « x² + x + 1 − 9 », `d` « x² + 2x + 1 − 9 »
(clé). Chaque distracteur ne change **qu'un** terme de la clé (signe / présence / coefficient du double
produit) : le terme du milieu présent 3 fois sur 4, le signe « + » deux fois contre une, le coefficient 2
deux fois contre une ⇒ le vote reconstruit « + 2x », et la clé est la seule option à un changement de
chacune des trois autres. C'est le cas que la consigne exige de casser par un plan 2×2.

**Correctif** :
- option `b` → `"x² − x + 1 − 9"`, **muette** (retirer `"misconceptionTag": "math.alg.carre-somme-sans-double-produit"`) ;
- explication : remplacer « أو نسيان الجداء المضاعف فنكتب x² + 1 − 9 ؛ أو كتابته دون العامل 2 فنكتب x² + x + 1 − 9. »
  par « أو كتابة الجداء المضاعف دون العامل 2 فنكتب x² + x + 1 − 9 ؛ أو جمع الخطأين فنكتب x² − x + 1 − 9. »
  (phrase finale complète : « الخطأ الشائع: إعطاء الجداء المضاعف الإشارة − فنكتب x² − 2x + 1 − 9 ؛ أو كتابة الجداء المضاعف دون العامل 2 فنكتب x² + x + 1 − 9 ؛ أو جمع الخطأين فنكتب x² − x + 1 − 9. »).

Vérifié : plan 2×2 (signe ± × coefficient 2/1), vote à égalité sur les deux axes, chaque option à un
changement de deux autres ; longueurs 15 · 14 · 14 · 15 (clé à égalité avec `a`) ; aucun distracteur ne se
réduit à A (x² − 2x − 8, x² − x − 8, x² + x − 8) ; étiquettes `a` et `c` inchangées et exactes ; aucune fuite ;
gates vertes et rendu correct en bac à sable. (On perd l'erreur « sans double produit », portée ailleurs
dans le corpus ; un plan 2×2 à 4 options ne peut pas la garder avec les deux autres.)

### D2 — 13 Q1 [majeur · rendu de l'énoncé] — préexistant, manqué au 1er audit

La seconde ligne de l'énoncé, « (3/21)³ », est un seul jeton sans relation : `isDisplayEquation` la refuse
(`isMathPhrase` veut une relation ou ≥ 2 jetons avec opérateur) et, sans lettre arabe, `splitMathRuns` passe
par `splitLtrProse`, qui la laisse en prose ⇒ dans la carte RTL l'algorithme bidi la rend **« ³(3/21) »**
(exposant à gauche, à la place de l'indice d'une racine cubique). Mesuré et capturé en Chromium avec le
`bidi.ts` d'`origin/main` (ce46894c). Mon harnais du 1er audit écartait les chaînes sans lettre (« arithmétique
chiffres seuls ») : c'est ainsi qu'il l'a manqué.

**Correctif** : énoncé → `"ما قيمة العدد A التالي ؟\nA = (3/21)³"` (options, clé, explication inchangées).
Vérifié : la ligne « A = (3/21)³ » est une ligne-équation (`isDisplayEquation` vrai) ⇒ bloc LTR centré, rendu
« A = (3/21)³ » (capture) ; gates vertes.

### D3 — 19 Q3 [mineur · consigne] — conséquence de MON correctif de la ligne de données

Dernière ligne actuelle : « ما المساواة التي نحصل عليها بتعويض هذه الأطوال ؟ ». Depuis que la ligne donne
AD = 4 ، DC = 6 ، EB = 2, « ces longueurs » ne se substituent plus telles quelles : DC n'apparaît pas dans
EB/EA = FB/AD et EA doit être calculée. Lue à la lettre, la consigne pousse à loger 6 à la place de EA, soit
`b` « 2/6 = FB/4 » (et `c`) — les seules options faites des trois nombres donnés — alors que la clé emploie
4 deux fois et pas 6. Pas de double réponse (EA ≠ DC), mais une consigne inexacte qui oriente vers un
distracteur.

**Correctif** : remplacer cette ligne par « ما المساواة التي نحصل عليها بعد تعويض كلّ طول في هذه المساواة بقيمته ؟ ».
Vérifié : neutre (n'annonce aucune valeur), aucune fuite, aucune paire proche créée (tranche), rendu correct.

### D4 — 17 Q4, Q6, Q7 [mineur · figure, recommandé]

La figure est tracée à l'échelle de **x = 2** : AB = BC = 56 px (étiquettes « x » et « 2 »), AE = EF = 112 px
(« 4 » et « x + 2 ») — toute figure à l'échelle des étiquettes l'est forcément. Lu sur la figure, x = 2 se
teste dans les options : en **Q6** seule la clé est vraie en x = 2 (ce qui est nécessaire à sa justesse), en
**Q4** seule x/4 = 2/(x + 2) l'est (0,5 = 0,5 ; 1/3 ≠ 0,5 ; 0,5 ≠ 2 ; 1/3 ≠ 2), et en Q7 x se lit sans résoudre.
Je l'avais jugé tolérable au 1er audit pour la seule question finale ; ma Q6 (figure ajoutée) en fait un
raccourci dans une deuxième question, et je n'avais pas vu qu'il valait déjà pour Q4.

**Correctif** (dans les trois copies de la figure, Q4, Q6, Q7) :
- `d="M170 202 L58 202"` → `d="M170 202 L86 202"` ; `d="M226 34 L58 202"` → `d="M226 34 L86 202"` ;
- `<circle cx="58" cy="202" r="4.4"/>` → `<circle cx="86" cy="202" r="4.4"/>` ;
  `<circle cx="170" cy="90" r="4.6"/>` → `<circle cx="170" cy="101.2" r="4.6"/>` ;
- texte « A » : `y="93"` → `y="104"` ; texte « F » : `x="45"` → `x="73"` ; texte « x » : `y="67"` → `y="73"` ;
  texte « 4 » : `y="151"` → `y="157"` ; texte « x + 2 » : `x="114"` → `x="128"` ;
- Q7 seulement, triangle grisé : `d="M170 90 L170 202 L58 202 Z"` → `d="M170 101.2 L170 202 L86 202 Z"` ;
- dans les trois énoncés : « في الشكل التالي المستقيم (BE) » → « في الشكل التالي ، وهو غير مرسوم بمقياس الرسم ، المستقيم (BE) ».

Vérifié : C(226 ; 34), A(170 ; 101,2), F(86 ; 202) alignés (pentes −6/5 et −6/5), (BC) ∥ (EF), angles droits
inchangés, Thalès vrai dans le dessin (AB/AE = BC/EF = 2/3), rien hors du `viewBox` (rendu Chromium) ; les
lectures visuelles se contredisent (AB ≈ 1,2 × BC ⇒ x ≈ 2,4 ; EF < AE ⇒ x < 2) et aucune valeur lue (1 ; 2,4 ;
3 ; 4) ne rend vraie une seule option de Q4 ou de Q6 ; gates vertes, aucune paire proche créée par l'ajout
commun aux trois énoncés. (Mention « غير مرسوم بمقياس الرسم » déjà employée par la mission 20.)

---

## Étiquettes

- **Registre** (`origin/main` 4f72f94b) : les 36 identifiants posés dans les fichiers existent ; toutes les
  compétences existent ; aucune clé étiquetée ; 88 étiquettes sur 141 distracteurs. Les 8 options « en
  attente » : textes identiques au fichier, muettes, jamais la clé, toutes dans des QCM.
- **Les 3 nouvelles** (absentes d'`origin/main`, compétences existantes, une phrase d'élève fr/en/ar chacune,
  aucun vocabulaire vectoriel ; `math.vec.*` n'est qu'un préfixe historique) :
  - `math.geo.droite-des-milieux-mauvais-cote` — lot : 13 Q4 `a`, `b` ; 15 Q3 `b`, `d` ; publié relu :
    18/07 Q5 `a` « 2,5 » (= AB/2, AB porte E : exact). **18/12 Q2 `e` « IL = AD/2 » exécute bien l'erreur mais
    c'est une question `multi`** : son schéma d'option (`wireOptionSchema`) n'a pas de `misconceptionTag` et
    `sql-builder` n'émet `distractor_tags` que pour les QCM — une étiquette posée là passe `content:check`
    (clé inconnue silencieusement retirée, essayé en bac à sable) et **disparaît à l'émission**. Ne pas l'y
    poser. Décompte réel : **3 questions** (13 Q4, 15 Q3, 18/07 Q5) — seuil atteint, juste. 18/12 Q2 `d` :
    non étiquetable, d'accord (AB n'est pas un côté de ADC).
  - `math.vec.milieu-difference-au-lieu-de-somme` — 16 Q2 `a` + 09/09 Q8 `d` (−√2 ; 1), 12/07 Q5 `b` (2 ; −2),
    18/07 Q2 `c` (4 ; 2), 18/08 Q1 `c` (2,5 ; 0), 18/11 Q1 `a` (2 ; −1) et `c` (4 ; −2) (différence entière),
    18/17 Q2 `c` I(0 ; −4) J(3 ; −4) : **toutes exactes, 7 questions**.
  - `math.geo.position-relative-ignoree` — 16 Q6 `a`, 18 Q3 `a` + 08/11 Q4 `c` « 9 cm » (O mis hors de [BN]),
    09/09 Q6 `c` « 5 » (H mis hors de [BO]) : **toutes exactes, 4 questions**.
- `math.alg.produit-nul-une-seule-solution` (déjà sur `origin/main`) sur 17 Q5 `c` : exact.
- Libellés élargis confirmés sur `origin/main` : `operation-inverse-appliquee` (« … une division au lieu d'une
  multiplication (ou l'inverse) »), `racine-distribuee-sur-somme`, `produit-signes-negatifs`.
- Note des étiquettes en attente, sans conséquence : elle range 13 Q3 `d` sous « soustraction au lieu
  d'addition » alors que 60 est une addition au lieu d'une soustraction — le libellé couvre les deux sens.

## Contrôles sur toute la tranche (47 questions)

- **Aveugle** : 47/47 clés retrouvées avant lecture ; questions modifiées refaites par deux méthodes.
- **Explications** : toutes les égalités des questions modifiées recalculées justes ; chaque mécanisme
  d'erreur produit bien la valeur de son option.
- **Forme** (script + lecture) : aucune clé strictement la plus longue (tranche : 0 dans 13–20) ; aucune
  option somme ou différence de deux autres ; plans 2×2 réels : 14 Q1, Q2, Q4 ; 16 Q4 ; 17 Q4, Q6 ; 18 Q1, Q3,
  Q4, Q6, Q7, Q8 ; 19 Q2, Q6, Q7, Q8 ; 20 Q3 — **sauf 17 Q2 (D1)** ; aucune option ne nie une prémisse, une
  plage ou la figure ; énoncés au pluriel : 16 Q1 corrigé ; positions de clé a 12 · b 11 · c 12 · d 12.
- **Fuites** : aucune fuite en avant par une explication (ordre d'émission = ordre du fichier, rampes non
  décroissantes partout) ; plus aucune fuite **É**. Restent les fuites **S** déjà tolérées (données que le sujet
  énonce et dont l'étape suivante a besoin) : 18 Q2 ← Q1, Q3 et Q5 ← Q2 (E(0 ; a²)), Q7 et Q8 ← Q5, Q8 ← Q6 ;
  19 Q6 ← Q4 (FB = 2), Q7 et Q8 ← Q6 (200 m²) ; 20 Q4 et Q5 ← Q1 (2700), Q5 et Q6 ← Q3. 17 n'en a plus aucune.
  (19 Q5 : « 200 » dans l'explication est la valeur d'un distracteur de EB, coïncidence avec l'aire.)
- **Autonomie** : chaque énoncé modifié se lit seul ; aucune technique hors cours (ordre du manifeste 9ᵉ :
  02, 16, 03, 04, 07, 12 avant 08 ; échelle et pourcentages : acquis antérieurs ; gloses présentes).
- **R-3** : ni vecteur ni translation (« شعاع » n'apparaît qu'en 20, « الشعاع الضوئي » : rayon lumineux).
- **Doublons** : aucune mission publiée ne reprend 2010 tech ex1, 2011 tech ex3, 2017 tech ex1, 2003 ex3,
  2010 gén ex3, 2016 gén ex2, 2013 tech ex2 ni 2025 tech ex3 (recherche par titres de session et par données
  sur tous les exercices et quiz de maths d'`origin/main`) ; les exercices en cours d'autres lots dans
  l'arbre (09/30, 12/10, 12/12, 18/25, 18/26) sont d'autres exercices des mêmes sessions.
- **Gates** (bac à sable `origin/main` + 8 fichiers du lot, puis avec D1–D4 appliqués) : `content:check`
  vert ; `content:qa --subject math` 0 erreur, aucun avertissement sur 08 ; `content:tranche --chapters 08` :
  0 clé la plus longue dans 13–20, 38 paires proches **dont aucune avec 13–20** (liste complète), 0 gabarit ;
  `content:figures:check` vert. `content:overflow:check` n'a pas pu tourner (Chromium headless 1234 absent du
  conteneur) : débordements des SVG neufs vérifiés à la main et en capture.
- **Rendu arabe** (Chromium, `bidi.ts` ce46894c, 290 chaînes) : hors conception, seul D2. Le reste : chaînes
  chiffres seuls lues de droite à gauche, nombre + unité, ponctuation de bord — par conception.

## Ce que l'auteur ne pouvait pas savoir

1. **Lacune du moteur** (arena `bidi.ts`) : une ligne faite d'un seul jeton-puissance n'est ni ligne-équation
   ni isolée et se rend renversée dans une carte RTL. Outre 13 Q1, **5 énoncés publiés** sont touchés :
   `03/16-examen-2023-technique` Q3 « (0,001)⁻⁴ » (rendu « ⁴⁻(0,001) »), `03/24-examen-2023-technique` Q3
   « (2√2)² », `16/10-devoir-portee-de-l-exposant` Q1 « 4(√3)⁴ » (rendu « ⁴(3√)4 »), Q2 « (4√3)² », Q3
   « (4√3)⁻² ». Correctif côté moteur suggéré : accepter comme ligne-équation (ou isoler) un jeton unique qui
   porte un exposant ou un radical. En attendant, côté contenu : « A = … ».
2. **18/12 Q2 `e`** est une question `multi` : une étiquette y serait retirée sans erreur (cf. § Étiquettes).
3. **Arbre partagé en retard** : `content/math/08-thales/cours.md` y garde, ligne 310, l'ancien énoncé de la
   propriété du papillon (« مع A و B على مستقيم و C و D على الآخر », faux) que `origin/main` a corrigé (#590,
   « A و C … B و D ») ; ne pas committer ce fichier avec le lot (le `chapter.json` ne diffère d'`origin/main`
   que par la ligne `sources[]`, conforme).
4. D1, D3 et D4 viennent de mes propres textes ou correctifs du 1er audit ; D2 était présent et mon 1er audit
   l'a manqué. Les deux reprises déjà faites par l'auteur sur mes textes (17 Q6, 19 Q8) sont justes.

## Chiffre final

- **Questions re-résolues : 47/47** (8 missions) ; **clés fausses : 0** ; **questions modifiées vérifiées : 33**
  (+ 17 Q4 déplacée, + en-têtes de 19 et 20, + 8 options en attente sur 13 Q4, 15 Q3, 16 Q2, 16 Q6, 17 Q5, 18 Q3).
- **Défauts : 0 critique · 2 majeurs (D1 17 Q2, D2 13 Q1) · 2 mineurs (D3 19 Q3, D4 17 Q4/Q6/Q7).**
- Questions à reprendre : **6** (13 Q1 ; 17 Q2, Q4, Q6, Q7 ; 19 Q3) — dont 4 pour le mineur recommandé D4.
- Verdict : **à corriger avant livraison** ; après D1–D4 (textes exacts ci-dessus, validés en bac à sable),
  **livrable**.

---

## Annexe — journal de progression (écrit au fil de l'eau)

**Étape 1 — re-résolution à l'aveugle (énoncés + options seuls), faite pour les 47 questions avant
toute lecture de clé.** Mes réponses : 13 : 1/343 · 7 · 40 · IJ = AC/2 — 14 : c (points + parallèle +
Thalès direct) · 1,5/6 = 2/AC · 8 · 80 — 15 : √3 · C milieu de [AB] · 3 · 200 — 16 : B seule · (0 ; 0) ·
(0 ; 3) · CO/CB · 6 · (4 ; 3) — 17 : 0 · x² + 2x + 1 − 9 · (x − 2)(x + 4) · x/4 = 2/(x + 2) · {−4 ; 2} ·
x² + 2x = 8 · 8 — 18 : OA/OI = OE/OB · a² · a² + 1 · OK/OA = OJ/OM · a/(a² + 1) · x² − (5/2)x + 1 ·
2a² − 5a + 2 = 0 · « a = 2 ، إذن OA = 2 × OI … منتصف » — 19 : 4 · a (⊥ commune) · 2/4 = FB/4 · 2 · 20 ·
200 · 200 × p ≥ 18000 · 90 — 20 : 2700 · parallèles (⊥ commune) · MA/MH = AB/PH · 9/10 · 54 · 56.
**Clés lues ensuite : 47/47 concordent.** Questions modifiées recalculées par deux méthodes : 16 Q5
(coordonnées : (CA) y = 3x − 9, y = 3 ⇒ M(4 ; 3), BM = 6 ; Thalès : O milieu de [BC], 3/BM = 1/2) ;
16 Q6 (idem + contrôle « A milieu de [CM] ») ; 18 Q5 (Thalès OK/a = 1/(a² + 1) ; coordonnées : droite
par J(0 ; 1) de direction (−a ; a² + 1) coupe y = 0 en x = a/(a² + 1)) ; 18 Q8 (sympy : racines 1/2 et 2 ;
contrôle 2/(4 + 1) = 2/5) ; 14 Q4 (AC = 2 × 6 ÷ 1,5 = 8 cm ; 8 × 1000 cm = 80 m ; contrôle 0,25 = 0,25) ;
17 Q6 (x(x + 2) = 8 ; en x = 2 : 8 = 8) ; 17 Q7 (x = 2, EF = 4, aire 8 ; BEF 12, ABC 2) ; 19 Q6 (20 m × 20 m ÷ 2 ;
contrôle 2 cm² × 100 m²/cm²) ; 19 Q8 (18000 ÷ 200 = 90 ; 200 × 90 = 18000).

**Étape 2 — diff question par question contre `l10-backup-audited/`** (script mot à mot : énoncé hors
SVG, SVG, options + étiquettes, clé, explication, étage, compétences). Rien d'autre n'a changé que les
points listés par l'orchestrateur, plus : 13 Q2 et Q3 options **réordonnées** (25 · 12,5 · 7 · 5 et
30 · 40 · 47,5 · 60), 19 Q7 **reformulée** (« يبيع صاحب الأرض الجزء BEF … فما الشرط الذي يجب أن يحقّقه p ؟ »),
16 Q6 reformulée (« في المستوي المنسوب إلى معلّم متعامد ومتجانس … A = (3 ; 0) … ») — « معلّم » est le terme du
cours `12-repere-plan` (14 occurrences) ✓ — et 17 Q6 : figure de Q4 avec un `<title>` allongé
(« والمثلثان BAC و EAF متقابلان بالرأس A ») ; 18 Q5 : même SVG que Q4 (chaîne identique).

**Étape 3 — constats** : D1 (17 Q2, vote), D3 (19 Q3, consigne), D4 (17, figure à l'échelle de x = 2) ;
le reste OK.

**Étape 4 — contrôles transverses** : syscheck (rampes, ordre d'émission, clé la plus longue,
somme/différence, fuites) ; registre `origin/main` ; options en attente ; occurrences publiées des 3
nouvelles étiquettes relues ; gates en bac à sable ; doublons ; rendu bidi ⇒ D2 (13 Q1). Correctifs D1–D4
appliqués dans le bac à sable seulement : gates vertes, rendu vérifié en capture.
