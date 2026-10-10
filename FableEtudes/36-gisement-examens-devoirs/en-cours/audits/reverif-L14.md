# Re-vérification ciblée — tranche L14 (maths 9ᵉ, ch. 09, missions 36 à 41) après le tour de corrections

Auditeur indépendant (même consigne que `audit-L14.md`). Fichiers relus dans l'arbre de travail tels quels ; questions
touchées re-résolues à l'aveugle AVANT lecture de la clé ; rien n'est modifié dans le dépôt. Priorité : les défauts
INTRODUITS par les correctifs (ceux de l'audit comme ceux de l'auteur).

_Re-vérification complète : fichiers 36 à 41, étiquettes, gates, chiffre final._

## Méthode

- Version auditée = `l14-work/snap-audit-before/` : empreintes sha256 identiques, fichier par fichier, à celles que
  j'avais relevées à la fin de l'audit (0761eade…, e54696be…, 6ee10a6c…, 5efaaf95…, d952113e…, af03d951…). Arbre
  actuel relevé au début de cette passe : 52a06472…, 0908b044…, f4647571…, 35d044cf…, def286cc…, 74b7b5c9….
- Diff structurel aveugle (énoncés, options, type, difficulté, en-têtes — sans clé, explication ni étiquette), puis
  diff élément par élément des SVG. Questions touchées :
  36 Q2 (figure), Q6 ; 37 Q2 (figure + option b), Q3 (énoncé), Q4, Q7, Q9 (figure), Q10 (figure), Q11, Q12 (énoncé) ;
  38 en-tête, Q1 (ex-Q2, d1), Q2 (ex-Q1, inchangée), Q4 (énoncé + figure), Q8 ; 39 Q3, Q9 ; 40 Q1 (ex-Q3, d1),
  Q2 (ex-Q1), Q3 (ex-Q2, inchangée), Q8 (énoncé), Q9 (figure) ; 41 Q7, Q9. 41 Q2 inchangée (non appliquée).
- Réponses à l'aveugle notées AVANT lecture des clés (valeurs recalculées par sympy / Fraction) :
  36 Q2 d, Q6 d ; 37 Q2 c, Q3 b, Q4 {a, b}, Q7 c, Q9 b, Q10 c, Q11 a, Q12 d ; 38 Q1 c, Q4 d, Q8 d ; 39 Q3 a, Q9 a ;
  40 Q1 d, Q2 c, Q8 b, Q9 c ; 41 Q7 a, Q9 c.
- Rendu : moteur arena `origin/main` bffcca85 (avec #1154 — figure posée `dir="ltr"` — et #1160 — nombre suivi de π,
  d'une lettre grecque ou de « ° » isolé) ; `splitMathRuns` / `isDisplayEquation` / `isMathExpression` du moteur,
  SVG passés par DOMPurify avec la configuration de l'app, Chromium `dir="rtl"`, carte de 380 px ; ordre visuel de
  chaque glyphe relevé (Range API) contre le texte source ; captures inspectées à l'œil.
- Gates en lecture seule sur une copie de travail : corpus `origin/main` 18c8a7ac + les six fichiers, moteur bffcca85.

## Fichier 36 (11 questions, challenge d4 300/60, rampe 2,2,2,2,2,2,3,3,3,3,3) — OK

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q2 (`<title>` de la figure) | d (BCE) | d | OK |
| Q6 (option b, étiquette, explication) | d | d | OK |
| Q3 b (« 3 », étiquette ajoutée) | — (clé inchangée d) | d | OK |
| Q8 c (« 10,8 », étiquette retirée) | — (clé inchangée b) | b | OK |

- **Q2.** `<title>` « النقاط B و C و E والمنتصفان A و O » : ne nomme plus le triangle-clé ; aucune autre ligne du SVG
  n'a bougé (diff élément par élément).
- **Q6.** Plan 2×2 complet : appariement (CD × CB face à CE × BE, ou CD × BE face à CE × CB) × « ÷ 2 » présent ou non ;
  chaque facteur partagé 2–2, plus aucun vote terme à terme. Valeurs (B(−4 ; 0), C(4 ; 0), E(4 ; 6), CD = 24/5,
  BE = 10) : a 192/5 ≠ 60, b 192/5 ≠ 30, c 48 ≠ 24, d 48 = 48. Étiquettes : a `relation-aire-mauvais-cote`,
  c `aire-triangle-sans-moitie`, b (deux erreurs) muette, la clé non étiquetée. L'explication décrit chacun des trois
  chemins ; la coche ✓ suit la clé. Rendu Chromium : options gauche-à-droite, parenthèses à leur place.
- **Q3 b / Q8 c.** « 3 » (EC = OA) : la première phrase du libellé de `droite-des-milieux-facteur-deux` (« vaut la
  MOITIÉ du troisième côté ») corrige exactement ce chemin, que l'explication décrit (« اعتبار القطعتين متساويتين ») ;
  « 10,8 » (deux erreurs) est bien muette.

## Fichier 37 (12 questions, challenge d4 300/60, rampe 2,2,2,2,2,2,2,3,3,3,3,3) — défaut introduit (Q9, figure)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q2 (option b, explication, figure) | c | c | OK (écart de l'auteur fondé) |
| Q3 (énoncé « هل في هذا الحلّ خطأ ؟ … ») | b | b | OK |
| Q4 (multi : c et d raccourcies) | {a, b} | {a, b} | OK |
| Q5 (explication) | — (clé inchangée d) | d | OK |
| Q6 c (« 4√2 », étiquette ajoutée) | — (clé inchangée a) | a | OK |
| Q7 (option d, étiquette retirée, explication) | c | c | OK |
| Q9 (figure : trait de codage déplacé ; c étiquetée) | b | b | **défaut introduit (figure) — majeur** |
| Q10 (figure : étiquette « 4 ») | c | c | OK |
| Q11 (glose, option d, explication) | a | a | OK |
| Q12 (définition descriptive) | d | d | OK |

- **Q2.** b « …مستقيم يمرّ من منتصف قطعة… » est fausse (le milieu seul ne suffit pas) ; longueurs 52 / 66 / 62 / 62.
  Explication : l'auteur a retiré « O » de « المرور من المنتصف O » — juste : O n'est ni dans l'énoncé ni sur la figure
  de Q2. **Défaut de mon correctif** (je l'avais gardé de l'explication d'origine). Figure : `viewBox` 216 → 244,
  tout décalé de 28,35, le sommet de Δ (y = 34) passe au-dessus de P (y = 62,35) et l'étiquette « Δ » (174 ; 38) est
  dans le cadre ; mesure Chromium et `check-overflow` : aucun texte hors `viewBox`. Meilleur que mon `y="14"` : Δ
  nomme désormais visiblement la droite, plus le point P.
- **Q3.** L'énoncé n'impose plus d'erreur ; l'option d « لا يوجد خطأ » redevient une réponse possible. Explication
  inchangée et cohérente (étapes 1 et 3 justes, erreur en 2).
- **Q4.** a et b valides, c (« PA = PB ، إذن … ») et d (« (OP) عمودي على (AB) في O ، إذن … ») invalides ; longueurs
  47 / 58 / 33 / 50 : plus de partition par la forme. Aucune étiquette sur ce `multi`.
- **Q5.** « BM/BP = BO/BA » seul : la fuite vers Q6 (OM/AP = 1/2) a disparu.
- **Q6 c.** « 4√2 » (OM = AP) sous `droite-des-milieux-facteur-deux` : exact, même raisonnement qu'en 36 Q3 b.
- **Q7.** d « (AM) ⊥ (BP) » est fausse (AM·BP = −16) ; elle ne nie plus l'énoncé ; quatre options de 31 caractères ;
  le vote laisse b et c à égalité. Explication : le pied de la perpendiculaire issue de A sur (BP) est bien P
  (APB droit), donc « M … ليست المسقط العمودي للنقطة A عليه » est juste. d muette en attendant la nouvelle étiquette.
- **Q9 — [MAJEUR, introduit par la retouche de la figure].** Le trait simple de [OB] est passé de x = 223 (sur K,
  caché par (KH)) à x = 191,5, **milieu de [OK]**. Avec le trait de [AO] (x = 97, milieu de [AO]), la figure code
  désormais **AO = OK** : faux (126 px contre 63 px, soit 4 contre 2), et ce codage mène tout droit au distracteur
  a « 1/2 » (AK = 2 AO ⇒ AP/AH = AO/AK = 1/2, le chemin que l'explication décrit comme « اعتبار K هي B »). Mon audit
  signalait ce trait caché sans donner de texte de remplacement : l'auteur a improvisé. Correctif (chaque chaîne
  présente une fois ; copie rendue dans Chromium : aucun débordement, doubles traits de [PM] et [MB] intacts) :
  **supprimer les deux traits simples**
  `<path d="M97 228 L97 218" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/>` et
  `<path d="M191.5 228 L191.5 218" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/>`.
  « O منتصفها » est dit par l'énoncé, et [OB] n'a pas de place pour un trait visible : son milieu K porte (KH) et
  l'angle droit. Q9 c « 4/3 » sous `segment-mal-choisi` : exact (AB pris pour AO).
- **Q10.** « 4 » à x = 213,64 (je proposais 214) : détaché du trait de codage, lu « 4 ».
- **Q11.** Glose « (نقطة تلاقي ارتفاعاته) » : aucune option ne contient « ارتفاع » (le mot n'est que dans la question),
  donc pas d'appariement. d « …لأنّ PAB قائم في P و M من (PB) » porte la même double raison que la clé : l'indice
  « nombre de conditions » a disparu. d est fausse (AP·AM = 32 ≠ 0) ; longueurs 52 / 48 / 55 / 52. Explication juste.
- **Q12.** Glose descriptive « (النقطة التي تلتقي عندها المستقيمات الثلاثة المارّة من رؤوسه والعمودية على أضلاعه
  المقابلة) » : définition exacte, accords justes (pluriel non humain). Sans « ارتفاع », elle ne s'apparie pas au
  « الارتفاع » de d. Le seul mot commun, « عمودي », figure aussi dans c (« الموسّط العمودي »), si bien que l'appariement
  de surface pointe c autant que d. Pour choisir d, il faut reconnaître que (BN), qui passe par B et est perpendiculaire
  à (AM), est l'une des droites de la définition, et que c exige que N soit le milieu de [AM] (faux : milieu (−1 ; 1),
  N(16/5 ; 12/5)). R-3 réglé sans la ligne de cours (qui reste souhaitable, hors lot). L'énoncé fait cinq lignes sur
  une carte de 380 px mais reste lisible.

## Fichier 38 (9 questions, PASSÉ en boss d3 120/30, titre ⭐⭐⭐, rampe 1,2,2,2,2,2,3,3,3) — OK

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| en-tête boss d3 120/30, titre ⭐⭐⭐ | — | — | OK |
| Q1 (ex-Q2, d1 ; énoncé allégé, angle droit de la figure retiré) | c (8 − x) | c | OK |
| Q2 (ex-Q1, inchangée) | — (clé inchangée a) | a | OK |
| Q4 (énoncé allégé ; figure : [AE] tracé, angle droit en A retiré) | d (x(8 − x)/2) | d | OK |
| Q6 c (« (x + 4)² », étiquette ajoutée) | — (clé inchangée b) | b | OK |
| Q8 (option c, étiquette, explication) | d (0 < a ≤ 8) | d | OK (écart de l'auteur fondé) |

- **En-tête.** `difficulty: 3`, `mode: "boss"`, 120/30, « ⭐⭐⭐ » ; le reste du titre est inchangé. Une d1 en tête de
  boss d'examen est l'usage publié (09/19, 20, 21, 23, 24, 25, 27, 28, 29, 31, 32 s'ouvrent sur une d1). Trois vraies d3 sur neuf :
  honnête pour un boss (09/23 : 1 sur 8 ; 09/28 : 2 sur 8).
- **Q1.** « ABC مثلّث حيث AB = 8 » suffit (AF = AB − BF) ; plus de reprise de la clé de Q2 ; d1 justifiée (une
  soustraction). Figure sans codage d'angle droit, cohérente avec l'énoncé. Explication inchangée et juste.
- **Q4.** Énoncé autonome sans l'angle droit en A (l'aire vient de (EF) ⊥ (AB) et de EF = x, donnés). [AE] est tracé
  (vert, 2,4, comme [EF]) : le triangle AEF est enfin visible ; aucune étiquette touchée ([AE] passe à 25 px du « x »
  de [EF]). L'explication ne s'appuie que sur l'angle droit en F.
- **Q6 c.** `carre-difference-signes` : l'explication décrit le chemin (« إهمال إشارة الحدّ الأوسط ») que le libellé
  nomme. Exact.
- **Q8.** c « 0 < a ≤ 4 » est fausse (a = 8 pour x = 4 ; vérifié sur 799 valeurs de x) et d seule reste vraie.
  `reponse-a-l-autre-inconnue` (« l'autre inconnue ») est exact. Explication : ma fin « مع أنّ a = 8 عند x = 4 »
  livrait l'étape-clé de Q9 (x = 4, donc BF/AB = 1/2) : **défaut de mon correctif**, bien vu par l'auteur. Sa
  version, « أو الخلط بين المجهولين a و x فنعطي قيمة x حدًّا أعلى لـ a فنكتب a ≤ 4 ، مع أنّ a تبلغ 8 وهي أكبر من 4 »,
  ne nomme plus x = 4. Reste « والمساواة ممكنة حين ينعدم المربّع », indispensable pour justifier ≤ 8. C'est la
  première marche de Q9 : décomposition inhérente à l'enchaînement officiel 3b → 4a, acceptée comme les autres
  demi-étapes de la tranche.

## Fichier 39 (11 questions, challenge d4 300/60, rampe 2,2,2,2,2,2,2,3,3,3,3) — OK

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q3 (option d « 6/5 », étiquette, explication) | a (12/5) | a | OK |
| Q9 (définition descriptive ; queue commune retirée des options) | a | a | OK |

- **Q3.** d « 6/5 » (AB × CH = (AC × BC) ÷ 2, la moitié d'un seul côté) est fausse ; `aire-triangle-sans-moitie`
  est exact. L'explication décrit les trois chemins (15/4, 6/5, 6). Le contrôle du cours « العمودي أقصر من كلّ مائل »
  n'écarte plus que b (15/4) et c (6), car 6/5 < AC = 3 : il ne désigne plus la clé. Longueurs 4 / 4 / 1 / 3.
- **Q9.** Même glose descriptive qu'en 37 Q12. Le seul mot qu'elle partage avec les options, « عمودي », est dans les
  quatre (« فهو عمودي على (AF) ») et, en plus, dans c et d (« الموسّط العمودي ») : aucun appariement vers la clé. Le
  plan 2×2 (ارتفاع / الموسّط العمودي × قائم في K / في B) est intact. La queue commune « إذن K تنتمي إلى الدائرة التي
  قطرها [AB] », qui n'était que le but posé par la question, est retirée : options de 89 / 89 / 94 / 94 caractères.
  L'explication, inchangée, conclut toujours sur ce but. b garde `hypotenuse-mal-choisie` jusqu'à la livraison des
  nouvelles étiquettes ; d (deux erreurs) muette.
- Étage inchangé : 4 vraies d3 sur 11, honnête à la limite basse (moyenne 2,36).

## Fichier 40 (9 questions, challenge d4 300/60, rampe 1,2,2,2,2,3,3,3,3) — réserve mineure (étage à la limite)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (ex-Q3, passée d1) | d (6) | d | OK |
| Q2 (ex-Q1 ; option b « 1 », étiquette retirée, explication) | c (5) | c | OK |
| Q3 (ex-Q2, inchangée) | — (clé inchangée a) | a | OK |
| Q8 (énoncé « هل في هذا الحلّ خطأ ؟ … ») | b | b | OK |
| Q9 (figure : étiquettes « E » et « 2 ») | c (6/5 ; 8/5) | c | OK (écart de l'auteur fondé) |
| en-tête challenge d4 | — | — | réserve mineure |

- **Q1.** AD = 2 × OA = 6 : la d1 est honnête. Options et étiquettes inchangées (a « 3 », b « 3/2 » :
  `rayon-et-diametre-confondus`).
- **Q2.** Plan 2×2 (carrés ou non × somme ou différence) : 5, √7, 7, 1, chaque facteur 2–2. « 1 » (4 − 3, deux
  erreurs) est muette ; l'explication décrit les trois chemins. Le doublon avec 31 Q1 et 12/06 Q1 est rompu ({7, 1, 5,
  √7} contre {5, 7, 25, √7}, contexte différent). Paire de surface la plus proche : 09/33 Q2 à 0,46, autre question
  (recherche d'un côté de l'angle droit), pas un doublon.
- **Q8.** Énoncé neutre, cohérent avec l'option d ; explication inchangée et juste.
- **Q9.** « 2 » à (219,29 ; 175,57) : son centre est à 7,7 px de [EB], 28 px de [HB], 37 px de (EH), il se lit BE sans
  ambiguïté. Ma position (235 ; 155) tombait à 5,9 px de la ligne de cote de [OB] (de (63,92 ; 14,8) à
  (284,88 ; 180,51), y = 143,1 en x = 235), là où se lit le « 5 » : **défaut de mon correctif**, bien vu par l'auteur.
  « E » à (168,1 ; 147,43) : 16 px de E, 59 px de H. Aucun texte hors `viewBox`.
- **Étage.** Vraies d3 : 4 sur 9 (Q7, BF par le papillon après avoir retrouvé OE et BE, et Q8, la chasse à l'erreur,
  sont solides ; Q6 et Q9 moyennes). Q1 est une d1, Q2 et Q3 des d2 faciles. Moyenne 2,33, soit la plus basse des
  défis de la tranche, juste sous le plancher des défis publiés du chapitre (2,375 : 09/10, 09/11) et dans la plage
  des boss d'examen (2,11 à 2,5). Le contenu n'a pas changé depuis l'audit : la retouche d1 rend seulement l'étiquetage
  honnête. **Réserve mineure** : défi honnête de justesse ; un repli en boss d3 120/30 se défendrait aussi, je ne
  l'impose pas.

## Fichier 41 (10 questions, challenge d4 300/60, rampe 2,2,2,2,2,3,3,3,3,3) — OK · réserve mineure (Q2, au choix)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q7 (option b, explication) | a (MO = 2√5/5 ; MB = 4√5/5) | a | OK |
| Q9 (option d « 2/5 », étiquette, explication) | c (4/5) | c | OK |
| Q2 (non appliquée) | — (clé inchangée d) | d | réserve mineure : remplacement possible ci-dessous |

- **Q7.** b « MO = √5/2 ; MB = 3√5/4 » mène la méprise « partie sur tout » jusqu'au bout (MJ = √5/4, donc
  MB = √5 − √5/4). Deux options ont MB > MO (a, b) et deux MB = MO/2 (c, d) : le marqueur de forme a disparu.
  Longueurs 23 / 22 / 23 / 19. L'explication est juste ; l'ajout de l'auteur (« مع أنّ 1/4 نسبة جزء إلى الجزء الآخر
  وحصّة الجزء من الكلّ هي 1/5 أو 4/5 ») l'est aussi. Résidu connu, mineur : c et d donnent MO > OA = 2√5.
- **Q9.** d « 2/5 » ((8/5 ÷ 2) ÷ 2) est fausse ; `aire-triangle-sans-moitie` est exact. Le contrôle « العمودي أقصر من
  كلّ مائل » (MH < OM ≈ 0,894) n'écarte plus que a (8/5) et b (1).
- **Q2 — arbitrage (b).** Les options {20, 6, 2√3, 2√5} sont celles de 20/10 Q2 (même calcul √(2² + 4²), mêmes pièges).
  Les trois objections de l'auteur sont exactes : 4√5 recrée un vote (radicande 5 deux fois, coefficient 2 deux fois,
  clé à l'intersection) ; 4 et √6 tombent au contrôle du cours « الوتر أطول الأضلاع » ; 2 vaut OB. Mais un substitut
  échappe aux trois : **b « 6 » → « 3√2 »** (OA² = 2 + 16 = 18, OB non élevé au carré). Vérifié par script :
  3√2 ≈ 4,243 ≠ 2√5 ≈ 4,472 ; il est dans ]AB ; OB + AB[ = ]4 ; 6[, donc ni le contrôle du cours ni la figure à
  l'échelle ne l'écartent ; {20, 3√2, 2√3, 2√5} n'est plus l'ensemble de 20/10 Q2 ; longueurs 2 / 3 / 3 / 3 (clé non
  la plus longue) ; coefficients 3 / 2 / 2, radicandes 2 / 3 / 5 (le seul vote, sur le coefficient 2, existe déjà) ;
  3√2 n'apparaît nulle part ailleurs dans 41. Il améliore même la question : aujourd'hui les trois distracteurs
  tombent (2√3 au contrôle du cours ; 20 et 6, qui atteignent ou dépassent OB + AB, à vue sur la figure à l'échelle) ; après, 3√2 résiste. Étiquette :
  garder `math.geo.pythagore-sans-carres` (« Tu additionnes … les longueurs au lieu de leurs carrés » : ici la
  longueur OB). Explication : remplacer « أو جمع الطولين مباشرة فنكتب 2 + 4 = 6 » par « أو نسيان تربيع الطول OB
  فنكتب OA² = 2 + 16 = 18 أي OA = √18 = 3√2 ». Copie rendue dans Chromium : options gauche-à-droite ;
  « OA² = 2 + 16 = 18 » et « OA = √18 = 3√2 » mesurées gauche-à-droite (Range API). Doublon inter-chapitres (20
  et 09) : mineur, au choix de la livraison.

## Étiquettes

**Étiquettes existantes posées dans les fichiers** (relues en contexte) :
- retirées : 36 Q6 b, 36 Q8 c (options à deux erreurs), 37 Q7 d (option remplacée), 40 Q2 b (deux erreurs) ;
- ajoutées : 36 Q3 b et 37 Q6 c (`droite-des-milieux-facteur-deux`), 37 Q9 c (`segment-mal-choisi`), 38 Q6 c
  (`carre-difference-signes`) ;
- changées : 38 Q8 c (`reponse-a-l-autre-inconnue`), 39 Q3 d et 41 Q9 d (`aire-triangle-sans-moitie`).

Toutes sont exactes. Le décompte est inchangé (180 distracteurs étiquetables, 114 étiquetés, 66 muets). La clé n'est
jamais étiquetée, et rien n'est posé sur les `multi` 37 Q4 et 38 Q7. Toutes les étiquettes sont au registre
d'`origin/main`.

**Nouvelles étiquettes (`pending-tags/L14.json`).** Identifiants libres sur `origin/main` 18c8a7ac (855 étiquettes) ;
la compétence `math.geo.triangles-base` existe. Libellés fr et en : les miens, tels quels. Libellé ar
d'`angle-droit-mauvais-sommet` : « الرأس الخاطئ » remplace mon « الرأس الخطأ », meilleur choix (adjectif). Chaque
libellé nomme l'erreur exécutée.

Placements du lot (17 listés) :
- `angle-droit-mauvais-sommet`, exacts : 36 Q4 a et c (angle droit en B ou en E au lieu de C, le côté opposé pris
  pour hypoténuse en cohérence) ; 37 Q7 a et b (en B ou en A au lieu de N) ; 37 Q11 b (« قائم في P » lu comme
  (AP) ⊥ (AB)) ; 39 Q9 b (en B au lieu de K) ; 40 Q6 b (en A au lieu de E).
- **40 Q6 d (facultatif) : à ne pas poser.** O n'est pas un sommet du triangle ADE, et l'explication décrit c et d
  comme une confusion du diamètre [AD] avec le rayon [OE] (« الخلط بين القطر [AD] وشعاع الدائرة [OE] »). d reste muette,
  comme sa jumelle c.
- `droites-remarquables-confondues`, exacts : 36 Q5 a (médiane [CA] prise pour hauteur) ; 37 Q2 a (bissectrice pour
  médiatrice) ; 37 Q7 d (médiane pour hauteur) ; 37 Q12 a, b, c (hauteur prise pour médiane, bissectrice, médiatrice) ;
  39 Q9 c (hauteur pour médiatrice ; d, à deux erreurs, reste muette).
- 37 Q2 b et d : **acceptables**. Dans le triangle PAB de la figure, la droite issue de P par le milieu de [AB] est la
  médiane, et la perpendiculaire issue de P est la hauteur. La définition de la médiatrice donnée par le libellé
  (« perpendiculaire à un côté en son milieu ») corrige exactement la condition oubliée. `condition-suffisante-supposee`
  serait l'alternative stricte, mais son exemple et sa compétence portent sur les quadrilatères.

Soit 16 placements à faire, et un facultatif écarté.

Hors lot (12 listés, relus sur `origin/main` 18c8a7ac), tous exacts :
- `angle-droit-mauvais-sommet` : 20/02 Q2 b et c (angle droit en O, où (SO) ⊥ (OM)) ; 20/07 Q6 b (en B) ; 20/08
  Q3 b (en A) ; 20/24 Q4 d (en H) ; 18/03 Q2 b, facultatif (clause du cercle : I milieu de [BC] et IA = IB = IC, donc
  l'angle droit est en A).
- `droites-remarquables-confondues` : 09/25 Q3 b (pied de la hauteur pris pour un milieu), c (médianes prises pour
  hauteurs, une seule confusion dite deux fois), d (médianes prises pour médiatrices) ; 09/35 Q7 b (médiane prise
  pour hauteur), c (droite par le milieu prise pour médiatrice, comme 37 Q2 b) ; 20/18 Q5 b (médiane relative à
  l'hypoténuse prise pour hauteur ; `hauteur-confondue-avec-mediane` nomme le sens inverse).
- **Manquant (omission de mon audit, donc de la liste)** :
  `18-quadrilateres/exercices/25-examen-2016-technique-ex3-rectangle-parallelogramme-pythagore-thales-aire-echelle.json`
  Q1 d « المثلّث ADF قائم في A لأنّ ABCD مستطيل، و [DF] وتره، فنطبّق نظرية فيثاغورس » : angle droit mis en A au lieu
  de D (où DA ⊥ DF), et son explication le dit (« وضع الزاوية القائمة في A بحجّة أنّ ABCD مستطيل »). Elle porte
  aujourd'hui `hypotenuse-mal-choisie`, ce qui est inexact : à remplacer par `angle-droit-mauvais-sommet`.

Seuil de 3 questions distinctes : `angle-droit-mauvais-sommet` en a 5 dans le lot (36 Q4, 37 Q7, 37 Q11, 39 Q9, 40 Q6)
et 5 publiées (6 avec 18/03) ; `droites-remarquables-confondues` en a 5 dans le lot (36 Q5, 37 Q2, 37 Q7, 37 Q12,
39 Q9) et 3 publiées. Franchi dans les deux cas.

`hypotenuse-mal-choisie` garde des usages exacts :
- dans le lot après livraison : 38 Q2 b et c (réciproque), 38 Q3 c ([EF] pris pour hypoténuse de BFE), 39 Q2 d et
  39 Q11 d (√34), 40 Q2 d, 41 Q2 c, 41 Q8 c (réciproque) ;
- dans le publié : les 88 options `math` qui la portent sur `origin/main` ont été relues. Toutes sont des réciproques
  ou de vrais choix d'hypoténuse (09/09 Q4, 09/12 Q1, 09/17 Q2, 09/27 Q2 a, 09/32 Q2, 09/35 Q5, 12/02 Q4, 14/02 Q1,
  18/09 Q3, 18/14 Q4 d, 18/19 Q1, 20/03 Q6, 20/18 Q5 a, quiz 09 Q1-Q2…), sauf les cinq déjà listées (20/02 ×2, 20/07,
  20/08, 20/24) et 18/25 Q1 d ci-dessus.

Livraison : ajouter les deux entrées au registre dans le même commit que les placements (`content:qa` refuse une
étiquette non déclarée).

## Gates (lecture seule, copie de travail : corpus `origin/main` 18c8a7ac + les six fichiers, moteur bffcca85)

- `content:check` : vert (120 matières, 1 053 chapitres, 4 683 exercices, 28 412 questions ; 855 étiquettes).
- `content:qa --strict` : 0 erreur, code de sortie 0. 18 avertissements en `math`, aucun sur le chapitre 09.
- `content:tranche --changed` : la tranche est le chapitre 09 (325 questions, dont les 62).
  - Clé strictement la plus longue : 7 sur 317, aucune dans 36 à 41.
  - Positions de clé du chapitre : a 76, b 92, c 82, d 67.
  - 18 paires ≥ 0,45 : aucune ne touche 36 à 41 (toutes entre les missions publiées 01 à 05 du chapitre, deux
    avec le quiz de 14).
  - 0 candidat gabarit.
- Jaccard de surface, mesuré **sans** le filtre « figures identiques » de l'outil (qui n'apparie jamais deux énoncés à
  figures différentes) :
  - contre le publié, maximum 0,55 (39 Q2 et 09/33 Q2 : même gabarit 3-4-5, autre côté demandé, autres options),
    puis 0,47 (40 Q7 et 09/35 Q2) et 0,46 (40 Q3 et 09/35 Q1 ; 41 Q10 et 09/19 Q8 ; 40 Q2 et 09/33 Q2). Ces paires
    partagent le gabarit d'énoncé (« ونعلم أنّ الأطوال بالصنتمتر هي »), pas la tâche : pas de doublon ;
  - dans la tranche, maximum 0,78 (39 Q3 et Q4), 0,71 (39 Q10 et Q11), 0,69 (36 Q7 et Q8) : marches successives sur le
    même énoncé, décomposition déjà admise à l'audit.
- Dans la tranche : positions de clé des 60 questions à choix unique a 13, b 16, c 16, d 15 ; clé strictement la plus
  longue 0 sur 60 ; 249 options, 65 clés.
- `content:figures:check` : vert. `check-overflow`, lancé avec le Chromium 1194 local (le 1234 épinglé n'est pas
  installé) : calibration juste, 0 texte hors `viewBox` sur 56 figures.
- Rendu des 62 questions (énoncés, options, explications), ordre des glyphes mesuré : 0 inversion. Seules les chaînes
  purement numériques (« 3 + 4 = 7 ») et « 45° » ou « 90° » isolés suivent le sens de la phrase, comportement que
  `bidi.ts` déclare voulu.
- Réordonnancement de 38 et 40 : fichiers neufs, absents d'`origin/main`, donc aucun UUID déployé n'est re-calculé.

## Chiffre final

- 62 questions relues ; 21 questions touchées re-résolues à l'aveugle ; **0 clé fausse** ; 0 critique.
- **1 majeur introduit** : 37 Q9, la figure code AO = OK (trait de [OB] déplacé au milieu de [OK]). Il mène au
  distracteur 1/2 ; supprimer les deux traits simples.
- Les cinq écarts de l'auteur sont fondés :
  - 38 Q8, 40 Q9 et 37 Q2 (explication) corrigent **trois défauts de mes propres correctifs** : fuite de x = 4 vers
    Q9, étiquette posée sur la ligne de cote de [OB], « O » sans référent ;
  - la figure de 37 Q2 (cadre élargi) est meilleure que mon `y="14"` ;
  - les gloses descriptives de 37 Q12 et 39 Q9 ne désignent pas la clé par appariement de mots.
- Mon audit portait aussi la note cosmétique de 37 Q9 sans texte de remplacement : c'est d'elle qu'est né le défaut
  introduit.
- Réserves mineures :
  - 40 : défi honnête de justesse (moyenne 2,33), repli boss défendable, non imposé ;
  - 41 Q2 : remplacement vérifié proposé (b « 6 » → « 3√2 » et une phrase d'explication), au choix ;
  - étiquettes : ne pas poser 40 Q6 d ; ajouter 18/25 Q1 d hors lot.
- Étages : 36 (5 d3 sur 11), 37 (5 sur 12), 41 (5 sur 10) honnêtes ; 39 (4 sur 11) honnête à la limite basse ; 38 en
  boss d3 honnête ; rampes croissantes ; aucune explication ne renvoie à une question déplacée.
- **Verdict : livrable après le correctif de 37 Q9** (deux lignes à retirer du SVG).
