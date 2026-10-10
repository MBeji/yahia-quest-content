# Re-vérification ciblée — tranche L20 (maths 9ᵉ, ch. 03, missions 27 à 31) après le tour de corrections

Auditeur indépendant (même consigne que `audit-L20.md`). Fichiers relus dans l'arbre de travail tels quels ; questions
touchées re-résolues à l'aveugle AVANT lecture de la clé ; rien n'est modifié dans le dépôt. Priorité : les défauts
INTRODUITS par les correctifs (ceux de l'audit comme ceux de l'auteur).

_Re-vérification complète : fichiers 27 à 31, étiquettes, gates, chiffre final._

## Méthode

- Diff structurel aveugle (énoncés, options, type, difficulté — sans clé, explication ni étiquette) entre la version
  auditée et l'arbre de travail : questions touchées = 27 Q2, Q4 ; 28 Q2 (ex-Q4, énoncé épuré) ; 29 Q1, Q5 ; 30 Q4 ;
  31 Q2, Q4 (ex-Q5) ; explications modifiées en plus : 27 Q3, 29 Q4, Q7, 31 Q1, Q3. Ces huit questions re-résolues à
  l'aveugle, puis comparées aux clés ; valeurs recalculées par sympy.
- Rendu : `bidi.ts` du moteur à jour (arena `origin/main` 68529ff5, avec #1160 : formule ouverte par un nombre puis π
  ou une lettre grecque, ou « ° », désormais isolée) ; contrôle Chromium `dir=rtl` de toutes les lignes des cinq fichiers.
- Gates en lecture seule, sur une copie de travail (corpus `origin/main` 67cf20e4 + les cinq fichiers, moteur 68529ff5) :
  `content:check`, `content:qa --strict`, `content:tranche --changed`, Jaccard de surface et longueurs.
- Registre des étiquettes : inchangé sur `origin/main` depuis l'audit (67cf20e4 ne touche que `FableEtudes/`) ; la
  nouvelle étiquette n'y est pas encore, et aucun des cinq fichiers ne la porte (placement prévu à la livraison).

## Fichier 27 (4 questions, practice d2, rampe 2,2,2,2)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q2 (option a « 2¹⁶ », explication) | 2¹² | b | OK · réserve mineure |
| Q3 (explication) | — (clé inchangée a) | a | OK |
| Q4 (option a « 2030 », explication) | 1508 | c | OK · cosmétique |

- **Q2.** 2¹⁶ = 4⁸ = 65 536 ≠ 4096 (sympy) : faux, chemin « 4^(2³) puis base 2 » juste dans l'explication. Mon option
  « 4⁸ » aurait rendu la clé strictement la plus longue (2 caractères contre 3) : **défaut de mon correctif**, bien vu
  par l'auteur. Longueurs 3/3/2/2 : la clé n'est plus la plus longue au sens strict. Réserve résiduelle : la base 2
  revient dans trois options sur quatre (le vote sur la base n'écarte que 4⁵ : une chance sur 3), et 2¹⁶ et 2¹² sont
  les deux plus longues (une chance sur 2 pour qui choisit la plus longue). Je n'ai pas d'option de remplacement qui
  soit naturelle sans recréer l'un des deux indices (4¹² répète l'exposant 12 ; 4⁸ allonge la clé ; 2¹⁰ = 4⁵ ferait
  deux options égales) : **à garder en l'état**, mineur non bloquant.
- **Q3.** Texte de l'audit appliqué tel quel ; relu : « فالفرق a − b = 3,14 − π سالب، أي a < b ✓ » et « أي حساب π − 3,14
  مكان a − b = 3,14 − π » sont justes ; le run « a − b = 3,14 − π » s'ouvre sur une lettre et s'affiche gauche-à-droite
  (contrôle Chromium : aucune unité mal ordonnée). Coche ✓ après la clé. OK.
- **Q4.** 2030 = 1450 × 1,4 (4 % lu 40 %), faux ; écarts à 1450 : 580, 4, 58, 400, aucun n'est une option ; aucune option
  n'est somme ou différence de deux autres ; clé non la plus longue (4 chiffres partout) ; la plus proche de la clé
  reste 1454 ; phrase d'explication juste. Cosmétique : les options numériques ne sont plus rangées (2030 en tête) ;
  l'affichage les mélange, mais pour l'ordre du fichier : 1454, 1508, 1850, 2030 (identifiants inchangés).

## Fichier 28 (6 questions, boss d3, rampe 2,2,3,3,3,3)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q2 (ex-Q4, énoncé épuré) | 2 − √3 | a | OK |
| suppressions (ex-Q1 (1 + √3)², ex-Q3 √12 + √27) | — | — | OK |

- Fidélité à 2020 technique ex. 2 : Q1 = item 1 (a = 2 + √3), Q2 = item 2 (b = 2 − √3), Q3 = item 3a (ab = 1, numeric,
  depuis les définitions brutes), Q4 = item 3b (signe de b), Q6 = item 4 (somme = 4), Q5 = la seule marche (1/a + 1/b = a + b).
  Tous les items officiels sont là, sans marche superflue : fidèle, et plus près de l'officiel qu'avant. Le
  développement de (1 + √3)² reste enseigné dans l'explication de Q1. Le titre (« نشر مربّع مجموع، واختزال جذور… ») reste
  exact.
- Chaque question se lit seule : Q1 définit a, Q2 définit b, Q3 redonne a et b bruts, Q4-Q5 posent a, b génériques et
  ab = 1, Q6 donne les deux fractions. Aucune explication ne renvoie à une question supprimée.
- Ma réécriture de rechange de l'ancienne Q3 gardait le calcul de la vérification du cours ch. 02 : **défaut de mon
  correctif** ; la suppression est la bonne décision.
- En-tête boss d3 : Q3, Q5, Q6 sont de vrais d3 (Q4 limite) sur 6 questions : honnête.

## Fichier 29 (7 questions, PASSÉ en practice d2 75/15, titre ⭐⭐, rampe 2,2,2,2,2,2,3)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (option c « 4 − 2√3 − 2√3 + 3 = 7 − 4√3 », explication) | d (… − 3 = 1) | d | OK |
| Q4 (« 0 » muette, 2ᵉ chemin) | 8√3 | d | OK |
| Q5 (énoncé sans la lettre A) | 192 | c | OK |
| Q7 (« 1 + √3 » muette, 2ᵉ chemin) | 0 | b | OK |
| en-tête practice d2 | — | — | OK |

- **Q1.** Vote terme à terme : 3ᵉ terme +2√3 (a, b, d) contre −2√3 (c), 4ᵉ terme +3 (a, c) majoritaire → le vote
  reconstruit a, un distracteur : le défaut est levé. c = 7 − 4√3 ≠ 1 ; la chaîne interne de c est cohérente (4 + 3 = 7) ;
  clé non la plus longue (21 caractères contre 27 pour b et c). Explication juste (« الخطأ في إشارتين معًا… »).
- **Q4, Q7.** Les deux chemins ajoutés sont justes : a − b = 2 + √3 − 2 − √3 = 0 donc A = 4 × 0 = 0 ; a − 1 = 1 + √3 et
  ab + a − 2 = 1 + √3 (sympy). Options muettes, comme le veut la règle « deux erreurs, une option ».
- **Q5.** « نريد كتابة العدد 8√3 تحت جذر تربيعي واحد… » : plus de lien littéral avec le A de Q4 ; la tâche reste la seconde
  moitié de l'item 2 officiel (A = √192). OK.
- **En-tête.** Practice d2 avec une seule question d3 en fin de mission : conforme à l'usage publié (03/15, 03/24, 03/26,
  practice d2 terminées par une d3). Honnête.

## Fichier 30 (5 questions, boss d3, rampe 2,2,3,3,3)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q4 (multi refait) | {b, d} | {b, d} | clé juste · **défaut introduit (énoncé)** |

Jugement des cinq arguments avant lecture de la clé : a — invalide (« الفرق بين عددين موجبين موجب دائمًا » est faux :
2 − √5 < 0) ; b — valide ((2 − √3)² = 7 − 4√3, et 2 − √3 ≠ 0, donc un carré strictement positif) ; c — invalide et
conclusion fausse (4√3 ≈ 6,93) ; d — valide (carrés de deux positifs, 49 > 48) ; e — invalide (7 − 4√10 ≈ −5,65 < 0
avec 7 > 4). Deux justes = clé. Longueurs a 71, b 75, c 76, d 70, e 77 : plus d'indice de longueur. Explication juste de
bout en bout (contre-exemples 2 − √5 et 7 − 4√10 vérifiés). Rendu Chromium : aucune unité mal ordonnée.

- **[MAJEUR — introduit par la réécriture] L'énoncé annonce la conclusion.** « نريد إثبات أنّ العدد b موجب » dit à l'élève
  que b est positif : l'argument c, qui conclut « b سالب », nie cette prémisse et s'élimine à vue sans qu'on juge son
  erreur (4√3 = 12). L'ancien énoncé était neutre (« نريد تحديد إشارة العدد b »), comme l'officiel (« استنتج علامة b »).
  Correctif (une ligne ; segmentation et rendu Chromium vérifiés ; aucun argument ne change de statut ; explication
  inchangée, elle conclut déjà « إذن b موجب ✓ ») : remplacer « نريد إثبات أنّ العدد b موجب. اختر كلّ الاستدلالات الصحيحة. »
  par « نريد تحديد إشارة العدد b. اختر كلّ الاستدلالات الصحيحة. »
- **[NOTE de fidélité]** L'officiel enchaîne 2a « أحسب ab » → 2b « استنتج علامة b » : il attend la déduction par ab = 1.
  Q4 ne la propose plus (elle reste en 28 Q6, session 2020). La sous-question (signe de b) est gardée, la voie
  officielle non ; arbitrage acceptable pour défaire le gabarit répété avec 28 Q6, à dire au rapport de livraison.
  Effet de bord heureux : l'ancien énoncé (a, b et ab = 1 donnés) livrait la clé de Q5 (x = 1/a = b), ce n'est plus le cas.
- Prémisse b = 7 − 4√3 (résultat « بيّن أنّ » 1b) et l'identité de l'argument b (= clé de Q2) : convention des prémisses,
  Q2 précède Q4 dans l'ordre d'émission. Pas de défaut.

## Fichier 31 (4 questions, practice d2, rampe 1,2,2,2)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (a muette, c étiquetée, explication) | x = 3 − 2/3 | b | OK |
| Q2 (énoncé, c muette, explication) | 7/3 | d | OK |
| Q3 (explication de « 7,5 غ ») | — (clé inchangée c) | c | OK |
| Q4 (ex-Q5, d2, explication) | 30 − 10√5 | b | OK |
| suppression de l'ex-Q4 (développement) | — | — | OK |

- Fidélité à 2024 technique ex. 1 : Q1 + Q2 = item 1, Q3 = item 2, Q4 = item 3 (la valeur, comme l'officiel), item 4
  (patron) écarté à raison. Plus de doublon interne ; le titre (« … ونشر مربّع فرق ») reste exact.
- **Q1.** Chemins de l'explication justes : −x = 2/3 − 3 puis oubli de ÷(−1) → x = 2/3 − 3 (a, muette) ; 3 passé sans
  changer de signe → −x = 2/3 + 3 → x = −3 − 2/3 (d) ; 2/3 passé à gauche sans changer de signe → 3 + 2/3 = x (c). Le
  libellé de `transposition-sans-changer-signe` nomme exactement l'erreur de c et de d. Plan 2×2 intact.
- **Q2.** Équation posée seule ; 2×2 signe × grandeur intact ; chemins de « −7/3 » et « −1/3 » justes (2/3 − 3/3 = −1/3).
- **Q3.** Phrase ajoutée juste (0,75 × 12 = 9).
- **Q4.** d2 cohérent avec les autres carrés de la tranche ; 2×2 parfait ; « 20 = 25 − 5 » décrit comme la confusion
  carré de la différence / différence des carrés : prêt pour la nouvelle étiquette.
- Paire la plus proche : Q2 ↔ 12/20 Q6 (Jaccard 0,43 < 0,45), même tournure officielle « إذا كان x عددًا حقيقيًّا يحقّق »,
  autre équation (3 − 2x = x − 3) et autres options : pas un doublon.

## Étiquettes

- Retraits vérifiés : 27 Q4 (l'option « 58 » a disparu), 29 Q4 a, 29 Q7 d, 31 Q1 a, 31 Q2 c. Posée : 31 Q1 c. Aucune
  étiquette hors registre ; la clé n'est jamais étiquetée. Décompte relu : 75 distracteurs, 55 étiquetés, 20 muets (dont
  les 3 faux du multi) — 57/18 après la livraison.
- Nouvelle étiquette `math.alg.carre-difference-ecrit-difference-carres`, libellé exact pour chacun des quatre placements :
  30 Q2 b (2² − (√3)² = 1), 31 Q4 d (5² − (√5)² = 20), 03/22 Q1 c ((x − √2/2)² pris pour x² − 1/2 → (5 + 2√10)/4,
  recalculé) et 09/24 Q5 b (a² − b² = 12√2, que son explication décrit comme « الخلط بين مربّع الفرق وفرق المربّعين »).
  Ordre de livraison : ajouter l'entrée au registre DANS LE MÊME commit que les quatre placements (`content:qa` refuse
  une étiquette non déclarée).

## Gates (lecture seule)

`content:check` : vert (120 matières, 28 315 questions, soit 29 → 26 dans la tranche). `content:qa --strict` : 0 erreur,
aucun avertissement sur 27-31. `content:tranche --changed` : clé strictement la plus longue 0/24 (mcq de la tranche),
aucune paire ≥ 0,45 touchant la tranche, aucun candidat gabarit. Jaccard max 0,43 contre le publié, 0,36 en interne.

## Chiffre final

26 questions relues (dont 8 re-résolues à l'aveugle et 5 explications revérifiées) ; **0 clé fausse** ; 0 critique ;
**1 majeur introduit** (30 Q4 : énoncé qui annonce la conclusion — une ligne à remplacer) ; mineurs : 27 Q2 (vote sur
la base, à garder), note de fidélité 30 Q4 ; 1 cosmétique (ordre des options de 27 Q4). Deux de mes correctifs du
premier audit étaient défectueux (27 Q2 « 4⁸ » rendait la clé la plus longue ; la réécriture de rechange de 28 Q3
gardait le doublon du cours) ; l'auteur les a corrigés à juste titre. Questions à reprendre : **30 Q4 (énoncé)**, et au
choix l'ordre des options de 27 Q4. Verdict : livrable après le correctif de 30 Q4.
