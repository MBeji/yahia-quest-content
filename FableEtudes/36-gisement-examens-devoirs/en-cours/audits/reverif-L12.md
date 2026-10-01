# Re-vérification ciblée — lot L12 (ch.09, missions 23–29) — auditeur indépendant

État : **terminé**.
- Verdict : **NO-GO en l'état**, GO après les éditions E1 à E3 (§ 6).
- Données relues sur origin/main : moteur 779d982 (bidi #1137, #1138, #1139 compris) ; corpus fa035eef.

## 1. Re-résolution à l'aveugle des questions modifiées
26 questions ont un énoncé, des options ou une figure modifiés (23 Q4, Q6, Q7 · 24 Q4, Q6 · 25 Q2, Q4, Q8 · 26 Q2, Q3, Q4 · 27 Q2, Q4 · 28 Q2 à Q8 · 29 Q1, Q2, Q3, Q4, Q5 (figure), Q7). Chacune re-résolue sur son texte actuel, sans clé, étiquette ni explication, chaque option évaluée : **0 divergence** (26/26). Aucun identifiant de clé n'a changé, en-têtes, nombres de questions et difficultés inchangés.

## 2. Correctifs demandés : appliqués ?
Contrôle par script, texte exact de l'audit contre le fichier : 53 points vérifiés, 53 présents mot pour mot.

| Défaut | État | Reste |
|---|---|---|
| M1 (23 double le devoir 14) | arbitré : 23 gardé, devoir 14 repris à part | — (condition pour N1, § 5) |
| M2 23 Q4, 28 Q3, 28 Q2 | corrigé | — |
| M3 (11 questions) | corrigé | — (voir § 3 : 27 Q4, 29 Q7, mineurs) |
| M4 25 Q2 | corrigé | — |
| M4 29 Q1 | corrigé | — |
| **M4 26 Q4** | **non corrigé** : c'est mon correctif qui est fautif | [b] « OA = OB = OC ، فـ O متساوية البعد عن الرؤوس ، إذن ABC قائم في B » et [d] « OA = OB ، فالمثلّث OAB متقايس الضلعين ، إذن المثلّث ABC قائم في B » répondent à une autre question que celle posée (« … قائم في A ؟ ») : on les écarte à vue, et le rappel désigne encore [a] contre [c]. Voir § 3, défaut 1. |
| M5 titres 28 et 29 | corrigé | — |
| M6 25 Q8 | corrigé | — |
| M7 29 Q3 | corrigé | — |
| M8 (tous les points) | corrigé ; rendu confirmé sur le moteur de main (§ 4) | — |
| m2 (24 Q4, 24 Q6, 28 Q8) | corrigé | — |
| m3 titre 24 | corrigé | — |
| m4 24 Q6 [a] | appliqué comme je l'avais écrit, mais ma formulation est fautive | « نُخرج 4 من الجذر دون أخذ جذره » : l'option dit elle-même qu'elle oublie un geste. Voir § 3, défaut 2. |
| m6 27 Q7 [a] muette | corrigé | — |
| m7 24 Q7 [b], 29 Q4 [a] | corrigé | — |
| m8 24 Q8 | corrigé | — |
| m9 29 Q5 trait | corrigé | trait posé en x = 100, sur [MC] (45,3 → 215), à 27 px du chevron (127–133) ; la figure reste juste (A, B, C, M, D recalculés) |
| m1, m5, m10, m11, m12 | acceptés ou facultatifs, non repris | — |
| Étiquettes existantes (14 poses, liste « Déjà posées » du fichier d'attente) | posées | jugement au § 5 |

## 3. Défauts nouveaux introduits par les correctifs
Contrôles mécaniques sur les fichiers actuels :
- aucune clé strictement la plus longue ;
- 0 paire proche ;
- aucune option égale à la somme ou à la différence de deux autres (sympy, sur les 9 jeux d'options calculables ; les ensembles et les options rédigées ne s'y prêtent pas) ;
- aucune égalité fausse dans la partie correcte des explications modifiées ;
- chaque énoncé modifié se lit seul ;
- ordre d'émission = ordre du fichier dans les 7 missions, donc aucune fuite vers l'avant ;
- `content:qa` : 0 erreur ; figures justes ; débordement : seule la mission 11 déjà publiée.

1. **MAJEUR — 26 Q4, défaut introduit par mon propre correctif M4** (la leçon de L07).
   - Défaut : [b] et [d] concluent « قائم في B » alors que l'énoncé demande de prouver « قائم في A ». Elles tombent à la lecture, sans aucune mathématique.
   - Conséquence : le plan 2×2 (argument × sommet) est intact en apparence, mais un de ses deux axes est réfuté par l'énoncé. Il reste [a] contre [c], et le rappel (« متساوي البعد عن رؤوسه ») désigne [a].
   - L'option [b] d'origine de l'auteur avait le même défaut.
   - Correctif, vérifié par script (longueurs a 63, b 101, c 65, d 65 : la clé n'est pas la plus longue ; 0 paire proche ; bidi OK) :
     - [b] → « في المثلّث القائم ABC يكون منتصف الوتر O متساوي البعد عن الرؤوس ، أي OA = OB = OC ، إذن ABC قائم في A ». C'est la propriété directe, employée en supposant ce qu'on veut prouver. L'option est muette : retirer `math.geo.hypotenuse-mal-choisie`, aucune étiquette du registre ne nomme ce raisonnement circulaire.
     - [d] → rétablir l'option de l'auteur « (AH) عمودي على (BC) ، فالمثلّث ABC قائم في A لأنّ (AH) ارتفاع فيه » (muette).
     - [c] inchangée.
     - Explication : remplacer la partie après « ✓. » par « الخطأ الشائع: الانطلاق من مثلّث قائم لتطبيق الخاصية المباشرة ، وهذا يفترض ما نريد إثباته ؛ أو الاكتفاء بأنّ OAB متقايس الضلعين ، وهذا لا يقول شيئًا عن الزاوية عند A ؛ أو الاعتماد على أنّ (AH) عمودي على (BC) ، وهو يعطي زاويتين قائمتين عند H لا عند A. »
   - Résultat :
     - les quatre options concluent « قائم في A » ;
     - [a] et [b] partagent « OA = OB = OC » et « متساوي البعد عن الرؤوس », donc le vote ne départage plus [a] de [b] ;
     - [b] reprend davantage de mots du rappel que la clé (« يكون منتصف … متساوي البعد عن الرؤوس ») ;
     - ce qui départage [a] de [b], c'est le sens de la propriété : c'est exactement ce que la question veut tester.
2. **MINEUR — 24 Q6 [a], formulation m4 que j'avais proposée.**
   - Défaut : « نُخرج 4 من الجذر دون أخذ جذره ، √8 = 4√2 ، فـ a − b = 4√2 » annonce son propre oubli (« دون أخذ جذره »). Elle s'écarte donc sans connaître la règle.
   - Correctif : « √8 = √(4 × 2) = 4√2 لأنّ العامل 4 يخرج من الجذر ، فـ a − b = 4√2 » (même étiquette `math.num.facteur-racine-sans-carre`).
   - Longueurs : a 64, b 64, clé 57. Rendu OK. L'explication reste juste.
3. **MINEUR — 27 Q4 [c] « x² − 36 » (M3).**
   - Défaut : l'énoncé laisse x réel non nul quelconque. Or [b] √(x² − 36) n'est pas définie et [c] est négative pour 0 < |x| < 6 : deux distracteurs sur trois se réfutent par le domaine. Avant le correctif, un seul l'était, puisque [c] était « |x| + 6 ».
   - La paire restante, [a] contre [d] (racine oubliée), teste encore la compétence. Acceptable.
   - Correctif facultatif, plan {√, sans √} × {36, 12} (E10) : aucune option n'est réfutable par le domaine. Ce plan perd l'erreur d'hypoténuse.
     - Rejeté : le plan {36, 6}, que j'avais d'abord envisagé, rendait la clé strictement la plus longue (10 signes contre 9, 6 et 7).
4. **MINEUR, acceptable, pas de modification.**
   - 28 Q6 [a] et [c] prennent MB = 5 + a, donc MB > AB. Les écarter demande justement le raisonnement visé (M entre A et B).
   - 29 Q7 : [a] 2(1 + √2)/3 ≈ 1,61 et [c] 2(1 + √2) ≈ 4,83 dépassent 1. Or DA < DC impose DA < 1. L'ancienne [a] « 4 − 2√2 » ≈ 1,17 l'était déjà : il n'y a pas de régression. La paire [b] contre [d] teste le conjugué.
5. **Aucun autre défaut nouveau.**
   - 28 Q2 → Q3 : l'énoncé de Q3 porte la factorisation, mais Q3 est émise après Q2.
   - 29 Q3 → Q4 : l'énoncé de Q4 dit que CMB et ABM sont égales, mais Q4 est émise après Q3. L'explication de Q3 ne dit pas ∠MBC = ∠CMB.
   - En donjon, le tirage est aléatoire : même constat hors tranche que dans le premier audit.

## 4. Rendu avec le moteur de main (arena #1137, #1138, #1139)
Méthode :
- `splitMathRuns` et `isDisplayEquation` de `origin/main:src/shared/lib/bidi.ts` ;
- chaque ligne d'un champ rendue comme `RichField`, chaque option comme `OptionContent` ;
- une option est LTR si `isMathExpression`, sinon RTL (page RTL de la matière) ;
- ordre visuel calculé par bidi-js (UBA et miroirs) ;
- 479 chaînes des missions 23–29, dont 102 modifiées.

Résultats :
- **Tous les points M8 sont bons** :
  - « ∠ » est isolé, entre parenthèses ou seul, en énoncé, en option et en explication ;
  - « يلزم k + 25 = 9 » est bon ;
  - « (5 − a)² = … » est bon ;
  - 27 Q5 : chaque égalité est seule sur sa ligne, en bloc centré LTR ;
  - 26 Q3 ne contient plus « 1/b ».
- Les chiffres suivis d'une lettre (DIGIT_FIRST) et les signes collés à une lettre sont désormais isolés. Aucune chaîne du lot n'en souffre encore.
- **Reste un défaut que #1138 ne couvre pas.**
  - Ce que couvre #1138 : la parenthèse tournée vers l'extérieur (« ) » en attaque, « ( » en queue).
  - Ce qu'il ne couvre pas : quand une formule FERME un membre de phrase arabe entre parenthèses, la « ) » reste dans l'isolat, non inversée. Elle se dessine entre la formule et l'arabe, et le côté gauche n'a plus de parenthèse.
  - Occurrences dans le lot :
    - 24 Q7 explication (champ modifié, texte d'origine) : « … قمّته H (ضلعاه المتقايسان HE و HC) ✓. » → run « HC) ✓ ». Correctif : « … قمّته H ، وضلعاه المتقايسان هما HE و HC ✓. »
    - 25 Q2 explication (champ modifié, texte d'origine), deux fois : « AB = AC (لأنّ ABC متقايس الضلعين قمّته A) و AD = AC (لأنّ D مناظرة C بالنسبة إلى A). » → runs « A) ». Correctif : « AB = AC لأنّ ABC متقايس الضلعين قمّته A ، و AD = AC لأنّ D مناظرة C بالنسبة إلى A. »
    - 24 Q2 explication (champ non modifié) : « (لأنّ a² − b² ≠ 0) » → run « a² − b² ≠ 0) ». Correctif : « وغير معدومين معًا لأنّ a² − b² ≠ 0 ، فالمجموع a + b > 0. »
  - Les trois correctifs ont été rendus par simulation : aucun run déséquilibré, ordre juste.
  - Hors tranche : environ 450 isolats contenant une parenthèse sans sa compagne dans les maths publiées (446 comptés sur origin/main). Pour le moteur, peeler aussi une « ) » de queue et une « ( » d'attaque quand elles sont sans compagne, en comptant « [ ] » avec « ( ) » pour que « [By) » reste entier, et en laissant passer un neutre final comme « ✓ ».
- Facultatif : 29 Q1 explication, « على المستقيم نفسه (AC): (AB) لأنّ … ».
  - Défaut : les deux formules forment un seul run LTR, et « (AC) » se retrouve collé visuellement à « لأنّ ».
  - Correctif : « … على المستقيم نفسه (AC) ، فالمستقيم (AB) عمودي عليه لأنّ المثلّث ABC قائم في A ، والمستقيم (MC) عمودي عليه لأنّ Δ عمودي على (AC) في C. » (rendu vérifié).
- Libellés arabes N1, N2, N3 et élargissements proposés (§ 5) : rendu vérifié, OK.
- Faux positifs écartés :
  - « 5 cm » (rendu natif du corpus) ;
  - « على 4: x² + … » et « بـ E: (3x − 10)… » (ordre de lecture juste) ;
  - « مساحة ABC − مساحة ABE » (se lit juste de droite à gauche).

## 5. Étiquettes
Registre lu sur `origin/main` du corpus (fa035eef) : 642 entrées ; N1, N2 et N3 sont absentes, comme prévu.

**5.1 Poses de ce tour : le libellé nomme-t-il l'erreur exécutée ?**

| Option | Étiquette | Verdict |
|---|---|---|
| 23 Q3 [c] (x − 21)(x + 11) | racine-et-carre-confondus | exacte (b = 16 pris pour √16 = 4) |
| 25 Q7 [b] (x − 33)(x + 39) | racine-et-carre-confondus | exacte (36 pour 6) |
| 24 Q5 [b] 12√2 | difference-carres-confondue | exacte, voir 5.2 |
| 24 Q6 [a] | facteur-racine-sans-carre | exacte : c'est l'exemple du libellé (√8 = 2√2, pas 4√2) ; le défaut de formulation est traité au § 3 |
| 24 Q7 [b], 29 Q4 [a] « متقايس الأضلاع » | classement-triangle-par-cotes-errone | exacte (deux côtés égaux seulement, dit équilatéral) |
| 26 Q3 [a] 2(√3 + 1) | operation-inverse-appliquee | acceptable, à garder : l'élève multiplie par (√3 + 1) au lieu de diviser. La tête du libellé (« l'opération contraire de celle demandée ») le nomme, même si ses exemples ne citent pas × / ÷. Aucune étiquette plus proche ; même lecture que 29 Q7 [c] déjà posée. |
| 27 Q3 [b] x + 2√3 | operation-inverse-appliquee | exacte (somme au lieu de différence) |
| 27 Q3 [d] \|x\| − 2√3 | valeur-absolue-somme-additive | exacte, voir 5.2 |
| 28 Q3 [c] {10/3 ; −10} | produit-nul-racine-signe-non-oppose | exacte |
| 28 Q8 [c] 5/3 | numerateur-denominateur-inverses | exacte (S₂/S₁ lu S₁/S₂ ⇒ (5 − a)² = 4a² ⇒ a = 5/3) |
| 29 Q6 [a] DA(1 + 1/√2) = 2 | numerateur-denominateur-inverses | exacte (DA/DC lu DC/DA) |
| 29 Q6 [b] √2 × DA = 2 | thales-formes-melangees | exacte, voir 5.2 |
| 29 Q1 [d] | intersection-prise-pour-perpendicularite | exacte |
| 26 Q4 [b] | hypotenuse-mal-choisie | à retirer avec le correctif du § 3 : la nouvelle [b] est muette |

Les retraits sont justes : options à deux erreurs de M3, plan des signes de 28 Q2, 27 Q7 [a] (m6).

**5.2 Arbitrages demandés**
- **29 Q6 [b], thales-formes-melangees : exacte.**
  - L'élève écrit DA/AC = 1/√2 : un rapport « partie sur tout » égalé à la valeur donnée d'un rapport « partie sur reste » (DA/DC). C'est le mélange des deux écritures dans une même égalité que nomme le libellé.
  - Même usage que les 23 poses publiées, par exemple 08/11 Q3 [a] et 18/10 Q1 [c].
- **27 Q3 [d], valeur-absolue-somme-additive posée sur une différence : exacte dans la lecture établie du registre.**
  - Sur main, l'étiquette est déjà posée sur une différence au moins trois fois : 03/08 Q1 [d] « |1 − √8| = 1 + √8 », 09/13 Q4 [a] « |1 − √7| = 1 + √7 », 12/07 Q4 [d] « |√3 − 1,73| = √3 + 1,73 ». Leurs explications disent « وزّع القيمة المطلقة على الفرق ».
  - Ici, même geste (distribuer |·| sur x − 2√3), le signe moins gardé. On garde.
  - Élargissement facultatif, par parité avec #604 (racine-distribuee-sur-somme) :
    - FR « Tu distribues la valeur absolue sur une somme ou une différence : |a + b| n'est pas |a| + |b| en général — elle ne se distribue que sur un produit ou un quotient »
    - EN « You spread absolute value over a sum or a difference: |a + b| is not |a| + |b| in general — it distributes only over a product or a quotient »
    - AR « توزّع القيمة المطلقة على مجموع أو فرق: |a + b| ليست |a| + |b| عمومًا، فهي لا توزَّع إلّا على جداء أو خارج قسمة »
- **24 Q5 [b], difference-carres-confondue au sens (a − b)² = a² − b² : exacte.**
  - « Tu confonds une différence de deux carrés avec un carré » nomme la confusion dans les deux sens.
  - Main l'emploie déjà au moins trois fois dans ce sens : 03/01 Q5 [c] « (2x − 1)² → 4x² − 1 », 03/03 Q4 [b] « (3x − 1)² → 9x² − 1 », 04/18 Q3 [a] « (2x − 5)² → 4x² − 25 ».
  - Seule la remédiation vise la factorisation. Ajout facultatif :
    - FR « … ; et (a − b)² vaut a² − 2ab + b², pas a² − b² »
    - EN « …; and (a − b)² is a² − 2ab + b², not a² − b² »
    - AR « … ، و(a − b)² تساوي a² − 2ab + b² لا a² − b² »
- **Parité, 23 Q4 [b] {−1 ; 9} : oui, poser produit-nul-racine-signe-non-oppose.**
  - Même geste que 28 Q3 [c] : la racine d'un seul facteur lue avec son signe visible, l'autre juste. L'explication le dit déjà.
  - Deux distracteurs d'une même question peuvent partager une étiquette : `content:qa` ne l'interdit pas, et main le fait (03/01 Q3 [c] et [d] ; 19/02 Q6 [a], [b] et [d]).
  - Ma « muette » du premier audit était un oubli de parité.
- **23 Q2 [c] et l'élargissement de difference-carres-second-terme-non-eleve-au-carre : recevable.**
  - « Tu retranches le second terme sans l'élever au carré » décrit déjà k = 9 − 5 à la lettre.
  - L'exemple « (x − 5)², le dernier terme vaut 25, pas 5 » la rend exacte. Rendu AR vérifié.
  - Facultatif.
- **produit-nul-applique-a-une-somme (25 Q8 [d]) : ne rien faire tant qu'aucune deuxième question n'en a besoin.** D'accord.

**5.3 Nouvelles étiquettes : décomptes en questions distinctes, publié lu sur origin/main**
- **N1 `math.alg.produit-nul-une-seule-solution`** (compétence math.alg.equations-produit) : **3**.
  - Occurrences : 23 Q8 [a] « DM = 1 فقط » ; 09/10 Q5 [a] « r = 13 » (muette ; l'explication dit « الاكتفاء بأحد العاملين فيبقى حلّ واحد ») ; 09/14 Q4 [b] « موضع واحد: AM = 1 cm » (muette ; l'explication dit « الاكتفاء بحلّ واحد … وإهمال الآخر »).
  - Pas d'autre occurrence trouvée : j'ai parcouru les explications et les options des questions « equations-produit » publiées.
    - Les autres « حلّ واحد » relèvent de |X| = a.
    - 09/14 Q7 [b] « موضع واحد x = 5 » est une autre erreur : le terme + 11 est négligé.
  - **Condition** : la reprise du devoir 14 (M1) doit garder une option « un seul emplacement » portant N1, sinon le compte retombe à 2. Il faut l'écrire dans la consigne de la reprise.
  - Libellés :
    - FR « Tu ne gardes qu'une solution : chaque facteur nul du produit en donne une — écris-les toutes, puis n'écarte que celles que l'énoncé exclut »
    - EN « You keep only one solution: each factor set to zero gives one — write them all down, then discard only those the problem rules out »
    - AR « تحتفظ بحلّ واحد فقط: كلّ عامل منعدم يعطي حلًّا — اكتب الحلول كلّها ثمّ لا تُقصِ إلّا ما تستبعده المعطيات »
- **N2 `math.num.rationalisation-denominateur-oublie`** (math.num.racines-calcul) : **4**.
  - Occurrences : 24 Q11 [c] « 3 + 2√2 » (2/√2 écrit 2√2) ; 26 Q8 [a] « √3 + 1 » ; 02/06 Q4 [b] « 3√7 + 6 » (muette, « نسيان القسمة على 3 ») ; 03/14 Q7 [d] « 6 < 1/a < 7 » (muette, « نسيان القسمة على 2 »).
  - Libellés :
    - FR « Tu multiplies par le conjugué (ou par la racine) sans diviser par le nouveau dénominateur : 1/(√3 − 1) = (√3 + 1)/2, pas √3 + 1 »
    - EN « You multiply by the conjugate (or by the root) without dividing by the new denominator: 1/(√3 − 1) = (√3 + 1)/2, not √3 + 1 »
    - AR « تضرب في المرافق (أو في الجذر) ولا تقسم على المقام الجديد: 1/(√3 − 1) = (√3 + 1)/2 لا √3 + 1 »
- **N3 `math.geo.segment-mal-choisi`**, sans compétence : **4**, toutes dans le lot.
  - Occurrences : 23 Q5 [a] « x² + 9 » (DM au lieu de CM) ; 23 Q6 [d] « 2x² − 20x + 209 » (AB au lieu de AD) ; 24 Q9 [a] « a » (BC pris égal au côté a) ; 25 Q9 [d] « 8 » ([CD] au lieu de la médiane [BA]). 26 Q5 [d] reste muette.
  - Libellés :
    - FR « Tu prends dans la figure un autre segment que celui que demande la propriété : repère d'abord le bon triangle et ses côtés »
    - EN, **à corriger** : « first spot the right triangle » se lit « triangle rectangle » en anglais. Libellé proposé : « You take a different segment from the figure than the one the property asks for: first identify the correct triangle and its sides ».
    - AR « تأخذ من الشكل قطعة غير التي تطلبها الخاصية: حدّد أوّلًا المثلّث المناسب وأضلاعه »
  - **Sans compétence : oui.**
    - Pourquoi : l'erreur est une lecture de figure, transversale (Pythagore en 23 Q5 et Q6, aire en 24 Q9, centre de gravité en 25 Q9). `math.geo.pythagore` enverrait les erreurs de 24 Q9 et de 25 Q9 vers les mauvais exercices.
    - **Mais écrire l'entrée SANS clé `competency`, pas `"competency": null`.** Le schéma dit `competency: competencyIdSchema.optional()` (arena `src/shared/content/schema.ts`) : zod accepte l'absence et refuse `null`, donc le chargement du registre casserait.
    - Précédent : 368 entrées sans cette clé, dont math.alg.reponse-a-l-autre-inconnue.
    - Conséquence pour apply-tags.py : lire `t.get('competency')` et omettre la clé quand elle vaut None.
- Chaque libellé tient en une phrase, dans les trois langues.
- Bilan : 105 poses aujourd'hui. Après les correctifs : − 1 (26 Q4 [b]) + 7 (N1–N3) + 1 (23 Q4 [b]) = **112** poses, 113 avec 23 Q2 [c].

## 6. Verdict : **NO-GO en l'état**, GO dès que E1 à E3 sont appliqués
- Le NO-GO tient à un seul majeur : 26 Q4, que mon correctif M4 a laissé trivial.
- Tout le reste est corrigé mot pour mot, sans divergence de clé.
- Pas de nouvelle manche d'audit nécessaire : chaque texte ci-dessous a été vérifié ici (longueurs, vote, paires proches, prémisses, rendu sur le moteur de main). Chaque ancre est présente une seule fois dans le fichier.
- Relancer seulement `content:gates` après application.

**Bloquant**
- **E1 — 26 Q4** (`26-examen-2020-generale-ex2-radicaux-puissances-demi-cercle-hauteur-thales.json`, 4ᵉ question) :
  - [b] → « في المثلّث القائم ABC يكون منتصف الوتر O متساوي البعد عن الرؤوس ، أي OA = OB = OC ، إذن ABC قائم في A », et retirer `misconceptionTag`.
  - [d] → « (AH) عمودي على (BC) ، فالمثلّث ABC قائم في A لأنّ (AH) ارتفاع فيه » (muette).
  - Explication : remplacer « الخطأ الشائع: تطبيق الخاصية ثمّ نسبة الزاوية القائمة إلى B ، مع أنّها تقابل الوتر [BC] فرأسها A ؛ أو الاكتفاء بأنّ OAB متقايس الضلعين ، وهذا لا يقول شيئًا عن الزاوية عند A ولا عند B. » par « الخطأ الشائع: الانطلاق من مثلّث قائم لتطبيق الخاصية المباشرة ، وهذا يفترض ما نريد إثباته ؛ أو الاكتفاء بأنّ OAB متقايس الضلعين ، وهذا لا يقول شيئًا عن الزاوية عند A ؛ أو الاعتماد على أنّ (AH) عمودي على (BC) ، وهو يعطي زاويتين قائمتين عند H لا عند A. »
- **E2 — registre**, pour N3 :
  - entrée écrite **sans** clé `competency` (pas `null`, que zod refuse) ; apply-tags.py adapté en conséquence ;
  - libellé EN → « You take a different segment from the figure than the one the property asks for: first identify the correct triangle and its sides ».
- **E3 — poser les 7 étiquettes en attente** N1, N2 et N3, telles que dans `pending-tags/L12.json`, et créer les trois entrées avec les libellés du § 5.3.

**Recommandé, même commit, non bloquant**
- **E4** — 24 Q6 [a] → « √8 = √(4 × 2) = 4√2 لأنّ العامل 4 يخرج من الجذر ، فـ a − b = 4√2 ». Étiquette inchangée.
- **E5** — 23 Q4 [b] : poser `math.alg.produit-nul-racine-signe-non-oppose` (parité avec 28 Q3 [c]).
- **E6** — 24 Q7, explication : « قمّته H (ضلعاه المتقايسان HE و HC) ✓. » → « قمّته H ، وضلعاه المتقايسان هما HE و HC ✓. »
- **E7** — 25 Q2, explication : « AB = AC (لأنّ ABC متقايس الضلعين قمّته A) و AD = AC (لأنّ D مناظرة C بالنسبة إلى A). » → « AB = AC لأنّ ABC متقايس الضلعين قمّته A ، و AD = AC لأنّ D مناظرة C بالنسبة إلى A. »
- **E8** — 24 Q2, explication : « وغير معدومين معًا (لأنّ a² − b² ≠ 0) ، فالمجموع » → « وغير معدومين معًا لأنّ a² − b² ≠ 0 ، فالمجموع ».

**Facultatif**
- **E9** — 29 Q1, explication : « على المستقيم نفسه (AC): (AB) لأنّ المثلّث ABC قائم في A ، و(MC) لأنّ Δ عمودي على (AC) في C. » → « على المستقيم نفسه (AC) ، فالمستقيم (AB) عمودي عليه لأنّ المثلّث ABC قائم في A ، والمستقيم (MC) عمودي عليه لأنّ Δ عمودي على (AC) في C. »
- **E10** — 27 Q4 :
  - [b] « √(x² + 12) » (`math.num.puissance-confondue-avec-produit`, exacte : 6² pris pour 6 × 2) ;
  - [c] « x² + 12 » (muette) ;
  - explication : « ؛ أو اعتبار [OD] وترًا فنجد √(x² − 36). » → « ؛ أو حساب 6² على أنّه 6 × 2 = 12 فنجد √(x² + 12). »
  - Vérifié : longueurs 10, 10, 7, 7 ; 0 paire proche ; rendu OK.
- **E11** — élargissements de libellés : valeur-absolue-somme-additive, difference-carres-confondue, et difference-carres-second-terme-non-eleve-au-carre avec pose sur 23 Q2 [c] (textes au § 5.2).
- **E12** — dans la consigne de la reprise du devoir 14 : garder une option « un seul emplacement » portant N1.

**Hors tranche**
- Moteur : #1138 ne sort pas de l'isolat la « ) » qui ferme un membre de phrase arabe après une formule, ni la « ( » qui l'ouvre avant une formule. Environ 450 isolats sont touchés au publié. Correctif suggéré au § 4.

**Chiffre final**
- 26 questions modifiées re-résolues : 0 divergence.
- 53 correctifs sur 53 appliqués mot pour mot.
- 1 majeur restant : 26 Q4, dû à mon correctif.
- Mineurs :
  - 2 nouveaux : 24 Q6 [a] (formulation que j'avais proposée) et 27 Q4 (domaine) ;
  - parenthèses avalées par l'isolat, texte d'origine : 4 runs dans 3 explications (24 Q7, 25 Q2 deux fois, 24 Q2).
- Étiquettes : les 14 poses de ce tour sont exactes ou acceptables. N1 = 3, N2 = 4, N3 = 4 questions distinctes : créer les trois ; N3 sans compétence, clé absente.

