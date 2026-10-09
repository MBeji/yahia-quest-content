# Audit indépendant — tranche L20 (maths 9ᵉ, ch. 03 calcul littéral, missions 27 à 31)

Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skill `content-audit`).
Périmètre : `content/math/03-calcul-litteral/exercices/27…31` (arbre de travail), 29 questions.
Rien n'est modifié dans le dépôt. Rapport écrit au fil de l'eau.

_Rapport complet : fichiers 27 à 31, partie transversale et chiffre final._

## Méthode (rappel court)

- Clés re-résolues à l'aveugle (script `blind.py` : énoncé + options SANS clé, explication ni étiquette), puis
  comparées ; recalcul sympy exact + flottant de chaque valeur et de chaque option.
- Transcriptions officielles lues : `examens-nationaux/9eme-base/math/2020-technique.md`, `2021-technique.md`,
  `2022-technique.md`, `2024-technique.md` (identiques à `origin/main`).
- Registre des étiquettes et des compétences, cours des chapitres 15, 01, 19, 02, 16, 17, 03 (et 04), missions
  publiées : tout lu sur `origin/main` (d8af0b75).
- Rendu : segmentation par `splitMathRuns` / `isDisplayEquation` de `src/shared/lib/bidi.ts` du moteur
  (`origin/main` a6fc5400), puis rendu Chromium (playwright-core, page `dir=rtl`, classes `.math-run` /
  `.math-equation` du moteur) de chaque ligne d'énoncé, option et explication ; contrôle automatique de
  l'ordre affiché de chaque unité non arabe contre la source, puis captures agrandies des cas signalés.

---

## Fichier 27 — `27-examen-2020-technique-ex1-qcm-carre-somme-puissance-signe-pourcentage.json`

En-tête : d2 · practice · 75/15 · displayOrder 27 · titre « 🏛️ مناظرة 2020 (تقني) · التمرين 1 ⭐⭐: أسئلة اختيار من
متعدّد — … » conforme à l'usage publié (20 titres d'examen QCM portent « (أسئلة) اختيار من متعدّد — »), ne livre
aucune clé. Rampe 2,2,2,2. Fidélité : (√5 + 1)², (4²)³, a − b = 3,14 − π, 1450 DT et 4 % = transcription
2020 technique ex. 1 ; les 3 choix officiels de chaque item sont gardés.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 6 + 2√5 | c (6 + 2√5) | OK | (√5)² + 2√5 + 1 ; 3 distracteurs exacts (6 ; 2(√5 + 1) ; 8√5) |
| 2 | 2¹² | b (2¹²) | OK · réserve mineure | 4⁶ = 4096 = 2¹² ; 4¹², ajouté, fait de 12 le seul exposant répété |
| 3 | a < b | a (a < b, car π > 3,14) | OK · défaut de rendu dans l'explication | encadrement 3,14 < π < 3,15 enseigné (ch. 01, l. 202) |
| 4 | 1508 | c (1508) | OK · réserve mineure | 1450 × 1,04 = 1508 |

Étiquettes (libellés `origin/main`) : 1a `carre-somme-sans-double-produit` exacte ; 1b `puissance-confondue-avec-produit`
exacte (base × exposant) ; 1d `termes-semblables-par-coefficient` conforme à l'usage publié pour « entier fusionné
avec le coefficient d'un radical » (18 Q1, 21 Q1, 17/09 Q2…) ; 2c, 2d `puissances-puissance-exposants-additionnes`
exactes (2 + 3 ; 4 + 3 après 4² = 2⁴) ; 3b `irrationnel-traite-comme-rationnel`, 3c `approximation-defaut-exces-confondues`,
3d `int.subtract-smaller-from-larger` (π − 3,14 au lieu de 3,14 − π) exactes ; 4a `reponse-a-l-autre-inconnue`
(résultat intermédiaire) et 4b `pourcentage-recopie-comme-resultat` exactes. Muets justifiés : 2a « 4¹² » et
4d « 1850 » (aucune entrée du registre ne nomme « 4 % lu 400 »). Aucune étiquette inexacte.

Programme : carré d'une somme (ch. 03), (aᵐ)ⁿ = a^(m × n) (ch. 16, avec la vérification (2³)⁴ = 2¹²),
3,14 < π < 3,15 « قيمة تقريبية بالنقصان » (ch. 01 l. 202-203), comparaison par le signe de a − b (ch. 17 § 1),
pourcentage (acquis par convention, missions publiées 03/16 Q2…) : tout est enseigné avant le ch. 03.

Doublons : 03/16 Q1 (1 + √2)² et 17/13 Q3 (√5 − 1)² portent la même notion mais d'autres données, d'autres
options et d'autres pièges ; 03/16 Q2 (200 000 DT + 20 %) a le même gabarit d'explication que Q4 mais des
distracteurs différents (204, 210 contre 58, 1850) : annales voisines, pas de doublon.

Défauts :

- **[MAJEUR] Q3, explication — rendu bidi.** « 3,14 − π » (deux fois) n'est pas isolé par le moteur :
  `DIGIT_FIRST_FORMULA` n'accepte qu'une lettre latine après l'opérateur, et π est grec. Rendu Chromium
  `dir=rtl` (contrôle automatique + capture) : la formule s'affiche **« π − 3,14 »**. L'élève lit donc
  « فالعدد π − 3,14 سالب » (faux tel qu'affiché) et « أي كتابة π − 3,14 بدل π − 3,14 » (le piège devient
  illisible). « π − 3,14 » (lettre d'abord) et la ligne d'énoncé « a − b = 3,14 − π » (bloc `.math-equation`)
  s'affichent juste. Correctif (vérifié par `splitMathRuns` et dans Chromium : la formule ouvre sur la lettre a,
  le run reste gauche-à-droite) — remplacer
  « فالعدد 3,14 − π سالب. إذن a − b < 0، أي a < b ✓. » par
  « فالفرق a − b = 3,14 − π سالب، أي a < b ✓. »
  et « أو طرح الأصغر من الأكبر، أي كتابة π − 3,14 بدل 3,14 − π، فيخرج فرق موجب، مع أنّ a − b هو مقابل هذا الفرق. » par
  « أو طرح الأصغر من الأكبر، أي حساب π − 3,14 مكان a − b = 3,14 − π، فيخرج فرق موجب، مع أنّ a − b هو مقابل هذا الفرق. »
  (Note moteur : `DIGIT_FIRST_FORMULA` devrait accepter π — à remonter côté arena.)
- **[MINEUR] Q2 — indice de vote.** Avec « 4¹² » ajouté, les bases sont 2/2 mais l'exposant 12 est le seul
  répété (4¹², 2¹²) : un vote sur l'exposant ramène à {4¹², 2¹²}. Correctif : remplacer l'option a « 4¹² » par
  « 4⁸ » (muette ; (4²)³ lu 4^(2³) ; 4⁸ = 2¹⁶ = 65 536 ≠ 4096, vérifié), exposants alors tous distincts (12, 5, 7, 8),
  bases 2/2 ; et dans l'explication remplacer « ومن ضاعف الدليل 6 عند تحويل 4 إلى 2² وأبقى الأساس 4 وجد 4¹²، وهو يساوي 2²⁴ لا 2¹². »
  par « ومن رفع الدليل 2 إلى القوّة 3، أي كتب 4^(2³)، وجد 4⁸، وهو يساوي 2¹⁶ لا 2¹². »
- **[MINEUR · réserve] Q4 — option + donnée = clé.** 1508 est la seule option dont l'écart à la donnée 1450 est
  une autre option (58) : la clé se repère par cohérence sans calculer 4 %. Usage courant du corpus (résultat
  intermédiaire étiqueté `reponse-a-l-autre-inconnue`) ; à garder en connaissance de cause, ou remplacer « 58 »
  par « 2030 » (4 % lu 40 % : 1450 + 580 ; muette ; écarts à 1450 alors 4, 58, 400, 580, aucun n'est une option),
  l'explication remplaçant « أو الاكتفاء بقيمة الزيادة 58 دون إضافتها إلى المرتّب الأوّل » par
  « أو قراءة 4% على أنّها 40% فتخرج زيادة 580 والمرتّب 2030 ».

Verdict 27 : 4/4 clés justes ; 1 majeur (rendu), 2 mineurs. À corriger avant livraison (le majeur seulement est bloquant).

---

## Fichier 28 — `28-examen-2020-technique-ex2-carre-somme-radicaux-produit-signe-somme-de-fractions.json`

En-tête : d3 · boss · 120/30 · displayOrder 28 · titre « 🏛️ مناظرة 2020 (تقني) · التمرين 2 ⭐⭐⭐: نشر مربّع مجموع، واختزال
جذور، وجداء عددين، وإشارة عدد، ومجموع كسرين » (notions seulement). Rampe 2,2,2,2,3,3,3,3 non décroissante : l'ordre
d'émission est l'ordre du fichier. Fidélité : a = (1/2)(1 + √3)², b = (√48 + 3) − (√12 + √27 + 1), 1/(2 + √3) + 1/(2 − √3)
= transcription 2020 technique ex. 2 ; items 1, 2, 3a, 3b, 4 tous repris (Q2, Q4, Q5, Q6, Q8), Q1, Q3, Q7 sont des marches.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 4 + 2√3 | c (4 + 2√3) | OK · **doublon publié** | = 12-repere-plan/20 Q7 (voir majeur) |
| 2 | 2 + √3 | b (2 + √3) | OK | (1/2)(4 + 2√3) |
| 3 | 5√3 | c (5√3) | OK · réserve | 2√3 + 3√3 ; = vérification du cours ch. 02 |
| 4 | 2 − √3 | a (2 − √3) | OK | 4√3 + 3 − 2√3 − 3√3 − 1 |
| 5 (numeric) | 1 | value 1, exacte | OK | (2 + √3)(2 − √3) = 4 − 3, depuis les définitions brutes |
| 6 | d (même signe ; a > 0 donc b > 0) | d | OK | c conclut juste par une règle fausse (« الجداء موجب ⇒ كلاهما موجب ») |
| 7 | a + b | a (a + b) | OK | 1/a = b, 1/b = a |
| 8 | 4 | d (4) | OK | (2 − √3 + 2 + √3)/1 |

Recalcul sympy (exact + flottant) : toutes les clés ; chaque distracteur faux et produit par le chemin que dit
l'explication (10 + √3 = 1 + √3 + 9 ; 13√3 = 4√3 + 9√3 ; 13√6 ; √39 ; 4 + 5√3 ; 2 + 3√3 = 16√3 + 3 − 4√3 − 9√3 − 1 ;
√3 = (4 + 3 − 2 − 3 − 1)√3 ; 8 + 4√3 ; 1/2 ; 4/7 ; 2).

Plans 2×2 : Q1 (constante 4/4/4/10, radical ∅/√3/2√3/√3) — le vote terme à terme donne « 4 + √3 », un distracteur ;
l'option à deux erreurs 10 + √3 est muette. Q3 (13/13/5/1 × 6/3/3/39) — le vote donne « 13√3 », un distracteur ;
13√6, à deux erreurs, est muette. Q4 : le vote sur la constante laisse {2 − √3, 2 + 3√3} (1 sur 2), acceptable.
Aucune clé strictement la plus longue (mesure moteur `longestKey` : 0/27 sur la tranche).

Étiquettes : 1a `carre-somme-sans-double-produit`, 1b `double-produit-sans-facteur-2`, 2a (même), 2c `distribution-partielle`,
2d `operation-inverse-appliquee` (× 2 au lieu de × 1/2), 3b `facteur-racine-sans-carre`, 3d `racine-distribuee-sur-somme`,
4b `termes-semblables-par-coefficient` (usage publié), 4c `facteur-racine-sans-carre`, 4d `moins-devant-parenthese`,
6a `int.produit-signes-negatifs`, 6b `oppose-inverse-confondus`, 7b `frac.add-denominators`, 7c et 8a
`frac.add-numerators-and-denominators`, 7d et 8c `frac.equivalence-un-seul-terme-multiplie` (« تضرب المقام وحده » :
(1 + 1)/(ab)), 8b `difference-carres-somme-au-lieu-de-difference` : toutes exactes. Muets justifiés : 1d, 3a (deux
erreurs), 6c (règle des signes retournée, conclusion juste : aucune entrée ne la nomme exactement).

Règle des signes (Q6) : la clé d invoque « جداء موجب ⇒ الإشارة نفسها », exacte (pour des facteurs non nuls) ; c invoque
« ⇒ كلّ منهما موجب بالضرورة », fausse (contre-exemple (−2) × (−3) = 6, donné dans l'explication). Une seule
justification valide. Étage : Q5 (deux simplifications + conjugué), Q7, Q8 sont de vrais d3 ; Q6 est un d2-d3 (format
« raisonnement motivé ») : en-tête boss honnête.

Programme : identité (ch. 03), extraction de carrés et somme de radicaux semblables (ch. 02), signe d'un produit
(ch. 01/17), conjugué et produit = 1 (ch. 02 « إنطاق المقام » : 1/(√5 + 2) = √5 − 2), somme de fractions et inverse
(acquis, missions publiées 03/10, 17/10) : tout est enseigné ou acquis.

Fuites : ordre d'émission = ordre du fichier ; aucune explication ne donne la clé d'une question SUIVANTE (Q7 ne cite
ni 2 ± √3 ni 4 ; Q8 ne se lit pas dans Q7). Les prémisses « a × b = 1 » de Q6/Q7 portent sur a, b génériques et
reprennent le résultat officiel 3a (convention des prémisses) ; les explications de Q2, Q5, Q8 redonnent des clés
ANTÉRIEURES (4 + 2√3, 2 ± √3, produit 1) : coût connu du donjon, conforme à l'usage publié (03/25 Q6).

Rendu : aucune unité mal ordonnée (contrôle Chromium sur les 8 questions ; chaînes chiffre-seul laissées au sens
natif par conception).

Défauts :

- **[MAJEUR] Q1 — doublon d'une question publiée.** `12-repere-plan/exercices/20-examen-2026-technique-ex1-…` Q7
  pose « (1 + √3)² — ما قيمته ؟ » avec les options 4 [`carre-somme-sans-double-produit`], 4 + √3
  [`double-produit-sans-facteur-2`], 1 + 3√3, 4 + 2√3 (clé) et la même explication (« 1² + 2 × 1 × √3 + (√3)² =
  1 + 2√3 + 3 = 4 + 2√3 ✓ … 1 + 3 = 4 … 4 + √3 »). 28 Q1 a la même donnée, la même clé, trois options sur quatre
  identiques, mêmes étiquettes : le donjon peut tirer les deux. Le Jaccard de surface (0,27) ne le voit pas, les
  énoncés étant tournés autrement. Q1 est une marche ajoutée (l'officiel ne la pose pas) et Q2 développe déjà ce
  carré dans son explication. Correctif : **supprimer Q1** ; la mission garde 7 questions, rampe 2,2,2,3,3,3,3.
- **[MINEUR] Q3 — marche qui recopie le cours, et dont l'énoncé désigne la méthode.** « √12 + √27 » est mot pour mot
  la vérification `::: verifie` du ch. 02 (« احسب √12 + √27 » → 5√3), et « بعد تبسيطهما » dit de simplifier
  chaque radical, ce qui écarte √39 sans réfléchir. Correctif : supprimer Q3 (la mission tombe alors à 6 questions
  qui suivent les items officiels un à un : 2,2,3,3,3,3), ou, si elle reste, réécrire l'énoncé ainsi :
  « ما قيمة المجموع التالي في أبسط صورة ؟\n√12 + √27 ».
- **[MINEUR · cosmétique] Q4** : « نبسّط العدد b المعرَّف بالعبارة التالية، وفيها قوسان وجذور: » : la relative
  « وفيها قوسان وجذور » n'apporte rien. Proposé (on retire la relative, sans reprendre le cadre « نعتبر العدد
  الحقيقي … » déjà très servi) : « نبسّط العدد b المعرَّف بالعبارة التالية:\nb = (√48 + 3) − (√12 + √27 + 1)\nأيّ الكتابات التالية تساوي b في أبسط صورة ؟ ».

Verdict 28 : 8/8 clés justes ; 1 majeur (doublon publié), 2 mineurs. À corriger avant livraison (supprimer Q1).

---

## Fichier 29 — `29-examen-2021-technique-ex2-produit-somme-difference-radical-developpement.json`

En-tête : d3 · boss · 120/30 · displayOrder 29 · titre « 🏛️ مناظرة 2021 (تقني) · التمرين 2 ⭐⭐⭐: جداء عددين، ومجموعهما
وفرقهما، وكتابة عدد تحت الجذر، ونشر عبارة بحرفين » (notions seulement). Rampe 2,2,2,2,2,2,3. Fidélité : a = 2 + √3,
b = 2 − √3, A = (a + b)(a − b), √192, B = a(b − 1) + (a − 1) = transcription 2021 technique ex. 2 ; 1a → Q1, 1b → Q2 + Q3,
2 → Q4 + Q5, 3a → Q6, 3b → Q7 : aucune sous-question perdue ni déformée. Q4 ne propose pas √192 (qui serait une
seconde bonne réponse, = 8√3) : bien vu.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | d (4 − 2√3 + 2√3 − 3 = 1) | d | OK · **indice de vote** | chaque distracteur change UN terme de la clé |
| 2 | 4 | b (4) | OK | (2 + 2) + (√3 − √3) |
| 3 | 2√3 | c (2√3) | OK | 2 + √3 − 2 + √3 |
| 4 | 8√3 | d (8√3) | OK · étiquette ambiguë | 4 × 2√3 ; « 0 » a deux chemins |
| 5 | 192 | c (192) | OK | n = (8√3)² = 64 × 3 |
| 6 | ab − 1 | d (ab − 1) | OK | ab − a + a − 1 |
| 7 | 0 | b (0) | OK · étiquette ambiguë | ab − 1 = 0 ; « 1 + √3 » a deux chemins |

Recalcul sympy : clés justes ; 7 = 4 + 3, 4 − √6, 1 − 4√3, 14 = a² + b², 24, 67, 576 = 64 × 9, −1 − √3 = a(b − 1),
1 + √3, ab + a − 2, ab + 2a − 1 conformes aux chemins des explications. Aucune égalité fausse dans les explications.

Étiquettes : 1a `int.produit-signes-negatifs`, 1b `racine-produit-transforme-en-somme`, 2c `termes-semblables-par-coefficient`
(usage publié), 2d `int.signe-ignore-dans-somme`, 3a `moins-devant-parenthese`, 3b `radicaux-semblables-radicande-additionne`,
4b `difference-carres-somme-au-lieu-de-difference`, 4c `operation-inverse-appliquee` (somme au lieu du produit),
5a `facteur-racine-sans-carre` (le libellé cite justement 3√2 = √18), 5b `racine-produit-transforme-en-somme`,
5d `racine-et-carre-confondus` ((√3)² lu 9), 6b `distribution-partielle`, 6c `int.produit-signes-negatifs`,
7a, 7c `reponse-a-l-autre-inconnue` (résultat intermédiaire a(b − 1), ab) : exactes. Muets justifiés : 2a « 0 »
(conjugué pris pour l'opposé, aucune entrée), 3d, 6a (terme oublié). 1c « 1 − 4√3 » est muet alors que
l'explication nomme l'erreur ET l'option (« إعطاء الجداء √3 × 2 إشارة سالبة … 1 − 4√3 ») : porte R1, elle
mériterait `int.produit-signes-negatifs` — sans objet si le correctif de vote ci-dessous est retenu.

Programme, point R-3 (i) : « n√m = √(n²m) » n'est pas enseigné comme technique (le ch. 02 n'enseigne que l'extraction),
mais Q5 se résout par deux propriétés enseignées : la définition (√n)² = n, (√a)² = a (ch. 02) et le carré d'un produit
(ab)² = a²b² (ch. 16 « (a × b)^n = a^n × b^n ») ; la seconde voie de l'explication (√64 × √3 = √(64 × 3)) lit la règle du
produit de droite à gauche, comme le cours le fait (√54/√6 = √(54/6), √2 × √8 = √16). L'énoncé dit la forme visée
(√n, n entier naturel). Verdict : acquis par combinaison, pas un défaut. (Hors tranche : le cours du ch. 02 gagnerait
une ligne « 3√2 = √9 × √2 = √18 », que le libellé de `facteur-racine-sans-carre` suppose déjà.)

Fuites : aucune explication ne donne une clé SUIVANTE ; Q4 n'écrit jamais √192 (ni dans les options ni dans
l'explication) : n = 192 n'est pas livré. Mais l'énoncé de Q5 nomme « العدد A يساوي 8√3 », avec la lettre A de Q4 :
au donjon, Q5 tirée avant Q4 livre la clé de Q4 (voir mineur).

Rendu : aucune unité mal ordonnée (contrôle Chromium sur les 7 questions).

Étage (demandé) : une seule question d3 (Q7), six d2 d'une seule étape chacune (Q2 = 4 se fait de tête). Le profil
2,2,2,2,2,3 est publié en boss (03/17, 03/18, 03/25) mais aussi en practice d2 (03/24 et 03/26, deux sujets
techniques ex. 2, le même gabarit d'items). La charge réelle de 29 est celle de 24 et 26 : l'en-tête boss n'est pas
mensonger (une vraie d3), mais il est le moins défendable des trois ; je recommande practice d2 (75/15, titre ⭐⭐),
sans relever aucune étape (la règle interdit de durcir une étape facile pour tenir l'étage).

Défauts :

- **[MAJEUR] Q1 — vote terme à terme.** Les quatre chaînes partagent « 4 − 2√3 » ; 3ᵉ terme : +2√3 dans a, b, d,
  −2√3 dans c ; 4ᵉ terme : +3 (a), −√6 (b), −3 (c, d). Le vote terme à terme reconstruit « 4 − 2√3 + 2√3 − 3 », la
  clé, sans rien calculer. Correctif (plan 2×2) : remplacer l'option c « 4 − 2√3 − 2√3 − 3 = 1 − 4√3 » par
  « 4 − 2√3 − 2√3 + 3 = 7 − 4√3 » (muette : deux signes faux, ou b × b développé ; 7 − 4√3 ≠ 1, vérifié) ; le vote
  donne alors « 4 − 2√3 + 2√3 + 3 », le distracteur a. Clé non la plus longue (b et c′ sont plus longues). Dans
  l'explication, remplacer « أو إعطاء الجداء √3 × 2 إشارة سالبة فلا يتلاشى الحدّان الأوسطان ويخرج 4 − 2√3 − 2√3 − 3 = 1 − 4√3. »
  par « أو الخطأ في إشارتين معًا، √3 × 2 سالبًا و √3 × (−√3) موجبًا، فلا يتلاشى الحدّان الأوسطان ويخرج 4 − 2√3 − 2√3 + 3 = 7 − 4√3. »
- **[MINEUR] Q4, option a « 0 » — étiquette ambiguë.** Deux chemins : a − b = 0 en ne changeant que le premier signe
  (l'erreur de Q3, la plus naturelle quand on calcule (a + b)(a − b) facteur par facteur), ou a² − b² avec les deux
  doubles produits oubliés (7 − 7, celui qu'étiquette `carre-somme-sans-double-produit`). Correctif : retirer
  l'étiquette (muette), l'explication pouvant garder les deux chemins : ajouter « أو قلب إشارة الحدّ الأوّل وحده من b فيصير a − b = 0 ويخرج A = 4 × 0 = 0 ».
- **[MINEUR] Q7, option d « 1 + √3 » — étiquette ambiguë.** 1 + √3 = ab + a − 2 (`distribution-partielle`), mais aussi
  a − 1, le second terme seul — le pendant exact de l'option a (a(b − 1) seul, étiquetée `reponse-a-l-autre-inconnue`).
  Correctif : retirer l'étiquette (muette).
- **[MINEUR] Q5 — prémisse qui livre la clé de Q4 au donjon.** « العدد A يساوي 8√3 » reprend la lettre A définie en Q4.
  Correctif : « نريد كتابة العدد 8√3 تحت جذر تربيعي واحد، أي على الصورة √n حيث n عدد صحيح طبيعي. ما قيمة n ؟ »
  (même tâche, même clé 192, plus de lien avec le A de Q4 ; vérifié par `splitMathRuns` : « 8√3 » et « √n » isolés).
- **[MINEUR] Étage** : passer en practice d2 (75/15), titre « … · التمرين 2 ⭐⭐: … » (voir plus haut), ou le justifier
  au rapport de livraison par l'usage 03/17-18-25.

Verdict 29 : 7/7 clés justes ; 1 majeur (vote), 4 mineurs. À corriger avant livraison (Q1).

---

## Fichier 30 — `30-examen-2022-technique-ex2-radicaux-carre-difference-produit-signe-equation.json`

En-tête : d3 · boss · 120/30 · displayOrder 30 · titre « 🏛️ مناظرة 2022 (تقني) · التمرين 2 ⭐⭐⭐: اختزال جذور، ونشر مربّع فرق،
وجداء عددين، وإشارة عدد، وحلّ معادلة بسيطة » (notions seulement). Rampe 2,2,3,3,3. Fidélité : a = 7 + 4√12 − √48,
b = (2 − √3)², x(7 + 4√3) = 1 = transcription 2022 technique ex. 2 ; 1a → Q1, 1b → Q2, 2a → Q3 (depuis les formes brutes),
2b → Q4, 2c → Q5 : rien de perdu ni de déformé.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 7 + 4√3 | b | OK | 7 + 8√3 − 4√3 |
| 2 | 7 − 4√3 | c | OK | 4 − 4√3 + 3 ; plan 2×2 parfait (7/1 × ∅/−4√3) |
| 3 | 1 | a | OK | (7 + 4√3)(7 − 4√3) = 49 − 48, depuis les formes brutes |
| 4 (multi) | {b, d} | {b, d} | OK · réserve de forme | voir le jugement des cinq arguments |
| 5 | 7 − 4√3 | d | OK | 1/(7 + 4√3) = 7 − 4√3 (conjugué, ou ab = 1) |

Jugement de chaque argument de Q4, AVANT lecture de la clé : a — invalide (« la différence de deux positifs est
toujours positive » est faux : 3 − 5 = −2), conclusion vraie ; b — valide (ab = 1 > 0 ⇒ même signe ; a > 0) ;
c — invalide et conclusion fausse (4√3 ≈ 6,93, pas 12) ; d — valide (7 et 4√3 positifs, 49 > 48 ⇒ 7 > 4√3) ;
e — invalide (7 > 4 et √3 > 0 n'entraînent pas 7 > 4√3 : 7 − 4√10 ≈ −5,65 < 0), conclusion vraie. Deux justes,
b et d = clé. La consigne « اختر كلّ الاستدلالات الصحيحة » n'annonce pas le nombre ; l'explication justifie chaque
juste et réfute chaque faux (contre-exemples 3 − 5 et 7 − 4√10, vérifiés).

Recalcul sympy : clés ; 7 (√12 = 4√3, √48 = 16√3), 11√3, 7 + 12√3, 7, 1, 1 − 4√3, 97, 49 ± 28√3, −7 − 4√3 (produit
−97 − 56√3 < 0), −7 + 4√3 (produit −1), (7 − 4√3)/97 : conformes aux chemins des explications.

Étiquettes : 1a `facteur-racine-sans-carre`, 1c `termes-semblables-par-coefficient`, 1d `operation-inverse-appliquee`
(addition au lieu de la soustraction), 2a `carre-somme-sans-double-produit` (« somme ou différence »), 2d
`carre-difference-signes`, 3b `difference-carres-somme-au-lieu-de-difference`, 3c `carre-somme-sans-double-produit`
(b = 7 propagé), 3d `facteur-racine-sans-carre` (a = 7 propagé), 5a `oppose-inverse-confondus`, 5c
`difference-carres-somme-au-lieu-de-difference` : exactes. Muets : 2b « 1 » (voir la famille « (a − b)² écrit
a² − b² », section transversale), 5b « −7 + 4√3 » (opposé de l'inverse : deux gestes, aucune entrée exacte),
Q4 multi (pas d'étiquette possible).

Programme, point R-3 (ii) : x(7 + 4√3) = 1 se résout par la définition de l'inverse (acquise) ou en divisant par un
nombre non nul — `ax + b = c` est enseigné en 7ᵉ (`math-7eme/06-equations`, « حلّ معادلةٍ من الشكل ax + b = c ») et en
8ᵉ (`math-8eme/04-mua3adalat-daraja-oula`, y compris « معاملٌ كسريّ … نضرب في المقلوب ») ; le conjugué est au ch. 02.
Acquis, pas un défaut. Comparaison de deux positifs par leurs carrés : ch. 17 § « مقارنة مربّعَي عددين ».

Fuites : aucune explication ne donne une clé suivante. L'énoncé de Q4 redonne a = 7 + 4√3, b = 7 − 4√3 (résultats
« بيّن أنّ » 1a, 1b) et ab = 1 : à noter que l'officiel 2a est « أحسب ab » et non « بيّن أنّ ab = 1 » — la prémisse est
le résultat de l'étape précédente (2b « استنتج »), conforme à l'esprit, mais elle livre la clé de Q3 au donjon ; le fait
(7 + 4√3)(7 − 4√3) = 1 est de toute façon public dans le corpus (03/19 Q1 et Q3, 17/16 Q4). Pas de défaut.

Doublons : 03/19 Q1 et 17/16 Q4 calculent le même produit (options 1, 97 partagées) mais depuis les formes réduites ;
Q3 part des formes brutes (autre angle). 03/25 Q3 (multi) contient « b² = 7 − 4√3 » et « b² = 1 » pour b = 2 − √3 : même
calcul que Q2, deux pièges communs, mais item officiel des deux sessions et format différent — gabarit voisin, accepté.
Dans la tranche, Q4 et 28 Q6 posent la même tâche (signe de b depuis ab = 1 et a > 0) avec le même argument juste
(« الجداء موجب ⇒ الإشارة نفسها ») : deux sessions officielles posent l'item ; formats différents (mcq / multi avec une
seconde voie par les carrés) — mineur, voir plus bas.

Rendu : aucune unité mal ordonnée (Chromium, dont les cinq options du multi : « 7² = 49 » s'affiche « 49 = 7² » en
lecture gauche-droite, chaîne chiffres-seuls laissée au sens natif par conception, égalité vraie dans les deux sens).

Étage : Q3 (deux simplifications + conjugué), Q4 (cinq raisonnements), Q5 (inverse à radicaux) sont de vrais d3 :
en-tête boss honnête.

Défauts :

- **[MINEUR] Q4 — indice de longueur.** Longueurs (caractères) : d 89 (juste), b 77 (juste), a 71, c 48, e 38 : la plus
  longue est juste et les deux plus courtes sont fausses. Correctif (vérifié : longueurs b 77, e′ 77, c′ 76, a 71, d′ 70 ;
  rendu Chromium sans défaut ; aucun argument ne change de statut) :
  d → « مربّعا الموجبين 7 و 4√3 هما 49 و 48 ، و 49 > 48 ، إذن 7 > 4√3 و b موجب » (valide) ;
  c → « 4√3 = 4 × 3 = 12 لأنّ الجذر يزول عند الضرب ، و 12 > 7 ، إذن 4√3 > 7 و b سالب » (invalide, conclusion fausse) ;
  e → « 7 > 4 و √3 عدد موجب ، فتكفي مقارنة العدد 7 بالمعامل 4 وحده ، إذن 7 − 4√3 موجب » (invalide : c'est
  exactement le geste que l'explication réfute par 7 − 4√10).
- **[MINEUR] Gabarit répété dans la tranche : Q4 ↔ 28 Q6.** Même tâche, même argument juste presque mot pour mot
  (28 Q6 d « جداء a و b موجب ، فلهما الإشارة نفسها ، وبما أنّ a موجب فإنّ b موجب » ; 30 Q4 b « لدينا a × b = 1 > 0 ،
  فالعددان a و b من الإشارة نفسها ؛ و a موجب ، إذن b موجب »). Acceptable parce que les deux sessions posent l'item et
  que les formats diffèrent ; à signaler au registre de tranche, sans correctif obligatoire.

Verdict 30 : 5/5 clés justes ; 0 majeur, 2 mineurs. Livrable en l'état (le correctif de longueur est recommandé).

---

## Fichier 31 — `31-examen-2024-technique-ex1-qcm-isolation-pourcentage-carre-difference.json` (autre auteur, jamais audité)

En-tête : d2 · practice · 75/15 · displayOrder 31 · titre « 🏛️ مناظرة 2024 (تقني) · التمرين 1 ⭐⭐: أسئلة اختيار من متعدّد — عزل
المجهول ونسبة مائوية من كتلة ونشر مربّع فرق » (usage QCM publié, notions seulement). Rampe 1,2,2,2,3.
Fidélité : 3 − x = 2/3 ; 75 % / 25 % ; 12 غ ; (5 − √5)² = transcription 2024 technique ex. 1, items 1, 2, 3.

Écart sur l'item 4 (patron d'une pyramide) : **justifié**, deux fois. (1) La fiche programme 9ᵉ
(`programme/9eme-base/maths.md`, ch. 13) l'écrit en toutes lettres : « ⛔ Aucun patron (نشر) : le mot n'apparaît nulle
part » (l. 9220), et « Ni patron, ni section, ni aire latérale d'un solide » (l. 3083). (2) Un item d'espace n'a pas sa
place au ch. 03. Les trois items gardés conservent leur substance (isoler, pourcentage d'une masse, carré d'une
différence à radical) ; les choix officiels sont adaptés : item 1 {1/3, 11/3, 7/3} → Q2 {−1/3, 1/3, −7/3, 7/3}
(11/3 écarté à raison : avec −7/3 il ferait reconstruire 7/3 par vote — grandeurs 7, 7 ; signe + majoritaire — et
l'erreur 3 + 2/3 reste en Q1) ; item 2 {7.5, 9, 3} gardés + 16 ; item 3 {30 − 10√5, (√5)², 20} → (√5)² remplacé.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | x = 3 − 2/3 | b | OK · étiquettes à revoir | plan 2×2 sur les signes de 3 et 2/3, pas de vote |
| 2 | 7/3 | d (7/3) | OK · étiquette ambiguë | 9/3 − 2/3 ; plan 2×2 signe × grandeur |
| 3 | 9 g | c (9 غ) | OK · explication incomplète | 0,75 × 12 |
| 4 | 5² − 2 × 5 × √5 + (√5)² | a | OK · **doublon de fait avec Q5** | plan 2×2 parfait |
| 5 | 30 − 10√5 | b | OK · étage gonflé | 25 − 10√5 + 5 ; plan 2×2 parfait |

Recalcul sympy : x = 7/3 (solve) ; options de Q1 = −7/3, 7/3, 11/3, −11/3 ; 1/3 = 3/3 − 2/3 ; −1/3 = 2/3 − 3/3 ;
9 = 0,75 × 12, 3 = 25 %, 16 = 12 ÷ 0,75 ; (5 − √5)² = 30 − 10√5 ≈ 7,64 ; 30, 20 = 25 − 5, 20 − 10√5. Les quatre options de Q4,
évaluées, donnent EXACTEMENT les quatre options de Q5 (a → 30 − 10√5, b → 30, c → 20, d → 20 − 10√5).

Étiquettes (libellés `origin/main`) : 2b `frac.entier-converti-en-n-sur-n` (3 = 3/3) exacte ; 3a `reponse-a-l-autre-inconnue`
(les 25 %) et 3d `operation-inverse-appliquee` (÷ au lieu de ×) exactes ; 4b et 5c `carre-somme-sans-double-produit`,
4d et 5a `carre-difference-signes` exactes ; 1d `transposition-sans-changer-signe` (3 passé à droite sans changer de
signe : −x = 2/3 + 3) acceptable. Muets : 2a « −1/3 » (deux erreurs), 3b « 7,5 غ » (geste non reconstructible), 4c
« 5² − (√5)² » et 5d « 20 » (famille « (a − b)² écrit a² − b² », voir la section transversale).

Programme (R-3) : isoler x dans 3 − x = 2/3 est acquis — `math-7eme/06-equations` (« حلّ معادلةٍ من الشكل ax + b = c »)
et `math-8eme/04-mua3adalat-daraja-oula` ; pourcentage d'une quantité et coefficient multiplicateur : `math-8eme/05`
(« حسابُ نسبةٍ مئوية من كمّية ») ; carré d'une différence : ch. 03. Rien n'est hors programme.

Rendu : aucune unité mal ordonnée (Chromium) ; « 3 − x = 2/3 » dans la phrase de Q2 est isolé par `DIGIT_FIRST_FORMULA`
et s'affiche dans l'ordre ; « 75 % », « 12 غ » se lisent juste. Unité : « غ » (et non « g ») suit l'officiel et le
précédent publié du gisement (07/14 « كغ ») ; la règle `math-and-notation` (symboles SI) dirait « g » — à trancher une
fois pour tout le gisement, pas un défaut de ce lot.

Défauts :

- **[MAJEUR] Q4 ↔ Q5 — doublon de fait dans la mission.** Même nombre (5 − √5)², mêmes trois erreurs avec les mêmes
  étiquettes, options en correspondance un pour un (Q5 = Q4 calculé) : l'élève qui a la clé de l'une a celle de
  l'autre, et le retour de Q4 (route quête, Q4 avant Q5) livre Q5. L'officiel pose UN item (la valeur). Correctif :
  **supprimer Q4** et passer Q5 en d2 ; la mission garde 4 questions (rampe 1,2,2,2), comme 27 et 03/16.
- **[MINEUR] Q5 — difficulté gonflée.** (5 − √5)² est une application directe d'identité, étiquetée d2 partout ailleurs
  dans la tranche ((√5 + 1)² en 27 Q1, (2 − √3)² en 30 Q2) ; d3 ne tient que par l'ordre. Correctif : `difficulty: 2`
  (sans objet si Q4 est supprimée, voir ci-dessus).
- **[MINEUR] Q1/Q2 — étiquettes de transposition.** 1a « x = 2/3 − 3 » et 2c « −7/3 » ont deux chemins : −x passé à
  droite sans changer de signe (l'étiquette posée) OU −x = 2/3 − 3 puis oubli de la division par −1 — geste nommé
  exactement par `math.alg.coefficient-non-divise` (« تتوقّف قبل القسمة على معامل المجهول »), et plus fréquent.
  Règle « deux erreurs, une option » : retirer l'étiquette de 1a et de 2c. À l'inverse 1c « x = 3 + 2/3 », laissée
  muette, s'obtient par UNE transposition (3 = 2/3 + x, puis 2/3 passé à gauche sans changer de signe : 3 + 2/3 = x) :
  poser `math.alg.transposition-sans-changer-signe`. Dans l'explication de Q1, remplacer le paragraphe « الخطأ الشائع:
  نقل −x دون تغيير إشارته … ثمّ إهمال علامة الناقص أمام x. » par
  « الخطأ الشائع: كتابة −x = 2/3 − 3 ثمّ نسيان القسمة على −1 فيبقى x = 2/3 − 3 (ويعطيه أيضًا نقل −x دون تغيير إشارته)؛ أو نقل 3 دون تغيير إشارته فنكتب −x = 2/3 + 3 ومنه x = −3 − 2/3؛ أو نقل 2/3 دون تغيير إشارته فنكتب 3 + 2/3 = x. »
  (vérifié : chaque chemin donne l'option nommée ; rendu Chromium sans défaut, « −x », « −1 » et « 3 + 2/3 = x » isolés).
- **[MINEUR] Q3 — distracteur officiel non expliqué.** L'explication ne dit rien de « 7,5 غ ». Ajouter à la fin :
  « أمّا 7,5 غ فلا تساوي 75 % من 12 غ، لأنّ 0,75 × 12 = 9. » (vérification seule, sans prêter à l'élève un geste qu'on ne
  sait pas reconstruire).
- **[MINEUR · cosmétique] Q2** : l'équation est dans la phrase (« حيث 3 − x = 2/3 فإنّ »), alors que Q1 et l'usage publié
  (12/20 Q6) la posent seule ; rendu correct, mais pour l'homogénéité : « إذا كان x عددًا حقيقيًّا يحقّق:\n3 − x = 2/3\nفإنّ x يساوي : ».
- **[NOTE] Q1 → Q2** : Q1 (d1, isoler) donne l'expression dont Q2 (d2) demande la valeur ; acceptable, car Q2 teste un
  autre geste (9/3 − 2/3, piège 3 = 3/3) et aucune explication de Q1 ne calcule 7/3.

Verdict 31 : 5/5 clés justes ; 1 majeur (Q4/Q5), 3 mineurs + 1 cosmétique. À corriger avant livraison (supprimer Q4).

---

## Partie transversale

### Étiquettes — la famille « (a − b)² développé comme a² − b² »

Occurrences (lues sur `origin/main` + tranche) : **03/22 Q1 c** « (5 + 2√10)/4 » (étiquetée
`math.alg.difference-carres-confondue`), **09/24 Q5 b** « 12√2 » (même étiquette), **30 Q2 b** « 1 » (muette),
**31 Q4 c** « 5² − (√5)² » (muette), **31 Q5 d** « 20 » (muette ; l'explication dit « تجمع الخطأين », mais oublier 2ab ET
rendre +b² négatif, c'est mot pour mot écrire a² − b²), plus **03/25 Q3 c** « b² = 1 » (multi, non étiquetable). Soit
quatre à cinq questions distinctes étiquetables : le seuil de 3 est franchi, l'erreur se dit en une phrase, et le cours
du ch. 03 la nomme déjà (« ⚠️ الخلط بين a² − b² و (a − b)² »). Les autres familles muettes de la tranche (conjugué pris
pour l'opposé, opposé de l'inverse, 4 % lu 400, exposant doublé au changement de base) n'ont qu'une occurrence chacune
(recherche dans les explications de tout `content/math`) : elles restent muettes.

**L'étiquette posée en 22 Q1 (et en 09/24 Q5) est inexacte** : le libellé de `difference-carres-confondue` (« Tu
confonds une différence de deux carrés avec un carré : elle se factorise en un produit de la somme par la différence » /
« تخلط بين فرق مربّعَين والمربّع: فرق المربّعَين يُعمَّل إلى جداء المجموع في الفرق ») corrige le sens de la
FACTORISATION (a² − b² traité comme un carré) — juste pour 03/12 Q1, 03/18 Q4, 04/28 Q10 — et non le développement
(a − b)² → a² − b², où l'élève lit une règle de factorisation qui ne répond pas à son geste.

**Nouvelle étiquette proposée** (identifiant libre sur `origin/main`, rendu du libellé arabe vérifié par `splitMathRuns`
et dans Chromium, même gabarit que `difference-carres-somme-au-lieu-de-difference`) :

```json
"math.alg.carre-difference-ecrit-difference-carres": {
  "subject": "math",
  "labels": {
    "fr": "Tu développes le carré d'une différence comme une différence de carrés : (a − b)² vaut a² − 2ab + b², pas a² − b²",
    "en": "You expand the square of a difference as a difference of squares: (a − b)² is a² − 2ab + b², not a² − b²",
    "ar": "تنشر مربّع الفرق كأنّه فرق مربّعين: (a − b)² تساوي a² − 2ab + b² لا a² − b²"
  },
  "competency": "math.alg.identites-remarquables"
}
```

À poser sur 30 Q2 b, 31 Q4 c (ou, si Q4 est supprimée, 31 Q5 d, en remplaçant dans son explication « والقيمة 20 تجمع
الخطأين » par « أو الخلط بين مربّع الفرق وفرق المربّعين فنكتب 5² − (√5)² = 25 − 5 = 20 » — rendu vérifié) ; et, hors tranche,
à substituer à `difference-carres-confondue` sur 03/22 Q1 c et 09/24 Q5 b (fichiers publiés, à corriger par la session
de livraison).

Bilan des étiquettes de la tranche : aucune étiquette inventée (toutes dans le registre `origin/main`, `content:check`
vert) ; inexactes ou ambiguës : 29 Q4 a, 29 Q7 d, 31 Q1 a, 31 Q2 c (à rendre muettes) ; muettes qui méritent une
étiquette EXISTANTE : 31 Q1 c (`transposition-sans-changer-signe`), 29 Q1 c (`int.produit-signes-negatifs`, sans objet si
le correctif de vote est pris). Choix déclarés confirmés : 29 Q2 « 0 » muette ; `oppose-inverse-confondus` juste en
28 Q6 b et 30 Q5 a.

### Programme (R-3) — arbitrages demandés

- (i) 29 Q5 « 8√3 = √n » : technique non enseignée comme telle, mais déductible de deux propriétés enseignées ((√n)² = n
  au ch. 02 ; (ab)² = a²b² au ch. 16) ; acquis, pas un défaut.
- (ii) 30 Q5 x(7 + 4√3) = 1, 31 Q1-Q2 (3 − x = 2/3) : équations ax + b = c enseignées en 7ᵉ et 8ᵉ (`math-7eme/06`,
  `math-8eme/04`), inverse = définition acquise ; acquis.
- (iii) 27 Q3 : « 3,14 < π < 3,15 … قيمة تقريبية بالنقصان » au ch. 01 (l. 202-203) ; comparaison par le signe de a − b au
  ch. 17 ; enseigné.
- Autres : (a ± b)² et a² − b² (ch. 03), conjugué et 1/(√5 + 2) = √5 − 2 (ch. 02, « إنطاق المقام »), signe d'un produit
  (acquis, relatifs), pourcentage (`math-8eme/05` : « حسابُ نسبةٍ مئوية من كمّية » et coefficient 1 + t/100), puissance
  de puissance (ch. 16), comparaison par les carrés (ch. 17). **Aucune technique testée n'est ni enseignée ni donnée.**

### Étages

27 practice d2 : juste. 28 boss d3 : juste (Q5, Q7, Q8 vrais d3, Q6 limite). 29 boss d3 : une seule d3 (Q7) et six
étapes d'un geste — recommandé practice d2 (comme 03/24 et 03/26, même gabarit technique ex. 2), ou justification par
03/17-18-25. 30 boss d3 : juste (trois vrais d3). 31 practice d2 : juste, mais Q5 d3 est gonflé (→ d2). Rampes toutes
non décroissantes en ordre de fichier (l'ordre d'émission est donc celui des fichiers).

### Doublons

- Publiés : **28 Q1 = 12-repere-plan/20 Q7** (même (1 + √3)², même clé, 3 options sur 4 identiques) — majeur. Gabarits
  voisins acceptés (sessions différentes, angles ou options différents) : 27 Q1 ~ 03/16 Q1 et 17/13 Q3 ; 27 Q4 ~ 03/16 Q2 ;
  29 Q1 ~ 03/25 Q2 ; 30 Q2 ~ 03/25 Q3 ; 30 Q3 ~ 03/19 Q1, 17/16 Q4 ; 28 Q8 ~ 17/10 Q5. Le cadre « نعتبر العدد الحقيقي … ما
  كتابة … في أبسط صورة ؟ » ne revient PAS dans la tranche (cadres variés ; similarité de cadre max 0,43, 27 Q1 ↔ 17/16 Q1).
- Internes à une mission : **31 Q4 ↔ Q5** (doublon de fait) — majeur ; 31 Q1 → Q2 acceptable.
- Entre missions de la tranche : 30 Q4 ↔ 28 Q6 (même tâche, même argument juste) — mineur. Le carré « (p ± √q)² »
  revient cinq fois (27 Q1, 28 Q1, 30 Q2, 31 Q4, 31 Q5) ; les deux suppressions demandées (28 Q1, 31 Q4) le ramènent à trois
  items, chacun officiel. Aucune paire de missions ne diffère que par ses nombres.
- Jaccard de surface (fonctions du moteur, tout `content/math`) : max 0,42 contre le publié (31 Q1 ↔ 04/09 Q6, deux
  équations différentes) et 0,39 pour 27-30 (28 Q5 ↔ 09/21 Q3) ; 0,36 en interne : conforme à la déclaration de l'auteur,
  mais la mesure ne voit pas les deux doublons majeurs ci-dessus (énoncés tournés autrement).

### Fuites

Aucune fuite EN AVANT dans 27-30 (ordre d'émission = ordre du fichier ; Q7 de 28 ne livre pas 4 ; Q4 de 29 ne livre pas
192). 31 Q4 → Q5 en est une (traitée par la suppression de Q4). Au donjon, les prémisses de 28 Q6-Q7 (ab = 1 sur a, b
génériques), 30 Q4 (a, b, ab = 1 — fait déjà public au corpus) relèvent de la convention des prémisses ; seule celle de
29 Q5 (« العدد A يساوي 8√3 », lettre de Q4) mérite le petit correctif proposé. Aucune décimale de vérification qui livre
un verdict ; chaque coche ✓ suit la clé de sa question (27-31 relus).

### Rendu arabe, figures, notation

Un seul défaut d'ordre affiché, **27 Q3 (explication)** : « 3,14 − π » rendu « π − 3,14 ». Cause moteur : `DIGIT_FIRST_FORMULA`
(arena `src/shared/lib/bidi.ts`) n'admet qu'une lettre latine après l'opérateur. Mesure sur le corpus (`origin/main` + tranche) :
46 segments arabes « chiffre opérateur … π » non isolés, dont une partie seulement change de sens (les produits et
sommes « 4 × π », « 12 + 81π » se lisent dans les deux sens ; les différences, non : « 3 − π » en 19/05, « 6 − 2π » en
09/18, « 3,14 − π » ici) — à remonter côté
arena (accepter π, σ, Ω dans la classe de lettres), le correctif de contenu de 27 Q3 restant utile tant que le moteur n'a
pas bougé. Aucune ligne de formule seule refusée par `isDisplayEquation`, aucune paire d'options à virgule arabe, aucun
« على الشكل التالي » dans un énoncé (les « من الشكل (u + v)(u − v) » des explications de 28 Q5, Q8 et 30 Q3 ne touchent pas
`FIGURE_REFERENCE`). Aucune figure dans la tranche, et aucune n'y servirait (calcul pur). Balayages : chiffres
arabo-indiens, LaTeX, `$`, groupes de chiffres à espace simple, radicande arabe, tiret pour moins, virgule arabe en
notation : 0. `content:check` vert ; `content:qa --strict` : 0 erreur, aucun avertissement sur 27-31 ; clé strictement la
plus longue : 0/27 (mcq).

---

## Chiffre final

| fichier | questions | clés fausses | critiques | majeurs | mineurs | questions à reprendre |
| --- | --- | --- | --- | --- | --- | --- |
| 27 | 4 | 0 | 0 | 1 (Q3 rendu) | 2 | Q3 (obligatoire), Q2 (recommandé), Q4 (au choix) |
| 28 | 8 | 0 | 0 | 1 (Q1 doublon publié) | 2 | Q1 (supprimer), Q3, Q4 (cosmétique) |
| 29 | 7 | 0 | 0 | 1 (Q1 vote) | 4 | Q1, Q4, Q5, Q7 + en-tête (étage) |
| 30 | 5 | 0 | 0 | 0 | 2 | Q4 (longueurs), Q2 (nouvelle étiquette) |
| 31 | 5 | 0 | 0 | 1 (Q4/Q5 doublon) | 3 (+1 cosmétique) | Q4 (supprimer), Q5, Q1, Q2, Q3 |
| **total** | **29** | **0** | **0** | **4** | **13** | **4 bloquantes** (27 Q3, 28 Q1, 29 Q1, 31 Q4) ; 15 questions touchées hors options facultatives |

Hors tranche, à transmettre : nouvelle étiquette `math.alg.carre-difference-ecrit-difference-carres` (registre) et
réétiquetage de 03/22 Q1 c et 09/24 Q5 b ; correctif moteur de `DIGIT_FIRST_FORMULA` (π) ; décision de gisement sur
« غ / كغ » contre « g / kg ».

Verdict de la tranche : **à corriger avant livraison** (4 majeurs, aucun défaut critique, toutes les clés justes).
